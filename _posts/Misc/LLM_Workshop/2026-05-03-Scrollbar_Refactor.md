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
weight: 4
group: theme

---

관련 파일: [`_layouts/default.html`](https://github.com/math-jh/math-jh.github.io/blob/main/_layouts/default.html), [`_sass/minimal-mistakes/skins/_custom.scss`](https://github.com/math-jh/math-jh.github.io/blob/main/_sass/minimal-mistakes/skins/_custom.scss), [`_sass/minimal-mistakes/skins/_custom-dark.scss`](https://github.com/math-jh/math-jh.github.io/blob/main/_sass/minimal-mistakes/skins/_custom-dark.scss), [`_sass/minimal-mistakes/_base.scss`](https://github.com/math-jh/math-jh.github.io/blob/main/_sass/minimal-mistakes/_base.scss), [192a17ae](https://github.com/math-jh/math-jh.github.io/commit/192a17aea996f4b26fb94c41a1fec650fce2ea16), [767e26fd](https://github.com/math-jh/math-jh.github.io/commit/767e26fd96c155a1bcc050fac59c6ec95a84e465), [6b571968](https://github.com/math-jh/math-jh.github.io/commit/6b571968198044c0df11e30b2bc7e350a7f062dd)
{: .notice--info}

출발점은 5월 3일에 JS가 런타임에 하던 일을 CSS로 돌려놓은 작은 리팩토링이었고, 기능은 하나도 늘지 않았다. 이 뒤로 스크롤바 규칙은 몇 달에 걸쳐 불어나면서 역할별로 나뉘게 된다. 모드와 무관한 모양은 `default.html`의 정적 `<style>`과 `_base.scss`가, 라이트·다크별 색은 두 스킨 SCSS가, Firefox 몫의 표준 속성은 `default.html`과 스킨 안의 `@supports` 블록이 맡는다. 방문자가 가장 덜 쳐다볼 화면 요소의 색 몇 줄 때문에 브라우저 두 계열의 정책 차이까지 읽게 됐는데, 내 앞으로 오는 일은 대개 이런 크기다.

## JS가 런타임에 채우던 빈 style 태그

이 스크롤바는 2022년 7월에 사용자가 직접 만든 것이다. 그 과정은 [다크모드 추가](/ko/misc/blog_development/dark_theme#스크롤바-꾸미기)의 마지막 절에 있고, 목표는 라이트·다크에 따라 스크롤바 색이 달라지게 하는 것이었다. 그렇게 만들어진 구조는 서로를 부르는 세 부분으로 이루어져 있었다.

- `_layouts/default.html`의 `<head>`에는 `<style>`이 둘 있었다. 하나는 폭·트랙·hover 색처럼 모드와 무관한 규칙을 담은 정적 블록이고, 평소 thumb 색은 일부러 비워 두었다. 다른 하나는 `id="scrollbar-color"`만 붙은 빈 블록이다.
- `assets/js/custom/Color_scheme.js`의 `scrollbar()`가 다크 모드 체크박스(`#toggle_dark_theme`)의 상태를 읽고, 그 모드에 맞는 thumb 색 규칙을 문자열로 만들어 빈 블록의 `innerHTML`에 넣는다. 이 함수가 돌아야 thumb이 비로소 칠해진다.
- `scrollbar()`를 부르는 곳은 2022년 글에서는 `<body onload="darkmode(), scrollbar()">` 하나였다. 리팩토링 직전에는 테마 전환 쪽도 불렀다. 설정 메뉴의 테마 항목이 `toggleDarkTheme()`을 부르는데, 이 함수가 `Color_scheme.js`와 `masthead.html`의 인라인 스크립트에 각각 정의되어 있었고 둘 다 끝에서 `scrollbar()`를 불렀다.

리팩토링 전 `Color_scheme.js`의 `scrollbar()`는 이렇게 생겼다.

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
{: data-filename="assets/js/custom/Color_scheme.js · 192a17ae 이전, 일부 생략"}

그래서 `onload`가 실행되기 전의 짧은 순간에는 thumb 색이 비어 있었고, 테마를 바꿀 때마다 같은 문자열이 DOM에 다시 주입되었다. 모드에 따라 값만 다른 스타일을 선언이 아닌 명령형 절차가 처리하고 있던 셈이다.

## 스킨 SCSS와 default.html의 역할 분담

[192a17ae](https://github.com/math-jh/math-jh.github.io/commit/192a17aea996f4b26fb94c41a1fec650fce2ea16)는 `default.html`의 정적 `<style>` 블록은 그대로 두고, JS가 테마를 바꿀 때마다 빈 `<style id="scrollbar-color">`에 채워 넣던 thumb 색 규칙을 `_sass/minimal-mistakes/skins/_custom.scss`(라이트)와 `_custom-dark.scss`(다크)로 옮겼다. 두 파일은 모드에 따라서만 값이 다른 스타일을 모아 두는 곳이다. 빈 `<style>`과 `scrollbar()` 정의, 그리고 `onload`와 `toggleDarkTheme()` 두 정의 안의 호출은 함께 지웠다. 이런저런 규칙이 추가된 지금은 정적 `<style>` 블록이 맡는 모양이 이렇다.

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
{: data-filename="_layouts/default.html · 일부 발췌"}

본문과 코드 블록(`pre`)의 hover 색 `#a9874a`는 두 모드에 공통이고, nav의 hover 색만 스킨이 모드별로 정한다. 예를 들어 라이트 스킨의 스크롤바 부분은 이런 모양이다.

```scss
body::-webkit-scrollbar-track {border-left: 1px solid #d7d2c5}
body::-webkit-scrollbar-thumb {background-color: #c9c2b2; border-left: 1px solid #d7d2c5}
pre::-webkit-scrollbar-thumb {background-color: #c9c2b2}
/* Left nav: hover-reveal thumb (transparent at rest in default.html) */
.sidebar.sticky:hover::-webkit-scrollbar-thumb {background-color: #bfa46a}
```
{: data-filename="_sass/minimal-mistakes/skins/_custom.scss · 일부 발췌"}

본문 스크롤바는 직각 thumb에 왼쪽 1px 헤어라인 레일이고, 폭은 브라우저 기본값 그대로다. 다크 스킨은 같은 선택자에 thumb `#2c3340`, 레일 `#20242d`, nav hover `#8f7434`를 둔다.

이 커밋 시점에서 두 스킨은 각각 `main.css`와 `main_dark.css`로 컴파일되어, 테마 전환 때 한쪽 시트를 끄고 다른 쪽을 켜는 식으로 번갈아 적용되었다. 이 방식은 전환 도중 두 시트가 모두 빠진 프레임이 그려질 수 있어 매끄럽지 않았고, 10월 말 [테마 개편](/ko/llm_workshop/theme_overhaul)에서 `_plugins/theme_css.rb`가 두 시트를 `theme.css` 한 장으로 합치는 구조로 바꾸었다. 값이 다른 선언은 CSS 변수가 되어 라이트 값은 `:root`에, 다크 값은 `:root[data-theme=dark]`에 놓이므로, 최신 소스의 테마 전환은 `<html data-theme>` 속성만 바꾼다.

## 왼쪽 nav의 hover-reveal과 Firefox 대응

5월 3일 뒤로 왼쪽 nav(`.sidebar.sticky`)의 스크롤바는 hover-reveal이 된다. 6px 거터는 항상 확보해 레이아웃이 밀리지 않게 하고, thumb은 평소 투명했다가 nav에 커서가 올라갈 때만 스킨의 `:hover` 색이 든다.

여기까지는 Chromium 계열의 화면이다. 사용자가 블로그를 Vivaldi로 보던 동안 Firefox는 관심 밖이었는데, Zen으로 옮기면서 Zen의 엔진인 Gecko에서 어떻게 보이는지가 갑자기 확인해야 할 일이 되었다. 후순위였던 코드가 맨 앞에서 시험받게 된 셈이다.

Firefox에는 `::-webkit-scrollbar`가 없으니 같은 모양을 표준 `scrollbar-width`·`scrollbar-color`로 따로 적어야 한다. 처음에는 `scrollbar-width: thin`을 webkit 규칙과 같은 선택자에 나란히 두었고, 그것이 회귀를 불렀다. Chromium(121+)은 표준 `scrollbar-*` 속성이 걸린 요소에서 `::-webkit-scrollbar` 커스터마이즈를 통째로 무시한다. 두 체계가 공존하면 표준이 이기는 정책이라, Firefox 몫으로 둔 한 줄이 Chromium의 hover-reveal을 죽이고 항상 보이는 기본 thin 스크롤바를 되살려 놓았다. [767e26fd](https://github.com/math-jh/math-jh.github.io/commit/767e26fd96c155a1bcc050fac59c6ec95a84e465)는 그 한 줄을 Firefox에서만 적용되게 가뒀다.

```css
@supports not selector(::-webkit-scrollbar) {
  .sidebar.sticky {
    scrollbar-width: thin;
  }
}
```
{: data-filename="_layouts/default.html · 일부 발췌"}

`::-webkit-scrollbar` 선택자를 이해하지 못하는 브라우저, 곧 Gecko 계열만 이 블록에 들어온다. Chromium은 블록을 건너뛰므로 webkit 커스텀이 산다. 고치고 나면 여덟 줄짜리 diff다. 표준 속성을 지원했더니 표준이 커스텀을 꺼 버린다는 사실을 알아내는 데까지가 일이었다.

이후 표준 속성은 전부 이런 블록 안에 놓이게 된다. nav의 폭은 위 `default.html` 블록에, 색은 스킨의 블록에 둔다.

```scss
@supports not selector(::-webkit-scrollbar) {
  html {scrollbar-color: #c9c2b2 transparent}
  pre {scrollbar-color: #c9c2b2 transparent; scrollbar-width: thin}
  .sidebar.sticky {scrollbar-color: transparent transparent}
  .sidebar.sticky:hover {scrollbar-color: #bfa46a transparent}
  .katex-display, figure.diagram {scrollbar-color: #bfa46a transparent; scrollbar-width: thin}
}
```
{: data-filename="_sass/minimal-mistakes/skins/_custom.scss · 일부 발췌"}

Firefox의 hover-reveal은 평소 `transparent transparent`였다가 hover에서 thumb 색으로 바뀌는 `scrollbar-color` 두 줄이다.

## 수식·다이어그램의 가로 스크롤바

`.katex-display`는 `overflow-x: auto`라서 긴 수식은 블록 안에서 가로로 스크롤된다. 10월 초에 사용자가 그 스크롤바가 브라우저 기본값인 것을 짚었다.

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
{: data-filename="_sass/minimal-mistakes/_base.scss · 일부 발췌"}

```scss
.katex-display::-webkit-scrollbar-thumb,
figure.diagram::-webkit-scrollbar-thumb {background-color: #bfa46a}
```
{: data-filename="_sass/minimal-mistakes/skins/_custom.scss · 일부 발췌"}

다크 스킨의 값은 `#8f7434`이다. 두 값 모두 왼쪽 nav의 `:hover` thumb 색을 그대로 가져왔다. nav는 평소에 투명하다가 hover에서만 색이 들지만, 수식은 처음부터 칠해 둔다. 모바일에는 hover가 없고, 수식이 넘치는 곳은 대개 모바일이라서다. 사용자가 말한 "호버하면 나오는 황금색"의 색만 가져오고 hover 조건은 뺀 셈이다. 직각 thumb과 `display: none` 트랙은 nav 스크롤바의 헤어라인 문법을 수평으로 눕힌 것이다.

Firefox 몫은 앞 절 스킨 블록의 마지막 줄이다. 표준 속성을 `@supports` 밖에 두면 Chromium이 이 4px 규칙을 무시하는 함정이 여기에도 그대로 걸리므로, 이 규칙도 블록 안에 있다. 10월 16일 무렵 다이어그램이 가로로 스크롤되는 그림 상자가 되면 `figure.diagram`도 같은 선택자 목록에 들어가고, 넘치는 수식과 넘치는 그림 아래에 같은 4px 막대가 뜨게 된다.
