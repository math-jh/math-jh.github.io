#!/usr/bin/env python3
"""Focused tests for incomplete-response recovery in dependency_classifier."""
from __future__ import annotations

import importlib.util
import json
import sys
import unittest
from pathlib import Path
from types import SimpleNamespace
from unittest.mock import patch


MODULE_PATH = Path(__file__).with_name("dependency_classifier.py")
SPEC = importlib.util.spec_from_file_location("dependency_classifier_under_test", MODULE_PATH)
assert SPEC and SPEC.loader
dc = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = dc
SPEC.loader.exec_module(dc)


def row(ident: str, *, confidence: str = "high") -> dict:
    return {"id": ident, "relation": "required", "confidence": confidence, "reason": "test"}


class IncompleteResponseRecoveryTest(unittest.TestCase):
    def setUp(self) -> None:
        self.items = [{"id": ident} for ident in ("a", "b", "c")]

    def test_retries_only_missing_ids_and_keeps_valid_rows(self) -> None:
        calls: list[list[str]] = []

        def primary(items: list[dict]) -> dict:
            calls.append([item["id"] for item in items])
            if len(calls) == 1:
                return {"items": [row("a"), row("c")]}
            return {"items": [row("b")]}

        def unused_fallback(items: list[dict]) -> dict:
            self.fail(f"fallback should not run: {items}")

        result = dc.request_complete_results(
            self.items, review=False, stage="test", primary_name="primary",
            primary=primary, fallback_name="fallback", fallback=unused_fallback,
        )

        self.assertEqual(set(result), {"a", "b", "c"})
        self.assertEqual(calls, [["a", "b", "c"], ["b"]])

    def test_falls_back_only_for_items_still_missing_after_retry(self) -> None:
        primary_calls: list[list[str]] = []
        fallback_calls: list[list[str]] = []

        def primary(items: list[dict]) -> dict:
            primary_calls.append([item["id"] for item in items])
            return {"items": [row("a")]} if len(primary_calls) == 1 else {"items": []}

        def fallback(items: list[dict]) -> dict:
            fallback_calls.append([item["id"] for item in items])
            return {"items": [row("b"), row("c")]}

        result = dc.request_complete_results(
            self.items, review=False, stage="test", primary_name="primary",
            primary=primary, fallback_name="fallback", fallback=fallback,
        )

        self.assertEqual(set(result), {"a", "b", "c"})
        self.assertEqual(primary_calls, [["a", "b", "c"], ["b", "c"]])
        self.assertEqual(fallback_calls, [["b", "c"]])

    def test_raises_only_after_retry_and_fallback_are_exhausted(self) -> None:
        calls: list[tuple[str, list[str]]] = []

        def primary(items: list[dict]) -> dict:
            calls.append(("primary", [item["id"] for item in items]))
            return {"items": [row("a")]}

        def fallback(items: list[dict]) -> dict:
            calls.append(("fallback", [item["id"] for item in items]))
            return {"items": []}

        with self.assertRaisesRegex(RuntimeError, "after retry and fallback"):
            dc.request_complete_results(
                self.items, review=False, stage="test", primary_name="primary",
                primary=primary, fallback_name="fallback", fallback=fallback,
            )

        self.assertEqual(calls, [
            ("primary", ["a", "b", "c"]),
            ("primary", ["b", "c"]),
            ("fallback", ["b", "c"]),
        ])

    def test_first_pass_escalates_through_opus_to_codex(self) -> None:
        link = dc.Link("a", Path("unused"), 0, 0, "", "", "", None, None)
        with (
            patch.object(dc, "prompt_items", return_value=[{"id": "a"}]),
            patch.object(dc, "call_antigravity", return_value={"items": []}) as agy,
            patch.object(dc, "call_opus", return_value={"items": []}) as opus,
            patch.object(dc, "call_codex", return_value={"items": [row("a")]}) as codex,
        ):
            decisions, ambiguous = dc.classify([link])

        self.assertEqual(decisions, {"a": "required"})
        self.assertEqual(ambiguous, [])
        self.assertEqual(agy.call_count, 2)
        opus.assert_called_once_with([{"id": "a"}], review=False)
        codex.assert_called_once_with([{"id": "a"}], review=False)

    def test_first_pass_stops_at_opus_when_escalation_succeeds(self) -> None:
        link = dc.Link("a", Path("unused"), 0, 0, "", "", "", None, None)
        with (
            patch.object(dc, "prompt_items", return_value=[{"id": "a"}]),
            patch.object(dc, "call_antigravity", return_value={"items": []}) as agy,
            patch.object(dc, "call_opus", return_value={"items": [row("a")]}) as opus,
            patch.object(dc, "call_codex") as codex,
        ):
            decisions, ambiguous = dc.classify([link])

        self.assertEqual(decisions, {"a": "required"})
        self.assertEqual(ambiguous, [])
        self.assertEqual(agy.call_count, 2)
        opus.assert_called_once_with([{"id": "a"}], review=False)
        codex.assert_not_called()

    def test_opus_review_falls_back_to_codex_not_antigravity(self) -> None:
        link = dc.Link("a", Path("unused"), 0, 0, "", "", "", None, None)
        first = {"items": [row("a", confidence="medium")]}
        reviewed = {"items": [{"id": "a", "relation": "required", "reason": "test"}]}
        with (
            patch.object(dc, "prompt_items", return_value=[{"id": "a"}]),
            patch.object(dc, "call_antigravity", return_value=first) as agy,
            patch.object(dc, "call_opus", return_value={"items": []}) as opus,
            patch.object(dc, "call_codex", return_value=reviewed) as codex,
        ):
            decisions, ambiguous = dc.classify([link])

        self.assertEqual(decisions, {"a": "required"})
        self.assertEqual(ambiguous, [])
        agy.assert_called_once_with([{"id": "a"}], review=False)
        self.assertEqual(opus.call_count, 2)
        codex.assert_called_once_with([{"id": "a"}], review=True)

    def test_codex_fallback_uses_multi_auth_read_only_structured_exec(self) -> None:
        def fake_run(argv: list[str], **kwargs):
            self.assertEqual(argv[0], dc.CODEX_BIN)
            self.assertEqual(dc.CODEX_BIN, str(Path.home() / ".npm-global/bin/codex-multi-auth-codex"))
            self.assertIn("--sandbox", argv)
            self.assertEqual(argv[argv.index("--sandbox") + 1], "read-only")
            self.assertIn("--ephemeral", argv)
            self.assertIn("--output-schema", argv)
            self.assertNotIn("--ignore-user-config", argv)
            schema_path = Path(argv[argv.index("--output-schema") + 1])
            schema = json.loads(schema_path.read_text(encoding="utf-8"))
            self.assertEqual(schema["properties"]["items"]["minItems"], 1)
            output_path = Path(argv[argv.index("--output-last-message") + 1])
            output_path.write_text(json.dumps({"items": [row("a")]}), encoding="utf-8")
            return SimpleNamespace(returncode=0, stderr="")

        with patch.object(dc.subprocess, "run", side_effect=fake_run):
            result = dc.call_codex([{"id": "a"}], review=False)

        self.assertEqual(result, {"items": [row("a")]})


if __name__ == "__main__":
    unittest.main()
