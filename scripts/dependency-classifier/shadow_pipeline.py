#!/usr/bin/env python3
"""The shadow pipeline's judging steps.

Step 1  every stage judges every link of a unit, blind to the other stages.
Step 2  a risk score from the Step 1 answers and the link's objective features
        picks the judgments that get a second look.
Step 3  the flagged judgments go back to the same model, in a fresh call that
        carries the first call's trace.
Step 4  that review compares the link with the precedents (blind multiple
        choice) and the open pending issues, and either answers by a
        precedent, attaches the link to a pending issue, or raises a new one.

A higher stage also re-runs Step 4 blind for every link a lower stage sent
through Steps 3–4 (rule C), and the worker compares the two.  Only after that
does a reveal call show the higher model the lower model's issue statement, to
merge issues stated in different words (rule A) and to note where the blind
results differ.  The reveal never changes a vote.
"""
from __future__ import annotations

import json
import time
from pathlib import Path

import shadow_features as feat
import shadow_models as models
import shadow_prompts as sp

MAX_RETRY = 1
# One call answers at most this many links; a whole article goes in with every chunk.
MAX_ITEMS = int(__import__("os").environ.get("DEPENDENCY_SHADOW_MAX_ITEMS", "20"))


def log(message: str) -> None:
    import dependency_classifier as dc
    dc.log(message)


def _split(call: dict) -> list[dict]:
    """Halve a call's items; each half keeps only the target excerpts it uses."""
    items = call["items"]
    halves = []
    for part in (items[: len(items) // 2], items[len(items) // 2:]):
        keys = {item.get("target_key") for item in part}
        halves.append({**call, "items": part,
                       "targets": {k: v for k, v in call["targets"].items() if k in keys}})
    return halves


def step1_prompt(call: dict) -> str:
    return sp.step1_prompt(source_rel=call["source_rel"], source_text=call["text"],
                           lang=call["lang"], targets=call["targets"], items=call["items"])


def _chunks(call: dict) -> list[dict]:
    items = call["items"]
    out = []
    for i in range(0, len(items), MAX_ITEMS):
        part = items[i:i + MAX_ITEMS]
        keys = {item.get("target_key") for item in part}
        out.append({**call, "items": part,
                    "targets": {k: v for k, v in call["targets"].items() if k in keys}})
    return out


def _run_parts(stage: str, parts: list[dict]) -> tuple[dict[str, dict], list[dict]]:
    rows, usages = {}, []
    for part in parts:
        r, u = run_step1(stage, part)
        rows.update(r)
        usages.extend(u)
    return rows, usages


def run_step1(stage: str, call: dict) -> tuple[dict[str, dict], list[dict]]:
    """Step 1 for one source file.  Returns rows by lid and the usage of each call."""
    if len(call["items"]) > MAX_ITEMS:
        return _run_parts(stage, _chunks(call))
    prompt = step1_prompt(call)
    if len(prompt.encode("utf-8")) > models.MAX_PROMPT_BYTES and len(call["items"]) > 1:
        return _run_parts(stage, _split(call))
    rows: dict[str, dict] = {}
    usages: list[dict] = []
    pending = call
    for attempt in range(MAX_RETRY + 1):
        ids = [item["id"] for item in pending["items"]]
        schema = sp.step1_schema(ids) if stage == "S3" else None
        try:
            payload, usage = models.call(stage, step1_prompt(pending), schema)
        except models.ModelError as exc:
            if "output token limit" in str(exc) and len(pending["items"]) > 1:
                log(f"{stage} step 1: output limit on {len(pending['items'])} item(s); asking in halves")
                r, u = _run_parts(stage, _split(pending))
                rows.update(r)
                usages.extend(u)
                break
            raise
        usage = {**usage, "items": len(ids), "prompt_bytes": len(step1_prompt(pending).encode())}
        usages.append(usage)
        got = sp.validate_step1(payload, set(ids))
        rows.update(got)
        missing = [item for item in pending["items"] if item["id"] not in rows]
        if missing:
            save_raw(stage, call["source_rel"], len(missing))
        if not missing:
            break
        if attempt < MAX_RETRY:
            log(f"{stage} step 1: asking again for {len(missing)} item(s) of {call['source_rel']}")
            keys = {item.get("target_key") for item in missing}
            pending = {**pending, "items": missing,
                       "targets": {k: v for k, v in pending["targets"].items() if k in keys}}
    for lid, row in rows.items():
        row["quote_score"] = feat.quote_score(row["evidence"], call["text"])
    missing = [item["id"] for item in call["items"] if item["id"] not in rows]
    if missing:
        raise models.ModelError(
            f"{stage} step 1 left {len(missing)} item(s) unanswered in {call['source_rel']}: "
            f"{missing[:4]}")
    return rows, usages


def save_raw(stage: str, source_rel: str, missing: int) -> None:
    """Keep the raw response of a call whose rows did not all validate (private state dir)."""
    import shadow_store as store
    folder = store.STATE_DIR / "debug"
    folder.mkdir(parents=True, exist_ok=True)
    name = f"{time.strftime('%Y%m%d-%H%M%S')}-{stage}-{Path(source_rel).stem}.txt"
    (folder / name).write_text(f"missing={missing}\n{models.LAST_RAW}", encoding="utf-8")
    log(f"{stage}: {missing} row(s) did not validate; raw response kept in {folder / name}")


def dump_prompt(call: dict) -> str:
    """For --probe: the exact prompt a call would send."""
    return step1_prompt(call)


def summarize_rows(rows: dict[str, dict]) -> dict:
    out: dict = {"n": len(rows), "relation": {}, "basis": {}, "boundary": {},
                 "inconsistent": 0, "missing_boundary_text": 0, "quote_low": 0}
    for row in rows.values():
        for key in ("relation", "basis"):
            out[key][row[key]] = out[key].get(row[key], 0) + 1
        out["boundary"][str(row["boundary"])] = out["boundary"].get(str(row["boundary"]), 0) + 1
        out["inconsistent"] += int(row["inconsistent"])
        out["missing_boundary_text"] += int(row["missing_boundary_text"])
        out["quote_low"] += int(row["quote_score"] < 0.8)
    return out


def jsonable(value):
    return json.loads(json.dumps(value, ensure_ascii=False, default=str))


# ── Steps 2–4 and the reveal, for one stage of one unit ───────────────────

import hashlib  # noqa: E402
import time  # noqa: E402

import dependency_classifier as dc  # noqa: E402
import shadow_book as book  # noqa: E402
import shadow_risk as risk  # noqa: E402
import shadow_units as units  # noqa: E402

STAGES = models.STAGES
STEP1_FIELDS = ("preview", "need", "need_kind", "provided", "relation", "evidence", "reason",
                "other_side", "flip_condition")


def vote(link_rec: dict, stage: str) -> str | None:
    rec = link_rec.get("stages", {}).get(stage)
    if not rec:
        return None
    if rec.get("step4"):
        return rec["step4"]["relation"]
    return rec["step1"]["relation"]


def step4_items(unit: units.Unit, unit_rec: dict, stage: str, lids: list[str]) -> list[dict]:
    items = []
    for lid in lids:
        link = unit.link(lid)
        text = unit.texts[link.source]
        _, target_excerpt = dc.target_context(link, True)
        row = unit_rec["links"][lid]["stages"][stage]["step1"]
        items.append({
            "id": lid, "link": text[link.start:link.ial_end or link.end], "line": link.line,
            "target": link.target,
            "source_context": dc.source_context(text, link.start, 2),
            "target_context": target_excerpt,
            "your_step1": {k: row[k] for k in STEP1_FIELDS},
        })
    return items


def run_step4(stage: str, items: list[dict]) -> tuple[dict[str, dict], list[dict]]:
    """Step 4 for a batch: a first call on the index, a second with any files asked for."""
    p_live = {e.id: e for e in book.live("P")}
    q_ids = {e.id for e in book.live("Q")}
    p_lines = book.index_lines("P")
    q_lines = book.index_lines("Q", limit=80)
    rows: dict[str, dict] = {}
    usages: list[dict] = []
    pending = items
    for attempt in range(MAX_RETRY + 1):
        ids = [i["id"] for i in pending]
        prompt = sp.step4_prompt(items=pending, precedent_lines=p_lines, pending_lines=q_lines)
        payload, usage = models.call(stage, prompt, sp.step4_schema(ids) if stage == "S3" else None)
        usages.append({**usage, "items": len(ids), "step": 4})
        rows.update(sp.validate_step4(payload, set(ids), precedents=set(p_live), pending=q_ids,
                                      files_phase=False))
        pending = [i for i in pending if i["id"] not in rows]
        if not pending:
            break
    if pending:
        raise models.ModelError(f"{stage} step 4 left {len(pending)} item(s) unanswered")
    asked = {lid: r["candidates"] for lid, r in rows.items() if r["candidates"]}
    if asked:
        wanted = sorted({pid for cands in asked.values() for pid in cands})
        files = {pid: p_live[pid].path.read_text(encoding="utf-8") for pid in wanted}
        sub = [i for i in items if i["id"] in asked]
        ids = [i["id"] for i in sub]
        prompt = sp.step4_prompt(items=sub, precedent_lines=p_lines, pending_lines=q_lines, files=files)
        payload, usage = models.call(stage, prompt, sp.step4_schema(ids) if stage == "S3" else None)
        usages.append({**usage, "items": len(ids), "step": "4-files"})
        decided = sp.validate_step4(payload, set(ids), precedents=set(p_live), pending=q_ids,
                                    files_phase=True)
        missing = [lid for lid in ids if lid not in decided]
        if missing:
            raise models.ModelError(f"{stage} step 4 (files) left {len(missing)} item(s) unanswered")
        rows.update(decided)
    return rows, usages


def _record_issue(stage: str, lid: str, row: dict) -> None:
    """Write a Step 4 outcome into the pending-issue files."""
    earlier = book.open_for(lid, raised_by=stage) if row["pending"] == "new" else None
    if earlier is not None:
        # A retried stage: the issue this stage raised for the link last time stands.
        row["pending_id"] = earlier.id
        return
    if row["pending"] == "new":
        issue = row["new_issue"]
        row["pending_id"] = book.raise_issue(question=issue["question"], statement=issue["statement"],
                                             description=issue["description"], raised_by=stage, lid=lid)
    elif row["pending"]:
        book.attach(row["pending"], lid)
        row["pending_id"] = row["pending"]
    if row.get("pending_id"):
        book.add_opinion(row["pending_id"],
                         f"{models.PROVIDER[stage]} ({stage}, lid `{lid}`): {row['relation']} — "
                         f"{row['precedent_reason'] or '판례 없음'}")


def run_reveal(stage: str, unit: units.Unit, unit_rec: dict, lids: list[str]) -> list[dict]:
    """Rule A and the difference note.  Changes issue files, never votes."""
    lower = STAGES[:STAGES.index(stage)]
    items = []
    for lid in lids:
        mine = unit_rec["links"][lid]["stages"][stage].get("step4")
        if not mine:
            continue
        lows = []
        for s in lower:
            low = unit_rec["links"][lid]["stages"].get(s, {}).get("step4")
            if not low:
                continue
            entry = book.get(low["pending_id"]) if low.get("pending_id") else None
            lows.append({"model": s, "precedent": low["precedent"], "relation": low["relation"],
                         "pending_id": low.get("pending_id"),
                         "pending_statement": entry.body if entry else None})
        if not lows:
            continue
        differs = any(low["precedent"] != mine["precedent"] or low["relation"] != mine["relation"]
                      for low in lows)
        raised = any(low["pending_id"] for low in lows)
        if not (differs or raised):
            continue
        link = unit.link(lid)
        text = unit.texts[link.source]
        mine_view = {k: mine[k] for k in ("precedent", "precedent_reason", "relation")}
        if mine.get("pending_id"):
            entry = book.get(mine["pending_id"])
            mine_view["pending_statement"] = entry.body if entry else None
        items.append({"id": lid, "link": text[link.start:link.ial_end or link.end],
                      "source_context": dc.source_context(text, link.start, 1),
                      "your_blind_review": mine_view, "lower": lows})
    if not items:
        return []
    ids = [i["id"] for i in items]
    payload, usage = models.call(stage, sp.reveal_prompt(items),
                                 sp.reveal_schema(ids) if stage == "S3" else None)
    rows = sp.validate_reveal(payload, set(ids))
    for item in items:
        lid = item["id"]
        result = rows.get(lid)
        if not result:
            continue
        mine = unit_rec["links"][lid]["stages"][stage]["step4"]
        mine["reveal"] = result
        for check in result["issue_check"]:
            low = next((x for x in item["lower"] if x["model"] == check["model"]), None)
            if not low or not low["pending_id"]:
                continue
            if check["verdict"] == "same":
                if mine.get("pending_id") and mine["pending_id"] != low["pending_id"]:
                    book.merge(mine["pending_id"], low["pending_id"])
                    mine["pending_id"] = low["pending_id"]
                if check["statement"]:
                    book.restate(low["pending_id"], check["statement"], check["description"])
            elif check["verdict"] == "covered" and check["precedent"]:
                book.add_opinion(low["pending_id"],
                                 f"{models.PROVIDER[stage]} ({stage}): {check['precedent']} 이(가) 이미 다룬다")
    return [{**usage, "items": len(ids), "step": "reveal"}]


def run_stage(stage: str, unit: units.Unit, unit_rec: dict, only: set[str] | None) -> dict:
    """Run one stage over the unit's round.  Mutates unit_rec; returns a summary."""
    now = int(time.time())
    fitted = risk.load_model()
    links = unit_rec.setdefault("links", {})
    usage = unit_rec.setdefault("usage", {}).setdefault(stage, [])
    round_lids: list[str] = []
    for call in units.build_calls(unit, only):
        rows, usages = run_step1(stage, call)
        usage.extend(usages)
        for item in call["items"]:
            lid = item["id"]
            round_lids.append(lid)
            rec = links.setdefault(lid, {})
            rec.update({"source": call["source_rel"], "line": item["line"], "link": item["link"],
                        "target": item["target"], "features": call["features"][lid]})
            stages = rec.setdefault("stages", {})
            stages[stage] = {"step1": rows[lid], "at": now,
                             "step2": risk.score(stage, rows[lid], call["features"][lid], fitted)}
    lower = STAGES[:STAGES.index(stage)]
    forced = {lid for lid in round_lids
              if any(links[lid]["stages"].get(s, {}).get("step4") for s in lower)}
    flagged = {lid for lid in round_lids if links[lid]["stages"][stage]["step2"]["flagged"]}
    review = sorted(flagged | forced)
    for lid in forced:
        links[lid]["stages"][stage]["forced"] = True
    if review:
        rows4, usages = run_step4(stage, step4_items(unit, unit_rec, stage, review))
        usage.extend(usages)
        for lid, row in rows4.items():
            _record_issue(stage, lid, row)
            links[lid]["stages"][stage]["step4"] = row
    if lower and forced:
        usage.extend(run_reveal(stage, unit, unit_rec, sorted(forced)))
    return {"stage": stage, "links": len(round_lids), "flagged": len(flagged),
            "forced": len(forced), "reviewed": len(review)}


# ── finalization (after S3) ───────────────────────────────────────────────

AUDIT_RATES = {"decisive": 0.04, "cross": 0.017, "same_page": 0.007, "precedent": 0.25}
AUDIT_FIRST_WEEK = 2.0
AUDIT_OVERSAMPLE = 2.0


def _pair_key(rec: dict) -> str:
    return rec["target"].split("#", 1)[0] if not rec["target"].startswith("#") else "#"


def decisive(lid: str, rec: dict, links: dict) -> bool:
    """Would this link's value change what readers see?  Same-page links never do."""
    if rec["features"].get("same_page"):
        return False
    pair = [(other, r) for other, r in links.items()
            if other != lid and r.get("source") == rec["source"] and _pair_key(r) == _pair_key(rec)]
    return not any((r.get("final") or {}).get("relation") == "required" for _, r in pair)


def audit_draw(lid: str, rec: dict, links: dict, started_at: float) -> str | None:
    precedent = any((s.get("step4") or {}).get("precedent", "none") != "none"
                    for s in rec["stages"].values())
    if precedent:
        stratum = "precedent"
    elif rec["features"].get("same_page"):
        stratum = "same_page"
    elif decisive(lid, rec, links):
        stratum = "decisive"
    else:
        stratum = "cross"
    p = AUDIT_RATES[stratum]
    s1 = rec["stages"]["S1"]["step1"]
    if s1["boundary"] or s1["basis"] == "weak_verify":
        p *= AUDIT_OVERSAMPLE
    if time.time() - started_at < 7 * 86400:
        p *= AUDIT_FIRST_WEEK
    draw = int(hashlib.sha1(f"audit:{lid}".encode()).hexdigest()[:8], 16) / 0xFFFFFFFF
    return stratum if draw < min(p, 1.0) else None


def finalize(unit_rec: dict, round_lids: list[str], records: dict, queue: dict,
             started_at: float) -> dict:
    """Unanimous with agreeing precedents → shadow ledger; anything else → human queue."""
    now = int(time.time())
    links = unit_rec["links"]
    done = disputed = sampled = 0
    for lid in round_lids:
        rec = links[lid]
        votes = {s: vote(rec, s) for s in STAGES}
        precs = {s: rec["stages"][s]["step4"]["precedent"] for s in STAGES
                 if rec["stages"][s].get("step4")}
        precedent_split = len(precs) >= 2 and len(set(precs.values())) > 1
        if len(set(votes.values())) == 1 and not precedent_split:
            relation = votes["S1"]
            rec["final"] = {"relation": relation, "by": "unanimous", "at": now}
            records[lid] = dc.ledger.Record(relation, True)
            for pid in set(precs.values()) - {"none"}:
                book.bump_applied(pid, lid)
            done += 1
            stratum = audit_draw(lid, rec, links, started_at)
            if stratum:
                queue["audit"][lid] = {"unit": unit_rec["unit"], "stratum": stratum, "created": now}
                sampled += 1
        else:
            rec["final"] = {"relation": None, "by": "human", "at": now}
            issues = sorted({s.get("step4", {}).get("pending_id") for s in rec["stages"].values()
                             if s.get("step4") and s["step4"].get("pending_id")})
            queue["human"][lid] = {
                "unit": unit_rec["unit"], "kind": "dispute", "votes": votes,
                "precedents": precs, "issues": issues,
                "decisive": decisive(lid, rec, links), "created": now,
            }
            disputed += 1
    return {"finalized": done, "to_human": disputed, "audit": sampled}
