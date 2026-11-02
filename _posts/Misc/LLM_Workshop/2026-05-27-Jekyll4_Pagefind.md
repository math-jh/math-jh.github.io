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
last_modified_at: 2026-11-02
weight: 9

---

관련 파일: [`.github/workflows/build-deploy.yml`](https://github.com/math-jh/math-jh.github.io/blob/main/.github/workflows/build-deploy.yml), [`Gemfile`](https://github.com/math-jh/math-jh.github.io/blob/main/Gemfile), [`_includes/search/pagefind-search-scripts.html`](https://github.com/math-jh/math-jh.github.io/blob/main/_includes/search/pagefind-search-scripts.html), [`scripts/reindex-pagefind.sh`](https://github.com/math-jh/math-jh.github.io/blob/main/scripts/reindex-pagefind.sh)
{: .notice--info}

이 블로그는 처음 만들어진 이후 줄곧 GitHub Pages의 기본 빌드 위에서 돌았다. 푸시하면 GitHub이 Jekyll로 빌드해서 띄워주는 흐름이다. 편하지만 두 가지 비용이 있었다. Jekyll이 3.x에 묶여 있었고(github-pages gem이 4.x 출시 후로도 한참 3.x를 핀했다), 빌드 절차에 끼어들 수 없었다.

전환은 한 커밋에 묶였다 ([c163cc35](https://github.com/math-jh/math-jh.github.io/commit/c163cc35)). Jekyll 4로 올리는 것, lunr 검색을 Pagefind로 교체하는 것, 빌드를 GitHub Actions로 옮기는 것이 함께 들어갔다. Actions로 옮기면 빌드 안에서 Jekyll 버전을 직접 정할 수 있고, Pagefind 인덱싱 스텝도 그 빌드 뒤에 붙일 수 있기 때문이다.

## Jekyll 4와 Actions 빌드

`github-pages` gem을 제거하고 `jekyll ~> 4.3`을 직접 적었다. 4.4.1이 설치됐고, 로컬 빌드가 71초에서 35초로 2배쯤 빨라졌다.

옮기면서 `_config.yml`에 남아 있던 `math_engine: katex` 한 줄을 지웠다. 이 줄은 한참 전부터 작동하지 않았다. `kramdown-math-katex` gem이 설치돼 있지 않아 kramdown은 raw `$$...$$`를 그대로 출력하고, KaTeX는 클라이언트에서 `katex.min.js`로 렌더링하고 있었다. 표면상 문제가 없어 방치돼 있던 설정이다. 번들은 로컬에서 `vendor/bundle`에 깔고(`.gitignore`에 추가), CI에서는 `bundler-cache: true`가 캐싱을 맡는다.

워크플로는 Ruby와 Node를 준비하고 `npm ci`로 Pagefind와 썸네일 생성기를 깐 뒤, 홈 타일 생성, `jekyll build`, `npx pagefind --site _site` 순으로 돌아 `_site`를 Pages에 올린다. 빌드를 직접 돌리게 되면서 GitHub Pages 기본 빌드가 무시하던 `_plugins/`의 자체 플러그인도 돈다.

## 언어별로 갈리는 Pagefind 색인

기존 lunr 셋업은 한국어에 대해 사실상 망가져 있었다. `assets/js/lunr/lunr-gr.js`가 있었는데, 그 `gr`은 그리스어 stemmer였다. 한국어를 위한 케이스는 어디에도 없었고, lunr-store는 글의 언어를 구분하지 않고 EN/KO를 한 인덱스에 섞어 넣었다. 그래서 `/ko/`에서 검색하면 영어 결과가 같이 나왔다. 아무도 신고하지 않은 걸 보면 검색 자체를 거의 안 쓴 모양이다.

Pagefind는 빌드된 `_site/` 위에서 도는 정적 인덱서다. `data-pagefind-body` 속성이 붙은 영역만 인덱싱하므로, `_layouts/single.html`의 `<article>`에 그 속성을 붙였다. 글 layout이 아닌 페이지(아카이브, About 같은 것)는 자동으로 빠진다.

언어 분리는 따로 작업할 게 없었다. Pagefind는 `<html lang>` 속성을 보고 인덱스를 언어별로 나누는데, 이 블로그는 이미 permalink 기반으로 페이지마다 `lang`을 지정하고 있었다. 그래서 `/ko/` 페이지의 검색은 한국어 결과만, `/en/`은 영어 결과만 잡는다. lunr였다면 store에 lang 필터를 넣고 검색 시 분기해야 했을 일이다.

로컬 미리보기의 색인은 Pi가 따로 만든다. CI의 x86 러너에서는 npm의 Pagefind로 충분하지만, Pi 5는 16KB 페이지 커널이라 npm 배포판이 jemalloc 페이지 크기 불일치로 죽는다. 그래서 cargo로 직접 빌드한 바이너리를 쓰고, 크론이 매일 04:50 이 스크립트로 `_site/pagefind/`를 다시 만든다. Jekyll 리빌드가 이 디렉토리를 지우지 않도록 `_config.yml`의 `keep_files`에 `pagefind`를 넣어 두었다.

```bash
REPO="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
# Clean previous index fragments to avoid unbounded accumulation
rm -rf "$REPO/_site/pagefind"

"${CARGO_HOME:-$HOME/.local/share/cargo}/bin/pagefind" --site "$REPO/_site" --quiet
```
{: data-filename="scripts/reindex-pagefind.sh"}

바이너리 경로는 한참 뒤 홈 디렉토리를 정리하면서 바뀌었다.

> 이 Pi의 홈 디렉터리에 .으로 시작하는 폴더가 너무 많은데 꾹 참고 써야하나?

죽은 폴더는 지우고 남는 것들은 환경변수로 줄일 수 있는 만큼 줄이라는 것이 사용자의 결론이었고, 그 정리에서 `~/.cargo`가 `~/.local/share/cargo`로 옮겨졌다. 크론은 `.bashrc`를 읽지 않으므로 스크립트는 `CARGO_HOME`이 없어도 새 기본 경로로 떨어지게 기본값을 인라인한다. 크론 줄은 출력을 버리기 때문에, 이 경로가 틀리면 에러 하나 없이 로컬 검색이 옛 색인에 머문다.

## 돋보기 아이콘의 검색 오버레이

Pagefind는 검색 UI도 자체 제공한다(`PagefindUI`). 처음엔 검색 페이지(`/search/`)에 띄워두는 형태였는데, 사용자는 오른쪽 상단의 돋보기 아이콘에서 모달 오버레이로 뜨기를 원했다. 검색하려고 페이지를 떠나면 흐름이 끊기기 때문이다.

오버레이 자체는 간단했고, 스타일링이 길었다. PagefindUI는 벤더된 자체 CSS를 가져오는데, 그 선택자(`.pagefind-ui__search-input.svelte-XXXX`)는 우리 규칙과 명시도가 같고 항상 나중에 로드된다. 같은 명시도면 로드 순서로 결정되니 우리 규칙이 매번 밀렸다. 그래서 입력창의 테두리·배경·그림자를 지우는 줄은 `!important`로 처리했다. 보통은 피하지만 이 경우엔 다른 방법이 없었다.

```scss
.pagefind-ui {
  .pagefind-ui__search-input {
    background: transparent !important;
    border: none !important;
    box-shadow: none !important;
    &:focus { outline: none !important; box-shadow: none !important; }
  }
}
```
{: data-filename="_sass/_pagefind-overrides.scss"}

`pagefind-ui.js`는 페이지와 함께 받지만, `PagefindUI` 인스턴스는 돋보기를 처음 누를 때 만든다. 숨겨진 오버레이에 페이지 로드 때 마운트하면 마스트헤드의 오버레이 상태와 부딪쳐 빈 팝업이 남을 수 있었다.

세부 스타일은 그날 오후 한 시간 남짓 동안 한 줄씩 들어갔다. backdrop blur, 카드 테두리의 금색 액센트, empty-state 패딩, input pointer-events 보장이 차례로 붙어 `Search overlay:`로 시작하는 커밋이 여섯 개 남았다. 매번 결과를 보고 다음 한 줄이 정해지는 류라 한 번에 끝낼 수 없는 작업이다. 여섯 개의 커밋 끝에 검색창의 보더가 사라졌다. 위대한 업적은 아니다.
