#!/usr/bin/env python3
"""Tests for linkdep_core: link extraction and excerpts, the quota gate, lid minting,
and the ledger file format."""
from __future__ import annotations

import importlib.util
import json
import sys
import tempfile
import time
import unittest
from contextlib import ExitStack
from datetime import datetime, timedelta, timezone
from pathlib import Path
from types import SimpleNamespace
from unittest.mock import patch


MODULE_PATH = Path(__file__).with_name("linkdep_core.py")
SPEC = importlib.util.spec_from_file_location("linkdep_core_under_test", MODULE_PATH)
assert SPEC and SPEC.loader
core = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = core
SPEC.loader.exec_module(core)

R = core.ledger.Record


class PostScopeTest(unittest.TestCase):
    def test_math_posts_only(self) -> None:
        self.assertTrue(core._POSTS)
        self.assertTrue(all(post.path.is_relative_to(core.MATH_POST_ROOT) for post in core._POSTS))


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
            with patch.object(core, "QUOTA_STATE_DIR", root):
                self.assertFalse(core.provider_available("Claude Opus"))

    def test_codex_pool_stays_open_when_one_account_is_available(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            self.write_state(root, "codex1", self.quota_state(utilization=0.80))
            self.write_state(root, "codex2", self.quota_state(utilization=0.20))
            with patch.object(core, "QUOTA_STATE_DIR", root):
                self.assertTrue(core.provider_available("Codex"))

    def test_unknown_codex_member_is_fail_open(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            self.write_state(root, "codex1", self.quota_state(utilization=0.80))
            with patch.object(core, "QUOTA_STATE_DIR", root):
                self.assertTrue(core.provider_available("Codex"))

    def weekly_state(self, *, weekly: float, hours_left: float, five: float = 0.1) -> dict:
        reset = datetime.now(timezone.utc) + timedelta(hours=hours_left)
        state = self.quota_state(utilization=five)
        state["weekly"] = {"utilization": weekly, "resetTime": reset.isoformat()}
        return state

    def test_weekly_limit_holds_until_the_final_stretch(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            with patch.object(core, "QUOTA_STATE_DIR", root):
                self.write_state(root, "antigravity", self.weekly_state(weekly=0.95, hours_left=30))
                self.assertFalse(core.provider_available("Antigravity"))
                self.write_state(root, "antigravity", self.weekly_state(weekly=0.95, hours_left=20))
                self.assertTrue(core.provider_available("Antigravity"))

    def test_final_stretch_keeps_the_5h_limit(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            self.write_state(root, "antigravity",
                             self.weekly_state(weekly=0.95, hours_left=20, five=0.75))
            with patch.object(core, "QUOTA_STATE_DIR", root):
                self.assertFalse(core.provider_available("Antigravity"))


class LocalOnlyPolicyTest(unittest.TestCase):
    def test_untracked_gromov_witten_unit_is_local_only(self) -> None:
        path = core.LOCAL_ONLY_POST_ROOTS[0] / "ko" / "draft.md"
        result = SimpleNamespace(returncode=0, stdout="", stderr="")
        with patch.object(core.subprocess, "run", return_value=result) as run:
            self.assertTrue(core.is_local_only_untracked_unit([path]))
        self.assertIn("ls-files", run.call_args.args[0])

    def test_tracked_gromov_witten_post_still_uses_commit_path(self) -> None:
        path = core.LOCAL_ONLY_POST_ROOTS[0] / "ko" / "published.md"
        rel = str(path.relative_to(core.ROOT))
        result = SimpleNamespace(returncode=0, stdout=rel + "\0", stderr="")
        with patch.object(core.subprocess, "run", return_value=result):
            self.assertFalse(core.is_local_only_untracked_unit([path]))

    def test_other_untracked_paths_do_not_gain_local_only_exception(self) -> None:
        path = core.ROOT / "_posts" / "Math" / "Topology" / "ko" / "draft.md"
        with patch.object(core.subprocess, "run") as run:
            self.assertFalse(core.is_local_only_untracked_unit([path]))
        run.assert_not_called()


BODY = (
    "---\ntitle: t\n---\n\n"
    "첫 문단.\n\n"
    "본문에서 [가](/ko/math/a){: data-lid=\"aaaaa\" } 를 쓰고\n"
    "[나](/ko/math/b){: .x data-lid=\"bbbbb\" } 도 쓰고 [다](/ko/math/c){: data-lid=\"ccccc\" } 는 아직이다.\n"
)


class ExtractLinksTest(unittest.TestCase):
    """Internal links in source order, each with the lid of its IAL."""

    def setUp(self) -> None:
        self.tmp = tempfile.TemporaryDirectory()
        self.root = Path(self.tmp.name)
        self.path = self.root / "_posts/Math/Test/ko/draft.md"
        self.path.parent.mkdir(parents=True)
        self.path.write_text(BODY, encoding="utf-8")
        self.addCleanup(self.tmp.cleanup)

    def links(self, path: Path | None = None, text: str = BODY) -> list:
        post = SimpleNamespace(lang="ko", published=True, path=self.path)
        with (
            patch.object(core, "ROOT", self.root),
            patch.object(core, "by_permalink", return_value=post),
        ):
            return core.extract_links(path or self.path, text)

    def test_every_internal_link_comes_back_with_its_lid(self) -> None:
        found = self.links()

        self.assertEqual([x.target for x in found], ["/ko/math/a", "/ko/math/b", "/ko/math/c"])
        self.assertEqual([x.lid for x in found], ["aaaaa", "bbbbb", "ccccc"])

    def test_a_link_without_an_ial_has_no_lid(self) -> None:
        found = self.links(text="---\ntitle: t\n---\n\n[가](/ko/math/a) 와 [나](#def2){: .x }.\n")

        self.assertEqual([x.lid for x in found], [None, None])

    def test_line_numbers_count_markdown_lines(self) -> None:
        found = self.links()
        lines = BODY.splitlines()

        self.assertIn("[가]", lines[found[0].line - 1])
        self.assertIn("[나]", lines[found[1].line - 1])

    def test_an_en_link_sharing_a_ko_lid_is_left_to_the_ko_link(self) -> None:
        en_path = self.root / "_posts/Math/Test/en/draft.md"
        with (
            patch.object(core, "ROOT", self.root),
            patch.object(core, "by_permalink", return_value=SimpleNamespace(path=self.path)),
        ):
            ko_all = core.ko_lids([self.path, en_path], {self.path: BODY, en_path: BODY})
        en = self.links(en_path)

        self.assertEqual(ko_all, {"aaaaa", "bbbbb", "ccccc"})
        self.assertTrue(all(core.awaits_ko(x, ko_all) for x in en))
        self.assertFalse(any(core.awaits_ko(x, ko_all) for x in self.links()))
        self.assertFalse(core.awaits_ko(en[0], ko_all - {"aaaaa"}))

    def test_offset_between_paragraphs_takes_the_preceding_one(self) -> None:
        text = "---\ntitle: t\n---\n\n첫째.\n\n\n\n둘째.\n"
        gap = text.index("첫째.") + len("첫째.") + 2

        self.assertEqual(core.paragraph_context(text, gap, 0), "첫째.")

    def test_link_in_footnote_gets_the_passage_it_annotates(self) -> None:
        text = ("---\ntitle: t\n---\n\n이 \"집합\"을 생각한다.[^1]\n\n무관한 문단.\n\n"
                "다른 문단.\n\n다른 문단 둘.\n\n"
                "[^1]: 집합이 아니다. ([예시 4](/ko/x#ex4))\n[^2]: 다른 각주.\n")
        src = core.source_context(text, text.index("[예시 4]"), 0)

        self.assertIn("[^1]: 집합이 아니다.", src)
        self.assertIn("이 \"집합\"을 생각한다.[^1]", src)

    def test_body_paragraph_gets_its_footnote_text(self) -> None:
        text = ("---\ntitle: t\n---\n\n[정리 3](/ko/x#thm3)으로부터 얻는다.[^a]\n\n"
                "다른 문단.\n\n다른 문단 둘.\n\n"
                "[^a]: 여기서 compactness 가정을 쓴다.\n    이어지는 줄.\n\n끝 문단.\n")
        src = core.source_context(text, text.index("[정리 3]"), 0)

        self.assertIn("[^a]: 여기서 compactness 가정을 쓴다.\n    이어지는 줄.", src)
        self.assertNotIn("끝 문단.", src)


LID_BODY = """---
title: t
---

본문에서 [가](#def1)를 쓰고 [나](#def2){: data-lid="xxxxx" }도 쓴다.
"""


KO_REL = "_posts/Math/Cat/ko/2025-01-01-A.md"
EN_REL = "_posts/Math/Cat/en/2026-01-01-A.md"


class LidFixture(unittest.TestCase):
    """KO/EN 한 쌍을 임시 루트에 두고 mint_lids 를 돌리는 바탕."""

    def setUp(self) -> None:
        self.tmp = tempfile.TemporaryDirectory()
        self.addCleanup(self.tmp.cleanup)
        self.root = Path(self.tmp.name)
        self.ko = self.root / KO_REL
        self.en = self.root / EN_REL
        self.write(LID_BODY, LID_BODY)
        self.ledger = self.root / "link-ids.txt"
        self.pairing = self.root / "pairing.json"

    def write(self, ko: str | None, en: str) -> None:
        for path, body in ((self.ko, ko), (self.en, en)):
            path.parent.mkdir(parents=True, exist_ok=True)
            if body is None:
                path.unlink(missing_ok=True)
            else:
                path.write_text(body, encoding="utf-8")

    def mint(self, *, dirty: list[str] | None = None, also=()) -> bool:
        dirty = dirty or []
        patches = [
            patch.object(core, "ROOT", self.root),
            patch.object(core, "LID_LEDGER", self.ledger),
            patch.object(core, "PAIRING_STATE_PATH", self.pairing),
            patch.object(core, "dirty_paths",
                         side_effect=lambda rels, _root: [r for r in rels if r in dirty]),
            patch.object(core, "hard_lint", return_value=set()),
            patch.object(core, "is_local_only_untracked_unit", return_value=False),
            patch.object(core, "commit_outputs", return_value=True),
        ]
        with ExitStack() as stack:
            for item in patches:
                stack.enter_context(item)
            for item in also:
                stack.enter_context(item)
            return core.mint_lids(commit=True)

    def lids(self, path: Path) -> list[str]:
        return core.LID_RE.findall(path.read_text(encoding="utf-8"))

    def minted(self) -> list[str]:
        if not self.ledger.exists():
            return []
        return sorted(self.ledger.read_text(encoding="utf-8").split())


class LidMintingTest(LidFixture):
    """lid 없는 링크의 식별자 발급 — 원장이 그 링크의 판정을 담으려면 이게 먼저다."""

    def test_ko_links_get_identifiers_and_their_en_translations_inherit_them(self) -> None:
        self.assertFalse(self.mint())
        ko, en = self.lids(self.ko), self.lids(self.en)
        self.assertEqual(ko[1], "xxxxx")
        self.assertEqual(en, ko)
        self.assertEqual(self.minted(), [ko[0]])

    def test_existing_identifiers_are_never_reissued(self) -> None:
        self.mint()
        before = self.ko.read_text(encoding="utf-8"), self.en.read_text(encoding="utf-8")
        self.mint()
        self.assertEqual((self.ko.read_text(encoding="utf-8"),
                          self.en.read_text(encoding="utf-8")), before)

    def test_a_value_already_in_use_is_drawn_again(self) -> None:
        self.ledger.write_text("aaaaa\n", encoding="utf-8")
        draws = iter("aaaaa" + "bbbbb")
        with patch.object(core.secrets, "choice", side_effect=lambda _seq: next(draws)):
            self.mint()
        self.assertEqual(self.lids(self.ko)[0], "bbbbb")
        self.assertEqual(self.lids(self.en)[0], "bbbbb")

    def test_a_post_with_uncommitted_edits_waits(self) -> None:
        self.mint(dirty=[KO_REL, EN_REL])
        self.assertEqual(self.lids(self.ko), ["xxxxx"])
        self.assertFalse(self.ledger.exists())

    def test_en_waits_while_its_ko_twin_still_lacks_an_identifier(self) -> None:
        # KO 가 이번에 발급을 못 받으면 EN 은 후보를 볼 수 없다. 그때 새 값을 주면
        # 같은 출현이 KO 와 갈린다.
        self.mint(dirty=[KO_REL])
        self.assertEqual(self.lids(self.ko), ["xxxxx"])
        self.assertEqual(self.lids(self.en), ["xxxxx"])

    def test_an_en_link_with_no_ko_occurrence_gets_its_own(self) -> None:
        self.write(LID_BODY, LID_BODY.replace("도 쓴다.", "도 쓰고 [다](#def3)도 쓴다."))
        self.mint()
        ko, en = self.lids(self.ko), self.lids(self.en)
        self.assertEqual(en[:2], ko)
        self.assertNotIn(en[2], ko)
        self.assertEqual(self.minted(), sorted([ko[0], en[2]]))

    def test_an_en_post_without_a_ko_twin_mints_its_own(self) -> None:
        self.write(None, LID_BODY)
        self.mint()
        self.assertEqual(self.lids(self.en)[1], "xxxxx")
        self.assertEqual(self.minted(), [self.lids(self.en)[0]])


KO_TWICE = """---
title: t
---

[가](#def1){: data-lid="aaaa1" }는 A이고 [가](#def1){: data-lid="aaaa2" }는 B이다.
"""

EN_TWICE = """---
title: t
---

B is [ga](#def1) and A is [ga](#def1).
"""


class LidPairingTest(LidFixture):
    """같은 대상이 여러 번 나와 순서로만 갈리는 EN 링크 — 모델이 문장을 읽고 짝을 정한다."""

    def setUp(self) -> None:
        super().setUp()
        self.write(KO_TWICE, EN_TWICE)

    def ask(self, answer=None, *, error=None, open_quota=True):
        model = patch.object(core, "ask_antigravity", return_value=answer,
                             side_effect=error)
        notify = patch.object(core, "notify")
        extra = (patch.object(core, "provider_available", return_value=open_quota),
                 patch.object(core, "acquire_provider_slot"))
        with model as m, notify as n:
            called = self.mint(also=extra)
        return SimpleNamespace(called=called, model=m, notify=n)

    def state(self) -> dict:
        return json.loads(self.pairing.read_text(encoding="utf-8")).get(EN_REL, {})

    def test_the_model_decides_occurrences_split_only_by_order(self) -> None:
        run = self.ask({"assignments": [{"en": "e1", "lid": "aaaa2"},
                                        {"en": "[e2]", "lid": "aaaa1"}]})
        self.assertTrue(run.called)
        prompt = run.model.call_args.args[0]
        self.assertIn("⟦e1⟧[ga](#def1)", prompt)
        self.assertIn('⟦aaaa2⟧[가](#def1){: data-lid="aaaa2" }', prompt)
        self.assertEqual(self.lids(self.en), ["aaaa2", "aaaa1"])
        self.assertFalse(self.ledger.exists())
        self.assertEqual(self.state(), {})

    def test_only_an_unmatched_verdict_mints_and_undecided_waits(self) -> None:
        run = self.ask({"unmatched": [{"en": "e1", "why": "번역이 덧붙임"}],
                        "undecided": [{"en": "e2", "why": "모름"}]})
        en = self.lids(self.en)
        self.assertEqual(len(en), 1)
        self.assertNotIn(en[0], {"aaaa1", "aaaa2"})
        self.assertEqual(self.minted(), en)
        self.assertEqual(self.state()["attempts"], 1)
        run.notify.assert_not_called()

    def test_answers_breaking_the_rules_are_dropped(self) -> None:
        self.ask({"assignments": [{"en": "e1", "lid": "zzzzz"},
                                  {"en": "e2", "lid": "aaaa1"},
                                  {"en": "e9", "lid": "aaaa2"}]})
        self.assertEqual(self.en.read_text(encoding="utf-8").count("data-lid"), 1)
        self.assertIn('[ga](#def1){: data-lid="aaaa1" }.', self.en.read_text(encoding="utf-8"))
        # 남은 링크는 후보도 하나뿐이라 다음 발급에서 모델 없이 풀린다
        run = self.ask({"assignments": []})
        run.model.assert_not_called()
        self.assertEqual(self.lids(self.en), ["aaaa2", "aaaa1"])

    def test_a_failed_call_or_closed_quota_writes_nothing(self) -> None:
        run = self.ask(error=RuntimeError("boom"))
        self.assertTrue(run.called)
        self.assertEqual(self.lids(self.en), [])
        self.assertEqual(self.state()["attempts"], 1)
        run = self.ask({"assignments": []}, open_quota=False)
        self.assertFalse(run.called)
        run.model.assert_not_called()

    def test_repeated_failure_notifies_once_and_rests_a_day(self) -> None:
        for _ in range(core.PAIRING_MAX_ATTEMPTS):
            run = self.ask(error=RuntimeError("boom"))
        run.notify.assert_called_once()
        self.assertGreater(self.state()["retry_after"], time.time())
        run = self.ask(error=RuntimeError("boom"))
        self.assertFalse(run.called)
        run.model.assert_not_called()


class LedgerFileTest(unittest.TestCase):
    """_data/link_relations.yml 의 직렬화."""

    def test_round_trip_is_stable_and_keys_stay_strings(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            path = Path(tmp) / "link_relations.yml"
            records = {"01234": R("required", True), "false": R("weak", True),
                       "zz9zz": R("forward")}
            text = core.ledger.dump(records)
            path.write_text(text, encoding="utf-8")

            self.assertEqual(core.ledger.load(path), records)
            self.assertEqual(core.ledger.dump(core.ledger.load(path)), text)
            self.assertIn('"01234": {relation: required, reviewed: true}', text)
            self.assertIn('"zz9zz": {relation: forward}', text)

    def test_a_bad_relation_is_rejected(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            path = Path(tmp) / "link_relations.yml"
            for value in ("sideways", "requires-review"):
                path.write_text(f'"aaaaa": {{relation: {value}}}\n', encoding="utf-8")
                with self.assertRaises(ValueError):
                    core.ledger.load(path)


if __name__ == "__main__":
    unittest.main()
