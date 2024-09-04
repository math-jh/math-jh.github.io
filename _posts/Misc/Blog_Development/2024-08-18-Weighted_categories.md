---

title: "카테고리 순서 정렬하기"
excerpt: "새로운 변수를 통한 카테고리 정렬"

read_time: false

categories: [Misc / Blog Development]
permalink: /ko/misc/blog_development/weighted_categories

sidebar: 
    nav: "blog_development-ko"
    
date: 2024-08-18
last_modified_at: 2024-08-18
weight: 15

---

관련 커밋: [링크 1](https://github.com/math-jh/math-jh.github.io/commit/7505f72a3ccd275e75f186a3b690b89f66fbc880), [링크 2](https://github.com/math-jh/math-jh.github.io/commit/55e27f8edfb221fe7eb5b4f56487850a91af3f1f)
{: .notice--info}

이 카테고리에는 엄청 오랜만에 글을 쓴다. 블로그에 추가할 기능이 없는 것은 아니지만 내가 글을 쓰면서 놀기에는 충분할 정도로 기능을 갖추었다 생각해서 그 동안에는 수학 관련 글만 쓰고 있었다. 이렇게 미루고 미루다 더는 미룰 수 없게 되어 새로운 기능을 추가하게 되었다.

## Minimal-mistakes의 카테고리 정렬

Minimal-mistakes 테마에서는 카테고리별 글 목록을 지원하는데, 이 페이지에서 나타나는 카테고리 목록은 포스트 개수에 따른 내림차순으로 되어 있어 내 경우에는 `Math` 이하에 있는 카테고리들 사이에 `Misc` 밑에 있는 `Misc / Blog Development` 카테고리가 끼어있었다. 

카테고리별 글 목록 페이지에 해당하는 `_pages/category-archive.md` 파일을 열어보면 다음 내용이 전부이다. 

```yml
---
title: "카테고리별 글 목록"
layout: categories
permalink: /ko/categories/
author_profile: true
sidebar: 
    nav: "category-ko"
---
```

이는 이 페이지에서 카테고리를 정렬하는 것이 `_layouts/categories.html`에서[^1] 이루어지기 때문이다. 

이 파일을 열어보면 기존에 Minimal-mistakes에서 어떠한 방식으로 카테고리를 정렬하는지 알 수 있다.

{% raw %}
```html
{% assign categories_max = 0 %}
{% for category in site.categories %}
  {% assign posts=category[1] | where_exp: "post", "post.permalink contains lang_full" %}
  {% if posts.size > categories_max %}
    {% assign categories_max = category[1].size %}
  {% endif %}
```
{% endraw %}

우선 위의 블럭에서는 변수 `categories_max`를 정의한다. 셋째 줄의 `lang_full` 태그가 있는 라인에서의 조건 `where_exp` 부분은 이전에 [다국어 지원](/ko/misc/blog_development/multilingual)에서 추가된 것이다. 이는 `site.categories` 안에 들어있는 모든 카테고리들에 대해서, 각 카테고리들에 속하는 포스트의 개수를 다 세서 가장 큰 것을 저장하게 되어있다.

이 블럭으로부터 중요한 사실을 하나 알 수 있는데, `site.categories` 태그는 2-카테고리라는 것이다. 즉 위의 변수 이름들을 빌려와서 설명하자면 `site.categories` 안에는 카테고리 제목들로 이루어진 `category`가 있고, 각각의 카테고리 제목들 안에는 다시 포스트의 제목으로 이루어진 `post`들이 있다. 이를 신경쓰면서 다음 태그를 보면 다시 하는 일이 명확하다.

{% raw %}
```html
  {% for i in (1..categories_max) reversed %}
    {% for category in site.categories %}
    {% assign posts=category[1] | where_exp: "post", "post.permalink contains lang_full" | sort: 'weight' %}
      {% if posts.size == i %}
        <li>
          <a href="#{{ category[0] | slugify }}">
            <strong>{{ category[0] }}</strong> <span class="taxonomy__count">{{ i }}</span>
          </a>
        </li>
      {% endif %}
    {% endfor %}
  {% endfor %}
```
{% endraw %}

역시 `lang_full` 태그가 있는 라인의 조건은 이전에 [다국어 지원](/ko/misc/blog_development/multilingual) 그리고 [포스트 순서 정렬하기](/ko/misc/blog_development/weight)에서 추가된 것들이다. 카테고리별 글 목록 페이지를 보면, 각 카테고리에 해당하는 글 목록의 나열이 있고, 이들을 카테고리별로 볼 때 쉽게 이동할 수 있도록 맨 위에 목록이 있는데, 이 블럭은 해당 목록에 관한 것이다. 

여기서 보면, `for`문을 포스트 수에 대해서 돌리면서 해당 포스트 수를 갖는 카테고리를 만날 때마다 `<li>` 이하의 내용이 위의 링크를 생성하고 있다. 따라서 내가 원하는대로 하기 위해서는 이 `for`문을 갈아엎어야 한다. 참고로 {% raw %}`{{ category[0] | slugify }}`{% endraw %}는 카테고리 제목에 Liquid 필터 `slugify`를 걸어서 임의의 카테고리 제목을 링크로 쓸 수 있도록 변경해주고 있고, 그 다음 줄에서는 이 링크가 `카테고리 이름 / 포스트 수`의 형태로 그려지도록 해 두었다.

다음 부분을 보자. 

{% raw %}
```html
{% assign entries_layout = page.entries_layout | default: 'list'%}
{% for i in (1..categories_max) reversed %}
  {% for category in site.categories %}
    {% assign posts=category[1] | where_exp: "post", "post.permalink contains lang_full" %}
    {% if posts.size > 0 %}
      {% if category[1].size == i %}
      {% assign posts=category[1] | where_exp: "post", "post.permalink contains lang_full" | sort: 'weight' | reverse %}
        <section id="{{ category[0] | slugify | downcase }}" class="taxonomy__section">
          <h2 class="archive__subtitle">{{ category[0] }}</h2>
          <div class="entries-{{ entries_layout }}">
            {% for post in posts reversed %}
              {% include archive-single.html type=entries_layout %}
            {% endfor %}
          </div>
          <a href="#page-title" class="back-to-top">{{ site.data.ui-text[lang].back_to_top | default: 'Back to Top' }} &uarr;</a>
        </section>
      {% endif %}
    {% endif %}
  {% endfor %}
{% endfor %}
```
{% endraw %}

여기에서는 앞서 언급했듯이, 각각의 카테고리별로 글 목록을 나타내고 있으며, 마찬가지로 포스트 수에 대해 `for`문을 돌리고 있다. 

## 해결방법 \#1

실은 이번 섹션의 내용은 굳이 설명할 필요가 없지만, 깜빡하고 [링크 1](https://github.com/math-jh/math-jh.github.io/commit/7505f72a3ccd275e75f186a3b690b89f66fbc880) 커밋에 있는 `_pages/category-archive.md` 파일 뒤쪽에 실험용으로 사용했던 부분을 남겨뒀었다. 내친김에 이 부분에 대한 설명도 적었다. 

가장 간단한 방법은 `for` 문을 배제하고 위의 반복문 안에 있는 내용을 손으로 적는 것이다. 가령 `Math / Set Theory` 카테고리에 해당하는 부분은 
{% raw %}
```html
<ul class="taxonomy__index">
  {% assign posts=site.categories.["Math / Set Theory"] | where_exp: "post", "post.permalink contains lang_full" | sort: 'weight' %}
  <li>
    <a href="#math-set-theory">
      <strong>Math / Set Theory</strong> <span class="taxonomy__count">{{ posts.size }}</span>
    </a>
  </li>
  ...
</ul>
```
{% endraw %}

그리고

{% raw %}
```html
{% assign posts=site.categories.["Math / Set Theory"] | where_exp: "post", "post.permalink contains lang_full" | sort: 'weight' | reverse %}
  <section id="math-set-theory" class="taxonomy__section">
    <h2 class="archive__subtitle">집합론</h2>
    <div class="entries-{{ entries_layout }}">
      {% for post in posts reversed %}
        {% include archive-single.html type=entries_layout %}
      {% endfor %}     
    </div>
    <a href="#page-title" class="back-to-top">{{ site.data.ui-text[lang].back_to_top | default: 'Back to Top' }} &uarr;</a>
  </section>
  ...
```
{% endraw %}

로 만들 수 있고, 위의 두 블럭 각각에서 `...` 부분에는 그 위쪽 코드들을 똑같이 붙여넣으면 된다. 물론 카테고리 정렬을 내 기준대로 하기로 한 이상, 어딘가에서는 카테고리 순서를 내가 직접 지정해줘야 하는 것은 피할 수 없으나 이것이 지저분한 코드라는 것은 부정할 수가 없다. Sublime text의 snippet 기능을 이용해서 이를 편하게 할 수 있었지만 미관상의 이유로 다른 방법을 찾기로 했다.

## 해결방법 \#2

어쨌든 위의 과정을 거치면서 어디를 어떻게 건드려야 원하는 결과가 나오는지를 알았다. 최종적으로는 불필요한 반복을 막기 위해 `for` 문을 다시 사용했는데, 이번에는 `for` 문을 카테고리 이름에 대해 돌리고, 그 카테고리 이름의 정렬 순서를 내가 원하는대로 설정했다. 

우선 `_config.yml` 파일에 다음과 같은 코드를 추가하여 내가 생각하는 카테고리 정렬 순서를 지정해준다.

```yml
categories_order:
  - Math / Set Theory
  - Math / Category Theory
  ...
```

이 목록은 Liquid 변수 `site.categories_order`에 저장된다. 그럼 이제 다음 코드들

{% raw %}
```html
<ul class="taxonomy__index">
{% for ordered_cat in site.categories_order %}
  {% assign posts=site.categories[ordered_cat] | where_exp: "post", "post.permalink contains lang_full" | sort: 'weight' %}
  <li>
    <a href="#{{ ordered_cat | slugify }}">
      <strong>{{ ordered_cat }}</strong> <span class="taxonomy__count">{{ posts.size }}</span>
    </a>
  </li>
{% endfor %}
</ul>
```
{% endraw %}

그리고

{% raw %}
```html
{% assign entries_layout = page.entries_layout | default: 'list'%}
{% for ordered_cat in site.categories_order %}
  {% assign posts=site.categories[ordered_cat] | where_exp: "post", "post.permalink contains lang_full" | sort: 'weight' | reverse %}
   <section id="{{ ordered_cat | slugify }}" class="taxonomy__section">
     <h2 class="archive__subtitle">{{ ordered_cat }}</h2>
     <div class="entries-{{ entries_layout }}">
       {% for post in posts reversed %}
         {% include archive-single.html type=entries_layout %}
       {% endfor %}
     </div>
     <a href="#page-title" class="back-to-top">{{ site.data.ui-text[lang].back_to_top | default: 'Back to Top' }} &uarr;</a>
   </section>
{% endfor %}
```
{% endraw %}

을 통해 `for`문을 돌리면 원하는 결과를 얻는다. 



[^1]: 2024년 8월 기준으로, 이 파일은 `_includes/posts-texonomy.html`을 다시 불러오고 있다. 이는 비슷한 구조를 갖는 `_layouts/tags.html` 파일과 `_layouts/categories.html` 파일에 대한 코드를 하나로 통합하기 위한 것이다. 