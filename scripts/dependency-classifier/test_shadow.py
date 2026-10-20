#!/usr/bin/env python3
"""Tests for the shadow re-judging pipeline that need no model call.

State goes to a temporary directory (DEPENDENCY_SHADOW_STATE_DIR) and the shadow
ledger to a temporary file, so nothing under ~/.local/state or _data is touched.
"""
from __future__ import annotations

import json
import os
import sys
import tempfile
import time
import unittest
from pathlib import Path
from unittest.mock import patch

TMP = tempfile.mkdtemp(prefix="shadow-test-")
os.environ["DEPENDENCY_SHADOW_STATE_DIR"] = TMP
os.environ["DEPENDENCY_SHADOW_BOOK_DIR"] = str(Path(TMP) / "book")
HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
sys.path.insert(0, str(HERE.parent / "dashboard"))

import dependency_classifier as dc  # noqa: E402
import shadow_book as book  # noqa: E402
import shadow_features as feat  # noqa: E402
import shadow_models as models  # noqa: E402
import shadow_pipeline as pipe  # noqa: E402
import shadow_prompts as sp  # noqa: E402
import shadow_risk as risk  # noqa: E402
import shadow_store as store  # noqa: E402

store.LEDGER_PATH = Path(TMP) / "link_relations_next.yml"
store.LOCK_PATH = Path(TMP) / "state.lock"
store.TICK_LOCK_PATH = Path(TMP) / "tick.lock"
store.BOOK_LOCK_PATH = Path(TMP) / "book.lock"
for name in ("PRECEDENTS_DIR", "PENDING_DIR", "HISTORY_DIR"):
    assert str(getattr(store, name)).startswith(TMP), name


def step1(**kw) -> dict:
    base = {"id": "aaaaa", "preview": False, "need": "yes", "need_kind": "step",
            "provided": "none", "relation": "required", "evidence": "문장", "reason": "이유",
            "other_side": None, "flip_condition": None, "requested_precedents": []}
    base.update(kw)
    return base


class Step1ValidationTest(unittest.TestCase):
    def check(self, **kw):
        rows = sp.validate_step1({"items": [step1(**kw)]}, {"aaaaa"})
        return rows.get("aaaaa")

    def test_required_by_the_table(self):
        row = self.check()
        self.assertEqual((row["expected"], row["basis"], row["boundary"]), ("required", "required_step", 0))
        self.assertFalse(row["inconsistent"])

    def test_provided_full_is_weak_verify(self):
        row = self.check(provided="full", relation="weak")
        self.assertEqual(row["basis"], "weak_verify")

    def test_need_no_drops_kind_and_provided(self):
        row = self.check(need="no", need_kind="step", provided="full", relation="weak")
        self.assertIsNone(row["need_kind"])
        self.assertIsNone(row["provided"])
        self.assertEqual(row["basis"], "weak_other")

    def test_preview_is_forward(self):
        row = self.check(preview=True, relation="forward", need=None, need_kind=None, provided=None)
        self.assertEqual(row["basis"], "forward")

    def test_contradiction_is_kept_and_flagged(self):
        row = self.check(provided="full", relation="required")
        self.assertTrue(row["inconsistent"])
        row = self.check(relation="forward")
        self.assertTrue(row["inconsistent"])

    def test_boundary_needs_explanations(self):
        row = self.check(need="borderline", relation="weak")
        self.assertEqual(row["boundary"], 1)
        self.assertTrue(row["missing_boundary_text"])
        row = self.check(need="borderline", provided="partial", relation="weak",
                         other_side="반대", flip_condition="조건")
        self.assertEqual(row["boundary"], 2)
        self.assertFalse(row["missing_boundary_text"])

    def test_invalid_rows_are_dropped(self):
        self.assertIsNone(self.check(need="maybe"))
        self.assertIsNone(self.check(need="yes", need_kind=None))
        self.assertIsNone(self.check(relation="ambiguous"))
        self.assertEqual(sp.validate_step1({"items": [step1(id="zzzzz")]}, {"aaaaa"}), {})


class JsonRepairTest(unittest.TestCase):
    def test_latex_in_strings(self):
        raw = '{"items":[{"id":"x","evidence":"$\\im f$와 \\[집합론\\] 그리고 $\\theta$, \\rightarrow"}]}'
        value = models.parse_model_json(raw)
        self.assertEqual(value["items"][0]["evidence"], "$\\im f$와 \\[집합론\\] 그리고 $\\theta$, \\rightarrow")

    def test_valid_json_untouched(self):
        raw = '```json\n{"items":[{"id":"x","evidence":"a\\nb \\"q\\" \\\\alpha"}]}\n```'
        self.assertEqual(models.parse_model_json(raw)["items"][0]["evidence"], 'a\nb "q" \\alpha')

    def test_raw_newline_inside_string(self):
        raw = '{"items":[{"id":"x","evidence":"첫 줄\n둘째 줄"}]}'
        self.assertEqual(models.parse_model_json(raw)["items"][0]["evidence"], "첫 줄\n둘째 줄")


class QuoteScoreTest(unittest.TestCase):
    SOURCE = ("따라서 [§군, ⁋정의 3](/ko/math/groups#def3){: data-lid=\"abcde\" }에 의하여 "
              "$$f(xy^{-1})=f(x)f(y)^{-1}$$ 이다. 이로부터 \\[명제\\]가 따라온다.")

    def test_escapes_markup_and_delimiters_normalised(self):
        quote = "따라서 §군, ⁋정의 3에 의하여 $f(xy^{-1})=f(x)f(y)^{-1}$ 이다."
        self.assertEqual(feat.quote_score(quote, self.SOURCE), 1.0)

    def test_paraphrase_scores_low(self):
        self.assertLess(feat.quote_score("완전히 다른 문장이 여기에 있다", self.SOURCE), 0.6)


class Step4ValidationTest(unittest.TestCase):
    def test_offered_ids_only(self):
        payload = {"items": [
            {"id": "a", "candidates": [], "precedent": "P-0009", "precedent_reason": "", "pending": None,
             "new_issue": None, "relation": "weak"},
            {"id": "b", "candidates": [], "precedent": "P-0001", "precedent_reason": "r", "pending": None,
             "new_issue": None, "relation": "weak"},
            {"id": "c", "candidates": [], "precedent": "none", "precedent_reason": "", "pending": "new",
             "new_issue": {"question": "provided", "statement": "~인가?", "description": "한 줄"},
             "relation": "required"},
            {"id": "d", "candidates": [], "precedent": "none", "precedent_reason": "", "pending": "Q-0003",
             "new_issue": None, "relation": "required"},
            {"id": "e", "candidates": ["P-0001"], "precedent": "none", "precedent_reason": "",
             "pending": None, "new_issue": None, "relation": "weak"},
        ]}
        rows = sp.validate_step4(payload, set("abcde"), precedents={"P-0001"}, pending={"Q-0003"},
                                 files_phase=False)
        self.assertNotIn("a", rows)
        self.assertEqual(rows["b"]["precedent"], "P-0001")
        self.assertEqual(rows["c"]["new_issue"]["question"], "provided")
        self.assertEqual(rows["d"]["pending"], "Q-0003")
        self.assertEqual(rows["e"]["candidates"], ["P-0001"])
        files = sp.validate_step4(payload, {"e"}, precedents={"P-0001"}, pending=set(), files_phase=True)
        self.assertNotIn("e", files)        # the files phase must decide, not ask again


def link_rec(source: str, target: str, votes: dict, *, same_page=False, precedent=None) -> dict:
    stages = {}
    for stage, rel in votes.items():
        row = sp.validate_step1({"items": [step1(relation=rel, provided="none" if rel == "required" else "full")]},
                                {"aaaaa"})["aaaaa"]
        row["quote_score"] = 1.0
        s = {"step1": row}
        if precedent:
            s["step4"] = {"relation": rel, "precedent": precedent.get(stage, "none"),
                          "precedent_reason": "", "pending": None, "new_issue": None, "candidates": []}
        stages[stage] = s
    return {"source": source, "line": 1, "link": "[x](y)", "target": target,
            "features": {"same_page": same_page}, "stages": stages}


class FinalizeTest(unittest.TestCase):
    def test_unanimous_split_and_precedent_split(self):
        record = {"unit": "u", "links": {
            "l1": link_rec("a.md", "/ko/math/x#def1", {"S1": "weak", "S2": "weak", "S3": "weak"}),
            "l2": link_rec("a.md", "/ko/math/x#def2", {"S1": "weak", "S2": "required", "S3": "weak"}),
            "l3": link_rec("a.md", "/ko/math/y", {"S1": "weak", "S2": "weak", "S3": "weak"},
                           precedent={"S1": "P-0001", "S2": "none", "S3": "P-0001"}),
        }}
        records, queue = {}, store.load_queue()
        result = pipe.finalize(record, ["l1", "l2", "l3"], records, queue, time.time() - 30 * 86400)
        self.assertEqual(result["finalized"], 1)
        self.assertEqual(result["to_human"], 2)
        self.assertEqual(records["l1"].relation, "weak")
        self.assertIn("l2", queue["human"])
        self.assertIn("l3", queue["human"])           # precedents disagreed
        self.assertTrue(queue["human"]["l2"]["decisive"])

    def test_decisive_only_without_another_required_in_pair(self):
        links = {
            "r": {**link_rec("a.md", "/ko/math/x#def1", {"S1": "required"}), "final": {"relation": "required"}},
            "w": link_rec("a.md", "/ko/math/x#def2", {"S1": "weak"}),
            "s": link_rec("a.md", "#def3", {"S1": "weak"}, same_page=True),
        }
        self.assertFalse(pipe.decisive("w", links["w"], links))
        self.assertFalse(pipe.decisive("s", links["s"], links))
        self.assertTrue(pipe.decisive("r", links["r"], links))

    def test_audit_draw_is_deterministic(self):
        rec = link_rec("a.md", "/ko/math/x", {"S1": "weak", "S2": "weak", "S3": "weak"})
        first = [pipe.audit_draw(f"l{i:04d}", rec, {f"l{i:04d}": rec}, 0) for i in range(2000)]
        again = [pipe.audit_draw(f"l{i:04d}", rec, {f"l{i:04d}": rec}, 0) for i in range(2000)]
        self.assertEqual(first, again)
        rate = sum(1 for x in first if x) / len(first)
        self.assertTrue(0.04 < rate < 0.12, rate)    # decisive rate, weak_verify oversampled


class RiskTest(unittest.TestCase):
    def test_rule_flags(self):
        row = sp.validate_step1({"items": [step1(need="borderline", relation="weak")]}, {"aaaaa"})["aaaaa"]
        row["quote_score"] = 1.0
        self.assertTrue(risk.score("S1", row, {}, {})["flagged"])
        clean = sp.validate_step1({"items": [step1()]}, {"aaaaa"})["aaaaa"]
        clean["quote_score"] = 1.0
        self.assertFalse(risk.score("S1", clean, {}, {})["flagged"])
        clean["quote_score"] = 0.3
        self.assertEqual(risk.score("S1", clean, {}, {})["reasons"], ["quote"])

    def test_fit_ranks_and_flags_a_share(self):
        import random
        rnd = random.Random(1)
        rows = []
        for _ in range(600):
            boundary = rnd.random() < 0.3
            row = sp.validate_step1({"items": [step1(need="borderline" if boundary else "yes",
                                                     other_side="x", flip_condition="y")]}, {"aaaaa"})["aaaaa"]
            row["quote_score"] = 1.0
            overturned = int(rnd.random() < (0.5 if boundary else 0.05))
            rows.append((risk.vector(row, {}), overturned, row))
        with patch.object(risk.store, "CALIBRATION_PATH", Path(TMP) / "cal.json"):
            model = risk.fit({"S1": [(v, o) for v, o, _ in rows]})
            self.assertIn("S1", model)
            flagged = [risk.score("S1", r, {}, model)["flagged"] for _, _, r in rows]
            share = sum(flagged) / len(flagged)
            self.assertTrue(0.2 <= share <= 0.45, share)


class BookTest(unittest.TestCase):
    def test_issue_lifecycle(self):
        q1 = book.raise_issue(question="provided", statement="~인가?", description="첫 쟁점",
                              raised_by="S1", lid="l1")
        q2 = book.raise_issue(question="provided", statement="~인가? (다른 말)", description="둘째",
                              raised_by="S2", lid="l2")
        book.attach(q1, "l3")
        book.restate(q1, "통합한 진술", "통합 설명")
        book.merge(q2, q1)
        e1, e2 = book.get(q1), book.get(q2)
        self.assertEqual(e1.meta["links"], ["l1", "l3", "l2"])
        self.assertIn("통합한 진술", e1.body)
        self.assertEqual(e1.description, "통합 설명")
        self.assertEqual(e2.status, "merged")
        self.assertEqual([e.id for e in book.live("Q")], [q1])
        self.assertTrue((store.PENDING_DIR / "INDEX.md").read_text().count(q1))
        self.assertTrue(list(store.HISTORY_DIR.glob(f"{q1}.*.md")))
        self.assertEqual(book.open_for("l2").id, q1)


class MergeUnitRecordTest(unittest.TestCase):
    def test_keeps_links_written_by_others(self):
        store.save_unit_record("h1", {"links": {"a": {"final": {"relation": "weak", "by": "human"}}}})
        mine = {"unit": "u", "round": ["b"], "links": {"a": {"stale": True}, "b": {"new": True}}}
        fresh = store.merge_unit_record("h1", mine, ["b"])
        self.assertEqual(fresh["links"]["a"], {"final": {"relation": "weak", "by": "human"}})
        self.assertEqual(fresh["links"]["b"], {"new": True})


class DashboardFlowTest(unittest.TestCase):
    def setUp(self):
        import shadow_api
        self.api = shadow_api
        rec = link_rec("a.md", "/ko/math/x", {"S1": "weak", "S2": "required", "S3": "weak"})
        import shadow_units as units
        self.h = units.unit_hash("unit-key")
        store.save_unit_record(self.h, {"unit": "unit-key", "links": {"zz001": rec, "zz002": {
            **link_rec("a.md", "/ko/math/y", {"S1": "weak", "S2": "weak", "S3": "weak"}),
            "final": {"relation": "weak", "by": "unanimous"}}}})
        queue = store.load_queue()
        queue["human"] = {"zz001": {"unit": "unit-key", "votes": {}, "issues": []}}
        queue["audit"] = {"zz002": {"unit": "unit-key", "stratum": "decisive"}}
        queue["settled"] = {}
        queue["digest"] = []
        store.save_queue(queue)
        store.save_ledger({})

    def test_rule_and_reopen(self):
        self.api.rule("zz001", "required", "설명")
        self.assertEqual(store.load_ledger()["zz001"].relation, "required")
        queue = store.load_queue()
        self.assertNotIn("zz001", queue["human"])
        self.assertEqual(queue["digest"][0]["kind"], "ruling_note")
        self.api.reopen("zz001")
        self.assertNotIn("zz001", store.load_ledger())
        queue = store.load_queue()
        self.assertIn("zz001", queue["human"])
        self.assertEqual(queue["digest"], [])

    def test_audit_needs_explanation_to_differ(self):
        out = self.api.audit("zz002", "required")
        self.assertTrue(out["need_explanation"])
        self.assertIn("zz002", store.load_queue()["audit"])
        out = self.api.audit("zz002", "required", "만장일치가 진술의 제공 여부를 잘못 읽었다")
        self.assertFalse(out["match"])
        self.assertEqual(store.load_ledger()["zz002"].relation, "required")
        self.assertEqual(store.load_queue()["digest"][-1]["kind"], "audit_error")

    def test_audit_match(self):
        out = self.api.audit("zz002", "weak")
        self.assertTrue(out["match"])
        self.assertNotIn("zz002", store.load_ledger())     # unchanged: nothing written


class LedgerFormatTest(unittest.TestCase):
    def test_same_format_as_production(self):
        store.save_ledger({"0a1b2": dc.ledger.Record("weak", True)})
        text = store.LEDGER_PATH.read_text(encoding="utf-8")
        self.assertIn('"0a1b2": {relation: weak, reviewed: true}', text)
        self.assertEqual(dc.ledger.load(store.LEDGER_PATH)["0a1b2"].relation, "weak")



class EndToEndFakeModelTest(unittest.TestCase):
    """S1→S2→S3→finalize on a real post, with scripted model answers."""

    POST = HERE.parents[1] / "_posts/Math/Algebraic_Structures/ko/2021-09-08-Group_Homomorphisms.md"

    @staticmethod
    def _items(prompt: str) -> list[dict]:
        return json.loads(prompt.rsplit("ITEMS:\n", 1)[1])

    def fake_call(self, stage, prompt, schema=None):
        items = self._items(prompt)
        if prompt.startswith(sp.STEP1_HEAD[:40]):
            rows = []
            for i, item in enumerate(items):
                odd = stage == "S1" and i == 0
                rows.append(step1(id=item["id"], need="borderline" if odd else "yes",
                                  relation="weak" if odd else "required",
                                  other_side="x" if odd else None, flip_condition="y" if odd else None,
                                  evidence=item["link"]))
            return {"items": rows}, {"items": len(rows)}
        if prompt.startswith(sp.STEP4_HEAD[:40]):
            return {"items": [{"id": it["id"], "candidates": [], "precedent": "none",
                               "precedent_reason": "판례 없음", "pending": "new",
                               "new_issue": {"question": "need", "statement": "~인가?",
                                             "description": f"{stage} 쟁점"},
                               "relation": "weak" if stage == "S1" else "required"}
                              for it in items]}, {}
        return {"items": [{"id": it["id"], "issue_check": [
            {"model": low["model"], "verdict": "same", "statement": "통합 진술",
             "description": "통합 쟁점", "precedent": None} for low in it["lower"]],
            "difference_note": "S1 은 필요를 경계로 봤다"} for it in items]}, {}

    def test_round(self):
        import shadow_tick as tick
        import shadow_units as units
        paths = tick.find_unit(str(self.POST)) if hasattr(tick, "find_unit") else None
        if paths is None:
            for p in units.all_units():
                if self.POST in p:
                    paths = p
        state = {"units": {}, "started_at": time.time() - 30 * 86400}
        with patch.object(models, "call", side_effect=self.fake_call), \
                patch.object(models, "available", return_value=True), \
                patch.object(tick, "dirty_paths", return_value=[]), \
                patch.object(tick, "commit_outputs", return_value=True):
            unit = units.load_unit(paths)
            self.assertFalse(unit.waiting)
            tick.run(state, paths, "S1", unit, "new", commit=False)
            entry = state["units"][unit.key]
            self.assertEqual(entry["next"], "S2")
            for stage in ("S2", "S3"):
                tick.run(state, paths, stage, units.load_unit(paths), "continue", commit=False)
            self.assertIsNone(entry["next"])
        ledger_now = store.load_ledger()
        queue = store.load_queue()
        lids = unit.lids
        first = lids[0]
        self.assertIn(first, queue["human"])
        self.assertEqual(set(ledger_now), set(lids[1:]) | (set(ledger_now) - set(lids)))
        self.assertTrue(all(ledger_now[l].relation == "required" for l in lids[1:]))
        record = store.load_unit_record(units.unit_hash(unit.key))
        s2 = record["links"][first]["stages"]["S2"]
        self.assertTrue(s2.get("forced"))                    # rule C: S1 went through Step 4
        self.assertEqual(s2["step4"]["reveal"]["difference_note"], "S1 은 필요를 경계로 봤다")
        open_q = [e for e in book.live("Q") if first in (e.meta.get("links") or [])]
        self.assertEqual(len(open_q), 1)                     # S2/S3 issues merged into S1's
        self.assertEqual(open_q[0].description, "통합 쟁점")


class ScopeTest(unittest.TestCase):
    def test_drafts_and_revising_posts_are_left_alone(self):
        from types import SimpleNamespace
        import shadow_tick
        d = Path(tempfile.mkdtemp(prefix="scope-", dir=TMP))
        heads = {"live": "title: a", "draft": "title: b\npublished: false",
                 "rev": "title: c\nrevising: true", "en": "title: d"}
        paths = {}
        for name, head in heads.items():
            paths[name] = d / f"{name}.md"
            paths[name].write_text(f"---\n{head}\n---\nbody\n", encoding="utf-8")
        posts = [SimpleNamespace(path=p, published=name != "draft") for name, p in paths.items()]
        key = lambda ps: "+".join(p.stem for p in ps)  # noqa: E731
        with patch.object(dc, "_POSTS", posts), patch.object(dc, "unit_key", key):
            skip = shadow_tick.out_of_scope(
                [[paths["live"]], [paths["draft"]], [paths["rev"], paths["en"]]])
        self.assertEqual(skip, {"draft", "rev+en"})


if __name__ == "__main__":
    unittest.main()
