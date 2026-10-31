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
   first, since the shadow ledger fills exactly those slots on the site.  Only
   published posts that are not under revision are judged (``out_of_scope``).

A round is the set of links one pass through S1→S2→S3 judges.  If a unit's text
changes while its round is open, the round restarts.  After S3 the round is
finalized: unanimous links go to the shadow ledger, which is committed
(``[Cron] Link Dependencies Shadow [lastmod-skip]``); the rest go to the human
queue.

Log wording matters: the dashboard reads "error" and "failed" in this log as a
failed run, so those words appear only for real failures.
"""
from __future__ import annotations

import re
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
# A prompt over the byte limit is deterministic: the same text builds the same
# prompt, so the hourly retry only re-spent the earlier stages' calls (S2 Step 1 is
# Opus) and logged the same failure.  Such a unit is parked until its text changes,
# with a weekly retry in case the limit itself was raised.
PARK_SEC = 7 * 24 * 3600
FIT_EVERY_SEC = 24 * 3600
NEXT = {"S1": "S2", "S2": "S3", "S3": None}
LEDGER_REL = store.LEDGER_REL


def _fingerprint(paths: list[Path]) -> str:
    return units.Unit(key="", paths=paths, texts={p: p.read_text(encoding="utf-8") for p in paths}).fingerprint


# The key of scripts/ci/freeze_revising_posts.py for a published post being reworked.
REVISING_RE = re.compile(r"^revising:\s*true\s*$", re.M)


def out_of_scope(all_paths: list[list[Path]]) -> set[str]:
    """Keys of the units the cron leaves alone: drafts (``published: false``) and posts
    under revision.  Their text is still being edited and links come and go, so they
    are judged once the flag is gone (user decision 2026-10-20).  A round under way
    pauses and restarts then, since the text will have changed."""
    published = {post.path: post.published for post in dc._POSTS}
    skip = set()
    for paths in all_paths:
        for path in paths:
            text = path.read_text(encoding="utf-8")
            front = text[4:].split("\n---", 1)[0] if text.startswith("---\n") else ""
            if not published.get(path, True) or REVISING_RE.search(front):
                skip.add(dc.unit_key(paths))
                break
    return skip


def pick(state: dict) -> tuple | None:
    """The next (paths, stage, unit, reason) to run, or None."""
    now = time.time()
    all_paths = units.all_units()
    rels = [str(p.relative_to(store.ROOT)) for paths in all_paths for p in paths]
    dirty = set(dirty_paths(rels, store.ROOT))
    skip = out_of_scope(all_paths)
    entries = state["units"]
    open_rounds = sum(1 for key, e in entries.items()
                      if e.get("next") and key not in skip and not e.get("parked_fp"))

    def usable(paths: list[Path], key: str) -> bool:
        if key in skip:
            return False
        if any(str(p.relative_to(store.ROOT)) in dirty for p in paths):
            return False
        entry = entries.get(key, {})
        if entry.get("parked_fp") and _fingerprint(paths) != entry["parked_fp"]:
            return True                                 # the text changed: try again
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
        blank = any(production.get(l) is None or production[l].relation not in dc.RELATIONS
                    for l in _cheap_lids(paths))
        (fresh_blank if blank else fresh_other).append(paths)
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


def commit_ledger(detail: str, commit: bool) -> None:
    """Commit whatever the shadow ledger holds now (the dashboard's rulings ride along)."""
    if not commit:
        log(f"shadow ledger saved without commit: {detail}")
        return
    if not commit_outputs("Link Dependencies Shadow", [LEDGER_REL], detail, log=log, repo=store.ROOT):
        raise RuntimeError("could not commit the shadow ledger")


def _locked():
    held = store.lock(120)
    if held is None:
        raise RuntimeError("shadow state stayed locked for two minutes")
    return held


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


def run_recheck(commit: bool) -> bool:
    """One approved "다시 볼 후보": Step 4 again on all three stages with the new precedent.

    The link keeps its value if every stage still lands on it with agreeing
    precedents; otherwise it goes to the human queue as a recheck.
    """
    queue = store.load_queue()
    if not queue["recheck"]:
        return False
    if not all(models.available(s) for s in models.STAGES):
        return False
    item = queue["recheck"][0]
    lid = item["lid"]
    all_paths = units.all_units()
    found = None
    for paths in all_paths:
        h = units.unit_hash(dc.unit_key(paths))
        record = store.load_unit_record(h)
        if lid in record.get("links", {}):
            found = (paths, h, record)
            break
    gone = found is None or units.load_unit(found[0]).link(lid) is None
    # A draft or a post under revision gets a fresh round once its flag is gone,
    # and that round sees the new precedent anyway.
    paused = not gone and dc.unit_key(found[0]) in out_of_scope(all_paths)
    if gone or paused:
        with _locked():
            queue = store.load_queue()
            queue["recheck"] = [x for x in queue["recheck"] if x != item]
            store.save_queue(queue)
        log(f"shadow recheck {lid}: " + ("the link is gone" if gone else "its post is a draft or under revision")
            + "; dropped")
        return True
    paths, h, record = found
    unit = units.load_unit(paths)
    rec = record["links"][lid]
    results = {}
    try:
        for stage in models.STAGES:
            rows, usages = pipe.run_step4(stage, pipe.step4_items(unit, record, stage, [lid]))
            pipe._record_issue(stage, lid, rows[lid])
            results[stage] = rows[lid]
    except Exception as exc:  # noqa: BLE001
        log(f"ERROR shadow recheck {lid}: {exc}")
        return True
    final = (rec.get("final") or {}).get("relation")
    relations = {r["relation"] for r in results.values()}
    precedents = {r["precedent"] for r in results.values()}
    rec.setdefault("rechecks", []).append({"precedent": item["precedent"], "results": results,
                                           "at": int(time.time())})
    held = _locked()
    queue = store.load_queue()
    queue["recheck"] = [x for x in queue["recheck"] if x != item]
    if relations == {final} and len(precedents) == 1:
        log(f"shadow recheck {lid}: still {final} under {item['precedent']}")
    else:
        queue["human"][lid] = {"unit": record["unit"], "kind": "recheck",
                               "votes": {s: r["relation"] for s, r in results.items()},
                               "precedents": {s: r["precedent"] for s, r in results.items()},
                               "issues": sorted({r.get("pending_id") for r in results.values()
                                                 if r.get("pending_id")}),
                               "was": final, "precedent": item["precedent"],
                               "decisive": pipe.decisive(lid, rec, record["links"]),
                               "created": int(time.time())}
        log(f"shadow recheck {lid}: sent to the human queue ({sorted(relations)})")
    with held:
        store.merge_unit_record(h, record, [lid])
        store.save_queue(queue)
    return True


def tick(*, commit: bool = True) -> int:
    if dc.legacy_classifier_running():
        log("legacy dependency classifier is still running; skip this tick")
        return 0
    probe = dc.ledger.try_lock()
    if probe is None:
        # The old classifier holds this for its whole tick; the dashboard only for
        # a moment.  Either way, mint_lids should not race it.
        log("link relation ledger is locked (old classifier or dashboard); skip this tick")
        return 0
    probe.release()
    tick_lock = store.try_tick_lock()
    if tick_lock is None:
        log("another shadow tick (or the pilot) is still running; skip this tick")
        return 0
    try:
        if dc.mint_lids(commit=commit):
            return 0
        if run_digest():
            return 0
        if run_recheck(commit):
            return 0
        state = store.load_state()
        state.setdefault("started_at", int(time.time()))
        maybe_fit(state)
        picked = pick(state)
        if picked is None:
            store.save_state(state)
            log("shadow: nothing runnable this tick (rounds waiting on quota, or all done)")
            return 0
        paths, stage, unit, reason = picked
        return run(state, paths, stage, unit, reason, commit=commit)
    finally:
        try:
            # Dashboard rulings write the shadow ledger too; commit them even on a
            # tick that finalized nothing, so they never sit in the tree for autopush.
            if commit and dirty_paths([LEDGER_REL], store.ROOT):
                commit_ledger("대시보드 판정 반영", commit)
        except Exception as exc:  # noqa: BLE001
            log(f"ERROR shadow ledger commit: {exc}")
        tick_lock.release()


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
        elif stage == "S1" and not record.get("round"):
            # The round's S1 failed before anything was saved, so the unit record never
            # got its round: start it again rather than close the unit as finished.
            start_round(unit, record, "restart")
        round_lids = [lid for lid in record.get("round", []) if unit.link(lid) is not None]
        record["round"] = round_lids
        if not round_lids:
            entry.update({"next": None, "updated": int(time.time())})
            entry.pop("error", None)
            entry.pop("retry_after", None)
            with _locked():
                store.merge_unit_record(h, record, [])
            store.save_state(state)
            return 0
        log(f"shadow {stage} {key}: {len(round_lids)} link(s) ({reason})")
        summary = pipe.run_stage(stage, unit, record, set(round_lids))
        if _fingerprint(paths) != unit.fingerprint:
            log(f"shadow {stage} {key}: text changed during the stage; the round restarts")
            entry["updated"] = int(time.time())
            store.save_state(state)
            return 0
        result = None
        with _locked():
            fresh = store.merge_unit_record(h, record, round_lids)
            if stage == "S3":
                queue = store.load_queue()
                records = store.load_ledger()
                result = pipe.finalize(fresh, round_lids, records, queue, state["started_at"])
                store.save_unit_record(h, fresh)
                store.save_queue(queue)
                store.save_ledger(records)
        entry.update({"next": NEXT[stage], "updated": int(time.time()), "fp": unit.fingerprint})
        entry.pop("error", None)
        entry.pop("retry_after", None)
        entry.pop("parked_fp", None)
        log(f"shadow {stage} {key}: {summary}")
        if result is not None:
            entry["links"] = len(unit.lids)
            log(f"shadow finalized {key}: {result}")
            if result["to_human"]:
                dc.notify("[dependency] 링크 재판정",
                          f"{paths[0].stem}: 판정 대기 {result['to_human']}건 추가", level="passive",
                          url=dc.DASHBOARD_URL, digest=True)
            store.save_state(state)
            commit_ledger(f"{paths[0].stem}: 확정 {result['finalized']}건, "
                          f"사람 판정 대기 {result['to_human']}건", commit)
        store.save_state(state)
        return 0
    except Exception as exc:  # noqa: BLE001
        if isinstance(exc, models.ModelError) and "prompt exceeds" in str(exc):
            first = entry.get("parked_fp") != unit.fingerprint
            entry.update({"updated": int(time.time()), "retry_after": int(time.time() + PARK_SEC),
                          "error": str(exc)[:1000], "parked_fp": unit.fingerprint})
            store.save_state(state)
            # No "error"/"failed" here: the dashboard would read this handled state
            # as a broken worker (see the module docstring).
            log(f"shadow {stage} {key}: parked — {exc}; waits until the text changes")
            if first:
                dc.notify("[dependency] 섀도 판정 보류",
                          f"{paths[0].stem} {stage}: 프롬프트가 한도({models.MAX_PROMPT_BYTES} bytes)를 "
                          f"넘어 글이 바뀔 때까지 이 글은 건너뜁니다.\n{exc}",
                          level="passive", url=dc.DASHBOARD_URL, digest=True)
            return 0
        entry.update({"updated": int(time.time()), "retry_after": int(time.time() + RETRY_SEC),
                      "error": str(exc)[:1000]})
        store.save_state(state)
        log(f"ERROR shadow {stage} {key}: {exc}")
        return 1
    finally:
        lease.release()
