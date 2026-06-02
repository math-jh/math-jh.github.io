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
    state:  ~/math-jh.github.io/scripts/translation/translation_state.json
    log:    redirect cron stderr (e.g. translation.log)
    lock:   /tmp/translate-worker.lock

Cron suggestion:
    */30 * * * * cd /home/junhyeok/math-jh.github.io/scripts/translation \\
                 && /usr/bin/python3 translate_worker.py >>translation.log 2>&1
"""

from __future__ import annotations

import argparse
import difflib
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
# No-tools agent + empty MCP for the single-shot verify/audit call (see call_kimi).
VERIFY_AGENT_FILE     = str(SCRIPT_DIR / "verify-agent.yaml")
VERIFY_MCP_FILE       = str(SCRIPT_DIR / "verify-mcp.json")
KIMI_TIMEOUT_SEC      = 1500                 # 25min — large posts (>30KB) often need >15min
MAX_TRANSLATE_ATTEMPTS = 3                   # re-translate on LOSSY verify verdict, up to N tries
MIN_KO_BODY_CHARS     = 300                  # skip stubs below this
FAIL_RETRY_AFTER_SEC  = 24 * 3600
POLISH_INTERVAL_SEC   = 14 * 24 * 3600       # (unused) polish is now one-time; see Phase 3
GIT_DRIFT_MARGIN_SEC  = 60                   # (unused) drift is now opt-in via `drift_needed: true`
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


TRANSLATION_SOURCE_TAG = "kimi-cli"


_META_KEYS = ("translated_at", "translation_source", "last_polished_at")

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
    if not ko_fields:
        return {}
    prompt = _FM_FIELDS_PROMPT.format(
        ko_json=json.dumps(ko_fields, ensure_ascii=False, indent=2),
        keys=list(ko_fields.keys()),
    )
    out = call_kimi(prompt, thinking=False)
    out = _FENCE_RE.sub("", out).strip()
    try:
        data = json.loads(out)
    except json.JSONDecodeError as e:
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
    - new translated_at / translation_source / (optionally last_polished_at): appended
    """
    fm = ko_fm
    # Strip any existing translation meta to keep frontmatter idempotent.
    for k in _META_KEYS:
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

INSTRUCTIONS = """You translate the BODY of a Korean math blog post (Jekyll markdown) into natural, idiomatic English. The input is the body content only — frontmatter has already been stripped and is handled separately by a script. Output ONLY the translated body. No frontmatter, no `---` lines, no explanation, no code fences, no preamble.

Conversion rules for the body:

1. Math content: preserve every `$$...$$` block VERBATIM — same LaTeX, same count, same order, AND the SAME DELIMITER. A KO `$$...$$` display block MUST remain a `$$...$$` display block in EN; never downgrade a display block into inline `$...$`. Likewise keep inline `$...$` inline. Do not translate variable names or LaTeX commands.
   - WRONG: KO `... 사상 $$f\\colon X \\to Y$$ 가 주어지면 ...` → EN `... given a map $f\\colon X \\to Y$, ...` (display block collapsed into inline — FORBIDDEN).
   - RIGHT: EN `... given a map $$f\\colon X \\to Y$$, ...` (delimiter preserved).

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

4. HTML structure: preserve `<div class="...">`, translate `<ins>` labels:
   - `<ins id="def1">**정의 1**</ins>` → `<ins id="def1">**Definition 1**</ins>` (id and number N unchanged).
   - `<details class="proof"><summary>증명</summary>` → `<summary>Proof</summary>`.

5. Style: first-person plural ("we"); idiomatic, not literal grammar. "우리는 ~를 정의한다" → "we define ~".

6. Section headers: `## 정의` → `## Definition`. Use noun phrases.

7. Footnotes: `[^1]` markers preserved; footnote bodies translated.

8. References: `참고문헌` → `References`. BibTeX entries (author / journal / year / pages) unchanged.

# Self-check before responding (must all pass)

- Same number of `$$...$$` blocks as the KO body — count the `$$` markers: EN must have exactly as many `$$...$$` display blocks as KO, none silently downgraded to inline `$...$`, none added/dropped/split/merged.
- Every `<ins id="...">` from KO appears with the same id and same number N.
- No Korean labels remain (정의, 명제, 정리, 보조정리, 따름정리, 예시, 참고, 증명, 참고문헌).
- The body ends at the final content line — do not truncate mid-sentence.
- Output begins with the first body character (no leading `---` or blank lines).

Now translate the body below."""


def build_prompt(ko_body: str) -> str:
    return INSTRUCTIONS + "\n\n" + ko_body


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

1. **Math blocks `$$...$$`** — byte-for-byte: LaTeX commands, variable names, spacing, ordering, AND delimiter. The COUNT and ORDER of `$$...$$` display blocks MUST match the KO source exactly. NEVER downgrade a `$$...$$` display block into inline `$...$` (and never promote inline into display). Easiest rule: never touch what is inside `$$...$$`, and never change a `$$` delimiter into `$`.
2. **`<ins id="...">**Label N**</ins>` numbering** — every `<ins>` id (e.g. `def1`, `prop2`) and the integer N MUST appear with the same id and N, in the same order as in the KO source.
3. Cross-reference **paths** (`/en/math/...`) and **anchors** (`#def1`, `#prop2`) — unchanged. Visible labels may be lightly refined only if materially clearer.
   - **Verification rule**: do NOT change an anchor target or invent a new `[display](url)` pairing unless you have actually seen the target with that exact form. If unsure, leave the existing form untouched.
4. HTML structure — `<div class="...">`, `<ins id="...">**...**</ins>`, `<details class="proof"><summary>...</summary>`, `<sub>...</sub>` — keep exactly.
5. Section headers (`## ...`) — keep as-is unless genuinely wrong.
6. Footnote markers `[^N]` and identifiers — unchanged.
7. References / bibliography entries (BibTeX-style) — unchanged.

# Self-check before responding

- Same number of `$$...$$` blocks as the KO body — none downgraded to inline `$...$`.
- Every `<ins id="...">**Label N**</ins>` from KO present with identical id and N.
- No Korean labels remain (정의, 명제, 정리, 보조정리, 따름정리, 예시, 참고, 증명, 참고문헌).
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
            f"kimi CLI exited {proc.returncode}: "
            f"stderr={proc.stderr.strip()[:500]!r}"
        )
    out = proc.stdout
    if not out.strip():
        raise RuntimeError(f"kimi returned empty output; stderr={proc.stderr.strip()[:500]!r}")
    # Defensive: strip code fences if Kimi wrapped output
    out = _FENCE_RE.sub("", out).strip() + "\n"
    # Defensive: Kimi occasionally outputs `---title: ...` with no newline
    # after the opening triple-dash. _FRONTMATTER_RE (and the rest of the
    # pipeline) then silently no-ops, leaving the EN file with corrupt
    # frontmatter. Normalize here.
    if out.startswith("---") and len(out) > 3 and out[3] != "\n":
        out = "---\n" + out[3:]
    return out


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
      6. Validate the assembled output (math count, <ins> ids, label residue).
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
    if reason == "polish" and en_current_body.strip():
        prompt = build_polish_prompt(ko_body, en_current_body)
    else:
        prompt = build_prompt(ko_body)
    en_body = call_kimi(prompt)

    # ---- Step 3: body post-processing ----
    en_body, _n_fixed = label_fix(en_body)
    en_body = re.sub(r"<sub>[^<]*?</sub>", "", en_body)
    # Mechanical /ko/ → /en/ for any cross-refs the LLM forgot to convert.
    # Blanket substring replacement; the math blog body never has legitimate
    # `/ko/` in prose or code, so we don't need a guarded regex.
    en_body = en_body.replace("/ko/", "/en/")

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
        raise RuntimeError(f"validation failed: {err}")
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

# A KO/EN `$$`-count mismatch is almost always a `$$display$$`→`$inline$`
# downgrade (the LaTeX survives, only the delimiter changed) or a harmless
# merge/split — not lost content. We localize the real divergences mechanically
# and only ask Kimi about the few regions where math genuinely went missing.
#
# Key fact: the LaTeX inside `$$...$$` is identical in KO and EN (math isn't
# translated). So a KO block "survives" iff its whitespace-normalized LaTeX
# appears anywhere in EN's math — display OR inline. Blocks that pass that check
# are benign by construction (no model needed); only blocks whose content is
# absent from EN entirely are suspect, and Kimi sees just those `<ins>` regions
# — and is never told about `$$`/counts, so it can't loop on counting.

_DISPLAY_RE = re.compile(r"\$\$(.*?)\$\$", re.DOTALL)
_INS_RE     = re.compile(r'<ins id="([^"]+)"')
_INLINE_RE  = re.compile(r"\$([^$\n]+?)\$")
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


def _ins_anchors(text: str):
    """[(id, line_index), ...] for each `<ins id>`, in document order."""
    return [(m.group(1), text.count("\n", 0, m.start())) for m in _INS_RE.finditer(text)]


def _ins_regions(text: str) -> dict:
    """id -> region text (its `<ins>` line up to the next anchor). Text before
    the first anchor is filed under _PREAMBLE."""
    lines = text.split("\n")
    anchors = _ins_anchors(text)
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
    suspect_ids  — ordered `<ins>` ids (or _PREAMBLE) whose region holds a KO
                   block whose LaTeX is absent from EN entirely.

    `<ins>` anchors are the alignment unit because they survive the `$$`→`$`
    downgrade 1:1, whereas matched `$$` blocks go sparse exactly in the
    downgrade-heavy posts we care about (EN keeps ~20% of KO's `$$`), which
    misaligns any block-bracketed window."""
    ko_body, en_body = _SUB_STRIP_RE.sub("", ko), _SUB_STRIP_RE.sub("", en)
    ko_iter = list(_DISPLAY_RE.finditer(ko_body))
    ko_blocks = [_norm_math(m.group(1)) for m in ko_iter]
    ko_lines = [ko_body.count("\n", 0, m.start()) for m in ko_iter]
    en_blocks = [_norm_math(m.group(1)) for m in _DISPLAY_RE.finditer(en_body)]
    inventory = _en_math_inventory(en)

    sm = difflib.SequenceMatcher(None, ko_blocks, en_blocks, autojunk=False)
    missing = []
    for tag, i1, i2, _j1, _j2 in sm.get_opcodes():
        if tag in ("delete", "replace"):
            missing.extend(range(i1, i2))

    anchors = _ins_anchors(ko_body)

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

Set the overall VERDICT to lossy if ANY pair is LOSSY, otherwise safe.

Output (terse, no preamble, no closing remarks):

VERDICT: <safe | lossy>
FINDINGS:
- [pair N] <SAFE | LOSSY>: <one short sentence; for LOSSY, name exactly what meaning differs>
"""


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
      2. Semantic — only the `<ins>` regions holding a genuinely-absent KO block
         go to Kimi (no-tools agent), which judges meaning preservation WITHOUT
         being told anything about `$$`/counts. `<ins>` is the alignment unit
         because it survives the downgrade 1:1 (matched `$$` blocks go sparse in
         downgrade-heavy posts and misalign). Returns a terse VERDICT string;
         'verify-failed: …' on error.
    """
    benign, suspect_ids = _locate_divergences(ko_content, en_new)
    if not suspect_ids:
        return (f"VERDICT: safe\nCOUNTS: ko={ko_count} en={en_count}\n"
                f"- mechanical: all {benign} differing block(s) survive in EN as "
                f"inline/text (`$$`→`$` downgrade or rephrase); no content missing.")

    omitted = max(0, len(suspect_ids) - _VERIFY_MAX_REGIONS)
    ko_reg, en_reg = _ins_regions(ko_content), _ins_regions(en_new)
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

    MAX_ATTEMPTS = 3
    for attempt in range(1, MAX_ATTEMPTS + 1):
        try:
            # thinking OFF: thinking mode didn't suppress the model's tendency to
            # "think out loud" in the visible message on dense posts (and was
            # slower). We instead make correctness immune to it: _finalize_verdict
            # keeps only the model's LAST verdict, so any premature first-impression
            # verdict it emits before revising is ignored.
            out = call_kimi(prompt, thinking=False,
                            agent_file=VERIFY_AGENT_FILE,
                            mcp_config_file=VERIFY_MCP_FILE).strip()
            note = (f"\n(benign downgrades: {benign}; semantic-checked regions: "
                    f"{len(pairs)}" + (f"; {omitted} omitted" if omitted else "") + ")")
            return _finalize_verdict(out) + note
        except subprocess.TimeoutExpired:
            log(f"verify: kimi timeout {attempt}/{MAX_ATTEMPTS}"
                + (", retrying" if attempt < MAX_ATTEMPTS else ", giving up"))
            continue
        except Exception as e:
            return f"verify-failed: {e!r}"
    return f"verify-failed: kimi timeout after {MAX_ATTEMPTS} attempts"


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


def run_verify(state: dict, ko_path: Path, en_path: Path, key: str) -> int:
    """Read-only verification of an existing EN translation against KO.

    Deterministic LaTeX-corruption lints + the math-block semantic check (Kimi
    only when block counts genuinely diverge). Records the outcome in state and
    notifies on problems. NEVER modifies the EN file. Marks `verified_at` so the
    post is checked at most once.
    """
    ko_text = ko_path.read_text(encoding="utf-8")
    en_text = en_path.read_text(encoding="utf-8")
    ko_n = len(_MATH_BLOCK_RE.findall(_SUB_STRIP_RE.sub("", ko_text)))
    en_n = len(_MATH_BLOCK_RE.findall(_SUB_STRIP_RE.sub("", en_text)))
    lints = lint_latex(en_text)
    verdict_text = ""
    if ko_n != en_n:
        verdict_text = verify_math_mismatch(ko_text, en_text, ko_n, en_n)
    verdict_safe = bool(re.search(r"^VERDICT:\s*safe\b", verdict_text, re.M | re.I))
    clean = (not lints) and (ko_n == en_n or verdict_safe)

    entry = state["files"].get(key, {})
    entry["verified_at"] = datetime.now(timezone.utc).isoformat(timespec="seconds")
    entry["verify_math_counts"] = [ko_n, en_n]
    entry["verify_lints"] = lints[:20] or None
    if verdict_text:
        entry["verify_verdict"] = verdict_text[:4000]
    state["files"][key] = entry
    save_state(state)

    if clean:
        log(f"VERIFY ({key}): clean (math ko={ko_n} en={en_n})")
        return 0

    head = []
    if lints:
        head.append(f"{len(lints)} latex-lint")
    if verdict_text and not verdict_safe:
        head.append(verdict_text.splitlines()[0])
    log(f"VERIFY ({key}): FLAGGED \u2014 {'; '.join(head)}")
    for ln in lints:
        log(f"  LINT ({key}): {ln}")
    for ln in verdict_text.splitlines():
        log(f"  VERIFY ({key}): {ln}")
    body = ""
    if verdict_text and not verdict_safe:
        body += verdict_text + "\n"
    if lints:
        body += "LINTS:\n" + "\n".join(lints)
    _notify_telegram(f"translation verify flagged: {key}", body[:1500])
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

        if reason == "verify":
            return run_verify(state, ko_path, en_path, key)

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
                state["files"][key] = {
                    "status": "failed",
                    "last_attempt_ts": time.time(),
                    "error": f"timeout after {KIMI_TIMEOUT_SEC}s",
                }
                save_state(state)
                log(f"FAILED: timeout (attempt {attempt})")
                return 1
            except Exception as e:
                state["files"][key] = {
                    "status": "failed",
                    "last_attempt_ts": time.time(),
                    "error": str(e)[:500],
                }
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
            ko_n = len(_MATH_BLOCK_RE.findall(_SUB_STRIP_RE.sub("", ko_text)))
            en_n = len(_MATH_BLOCK_RE.findall(_SUB_STRIP_RE.sub("", translated)))
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
        if reason == "drift":
            clear_drift_flag(ko_path)   # consume the opt-in flag; don't re-drift
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
        if lossy_history:
            state["files"][key]["lossy_retry_count"] = len(lossy_history)
        if verdict_text:
            state["files"][key]["verify_verdict"] = verdict_text[:4000]

        if warnings:
            # Suppress telegram on VERDICT: safe — math-count mismatch is the only
            # current warning source, and "safe" means the divergence is rephrasing.
            # minor / lossy / verify-failed still notify.
            verdict_safe = bool(
                verdict_text
                and re.search(r"^VERDICT:\s*safe\b",
                              verdict_text, re.MULTILINE | re.IGNORECASE)
            )
            if verdict_safe:
                log(f"VERIFY ({key}): safe verdict — telegram suppressed")
            else:
                body_lines = [key, f"→ {en_path.relative_to(BLOG_ROOT)}", ""]
                body_lines += [f"• {w}" for w in warnings]
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
        return 0
    finally:
        release_lock()


if __name__ == "__main__":
    sys.exit(main())
