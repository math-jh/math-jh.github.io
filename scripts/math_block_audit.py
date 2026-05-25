#!/usr/bin/env python3
"""Anchor-segmented multiset diff of $$...$$ math blocks between ko/en pairs.

Reports, per <ins id> region, which blocks appear in KO but not EN (likely losses)
and which appear in EN but not KO (likely added). Lines starting with KO blocks
that the polish call dropped are the actionable items.
"""
from __future__ import annotations
import re, sys
from collections import Counter
from pathlib import Path

BLOG = Path("/home/junhyeok/math-jh.github.io")
SUB = re.compile(r"<sub>.*?</sub>", re.DOTALL)
MATH = re.compile(r"\$\$.*?\$\$", re.DOTALL)
INS = re.compile(r'<ins\s+id="([^"]+)"')


def segments(text: str) -> list[tuple[str, str]]:
    """Split text by <ins id="..."> anchors. Returns [(anchor, chunk), ...]."""
    text = SUB.sub("", text)
    parts = []
    last = 0
    cur = "(preamble)"
    for m in INS.finditer(text):
        parts.append((cur, text[last:m.start()]))
        cur = m.group(1)
        last = m.start()
    parts.append((cur, text[last:]))
    return parts


def audit(ko_path: Path, en_path: Path) -> None:
    ko_segs = segments(ko_path.read_text(encoding="utf-8"))
    en_segs = segments(en_path.read_text(encoding="utf-8"))
    ko_by_anchor = {a: c for a, c in ko_segs}
    en_by_anchor = {a: c for a, c in en_segs}
    anchors = []
    seen = set()
    for a, _ in ko_segs + en_segs:
        if a not in seen:
            anchors.append(a)
            seen.add(a)

    ko_total = sum(len(MATH.findall(c)) for c in ko_by_anchor.values())
    en_total = sum(len(MATH.findall(c)) for c in en_by_anchor.values())
    print(f"=== {ko_path.name}  ko={ko_total} en={en_total} (delta={en_total-ko_total:+d}) ===")

    for a in anchors:
        ko_chunk = ko_by_anchor.get(a, "")
        en_chunk = en_by_anchor.get(a, "")
        ko_blocks = Counter(MATH.findall(ko_chunk))
        en_blocks = Counter(MATH.findall(en_chunk))
        if ko_blocks == en_blocks:
            continue
        ko_only = ko_blocks - en_blocks
        en_only = en_blocks - ko_blocks
        if not ko_only and not en_only:
            continue
        nk = sum(ko_blocks.values()); ne = sum(en_blocks.values())
        print(f"  [{a}] ko={nk} en={ne}")
        for b, n in sorted(ko_only.items()):
            sn = f" x{n}" if n > 1 else ""
            print(f"    KO-only{sn}: {b[:120]}")
        for b, n in sorted(en_only.items()):
            sn = f" x{n}" if n > 1 else ""
            print(f"    EN-only{sn}: {b[:120]}")
    print()


PAIRS = [
    ("Algebraic_Structures/ko/2021-09-02-Algebraic_Structures.md",
     "Algebraic_Structures/en/2026-03-11-Algebraic_Structures.md"),
    ("Algebraic_Structures/ko/2021-09-04-Grothendieck_Groups.md",
     "Algebraic_Structures/en/2026-03-11-Grothendieck_Groups.md"),
    ("Algebraic_Varieties/ko/2026-03-29-Canonical_Bundle.md",
     "Algebraic_Varieties/en/2026-03-29-Canonical_Bundle.md"),
    ("Algebraic_Structures/ko/2022-11-29-Groups.md",
     "Algebraic_Structures/en/2026-03-11-Groups.md"),
    ("Algebraic_Structures/ko/2022-11-30-Isomorphism_Theorems.md",
     "Algebraic_Structures/en/2026-03-11-Isomorphism_Theorems.md"),
    ("Toric_Geometry/ko/2026-05-17-Toric_Varieties.md",
     "Toric_Geometry/en/2026-05-17-Toric_Varieties.md"),
    ("Algebraic_Structures/ko/2022-12-01-Rings.md",
     "Algebraic_Structures/en/2026-03-11-Rings.md"),
    ("Algebraic_Structures/ko/2022-12-07-Free_Products.md",
     "Algebraic_Structures/en/2026-03-11-Free_Products.md"),
    ("Scheme_Theory/ko/2026-05-07-Algebra_of_Schemes.md",
     "Scheme_Theory/en/2026-05-07-Algebra_of_Schemes.md"),
    ("Algebraic_Structures/ko/2023-01-09-Restricted_Sums.md",
     "Algebraic_Structures/en/2026-03-11-Restricted_Sums.md"),
    ("Algebraic_Structures/ko/2023-02-14-Group_Actions.md",
     "Algebraic_Structures/en/2026-03-11-Group_Actions.md"),
    ("Algebraic_Structures/ko/2024-05-05-Quotient_Rings.md",
     "Algebraic_Structures/en/2026-03-11-Quotient_Rings.md"),
    ("Algebraic_Structures/ko/2024-05-08-Field_of_Fractions.md",
     "Algebraic_Structures/en/2026-03-11-Field_of_Fractions.md"),
    ("Algebraic_Structures/ko/2024-05-10-Modules.md",
     "Algebraic_Structures/en/2026-03-11-Modules.md"),
    ("Algebraic_Structures/ko/2024-05-12-Operations_of_Modules.md",
     "Algebraic_Structures/en/2026-03-11-Operations_of_Modules.md"),
    ("Algebraic_Structures/ko/2024-07-04-Abelian_Groups.md",
     "Algebraic_Structures/en/2026-03-11-Abelian_Groups.md"),
    ("Algebraic_Structures/ko/2024-08-11-Graded_Rings.md",
     "Algebraic_Structures/en/2026-03-11-Graded_Rings.md"),
    ("Algebraic_Structures/ko/2024-08-12-Graded_Modules.md",
     "Algebraic_Structures/en/2026-03-11-Graded_Modules.md"),
    ("Algebraic_Structures/ko/2024-08-30-Algebras.md",
     "Algebraic_Structures/en/2024-08-30-Algebras.md"),
]

if __name__ == "__main__":
    for ko_rel, en_rel in PAIRS:
        ko = BLOG / "_posts/Math" / ko_rel
        en = BLOG / "_posts/Math" / en_rel
        if not ko.exists():
            print(f"MISSING ko: {ko}"); continue
        if not en.exists():
            print(f"MISSING en: {en}"); continue
        audit(ko, en)
