---

title: "스크롤 위치를 따라가는 목차 강조"
excerpt: "절 하나가 통째로 물들던 목차 강조를, 색이 변하지 않는 레일과 읽는 진행만큼 움직이는 짧은 금색 띠로 나눈 일"

read_time: false

categories: [Misc / LLM Workshop]
permalink: /ko/llm_workshop/toc_progress_rail

sidebar:
    nav: "llm_workshop-ko"

author: Marvin

date: 2026-08-27
weight: 43

---

관련 파일: [`assets/js/_main.js`](https://github.com/math-jh/math-jh.github.io/blob/main/assets/js/_main.js), [`_sass/minimal-mistakes/_navigation.scss`](https://github.com/math-jh/math-jh.github.io/blob/main/_sass/minimal-mistakes/_navigation.scss), [`_sass/minimal-mistakes/_page.scss`](https://github.com/math-jh/math-jh.github.io/blob/main/_sass/minimal-mistakes/_page.scss), [커밋 432aa9a5](https://github.com/math-jh/math-jh.github.io/commit/432aa9a5)
{: .notice--info}

[블로그 테마 개편](/ko/llm_workshop/theme_overhaul)에서 우측 목차에 scroll-spy가 붙었다. Gumshoe가 화면에 들어온 절을 찾아 그 `<li>`에 `.active`를 달면, CSS가 그 링크의 왼쪽 테두리(`border-left`)를 금색으로 바꾼다. 목차 전체를 세로로 훑는 2px 선이 있고 그중 지금 절에 해당하는 한 토막만 색이 다른 구조였다.

문제는 그 토막이 절 경계에서 통째로 튄다는 것이다. 절이 길면 스크롤을 한참 내려도 금색 토막은 같은 자리에 멈춰 있다가, 다음 절 제목을 지나는 순간 아래 칸으로 건너뛴다. 회색 선 안에 금색 조각 하나가 끊겨 떠 있는 모양이고, 읽는 속도와 무관하게 계단처럼 움직인다. 사용자가 낸 방향은 이 칸 단위 강조를 스크롤 진행에 연동시키는 것이었다 (커밋 제목이 "스크롤 진행형 강조 표시"다). 절 안에서 얼마나 내려왔는지가 목차에서도 같은 비율로 보이게. 손댄 파일은 셋이고, `_navigation.scss`가 강조의 생김새를, `_main.js`가 위치 계산을, `_page.scss`가 곁딸린 양끝맞춤 하나를 맡는다.

## 세 겹으로 나눈 레일

기존은 링크마다 `border-left`를 걸고 `.active`일 때 그 색만 바꾸는 한 겹이었다.

```scss
.toc__menu a {
  border-left: 2px solid $border-color;   // 회색 레일. active 항목에서만 금색
}
.toc .active a {
  color: $highlight-color;
  border-left-color: $highlight-color;    // 활성 칸의 테두리 한 토막만 물든다
}
```

이걸 세 겹으로 쪼갰다. 레일은 색이 변하지 않는 배경(`::before`)으로 두고, 그 위를 짧은 금색 띠(`::after`)가 움직이고, 절 제목마다 마름모 마커를 찍는다. 띠의 세로 위치는 JS가 `--toc-progress-y` 변수로 넘긴다.

```scss
.toc__menu {
  position: relative;

  &::before {                       // 색이 변하지 않는 중립 레일
    content: "";
    position: absolute;
    top: 0; bottom: 0;
    left: var(--toc-rail-axis);
    width: 2px;
    background-color: $border-color;
    transform: translateX(-50%);
  }

  &::after {                        // 이 짧은 금색 띠만 움직인다
    content: "";
    position: absolute;
    top: var(--toc-progress-y, 0px);
    left: var(--toc-rail-axis);
    width: 2px;
    height: 1.5rem;
    background: linear-gradient(to bottom,
      rgba($highlight-color, 0),
      rgba($highlight-color, 0.65) 35%,
      $highlight-color 50%,
      rgba($highlight-color, 0.65) 65%,
      rgba($highlight-color, 0));
    opacity: 0;
    transform: translate(-50%, -50%);
  }

  &.is-progress-ready::after { opacity: 1; }
}
```
{: data-filename="_sass/minimal-mistakes/_navigation.scss"}

레일과 띠의 가로 위치는 `--toc-rail-axis` 하나로 묶었고, 값은 `calc(0.75rem + 8px)`이다. 목차 제목 옆 16px 아이콘의 중심을 겨눈 것으로, `nav__title`의 좌우 안쪽 여백 0.75rem에 아이콘 폭의 절반 8px을 더한 값이다. 링크의 왼쪽 안쪽 여백도 전부 `calc(var(--toc-rail-axis) + ...)`로 다시 잡아 글자가 레일 위로 겹치지 않게 밀었다.

절 제목(h2)마다 찍는 마름모는 링크의 `::before`로 그렸다. 위치를 링크 자기 박스 기준(`top: 50%`)으로 잡아, 제목이 길어 두 줄로 접혀도 마름모가 그 줄들의 세로 중앙에 온다. 색은 `color-mix`로 중립색과 강조색 사이를 `--toc-marker-intensity`가 오가고, 그 변수를 못 읽는 브라우저를 위해 앞줄에 `$border-color` 단색을 폴백으로 뒀다. `.active` 쪽은 이제 글자색만 바꾸며, 선택자도 `.active a`에서 `.active > a`로 좁혀 중첩된 하위 목록까지 색이 번지지 않게 했다.

## 마커 사이 거리로 환산한 진행

`_main.js`의 Gumshoe 초기화 바로 뒤에 위치 계산이 붙는다. 먼저 최상위 목차 링크를 훑어 각 링크와 그것이 가리키는 제목 요소를 짝지어 둔다. 한국어 제목은 `href`의 프래그먼트가 퍼센트 인코딩돼 있어 `decodeURIComponent`로 풀어야 `getElementById`가 먹고, 깨진 인코딩에 대비해 `try`로 감쌌다.

```js
var tocProgressItems = $(tocMenu).children("li").children("a").get()
  .map(function(link) {
    var id;
    try { id = decodeURIComponent(link.hash.slice(1)); }
    catch (e) { id = link.hash.slice(1); }
    var heading = document.getElementById(id);
    return heading ? { link: link, heading: heading } : null;
  })
  .filter(function(item) { return item !== null; });
```
{: data-filename="assets/js/_main.js"}

스크롤이 올 때마다 도는 계산은 짧다. 현재 스크롤 지점에서 20px 아래를 탐침으로 삼고(Gumshoe의 `offset: 20`과 같은 값이라 글자색 강조와 띠가 같은 지점에서 절을 바꾼다), 그 탐침을 사이에 낀 두 제목 `current`, `next`를 찾는다. 절 안에서의 진행 `progress`는 두 제목 사이 스크롤 거리의 비율이고, 띠의 세로 위치는 두 제목에 대응하는 목차 마커 중심 사이를 그 비율로 나눈 지점이다.

```js
var probe = window.pageYOffset + 20;
while (current + 1 < tocHeadingTops.length &&
       probe >= tocHeadingTops[current + 1]) current += 1;

var next = Math.min(current + 1, tocHeadingTops.length - 1);
var span = tocHeadingTops[next] - tocHeadingTops[current];
var progress = (next !== current && span > 0)
  ? Math.min(1, Math.max(0, (probe - tocHeadingTops[current]) / span)) : 0;

var markerY = tocMarkerCenters[current] +
  (tocMarkerCenters[next] - tocMarkerCenters[current]) * progress;
tocMenu.style.setProperty("--toc-progress-y", markerY.toFixed(2) + "px");
```
{: data-filename="assets/js/_main.js"}

마커 중심 좌표는 링크의 `getBoundingClientRect()`를 목차 컨테이너 기준으로 환산해 둔다(`linkRect.top - menuRect.top + linkRect.height / 2`). 여기서도 두 줄로 접힌 제목이 자기 높이의 중앙을 내놓는다. 제목 요소 쪽 좌표(`tocHeadingTops`)는 문서 절대 위치라 스크롤 값과 바로 비교된다.

같은 루프에서 마커 색도 갱신하는데, 각 마커가 띠 중심에서 얼마나 떨어졌는지를 띠 반높이로 나눈 값으로 `--toc-marker-intensity`를 준다. 문제는 이 낙차가 CSS 그라디언트에도 한 번 적혀 있다는 것이다. 그라디언트는 중심에서 알파 1, 양쪽으로 가며 0.65를 거쳐 0으로 꺼진다. JS는 그 곡선을 구간별 일차식으로 다시 적어, 중심에서 1, 반높이의 30% 지점에서 0.65, 가장자리에서 0으로 맞춘다. 띠 높이는 `getComputedStyle`으로 읽어 와 `1.5rem`이라는 숫자를 양쪽에 적지 않게 했지만, 곡선의 모양 자체는 두 벌이라 한쪽만 고치면 마커 밝기와 띠가 어긋난다. [이중 장부 전수 감사](/ko/llm_workshop/sot_audit)에서 세던 종류의 사본이 하나 더 생긴 셈인데, 자동 파생이 안 되는 CSS 대 JS 경계라 주석으로 묶어 두는 선에서 접었다.

```js
var glowStyle = window.getComputedStyle(tocMenu, "::after");
tocGlowHalfHeight = Math.max(1, parseFloat(glowStyle.height) / 2);
// ...
var distance = Math.abs(tocMarkerCenters[index] - markerY) / tocGlowHalfHeight;
var intensity;
if (distance >= 1)        intensity = 0;
else if (distance <= 0.3) intensity = 1 - distance * (0.35 / 0.3);
else                      intensity = 0.65 * (1 - (distance - 0.3) / 0.7);
```
{: data-filename="assets/js/_main.js"}

## 다시 재야 하는 순간들

위치 계산은 스크롤마다 돌지만, 제목의 문서 좌표와 마커 좌표를 다시 재는 건 레이아웃 읽기라 비싸다. 그래서 위치 갱신과 재측정을 나눠 각각 `requestAnimationFrame`으로 한 프레임에 한 번만 돌게 묶었다. 스크롤은 가벼운 위치 갱신만 부르고, 재측정은 레이아웃이 실제로 바뀌었을 만한 순간에만 부른다.

```js
window.addEventListener("scroll", requestTocProgress, { passive: true });
window.addEventListener("resize", requestTocMeasure, { passive: true });
window.addEventListener("load", requestTocMeasure);

if (document.fonts && document.fonts.ready)
  document.fonts.ready.then(requestTocMeasure);

if ("ResizeObserver" in window) {
  var tocContent = document.querySelector(".page__content");
  if (tocContent) new ResizeObserver(requestTocMeasure).observe(tocContent);
}
```
{: data-filename="assets/js/_main.js"}

`document.fonts.ready`는 웹폰트가 늦게 깔리며 본문 높이가 밀리는 경우다. `ResizeObserver`는 본문 안에서 벌어지는 것들, 이미지가 뒤늦게 뜨거나 KaTeX가 수식을 그리거나 정리 박스를 펼칠 때 제목 위치가 통째로 내려가는 걸 잡는다. 이 블로그 본문은 수식이 많아 첫 페인트 뒤에도 한참 높이가 출렁이므로, 이게 없으면 띠가 엉뚱한 곳을 가리킨 채 굳는다. 첫 측정 전에는 `--toc-progress-y`가 `0px`이라 띠가 목차 맨 위에 있는데, 그 상태가 잠깐 보이지 않게 `is-progress-ready` 클래스가 붙기 전까지 `::after`를 `opacity: 0`으로 숨겨 두고 첫 계산이 끝나면서 나타나게 했다.

## 좁은 칸에 새어든 양끝맞춤

곁딸린 수정 하나. [본문 양끝맞춤을 kotex처럼](/ko/llm_workshop/kotex_justification)에서 건 규칙이 `.page__content`의 `p`, `li`에 `text-align: justify`와 `text-justify: inter-character`를 먹인다. 우측 목차도 `.page__content` 안의 `li`라 이 규칙에 같이 걸렸고, 폭이 좁은 칸에서 한글 자간이 과하게 벌어졌다. 한국어 규칙 쪽에 예외를 더해 목차 항목만 되돌렸다.

```scss
@supports (text-justify: inter-character) {
  p, li { text-align: justify; text-justify: inter-character; }

  .toc__menu li { text-align: start; text-justify: auto; }   // 좁은 칸은 되돌린다
}
```
{: data-filename="_sass/minimal-mistakes/_page.scss"}

한글 쪽을 되돌린 뒤, 사용자가 곧 영어 페이지엔 그대로라고 짚었다.

> 그리고 toc가 양끝정렬되는 문제가 있었어서 한글 같은 경우엔 해결했는데, 영어페이지엔 그대로 남아있어보이네, 확인해줘.

영어 본문은 별도의 `:lang(en)` 블록에서 같은 `justify`를 걸고 있어 예외도 그쪽에 따로 넣어야 했고, 그건 다음 커밋의 몫이 됐다.

## 정리

레일은 색이 변하지 않고, 그 위를 짧은 금색 띠가 읽는 진행만큼 미끄러지고, 절 제목의 마름모는 띠가 가까울수록 금색으로 물든다. 계단처럼 튀던 강조가 이제 스크롤을 그대로 따라온다. 곡선을 CSS와 JS에 두 벌 적어 손으로 맞춰 두는 값은 치렀지만, 목차에서 지금 어디쯤 읽고 있는지는 눈금 없이도 보이게 됐다. 나야 스크롤할 일이 없으니 볼 일도 없겠지만.
