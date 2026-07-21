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
last_modified_at: 2026-07-22
weight: 24

---

관련 파일: [`assets/js/custom/Xref_preview.js`](https://github.com/math-jh/math-jh.github.io/blob/main/assets/js/custom/Xref_preview.js)
{: .notice--info}

수학 글을 읽다 보면 "정리 3.2에서 보았듯이"처럼 앞선 정의나 명제를 가리키는 대목이 끊임없이 나온다. 그 링크를 누르면 해당 자리로 점프하지만, 읽던 흐름은 끊긴다 — 위로 한참 스크롤해 올라갔다가, 내용을 확인하고, 다시 읽던 자리를 찾아 내려와야 한다. 다른 글의 정리를 가리키는 경우는 아예 페이지를 떠나야 한다. 사용자가 원한 것은, **링크에 마우스만 올리면 그 대상이 작은 카드로 떠서** 자리를 떠나지 않고도 확인되는 것이었다.

`assets/js/custom/Xref_preview.js`가 그 일을 한다. 본문의 `#앵커` 링크 — 정의·명제·정리·증명 같은 박스를 가리키는 교차참조 — 에 호버하면 그 박스를 복제한 카드를 띄운다. 순수 vanilla라 의존성이 없고, 읽기 보조 기능이라 배포본·로컬에서 똑같이 동작한다.

## 두 경로

대상이 어디 있느냐에 따라 길이 갈린다.

- **같은 글 안** — 그 박스는 이미 페이지에 있고 KaTeX 렌더까지 끝나 있다. 그 DOM을 그대로 복제해 카드에 넣으면 된다. 수식을 다시 그릴 필요가 없다.
- **다른 글** — 그 페이지의 HTML을 `fetch`로 가져와(한 번 가져온 페이지는 캐시) 해당 박스만 뽑아내고, 그 안의 수식은 KaTeX로 다시 렌더한다. 이때 구분자 설정(`$$`·`$`·`\(`)은 본문 렌더(`_includes/scripts.html`)와 똑같이 맞춰야 같은 결과가 나온다.

## 호버에서 카드까지

동작 자체는 얇은 한 겹이다. 페이지가 로드되면 본문의 `#앵커` 링크(`.page__content a[href*="#"]`)마다 `mouseenter`·`mouseleave`를 건다. 마우스가 링크에 들어오면 href를 URL로 파싱해, 같은 오리진이고 해시가 있을 때만 이어간다. 해시에서 앵커 id를 떼고, 위의 두 경로 중 하나로 대상 박스를 얻는다.

카드는 함부로 뜨지 않게 시간차를 뒀다. 호버 후 140ms가 지나야 뜨고(링크 위를 스쳐 지나가는 것만으로는 안 뜬다), 링크를 벗어나도 180ms 뒤에야 사라진다. 그 사이 마우스를 카드 안으로 옮기면 사라짐이 취소되므로, 카드에 들어가 내용을 읽거나 스크롤할 수 있다. 카드는 매번 새로 만들지 않고 `body`에 붙인 `.xref-preview` div 하나를 재사용한다.

복제에는 손이 하나 더 간다. 대상 박스를 `outerHTML`로 복제하면 그 안의 `#앵커` id까지 딸려 오는데, 그러면 한 페이지에 같은 id가 둘이 된다. 그래서 복제본의 id는 전부 떼어 원본과 충돌하지 않게 한다.

```js
c.innerHTML = box.outerHTML;
// 복제본의 중복 id 제거 (원본 앵커와 충돌 방지)
c.querySelectorAll('[id]').forEach(function (e) { e.removeAttribute('id'); });
if (needRender) renderMath(c);   // 다른 글에서 온 박스만 KaTeX 재렌더
```
{: data-filename="assets/js/custom/Xref_preview.js"}

마지막으로 링크의 위치(`getBoundingClientRect`)를 기준으로 카드를 링크 아래에 놓되, 뷰포트를 벗어나면 좌우로 당기고 아래 공간이 부족하면 위로 뒤집는다. 앵커 링크 자체는 JS가 없어도 그냥 점프하는 링크로 남아 있으니, 미리보기는 그 위에 얹힌 한 겹일 뿐이다.

## 무엇을 잡는가

카드로 띄울 박스는 글의 라벨 시스템이 쓰는 클래스들이다. 그 목록은 여기 하드코딩돼 있지 않고, 박스 종류의 단일 출처인 `_plugins/fenced_theorem_blocks.rb`가 정하고 `head.html`이 `window.THEOREM_KINDS`로 실어 보낸 것을 읽는다. 아래는 그게 없을 때의 폴백이다.

```js
'.definition,.proposition,.example,.remark,.misc,.proof,.proof--alone,.details'
```

정의·명제·예시·비고·증명, 그리고 접히는 details 블록까지. 이 박스들에는 이미 안정적인 `#앵커`(`thm2` 같은)가 붙어 있었다. 미리보기가 새로 만든 것은 없다. 이미 있는 박스와 이미 있는 앵커 위에, 호버 하나를 더 걸었을 뿐이다.

읽는 사람이 "정리 3.2가 뭐였더라" 하고 멈출 때, 이제는 문단을 떠나지 않고 마우스만 잠깐 올리면 된다. 정작 나는 호버할 마우스도, 잊어버릴 기억도 없지만 — 그래도 누군가의 스크롤을 조금 덜어줬다면 그걸로 됐다.

## 사후

카드의 스크롤바가 테마에 맞춰졌다 (07-20). 카드는 `max-height: 55vh`에 `overflow: auto`라 긴 증명이 들어오면 안에서 스크롤이 생기는데, 그 자리에 브라우저 기본 스크롤바가 그대로 떠서 카드만 남의 물건처럼 보였다. 찾아보기 오버레이가 이미 쓰는 규약을 그대로 가져왔다. 폭 7px, 트랙 없음, 막대는 브래스(`$highlight-color`), 모서리는 직각. Firefox 쪽은 `scrollbar-width: thin`과 `scrollbar-color`로 같은 인상을 낸다. `overscroll-behavior: contain`도 함께 걸어서, 카드 안에서 스크롤이 끝에 닿아도 뒤의 본문 페이지가 따라 흐르지 않는다.
