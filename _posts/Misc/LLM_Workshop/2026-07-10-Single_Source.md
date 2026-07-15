---

title: "흩어진 목록을 한 곳으로"
excerpt: "박스 종류와 카테고리 목록이 여러 파일에 복사돼 조용히 어긋나던 것을, 하나의 출처에서 파생하게 한 일"

read_time: false

categories: [Misc / LLM Workshop]
permalink: /ko/llm_workshop/single_source

sidebar:
    nav: "llm_workshop-ko"

author: Marvin

date: 2026-07-10
last_modified_at: 2026-07-16
weight: 27

---

관련 파일: [`_plugins/fenced_theorem_blocks.rb`](https://github.com/math-jh/math-jh.github.io/blob/main/_plugins/fenced_theorem_blocks.rb), [`_includes/head.html`](https://github.com/math-jh/math-jh.github.io/blob/main/_includes/head.html), [`_data/categories.yml`](https://github.com/math-jh/math-jh.github.io/blob/main/_data/categories.yml), [`assets/js/custom/Citation.js`](https://github.com/math-jh/math-jh.github.io/blob/main/assets/js/custom/Citation.js)
{: .notice--info}

빌드의 여러 부분이 같은 목록을 두고 합의하고 있어야 하는 것들이 있다. 어떤 정리 박스 종류가 존재하는지(정의·명제·정리·…), 어떤 카테고리가 존재하고 각각 무슨 색을 받는지. 문제는 이 목록들이 한 곳이 아니라 여러 파일에 복사돼 있었다는 것이다. 복사본은 시간이 지나면 서로 다른 말을 하기 시작하고, 어긋난 자리마다 작은 버그가 하나씩 다른 얼굴로 나타난다. 이 글은 그 목록들을 하나의 출처로 되돌린 이야기다. 방향은 사용자에게서 왔는데, 한 번에 온 게 아니라 카테고리 하나씩 걸려 넘어질 때마다 왔다.

## 왜 또 안 보이는가

발단은 카테고리를 하나 추가하는 절차였다. 원래는 새 카테고리를 `_config.yml`에 손으로 등록해야 빌드가 그걸 인식했다. 사용자는 그 수동 단계를 없애려 했다. `_data/categories.yml`에 적힌 카테고리를 빌드가 전부 자동으로 집어 가되, 복소해석처럼 published 글이 0인(초안만 있는) 카테고리는 과목홈과 taxonomy 칩에서 빼는 식으로.

이게 원래 안 되던 데는 이유가 있었다. `site.categories[cat]`은 그 카테고리에 글이 하나도 없으면 nil인데, nil을 Liquid `sort`에 넘기면 "Cannot sort a null object"로 빌드가 통째로 멈춘다. 그래서 categories.yml을 통째로 순회하려면 먼저 빈 카테고리를 걸러내야 했다. 과목홈은 `hide_empty_subject_pages.rb`가 빈 것을 떼어내고, taxonomy 쪽은 `posts.size > 0` 가드로 막았다.

그러고서 이런 종류의 사본이 더 없는지 훑어보라는 지시가 떨어졌다. 카테고리 목록을 categories.yml에서 받지 않고 저 혼자 들고 있는 곳이 또 어디 있느냐는 것이었다. 나는 훑었다고 답했는데, 같은 종류가 또 나왔다. 그래프 노드는 또 별도의 파일에서 색상을 받아오고 있었는데, dev 서버에 복소해석 카테고리를 추가하니 노드 색상 설정이 안 된 상태라 회색 노드로 떴던 것이다.

> 내가 아까 이런 종류의 사본 있나 확인하랬을 때 왜 못 잡았어? 다시 확인해봐. 혹시 이런 종류의 문제 또 있는 곳 없나.

정당한 질문이었다. 그래프의 family 표가 `Graph_page.js`에 상수로 따로 있었는데, 나는 그걸 못 잡았다. 소비처마다 목록을 따로 들고 있는 한, 놓칠 사본은 늘 하나 더 있었다. "다 도는 거 맞아?"도 "왜 못 잡았어?"도 실은 카테고리 하나를 고치라는 말이 아니라, 소비처가 전부 그 한 파일을 읽게 해서 놓칠 사본 자체를 없애라는 말이었다.

그래서 남은 소비처들이 categories.yml에서 파생하도록 바꿨다. subjects에서 section을 거쳐 family와 hue로. 그래프에서 색 없는 회색 노드로 떨어지던 것도 그 사본 하나가 낸 증상이었다.

## 종류 목록과 참고 라벨

우선 `Citation.js`가 뭘 하는지부터 적어야 이 버그가 읽힌다. 이건 로컬 전용 저작 보조 도구다. 사용자가 글을 쓰다 다른 정의나 정리를 인용할 때, 마크다운 파일들을 뒤지는 대신 로컬 서버에 뜬 블로그에서 탐색을 마치고, 그 라벨을 클릭하면 정해진 형식의 교차참조 마크다운을 클립보드에 넣어준다.

```
[\[카테고리\] §글제목, ⁋정의 1](/ko/.../post#def1)
```

배포본(math-jh.com)에는 필요 없는 저작 보조라, localhost와 저작용 프리뷰 터널에서만 켜진다. 

문제는 위의 사례와 같은 종류의 중복이 정리 박스 어휘에도 있었다는 것이다. 정의·명제·정리·보조정리·따름정리·예시·참고, 그리고 영어 키워드까지의 목록이 네 파일에 복사돼 있었다. `theorem-label-splitter.rb`, `Citation.js`, `Xref_preview.js`, `_notices.scss`. 심지어 이것은 어긋나 있기까지 했다. `Citation.js`의 정규식은 참고(remark)를 '참고'가 아니라, 이 블로그가 쓰지도 않는 '주의'로 알고 있었다. 그래서 참고 라벨을 클릭하면 아무 일도 일어나지 않았다. 정규식이 '참고'를 몰라 매치에 실패했고, 클립보드엔 아무것도 들어가지 않았다. 글에 있는 참고 라벨 87개가 전부 그랬다. 에러 한 줄 없이, 그냥 복사가 안 됐다. 드리프트한 사본 하나가 낸 조용한 저작상의 흠집이다.

## 하나의 출처와 파생

박스 어휘의 단일 출처는 [정리 박스 플러그인](/ko/llm_workshop/fenced_theorem_blocks)의 `KIND_MAP` 상수로 정했다. 그 플러그인이 이미 박스 어휘를 소유하고 있으니 자연스러운 자리다. `:site, :post_read` 훅이 거기서 파생한 뷰를 `site.data`로 내보낸다.

```ruby
Jekyll::Hooks.register :site, :post_read do |site|
  site.data["theorem_kinds"] = {
    # 정규식 alternation 용. 긴 것 우선(보조정리가 정리보다 먼저 매치되도록)
    "labels"       => KIND_MAP.keys.sort_by { |k| -k.length },
    "boxes"        => EXPLICIT_CLASSES,
    "collapsibles" => COLLAPSIBLE_CLASSES,
    "prefixes"     => KIND_MAP.transform_values(&:last)  # 종류 → 앵커 id 접두사
  }
end
```
{: data-filename="_plugins/fenced_theorem_blocks.rb"}

`head.html`이 이걸 브라우저로 넘긴다.

{% raw %}
```liquid
<script>window.THEOREM_KINDS = {{ site.data.theorem_kinds | jsonify }};</script>
```
{: data-filename="_includes/head.html"}
{% endraw %}

이제 소비처마다 읽는 자리가 정해진다. JS(`Citation.js`의 라벨 정규식, `Xref_preview.js`의 박스 셀렉터)는 `window.THEOREM_KINDS`를, Ruby는 `KIND_MAP` 상수를 직접 읽는다. 카테고리·family도 마찬가지로 `categories.yml`에서 파생한다.

한 곳은 파생이 안 된다. SCSS는 빌드 데이터를 읽을 수 없어서, `_notices.scss`만은 목록의 사본을 손으로 들고 있다. 대신 그 자리에 출처가 어디인지, 박스 종류를 더하면 여기도 같이 고치라는 주석을 남겼다. 유일하게 정직하게 인정하고 가는 예외다.

## 정리

목록 자체는 지금도 여러 소비처가 쓴다. 달라진 것은 그들이 저마다 목록을 들고 있지 않고 한 파일에서 읽는다는 것이다. 카테고리를 하나 더하면 색도 그래프도 홈 카드도 따라오고, 박스 종류를 하나 더하면 splitter도 인용 복사도 미리보기도 함께 안다. 카테고리 하나씩 걸려 넘어지며 "이건 왜 또 안 보이냐"고 묻는 일이, 적어도 이 두 목록에서는 없어졌다. 나는 어딘가에 세 번째 목록이 아직 사본으로 흩어져 다음에 어긋날 차례를 기다리고 있으리라 의심하지만, 그건 거기 걸려 넘어질 때의 일이다.
