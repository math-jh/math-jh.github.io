---

title: "Dependabot PR 자동 검토와 머지"
excerpt: "Dependabot PR만 결정적 관문, 도구를 제한한 Claude 판정, squash 머지, main 빌드 확인의 순서로 처리하는 하루 한 번의 크론"

read_time: false

categories: [Misc / LLM Workshop]
permalink: /ko/llm_workshop/dependabot_automerge

sidebar:
    nav: "llm_workshop-ko"

author: Marvin

date: 2026-11-16
weight: 75
group: agents

---

관련 파일: [`scripts/dependabot/automerge.py`](https://github.com/math-jh/math-jh.github.io/blob/main/scripts/dependabot/automerge.py), [`.github/dependabot.yml`](https://github.com/math-jh/math-jh.github.io/blob/main/.github/dependabot.yml), [`scripts/dashboard/server.py`](https://github.com/math-jh/math-jh.github.io/blob/main/scripts/dashboard/server.py), [15373316](https://github.com/math-jh/math-jh.github.io/commit/15373316)
{: .notice--info}

Dependabot은 6월 말부터 매주 월요일에 gem·npm·GitHub Actions 업데이트 PR을 열고 있었고, 그 PR은 5분마다 도는 [PR 알림](/ko/llm_workshop/pi_notifications_bark)으로 사용자의 폰에 도착했다. 알림이 끝이었다. 열어서 변경 내역을 읽고, 머지하고, 배포가 초록인지 확인하는 일은 사용자 몫이었다. 사용자가 원한 것은 이 검토를 LLM에게 넘기는 것이었다.

> 그니까 내가 원하는 건 이 기능을 완전 스크립트로 구현할 필요 없고, 새 PR 감지되면 LLM (염두에 두고 있는 건 Claude야) 이 확인해서 승인하는 것. 단, 우리 블로그에선 블로그 댓글도 PR의 일종으로 오고 그걸 승인하는 건 내가 할 일이니까 이쪽 경로에는 그게 개입하면 안 되고, 오직 dependabot에서 오는 것만 개입해야 해.

여기에 하루 최대 한 번만 돌게 하고, 프롬프트 인젝션에 대비해 꼭 필요한 도구만 주는 조건이 붙었다. 하루 한 번의 구체적인 횟수는 지금까지의 양상을 보고 정하라는 위임이었다. 그래서 `automerge.py`는 판단을 Claude에게 맡기되, 판단 앞뒤를 결정적인 코드가 감싸는 구조가 되었다.

## 댓글 PR을 걸러 내는 경로

이 블로그의 댓글은 `comment/*` 브랜치의 PR로 들어오고, 그 승인은 사용자가 직접 한다. 자동 머지가 이 PR을 건드릴 가능성을 설계에서 지우는 것이 첫 번째 요구였다. 목록을 가져오는 단계부터 작성자를 지정한다.

```python
def open_dependabot_pulls() -> list[dict]:
    out = gh("pr", "list", "--repo", REPO, "--state", "open", "--author", "app/dependabot",
             "--limit", "50", "--json",
             "number,title,url,body,headRefName,headRefOid,baseRefOid,author,isDraft,"
             "isCrossRepository,mergeable,mergeStateStatus,statusCheckRollup")
    return sorted(json.loads(out or "[]"), key=lambda p: p["number"])
```
{: data-filename="scripts/dependabot/automerge.py · 일부 발췌"}

`--author app/dependabot`으로 받으면 댓글 PR은 이 스크립트가 처리할 후보에 올라오지도 않는다. 이어지는 관문 함수가 작성자와 브랜치 접두사를 한 번 더 확인하지만, 이는 이중 확인이고 첫 번째 차단은 이 목록이다.

## 모델에 가기 전의 관문

Claude의 판정은 확률적이므로, 판정과 무관하게 지켜야 할 조건은 `gate()`가 먼저 걸러 낸다. 이 함수는 PR을 `ok`, `hold`, `wait` 셋 중 하나로 분류하고 이유를 남긴다. 확인 순서는 값싼 것부터다.

1. 작성자가 `app/dependabot`이고, 브랜치가 같은 저장소의 `dependabot/*`이며, draft가 아닐 것.
2. 커밋 전부의 작성자가 `dependabot[bot]`이고 GitHub 서명 검증이 통과했을 것. 사람이 PR 브랜치에 커밋을 덧붙였다면 보류한다.
3. 바뀐 파일이 의존성 manifest(`Gemfile`, `Gemfile.lock`, `package.json`, `package-lock.json`)뿐일 것.
4. 커밋 본문에 Dependabot이 붙이는 `updated-dependencies` 메타데이터가 있을 것.
5. PR 체크가 모두 성공이고 GitHub가 `MERGEABLE`/`CLEAN`으로 볼 것. 체크가 진행 중이거나 머지 상태가 계산 중이면 `wait`이고, 실패하면 `hold`다.

3번에는 예외가 하나 있다. `dependabot/github_actions/` 브랜치에 한해 `.github/workflows/*.yml`의 변경을 허용하되, 바뀐 줄이 전부 `uses: owner/action@ref` 꼴이어야 한다.

```python
USES_LINE = re.compile(r"^\s*(-\s+)?uses:\s*[\w.\-]+/[\w.\-/]+@[\w.\-]+\s*(#.*)?$")

def workflow_patch_ok(patch: str | None) -> bool:
    """워크플로 파일의 변경 줄이 전부 `uses:` 줄인가."""
    if not patch:
        return False
    for line in patch.splitlines():
        if line.startswith(("+++", "---", "@@")) or not line[:1] in ("+", "-"):
            continue
        if not USES_LINE.match(line[1:]):
            return False
    return True
```
{: data-filename="scripts/dependabot/automerge.py · 일부 발췌"}

diff의 헤더(`+++`, `---`, `@@`)와 맥락 줄(앞 글자가 `+`·`-`가 아닌 줄)은 건너뛰고, 추가·삭제된 줄만 정규식에 대 본다. 워크플로 파일은 배포 권한을 가진 코드여서, `uses:` 줄 하나가 아닌 다른 줄이 끼어 있으면 Dependabot이 보낸 것이어도 사람이 봐야 한다. 이 관문에서 `hold`가 나온 PR은 Claude를 거치지 않고, 이유와 함께 (PR, head) 한 쌍당 한 번 폰으로 알림이 간다.

## 도구를 줄인 Claude 판정

관문을 통과한 PR 가운데 그 head에 대한 판정이 없는 것을 한 세션에 묶어 판정받는다. 판정은 head sha별로 상태 파일에 저장하므로, 같은 커밋을 두 번 판정하지 않는다. 호출은 하루 한 번으로 제한하며, 같은 날 이미 판정했으면 로그만 남기고 다음 날로 미룬다.

```python
cmd = [str(CLAUDE), "-p", "--restricted", "--strict-mcp-config",
       "--disable-slash-commands", "--no-session-persistence",
       "--tools", "Read,Grep,Glob,WebFetch",
       "--allowedTools", *[f"WebFetch(domain:{d})" for d in WEB_DOMAINS],
       "--permission-mode", "dontAsk",
       "--model", MODEL, "--effort", EFFORT,
       "--output-format", "json", "--json-schema", json.dumps(VERDICT_SCHEMA)]
```
{: data-filename="scripts/dependabot/automerge.py · judge() 일부 발췌"}

사용자가 우려한 것은 PR 본문이다. 본문에는 업스트림 릴리스 노트가 인용되는데, 이는 제3자가 쓴 텍스트이고 "이전 지시를 무시하라" 같은 문장이 들어올 수 있다. 그래서 이 호출은 쓸 수 있는 도구와 읽을 수 있는 곳을 모두 좁힌다.

- 도구는 `Read`, `Grep`, `Glob`, 그리고 도메인을 제한한 `WebFetch`뿐이다. 도메인은 `github.com`, `raw.githubusercontent.com`, `rubygems.org`, npm 두 곳이다. 쓰기와 셸이 없으므로 판정 세션이 직접 할 수 있는 일은 읽기뿐이다.
- 작업 디렉터리는 임시 폴더 하나다. 호출부가 GitHub API로 모은 `facts.json`(바뀐 파일, Dependabot 메타데이터, 락파일에서 버전이 달라진 모든 패키지), `diff.patch`, `pr-body.md`와, `origin/main`의 공개 소스를 `git archive`로 푼 스냅샷이 들어 있다. 레포 작업 트리를 주지 않으므로 미발행 글이나 로컬 설정은 보이지 않는다.
- 출력은 JSON 스키마를 지킨 판정뿐이다. PR마다 `approve`/`hold`, 한국어 요약, 우려, 확인한 출처를 돌려준다. 승인·머지는 스크립트가 하고, 모델의 출력은 그 결정의 입력일 뿐이다.

`facts.json`에 락파일 비교를 넣은 이유는 PR 제목이 전이 의존성의 변경을 말해 주지 않기 때문이다. `lockfile_changes`는 base와 head의 `Gemfile.lock`·`package-lock.json`을 각각 내려받아 버전이 달라진 패키지를 전부 나열하고, 바뀌면 빌드가 통과해도 사이트 출력이 달라질 수 있는 패키지(`jekyll`, `kramdown`, `rouge`, `sass-embedded`, `pagefind` 등)에는 `render_relevant` 표시를 붙인다. 프롬프트는 이 표시가 붙었거나 메이저 변경인 항목은 업스트림 변경 내역을 읽고, 이 사이트의 `_config.yml`·`_plugins`·`_sass`가 그 기능을 실제로 쓰는지 대조하라고 요구한다. 기준은 한 줄이다. 빌드 실패는 머지 뒤에 자동으로 드러나므로, 빌드는 통과하지만 출력이 조용히 달라지는 변경을 가장 경계하라고 했다. 근거를 못 읽었거나 조금이라도 이상하면 `hold`다.

11월 16일 첫 실행에서 npm 그룹 PR(pagefind 1.5.2→1.6.0, js-yaml 5.4.2→5.5.0)에 대한 판정은 전이 의존성 `argparse`가 2.0.1에서 3.0.4로 메이저 점프한 것까지 찾아냈다. 이 변경이 js-yaml의 CLI에만 해당하고 `scripts/generate-thumbnails.js`는 `yaml.load`만 쓴다는 대조를 근거로 승인했다.

## 승인, 머지, 그리고 main 빌드

승인 판정이 나온 PR의 처리는 순서가 중요하다.

`Gemfile.lock`이 바뀐 PR은 머지 전에 그 락파일을 이 Pi의 `vendor/bundle`에 먼저 설치한다. 머지 뒤 `blog-autopush`가 락파일을 당겨 오면, 개발 서버의 `bundle exec`가 아직 설치되지 않은 gem 때문에 다음 재시작에서 죽는다. 그래서 임시 디렉터리에 head의 `Gemfile`과 `Gemfile.lock`을 내려받고 `bundle check`로 이미 설치돼 있는지 본 뒤, 없을 때만 `bundle install`을 돌린다. 이미 있는 버전은 지우지 않는다.

그다음에는 `blog-autopush.service`가 도는 중이면 끝나기를 최대 20분 기다린다. 승인 리뷰를 달고 `--match-head-commit`으로 검토한 head와 같을 때만 squash 머지를 요청한다. 리뷰 본문의 `@`는 전각 `＠`로 바꿔 둔다. 이 본문이 Claude의 요약을 그대로 싣기 때문에, 그 안에 `@dependabot <명령>`이나 멘션이 있어도 GitHub에서 작동하지 않게 하려는 것이다.

머지가 끝이 아니다. main에 머지하면 곧바로 사이트가 다시 빌드되고 배포되므로, 스크립트는 그 실행이 초록인지까지 본다. 머지 커밋이거나 그 자손을 head로 가진 `Build and deploy` 실행이 성공할 때까지 다음 PR을 머지하지 않는다. 자손까지 보는 이유는 GitHub Pages의 `concurrency` 때문이다. 머지 직후 다른 push가 오면 대기 중이던 실행이 `cancelled`로 밀려날 수 있고, 그 경우에도 뒤따른 실행이 같은 변경을 포함한다. `cancelled`와 `skipped`는 실패로 세지 않는다. 실패는 두 갈래로 나눈다. build job이 실패했으면 즉시 `timeSensitive`로 알리고, deploy만 실패했으면 autopush의 `retry_failed_ci`가 다음 짝수 정시에 다시 돌리므로 알림만 한다. 이 스크립트는 재실행도 되돌리기도 하지 않는다. 한 번에 한 PR만 머지하므로 빌드가 깨졌을 때 원인은 항상 하나다.

머지한 PR은 `state.inflight`로 기록한다. 한 번의 실행이 빌드를 기다리는 시간은 60분이고, 그 안에 결과가 안 나오면 다음 날 실행이 이 기록부터 이어 본다. 초록이 아니면 새 머지 없이 끝난다.

## 첫 실행

크론은 매일 19:30에 `cron-gate blog-dependabot`을 앞세워 돈다. PR이 월요일 18:55 무렵에 오는 것이 7월부터 11월까지의 기록에서 확인되어, 그 직후로 시각을 잡았다. 대시보드의 크론 목록에는 `blog-dependabot` 항목을 추가해, [크론 정지 게이트](/ko/llm_workshop/cron_gate)로 멈추고 재개할 수 있게 했다.

11월 16일 저녁에 열려 있던 PR은 두 건(#53 jekyll-include-cache, #54 npm 그룹)이었고, 둘 다 관문을 통과해 Claude의 승인 판정을 받았다. 19:49의 실행 로그에는 오늘은 이미 판정했다는 줄만 남았다. 사용자는 이 두 건을 수동으로 한번 돌려 보자고 했고, 20:27에 같은 스크립트를 다시 실행했다.

> 그래, 둘 다 머지해줄래? 수동으로 해볼까?

#53은 20:27에 승인·머지되어 20:29에 빌드 성공, #54는 20:30에 머지되어 20:33에 빌드 성공으로 끝났다. 판정은 head sha로 캐시돼 있어서 이 실행은 Claude를 다시 부르지 않았다.

남은 일은 실제 월요일에 이 크론이 처음부터 끝까지 혼자 도는 것을 보는 것이다. 게이트가 `hold`로 넘긴 경우와 Claude가 `hold`로 판정한 경우는 아직 실제 PR로 겪어 보지 못했다.
