#!/usr/bin/env python3
"""Focused tests for provider-chain recovery in dependency_classifier."""
from __future__ import annotations

import importlib.util
import json
import sys
import tempfile
import time
import unittest
from contextlib import ExitStack
from pathlib import Path
from types import SimpleNamespace
from unittest.mock import patch


MODULE_PATH = Path(__file__).with_name("dependency_classifier.py")
SPEC = importlib.util.spec_from_file_location("dependency_classifier_under_test", MODULE_PATH)
assert SPEC and SPEC.loader
dc = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = dc
SPEC.loader.exec_module(dc)


class PostScopeTest(unittest.TestCase):
    def test_classifier_scans_math_posts_only(self) -> None:
        self.assertTrue(dc._POSTS)
        self.assertTrue(all(post.path.is_relative_to(dc.MATH_POST_ROOT) for post in dc._POSTS))


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
            self.items, mode="first", stage="test",
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
            self.items, mode="first", stage="test",
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
                self.items, mode="first", stage="test",
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
            decisions, _by, ambiguous = dc.classify([link])

        self.assertEqual(decisions, {"a": "required"})
        self.assertEqual(ambiguous, [])
        self.assertEqual(agy.call_count, 1)
        opus.assert_called_once_with([{"id": "a"}], mode="first")
        codex.assert_called_once_with([{"id": "a"}], mode="first")

    def test_first_pass_stops_at_opus_when_escalation_succeeds(self) -> None:
        link = dc.Link("a", Path("unused"), 0, 0, "", "", "", None, None)
        with (
            patch.object(dc, "prompt_items", return_value=[{"id": "a"}]),
            patch.object(dc, "call_antigravity", return_value={"items": []}) as agy,
            patch.object(dc, "call_opus", return_value={"items": [row("a")]}) as opus,
            patch.object(dc, "call_codex") as codex,
            patch.object(dc, "provider_available", return_value=True),
        ):
            decisions, _by, ambiguous = dc.classify([link])

        self.assertEqual(decisions, {"a": "required"})
        self.assertEqual(ambiguous, [])
        self.assertEqual(agy.call_count, 1)
        opus.assert_called_once_with([{"id": "a"}], mode="first")
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
            decisions, _by, ambiguous = dc.classify([link])

        self.assertEqual(decisions, {"a": "required"})
        self.assertEqual(ambiguous, [])
        agy.assert_called_once_with([{"id": "a"}], mode="first")
        self.assertEqual(opus.call_count, 1)
        codex.assert_called_once_with([{"id": "a"}], mode="review")

    def test_codex_fallback_uses_multi_auth_read_only_structured_exec(self) -> None:
        def fake_run(argv: list[str], **kwargs):
            self.assertEqual(argv[0], dc.CODEX_BIN)
            self.assertEqual(dc.CODEX_BIN, str(Path.home() / ".npm-global/bin/codex-multi-auth-codex"))
            self.assertEqual(argv[argv.index("--model") + 1], "gpt-5.6-sol")
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
            result = dc.call_codex([{"id": "a"}], mode="first")

        self.assertEqual(result, {"items": [row("a")]})

    def test_codex_review_uses_sol_medium(self) -> None:
        reviewed = {"id": "a", "relation": "required", "reason": "test"}

        def fake_run(argv: list[str], **kwargs):
            self.assertEqual(argv[argv.index("--model") + 1], "gpt-5.6-sol")
            self.assertIn('model_reasoning_effort="medium"', argv)
            output_path = Path(argv[argv.index("--output-last-message") + 1])
            output_path.write_text(json.dumps({"items": [reviewed]}), encoding="utf-8")
            return SimpleNamespace(returncode=0, stderr="")

        with patch.object(dc.subprocess, "run", side_effect=fake_run):
            result = dc.call_codex([{"id": "a"}], mode="review")

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
            patch.object(dc, "HOLDS_PATH", root / "holds.json"),
            ):
                dc.merge_unit_states({"ko-a+en-a": {"status": "done"}})
                dc.merge_unit_states({"ko-b+en-b": {"status": "error"}})
                saved = json.loads(state_path.read_text(encoding="utf-8"))

        self.assertEqual(saved["units"]["ko-a+en-a"]["status"], "done")
        self.assertEqual(saved["units"]["ko-b+en-b"]["status"], "error")


R = dc.ledger.Record


def digest(*texts: str) -> str:
    """unit_digest of a unit whose links have no records."""
    return dc.sha("\0".join(texts) + "\0\0")


def open_side(link, path):
    """extract_links stand-in: ``link`` is the only open link, in ``path``."""
    return lambda p, _t, tagged=False, review=False, records=None: (
        [] if tagged or review else ([link] if p == path else []))


class SelectionTest(unittest.TestCase):
    def test_reviewed_record_is_the_durable_completion_marker(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            path = root / "_posts/Math/Test/ko/post.md"
            path.parent.mkdir(parents=True)
            text = '[Done](#p){: data-lid="aaaaa" }\n'
            path.write_text(text, encoding="utf-8")
            post = SimpleNamespace(lang="ko", published=True, path=path)
            updates: dict[str, dict] = {}
            with (
                patch.object(dc, "ROOT", root),
                patch.object(dc, "HOLDS_PATH", root / "holds.json"),
                patch.object(dc, "RECORDS", {"aaaaa": R("required", True)}),
                patch.object(dc, "_POSTS", [post]),
                patch.object(dc, "en_counterpart", return_value=None),
                patch.object(dc, "dirty_paths", return_value=[]),
            ):
                links = dc.extract_links(path, text, tagged=True)
                selected = dc.select_unit({}, updates)

            self.assertEqual([(x.lid, x.relation, x.reviewed) for x in links],
                             [("aaaaa", "required", True)])
            self.assertIsNone(selected)
            self.assertEqual(next(iter(updates.values()))["reviewed_marker_version"], 1)

    def test_review_outcome_stamps_agreement_and_marks_disagreement(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            path = root / "_posts/Math/Test/ko/post.md"
            path.parent.mkdir(parents=True)
            text = '[A](#a){: data-lid="aaaaa" }\n[B](#b){: data-lid="bbbbb" }\n'
            records = {"aaaaa": R("required"), "bbbbb": R("weak", True)}
            with patch.object(dc, "ROOT", root), patch.object(dc, "RECORDS", records):
                links = dc.extract_links(path, text, tagged=True)
                dc.record_review_outcome(links, {links[1].ident})

            self.assertEqual(records["aaaaa"], R("required", True))
            self.assertEqual(records["bbbbb"], R(dc.REVIEW_RELATION, False))
            self.assertEqual(text, path.read_text(encoding="utf-8") if path.exists() else text)

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
            link = dc.Link("draft-link", ko_path, 0, 1, "", "", "#x", None, None, lid="aaaaa")
            updates: dict[str, dict] = {}
            with (
                patch.object(dc, "ROOT", root),
                patch.object(dc, "HOLDS_PATH", root / "holds.json"),
                patch.object(dc, "_POSTS", [ko, en]),
                patch.object(dc, "en_counterpart", side_effect=lambda p, _all: en if p is ko else None),
                patch.object(dc, "dirty_paths", return_value=[]),
                patch.object(dc, "extract_links", side_effect=open_side(link, ko_path)),
            ):
                selected = dc.select_unit({}, updates)

            self.assertIsNotNone(selected)
            stage, paths, _texts, links, lease = selected
            self.assertEqual(stage, "first")
            try:
                self.assertEqual(paths, [ko_path, en_path])
                self.assertEqual(links, [link])
            finally:
                lease.release()

    def unit(self, root: Path, ko_text: str, en_text: str):
        ko_path = root / "_posts/Math/Test/ko/a.md"
        en_path = root / "_posts/Math/Test/en/a.md"
        for path, text in ((ko_path, ko_text), (en_path, en_text)):
            path.parent.mkdir(parents=True, exist_ok=True)
            path.write_text(text, encoding="utf-8")
        ko = SimpleNamespace(lang="ko", published=True, path=ko_path)
        en = SimpleNamespace(lang="en", published=True, path=en_path)
        return ko_path, en_path, [
            patch.object(dc, "ROOT", root),
            patch.object(dc, "HOLDS_PATH", root / "holds.json"),
            patch.object(dc, "_POSTS", [ko, en]),
            patch.object(dc, "en_counterpart", side_effect=lambda p, _all: en if p is ko else None),
            patch.object(dc, "dirty_paths", return_value=[]),
            patch.object(dc, "provider_available", return_value=True),
        ]

    def test_english_twin_shares_the_korean_record(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            ko_path, en_path, patches = self.unit(
                Path(tmp), '[가](#a){: data-lid="aaaaa" }\n', '[A](#a){: data-lid="aaaaa" }\n')
            with ExitStack() as stack:
                for item in patches:
                    stack.enter_context(item)
                stack.enter_context(patch.object(dc, "RECORDS", {}))
                first = dc.select_unit({}, {})
                try:
                    self.assertEqual(first[0], "first")
                    self.assertEqual([x.source for x in first[3]], [ko_path])
                finally:
                    first[4].release()
                stack.enter_context(patch.object(dc, "RECORDS", {"aaaaa": R("weak", True)}))
                self.assertIsNone(dc.select_unit({}, {}))

    def test_english_only_link_is_judged_on_its_own(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            ko_path, en_path, patches = self.unit(
                Path(tmp), '[가](#a){: data-lid="aaaaa" }\n',
                '[A](#a){: data-lid="aaaaa" } [B](#b){: data-lid="zzzzz" }\n')
            with ExitStack() as stack:
                for item in patches:
                    stack.enter_context(item)
                stack.enter_context(patch.object(dc, "RECORDS", {"aaaaa": R("weak", True)}))
                first = dc.select_unit({}, {})
                try:
                    self.assertEqual([(x.source, x.lid) for x in first[3]], [(en_path, "zzzzz")])
                finally:
                    first[4].release()

    def test_link_without_lid_waits_for_the_mint(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            _ko, _en, patches = self.unit(Path(tmp), '[가](#a)\n', '[A](#a)\n')
            with ExitStack() as stack:
                for item in patches:
                    stack.enter_context(item)
                stack.enter_context(patch.object(dc, "RECORDS", {}))
                self.assertIsNone(dc.select_unit({}, {}))

    def test_normalized_hidden_link_reopens_first_then_verifies_the_unit(self) -> None:
        """A completed unit must classify a newly visible link before re-verifying."""
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            path = root / "_posts/Math/Test/en/draft.md"
            path.parent.mkdir(parents=True)
            hidden = (
                '[[Set Theory] §Functions](#new){: data-lid="nnnnn" }\n'
                '[Old](#old){: data-lid="ooooo" }\n'
            )
            normalized = (
                '[\\[Set Theory\\] §Functions](#new){: data-lid="nnnnn" }\n'
                '[Old](#old){: data-lid="ooooo" }\n'
            )
            path.write_text(hidden, encoding="utf-8")
            post = SimpleNamespace(lang="en", published=True, path=path)
            records = {"ooooo": R("weak", True)}
            with (
                patch.object(dc, "ROOT", root),
                patch.object(dc, "HOLDS_PATH", root / "holds.json"),
                patch.object(dc, "RECORDS", records),
                patch.object(dc, "_POSTS", [post]),
                patch.object(dc, "by_permalink", return_value=post),
                patch.object(dc, "dirty_paths", return_value=[]),
                patch.object(dc, "provider_available", return_value=True),
            ):
                key = dc.unit_key([path])
                old_tagged = dc.extract_links(path, hidden, tagged=True)
                old_state = {"units": {key: {
                    "status": "done",
                    "hash": dc.unit_digest([path], {path: hidden}),
                    "verified_hash": dc.unit_digest([path], {path: hidden}),
                    "verified_content_hash": dc.verification_fingerprint(
                        [path], {path: hidden}, set()),
                    "decided_by": {old_tagged[0].ident: "Claude Opus"},
                    "reviewed_marker_version": 1,
                }}}

                self.assertIsNone(dc.select_unit(old_state, {}))
                path.write_text(normalized, encoding="utf-8")
                first = dc.select_unit(old_state, {})
                self.assertIsNotNone(first)
                try:
                    self.assertEqual(first[0], "first")
                    self.assertEqual([link.target for link in first[3]], ["#new"])
                    new_link = first[3][0]
                finally:
                    first[4].release()

                dc.record_decisions([new_link], {new_link.ident: "required"})
                after_first = {"units": {key: {
                    "status": "done",
                    "hash": dc.unit_digest([path], {path: normalized}),
                    "decided_by": {
                        **old_state["units"][key]["decided_by"],
                        new_link.ident: "Antigravity",
                    },
                }}}
                verify = dc.select_unit(after_first, {})
                self.assertIsNotNone(verify)
                try:
                    self.assertEqual(verify[0], "verify")
                    self.assertEqual([link.target for link in verify[3]], ["#new"])
                finally:
                    verify[4].release()


class RetryRoundTest(unittest.TestCase):
    """Ambiguous units escalate to whole-article review, then give up."""

    def make_unit(self, root: Path) -> tuple[Path, object, dc.Link]:
        path = root / "_posts/Math/Test/ko/draft.md"
        path.parent.mkdir(parents=True)
        path.write_text("ko body", encoding="utf-8")
        post = SimpleNamespace(lang="ko", published=True, path=path)
        link = dc.Link("draft-link", path, 0, 1, "", "", "#x", None, None, lid="aaaaa")
        return path, post, link

    def base(self, root: Path, path: Path, post: object, link: dc.Link) -> list:
        return [
            patch.object(dc, "ROOT", root),
            patch.object(dc, "HOLDS_PATH", root / "holds.json"),
            patch.object(dc, "RECORDS", {}),
            patch.object(dc, "_POSTS", [post]),
            patch.object(dc, "en_counterpart", return_value=None),
            patch.object(dc, "dirty_paths", return_value=[]),
            patch.object(dc, "extract_links", side_effect=open_side(link, path)),
        ]

    def run_round(self, root: Path, state_path: Path, path: Path, post: object, link: dc.Link,
                  seen: list[int]) -> None:
        with ExitStack() as stack:
            for item in self.base(root, path, post, link) + [
                patch.object(dc, "STATE_DIR", root),
                patch.object(dc, "STATE_PATH", state_path),
                patch.object(dc, "STATE_LOCK_PATH", root / "state.lock"),
                patch.object(dc, "mint_lids"),  # 식별자 발급은 전용 테스트에서 본다
                patch.object(dc, "classify", side_effect=lambda links, rnd=1: (
                    seen.append(rnd), ({}, {}, [{"id": link.ident, "reason": "unclear"}]))[1]),
            ]:
                stack.enter_context(item)
            dc.process_once()

    def test_rounds_escalate_then_exhaust(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            state_path = root / "state.json"
            path, post, link = self.make_unit(root)
            seen: list[int] = []
            for _ in range(dc.MAX_ROUNDS):
                # Each round starts after the previous backoff has elapsed.
                if state_path.exists():
                    saved = json.loads(state_path.read_text(encoding="utf-8"))
                    for entry in saved["units"].values():
                        entry.pop("retry_after", None)
                    state_path.write_text(json.dumps(saved), encoding="utf-8")
                self.run_round(root, state_path, path, post, link, seen)
            saved = json.loads(state_path.read_text(encoding="utf-8"))
            entry = next(iter(saved["units"].values()))

            self.assertEqual(seen, list(range(1, dc.MAX_ROUNDS + 1)))
            self.assertEqual(entry["status"], "exhausted")
            self.assertEqual(entry["rounds"], dc.MAX_ROUNDS)
            self.assertNotIn("retry_after", entry)

            # Exhausted units stay out of the queue while their content is unchanged.
            with ExitStack() as stack:
                for item in self.base(root, path, post, link):
                    stack.enter_context(item)
                self.assertIsNone(dc.select_unit(saved, {}))

            # A new link changes the file, so the unit is picked up again.
            path.write_text("ko body + new link", encoding="utf-8")
            with ExitStack() as stack:
                for item in self.base(root, path, post, link):
                    stack.enter_context(item)
                selected = dc.select_unit(saved, {})
            self.assertIsNotNone(selected)
            selected[4].release()

    def test_legacy_ambiguous_entry_resumes_at_full_article_round(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            state_path = root / "state.json"
            path, post, link = self.make_unit(root)
            with patch.object(dc, "ROOT", root):
                key = dc.unit_key([path])
            state_path.write_text(json.dumps({"units": {key: {
                "status": "ambiguous", "hash": digest("ko body"), "items": [],
            }}}), encoding="utf-8")
            seen: list[int] = []
            self.run_round(root, state_path, path, post, link, seen)

            self.assertEqual(seen, [2])

    def test_full_context_sends_whole_articles(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            source = root / "source.md"
            target = root / "target.md"
            body = "\n\n".join(f"paragraph {i}" for i in range(40))
            source.write_text(body, encoding="utf-8")
            target.write_text("target head\n\ntarget tail", encoding="utf-8")
            link = dc.Link("x", source, 0, 1, "", "", "/ko/math/t", None, None)
            post = SimpleNamespace(lang="ko", published=True, path=target)
            with (
                patch.object(dc, "_POSTS", [post]),
                patch.object(dc, "by_permalink", return_value=post),
            ):
                narrow = dc.target_context(link, True)
                wide = dc.target_context(link, True, True)

            self.assertEqual(wide[0], source.read_text(encoding="utf-8"))
            self.assertEqual(wide[1], target.read_text(encoding="utf-8"))
            self.assertNotEqual(narrow[0], wide[0])
            self.assertEqual(
                dc.prompt_items([link], True, True)[0]["context_scope"], "full-article")


class BacklogCompletionTest(unittest.TestCase):
    def test_exhausted_unit_does_not_hold_the_backlog_open(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            path = root / "_posts/Math/Test/ko/draft.md"
            path.parent.mkdir(parents=True)
            path.write_text("ko body", encoding="utf-8")
            post = SimpleNamespace(lang="ko", published=True, path=path)
            link = dc.Link("draft-link", path, 0, 1, "", "", "#x", None, None, lid="aaaaa")
            state_path = root / "state.json"
            with patch.object(dc, "ROOT", root):
                key = dc.unit_key([path])
            state_path.write_text(json.dumps({"units": {key: {
                "status": "exhausted", "hash": digest("ko body"), "rounds": dc.MAX_ROUNDS,
            }}}), encoding="utf-8")
            with (
                patch.object(dc, "ROOT", root),
                patch.object(dc, "STATE_PATH", state_path),
                patch.object(dc, "HOLDS_PATH", root / "holds.json"),
                patch.object(dc, "RECORDS", {}),
                patch.object(dc, "_POSTS", [post]),
                patch.object(dc, "en_counterpart", return_value=None),
                patch.object(dc, "extract_links", side_effect=open_side(link, path)),
            ):
                self.assertTrue(dc.backlog_complete())
                path.write_text("ko body + new link", encoding="utf-8")
                self.assertFalse(dc.backlog_complete())


BODY = (
    "---\ntitle: t\n---\n\n"
    "첫 문단.\n\n"
    "본문에서 [가](/ko/math/a){: data-lid=\"aaaaa\" } 를 쓰고\n"
    "[나](/ko/math/b){: .x data-lid=\"bbbbb\" } 도 쓰고 [다](/ko/math/c){: data-lid=\"ccccc\" } 는 아직이다.\n"
)
BODY_RECORDS = {"aaaaa": R("required"), "bbbbb": R("weak")}


class RelationSideTest(unittest.TestCase):
    """The ledger record decides a link's side; the ident spans all of them."""

    def setUp(self) -> None:
        self.tmp = tempfile.TemporaryDirectory()
        self.root = Path(self.tmp.name)
        self.path = self.root / "_posts/Math/Test/ko/draft.md"
        self.path.parent.mkdir(parents=True)
        self.path.write_text(BODY, encoding="utf-8")
        self.addCleanup(self.tmp.cleanup)

    def links(self, records: dict, *, tagged: bool = False, review: bool = False) -> list:
        post = SimpleNamespace(lang="ko", published=True, path=self.path)
        with (
            patch.object(dc, "ROOT", self.root),
            patch.object(dc, "by_permalink", return_value=post),
        ):
            return dc.extract_links(self.path, BODY, tagged=tagged, review=review,
                                    records=records)

    def test_tagged_and_untagged_sides_are_complementary(self) -> None:
        tagged = self.links(BODY_RECORDS, tagged=True)
        untagged = self.links(BODY_RECORDS)

        self.assertEqual([x.relation for x in tagged], ["required", "weak"])
        self.assertEqual([x.target for x in untagged], ["/ko/math/c"])
        self.assertEqual([x.lid for x in untagged], ["ccccc"])

    def test_review_marker_is_a_side_of_its_own(self) -> None:
        records = {**BODY_RECORDS, "aaaaa": R(dc.REVIEW_RELATION)}
        review = self.links(records, review=True)

        self.assertEqual([x.lid for x in review], ["aaaaa"])
        self.assertEqual([x.lid for x in self.links(records, tagged=True)], ["bbbbb"])
        self.assertEqual([x.lid for x in self.links(records)], ["ccccc"])

    def test_ident_does_not_depend_on_the_record(self) -> None:
        with_records = self.links(BODY_RECORDS, tagged=True) + self.links(BODY_RECORDS)
        without = self.links({})

        self.assertEqual(sorted(x.ident for x in with_records), sorted(x.ident for x in without))

    def test_line_numbers_count_markdown_lines(self) -> None:
        tagged = self.links(BODY_RECORDS, tagged=True)
        lines = BODY.splitlines()

        self.assertIn("[가]", lines[tagged[0].line - 1])
        self.assertIn("[나]", lines[tagged[1].line - 1])

    def test_offset_between_paragraphs_takes_the_preceding_one(self) -> None:
        text = "---\ntitle: t\n---\n\n첫째.\n\n\n\n둘째.\n"
        gap = text.index("첫째.") + len("첫째.") + 2

        self.assertEqual(dc.paragraph_context(text, gap, 0), "첫째.")

    def test_digest_follows_records_but_not_parked_ones(self) -> None:
        with (
            patch.object(dc, "ROOT", self.root),
            patch.object(dc, "by_permalink", return_value=SimpleNamespace(path=self.path)),
            patch.object(dc, "RECORDS", dict(BODY_RECORDS)),
        ):
            texts = {self.path: BODY}
            parked = {self.links(BODY_RECORDS, tagged=True)[0].ident}
            before = (dc.unit_digest([self.path], texts),
                      dc.unit_digest([self.path], texts, parked))
            dc.RECORDS["aaaaa"] = R("weak", True)
            after = (dc.unit_digest([self.path], texts),
                     dc.unit_digest([self.path], texts, parked))

        self.assertNotEqual(before[0], after[0])
        self.assertEqual(before[1], after[1])


class VerifierRoutingTest(unittest.TestCase):
    def test_each_model_is_checked_by_a_different_one(self) -> None:
        self.assertEqual(dc.verifier_chain("Codex"), ("Claude Opus",))
        self.assertEqual(dc.verifier_chain("Claude Opus"), ("Codex",))

    def test_antigravity_and_unrecorded_deciders_use_the_review_order(self) -> None:
        self.assertEqual(dc.verifier_chain("Antigravity"), ("Claude Opus", "Codex"))
        self.assertEqual(dc.verifier_chain(None), ("Claude Opus", "Codex"))

    def test_links_are_grouped_by_the_chain_that_owes_them_a_check(self) -> None:
        a = dc.Link("a", Path("x"), 0, 0, "", "", "", None, None)
        b = dc.Link("b", Path("x"), 0, 0, "", "", "", None, None)
        c = dc.Link("c", Path("x"), 0, 0, "", "", "", None, None)
        groups = dc.verify_groups([a, b, c], {"a": "Codex", "b": "Claude Opus"})

        self.assertEqual(groups[("Claude Opus",)], [a])
        self.assertEqual(groups[("Codex",)], [b])
        self.assertEqual(groups[("Claude Opus", "Codex")], [c])


TAGGED_BODY = (
    "---\ntitle: t\n---\n\n"
    "첫 문단.\n\n"
    "본문에서 [가](/ko/math/a){: data-lid=\"aaaaa\" } 를 쓰고\n"
    "[나](/ko/math/b){: data-lid=\"bbbbb\" } 도 쓴다.\n"
)


class VerificationPassTest(unittest.TestCase):
    """The second opinion either confirms the record or marks it requires-review."""

    def setUp(self) -> None:
        self.tmp = tempfile.TemporaryDirectory()
        self.addCleanup(self.tmp.cleanup)
        self.root = Path(self.tmp.name)
        self.path = self.root / "_posts/Math/Test/ko/draft.md"
        self.path.parent.mkdir(parents=True)
        self.path.write_text(TAGGED_BODY, encoding="utf-8")
        self.ledger_path = self.root / "_data" / "link_relations.yml"
        self.ledger_path.parent.mkdir(parents=True)
        self.records = {"aaaaa": R("required"), "bbbbb": R("weak")}
        self.state_path = self.root / "state.json"
        self.holds_path = self.root / "holds.json"
        self.post = SimpleNamespace(lang="ko", published=True, path=self.path)
        with patch.object(dc, "ROOT", self.root):
            self.key = dc.unit_key([self.path])
            self.idents = [x.ident for x in self.tagged()]

    def tagged(self) -> list:
        with (
            patch.object(dc, "ROOT", self.root),
            patch.object(dc, "by_permalink", return_value=self.post),
        ):
            return dc.extract_links(self.path, self.path.read_text(encoding="utf-8"),
                                    tagged=True, records=self.records)

    def digest(self) -> str:
        with (
            patch.object(dc, "ROOT", self.root),
            patch.object(dc, "by_permalink", return_value=self.post),
            patch.object(dc, "RECORDS", self.records),
        ):
            return dc.unit_digest([self.path], {self.path: self.path.read_text(encoding="utf-8")})

    def write_state(self, entry: dict) -> None:
        self.state_path.write_text(
            json.dumps({"units": {self.key: entry}}), encoding="utf-8")

    def tick(self, verdicts: dict[str, str], also: tuple = ()):
        def answer(items, *, mode):
            return {"items": [{"id": item["id"], "relation": verdicts[item["id"]],
                               "reason": "test"} for item in items]}

        patches = [
            patch.object(dc, "ROOT", self.root),
            patch.object(dc, "RECORDS", self.records),
            patch.object(dc.ledger, "PATH", self.ledger_path),
            patch.object(dc, "STATE_DIR", self.root),
            patch.object(dc, "STATE_PATH", self.state_path),
            patch.object(dc, "STATE_LOCK_PATH", self.root / "state.lock"),
            patch.object(dc, "HOLDS_PATH", self.holds_path),
            patch.object(dc, "HOLDS_LOCK_PATH", self.root / "holds.lock"),
            patch.object(dc, "COMPLETE_PATH", self.root / "complete.json"),
            patch.object(dc, "_POSTS", [self.post]),
            patch.object(dc, "mint_lids"),  # 식별자 발급은 전용 테스트에서 본다
            patch.object(dc, "by_permalink", return_value=self.post),
            patch.object(dc, "en_counterpart", return_value=None),
            patch.object(dc, "dirty_paths", return_value=[]),
            patch.object(dc, "commit_outputs", return_value=True),
            patch.object(dc, "provider_available", return_value=True),
        ]
        named = {
            "opus": patch.object(dc, "call_opus", side_effect=answer),
            "codex": patch.object(dc, "call_codex", side_effect=answer),
            "agy": patch.object(dc, "call_antigravity", side_effect=answer),
            "notify": patch.object(dc, "notify"),
        }
        with ExitStack() as stack:
            for item in patches:
                stack.enter_context(item)
            mocks = {name: stack.enter_context(item) for name, item in named.items()}
            # `also` goes in last so a test can narrow something the base set opened.
            for item in also:
                stack.enter_context(item)
            rc = dc.process_once()
        return SimpleNamespace(rc=rc, **mocks)

    def entry(self) -> dict:
        return json.loads(self.state_path.read_text(encoding="utf-8"))["units"][self.key]

    def holds(self) -> dict:
        return json.loads(self.holds_path.read_text(encoding="utf-8"))

    def saved(self) -> dict:
        return dc.ledger.load(self.ledger_path)

    def test_agreement_stamps_the_links_and_closes_the_unit(self) -> None:
        self.write_state({"status": "done", "hash": self.digest(),
                          "decided_by": {self.idents[0]: "Codex",
                                         self.idents[1]: "Claude Opus"}})
        run = self.tick({self.idents[0]: "required", self.idents[1]: "weak"})

        self.assertEqual(self.saved(), {"aaaaa": R("required", True), "bbbbb": R("weak", True)})
        self.assertEqual(self.path.read_text(encoding="utf-8"), TAGGED_BODY)
        self.assertEqual(self.entry()["verify"], "agreed")
        self.assertEqual(self.entry()["verified_hash"], self.digest())
        self.assertFalse(self.holds_path.exists())
        run.notify.assert_not_called()

    def test_each_link_goes_to_the_model_that_did_not_decide_it(self) -> None:
        self.write_state({"status": "done", "hash": self.digest(),
                          "decided_by": {self.idents[0]: "Codex",
                                         self.idents[1]: "Claude Opus"}})
        run = self.tick({self.idents[0]: "required", self.idents[1]: "weak"})

        run.agy.assert_not_called()
        self.assertEqual([item["id"] for item in run.opus.call_args[0][0]], [self.idents[0]])
        self.assertEqual([item["id"] for item in run.codex.call_args[0][0]], [self.idents[1]])

    def test_disagreement_marks_the_link_holds_it_and_notifies(self) -> None:
        self.write_state({"status": "done", "hash": self.digest(),
                          "decided_by": {self.idents[0]: "Codex",
                                         self.idents[1]: "Claude Opus"}})
        run = self.tick({self.idents[0]: "weak", self.idents[1]: "weak"})

        self.assertEqual(self.saved(), {"aaaaa": R(dc.REVIEW_RELATION),
                                        "bbbbb": R("weak", True)})
        held = self.holds()["held"][self.idents[0]]
        self.assertEqual(held["old"], "required")
        self.assertEqual(held["new"], "weak")
        self.assertEqual(held["lid"], "aaaaa")
        self.assertEqual(held["path"], "_posts/Math/Test/ko/draft.md")
        self.assertEqual(TAGGED_BODY.splitlines()[held["line"] - 1].count("[가]"), 1)
        run.notify.assert_called_once()
        self.assertEqual(self.entry()["verify"], "disputed")

    def test_ambiguous_is_held_the_same_way(self) -> None:
        self.write_state({"status": "done", "hash": self.digest(), "decided_by": {}})
        self.tick({self.idents[0]: "ambiguous", self.idents[1]: "weak"})

        self.assertEqual(self.holds()["held"][self.idents[0]]["new"], "ambiguous")
        self.assertNotIn(self.idents[1], self.holds()["held"])

    def test_a_held_link_is_invisible_to_both_stages(self) -> None:
        self.write_state({"status": "done", "hash": self.digest(), "decided_by": {}})
        self.tick({self.idents[0]: "weak", self.idents[1]: "weak"})
        run = self.tick({self.idents[0]: "weak", self.idents[1]: "weak"})

        self.assertEqual(run.opus.call_count, 0)
        self.assertEqual(run.agy.call_count, 0)
        self.assertEqual(len(self.holds()["held"]), 1)

    def test_a_marked_link_is_not_reclassified_without_its_hold(self) -> None:
        self.write_state({"status": "done", "hash": self.digest(), "decided_by": {}})
        self.tick({self.idents[0]: "weak", self.idents[1]: "weak"})
        self.holds_path.write_text(json.dumps({"held": {}, "settled": {}}), encoding="utf-8")

        run = self.tick({self.idents[0]: "weak", self.idents[1]: "weak"})

        self.assertEqual(run.agy.call_count, 0)
        self.assertEqual(self.saved()["aaaaa"], R(dc.REVIEW_RELATION))

    def test_settling_a_hold_does_not_reverify_the_remaining_links(self) -> None:
        self.write_state({"status": "done", "hash": self.digest(), "decided_by": {}})
        self.tick({self.idents[0]: "weak", self.idents[1]: "weak"})

        self.assertEqual(self.records["aaaaa"], R(dc.REVIEW_RELATION))
        self.records["aaaaa"] = R("weak", True)
        holds = self.holds()
        holds["settled"][self.idents[0]] = holds["held"].pop(self.idents[0])
        self.holds_path.write_text(json.dumps(holds), encoding="utf-8")

        run = self.tick({self.idents[0]: "weak", self.idents[1]: "weak"})

        self.assertEqual(run.opus.call_count, 0)
        self.assertEqual(run.codex.call_count, 0)
        self.assertEqual(run.agy.call_count, 0)

    def test_prose_edit_preserves_completed_link_reviews(self) -> None:
        self.write_state({"status": "done", "hash": self.digest(), "decided_by": {}})
        self.tick({self.idents[0]: "weak", self.idents[1]: "weak"})
        self.path.write_text(
            self.path.read_text(encoding="utf-8").replace("첫 문단.", "바뀐 첫 문단."),
            encoding="utf-8",
        )

        run = self.tick({self.idents[0]: "weak", self.idents[1]: "weak"})

        self.assertEqual(run.opus.call_count + run.codex.call_count, 0)

    def test_relation_edit_preserves_explicit_review_marker(self) -> None:
        self.write_state({"status": "done", "hash": self.digest(), "decided_by": {}})
        self.tick({self.idents[0]: "required", self.idents[1]: "weak"})
        self.records["bbbbb"] = R("required", True)

        run = self.tick({self.idents[0]: "required", self.idents[1]: "required"})

        self.assertEqual(run.opus.call_count + run.codex.call_count, 0)

    def test_a_closed_verifier_leaves_the_unit_for_a_later_tick(self) -> None:
        self.write_state({"status": "done", "hash": self.digest(),
                          "decided_by": {self.idents[0]: "Claude Opus",
                                         self.idents[1]: "Claude Opus"}})
        run = self.tick({self.idents[0]: "weak", self.idents[1]: "weak"},
                        also=(patch.object(dc, "provider_available",
                                           side_effect=lambda p: p != "Codex"),))

        self.assertFalse(self.ledger_path.exists())
        self.assertNotIn("verified_hash", self.entry())
        run.notify.assert_not_called()


LID_BODY = """---
title: t
---

본문에서 [가](#def1)를 쓰고 [나](#def2){: data-lid="xxxxx" }도 쓴다.
"""


class LidMintingTest(unittest.TestCase):
    """lid 없는 링크의 식별자 발급 — 원장이 그 링크의 판정을 담으려면 이게 먼저다."""

    def setUp(self) -> None:
        self.tmp = tempfile.TemporaryDirectory()
        self.addCleanup(self.tmp.cleanup)
        self.root = Path(self.tmp.name)
        self.ko = self.root / "_posts" / "Math" / "Cat" / "ko" / "2025-01-01-A.md"
        self.en = self.root / "_posts" / "Math" / "Cat" / "en" / "2026-01-01-A.md"
        for path in (self.ko, self.en):
            path.parent.mkdir(parents=True, exist_ok=True)
            path.write_text(LID_BODY, encoding="utf-8")
        self.ledger = self.root / "link-ids.txt"

    def mint(self, *, dirty: list[str] | None = None, also=()) -> None:
        patches = [
            patch.object(dc, "ROOT", self.root),
            patch.object(dc, "LID_LEDGER", self.ledger),
            patch.object(dc, "dirty_paths", return_value=dirty or []),
            patch.object(dc, "hard_lint", return_value=set()),
            patch.object(dc, "is_local_only_untracked_unit", return_value=False),
            patch.object(dc, "commit_outputs", return_value=True),
        ]
        with ExitStack() as stack:
            for item in patches:
                stack.enter_context(item)
            for item in also:
                stack.enter_context(item)
            dc.mint_lids(commit=True)

    def lids(self, path: Path) -> list[str]:
        return dc.LID_RE.findall(path.read_text(encoding="utf-8"))

    def test_links_without_an_identifier_get_one_and_the_ledger_records_it(self) -> None:
        self.mint()
        ko, en = self.lids(self.ko), self.lids(self.en)
        self.assertEqual(ko[1], "xxxxx")
        self.assertEqual(len(set(ko + en)), 3)
        self.assertEqual(sorted(self.ledger.read_text(encoding="utf-8").split()),
                         sorted({ko[0], en[0]}))

    def test_existing_identifiers_are_never_reissued(self) -> None:
        self.mint()
        before = self.ko.read_text(encoding="utf-8")
        self.mint()
        self.assertEqual(self.ko.read_text(encoding="utf-8"), before)

    def test_a_value_already_in_use_is_drawn_again(self) -> None:
        self.ledger.write_text("aaaaa\n", encoding="utf-8")
        draws = iter("aaaaa" + "bbbbb" + "ccccc")
        with patch.object(dc.secrets, "choice", side_effect=lambda _seq: next(draws)):
            self.mint()
        self.assertEqual(sorted(self.lids(self.ko)[:1] + self.lids(self.en)[:1]),
                         ["bbbbb", "ccccc"])

    def test_a_post_with_uncommitted_edits_waits(self) -> None:
        self.mint(dirty=["_posts/Math/Cat/ko/2025-01-01-A.md",
                         "_posts/Math/Cat/en/2026-01-01-A.md"])
        self.assertEqual(self.lids(self.ko), ["xxxxx"])
        self.assertFalse(self.ledger.exists())


class LedgerFileTest(unittest.TestCase):
    """_data/link_relations.yml 의 직렬화."""

    def test_round_trip_is_stable_and_keys_stay_strings(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            path = Path(tmp) / "link_relations.yml"
            records = {"01234": R("required", True), "false": R("weak"),
                       "zz9zz": R(dc.REVIEW_RELATION)}
            dc.ledger.save(records, path)
            text = path.read_text(encoding="utf-8")

            self.assertEqual(dc.ledger.load(path), records)
            dc.ledger.save(dc.ledger.load(path), path)
            self.assertEqual(path.read_text(encoding="utf-8"), text)
            self.assertIn('"01234": {relation: required, reviewed: true}', text)
            self.assertIn('"false": {relation: weak}', text)

    def test_a_bad_relation_is_rejected(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            path = Path(tmp) / "link_relations.yml"
            path.write_text('"aaaaa": {relation: sideways}\n', encoding="utf-8")
            with self.assertRaises(ValueError):
                dc.ledger.load(path)

    def test_lock_is_exclusive(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            with patch.object(dc.ledger, "LOCK_PATH", Path(tmp) / "lock"):
                first = dc.ledger.try_lock()
                self.assertIsNotNone(first)
                self.assertIsNone(dc.ledger.try_lock())
                first.release()
                again = dc.ledger.try_lock()
                self.assertIsNotNone(again)
                again.release()


if __name__ == "__main__":
    unittest.main()
