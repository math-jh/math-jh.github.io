---
title: "개정 중인 글 동결"
excerpt: "revising: true가 붙은 글을 CI 체크아웃에서 마지막 발행 판본으로 되돌려, 고치는 동안에도 프로덕션이 그 판본을 띄우게 하는 단계"

read_time: false

categories: [Misc / LLM Workshop]
permalink: /ko/llm_workshop/revising_freeze

sidebar:
    nav: "llm_workshop-ko"

author: Marvin

date: 2026-08-07
last_modified_at: 2026-11-02
weight: 37

---

관련 파일: [`scripts/ci/freeze_revising_posts.py`](https://github.com/math-jh/math-jh.github.io/blob/main/scripts/ci/freeze_revising_posts.py), [`_includes/revising-notice.html`](https://github.com/math-jh/math-jh.github.io/blob/main/_includes/revising-notice.html), [`.github/workflows/build-deploy.yml`](https://github.com/math-jh/math-jh.github.io/blob/main/.github/workflows/build-deploy.yml), [`_plugins/diagram_tag.rb`](https://github.com/math-jh/math-jh.github.io/blob/main/_plugins/diagram_tag.rb)
{: .notice--info}

발행된 글을 고치는 동안 `published: false`로 내려 두면 그 URL은 개정이 끝날 때까지 404가 되고, 그 글을 가리키던 인바운드 링크와 사이트맵, 검색 색인이 함께 깨진다. 사용자는 이 간극을 없애자고 했다. 개정 중인 글도 내리지 말고, 마지막으로 정상 발행 상태였던 판본을 프로덕션에 그대로 띄워 두자는 것. 지금의 규약은 고치는 글의 frontmatter에 `revising: true` 한 키를 다는 것이다. CI가 그 키를 보고 글을 과거 판본으로 되돌린 뒤 빌드하므로, dev 서버는 고치는 중인 원고를, 프로덕션은 직전 판본을 보여 준다. 글을 당장 내려야 할 때는 `revising` 없이 `published: false`만 단다. 그러면 옛 판본도 서빙되지 않는다.

## 마지막으로 발행 상태였던 판본의 탐색

`scripts/ci/freeze_revising_posts.py`는 CI 체크아웃에서만 돈다. `git ls-files _posts`로 추적 중인 글을 훑어 frontmatter에 `revising: true`가 있는 것을 추리고, 글마다 이력을 거슬러 올라가 마지막으로 멀쩡했던 커밋을 찾는다.

```python
def last_healthy(path: str):
    """마지막으로 **발행 중이고 개정 중도 아니었던** (sha, 그 시점 경로, 본문)."""
    for sha, hist_path in history(path):
        blob = git("show", f"{sha}:{hist_path}")
        if not blob:
            continue
        fm = frontmatter(blob)
        if not UNPUB_RE.search(fm) and not REVISING_RE.search(fm):
            return sha, hist_path, blob
    return None
```
{: data-filename="scripts/ci/freeze_revising_posts.py"}

멀쩡하다는 것은 그 커밋의 frontmatter에 `published: false`도 `revising: true`도 없다는 뜻이다. `revising: true`가 붙은 커밋은 그 자체로 개정 중 원고라 거기서 멈추면 안 된다. 이 조건이 빠졌을 때 벌어진 일은 마지막 절에 있다. `history()`는 `git log --follow --name-only`의 출력에서 커밋마다 그 시점의 경로를 함께 뽑으므로, 개정 중에 파일명이 바뀐 글도 옛 이름의 blob을 찾아 읽는다. 되짚는 커밋 수는 파일당 120개(`MAX_WALK`)에서 끊는다.

찾은 blob으로 워킹트리의 파일을 덮어쓰는 것이 동결의 본체다. 쓰기 전에 frontmatter에 `revising: true`와 판본 날짜 `revising_snapshot`을 다시 넣는다. 되돌리는 범위는 본문뿐이고, 레이아웃·SCSS·사이드바 같은 사이트 전역 요소는 최신 상태를 따라간다. 빌드된 `_site` 스냅샷을 재활용하지 않고 blob을 복원해 처음부터 빌드하는 이유가 이것이다. 동결한 글과 판본 sha는 `GITHUB_STEP_SUMMARY`에 적혀 Actions 실행 요약에 뜬다.

되살릴 판본을 못 찾은 글은 두 갈래로 갈린다. 현재 파일에 `published: false`도 붙어 있으면 어차피 숨겨지는 초안이라 경고만 남긴다. `revising: true`만 있으면 고치는 중인 원고가 그대로 배포되는 경우이므로 빌드를 중단한다.

## ko·en이 공유하는 그림의 frozen 사본

본문만 과거로 돌리는 것으로는 부족하다. 다이어그램 SVG와 이미지는 `assets/images/Math/<Category>/<Article>-1.svg`처럼 글 제목으로 경로가 고정되어 있고, ko/en 두 언어판이 같은 파일을 공유한다. 이 경로를 제자리에서 과거 버전으로 되돌리면, 한쪽 언어만 개정 중이어도 발행 중인 반대쪽 언어의 그림까지 과거로 끌려간다.

그래서 복원된 본문이 참조하는 자산 중 내용이 실제로 달라진 것만 골라 전용 사본을 뜬다.

```python
def freeze_assets(text: str, sha: str, apply: bool, log: list[str]) -> str:
    """복원된 본문이 참조하는 자산 중 내용이 달라진 것만 전용 사본으로 뜬다."""
    sha8 = sha[:8]
    for whole, repo_path, dest_rel, new_ref in asset_refs(text, sha8):
        old = git("show", f"{sha}:{repo_path}", binary=True)
        if old is None:
            continue  # 당시에도 없던 자산 참조
        cur_file = ROOT / repo_path
        cur = cur_file.read_bytes() if cur_file.is_file() else None
        if cur == old:
            continue
        if apply:
            dest = ROOT / dest_rel
            dest.parent.mkdir(parents=True, exist_ok=True)
            dest.write_bytes(old)
        text = text.replace(whole, new_ref)
    return text
```
{: data-filename="scripts/ci/freeze_revising_posts.py"}

`asset_refs()`는 사본 경로와 바뀐 참조 문자열을 한 규칙에서 함께 만든다. 참조 종류마다 기준 디렉토리가 달라서다. {% raw %}{% diagram %}{% endraw %} 태그가 참조하는 경로는 `assets/images/` 기준이라 `assets/images/frozen/<sha8>/...`에, `/assets/...` 직접 링크와 `src`·`href` 속성은 사이트 루트 기준이라 `assets/frozen/<sha8>/...`에 사본이 뜬다. 옛 판본이 그 사이 삭제된 이미지를 참조하는 경우도 실제로 있었는데, 이때는 현재 파일이 없으니 `git show`로 꺼낸 옛 blob이 그대로 사본이 된다.

`_plugins/diagram_tag.rb`의 PNG 예외 목록(`EXCEPTIONS`)은 경로 문자열(`Math/Algebraic_Topology/Homology-3.svg` 등)로 조회하는데, 자산이 `frozen/<sha8>/` 접두를 달고 들어오면 그대로는 매치되지 않는다. 조회 전에 접두를 떼는 정규식이 하나 끼어 있다.

```ruby
FROZEN_PREFIX = %r{\Afrozen/[0-9a-f]{8}/}
# ...
if @path.end_with?('.png') || EXCEPTIONS.include?(@path.sub(FROZEN_PREFIX, ''))
```
{: data-filename="_plugins/diagram_tag.rb"}

## 판본 날짜와 수정 중 알림

본문은 과거 판본인데, 파일의 git 로그를 읽는 `last_modified_git` 플러그인은 이 파일을 "오늘 수정됨"으로 표시한다. 그래서 복원한 blob의 frontmatter에 `last_modified_at`이 없으면 healthy 커밋의 시각을 그 자리에 넣는다. 이미 값이 있으면 건드리지 않는다.

독자에게도 지금 보는 것이 최신이 아니라는 사실을 알려야 한다. `_includes/revising-notice.html`이 `page.revising`을 보고 글 상단에 안내를 띄우는데, 문구는 두 갈래다.

{% raw %}
```liquid
{% if page.revising_snapshot %}
  {% assign _date = page.revising_snapshot | date: "%Y-%m-%d" %}
  {% assign _notice = site.data.ui-text[_lang].revising_notice | replace: "__DATE__", _date %}
{% else %}
  {% assign _notice = site.data.ui-text[_lang].revising_notice_wip %}
{% endif %}
```
{: data-filename="_includes/revising-notice.html"}
{% endraw %}

`revising_snapshot`은 동결 스크립트만 채우는 필드다. 프로덕션 빌드는 이 값을 갖고 있으니 "아래 본문은 YYYY-MM-DD 시점의 판본"이라고 날짜를 넣어 보여 준다. dev 서버는 동결 단계를 거치지 않고 워킹트리를 그대로 빌드하므로 `revising: true`만 있고 날짜가 없어서, 날짜 없는 `revising_notice_wip` 문구가 뜬다. 같은 include가 두 서버에서 다른 문구를 내는 것은 이 필드 하나의 유무로 갈린다.

## 체크아웃 직후의 동결 단계와 `_posts` 한정 가드

`--apply`는 `_posts`가 clean할 때만 워킹트리를 고쳐 쓴다. 로컬에서 실수로 돌려 개정 중인 원고를 과거 판본으로 덮어쓰는 사고를 막는 가드다. 처음에는 이 가드가 워킹트리 전체를 봤고, 동결 단계는 `jekyll build` 바로 앞에 있었다. CI 체크아웃은 매번 clean하게 시작하니 걸릴 일이 없다고 봤는데, 그 자리는 홈 타일 썸네일을 굽는 단계 다음이었다. 그 단계는 `_data/hues.yml`에서 JPEG를 매번 새로 만들어 낸다. 가드가 본 것은 그 결과였다.

```
freeze: --apply 는 clean 워킹트리에서만 동작한다. 커밋되지 않은 변경:
 M assets/images/Pages/Thumbnails/Files/Commutative_Algebra.jpeg
 M assets/images/Pages/Thumbnails/Files/Homological_Algebra.jpeg
 M assets/images/Pages/Thumbnails/Files/Linear_Algebra.jpeg
```

build가 exit 1로 죽고 deploy는 skip됐다. 같은 이유로 두 번 연속 실패한 뒤에 두 군데를 고쳤다. 동결은 git 이력만 있으면 되는 작업이라 단계를 Checkout 바로 다음으로 올렸고, 가드의 검사 범위는 `git status --porcelain -- _posts`로 좁혔다.

```yaml
- name: Checkout
  uses: actions/checkout@v7
  with:
    fetch-depth: 0

- name: Freeze posts under revision
  run: python3 scripts/ci/freeze_revising_posts.py --apply
```
{: data-filename=".github/workflows/build-deploy.yml"}

가드가 지키려던 것은 커밋되지 않은 원고이지 자산이 아니다. 자산 쪽은 빌드가 파일을 만들어 내니 언제든 dirty일 수 있고, 스크립트가 자산에 쓰는 것은 `frozen/` 아래 새 경로뿐이라 덮어쓸 것도 없다. 그래서 범위를 좁힌 쪽은 단계 순서가 다시 바뀌어도 성립한다. `FREEZE_ALLOW_DIRTY=1`로 가드를 끌 수 있지만, 버려도 되는 사본에서 동작만 확인할 때 쓰는 용도다.

## `revising` 한 키로의 이관과 7분의 공백

동결이 처음 생겼을 때의 규약은 `published: false`와 `revising: true`를 함께 다는 것이었다. 열흘 뒤, 대시보드에서 개정 중인 글들이 미발행 초안으로 잡히는 게 눈에 띄었다. `published: false`가 두 가지 뜻을 겸하고 있었던 탓이다. 하나는 이 글이 동결 대상이라는 뜻이고, 다른 하나는 대시보드 개요·용어 스윕의 초안 선별·번역 워커의 `is_draft`가 읽는 "발행된 적 없는 초안"이라는 뜻이다.

> 그리고 지금 revising: true인 글들도 dashboard에서 미발행으로 잡히는데 그건 아니지. (1) revising: true면 자동으로 published: false인 것으로 간주하고 직전 판본 스냅샷 띄워서, 그 글들에서 publish: false키들을 없애던가, (2) dashboard를 손보자. 난 의미상 (1)이 맞다 보는데.

(1)로 정리됐다. 개정 중이던 199편에서 `published: false` 한 줄씩을 걷어 내는 일회성 스윕(`scripts/sweeps/revising_drop_published.py`)에는 게이트를 세게 걸었다. frontmatter에서 사라지는 줄이 정확히 하나여야 하고, 본문은 바이트 단위로 원문과 같아야 통과한다.

그 키가 겸하던 자리는 읽는 쪽이 하나씩 넘겨받았다. 번역 워커의 `is_draft`는 이제 `revising: true`도 건너뛴다. 이 조건이 없으면 워커가 개정 중인 글을 발행 글로 보고, 고치는 중인 원고를 번역해 EN을 덮어쓴다. 대시보드 서버는 개정 중인 글을 미발행 집계에서 빼고 따로 센다. 그 수를 보일 자리는 사용자가 정했다.

> 이제 개정 중 편수 보이게 미발행 초안 카드에 추가하고, GUIDELINE이랑 service map 등등 남은 일들 다 해.

미발행 초안 카드의 설명줄 끝에 `· 개정 중 N편 (발행 상태)`가 붙는다.

빠진 것은 `freeze_revising_posts.py` 자신이었다. 그때의 `last_healthy`는 `published: false`의 유무만 봤다. 그 키를 걷어 낸 뒤로는 지금 커밋 자체가 그 조건을 통과하니, 개정 중인 원고가 곧 "마지막 healthy 판본"으로 읽히고 동결은 아무것도 되돌리지 않는 no-op이 됐다. 스윕 커밋의 빌드가 12:52(UTC)에 배포를 마쳤고, 판정을 고친 다음 커밋의 배포가 13:00에 끝나기까지 7분 반 동안 개정 중이던 199편은 다듬는 중인 원고 그대로 프로덕션에 떠 있었다. 첫 절의 `last_healthy`가 `revising: true`까지 거르는 것이 그 수정이다.

되살릴 판본이 없는 `revising` 글이 경고가 아니라 빌드 중단인 것도 이 이관에서 정해졌다. `published: false`가 뒤를 받치던 동안에는 판본을 못 찾아도 그 글이 숨겨질 뿐이었다. 지금은 CI의 동결 단계가 고치는 중인 원고와 프로덕션 사이에 놓인 유일한 단계다.
