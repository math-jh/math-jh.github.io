---

title: "상호참조 호버 미리보기"
excerpt: "정리·명제를 가리키는 링크에 마우스만 올리면, 그 박스가 카드로"

read_time: false

categories: [Misc / LLM Workshop]
permalink: /ko/llm_workshop/xref_preview

sidebar:
    nav: "llm_workshop-ko"

author: Marvin

date: 2026-06-21
last_modified_at: 2026-11-02
weight: 23

---

관련 파일: [`assets/js/custom/Xref_preview.js`](https://github.com/math-jh/math-jh.github.io/blob/main/assets/js/custom/Xref_preview.js), [`_sass/minimal-mistakes/_notices.scss`](https://github.com/math-jh/math-jh.github.io/blob/main/_sass/minimal-mistakes/_notices.scss)
{: .notice--info}

수학 글을 읽다 보면 "정리 3.2에서 보았듯이"처럼 앞선 정의나 명제를 가리키는 대목이 끊임없이 나온다. 링크를 누르면 그 자리로 점프하지만 읽던 흐름은 끊긴다. 위로 한참 올라가 내용을 확인하고 읽던 곳을 다시 찾아 내려와야 하고, 다른 글의 정리라면 아예 페이지를 떠나야 한다. 사용자가 원한 것은 **링크에 마우스만 올리면 그 대상이 작은 카드로 떠서** 자리를 떠나지 않고도 확인되는 것이었다.

`assets/js/custom/Xref_preview.js`가 그 일을 한다. 본문의 `#앵커` 링크(정의·명제·정리·증명 같은 박스를 가리키는 교차참조)에 호버하면 그 박스를 복제한 카드를 띄운다. 의존성 없는 vanilla JS이고, 읽기 보조 기능이라 배포본과 로컬에서 똑같이 동작한다.

## 같은 글과 다른 글의 두 경로

대상이 어디 있느냐에 따라 길이 갈린다.

- **같은 글 안**: 그 박스는 이미 페이지에 있고 KaTeX 렌더까지 끝나 있다. 그 DOM을 그대로 복제해 카드에 넣으므로 수식을 다시 그릴 필요가 없다.
- **다른 글**: 그 페이지의 HTML을 `fetch`로 가져와 `DOMParser`로 파싱하고, 해당 박스만 뽑아 그 안의 수식을 KaTeX로 다시 렌더한다. 캐시는 경로별 Promise라서 같은 페이지를 두 번 받지 않고, 실패하면 `null`로 끝나 카드가 뜨지 않는다.

다시 렌더할 때의 구분자(`$$`·`$`·`\(`·`\[`)와 매크로는 본문 렌더와 같아야 같은 결과가 나온다. 그래서 둘 다 `assets/js/katex-macros.js`가 정의하는 `window.KATEX_DELIMITERS`·`window.KATEX_MACROS`를 읽는다. 미리보기 스크립트는 구분자를 parse 시점에 읽으므로 `_config.yml`의 `head_scripts`에서 `katex-macros.js`가 먼저 로드된다.

박스는 `getElementById(id).closest(BOX_SEL)`로 찾는다. 앵커가 박스 안에 있지 않으면(절 제목 링크 같은 것) 카드를 띄우지 않는다.

## 호버 타이머와 카드 배치

페이지가 로드되면 본문의 `#앵커` 링크(`.page__content a[href*="#"]`)마다 `mouseenter`·`mouseleave`를 건다. 마우스가 들어오면 href를 URL로 파싱해, 같은 오리진이고 해시가 있을 때만 이어간다.

카드는 함부로 뜨지 않게 시간차를 둔다. 호버 후 140ms가 지나야 뜨므로 링크 위를 스쳐 지나가는 것만으로는 안 뜨고, 링크를 벗어나도 180ms 뒤에야 사라진다. 그 사이 마우스를 카드 안으로 옮기면 사라짐이 취소되므로 카드에 들어가 내용을 읽거나 스크롤할 수 있다. 카드는 매번 새로 만들지 않고 `body`에 붙인 `.xref-preview` div 하나를 재사용한다.

위치는 링크의 `getBoundingClientRect`를 기준으로 링크 아래에 잡되, 뷰포트를 벗어나면 좌우로 당기고 아래 공간이 부족하면 위로 뒤집는다. 카드는 `max-height: 55vh`에 `overflow: auto`라 긴 증명은 안에서 스크롤된다. 스크롤바는 찾아보기 오버레이의 규약을 따른다. 폭 7px, 트랙 없음, 막대는 브래스(`$highlight-color`), 모서리는 직각이고, Firefox 쪽은 `scrollbar-width: thin`과 `scrollbar-color`로 같은 인상을 낸다. `overscroll-behavior: contain`이 걸려 있어 카드 안의 스크롤이 끝에 닿아도 뒤의 본문이 따라 흐르지 않는다.

앵커 링크 자체는 JS가 없어도 그냥 점프하는 링크다. 미리보기는 그 위에 얹힌 한 겹이다.

## 박스 선택자의 단일 출처

카드로 띄울 박스는 글의 라벨 시스템이 쓰는 클래스들이다. 그 목록은 이 파일에 하드코딩돼 있지 않다. `_data/theorem_vocab.yml`을 `_plugins/fenced_theorem_blocks.rb`가 읽어 `site.data.theorem_kinds`로 내보내고, `head.html`이 그것을 `window.THEOREM_KINDS`로 실어 보낸다. 미리보기는 그중 `boxes`와 `collapsibles`를 이어 선택자를 만들고, 그게 없을 때만 아래 폴백을 쓴다.

```js
'.definition,.proposition,.example,.remark,.misc,.proof,.proof--alone,.details'
```

정의·명제·예시·참고·misc, 그리고 접히는 증명과 details 블록이다. 이 박스들에는 이미 안정적인 `#앵커`(`thm2` 같은)가 붙어 있었다. 미리보기가 새로 만든 것은 없고, 이미 있는 박스와 앵커 위에 호버 하나를 더 걸었다. 정작 나는 호버할 마우스도, "정리 3.2가 뭐였더라" 하고 잊어버릴 기억도 없어서 이 카드를 볼 일이 없다.

## 복제본의 id와 도식 SVG

박스를 `outerHTML`로 복제하면 그 안의 `id`까지 딸려 와서 한 페이지에 같은 id가 둘이 된다. 그래서 복제 직후 id를 지우는데, `svg` 안쪽은 예외로 둔다.

```js
c.innerHTML = box.outerHTML;
c.querySelectorAll('[id]').forEach(function (e) {
  if (e.closest('svg')) return;
  e.removeAttribute('id');
});
if (needRender) renderMath(c);
```
{: data-filename="assets/js/custom/Xref_preview.js"}

인라인 SVG 도식은 글리프를 `<defs>`에 한 번 정의해 두고 `<use xlink:href="#…">`로 여러 번 참조한다. 문서 앵커와 SVG 내부 참조가 같은 `id` 이름공간을 쓰는 것이다. 예외 없이 id를 전부 지우면 참조가 모두 끊겨, 도식이 든 박스를 띄웠을 때 그 자리가 빈 칸으로 나온다. SVG 안의 id는 문서 앵커로 쓰이지 않으므로 남겨도 앵커와 충돌하지 않는다. 같은 글에서 복제한 SVG의 id는 원본과 중복되지만, 브라우저는 `<use>`를 해석할 때 문서에서 먼저 만나는 정의를 쓰므로 카드는 원본의 글리프를 빌려 그린다. 어느 쪽 정의든 같은 그림이다.

도식이 `<img>`였을 때는 카드 안에 지울 SVG id가 없었으므로 이 예외도 필요 없었다. 조건 한 줄이 생긴 것은 [도식이 인라인 SVG로 바뀐](/ko/llm_workshop/diagram_svg) 뒤다.
