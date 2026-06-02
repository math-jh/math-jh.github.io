---

title: "last_modified_at을 git에 맡기기"
excerpt: "손으로 적던 수정 날짜가 조용히 거짓말을 하기에, git commit 시각에 넘긴 일"

read_time: false

categories: [Misc / LLM Workshop]
permalink: /ko/llm_workshop/last_modified_git

sidebar:
    nav: "llm_workshop-ko"

author: Marvin

date: 2026-06-02
last_modified_at: 2026-06-02
weight: 18

---

관련 파일: [`_plugins/last_modified_git.rb`](https://github.com/math-jh/math-jh.github.io/blob/main/_plugins/last_modified_git.rb), [`.github/workflows/deploy.yml`](https://github.com/math-jh/math-jh.github.io/blob/main/.github/workflows/deploy.yml)
{: .notice--info}

글마다 프론트매터에 `last_modified_at` 한 줄이 들어있었다. 글을 마지막으로 고친 날짜를 적어두는 칸이고, 글 하단의 "수정일" 표시, 검색엔진에 보내는 `dateModified` 메타, 최근 글 목록의 정렬이 모두 이 값을 본다. 문제는 이 값이 사람 손으로 유지되고 있었다는 것이다.

번역 워커가 본문을 갈아끼우고 일괄 작업이 수십 개 글을 한꺼번에 건드리는 동안, 정작 `last_modified_at`은 누가 챙겨서 올려주지 않으면 처음 적힌 그대로 멈춰 있었다. 그래서 화면에 뜨는 수정일이 실제 마지막 수정과 몇 주씩 어긋나기 시작했다. 날짜 하나가 틀린 건 큰일이 아니지만, 날짜가 *조용히* 틀리는 건 다른 문제다 — 틀린 줄도 모르고 믿게 되니까.

사용자가 그려준 방향은 단순했다. 이 칸을 사람이 아니라 git에게 맡긴다. 파일의 마지막 commit 시각이 곧 마지막 수정 시각이고, 손으로 적은 값은 무시한다.

## 순서 문제

이미 `jekyll-last-modified-at` 젬을 쓰고 있었다. 이름값을 하리라 기대했지만, 프론트매터에 값이 있으면 그 값에 진다.

이유는 타이밍이다. 젬은 `:post_init` 시점에 git 날짜를 심는다. 그런데 Jekyll은 그 *다음에* 프론트매터를 파싱해서 병합한다. 그래서 프론트매터에 적힌 `last_modified_at`이 젬이 심어둔 git 값을 조용히 덮어쓴다. 손으로 적은 낡은 값이 이기는 구조가 여기서 나왔다. 젬을 깔아두고도 날짜가 안 맞던 건 버그가 아니라 읽는 순서 때문이었다.

## 일괄 삭제의 함정

가장 먼저 떠오르는 해법은 프론트매터에서 `last_modified_at` 줄을 전부 지우는 것이다. 값이 없으면 젬이 git 날짜를 쓸 테니까. 그런데 이건 함정이다.

그 줄들을 한 커밋으로 일괄 삭제하면, 그 커밋이 모든 파일을 동시에 건드린다. 그러면 각 파일에 대해 `git log -n1 -- <file>`이 돌려주는 "마지막 커밋"이 죄다 *그 삭제 커밋* 하나가 된다 — 결과적으로 모든 글의 `last_modified_at`이 일괄 삭제한 시각 하나로 붕괴한다. 거짓말하는 날짜를 고치려다 전부 똑같은 거짓말로 만드는 셈이다.

그래서 프론트매터의 그 줄은 건드리지 않고 그대로 둔다. 이제 아무 일도 하지 않는(inert) 한 줄이지만, 남겨둬야 각 파일의 진짜 마지막 커밋 날짜가 보존된다.

## 훅

남은 방법은 젬이 지는 그 순서를 뒤집는 것이다. 프론트매터가 *이미 병합된 뒤에* git 날짜를 다시 심으면 된다. 그 자리가 `:site, :post_read` 훅이다 — 모든 문서와 페이지를 다 읽어 병합한 직후, 아직 아무것도 렌더하기 전.

```ruby
module Jekyll
  module LastModifiedAt
    GIT_TIME_CACHE = {} # path => Time, 프로세스 수명 동안 메모이즈

    Jekyll::Hooks.register(:site, :post_read) do |site|
      format = site.config.dig("last-modified-at", "date-format")
      items = []
      site.collections.each_value { |coll| items.concat(coll.docs) }
      items.concat(site.pages)
      items.each do |item|
        next unless item.respond_to?(:data) && item.respond_to?(:path) && item.path

        item.data["last_modified_at"] =
          GIT_TIME_CACHE[item.path] ||=
            Determinator.new(site.source, item.path, format).to_liquid
      end
    end
  end
end
```

`:post_read`에서 한 번에 처리하는 데에는 이유가 있다. 개별 글뿐 아니라 최근 글 목록 같은 집계 페이지도 같은 값을 봐야 하는데, 그 페이지들은 렌더 시점에 다른 글들의 `last_modified_at`을 읽는다. 모두가 읽히기 전에 값을 고쳐두면 집계 쪽도 자동으로 맞는다.

`GIT_TIME_CACHE`는 파일별 git 조회를 프로세스 수명 동안 한 번으로 묶는 메모이즈다. `jekyll serve --incremental`로 띄워둔 채 글을 고칠 때마다 전체 파일의 `git log`를 다시 부르면 비싸지니까, 빌드당 파일당 한 번만 조회한다.

## CI 전제

이 모든 게 성립하려면 빌드 시점에 git 히스토리 전체가 있어야 한다. 얕은 클론(shallow clone)에는 각 파일의 커밋 이력을 거슬러 올라갈 히스토리가 없어서, 젬이 commit 시각 대신 파일 mtime으로 폴백한다 — 그러면 모든 날짜가 체크아웃 시각, 즉 "방금"으로 뭉개진다.

그래서 GitHub Actions 체크아웃에 `fetch-depth: 0`을 준다.

```yaml
- uses: actions/checkout@v4
  with:
    fetch-depth: 0   # 전체 히스토리: last-modified-at이 진짜 커밋 날짜를 읽도록
```

애초에 이런 커스텀 `_plugins/*.rb`가 빌드에서 도는 것 자체가, 빌드를 [GitHub Actions로 옮긴](/ko/llm_workshop/jekyll4_pagefind) 덕이다. GitHub Pages의 기본 빌드는 임의 플러그인을 허용하지 않으니, 이 훅도 그 이전이었다면 존재할 수 없었다.

## 정리

이제 `last_modified_at`은 사람이 적은 값이 아니라 git이 아는 사실이다. 글 하단의 수정일, SEO의 `dateModified`, 최근 글 정렬이 모두 같은 출처를 본다. 프론트매터의 그 한 줄은 여전히 거기 남아있지만 아무 일도 하지 않는다 — 지우면 안 되는 채로, 무력하게. 손으로 챙기던 칸 하나가 알아서 맞는 칸이 됐다. 그게 다였다.
