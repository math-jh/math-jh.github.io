#!/usr/bin/env python3
"""What the link-dependency pipeline (linkdep_*.py) reads from the posts.

* The internal links of a Math post (``extract_links``) and the excerpts a model
  is shown around a link and around its target (``source_context``,
  ``target_context``).
* The units the pipeline works on: a KO post with its EN counterpart
  (``iter_units``, ``unit_key``).  An EN link carrying the lid of a KO link in
  the unit is that link's translation and shares its ledger record
  (``awaits_ko``).
* Link identifiers (``mint_lids``).  A post carries only the identifier, in the
  link's IAL; the relation is in the ledger ``_data/link_relations.yml``::

      [label](/ko/math/example){: data-lid="k7m2x" }
      "k7m2x": {relation: required, reviewed: true}

* The quota gate and the per-provider call slots the model calls go through
  (``provider_available``, ``acquire_provider_slot``).

Judging itself is in linkdep_pipeline.py and linkdep_tick.py.
"""
from __future__ import annotations

import fcntl
import hashlib
import importlib.util
import json
import os
import re
import secrets
import subprocess
import sys
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
from blog_file_lock import try_acquire_file_locks  # noqa: E402
import link_relations as ledger  # noqa: E402,F401 — importers reach the ledger as core.ledger
from cron_commit import commit_outputs, dirty_paths  # noqa: E402

# The lid ledger and the lid-pairing state.  The pipeline's own state directory is
# linkdep_store.STATE_DIR.
STATE_DIR = Path.home() / ".local" / "state"

QUOTA_STATE_DIR = Path(os.environ.get(
    "DEPENDENCY_QUOTA_STATE_DIR", str(Path.home() / "Projects" / "hud-display" / "state")))
QUOTA_MAX_STALE_SEC = int(os.environ.get("DEPENDENCY_QUOTA_MAX_STALE_SEC", str(45 * 60)))
QUOTA_LIMIT_5H = float(os.environ.get("DEPENDENCY_QUOTA_LIMIT_5H", "0.70"))
QUOTA_LIMIT_WEEKLY = float(os.environ.get("DEPENDENCY_QUOTA_LIMIT_WEEKLY", "0.90"))
# Codex passed 8/8 simultaneous probes on 2026-09-10; six leaves room for IDE use.
PROVIDER_SLOT_COUNTS = {"Antigravity": 4, "Claude Opus": 4, "Codex": 6}
PROVIDER_SLOT_PATHS = {
    name: tuple(Path(
        f"/tmp/dependency-classifier-{name.lower().replace(' ', '-')}-slot-{i}.lock"
    ) for i in range(count))
    for name, count in PROVIDER_SLOT_COUNTS.items()
}

AGY_BIN = os.environ.get("DEPENDENCY_AGY_BIN", str(Path.home() / ".gemini/bin/agy"))
# No model ID by default, only an effort level: the model is the Antigravity CLI's
# own default.
AGY_MODEL = os.environ.get("DEPENDENCY_AGY_MODEL")
AGY_EFFORT = os.environ.get("DEPENDENCY_AGY_EFFORT") or "medium"
CLAUDE_BIN = os.environ.get("DEPENDENCY_CLAUDE_BIN", str(Path.home() / ".local/bin/claude"))
CLAUDE_MODEL = os.environ.get("DEPENDENCY_CLAUDE_MODEL", "opus")
CODEX_BIN = os.environ.get(
    "DEPENDENCY_CODEX_BIN", str(Path.home() / ".npm-global/bin/codex-multi-auth-codex"))
# No model ID by default, only an effort level: a pinned ID goes stale (on
# 2026-10-19 gpt-5.6-sol was refused on a Free-plan account and answered "Selected
# model is at capacity" for an afternoon).  Left empty, Codex uses the model of
# ~/.codex/config.toml; the variables remain for an emergency pin.
CODEX_MODEL_OVERRIDE = os.environ.get("DEPENDENCY_CODEX_MODEL")
CODEX_EFFORT_OVERRIDE = os.environ.get("DEPENDENCY_CODEX_EFFORT")
CODEX_REVIEW_MODEL = os.environ.get(
    "DEPENDENCY_CODEX_REVIEW_MODEL", CODEX_MODEL_OVERRIDE or "")
CODEX_REVIEW_EFFORT = os.environ.get(
    "DEPENDENCY_CODEX_REVIEW_EFFORT", CODEX_EFFORT_OVERRIDE or "medium")
MODEL_TIMEOUT = int(os.environ.get("DEPENDENCY_MODEL_TIMEOUT", "900"))
BLOCK_SEC = 24 * 3600
NOTIFY_BIN = os.environ.get(
    "DEPENDENCY_NOTIFY_BIN", str(Path.home() / ".local" / "bin" / "notify"))
# 알림을 누르면 바로 판정할 수 있는 자리로 보낸다.
DASHBOARD_URL = os.environ.get(
    "DEPENDENCY_DASHBOARD_URL", "https://preview.math-jh.com/dash/audit")

IAL_RE = re.compile(r'^\{:\s*([^}]*)\}')
LID_RE = re.compile(r'\bdata-lid\s*=\s*["\']([^"\']*)["\']')


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
           url: str = DASHBOARD_URL, digest: bool = False) -> None:
    """Best-effort alert.  A failed notification must not fail the tick.
    ``digest`` defers it to the shim's daily summary (no action needed now)."""
    try:
        proc = subprocess.run(
            [NOTIFY_BIN, "-s", subject, "-b", body, "-g", "blog/worker", "-l", level,
             *(("-u", url) if url else ()), *(("--digest",) if digest else ())],
            check=False, timeout=20, capture_output=True, text=True,
        )
        if proc.returncode:
            log(f"notify rc={proc.returncode}: {proc.stderr.strip()[:300]!r}")
    except Exception as exc:  # noqa: BLE001
        log(f"notify skipped: {exc!r}")


def sha(text: str) -> str:
    return hashlib.sha256(text.encode("utf-8")).hexdigest()


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


def extract_links(path: Path, text: str) -> list[Link]:
    """The post's internal links in source order, outside code/raw/math/inline-code
    spans.  ``lid`` is the ``data-lid`` of the link's IAL, None when it has none."""
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
        ordinal += 1
        stable = f"{path.relative_to(ROOT)}:{ordinal}:{target}:{label}"
        result.append(Link(
            ident=hashlib.sha1(stable.encode()).hexdigest()[:12], source=path,
            start=match.start(), end=match.end(), markup=markup, label=label,
            target=target, ial_start=ial_start, ial_end=ial_end,
            line=text.count("\n", 0, match.start()) + 1, lid=lid,
        ))
    return result


def ko_lids(paths: list[Path], texts: dict[Path, str]) -> set[str]:
    """이 unit 의 KO 쪽에 있는 모든 링크의 lid."""
    return {link.lid for path in paths if path.parent.name == "ko"
            for link in extract_links(path, texts[path]) if link.lid}


def awaits_ko(link: Link, ko_all: set[str]) -> bool:
    """이 EN 링크의 판정이 KO 짝의 몫인가.

    판정의 정본은 KO 다. 같은 lid 를 가진 KO 링크가 이 unit 에 있으면 EN 은 그
    번역이므로 스스로 판정받지 않고, 원장의 같은 레코드를 쓴다. EN 을 따로 물으면
    같은 출현에 다른 값이 붙는다.
    """
    return link.source.parent.name == "en" and bool(link.lid) and link.lid in ko_all


def read_post(path: Path) -> str:
    return path.read_text(encoding="utf-8")


def paragraph_context(text: str, offset: int, radius: int) -> str:
    body_start = 0
    if text.startswith("---\n"):
        end = text.find("\n---\n", 4)
        if end >= 0:
            body_start = end + 5
    chunks = []
    for m in re.finditer(r"\S(?:.*?\S)?(?=\n\s*\n|\s*\Z)", text[body_start:], re.DOTALL):
        chunks.append((body_start + m.start(), body_start + m.end(), m.group(0)))
    idx = next((i for i, (a, b, _) in enumerate(chunks) if a <= offset <= b), None)
    if idx is None:
        # An offset in the blank lines between paragraphs belongs to the one before.
        idx = max((i for i, (a, _b, _t) in enumerate(chunks) if a <= offset), default=0)
    lo, hi = max(0, idx - radius), min(len(chunks), idx + radius + 1)
    return "\n\n".join(c[2] for c in chunks[lo:hi])[:7000]


def target_context(link: Link, wide: bool) -> tuple[str, str]:
    """(excerpt around the link, excerpt of what it points at).  ``wide`` takes
    more of both."""
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
        # from a mere analogy; ``wide`` takes a larger slice.
        context = text[:9000 if wide else 4500]
    src = source_context(source_text, link.start, 2 if wide else 1)
    return src, context[:12000 if wide else 6500]


FOOTNOTE_DEF_RE = re.compile(r"(?m)^\[\^([^\]\s]+)\]:")
FOOTNOTE_REF_RE = re.compile(r"\[\^([^\]\s]+)\](?!:)")


def _footnote_defs(text: str) -> dict[str, tuple[int, int]]:
    """각주 정의 `[^id]: …` 의 (시작, 끝) — 끝은 다음 정의나 들여쓰지 않은 새 문단."""
    starts = [(m.group(1), m.start()) for m in FOOTNOTE_DEF_RE.finditer(text)]
    spans = {}
    for i, (fid, start) in enumerate(starts):
        limit = starts[i + 1][1] if i + 1 < len(starts) else len(text)
        brk = re.search(r"\n\s*\n(?=\S)", text[start:limit])
        spans[fid] = (start, start + brk.start() if brk else limit)
    return spans


def source_context(text: str, offset: int, radius: int) -> str:
    """링크 주변 문단에 각주의 짝을 붙인다.

    각주 정의는 글 끝에 모여 있어서 문단 단위로 자르면 짝이 떨어진다. 링크가
    각주 안에 있으면 그 각주를 다는 본문 문단을, 본문 문단에 각주 표지가 있으면
    그 각주 내용을 덧붙인다.
    """
    src = paragraph_context(text, offset, radius)
    defs = _footnote_defs(text)
    home = next((fid for fid, (a, b) in defs.items() if a <= offset < b), None)
    extra = []
    if home:
        for m in FOOTNOTE_REF_RE.finditer(text):
            if m.group(1) == home and not any(a <= m.start() < b for a, b in defs.values()):
                extra.append(f"[Footnote [^{home}] is attached to this passage]\n\n"
                             + paragraph_context(text, m.start(), radius))
                break
    else:
        for fid in dict.fromkeys(FOOTNOTE_REF_RE.findall(src)):
            if fid in defs:
                a, b = defs[fid]
                note = text[a:b].strip()
                if note not in src:
                    extra.append(note)
    return "\n\n".join([src, *extra])


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


def ask_antigravity(prompt: str) -> dict:
    proc = subprocess.run(
        # `[cron]` 접두사: 세션 리퍼가 agy 대화 db 를 봇 대화로 알아보는 표지.
        [AGY_BIN, "--print", "[cron]\n\n" + prompt,
         *(["--model", AGY_MODEL] if AGY_MODEL else ["--effort", AGY_EFFORT]),
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
        "Link Dependencies", [str(p.relative_to(ROOT)) for p in paths],
        detail, log=log, repo=ROOT,
    )
    if not committed:
        # The targets were clean before this tick, so restoring them cannot
        # overwrite user work.  Never leave unowned generated edits behind.
        for path in paths:
            if path.exists() and path.read_text(encoding="utf-8") == rendered[path]:
                path.write_text(originals[path], encoding="utf-8")
        raise RuntimeError("could not commit worker outputs; restored originals")


LID_LEDGER = Path.home() / ".local" / "state" / "link-ids.txt"
LID_ALPHABET = "0123456789abcdefghijklmnopqrstuvwxyz"
LID_LENGTH = 5
PAIRING_STATE_PATH = STATE_DIR / "link-lid-pairing.json"
PAIRING_MAX_ATTEMPTS = 3
PAIRING_WINDOW = (700, 400)     # 모델에게 보여 줄 링크 앞·뒤 글자 수
SECTION_ANCHOR_GATE = Path(__file__).resolve().parents[2] / "scripts" / "translation" / "section_anchor_gate.py"
IAL_ANY_RE = re.compile(r"\{:[^}\n]*\}")


def loose_links(path: Path, text: str) -> list[Link]:
    """lid 가 없는 링크 — 원장에 판정을 담을 자리가 아직 없다."""
    return [link for link in extract_links(path, text) if link.lid is None]


def twin_path(path: Path) -> Path | None:
    """KO 글이면 EN 짝, EN 글이면 KO 짝. 날짜 접두사는 언어마다 다를 수 있다."""
    m = re.match(r"\d{4}-\d{2}-\d{2}-(.+\.md)$", path.name)
    if not m or path.parent.name not in ("ko", "en"):
        return None
    other = path.parent.parent / ("en" if path.parent.name == "ko" else "ko")
    found = sorted(other.glob(f"????-??-??-{m.group(1)}"))
    return found[0] if found else None


_anchor_gate_module = None


def anchor_gate():
    """번역 파이프라인의 섹션 앵커 대응(section_anchor_gate). 쓸 때 처음 불러온다."""
    global _anchor_gate_module
    if _anchor_gate_module is None:
        spec = importlib.util.spec_from_file_location("section_anchor_gate", SECTION_ANCHOR_GATE)
        assert spec and spec.loader
        module = importlib.util.module_from_spec(spec)
        sys.modules.setdefault("section_anchor_gate", module)
        spec.loader.exec_module(module)
        _anchor_gate_module = module
    return _anchor_gate_module


def h2_slugs(path: Path) -> list[str]:
    gate = anchor_gate()
    return [h.slug for h in gate.extract_headings(path.read_text(encoding="utf-8"))
            if h.level == 2]


def pair_key(target: str, home: Path) -> tuple[str, str | None]:
    """링크 target 의 언어 중립 키 `(경로, 앵커)`. 앵커를 환원하지 못하면 앵커가 None.

    라벨 앵커(`#prop7`)는 언어 불변이라 그대로 쓴다. 섹션 앵커는 번역되므로
    (`#텐서곱` ↔ `#tensor-product`) 대상 글의 H2 목록에서의 위치로 바꾼다. 대상 글의
    KO/EN H2 개수가 다르거나 앵커가 목록에 없으면 위치가 대응을 보장하지 못한다.
    같은 글 안 앵커의 대상 글은 링크가 있는 글 자신이다.
    """
    path, _, frag = target.partition("#")
    path = path.split("?", 1)[0].rstrip("/")
    if path:
        post = by_permalink(path, _POSTS)
        dest = post.path if post else None
        key_path = re.sub(r"^/(?:ko|en)(?=/)", "", path)
    else:
        dest, key_path = home, "@self"
    if not frag or anchor_gate().LABEL_ANCHOR_RE.match(frag):
        return key_path, frag
    other = twin_path(dest) if dest else None
    if other is None:
        return key_path, None
    try:
        mine, theirs = h2_slugs(dest), h2_slugs(other)
    except OSError:
        return key_path, None
    if len(mine) != len(theirs) or frag not in mine:
        return key_path, None
    return key_path, f"§{mine.index(frag)}"


def plan_en_lids(
    en_path: Path, en_text: str, ko_path: Path, ko_text: str,
) -> tuple[list[tuple[Link, str]], list[Link], list[tuple[Link, list[Link]]]]:
    """EN 의 lid 없는 링크를 (KO lid 를 이어받을 것, 새로 받을 것, 모델에 물을 것)으로.

    후보는 KO 출현 중 lid 가 EN 어디에도 없는 것, 그중 같은 대상(경로가 같고 앵커가
    같거나 어느 한쪽이 환원 불가)으로 가는 것이다.
      - 후보가 없으면 그 EN 링크는 KO 의 어느 출현의 번역도 아니다 → 새 lid.
      - EN 링크와 KO 후보가 서로에게 유일한 후보이고 키까지 같으면 그 lid 를 옮긴다.
        문장을 읽지 않고 짝을 짓는 곳은 여기뿐이라 1:1 로 묶어 둔다.
      - 나머지는 같은 대상이 여러 번 나와 순서로만 갈리는 경우다. 번역은 순서를
        바꿀 수 있으므로 위치로 정하지 않고 모델이 문장을 읽어 정한다.
    """
    en_lids = set(LID_RE.findall(en_text))
    loose = loose_links(en_path, en_text)
    open_ko = [k for k in extract_links(ko_path, ko_text) if k.lid and k.lid not in en_lids]
    en_key = {e.start: pair_key(e.target, en_path) for e in loose}
    ko_key = {k.start: pair_key(k.target, ko_path) for k in open_ko}

    def fits(a: tuple[str, str | None], b: tuple[str, str | None]) -> bool:
        return a[0] == b[0] and (a[1] is None or b[1] is None or a[1] == b[1])

    found = {e.start: [k for k in open_ko if fits(en_key[e.start], ko_key[k.start])]
             for e in loose}
    inherit, fresh, ask = [], [], []
    for e in loose:
        mine = found[e.start]
        if not mine:
            fresh.append(e)
            continue
        if len(mine) == 1:
            k = mine[0]
            rivals = [x.start for x in loose if any(c.start == k.start for c in found[x.start])]
            if (en_key[e.start][1] is not None and en_key[e.start] == ko_key[k.start]
                    and rivals == [e.start]):
                inherit.append((e, k.lid))
                continue
        ask.append((e, mine))
    return inherit, fresh, ask


def with_lids(text: str, assign: list[tuple[Link, str]]) -> str:
    """각 링크의 IAL 에 lid 를 단다 (IAL 이 없으면 붙인다). 링크는 이 text 에서 뽑은 것."""
    edits = []
    for link, value in assign:
        if link.ial_start is None:
            edits.append((link.end, link.end, f'{{: data-lid="{value}" }}'))
        else:
            ial = text[link.ial_start:link.ial_end]
            edits.append((link.ial_start, link.ial_end,
                          ial[:2] + f' data-lid="{value}"' + ial[2:]))
    for start, end, replacement in sorted(edits, reverse=True):
        text = text[:start] + replacement + text[end:]
    return text


def duplicate_lids(text: str) -> set[str]:
    values = LID_RE.findall(text)
    return {v for v in values if values.count(v) > 1}


def lid_drawer() -> Callable[[], str]:
    """새 lid 를 뽑는 함수. `현재 코퍼스 ∪ 발급 대장` 과 대조해 겹치면 다시 뽑는다."""
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

    return draw


def record_minted(values: list[str]) -> None:
    if not values:
        return
    LID_LEDGER.parent.mkdir(parents=True, exist_ok=True)
    with LID_LEDGER.open("a", encoding="utf-8") as handle:
        handle.write("".join(value + "\n" for value in values))


def mint_lids(*, commit: bool) -> bool:
    """lid 없는 링크에 식별자를 준다. 판정보다 **먼저** 돈다. 모델을 불렀으면 True.

    관계는 lid 를 키로 원장에 적히므로 lid 없는 링크는 판정을 담을 곳이 없다.
    KO 링크는 새 값을 받는다. EN 링크가 KO 출현의 번역이면 그 lid 를 이어받아야
    두 링크가 한 레코드를 공유한다. 새 값을 주면 같은 출현이 따로 판정되고, 그 값
    차이는 에러를 내지 않는다. 번역이 lid 를 옮기지 못한 EN 링크(번역 당시 대상 글이
    없어 링크로 잡히지 않았다가 대상 글이 번역된 경우, 번역이 lid 를 흘린 경우)가
    여기로 온다. `plan_en_lids` 가 나눈 대로 이어받거나 새로 받고, 순서로만 갈리는
    것은 `pair_with_model` 이 모델에게 물어 정한다(틱당 한 글). 답이 나오기 전까지
    그 링크는 lid 없이 기다린다.

    KO 를 먼저 발급하고 EN 후보는 그 결과로 계산한다. KO 짝에 lid 없는 링크가
    남아 있으면(dirty·잠김으로 이번에 못 받았으면) 그 EN 글은 다음 틱으로 미룬다.
    후보를 못 본 채 새 값을 주면 같은 출현이 갈린다.

    값은 36진수 5자 난수이고, `현재 코퍼스 ∪ 발급 대장` 과 대조해 다시 뽑으므로
    유일성은 확률이 아니라 검사로 보장된다. 지워진 링크의 id 가 풀려서 다른
    링크에 재배정되지 않도록 대장은 한 번 발급한 값을 계속 들고 있는다.
    """
    scope = ROOT / "_posts" / "Math"
    targets = sorted(p for p in scope.rglob("*.md") if p.parent.name in ("ko", "en"))
    texts = {p: p.read_text(encoding="utf-8") for p in targets}
    loose = {p: loose_links(p, texts[p]) for p in targets}
    if not any(loose.values()):
        return False

    def clean(path: Path) -> bool:
        return not dirty_paths([str(path.relative_to(ROOT))], ROOT)

    draw, minted, inherited = lid_drawer(), [], 0

    def fresh_lid() -> str:
        minted.append(draw())
        return minted[-1]

    rendered: dict[Path, str] = {}
    for path in targets:
        if path.parent.name == "ko" and loose[path] and clean(path):
            rendered[path] = with_lids(texts[path], [(x, fresh_lid()) for x in loose[path]])
    waiting = []
    for path in targets:
        if path.parent.name != "en" or not loose[path] or not clean(path):
            continue
        ko = twin_path(path)
        if ko is None:
            assign = [(x, fresh_lid()) for x in loose[path]]
        else:
            ko_text = rendered.get(ko) or texts.get(ko) or ko.read_text(encoding="utf-8")
            if loose_links(ko, ko_text):
                continue
            inherit, fresh, ask = plan_en_lids(path, texts[path], ko, ko_text)
            if ask:
                waiting.append(path)
            assign = inherit + [(x, fresh_lid()) for x in fresh]
            inherited += len(inherit)
        if not assign:
            continue
        text = with_lids(texts[path], assign)
        if duplicate_lids(text):
            log(f"lid: {path.relative_to(ROOT)} — 이어받은 lid 가 겹친다, 쓰지 않음")
            continue
        rendered[path] = text

    if rendered:
        lease = try_acquire_file_locks(list(rendered))
        if lease is None:
            log("lid: 대상 글이 잠겨 있다 — 다음 틱에")
            return False
        try:
            written = [v for v in minted if any(f'"{v}"' in rendered[p] for p in rendered)]
            record_minted(written)
            detail = f"링크 식별자 {len(written)}건 발급"
            if inherited:
                detail += f", KO 짝 lid {inherited}건 이어받음"
            # 추적되는 글과 로컬 전용(untracked GW) 글을 한 번에 넘기면 커밋 경로가 갈려
            # 둘 다 실패한다 — 나눠서 게시한다.
            local = [p for p in rendered if is_local_only_untracked_unit([p])]
            for group in ([p for p in rendered if p not in local], local):
                if group:
                    publish(group, texts, rendered, commit=commit, detail=detail)
        finally:
            lease.release()
        log(f"lid: {len(written)} minted, {inherited} inherited from KO "
            f"across {len(rendered)} post(s)")
    return pair_with_model(waiting, draw, commit=commit)


PAIRING_PROMPT = """You are matching internal links between a Korean mathematics article and its English translation.

Every link occurrence in the Korean article carries a permanent identifier: the `data-lid="xxxxx"` in the attribute list right after the link. The English translation should carry the same identifier on the link that renders that occurrence. The English links listed below have none. For each one, decide from the sentences which Korean occurrence it renders. The same target is often linked several times in one article, translation may reorder sentences, and a translation may also contain a link the Korean article does not have.

In each excerpt the link in question is the one immediately after its tag: ⟦e3⟧ for an English link, ⟦<lid>⟧ for a Korean candidate.

{groups}

Answer with one JSON object and nothing else:
{"assignments": [{"en": "e1", "lid": "abcde"}], "unmatched": [{"en": "e2", "why": "..."}], "undecided": [{"en": "e3", "why": "..."}]}

- assignments: the English link renders that Korean occurrence. Use only a lid listed for that English link, and each lid at most once. If the English link merges several Korean occurrences, give the one whose sentence it renders.
- unmatched: none of the listed Korean occurrences is rendered by this English link; the translation added it.
- undecided: you cannot tell. A wrong match is worse than an undecided one, which is asked again later.
Put every listed English link in exactly one of the three lists. Write each "why" in Korean."""


def link_window(text: str, link: Link, tag: str) -> str:
    """링크 앞뒤 몇백 자를 잘라, 묻는 링크 바로 앞에 태그를 넣는다."""
    end = link.ial_end or link.end
    a = max(0, link.start - PAIRING_WINDOW[0])
    b = min(len(text), end + PAIRING_WINDOW[1])
    return (("…" if a else "") + text[a:link.start] + f"⟦{tag}⟧" + text[link.start:b]
            + ("…" if b < len(text) else ""))


def pairing_prompt(en_text: str, ko_text: str, ask: list[tuple[Link, list[Link]]]) -> str:
    blocks, shown = [], {}
    for i, (link, found) in enumerate(ask, 1):
        blocks.append(f"English link e{i}: {link.markup}\n"
                      f"Korean candidates for e{i}: {', '.join(k.lid for k in found)}\n"
                      f"Excerpt:\n{link_window(en_text, link, f'e{i}')}")
        for k in found:
            shown.setdefault(k.lid, k)
    for lid, k in shown.items():
        blocks.append(f"Korean candidate {lid}\nExcerpt:\n{link_window(ko_text, k, lid)}")
    return PAIRING_PROMPT.replace("{groups}", "\n\n".join(blocks))


def check_pairing(
    answer: dict, ask: list[tuple[Link, list[Link]]],
) -> tuple[list[tuple[Link, str]], list[Link], list[str]]:
    """모델의 답에서 규칙을 지킨 것만 (이어받을 것, 새로 받을 것, 버린 사유)로."""
    asked = {f"e{i}": (link, {k.lid for k in found}) for i, (link, found) in enumerate(ask, 1)}
    inherit, fresh, notes = [], [], []
    answered, used = set(), set()

    def tag_of(item: object) -> str:
        raw = item.get("en") if isinstance(item, dict) else None
        return str(raw or "").strip().strip("[]⟦⟧ ")

    for item in answer.get("assignments") or []:
        tag, lid = tag_of(item), str(item.get("lid") or "").strip()
        if tag not in asked or tag in answered:
            notes.append(f"{tag}: 묻지 않았거나 두 번 답한 링크")
        elif lid not in asked[tag][1]:
            notes.append(f"{tag}: 후보 밖의 lid {lid}")
        elif lid in used:
            notes.append(f"{tag}: lid {lid} 를 두 번 씀")
        else:
            answered.add(tag)
            used.add(lid)
            inherit.append((asked[tag][0], lid))
    for item in answer.get("unmatched") or []:
        tag = tag_of(item)
        if tag not in asked or tag in answered:
            notes.append(f"{tag}: 묻지 않았거나 두 번 답한 링크")
        else:
            answered.add(tag)
            fresh.append(asked[tag][0])
            notes.append(f"{tag}: KO 짝 없음 — {str(item.get('why') or '')[:120]}")
    for item in answer.get("undecided") or []:
        notes.append(f"{tag_of(item)}: 미정 — {str(item.get('why') or '')[:120]}")
    return inherit, fresh, notes


def load_pairing_state() -> dict:
    try:
        value = json.loads(PAIRING_STATE_PATH.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError):
        return {}
    return value if isinstance(value, dict) else {}


def save_pairing_state(state: dict) -> None:
    PAIRING_STATE_PATH.parent.mkdir(parents=True, exist_ok=True)
    tmp = PAIRING_STATE_PATH.with_suffix(".tmp")
    tmp.write_text(json.dumps(state, ensure_ascii=False, indent=1), encoding="utf-8")
    os.replace(tmp, PAIRING_STATE_PATH)


def pair_with_model(queue: list[Path], draw: Callable[[], str], *, commit: bool) -> bool:
    """순서로만 갈리는 EN 링크의 KO 짝을 모델에게 묻는다. 한 틱에 한 글. 불렀으면 True.

    모델은 판단만 하고 파일은 여기서 쓴다. 후보는 같은 대상으로 가는 짝 없는 KO
    출현으로만 제시하고, 답의 lid 는 그 링크의 후보 안이어야 하며 한 번씩만 쓸 수 있다.
    새 lid 는 모델이 "이 링크의 KO 출현이 없다"(unmatched)고 답한 링크만 받는다.
    미정·규칙 위반·호출 실패·쿼터는 아무것도 쓰지 않고 그 링크를 lid 없이 남긴다.
    lid 없는 EN 링크는 판정을 기다릴 뿐 막는 것이 없지만, 잘못 지은 짝이나 성급한
    새 값은 KO 와 다른 판정을 조용히 만든다.

    같은 내용(IAL 을 뺀 KO+EN)에 PAIRING_MAX_ATTEMPTS 번 물어도 남으면 알리고 하루
    쉰다. 내용이 바뀌면 횟수는 처음부터 센다.
    """
    if not queue:
        return False
    state = load_pairing_state()
    now = time.time()
    for en_path in queue:
        ko_path = twin_path(en_path)
        if ko_path is None:
            continue
        key = str(en_path.relative_to(ROOT))
        lease = try_acquire_file_locks([ko_path, en_path])
        if lease is None:
            continue
        try:
            if dirty_paths([str(p.relative_to(ROOT)) for p in (ko_path, en_path)], ROOT):
                continue
            ko_text = ko_path.read_text(encoding="utf-8")
            en_text = en_path.read_text(encoding="utf-8")
            digest = sha(IAL_ANY_RE.sub("", ko_text) + "\0" + IAL_ANY_RE.sub("", en_text))
            entry = state.get(key, {})
            if entry.get("digest") != digest:
                entry = {"digest": digest}
            if entry.get("retry_after", 0) > now or loose_links(ko_path, ko_text):
                continue
            _inherit, _fresh, ask = plan_en_lids(en_path, en_text, ko_path, ko_text)
            if not ask:
                continue
            if not provider_available("Antigravity"):
                log("lid pairing: Antigravity quota closed — next tick")
                return False
            log(f"lid pairing: {key} — asking the model for {len(ask)} KO twin(s)")
            slot = acquire_provider_slot("Antigravity")
            try:
                answer = ask_antigravity(pairing_prompt(en_text, ko_text, ask))
                inherit, fresh, notes = check_pairing(answer, ask)
            except Exception as exc:  # noqa: BLE001 — 실패는 이 글을 미룰 뿐이다
                inherit, fresh, notes = [], [], [f"호출 실패: {str(exc)[:300]}"]
            finally:
                slot.close()
            values = [draw() for _ in fresh]
            assign = inherit + list(zip(fresh, values))
            if assign:
                text = with_lids(en_text, assign)
                try:
                    if duplicate_lids(text):
                        raise RuntimeError(f"lid 중복 {sorted(duplicate_lids(text))}")
                    record_minted(values)
                    publish([en_path], {en_path: en_text}, {en_path: text}, commit=commit,
                            detail=f"링크 식별자: KO 짝 lid {len(inherit)}건 이어받음(모델 판단)"
                                   + (f", EN 전용 {len(fresh)}건 발급" if fresh else ""))
                except RuntimeError as exc:
                    notes.append(f"쓰기 거절: {exc}")
                    inherit, fresh, assign = [], [], []
            for note in notes:
                log(f"lid pairing: {key} — {note}")
            left = len(ask) - len(assign)
            if left:
                entry["attempts"] = entry.get("attempts", 0) + 1
                if entry["attempts"] >= PAIRING_MAX_ATTEMPTS:
                    entry.update(attempts=0, retry_after=int(now + BLOCK_SEC))
                    notify("링크 lid 짝 미정",
                           f"{key}\nEN 링크 {left}개의 KO 짝을 {PAIRING_MAX_ATTEMPTS}번 물어도 "
                           "정하지 못했다. 하루 뒤 다시 묻는다.\n" + "\n".join(notes[:5]),
                           url="")
                state[key] = entry
            else:
                state.pop(key, None)
            save_pairing_state(state)
            log(f"lid pairing: {key} — inherited {len(inherit)}, EN-only {len(fresh)}, left {left}")
            return True
        finally:
            lease.release()
    return False


_POSTS = [post for post in iter_posts() if post.path.is_relative_to(MATH_POST_ROOT)]
