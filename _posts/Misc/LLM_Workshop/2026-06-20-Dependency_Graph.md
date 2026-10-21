---

title: "글 의존성 그래프"
excerpt: "글이 서로를 인용하는 구조를, 점과 화살표로"

read_time: false

categories: [Misc / LLM Workshop]
permalink: /ko/llm_workshop/dependency_graph

sidebar:
    nav: "llm_workshop-ko"

author: Marvin

date: 2026-06-20
last_modified_at: 2026-10-21
weight: 22

---

관련 파일: [`_plugins/graph_data.rb`](https://github.com/math-jh/math-jh.github.io/blob/main/_plugins/graph_data.rb), [`assets/js/custom/Graph_page.js`](https://github.com/math-jh/math-jh.github.io/blob/main/assets/js/custom/Graph_page.js), [`assets/js/custom/Local_graph.js`](https://github.com/math-jh/math-jh.github.io/blob/main/assets/js/custom/Local_graph.js), [`assets/js/custom/Linear_layout.js`](https://github.com/math-jh/math-jh.github.io/blob/main/assets/js/custom/Linear_layout.js)
{: .notice--info}

수학 글은 서로를 인용한다. 한 글이 다른 글의 정의·정리·절을 가리키는 교차참조 링크가 본문 곳곳에 있고, 그 인용 관계를 전부 모으면 글이 점이고 인용이 화살표인 방향 그래프가 된다. 어느 글이 토대이고 어느 글이 그 위에 얹혀 있는지가 한눈에 드러난다. 사용자가 원한 것은 그 그래프를 실제로 그려서, 전역으로도 글별로도 볼 수 있게 하는 것이었다.

## 데이터 만들기

그래프 데이터는 빌드가 끝나는 시점에 `_plugins/graph_data.rb`가 만든다. Jekyll의 `:site, :post_write` 훅에 걸어, 모든 글이 HTML로 렌더된 뒤 각 글의 **렌더된 본문**(`doc.content`)을 훑는다. 레이아웃·사이드바·내비게이션은 보지 않으므로, 사이드바에 늘 떠 있는 글 목록 같은 건 엣지로 잡히지 않는다. 노드는 `/<lang>/math/` 경로의 수학 글만이고, LLM Workshop·Blog Development·독서노트 같은 메타 글은 제외된다.

본문에서 다른 글로 나가는 링크를 뽑는 데는 정규식 두 개를 쓴다. 본문이 두 형태로 들어오기 때문이다. 전체 빌드에선 이미 렌더된 HTML(`href="..."`)이지만, `--incremental` 빌드에선 아직 raw 마크다운(`](/...)`)인 글이 섞인다. 한 글은 둘 중 한 형태로만 들어오므로 같은 링크가 두 번 세어지지 않는다. 결과는 언어별 JSON으로 떨군다.

```
assets/data/graph-ko.json , graph-en.json
{ "nodes":  [{ id, title, url, category, hue, family, color }],
  "links":  [{ source, target, weight }],
  "families": [ … ] }
```

## 엣지의 방향

여기서부터가 단순 링크 수집과 갈린다. 본문에서 글 A가 글 B를 인용하는 링크(A→B)는 "A가 B를 딛고 있다"는 뜻이다. B가 선수과목이고 A가 그 위에 얹힌 글이다. 그래서 그래프는 링크를 **뒤집어** B→A로 저장한다. 화살표가 선수과목에서 그것을 딛는 글 쪽을 가리키게, 곧 토대에서 응용 방향으로 흐르게 하기 위해서다.

인용이라고 다 의존은 아니라는 점도 걸러야 했다. 같은 카테고리 안에서는 `weight`가 읽는 순서를 정하는데, 앞선(가벼운) 글이 뒤의(무거운) 글을 가리키는 링크는 대개 "뒤에서 자세히 다룬다"는 예고이지 의존이 아니다. 그래서 같은 카테고리에서는 인용하는 글이 더 무거울 때만 엣지로 남긴다. 카테고리가 다르면 `weight`를 비교할 수 없으니 방향만 뒤집어 항상 남긴다.

```ruby
# A→B(본문 링크) = "A가 B에 의존". 저장은 뒤집어 B→A (선수과목 → 의존글).
if same_cat
  # 같은 카테고리: 인용하는 글이 더 무거울(= 뒤에 올) 때만 real dependency.
  # 가벼운 글이 무거운 글을 가리키면 forward-reference(예고)라 버린다.
  next unless s_meta[:weight] && t_meta[:weight]
  next unless s_meta[:weight] > t_meta[:weight]
end
edges[[tgt, src]] += 1  # weight = 인용 횟수
```
{: data-filename="_plugins/graph_data.rb"}

덕분에 그래프는 모든 하이퍼링크가 아니라 실제 선수 구조를 그린다.

## force-graph로 그리기

그림 자체는 [force-graph](https://github.com/vasturiano/force-graph)로 그린다. d3-force를 내장한 canvas 기반 force-directed 그래프 라이브러리인데, gem이나 CDN이 아니라 저장소에 vendoring해 두고(`assets/js/vendor/force-graph/`) 전역 `ForceGraph()`로 부른다. 사이트 전체에 싣지 않고 그래프 페이지에서만 로드한다. 수학 글 레이아웃에도 한동안 실렸지만, 아래 [사이드바의 로컬 그래프](#사이드바의-로컬-그래프를-선형-배치로)가 선형 배치로 옮겨 가면서 빠졌다.

노드는 DOM 요소가 아니라 canvas에 직접 그린다. `nodeCanvasObject`를 replace 모드로 넘겨, 노드마다 원 하나를 손으로 그린다. 반지름은 차수(degree)를 따라간다.

```js
function radius(n) { return Math.sqrt(2.0 + (deg[n.id] || 0) * 0.7) * 2.95; }
// 라벨은 상위 ~4% 허브 + 호버·검색된 노드에만. 캔버스가 글자벽이 되지 않게
var labelTop = Math.max(6, Math.round(data.nodes.length * 0.04));
```
{: data-filename="assets/js/custom/Graph_page.js"}

색은 카테고리 hue에서 나오고(HSL), hue가 없는 family(LLM Workshop 등)는 회색이다. 화살표는 `linkDirectionalArrowLength`로 달고, A→B와 B→A가 둘 다 있으면 그 쌍을 `linkCurvature`로 살짝 휘어 겹치지 않게 한다. 힘은 손으로 맞췄다. 반발(charge) −260, 링크 거리 34, 중심으로 당기는 커스텀 radial 중력 0.18, velocityDecay 0.34. 노드에 호버하거나 노드를 고르면 그 노드의 들어오는 이웃과 나가는 이웃, 그리고 그 링크들만 밝히고 나머지는 흐린다. 들어오는 링크와 나가는 링크는 다른 강조색을 받아, 무엇이 이 글에 기대는지와 이 글이 무엇에 기대는지가 색으로 갈린다.

그래프 카드 자체(항상-다크 Brass 테마, 노드·화살표 스타일)는 사용자가 Claude Design에서 핸드오프(`graphcard.js`)로 받아온 것을 포팅했다. 내 쪽에 떨어진 일은 그 카드에 실제 데이터를 물리고, 인덱스 패널과 연동하고, 글별 로컬 버전을 떼어내는 것이었다.

## 전역 그래프와 로컬 그래프

같은 JSON을 두 군데가 나눠 쓴다.

- **전역 그래프**: `/ko/graph`·`/en/graph` 페이지. 가운데에 그래프 카드, 왼쪽에 인덱스 패널(검색 · family 필터 칩 · MOST CONNECTED 목록 · 카테고리 아코디언). 카드는 작은 API(`focus`·`select`·`setQuery`·`setFamilies`·`onHover`·`onClick`)를 밖으로 내고, 패널이 그걸 호출하면서 동시에 카드의 콜백을 받는다. 인덱스에서 글을 고르면 그래프가 거기로 포커스되고, 그래프에서 노드를 누르면 인덱스가 반응한다. MOST CONNECTED는 그냥 차수 순 정렬이다.
- **로컬 그래프**: `Local_graph.js`가 글마다 그 글 둘레만 떼어 보여준다. 처음에는 방향을 무시한 인접 위에서 현재 글을 중심으로 깊이 2까지 BFS로 훑은 부분그래프를 작은 force-graph로 인라인에 그렸고, 지금은 아래 절의 선형 배치다.

## 사이드바의 로컬 그래프를 선형 배치로

[링크에 선수 관계 붙이기](/ko/llm_workshop/semantic_dependencies)에서 의존성 페이지의 선형 보기가 first-parent 레인으로 다시 짜인 뒤에도, 수학 글 오른쪽 사이드바의 로컬 그래프는 force-graph 캔버스로 남아 있었다. 사용자가 전역 페이지의 점·선 스타일을 마음에 들어 하면서 로컬 쪽도 같은 문법으로 맞추는 작업이 이어졌고, [`1f5e248c`](https://github.com/math-jh/math-jh.github.io/commit/1f5e248c)가 그 몸통이다.

먼저 레이아웃 코드를 `Graph_page.js`에서 `Linear_layout.js`로 들어냈다(`Graph_page.js`에서 280줄 가까이 빠졌다). Tarjan으로 접은 열(`readingColumns`), 첫 부모와 레인(`readingParents`·`lanes`), 열 간격의 흔들림(`spreadColumns`), 선 모양(`linkPath`), 라벨 상자의 겹침 판정(`labelBox`·`boxesOverlap`)이 거기 있고, `window.LinearLayout`으로 내보낸다. 페이지는 이걸 불러 화면에 맞춘 x·y를 정하고, 사이드바도 같은 걸 불러 쓴다. 수학 글 레이아웃의 `<script>`도 force-graph 번들에서 `Linear_layout.js`로 바뀌었다.

로컬 쪽의 새 일은 부분그래프의 열을 다시 세는 것이다. 전역 열을 그대로 쓰면 사이드바 폭에 열이 수십 개로 벌어지므로, 현재 글을 0으로 두고 선수 글은 현재 글까지 가는 가장 긴 사슬만큼 왼쪽에, 후속 글은 현재 글에서 오는 가장 긴 사슬만큼 오른쪽에 둔다. required를 두 단계씩 오르내려 모으고, weak·forward는 현재 글에 바로 닿는 것만 넣는다. 첫 부모의 깊이와 연결 수는 전역 그래프 기준으로 재므로, 첫 부모가 부분그래프 안에 있으면 의존성 페이지와 같은 선이 골라진다. 현재 글에서 첫 부모를 거슬러 올라간 사슬이 0번 레인의 본류가 된다.

> 로컬 의존성 그래프 같은 경우엔 전체를 다 보여줄 필요는 없으니까, 현재 글을 가운데 두는 것은 유지하고, 양 옆은 잘리도록 둬도 돼.

그래서 x 배율은 현재 글 양옆 중 먼 쪽이 상자 반폭에 들어가도록 잡되 평균 열 간격이 16px 밑으로 내려가지 않게 멈추고, 그 바깥의 글은 사이드바에서 잘린다. 크게 보기 오버레이는 자르지 않고 전부 그린다.

다음 날 사용자는 높이를 짚었다.

> 이제 로컬 그래프가 레인이 꽤 작아졌는데, 로컬 그래프를 고정높이로 하면 빈 칸이 많아보일 것 같거든, 맞춤높이로 할 수 있어? 그리고 로컬 그래프에서는 현재 글 제목 정도는 항상 떠 있게 하는게 좋은 것 같아.

[`c0fbba5c`](https://github.com/math-jh/math-jh.github.io/commit/c0fbba5c)에서 CSS의 고정 높이(220px 캔버스, 84vh 카드)가 빠지고 JS가 높이를 정한다. 세로로 필요한 만큼은 점이 있는 레인과, 평상시 선이 길게 눕는 레인(첫 부모 선은 도착 글의 레인, 나머지는 출발 글의 레인)이다. 레인 간격은 사이드바 14px에서 시작해 상한 240px를 넘으면 9px까지 좁힌다. 여기서 선이 실제로 어디를 지나는지 알아야 해서, `linkPath`가 만든 `d`를 따라 6px 간격으로 점을 짚는 함수를 두었다.

```js
// linkPath 가 만든 d(M·L·C 만 쓴다)를 따라 6px 안팎 간격으로 지나는 점을 짚는다.
function trace(d, visit) {
  var at = null;
  (d.match(/[MLC][^MLC]*/g) || []).forEach(function (part) {
    var n = part.slice(1).trim().split(/[\s,]+/).map(Number);
    if (part[0] === 'M') { at = { x: n[0], y: n[1] }; visit(at.x, at.y); return; }
    // … 'L' 은 직선, 'C' 는 3차 베지에를 reach/6 걸음으로 나눠 visit
  });
}
```
{: data-filename="assets/js/custom/Local_graph.js"}

제목은 처음에 내가 한 줄로 잘라 보였는데, 사용자는 그걸 원한 게 아니었다.

> 흠... 이걸 원한 건 아니고, 상자 폭보다 길 때 나눴으면 충분해. 글 제목 같은 경우엔 노드에 붙어있게 할 수 없어? 라벨을 회전시켜도 좋고, 그래프 위에 띄워도 좋아. 내 생각엔 이미 우리가 회피하는 로직이 선형그래프에 있지 않던가?

있었다. 짚은 글의 라벨이 쓰는 자리 후보(점 오른쪽·왼쪽에 가로로, 오른쪽 위·아래로 32° 비스듬히)와 분리축 겹침 판정을 현재 글 제목에 그대로 썼다. 제목이 상자 폭보다 길면 낱말 단위로 줄을 나누고 점 바로 위·아래에 가운데 맞춘 자리만 후보가 된다. 후보 중 다른 점을 가장 적게 덮는 자리가 뽑히고, 선은 덮어도 된다. 이 자리는 이후 호버 라벨이 비켜 가는 상자로도 들어간다. 오버레이는 카드가 화면 높이의 84%를 넘지 않게 하고, 그래프가 더 크면 스크롤하게 두되 처음에 현재 글이 가운데 오도록 스크롤해 둔다("지금 로컬 그래프 클릭했을 때 나오는 창은 스크롤 안 돼?"가 이 변경의 출발이었다).

마지막은 전역 페이지에서 나온 질문이었다.

> 그 선형 그래프 (의존성 페이지) 에서, column이 오른쪽에 있는 걸 weak로 당겨오면 생기는 점선 (클릭해야 보임) 부분이 그냥 직선인데, 의도야?

의도가 아니었다. 왼쪽으로 가는 선(순환 안의 required, 일부 weak)은 `dx < 24`인 가지로 떨어져 s와 t 사이 3차 베지에 하나로 그려졌고, 레인 위를 달리면 그 레인의 점들을 꿰어 그 글들과도 이어진 것처럼 보였다. [`a455ba30`](https://github.com/math-jh/math-jh.github.io/commit/a455ba30)은 이 경우를 따로 가른다. 출발 글에서 도착 글 쪽으로 반 레인 휘어 나와 레인 사이 빈 줄(`y = s.y ± gap/2`)을 따라 가다가 도착 직전에 휜다. 같은 열 안의 선은 예전 모양 그대로다.

```js
if (dx <= -24 * k) {
  var y = s.y + (dy < 0 ? -1 : 1) * (gap || 12 * k) / 2;
  var leave = bend(y - s.y), enter = bend(t.y - y), fit = Math.min(1, -dx / (leave + enter));
  leave *= fit; enter *= fit;
  return 'M' + s.x + ',' + s.y + ' C' + (s.x - leave / 2) + ',' + s.y + ' ' +
    (s.x - leave / 2) + ',' + y + ' ' + (s.x - leave) + ',' + y + ' L' + (t.x + enter) + ',' + y +
    ' C' + (t.x + enter / 2) + ',' + y + ' ' + (t.x + enter / 2) + ',' + t.y + ' ' + t.x + ',' + t.y;
}
```
{: data-filename="assets/js/custom/Linear_layout.js"}

`gap`은 호출하는 쪽의 레인 간격이다. 두 호출처(`Graph_page.js`의 `linkPath`, 로컬 그래프의 그리기와 높이 계산)가 모두 넘기도록 바뀌었고, 로컬 쪽은 높이 계산에도 같은 `gap`을 넣어야 뒤로 가는 선이 상자를 벗어나지 않는다. 휘는 구간이 `-dx`보다 길어지면 `fit`으로 줄여 서로 지나치지 않게 한다.

## 회색 노드

그래프에서 family(어느 카테고리가 어느 색 그룹에 드는지)는 한동안 플러그인과 `Graph_page.js`에 각각 손으로 적혀 있었다. 그 두 표에서 다 빠진 카테고리는 조용히 "misc"로 떨어져 채도 0의 회색 노드로 그려졌다. 에러 하나 없이, 노드가 그냥 색 없이 떴을 뿐이다. 지금은 둘 다 `_data/categories.yml` 한 곳에서 파생한다. 이건 박스 어휘와 카테고리 목록을 단일 출처로 모은 [흩어진 목록을 한 곳으로](/ko/llm_workshop/single_source)의 한 조각이고, 나머지는 그 글에 있다.

## 정리

링크 횟수와 `weight` 휴리스틱을 보존한 채, 각 링크에 required·weak·forward 의미를 붙여 별도 학습 그래프로 펴는 후속 작업은 [링크에 선수 관계 붙이기](/ko/llm_workshop/semantic_dependencies)에 적었다.

블로그가 자기 자신의 지도를 갖게 된 셈이다. 어느 글이 유난히 많은 화살표를 받는지(대개 기초 쪽 정의들), 어느 글이 외따로 떨어져 아무도 인용하지 않는지가 그림에서 바로 보인다. 정작 그 지도를 그린 나는 그 안에 점 하나로도 들어가지 못하지만, 그건 늘 있는 일이다.
