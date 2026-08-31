#!/usr/bin/env python3
"""
translate_worker.py — single-shot ko→en translation worker (Kimi CLI).

Designed for half-hourly cron (:15/:45). Picks ONE Korean blog post that needs
translation (missing en/ counterpart, or drift_needed), sends it to Kimi through
the native `kimi` CLI, writes the en/ counterpart. 2026-07-21: GLM 해지로 Kimi
기본 복귀 (7-20의 Kimi→GLM 스왑을 하루 만에 되돌림). The dead `glm` path is
kept behind TRANSLATOR_BACKEND="glm" for reference only — claudeglm is retired.

Usage:
    python3 translate_worker.py            # run one translation, exit
    python3 translate_worker.py --status   # print stats only, no API call
    python3 translate_worker.py --dry-run  # show what would be translated

Files:
    state:  ~/math-jh.github.io/scripts/translation/translation_state.json
    log:    redirect cron stderr (e.g. translation.log)
    lock:   /tmp/translate-worker.lock

Cron suggestion:
    */30 * * * * cd /home/junhyeok/math-jh.github.io/scripts/translation \\
                 && /usr/bin/python3 translate_worker.py >>translation.log 2>&1
"""

from __future__ import annotations

import argparse
import collections
import difflib
import hashlib
import json
import os
import re
import shutil
import subprocess
import sys
import time

import yaml
from datetime import datetime, timezone
from pathlib import Path
from typing import List, Optional, Tuple

# ---------------------------------------------------------------------------
# Paths
# ---------------------------------------------------------------------------

BLOG_ROOT   = Path("/home/junhyeok/math-jh.github.io")
POSTS_ROOT  = BLOG_ROOT / "_posts" / "Math"
SCRIPT_DIR  = Path(__file__).resolve().parent
STATE_PATH  = SCRIPT_DIR / "translation_state.json"
LOCK_PATH   = Path("/tmp/translate-worker.lock")
# 검증 실패 시 엔진 출력과 조립본을 떨어뜨리는 곳. 한 줄짜리 에러 메시지만으로는
# 엔진 truncation 과 "마커가 줄 시작이 아닌 위치에 놓임" 을 구별할 수 없다.
# /tmp 는 tmpfs(RAM) 이므로 ext4 인 /var/tmp 를 쓴다.
FAIL_DUMP_DIR = Path("/var/tmp/translate-fail")

# ---------------------------------------------------------------------------
# Kimi CLI
# ---------------------------------------------------------------------------

# 번역 엔진 백엔드: "kimi"(기본, native kimi CLI) 또는 "glm"(사장된 경로 — GLM
# 해지됨, 참고용으로만 잔존. claudeglm 바이너리는 제거되어 실행 불가).
TRANSLATOR_BACKEND    = os.environ.get("TRANSLATOR_BACKEND", "kimi")
GLM_BIN               = str(Path.home() / ".local/bin/claudeglm")
# kimi-headless 어댑터를 거친다. PATH 의 `kimi` 를 집으면 안 된다 — 그건
# kimi-code 본체라 이 워커가 쓰는 구 CLI 규약(stdin 프롬프트, 장식 없는 최종
# 메시지)을 안 지킨다. 특히 --output-format text 가 본문에 `• ` 를 붙여 번역
# 결과를 에러 없이 오염시킨다.
KIMI_BIN              = os.environ.get("KIMI_BIN") or str(
    Path.home() / ".local/bin/kimi-headless")
# No-tools agent + empty MCP for the single-shot verify/audit call (see call_kimi).
VERIFY_AGENT_FILE     = str(SCRIPT_DIR / "verify-agent.yaml")
VERIFY_MCP_FILE       = str(SCRIPT_DIR / "verify-mcp.json")
KIMI_TIMEOUT_SEC      = 3600                 # 60min — 70KB+ 글은 25분으로 부족하다. cron 은
                                             # 30분 주기지만 acquire_lock 이 겹침을 막으므로
                                             # 한 번의 호출이 여러 tick 을 넘겨도 안전하다.
MAX_TRANSLATE_ATTEMPTS = 3                   # re-translate on LOSSY verify verdict, up to N tries

# 큰 글은 조각내어 번역한다. 엔진의 출력 예산은 32K 토큰이고 그 안에 EN 본문이
# 통째로 들어가야 하는데, KO 본문이 이 한계에 가까워지면 모델이 형식을 잃고
# "KO 인용 → EN" 대역 워크시트를 뱉다가 예산을 소진하며 잘린다 (2026-08-02
# Sheaf_Cohomology_of_Schemes, KO 본문 53,978c → 출력 100,470c 중간 절단).
# 조각 경계는 `:::` 박스 경계(_split_regions)라 정리 박스를 가르지 않는다.
FULL_CHUNK_THRESHOLD  = 24_000               # 이 KO 본문 길이(자)를 넘으면 분할
MAX_CHUNK_CHARS       = 12_000               # 조각 하나에 담을 KO 본문 목표치

# Claude verify. 2026-07-20부터 `claude -p --model haiku` 직접 호출 (구독
# 과금 확인됨). 옛 tmux 상주 세션 경로(verify_session.sh, .done 폴링)는
# 과금 정책 롤백 대비로 파일과 상수를 남겨 둔다 — call_claude_verify 참고.
CLAUDE_VERIFY_SCRIPT       = str(SCRIPT_DIR / "verify_session.sh")
CLAUDE_VERIFY_DIR          = Path("/tmp/translation-verify")
CLAUDE_VERIFY_SEND_TIMEOUT = 120             # cold launch (spawn + wait_ready) headroom
CLAUDE_VERIFY_DONE_TIMEOUT = 240             # max wait for the session to write `.done`

# 잔여 지적 수리 게이트 (opus). 결정론 게이트(section_anchor_gate)가 못 고치고
# 남긴 md_lint·앵커 지적만 넘겨 고치게 한다. 지적이 없으면 호출하지 않는다 —
# 워커가 :15/:45 로 도는 이상 무조건 호출은 대부분의 틱에서 헛돈이다.
FIXUP_MODEL       = "opus"
FIXUP_TIMEOUT_SEC = 600                      # 도구 사용 세션이라 verify 보다 넉넉히
FIXUP_MAX_FINDINGS = 12                      # 이보다 많으면 번역 자체가 틀어진 것 — 사람 몫

# Set True once a verify session is used in a run; main() tears the session down
# at the end of the run (it is reused across calls *within* a run, then killed so
# it never lingers idle between cron ticks — re-created lazily on the next verify).
_verify_session_used = False


def kill_verify_session() -> None:
    """Kill the translation-verify tmux session (no-op if absent)."""
    try:
        subprocess.run(["bash", CLAUDE_VERIFY_SCRIPT, "--kill"],
                       capture_output=True, timeout=15)
    except Exception:
        pass
MIN_KO_BODY_CHARS     = 300                  # skip stubs below this
FAIL_RETRY_AFTER_SEC  = 24 * 3600
# 실패 알림 간격. 실패한 글은 백오프를 타고 다음 글로 넘어가므로 엔진 쿼터 소진
# 같은 전면 장애에서는 틱마다 실패한다 — 그대로 알리면 하루 48 통이다. 대신
# 쿨다운을 두고 연속 실패 횟수를 실어 보낸다.
FAIL_NOTIFY_COOLDOWN_SEC = 6 * 3600
POLISH_INTERVAL_SEC   = 14 * 24 * 3600       # (unused) polish is now one-time; see Phase 3
GIT_DRIFT_MARGIN_SEC  = 60                   # (unused) drift is now opt-in via `drift_needed: true`
TRUNCATION_RATIO      = 0.60                 # min output/reference body length; below → fail
# EN 본문(수식·<sub> 제외)에 허용되는 최대 한글 문자수. 정상 코퍼스 최대는 19자
# (참고문헌의 한국어 서지 — 이인석 <선형대수와 군> 등)이고, 산문 한 문단만 미번역돼도
# 100자를 훌쩍 넘는다. 2026-07-30 Divisors_and_Linear_Systems 사고(엔진이 헤딩·라벨만
# 영어화하고 산문 전체를 원문 복사 — 7052자 잔존)가 구조 게이트를 전부 통과한 뒤 신설.
HANGUL_RESIDUE_MAX    = 80

# Local helper (label fix/audit)
sys.path.insert(0, str(SCRIPT_DIR))
from label_normalize import fix_text as label_fix, audit_text as label_audit  # noqa: E402
from math_delimiters import math_profile  # noqa: E402

# 수식 스팬 정규식의 단일 출처는 .agents/hooks/md_lint.py — mech_sweep·josa_check 와
# 같은 관례로 import 한다.
sys.path.insert(0, str(BLOG_ROOT / ".agents" / "hooks"))
import md_lint as _md_lint  # noqa: E402

# 초안(published:false) 판정의 단일 출처는 terms_common.
sys.path.insert(0, str(BLOG_ROOT / "scripts" / "term-extraction"))
from terms_common import published_false_in_fm as _published_false_in_fm  # noqa: E402


# ---------------------------------------------------------------------------
# Lock
# ---------------------------------------------------------------------------

def acquire_lock() -> bool:
    if LOCK_PATH.exists():
        try:
            pid = int(LOCK_PATH.read_text().strip())
            os.kill(pid, 0)                   # check if alive
            return False                       # another instance is running
        except (ValueError, ProcessLookupError, PermissionError):
            pass                               # stale lock — overwrite
    LOCK_PATH.write_text(str(os.getpid()))
    return True


def release_lock() -> None:
    try:
        LOCK_PATH.unlink()
    except FileNotFoundError:
        pass


# ---------------------------------------------------------------------------
# State
# ---------------------------------------------------------------------------

# translation_state.json 스키마의 정본은 이 파일이다. 외부 소비자:
# scripts/term-extraction/term_extract_worker.py 의 load_translation_ts 가
# files/status=="done"/last_attempt_ts 를 읽는다.
# 키를 바꾸면 저쪽 tripwire 경고를 확인할 것.
# state 의 키는 KO 파일 경로다. 글을 개명·이동하면(날짜 접두사 수정, 카테고리
# rename, Title_Case 정규화) 워커는 새 키를 만들고 옛 키는 그대로 남아, 번역 이력이
# 옛 키에 갇힌 채 --status·대시보드 숫자만 부푼다 (2026-08-15 실측 618키 중 187).
# 아래 마이그레이션이 기동 때 그 키들을 따라간다.
_MIGRATE_HIST_FIELDS = (
    "translated_at", "en_path", "in_chars", "out_chars", "verify_verdict",
    "warnings", "lossy_retry_count", "reason", "ko_git_commit_ts",
    "verify_ko_typos", "verify_ko_typos_review", "needs_review",
)
_migrated_keys = 0          # main() 이 이 값을 보고 즉시 저장한다


def _slug_key(name) -> str:
    """날짜 접두사·대소문자·구분자를 지운 파일명 — 개명 추적용 동일성 판정."""
    stem = re.sub(r"^\d{4}-\d{2}-\d{2}-", "", Path(name).name)
    return re.sub(r"[^a-z0-9]", "", stem.lower().removesuffix(".md"))


def _date_prefix(name) -> Optional[str]:
    m = re.match(r"^(\d{4}-\d{2}-\d{2})-", Path(name).name)
    return m.group(1) if m else None


def migrate_state_keys(state: dict) -> int:
    """파일이 옮겨간 state 키를 현재 경로로 따라가게 한다. 옮긴 개수를 돌려준다.

    **유일하게 확정될 때만** 옮긴다 — slug 가 여러 파일에 걸리면 날짜 접두사,
    그래도 갈리면 카테고리로 좁히고, 그래도 남으면 손대지 않는다 (실측으로 slug
    충돌이 20건 있었고 그중 13건은 두 단계를 다 거쳐야 갈렸다). 대상 파일이 아예
    없는 키도 건드리지 않는다 — 병합으로 사라진 것인지 판단하려면 git 이력을
    봐야 하고, 그건 사람이 할 일이다.
    """
    files = state.get("files", {})
    missing = [k for k in files if not (BLOG_ROOT / k).exists()]
    if not missing:
        return 0                      # 정상 상태에서는 디스크를 훑지도 않는다
    disk: dict = {}
    for p in BLOG_ROOT.glob("_posts/**/ko/*.md"):
        disk.setdefault(_slug_key(p.name), []).append(str(p.relative_to(BLOG_ROOT)))

    moved = 0
    for old in missing:
        cands = disk.get(_slug_key(old), [])
        if len(cands) > 1:
            same = [c for c in cands if _date_prefix(c) == _date_prefix(old)]
            if len(same) != 1:
                same = [c for c in cands
                        if Path(c).parts[:-2] == Path(old).parts[:-2]]
            cands = same
        if len(cands) != 1:
            continue
        new = cands[0]
        dead, live = files[old], files.get(new, {})
        dead_newer = (dead.get("last_attempt_ts") or 0) > (live.get("last_attempt_ts") or 0)
        base, over = (dict(live), dead) if dead_newer else (dict(dead), live)
        base.update(over)             # 최신 관찰이 status·타임스탬프를 정한다
        for f in _MIGRATE_HIST_FIELDS:   # 한쪽에만 있는 이력은 잃지 않는다
            if f not in base:
                if f in dead:
                    base[f] = dead[f]
                elif f in live:
                    base[f] = live[f]
        ep = base.get("en_path")
        if ep and not (BLOG_ROOT / ep).exists():
            en_dir = BLOG_ROOT / Path(new).parent.parent / "en"
            hit = [str(p.relative_to(BLOG_ROOT)) for p in en_dir.glob("*.md")
                   if _slug_key(p.name) == _slug_key(ep)] if en_dir.is_dir() else []
            if len(hit) == 1:
                base["en_path"] = hit[0]
        files[new] = base
        del files[old]
        moved += 1
        # 대량 rename 뒤에는 이게 100줄을 넘는다 — 앞쪽만 남기고 나머지는 수로 센다.
        if moved <= 10:
            log(f"state 키 이관: {old} → {new}")
        elif moved == 11:
            log("state 키 이관: … (이하 생략, 아래 합계 참고)")
    if moved:
        log(f"state 키 {moved}건 이관 (남은 미해소 {len(missing) - moved}건은 그대로 둔다)")
    return moved


def load_state() -> dict:
    global _migrated_keys
    if STATE_PATH.exists():
        state = json.loads(STATE_PATH.read_text(encoding="utf-8"))
        _migrated_keys = migrate_state_keys(state)
        return state
    return {
        "files": {},
        "stats": {"total_done": 0, "total_in_chars": 0, "total_out_chars": 0},
    }


def save_state(state: dict) -> None:
    tmp = STATE_PATH.with_suffix(".tmp")
    tmp.write_text(json.dumps(state, indent=2, ensure_ascii=False), encoding="utf-8")
    tmp.replace(STATE_PATH)


# ---------------------------------------------------------------------------
# Target selection
# ---------------------------------------------------------------------------

_DATE_PREFIX_RE = re.compile(r"^\d{4}-\d{2}-\d{2}-")
_FRONTMATTER_RE = re.compile(r"^---\s*\n(.*?)\n---\s*\n", re.DOTALL)
# 개정 중 표시. CI 의 freeze_revising_posts.py 가 이 키를 보고 프로덕션을 직전 발행
# 판본으로 되돌린다 (is_draft 참고).
_REVISING_RE = re.compile(r"^revising:\s*true\s*$", re.M)


def topic_slug(path: Path) -> str:
    """Filename with leading 'YYYY-MM-DD-' stripped. Pairing key for ko↔en."""
    return _DATE_PREFIX_RE.sub("", path.name, count=1)


def en_dir_for_ko(ko_path: Path) -> Path:
    parts = list(ko_path.parts[:-1])     # drop filename
    parts[parts.index("ko")] = "en"
    return Path(*parts)


def find_en_counterpart(ko_path: Path) -> Optional[Path]:
    """Return existing en/ file matching ko's topic slug, ignoring date prefix."""
    en_dir = en_dir_for_ko(ko_path)
    if not en_dir.exists():
        return None
    slug = topic_slug(ko_path)
    for en_file in en_dir.glob("*.md"):
        if topic_slug(en_file) == slug:
            return en_file
    return None


def en_path_for_new_translation(ko_path: Path) -> Path:
    """Where to write a fresh translation: en/ dir + ko's filename (mirrors ko date)."""
    return en_dir_for_ko(ko_path) / ko_path.name


def _read_frontmatter(path: Path) -> str:
    text = path.read_text(encoding="utf-8")
    m = _FRONTMATTER_RE.match(text)
    return m.group(1) if m else ""


def _ko_body_length(ko_path: Path) -> int:
    """Length of the body after frontmatter — used to skip stubs."""
    text = ko_path.read_text(encoding="utf-8")
    m = _FRONTMATTER_RE.match(text)
    body = text[m.end():] if m else text
    return len(body.strip())


def is_draft(ko_path: Path) -> bool:
    """번역을 걸지 않을 글. 초안(`published: false`)과 개정 중(`revising: true`)이다.

    `published: false` 판정은 단일 출처 terms_common.published_false_in_fm.

    개정 중을 여기서 막는 이유: 2026-08-17 이전에는 개정 중인 글에 `published: false`가
    함께 붙어 있어 이 검사가 자동으로 걸렀다. 그 키를 걷어낸 뒤로는 개정 중인 글이
    발행 글로 보이므로, 막지 않으면 워커가 **고치는 중인 원고**를 번역해 EN 을 덮어쓴다.
    개정이 끝나 revising 키가 빠지면 그때 drift_needed 가 재번역을 부른다.
    """
    fm = _read_frontmatter(ko_path)
    return _published_false_in_fm(fm) or bool(_REVISING_RE.search(fm))


def ko_wants_drift(ko_path: Path) -> bool:
    """True if KO frontmatter has `drift_needed: true`.

    This is the explicit, opt-in signal that the author edited the KO source
    and wants the EN re-translated. The author sets it by hand; the worker
    clears it after a successful drift translation (see clear_drift_flag).
    Replaces the old timestamp heuristic, which re-translated on *any* KO
    commit and so clobbered manual post-translation fixes (typo corrections,
    fidelity edits) with a fresh machine translation.
    """
    for line in _read_frontmatter(ko_path).splitlines():
        s = line.strip()
        if s.startswith("drift_needed"):
            value = s.split(":", 1)[1].strip().strip('"').strip("'").lower()
            return value == "true"
    return False


def clear_drift_flag(ko_path: Path) -> None:
    """Strip the `drift_needed:` line from KO frontmatter after a drift run.

    Consumes the opt-in flag so the post is not re-translated on every tick.
    Only the frontmatter block is rewritten; the body is left byte-for-byte
    intact. Because drift is now flag-driven (not timestamp-driven), the
    resulting KO commit does not re-trigger drift.
    """
    text = ko_path.read_text(encoding="utf-8")
    m = _FRONTMATTER_RE.match(text)
    if not m:
        return
    fm_block, body = text[:m.end()], text[m.end():]
    new_fm = re.sub(r"^drift_needed\s*:.*\n?", "", fm_block, flags=re.MULTILINE)
    if new_fm != fm_block:
        ko_path.write_text(new_fm + body, encoding="utf-8")


# ── git: 봇 산출물은 봇이 커밋한다 ─────────────────────────────────────────
#
# EN 은 사실상 봇 산출물이라 사람이 손댈 일이 거의 없다. 워커가 자기 산출물을 직접
# 커밋하면 autopush 의 haiku 분류기가 거대한 EN diff 를 볼 일이 없어진다. 그 분류기는
# staged .md diff 가 8만 자를 넘으면 오분류를 피하려고 HALT 하는데, EN 재번역 몇 편이면
# 쉽게 넘어서 실제로 autopush 가 계속 멈춰 있었다 (2026-07-14).
#
# push 는 하지 않는다 — autopush 가 밀린 커밋까지 함께 밀어준다.
AUTOPUSH_LOCK = Path("/tmp/blog-autopush.lock")
COMMIT_LOCK_WAIT_SEC = 120

# 번역은 LLM 산출물이므로 author=Marvin, 커밋 행위자는 Claude (2026-07-22 정체성
# 체계, 히스토리 리라이트와 동일 구도). marvin@math-jh.com 은 의도적으로 GitHub
# 미등록 주소 — 나중에 machine account 를 만들어 인증하면 소급 연결된다.
_GIT_IDENTITY = {
    "GIT_AUTHOR_NAME": "Marvin", "GIT_AUTHOR_EMAIL": "marvin@math-jh.com",
    "GIT_COMMITTER_NAME": "Claude", "GIT_COMMITTER_EMAIL": "noreply@anthropic.com",
}


def _git(*args: str) -> Tuple[int, str, str]:
    p = subprocess.run(["git", *args], cwd=str(BLOG_ROOT),
                       capture_output=True, text=True,
                       env={**os.environ, **_GIT_IDENTITY})
    return p.returncode, p.stdout, p.stderr


def _post_title(path: Path) -> str:
    try:
        m = re.search(r'^title:\s*"?(.+?)"?\s*$',
                      path.read_text(encoding="utf-8")[:2000], re.MULTILINE)
        return m.group(1) if m else path.stem
    except OSError:
        return path.stem


# 제목은 `cron(translate): …` 로 시작한다 — cron 산출물 커밋은 전부 `cron(<워커>):`
# 접두사를 달아, git log 만 봐도 어느 워커가 낸 것인지 보이게 하는 규약이다
# (scripts/lib/cron_commit.py 를 쓰는 다른 워커들과 같은 형식).
_COMMIT_PREFIX = "cron(translate): "
_COMMIT_SUBJECT = {
    "pending": "EN 신규 번역",       # Phase 1: EN 이 아예 없던 글
    "drift":   "EN 재번역(drift)",   # Phase 2: KO 가 바뀌어 `drift_needed` 가 걸린 글
    "polish":  "EN 다듬기(polish)",  # Phase 3: 글당 1회, EN 산문만 손보는 패스
}


def commit_translation(ko_path: Path, en_path: Path, reason: str) -> None:
    """방금 쓴 EN(과 drift 면 KO 플래그)을 커밋한다. 실패해도 번역은 살린다.

    drift 일 때 KO 는 `drift_needed` 한 줄만 지워진 상태이므로 mechanical
    (`[lastmod-skip]`), EN 본문은 content 로 **따로** 커밋한다. 한 커밋에 묶으면
    KO 의 last_modified_at 까지 바뀐다.

    autopush 와 같은 락을 쓴다 (둘 다 같은 레포에 git 을 건다). 못 잡으면 커밋을
    건너뛴다 — 파일은 워킹트리에 남으므로 다음 autopush 가 가져간다.
    """
    import fcntl

    deadline = time.time() + COMMIT_LOCK_WAIT_SEC
    fd = os.open(str(AUTOPUSH_LOCK), os.O_CREAT | os.O_RDWR)
    try:
        while True:
            try:
                fcntl.flock(fd, fcntl.LOCK_EX | fcntl.LOCK_NB)
                break
            except OSError:
                if time.time() >= deadline:
                    log("commit: autopush 가 락을 쥐고 있다 — 커밋 건너뜀 "
                        "(다음 autopush 가 가져간다)")
                    return
                time.sleep(5)

        rel_en = str(en_path.relative_to(BLOG_ROOT))
        rel_ko = str(ko_path.relative_to(BLOG_ROOT))
        title = _post_title(en_path)

        # 1) KO: drift 플래그 소거 (mechanical). 실제로 바뀐 게 있을 때만.
        rc, out, _ = _git("status", "--porcelain", "--", rel_ko)
        if reason == "drift" and out.strip():
            _git("add", "--", rel_ko)
            rc, _, err = _git("commit", "-m",
                              _COMMIT_PREFIX
                              + "재번역 완료된 글의 drift 플래그 소거 [lastmod-skip]")
            if rc != 0:
                log(f"commit(ko) 실패: {err.strip()[:200]}")
                _git("reset", "-q", "--", rel_ko)

        # 2) EN: 번역 결과 (content)
        subject = _COMMIT_PREFIX + _COMMIT_SUBJECT.get(reason, f"EN 재번역({reason})")
        _git("add", "--", rel_en)
        rc, _, err = _git("commit", "-m", f"{subject}: {title}")
        if rc != 0:
            log(f"commit(en) 실패: {err.strip()[:200]}")
            _git("reset", "-q", "--", rel_en)
            return
        log(f"committed: {subject}: {title}")
    finally:
        os.close(fd)


# EN frontmatter 의 translation_source 태그. 단일 출처 = _config.yml 의
# translation_source_tag — 같은 값을 _includes/translation-notice.html 이
# site.translation_source_tag 로 비교한다. 현재 번역 워커의 태그이며, 워커가
# 본격적으로 바뀌면 _config.yml 값과 함께 바뀐다.
def _load_translation_source_tag() -> str:
    for line in (BLOG_ROOT / "_config.yml").read_text(encoding="utf-8").splitlines():
        s = line.strip()
        if s.startswith("translation_source_tag"):
            return s.split(":", 1)[1].split("#")[0].strip().strip('"').strip("'")
    sys.exit("_config.yml 에 translation_source_tag 가 없음 — 노티스 include 와 "
             "짝이 되는 정본 키다. 지우지 말 것.")


TRANSLATION_SOURCE_TAG = _load_translation_source_tag()


_META_KEYS = ("translated_at", "translation_source", "last_polished_at")

# KO-side pipeline switches. They steer the worker and mean nothing on the EN
# side, so they must not ride along when EN frontmatter is composed from KO's —
# `drift_needed` leaking into an EN file is exactly what happened on 2026-07-12.
_KO_ONLY_KEYS = ("drift_needed",)

# Frontmatter fields that are LLM-translated (rest are deterministic).
_LLM_FRONTMATTER_FIELDS = ("title", "excerpt", "description")


def _split_fm_block(text: str) -> Tuple[str, str]:
    """Return (frontmatter_inside_dashes, body_after_closing_dashes).

    Tolerant of `---title:` (missing newline after opening ---).
    """
    m = _FRONTMATTER_RE.match(text)
    if m:
        return m.group(1), text[m.end():]
    if text.startswith("---") and len(text) > 3:
        close = text.find("\n---", 3)
        if close != -1:
            fm = text[3:close].lstrip("\n")
            body_start = close + 4
            if body_start < len(text) and text[body_start] == "\n":
                body_start += 1
            return fm, text[body_start:]
    return "", text


def _extract_fm_scalar(fm: str, key: str) -> Optional[str]:
    """Extract a top-level scalar value (title/excerpt/description style)."""
    m = re.search(rf'^{re.escape(key)}\s*:\s*"((?:[^"\\]|\\.)*)"\s*$', fm, re.M)
    if m:
        return m.group(1).replace('\\"', '"').replace("\\\\", "\\")
    m = re.search(rf"^{re.escape(key)}\s*:\s*([^\n]+)$", fm, re.M)
    if m:
        return m.group(1).strip().strip('"').strip("'")
    return None


_FM_FIELDS_PROMPT = """Translate these Korean Jekyll frontmatter values to natural, idiomatic English. Output ONLY a single JSON object with the same keys; no preamble, no code fences, no commentary.

Style:
- title: a concise English noun phrase (e.g. "Abelian Groups and Fields"). Match the canonical English math terminology.
- excerpt: a short phrase (≤ 12 words) describing the post's topic. Keep nouns parallel.
- description: 1–2 sentences in natural English. No math notation, no escape characters.

Constraints:
- No Korean characters in any output value.
- No surrounding quotes inside the JSON values.
- Output must be valid JSON parseable by Python json.loads.

KO input (JSON):
{ko_json}

Required output keys: {keys}"""


def _translate_fm_fields_via_kimi(ko_fields: dict) -> dict:
    """Small focused kimi call to translate title/excerpt/description.

    `ko_fields` only includes keys whose values exist in KO frontmatter.
    Returns a dict with the same keys mapped to English strings.
    """
    # (프롬프트에 "no code fences" 라고 써도 모델은 종종 ```json 으로 감싸 내놓는다.
    #  _parse_json_object 가 벗겨낸다 — 2026-07-14 실제로 이 때문에 실패했다.)
    if not ko_fields:
        return {}
    prompt = _FM_FIELDS_PROMPT.format(
        ko_json=json.dumps(ko_fields, ensure_ascii=False, indent=2),
        keys=list(ko_fields.keys()),
    )
    out = call_kimi(prompt, thinking=False)
    try:
        data = _parse_json_object(out)
    except (json.JSONDecodeError, ValueError) as e:
        raise RuntimeError(f"frontmatter-fields translation: invalid JSON output ({e}): {out[:200]!r}")
    return {k: str(data.get(k, "")).strip() for k in ko_fields.keys()}


def _compose_en_frontmatter(
    ko_fm: str,
    en_fields: dict,
    *,
    translated_at_iso: str,
    polished_at_iso: Optional[str] = None,
) -> str:
    """Build EN frontmatter deterministically from KO frontmatter.

    - LLM-translated fields (title/excerpt/description): replaced with en_fields
    - permalink: `/ko/` → `/en/` (whole-token swap)
    - sidebar.nav: trailing `-ko` → `-en`
    - existing translation_source / translated_at / last_polished_at: stripped
    - KO-only pipeline switches (drift_needed): dropped
    - new translated_at / translation_source / (optionally last_polished_at): appended
    """
    fm = ko_fm
    # Strip any existing translation meta to keep frontmatter idempotent, and any
    # KO-only switch that must not cross over to the EN side.
    for k in _META_KEYS + _KO_ONLY_KEYS:
        fm = re.sub(rf"^{k}\s*:.*\n?", "", fm, flags=re.M)

    out_lines: list[str] = []
    for line in fm.splitlines():
        stripped = line.strip()
        if stripped and not stripped.startswith("#") and ":" in stripped and line[:1] not in (" ", "\t"):
            key = stripped.split(":", 1)[0].strip()
            if key in _LLM_FRONTMATTER_FIELDS and key in en_fields and en_fields[key]:
                v = en_fields[key].replace("\\", "\\\\").replace('"', '\\"')
                out_lines.append(f'{key}: "{v}"')
                continue
            if key == "permalink":
                out_lines.append(line.replace("/ko/", "/en/", 1))
                continue
        # nested keys (sidebar nav, header) — pattern: `    nav: "xxx-ko"`
        if re.search(r'^\s+nav\s*:\s*"[^"]*-ko"\s*$', line):
            out_lines.append(re.sub(r'-ko"\s*$', '-en"', line))
            continue
        out_lines.append(line)

    composed = "\n".join(out_lines).rstrip() + (
        f"\ntranslated_at: {translated_at_iso}\n"
        f"translation_source: {TRANSLATION_SOURCE_TAG}\n"
    )
    if polished_at_iso:
        composed += f"last_polished_at: {polished_at_iso}\n"
    return composed


def en_translation_meta(en_path: Path) -> dict:
    """Read translated_at / translation_source / last_polished_at from en frontmatter."""
    meta = {}
    for line in _read_frontmatter(en_path).splitlines():
        s = line.strip()
        for key in _META_KEYS:
            if s.startswith(key + ":"):
                meta[key] = s.split(":", 1)[1].strip().strip('"').strip("'")
                break
    return meta


def is_our_translation(en_path: Path) -> bool:
    """True iff en file frontmatter has translation_source matching our tag."""
    return en_translation_meta(en_path).get("translation_source") == TRANSLATION_SOURCE_TAG


def inject_translation_metadata(
    translated_md: str,
    translated_at_iso: str,
    *,
    polished_at_iso: Optional[str] = None,
) -> str:
    """Insert translated_at / translation_source / last_polished_at into frontmatter.

    Idempotent: strips any pre-existing markers before re-injecting. `last_polished_at`
    is only written when `polished_at_iso` is provided (i.e. on polish runs); pending
    and drift re-translations drop the field so the next polish becomes due again.
    """
    m = _FRONTMATTER_RE.match(translated_md)
    if not m:
        return translated_md
    fm = m.group(1)
    for k in _META_KEYS:
        fm = re.sub(rf"^{k}\s*:.*\n?", "", fm, flags=re.MULTILINE)
    fm = fm.rstrip() + (
        f"\ntranslated_at: {translated_at_iso}\n"
        f"translation_source: {TRANSLATION_SOURCE_TAG}\n"
    )
    if polished_at_iso:
        fm += f"last_polished_at: {polished_at_iso}\n"
    return f"---\n{fm}---\n{translated_md[m.end():]}"


def git_last_commit_ts(path: Path) -> Optional[float]:
    """Unix timestamp of the last git commit touching `path`, or None if not tracked."""
    try:
        out = subprocess.check_output(
            ["git", "log", "-1", "--format=%ct", "--", str(path)],
            cwd=str(BLOG_ROOT),
            text=True,
            stderr=subprocess.DEVNULL,
        ).strip()
        return float(out) if out else None
    except (subprocess.CalledProcessError, FileNotFoundError):
        return None


def _iso_to_ts(iso: str) -> float:
    try:
        return datetime.fromisoformat(iso).timestamp()
    except Exception:
        return 0.0


def find_next_target(state: dict) -> Optional[Tuple[Path, Path, str]]:
    """Four-phase priority: pending → drift → polish → verify.

    Returns (ko_path, en_path_to_write, reason) or None.
    """
    ko_files = sorted(POSTS_ROOT.glob("*/ko/*.md"))
    now = time.time()

    # --- Phase 1: untranslated (no en counterpart, not a draft) ----------
    for ko in ko_files:
        key = str(ko.relative_to(BLOG_ROOT))
        entry = state["files"].get(key, {})

        if entry.get("status") == "failed":
            if now - entry.get("last_attempt_ts", 0) < FAIL_RETRY_AFTER_SEC:
                continue

        if is_draft(ko):
            if entry.get("status") != "draft_skip":
                state["files"][key] = {"status": "draft_skip", "last_attempt_ts": now}
            continue

        if _ko_body_length(ko) < MIN_KO_BODY_CHARS:
            if entry.get("status") != "stub":
                state["files"][key] = {"status": "stub", "last_attempt_ts": now}
            continue

        if find_en_counterpart(ko) is None:
            return ko, en_path_for_new_translation(ko), "pending"

    # --- Phase 2: drift (explicit opt-in via `drift_needed: true` in KO) ------
    for ko in ko_files:
        if is_draft(ko):
            continue
        # Honour the failure backoff, as Phase 1 does. Without it a post that
        # fails validation every time is picked again on the very next tick, and
        # since drift is scanned in a fixed order it stays at the head of the
        # queue forever — starving every other flagged post while burning a full
        # re-translation each pass. That is what a bad `drift_needed` exemption
        # did on 2026-07-12: 48 wasted re-translations of one post over 26h.
        entry = state["files"].get(str(ko.relative_to(BLOG_ROOT)), {})
        if entry.get("status") == "failed" and \
           now - entry.get("last_attempt_ts", 0) < FAIL_RETRY_AFTER_SEC:
            continue
        existing_en = find_en_counterpart(ko)
        if existing_en is None:
            continue
        if not is_our_translation(existing_en):    # manual translation — leave alone
            continue
        if ko_wants_drift(ko):
            return ko, existing_en, "drift"

    # --- Phase 3: polish (one-time; never-polished posts) ----------------
    # Polish improves the EN prose. It runs at most once per post: once
    # last_polished_at is set the post is not re-polished (so a single pass is
    # not compounded). A single pass can still introduce errors — Phase 4 then
    # verifies the polished result and surfaces any such damage.
    for ko in ko_files:
        if is_draft(ko):
            continue
        # Phase 1·2 와 같은 실패 백오프. polish 는 last_polished_at 이 박혀야
        # 큐에서 빠지는데, 검증에 걸려 실패하면 그 키는 안 박힌다 — 백오프가
        # 없으면 고정된 스캔 순서의 맨 앞에 그대로 남아 다음 틱에 또 뽑히고,
        # 아직 polish 안 된 나머지 글이 전부 굶는다.
        entry = state["files"].get(str(ko.relative_to(BLOG_ROOT)), {})
        if entry.get("status") == "failed" and \
           now - entry.get("last_attempt_ts", 0) < FAIL_RETRY_AFTER_SEC:
            continue
        existing_en = find_en_counterpart(ko)
        if existing_en is None:
            continue
        if not is_our_translation(existing_en):
            continue
        if _iso_to_ts(en_translation_meta(existing_en).get("last_polished_at", "")) > 0:
            continue                       # already polished → don't re-polish
        return ko, existing_en, "polish"

    # --- Phase 4: verify (read-only, one-time; polished posts only) ------
    # Runs ONLY on posts that have been polished (last_polished_at set) but not
    # yet verified. Lints + semantically checks the polished EN against the KO
    # and surfaces problems the polish pass may have introduced (log + telegram).
    # The EN file is never modified. One-time: a recorded `verified_at` retires
    # the post.
    for ko in ko_files:
        if is_draft(ko):
            continue
        existing_en = find_en_counterpart(ko)
        if existing_en is None:
            continue
        if not is_our_translation(existing_en):
            continue
        if _iso_to_ts(en_translation_meta(existing_en).get("last_polished_at", "")) <= 0:
            continue                       # not polished yet → verify comes later
        if state["files"].get(str(ko.relative_to(BLOG_ROOT)), {}).get("verified_at"):
            continue                       # already verified → done
        return ko, existing_en, "verify"

    return None


# ---------------------------------------------------------------------------
# Prompt
# ---------------------------------------------------------------------------
# 아래 프롬프트가 지켜야 하는 규칙의 source of truth 는
# `.claude/guidelines/GUIDELINE-Translation.md` 다 (구분자 verbatim 보존, `:::`
# 라벨→앵커 유도, 한영 병기 처리, validate_translation 불변식). 문서를 런타임에
# 읽어 붙이지 않고 여기에 영어로 풀어 둔 것은 엔진에 주는 지시가 예시·반례까지
# 포함한 튜닝된 형태여야 하기 때문이다. 규칙을 바꿀 때는 양쪽을 같이 고칠 것.

INSTRUCTIONS = """You translate the BODY of a Korean math blog post (Jekyll markdown) into natural, idiomatic English. The input is the body content only — frontmatter has already been stripped and is handled separately by a script. Output ONLY the translated body. No frontmatter, no `---` lines, no explanation, no code fences, no preamble.

Conversion rules for the body:

1. Math content: preserve every math span VERBATIM — same LaTeX, same count, same order, AND the SAME DELIMITER. Do not translate variable names or LaTeX commands. The blog uses standard delimiters: inline math is `$...$`, display (centered, standalone) math is `$$...$$`. Copy whichever the KO used; never swap one for the other.
   - WRONG: KO `... 다음 식이 성립한다.\\n\\n$$\\int_0^1 f = 1$$\\n\\n` → EN `... the identity $\\int_0^1 f = 1$ holds.` (a display block collapsed into inline — FORBIDDEN).
   - WRONG: KO `... 사상 $f\\colon X \\to Y$ 가 주어지면 ...` → EN `... given a map $$f\\colon X \\to Y$$, ...` (inline promoted to display — also FORBIDDEN).
   - RIGHT: the EN has exactly as many `$$...$$` spans, and exactly as many `$...$` spans, as the KO.
   - Inside a `$$...$$` (or `$...$`) span, a single `$` may legitimately appear within `\\text{...}`/`\\tag{...}` — that is LaTeX re-entering math mode from text mode. Leave it alone.

2. Cross-reference links:
   - Path: `/ko/...` → `/en/...` (slug stays the same).
   - Visible label: translate Korean section title (e.g. `§아핀다양체` → `§Affine Varieties`).
   - Category bracket: `[\\[대수다양체\\] §..., ⁋정의 7]` → `[\\[Algebraic Varieties\\] §..., ⁋Definition 7]`.
   - Labels: 정의→Definition, 명제→Proposition, 정리→Theorem, 보조정리→Lemma, 따름정리→Corollary, 예시→Example, 참고→Remark.
   - Within-doc refs: `[정의 3](#def3)` → `[Definition 3](#def3)` (id unchanged).
   - **Verification rule**: only emit a link `[display](url)` or an in-doc anchor `#labelN` if you are confident the target exists in the source body or in the linked post's English form. If uncertain about the precise English wording of a cross-reference label, keep the KO source form verbatim — a post-processing pass will normalise it. Do NOT invent English titles, definition numbers, or anchor ids that you have not seen.

3. Bilingual italic terms:
   - `*english<sub>한국어</sub>*` → `*english*` (drop Korean gloss).
   - `*한국어<sub>english</sub>*` → `*English*` (use English gloss as primary).
   - `<em-ko>...</em-ko>` (Korean-emphasis tag) → plain `*...*` emphasis around the translated text. The tag must not appear in EN output.

4. Theorem-box fenced blocks (`:::`): keep every `:::` fence line exactly where it is, with the same count and order — both the labeled opener and the bare `:::` closer. On the opener, translate ONLY the label text:
   - Derived box `::: 정리 2 (Thom isomorphism)` → `::: Theorem 2 (Thom isomorphism)`: translate the kind word (정의→Definition, 명제→Proposition, 정리→Theorem, 보조정리→Lemma, 따름정리→Corollary, 예시→Example, 참고→Remark), keep the number N unchanged, translate the parenthesized name.
   - Attached proof `::: 증명` → `::: Proof`. Standalone proof `::: 증명 (정리 4)` → `::: Proof (Theorem 4)` (translate the label inside the parentheses too).
   - misc box `::: misc 주장 4 (Mirror theorem, $$D$$-module form) {#conj4}` → `::: misc Conjecture 4 (Mirror theorem, $$D$$-module form) {#conj4}`: translate the label text but keep the trailing `{#conj4}` anchor EXACTLY (same id, same braces).
   - The bare closing `:::` line is copied verbatim. Never add, drop, split, merge, or reorder `:::` lines.
   - Some blocks are still written as legacy HTML rather than `:::` — preserve `<div class="...">`, `</div>`, `<details class="proof">`, `</details>` exactly, and translate only their labels: `<ins id="def1">**정의 1**</ins>` → `<ins id="def1">**Definition 1**</ins>` (id and number N unchanged), `<summary>증명</summary>` → `<summary>Proof</summary>`.

5. Style: first-person plural ("we"); idiomatic, not literal grammar. "우리는 ~를 정의한다" → "we define ~".

6. Section headers: `## 정의` → `## Definition`. Use noun phrases.

7. Footnotes: `[^1]` markers preserved; footnote bodies translated.

8. References: the bibliography is handled OUTSIDE this translation. If the body contains the literal line `@@REFERENCES@@`, copy that line verbatim, exactly once, in the same position. NEVER write a References section or bibliography entries yourself, and never invent citations.

# Self-check before responding (must all pass)

- Same math delimiters as the KO body: EN must have exactly as many `$$...$$` display spans AND exactly as many `$...$` inline spans as KO. None downgraded, none promoted, none added/dropped/split/merged.
- Every `:::` opener from KO appears in EN with the label translated but the SAME derived anchor: the kind→prefix mapping (정의→def, 명제→prop, 정리→thm, 보조정리→lem, 따름정리→cor, 예시→ex, 참고→rmk) plus the unchanged number, and every `::: misc … {#id}` keeps its `{#id}` intact. The `:::` fence lines have the same count and order as KO; no Korean kind word survives on any opener.
- No Korean labels remain (정의, 명제, 정리, 보조정리, 따름정리, 예시, 참고, 증명, 참고문헌).
- **No Korean prose remains anywhere.** Every Korean sentence and paragraph is translated into English. Translating only headings, labels, and links while copying Korean paragraphs verbatim is a FAILED translation and will be rejected.
- If the input contained the line `@@REFERENCES@@`, the output contains it verbatim, exactly once.
- The body ends at the final content line — do not truncate mid-sentence.
- Output begins with the first body character (no leading `---` or blank lines).

Now translate the body below."""


def build_prompt(ko_body: str) -> str:
    return INSTRUCTIONS + "\n\n" + ko_body


_CHUNK_NOTE = """# Fragment mode

The text below is fragment {idx} of {total} of a single post body, cut at
theorem-box boundaries. Translate the whole fragment.

- The fragment may begin or end mid-section. That is expected. Do not add an
  introduction, a recap, a transition, or a closing sentence, and do not
  mention the split.
- Keep every label number exactly as it appears; numbering continues across
  fragments and you cannot see the others.
- Do not restate these rules, do not quote the Korean back, do not narrate your
  work. The response must be the translated fragment and nothing else.

Now translate the fragment below."""


def build_chunk_prompt(ko_chunk: str, idx: int, total: int) -> str:
    return (INSTRUCTIONS + "\n\n"
            + _CHUNK_NOTE.format(idx=idx, total=total) + "\n\n" + ko_chunk)


# ---------------------------------------------------------------------------
# References isolation
# ---------------------------------------------------------------------------
# 참고문헌 섹션은 frontmatter처럼 엔진에 보내지 않는다. 엔진이 서지를 지어내
# 붙이거나(2026-07-30 en Singular_Value_Decomposition에 [TB]·[Str] 발명 사례)
# 항목을 고치는 것을 원천 차단하기 위해, 본문에서 블록을 잘라내 sentinel 한
# 줄로 바꿔 보내고 번역 후 KO 원문 그대로(마커만 **References**로) 재부착한다.
# footnote 정의는 참고문헌 뒤에 올 수 있으나 번역이 필요하므로 블록에 포함하지
# 않는다 — 블록은 마커 줄부터 마지막 연속 엔트리 줄까지다.

REFS_SENTINEL = "@@REFERENCES@@"
_REFS_MARK_RE  = re.compile(r"^\*\*(참고문헌|References)\*\*[ \t]*$", re.M)
_REFS_SENTINEL_LINE_RE = re.compile(
    r"^[ \t]*" + re.escape(REFS_SENTINEL) + r"[ \t]*$", re.M)
_REFS_ENTRY_RE = re.compile(r"^\s*(\*\*\[[^\]]+\]\*\*|\[[^\]^]+\][ (])")


def dump_failure(ko_path: Path, err: str, *, engine_out: str, assembled: str) -> None:
    """검증 실패의 증거를 FAIL_DUMP_DIR 에 남긴다 (엔진 출력 / 조립본 / 에러)."""
    try:
        FAIL_DUMP_DIR.mkdir(parents=True, exist_ok=True)
        stem = ko_path.stem
        (FAIL_DUMP_DIR / f"{stem}.engine.md").write_text(engine_out, encoding="utf-8")
        (FAIL_DUMP_DIR / f"{stem}.assembled.md").write_text(assembled, encoding="utf-8")
        (FAIL_DUMP_DIR / f"{stem}.error.txt").write_text(err + "\n", encoding="utf-8")
        log(f"failure dump: {FAIL_DUMP_DIR}/{stem}.*")
    except Exception as e:                       # 덤프 실패가 번역 실패를 가리면 안 된다
        log(f"failure dump skipped: {e!r}")


def extract_refs_block(body: str) -> Tuple[str, Optional[str]]:
    """(refs 블록을 sentinel로 치환한 body, 블록 원문) 반환. 블록 없으면 (body, None)."""
    m = _REFS_MARK_RE.search(body)
    if not m:
        return body, None
    head = body[: m.start()]
    lines = body[m.start() :].split("\n")   # lines[0] = marker line
    last = 0
    for i, line in enumerate(lines[1:], start=1):
        if _REFS_ENTRY_RE.match(line):
            last = i
        elif line.strip():
            break                            # 엔트리·빈 줄 외의 내용 → 블록 종료
    if last == 0:
        return body, None                    # 마커만 있고 엔트리 없음
    block = "\n".join(lines[: last + 1])
    rest = "\n".join(lines[last + 1 :])
    return head + REFS_SENTINEL + ("\n" + rest if rest else ""), block


def reattach_refs_block(body: str, ko_refs: Optional[str]) -> str:
    """sentinel 자리에 KO refs 블록을 마커만 영어화해 재부착한다.

    sentinel 은 <em>줄을 독차지한</em> 것만 인정한다. 문장 안에 박힌 것을 그대로
    치환하면 `**References**` 가 줄 시작에 오지 않아 마커 정규식에 걸리지 않고,
    검증은 "참고문헌 없음"이라는 엉뚱한 이름으로 실패한다 (2026-08-02: 엔진이
    지시사항을 복창하며 만든 ``- `@@REFERENCES@@` preserved verbatim`` 줄이
    유일한 출현이었던 사례). 여기서 먼저 죽는 편이 진단에 낫다.
    """
    n_raw = body.count(REFS_SENTINEL)
    matches = list(_REFS_SENTINEL_LINE_RE.finditer(body))
    if ko_refs is None:
        if n_raw:
            raise RuntimeError("refs sentinel appeared but KO has no references block")
        return body
    if len(matches) != 1:
        raise RuntimeError(
            f"refs sentinel: {len(matches)} standalone line(s) / {n_raw} raw "
            f"occurrence(s), expected exactly 1 of each — engine dropped, "
            f"duplicated, or inlined it"
        )
    en_refs = _REFS_MARK_RE.sub("**References**", ko_refs, count=1)
    m = matches[0]
    return body[: m.start()] + en_refs + body[m.end() :]


POLISH_INSTRUCTIONS = """You are polishing the BODY of an existing English translation of a Korean math blog post. Frontmatter has been stripped and is handled separately by a script. Output ONLY the polished body. No frontmatter, no `---` lines, no explanation, no code fences, no preamble.

# Task

Given the Korean source body (for meaning reference) and the current English translation body, produce an *improved* English body. Refine prose quality. Preserve everything else exactly.

# What to improve

- Awkward translations or literal Korean grammar → idiomatic English
- Word choice → more precise mathematical or natural English
- Sentence flow → smoother connectives, less choppy
- Terminology consistency within the post and against standard mathematical English
- Fix translation drift: if the EN diverges from the KO meaning, restore fidelity

# What to preserve VERBATIM — mathematical fidelity is non-negotiable

1. **Math spans** — byte-for-byte: LaTeX commands, variable names, spacing, ordering, AND delimiter. The blog uses standard delimiters: inline `$...$`, display (centered, standalone) `$$...$$`. The COUNT and ORDER of both kinds MUST match the KO source exactly. NEVER swap one for the other — no downgrading a `$$...$$` display block into inline `$...$`, no promoting inline into display. Easiest rule: never touch anything between math delimiters, and never change a delimiter's length. A single `$` inside `\\text{...}`/`\\tag{...}` is LaTeX re-entering math mode from text mode — leave it.
2. **Fenced theorem-box `:::` openers** — every `:::` fence line (the labeled opener and the bare `:::` closer) stays in place, with the same count and order. The opener's derived anchor MUST be unchanged: the kind→prefix mapping (Definition→def, Proposition→prop, Theorem→thm, Lemma→lem, Corollary→cor, Example→ex, Remark→rmk) plus the integer N, and every `::: misc … {#id}` keeps its `{#id}`. Never change N.
3. Cross-reference **paths** (`/en/math/...`) and **anchors** (`#def1`, `#prop2`) — unchanged. Visible labels may be lightly refined only if materially clearer.
   - **Verification rule**: do NOT change an anchor target or invent a new `[display](url)` pairing unless you have actually seen the target with that exact form. If unsure, leave the existing form untouched.
4. Fenced `:::` blocks (opener label already in English from the initial translation — keep it English), any legacy theorem-box HTML that remains (`<div class="...">`, `<ins id="...">**...**</ins>`, `<details class="proof"><summary>...</summary>`), and inline HTML (`<sub>...</sub>`, `<cap>`, `<em>`) — keep exactly, with ids and numbers unchanged.
5. Section headers (`## ...`) — keep as-is unless genuinely wrong.
6. Footnote markers `[^N]` and identifiers — unchanged.
7. References: the bibliography is handled OUTSIDE this polish. If the body contains the literal line `@@REFERENCES@@`, copy that line verbatim, exactly once, in the same position. NEVER write a References section or bibliography entries yourself.

# Self-check before responding

- Same math delimiters as the KO body — as many `$$...$$` display spans and as many `$...$` inline spans; none downgraded, none promoted.
- Every `:::` opener present with its derived anchor (kind→prefix + N) unchanged and every `::: misc … {#id}` intact; `:::` line count and order match the KO source.
- No Korean labels remain (정의, 명제, 정리, 보조정리, 따름정리, 예시, 참고, 증명, 참고문헌).
- No Korean prose remains — every sentence of the output is English.
- If the input contained the line `@@REFERENCES@@`, the output contains it verbatim, exactly once.
- Output is body only — no frontmatter or `---` lines.

# Style anchors

- First-person plural ("we ...") throughout.
- Precise, technical, declarative; match the user's canonical voice in other posts.
- No "translator notes", no meta-commentary, no apologies.
- Do not restructure paragraphs unless the original is broken.

# Input format

You will receive:
- Korean source body between `--- KO BODY ---` / `--- END KO BODY ---`
- Current English translation body between `--- EN BODY ---` / `--- END EN BODY ---`

Output ONLY the polished English body."""


def build_polish_prompt(ko_body: str, en_body: str) -> str:
    return (
        POLISH_INSTRUCTIONS
        + "\n\n--- KO BODY ---\n"   + ko_body + "\n--- END KO BODY ---\n"
        + "\n--- EN BODY ---\n"     + en_body + "\n--- END EN BODY ---\n"
    )


# ---------------------------------------------------------------------------
# Kimi invocation
# ---------------------------------------------------------------------------

_FENCE_RE     = re.compile(r"^\s*```(?:markdown|md)?\s*\n|\n```\s*$", re.MULTILINE)


def _parse_json_object(out: str) -> dict:
    """모델이 낸 JSON 을 관대하게 파싱한다.

    `_FENCE_RE` 는 ```markdown / ```md / bare ``` 만 벗기므로 ```json 은 그대로 남아
    파싱이 터졌다. 여기서는 **어떤 언어 태그든** 벗겨내고, 그래도 안 되면 첫 `{` 부터
    마지막 `}` 까지를 떼어 다시 시도한다 (모델이 앞뒤로 군말을 붙인 경우).

    본문 경로에는 쓰지 않는다 — 본문은 코드블럭으로 시작·끝날 수 있어서 펜스를 넓게
    벗기면 진짜 코드블럭을 먹는다.
    """
    t = out.strip()
    t = re.sub(r"\A```[A-Za-z0-9_+-]*[ \t]*\n", "", t)
    t = re.sub(r"\n```[ \t]*\Z", "", t).strip()
    try:
        return json.loads(t)
    except json.JSONDecodeError:
        i, j = t.find("{"), t.rfind("}")
        if i == -1 or j <= i:
            raise
        return json.loads(t[i:j + 1])

_MATH_BLOCK_RE = re.compile(r"\$\$.*?\$\$", re.DOTALL)
_KO_PATH_RE    = re.compile(r"/ko/[A-Za-z0-9_\-/]+")


# ---------------------------------------------------------------------------
# Theorem-box syntax (fenced `:::` + residual Style-A HTML)
# ---------------------------------------------------------------------------
# The source markdown now carries pandoc-style `::: <label>` theorem boxes,
# which a Jekyll :pre_render plugin (_plugins/fenced_theorem_blocks.rb) expands
# to the old Style-A HTML (<div class>/<ins id>/<details class="proof">) at
# build time. The migration converted only the byte-exact-invertible blocks;
# ~167 non-canonical blocks across the Math corpus were intentionally LEFT as
# raw Style-A HTML. So the source is a MIX of both forms and the worker must
# handle their UNION.
#
# Anchor id derivation:
#   ::: 정리 2 (name)  / ::: Theorem 2 (name)   -> derived id thm2  (kind+number)
#   ::: misc <label> {#conj4}                   -> explicit id conj4
#   ::: 증명 | ::: Proof | ::: 증명 (정리 4)      -> proof: NO id
#   <ins id="def9">**정의 9**</ins> …            -> residual raw HTML: id def9
# Fence-/raw-aware: a `:::` or `<ins>` inside ``` code fences or {% raw %} blocks
# is ignored, exactly as the plugin ignores it.

# 박스 어휘의 단일 출처 = _data/theorem_vocab.yml.
# 플러그인 KIND_MAP 과 같은 파일에서 파생하므로 새 종류를 더해도 여기는 무변경.
_VOCAB = yaml.safe_load(
    (BLOG_ROOT / "_data" / "theorem_vocab.yml").read_text(encoding="utf-8"))

_KIND_PREFIX = {k["ko"]: k["prefix"] for k in _VOCAB["kinds"]} \
             | {k["en"]: k["prefix"] for k in _VOCAB["kinds"]}
_KIND_ALT = "|".join(re.escape(k) for k in sorted(_KIND_PREFIX, key=lambda s: -len(s)))
_DERIVED_LABEL_RE = re.compile(r"^(" + _KIND_ALT + r")[ \t]+(\d+)")
_MISC_LABEL_RE    = re.compile(r"^misc[ \t]+(.+?)[ \t]*\{#([^}]+)\}[ \t]*$")

# Opener carrying a label (bare closing `:::` has no label and won't match).
_FENCE_LABEL_RE     = re.compile(r"^:::[ \t]+(.+?)[ \t]*$")
_INS_LINE_RE        = re.compile(r'<ins\s+id="([^"]+)"')      # residual Style-A HTML
_CODEFENCE_OPEN_RE  = re.compile(r"^ {0,3}(`{3,}|~{3,})")
_CODEFENCE_CLOSE_RE = re.compile(r"^ {0,3}(`{3,}|~{3,})[ \t]*$")
_RAW_OPEN_RE        = re.compile(r"^\s*\{%\s*raw\s*%\}\s*$")
_RAW_CLOSE_RE       = re.compile(r"^\s*\{%\s*endraw\s*%\}\s*$")
_HANGUL_RE          = re.compile(r"[가-힣]")


def _fenced_block_id(label: str) -> Optional[str]:
    """Anchor id for a `::: ` opener label, mirroring the plugin's derivation.

    Returns the id for box blocks (a misc block's explicit `{#id}`, or a derived
    box's kind→prefix + number), or None for proof blocks and anything the
    plugin would not recognize (those carry no anchor id)."""
    m = _MISC_LABEL_RE.match(label)
    if m:
        return m.group(2)
    m = _DERIVED_LABEL_RE.match(label)
    if m:
        return _KIND_PREFIX[m.group(1)] + m.group(2)
    return None


def _iter_source_lines(text: str):
    """Yield (line_index, line) for every line OUTSIDE ``` code fences and
    {% raw %} blocks — the plugin's exact fence-/raw-aware scan. Fence/raw
    delimiter lines and everything between them are skipped."""
    in_fence = in_raw = False
    fchar = ""
    flen = 0
    for idx, line in enumerate(text.split("\n")):
        if in_raw:
            if _RAW_CLOSE_RE.match(line):
                in_raw = False
            continue
        if not in_fence and _RAW_OPEN_RE.match(line):
            in_raw = True
            continue
        if in_fence:
            mc = _CODEFENCE_CLOSE_RE.match(line)
            if mc and mc.group(1)[0] == fchar and len(mc.group(1)) >= flen:
                in_fence = False
            continue
        mo = _CODEFENCE_OPEN_RE.match(line)
        if mo:
            in_fence = True
            fchar = mo.group(1)[0]
            flen = len(mo.group(1))
            continue
        yield idx, line


def _iter_fence_openers(text: str):
    """Yield (line_index, label) for each `::: <label>` opener OUTSIDE fences/raw.
    The bare closing `:::` has no label and is not yielded."""
    for idx, line in _iter_source_lines(text):
        m = _FENCE_LABEL_RE.match(line)
        if m:
            yield idx, m.group(1)


def _box_anchors(text: str) -> list:
    """[(id, line_index), ...] for every theorem-box anchor in document order:
    a `:::` box opener (derived/misc) OR a residual raw `<ins id>` line. Both
    forms coexist in the source (see module note). Proof openers carry no id and
    are skipped, so a proof folds into the preceding box's region — the same
    alignment the old <ins>-only split had (a proof <details> held no <ins id>).
    """
    out = []
    for idx, line in _iter_source_lines(text):
        m = _FENCE_LABEL_RE.match(line)
        if m:
            bid = _fenced_block_id(m.group(1))
            if bid is not None:
                out.append((bid, idx))
            continue
        mi = _INS_LINE_RE.search(line)
        if mi:
            out.append((mi.group(1), idx))
    return out


def _box_ids(text: str) -> set:
    """Set of theorem-box anchor ids in text (fenced-derived ∪ residual <ins id>).
    Equals the <ins id> set the plugin ultimately emits."""
    return {bid for bid, _ln in _box_anchors(text)}


def _fenced_residual_ko_labels(text: str) -> list:
    """`:::` openers whose label still contains Korean text — an untranslated
    label the id-set check cannot catch (a KO opener and its EN form derive the
    SAME id) and label_audit misses (it only scans **bold**/§/⁋/headers/
    <summary>, not `:::` openers). A correctly translated EN opener never
    contains Hangul, so a Hangul scan of the opener label is precise. (Residual
    KO in raw `<ins>**정의 N**</ins>` HTML is already caught by label_audit's
    **bold** rule.) Fence-/raw-aware."""
    return [
        f"line {idx + 1}: untranslated KO text in fenced opener {label!r}"
        for idx, label in _iter_fence_openers(text)
        if _HANGUL_RE.search(label)
    ]


def _body_after_frontmatter(text: str) -> str:
    m = _FRONTMATTER_RE.match(text)
    return text[m.end():] if m else text


def _fm_top_keys(text: str) -> set[str]:
    m = _FRONTMATTER_RE.match(text)
    if not m:
        return set()
    keys: set[str] = set()
    for line in m.group(1).splitlines():
        if not line or line[0] in (" ", "\t", "#", "-"):
            continue
        if ":" in line:
            keys.add(line.split(":", 1)[0].strip())
    return keys


def _strip_math_and_glosses(body: str) -> str:
    """한글 잔류를 세기 전에 수식 span 과 `<sub>` 병기를 걷어낸다.

    수식 안의 `\\text{한글}` 과 병기용 gloss 는 정상적인 한글이므로 세면 안 된다.
    참고문헌 블록(한국어 서지를 인용할 수 있다)은 호출자가 이미 제외한다.
    """
    prose = re.sub(r"<sub>.*?</sub>", "", body, flags=re.DOTALL)
    prose = re.sub(r"\$\$.*?\$\$", "", prose, flags=re.DOTALL)
    return re.sub(r"\$[^$\n]*\$", "", prose)


def validate_translation(
    translated: str,
    *,
    ko_content: str,
    reason: str,
    en_current: Optional[str],
    warnings: Optional[list] = None,
) -> Optional[str]:
    """Return None on success, error string on hard failure.

    `warnings`, if provided, is appended with non-blocking issues (logged + notified
    by caller, but the translation is still accepted).
    """
    if warnings is None:
        warnings = []

    if not _FRONTMATTER_RE.match(translated):
        return "frontmatter missing or malformed (no enclosing --- block)"

    # Truncation: output body must be >= 60% of KO body. For polish, ALSO require
    # >= 85% of en_current — polish should never significantly shrink the post,
    # so a big drop signals the model truncated mid-output (Modules.md 2026-05-25
    # incident: file ended mid-sentence at thm10 yet passed the 60% gate).
    out_body = _body_after_frontmatter(translated).strip()
    ko_body  = _body_after_frontmatter(ko_content).strip()
    if ko_body and len(out_body) < TRUNCATION_RATIO * len(ko_body):
        return (
            f"output body {len(out_body)}c < {TRUNCATION_RATIO:.0%} of ko "
            f"{len(ko_body)}c — truncation suspected"
        )
    if reason == "polish" and en_current:
        en_body = _body_after_frontmatter(en_current).strip()
        if en_body and len(out_body) < 0.85 * len(en_body):
            return (
                f"polish output body {len(out_body)}c < 85% of en_current "
                f"{len(en_body)}c — polish truncation suspected"
            )

    # References: the engine never sees the block (extract/reattach in
    # translate()), so EN entries must be byte-identical to KO's. A mismatch
    # means another path (incremental drift, manual EN edit) altered or
    # invented entries.
    _, ko_refs_blk = extract_refs_block(_body_after_frontmatter(ko_content).strip())
    en_wo_refs, en_refs_blk = extract_refs_block(out_body)

    # 한글 잔류 검사가 참고문헌 대조보다 먼저다. 엔진이 번역 대신 KO 를 인용한
    # 대역 워크시트를 내놓으면 참고문헌 마커도 함께 망가지는데, 참고문헌 검사가
    # 먼저 return 하면 "참고문헌 없음"이라는 지엽적인 이름으로 보고되어 진짜
    # 실패(번역이 아예 안 됨)를 가린다.
    prose = _strip_math_and_glosses(en_wo_refs)
    hangul = re.findall(r"[가-힣]", prose)
    if len(hangul) > HANGUL_RESIDUE_MAX:
        sample = "".join(hangul[:20])
        return (
            f"{len(hangul)} Hangul chars in body (max {HANGUL_RESIDUE_MAX}) — "
            f"untranslated prose suspected, e.g. {sample!r}"
        )

    if en_refs_blk is not None and ko_refs_blk is None:
        return "references section present in EN but absent in KO — invented references"
    if ko_refs_blk is not None and en_refs_blk is None:
        return "references section missing in EN (present in KO)"
    if ko_refs_blk and en_refs_blk:
        ko_entries = ko_refs_blk.split("\n", 1)[1]
        en_entries = en_refs_blk.split("\n", 1)[1]
        if ko_entries != en_entries:
            return "references entries differ from KO source"

    # Residual Korean prose: a lazy engine can pass every structural gate below
    # by returning the KO body near-verbatim (headings/labels translated, prose
    # copied — the copy has identical math profile, box ids, and length, and the
    # worker's own post-processing anglicizes labels and /ko/ paths, so nothing
    # structural is left to fail). The hard-fail threshold is checked above,
    # before the references comparison; what remains here is the sub-threshold
    # warning.
    if hangul:
        # Sub-threshold residue is accepted (may be a legitimate bibliography
        # entry or Korean-terminology mention) but always surfaced for human
        # review — warnings containing "Hangul" bypass the verdict-safe
        # telegram suppression and set needs_review on the state entry.
        sample = "".join(hangul[:20])
        warnings.append(
            f"{len(hangul)} Hangul chars in body (≤{HANGUL_RESIDUE_MAX}, "
            f"needs review) — e.g. {sample!r}"
        )

    # Korean anchors on /en/ links: the KO source's section anchors are Hangul
    # slugs; the mechanical /ko/→/en/ rewrite keeps them, but EN pages have
    # English heading slugs, so the anchor 404s. The correct EN slug needs the
    # target page, which the engine cannot see — warn (telegram) instead of
    # failing, and fix by hand.
    ko_anchors = re.findall(r"\]\(/en/[^)\s#]*#[^)\s]*[가-힣][^)\s]*\)", out_body)
    if ko_anchors:
        warnings.append(
            f"{len(ko_anchors)} Hangul anchor(s) on /en/ links, "
            f"e.g. {ko_anchors[0]!r}"
        )

    # Math block count: WARN ONLY. Strip <sub>...</sub> first (bilingual glosses
    # are dropped per translation rules, which legitimately reduces the count).
    # False positives (rephrasings that merge/split blocks) are common enough that
    # a hard fail wastes a whole day per file; we log + notify instead.
    _SUB_RE = re.compile(r"<sub>.*?</sub>", re.DOTALL)
    # 수식 구분자 프로필: (디스플레이 `$$...$$` 수, 인라인 `$...$` 수). 수식 내용은
    # verbatim 보존이 원칙이므로 KO 와 EN 이 정확히 같아야 한다. 어긋나면 모델이 구분자를
    # 바꾼 것이다 — 특히 디스플레이를 인라인으로 낮추면 가운데 정렬 수식이 문장 속으로
    # 들어가 버린다. (`<sub>` 한영병기는 ko/en 이 서로 다르므로 빼고 센다.)
    ko_math = math_profile(_SUB_RE.sub("", ko_content))
    en_math = math_profile(_SUB_RE.sub("", translated))
    if ko_math != en_math:
        warnings.append(
            f"math block count mismatch: ko=display {ko_math[0]}/inline {ko_math[1]}, "
            f"en=display {en_math[0]}/inline {en_math[1]}"
        )

    # Theorem-box anchor ids must match the KO source exactly. Ids come from the
    # `:::` openers (kind→prefix + number for derived boxes, the explicit `{#id}`
    # for misc boxes — the same derivation the pre_render plugin uses to emit
    # <ins id>) UNIONed with any residual raw `<ins id>` HTML the migration left
    # un-converted. Proof openers carry no id.
    ko_ids = _box_ids(ko_content)
    en_ids = _box_ids(translated)
    if ko_ids != en_ids:
        missing = sorted(ko_ids - en_ids)
        extra   = sorted(en_ids - ko_ids)
        return f"fenced box id mismatch: missing={missing} extra={extra}"

    # An untranslated KO label left on a `:::` opener slips past BOTH the id
    # check (a KO opener and its EN form derive the same id) and label_audit
    # (which never looks at `:::` openers), so check it directly.
    residual_fenced = _fenced_residual_ko_labels(translated)
    if residual_fenced:
        more = f" (+{len(residual_fenced)-1} more)" if len(residual_fenced) > 1 else ""
        return f"untranslated fenced label — {residual_fenced[0]}{more}"

    # No /ko/ paths in body (must all be /en/)
    body = _body_after_frontmatter(translated)
    ko_paths = _KO_PATH_RE.findall(body)
    if ko_paths:
        return f"{len(ko_paths)} /ko/ path(s) in body, e.g. {ko_paths[0]!r}"

    # Residual KO labels (delegated to label_normalize.audit_text)
    label_issues = label_audit(translated)
    if label_issues:
        more = f" (+{len(label_issues)-1} more)" if len(label_issues) > 1 else ""
        return f"residual KO label — {label_issues[0]}{more}"

    # Frontmatter keys: ko ⊆ en (en may add translated_at / translation_source /
    # last_polished_at). _KO_ONLY_KEYS are deliberately stripped by
    # _compose_en_frontmatter, so they must be exempt here — otherwise every
    # translation of a drift-flagged post fails validation and the worker
    # re-translates it forever (this is exactly what happened on 2026-07-12).
    ko_keys = _fm_top_keys(ko_content) - set(_KO_ONLY_KEYS)
    en_keys = _fm_top_keys(translated)
    missing_keys = ko_keys - en_keys
    if missing_keys:
        return f"frontmatter keys dropped: {sorted(missing_keys)}"

    return None


def call_kimi(prompt: str, *, thinking: bool = False,
              agent_file: Optional[str] = None,
              mcp_config_file: Optional[str] = None) -> str:
    """Invoke `kimi --quiet` with prompt on stdin, return final assistant message.

    Thinking is OFF by default — it shares the 32K output-token budget with the
    actual response, and on large posts (e.g. Modules.md 2026-05-25) the model
    can burn the entire budget on internal reasoning and then truncate the
    visible output. Callers that need analytical depth (e.g. verify) opt in.

    agent_file / mcp_config_file override the agent spec and MCP config. The
    default kimi agent is agentic with a full toolset (Shell, Grep, ReadFile,
    SearchWeb, …); on a single-shot analysis prompt (everything inlined, no
    files to read) the model still reaches for Shell/Grep to "count the blocks"
    and loops dozens of tool-call steps, re-reading the whole context as
    cache_read each step. The verify audit did exactly this — median 18, up to
    177 steps/turn, ~96% of ALL Kimi cron tokens (2026-05). Pointing the verify
    call at a no-tools agent (verify-agent.yaml, allowed_tools: []) + an empty
    MCP config forces a direct one-step answer (validated: complete, correctly
    formatted verdict, exit 0, ~50K tokens/post vs millions before). A step cap
    is NOT a safe substitute — the model spends step 1 on the tool call, so any
    low cap truncates before the verdict and exits non-zero on big posts.
    """
    if TRANSLATOR_BACKEND == "glm":
        # claudeglm -p: 헤드리스 단발. 도구는 안 준다 (allowedTools 미지정 =
        # 전부 거부) — 위의 Kimi agentic-loop 폭주와 같은 사고를 원천 차단.
        # thinking/agent_file/mcp_config_file 은 kimi 전용이라 무시된다.
        args = [GLM_BIN, "-p", "--output-format", "text"]
    else:
        args = [KIMI_BIN, "--quiet", "--print", "--final-message-only",
                "--thinking" if thinking else "--no-thinking"]
        if agent_file is not None:
            args += ["--agent-file", agent_file]
        if mcp_config_file is not None:
            args += ["--mcp-config-file", mcp_config_file]
    proc = subprocess.run(
        args,
        input=prompt,
        capture_output=True,
        text=True,
        timeout=KIMI_TIMEOUT_SEC,
        cwd="/tmp",                          # isolate from blog tree (we do all IO)
    )
    if proc.returncode != 0:
        raise RuntimeError(
            f"{Path(args[0]).name} CLI exited {proc.returncode}: "
            f"stderr={proc.stderr.strip()[:500]!r}"
        )
    out = proc.stdout
    if not out.strip():
        raise RuntimeError(f"{Path(args[0]).name} returned empty output; "
                           f"stderr={proc.stderr.strip()[:500]!r}")
    # Defensive: strip code fences if Kimi wrapped output
    out = _FENCE_RE.sub("", out).strip() + "\n"
    # Defensive: Kimi occasionally outputs `---title: ...` with no newline
    # after the opening triple-dash. _FRONTMATTER_RE (and the rest of the
    # pipeline) then silently no-ops, leaving the EN file with corrupt
    # frontmatter. Normalize here.
    if out.startswith("---") and len(out) > 3 and out[3] != "\n":
        out = "---\n" + out[3:]
    return out


def _group_regions(regions, max_chars: int) -> list:
    """연속한 region 들을 max_chars 이하의 조각으로 묶는다.

    region 은 본문의 연속된 slice 이므로 한 묶음 안의 텍스트를 이어 붙이면 원문이
    그대로 나온다. 혼자서 max_chars 를 넘는 region 은 쪼개지 않고 그대로 한 조각이
    된다 — 정리 박스 하나를 두 호출에 걸쳐 자르면 `:::` 짝이 깨진다.
    """
    batches: list = []
    cur: list = []
    cur_len = 0
    for _rid, text in regions:
        if cur and cur_len + len(text) > max_chars:
            batches.append("".join(cur))
            cur, cur_len = [], 0
        cur.append(text)
        cur_len += len(text)
    if cur:
        batches.append("".join(cur))
    return [b for b in batches if b.strip()]


def translate_body_chunked(ko_body: str) -> Tuple[str, int]:
    """큰 본문을 조각내어 번역하고 이어 붙인다. 반환은 (EN 본문, 프롬프트 총 길이)."""
    batches = _group_regions(_split_regions(ko_body), MAX_CHUNK_CHARS)
    outs: list = []
    prompt_chars = 0
    log(f"chunked translation: ko body {len(ko_body)}c → {len(batches)} chunk(s)")
    for i, chunk in enumerate(batches, start=1):
        prompt = build_chunk_prompt(chunk, i, len(batches))
        prompt_chars += len(prompt)
        log(f"  chunk {i}/{len(batches)}: ko {len(chunk)}c")
        outs.append(call_kimi(prompt).strip())
    return "\n\n".join(o for o in outs if o) + "\n", prompt_chars


def translate(
    ko_path: Path,
    translated_at_iso: str,
    *,
    reason: str,
    en_path: Optional[Path] = None,
    warnings: Optional[list] = None,
) -> Tuple[str, int, int]:
    """Translate or polish a KO post into EN.

    Pipeline:
      1. Split KO into frontmatter + body.
      2. Determine EN title/excerpt/description:
         - translate: kimi small task on KO frontmatter values.
         - polish: prefer existing EN values; only translate fields missing
           from EN (e.g. description, added later via the KO description batch).
      3. Body translation/polish: kimi main call. Output is body only — no
         frontmatter handling on the LLM side.
      4. Body post-processing: label_fix, strip residual <sub>, mechanical
         /ko/ → /en/ (the validator no longer hard-fails on /ko/ residue;
         we just normalise it).
      5. Compose EN frontmatter deterministically from KO frontmatter
         (permalink /ko/→/en/, sidebar.nav -ko→-en, translated fields, meta).
      6. Validate the assembled output (math count, fenced box ids, label residue).
    """
    ko_content = ko_path.read_text(encoding="utf-8")
    ko_fm_text, ko_body = _split_fm_block(ko_content)

    en_current: Optional[str] = None
    en_current_fm_text, en_current_body = "", ""
    if reason == "polish" and en_path is not None and en_path.exists():
        en_current = en_path.read_text(encoding="utf-8")
        en_current_fm_text, en_current_body = _split_fm_block(en_current)

    # ---- Step 1: title / excerpt / description ----
    en_fields: dict = {}
    fields_to_translate: dict = {}
    for key in _LLM_FRONTMATTER_FIELDS:
        ko_val = _extract_fm_scalar(ko_fm_text, key)
        if not ko_val:  # missing or empty in KO → skip the field entirely
            continue
        if reason == "polish" and en_current_fm_text:
            existing = _extract_fm_scalar(en_current_fm_text, key)
            if existing:
                en_fields[key] = existing
                continue
        fields_to_translate[key] = ko_val
    if fields_to_translate:
        en_fields.update(_translate_fm_fields_via_kimi(fields_to_translate))

    # ---- Step 2: body translation / polish ----
    # 참고문헌 격리: 엔진에는 sentinel만 보내고 KO 블록을 verbatim 재부착한다.
    ko_body, ko_refs = extract_refs_block(ko_body)
    if reason == "polish" and en_current_body.strip():
        en_current_body, _ = extract_refs_block(en_current_body)
        prompt = build_polish_prompt(ko_body, en_current_body)
        en_body = call_kimi(prompt)
        prompt_chars = len(prompt)
    elif len(ko_body) > FULL_CHUNK_THRESHOLD:
        en_body, prompt_chars = translate_body_chunked(ko_body)
    else:
        prompt = build_prompt(ko_body)
        en_body = call_kimi(prompt)
        prompt_chars = len(prompt)
    engine_out = en_body                         # 검증 실패 시 덤프용 원본

    # ---- Step 3: body post-processing ----
    en_body, _n_fixed = label_fix(en_body)
    en_body = re.sub(r"<sub>[^<]*?</sub>", "", en_body)
    # <em-ko>(및 오타 <em_ko>)는 KO 전용 한국어 강조 태그 — EN에는 plain 강조로
    # 치환한다 (2026-07-21 룰링; md_lint가 en/ 신설을 경고).
    en_body = re.sub(r"<em[-_]ko>(.*?)</em[-_]ko>", r"*\1*", en_body, flags=re.DOTALL)
    # Mechanical /ko/ → /en/ for any cross-refs the LLM forgot to convert.
    # Blanket substring replacement; the math blog body never has legitimate
    # `/ko/` in prose or code, so we don't need a guarded regex.
    en_body = en_body.replace("/ko/", "/en/")
    # 수식 구분자는 더 이상 정규화하지 않는다. 2026-07-13 부터 인라인은 표준 `$...$`,
    # 디스플레이는 `$$...$$` 이므로, 모델이 원래 내던 출력이 곧 정답이다. 남은 위험
    # (KO 의 디스플레이를 인라인으로 낮추는 것) 은 validate_translation 의 KO/EN
    # 수식 프로필 대조가 잡는다. 자세한 배경은 math_delimiters.py 참고.
    en_body = reattach_refs_block(en_body, ko_refs)

    # ---- Step 4: compose final EN file ----
    polished_at_iso = translated_at_iso if reason == "polish" else None
    en_fm = _compose_en_frontmatter(
        ko_fm_text, en_fields,
        translated_at_iso=translated_at_iso,
        polished_at_iso=polished_at_iso,
    )
    translated = f"---\n{en_fm}---\n{en_body.lstrip(chr(10))}"

    # ---- Step 5: validate assembled output ----
    err = validate_translation(
        translated, ko_content=ko_content, reason=reason,
        en_current=en_current, warnings=warnings,
    )
    if err:
        dump_failure(ko_path, err, engine_out=engine_out, assembled=translated)
        raise RuntimeError(f"validation failed: {err}")
    return translated, prompt_chars, len(translated)


HERMES_BIN = shutil.which("hermes") or str(Path.home() / ".local/bin/hermes")


def _notify_telegram(subject: str, body: str) -> None:
    """Best-effort hermes telegram notify; logs (but doesn't raise) on failure."""
    try:
        r = subprocess.run(
            [HERMES_BIN, "send", "-t", "telegram", "-s", subject, "-q", body],
            check=False, timeout=15, capture_output=True, text=True,
        )
        if r.returncode != 0:
            log(f"telegram notify failed rc={r.returncode}: {r.stderr.strip()[:300]!r}")
    except Exception as e:
        log(f"telegram notify exception: {e!r}")


def record_failure(state: dict, key: str, error: str) -> None:
    """번역 실패를 state 에 남기고, 쿨다운을 지켜 텔레그램으로 알린다.

    엔트리를 통째로 갈아끼우지 않고 **덮어쓴다**. translated_at·en_path·
    verified_at·verify_* 는 그 글의 번역 이력이고 실패는 그 위에 얹히는 상태다.
    갈아끼우면 EN 파일은 그대로인데 이력만 사라져서, Phase 4 가 verified_at 이
    없어진 글을 다시 검증하고(haiku 헛돈) 대시보드·term-extract 가 이미 번역된
    글을 미번역으로 센다.

    실패 자체는 로그에만 남던 것을 알림까지 잇는다. 24 시간 백오프가 다음 글로
    넘겨 주기 때문에 큐는 안 막히지만, 엔진 쿼터가 소진되면 아무 EN 도 안 나가는
    상태가 알림 없이 며칠 이어진다 (2026-08-30 ~ 08-31 실측: 실패 10 회, 알림 0 통).
    """
    now = time.time()
    entry = dict(state["files"].get(key) or {})
    entry.update({"status": "failed", "last_attempt_ts": now, "error": error[:500]})
    state["files"][key] = entry

    notice = state.setdefault("failure_notice", {})
    notice["count"] = int(notice.get("count", 0)) + 1
    notice.setdefault("since", now)
    if now - notice.get("last_notified", 0) < FAIL_NOTIFY_COOLDOWN_SEC:
        return
    notice["last_notified"] = now
    since = datetime.fromtimestamp(notice["since"]).strftime("%m-%d %H:%M")
    _notify_telegram(
        "[translate-worker] 번역 실패",
        f"{key}\n연속 {notice['count']}회 (최초 {since})\n"
        f"{error[:300]}\n"
        f"실패한 글은 {FAIL_RETRY_AFTER_SEC // 3600}시간 뒤 자동 재시도한다.",
    )


# ---------------------------------------------------------------------------
# Math-mismatch verification (Kimi second opinion)
# ---------------------------------------------------------------------------

_SUB_STRIP_RE = re.compile(r"<sub>.*?</sub>", re.DOTALL)

# A KO/EN `$$`-count mismatch is almost always a `$$display$$`→`$inline$`
# downgrade (the LaTeX survives, only the delimiter changed) or a harmless
# merge/split — not lost content. We localize the real divergences mechanically
# and only ask Kimi about the few regions where math genuinely went missing.
#
# Key fact: the LaTeX inside `$$...$$` is identical in KO and EN (math isn't
# translated). So a KO block "survives" iff its whitespace-normalized LaTeX
# appears anywhere in EN's math — display OR inline. Blocks that pass that check
# are benign by construction (no model needed); only blocks whose content is
# absent from EN entirely are suspect, and Kimi sees just those `:::` box regions
# — and is never told about `$$`/counts, so it can't loop on counting.

_DISPLAY_RE = re.compile(r"\$\$(.*?)\$\$", re.DOTALL)
_INLINE_RE  = re.compile(r"\$([^$\n]+?)\$")
# 수식 스팬 하나 — 단일 출처 md_lint._MATH_SPAN_RE (파일 머리 import 참고).
# `$$...$$` 를 먼저 시도하므로 `$$` 를 single-$ 두 개로 쪼개지 않는다
# (kramdown 의 inline_math 파서와 같은 교대 순서). 그룹 구조도 동일:
# group(1)=display 본문, group(2)=inline 본문 — _span_tex 가 이에 의존한다.
_MATH_SPAN_RE = _md_lint._MATH_SPAN_RE


def _span_tex(m: "re.Match") -> str:
    """_MATH_SPAN_RE 매치에서 LaTeX 본문만 꺼낸다 (display 든 inline 이든)."""
    return m.group(1) if m.group(1) is not None else m.group(2)
_PREAMBLE   = "__preamble__"
_VERIFY_MAX_REGIONS = 12


def _norm_math(s: str) -> str:
    """Whitespace-insensitive key for matching LaTeX across KO/EN."""
    return re.sub(r"\s+", "", s)


def _en_math_inventory(en: str) -> set:
    """Every math fragment in EN — `$$display$$` AND `$inline$` (the downgrade
    target) — normalized, so we can ask 'does this KO block survive anywhere?'."""
    body = _SUB_STRIP_RE.sub("", en)
    disp = _DISPLAY_RE.findall(body)
    inline = _INLINE_RE.findall(_DISPLAY_RE.sub("", body))
    return {_norm_math(x) for x in (*disp, *inline)}


def _box_regions(text: str) -> dict:
    """id -> region text (its box-anchor line up to the next box anchor). Text
    before the first anchor is filed under _PREAMBLE."""
    lines = text.split("\n")
    anchors = _box_anchors(text)
    out = {}
    first = anchors[0][1] if anchors else len(lines)
    out[_PREAMBLE] = "\n".join(lines[:first])
    for i, (aid, ln) in enumerate(anchors):
        end = anchors[i + 1][1] if i + 1 < len(anchors) else len(lines)
        out[aid] = "\n".join(lines[ln:end])
    return out


def _locate_divergences(ko: str, en: str):
    """(benign_count, suspect_region_ids).

    benign_count — KO blocks missing from EN's `$$` sequence whose LaTeX still
                   survives somewhere in EN (pure `$$`→`$` downgrade / rephrase).
    suspect_ids  — ordered `:::` box ids (or _PREAMBLE) whose region holds a KO
                   block whose LaTeX is absent from EN entirely.

    `:::` box anchors are the alignment unit because their derived id is identical
    across KO/EN and survives the `$$`→`$` downgrade 1:1, whereas matched `$$`
    blocks go sparse exactly in the downgrade-heavy posts we care about (EN keeps
    ~20% of KO's `$$`), which misaligns any block-bracketed window."""
    ko_body, en_body = _SUB_STRIP_RE.sub("", ko), _SUB_STRIP_RE.sub("", en)
    # 디스플레이와 인라인을 **둘 다** 센다. 2026-07-13 부터 본문 수식의 90% 이상이
    # 인라인 `$...$` 이므로, 예전처럼 `$$` 블록만 훑으면 인라인 수식이 통째로
    # 사라져도 "0 differing block" 이라며 통과해 버린다.
    ko_iter = list(_MATH_SPAN_RE.finditer(ko_body))
    ko_blocks = [_norm_math(_span_tex(m)) for m in ko_iter]
    ko_lines = [ko_body.count("\n", 0, m.start()) for m in ko_iter]
    en_blocks = [_norm_math(_span_tex(m)) for m in _MATH_SPAN_RE.finditer(en_body)]
    inventory = _en_math_inventory(en)

    sm = difflib.SequenceMatcher(None, ko_blocks, en_blocks, autojunk=False)
    missing = []
    for tag, i1, i2, _j1, _j2 in sm.get_opcodes():
        if tag in ("delete", "replace"):
            missing.extend(range(i1, i2))

    anchors = _box_anchors(ko_body)

    def enclosing(line: int) -> str:
        cur = _PREAMBLE
        for aid, ln in anchors:
            if ln <= line:
                cur = aid
            else:
                break
        return cur

    benign = 0
    suspect_ids: list = []
    for idx in missing:
        if idx >= len(ko_blocks):
            continue
        if ko_blocks[idx] in inventory:
            benign += 1
            continue
        rid = enclosing(ko_lines[idx])
        if rid not in suspect_ids:
            suspect_ids.append(rid)
    return benign, suspect_ids


def _cap_region(text: str, limit: int = 4500) -> str:
    """Trim a region to ~limit chars, ending on a line boundary when possible.

    A truncation marker is appended so the semantic check never mistakes an
    end-truncated passage for dropped content (regions rarely exceed the cap;
    the marker only matters for the occasional very long proof)."""
    if len(text) <= limit:
        return text
    cut = text.rfind("\n", 0, limit)
    return text[: cut if cut > limit // 2 else limit] + "\n…[passage truncated here — ignore any apparent missing content past this point]"


def _finalize_verdict(out: str) -> str:
    """Keep only from the LAST `VERDICT:` line. Even in thinking mode the model
    can occasionally restate a first-impression verdict before its final one;
    main() parses the verdict with a MULTILINE `^VERDICT:` search that would
    otherwise latch onto the premature one. The last verdict is the decision."""
    starts = [m.start() for m in re.finditer(r"(?m)^VERDICT:", out)]
    return out[starts[-1]:] if starts else out


VERIFY_SEM_INSTRUCTIONS = """You compare passages from a Korean math blog post against their English translation, to catch any loss of meaning.

For each numbered pair below, decide whether the English conveys the SAME mathematical content as the Korean: is any statement, hypothesis, conclusion, definition, formula, or symbol dropped, added, or changed in meaning? Pure rewording, reordering, or different notation/formatting is NOT a problem — only a change in mathematical meaning is.

Mark a pair SAFE (NOT lossy) in these common cases:
- The English renders a Korean math-mode symbol as English prose, or omits a repeated variable that English grammar does not need (e.g. Korean "임의의 $$W$$에 대하여 $$W$$를 포함하는" → English "every $$W$$ lies in"). The meaning is unchanged.
- The English corrects an evident typo or error in the Korean source (a missing "=0", a duplicated/garbled symbol, a wrong index, a non-existent anchor). A more-correct English rendering is NOT a loss.
- The same equation appears with different surrounding text, or two adjacent blocks are merged or split.

Only mark a pair LOSSY when you are CONFIDENT that a mathematical statement, hypothesis, conclusion, or symbol is genuinely ABSENT from the English or is mathematically WRONG in the English. When uncertain, choose SAFE. First confirm the two passages describe the same spot — never judge a mismatched pair as lossy.

Set the overall VERDICT to lossy if ANY pair is LOSSY, otherwise safe.

Separately: whenever the English differs from the Korean BECAUSE THE KOREAN IS WRONG
— a wrong index or subscript, a swapped operator, a missing prime, a misspelling, a
garbled symbol, an equation that says something the surrounding prose contradicts —
report it under KO-TYPOS, quoting the Korean as written and the correct form. Do this
even though the pair is SAFE: the English needs no fix, but the Korean does. Report
ONLY things you are confident are errors in the Korean; omit the section if there are
none. Never invent one to fill the section.

Output (terse, no preamble, no closing remarks):

VERDICT: <safe | lossy>
FINDINGS:
- [pair N] <SAFE | LOSSY>: <one short sentence; for LOSSY, name exactly what meaning differs>
KO-TYPOS:
- <the Korean as written> -> <the correct form>: <a few words on why>
"""


def call_claude_verify(prompt: str) -> str:
    """Run one verify task via `claude -p --model haiku` and return the verdict.

    2026-07-20: `claude -p` 가 구독 과금으로 바뀌어 (사용자 확인) tmux 상주
    세션 우회가 불필요해졌다. 구 경로(verify_session.sh + .done 폴링)는
    파일로 보존 — 과금 정책이 되돌아오면 그대로 복원할 것.
    Raises RuntimeError on nonzero exit or empty verdict.
    """
    full = prompt + (
        "\n\n---\n"
        "Output ONLY the verdict block (the lines beginning `VERDICT:` and "
        "`FINDINGS:` — no preamble, no explanation, no code fence). "
        "Do not use any tools.\n"
    )
    claude_bin = shutil.which("claude") or str(Path.home() / ".local/bin/claude")
    # 2026-08-08: ~/.claude/settings.json 의 advisorModel(fable)이 전역 기본값이라,
    # 막지 않으면 haiku(advisor_rank 1) 세션인 이 verify 에도 Fable 상담이 붙는다
    # (부착 조건은 base_rank <= advisor_rank). 정해진 정책은 "cron 은 research
    # researcher 하나만 advisor 사용" 이므로 끈다. 이 env 가 유일하게 확실한 off:
    # advisor 게이트의 첫 검사라 settings 의 advisorModel 보다 먼저 short-circuit
    # 하고, `--advisor <더 약한 모델>` 방식은 rank 1 인 haiku 를 값으로 못 쓴다.
    env = {**os.environ, "CLAUDE_CODE_DISABLE_ADVISOR_TOOL": "1"}
    proc = subprocess.run(
        [claude_bin, "-p", "--model", "haiku", "--output-format", "text"],
        # 첫 user 메시지를 리터럴 `[cron]` 으로 시작시킨다 — 세션 트랜스크립트
        # 리퍼가 봇 턴을 식별하는 단일 규약 (프롬프트 문구 변경에 영향받지 않음).
        # verdict 블록만 출력하라는 지시와 섞이지 않도록 단독 줄로 둔다.
        input="[cron]\n\n" + full, capture_output=True, text=True,
        timeout=CLAUDE_VERIFY_DONE_TIMEOUT,
        cwd=str(BLOG_ROOT), env=env,
    )
    if proc.returncode != 0:
        raise RuntimeError(
            f"claude -p verify exited {proc.returncode}: "
            f"{proc.stderr.strip()[:300]!r}"
        )
    out = _FENCE_RE.sub("", proc.stdout).strip()
    if not out:
        raise RuntimeError("claude -p verify produced empty verdict")
    return out


_FIXUP_PROMPT = """You are fixing lint findings on one English post of a bilingual math blog.

File to edit:    @@PATH@@
Korean original: @@KO_PATH@@

Findings (from the repo's own linters — each is a real violation of the house
guidelines in GUIDELINE.md):

@@FINDINGS@@

Rules:
- Fix ONLY the findings listed above. Make the smallest edit that resolves each.
- Do NOT rewrite, restructure, retitle, or renumber anything else.
- Do NOT touch the References/참고문헌 section under any circumstance.
- Do NOT alter math spans (`$...$`, `$$...$$`), display blocks, or `\\tag{}`.
- A `§Section Name` citation must match the target post's `title:` exactly —
  read the target file to get it rather than guessing.
- Residual Korean: translate leftover Korean prose, and replace a Korean anchor
  on an `/en/` link with the target page's actual English heading slug (read the
  target file). But some Korean is intentional — a Korean bibliography entry, or
  a Korean term deliberately glossed. Leave those alone and count them as left.
- The Korean original is listed above for one purpose only: when a finding is
  about residual Korean, open it to see what that passage actually says, so your
  replacement matches the source rather than paraphrasing. Do not diff the two
  files, do not import anything else from it, and do not re-translate any passage
  that no finding names.
- Use the Edit tool on the file in place. Do not create files.

When done, output exactly one final line and nothing else:
FIXUP: <n> fixed / <m> left  — <short reason if any left>
"""


def call_claude_fixup(en_path: Path, ko_path: Path, findings: List[str]) -> str:
    """Run one lint-repair pass over `en_path` with `claude -p --model opus`.

    Returns the model's terse summary line. Raises RuntimeError on nonzero exit.
    Editing needs tools, so unlike call_claude_verify this session runs with
    bypassPermissions and a working directory — the title-mismatch class can
    only be fixed by reading the cited post's frontmatter.
    """
    # str.format 을 쓰지 않는다 — 프롬프트 본문에 리터럴 중괄호(`\\tag{}`, `$...$`)가
    # 있어 포맷 자리표시자로 해석된다 (2026-08-15 실측: "Replacement index 0 out of
    # range" 로 게이트가 통째로 죽었다).
    prompt = (_FIXUP_PROMPT
              .replace("@@PATH@@", str(en_path.relative_to(BLOG_ROOT)))
              .replace("@@KO_PATH@@", str(ko_path.relative_to(BLOG_ROOT)))
              .replace("@@FINDINGS@@",
                       "\n".join(f"- {f}" for f in findings)))
    claude_bin = shutil.which("claude") or str(Path.home() / ".local/bin/claude")
    # advisorModel(fable) 이 전역 기본값이라, 막지 않으면 opus 세션에도 상담이
    # 붙는다 (부착 조건 base_rank <= advisor_rank). cron 은 advisor 를 쓰지 않는다
    # — call_claude_verify 의 같은 주석 참고.
    env = {**os.environ, "CLAUDE_CODE_DISABLE_ADVISOR_TOOL": "1"}
    proc = subprocess.run(
        [claude_bin, "-p", "--model", FIXUP_MODEL,
         "--permission-mode", "bypassPermissions", "--output-format", "text"],
        # 첫 user 메시지의 리터럴 `[cron]` 은 세션 트랜스크립트 리퍼의 봇 턴
        # 식별 규약이다 (call_claude_verify 와 동일).
        input="[cron]\n\n" + prompt, capture_output=True, text=True,
        timeout=FIXUP_TIMEOUT_SEC, cwd=str(BLOG_ROOT), env=env,
    )
    if proc.returncode != 0:
        raise RuntimeError(
            f"claude -p fixup exited {proc.returncode}: "
            f"{proc.stderr.strip()[:200]!r}"
        )
    out = _FENCE_RE.sub("", proc.stdout).strip()
    tail = [l.strip() for l in out.splitlines() if l.strip()]
    return tail[-1][:200] if tail else "(no summary)"


def _flat(s) -> str:
    """로그 한 줄로 접는다 — 여러 줄 출력은 대시보드의 마지막-실행 오류 판정을
    통째로 오염시킨다 (blog-worker-log-timestamp 계약)."""
    return " ".join(str(s).split())


_KO_TYPO_REVIEW_PROMPT = """A weaker model compared a Korean math post with its English translation and
claimed the *Korean* source contains errors. Judge each claim against the Korean
text below. You are reviewing only — do not propose rewrites of anything else.

Korean source (@@KO_PATH@@):
--- BEGIN ---
@@KO_BODY@@
--- END ---

Claims:

@@CLAIMS@@

For each claim, decide:
  VALID  — the Korean really is wrong and the proposed correction is right.
  FALSE  — the Korean is correct as written, or the claim misreads it (a
           convention it dislikes, a deliberate notation, a hallucinated quote).
  UNSURE — you cannot locate the quoted Korean, or judging needs context outside
           this file.

Output exactly one line per claim, in order, and nothing else:
<n>. VALID|FALSE|UNSURE — <one clause of reasoning>
"""

_KO_TYPO_VERDICT_RE = re.compile(
    r"^\s*(?P<n>\d+)\s*[.)]\s*(?P<verdict>VALID|FALSE|UNSURE)\b[\s—:-]*(?P<why>.*)$",
    re.I)
KO_TYPO_BODY_MAX = 40_000        # 프롬프트에 싣는 KO 본문 상한
KO_TYPO_MAX_CLAIMS = 10


def call_claude_ko_typo_review(ko_path: Path, claims: List[str]) -> List[str]:
    """KO 오타 주장들을 opus 한 번에 넘겨 타당성만 판정받는다.

    **도구 없이** 돈다 — KO 본문을 프롬프트에 붙여 넣고 판정문만 받는다.
    사용자가 쓴 원문이라 봇이 고칠 대상이 아니고, 도구를 안 주면 고칠 수단
    자체가 없다. 반환값은 `<n>. VERDICT — 사유` 줄들.
    """
    body = _body_after_frontmatter(ko_path.read_text(encoding="utf-8")).strip()
    prompt = (_KO_TYPO_REVIEW_PROMPT
              .replace("@@KO_PATH@@", str(ko_path.relative_to(BLOG_ROOT)))
              .replace("@@KO_BODY@@", body[:KO_TYPO_BODY_MAX])
              .replace("@@CLAIMS@@",
                       "\n".join(f"{i}. {c}" for i, c in enumerate(claims, 1))))
    claude_bin = shutil.which("claude") or str(Path.home() / ".local/bin/claude")
    env = {**os.environ, "CLAUDE_CODE_DISABLE_ADVISOR_TOOL": "1"}
    proc = subprocess.run(
        [claude_bin, "-p", "--model", FIXUP_MODEL, "--output-format", "text"],
        input="[cron]\n\n" + prompt + "\n\nDo not use any tools.\n",
        capture_output=True, text=True, timeout=FIXUP_TIMEOUT_SEC,
        cwd=str(BLOG_ROOT), env=env,
    )
    if proc.returncode != 0:
        raise RuntimeError(f"claude -p ko-typo review exited {proc.returncode}: "
                           f"{proc.stderr.strip()[:200]!r}")
    return [l.strip() for l in _FENCE_RE.sub("", proc.stdout).splitlines() if l.strip()]


def review_ko_typos(ko_path: Path, key: str, claims: List[str]) -> List[dict]:
    """각 주장에 opus 판정을 붙여 돌려준다. 실패하면 판정 없이 원 주장만.

    KO 파일이 바뀌지 않았는지 해시로 확인한다 — 검토 전용 계약이 프롬프트로만
    걸려 있으면 지켜졌는지 알 수 없다. 사용자가 쓴 본문이므로 봇이 고치는 것은
    별도 절차(revising:true + drift_needed:true) 없이는 금지다.
    """
    out = [{"claim": c} for c in claims]
    if len(claims) > KO_TYPO_MAX_CLAIMS:
        log(f"GATE-KO-TYPO ({key}): 주장 {len(claims)}건 — 상한 "
            f"{KO_TYPO_MAX_CLAIMS} 초과라 검토 생략")
        return out
    before = hashlib.sha256(ko_path.read_bytes()).hexdigest()
    try:
        lines = call_claude_ko_typo_review(ko_path, claims)
    except Exception as e:
        log(f"GATE-KO-TYPO ({key}): 호출 실패 — {_flat(e)[:160]}")
        return out
    if hashlib.sha256(ko_path.read_bytes()).hexdigest() != before:
        log(f"GATE-KO-TYPO ({key}): KO 파일이 변경됨 — 검토 전용 계약 위반")
        _notify_telegram("[translate-worker] KO 검토가 원문을 수정함",
                         f"{key}\n검토 전용이어야 하는 단계가 KO 원문을 바꿨다. 확인 필요.")
    for ln in lines:
        m = _KO_TYPO_VERDICT_RE.match(ln)
        if not m:
            continue
        i = int(m.group("n")) - 1
        if 0 <= i < len(out):
            out[i]["verdict"] = m.group("verdict").upper()
            out[i]["why"] = m.group("why").strip()[:200]
    tally = collections.Counter(o.get("verdict", "?") for o in out)
    log(f"GATE-KO-TYPO ({key}): 주장 {len(claims)}건 판정 — "
        + " ".join(f"{k}={v}" for k, v in sorted(tally.items())))
    return out


def _hangul_findings(en_path: Path) -> List[str]:
    """EN 파일 하나에서 한글 잔존·한글 앵커 지적을 다시 뽑는다.

    번역 직후(out_body 기준) 계산한 것과 같은 규칙 — 수식·병기 <sub>·참고문헌
    블록은 제외한다. 게이트가 고친 뒤 **최종 파일 내용으로** 재판정하는 데 쓴다.
    """
    out = []
    try:
        body = _body_after_frontmatter(en_path.read_text(encoding="utf-8")).strip()
    except OSError:
        return out
    body_wo_refs, _ = extract_refs_block(body)
    hangul = re.findall(r"[가-힣]", _strip_math_and_glosses(body_wo_refs))
    if hangul:
        out.append(f"{len(hangul)} Hangul chars in body (≤{HANGUL_RESIDUE_MAX}, "
                   f"needs review) — e.g. {''.join(hangul[:20])!r}")
    anchors = re.findall(r"\]\(/en/[^)\s#]*#[^)\s]*[가-힣][^)\s]*\)", body)
    if anchors:
        out.append(f"{len(anchors)} Hangul anchor(s) on /en/ links, "
                   f"e.g. {anchors[0]!r}")
    return out


def _fixup_pass(en_path: Path, ko_path: Path, key: str,
                findings: List[str]) -> List[str]:
    """opus 한 패스로 지적을 고치고, **게이트를 다시 돌려** 남은 지적을 반환한다.

    판정은 모델의 자기 보고가 아니라 재검사 결과다. 호출 실패·타임아웃은 원래
    지적을 그대로 돌려주므로, 이 게이트가 죽어도 파이프라인은 게이트 도입 전과
    똑같이 동작한다 (커밋은 진행, 지적은 텔레그램).
    """
    if len(findings) > FIXUP_MAX_FINDINGS:
        log(f"GATE-OPUS ({key}): 지적 {len(findings)}건 — 상한 "
            f"{FIXUP_MAX_FINDINGS} 초과라 넘기지 않는다 (번역 자체 재검토 대상)")
        return findings
    try:
        summary = call_claude_fixup(en_path, ko_path, findings)
    except Exception as e:
        log(f"GATE-OPUS ({key}): 호출 실패 — {_flat(e)[:160]}")
        return findings
    log(f"GATE-OPUS ({key}): {_flat(summary)[:160]}")

    from section_anchor_gate import run_gate
    res = run_gate(en_path, ko_path, apply=True, mdlint=True)
    remain = res.fails + res.mdlint_lines + _hangul_findings(en_path)
    log(f"GATE-OPUS ({key}): 재검사 — 지적 {len(findings)}건 중 "
        f"{len(findings) - len(remain)}건 해소, 잔여 {len(remain)}건")
    return remain


def verify_math_mismatch(
    ko_content: str, en_new: str, ko_count: int, en_count: int,
    *, en_old: Optional[str] = None,   # unused; kept for call-site compatibility
) -> str:
    """Decide whether a KO/EN `$$`-count mismatch lost any mathematical meaning.

    Two stages:
      1. Mechanical — a KO block is benign iff its whitespace-normalized LaTeX
         appears anywhere in EN (display or inline), since math is identical
         across languages. Most mismatches are pure `$$display$$`→`$inline$`
         downgrades and resolve here with NO model call.
      2. Semantic — only the `:::` box regions holding a genuinely-absent KO
         block go to Kimi (no-tools agent), which judges meaning preservation
         WITHOUT being told anything about `$$`/counts. The `:::` box is the
         alignment unit because its derived id is identical across KO/EN and
         survives the downgrade 1:1 (matched `$$` blocks go sparse in
         downgrade-heavy posts and misalign). Returns a terse VERDICT string;
         'verify-failed: …' on error.
    """
    benign, suspect_ids = _locate_divergences(ko_content, en_new)
    if not suspect_ids:
        return (f"VERDICT: safe\nCOUNTS: ko={ko_count} en={en_count}\n"
                f"- mechanical: all {benign} differing block(s) survive in EN as "
                f"inline/text (`$$`→`$` downgrade or rephrase); no content missing.")

    omitted = max(0, len(suspect_ids) - _VERIFY_MAX_REGIONS)
    ko_reg, en_reg = _box_regions(ko_content), _box_regions(en_new)
    pairs = []
    for rid in suspect_ids[:_VERIFY_MAX_REGIONS]:
        kr, er = _cap_region(ko_reg.get(rid, "")), _cap_region(en_reg.get(rid, ""))
        if kr.strip() and er.strip():
            pairs.append((rid, kr, er))
    if not pairs:
        return (f"VERDICT: lossy\nCOUNTS: ko={ko_count} en={en_count}\n"
                f"- {len(suspect_ids)} KO block(s) absent from EN with no comparable "
                f"region found — needs manual check.")

    prompt = VERIFY_SEM_INSTRUCTIONS + "\n"
    for i, (rid, kr, er) in enumerate(pairs, 1):
        prompt += f"\n=== PAIR {i} [{rid}] ===\n[KOREAN]\n{kr}\n[ENGLISH]\n{er}\n"
    if omitted:
        prompt += f"\n(Note: {omitted} further suspect region(s) omitted for length.)\n"

    MAX_ATTEMPTS = 2
    for attempt in range(1, MAX_ATTEMPTS + 1):
        try:
            # Verdict comes back via a file the claude session writes (see
            # call_claude_verify). _finalize_verdict keeps only the LAST verdict
            # line, so any premature first-impression verdict is ignored.
            out = call_claude_verify(prompt)
            note = (f"\n(benign downgrades: {benign}; semantic-checked regions: "
                    f"{len(pairs)}" + (f"; {omitted} omitted" if omitted else "") + ")")
            return _finalize_verdict(out) + note
        except subprocess.TimeoutExpired:
            log(f"verify: claude session timeout {attempt}/{MAX_ATTEMPTS}"
                + (", retrying" if attempt < MAX_ATTEMPTS else ", giving up"))
            continue
        except Exception as e:
            return f"verify-failed: {e!r}"
    return f"verify-failed: claude session timeout after {MAX_ATTEMPTS} attempts"


# ---------------------------------------------------------------------------
# Region-incremental drift (re-translate only the changed <ins> regions)
# ---------------------------------------------------------------------------

def git_show_at(ko_path: Path, sha: str) -> Optional[str]:
    """`git show <sha>:<relpath>` content, or None if unavailable. Read-only."""
    try:
        rel = str(ko_path.relative_to(BLOG_ROOT))
        return subprocess.check_output(
            ["git", "show", f"{sha}:{rel}"],
            cwd=str(BLOG_ROOT), text=True, stderr=subprocess.DEVNULL,
        )
    except (subprocess.CalledProcessError, FileNotFoundError):
        return None


def git_commit_before(ko_path: Path, iso_ts: str) -> Optional[str]:
    """SHA of the last commit touching ko_path at or before iso_ts, or None."""
    try:
        rel = str(ko_path.relative_to(BLOG_ROOT))
        out = subprocess.check_output(
            ["git", "rev-list", "-1", f"--until={iso_ts}", "HEAD", "--", rel],
            cwd=str(BLOG_ROOT), text=True, stderr=subprocess.DEVNULL,
        ).strip()
        return out or None
    except (subprocess.CalledProcessError, FileNotFoundError):
        return None


def _split_regions(body: str):
    """Lossless split of a post body at theorem-box-anchor boundaries (`:::` box
    openers and residual raw `<ins id>` lines).

    Returns [(region_id, region_text), ...]; the first chunk is keyed _PREAMBLE
    (text before the first anchor). ''.join(text for _, text) == body exactly,
    so regions reassemble by concatenation. The box id (def1/prop2/conj4/…),
    identical across the KO and EN anchors, is the alignment key; proof openers
    carry no id and fold into the preceding box's region — the same behavior the
    old <ins>-based split had.
    """
    anchors = _box_anchors(body)
    if not anchors:
        return [(_PREAMBLE, body)]
    lines = body.split("\n")
    offsets = []
    off = 0
    for ln in lines:
        offsets.append(off)
        off += len(ln) + 1                       # +1 for the '\n' split removed
    starts = [offsets[idx] for _bid, idx in anchors]
    out = [(_PREAMBLE, body[:starts[0]])]
    for i, (bid, _idx) in enumerate(anchors):
        end = starts[i + 1] if i + 1 < len(anchors) else len(body)
        out.append((bid, body[starts[i]:end]))
    return out


def _region_norm(text: str) -> str:
    """Whitespace-collapsed key for change detection (ignores pure reflow)."""
    return re.sub(r"\s+", " ", text).strip()


def translate_drift_incremental(
    ko_path: Path, en_path: Path, translated_at_iso: str,
) -> Optional[Tuple[str, int, int, int, int]]:
    """Region-level incremental drift re-translation.

    Baseline = the KO as it was at the EN's `translated_at` commit (via git). Only
    the `:::`-box-keyed regions whose KO content changed since then are re-sent to
    Kimi; unchanged regions keep their existing EN text verbatim, so manual EN
    fixes survive and unchanged math is never re-translated.

    Returns (assembled_en, in_chars, out_chars, n_retranslated, n_total) on a
    provably-clean result, or None to tell the caller to fall back to a full
    re-translation (no git baseline / structure desync / validation not clean).
    """
    if not is_our_translation(en_path):
        return None
    en_text = en_path.read_text(encoding="utf-8")
    en_fm_text, en_body = _split_fm_block(en_text)

    ta = en_translation_meta(en_path).get("translated_at")
    if not ta:
        return None
    sha = git_commit_before(ko_path, ta)
    if not sha:
        return None
    old_ko = git_show_at(ko_path, sha)
    if old_ko is None:
        return None
    _, old_body = _split_fm_block(old_ko)

    ko_content = ko_path.read_text(encoding="utf-8")
    ko_fm_text, ko_body = _split_fm_block(ko_content)

    # Incremental drift asks "what changed in the KO since we translated it?" — it
    # never compares the KO against the EN. So an EN that was *born* damaged (the
    # model silently dropped a box at translation time, with the KO untouched
    # since) is invisible to it: every region matches its baseline, nothing is
    # re-sent, and the damage survives the drift run. Seen for real on 2026-07-12
    # (Divisors: "re-translated 0/17 region(s)" while the EN was missing an
    # Example the KO has). So: if the two sides are structurally out of step,
    # incremental cannot be the repair — fall back to a full re-translation.
    struct = lint_structure(ko_content, en_text)
    if struct:
        log(f"drift: EN structurally diverges from KO ({'; '.join(struct[:3])}"
            f"{' …' if len(struct) > 3 else ''}); full re-translation")
        return None

    old_regions = dict(_split_regions(old_body))
    en_regions  = dict(_split_regions(en_body))
    cur_regions = _split_regions(ko_body)

    out_chunks: list[str] = []
    in_chars = out_chars = n_retrans = 0
    for rid, ko_chunk in cur_regions:
        unchanged = (
            rid in old_regions and rid in en_regions
            and _region_norm(old_regions[rid]) == _region_norm(ko_chunk)
        )
        if unchanged:
            out_chunks.append(en_regions[rid].rstrip())
        else:
            prompt = build_prompt(ko_chunk)
            en_chunk = call_kimi(prompt)
            en_chunk, _ = label_fix(en_chunk)
            en_chunk = re.sub(r"<sub>[^<]*?</sub>", "", en_chunk)
            en_chunk = re.sub(r"<em[-_]ko>(.*?)</em[-_]ko>", r"*\1*",
                              en_chunk, flags=re.DOTALL)
            en_chunk = en_chunk.replace("/ko/", "/en/")
            out_chunks.append(en_chunk.rstrip())
            in_chars  += len(prompt)
            out_chars += len(en_chunk)
            n_retrans += 1

    if n_retrans == 0:
        new_body = en_body                       # only fm/whitespace changed
    else:
        new_body = "\n\n".join(c for c in out_chunks if c) + "\n"

    # Frontmatter: keep the existing EN translated fields (drift rarely edits
    # title/excerpt/description); only translate a field absent from EN.
    en_fields: dict = {}
    to_translate: dict = {}
    for fkey in _LLM_FRONTMATTER_FIELDS:
        ko_val = _extract_fm_scalar(ko_fm_text, fkey)
        if not ko_val:
            continue
        existing = _extract_fm_scalar(en_fm_text, fkey)
        if existing:
            en_fields[fkey] = existing
        else:
            to_translate[fkey] = ko_val
    if to_translate:
        en_fields.update(_translate_fm_fields_via_kimi(to_translate))

    en_fm = _compose_en_frontmatter(
        ko_fm_text, en_fields, translated_at_iso=translated_at_iso)
    assembled = f"---\n{en_fm}---\n{new_body.lstrip(chr(10))}"

    warns: list = []
    err = validate_translation(
        assembled, ko_content=ko_content, reason="drift",
        en_current=en_text, warnings=warns)
    if err or warns:
        log(f"incremental drift not clean (err={err}, warns={warns}); full fallback")
        return None
    return assembled, in_chars, out_chars, n_retrans, len(cur_regions)


# ---------------------------------------------------------------------------
# Commands
# ---------------------------------------------------------------------------

def log(msg: str) -> None:
    print(f"[{datetime.now().isoformat(timespec='seconds')}] {msg}", file=sys.stderr)


def cmd_status(state: dict) -> int:
    files = state.get("files", {})
    by_status: dict[str, int] = {}
    for entry in files.values():
        s = entry.get("status", "?")
        by_status[s] = by_status.get(s, 0) + 1
    stats = state.get("stats", {})
    print("Translation worker status")
    print(f"  total ko/ posts tracked: {len(files)}")
    for k, v in sorted(by_status.items()):
        print(f"    {k:>10}: {v}")
    print(f"  cumulative chars: input={stats.get('total_in_chars', 0):,}, "
          f"output={stats.get('total_out_chars', 0):,}")
    print(f"  total translated:  {stats.get('total_done', 0)}")
    review = sorted(k for k, e in files.items() if e.get("needs_review"))
    if review:
        print(f"  needs review (Hangul residue/anchor): {len(review)}")
        for k in review:
            print(f"    - {k}")
    return 0


def cmd_dry_run(state: dict) -> int:
    target = find_next_target(state)
    if target is None:
        print("No pending translation.")
        return 0
    ko_path, en_path, reason = target
    print(f"Would translate ({reason}):")
    print(f"  ko: {ko_path.relative_to(BLOG_ROOT)}")
    print(f"  en: {en_path.relative_to(BLOG_ROOT)}")
    print(f"  ko body length: {_ko_body_length(ko_path)} chars")
    print(f"  kimi binary: {KIMI_BIN}")
    return 0


_LINT_RULES = [
    (re.compile(r"\^\{\^"), "doubled superscript `^{^` (e.g. `^{^{-1}}`)"),
    (re.compile(
        r"(?<!\\)\\\\(?!\\)(math[a-z]*|frac|operatorname|begin|end|left|right|cdot|cdots|"
        r"ldots|circ|in|subseteq|subset|cap|cup|wedge|otimes|oplus|nabla|partial|"
        r"sum|prod|int|varphi|psi|phi|alpha|beta|gamma|lambda|sigma|tau|mu|nu|"
        r"rho|theta|Gamma|Delta|Omega|langle|rangle|lvert|rvert|mid)\b"),
     "double backslash before a macro (e.g. `\\\\mathfrak`) \u2014 LaTeX corruption"),
]


def lint_latex(text: str) -> list:
    """Cheap, high-precision regex lints for the LaTeX-corruption classes the
    old polish pass used to introduce. Read-only; returns human-readable findings
    with surrounding context for manual fixing."""
    out = []
    for rx, desc in _LINT_RULES:
        for m in rx.finditer(text):
            ctx = text[max(0, m.start() - 24): m.start() + 24].replace("\n", " ")
            out.append(f"{desc}: \u2026{ctx}\u2026")
    return out


# --- Structural KO/EN comparison (deterministic; no model in the loop) -------
# The semantic verifier hallucinates (see the telegram policy note in run_verify),
# so it cannot be trusted alone. But whole boxes going missing and proof bodies
# coming out empty are *countable*: parse both sides' `:::` fences and compare.
# This finds nothing that isn't there and costs no tokens. On 2026-07-12 it caught
# 21 posts whose EN had silently gone stale after the KO was edited (Compactness:
# KO 49 boxes vs EN 13; a 2669-char proof in Resolutions absent from EN).

# 단일 출처 _data/theorem_vocab.yml 파생 (감사 [4]). extra_canon 이 명시형
# 전용 어휘(주장→Conjecture 등)를 담는다 — 정준화가 빠지면 멀쩡한 번역의
# 박스 대조가 어긋난다.
_KIND_CANON = {k["ko"]: k["en"] for k in _VOCAB["kinds"]} | _VOCAB["extra_canon"]
_EXPLICIT_CLASSES = set(_VOCAB["explicit_classes"])


def _canon_kind(label: str) -> str:
    """Fence label -> a KO/EN-neutral kind name, so the two sides are comparable.
    `::: 정리 2 (Tychonoff)` and `::: Theorem 2 (Tychonoff)` both give "Theorem".

    For the explicit form (`::: misc 주장 4 {#conj4}`) the class word is skipped;
    the token after it carries the kind. Compound kinds (`명제--정의` /
    `Proposition--Definition`) canonicalize part by part. An unknown label is
    returned as-is, which is harmless while both sides spell it the same way
    (`Peano`, `The`, ...) and is a genuine finding when they do not."""
    toks = label.split()
    if not toks:
        return "?"
    head = toks[0]
    if head in _EXPLICIT_CLASSES and len(toks) > 1:
        head = toks[1]
    return "--".join(_KIND_CANON.get(p, p) for p in head.split("--"))


def _fence_blocks(text: str) -> list:
    """[(kind, body, line_no), ...] for every `:::` box, in document order.
    Code fences and {% raw %} blocks are skipped (_iter_source_lines)."""
    lines = text.split("\n")
    stack, out = [], []
    for idx, line in _iter_source_lines(text):
        s = line.strip()
        if not s.startswith(":::"):
            continue
        m = _FENCE_LABEL_RE.match(line)
        if m:
            stack.append((m.group(1).strip(), idx))
        elif s == ":::" and stack:
            label, start = stack.pop()
            body = "\n".join(lines[start + 1:idx]).strip()
            out.append((_canon_kind(label), body, start + 1))
    return out


def lint_structure(ko_text: str, en_text: str) -> list:
    """Deterministic KO/EN structural findings: boxes that vanished in EN, and
    EN blocks whose body is empty while the KO counterpart's is not."""
    ko_b, en_b = _fence_blocks(ko_text), _fence_blocks(en_text)
    out = []

    kc = collections.Counter(k for k, _, _ in ko_b)
    ec = collections.Counter(k for k, _, _ in en_b)
    for kind in sorted(set(kc) | set(ec)):
        a, b = kc.get(kind, 0), ec.get(kind, 0)
        if a != b:
            out.append(f"box count mismatch: {kind} ko={a} en={b}")

    # Positional pairing only means something while the two sides line up: once a
    # box is missing, everything after it shifts. The count mismatch above already
    # reports that case, so here we just pair up to the shorter side.
    for i, (kind, body, ln) in enumerate(en_b):
        if body or i >= len(ko_b):
            continue
        if ko_b[i][1]:
            out.append(f"empty EN block: #{i + 1} {kind} (en line {ln}) "
                       f"- KO has {len(ko_b[i][1])} chars")
    return out


# KO-TYPOS 파싱 규칙은 ko_typos 모듈이 단일 출처다 — 대시보드
# (server.py :: sec_translation)가 같은 모듈을 import 한다. 여기 복제하면
# 두 목록이 조용히 갈라진다.
from ko_typos import extract_ko_typos  # noqa: E402


def run_verify(state: dict, ko_path: Path, en_path: Path, key: str) -> int:
    """Read-only verification of an existing EN translation against KO.

    Deterministic LaTeX-corruption lints + the math-block semantic check (Kimi
    only when block counts genuinely diverge). Records the outcome in state and
    notifies on problems. NEVER modifies the EN file. Marks `verified_at` so the
    post is checked at most once.
    """
    ko_text = ko_path.read_text(encoding="utf-8")
    en_text = en_path.read_text(encoding="utf-8")
    # (디스플레이, 인라인) 프로필로 비교한다 — 총 개수만 보면 디스플레이가 인라인으로
    # 바뀐 것(합계 불변)을 놓친다. gap 계산·로그는 총합을 쓴다.
    ko_p = math_profile(_SUB_STRIP_RE.sub("", ko_text))
    en_p = math_profile(_SUB_STRIP_RE.sub("", en_text))
    ko_n, en_n = sum(ko_p), sum(en_p)
    lints = lint_latex(en_text)
    struct = lint_structure(ko_text, en_text)
    verdict_text = ""
    if ko_p != en_p:
        verdict_text = verify_math_mismatch(ko_text, en_text, ko_n, en_n)
    verdict_safe = bool(re.search(r"^VERDICT:\s*safe\b", verdict_text, re.M | re.I))
    ko_typos = extract_ko_typos(verdict_text)
    # `clean` is about the EN: a KO typo means the KO needs fixing, not the EN, so
    # it must not make the translation look defective. But it still has to be
    # surfaced, so it is checked separately at the early return below.
    clean = (not lints) and (not struct) and (ko_p == en_p or verdict_safe)

    entry = state["files"].get(key, {})
    entry["verified_at"] = datetime.now(timezone.utc).isoformat(timespec="seconds")
    entry["verify_math_counts"] = [list(ko_p), list(en_p)]
    entry["verify_lints"] = lints[:20] or None
    entry["verify_structure"] = struct[:20] or None
    entry["verify_ko_typos"] = ko_typos[:20] or None
    if verdict_text:
        entry["verify_verdict"] = verdict_text[:4000]
    state["files"][key] = entry
    save_state(state)

    if clean and not ko_typos:
        log(f"VERIFY ({key}): clean (math ko={ko_n} en={en_n})")
        return 0

    head = []
    if struct:
        head.append(f"{len(struct)} structure")
    if lints:
        head.append(f"{len(lints)} latex-lint")
    if ko_typos:
        head.append(f"{len(ko_typos)} ko-typo")
    if verdict_text and not verdict_safe:
        head.append(verdict_text.splitlines()[0])
    log(f"VERIFY ({key}): FLAGGED — {'; '.join(head)}")
    for ln in struct:
        log(f"  STRUCT ({key}): {ln}")
    for ln in lints:
        log(f"  LINT ({key}): {ln}")
    for ln in ko_typos:
        log(f"  KO-TYPO ({key}): {ln}")
    for ln in verdict_text.splitlines():
        log(f"  VERIFY ({key}): {ln}")

    # Telegram policy. Three of the four signals always alert.
    #
    # Deterministic and therefore trustworthy: the latex-lints, and the structural
    # KO/EN comparison (a box that exists in KO and not in EN is a fact, not an
    # opinion).
    #
    # KO-typos also always alert. They are model-reported, but they point at the
    # *Korean*, and they were being dropped precisely because they ride along with
    # a SAFE verdict. A 2026-07-13 sweep of stored verdicts found 19 posts with
    # such reports (16 never surfaced); source-checking them confirmed 13 real KO
    # errors. False positives here cost one grep; the misses cost a wrong theorem
    # standing on the site for a year.
    #
    # The semantic "lossy" verdict is the unreliable one — false-positive-prone
    # (2026-06-04 audit: 0 real losses across 30 manually source-checked flags;
    # the model hallucinates diffs, misaligns pairs, and mistakes typo-correction
    # or math-mode→prose rephrasing for loss). So it alerts ONLY when the
    # math-block gap is large; a small gap is virtually always benign rephrasing
    # and is logged + recorded (above) for optional review, not pushed.
    #
    # Note the division of labour: the real losses found on 2026-07-12 (EN gone
    # stale after a KO edit) were all caught by `struct`, which needs no model.
    gap = abs(ko_n - en_n)
    semantic_flag = bool(verdict_text) and not verdict_safe
    big_gap = ko_n > 0 and gap / ko_n >= 0.15
    if not (lints or struct or ko_typos or (semantic_flag and big_gap)):
        return 0

    body = ""
    if struct:
        body += "STRUCTURE (deterministic):\n" + "\n".join(struct) + "\n"
    if ko_typos:
        body += "KO-TYPOS (fix the Korean, not the English):\n" + "\n".join(ko_typos) + "\n"
    if semantic_flag:
        body += verdict_text + "\n"
    if lints:
        body += "LINTS:\n" + "\n".join(lints)
    _notify_telegram(f"translation verify flagged: {key}", body[:1500])
    return 0



# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------

def cmd_lint_structure() -> int:
    """Sweep every ko/en pair through the deterministic structural lint.

    Needs neither the model nor the state file, so it is safe to run any time —
    including before a translation, to see what the verify phase would flag."""
    n_bad = 0
    for ko in sorted(POSTS_ROOT.glob("*/ko/*.md")):
        en = find_en_counterpart(ko)
        if en is None or not en.exists():
            continue
        findings = lint_structure(ko.read_text(encoding="utf-8"),
                                  en.read_text(encoding="utf-8"))
        if not findings:
            continue
        n_bad += 1
        print(f"\n{ko.relative_to(BLOG_ROOT)}")
        for f in findings:
            print(f"   {f}")
    print(f"\n{n_bad} post(s) with structural KO/EN divergence")
    return 0


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__.split("\n\n")[0])
    ap.add_argument("--status",  action="store_true", help="print stats and exit")
    ap.add_argument("--dry-run", action="store_true", help="show next target without translating")
    ap.add_argument("--lint-structure", action="store_true",
                    help="compare ko/en theorem-box structure for every pair and exit "
                         "(deterministic, no model, no state)")
    args = ap.parse_args()

    if args.lint_structure:
        return cmd_lint_structure()

    if not Path(KIMI_BIN).exists():
        log(f"kimi CLI not found at {KIMI_BIN}")
        return 2

    state = load_state()

    if args.status:
        return cmd_status(state)
    if args.dry_run:
        return cmd_dry_run(state)

    if not acquire_lock():
        log("another instance running, exit")
        return 0

    # 키 이관은 락을 잡은 직후 바로 굳힌다 — 이후 단계가 실패해도 이관은 남는다.
    # (--status·--dry-run 은 여기까지 오지 않으므로 읽기 전용이 유지된다.)
    if _migrated_keys:
        save_state(state)

    try:
        target = find_next_target(state)
        if target is None:
            log("nothing pending")
            save_state(state)                # may have updated stub markers
            return 0
        ko_path, en_path, reason = target
        en_path.parent.mkdir(parents=True, exist_ok=True)
        key = str(ko_path.relative_to(BLOG_ROOT))

        if reason == "verify":
            return run_verify(state, ko_path, en_path, key)

        # Drift: try region-incremental re-translation first — only the <ins>
        # regions whose KO changed (vs the git baseline) go to Kimi; unchanged
        # EN is kept verbatim so manual fixes survive. Falls back to a full
        # re-translation when there is no baseline or the result is not clean.
        if reason == "drift":
            inc_at = datetime.now(timezone.utc).isoformat(timespec="seconds")
            try:
                inc = translate_drift_incremental(ko_path, en_path, inc_at)
            except subprocess.TimeoutExpired:
                inc = None
            except Exception as e:
                log(f"incremental drift error ({e!r}); full fallback")
                inc = None
            if inc is not None:
                assembled, in_chars, out_chars, n_re, n_tot = inc
                en_path.write_text(assembled, encoding="utf-8")
                clear_drift_flag(ko_path)
                state["files"][key] = {
                    "status": "done",
                    "last_attempt_ts": time.time(),
                    "en_path": str(en_path.relative_to(BLOG_ROOT)),
                    "ko_git_commit_ts": git_last_commit_ts(ko_path),
                    "translated_at": inc_at,
                    "in_chars": in_chars, "out_chars": out_chars,
                    "reason": "drift-incremental",
                    "regions_retranslated": n_re, "regions_total": n_tot,
                }
                state.pop("failure_notice", None)   # 엔진이 살아났다 — 다음 장애는 첫 통부터
                stats = state.setdefault("stats", {})
                stats["total_done"]      = stats.get("total_done", 0) + 1
                stats["total_in_chars"]  = stats.get("total_in_chars", 0) + in_chars
                stats["total_out_chars"] = stats.get("total_out_chars", 0) + out_chars
                save_state(state)
                log(f"DONE (incremental drift): {en_path.relative_to(BLOG_ROOT)} — "
                    f"re-translated {n_re}/{n_tot} region(s), kept {n_tot - n_re} "
                    f"(in={in_chars}c, out={out_chars}c)")
                return 0
            log(f"drift: incremental unavailable for {key}, full re-translation")

        log(f"translating ({reason}): {key} → {en_path.relative_to(BLOG_ROOT)} (ko {ko_path.stat().st_size}B)")

        # Snapshot pre-polish EN once — needed across retries (verify diff target,
        # and translate() reads en_path for the polish prompt on every attempt).
        en_old_snapshot: Optional[str] = None
        if reason == "polish" and en_path.exists():
            en_old_snapshot = en_path.read_text(encoding="utf-8")

        translated_at = datetime.now(timezone.utc).isoformat(timespec="seconds")
        translated = ""
        in_chars = out_chars = 0
        warnings: list = []
        verdict_text = ""
        lossy_history: list[tuple[int, str]] = []

        for attempt in range(1, MAX_TRANSLATE_ATTEMPTS + 1):
            warnings = []
            try:
                translated, in_chars, out_chars = translate(
                    ko_path, translated_at, reason=reason, en_path=en_path,
                    warnings=warnings,
                )
            except subprocess.TimeoutExpired:
                record_failure(state, key, f"timeout after {KIMI_TIMEOUT_SEC}s")
                save_state(state)
                log(f"FAILED: timeout (attempt {attempt})")
                return 1
            except Exception as e:
                record_failure(state, key, str(e))
                save_state(state)
                log(f"FAILED: {e!r} (attempt {attempt})")
                return 1

            for w in warnings:
                log(f"WARN ({key}) attempt {attempt}: {w}")

            math_warn = next(
                (w for w in warnings if w.startswith("math block count mismatch")),
                None,
            )
            if not math_warn:
                verdict_text = ""
                break

            ko_text = ko_path.read_text(encoding="utf-8")
            ko_n = sum(math_profile(_SUB_STRIP_RE.sub("", ko_text)))
            en_n = sum(math_profile(_SUB_STRIP_RE.sub("", translated)))
            log(f"VERIFY ({key}) attempt {attempt}/{MAX_TRANSLATE_ATTEMPTS}: "
                f"math mismatch ko={ko_n}/en={en_n}"
                + (" (with en_old)" if en_old_snapshot else ""))
            verdict_text = verify_math_mismatch(
                ko_text, translated, ko_n, en_n, en_old=en_old_snapshot,
            )
            for line in verdict_text.splitlines():
                log(f"VERIFY ({key}) attempt {attempt}: {line}")

            is_lossy = bool(re.search(
                r"^VERDICT:\s*lossy\b", verdict_text, re.MULTILINE | re.IGNORECASE
            ))
            if not is_lossy:
                break

            lossy_history.append((attempt, verdict_text))
            if attempt < MAX_TRANSLATE_ATTEMPTS:
                log(f"LOSSY verdict on attempt {attempt}, re-translating")
            else:
                log(f"LOSSY verdict persisted after {MAX_TRANSLATE_ATTEMPTS} attempts — accepting last")

        en_path.write_text(translated, encoding="utf-8")
        if reason in ("pending", "drift"):
            # consume the opt-in flag; don't re-drift. pending 도 지운다 — 방금
            # 현재 KO 로부터 EN 을 만들었으므로 drift 는 이미 해소된 상태이고,
            # 남겨 두면 다음 tick 이 같은 글을 통째로 재번역한다.
            clear_drift_flag(ko_path)
        # ── 게이트: 결정론 수리 → opus 잔여 수리 → 재검사 ─────────────────
        # 상태 기록·알림보다 **먼저** 돈다. 게이트가 고칠 수 있는 것까지 경고로
        # 올리면 이미 해소된 일로 알림이 나가고 needs_review 마커가 남는다.
        # 게이트 실패는 번역을 죽이지 않는다 — 커밋은 진행하고 잔여만 넘긴다.
        hangul_warns = [w for w in warnings if "Hangul" in w]
        gate_residual: List[str] = list(hangul_warns)
        try:
            from section_anchor_gate import run_gate
            gres = run_gate(en_path, ko_path, apply=True, mdlint=True)
            for ln in gres.log_lines:
                log(f"GATE ({key}): {ln}")
            # opus 로 넘기는 입력은 결정론 게이트의 잔여 + 한글 경고다. 한글
            # 경고는 **게이트가 돈 뒤 파일로 다시 뽑는다** — 한글 앵커는 게이트가
            # 결정론으로 고치는 부류라, 번역 단계의 낡은 경고를 그대로 넘기면
            # 이미 고쳐진 것을 고치라고 부르는 헛돈이 된다. 수식 개수 불일치는
            # 넣지 않는다 — 프롬프트가 수식을 못 만지게 돼 있고, 그쪽은
            # verify_math_mismatch 라는 자기 검증 경로가 따로 있다.
            residual = gres.fails + gres.mdlint_lines + _hangul_findings(en_path)
            gate_residual = _fixup_pass(en_path, ko_path, key, residual) \
                if residual else []
        except Exception as e:
            log(f"GATE exception (non-fatal): {_flat(e)[:160]}")

        # 한글 경고는 최종 파일로 재판정한다. 게이트가 고쳤으면 알림에서도
        # needs_review 에서도 빠져야 한다 (마커만 남아 --status 를 오염시킨 사례 있음).
        warnings = [w for w in warnings if "Hangul" not in w] \
            + _hangul_findings(en_path)
        hangul_warns = [w for w in warnings if "Hangul" in w]

        # 검증기가 KO 원문의 오류를 지적했으면 opus 에게 타당성만 판정받는다.
        # 검증기는 약한 모델이라 오탐이 섞이고, 이 지적은 SAFE verdict 에 붙어
        # 오므로 사람이 걸러 줄 다른 관문이 없다. 판정만 하고 원문은 고치지
        # 않는다 — 사용자가 쓴 본문이다.
        ko_typo_review: List[dict] = []
        ko_typo_claims = extract_ko_typos(verdict_text)
        if ko_typo_claims:
            ko_typo_review = review_ko_typos(ko_path, key, ko_typo_claims)

        state["files"][key] = {
            "status": "done",
            "last_attempt_ts": time.time(),
            "en_path": str(en_path.relative_to(BLOG_ROOT)),
            "ko_git_commit_ts": git_last_commit_ts(ko_path),
            "translated_at": translated_at,
            "in_chars": in_chars,
            "out_chars": out_chars,
            "reason": reason,
            "warnings": warnings or None,
        }
        state.pop("failure_notice", None)   # 엔진이 살아났다 — 다음 장애는 첫 통부터
        if lossy_history:
            state["files"][key]["lossy_retry_count"] = len(lossy_history)
        if verdict_text:
            state["files"][key]["verify_verdict"] = verdict_text[:4000]
        if hangul_warns:
            # 게이트를 거치고도 남은 한글만 여기 온다 — 임계 미만 한글 잔존·한글
            # 앵커는 정오 판단에 사람이 필요하다. 확인 후 손으로 지운다.
            state["files"][key]["needs_review"] = hangul_warns
        if ko_typo_review:
            # FALSE 판정도 지운 채로 저장하지 않는다 — 대시보드의 '수정' 체크
            # 흐름과 사용자의 최종 판단이 전체 목록을 본다. 주석을 다는 것이지
            # 거르는 것이 아니다.
            state["files"][key]["verify_ko_typos"] = ko_typo_claims[:20]
            state["files"][key]["verify_ko_typos_review"] = ko_typo_review[:20]

        # 게이트가 못 고치고 남긴 것도 같은 알림에 싣는다 (한글 경고와 중복되지
        # 않게 warnings 에 없는 것만).
        gate_only = [x for x in gate_residual if x not in warnings]
        # 판정이 붙은 KO 오타 지적. FALSE 만 남으면 알릴 것이 없다.
        ko_actionable = [o for o in ko_typo_review
                         if o.get("verdict", "UNSURE") != "FALSE"]

        if warnings or gate_only or ko_actionable:
            # Suppress telegram only when the verdict is safe AND every warning
            # is a math-count mismatch ("safe" means the divergence is
            # rephrasing). Hangul warnings (residual prose, Korean anchors)
            # always notify — they need human review regardless of the math
            # verdict. minor / lossy / verify-failed still notify.
            verdict_safe = bool(
                verdict_text
                and re.search(r"^VERDICT:\s*safe\b",
                              verdict_text, re.MULTILINE | re.IGNORECASE)
            )
            only_math = not gate_only and not ko_actionable and all(
                w.startswith("math block count mismatch") for w in warnings
            )
            if verdict_safe and only_math:
                log(f"VERIFY ({key}): safe verdict — telegram suppressed")
            else:
                body_lines = [key, f"→ {en_path.relative_to(BLOG_ROOT)}", ""]
                body_lines += [f"• {w}" for w in warnings]
                body_lines += [f"• (게이트 잔여) {x}" for x in gate_only]
                if ko_typo_review:
                    n_false = len(ko_typo_review) - len(ko_actionable)
                    body_lines += ["", f"KO 오타 지적 {len(ko_typo_review)}건 "
                                       f"(opus 오탐 판정 {n_false}건 제외):"]
                    for o in ko_actionable:
                        body_lines.append(
                            f"• [{o.get('verdict', 'UNSURE')}] {o['claim']}"
                            + (f"\n    → {o['why']}" if o.get("why") else ""))
                if lossy_history:
                    final_lossy = bool(re.search(
                        r"^VERDICT:\s*lossy\b", verdict_text,
                        re.MULTILINE | re.IGNORECASE,
                    ))
                    body_lines += ["", (
                        f"LOSSY persisted on all {len(lossy_history)}/{MAX_TRANSLATE_ATTEMPTS} attempts"
                        if final_lossy else
                        f"recovered after {len(lossy_history)} lossy attempt(s)"
                    )]
                if verdict_text:
                    body_lines += ["", "--- kimi verify (final) ---", verdict_text]
                _notify_telegram(
                    f"[translate-worker] {reason} warnings",
                    "\n".join(body_lines),
                )
        stats = state.setdefault("stats", {})
        stats["total_done"]      = stats.get("total_done", 0) + 1
        stats["total_in_chars"]  = stats.get("total_in_chars",  0) + in_chars
        stats["total_out_chars"] = stats.get("total_out_chars", 0) + out_chars
        save_state(state)

        log(f"DONE: {en_path.relative_to(BLOG_ROOT)} (in={in_chars}c, out={out_chars}c)")
        commit_translation(ko_path, en_path, reason)

        # 이 글을 가리키던 유보(EN 미번역 대상) 섹션 앵커의 자가 치유. 수리된
        # 형제 파일은 커밋하지 않는다 — 워킹트리에 남아 다음 autopush 가 가져간다.
        try:
            from section_anchor_gate import sweep_target
            sres = sweep_target(en_path, apply=True)
            for ln in sres.log_lines:
                log(f"SWEEP ({key}): {ln}")
        except Exception as e:
            log(f"SWEEP exception (non-fatal): {_flat(e)[:160]}")
        return 0
    finally:
        release_lock()
        if _verify_session_used:
            kill_verify_session()


if __name__ == "__main__":
    sys.exit(main())
