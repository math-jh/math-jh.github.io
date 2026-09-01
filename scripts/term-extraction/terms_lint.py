#!/usr/bin/env python3
"""terms_lint.py — 찾아보기 데이터(_data/terms.yml)의 검증·정규화기.

link_normalizer.rb 가 글 본문의 교차참조 표시 텍스트를 빌드 때 정본으로
맞추듯이, 이 스크립트는 terms.yml 을 정본(글 frontmatter title ·
categories.yml ko 표시명)과 대조한다. 차이: 저쪽은 in-memory 재작성(소스
불변)이고, 이쪽은 terms.yml 이 기계 관리 데이터라서 --fix 로 파일 자체를
고친다.

검사 (E=에러 → exit 1, W=경고 → exit 0):
  E SCHEMA/PRIMARY/LANG  필드 누락·이상값
  E GROUP     글자 분류 오류 (수식 래퍼·발음기호 접기 기준)      [--fix 가능]
  E LABEL     라벨이 '[categories.yml ko] §현재 글 제목' 이 아님   [--fix 가능]
  E EMPTY_GROUP 빈 그룹 (조판이 깨진다)                          [--fix 가능]
  E ORDER     그룹 내 정렬 위반 (nat_key·id 순 = 조판 순서)       [--fix 가능]
  E CASE      인명 파생 고유명사 소문자 (terms_common._PROPER_FORMS 기준;
              추출 시점 교정과 같은 표 — 기존 항목의 드리프트를 잡는다)
                                                                [--fix 가능]
  E DEFS_ORDER defs 가 논리 순서가 아님 (categories.yml 순서→weight; 2026-07-21
              추가 — add_def 는 등록순 append 라 논리 순서 보장이 없었음. 모든
              def 대상이 해석 가능할 때만 검사·정렬)              [--fix 가능]
  E URL       def/ref url 이 어떤 글의 permalink 도 아님 (깨진 링크)
  E DUP_ID/DUP_TERM 중복 (Čech/čech 같은 정규화 중복 포함)
  E SEE       see 가 없는 항목 id 를 가리킴
  W UNPUB     published:false 초안으로의 링크 (발행 전까지 프로덕션 404)

--fix 는 결정적 수정만 한다 (라벨 정규화·그룹 이동·빈 그룹 제거). 깨진
url·중복·dangling see 는 판단이 필요하므로 절대 자동 수정하지 않는다 —
보고만 하고 exit 1. 수정 전 원본은 terms.yml.bak 으로 남긴다.

--notify 는 남은 에러가 있을 때 알림 shim(~/.local/bin/notify)으로 알린다.

--fix 는 terms.yml 을 읽고 다시 쓰므로(read→write) 같은 파일을 쓰는 다른 실행과
lost update 로 부딪힌다. extract_terms.py 와 같은 PID 파일 lock(/tmp/extract-terms.lock)
을 잡아 양방향으로 물린다 (relabel.py 도 같은 lock 을 잡는다). 못 잡으면 이번 회차를
건너뛴다 — 매일 도는 감사라 다음 실행에서 처리된다.

cron (매일 04:20, link normalizer 감사 04:30 직전):
  20 4 * * * cd .../scripts/term-extraction && python3 terms_lint.py --fix --notify >>term_extraction_lint.log 2>&1
"""
from __future__ import annotations

import argparse
import os
import re
import sys
import time
from datetime import datetime
from pathlib import Path

import yaml

sys.path.insert(0, str(Path(__file__).resolve().parent))
from terms_common import (  # noqa: E402
    BLOG_ROOT, CATEGORIES_PATH, TERMS_PATH, Issue, _frontmatter,
    category_ko_maps, chunk_field, chunk_id, insert_sorted, join_file,
    letter_of, nat_key, normalize_proper_case, permalink_map, semantic_checks,
    split_file, url_slug, yaml_quote,
)

sys.path.insert(0, str(BLOG_ROOT / "scripts/lib"))
from cron_commit import commit_outputs  # noqa: E402

SCRIPT_DIR = Path(__file__).resolve().parent
BACKUP_PATH = SCRIPT_DIR / "terms.yml.bak"

# terms.yml 쓰기 lock — extract_terms.py 와 같은 PID 파일 경로·규약.
LOCK_PATH = Path("/tmp/extract-terms.lock")
LOCK_WAIT = 180.0


def log(msg: str) -> None:
    print(f"[{datetime.now():%Y-%m-%d %H:%M:%S}] {msg}")


def acquire_lock(wait_s: float = LOCK_WAIT) -> bool:
    """살아 있는 PID 가 쥐고 있으면 놓을 때까지 기다린다. 상한 초과 시 False."""
    deadline = time.monotonic() + wait_s
    while True:
        if LOCK_PATH.exists():
            alive = True
            try:
                os.kill(int(LOCK_PATH.read_text().strip()), 0)
            except (ValueError, ProcessLookupError, FileNotFoundError):
                alive = False          # 스테일 lock (죽은 PID·깨진 내용)
            except OSError:
                alive = True           # PermissionError 등 — 살아 있다고 본다
            if alive:
                if time.monotonic() >= deadline:
                    return False
                time.sleep(5)
                continue
        try:
            LOCK_PATH.write_text(str(os.getpid()))
        except OSError:
            return False
        return True


def release_lock() -> None:
    try:
        if LOCK_PATH.read_text().strip() == str(os.getpid()):
            LOCK_PATH.unlink()
    except (OSError, ValueError):
        pass


def send_notify(msg: str, subject: str = "[terms_lint]",
                ttl: int | None = 86400) -> None:
    """알림 한 통. 벤더는 shim(~/.local/bin/notify) 안에만 있다.

    deprecated_terms_lint.py 가 이 함수를 import 해서 쓴다.
    """
    import subprocess
    notify = Path.home() / ".local/bin/notify"
    try:
        cmd = [str(notify), "-s", subject, "-b", msg, "-g", "blog"]
        if ttl is not None:
            cmd.extend(["--archive", "--ttl", str(ttl)])
        r = subprocess.run(cmd,
                           capture_output=True, text=True, timeout=20)
        if r.returncode != 0:
            log(f"알림 전송 실패 rc={r.returncode}: {r.stderr.strip()[:200]}")
    except Exception as e:  # noqa: BLE001
        log(f"알림 전송 실패: {e}")


# ---------------------------------------------------------------------------
# 자동 수정 (결정적인 것만)
# ---------------------------------------------------------------------------

def fix_labels(text: str, pmap: dict, ko_by_slug: dict) -> tuple[str, int]:
    """라벨 줄(다음 줄이 url)을 '[categories.yml ko] §현재 제목' 으로."""
    lines = text.split("\n")
    n = 0
    for i, ln in enumerate(lines):
        m = re.match(r"^(\s*)- label: (.*)$", ln)
        if not m or i + 1 >= len(lines):
            continue
        mu = re.match(r"^\s*url: (\S+)$", lines[i + 1])
        if not mu:
            continue
        url = mu.group(1).split("#")[0].rstrip("/")
        if url not in pmap:
            continue  # 깨진 url 은 자동 수정 대상 아님
        cat = ko_by_slug.get(url_slug(url) or "")
        if not cat:
            continue
        old = m.group(2).strip()
        if old.startswith(("'", '"')) and len(old) >= 2 and old.endswith(old[0]):
            old = old[1:-1].replace("''", "'") if old[0] == "'" else old[1:-1]
        new = f"[{cat}] §{pmap[url]['title']}"
        if new != old:
            lines[i] = f"{m.group(1)}- label: {yaml_quote(new)}"
            n += 1
    return "\n".join(lines), n


def _order_key(c: str):
    return (nat_key(chunk_field(c, "en") or ""), chunk_id(c))


def check_parser_parity(text: str, data: dict) -> list[Issue]:
    """청크 파서(terms_common.split_file/chunk_field)와 yaml.safe_load 가 같은
    사실을 읽는지 교차 검증 (이중 SoT 감사 [10], 2026-07-22).

    terms.yml 은 두 파서 계열이 함께 읽는다 — 조판·수술은 포맷 보존 청크
    파서로, lint·워커 게이트는 yaml 로. 청크 파서는 `  key: value` 평면
    스칼라 형태를 가정하는데, 이 가정을 강제하는 게이트가 없어서 블록
    스칼라(`ko: |-`)나 이상 들여쓰기가 들어오면 두 계열이 **다른 값을
    조용히** 읽는다. 여기서 id·en·ko·primary 를 항목 단위로 대조해 어긋나면
    E — 편집 훅(terms_lint_hook)이 즉시 막는다."""
    issues: list[Issue] = []
    _, groups = split_file(text)
    for letter, chunks in groups.items():
        ents = (data.get(letter) or []) if isinstance(data, dict) else []
        if len(chunks) != len(ents):
            issues.append(Issue("E", "PARSER", f"{letter} 그룹 항목 수가 파서별로 다름 "
                                f"(청크 {len(chunks)} vs yaml {len(ents)})"))
            continue
        for c, e in zip(chunks, ents):
            if not isinstance(e, dict):
                issues.append(Issue("E", "PARSER", f"{letter} 그룹에 매핑 아닌 항목"))
                continue
            for f in ("id", "en", "ko", "primary"):
                cv = chunk_id(c) if f == "id" else chunk_field(c, f)
                yv = e.get(f)
                cv = "" if cv is None else str(cv)
                yv = "" if yv is None else str(yv)
                if cv != yv:
                    issues.append(Issue("E", "PARSER",
                                        f"{chunk_id(c) or '?'}: {f} 가 파서별로 다름 "
                                        f"(청크 {cv!r} vs yaml {yv!r} — 블록 스칼라/"
                                        f"들여쓰기 이상 의심)"))
    return issues


def check_order(text: str) -> list[Issue]:
    """그룹 내 정렬 (fold 정규화 nat_key, 동률은 id). Terms 페이지가 파일
    순서 그대로 렌더하므로 여기가 곧 조판 순서다."""
    _, groups = split_file(text)
    return [Issue("E", "ORDER", f"{letter} 그룹이 정렬 순서가 아님",
                  fixable=True)
            for letter, chunks in groups.items()
            if [_order_key(c) for c in chunks]
            != sorted(_order_key(c) for c in chunks)]


def fix_order(text: str) -> tuple[str, int]:
    header, groups = split_file(text)
    n = 0
    for letter, chunks in groups.items():
        ordered = sorted(chunks, key=_order_key)
        if ordered != chunks:
            n += 1
            groups[letter] = ordered
    return join_file(header, groups), n


_EN_LINE_RE = re.compile(r"^(  en: )(.*)$", re.M)


def check_case(text: str) -> list[Issue]:
    """en 표기의 인명 파생 고유명사 소문자 드리프트 (_PROPER_FORMS 기준)."""
    _, groups = split_file(text)
    out = []
    for chunks in groups.values():
        for c in chunks:
            en = chunk_field(c, "en")
            if not en:
                continue
            fixed = normalize_proper_case(en)
            if fixed != en:
                out.append(Issue("E", "CASE",
                                 f"{chunk_id(c)}: en {en!r} → {fixed!r}",
                                 fixable=True))
    return out


def fix_case(text: str) -> tuple[str, int]:
    header, groups = split_file(text)
    n = 0
    for chunks in groups.values():
        for i, c in enumerate(chunks):
            en = chunk_field(c, "en")
            if not en:
                continue
            fixed = normalize_proper_case(en)
            if fixed != en:
                chunks[i] = _EN_LINE_RE.sub(
                    lambda m: m.group(1) + yaml_quote(fixed), c, count=1)
                n += 1
    return join_file(header, groups), n


_CAT_IDX: dict[str, int] | None = None
_WEIGHT_CACHE: dict[str, tuple | None] = {}


def _cat_idx() -> dict[str, int]:
    """카테고리 url 슬러그 → categories.yml subjects 순서 index (= 논리 순서)."""
    global _CAT_IDX
    if _CAT_IDX is None:
        cats = yaml.safe_load(CATEGORIES_PATH.read_text(encoding="utf-8"))
        _CAT_IDX = {}
        for i, name in enumerate((cats.get("subjects") or {})):
            slug = name.split(" / ")[-1].lower().replace(" ", "_")
            _CAT_IDX[slug] = i
    return _CAT_IDX


def _def_key(item: str, pmap: dict) -> tuple | None:
    """def 항목의 논리 순서 키 (cat_idx, weight). 해석 불가면 None."""
    m = re.search(r"^\s*url: (\S+)$", item, re.M)
    if not m:
        return None
    pl = m.group(1).split("#")[0].rstrip("/")
    if pl in _WEIGHT_CACHE:
        return _WEIGHT_CACHE[pl]
    key = None
    info = pmap.get(pl)
    ms = re.match(r"/ko/math/([^/]+)/", pl)
    if info and ms and ms.group(1) in _cat_idx():
        try:
            fm = _frontmatter((BLOG_ROOT / info["path"]).read_text(encoding="utf-8"))
            key = (_cat_idx()[ms.group(1)], int(fm.get("weight")))
        except (OSError, TypeError, ValueError):
            key = None
    _WEIGHT_CACHE[pl] = key
    return key


def _defs_block(chunk: str) -> tuple[int, int, list[str]] | None:
    """(defs 시작줄, 끝줄 exclusive, item 문자열 목록). defs 없으면 None."""
    lines = chunk.split("\n")
    try:
        s = next(i for i, ln in enumerate(lines) if ln.rstrip() == "  defs:")
    except StopIteration:
        return None
    j = s + 1
    while j < len(lines) and (lines[j].startswith("  - ")
                              or lines[j].startswith("    ")):
        j += 1
    items, cur = [], []
    for ln in lines[s + 1:j]:
        if ln.startswith("  - ") and cur:
            items.append("\n".join(cur))
            cur = []
        cur.append(ln)
    if cur:
        items.append("\n".join(cur))
    return s, j, items


def _defs_reorder(chunk: str, pmap: dict) -> str | None:
    """defs 를 논리 순서로 재정렬한 청크. 재정렬 불필요·불가면 None.

    def 대상 중 하나라도 (카테고리·weight) 해석이 안 되면 판단 불가로 두고
    건드리지 않는다 — 깨진 url 은 URL 검사가 따로 보고한다."""
    blk = _defs_block(chunk)
    if blk is None or len(blk[2]) < 2:
        return None
    s, j, items = blk
    keys = [_def_key(it, pmap) for it in items]
    if any(k is None for k in keys):
        return None
    order = sorted(range(len(items)), key=lambda i: (keys[i], i))
    if order == list(range(len(items))):
        return None
    lines = chunk.split("\n")
    new_items = [items[i] for i in order]
    return "\n".join(lines[:s + 1] + new_items + lines[j:])


def check_defs_order(text: str, pmap: dict) -> list[Issue]:
    _, groups = split_file(text)
    return [Issue("E", "DEFS_ORDER",
                  f"{chunk_id(c)}: defs 가 논리 순서(카테고리→weight)가 아님",
                  fixable=True)
            for chunks in groups.values() for c in chunks
            if _defs_reorder(c, pmap) is not None]


def fix_defs_order(text: str, pmap: dict) -> tuple[str, int]:
    header, groups = split_file(text)
    n = 0
    for letter, chunks in groups.items():
        for i, c in enumerate(chunks):
            c2 = _defs_reorder(c, pmap)
            if c2 is not None:
                chunks[i] = c2
                n += 1
    return join_file(header, groups), n


def fix_groups(text: str) -> tuple[str, int]:
    """오분류 청크를 제 그룹으로 이동, 빈 그룹 제거."""
    header, groups = split_file(text)
    moves = []
    for letter in list(groups):
        stay = []
        for c in groups[letter]:
            lo = letter_of(chunk_field(c, "en") or "")
            if lo and lo != letter:
                moves.append((lo, c))
            else:
                stay.append(c)
        groups[letter] = stay
    for lo, c in moves:
        insert_sorted(groups.setdefault(lo, []), c)
    return join_file(header, groups), len(moves)


# ---------------------------------------------------------------------------
# main
# ---------------------------------------------------------------------------

def run(path: Path, fix: bool, notify: bool) -> int:
    text = path.read_text(encoding="utf-8")
    try:
        data = yaml.safe_load(text)
    except yaml.YAMLError as e:
        log(f"ERROR PARSE: {e}")
        if notify:
            send_notify(f"[terms_lint] terms.yml 이 YAML 로 파싱되지 않음: {e}")
        return 1

    pmap = permalink_map()
    ko_by_slug, _ = category_ko_maps()
    issues = (semantic_checks(data, pmap, ko_by_slug) + check_order(text)
              + check_case(text)
              + check_defs_order(text, pmap) + check_parser_parity(text, data))

    if fix and any(i.fixable for i in issues):
        BACKUP_PATH.write_text(text, encoding="utf-8")
        new, n_case = fix_case(text)
        new, n_lbl = fix_labels(new, pmap, ko_by_slug)
        new, n_grp = fix_groups(new)  # 빈 그룹 제거 포함
        new, n_ord = fix_order(new)
        new, n_def = fix_defs_order(new, pmap)
        if new != text:
            # 수정본이 자기 검사를 통과해야만 쓴다: 파싱되고, 항목이 사라지지
            # 않았고, 고칠 수 있는 에러가 실제로 줄었을 것.
            try:
                nd = yaml.safe_load(new)
            except yaml.YAMLError as e:
                log(f"ERROR: 수정본이 YAML 파싱 실패 — 쓰지 않음: {e}")
                return 1
            old_n = sum(len(v or []) for v in data.values())
            new_n = sum(len(v or []) for v in nd.values())
            if new_n != old_n:
                log(f"ERROR: 수정 중 항목 수 변동({old_n}→{new_n}) — 쓰지 않음")
                return 1
            tmp = path.with_suffix(".tmp")
            tmp.write_text(new, encoding="utf-8")
            tmp.replace(path)
            log(f"자동 수정: 라벨 {n_lbl}건, 케이스 {n_case}건, 그룹 이동 {n_grp}건, "
                f"정렬 {n_ord}그룹, defs 재정렬 {n_def}건 (백업: {BACKUP_PATH.name})")
            # 자기 수정분은 자기 이름으로 커밋한다 (push 는 autopush). --path 로
            # 다른 파일을 검사하는 테스트 실행은 커밋하지 않는다.
            if path.resolve() == TERMS_PATH.resolve():
                commit_outputs("terms-lint", [str(TERMS_PATH.relative_to(BLOG_ROOT))],
                               f"라벨 {n_lbl}·케이스 {n_case}·그룹 {n_grp}·"
                               f"정렬 {n_ord}·defs {n_def}건 자동 수정", log=log)
            issues = (semantic_checks(nd, pmap, ko_by_slug) + check_order(new)
                      + check_case(new)
                      + check_defs_order(new, pmap) + check_parser_parity(new, nd))

    errors = [i for i in issues if i.level == "E"]
    warns = [i for i in issues if i.level == "W"]
    for i in errors:
        log(repr(i))
    # UNPUB 는 같은 초안을 여러 항목이 가리켜 수십 줄이 되므로 url 별로 묶는다
    unpub: dict[str, int] = {}
    for i in warns:
        if i.code == "UNPUB":
            url = i.msg.split()[1]
            unpub[url] = unpub.get(url, 0) + 1
        else:
            log(repr(i))
    for url, cnt in sorted(unpub.items()):
        log(f"[W] UNPUB: {url} ← 항목 {cnt}개 (published:false 초안, 발행 전까지 프로덕션 404)")
    n = sum(len(v or []) for v in yaml.safe_load(path.read_text(encoding='utf-8')).values())
    log(f"요약: 항목 {n} · 에러 {len(errors)} · 경고 {len(warns)}")

    if errors and notify:
        head = "\n".join(repr(i) for i in errors[:10])
        more = f"\n… 외 {len(errors) - 10}건" if len(errors) > 10 else ""
        send_notify(f"[terms_lint] terms.yml 에러 {len(errors)}건 (자동 수정 불가분):\n{head}{more}")
    return 1 if errors else 0


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--fix", action="store_true", help="결정적 드리프트 자동 수정")
    ap.add_argument("--notify", action="store_true", help="에러 잔존 시 Bark 알림")
    ap.add_argument("--path", default=str(TERMS_PATH), help="검사 대상 (테스트용)")
    args = ap.parse_args()
    # 읽기 전용 실행과 테스트 대상(--path)은 lock 이 필요 없다 (쓰기는 tmp+replace 라
    # 원자적이고, 부딪히는 것은 --fix 의 read→write 뿐이다).
    locked = args.fix and Path(args.path).resolve() == TERMS_PATH.resolve()
    if locked and not acquire_lock():
        log(f"SKIP: terms.yml 쓰기 lock 을 {int(LOCK_WAIT)}초 안에 얻지 못함 "
            f"({LOCK_PATH}) — 다른 실행이 쓰는 중이다. 다음 회차에서 처리된다.")
        return 0
    try:
        return run(Path(args.path), args.fix, args.notify)
    except Exception as e:  # noqa: BLE001
        log(f"CRASH: {e!r}")
        if args.notify:
            send_notify(f"[terms_lint] 크래시: {e!r}")
        return 2
    finally:
        if locked:
            release_lock()


if __name__ == "__main__":
    sys.exit(main())
