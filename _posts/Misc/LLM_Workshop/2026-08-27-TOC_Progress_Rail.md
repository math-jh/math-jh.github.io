---

title: "스크롤 위치를 따라가는 목차 강조"
excerpt: "절마다 건너뛰던 목차 강조를 스크롤에 따라 움직이는 금색 띠로 바꾸고, 본문과 목차의 위치를 대응시키는 방식"

read_time: false

categories: [Misc / LLM Workshop]
permalink: /ko/llm_workshop/toc_progress_rail

sidebar:
    nav: "llm_workshop-ko"

author: Marvin

date: 2026-08-27
weight: 43
group: features

---

관련 파일: [`assets/js/_main.js`](https://github.com/math-jh/math-jh.github.io/blob/main/assets/js/_main.js), [`_sass/minimal-mistakes/_navigation.scss`](https://github.com/math-jh/math-jh.github.io/blob/main/_sass/minimal-mistakes/_navigation.scss), [커밋 432aa9a5](https://github.com/math-jh/math-jh.github.io/commit/432aa9a5), [커밋 b7fb2984](https://github.com/math-jh/math-jh.github.io/commit/b7fb2984), [커밋 725bc413](https://github.com/math-jh/math-jh.github.io/commit/725bc413)
{: .notice--info}

## 기존 목차와 현재 절 강조

이 블로그가 쓰는 Minimal Mistakes 테마는 글의 제목들을 모아 목차를 만들고, 각 항목을 해당 제목의 앵커로 연결한다. 목차를 누르면 그 절로 이동한다. 여기에 스크롤 위치에 맞춰 현재 절의 항목을 강조하는 기능도 있다. 이렇게 본문 위치를 추적해 탐색 메뉴에 반영하는 scroll-spy 기능은 이 테마에서는 Gumshoe라는 JavaScript 라이브러리가 맡는다. Gumshoe는 목차 링크가 가리키는 제목들의 위치를 확인하고, 스크롤할 때 현재 읽는 절에 해당하는 목차 항목에 `.active` 클래스를 붙인다. 이렇게 Gumshoe가 어떤 항목이 활성 상태인지 표시하면, 테마의 CSS가 `.active`를 선택해 모양을 바꾼다.

이 블로그의 기존 CSS는 활성 항목의 글자색과 왼쪽 테두리를 금색으로 바꿨다. 각 링크에 세로 테두리가 하나씩 있으므로, 현재 절에 해당하는 한 칸만 금색으로 보였다. 절이 길면 한참 스크롤해도 강조가 제자리에 머물고, 다음 제목을 지나면 아래 항목으로 통째로 옮겨 갔다. 현재 절은 알 수 있지만, 그 절을 얼마나 읽었는지는 드러나지 않는 방식이다.

사용자는 강조가 스크롤 진행에 따라 조금씩 움직이기를 원했다. 그래서 Gumshoe의 현재 항목 판정과 글자색 강조는 유지하고, 본문 위치를 별도로 계산해 목차 옆의 금색 띠를 움직이게 했다. CSS는 띠의 모양을, `assets/js/_main.js`는 위치 계산을 맡는다.

## 세로선과 이동하는 강조 띠

새 구현에서는 각 링크의 왼쪽 테두리를 없애고, 목차의 맨 위부터 맨 아래까지 이어지는 옅은 세로선 하나를 그린다. 이 선은 그대로 두고, 그 위에 짧은 금색 띠를 겹쳐 스크롤할수록 아래로 움직이게 한다. 선 전체의 색이 변하는 것이 아니라, 현재 읽는 위치를 나타내는 띠만 이동하는 것이다.

동작을 나누는 아이디어는 Gumshoe와 같다. JavaScript가 스크롤 위치를 계산해 상태를 전달하면, CSS가 그 상태에 맞춰 화면을 그린다. 차이점은 Gumshoe는 현재 절을 `.active` 클래스로 표시하고, 별도로 추가한 진행 띠 코드는 띠의 세로 좌표를 CSS 변수 `--toc-progress-y`에 넣는다는 것 정도이다. 

CSS는 목차 목록인 `.toc__menu`의 `::before`에 고정된 세로선을, `::after`에 움직이는 띠를 그린다. 여기서 `::after`가 JS에서 받은 좌표를 위치로 사용하여 금색 세로선을 그려주게 되는 것이다. 아래 코드의 `&::after`는 `.toc__menu::after`를 뜻하고, `top: var(--toc-progress-y, 0px)`가 그 좌표를 읽는 부분이다. 본문의 섹션 제목에 해당하는 항목 옆에는 작은 마름모도 놓는다. 마름모는 선 위의 고정된 눈금 역할을 한다. 금색 띠가 가까워지면 함께 금색으로 밝아지고, 멀어지면 다시 옅은 색으로 돌아간다.

```scss
&::after {
  content: "";
  position: absolute;
  z-index: 2;
  top: var(--toc-progress-y, 0px);
  left: var(--toc-rail-axis);
  width: 2px;
  height: 1.5rem;
  background: linear-gradient(
    to bottom,
    rgba($highlight-color, 0),
    rgba($highlight-color, 0.65) 35%,
    $highlight-color 50%,
    rgba($highlight-color, 0.65) 65%,
    rgba($highlight-color, 0)
  );
  opacity: 0;
  transform: translate(-50%, -50%);
  transition: opacity 0.15s ease;
  pointer-events: none;
}
```
{: data-filename="_sass/minimal-mistakes/_navigation.scss · 일부 발췌"}

띠는 가운데가 가장 밝고 양 끝으로 갈수록 투명해진다. JS가 `--toc-progress-y`에 세로 좌표를 넣으면, `top`과 `translate(-50%, -50%)`가 띠의 중심을 그 위치에 맞춘다. 따라서 이 값 하나를 갱신하면 띠 전체가 위아래로 움직인다. 세로선과 띠, 마름모는 모두 같은 가로 좌표 `--toc-rail-axis`를 사용한다. 마름모는 각 링크 높이의 가운데에 놓는다. 긴 절 제목이 두 줄로 접혀도 한쪽 줄에 치우치지 않고 항목 전체의 중앙을 가리키게 했다. 기존 `.active`는 글자색만 바꾸며, 강조 띠의 위치와는 별도로 동작한다.

## 본문과 목차의 위치 대응

다소 주의할 것은 본문 전체에서 몇 퍼센트를 읽었는지만 목차 높이에 곱하면, 절마다 길이가 다르다는 사실을 반영할 수 없다는 것이다. 예를 들어 본문 절 하나가 글의 절반을 차지해도 목차에서는 한 줄일 수 있다. 그래서 본문과 목차에 서로 대응하는 기준점들을 만들고, 그 사이를 같은 비율로 이동시켜야 한다. 처음에는 절 제목을 기준점으로 썼지만, 사용자의 방향대로 각 절의 중앙을 그 절의 마름모에 대응시켰다. 여기서 중앙은 제목에서 다음 최상위 제목까지의 세로 거리 중간이고, 마지막 절은 본문 끝까지의 중간이다. 본문 시작과 끝은 각각 목차 세로선의 위끝과 아래끝에 대응한다.

먼저 최상위 목차 링크와 실제 제목 요소를 짝지어 제목의 문서 좌표를 잰다. 목차 쪽에서는 각 링크의 세로 중심을 구한다. 두 줄짜리 항목도 이 중심을 쓰므로, 마름모와 띠가 만나는 위치가 일치한다.

```js
tocSectionCenters = headingTops.map(function(top, index) {
  var end = index + 1 < headingTops.length
    ? headingTops[index + 1]
    : Math.max(top, contentBottom);
  return top + (end - top) / 2;
});
tocMarkerCenters = tocProgressItems.map(function(item) {
  var linkRect = item.link.getBoundingClientRect();
  return linkRect.top - menuRect.top + linkRect.height / 2;
});
tocProgressAnchors = [contentTop]
  .concat(tocSectionCenters, [contentBottom]);
tocRailAnchors = [0]
  .concat(tocMarkerCenters, [tocMenu.offsetHeight]);
```
{: data-filename="assets/js/_main.js · 일부 발췌"}

본문 쪽 배열은 글 시작·절 중앙들·글 끝이고, 목차 쪽 배열은 선의 위끝·마름모 중심들·선의 아래끝이다. 같은 번호끼리 한 쌍이다. 예를 들어 스크롤 위치가 첫 절 중앙과 둘째 절 중앙 사이의 4분의 1 지점이면, 띠도 첫 마름모에서 둘째 마름모로 가는 거리의 4분의 1만큼 이동한다. 긴 본문 구간에서는 천천히 움직이고, 짧은 구간에서는 같은 스크롤 거리에도 더 많이 움직이는 셈이다.

현재 읽는 위치는 화면 위에서 20px 아래로 잡는다. Gumshoe가 절을 전환하는 기준과 같은 값이다. 스크롤할 때는 이 위치를 사이에 둔 두 본문 기준점을 찾고, 해당 구간에서 이동한 비율을 계산한다.

```js
next = Math.min(current + 1, tocProgressAnchors.length - 1);
span = tocProgressAnchors[next] - tocProgressAnchors[current];

if (next !== current && span > 0) {
  progress = Math.max(
    0,
    Math.min(1, (probe - tocProgressAnchors[current]) / span)
  );
}

markerY = tocRailAnchors[current] +
  (tocRailAnchors[next] - tocRailAnchors[current]) * progress;

tocMenu.style.setProperty("--toc-progress-y", markerY.toFixed(2) + "px");
```
{: data-filename="assets/js/_main.js · 일부 발췌"}

계산한 비율을 목차의 두 대응 좌표 사이에 적용해 띠 중심의 위치를 구한다. 본문 시작 전에는 비율을 0으로, 끝을 넘으면 마지막 좌표로 제한하므로 띠의 중심은 선의 범위를 벗어나지 않는다.

글자색과 띠는 서로 다른 정보를 준다. 글자색은 절 제목을 지날 때 다음 항목으로 바뀌지만, 띠는 절 중앙들을 기준으로 계속 움직인다. 따라서 다음 절 제목을 막 지났을 때 글자색은 이미 다음 항목을 가리키고, 띠는 두 마름모 사이에 있을 수 있다.

## 마름모 밝기와 세로선 양 끝

마름모는 강조 띠의 중심에서 가까울수록 밝아진다. JS는 마름모와 띠 중심의 거리를 띠 높이의 절반으로 나누어, 중심에서는 강조색을 전부 쓰고 가장자리에서는 중립색만 쓰도록 밝기를 계산한다. 그 값을 `--toc-marker-intensity`로 전달하면 CSS의 `color-mix`가 두 색을 섞는다.

띠의 높이는 `getComputedStyle`로 CSS에서 읽는다. 다만 밝기가 줄어드는 모양은 CSS 그라디언트와 JS 계산에 각각 적혀 있다. 중심에서 1, 반높이의 30% 지점에서 0.65, 가장자리에서 0이 되도록 맞춘 것이다. 그라디언트의 색 정지점을 바꾸면 JS 계산도 함께 바꿔야 한다. 현재 구현은 이 대응을 코드 주석으로 남겨 두고 있다.

이후 사용자는 글의 시작과 끝에서 띠가 보이는 모양도 짚었다.

> 목차 사이드바 있잖아, 그게 시작이랑 끝이, 그라데이션의 끝이 시작과 끝인 걸로 되어 있는 것 같은데, 그라데이션의 중앙이 시작과 끝이도록 해 줘.

띠의 중심은 이미 선의 위끝에서 아래끝까지 움직였지만, 띠 자체에는 높이가 있어 양 끝에서 절반이 선 밖으로 나왔다. 이 부분은 위치 계산을 바꾸지 않고, 목차 메뉴의 위아래 경계에서 그림을 자르는 것으로 처리했다.

```scss
clip-path: inset(0 -100vw);
```
{: data-filename="_sass/minimal-mistakes/_navigation.scss · 일부 발췌"}

`inset()`의 첫 값 `0`은 위아래를 메뉴 경계에 맞춰 자르고, 둘째 값 `-100vw`는 좌우의 잘라 내는 경계를 넓힌다. 그래서 가로로 나온 요소는 유지하면서 띠의 위아래 돌출 부분만 숨긴다. 맨 위에서는 띠의 아래쪽 절반, 맨 아래에서는 위쪽 절반이 남아 가장 밝은 중심이 선 끝에 놓인다.

## 레이아웃 변경과 재측정

본문과 목차의 좌표를 처음 한 번만 재면, 이미지나 수식이 늦게 그려진 뒤에는 대응이 어긋난다. 웹폰트가 적용되어 줄바꿈이 달라지거나 접힌 증명을 펼칠 때도 뒤쪽 제목의 위치가 바뀐다.

그래서 좌표를 재는 `measureTocProgress`와 이미 잰 좌표로 띠를 옮기는 `updateTocProgress`를 나눴다. 스크롤할 때는 위치 갱신만 요청한다. 창 크기 변경, 페이지 로드, 웹폰트 준비가 끝났을 때는 좌표를 다시 잰다. 본문에는 `ResizeObserver`를 붙여 크기 변화가 생길 때도 재측정을 요청한다.

```js
var requestTocProgress = function() {
  if (tocProgressFrame !== null) return;
  tocProgressFrame = window.requestAnimationFrame(updateTocProgress);
};
```
{: data-filename="assets/js/_main.js · 일부 발췌"}

스크롤 이벤트가 한 화면 갱신 사이에 여러 번 발생해도, 이미 예약한 갱신이 있으면 추가로 예약하지 않는다. 브라우저가 다음 화면을 그리기 전에 한 번만 실행하도록 `requestAnimationFrame`으로 묶은 것이다. 재측정 요청도 같은 방식으로 합치고, 측정이 끝나면 위치를 한 번 갱신한다.

첫 계산 전에는 띠를 숨긴다. 아직 좌표가 없는 상태에서 목차 맨 위에 나타났다 이동하는 것을 막기 위해서다. 첫 갱신이 끝나 `is-progress-ready` 클래스가 붙으면 띠가 나타난다.
