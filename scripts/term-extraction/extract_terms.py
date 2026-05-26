#!/usr/bin/env python3
"""
extract_terms.py — single-shot term harvester for _pages/ko/Index_ko.md.

Each cron tick picks ONE Korean post that hasn't been processed yet (or whose
mtime is newer than the last scan), scans it for math-term definitions, and
folds the result into the index:

  Definitive forms (auto-add to Index_ko.md)
    **English Term.<sub>한글 용어</sub>**         -> English-first
    *English term<sub>한글 용어</sub>*            -> English-first
    **한글 용어<sub>English Term.</sub>**         -> Korean-first
    *한글 용어<sub>English Term</sub>*            -> Korean-first

  Ambiguous (written to scripts/term-extraction/term_extraction_review.md instead)
    *term*                  (no <sub> partner)
    **term**                (could be emphasis or a definition)

The "definition" reference inserted into Index_ko.md follows the existing
convention, e.g.
    [\\[집합론\\] §ZFC 공리계](/ko/math/set_theory/zfc_axioms)
and is merged with `<br/>` separators when the term is defined in several
posts (the user's rule for `associative law` etc.).

Cron:
    */20 * * * * cd /home/junhyeok/math-jh.github.io/scripts/term-extraction \\
                 && /usr/bin/python3 extract_terms.py >>extract_terms.log 2>&1
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

BLOG_ROOT   = Path("/home/junhyeok/math-jh.github.io")
POSTS_ROOT  = BLOG_ROOT / "_posts" / "Math"
INDEX_PATH  = BLOG_ROOT / "_pages" / "ko" / "Index_ko.md"
SCRIPT_DIR  = Path(__file__).resolve().parent
STATE_PATH  = SCRIPT_DIR / "term_extraction_state.json"
REVIEW_PATH = SCRIPT_DIR / "term_extraction_review.md"
LOCK_PATH   = Path("/tmp/extract-terms.lock")

# Map `categories:` frontmatter values to the Korean label used inside
# Index_ko.md's "정의" column (e.g. "Math / Set Theory" -> "집합론").
CATEGORY_KO: dict[str, str] = {
    "Math / Set Theory":           "집합론",
    "Math / Linear Algebra":       "선형대수학",
    "Math / Multilinear Algebra":  "다중선형대수학",
    "Math / Category Theory":      "범주론",
    "Math / Algebraic Structures": "대수적 구조",
    "Math / Group Theory":         "군론",
    "Math / Ring Theory":          "환론",
    "Math / Field Theory":         "체론",
    "Math / Homological Algebra":  "호몰로지 대수학",
    "Math / Commutative Algebra":  "가환대수학",
    "Math / Representation Theory":"표현론",
    "Math / Topology":             "위상수학",
    "Math / Algebraic Topology":   "대수적 위상수학",
    "Math / Manifold":             "미분다양체",
    "Math / Lie Theory":           "리 이론",
    "Math / Riemannian Geometry":  "리만기하학",
    "Math / Algebraic Varieties":  "대수기하학",
    "Math / Scheme Theory":        "스킴 이론",
    "Math / Toric Geometry":       "Toric 기하학",
    "Math / Symplectic Geometry":  "심플렉틱 기하학",
    "Math / Mirror Symmetry":      "거울대칭",
    "Misc / Blog Development":     "블로그 개발",
    "Misc / Peripherals":          "주변기기",
}

# ---------------------------------------------------------------------------
# Lock & state
# ---------------------------------------------------------------------------

def acquire_lock() -> bool:
    if LOCK_PATH.exists():
        try:
            pid = int(LOCK_PATH.read_text().strip())
            os.kill(pid, 0)
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
        return json.loads(STATE_PATH.read_text(encoding="utf-8"))
    return {"files": {}}


def save_state(state: dict[str, Any]) -> None:
    tmp = STATE_PATH.with_suffix(".tmp")
    tmp.write_text(json.dumps(state, indent=2, ensure_ascii=False), encoding="utf-8")
    tmp.replace(STATE_PATH)


# ---------------------------------------------------------------------------
# Post parsing
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
    """Return True if the frontmatter has `published: false`.
    Drafts/hidden posts are skipped by the picker."""
    fm = parse_frontmatter(text)
    return fm.get("published", "").strip().lower() == "false"


def frontmatter_categories(text: str) -> list[str]:
    m = _FM_RE.match(text)
    if not m:
        return []
    for line in m.group(1).splitlines():
        if line.startswith("categories:"):
            raw = line.split(":", 1)[1].strip()
            raw = raw.strip("[]")
            return [c.strip().strip('"').strip("'") for c in raw.split(",") if c.strip()]
    return []


def strip_frontmatter(text: str) -> str:
    return _FM_RE.sub("", text, count=1)


_FILENAME_DATE_RE = re.compile(r"^(\d{4})-(\d{2})-(\d{2})-")


def _publication_date_key(path: Path) -> tuple[int, int, int, str]:
    """Sort key derived from the YYYY-MM-DD prefix on the filename.
    Posts without a date prefix fall back to (9999, 12, 31, name) so they
    sort to the very end — they aren't real published posts."""
    m = _FILENAME_DATE_RE.match(path.name)
    if not m:
        return (9999, 12, 31, path.name)
    return (int(m.group(1)), int(m.group(2)), int(m.group(3)), path.name)


def pick_next_post(state: dict[str, Any]) -> Path | None:
    """Return the next post to scan, or None if everything is up-to-date.

    Processed/unprocessed bookkeeping
    ---------------------------------
    State lives at scripts/term-extraction/term_extraction_state.json:
        { "files": { "<rel_path>": <last_scanned_mtime>, ... } }
    A post is considered processed when its rel-path is in `files` and
    the stored mtime is ≥ the file's current mtime (minus a 1-second
    fudge for filesystems with poor mtime precision). Any post that is
    new, or has been edited since the last scan, becomes a candidate.

    Selection order
    ---------------
    Oldest by **publication date** (YYYY-MM-DD prefix on the filename)
    first — this matches the natural reading order of the blog so that
    foundational posts seed Index_ko.md before later posts cite them.
    """
    seen = state.get("files", {})
    candidates: list[Path] = []
    for p in POSTS_ROOT.rglob("ko/*.md"):
        rel = str(p.relative_to(BLOG_ROOT))
        last = seen.get(rel)
        mtime = p.stat().st_mtime
        if last is not None and float(last) >= mtime - 1:
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
# Term extraction
# ---------------------------------------------------------------------------

# Definitive forms — bold or italic wrapper around `TERM<sub>OTHER</sub>`.
# The dot after Term is optional ("Axiom of Existence." vs "Axiom of Existence").
_DEF_RE = re.compile(
    r"(?P<emph>\*\*|\*)"
    r"(?P<a>[^*\n<]+?)"
    r"\.?\s*<sub>\s*(?P<b>[^<]+?)\s*</sub>"
    r"(?P=emph)",
    re.UNICODE,
)

# Ambiguous: single-language emphasis. Captured for review only.
_AMBIG_RE = re.compile(
    r"(?<![*\w])(?P<emph>\*\*|\*)(?P<term>[^*\n<>{}\[\]]{2,60})(?P=emph)(?![*\w])",
    re.UNICODE,
)

_HANGUL_RE = re.compile(r"[ㄱ-ㆎ가-힣]")
_LATIN_RE  = re.compile(r"[A-Za-z]")


def _is_korean(s: str) -> bool:
    return bool(_HANGUL_RE.search(s))


def _is_latin(s: str) -> bool:
    return bool(_LATIN_RE.search(s) and not _HANGUL_RE.search(s))


_LEAD_THE_RE = re.compile(r"^\s*the\s+", re.IGNORECASE)


_PROPER_NOUNS = {
    # Mathematician names the index keeps capitalised.
    "abel", "abel-jacobi",  # exception: "abelian" → lowercase
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
    """Strip the introductory article "The" and a trailing period, then
    lowercase every word that isn't a recognised proper noun. Single-capital
    prefixes (K-theory, L-function) are preserved."""
    s = s.strip().rstrip(".")
    s = _LEAD_THE_RE.sub("", s, count=1).strip()
    if not s:
        return s
    # Split into word tokens while keeping separators so we can rejoin verbatim.
    tokens = re.split(r"(\s+|-)", s)
    out: list[str] = []
    for tok in tokens:
        if not tok or tok.isspace() or tok == "-":
            out.append(tok)
            continue
        if not tok[0].isascii():
            out.append(tok)
            continue
        if tok.lower() in _PROPER_NOUNS:
            out.append(tok)
            continue
        # Single-capital prefix like "K" in "K-theory".
        if re.match(r"^[A-Z]$", tok) and "".join(out).endswith("-") is False and len(tokens) > 1:
            # only preserve when followed by a hyphen-word
            out.append(tok)
            continue
        out.append(tok.lower())
    return "".join(out)


def classify_definitions(body: str) -> tuple[list[dict[str, str]], list[dict[str, str]]]:
    """Return (definite_terms, ambiguous_terms)."""
    definite: list[dict[str, str]] = []
    seen_pairs: set[tuple[str, str]] = set()

    for m in _DEF_RE.finditer(body):
        a, b = m.group("a").strip(), m.group("b").strip()
        if not a or not b:
            continue
        # Skip when both halves are the same language (probably not a translation pair).
        a_ko, b_ko = _is_korean(a), _is_korean(b)
        a_en, b_en = _is_latin(a), _is_latin(b)
        if a_ko == b_ko and a_en == b_en:
            continue
        # Outer is the primary (visible) form; <sub> is the secondary.
        if a_en and b_ko:
            primary = "en"
            eng, kor = a, b
        elif a_ko and b_en:
            primary = "ko"
            eng, kor = b, a
        else:
            continue
        eng = _normalize_english(eng)
        kor = kor.strip().rstrip(".")
        if not eng or not kor:
            continue
        key = (eng.lower(), kor)
        if key in seen_pairs:
            continue
        seen_pairs.add(key)
        definite.append({"english": eng, "korean": kor, "primary": primary})

    # Ambiguous: anything that's plainly emphasised but didn't match a <sub> pair.
    # Skip very short tokens like "a", "b" and obvious section/heading bold like
    # "**예시 N**" or "**참고문헌**" (we don't want those in the index).
    ambiguous: list[dict[str, str]] = []
    seen_ambig: set[str] = set()

    # Skip emphasis that occurs inside a bibliography line such as
    #   "**[HJJ]** K. Hrbacek, ... *Introduction to Set Theory*."
    biblio_line_re = re.compile(r"^\s*\*\*\[[A-Za-z0-9]+\]\*\*", re.MULTILINE)
    biblio_spans: list[tuple[int, int]] = []
    for bm in biblio_line_re.finditer(body):
        # Capture the rest of the bibliography paragraph (until blank line).
        end = body.find("\n\n", bm.end())
        if end == -1:
            end = len(body)
        biblio_spans.append((bm.start(), end))

    for m in _AMBIG_RE.finditer(body):
        term = m.group("term").strip()
        if "<sub>" in term:
            continue
        if len(term) < 2:
            continue
        # Drop "예시 N", "명제 N", "참고문헌", "정리 N" etc.
        if re.match(r"^(예시|명제|정의|정리|보조정리|따름정리|참고문헌|증명|참고|약속|기호|주의|관찰)\b", term):
            continue
        # Drop Korean particles / conjunctions that escaped via **A 이거나 B**.
        if re.match(r"^[ㄱ-ㆎ가-힣]{1,3}$", term) and term in {
            "이거나", "이고", "또는", "그리고", "그러므로", "따라서", "즉",
        }:
            continue
        # Drop pure numerics / symbols.
        if not (_HANGUL_RE.search(term) or _LATIN_RE.search(term)):
            continue
        # Skip if inside a bibliography line.
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
# Index_ko.md mutation
# ---------------------------------------------------------------------------

_SECTION_HEADER_RE = re.compile(r"^##\s+([A-Z])\s*$", re.MULTILINE)
_ROW_ID_RE = re.compile(r'<(?:selected|unselected)\s+id="([^"]+)"', re.IGNORECASE)
# Pull the English term out of a row. The English cell is whichever of the
# two `<selected>` / `<unselected>` cells contains Latin letters.
_ROW_CELL_RE = re.compile(r"<(selected|unselected)(?:\s+id=\"[^\"]*\")?\s*>(.*?)</\1>", re.IGNORECASE | re.DOTALL)


def _english_in_row(row: str) -> str | None:
    """Return the lower-cased English term displayed in this Index row, or None."""
    for _, inner in _ROW_CELL_RE.findall(row):
        text = re.sub(r"&#?\w+;", "", inner).strip()  # drop &#9745; etc.
        text = re.sub(r"\s+", " ", text).strip()
        if _LATIN_RE.search(text) and not _HANGUL_RE.search(text):
            return text.lower()
    return None


def _sort_key(s: str) -> str:
    """Accent- and case-insensitive lexicographic key.

    Folding diacritics so that Č sorts next to c, é next to e, etc. Without
    this, raw code-point comparison places Č (U+010D) after every lowercase
    ASCII letter, which caused new c-words to land above existing Čech rows.
    """
    norm = unicodedata.normalize("NFKD", s.casefold())
    return "".join(ch for ch in norm if not unicodedata.combining(ch))


def _slugify_id(eng: str) -> str:
    s = eng.lower().strip()
    s = re.sub(r"[^\w\-]+", "_", s, flags=re.UNICODE)
    s = re.sub(r"_+", "_", s).strip("_")
    return s


def _build_row(eng: str, kor: str, primary: str, def_link: str) -> str:
    eng_id = _slugify_id(eng)
    if primary == "en":
        eng_cell = f'<selected id="{eng_id}">{eng} &#9745;</selected>'
        kor_cell = f'<unselected>{kor}</unselected>'
    else:
        eng_cell = f'<unselected id="{eng_id}">{eng}</unselected>'
        kor_cell = f'<selected>{kor} &#9745;</selected>'
    return f"| {eng_cell} | {kor_cell} | {def_link} |  |"


def _def_link(category_ko: str, post_title: str, permalink: str) -> str:
    return f"[\\[{category_ko}\\] §{post_title}]({permalink})"


def upsert_terms(
    index_text: str,
    terms: list[dict[str, str]],
    category_ko: str,
    post_title: str,
    permalink: str,
) -> tuple[str, list[str]]:
    """Return (new_index_text, list_of_change_descriptions)."""
    changes: list[str] = []
    lines = index_text.splitlines(keepends=True)

    # Precompute (start_line, end_line) for each `## X` section.
    section_ranges: dict[str, tuple[int, int]] = {}
    section_starts: list[tuple[int, str]] = []
    for i, line in enumerate(lines):
        m = _SECTION_HEADER_RE.match(line.rstrip("\n"))
        if m:
            section_starts.append((i, m.group(1).upper()))
    for idx, (start, letter) in enumerate(section_starts):
        end = section_starts[idx + 1][0] if idx + 1 < len(section_starts) else len(lines)
        section_ranges[letter] = (start, end)

    new_link = _def_link(category_ko, post_title, permalink)

    for term in terms:
        eng = term["english"]
        kor = term["korean"]
        primary = term["primary"]
        eng_id = _slugify_id(eng)
        first = eng.lstrip()[:1].upper()
        if first < "A" or first > "Z":
            # Non-ASCII first letter — put in Z bucket so user can re-file.
            first = "Z"
        if first not in section_ranges:
            changes.append(f"skipped {eng!r}: no `## {first}` section in Index_ko.md")
            continue

        sec_start, sec_end = section_ranges[first]
        # Find an existing row whose English cell matches this term.
        # We compare by display text (case-insensitive, whitespace-collapsed)
        # because human-curated ids may contain typos like "axiom_of_power set".
        target_eng = eng.lower().strip()
        existing_idx: int | None = None
        for i in range(sec_start, sec_end):
            row = lines[i]
            if "<selected" not in row and "<unselected" not in row:
                continue
            row_eng = _english_in_row(row)
            if row_eng and row_eng == target_eng:
                existing_idx = i
                break
            m = _ROW_ID_RE.search(row)
            if m and m.group(1).strip().lower().replace(" ", "_") == eng_id.lower():
                existing_idx = i
                break

        if existing_idx is not None:
            row = lines[existing_idx]
            # Already references this exact permalink? leave it alone.
            if permalink in row:
                continue
            cells = row.split("|")
            # row layout: ['', ' eng_cell ', ' kor_cell ', ' def_cell ', ' ref_cell ', '\n']
            if len(cells) >= 5:
                def_cell = cells[3].strip()
                if def_cell:
                    def_cell = def_cell + "<br/>" + new_link
                else:
                    def_cell = new_link
                cells[3] = f" {def_cell} "
                new_row = "|".join(cells)
                if not new_row.endswith("\n"):
                    new_row += "\n"
                lines[existing_idx] = new_row
                changes.append(f"appended ref for {eng!r}: {permalink}")
                # ranges shift by 0 (in-place edit) — no rebuild needed.
            else:
                changes.append(f"skipped {eng!r}: malformed row at line {existing_idx + 1}")
            continue

        # New row: keep the section in lexicographic order by English term.
        # Comparison is case- and accent-insensitive (see `_sort_key`) so that
        # Čech, é-accented forms, etc. sort alongside their ASCII counterparts
        # instead of after every lowercase letter. Walk through rows in the
        # section and insert before the first row whose English cell sorts
        # strictly after our term.
        insert_at = sec_end
        while insert_at > sec_start and lines[insert_at - 1].strip() == "":
            insert_at -= 1  # land before trailing blank lines
        target_key = _sort_key(eng)
        for i in range(sec_start + 1, insert_at):
            row = lines[i]
            if "<selected" not in row and "<unselected" not in row:
                continue
            row_eng = _english_in_row(row)
            if row_eng and _sort_key(row_eng) > target_key:
                insert_at = i
                break
        new_row = _build_row(eng, kor, primary, new_link)
        if not new_row.endswith("\n"):
            new_row += "\n"
        lines.insert(insert_at, new_row)
        changes.append(f"inserted {eng!r} ({primary}-first) into ## {first}")
        # Rebuild section_ranges for sections after `first`.
        for letter, (s, e) in list(section_ranges.items()):
            if s >= insert_at:
                section_ranges[letter] = (s + 1, e + 1)
            elif e >= insert_at:
                section_ranges[letter] = (s, e + 1)

    return "".join(lines), changes


# ---------------------------------------------------------------------------
# Review file
# ---------------------------------------------------------------------------

def append_review(
    post_rel: str,
    post_title: str,
    permalink: str,
    ambiguous: list[dict[str, str]],
) -> None:
    if not ambiguous:
        return
    stamp = datetime.now(timezone.utc).isoformat(timespec="seconds")
    chunks: list[str] = []
    if not REVIEW_PATH.exists():
        chunks.append("# Term-extraction review\n\n")
        chunks.append("Items below were flagged as **ambiguous** (no `<sub>` partner).\n")
        chunks.append("Decide whether each one is a definition and edit `_pages/ko/Index_ko.md` accordingly.\n\n")
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
# Main
# ---------------------------------------------------------------------------

def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--dry-run", action="store_true")
    ap.add_argument("--file", help="process this specific post (skip state-based picker)")
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
        else:
            post = pick_next_post(state)
            if post is None:
                print("no posts need rescanning.")
                return 0

        rel = str(post.relative_to(BLOG_ROOT))
        text = post.read_text(encoding="utf-8")
        if is_unpublished(text):
            print(f"skipping {rel}: published: false")
            return 0
        fm = parse_frontmatter(text)
        cats = frontmatter_categories(text)
        permalink = fm.get("permalink", "")
        title = fm.get("title", post.stem)

        category_ko = None
        for c in cats:
            if c in CATEGORY_KO:
                category_ko = CATEGORY_KO[c]
                break
        if not category_ko:
            category_ko = (cats[0] if cats else "Math").split("/")[-1].strip()

        body = strip_frontmatter(text)
        definite, ambiguous = classify_definitions(body)

        print(f"scanning {rel}")
        print(f"  title: {title}")
        print(f"  permalink: {permalink}")
        print(f"  category(ko): {category_ko}")
        print(f"  definite: {len(definite)}, ambiguous: {len(ambiguous)}")

        if args.dry_run:
            for t in definite:
                print(f"  + {t['primary']}: {t['english']} / {t['korean']}")
            for a in ambiguous:
                print(f"  ? {a['term']} ({a['recommendation']})")
            return 0

        if definite:
            index_text = INDEX_PATH.read_text(encoding="utf-8")
            new_text, changes = upsert_terms(index_text, definite, category_ko, title, permalink)
            if new_text != index_text:
                orig_mode = INDEX_PATH.stat().st_mode
                tmp = INDEX_PATH.with_suffix(".tmp")
                tmp.write_text(new_text, encoding="utf-8")
                os.chmod(tmp, orig_mode)
                tmp.replace(INDEX_PATH)
            for c in changes:
                print(f"  * {c}")

        append_review(rel, title, permalink, ambiguous)

        state.setdefault("files", {})[rel] = post.stat().st_mtime
        save_state(state)

        return 0
    finally:
        release_lock()


if __name__ == "__main__":
    sys.exit(main())
