#!/usr/bin/env bash
# Cron entry point for Marvin (blogdev-bot). Fires once per tick (weekly).
# 2026-07-20: tmux 상주 세션 → `claude -p` 단발 전환 (구독 과금 확인).
# 옛 tmux 드라이버는 lib.sh(함수 그대로)와
# ~/.local/share/tmux-bots-archive/blogdev-drive.sh.tmux 에 보존.
set -euo pipefail
HERE="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
# shellcheck source=lib.sh
source "$HERE/lib.sh"   # log·git_sync·CLAUDE_BIN·BLOG_ROOT 재사용 (tmux 함수 미사용)

git_sync
log "launching claude -p (sonnet) for marvin"
cd "$BLOG_ROOT"
if ! timeout 2400 "$CLAUDE_BIN" -p --model sonnet \
      --permission-mode bypassPermissions \
      "Read $HERE/marvin.md and execute it now."; then
  log "claude -p failed"
  exit 1
fi
log "marvin turn complete"
