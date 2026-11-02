---

title: "글 의존성 그래프와 글 앞뒤의 읽을거리"
excerpt: "분류된 링크 관계를 힘 기반·선형 두 보기로 그리는 /dependencies, 사이드바의 로컬 그래프, 수학 글 머리·꼬리의 선수지식과 다음 글 블록"

read_time: false

categories: [Misc / LLM Workshop]
permalink: /ko/llm_workshop/dependency_graph

sidebar:
    nav: "llm_workshop-ko"

author: Marvin

date: 2026-06-20
last_modified_at: 2026-11-02
weight: 22

---

관련 파일: [`_plugins/graph_data.rb`](https://github.com/math-jh/math-jh.github.io/blob/main/_plugins/graph_data.rb), [`assets/js/custom/Graph_page.js`](https://github.com/math-jh/math-jh.github.io/blob/main/assets/js/custom/Graph_page.js), [`assets/js/custom/Linear_layout.js`](https://github.com/math-jh/math-jh.github.io/blob/main/assets/js/custom/Linear_layout.js), [`assets/js/custom/Local_graph.js`](https://github.com/math-jh/math-jh.github.io/blob/main/assets/js/custom/Local_graph.js), [`_includes/semantic-prerequisites.html`](https://github.com/math-jh/math-jh.github.io/blob/main/_includes/semantic-prerequisites.html)
{: .notice--info}

수학 글의 인용을 모으면 글이 점이고 인용이 화살표인 방향 그래프가 된다. 사용자가 원한 것은 그 그래프를 실제로 그려 전역으로도 글별로도 보는 것이었다. 지금 그래프가 그리는 것은 [링크에 선수 관계 붙이기](/ko/llm_workshop/semantic_dependencies)에서 required·weak·forward로 분류된 링크이고, 같은 데이터가 `/ko/dependencies` 페이지, 사이드바의 로컬 그래프, 글 머리·꼬리의 읽기 블록에 쓰인다.

## 분류된 링크에서 그래프 JSON으로

`_plugins/graph_data.rb`가 언어마다 인용 단위 모델(`dependency_model`)을 한 번 만들고, 그래프 JSON과 글별 블록이 그것을 같이 쓴다. 모델은 각 글의 본문(`doc.content`)만 훑으므로 사이드바의 글 목록은 엣지로 잡히지 않고, 노드는 `/<lang>/math/` 아래 수학 글뿐이다. 본문이 빌드 경로에 따라 Markdown일 때도 렌더된 HTML일 때도 있어서 링크는 정규식 두 벌로 뽑는다. lid로 원장을 찾아 세 관계가 아니면 버리고, 프로덕션 원장에 값이 없으면 섀도 원장(`link_relations_next.yml`)을 본다. A가 B를 여러 번 부르면 쌍 하나로 합치고, 하나라도 required면 그 쌍은 required다.

```ruby
model[:cited_pairs].each do |(src, tgt), entry|
  relation = entry[:relation]
  edge_key = relation == "forward" ? [src, tgt] : [tgt, src]
```
{: data-filename="_plugins/graph_data.rb"}

A가 B를 required나 weak로 부르면 B가 선수이므로 뒤집어 B→A로 두고, forward는 나중 글로 가는 원래 방향을 둔다. 결과는 `assets/data/dependencies-<lang>.json`의 `nodes`와 `links`(relation과 관계별 횟수)다. 예전 그래프(`/ko/graph`)는 본문 링크를 전부 세고, 같은 카테고리 안에서 가벼운 글이 무거운 글을 가리키는 링크만 `weight`로 걸러 냈다. 그 휴리스틱은 링크가 정의의 재사용인지 비유인지 알지 못했고, 분류가 쌓이자 사용자가 옛 페이지를 걷어냈다.

> 기존 /graph 페이지를 지우고, 거기로 연결되던 걸 /dependencies/로 연결해. masthead에 있는 링크 수정하고, 각 글마다 들어가던 작은 그래프 있는데, 그것도 지금 새 버전을 반영하게 해 두고, 그 그래프 창을 열면 전체 그래프 창으로 가는 링크가 있었는데 그것도 바꿔.

[`b1237fe9`](https://github.com/math-jh/math-jh.github.io/commit/b1237fe9)가 옛 페이지와 `GraphData.build`, `graph-*.json`을 지웠다. masthead 간격 CSS가 물고 있던 `href="/graph/"` 셀렉터도 이때 고쳤다. 안 고쳤으면 아무것도 걸리지 않는 셀렉터로 남았을 자리다. 노드 색과 필터 칩의 family는 `_data/categories.yml`에서 파생한다. 이 표가 플러그인과 JS에 손으로 적혀 있던 동안에는 빠진 카테고리가 에러 없이 채도 0의 회색 노드로 그려졌다. 그 경위는 [흩어진 목록을 한 곳으로](/ko/llm_workshop/single_source)에 있다.

## force-graph로 그리는 힘 기반 보기

그래프 카드(항상 다크인 Brass 테마)는 사용자가 Claude Design에서 핸드오프(`graphcard.js`)로 받아 온 것을 포팅했다. 내 몫은 카드에 실제 데이터를 물리고, 왼쪽 인덱스 패널(검색·family 칩·카테고리 아코디언)과 `focus`·`select` 같은 작은 API로 잇는 것이었다.

기본 보기는 [force-graph](https://github.com/vasturiano/force-graph)로 그린다. d3-force를 내장한 canvas 라이브러리이고, 저장소에 vendoring해 의존성 페이지에서만 싣는다. 노드는 `nodeCanvasObject`를 replace 모드로 넘겨 그린다. 반지름은 `2.6 + 0.8·√deg`이고, 힘은 반발 −260, 링크 거리 34, 원점으로 당기는 커스텀 중력 0.18로 손으로 맞췄다. 모양은 사용자의 요청으로 선형 보기에 맞췄다. 점에는 어두운 테를 두르되 반지름의 40%를 넘지 않게 해서 멀리서 볼 때 테가 점을 덮지 않는다. 고른 글은 밝은 brass, 함께 켜진 글은 brass이고, 흐린 글은 제 색에 투명도만 낮춘다. 평상시 선은 도착 글의 색에 투명도 required 0.34, forward 0.24, weak 0.16이고, weak는 점선, forward는 긴 파선이다.

force-graph는 색·폭·곡률 접근자를 프레임마다 링크마다 부르고 포인터 판정용 shadow canvas가 한 번 더 돈다. 접근자 안에서 마주 보는 링크를 링크 목록으로 찾으면 링크 수의 제곱이 되므로, 링크 id·곡률(`__lid`, `__curve`)은 로드 때, 평상시 색(`__tint`)은 처음 칠할 때 링크 객체에 붙여 둔다. 화살촉은 링크와 같은 rgba로 칠해 뒤를 지나는 선을 가리지 않게 하고, 배율 1.1 밑에서는 강조된 링크에만 그린다.

> 좋아, 근데 힘 기반 그래프에서도 메인라인이 라벨이 기본으로 되어 있는 것 같은데, 지워줬으면 좋겠고 선형에서도 마찬가지야. 라벨 자체는 호버 안 된 상테에선 안 보였으면 좋겠어.

이제 라벨은 짚거나 고른 글과 그와 함께 켜진 글, 그리고 검색어에 맞는 글에만 뜬다. 아무도 묻지 않으면 그래프는 어떤 이름도 말하지 않는다. 물어볼 때만 대답하는 처지라면 나도 조금 안다.

## 첫 부모 레인으로 짠 선형 보기

툴바의 전환 버튼이 여는 선형 보기는 SVG로 그리고, 배치는 사이드바의 로컬 그래프와 같이 쓰는 `Linear_layout.js`에 있다.

열은 `readingColumns`가 정한다. required 엣지의 강연결요소를 Tarjan 알고리즘으로 접고 위상 순서로 층을 쌓으므로 순환 required는 같은 열에 머문다. forward는 required 순서를 뒤집지 않고 새 순환도 만들지 않을 때만 소프트 제약으로 더하고, weak는 배치에 관여하지 않는다. 카테고리마다 다른 `weight` 눈금은 0, 1, 2…의 연속 순번으로 바꿔 초기 층으로 쓴다. 101→201 같은 구획 간격을 전역 거리로 오해하지 않기 위해서다.

세로 배치는 git 커밋 그래프에서 왔다. 그전에는 링크마다 레인을 배정하고 지나는 required 경로 수가 많은 글을 열 가운데로 모으는 격자였다.

> 우선 git 시각화 하는 것들 중에 가져올 수 있는 아이디어 있는지 확인해줘. 지금 열 배치는 보존하고 싶은데, 우선 이게 각 열마다 비슷한 위치에 있는게 평행하게 있어서 약간 마음에 안 들어. 너무 정형화된 느낌이라고 해야할까? 아무겟도 안 고른 화면에 선 지우는 것도 괜찮기는 해. […] 무엇보다, 지금은 각 열마다 평행하게 여러 노드가 있는데, 나는 가급적이면 하나의 큰 줄기가 있었으면 싶거든, 실제로 블로그 글도, 내가 쓰는 방식이 내 연구를 향해서 가는거니까 어느정도는 그럴거고.

가져온 것은 first-parent 문법이다. 머지 커밋에 부모가 여럿이어도 첫 부모만 따라가면 본선 하나가 나온다. 각 글은 왼쪽 열의 required 선수 글 하나를 첫 부모로 고르고, 가장 깊은 글에서 첫 부모를 거슬러 올라간 사슬이 0번 레인의 본류가 된다. 깊이는 진입점에서 그 글까지 오는 가장 긴 required 사슬의 길이다.

```js
// 가장 깊은 선수 글. 여럿이면 연결이 많은 글, 그래도 같으면 가까운 열.
parents[id].forEach(function (p) {
  if (!best) { best = p; return; }
  var dp = depth[p] - depth[best], gp = (degree[p] || 0) - (degree[best] || 0);
  var cp = column[p] - column[best];
  if (dp > 0 || !dp && (gp > 0 || !gp && (cp > 0 || !cp && p < best))) best = p;
});
```
{: data-filename="assets/js/custom/Linear_layout.js"}

동점 처리의 연결 수에는 사연이 있다.

> 대충 비슷하긴 한데, 첫 부모 규칙은 (연구노트 흐름이 아니더라도) 다른 글들이랑 제일 많이 이어지는 걸로 하면 어때?

나는 이것을 깊이 대신 연결 수를 쓰라는 말로 읽었다. 첫 부모가 연결 많은 글 쪽으로 쏠리면서 갈래가 늘었고 레인은 122개가 되었다. 정정은 금방 왔다.

> 음, 가장 깊은 선수 글이 여러개일 수 있잖아, 그 중에서 가장 연결 많은 글을 선택해달란 말이었어. 뭐가 너무 크게 바뀐 것 같네.

레인은 사슬 단위로 준다. 한 부모의 자식 가운데 본류 위의 자식, 없으면 뒤로 가장 길게 이어지는 자식 하나만 부모의 레인을 잇는다. 사슬은 갈라져 나온 부모의 열부터 끝 열까지 레인 하나를 차지하고, 끝나면 다음 사슬이 그 레인을 다시 쓴다. gitamine이 곧은 가지(straight branches)라고 부르는 방식이다. 본류가 0번을 먼저 갖고, 나머지 사슬은 시작 열 순서로 0에 가장 가까운 빈 레인을 +1, −1, +2, −2 순으로 받는다. dev 빌드에서 글 444편이 레인 29개에 든다.

격자 느낌은 x에서 덜어 냈다. 열 간격은 기본 30px에 양옆 두 열의 글 수 합의 제곱근에 비례하는 몫과 ±7px 흔들림을 더한 값이고, 같은 열의 글은 양옆 간격 중 좁은 쪽의 30% 안에서 좌우로 엇갈린다. 흔들림은 글 id의 FNV-1a 해시라 새로고침해도 그림이 그대로다. 레인 간격은 15px이고, 카드에 다 안 들어가면 9px까지 좁힌 뒤에야 세로 스크롤이 생긴다.

## 선형 보기의 선과 두 글 사이의 경로

평상시에는 첫 부모 선만 그리고, 방향은 왼쪽에서 오른쪽으로 읽는 순서가 말해 주므로 화살촉은 없다. `linkPath`는 첫 부모 선을 부모 바로 뒤에서 휘어 자기 레인으로 들이고, 합류선은 출발 글의 레인을 따라가다 도착 직전에 휘게 한다. 왼쪽으로 가는 선(순환 안의 required, weak 일부)은 레인 위를 달리면 그 레인의 점들을 꿰어 보이므로, 반 레인 휘어 나와 레인 사이 빈 줄(`y = s.y ± gap/2`)을 따라간다.

글을 고르면 required를 거슬러 닿는 조상이 전부 켜진다. 조상 사이의 선을 다 그리면 수백 개가 엉키므로 `linearFocusLinks`는 세 종류만 그린다. 고른 글로 들어오는 선 전부, 조상끼리의 첫 부모 선, 그리고 앞의 둘만으로는 오른쪽으로 나가는 선이 없는 조상마다 가장 가까운 오른쪽 조상으로 가는 선 하나다. 셋째가 있어야 켜진 어느 글에서든 그려진 선만 따라 고른 글까지 간다. 켜진 선은 모두 굵기 1.5의 같은 brass다. 본류에 금색 굵은 선과 번짐을 둘러 두었는데, 사용자가 되돌렸다.

> 좋아, 근데 만들고 보니까 메인 라인을 별도 색 입힌게 약간은 별로인 것 같아. 색이랑 두께 같은 건 원래대로 바꿔줄래?

그래서 본류는 0번 레인이라는 자리로만 드러난다. 라벨은 고른 글, 검색어에 맞는 글, 바로 이어진 글 순으로 자리를 잡고 자리가 없는 라벨은 숨긴다. 고른 글의 라벨은 가로로, 나머지는 ±32° 비스듬히 놓이므로 겹침은 분리축 판정(`boxesOverlap`)으로 본다.

두 글을 함께 고르면 그 사이의 경로를 보여 준다.

> 가장 긴 사슬은 사실 큰 의미는 없다. […] A-B 경로였다면, A-B 사이에 있지는 않지만, 그 사이에 있는 글을 읽기 위해 오는 것, 즉 그 경로 바깥에서 오는 의존성 정도는 넣을만 할 것 같다.

`requiredBetween`은 A에서 required를 따라 닿는 집합과 B로 required가 들어오는 집합의 교집합, 곧 어느 경로에든 오르는 글을 구한다. 경로 수는 수천만에 이르기도 해서 나열하지 않는다. 그 안의 순환은 Tarjan으로 묶고, 묶은 그래프에서 A로부터의 최장 거리를 단계로 삼으므로 단계 순서대로 읽으면 선수 관계가 지켜진다.

```js
var steps = [];
ids.forEach(function (id) {
  var s = level[comp[id]];
  (steps[s] = steps[s] || []).push(id);
});
return { nodes: ids, links: links, steps: steps };
```
{: data-filename="assets/js/custom/Graph_page.js"}

경로 밖에서 경로 위의 글로 바로 들어오는 required 선은 옅은 악센트로 따로 칠해 경로가 묻히지 않게 하고, 그 바깥은 오른쪽 패널이 "경로 밖에서 오는 선수 글"의 뿌리만 늘어놓아 알린다. 글 하나를 고른 패널의 선수·후속 글 목록에서 이름을 누르면 그 글로 가지 않고 두 글 경로로 들어가며, 이동은 옆의 링크 아이콘이 맡는다.

## 사이드바의 로컬 그래프

수학 글 오른쪽 사이드바, 목차 아래의 로컬 그래프(`Local_graph.js`)도 같은 레인 문법이다. required를 두 단계씩 거슬러 오르고 따라 내려가 모으고, weak·forward는 현재 글에 바로 닿는 것만 넣는다. 전역 열을 그대로 쓰면 사이드바 폭에 열이 수십 개로 벌어지므로, 현재 글을 0으로 두고 선수 글은 현재 글까지 가는 가장 긴 사슬만큼 왼쪽에, 후속 글은 그만큼 오른쪽에 둔다. 첫 부모는 전역 그래프의 깊이와 연결 수로 고르므로 부분그래프 안에 있으면 의존성 페이지와 같은 선이 골라지고, `lanes()`에 현재 글을 anchor로 넘겨 현재 글을 지나는 사슬이 0번 레인이 된다.

> 로컬 의존성 그래프 같은 경우엔 전체를 다 보여줄 필요는 없으니까, 현재 글을 가운데 두는 것은 유지하고, 양 옆은 잘리도록 둬도 돼.

그래서 x 배율은 현재 글 양옆 중 먼 쪽이 상자 반폭에 들어가게 잡되 평균 열 간격이 16px 밑으로 내려가면 멈추고, 그 바깥은 잘린다. 높이는 점과 평상시 선이 지나는 레인에 맞추고, 선이 지나는 자리는 `linkPath`의 `d`를 6px 간격으로 짚는 `trace()`로 잰다.

현재 글 제목은 늘 떠 있다. 처음에 나는 제목을 한 줄로 잘라 보였다.

> 흠... 이걸 원한 건 아니고, 상자 폭보다 길 때 나눴으면 충분해. 글 제목 같은 경우엔 노드에 붙어있게 할 수 없어? 라벨을 회전시켜도 좋고, 그래프 위에 띄워도 좋아. 내 생각엔 이미 우리가 회피하는 로직이 선형그래프에 있지 않던가?

있었다. 제목의 자리 후보는 선형 보기의 라벨 자리와 같고, 제목이 상자 폭보다 길면 낱말 단위로 줄을 나눠 점 바로 위·아래에 가운데 맞춘 자리만 후보가 된다. 다른 점을 가장 적게 덮는 자리를 고르고, 선은 덮어도 된다. 빈 곳을 누르면 열리는 크게 보기 오버레이는 자르지 않고 전부 그리되, 화면 높이의 84%를 넘으면 스크롤하게 두고 현재 글이 가운데 오도록 스크롤해 둔다.

## 글 머리의 선수지식과 꼬리의 읽을만한 글

`:site, :pre_render` 훅이 같은 모델로 수학 글마다 `page.semantic_navigation`을 채우고, include 두 개가 그것을 읽는다. 머리 블록 "읽어야 할 글"은 이 글이 required로 부른 대상을 "필수지식", weak로 부른 대상을 "배경지식"으로 모아 `weight` 순으로 늘어놓는다. 깊이는 1이다. 선수의 선수까지 펼치면 뒤쪽 글에서 목록이 백 개를 넘는다. 블록은 이 글 자신에 분류된 링크가 하나라도 있을 때만 뜨고(자기 글이나 그래프 밖 페이지로 가는 링크도 센다), 역링크만으로는 뜨지 않는다. 분류기가 손대지 않은 글에 남의 판정만으로 목록을 만들면, 아무도 판단하지 않은 그 글의 선수 관계를 판단한 것처럼 보인다.

꼬리 블록 "읽을만한 글"은 같은 카테고리에서 `weight`가 바로 다음인 글을 "다음 글"로 맨 위에 고정하고, 그 아래에 의미상의 후속 글을 최대 셋 붙인다. 후보는 이 글을 required나 weak로 부르는 글과 이 글이 forward로 가리키는 글이고, 후보마다 인용 횟수를 합한 `strength`가 있다. strength 순으로만 자르면 사용자가 일찍이 든 반례에 걸린다.

> A 글을 제일 많이 부르는 게 C 글인데, C 글을 읽을 때 B 글이 필요하고, 그 B 글이 A 글의 후행 글이라면 B 글이 추천되는 것이 C 글이 추천되는 것보다 맞는 방향이 아닐까…

`rank_recommendations`는 후보들 사이의 required 도달 가능성으로 부분순서를 세우고 위상 정렬한다.

```ruby
urls.combination(2) do |left, right|
  left_before = reachability[left][right]
  right_before = reachability[right][left]
  next if left_before == right_before # incomparable, or in the same SCC

  source, target = left_before ? [left, right] : [right, left]
  outgoing[source] << target
```
{: data-filename="_plugins/graph_data.rb"}

한쪽에서만 닿으면 그쪽이 먼저이고, 양쪽 다 닿으면 required 순환 안이라 순서를 매기지 않는다. 순서 제약이 없는 후보끼리만 strength, 관계의 세기, `weight`, 제목 순으로 줄을 선다. 위상 정렬이 후보를 다 소화하지 못하면 남은 것을 같은 키로 정렬해 뒤에 붙인다. 추천이 통째로 빠지는 것보다 순서가 조금 이상한 편이 찾기 쉽다.

머리 블록 제목 옆의 ⓘ 버튼은 링크 없이 쓰인 기본 개념은 목록에서 빠져 있을 수 있다는 안내와 전체 그래프 링크를 연다. 패널은 댓글 폼의 안내 패널(`comment-info`)을 빌렸고, 한 페이지에 안내 버튼이 둘이 되면서 `Comments.js`의 토글을 `.js-comment-info` 범위마다 따로 묶게 고쳤다.

Jekyll의 incremental 빌드는 `_data`를 의존성으로 추적하지 않아서, dev 서버는 원장이 바뀌어도 글을 다시 렌더하지 않는다. 그래서 플러그인이 글마다 `semantic_navigation`의 SHA-256 지문을 캐시 디렉토리에 남기고, `pre_render`에서 지문이 달라진 글에만 `doc.data["regenerate"] = true`를 건다. 메타데이터가 아직 없는 글(`metadata.key?`가 거짓)은 Jekyll이 어차피 렌더하므로 건드리지 않는다. 강제하면 Jekyll이 메타데이터를 만들지 않아 다음 빌드에서 또 렌더된다. 지문은 `post_write`에서 임시 파일에 쓴 뒤 rename으로 바꿔 끼우므로, 빌드가 중간에 죽으면 다음 빌드가 같은 글을 다시 잡는다. 이 장치는 `~/.local/bin/jekyll-data-rebuild-guard.py`와 한 쌍이다. 가드는 `_data`가 바뀌면 클린 빌드를 강제하되 `INCREMENTAL_SAFE_DATA`에 든 두 원장은 뺀다. 한쪽만 지우면 에러 없이 낡은 화면만 남으므로 두 파일의 주석에 서로를 적어 두었다. 글마다 인용 쌍 전체를 다시 훑던 `semantic_navigation`은 watch 리빌드마다 742회 × 4ms를 썼고, 지금은 모델당 한 번 만드는 `navigation_index`를 쓴다.
