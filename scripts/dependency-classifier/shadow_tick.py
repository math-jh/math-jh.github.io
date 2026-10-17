#!/usr/bin/env python3
"""One cron tick of the shadow pipeline: one stage of one unit, nothing in parallel.

Order of business:
1. ``mint_lids`` — new links get their lid first, exactly as before.  The
   translation worker waits for lids (``awaiting_link_ids``), so this must keep
   running whatever else the tick does.  A tick that asked a model to pair EN
   lids ends there.
2. one digest job, if the dashboard queued any (a ruling with an explanation, or
   a pending issue to turn into a precedent).
3. one stage of one unit.  A unit whose round is under way comes first, oldest
   first, as soon as the provider of its next stage is open — rounds are
   finished before new ones start, so the calibration and the precedents see
   complete results early.  A new round starts only while fewer than ``WIP_CAP``
   rounds are open.  New links in a finished unit come before untouched units,
   and among untouched units those with links production has no value for come
   first, since the shadow ledger fills exactly those slots on the site.

A round is the set of links one pass through S1→S2→S3 judges.  If a unit's text
changes while its round is open, the round restarts.  After S3 the round is
finalized: unanimous links go to the shadow ledger, which is committed
(``[Cron] Link Dependencies Shadow [lastmod-skip]``); the rest go to the human
queue.

Log wording matters: the dashboard reads "error" and "failed" in this log as a
failed run, so those words appear only for real failures.
"""
from __future__ import annotations

import time
from pathlib import Path

import dependency_classifier as dc
import shadow_models as models
import shadow_pipeline as pipe
import shadow_risk as risk
import shadow_store as store
import shadow_units as units
from blog_file_lock import try_acquire_file_locks
from cron_commit import commit_outputs, dirty_paths

log = dc.log
WIP_CAP = 4
RETRY_SEC = 3600
FIT_EVERY_SEC = 24 * 3600
NEXT = {"S1": "S2", "S2": "S3", "S3": None}
LEDGER_REL = str(store.LEDGER_PATH.relative_to(store.ROOT))


def _fingerprint(paths: list[Path]) -> str:
    return units.Unit(key="", paths=paths, texts={p: p.read_text(encoding="utf-8") for p in paths}).fingerprint


def _production_blank(unit: units.Unit, production: dict) -> bool:
    return any((production.get(lid) is None or production[lid].relation not in dc.RELATIONS)
               for lid in unit.lids)


def pick(state: dict) -> tuple | None:
    """The next (paths, stage, unit, reason) to run, or None."""
    now = time.time()
    all_paths = units.all_units()
    rels = [str(p.relative_to(store.ROOT)) for paths in all_paths for p in paths]
    dirty = set(dirty_paths(rels, store.ROOT))
    entries = state["units"]
    open_rounds = sum(1 for e in entries.values() if e.get("next"))

    def usable(paths: list[Path], key: str) -> bool:
        if any(str(p.relative_to(store.ROOT)) in dirty for p in paths):
            return False
        entry = entries.get(key, {})
        return entry.get("retry_after", 0) <= now

    # 1. rounds under way, oldest first
    under_way = sorted(((e.get("updated", 0), key) for key, e in entries.items() if e.get("next")))
    by_key = {dc.unit_key(paths): paths for paths in all_paths}
    for _, key in under_way:
        paths = by_key.get(key)
        if paths is None:
            entries.pop(key, None)                      # the post is gone
            continue
        if not usable(paths, key):
            continue
        entry = entries[key]
        if _fingerprint(paths) != entry["fp"]:
            unit = units.load_unit(paths)
            if unit.waiting or not models.available("S1"):
                continue
            return paths, "S1", unit, "restart"
        if models.available(entry["next"]):
            return paths, entry["next"], units.load_unit(paths), "continue"
    if open_rounds >= WIP_CAP or not models.available("S1"):
        return None
    # 2. finished units whose text changed (new links), then 3. untouched units
    production = dc.ledger.load()
    fresh_blank, fresh_other = [], []
    for paths in all_paths:
        key = dc.unit_key(paths)
        if not usable(paths, key):
            continue
        entry = entries.get(key)
        if entry is not None:
            if entry.get("next") or entry.get("fp") == _fingerprint(paths):
                continue
            unit = units.load_unit(paths)
            record = store.load_unit_record(units.unit_hash(key))
            done = {lid for lid, r in record.get("links", {}).items() if r.get("final")}
            if not unit.waiting and set(unit.lids) - done:
                return paths, "S1", unit, "delta"
            entry["fp"] = unit.fingerprint              # edits without new links
            continue
        (fresh_blank if any(production.get(l) is None for l in _cheap_lids(paths))
         else fresh_other).append(paths)
    for paths in fresh_blank + fresh_other:
        unit = units.load_unit(paths)
        if unit.waiting or not unit.lids:
            if not unit.lids and not unit.waiting:
                entries[unit.key] = {"fp": unit.fingerprint, "next": None, "updated": int(now),
                                     "links": 0}
            continue
        return paths, "S1", unit, "new"
    return None


def _cheap_lids(paths: list[Path]) -> list[str]:
    import re
    found = []
    for p in paths:
        found += re.findall(r'data-lid="([0-9a-z]{5})"', p.read_text(encoding="utf-8"))
    return found


def start_round(unit: units.Unit, record: dict, reason: str) -> list[str]:
    links = record.setdefault("links", {})
    if reason == "delta":
        lids = [lid for lid in unit.lids if not (links.get(lid) or {}).get("final")]
    else:
        lids = [lid for lid in unit.lids if not (links.get(lid) or {}).get("final")] \
            if reason == "restart" else list(unit.lids)
    for lid in lids:
        links[lid] = {}
    record["round"] = lids
    record["round_no"] = record.get("round_no", 0) + 1
    record["unit"] = unit.key
    return lids


def commit_ledger(records: dict, detail: str, commit: bool) -> None:
    before = store.LEDGER_PATH.read_text(encoding="utf-8") if store.LEDGER_PATH.exists() else None
    store.save_ledger(records)
    if not commit:
        log(f"shadow ledger saved without commit: {detail}")
        return
    if not commit_outputs("Link Dependencies Shadow", [LEDGER_REL], detail, log=log, repo=store.ROOT):
        if before is not None:
            store.write_text(store.LEDGER_PATH, before)
        raise RuntimeError("could not commit the shadow ledger; restored it")


def maybe_fit(state: dict) -> None:
    if time.time() - state.get("fitted_at", 0) < FIT_EVERY_SEC:
        return
    outcomes: dict[str, list] = {s: [] for s in models.STAGES}
    for path in store.UNITS_DIR.glob("*.json"):
        record = store.read_json(path, {})
        for rec in record.get("links", {}).values():
            final = (rec.get("final") or {}).get("relation")
            if not final:
                continue
            for stage, srec in rec.get("stages", {}).items():
                row = srec.get("step1")
                if row:
                    outcomes[stage].append((risk.vector(row, rec.get("features", {})),
                                            int(row["relation"] != final)))
    fitted = risk.fit(outcomes)
    state["fitted_at"] = int(time.time())
    if fitted:
        log("shadow calibration refitted: " + ", ".join(
            f"{s} n={m['n']} overturned={m['overturned']}" for s, m in fitted.items()))


def run_digest() -> bool:
    import shadow_digest
    return shadow_digest.run_one()


def tick(*, commit: bool = True) -> int:
    if dc.legacy_classifier_running():
        log("legacy dependency classifier is still running; skip this tick")
        return 0
    production_lock = dc.ledger.try_lock()
    if production_lock is None:
        log("link relation ledger is locked (dashboard); skip this tick")
        return 0
    shadow_lock = store.try_lock()
    if shadow_lock is None:
        production_lock.release()
        log("shadow state is locked (dashboard or another tick); skip this tick")
        return 0
    try:
        if dc.mint_lids(commit=commit):
            return 0
        if run_digest():
            return 0
        state = store.load_state()
        state.setdefault("started_at", int(time.time()))
        picked = pick(state)
        if picked is None:
            store.save_state(state)
            maybe_fit(state)
            store.save_state(state)
            log("shadow: nothing runnable this tick (rounds waiting on quota, or all done)")
            return 0
        paths, stage, unit, reason = picked
        return run(state, paths, stage, unit, reason, commit=commit)
    finally:
        shadow_lock.release()
        production_lock.release()


def run(state: dict, paths: list[Path], stage: str, unit: units.Unit, reason: str,
        *, commit: bool) -> int:
    key = unit.key
    h = units.unit_hash(key)
    lease = try_acquire_file_locks(paths)
    if lease is None:
        log(f"shadow: {key} is locked by another worker; next tick")
        return 0
    entry = state["units"].setdefault(key, {})
    try:
        record = store.load_unit_record(h)
        if stage == "S1" and reason in ("new", "delta", "restart"):
            start_round(unit, record, reason)
            entry.update({"fp": unit.fingerprint, "next": "S1", "started": int(time.time())})
        round_lids = [lid for lid in record.get("round", []) if unit.link(lid) is not None]
        record["round"] = round_lids
        if not round_lids:
            entry.update({"next": None, "updated": int(time.time())})
            store.save_unit_record(h, record)
            store.save_state(state)
            return 0
        log(f"shadow {stage} {key}: {len(round_lids)} link(s) ({reason})")
        summary = pipe.run_stage(stage, unit, record, set(round_lids))
        if _fingerprint(paths) != unit.fingerprint:
            log(f"shadow {stage} {key}: text changed during the stage; the round restarts")
            entry["updated"] = int(time.time())
            store.save_state(state)
            return 0
        store.save_unit_record(h, record)
        entry.update({"next": NEXT[stage], "updated": int(time.time()), "fp": unit.fingerprint})
        entry.pop("error", None)
        entry.pop("retry_after", None)
        log(f"shadow {stage} {key}: {summary}")
        if stage == "S3":
            queue = store.load_queue()
            records = store.load_ledger()
            result = pipe.finalize(record, round_lids, records, queue, state["started_at"])
            store.save_unit_record(h, record)
            store.save_queue(queue)
            commit_ledger(records, f"{paths[0].stem}: 확정 {result['finalized']}건, "
                                   f"사람 판정 대기 {result['to_human']}건", commit)
            entry["links"] = len(unit.lids)
            log(f"shadow finalized {key}: {result}")
        store.save_state(state)
        return 0
    except Exception as exc:  # noqa: BLE001
        entry.update({"updated": int(time.time()), "retry_after": int(time.time() + RETRY_SEC),
                      "error": str(exc)[:1000]})
        if "record" in locals():
            store.save_unit_record(h, record)
        store.save_state(state)
        log(f"ERROR shadow {stage} {key}: {exc}")
        return 1
    finally:
        lease.release()
