#!/usr/bin/env bash
#
# .gitignore 히스토리 재작성 — 모든 커밋의 .gitignore 를 "현재 내용"으로 바꾼다.
# 처음부터 지금 모습이었던 것처럼 보이게 하고, 옛 버전에 적혀 있던 경로
# (Mirror_Symmetry 화이트리스트, Gromov_Witten_Theory, index-monitor,
#  reading-bot / blogdev-bot state, extract_terms.py …)를 히스토리에서 지운다.
#
# 대화형 프롬프트 없이 **두 단계**로 나뉜다:
#
#   bash ~/rewrite-gitignore-history.sh          # 1단계: 재작성 + 전수 검증까지. 푸시 안 함.
#   bash ~/rewrite-gitignore-history.sh --push   # 2단계: 검증 다시 하고 force-push + 동기화
#
# 1단계는 원격을 전혀 건드리지 않는다. 출력(특히 검증 결과)을 보고 나서 2단계를 돌리면 된다.
# 두 단계 사이에는 autopush 타이머가 멈춘 채로 있고, 2단계 끝에 되살아난다.
#
# 작업 저장소의 워킹트리는 1단계에서 전혀 건드리지 않는다 (별도 bare 클론에서 재작성).
# 2단계 마지막에 `git reset --hard origin/main` 을 하는데, tracked 내용은 재작성 전후가
# 같으므로 잃는 것이 없다. untracked/ignored 파일(GW 초안, notes/, 봇 state)도 그대로다.
#
# 되돌리기:  git -C /var/tmp/gitignore-rewrite/backup.git \
#              push --force --mirror git@github.com:math-jh/math-jh.github.io.git

set -euo pipefail

REPO="${REPO:-/home/junhyeok/math-jh.github.io}"
WORK="${WORK:-/var/tmp/gitignore-rewrite}"
BRANCH="${BRANCH:-main}"
TIMER="${TIMER:-blog-autopush.timer}"
LEAKS='Gromov_Witten_Theory|index-monitor|reading-bot|blogdev-bot|extract_terms|Mirror_Symmetry|term_extraction|translation_state|audit-report'

say()  { printf '\n\033[1m== %s\033[0m\n' "$*"; }
ok()   { printf '   \033[32m✓\033[0m %s\n' "$*"; }
die()  { printf '\n\033[31m!! %s\033[0m\n' "$*" >&2; exit 1; }

MODE="prepare"
[ "${1:-}" = "--push" ] && MODE="push"

command -v git-filter-repo >/dev/null || die "git-filter-repo 가 필요합니다 (pip install git-filter-repo)."
[ -d "$REPO/.git" ] || die "저장소를 찾을 수 없습니다: $REPO"
REMOTE=$(git -C "$REPO" remote get-url origin)

# ---------------------------------------------------------------- 검증 함수
verify() {
  local dir=$1
  local leftover
  leftover=$(git -C "$dir" log --all --full-history --format='%H' -- .gitignore \
    | while read -r c; do git -C "$dir" cat-file -p "$c:.gitignore" 2>/dev/null; done \
    | grep -cE "$LEAKS" || true)
  [ "$leftover" -eq 0 ] || die "히스토리에 민감 경로가 아직 $leftover 줄 남아 있습니다."
  ok "히스토리 전체(.gitignore 96개 버전)에서 민감 경로 0줄"

  local head
  head=$(git -C "$dir" rev-parse "$BRANCH")
  diff <(git -C "$dir" cat-file -p "$head:.gitignore") "$WORK/new_gitignore" >/dev/null \
    || die "HEAD 의 .gitignore 가 현재 파일과 다릅니다."
  ok "HEAD 의 .gitignore == 현재 $REPO/.gitignore"
  ok "커밋 수: $(git -C "$dir" rev-list --all --count)"
}

# ================================================================= 2단계
if [ "$MODE" = "push" ]; then
  [ -d "$WORK/rewrite.git" ] || die "1단계를 먼저 돌리세요 ($WORK/rewrite.git 없음)."

  say "재검증 (푸시 직전)"
  verify "$WORK/rewrite.git"

  say "force-push → $REMOTE"
  cd "$WORK/rewrite.git"
  git remote add origin "$REMOTE" 2>/dev/null || git remote set-url origin "$REMOTE"
  git push --force origin "refs/heads/*:refs/heads/*"
  git push --force origin "refs/tags/*:refs/tags/*" 2>/dev/null || true
  ok "푸시 완료"

  say "작업 저장소를 새 히스토리에 맞춤"
  cd "$REPO"
  git fetch origin
  git reset --hard "origin/$BRANCH"
  git reflog expire --expire=now --all
  git gc --prune=now --quiet
  ok "$REPO 가 새 origin/$BRANCH 와 동기화됨 (tracked 내용은 이전과 동일)"

  say "autopush 타이머 복구"
  systemctl --user start "$TIMER" && ok "$TIMER 시작"

  say "완료"
  cat <<'NOTE'
   - 백업(옛 히스토리): /var/tmp/gitignore-rewrite/backup.git
     복구:  git -C /var/tmp/gitignore-rewrite/backup.git push --force --mirror <origin>
   - GitHub Actions 가 force-push 로 다시 돌며 사이트를 재배포합니다.
   - 남는 노출: GitHub 은 도달 불가능해진 옛 객체를 한동안 보관하며, 옛 커밋 SHA 를
     아는 사람은 그걸로 접근할 수 있습니다. 완전 제거를 원하면 GitHub Support 에
     gc 를 요청하세요. 이미 clone/fork 한 사본에는 여전히 옛 히스토리가 남습니다.
NOTE
  exit 0
fi

# ================================================================= 1단계
say "0) 사전 점검"
# 2단계에서 워킹 저장소를 origin 에 맞춰 리셋하므로, 커밋되지 않은 tracked 변경이
# 있으면 사라진다. 먼저 커밋·푸시할 것. (untracked/ignored 파일은 영향 없음.)
git -C "$REPO" diff --quiet          || die "커밋되지 않은 변경이 있습니다. 먼저 커밋·푸시하세요."
git -C "$REPO" diff --cached --quiet || die "스테이징된 변경이 있습니다. 먼저 커밋·푸시하세요."
git -C "$REPO" fetch -q origin "$BRANCH"
[ -z "$(git -C "$REPO" rev-list "origin/$BRANCH..$BRANCH")" ] || die "푸시되지 않은 커밋이 있습니다."
[ -s "$REPO/.gitignore" ] || die ".gitignore 가 비어 있습니다."
if grep -qE "$LEAKS" "$REPO/.gitignore"; then die "현재 .gitignore 에 아직 민감 경로가 있습니다."; fi
ok "워킹트리 깨끗, origin/$BRANCH 와 동기화, 현재 .gitignore 깨끗"

say "1) autopush 정지 (재작성·푸시 중 동시 커밋 방지)"
systemctl --user stop "$TIMER"
ok "$TIMER 정지 — 2단계(--push)가 끝나면 자동으로 복구됩니다"

say "2) bare 클론 + 백업"
rm -rf "$WORK"; mkdir -p "$WORK"
git clone --bare "$REMOTE" "$WORK/rewrite.git"
cp -a "$WORK/rewrite.git" "$WORK/backup.git"
cp "$REPO/.gitignore" "$WORK/new_gitignore"
ok "백업: $WORK/backup.git"

say "3) 역대 .gitignore 블롭 수집"
before=$(git -C "$WORK/rewrite.git" log --all --full-history --format='%H' -- .gitignore \
  | while read -r c; do git -C "$WORK/rewrite.git" cat-file -p "$c:.gitignore" 2>/dev/null; done \
  | grep -cE "$LEAKS" || true)
git -C "$WORK/rewrite.git" log --all --full-history --format='%H' -- .gitignore \
  | while read -r c; do git -C "$WORK/rewrite.git" rev-parse -q --verify "$c:.gitignore" || true; done \
  | sort -u > "$WORK/blob_ids.txt"
n=$(wc -l < "$WORK/blob_ids.txt")
[ "$n" -gt 0 ] || die ".gitignore 블롭을 찾지 못했습니다."
ok "고유 블롭 $n 개 / 재작성 전 민감 경로 $before 줄"

say "4) 히스토리 재작성 (커밋 메시지·작성자·시각은 보존)"
cat > "$WORK/cb.py" <<PYEOF
if "_GI" not in globals():
    globals()["_GI"] = set(
        line.strip() for line in open("$WORK/blob_ids.txt") if line.strip()
    )
    globals()["_NEW"] = open("$WORK/new_gitignore", "rb").read()
_id = blob.original_id
if isinstance(_id, bytes):
    _id = _id.decode()
if _id in globals()["_GI"]:
    blob.data = globals()["_NEW"]
PYEOF
cd "$WORK/rewrite.git"
git filter-repo --force --blob-callback "$(cat "$WORK/cb.py")"
ok "재작성 완료"

say "5) 전수 검증"
verify "$WORK/rewrite.git"

say "1단계 끝 — 원격은 아직 그대로입니다"
cat <<NOTE

   위 검증이 모두 ✓ 이면 아래로 푸시하세요 (이 명령이 다시 검증한 뒤 밀고,
   작업 저장소를 동기화하고, autopush 타이머를 되살립니다):

       bash ~/rewrite-gitignore-history.sh --push

   그만두려면 (원격은 손대지 않았으므로 그냥 정리만 하면 됩니다):

       rm -rf $WORK && systemctl --user start $TIMER
NOTE
