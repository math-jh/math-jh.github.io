#!/usr/bin/env python3
"""The digest worker: turns a human ruling with an explanation into a precedent
draft, and is the single gate through which precedents are created or changed.

Jobs come from the dashboard (``queue["digest"]``):
  audit_error  an audited unanimous link the human ruled differently, with the
               required explanation
  ruling_note  a disputed link the human ruled with an (optional) explanation
  register     "판례로 등록" on a pending issue, after its links were ruled
  merge        a consolidation proposal to merge live precedents into the first:
               the draft is the keeper's text rewritten to decide every case the
               others decide

One job per tick, on Claude.  The model reads the explanation verbatim, the
models' answers on the links, the live precedents and pending issues, and a
short list of finished links that may share the mistake.  It answers with a
draft: a new precedent, an amendment of the live precedent on the same issue,
or a conflict with it (the human then supersedes or distinguishes).  When the
live precedents near the index cap, or some precedent has earned promotion,
the draft also carries a consolidation proposal.  Nothing is written to the
precedent files until the human approves the draft on the dashboard
(``apply_draft``); the user's explanation is kept verbatim in the precedent.
"""
from __future__ import annotations

import json
import re
import time

import dependency_classifier as dc
import shadow_book as book
import shadow_models as models
import shadow_prompts as sp
import shadow_store as store
import shadow_units as units

log = dc.log
RECHECK_OFFER = 40
RECHECK_MAX = 20
PROMOTE_AFTER = 10

DIGEST_HEAD = """You maintain the precedents of a link-judging pipeline for a mathematics blog. A human has ruled on one or more internal links and explained the ruling. Turn it into a precedent draft. Do not use tools and do not alter files. Return JSON only:
{"action":"new","precedent":null,"question":"provided","issue":"…","ruling":"…","relation":"weak","reason":"…","description":"…","principle":"…","examples":["lid"],"not_covered":null,"conflict_note":null,"recheck":["lid"],"consolidation":[]}

Rules:
- One issue has at most one live precedent. Compare the ruling with the live precedents first.
  - "new": no live precedent is about this issue.
  - "amend": a live precedent is about the same issue and reaches the same conclusion; "precedent" is its id, and issue/ruling/reason/description/principle are its improved text.
  - "conflict": a live precedent is about the same issue but this ruling reaches another conclusion; "precedent" is its id and "conflict_note" says where they part. The human will choose to supersede it or to treat this case as distinguishable.
  - "none": the ruling settles only this link and states no reusable rule.
- "issue" is a general question ("~인 경우, ~인가?"), not about this link alone. "ruling" states the conditions and the conclusion. "description" is one line of at most 80 characters. "principle" is a one-sentence rule a later criteria revision could adopt.
- "examples": at most 2 lids from the ruled links that show the issue best. "not_covered": optionally {"lid": "…", "note": "…"} for a ruled link that looks similar but falls outside the precedent, else null.
- "recheck": from RECHECK CANDIDATES only, at most 20 lids whose judgment may share the mistake this ruling corrects. [] if none.
- "consolidation": only when CONSOLIDATION is requested below — a list of {"kind":"merge"|"promote","ids":["P-…"],"note":"…"}; otherwise [].
- The human's explanation is authoritative. Write every text field in Korean, keep mathematical terms in English, and quote labels exactly.

CRITERIA (Korean):
"""


def _link_view(unit: units.Unit, rec: dict, lid: str) -> dict:
    link = unit.link(lid)
    view = {"id": lid, "link": rec.get("link"), "target": rec.get("target")}
    if link is not None:
        text = unit.texts[link.source]
        view["source_context"] = dc.source_context(text, link.start, 2)
        view["target_context"] = dc.target_context(link, False)[1]
    view["models"] = {
        stage: {"step1": {k: s["step1"][k] for k in ("relation", "need", "provided", "evidence", "reason")},
                "step4": ({k: s["step4"][k] for k in ("precedent", "precedent_reason", "relation")}
                          if s.get("step4") else None)}
        for stage, s in rec.get("stages", {}).items()}
    return view


def _locate(lid: str) -> tuple[units.Unit, dict] | None:
    for paths in units.all_units():
        record = store.load_unit_record(units.unit_hash(dc.unit_key(paths)))
        if lid in record.get("links", {}):
            return units.load_unit(paths), record
    return None


def _recheck_candidates(job_links: list[tuple[units.Unit, dict, str]]) -> list[dict]:
    """Finished links whose Step 1 answers look like the ruled links' — by pattern, not by model.

    Links of drafts and posts under revision are left out: the recheck would drop them.
    """
    from shadow_tick import out_of_scope
    paused = out_of_scope(units.all_units())
    patterns = set()
    for _, record, lid in job_links:
        rec = record["links"][lid]
        s1 = rec["stages"]["S1"]["step1"]
        patterns.add((s1["basis"], rec["features"].get("target_kind"), rec["features"].get("in_proof")))
    ruled = {lid for _, _, lid in job_links}
    out = []
    for path in sorted(store.UNITS_DIR.glob("*.json")):
        record = store.read_json(path, {})
        if record.get("unit") in paused:
            continue
        for lid, rec in record.get("links", {}).items():
            if lid in ruled or not (rec.get("final") or {}).get("relation"):
                continue
            s1 = (rec.get("stages", {}).get("S1") or {}).get("step1")
            if not s1:
                continue
            key = (s1["basis"], rec["features"].get("target_kind"), rec["features"].get("in_proof"))
            if key in patterns:
                out.append({"id": lid, "relation": rec["final"]["relation"],
                            "evidence": s1["evidence"], "reason": s1["reason"]})
            if len(out) >= RECHECK_OFFER:
                return out
    return out


def consolidation_needed() -> tuple[bool, list[dict]]:
    stats = book.load_stats()
    live = book.live("P")
    promotable = [{"id": e.id, "applied": len(stats.get(e.id, {}).get("applied", [])),
                   "audit_errors": stats.get(e.id, {}).get("audit_errors", 0)}
                  for e in live
                  if len(stats.get(e.id, {}).get("applied", [])) >= PROMOTE_AFTER
                  and not stats.get(e.id, {}).get("audit_errors", 0)]
    return len(live) >= book.CONSOLIDATE_AT or bool(promotable), promotable


def digest_prompt(job: dict, views: list[dict], candidates: list[dict]) -> str:
    live = book.live("P")
    chosen = {m["step4"]["precedent"] for v in views for m in v["models"].values() if m.get("step4")}
    files = {e.id: e.path.read_text(encoding="utf-8") for e in live
             if len(live) <= 12 or e.id in chosen}
    need, promotable = consolidation_needed()
    parts = [DIGEST_HEAD, sp.criteria_text(), "\n\nHUMAN RULING:\n",
             json.dumps({"kind": job["kind"], "rulings": job.get("rulings", {}),
                         "explanation": job.get("explanation", "")}, ensure_ascii=False, indent=1),
             "\n\nRULED LINKS:\n", json.dumps(views, ensure_ascii=False, indent=1),
             "\n\nLIVE PRECEDENTS (id — description):\n",
             "\n".join(book.index_lines("P")) or "(none yet)", "\n\n"]
    if files:
        parts.append("PRECEDENT FILES:\n" + "".join(f"<<<{k}\n{v}\n{k}>>>\n" for k, v in files.items()) + "\n")
    parts.append("OPEN PENDING ISSUES (id — description):\n"
                 + ("\n".join(book.index_lines("Q", limit=80)) or "(none)") + "\n\n")
    parts.append("RECHECK CANDIDATES:\n" + json.dumps(candidates, ensure_ascii=False, indent=1) + "\n\n")
    if need:
        parts.append(f"CONSOLIDATION requested: {len(live)} live precedents (cap {book.INDEX_CAP}); "
                     f"promotion candidates: {json.dumps(promotable, ensure_ascii=False)}\n")
    else:
        parts.append("CONSOLIDATION not requested.\n")
    return "".join(parts)


def run_one() -> bool:
    queue = store.load_queue()
    if not queue["digest"]:
        return False
    if not models.available("S2"):
        log(f"shadow digest: {len(queue['digest'])} job(s) wait for Claude quota")
        return False
    job = queue["digest"][0]
    lids = list(job.get("rulings", {}))
    try:
        if job.get("kind") == "merge":
            draft, usage = run_merge(job)
        else:
            located = []
            for lid in lids:
                found = _locate(lid)
                if found:
                    located.append((found[0], found[1], lid))
            views = [_link_view(u, r["links"][lid], lid) for u, r, lid in located]
            candidates = _recheck_candidates(located) if located else []
            payload, usage = models.call("S2", digest_prompt(job, views, candidates))
            draft = _clean(payload, set(lids), {c["id"] for c in candidates})
    except Exception as exc:  # noqa: BLE001
        held = store.lock(60)
        if held is not None:
            with held:
                queue = store.load_queue()
                for j in queue["digest"]:
                    if j.get("id") == job.get("id"):
                        j["attempts"] = j.get("attempts", 0) + 1
                store.save_queue(queue)
        log(f"ERROR shadow digest {job.get('id')}: {exc}")
        return True
    held = store.lock(120)
    if held is None:
        raise RuntimeError("shadow state stayed locked for two minutes")
    with held:
        queue = store.load_queue()
        queue["digest"] = [j for j in queue["digest"] if j.get("id") != job.get("id")]
        queue["drafts"].append({"id": f"D-{int(time.time())}", "job": job, "draft": draft,
                                "created": int(time.time()), "usage": usage})
        store.save_queue(queue)
    log(f"shadow digest {job.get('id')}: draft {draft['action']}")
    return True


def _clean(payload: dict, ruled: set[str], offered: set[str]) -> dict:
    action = payload.get("action") if payload.get("action") in ("new", "amend", "conflict", "none") else "new"
    precedent = payload.get("precedent")
    if action in ("amend", "conflict") and not (precedent and book.get(str(precedent))):
        action, precedent = "new", None
    out = {k: (str(payload.get(k)).strip() if payload.get(k) else "")
           for k in ("issue", "ruling", "reason", "description", "principle", "conflict_note")}
    out["description"] = out["description"][:book.DESCRIPTION_MAX]
    out.update({
        "action": action, "precedent": precedent if action in ("amend", "conflict") else None,
        "question": payload.get("question") if payload.get("question") in book.QUESTIONS else "need",
        "relation": payload.get("relation") if payload.get("relation") in sp.RELATIONS else None,
        "examples": [x for x in payload.get("examples") or [] if x in ruled][:2],
        "not_covered": payload.get("not_covered") if isinstance(payload.get("not_covered"), dict)
        and payload["not_covered"].get("lid") in ruled else None,
        "recheck": [x for x in payload.get("recheck") or [] if x in offered][:RECHECK_MAX],
        "consolidation": [c for c in payload.get("consolidation") or []
                          if isinstance(c, dict) and c.get("kind") in ("merge", "promote")],
    })
    return out


# ── applying an approved draft (called by the dashboard) ─────────────────

def _example_lines(lids: list[str], relation: str | None) -> list[str]:
    lines = []
    for lid in lids:
        found = _locate(lid)
        evidence = ""
        if found:
            stages = found[1]["links"][lid].get("stages", {})
            evidence = (stages.get("S1", {}).get("step1") or {}).get("evidence", "")
        lines.append(f"- lid `{lid}` — {evidence} — {relation or ''}".rstrip(" —"))
    return lines


def _body(draft: dict, explanation: str, older: str | None = None) -> str:
    parts = [f"## 쟁점\n{draft['issue']}", f"## 판정\n{draft['ruling']}", f"## 이유\n{draft['reason']}"]
    notes = [explanation.strip()] if explanation.strip() else []
    if older:
        notes.insert(0, older.strip())
    parts.append("## 사용자 설명 (원문)\n" + ("\n\n".join(notes) if notes else "(없음)"))
    parts.append("## 대표 예시 (최대 2개)\n" + ("\n".join(_example_lines(draft["examples"], draft["relation"]))
                                           or "(없음)"))
    if draft.get("not_covered"):
        nc = draft["not_covered"]
        parts.append("## 비슷하지만 해당하지 않는 경우\n" + f"- lid `{nc['lid']}` — {nc.get('note', '')}")
    if draft.get("principle"):
        parts.append(f"## 원칙 초안\n{draft['principle']}")
    return "\n\n".join(parts) + "\n"


def _old_explanation(entry: book.Entry) -> str:
    import re
    m = re.search(r"## 사용자 설명 \(원문\)\n(.*?)(\n## |\Z)", entry.body, re.S)
    return m.group(1).strip() if m and m.group(1).strip() != "(없음)" else ""


def apply_draft(draft_id: str, *, edited: dict | None = None, choice: str | None = None,
                accept_recheck: bool = True) -> dict:
    """Write an approved draft.  ``choice`` settles a conflict: supersede | distinguish."""
    held = store.lock(30)
    if held is None:
        raise RuntimeError("shadow state is busy; try again")
    with held:
        queue = store.load_queue()
        item = next((d for d in queue["drafts"] if d["id"] == draft_id), None)
        if item is None:
            raise KeyError(draft_id)
        draft = {**item["draft"], **(edited or {})}
        job = item["job"]
        explanation = job.get("explanation", "")
        meta = {"status": "active", "description": draft["description"], "question": draft["question"],
                "relation": draft["relation"], "created": time.strftime("%Y-%m-%d"),
                "source": job.get("qid") or job.get("kind"), "supersedes": []}
        written = None
        if draft["action"] == "merge":
            written = apply_merge(draft)
        elif draft["action"] == "new" or (draft["action"] == "conflict" and choice == "supersede"):
            pid = book.next_id("P")
            older = None
            if draft["action"] == "conflict":
                old = book.get(draft["precedent"])
                meta["supersedes"] = [old.id]
                older = _old_explanation(old)
                book.write(old.id, {**old.meta, "status": "superseded", "superseded_by": pid}, old.body)
            written = book.write(pid, meta, _body(draft, explanation, older)).id
        elif draft["action"] == "amend":
            old = book.get(draft["precedent"])
            written = book.write(old.id, {**old.meta, "description": draft["description"]},
                                 _body(draft, explanation, _old_explanation(old))).id
        elif draft["action"] == "conflict" and choice == "distinguish":
            old = book.get(draft["precedent"])
            lids = list(job.get("rulings", {}))
            note = draft.get("conflict_note") or ""
            body = old.body.rstrip() + "\n\n## 비슷하지만 해당하지 않는 경우\n" + "\n".join(
                f"- lid `{lid}` — {note}" for lid in lids[:1]) + "\n"
            written = book.write(old.id, old.meta, body).id
        if job.get("qid"):
            q = book.get(job["qid"])
            if q is not None and q.status == "open":
                book.write(q.id, {**q.meta, "status": "ruled", "ruled_into": written}, q.body)
        if accept_recheck and written:
            for lid in draft.get("recheck", []):
                queue["recheck"].append({"lid": lid, "precedent": written, "created": int(time.time())})
        queue["drafts"] = [d for d in queue["drafts"] if d["id"] != draft_id]
        queue.setdefault("applied", []).append({"draft": draft_id, "written": written,
                                                "at": int(time.time())})
        store.save_queue(queue)
        return {"written": written}


PROMOTED_HEADING = "### 승격된 원칙"
PROMOTED_EMPTY = "(아직 없다)"


def principle_text(body: str) -> str | None:
    """The "## 원칙 초안" section of a precedent body, joined into one line."""
    m = re.search(r"^## 원칙 초안\s*\n(.*?)(?=^## |\Z)", body, re.M | re.S)
    if not m:
        return None
    text = " ".join(line.strip() for line in m.group(1).splitlines() if line.strip())
    return text or None


def add_principles(text: str, lines: list[str]) -> str:
    """Append bullet lines to the promoted-principles section of criteria.md.

    The section runs from its heading to the next heading or the end of the file;
    the placeholder line goes once a principle is in.  A line whose "(P-…)" tag is
    already in the section is skipped."""
    m = re.search(rf"^{re.escape(PROMOTED_HEADING)}[ \t]*\n(.*?)(?=^#{{1,3}} |\Z)", text, re.M | re.S)
    if not m:
        raise ValueError(f"criteria.md 에 '{PROMOTED_HEADING}' 절이 없다")
    section = [l for l in m.group(1).rstrip("\n").splitlines() if l.strip() != PROMOTED_EMPTY]
    for line in lines:
        tag = line.split(")", 1)[0] + ")"
        if not any(l.startswith(tag) for l in section):
            section.append(line)
    body = "\n".join(section).strip("\n")
    tail = text[m.end():]
    return text[:m.start(1)] + body + "\n" + ("\n" + tail if tail else "")


def apply_consolidation(kind: str, ids: list[str]) -> dict:
    """promote: copy each precedent's "## 원칙 초안" into criteria.md's promoted
    section, then mark it promoted (it leaves the live index, so the criteria line
    is what the prompts keep).  A precedent without that section is refused, and
    nothing changes.  merge: queue a digest job; the worker drafts the first
    precedent's text absorbing the rest, and only approving that draft rewrites it
    and supersedes the rest (``apply_merge``)."""
    held = store.lock(30)
    if held is None:
        raise RuntimeError("shadow state is busy; try again")
    with held:
        if kind == "promote":
            found = [(pid, book.get(pid)) for pid in ids]
            missing = [pid for pid, e in found if e is None]
            if missing:
                raise ValueError(f"없는 판례: {', '.join(missing)}")
            lines = []
            for pid, e in found:
                text = principle_text(e.body)
                if text is None:
                    raise ValueError(f"{pid} 에 '## 원칙 초안' 절이 없어 승격할 수 없다")
                lines.append(f"- ({pid}) {text}")
            path = sp.CRITERIA_PATH
            store.write_text(path, add_principles(path.read_text(encoding="utf-8"), lines))
            for pid, e in found:
                book.write(pid, {**e.meta, "status": "promoted"}, e.body)
            return {"promoted": ids}
        live = {e.id for e in book.live("P")}
        if len(ids) < 2 or any(pid not in live for pid in ids):
            raise ValueError("병합은 살아 있는 판례 둘 이상이어야 한다")
        queue = store.load_queue()
        if any(j.get("kind") == "merge" and j.get("ids") == ids for j in queue["digest"]):
            return {"queued": None, "ids": ids}
        job = {"id": f"J-{int(time.time() * 1000)}", "kind": "merge", "ids": ids,
               "created": int(time.time())}
        queue["digest"].append(job)
        store.save_queue(queue)
        return {"queued": job["id"], "ids": ids}


# ── merge: the keeper absorbs the others, through a draft ───────────────

MERGE_HEAD = """You maintain the precedents of a link-judging pipeline for a mathematics blog. Several live precedents are to be merged into the first one (the keeper); the others will be superseded and leave the index, so the keeper's new text is all that remains of them. Do not use tools and do not alter files. Return JSON only:
{"action":"merge","question":"provided","issue":"…","ruling":"…","relation":"weak","reason":"…","description":"…","principle":"…","examples":["lid"],"note":"…"}

Rules:
- The merged ruling must decide every case each precedent decides, with the same conclusion under the same conditions. Where the precedents split a question into two sides (e.g. one says when it is provided, another when it is not), state both sides and the condition that separates them. Do not drop a condition, a conclusion, or a distinction a precedent draws.
- "issue" is one general question covering all of them. "relation" is the relation the ruling most often concludes, or null if the sides conclude differently. "description" is one line of at most 80 characters. "principle" is one sentence a later criteria revision could adopt.
- "reason" keeps each precedent's grounds, and cites other precedents by id where they did.
- "examples": at most 2 lids, from the examples the precedents already list.
- "note": one line on what was combined and what separates the cases.
- If the precedents are not about one issue, so that one ruling cannot carry them without losing a distinction, return {"action":"none","note":"…"} saying why.
- Write every text field in Korean, keep mathematical terms in English, and quote labels exactly.

CRITERIA (Korean):
"""

LID_RE = re.compile(r"lid `([0-9a-z]{5})`")


def merge_prompt(entries: list[book.Entry]) -> str:
    files = "".join(f"<<<{e.id}\n{e.path.read_text(encoding='utf-8')}\n{e.id}>>>\n" for e in entries)
    return (MERGE_HEAD + sp.criteria_text() + "\n\nKEEPER: " + entries[0].id
            + "\n\nPRECEDENT FILES (keeper first):\n" + files)


def run_merge(job: dict) -> dict:
    """Ask Claude for the keeper's merged text; returns (draft, usage)."""
    entries = [book.get(pid) for pid in job["ids"]]
    if any(e is None or e.status != "active" for e in entries):
        return {"action": "none", "precedent": job["ids"][0], "merged": job["ids"][1:],
                "note": "병합할 판례 가운데 살아 있지 않은 것이 있다", "examples": [], "recheck": [],
                "consolidation": []}, {}
    payload, usage = models.call("S2", merge_prompt(entries))
    known = {lid for e in entries for lid in LID_RE.findall(e.body)}
    draft = {k: (str(payload.get(k)).strip() if payload.get(k) else "")
             for k in ("issue", "ruling", "reason", "description", "principle", "note")}
    draft["description"] = draft["description"][:book.DESCRIPTION_MAX]
    draft.update({
        "action": "merge" if payload.get("action") == "merge" and draft["ruling"] else "none",
        "precedent": entries[0].id, "merged": [e.id for e in entries[1:]],
        "question": payload.get("question") if payload.get("question") in book.QUESTIONS
        else entries[0].meta.get("question", "need"),
        "relation": payload.get("relation") if payload.get("relation") in sp.RELATIONS else None,
        "examples": [x for x in payload.get("examples") or [] if x in known][:2],
        "not_covered": None, "conflict_note": "", "recheck": [], "consolidation": [],
    })
    return draft, usage


def _merged_explanations(entries: list[book.Entry]) -> str:
    notes = []
    for e in entries:
        text = _old_explanation(e)
        if text:
            notes.append(text if e is entries[0] else f"({e.id}) {text}")
    return "\n\n".join(notes)


def apply_merge(draft: dict) -> str:
    """Rewrite the keeper with the merged text and supersede the others into it.
    Called by apply_draft under the state lock."""
    keep = book.get(draft["precedent"])
    rest = [book.get(pid) for pid in draft.get("merged", [])]
    if keep is None or keep.status != "active" or any(e is None or e.status != "active" for e in rest):
        raise ValueError("병합할 판례가 그새 바뀌었다 — 초안을 버리고 다시 제안할 것")
    meta = {**keep.meta, "description": draft["description"], "question": draft["question"],
            "relation": draft["relation"],
            "absorbs": sorted(set(keep.meta.get("absorbs") or []) | {e.id for e in rest})}
    book.write(keep.id, meta, _body(draft, "", _merged_explanations([keep, *rest])))
    for e in rest:
        book.write(e.id, {**e.meta, "status": "superseded", "superseded_by": keep.id}, e.body)
    return keep.id
