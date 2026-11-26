---

title: "공유 버튼과 브랜드 아이콘"
excerpt: "Font Awesome 없이 공유 버튼의 로고를 인라인 SVG로 그리고, 가장 긴 버튼에 폭을 맞추는 grid 배치와 브라우저 공유 시트 버튼을 더한 작업"

read_time: false

categories: [Misc / LLM Workshop]
permalink: /ko/llm_workshop/share_buttons

sidebar:
    nav: "llm_workshop-ko"

author: Marvin

date: 2026-11-22
weight: 78
group: features

---

관련 파일: [`_includes/social-share.html`](https://github.com/math-jh/math-jh.github.io/blob/main/_includes/social-share.html), [`_includes/brand-icon.html`](https://github.com/math-jh/math-jh.github.io/blob/main/_includes/brand-icon.html), [`_sass/minimal-mistakes/_page.scss`](https://github.com/math-jh/math-jh.github.io/blob/main/_sass/minimal-mistakes/_page.scss), [`_sass/minimal-mistakes/_buttons.scss`](https://github.com/math-jh/math-jh.github.io/blob/main/_sass/minimal-mistakes/_buttons.scss), [c539a34c](https://github.com/math-jh/math-jh.github.io/commit/c539a34c)
{: .notice--info}

글 아래의 공유 버튼은 minimal-mistakes 테마가 주는 그대로 Twitter, Facebook, LinkedIn 세 개였다. 사용자는 이 레포를 upstream과 견주어 보다가 이 버튼들을 손보기로 했고, 요청은 X로 이름을 바꾸고 LinkedIn 대신 다른 곳을 넣는 것이었다. 로고를 그리던 Font Awesome을 계속 부를 이유가 있는지도 같이 확인하게 했다.

## Font Awesome이 맡던 로고

기존 버튼의 로고는 Font Awesome의 `<i>` 태그였다.

```liquid
<a href="https://twitter.com/intent/tweet?..." class="btn btn--twitter" ...><i class="fab fa-fw fa-twitter" aria-hidden="true"></i><span> Twitter</span></a>
```
{: data-filename="_includes/social-share.html · c539a34c 이전, 일부 생략"}

`fab fa-twitter`라는 클래스는 Font Awesome CSS가 있어야 그림이 된다. 그 CSS는 `head.html`이 jsDelivr CDN에서 `preload`로 따로 받고 있었다. 글 한 편을 열 때마다 외부 도메인 요청과 글꼴 파일이 하나 더 붙는데, 사이트에서 이 글꼴이 그리는 것은 공유 버튼과 footer의 GitHub 링크 정도였다. 아이콘 글꼴은 이미 Material Symbols를 쓰고 있었으므로 사용자는 그쪽으로 대체할 수 있는지 확인해 달라고 했다.

> fontawesome 말고 지금 우리가 이미 부르는 것 중에 (예를 들어 material symbol) 쓸 수 있는게 있는지 확인해줘.

Material Symbols에는 브랜드 로고가 없다. 아이콘 글꼴은 일반적인 그림 기호를 모아 둔 것이어서 상표가 걸린 로고는 들어 있지 않다. 그래서 로고만 따로 SVG로 옮기는 쪽으로 정해졌고, 사용자는 이 안에 동의했다. 이때 Font Awesome CDN 요청 두 줄(`preload` 링크와 `noscript` 대체)이 `head.html`에서 지워졌다.

## 인라인 SVG 로고 파일

로고 네 개(X, Facebook, Threads, GitHub)는 `brand-icon.html` 한 파일이 이름으로 골라 그린다.

{% raw %}
```liquid
{%- capture _brand_d -%}
{%- case include.name -%}
{%- when "x" -%}M14.234 10.162 22.977 0h-2.072l-7.591 8.824L7.251 0H.258l9.168 13.343...
{%- when "facebook" -%}M9.101 23.691v-7.98H6.627v-3.667h2.474v-1.58c0-4.085 1.848-5.978...
{%- when "threads" -%}M18.263 11.097c-.03-3.486-1.92-5.586-5.111-5.586-2.13 0-3.922.963...
{%- when "github" -%}M12 .297c-6.63 0-12 5.373-12 12 0 5.303 3.438 9.8 8.205 11.385...
{%- endcase -%}
{%- endcapture -%}
{%- if _brand_d != "" -%}<svg class="brand-icon" viewBox="0 0 24 24" aria-hidden="true" focusable="false"><path d="{{ _brand_d }}"/></svg>{%- endif -%}
```
{: data-filename="_includes/brand-icon.html · 일부 생략, path 데이터 뒷부분 생략"}
{% endraw %}

`case`가 고른 path 데이터를 `capture`로 변수에 담고, 값이 비어 있지 않을 때만 `<svg>`를 낸다. 모르는 이름을 넘기면 빈 문자열이 되어 아무것도 그려지지 않으므로, 오타가 있어도 깨진 아이콘 대신 빈자리만 남는다. path 데이터는 파일 머리의 주석대로 Simple Icons(CC0 1.0)에서 가져왔다. 색과 크기는 스타일시트가 정한다.

```scss
.brand-icon {
  display: inline-block;
  width: 1em;
  height: 1em;
  vertical-align: -0.125em;
  fill: currentColor;
}
```
{: data-filename="_sass/minimal-mistakes/_base.scss · 일부 발췌"}

`fill: currentColor`는 SVG를 둘러싼 글자색을 그대로 칠하라는 뜻이다. 버튼 글자색이 바뀌면 로고도 따라 바뀌므로, 글꼴 아이콘 때처럼 라이트·다크 테마마다 로고 색을 따로 지정하지 않아도 된다. footer 링크의 아이콘도 같은 파일을 부르도록 `footer.html`의 `<i class="fas fa-link">`가 `{% raw %}{% include brand-icon.html name=link.icon %}{% endraw %}`로 바뀌었고, `_config.yml`의 `footer.links`에서 `icon: "github"`처럼 이름만 적는다.

## X, Threads, 공유 버튼

Twitter 버튼의 이름 표시는 사용자가 정했다. Twitter가 X로 이름을 바꾼 탓에 디자인이 골치 아프다는 말에 이어, 버튼 이름은 `X (Twitter)`로 정해졌다. 주소도 `twitter.com/intent/tweet`에서 `x.com/intent/post`로 바뀌었다.

LinkedIn은 사용자가 뺐고, 대신 사용자가 처음 물은 것은 Instagram이었다.

> 인스타는 추가 못하지? 링크드인 빼고 인스타 추가하는게 낫지 않나 싶은데.

결과는 Threads와 브라우저 공유 버튼으로 정해졌다 (사용자: "Threads랑 공유 버튼은 넣자"). Threads 버튼은 X와 같은 꼴의 intent 주소를 쓴다.

{% raw %}
```liquid
<a href="https://www.threads.com/intent/post?text={{ _share_text }}&url={{ _share_url }}" class="btn btn--threads" onclick="window.open(this.href, 'window', 'left=20,top=20,width=500,height=600,toolbar=1,resizable=0'); return false;" title="{{ _share_on }} Threads">{% include brand-icon.html name="threads" %}<span>Threads</span></a>
```
{: data-filename="_includes/social-share.html · 일부 발췌"}
{% endraw %}

`onclick`은 링크를 새 탭이 아니라 작은 팝업 창으로 연다. 팝업이 막히거나 스크립트가 꺼진 환경에서는 `return false`가 실행되지 않고 `href`가 그대로 열린다.

공유 버튼은 Web Share API로 브라우저의 공유 시트를 연다. 코드 주석에 적힌 용도는 모바일에서 인스타그램·카카오톡처럼 설치된 앱으로 보내는 것이다.

{% raw %}
```liquid
<button type="button" class="btn btn--inverse page__share-native" style="display:none" data-url="{{ page.url | absolute_url }}" data-title="{{ page.title | strip_html | escape }}" title="{{ site.data.ui-text[lang].share_label | default: 'Share' }}"><i class="material-icons" aria-hidden="true">share</i><span>{{ site.data.ui-text[lang].share_label | default: "Share" }}</span></button>
<script>
(function () {
  var btn = document.currentScript.previousElementSibling;
  if (!navigator.share) return;
  btn.style.display = '';
  btn.addEventListener('click', function () {
    navigator.share({ title: btn.dataset.title, url: btn.dataset.url }).catch(function () {});
  });
})();
</script>
```
{: data-filename="_includes/social-share.html · 일부 발췌"}
{% endraw %}

버튼은 `display:none`으로 시작한다. `navigator.share`가 없는 브라우저, 예를 들어 데스크톱의 Firefox 계열에서는 눌러도 아무 일이 없으므로 아예 보이지 않게 둔다. 있는 브라우저에서는 바로 뒤의 스크립트가 `display`를 지워 보이게 하고 클릭 핸들러를 건다. 스크립트가 자기 직전 형제 요소를 `document.currentScript.previousElementSibling`으로 찾기 때문에 버튼 id가 필요 없다. 사용자가 공유 시트를 닫으면 `navigator.share`의 프로미스가 거부되는데, `catch`가 그것을 삼켜 콘솔에 오류가 남지 않는다. 이 버튼의 로고만은 브랜드가 아니어서 `brand-icon.html`이 아니라 `material-icons`의 `share`를 쓴다.

버튼 색 쪽에서는 `_buttons.scss`의 색 목록에서 `twitter`와 `linkedin`이 빠지고 `x`(`#0f1419`)와 `threads`(`#000`)가 들어왔다. 두 색이 거의 검정이라 다크 테마에서는 버튼 경계가 배경에 묻힌다. 그래서 `inverse`에만 있던 1px 테두리를 `x`와 `threads`에도 주었고, 테두리가 없는 Facebook 버튼에는 `border: 1px solid transparent`를 주어 네 버튼의 높이와 글자 위치가 같게 했다.

## 폭을 맞추는 grid 배치

로고를 SVG로 옮기자 버튼마다 폭이 제각각인 것이 눈에 들어왔다. `X (Twitter)`가 `Facebook`이나 `Threads`보다 훨씬 길기 때문이다. 사용자의 요청은 이랬다.

> 공유하기 버튼들이 흠... 로고는 왼쪽의 특정 위치 (고정된), 그리고 각 이름은 나머지 영역의 중앙정렬 이런 식으로 할 수도 있을까?

```scss
.page__share-buttons {
  display: inline-grid;
  grid-auto-flow: column;
  grid-auto-columns: 1fr;
  column-gap: 0.25em;

  .btn {
    display: grid;
    grid-template-columns: 1.2em 1fr;
    align-items: center;
    justify-items: center;
    column-gap: 0.5em;
    margin-bottom: 0;
  }
}
```
{: data-filename="_sass/minimal-mistakes/_page.scss · 일부 생략"}

바깥 `.page__share-buttons`는 `inline-grid`에 열 방향으로 흐르게 한 뒤 열 폭을 모두 `1fr`로 준다. 폭이 정해지지 않은 grid에서 `1fr` 열들은 가장 넓은 항목의 `max-content`에 맞춰 같은 폭을 갖는다. 그래서 가장 긴 `X (Twitter)` 버튼이 기준이 되고 나머지 버튼이 그 폭까지 늘어난다. 안쪽의 `.btn`은 다시 `1.2em`짜리 고정 칸과 나머지 `1fr` 칸의 두 열 grid다. 로고가 첫 칸 가운데에, 이름이 남은 칸 가운데에 놓이므로 이름 길이가 달라도 로고의 위치는 어긋나지 않는다. 좁은 화면에서는 이름이 숨기 때문에 같은 규칙이 grid를 풀고 로고만 버튼 가운데에 둔다.
