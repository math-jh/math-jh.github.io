#!/usr/bin/env bash
# Cron entry point for Marvin (reading-bot). Fires once per tick.
set -euo pipefail
HERE="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
# shellcheck source=lib.sh
source "$HERE/lib.sh"

cleanup_bot_sessions
ensure_session
git_sync
prep_marvin
send_line "Read $HERE/marvin.md and execute it now."
log "injected marvin prompt"
