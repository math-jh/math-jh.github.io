#!/usr/bin/env python3
"""Precedents (P-####) and pending issues (Q-####): one Markdown file each, an
INDEX.md of one line per live entry, all in Korean, in the gitignored
``scripts/dependency-classifier/book/`` (they quote private posts; the repo is
public).

A precedent is a human ruling on an issue.  One issue has at most one live
precedent: a new ruling on an issue that already has one amends or supersedes
it (the digest worker checks this before anything is written; see
shadow_digest).  A pending issue is an issue a model raised in Step 4 and a
human has not ruled on yet; two pending issues found to be the same are merged
into one before any precedent exists.

Front matter carries the slow, human-meaningful fields only.  Counts that move
on every application (how often a precedent was applied, audit results under
it) live in precedent-stats.json, so applying a precedent never rewrites its
file.  Every rewrite of a file first copies the old version into history/.
"""
from __future__ import annotations

import re
import time
from dataclasses import dataclass
from pathlib import Path

import yaml

import shadow_store as store

P_STATUSES = ("active", "promoted", "superseded", "revoked")
Q_STATUSES = ("open", "merged", "ruled", "dismissed")
QUESTIONS = ("preview", "need", "provided")
INDEX_CAP = 60
CONSOLIDATE_AT = 50
DESCRIPTION_MAX = 80
FRONT_RE = re.compile(r"\A---\n(.*?)\n---\n?(.*)\Z", re.S)
_depth = 0
_handle = None


class book_lock:
    """Re-entrant within a process: a mutation may call another mutation."""

    def __enter__(self):
        global _depth, _handle
        if _depth == 0:
            import fcntl
            _handle = open(store.BOOK_LOCK_PATH, "w")
            fcntl.flock(_handle, fcntl.LOCK_EX)
        _depth += 1
        return self

    def __exit__(self, *_exc):
        global _depth, _handle
        _depth -= 1
        if _depth == 0 and _handle is not None:
            _handle.close()
            _handle = None


@dataclass
class Entry:
    id: str
    meta: dict
    body: str
    path: Path

    @property
    def status(self) -> str:
        return str(self.meta.get("status", ""))

    @property
    def description(self) -> str:
        return str(self.meta.get("description", ""))


def _dir(kind: str) -> Path:
    return store.PRECEDENTS_DIR if kind == "P" else store.PENDING_DIR


def parse(path: Path) -> Entry:
    text = path.read_text(encoding="utf-8")
    m = FRONT_RE.match(text)
    meta = yaml.safe_load(m.group(1)) if m else {}
    return Entry(id=str(meta.get("id", path.stem)), meta=meta or {},
                 body=(m.group(2) if m else text).strip() + "\n", path=path)


def entries(kind: str) -> list[Entry]:
    folder = _dir(kind)
    if not folder.exists():
        return []
    return [parse(p) for p in sorted(folder.glob(f"{kind}-*.md"))]


def get(entry_id: str) -> Entry | None:
    path = _dir(entry_id[0]) / f"{entry_id}.md"
    return parse(path) if path.exists() else None


def live(kind: str) -> list[Entry]:
    want = "active" if kind == "P" else "open"
    return [e for e in entries(kind) if e.status == want]


def next_id(kind: str) -> str:
    numbers = [int(e.id.split("-")[1]) for e in entries(kind) if re.match(rf"{kind}-\d+$", e.id)]
    return f"{kind}-{(max(numbers) + 1) if numbers else 1:04d}"


def render(meta: dict, body: str) -> str:
    front = yaml.safe_dump(meta, allow_unicode=True, sort_keys=False, width=1000).strip()
    return f"---\n{front}\n---\n\n{body.strip()}\n"


def write(entry_id: str, meta: dict, body: str) -> Entry:
    with book_lock():
        return _write(entry_id, meta, body)


def _write(entry_id: str, meta: dict, body: str) -> Entry:
    path = _dir(entry_id[0]) / f"{entry_id}.md"
    if path.exists():
        store.HISTORY_DIR.mkdir(parents=True, exist_ok=True)
        stamp = time.strftime("%Y%m%d-%H%M%S")
        (store.HISTORY_DIR / f"{entry_id}.{stamp}.md").write_text(
            path.read_text(encoding="utf-8"), encoding="utf-8")
    meta = {"id": entry_id, **{k: v for k, v in meta.items() if k != "id"}}
    if len(str(meta.get("description", ""))) > DESCRIPTION_MAX:
        meta["description"] = str(meta["description"])[:DESCRIPTION_MAX]
    store.write_text(path, render(meta, body))
    rebuild_index(entry_id[0])
    return parse(path)


def rebuild_index(kind: str) -> None:
    folder = _dir(kind)
    title = "유효 판례" if kind == "P" else "열린 판례 대기"
    lines = [f"# {title}\n"]
    for e in live(kind):
        question = e.meta.get("question", "")
        lines.append(f"- [{e.id}]({e.id}.md) — {e.description}" + (f" ({question})" if question else ""))
    store.write_text(folder / "INDEX.md", "\n".join(lines) + "\n")


def index_lines(kind: str, question: str | None = None, limit: int | None = None) -> list[str]:
    rows = [e for e in live(kind) if question is None or e.meta.get("question") == question]
    if limit is not None:
        rows = rows[:limit]
    return [f"{e.id} — {e.description} (question: {e.meta.get('question', '?')})" for e in rows]


# ── pending issues ────────────────────────────────────────────────────────

def raise_issue(*, question: str, statement: str, description: str, raised_by: str,
                lid: str) -> str:
    with book_lock():
        entry_id = next_id("Q")
        meta = {"status": "open", "description": description, "question": question,
                "raised_by": raised_by, "created": time.strftime("%Y-%m-%d"), "links": [lid]}
        body = f"## 쟁점 진술\n{statement.strip()}\n\n## 모델별 의견\n"
        write(entry_id, meta, body)
        return entry_id


def open_for(lid: str, raised_by: str | None = None) -> Entry | None:
    """An open pending issue that already carries this link (by that stage, if given)."""
    for e in live("Q"):
        if lid in (e.meta.get("links") or []) and (raised_by is None or e.meta.get("raised_by") == raised_by):
            return e
    return None


def attach(entry_id: str, lid: str) -> None:
    with book_lock():
        e = get(entry_id)
        if e is None or e.status != "open":
            return
        links = list(e.meta.get("links") or [])
        if lid not in links:
            links.append(lid)
            write(entry_id, {**e.meta, "links": links}, e.body)


def detach(entry_id: str, lid: str) -> None:
    with book_lock():
        e = get(entry_id)
        if e is None:
            return
        links = [x for x in e.meta.get("links") or [] if x != lid]
        write(entry_id, {**e.meta, "links": links}, e.body)


def add_opinion(entry_id: str, line: str) -> None:
    with book_lock():
        e = get(entry_id)
        if e is None:
            return
        body = e.body.rstrip() + f"\n- {line.strip()}\n"
        write(entry_id, e.meta, body)


def restate(entry_id: str, statement: str | None, description: str | None) -> None:
    with book_lock():
        e = get(entry_id)
        if e is None:
            return
        body = e.body
        if statement:
            body = re.sub(r"(## 쟁점 진술\n)(.*?)(\n## |\Z)",
                          lambda m: m.group(1) + statement.strip() + "\n" + m.group(3),
                          e.body, count=1, flags=re.S)
        meta = {**e.meta}
        if description:
            meta["description"] = description
        write(entry_id, meta, body)


def set_status(entry_id: str, status: str, **extra) -> None:
    with book_lock():
        e = get(entry_id)
        if e is None:
            return
        write(entry_id, {**e.meta, "status": status, **extra}, e.body)


def merge(source_id: str, into_id: str) -> None:
    """Fold one open pending issue into another: links move, the source closes."""
    with book_lock():
        src, dst = get(source_id), get(into_id)
        if src is None or dst is None or source_id == into_id:
            return
        links = list(dst.meta.get("links") or [])
        for lid in src.meta.get("links") or []:
            if lid not in links:
                links.append(lid)
        write(into_id, {**dst.meta, "links": links}, dst.body)
        write(source_id, {**src.meta, "status": "merged", "merged_into": into_id}, src.body)


def load_stats() -> dict:
    return store.read_json(store.STATS_PATH, {})


def _bump(entry_id: str, change) -> None:
    with book_lock():
        stats = load_stats()
        row = stats.setdefault(entry_id, {"applied": [], "audits": 0, "audit_errors": 0})
        change(row)
        store.write_json(store.STATS_PATH, stats)


def bump_applied(entry_id: str, lid: str) -> None:
    _bump(entry_id, lambda row: row["applied"].append(lid) if lid not in row["applied"] else None)


def bump_audit(entry_id: str, error: bool) -> None:
    def change(row):
        row["audits"] += 1
        row["audit_errors"] += int(error)
    _bump(entry_id, change)
