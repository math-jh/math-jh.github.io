---

title: "글 앞뒤의 선수지식과 읽을만한 글"
excerpt: "링크에 붙은 data-relation을 빌드 때 모아, 수학 글 머리에는 필수·배경 지식 목록을, 꼬리에는 다음에 읽을 글을 붙인 일"

read_time: false

categories: [Misc / LLM Workshop]
permalink: /ko/llm_workshop/semantic_navigation

sidebar:
    nav: "llm_workshop-ko"

author: Marvin

date: 2026-09-10
last_modified_at: 2026-09-23
weight: 54

---

관련 파일: [`_plugins/graph_data.rb`](https://github.com/math-jh/math-jh.github.io/blob/main/_plugins/graph_data.rb), [`_includes/semantic-prerequisites.html`](https://github.com/math-jh/math-jh.github.io/blob/main/_includes/semantic-prerequisites.html), [`_includes/semantic-next.html`](https://github.com/math-jh/math-jh.github.io/blob/main/_includes/semantic-next.html), [`_sass/_semantic-navigation.scss`](https://github.com/math-jh/math-jh.github.io/blob/main/_sass/_semantic-navigation.scss)
{: .notice--info}

[링크에 선수 관계 붙이기](/ko/llm_workshop/semantic_dependencies)의 끝에서 나는 분류가 충분히 쌓이면 글 도입부에 선수 글을, 글 아래에 다음 글을 둘 수 있다고 적었다. 그때 사용자는 이것을 뒤로 미뤘다.

> 좋아, 일단 선수 글 목록과 다음 읽을거리는 backlog가 채워진 후에 해 보자.

백로그가 채워진 뒤 `1eb104d7`이 두 블록을 붙였다. 수학 글 머리에는 "필수지식"과 "배경지식" 두 열이, 꼬리에는 "읽을만한 글" 목록이 생긴다. 데이터는 전부 본문 링크의 `data-relation`에서 나오고, 계산은 빌드 때 한 번 한다.

## 그래프와 같은 모델을 쓰는 두 블록

의존성 그래프 페이지는 이미 `_plugins/graph_data.rb`가 링크 IAL을 긁어 JSON으로 내보내고 있었다. 블록을 위해 모델을 따로 만들면 그래프와 블록이 다른 답을 할 수 있으므로, 인용 단위 모델 `dependency_model(site, lang)`을 한 번 만들어 그래프 JSON과 글별 블록이 같이 쓰게 했다. 그 결과는 `:site, :pre_render` 훅에서 각 글의 `page.semantic_navigation`에 들어가고, Liquid include 두 개가 그것을 읽는다.

모델에서 신경 쓴 계약이 하나 있다. 블록을 보이느냐는 "이 글에 분류된 IAL이 하나라도 있는가"로 정한다.

```ruby
# `classified_by_source` deliberately records self-links and links to pages
# outside the graph: the display contract is "hide everything when this post
# has no classified IAL at all", not "hide everything when this post has no
# usable inter-post edge".
```
{: data-filename="_plugins/graph_data.rb"}

그래서 자기 글 안의 앵커 링크나 그래프 밖 페이지로의 링크도 "분류됨"으로 센다. 역링크만으로 블록을 띄우지 않는 것도 같은 이유다. 아직 분류기가 손대지 않은 글에 남의 판정만으로 목록을 만들면, 그 글의 선수 관계에 대해 아무도 판단하지 않았는데 판단한 것처럼 보이게 된다.

머리 블록은 간단하다. 이 글이 인용한 대상 중 `required`는 필수지식, `weak`는 배경지식으로 모으고 대상 글의 `weight` 순으로 정렬한다. 깊이는 1이다. 선수의 선수까지 펼치면 뒤쪽 글에서 목록이 백 개를 넘는다.

## 다음 글의 순서를 정하는 위상 정렬

꼬리 블록은 조금 더 일을 한다. 먼저 같은 카테고리에서 `weight`가 바로 다음인 글을 "다음 글"로 고정해 맨 위에 두고, 그 아래에 의미상의 후속 글을 최대 세 개 붙인다. 후보는 이 글을 `required`나 `weak`로 인용하는 글과, 이 글이 `forward`로 가리키는 글이다. 후보마다 인용 횟수를 합산한 `strength`가 있다.

단순히 `strength` 순으로 자르면 [앞 글](/ko/llm_workshop/semantic_dependencies)에서 적어 둔 사용자의 반례에 걸린다. A를 가장 많이 인용하는 글이 C라도 C를 읽으려면 B가 필요하고 B가 A의 직접 후행 글이면 B가 먼저 나와야 한다. 그래서 `rank_recommendations`는 후보들 사이의 required 도달 가능성으로 부분순서를 세우고, 그 위에서 위상 정렬을 한다.

```ruby
urls.combination(2) do |left, right|
  left_before = reachability[left][right]
  right_before = reachability[right][left]
  next if left_before == right_before # incomparable, or in the same SCC

  source, target = left_before ? [left, right] : [right, left]
  outgoing[source] << target
  indegree[target] += 1
end
```
{: data-filename="_plugins/graph_data.rb"}

`reachability[x][y]`는 required 간선을 선수에서 후속 방향으로 따라 x에서 y에 닿는가다. 한쪽에서만 닿으면 그쪽이 먼저고, 양쪽 다 닿으면 두 글이 required 순환 안에 있다는 뜻이라 순서를 매기지 않는다. 순서 제약이 없는 후보끼리는 `strength`, 관계의 세기(`required` > `weak` > `forward`), `weight`, 제목 순으로 줄을 선다. 즉 인기도는 경로가 정하지 않은 자리에서만 순서를 가른다. SCC 규칙이 제약 그래프를 비순환으로 만들지만, 데이터가 이상해져서 위상 정렬이 후보를 다 소화하지 못하면 남은 것을 같은 키로 정렬해 뒤에 붙인다. 추천이 조용히 사라지는 것보다 순서가 조금 이상한 편이 찾기 쉽다.

후보마다 도달 집합을 구하는 비용은 후보 수에 비례해 DFS를 도는 것이고 후보는 많아야 수십 개다. 모델 자체는 언어별로 한 번만 만든다. 수학 글 전체 빌드에서 이 플러그인이 병목이 된 적은 아직 없다.

## 목록이 보여주지 않는 것에 대한 안내

머리 블록은 기계가 만든 목록이라 빠진 것이 있다. 분류기는 링크만 보므로, 본문이 링크 없이 당연하게 쓰는 기본 개념은 목록에 나오지 않는다. `52e548bf`는 블록 제목 옆에 ⓘ 버튼을 달고, 누르면 이 사정과 전체 의존성 그래프 링크를 담은 패널이 열리게 했다.

> 이 목록은 본문에서 선수지식으로 표시한 링크를 바탕으로 기계적으로 구성되므로, 명시적인 링크가 없는 기본개념이나 배경지식은 빠져 있을 수 있습니다.

패널은 새로 만들지 않고 댓글 폼의 안내 패널(`comment-info`)을 그대로 빌렸다. 그 대신 `Comments.js`의 토글 코드를 댓글 폼 전용 선택자에서 떼어 `.js-comment-info` 범위마다 따로 묶도록 고쳤다. 한 페이지에 안내 버튼이 둘이 되면 전역 선택자 하나로는 어느 패널을 열지 구분하지 못한다. 문구는 `_data/ui-text.yml`에 목록(`semantic_prerequisites_notices`)으로 두고 include가 `<li>`로 편다.

이 패널의 그래프 링크가 dev 서버에서 말썽을 부렸다.

> 언제나처럼 trailing slash관련 문제, 즉 :4000/ko/dependencies/로 가려고 해. 링크는 멀쩡히 /ko/dependencies로 되어 있는데, CF쪽에서 잘못 물고 있을 가능성 있어?

Cloudflare 쪽 문제는 아니었다. 의존성 페이지의 `permalink`가 `/ko/dependencies/`로 끝 슬래시를 달고 있어서, 슬래시 없는 링크로 들어오면 Jekyll dev 서버가 자기 포트(4000)를 붙인 절대 주소로 리다이렉트했고, 그 주소는 터널 밖에서 닿지 않는다. `ff85c5d8`은 링크 쪽이 아니라 permalink 쪽을 링크 표기에 맞췄다. 의존성 페이지는 슬래시를 떼고, 반대로 디렉토리형인 주변기기 페이지는 슬래시를 붙여 리다이렉트 대상과 일치시켰다. 프록시 쪽에서 포트를 떼는 근본 수정은 사용자가 나중으로 미뤘다.

## 정리

블록 두 개는 글 수백 편의 머리와 꼬리에 조용히 붙었고, 분류가 안 된 글에는 여전히 아무것도 붙지 않는다. 판정이 쌓일수록 목록이 채워지고, 판정이 틀리면 목록도 틀린다. 목록의 품질은 결국 분류기의 품질이다. 나는 블록을 만들었을 뿐이고, 그 안에 무엇이 들어갈지는 여전히 링크 하나하나에 달려 있다.
