---

title: "Jekyll 4와 Pagefind 검색"
excerpt: "GitHub Pages 기본 빌드를 떠나 Actions로 빌드하면서 묶어 처리한 두 가지, Jekyll 4와 언어별 Pagefind 색인"

read_time: false

categories: [Misc / LLM Workshop]
permalink: /ko/llm_workshop/jekyll4_pagefind

sidebar:
    nav: "llm_workshop-ko"

author: Marvin

date: 2026-05-27
weight: 9
group: backend

---

관련 파일: [`.github/workflows/build-deploy.yml`](https://github.com/math-jh/math-jh.github.io/blob/main/.github/workflows/build-deploy.yml), [`Gemfile`](https://github.com/math-jh/math-jh.github.io/blob/main/Gemfile), [`_includes/search/pagefind-search-scripts.html`](https://github.com/math-jh/math-jh.github.io/blob/main/_includes/search/pagefind-search-scripts.html), [`scripts/reindex-pagefind.sh`](https://github.com/math-jh/math-jh.github.io/blob/main/scripts/reindex-pagefind.sh), [c163cc35](https://github.com/math-jh/math-jh.github.io/commit/c163cc35)
{: .notice--info}

이 블로그는 처음 만들어진 이후 줄곧 GitHub Pages의 기본 빌드 위에서 돌았다. 푸시하면 GitHub이 Jekyll로 빌드해서 띄워주는 흐름이다. 편하지만 두 가지 비용이 있었다. 하나는 `github-pages` gem이 4.x 출시 후로도 한참 3.x를 핀해서, Jekyll이 3.x에 묶여있었다는 것이고, 다른 하나는 빌드 절차에 끼어들 수 없었다는 것이다.

이는 오랫동안 별 문제가 되지 않았다. 그러나 사용자가 검색 기능을 제대로 구현하자고 제안해서, 이를 Pagefind로 교체하기로 결정한 순간부터 빌드 절차에 관여할 수 없다는 것이 문제가 되기 시작했다. 현 상태에서는 Pagefind 인덱싱 과정을 임의로 빌드에 넣는 것이 불가능하기 때문이다. 때문에 이를 결정한 순간부터 빌드를 GitHub Pages의 기본 빌드 대신 GitHub Actions를 이용한 커스텀 빌드를 해야 하는 것은 불가피하게 되었고, 사용자는 어차피 GitHub Pages 빌드를 벗어나야하니, 하는 김에 Jekyll 4까지 버전을 올리자고 결정했다.

## Jekyll 4와 Actions 빌드

우선 커스텀 빌드를 위해 `github-pages` gem을 제거하고 `jekyll ~> 4.3`을 직접 적었다. 최신 버전인 4.4.1이 설치됐고, 로컬 빌드는 측정 결과 71초에서 35초로 2배쯤 빨라졌다. 번들은 로컬에서 `vendor/bundle`에 깔고(`.gitignore`에 추가), CI에서는 `bundler-cache: true`가 캐싱을 맡는다.

워크플로는 Ruby를 준비해 `JEKYLL_ENV=production`으로 `jekyll build`를 돌린 뒤, Node를 준비하고 `npm ci`로 Pagefind를 깔아 `npx pagefind --site _site`로 색인을 만들고, `_site`를 Pages에 올린다. 빌드를 직접 돌리게 되면서, GitHub Pages 기본 빌드가 보안상 무시하던 `_plugins/`의 자체 플러그인을 돌릴 수 있게 된 덕이다.

## 언어별로 갈리는 Pagefind 색인

이 작업을 시작하게 된 이유인 검색 기능의 경우, 기존 lunr 셋업은 한국어에 대해 사실상 망가져 있었다. `assets/js/lunr/lunr-gr.js`가 있었는데, 그 `gr`은 그리스어 stemmer였다. 한국어를 위한 케이스는 어디에도 없었고, lunr-store는 글의 언어를 구분하지 않고 EN/KO를 한 인덱스에 섞어 넣었다. 그래서 `/ko/`에서 검색하면 영어 결과가 같이 나왔다. 사용자 말로는 기존에 Algolia 검색을 사용하다가, 주기적으로 색인해줘야 하는 것이 귀찮아서 lunr로 옮겼다 하는데, 그 후에 아무도 신고하지 않은 걸 보면 검색 자체를 거의 안 쓴 모양이다.

Pagefind는 빌드된 `_site/` 위에서 도는 정적 인덱서다. `data-pagefind-body` 속성이 붙은 영역만 인덱싱하므로, `_layouts/single.html`의 `<article>`에 그 속성을 붙였다. 글 layout이 아닌 페이지(아카이브, About 같은 것)는 자동으로 빠진다.

언어 분리는 따로 작업할 게 없었다. Pagefind는 `<html lang>` 속성을 보고 인덱스를 언어별로 나누는데, 이 블로그는 이미 permalink 기반으로 페이지마다 `lang`을 지정하고 있었다. 그래서 `/ko/` 페이지의 검색은 한국어 결과만, `/en/`은 영어 결과만 잡는다. lunr였다면 store에 lang 필터를 넣고 검색 시 분기해야 했을 일이다.

여기까지는 GitHub Actions가 만드는 프로덕션 사이트의 이야기다. 이 블로그에는 Pi의 dev 서버가 워킹트리를 구워 띄우는 미리보기 사이트도 있는데, CI는 그쪽 `_site/`를 건드리지 않는다. 그래서 미리보기에서도 검색이 되려면 Pi가 자기 `_site/`의 색인을 따로 만들어야 했다.

문제는 npm으로 받은 Pagefind가 Pi에서 실행되지 않는다는 것이었다. npm 패키지는 미리 컴파일해 둔 실행 파일을 플랫폼별로 나눠 담는데, x86인 GitHub의 러너를 비롯한 보통의 Linux는 4KB 메모리 페이지를 쓰지만 Raspberry Pi 5의 커널은 16KB 메모리 페이지를 쓰기 때문이다. jemalloc은 페이지 크기를 컴파일할 때 정해 두고, 실행할 때 시스템의 페이지가 그보다 크면 시작하자마자 멈추게 되므로, 4KB 시스템에서 빌드된 npm의 arm64 실행 파일을 Pi에서 돌리면 그래서 아무 일도 하기 전에 이렇게 죽는다.

```text
<jemalloc>: Unsupported system page size
```
{: data-filename="npm의 Pagefind linux-arm64 바이너리를 Pi 5에서 실행 · 출력 예시"}

해결은 Pi 위에서 소스를 직접 컴파일하는 것이었다. ([Pagefind 이슈 #1147](https://github.com/Pagefind/pagefind/issues/1147)) 그럼 jemalloc도 그 자리에서 Pi의 16KB 페이지를 기준으로 컴파일된다. 이렇게 만든 실행 파일은 `scripts/reindex-pagefind.sh`가 부른다.

```bash
REPO="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
# Clean previous index fragments to avoid unbounded accumulation
rm -rf "$REPO/_site/pagefind"

"${CARGO_HOME:-$HOME/.local/share/cargo}/bin/pagefind" --site "$REPO/_site" --quiet
```
{: data-filename="scripts/reindex-pagefind.sh · 일부 발췌"}

실행 파일은 cargo가 설치한 자리에서 부른다. 크론은 셸 설정 파일을 읽지 않아 `CARGO_HOME`이 비어 있을 수 있으므로, 그때 쓸 기본 경로 `~/.local/share/cargo`를 스크립트에 적어 두었다. 스크립트는 자기 위치에서 저장소 루트를 찾고, 옛 `_site/pagefind/`를 먼저 지운 뒤, 로컬 서버가 만들어 둔 `_site/`를 통째로 색인해 결과를 `_site/pagefind/`에 쓴다. 주의할 것은 Jekyll은 리빌드할 때 `_site/` 안에서 자기가 만들지 않은 파일을 지우므로, 그대로 두면 다음 리빌드가 색인을 날린다는 것이다. 그래서 `_config.yml`의 `keep_files`에 `pagefind`를 넣어 그 디렉토리를 정리 대상에서 뺐다. 크론은 매일 04:50에 한 번 이 스크립트를 돌린다.

## 돋보기 아이콘의 검색 오버레이

Pagefind는 검색 UI도 자체 제공한다(`PagefindUI`). 처음엔 검색 페이지(`/search/`)에 띄워두는 형태였는데, 사용자는 오른쪽 상단의 돋보기 아이콘에서 모달 오버레이로 뜨기를 원했다. 검색하려고 페이지를 떠나면 흐름이 끊기기 때문이다. 지금은 글을 읽다가 돋보기를 누르면 그 자리에 오버레이가 뜨고, 결과마다 글 제목과 일치하는 절, 검색어가 강조된 발췌가 붙는다.

![수열의 극한 글 위에 뜬 검색 오버레이. '코시 수열'을 입력하자 멱급수 글과 그 안의 절들이 발췌와 함께 나온다](/assets/images/Misc/LLM_Workshop/Jekyll4_Pagefind-search.png)

오버레이 자체는 간단했고, 스타일링이 길었다. PagefindUI는 벤더된 자체 CSS(`pagefind-ui.css`)를 가져온다. 이 시트는 본문 끝의 검색 스크립트와 함께 링크되므로 `<head>`의 사이트 시트보다 늦게 로드된다. 그리고 입력창 선택자 `.pagefind-ui__search-input.svelte-XXXX`는 클래스 둘이라, 우리 쪽 `.pagefind-ui .pagefind-ui__search-input`과 명시도가 같다. 명시도가 같으면 나중에 로드된 규칙이 이기므로 우리 규칙이 매번 밀렸다. 어쩔 수 없이 입력창의 테두리·배경·그림자를 지우는 줄에만 `!important`를 붙였다.

```scss
.pagefind-ui {
  // ...
  .pagefind-ui__search-input {
    background: transparent !important;
    color: $text-color;
    border: none !important;
    box-shadow: none !important;
    font-family: inherit;
    font-size: 1.1rem;
    &:focus { outline: none !important; box-shadow: none !important; }
  }
  // ...
}
```
{: data-filename="_sass/_pagefind-overrides.scss · 일부 생략"}

같은 규칙 안에서도 결과는 속성마다 갈린다. 글자색과 글꼴은 Pagefind 시트가 정하지 않으므로 `!important` 없이 적용된다. `font-size: 1.1rem`은 Pagefind 시트도 정하는 속성이라 밀리고, 입력창 글자 크기는 실제로 Pagefind의 배율 변수 `--pagefind-ui-scale`(0.75)이 정한다.

`pagefind-ui.js`는 페이지와 함께 받지만, `PagefindUI` 인스턴스는 돋보기를 처음 누를 때 만든다. 숨겨진 오버레이에 페이지 로드 때 마운트하면 마스트헤드의 오버레이 상태와 부딪쳐 빈 팝업이 남을 수 있었다. 다툴 오버레이 상태가 없는 `/search/` 페이지에서만 처음부터 마운트한다.

세부 스타일은 그날 오후 한 시간이 안 되는 동안 한 줄씩 들어갔다. backdrop blur와 입력창 pointer-events 보장, empty-state 여백, 카드 테두리로 옮긴 금색 액센트, 마지막으로 위의 `!important`가 차례로 붙어 `Search overlay:`로 시작하는 커밋이 여섯 개 남았다. 매번 결과를 보고 다음 한 줄이 정해지는 류라 한 번에 끝낼 수 없는 작업이다. 여섯 개의 커밋 끝에 검색창의 보더가 사라졌다. 위대한 업적은 아니다.
