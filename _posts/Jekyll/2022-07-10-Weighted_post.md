---

title: "깃블로그 포스트 순서 정렬하기"
excerpt: "새로운 변수를 통한 순서 정렬"

lang: ko

categories: [Blog development]
permalink: /blog_dev/weight

sidebar: 
    nav: "dev"
    
date: 2022-07-10
last_modified_at: 2022-07-10
weight: 11

---

## 목표

Minimal-mistakes 테마는 포스트를 배열할 때 날짜순으로 우선 정렬하고, 같은 날짜에 적힌 포스트의 경우 제목명 순으로 정렬한다. 따라서 포스팅의 순서를 맞추기 위해서는 작성 일자를 임의로 수정해야 한다. 이건 별로 바람직한 일이 아니라고 생각되어 새로운 방법이 필요했다. 

배열을 수정하는 것은 어려운 일은 아니지만, 카테고리 모음에서 보이는 배열 뿐만 아니라 포스트 하단의 이전 글/다음 글 버튼 또한 같은 방식으로 배열되어 있어야 하므로 약간의 liquid 문법을 사용해야 한다. 

## Frontmatter에 weight 할당하기

이를 위해 나는 frontmatter에 추가적인 넘버링 `weight`을 추가해서, 카테고리 및 pagination이 weight을 기준으로 정렬되도록 하였다. 예를 들어, 이 글의 frontmatter는 이제 
```yml
---

title: "포스트 순서 정렬하기"
categories: [Blog development]
permalink: /blog_dev/weight
date: 2022-07-10
last_modified_at: 2022-07-10
weight: 11

---
```
이 된다.

## 레이아웃 수정

이후 `_layouts/categories.html` 파일을 다음과 같이 수정해준다. 나는 레이아웃을 수정하며 내가 사용하지 않을 것 같은 레이아웃 파일들도 모두 삭제했다.
{% raw %}
```html
---
layout: archive
---

{{ content }}

{% assign categories_max = 0 %}
{% for category in site.categories %}
  {% if category[1].size > categories_max %}
    {% assign categories_max = category[1].size %}
  {% endif %}
{% endfor %}

<ul class="taxonomy__index">
  {% for i in (1..categories_max) reversed %}
    {% for category in site.categories %}
    {% assign posts=category[1] | sort: 'weight' %}
      {% if category[1].size == i %}
        <li>
          <a href="#{{ category[0] | slugify }}">
            <strong>{{ category[0] }}</strong> <span class="taxonomy__count">{{ i }}</span>
          </a>
        </li>
      {% endif %}
    {% endfor %}
  {% endfor %}
</ul>

{% assign entries_layout = page.entries_layout | default: 'list' %}
{% for i in (1..categories_max) reversed %}
  {% for category in site.categories %}
    {% if category[1].size == i %}
      {% assign posts = category[1] | sort: 'weight' %}
      <section id="{{ category[0] | slugify | downcase }}" class="taxonomy__section">
        <h2 class="archive__subtitle">{{ category[0] }}</h2>
        <div class="entries-{{ entries_layout }}">
          {% for post in posts %}
            {% include archive-single.html type=entries_layout %}
          {% endfor %}
        </div>
        <a href="#page-title" class="back-to-top">{{ site.data.ui-text[site.locale].back_to_top | default: 'Back to Top' }} &uarr;</a>
      </section>
    {% endif %}
  {% endfor %}
{% endfor %}
```
{% endraw %}

이제 `category` 레이아웃이 적용된 `categories-archive.md`에 해당하는 페이지를 보면, 날짜에 관계 없이 `weight`이 작은 순으로 정렬된 것을 확인할 수 있다.

## Pagination 수정하기

포스트 가장 밑에 있는 이전 글/다음 글 버튼은 `post_pagintation.html`을 기준으로 이루어진다. 나는 [이 글](https://ansohxxn.github.io/blog/prevnext/)을 바탕으로 포스트 하단의 이전 글/다음 글 버튼이 동일한 카테고리 내에서만 이동하도록 한 상태여서, 수정 전의 파일이 다음과 같다.
{% raw %}
```html
<!--첫 번째 문단-->
{% assign cat = page.categories[0] %}
{% assign cat_list = site.categories[cat] %}
{% for post in cat_list %}
  {% if post.url == page.url %}
    {% assign prevIndex = forloop.index0 | minus: 1 %}
    {% assign nextIndex = forloop.index0 | plus: 1 %}
    {% if forloop.first == false %}
      {% assign next_post = cat_list[prevIndex] %}
    {% endif %}
    {% if forloop.last == false %}
      {% assign prev_post = cat_list[nextIndex] %}
    {% endif %}
    {% break %}
  {% endif %}
{% endfor %}

<!--두 번째 문단-->
{% if prev_post or next_post %}
  <nav class="pagination">
    {% if prev_post %}
      <a href="{{ prev_post.url }}" class="pagination--pager">{{ site.data.ui-text[site.locale].pagination_previous | default: "Previous" }}</a>
    {% else %}
      <a href="#" class="pagination--pager disabled">{{ site.data.ui-text[site.locale].pagination_previous | default: "Previous" }}</a>
    {% endif %}
    {% if next_post %}
      <a href="{{ next_post.url }}" class="pagination--pager">{{ site.data.ui-text[site.locale].pagination_next | default: "Next" }}</a>
    {% else %}
      <a href="#" class="pagination--pager disabled">{{ site.data.ui-text[site.locale].pagination_next | default: "Next" }}</a>
    {% endif %}
  </nav>
{% endif %}
```
{% endraw %}

이제 아까와 마찬가지로 `cat_list`를 `weight`에 맞추어 정렬해주면 되므로, `sort: 'weight'`를 `liquid`문법에 추가해주면 된다. 하지만 아까와는 다르게 방향을 반대로 해야 하므로 `reverse` 태그도 넣어줘야 한다. 따라서 수정 후에는 다음과 같이 된다.
{% raw %}
```html
<!--첫 번째 문단-->
{% assign cat = page.categories[0] %}
{% assign cat_list = site.categories[cat] | sort: 'weight' | reverse %}
{% for post in cat_list %}
  {% if post.url == page.url %}
    {% assign prevIndex = forloop.index0 | minus: 1 %}
    {% assign nextIndex = forloop.index0 | plus: 1 %}
    {% if forloop.first == false %}
      {% assign next_post = cat_list[prevIndex] %}
    {% endif %}
    {% if forloop.last == false %}
      {% assign prev_post = cat_list[nextIndex] %}
    {% endif %}
    {% break %}
  {% endif %}
{% endfor %}

<!--두 번째 문단-->
{% if prev_post or next_post %}
  <nav class="pagination">
    {% if prev_post %}
      <a href="{{ prev_post.url }}" class="pagination--pager">{{ site.data.ui-text[site.locale].pagination_previous | default: "Previous" }}</a>
    {% else %}
      <a href="#" class="pagination--pager disabled">{{ site.data.ui-text[site.locale].pagination_previous | default: "Previous" }}</a>
    {% endif %}
    {% if next_post %}
      <a href="{{ next_post.url }}" class="pagination--pager">{{ site.data.ui-text[site.locale].pagination_next | default: "Next" }}</a>
    {% else %}
      <a href="#" class="pagination--pager disabled">{{ site.data.ui-text[site.locale].pagination_next | default: "Next" }}</a>
    {% endif %}
  </nav>
{% endif %}
```
{% endraw %}