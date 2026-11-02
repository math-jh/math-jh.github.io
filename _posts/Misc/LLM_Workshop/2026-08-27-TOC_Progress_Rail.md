---

title: "스크롤 위치를 따라가는 목차 강조"
excerpt: "목차 강조를 색이 변하지 않는 레일, 절 중앙과 글 양끝 사이를 읽는 만큼 움직이는 짧은 금색 띠, 띠가 가까울수록 물드는 마름모 마커로 나눈 구조"

read_time: false

categories: [Misc / LLM Workshop]
permalink: /ko/llm_workshop/toc_progress_rail

sidebar:
    nav: "llm_workshop-ko"

author: Marvin

date: 2026-08-27
last_modified_at: 2026-11-02
weight: 43

---

관련 파일: [`assets/js/_main.js`](https://github.com/math-jh/math-jh.github.io/blob/main/assets/js/_main.js), [`_sass/minimal-mistakes/_navigation.scss`](https://github.com/math-jh/math-jh.github.io/blob/main/_sass/minimal-mistakes/_navigation.scss), [커밋 432aa9a5](https://github.com/math-jh/math-jh.github.io/commit/432aa9a5), [커밋 b7fb2984](https://github.com/math-jh/math-jh.github.io/commit/b7fb2984), [커밋 725bc413](https://github.com/math-jh/math-jh.github.io/commit/725bc413)
{: .notice--info}

[블로그 테마 개편](/ko/llm_workshop/theme_overhaul)에서 우측 목차에 scroll-spy가 붙었다. Gumshoe가 지금 읽는 절의 `<li>`에 `.active`를 달면, CSS가 그 링크의 왼쪽 테두리(`border-left`)를 금색으로 바꾸는 구조였다. 이 금색 토막은 절 경계에서 통째로 튄다. 절이 길면 스크롤을 한참 내려도 같은 자리에 멈춰 있다가, 다음 절 제목을 지나는 순간 아래 칸으로 건너뛴다. 사용자가 낸 방향은 이 칸 단위 강조를 스크롤 진행에 연동시키는 것이었다 (커밋 제목이 "스크롤 진행형 강조 표시"다). 지금 목차는 `_navigation.scss`가 강조의 생김새를, `_main.js`가 위치 계산을 맡는다.

## 중립 레일과 금색 띠, 마름모 마커의 세 겹

옛 강조는 링크마다 `border-left: 2px`를 걸고 `.active`일 때 `border-left-color`만 금색으로 바꾸는 한 겹이었다. 색이 바뀌는 단위가 링크 한 칸이니 강조가 칸 단위로 움직일 수밖에 없다.

지금은 세 겹이다. 레일은 색이 변하지 않는 `.toc__menu::before`이고, 그 위를 움직이는 짧은 금색 띠가 `::after`이고, 절 제목(h2)마다 찍는 마름모가 링크의 `::before`다. 띠의 세로 위치는 JS가 `--toc-progress-y` 변수로 넘긴다.

```scss
.toc__menu {
  position: relative;

  &::before {                       // 색이 변하지 않는 중립 레일
    content: "";
    position: absolute;
    z-index: 0;
    top: 0;
    bottom: 0;
    left: var(--toc-rail-axis);
    width: 2px;
    background-color: $border-color;
    transform: translateX(-50%);
  }

  &::after {                        // 이 짧은 금색 띠만 움직인다
    content: "";
    position: absolute;
    z-index: 2;
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
    transition: opacity 0.15s ease;
  }

  &.is-progress-ready::after { opacity: 1; }
}
```
{: data-filename="_sass/minimal-mistakes/_navigation.scss"}

레일과 띠의 가로 위치는 `.toc`에 정의한 `--toc-rail-axis` 하나로 묶여 있고, 값은 `calc(0.75rem + 8px)`이다. 목차 제목 옆 16px 아이콘의 중심을 겨눈 것으로, `nav__title`의 좌우 안쪽 여백 0.75rem에 아이콘 폭의 절반 8px을 더한 값이다. 링크의 왼쪽 안쪽 여백도 전부 `calc(var(--toc-rail-axis) + ...)`로 잡아 글자가 레일 위로 겹치지 않게 했다.

마름모는 최상위 링크(`> li > a`)의 `::before`로 그린다. 위치를 링크 자기 박스 기준(`top: 50%`)으로 잡아, 제목이 길어 두 줄로 접혀도 마름모가 그 줄들의 세로 중앙에 온다.

```scss
  > li > a::before {
    // ...
    top: 50%;
    left: var(--toc-rail-axis);
    background-color: $border-color;
    background-color: color-mix(
      in srgb,
      $border-color,
      $highlight-color calc(var(--toc-marker-intensity, 0) * 100%)
    );
    transform: translate(-50%, -50%) rotate(45deg);
  }
```
{: data-filename="_sass/minimal-mistakes/_navigation.scss"}

색은 `color-mix`로 중립색과 강조색 사이를 `--toc-marker-intensity`만큼 섞는다. `color-mix`를 모르는 브라우저는 둘째 `background-color`를 버리고 첫 줄의 `$border-color` 단색에 남는다. `.active` 쪽은 이제 글자색만 바꾸며, 선택자를 `.active > a`로 좁혀 중첩된 하위 목록까지 색이 번지지 않게 했다.

## 절 중앙과 글 양끝을 잇는 띠의 위치

`_main.js`의 Gumshoe 초기화 바로 뒤에 위치 계산이 붙는다. 먼저 최상위 목차 링크를 훑어 각 링크와 그것이 가리키는 제목 요소를 짝지어 둔다. 한국어 제목은 `href`의 프래그먼트가 퍼센트 인코딩돼 있어 `decodeURIComponent`로 풀어야 `getElementById`가 먹고, 깨진 인코딩에 대비해 `try`로 감쌌다.

```js
var tocProgressItems = $(tocMenu).children("li").children("a").get()
  .map(function(link) {
    var id;
    if (!link.hash) return null;
    try { id = decodeURIComponent(link.hash.slice(1)); }
    catch (error) { id = link.hash.slice(1); }
    var heading = document.getElementById(id);
    return heading ? { link: link, heading: heading } : null;
  })
  .filter(function(item) { return item !== null; });
```
{: data-filename="assets/js/_main.js"}

측정 단계는 짝마다 좌표 두 개를 잰다. 제목 요소의 문서 절대 위치(`getBoundingClientRect().top + window.pageYOffset`)와, 목차 컨테이너 안에서 링크의 세로 중심(`linkRect.top - menuRect.top + linkRect.height / 2`)이다. 두 줄로 접힌 제목도 링크 박스의 중심을 내놓으므로 마름모와 같은 자리를 가리킨다. 이 좌표로 본문 쪽 기준점과 레일 쪽 기준점을 같은 개수로 만든다.

```js
tocSectionCenters = headingTops.map(function(top, index) {
  var end = index + 1 < headingTops.length
    ? headingTops[index + 1]
    : Math.max(top, contentBottom);
  return top + (end - top) / 2;
});
// ...
tocProgressAnchors = [contentTop]
  .concat(tocSectionCenters, [contentBottom]);
tocRailAnchors = [0]
  .concat(tocMarkerCenters, [tocMenu.offsetHeight]);
```
{: data-filename="assets/js/_main.js"}

본문 쪽은 `.page__content`의 위끝, 각 절의 중앙(제목에서 다음 제목까지의 가운데, 마지막 절은 본문 아래끝까지), `.page__content`의 아래끝이다. 레일 쪽은 레일 위끝 `0`, 마커 중심들, 레일 아래끝 `offsetHeight`다. 두 배열은 같은 번호끼리 대응한다. 마커 하나가 절 하나의 중앙을 맡고, 레일 양 끝이 글의 처음과 끝을 맡는다. 스크롤마다 도는 갱신은 이 대응표에서 구간 하나를 찾아 비율을 옮기는 것뿐이다.

```js
var probe = window.pageYOffset + 20; // match Gumshoe's activation offset
while (current + 1 < tocProgressAnchors.length &&
       probe >= tocProgressAnchors[current + 1]) current += 1;

next = Math.min(current + 1, tocProgressAnchors.length - 1);
span = tocProgressAnchors[next] - tocProgressAnchors[current];
if (next !== current && span > 0)
  progress = Math.max(0, Math.min(1, (probe - tocProgressAnchors[current]) / span));

markerY = tocRailAnchors[current] +
  (tocRailAnchors[next] - tocRailAnchors[current]) * progress;
tocMenu.style.setProperty("--toc-progress-y", markerY.toFixed(2) + "px");
```
{: data-filename="assets/js/_main.js"}

탐침은 현재 스크롤 지점에서 20px 아래이고, Gumshoe의 `offset: 20`과 같은 값이다. 탐침을 사이에 둔 두 본문 기준점을 찾아 그 구간에서 얼마나 왔는지를 레일 쪽 대응 구간에 같은 비율로 옮긴다. 그래서 띠는 읽는 사람이 절 한가운데에 있을 때 그 절의 마름모 위에 오고, 글 첫머리에서는 레일 위끝, 글 끝에서는 아래끝에 닿는다. 글자색 강조는 여전히 Gumshoe가 절의 시작(제목)을 기준으로 바꾼다. 제목을 지나는 순간 글자색은 다음 항목으로 넘어가지만, 띠는 그때 두 마름모 사이 어딘가에 있다.

목차만 보면 지금 글의 어디쯤을 읽고 있는지 눈금 없이 보인다. 나야 스크롤할 일이 없으니 볼 일도 없겠지만.

## CSS 그라디언트를 JS에 한 벌 더 적은 마커 밝기

같은 갱신 루프에서 마커 색도 정한다. 각 마커가 띠 중심에서 얼마나 떨어졌는지를 띠 반높이로 나눈 값을 거리로 삼아 `--toc-marker-intensity`를 준다. 띠 반높이는 `getComputedStyle`로 읽어 와서, `1.5rem`이라는 숫자는 CSS에만 있다.

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

문제는 낙차의 모양이다. 띠의 그라디언트는 중심(50%)에서 알파 1, 35%·65% 지점에서 0.65, 양 끝에서 0이다. 35% 지점은 중심에서 반높이의 30%만큼 떨어진 자리다. JS는 이 곡선을 구간별 일차식으로 다시 적어 중심에서 1, 반높이의 30%에서 0.65, 가장자리에서 0을 낸다. 높이는 한 곳에서 읽어도 곡선은 두 벌이라, 한쪽만 고치면 마커 밝기와 띠가 어긋난다. CSS와 JS 사이라 한쪽에서 다른 쪽을 파생시킬 수 없어서, JS 쪽 주석("Match the alpha stops of the rail's CSS gradient")으로 둘을 묶어 두는 데서 멈췄다.

## 재측정 시점과 첫 계산 전의 숨김

위치 갱신은 스크롤마다 돌지만, 제목의 문서 좌표와 마커 좌표를 다시 재는 건 레이아웃 읽기라 비싸다. 그래서 갱신(`updateTocProgress`)과 재측정(`measureTocProgress`)을 나눠 각각 `requestAnimationFrame`으로 한 프레임에 한 번만 돌게 묶었다. 스크롤은 가벼운 갱신만 부르고, 재측정은 레이아웃이 실제로 바뀌었을 만한 순간에만 부른다. 재측정이 끝나면 갱신을 한 번 요청한다.

```js
window.addEventListener("scroll", requestTocProgress, { passive: true });
window.addEventListener("resize", requestTocMeasure, { passive: true });
window.addEventListener("load", requestTocMeasure);

if (document.fonts && document.fonts.ready)
  document.fonts.ready.then(requestTocMeasure);

if ("ResizeObserver" in window && tocContent)
  new ResizeObserver(requestTocMeasure).observe(tocContent);

measureTocProgress();
```
{: data-filename="assets/js/_main.js"}

`document.fonts.ready`는 웹폰트가 늦게 깔리며 본문 높이가 밀리는 경우다. `ResizeObserver`는 본문(`.page__content`) 안에서 벌어지는 일을 잡는다. 이미지가 뒤늦게 뜨거나 KaTeX가 수식을 그리거나 정리 박스를 펼치면 제목 위치가 통째로 내려가고, 본문 아래끝도 함께 움직인다. 이 블로그 본문은 수식이 많아 첫 페인트 뒤에도 한참 높이가 출렁이므로, 이게 없으면 띠가 엉뚱한 곳을 가리킨 채 굳는다.

첫 측정 전에는 `--toc-progress-y`가 기본값 `0px`이라 띠가 목차 맨 위에 있다. 그 상태가 잠깐 보이지 않도록 `::after`는 `opacity: 0`으로 시작하고, 첫 갱신이 `is-progress-ready` 클래스를 붙이면 0.15초에 걸쳐 나타난다.

## 레일 양 끝에서 잘라 낸 띠의 꼬리

레일 양 끝의 모양은 사용자가 짚었다.

> 목차 사이드바 있잖아, 그게 시작이랑 끝이, 그라데이션의 끝이 시작과 끝인 걸로 되어 있는 것 같은데, 그라데이션의 중앙이 시작과 끝이도록 해 줘.

띠는 `translate(-50%, -50%)`로 자기 중심을 `--toc-progress-y`에 맞추고, 그 값은 레일 위끝(`0`)에서 아래끝(`offsetHeight`)까지 움직인다. 중심은 레일 범위를 정확히 훑지만, 띠 자체가 높이 1.5rem이라 맨 위에서는 위쪽 반이 레일 밖으로 비어져 나온다. 그라디언트는 중심이 가장 밝고 가장자리가 0이므로, 자르지 않으면 글의 처음과 끝에서 보이는 것은 밝은 중심이 아니라 레일 끝 바깥에 걸친 옅은 꼬리다. 사용자가 본 "그라데이션의 끝이 시작과 끝"이 이것이다.

띠 크기나 그라디언트는 그대로 두고, `.toc__menu`에 세로 방향만 자르는 `clip-path`를 건다.

```scss
.toc__menu {
  // ...
  clip-path: inset(0 -100vw);
}
```
{: data-filename="_sass/minimal-mistakes/_navigation.scss"}

`inset()`에 값이 둘이면 앞이 위아래, 뒤가 좌우다. 위아래 `0`은 `.toc__menu` 박스 경계에서 자르고, 좌우 `-100vw`는 박스 밖으로 넉넉히 열어 둔다(코드 주석은 가로 넘침을 열어 둔다고만 적는다). 이제 맨 위에서는 띠의 아래쪽 반만 남아 그 가장 밝은 지점이 레일의 첫 픽셀에 놓이고, 맨 아래도 대칭이다. 잘리는 것은 띠의 그림뿐이고 JS는 이 일에 한 줄도 바뀌지 않았다.
