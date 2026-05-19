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
KIMI_TIMEOUT_SEC      = 900                  # generous for thinking + long posts
MIN_KO_BODY_CHARS     = 300                  # skip stubs below this
FAIL_RETRY_AFTER_SEC  = 24 * 3600


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

def ko_to_en_path(ko_path: Path) -> Path:
    parts = list(ko_path.parts)
    parts[parts.index("ko")] = "en"
    return Path(*parts)


def _ko_body_length(ko_path: Path) -> int:
    """Length of the body after frontmatter — used to skip stubs."""
    text = ko_path.read_text(encoding="utf-8")
    m = re.match(r"^---\s*\n.*?\n---\s*\n", text, re.DOTALL)
    body = text[m.end():] if m else text
    return len(body.strip())


def find_next_target(state: dict) -> Optional[Tuple[Path, str]]:
    """Return (ko_path, reason) for next translation, or None."""
    ko_files = sorted(POSTS_ROOT.glob("*/ko/*.md"))
    pending, drift = [], []
    now = time.time()
    for ko in ko_files:
        key = str(ko.relative_to(BLOG_ROOT))
        entry = state["files"].get(key, {})

        # Skip recently-failed files (retry window)
        if entry.get("status") == "failed":
            if now - entry.get("last_attempt_ts", 0) < FAIL_RETRY_AFTER_SEC:
                continue

        # Skip empty / stub files
        if _ko_body_length(ko) < MIN_KO_BODY_CHARS:
            if entry.get("status") != "stub":
                state["files"][key] = {"status": "stub", "last_attempt_ts": now}
            continue

        en = ko_to_en_path(ko)
        if not en.exists():
            pending.append(ko)
        elif ko.stat().st_mtime > en.stat().st_mtime + 1:
            drift.append(ko)

    if pending:
        return pending[0], "pending"
    if drift:
        return drift[0], "drift"
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

Now translate the post below."""


def build_prompt(ko_content: str) -> str:
    return INSTRUCTIONS + "\n\n--- BEGIN POST ---\n" + ko_content + "\n--- END POST ---\n"


# ---------------------------------------------------------------------------
# Kimi invocation
# ---------------------------------------------------------------------------

_FENCE_RE = re.compile(r"^\s*```(?:markdown|md)?\s*\n|\n```\s*$", re.MULTILINE)


def call_kimi(prompt: str) -> str:
    """Invoke `kimi --quiet` with prompt on stdin, return final assistant message."""
    proc = subprocess.run(
        [KIMI_BIN, "--quiet", "--print", "--final-message-only"],
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


def translate(ko_path: Path) -> Tuple[str, int, int]:
    ko_content = ko_path.read_text(encoding="utf-8")
    prompt = build_prompt(ko_content)
    translated = call_kimi(prompt)
    return translated, len(prompt), len(translated)


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
    ko_path, reason = target
    en_path = ko_to_en_path(ko_path)
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
        ko_path, reason = target
        en_path = ko_to_en_path(ko_path)
        en_path.parent.mkdir(parents=True, exist_ok=True)
        key = str(ko_path.relative_to(BLOG_ROOT))
        log(f"translating ({reason}): {key} (ko {ko_path.stat().st_size}B)")

        try:
            translated, in_chars, out_chars = translate(ko_path)
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

        en_path.write_text(translated, encoding="utf-8")
        state["files"][key] = {
            "status": "done",
            "last_attempt_ts": time.time(),
            "en_path": str(en_path.relative_to(BLOG_ROOT)),
            "ko_mtime": ko_path.stat().st_mtime,
            "translated_at": datetime.now(timezone.utc).isoformat(timespec="seconds"),
            "in_chars": in_chars,
            "out_chars": out_chars,
            "reason": reason,
        }
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
