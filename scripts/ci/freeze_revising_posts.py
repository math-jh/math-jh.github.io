#!/usr/bin/env python3
"""프로덕션 빌드 직전, 개정 중인 글을 "마지막으로 healthy했던 판본"으로 되돌린다.

발행된 글을 고칠 때의 규약은 `revising: true` + `drift_needed: true`다. `published: false`는
쓰지 않는다 — 그것만으로는 그 글이 프로덕션에서 통째로 사라져(404) 인바운드 링크·사이트맵·
검색 색인이 개정 기간 내내 깨지고, 두 키를 함께 쓰던 옛 규약에서는 대시보드·워커가 개정 중인
글을 미발행 초안으로 셌다. 이 스크립트는 CI 체크아웃(일회용 워킹트리)에서만 돌면서

    revising: true  →  마지막으로 발행 상태였던 커밋의 blob으로 교체

를 수행한다. 그래서 **이 단계가 곧 개정 중 원고의 유일한 차단막이다** — 되살릴 판본을 못 찾으면
경고가 아니라 배포를 중단한다(2026-08-17 이전에는 `published: false`가 뒤를 받치고 있었다).

를 수행하므로, dev 서버(`serve --unpublished`, 워킹트리 그대로)는 개정 중인 최신 원고를,
프로덕션은 마지막 healthy 판본을 서빙하게 된다.

되돌리는 것은 **본문뿐**이다. 레이아웃·SCSS·사이드바·terms 오버레이 같은 사이트 전역
요소는 최신 상태를 그대로 따라간다. 빌드된 _site 스냅샷을 재활용하지 않고 blob을 복원해
다시 빌드하는 이유가 이것이다.

자산(다이어그램 SVG·이미지)은 ko/en 두 글이 같은 파일을 공유하고 파일명이 글 제목으로
고정돼 있어(`assets/images/Math/<Category>/<Article>-1.svg`) 제자리 되돌리기가 위험하다.
한쪽 언어만 개정 중일 때 발행 중인 짝의 그림까지 과거로 돌아가기 때문이다. 그래서 복원된
본문이 참조하는 자산 중 **내용이 바뀐 것만** 전용 사본으로 떠서 참조를 그쪽으로 돌린다:

    assets/images/frozen/<sha8>/<경로>      ({% diagram %} 참조)
    assets/frozen/<sha8>/<경로>             (/assets/... 직접 참조)

frontmatter에는 `revising_snapshot`(판본 날짜, 글 상단 알림에 노출)과
`last_modified_at`(healthy 커밋 시각)을 주입한다. 후자가 없으면 last_modified_git 플러그인이
파일의 git log를 읽어 "오늘 수정됨"으로 표시한다. 본문은 과거인데 날짜만 오늘이 된다.

사용법:

    scripts/ci/freeze_revising_posts.py            # dry-run 보고만
    scripts/ci/freeze_revising_posts.py --apply    # 워킹트리를 실제로 고쳐씀 (CI 전용)

`--apply`는 `_posts`가 clean할 때만 동작한다. 로컬에서 실수로 돌려 개정 중인 원고를
날리는 사고를 막기 위한 것이며, CI 체크아웃은 항상 clean이라 걸리지 않는다.
(`FREEZE_ALLOW_DIRTY=1`로 이 검사를 끌 수 있지만, 버려도 되는 사본에서 동작을 확인할
때만 쓴다.)
"""

from __future__ import annotations

import argparse
import os
import re
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]

FM_RE = re.compile(r"\A---\r?\n(.*?)\r?\n---\r?\n?", re.S)
UNPUB_RE = re.compile(r"^published:\s*false\s*$", re.M)
REVISING_RE = re.compile(r"^revising:\s*true\s*$", re.M)
LASTMOD_RE = re.compile(r"^last_modified_at:", re.M)

# 본문 안의 자산 참조. (참조 문자열 전체, 자산의 repo 경로, 삽입 지점) 을 뽑는다.
DIAGRAM_RE = re.compile(r"(\{%-?\s*diagram\s+)(\S+)")
MD_ASSET_RE = re.compile(r"\]\((/assets/[^)\s]+)\)")
SRC_ASSET_RE = re.compile(r"""(?:src|href)=["'](/assets/[^"']+)["']""")

MAX_WALK = 120  # 파일당 되짚어 볼 커밋 수 상한


def git(*args: str, binary: bool = False):
    """git 호출. 실패하면 (없는 blob 등) None."""
    p = subprocess.run(
        ["git", "-C", str(ROOT), *args],
        capture_output=True,
        text=not binary,
    )
    if p.returncode != 0:
        return None
    return p.stdout


def frontmatter(text: str) -> str:
    m = FM_RE.match(text)
    return m.group(1) if m else ""


def history(path: str) -> list[tuple[str, str]]:
    """(sha, 그 커밋 시점의 경로) 목록, 최신순. rename을 따라간다."""
    out = git("log", "--follow", f"--max-count={MAX_WALK}", "--format=%x01%H", "--name-only", "--", path)
    if not out:
        return []
    entries = []
    for chunk in out.split("\x01"):
        lines = [ln for ln in chunk.splitlines() if ln.strip()]
        if len(lines) >= 2:
            entries.append((lines[0], lines[-1]))
        elif lines:  # 머지 커밋 등 이름이 안 붙는 경우 현재 경로로 시도
            entries.append((lines[0], path))
    return entries


def last_healthy(path: str):
    """마지막으로 **발행 중이고 개정 중도 아니었던** (sha, 그 시점 경로, 본문).

    `revising`까지 보는 것이 핵심이다. 판정을 `published: false` 하나로 두면, 개정 중
    표시가 한 키로 바뀐 뒤(2026-08-17)에는 지금 커밋 자체가 healthy로 잡혀 **고치는
    중인 원고가 그대로 복원된다** — 동결이 no-op이 되고 프로덕션이 초안을 띄운다.
    """
    for sha, hist_path in history(path):
        blob = git("show", f"{sha}:{hist_path}")
        if not blob:
            continue
        fm = frontmatter(blob)
        if not UNPUB_RE.search(fm) and not REVISING_RE.search(fm):
            return sha, hist_path, blob
    return None


def set_fm_keys(text: str, keys: dict[str, str]) -> str:
    """frontmatter의 키를 덮어쓰거나 없으면 추가한다."""
    m = FM_RE.match(text)
    if not m:
        raise ValueError("frontmatter 없음")
    fm, body = m.group(1), text[m.end():]
    for k, v in keys.items():
        line = f"{k}: {v}"
        pat = re.compile(rf"^{re.escape(k)}\s*:.*$", re.M)
        fm = pat.sub(line, fm) if pat.search(fm) else fm + "\n" + line
    fm = UNPUB_RE.sub("published: true", fm)
    return f"---\n{fm}\n---\n{body}"


def asset_refs(text: str, sha8: str):
    """(원본 참조 문자열, repo 상대 자산 경로, 사본 경로, 치환된 참조 문자열) 목록.

    사본 경로와 치환 참조는 반드시 같은 규칙에서 나와야 한다. 참조 종류마다 기준
    디렉토리가 다르므로(diagram 태그는 `assets/images/` 기준, 나머지는 사이트 루트
    기준) 각각의 기준 바로 아래에 `frozen/<sha8>/`을 끼워 넣는다.
    """
    refs = []
    for m in DIAGRAM_RE.finditer(text):
        pre, p = m.group(1), m.group(2)
        refs.append((m.group(0), f"assets/images/{p}", f"assets/images/frozen/{sha8}/{p}", f"{pre}frozen/{sha8}/{p}"))
    for m in list(MD_ASSET_RE.finditer(text)) + list(SRC_ASSET_RE.finditer(text)):
        url, whole = m.group(1), m.group(0)
        rest = url[len("/assets/"):]
        frozen_url = f"/assets/frozen/{sha8}/{rest}"
        refs.append((whole, f"assets/{rest}", f"assets/frozen/{sha8}/{rest}", whole.replace(url, frozen_url)))
    return refs


def freeze_assets(text: str, sha: str, apply: bool, log: list[str]) -> str:
    """복원된 본문이 참조하는 자산 중 내용이 달라진 것만 전용 사본으로 뜬다."""
    sha8 = sha[:8]
    for whole, repo_path, dest_rel, new_ref in asset_refs(text, sha8):
        old = git("show", f"{sha}:{repo_path}", binary=True)
        if old is None:
            log.append(f"      ! 당시에도 없던 자산 참조: {repo_path}")
            continue
        cur_file = ROOT / repo_path
        cur = cur_file.read_bytes() if cur_file.is_file() else None
        if cur == old:
            continue
        log.append(f"      자산 고정: {repo_path} -> {dest_rel}" + ("  (현재 삭제됨)" if cur is None else ""))
        if apply:
            dest = ROOT / dest_rel
            dest.parent.mkdir(parents=True, exist_ok=True)
            dest.write_bytes(old)
        text = text.replace(whole, new_ref)
    return text


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--apply", action="store_true", help="워킹트리를 실제로 고쳐쓴다 (CI 전용)")
    args = ap.parse_args()

    # 검사 범위는 `_posts`뿐이다. 이 가드가 지키려는 것은 커밋되지 않은 원고이고,
    # 자산 쪽은 빌드가 생성하는 파일(썸네일 등)이 있어 언제든 dirty일 수 있다.
    # 스크립트가 자산에 쓰는 것은 frozen/ 아래 새 경로뿐이라 덮어쓸 위험이 없다.
    if args.apply and not os.environ.get("FREEZE_ALLOW_DIRTY"):
        dirty = git("status", "--porcelain", "--", "_posts")
        if dirty and dirty.strip():
            print("freeze: --apply 는 _posts가 clean할 때만 동작한다. 커밋되지 않은 변경:", file=sys.stderr)
            print(dirty, file=sys.stderr)
            return 1

    tracked = (git("ls-files", "_posts") or "").splitlines()
    targets, fatal, warn = [], [], []
    for rel in tracked:
        if not rel.endswith(".md"):
            continue
        fm = frontmatter((ROOT / rel).read_text(encoding="utf-8"))
        if not REVISING_RE.search(fm):
            continue
        targets.append(rel)

    log: list[str] = []
    frozen = 0
    for rel in sorted(targets):
        found = last_healthy(rel)
        if not found:
            # 되살릴 판본이 없는데 revising 만 붙어 있으면 그 원고가 그대로 나간다.
            # `published: false` 가 이 자리를 막고 있던 시절에는 경고로 충분했다.
            if UNPUB_RE.search(frontmatter((ROOT / rel).read_text(encoding="utf-8"))):
                warn.append((rel, "revising: true 인데 발행됐던 이력이 없다 "
                                  "(published: false 가 가리고 있다 — 그냥 초안이면 revising 키를 뺄 것)"))
            else:
                fatal.append((rel, "revising: true 인데 되살릴 발행 판본이 없다 "
                                   "(발행된 적 없는 초안이면 revising 대신 published: false 를 쓴다)"))
            continue
        sha, hist_path, blob = found
        date = (git("log", "-1", "--format=%cs", sha) or "").strip()
        iso = (git("log", "-1", "--format=%cI", sha) or "").strip()
        keys = {"revising": "true", "revising_snapshot": date}
        if not LASTMOD_RE.search(frontmatter(blob)):
            keys["last_modified_at"] = iso
        text = set_fm_keys(blob, keys)
        log.append(f"  {rel}\n      판본 {sha[:8]} ({date})" + (f"  [당시 경로 {hist_path}]" if hist_path != rel else ""))
        text = freeze_assets(text, sha, args.apply, log)
        if args.apply:
            (ROOT / rel).write_text(text, encoding="utf-8")
        frozen += 1

    mode = "동결 적용" if args.apply else "dry-run"
    print(f"freeze ({mode}): revising 대상 {len(targets)}편 중 {frozen}편 동결")
    print("\n".join(log))
    for rel, why in warn:
        print(f"freeze: 경고 {rel}: {why}", file=sys.stderr)
    for rel, why in fatal:
        print(f"freeze: 중단 {rel}: {why}", file=sys.stderr)

    summary = os.environ.get("GITHUB_STEP_SUMMARY")
    if summary:
        with open(summary, "a", encoding="utf-8") as fh:
            fh.write(f"### 개정 중 글 동결 ({frozen}편)\n\n```\n" + "\n".join(log) + "\n```\n")

    return 1 if fatal else 0


if __name__ == "__main__":
    sys.exit(main())
