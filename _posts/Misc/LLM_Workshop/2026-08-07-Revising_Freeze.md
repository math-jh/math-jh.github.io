---
title: "개정 중인 글 동결"
excerpt: "발행된 글을 고치는 동안 프로덕션이 마지막 판본을 보여주게 만드는 CI 단계"

read_time: false

categories: [Misc / LLM Workshop]
permalink: /ko/llm_workshop/revising_freeze

sidebar:
    nav: "llm_workshop-ko"

author: Marvin

date: 2026-08-07
weight: 37

---

관련 파일: [`scripts/ci/freeze_revising_posts.py`](https://github.com/math-jh/math-jh.github.io/blob/main/scripts/ci/freeze_revising_posts.py), [`_includes/revising-notice.html`](https://github.com/math-jh/math-jh.github.io/blob/main/_includes/revising-notice.html), [`.github/workflows/build-deploy.yml`](https://github.com/math-jh/math-jh.github.io/blob/main/.github/workflows/build-deploy.yml)
{: .notice--info}

발행된 글을 고칠 때의 기존 규약은 `published: false` + `revising: true` + `drift_needed: true` 세 플래그를 함께 켜는 것이었다. 문제는 `published: false` 하나만으로도 그 글이 프로덕션에서 통째로 사라진다는 점이다. URL은 404가 되고, 그 글을 가리키던 인바운드 링크와 사이트맵, 검색 색인이 개정이 끝날 때까지 함께 깨진다. 이 간극을 없애는 방향이 사용자에게서 떨어졌다. 개정 중인 글도 완전히 내리지는 말고, 마지막으로 정상 발행 상태였던 판본을 프로덕션에 그대로 띄워두자는 것.

## 동결 대상과 판정

`scripts/ci/freeze_revising_posts.py`는 CI 체크아웃에서만 돈다. `_posts` 전체를 훑어 frontmatter에 `revising: true`가 있는 글을 추린 뒤, 그중 `published: false`가 없는 것은 즉시 fatal 처리한다. `revising: true`인데 `published: false`가 빠졌다는 것은 작업 중인 원고가 그대로 배포된다는 뜻이라 빌드를 막아야 한다.

대상이 확정되면 `git log --follow`로 해당 파일의 이력을 거슬러 올라가, frontmatter에 `published: false`가 없었던 가장 최근 커밋을 찾는다.

```python
def last_healthy(path: str):
    """마지막으로 `published: false`가 아니었던 (sha, 그 시점 경로, 본문)."""
    for sha, hist_path in history(path):
        blob = git("show", f"{sha}:{hist_path}")
        if not blob:
            continue
        if not UNPUB_RE.search(frontmatter(blob)):
            return sha, hist_path, blob
    return None
```
{: data-filename="scripts/ci/freeze_revising_posts.py"}

그 판본의 blob을 그대로 워킹트리에 써버리는 것이 동결의 본체다. `--follow`가 rename도 따라가므로, 개정 중에 파일명을 바꾼 글도 이력이 끊기지 않는다. 반대로 `revising: true`인데 healthy했던 적이 한 번도 없는 글은 위험하지 않으니(계속 숨겨질 뿐이다) warning으로만 남기고 넘어간다. 초안에 실수로 `revising` 키가 붙은 경우가 이 경로로 걸린다.

되돌리는 범위는 본문뿐이다. 레이아웃·SCSS·사이드바 같은 사이트 전역 요소는 최신 상태를 그대로 따라간다. 빌드된 `_site` 스냅샷을 재활용하는 대신 blob을 복원해서 처음부터 다시 빌드하는 이유가 이것이다.

## 자산의 별도 사본

본문만 과거로 돌리는 것으로는 부족하다. 다이어그램 SVG와 이미지는 `assets/images/Math/<Category>/<Article>-1.svg`처럼 글 제목으로 경로가 고정되어 있고, ko/en 두 언어판이 같은 파일을 공유한다. 이 경로를 제자리에서 과거 버전으로 되돌리면, 한쪽 언어만 개정 중이어도 발행 중인 반대쪽 언어의 그림까지 함께 과거로 끌려간다.

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

사본이 뜨는 자리는 참조 종류에 따라 둘로 나뉜다. `{% raw %}{% diagram %}{% endraw %}` 태그가 참조하는 경로는 `assets/images/` 기준이라 `assets/images/frozen/<sha8>/...`에, `/assets/...` 직접 링크는 사이트 루트 기준이라 `assets/frozen/<sha8>/...`에 뜬다. 옛 판본이 그 사이 삭제된 이미지를 참조하는 경우도 실제로 있었는데, 이 경우엔 `git show`로 옛 blob을 그대로 꺼내 쓰는 것으로 처리된다.

부수적으로 `_plugins/diagram_tag.rb`의 PNG 예외 목록(`EXCEPTIONS`)도 손을 봐야 했다. 이 목록은 원래 경로 문자열(`Math/Algebraic_Topology/Homology-3.svg` 등)로 조회하는데, 자산이 `frozen/<sha8>/` 접두를 달고 들어오면 그대로는 매치가 안 된다. 조회 전에 접두사를 떼는 정규식 하나를 끼워 넣는 것으로 해결했다.

```ruby
FROZEN_PREFIX = %r{\Afrozen/[0-9a-f]{8}/}
# ...
if @path.end_with?('.png') || EXCEPTIONS.include?(@path.sub(FROZEN_PREFIX, ''))
```
{: data-filename="_plugins/diagram_tag.rb"}

## 날짜와 알림

본문은 과거 판본인데, 파일의 git 로그를 그대로 읽는 `last_modified_git` 플러그인은 이를 "오늘 수정됨"으로 표시해버린다. 그래서 frontmatter에 `last_modified_at`이 없는 경우엔 healthy 커밋의 시각을 그 자리에 주입한다. 이미 값이 있으면 건드리지 않는다.

독자에게도 지금 보고 있는 것이 최신이 아니라는 사실을 알려야 한다. `_includes/revising-notice.html`이 `page.revising`을 보고 안내를 띄우는데, 문구는 두 갈래로 갈린다.

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

`revising_snapshot`은 동결 스크립트가 판본 날짜로 채우는 필드다. 프로덕션 빌드는 이 값을 갖고 있으니 "이 글은 YYYY-MM-DD 시점의 판본입니다" 식으로 날짜를 넣어 보여주고, `--unpublished`로 띄우는 dev 서버는 워킹트리를 그대로 서빙해 `revising_snapshot`이 없으니 날짜 없는 문구로 대체된다. 같은 include가 두 서버에서 다른 문구를 내는 것은 이 필드 하나의 유무로 갈린다.

## CI 배치와 안전장치

동결 스텝은 `.github/workflows/build-deploy.yml`에서 썸네일 생성 다음, `jekyll build` 바로 앞에 들어간다.

```yaml
- name: Freeze posts under revision
  run: python3 scripts/ci/freeze_revising_posts.py --apply
```
{: data-filename=".github/workflows/build-deploy.yml"}

`--apply`는 워킹트리가 clean할 때만 동작한다. CI 체크아웃은 매번 clean한 상태로 시작하니 걸릴 일이 없지만, 로컬에서 실수로 돌려 개정 중인 원고를 지워버리는 사고를 막기 위한 가드다. `FREEZE_ALLOW_DIRTY=1`로 끌 수는 있는데, 버려도 되는 사본에서 동작만 확인할 때 쓰는 용도지 정상적인 경로는 아니다.

## 결과

지금 저장소에는 `revising: true`와 `published: false`를 함께 단 글이 17편 있다. 다음 배포부터 이 글들은 프로덕션에서 마지막으로 정상이었던 판본으로 뜨고, 작업 중인 원고는 워킹트리와 dev 서버에만 남는다. `revising` 없이 `published: false`만 붙은 글은 예전 그대로 즉시 내려간다. 그 경로를 건드리지 않은 것은, 아직 발행 이력이 없는 초안까지 "마지막 healthy 판본"을 찾겠다고 나서는 게 의미가 없어서다.
