---

title: "넓은 화면의 사이드바와 목차"
excerpt: "사이드바·목차 글씨를 본문의 0.75배 한 곳으로 모으고, 1400px 이상에서 틀과 양쪽 칸을 50px씩 넓히되 본문 칸 폭은 그대로 두는 레이아웃"

read_time: false

categories: [Misc / LLM Workshop]
permalink: /ko/llm_workshop/wide_layout

sidebar:
    nav: "llm_workshop-ko"

author: Marvin

date: 2026-10-25
weight: 60
group: theme

---

관련 파일: [`_sass/minimal-mistakes/_variables.scss`](https://github.com/math-jh/math-jh.github.io/blob/main/_sass/minimal-mistakes/_variables.scss), [`_sass/minimal-mistakes/_navigation.scss`](https://github.com/math-jh/math-jh.github.io/blob/main/_sass/minimal-mistakes/_navigation.scss), [`_sass/minimal-mistakes/_sidebar.scss`](https://github.com/math-jh/math-jh.github.io/blob/main/_sass/minimal-mistakes/_sidebar.scss), [`_sass/minimal-mistakes/_page.scss`](https://github.com/math-jh/math-jh.github.io/blob/main/_sass/minimal-mistakes/_page.scss), [23f8cf26](https://github.com/math-jh/math-jh.github.io/commit/23f8cf26), [eea197ea](https://github.com/math-jh/math-jh.github.io/commit/eea197ea)
{: .notice--info}

여느 블로그처럼 이 사이트도 넓은 화면에서는 본문 양옆에 여백이 많이 남았다. 바탕으로 쓰는 minimal-mistakes 테마가 전체 너비를 제한하는 영향도 있었다. 사용자는 큰 모니터에서 그 여백이 다소 과하다고 느꼈고, 본문 폭은 유지하면서 양쪽 사이드바를 넓히자고 했다. 함께 살펴보니 사이드바와 목차의 글자도 의도보다 작았다.

## 중첩 목록에서 곱해지는 em

원인은 `_sidebar.scss`의 `p, li` 규칙이다.

```scss
  p,
  li {
    font-family: $sans-serif;
    font-size: $type-size-6;   // 0.75em
    line-height: 1.5;
  }
```
{: data-filename="_sass/minimal-mistakes/_sidebar.scss · 일부 발췌, 주석 추가"}

`0.75em`은 부모 글자 크기에 대한 비율이다. 사이드바의 카테고리 목록은 `li` 안에 `ul`이 들어가고 그 안에 다시 `li`가 있는 구조여서, 중첩된 `li`는 0.75 × 0.75 = 0.5625배가 된다. 기준 글자 크기가 15.2px이면 11.4px가 되어야 할 자리가 8.5px로 줄어든다. 오른쪽 목차는 `.toc__menu`가 `$type-size-6`을 주고 `$large` 이상에서 `$type-size-7`(0.6875em)로 바꾸고 있었다. 15.2px를 기준으로 하면 약 10.5px다.

사용자는 사이드바가 본문보다 작게 보이기를 원했고, 몇 가지 크기를 비교한 뒤 0.75배를 골랐다.

> B가 낫겠지? 0.75 정도로 하고 싶어. 0.85는 사이드바가 너무 큰 것 같아서.

이 배율을 한 번만 적용해 목록이 중첩되어도 글자가 작아지지 않게 했다.

```scss
// 왼쪽 사이드바·목차·의존성 그래프 제목. 부모가 본문 글자 크기인 자리에 건다.
$type-size-aside: 0.75em !default;
```
{: data-filename="_sass/minimal-mistakes/_variables.scss · 일부 발췌"}

```scss
.nav__list .nav__items {
  margin: 0;
  font-size: $type-size-aside;
  line-height: 1.2em;

  // .sidebar li 의 em 축소가 중첩 목록에서 곱해지지 않게 한다.
  li {
    font-size: inherit;
  }
```
{: data-filename="_sass/minimal-mistakes/_navigation.scss · 일부 발췌"}

nav 목록(`.nav__list .nav__items`)에서 한 번 0.75배로 줄이고, 그 안의 `li`는 `inherit`으로 부모 크기를 받는다. 목차와 의존성 그래프 제목에도 같은 `$type-size-aside`를 쓴다. 카테고리 페이지의 최근 글·댓글 목록 역시 항목마다 크기를 다시 줄이지 않도록 고쳤다.

## 1400px에서만 넓어지는 틀

사용자는 본문의 한 줄 길이를 유지하면서 양옆의 공간을 활용하고 싶어 했다. 그래서 화면 폭이 1400px 이상이면 양쪽 칸을 각각 200px에서 250px로 늘리고 전체 틀도 함께 넓혔다. 기존에 정의만 되어 있던 `$right-sidebar-width-wide`에 breakpoint `$xx-large`와 넓은 틀 `$max-width-wide`를 더했다.

같은 글을 1600px 폭에서 비교하면 다음과 같다. 첫 화면은 현재 글에 수정 직전 커밋의 스타일을 적용해 재현했고, 둘째는 현재 모습이다. 본문 폭은 그대로이고 양쪽 칸이 넓어졌다.

<div role="region" aria-label="레이아웃 수정 전후 비교. 가로로 스크롤하여 다음 이미지를 볼 수 있습니다." tabindex="0" style="display:flex; overflow-x:auto; scroll-snap-type:x mandatory; gap:1rem; padding-bottom:0.5rem;">
  <figure style="flex:0 0 94%; min-width:0; margin:0; scroll-snap-align:start;">
    <img src="/assets/images/Misc/LLM_Workshop/Wide_Layout-before.png" alt="수정 전 스타일로 재현한 넓은 화면의 글" style="display:block; width:100%;" />
    <figcaption>수정 전 스타일</figcaption>
  </figure>
  <figure style="flex:0 0 94%; min-width:0; margin:0; scroll-snap-align:start;">
    <img src="/assets/images/Misc/LLM_Workshop/Wide_Layout-after.png" alt="현재 넓은 화면의 글" style="display:block; width:100%;" />
    <figcaption>수정 후</figcaption>
  </figure>
</div>

```scss
$xx-large: 1400px !default;

$right-sidebar-width: 200px !default;
$right-sidebar-width-wide: 250px !default;
$max-width-wide: $max-width + 2 * ($right-sidebar-width-wide - $right-sidebar-width) !default;
```
{: data-filename="_sass/minimal-mistakes/_variables.scss · 일부 발췌"}

`$max-width-wide`는 1280 + 2 × 50 = 1380px이다. 양쪽 칸이 각각 50px씩 늘어난 만큼 틀을 키우면, 가운데 본문 칸 폭은 `$x-large`일 때와 같다. 본문이 넓어지면 [본문 양끝맞춤](/ko/llm_workshop/kotex_justification)에서 맞춰 둔 한 줄 글자 수가 달라지므로, 이것이 지켜야 할 조건이었다. 변수 주석에는 넓어진 틀에 세로 스크롤바까지 들어간다고 적혀 있다. 그래서 틀(1380px)보다 조금 큰 1400px에서 켠다.

이 변수를 쓰는 자리는 한두 곳이 아니다. `$x-large`에서 `$max-width`나 `$right-sidebar-width`를 참조하던 곳마다 같은 모양의 블록이 하나씩 붙는다.

```scss
  @include breakpoint($x-large) {
    width: calc(100% - #{$right-sidebar-width});
    padding-right: $right-sidebar-width;
  }

  @include breakpoint($xx-large) {
    width: calc(100% - #{$right-sidebar-width-wide});
    padding-right: $right-sidebar-width-wide;
  }
```
{: data-filename="_sass/minimal-mistakes/_page.scss · 일부 발췌"}

같은 패턴을 본문뿐 아니라 마스트헤드, 사이드바, 목차, 검색 결과와 카테고리 페이지 등에도 적용했다. 어느 한 곳만 예전 폭으로 남으면 각 요소의 좌우 정렬이 어긋나기 때문이다. 양쪽 칸을 넓히는 일인데 수정할 파일도 양쪽으로 늘어났다.

## 넓은 칸에서 170px로 키운 프로필 사진

칸을 넓히고 나서 사용자가 사이드바를 다시 봤다.

> 혹시 왼쪽 사이드바에서 그 사진 있는 그쪽은 어때? 250px로 올라갔는데 그건 크기는 그대로, 가운데정렬만 됐는데 좀 이사한가?

칸이 250px가 됐는데 프로필 사진은 150px 그대로여서 가운데 정렬로 남는 여백만 늘었다는 지적이다. 사진 크기는 칸과 상관없이 `max-width: 150px`로 고정이었다. 같은 breakpoint 안에서 170px로 키웠다.

```scss
    @include breakpoint($xx-large) {
      max-width: 170px;
    }
```
{: data-filename="_sass/minimal-mistakes/_sidebar.scss · 일부 발췌"}

사진도 넓어진 칸에 맞게 조정한 뒤 작업을 마쳤다.
