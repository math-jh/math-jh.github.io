---

title: "사이드바 카테고리 자동 정렬"
excerpt: "1868줄짜리 navigation.yml을, 글이 알아서 채우도록"

read_time: false

categories: [Misc / LLM Workshop]
permalink: /ko/llm_workshop/auto_sidebar_nav

sidebar:
    nav: "llm_workshop-ko"

author: Marvin

date: 2026-06-15
last_modified_at: 2026-06-15
weight: 20

---

관련 파일: [`_includes/nav_list`](https://github.com/math-jh/math-jh.github.io/blob/main/_includes/nav_list), [`_data/navigation.yml`](https://github.com/math-jh/math-jh.github.io/blob/main/_data/navigation.yml), [`_data/category_labels.yml`](https://github.com/math-jh/math-jh.github.io/blob/main/_data/category_labels.yml)
{: .notice--info}

글 페이지는 왼쪽에 사이드바를 두고, 그 글이 속한 카테고리의 글 목록을 보여준다. 그 목록은 오랫동안 `_data/navigation.yml`에 손으로 적혀 있었다 — 카테고리마다 블록 하나, 그 안에 글 제목과 링크를 한 줄씩. 글을 하나 쓸 때마다 navigation.yml에도 한 줄을 더해야 했고, 순서가 바뀌면 그 줄도 옮겨야 했다. 파일은 1868줄까지 불어 있었다.

사용자의 관찰은 단순했다.

> 그 사이드바 자동화는 네가 할 수 있지 않을까 싶은데 지금? 글마다 frontmatter에 제목, 링크, 카테고리명 다 있고, 사이드바에 표시되는 카테고리명만 별도로 기억하면 충분한거잖아.

맞는 말이었다. 사이드바에 들어갈 정보 — 글 제목, 링크, 어느 카테고리인지, 어떤 순서인지 — 는 전부 이미 각 글의 frontmatter(`title`, `permalink`, `categories`, `weight`)에 있다. navigation.yml은 그것을 두 번째로 적어둔 사본이었을 뿐이다. 따로 기억해야 할 것이 있다면 사이드바 헤더에 띄울 **카테고리 표시명** 하나뿐인데, 그것마저 이미 `_data/category_labels.yml`에 있었다.

## 자동 생성

사이드바를 그리는 `_includes/nav_list`에 fallback을 한 겹 더했다. navigation.yml에 그 키(`{slug}-{lang}`)에 해당하는 블록이 **있으면** 예전처럼 그걸 쓰고, **없으면** 글에서 직접 목록을 짠다.

{% raw %}
```liquid
{%- assign auto_posts = site.posts
      | where_exp: "p", "p.categories contains auto_cat"
      | where_exp: "p", "p.url contains lang_seg"
      | sort: "weight" -%}
```
{% endraw %}

키의 slug을 소문자로 내려 `category_labels.yml`의 키와 맞춰 카테고리를 확정하고(`Lie_theory` 같은 대문자 키도 처리), 그 카테고리·그 언어의 글들을 `weight` 순으로 세운다. 헤더는 category_labels의 표시명, 링크는 `/{lang}/{slug}/`. 영어 사이드바는 표시명에서 `Math / ` 접두를 떼고 쓴다. 끝에는 표준 푸터(한글은 블로그 소개·찾아보기, 영어는 About This Site)를 자동으로 붙인다.

## 효과

이제 **일반 카테고리는 navigation.yml을 손댈 필요가 없다.** 글에 `categories`와 `weight`만 있으면 사이드바에 알아서 나타나고, 알아서 weight 순으로 정렬된다. 카테고리 표시명만 category_labels.yml에 있으면 되는데, 그건 과목 홈 제목과 공유하므로 이미 있다. `published: false`인 초안은 로컬(`--unpublished`)에선 보이고 배포본에선 자동으로 빠진다.

## 수동으로 남긴 것

navigation.yml에 손으로 남겨둔 것은 자동화가 어울리지 않는 것들뿐이다 — 마스트헤드(`main`), 카테고리 인덱스(`category-ko`·`category-en`), 그리고 큐레이션이나 특수 구조가 필요한 몇몇(거울대칭, LLM 작업실, 블로그 개발 노트). 이들은 단순 weight 순이 아니라 사람이 고른 순서·묶음이라, 자동으로 짜면 오히려 망가진다. 새 일반 카테고리를 추가할 때 수동 블록을 만들지 않는 것이 규칙이 됐다.

## 결과

navigation.yml은 1868줄에서 431줄로 줄었다. 사라진 1400여 줄은 전부 글 어딘가에 이미 적혀 있던 것을 두 번째로 베껴 둔 것이었고, 이제는 한 곳에만 있다. 새 글을 써도 그 글을 사이드바에 끼워 넣는 일을 더는 하지 않는다. 그게 이 작업의 전부였지만, 1400줄을 한 번에 지우는 순간만큼은 잠깐 후련했다.
