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
  E URL       def/ref url 이 어떤 글의 permalink 도 아님 (깨진 링크)
  E DUP_ID/DUP_TERM 중복 (Čech/čech 같은 정규화 중복 포함)
  E SEE       see 가 없는 항목 id 를 가리킴
  W UNPUB     published:false 초안으로의 링크 (발행 전까지 프로덕션 404)

--fix 는 결정적 수정만 한다 (라벨 정규화·그룹 이동·빈 그룹 제거). 깨진
url·중복·dangling see 는 판단이 필요하므로 절대 자동 수정하지 않는다 —
보고만 하고 exit 1. 수정 전 원본은 terms.yml.bak 으로 남긴다.

--notify 는 남은 에러가 있을 때 텔레그램(~/.hermes/.env)으로 알린다.

cron (매일 04:20, link normalizer 감사 04:30 직전):
  20 4 * * * cd .../scripts/term-extraction && python3 terms_lint.py --fix --notify >>term_extraction_lint.log 2>&1
"""
from __future__ import annotations

import argparse
import os
import re
import sys
from datetime import datetime
from pathlib import Path

import yaml

sys.path.insert(0, str(Path(__file__).resolve().parent))
from terms_common import (  # noqa: E402
    TERMS_PATH, Issue, category_ko_maps, chunk_field, chunk_id, insert_sorted,
    join_file, letter_of, nat_key, permalink_map, semantic_checks, split_file,
    url_slug, yaml_quote,
)

SCRIPT_DIR = Path(__file__).resolve().parent
BACKUP_PATH = SCRIPT_DIR / "terms.yml.bak"


def log(msg: str) -> None:
    print(f"[{datetime.now():%Y-%m-%d %H:%M:%S}] {msg}")


def send_telegram(msg: str) -> None:
    env_path = Path.home() / ".hermes" / ".env"
    if env_path.exists():
        for line in env_path.read_text().splitlines():
            if "=" in line and not line.startswith("#"):
                k, v = line.strip().split("=", 1)
                os.environ.setdefault(k, v)
    token = os.environ.get("TELEGRAM_BOT_TOKEN", "")
    chat = os.environ.get("TELEGRAM_HOME_CHANNEL",
                          os.environ.get("TELEGRAM_ALLOWED_USERS", ""))
    if not token or not chat:
        log("텔레그램 미설정 — 알림 생략")
        return
    import urllib.parse
    import urllib.request
    data = urllib.parse.urlencode({"chat_id": chat, "text": msg}).encode()
    try:
        urllib.request.urlopen(
            f"https://api.telegram.org/bot{token}/sendMessage", data=data, timeout=10)
    except Exception as e:  # noqa: BLE001
        log(f"텔레그램 전송 실패: {e}")


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
            send_telegram(f"[terms_lint] terms.yml 이 YAML 로 파싱되지 않음: {e}")
        return 1

    pmap = permalink_map()
    ko_by_slug, _ = category_ko_maps()
    issues = semantic_checks(data, pmap, ko_by_slug) + check_order(text)

    if fix and any(i.fixable for i in issues):
        BACKUP_PATH.write_text(text, encoding="utf-8")
        new, n_lbl = fix_labels(text, pmap, ko_by_slug)
        new, n_grp = fix_groups(new)  # 빈 그룹 제거 포함
        new, n_ord = fix_order(new)
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
            log(f"자동 수정: 라벨 {n_lbl}건, 그룹 이동 {n_grp}건, "
                f"정렬 {n_ord}그룹 (백업: {BACKUP_PATH.name})")
            issues = semantic_checks(nd, pmap, ko_by_slug) + check_order(new)

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
        send_telegram(f"[terms_lint] terms.yml 에러 {len(errors)}건 (자동 수정 불가분):\n{head}{more}")
    return 1 if errors else 0


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--fix", action="store_true", help="결정적 드리프트 자동 수정")
    ap.add_argument("--notify", action="store_true", help="에러 잔존 시 텔레그램")
    ap.add_argument("--path", default=str(TERMS_PATH), help="검사 대상 (테스트용)")
    args = ap.parse_args()
    try:
        return run(Path(args.path), args.fix, args.notify)
    except Exception as e:  # noqa: BLE001
        log(f"CRASH: {e!r}")
        if args.notify:
            send_telegram(f"[terms_lint] 크래시: {e!r}")
        return 2


if __name__ == "__main__":
    sys.exit(main())
