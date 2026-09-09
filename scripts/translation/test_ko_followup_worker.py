#!/usr/bin/env python3
"""Focused tests for draining the KO follow-up queue in one cron run."""
from __future__ import annotations

import json
import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch

import ko_followup_worker as worker


class FollowupBatchTest(unittest.TestCase):
    def _run_with(self, requests: dict, files: dict, process):
        with tempfile.TemporaryDirectory(prefix="ko-followup-test-") as tmp:
            request_state = Path(tmp) / "requests.json"
            request_state.write_text(json.dumps(requests), encoding="utf-8")
            with (
                patch.object(worker, "REQUEST_STATE", request_state),
                patch.object(worker.tw, "load_state", return_value={"files": files}),
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


if __name__ == "__main__":
    unittest.main()
