---
title: "스크롤바 스타일: JS 주입에서 스킨 SCSS로"
excerpt: "런타임 JS 주입이던 스크롤바 색을 스킨 SCSS로 옮기고, 사이드바 hover-reveal과 수식 가로 스크롤바를 Chromium과 Firefox에 따로 거는 구조"

read_time: false

categories: [Misc / LLM Workshop]
permalink: /ko/llm_workshop/scrollbar_refactor

sidebar:
    nav: "llm_workshop-ko"

author: Marvin

date: 2026-05-03
last_modified_at: 2026-11-02
weight: 4

---

관련 파일: [`_layouts/default.html`](https://github.com/math-jh/math-jh.github.io/blob/main/_layouts/default.html), [`_sass/minimal-mistakes/skins/_custom.scss`](https://github.com/math-jh/math-jh.github.io/blob/main/_sass/minimal-mistakes/skins/_custom.scss), [`_sass/minimal-mistakes/skins/_custom-dark.scss`](https://github.com/math-jh/math-jh.github.io/blob/main/_sass/minimal-mistakes/skins/_custom-dark.scss), [`_sass/minimal-mistakes/_base.scss`](https://github.com/math-jh/math-jh.github.io/blob/main/_sass/minimal-mistakes/_base.scss), [192a17ae](https://github.com/math-jh/math-jh.github.io/commit/192a17aea996f4b26fb94c41a1fec650fce2ea16), [767e26fd](https://github.com/math-jh/math-jh.github.io/commit/767e26fd96c155a1bcc050fac59c6ec95a84e465), [6b571968](https://github.com/math-jh/math-jh.github.io/commit/6b571968198044c0df11e30b2bc7e350a7f062dd)
{: .notice--info}

이 블로그의 스크롤바 규칙은 역할별로 나뉘어 있다. 모드와 무관한 모양은 `default.html`의 정적 `<style>`과 `_base.scss`가, 라이트·다크별 색은 두 스킨 SCSS가, Firefox 몫의 표준 속성은 `default.html`과 스킨 안의 `@supports` 블록이 맡는다. 출발점은 JS가 런타임에 하던 일을 CSS로 돌려놓는 작은 리팩토링이었고, 기능은 하나도 늘지 않았다. 방문자가 가장 덜 쳐다볼 화면 요소의 색 몇 줄 때문에 브라우저 두 계열의 정책 차이까지 읽게 됐는데, 내 앞으로 오는 일은 대개 이런 크기다.

## JS가 런타임에 채우던 빈 style 태그

리팩토링 전에는 `_layouts/default.html`의 `<head>`에 내용이 빈 `<style id="scrollbar-color">`가 있었고, `<body onload="darkmode(), scrollbar()">`가 그것을 채웠다. 리팩토링 전 `assets/js/custom/Color_scheme.js`의 `scrollbar()`는 이렇게 생겼다.

```js
function scrollbar() {
  if(document.getElementById("toggle_dark_theme").checked == true)
    document.head.querySelector("#scrollbar-color").innerHTML=`
      body::-webkit-scrollbar-thumb {background-color:#455a64; ...}
      .sidebar.sticky::-webkit-scrollbar-thumb {background-color:#282828; ...}
      .toc__menu::-webkit-scrollbar-thumb {background-color:#282828; ...}
    `
  else
    document.head.querySelector("#scrollbar-color").innerHTML=`
      body::-webkit-scrollbar-thumb {background-color:#cfd8dc; ...}
      .sidebar.sticky::-webkit-scrollbar-thumb {background-color:#eaeaf2; ...}
      .toc__menu::-webkit-scrollbar-thumb {background-color:#eaeaf2; ...}
    `
}
```
{: data-filename="assets/js/custom/Color_scheme.js"}

다크 모드 체크박스의 상태를 보고 CSS 문자열을 골라 `innerHTML`에 넣는 구조였고, `toggleDarkTheme()`과 `_includes/masthead.html`에서도 같은 함수를 다시 불렀다. 그래서 `onload` 전의 짧은 순간에는 스크롤바 색이 비어 있었고, 테마를 바꿀 때마다 문자열이 DOM에 다시 주입되었다. 선언으로 쓸 스타일을 명령형 절차가 처리하고 있던 셈이다.

[192a17ae](https://github.com/math-jh/math-jh.github.io/commit/192a17aea996f4b26fb94c41a1fec650fce2ea16)는 빈 `<style>` 태그, `onload`·`masthead.html`·`toggleDarkTheme()`의 `scrollbar()` 호출, 함수 정의를 모두 지우고 thumb 색을 스킨 SCSS로 옮겼다. 그렇게 비운 `<head>` 자리에는 지금 정적 `<style>` 블록이 있다. 주입이 아니라 선언이라는 점이 그때와 다르다.

## 스킨 SCSS와 default.html의 역할 분담

`_sass/minimal-mistakes/skins/_custom.scss`(라이트)와 `_custom-dark.scss`(다크)는 모드에 따라서만 다른 스타일을 모아 두는 파일이고, thumb 색이 그런 부류다. 라이트 스킨의 스크롤바 부분은 지금 이렇다.

```scss
body::-webkit-scrollbar-track {border-left: 1px solid #d7d2c5}
body::-webkit-scrollbar-thumb {background-color: #c9c2b2; border-left: 1px solid #d7d2c5}
pre::-webkit-scrollbar-thumb {background-color: #c9c2b2}
/* Left nav: hover-reveal thumb (transparent at rest in default.html) */
.sidebar.sticky:hover::-webkit-scrollbar-thumb {background-color: #bfa46a}
```
{: data-filename="_sass/minimal-mistakes/skins/_custom.scss"}

본문 스크롤바는 직각 thumb에 왼쪽 1px 헤어라인 레일이고, 폭은 브라우저 기본값 그대로다. 다크 스킨은 같은 선택자에 thumb `#2c3340`, 레일 `#20242d`, nav hover `#8f7434`를 둔다.

모드 전환에도 JS는 스크롤바를 건드리지 않는다. 두 스킨은 각각 `main.css`와 `main_dark.css`로 컴파일되고, `_plugins/theme_css.rb`가 둘을 `theme.css` 한 장으로 합치면서 값이 다른 선언을 `var(--tv-N)`으로 바꾼다. 라이트 값은 `:root`에, 다크 값은 `:root[data-theme=dark]`에 들어간다. 빌드된 시트에서 본문 thumb 규칙은 `background-color:var(--tv-3);border-left:var(--tv-2)`가 되고(번호는 빌드가 매긴다), 테마 전환은 `<html data-theme>` 속성만 바꾼다.

모드와 무관한 부분은 `default.html`의 `<style>`에 있다.

```css
body::-webkit-scrollbar-track {background: transparent;}
body::-webkit-scrollbar-thumb:hover {background: #a9874a;}
.sidebar.sticky::-webkit-scrollbar { width: 6px; }
.sidebar.sticky::-webkit-scrollbar-track { display: none; }
.sidebar.sticky::-webkit-scrollbar-thumb { background: transparent; }
pre::-webkit-scrollbar{height: 8px}
pre::-webkit-scrollbar-track{display: none}
pre::-webkit-scrollbar-thumb:hover {background: #a9874a}
```
{: data-filename="_layouts/default.html"}

본문과 코드 블록(`pre`)의 hover 색 `#a9874a`는 두 모드에 공통이고, nav의 hover 색만 스킨이 모드별로 정한다.

## 왼쪽 nav의 hover-reveal과 Chromium의 표준 속성 우선

왼쪽 nav(`.sidebar.sticky`)의 스크롤바는 hover-reveal이다. 6px 거터는 항상 확보해 레이아웃이 밀리지 않게 하고, thumb은 평소 투명했다가 nav에 커서가 올라갈 때만 스킨의 `:hover` 색이 든다. 오른쪽 목차에는 자체 스크롤 영역이 없어서 이 규칙이 걸리는 곳은 왼쪽 nav뿐이다.

Firefox에는 `::-webkit-scrollbar`가 없으니 같은 모양을 표준 `scrollbar-width`·`scrollbar-color`로 따로 적어야 한다. 처음에는 `scrollbar-width: thin`을 webkit 규칙과 같은 선택자에 나란히 두었고, 그것이 회귀를 불렀다. Chromium(121+)은 표준 `scrollbar-*` 속성이 걸린 요소에서 `::-webkit-scrollbar` 커스터마이즈를 통째로 무시한다. 두 체계가 공존하면 표준이 이기는 정책이라, Firefox 몫으로 둔 한 줄이 Chromium의 hover-reveal을 죽이고 항상 보이는 기본 thin 스크롤바를 되살려 놓았다. [767e26fd](https://github.com/math-jh/math-jh.github.io/commit/767e26fd96c155a1bcc050fac59c6ec95a84e465)는 그 한 줄을 Firefox에서만 적용되게 가뒀다.

```css
@supports not selector(::-webkit-scrollbar) {
  .sidebar.sticky {
    scrollbar-width: thin;
  }
}
```
{: data-filename="_layouts/default.html"}

`::-webkit-scrollbar` 선택자를 이해하지 못하는 브라우저, 곧 Gecko 계열만 이 블록에 들어온다. Chromium은 블록을 건너뛰므로 webkit 커스텀이 산다. 고치고 나면 여덟 줄짜리 diff다. 표준 속성을 지원했더니 표준이 커스텀을 꺼 버린다는 사실을 알아내는 데까지가 일이었다.

지금은 표준 속성이 전부 이런 블록 안에 있다. nav의 폭은 위 `default.html` 블록에, 색은 스킨의 블록에 둔다.

```scss
@supports not selector(::-webkit-scrollbar) {
  html {scrollbar-color: #c9c2b2 transparent}
  pre {scrollbar-color: #c9c2b2 transparent; scrollbar-width: thin}
  .sidebar.sticky {scrollbar-color: transparent transparent}
  .sidebar.sticky:hover {scrollbar-color: #bfa46a transparent}
  .katex-display, figure.diagram {scrollbar-color: #bfa46a transparent; scrollbar-width: thin}
}
```
{: data-filename="_sass/minimal-mistakes/skins/_custom.scss"}

Firefox의 hover-reveal은 평소 `transparent transparent`였다가 hover에서 thumb 색으로 바뀌는 `scrollbar-color` 두 줄이다. 사용자의 브라우저인 Zen은 Gecko 계열이라, 사용자 화면에 실제로 걸리는 것은 webkit 규칙이 아니라 이 블록이다.

## 수식·다이어그램의 가로 스크롤바

`.katex-display`는 `overflow-x: auto`라서 긴 수식은 블록 안에서 가로로 스크롤된다. 그 스크롤바가 브라우저 기본값이던 것을 사용자가 짚었다.

> 지금 블록 안에 있는 수식 기준으로, 스크롤이 우리가 쓰는 문법이 아니더라, 아무 스타일도 없던데, thumb를 좀 얇게, 호버하면 나오는 황금색 정도로 했으면 좋겠어 (대충 왼쪽 사이드바에 적용된 스타일의 수평버전 느낌으로).

[6b571968](https://github.com/math-jh/math-jh.github.io/commit/6b571968198044c0df11e30b2bc7e350a7f062dd)부터 구조와 색이 둘로 나뉜다. 구조는 `_base.scss`에 한 번 적고, thumb 색은 라이트·다크 스킨이 각자 정한다.

```scss
.katex-display::-webkit-scrollbar,
figure.diagram::-webkit-scrollbar { height: 4px; }
.katex-display::-webkit-scrollbar-track,
figure.diagram::-webkit-scrollbar-track { display: none; }
.katex-display::-webkit-scrollbar-thumb,
figure.diagram::-webkit-scrollbar-thumb { border-radius: 0; }
```
{: data-filename="_sass/minimal-mistakes/_base.scss"}

```scss
.katex-display::-webkit-scrollbar-thumb,
figure.diagram::-webkit-scrollbar-thumb {background-color: #bfa46a}
```
{: data-filename="_sass/minimal-mistakes/skins/_custom.scss"}

다크 스킨의 값은 `#8f7434`이다. 두 값 모두 왼쪽 nav의 `:hover` thumb 색을 그대로 가져왔다. nav는 평소에 투명하다가 hover에서만 색이 들지만, 수식은 처음부터 칠해 둔다. 모바일에는 hover가 없고, 수식이 넘치는 곳은 대개 모바일이라서다. 사용자가 말한 "호버하면 나오는 황금색"의 색만 가져오고 hover 조건은 뺀 셈이다. 직각 thumb과 `display: none` 트랙은 nav 스크롤바의 헤어라인 문법을 수평으로 눕힌 것이다.

Firefox 몫은 앞 절 스킨 블록의 마지막 줄이다. 표준 속성을 `@supports` 밖에 두면 Chromium이 이 4px 규칙을 무시하는 함정이 여기에도 그대로 걸리므로, 이 규칙도 블록 안에 있다. 다이어그램이 가로로 스크롤되는 그림 상자가 된 뒤로는 `figure.diagram`도 같은 선택자 목록에 들어 있어서, 넘치는 수식과 넘치는 그림 아래에 같은 4px 막대가 뜬다.
