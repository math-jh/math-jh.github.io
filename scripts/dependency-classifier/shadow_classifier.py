#!/usr/bin/env python3
"""Shadow re-judging of internal-link relations — the cron entry point.

Every internal link of `_posts/Math` is judged again from scratch, blind to the
production ledger, by three fixed models in turn (S1 Antigravity, S2 Claude
Opus, S3 Codex).  A unanimous result goes to the shadow ledger
`_data/link_relations_next.yml`; anything else waits for a human ruling on the
dashboard.  The production ledger stays as it is until the shadow run is
promoted.  The design record is the memory file project_dependency_shadow_ledger
and this package's docstrings; criteria.md holds the criteria.

Modes:
  (no flag)          one cron tick
  --probe PATH       Step 1 of one unit for one stage, nothing written to state
  --pilot N          the signal pilot: Step 1 by S1 twice, S2, and S3 on N units
  --pilot-report     the pilot's distributions
  --status           counts
"""
from __future__ import annotations

import argparse
import json
import sys
import time
from pathlib import Path

import dependency_classifier as dc
import shadow_models as models
import shadow_pipeline as pipe
import shadow_store as store
import shadow_units as units

log = dc.log


def find_unit(path_arg: str) -> list[Path]:
    target = Path(path_arg).resolve()
    for paths in units.all_units():
        if target in [p.resolve() for p in paths]:
            return paths
    raise SystemExit(f"no unit contains {path_arg}")


def probe(path_arg: str, stage: str, out: str | None, prompt_only: bool) -> int:
    unit = units.load_unit(find_unit(path_arg))
    if unit.waiting:
        log(f"{unit.key}: some link still lacks a lid; the unit would wait")
    calls = units.build_calls(unit)
    result = {"unit": unit.key, "calls": []}
    for call in calls:
        prompt = pipe.dump_prompt(call)
        log(f"{call['source_rel']}: {len(call['items'])} item(s), "
            f"{len(call['targets'])} target excerpt(s), prompt {len(prompt.encode())} bytes")
        if prompt_only:
            if out:
                Path(out).write_text(prompt, encoding="utf-8")
            continue
        started = time.time()
        rows, usages = pipe.run_step1(stage, call)
        log(f"{stage} answered {len(rows)} item(s) in {time.time() - started:.0f}s")
        result["calls"].append({"source": call["source_rel"], "features": call["features"],
                                "rows": rows, "usage": usages,
                                "summary": pipe.summarize_rows(rows)})
    if out and not prompt_only:
        Path(out).write_text(json.dumps(pipe.jsonable(result), ensure_ascii=False, indent=1),
                             encoding="utf-8")
    for call in result["calls"]:
        print(json.dumps(call["summary"], ensure_ascii=False))
        print(json.dumps(call["usage"], ensure_ascii=False))
    return 0


# ── pilot ────────────────────────────────────────────────────────────────

PILOT_RUNS = (("S1a", "S1"), ("S1b", "S1"), ("S2", "S2"), ("S3", "S3"))


def pilot_units(n: int) -> list[list[Path]]:
    """Medium-sized units, spread over categories, in a fixed pseudo-random order."""
    by_cat: dict[str, list[tuple[str, list[Path]]]] = {}
    for paths in units.all_units():
        if paths[0].parent.name != "ko":
            continue
        unit = units.load_unit(paths)
        count = len(unit.lids)
        if unit.waiting or not 5 <= count <= 60:
            continue
        by_cat.setdefault(paths[0].parent.parent.name, []).append((units.unit_hash(unit.key), paths))
    for rows in by_cat.values():
        rows.sort()
    chosen: list[list[Path]] = []
    cats = sorted(by_cat)
    depth = 0
    while len(chosen) < n and any(len(by_cat[c]) > depth for c in cats):
        for cat in cats:
            if len(chosen) < n and len(by_cat[cat]) > depth:
                chosen.append(by_cat[cat][depth][1])
        depth += 1
    return chosen


def pilot(n: int) -> int:
    held = store.try_tick_lock()
    if held is None:
        log("pilot: a shadow tick (or another pilot) holds the tick lock")
        return 0
    try:
        for paths in pilot_units(n):
            unit = units.load_unit(paths)
            out_path = store.PILOT_DIR / f"{units.unit_hash(unit.key)}.json"
            record = store.read_json(out_path, {})
            if record.get("fingerprint") != unit.fingerprint:
                record = {"unit": unit.key, "fingerprint": unit.fingerprint, "calls": []}
            calls = units.build_calls(unit)
            if not record["calls"]:
                record["calls"] = [{"source": c["source_rel"], "features": c["features"],
                                    "runs": {}, "usage": {}, "errors": {}} for c in calls]
            for call, saved in zip(calls, record["calls"]):
                for name, stage in PILOT_RUNS:
                    if name in saved["runs"]:
                        continue
                    if not models.available(stage):
                        log(f"pilot: {models.PROVIDER[stage]} quota closed; {name} left for later")
                        continue
                    started = time.time()
                    try:
                        rows, usages = pipe.run_step1(stage, call)
                    except Exception as exc:  # noqa: BLE001
                        saved["errors"][name] = str(exc)[:500]
                        log(f"pilot: {name} gave no answer for {call['source_rel']}: {exc}")
                        continue
                    saved["runs"][name] = rows
                    saved["usage"][name] = usages
                    saved["errors"].pop(name, None)
                    store.write_json(out_path, pipe.jsonable(record))
                    log(f"pilot: {name} {call['source_rel']} {len(rows)} item(s) "
                        f"{time.time() - started:.0f}s")
        return 0
    finally:
        held.release()


def pilot_report() -> int:
    import shadow_report
    print(shadow_report.render(store.PILOT_DIR))
    return 0


def status() -> int:
    state = store.load_state()
    counts: dict[str, int] = {}
    for entry in state["units"].values():
        counts[entry.get("stage", "?")] = counts.get(entry.get("stage", "?"), 0) + 1
    queue = store.load_queue()
    print(json.dumps({
        "state": str(store.STATE_PATH), "stages": counts,
        "ledger": len(store.load_ledger()),
        "human": len(queue["human"]), "audit": len(queue["audit"]),
        "digest": len(queue["digest"]),
        "providers": {stage: models.available(stage) for stage in models.STAGES},
    }, ensure_ascii=False, indent=2))
    return 0


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--probe")
    parser.add_argument("--stage", default="S1", choices=models.STAGES)
    parser.add_argument("--out")
    parser.add_argument("--prompt-only", action="store_true")
    parser.add_argument("--pilot", type=int)
    parser.add_argument("--pilot-report", action="store_true")
    parser.add_argument("--status", action="store_true")
    parser.add_argument("--no-commit", action="store_true")
    args = parser.parse_args()
    if args.probe:
        return probe(args.probe, args.stage, args.out, args.prompt_only)
    if args.pilot:
        return pilot(args.pilot)
    if args.pilot_report:
        return pilot_report()
    if args.status:
        return status()
    import shadow_tick
    return shadow_tick.tick(commit=not args.no_commit)


if __name__ == "__main__":
    sys.exit(main())
