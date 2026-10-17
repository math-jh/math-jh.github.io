#!/usr/bin/env python3
"""Distributions of the signal pilot: what the Step 1 answers look like, and
which signals go with a non-unanimous vote.  Read-only over the pilot files."""
from __future__ import annotations

import json
from collections import Counter, defaultdict
from pathlib import Path

RUNS = ("S1a", "S1b", "S2", "S3")
VOTERS = ("S1a", "S2", "S3")


def _pct(a: int, b: int) -> str:
    return f"{a}/{b} ({100 * a / b:.0f}%)" if b else "0/0"


def load(pilot_dir: Path) -> list[dict]:
    """One row per link: the four runs' answers and the link's features."""
    out = []
    for path in sorted(pilot_dir.glob("*.json")):
        record = json.loads(path.read_text(encoding="utf-8"))
        for call in record.get("calls", []):
            runs = call.get("runs", {})
            for lid, features in call.get("features", {}).items():
                out.append({"lid": lid, "unit": record["unit"], "source": call["source"],
                            "features": features,
                            "runs": {name: runs[name][lid] for name in RUNS
                                     if name in runs and lid in runs[name]}})
    return out


def usage_table(pilot_dir: Path) -> list[str]:
    acc: dict[str, list[dict]] = defaultdict(list)
    for path in sorted(pilot_dir.glob("*.json")):
        record = json.loads(path.read_text(encoding="utf-8"))
        for call in record.get("calls", []):
            for name, usages in call.get("usage", {}).items():
                acc[name].extend(usages)
    lines = ["| run | calls | items | avg input tok | avg output tok | output tok/item |",
             "|---|---|---|---|---|---|"]
    for name in RUNS:
        rows = acc.get(name, [])
        if not rows:
            continue
        items = sum(r.get("items", 0) for r in rows)

        def tok(r, *keys):
            return sum(int(r.get(k) or 0) for k in keys)
        inp = sum(tok(r, "input_tokens", "cache_creation_input_tokens",
                      "cache_read_input_tokens", "cached_input_tokens") for r in rows)
        outp = sum(tok(r, "output_tokens") for r in rows)
        lines.append(f"| {name} | {len(rows)} | {items} | {inp // len(rows)} | "
                     f"{outp // len(rows)} | {outp / max(items, 1):.0f} |")
    return lines


def render(pilot_dir: Path) -> str:
    links = load(pilot_dir)
    lines = [f"links: {len(links)}"]
    complete = [x for x in links if all(v in x["runs"] for v in VOTERS)]
    lines.append(f"links with all three votes: {len(complete)}")

    lines.append("\n## per run")
    for name in RUNS:
        rows = [x["runs"][name] for x in links if name in x["runs"]]
        if not rows:
            continue
        rel = Counter(r["relation"] for r in rows)
        basis = Counter(r["basis"] for r in rows)
        bnd = sum(1 for r in rows if r["boundary"])
        inc = sum(1 for r in rows if r["inconsistent"])
        q = Counter("1.0" if r["quote_score"] >= 1 else ">=.9" if r["quote_score"] >= .9
                    else ">=.8" if r["quote_score"] >= .8 else "<.8" for r in rows)
        lines.append(f"- {name}: n={len(rows)} relation={dict(rel)} basis={dict(basis)} "
                     f"boundary={_pct(bnd, len(rows))} inconsistent={_pct(inc, len(rows))} "
                     f"quote={dict(q)}")

    pair = [x for x in links if "S1a" in x["runs"] and "S1b" in x["runs"]]
    if pair:
        same_rel = sum(1 for x in pair if x["runs"]["S1a"]["relation"] == x["runs"]["S1b"]["relation"])
        keys = ("preview", "need", "need_kind", "provided", "relation")
        same_all = sum(1 for x in pair if all(x["runs"]["S1a"][k] == x["runs"]["S1b"][k] for k in keys))
        lines.append("\n## agy repeat (S1a vs S1b)")
        lines.append(f"- same relation: {_pct(same_rel, len(pair))}")
        lines.append(f"- same answers on all five fields: {_pct(same_all, len(pair))}")

    if complete:
        lines.append("\n## votes (S1a, S2, S3)")
        unan = [x for x in complete if len({x["runs"][v]["relation"] for v in VOTERS}) == 1]
        lines.append(f"- unanimous: {_pct(len(unan), len(complete))}")
        for a, b in (("S1a", "S2"), ("S1a", "S3"), ("S2", "S3")):
            same = sum(1 for x in complete if x["runs"][a]["relation"] == x["runs"][b]["relation"])
            lines.append(f"- {a}={b}: {_pct(same, len(complete))}")
        pattern = Counter(tuple(x["runs"][v]["relation"] for v in VOTERS) for x in complete)
        lines.append("- patterns: " + ", ".join(f"{'/'.join(k)}={n}" for k, n in pattern.most_common(12)))

        lines.append("\n## signal → non-unanimous rate (signals of S1a unless named)")
        split = {x["lid"]: len({x["runs"][v]["relation"] for v in VOTERS}) > 1 for x in complete}

        def group(name: str, key) -> None:
            buckets: dict[str, list[bool]] = defaultdict(list)
            for x in complete:
                buckets[str(key(x))].append(split[x["lid"]])
            parts = [f"{k}: {_pct(sum(v), len(v))}" for k, v in sorted(buckets.items())]
            lines.append(f"- {name}: " + "; ".join(parts))

        r1 = lambda x: x["runs"]["S1a"]  # noqa: E731
        group("S1a boundary", lambda x: r1(x)["boundary"])
        group("S1a basis", lambda x: r1(x)["basis"])
        group("S1a inconsistent", lambda x: r1(x)["inconsistent"])
        group("S1a quote<.8", lambda x: r1(x)["quote_score"] < .8)
        if pair:
            group("S1a≠S1b", lambda x: "S1b" in x["runs"] and x["runs"]["S1b"]["relation"] != r1(x)["relation"])
        group("S2 boundary", lambda x: x["runs"]["S2"]["boundary"])
        group("S3 boundary", lambda x: x["runs"]["S3"]["boundary"])
        group("any boundary", lambda x: any(x["runs"][v]["boundary"] for v in VOTERS))
        for f in ("same_page", "target_kind", "in_proof", "in_box_statement", "in_footnote",
                  "in_paren", "in_heading", "target_before", "target_post_earlier"):
            group(f"feature {f}", lambda x, f=f: x["features"].get(f))
        group("feature pair_size>1", lambda x: (x["features"].get("pair_size") or 1) > 1)

    lines.append("\n## usage")
    lines.extend(usage_table(pilot_dir))
    return "\n".join(lines)
