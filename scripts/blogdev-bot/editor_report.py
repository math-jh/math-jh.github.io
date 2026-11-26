#!/usr/bin/env python3
"""편집 턴 보고의 '사용자가 정할 것'을 사용자에게 알림으로 보낸다.

drive.sh 가 편집 턴(`claude -p`, editor.md)의 출력을 파일로 받아 두고 이 스크립트에
넘긴다. 보고는 run.log 에만 남고 사용자는 그 로그를 읽지 않으므로, 정할 것이 있으면
여기서 `notify --digest` 로 보낸다(HUD 에는 바로, 폰에는 다음 날 하루 요약으로).

보고 끝의 꼴은 editor.md 6번이 정한다:

    사용자가 정할 것: 없음

    사용자가 정할 것:
    - <글 파일 이름>: <정할 것>

그 줄이 없으면 보고의 꼬리를 대신 보낸다. 꼴이 어긋났다는 이유로 정할 것이 조용히
묻히지 않게 하려는 것이다.

편집 턴은 집필 턴(marvin.md)의 보고를 읽어 필요한 화면 같은 요청을 먼저 처리해 보고,
못 한 것만 정할 것으로 넘긴다. 편집 턴이 실패로 끝나면 그 처리가 없었으므로
`--editor-failed` 로 집필 턴의 보고 꼬리를 그대로 보낸다.

출력은 drive.sh 가 run.log 에 한 줄씩 찍는다. 알림 전송이 실패한 경우에만 'failed'
를 쓴다(대시보드 '개발 노트 봇' 카드의 오류 불).

    editor_report.py <편집 턴 보고 파일> <대상 글 경로>...
    editor_report.py --editor-failed <집필 턴 보고 파일> <대상 글 경로>...
"""
import argparse
import re
import subprocess
import sys
from pathlib import Path

NOTIFY = Path.home() / ".local/bin/notify"
MARKER_RE = re.compile(r"^\s*(?:[-*]\s*)?(?:\*\*)?사용자가 정할 것(?:\*\*)?\s*:\s*(?:\*\*)?\s*(.*)$")
NONE_RE = re.compile(r"^(?:없음|없습니다)")
ITEM_RE = re.compile(r"^\s*[-*]\s+\S")
BODY_MAX = 1400
TAIL_CHARS = 800


def post_name(path: str) -> str:
    """`_posts/.../2026-11-22-Share_Buttons.md` → `Share_Buttons`."""
    return re.sub(r"^\d{4}-\d{2}-\d{2}-", "", Path(path).stem)


def decisions(report: str):
    """(찾음 여부, 정할 것 본문). 본문이 비면 정할 것이 없다는 뜻이다."""
    lines = report.splitlines()
    for i in range(len(lines) - 1, -1, -1):
        m = MARKER_RE.match(lines[i])
        if not m:
            continue
        inline, below = m.group(1).strip(), lines[i + 1:]
        if NONE_RE.match(inline) and not any(ITEM_RE.match(ln) for ln in below):
            return True, ""
        return True, "\n".join([inline] + below).strip()
    return False, ""


def send(subject: str, body: str) -> bool:
    if len(body) > BODY_MAX:
        body = body[:BODY_MAX] + "…"
    cmd = [str(NOTIFY), "-s", subject, "-b", body, "-g", "blog/worker", "--digest"]
    try:
        r = subprocess.run(cmd, capture_output=True, text=True, timeout=20)
    except Exception as e:  # noqa: BLE001
        print(f"decisions: notify failed ({e})")
        return False
    if r.returncode != 0:
        print(f"decisions: notify failed rc={r.returncode} {r.stderr.strip()[:200]}")
        return False
    return True


def tail_of(report: str) -> str:
    return report.strip()[-TAIL_CHARS:] or "(출력 없음)"


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--editor-failed", action="store_true",
                    help="편집 턴이 실패했다. 보고 파일은 집필 턴의 것이다")
    ap.add_argument("report", type=Path)
    ap.add_argument("targets", nargs="*")
    args = ap.parse_args()
    report = args.report.read_text(encoding="utf-8", errors="replace") if args.report.is_file() else ""
    names = ", ".join(post_name(p) for p in args.targets) or "대상 글 미상"

    if args.editor_failed:
        body = ("편집 턴이 끝나지 못해 집필 턴 보고를 처리하지 못했다. 글은 집필 턴의 판본으로 "
                "커밋된다. 집필 턴 보고 끝부분:\n\n" + tail_of(report))
        if send(f"개발 노트 봇 · 편집 턴 실패 ({names})", body):
            print("decisions: 편집 턴 실패 → 집필 턴 보고 꼬리를 하루 요약으로")
        return 0

    found, body = decisions(report)
    if found and not body:
        print("decisions: 없음")
        return 0
    if found:
        if send(f"개발 노트 봇 · 정할 것 ({names})", body):
            print(f"decisions: {len(body.splitlines())}줄 → 하루 요약")
        return 0
    body = "편집 턴 보고에 '사용자가 정할 것:' 줄이 없다. 보고 끝부분:\n\n" + tail_of(report)
    if send(f"개발 노트 봇 · 편집 보고 꼴 어긋남 ({names})", body):
        print("decisions: '사용자가 정할 것' 줄 없음 → 보고 꼬리를 하루 요약으로")
    return 0


if __name__ == "__main__":
    sys.exit(main())
