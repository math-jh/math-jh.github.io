#!/usr/bin/env bash
#
# .claude/ 를 히스토리 전체에서 제거한다 (파일 자체를 없애는 filter-repo --invert-paths).
# CLAUDE.md 는 예전 purge 때 이미 지워졌는데 .claude/settings.json 이 남아 있었다.
#
# 전제: 먼저 `git rm -r --cached .claude` 를 커밋·푸시해 HEAD 에서 빠져 있어야 한다.
#       (그래야 마지막 `git reset --hard` 가 디스크의 .claude/ 를 지우지 않는다 —
#        untracked 파일은 건드리지 않으므로.)
#
# 비대화형 2단계:
#   bash ~/purge-claude-history.sh          # 재작성 + 전수 검증까지. 푸시 안 함.
#   bash ~/purge-claude-history.sh --push   # 재검증 → force-push → 동기화 → 타이머 복구
#
# 되돌리기:  git -C /var/tmp/claude-purge/backup.git \
#              push --force --mirror git@github.com:math-jh/math-jh.github.io.git

set -euo pipefail

REPO="${REPO:-/home/junhyeok/math-jh.github.io}"
WORK="${WORK:-/var/tmp/claude-purge}"
BRANCH="${BRANCH:-main}"
TIMER="${TIMER:-blog-autopush.timer}"
TARGET=".claude"

say() { printf '\n\033[1m== %s\033[0m\n' "$*"; }
ok()  { printf '   \033[32m✓\033[0m %s\n' "$*"; }
die() { printf '\n\033[31m!! %s\033[0m\n' "$*" >&2; exit 1; }

MODE="prepare"; [ "${1:-}" = "--push" ] && MODE="push"

command -v git-filter-repo >/dev/null || die "git-filter-repo 가 필요합니다."
[ -d "$REPO/.git" ] || die "저장소를 찾을 수 없습니다: $REPO"
REMOTE=$(git -C "$REPO" remote get-url origin)

verify() {
  local dir=$1 n
  n=$(git -C "$dir" log --all --oneline -- "$TARGET" | wc -l)
  [ "$n" -eq 0 ] || die "히스토리에 $TARGET 을 건드린 커밋이 아직 $n 개 있습니다."
  ok "히스토리 전체에서 $TARGET 커밋 0개"

  n=$(git -C "$dir" ls-tree -r --name-only "$BRANCH" | grep -c "^$TARGET/" || true)
  [ "$n" -eq 0 ] || die "HEAD 트리에 $TARGET 파일이 $n 개 남아 있습니다."
  ok "HEAD 트리에 $TARGET 없음"
  ok "커밋 수: $(git -C "$dir" log --all --oneline | wc -l)"
}

if [ "$MODE" = "push" ]; then
  [ -d "$WORK/rewrite.git" ] || die "1단계를 먼저 돌리세요 ($WORK/rewrite.git 없음)."

  say "재검증 (푸시 직전)"; verify "$WORK/rewrite.git"

  say "force-push → $REMOTE"
  cd "$WORK/rewrite.git"
  git remote add origin "$REMOTE" 2>/dev/null || git remote set-url origin "$REMOTE"
  git push --force origin "refs/heads/*:refs/heads/*"
  ok "푸시 완료"

  say "작업 저장소 동기화"
  cd "$REPO"
  git fetch origin
  git reset --hard "origin/$BRANCH"
  git reflog expire --expire=now --all
  git gc --prune=now --quiet
  ok "동기화 완료 — 디스크의 .claude/ 는 untracked 라 그대로 남습니다"
  [ -f "$REPO/.claude/settings.json" ] && ok ".claude/settings.json 디스크에 살아있음" \
    || printf '   \033[31m!!\033[0m .claude/settings.json 이 사라졌습니다 — 백업에서 복구하세요\n'

  say "autopush 타이머 복구"; systemctl --user start "$TIMER" && ok "$TIMER 시작"
  say "완료 — 백업: $WORK/backup.git"
  exit 0
fi

say "0) 사전 점검"
git -C "$REPO" diff --quiet          || die "커밋되지 않은 변경이 있습니다."
git -C "$REPO" diff --cached --quiet || die "스테이징된 변경이 있습니다."
git -C "$REPO" fetch -q origin "$BRANCH"
[ -z "$(git -C "$REPO" rev-list "origin/$BRANCH..$BRANCH")" ] || die "푸시되지 않은 커밋이 있습니다."
n=$(git -C "$REPO" ls-files "$TARGET" | wc -l)
[ "$n" -eq 0 ] || die "$TARGET 이 아직 추적 중입니다($n개). 먼저 'git rm -r --cached $TARGET' 를 커밋·푸시하세요."
ok "워킹트리 깨끗, origin/$BRANCH 동기화, $TARGET 추적 해제됨"

say "1) autopush 정지"
systemctl --user stop "$TIMER"
ok "$TIMER 정지 — 2단계(--push) 끝에 복구됩니다"

say "2) bare 클론 + 백업"
rm -rf "$WORK"; mkdir -p "$WORK"
git clone --bare "$REMOTE" "$WORK/rewrite.git"
cp -a "$WORK/rewrite.git" "$WORK/backup.git"
ok "백업: $WORK/backup.git"
before=$(git -C "$WORK/rewrite.git" log --all --oneline -- "$TARGET" | wc -l)
ok "재작성 전 $TARGET 커밋: $before 개 / 전체 $(git -C "$WORK/rewrite.git" log --all --oneline | wc -l)"

say "3) 히스토리에서 $TARGET 제거 (커밋 메시지·작성자·시각 보존)"
cd "$WORK/rewrite.git"
git filter-repo --force --invert-paths --path "$TARGET"
ok "재작성 완료"

say "4) 전수 검증"; verify "$WORK/rewrite.git"

say "1단계 끝 — 원격은 아직 그대로입니다"
cat <<NOTE

   위가 모두 ✓ 이면:
       bash ~/purge-claude-history.sh --push

   그만두려면 (원격 무손상):
       rm -rf $WORK && systemctl --user start $TIMER
NOTE
