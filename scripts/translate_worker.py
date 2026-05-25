#!/usr/bin/env python3
"""
translate_worker.py — single-shot Kimi ko→en translation worker.

Designed for half-hourly cron. Picks ONE Korean blog post that needs translation
(missing en/ counterpart, or en/ exists but ko/ is newer = drift), sends it
to Kimi via the local `kimi` CLI (OAuth-authenticated), writes en/ counterpart.

Usage:
    python3 translate_worker.py            # run one translation, exit
    python3 translate_worker.py --status   # print stats only, no API call
    python3 translate_worker.py --dry-run  # show what would be translated

Files:
    state:  ~/math-jh.github.io/scripts/translation_state.json
    log:    redirect cron stderr (e.g. translation.log)
    lock:   /tmp/translate-worker.lock

Cron suggestion:
    */30 * * * * cd /home/junhyeok/math-jh.github.io/scripts \\
                 && /usr/bin/python3 translate_worker.py >>translation.log 2>&1
"""

from __future__ import annotations

import argparse
import json
import os
import re
import shutil
import subprocess
import sys
import time
from datetime import datetime, timezone
from pathlib import Path
from typing import Optional, Tuple

# ---------------------------------------------------------------------------
# Paths
# ---------------------------------------------------------------------------

BLOG_ROOT   = Path("/home/junhyeok/math-jh.github.io")
POSTS_ROOT  = BLOG_ROOT / "_posts" / "Math"
SCRIPT_DIR  = Path(__file__).resolve().parent
STATE_PATH  = SCRIPT_DIR / "translation_state.json"
LOCK_PATH   = Path("/tmp/translate-worker.lock")

# ---------------------------------------------------------------------------
# Kimi CLI
# ---------------------------------------------------------------------------

KIMI_BIN              = shutil.which("kimi") or str(Path.home() / ".local/bin/kimi")
KIMI_TIMEOUT_SEC      = 1500                 # 25min — large posts (>30KB) often need >15min
MIN_KO_BODY_CHARS     = 300                  # skip stubs below this
FAIL_RETRY_AFTER_SEC  = 24 * 3600
POLISH_INTERVAL_SEC   = 14 * 24 * 3600       # re-polish only if last polish > 14d ago
GIT_DRIFT_MARGIN_SEC  = 60                   # ignore drift within this window of translation time
TRUNCATION_RATIO      = 0.60                 # min output/reference body length; below → fail

# Local helper (label fix/audit)
sys.path.insert(0, str(SCRIPT_DIR))
from label_normalize import fix_text as label_fix, audit_text as label_audit  # noqa: E402


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

def load_state() -> dict:
    if STATE_PATH.exists():
        return json.loads(STATE_PATH.read_text(encoding="utf-8"))
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
    """True if frontmatter has `published: false`. Drafts are skipped."""
    for line in _read_frontmatter(ko_path).splitlines():
        s = line.strip()
        if s.startswith("published"):
            value = s.split(":", 1)[1].strip().strip('"').strip("'").lower()
            return value == "false"
    return False


TRANSLATION_SOURCE_TAG = "kimi-cli"


_META_KEYS = ("translated_at", "translation_source", "last_polished_at")


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
    """Three-phase priority: pending → drift → polish.

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

    # --- Phase 2: drift (git history says ko updated since our last translate) -
    for ko in ko_files:
        if is_draft(ko):
            continue
        existing_en = find_en_counterpart(ko)
        if existing_en is None:
            continue
        if not is_our_translation(existing_en):    # manual translation — leave alone
            continue
        ko_commit_ts = git_last_commit_ts(ko)
        if ko_commit_ts is None:
            continue
        translated_ts = _iso_to_ts(en_translation_meta(existing_en).get("translated_at", ""))
        if ko_commit_ts > translated_ts + GIT_DRIFT_MARGIN_SEC:
            return ko, existing_en, "drift"

    # --- Phase 3: polish (never-polished first, then oldest last_polished_at > 14d) ---
    polish_candidates = []
    for ko in ko_files:
        if is_draft(ko):
            continue
        existing_en = find_en_counterpart(ko)
        if existing_en is None:
            continue
        if not is_our_translation(existing_en):
            continue
        meta = en_translation_meta(existing_en)
        last_polished = _iso_to_ts(meta.get("last_polished_at", ""))
        if last_polished > 0 and now - last_polished < POLISH_INTERVAL_SEC:
            continue
        polish_candidates.append((last_polished, ko, existing_en))

    if polish_candidates:
        polish_candidates.sort()      # 0.0 (never polished) first, then oldest
        _, ko, en = polish_candidates[0]
        return ko, en, "polish"

    return None


# ---------------------------------------------------------------------------
# Prompt
# ---------------------------------------------------------------------------

INSTRUCTIONS = """You translate Korean math blog posts (Jekyll markdown) into natural, idiomatic English. Output ONLY the translated markdown — no explanation, no code fences, no preamble. Start at the opening `---` and end at the last content line.

Conversion rules:

1. Math content: preserve every `$$...$$` block VERBATIM. Do not translate variable names or LaTeX commands.

2. Frontmatter:
   - `title:` translate Korean to English (e.g. "가환군과 체" → "Abelian Groups and Fields")
   - `excerpt:` translate to natural English
   - `permalink:` replace `/ko/` with `/en/` (slug unchanged)
   - `sidebar.nav:` replace `"{cat}-ko"` with `"{cat}-en"`
   - `categories`, `header`, `date`, `last_modified_at`, `weight`, `published`: keep unchanged

3. Cross-reference links in body:
   - Path: `/ko/...` → `/en/...` (slug stays)
   - Visible label: translate Korean section title (e.g. `§아핀다양체` → `§Affine Varieties`)
   - Category bracket: `[\\[대수다양체\\] §..., ⁋정의 7]` → `[\\[Algebraic Varieties\\] §..., ⁋Definition 7]`
   - Labels: 정의→Definition, 명제→Proposition, 정리→Theorem, 보조정리→Lemma, 따름정리→Corollary, 예시→Example, 참고→Remark
   - Within-doc refs: `[정의 3](#def3)` → `[Definition 3](#def3)` (id unchanged)

4. Bilingual italic terms:
   - `*english<sub>한국어</sub>*` → `*english*` (drop Korean gloss)
   - `*한국어<sub>english</sub>*` → `*English*` (use English gloss as primary)

5. HTML structure: preserve `<div class="...">`, translate `<ins>` labels:
   - `<ins id="def1">**정의 1**</ins>` → `<ins id="def1">**Definition 1**</ins>` (id unchanged)
   - `<details class="proof"><summary>증명</summary>` → `<summary>Proof</summary>`

6. Style: first-person plural "우리는" → "we"; "살펴보았다" → "we saw / we studied"; "이번 글에서 우리는 ~를 정의한다" → "In this post we define ~". Idiomatic English, not literal grammar.

7. Section headers: `## 정의` → `## Definition`. Use noun phrases.

8. Footnotes: `[^1]` markers preserved; footnote bodies translated.

9. References: `참고문헌` → `References`. BibTeX entries (author / journal / year / pages) unchanged.

# Self-check before responding (must all pass)

- Same number of `$$...$$` blocks as the KO source — no math added, dropped, split, or merged
- Every `<ins id="...">` from KO appears with the same id and the same number N
- No `/ko/` paths remain in the body (all cross-ref paths use `/en/`)
- No Korean labels remain (정의, 명제, 정리, 보조정리, 따름정리, 예시, 참고, 증명, 참고문헌)
- Frontmatter has both opening and closing `---`, and the body ends at the final content line (do not truncate mid-sentence)

Now translate the post below."""


def build_prompt(ko_content: str) -> str:
    return INSTRUCTIONS + "\n\n--- BEGIN POST ---\n" + ko_content + "\n--- END POST ---\n"


POLISH_INSTRUCTIONS = """You are polishing an existing English translation of a Korean math blog post. Output ONLY the polished markdown — no explanation, no code fences, no preamble. Start at the opening `---` (frontmatter) and end at the last content line.

# Task

Given the Korean source (for meaning reference) and the current English translation, produce an *improved* English version. Refine prose quality. Preserve everything else exactly.

# What to improve

- Awkward translations or literal Korean grammar → idiomatic English
- Word choice → more precise mathematical or natural English
- Sentence flow → smoother connectives, less choppy
- Terminology consistency within the post and against standard mathematical English
- Fix translation drift: if the EN diverges from the KO meaning, restore fidelity

# What to preserve VERBATIM — mathematical fidelity is non-negotiable

1. **Math blocks `$$...$$`** — every character byte-for-byte: LaTeX commands, variable names, spacing, ordering. The COUNT and ORDER of math blocks in the output MUST match the Korean source exactly. Do not split, merge, reorder, add, or remove math blocks. Easiest rule: never touch what is inside `$$...$$`.
2. **`<ins id="...">**Label N**</ins>` numbering** — every `<ins>` id (e.g. `def1`, `prop2`, `thm3`) and the integer N inside MUST appear in the output with the same id, the same number, in the same order as in the source. Numbering drift breaks every cross-reference in the blog.
3. Frontmatter — every key, in the same order. Do not add or drop fields. `translated_at` and `last_polished_at` are injected automatically — do not write them yourself.
4. Cross-reference link **paths** `/en/math/...` and **anchors** (`#def1`, `#prop2`) — unchanged. Visible labels may be lightly refined only if materially clearer.
5. HTML structure — `<div class="...">`, `<ins id="...">**...**</ins>`, `<details class="proof"><summary>...</summary>`, `<sub>...</sub>` — keep exactly
6. Section headers (`## ...`) — keep as-is unless genuinely wrong
7. Footnote markers `[^N]` and identifiers — unchanged
8. References / bibliography entries (BibTeX-style) — unchanged

# Self-check before responding

Mentally verify:
- Same number of `$$...$$` blocks as the KO source? ✓
- Every `<ins id="...">**Label N**</ins>` from KO is present with identical id and N? ✓
- No `/ko/` paths remain in the body? ✓
- No Korean labels remain (정의, 명제, 정리, 보조정리, 따름정리, 예시, 참고, 증명, 참고문헌)? ✓
- Frontmatter starts with `---` and the closing `---` is present? ✓

# Style anchors

- First-person plural ("we ...") throughout
- Precise, technical, declarative; matches the user's canonical voice in other posts
- No "translator notes", no meta-commentary, no apologies
- Do not restructure paragraphs unless the original is broken

# Input format

You will receive:
- Korean source between `--- KO SOURCE ---` / `--- END KO SOURCE ---`
- Current English translation between `--- EN CURRENT ---` / `--- END EN CURRENT ---`

Output ONLY the polished English markdown."""


def build_polish_prompt(ko_content: str, en_content: str) -> str:
    # Strip our injected markers from en before passing — we re-inject post-call.
    en_clean = re.sub(r"^translated_at\s*:.*\n?",     "", en_content, flags=re.MULTILINE)
    en_clean = re.sub(r"^translation_source\s*:.*\n?", "", en_clean,   flags=re.MULTILINE)
    return (
        POLISH_INSTRUCTIONS
        + "\n\n--- KO SOURCE ---\n"   + ko_content + "\n--- END KO SOURCE ---\n"
        + "\n--- EN CURRENT ---\n"    + en_clean   + "\n--- END EN CURRENT ---\n"
    )


# ---------------------------------------------------------------------------
# Kimi invocation
# ---------------------------------------------------------------------------

_FENCE_RE     = re.compile(r"^\s*```(?:markdown|md)?\s*\n|\n```\s*$", re.MULTILINE)
_MATH_BLOCK_RE = re.compile(r"\$\$.*?\$\$", re.DOTALL)
_INS_ID_RE     = re.compile(r'<ins\s+id="([^"]+)"')
_KO_PATH_RE    = re.compile(r"/ko/[A-Za-z0-9_\-/]+")


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

    # Math block count: WARN ONLY. Strip <sub>...</sub> first (bilingual glosses
    # are dropped per translation rules, which legitimately reduces the count).
    # False positives (rephrasings that merge/split blocks) are common enough that
    # a hard fail wastes a whole day per file; we log + notify instead.
    _SUB_RE = re.compile(r"<sub>.*?</sub>", re.DOTALL)
    ko_math = len(_MATH_BLOCK_RE.findall(_SUB_RE.sub("", ko_content)))
    en_math = len(_MATH_BLOCK_RE.findall(_SUB_RE.sub("", translated)))
    if ko_math != en_math:
        warnings.append(f"math block count mismatch: ko={ko_math}, en={en_math}")

    # <ins id="..."> id set must match KO source exactly
    ko_ids = set(_INS_ID_RE.findall(ko_content))
    en_ids = set(_INS_ID_RE.findall(translated))
    if ko_ids != en_ids:
        missing = sorted(ko_ids - en_ids)
        extra   = sorted(en_ids - ko_ids)
        return f"<ins id> mismatch: missing={missing} extra={extra}"

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

    # Frontmatter keys: ko ⊆ en (en may add translated_at / translation_source / last_polished_at)
    ko_keys = _fm_top_keys(ko_content)
    en_keys = _fm_top_keys(translated)
    missing_keys = ko_keys - en_keys
    if missing_keys:
        return f"frontmatter keys dropped: {sorted(missing_keys)}"

    return None


def call_kimi(prompt: str, *, thinking: bool = False) -> str:
    """Invoke `kimi --quiet` with prompt on stdin, return final assistant message.

    Thinking is OFF by default — it shares the 32K output-token budget with the
    actual response, and on large posts (e.g. Modules.md 2026-05-25) the model
    can burn the entire budget on internal reasoning and then truncate the
    visible output. Callers that need analytical depth (e.g. verify) opt in.
    """
    args = [KIMI_BIN, "--quiet", "--print", "--final-message-only",
            "--thinking" if thinking else "--no-thinking"]
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
            f"kimi CLI exited {proc.returncode}: "
            f"stderr={proc.stderr.strip()[:500]!r}"
        )
    out = proc.stdout
    if not out.strip():
        raise RuntimeError(f"kimi returned empty output; stderr={proc.stderr.strip()[:500]!r}")
    # Defensive: strip code fences if Kimi wrapped output
    out = _FENCE_RE.sub("", out).strip() + "\n"
    return out


def translate(
    ko_path: Path,
    translated_at_iso: str,
    *,
    reason: str,
    en_path: Optional[Path] = None,
    warnings: Optional[list] = None,
) -> Tuple[str, int, int]:
    ko_content = ko_path.read_text(encoding="utf-8")
    en_current: Optional[str] = None
    if reason == "polish" and en_path is not None and en_path.exists():
        en_current = en_path.read_text(encoding="utf-8")
        prompt = build_polish_prompt(ko_content, en_current)
    else:                                       # pending or drift → re-translate from scratch
        prompt = build_prompt(ko_content)

    translated = call_kimi(prompt)
    # Mechanical KO-label cleanup before any validation / metadata injection.
    translated, _n_fixed = label_fix(translated)
    # Strip residual bilingual `<sub>...</sub>` glosses. The translation rule
    # already drops/replaces them, but Kimi occasionally leaves them behind
    # (esp. `<sub>한국어</sub>`). No legitimate <sub> use exists in this blog
    # (math uses LaTeX subscripts), so blanket-stripping is safe.
    translated = re.sub(r"<sub>[^<]*?</sub>", "", translated)

    err = validate_translation(
        translated, ko_content=ko_content, reason=reason, en_current=en_current,
        warnings=warnings,
    )
    if err:
        raise RuntimeError(f"validation failed: {err}")

    polished = translated_at_iso if reason == "polish" else None
    translated = inject_translation_metadata(
        translated, translated_at_iso, polished_at_iso=polished,
    )
    return translated, len(prompt), len(translated)


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


# ---------------------------------------------------------------------------
# Math-mismatch verification (Kimi second opinion)
# ---------------------------------------------------------------------------

_SUB_STRIP_RE = re.compile(r"<sub>.*?</sub>", re.DOTALL)

VERIFY_INSTRUCTIONS_FRESH = """You audit a Korean→English math blog translation for content fidelity.

The validator flagged that the COUNT of `$$...$$` math blocks differs between KO and EN. Your job is to decide whether any actual mathematical content was lost, altered, or added, OR whether the difference is just a rephrasing that merges/splits blocks while preserving meaning.

Method:
1. Walk both versions in parallel, anchoring by `<ins id="...">` labels.
2. For each anchor region where the math-block count differs, identify the specific block(s) involved.
3. Classify each difference:
   - SAFE-REPHRASE: blocks merged/split or variable inlined, no math content lost (e.g. KO `$$A$$ + $$S$$` → EN `$$S \\subseteq A$$`).
   - LOSSY: a mathematical statement, hypothesis, conclusion, or symbol that carries meaning was dropped, or content was added that does not exist in KO.
   - QUESTIONABLE: cannot tell from surrounding context alone.

Output format (strict, terse, no preamble, no closing remarks):

VERDICT: <safe | minor | lossy>
COUNTS: ko=<N> en=<M>
FINDINGS:
- [<anchor or section>] <SAFE-REPHRASE | LOSSY | QUESTIONABLE>: <one short sentence on what changed>
- ...
(Limit to at most 8 findings. If more, summarize the rest in one closing bullet.)
"""

VERIFY_INSTRUCTIONS_POLISH = """You audit a polish pass on an English translation of a Korean math blog post for content fidelity.

Three inputs:
- KO SOURCE: the Korean original (ground truth for mathematical content).
- EN OLD: the previous English translation, already validated — treat as the trusted baseline.
- EN NEW: the polished output. The validator flagged that EN NEW's `$$...$$` block count diverges from KO.

Since EN OLD was previously validated against KO, the most likely cause of the new mismatch is that POLISH changed something. Focus your analysis on EN OLD → EN NEW: what did polish add, drop, merge, or split that produced the divergence?

Method:
1. Walk EN OLD and EN NEW in parallel, anchoring by `<ins id="...">` labels.
2. For each anchor region where math-block count or content differs, identify the specific block(s) polish modified.
3. Cross-check against KO to judge whether the change preserves meaning.
4. Classify each difference:
   - SAFE-REPHRASE: polish merged/split blocks or inlined a variable, no math content lost vs KO.
   - LOSSY: polish dropped a hypothesis/conclusion/symbol that exists in KO, or introduced something not in KO.
   - QUESTIONABLE: cannot tell from surrounding context alone.

Output format (strict, terse, no preamble, no closing remarks):

VERDICT: <safe | minor | lossy>
COUNTS: ko=<N> en_old=<O> en_new=<M>
POLISH CHANGED:
- [<anchor>] <SAFE-REPHRASE | LOSSY | QUESTIONABLE>: <what polish did, one short sentence>
- ...
(Limit to at most 8 findings. If more, summarize the rest in one closing bullet.)
"""


def build_verify_prompt(
    ko_content: str, en_new: str, ko_count: int, en_count: int,
    *, en_old: Optional[str] = None,
) -> str:
    if en_old is not None:
        en_old_n = len(_MATH_BLOCK_RE.findall(_SUB_STRIP_RE.sub("", en_old)))
        return (
            VERIFY_INSTRUCTIONS_POLISH
            + f"\n\nFlagged counts: ko={ko_count}, en_old={en_old_n}, en_new={en_count}\n"
            + "\n--- KO SOURCE ---\n"   + ko_content + "\n--- END KO SOURCE ---\n"
            + "\n--- EN OLD ---\n"      + en_old     + "\n--- END EN OLD ---\n"
            + "\n--- EN NEW ---\n"      + en_new     + "\n--- END EN NEW ---\n"
        )
    return (
        VERIFY_INSTRUCTIONS_FRESH
        + f"\n\nFlagged counts: ko={ko_count}, en={en_count}\n"
        + "\n--- KO SOURCE ---\n"  + ko_content + "\n--- END KO SOURCE ---\n"
        + "\n--- EN TRANSLATION ---\n" + en_new + "\n--- END EN TRANSLATION ---\n"
    )


def verify_math_mismatch(
    ko_content: str, en_new: str, ko_count: int, en_count: int,
    *, en_old: Optional[str] = None,
) -> str:
    """Run a separate Kimi call to diagnose a math-count mismatch.

    For polish, pass `en_old` (the pre-polish EN content) so the model can focus
    on what polish changed rather than re-deriving the whole KO↔EN alignment.

    Returns the assistant's terse verdict text. On failure, returns a short
    error string starting with 'verify-failed:' so caller can still notify.
    """
    prompt = build_verify_prompt(ko_content, en_new, ko_count, en_count, en_old=en_old)
    # Thinking OFF: with 400+ math blocks the model burns the 32K output budget on
    # internal reasoning and times out before producing the verdict (observed
    # 2026-05-25 on Characteristic_Classes, Cohomology_of_Projective_Spaces,
    # Riemann_Roch_Theorem). The verdict format is short bullet list — no
    # reasoning depth needed; the model can still classify SAFE/LOSSY from prose.
    try:
        return call_kimi(prompt, thinking=False).strip()
    except subprocess.TimeoutExpired:
        return "verify-failed: kimi timeout"
    except Exception as e:
        return f"verify-failed: {e!r}"


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


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------

def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__.split("\n\n")[0])
    ap.add_argument("--status",  action="store_true", help="print stats and exit")
    ap.add_argument("--dry-run", action="store_true", help="show next target without translating")
    args = ap.parse_args()

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

    try:
        target = find_next_target(state)
        if target is None:
            log("nothing pending")
            save_state(state)                # may have updated stub markers
            return 0
        ko_path, en_path, reason = target
        en_path.parent.mkdir(parents=True, exist_ok=True)
        key = str(ko_path.relative_to(BLOG_ROOT))
        log(f"translating ({reason}): {key} → {en_path.relative_to(BLOG_ROOT)} (ko {ko_path.stat().st_size}B)")

        translated_at = datetime.now(timezone.utc).isoformat(timespec="seconds")
        warnings: list = []
        try:
            translated, in_chars, out_chars = translate(
                ko_path, translated_at, reason=reason, en_path=en_path,
                warnings=warnings,
            )
        except subprocess.TimeoutExpired:
            state["files"][key] = {
                "status": "failed",
                "last_attempt_ts": time.time(),
                "error": f"timeout after {KIMI_TIMEOUT_SEC}s",
            }
            save_state(state)
            log(f"FAILED: timeout")
            return 1
        except Exception as e:
            state["files"][key] = {
                "status": "failed",
                "last_attempt_ts": time.time(),
                "error": str(e)[:500],
            }
            save_state(state)
            log(f"FAILED: {e!r}")
            return 1

        # Snapshot pre-polish EN before overwrite — verify needs it for old→new diff.
        en_old_snapshot: Optional[str] = None
        if reason == "polish" and en_path.exists():
            en_old_snapshot = en_path.read_text(encoding="utf-8")
        en_path.write_text(translated, encoding="utf-8")
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
        if warnings:
            for w in warnings:
                log(f"WARN ({key}): {w}")
            # If the math-block count mismatch is the warning, run a Kimi second
            # opinion to diagnose what changed before notifying — the raw count is
            # rarely actionable on its own (most mismatches are safe rephrasings).
            math_warn = next(
                (w for w in warnings if w.startswith("math block count mismatch")),
                None,
            )
            verdict_text = ""
            if math_warn:
                ko_text = ko_path.read_text(encoding="utf-8")
                # Reuse the same SUB-strip the validator used so counts agree.
                ko_n = len(_MATH_BLOCK_RE.findall(_SUB_STRIP_RE.sub("", ko_text)))
                en_n = len(_MATH_BLOCK_RE.findall(_SUB_STRIP_RE.sub("", translated)))
                log(f"VERIFY ({key}): running kimi diagnosis for math mismatch ko={ko_n}/en={en_n}"
                    + (" (with en_old)" if en_old_snapshot else ""))
                verdict_text = verify_math_mismatch(
                    ko_text, translated, ko_n, en_n, en_old=en_old_snapshot,
                )
                for line in verdict_text.splitlines():
                    log(f"VERIFY ({key}): {line}")
                state["files"][key]["verify_verdict"] = verdict_text[:4000]
            body_lines = [key, f"→ {en_path.relative_to(BLOG_ROOT)}", ""]
            body_lines += [f"• {w}" for w in warnings]
            if verdict_text:
                body_lines += ["", "--- kimi verify ---", verdict_text]
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
        return 0
    finally:
        release_lock()


if __name__ == "__main__":
    sys.exit(main())
