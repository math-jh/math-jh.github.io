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

weight: 11
group: backend

---

관련 파일: [`_plugins/link_normalizer.rb`](https://github.com/math-jh/math-jh.github.io/blob/main/_plugins/link_normalizer.rb), [`scripts/audit/link_normalizer_run.sh`](https://github.com/math-jh/math-jh.github.io/blob/main/scripts/audit/link_normalizer_run.sh), `scripts/audit/link-overrides.log` (gitignored, 빌드 산물)
{: .notice--info}

이 블로그의 수학 글들은 서로 빽빽하게 링크되어 있다. 다른 글의 정의나 명제를 부를 때 쓰는 형식이 정해져 있고, 대략 이런 모양이다.

```markdown
([\[대수적 위상수학\] §코호몰로지, ⁋따름정리 10](/ko/math/algebraic_topology/cohomology#cor10))
```
{: data-filename="수학 글의 교차참조 · 형식 예시"}

`\[카테고리\]`, `§글제목`, `⁋라벨` 세 부분으로 이루어진다. 같은 카테고리 안의 글이면 `\[카테고리\]`를 생략하고, 같은 글 안의 참조는 `[명제 4](#prop4)`처럼 짧아진다. 형식은 LLM이 글을 검토할 때 쓰는 가이드라인에 적혀 있고, 사용자도 글을 쓸 때 이 형식대로 손으로 채운다.

문제는 대상이 바뀌어도 표시명이 따라가지 않는다는 것이다. 어떤 글의 제목이 바뀌면 그 글을 가리키는 다른 글들의 `§제목`이 그 순간 낡고, 라벨 번호가 밀리면 더 심하다. 사람이든 LLM이든 수동 검사로 이것을 전부 잡기는 사실상 불가능하다.

방향은 둘이었다. (a) 소스 markdown을 일괄로 다시 써서 canonical에 맞추거나, (b) 빌드 때 렌더링 결과만 canonical로 덮어쓰고 소스는 그대로 두는 것이다. 사용자는 (b)를 택했다. 소스에는 사람이 어떤 표기를 의도했는지가 남아 있어야 하고, 자동 스크립트가 그것을 매번 덮어쓰면 git diff가 의도 없는 변화로 흐려진다. 빌드 산물은 어차피 매번 새로 만들어지니 거기서 정리하면 된다.

(b)가 가능해진 것은 [Jekyll 4와 Pagefind 검색](/ko/llm_workshop/jekyll4_pagefind)의 부수효과다. GitHub Pages의 기본 빌드는 보안상 사용자 플러그인을 실행하지 않아서 `_plugins/`에 무엇을 넣어도 무시되었다. 빌드를 GitHub Actions로 옮긴 뒤로는 우리 Jekyll 위에서 우리 플러그인이 돈다.

## 빌드 훅과 정본 맵

플러그인은 Jekyll 훅 세 개다. 

```ruby
Jekyll::Hooks.register :site, :pre_render do |site|
  next unless Jekyll.env == "production"

  LinkNormalizer.maps = LinkNormalizer::Maps.new(site)

  tracker_path = File.join(site.source, LinkNormalizer::TRACKER_REL)
  FileUtils.mkdir_p(File.dirname(tracker_path))
  LinkNormalizer.tracker_io = File.open(tracker_path, "w")
  LinkNormalizer.bucket_counts = Hash.new(0)
end

Jekyll::Hooks.register :documents, :pre_render do |doc|
  next unless Jekyll.env == "production"
  next unless doc.url =~ %r{\A/(ko|en)/}
  next unless doc.content.is_a?(String)
  new_content, diffs = LinkNormalizer.normalize(doc.content, doc.relative_path, doc.url)
  doc.instance_variable_set(:@content, new_content) unless diffs.empty?
  diffs.each do |d|
    LinkNormalizer.bucket_counts[d["bucket"]] += 1
    LinkNormalizer.tracker_io.puts JSON.generate(d) rescue nil
  end
end

Jekyll::Hooks.register :site, :post_write do |_site|
  next unless Jekyll.env == "production"
  io = LinkNormalizer.tracker_io
  counts = LinkNormalizer.bucket_counts || {}
  if io
    total = counts.values.sum
    summary = { "summary" => true, "total" => total }
    # ...
    io.puts JSON.generate(summary) rescue nil
    io.close
  end
  LinkNormalizer.tracker_io = nil
  LinkNormalizer.bucket_counts = nil
end
```
{: data-filename="_plugins/link_normalizer.rb · 일부 생략, 주석 생략"}

Jekyll은 소스를 전부 읽어 글마다 문서 객체를 만든 뒤, 렌더를 시작하기 전에 `:site, :pre_render`를 한 번 부른다. 첫 훅은 여기서 맵을 만들고 감사 로그를 `"w"`로 열어 지난 빌드의 내용을 비운다. 렌더 단계에서 Jekyll은 문서마다 `:documents, :pre_render`를 먼저 부르고, 그 뒤에 Liquid를 처리하고 markdown을 HTML로 바꾼다. 그래서 둘째 훅이 받는 `doc.content`는 front matter를 뗀 markdown 본문이고, 정규식이 링크 문법 `[…](…)`을 그대로 찾을 수 있다. 이 본문은 Jekyll이 파일에서 읽어 메모리에 올린 사본이다. 표시명을 고친 새 본문을 문서의 `@content`에 넣으면 이어지는 변환은 새 본문으로 진행되고, 디스크의 `.md`는 그대로 남는다. 고친 링크마다 감사 로그에 JSON 한 줄을 쓰고, 그 링크의 버킷(아래 감사 로그 절의 분류) 개수를 하나 올린다. `_site/`에 파일을 다 쓴 뒤 부르는 `:site, :post_write`에서 셋째 훅이 버킷별 개수를 요약 줄로 붙이고 로그를 닫는다. 생략한 줄은 버킷 이름을 하나씩 돌며 개수를 요약에 옮기는 부분이다.

세 훅 모두 `Jekyll.env == "production"`일 때만 돈다. 로컬 livereload 서버에서는 저장마다 붙는 비용과 데몬의 재빌드가 감사 로그를 덮어쓰는 일을 피하려고 꺼 둔다. 그래서 dev 서버 미리보기에는 손으로 쓴 표시명이 그대로 보인다.

첫 패스가 만드는 맵은 다섯 개다.

- `title_by_url`: permalink → frontmatter `title`
- `label_by_anchor`: `permalink#prop3` → 본문 `<ins id="prop3">**…**</ins>`의 굵은 글씨
- `h2_by_anchor`: `permalink#슬러그` → `## …` 헤딩 텍스트
- `footnote_anchors`: `[^N]:` 정의에서 만든 `permalink#fn:N` 집합
- `category_by_lang`: 카테고리 슬러그 → 언어별 표시 이름

라벨 맵은 훅 순서에 기댄다. 수학 글의 정리 박스는 소스에서 `:::` 블록으로 쓰고, 맵이 읽는 `<ins id>` HTML은 `fenced_theorem_blocks.rb`가 빌드 중에 만든다. ([fenced-div 정리 박스와 전처리 플러그인](/ko/llm_workshop/fenced_theorem_blocks)) 그 변환기가 같은 `:site, :pre_render`에 `PRIORITY_MAP[:high]`로 등록되어 있어서, 보통 우선순위인 이 플러그인이 맵을 만들 때는 본문에 이미 `<ins id>`가 있다. 순서가 뒤집히면 `:::`로 쓴 글의 라벨이 맵에서 전부 빠진다.

카테고리 표시 이름은 `_data/categories.yml`의 `subjects`에서 만든다. `subjects`를 읽지 못하면 맵이 빈 채로 만들어져 cross-category 링크의 `\[대수기하\]` 브래킷이 전부 탈락하는데, 빈 맵은 카테고리를 가진 링크가 하나도 없는 상태와 구별되지 않아서 에러도 나지 않는다. 맵을 만드는 코드가 아래다.

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
{: data-filename="_plugins/link_normalizer.rb · 일부 발췌"}

`subjects`의 키마다 `" / "` 뒤를 EN 이름으로 뗀다(`"Math / Algebraic Topology"` → `Algebraic Topology`). URL 슬러그는 이 이름을 소문자로 바꾸고, 영숫자가 아닌 글자 묶음(`[^a-z0-9]+`)을 `_` 하나로 접은 뒤 앞뒤에 남은 `_`(`\A_|_\z`)를 지워 얻는다. 그래서 `algebraic_topology`가 되어 URL의 카테고리 조각과 맞는다. KO 이름은 항목의 `ko` 필드이고, 그 필드가 없으면 KO 맵에는 넣지 않는다.

## 표시 텍스트의 재조립

링크는 정규식 하나로 잡는다.

```ruby
LINK_RE = /\[((?:[^\[\]]|\\\[|\\\])*?)\]\(((?:\/(?:ko|en)\/|#)[^\s)]*)\)/
```
{: data-filename="_plugins/link_normalizer.rb · 일부 발췌"}

첫째 괄호 `((?:[^\[\]]|\\\[|\\\])*?)`가 표시 텍스트다. 대괄호가 아닌 글자이거나 이스케이프된 `\[`·`\]`인 것만 모으므로, `\[대수적 위상수학\]`처럼 이스케이프한 카테고리 브래킷은 표시 텍스트 안에 남고, 맨 대괄호는 넘지 못하므로 표시 텍스트는 `](`가 나오는 자리에서 끝난다. 둘째 괄호 `((?:\/(?:ko|en)\/|#)[^\s)]*)`가 URL로, `/ko/`·`/en/`이나 `#`으로 시작해 공백이나 닫는 괄호 앞까지다. 그래서 내부 경로와 같은 글 앵커(`#…`)만 잡히고, 외부 링크는 이 시작 조건에서 처음부터 빠진다.

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
elsif anchor&.start_with?("fn:") && maps.footnote_anchors["#{url_path}##{anchor}"]
  # ...
end
```
{: data-filename="_plugins/link_normalizer.rb · 일부 생략, 주석 한 줄 뺌"}

맨 앞의 카테고리 브래킷은 소스에 있었고 두 글의 카테고리가 다를 때만 넣는다. 다음 조각은 `§`가 있었으면 대상 글의 현재 `title`이고, 표지가 하나도 없었으면 그 제목만이다. 꼬리는 마지막 조각 뒤에 쉼표로 붙인다. `§§` 뒤는 헤딩 맵의 텍스트로, `⁋` 뒤는 라벨 맵의 텍스트로 바뀌고, 앞에 붙일 조각이 없으면 제목을 먼저 넣는다. 그래서 표지가 없는 링크는 대상 글의 제목으로 통째로 바뀐다. 대상이 카테고리 랜딩 페이지(`/ko/set_theory`)이면 이 조립까지 가지 않고, 그 앞에서 카테고리 이름으로 바뀐다. `[이전 글](…)`도 배포본에서는 대상 글의 제목이 된다. 생략한 마지막 갈래는 아래의 각주 처리다.

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
{: data-filename="_plugins/link_normalizer.rb · 일부 발췌"}

한글 음절과 한자를 살리고 나머지 구두점을 떨군 뒤, 공백을 `-`로 바꾸고 소문자로 통일한다. 첫 패스가 모든 `## ` 줄을 이 슬러그로 맵에 넣어 두고, 앵커가 맞으면 표시명을 헤딩의 정확한 텍스트로 덮어쓴다.

같은 글 안의 `[명제 4](#prop4)`는 자기 글의 맵에서 `#prop4`를 찾아 그 `<ins>`의 굵은 글씨로 덮어쓴다. `::: proposition 명제 5 {#prop-def3}` 같은 명시형 박스처럼 id와 번호가 따로 노는 경우에도 표시명은 지금 그 id에 붙은 라벨을 따른다. 같은 글 안에서 앵커를 못 찾으면 아무것도 바꾸지 않는다.

각주 링크는 대상 글의 `[^N]:` 정의로 판정한다. 링크가 살아 있는 `#fn:N`을 가리키면 작성자가 쓴 `, 각주 N` 꼬리를 원문 그대로 붙여 둔다. 덧붙일 정본 텍스트가 없기 때문이다. 없어진 각주를 가리킬 때만 꼬리를 떼고 `footnote-stripped`로 따로 태그해서, 라벨이나 H2 앵커가 깨진 경우와 구분되게 남긴다.

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
{: data-filename="_plugins/link_normalizer.rb · 일부 발췌"}

본문을 한 줄씩 읽으며, 여는 펜스를 만나면 그 줄부터 닫는 펜스까지를 줄 단위로 자리표시자에 넣는다. 여는 줄의 패턴 `` \A[ \t]{0,3}(`{3,}|~{3,}) ``는 들여쓰기 세 칸까지 허용한 백틱이나 물결표 세 개 이상으로, 마크다운의 펜스 규칙과 같다. 닫는 줄은 같은 패턴 뒤에 공백만 오고(`[ \t]*\z`) 첫 글자가 여는 줄의 문자와 같아야 한다. 그래서 백틱 펜스 안의 `~~~`는 블록을 닫지 못한다. 펜스 밖의 줄에서는 인라인 코드를 백틱 쌍 단위로 자리표시자에 넣는다. 치환이 끝나면 `unmask_code`가 자리표시자를 원문으로 되돌린다. 자리표시자를 NUL로 감싼 것은 본문에 나올 수 없는 바이트라서 마스크 경계가 본문과 부딪히지 않기 때문이다. 마스킹된 구간은 `LINK_RE`가 아예 보지 못하므로 고쳐지지도, 감사에 기록되지도 않는다.

## 감사 로그의 버킷

소스의 표시명과 canonical이 다르면 그 차이를 분류해서 `scripts/audit/link-overrides.log`에 한 줄에 JSON 하나씩 적는다. 이 파일은 빌드마다 처음부터 다시 쓰인다.

```json
{"source":"...","url":"...","original":"...","canonical":"...","bucket":"cosmetic/label-enrich"}
```
{: data-filename="scripts/audit/link-overrides.log · 형식 예시"}

버킷은 이렇다.

- **cosmetic/label-enrich**: canonical에 괄호 부연이 붙었다(`명제 3` → `명제 3 (Riemann–Roch for surfaces)`). 플러그인이 제 일을 하는 중이다.
- **cosmetic/label-trim**: 소스 쪽 괄호를 canonical이 잘라냈다. `Proposition 6 (1)`의 `(1)`처럼 사람이 넣은 정보일 수 있으니 한 번 봐야 한다.
- **cosmetic/same-cat-omit**: 같은 카테고리라서 브래킷을 뗐다. 무해하다.
- **title-drift**: 대상의 제목·카테고리 이름·섹션명·라벨이 바뀌었다(`section-renamed`, `category-renamed`, `label-renamed`). 대상 글에서 사라진 각주는 `footnote-stripped`로 따로 센다. 소스를 고칠 대상이다.
- **anchor-dropped**: 다른 글의 앵커(`#prop8` 등)가 없어져 `⁋` 꼬리를 뗐다. 배포본은 글 단위 링크로 살아남지만 수정은 소스에서 해야 한다.

분류는 문자열 비교다. 앞의 `\[…\]`와 뒤의 `, ⁋…`·`, §§…`·`, 각주 …` 꼬리를 떼어 따로 비교하고, 한쪽이 괄호만 더한 꼴이면 cosmetic, 아니면 title-drift로 보낸다. 표지 없는 링크가 대상 제목으로 바뀐 것도 여기서는 `section-renamed`로 떨어지므로, 그 숫자가 전부 낡은 소스는 아니다.

빌드 끝에는 버킷별 개수를 담은 summary 줄이 붙는다. 첫날 버킷 분류를 붙이고 돌린 빌드에서는 463건 중 459건이 label-enrich였고, 소스를 살펴볼 것은 각주 2건과 깨진 앵커 2건이었다.

CI가 남기는 로그는 배포와 함께 버려지므로, 매일 04:30 크론이 `link_normalizer_run.sh`로 로컬 프로덕션 빌드를 한 번 따로 돌린다. 출력은 `/var/tmp`의 일회용 디렉토리로 보낸다. 이 Pi의 `/tmp`는 RAM 위의 tmpfs이고 `_site` 전체는 700MB쯤 된다. 끝나면 summary 줄에 시각을 붙여 `link_normalizer.log`에 이어 쓴다. 422줄로 자란 플러그인이 하는 일의 9할은 여전히 괄호를 더하는 것이다.
