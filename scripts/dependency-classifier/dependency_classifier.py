#!/usr/bin/env python3
"""Classify internal Markdown links as required, weak, or forward.

One cron tick handles one logical KO/EN article pair.  Each language is judged
independently, but both files are written and committed together.  Antigravity
accepts only self-declared HIGH decisions; MEDIUM decisions are reviewed by a
separate Claude Opus pass with wider context.  A single ambiguous decision
blocks the whole pair so an article is not repeatedly rewritten.

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
from typing import Iterable

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT / "scripts" / "postnav"))
sys.path.insert(0, str(ROOT / ".agents" / "hooks"))
sys.path.insert(0, str(ROOT / "scripts" / "lib"))

from common import by_permalink, en_counterpart, find_box, iter_posts, parse_labels, protected_spans  # noqa: E402
import md_lint  # noqa: E402
from blog_file_lock import FileLockSet, try_acquire_file_locks  # noqa: E402
from cron_commit import commit_outputs, dirty_paths  # noqa: E402

STATE_DIR = Path.home() / ".local" / "state"
STATE_PATH = STATE_DIR / "dependency-classifier.json"
STATE_LOCK_PATH = Path("/tmp/dependency-classifier-state.lock")
LEGACY_LOCK_PATH = Path("/tmp/dependency-classifier.lock")
SLOT_PATHS = tuple(Path(f"/tmp/dependency-classifier-slot-{i}.lock") for i in range(4))

AGY_BIN = os.environ.get("DEPENDENCY_AGY_BIN", str(Path.home() / ".gemini/bin/agy"))
AGY_MODEL = os.environ.get("DEPENDENCY_AGY_MODEL", "gemini-3.8-flash-high")
CLAUDE_BIN = os.environ.get("DEPENDENCY_CLAUDE_BIN", str(Path.home() / ".local/bin/claude"))
CLAUDE_MODEL = os.environ.get("DEPENDENCY_CLAUDE_MODEL", "opus")
CODEX_BIN = os.environ.get(
    "DEPENDENCY_CODEX_BIN", str(Path.home() / ".npm-global/bin/codex-multi-auth-codex"))
CODEX_MODEL = os.environ.get("DEPENDENCY_CODEX_MODEL", "gpt-5.6-sol")
CODEX_EFFORT = os.environ.get("DEPENDENCY_CODEX_EFFORT", "high")
MODEL_TIMEOUT = int(os.environ.get("DEPENDENCY_MODEL_TIMEOUT", "900"))
BLOCK_SEC = 24 * 3600
CHUNK_SIZE = 10
RELATIONS = {"required", "weak", "forward"}

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
    relation: str | None = None


def log(message: str) -> None:
    print(f"[{datetime.now():%Y-%m-%d %H:%M:%S}] {message}", flush=True)


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
    """Cap expensive classifier model calls at four concurrent processes."""
    for path in SLOT_PATHS:
        lock_fh = open(path, "w")
        try:
            fcntl.flock(lock_fh, fcntl.LOCK_EX | fcntl.LOCK_NB)
            return lock_fh
        except OSError:
            lock_fh.close()
    return None


def overlaps(pos: int, spans: Iterable[tuple[int, int]]) -> bool:
    return any(a <= pos < b for a, b in spans)


def internal_target(target: str) -> bool:
    clean = target.strip()
    return clean.startswith("#") or clean.startswith("/ko/") or clean.startswith("/en/")


def extract_links(path: Path, text: str) -> list[Link]:
    """Find unclassified post links outside code/raw/math/inline-code spans."""
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
        if ial and RELATION_RE.search(ial.group(1)):
            continue
        ordinal += 1
        stable = f"{path.relative_to(ROOT)}:{ordinal}:{target}:{label}"
        result.append(Link(
            ident=hashlib.sha1(stable.encode()).hexdigest()[:12], source=path,
            start=match.start(), end=match.end(), markup=markup, label=label,
            target=target, ial_start=ial_start, ial_end=ial_end,
        ))
    return result


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


def target_context(link: Link, wide: bool) -> tuple[str, str]:
    source_text = link.source.read_text(encoding="utf-8")
    target = link.target
    anchor = target.split("#", 1)[1] if "#" in target else ""
    if target.startswith("#"):
        post_path = link.source
    else:
        base = target.split("#", 1)[0].split("?", 1)[0]
        post = by_permalink(base, _POSTS)
        post_path = post.path if post else link.source
    text = post_path.read_text(encoding="utf-8")
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


def prompt_items(links: list[Link], wide: bool) -> list[dict]:
    items = []
    for link in links:
        src, dst = target_context(link, wide)
        items.append({
            "id": link.ident,
            "language": "en" if "/en/" in str(link.source) else "ko",
            "link": link.markup,
            "target": link.target,
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

ITEMS:
"""


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


def call_antigravity(items: list[dict], *, review: bool = False) -> dict:
    prompt = (REVIEW_PROMPT if review else FIRST_PROMPT) + json.dumps(items, ensure_ascii=False)
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


def call_opus(items: list[dict], *, review: bool = True) -> dict:
    prompt = (REVIEW_PROMPT if review else FIRST_PROMPT) + json.dumps(items, ensure_ascii=False)
    env = {**os.environ, "CLAUDE_CODE_DISABLE_ADVISOR_TOOL": "1"}
    proc = subprocess.run(
        [CLAUDE_BIN, "-p", "--model", CLAUDE_MODEL, "--output-format", "text"],
        input="[cron]\n\n" + prompt, cwd=str(ROOT), env=env,
        capture_output=True, text=True, timeout=MODEL_TIMEOUT,
    )
    if proc.returncode:
        raise RuntimeError(f"Claude Opus exited {proc.returncode}: {proc.stderr.strip()[:400]}")
    return parse_json_value(proc.stdout)


def codex_output_schema(items: list[dict], *, review: bool) -> dict:
    properties = {
        "id": {"type": "string", "enum": [str(item["id"]) for item in items]},
        "relation": {
            "type": "string",
            "enum": sorted(RELATIONS | ({"ambiguous"} if review else set())),
        },
        "reason": {"type": "string"},
    }
    required = ["id", "relation", "reason"]
    if not review:
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


def call_codex(items: list[dict], *, review: bool) -> dict:
    """Use the multi-auth Codex CLI as the final structured-output fallback."""
    prompt = (REVIEW_PROMPT if review else FIRST_PROMPT) + json.dumps(items, ensure_ascii=False)
    with tempfile.TemporaryDirectory(prefix="dependency-codex-") as tmp:
        tmp_path = Path(tmp)
        schema_path = tmp_path / "schema.json"
        output_path = tmp_path / "last-message.json"
        schema_path.write_text(
            json.dumps(codex_output_schema(items, review=review), ensure_ascii=False),
            encoding="utf-8",
        )
        proc = subprocess.run(
            [CODEX_BIN, "exec", "--model", CODEX_MODEL,
             "-c", f'model_reasoning_effort="{CODEX_EFFORT}"',
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


def valid_results(payload: dict, expected: set[str], *, review: bool) -> dict[str, dict]:
    rows = payload.get("items")
    if not isinstance(rows, list):
        return {}
    out = {}
    allowed = RELATIONS | ({"ambiguous"} if review else set())
    for row in rows:
        if not isinstance(row, dict) or row.get("id") not in expected:
            continue
        relation = str(row.get("relation", "")).lower()
        if relation not in allowed:
            continue
        if not review and str(row.get("confidence", "")).lower() not in {"high", "medium"}:
            continue
        out[row["id"]] = row
    return out


def request_complete_results(
    items: list[dict], *, review: bool, stage: str,
    primary_name: str, primary, fallback_name: str, fallback,
    final_fallback_name: str | None = None, final_fallback=None,
) -> dict[str, dict]:
    """Keep valid rows and recover only incomplete IDs within this cron tick."""
    accepted: dict[str, dict] = {}
    pending = items
    last_issue = "incomplete model response"
    attempts = [
        (primary_name, primary),
        (primary_name, primary),
        (fallback_name, fallback),
    ]
    if final_fallback_name is not None and final_fallback is not None:
        attempts.append((final_fallback_name, final_fallback))
    for attempt_index, (model_name, caller) in enumerate(attempts):
        expected = {str(item["id"]) for item in pending}
        try:
            payload = caller(pending)
            accepted.update(valid_results(payload, expected, review=review))
            last_issue = "model omitted or invalidated requested items"
        except Exception as exc:
            # A malformed envelope, timeout, or provider failure is recoverable here.
            # Do not log the exception on a recovered run: the dashboard treats words
            # such as "error" and "failed" in the run log as a real job failure.
            last_issue = f"{type(exc).__name__}: {str(exc)[:240]}"
        pending = [item for item in pending if str(item["id"]) not in accepted]
        if not pending:
            return accepted
        if attempt_index == 0:
            log(f"{stage}: retrying {len(pending)} incomplete item(s) with {model_name}")
        elif attempt_index + 1 < len(attempts):
            next_name = attempts[attempt_index + 1][0]
            log(f"{stage}: falling back for {len(pending)} incomplete item(s) to {next_name}")
    missing = sorted(str(item["id"]) for item in pending)
    raise RuntimeError(
        f"{stage} omitted/invalidated {len(missing)} item(s) after retry and fallback: "
        f"{missing[:4]} ({last_issue})"
    )


def classify(links: list[Link]) -> tuple[dict[str, str], list[dict]]:
    first: dict[str, dict] = {}
    for i in range(0, len(links), CHUNK_SIZE):
        chunk = links[i:i + CHUNK_SIZE]
        values = request_complete_results(
            prompt_items(chunk, False), review=False, stage="first pass",
            primary_name="Antigravity",
            primary=lambda items: call_antigravity(items, review=False),
            fallback_name="Claude Opus",
            fallback=lambda items: call_opus(items, review=False),
            final_fallback_name="Codex",
            final_fallback=lambda items: call_codex(items, review=False),
        )
        first.update(values)
    decisions = {ident: str(row["relation"]).lower() for ident, row in first.items()
                 if str(row["confidence"]).lower() == "high"}
    medium = [link for link in links if str(first[link.ident]["confidence"]).lower() == "medium"]
    log(f"first pass: high={len(decisions)}, medium={len(medium)}")
    ambiguous = []
    for i in range(0, len(medium), CHUNK_SIZE):
        chunk = medium[i:i + CHUNK_SIZE]
        values = request_complete_results(
            prompt_items(chunk, True), review=True, stage="Opus review",
            primary_name="Claude Opus",
            primary=lambda items: call_opus(items, review=True),
            fallback_name="Codex",
            fallback=lambda items: call_codex(items, review=True),
        )
        for ident, row in values.items():
            relation = str(row["relation"]).lower()
            if relation == "ambiguous":
                ambiguous.append({"id": ident, "reason": row.get("reason", "")})
            else:
                decisions[ident] = relation
    if medium:
        log(f"Opus review: decided={len(medium) - len(ambiguous)}, ambiguous={len(ambiguous)}")
    if set(decisions) | {x["id"] for x in ambiguous} != {x.ident for x in links}:
        raise RuntimeError("internal decision accounting mismatch")
    return decisions, ambiguous


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


def select_unit(
    state: dict, updates: dict[str, dict],
) -> tuple[list[Path], dict[Path, str], list[Link], FileLockSet] | None:
    now = time.time()
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
    for paths in units:
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
            if entry.get("hash") == fingerprint and entry.get("status") == "done":
                lease.release()
                continue
            if entry.get("hash") == fingerprint and entry.get("retry_after", 0) > now:
                lease.release()
                continue
            links = [link for p in paths for link in extract_links(p, texts[p])]
            if not links:
                updates[key] = {
                    "status": "done", "hash": fingerprint,
                    "checked_at": int(now), "links": 0,
                }
                lease.release()
                continue
            return paths, texts, links, lease
        except Exception:
            lease.release()
            raise
    return None


def process_once(dry_run: bool = False) -> int:
    state = load_state()
    scan_updates: dict[str, dict] = {}
    selected = select_unit(state, scan_updates)
    merge_unit_states(scan_updates)
    if not selected:
        log("queue empty (or every pending target is locked/dirty/backed off)")
        return 0
    paths, originals, links, lease = selected
    key = unit_key(paths)
    try:
        log(f"selected {key}: {len(links)} unclassified link(s)")
        if dry_run:
            for link in links:
                log(f"dry-run {link.source.relative_to(ROOT)} {link.target}")
            return 0
        fingerprint = sha("\0".join(originals[p] for p in paths))
        try:
            decisions, ambiguous = classify(links)
            if ambiguous:
                merge_unit_states({key: {
                    "status": "ambiguous", "hash": fingerprint,
                    "checked_at": int(time.time()),
                    "retry_after": int(time.time() + BLOCK_SEC), "items": ambiguous,
                }})
                log(f"blocked {key}: {len(ambiguous)} ambiguous decision(s); no files changed")
                return 0
            rels = [str(p.relative_to(ROOT)) for p in paths]
            if dirty_paths(rels, ROOT) or any(
                p.read_text(encoding="utf-8") != originals[p] for p in paths
            ):
                raise RuntimeError("target changed while models were running")
            by_path = {p: [x for x in links if x.source == p] for p in paths}
            rendered = {p: annotate(originals[p], by_path[p], decisions) for p in paths}
            for path in paths:
                introduced = hard_lint(path, rendered[path]) - hard_lint(path, originals[path])
                if introduced:
                    raise RuntimeError(
                        f"annotation introduces md_lint findings in {path}: "
                        f"{sorted(introduced)[:3]}"
                    )
            for path in paths:
                path.write_text(rendered[path], encoding="utf-8")
            committed = commit_outputs(
                "Link Dependencies Classifier", rels,
                f"{paths[0].stem} 링크 {len(links)}건 분류", log=log, repo=ROOT,
            )
            if not committed:
                # The targets were clean before this tick, so restoring them cannot
                # overwrite user work.  Never leave unowned generated edits behind.
                for path in paths:
                    if path.exists() and path.read_text(encoding="utf-8") == rendered[path]:
                        path.write_text(originals[path], encoding="utf-8")
                raise RuntimeError("could not commit worker outputs; restored originals")
            merge_unit_states({key: {
                "status": "done", "hash": sha("\0".join(rendered[p] for p in paths)),
                "checked_at": int(time.time()), "links": len(links),
            }})
            log(f"done {key}: {len(links)} relation tag(s)")
            return 0
        except Exception as exc:
            merge_unit_states({key: {
                "status": "error", "hash": fingerprint,
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
    for value in state.get("units", {}).values():
        counts[value.get("status", "unknown")] = counts.get(value.get("status", "unknown"), 0) + 1
    print(json.dumps({"state": str(STATE_PATH), "counts": counts}, ensure_ascii=False, indent=2))
    return 0


_POSTS = iter_posts()


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--dry-run", action="store_true")
    parser.add_argument("--status", action="store_true")
    args = parser.parse_args()
    if args.status:
        return status()
    if legacy_classifier_running():
        log("legacy dependency classifier is still running; skip this tick")
        return 0
    slot_fh = acquire_slot()
    if slot_fh is None:
        log("four dependency classifiers are already running; skip this tick")
        return 0
    try:
        return process_once(args.dry_run)
    finally:
        slot_fh.close()


if __name__ == "__main__":
    raise SystemExit(main())
