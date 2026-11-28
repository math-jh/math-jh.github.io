#!/usr/bin/env python3
"""Tests for the link-dependency pipeline that need no model call.

State goes to a temporary directory (DEPENDENCY_STATE_DIR) and the
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

TMP = tempfile.mkdtemp(prefix="linkdep-test-")
os.environ["DEPENDENCY_STATE_DIR"] = TMP
os.environ["DEPENDENCY_BOOK_DIR"] = str(Path(TMP) / "book")
# Rounds finalize and call core.notify; tests must not reach the phone (or the digest).
os.environ["DEPENDENCY_NOTIFY_BIN"] = "/bin/true"
# S1's Gemini API path must not reach the real gemini-credit (and the shared balance).
os.environ["GEMINI_CREDIT_BIN"] = str(Path(TMP) / "no-gemini-credit")
HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
sys.path.insert(0, str(HERE.parent / "dashboard"))

import linkdep_core as core  # noqa: E402
import linkdep_book as book  # noqa: E402
import linkdep_features as feat  # noqa: E402
import linkdep_models as models  # noqa: E402
import linkdep_pipeline as pipe  # noqa: E402
import linkdep_prompts as sp  # noqa: E402
import linkdep_risk as risk  # noqa: E402
import linkdep_store as store  # noqa: E402

store.LEDGER_PATH = Path(TMP) / "link_relations.yml"
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
        bumped = []
        with patch.object(pipe.book, "bump_applied", lambda pid, lid: bumped.append((pid, lid))):
            result = pipe.finalize(record, ["l1", "l2", "l3"], records, queue, time.time() - 30 * 86400)
        self.assertEqual(result["finalized"], 2)
        self.assertEqual(result["to_human"], 1)
        self.assertEqual(records["l1"].relation, "weak")
        self.assertIn("l2", queue["human"])
        self.assertEqual(records["l3"].relation, "weak")    # precedents disagreed, votes did not
        self.assertEqual(bumped, [("P-0001", "l3")])         # cited by two of three
        self.assertTrue(queue["human"]["l2"]["decisive"])

    def test_one_model_citation_in_a_split_is_not_counted(self):
        record = {"unit": "u", "links": {
            "l1": link_rec("a.md", "/ko/math/y", {"S1": "weak", "S2": "weak", "S3": "weak"},
                           precedent={"S1": "P-0001", "S2": "none", "S3": "P-0002"}),
        }}
        bumped = []
        with patch.object(pipe.book, "bump_applied", lambda pid, lid: bumped.append(pid)):
            pipe.finalize(record, ["l1"], {}, store.load_queue(), time.time() - 30 * 86400)
        self.assertEqual(bumped, [])

    def test_promote_copies_principle_into_criteria(self):
        import linkdep_digest as digest
        criteria = Path(TMP) / "criteria.md"
        criteria.write_text("### 관계\n본문\n\n### 승격된 원칙\n(아직 없다)\n", encoding="utf-8")
        for pid, extra in (("P-0901", "## 원칙 초안\n첫째 원칙\n이어지는 줄.\n"), ("P-0902", "")):
            book.write(pid, {"id": pid, "status": "active", "description": "d", "question": "need"},
                       f"## 쟁점\nq\n\n## 판정\nr\n\n{extra}")
        with patch.object(digest.sp, "CRITERIA_PATH", criteria):
            with self.assertRaises(ValueError):
                digest.apply_consolidation("promote", ["P-0901", "P-0902"])   # P-0902 has no draft
            self.assertEqual(book.get("P-0901").status, "active")             # nothing changed
            digest.apply_consolidation("promote", ["P-0901"])
            digest.apply_consolidation("promote", ["P-0901"])                 # idempotent
        self.assertEqual(criteria.read_text(encoding="utf-8"),
                         "### 관계\n본문\n\n### 승격된 원칙\n- (P-0901) 첫째 원칙 이어지는 줄.\n")
        self.assertEqual(book.get("P-0901").status, "promoted")

    def test_merge_goes_through_a_draft_that_absorbs_the_rest(self):
        import linkdep_digest as digest
        for pid, expl in (("P-0911", "첫 설명"), ("P-0912", "둘째 설명")):
            book.write(pid, {"id": pid, "status": "active", "description": pid, "question": "provided"},
                       f"## 쟁점\nq\n\n## 판정\n{pid} 판정\n\n## 이유\nr\n\n## 사용자 설명 (원문)\n{expl}\n\n"
                       f"## 대표 예시 (최대 2개)\n- lid `ab{pid[-3:]}` — e — weak\n")
        out = digest.apply_consolidation("merge", ["P-0911", "P-0912"])
        self.assertTrue(out["queued"])
        self.assertEqual(book.get("P-0912").status, "active")              # nothing yet
        queue = store.load_queue()
        queue["digest"] = [j for j in queue["digest"] if j.get("kind") == "merge"]
        store.save_queue(queue)
        reply = {"action": "merge", "question": "provided", "issue": "합친 쟁점", "ruling": "양쪽 판정",
                 "relation": None, "reason": "근거", "description": "합친 판례", "principle": "합친 원칙",
                 "examples": ["ab911", "zzzzz"], "note": "두 쪽을 합쳤다"}
        with patch.object(digest.models, "available", return_value=True), \
                patch.object(digest.models, "call", return_value=(reply, {})):
            self.assertTrue(digest.run_one())
        draft = store.load_queue()["drafts"][-1]
        self.assertEqual(draft["draft"]["action"], "merge")
        self.assertEqual(draft["draft"]["examples"], ["ab911"])           # only lids the precedents list
        digest.apply_draft(draft["id"])
        keep, gone = book.get("P-0911"), book.get("P-0912")
        self.assertEqual(gone.status, "superseded")
        self.assertEqual(gone.meta["superseded_by"], "P-0911")
        self.assertIn("양쪽 판정", keep.body)
        self.assertIn("첫 설명", keep.body)
        self.assertIn("(P-0912) 둘째 설명", keep.body)
        self.assertEqual(keep.meta["absorbs"], ["P-0912"])

    def _precedent(self, pid, status="active", principle="원칙"):
        return book.write(pid, {"id": pid, "status": status, "description": pid, "question": "provided"},
                          f"## 쟁점\nq\n\n## 판정\n{pid} 판정\n\n## 이유\nr\n\n"
                          f"## 사용자 설명 (원문)\n(없음)\n\n## 원칙 초안\n{principle}\n")

    def test_proposals_never_share_a_precedent(self):
        import linkdep_digest as digest
        for pid in ("P-0921", "P-0922", "P-0923", "P-0924"):
            self._precedent(pid)
        self._precedent("P-0925", status="promoted")
        got = digest.clean_proposals([
            {"kind": "merge", "ids": ["P-0921", "P-0922"]},      # P-0921 is promoted below
            {"kind": "merge", "ids": ["P-0923", "P-0924"]},
            {"kind": "merge", "ids": ["P-0924", "P-0923"]},      # the same merge again
            {"kind": "merge", "ids": ["P-0923", "P-0925"]},      # P-0925 is not live
            {"kind": "promote", "ids": ["P-0921", "P-0925"]},
            {"kind": "other", "ids": ["P-0922"]}, "junk"])
        self.assertEqual([(c["kind"], c["ids"]) for c in got],
                         [("promote", ["P-0921"]), ("merge", ["P-0923", "P-0924"])])

    def test_merge_is_queued_once_and_a_dead_one_is_dropped(self):
        import linkdep_digest as digest
        for pid in ("P-0931", "P-0932", "P-0933"):
            self._precedent(pid)
        queue = store.load_queue()
        queue["digest"], queue["drafts"] = [], []
        store.save_queue(queue)
        self.assertTrue(digest.apply_consolidation("merge", ["P-0931", "P-0932"])["queued"])
        self.assertIsNone(digest.apply_consolidation("merge", ["P-0932", "P-0931"])["queued"])
        with self.assertRaises(ValueError):
            digest.apply_consolidation("merge", ["P-0932", "P-0933"])    # P-0932 already waits
        self.assertEqual(len(store.load_queue()["digest"]), 1)
        book.set_status("P-0932", "promoted")
        with self.assertRaises(ValueError):
            digest.apply_consolidation("merge", ["P-0932", "P-0933"])    # not live
        with patch.object(digest.models, "available", return_value=True), \
                patch.object(digest.models, "call", side_effect=AssertionError("no call")):
            self.assertTrue(digest.run_one())
        queue = store.load_queue()
        self.assertEqual((queue["digest"], queue["drafts"]), ([], []))

    def test_stale_draft_is_drafted_again(self):
        import linkdep_digest as digest
        self._precedent("P-0941")
        job = {"id": "J-1", "kind": "ruling_note", "rulings": {}, "explanation": "설명"}
        draft = digest._clean({"action": "amend", "precedent": "P-0941", "issue": "i", "ruling": "새 판정",
                               "reason": "r", "description": "d", "principle": "p"}, set(), set())
        queue = store.load_queue()
        queue["digest"], queue["drafts"] = [], [{"id": "D-1", "job": job, "draft": draft}]
        store.save_queue(queue)
        self._precedent("P-0941", principle="그새 고친 원칙")              # another draft landed first
        out = digest.apply_draft("D-1")
        self.assertEqual(out, {"written": None, "requeued": ["P-0941"]})
        self.assertIn("그새 고친 원칙", book.get("P-0941").body)             # not overwritten
        queue = store.load_queue()
        self.assertEqual(queue["drafts"], [])
        self.assertEqual([j["id"] for j in queue["digest"]], ["J-1"])
        queue["digest"] = []
        store.save_queue(queue)

    def test_rewriting_a_promoted_precedent_rewrites_its_criteria_line(self):
        import linkdep_digest as digest
        criteria = Path(TMP) / "criteria2.md"
        criteria.write_text("### 승격된 원칙\n- (P-0950) 남의 줄\n- (P-0951) 옛 원칙\n\n### 뒤\n끝\n",
                            encoding="utf-8")
        self._precedent("P-0951", status="promoted", principle="옛 원칙")
        job = {"id": "J-2", "kind": "ruling_note", "rulings": {}, "explanation": ""}
        with patch.object(digest.sp, "CRITERIA_PATH", criteria):
            for n, (action, choice) in enumerate((("amend", None), ("conflict", "supersede"))):
                draft = digest._clean({"action": action, "precedent": "P-0951", "issue": "i",
                                       "ruling": "r", "reason": "r", "description": "d",
                                       "principle": "새 원칙"}, set(), set())
                queue = store.load_queue()
                queue["drafts"] = [{"id": f"D-{n}", "job": job, "draft": draft}]
                store.save_queue(queue)
                written = digest.apply_draft(f"D-{n}", choice=choice)["written"]
                if action == "amend":
                    self.assertEqual(book.get("P-0951").status, "promoted")
                    self.assertEqual(criteria.read_text(encoding="utf-8"),
                                     "### 승격된 원칙\n- (P-0950) 남의 줄\n- (P-0951) 새 원칙\n\n### 뒤\n끝\n")
            self.assertNotEqual(written, "P-0951")
            self.assertEqual(book.get("P-0951").status, "superseded")
            self.assertEqual(criteria.read_text(encoding="utf-8"),
                             "### 승격된 원칙\n- (P-0950) 남의 줄\n\n### 뒤\n끝\n")
            with self.assertRaises(ValueError):
                digest.apply_consolidation("promote", ["P-0951"])            # superseded stays so

    def test_provisional_outcome_is_the_two_one_majority(self):
        self.assertEqual(risk.provisional_outcome({"S1": "weak", "S2": "required", "S3": "required"}),
                         "required")
        self.assertIsNone(risk.provisional_outcome({"S1": "weak", "S2": "required", "S3": "forward"}))
        self.assertIsNone(risk.provisional_outcome({"S1": "weak", "S2": "weak", "S3": None}))

    def test_lone_s1(self):
        lone = link_rec("a.md", "/ko/math/x", {"S1": "weak", "S2": "required", "S3": "required"})
        self.assertTrue(pipe.lone_s1(lone))
        reviewed = link_rec("a.md", "/ko/math/x", {"S1": "weak", "S2": "required", "S3": "required"},
                            precedent={"S1": "none"})
        self.assertFalse(pipe.lone_s1(reviewed))             # S1 already ran Step 4
        self.assertFalse(pipe.lone_s1(
            link_rec("a.md", "/ko/math/x", {"S1": "required", "S2": "weak", "S3": "required"})))
        self.assertFalse(pipe.lone_s1(
            link_rec("a.md", "/ko/math/x", {"S1": "weak", "S2": "weak", "S3": "weak"})))

    def test_late_s1_step4_settles_the_vote(self):
        record = {"unit": "u", "links": {
            "l1": link_rec("a.md", "/ko/math/x#def1", {"S1": "weak", "S2": "required", "S3": "required"}),
            "l2": link_rec("a.md", "/ko/math/x#def2", {"S1": "weak", "S2": "weak", "S3": "weak"}),
        }}

        class FakeUnit:
            def link(self, lid):
                return object()

        row = {"relation": "required", "precedent": "P-0001", "precedent_reason": "",
               "pending": None, "new_issue": None, "candidates": []}
        seen = []
        with patch.object(pipe, "step4_items", lambda u, r, stage, lids: (seen.append((stage, lids)), lids)[1]), \
                patch.object(pipe, "step4_batches", lambda items: [items]), \
                patch.object(pipe, "run_step4", lambda stage, batch: ({lid: dict(row) for lid in batch}, [{}])), \
                patch.object(pipe, "_record_issue", lambda *a: None):
            out = pipe.run_late_s1(FakeUnit(), record, ["l1", "l2"])
        self.assertEqual(seen, [("S1", ["l1"])])
        self.assertEqual(out, {"late_s1": 1, "late_s1_changed": 1})
        self.assertTrue(record["links"]["l1"]["stages"]["S1"]["late"])
        records, queue = {}, store.load_queue()
        with patch.object(pipe.book, "bump_applied", lambda pid, lid: None):
            result = pipe.finalize(record, ["l1", "l2"], records, queue, time.time() - 30 * 86400)
        self.assertEqual(result["finalized"], 2)
        self.assertEqual(records["l1"].relation, "required")

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
        import linkdeps_api
        self.api = linkdeps_api
        rec = link_rec("a.md", "/ko/math/x", {"S1": "weak", "S2": "required", "S3": "weak"})
        import linkdep_units as units
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
        store.save_ledger({"0a1b2": core.ledger.Record("weak", True)})
        text = store.LEDGER_PATH.read_text(encoding="utf-8")
        self.assertIn('"0a1b2": {relation: weak, reviewed: true}', text)
        self.assertEqual(core.ledger.load(store.LEDGER_PATH)["0a1b2"].relation, "weak")



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
        import linkdep_tick as tick
        import linkdep_units as units
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
    def test_only_local_posts_are_left_alone(self):
        import linkdep_tick
        d = Path(tempfile.mkdtemp(prefix="scope-", dir=TMP))
        heads = {"live": "title: a", "draft": "title: b\npublished: false",
                 "rev": "title: c\nrevising: true", "en": "title: d",
                 "local": "title: e", "local_en": "title: f", "half": "title: g"}
        paths = {}
        for name, head in heads.items():
            paths[name] = d / f"{name}.md"
            paths[name].write_text(f"---\n{head}\n---\nbody\n", encoding="utf-8")
        tracked = {str(paths[name]) for name in ("live", "draft", "rev", "en", "half")}
        key = lambda ps: "+".join(p.stem for p in ps)  # noqa: E731
        with patch.object(store, "ROOT", Path("/")), patch.object(core, "unit_key", key), \
                patch.object(linkdep_tick, "tracked_posts",
                             return_value={p.lstrip("/") for p in tracked}):
            skip = linkdep_tick.out_of_scope(
                [[paths["live"]], [paths["draft"]], [paths["rev"], paths["en"]],
                 [paths["local"]], [paths["half"], paths["local_en"]]])
        self.assertEqual(skip, {"local", "half+local_en"})

    def test_recheck_drops_links_of_paused_posts(self):
        from types import SimpleNamespace
        import linkdep_tick
        import linkdep_units as units
        paths = [EndToEndFakeModelTest.POST]
        key = core.unit_key(paths)
        record = {"unit": key, "links": {"zzzzz": {"final": {"relation": "weak"}}}}
        with store.lock(5):
            queue = store.load_queue()
            queue["recheck"] = [{"lid": "zzzzz", "precedent": "P-0001", "created": 0}]
            store.save_queue(queue)
        with patch.object(units, "all_units", return_value=[paths]), \
                patch.object(store, "load_unit_record", return_value=record), \
                patch.object(units, "load_unit", return_value=SimpleNamespace(link=lambda lid: {})), \
                patch.object(linkdep_tick, "out_of_scope", return_value={key}), \
                patch.object(linkdep_tick, "fill_complete", return_value=True), \
                patch.object(models, "available", return_value=True), \
                patch.object(models, "call", side_effect=AssertionError("no model call")):
            self.assertTrue(linkdep_tick.run_recheck(commit=False))
        queue = store.load_queue()
        self.assertEqual(queue["recheck"], [])
        self.assertNotIn("zzzzz", queue["human"])

    def test_recheck_waits_until_the_ledger_is_full(self):
        import linkdep_tick
        with store.lock(5):
            queue = store.load_queue()
            queue["recheck"] = [{"lid": "zzzzw", "precedent": "P-0001", "created": 0}]
            store.save_queue(queue)
        with patch.object(linkdep_tick, "fill_complete", return_value=False), \
                patch.object(models, "call", side_effect=AssertionError("no model call")):
            self.assertFalse(linkdep_tick.run_recheck(commit=False))
        self.assertEqual([x["lid"] for x in store.load_queue()["recheck"]], ["zzzzw"])
        with store.lock(5):
            queue = store.load_queue()
            queue["recheck"] = []
            store.save_queue(queue)

    def test_recheck_drops_every_item_of_a_human_decided_link(self):
        from types import SimpleNamespace
        import linkdep_tick
        import linkdep_units as units
        paths = [EndToEndFakeModelTest.POST]
        key = core.unit_key(paths)
        record = {"unit": key, "links": {"zzzzh": {"final": {"relation": "weak", "by": "human"}}}}
        with store.lock(5):
            queue = store.load_queue()
            queue["recheck"] = [{"lid": "zzzzh", "precedent": p, "created": 0}
                                for p in ("P-0001", "P-0002")]
            store.save_queue(queue)
        with patch.object(units, "all_units", return_value=[paths]), \
                patch.object(store, "load_unit_record", return_value=record), \
                patch.object(units, "load_unit", return_value=SimpleNamespace(link=lambda lid: {})), \
                patch.object(linkdep_tick, "out_of_scope", return_value=set()), \
                patch.object(linkdep_tick, "fill_complete", return_value=True), \
                patch.object(models, "available", return_value=True), \
                patch.object(models, "call", side_effect=AssertionError("no model call")):
            self.assertTrue(linkdep_tick.run_recheck(commit=False))
        queue = store.load_queue()
        self.assertEqual(queue["recheck"], [])
        self.assertNotIn("zzzzh", queue["human"])

    def _run_recheck_with(self, lid: str, during=None, relation="required"):
        """A recheck of a 'weak' link whose three Step 4 answers are ``relation``, each
        stage citing another precedent; ``during`` runs inside the call."""
        from types import SimpleNamespace
        import linkdep_tick
        import linkdep_units as units
        paths = [EndToEndFakeModelTest.POST]
        key = core.unit_key(paths)
        h = units.unit_hash(key)
        with store.lock(5):
            store.save_unit_record(h, {"unit": key, "links": {
                lid: {"final": {"relation": "weak", "by": "unanimous"}}}})
            queue = store.load_queue()
            queue["recheck"] = [{"lid": lid, "precedent": p, "created": 0} for p in ("P-0001", "P-0002")]
            store.save_queue(queue)
        cited = {"S1": "P-0001", "S2": "P-0002", "S3": "none"}

        def step4(stage, items):
            if during:
                during(h)
            return {lid: {"relation": relation, "precedent": cited[stage], "pending_id": None}}, {}

        with patch.object(units, "all_units", return_value=[paths]), \
                patch.object(units, "load_unit", return_value=SimpleNamespace(link=lambda lid: {})), \
                patch.object(linkdep_tick, "out_of_scope", return_value=set()), \
                patch.object(linkdep_tick, "fill_complete", return_value=True), \
                patch.object(models, "available", return_value=True), \
                patch.object(pipe, "step4_items", return_value=[]), \
                patch.object(pipe, "run_step4", side_effect=step4), \
                patch.object(pipe, "_record_issue"), \
                patch.object(pipe, "decisive", return_value=False):
            self.assertTrue(linkdep_tick.run_recheck(commit=False))
        return store.load_queue(), store.load_unit_record(h)["links"][lid]

    def test_recheck_sends_a_changed_vote_to_the_human(self):
        queue, rec = self._run_recheck_with("zzzzr")
        self.assertEqual(queue["recheck"], [])                 # both precedents' items answered
        self.assertEqual(queue["human"]["zzzzr"]["kind"], "recheck")
        self.assertEqual(len(rec["rechecks"]), 1)
        with store.lock(5):
            queue = store.load_queue()
            queue["human"].pop("zzzzr")
            store.save_queue(queue)

    def test_recheck_keeps_an_unchanged_value_whatever_the_precedents(self):
        queue, rec = self._run_recheck_with("zzzzp", relation="weak")
        self.assertEqual(queue["recheck"], [])
        self.assertNotIn("zzzzp", queue["human"])
        self.assertEqual(rec["final"]["relation"], "weak")
        self.assertEqual(len(rec["rechecks"]), 1)

    def test_recheck_keeps_a_ruling_made_during_the_calls(self):
        def rule(h):
            record = store.load_unit_record(h)
            record["links"]["zzzzq"]["final"] = {"relation": "weak", "by": "human", "at": 1}
            store.save_unit_record(h, record)

        queue, rec = self._run_recheck_with("zzzzq", during=rule)
        self.assertNotIn("zzzzq", queue["human"])
        self.assertEqual(rec["final"]["by"], "human")
        self.assertEqual(len(rec["rechecks"]), 1)

    def test_fill_complete(self):
        import linkdep_tick
        import linkdep_units as units
        d = Path(tempfile.mkdtemp(prefix="fill-", dir=TMP))
        paths = {}
        for name in ("done", "open", "parked", "untouched", "nolinks", "paused"):
            paths[name] = d / f"{name}.md"
            body = "" if name == "nolinks" else '[x](/a/){: data-lid="abcde" }'
            paths[name].write_text(f"---\ntitle: {name}\n---\n{body}\n", encoding="utf-8")
        key = lambda ps: "+".join(p.stem for p in ps)  # noqa: E731
        entries = {"done": {"next": None}, "open": {"next": "S2"},
                   "parked": {"next": "S2", "parked_fp": "x"}, "paused": {"next": "S1"}}

        def check(names):
            with patch.object(units, "all_units", return_value=[[paths[n]] for n in names]), \
                    patch.object(core, "unit_key", key), \
                    patch.object(linkdep_tick, "out_of_scope", return_value={"paused"}):
                return linkdep_tick.fill_complete({"units": entries})

        self.assertTrue(check(["done", "parked", "nolinks", "paused"]))
        self.assertFalse(check(["done", "open"]))
        self.assertFalse(check(["done", "untouched"]))

    def test_recheck_candidates_leave_the_human_alone_and_spread_out(self):
        import linkdep_digest
        import linkdep_tick
        import linkdep_units as units
        s1 = {"basis": "yy-basis", "evidence": "e", "reason": "r"}

        def rec(by="unanimous", rechecks=0):
            return {"final": {"relation": "weak", "by": by}, "stages": {"S1": {"step1": s1}},
                    "features": {"target_kind": "yy", "in_proof": False},
                    "rechecks": [{}] * rechecks}

        store.write_json(store.UNITS_DIR / "yy-a.json", {"unit": "a", "links": {
            "yy-human": rec("human"), "yy-audit": rec("audit"), "yy-confirmed": rec(),
            "yy-queued": rec(), "yy-waiting": rec(), "yy-often": rec(rechecks=3)}})
        store.write_json(store.UNITS_DIR / "yy-b.json", {"unit": "b", "links": {
            "yy-fresh": rec(), "yy-tiebreak": rec("fable-tiebreak", rechecks=1)}})
        with store.lock(5):
            queue = store.load_queue()
            queue["settled"]["yy-confirmed"] = {"how": "audit"}
            queue["recheck"].append({"lid": "yy-queued", "precedent": "P-0001", "created": 0})
            queue["human"]["yy-waiting"] = {"unit": "a"}
            store.save_queue(queue)
        ruled = (None, {"links": {"yy-ruled": rec()}}, "yy-ruled")
        try:
            with patch.object(units, "all_units", return_value=[]), \
                    patch.object(linkdep_tick, "out_of_scope", return_value=set()):
                ids = [c["id"] for c in linkdep_digest._recheck_candidates([ruled])]
                self.assertEqual(ids, ["yy-fresh", "yy-tiebreak", "yy-often"])
                with patch.object(linkdep_digest, "RECHECK_OFFER", 1):
                    self.assertEqual([c["id"] for c in linkdep_digest._recheck_candidates([ruled])],
                                     ["yy-fresh"])
        finally:
            with store.lock(5):
                queue = store.load_queue()
                queue["settled"].pop("yy-confirmed", None)
                queue["recheck"] = [x for x in queue["recheck"] if x["lid"] != "yy-queued"]
                queue["human"].pop("yy-waiting", None)
                store.save_queue(queue)

    def test_recheck_candidates_skip_paused_posts(self):
        import linkdep_digest
        import linkdep_tick
        import linkdep_units as units
        s1 = {"basis": "zz-basis", "evidence": "e", "reason": "r"}
        rec = {"final": {"relation": "weak"}, "stages": {"S1": {"step1": s1}},
               "features": {"target_kind": "zz", "in_proof": True}}
        for name in ("paused", "live"):
            store.write_json(store.UNITS_DIR / f"zz-{name}.json",
                             {"unit": name, "links": {f"{name}-link": rec}})
        ruled = (None, {"links": {"ruled": rec}}, "ruled")
        with patch.object(units, "all_units", return_value=[]), \
                patch.object(linkdep_tick, "out_of_scope", return_value={"paused"}):
            ids = {c["id"] for c in linkdep_digest._recheck_candidates([ruled])}
        self.assertEqual(ids, {"live-link"})


class StageResumeTest(unittest.TestCase):
    # Named to sort after BookTest/EndToEnd: these rounds share the module's temp book.
    """A stage stopped midway keeps every answer it got and asks only for the rest."""

    def test_stage_resumes_after_the_gate_closes(self):
        import linkdep_tick as tick
        import linkdep_units as units
        e2e = EndToEndFakeModelTest()
        paths = next(p for p in units.all_units() if EndToEndFakeModelTest.POST in p)
        unit = units.load_unit(paths)
        h = units.unit_hash(unit.key)
        lids = set(unit.lids)
        self.assertGreater(len(lids), 4)
        asked: list[tuple[str, str, list[str]]] = []     # (stage, step, ids) of answered calls
        allow: dict[tuple[str, str], int] = {}           # calls of that kind before the gate closes

        def call(stage, prompt, schema=None):
            step = ("1" if prompt.startswith(sp.STEP1_HEAD[:40]) else
                    "4" if prompt.startswith(sp.STEP4_HEAD[:40]) else "reveal")
            left = allow.get((stage, step))
            if left is not None:
                if left == 0:
                    raise models.ModelError(
                        f"{models.PROVIDER[stage]} quota gate closed while waiting for a slot")
                allow[(stage, step)] = left - 1
            asked.append((stage, step, [it["id"] for it in e2e._items(prompt)]))
            return e2e.fake_call(stage, prompt, schema)

        def ids(step):
            return sorted(i for _, s, got in asked if s == step for i in got)

        def stage_has(stage, key):
            links = store.load_unit_record(h)["links"]
            return {lid for lid in lids if links[lid].get("stages", {}).get(stage, {}).get(key)}

        def run(stage, why="continue"):
            return tick.run(state, paths, stage, units.load_unit(paths), why, commit=False)

        flag_all = {"risk": None, "flagged": True, "reasons": ["test"], "by": "rule"}
        state = {"units": {}, "started_at": time.time() - 30 * 86400}
        with patch.object(models, "call", side_effect=call), \
                patch.object(models, "available", return_value=True), \
                patch.object(risk, "score", return_value=flag_all), \
                patch.object(pipe, "MAX_ITEMS", 1), \
                patch.object(pipe, "BATCH_PROMPT_BYTES", 1), \
                patch.object(tick, "dirty_paths", return_value=[]), \
                patch.object(tick, "commit_outputs", return_value=True):
            # Closed at the first call: the new round is on disk all the same.
            allow[("S1", "1")] = 0
            self.assertEqual(run("S1", "new"), 1)
            self.assertEqual(set(store.load_unit_record(h)["round"]), lids)
            # Closed at the second Step 1 chunk: the first chunk's answer stays.
            allow[("S1", "1")] = 1
            self.assertEqual(run("S1"), 1)
            first = stage_has("S1", "step1")
            self.assertEqual(len(first), 1)
            # Closed at the fourth Step 4 batch: Step 1 asks only for the rest.
            allow.clear(), asked.clear()
            allow[("S1", "4")] = 3
            self.assertEqual(run("S1"), 1)
            self.assertEqual(ids("1"), sorted(lids - first))
            batched = stage_has("S1", "step4")
            self.assertEqual(len(batched), 3)
            # The next run asks no Step 1 and Step 4 only for the rest.
            allow.clear(), asked.clear()
            self.assertEqual(run("S1"), 0)
            self.assertEqual(ids("1"), [])
            self.assertEqual(ids("4"), sorted(lids - batched))
            self.assertEqual(state["units"][unit.key]["next"], "S2")
            # S2 closed at its third reveal batch; the rerun reveals only the rest.
            allow[("S2", "reveal")] = 2
            self.assertEqual(run("S2"), 1)
            revealed = {lid for lid in stage_has("S2", "step4")
                        if store.load_unit_record(h)["links"][lid]["stages"]["S2"]["step4"].get("reveal")}
            self.assertEqual(len(revealed), 2)
            allow.clear(), asked.clear()
            self.assertEqual(run("S2"), 0)
            self.assertEqual((ids("1"), ids("4")), ([], []))
            self.assertEqual(ids("reveal"), sorted(lids - revealed))
            self.assertEqual(run("S3"), 0)
        self.assertIsNone(state["units"][unit.key]["next"])
        # Every link went through Step 4, where the scripted S1 says weak and S2·S3
        # say required: the whole round goes to the human queue.
        self.assertTrue(lids <= set(store.load_queue()["human"]))

    def test_step4_keeps_the_answered_items_of_a_batch(self):
        """A batch whose answer leaves an item out keeps the rest; the rerun asks only for it."""
        import linkdep_tick as tick
        import linkdep_units as units
        e2e = EndToEndFakeModelTest()
        paths = next(p for p in units.all_units() if EndToEndFakeModelTest.POST in p)
        unit = units.load_unit(paths)
        h = units.unit_hash(unit.key)
        dropped = unit.lids[1]
        drop = [True]
        step4_ids: list[list[str]] = []

        def call(stage, prompt, schema=None):
            payload, usage = e2e.fake_call(stage, prompt, schema)
            if prompt.startswith(sp.STEP4_HEAD[:40]):
                step4_ids.append([it["id"] for it in e2e._items(prompt)])
                if drop[0]:
                    payload = {"items": [r for r in payload["items"] if r["id"] != dropped]}
            return payload, usage

        flag_all = {"risk": None, "flagged": True, "reasons": ["test"], "by": "rule"}
        state = {"units": {}, "started_at": time.time() - 30 * 86400}
        with patch.object(models, "call", side_effect=call), \
                patch.object(models, "available", return_value=True), \
                patch.object(risk, "score", return_value=flag_all), \
                patch.object(tick, "dirty_paths", return_value=[]), \
                patch.object(tick, "commit_outputs", return_value=True):
            self.assertEqual(tick.run(state, paths, "S1", unit, "new", commit=False), 1)
            self.assertIn("1 item(s) unanswered", state["units"][unit.key]["error"])
            links = store.load_unit_record(h)["links"]
            kept = {lid for lid in unit.lids if links[lid]["stages"]["S1"].get("step4")}
            self.assertEqual(kept, set(unit.lids) - {dropped})
            self.assertEqual(step4_ids[-1], [dropped])          # the in-call retry
            drop[0] = False
            step4_ids.clear()
            self.assertEqual(tick.run(state, paths, "S1", units.load_unit(paths), "continue",
                                      commit=False), 0)
        self.assertEqual(step4_ids, [[dropped]])
        self.assertEqual(state["units"][unit.key]["next"], "S2")

    def test_broken_files_call_keeps_the_first_calls_decisions(self):
        from types import SimpleNamespace
        decided = {"relation": "required", "precedent": "none", "precedent_reason": "",
                   "pending": None, "new_issue": None, "candidates": []}
        path = Path(TMP) / "P-0001.md"
        path.write_text("판례", encoding="utf-8")
        live = {"P": [SimpleNamespace(id="P-0001", path=path)], "Q": []}

        def validate(payload, ids, **kw):
            return {"a": dict(decided), "b": {**decided, "candidates": ["P-0001"]}}

        calls = []

        def call(stage, prompt, schema=None):
            calls.append(prompt)
            if len(calls) == 2:
                raise models.ModelError("prompt exceeds 400000 bytes")
            return {}, {}
        with patch.object(pipe.book, "live", side_effect=lambda kind: live[kind]), \
                patch.object(pipe.book, "index_lines", return_value=[]), \
                patch.object(pipe.sp, "validate_step4", side_effect=validate), \
                patch.object(models, "call", side_effect=call):
            with self.assertRaises(pipe.PartialStep4) as caught:
                pipe.run_step4("S1", [{"id": "a"}, {"id": "b"}])
        exc = caught.exception
        self.assertIn("prompt exceeds", str(exc))            # tick parks on this wording
        self.assertIsNotNone(exc.broke)
        self.assertEqual((set(exc.rows), exc.missing), ({"a"}, ["b"]))

    def test_late_s1_keeps_a_partial_batch(self):
        record = {"unit": "u", "links": {
            "l1": link_rec("a.md", "/ko/math/x#def1", {"S1": "weak", "S2": "required", "S3": "required"}),
            "l2": link_rec("a.md", "/ko/math/x#def2", {"S1": "weak", "S2": "required", "S3": "required"}),
        }}

        class FakeUnit:
            def link(self, lid):
                return object()

        row = {"relation": "required", "precedent": "none", "precedent_reason": "",
               "pending": None, "new_issue": None, "candidates": []}

        def partial(stage, batch):
            raise pipe.PartialStep4("S1 step 4 left 1 item(s) unanswered", {"l1": dict(row)},
                                    [{}], ["l2"])
        with patch.object(pipe, "step4_items", lambda u, r, stage, lids: lids), \
                patch.object(pipe, "step4_batches", lambda items: [items]), \
                patch.object(pipe, "run_step4", side_effect=partial), \
                patch.object(pipe, "_record_issue", lambda *a: None):
            out = pipe.run_late_s1(FakeUnit(), record, ["l1", "l2"])
        self.assertEqual(out, {"late_s1": 2, "late_s1_changed": 1, "late_s1_unanswered": 1})
        self.assertTrue(record["links"]["l1"]["stages"]["S1"]["late"])
        self.assertNotIn("step4", record["links"]["l2"]["stages"]["S1"])


class StepFourBatchingTest(unittest.TestCase):
    # Named to sort after BookTest/EndToEnd: these rounds share the module's temp book.
    """Step 4 and the reveal split their items so no prompt overflows (2026-10-31)."""

    def test_pack(self):
        sizes = {"a": 5, "b": 5, "c": 5, "d": 20}
        out = pipe.pack(list("abcd"), lambda b: sum(sizes[x] for x in b), budget=10, max_items=5)
        self.assertEqual(out, [["a", "b"], ["c"], ["d"]])          # d alone, over budget
        self.assertEqual(pipe.pack(list("abc"), lambda b: 0, budget=10, max_items=2),
                         [["a", "b"], ["c"]])

    def test_round_with_one_item_per_call(self):
        """The end-to-end round, with every Step 4 / reveal call holding one item."""
        import linkdep_tick as tick
        import linkdep_units as units
        e2e = EndToEndFakeModelTest()
        prompts = []

        def call(stage, prompt, schema=None):
            if not prompt.startswith(sp.STEP1_HEAD[:40]):
                prompts.append(len(e2e._items(prompt)))
            return e2e.fake_call(stage, prompt, schema)

        paths = next(p for p in units.all_units() if EndToEndFakeModelTest.POST in p)
        state = {"units": {}, "started_at": time.time() - 30 * 86400}
        with patch.object(models, "call", side_effect=call), \
                patch.object(models, "available", return_value=True), \
                patch.object(pipe, "BATCH_PROMPT_BYTES", 1), \
                patch.object(tick, "dirty_paths", return_value=[]), \
                patch.object(tick, "commit_outputs", return_value=True):
            for stage, why in (("S1", "new"), ("S2", "continue"), ("S3", "continue")):
                self.assertEqual(tick.run(state, paths, stage, units.load_unit(paths), why,
                                          commit=False), 0)
        self.assertIsNone(state["units"][units.load_unit(paths).key]["next"])
        self.assertTrue(prompts)
        self.assertEqual(set(prompts), {1})


class UnitParkingTest(unittest.TestCase):
    """A prompt over the byte limit parks the unit instead of retrying hourly."""

    def test_oversize_parks_quietly(self):
        import linkdep_tick as tick
        import linkdep_units as units
        paths = next(p for p in units.all_units() if EndToEndFakeModelTest.POST in p)
        unit = units.load_unit(paths)
        state = {"units": {}, "started_at": time.time()}
        logged, sent = [], []
        with patch.object(models, "call",
                          side_effect=models.ModelError("prompt exceeds 400000 bytes")), \
                patch.object(models, "available", return_value=True), \
                patch.object(tick, "log", side_effect=logged.append), \
                patch.object(core, "notify", side_effect=lambda *a, **k: sent.append(k)), \
                patch.object(tick, "dirty_paths", return_value=[]):
            self.assertEqual(tick.run(state, paths, "S1", unit, "new", commit=False), 0)
            self.assertEqual(tick.run(state, paths, "S1", unit, "new", commit=False), 0)
        entry = state["units"][unit.key]
        self.assertEqual(entry["parked_fp"], unit.fingerprint)
        self.assertGreater(entry["retry_after"], time.time() + 6 * 86400)
        self.assertFalse(any(dc_err in line.lower() for line in logged
                             for dc_err in ("error", "failed", "failure")))
        self.assertEqual(len(sent), 1)                     # announced once, to the digest
        self.assertTrue(sent[0].get("digest"))


class CommitLedgerTest(unittest.TestCase):
    """Only a ledger left dirty after the commit attempt is a failure."""

    def test_nothing_to_commit_is_quiet(self):
        import linkdep_tick as tick
        with patch.object(tick, "commit_outputs", return_value=False), \
                patch.object(tick, "dirty_paths", return_value=[]):
            tick.commit_ledger("Series: 확정 0건, 사람 판정 대기 2건", True)

    def test_dirty_after_attempt_raises(self):
        import linkdep_tick as tick
        with patch.object(tick, "commit_outputs", return_value=False), \
                patch.object(tick, "dirty_paths", return_value=[tick.LEDGER_REL]):
            with self.assertRaises(RuntimeError):
                tick.commit_ledger("Line_Bundles: 확정 2건, 사람 판정 대기 2건", True)


class ClaudeBillingTest(unittest.TestCase):
    """S2 picks credits or subscription via claude-credit; refusals fall back."""

    @staticmethod
    def proc(rc=0, **envelope):
        from subprocess import CompletedProcess
        body = {"is_error": False, "result": '{"items": []}', "total_cost_usd": 0.5,
                "usage": {"output_tokens": 3}, "num_turns": 1, **envelope}
        return CompletedProcess([], rc, json.dumps(body), "")

    def run_s2(self, route_key, *procs):
        cli, runs = [], []

        def run(prompt, api_key=""):
            runs.append(api_key)
            return procs[len(runs) - 1]
        with patch.object(models, "_credit_key", return_value=(route_key, "test")), \
                patch.object(models, "_run_claude", side_effect=run), \
                patch.object(models, "_credit_cli", side_effect=lambda *a: cli.append(a)):
            payload, usage = models._claude("ITEMS:\n[]")
        return payload, usage, runs, cli

    def test_subscription_route_makes_one_plain_call(self):
        _, usage, runs, cli = self.run_s2("", self.proc())
        self.assertEqual(runs, [""])
        self.assertEqual(usage["billing"], "subscription")
        self.assertEqual(cli, [])

    def test_credit_route_records_cost(self):
        _, usage, runs, cli = self.run_s2("sk-test", self.proc())
        self.assertEqual(runs, ["sk-test"])
        self.assertEqual(usage["billing"], "credit")
        self.assertEqual(cli, [("record", "--cost", "0.5", "--by", models.CREDIT_CALLER)])

    def test_used_up_credits_fall_back_to_subscription(self):
        refused = self.proc(1, is_error=True, api_error_status=400, total_cost_usd=0,
                            result="Credit balance is too low · Add funds")
        _, usage, runs, cli = self.run_s2("sk-test", refused, self.proc())
        self.assertEqual(runs, ["sk-test", ""])
        self.assertEqual(usage["billing"], "subscription")
        self.assertEqual(cli[0][:3], ("exhausted", "--kind", "credit"))

    def test_rejected_key_falls_back_as_auth(self):
        refused = self.proc(1, is_error=True, api_error_status=401, result="Invalid API key")
        _, usage, runs, cli = self.run_s2("sk-test", refused, self.proc())
        self.assertEqual(runs, ["sk-test", ""])
        self.assertEqual(cli[0][:3], ("exhausted", "--kind", "auth"))

    def test_other_credit_path_errors_stay_model_errors(self):
        overloaded = self.proc(1, is_error=True, api_error_status=529, result="Overloaded")
        with self.assertRaises(models.ModelError):
            self.run_s2("sk-test", overloaded)

    def test_router_garbage_means_subscription(self):
        from subprocess import CompletedProcess
        with patch.object(models, "_credit_cli", return_value=CompletedProcess([], 0, "nope", "")):
            self.assertEqual(models._credit_key()[0], "")
        with patch.object(models, "_credit_cli", return_value=None):
            self.assertEqual(models._credit_key()[0], "")

    def test_credit_call_is_bare_and_subscription_call_has_no_key(self):
        seen = []

        def fake_run(args, **kw):
            from subprocess import CompletedProcess
            seen.append((args, kw["env"]))
            return CompletedProcess(args, 0, "{}", "")
        with patch.dict(os.environ, {"ANTHROPIC_API_KEY": "leaked"}), \
                patch.object(models.subprocess, "run", side_effect=fake_run):
            models._run_claude("p", "sk-test")
            models._run_claude("p")
        (bare_args, bare_env), (plain_args, plain_env) = seen
        self.assertIn("--bare", bare_args)
        self.assertIn("--no-session-persistence", bare_args)
        self.assertEqual(bare_env["ANTHROPIC_API_KEY"], "sk-test")
        self.assertNotIn("--bare", plain_args)
        self.assertNotIn("ANTHROPIC_API_KEY", plain_env)


class GeminiApiS1Test(unittest.TestCase):
    """S1 goes to the Gemini API only while the Antigravity gate is closed."""

    class Slot:
        def close(self):
            pass

    def test_test_env_never_reaches_gemini_credit(self):
        self.assertFalse(models.gemini_api_usable())

    def test_available_falls_back_to_the_api_for_s1_only(self):
        with patch.object(core, "provider_available", return_value=False):
            with patch.object(models, "gemini_api_usable", return_value=True):
                self.assertTrue(models.available("S1"))
                self.assertFalse(models.available("S2"))
                self.assertFalse(models.available("S3"))
            with patch.object(models, "gemini_api_usable", return_value=False):
                self.assertFalse(models.available("S1"))

    def test_call_routes_s1_by_the_gate(self):
        api = ({"items": []}, {"billing": "gemini-api"})
        agy = ({"items": []}, {"turns": 1})
        with patch.object(core, "acquire_provider_slot", return_value=self.Slot()), \
                patch.object(models, "_gemini_api", return_value=api) as via_api, \
                patch.object(models, "_agy", return_value=agy) as via_agy:
            with patch.object(core, "provider_available", return_value=True):
                self.assertEqual(models.call("S1", "p"), agy)
            with patch.object(core, "provider_available", return_value=False), \
                    patch.object(models, "gemini_api_usable", return_value=True):
                self.assertEqual(models.call("S1", "p"), api)
            with patch.object(core, "provider_available", return_value=False), \
                    patch.object(models, "gemini_api_usable", return_value=False):
                with self.assertRaisesRegex(models.ModelError, "quota gate closed"):
                    models.call("S1", "p")
        self.assertEqual(via_api.call_count, 1)
        self.assertEqual(via_agy.call_count, 1)

    def test_api_call_arguments_usage_and_errors(self):
        from subprocess import CompletedProcess
        reply = {"text": '{"items": []}', "model": "gemini-4-neon", "tier": "flex", "cost": 0.01,
                 "usage": {"promptTokenCount": 1000, "candidatesTokenCount": 200,
                           "thoughtsTokenCount": 800}}
        seen = []

        def run(rc, out="", err=""):
            def fake(args, **kw):
                seen.append((args, kw.get("input")))
                return CompletedProcess(args, rc, out, err)
            return fake
        with patch.object(models.subprocess, "run", side_effect=run(0, json.dumps(reply))):
            payload, usage = models._gemini_api("PROMPT")
        args, given = seen[-1]
        self.assertEqual(payload, {"items": []})
        self.assertEqual(given, "PROMPT")                      # no [cron] prefix on the API
        for flag, value in (("--model", "gemini-4-neon"), ("--thinking", models.AGY_EFFORT),
                            ("--system-file", str(models.AGY_AGENT_FILE)), ("--tier", "flex")):
            self.assertEqual(args[args.index(flag) + 1], value)
        self.assertIn("--fallback-standard", args)
        self.assertEqual((usage["input_tokens"], usage["output_tokens"], usage["thinking_tokens"]),
                         (1000, 1000, 800))
        self.assertEqual((usage["billing"], usage["tier"], usage["cost_usd"]),
                         ("gemini-api", "flex", 0.01))
        with patch.object(models.subprocess, "run", side_effect=run(3, err="HTTP 429 X")):
            with self.assertRaisesRegex(models.ModelError, "refused"):
                models._gemini_api("p")
        with patch.object(models.subprocess, "run", side_effect=run(1, err="empty answer: MAX_TOKENS")):
            with self.assertRaisesRegex(models.ModelError, "output token limit"):
                models._gemini_api("p")


if __name__ == "__main__":
    unittest.main()
