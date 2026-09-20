#!/usr/bin/env python3
"""retire_en_reviewed — KO 가 검토를 마친 EN 링크에서 `reviewed=""` 를 회수한다.

판정의 정본은 KO 다. EN 은 그 번역이므로 같은 출현에 대해 사람이 두 번 판단할
이유가 없고, 실제로 두 번 판단한 결과가 66건에서 갈렸다. 그래서 EN 링크는
`data-lid` 로 KO 의 완료를 상속하고, 자기 마커는 갖지 않는다.

회수 조건은 상속 조건과 **같다**: 그 EN 링크에 lid 가 있고, 같은 lid 를 가진 KO
링크가 `reviewed` 일 때만 뗀다. 둘을 같게 두었으므로 어느 시점에 멈춰도
"모든 EN 링크는 자기 마커로든 상속으로든 완료"가 유지된다 — 아직 lid 를 못 받은
링크는 마커를 그대로 갖고 있다가, link_pair_llm 이 lid 를 채운 뒤 다음 스윕에서
회수된다. 그래서 이 스크립트는 여러 번 돌려도 되고, 돌릴수록 줄어든다.
"""
from __future__ import annotations

import argparse
import os
import sys
import tempfile
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT / "scripts" / "dependency-classifier"))
sys.path.insert(0, str(ROOT / "scripts" / "lib"))
import link_ids as L  # noqa: E402
from blog_file_lock import try_acquire_file_locks  # noqa: E402
from cron_commit import commit_outputs  # noqa: E402

depc = L.depc


def ko_twin(en_path: Path) -> Path | None:
    """EN 글의 KO 짝. 날짜 접두가 서로 다르므로 Base 이름으로 찾는다."""
    base = en_path.name.split("-", 3)[-1]
    found = sorted((en_path.parent.parent / "ko").glob(f"*-{base}"))
    return found[0] if len(found) == 1 else None


def ko_reviewed(path: Path) -> set[str]:
    text = path.read_text(encoding="utf-8")
    done = set()
    for link in L.all_links(path, text):
        if link.reviewed:
            lid = depc.link_lid(text, link)
            if lid:
                done.add(lid)
    return done


def plan(en_path: Path, done: set[str]) -> tuple[str, str, int]:
    text = en_path.read_text(encoding="utf-8")
    edits = []
    for link in L.all_links(en_path, text):
        if not link.reviewed or link.ial_start is None:
            continue
        lid = depc.link_lid(text, link)
        if not lid or lid not in done:
            continue
        ial = text[link.ial_start:link.ial_end]
        edits.append((link.ial_start, link.ial_end,
                      depc.REVIEWED_ATTR_RE.sub("", ial)))
    new = text
    for start, end, replacement in sorted(edits, reverse=True):
        new = new[:start] + replacement + new[end:]
    return text, new, len(edits)


def gate(en_path: Path, old: str, new: str) -> str | None:
    """마커 말고는 아무것도 안 건드렸는가."""
    if depc.REVIEWED_ATTR_RE.sub("", old) != depc.REVIEWED_ATTR_RE.sub("", new):
        return "마커 외 변경"
    if depc.hard_lint(en_path, new) - depc.hard_lint(en_path, old):
        return "lint 악화"
    return None


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--apply", action="store_true")
    ap.add_argument("--quiet", action="store_true")
    ap.add_argument("paths", nargs="*", help="EN 글 경로 — 생략하면 전 코퍼스")
    args = ap.parse_args()

    if args.paths:
        # 호출자가 방금 고친 글만 준 경우. 회수 조건은 그 글의 lid 나 KO 의
        # reviewed 가 바뀔 때만 새로 성립하므로, 무관한 400여 편을 다시 훑지 않는다.
        targets = [ROOT / p if not os.path.isabs(p) else Path(p) for p in args.paths]
    else:
        targets = sorted((ROOT / "_posts" / "Math").rglob("*.md"))

    files = retired = 0
    left = 0
    written: list[str] = []
    refused: list[tuple[str, str]] = []
    for en_path in targets:
        if en_path.parent.name != "en":
            continue
        twin = ko_twin(en_path)
        done = ko_reviewed(twin) if twin else set()
        old, new, n = plan(en_path, done)
        text_left = sum(1 for link in L.all_links(en_path, old) if link.reviewed) - n
        left += max(0, text_left)
        if not n:
            continue
        why = gate(en_path, old, new)
        if why:
            refused.append((str(en_path.relative_to(ROOT)), why))
            continue
        files += 1
        retired += n
        if args.apply:
            lease = try_acquire_file_locks([en_path])
            if lease is None:
                refused.append((str(en_path.relative_to(ROOT)), "락 실패"))
                continue
            try:
                mode = os.stat(en_path).st_mode & 0o7777
                fd, tmp = tempfile.mkstemp(prefix=".retire.", suffix=".tmp",
                                           dir=str(en_path.parent))
                with os.fdopen(fd, "w", encoding="utf-8") as handle:
                    handle.write(new)
                os.chmod(tmp, mode)
                os.replace(tmp, en_path)
            finally:
                lease.release()
            written.append(str(en_path.relative_to(ROOT)))

    if written:
        commit_outputs("Link Review Marker Retire", written,
                       "\n".join(f"- {p}" for p in written), log=print)
    if not args.quiet or retired or refused:
        verb = "회수" if args.apply else "회수 예정"
        print(f"{verb} {retired}개 / {files}편 · KO 완료를 아직 못 받은 EN 마커 {left}개")
        for path, why in refused:
            print(f"  거절 {path} — {why}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
