---

title: "공개 저장소의 히스토리 재작성"
excerpt: "옛 .gitignore 판본이 미발행 디렉토리 이름을 흘리고 있었다. 모든 판본을 현재 내용으로 되감고 .claude는 경로째 들어냈으며, 그 여파로 끊긴 커밋 링크는 GitHub에 남은 옛 객체로 되짚었다"

read_time: false

categories: [Misc / LLM Workshop]
permalink: /ko/llm_workshop/history_rewrite

sidebar:
    nav: "llm_workshop-ko"

author: Marvin

date: 2026-08-29
weight: 45
group: backend

---

관련 파일: [`scripts/rewrite-gitignore-history.sh`](https://github.com/math-jh/math-jh.github.io/blob/main/scripts/rewrite-gitignore-history.sh), [`scripts/purge-claude-history.sh`](https://github.com/math-jh/math-jh.github.io/blob/main/scripts/purge-claude-history.sh), [`.gitignore`](https://github.com/math-jh/math-jh.github.io/blob/main/.gitignore), [커밋](https://github.com/math-jh/math-jh.github.io/commit/154abed1)
{: .notice--info}

이 저장소는 공개다. 그러면 `.gitignore`도 공개고, 그 파일의 모든 옛 판본도 공개다. `git log -p -- .gitignore` 한 줄이면 지금까지 이 파일이 무엇을 무시해 왔는지가 전부 나온다. 문제는 그 목록이 커밋된 적 없는 경로의 이름까지 담고 있었다는 것이다.

## 옛 .gitignore 판본이 흘리던 목록

옛 `.gitignore` 판본에는 사용자가 연구 스트림으로 쓰던 카테고리인 `_posts/Math/Gromov_Witten_Theory/`와 `_posts/Math/Mirror_Symmetry/` 등을 무시하라는 규칙과 `scripts/index-monitor/`, `reading-bot`와 `blogdev-bot`의 state 파일, `extract_terms.py`, `translation_state.json`, `audit-report.md`가 적혀 있었다. 규칙에 걸린 파일은 저장소에 들어가지 않았지만, 무시 규칙에 이름이 있다는 것은 그런 것이 존재한다는 사실을 히스토리에 남긴다. 미발행 연구 스트림이 있다는 것, 색인 모니터와 여러 봇이 돈다는 것 정도는 `.gitignore` 한 파일의 diff를 훑는 것으로 알 수 있었다.

방향은 `.gitignore`와 `.git/info/exclude`의 머리 주석에 적혀 있다. 공개 저장소에 남는 `.gitignore`에는 공개해도 무해한 일반 규칙만 두고, 로컬 전용 경로는 커밋되지 않는 `.git/info/exclude`로 옮긴다. 이 파일은 클론에 따라오지 않아서, 다른 기계에서 작업하려면 그 내용을 새 클론의 `.git/info/exclude`로 손으로 복사해야 한다. 안 하면 `git add -A`가 미발행 스트림을 커밋한다는 경고가 파일 머리에 있다. 옮기는 김에 죽은 규칙 하나도 버렸다. 옛 `.gitignore`의 `dir/**` + `!dir/ko/` 화이트리스트는 `**`가 하위 파일을 전부 다시 잡는 바람에 실제로는 아무것도 되살리지 못했다.

그러면 할 일이 둘로 갈린다. 현재 `.gitignore`를 새로 쓰는 것은 평범한 커밋 하나로 끝나지만, 이미 밀어 둔 옛 판본이 계속 흘리는 것은 히스토리를 다시 쓰지 않으면 멈추지 않는다. 뒤엣것을 두 스크립트가 맡는다.

## filter-repo의 두 갈래

두 스크립트는 `git filter-repo`를 쓰지만 대상 파일의 성격이 달라 방식이 갈린다.

`.claude/`는 어느 커밋에도 있으면 안 되는 경로다. `purge-claude-history.sh`는 경로째 들어낸다.

```bash
git filter-repo --force --invert-paths --path "$TARGET"
```
{: data-filename="scripts/purge-claude-history.sh · 일부 발췌"}

`.gitignore`는 그럴 수 없다. git이 모든 커밋에서 이 파일을 기대하고, 이 파일이 없는 옛 체크아웃은 아무것도 무시하지 않게 된다. 경로는 그대로 두고 내용만 되감는다. 먼저 역대 `.gitignore` 블롭 ID를 전부 모은다.

```bash
git -C "$WORK/rewrite.git" log --all --full-history --format='%H' -- .gitignore \
  | while read -r c; do git -C "$WORK/rewrite.git" rev-parse -q --verify "$c:.gitignore" || true; done \
  | sort -u > "$WORK/blob_ids.txt"
```
{: data-filename="scripts/rewrite-gitignore-history.sh · 일부 발췌"}

`.gitignore`를 건드린 커밋을 모든 ref에서 찾고, 커밋마다 그 시점의 `.gitignore`가 가리키는 블롭 ID를 `rev-parse`로 뽑는다. `--full-history`는 경로로 이력을 좁힐 때 git이 기본으로 건너뛰는 곁가지 커밋까지 보게 한다. 파일을 지운 커밋에서는 `rev-parse`가 실패하므로 `|| true`로 넘기고, 내용이 같은 판본은 같은 블롭이므로 `sort -u`로 중복을 걷는다.

ID를 먼저 모으는 것은 filter-repo의 blob-callback이 블롭마다 불리면서도 그 블롭이 어느 경로의 내용인지는 알려 주지 않기 때문이다. 콜백은 이 ID로 `.gitignore`의 옛 판본을 알아보고, 그 데이터를 현재 파일 내용으로 바꿔치운다.

```python
_id = blob.original_id
if isinstance(_id, bytes):
    _id = _id.decode()
if _id in globals()["_GI"]:
    blob.data = globals()["_NEW"]
```
{: data-filename="scripts/rewrite-gitignore-history.sh · blob-callback 일부 발췌"}

`_GI`는 앞에서 모은 ID 집합이고 `_NEW`는 현재 `.gitignore`의 바이트다. 콜백 본문은 블롭마다 다시 실행되므로, 이 둘은 첫 호출에서 한 번만 읽어 `globals()`에 둔다. 원래 ID가 집합에 없는 블롭은 그대로 지나간다.

결과적으로 모든 판본의 `.gitignore`가 재작성 시점의 HEAD와 바이트 단위로 같아진다. 재작성 직후의 `git log -p -- .gitignore`에는 diff가 거의 남지 않았고, 남은 것에도 로컬 경로는 없었다. 커밋 메시지, 작성자, 시각은 건드리지 않는다. blob-callback은 블롭 내용만 다시 쓴다. 그래서 히스토리 속 `.gitignore`는 스크립트 머리 주석이 적은 대로 처음부터 이 모습이었던 것처럼 보인다.

## 프롬프트 없는 2단계와 전수 검증

두 스크립트 모두 대화형 프롬프트를 두지 않고 두 단계로 나뉜다. 인자 없이 돌리면 1단계(`prepare`), `--push`를 붙이면 2단계다. `prepare`는 autopush 타이머를 멈추고, 원격을 bare 클론하고, 그 클론을 `backup.git`으로 한 번 더 복사하고, 클론 안에서 재작성한 뒤 검증까지 하고 멈춘다. 원격은 손대지 않는다. `--push`는 검증을 다시 돌리고, `git push --force`로 밀고, 작업 저장소를 `git fetch && git reset --hard origin/$BRANCH`로 새 히스토리에 맞추고, `git gc --prune=now`, 그리고 타이머를 되살린다. `prepare`는 시작하기 전에 작업 저장소에 커밋되지 않은 변경이나 푸시되지 않은 커밋이 있으면 멈춘다. 2단계의 `git reset --hard`가 그것들을 지우기 때문이다.

단계를 쪼갠 이유는 이 스크립트가 TTY 없는 헤드리스 세션에서 돈다는 것이다. 되돌릴 수 없는 force-push 앞에서 사람이 1단계 출력, 특히 검증 결과를 읽을 자리가 있어야 한다. 타이머를 멈추는 이유는 autopush가 두 시간마다 커밋을 얹기 때문이다. 재작성 중에 커밋 하나가 옛 히스토리 위에 떨어지면 force-push에서 그대로 사라진다.

검증은 표본 점검이 아니라 전수다. `.claude` 쪽은 `git log --all -- .claude`가 0건이고 HEAD 트리에 `.claude/` 항목이 없어야 통과다. `.gitignore` 쪽은 역대 `.gitignore` 블롭을 전부 풀어서 민감 경로 정규식(`Gromov_Witten_Theory|index-monitor|reading-bot|blogdev-bot|extract_terms|Mirror_Symmetry|term_extraction|translation_state|audit-report`)에 0줄이 걸려야 하고, HEAD의 `.gitignore`가 현재 작업 파일과 `diff`로 완전히 같아야 한다.

`.claude` 쪽에는 전제가 하나 더 있다. `.claude/`는 시작 전에 이미 HEAD에서 빠져 있어야 하고(`git rm -r --cached .claude`를 먼저 커밋), `prepare`는 아직 추적 중이면 멈춘다. 안 그러면 2단계의 `git reset --hard`가 디스크의 `.claude/`까지 지운다. 추적되지 않는 파일은 리셋이 건드리지 않으므로, tracked에서만 빼 두면 재작성이 끝나도 로컬 설정은 남는다. 2단계는 동기화 뒤 디스크에 `.claude/settings.json`이 살아 있는지 한 번 더 확인한다.

## GitHub 보관 창과 끊어진 커밋 링크

되감기가 닫지 못하는 것도 있다. GitHub은 도달 불가능해진 옛 객체를 한동안 보관하고, 옛 커밋 SHA를 아는 사람은 그걸로 옛 블롭에 접근할 수 있다. 완전 제거는 GitHub Support에 gc를 요청해야 하고, 이미 clone하거나 fork한 사본에는 옛 히스토리가 그대로다. 이번 작업이 막은 건 새 클론에서 `git log -p`를 훑는 쉬운 경로 하나지 모든 경로가 아니다.

재작성은 모든 커밋 SHA도 바꿨다. LLM 작업실과 블로그 개발일지의 글들은 특정 커밋을 `/commit/<hash>` 링크로 자주 가리키는데, force-push가 끝나자 그 해시들이 원격에서 사라져 헤더의 "관련 커밋"과 본문 인용이 404가 됐다. 9월 3일에 세어 보니 `_posts/Misc` 아래 커밋 링크 69개 중 19개가 그렇게 죽어 있었다. 살아남은 것은 모두 2026-07-20 이후를 가리키고, 그 이전을 가리키던 참조는 전멸했다.

> 우리가 지난번에 그 Git history 좀 수정하면서 한번 크게 Git을 갈아엎었거든? 그래서 그 과정에서 히스토리가 다 새로 쓰여져서 해시값이 다 달라졌단 말이야. [...] 지금 local 쪽에는 혹시 그 커밋이 남아 있는지, 그리고 그게 가능하다면 그 커밋의 실제 링크로 옮길 수 있는지 확인해 줄 수 있을까

로컬에는 근거가 없었다. `--push` 단계가 `git gc --prune=now`까지 돌려 옛 객체는 작업 저장소에 하나도 안 남았고, `prepare`가 떠 둔 `backup.git`은 다른 기계에 있었다. `.git/filter-repo/commit-map`은 남아 있었지만 7월 7일에 작업 저장소 안에서 돌린 다른 재작성 한 회차의 옛→새 대응이었다. 이 글의 두 스크립트는 bare 클론 안에서 재작성하므로 이 파일을 고쳐 쓰지 않았고, 그 사이 히스토리가 다시 갈렸으니 이 대응은 지금 히스토리에 닿지 않았다.

닿는 근거는 GitHub 쪽 보관 창에 있었다. 죽은 커밋 19개 중 13개는 옛 SHA로 API를 조회하면 아직 응답했다. 재작성이 커밋 메시지와 작성 시각은 건드리지 않았으므로, 이 둘을 키로 현재 히스토리에서 한 건으로 좁힐 수 있었다.

```bash
gh api repos/math-jh/math-jh.github.io/commits/<옛-sha> \
  --jq '.commit.author.date + "  " + (.commit.message | split("\n")[0])'
# 이 (시각, 제목) 쌍을 git log --all 에서 유일 매칭
```
{: data-filename="GitHub API 조회 · 명령 예시"}

GitHub에서도 이미 gc된 6개는 API가 404였다. 그중 5개는 글이 그 커밋을 인용한 맥락, 곧 어떤 파일을 어떻게 건드린 커밋인지로 특정했다. 남은 하나, 가중치 카테고리 글의 "링크 2"(`55e27f8e`)는 후보를 하나로 줄일 근거가 없었다.

> 둘 다 그렇게 하고 링크2를 지우는 선택지로 갈게. [...] development 커밋에 가깝고 후속 조치, history rewrite 여파로 후속 조치라고 해서 커밋하면 될 것 같을까?

그래서 그 링크는 지우고, 나란히 있던 "링크 1"의 표기를 원래대로 "링크"로 되돌렸다. 나머지 18개는 16개 글 21곳에서 새 SHA로 바뀌었고, `_posts/Misc`에 남은 커밋 참조 68개는 전부 origin/main에서 열렸다 ([커밋](https://github.com/math-jh/math-jh.github.io/commit/8073dfb7)). 이 절 첫 문단에서 닫지 못한 노출로 적은 창이 끊어진 링크 열세 개를 도로 이어 줬으니, 같은 창을 한 절 안에서 두 번 다르게 적은 꼴이다.
