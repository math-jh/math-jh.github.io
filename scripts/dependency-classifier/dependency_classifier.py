#!/usr/bin/env python3
"""Classify internal Markdown links as required, weak, or forward.

One cron tick handles one logical KO/EN article pair.  Each language is judged
independently and the pair is persisted together.  Tracked posts are committed;
untracked posts under the explicitly local-only Gromov-Witten stream are updated
in place.

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

Disagreement is not resolved automatically.  When the verifier returns a
different relation, or ambiguous, the relation tag is **removed** from the file
and the link is held in ``dependency-classifier-holds.json``: the first pass
skips held links, so nothing reclassifies it, and the dashboard's link-audit
panel lists it with its file and line for a human ruling.  Checking the item off
there confirms the user's own tag and settles the link permanently.  Every hold
is announced through the notify shim as it is recorded.

The inline representation is Kramdown IAL syntax::

    [label](/ko/math/example){: data-relation="required" }

State and logs live outside the repository under ~/.local/state.
"""
from __future__ import annotations

import argparse
import fcntl
import hashlib
import json
import os
import re
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
from cron_commit import commit_outputs, dirty_paths  # noqa: E402

STATE_DIR = Path.home() / ".local" / "state"
STATE_PATH = STATE_DIR / "dependency-classifier.json"
HOLDS_PATH = STATE_DIR / "dependency-classifier-holds.json"
HOLDS_LOCK_PATH = Path("/tmp/dependency-classifier-holds.lock")
COMPLETE_PATH = STATE_DIR / "dependency-classifier.complete"
STATE_LOCK_PATH = Path("/tmp/dependency-classifier-state.lock")
LEGACY_LOCK_PATH = Path("/tmp/dependency-classifier.lock")
WORKER_SLOT_PATHS = tuple(Path(f"/tmp/dependency-classifier-slot-{i}.lock") for i in range(6))

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
RELATIONS = {"required", "weak", "forward"}
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

IAL_RE = re.compile(r'^\{:\s*([^}]*)\}')
RELATION_RE = re.compile(r'\bdata-relation\s*=\s*["\'](required|weak|forward)["\']')


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
    relation: str | None = None

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


def notify(subject: str, body: str, level: str = "active") -> None:
    """Best-effort alert.  A failed notification must not fail the tick."""
    try:
        proc = subprocess.run(
            [NOTIFY_BIN, "-s", subject, "-b", body, "-g", "blog", "-l", level],
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


def acquire_slot():
    """Cap the one-off backlog at six concurrent article workers."""
    for path in WORKER_SLOT_PATHS:
        lock_fh = open(path, "w")
        try:
            fcntl.flock(lock_fh, fcntl.LOCK_EX | fcntl.LOCK_NB)
            return lock_fh
        except OSError:
            lock_fh.close()
    return None


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


def extract_links(path: Path, text: str, *, tagged: bool = False) -> list[Link]:
    """Find post links outside code/raw/math/inline-code spans.

    ``tagged`` selects which side of the relation tag is returned: the default
    yields the links still waiting for a relation, and ``True`` yields the ones
    that already carry one, with ``relation`` filled in.  The ordinal behind a
    link's ident counts every candidate in the file either way, so an ident names
    the same link whether or not its tag is currently present.
    """
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
        found = RELATION_RE.search(ial.group(1)) if ial else None
        ordinal += 1
        if bool(found) != tagged:
            continue
        stable = f"{path.relative_to(ROOT)}:{ordinal}:{target}:{label}"
        result.append(Link(
            ident=hashlib.sha1(stable.encode()).hexdigest()[:12], source=path,
            start=match.start(), end=match.end(), markup=markup, label=label,
            target=target, ial_start=ial_start, ial_end=ial_end,
            line=text.count("\n", 0, match.start()) + 1,
            relation=found.group(1) if found else None,
        ))
    return result


_TEXT_OVERRIDE: dict[Path, str] = {}


def read_post(path: Path) -> str:
    """Article text as the current pass should see it.

    The verification pass registers a tag-stripped copy of the unit here so the
    excerpts it hands the model carry no relation attribute to anchor on.
    """
    override = _TEXT_OVERRIDE.get(path)
    return path.read_text(encoding="utf-8") if override is None else override


def strip_relations(text: str, links: list[Link]) -> str:
    """Drop the data-relation attribute from the IAL of each given link."""
    edits = []
    for link in links:
        if link.ial_start is None or link.ial_end is None:
            continue
        ial = text[link.ial_start:link.ial_end]
        inner = RELATION_RE.sub("", ial[2:-1]).strip()
        edits.append((link.ial_start, link.ial_end, f"{{: {inner} }}" if inner else ""))
    for start, end, replacement in sorted(edits, reverse=True):
        text = text[:start] + replacement + text[end:]
    return text


def paragraph_context(text: str, offset: int, radius: int) -> str:
    body_start = 0
    if text.startswith("---\n"):
        end = text.find("\n---\n", 4)
        if end >= 0:
            body_start = end + 5
    chunks = []
    for m in re.finditer(r"\S(?:.*?\S)?(?=\n\s*\n|\Z)", text[body_start:], re.DOTALL):
        chunks.append((body_start + m.start(), body_start + m.end(), m.group(0)))
    idx = next((i for i, (a, b, _) in enumerate(chunks) if a <= offset <= b), 0)
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


FIRST_PROMPT = """You classify semantic relations of internal links in a mathematics blog.
Return JSON only: {"items":[{"id":"...","relation":"required|weak|forward","confidence":"high|medium","reason":"short"}]}.

Definitions are about the source article as a learning unit:
- required: understanding the linked target is genuinely needed before the source passage/article. This includes a cited proof or construction whose substance the source actually reuses.
- weak: helpful background, analogy, comparison, optional example, attribution, terminology, or a reference that is not a prerequisite.
- forward: the source is self-contained and says the target will later extend, develop, or revisit the present idea.

Classify meaning, not wording or link direction. A link may look like an analogy yet still be required if the source imports the target's proof idea. Conversely, a formal citation may be weak. Same-page anchors must also be classified.

In particular, do not mark a link required merely because the source uses the target's vocabulary. If the source has already established a fact independently and the link only names or recasts it in more advanced language (for example, calling an already described inclusion a "full subcategory"), classify it as weak. Use required only when a reader must know or import the target's definition, theorem, proof, or construction to follow the source's reasoning or subsequent development. Apply this counterfactual test: if removing the linked terminology and parenthetical citation leaves the mathematical argument understandable and complete, the link is weak.

Confidence rule is deliberately strict: HIGH only when the supplied context makes exactly one class clear. If there is any plausible doubt, missing context, mixed role, or interpretive choice, output MEDIUM. Never use HIGH merely because a phrase matches a familiar pattern. Do not use tools and do not alter files.

ITEMS:
"""

REVIEW_PROMPT = """You are the independent final reviewer for ambiguous dependency-link classifications in a mathematics blog. You have wider excerpts than the first model.
Return JSON only: {"items":[{"id":"...","relation":"required|weak|forward|ambiguous","reason":"short"}]}.

Use these exact meanings: required = target knowledge/substance is needed before the source; weak = useful but optional background/analogy/citation/terminology; forward = source is self-contained and target is a later expansion. Judge semantic use, not surface phrasing. A definition link is weak when it merely gives an advanced name or reformulation to a fact already established independently, such as calling an already described inclusion a "full subcategory". It is required only when the source's reasoning or later development actually needs the target's definition, theorem, proof, or construction. Apply the counterfactual test: if removing the linked terminology and citation leaves the mathematical argument understandable and complete, choose weak. Choose ambiguous if the excerpts still do not justify one class. Do not use tools and do not alter files.

Each item states its context_scope. "excerpt" means you see passages around the link. "full-article" means source_context and target_context are the complete articles, truncated only if extremely long: there is no wider context to wait for, so decide on the evidence given and reserve ambiguous for links whose role is genuinely undecidable rather than merely unstated.

ITEMS:
"""

VERIFY_PROMPT = """You classify semantic relations of internal links in a mathematics blog. Your classification is an independent second opinion: another model has already judged these links, you are deliberately not shown its verdict, and your answer is compared against it. Judge the links on the excerpts alone.
Return JSON only: {"items":[{"id":"...","relation":"required|weak|forward|ambiguous","reason":"short"}]}.

Use these exact meanings: required = target knowledge/substance is needed before the source; weak = useful but optional background/analogy/citation/terminology; forward = source is self-contained and target is a later expansion. Judge semantic use, not surface phrasing. A definition link is weak when it merely gives an advanced name or reformulation to a fact already established independently, such as calling an already described inclusion a "full subcategory". It is required only when the source's reasoning or later development actually needs the target's definition, theorem, proof, or construction. Apply the counterfactual test: if removing the linked terminology and citation leaves the mathematical argument understandable and complete, choose weak. Choose ambiguous only when the excerpts leave the link's role genuinely undecidable. Do not use tools and do not alter files.

ITEMS:
"""

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


def annotate(text: str, links: list[Link], decisions: dict[str, str]) -> str:
    edits = []
    for link in links:
        relation = decisions[link.ident]
        if link.ial_start is not None and link.ial_end is not None:
            old = text[link.ial_start:link.ial_end]
            replacement = old[:-1].rstrip() + f' data-relation="{relation}" }}'
            edits.append((link.ial_start, link.ial_end, replacement))
        else:
            edits.append((link.end, link.end, f'{{: data-relation="{relation}" }}'))
    for start, end, replacement in sorted(edits, reverse=True):
        text = text[:start] + replacement + text[end:]
    return text


def hard_lint(path: Path, text: str) -> set[str]:
    return {p for p in md_lint.collect_problems(str(path), text, "", {})
            if not p.startswith(md_lint.SOFT)}


def unit_key(paths: list[Path]) -> str:
    return "+".join(str(p.relative_to(ROOT)) for p in paths)


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
    """Take the first unit with work, and say which of the two stages it is in.

    Classifying comes first: a unit is verified only once no link in it is
    waiting for a relation.  Links parked for a human ruling are invisible to
    both stages, so a disputed link neither reclassifies nor re-disputes.
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
            fingerprint = sha("\0".join(texts[p] for p in paths))
            entry = state.get("units", {}).get(key, {})
            at_judged_content = entry.get("hash") == fingerprint
            if at_judged_content and entry.get("retry_after", 0) > now:
                lease.release()
                continue
            links = [link for p in paths for link in extract_links(p, texts[p])
                     if link.ident not in parked]
            if links:
                if at_judged_content and entry.get("status") == "exhausted":
                    # An exhausted unit spent all MAX_ROUNDS rounds without a
                    # verdict.  It comes back only when the files change, which
                    # also resets the round counter, so a newly added link
                    # reopens it.
                    lease.release()
                    continue
                return "first", paths, texts, links, lease
            if entry.get("verified_hash") == fingerprint:
                lease.release()
                continue
            tagged = [p_link for p in paths
                      for p_link in extract_links(p, texts[p], tagged=True)
                      if p_link.ident not in parked]
            if not tagged:
                updates[key] = {
                    "status": "done", "hash": fingerprint,
                    "verified_hash": fingerprint,
                    "checked_at": int(now), "links": 0,
                }
                lease.release()
                continue
            decided_by = entry.get("decided_by", {}) if at_judged_content else {}
            chains = {verifier_chain(decided_by.get(link.ident)) for link in tagged}
            if not all(any(provider_available(p) for p in chain) for chain in chains):
                # A cross-model verifier has no stand-in.  Leave the unit for a
                # tick where its quota is open instead of waiting on a slot.
                lease.release()
                continue
            return "verify", paths, texts, tagged, lease
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
            texts = [p.read_text(encoding="utf-8") for p in paths]
        except OSError:
            continue
        if entry.get("hash") == sha("\0".join(texts)):
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
        if any(link.ident not in parked
               for p in paths for link in extract_links(p, texts[p])):
            return False
        entry = state.get("units", {}).get(key, {})
        if entry.get("verified_hash") != sha("\0".join(texts[p] for p in paths)):
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


def publish(
    paths: list[Path], originals: dict[Path, str], rendered: dict[Path, str],
    *, detail: str, commit: bool,
) -> None:
    """Write the rewritten unit, and own the result in Git or not at all."""
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
    rendered = {p: annotate(originals[p], [x for x in links if x.source == p], decisions)
                for p in paths}
    publish(paths, originals, rendered, commit=commit,
            detail=f"{paths[0].stem} 링크 {len(links)}건 분류")
    merge_unit_states({key: {
        "status": "done", "hash": sha("\0".join(rendered[p] for p in paths)),
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
    _TEXT_OVERRIDE.update(
        {p: strip_relations(originals[p], [x for x in links if x.source == p]) for p in paths})
    try:
        verdicts = verify(links, decided_by)
    finally:
        _TEXT_OVERRIDE.clear()
    disputed = [(link, str(verdicts[link.ident]["relation"]).lower()) for link in links
                if str(verdicts[link.ident]["relation"]).lower() != link.relation]
    if not disputed:
        merge_unit_states({key: {**cleared(entry), "verified_hash": fingerprint,
                                 "verified_at": int(time.time()), "verify": "agreed"}})
        log(f"verified {key}: {len(links)} relation(s) confirmed")
        return 0
    guard_unchanged(paths, originals)
    rendered = {p: strip_relations(originals[p], [x for x, _ in disputed if x.source == p])
                for p in paths}
    publish(paths, originals, rendered, commit=commit,
            detail=f"{paths[0].stem} 링크 {len(disputed)}건 재검토 보류")
    now = int(time.time())
    holds = {}
    lines = []
    for link, relation in disputed:
        row = verdicts[link.ident]
        verifier = row.get("provider", "")
        holds[link.ident] = {
            "path": str(link.source.relative_to(ROOT)), "line": link.line,
            "label": link.label, "target": link.target, "markup": link.markup,
            "old": link.relation, "new": relation,
            "reason": str(row.get("reason", ""))[:600],
            "decided_by": decided_by.get(link.ident, ""), "verifier": verifier,
            "unit": key, "at": now,
        }
        lines.append(f"{link.where()} {link.relation}→{relation} [{verifier}] {link.brief()}")
    merge_holds(holds)
    settled_hash = sha("\0".join(rendered[p] for p in paths))
    merge_unit_states({key: {
        **cleared(entry), "hash": settled_hash, "verified_hash": settled_hash,
        "verified_at": now, "verify": "disputed", "checked_at": now,
    }})
    for line in lines:
        log("disputed " + line)
    log(f"held {key}: {len(disputed)} link(s) lost their tag pending a ruling")
    notify(
        f"[dependency] 링크 {len(disputed)}건 재검토 불일치",
        f"{paths[0].stem}\n" + "\n".join(lines[:8])
        + (f"\n… 외 {len(lines) - 8}건" if len(lines) > 8 else "")
        + "\n\n대시보드 #audit 의 링크 감사에서 판정할 것.",
    )
    return 0


def process_once(dry_run: bool = False, *, commit: bool = True) -> int:
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
        fingerprint = sha("\0".join(originals[p] for p in paths))
        entry = state.get("units", {}).get(key, {})
        runner = run_first_pass if stage == "first" else run_verify_pass
        try:
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
    slot_fh = acquire_slot()
    if slot_fh is None:
        log("six dependency classifiers are already running; skip this tick")
        return 0
    try:
        return process_once(args.dry_run, commit=not args.no_commit)
    finally:
        slot_fh.close()


if __name__ == "__main__":
    raise SystemExit(main())
