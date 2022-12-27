---

title: "다국어 지원"
excerpt: "다국어 지원 및 사이트 구조 수정"

read_time: false

categories: [Misc / Blog Development]
permalink: /ko/misc/blog_development/multilingual

sidebar: 
    nav: "blog_development-ko"

date: 2022-07-10
last_modified_at: 2022-07-10
weight: 14

---

관련 커밋: [링크](https://github.com/math-jh/math-jh.github.io/commit/29b538ec0a9ad14be4c52ed148a53d200017dbb1)
{: .notice--info}

얼마나 사용할지는 모르겠지만, 블로그에 다국어 (정확히 말하자면 한/영만) 기능을 지원하고 싶어졌다. 이 기능은 사용하는 사람이 별로 없어서인지 정보가 거의 없어서 열심히 삽질을 해야 했다. 

내가 짠 코드들은 좀 지저분하지만, 그래도 혹시 비슷한 삽질을 하시는 분이 있을까 싶어 기록을 남겨둔다.

## 사이트맵 및 기본 구상

Jekyll 블로그를 만들 때, 두 개의 base url을 지정하여 이들을 따로따로 Jekyll로 빌드하고, 그 후 합치는 방법이 있었으면 좋았겠지만 안타깝게도 그런 방법은 찾지 못했다. 그래서 그냥 사이트 구조를 처음부터 바꾸기로 했다.

모든 글의 path 맨 앞에 `/en/`과 `/ko/`를 붙여 사이트를 크게 

- `math-jh.github.io/ko/~~`으로 표현되는 한글 버전의 사이트,
- `math-jh.github.io/en/~~`으로 표현되는 영어 버전의 사이트,

이렇게 두 개의 부분으로 나눈다. 그럼 홈 `math-jh.github.io/`는 언어 선택 페이지로 사용하면 적당할 것 같다. 

같은 주제를 공유하지만 언어만 다른 두 포스트가 있다면, 이들 포스트 사이를 자유롭게 이동할 수 있는 버튼 또한 필요하다. 이를 도식으로 나타내면 다음과 같다.

![sitemap](/assets/images/Blog_development/Multilingual-1.png){:width="800px" class="invert" .align-center}

서로 다른 언어의 두 포스트를 왔다갔다 하는 버튼은 다크모드를 적용할 때 만든 masthead 아이콘 옆에 두기로 하였으며, 이 버튼은 세 가지 조건

1. 현재 페이지의 언어가 한글이면 `ko`, 영어면 `en`으로 표시되며,
2. 이 버튼을 누르면 한글 페이지에서 영어 페이지로, 영어 페이지에서 한글 페이지로 이동하고,
3. 만일 동일한 주제를 가진 다른 언어의 글이 존재하지 않는다면 이 버튼은 보이지 않는다.

을 만족해야 한다. 또 github pages를 이용해 올릴 때, 수동으로 사이트를 빌드해서 올릴 필요가 없도록 플러그인은 사용하지 않는 것을 목표로 한다.

## Liquid 필터

Jekyll에서 다국어를 사용하는 사람이 없어서, 이를 구글링해봐도 결과가 아주 적었다. 그 중 유용했던 것은 [이 글](https://piaflu.tistory.com/136)이었다. 이 글에서는 `lang`와 `lang-ref`를 정의하여 `lang-ref`가 같은 포스트들을 동일한 글로 취급한 후, 같은 `lang-ref`를 공유하는 포스트들의 `lang`들을 나열하는 방식으로 다국어 기능을 구현했다. 

내 경우에 이를 비슷하게 구현하면 대충 다음과 같은 코드가 될 것이다.

{% raw %}
```
{% if page.lang %}
    <div> <a href="{% if page.lang == "ko" %}{{ page.url | relative_url | remove_first: "/ko" | prepend: "/en"}}{% else %}{{ page.url | relative_url | remove_first: "/en" | prepend: "/ko"}}{% endif %}">{{ page.lang }}</a></div>
{% endif %}
```
{% endraw %}

그러나 이 코드는 실패했다. 이는 Jekyll이 사이트를 빌드할 때 각 페이지마다 masthead와 footer 등을 빌드하는 대신, 하나의 페이지에 대해 masthead와 footer를 빌드한 후 본문만 바꿔가며 각 페이지들을 만들기 때문이다.[^1] 결과적으로 내가 소스에는 위와 같은 코드를 짜 놓는다고 하더라도, Jekyll을 통해 페이지가 빌드되면 위의 코드들은 모두 고정된 상수들로 바뀌어버려 원하는대로 행동하지 않게 된다.

반면 원래 글에서는 언어 선택기가 본문영역 내부에 있었기 때문에 Jekyll이 페이지를 빌드할 때 페이지마다 언어 선택기를 새로 만들었고, 따라서 잘 동작했다. 어쨌든 내 경우에는 이 방법을 사용할 수 있는 방법이 없다.

## 자바스크립트

이렇게 실패를 하고 나니, 사실상 liquid만을 이용하여 이 기능을 구현하는 것은 불가능하다고 판단했다. 결국 masthead에 언어 선택기를 넣기 위해서는 HTML 컨텐츠가 로드된 후 페이지 안의 컨텐츠들을 능동적으로 수정해야 했고, 이를 위해서는 자바스크립트가 거의 유일한 해결책이었다. 

다만 자바스크립트가 포스트의 frontmatter를 읽어오도록 하려면 {% raw %}`{{ post.lang }}`{% endraw %}와 같이 liquid 필터를 이용하는 것이 필수적인데, 이 또한 위와 동일한 이유로 불가능하다. 따라서 나는 liquid를 통해 frontmatter에서 직접적으로 `lang`을 받아오는 대신, 현재 url을 자바스크립트로 받아온 후, 이를 바탕으로 현재의 언어를 추정하도록 코드를 짰다. 

우선 `masthead.html`에 다음과 같이 정의된 체크박스가 있다.
```html
<label class="switch" for="lang" id="lang_container">
    <input type="checkbox" id="lang" onclick="lang_select()"/>
    <span class="checked">en</span>
    <span class="unchecked">ko</span>
</label>
```
즉 체크박스가 체크되어 있으면 `en`으로 표시되고, 체크되어있지 않으면 `ko`로 표시되는 체크박스다. 이 체크박스를 클릭할 때마다 `lang_select()` 함수가 실행된다. 이 함수는 현재 url의 path의 가장 처음 부분을 `/ko/`에서 `/en/`으로 바꾼 url로 리다이렉트 해주는 함수이다. 
```javascript
function lang_select() {
    var pathname = window.location.pathname.split('/');
    var newpathname = "";
    if (pathname[1] == "en") {
      var newlang = "/ko";
    } else if (pathname[1] == "ko") {
      var newlang = "/en";
    }
    for (i = 2; i < pathname.length; i++) {
      newpathname += "/";
      newpathname += pathname[i];
    }
    window.location.href = newlang + newpathname;
}
````
어차피 나는 영어와 한글만 왔다갔다 할 것이므로 그냥 하드코딩을 해서 한글 페이지와 영어 페이지로의 링크가 생성되도록 하였다. 만약 <em_ko>정말로</em_ko> 다국어 사이트를 만든다면, `_config.yml`에서 지원할 다국어의 목록을 입력한 후, 이 목록을 이용해서 liquid로 for 문을 걸어서 순서대로 언어를 바꾸도록 할 수 있을 것 같다. 

역시 마찬가지로, masthead에서 사이트 이름을 클릭했을 시 언어선택 페이지인 `math-jh.github.io/`가 아닌 각각의 홈 화면 `math-jh.github.io/ko/`와 `math-jh.github.io/en/`이 나오도록 하는 것도 자바스크립트가 필요하다.
```javascript
function lang_home() {
    var origin = window.location.origin;
    var pathname = window.location.pathname.split('/');
    if (pathname[1] == "en" || pathname[1] == "ko"){
        window.location.href = "/" + pathname[1];
    }
    else {
        window.location.href = "/"
    }
}
```
마지막으로 이 체크박스는 접속한 페이지의 주소와 관계없이 항상 unchecked인 상태로 시작할테니, `DOMContentLoaded`를 트리거로 하여 이를 올바르게 수정해주는 스크립트를 `head.html`에 넣었다. 

{% raw %}
```javascript
{% if site.multilingual %}
  window.addEventListener('DOMContentLoaded', function(){
    var origin = window.location.origin;
    var newpathname = "";
    var pathname = window.location.pathname.split('/');
    if(!(pathname[1] == "en" || pathname[1] == "ko")){
      document.getElementById('lang_container').style.display="none";
    } else if (pathname[1] == "en") {
      document.querySelector("#lang").checked=true;
      var newlang="/ko"
    } else if (pathname[1] == "ko") {
      document.querySelector("#lang").checked=false;
      var newlang="/en"
    }
    for (i = 2; i < pathname.length; i++) {
      newpathname += "/";
      newpathname += pathname[i];
    }
    var newurl = newlang + newpathname;
    var http = new XMLHttpRequest();
    http.open('HEAD', newurl, false);
    http.send();
    if (http.status == 404) {
      document.getElementById('lang_container').style.display="none";
    }
  })
{% endif %} 
````
{% endraw %}

이 코드는 path의 맨 앞이 `/ko/` 혹은 `/en/`으로 시작하지 않는다면 이 체크박스를 숨기고, 또 path가 `/ko/` 혹은 `/en/`으로 시작하더라도 다른 언어의 페이지가 존재하지 않는다면 마찬가지로 체크박스를 숨기는 기능 또한 겸하고 있다.

어쨌든 이를 통해 masthead쪽과 관련된 문제는 모두 해결했다.

## Pagination 수정

언어가 다른 두 페이지가 같은 카테고리를 공유한다면, 기존의 `post_pagination.html`은 이들을 날짜순으로 (내 경우에는 `weight` 순으로) 배열한 후 언어에 관계 없이 이전 글/다음 글을 할당할 것이다. 따라서 한글 페이지를 읽다 다음 페이지를 눌렀는데 뜬금없이 영어 페이지가 나오는 경우가 생기게 된다. 

따라서 `post_pagination.html`을 다음과 같이 수정하였다.[^2]

{% raw %}
```html
{% assign lang = site.locale %}
{% assign lang_prefix = page.url | truncate: 3, "" %}
{% if lang_prefix contains "en" or lang_prefix contains "ko" %}
  {% assign lang = lang_prefix | remove_first: "/" %}
{% endif %}
{% assign lang_full = lang | append: "/" | prepend: "/" %}

<!--첫 번째 문단-->
{% assign current_category = page.categories[0] %}
{% assign lang_posts = site.posts | where_exp: "post", "post.permalink contains lang_full" %}
{% assign cat_list = lang_posts | where: "categories", current_category | sort: "weight" | reverse %}
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
  <nav class="pagination" style="margin-bottom:3em">
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

이에 따르면 `/ko/` 혹은 `/en/`로 시작하는 포스트는 자신과 같은 카테고리를 갖고 자신과 동일한 언어를 사용하는 포스트들 가운데에서 이전 글과 다음 글을 찾을 것이다. 반면 permalink가 이들 둘로 시작하지 않는 포스트의 경우, 자신과 동일한 카테고리의 포스트들 가운데 permalink가 `/ko-KR/`를 포함하는 (`site.locale`이 `ko-KR`이기 때문이다) 포스트들을 늘어두고 이전 글/다음 글을 결졍하게 된다. 

어쨌든 내 구상에서 permalink가 `/ko/` 혹은 `/en/`로 시작하지 않는 포스트는 `404.md`나 언어 선택화면, 자기소개 페이지 등 어차피 카테고리가 존재하지 않을 포스트들 뿐이기 때문에 이 부분은 어찌돼도 좋았다. 

## Site.locale 수정

영어만 할 수 있는 사람이 영어로 검색하여 내 사이트의 영어 버전에 접속하였을 때, 본문 내용만 영어고 나머지 메뉴는 모두 한글이라면 당혹스러울 것이다.  
위의 코드에서 보듯이 minimal-mistakes는 각 용어들의 번역이 담긴 `data/ui-text.yml` 파일에서 `site.locale`에 해당하는 언어를 골라서 페이지를 빌드한다. 따라서 `site.locale`자리에 현재 페이지의 언어를 감지하도록 `lang`을 넣어주면 한/영 버전의 사이트 모두에서 자신의 언어에 해당하는 메뉴를 볼 수 있게 된다. 


[^1]: 예를 들어, masthead에 {% raw %}`{{ page.url }}`{% endraw %}을 넣어보면 이 사실을 알 수 있다. 만일 Jekyll이 페이지별로 `masthead.html`을 따로따로 불러온다면, masthead에 적힌 {% raw %}`{{ page.url }}`{% endraw %}는 페이지마다 다른 주소값을 주어야 할 것이나, 실제로는 모든 페이지에서 특정한 페이지의 url만 보인다.
[^2]: 원래는 첫 시도 때의 `lang` 태그를 살려두고 이용했었는데, 이 부분을 제외하고는 해당 태그가 하는 역할이 없어 url을 이용하는 방식으로 수정했다.