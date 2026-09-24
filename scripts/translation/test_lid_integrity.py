#!/usr/bin/env python3
"""번역이 실어 나르는 data-lid 의 무결성 게이트 테스트."""
from __future__ import annotations

import importlib.util
import sys
import unittest
from pathlib import Path


MODULE_PATH = Path(__file__).with_name("translate_worker.py")
SPEC = importlib.util.spec_from_file_location("translate_worker_lid_test", MODULE_PATH)
assert SPEC and SPEC.loader
worker = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = worker
SPEC.loader.exec_module(worker)


class LidIntegrityTest(unittest.TestCase):
    def setUp(self) -> None:
        self.ko = (
            '[가](/ko/math/a#def1){: data-lid="k7m2x" }\n'
            '[나](/ko/math/a#def1){: data-lid="q3z9b" }\n'
        )

    def test_known_lids_survive(self) -> None:
        en = ('[A](/en/math/a#def1){: data-lid="k7m2x" }\n'
              '[B](/en/math/a#def1){: data-lid="q3z9b" }\n')
        out, notes = worker.enforce_lid_integrity(en, self.ko)
        self.assertEqual(out, en)
        self.assertEqual(notes, [])

    def test_invented_lid_is_dropped(self) -> None:
        en = '[A](/en/math/a#def1){: data-lid="zzzzz" }\n'
        out, notes = worker.enforce_lid_integrity(en, self.ko)
        self.assertEqual(out, "[A](/en/math/a#def1)\n")
        self.assertEqual(len(notes), 1)
        self.assertIn("zzzzz", notes[0])

    def test_duplicate_keeps_only_the_first(self) -> None:
        en = ('[A](/en/math/a#def1){: data-lid="k7m2x" }\n'
              '[B](/en/math/a#def1){: data-lid="k7m2x" }\n')
        out, notes = worker.enforce_lid_integrity(en, self.ko)
        self.assertEqual(out.count('data-lid="k7m2x"'), 1)
        self.assertEqual(out, '[A](/en/math/a#def1){: data-lid="k7m2x" }\n'
                              '[B](/en/math/a#def1)\n')
        self.assertEqual(len(notes), 1)

    def test_merged_link_leaves_the_other_lid_unused(self) -> None:
        """두 KO 링크가 한 EN 링크로 합쳐지면 남은 lid 하나만 실려 온다."""
        en = '[A and B](/en/math/a#def1){: data-lid="q3z9b" }\n'
        out, notes = worker.enforce_lid_integrity(en, self.ko)
        self.assertEqual(out, en)
        self.assertEqual(notes, [])

    def test_prose_mentioning_an_unknown_lid_is_untouched(self) -> None:
        """IAL 밖의 같은 글자는 건드리지 않는다 — 산문은 링크 속성이 아니다."""
        en = 'Workshop note: an identifier such as data-lid="zzzzz" names one link.\n'
        out, notes = worker.enforce_lid_integrity(en, self.ko)
        self.assertEqual(out, en)
        self.assertEqual(notes, [])


if __name__ == "__main__":
    unittest.main()
