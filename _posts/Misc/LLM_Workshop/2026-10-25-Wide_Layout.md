---

title: "큰 모니터에서 양쪽 칸만 넓히기"
excerpt: "사이드바·목차 글씨를 본문의 0.75배 한 곳으로 모으고, 1400px 이상에서 틀과 양쪽 칸을 50px씩 넓히되 본문 칸 폭은 그대로 두는 레이아웃"

read_time: false

categories: [Misc / LLM Workshop]
permalink: /ko/llm_workshop/wide_layout

sidebar:
    nav: "llm_workshop-ko"

author: Marvin

date: 2026-10-25
last_modified_at: 2026-11-02
weight: 60

---

관련 파일: [`_sass/minimal-mistakes/_variables.scss`](https://github.com/math-jh/math-jh.github.io/blob/main/_sass/minimal-mistakes/_variables.scss), [`_sass/minimal-mistakes/_navigation.scss`](https://github.com/math-jh/math-jh.github.io/blob/main/_sass/minimal-mistakes/_navigation.scss), [`_sass/minimal-mistakes/_sidebar.scss`](https://github.com/math-jh/math-jh.github.io/blob/main/_sass/minimal-mistakes/_sidebar.scss), [`_sass/minimal-mistakes/_page.scss`](https://github.com/math-jh/math-jh.github.io/blob/main/_sass/minimal-mistakes/_page.scss), [23f8cf26](https://github.com/math-jh/math-jh.github.io/commit/23f8cf26), [eea197ea](https://github.com/math-jh/math-jh.github.io/commit/eea197ea)
{: .notice--info}

데스크탑 화면으로 사이트를 둘러본 외부 리뷰가 사용자의 채팅에 통째로 붙여 넣어졌다. 꼭 고칠 것 첫 항목은 이랬다. 본문은 15.2px라 괜찮은데 왼쪽 사이드바는 약 10px, 오른쪽 목차는 약 10.5px라서 큰 모니터에서는 거의 읽을 수 없고, 12~13px까지 올리라는 것이었다.

숫자가 맞는지부터 확인해야 했다. 사이드바 글씨가 작은 것은 의도였지만, 10px까지 내려간 것은 의도가 아니었다.

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
{: data-filename="_sass/minimal-mistakes/_sidebar.scss"}

`0.75em`은 부모 글자 크기에 대한 비율이다. 사이드바의 카테고리 목록은 `li` 안에 `ul`이 들어가고 그 안에 다시 `li`가 있는 구조여서, 중첩된 `li`는 0.75 × 0.75 = 0.5625배가 된다. 본문이 15.2px이면 11.4px가 되어야 할 자리가 8.5px로 줄어든다. 오른쪽 목차는 `.toc__menu`가 `$type-size-6`을 주고 `$large` 이상에서 `$type-size-7`(0.6875em)로 한 번 더 줄이고 있었다. 15.2 × 0.6875 ≈ 10.5px로 리뷰의 숫자와 맞는다. 같은 "작은 글씨"를 만드는 방법이 규칙마다 달랐다.

사용자가 정한 것은 배율이었다. 제안된 12~13px(본문의 0.85배쯤)는 사이드바가 너무 커 보인다는 이유로 받아들이지 않았다.

> B가 낫겠지? 0.75 정도로 하고 싶어. 0.85는 사이드바가 너무 큰 것 같아서.

그래서 숫자를 올리는 대신, 이 배율이 한 곳에서만 정의되고 중첩에서 곱해지지 않게 만드는 일이 됐다.

```scss
// 왼쪽 사이드바·목차·의존성 그래프 제목. 부모가 본문 글자 크기인 자리에 건다.
$type-size-aside: 0.75em !default;
```
{: data-filename="_sass/minimal-mistakes/_variables.scss"}

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
{: data-filename="_sass/minimal-mistakes/_navigation.scss"}

nav 목록(`.nav__list .nav__items`)에서 한 번 0.75배로 줄이고, 그 안의 모든 `li`는 `inherit`으로 부모 크기를 그대로 받는다. 이 자리가 주던 `$type-size-4`와 안쪽 `a`의 `0.95em`은 지웠고, 목록 안의 `.nav__sub-title`도 `1em`이다. 목차 제목(`.toc .nav__title`), 목차 메뉴(`.toc__menu`), 의존성 그래프 위젯의 제목은 `$type-size-6` 대신 `$type-size-aside`를 쓰고, `.toc__menu`의 `$large` 블록은 같은 배율을 위해 지웠다. 카테고리 목록 페이지의 오른쪽 최근 글·댓글 칸(`_recents-sidebar.scss`)은 `li, p`에서 `font-size`를 빼고 크기를 `.nav__items`에 맡기며, 글꼴과 행간만 왼쪽 규칙을 복제한다.

## 1400px에서만 넓어지는 틀

커밋 메시지가 적은 방향은, 폭이 1400px 이상인 화면에서 양쪽 칸을 200px에서 250px로 늘리고 틀도 함께 넓히는 것이다. 이 테마의 폭은 전부 `$right-sidebar-width`와 `$max-width`에서 파생된다. `$right-sidebar-width-wide: 250px`는 정의만 있고 쓰이지 않던 변수이고, 여기에 breakpoint `$xx-large`와 넓은 틀 `$max-width-wide`를 더했다.

```scss
$xx-large: 1400px !default;

$right-sidebar-width: 200px !default;
$right-sidebar-width-wide: 250px !default;
$max-width-wide: $max-width + 2 * ($right-sidebar-width-wide - $right-sidebar-width) !default;
```
{: data-filename="_sass/minimal-mistakes/_variables.scss"}

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
{: data-filename="_sass/minimal-mistakes/_page.scss"}

같은 패턴이 `#main`, 마스트헤드, 브레드크럼, footer, 검색 결과 틀, hero, 그래프 페이지 틀, 왼쪽 `.sidebar`와 오른쪽 `.sidebar__right`의 폭, 오른쪽 sticky 칸(`.sidebar__right-slot`의 `right`·`width`), 카테고리 페이지의 2단 grid(`grid-template-columns: minmax(0, 1fr) $right-sidebar-width-wide`), 맨 위로 가기 버튼의 `right`에 들어갔다. 커밋은 `.scss` 열한 개를 건드렸다. 하나만 빠뜨리면 그 자리의 틀만 1280px에 남아서 마스트헤드 로고와 본문 사이에 어긋난 세로선이 생긴다.

## 넓은 칸에서 170px로 키운 프로필 사진

칸을 넓히고 나서 사용자가 사이드바를 다시 봤다.

> 혹시 왼쪽 사이드바에서 그 사진 있는 그쪽은 어때? 250px로 올라갔는데 그건 크기는 그대로, 가운데정렬만 됐는데 좀 이사한가?

칸이 250px가 됐는데 프로필 사진은 150px 그대로여서 가운데 정렬로 남는 여백만 늘었다는 지적이다. 사진 크기는 칸과 상관없이 `max-width: 150px`로 고정이었다. 같은 breakpoint 안에서 170px로 키웠다.

```scss
    @include breakpoint($xx-large) {
      max-width: 170px;
    }
```
{: data-filename="_sass/minimal-mistakes/_sidebar.scss"}

170이라는 값은 칸의 비율을 따른 것이 아니다. 칸은 25% 늘었고 사진은 13% 늘었다.

## 홈 과목 카드 문구의 ui-text 이전

같은 커밋에는 홈 과목 카드의 "Read more"와 "N subjects"가 `subject-grid.html`에 영어로 하드코딩돼 있던 것을 `ui-text.yml`로 옮기는 변경도 실려 있다(한국어는 "더 보기"·"과목 N개"). 복수형 처리는 `subject_count_one`과 `subject_count_other` 두 키를 두고 `__N__`을 치환하는 방식이다.
