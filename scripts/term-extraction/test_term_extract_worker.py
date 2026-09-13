#!/usr/bin/env python3
"""Selection tests for the bounded term-extraction lifecycle."""
from __future__ import annotations

import importlib.util
import sys
import unittest
from pathlib import Path
from types import SimpleNamespace
from unittest.mock import patch


MODULE_PATH = Path(__file__).with_name("term_extract_worker.py")
SPEC = importlib.util.spec_from_file_location("term_extract_worker_under_test", MODULE_PATH)
assert SPEC and SPEC.loader
worker = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = worker
SPEC.loader.exec_module(worker)


class SelectionTest(unittest.TestCase):
    def test_existing_post_gets_exactly_one_retry(self) -> None:
        rel = "_posts/Math/Test/ko/post.md"
        state = {"posts": {rel: {"last_checked": 100.0}}, "audit": {}}
        with (
            patch.object(worker, "all_ko_posts", return_value=[rel]),
            patch.object(worker, "ko_content_commits", return_value={rel: ("a", 90.0)}),
            patch.object(worker.time, "time", return_value=200.0),
        ):
            self.assertEqual(worker.select_post(state), (rel, "retry"))
            state["posts"][rel]["revision_attempts"] = 2
            self.assertEqual(worker.select_post(state), (None, ""))

    def test_new_content_commit_starts_a_new_two_attempt_generation(self) -> None:
        rel = "_posts/Math/Test/ko/post.md"
        state = {"posts": {rel: {
            "last_checked": 100.0, "revision_attempts": 2, "content_commit": "old",
        }}, "audit": {}}
        with (
            patch.object(worker, "all_ko_posts", return_value=[rel]),
            patch.object(worker, "ko_content_commits", return_value={rel: ("new", 150.0)}),
            patch.object(worker.time, "time", return_value=200.0),
        ):
            self.assertEqual(worker.select_post(state), (rel, "modified"))


class CommitMarkerTest(unittest.TestCase):
    def test_lastmod_skip_and_dev_commits_are_not_content_signals(self) -> None:
        content = (
            "\x1enew\x1f300\x1fmechanical [lastmod-skip]\n\x00\n"
            "_posts/Math/Test/ko/post.md\x00"
            "\x1emid\x1f200\x1fnotes [dev]\n\x00\n"
            "_posts/Math/Test/ko/post.md\x00"
            "\x1eold\x1f100\x1factual content\n\x00\n"
            "_posts/Math/Test/ko/post.md\x00"
        )
        result = SimpleNamespace(returncode=0, stdout=content)
        with patch.object(worker.subprocess, "run", return_value=result):
            self.assertEqual(
                worker.ko_content_commits()["_posts/Math/Test/ko/post.md"],
                ("old", 100.0),
            )


if __name__ == "__main__":
    unittest.main()
