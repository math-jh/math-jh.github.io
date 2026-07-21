#!/usr/bin/env python3
"""gloss_backfill.py — 정의 박스 내 무병기(<sub> 없는) 영어 이탤릭 용어에
한국어 병기를 일회성으로 소급 추가하는 파이프라인 (2026-07-21).

배경: `::: 정의 N` / `::: Definition N` fenced-div 안에서 이탤릭(`*term*`)으로
정의되는 용어는 규칙상 `*english<sub>한국어</sub>*` 한영 병기가 필수다. 옛 글
다수가 이 규칙 이전에 쓰여 병기가 빠져 있다. term_extract_worker.py 의
stage-1(classify_definitions)은 `<sub>` 쌍 마커만 인식하므로 이 용어들은
terms.yml 색인에서 통째로 누락된다. 이 스크립트가 그 격차를 메운다.

## 판정 정책 (2026-07-21 사용자 룰링 확정본)

1. **REUSE (조치 없음)**: 용어가 이미 코퍼스 다른 글에 `*en<sub>ko</sub>*`
   전례가 있거나(S0) terms.yml 에 이미 등록돼(S0b) 있으면, 이 글의 무병기
   이탤릭은 "재사용"(이미 아는 용어를 병기 없이 다시 언급)일 수 있다 —
   **절대 병기하지 않는다.** 글도 terms.yml 도 무수정. 정의 서술 패턴이
   감지된 경우만 리뷰 파일 부록에 FYI 로 기록한다(사용자가 나중에 진짜
   재정의였는지 훑어보게).
2. **신규 용어만 병기 대상.** 같은 신규 용어가 여러 글의 정의 박스에
   등장하면 **논리적으로 가장 앞선 글 하나에만** 병기한다: 같은 카테고리면
   weight 최소인 글, 카테고리가 다르면 판단 불가 → REVIEW(무적용). 나머지
   글의 등장은 재사용으로 간주해 무병기 유지.
3. **AUTO 소스 계층 (신규 용어 한정)**: KMS exact 단일 → 자동 적용. KMS exact
   복수 후보 → 문맥을 읽어 후보 **안에서만** 선택(코드가 membership 검증).
   위키만 있음 / 소스 없음 / 다중 정의처 판단 불가 → REVIEW(무적용). 후보
   밖 임의 번역은 어떤 경우에도 금지.
4. **적용**: dry-run 통계 확인 → 실제 적용(파일별 트랜잭션 — 검증 실패 시 그
   파일만 원복) → terms.yml 신규 entry 등록(이미 있는 항목은 절대 건드리지
   않음 — defs/url 갱신은 term_extract_worker 의 정기 스캔 몫).

## 소스 (전부 캐시 — 이후 상시 배선 재사용)

- S0  : 코퍼스 전례. `_posts/Math/*/ko/*.md` 전체에서
        `\\*(en)<sub>(ko)</sub>\\*` 스캔 (라틴 쪽이 en). dedup_key(en) → ko.
- S0b : terms.yml 기존 en → ko (terms_common.split_file/chunk_field/dedup_key).
- S1  : KMS 대한수학회 수학용어집(kms.or.kr) — exact ename 일치 행만, ko 는
        콤마 분리 복수 후보 가능. 캐시: kms_cache.json.
- S2  : 위키백과 langlink(en→ko) — REVIEW 전용(형태 도출 필요), 캐시:
        wiki_cache.json.

## 사용

    python3 gloss_backfill.py detect              # stage 1 만, 통계 출력
    python3 gloss_backfill.py research             # stage 2, 캐시 채움
    python3 gloss_backfill.py classify             # stage 3, review.md 작성
    python3 gloss_backfill.py apply --dry-run       # stage 4, 통계만(무수정)
    python3 gloss_backfill.py apply                 # stage 4, 실제 적용
    python3 gloss_backfill.py all [--dry-run]       # 1→2→3→4 순서로

각 stage 는 이전 stage 산출물(캐시 파일)을 재사용하므로 재실행이 저렴하다.
"""
from __future__ import annotations

import argparse
import glob
import json
import re
import sys
import time
import urllib.error
import urllib.parse
import urllib.request
from collections import Counter, defaultdict
from dataclasses import dataclass, field
from datetime import datetime, timezone
from pathlib import Path

import yaml

SCRIPT_DIR = Path(__file__).resolve().parent
BLOG_ROOT = SCRIPT_DIR.parents[1]
sys.path.insert(0, str(SCRIPT_DIR))

from terms_common import (  # noqa: E402
    GEN_ED_DIRS, TERMS_PATH, category_ko_maps, chunk_field, chunk_id, dedup_key,
    insert_sorted, join_file, letter_of, permalink_map, semantic_checks,
    slugify_id, split_file, url_slug, yaml_quote,
)
from term_extract_worker import (  # noqa: E402
    build_entry, decide_primary, entry_index, post_meta, write_gate,
)
from extract_terms import (  # noqa: E402
    add_def_to_chunk, parse_frontmatter, strip_frontmatter,
)

try:
    from bs4 import BeautifulSoup
except ImportError:  # pragma: no cover
    BeautifulSoup = None

KMS_CACHE_PATH = SCRIPT_DIR / "kms_cache.json"
WIKI_CACHE_PATH = SCRIPT_DIR / "wiki_cache.json"
SKIP_PATH = SCRIPT_DIR / "gloss_skip.yml"  # gloss_stage.py 와 공유하는 영구
                                            # 생략 확정 목록(사용자 편집)
REVIEW_PATH = SCRIPT_DIR / "gloss_backfill_review.md"
TERMS_BACKUP_PATH = SCRIPT_DIR / "terms.yml.bak-gloss-backfill"
DECISIONS_PATH = SCRIPT_DIR / "gloss_backfill_decisions.json"  # 사람이 단 KMS
                                                                # 복수후보 선택 근거

POSTS_GLOB = str(BLOG_ROOT / "_posts" / "Math" / "*" / "ko" / "*.md")

UA = "math-jh.github.io gloss-backfill/1.0 (contact: kimjunhyeok96@gmail.com)"

# ---------------------------------------------------------------------------
# Stage 1: 탐지
# ---------------------------------------------------------------------------

BOX_RE = re.compile(r"^::: (?:정의|[Dd]efinition)\b[^\n]*\n(.*?)^:::[ \t]*$",
                    re.M | re.S)
ITALIC_RE = re.compile(r"(?<!\*)\*([A-Za-z][^*<\n]{1,60}?)\*(?!\*)")
_DOLLAR_BLOCK_RE = re.compile(r"\$\$.*?\$\$", re.S)
_DOLLAR_INLINE_RE = re.compile(r"\$[^$\n]+?\$")
_CODE_RE = re.compile(r"`[^`\n]+?`")

CORPUS_GLOSS_RE = re.compile(r"\*([^*<]+)<sub>([^<]+)</sub>\*")
_HANGUL_RE = re.compile(r"[가-힣]")
_LATIN_RE = re.compile(r"[A-Za-z]")
_WEIGHT_RE = re.compile(r"^weight:\s*(\d+)", re.M)

_DEFN_TAIL_PATTERNS = (
    "라는 것은", "라고 하는 것은", "라 한다", "라고 한다", "라 부른다",
    "라고 부른다", "라 불린다", "라고 불린다", "이라 하자", "라 하자",
    "라 정의한다", "라고 정의한다", "라 칭한다",
)


def _mask_same_len(text: str, pattern: re.Pattern) -> str:
    def repl(m: re.Match) -> str:
        s = m.group(0)
        return "".join("\n" if c == "\n" else "\x00" for c in s)
    return pattern.sub(repl, text)


def mask_box_content(content: str) -> str:
    content = _mask_same_len(content, _DOLLAR_BLOCK_RE)
    content = _mask_same_len(content, _DOLLAR_INLINE_RE)
    content = _mask_same_len(content, _CODE_RE)
    return content


@dataclass
class Occurrence:
    file: str
    box_start: int
    box_end: int
    match_start: int
    insert_at: int          # 이 오프셋 바로 앞에 <sub>gloss</sub> 를 끼워 넣는다
    raw: str                # 원문 표기 (whitespace-trimmed)
    context: str
    box_label: str
    category: str            # _posts/Math/<Category>/ko/... 의 <Category>
    weight: int | None
    has_defn_phrasing: bool


def all_ko_posts() -> list[str]:
    return sorted(str(Path(p).relative_to(BLOG_ROOT))
                  for p in glob.glob(POSTS_GLOB))


def category_of(rel: str) -> str:
    parts = Path(rel).parts
    # _posts / Math / <Category> / ko / file.md
    return parts[2] if len(parts) >= 3 else ""


def weight_of(text: str) -> int | None:
    m = _WEIGHT_RE.search(text)
    return int(m.group(1)) if m else None


def has_definitional_phrasing(text: str, insert_at: int, window: int = 60) -> bool:
    tail = text[insert_at:insert_at + window]
    tail = re.sub(r"^\*", "", tail)  # 닫는 * 건너뛰기
    return any(p in tail[:40] for p in _DEFN_TAIL_PATTERNS)


def detect_file(rel: str, text: str) -> list[Occurrence]:
    occs: list[Occurrence] = []
    cat = category_of(rel)
    w = weight_of(text)
    for bm in BOX_RE.finditer(text):
        box_start, box_end = bm.start(1), bm.end(1)
        content = text[box_start:box_end]
        masked = mask_box_content(content)
        box_label = bm.group(0).split("\n", 1)[0][len("::: "):].strip()
        for im in ITALIC_RE.finditer(masked):
            # 매치 위치는 masked 문자열 기준(길이 보존)이지만, 실제 표기(raw)는
            # 원문 content 에서 같은 span 을 잘라야 한다 — masked 에서 그대로
            # 잘라내면 수식·코드가 있던 자리가 \x00 널바이트로 남는다.
            raw = content[im.start(1):im.end(1)]
            if "<sub>" in raw:
                continue  # 구조적으로 도달 불가(문자 클래스가 '<' 배제) — 방어적
            raw_s = raw.strip()
            if not raw_s or not re.search(r"[A-Za-z]", raw_s):
                continue
            trail_ws = len(raw) - len(raw.rstrip())
            insert_at = box_start + im.end(1) - trail_ws
            match_start = box_start + im.start(1)
            ctx_s = max(0, match_start - 80)
            ctx_e = min(len(text), insert_at + 80)
            context = text[ctx_s:ctx_e].replace("\n", " ")
            occs.append(Occurrence(
                file=rel, box_start=box_start, box_end=box_end,
                match_start=match_start, insert_at=insert_at, raw=raw_s,
                context=context, box_label=box_label, category=cat, weight=w,
                has_defn_phrasing=has_definitional_phrasing(text, insert_at),
            ))
    return occs


def detect_all() -> dict[str, list[Occurrence]]:
    """dedup_key(raw) → occurrences (여러 파일에 걸칠 수 있음)."""
    groups: dict[str, list[Occurrence]] = defaultdict(list)
    for rel in all_ko_posts():
        text = (BLOG_ROOT / rel).read_text(encoding="utf-8")
        for occ in detect_file(rel, text):
            k = dedup_key(occ.raw)
            if k:
                groups[k].append(occ)
    return groups


def display_term(occs: list[Occurrence]) -> str:
    """대표 원문 표기 — 최빈, 동률이면 최초 등장."""
    counts: dict[str, int] = defaultdict(int)
    order: dict[str, int] = {}
    for i, o in enumerate(occs):
        counts[o.raw] += 1
        order.setdefault(o.raw, i)
    return max(counts, key=lambda r: (counts[r], -order[r]))


# ---------------------------------------------------------------------------
# S0 / S0b — 전례 소스 (사람이 만든 코퍼스 자체가 근거이므로 리서치 아님)
# ---------------------------------------------------------------------------

def build_s0_map() -> dict[str, dict[str, set[str]]]:
    """dedup_key(en) → {ko gloss: {rel 파일...}}."""
    s0: dict[str, dict[str, set[str]]] = defaultdict(lambda: defaultdict(set))
    for rel in all_ko_posts():
        text = (BLOG_ROOT / rel).read_text(encoding="utf-8")
        for m in CORPUS_GLOSS_RE.finditer(text):
            a, b = m.group(1).strip(), m.group(2).strip()
            a_l, a_h = bool(_LATIN_RE.search(a)), bool(_HANGUL_RE.search(a))
            b_l, b_h = bool(_LATIN_RE.search(b)), bool(_HANGUL_RE.search(b))
            if a_l and not a_h and b_h:
                en, ko = a, b
            elif b_l and not b_h and a_h:
                en, ko = b, a
            else:
                continue
            k = dedup_key(en)
            if k:
                s0[k][ko].add(rel)
    return s0


def build_yml_map() -> tuple[dict[str, str], list[str], dict[str, list[str]]]:
    """(dedup_key(en) → ko, header, groups) — terms.yml 현재 상태."""
    text = TERMS_PATH.read_text(encoding="utf-8")
    header, groups = split_file(text)
    out: dict[str, str] = {}
    for letter, chunks in groups.items():
        for c in chunks:
            en = chunk_field(c, "en") or ""
            ko = chunk_field(c, "ko") or ""
            k = dedup_key(en)
            if k and ko:
                out[k] = ko
    return out, header, groups


# ---------------------------------------------------------------------------
# Stage 2: KMS / Wikipedia 조회 (캐시)
# ---------------------------------------------------------------------------

def load_cache(path: Path) -> dict:
    if path.exists():
        try:
            return json.loads(path.read_text(encoding="utf-8"))
        except (OSError, json.JSONDecodeError):
            pass
    return {}


def save_cache(path: Path, cache: dict) -> None:
    tmp = path.with_suffix(".tmp")
    tmp.write_text(json.dumps(cache, ensure_ascii=False, indent=1, sort_keys=True),
                   encoding="utf-8")
    tmp.replace(path)


def _kms_fetch_page(term: str, start: int) -> tuple[list[tuple[str, str]], bool]:
    url = ("https://www.kms.or.kr/mathdict/list.html?start=%d&sort=ename"
           "&key=ename&keyword=%s" % (start, urllib.parse.quote(term)))
    req = urllib.request.Request(url, headers={"User-Agent": UA})
    try:
        with urllib.request.urlopen(req, timeout=15) as resp:
            raw = resp.read().decode("utf-8", "replace")
    except (urllib.error.URLError, TimeoutError, OSError):
        return [], False
    if BeautifulSoup is None:
        rows = re.findall(r"<tr class='list'>\s*<td>([^<]*)</td>\s*"
                          r"<td>([^<]*)</td>", raw)
        return rows, True
    soup = BeautifulSoup(raw, "lxml")
    rows = []
    for tr in soup.select("tr.list"):
        tds = tr.find_all("td")
        if len(tds) == 2:
            rows.append((tds[0].get_text(strip=True), tds[1].get_text(strip=True)))
    return rows, True


def kms_query(term: str, cache: dict) -> dict:
    """캐시 포맷 계약: {"<용어 소문자>": {"ts": ISO8601, "candidates": [...]}}
    (exact 없어도 candidates: [] 로 부정 캐시 저장 — 상시 배선 공유 계약)."""
    key = term.strip().lower()
    if key in cache:
        return cache[key]
    exact: list[tuple[str, str]] = []
    for start in (0, 30, 60):
        rows, ok = _kms_fetch_page(term, start)
        time.sleep(0.5)
        if not ok or not rows:
            break
        for ename, ko in rows:
            if ename.strip().lower() == key:
                exact.append((ename.strip(), ko.strip()))
        if exact:
            break
    candidates: list[str] = []
    for _, ko in exact:
        for c in (x.strip() for x in ko.split(",")):
            if c and c not in candidates:
                candidates.append(c)
    result = {"ts": datetime.now(timezone.utc).isoformat(timespec="seconds"),
              "candidates": candidates}
    cache[key] = result
    return result


def _wiki_api(params: dict) -> dict:
    url = "https://en.wikipedia.org/w/api.php?" + urllib.parse.urlencode(params)
    req = urllib.request.Request(url, headers={"User-Agent": UA})
    with urllib.request.urlopen(req, timeout=15) as resp:
        return json.loads(resp.read().decode("utf-8"))


def wiki_query(term: str, cache: dict) -> dict:
    """캐시 포맷 계약: {"<용어 소문자>": {"ts": ISO8601, "title_en": str|null,
    "ko_title": str|null}} (문서 없음/ko 링크 없음도 null 로 부정 캐시 저장)."""
    key = term.strip().lower()
    if key in cache:
        return cache[key]
    title_en: str | None = None
    ko_title: str | None = None
    try:
        data = _wiki_api({"action": "query", "titles": term, "prop": "langlinks",
                          "lllang": "ko", "format": "json", "redirects": 1})
        time.sleep(0.3)
        pages = data.get("query", {}).get("pages", {})
        page = next(iter(pages.values()), {})
        if "missing" not in page:
            title_en = page.get("title")
            if page.get("langlinks"):
                ko_title = page["langlinks"][0]["*"]
        if ko_title is None:
            data2 = _wiki_api({"action": "query", "list": "search",
                              "srsearch": term, "srlimit": 1, "format": "json"})
            time.sleep(0.3)
            hits = data2.get("query", {}).get("search", [])
            if hits:
                title2 = hits[0]["title"]
                data3 = _wiki_api({"action": "query", "titles": title2,
                                  "prop": "langlinks", "lllang": "ko",
                                  "format": "json", "redirects": 1})
                time.sleep(0.3)
                pages3 = data3.get("query", {}).get("pages", {})
                page3 = next(iter(pages3.values()), {})
                if "missing" not in page3:
                    title_en = title2
                    if page3.get("langlinks"):
                        ko_title = page3["langlinks"][0]["*"]
    except Exception:  # noqa: BLE001
        pass
    result = {"ts": datetime.now(timezone.utc).isoformat(timespec="seconds"),
              "title_en": title_en, "ko_title": ko_title}
    cache[key] = result
    return result


# ---------------------------------------------------------------------------
# Stage 3: 계층 판정
# ---------------------------------------------------------------------------

# 교양수학 예외(2026-07-21 룰링): 신규 용어가 여러 글에 등장하고 논리적으로
# 가장 앞선 정의처가 교양수학이면, 교양 정의처 + 그 다음 순위의 비교양
# 정의처 **둘 다**에 병기해 비교양 쪽에 "정식 거처"를 보장한다. 앞선
# 정의처가 비교양이면 기존 규칙(단일 선택) 그대로.
# 교양수학 집합은 terms_common.GEN_ED_DIRS (단일 출처: _data/categories.yml
# 의 section: liberal_arts — 이중 SoT 감사 [U2], 2026-07-22).


@dataclass
class Decision:
    key: str
    display: str
    occs: list[Occurrence]
    bucket: str              # "AUTO" | "REUSE" | "REVIEW"
    reason: str = ""
    gloss: str | None = None
    source: str = ""
    chosen_files: list[str] = field(default_factory=list)  # 순서 중요(defs 순서)
    candidates: list[str] = field(default_factory=list)
    note: str = ""


def load_decisions_overrides() -> dict[str, str]:
    """사람이 KMS 복수후보에 대해 미리 단 선택(term_key → 선택 gloss)."""
    if DECISIONS_PATH.exists():
        try:
            return json.loads(DECISIONS_PATH.read_text(encoding="utf-8"))
        except (OSError, json.JSONDecodeError):
            pass
    return {}


def load_skip_set() -> set[str]:
    """gloss_skip.yml — gloss_stage.py(상시 배선)와 공유하는 영구 생략 목록.
    여기 있는 용어(소문자 비교)는 KMS/Wiki 조회 없이 곧장 REVIEW 로 보낸다."""
    if not SKIP_PATH.exists():
        return set()
    try:
        data = yaml.safe_load(SKIP_PATH.read_text(encoding="utf-8")) or {}
    except yaml.YAMLError:
        return set()
    return {str(s).strip().lower() for s in (data.get("skip") or [])}


def classify_all(groups: dict[str, list[Occurrence]],
                 s0: dict[str, dict[str, set[str]]],
                 yml_map: dict[str, str],
                 kms_cache: dict, wiki_cache: dict,
                 overrides: dict[str, str],
                 skip_set: set[str],
                 do_network: bool) -> list[Decision]:
    decisions: list[Decision] = []
    for i, (key, occs) in enumerate(sorted(groups.items(), key=lambda kv: kv[0])):
        if do_network and i and i % 15 == 0:
            # 네트워크 조회는 몇 분씩 걸릴 수 있다 — 중간에 죽어도 그동안의
            # 조회 결과(부정 캐시 포함)를 잃지 않도록 주기적으로 flush.
            save_cache(KMS_CACHE_PATH, kms_cache)
            save_cache(WIKI_CACHE_PATH, wiki_cache)
        disp = display_term(occs)
        s0_vals = s0.get(key, {})
        yml_val = yml_map.get(key)

        # ---- REUSE: 이미 아는 용어 (병기 안 함 — FYI 기록만) ----
        if s0_vals or yml_val:
            known = yml_val or next(iter(s0_vals))
            src = "terms.yml" if yml_val else "S0"
            note = ""
            if len(s0_vals) > 1:  # 코퍼스 자체가 내부적으로 불일치 — 참고용 전체 나열
                variants = ", ".join(f"{ko!r}({sorted(files)})"
                                    for ko, files in s0_vals.items())
                note = f"S0 내부 불일치: {variants}"
            decisions.append(Decision(key, disp, occs, "REUSE",
                                      reason="기존 전례/색인", gloss=known,
                                      source=src, note=note))
            continue

        # ---- 신규 용어: 어느 글(들)에 병기할지 먼저 결정 ----
        files = sorted(set(o.file for o in occs))
        cats = {f: next(o.category for o in occs if o.file == f) for f in files}
        weights = {f: next(o.weight for o in occs if o.file == f) for f in files}

        if len(files) == 1:
            chosen_files = files
            file_note = "단일 등장"
        elif any(w is None for w in weights.values()):
            decisions.append(Decision(
                key, disp, occs, "REVIEW", reason="다중 정의처(weight 누락)",
                note=f"등장 글: {files}"))
            continue
        elif len(set(cats.values())) == 1:
            chosen_files = [min(files, key=lambda f: weights[f])]
            file_note = (f"동일 카테고리({next(iter(cats.values()))}) "
                        f"weight 최소({weights[chosen_files[0]]}) 글 선택")
        else:
            edu_files = [f for f in files if cats[f] in GEN_ED_DIRS]
            other_files = [f for f in files if cats[f] not in GEN_ED_DIRS]
            other_cats = {cats[f] for f in other_files}
            if edu_files and len(other_cats) <= 1:
                # 교양수학 예외: 교양 정의처가 논리적으로 가장 앞선다고 보고,
                # 교양 하나 + (있으면) 비교양 최선위 하나 — 둘 다에 병기.
                primary = min(edu_files, key=lambda f: weights[f])
                chosen_files = [primary]
                file_note = (f"교양수학({cats[primary]}) 정의처 우선 선택 "
                            f"(weight {weights[primary]})")
                if other_files:
                    secondary = min(other_files, key=lambda f: weights[f])
                    chosen_files.append(secondary)
                    file_note += (f"; 비교양({cats[secondary]}) 후속 정의처도 "
                                f"둘째 defs 로 등록 (weight {weights[secondary]})")
                else:
                    file_note += "; 비교양 후속 정의처 없음 — 교양 하나만"
            else:
                cat_w = "; ".join(f"{f}[{cats[f]}/w{weights[f]}]" for f in files)
                decisions.append(Decision(
                    key, disp, occs, "REVIEW",
                    reason="다중 정의처(카테고리 상이·판단불가)", note=cat_w))
                continue

        # ---- 영구 생략 목록 (gloss_skip.yml — gloss_stage.py 와 공유) ----
        if disp.strip().lower() in skip_set:
            decisions.append(Decision(
                key, disp, occs, "REVIEW", reason="gloss_skip.yml 등재(생략 확정)",
                note=f"등장 글: {files}"))
            continue

        # ---- 소스 조회 (KMS → 실패시 Wiki) ----
        if do_network:
            kms = kms_query(disp, kms_cache)
        else:
            kms = kms_cache.get(disp.strip().lower(), {"candidates": []})
        candidates = kms.get("candidates", [])

        if len(candidates) == 1:
            decisions.append(Decision(
                key, disp, occs, "AUTO", reason="KMS exact 단일",
                gloss=candidates[0], source="KMS", chosen_files=chosen_files,
                candidates=candidates, note=file_note))
            continue
        if len(candidates) > 1:
            pick = overrides.get(key)
            if pick is not None and pick in candidates:
                decisions.append(Decision(
                    key, disp, occs, "AUTO", reason="KMS exact 복수(문맥 선택)",
                    gloss=pick, source="KMS", chosen_files=chosen_files,
                    candidates=candidates, note=file_note))
            else:
                decisions.append(Decision(
                    key, disp, occs, "REVIEW",
                    reason="KMS exact 복수(선택 미확정)",
                    candidates=candidates,
                    note=f"{file_note}; overrides 에 gloss_backfill_decisions.json "
                        f"으로 후보 중 하나를 지정할 것"))
            continue

        # KMS 없음 → Wiki
        if do_network:
            wiki = wiki_query(disp, wiki_cache)
        else:
            wiki = wiki_cache.get(disp.strip().lower(),
                                  {"title_en": None, "ko_title": None})
        if wiki.get("ko_title"):
            decisions.append(Decision(
                key, disp, occs, "REVIEW", reason="위키만 있음(형태 도출 필요)",
                gloss=wiki["ko_title"], source=f"wiki:{wiki.get('title_en')}",
                note=file_note))
        else:
            decisions.append(Decision(
                key, disp, occs, "REVIEW", reason="소스 없음", note=file_note))
    return decisions


# ---------------------------------------------------------------------------
# Review 파일 작성
# ---------------------------------------------------------------------------

def write_review(decisions: list[Decision]) -> None:
    auto = [d for d in decisions if d.bucket == "AUTO"]
    review = [d for d in decisions if d.bucket == "REVIEW"]
    reuse = [d for d in decisions if d.bucket == "REUSE"]

    skipped = [d for d in review if d.reason.startswith("gloss_skip.yml")]
    conflict = [d for d in review if ("정의처" in d.reason or "복수" in d.reason)
               and d not in skipped]
    wiki_only = [d for d in review if d.reason.startswith("위키")]
    no_source = [d for d in review if d.reason == "소스 없음"]

    lines: list[str] = []
    lines.append("# gloss_backfill 판정 결과\n")
    lines.append(f"생성: {datetime.now(timezone.utc).isoformat(timespec='seconds')}\n")
    lines.append(f"AUTO {len(auto)} · REVIEW {len(review)} "
                f"(다중정의처/복수미확정 {len(conflict)} · 위키 {len(wiki_only)} · "
                f"무소스 {len(no_source)} · gloss_skip {len(skipped)}) · "
                f"REUSE(조치없음) {len(reuse)}\n")

    lines.append("\n## AUTO (적용분)\n")
    lines.append("| 용어 | gloss | 소스 | 적용 글 | 비고 |\n")
    lines.append("| --- | --- | --- | --- | --- |\n")
    for d in sorted(auto, key=lambda d: d.display.lower()):
        files_disp = ", ".join(f"`{f}`" for f in d.chosen_files)
        lines.append(f"| `{d.display}` | {d.gloss} | {d.reason} | "
                    f"{files_disp} | {d.note} |\n")

    lines.append("\n## REVIEW — 다중 정의처 / KMS 복수후보 미확정\n")
    for d in sorted(conflict, key=lambda d: d.display.lower()):
        cand = f" 후보={d.candidates}" if d.candidates else ""
        lines.append(f"- [ ] `{d.display}` — {d.reason}{cand} — {d.note}\n")

    lines.append("\n## REVIEW — 위키만 도출됨 (형태 조정 필요, 미적용)\n")
    for d in sorted(wiki_only, key=lambda d: d.display.lower()):
        files = sorted(set(o.file for o in d.occs))
        lines.append(f"- [ ] `{d.display}` — 제안 gloss: \"{d.gloss}\" "
                    f"({d.source}) — 등장 글: {files} — {d.note}\n")

    lines.append("\n## REVIEW — 소스 없음\n")
    for d in sorted(no_source, key=lambda d: d.display.lower()):
        files = sorted(set(o.file for o in d.occs))
        ctx = d.occs[0].context if d.occs else ""
        lines.append(f"- [ ] `{d.display}` — 등장 글: {files} — 문맥: …{ctx}…\n")

    if skipped:
        lines.append("\n## REVIEW — gloss_skip.yml 영구 생략 목록 (FYI, 미적용)\n")
        for d in sorted(skipped, key=lambda d: d.display.lower()):
            files = sorted(set(o.file for o in d.occs))
            lines.append(f"- `{d.display}` — 등장 글: {files}\n")

    lines.append("\n## REUSE (조치 없음, FYI) — 정의 서술 패턴이 감지된 재사용\n")
    lines.append("이 항목들은 이미 코퍼스 전례/terms.yml 이 있어 **병기하지 "
                "않았다**. 아래는 그중 정의 서술처럼 읽히는 문맥이 감지된 "
                "출현만 — 사용자가 진짜 재정의였는지 훑어보기 위한 목록이다 "
                "(체크박스 룰링 대상 아님).\n\n")
    n_flag = 0
    for d in sorted(reuse, key=lambda d: d.display.lower()):
        for o in d.occs:
            if o.has_defn_phrasing:
                n_flag += 1
                extra = f" — {d.note}" if d.note else ""
                lines.append(f"- `{d.display}` (알려진 gloss: \"{d.gloss}\", "
                            f"{d.source}{extra}) — `{o.file}` {o.box_label} — "
                            f"문맥: …{o.context}…\n")
    if n_flag == 0:
        lines.append("(감지된 항목 없음)\n")

    REVIEW_PATH.write_text("".join(lines), encoding="utf-8")


# ---------------------------------------------------------------------------
# Stage 4: 적용
# ---------------------------------------------------------------------------

def plan_edits(auto: list[Decision]) -> dict[str, list[tuple[int, str]]]:
    """file → [(insert_at, insert_text), ...] (같은 파일 내 오름차순)."""
    per_file: dict[str, list[tuple[int, str]]] = defaultdict(list)
    for d in auto:
        for o in d.occs:
            if o.file not in d.chosen_files:
                continue  # 선택되지 않은 글의 출현은 재사용으로 두고 손대지 않음
            per_file[o.file].append((o.insert_at, f"<sub>{d.gloss}</sub>"))
    for f in per_file:
        per_file[f].sort(key=lambda t: t[0])
    return per_file


def apply_edits_in_memory(text: str, edits: list[tuple[int, str]]) -> str:
    out = []
    pos = 0
    for ins_at, ins_text in edits:
        out.append(text[pos:ins_at])
        out.append(ins_text)
        pos = ins_at
    out.append(text[pos:])
    return "".join(out)


def verify_file(old_text: str, new_text: str, n_expected: int,
                rel: str) -> tuple[list[str], set[str]]:
    errs = []
    if old_text.count("$") != new_text.count("$"):
        errs.append(f"$ 개수 변경 {old_text.count('$')}→{new_text.count('$')}")
    d_sub = new_text.count("<sub>") - old_text.count("<sub>")
    if d_sub != n_expected:
        errs.append(f"<sub> 증가량 {d_sub} != 기대 {n_expected}")
    # 재탐지: 이 파일에서 적용된 term 들이 무병기 목록에서 사라졌는지
    new_groups = detect_file(rel, new_text)
    remaining_keys = {dedup_key(o.raw) for o in new_groups}
    return errs, remaining_keys


def run_apply(decisions: list[Decision], dry_run: bool) -> dict:
    auto = [d for d in decisions if d.bucket == "AUTO"]
    per_file = plan_edits(auto)

    # membership 안전망: gloss 가 반드시 candidates(또는 REUSE known) 안에 있어야 함
    for d in auto:
        if d.candidates and d.gloss not in d.candidates:
            raise RuntimeError(f"membership 위반: {d.display!r} gloss={d.gloss!r} "
                              f"not in {d.candidates!r}")

    stats = {"files": 0, "subs_added": 0, "failed": []}
    file_texts_new: dict[str, str] = {}
    for rel, edits in per_file.items():
        path = BLOG_ROOT / rel
        old_text = path.read_text(encoding="utf-8")
        # applied term keys for THIS file (used for scoped re-detection check)
        applied_keys = {dedup_key(o.raw) for d in auto for o in d.occs
                       if o.file == rel and rel in d.chosen_files}
        new_text = apply_edits_in_memory(old_text, edits)
        errs, remaining_keys = verify_file(old_text, new_text, len(edits), rel)
        still_bad = applied_keys & remaining_keys
        if still_bad:
            errs.append(f"재탐지 후에도 무병기로 남은 term: {sorted(still_bad)}")
        if errs:
            stats["failed"].append({"file": rel, "errors": errs})
            continue
        stats["files"] += 1
        stats["subs_added"] += len(edits)
        file_texts_new[rel] = new_text

    if dry_run:
        # terms.yml 에 새로 생길 entry 수도 미리보기(쓰지는 않음)
        stats["terms_yml_new_entries"] = register_terms_yml(
            auto, file_texts_new, dry_run=True)
        return {"stats": stats, "file_texts_new": None, "auto": auto}

    # ---- 실제 파일 쓰기 ----
    for rel, new_text in file_texts_new.items():
        (BLOG_ROOT / rel).write_text(new_text, encoding="utf-8")

    # ---- terms.yml 신규 entry 등록 (이미 있는 항목은 건드리지 않음) ----
    n_new_entries = register_terms_yml(auto, file_texts_new, dry_run=False)
    stats["terms_yml_new_entries"] = n_new_entries
    return {"stats": stats, "file_texts_new": file_texts_new, "auto": auto}


def register_terms_yml(auto: list[Decision], file_texts_new: dict[str, str],
                       dry_run: bool) -> int:
    """AUTO 로 실제 적용된(글 파일에 성공적으로 쓰인) 항목만 terms.yml 에 신규
    entry 로 등록. 이미 색인에 있는 항목은 여기 안 옴(REUSE 로 걸러졌음).
    chosen_files 가 둘(교양+비교양)이고 둘 다 성공했으면 defs 를 그 순서
    그대로(교양 먼저) 두 항목 등록한다.
    """
    n_added = 0
    skipped: list[str] = []
    todo = []  # (d, succeeded_files) — succeeded_files 순서 = defs 등록 순서
    for d in auto:
        succeeded_files = [f for f in d.chosen_files if f in file_texts_new]
        if succeeded_files:
            todo.append((d, succeeded_files))
    if not todo:
        return 0

    # read-modify-write: 다른 프로세스(예: 사용자의 방금 수정)가 있었을 수
    # 있으므로 쓰기 직전 최신 파일을 다시 읽는다.
    old_text = TERMS_PATH.read_text(encoding="utf-8")
    header, groups = split_file(old_text)
    idx = entry_index(groups)

    for d, succeeded_files in todo:
        en = d.display
        ko = d.gloss
        k = dedup_key(en)
        if k in idx:
            continue  # 이미 다른 표기로 색인돼 있음 — 건드리지 않음
        lt = letter_of(en)
        if lt is None:
            skipped.append(f"{en!r}: 라틴 글자 없음")
            continue
        try:
            metas = [post_meta(f) for f in succeeded_files]
        except Exception as e:  # noqa: BLE001 — 프론트매터 불완전한 글 하나가
            # 전체 배치를 막지 않게 이 항목만 건너뛰고 계속
            skipped.append(f"{en!r} ({succeeded_files}): post_meta 실패 {e}")
            continue
        prim = decide_primary(en, ko, "en")
        _, permalink0, label0 = metas[0]
        entry = build_entry(en, ko, prim, label0, permalink0, [])
        for _, permalink_i, label_i in metas[1:]:
            entry2 = add_def_to_chunk(entry, label_i, permalink_i)
            if entry2 is not None:
                entry = entry2
        eid = chunk_id(entry)
        if any(chunk_id(c) == eid for c in groups.get(lt, [])):
            continue
        insert_sorted(groups.setdefault(lt, []), entry)
        idx[k] = (lt, len(groups[lt]) - 1)
        n_added += 1
    if skipped:
        print("terms.yml 등록 건너뜀:")
        for s in skipped:
            print(f"  - {s}")

    if n_added == 0:
        return 0
    new_text = join_file(header, groups)
    if not write_gate(old_text, new_text, n_added):
        raise RuntimeError("terms.yml 쓰기 게이트 불통과 — 쓰지 않음")
    if dry_run:
        return n_added
    TERMS_BACKUP_PATH.write_text(old_text, encoding="utf-8")
    tmp = TERMS_PATH.with_suffix(".tmp")
    tmp.write_text(new_text, encoding="utf-8")
    tmp.replace(TERMS_PATH)
    return n_added


# ---------------------------------------------------------------------------
# CLI
# ---------------------------------------------------------------------------

def _prepare(do_network: bool) -> tuple[list[Decision], dict, dict]:
    groups = detect_all()
    s0 = build_s0_map()
    yml_map, _, _ = build_yml_map()
    kms_cache = load_cache(KMS_CACHE_PATH)
    wiki_cache = load_cache(WIKI_CACHE_PATH)
    overrides = load_decisions_overrides()
    skip_set = load_skip_set()
    decisions = classify_all(groups, s0, yml_map, kms_cache, wiki_cache,
                             overrides, skip_set, do_network)
    if do_network:
        save_cache(KMS_CACHE_PATH, kms_cache)
        save_cache(WIKI_CACHE_PATH, wiki_cache)
    return decisions, kms_cache, wiki_cache


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("cmd", choices=["detect", "research", "classify", "apply", "all"])
    ap.add_argument("--dry-run", action="store_true")
    args = ap.parse_args()

    if args.cmd == "detect":
        groups = detect_all()
        n_occ = sum(len(v) for v in groups.values())
        n_files = len({o.file for v in groups.values() for o in v})
        print(f"파일 {n_files} / 출현 {n_occ} / 유니크 용어 {len(groups)}")
        return 0

    if args.cmd == "research":
        decisions, kms_cache, wiki_cache = _prepare(do_network=True)
        print(f"KMS 캐시 {len(kms_cache)} 항목 / Wiki 캐시 {len(wiki_cache)} 항목")
        return 0

    if args.cmd == "classify":
        decisions, _, _ = _prepare(do_network=False)
        write_review(decisions)
        n = Counter(d.bucket for d in decisions)
        print(f"AUTO {n['AUTO']} / REVIEW {n['REVIEW']} / REUSE {n['REUSE']}")
        print(f"review file: {REVIEW_PATH}")
        return 0

    if args.cmd == "apply":
        decisions, _, _ = _prepare(do_network=False)
        result = run_apply(decisions, dry_run=args.dry_run)
        st = result["stats"]
        print(f"[{'DRY-RUN' if args.dry_run else 'APPLY'}] "
             f"파일 {st['files']} / +{st['subs_added']} 병기 / "
             f"실패 {len(st['failed'])}")
        for f in st["failed"]:
            print(f"  실패: {f['file']}: {f['errors']}")
        print(f"terms.yml 신규 entry: {st.get('terms_yml_new_entries', 0)}")
        return 0

    if args.cmd == "all":
        decisions, _, _ = _prepare(do_network=True)
        write_review(decisions)
        result = run_apply(decisions, dry_run=args.dry_run)
        st = result["stats"]
        print(f"[{'DRY-RUN' if args.dry_run else 'APPLY'}] "
             f"파일 {st['files']} / +{st['subs_added']} 병기 / "
             f"실패 {len(st['failed'])}")
        return 0

    return 1


if __name__ == "__main__":
    sys.exit(main())
