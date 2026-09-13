#!/usr/bin/env python3
"""Language-local dependency-review marker tests."""
from __future__ import annotations

import importlib.util
import sys
import unittest
from pathlib import Path


MODULE_PATH = Path(__file__).with_name("translate_worker.py")
SPEC = importlib.util.spec_from_file_location("translate_worker_reviewed_test", MODULE_PATH)
assert SPEC and SPEC.loader
worker = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = worker
SPEC.loader.exec_module(worker)


class ReviewedPolicyTest(unittest.TestCase):
    def setUp(self) -> None:
        self.body = (
            '[A](/ko/math/a){: data-relation="required" reviewed="" }\n'
            'prose reviewed="" stays prose\n'
        )

    def test_korean_marker_is_hidden_from_translation_prompts(self) -> None:
        stripped = worker.strip_reviewed_attrs(self.body)
        self.assertIn('data-relation="required"', stripped)
        self.assertNotIn('required" reviewed=', stripped)
        self.assertIn('prose reviewed="" stays prose', stripped)

    def test_fresh_and_drift_remove_reviewed_but_polish_preserves_it(self) -> None:
        for reason in ("pending", "drift"):
            self.assertNotIn(
                'required" reviewed=', worker.apply_reviewed_policy(self.body, reason))
        self.assertEqual(worker.apply_reviewed_policy(self.body, "polish"), self.body)


if __name__ == "__main__":
    unittest.main()
