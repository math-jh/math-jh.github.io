#!/usr/bin/env python3
"""감사 페이지(#audit) 링크 재판정의 데이터와 판정 동작 — 의존성 링크 전면 재판정(섀도 원장).

데이터의 정본은 scripts/dependency-classifier/shadow_*.py 가 쓰는 상태다
(~/.local/state/dependency-shadow, _data/link_relations_next.yml). 여기서는 그걸
읽어 화면용으로 묶고, 사람의 판정을 같은 모듈로 쓴다. 쓰기는 전부 shadow_store 의
짧은 상태 락 안에서 한다 — 틱은 모델 호출 중에 이 락을 쥐지 않으므로 오래 기다릴
일이 없다.

사람이 볼 것은 셋이다:
* 판정 대기 — 세 모델이 갈렸거나 판례 선택이 갈린 링크. 판례 대기(쟁점)별로 묶고,
  화면(그래프·선수지식)을 바꾸는 링크를 먼저 보인다. 판정 단위는 링크다.
* 감사 — 만장일치로 끝난 링크의 표본. 모델들의 답을 가린 채 먼저 고르고, 고른 뒤에
  공개한다. 만장일치와 다르게 고르면 설명이 있어야 판정이 들어간다.
* 판례 — digest 워커의 초안 승인, 판례·판례 대기의 한 줄 설명 수정, 철회·정리.
그 밖에 신호 파일럿(shadow_classifier.py --pilot)의 판정을 읽기 전용으로 펼친다.
"""
from __future__ import annotations

import time
from pathlib import Path

import dependency_classifier as dc
import shadow_book as book
import shadow_prompts as sp
import shadow_report as report
import shadow_store as store
import shadow_units as units

LOCK_WAIT = 15
STAGES = ("S1", "S2", "S3")
MODEL = {"S1": "Antigravity", "S2": "Claude", "S3": "Codex"}


class Busy(RuntimeError):
    pass


def _locked():
    held = store.lock(LOCK_WAIT)
    if held is None:
        raise Busy("섀도 상태를 다른 작업이 쓰는 중이다 — 잠시 뒤 다시")
    return held


# ── 읽기 ──────────────────────────────────────────────────────────────────

def _unit_paths() -> dict[str, list[Path]]:
    return {dc.unit_key(paths): paths for paths in units.all_units()}


class _Units:
    """한 요청 안에서 unit 을 한 번만 읽는다 (extract_links 가 싸지 않다)."""

    def __init__(self) -> None:
        self.paths = _unit_paths()
        self._units: dict[str, units.Unit] = {}
        self._records: dict[str, dict] = {}

    def unit(self, key: str) -> units.Unit | None:
        if key not in self._units:
            paths = self.paths.get(key)
            self._units[key] = units.load_unit(paths) if paths else None
        return self._units[key]

    def record(self, key: str) -> dict:
        if key not in self._records:
            self._records[key] = store.load_unit_record(units.unit_hash(key))
        return self._records[key]


def _context(u: units.Unit | None, lid: str) -> dict:
    if u is None:
        return {}
    link = u.link(lid)
    if link is None:
        return {"gone": True}
    text = u.texts[link.source]
    return {"source_context": dc.source_context(text, link.start, 1),
            "target_context": dc.target_context(link, False)[1],
            "path": str(link.source.relative_to(store.ROOT)), "line": link.line,
            "markup": text[link.start:link.ial_end or link.end], "target": link.target}


def _permalinks() -> dict[str, str]:
    """소스 경로 → 그 글의 permalink. 미리보기가 dev 서버의 구워진 글을 띄울 때 쓴다."""
    return {post.rel: post.permalink for post in dc._POSTS}


def _brief(rec: dict, permalinks: dict[str, str]) -> dict:
    """Where the link is, from the unit record alone — cheap enough for every row."""
    return {"path": rec.get("source"), "line": rec.get("line"), "markup": rec.get("link"),
            "target": rec.get("target"), "same_page": (rec.get("features") or {}).get("same_page"),
            "permalink": permalinks.get(rec.get("source") or "")}


def link_detail(lid: str, unit: str = "") -> dict:
    """Source paragraph and target excerpt of one link, read on demand — a queued link,
    or with ``unit`` a pilot link."""
    queue = store.load_queue()
    item = queue["human"].get(lid) or queue["audit"].get(lid) or queue["settled"].get(lid)
    if item is None and not unit:
        raise KeyError(lid)
    paths = _unit_paths().get(item["unit"] if item is not None else unit)
    return {"lid": lid, **_context(units.load_unit(paths) if paths else None, lid)}


PILOT_RUNS = {"S1a": "Antigravity", "S1b": "Antigravity", "S1c": "Antigravity",
              "S2": "Claude", "S3": "Codex"}
PILOT_FIELDS = ("relation", "preview", "need", "need_kind", "provided", "evidence", "reason",
                "other_side", "flip_condition", "basis", "boundary", "inconsistent", "quote_score")


def pilot() -> dict:
    """파일럿 판정을 글별·링크별로 편다. S1 은 S1a·S1b(갈리면 S1c)의 다수결이다."""
    cache = _Units()
    permalinks = _permalinks()
    posts = []
    for path in sorted(store.PILOT_DIR.glob("*.json"), key=lambda p: p.stat().st_mtime):
        record = store.read_json(path, {})
        u = cache.unit(record.get("unit", ""))
        links, ran = [], set()
        for call in record.get("calls", []):
            runs = call.get("runs", {})
            ran |= set(runs)
            for lid, features in call.get("features", {}).items():
                mine = {name: {k: rows[lid].get(k) for k in PILOT_FIELDS}
                        for name, rows in runs.items() if lid in rows}
                s1 = report.s1_majority(mine)
                link = u.link(lid) if u else None
                done = s1 is not None and "S2" in mine and "S3" in mine
                links.append({
                    "lid": lid, "path": call.get("source"), "line": link.line if link else None,
                    "markup": u.texts[link.source][link.start:link.ial_end or link.end] if link else None,
                    "permalink": permalinks.get(call.get("source") or ""),
                    "same_page": features.get("same_page"),
                    "runs": mine, "s1": s1, "done": done,
                    "unanimous": done and len({s1, mine["S2"]["relation"], mine["S3"]["relation"]}) == 1,
                    "unanimous_s1a": done and len({mine["S1a"]["relation"], mine["S2"]["relation"],
                                                   mine["S3"]["relation"]}) == 1,
                })
        errors = {name: err for call in record.get("calls", [])
                  for name, err in (call.get("errors") or {}).items()}
        posts.append({"unit": record.get("unit"), "links": links, "ran": sorted(ran),
                      "errors": errors})
    every = [x for p in posts for x in p["links"]]
    done = [x for x in every if x["done"]]
    try:
        tail = (store.STATE_DIR / "pilot.log").read_text(encoding="utf-8").splitlines()[-200:]
    except OSError:
        tail = []
    return {"posts": posts, "models": PILOT_RUNS,
            "summary": {"posts": len(posts), "links": len(every), "done": len(done),
                        "unanimous": sum(1 for x in done if x["unanimous"]),
                        "unanimous_s1a": sum(1 for x in done if x["unanimous_s1a"])},
            "last": tail[-1] if tail else "",
            "quota": [line for line in tail if "agy weekly remaining" in line][-2:]}


def _stage_view(rec: dict) -> dict:
    out = {}
    for stage in STAGES:
        s = rec.get("stages", {}).get(stage)
        if not s:
            continue
        row = s["step1"]
        view = {"model": MODEL[stage],
                "step1": {k: row.get(k) for k in ("relation", "preview", "need", "need_kind",
                                                   "provided", "evidence", "reason", "other_side",
                                                   "flip_condition", "basis", "boundary",
                                                   "inconsistent", "quote_score")}}
        if s.get("step4"):
            s4 = s["step4"]
            view["step4"] = {"relation": s4["relation"], "precedent": s4["precedent"],
                             "reason": s4.get("precedent_reason"),
                             "pending": s4.get("pending_id"),
                             "note": (s4.get("reveal") or {}).get("difference_note")}
        out[stage] = view
    return out


def snapshot() -> dict:
    state = store.load_state()
    queue = store.load_queue()
    cache = _Units()
    permalinks = _permalinks()
    stages: dict[str, int] = {}
    for entry in state["units"].values():
        key = entry.get("next") or "done"
        stages[key] = stages.get(key, 0) + 1

    groups: dict[str, dict] = {}
    for lid, item in queue["human"].items():
        rec = cache.record(item["unit"]).get("links", {}).get(lid, {})
        issue = (item.get("issues") or [None])[0]
        g = groups.setdefault(issue or "", {"issue": issue, "items": []})
        g["items"].append({
            "lid": lid, "kind": item.get("kind"), "decisive": item.get("decisive"),
            "votes": item.get("votes"), "precedents": item.get("precedents"),
            "issues": item.get("issues"), "was": item.get("was"), "created": item.get("created"),
            "stages": _stage_view(rec), **_brief(rec, permalinks),
        })
    for g in groups.values():
        g["items"].sort(key=lambda x: (not x.get("decisive"), x.get("created") or 0))
        if g["issue"]:
            e = book.get(g["issue"])
            if e is not None:
                g.update({"description": e.description, "question": e.meta.get("question"),
                          "status": e.status, "body": e.body})
    human = sorted(groups.values(),
                   key=lambda g: (not any(x.get("decisive") for x in g["items"]), g["issue"] is None,
                                  min(x.get("created") or 0 for x in g["items"])))

    audit = []
    for lid, item in sorted(queue["audit"].items(), key=lambda kv: kv[1].get("created", 0)):
        rec = cache.record(item["unit"]).get("links", {}).get(lid, {})
        audit.append({"lid": lid, "stratum": item.get("stratum"), "created": item.get("created"),
                      **_brief(rec, permalinks)})

    stats = book.load_stats()
    return {
        "progress": {"units": len(cache.paths), "stages": stages,
                     "ledger": len(store.load_ledger()), "human": len(queue["human"]),
                     "audit": len(queue["audit"]), "digest": len(queue["digest"]),
                     "drafts": len(queue["drafts"]), "recheck": len(queue["recheck"]),
                     "settled": len(queue["settled"]),
                     "errors": [{"unit": k, "error": e.get("error")} for k, e in state["units"].items()
                                if e.get("error")][:10]},
        "human": human,
        "audit": audit,
        "drafts": queue["drafts"],
        "precedents": [{"id": e.id, "status": e.status, "description": e.description,
                        "question": e.meta.get("question"), "relation": e.meta.get("relation"),
                        "applied": len(stats.get(e.id, {}).get("applied", [])),
                        "audits": stats.get(e.id, {}).get("audits", 0),
                        "audit_errors": stats.get(e.id, {}).get("audit_errors", 0),
                        "body": e.body} for e in book.entries("P")],
        "pending": [{"id": e.id, "status": e.status, "description": e.description,
                     "question": e.meta.get("question"), "links": e.meta.get("links") or [],
                     "raised_by": e.meta.get("raised_by"), "body": e.body}
                    for e in book.entries("Q") if e.status == "open"],
        "criteria": sp.criteria_text(),
        "settled": [{**x, **_brief((cache.record(x["unit"]) if x.get("unit") else {})
                                   .get("links", {}).get(x["lid"], {}), permalinks)}
                    for x in sorted(({"lid": k, **v} for k, v in queue["settled"].items()),
                                    key=lambda x: -x.get("at", 0))[:20]],
    }


# ── 판정 ──────────────────────────────────────────────────────────────────

def _check_relation(relation: str) -> None:
    if relation not in sp.RELATIONS:
        raise ValueError("relation 은 required·weak·forward 중 하나")


def _set_final(unit_key: str, lid: str, final: dict) -> None:
    h = units.unit_hash(unit_key)
    record = store.load_unit_record(h)
    record.setdefault("links", {}).setdefault(lid, {})["final"] = final
    store.save_unit_record(h, record)


def _job_id(prefix: str) -> str:
    return f"{prefix}-{int(time.time() * 1000)}"


def rule(lid: str, relation: str, explanation: str = "") -> dict:
    """판정 대기 링크 하나를 판정한다. 설명을 쓰면 digest 로 간다."""
    _check_relation(relation)
    with _locked():
        queue = store.load_queue()
        item = queue["human"].get(lid)
        if item is None:
            raise KeyError("이미 판정된 링크")
        records = store.load_ledger()
        records[lid] = dc.ledger.Record(relation, True)
        store.save_ledger(records)
        now = int(time.time())
        _set_final(item["unit"], lid, {"relation": relation, "by": "human", "at": now,
                                        **({"explanation": explanation} if explanation else {})})
        queue["human"].pop(lid)
        queue["settled"][lid] = {**item, "relation": relation, "at": now, "how": "ruling"}
        if explanation.strip():
            queue["digest"].append({"id": _job_id("J"), "kind": "ruling_note",
                                    "rulings": {lid: relation}, "explanation": explanation.strip(),
                                    "qid": (item.get("issues") or [None])[0]})
        store.save_queue(queue)
    return {"lid": lid, "relation": relation}


def reopen(lid: str) -> dict:
    """방금 내린 판정을 되돌려 판정 대기로 돌린다 (감사 판정은 감사로)."""
    with _locked():
        queue = store.load_queue()
        item = queue["settled"].pop(lid, None)
        if item is None:
            raise KeyError("되돌릴 판정이 없다")
        records = store.load_ledger()
        how = item.pop("how", "ruling")
        prior = item.pop("prior", None)
        item.pop("relation", None)
        item.pop("at", None)
        if how == "audit":
            if prior:
                records[lid] = dc.ledger.Record(prior, True)
                _set_final(item["unit"], lid, {"relation": prior, "by": "unanimous",
                                                "at": int(time.time())})
            queue["audit"][lid] = item
        else:
            records.pop(lid, None)
            _set_final(item["unit"], lid, {"relation": None, "by": "human", "at": int(time.time())})
            queue["human"][lid] = item
        store.save_ledger(records)
        queue["digest"] = [j for j in queue["digest"] if lid not in (j.get("rulings") or {})]
        store.save_queue(queue)
    return {"lid": lid}


def audit(lid: str, relation: str, explanation: str = "") -> dict:
    """감사 답. 고른 값이 만장일치와 같으면 그대로 확인, 다르면 설명이 있어야 들어간다.

    응답에 모델들의 답을 실어 보낸다 — 고르기 전에는 화면에 없던 정보다."""
    _check_relation(relation)
    with _locked():
        queue = store.load_queue()
        item = queue["audit"].get(lid)
        if item is None:
            raise KeyError("이미 처리된 감사 항목")
        record = store.load_unit_record(units.unit_hash(item["unit"]))
        rec = record.get("links", {}).get(lid, {})
        final = (rec.get("final") or {}).get("relation")
        reveal = {"final": final, "stages": _stage_view(rec)}
        precedents = {s["step4"]["precedent"] for s in rec.get("stages", {}).values()
                      if s.get("step4") and s["step4"]["precedent"] != "none"}
        if relation != final and not explanation.strip():
            return {"match": False, "need_explanation": True, "reveal": reveal}
        now = int(time.time())
        for pid in precedents:
            book.bump_audit(pid, error=relation != final)
        queue["audit"].pop(lid)
        queue["settled"][lid] = {**item, "relation": relation, "at": now, "how": "audit",
                                 "prior": final}
        if relation != final:
            records = store.load_ledger()
            records[lid] = dc.ledger.Record(relation, True)
            store.save_ledger(records)
            _set_final(item["unit"], lid, {"relation": relation, "by": "audit", "was": final,
                                            "at": now, "explanation": explanation.strip()})
            queue["digest"].append({"id": _job_id("J"), "kind": "audit_error",
                                    "rulings": {lid: relation}, "unanimous": final,
                                    "explanation": explanation.strip()})
        store.save_queue(queue)
    return {"match": relation == final, "reveal": reveal}


def register(qid: str, explanation: str = "") -> dict:
    """판례 대기 하나를 판례로 등록해 달라고 digest 에 넘긴다 (판정된 링크만 실린다)."""
    e = book.get(qid)
    if e is None or e.status != "open":
        raise KeyError("열린 판례 대기가 아니다")
    with _locked():
        queue = store.load_queue()
        rulings = {}
        for lid in e.meta.get("links") or []:
            settled = queue["settled"].get(lid)
            if settled and settled.get("relation"):
                rulings[lid] = settled["relation"]
        if not rulings:
            raise ValueError("이 쟁점의 링크를 먼저 하나 이상 판정해야 한다")
        queue["digest"].append({"id": _job_id("J"), "kind": "register", "qid": qid,
                                "rulings": rulings, "explanation": explanation.strip()})
        store.save_queue(queue)
    return {"qid": qid, "rulings": len(rulings)}


def edit_issue(entry_id: str, statement: str | None, description: str | None) -> dict:
    if description is not None and len(description) > book.DESCRIPTION_MAX:
        raise ValueError(f"한 줄 설명은 {book.DESCRIPTION_MAX}자 이내")
    book.restate(entry_id, statement or None, description or None)
    return {"id": entry_id}


def move(lid: str, from_id: str | None, to_id: str | None, new: dict | None) -> dict:
    """링크를 다른 쟁점으로 옮기거나 새 쟁점을 만든다."""
    with _locked():
        queue = store.load_queue()
        item = queue["human"].get(lid)
        if item is None:
            raise KeyError("판정 대기 링크가 아니다")
        if new:
            if new.get("question") not in book.QUESTIONS or not new.get("statement") \
                    or not new.get("description"):
                raise ValueError("새 쟁점에는 question·statement·description 이 필요하다")
            to_id = book.raise_issue(question=new["question"], statement=new["statement"],
                                     description=new["description"][:book.DESCRIPTION_MAX],
                                     raised_by="human", lid=lid)
        elif to_id:
            book.attach(to_id, lid)
        if from_id:
            book.detach(from_id, lid)
        issues = [x for x in item.get("issues") or [] if x != from_id]
        if to_id and to_id not in issues:
            issues.insert(0, to_id)
        item["issues"] = issues
        store.save_queue(queue)
    return {"lid": lid, "issue": to_id}


def close_issue(qid: str, action: str, into: str | None = None) -> dict:
    if action == "dismiss":
        book.set_status(qid, "dismissed")
    elif action == "merge" and into:
        book.merge(qid, into)
        with _locked():
            queue = store.load_queue()
            for item in queue["human"].values():
                if qid in (item.get("issues") or []):
                    item["issues"] = [into if x == qid else x for x in item["issues"]]
            store.save_queue(queue)
    else:
        raise ValueError("action 은 dismiss 또는 merge(into 필요)")
    return {"id": qid}


def draft(draft_id: str, action: str, edited: dict | None, choice: str | None,
          accept_recheck: bool) -> dict:
    import shadow_digest
    if action == "discard":
        with _locked():
            queue = store.load_queue()
            queue["drafts"] = [d for d in queue["drafts"] if d["id"] != draft_id]
            store.save_queue(queue)
        return {"discarded": draft_id}
    allowed = {k: v for k, v in (edited or {}).items()
               if k in ("issue", "ruling", "reason", "description", "principle", "relation", "question")}
    return shadow_digest.apply_draft(draft_id, edited=allowed, choice=choice,
                                     accept_recheck=accept_recheck)


def precedent(pid: str, action: str, description: str | None = None) -> dict:
    e = book.get(pid)
    if e is None:
        raise KeyError(pid)
    if action == "describe":
        if not description or len(description) > book.DESCRIPTION_MAX:
            raise ValueError(f"한 줄 설명은 1–{book.DESCRIPTION_MAX}자")
        book.restate(pid, None, description)
        return {"id": pid}
    if action == "revoke":
        book.set_status(pid, "revoked", revoked=time.strftime("%Y-%m-%d"))
        with _locked():
            queue = store.load_queue()
            for lid in book.load_stats().get(pid, {}).get("applied", []):
                queue["recheck"].append({"lid": lid, "precedent": None, "created": int(time.time()),
                                         "revoked": pid})
            store.save_queue(queue)
        return {"id": pid, "rechecks": len(book.load_stats().get(pid, {}).get("applied", []))}
    raise ValueError("action 은 describe 또는 revoke")


def consolidate(kind: str, ids: list[str]) -> dict:
    import shadow_digest
    if kind not in ("merge", "promote") or not ids:
        raise ValueError("kind 는 merge·promote, ids 필요")
    return shadow_digest.apply_consolidation(kind, ids)
