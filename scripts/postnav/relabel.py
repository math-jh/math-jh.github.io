#!/usr/bin/env python3
"""relabel — 라벨 번호 shift + 재라벨링 cascade (글 내부·en 짝·inbound 전파).

사용:
  relabel.py shift '<글지정>' --from 18 --by 2 [--apply] [--allow-dangling]

동작: ko 글의 번호 ≥ from 인 모든 박스를 by만큼 밀고(전역 공유 카운터),
같은 매핑을 (1) 글 내부 라벨 정의 줄 (2) 글 내부 참조 링크 (3) 단독형 증명 귀속
(4) en 짝 파일 (5) inbound 인용 전체에 단일 패스로 전파한다. inbound 범위는
`_posts`·`_pages`의 마크다운 인용과 `_data/*.yml`의 `url:` 앵커까지다.
기본은 dry-run diff. --apply 시에만 실제 쓰기.

--apply는 cron 워커(번역 :15/:45, 용어 추출 :00/:30)의 lock을 그대로 잡고 그 안에서
읽기·변환·쓰기를 한 번에 끝낸다. 워커가 쥐고 있으면 놓을 때까지 기다리고(--lock-wait,
기본 600초), 쓰기 전 원본을 /tmp에 백업해 복구 명령을 출력한다. git 상태는 보지
않는다 — 커밋 체크포인트는 요구하지 않는다.

삽입: shift로 번호 자리를 비운 뒤 새 박스를 삽입한다.
삭제: ① 지울 박스를 가리키는 인용을 먼저 재조준하거나 지운다 ② 박스를 삭제한다
③ 음수 --by로 당긴다. ①을 건너뛰면 DANGLING 게이트가 --apply를 막는다. 삭제된
번호를 가리키던 앵커는 shift 후 **다른 박스로 조용히 재배선**되는데, 텍스트 번호와
앵커가 서로 일치하는 상태라 md_lint도 잡지 못하기 때문이다 (깨진 링크가 아니라
엉뚱한 정리를 가리키는 멀쩡해 보이는 링크가 된다).

en 짝의 라벨 구조가 ko와 다르면(번역 밀림) en 파일 자체는 번역 워커의 재생성에
맡기고 건드리지 않되, en permalink를 가리키는 외부 참조는 재생성 결과(=ko의 번호)에
맞춰 미리 갱신한다. 여기서 안 고치면 영영 고칠 기회가 없다.

자동 치환하지 않고 REVIEW로만 보고: 링크 없는 맨텍스트 언급, 명시형 {#id}의
id 자체(표시 번호는 shift), 텍스트↔앵커 불일치 등 판단이 필요한 것 전부.
"""

from __future__ import annotations

import argparse
import contextlib
import difflib
import fcntl
import os
import re
import sys
import tempfile
import time
from dataclasses import dataclass, field
from datetime import datetime
from pathlib import Path

from common import (
    CITATION_UNIT_RE, EXTRA_CANON, KIND_PREFIX, NUMBERED_ALT, PREFIX_KIND, ROOT,
    TEXT_LABEL_RE, en_counterpart, in_spans, iter_posts, parse_labels, protected_spans,
)
from find_post import resolve_one, fail

REVIEW: list[str] = []
DANGLING: list[str] = []
DANGLING_ANCHORS: set[str] = set()   # --allow-dangling 시 사후 게이트에서 제외할 앵커
TALLY: dict[tuple[str, str], int] = {}   # (파일, 변경 종류) → 건수 (변경 내역 보고용)
TALLY_KINDS = ("라벨 정의 줄", "증명 귀속", "글 내부 참조", "inbound 인용", "url 앵커")


def tally(rel: str, kind: str) -> None:
    TALLY[(rel, kind)] = TALLY.get((rel, kind), 0) + 1

# _posts 밖에서 글 앵커를 들고 있는 곳: _pages 마크다운, _data yml의 url 값.
EXTRA_MD_DIRS = ("_pages",)
DATA_DIR = "_data"

# 같은 파일을 쓰는 cron 워커들의 lock (그들이 쓰는 방식·경로 그대로 잡는다).
# 워커가 쥐고 있으면 거절하지 않고 놓을 때까지 기다린다 — 하루 종일 도는 워커 때문에
# 도구를 못 쓰게 되면 안 되기 때문. RELABEL_LOCK_DIR은 테스트용 우회로.
LOCK_DIR = Path(os.environ.get("RELABEL_LOCK_DIR", tempfile.gettempdir()))
WORKER_LOCKS = (
    ("translate-worker.lock", "pid", "translate_worker (번역, 매시 :15/:45)"),
    ("term-extract-worker.lock", "flock", "term_extract_worker (용어 추출, 매시 :00/:30)"),
    ("extract-terms.lock", "pid", "extract_terms (terms.yml 갱신)"),
)

# yml `url: /ko/math/cat/slug#prop6` 형태의 앵커.
DATA_URL_RE = re.compile(
    r"(?P<path>/[A-Za-z0-9_/\-]+)#(?P<aword>[A-Za-z][\w\-]*?)(?P<anum>\d+)(?![\w\-])"
)

# `<종류> <번호>` 꼴인데 파서가 번호를 못 읽은 라벨 (어휘표 밖 선두 토큰).
LOOKS_NUMBERED_RE = re.compile(r"^[^\s(){}]+[ \t]+\d+(?:[ \t]|$|\()")

# 종류 단어의 ko↔en 짝 — kinds 밖 어휘(extra_canon)까지.
CANON_PAIRS: dict[str, set[str]] = {}
for _ko, _en in EXTRA_CANON.items():
    for _w in (_ko, _en):
        CANON_PAIRS.setdefault(_w, set()).update({_ko, _en})

# 숫자 읽기(한자어)의 끝자리 받침: 조사 선택용. 0은 '십'(ㅂ)으로 끝난다.
_DIGIT_BATCHIM = {0: "ㅂ", 1: "ㄹ", 2: None, 3: "ㅁ", 4: None, 5: None,
                  6: "ㄱ", 7: "ㄹ", 8: "ㄹ", 9: None}
_JOSA_RE = re.compile(r"^(으로|은|는|이|가|을|를|과|와|로)")


def _josa_for(n: int, josa: str) -> str:
    b = _DIGIT_BATCHIM[n % 10]
    if josa in ("으로", "로"):
        return "로" if b in (None, "ㄹ") else "으로"
    pairs = {"은": ("은", "는"), "는": ("은", "는"), "이": ("이", "가"), "가": ("이", "가"),
             "을": ("을", "를"), "를": ("을", "를"), "과": ("과", "와"), "와": ("과", "와")}
    with_b, without_b = pairs[josa]
    return with_b if b else without_b


def josa_check(text: str, end_pos: int, old: int, new: int, rel: str, ln: int) -> None:
    """shift된 인용 링크 직후의 조사 — 받침 범주가 바뀌면 REVIEW (자동 수정 안 함)."""
    m = _JOSA_RE.match(text[end_pos:end_pos + 2])
    if not m:
        return
    j = m.group(1)
    if _josa_for(old, j) != _josa_for(new, j):
        REVIEW.append(f"{rel}:{ln}: 번호 {old}→{new} 뒤 조사 '{j}' → '{_josa_for(new, j)}' 확인 필요"
                      f" ('이'가 계사 이다/이며 어간이면 그대로 둘 것)")


def line_offsets(text: str) -> list[int]:
    offs = [0]
    for line in text.split("\n")[:-1]:
        offs.append(offs[-1] + len(line) + 1)
    return offs


class LineIndex:
    """문자 위치 → 1-indexed 줄번호."""

    def __init__(self, text: str) -> None:
        self.offs = line_offsets(text)

    def of(self, pos: int) -> int:
        lo, hi = 0, len(self.offs) - 1
        while lo < hi:
            mid = (lo + hi + 1) // 2
            if self.offs[mid] <= pos:
                lo = mid
            else:
                hi = mid - 1
        return lo + 1


class WorkerLocks:
    """cron 워커와 같은 파일을 동시에 쓰지 않도록 그들의 lock을 그대로 잡는다."""

    def __init__(self, wait_s: float) -> None:
        self.wait_s = wait_s
        self.held: list[tuple[Path, object | None]] = []

    def __enter__(self) -> "WorkerLocks":
        for name, style, who in WORKER_LOCKS:
            p = LOCK_DIR / name
            deadline = time.monotonic() + self.wait_s
            announced = False
            while not self._take(p, style):
                if time.monotonic() >= deadline:
                    self.__exit__(None, None, None)
                    fail(f"{who} 가 {int(self.wait_s)}초째 lock을 쥐고 있다 ({p}) — "
                         "끝난 뒤 재실행하거나 --lock-wait 를 늘릴 것")
                if not announced:
                    print(f"WAIT {who} 가 도는 중 — lock 대기 ({p})", flush=True)
                    announced = True
                time.sleep(2)
        return self

    def _take(self, p: Path, style: str) -> bool:
        if style == "flock":
            fh = open(p, "w")
            try:
                fcntl.flock(fh, fcntl.LOCK_EX | fcntl.LOCK_NB)
            except OSError:
                fh.close()
                return False
            self.held.append((p, fh))
            return True
        if p.exists():                      # PID 파일: 살아 있는 프로세스면 양보
            try:
                os.kill(int(p.read_text().strip()), 0)
                return False
            except (ValueError, ProcessLookupError, PermissionError, OSError):
                pass
        p.write_text(str(os.getpid()))
        self.held.append((p, None))
        return True

    def __exit__(self, *exc) -> None:
        for p, fh in reversed(self.held):
            if fh is not None:              # flock 파일은 워커도 같은 경로를 열므로 지우지 않는다
                with contextlib.suppress(OSError):
                    fcntl.flock(fh, fcntl.LOCK_UN)
                    fh.close()
            else:
                with contextlib.suppress(OSError, ValueError):
                    if p.read_text().strip() == str(os.getpid()):
                        p.unlink()
        self.held.clear()


@dataclass
class Ctx:
    mapping: dict[int, int]                        # 옛 번호 → 새 번호
    explicit_map: dict[str, tuple[set[str], int]]  # 명시형 id → (종류 표기들, 번호)
    target_paths: set[str]                         # 대상 글의 ko·en permalink
    valid_anchors: set[str] = field(default_factory=set)   # shift 전 실존 유도형 앵커
    after_anchors: set[str] = field(default_factory=set)   # shift 후 실존하게 될 앵커


def check_unreadable_labels(doc, rel: str) -> None:
    """`<종류> <번호>` 꼴인데 번호를 못 읽은 라벨 — shift에서 빠져 번호에 구멍이 난다.

    종류 어휘의 정본은 `_data/theorem_vocab.yml`(kinds·extra_canon)이므로, 여기서
    걸리면 그 파일에 어휘를 더하는 것이 해결이다 (플러그인·번역 워커도 함께 따라온다).
    """
    for b in doc.boxes:
        if b.number is None and LOOKS_NUMBERED_RE.match(b.label):
            fail(f"{rel}:{b.line_start}: 라벨 {b.label!r}의 번호를 파서가 읽지 못한다 "
                 "— 선두 토큰이 _data/theorem_vocab.yml의 kinds·extra_canon 밖이다. "
                 "그 어휘를 extra_canon에 추가한 뒤 재실행할 것 (그대로 두면 이 박스만 "
                 "shift에서 빠져 번호가 어긋난다).")


def note_dangling(ctx: Ctx, anchor: str, rel: str, ln: int, sample: str) -> None:
    """대상 글에 없는 번호를 가리키는 인용 — 자동 치환하지 않고 게이트로 올린다."""
    if anchor in ctx.after_anchors:
        tail = ("shift 후 이 앵커를 **다른 박스**가 차지한다 — 텍스트 번호와 앵커가 "
                "서로 일치하므로 md_lint도 못 잡는 조용한 오배선이 된다")
    else:
        tail = "shift 후에도 대상 없음 (md_lint의 앵커 실존 검사에는 걸린다)"
    DANGLING.append(f"{rel}:{ln}: #{anchor} — 대상 글에 그 번호의 박스가 없음; {tail}: {sample[:100]!r}")
    DANGLING_ANCHORS.add(anchor)


def masked_segments(text: str) -> list[str]:
    return sorted(text[s:e] for s, e in protected_spans(text))


def shift_opening_lines(text: str, doc, mapping: dict[int, int], rel: str) -> list[tuple[int, int, str]]:
    """::: 여는 줄들(파서가 준 줄번호만)의 번호 shift → char-range 에딧 목록."""
    offs = line_offsets(text)
    lines = text.split("\n")
    edits = []

    def edit_line(lineno: int, new_line: str) -> None:
        old_line = lines[lineno - 1]
        if new_line != old_line:
            edits.append((offs[lineno - 1], offs[lineno - 1] + len(old_line), new_line))

    for b in doc.boxes:
        if b.number is None or b.number not in mapping:
            continue
        old_line = lines[b.line_start - 1]
        new_line, n = re.subn(
            rf"^(:::[ \t]+(?:[\w\-]+[ \t]+)?{re.escape(b.kind)}[ \t]+){b.number}(?!\d)",
            lambda m: f"{m.group(1)}{mapping[b.number]}", old_line, count=1)
        if n != 1:
            REVIEW.append(f"{rel}:{b.line_start}: 여는 줄 번호 치환 실패 — 수동 확인: {old_line!r}")
            continue
        edit_line(b.line_start, new_line)
        tally(rel, "라벨 정의 줄")
        if b.explicit:
            REVIEW.append(f"{rel}:{b.line_start}: 명시형 {{#{b.anchor}}} — 표시 번호만 "
                          f"{b.number}→{mapping[b.number]} shift, id는 유지 (id 개명 여부 판단 필요)")
    for pr in doc.proofs:
        if not pr.standalone or not pr.target_text:
            continue
        tm = re.match(rf"^({NUMBERED_ALT})[ \t]+(\d+)$", pr.target_text.strip())
        if not tm:
            continue
        old = int(tm.group(2))
        if old not in mapping:
            continue
        old_line = lines[pr.line_start - 1]
        new_line = re.sub(rf"(\({re.escape(tm.group(1))}[ \t]+){old}(?!\d)",
                          lambda m: f"{m.group(1)}{mapping[old]}", old_line, count=1)
        edit_line(pr.line_start, new_line)
        tally(rel, "증명 귀속")
    return edits


def shift_citations(text: str, own_paths: set[str], ctx: Ctx,
                    rel: str, is_target_file: bool) -> list[tuple[int, int, str]]:
    """인용 단위 [<text>](<path>#<anchor>)의 번호+앵커 동시 shift.

    is_target_file: 대상 글 자신(ko/en) — path가 빈 값(#anchor)이거나 자기 permalink.
    그 외 파일 — path가 대상 permalink(ko/en)일 때만.
    """
    spans = protected_spans(text)
    li = LineIndex(text)
    cite_kind = "글 내부 참조" if is_target_file else "inbound 인용"

    edits = []
    for m in CITATION_UNIT_RE.finditer(text):
        if in_spans(m.start(), spans):
            continue
        path = m.group("path").rstrip("/")
        if is_target_file:
            if path and path not in own_paths:
                continue
        else:
            if path not in ctx.target_paths:
                continue
        aword, anum = m.group("anchor"), m.group("anum")
        body = m.group("text")

        if anum and aword in PREFIX_KIND:
            anchor = aword + anum
            if anchor not in ctx.valid_anchors:
                note_dangling(ctx, anchor, rel, li.of(m.start()), m.group(0))
                continue
            old = int(anum)
            if old not in ctx.mapping:
                continue
            new = ctx.mapping[old]
            # text 안에서 같은 접두의 종류+번호 — 마지막 출현(⁋ 위치)을 치환.
            cands = [t for t in TEXT_LABEL_RE.finditer(body)
                     if KIND_PREFIX.get(t.group(1)) == aword]
            if not cands:
                REVIEW.append(f"{rel}:{li.of(m.start())}: 앵커 #{aword}{old} 인데 텍스트에 "
                              f"대응 라벨 없음 — 수동 확인: {m.group(0)[:100]!r}")
                continue
            t = cands[-1]
            if int(t.group(2)) != old:
                REVIEW.append(f"{rel}:{li.of(m.start())}: 텍스트 '{t.group(0)}' ↔ 앵커 "
                              f"#{aword}{old} 불일치 — 기존 오류, 수동 수정 필요")
                continue
            new_body = body[:t.start(2)] + str(new) + body[t.end(2):]
            replaced = f"[{new_body}]({m.group('path')}#{aword}{new})"
            edits.append((m.start(), m.end(), replaced))
            tally(rel, cite_kind)
            josa_check(text, m.end(), old, new, rel, li.of(m.start()))
        else:
            # 명시형 id 앵커: id는 verbatim 유지, 표시 번호만 shift.
            full_id = aword + anum
            if full_id not in ctx.explicit_map:
                continue
            kinds, old = ctx.explicit_map[full_id]
            if old not in ctx.mapping:
                continue
            alt = "|".join(re.escape(k) for k in sorted(kinds, key=len, reverse=True))
            cands = [t for t in re.finditer(rf"(?:{alt})[ \t]+(\d+)(?!\d)", body)
                     if int(t.group(1)) == old]
            if not cands:
                continue
            t = cands[-1]
            new_body = body[:t.start(1)] + str(ctx.mapping[old]) + body[t.end(1):]
            edits.append((m.start(), m.end(), f"[{new_body}]({m.group('path')}#{full_id})"))
            tally(rel, cite_kind)
            REVIEW.append(f"{rel}:{li.of(m.start())}: 명시형 #{full_id} 참조 — 표시 번호만 "
                          f"{old}→{ctx.mapping[old]}, id 유지")
    return edits


def shift_data_urls(text: str, ctx: Ctx, rel: str) -> list[tuple[int, int, str]]:
    """_data yml의 `url: <permalink>#<앵커>` — 앵커만 shift (label에는 번호가 없다)."""
    li = LineIndex(text)
    edits = []
    for m in DATA_URL_RE.finditer(text):
        if m.group("path").rstrip("/") not in ctx.target_paths:
            continue
        aword, anum = m.group("aword"), m.group("anum")
        if aword not in PREFIX_KIND:
            continue  # 명시형 id·기타 앵커는 번호를 유도하지 않으므로 그대로 둔다
        anchor = aword + anum
        if anchor not in ctx.valid_anchors:
            note_dangling(ctx, anchor, rel, li.of(m.start()), m.group(0))
            continue
        old = int(anum)
        if old not in ctx.mapping:
            continue
        edits.append((m.start("aword"), m.end("anum"), f"{aword}{ctx.mapping[old]}"))
        tally(rel, "url 앵커")
    return edits


def bare_text_scan(text: str, doc, mapping: dict[int, int], rel: str) -> None:
    """대상 글 안에서 링크·::: 줄 밖의 종류+번호 평문 언급 — 치환하지 않고 REVIEW."""
    spans = list(protected_spans(text))
    li = LineIndex(text)
    opening = {b.line_start for b in doc.boxes} | {p.line_start for p in doc.proofs}
    cited = [(m.start(), m.end()) for m in CITATION_UNIT_RE.finditer(text)]
    lines = text.split("\n")
    for m in TEXT_LABEL_RE.finditer(text):
        if int(m.group(2)) not in mapping:
            continue
        if in_spans(m.start(), spans) or any(s <= m.start() < e for s, e in cited):
            continue
        ln = li.of(m.start())
        if ln in opening:
            continue
        REVIEW.append(f"{rel}:{ln}: 링크 없는 평문 언급 '{m.group(0)}' — shift 여부 판단 필요: "
                      f"{lines[ln - 1].strip()[:100]!r}")


def inbound_bare_scan(text: str, ctx: Ctx, rel: str) -> None:
    """inbound 파일에서 대상 글 링크와 **같은 줄**의 링크 밖 평문 라벨 — REVIEW.

    `[§정칙국소환](…/regular_local_rings)의 명제 4` 처럼 앵커 없이 번호만 부르는
    인용은 인용 단위 regex에 걸리지 않아 자동 shift 대상이 아니다.
    """
    spans = protected_spans(text)
    cited = [(m.start(), m.end()) for m in CITATION_UNIT_RE.finditer(text)]
    offs = line_offsets(text)
    for i, line in enumerate(text.split("\n"), start=1):
        if not any(p in line for p in ctx.target_paths):
            continue
        base = offs[i - 1]
        for m in TEXT_LABEL_RE.finditer(line):
            pos = base + m.start()
            if in_spans(pos, spans) or any(s <= pos < e for s, e in cited):
                continue
            if int(m.group(2)) not in ctx.mapping:
                continue
            REVIEW.append(f"{rel}:{i}: 대상 글 링크와 같은 줄의 링크 밖 평문 '{m.group(0)}' — "
                          f"이 글을 가리키는 것이면 수동 shift 필요: {line.strip()[:100]!r}")


def apply_edits(text: str, edits: list[tuple[int, int, str]]) -> str:
    for s, e, _ in edits:
        for s2, e2, _ in edits:
            if (s, e) != (s2, e2) and s < e2 and s2 < e:
                fail(f"에딧 겹침 (내부 버그): {s}-{e} vs {s2}-{e2}")
    out = text
    for s, e, rep in sorted(edits, reverse=True):
        out = out[:s] + rep + out[e:]
    return out


def transform_md(path: Path, rel: str, ctx: Ctx, is_target: bool,
                 own_paths: set[str]) -> str | None:
    text = path.read_text(encoding="utf-8")
    if not is_target and not any(p in text for p in ctx.target_paths):
        return None
    edits = []
    if is_target:
        doc = parse_labels(text)
        check_unreadable_labels(doc, rel)
        edits += shift_opening_lines(text, doc, ctx.mapping, rel)
        bare_text_scan(text, doc, ctx.mapping, rel)
    else:
        inbound_bare_scan(text, ctx, rel)
    edits += shift_citations(text, own_paths, ctx, rel, is_target)
    if not edits:
        return None
    new = apply_edits(text, edits)
    if masked_segments(text) != masked_segments(new):
        fail(f"{rel}: 보호 구간(수식·fence)이 변경됨 — abort")
    return new


def transform_data(path: Path, rel: str, ctx: Ctx) -> str | None:
    text = path.read_text(encoding="utf-8")
    if not any(p in text for p in ctx.target_paths):
        return None
    edits = shift_data_urls(text, ctx, rel)
    if not edits:
        return None
    new = apply_edits(text, edits)
    if text.count("#") != new.count("#") or len(text.split("\n")) != len(new.split("\n")):
        fail(f"{rel}: yml 구조가 바뀜 — abort")
    return new


def kind_spellings(kind: str) -> set[str]:
    """종류 단어의 ko·en 표기 쌍 (kinds → PREFIX_KIND, 그 밖 → extra_canon)."""
    prefix = KIND_PREFIX.get(kind)
    if prefix:
        return set(PREFIX_KIND[prefix])
    return set(CANON_PAIRS.get(kind, {kind}))


def build_explicit_map(doc, en_doc) -> dict[str, tuple[set[str], int]]:
    """명시형 id → (종류 표기들, 번호). en 짝의 표기까지 모아야 en 참조도 잡힌다."""
    out: dict[str, tuple[set[str], int]] = {}
    for b in doc.boxes:
        if b.explicit and b.number is not None:
            out[b.anchor] = (kind_spellings(b.kind), b.number)
    if en_doc is None:
        return out
    for b in en_doc.boxes:
        if b.explicit and b.anchor in out:
            kinds, num = out[b.anchor]
            out[b.anchor] = (kinds | kind_spellings(b.kind), num)
    return out


def label_signature(doc) -> set[tuple[str, int]]:
    """(앵커, 번호) 집합 — ko·en 짝의 라벨 구조 대조용."""
    return {(b.anchor, b.number) for b in doc.boxes if b.number is not None}


def anchor_sets(doc, mapping: dict[int, int]) -> tuple[set[str], set[str]]:
    """(shift 전 실존 유도형 앵커, shift 후 실존하게 될 유도형 앵커)."""
    valid, after = set(), set()
    for b in doc.boxes:
        if b.explicit or b.number is None:
            continue
        valid.add(b.anchor)
        after.add(f"{KIND_PREFIX[b.kind]}{mapping.get(b.number, b.number)}")
    return valid, after


def extra_md_paths() -> list[Path]:
    out: list[Path] = []
    for d in EXTRA_MD_DIRS:
        out += sorted((ROOT / d).rglob("*.md"))
    return out


def data_paths() -> list[Path]:
    return sorted((ROOT / DATA_DIR).rglob("*.yml"))


def write_backup(changes: list[tuple[str, Path, str]]) -> Path:
    """쓰기 전 원본 사본 — 커밋 체크포인트 대신의 되돌리기 수단."""
    base = Path(tempfile.gettempdir()) / f"relabel-backup-{datetime.now():%Y%m%d-%H%M%S}"
    for rel, path, _ in changes:
        dst = base / rel
        dst.parent.mkdir(parents=True, exist_ok=True)
        dst.write_text(path.read_text(encoding="utf-8"), encoding="utf-8")
    return base


def verify_after_apply(written: list[tuple[str, Path]], ctx: Ctx,
                       target_rels: set[str]) -> list[str]:
    """쓴 뒤 재스캔: 대상 글을 가리키는 유도형 앵커가 전부 실존하는가."""
    bad = []
    for rel, path in written:
        text = path.read_text(encoding="utf-8")
        li = LineIndex(text)
        if path.suffix == ".yml":
            hits = [(m.start(), m.group("aword"), m.group("anum"))
                    for m in DATA_URL_RE.finditer(text)
                    if m.group("path").rstrip("/") in ctx.target_paths]
        else:
            hits = []
            for m in CITATION_UNIT_RE.finditer(text):
                p = m.group("path").rstrip("/")
                if p:
                    if p not in ctx.target_paths:
                        continue
                elif rel not in target_rels:
                    continue   # 남의 글의 내부 앵커
                hits.append((m.start(), m.group("anchor"), m.group("anum")))
        for pos, aword, anum in hits:
            if not anum or aword not in PREFIX_KIND:
                continue
            anchor = aword + anum
            # --allow-dangling으로 이미 보고하고 통과시킨 것은 다시 세지 않는다.
            if anchor not in ctx.after_anchors and anchor not in DANGLING_ANCHORS:
                bad.append(f"{rel}:{li.of(pos)}: #{anchor} 대상 없음")
    return bad


def run_shift(args) -> None:
    posts = iter_posts()
    target, _ = resolve_one(args.post, posts, lang="ko")
    if target.lang != "ko":
        fail("ko 원본을 지정할 것 — en 짝은 자동으로 함께 처리된다")
    en = en_counterpart(target, posts)

    doc = parse_labels(target.path.read_text(encoding="utf-8"))
    check_unreadable_labels(doc, target.rel)
    all_nums = [b.number for b in doc.boxes if b.number is not None]
    nums = sorted(set(all_nums))
    moving = [n for n in nums if n >= args.start]
    if not moving:
        fail(f"번호 ≥ {args.start} 인 박스가 없음 (실존: {nums})")
    mapping = {n: n + args.delta for n in moving}
    if min(mapping.values()) < 1:
        fail("shift 결과 번호가 1 미만이 됨")
    untouched = {n for n in nums if n < args.start}
    collide = untouched & set(mapping.values())
    if collide:
        fail(f"shift 결과 번호 충돌: {sorted(collide)} — 삭제가 덜 됐거나 delta 오류")

    en_doc = None
    en_drifted = False
    if en is not None:
        en_doc = parse_labels(en.path.read_text(encoding="utf-8"))
        check_unreadable_labels(en_doc, en.rel)
        en_drifted = label_signature(doc) != label_signature(en_doc)

    ko_pl = target.permalink.rstrip("/")
    en_pl = en.permalink.rstrip("/") if en else None
    ctx = Ctx(
        mapping=mapping,
        explicit_map=build_explicit_map(doc, en_doc),
        target_paths={p for p in (ko_pl, en_pl) if p},
    )
    ctx.valid_anchors, ctx.after_anchors = anchor_sets(doc, mapping)

    print(f"PLAN {target.rel}: 번호 {len(moving)}개 shift "
          f"({moving[0]}..{moving[-1]} → {mapping[moving[0]]}..{mapping[moving[-1]]}, by={args.delta:+d})")
    if en is None:
        print("NOTE en 짝 없음 — ko만 처리")
    elif en_drifted:
        ko_sig, en_sig = label_signature(doc), label_signature(en_doc)
        print(f"NOTE en 짝의 라벨 구조가 ko와 다르다 (번역 밀림) — {en.rel} 파일 자체는 "
              "번역 워커의 재생성에 맡기고 건드리지 않는다. en permalink를 가리키는 "
              "외부 참조는 재생성 결과(=ko의 번호)에 맞춰 지금 갱신한다.\n"
              f"     ko에만: {sorted(a for a, _ in ko_sig - en_sig)}\n"
              f"     en에만: {sorted(a for a, _ in en_sig - ko_sig)}")

    changes: list[tuple[str, Path, str]] = []

    def stage(path: Path, new: str | None) -> None:
        if new is not None:
            changes.append((str(path.relative_to(ROOT)), path, new))

    targets = [(target, {ko_pl})]
    if en is not None and not en_drifted:
        targets.append((en, {en_pl}))
    for p, own in targets:
        stage(p.path, transform_md(p.path, p.rel, ctx, True, own))
    for p in posts:
        if p.path == target.path or (en and p.path == en.path):
            continue
        stage(p.path, transform_md(p.path, p.rel, ctx, False, set()))
    for path in extra_md_paths():
        stage(path, transform_md(path, str(path.relative_to(ROOT)), ctx, False, set()))
    for path in data_paths():
        stage(path, transform_data(path, str(path.relative_to(ROOT)), ctx))

    for rel, path, new in changes:
        old = path.read_text(encoding="utf-8")
        diff = difflib.unified_diff(old.splitlines(keepends=True), new.splitlines(keepends=True),
                                    fromfile=rel, tofile=rel + " (shifted)")
        sys.stdout.writelines(diff)
        print()

    if changes:
        print("── 변경 내역 " + "─" * 56)
        print(f"  번호 매핑: {', '.join(f'{o}→{n}' for o, n in sorted(mapping.items()))}")
        width = max(len(rel) for rel, _, _ in changes)
        for rel, _, _ in changes:
            parts = [f"{k} {TALLY[(rel, k)]}" for k in TALLY_KINDS if (rel, k) in TALLY]
            print(f"  {rel.ljust(width)}  {', '.join(parts)}")

    if DANGLING:
        print("── DANGLING (없는 번호를 가리키는 인용 — 먼저 처리할 것) " + "─" * 16)
        for d in DANGLING:
            print("  " + d)
    if REVIEW:
        print("── REVIEW (자동 치환 안 함 — 판단 필요) " + "─" * 30)
        for r in REVIEW:
            print("  " + r)

    print(f"SUMMARY 파일 {len(changes)}개 변경, DANGLING {len(DANGLING)}건, REVIEW {len(REVIEW)}건"
          + ("" if args.apply else " (dry-run — 쓰지 않음)"))
    if not args.apply:
        return

    if DANGLING and not args.allow_dangling:
        fail(f"DANGLING {len(DANGLING)}건 — 쓰지 않았다. 위 인용들은 삭제된(또는 애초에 없는) "
             "번호를 가리키므로 shift가 이들을 다른 박스로 조용히 재배선한다. 각 인용을 "
             "먼저 재조준하거나 지운 뒤 다시 실행할 것. "
             "의도적으로 무시하려면 --allow-dangling.")

    backup = write_backup(changes)
    print(f"APPLY 백업 {backup}  (되돌리기: cp -r {backup}/. {ROOT}/)")
    print("APPLY 대상: (IDE에 열린 파일이 있으면 버퍼 저장이 덮을 수 있음 — 닫고 실행할 것)")
    for rel, _, _ in changes:
        print("  " + rel)
    for rel, path, new in changes:
        path.write_text(new, encoding="utf-8")
    # 사후 게이트 ①: 대상 글 재파싱 — 번호 다중집합이 매핑 결과와 정확히 일치하는가.
    # (정의 6·정의 6′처럼 같은 번호를 의도적으로 공유하는 박스가 있어 유일성으로는 못 본다.)
    doc2 = parse_labels(target.path.read_text(encoding="utf-8"))
    nums2 = sorted(b.number for b in doc2.boxes if b.number is not None)
    expected = sorted(mapping.get(n, n) for n in all_nums)
    if nums2 != expected:
        print(f"ERROR shift 후 번호 집합 불일치 — 기대 {expected}, 실제 {nums2}", file=sys.stderr)
        sys.exit(1)
    # 사후 게이트 ②: 쓴 파일에서 대상 글 앵커가 전부 실존하는가.
    target_rels = {target.rel} | ({en.rel} if en and not en_drifted else set())
    bad = verify_after_apply([(rel, path) for rel, path, _ in changes], ctx, target_rels)
    if bad:
        print("ERROR shift 후 대상 없는 앵커 잔존:", file=sys.stderr)
        for b in bad:
            print("  " + b, file=sys.stderr)
        sys.exit(1)
    print("DONE")


def cmd_shift(args) -> None:
    # --apply는 워커 lock 안에서 읽기·변환·쓰기를 한 번에 끝낸다 (중간 쓰기 클로버 방지).
    with WorkerLocks(args.lock_wait) if args.apply else contextlib.nullcontext():
        run_shift(args)


def main() -> None:
    ap = argparse.ArgumentParser(prog="relabel")
    sub = ap.add_subparsers(dest="cmd", required=True)
    s = sub.add_parser("shift")
    s.add_argument("post")
    s.add_argument("--from", dest="start", type=int, required=True)
    s.add_argument("--by", dest="delta", type=int, required=True)
    s.add_argument("--apply", action="store_true")
    s.add_argument("--allow-dangling", action="store_true",
                   help="DANGLING 게이트 무시 (권장하지 않음)")
    s.add_argument("--lock-wait", type=float, default=600.0,
                   help="워커 lock 대기 상한(초). 기본 600")
    args = ap.parse_args()
    cmd_shift(args)


if __name__ == "__main__":
    main()
