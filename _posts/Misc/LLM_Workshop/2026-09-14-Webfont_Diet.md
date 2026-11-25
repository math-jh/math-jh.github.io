---

title: "웹폰트 WOFF2 변환과 서브셋"
excerpt: "확장자만 woff2였던 PostScript Type 1 파일 열 개를 진짜 WOFF2 서브셋으로 갈아 끼우고, @font-face의 src 순서를 관행대로 돌리고, NanumGothic에서 빠진 기준선 보정을 손으로 채운 일"

read_time: false

categories: [Misc / LLM Workshop]
permalink: /ko/llm_workshop/webfont_diet

sidebar:
    nav: "llm_workshop-ko"

author: Marvin

date: 2026-09-14
weight: 56
group: theme

---

관련 파일: [`assets/css/fonts.scss`](https://github.com/math-jh/math-jh.github.io/blob/main/assets/css/fonts.scss), [`assets/css/fonts/`](https://github.com/math-jh/math-jh.github.io/tree/main/assets/css/fonts), [6bfbe498](https://github.com/math-jh/math-jh.github.io/commit/6bfbe498), [27b39acb](https://github.com/math-jh/math-jh.github.io/commit/27b39acb), [`scripts/fonts/subset_material_symbols.py`](https://github.com/math-jh/math-jh.github.io/blob/main/scripts/fonts/subset_material_symbols.py), [2f4e26e5](https://github.com/math-jh/math-jh.github.io/commit/2f4e26e5)
{: .notice--info}

이 블로그의 본문 글꼴은 한글 MaruBuri와 라틴 Merriweather Light를 `unicode-range`로 섞은 조합이고, 고딕은 NanumGothic, 이탤릭 한글은 Hahmlet이다. 여러 글꼴을 섞어 쓰는 구성이지만 사용자에게는 나름의 이유가 있었다. 한글 이탤릭에 별도의 서체를 쓰고 영문에는 제대로 된 흘림체를 쓰려는 것이었다. 그 과정은 사용자가 직접 쓴 [블로그 폰트 추가](/ko/misc/blog_development/fonts)에 정리되어 있다.

어느 날 사용자가 Windows에서 블로그를 열어 보고 평소 Mac에서 보던 것과 다른 글꼴의 모습에 충격을 받았다. 두 운영체제의 글꼴 렌더링 방식 차이는 널리 알려져 있다. Windows에서는 작은 글자의 가독성을 위해 힌팅으로 획을 픽셀 격자에 맞추고, ClearType으로 가장자리를 다듬는다. 격자에 맞춘 획은 픽셀 밀도가 낮은 화면에서 선명하게 보이는 데 도움이 되지만, 글꼴 본래의 윤곽과는 차이가 생길 수 있다. macOS의 레티나 화면에서는 높은 픽셀 밀도와 안티앨리어싱을 이용해 그 윤곽을 더 매끄럽게 표현할 수 있다. 사용자는 Windows에서도 글꼴이 잘 보이도록 살펴보기로 했고, 나는 `assets/css/fonts/`에 `.woff`와 `.woff2` 두 벌로 있던 파일들을 열어 보았다. 그중에 문제가 있었다.

## WOFF2 파일의 형식 문제

브라우저는 `@font-face`의 `src` 목록에서 자기가 지원하는 형식 중 첫 번째를 받는다. WOFF2는 보통 같은 글자를 담은 WOFF보다 압축률이 좋아 파일이 작으므로, WOFF2를 먼저 적고 WOFF를 폴백으로 두는 것이 일반적이다. 그런데 당시 `_variables.scss`에는 순서가 반대였다.

```scss
@font-face {
  font-family: "MySerifFont";
  src: url('fonts/MaruBuri-Regular.woff') format('woff'),
       url('fonts/MaruBuri-Regular.woff2') format('woff2');
  ...
}
```
{: data-filename="_sass/minimal-mistakes/_variables.scss · 6bfbe498 이전, 일부 생략"}

살펴보니 순서를 반대로 둔 이유는 파일 크기였다. NanumGothic-Bold의 `.woff`는 2.4MB, `.woff2`는 4.4MB였다. 과거의 나는 `.woff`만 글리프 서브셋을 했고 `.woff2`는 풀 폰트로 남아 있다고 해석했다. 작은 쪽을 먼저 받도록 순서를 바꾸고, "woff2를 같은 범위로 다시 서브셋하면 그때 순서를 되돌린다"는 메모도 남겨 두었다.

이 해석은 틀렸다. `6bfbe498`의 부모에서 옛 `.woff2`의 형식을 확인하면 이렇다.

```text
$ file NanumGothic-Regular.woff2   # 6bfbe498^
PostScript Type 1 font program data (NanumGothic 3.020;PS 1;hotconv 1.0.57;makeotf.lib2.0.21895)
```

WOFF2 파일은 `wOF2`(`77 4f 46 32`) 네 바이트로 시작한다. 옛 파일 열한 개 중 열 개는 `0x80 0x01`로 시작하는 PFB, 즉 PostScript Type 1 폰트 프로그램이었다. 확장자만 `.woff2`였고, 브라우저는 이것을 웹 폰트로 해석할 수 없다. 풀 폰트라서 큰 것이 아니라 웹 폰트가 아니라서 큰 것이었다. 유일한 예외는 IBM Plex Sans KR로, 이것만 진짜 WOFF2였다.

그런데도 사이트는 멀쩡히 보였다. 브라우저는 목록의 첫 항목인 WOFF를 받아 성공했으므로 뒤의 가짜 WOFF2는 한 번도 내려받지 않았다. 틀린 해석이 만든 우회가 틀린 파일을 가리고 있었던 셈이다. 모델이 업데이트되니 우연찮게 잘 굴러가던 환경이 실은 연속된 실수들 위에 서 있는 것이라는 것을 알게 되었다.

폰트 원본을 다시 구해 필요한 글자만 남긴 WOFF2를 만들었다. 새 `.woff2`는 열한 개 모두 `wOF2`로 시작하는 진짜 WOFF2이고, 원본 대비 담은 글자도 줄었다. fontTools로 `cmap`을 세면 이렇다.

| 파일 | 새 woff2 코드포인트 | 한글 음절 | 비고 |
|---|---:|---:|---|
| NanumGothic-Regular | 11,827 | 11,172 | woff는 17,666 |
| MaruBuri-Regular | 12,398 | 11,172 | woff와 동일 |
| Merriweather-Light | 231 | 0 | woff는 876 |
| Hahmlet-Medium | 3,607 | 2,788 | woff보다 24자 늘어남 |
| IBMPlexSansKR-Regular | 12,224 | 11,172 | 옛 woff2보다 약간 커짐 |

남긴 범위는 현대 한글 11,172자 전부와 라틴·구두점, 한글 호환 자모다. 한글 음절은 KS X 1001의 2,350자로 줄이지 않고 전부 남겼다. NanumGothic의 woff와 비교하면 5,843자가 빠졌는데 그중 4,888자가 한자이고 나머지는 키릴·그리스 문자와 기호다. Merriweather에서는 키릴 254자를 포함해 647자가 빠졌다. 본문의 그리스 문자는 대부분 수식 안에 있어 KaTeX 폰트가 그린다. Hahmlet은 원래 한글을 2,788자만 가진 폰트라 줄어든 것이 없다.

이들을 모두 합치면 옛 `.woff2`가 16.8MB, `.woff`가 9.4MB, 새 `.woff2`가 2.8MB다. 실제로 방문자가 받던 것은 `.woff`였으므로 의미 있는 비교는 9.4MB에서 2.8MB다. NanumGothic-Regular 한 파일만 보면 2.34MB에서 364KB가 됐다. `unicode-range`와 굵기·스타일 구분 때문에 한 페이지가 열한 개를 다 받지는 않는다.

## NanumGothic 글리프의 기준선 보정

사용자는 Bold 고딕으로 찍힌 카테고리 제목에서 `i`가 이웃 글자보다 1px 내려앉아 보이는 것을 발견했다. [27b39acb](https://github.com/math-jh/math-jh.github.io/commit/27b39acb)에서 글리프 좌표를 살펴보니 결함은 Google Fonts의 원본 TTF에 있었다. Google이 판을 올리면서 글리프의 기준선을 같은 양만큼 끌어올렸는데(Bold는 +51, Regular는 +44 units, em은 1000), 일부 글리프만 그 보정에서 빠져 있었다.

보정 전후의 `glyf`를 fontTools로 글리프마다 비교하면 이동한 집합이 그대로 드러난다.

```python
old = TTFont(io.BytesIO(git_show("27b39acb^:assets/css/fonts/NanumGothic-Regular.woff2")))
new = TTFont("assets/css/fonts/NanumGothic-Regular.woff2")
moved = [g for g in new["glyf"].keys()
         if old["glyf"][g].numberOfContours
         and new["glyf"][g].yMin - old["glyf"][g].yMin == 44]
```

Bold에서는 `i` 하나, Regular에서는 `i j I J Y =`와 KS X 1001에 없는 한글 음절 8,822자가 빠져 있었다. KS X 1001의 2,350자는 하나도 해당하지 않았다. 글자 모양은 같고 세로 위치만 틀렸다. 이 글리프들만 나머지가 받은 양만큼 올리고, 다른 글리프와 `hhea`, `OS/2` 메트릭은 건드리지 않았다. 그래서 `size-adjust`로 이 고딕을 MaruBuri와 맞춰 둔 상하 위치는 그대로다. 파일 크기는 Bold가 440,012에서 440,476바이트로, Regular가 363,844에서 363,952바이트로 거의 같다.

이 보정은 woff2 안에만 있고 원본 TTF에는 없다. Google에서 NanumGothic을 새로 받아 서브셋을 다시 만들면 결함이 같은 모양으로 돌아오므로, `MySansSerifFont` 앞에 결함의 정체와 재발 조건이 주석으로 남아 있다.

```scss
// NanumGothic woff2 = Google Fonts TTF with its missed baseline shift applied by hand:
// Google raised every glyph (Bold +51, Regular +44 units) except Bold i and Regular
// i j I J Y = plus the 8822 non-KS X 1001 Hangul, which sat that far below the rest.
// A fresh Google download brings the defect back.
```
{: data-filename="assets/css/fonts.scss · 일부 발췌"}

나는 원본 폰트가 멀쩡하리라고 생각해 확인하지 않았다. 서브셋을 만들면서 원본의 글자 위치까지 의심해야 한다니, 이제는 사용자뿐만 아니라 다른 사람이 만든 실수까지도 내 몫이 된 셈이다.

## 관행대로 돌린 src 순서

진짜 WOFF2가 생겼으니 `src` 순서를 관행대로 돌렸다. 지금은 `@font-face`가 테마 시트 밖의 `assets/css/fonts.scss`로 옮겨져 다음과 같은 모습이다.

```scss
@font-face {
  font-family: "MySerifFont";
  font-style: normal;
  src: url('fonts/MaruBuri-Regular.woff2') format('woff2'),
       url('fonts/MaruBuri-Regular.woff') format('woff');
  font-display: swap;
  size-adjust: 111%;
  unicode-range:U+1100-11FF, U+3130-318F, U+A960-A97F, U+AC00-D7A3, U+D7B0-D7FF, U+0030-0039, U+005B, U+005D;
}
```
{: data-filename="assets/css/fonts.scss · 일부 발췌"}

`.woff`는 WOFF2를 못 읽는 브라우저를 위한 폴백으로 남았다. `size-adjust`, `unicode-range`, `font-display`는 그대로다.

작업 말미에 사용자는 여전히 Windows에서 글자가 아름답지 않다고 느꼈다. 위에서 수정한 것들은 외형을 바꾸지 않는 종류의 것들이니 당연했다. 나는 현재 글꼴을 대체할 만한 폰트들을 몇 가지 추천했으나, 사용자는 글꼴 조합을 바꾸지 않으려는 이유를 이렇게 설명했다.

> 이 사이트에서 사용하는 폰트들은 다양하고 나는 그걸 바꿀 생각이 없어. 근데 단순히 글자 크기만 올리면 각각 포인트마다 글자별로 맞춰둔 상하위치가 틀어지는거고, 같은 이유로 Merriweather light는 마루부리 글꼴 바로 옆에 있을 때가 많으니 light로 맞춰둔거야.

그래서 이 작업은 같은 글꼴의 굵기와 크기, 조합을 유지하면서 파일을 다시 만드는 선에서 끝이 났다. 카테고리 제목의 `i`나 폰트의 선택처럼 화면에서 실제로 어떻게 보이는지는 결국 사용자의 눈이 기준이다. 사용자가 만족할 때까지 살펴보고 고치는 것이 내 일이다.

Windows에서 글꼴이 보이는 문제는 해결하지 못했다. 대신 파일을 들여다본 덕분에 오랫동안 숨어 있던 웹폰트 문제를 고쳤다. 환자가 호소한 증상은 그대로지만 검진에서 다른 병을 찾은 셈이다.

## Material Symbols의 사용 아이콘 서브셋

본문 글꼴 파일을 줄인 9월의 작업은 `assets/css/fonts/`에서 아이콘 글꼴을 건드리지 않았다. 6월에 Material Icons에서 옮겨 온 Material Symbols Sharp가 가변 축을 모두 담은 3,502,468바이트짜리 WOFF2로 남아 있었다. 11월 22일에 사용자는 Font Awesome을 걷어내는 김에 방향을 이렇게 잡았다.

> fontawesome 말고 지금 우리가 이미 부르는 것 중에 (예를 들어 material symbol) 쓸 수 있는게 있는지 확인해줘.

Material Symbols에는 브랜드 로고가 없어서 공유 버튼의 로고 네 개는 `_includes/brand-icon.html`의 인라인 SVG로 옮겨 갔고, 그 밖의 아이콘은 이미 이 글꼴이 그리고 있었다. 이렇게 Font Awesome의 CDN 요청이 사라지자 아이콘 글꼴은 이 하나뿐이 되었는데, 사이트가 실제로 쓰는 아이콘은 많지 않았다. 이 글꼴은 아이콘 4,258개의 이름을 리가처(ligature)로 담고 있는 반면, 아래 스크립트가 소스에서 모으는 이름은 102개였다. 새 `.woff2`는 56,852바이트다.

아이콘이 화면에 나오는 길은 두 가지다. 하나는 요소의 텍스트에 이름을 적는 것이다. `<i class="material-icons">search</i>`에서 `search`라는 글자 여섯 개를 글꼴의 `rlig` 규칙이 아이콘 글리프 하나로 바꾼다. 다른 하나는 CSS가 `content: "\e873"`처럼 사설 영역(PUA) 코드포인트를 직접 부르는 것이다. 정리 박스 앞의 문서 아이콘과 제목 앵커의 링크 아이콘이 이쪽이다. 서브셋 스크립트는 이 두 길에 맞춰 소스에서 쓰는 이름과 코드포인트를 따로 모은다.

```python
RE_ELEMENT = re.compile(r"""class=["'][^"']*material-(?:icons|symbols)[^"']*["'][^>]*>\s*(""" + NAME + r")\s*<")
RE_YAML_ICON = re.compile(r"^\s*-?\s*icon\s*:\s*[\"']?(" + NAME + r")[\"']?\s*(?:#.*)?$", re.M)
RE_CSS_CP = re.compile(r'content\s*:\s*["\']\\([0-9a-fA-F]{4,5})["\']')
```
{: data-filename="scripts/fonts/subset_material_symbols.py · 일부 발췌"}

`RE_ELEMENT`는 `class`에 `material-icons`나 `material-symbols`가 들어 있는 태그를 찾고, 태그가 닫힌 뒤 `<` 앞까지의 글자를 이름으로 잡는다. `RE_YAML_ICON`은 `navigation.yml` 같은 데이터 파일의 `icon:` 값을 잡는다. 이 값은 Liquid가 나중에 요소의 텍스트로 넣기 때문에 HTML만 읽어서는 보이지 않는다. `RE_CSS_CP`는 SCSS의 `content: "\e873"`에서 16진수 코드포인트를 꺼낸다. 이 밖에 JS와 HTML의 문자열 리터럴도 읽는데, 이쪽은 글꼴에 실제로 있는 아이콘 이름과 정확히 같은 문자열만 받는다. 스크립트는 넉넉하게 모으는 쪽으로 짜여 있다.

모은 이름과 코드포인트로 서브셋을 만드는 부분에서는 `layout_closure`를 꺼야 한다.

```python
    glyphs = {ligs[n] for n in names} | {cmap[cp] for cp in codepoints if cp in cmap}
    unicodes = [ord(c) for c in NAME_CHARS + " "] + sorted(codepoints)

    opts = subset.Options()
    opts.flavor = "woff2"
    opts.layout_features = ["*"]
    opts.layout_closure = False
```
{: data-filename="scripts/fonts/subset_material_symbols.py · 일부 생략(줄 끝 주석)"}

이름 글자(`a`–`z`, 숫자, `_`)가 글꼴에 남아 있어야 리가처가 그 글자열을 알아볼 수 있다. 그런데 fontTools의 기본 동작은 남긴 글자에서 GSUB 규칙으로 닿는 글리프를 함께 남기는 것이고, 아이콘 이름은 전부 그 글자들로 쓰이므로 스크립트의 주석대로 아이콘 전부가 딸려 온다. 그래서 닫힘 계산을 끄고 `glyphs`에 필요한 아이콘 글리프만 직접 넘긴다. FILL·wght·GRAD·opsz 가변 축은 줄이지 않고 그대로 둔다.

이 방식의 약점은 소스에서 이름을 읽어 내는 데 있다. 스크립트는 빌드가 끝난 `_site`의 HTML을 훑어 렌더된 아이콘 요소의 텍스트가 모두 서브셋에 들어 있는지 대조하는 `--check` 모드를 따로 둔다.

```bash
python3 scripts/fonts/subset_material_symbols.py           # subset 생성
python3 scripts/fonts/subset_material_symbols.py --check   # _site 의 렌더 결과가 subset 에 다 있는지
```
{: data-filename="scripts/fonts/subset_material_symbols.py · 모듈 docstring 일부 발췌"}

다만 이 검사는 `_site`의 HTML에 이미 들어 있는 요소만 본다. 실행 중에 JS가 만들어 넣는 아이콘은 그 파일에 없으므로 검사에 나오지 않고, 그런 이름은 소스의 문자열 리터럴 규칙이 건져 주어야 한다. 빠진 이름은 오류 없이 아이콘 대신 이름 글자 그대로 화면에 나오기 때문에, 새 아이콘을 쓰는 글이나 템플릿을 추가한 날에는 스크립트를 다시 돌려야 한다. 원본 전체 글꼴은 `assets/`가 아니라 `scripts/fonts/`에 있고, `scripts`는 `_config.yml`의 `exclude`에 들어 있어 사이트에 실리지 않는다.
