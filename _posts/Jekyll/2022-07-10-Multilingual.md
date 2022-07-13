---

title: "Jekyll 블로그 다국어 지원"
excerpt: "다국어 지원 및 사이트 구조 수정"

lang: ko

categories: [Blog development]
permalink: /blog_dev/multilingual

sidebar: 
    nav: "dev"

date: 2022-07-10
last_modified_at: 2022-07-10
weight: 13

---

얼마나 사용할 수 있을지는 모르겠지만, 블로그에 다국어 기능을 지원하고 싶어졌다. 이 기능은 사용하는 사람이 별로 없어서인지 정보가 거의 없어서 열심히 삽질을 해야 했다. 혹시 비슷한 삽질을 하시는 분이 있을까 싶어 기록을 남겨둔다.

## 사이트맵

다국어 지원을 위해 사이트 구조를 바꿨다. Jekyll 블로그를 만들 때, 두 개의 base url을 지정하여 이들을 따로따로 Jekyll로 빌드하고, 그 후 합치는 방법이 있었으면 좋았겠지만 안타깝게도 그런 방법은 찾지 못했다. 

우선 모든 글의 path 맨 앞에 `/en/`과 `/ko/`를 붙여 사이트를 크게 `math-jh.github.io/ko/~~`으로 표현되는 한글 버전의 사이트와 `math-jh.github.io/en/~~`으로 표현되는 영어 버전의 사이트로 나누기로 했다. 아무것도 없는 홈 `math-jh.github.io/`는 언어 선택 페이지로 사용하면 적당할 것 같았다. 또, 같은 주제를 공유하는 포스트들 사이에는 언어전환이 자유롭도록 하고 싶었다. 따라서 대략 다음과 같은 구조가 생긴다.

![sitemap](/assets/images/Blog_development/Multilingual-1.png){:width="700px" class="invert" .align-center}

