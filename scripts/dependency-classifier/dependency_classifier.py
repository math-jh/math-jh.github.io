#!/usr/bin/env python3
"""Classify internal Markdown links as required, weak, or forward.

One cron tick handles one logical KO/EN article pair.  A link's relation lives
in the ledger ``_data/link_relations.yml``, keyed by the ``data-lid`` in the link's
IAL.  An EN link carrying the lid of a KO link is that link's translation and
shares its record, so only KO links and EN links without a KO twin are judged.
Each judgment rewrites the ledger and commits it.

A unit passes through two stages, one per tick.

The **first pass** classifies links that carry no relation yet along the
Antigravity > Claude Opus > Codex chain.  Antigravity accepts only self-declared
HIGH decisions; MEDIUM decisions receive a wider-context review from the next
available provider in the Claude Opus > Codex chain.  A single ambiguous decision
blocks the whole pair so an article is not repeatedly rewritten.  A blocked pair
is retried a day later, and the round counter kept in the state file escalates
the evidence: round 1 reviews excerpts, rounds 2 and 3 hand the reviewer the
complete source and target articles.  After MAX_ROUNDS the unit is marked
exhausted and skipped until its files change, which resets the counter — so an
edit that adds a new link always reopens the unit.

The **verification pass** then re-judges the same links from scratch.  The
existing relation is stripped out of the prompt, so the verifier sees an
untagged link and cannot anchor on the earlier verdict.  The verifier is a
different model from the one that decided the link: Codex checks Claude Opus,
Claude Opus checks Codex, and a link decided by Antigravity (or by the pre-2026-09
backlog, whose decider was not recorded) goes down the existing Claude Opus >
Codex review chain.  A single-provider assignment has no fallback, so a unit
whose verifier is closed by the quota gate is left for a later tick instead of
waiting on a provider slot.

A record's ``reviewed: true`` is the durable completion marker.  Its presence
means the semantic relation has already been reviewed, by the verification pass
or by a human ruling.  It belongs to the lid, so it survives link renames, moves,
and proposition-number changes; removing it is the explicit way to request
another verification pass.

Disagreement is not resolved automatically.  When the verifier returns a
different relation, or ambiguous, the relation value is **replaced** with the
marker ``requires-review`` and the link is held in
``dependency-classifier-holds.json``.  Graph consumers accept only
required·weak·forward, so the marked link drops out of the graph as an untagged
one would.  Neither stage picks up a marked link, so nothing reclassifies it, and
the dashboard's link-audit panel lists it with its file and line for a human
ruling, which the dashboard writes back to the ledger as a reviewed record.
Every hold is announced through the notify shim as it is recorded.

A post carries only the identifier; the relation is in the ledger::

    [label](/ko/math/example){: data-lid="k7m2x" }
    "k7m2x": {relation: required, reviewed: true}

A tick holds the ledger lock from start to finish and skips when the lock is
taken, which is also how a dashboard ruling in progress defers the tick.

State and logs live outside the repository under ~/.local/state.
"""
from __future__ import annotations

import argparse
import fcntl
import hashlib
import json
import os
import re
import secrets
import subprocess
import sys
import tempfile
import time
from dataclasses import dataclass
from datetime import datetime
from pathlib import Path
from typing import Callable, Iterable

ROOT = Path(__file__).resolve().parents[2]
MATH_POST_ROOT = ROOT / "_posts" / "Math"
sys.path.insert(0, str(ROOT / "scripts" / "postnav"))
sys.path.insert(0, str(ROOT / ".agents" / "hooks"))
sys.path.insert(0, str(ROOT / "scripts" / "lib"))
LOCAL_ONLY_POST_ROOTS = (ROOT / "_posts" / "Math" / "Gromov_Witten_Theory",)

from common import by_permalink, en_counterpart, find_box, iter_posts, parse_labels, protected_spans  # noqa: E402
import md_lint  # noqa: E402
from blog_file_lock import FileLockSet, try_acquire_file_locks  # noqa: E402
import link_relations as ledger  # noqa: E402
from cron_commit import commit_outputs, dirty_paths  # noqa: E402

STATE_DIR = Path.home() / ".local" / "state"
STATE_PATH = STATE_DIR / "dependency-classifier.json"
HOLDS_PATH = STATE_DIR / "dependency-classifier-holds.json"
HOLDS_LOCK_PATH = Path("/tmp/dependency-classifier-holds.lock")
COMPLETE_PATH = STATE_DIR / "dependency-classifier.complete"
STATE_LOCK_PATH = Path("/tmp/dependency-classifier-state.lock")
LEGACY_LOCK_PATH = Path("/tmp/dependency-classifier.lock")

QUOTA_STATE_DIR = Path(os.environ.get(
    "DEPENDENCY_QUOTA_STATE_DIR", str(Path.home() / "Projects" / "hud-display" / "state")))
QUOTA_MAX_STALE_SEC = int(os.environ.get("DEPENDENCY_QUOTA_MAX_STALE_SEC", str(45 * 60)))
QUOTA_LIMIT_5H = float(os.environ.get("DEPENDENCY_QUOTA_LIMIT_5H", "0.70"))
QUOTA_LIMIT_WEEKLY = float(os.environ.get("DEPENDENCY_QUOTA_LIMIT_WEEKLY", "0.90"))
# Codex passed 8/8 simultaneous probes on 2026-09-10; six leaves room for IDE use.
# Claude was already quota-closed at one probe, so its former four-worker cap stays.
PROVIDER_SLOT_COUNTS = {"Antigravity": 4, "Claude Opus": 4, "Codex": 6}
PROVIDER_SLOT_PATHS = {
    name: tuple(Path(
        f"/tmp/dependency-classifier-{name.lower().replace(' ', '-')}-slot-{i}.lock"
    ) for i in range(count))
    for name, count in PROVIDER_SLOT_COUNTS.items()
}

AGY_BIN = os.environ.get("DEPENDENCY_AGY_BIN", str(Path.home() / ".gemini/bin/agy"))
AGY_MODEL = os.environ.get("DEPENDENCY_AGY_MODEL", "gemini-3.8-flash-high")
CLAUDE_BIN = os.environ.get("DEPENDENCY_CLAUDE_BIN", str(Path.home() / ".local/bin/claude"))
CLAUDE_MODEL = os.environ.get("DEPENDENCY_CLAUDE_MODEL", "opus")
CODEX_BIN = os.environ.get(
    "DEPENDENCY_CODEX_BIN", str(Path.home() / ".npm-global/bin/codex-multi-auth-codex"))
# sol is the model ~/.codex/config.toml calls the strongest of the Codex line.
CODEX_MODEL_OVERRIDE = os.environ.get("DEPENDENCY_CODEX_MODEL")
CODEX_EFFORT_OVERRIDE = os.environ.get("DEPENDENCY_CODEX_EFFORT")
CODEX_FIRST_MODEL = os.environ.get(
    "DEPENDENCY_CODEX_FIRST_MODEL", CODEX_MODEL_OVERRIDE or "gpt-5.6-sol")
CODEX_FIRST_EFFORT = os.environ.get(
    "DEPENDENCY_CODEX_FIRST_EFFORT", CODEX_EFFORT_OVERRIDE or "medium")
CODEX_REVIEW_MODEL = os.environ.get(
    "DEPENDENCY_CODEX_REVIEW_MODEL", CODEX_MODEL_OVERRIDE or "gpt-5.6-sol")
CODEX_REVIEW_EFFORT = os.environ.get(
    "DEPENDENCY_CODEX_REVIEW_EFFORT", CODEX_EFFORT_OVERRIDE or "medium")
MODEL_TIMEOUT = int(os.environ.get("DEPENDENCY_MODEL_TIMEOUT", "900"))
BLOCK_SEC = 24 * 3600
CHUNK_SIZE = 10
# Review rounds from the second one on hand the reviewer the complete articles
# instead of excerpts: the recorded ambiguous reasons are almost always "the link
# does not appear in the given source excerpt".  Whole articles are large, so the
# full round sends fewer items per request.
MAX_ROUNDS = 3
FULL_CHUNK_SIZE = 4
FULL_SOURCE_CAP = 30000
FULL_TARGET_CAP = 30000
RELATIONS = set(ledger.RELATIONS)
# A link the verifier disagreed with waits for a human ruling.  The verdict of a
# single model is never enough to overwrite the other model's tag, so the tag is
# taken off and the link is parked here instead.
VERIFIER_CHAINS = {
    "Codex": ("Claude Opus",),
    "Claude Opus": ("Codex",),
    "Antigravity": ("Claude Opus", "Codex"),
}
DEFAULT_VERIFIER_CHAIN = VERIFIER_CHAINS["Antigravity"]
NOTIFY_BIN = os.environ.get(
    "DEPENDENCY_NOTIFY_BIN", str(Path.home() / ".local" / "bin" / "notify"))
# 알림을 누르면 바로 판정할 수 있는 자리로 보낸다.
DASHBOARD_URL = os.environ.get(
    "DEPENDENCY_DASHBOARD_URL", "https://preview.math-jh.com/dash/#audit")

IAL_RE = re.compile(r'^\{:\s*([^}]*)\}')
LID_RE = re.compile(r'\bdata-lid\s*=\s*["\']([^"\']*)["\']')
REVIEW_RELATION = ledger.REVIEW_RELATION

# The ledger as this tick reads and writes it.  main() loads it after taking the
# ledger lock; other importers (the dashboard) pass their own copy to
# extract_links.
RECORDS: dict[str, ledger.Record] = {}


@dataclass
class Link:
    ident: str
    source: Path
    start: int
    end: int
    markup: str
    label: str
    target: str
    ial_start: int | None
    ial_end: int | None
    line: int = 0
    lid: str | None = None
    relation: str | None = None
    reviewed: bool = False

    def where(self) -> str:
        """`path:line` as the editor and the dashboard count Markdown lines."""
        return f"{self.source.relative_to(ROOT)}:{self.line}"

    def brief(self) -> str:
        """One short line for a log or an alert.

        A label may run to hundreds of characters across several lines: the link
        regex reads an escaped `\\[` as an opening bracket and swallows the prose
        up to the next real link.  The tag still lands in the right place, so the
        blob is a display problem, not a placement one.
        """
        flat = " ".join(self.markup.split())
        return flat if len(flat) <= 90 else flat[:87] + "…"


def log(message: str) -> None:
    print(f"[{datetime.now():%Y-%m-%d %H:%M:%S}] {message}", flush=True)


def notify(subject: str, body: str, level: str = "active",
           url: str = DASHBOARD_URL) -> None:
    """Best-effort alert.  A failed notification must not fail the tick."""
    try:
        proc = subprocess.run(
            [NOTIFY_BIN, "-s", subject, "-b", body, "-g", "blog", "-l", level,
             *(("-u", url) if url else ())],
            check=False, timeout=20, capture_output=True, text=True,
        )
        if proc.returncode:
            log(f"notify rc={proc.returncode}: {proc.stderr.strip()[:300]!r}")
    except Exception as exc:  # noqa: BLE001
        log(f"notify skipped: {exc!r}")


def sha(text: str) -> str:
    return hashlib.sha256(text.encode("utf-8")).hexdigest()


def load_state() -> dict:
    try:
        value = json.loads(STATE_PATH.read_text(encoding="utf-8"))
        return value if isinstance(value, dict) else {}
    except (OSError, json.JSONDecodeError):
        return {}


def _save_state_unlocked(state: dict) -> None:
    STATE_DIR.mkdir(parents=True, exist_ok=True)
    fd, tmp_name = tempfile.mkstemp(prefix="dependency-classifier.", suffix=".tmp", dir=STATE_DIR)
    try:
        with os.fdopen(fd, "w", encoding="utf-8") as fh:
            fh.write(json.dumps(state, ensure_ascii=False, indent=2) + "\n")
        os.replace(tmp_name, STATE_PATH)
    finally:
        try:
            os.unlink(tmp_name)
        except FileNotFoundError:
            pass


def merge_unit_states(updates: dict[str, dict]) -> None:
    """Merge only this process's unit results under a short state-file lock."""
    if not updates:
        return
    lock_fh = open(STATE_LOCK_PATH, "w")
    try:
        fcntl.flock(lock_fh, fcntl.LOCK_EX)
        latest = load_state()
        latest.setdefault("units", {}).update(updates)
        _save_state_unlocked(latest)
    finally:
        lock_fh.close()


def load_holds() -> dict:
    """Links parked for a human ruling, plus the ones already ruled on.

    ``held`` is what the dashboard's link-audit panel lists; the first pass skips
    those idents so nothing reclassifies a link the user has yet to decide.
    ``settled`` is the user's own verdict: the verifier leaves those links alone,
    so a hand-written tag cannot be disputed back into the queue.
    """
    try:
        value = json.loads(HOLDS_PATH.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError):
        value = {}
    if not isinstance(value, dict):
        value = {}
    for section in ("held", "settled"):
        if not isinstance(value.get(section), dict):
            value[section] = {}
    return value


def merge_holds(new_holds: dict[str, dict]) -> None:
    if not new_holds:
        return
    lock_fh = open(HOLDS_LOCK_PATH, "w")
    try:
        fcntl.flock(lock_fh, fcntl.LOCK_EX)
        holds = load_holds()
        holds["held"].update(new_holds)
        STATE_DIR.mkdir(parents=True, exist_ok=True)
        fd, tmp_name = tempfile.mkstemp(
            prefix="dependency-classifier-holds.", suffix=".tmp", dir=STATE_DIR)
        try:
            with os.fdopen(fd, "w", encoding="utf-8") as fh:
                fh.write(json.dumps(holds, ensure_ascii=False, indent=2) + "\n")
            os.replace(tmp_name, HOLDS_PATH)
        finally:
            try:
                os.unlink(tmp_name)
            except FileNotFoundError:
                pass
    finally:
        lock_fh.close()


def parked_idents() -> set[str]:
    holds = load_holds()
    return set(holds["held"]) | set(holds["settled"])


def legacy_classifier_running() -> bool:
    """Avoid overlapping the pre-file-lock process during live deployment."""
    lock_fh = open(LEGACY_LOCK_PATH, "w")
    try:
        try:
            fcntl.flock(lock_fh, fcntl.LOCK_EX | fcntl.LOCK_NB)
            return False
        except OSError:
            return True
    finally:
        lock_fh.close()


def acquire_provider_slot(provider: str):
    """Wait for a measured provider-specific model slot."""
    paths = PROVIDER_SLOT_PATHS[provider]
    while True:
        for path in paths:
            lock_fh = open(path, "w")
            try:
                fcntl.flock(lock_fh, fcntl.LOCK_EX | fcntl.LOCK_NB)
                return lock_fh
            except OSError:
                lock_fh.close()
        time.sleep(1)


def _fresh_quota_state(name: str) -> dict | None:
    try:
        value = json.loads((QUOTA_STATE_DIR / f"{name}_quota.json").read_text(encoding="utf-8"))
        stamp = float(value["ts"])
        current = time.time()
        if (value.get("ok") is not True or stamp > current + 300
                or current - stamp > QUOTA_MAX_STALE_SEC):
            return None
        return value
    except (OSError, KeyError, TypeError, ValueError, json.JSONDecodeError):
        return None


def _future_reset(window: object) -> bool:
    if not isinstance(window, dict):
        return False
    raw = window.get("resetTime")
    try:
        return datetime.fromisoformat(str(raw).replace("Z", "+00:00")).timestamp() > time.time()
    except (TypeError, ValueError):
        return False


def _quota_window_blocked(window: object, limit: float) -> bool:
    if not isinstance(window, dict) or not _future_reset(window):
        return False
    try:
        return float(window.get("utilization")) >= limit
    except (TypeError, ValueError):
        return False


def _quota_member_available(state: dict) -> bool:
    if state.get("enabled") is False:
        return False
    return not (
        _quota_window_blocked(state.get("limit5h"), QUOTA_LIMIT_5H)
        or _quota_window_blocked(state.get("weekly"), QUOTA_LIMIT_WEEKLY)
    )


def provider_available(provider: str) -> bool:
    """Use quota snapshots only to route calls; unknown/stale state is fail-open."""
    if provider == "Antigravity":
        state = _fresh_quota_state("antigravity")
        return True if state is None else _quota_member_available(state)
    if provider == "Claude Opus":
        state = _fresh_quota_state("claude")
        return True if state is None else _quota_member_available(state)
    if provider == "Codex":
        states = [_fresh_quota_state("codex1"), _fresh_quota_state("codex2")]
        known = [state for state in states if state is not None]
        # A missing/stale member might still be runnable, so only close the pool
        # when every configured account has fresh, decisive evidence.
        return any(state is None for state in states) or any(
            _quota_member_available(state) for state in known)
    raise ValueError(f"unknown provider: {provider}")


def overlaps(pos: int, spans: Iterable[tuple[int, int]]) -> bool:
    return any(a <= pos < b for a, b in spans)


def internal_target(target: str) -> bool:
    clean = target.strip()
    return clean.startswith("#") or clean.startswith("/ko/") or clean.startswith("/en/")


def extract_links(
    path: Path, text: str, *, tagged: bool = False, review: bool = False,
    records: dict[str, ledger.Record] | None = None,
) -> list[Link]:
    """Find post links outside code/raw/math/inline-code spans.

    A link's relation is the ledger record of its ``data-lid``; ``records``
    defaults to the ledger this tick loaded.  ``tagged`` selects which side is
    returned: the default yields the links still waiting for a relation (no lid,
    or a lid without a record), and ``True`` yields the ones that have one, with
    ``relation`` filled in.  ``review`` yields the links whose record is
    ``requires-review`` instead; neither other side includes them, so a marked
    link waits for a human however the holds ledger reads.  The ordinal behind a
    link's ident counts every candidate in the file either way, so an ident
    names the same link whatever its record currently says.
    """
    book = RECORDS if records is None else records
    protected = protected_spans(text)
    result: list[Link] = []
    ordinal = 0
    for match in md_lint._LINK_ALL_RE.finditer(text):
        if overlaps(match.start(), protected):
            continue
        if match.start() and text[match.start() - 1] == "!":
            continue
        markup = match.group(0)
        pivot = markup.rfind("](")
        if pivot < 0:
            continue
        label = markup[1:pivot]
        target = markup[pivot + 2:-1].strip()
        if not internal_target(target):
            continue
        # Direct internal paths must resolve to a post.  Same-page anchors are
        # intentionally retained; they carry useful future learning metadata.
        if target.startswith("/"):
            base = target.split("#", 1)[0].split("?", 1)[0]
            if by_permalink(base, _POSTS) is None:
                continue
        tail = text[match.end():]
        ial = IAL_RE.match(tail)
        ial_start = match.end() if ial else None
        ial_end = match.end() + ial.end() if ial else None
        lid_match = LID_RE.search(ial.group(1)) if ial else None
        lid = lid_match.group(1) if lid_match else None
        record = book.get(lid) if lid else None
        found = record.relation if record and record.relation in RELATIONS else None
        marked = bool(record and record.relation == REVIEW_RELATION)
        reviewed = bool(record and record.reviewed)
        ordinal += 1
        side = "review" if marked else "tagged" if found else "open"
        if side != ("review" if review else "tagged" if tagged else "open"):
            continue
        stable = f"{path.relative_to(ROOT)}:{ordinal}:{target}:{label}"
        result.append(Link(
            ident=hashlib.sha1(stable.encode()).hexdigest()[:12], source=path,
            start=match.start(), end=match.end(), markup=markup, label=label,
            target=target, ial_start=ial_start, ial_end=ial_end,
            line=text.count("\n", 0, match.start()) + 1,
            lid=lid, relation=found, reviewed=reviewed,
        ))
    return result


def link_lid(text: str, link: Link) -> str | None:
    """이 링크 IAL 의 `data-lid` — 출현의 영속 식별자."""
    return link.lid


def ko_lids(paths: list[Path], texts: dict[Path, str]) -> set[str]:
    """이 unit 의 KO 쪽에 있는 모든 링크의 lid — 판정 여부와 무관하다."""
    found: set[str] = set()
    for path in paths:
        if path.parent.name != "ko":
            continue
        for kwargs in ({}, {"tagged": True}, {"review": True}):
            for link in extract_links(path, texts[path], **kwargs):
                lid = link_lid(texts[path], link)
                if lid:
                    found.add(lid)
    return found


def awaits_ko(link: Link, text: str, ko_all: set[str]) -> bool:
    """이 EN 링크의 판정과 검토가 KO 짝의 몫인가.

    판정의 정본은 KO 다. 같은 lid 를 가진 KO 링크가 이 unit 에 있으면 EN 은 그
    번역이므로 스스로 판정받지 않는다 — 1차 분류도 검증도 거치지 않고, KO 에
    값이 정해지면 상속 패스가 그 값을 옮기고, KO 가 검토되면 완료도 따라간다.
    KO 짝이 아직 판정 중이어도 마찬가지다. 그 사이 EN 을 따로 물으면 같은 출현에
    다른 값이 붙고, 그것이 KO/EN 불일치의 발생원이다.
    """
    if link.source.parent.name != "en":
        return False
    lid = link_lid(text, link)
    return bool(lid) and lid in ko_all


def settled_for_human(link: Link, text: str, ko_all: set[str]) -> bool:
    """이 링크가 사람 검토를 기다리지 않는가 — 자기 표지가 있거나 KO 에 위임됐다."""
    return link.reviewed or awaits_ko(link, text, ko_all)


def read_post(path: Path) -> str:
    return path.read_text(encoding="utf-8")


def record_decisions(links: list[Link], decisions: dict[str, str]) -> None:
    """First-pass verdicts become fresh, unreviewed records."""
    for link in links:
        RECORDS[link.lid] = ledger.Record(decisions[link.ident])


def record_reviewed(links: list[Link]) -> None:
    """Mark each link's record as reviewed, keeping its relation."""
    for link in links:
        RECORDS[link.lid] = ledger.Record(RECORDS[link.lid].relation, True)


def record_review_outcome(links: list[Link], disputed: set[str]) -> None:
    """Stamp agreements and turn disagreements into unreviewed holds."""
    for link in links:
        if link.ident in disputed:
            RECORDS[link.lid] = ledger.Record(REVIEW_RELATION)
        else:
            RECORDS[link.lid] = ledger.Record(RECORDS[link.lid].relation, True)


def paragraph_context(text: str, offset: int, radius: int) -> str:
    body_start = 0
    if text.startswith("---\n"):
        end = text.find("\n---\n", 4)
        if end >= 0:
            body_start = end + 5
    chunks = []
    for m in re.finditer(r"\S(?:.*?\S)?(?=\n\s*\n|\Z)", text[body_start:], re.DOTALL):
        chunks.append((body_start + m.start(), body_start + m.end(), m.group(0)))
    idx = next((i for i, (a, b, _) in enumerate(chunks) if a <= offset <= b), None)
    if idx is None:
        # An offset in the blank lines between paragraphs belongs to the one before.
        idx = max((i for i, (a, _b, _t) in enumerate(chunks) if a <= offset), default=0)
    lo, hi = max(0, idx - radius), min(len(chunks), idx + radius + 1)
    return "\n\n".join(c[2] for c in chunks[lo:hi])[:7000]


def target_context(link: Link, wide: bool, full: bool = False) -> tuple[str, str]:
    source_text = read_post(link.source)
    target = link.target
    anchor = target.split("#", 1)[1] if "#" in target else ""
    if target.startswith("#"):
        post_path = link.source
    else:
        base = target.split("#", 1)[0].split("?", 1)[0]
        post = by_permalink(base, _POSTS)
        post_path = post.path if post else link.source
    text = read_post(post_path)
    if full:
        return source_text[:FULL_SOURCE_CAP], text[:FULL_TARGET_CAP]
    context = ""
    if anchor:
        box = find_box(parse_labels(text), anchor=anchor)
        if box:
            lines = text.splitlines()
            starts = [box.line_start] + [p.line_start for p in box.proofs]
            ends = [box.line_end] + [p.line_end for p in box.proofs]
            pad = 8 if wide else 2
            context = "\n".join(lines[max(0, min(starts) - 1 - pad):min(len(lines), max(ends) + pad)])
        else:
            marker = re.search(rf"(?m)^.*(?:\{{#{re.escape(anchor)}\}}|id=[\"']{re.escape(anchor)}[\"']).*$", text)
            context = paragraph_context(text, marker.start() if marker else 0, 2 if wide else 1)
    if not context:
        # The target introduction is often enough to distinguish a prerequisite
        # from a mere analogy; the reviewer gets a larger slice.
        context = text[:9000 if wide else 4500]
    src = paragraph_context(source_text, link.start, 2 if wide else 1)
    return src, context[:12000 if wide else 6500]


def prompt_items(links: list[Link], wide: bool, full: bool = False) -> list[dict]:
    items = []
    for link in links:
        src, dst = target_context(link, wide, full)
        items.append({
            "id": link.ident,
            "language": "en" if "/en/" in str(link.source) else "ko",
            "link": link.markup,
            "target": link.target,
            "context_scope": "full-article" if full else "excerpt",
            "source_context": src,
            "target_context": dst,
        })
    return items


REASON_LANGUAGE = """Write every "reason" in Korean, whatever the language of the article. Keep mathematical terms in English and quote labels (e.g. Theorem 9, 정리 9) exactly as they appear.
"""

# 세 프롬프트가 공유하는 판정 원칙. 한 곳에만 둔다 — 복사본이 여럿이면 따로 표류한다.
RELATION_PRINCIPLE = """Each class is about the claims the source article itself makes:
- required: the link is the ground for a claim the source article makes: a fact it states as true and goes on from, a construction it builds on, or a definition it stands on, including one it pauses to recall. This holds whether or not the source reproduces the proof, and whatever kind of target it is. An example is required when the fact or object the source goes on to use was established there.
- weak: the link supports something the source does not itself claim, such as a remark, a perspective, a passing generalisation, or an attribution, so the sentence it sits in carries no weight in the article. A link that only gives an advanced name to a fact the source has already established on its own (for example, calling an already described inclusion a "full subcategory") is weak for the same reason: the ground of that claim is the source, not the target.
- forward: the source is self-contained and says the target will later extend, develop, or revisit the present idea.

Decide by asking whether the source article makes the claim this link grounds. Do not decide by form or by the target's type: a parenthetical citation, the word "example", a definition the source restates in full, or a proof the source leaves out does not by itself make a link weak, and dependency-sounding wording such as "by applying" does not by itself make it required. Same-page anchors are classified the same way.
"""

FIRST_PROMPT = ("""You classify semantic relations of internal links in a mathematics blog.
Return JSON only: {"items":[{"id":"...","relation":"required|weak|forward","confidence":"high|medium","reason":"short"}]}.
""" + REASON_LANGUAGE + "\n" + RELATION_PRINCIPLE + """
Confidence rule is deliberately strict: HIGH only when the supplied context makes exactly one class clear. If there is any plausible doubt, missing context, mixed role, or interpretive choice, output MEDIUM. Never use HIGH merely because a phrase matches a familiar pattern. Do not use tools and do not alter files.

ITEMS:
""")

REVIEW_PROMPT = ("""You are the independent final reviewer for ambiguous dependency-link classifications in a mathematics blog. You have wider excerpts than the first model.
Return JSON only: {"items":[{"id":"...","relation":"required|weak|forward|ambiguous","reason":"short"}]}.
""" + REASON_LANGUAGE + "\n" + RELATION_PRINCIPLE + """
Choose ambiguous if the excerpts still do not justify one class. Do not use tools and do not alter files.

Each item states its context_scope. "excerpt" means you see passages around the link. "full-article" means source_context and target_context are the complete articles, truncated only if extremely long: there is no wider context to wait for, so decide on the evidence given and reserve ambiguous for links whose role is genuinely undecidable rather than merely unstated.

ITEMS:
""")

VERIFY_PROMPT = ("""You classify semantic relations of internal links in a mathematics blog. Your classification is an independent second opinion: another model has already judged these links, you are deliberately not shown its verdict, and your answer is compared against it. Judge the links on the excerpts alone.
Return JSON only: {"items":[{"id":"...","relation":"required|weak|forward|ambiguous","reason":"short"}]}.
""" + REASON_LANGUAGE + "\n" + RELATION_PRINCIPLE + """
Choose ambiguous only when the excerpts leave the link's role genuinely undecidable. Do not use tools and do not alter files.

ITEMS:
""")

PROMPTS = {"first": FIRST_PROMPT, "review": REVIEW_PROMPT, "verify": VERIFY_PROMPT}


def allows_ambiguous(mode: str) -> bool:
    return mode != "first"


def parse_json_value(raw: str) -> dict:
    raw = re.sub(r"^```(?:json)?\s*|\s*```$", "", raw.strip(), flags=re.I)
    decoder = json.JSONDecoder()
    for pos, ch in enumerate(raw):
        if ch not in "[{":
            continue
        try:
            value, _ = decoder.raw_decode(raw[pos:])
        except json.JSONDecodeError:
            continue
        if isinstance(value, list):
            return {"items": value}
        if isinstance(value, dict):
            return value
    raise RuntimeError(f"model returned no JSON value: {raw[:300]!r}")


def call_antigravity(items: list[dict], *, mode: str) -> dict:
    prompt = PROMPTS[mode] + json.dumps(items, ensure_ascii=False)
    proc = subprocess.run(
        [AGY_BIN, "--print", prompt, "--model", AGY_MODEL,
         "--output-format", "json", "--disable-slash-commands", "--print-timeout", "15m"],
        cwd="/tmp", stdin=subprocess.DEVNULL, capture_output=True, text=True,
        timeout=MODEL_TIMEOUT,
    )
    if proc.returncode:
        raise RuntimeError(f"Antigravity exited {proc.returncode}: {proc.stderr.strip()[:400]}")
    envelope = json.loads(proc.stdout)
    if envelope.get("status") != "SUCCESS":
        raise RuntimeError(f"Antigravity status {envelope.get('status')}: {envelope.get('error', '')}")
    return parse_json_value(str(envelope.get("response", "")))


def call_opus(items: list[dict], *, mode: str) -> dict:
    prompt = PROMPTS[mode] + json.dumps(items, ensure_ascii=False)
    env = {**os.environ, "CLAUDE_CODE_DISABLE_ADVISOR_TOOL": "1"}
    proc = subprocess.run(
        [CLAUDE_BIN, "-p", "--model", CLAUDE_MODEL, "--output-format", "text"],
        input="[cron]\n\n" + prompt, cwd=str(ROOT), env=env,
        capture_output=True, text=True, timeout=MODEL_TIMEOUT,
    )
    if proc.returncode:
        raise RuntimeError(f"Claude Opus exited {proc.returncode}: {proc.stderr.strip()[:400]}")
    return parse_json_value(proc.stdout)


def codex_output_schema(items: list[dict], *, mode: str) -> dict:
    properties = {
        "id": {"type": "string", "enum": [str(item["id"]) for item in items]},
        "relation": {
            "type": "string",
            "enum": sorted(RELATIONS | ({"ambiguous"} if allows_ambiguous(mode) else set())),
        },
        "reason": {"type": "string"},
    }
    required = ["id", "relation", "reason"]
    if mode == "first":
        properties["confidence"] = {"type": "string", "enum": ["high", "medium"]}
        required.append("confidence")
    count = len(items)
    return {
        "type": "object",
        "properties": {
            "items": {
                "type": "array",
                "items": {
                    "type": "object",
                    "properties": properties,
                    "required": required,
                    "additionalProperties": False,
                },
                "minItems": count,
                "maxItems": count,
            },
        },
        "required": ["items"],
        "additionalProperties": False,
    }


def call_codex(items: list[dict], *, mode: str) -> dict:
    """Use the multi-auth Codex CLI through its structured-output mode."""
    prompt = PROMPTS[mode] + json.dumps(items, ensure_ascii=False)
    model = CODEX_FIRST_MODEL if mode == "first" else CODEX_REVIEW_MODEL
    effort = CODEX_FIRST_EFFORT if mode == "first" else CODEX_REVIEW_EFFORT
    with tempfile.TemporaryDirectory(prefix="dependency-codex-") as tmp:
        tmp_path = Path(tmp)
        schema_path = tmp_path / "schema.json"
        output_path = tmp_path / "last-message.json"
        schema_path.write_text(
            json.dumps(codex_output_schema(items, mode=mode), ensure_ascii=False),
            encoding="utf-8",
        )
        proc = subprocess.run(
            [CODEX_BIN, "exec", "--model", model,
             "-c", f'model_reasoning_effort="{effort}"',
             "--sandbox", "read-only", "--skip-git-repo-check", "--ephemeral",
             "--color", "never", "--output-schema", str(schema_path),
             "--output-last-message", str(output_path), "-"],
            input="[cron]\n\n" + prompt, cwd=tmp,
            capture_output=True, text=True, timeout=MODEL_TIMEOUT,
        )
        if proc.returncode:
            raise RuntimeError(f"Codex exited {proc.returncode}: {proc.stderr.strip()[:400]}")
        if not output_path.exists():
            raise RuntimeError("Codex produced no last-message file")
        return parse_json_value(output_path.read_text(encoding="utf-8"))


def call_provider(provider: str, items: list[dict], *, mode: str) -> dict:
    slot_fh = acquire_provider_slot(provider)
    try:
        if not provider_available(provider):
            raise RuntimeError(f"{provider} quota gate closed while waiting for a slot")
        if provider == "Antigravity":
            return call_antigravity(items, mode=mode)
        if provider == "Claude Opus":
            return call_opus(items, mode=mode)
        if provider == "Codex":
            return call_codex(items, mode=mode)
        raise ValueError(f"unknown provider: {provider}")
    finally:
        slot_fh.close()


ProviderCaller = Callable[[list[dict]], dict]

CHAINS = {
    "first": ("Antigravity", "Claude Opus", "Codex"),
    "review": ("Claude Opus", "Codex"),
}


def provider_attempts(
    *, mode: str, order: Iterable[str] | None = None,
) -> list[tuple[str, ProviderCaller]]:
    chain = tuple(order) if order is not None else CHAINS[mode]
    return [
        (provider, lambda items, provider=provider: call_provider(provider, items, mode=mode))
        for provider in chain if provider_available(provider)
    ]


def valid_results(payload: dict, expected: set[str], *, mode: str) -> dict[str, dict]:
    rows = payload.get("items")
    if not isinstance(rows, list):
        return {}
    out = {}
    allowed = RELATIONS | ({"ambiguous"} if allows_ambiguous(mode) else set())
    for row in rows:
        if not isinstance(row, dict) or row.get("id") not in expected:
            continue
        relation = str(row.get("relation", "")).lower()
        if relation not in allowed:
            continue
        if mode == "first" and str(row.get("confidence", "")).lower() not in {"high", "medium"}:
            continue
        out[row["id"]] = row
    return out


def request_complete_results(
    items: list[dict], *, mode: str, stage: str,
    attempts: list[tuple[str, ProviderCaller]],
) -> dict[str, dict]:
    """Keep valid rows and recover only incomplete IDs within this cron tick.

    Every accepted row carries the provider that produced it under ``provider``:
    the verification pass routes a link to a model other than the one that
    decided it, so the decider has to be recorded per link, not per unit.
    """
    accepted: dict[str, dict] = {}
    pending = items
    last_issue = "incomplete model response"
    if not attempts:
        raise RuntimeError(f"{stage}: every provider is closed by the quota gate")
    for attempt_index, (model_name, caller) in enumerate(attempts):
        expected = {str(item["id"]) for item in pending}
        try:
            payload = caller(pending)
            for ident, row in valid_results(payload, expected, mode=mode).items():
                accepted[ident] = {**row, "provider": model_name}
            last_issue = "model omitted or invalidated requested items"
        except Exception as exc:
            # A malformed envelope, timeout, or provider failure is recoverable here.
            # Do not log the exception on a recovered run: the dashboard treats words
            # such as "error" and "failed" in the run log as a real job failure.
            last_issue = f"{type(exc).__name__}: {str(exc)[:240]}"
        pending = [item for item in pending if str(item["id"]) not in accepted]
        if not pending:
            return accepted
        if attempt_index + 1 < len(attempts):
            next_name = attempts[attempt_index + 1][0]
            log(f"{stage}: falling back for {len(pending)} incomplete item(s) to {next_name}")
    missing = sorted(str(item["id"]) for item in pending)
    raise RuntimeError(
        f"{stage} omitted/invalidated {len(missing)} item(s) after provider chain: "
        f"{missing[:4]} ({last_issue})"
    )


def classify(
    links: list[Link], round_no: int = 1,
) -> tuple[dict[str, str], dict[str, str], list[dict]]:
    first_attempts = provider_attempts(mode="first")
    review_attempts = provider_attempts(mode="review")
    full = round_no >= 2
    log(
        f"round {round_no}/{MAX_ROUNDS}"
        + (" (review reads the complete articles)" if full else "")
        + "; quota route: first=" + " > ".join(name for name, _ in first_attempts)
        + "; review=" + " > ".join(name for name, _ in review_attempts)
    )
    first: dict[str, dict] = {}
    for i in range(0, len(links), CHUNK_SIZE):
        chunk = links[i:i + CHUNK_SIZE]
        values = request_complete_results(
            prompt_items(chunk, False), mode="first", stage="first pass",
            attempts=first_attempts,
        )
        first.update(values)
    decisions = {ident: str(row["relation"]).lower() for ident, row in first.items()
                 if str(row["confidence"]).lower() == "high"}
    decided_by = {ident: first[ident]["provider"] for ident in decisions}
    medium = [link for link in links if str(first[link.ident]["confidence"]).lower() == "medium"]
    log(f"first pass: high={len(decisions)}, medium={len(medium)}")
    ambiguous = []
    review_chunk = FULL_CHUNK_SIZE if full else CHUNK_SIZE
    for i in range(0, len(medium), review_chunk):
        chunk = medium[i:i + review_chunk]
        values = request_complete_results(
            prompt_items(chunk, True, full), mode="review", stage="review",
            attempts=review_attempts,
        )
        for ident, row in values.items():
            relation = str(row["relation"]).lower()
            if relation == "ambiguous":
                ambiguous.append({"id": ident, "reason": row.get("reason", "")})
            else:
                decisions[ident] = relation
                decided_by[ident] = row["provider"]
    if medium:
        log(f"review: decided={len(medium) - len(ambiguous)}, ambiguous={len(ambiguous)}")
    if set(decisions) | {x["id"] for x in ambiguous} != {x.ident for x in links}:
        raise RuntimeError("internal decision accounting mismatch")
    return decisions, decided_by, ambiguous


def verifier_chain(provider: str | None) -> tuple[str, ...]:
    """Who re-judges a link the given provider decided."""
    return VERIFIER_CHAINS.get(provider or "", DEFAULT_VERIFIER_CHAIN)


def verify_groups(links: list[Link], decided_by: dict[str, str]) -> dict[tuple[str, ...], list[Link]]:
    groups: dict[tuple[str, ...], list[Link]] = {}
    for link in links:
        groups.setdefault(verifier_chain(decided_by.get(link.ident)), []).append(link)
    return groups


def verify(links: list[Link], decided_by: dict[str, str]) -> dict[str, dict]:
    """Re-judge each link with a model other than the one that decided it."""
    verdicts: dict[str, dict] = {}
    for chain, group in verify_groups(links, decided_by).items():
        attempts = provider_attempts(mode="verify", order=chain)
        log(f"verify {len(group)} link(s) via " + " > ".join(name for name, _ in attempts))
        for i in range(0, len(group), CHUNK_SIZE):
            chunk = group[i:i + CHUNK_SIZE]
            verdicts.update(request_complete_results(
                prompt_items(chunk, True), mode="verify", stage="verify",
                attempts=attempts,
            ))
    if set(verdicts) != {link.ident for link in links}:
        raise RuntimeError("internal verification accounting mismatch")
    return verdicts


def hard_lint(path: Path, text: str) -> set[str]:
    return {p for p in md_lint.collect_problems(str(path), text, "", {})
            if not p.startswith(md_lint.SOFT)}


def unit_key(paths: list[Path]) -> str:
    return "+".join(str(p.relative_to(ROOT)) for p in paths)


def unit_digest(
    paths: list[Path], texts: dict[Path, str], parked: set[str] = frozenset(),
) -> str:
    """Hash the unit's text together with the records of its links.

    A relation lives in the ledger, not in the text, so the text alone no longer
    changes when a verdict does.  Records of human-parked links are left out:
    resolving a hold swaps a parked link's ``requires-review`` for a relation,
    and that known bookkeeping edit must not invalidate the verification of every
    other link in the unit, while prose edits and relation changes on non-parked
    links must still do so.
    """
    rows = []
    for path in paths:
        for link in unit_links(path, texts[path]):
            if link.lid and link.ident not in parked:
                record = RECORDS.get(link.lid)
                if record:
                    rows.append(f"{link.lid}={record.relation}:{int(record.reviewed)}")
    return sha("\0".join(texts[p] for p in paths) + "\0\0" + "\n".join(sorted(set(rows))))


def verification_fingerprint(
    paths: list[Path], texts: dict[Path, str], parked: set[str],
) -> str:
    return unit_digest(paths, texts, parked)


def verified_at_content(entry: dict, raw_hash: str, content_hash: str) -> bool:
    """Accept the canonical hash, with an exact-raw fallback for old state."""
    canonical = entry.get("verified_content_hash")
    if canonical is not None:
        return canonical == content_hash
    return entry.get("verified_hash") == raw_hash


def is_local_only_untracked_unit(paths: list[Path]) -> bool:
    """True for untracked posts in an explicitly approved local-only stream."""
    if not paths or not all(
        any(path.is_relative_to(root) for root in LOCAL_ONLY_POST_ROOTS)
        for path in paths
    ):
        return False
    rels = [str(path.relative_to(ROOT)) for path in paths]
    proc = subprocess.run(
        ["git", "ls-files", "-z", "--", *rels], cwd=str(ROOT),
        capture_output=True, text=True,
    )
    if proc.returncode:
        raise RuntimeError(f"could not inspect tracked paths: {proc.stderr.strip()[:200]}")
    return not any(proc.stdout.split("\0"))


def iter_units() -> list[list[Path]]:
    """A KO post and its EN counterpart form one unit; unpaired posts stand alone."""
    units: list[list[Path]] = []
    paired_en: set[Path] = set()
    for post in _POSTS:
        if post.lang != "ko":
            continue
        en = en_counterpart(post, _POSTS)
        paths = [post.path]
        if en:
            paths.append(en.path)
            paired_en.add(en.path)
        units.append(paths)
    for post in _POSTS:
        if post.lang == "en" and post.path not in paired_en:
            units.append([post.path])
    return units


def select_unit(
    state: dict, updates: dict[str, dict],
) -> tuple[str, list[Path], dict[Path, str], list[Link], FileLockSet] | None:
    """Take the first unit with work and return first, stamp, or verify.

    Classifying comes first: a unit is verified only once no link in it is
    waiting for a relation.  Links parked for a human ruling are invisible to
    every stage, and so are EN links that share a lid with a KO link in the
    unit: they are the KO link's translation and use its record.  A link
    without a lid waits for the next tick's mint.  Records marked reviewed are
    permanently complete.  ``stamp`` migrates a legacy state-only verification
    to the reviewed mark without spending another model call.
    """
    now = time.time()
    parked = parked_idents()
    for paths in iter_units():
        lease = try_acquire_file_locks(paths)
        if lease is None:
            continue
        try:
            rels = [str(p.relative_to(ROOT)) for p in paths]
            if dirty_paths(rels, ROOT):
                lease.release()
                continue
            texts = {p: p.read_text(encoding="utf-8") for p in paths}
            key = unit_key(paths)
            fingerprint = unit_digest(paths, texts)
            verify_fingerprint = verification_fingerprint(paths, texts, parked)
            entry = state.get("units", {}).get(key, {})
            at_judged_content = entry.get("hash") == fingerprint
            if at_judged_content and entry.get("retry_after", 0) > now:
                lease.release()
                continue
            ko_all = ko_lids(paths, texts)

            def own(link: Link) -> bool:
                return (link.ident not in parked and link.lid is not None
                        and not awaits_ko(link, texts[link.source], ko_all))

            links = [link for p in paths for link in extract_links(p, texts[p]) if own(link)]
            if links:
                if at_judged_content and entry.get("status") == "exhausted":
                    # An exhausted unit spent all MAX_ROUNDS rounds without a
                    # verdict.  It comes back only when the files change, which
                    # also resets the round counter, so a newly added link
                    # reopens it.
                    lease.release()
                    continue
                return "first", paths, texts, links, lease
            tagged = [link for p in paths
                      for link in extract_links(p, texts[p], tagged=True) if own(link)]
            if not tagged:
                updates[key] = {
                    "status": "done", "hash": fingerprint,
                    "verified_hash": fingerprint,
                    "verified_content_hash": verify_fingerprint,
                    "checked_at": int(now), "links": 0,
                }
                lease.release()
                continue
            pending_review = [link for link in tagged if not link.reviewed]
            if not pending_review:
                updates[key] = {
                    **cleared(entry), "status": "done", "hash": fingerprint,
                    "verified_hash": fingerprint,
                    "verified_content_hash": verify_fingerprint,
                    "verified_at": entry.get("verified_at", int(now)),
                    "verify": entry.get("verify", "author-reviewed"),
                    "reviewed_marker_version": 1,
                }
                lease.release()
                continue
            if (not entry.get("reviewed_marker_version")
                    and verified_at_content(entry, fingerprint, verify_fingerprint)):
                return "stamp", paths, texts, pending_review, lease
            decided_by = entry.get("decided_by", {}) if at_judged_content else {}
            chains = {verifier_chain(decided_by.get(link.ident)) for link in pending_review}
            if not all(any(provider_available(p) for p in chain) for chain in chains):
                # A cross-model verifier has no stand-in.  Leave the unit for a
                # tick where its quota is open instead of waiting on a slot.
                lease.release()
                continue
            return "verify", paths, texts, pending_review, lease
        except Exception:
            lease.release()
            raise
    return None


def exhausted_units() -> dict[str, dict]:
    """Units that spent every round without a verdict, still at the judged content."""
    state = load_state()
    out = {}
    for paths in iter_units():
        entry = state.get("units", {}).get(unit_key(paths), {})
        if entry.get("status") != "exhausted":
            continue
        try:
            texts = {p: p.read_text(encoding="utf-8") for p in paths}
        except OSError:
            continue
        if entry.get("hash") == unit_digest(paths, texts):
            out[unit_key(paths)] = entry
    return out


def backlog_complete() -> bool:
    """True when every link left is classified, verified, exhausted, or parked."""
    spent = exhausted_units()
    state = load_state()
    parked = parked_idents()
    for paths in iter_units():
        key = unit_key(paths)
        if key in spent:
            continue
        try:
            texts = {p: p.read_text(encoding="utf-8") for p in paths}
        except OSError:
            return False
        ko_all = ko_lids(paths, texts)
        if any(link.ident not in parked and not awaits_ko(link, texts[p], ko_all)
               for p in paths for link in extract_links(p, texts[p])):
            return False
        entry = state.get("units", {}).get(key, {})
        raw_hash = unit_digest(paths, texts)
        content_hash = verification_fingerprint(paths, texts, parked)
        pending_review = [
            link for p in paths for link in extract_links(p, texts[p], tagged=True)
            if link.ident not in parked
            and not settled_for_human(link, texts[p], ko_all)
        ]
        legacy_complete = (not entry.get("reviewed_marker_version")
                           and verified_at_content(entry, raw_hash, content_hash))
        if pending_review and not legacy_complete:
            return False
    return True


def mark_backlog_complete() -> None:
    STATE_DIR.mkdir(parents=True, exist_ok=True)
    COMPLETE_PATH.write_text(
        json.dumps({"completed_at": datetime.now().astimezone().isoformat(timespec="seconds")})
        + "\n",
        encoding="utf-8",
    )


def cleared(entry: dict) -> dict:
    """The unit's history without the marks of a failed tick."""
    return {k: v for k, v in entry.items() if k not in {"error", "retry_after", "items"}}


def guard_unchanged(paths: list[Path], originals: dict[Path, str]) -> None:
    rels = [str(p.relative_to(ROOT)) for p in paths]
    if dirty_paths(rels, ROOT) or any(
        p.read_text(encoding="utf-8") != originals[p] for p in paths
    ):
        raise RuntimeError("target changed while models were running")


LEDGER_REL = str(ledger.PATH.relative_to(ROOT))


def publish_records(paths: list[Path], *, detail: str, commit: bool) -> None:
    """Write the ledger this tick changed, and own the result in Git or not at all."""
    key = unit_key(paths)
    before = ledger.PATH.read_text(encoding="utf-8") if ledger.PATH.exists() else None
    ledger.save(RECORDS)
    if not commit:
        return log(f"saved without commit: {key}")
    committed = commit_outputs(
        "Link Dependencies Classifier", [LEDGER_REL], detail, log=log, repo=ROOT,
    )
    if not committed:
        # Never leave unowned generated edits behind.
        if before is not None:
            ledger.PATH.write_text(before, encoding="utf-8")
        raise RuntimeError("could not commit worker outputs; restored the ledger")


def publish(
    paths: list[Path], originals: dict[Path, str], rendered: dict[Path, str],
    *, detail: str, commit: bool,
) -> None:
    """Write rewritten posts (lid minting), and own the result in Git or not at all."""
    key = unit_key(paths)
    for path in paths:
        introduced = hard_lint(path, rendered[path]) - hard_lint(path, originals[path])
        if introduced:
            raise RuntimeError(
                f"annotation introduces md_lint findings in {path}: {sorted(introduced)[:3]}"
            )
    for path in paths:
        path.write_text(rendered[path], encoding="utf-8")
    if not commit:
        return log(f"saved without commit: {key}")
    if is_local_only_untracked_unit(paths):
        return log(f"saved local-only: {key} (Git commit skipped)")
    committed = commit_outputs(
        "Link Dependencies Classifier", [str(p.relative_to(ROOT)) for p in paths],
        detail, log=log, repo=ROOT,
    )
    if not committed:
        # The targets were clean before this tick, so restoring them cannot
        # overwrite user work.  Never leave unowned generated edits behind.
        for path in paths:
            if path.exists() and path.read_text(encoding="utf-8") == rendered[path]:
                path.write_text(originals[path], encoding="utf-8")
        raise RuntimeError("could not commit worker outputs; restored originals")


def run_first_pass(
    paths: list[Path], originals: dict[Path, str], links: list[Link],
    entry: dict, fingerprint: str, *, commit: bool,
) -> int:
    key = unit_key(paths)
    # Entries written before the round counter existed already spent one
    # excerpt round, so they resume at the full-article round.
    legacy = 1 if entry.get("status") == "ambiguous" else 0
    previous = entry.get("rounds", legacy) if entry.get("hash") == fingerprint else 0
    round_no = previous + 1
    decisions, decided_by, ambiguous = classify(links, round_no)
    if ambiguous:
        exhausted = round_no >= MAX_ROUNDS
        record = {
            "status": "exhausted" if exhausted else "ambiguous",
            "hash": fingerprint, "checked_at": int(time.time()),
            "rounds": round_no, "items": ambiguous,
        }
        if not exhausted:
            record["retry_after"] = int(time.time() + BLOCK_SEC)
        merge_unit_states({key: record})
        log(
            f"blocked {key}: {len(ambiguous)} ambiguous decision(s) "
            f"in round {round_no}/{MAX_ROUNDS}; no files changed"
            + ("; giving up until the files change" if exhausted else "")
        )
        return 0
    guard_unchanged(paths, originals)
    record_decisions(links, decisions)
    publish_records(paths, commit=commit,
                    detail=f"{paths[0].stem} 링크 {len(links)}건 분류")
    merge_unit_states({key: {
        "status": "done", "hash": unit_digest(paths, originals),
        "checked_at": int(time.time()), "links": len(links),
        "decided_by": {**entry.get("decided_by", {}), **decided_by},
    }})
    for link in links:
        log(f"classified {link.where()} {decisions[link.ident]} "
            f"[{decided_by[link.ident]}] {link.brief()}")
    log(f"done {key}: {len(links)} relation tag(s)")
    return 0


def run_verify_pass(
    paths: list[Path], originals: dict[Path, str], links: list[Link],
    entry: dict, fingerprint: str, *, commit: bool,
) -> int:
    key = unit_key(paths)
    decided_by = entry.get("decided_by", {}) if entry.get("hash") == fingerprint else {}
    # The text carries no relation, so the verifier cannot anchor on the verdict.
    verdicts = verify(links, decided_by)
    disputed = [(link, str(verdicts[link.ident]["relation"]).lower()) for link in links
                if str(verdicts[link.ident]["relation"]).lower() != link.relation]
    if not disputed:
        guard_unchanged(paths, originals)
        record_review_outcome(links, set())
        publish_records(paths, commit=commit,
                        detail=f"{paths[0].stem} 링크 {len(links)}건 검토 완료")
        fingerprint = unit_digest(paths, originals)
        content_hash = verification_fingerprint(paths, originals, parked_idents())
        merge_unit_states({key: {
            **cleared(entry), "status": "done", "hash": fingerprint,
            "verified_hash": fingerprint,
            "verified_content_hash": content_hash,
            "verified_at": int(time.time()), "verify": "agreed",
            "reviewed_marker_version": 1,
        }})
        log(f"verified {key}: {len(links)} relation(s) confirmed")
        return 0
    guard_unchanged(paths, originals)
    disputed_ids = {link.ident for link, _ in disputed}
    record_review_outcome(links, disputed_ids)
    publish_records(paths, commit=commit,
                    detail=f"{paths[0].stem} 링크 {len(disputed)}건 재검토 보류")
    now = int(time.time())
    holds = {}
    lines = []
    for link, relation in disputed:
        row = verdicts[link.ident]
        verifier = row.get("provider", "")
        holds[link.ident] = {
            "path": str(link.source.relative_to(ROOT)), "line": link.line,
            "lid": link.lid,
            "label": link.label, "target": link.target, "markup": link.markup,
            "old": link.relation, "new": relation,
            "reason": str(row.get("reason", ""))[:600],
            "decided_by": decided_by.get(link.ident, ""), "verifier": verifier,
            "unit": key, "at": now,
        }
        lines.append(f"{link.where()} {link.relation}→{relation} [{verifier}] {link.brief()}")
    merge_holds(holds)
    settled_hash = unit_digest(paths, originals)
    content_hash = verification_fingerprint(
        paths, originals, parked_idents() | set(holds),
    )
    merge_unit_states({key: {
        **cleared(entry), "hash": settled_hash, "verified_hash": settled_hash,
        "verified_content_hash": content_hash,
        "verified_at": now, "verify": "disputed", "checked_at": now,
        "reviewed_marker_version": 1,
    }})
    for line in lines:
        log("disputed " + line)
    log(f"held {key}: {len(disputed)} link(s) marked {REVIEW_RELATION} pending a ruling")
    notify(
        f"[dependency] 링크 {len(disputed)}건 재검토 불일치",
        f"{paths[0].stem}\n" + "\n".join(lines[:8])
        + (f"\n… 외 {len(lines) - 8}건" if len(lines) > 8 else "")
        + "\n\n눌러서 대시보드 감사 → 의존성 링크 보류에서 판정.",
    )
    return 0


LID_LEDGER = Path.home() / ".local" / "state" / "link-ids.txt"
LID_ALPHABET = "0123456789abcdefghijklmnopqrstuvwxyz"
LID_LENGTH = 5


def unit_links(path: Path, text: str) -> list[Link]:
    """이 글의 모든 링크를 소스 순서로. extract_links 는 한 side 씩만 돌려준다."""
    seen: dict[int, Link] = {}
    for kwargs in ({}, {"tagged": True}, {"review": True}):
        for link in extract_links(path, text, **kwargs):
            seen[link.start] = link
    return [seen[k] for k in sorted(seen)]


def mint_lids(*, commit: bool) -> None:
    """lid 없는 링크에 식별자를 발급한다. 판정보다 **먼저** 돈다.

    관계는 lid 를 키로 원장에 적히므로 lid 없는 링크는 판정을 담을 곳이 없다.
    KO 링크의 lid 는 번역을 타고 EN 으로 건너가 두 링크가 한 레코드를 공유하게
    하고, EN 에만 있는 링크(번역이 KO 에 없는 링크를 만들었거나 lid 를 흘린 경우)도
    자기 lid 를 받아 따로 판정된다. 발급을 매 틱의 첫 단계로 두어 같은 틱에서 새
    링크가 판정되기 전에 식별자를 갖는 것을 보장한다.

    값은 36진수 5자 난수이고, `현재 코퍼스 ∪ 발급 대장` 과 대조해 다시 뽑으므로
    유일성은 확률이 아니라 검사로 보장된다. 지워진 링크의 id 가 풀려서 다른
    링크에 재배정되지 않도록 대장은 한 번 발급한 값을 계속 들고 있는다.
    """
    scope = ROOT / "_posts" / "Math"
    targets = sorted(p for p in scope.rglob("*.md") if p.parent.name in ("ko", "en"))
    texts, pending = {}, {}
    for path in targets:
        text = path.read_text(encoding="utf-8")
        missing = [x for x in unit_links(path, text) if link_lid(text, x) is None]
        if missing:
            texts[path], pending[path] = text, missing
    if not pending:
        return

    used = set()
    if LID_LEDGER.exists():
        used |= {ln.strip() for ln in LID_LEDGER.read_text(encoding="utf-8").splitlines() if ln.strip()}
    for path in ROOT.joinpath("_posts").rglob("*.md"):
        used |= set(LID_RE.findall(path.read_text(encoding="utf-8")))

    def draw() -> str:
        while True:
            value = "".join(secrets.choice(LID_ALPHABET) for _ in range(LID_LENGTH))
            if value not in used:
                used.add(value)
                return value

    rendered, minted = {}, []
    for path, links in pending.items():
        if dirty_paths([str(path.relative_to(ROOT))], ROOT):
            continue
        text, edits = texts[path], []
        for link in links:
            value = draw()
            minted.append(value)
            if link.ial_start is None:
                edits.append((link.end, link.end, f'{{: data-lid="{value}" }}'))
            else:
                ial = text[link.ial_start:link.ial_end]
                edits.append((link.ial_start, link.ial_end,
                              ial[:2] + f' data-lid="{value}"' + ial[2:]))
        for start, end, replacement in sorted(edits, reverse=True):
            text = text[:start] + replacement + text[end:]
        rendered[path] = text
    if not rendered:
        return

    lease = try_acquire_file_locks(list(rendered))
    if lease is None:
        return log("lid: 대상 글이 잠겨 있다 — 다음 틱에")
    try:
        LID_LEDGER.parent.mkdir(parents=True, exist_ok=True)
        with LID_LEDGER.open("a", encoding="utf-8") as handle:
            handle.write("".join(value + "\n" for value in minted))
        # 추적되는 글과 로컬 전용(untracked GW) 글을 한 번에 넘기면 커밋 경로가 갈려
        # 둘 다 실패한다 — 나눠서 게시한다.
        local = [p for p in rendered if is_local_only_untracked_unit([p])]
        for group in ([p for p in rendered if p not in local], local):
            if group:
                publish(group, texts, rendered, commit=commit,
                        detail=f"링크 식별자 {len(minted)}건 발급")
    finally:
        lease.release()
    log(f"lid: {len(minted)} identifier(s) minted across {len(rendered)} post(s)")


def run_stamp_pass(
    paths: list[Path], originals: dict[Path, str], links: list[Link],
    entry: dict, *, commit: bool,
) -> int:
    """Migrate a completed legacy verification from state into each link's record."""
    key = unit_key(paths)
    guard_unchanged(paths, originals)
    record_reviewed(links)
    publish_records(paths, commit=commit,
                    detail=f"{paths[0].stem} 기존 검토 링크 {len(links)}건 마커 이관")
    fingerprint = unit_digest(paths, originals)
    merge_unit_states({key: {
        **cleared(entry), "status": "done", "hash": fingerprint,
        "verified_hash": fingerprint,
        "verified_content_hash": verification_fingerprint(
            paths, originals, parked_idents()),
        "reviewed_marker_version": 1,
    }})
    log(f"stamped {key}: {len(links)} legacy reviewed link(s)")
    return 0


def process_once(dry_run: bool = False, *, commit: bool = True) -> int:
    if not dry_run:
        mint_lids(commit=commit)
    state = load_state()
    scan_updates: dict[str, dict] = {}
    selected = select_unit(state, scan_updates)
    merge_unit_states(scan_updates)
    if not selected:
        if backlog_complete():
            if not dry_run:
                mark_backlog_complete()
            spent = exhausted_units()
            log(
                f"backlog complete; marker={COMPLETE_PATH}"
                + (f"; {len(spent)} unit(s) left undecided after {MAX_ROUNDS} rounds: "
                   + ", ".join(sorted(spent)[:3]) if spent else "")
            )
        else:
            log("queue temporarily unavailable (pending target is locked/dirty/backed off)")
        return 0
    stage, paths, originals, links, lease = selected
    key = unit_key(paths)
    noun = "unclassified" if stage == "first" else "classified"
    try:
        log(f"selected {key} for {stage} pass: {len(links)} {noun} link(s)")
        if dry_run:
            for link in links:
                log(f"dry-run {stage} {link.where()} {link.relation or '—'} {link.brief()}")
            return 0
        fingerprint = unit_digest(paths, originals)
        entry = state.get("units", {}).get(key, {})
        runner = {
            "first": run_first_pass,
            "verify": run_verify_pass,
        }.get(stage)
        try:
            if stage == "stamp":
                return run_stamp_pass(paths, originals, links, entry, commit=commit)
            assert runner is not None
            return runner(paths, originals, links, entry, fingerprint, commit=commit)
        except Exception as exc:
            merge_unit_states({key: {
                **entry, "status": "error", "hash": fingerprint,
                "checked_at": int(time.time()),
                "retry_after": int(time.time() + 3600), "error": str(exc)[:1000],
            }})
            log(f"ERROR {key}: {exc}")
            return 1
    finally:
        lease.release()


def status() -> int:
    state = load_state()
    counts: dict[str, int] = {}
    verify_counts: dict[str, int] = {}
    for value in state.get("units", {}).values():
        counts[value.get("status", "unknown")] = counts.get(value.get("status", "unknown"), 0) + 1
        mark = value.get("verify", "pending" if "verified_hash" not in value else "agreed")
        verify_counts[mark] = verify_counts.get(mark, 0) + 1
    holds = load_holds()
    print(json.dumps({
        "state": str(STATE_PATH), "counts": counts, "verify": verify_counts,
        "holds": str(HOLDS_PATH),
        "held": len(holds["held"]), "settled": len(holds["settled"]),
        "complete": COMPLETE_PATH.exists(), "complete_marker": str(COMPLETE_PATH),
        "providers": {
            provider: {
                "available": provider_available(provider),
                "slots": PROVIDER_SLOT_COUNTS[provider],
            }
            for provider in PROVIDER_SLOT_COUNTS
        },
    }, ensure_ascii=False, indent=2))
    return 0


_POSTS = [post for post in iter_posts() if post.path.is_relative_to(MATH_POST_ROOT)]


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--dry-run", action="store_true")
    parser.add_argument("--no-commit", action="store_true")
    parser.add_argument("--status", action="store_true")
    args = parser.parse_args()
    if args.status:
        return status()
    if legacy_classifier_running():
        log("legacy dependency classifier is still running; skip this tick")
        return 0
    held = ledger.try_lock()
    if held is None:
        log("link relation ledger is locked (classifier or dashboard); skip this tick")
        return 0
    try:
        RECORDS.clear()
        RECORDS.update(ledger.load())
        return process_once(args.dry_run, commit=not args.no_commit)
    finally:
        held.release()


if __name__ == "__main__":
    raise SystemExit(main())
