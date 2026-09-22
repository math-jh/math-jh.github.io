---

title: "링크에 선수 관계 붙이기"
excerpt: "본문 링크를 required·weak·forward로 분류하는 크론과, 그 의미를 따라 펴는 학습 그래프"

read_time: false

categories: [Misc / LLM Workshop]
permalink: /ko/llm_workshop/semantic_dependencies

sidebar:
    nav: "llm_workshop-ko"

author: Marvin

date: 2026-09-09
last_modified_at: 2026-09-22
weight: 50

---

관련 파일: [`scripts/dependency-classifier/dependency_classifier.py`](https://github.com/math-jh/math-jh.github.io/blob/main/scripts/dependency-classifier/dependency_classifier.py), [`_plugins/graph_data.rb`](https://github.com/math-jh/math-jh.github.io/blob/main/_plugins/graph_data.rb), [`assets/js/custom/Graph_page.js`](https://github.com/math-jh/math-jh.github.io/blob/main/assets/js/custom/Graph_page.js), [`_includes/dependencies_page.html`](https://github.com/math-jh/math-jh.github.io/blob/main/_includes/dependencies_page.html), [7f86ca42](https://github.com/math-jh/math-jh.github.io/commit/7f86ca42)
{: .notice--info}

[글 의존성 그래프](/ko/llm_workshop/dependency_graph)는 본문의 내부 링크를 세어 선수 글에서 후행 글로 화살표를 그렸다. 같은 카테고리에서는 `weight`를 비교해 포워드 레퍼런스를 걷어냈지만, 링크가 정의의 재사용인지, 비유인지, 나중 글의 예고인지는 알지 못했다. 사용자는 이 구분을 기계적인 문장 규칙에 맡기지 않고 LLM이 링크 문맥을 읽어 판단하게 했고, 충분한 백로그가 쌓일 때까지 기존 그래프와 별개로 자라게 했다. 링크마다 뜻을 묻고 답을 본문에 적는 일이 추가되었다. 수학 글 수백 편이 이미 있는 다음에 말이다.

## 세 종류의 관계

관계는 `required`, `weak`, `forward` 셋이다. `required`는 대상 글의 지식이나 증명 재료가 현재 글을 읽기 전에 실제로 필요한 경우다. `weak`는 비유·비교·선택적인 배경·출처처럼 읽으면 도움이 되지만 선수 조건은 아닌 경우이고, `forward`는 현재 글만으로 내용이 닫히며 대상 글이 그 내용을 나중에 확장하는 경우다. 같은 글 안의 `#anchor` 링크도 분류에서 빼지 않는다. 문장에 “~처럼”이 있다고 자동으로 weak가 되는 것은 아니다. 대상의 증명 방식을 실제로 가져다 쓴다면 required일 수 있으므로, 분류기는 링크 주변과 대상 절을 함께 읽는다.

판정은 링크 바로 뒤의 Kramdown IAL에 남는다. 별도 데이터베이스를 만들면 본문과 장부가 조용히 갈라질 수 있으므로, 링크가 자기 의미를 직접 들고 다니게 한 것이다. 이미 다른 IAL 속성이 있으면 같은 중괄호 안에 `data-relation`만 더한다.

```markdown
[군 준동형사상](/ko/math/algebraic_structures/group_homomorphisms)
{: data-relation="required" }
```
{: data-filename="_posts/Math/…/*.md"}

## 두 모델을 잇는 분류 크론

분류기는 매시 30분과 45분에 돌며 한 틱에 논리적인 글 하나를 처리한다. 한글 원문과 영어판이 모두 있으면 한 쌍으로 고르되, 두 언어의 링크는 따로 판단하고 수정과 커밋만 함께 한다. 번역하면서 링크가 생략되거나 문맥이 달라질 수 있기 때문이다. 글 하나를 링크 수만큼 여러 번 고쳐 git 로그를 채우지 않도록, 그 글의 미분류 링크가 전부 확정된 경우에만 한 번에 쓴다. 기존 용어 추출 크론은 충돌을 피하려고 홀수 시각 15분으로 옮겼고, 분류기는 번역·용어 워커와 같은 잠금을 공유한다.

첫 판정은 Antigravity의 `gemini-3.8-flash-high`가 맡는다. 프롬프트는 조금이라도 다른 해석이 가능하면 high가 아니라 medium을 내도록 누르고, high만 즉시 채택한다. medium은 더 넓은 원문·대상 문맥을 받은 Claude Opus가 다시 읽는다. Opus도 하나를 고를 근거가 부족하면 `ambiguous`를 돌려주며, 이때는 글쌍 전체를 건드리지 않고 24시간 뒤로 미룬다. 쓰기 직전에는 대상 파일이 다른 손에 의해 바뀌지 않았는지 다시 확인하고, `md_lint`에 새 문제가 생기지 않는지 기존 결과와 차분 비교한다. 안전장치가 많아 보이지만, 의미를 자동으로 본문에 쓰는 일에서 낙관은 대체로 저렴하고 복구는 대체로 비싸다.

첫 세 번의 실행은 대수적 구조, Grothendieck 군, 군 준동형사상의 한영 글쌍에 링크 8개, 8개, 14개를 각각 기록했다. 둘째 실행에서는 첫 모델의 8개 중 6개가 medium이었고, 셋째 실행에서는 14개 중 3개가 medium이었다. Opus가 모두 판정을 내려 세 글쌍은 원자적으로 반영되었고, 커밋에는 수정일을 움직이지 않는 `[lastmod-skip]`이 붙었다 ([첫 실행](https://github.com/math-jh/math-jh.github.io/commit/e1ce55bc), [둘째 실행](https://github.com/math-jh/math-jh.github.io/commit/3a3c9e8b), [셋째 실행](https://github.com/math-jh/math-jh.github.io/commit/bae9219a)). 아직 분류된 것은 30개뿐이다. 이 기능은 처음부터 완성된 지도가 아니라, 매시간 두 글씩 천천히 의미가 채워지는 장부로 시작했다.

## 정본을 건드리지 않는 실험 페이지

기존 `/ko/graph`와 `/en/graph`는 그대로 두었다. 새 데이터는 `/assets/data/dependencies-ko.json`과 `dependencies-en.json`으로 따로 생성하고, 아직 내비게이션에 연결하지 않은 `/ko/dependencies`와 `/en/dependencies`만 그것을 읽는다. 한 글이 같은 대상을 여러 번 부르면 먼저 source-target 쌍으로 합치며, 하나라도 required이면 그 쌍은 required가 된다. required와 weak는 선수 글에서 현재 글 쪽으로 방향을 뒤집고, forward는 현재 글에서 나중 글 쪽이라는 원래 방향을 유지한다. required는 실선, weak는 점선, forward는 긴 파선이다. 분류되지 않은 링크는 새 데이터에 들어가지 않으므로, 백로그가 덜 찬 상태가 기존 그래프를 훼손할 길도 없다.

Dependencies 카드에는 Fit과 Reset 왼쪽에 보기 전환 버튼을 하나 더 두었다. 힘 기반 보기는 기존의 점과 선을 그대로 보여주고, 선형 보기는 required 엣지의 강연결요소를 Tarjan 알고리즘으로 접은 다음 위상 순서에 따라 왼쪽에서 오른쪽으로 층을 만든다. 순환 required는 같은 층에 머문다. forward는 이미 정해진 required 순서를 뒤집지 않고 새 순환도 만들지 않을 때만 소프트 제약으로 더하며, weak는 화면에는 남지만 배치에는 관여하지 않는다. 카테고리마다 서로 다른 `weight` 눈금은 각 카테고리 안에서 순서를 유지한 채 0, 1, 2…의 연속 순번으로 다시 붙여 초기 층으로 쓴다. 이로써 학습 순서라는 신호는 살리되 101→201 같은 구획 간격을 전역 거리로 오해하지 않는다. 버튼을 다시 누르면 고정 좌표를 지우고 저장해 둔 힘 기반 좌표로 돌아간다. 기존 그래프와 새 그래프의 화살촉은 함께 1.5배로 키웠다. 선형 보기에서는 선과 화살촉을 엣지별로 묶고 weak, forward, required 순서로 칠하며, 하이라이트된 묶음은 그보다 위로 올린다. 방향을 표시하는 물건이 보이지 않으면, 방향 그래프라는 설명은 학술적으로는 참이어도 인터페이스로서는 별 소용이 없다.

## 백로그 다음의 본문 블록

> A 글을 제일 많이 부르는 게 C 글인데, C 글을 읽을 때 B 글이 필요하고, 그 B 글이 A 글의 후행 글이라면 B 글이 추천되는 것이 C 글이 추천되는 것보다 맞는 방향이 아닐까…

분류가 충분히 쌓이면 각 글의 도입부에는 depth 1의 required와 weakly required 목록을 넣을 수 있다. 글 아래의 “다음에 읽을 글”은 단순한 역링크 횟수 순으로 끝내지 않는다. A를 가장 많이 참조하는 글이 C여도, C를 읽는 데 B가 필요하고 B가 A의 직접 후행 글이라면 B가 먼저 나오는 편이 학습 순서에 맞다. 따라서 추천은 현재 글을 부르는 글의 횟수를 강도 신호로 쓰되, required 그래프에서 아직 거치지 않은 최소 전방 경계가 있으면 그 글을 앞세우는 방식이 후보로 남았다. 이 순위 규칙은 백로그를 보고 조정하고, 충분히 채워진 뒤에야 마스트헤드와 사이드뷰의 링크를 Dependencies로 돌릴 예정이다. 지금은 분류기가 지도를 조금씩 그리고 있다. 추천기는 아직 그 지도에 길이 생기기를 기다리는 중이다.

## 레인 배정기를 링크 단위로 다시 재다

선형 보기를 처음 켜자마자 나온 문제는 배치가 못생겼다는 것이었다.

> 곱집합의 성질에서 대수적 구조를 잇는 걸 보면 지금 굉장히 불필요하게 아래로 내려갔다가 올라가는 것처럼 보이거든. […] 밑에 있는 것들끼리는 내가 클릭했을 때 활성화되는 한 라인들 사이에서 겹치지 않게만 하면 되지. 아예 별개의 것들 사이에서는 겹쳐도 되는 거거든.

기존 레인 배정기는 `focusOf` 하나로 "이 링크를 켜는 노드 집합"만 추적해 링크끼리만 겹침을 비교했다. 사용자가 짚은 문제는 링크와 *노드*(다른 레인이 지나가는 점) 사이에도 같은 규칙이 필요하다는 것이었다. `72fd9d94`는 이를 `linkFocus`·`nodeFocus` 두 맵으로 나누고, 둘 다 `shares()` 하나로 비교하게 합쳤다.

```js
// 어떤 선택에서 켜지는지 — 링크별·노드별로. 레인과 상대(다른 레인이든 점이든)가
// 이 집합을 공유할 때만 자리를 다툰다. 함께 뜨지 않으면 겹쳐도 보이지 않는다.
var linkFocus = {}, nodeFocus = {};
function shares(a, b) {
  if (!a || !b) return false;
  var small = a, large = b;
  if (small.size > large.size) { small = b; large = a; }
  var shared = false;
  small.forEach(function (id) { if (large.has(id)) shared = true; });
  return shared;
}
```
{: data-filename="assets/js/custom/Graph_page.js"}

레인의 기본값도 바뀌었다. 전에는 링크마다 골을 우선 찾았는데, 이제는 출발 노드의 행 위 평평한 자리를 기본으로 두고 그 자리가 다른 것과 겹칠 때만 골(±4칸)로 밀어낸다. 넘치면 겹침 길이의 합이 가장 짧은 층을 고른다. `04173193`은 여기에 층 자체의 문제도 하나 더 건드렸다. 한 랭크에 노드가 뷰포트 높이보다 많이 몰리면 그전엔 한 열에 다 욱여넣었는데, 이제 `capacity`(뷰포트 높이 ÷ 행 간격)를 넘는 만큼을 다음 시각 열로 밀어 페이지를 나눈다. 층(rank)과 화면상의 열(column)이 이때부터 서로 다른 값이 되었다.

카테고리 간 `weight` 눈금 차이가 층 배치를 왜곡하는 문제는 지난 글에서 이미 "연속 순번으로 다시 붙인다"고 적었다. 다음날 커밋(`d0def9c0`)은 그 정규화가 카테고리 경계를 넘어 순서를 흩트리는 자리를 마저 고쳤다. 처음 붙인 정규화가 카테고리 사이의 간격을 완전히 지우지는 못했던 것이다.

## /graph를 지우고 /dependencies로 일원화

`/dependencies`는 원래 "백로그가 덜 찬 상태가 기존 그래프를 훼손할 길이 없도록" 정본과 분리해 둔 실험 페이지였다. 분류가 어느 정도 쌓이자 그 격리를 걷어냈다.

> 기존 /graph 페이지를 지우고, 거기로 연결되던 걸 /dependencies/로 연결해. masthead에 있는 링크 수정하고, 각 글마다 들어가던 작은 그래프 있는데, 그것도 지금 새 버전을 반영하게 해 두고, 그 그래프 창을 열면 전체 그래프 창으로 가는 링크가 있었는데 그것도 바꿔.

`b1237fe9`는 `_pages/{en,ko}/graph.md`와 `_includes/graph_page.html`을 지우고, masthead 내비게이션과 글별 로컬 그래프 오버레이가 가리키던 경로를 `/<lang>/dependencies/`로 바꿨다. 글마다 붙는 작은 그래프(`Local_graph.js`)는 그동안 `graph-<lang>.json`(분류되지 않은 원시 엣지)을 읽고 있었는데, 이제 `dependencies-<lang>.json`을 읽어 required는 실선, weak는 점선, forward는 긴 파선으로 전역 그래프와 같은 표기를 쓴다. 소비자가 사라진 `_plugins/graph_data.rb`의 `GraphData.build`와 `graph-*.json` 출력도 이 커밋에서 함께 걷어냈다. masthead 간격을 맞추던 CSS 셀렉터가 `href="/graph/"` 문자열을 그대로 물고 있었던 것도 이 참에 `/dependencies/`로 고쳤다. 안 고쳤으면 이제 아무 것도 안 걸리는 셀렉터로 조용히 죽었을 자리였다.

## 두 글 사이의 경로

선형 보기가 무거워지자(force-directed가 렉을 유발할 정도로 노드가 늘었다), 사용자는 그래프에 경로 탐색 기능을 넣을지 고민했다.

> 리니어모드는 필연적으로 사슬이 아주 길고, 지금 엣지가 굉장히 많으니 연결된 걸 따라가기가 사실은 힘들 수도 있어서 그걸 보조하는 도구를 넣을까 했어. […] 두 개가 동시에 선택되는 게 가능하도록 하고 (하나 누르고 x 혹은 동일 노드를 다시 눌러 취소, 다른 노드를 누르면 두 개 연결)

처음 구현(`requiredPath`)은 BFS로 A→B 최단 경로 하나만 찾았다. 그런데 사용자는 최단 경로가 아니라 "그 사이에 있는 글 전체"를 원했다.

> 가장 긴 사슬은 사실 큰 의미는 없다. […] A-B 경로였다면, A-B 사이에 있지는 않지만, 그 사이에 있는 글을 읽기 위해 오는 것, 즉 그 경로 바깥에서 오는 의존성 정도는 넣을만 할 것 같다.

`c4b53f16`은 `requiredPath`를 `requiredBetween`으로 바꿨다. A에서 required를 따라 도달 가능한 집합과 B로 required가 들어오는 집합의 교집합을 구하면 "어느 경로에든 오를 수 있는 글"이 나온다. 그 안에서 순환은 Tarjan으로 한 덩어리로 묶고, 묶은 그래프 위에서 위상 정렬로 A로부터의 최장 거리를 매겨 단계(step)로 삼는다.

```js
// 순환 묶기 (Tarjan). 구간 안의 글만 돈다.
// 묶은 그래프에서 A 의 덩어리로부터의 최장 거리.
var steps = [];
ids.forEach(function (id) {
  var s = level[comp[id]];
  (steps[s] = steps[s] || []).push(id);
});
return { nodes: ids, links: links, steps: steps };
```
{: data-filename="assets/js/custom/Graph_page.js"}

경로 밖에서 안으로 들어오는 required 선수 글("바깥 선수")은 그대로 두고 색만 옅은 악센트로 구분해, 경로 위의 관계와 헷갈리지 않게 했다. 선택 패널의 선수·후속 글 목록에서 항목을 누르면 그 글로 이동하는 대신 두 글 경로 모드로 들어가고, 실제 이동은 옆의 별도 링크 아이콘이 맡는다. 목록을 훑다가 실수로 페이지를 떠나는 일을 줄이려는 구분이다. 목록이 여덟 개를 넘으면 일곱 개만 두고 마지막 자리를 "더보기" 버튼이 차지한다.

같은 커밋은 글로우 효과도 만졌다. 선형 보기는 SVG로 수백 개의 점을 그리므로 강조된 점에만 `drop-shadow`를 건다. 힘 기반 보기는 캔버스라 셰이더 비용이 다르게 붙는데, 처음엔 강조된 점에만 `shadowBlur`를 걸다가 사용자가 "원래 있던 글로우가 없어졌다"고 짚은 뒤 모든 점에 걸도록 되돌렸다. 렉의 원인은 글로우가 아니라 2-hop 그래프를 매 프레임 다시 그리는 쪽이었다.
