#!/usr/bin/env python3
"""판본 비교기 메모 CLI — 지시서를 반영한 세션이 자기가 처리한 메모를 지운다.

메모는 브라우저가 아니라 이 Pi 에 있다 (`~/.local/state/blog_dashboard_review.json`).
그래서 지시서를 받은 세션이 반영을 끝낸 뒤 여기서 지워 줘야 사용자가 다음 메모를
깨끗한 상태에서 시작한다.

**id 로 지운다.** 글 단위로 싹 지우면 지시서를 복사한 뒤에 새로 적힌 메모까지
날아간다 — 사용자가 검토를 계속하는 동안 세션이 도는 게 정상이므로 그 사고가 실제로
난다.

사용법:
    notes_cli.py --list [<글 경로>]
    notes_cli.py --del n123 n456 …      지시서 끝에 실린 id 를 그대로
    notes_cli.py --done n123 n456 …     지우지 않고 '처리함' 으로만
"""

from __future__ import annotations

import argparse
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import compare as C  # noqa: E402


def main() -> None:
    ap = argparse.ArgumentParser(description=__doc__,
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--list", nargs="?", const="", metavar="PATH", help="메모 목록")
    ap.add_argument("--del", dest="delete", nargs="+", metavar="ID", help="메모 삭제")
    ap.add_argument("--done", nargs="+", metavar="ID", help="처리함으로 표시")
    args = ap.parse_args()

    state = C.review_state()
    notes = state["notes"]

    if args.list is not None:
        rows = [n for n in notes if not args.list or n.get("path") == args.list]
        for n in rows:
            where = " · ".join(x for x in (n.get("heading"), n.get("label")) if x)
            print(f"{n['id']}\t{n.get('status','open')}\t{n['path']}\t{where}\t"
                  f"{n['text'][:60]}")
        print(f"— {len(rows)}건", file=sys.stderr)
        return

    ids = args.delete or args.done or []
    if not ids:
        ap.print_help()
        raise SystemExit(2)

    known = {n["id"] for n in notes}
    missing = [i for i in ids if i not in known]
    hit = [i for i in ids if i in known]
    for i in hit:
        C.review_update({"kind": "note-del" if args.delete else "note-done",
                         "id": i, "status": "done"})
    verb = "삭제" if args.delete else "처리함 표시"
    print(f"{verb} {len(hit)}건" + (f" · 없는 id {len(missing)}건: {' '.join(missing)}"
                                    if missing else ""))


if __name__ == "__main__":
    main()
