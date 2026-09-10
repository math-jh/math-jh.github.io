#!/usr/bin/env python3
"""Focused tests for provider-chain recovery in dependency_classifier."""
from __future__ import annotations

import importlib.util
import json
import sys
import tempfile
import time
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

    def test_passes_only_missing_ids_to_next_provider(self) -> None:
        calls: list[list[str]] = []

        def primary(items: list[dict]) -> dict:
            calls.append([item["id"] for item in items])
            return {"items": [row("a"), row("c")]}

        def fallback(items: list[dict]) -> dict:
            calls.append([item["id"] for item in items])
            return {"items": [row("b")]}

        result = dc.request_complete_results(
            self.items, review=False, stage="test",
            attempts=[("primary", primary), ("fallback", fallback)],
        )

        self.assertEqual(set(result), {"a", "b", "c"})
        self.assertEqual(calls, [["a", "b", "c"], ["b"]])

    def test_escalates_missing_items_across_provider_chain(self) -> None:
        calls: list[tuple[str, list[str]]] = []

        def primary(items: list[dict]) -> dict:
            calls.append(("primary", [item["id"] for item in items]))
            return {"items": [row("a")]}

        def fallback(items: list[dict]) -> dict:
            calls.append(("fallback", [item["id"] for item in items]))
            return {"items": [row("b")]}

        def final(items: list[dict]) -> dict:
            calls.append(("final", [item["id"] for item in items]))
            return {"items": [row("b"), row("c")]}

        result = dc.request_complete_results(
            self.items, review=False, stage="test",
            attempts=[("primary", primary), ("fallback", fallback), ("final", final)],
        )

        self.assertEqual(set(result), {"a", "b", "c"})
        self.assertEqual(calls, [
            ("primary", ["a", "b", "c"]),
            ("fallback", ["b", "c"]),
            ("final", ["c"]),
        ])

    def test_raises_after_provider_chain_is_exhausted(self) -> None:
        calls: list[tuple[str, list[str]]] = []

        def primary(items: list[dict]) -> dict:
            calls.append(("primary", [item["id"] for item in items]))
            return {"items": [row("a")]}

        def fallback(items: list[dict]) -> dict:
            calls.append(("fallback", [item["id"] for item in items]))
            return {"items": []}

        with self.assertRaisesRegex(RuntimeError, "after provider chain"):
            dc.request_complete_results(
                self.items, review=False, stage="test",
                attempts=[("primary", primary), ("fallback", fallback)],
            )

        self.assertEqual(calls, [
            ("primary", ["a", "b", "c"]),
            ("fallback", ["b", "c"]),
        ])

    def test_first_pass_escalates_through_opus_to_codex(self) -> None:
        link = dc.Link("a", Path("unused"), 0, 0, "", "", "", None, None)
        with (
            patch.object(dc, "prompt_items", return_value=[{"id": "a"}]),
            patch.object(dc, "call_antigravity", return_value={"items": []}) as agy,
            patch.object(dc, "call_opus", return_value={"items": []}) as opus,
            patch.object(dc, "call_codex", return_value={"items": [row("a")]}) as codex,
            patch.object(dc, "provider_available", return_value=True),
        ):
            decisions, ambiguous = dc.classify([link])

        self.assertEqual(decisions, {"a": "required"})
        self.assertEqual(ambiguous, [])
        self.assertEqual(agy.call_count, 1)
        opus.assert_called_once_with([{"id": "a"}], review=False)
        codex.assert_called_once_with([{"id": "a"}], review=False)

    def test_first_pass_stops_at_opus_when_escalation_succeeds(self) -> None:
        link = dc.Link("a", Path("unused"), 0, 0, "", "", "", None, None)
        with (
            patch.object(dc, "prompt_items", return_value=[{"id": "a"}]),
            patch.object(dc, "call_antigravity", return_value={"items": []}) as agy,
            patch.object(dc, "call_opus", return_value={"items": [row("a")]}) as opus,
            patch.object(dc, "call_codex") as codex,
            patch.object(dc, "provider_available", return_value=True),
        ):
            decisions, ambiguous = dc.classify([link])

        self.assertEqual(decisions, {"a": "required"})
        self.assertEqual(ambiguous, [])
        self.assertEqual(agy.call_count, 1)
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
            patch.object(dc, "provider_available", return_value=True),
        ):
            decisions, ambiguous = dc.classify([link])

        self.assertEqual(decisions, {"a": "required"})
        self.assertEqual(ambiguous, [])
        agy.assert_called_once_with([{"id": "a"}], review=False)
        self.assertEqual(opus.call_count, 1)
        codex.assert_called_once_with([{"id": "a"}], review=True)

    def test_codex_fallback_uses_multi_auth_read_only_structured_exec(self) -> None:
        def fake_run(argv: list[str], **kwargs):
            self.assertEqual(argv[0], dc.CODEX_BIN)
            self.assertEqual(dc.CODEX_BIN, str(Path.home() / ".npm-global/bin/codex-multi-auth-codex"))
            self.assertEqual(argv[argv.index("--model") + 1], "gpt-5.6-luna")
            self.assertIn('model_reasoning_effort="medium"', argv)
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

    def test_codex_review_uses_terra_medium(self) -> None:
        reviewed = {"id": "a", "relation": "required", "reason": "test"}

        def fake_run(argv: list[str], **kwargs):
            self.assertEqual(argv[argv.index("--model") + 1], "gpt-5.6-terra")
            self.assertIn('model_reasoning_effort="medium"', argv)
            output_path = Path(argv[argv.index("--output-last-message") + 1])
            output_path.write_text(json.dumps({"items": [reviewed]}), encoding="utf-8")
            return SimpleNamespace(returncode=0, stderr="")

        with patch.object(dc.subprocess, "run", side_effect=fake_run):
            result = dc.call_codex([{"id": "a"}], review=True)

        self.assertEqual(result, {"items": [reviewed]})


class QuotaRoutingTest(unittest.TestCase):
    def quota_state(self, *, utilization: float, enabled: bool = True) -> dict:
        return {
            "ok": True,
            "enabled": enabled,
            "ts": time.time(),
            "limit5h": {"utilization": utilization, "resetTime": "2099-01-01T00:00:00Z"},
            "weekly": {"utilization": 0.1, "resetTime": "2099-01-01T00:00:00Z"},
        }

    def write_state(self, root: Path, name: str, state: dict) -> None:
        (root / f"{name}_quota.json").write_text(json.dumps(state), encoding="utf-8")

    def test_single_provider_closes_at_governor_threshold(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            self.write_state(root, "claude", self.quota_state(utilization=0.70))
            with patch.object(dc, "QUOTA_STATE_DIR", root):
                self.assertFalse(dc.provider_available("Claude Opus"))

    def test_codex_pool_stays_open_when_one_account_is_available(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            self.write_state(root, "codex1", self.quota_state(utilization=0.80))
            self.write_state(root, "codex2", self.quota_state(utilization=0.20))
            with patch.object(dc, "QUOTA_STATE_DIR", root):
                self.assertTrue(dc.provider_available("Codex"))

    def test_unknown_codex_member_is_fail_open(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            self.write_state(root, "codex1", self.quota_state(utilization=0.80))
            with patch.object(dc, "QUOTA_STATE_DIR", root):
                self.assertTrue(dc.provider_available("Codex"))


class LocalOnlyPolicyTest(unittest.TestCase):
    def test_untracked_gromov_witten_unit_is_local_only(self) -> None:
        path = dc.LOCAL_ONLY_POST_ROOTS[0] / "ko" / "draft.md"
        result = SimpleNamespace(returncode=0, stdout="", stderr="")
        with patch.object(dc.subprocess, "run", return_value=result) as run:
            self.assertTrue(dc.is_local_only_untracked_unit([path]))
        self.assertIn("ls-files", run.call_args.args[0])

    def test_tracked_gromov_witten_post_still_uses_commit_path(self) -> None:
        path = dc.LOCAL_ONLY_POST_ROOTS[0] / "ko" / "published.md"
        rel = str(path.relative_to(dc.ROOT))
        result = SimpleNamespace(returncode=0, stdout=rel + "\0", stderr="")
        with patch.object(dc.subprocess, "run", return_value=result):
            self.assertFalse(dc.is_local_only_untracked_unit([path]))

    def test_other_untracked_paths_do_not_gain_local_only_exception(self) -> None:
        path = dc.ROOT / "_posts" / "Math" / "Topology" / "ko" / "draft.md"
        with patch.object(dc.subprocess, "run") as run:
            self.assertFalse(dc.is_local_only_untracked_unit([path]))
        run.assert_not_called()


class ParallelStateTest(unittest.TestCase):
    def test_unit_updates_merge_without_overwriting_other_process(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            state_path = root / "state.json"
            with (
                patch.object(dc, "STATE_DIR", root),
                patch.object(dc, "STATE_PATH", state_path),
                patch.object(dc, "STATE_LOCK_PATH", root / "state.lock"),
            ):
                dc.merge_unit_states({"ko-a+en-a": {"status": "done"}})
                dc.merge_unit_states({"ko-b+en-b": {"status": "error"}})
                saved = json.loads(state_path.read_text(encoding="utf-8"))

        self.assertEqual(saved["units"]["ko-a+en-a"]["status"], "done")
        self.assertEqual(saved["units"]["ko-b+en-b"]["status"], "error")


class SelectionTest(unittest.TestCase):
    def test_unpublished_ko_and_en_pair_is_included(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            ko_path = root / "_posts/Math/Test/ko/draft.md"
            en_path = root / "_posts/Math/Test/en/draft.md"
            ko_path.parent.mkdir(parents=True)
            en_path.parent.mkdir(parents=True)
            ko_path.write_text("ko", encoding="utf-8")
            en_path.write_text("en", encoding="utf-8")
            ko = SimpleNamespace(lang="ko", published=False, path=ko_path)
            en = SimpleNamespace(lang="en", published=False, path=en_path)
            link = dc.Link("draft-link", ko_path, 0, 1, "", "", "#x", None, None)
            updates: dict[str, dict] = {}
            with (
                patch.object(dc, "ROOT", root),
                patch.object(dc, "_POSTS", [ko, en]),
                patch.object(dc, "en_counterpart", side_effect=lambda p, _all: en if p is ko else None),
                patch.object(dc, "dirty_paths", return_value=[]),
                patch.object(dc, "extract_links", side_effect=lambda p, _text: [link] if p == ko_path else []),
            ):
                selected = dc.select_unit({}, updates)

            self.assertIsNotNone(selected)
            paths, _texts, links, lease = selected
            try:
                self.assertEqual(paths, [ko_path, en_path])
                self.assertEqual(links, [link])
            finally:
                lease.release()


if __name__ == "__main__":
    unittest.main()
