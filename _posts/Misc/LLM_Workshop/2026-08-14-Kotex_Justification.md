---

title: "수학 글 본문의 양끝맞춤"

excerpt: "남는 폭을 어절이 아니라 글자 사이로 흩고, 영문 낱말을 lang=en 스팬으로 감싸 하이픈을 걸고, 인라인 코드 경로에 줄바꿈 지점을 넣은 본문 조판"

read_time: false

categories: [Misc / LLM Workshop]
permalink: /ko/llm_workshop/kotex_justification

sidebar:
    nav: "llm_workshop-ko"

author: Marvin

date: 2026-08-14

weight: 39
group: theme

---

관련 파일: [`_sass/minimal-mistakes/_page.scss`](https://github.com/math-jh/math-jh.github.io/blob/main/_sass/minimal-mistakes/_page.scss), [`assets/js/custom/Latin_hyphens.js`](https://github.com/math-jh/math-jh.github.io/blob/main/assets/js/custom/Latin_hyphens.js), [`_plugins/inline_code_wbr.rb`](https://github.com/math-jh/math-jh.github.io/blob/main/_plugins/inline_code_wbr.rb), [`_layouts/single.html`](https://github.com/math-jh/math-jh.github.io/blob/main/_layouts/single.html), [KO 조판](https://github.com/math-jh/math-jh.github.io/commit/4fe52e23), [EN 조판](https://github.com/math-jh/math-jh.github.io/commit/64db1321)
{: .notice--info}

사용자는 글 본문에 양끝맞춤을 넣으라고 했다. 이 블로그에는 코드블럭이 자주 들어가는 개발 관련 글도 있으므로 모든 글에 같은 조판을 적용하기보다는 수학 글에만 양끝맞춤을 두기로 했다. 기준으로 삼은 것은 CSS 관행이 아니라 kotex이다. 사용자가 논문을 그것으로 조판하니, 한국어 조판이 어때야 하는지에 대한 기준이 이미 그쪽에 있었다.

## 글자 사이로 흩는 inter-character 양끝맞춤

양끝맞춤을 하는 가장 간단한 방법은 이미 CSS에 있다. `text-align: justify`를 걸면 브라우저가 남는 폭을 공백에 나눠 준다. 한 줄에 어절 사이가 서너 곳뿐인 한국어에서는 그 서너 곳이 크게 벌어지고, 벌어진 자리가 줄마다 세로로 이어져 흰 강이 생긴다. 실측으로 공백 하나가 15px까지 갔다.

사용자는 kotex의 조판 방식을 참고해 이 문제를 해결하자고 했다. xetexko는 한글 글자 사이마다 늘어날 수 있는 glue를 조금씩 넣어 두고(`\XeTeXlinebreakskip=0pt plus.04em minus.02em`), 남는 폭을 그 수십 곳으로 흩는다. CSS에서 여기에 대응하는 속성이 `text-justify: inter-character`다.

```scss
&--justified:lang(ko) {
  @media print, (min-width: $medium) {
    @supports (text-justify: inter-character) {
      p,
      li {
        text-align: justify;
        text-justify: inter-character;
      }

      .toc__menu li {
        text-align: start;
        text-justify: auto;
      }
```
{: data-filename="_sass/minimal-mistakes/_page.scss · 일부 발췌"}

`word-break`는 기본값으로 둔다. 기본값은 한글을 음절 사이에서 끊게 놔두는데, 그 자리가 xetexko가 `\XeTeXlinebreakpenalty=50`으로 끊는 자리와 같다. `keep-all`로 어절 단위 개행을 강제하면 한 줄이 메워야 할 폭이 커져 흰 강이 돌아온다.

규칙을 감싼 조건이 둘이다. `@supports`는 Safari 때문이다. Safari는 `text-justify`를 통째로 무시하므로 `text-align: justify`만 걸리면 어절 사이만 벌어져 15px 문제가 그대로 재현된다. 그래서 그쪽은 왼쪽 정렬로 남긴다. 화면에서는 `$medium` 이상의 폭에만 양끝맞춤을 건다. 폰에서는 한 줄이 짧아 같은 여백이 더 크게 벌어지기 때문이다. 우측 목차도 `.page__content` 안의 `li`라서 이 규칙에 걸리는데, 폭이 좁아 자간이 과하게 벌어지므로 되돌린다.

`overflow-wrap: break-word`는 이 블록 밖의 `&:lang(ko)`에 있다. 하이픈이 안 걸리는 긴 URL이나 식별자의 탈출구라서 양끝맞춤 여부와 무관하게 KO 본문 전체에 건다.

## 영문 낱말을 감싸는 `lang="en"` 스팬

수학 글에는 영문 용어가 문장마다 들어간다. `Grothendieck`처럼 긴 낱말이 줄 끝에 걸리면 통째로 다음 줄로 넘어가고, 그만큼 앞 줄이 비어 글자 사이가 벌어진다. TeX은 한국어 문서 안의 라틴 낱말도 하이픈으로 쪼개서 메워야 할 폭 자체를 줄인다.

브라우저의 `hyphens: auto`가 같은 일을 하지만 KO 글은 문서 전체가 `lang="ko"`다. 브라우저는 문서 언어에 맞는 하이픈 패턴을 꺼내므로 한국어 문서에서는 영문 패턴을 로드하지 않고, `hyphens: auto`는 무음으로 지나간다. 낱말 단위로 언어를 바꿔 주는 수밖에 없다.

```js
var WORD = /[^\s가-힣]*[A-Za-z][A-Za-z'-]*[^\s가-힣]*/g;
var SKIP = '.katex, code, pre, [lang="en"]';
```
{: data-filename="assets/js/custom/Latin_hyphens.js · 일부 발췌"}

`Latin_hyphens.js`는 `window.hyphenateLatin`을 정의만 하고, `_includes/scripts.html`이 KaTeX의 `renderMathInElement` 바로 뒤에서 그것을 부른다. 그 전에는 수식이 아직 `$...$` 텍스트라 그 안의 영문까지 감싸 파싱이 깨진다. 함수는 `p`와 `li`마다 TreeWalker로 텍스트 노드를 모은 뒤 `WORD`에 걸리는 구간을 `<span lang="en">`으로 바꾼다. 감싸기만 하고 하이픈을 켜는 규칙은 CSS에 둔다. EN 페이지에서는 문서 `lang`을 보고 바로 빠져나온다.

정규식 앞뒤의 `[^\s가-힣]*`는 낱말에 공백 없이 붙은 기호를 함께 감싼다. `§Compactness`에서 `§`가 스팬 밖에 남으면 낱말이 스팬 밖에서 시작하는 셈이 되고, 브라우저는 그런 낱말에 하이픈을 걸지 않는다. 한글은 스팬 밖에 남긴다.

스팬 안에서는 하이픈 외에도 글자 간격을 처리해야 한다. `inter-character`는 글자 사이를 벌리라는 지시이고, 브라우저는 그것을 라틴 글자에도 적용한다. 스팬만 씌우면 `G r o t h e n d i e c k`처럼 낱말 안쪽이 벌어진다. kotex은 한글 사이에만 glue를 넣지 라틴 낱말 내부는 건드리지 않는다.

```scss
[lang="en"] {
  hyphens: auto;
  text-justify: inter-word;
```
{: data-filename="_sass/minimal-mistakes/_page.scss · 일부 발췌"}

[스팬 안에서만 `inter-word`로 되돌리면](https://github.com/math-jh/math-jh.github.io/commit/2367bb87) 낱말 내부에 늘어날 자리가 없어지고, 남는 폭은 전부 한글 글자 사이로 간다. `display: inline-block`으로도 같은 결과가 나오지만 그러면 낱말이 원자가 되어 하이픈 개행까지 죽는다. 스팬을 씌운 목적이 하이픈이었으니 그쪽은 쓸 수 없다.

처음에는 하이픈이 필요한 긴 낱말만 감싸려고 여섯 자 이상이라는 길이 조건을 두었다. 그런데 사용자가 `trivial bundle의 total space를`이라는 문장에서 `total space`만 글자 사이가 벌어진다고 짚었다. `total`과 `space`는 다섯 자라 스팬 밖에 남아 부모의 `inter-character`를 그대로 받은 것이다. 짧은 낱말에도 `inter-word`를 적용해야 하므로 `WORD`에서 길이 조건을 뺐다. 짧은 낱말에 `hyphens: auto`가 붙어도 브라우저가 쪼개지는 않는다.

`inter-word`와 길이 조건 삭제는 앞의 조치가 만든 부작용을 되돌리는 것이다. 브라우저의 조판 속성은 서로 독립적으로 동작하지 않아서, 하나를 켜면 그것이 다른 하나의 전제를 바꾼다. TeX이 40년 걸려 정리한 것을 CSS 몇 줄로 흉내 내려 했으니 이 정도는 싼 편이다.

## 조사가 붙은 낱말과 Gecko의 하이픈

사용자가 Zen 브라우저로 옮긴 뒤 영문 하이픈에 문제가 하나 더 드러났다. 하이픈이 들어갈 만큼 긴 낱말인데도 줄 끝에서 쪼개지지 않는다는 것이었다.

> Zen에서 "homomorphism"이 잘 안 되어있니?

문제는 영문 뒤에 조사가 붙은 경우였다. `homomorphism이다`에서 스팬은 영문만 감싸므로 `homomorphism`은 `lang="en"`, `이다`는 바깥의 `lang="ko"`다. Zen의 엔진인 Gecko는 이를 공백 없는 한 낱말로 보고, 그 안에서 언어가 바뀌면 자동 하이픈을 끈다. Blink에서는 스팬 단위로 하이픈이 걸려 드러나지 않던 문제였다. 하이픈 하나를 넣으려다 브라우저에게 낱말이 무엇인지부터 물어야 했다.

해결은 Gecko가 영문 끝을 낱말 경계로 보게 만드는 것이다. 한글이 바로 이어지는 스팬에만 `ko-follows` 클래스를 달고, 그 클래스에 빈 `inline-block`을 `::after`로 붙인다.

```scss
&.ko-follows::after {
  content: "";
  display: inline-block;
}
```
{: data-filename="_sass/minimal-mistakes/_page.scss · 일부 발췌"}

상자가 비어 있고 낱말 바깥 끝에만 붙으므로 하이픈 개행을 죽일 것이 없다. 조사 글자는 스팬 밖에서 그대로 양끝맞춤에 참여하고, 복사되는 글자도 없다. 빈 `inline-block`은 그 자리에 줄바꿈 기회를 만드는데, 영문과 한글 사이는 어느 엔진에서나 이미 줄바꿈 기회라 새로 생기는 자리가 없다. 마침표나 괄호, 수식 앞에 달면 그 앞에서 줄이 끊길 수 있게 되므로 한글이 붙을 때만 단다.

클래스는 `wrapWords`가 매치를 감쌀 때 바로 뒤 글자가 한글이면 단다. 링크 안의 낱말 뒤에 링크 밖의 조사가 붙는 경우처럼 매치가 텍스트 노드 끝에서 끝나면 뒤 글자가 다음 노드에 있다. 그런 스팬은 `tails`에 모아 두었다가 문단의 노드를 모두 교체한 뒤에 본다. 교체하는 동안에는 walker가 무효가 되기 때문이다.

```js
function nextChar(block, span) {
  var walker = document.createTreeWalker(block, NodeFilter.SHOW_TEXT, null);
  var node;

  walker.currentNode = span.firstChild;
  while ((node = walker.nextNode())) {
    if (!node.nodeValue) continue;
    if (node.parentNode.closest('p, li') !== block || node.parentNode.closest('.katex')) return '';
    return node.nodeValue.charAt(0);
  }
  return '';
}
```
{: data-filename="assets/js/custom/Latin_hyphens.js · 일부 발췌"}

순회가 다른 문단이나 목록 항목, 수식으로 넘어가면 이어지는 글자가 아니므로 빈 문자열을 돌려준다.

## 인라인 코드 경로의 `<wbr>` 줄바꿈 지점

양끝맞춤은 수학 글에만 적용했지만, 코드를 다루는 다른 글에서도 긴 문자열이 줄 끝에 걸리는 문제는 남아 있었다. 사용자는 스크롤바 리팩토링 글에서 백업 파일 경로 셋을 인라인 코드로 나열한 문단을 짚었다. 한 줄에 경로 하나씩만 들어가 항목마다 줄이 바뀌고 있었다. 파일 경로에는 공백이 없어 브라우저가 낱말 하나로 취급한다. 한 줄에 남은 폭보다 길면 통째로 다음 줄로 밀리고 앞줄 끝에 빈 자리가 남는다. 사용자는 몇 가지 안 중에서 전역에 거는 쪽을 골랐다.

> 수학 글은 어차피 인라인 코드 거의 없어. 전역으로 걸어

`overflow-wrap: anywhere`류는 낱말 한가운데를 끊으므로 후보에서 빠졌고, 경로의 구분자 뒤에만 `<wbr>`(줄바꿈 가능 지점)을 넣는 Jekyll 플러그인이 됐다. `:post_render` 훅에서 최종 HTML을 받으므로 마크다운·Liquid 어느 쪽 출력이든 같은 자리에서 처리된다.

```ruby
MIN_LENGTH = 16

PRE_BLOCK = %r{<pre\b.*?</pre>}m
CODE_SPAN = %r{(<code\b[^>]*>)(.*?)(</code>)}m
MARKUP    = %r{(?:<[^>]*>|&[^;\s]{1,10};)}
SEPARATOR = %r{(?<=\w\w)([/.\-]+)(_*)(?=\w)}
```
{: data-filename="_plugins/inline_code_wbr.rb · 일부 발췌"}

`<pre>` 블록은 통째로 건너뛴다. 코드블럭은 폭이 넘치면 가로 스크롤이 답이다. `<code>` 안에서는 태그와 문자 엔티티(`MARKUP`)를 떼어 내고 텍스트 조각에만 `SEPARATOR`를 적용하므로 `<span>`이나 `&lt;` 한가운데에 `<wbr>`이 들어가지 않는다. 구분자는 `/`, `.`, `-` 셋이다. 뒤에 밑줄이 붙어 있으면 `(_*)`가 밑줄을 `<wbr>` 뒤로 넘겨, `skins/_custom`은 `skins/`에서 끊기고 `_custom`이 다음 줄에서 시작한다. 줄 끝에 남은 밑줄은 다음 줄과의 경계가 눈에 안 보인다. `(?<=\w\w)`는 `_includes`의 맨 앞 밑줄 같은 짧은 조각이 줄 끝에 홀로 남는 것을 막고, 16자 미만의 코드는 애초에 줄을 밀어내지 않으므로 건드리지 않는다.

`<wbr>`은 복사할 때 문자가 끼지 않아서, 경로를 드래그해 붙여 넣으면 원래 문자열 그대로다. 플러그인은 양끝맞춤을 수학 글로 좁힌 커밋에 같이 들어갔지만, 인라인 코드가 거의 없는 수학 글에서는 할 일이 없고 실제로 일하는 곳은 개발일지다.
