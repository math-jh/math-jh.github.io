#!/usr/bin/env python3
"""KO 원문 감사가 후속 판정 밖의 경로에서 지워지지 않는지 확인한다.

감사(verify_ko_typos · verify_ko_typos_review · 기준 판본)는 대시보드 체크 뒤
ko_followup_worker 의 판정 통과로만 지워진다. Phase 4 재검증과 재번역 기록이
이를 비우거나 떨어뜨리면 지적이 대시보드에서 조용히 사라진다.
"""
from __future__ import annotations

import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch

import translate_worker as tw

KO = (
    "첫 문단이다.\n"
    "이 함수는 모든 직선 방향에서 그 극한이 $0$이다.\n"
    "마지막 문단이다.\n"
)


def audit(quote: str, claim: str, verdict: str = "VALID") -> dict:
    return {"kind": "ERROR", "quote": quote, "issue": claim, "claim": claim,
            "verdict": verdict, "line": 2}


def check_result(verdict_text: str) -> dict:
    return {
        "ko_p": (1, 1), "en_p": (1, 1), "lints": [], "struct": [],
        "verdict": verdict_text,
        "fields": {"verified_at": "2026-11-01T00:00:00+00:00",
                   "verify_math_counts": [[1, 1], [1, 1]],
                   "verify_lints": None, "verify_structure": None},
    }


class KoAuditStateTest(unittest.TestCase):
    def setUp(self) -> None:
        tmp = tempfile.TemporaryDirectory(prefix="ko-audit-")
        self.addCleanup(tmp.cleanup)
        self.ko = Path(tmp.name) / "post.md"
        self.en = Path(tmp.name) / "post.en.md"
        self.ko.write_text(KO, encoding="utf-8")
        self.en.write_text("EN\n", encoding="utf-8")
        for name, value in (("save_state", lambda state: None),
                            ("log", lambda msg: None),
                            ("_notify", lambda *a, **k: None)):
            patcher = patch.object(tw, name, value)
            patcher.start()
            self.addCleanup(patcher.stop)

    def outstanding_entry(self) -> dict:
        old = audit("모든 직선 방향에서", "기준점이 없다")
        return {
            "status": "done",
            "verify_ko_typos": [old["claim"]],
            "verify_ko_typos_review": [old],
            "ko_reviewed_at": "2026-09-30T00:00:00+00:00",
            "ko_review_base_content": KO,
            "ko_review_base_sha256": "base",
            "ko_followup_wait": {"request": "x", "count": 1},
        }

    def run_verify(self, entry: dict, verdict_text: str, review=None) -> dict:
        state = {"files": {"k": entry}}
        reviewer = patch.object(tw, "review_ko_findings",
                                side_effect=review or (lambda p, k, f: []))
        with patch.object(tw, "check_en", return_value=check_result(verdict_text)), \
                reviewer as mocked:
            tw.run_verify(state, self.ko, self.en, "k")
        self.reviewer = mocked
        return state["files"]["k"]

    def test_reverify_without_ko_typos_keeps_outstanding_audit(self) -> None:
        entry = self.run_verify(self.outstanding_entry(), "VERDICT: safe\n")
        self.assertEqual(entry["verify_ko_typos"], ["기준점이 없다"])
        self.assertEqual(entry["ko_reviewed_at"], "2026-09-30T00:00:00+00:00")
        self.assertEqual(entry["verified_at"], "2026-11-01T00:00:00+00:00")
        self.reviewer.assert_not_called()

    def test_reverify_clears_only_when_no_live_audit(self) -> None:
        entry = self.outstanding_entry()
        entry["verify_ko_typos_review"][0]["verdict"] = "FALSE"
        entry = self.run_verify(entry, "VERDICT: safe\n")
        self.assertIsNone(entry["verify_ko_typos"])

    def test_phase4_ko_typos_become_a_reviewed_audit(self) -> None:
        verdict = "VERDICT: safe\nKO-TYPOS:\n- 부호가 틀렸다\n"
        entry = self.run_verify(
            {"status": "done"}, verdict,
            review=lambda p, k, f: [{**x, "claim": x["issue"], "verdict": "VALID"}
                                    for x in f])
        self.assertEqual(entry["verify_ko_typos"], ["부호가 틀렸다"])
        self.assertTrue(entry["ko_reviewed_at"])
        self.assertEqual(entry["ko_review_base_content"], KO)

    def test_already_reviewed_claim_is_not_sent_again(self) -> None:
        entry = self.outstanding_entry()
        claim = tw._finding_claim(tw.ko_typo_findings(["기준점이 없다"])[0])
        entry["verify_ko_typos_review"][0]["claim"] = claim
        entry["verify_ko_typos"] = [claim]
        verdict = "VERDICT: safe\nKO-TYPOS:\n- 기준점이 없다\n"
        entry = self.run_verify(entry, verdict)
        self.reviewer.assert_not_called()
        self.assertEqual(entry["ko_reviewed_at"], "2026-09-30T00:00:00+00:00")

    def test_new_claim_merges_and_drops_fixed_old_findings(self) -> None:
        entry = self.outstanding_entry()
        gone = audit("이미 고친 문장", "고쳐진 지적")
        entry["verify_ko_typos_review"].append(gone)
        entry["verify_ko_typos"].append(gone["claim"])
        verdict = "VERDICT: safe\nKO-TYPOS:\n- 새 지적\n"
        entry = self.run_verify(
            entry, verdict,
            review=lambda p, k, f: [{**x, "claim": x["issue"], "verdict": "VALID"}
                                    for x in f])
        self.assertEqual(entry["verify_ko_typos"], ["기준점이 없다", "새 지적"])
        self.assertNotEqual(entry["ko_reviewed_at"], "2026-09-30T00:00:00+00:00")
        self.assertEqual(entry["verify_ko_typos_review"][0]["line"], 2)
        self.assertNotIn("ko_followup_wait", entry)

    def test_rewritten_entry_carries_outstanding_audit(self) -> None:
        prev = self.outstanding_entry()
        fresh = {"status": "done", "reason": "drift-incremental"}
        tw.merge_ko_audit(prev, fresh, self.ko, [], "k")
        for field in tw.KO_AUDIT_FIELDS:
            if field in prev:
                self.assertEqual(fresh[field], prev[field], field)

    def test_rewritten_entry_without_audit_records_new_review(self) -> None:
        fresh = {"status": "done"}
        review = [audit("마지막 문단", "새 감사")]
        tw.merge_ko_audit({"status": "done"}, fresh, self.ko, review, "k")
        self.assertEqual(fresh["verify_ko_typos"], ["새 감사"])
        self.assertEqual(fresh["ko_review_base_content"], KO)


if __name__ == "__main__":
    unittest.main()
