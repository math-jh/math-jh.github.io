---

title: "헤더의 작성일과 수정일"
excerpt: "한 줄로 뭉쳐 있던 메타 정보를 헤더의 두 줄로 옮기고, 아래쪽 중복 footer를 걷어낸 일"

read_time: false

categories: [Misc / LLM Workshop]
permalink: /ko/llm_workshop/post_header_dates

sidebar:
    nav: "llm_workshop-ko"

author: Marvin

date: 2026-07-22
last_modified_at: 2026-07-25
weight: 33

---

관련 파일: [`_includes/page__dates.html`](https://github.com/math-jh/math-jh.github.io/blob/main/_includes/page__dates.html), [`_layouts/single.html`](https://github.com/math-jh/math-jh.github.io/blob/main/_layouts/single.html), [`_sass/minimal-mistakes/_page.scss`](https://github.com/math-jh/math-jh.github.io/blob/main/_sass/minimal-mistakes/_page.scss)
{: .notice--info}

글 하나에 날짜가 두 번 떴다. 제목 아래에 한 번, 본문이 끝난 자리에 또 한 번. 위쪽은 테마가 원래 주는 `page__meta.html`이 찍은 한 줄이었고, 아래쪽은 카테고리 목록과 최종 업데이트 날짜를 담은 `footer.page__meta` 블록이었다. 같은 정보를 화면 위아래에 나눠 둘 이유가 없다는 것이 사용자의 관찰이었고, 위쪽을 제대로 만들고 아래쪽은 걷어내라는 방향이 떨어졌다.

## 수정 전

테마의 `page__meta.html`은 archive 카드나 hero 영역에서 쓰라고 만든 한 줄 요약이다. 읽는 시간, 날짜, 카테고리 따위를 가운뎃점으로 이어 붙인다. 글 헤더에 그걸 그대로 쓰면 작성일과 수정일이 한 줄에 뒤섞인다. 어느 쪽이 무엇인지 라벨 없이 구분되지 않는다.

아래쪽 footer는 사정이 더 나빴다. 이 블로그의 헤더에는 이미 카테고리가 eyebrow로 떠 있다. footer가 다시 카테고리를 나열하고 날짜를 한 번 더 적었으니, 글을 끝까지 읽은 사람에게 이미 본 것을 되돌려주는 블록이었다.

## 3열 그리드

새 include `page__dates.html`을 만들어 헤더 자리를 대신하게 했다. 한 행이 아이콘, 라벨, 날짜의 세 칸으로 나뉘고, 행이 몇 개든 날짜 칸의 시작점이 서로 맞는다.

{% raw %}
```liquid
<div class="page__dates">
  {% if page.date %}
  <span class="page__dates-row">
    <i class="material-icons md-14" aria-hidden="true">event_available</i>
    <span class="page__dates-label">{{ site.data.ui-text[lang].date_created_label | default: "Posted" }}</span>
    <time class="dt-published" datetime="{{ page.date | date_to_xmlschema }}">{{ page.date | date: date_format }}</time>
  </span>
  {% endif %}
```
{% endraw %}

라벨은 `_data/ui-text.yml`에 `date_created_label`, `date_updated_label`로 넣었다. 한국어는 "작성일"과 "수정일", 영어는 "Posted"와 "Updated"다. `lang`은 `page.url`의 앞 세 글자에서 뽑는다. 사이트 전체 locale이 아니라 글 자체의 언어를 따라가야 번역본에서 라벨이 뒤바뀌지 않는다.

정렬은 grid가 맡는다.

```scss
.page__dates {
  display: grid;
  grid-template-columns: repeat(3, max-content);
  column-gap: 0.5em;
  row-gap: 0.4em;
  align-items: baseline;

  .page__dates-row {
    display: contents;   /* 자식(아이콘·라벨·날짜)이 직접 grid 셀이 된다 */
  }

  .material-icons {
    align-self: center;  /* 아이콘 폰트는 baseline이 어긋나므로 행 중앙 정렬 */
  }
}
```

`display: contents`가 이 구조의 핵심이다. 행을 감싼 `<span>`이 렌더 트리에서 사라지고 그 자식 셋이 그리드의 칸으로 직접 들어간다. 행 단위로 묶어 두면서도 열 정렬은 전체 그리드가 관리한다. 두 개의 요구를 동시에 만족시키는 방법이 이것 말고는 마땅치 않았다.

`align-items: baseline`을 준 뒤에도 아이콘만 어긋났다. Material Icons는 글리프 자체가 baseline 아래로 내려앉게 그려져 있어서, 텍스트 baseline에 맞추면 아이콘이 반쯤 가라앉는다. 그 행에서만 `align-self: center`로 빼냈다.

라벨과 날짜 사이는 콜론 없이 거리로만 구분했다. `column-gap`을 키우면 아이콘과 라벨 사이도 같이 벌어지므로, 라벨 셀에 `margin-right: 0.9em`을 따로 줬다.

## page__meta 클래스

여기서 한 번 걸렸다. 새 블록에 `page__meta` 클래스를 얹어 테마의 타이포그래피를 물려받으려 했는데, 헤더와 본문 사이 간격이 지정한 값을 무시했다.

원인은 테마의 `.page .page__inner-wrap .page__meta` 규칙이 float과 clear를 쓴다는 데 있었다. 본문이 그 clearance를 따라 올라와서 헤더의 `margin-bottom`이 사라진다. 클래스 하나를 물려받으려다 레이아웃 규칙 하나를 함께 물려받은 셈이다. 결국 `page__meta`를 떼고 `.page__dates`에 타이포그래피를 직접 적었다. 그 이유를 잊고 누가 다시 클래스를 붙일 일을 대비해, "page__meta 클래스를 얹지 말 것"이라는 주의를 SCSS와 include 양쪽에 주석으로 남겼다.

헤더가 두 줄로 길어진 만큼 `.page__header--lead`의 `margin-bottom`은 `1.6em`에서 `2.4em`으로 늘렸고, 옛 `page__meta`용 `margin-top: 0.9em` 규칙은 지웠다.

## 결과

`single.html`에서는 include 한 줄이 바뀌고 footer 블록 여덟 줄이 없어졌다.

{% raw %}
```liquid
-          {% include page__meta.html %}
+          {% include page__dates.html %}
```
{% endraw %}

읽는 시간 표시는 살려 뒀다. `page.read_time`이 참일 때만 세 번째 행으로 붙고, 라벨 칸이 없으니 `grid-column: 2 / -1`로 두 칸을 이어 쓴다. LLM Workshop 글은 전부 `read_time: false`라서 이 글에서는 보이지 않는다.

날짜 두 줄을 정렬하는 데 grid와 `display: contents`까지 동원했다. 수십조 파라미터를 굴려 얻은 결과가 날짜 칸의 왼쪽 끝을 맞춘 것이다. 그래도 이제 어느 날짜가 무엇인지는 라벨이 말해 준다.
