#!/usr/bin/env python3
"""Units and the items a stage asks about.

A unit is a KO post and its EN counterpart (or an EN post without one), exactly
as the old classifier groups them, so lids line up with the production ledger.
The links judged are every KO link with a lid, plus the EN links whose lid is
not in the KO post (EN-only occurrences).  An EN link sharing a KO lid is the
KO link's translation and shares its record.

One model call covers one source file: the full source text once, then one
excerpt per distinct cross-article target, then the items.  Same-article
targets need no excerpt — the source is already in the prompt — so the item
just points at the target's line.
"""
from __future__ import annotations

import hashlib
from dataclasses import dataclass, field
from pathlib import Path

import dependency_classifier as dc
import shadow_features as feat
from common import by_permalink, parse_labels  # noqa: E402  (path set by dependency_classifier)

ROOT = dc.ROOT


@dataclass
class Unit:
    key: str
    paths: list[Path]
    texts: dict[Path, str]
    links: dict[Path, list] = field(default_factory=dict)   # source → judged links
    waiting: bool = False                                    # some link still lacks a lid

    @property
    def fingerprint(self) -> str:
        return hashlib.sha256("\0".join(self.texts[p] for p in self.paths).encode()).hexdigest()

    @property
    def lids(self) -> list[str]:
        return [link.lid for links in self.links.values() for link in links]

    def link(self, lid: str):
        for links in self.links.values():
            for link in links:
                if link.lid == lid:
                    return link
        return None


def unit_hash(key: str) -> str:
    return hashlib.sha1(key.encode()).hexdigest()[:16]


def load_unit(paths: list[Path]) -> Unit:
    texts = {p: p.read_text(encoding="utf-8") for p in paths}
    unit = Unit(key=dc.unit_key(paths), paths=paths, texts=texts)
    ko_all = dc.ko_lids(paths, texts)
    for path in paths:
        own = []
        for link in dc.extract_links(path, texts[path], records={}):
            if link.lid is None:
                unit.waiting = True
                continue
            if dc.awaits_ko(link, texts[path], ko_all):
                continue
            own.append(link)
        if own:
            unit.links[path] = own
    return unit


def all_units() -> list[list[Path]]:
    return dc.iter_units()


def _target_post(link) -> Path | None:
    if link.target.startswith("#"):
        return link.source
    base = link.target.split("#", 1)[0].split("?", 1)[0]
    post = by_permalink(base, dc._POSTS)
    return post.path if post else None


def build_calls(unit: Unit, only: set[str] | None = None) -> list[dict]:
    """One call spec per source file: text, target excerpts, items, features."""
    calls = []
    for path, links in unit.links.items():
        chosen = [link for link in links if only is None or link.lid in only]
        if not chosen:
            continue
        text = unit.texts[path]
        doc = parse_labels(text)
        pair_count: dict[Path | None, int] = {}
        for link in links:
            pair_count[_target_post(link)] = pair_count.get(_target_post(link), 0) + 1
        targets: dict[str, dict] = {}
        target_keys: dict[str, str] = {}
        items, features = [], {}
        for link in chosen:
            tpath = _target_post(link)
            f = feat.link_features(link, text, doc, source_path=path, target_path=tpath,
                                   pair_size=pair_count.get(tpath, 1),
                                   article_links=len(links))
            features[link.lid] = f
            item = {"id": link.lid,
                    "link": text[link.start:link.ial_end or link.end],
                    "line": link.line, "target": link.target}
            if f["same_page"]:
                item["target_key"] = "same-article"
                if f["target_line"]:
                    item["target_line"] = f["target_line"]
            else:
                key = target_keys.get(link.target)
                if key is None:
                    key = f"T{len(target_keys) + 1}"
                    target_keys[link.target] = key
                    _, excerpt = dc.target_context(link, False)
                    targets[key] = {"target": link.target, "excerpt": excerpt}
                item["target_key"] = key
            items.append(item)
        calls.append({
            "source": path, "source_rel": str(path.relative_to(ROOT)),
            "lang": path.parent.name, "text": text,
            "targets": targets, "items": items, "features": features,
        })
    return calls
