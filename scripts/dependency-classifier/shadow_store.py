#!/usr/bin/env python3
"""Where the shadow pipeline keeps things, and how it writes them.

Two places, on purpose:

* ``_data/link_relations_next.yml`` (in the repo) — the shadow ledger.  Only
  finished records, in the production format ``{relation, reviewed}``, keyed by
  lid.  Jekyll reads it as a fallback for lids the production ledger has no
  value for (``_plugins/graph_data.rb :: relation_of``), and it replaces the
  production ledger when the shadow run is promoted.
* ``~/.local/state/dependency-shadow/`` (never in the repo) — everything else:
  per-unit stage results with the models' traces, the human and audit queues,
  digest jobs, and the precedent and pending-issue files.  The repo is public
  and some judged posts are private (the local-only research stream), and
  traces, precedents, and pending issues quote the source text verbatim, so
  none of them may live in the repo.

Every write is an atomic replace.  ``LOCK_PATH`` serialises the cron tick and
the dashboard's writes to this state.
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
LEDGER_PATH = ROOT / "_data" / "link_relations_next.yml"
STATE_DIR = Path(os.environ.get(
    "DEPENDENCY_SHADOW_STATE_DIR", str(Path.home() / ".local" / "state" / "dependency-shadow")))
STATE_PATH = STATE_DIR / "state.json"
UNITS_DIR = STATE_DIR / "units"
QUEUE_PATH = STATE_DIR / "queue.json"
PILOT_DIR = STATE_DIR / "pilot"
PRECEDENTS_DIR = STATE_DIR / "precedents"
PENDING_DIR = STATE_DIR / "pending"
HISTORY_DIR = STATE_DIR / "history"
STATS_PATH = STATE_DIR / "precedent-stats.json"
CALIBRATION_PATH = STATE_DIR / "calibration.json"
LOCK_PATH = Path("/tmp/dependency-shadow.lock")

LEDGER_HEADER = """\
# 섀도 원장 — 의존성 링크 전면 재판정의 확정 결과 (2026-10-17 결정).
# 형식은 _data/link_relations.yml 과 같다: 키는 본문 링크 IAL 의 data-lid,
# 값은 {relation: required|weak|forward, reviewed: true}.
# 세 모델 만장일치이거나 사람이 판정한 링크만 여기에 온다.
# Jekyll 은 프로덕션 원장에 값이 없는 lid 에만 이 파일을 쓴다 (_plugins/graph_data.rb).
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


def try_lock() -> Lock | None:
    handle = open(LOCK_PATH, "w")
    try:
        fcntl.flock(handle, fcntl.LOCK_EX | fcntl.LOCK_NB)
    except OSError:
        handle.close()
        return None
    return Lock(handle)


def lock(timeout: float) -> Lock | None:
    deadline = time.monotonic() + timeout
    while True:
        taken = try_lock()
        if taken is not None or time.monotonic() >= deadline:
            return taken
        time.sleep(0.5)


# ── shadow ledger ─────────────────────────────────────────────────────────

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
