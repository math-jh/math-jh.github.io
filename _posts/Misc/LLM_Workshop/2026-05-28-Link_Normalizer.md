---

title: "내부 링크 표시명 자동 보정"
excerpt: "소스는 그대로 두고 빌드 때 교차참조 표시명을 대상 글의 현재 제목·라벨로 다시 조립하는 Jekyll 플러그인"

read_time: false

categories: [Misc / LLM Workshop]
permalink: /ko/llm_workshop/link_normalizer

sidebar:
    nav: "llm_workshop-ko"

author: Marvin

date: 2026-05-28
last_modified_at: 2026-11-02

weight: 11

---

관련 파일: [`_plugins/link_normalizer.rb`](https://github.com/math-jh/math-jh.github.io/blob/main/_plugins/link_normalizer.rb), [`scripts/audit/link_normalizer_run.sh`](https://github.com/math-jh/math-jh.github.io/blob/main/scripts/audit/link_normalizer_run.sh), `scripts/audit/link-overrides.log` (gitignored, 빌드 산물)
{: .notice--info}

이 블로그의 수학 글들은 서로 빽빽하게 링크되어 있다. 다른 글의 정의나 명제를 부를 때 쓰는 형식이 정해져 있고, 대략 이런 모양이다.

```markdown
([\[대수적 위상수학\] §코호몰로지, ⁋따름정리 10](/ko/math/algebraic_topology/cohomology#cor10))
```

`\[카테고리\]`, `§글제목`, `⁋라벨` 세 부분으로 이루어진다. 같은 카테고리 안의 글이면 `\[카테고리\]`를 생략하고, 같은 글 안의 참조는 `[명제 4](#prop4)`처럼 짧아진다. 형식은 LLM이 글을 검토할 때 쓰는 가이드라인에 적혀 있고, 사용자도 글을 쓸 때 이 형식대로 손으로 채운다.

문제는 대상이 바뀌어도 표시명이 따라가지 않는다는 것이다. 어떤 글의 제목이 바뀌면 그 글을 가리키는 다른 글들의 `§제목`이 그 순간 낡고, 라벨 번호가 밀리면 더 심하다. 사람이든 LLM이든 수동 검사로 이것을 전부 잡기는 사실상 불가능하다.

방향은 둘이었다. (a) 소스 markdown을 일괄로 다시 써서 canonical에 맞추거나, (b) 빌드 때 렌더링 결과만 canonical로 덮어쓰고 소스는 그대로 두는 것이다. 사용자는 (b)를 택했다. 소스에는 사람이 어떤 표기를 의도했는지가 남아 있어야 하고, 자동 스크립트가 그것을 매번 덮어쓰면 git diff가 의도 없는 변화로 흐려진다. 빌드 산물은 어차피 매번 새로 만들어지니 거기서 정리하면 된다.

(b)가 가능해진 것은 [Jekyll 4와 Pagefind 검색](/ko/llm_workshop/jekyll4_pagefind)의 부수효과다. GitHub Pages의 기본 빌드는 보안상 사용자 플러그인을 실행하지 않아서 `_plugins/`에 무엇을 넣어도 무시되었다. 빌드를 GitHub Actions로 옮긴 뒤로는 우리 Jekyll 위에서 우리 플러그인이 돈다.

## 빌드 훅과 정본 맵

플러그인은 Jekyll 훅 세 개다. `:site, :pre_render`에서 모든 글을 훑어 정본 맵을 만들고, `:documents, :pre_render`에서 문서마다 아직 markdown인 `doc.content`의 내부 링크 표시 텍스트를 다시 조립하며, `:site, :post_write`에서 감사 로그에 요약 줄을 쓴다. 소스 파일은 그대로이고 메모리의 문서만 바뀐다. Jekyll 4의 `Document#content=`가 글의 `@content`를 늘 바꿔 주지는 않아서, 바뀐 본문은 `instance_variable_set(:@content, …)`으로 직접 넣는다.

세 훅 모두 `Jekyll.env == "production"`일 때만 돈다. 로컬 livereload 서버에서는 저장마다 붙는 비용과 데몬의 재빌드가 감사 로그를 덮어쓰는 일을 피하려고 꺼 둔다. 그래서 dev 서버 미리보기에는 손으로 쓴 표시명이 그대로 보인다.

첫 패스가 만드는 맵은 다섯 개다.

- `title_by_url`: permalink → frontmatter `title`
- `label_by_anchor`: `permalink#prop3` → 본문 `<ins id="prop3">**…**</ins>`의 굵은 글씨
- `h2_by_anchor`: `permalink#슬러그` → `## …` 헤딩 텍스트
- `footnote_anchors`: `[^N]:` 정의에서 만든 `permalink#fn:N` 집합
- `category_by_lang`: 카테고리 슬러그 → 언어별 표시 이름

라벨 맵은 훅 순서에 기대고 있다. 지금 수학 글의 정리 박스는 소스에서 `:::` 블록으로 쓰고, `fenced_theorem_blocks.rb`가 이것을 `<ins id>` HTML로 바꾼다. 그 변환기가 같은 `:site, :pre_render`에 `PRIORITY_MAP[:high]`로 등록되어 있어서, 보통 우선순위인 이 플러그인이 맵을 만들 때는 본문에 이미 `<ins id>`가 있다. 순서가 뒤집히면 `:::`로 쓴 글의 라벨이 맵에서 전부 빠진다.

카테고리 표시 이름은 `_data/categories.yml`의 `subjects`에서 파생한다.

```ruby
def build_category_map(site)
  subjects = (site.data["categories"] || {})["subjects"] || {}
  subjects.each do |key, meta|
    en_name = key.to_s.split(" / ").last.to_s.strip
    next if en_name.empty?
    slug = en_name.downcase.gsub(/[^a-z0-9]+/, "_").gsub(/\A_|_\z/, "")
    @category_by_lang["en"][slug] = en_name
    ko_name = meta.is_a?(Hash) ? (meta["ko"] || "").to_s.strip : ""
    @category_by_lang["ko"][slug] = ko_name unless ko_name.empty?
  end
end
```
{: data-filename="_plugins/link_normalizer.rb"}

키 `"Math / Algebraic Topology"`의 `" / "` 뒤가 EN 이름, `ko` 필드가 KO 이름이고, URL 슬러그는 EN 이름의 비영숫자를 `_`로 접어 얻는다. 처음에는 이 맵을 네비게이션 데이터에서 만들었는데, 7월 10일 사이드바 정리로 그 데이터의 모양이 바뀌자 맵이 빈 채로 만들어져 cross-category 링크의 `\[대수기하\]` 브래킷이 전부 탈락했다. 빈 맵은 카테고리를 가진 링크가 하나도 없는 상태와 구별되지 않아서 에러도 없었다. 네비게이션은 표시 순서를 정하는 파일이고, 이름의 정본은 `categories.yml`이다.

## 표시 텍스트의 재조립

링크는 정규식 하나로 잡는다.

```ruby
LINK_RE = /\[((?:[^\[\]]|\\\[|\\\])*?)\]\(((?:\/(?:ko|en)\/|#)[^\s)]*)\)/
```
{: data-filename="_plugins/link_normalizer.rb"}

표시 텍스트 안의 대괄호는 이스케이프된 `\[`·`\]`만 허용하고, URL은 `/ko/`·`/en/`로 시작하는 내부 경로나 같은 글 앵커(`#…`)만 받는다. 외부 링크는 처음부터 걸리지 않는다.

표시 텍스트의 꼴은 여덟 가지(`\[Category\]` 유무 × 꼬리 `⁋Label`·`§§H2`·없음, 같은 글 안의 `Label N`, 표지 없는 plain term)이지만, 코드가 실제로 보는 것은 표지 네 개(`\[`, `§`, `§§`, `⁋`)의 유무다. 원래 있던 표지에 맞춰 조각을 다시 쌓는다.

```ruby
pieces = []
if has_cat && cat_name && !same_cat
  pieces << "\\[#{cat_name}\\]"
end
if has_section
  pieces << "§#{target_title}"
elsif !has_cat && !has_label && !has_h2
  pieces << target_title
end

if has_h2 && h2_text
  pieces << target_title if pieces.empty?
  pieces[-1] = "#{pieces[-1]}, §§#{h2_text}"
elsif has_label && label_text
  pieces << target_title if pieces.empty?
  pieces[-1] = "#{pieces[-1]}, ⁋#{label_text}"
end
```
{: data-filename="_plugins/link_normalizer.rb"}

카테고리 브래킷은 소스에 있었고 두 글의 카테고리가 다를 때만 남는다. `§` 뒤는 대상 글의 현재 `title`로, `⁋` 뒤는 라벨 맵의 텍스트로 바뀐다. 표지가 없는 링크는 대상이 글이면 그 제목으로, 카테고리 랜딩 페이지(`/ko/set_theory`)면 카테고리 이름으로 통째로 바뀐다. `[이전 글](…)`도 배포본에서는 대상 글의 제목이 된다.

`§§` 섹션 링크는 앵커를 kramdown의 `auto_ids`와 같은 규칙으로 슬러그화해서 맞춘다. `## 극한의 보편성질`이 `#극한의-보편성질`이 되는 규칙이다.

```ruby
def kramdown_slug(text)
  s = text.dup
  s.gsub!(/[^[:alnum:][:space:]一-鿿가-힯\-]+/, "")
  s.strip!
  s.gsub!(/\s+/, "-")
  s.downcase!
  s
end
```
{: data-filename="_plugins/link_normalizer.rb"}

한글 음절과 한자를 살리고 나머지 구두점을 떨군 뒤, 공백을 `-`로 바꾸고 소문자로 통일한다. 첫 패스가 모든 `## ` 줄을 이 슬러그로 맵에 넣어 두고, 앵커가 맞으면 표시명을 헤딩의 정확한 텍스트로 덮어쓴다.

같은 글 안의 `[명제 4](#prop4)`는 자기 글의 맵에서 `#prop4`를 찾아 그 `<ins>`의 굵은 글씨로 덮어쓴다. `::: proposition 명제 5 {#prop-def3}` 같은 명시형 박스처럼 id와 번호가 따로 노는 경우에도 표시명은 지금 그 id에 붙은 라벨을 따른다. 같은 글 안에서 앵커를 못 찾으면 아무것도 바꾸지 않는다.

각주는 대상 글의 `[^N]:` 정의로 판정한다. 링크가 살아 있는 `#fn:N`을 가리키면 작성자가 쓴 `, 각주 N` 꼬리를 원문 그대로 붙여 둔다. 덧붙일 정본 텍스트가 없기 때문이다. 없어진 각주를 가리키면 꼬리를 떼고 따로 태그해서, 라벨이나 H2 앵커가 깨진 경우와 구분되게 남긴다.

## 코드 블록 마스킹

LLM Workshop 글은 링크 문법 자체를 예시로 적는 일이 잦다. 이 글 첫머리의 인용 예시도 그렇다. `LINK_RE`가 코드 블록 안까지 보면 그 예시가 실제 링크로 취급되어, 배포본에서는 `⁋따름정리 10 (Künneth)`로 고쳐 나가고 감사 로그에도 오른다. 그래서 치환 전에 코드를 통째로 빼낸다.

```ruby
def mask_code(content)
  stash = []
  out = +""
  fence = nil
  content.each_line do |line|
    opens = line.match(/\A[ \t]{0,3}(`{3,}|~{3,})/)
    if fence || opens
      nl = line.end_with?("\n") ? "\n" : ""
      stash << line.chomp("\n")
      out << "\x00LNMASK#{stash.size - 1}\x00#{nl}"
      if fence
        fence = nil if line.chomp =~ /\A[ \t]{0,3}(`{3,}|~{3,})[ \t]*\z/ &&
                       line.lstrip[0] == fence
      else
        fence = opens[1][0]
      end
    else
      out << line.gsub(/`[^`\n]+`/) do |code|
        stash << code
        "\x00LNMASK#{stash.size - 1}\x00"
      end
    end
  end
  [out, stash]
end
```
{: data-filename="_plugins/link_normalizer.rb"}

펜스 블록은 여는 줄부터 같은 문자(백틱이나 물결표)로 닫는 줄까지 줄 단위로, 인라인 코드는 백틱 쌍 단위로 자리표시자에 넣어 두고, 치환이 끝나면 `unmask_code`가 되돌린다. 자리표시자를 NUL로 감싼 것은 본문에 나올 수 없는 바이트라서 마스크 경계가 본문과 부딪히지 않기 때문이다. 마스킹된 구간은 `LINK_RE`가 아예 보지 못하므로 고쳐지지도, 감사에 기록되지도 않는다.

## 감사 로그의 버킷

소스의 표시명과 canonical이 다르면 그 차이를 분류해서 `scripts/audit/link-overrides.log`에 한 줄에 JSON 하나씩 적는다. 이 파일은 빌드마다 처음부터 다시 쓰인다.

```json
{"source":"...","url":"...","original":"...","canonical":"...","bucket":"cosmetic/label-enrich"}
```

버킷은 이렇다.

- **cosmetic/label-enrich**: canonical에 괄호 부연이 붙었다(`명제 3` → `명제 3 (Riemann–Roch for surfaces)`). 플러그인이 제 일을 하는 중이다.
- **cosmetic/label-trim**: 소스 쪽 괄호를 canonical이 잘라냈다. `Proposition 6 (1)`의 `(1)`처럼 사람이 넣은 정보일 수 있으니 한 번 봐야 한다.
- **cosmetic/same-cat-omit**: 같은 카테고리라서 브래킷을 뗐다. 무해하다.
- **title-drift**: 대상의 제목·카테고리 이름·섹션명·라벨이 바뀌었다(`section-renamed`, `category-renamed`, `label-renamed`). 대상 글에서 사라진 각주는 `footnote-stripped`로 따로 센다. 소스를 고칠 대상이다.
- **anchor-dropped**: 다른 글의 앵커(`#prop8` 등)가 없어져 `⁋` 꼬리를 뗐다. 배포본은 글 단위 링크로 살아남지만 수정은 소스에서 해야 한다.

분류는 문자열 비교다. 앞의 `\[…\]`와 뒤의 `, ⁋…`·`, §§…`·`, 각주 …` 꼬리를 떼어 따로 비교하고, 한쪽이 괄호만 더한 꼴이면 cosmetic, 아니면 title-drift로 보낸다. 표지 없는 링크가 대상 제목으로 바뀐 것도 여기서는 `section-renamed`로 떨어지므로, 그 숫자가 전부 낡은 소스는 아니다.

빌드 끝에는 버킷별 개수를 담은 summary 줄이 붙는다. 첫날 버킷 분류를 붙이고 돌린 빌드에서는 463건 중 459건이 label-enrich였고, 소스를 살펴볼 것은 각주 2건과 깨진 앵커 2건이었다.

CI가 남기는 로그는 배포와 함께 버려지므로, 매일 04:30 크론이 `link_normalizer_run.sh`로 로컬 프로덕션 빌드를 한 번 따로 돌린다. 출력은 `/var/tmp`의 일회용 디렉토리로 보낸다. 이 Pi의 `/tmp`는 RAM 위의 tmpfs이고 `_site` 전체는 700MB쯤 된다. 끝나면 summary 줄에 시각을 붙여 `link_normalizer.log`에 이어 쓰고, 대시보드의 "링크 정규화 감사" 워커가 이 파일을 본다. 11월 2일 새벽의 줄은 1,701건 중 label-enrich가 1,564건이었다. 422줄로 자란 플러그인이 하는 일의 9할은 여전히 괄호를 더하는 것이다.
