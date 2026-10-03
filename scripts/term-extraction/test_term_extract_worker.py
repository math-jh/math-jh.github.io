#!/usr/bin/env python3
"""Selection tests for the bounded term-extraction lifecycle."""
from __future__ import annotations

import importlib.util
import sys
import tempfile
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


TERMS_WITH_DEL_OPERATOR = """# test
D:
- id: dolbeault_complex
  en: Dolbeault complex
  ko: Dolbeault 복합체
  primary: en
  defs:
  - label: '[테스트] §글'
    url: /ko/math/test/post
P:
- id: del_operator
  en: $\\partial$-operator
  ko: $\\partial$-연산자
  primary: ko
  defs:
  - label: '[테스트] §글'
    url: /ko/math/test/post
"""


class ExistingEntryTest(unittest.TestCase):
    def setUp(self) -> None:
        from terms_common import split_file
        _, self.groups = split_file(TERMS_WITH_DEL_OPERATOR)
        self.idx = worker.entry_index(self.groups)
        self.ids = worker.id_index(self.groups)

    def test_new_entry_id_finds_entry_filed_under_another_letter(self) -> None:
        self.assertEqual(
            worker.find_entry(self.idx, self.ids, "deloperator", "del operator"),
            ("P", 0),
        )

    def test_unrelated_term_is_not_matched(self) -> None:
        self.assertIsNone(
            worker.find_entry(self.idx, self.ids, "deltafunction", "delta function"))
        self.assertIsNone(worker.find_entry(self.idx, self.ids, "", ""))

    def test_marker_for_existing_entry_is_not_added_again(self) -> None:
        rel = "_posts/Math/Test/ko/post.md"
        body = ("::: 정의 1\n"
                "*del 연산자<sub>del operator</sub>* $\\partial$를 정의한다.\n"
                ":::\n\n" + "본문 문장이다. " * 60)
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            post = root / rel
            post.parent.mkdir(parents=True)
            post.write_text("---\ntitle: 글\n---\n" + body, encoding="utf-8")
            terms = root / "terms.yml"
            terms.write_text(TERMS_WITH_DEL_OPERATOR, encoding="utf-8")
            with (
                patch.dict(worker.os.environ, {"GLOSS_STAGE": "0"}),
                patch.object(worker, "BLOG_ROOT", root),
                patch.object(worker, "TERMS_PATH", terms),
                patch.object(worker, "post_meta",
                             return_value=("글", "/ko/math/test/post", "[테스트] §글")),
                patch.object(worker, "review_note"),
                patch.object(worker, "llm_json",
                             side_effect=AssertionError("LLM 호출 없음이어야 한다")),
            ):
                self.assertEqual(worker.process_post(rel, "first", dry=True), [])
            self.assertEqual(terms.read_text(encoding="utf-8"), TERMS_WITH_DEL_OPERATOR)


if __name__ == "__main__":
    unittest.main()
