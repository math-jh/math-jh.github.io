#!/usr/bin/env python3
"""term_extract_worker.py — 찾아보기(terms.yml) 용어 추출 cron 워커 (v2).

2026-07-20 재작성 (구 extract_terms.py 는 terms.yml 개편 전 설계라 폐기,
정의 마커 파서·upsert 부품만 import 해 재사용). 설계 원칙 = 안전 우선:
terms.yml 은 오염되면 바로잡기 어려우므로 **LLM 은 terms.yml 을 절대 직접
쓰지 않는다**. LLM 은 JSON 제안만 내고, 결정론적 applier 가 전 항목을
검증(스키마·중복·url 실재·primary 실측)한 뒤 쓰기 게이트(파싱·항목수·
semantic_checks 비악화)를 통과해야만 원자적으로 쓴다. 실패는 글 단위
격리(3회 → 7일 quarantine + notify 알림).

틱마다 (cron :00/:30) 글 하나:
  선정 (스크립트만, LLM 무관 — 매칭 없어도 로그 한 줄은 남긴다):
    0. 한 번도 안 돌린 글 (path 순)          — published:false 포함
    1. 마지막 검사 후 translation worker 가 재번역한 글 (재번역 = 한때
       drift_needed = 내용 변경 = 새 용어 가능성↑), 오래된 번역부터
    2. 마지막 검사가 14일 지났고 **그 뒤에 실제로 바뀐** 글, 오래된 검사부터
       (안 바뀐 글은 다시 넣어도 같은 답이 나온다)
    3. 전부 비면: 하루 1회만 terms.yml 자체 감사 (글자 하나씩 순환,
       각 항목의 sees 보강)
  처리:
    - 정의 마커(*en<sub>ko</sub>* 등)는 결정론 파싱 (extract_terms 재사용).
      · 색인에 없는 마커 → 신규 항목 (defs = 이 글[#앵커])
      · 색인에 있는데 이 글이 defs 에 없는 마커 → LLM 이 동음이의/뉘앙스
        판정 → add_def 또는 skip
    - (2)로 들어온 글은 추가로 LLM 이 '주요 사용 용어'를 추출, 색인에 없는
      것만 후보 목록(그 용어가 실제 등장하는 글들)을 주고 논리적으로 가장
      앞선 글을 defs 로 고르게 한다.
    - primary 는 LLM 을 믿지 않는다: usage_dominance 실측 → 유의하면 실측,
      아니면 정의 마커의 주표기(그마저 없으면 en — 블로그 확정 정책).
    - 필수 필드: id(slugify_id 로 생성, LLM id 불신)·en·ko·primary·defs 1+.
      ko 를 모르는 후보는 추가하지 않고 리뷰 파일로.
    - sees: 제안된 관련어 중 실존 항목만 (label 은 대상 항목에서 파생).
  변경은 자기 이름으로 커밋한다 (scripts/lib/cron_commit.py — `cron(term-extract):`,
  push 는 autopush 몫). 텔레그램은 문제일 때만 — 3회 연속 실패 → 격리.

사용: term_extract_worker.py [--dry-run] [--status] [--audit-letter X]
cron: 0,30 * * * * cd .../scripts/term-extraction && python3 term_extract_worker.py >>term_extract_worker.log 2>&1
"""
from __future__ import annotations

import argparse
import fcntl
import json
import os
import re
import shutil
import subprocess
import sys
import time
from datetime import datetime
from pathlib import Path

SCRIPT_DIR = Path(__file__).resolve().parent
BLOG_ROOT = SCRIPT_DIR.parents[1]
sys.path.insert(0, str(SCRIPT_DIR))

from terms_common import (  # noqa: E402
    GEN_ED_CATS, TERMS_PATH, category_ko_maps, chunk_field, chunk_id,
    ko_forms, ko_primary,
    dedup_key, insert_sorted, join_file, letter_of, normalize_proper_case,
    permalink_map, semantic_checks, slugify_id, split_file, url_slug,
    yaml_quote,
)
from extract_terms import (  # noqa: E402
    classify_definitions, add_def_to_chunk, parse_frontmatter,
    strip_frontmatter,
)
from terms_lint import send_notify, _defs_block  # noqa: E402
from usage_dominance import count_term, dominance  # noqa: E402
import gloss_stage  # noqa: E402
import yaml  # noqa: E402

sys.path.insert(0, str(BLOG_ROOT / "scripts/lib"))
from cron_commit import commit_outputs, dirty_paths  # noqa: E402

STATE_PATH = SCRIPT_DIR / "term_extract_worker_state.json"
LOCK_PATH = Path("/tmp/term-extract-worker.lock")
REVIEW_PATH = SCRIPT_DIR / "term_extraction_review.md"
BACKUP_PATH = SCRIPT_DIR / "terms.yml.bak-extract"
# 자기 산출물을 자기가 커밋한다 (cron_commit). 레포 상대 경로가 pathspec 이다.
REL_TERMS = str(TERMS_PATH.relative_to(BLOG_ROOT))
REL_REVIEW = str(REVIEW_PATH.relative_to(BLOG_ROOT))

LLM_BIN = os.environ.get("TERM_EXTRACT_LLM",
                         str(Path.home() / ".local/bin/claude"))
# term_extract 는 결정적 JSON 추출이라 haiku 로 충분하고 20x 헤드룸에서 사실상
# 공짜다 (GLM 구독 은퇴 대비). 단 `claude -p` 는 세션 기본 모델(현재 opus)을
# 쓰므로 --model 을 명시하지 않으면 opus 로 과금된다 — TERM_EXTRACT_MODEL 로
# 강제한다. GLM 롤백: TERM_EXTRACT_LLM=claudeglm TERM_EXTRACT_MODEL= (빈 값).
LLM_MODEL = os.environ.get("TERM_EXTRACT_MODEL", "haiku")
LLM_TIMEOUT = 600
STALE_SEC = 14 * 24 * 3600
QUARANTINE_FAILS = 3
QUARANTINE_SEC = 7 * 24 * 3600
MIN_BODY_CHARS = 300
MAX_SEE_PER_AUDIT = 10
MAX_NEW_TERMS_PER_POST = 12   # 폭주 상한 — 넘으면 초과분은 리뷰로

_lock_fh = None


def log(msg: str) -> None:
    print(f"[{datetime.now():%Y-%m-%d %H:%M:%S}] {msg}")


def acquire_lock() -> bool:
    global _lock_fh
    _lock_fh = open(LOCK_PATH, "w")
    try:
        fcntl.flock(_lock_fh, fcntl.LOCK_EX | fcntl.LOCK_NB)
        return True
    except OSError:
        return False


# ---------------------------------------------------------------------------
# state
# ---------------------------------------------------------------------------

def load_state() -> dict:
    if STATE_PATH.exists():
        try:
            return json.loads(STATE_PATH.read_text(encoding="utf-8"))
        except (OSError, json.JSONDecodeError):
            pass
    return {"posts": {}, "audit": {"letter": "A"}}


def save_state(state: dict) -> None:
    tmp = STATE_PATH.with_suffix(".tmp")
    tmp.write_text(json.dumps(state, ensure_ascii=False, indent=1),
                   encoding="utf-8")
    tmp.replace(STATE_PATH)


# ---------------------------------------------------------------------------
# 글 선정 (LLM 무관)
# ---------------------------------------------------------------------------

def all_ko_posts() -> list[str]:
    out = []
    for p in sorted(BLOG_ROOT.glob("_posts/Math/**/ko/*.md")):
        out.append(str(p.relative_to(BLOG_ROOT)))
    return out


def ko_commit_ts() -> dict[str, float]:
    """rel → 그 글이 마지막으로 커밋된 시각. stale 재검사 게이트용.

    전체 히스토리를 한 번에 훑는다 (실측 0.35s, 경로 1000여 개). 글마다
    `git log` 를 부르면 600 회 프로세스 기동이라 틱 예산을 먹는다.
    """
    p = subprocess.run(
        ["git", "log", "--name-only", "--pretty=format:%ct", "--", "_posts"],
        cwd=str(BLOG_ROOT), capture_output=True, text=True)
    out: dict[str, float] = {}
    if p.returncode != 0:
        log("경고: git log 실패 — stale 게이트 없이 진행")
        return out
    ts = 0.0
    for ln in p.stdout.splitlines():
        if not ln:
            continue
        if ln.isdigit():
            ts = float(ln)
        elif ts and ln not in out:   # 최신 커밋이 먼저 나온다
            out[ln] = ts
    return out


def load_translation_ts() -> dict[str, float]:
    """rel path → 마지막 번역 완료 시각 (status done 만).

    스키마(files/status/last_attempt_ts)의 정본은 생산자
    scripts/translation/translate_worker.py 다 (이중 SoT 감사 [U1], 2026-07-22).
    키가 개명되면 이 함수는 빈 결과로 조용히 강등되므로, 파일은 있는데 아는
    키가 하나도 없으면 스키마 변경으로 보고 경고를 남긴다 (우선순위 기능만
    무뎌질 뿐 치명적이지 않아 하드 실패는 하지 않는다)."""
    p = BLOG_ROOT / "scripts/translation/translation_state.json"
    try:
        files = json.loads(p.read_text(encoding="utf-8")).get("files", {})
    except (OSError, json.JSONDecodeError):
        return {}
    if files and not any(isinstance(v, dict) and "status" in v for v in files.values()):
        log("경고: translation_state.json 에 status 키가 없음 — 생산자"
            "(translate_worker) 스키마가 바뀐 듯. 번역 연동 우선순위 비활성.")
    return {rel: v.get("last_attempt_ts", 0.0)
            for rel, v in files.items() if v.get("status") == "done"}


def select_post(state: dict) -> tuple[str | None, str]:
    """(rel, kind) — kind ∈ first|drift|stale. 없으면 (None, '')."""
    now = time.time()
    posts = all_ko_posts()
    st = state["posts"]

    def ok(rel: str) -> bool:
        q = st.get(rel, {}).get("quarantined_until", 0)
        return q <= now

    never = [r for r in posts if "last_checked" not in st.get(r, {}) and ok(r)]
    if never:
        return never[0], "first"

    trans = load_translation_ts()
    drift = [(trans[r], r) for r in posts
             if r in trans and ok(r)
             and trans[r] > st.get(r, {}).get("last_checked", 0)]
    if drift:
        return sorted(drift)[0][1], "drift"

    # stale 재검사는 **글이 마지막 검사 뒤에 실제로 바뀐 경우만** 한다. 안 바뀐 글을
    # 14 일마다 다시 LLM 에 넣어 봐야 같은 답이 나온다 — 2026-08-10 에 1 차 수확이
    # 끝나면서 그 재검사가 하루 43 회 헛돌 예정이었다. 커밋 시각이 없는 글(gitignore
    # 된 Mirror_Symmetry 등)은 파일 mtime 으로 판단한다.
    git_ts = ko_commit_ts()

    def changed_since(rel: str, since: float) -> bool:
        ts = git_ts.get(rel)
        if ts is None:
            try:
                ts = (BLOG_ROOT / rel).stat().st_mtime
            except OSError:
                return False
        return ts > since

    stale = [(st[r]["last_checked"], r) for r in posts
             if r in st and ok(r)
             and now - st[r].get("last_checked", now) > STALE_SEC
             and changed_since(r, st[r].get("last_checked", now))]
    if stale:
        return sorted(stale)[0][1], "stale"
    return None, ""


# ---------------------------------------------------------------------------
# LLM 호출 (JSON 제안만 — terms.yml 접근 없음)
# ---------------------------------------------------------------------------

def call_llm(prompt: str) -> str:
    args = [LLM_BIN, "-p", "--output-format", "text"]
    if LLM_MODEL:
        args += ["--model", LLM_MODEL]
    # 2026-08-08: ~/.claude/settings.json 에 advisorModel(fable)이 전역 기본값으로
    # 들어갔다. advisor 부착 조건이 base_rank <= advisor_rank 라서 haiku(rank 1)로
    # 도는 이 워커도 조건을 만족해 Fable 상담이 붙는다 — 30분마다, 하루 48회.
    # 이 워커는 기계적 용어 추출이라 상위 모델 상담이 필요 없으므로 끈다.
    # 끄는 방법은 이 env 뿐이다: `--advisor <더 약한 모델>`은 base rank 에 따라
    # 켜지기도 하고, rank 1 인 haiku 는 advisor 값으로 아예 거부당한다(실측).
    env = {**os.environ, "CLAUDE_CODE_DISABLE_ADVISOR_TOOL": "1"}
    # 첫 user 메시지를 리터럴 `[cron]` 으로 시작시킨다 — 세션 트랜스크립트
    # 리퍼가 봇 턴을 식별하는 단일 규약. 프롬프트 문구가 바뀌어도 이 접두사만
    # 지키면 리퍼는 그대로다. JSON 만 출력하라는 지시와 섞이지 않도록 단독 줄로.
    proc = subprocess.run(
        args,
        input="[cron]\n\n" + prompt, capture_output=True, text=True,
        timeout=LLM_TIMEOUT, cwd="/tmp", env=env,
    )
    if proc.returncode != 0:
        raise RuntimeError(f"LLM exited {proc.returncode}: "
                           f"{proc.stderr.strip()[:300]!r}")
    return proc.stdout


def _json_values(text: str) -> list:
    """text 에 담긴 top-level JSON 값을 앞에서부터 전부 뽑는다.

    haiku 는 N 개 항목을 한 배열로 달라는 프롬프트(NUANCE·GLOSS_GATE·PICKDEF)에
    항목마다 배열을 하나씩 내놓는 일이 잦다. `\\[.*\\]|\\{.*\\}` 를 greedy·DOTALL
    로 잡으면 첫 `[` 부터 마지막 `]` 까지 통째로 삼켜 json.loads 가 "Extra data"
    로 죽는다 — 로그의 파싱 실패 44 건 중 39 건이 `line 4 (char 32|35)`, 즉 3 줄
    짜리 첫 배열 직후 두 번째 배열이 시작하는 지점이었다. 그래서 정규식으로
    한 덩어리를 집는 대신 raw_decode 로 값을 하나씩 훑는다.
    """
    dec = json.JSONDecoder()
    vals: list = []
    i, n = 0, len(text)
    while i < n:
        if text[i] not in "[{":
            i += 1
            continue
        try:
            val, end = dec.raw_decode(text, i)
        except ValueError:
            i += 1
            continue
        vals.append(val)
        i = end
    return vals


_RETRY_NOTE = ("\n\n(직전 응답이 JSON 으로 파싱되지 않았다. 설명도 코드펜스도 없이 "
               "요청한 배열 **하나만** 출력하라.)")


def llm_json(prompt: str):
    """LLM 을 불러 JSON 을 받는다. 파싱이 깨지면 한 번만 다시 묻는다.

    재시도는 파싱 실패에만 건다 — 쿼터 게이트나 CLI 비정상 종료는 다시 물어도
    같은 결과이고, 이 워커는 주간 쿼터를 이미 자주 태운다(로그의 blocked 194 틱).
    """
    last: Exception | None = None
    for attempt in (0, 1):
        if attempt:
            # 재시도가 실제로 얼마나 구제하는지 로그에 남긴다 — 조용히 다시
            # 물으면 파싱 실패가 줄었는지 늘었는지 알 방법이 없다.
            log(f"JSON 파싱 실패 → 재질의: {last}")
        out = call_llm(prompt if attempt == 0 else prompt + _RETRY_NOTE)
        out = re.sub(r"```(?:json)?", "", out)
        vals = _json_values(out)
        if not vals:
            last = RuntimeError(f"LLM 출력에서 JSON 을 못 찾음: {out[:200]!r}")
            continue
        if len(vals) == 1:
            return vals[0]
        # 값이 여럿이면 항목당 배열 하나씩 낸 경우다 — 배열만 골라 이어붙인다.
        lists = [v for v in vals if isinstance(v, list)]
        if lists:
            merged: list = []
            for v in lists:
                merged.extend(v)
            return merged
        last = RuntimeError(f"top-level JSON 값이 {len(vals)}개인데 배열이 없다")
    raise last


# ---------------------------------------------------------------------------
# 글 처리
# ---------------------------------------------------------------------------

_HANGUL_RE = re.compile(r"[가-힣]")


def post_meta(rel: str) -> tuple[str, str, str]:
    """(title, permalink, label). label 은 '[카테고리 ko] §제목'."""
    text = (BLOG_ROOT / rel).read_text(encoding="utf-8")
    fm = parse_frontmatter(text)
    title = fm.get("title", "").strip("'\"")
    permalink = fm.get("permalink", "").rstrip("/")
    ko_by_slug, _ = category_ko_maps()
    cat = ko_by_slug.get(url_slug(permalink) or "", "")
    if not (title and permalink and cat):
        raise RuntimeError(f"frontmatter 불완전: {rel} "
                           f"(title={title!r} permalink={permalink!r} cat={cat!r})")
    return title, permalink, f"[{cat}] §{title}"


def entry_index(groups: dict[str, list[str]]) -> dict[str, tuple[str, int]]:
    """dedup_key(en|ko) → (letter, chunk 위치)."""
    idx = {}
    for letter, chunks in groups.items():
        for i, c in enumerate(chunks):
            # ko 는 쉼표로 구분된 복수 한국어형을 담을 수 있으므로 이형마다 건다
            forms = [chunk_field(c, "en") or ""]
            forms += ko_forms(chunk_field(c, "ko"))
            for f in forms:
                k = dedup_key(f)
                if k:
                    idx.setdefault(k, (letter, i))
    return idx


def _defs_cats(chunk: str) -> set[str]:
    """entry 청크의 defs 대상 카테고리 슬러그 집합 (refs/see는 제외)."""
    blk = _defs_block(chunk)
    if not blk:
        return set()
    cats = set()
    for it in blk[2]:
        m = re.search(r"^\s*url: /ko/math/([^/#\s]+)", it, re.M)
        if m:
            cats.add(m.group(1))
    return cats


def _gen_ed_promotion(chunk: str, my_cat: str | None) -> bool:
    """교양수학 예외 (2026-07-21 룰링): 기존 defs가 전부 교양(calculus/
    linear_algebra)이고 현재 글이 전공 글이면, 이 글의 정의는 '정식 거처'로서
    뉘앙스 판정 없이 defs에 추가한다."""
    dcats = _defs_cats(chunk)
    return bool(dcats) and dcats <= GEN_ED_CATS \
        and my_cat is not None and my_cat not in GEN_ED_CATS


def decide_primary(en: str, ko: str, marker_primary: str | None) -> str:
    n_en, n_ko, verdict = dominance(en, ko)
    if verdict in ("en", "ko"):
        return verdict
    return marker_primary if marker_primary in ("en", "ko") else "en"


def build_entry(en: str, ko: str, primary: str, label: str, url: str,
                see_ids: list[tuple[str, str, str]]) -> str:
    """see_ids: (id, label, primary) — 대상 항목에서 파생."""
    en = normalize_proper_case(en)  # 인명 파생 고유명사 대문자 교정 (id 는 소문자 유지)
    lines = [f"- id: {slugify_id(en)}",
             f"  en: {yaml_quote(en)}",
             f"  ko: {yaml_quote(ko)}",
             f"  primary: {primary}",
             "  defs:",
             f"  - label: {yaml_quote(label)}",
             f"    url: {url}"]
    if see_ids:
        lines.append("  see:")
        for sid, slabel, sprim in see_ids:
            lines.append(f"  - label: {yaml_quote(slabel)}")
            if sprim == "ko":
                lines.append("    lang: ko")
            lines.append(f"    id: {sid}")
    return "\n".join(lines)


def see_tuple(chunk: str) -> tuple[str, str, str]:
    en = chunk_field(chunk, "en") or ""
    ko = chunk_field(chunk, "ko") or ""
    prim = chunk_field(chunk, "primary") or "en"
    label = ko_primary(ko) if prim == "ko" else (en[:1].upper() + en[1:])
    return chunk_id(chunk), label, prim


def add_see_to_chunk(chunk: str, target: tuple[str, str, str]) -> str | None:
    """see 에 대상 추가. 이미 있으면 None. 대상 (id, label, primary)."""
    sid, slabel, sprim = target
    if re.search(rf"^    id: {re.escape(sid)}$", chunk, re.M):
        return None
    block = [f"  - label: {yaml_quote(slabel)}"]
    if sprim == "ko":
        block.append("    lang: ko")
    block.append(f"    id: {sid}")
    lines = chunk.split("\n")
    if not any(ln.startswith("  see:") for ln in lines):
        return "\n".join(lines + ["  see:"] + block)
    return "\n".join(lines + block)  # see: 는 항목 마지막 필드


def review_note(lines: list[str]) -> None:
    if not lines:
        return
    with open(REVIEW_PATH, "a", encoding="utf-8") as f:
        f.write(f"\n## term_extract_worker {datetime.now():%Y-%m-%d %H:%M}\n\n")
        f.writelines(f"- {ln}\n" for ln in lines)


NUANCE_PROMPT = """수학 블로그 찾아보기 색인 관리 작업이다. 도구를 쓰지 말고 JSON 만 출력하라.

아래 각 항목은 (기존 색인 항목, 이번 글의 정의 문맥) 쌍이다. 이번 글이 같은
개념을 다시 정의/복습하는 것이면 "skip", 동음이의어이거나 뉘앙스·문맥이 달라
색인에서 두 정의처를 모두 보여줄 가치가 있으면 "add_def" 로 판정하라.

출력: [{"i": <번호>, "verdict": "add_def"|"skip"}] 만.

"""

MAJOR_PROMPT = """수학 블로그 찾아보기 색인 관리 작업이다. 도구를 쓰지 말고 JSON 만 출력하라.

아래 글에서 **주요하게 사용되는 수학 용어**를 최대 10개 추출하라. 이 글에서
정의했는지는 무관하다. 찾아보기 색인에 실릴 가치가 있는 개념어만 — 일반어·
조사·인명 단독은 제외. 각 용어의 영어형과 한국어형을 함께 적되, 한국어형을
모르면 ko 를 "" 로 두라. 인명 파생 형용사·고유명사(Hermitian, Noetherian,
Gaussian, Euler, Cauchy, Möbius 등)는 반드시 대문자로 표기하라 — 단
abelian 처럼 관용적으로 소문자인 형용사는 소문자 그대로 둔다.

출력: [{"en": "...", "ko": "..."}] 만.

--- 글 ---
"""

GLOSS_PICK_PROMPT = """수학 블로그 찾아보기 색인 관리 작업이다. 도구를 쓰지 말고 JSON 만 출력하라.

정의 문맥과 KMS 수학용어집의 한글 후보 목록이 주어진다. 이 문맥에 맞는 후보의
번호(0부터)를 고르라. KMS 는 전 분야 용어집이라 다른 분야의 동음이의어 번역이
섞여 있을 수 있다. 어느 후보도 이 문맥의 수학적 의미와 맞지 않으면 "NONE".
**후보에 없는 번역을 만들지 말 것** — 출력은 번호 선택 또는 "NONE" 만 유효하다.

출력: [{"pick": <번호>|"NONE"}] 만.

"""

GLOSS_GATE_PROMPT = """수학 블로그 찾아보기 색인 관리 작업이다. 도구를 쓰지 말고 JSON 만 출력하라.

정의 문맥, 영어 용어, KMS 수학용어집에서 exact match 로 얻은 한국어 병기 후보가
주어진다. 이 병기가 **이 문맥의 수학적 의미**와 일치하는지 판정하라. KMS 는 전
분야 용어집이라 교차 분야 동음이의어가 섞인다 — 예: reducible 의 KMS 표제
'약분가능'은 분수(fraction) 문맥의 뜻이고, 환론·표현론 문맥의 reducible 은
'가약'이다. 이런 분야 불일치가 보이면 "no", 확신이 서지 않으면 "unsure",
문맥과 일치할 때만 "yes".

출력: [{"verdict": "yes"|"no"|"unsure"}] 만.

"""

PICKDEF_PROMPT = """수학 블로그 찾아보기 색인 관리 작업이다. 도구를 쓰지 말고 JSON 만 출력하라.

아래 각 용어에 대해, 그 용어가 실제 등장하는 글 후보 목록이 주어진다.
색인의 defs(정의처)로 삼을, **논리적으로 가장 앞선**(그 개념이 처음 정의·
도입되는) 글의 번호를 고르라. 어떤 후보도 정의처로 적절치 않거나 색인에
실을 가치가 없으면 "skip".

출력: [{"term": "<en>", "pick": <후보 번호>|"skip"}] 만.

"""


def process_post(rel: str, kind: str, dry: bool) -> list[str]:
    """변경 요약 리스트 반환 (빈 리스트 = 변경 없음)."""
    text = (BLOG_ROOT / rel).read_text(encoding="utf-8")
    body = strip_frontmatter(text)
    if len(body) < MIN_BODY_CHARS:
        log(f"stub 건너뜀: {rel}")
        return []
    title, permalink, label = post_meta(rel)

    terms_text = TERMS_PATH.read_text(encoding="utf-8")
    header, groups = split_file(terms_text)
    idx = entry_index(groups)

    changes: list[str] = []
    review: list[str] = []
    adds: list[tuple[str, str]] = []      # (letter, entry_chunk)
    def_adds: list[tuple[str, int, str]] = []  # (letter, pos, url)

    # --- 1. 정의 마커 (결정론) ---
    definite, _ambig = classify_definitions(body)
    new_markers, known_markers = [], []
    for d in definite:
        k = dedup_key(d["english"]) or dedup_key(d["korean"])
        if k in idx:
            known_markers.append((d, idx[k]))
        else:
            new_markers.append(d)

    for d in new_markers[:MAX_NEW_TERMS_PER_POST]:
        en, ko = d["english"], d["korean"]
        if not en or not _HANGUL_RE.search(ko):
            review.append(f"{rel}: 마커 쌍 불완전 en={en!r} ko={ko!r} — 보류")
            continue
        lt = letter_of(en)
        if not lt:
            review.append(f"{rel}: 라틴 글자 없는 en={en!r} — 보류")
            continue
        url = permalink + (f"#{d['anchor']}" if d.get("anchor") else "")
        prim = decide_primary(en, ko, d.get("primary"))
        adds.append((lt, build_entry(en, ko, prim, label, url, [])))
        changes.append(f"신규 {en!r}({prim}) ← {url}")
    for d in new_markers[MAX_NEW_TERMS_PER_POST:]:
        review.append(f"{rel}: 상한 초과 신규 후보 {d['english']!r} — 보류")

    # --- 1.5 병기 상시 단계 (2026-07-21 배선; 일회성 소급은 gloss_backfill) ---
    # 정의 박스의 무병기 영어 이탤릭 중 **색인에 없는 신규 용어만** 병기한다.
    # 색인에 있는 용어의 무병기 이탤릭은 의도적 재사용(사용자 룰링 확정) —
    # 절대 건드리지 않는다. 병기는 KMS exact 후보 안에서만 (임의 번역 금지).
    if os.environ.get("GLOSS_STAGE", "1") != "0":
        _skips = gloss_stage.skip_terms()
        _pend = gloss_stage.pending()
        _my_cat = url_slug(permalink)
        # (occ, gloss, 기존 entry (lt,pos)|None) — None이면 신규 등록
        gloss_todo: list[tuple[dict, str, tuple | None]] = []
        for occ in gloss_stage.detect_unglossed(text):
            gterm = occ["term"]
            gk = dedup_key(gterm)
            if not gk or gterm.lower() in _skips or gterm.lower() in _pend:
                continue
            if gk in idx:
                # 색인 기존 용어의 무병기 이탤릭 = 의도적 재사용 → 불간섭.
                # 예외(교양 룰링): defs가 전부 교양수학이고 이 글이 전공 글이면
                # 정식 거처 — entry의 확립된 ko로 병기하고 defs에 추가한다.
                _lt, _pos = idx[gk]
                _chunk = groups[_lt][_pos]
                _eko = ko_primary(chunk_field(_chunk, "ko"))
                if _gen_ed_promotion(_chunk, _my_cat) and _eko:
                    gloss_todo.append((occ, _eko, (_lt, _pos)))
                continue
            verdict, val = gloss_stage.decide(gterm)
            if verdict == "auto":
                # KMS exact 단일 매치도 교차 분야 동음이의어일 수 있다
                # (2026-07-21 룰링: backfill 8/45 오병기, 예: 환론 문맥의
                # reducible 에 분수 뜻 '약분가능'). haiku 게이트가 yes 일
                # 때만 자동 적용, no/unsure/호출 실패는 전부 리뷰로 회부
                # (fail-to-review).
                ctx = text[occ["box_start"]:occ["box_end"]][:400]
                try:
                    g = llm_json(
                        GLOSS_GATE_PROMPT
                        + f"용어: {gterm}\n병기 후보: {val}"
                        + f"\n\n--- 정의 문맥 ---\n{ctx}")
                    gv = g[0].get("verdict") \
                        if g and isinstance(g[0], dict) else None
                except Exception as e:  # noqa: BLE001 — fail-to-review
                    gv = f"호출 실패 {str(e)[:100]}"
                if gv != "yes":
                    verdict, val = "review", \
                        f"게이트 {gv}: KMS 단일 후보 {val!r} 자동 적용 보류"
            elif verdict == "pick":
                ctx = text[occ["box_start"]:occ["box_end"]][:400]
                try:
                    picks = llm_json(
                        GLOSS_PICK_PROMPT
                        + f"용어: {gterm}\n후보: {val}\n\n--- 정의 문맥 ---\n{ctx}")
                    sel = picks[0].get("pick") \
                        if picks and isinstance(picks[0], dict) else None
                except Exception as e:  # noqa: BLE001 — fail-to-review
                    sel = f"호출 실패 {str(e)[:100]}"
                if isinstance(sel, int) and 0 <= sel < len(val):
                    verdict, val = "auto", val[sel]
                elif isinstance(sel, str) and sel.strip().upper() == "NONE":
                    verdict, val = "review", \
                        f"KMS 복수 후보 {val} — 어느 것도 문맥 불일치(NONE)"
                else:
                    verdict, val = "review", \
                        f"KMS 복수 후보 {val} — 선택 보류 ({sel!r})"
            if verdict == "auto":
                gloss_todo.append((occ, val, None))
            else:
                review.append(f"{rel}: 병기 필요 {gterm!r} — {val}")
                gloss_stage.mark_pending(gterm, str(val))
        if gloss_todo:
            cur = text
            for occ, gloss, entry_at in gloss_todo:
                # 앞선 적용으로 span이 밀리므로 용어별 재탐지 후 적용
                fresh = {o["term"].lower(): o
                         for o in gloss_stage.detect_unglossed(cur)}
                o = fresh.get(occ["term"].lower())
                nt = gloss_stage.apply_gloss(cur, o, gloss) if o else None
                if nt is None:
                    review.append(f"{rel}: 병기 적용 실패 {occ['term']!r} — 보류")
                    continue
                cur = nt
                gurl = permalink + (f"#{occ['anchor']}" if occ.get("anchor") else "")
                if entry_at is not None:
                    # 교양 예외 경로: 기존 entry에 정식 거처 def 추가
                    def_adds.append((entry_at[0], entry_at[1], gurl))
                    changes.append(
                        f"병기+defs(정식 거처) {occ['term']!r}<{gloss}> ← {gurl}")
                    continue
                glt = letter_of(occ["term"])
                if glt:
                    prim = decide_primary(occ["term"], gloss, "en")
                    adds.append((glt, build_entry(
                        occ["term"], gloss, prim, label, gurl, [])))
                changes.append(f"병기+신규 {occ['term']!r}<{gloss}> ← {gurl}")
            if cur != text and not dry:
                _p = BLOG_ROOT / rel
                _tmp = _p.with_suffix(".md.tmp")
                _tmp.write_text(cur, encoding="utf-8")
                _tmp.replace(_p)
                text, body = cur, strip_frontmatter(cur)

    # --- 2. 아는 용어의 재정의 → 뉘앙스 판정 (LLM) ---
    pend = []
    my_cat = url_slug(permalink)
    for d, (lt, pos) in known_markers:
        chunk = groups[lt][pos]
        if re.search(rf"^    url: {re.escape(permalink)}(?:#|$)", chunk, re.M):
            continue  # 이 글이 이미 defs 에 있음
        if _gen_ed_promotion(chunk, my_cat):
            url = permalink + (f"#{d['anchor']}" if d.get("anchor") else "")
            def_adds.append((lt, pos, url))
            changes.append(f"defs 추가(정식 거처) {d['english']!r} ← {url}")
            continue
        pend.append((d, lt, pos))
    if pend:
        items = []
        for i, (d, lt, pos) in enumerate(pend):
            c = groups[lt][pos]
            marker = f"*{d['english']}<sub>{d['korean']}</sub>*"
            pos_in_body = body.find(d["english"])
            ctx = body[max(0, pos_in_body - 200):pos_in_body + 200]
            items.append(f"[{i}] 기존 항목: en={chunk_field(c, 'en')} "
                         f"ko={chunk_field(c, 'ko')} "
                         f"defs={re.findall(r'- label: (.*)', c)}\n"
                         f"    이번 글({title})의 마커: {marker}\n"
                         f"    문맥: …{ctx}…")
        verdicts = llm_json(NUANCE_PROMPT + "\n\n".join(items))
        vmap = {v.get("i"): v.get("verdict") for v in verdicts
                if isinstance(v, dict)}
        for i, (d, lt, pos) in enumerate(pend):
            if vmap.get(i) == "add_def":
                url = permalink + (f"#{d['anchor']}" if d.get("anchor") else "")
                def_adds.append((lt, pos, url))
                changes.append(f"defs 추가 {d['english']!r} ← {url}")

    # --- 3. (stale 만) 주요 사용 용어 → 색인 부재분 추가 ---
    if kind == "stale":
        majors = llm_json(MAJOR_PROMPT + body[:60000])
        missing = []
        for t in majors:
            if not isinstance(t, dict):
                continue
            en, ko = (t.get("en") or "").strip(), (t.get("ko") or "").strip()
            if not en or dedup_key(en) in idx or (ko and dedup_key(ko) in idx):
                continue
            if count_term(en) + count_term(ko) < 2:
                continue  # 코퍼스에 사실상 없음 — 환각 가능성
            missing.append((en, ko))
        if missing:
            pmap = permalink_map()
            cand_lists = {}
            items = []
            for en, ko in missing:
                cands = []
                for p in all_ko_posts():
                    try:
                        t2 = (BLOG_ROOT / p).read_text(encoding="utf-8")
                    except OSError:
                        continue
                    if re.search(rf"(?i)(?<![A-Za-z]){re.escape(en)}(?![A-Za-z])",
                                 t2) or (ko and ko in t2):
                        fm = parse_frontmatter(t2)
                        pl = fm.get("permalink", "").rstrip("/")
                        if pl in pmap:
                            cands.append((p, fm.get("title", ""), pl,
                                          fm.get("weight", "?")))
                if cands:
                    cand_lists[en] = cands
                    lst = "\n".join(
                        f"  ({j}) {c[0].split('/')[2]}/w{c[3]} {c[1]}"
                        for j, c in enumerate(cands[:15]))
                    items.append(f"용어 {en!r} ({ko!r}):\n{lst}")
            if items:
                picks = llm_json(PICKDEF_PROMPT + "\n\n".join(items))
                pkmap = {p.get("term"): p.get("pick") for p in picks
                         if isinstance(p, dict)}
                for en, ko in missing:
                    pick = pkmap.get(en)
                    cands = cand_lists.get(en, [])
                    if pick == "skip" or not isinstance(pick, int) \
                            or not (0 <= pick < len(cands[:15])):
                        continue
                    if not _HANGUL_RE.search(ko):
                        review.append(f"{rel}: 주요 용어 {en!r} ko 미상 — 보류")
                        continue
                    lt = letter_of(en)
                    if not lt:
                        continue
                    dp, dtitle, dpl, _w = cands[pick]
                    ko_by_slug, _ = category_ko_maps()
                    dcat = ko_by_slug.get(url_slug(dpl) or "", "")
                    if not dcat:
                        continue
                    prim = decide_primary(en, ko, None)
                    adds.append((lt, build_entry(
                        en, ko, prim, f"[{dcat}] §{dtitle}", dpl, [])))
                    changes.append(f"신규(주요어) {en!r}({prim}) ← {dpl}")

    review_note(review)
    if not changes:
        return []

    # --- 4. 결정론 적용 + 쓰기 게이트 ---
    for lt, pos, url in def_adds:
        c2 = add_def_to_chunk(groups[lt][pos], label, url)
        if c2:
            groups[lt][pos] = c2
    seen_new = set()
    n_added = 0
    for lt, entry in adds:
        eid = chunk_id(entry)
        if eid in seen_new or any(chunk_id(c) == eid for c in groups.get(lt, [])):
            continue
        seen_new.add(eid)
        insert_sorted(groups.setdefault(lt, []), entry)
        n_added += 1

    new_text = join_file(header, groups)
    if not write_gate(terms_text, new_text, n_added):
        raise RuntimeError("쓰기 게이트 불통과 — 변경 폐기")
    if dry:
        log("[dry-run] 통과한 변경:\n  " + "\n  ".join(changes))
        return []
    BACKUP_PATH.write_text(terms_text, encoding="utf-8")
    tmp = TERMS_PATH.with_suffix(".tmp")
    tmp.write_text(new_text, encoding="utf-8")
    tmp.replace(TERMS_PATH)
    return changes


def write_gate(old_text: str, new_text: str, expect_added: int) -> bool:
    try:
        old_d, new_d = yaml.safe_load(old_text), yaml.safe_load(new_text)
    except yaml.YAMLError as e:
        log(f"게이트: YAML 파싱 실패 {e}")
        return False
    old_n = sum(len(v or []) for v in old_d.values())
    new_n = sum(len(v or []) for v in new_d.values())
    if new_n != old_n + expect_added:
        log(f"게이트: 항목 수 {old_n}+{expect_added} != {new_n}")
        return False
    pmap = permalink_map()
    ko_by_slug, _ = category_ko_maps()
    old_errs = [i for i in semantic_checks(old_d, pmap, ko_by_slug)
                if i.level == "E"]
    new_errs = [i for i in semantic_checks(new_d, pmap, ko_by_slug)
                if i.level == "E"]
    if len(new_errs) > len(old_errs):
        # 늘어난 에러가 무엇인지 남긴다. 개수만 찍으면 어느 항목의 어떤 코드가
        # 걸렸는지 알 길이 없어 재현하려면 LLM 호출을 다시 태워야 한다 —
        # 게이트 불통과 12 건이 전부 그 상태로 묻혀 있었다.
        before = {i.key() for i in old_errs}
        added = [i for i in new_errs if i.key() not in before]
        detail = " · ".join(f"{i.code}: {i.msg}" for i in added[:5])
        log(f"게이트: 에러 증가 {len(old_errs)}→{len(new_errs)}"
            + (f" — {detail}" if detail else ""))
        return False
    return True


# ---------------------------------------------------------------------------
# terms.yml 감사 (짝수 시각, 글자 하나씩 — sees 보강)
# ---------------------------------------------------------------------------

AUDIT_PROMPT = """수학 블로그 찾아보기 색인의 sees(관련 항목) 보강 작업이다. 도구를 쓰지
말고 JSON 만 출력하라.

아래는 한 글자 그룹의 항목들과, 색인 전체의 id 목록이다. 각 항목에 대해
sees 에 추가할 가치가 있는 **밀접하게 관련된** 기존 항목이 있으면 제안하라.
이미 see 에 있는 것·자기 자신·느슨한 연관은 제외. 확신 없으면 제안하지
말 것 (빈 배열이 정상 결과다).

출력: [{"id": "<항목 id>", "add": ["<대상 id>", ...]}] 만.

"""


def audit_letter(state: dict, dry: bool) -> list[str]:
    letter = state["audit"].get("letter", "A")
    terms_text = TERMS_PATH.read_text(encoding="utf-8")
    header, groups = split_file(terms_text)
    nxt = chr(ord(letter) + 1) if letter < "Z" else "A"
    while letter not in groups:
        letter = nxt
        nxt = chr(ord(letter) + 1) if letter < "Z" else "A"
    state["audit"]["letter"] = nxt

    all_ids = {chunk_id(c): (lt, i)
               for lt, cs in groups.items() for i, c in enumerate(cs)}
    entries_txt = "\n".join(
        f"- {chunk_id(c)}: en={chunk_field(c, 'en')} ko={chunk_field(c, 'ko')} "
        f"see={re.findall(r'^    id: (.*)$', c, re.M)}"
        for c in groups[letter])
    prompt = (AUDIT_PROMPT + f"[{letter} 그룹]\n{entries_txt}\n\n"
              f"[전체 id 목록]\n{' '.join(sorted(all_ids))}")
    props = llm_json(prompt)

    changes: list[str] = []
    n_add = 0
    for p in props:
        if not isinstance(p, dict) or n_add >= MAX_SEE_PER_AUDIT:
            break
        pid = p.get("id")
        if pid not in all_ids or all_ids[pid][0] != letter:
            continue
        lt, pos = all_ids[pid]
        for tid in p.get("add", []):
            if n_add >= MAX_SEE_PER_AUDIT or tid == pid or tid not in all_ids:
                continue
            t_lt, t_pos = all_ids[tid]
            c2 = add_see_to_chunk(groups[lt][pos],
                                  see_tuple(groups[t_lt][t_pos]))
            if c2 is None:
                continue
            groups[lt][pos] = c2
            n_add += 1
            changes.append(f"see: {pid} → {tid}")

    if not changes:
        log(f"감사 {letter}: 추가 없음 (다음 {nxt})")
        return []
    new_text = join_file(header, groups)
    if not write_gate(terms_text, new_text, 0):
        raise RuntimeError("감사 쓰기 게이트 불통과")
    if dry:
        log(f"[dry-run] 감사 {letter}:\n  " + "\n  ".join(changes))
        return []
    BACKUP_PATH.write_text(terms_text, encoding="utf-8")
    tmp = TERMS_PATH.with_suffix(".tmp")
    tmp.write_text(new_text, encoding="utf-8")
    tmp.replace(TERMS_PATH)
    log(f"감사 {letter}: " + " · ".join(changes) + f" (다음 {nxt})")
    return [f"감사({letter}) " + c for c in changes]


# ---------------------------------------------------------------------------
# main
# ---------------------------------------------------------------------------

def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--dry-run", action="store_true")
    ap.add_argument("--status", action="store_true")
    ap.add_argument("--audit-letter", help="감사만 즉시 실행 (테스트)")
    args = ap.parse_args()

    state = load_state()
    if args.status:
        st = state["posts"]
        n_posts = len(all_ko_posts())
        checked = sum(1 for v in st.values() if "last_checked" in v)
        print(f"ko 글 {n_posts} · 검사됨 {checked} · "
              f"quarantine {sum(1 for v in st.values() if v.get('quarantined_until', 0) > time.time())} · "
              f"다음 감사 글자 {state['audit'].get('letter')}")
        return 0

    if not acquire_lock():
        return 0  # 이전 틱이 아직 도는 중 — 조용히
    if not shutil.which(LLM_BIN) and not os.access(LLM_BIN, os.X_OK):
        log(f"LLM 바이너리 없음: {LLM_BIN}")
        return 1

    if args.audit_letter:
        letter = state["audit"]["letter"] = args.audit_letter.upper()
        ch = audit_letter(state, args.dry_run)
        if not args.dry_run:
            save_state(state)
            if ch:
                commit_outputs("term-extract", [REL_TERMS],
                               f"see 링크 {len(ch)}건 (감사 {letter})", log=log)
        return 0

    rel, kind = select_post(state)
    if rel is None:
        today = f"{datetime.now():%Y-%m-%d}"
        # 감사(see 링크 보강)는 하루 한 번으로 묶는다. 2026-08-10 에 1 차 수확이
        # 끝나 유휴 틱이 대부분이 되면서, 짝수 시각마다 도는 감사가 하루 23 회
        # LLM 호출로 see 링크를 228 건 밀어 넣었다 — 그게 상시 비용의 거의 전부다.
        if state["audit"].get("last_date") != today:
            letter = state["audit"].get("letter", "A")
            try:
                ch = audit_letter(state, args.dry_run)
            except Exception as e:
                log(f"감사 실패: {e}")
                return 1
            if not args.dry_run:
                state["audit"]["last_date"] = today
                save_state(state)
                if ch:
                    commit_outputs("term-extract", [REL_TERMS],
                                   f"see 링크 {len(ch)}건 (감사 {letter})", log=log)
        else:
            # 할 일이 없어도 한 줄은 남긴다 — 대시보드가 이 로그의 mtime 으로
            # 워커 생존을 판정하므로(2.5×30분), 조용히 끝내면 정상 동작 중에
            # '안 돎'으로 표시된다.
            log("대상 없음 (감사는 하루 1회, 오늘치 완료)")
        return 0

    log(f"선정({kind}): {rel}")
    ps = state["posts"].setdefault(rel, {})
    # 처리 전에 글이 이미 더러웠으면(사용자가 편집 중) 그 글은 cron 커밋에 넣지
    # 않는다 — 넣으면 작업 중인 원고가 [lastmod-skip] 붙은 봇 커밋에 딸려 들어간다.
    # 병기만 워킹트리에 남고, autopush 가 분류해서 가져간다.
    post_was_dirty = bool(dirty_paths([rel]))
    try:
        changes = process_post(rel, kind, args.dry_run)
    except Exception as e:
        log(f"실패: {rel}: {e}")
        ps["fails"] = ps.get("fails", 0) + 1
        if ps["fails"] >= QUARANTINE_FAILS:
            ps["quarantined_until"] = time.time() + QUARANTINE_SEC
            ps["fails"] = 0
            send_notify(f"{rel} {QUARANTINE_FAILS}회 실패 → "
                        f"7일 격리: {str(e)[:200]}",
                        subject="[용어 추출]", ttl=None)
        if not args.dry_run:
            save_state(state)
        return 1

    ps["last_checked"] = time.time()
    ps["fails"] = 0
    if not args.dry_run:
        save_state(state)
    if changes:
        log("변경: " + " · ".join(changes))
        # 정상 변경은 텔레그램으로 알리지 않는다 (하루 30 회씩 왔다) — 히스토리와
        # 로그에 남고 대시보드가 보여 준다. 알림은 문제일 때만: 3 회 연속 실패 →
        # 격리 (위 except 절).
        if not args.dry_run:
            # 병기는 글 본문도 고치므로 깨끗했던 글은 같은 커밋에 넣는다. 표기·병기
            # 정비라 [lastmod-skip] — 독자가 다시 읽을 것은 없다.
            paths = [REL_TERMS, REL_REVIEW] + ([] if post_was_dirty else [rel])
            if post_was_dirty:
                log(f"편집 중인 글이라 커밋에서 제외: {rel} (autopush 가 가져간다)")
            commit_outputs("term-extract", paths,
                           f"{Path(rel).stem} {len(changes)}건", log=log)
    else:
        log(f"변경 없음: {rel}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
