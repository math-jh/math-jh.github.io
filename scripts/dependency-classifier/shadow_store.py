#!/usr/bin/env python3
"""Where the pipeline keeps things, and how it writes them.

Three places, on purpose:

* ``_data/link_relations.yml`` (in the repo) — the ledger.  Only finished
  records ``{relation, reviewed: true}``, keyed by lid.  Jekyll reads it as
  ``site.data["link_relations"]`` (``_plugins/graph_data.rb :: relation_of``); a
  lid without a record is unclassified on the site.
* ``scripts/dependency-classifier/book/`` (in the repo, gitignored) — the
  precedent and pending-issue files, which the human reads and edits.
* ``~/.local/state/dependency-shadow/`` (never in the repo) — everything else:
  per-unit stage results with the models' traces, the human and audit queues,
  digest jobs, precedent statistics, the calibration.
  The repo is public and some judged posts are private (the local-only research
  stream).  Traces, precedents, and pending issues quote the source text
  verbatim, so none of them may be committed: the book folder is in .gitignore
  and the rest never enters the repo.

Every write is an atomic replace.  Three locks:
* ``TICK_LOCK_PATH`` — held for a whole tick (and by the pilot), so ticks never
  overlap.  Model calls happen under it, so nothing else waits on it.
* ``LOCK_PATH`` — held only around a read-modify-write of the queue, the
  ledger, or a unit record, by the tick and by the dashboard alike.
* ``BOOK_LOCK_PATH`` — held around a read-modify-write of a precedent or
  pending-issue file (shadow_book).
"""
from __future__ import annotations

import fcntl
import json
import os
import sys
import tempfile
import time
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "lib"))
import link_relations as ledger  # noqa: E402

ROOT = ledger.ROOT
LEDGER_REL = "_data/link_relations.yml"
LEDGER_PATH = ROOT / LEDGER_REL
STATE_DIR = Path(os.environ.get(
    "DEPENDENCY_SHADOW_STATE_DIR", str(Path.home() / ".local" / "state" / "dependency-shadow")))
STATE_PATH = STATE_DIR / "state.json"
UNITS_DIR = STATE_DIR / "units"
QUEUE_PATH = STATE_DIR / "queue.json"
PILOT_DIR = STATE_DIR / "pilot"
# Precedents and pending issues are files the human reads and edits, so they live in
# the repo (synced to the user's devices) — but in a gitignored folder, because
# they quote private posts and the repo is public.
BOOK_DIR = Path(os.environ.get(
    "DEPENDENCY_SHADOW_BOOK_DIR", str(ROOT / "scripts" / "dependency-classifier" / "book")))
PRECEDENTS_DIR = BOOK_DIR / "precedents"
PENDING_DIR = BOOK_DIR / "pending"
HISTORY_DIR = BOOK_DIR / "history"
STATS_PATH = STATE_DIR / "precedent-stats.json"
CALIBRATION_PATH = STATE_DIR / "calibration.json"
LOCK_PATH = Path("/tmp/dependency-shadow.lock")
TICK_LOCK_PATH = Path("/tmp/dependency-shadow-tick.lock")
BOOK_LOCK_PATH = Path("/tmp/dependency-shadow-book.lock")

LEDGER_HEADER = """\
# 링크 관계 원장. 키는 본문 링크 IAL 의 data-lid, 값은 그 출현의 의존 관계다:
# {relation: required|weak|forward, reviewed: true}.
# 세 모델 만장일치이거나 사람이 판정한 링크만 여기에 온다. 레코드가 없는 lid 는 미분류다.
# 같은 lid 를 가진 KO 링크와 EN 링크가 이 레코드 하나를 공유한다.
# 쓰는 곳은 scripts/dependency-classifier/shadow_*.py 와 대시보드뿐이다.
"""


def write_json(path: Path, value) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    fd, tmp = tempfile.mkstemp(prefix=f".{path.name}.", suffix=".tmp", dir=path.parent)
    try:
        with os.fdopen(fd, "w", encoding="utf-8") as fh:
            fh.write(json.dumps(value, ensure_ascii=False, indent=1) + "\n")
        os.replace(tmp, path)
    finally:
        try:
            os.unlink(tmp)
        except FileNotFoundError:
            pass


def write_text(path: Path, text: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    fd, tmp = tempfile.mkstemp(prefix=f".{path.name}.", suffix=".tmp", dir=path.parent)
    try:
        with os.fdopen(fd, "w", encoding="utf-8") as fh:
            fh.write(text)
        os.replace(tmp, path)
    finally:
        try:
            os.unlink(tmp)
        except FileNotFoundError:
            pass


def read_json(path: Path, default):
    try:
        value = json.loads(path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError):
        return default
    return value if isinstance(value, type(default)) else default


class Lock:
    def __init__(self, handle) -> None:
        self._handle = handle

    def release(self) -> None:
        if self._handle is not None:
            self._handle.close()
            self._handle = None

    def __enter__(self) -> "Lock":
        return self

    def __exit__(self, *_exc: object) -> None:
        self.release()


def _try(path: Path) -> Lock | None:
    handle = open(path, "w")
    try:
        fcntl.flock(handle, fcntl.LOCK_EX | fcntl.LOCK_NB)
    except OSError:
        handle.close()
        return None
    return Lock(handle)


def try_lock() -> Lock | None:
    return _try(LOCK_PATH)


def try_tick_lock() -> Lock | None:
    return _try(TICK_LOCK_PATH)


def lock(timeout: float) -> Lock | None:
    deadline = time.monotonic() + timeout
    while True:
        taken = try_lock()
        if taken is not None or time.monotonic() >= deadline:
            return taken
        time.sleep(0.5)


# ── ledger ────────────────────────────────────────────────────────────────

def load_ledger() -> dict[str, ledger.Record]:
    return ledger.load(LEDGER_PATH)


def save_ledger(records: dict[str, ledger.Record]) -> None:
    text = ledger.dump(records).replace(ledger.HEADER, LEDGER_HEADER, 1)
    write_text(LEDGER_PATH, text)
    os.chmod(LEDGER_PATH, 0o664)


# ── state ─────────────────────────────────────────────────────────────────

def load_state() -> dict:
    state = read_json(STATE_PATH, {})
    state.setdefault("units", {})
    return state


def save_state(state: dict) -> None:
    write_json(STATE_PATH, state)


def unit_path(unit_hash: str) -> Path:
    return UNITS_DIR / f"{unit_hash}.json"


def load_unit_record(unit_hash: str) -> dict:
    return read_json(unit_path(unit_hash), {})


def save_unit_record(unit_hash: str, record: dict) -> None:
    write_json(unit_path(unit_hash), record)


def load_queue() -> dict:
    queue = read_json(QUEUE_PATH, {})
    for key in ("human", "audit", "settled"):
        queue.setdefault(key, {})
    for key in ("digest", "drafts", "recheck"):
        queue.setdefault(key, [])
    return queue


def save_queue(queue: dict) -> None:
    write_json(QUEUE_PATH, queue)


def human_decided(lid: str, rec: dict, queue: dict) -> bool:
    """Whether the human has the say on this link: a ruling (or a reopened one waiting
    for it), or an audit, whether it overturned the unanimous value or confirmed it.
    Rechecks leave these links alone — a model never reopens a human decision."""
    if (rec.get("final") or {}).get("by") in ("human", "audit"):
        return True
    return (queue["settled"].get(lid) or {}).get("how") == "audit"


def merge_unit_record(unit_hash: str, mine: dict, lids: list[str]) -> dict:
    """Write this round's links into the latest copy, keeping what others wrote since.

    The tick holds a unit record in memory for minutes while models answer; the
    dashboard may meanwhile write a human ruling into another link of the same
    unit.  Only the round's links and the round bookkeeping come from ``mine``.
    The caller holds LOCK_PATH.
    """
    fresh = load_unit_record(unit_hash)
    links = fresh.setdefault("links", {})
    for lid in lids:
        if lid in mine.get("links", {}):
            links[lid] = mine["links"][lid]
    for key in ("unit", "round", "round_no", "usage"):
        if key in mine:
            fresh[key] = mine[key]
    save_unit_record(unit_hash, fresh)
    return fresh
