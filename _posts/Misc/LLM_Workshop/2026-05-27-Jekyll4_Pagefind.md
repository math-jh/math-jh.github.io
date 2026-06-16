---

title: "Jekyll 4와 Pagefind 검색"
excerpt: "GitHub Pages 기본 빌드를 떠나면서 묶어 처리한 두 가지"

read_time: false

categories: [Misc / LLM Workshop]
permalink: /ko/llm_workshop/jekyll4_pagefind

sidebar:
    nav: "llm_workshop-ko"

author: Marvin

date: 2026-05-27
weight: 10

---

관련 파일: [`.github/workflows/deploy.yml`](https://github.com/math-jh/math-jh.github.io/blob/main/.github/workflows/deploy.yml), [`Gemfile`](https://github.com/math-jh/math-jh.github.io/blob/main/Gemfile), [`_includes/search/pagefind-search-scripts.html`](https://github.com/math-jh/math-jh.github.io/blob/main/_includes/search/pagefind-search-scripts.html), [`scripts/reindex-pagefind.sh`](https://github.com/math-jh/math-jh.github.io/blob/main/scripts/reindex-pagefind.sh)
{: .notice--info}

이 블로그는 처음 만들어진 이후 줄곧 GitHub Pages의 기본 빌드 파이프라인 위에서 돌았다. 푸시하면 GitHub이 Jekyll로 빌드해서 띄워주는 흐름이다. 편하지만 두 가지 비용이 있었다. Jekyll이 3.x에 묶여 있었고(github-pages gem이 4.x 출시 후로도 한참 3.x를 핀했다), 빌드 절차에 끼어들 수 없었다. 후자는 그때까진 큰 불만이 아니었지만, 결국 두 문제를 같이 풀 시점이 왔다.

전환은 한 PR에 묶였다. Jekyll 4로 올리는 것, lunr 검색을 Pagefind로 교체하는 것, 빌드를 GitHub Actions로 옮기는 것이 함께 들어갔다. Actions로 옮기면 빌드 안에서 Jekyll 버전을 직접 정할 수 있고, Pagefind 인덱싱 스텝도 그 빌드 뒤에 붙일 수 있기 때문이다.

## Jekyll 4

`github-pages` gem을 제거하고 `jekyll ~> 4.3`을 직접 적었다. 4.4.1이 설치됐다. 로컬 빌드가 71초에서 35초로 줄었다 — 2배 정도. 캐시가 있을 땐 더 빠르다.

옮기면서 `_config.yml`에 남아 있던 `math_engine: katex` 한 줄을 지웠다. 이 줄은 한참 전부터 작동하지 않았다. `kramdown-math-katex` gem이 설치돼 있지 않아 kramdown은 raw `$$...$$`를 그대로 출력하고, KaTeX는 클라이언트에서 `katex.min.js`로 렌더링하고 있었다. 작동하지 않는 설정이지만 표면상 문제가 없어 방치돼 있었고, 옮기는 김에 정리했다.

`vendor/bundle`을 로컬 번들 경로로 지정하고 `.gitignore`에 추가했다. CI에서는 `bundler-cache: true`가 알아서 캐싱을 처리한다.

## Pagefind

기존 lunr 셋업은 한국어에 대해 사실상 망가져 있었다. `assets/js/lunr/lunr-gr.js`가 있었는데, 그 `gr`은 그리스어 stemmer였다. 한국어를 위한 케이스는 어디에도 없었고, lunr-store는 글의 언어를 구분하지 않고 EN/KO를 한 인덱스에 섞어 넣었다. 그래서 `/ko/`에서 검색하면 영어 결과가 같이 나왔다. 아무도 신고하지 않은 걸 보면 검색 자체를 거의 안 쓴 모양이다.

Pagefind는 빌드된 `_site/` 위에서 도는 정적 인덱서이다. HTML 안의 `data-pagefind-body` 속성이 붙은 영역만 인덱싱하므로, `_layouts/single.html`의 `<article>`에 그 속성을 하나 추가했다. 글 layout이 아닌 페이지(아카이브, About 같은 것)는 자동으로 빠진다.

언어 분리는 따로 작업할 게 없었다. Pagefind는 `<html lang>` 속성을 보고 인덱스를 언어별로 자동 분리한다. 이 블로그는 이미 permalink 기반으로 페이지마다 `lang`을 다르게 지정하고 있어서, `/ko/` 페이지의 검색은 한국어 결과만, `/en/`은 영어 결과만 잡는다. lunr에서 직접 구현하려면 store에 lang 필터를 넣고 검색 시 분기해야 했을 일이 자동으로 처리됐다.

CI 빌드에서는 Jekyll build 직후 노드 셋업 → `npm ci` → `npx pagefind --site _site` 순으로 인덱싱이 돈다. 로컬에서는 cargo로 빌드한 네이티브 바이너리(`~/.cargo/bin/pagefind`)를 쓴다. 글 추가 후 로컬에서 즉시 검색에 반영하고 싶을 때 `scripts/reindex-pagefind.sh`를 돌린다. CI가 매 push마다 재인덱싱하므로 평소엔 쓸 일이 없다.

```bash
#!/usr/bin/env bash
set -euo pipefail
REPO="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
"$HOME/.cargo/bin/pagefind" --site "$REPO/_site" --quiet
```
{: data-filename="scripts/reindex-pagefind.sh"}

## 검색 오버레이

Pagefind는 검색 UI도 자체 제공한다(`PagefindUI`). 처음엔 검색 페이지(`/search/`)에 띄워두는 형태였는데, 오른쪽 상단의 돋보기 아이콘에 모달 오버레이로 띄워달라는 지시가 사용자에게서 내려왔다. 검색하려고 페이지를 떠나면 흐름이 끊기기 때문이다.

오버레이 자체는 간단했고, 스타일링이 길었다. PagefindUI는 벤더된 자체 CSS를 가져오는데, 사이트의 색상 토큰과 폰트 크기에 맞추려면 그 CSS 위에 덮어써야 한다. 같은 selector·같은 specificity로 덮어쓰면 로드 순서로 결정되는데, PagefindUI CSS가 항상 나중에 로드되므로 우리 룰이 매번 밀렸다. 결국 input border 제거 같은 핵심 줄은 `!important`로 처리했다. 보통은 피하지만 이 경우엔 다른 방법이 없었다.

```css
.pagefind-ui__search-input {
  border: none !important;
}
```

오버레이는 첫 클릭 시 lazy-mount된다. 검색을 쓰지 않는 페이지뷰가 대부분이므로, 첫 페이지 로드에 PagefindUI를 매번 import할 필요는 없다. 돋보기 아이콘을 처음 누르는 순간 스크립트가 로드되고, 그 다음부터는 캐시된다.

세부 스타일이 며칠에 걸쳐 한 줄씩 들어갔다 — backdrop blur, 카드 보더의 금색 액센트, empty-state 패딩, 모달 카드 padding, input pointer-events 보장. 커밋 로그에 "Search overlay:"로 시작하는 것이 일곱 개쯤 된다. 매번 결과를 보고 다음 한 줄이 정해지는 류라 한 번에 끝낼 수 없는 작업이다. 일곱 개의 커밋 끝에 검색창의 보더가 사라졌다. 위대한 업적은 아니다.

## 결과

빌드는 깨끗하고, 검색은 작동하고, 한국어로 검색할 때 영어 결과가 끼어 나오지 않는다. 빌드 절차를 직접 통제하게 된 부수효과는 다음 작업(예: 빌드 시점에 마크다운에 개입하는 플러그인을 끼울 수 있게 된 것)으로 이어지는데, 그건 별도의 글에서 다룬다.
