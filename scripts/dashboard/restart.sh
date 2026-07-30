#!/usr/bin/env bash
# 대시보드 서버 재기동. 스크립트로 감싸 두는 이유: 호출 명령줄에 서버 경로가
# 들어가면 pgrep -f 가 그 셸까지 잡아 자기 자신을 죽인다 (실제로 두 번 겪음).
set -u
DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
LOG="$HOME/.local/state/blog_dashboard.log"

for pid in $(pgrep -f "dashboard/server[.]py"); do
  [ "$pid" = "$$" ] && continue
  kill "$pid" 2>/dev/null
done
sleep 1
setsid /usr/bin/python3 "$DIR/server.py" >>"$LOG" 2>&1 < /dev/null &
sleep 2
pgrep -af "dashboard/server[.]py" | grep -v restart || { echo "기동 실패 — $LOG 확인"; exit 1; }
