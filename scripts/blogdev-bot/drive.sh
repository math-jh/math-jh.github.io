#!/usr/bin/env bash
# Cron entry point for Marvin (blogdev-bot). Fires daily 10:05; most days the
# mechanical gate below exits before any model is spawned.
# 2026-07-20: tmux 상주 세션 → `claude -p` 단발 전환 (구독 과금 확인).
# 옛 tmux 드라이버는 lib.sh(함수 그대로)와
# ~/.local/share/tmux-bots-archive/blogdev-drive.sh.tmux 에 보존.
set -euo pipefail
HERE="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
# shellcheck source=lib.sh
source "$HERE/lib.sh"   # log·git_sync·CLAUDE_BIN·BLOG_ROOT 재사용 (tmux 함수 미사용)

git_sync

# 기계 게이트 — 새 `[dev]` 커밋이 없으면 LLM을 아예 띄우지 않는다. 예전에는 이
# 판정을 모델이 했으므로, 쓸 게 없는 날도 세션 하나를 온전히 태웠다. 매일 돌리는
# 이상 그 헛턴이 대부분의 날이 된다.
#   exit 0 = 큐에 작업 있음 / 3 = 없음 / 그 외 = 오류
set +e
"$HERE/dev_queue.py" >/dev/null
gate_rc=$?
set -e
case "$gate_rc" in
  0) log "새 [dev] 커밋 있음 — marvin 기동" ;;
  3) log "새 [dev] 커밋 없음 — LLM 호출 없이 종료"; exit 0 ;;
  *) log "dev_queue.py 오류 (rc=$gate_rc) — 중단"; exit 1 ;;
esac

log "launching claude -p (sonnet) for marvin"
cd "$BLOG_ROOT"
# 모델을 띄우기 전 워크숍 경로의 dirty 목록. 실행 후 이 목록에 없는 것만 봇
# 산출물로 보고 커밋한다 — 사용자가 편집 중이던 글을 봇 커밋에 넣지 않는다.
BEFORE_DIRTY="$(mktemp)"
# 집필 턴의 보고(필요한 화면, 제목·excerpt 어긋남 등). 편집 턴이 읽고 처리할 수
# 있는 것은 처리하고, 나머지를 '사용자가 정할 것'으로 넘긴다 (editor.md 6번).
WRITE_REPORT="$(mktemp)"
trap 'rm -f "$BEFORE_DIRTY" "$WRITE_REPORT"' EXIT
"$HERE/commit_posts.py" --snapshot "$BEFORE_DIRTY"
# 2026-08-08: ~/.claude/settings.json 에 advisorModel(fable)이 전역 기본값으로
# 들어갔다. 부착 조건이 base_rank <= advisor_rank 라 sonnet(3) 세션인 marvin 도
# fable(5) 상담이 붙는다. cron 잡은 research 파이프라인의 researcher 하나만
# advisor 를 쓰기로 했으므로 여기서는 끈다. 이 env 가 유일하게 확실한 off 다
# (게이트 함수의 첫 검사라 settings 의 advisorModel 보다 먼저 short-circuit).
export CLAUDE_CODE_DISABLE_ADVISOR_TOOL=1
if ! timeout 2400 "$CLAUDE_BIN" -p --model sonnet \
      --permission-mode bypassPermissions \
      "[cron] Read $HERE/marvin.md and execute it now." \
      | tee "$WRITE_REPORT"; then
  log "claude -p failed"
  exit 1
fi
log "marvin turn complete"

# 편집 턴 — 집필 턴이 워크숍 글을 남겼으면 다른 모델이 그 글을 독자로서 다시 읽고
# 구성을 고친다(editor.md). 집필 턴은 diff 를 보며 쓰므로 diff 에 있던 것을 다
# 받아 적고 새 일을 뒤에 덧붙인다. 편집 턴은 그 diff 를 보지 않는다.
# 편집이 끊기거나 front matter 를 건드리면 edit_guard.py 가 집필 턴의 판본으로
# 되돌리므로, 편집 턴이 어떻게 끝나든 커밋되는 것은 온전한 글이다.
EDIT_STORE="$(mktemp -d)"
EDIT_REPORT="$(mktemp)"
trap 'rm -rf "$BEFORE_DIRTY" "$WRITE_REPORT" "$EDIT_STORE" "$EDIT_REPORT"' EXIT
# edit_guard.py 가 죽어도 드라이버는 계속 간다 — 편집을 건너뛸 뿐 커밋은 해야 한다.
EDIT_TARGETS="$("$HERE/edit_guard.py" --save "$EDIT_STORE" --before "$BEFORE_DIRTY" | tr '\n' ' ' || true)"
if [ -n "${EDIT_TARGETS// /}" ]; then
  log "launching claude -p (opus) for editor: $EDIT_TARGETS"
  # 보고는 run.log 에 그대로 찍고, 끝의 '사용자가 정할 것:'(editor.md 6번)은
  # editor_report.py 가 읽어 알림으로 보낸다. 사용자는 run.log 를 읽지 않는다.
  if timeout 2400 "$CLAUDE_BIN" -p --model opus \
        --permission-mode bypassPermissions \
        "[cron] Read $HERE/editor.md and execute it now. 대상 글: $EDIT_TARGETS 집필 턴 보고: $WRITE_REPORT" \
        | tee "$EDIT_REPORT"; then
    "$HERE/edit_guard.py" --check "$EDIT_STORE" 2>&1 | while read -r line; do
      log "$line"
    done || true
    log "editor turn complete"
    # shellcheck disable=SC2086  # 대상 글 경로는 공백 없는 목록
    "$HERE/editor_report.py" "$EDIT_REPORT" $EDIT_TARGETS 2>&1 | while read -r line; do
      log "$line"
    done || true
  else
    "$HERE/edit_guard.py" --restore "$EDIT_STORE" 2>&1 | while read -r line; do
      log "$line"
    done || true
    log "editor turn failed — 집필 턴의 글을 그대로 커밋한다"
    # 편집 턴이 집필 보고를 처리하지 못했으므로 그 보고를 그대로 사용자에게 넘긴다.
    # shellcheck disable=SC2086
    "$HERE/editor_report.py" --editor-failed "$WRITE_REPORT" $EDIT_TARGETS 2>&1 | while read -r line; do
      log "$line"
    done || true
  fi
fi

# 자기 산출물은 자기 이름(author=Marvin)으로 커밋한다. push 는 autopush 몫.
"$HERE/commit_posts.py" --before "$BEFORE_DIRTY" 2>&1 | while read -r line; do
  log "$line"
done
