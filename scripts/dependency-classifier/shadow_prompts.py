#!/usr/bin/env python3
"""Prompts, output schemas, and validation for the shadow re-judging pipeline.

The judging criteria live in ``criteria.md`` next to this file, in Korean.  The
prompt quotes that file verbatim and the dashboard renders the same file for its
"?" button, so there is exactly one copy of the criteria.  Everything else in a
prompt (how to answer, the item locator, the output shape) is English.

Step 1 does not ask a model how confident it is.  It asks the two questions the
criteria are built from — does the reader need what the target holds, and does
the source provide it — and lets the model mark a genuine boundary only through
``need: borderline`` or ``provided: partial``.  The worker derives the expected
relation, the criteria branch (``basis``), and the boundary count from those
answers; see ``derive``.
"""
from __future__ import annotations

import json
from pathlib import Path

HERE = Path(__file__).resolve().parent
CRITERIA_PATH = HERE / "criteria.md"

RELATIONS = ("required", "weak", "forward")
NEED = ("yes", "borderline", "no")
NEED_KIND = ("meaning", "step")
PROVIDED = ("full", "partial", "none")


def criteria_text() -> str:
    return CRITERIA_PATH.read_text(encoding="utf-8").strip()


STEP1_HOW = """HOW TO ANSWER
Answer, for every item, the questions the criteria are built from, each in its own field:
- preview (boolean): does the sentence carrying the link serve to announce that the target will later treat, extend, or develop the present material? Decide by the role of the sentence. If true, relation is "forward" and need, need_kind, provided are null.
- need: "yes" | "borderline" | "no". To follow the source at this point, does the reader need content that the target holds (a definition, notation, or construction; or a statement)? Answer this whether or not the source also provides that content.
- need_kind: "meaning" (criteria (a): the meaning of what is said here depends on it) | "step" (criteria (b): the argument here takes a step that relies on it). null when need is "no".
- provided: "full" | "partial" | "none". Is that needed content provided by the source, i.e. stated somewhere in the source article other than in the link's target itself? null when need is "no".
- relation: "required" | "weak" | "forward". It follows from the answers above: preview → forward; need "no" → weak; need "yes" with provided "full" → weak; need "yes" with provided "none" → required. Only when need is "borderline" or provided is "partial" do you choose between required and weak yourself.
- Use "borderline" and "partial" only for genuine boundary cases, never as a hedge. When you use either, other_side and flip_condition are mandatory.

Text fields — write them in Korean, keep mathematical terms in English, and quote labels (e.g. 정리 9, Theorem 9) exactly as they appear:
- evidence: the single sentence of the source that decides the judgment, copied verbatim.
- reason: one or two sentences.
- other_side: why the other of required/weak is plausible. null unless need is "borderline" or provided is "partial".
- flip_condition: what would have to be true for the other relation to hold. null under the same condition.
- requested_precedents: [] (reserved; leave empty).

Every field is always present; use null exactly where stated above.
"""

ITEM_LOCATOR = """ITEM LOCATOR
Each item is one occurrence of a link. The same link text can appear several times in an article, so an item names its occurrence by "id", which is the occurrence's data-lid: judge the occurrence in the source whose attribute list carries data-lid="<id>" (the "link" field shows it verbatim, with its line number), and no other. "target_key" names the target excerpt below; "same-article" means the target is part of the source itself, near the line given by "target_line" when known.
"""

STEP1_HEAD = """You judge the dependency relation of each internal link in one article of a mathematics blog. Do not use tools and do not alter files. Return JSON only, in the shape
{"items":[{"id":"…","preview":false,"need":"yes","need_kind":"step","provided":"none","relation":"required","evidence":"…","reason":"…","other_side":null,"flip_condition":null,"requested_precedents":[]}]}
with exactly one entry per item.

CRITERIA (Korean, authoritative):
"""


def step1_prompt(*, source_rel: str, source_text: str, lang: str,
                 targets: dict[str, dict], items: list[dict]) -> str:
    parts = [STEP1_HEAD, criteria_text(), "\n\n", STEP1_HOW, "\n", ITEM_LOCATOR, "\n"]
    parts.append(f"SOURCE ARTICLE ({lang}, {source_rel}):\n<<<SOURCE\n{source_text}\nSOURCE>>>\n\n")
    if targets:
        parts.append("TARGET EXCERPTS:\n")
        for key, target in targets.items():
            parts.append(f"[{key}] {target['target']}\n<<<{key}\n{target['excerpt']}\n{key}>>>\n\n")
    parts.append("ITEMS:\n")
    parts.append(json.dumps(items, ensure_ascii=False, indent=1))
    parts.append("\n")
    return "".join(parts)


def _nullable(values: tuple[str, ...]) -> dict:
    return {"type": ["string", "null"], "enum": [*values, None]}


def step1_schema(ids: list[str]) -> dict:
    """Strict JSON schema: every field required, nulls instead of absent fields.

    Codex's structured output rejects conditional requirements, so the schema
    states only the shape; the coupling between fields is checked in
    ``validate_step1``.
    """
    item = {
        "type": "object",
        "properties": {
            "id": {"type": "string", "enum": ids},
            "preview": {"type": "boolean"},
            "need": _nullable(NEED),
            "need_kind": _nullable(NEED_KIND),
            "provided": _nullable(PROVIDED),
            "relation": {"type": "string", "enum": list(RELATIONS)},
            "evidence": {"type": "string"},
            "reason": {"type": "string"},
            "other_side": {"type": ["string", "null"]},
            "flip_condition": {"type": ["string", "null"]},
            "requested_precedents": {"type": "array", "items": {"type": "string"}},
        },
        "required": ["id", "preview", "need", "need_kind", "provided", "relation",
                     "evidence", "reason", "other_side", "flip_condition",
                     "requested_precedents"],
        "additionalProperties": False,
    }
    return {
        "type": "object",
        "properties": {"items": {"type": "array", "items": item,
                                 "minItems": len(ids), "maxItems": len(ids)}},
        "required": ["items"],
        "additionalProperties": False,
    }


def _enum(value, allowed: tuple[str, ...]) -> str | None:
    if value is None:
        return None
    text = str(value).strip().lower()
    return text if text in allowed else "__bad__"


def _text(value) -> str | None:
    if value is None:
        return None
    text = str(value).strip()
    return text or None


def derive(row: dict) -> dict:
    """What the answers imply: expected relation, criteria branch, boundary count."""
    if row["preview"]:
        return {"expected": "forward", "basis": "forward", "boundary": 0}
    boundary = int(row["need"] == "borderline") + int(row["provided"] == "partial")
    if boundary:
        return {"expected": None, "basis": "boundary", "boundary": boundary}
    if row["need"] == "no":
        return {"expected": "weak", "basis": "weak_other", "boundary": 0}
    if row["provided"] == "full":
        basis = "weak_verify" if row["need_kind"] == "step" else "weak_other"
        return {"expected": "weak", "basis": basis, "boundary": 0}
    basis = "required_step" if row["need_kind"] == "step" else "required_meaning"
    return {"expected": "required", "basis": basis, "boundary": 0}


def validate_step1(payload: dict, expected: set[str]) -> dict[str, dict]:
    """Rows that satisfy the field coupling, keyed by lid; invalid rows are dropped.

    A dropped row is re-asked by the caller.  Inconsistency between the answers
    and ``relation`` is not a reason to drop: it is recorded (``inconsistent``)
    and becomes a risk signal, since it is the model contradicting itself.
    """
    rows = payload.get("items")
    if not isinstance(rows, list):
        return {}
    out: dict[str, dict] = {}
    for raw in rows:
        if not isinstance(raw, dict):
            continue
        lid = str(raw.get("id", ""))
        if lid not in expected or lid in out:
            continue
        preview = raw.get("preview")
        if isinstance(preview, str):
            preview = preview.strip().lower() == "true"
        if not isinstance(preview, bool):
            continue
        relation = _enum(raw.get("relation"), RELATIONS)
        if relation in (None, "__bad__"):
            continue
        need = _enum(raw.get("need"), NEED)
        kind = _enum(raw.get("need_kind"), NEED_KIND)
        provided = _enum(raw.get("provided"), PROVIDED)
        if "__bad__" in (need, kind, provided):
            continue
        if preview:
            need = kind = provided = None
        elif need is None:
            continue
        elif need == "no":
            kind = provided = None
        elif kind is None or provided is None:
            continue
        row = {
            "preview": preview, "need": need, "need_kind": kind, "provided": provided,
            "relation": relation,
            "evidence": _text(raw.get("evidence")) or "",
            "reason": _text(raw.get("reason")) or "",
            "other_side": _text(raw.get("other_side")),
            "flip_condition": _text(raw.get("flip_condition")),
            "requested_precedents": [str(x) for x in raw.get("requested_precedents") or []
                                     if isinstance(x, (str, int))],
        }
        facts = derive(row)
        row.update(facts)
        row["inconsistent"] = (
            (facts["expected"] is not None and facts["expected"] != relation)
            or (not preview and relation == "forward"))
        row["missing_boundary_text"] = bool(
            facts["boundary"] and not (row["other_side"] and row["flip_condition"]))
        out[lid] = row
    return out


# ── Step 4: precedents and pending issues ─────────────────────────────────

STEP4_HEAD = """You are reviewing your own earlier judgments of some internal links in a mathematics blog, against the precedents a human has ruled on and the open pending issues. Do not use tools and do not alter files. Return JSON only, one entry per item:
{"items":[{"id":"…","candidates":[],"precedent":"none","precedent_reason":"…","pending":"new","new_issue":{"question":"provided","statement":"…","description":"…"},"relation":"weak"}]}

CRITERIA (Korean, authoritative):
"""

STEP4_HOW = """HOW TO ANSWER
For each item:
1. Precedents. A precedent applies only when the conditions in its ruling fit this link. Choose a precedent only after reading its file. If a precedent might apply but its file is not attached below, list its id in "candidates" (at most 3) and give a provisional answer; the files will then be shown to you. Choose "none" when no precedent could fit.
2. If a precedent applies: "precedent" is its id, "relation" follows it, "pending" and "new_issue" are null.
3. If none applies, compare the link with the open pending issues. If it raises the same issue as one of them, "pending" is that id and "new_issue" is null. Otherwise "pending" is "new" and "new_issue" states the issue: "question" names which question of the criteria is unclear here (preview | need | provided); "statement" is the issue as a general question, not about this link alone; "description" is one line of at most 80 characters.
4. "relation" is your vote after this review.
Write precedent_reason, statement, and description in Korean, keep mathematical terms in English, and quote labels exactly. Every field is always present; use null where stated, [] for no candidates.
"""

STEP4_FILES_NOTE = """The files of the precedents you listed are attached under PRECEDENT FILES. Decide now: "candidates" must be [], and "precedent" is one of the attached ids or "none".
"""


def step4_prompt(*, items: list[dict], precedent_lines: list[str], pending_lines: list[str],
                 files: dict[str, str] | None = None) -> str:
    parts = [STEP4_HEAD, criteria_text(), "\n\n", STEP4_HOW, "\n"]
    parts.append("PRECEDENTS (id — description):\n"
                 + ("\n".join(precedent_lines) if precedent_lines else "(none yet)") + "\n\n")
    if files:
        parts.append(STEP4_FILES_NOTE + "\nPRECEDENT FILES:\n")
        for pid, text in files.items():
            parts.append(f"<<<{pid}\n{text}\n{pid}>>>\n\n")
    parts.append("OPEN PENDING ISSUES (id — description):\n"
                 + ("\n".join(pending_lines) if pending_lines else "(none)") + "\n\n")
    parts.append("ITEMS:\n" + json.dumps(items, ensure_ascii=False, indent=1) + "\n")
    return "".join(parts)


def step4_schema(ids: list[str]) -> dict:
    issue = {"type": ["object", "null"],
             "properties": {"question": {"type": "string", "enum": list(("preview", "need", "provided"))},
                            "statement": {"type": "string"},
                            "description": {"type": "string"}},
             "required": ["question", "statement", "description"],
             "additionalProperties": False}
    item = {
        "type": "object",
        "properties": {
            "id": {"type": "string", "enum": ids},
            "candidates": {"type": "array", "items": {"type": "string"}},
            "precedent": {"type": "string"},
            "precedent_reason": {"type": "string"},
            "pending": {"type": ["string", "null"]},
            "new_issue": issue,
            "relation": {"type": "string", "enum": list(RELATIONS)},
        },
        "required": ["id", "candidates", "precedent", "precedent_reason", "pending",
                     "new_issue", "relation"],
        "additionalProperties": False,
    }
    return {"type": "object",
            "properties": {"items": {"type": "array", "items": item,
                                     "minItems": len(ids), "maxItems": len(ids)}},
            "required": ["items"], "additionalProperties": False}


def validate_step4(payload: dict, expected: set[str], *, precedents: set[str],
                   pending: set[str], files_phase: bool) -> dict[str, dict]:
    """Rows whose ids point only at what the prompt offered."""
    out: dict[str, dict] = {}
    for raw in payload.get("items") or []:
        if not isinstance(raw, dict):
            continue
        lid = str(raw.get("id", ""))
        if lid not in expected or lid in out:
            continue
        relation = _enum(raw.get("relation"), RELATIONS)
        if relation in (None, "__bad__"):
            continue
        cands = [str(c) for c in raw.get("candidates") or [] if str(c) in precedents][:3]
        if files_phase:
            cands = []
        prec = str(raw.get("precedent") or "none")
        if prec != "none" and prec not in precedents:
            continue
        pend = raw.get("pending")
        issue = raw.get("new_issue")
        if prec != "none":
            pend, issue = None, None
        elif pend == "new":
            if not isinstance(issue, dict) or _enum(issue.get("question"), ("preview", "need", "provided")) in (None, "__bad__"):
                continue
            issue = {"question": issue["question"].strip().lower(),
                     "statement": _text(issue.get("statement")) or "",
                     "description": (_text(issue.get("description")) or "")[:80]}
            if not issue["statement"] or not issue["description"]:
                continue
        elif pend in pending:
            issue = None
        elif cands:
            pend, issue = None, None          # provisional; the files phase decides
        else:
            continue
        out[lid] = {"candidates": cands, "precedent": prec,
                    "precedent_reason": _text(raw.get("precedent_reason")) or "",
                    "pending": pend, "new_issue": issue, "relation": relation}
    return out


# ── reveal: rule A and the difference note (higher stages only) ───────────

REVEAL_HEAD = """You reviewed some internal links blind. Below, for each, are your blind review and what lower-stage models concluded in their own reviews. This call does not change any vote. Do not use tools and do not alter files. Return JSON only:
{"items":[{"id":"…","issue_check":[{"model":"S1","verdict":"same","statement":"…","description":"…","precedent":null}],"difference_note":null}]}

For every lower model that raised or joined a pending issue on the item, give one issue_check entry:
- "same": the lower model's issue and yours are the same issue in different words. Give one unified "statement" (a general question) and "description" (one line, at most 80 characters).
- "different": they are different issues. statement and description are null.
- "covered": a precedent you chose in your blind review already settles the lower model's issue. "precedent" is that id; statement and description are null.
If no lower model raised or joined an issue, issue_check is [].
"difference_note": when your blind result differs from a lower model's — in the precedent chosen or in the relation — say in one or two sentences where the readings part and why. Otherwise null. It is shown to the human who rules; it is not a vote.
Write statement, description, and difference_note in Korean, keeping mathematical terms in English.

CRITERIA (Korean, authoritative):
"""


def reveal_prompt(items: list[dict]) -> str:
    return (REVEAL_HEAD + criteria_text() + "\n\nITEMS:\n"
            + json.dumps(items, ensure_ascii=False, indent=1) + "\n")


def reveal_schema(ids: list[str]) -> dict:
    check = {"type": "object",
             "properties": {"model": {"type": "string"},
                            "verdict": {"type": "string", "enum": ["same", "different", "covered"]},
                            "statement": {"type": ["string", "null"]},
                            "description": {"type": ["string", "null"]},
                            "precedent": {"type": ["string", "null"]}},
             "required": ["model", "verdict", "statement", "description", "precedent"],
             "additionalProperties": False}
    item = {"type": "object",
            "properties": {"id": {"type": "string", "enum": ids},
                           "issue_check": {"type": "array", "items": check},
                           "difference_note": {"type": ["string", "null"]}},
            "required": ["id", "issue_check", "difference_note"],
            "additionalProperties": False}
    return {"type": "object",
            "properties": {"items": {"type": "array", "items": item,
                                     "minItems": len(ids), "maxItems": len(ids)}},
            "required": ["items"], "additionalProperties": False}


def validate_reveal(payload: dict, expected: set[str]) -> dict[str, dict]:
    out: dict[str, dict] = {}
    for raw in payload.get("items") or []:
        if not isinstance(raw, dict) or str(raw.get("id")) not in expected:
            continue
        checks = []
        for c in raw.get("issue_check") or []:
            if not isinstance(c, dict) or c.get("verdict") not in ("same", "different", "covered"):
                continue
            checks.append({"model": str(c.get("model", "")), "verdict": c["verdict"],
                           "statement": _text(c.get("statement")),
                           "description": (_text(c.get("description")) or "")[:80] or None,
                           "precedent": _text(c.get("precedent"))})
        out[str(raw["id"])] = {"issue_check": checks,
                               "difference_note": _text(raw.get("difference_note"))}
    return out
