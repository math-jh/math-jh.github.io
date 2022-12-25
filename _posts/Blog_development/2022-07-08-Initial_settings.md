---

title: "기본 설정"
excerpt: "Minimal-mistakes 초기 설정"

read_time: false

categories: [Blog Development]
permalink: /ko/blog_dev/initial_settings

sidebar: 
    nav: "blog_development-ko"

date: 2022-07-08
last_modified_at: 2022-07-08
weight: 3

---

관련 커밋: [링크](https://github.com/math-jh/math-jh.github.io/commit/ae1ab5d1f563af8cc8e9104f836b97724f9ad9a9)
{: .notice--info}

이제부터 모든 글은 내가 사용하는 테마인 Minimal-mistakes를 기준으로 작성한다. 

블로그 꾸밀 때 가장 많이 참고한 사이트는 [이 블로그](https://ansohxxn.github.io/)인데, 기능들을 소개할 때 자세히 설명을 덧붙여 주셔서 다른 기능들도 구현하기 용이했다.

## 불필요한 파일 지우기

앞선 글을 따라 minimal mistakes 테마를 설치했다면, 저장소에는 minimal-mistakes에서 제공하는 샘플 파일들이 같이 들어있을 것이다. 예를 들어 `/docs` 혹은 `/test` 폴더를 보면 minimal mistakes 데모 사이트에 있는 글들이 그대로 들어있다. 이들은 블로그 설정파일인 `_config.yml`에 exclude 목록에 속해있어 페이지를 생성할 때는 무시되지만, 어쨌든 우리 저장소에서는 용량만 차지하니 남겨둘 이유가 없다. 지운 파일들은 다음과 같다.

```
math-jh.github.io
├──  docs
|     ...
├──  test
|     ...
├──  CHANGELOG.md
├──  README.md
├──  Rakefile
├──  banner.js
├──  index.html
├──  minimal-mistakes-jekyll.gemspec
├──  package-lock.json
├──  package.json
├──  screenshot-layouts.png
└──  screenshot.png
```

macOS에서는 작업을 할 때마다 일종의 캐시처럼 `.DS_Store`파일이 생성된다. 이 파일들을 무시하기 위해 `.gitignore` 파일에 `.DS_Store`를 추가하였다.  
마찬가지로 로컬에서 작업을 할 때 생성되는 폴더 `_site`와 `.jekyll-cache`를 `.gitignore`에 추가하였으며, 로컬에서 필요한 gem들을 `Gemfile`에 넣어주었다.[^1]

## Config.yml 세팅

블로그에 대한 모든 정보는 최상위 디렉터리에 있는 `_config.yml`에 담겨있다고 생각해도 된다. 기본 설정에서는 사이트 이름은 Site Title, 저자 이름은 Your Name 등등으로 되어있는데, 이 파일을 수정하면 이를 바꿔줄 수 있다.

우선 `_config.yml` 파일의 `# Site Settings` 아래 항목에서 사이트, 저자 이름 등을 바꿔줄 수 있다.

```yml
# Site Settings
locale                   : "en-US"
title                    : "Site Title"
title_separator          : "-"
subtitle                 : # site tagline that appears below site title in masthead
name                     : "Your Name"
description              : "An amazing website."
url                      : # the base hostname & protocol for your site e.g. "https://mmistakes.github.io"
baseurl                  : # the subpath of your site, e.g. "/blog"
repository               : # GitHub username/repo-name e.g. "mmistakes/minimal-mistakes"
teaser                   : # path of fallback teaser image, e.g. "/assets/images/500x300.png"
logo                     : # path of logo image to display in the masthead, e.g. "/assets/images/88x88.png"
masthead_title           : # overrides the website title displayed in the masthead, use " " for no title
...
```

이 밑에도 breadcrumb나 댓글 등등 수정할 것이 있는데 우선은 이를 적절히 수정해준다. 

```yml
# Site Settings
locale                   : "ko-KR"
title                    : "수학쟁이의 낙서장"
title_separator          : "-"
subtitle                 : # site tagline that appears below site title in masthead
name                     : "Junhyeok Kim"
description              : "수학쟁이의 낙서장"
url                      : "https://math-jh.github.io" # the base hostname & protocol for your site e.g. "https://mmistakes.github.io"
baseurl                  : # the subpath of your site, e.g. "/blog"
repository               : "math-jh/math-jh.github.io" # GitHub username/repo-name e.g. "mmistakes/minimal-mistakes"
teaser                   : # path of fallback teaser image, e.g. "/assets/images/500x300.png"
logo                     : # path of logo image to display in the masthead, e.g. "/assets/images/88x88.png"
masthead_title           : # overrides the website title displayed in the masthead, use " " for no title
``` 

밑으로 쭉 내려가서 `# Site Author`의 항목을 수정하자. 

```yml
# Site Author
author:
  name             : "Your Name"
  avatar           : # path of avatar image, e.g. "/assets/images/bio-photo.jpg"
  bio              : "I am an **amazing** person."
  location         : "Somewhere"
  email            :
```

`avatar`를 사용하기 위해서는 아바타로 사용할 이미지를 넣은 후, 해당 이미지의 경로를 입력하면 된다. 

나는 이 부분을 다음과 같이 수정했다.

```yml
# Site Author
author:
  name             : "MathHolic"
  avatar           : /assets/images/Octahedral.jpeg # path of avatar image, e.g. "/assets/images/bio-photo.jpg"
  bio              : "Grad. student in mathematics"
  location         : "Seoul, Korea"
  email            : "kujuburi@icloud.com"
```

로컬에서 작업할 때, `_config.yml`의 수정사항은 `--livereload` 키를 사용하고 있더라도 실시간으로 반영되지 않으므로, 이것이 잘 적용되었나 확인하기 위해서는 잠시 서버를 내렸다가 다시 열어야 한다. 

이 과정을 거치면 

![Before_config](/assets/images/Blog_development/Initial_settings-1.png){:width="600px" .align-center}

이랬던 사이트가

![After_config](/assets/images/Blog_development/Initial_settings-2.png){:width="600px" .align-center}

이렇게 바뀐 것을 확인할 수 있다. 우측 상단의 Quick-Start Guide는 `_data/navigation.yml`을 열어서 수정하면 된다. 나는 간단히
```yml
main:
  - title: "Categories"
    url: /categories
```
만 남겨두었다. 이 링크는 아직까지 어떠한 것도 할당되어 있지 않으므로, `_pages/category-archive.md`를
```yml
---
title: "카테고리별 글 목록"
layout: categories
permalink: /categories
author_profile: true
---
```
만 적어서 생성했다. 

## 첫 글 작성하기

글을 작성할 때 필요한 마크다운 문법은 위에서 링크해두었던 블로그의 마크다운 문법 [관련 글](https://ansohxxn.github.io/blog/markdown/)에 잘 정리되어 있다. 

우선 앞으로 포스트들을 모아둘 `_posts/` 폴더를 만들고, 이 안에 마크다운(`.md`) 파일을 하나 만들어서 첫 글을 작성하자. 여담으로 `_drafts/` 폴더를 만들어 아직 완성되지 않은 포스트도 보관할 수 있다. 이 폴더에 저장된 포스트는 호스팅할 때에는 보이지 않고, 로컬에서 확인하려면 `jekyll serve` 혹은 `jekyll build` 명령의 인자로 `--drafts`를 추가해주면 된다. 

어쨌든 Jekyll이 마크다운 파일을 포스트로 인식하게 하려면 두 가지 조건이 만족되어야 한다.

1. 마크다운 파일의 이름을 반드시 `yyyy-mm-dd-파일이름`으로 지어줘야 한다. 
2. 또, 이 파일은 반드시 파일의 정보를 알려주는 YAML frontmatter로 시작해야 한다. 이건 별다른 건 아니고, 문서를 시작하기 전 두 개의 `---` 사이에 문서의 정보를 입력해주면 된다. 

예컨대 이 글은 

```yaml
---

title: "Minimal mistakes 테마의 기본 설정"
categories: [Blog Development]
permalink: /ko/blog_dev/initial_settings
sidebar: 
    nav: "blog_development-ko"
date: 2022-07-08
last_modified_at: 2022-07-08

---

관련 커밋: ...
```

이렇게 시작하고 있다.

- `title`: 말 그대로 포스트의 제목이다.
- `categories`: 포스트가 속해있는 카테고리를 나타낸다.
- `permalink`: 포스트가 가질 상대주소. 이 항목을 비워두면 `_config.yml`의 `# Outputting` 아래에 있는 `permalink` 규칙을 따라 자동으로 링크가 주어진다. 
- `sidebar`: 왼쪽에 나타날 사이드바를 의미한다. `_data/navigation.yml`에서 `dev`에 해당하는 목록을 만들면 왼쪽에 이 목록이 나타나게 된다.
- `date`: 문서의 작성 일시
- `last_modified_at`: 문서의 최종 수정 일시

그 외에도 여러가지 항목이 있다. 
- `layout`: 포스트가 취할 형식. `_layouts` 폴더에 들어가면 사용할 수 있는 형식들이 보인다.
- `excerpt`: 포스트에 대한 간략한 설명.
- `published`: `false`로 지정하면 파일을 `_drafts/` 폴더에 지정하는 것과 같은 효과를 준다. 로컬에서는 `--unpublished`를 통해 `published: false`인 파일을 빌드할 수 있다.
- `tags`: 포스트에 관한 태그들

`_config.yml`의 가장 밑으로 내려가보면 아래와 같이 `# Defaults` 항목에 여러가지가 적혀 있는데, 이는 포스트(`type: posts`)를 작성할 때 기본값을 지정해주는 것과 같다.

```yml
# Defaults
defaults:
  # _posts
  - scope:
      path: ""
      type: posts
    values:
      layout: single
      author_profile: true
      read_time: true
      comments: # true
      share: true
      related: true
```

예를 들어 이 글은 `layout`이 지정되지 않아서 원래대로라면 아무런 형식 없는 페이지가 되어야 하겠지만, 여기에서 `layout: single`이 기본값으로 지정되어 있어 `single` 레이아웃을 따라 포스팅이 예쁘게 보인다. `author-profile`, `comments`는 굳이 설명하지 않아도 될 것 같고, `read-time`은 이 페이지 맨 위에 있는 `4분 소요`를 표시할지, `share`는 공유 버튼을 활성화시킬지, `related`는 맨 밑에 관련글을 표시할지 아닐지의 여부를 나타낸다. 나는 이 기능이 마음에 들지 않아 default에서 빼 버렸다. `comments`의 경우, 추가적으로 설정할 것이 많아 지금은 `true`로 해 봤자 적용되지 않는다.

[^1]: 다만, 나는 이제 로컬에서 빌드할 대에는 `--destination`키를 이용해서 github 폴더 안에는 아예 `_site` 폴더가 생길 일이 없도록 해 두었다.