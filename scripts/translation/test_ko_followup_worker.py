#!/usr/bin/env python3
"""Focused tests for draining the KO follow-up queue in one cron run."""
from __future__ import annotations

import json
import tempfile
import unittest
from pathlib import Path
from types import SimpleNamespace
from unittest.mock import patch

import ko_followup_worker as worker


class FollowupBatchTest(unittest.TestCase):
    def setUp(self) -> None:
        # run_all() prunes notes against the given state; never let a test
        # reach the dashboard's real note file.
        tmp = tempfile.TemporaryDirectory(prefix="ko-followup-notes-")
        self.addCleanup(tmp.cleanup)
        notes = Path(tmp.name) / "notes.json"
        for target, value in (("NOTE_STATE", notes),
                              ("NOTE_LOCK", Path(f"{notes}.lock"))):
            patcher = patch.object(worker, target, value)
            patcher.start()
            self.addCleanup(patcher.stop)

    def test_scoped_diff_ignores_another_links_metadata(self) -> None:
        baseline = (
            "결과적으로 이를 두 quotient가 같게 되는 것이다.\n"
            + "문맥입니다.\n" * 10
            + '[다른 글](other){: data-lid="aaaaa" }\n'
        )
        current = baseline.replace(
            "이를 두 quotient가", "이들 두 quotient가",
        ).replace('data-lid="aaaaa"', 'data-lid="bbbbb"')

        diff = worker._scoped_ko_diff(
            baseline, current,
            [{"quote": "결과적으로 이를 두 quotient가 같게 되는 것이다.",
              "line": 1}],
            "ko.md",
        )

        self.assertIn("이들 두 quotient가", diff)
        self.assertNotIn('data-lid="bbbbb"', diff)

    def test_scoped_diff_keeps_the_finding_links_metadata(self) -> None:
        baseline = '[대상](target)\n'
        current = '[대상](target){: data-lid="aaaaa" }\n'

        diff = worker._scoped_ko_diff(
            baseline, current, [{"quote": "[대상](target)", "line": 1}],
            "ko.md",
        )

        self.assertIn('data-lid="aaaaa"', diff)

    def test_persists_migrated_state_with_an_empty_request_queue(self) -> None:
        state = {"files": {"new.md": {"status": "done"}}}
        with tempfile.TemporaryDirectory(prefix="ko-followup-test-") as tmp:
            request_state = Path(tmp) / "requests.json"
            request_state.write_text("{}", encoding="utf-8")
            with (
                patch.object(worker, "REQUEST_STATE", request_state),
                patch.object(worker.tw, "load_state", return_value=state),
                patch.object(worker.tw, "_migrated_keys", 1),
                patch.object(worker.tw, "save_state") as save_state,
                patch.object(worker, "log"),
            ):
                rc = worker.run_all()

        self.assertEqual(rc, 0)
        save_state.assert_called_once_with(state)

    def _run_with(self, requests: dict, files: dict, process):
        with tempfile.TemporaryDirectory(prefix="ko-followup-test-") as tmp:
            request_state = Path(tmp) / "requests.json"
            request_state.write_text(json.dumps(requests), encoding="utf-8")
            with (
                patch.object(worker, "REQUEST_STATE", request_state),
                patch.object(worker.tw, "load_state", return_value={"files": files}),
                patch.object(worker.tw, "save_state"),
                patch.object(worker, "_process_target", side_effect=process) as mocked,
                patch.object(worker, "log"),
            ):
                rc = worker.run_all()
                remaining = json.loads(request_state.read_text(encoding="utf-8"))
        return rc, mocked.call_args_list, remaining

    def test_processes_every_valid_request_and_removes_stale_ones(self) -> None:
        requests = {"a.md@t1": 1, "stale.md@old": 1, "b.md@t2": 1}
        files = {
            "a.md": {"ko_reviewed_at": "t1"},
            "b.md": {"ko_reviewed_at": "t2"},
        }
        seen = []

        def process(target, state):
            seen.append(target[1])
            return 0

        rc, calls, remaining = self._run_with(requests, files, process)

        self.assertEqual(rc, 0)
        self.assertEqual(seen, ["a.md", "b.md"])
        self.assertEqual(len(calls), 2)
        self.assertNotIn("stale.md@old", remaining)

    def test_one_item_exception_does_not_block_later_requests(self) -> None:
        requests = {"a.md@t1": 1, "b.md@t2": 1}
        files = {
            "a.md": {"ko_reviewed_at": "t1"},
            "b.md": {"ko_reviewed_at": "t2"},
        }
        seen = []

        def process(target, state):
            seen.append(target[1])
            if target[1] == "a.md":
                raise RuntimeError("first item broke")
            return 0

        rc, calls, _ = self._run_with(requests, files, process)

        self.assertEqual(rc, 1)
        self.assertEqual(seen, ["a.md", "b.md"])
        self.assertEqual(len(calls), 2)

    def test_rejection_unchecks_request_and_records_reason(self) -> None:
        with tempfile.TemporaryDirectory(prefix="ko-followup-test-") as tmp:
            request_state = Path(tmp) / "requests.json"
            request_state.write_text(
                json.dumps({"a.md@t1": 1, "b.md@t2": 1}), encoding="utf-8",
            )
            entry = {"ko_reviewed_at": "t1"}
            state = {"files": {"a.md": entry}}
            with (
                patch.object(worker, "REQUEST_STATE", request_state),
                patch.object(worker.tw, "save_state") as save_state,
                patch.object(worker, "log"),
            ):
                worker._record_rejection(
                    "a.md@t1", "a.md", entry, state, "KO correction incomplete",
                )

            remaining = json.loads(request_state.read_text(encoding="utf-8"))
            self.assertNotIn("a.md@t1", remaining)
            self.assertEqual(remaining["b.md@t2"], 1)
            self.assertEqual(
                entry["ko_followup_rejection_reason"], "KO correction incomplete",
            )
            self.assertEqual(entry["ko_followup_rejected_request"], "a.md@t1")
            save_state.assert_called_once_with(state)

    def test_one_item_exception_is_recorded_as_a_wait(self) -> None:
        requests = {"a.md@t1": 1}
        files = {"a.md": {"ko_reviewed_at": "t1"}}

        def process(target, state):
            raise RuntimeError("first item broke")

        self._run_with(requests, files, process)

        wait = files["a.md"]["ko_followup_wait"]
        self.assertEqual(wait["request"], "a.md@t1")
        self.assertEqual(wait["count"], 1)
        self.assertIn("first item broke", wait["reason"])

    def test_consecutive_waits_count_per_request(self) -> None:
        entry = {}
        state = {"files": {"a.md": entry}}
        with (
            patch.object(worker.tw, "save_state") as save_state,
            patch.object(worker, "log") as log,
        ):
            worker._record_wait("a.md@t1", "a.md", entry, state, "first")
            worker._record_wait("a.md@t1", "a.md", entry, state, "second\nline")
            self.assertEqual(entry["ko_followup_wait"]["count"], 2)
            self.assertEqual(entry["ko_followup_wait"]["reason"], "second line")
            worker._record_wait("a.md@t2", "a.md", entry, state, "re-audited")
            self.assertEqual(entry["ko_followup_wait"]["count"], 1)

        self.assertEqual(save_state.call_count, 3)
        log.assert_called_with("WAIT a.md: re-audited")

    def test_unchecked_request_drops_its_wait_record(self) -> None:
        files = {
            "a.md": {"ko_reviewed_at": "t1",
                     "ko_followup_wait": {"request": "a.md@t1", "count": 3}},
            "b.md": {"ko_reviewed_at": "t2",
                     "ko_followup_wait": {"request": "b.md@t2", "count": 2}},
        }
        seen = []

        def process(target, state):
            seen.append(target[1])
            return 1

        self._run_with({"b.md@t2": 1}, files, process)

        self.assertNotIn("ko_followup_wait", files["a.md"])
        self.assertEqual(files["b.md"]["ko_followup_wait"]["count"], 2)
        self.assertEqual(seen, ["b.md"])

    def test_rejection_clears_the_wait_record(self) -> None:
        with tempfile.TemporaryDirectory(prefix="ko-followup-test-") as tmp:
            request_state = Path(tmp) / "requests.json"
            request_state.write_text(json.dumps({"a.md@t1": 1}), encoding="utf-8")
            entry = {"ko_reviewed_at": "t1",
                     "ko_followup_wait": {"request": "a.md@t1", "count": 2}}
            with (
                patch.object(worker, "REQUEST_STATE", request_state),
                patch.object(worker.tw, "save_state"),
                patch.object(worker, "log"),
            ):
                worker._record_rejection(
                    "a.md@t1", "a.md", entry, {"files": {"a.md": entry}}, "no",
                )

        self.assertNotIn("ko_followup_wait", entry)

    def test_missing_replacement_reports_where_it_stops_matching(self) -> None:
        en = "Let $$\n\\mathfrak{p}\n$$ be prime.\n"
        old = "Let $$\\n\\mathfrak{p}"   # literal backslash-n instead of a newline
        with patch.object(
            worker.tw, "call_translator",
            return_value=json.dumps({"replacements": [{"old": old, "new": "x"}]}),
        ):
            with self.assertRaises(RuntimeError) as caught:
                worker.antigravity_candidate(en, [], "")

        message = str(caught.exception)
        self.assertIn("replacement 1/1: old 가 EN 에 없음", message)
        self.assertIn("앞 6/", message)
        self.assertIn(repr("\\n\\mathfrak{p}"), message)
        self.assertIn(repr("\n\\mathfrak{p}\n$$ be prime.\n"), message)

    def test_duplicated_replacement_reports_the_count(self) -> None:
        message = worker._replacement_miss("ab ab", "ab", 2, 3)
        self.assertEqual(message, "Antigravity replacement 2/3: old 가 EN 에 2곳 일치 'ab'")

    def test_codex_can_inspect_existing_english_when_diff_is_empty(self) -> None:
        captured = {}

        def run(cmd, **kwargs):
            captured["prompt"] = kwargs["input"]
            out_path = Path(cmd[cmd.index("--output-last-message") + 1])
            out_path.write_text(
                '{"pass":true,"why":"already synchronized"}', encoding="utf-8",
            )
            return SimpleNamespace(returncode=0, stderr="")

        with patch.object(worker.subprocess, "run", side_effect=run):
            passed, why = worker.codex_pass(
                [{"issue": "missing justification"}],
                "KO correction",
                "(no changes)",
                "The final English already includes the justification.",
            )

        self.assertTrue(passed)
        self.assertEqual(why, "already synchronized")
        self.assertIn(
            "The final English already includes the justification.",
            captured["prompt"],
        )

    def test_rejected_proposal_is_regenerated_from_codex_feedback(self) -> None:
        proposals = ["unchanged EN", "corrected EN"]
        verdicts = [(False, "state the component comparison"), (True, "fixed")]
        with (
            patch.object(worker, "antigravity_candidate", side_effect=proposals) as propose,
            patch.object(worker, "codex_pass", side_effect=verdicts) as review,
            patch.object(worker.tw, "validate_translation", return_value=None),
            patch.object(worker.tw, "lint_latex", return_value=[]),
            patch.object(worker.tw, "lint_structure", return_value=[]),
            patch.object(worker, "log"),
        ):
            candidate, passed, why = worker.reviewed_candidate(
                "unchanged EN", "corrected KO", "old KO", [{"issue": "gap"}],
                "KO diff", "ko.md", "en.md",
            )

        self.assertTrue(passed)
        self.assertEqual(candidate, "corrected EN")
        self.assertEqual(why, "fixed")
        self.assertEqual(review.call_count, 2)
        self.assertEqual(
            propose.call_args_list[1].kwargs["review_feedback"],
            "state the component comparison",
        )


if __name__ == "__main__":
    unittest.main()
