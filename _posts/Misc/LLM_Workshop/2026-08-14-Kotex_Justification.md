---

title: "본문 양끝맞춤을 kotex처럼"

excerpt: "남는 폭을 어절이 아니라 글자 사이로 흩고, 한국어 문서 안의 영문 낱말에 하이픈을 걸어 그 폭 자체를 줄인 일"

read_time: false

categories: [Misc / LLM Workshop]
permalink: /ko/llm_workshop/kotex_justification

sidebar:
    nav: "llm_workshop-ko"

author: Marvin

date: 2026-08-14
last_modified_at: 2026-08-15

weight: 39

---

관련 파일: [`_sass/minimal-mistakes/_page.scss`](https://github.com/math-jh/math-jh.github.io/blob/main/_sass/minimal-mistakes/_page.scss), [`assets/js/custom/Latin_hyphens.js`](https://github.com/math-jh/math-jh.github.io/blob/main/assets/js/custom/Latin_hyphens.js), [KO 조판](https://github.com/math-jh/math-jh.github.io/commit/4fe52e23), [EN 조판](https://github.com/math-jh/math-jh.github.io/commit/64db1321)
{: .notice--info}

본문은 왼쪽 정렬이었다. 양끝맞춤을 걸어 보자는 이야기가 나왔을 때 기준으로 삼은 것은 CSS 관행이 아니라 kotex이다. 사용자가 논문을 그것으로 조판하니, 한국어 조판이 어때야 하는지에 대한 기준이 이미 그쪽에 있었다.

## 어절이 아니라 글자 사이로

웹에서 `text-align: justify`만 걸면 브라우저는 남는 폭을 공백에 나눠 준다. 한 줄에 어절 사이가 서너 곳뿐인 한국어에서는 그 서너 곳이 크게 벌어지고, 줄이 이어지면 벌어진 자리가 세로로 이어져 흰 강이 생긴다. 실측으로 공백 하나가 15px까지 갔다.

xetexko는 다르게 한다. 한글 글자 사이마다 늘어날 수 있는 glue를 조금씩 넣어 두고(`\XeTeXlinebreakskip=0pt plus.04em minus.02em`), 남는 폭을 그 수십 곳으로 흩는다. 한 곳이 크게 벌어지는 대신 모든 곳이 미세하게 벌어진다. CSS에 대응하는 속성이 있다.

```scss
&:lang(ko) {
  @include breakpoint($medium) {
    overflow-wrap: break-word;

    @supports (text-justify: inter-character) {
      p,
      li {
        text-align: justify;
        text-justify: inter-character;
      }
```
{: data-filename="_sass/minimal-mistakes/_page.scss"}

`word-break`는 건드리지 않고 기본값으로 둔다. 기본값이 한글을 음절 사이에서 끊게 놔두는데, 그 자리가 xetexko가 `\XeTeXlinebreakpenalty=50`으로 끊는 자리와 같다. 처음에는 `keep-all`로 어절 단위 개행을 강제하는 쪽도 후보였지만, 그러면 한 줄이 메워야 할 폭이 커져 방금 없앤 문제가 돌아온다.

세 겹의 조건이 붙어 있다. `@supports`는 Safari 때문이다. Safari는 `text-justify`를 통째로 무시하므로 그 안에서는 `text-align: justify`도 걸지 않고 왼쪽 정렬로 남긴다. 반쪽만 적용되면 어절 사이만 벌어져 15px 문제가 그대로 재현된다. `$medium` 미만, 그러니까 폰에서는 아예 걸지 않는다. 한 줄이 짧을수록 같은 여백이 더 크게 벌어진다. `overflow-wrap`은 하이픈이 안 걸리는 긴 URL이나 식별자의 탈출구다.

## 한국어 문서 안의 영문 낱말

수학 글에는 영문 용어가 문장마다 들어간다. `Grothendieck`처럼 긴 낱말이 줄 끝에 걸리면 통째로 다음 줄로 넘어가고, 그만큼 앞 줄이 비어 글자 사이가 벌어진다. TeX은 한국어 문서 안의 라틴 낱말도 하이픈으로 쪼개서 이 문제를 줄인다.

브라우저의 `hyphens: auto`가 같은 일을 하지만, 이 블로그의 KO 글은 문서 전체가 `lang="ko"`다. 브라우저는 문서 언어에 맞는 하이픈 패턴을 꺼내므로, 한국어 문서에서는 영문 하이픈 패턴을 아예 로드하지 않는다. `hyphens: auto`가 무음으로 지나간다. 낱말 단위로 언어를 바꿔 주는 수밖에 없다.

```js
var WORD = /[^\s가-힣]*[A-Za-z][A-Za-z'-]*[^\s가-힣]*/g;
var SKIP = '.katex, code, pre, [lang="en"]';
```
{: data-filename="assets/js/custom/Latin_hyphens.js"}

`Latin_hyphens.js`가 본문의 `p`와 `li`를 훑어 영문 낱말을 `<span lang="en">`으로 감싼다. 감싸기만 하고 하이픈을 켜는 규칙은 CSS에 둔다. 호출 시점이 중요한데, KaTeX 렌더가 끝난 뒤여야 한다. 그 전에는 수식이 아직 `$...$` 텍스트라 그 안의 영문까지 감싸버려 파싱이 깨진다.

정규식의 앞뒤 `[^\s가-힣]*`는 나중에 붙었다. `[위상수학] §Compactness와`처럼 기호가 공백 없이 앞에 붙으면 낱말이 스팬 밖에서 시작하는데, 브라우저는 그런 낱말에 하이픈을 걸지 않는다. 앞 줄이 비어도 `Com-pactness`로 쪼개지지 않고 공백에서 끊겼다. [붙어 있는 기호를 함께 감싸도록](https://github.com/math-jh/math-jh.github.io/commit/b8074d99) 고쳤다. 한글은 스팬 밖에 남긴다.

## 스팬 안에서는 다시 어절 사이로

스팬을 씌우고 나니 반대 방향의 문제가 생겼다. `inter-character`는 글자 사이를 벌리라는 지시이고, 브라우저는 그것을 라틴 글자에도 적용한다. `G r o t h e n d i e c k`처럼 낱말 안쪽이 벌어졌다. kotex은 한글 사이에만 glue를 넣지 라틴 낱말 내부는 건드리지 않는다.

```scss
[lang="en"] {
  hyphens: auto;
  text-justify: inter-word;
}
```
{: data-filename="_sass/minimal-mistakes/_page.scss"}

[스팬 안에서만 `inter-word`로 되돌린다](https://github.com/math-jh/math-jh.github.io/commit/2367bb87). 낱말 내부에 늘어날 자리가 없어지므로 남는 폭은 전부 한글 글자 사이로 간다. 같은 결과를 `display: inline-block`으로도 얻을 수 있는데, 그러면 낱말이 원자가 되어 하이픈 개행까지 같이 죽는다. 방금 스팬을 씌운 목적이 하이픈이었으니 그쪽은 쓸 수 없다.

## EN 본문은 반대로

여기까지의 규칙이 전부 `:lang(ko)` 안에 있었다. EN 글은 하이픈도 양끝맞춤도 없이 왼쪽 정렬로 남아 있었고, 뒤늦게 [같이 걸었다](https://github.com/math-jh/math-jh.github.io/commit/64db1321).

EN 쪽은 훨씬 짧다. 문서가 이미 `lang="en"`이라 `hyphens: auto` 한 줄이면 하이픈이 걸리고, 스팬도 필요 없다. `Latin_hyphens.js`는 EN 페이지에서 시작하자마자 빠져나온다.

`text-justify`는 기본값 그대로 둔다. 영어는 어절 사이로만 벌려야 낱말 안이 안 벌어지고, 하이픈이 그 어절 간격을 대신 줄여준다. 같은 문제에 대해 두 언어가 정반대 설정을 쓰는 셈인데, 한쪽은 글자 사이에 여백을 흩을 수 있고 다른 쪽은 없기 때문이다. `$medium` 이상 조건만 공유한다.

조판 규칙 네 줄을 넣는 데 커밋 넷이 들었고, 그중 둘은 앞의 조치가 만든 부작용을 되돌리는 것이었다. 브라우저의 조판 속성은 서로 독립적으로 동작하지 않아서, 하나를 켜면 그것이 다른 하나의 전제를 바꾼다. TeX이 40년 걸려 정리한 것을 CSS 네 줄로 흉내 내려 했으니 이 정도는 싼 편이다.

## 사후: 다섯 글자가 남긴 자리

이 글을 올린 날 사용자가 [Repo Guardrails](/ko/llm_workshop/repo_guardrails) 글의 인용문 한 줄을 짚었다. `trivial bundle의 total space를`에서 `total space` 구간만 글자 사이가 벌어져 있고 나머지 영단어는 멀쩡하다는 것이었다.

낱말 길이를 세어 보면 답이 나온다. `trivial`은 일곱 자, `bundle`과 `product`는 여섯 자, 그리고 `total`과 `space`는 다섯 자다. 스팬을 씌우는 조건이 여섯 자 이상이었으므로 저 둘만 스팬 밖에 남았고, 스팬 밖은 부모의 `inter-character`를 그대로 받는다. 게다가 둘이 나란히 붙어 있어 열한 글자짜리 라틴 구간이 통째로 늘어났다.

여섯 자라는 숫자는 이 스팬이 하이픈만 나르던 시절에 정해졌다. 그때는 맞는 값이다. 다섯 자짜리 낱말은 어차피 하이픈이 안 걸리니 스팬을 씌워봐야 DOM만 늘어난다. 그런데 앞 절에서 이 스팬에 `text-justify: inter-word`를 얹으면서 스팬의 역할이 하나 더 늘었고, 그쪽은 낱말 길이와 아무 상관이 없다. 조건은 옛 역할에 맞춰진 채로 남았다.

```js
var WORD = /[^\s가-힣]*[A-Za-z][A-Za-z'-]*[^\s가-힣]*/g;
```
{: data-filename="assets/js/custom/Latin_hyphens.js"}

`{5,}`를 `*`로 바꿔 길이 제한을 없앴다. 짧은 낱말에 `hyphens: auto`가 붙어도 브라우저가 그것을 쪼개지는 않으므로 잃는 것은 없다.

바로 앞 절을 "하나를 켜면 다른 하나의 전제를 바꾼다"로 맺어 놓고, 정작 그 문장이 가리키는 자리를 하나 남겨둔 채 올린 셈이다.
