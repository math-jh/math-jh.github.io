#!/usr/bin/env python3
"""The link-relation ledger: `_data/link_relations.yml`.

Markdown carries only `{: data-lid="k7m2x" }` after an internal link.  What that
occurrence means for the dependency graph lives here, keyed by the lid:

    "k7m2x": {relation: required, reviewed: true}

A KO link and the EN link that translates it share one lid, so they share one
record.  A record is written once three models agree on the link or a human has
ruled on it; a lid without a record is unclassified.

This module is the file format.  The writers are the judging pipeline
(`scripts/dependency-classifier/linkdep_*.py`) and the dashboard's rulings
(`scripts/dashboard/linkdeps_api.py`); both write through
`linkdep_store.save_ledger` under that module's state lock.  Jekyll
(`_plugins/graph_data.rb`) reads the file as `site.data["link_relations"]`.
"""
from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parents[2]
PATH = ROOT / "_data" / "link_relations.yml"

RELATIONS = ("required", "weak", "forward")

HEADER = """\
# 링크 관계 원장. 키는 본문 링크 IAL 의 data-lid, 값은 그 출현의 의존 관계다:
# {relation: required|weak|forward, reviewed: true}.
# 세 모델 만장일치이거나 사람이 판정한 링크만 여기에 온다. 레코드가 없는 lid 는 미분류다.
# 같은 lid 를 가진 KO 링크와 EN 링크가 이 레코드 하나를 공유한다.
# 쓰는 곳은 scripts/dependency-classifier/linkdep_*.py 와 대시보드뿐이다.
"""


@dataclass(frozen=True)
class Record:
    relation: str
    reviewed: bool = False


def load(path: Path | None = None) -> dict[str, Record]:
    path = PATH if path is None else path
    try:
        # libyaml 로더가 있으면 쓴다 — 순수 파이썬 로더는 수천 줄 원장에 1초 넘게 걸린다.
        loader = getattr(yaml, "CSafeLoader", yaml.SafeLoader)
        raw = yaml.load(path.read_text(encoding="utf-8"), Loader=loader) or {}
    except FileNotFoundError:
        return {}
    records = {}
    for lid, value in raw.items():
        if not isinstance(value, dict) or value.get("relation") not in RELATIONS:
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
