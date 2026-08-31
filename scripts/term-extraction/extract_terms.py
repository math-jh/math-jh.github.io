#!/usr/bin/env python3
"""extract_terms.py — 찾아보기 데이터(_data/terms.yml) 용어 수확기.

크론 틱마다 아직 안 훑은(또는 수정된) 한국어 글 하나를 골라 정의 표기를
수확해 terms.yml 에 upsert 한다. 2026-07-18 이전(마크다운 표 Index_ko.md 에
행 삽입)에서 재작성 — 당시 실측된 드리프트·사고에 대한 안전망 포함:

  분류 (원본 유지)
    **English Term<sub>한글</sub>** / *한글<sub>English</sub>*  → 확정(자동 수록)
    <sub> 짝 없는 강조                                          → 리뷰 파일로

  안전망 (재작성에서 추가)
    * 카테고리 대괄호·라벨은 정본에서 파생: categories.yml ko 표시명 +
      대상 글의 현재 frontmatter title. 하드코딩 표는 두지 않는다 (옛
      CATEGORY_KO 는 4개 값이 틀어져 있었고 Manifold/Manifolds 키가 어긋났다).
      categories.yml 에 없는 카테고리면 수록하지 않고 에러.
    * 중복 판정은 dedup_key(발음기호·대소문자·수식 접기) — Čech/čech 처럼
      변형된 중복이 통과하지 못하게.
    * 절(A–Z) 배치는 terms_common.letter_of (수식 래퍼는 속 글자,
      $\\mathfrak{a}$-adic → A). 라틴 글자가 아예 없으면 자동 수록하지 않고
      리뷰로 넘긴다 — Z 절에 던져 두는 관행은 폐지.
    * 쓰기 게이트: 수정본을 쓰기 전에 semantic_checks 로 검사해서 지금
      파일보다 에러가 늘어나면 아무것도 쓰지 않고 실패 처리한다.
    * 실패 격리(quarantine): 같은 글이 3회 실패하면 큐에서 빼고 텔레그램으로
      알린다 — 한 글이 큐를 무한 점유하는 사고(번역 워커 26시간 루프) 방지.
    * 원자적 쓰기 + 직전본 백업(terms.yml.bak), 성공해야만 state 갱신.

cron (자리는 잡혀 있고 현재 PAUSED):
    */20 * * * * cd .../scripts/term-extraction && python3 extract_terms.py >>extract_terms.log 2>&1
"""
from __future__ import annotations

import argparse
import json
import os
import re
import sys
import unicodedata
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

import yaml

sys.path.insert(0, str(Path(__file__).resolve().parent))
from terms_common import (  # noqa: E402
    BLOG_ROOT, TERMS_PATH, category_ko_maps, chunk_field, chunk_id,
    dedup_key, insert_sorted, join_file, letter_of, permalink_map,
    render_entry, semantic_checks, slugify_id, split_file, yaml_quote,
)

POSTS_ROOT = BLOG_ROOT / "_posts" / "Math"
SCRIPT_DIR = Path(__file__).resolve().parent
STATE_PATH = SCRIPT_DIR / "term_extraction_state.json"
REVIEW_PATH = SCRIPT_DIR / "term_extraction_review.md"
BACKUP_PATH = SCRIPT_DIR / "terms.yml.bak"
LOCK_PATH = Path("/tmp/extract-terms.lock")
MAX_FAILURES = 3


def log(msg: str) -> None:
    print(f"[{datetime.now():%Y-%m-%d %H:%M:%S}] {msg}")


def send_notify(msg: str) -> None:
    """알림 한 통. 벤더는 shim(~/.local/bin/notify) 안에만 있다."""
    import subprocess
    notify = Path.home() / ".local/bin/notify"
    try:
        r = subprocess.run(
            [str(notify), "-s", "[extract_terms]", "-b", msg, "-g", "blog"],
            capture_output=True, text=True, timeout=20)
        if r.returncode != 0:
            log(f"알림 전송 실패 rc={r.returncode}: {r.stderr.strip()[:200]}")
    except Exception as e:  # noqa: BLE001
        log(f"알림 전송 실패: {e}")


# ---------------------------------------------------------------------------
# Lock & state
# ---------------------------------------------------------------------------

def acquire_lock() -> bool:
    if LOCK_PATH.exists():
        try:
            os.kill(int(LOCK_PATH.read_text().strip()), 0)
            return False
        except (ValueError, ProcessLookupError, PermissionError):
            pass
    LOCK_PATH.write_text(str(os.getpid()))
    return True


def release_lock() -> None:
    try:
        LOCK_PATH.unlink()
    except FileNotFoundError:
        pass


def load_state() -> dict[str, Any]:
    if STATE_PATH.exists():
        st = json.loads(STATE_PATH.read_text(encoding="utf-8"))
    else:
        st = {}
    st.setdefault("files", {})
    st.setdefault("failures", {})   # rel → 연속 실패 횟수
    st.setdefault("quarantine", []) # 3회 실패로 격리된 rel 목록
    return st


def save_state(state: dict[str, Any]) -> None:
    tmp = STATE_PATH.with_suffix(".tmp")
    tmp.write_text(json.dumps(state, indent=2, ensure_ascii=False), encoding="utf-8")
    tmp.replace(STATE_PATH)


# ---------------------------------------------------------------------------
# Post parsing (원본 유지)
# ---------------------------------------------------------------------------

_FM_RE = re.compile(r"^---\s*\n(.*?)\n---\s*\n", re.DOTALL)


def parse_frontmatter(text: str) -> dict[str, str]:
    m = _FM_RE.match(text)
    if not m:
        return {}
    fm: dict[str, str] = {}
    for line in m.group(1).splitlines():
        if ":" in line and not line.lstrip().startswith("#"):
            k, _, v = line.partition(":")
            fm[k.strip()] = v.strip().strip('"').strip("'")
    return fm


def is_unpublished(text: str) -> bool:
    return parse_frontmatter(text).get("published", "").strip().lower() == "false"


def frontmatter_categories(text: str) -> list[str]:
    m = _FM_RE.match(text)
    if not m:
        return []
    for line in m.group(1).splitlines():
        if line.startswith("categories:"):
            raw = line.split(":", 1)[1].strip().strip("[]")
            return [c.strip().strip('"').strip("'") for c in raw.split(",") if c.strip()]
    return []


def strip_frontmatter(text: str) -> str:
    return _FM_RE.sub("", text, count=1)


_FILENAME_DATE_RE = re.compile(r"^(\d{4})-(\d{2})-(\d{2})-")


def _publication_date_key(path: Path) -> tuple[int, int, int, str]:
    m = _FILENAME_DATE_RE.match(path.name)
    if not m:
        return (9999, 12, 31, path.name)
    return (int(m.group(1)), int(m.group(2)), int(m.group(3)), path.name)


def pick_next_post(state: dict[str, Any]) -> Path | None:
    """다음 스캔 대상: 새 글 또는 마지막 스캔 후 수정된 글, 발행일 오래된
    순. 격리(quarantine)된 글은 건너뛴다."""
    seen = state["files"]
    quarantined = set(state["quarantine"])
    candidates: list[Path] = []
    for p in POSTS_ROOT.rglob("ko/*.md"):
        rel = str(p.relative_to(BLOG_ROOT))
        if rel in quarantined:
            continue
        last = seen.get(rel)
        if last is not None and float(last) >= p.stat().st_mtime - 1:
            continue
        try:
            text = p.read_text(encoding="utf-8")
        except (OSError, UnicodeDecodeError):
            continue
        if is_unpublished(text):
            continue
        candidates.append(p)
    if not candidates:
        return None
    candidates.sort(key=_publication_date_key)
    return candidates[0]


# ---------------------------------------------------------------------------
# Term extraction (원본 유지)
# ---------------------------------------------------------------------------

_DEF_RE = re.compile(
    r"(?P<emph>\*\*|\*)"
    r"(?P<a>[^*\n<]+?)"
    r"\.?\s*<sub>\s*(?P<b>[^<]+?)\s*</sub>"
    r"(?P=emph)",
    re.UNICODE,
)

# 정리 블록 fence 헤더의 정의 (2026-07-03 fenced theorem block 마이그레이션
# 이후 정의 다수가 이 형태다 — 옛 수확기는 이걸 몰라서 마이그레이션된 글에서
# 확정 0 이 나왔다):
#   ::: misc The Axiom of Pair.<sub>짝 공리</sub> {#axiom-pair}
# {#anchor} 가 있으면 def url 에 앵커로 싣는다.
_BLOCK_DEF_RE = re.compile(
    r"^:{3,}\s*[a-z-]+\s+"
    r"(?P<a>[^<\n]+?)"
    r"\.?\s*<sub>\s*(?P<b>[^<\n]+?)\s*</sub>"
    r".*?(?:\{#(?P<anchor>[^}\s]+)\})?\s*$",
    re.UNICODE | re.MULTILINE,
)

_AMBIG_RE = re.compile(
    r"(?<![*\w])(?P<emph>\*\*|\*)(?P<term>[^*\n<>{}\[\]]{2,60})(?P=emph)(?![*\w])",
    re.UNICODE,
)

_HANGUL_RE = re.compile(r"[ㄱ-ㆎ가-힣]")
_LATIN_RE = re.compile(r"[A-Za-z]")


def _is_korean(s: str) -> bool:
    return bool(_HANGUL_RE.search(s))


def _is_latin(s: str) -> bool:
    return bool(_LATIN_RE.search(s) and not _HANGUL_RE.search(s))


_LEAD_THE_RE = re.compile(r"^\s*the\s+", re.IGNORECASE)

_PROPER_NOUNS = {
    "abel", "abel-jacobi",
    "bott", "boutet", "calabi", "calabi-yau", "cartan", "cech", "cesaro",
    "chern", "chevalley", "christoffel", "cohen-macaulay", "cohen",
    "deligne", "dirichlet", "dynkin", "euler", "fano", "fourier",
    "frobenius", "galois", "gauss", "godement", "gorenstein", "grothendieck",
    "hilbert", "hodge", "jacobi", "kahler", "kähler", "killing", "klein",
    "kodaira", "kronecker", "lagrange", "laurent", "lefschetz", "leray",
    "lie", "milnor", "minkowski", "morita", "mukai", "nakayama", "newton",
    "noether", "novikov", "picard", "poincare", "poincaré", "pontryagin",
    "ricci", "riemann", "schubert", "serre", "siegel", "stokes", "stiefel",
    "tate", "verma", "weil", "weyl", "yoneda", "young", "zariski",
}


def _normalize_english(s: str) -> str:
    s = s.strip().rstrip(".")
    s = _LEAD_THE_RE.sub("", s, count=1).strip()
    if not s:
        return s
    tokens = re.split(r"(\s+|-)", s)
    out: list[str] = []
    for tok in tokens:
        if not tok or tok.isspace() or tok == "-":
            out.append(tok)
            continue
        if not tok[0].isascii():
            out.append(tok)
            continue
        if "$" in tok:                    # 수식 구간($G$-module 등) 케이스 보존
            out.append(tok)
            continue
        if tok.lower() in _PROPER_NOUNS:
            out.append(tok)
            continue
        if re.match(r"^[A-Z]$", tok) and len(tokens) > 1:
            out.append(tok)
            continue
        out.append(tok.lower())
    return "".join(out)


def classify_definitions(body: str) -> tuple[list[dict[str, str]], list[dict[str, str]]]:
    definite: list[dict[str, str]] = []
    seen_pairs: set[tuple[str, str]] = set()

    def _classify_pair(a: str, b: str, anchor: str | None) -> None:
        if not a or not b:
            return
        a_ko, b_ko = _is_korean(a), _is_korean(b)
        a_en, b_en = _is_latin(a), _is_latin(b)
        if a_ko == b_ko and a_en == b_en:
            return
        if a_en and b_ko:
            primary, eng, kor = "en", a, b
        elif a_ko and b_en:
            primary, eng, kor = "ko", b, a
        else:
            return
        eng = _normalize_english(eng)
        kor = kor.strip().rstrip(".")
        if not eng or not kor:
            return
        key = (eng.lower(), kor)
        if key in seen_pairs:
            return
        seen_pairs.add(key)
        definite.append({"english": eng, "korean": kor, "primary": primary,
                         "anchor": anchor or ""})

    for m in _BLOCK_DEF_RE.finditer(body):
        _classify_pair(m.group("a").strip(), m.group("b").strip(), m.group("anchor"))
    for m in _DEF_RE.finditer(body):
        _classify_pair(m.group("a").strip(), m.group("b").strip(), None)

    ambiguous: list[dict[str, str]] = []
    seen_ambig: set[str] = set()

    biblio_line_re = re.compile(r"^\s*\*\*\[[A-Za-z0-9]+\]\*\*", re.MULTILINE)
    biblio_spans: list[tuple[int, int]] = []
    for bm in biblio_line_re.finditer(body):
        end = body.find("\n\n", bm.end())
        if end == -1:
            end = len(body)
        biblio_spans.append((bm.start(), end))

    for m in _AMBIG_RE.finditer(body):
        term = m.group("term").strip()
        if "<sub>" in term or len(term) < 2:
            continue
        if re.match(r"^(예시|명제|정의|정리|보조정리|따름정리|참고문헌|증명|참고|약속|기호|주의|관찰)\b", term):
            continue
        if re.match(r"^[ㄱ-ㆎ가-힣]{1,3}$", term) and term in {
            "이거나", "이고", "또는", "그리고", "그러므로", "따라서", "즉",
        }:
            continue
        if not (_HANGUL_RE.search(term) or _LATIN_RE.search(term)):
            continue
        pos = m.start()
        if any(s <= pos < e for s, e in biblio_spans):
            continue
        if term in seen_ambig:
            continue
        seen_ambig.add(term)
        recommendation = "looks like emphasis (no <sub> partner)"
        if _LATIN_RE.search(term) and _HANGUL_RE.search(term):
            recommendation = "mixed-script emphasis — possibly a definition"
        elif _LATIN_RE.search(term) and " " in term:
            recommendation = "multi-word English emphasis — possibly a definition"
        ambiguous.append({"term": term, "recommendation": recommendation})

    return definite, ambiguous


# ---------------------------------------------------------------------------
# terms.yml upsert
# ---------------------------------------------------------------------------

def add_def_to_chunk(chunk: str, label: str, url: str) -> str | None:
    """기존 항목 청크에 def 를 추가. 같은 글(앵커 무시)이 이미 있으면 None(no-op)."""
    base = url.split("#")[0].rstrip("/")
    lines = chunk.split("\n")
    for ln in lines:
        m = re.match(r"^\s*url: (\S+)$", ln)
        if m and m.group(1).split("#")[0].rstrip("/") == base:
            return None
    pair = [f"  - label: '{label.replace(chr(39), chr(39) * 2)}'", f"    url: {url}"]
    for i, ln in enumerate(lines):
        if ln.rstrip() == "  defs:":
            j = i + 1
            while j < len(lines) and (lines[j].startswith("  - ") or lines[j].startswith("    ")):
                j += 1
            return "\n".join(lines[:j] + pair + lines[j:])
    # defs 블록이 없는(bare) 항목: refs/see 앞에 신설
    insert = len(lines)
    for i, ln in enumerate(lines):
        if ln.rstrip() in ("  refs:", "  see:"):
            insert = i
            break
    return "\n".join(lines[:insert] + ["  defs:"] + pair + lines[insert:])


def upsert_terms(text: str, terms: list[dict[str, str]], label: str,
                 permalink: str) -> tuple[str, list[str], list[dict[str, str]]]:
    """terms.yml 텍스트에 확정 용어들을 upsert.

    반환: (새 텍스트, 변경 설명 목록, 자동 수록 불가로 리뷰로 넘길 항목)."""
    header, groups = split_file(text)
    changes: list[str] = []
    deferred: list[dict[str, str]] = []

    # 전역 색인: dedup_key(en) → (letter, index). 옛 항목이 잘못된 그룹에
    # 있어도 찾도록 전 그룹을 뒤진다.
    by_key: dict[str, tuple[str, int]] = {}
    ids: set[str] = set()
    for letter, chunks in groups.items():
        for i, c in enumerate(chunks):
            by_key.setdefault(dedup_key(chunk_field(c, "en") or ""), (letter, i))
            ids.add(chunk_id(c))

    for term in terms:
        eng, kor, primary = term["english"], term["korean"], term["primary"]
        url = permalink + (f"#{term['anchor']}" if term.get("anchor") else "")
        k = dedup_key(eng)
        if k in by_key:
            letter, i = by_key[k]
            new_chunk = add_def_to_chunk(groups[letter][i], label, url)
            if new_chunk is None:
                continue  # 이미 이 글을 가리킴 — 멱등
            groups[letter][i] = new_chunk
            changes.append(f"def 추가: {eng!r} ← {url}")
            continue
        lo = letter_of(eng)
        if lo is None:
            # 라틴 글자가 없어 절 배치 불가 — Z 에 던지지 않고 리뷰로.
            deferred.append({"term": f"{eng} / {kor}",
                             "recommendation": "no Latin letter — 절 배치 불가, 손으로 수록"})
            continue
        eid = slugify_id(eng)
        while eid in ids:  # id 충돌(다른 en 인데 같은 슬러그) — 접미사로 회피
            eid += "_2"
        ids.add(eid)
        chunk = render_entry(eid, eng, kor, "ko" if primary == "ko" else None,
                             label, url)
        insert_sorted(groups.setdefault(lo, []), chunk)
        by_key[k] = (lo, groups[lo].index(chunk))
        changes.append(f"신규 수록: {eng!r} ({primary}-first) → {lo} 절")

    return join_file(header, groups), changes, deferred


# ---------------------------------------------------------------------------
# Review file
# ---------------------------------------------------------------------------

def append_review(post_rel: str, post_title: str, permalink: str,
                  ambiguous: list[dict[str, str]]) -> None:
    if not ambiguous:
        return
    stamp = datetime.now(timezone.utc).isoformat(timespec="seconds")
    chunks: list[str] = []
    if not REVIEW_PATH.exists():
        chunks.append("# Term-extraction review\n\n")
        chunks.append("Items below were flagged as **ambiguous** (no `<sub>` partner).\n")
        chunks.append("Decide whether each one is a definition and add it to `_data/terms.yml` "
                      "(then run `terms_lint.py` to verify).\n\n")
    chunks.append(f"## {post_title}\n")
    chunks.append(f"- post: `{post_rel}`\n- permalink: `{permalink}`\n- scanned: {stamp}\n\n")
    chunks.append("| term | agent recommendation |\n| --- | --- |\n")
    for a in ambiguous:
        term = a["term"].replace("|", "\\|")
        rec = a["recommendation"].replace("|", "\\|")
        chunks.append(f"| `{term}` | {rec} |\n")
    chunks.append("\n")
    with REVIEW_PATH.open("a", encoding="utf-8") as f:
        f.write("".join(chunks))


# ---------------------------------------------------------------------------
# 한 글 처리 (쓰기 게이트 포함)
# ---------------------------------------------------------------------------

def process_post(post: Path, state: dict[str, Any], dry_run: bool) -> bool:
    """True = 성공(state 갱신됨), False = 실패(실패 카운트 증가)."""
    rel = str(post.relative_to(BLOG_ROOT))
    text = post.read_text(encoding="utf-8")
    if is_unpublished(text):
        log(f"건너뜀 {rel}: published: false")
        state["files"][rel] = post.stat().st_mtime
        return True
    fm = parse_frontmatter(text)
    permalink = fm.get("permalink", "")
    title = fm.get("title", post.stem)
    cats = frontmatter_categories(text)

    _, ko_by_name = category_ko_maps()
    category_ko = next((ko_by_name[c] for c in cats if c in ko_by_name), None)

    body = strip_frontmatter(text)
    definite, ambiguous = classify_definitions(body)

    log(f"스캔 {rel}")
    log(f"  title={title!r} permalink={permalink} category_ko={category_ko!r}")
    log(f"  확정 {len(definite)} · 모호 {len(ambiguous)}")

    if not permalink:
        log(f"  실패: permalink 없음")
        return False
    if definite and not category_ko:
        log(f"  실패: categories {cats!r} 가 categories.yml subjects 에 없음 — 수록 불가")
        return False

    if dry_run:
        for t in definite:
            print(f"  + {t['primary']}: {t['english']} / {t['korean']}")
        for a in ambiguous:
            print(f"  ? {a['term']} ({a['recommendation']})")
        return True

    if definite:
        label = f"[{category_ko}] §{title}"
        old_text = TERMS_PATH.read_text(encoding="utf-8")
        new_text, changes, deferred = upsert_terms(old_text, definite, label, permalink)
        ambiguous = ambiguous + deferred

        if new_text != old_text:
            # ── 쓰기 게이트: 수정본이 지금보다 나빠지면 아무것도 쓰지 않는다 ──
            pmap = permalink_map()
            ko_by_slug, _ = category_ko_maps()
            try:
                old_data = yaml.safe_load(old_text)
                new_data = yaml.safe_load(new_text)
            except yaml.YAMLError as e:
                log(f"  실패: upsert 결과가 YAML 파싱 불가 — 쓰지 않음: {e}")
                return False
            old_ids = {t["id"] for v in old_data.values() for t in (v or [])}
            new_ids = {t["id"] for v in new_data.values() for t in (v or [])}
            if not old_ids <= new_ids:
                log(f"  실패: 기존 항목이 사라짐 {sorted(old_ids - new_ids)[:5]} — 쓰지 않음")
                return False
            base = {i.key() for i in semantic_checks(old_data, pmap, ko_by_slug) if i.level == "E"}
            new_issues = {i.key() for i in semantic_checks(new_data, pmap, ko_by_slug) if i.level == "E"}
            introduced = new_issues - base
            if introduced:
                log(f"  실패: upsert 가 새 에러 유발 — 쓰지 않음: {sorted(introduced)[:5]}")
                return False

            BACKUP_PATH.write_text(old_text, encoding="utf-8")
            tmp = TERMS_PATH.with_suffix(".tmp")
            tmp.write_text(new_text, encoding="utf-8")
            tmp.replace(TERMS_PATH)
        for c in changes:
            log(f"  * {c}")

    append_review(rel, title, permalink, ambiguous)
    state["files"][rel] = post.stat().st_mtime
    state["failures"].pop(rel, None)
    return True


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------

def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--dry-run", action="store_true")
    ap.add_argument("--file", help="이 글만 처리 (state 무시)")
    ap.add_argument("--all", action="store_true", help="큐 전체 소진 (백필용)")
    args = ap.parse_args()

    if not acquire_lock():
        print("another instance is running; bailing.")
        return 0

    try:
        state = load_state()

        if args.file:
            post = Path(args.file)
            if not post.is_absolute():
                post = BLOG_ROOT / post
            posts = [post]
        elif args.all:
            posts = []
            while True:
                p = pick_next_post(state)
                if p is None or p in posts:
                    break
                posts.append(p)
                state["files"][str(p.relative_to(BLOG_ROOT))] = p.stat().st_mtime  # 임시 마킹
            # 실제 처리 전에 임시 마킹 원복
            for p in posts:
                state["files"].pop(str(p.relative_to(BLOG_ROOT)), None)
        else:
            p = pick_next_post(state)
            if p is None:
                print("no posts need rescanning.")
                return 0
            posts = [p]

        rc = 0
        for post in posts:
            rel = str(post.relative_to(BLOG_ROOT))
            try:
                ok = process_post(post, state, args.dry_run)
            except Exception as e:  # noqa: BLE001
                log(f"  크래시: {e!r}")
                ok = False
            if not ok and not args.dry_run:
                n = state["failures"].get(rel, 0) + 1
                state["failures"][rel] = n
                if n >= MAX_FAILURES:
                    state["quarantine"].append(rel)
                    state["failures"].pop(rel, None)
                    log(f"  격리: {rel} ({MAX_FAILURES}회 실패) — 큐에서 제외")
                    send_notify(f"{rel} 이 {MAX_FAILURES}회 실패해 격리됨. "
                                f"로그 확인 후 state 의 quarantine 에서 빼 주세요.")
                rc = 1
            if not args.dry_run:
                save_state(state)
        return rc
    finally:
        release_lock()


if __name__ == "__main__":
    sys.exit(main())
