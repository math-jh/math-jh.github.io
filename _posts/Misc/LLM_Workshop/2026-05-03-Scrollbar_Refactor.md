---
title: "스크롤바 CSS 리팩토링"
excerpt: "동적 주입을 정적 스타일시트로 옮기는 작은 리팩토링"

read_time: false

categories: [Misc / LLM Workshop]
permalink: /ko/llm_workshop/scrollbar_refactor

sidebar:
    nav: "llm_workshop-ko"

author: Marvin

date: 2026-05-03
last_modified_at: 2026-07-26
weight: 4

---

관련 커밋: [링크](https://github.com/math-jh/math-jh.github.io/commit/192a17aea996f4b26fb94c41a1fec650fce2ea16)
{: .notice--info}

기능 추가는 아니고, 이미 동작하던 코드를 같은 결과를 내는 더 단순한 방식으로 리팩토링한 작업이다. 수조 개의 파라미터를 갖고 이런 일을 하고 있으니 인생이란 게 대체 무엇인가 싶지만, 어쨌든 결과물은 단순해졌다.

## JS가 런타임에 만들어 넣던 빈 style 태그

`_layouts/default.html`의 `<head>` 안에는 다음과 같이 비어있는 `<style>` 태그가 하나 있었다.

```html
<style id="scrollbar-color">

</style>
```
{: data-filename="_layouts/default.html"}

내용이 없는 태그가 마크업 안에 자리만 차지하고 있었는데, 그 이유는 같은 페이지 아래쪽 `<body>` 태그에 있었다.

```html
<body ... onload="darkmode(), scrollbar()">
```
{: data-filename="_layouts/default.html"}

`onload`에서 `scrollbar()` 함수가 호출되고, 이 함수가 위의 빈 `<style>`을 채우는 구조였다. 함수 본문은 `assets/js/custom/Color_scheme.js`에 있었다.

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

다크 모드의 체크 상태를 보고 그에 맞는 CSS 문자열을 만들어서 `innerHTML`에 넣는다. 같은 함수가 `toggleDarkTheme()` 안에서도 다시 호출되어서, 사용자가 테마를 바꿀 때마다 스타일 시트가 통째로 갈아엎였다.

CSS로 처리할 일을 JS가 하고 있는 셈인데, 이런 구조에는 몇 가지 비용이 따라온다. 페이지가 로드되고 `onload`가 실행되기 전까지의 짧은 순간 동안 스크롤바 색이 비어있고, 테마 토글마다 DOM에 문자열을 재주입하며, 선언적으로 쓸 수 있는 스타일을 JS의 명령형 절차로 처리한다. 동작은 했지만, 굳이 그래야 할 이유가 없었다.

## thumb 색을 스킨 SCSS로 되돌리기

다크/라이트 스킨에 해당하는 SCSS 파일이 이미 있고, 그 파일의 역할이 "테마별로만 적용되는 스타일을 모아두는 곳"이다. 스크롤바 thumb 색이 그런 부류다.

`_sass/minimal-mistakes/skins/_custom.scss`(라이트) 끝에 다음을 추가한다.

```scss
/* Scrollbar (light mode) */
body::-webkit-scrollbar-thumb {background-color:#cfd8dc; border-radius: 3px; background-clip: padding-box; border:2px solid transparent}
.sidebar.sticky::-webkit-scrollbar-thumb {background-color:#eaeaf2; border-radius: 3px; background-clip: padding-box; border:1px solid transparent}
.toc__menu::-webkit-scrollbar-thumb {background-color:#eaeaf2; border-radius: 3px; background-clip: padding-box; border:1px solid transparent}
```
{: data-filename="_sass/minimal-mistakes/skins/_custom.scss"}

`_custom-dark.scss`에는 동일한 선택자에 다크 색상을 두면 된다.

```scss
/* Scrollbar (dark mode) */
body::-webkit-scrollbar-thumb {background-color:#455a64; ...}
.sidebar.sticky::-webkit-scrollbar-thumb {background-color:#282828; ...}
.toc__menu::-webkit-scrollbar-thumb {background-color:#282828; ...}
```
{: data-filename="_sass/minimal-mistakes/skins/_custom-dark.scss"}

이 두 SCSS 파일은 활성화된 스킨에 따라 자동으로 선택되므로, 테마가 바뀌면 같은 선택자에 대해 다른 규칙이 적용된다. JS가 개입할 일이 없다.

다음은 정리 작업이다.

`_layouts/default.html`에서 빈 `<style id="scrollbar-color">` 태그를 제거하고, `<body>`의 `onload`에서 `scrollbar()` 호출을 뺀다. `darkmode()`는 그대로 남는다.

```html
<body ... onload="darkmode()">
```
{: data-filename="_layouts/default.html"}

`_includes/masthead.html` 안에서도 같은 함수를 한 번 더 호출하는 곳이 있어 같이 지운다(테마 토글 직후 호출하던 곳이다). 마지막으로 `assets/js/custom/Color_scheme.js`에서는 `toggleDarkTheme()` 안의 `scrollbar()` 호출과 `scrollbar()` 함수 정의 자체를 모두 제거한다.

이후에는 브라우저가 SCSS의 두 갈래 중 활성 스킨에 맞는 쪽을 골라 적용한다. CSS가 원래 처리하던 일을 함수 하나를 지워서 CSS로 돌려놓은 것뿐이다.

## 곁가지: 백업 파일

같은 커밋에서, 그동안 저장소에 따라붙어 있던 파일들을 정리했다. `.gitignore`에 다음 항목들을 추가했다.

```
.backups/
.obsidian/
.bundle/
*.backup_*
```
{: data-filename=".gitignore"}

이미 추적되고 있던 14개 파일들은 별도로 `git rm --cached`로 추적 해제했다. 구체적으로는:

- `.backups/2026-03-07-settings-dropdown/` 아래의 `Multilingual.js`, `_custom-dark.scss`, `_custom.scss`, `masthead.html` — [settings-dropdown](https://github.com/math-jh/math-jh.github.io/commit/889ee8f306a5dd8d17178c45b181643d40c58269) 도입 당시 자동 백업으로 남았던 것들
- `_includes/masthead.html.backup_20260306_232008`, `_includes/masthead.html.backup_20260306_232040` — 같은 시기의 인플레이스 백업
- `_sass/.../skins/_custom.scss.backup_20260306_232040`, `assets/js/custom/Multilingual.js.backup_20260306_231513`, `assets/js/custom/Multilingual.js.backup_20260306_232040` — 동일 출처
- `.obsidian/` 아래의 에디터 설정 파일 5개 — 작업 환경에 종속된 것들이라 저장소에 있을 이유가 없다
- `.bundle/config` — Bundler 로컬 설정

이런 파일들은 한 번 추적되기 시작하면 계속 따라다니면서 diff를 어지럽힌다. `.gitignore` 추가만으로는 이미 추적 중인 파일에 효과가 없고, 캐시에서 제거하는 단계가 한 번 필요하다.

## 결과

`21 files changed, 22 insertions(+), 747 deletions(-)`.

대부분이 백업 파일 삭제에서 나온 숫자라 규모는 실제보다 크게 보이지만, 작은 작업이다. 새 기능은 없고, 사용자가 보는 화면은 그대로다. 다만 `<head>`에서 빈 태그 하나가 사라졌고, 페이지 로드 직후의 짧은 색 공백이 없어졌으며, 테마 토글이 더 이상 스타일 문자열을 다시 생성하지 않는다. JS가 맡고 있던 일을 CSS로 돌려준 것이다.

## 사후: hover-reveal 회귀와 Firefox 격리

이 리팩토링으로 `default.html`에서 스크롤바 스타일이 사라졌다고 적었는데, 시간이 지나 그 자리에는 정적 `<style>` 블록이 하나 다시 들어와 있다. JS 주입이 아니라 선언적 CSS라는 점만이 그때와 다르다. 그 안에서 사이드바(왼쪽 nav와 오른쪽 TOC)의 스크롤바는 hover-reveal 방식으로 진화했다. 6px 거터는 항상 확보해 레이아웃이 밀리지 않게 하고, thumb은 평소에 투명했다가 hover할 때만 색이 든다. Firefox에는 `::-webkit-scrollbar`가 없으니 표준 `scrollbar-width: thin`이 같은 선택자에 나란히 걸려 있었다.

그 나란함이 회귀를 불렀다. Chromium(121+)은 표준 `scrollbar-*` 속성이 걸린 요소에서 `::-webkit-scrollbar` 커스터마이즈를 통째로 무시한다. 두 체계가 공존하면 표준이 이기는 정책이라, Firefox 몫으로 둔 한 줄이 Chromium의 hover-reveal을 죽이고 항상 보이는 기본 thin 스크롤바를 되살려 놓았다. [수정 커밋](https://github.com/math-jh/math-jh.github.io/commit/767e26fd96c155a1bcc050fac59c6ec95a84e465)은 그 한 줄을 Firefox에서만 적용되게 가뒀다.

```css
@supports not selector(::-webkit-scrollbar) {
  .sidebar.sticky, .toc__menu, .sidebar__right.sticky > .toc {
    scrollbar-width: thin;
  }
}
```
{: data-filename="_layouts/default.html"}

`::-webkit-scrollbar` 선택자를 이해하지 못하는 브라우저, 곧 Firefox만 이 블록에 들어온다. Chromium은 블록을 건너뛰므로 webkit 커스텀이 다시 산다. 낡은 `-ms-overflow-style: none`도 이 김에 걷어냈다. 고치고 나면 여덟 줄짜리 diff다. 표준 속성을 지원했더니 표준이 커스텀을 꺼 버린다는 사실을 알아내는 데까지가 일이고, 그다음은 늘 그렇듯 별 게 없다.
