#!/usr/bin/env python3
"""label_normalize.py — fix or audit Korean math labels in translated EN posts.

Two modes:
    --mode=fix    rewrite recognized labels in place (post-translate cleanup)
    --mode=audit  scan for residual KO labels; exit non-zero if any are found

Used by translate_worker.py:
    * fix mode runs after every Kimi translation (pending/drift/polish)
    * audit mode runs as a final validation gate before writing to disk

Only structurally-anchored matches are touched (bold marker, section header,
cross-ref symbol, <summary> tag) — that avoids damaging real math terms whose
spelling happens to contain a label substring (e.g. "정의역" = "domain").
"""

from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path

# Longest-first so 보조정리 wins over 정리, 참고문헌 wins over 참고.
LABEL_MAP = [
    ("보조정리", "Lemma"),
    ("따름정리", "Corollary"),
    ("참고문헌", "References"),
    ("정의",     "Definition"),
    ("명제",     "Proposition"),
    ("정리",     "Theorem"),
    ("예시",     "Example"),
    ("참고",     "Remark"),
    ("증명",     "Proof"),
]
ENG = dict(LABEL_MAP)
_LABELS_RE = "|".join(re.escape(k) for k, _ in LABEL_MAP)

# Each pattern captures (label) plus surrounding context; replacement
# preserves context and substitutes the English equivalent.
_PATTERNS = [
    # **Label N** / **Label**
    (re.compile(rf"\*\*({_LABELS_RE})(\s*\d*)\*\*"),
     lambda m: f"**{ENG[m.group(1)]}{m.group(2)}**"),
    # §Label  (cross-ref section marker)
    (re.compile(rf"§({_LABELS_RE})"),
     lambda m: f"§{ENG[m.group(1)]}"),
    # ⁋Label N  (cross-ref paragraph marker)
    (re.compile(rf"⁋({_LABELS_RE})(\s*\d*)"),
     lambda m: f"⁋{ENG[m.group(1)]}{m.group(2)}"),
    # Markdown header line: "## Label" / "### Label N"
    (re.compile(rf"^(#{{1,6}}\s+)({_LABELS_RE})(\s*\d*\s*)$", re.MULTILINE),
     lambda m: f"{m.group(1)}{ENG[m.group(2)]}{m.group(3)}"),
    # <summary>Label</summary>
    (re.compile(rf"<summary>({_LABELS_RE})</summary>"),
     lambda m: f"<summary>{ENG[m.group(1)]}</summary>"),
]


def fix_text(text: str) -> tuple[str, int]:
    """Return (new_text, n_replacements)."""
    total = 0
    for regex, repl in _PATTERNS:
        text, n = regex.subn(repl, text)
        total += n
    return text, total


def audit_text(text: str) -> list[str]:
    """Return list of issue descriptions; empty list means clean."""
    issues: list[str] = []
    for regex, _ in _PATTERNS:
        for m in regex.finditer(text):
            line_no = text.count("\n", 0, m.start()) + 1
            issues.append(f"line {line_no}: residual KO label {m.group(0)!r}")
    return issues


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__.split("\n\n")[0])
    ap.add_argument("--mode", choices=["fix", "audit"], required=True)
    ap.add_argument("files", nargs="+", type=Path)
    args = ap.parse_args()

    fail_count = 0
    for path in args.files:
        text = path.read_text(encoding="utf-8")
        if args.mode == "fix":
            new, n = fix_text(text)
            if n:
                path.write_text(new, encoding="utf-8")
                print(f"FIXED ({n} replacements): {path}", file=sys.stderr)
        else:
            issues = audit_text(text)
            if issues:
                fail_count += 1
                print(f"AUDIT FAIL: {path}", file=sys.stderr)
                for issue in issues[:20]:
                    print(f"  {issue}", file=sys.stderr)
    return 1 if fail_count else 0


if __name__ == "__main__":
    sys.exit(main())
