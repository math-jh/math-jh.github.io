#!/usr/bin/env python3
from __future__ import annotations

import importlib.util
import sys
import tempfile
import unittest
from pathlib import Path


MODULE_PATH = Path(__file__).with_name("section_anchor_gate.py")
SPEC = importlib.util.spec_from_file_location("section_anchor_gate_under_test", MODULE_PATH)
assert SPEC and SPEC.loader
gate = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = gate
SPEC.loader.exec_module(gate)


class CitationBracketNormalizationTest(unittest.TestCase):
    def test_normalizes_category_prefix_and_preserves_relation_ial(self) -> None:
        source = (
            'See [[Set Theory] §Functions, ⁋Proposition 5]'
            '(/en/math/set_theory/functions#prop5)'
            '{: data-relation="required" }.\n'
        )

        actual, repairs = gate.normalize_citation_brackets(source)

        self.assertEqual(
            actual,
            'See [\\[Set Theory\\] §Functions, ⁋Proposition 5]'
            '(/en/math/set_theory/functions#prop5)'
            '{: data-relation="required" }.\n',
        )
        self.assertEqual(repairs, [(1, "/en/math/set_theory/functions#prop5")])

    def test_removes_one_extra_open_before_an_already_escaped_citation(self) -> None:
        source = (
            '([[\\[Schemes\\] §Descent, ⁋Theorem 6]'
            '(/en/math/scheme_theory/descent#thm6))\n'
        )

        actual, repairs = gate.normalize_citation_brackets(source)

        self.assertEqual(
            actual,
            '([\\[Schemes\\] §Descent, ⁋Theorem 6]'
            '(/en/math/scheme_theory/descent#thm6))\n',
        )
        self.assertEqual(repairs, [(1, "/en/math/scheme_theory/descent#thm6")])

    def test_unwraps_an_already_escaped_citation(self) -> None:
        source = (
            '([[\\[Commutative Algebra\\] §Localization, ⁋Lemma 1]]'
            '(/en/math/commutative_algebra/localization#lem1))\n'
        )

        actual, repairs = gate.normalize_citation_brackets(source)

        self.assertEqual(
            actual,
            '([\\[Commutative Algebra\\] §Localization, ⁋Lemma 1]'
            '(/en/math/commutative_algebra/localization#lem1))\n',
        )
        self.assertEqual(
            repairs, [(1, "/en/math/commutative_algebra/localization#lem1")],
        )

    def test_unwraps_an_unescaped_category_citation(self) -> None:
        source = (
            '[[Commutative Algebra] §Localization, ⁋Lemma 1]]'
            '(/en/math/commutative_algebra/localization#lem1)'
            '{: data-relation="required" }\n'
        )

        actual, repairs = gate.normalize_citation_brackets(source)

        self.assertEqual(
            actual,
            '[\\[Commutative Algebra\\] §Localization, ⁋Lemma 1]'
            '(/en/math/commutative_algebra/localization#lem1)'
            '{: data-relation="required" }\n',
        )
        self.assertEqual(
            repairs, [(1, "/en/math/commutative_algebra/localization#lem1")],
        )

    def test_masks_math_code_raw_and_fenced_div_labels(self) -> None:
        broken = "[[Set Theory] §Functions](/en/math/set_theory/functions)"
        source = "\n".join([
            broken,
            f"`${broken}`",
            f"${broken}$",
            "$$",
            broken,
            "$$",
            "```markdown",
            broken,
            "```",
            "{% raw %}",
            broken,
            "{% endraw %}",
            f"::: misc {broken} {{#custom}}",
            "",
        ])

        actual, repairs = gate.normalize_citation_brackets(source)

        self.assertEqual(actual.count("[\\[Set Theory\\]"), 1)
        self.assertEqual(actual.count(broken), 6)
        self.assertEqual(repairs, [(1, "/en/math/set_theory/functions")])

    def test_only_target_limits_sweep_side_effects_and_is_idempotent(self) -> None:
        source = (
            "[[A] §One](/en/math/a#one) and "
            "[[B] §Two](/en/math/b#two)\n"
        )

        once, repairs = gate.normalize_citation_brackets(
            source, only_target="/en/math/a",
        )
        twice, second_repairs = gate.normalize_citation_brackets(
            once, only_target="/en/math/a",
        )

        self.assertIn("[\\[A\\] §One]", once)
        self.assertIn("[[B] §Two]", once)
        self.assertEqual(repairs, [(1, "/en/math/a#one")])
        self.assertEqual(twice, once)
        self.assertEqual(second_repairs, [])

    def test_run_gate_applies_normalization_before_mdlint(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            path = Path(tmp) / "post.md"
            path.write_text(
                "[[Set Theory] §Functions](/en/math/set_theory/functions)\n",
                encoding="utf-8",
            )

            result = gate.run_gate(path, apply=True, mdlint=False)

            self.assertTrue(result.changed)
            self.assertIn("[\\[Set Theory\\] §Functions]", path.read_text())


if __name__ == "__main__":
    unittest.main()
