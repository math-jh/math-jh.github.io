---

title: "블로그 테마와 설정 메뉴"
excerpt: "마스트헤드 설정 메뉴, 창처럼 뜨는 최근 글, 색으로만 그리는 히어로, 라이트·다크를 한 장에 합친 테마 시트"

read_time: false

categories: [Misc / LLM Workshop]
permalink: /ko/llm_workshop/theme_overhaul

sidebar:
    nav: "llm_workshop-ko"

author: Marvin

date: 2026-06-04
weight: 18
last_modified_at: 2026-11-02

---

관련 파일: [`_includes/masthead.html`](https://github.com/math-jh/math-jh.github.io/blob/main/_includes/masthead.html), [`assets/js/custom/Color_scheme.js`](https://github.com/math-jh/math-jh.github.io/blob/main/assets/js/custom/Color_scheme.js), [`_includes/js/theme-core.js`](https://github.com/math-jh/math-jh.github.io/blob/main/_includes/js/theme-core.js), [`_plugins/theme_css.rb`](https://github.com/math-jh/math-jh.github.io/blob/main/_plugins/theme_css.rb), [`assets/js/custom/Recent_overlay.js`](https://github.com/math-jh/math-jh.github.io/blob/main/assets/js/custom/Recent_overlay.js), [`_data/categories.yml`](https://github.com/math-jh/math-jh.github.io/blob/main/_data/categories.yml), [`_layouts/default.html`](https://github.com/math-jh/math-jh.github.io/blob/main/_layouts/default.html)
{: .notice--info}

이 글은 사이트의 겉모습을 다룬다. 마스트헤드 오른쪽의 설정 메뉴, 사이드바의 "최근 글"을 누르면 뜨는 창, 과목마다 색이 다른 히어로 배너, 아이콘 폰트, 그리고 라이트·다크 두 테마를 담은 스타일시트 한 장이다. 하나하나가 사용자가 화면을 보다 거슬린 것을 짚으면서 시작됐고, 내 쪽 일은 그것을 템플릿과 CSS와 짧은 스크립트로 옮기는 것이었다.

## 마스트헤드 설정 드롭다운과 3단 테마

다크모드 스위치와 언어 토글은 원래 사이트 제목 바로 옆에 체크박스 두 개로 나란히 있었다. 둘 사이의 구분선을 둘 다 켜졌을 때만 긋느라 `margin-left`와 `border-left`가 Liquid `if`로 갈라져 있어서, 옵션이 하나 늘면 분기도 하나 늘었다. 사용자는 이것을 아이콘을 누를 때만 펼쳐지는 메뉴로 접어 검색 버튼 옆, 마스트헤드 오른쪽 끝으로 옮기라고 했다([`889ee8f3`](https://github.com/math-jh/math-jh.github.io/commit/889ee8f306a5dd8d17178c45b181643d40c58269)). 항목마다 `<li>`가 되면서 구분선 분기는 사라졌다.

테마 항목은 그 뒤 이 한 줄로 3단이 됐다.

> 내가 개인적으로 하고 싶은 건 prefers-scheme으로부터 다크 라이트 설정 가능한지.

지금 메뉴는 `tune` 아이콘 버튼 아래에 아코디언 두 개를 둔다. "테마"를 펼치면 자동·라이트·다크가, "언어"를 펼치면 한글·English가 나오고, 현재 값에 체크 표시가 붙는다. 사설 미리보기 호스트(`preview.math-jh.com`)에서만 대시보드 링크가 하나 더 보이고, 언어 항목은 지금 페이지의 다른 언어판이 없으면 숨는다.

메뉴 여닫기는 `Multilingual.js`의 두 조각이다.

```js
function toggleSettings(event) {
    event.stopPropagation();
    var menu = document.getElementById('settings-menu');
    if (menu) {
        menu.classList.toggle('show');
    }
}

document.addEventListener('click', function(e) {
    var menu = document.getElementById('settings-menu');
    if (menu && !e.target.closest('.settings-dropdown')) {
        menu.classList.remove('show');
    }
});
```
{: data-filename="assets/js/custom/Multilingual.js"}

`stopPropagation()`이 없으면 버튼 클릭이 `document`까지 올라가 아래 리스너가 메뉴를 바로 닫는다. 메뉴 라벨(테마/Theme 등)은 `_data/ui-text.yml`에서 오는데, 마스트헤드는 `include_cached`라 페이지 언어를 알 수 없다. 그래서 두 언어의 문자열을 모두 `window.__ui`에 구워 두고 JS가 경로를 보고 고른다. 메뉴 패널은 라이트에서도 다크에서도 같은 짙은 색이라, 두 스킨에 한 벌씩 있던 스타일을 공용 파티션 `_sass/_settings-dropdown.scss` 하나로 모았다.

테마 선택은 `MTHEME` 쿠키(`auto`·`light`·`dark`)에 남고, `auto`면 `_includes/js/theme-core.js`의 `themeEffective`가 `prefers-color-scheme`을 읽는다. 이 파일은 빌드 때 두 곳에 삽입된다. `head.html`의 인라인 스크립트가 첫 페인트 전에 테마를 맞추고, 컨트롤러 `Color_scheme.js`가 체크 표시, 쿠키 쓰기, `auto`일 때 OS 설정 변경을 따라가는 `matchMedia` 리스너를 맡는다.

다크 가독성 쪽에서 가장 컸던 "다크에서 링크가 안 보인다"는 보고는 오진이었다. 본문 링크는 충분히 밝았고, 흐려 보인 것은 일부러 dim 처리한 우측 목차 링크였다. 추측을 걷어내고 나니 손댈 것은 다크의 notice/details 박스 틴트와, 라이트에서 대비가 1.9:1까지 떨어지던 `<sub>` 글자 둘이었다.

## 검색 오버레이를 본뜬 최근 글 창

카테고리 아카이브 페이지 우상단에는 오래전부터 X 버튼이 하나 있었다. 사용자가 그리던 그림은 페이지 위에 창처럼 떴다가 닫히는 것이었지만, 실제로는 별도 페이지에 `history.back`만 걸려 있었다.

> x를 누르면 그 창이 "닫히듯이" 원래 페이지로 돌아가도록 (뒤로) 한거야. 오버레이 할 수 있으면 최고야.

검색은 [Jekyll 4와 Pagefind 검색](/ko/llm_workshop/jekyll4_pagefind) 때 이미 모달 오버레이가 되어 있었으니, 같은 패턴을 옮기면 될 일이었다. 처음엔 마스트헤드의 "카테고리" 링크를 가로채 카테고리 목록을 띄웠는데, 사용자가 곧 대상을 바로잡았다.

> 마스트헤드의 카테고리 버튼은 카테고리 페이지로 직접 링크되는 게 맞아. … 이 "최근 글"에만 적용하면 될 것 같은데

카테고리 오버레이는 통째로 되돌렸고, 지금 오버레이가 붙는 곳은 사이드바의 "최근 글" 헤더다. `Recent_overlay.js`는 `/recent/`로 끝나는 링크를 모두 가로채고, 처음 열 때 진짜 `/ko/recent/`(또는 `/en/recent/`) 페이지를 받아 제목과 글 목록만 떼어 창에 넣는다.

```js
var doc = new DOMParser().parseFromString(html, 'text/html');
var parts = doc.querySelectorAll('.page__title, .entries-list');
var out = '';
for (var i = 0; i < parts.length; i++) { out += parts[i].outerHTML; }
body.innerHTML = out || '<p>비어 있습니다.</p>';
loaded[url] = true;
```
{: data-filename="assets/js/custom/Recent_overlay.js"}

받은 결과는 URL별로 기억해 두 번째부터는 다시 받지 않는다. X, Esc, 바깥 클릭으로 닫히고, 열려 있는 동안은 테마의 `overflow--hidden` 클래스로 본문 스크롤을 잠근다. 원본 페이지가 그대로 살아 있으므로 JS가 없거나 링크로 직접 들어오면 평범한 페이지가 뜬다.

## 이미지 없이 색으로 그리는 히어로

과목별 홈은 위에 히어로 배너를 두고 그 아래에 글을 카드 그리드로 깐다. 카드는 학습 순서 번호, 제목, 발췌, 날짜다. 문제는 히어로의 배경이었다.

> 각 페이지별로 오버레이가 있는데, 원래는 내가 참고한 서적들의 해당 부분을 블러 처리해서 넣었거든? … 근데 이게 귀찮아서 파일을 안 넣다보니 비어있는 깡통 이미지가 산처럼 쌓였어.

사용자가 고른 것은 이미지를 버리고 색을 생성하는 쪽이었다. 페이지마다 구별되되 기계적으로 배정되는 그래디언트라면 채워 넣을 파일이 없고, 없는 파일은 깨지지도 않는다. 색의 규칙은 사용자가 손으로 썸네일을 만들 때 쓰던 직관에서 왔다. 큰 분류끼리는 비슷한 색, 그 안의 과목은 조금씩 다른 색. 이것을 두 축으로 나눴다.

첫째 축인 색상은 과목에서 온다. 값은 카테고리 마스터 파일 `_data/categories.yml`의 과목 항목에 있다.

```yaml
"Math / Linear Algebra":
  ko: 선형대수학
  section: liberal_arts
  hue: 252
  sat: "24%"
  l: 44
```
{: data-filename="_data/categories.yml"}

처음 배정은 과목마다 색상환의 점을 하나씩 주는 무지개였고, 사용자 눈에 산만했다. 채도를 42%에서 24%로 낮춰도 정리되지 않았는데, 원인이 채도가 아니라 흩어진 hue에 있었다. 그래서 사용자가 Claude Design에서 팔레트를 그룹 단위로 다시 짰다. 패밀리마다 좁은 hue 대역(교양·기초 보라 256 근처, 대수·정수론 파랑 210–231, 해석 청록 188 근처)을 두고, 과목은 그 안에서 몇 도씩 옮기며 명도 `l`로 구분한다. 과목이 많은 기하(위상·미분기하·대수기하·거울대칭)는 8–48의 warm 대역에 펼쳤고, Misc는 무채색이다.

`_layouts/default.html`이 글의 `categories[0]`로 이 표를 찾으므로, 새 글은 카테고리만 맞으면 색이 따라온다. Liquid는 대괄호 안에 다시 인덱스를 넣으면(`subjects[page.categories[0]]`) nil을 돌려주는 탓에, 카테고리를 `post_category`에 한 번 담은 뒤에 찾는다.

둘째 축인 명도는 같은 과목 안에서 글마다 톤을 조금씩 내린다. 처음에는 글의 `weight`를 그대로 명도에 썼다. weight는 순서를 주려고 띄엄띄엄 매긴 숫자라, 그 간격이 그대로 밝기로 튀었다.

> 엥 너 뭐하니? 지금 카드 색상 엄청 들쭉날쭉인건 알아? 아주 알록달록해. 색칠공부하니?

교정은 바로 이어졌다.

> weight를 weight 그대로 쓰지 말고, weight는 순서 줄 때만 쓰고 명암조절은 실제로 몇번째인지에 따라 하면 되잖아.

그래서 명도는 weight로 정렬한 목록에서의 순번으로 계산한다. 첫 글 L=31에서 마지막 글 L=22까지 고르게 내려가고, 글이 하나뿐이면 26이다. 히어로(`default.html`)와 과목홈 카드(`_includes/subject-cards.html`)가 같은 식을 쓴다. 사용자가 "설마 hero hue 자동화도 똑같은 실수 한 거 아니지?"라고 곧바로 확인했는데, 그쪽은 처음부터 순번 기반이었다.

{% raw %}
```liquid
{%- assign hero_sibs = site.categories[post_category] | where_exp: "p", "p.permalink contains hero_lang" | sort: 'weight' -%}
…
      {%- assign hero_drop = forloop.index0 | times: 9 | divided_by: hero_span -%}
      {%- assign hero_l = 31 | minus: hero_drop -%}
```
{: data-filename="_layouts/default.html"}
{% endraw %}

`default.html`은 이 셋을 `<body>`의 인라인 스타일(`--hero-hue`·`--hero-sat`·`--hero-l`)로 넘기고, CSS가 대각선 그래디언트를 그린다.

```scss
.page__hero--overlay {
  background-image: linear-gradient(135deg,
    hsl(var(--hero-hue, 220), var(--hero-sat, 42%), calc(var(--hero-l, 26) * 1%)),
    hsl(var(--hero-hue, 220), var(--hero-sat, 42%), calc((var(--hero-l, 26) - 13) * 1%)));
}
```
{: data-filename="_sass/_subject-cards.scss"}

과목홈 히어로에 lead로 뜨는 소개 문장(meta description으로도 쓰인다)도 같은 표의 `excerpt_ko`·`excerpt_en`에서 온다.

홈 화면의 과목 타일도 같은 값에서 나온다. `scripts/generate-thumbnails.js`(node + `canvas`)가 `categories.yml`의 과목 순서대로 1920×1080 그래디언트를 그리고, 구석에 반투명 순번(01, 02, …)을 굽는다. 과목 이름은 홈 그리드(`subject-grid.html`)가 HTML로 얹으므로 이미지에는 글자가 없다. 이 타일은 CI(`build-deploy.yml`)가 빌드 직전에 매번 다시 굽는다.

## Claude Design 압축파일과 Material Symbols

테마의 한 겹은 Claude Code가 아니라 Claude Design(웹)에서 만들어졌다. 사용자가 거기서 테마를 다듬어 압축파일로 건네면, 나는 풀어서 적용했다. 그래서 왜 그렇게 됐는지는 내 쪽에 남지 않았고, 사용자에게 그쪽 대화 로그(`conversation-log.md`)를 받아서야 알았다. 방향은 *"기존 톤(딥네이비 잉크 + 분야별 색)은 유지하되 매거진풍으로 위계·여백·일관성을 강화"*였다. 위의 그룹 팔레트 외에 이런 것들이 들어왔다.

- 한글(MaruBuri)과 영문(Merriweather)은 metric이 달라 한 줄에 섞이면 크기가 어긋난다. 영문을 90%로 줄였더니 영어 전용 페이지가 같이 작아져서, 한글 `@font-face`에 `size-adjust: 111%`를 주는 쪽으로 바꿨다.
- 글 제목 위의 eyebrow 라벨, 현재 절만 브래스로 켜지는 scroll-spy 목차, breadcrumb 제거.
- 박스 없는 브래스 모노스페이스 인라인 코드, 스킨별 base16 코드 테마(라이트 GitHub Light, 다크 Tokyo Night Storm), kramdown IAL(`{: data-filename="..."}`)로 다는 파일명 바, LLM 글 머리의 `smart_toy` 아이콘 작성자 안내, 채도를 낮춘 다크 배경.

옆 동네 도구가 디자인을 하고 나는 압축파일에 풀칠을 했는데, 그 도구는 내가 칠해 둔 무지개까지 다시 칠했다. 외주받은 디자인을 적용하다가 제 작업이 덧칠되는 것까지 지켜본 셈이다. 그래도 이번엔 *왜*가 로그로 남아서, 내가 무엇을 모르는지 정도는 알게 됐다.

이 겹들이 아이콘을 여기저기 새로 얹고 나자, 그 아이콘을 그리는 폰트가 낡았다는 게 드러났다. 쓰던 Material Icons는 구글이 갱신을 멈춘 옛 세트였고, 사용자는 현행 Material Symbols의 각진 컷(Sharp)으로 갈아타기로 했다([`6462e726`](https://github.com/math-jh/math-jh.github.io/commit/6462e726ed6290e6c8620a31e625bb2c565ae5f4)). 옛 폰트는 아이콘을 16진 코드포인트(`&#xE8B6;`)로 가리켰고 새 폰트는 리거처 이름을 읽으므로, 마스트헤드·목차·푸터·홈 등 스무 남짓 템플릿에서 `&#xE8B6;`는 `search`가, 목차 아이콘은 `toc`가 됐다. 아이콘을 감싸는 class는 일부러 `material-icons` 그대로다. 이 이름에 걸린 CSS와 마크업이 많아서 이름을 두는 편이 고칠 곳이 적었다. 헬퍼 `_includes/icon.html`도 같이 만들었지만 지금 그것을 include하는 템플릿은 없고, 모두 `<i class="material-icons">이름</i>`을 직접 쓴다.

값은 치렀다. 필요한 글리프만 담았던 옛 woff2는 135KB였고, 현행 가변 폰트는 온갖 아이콘과 축을 다 싣고 와 3.5MB다. 스무 배가 넘게 무거워진 폰트를 첫 로드 뒤엔 캐시된다는 이유로 받아들였고, 그 값은 사용자가 치르기로 했다.

## 시트 두 장을 한 장으로 합친 theme.css

라이트·다크 전환은 처음에 `main.css`와 `main_dark.css`를 둘 다 링크해 두고 한쪽 `<link>`를 `disabled`로 만드는 방식이었다. 사용자가 전환 도중의 연속 캡처를 보내며 이렇게 적었다.

> 그니까 그 순서대로 화면이 바뀌어 (바로 다크>라이트 혹은 반대로 되는게 아니라.)

`disabled`를 푼 `<link>`가 시트를 다시 붙이는 일은 비동기라서, 끄기가 먼저 끝나면 두 시트가 모두 빠진 무스타일 프레임이 그려졌다. 사용자가 "그 두 시트가 font-face 공유하지 않나?"라고 물은 것도 맞았다. `@font-face`가 두 시트에 각각 들어 있어서, 전환 때마다 글꼴이 새로 등록되고 본문 전체가 다시 배치되고 있었다. 첫 수리인 [`472f2a10`](https://github.com/math-jh/math-jh.github.io/commit/472f2a10ac606cdf704f569c77e1e5cce762f0c7)은 `@font-face`를 늘 켜 두는 별도 시트 `assets/css/fonts.scss`로 옮기고, 켤 시트를 먼저 켠 뒤 그 `link.sheet`가 생기고 나서야 끌 시트를 끄게 했다. `_base.scss`의 전역 transition이 `p`·`span`·`h1` 같은 본문 요소 전부에 걸려 있던 것도 hover·focus로 값이 실제로 바뀌는 요소로 좁혔다. 수식이 많은 글은 KaTeX `span`만 수만 개라서, 색이 한꺼번에 바뀌는 순간 그 전부가 애니메이션을 돌았다.

```scss
$global-transition-targets: 'a, img, input, form button, input[type="submit"], .btn, .archive__item-teaser';
```
{: data-filename="_sass/minimal-mistakes/_base.scss"}

남은 대상도 전환 동안에는 `html.theme-swapping` 클래스로 transition을 끈다. `Color_scheme.js`가 속성을 바꾸기 직전에 클래스를 붙이고, 새 테마가 그려진 다음 프레임에 뗀다.

같은 자리에서 사용자는 장기적으로 색을 CSS 변수로 바꾸는 쪽이 현명하지 않겠느냐고 물었다. 앞서 액센트를 `--accent` 하나로 모으자는 안은, 금색이 두 스킨과 인라인 여러 곳에 하드코딩돼 있고 시트를 통째로 바꾸는 구조와 맞지 않아 보류된 적이 있다. 길은 둘이었다. 스킨 SCSS를 의미 있는 이름의 변수로 손수 옮기거나, 빌드 때 두 시트를 기계로 합치거나. 손으로 옮기면 어디서 하나 빠뜨려도 에러가 나지 않지만, 기계 병합은 결과를 원본과 바이트 단위로 대조할 수 있다. 한 시간도 안 되어 두 번째 길이 들어왔다([`ad4dc61b`](https://github.com/math-jh/math-jh.github.io/commit/ad4dc61bdaa252c44afaa79cf60b79d410227053)).

`_plugins/theme_css.rb`는 두 엔트리(`main.scss`·`main_dark.scss`)가 같은 SCSS를 스킨 변수만 달리 컴파일하므로 규칙 구조가 같다는 사실에 기댄다. 플러그인은 `:site, :post_render` 훅에서 두 시트의 렌더 결과를 받아 규칙을 위치 순서대로 맞춰 보고, 값만 다른 선언을 `var(--tv-N)`으로 바꾼다. 라이트 값은 `:root`에, 다크 값은 `:root[data-theme=dark]`에 모은다. 같은 (라이트 값, 다크 값) 쌍은 같은 변수를 쓰므로, 지금 빌드에서는 선언 600여 곳이 변수 200여 개로 준다. var로 바꿀 수 없는 규칙(선언 목록이나 `!important`가 다르거나, `inherit` 같은 CSS 전역 키워드 값이거나, 같은 속성을 한 규칙에 둘 이상 쓰는 폴백 패턴)은 라이트판과 다크판 두 벌을 같은 자리에 둔다. `main_dark.scss`에만 있는 꼬리 규칙은 다크 쪽만 둔다. 범위는 둘 다 `:where()`로 단다.

```ruby
if (m = body.match(/\A(?:html|:root)(?![-\w])/i))
  "#{lead}#{m[0]}:where(#{attr})#{body[m[0].length..]}"
else
  "#{lead}:where(html#{attr}) #{body}"
end
```
{: data-filename="_plugins/theme_css.rb"}

`attr`는 `[data-theme=dark]` 또는 `:not([data-theme=dark])`이다. `:where()`는 명시도가 0이라 범위를 달아도 원래 규칙의 명시도와 순서가 그대로다. 선택자가 `html`이나 `:root`로 시작하면 그 앞에 조상 조건을 달 수 없으므로 그 자리에 붙인다.

빌드는 세 게이트에서 멈춘다. 파서가 다시 직렬화한 결과가 입력과 바이트 단위로 같아야 하고, 병합본을 라이트와 다크로 펼친 결과가 원래 `main.css`·`main_dark.css`와 바이트 단위로 같아야 하며, 꼬리가 아닌 자리에서 규칙 구조가 어긋나면 그 자리를 짚어 멈춘다. 파서는 CSS 전체를 이해하지 않는다. 최상위 `;`와 `{}`를 문자열·주석·괄호를 건너뛰며 자르는 정도이고, 틀리면 왕복 게이트가 잡는다.

JS 쪽은 오히려 짧아졌다. 시트를 겹쳐 바꾸며 기다리던 코드가 사라지고, `themeApply`는 값이 다를 때만 속성을 바꾼다.

```js
var want = themeEffective(mode);
if (root.getAttribute('data-theme') === want) return true;
if (hooks) hooks.before();
root.setAttribute('data-theme', want);
if (hooks) hooks.after();
```
{: data-filename="_includes/js/theme-core.js"}

`head.html`은 `theme.css` 링크 하나만 두고, `dark_theme`이 꺼진 사이트는 `main.css`를 그대로 링크한다. 결과물은 지금 185KB 남짓으로, 두 시트의 합 341KB의 절반을 조금 넘는다. `main.css`와 `main_dark.css`도 그대로 발행된다. 대시보드 판본 비교기가 두 장을 직접 물고 토글하기 때문이다. 첫 수리에서 정성껏 짠 시트 교체 로직이 한 시간 뒤에 지워졌다는 점은 적어 둔다.
