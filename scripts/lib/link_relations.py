#!/usr/bin/env python3
"""The link-relation ledger: `_data/link_relations.yml`.

Markdown carries only `{: data-lid="k7m2x" }` after an internal link.  What that
occurrence means for the dependency graph lives here, keyed by the lid:

    "k7m2x": {relation: required, reviewed: true}

A KO link and the EN link that translates it share one lid, so they share one
record.  A lid without a record is waiting for the classifier.

The dependency classifier and the dashboard's ruling buttons are the only
writers.  Both hold `LOCK_PATH` for the whole read-modify-write: the classifier
for its entire tick (a tick finds the lock taken and skips), the dashboard for a
single ruling.  Jekyll (`_plugins/graph_data.rb`) reads the file as
`site.data["link_relations"]`.
"""
from __future__ import annotations

import fcntl
import os
import tempfile
import time
from dataclasses import dataclass
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parents[2]
PATH = ROOT / "_data" / "link_relations.yml"
LOCK_PATH = Path("/tmp/link-relations.lock")

# `requires-review` marks a link whose two model verdicts disagreed; it waits for
# a human and counts as unclassified in the graph.
RELATIONS = ("required", "weak", "forward")
REVIEW_RELATION = "requires-review"
VALUES = RELATIONS + (REVIEW_RELATION,)

HEADER = """\
# 링크 관계 원장. 키는 본문 링크 IAL 의 data-lid, 값은 그 출현의 의존 관계다.
# relation: required | weak | forward | requires-review
# reviewed: true 이면 사람이 판정을 마쳤다 (없으면 false).
# 같은 lid 를 가진 KO 링크와 EN 링크가 이 레코드 하나를 공유한다.
# 쓰는 곳은 의존성 분류기와 대시보드 판정 버튼뿐이다 (scripts/lib/link_relations.py).
"""


@dataclass(frozen=True)
class Record:
    relation: str
    reviewed: bool = False


def load(path: Path | None = None) -> dict[str, Record]:
    path = PATH if path is None else path
    try:
        raw = yaml.safe_load(path.read_text(encoding="utf-8")) or {}
    except FileNotFoundError:
        return {}
    records = {}
    for lid, value in raw.items():
        if not isinstance(value, dict) or value.get("relation") not in VALUES:
            raise ValueError(f"{path}: bad record for {lid!r}: {value!r}")
        records[str(lid)] = Record(value["relation"], bool(value.get("reviewed", False)))
    return records


def dump(records: dict[str, Record]) -> str:
    lines = [HEADER]
    for lid in sorted(records):
        rec = records[lid]
        fields = f"relation: {rec.relation}" + (", reviewed: true" if rec.reviewed else "")
        # 키는 항상 따옴표로 감싼다 — 36진수 5자는 정수(`01234`)나 불리언(`false`)으로
        # 읽힐 수 있다.
        lines.append(f'"{lid}": {{{fields}}}\n')
    return "".join(lines)


def save(records: dict[str, Record], path: Path | None = None) -> None:
    """Replace the file atomically.  The caller holds the lock."""
    path = PATH if path is None else path
    text = dump(records)
    fd, tmp = tempfile.mkstemp(prefix=".link_relations.", suffix=".tmp", dir=path.parent)
    try:
        with os.fdopen(fd, "w", encoding="utf-8") as handle:
            handle.write(text)
        os.chmod(tmp, 0o664)
        os.replace(tmp, path)
    finally:
        try:
            os.unlink(tmp)
        except FileNotFoundError:
            pass


class Lock:
    """An acquired ledger lock.  Release by `release()` or as a context manager."""

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
    """Take the ledger lock without waiting, or return None."""
    handle = open(LOCK_PATH, "w")
    try:
        fcntl.flock(handle, fcntl.LOCK_EX | fcntl.LOCK_NB)
    except OSError:
        handle.close()
        return None
    return Lock(handle)


def lock(timeout: float) -> Lock | None:
    """Wait up to `timeout` seconds for the ledger lock."""
    deadline = time.monotonic() + timeout
    while True:
        taken = try_lock()
        if taken is not None or time.monotonic() >= deadline:
            return taken
        time.sleep(0.5)
