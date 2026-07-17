#!/usr/bin/env python3
"""
Reader/inspector for link-overrides.log.

The Jekyll plugin (`_plugins/link_normalizer.rb`) classifies each override
into one of three buckets at build time and writes the bucket inline. This
script just summarizes / filters / samples that file.

Buckets:
  cosmetic       — plugin enriches author's text with parenthetical from
                   target label (source markdown is fine as-is)
  title-drift    — target page title / category name / section name
                   changed; source displays stale text (worth fixing)
  anchor-dropped — target anchor no longer exists; `, ⁋Label N` tail
                   stripped (source has broken anchor — worth fixing)

Usage:
    python3 scripts/audit/triage_overrides.py
    python3 scripts/audit/triage_overrides.py --bucket title-drift --show 20
    python3 scripts/audit/triage_overrides.py --by-source --bucket anchor-dropped
"""
from __future__ import annotations
import argparse
import json
import sys
from collections import Counter, defaultdict
from pathlib import Path

LOG = Path(__file__).resolve().parent / "link-overrides.log"
BUCKETS = (
    "cosmetic/label-enrich",
    "cosmetic/label-trim",
    "cosmetic/same-cat-omit",
    "title-drift/section-renamed",
    "title-drift/category-renamed",
    "title-drift/label-renamed",
    "title-drift/footnote-stripped",
    "anchor-dropped",
)


def load():
    summary = None
    by_bucket: dict[str, list[dict]] = defaultdict(list)
    if not LOG.exists():
        print(f"log not found: {LOG} — run a Jekyll build first", file=sys.stderr)
        sys.exit(1)
    for line in LOG.read_text().splitlines():
        if not line.strip():
            continue
        try:
            d = json.loads(line)
        except json.JSONDecodeError:
            continue
        if d.get("summary"):
            summary = d
            continue
        by_bucket[d.get("bucket", "?")].append(d)
    return summary, by_bucket


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--bucket", choices=BUCKETS)
    ap.add_argument("--show", type=int, default=0, help="Print N examples per bucket")
    ap.add_argument("--by-source", action="store_true", help="Group by source file")
    args = ap.parse_args()

    summary, by_bucket = load()

    if summary:
        total = summary["total"]
        print(f"Total overrides: {total}")
        for k in BUCKETS:
            n = summary.get(k, 0)
            pct = (n / total * 100) if total else 0
            print(f"  {k:15s} {n:5d}  ({pct:5.1f}%)")
    else:
        total = sum(len(v) for v in by_bucket.values())
        print(f"Total overrides: {total}  (no summary line — old log?)")
        for k in BUCKETS:
            print(f"  {k:15s} {len(by_bucket.get(k, [])):5d}")
    print()

    if args.by_source:
        target = [args.bucket] if args.bucket else list(BUCKETS)
        for k in target:
            entries = by_bucket.get(k, [])
            if not entries:
                continue
            print(f"--- {k} by source (top 30) ---")
            cnt = Counter(d["source"] for d in entries)
            for src, n in cnt.most_common(30):
                print(f"  {n:4d}  {src}")
            print()
        return

    targets = [args.bucket] if args.bucket else list(BUCKETS)
    for k in targets:
        if args.show and by_bucket.get(k):
            print(f"--- {k} (first {args.show}) ---")
            for d in by_bucket[k][: args.show]:
                print(f"  {d['source']}")
                print(f"    url:       {d['url']}")
                print(f"    original:  {d['original']}")
                print(f"    canonical: {d['canonical']}")
            print()


if __name__ == "__main__":
    main()
