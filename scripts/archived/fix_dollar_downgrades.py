#!/usr/bin/env python3
"""Restore display-math delimiters in EN translations.

Some translations downgraded KO `$$...$$` display math to inline `$...$` in EN.
This blog's convention is that ALL body math uses `$$...$$` (single `$` breaks
the markdown parser on `_` etc.); single `$` is legitimate ONLY inside
`\\text{}` / `\\tag{}` (which live inside `$$`) and a few custom inline tags
(captions, glossary phrases, em-ko/em-en).

Fix, per EN post, purely mechanically (no model):
  - A single `$X$` is a downgrade iff its whitespace-normalized LaTeX matches a
    `$$X$$` block in the KO source (math is identical across languages), AND it
    is not inside a protected span.
  - Protected spans (never touched): `$$...$$` blocks and the custom inline tags
    in SKIP_TAGS, where single `$` is the intended convention.
  - Matching downgrades become `$$X$$` in place (inline position preserved;
    kramdown renders inline `$$...$$` inline).

Usage:
  python3 fix_dollar_downgrades.py            # dry-run: report + sample diffs
  python3 fix_dollar_downgrades.py --apply     # write the changes
"""
from __future__ import annotations

import argparse
import re
import sys

import translate_worker as tw

_DD   = re.compile(r"\$\$.*?\$\$", re.DOTALL)        # whole $$...$$ span
_DDc  = re.compile(r"\$\$(.*?)\$\$", re.DOTALL)      # capture its LaTeX
_SD   = re.compile(r"\$([^$\n]+?)\$")                # inline $...$
_norm = lambda s: re.sub(r"\s+", "", s)

# Custom inline contexts where single `$` is the intended convention — skip.
SKIP_TAGS = ("em-ko", "em-en", "phrase", "cap", "em")


def _protected_spans(text: str):
    spans = [(m.start(), m.end()) for m in _DD.finditer(text)]
    for tag in SKIP_TAGS:
        spans += [(m.start(), m.end())
                  for m in re.finditer(rf"<{tag}\b[^>]*>.*?</{tag}>", text, re.DOTALL)]
    return spans


def convert(text: str, ko_blocks: set) -> tuple[str, int]:
    """Return (converted_text, n_conversions). Protected spans are masked before
    matching so an inline `$...$` can never straddle a `$$` boundary."""
    masked = list(text)
    for a, b in _protected_spans(text):
        masked[a:b] = ["\x00"] * (b - a)
    masked = "".join(masked)

    repls = [(m.start(), m.end(), f"$${m.group(1)}$$")
             for m in _SD.finditer(masked) if _norm(m.group(1)) in ko_blocks]
    out = text
    for s, e, r in reversed(repls):            # right-to-left keeps offsets valid
        out = out[:s] + r + out[e:]

    # Invariant: each conversion adds exactly two `$` (`$X$` -> `$$X$$`) and
    # touches nothing else. (Don't assert global even-parity: a legit escaped
    # `\$` or lone `$` in prose makes the count odd independently of us.)
    assert out.count("$") == text.count("$") + 2 * len(repls), "unexpected $ delta"
    return out, len(repls)


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--apply", action="store_true", help="write changes (default: dry-run)")
    ap.add_argument("--samples", type=int, default=4, help="sample diff lines to print")
    args = ap.parse_args()

    total = 0
    touched = []
    for ko in sorted(tw.BLOG_ROOT.rglob("_posts/**/ko/*.md")):
        en = tw.find_en_counterpart(ko)
        if not en or not en.exists():
            continue
        et = en.read_text(encoding="utf-8")
        ko_blocks = {_norm(x) for x in _DDc.findall(tw._SUB_STRIP_RE.sub("", ko.read_text()))}
        new, n = convert(et, ko_blocks)
        if not n:
            continue
        total += n
        touched.append((n, en))
        if args.apply:
            en.write_text(new, encoding="utf-8")

    touched.sort(key=lambda t: -t[0])
    mode = "APPLIED" if args.apply else "DRY-RUN"
    print(f"[{mode}] {len(touched)} posts, {total} conversions")
    for n, en in touched:
        print(f"  {n:4d}  {en.relative_to(tw.BLOG_ROOT)}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
