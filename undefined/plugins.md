# _plugins/*.rb

## _plugins/fenced_theorem_blocks.rb
역할: 소스 마크다운의 `:::` 펜스드 div(정리/정의/증명 블록)를 기존 Style A HTML(`<div class="...">`, `<ins id="...">`)로 라인 스캔 변환. `:site,:pre_render` priority HIGH(30)로 link_normalizer보다 먼저 실행.

**uses (외부 정의 사용)**
- `Jekyll::Hooks`, `Jekyll::Hooks::PRIORITY_MAP`, `Jekyll.logger` (kind: gem) ← 정의: Jekyll gem(외부) — 훅 등록·우선순위 상수
- `site.posts.docs`, `doc.content`/`doc.instance_variable_set(:@content,...)` (kind: Jekyll core) ← 정의: Jekyll core — Jekyll 4 Document의 content writer가 항상 @content를 갈아끼우진 않아 ivar 직접 주입(주석에 명시된 우회)

**defines (외부 소비 정의)**
- `FencedTheoremBlocks::KIND_MAP` / `EXPLICIT_CLASSES` / `COLLAPSIBLE_CLASSES` (kind: Ruby 상수) → 소비: `_plugins/theorem-label-splitter.rb:29`(`BOX_ALT`가 `EXPLICIT_CLASSES` 직접 참조) — 정리 박스 어휘의 단일 출처(파일 로딩 순서: `_plugins/`는 알파벳순이라 `f` < `t`)
- `site.data["theorem_kinds"]` = {labels, boxes, collapsibles, prefixes} (`:site,:post_read` 훅, kind: site.data) → 소비: `assets/css/main.scss`/`main_dark.scss`(`$thm-boxes`/`$thm-collapsibles` Liquid 프론트매터) · `_includes/head.html:25`(`window.THEOREM_KINDS`로 브라우저 전달) → 다시 `assets/js/custom/Citation.js`, `assets/js/custom/Xref_preview.js`가 소비
- 변환된 `doc.content`(`<div class="definition|proposition|example|remark|misc" markdown="1">`, `<ins id="...">`) (kind: doc.content) → 소비: kramdown 렌더러(같은 패스에서 재파싱) · `_plugins/theorem-label-splitter.rb`(`BOX_START` 정규식이 렌더된 `<ins id>` 매칭) · `_plugins/link_normalizer.rb`(`Maps#initialize`가 `<ins id="...">**label**</ins>` 스캔해 `label_by_anchor` 구성) · `_sass/minimal-mistakes/_notices.scss`(class 셀렉터)

## _plugins/graph_data.rb
역할: `:site,:post_write`에 각 글 본문(doc.content)의 교차참조 링크를 스캔해 force-graph용 `assets/data/graph-{ko,en}.json` 생성.

**uses (외부 정의 사용)**
- `site.data["categories"]["subjects"]`(hue, section, excerpt_ko/en) (kind: _data) ← 정의: `_data/categories.yml`
- `site.data["categories"]["sections"]`(family 매핑용) (kind: _data) ← 정의: `_data/categories.yml`
- `site.data["categories"]["families"]`(key,label,label_ko,hue) (kind: _data) ← 정의: `_data/categories.yml`
- `doc.data["title"]`, `doc.data["weight"]`, `doc.url`, `doc.content` (kind: frontmatter/Jekyll core) ← 정의: 각 `_posts/**/*.md` 프론트매터(weight는 글 순서 프론트매터 키, 넓게 소비되는 키라 이 파일은 그중 한 소비처)

**defines (외부 소비 정의)**
- `assets/data/graph-ko.json`, `assets/data/graph-en.json` (kind: file-artifact) — 스키마: `nodes[].{id,title,url,category,hue,family,color}`, `links[].{source,target,weight}`, `families[].{key,label,label_ko,hue}` → 소비: `assets/js/custom/Graph_page.js`(`/graph` 전역 뷰, `fetch('/assets/data/graph-'+lang+'.json')`, `data.nodes`/`data.links`/`data.families` 전 필드 사용) · `assets/js/custom/Local_graph.js`(글별 2-hop 로컬 그래프, 동일 fetch)
- 비고: `Graph_page.js`에 `FAMILIES_FALLBACK` 상수가 fetch 실패시에만 쓰이는 안전망으로 남아있음(과거엔 이게 유일한 정의처라 버그였다고 주석에 명시 — 지금은 정상적 fallback)

## _plugins/hide_empty_subject_pages.rb
역할: `:site,:post_read`에 Math 과목홈(archive_custom 레이아웃)을 카테고리별로 물리 파일 없이 생성하고, 그 언어에 글이 0편인 과목홈은 `site.pages`에서 제거. 홈 그리드 섹션 뷰도 파생.

**uses (외부 정의 사용)**
- `site.data["categories"]["subjects"]`(ko, section, hue, excerpt_ko/en) (kind: _data) ← 정의: `_data/categories.yml`
- `site.data["categories"]["sections"]`(언어별 라벨) (kind: _data) ← 정의: `_data/categories.yml`
- `doc.data["categories"]` (kind: frontmatter, Jekyll 표준 categories 배열) ← 정의: 각 글 프론트매터
- `Jekyll::PageWithoutAFile` (kind: gem) ← 정의: Jekyll core — 파일 없는 페이지 생성 API

**defines (외부 소비 정의)**
- `site.data["home_sections"]` (kind: site.data) → 소비: `_includes/subject-grid.html:17`(홈 카드 그룹 렌더)
- `site.data["subject_pages"]` = {ko:{cat→url}, en:{...}} (kind: site.data) → 소비: `_includes/subject-grid.html:13`(홈 카드 실제 URL 조회)
- `page.data["category"]` (생성 페이지 + 살아남은 기존 과목홈 페이지에 역주입) (kind: page.data) → 소비: `_layouts/archive_custom.html`(과목 카드 목록 `site.categories[page.category]`) · `_layouts/default.html:89`(히어로 hue 조회 `site.data.categories.subjects[page.category]`)
- `page.data["eyebrow"]` (kind: page.data, frontmatter eyebrow 있으면 그 값 우선) → 소비: `_includes/page__hero.html:33-34`
- `page.data["excerpt"]`, `"last_modified_at"`, `"permalink"`, `"layout":"archive_custom"`, `"header"` (생성 페이지 frontmatter) (kind: page.data) → 소비: `_includes/page__hero.html`(excerpt→lead 문단) · `_includes/seo.html:40`(excerpt→meta description) · `_layouts/archive_custom.html`(layout 자체) — last_modified_at은 파일 없는 페이지라 일반 Time 값으로 심어 `jekyll-last-modified-at`/`last_modified_git.rb` 둘 다 손대지 않게 하는 방어 설계(주석에 ENOENT 사고 명시, 2026-07-18)
- `site.pages`에서 빈 과목홈 제거 (kind: 훅 부작용) → 소비: 이후 모든 렌더 단계(archive_custom 레이아웃을 타는 물리 페이지가 있어도 카운트 0이면 제거됨)

## _plugins/inline_list_math.rb
역할: `:documents,:pages`의 `:post_render`에서, 리스트 항목의 유일한 내용인 display math(`\[...\]`)를 inline(`\(...\)`)로 되돌리는 최종 HTML 후처리.

**uses (외부 정의 사용)**
- `Jekyll::Hooks`, `doc.output`, `doc.output_ext` (kind: Jekyll core) ← 정의: Jekyll core

**defines (외부 소비 정의)**
- 없음 — `InlineListMath` 모듈을 참조하는 타 `.rb` 파일 없음(grep 확인). 변환 결과(`doc.output`)는 최종 렌더 HTML 자체이므로 소비처는 "브라우저"이지 다른 레포 파일이 아님. 코드 자체를 다른 파일이 재사용/참조하지 않는 self-contained 후처리기.

## _plugins/kramdown_inline_math.rb
역할: kramdown 코어의 `inline_math` 파서를 몽키패치해 `$...$`(단일 달러)도 `$$...$$`와 동일하게 verbatim 수식으로 인식시킴. 추가로 `smart_quotes` 파서보다 `inline_math`가 먼저 매치되도록 span parser 순서를 재배치.

**uses (외부 정의 사용)**
- `Kramdown::Parser::Kramdown`, `parser(:inline_math)`, `@span_parsers`, `Kramdown::VERSION` (kind: gem) ← 정의: `kramdown` gem(외부, `require "kramdown/parser/kramdown/math"`) — 버전이 바뀌어 `start_re`/`span_start` 모양이 달라지면 `raise`로 빌드를 세우는 방어적 어써션 내장(정의처 자체가 이 파일 밖 gem이라 미스매치 시 즉시 실패하도록 설계)

**defines (외부 소비 정의)**
- 없음 — 이 파일은 kramdown 파서 내부 동작만 바꾸고, 결과물(`\(...\)` 인라인 수식 HTML)은 다른 플러그인이 아니라 KaTeX(클라이언트 JS, 이 레포 밖 CDN/번들)가 최종 소비. 이 파일의 심볼을 참조하는 타 `.rb` 없음.

## _plugins/last_modified_git.rb
역할: `:site,:post_read`에 frontmatter에 `last_modified_at`이 없는 모든 문서/페이지에 대해 git log 기반 최종 수정시각을 계산해 채운다. `[lastmod-skip]` 마커·ignore_commits SHA 목록의 커밋은 건너뜀.

**uses (외부 정의 사용)**
- `site.config.dig("last-modified-at","ignore_commits")` (kind: _config.yml 키) ← 정의 미발견 ⚠ — `_config.yml`에 `last-modified-at:` 키 자체가 현재 없음(grep 확인, `jekyll-last-modified-at` gem 등록 줄만 존재). 즉 이 config 키는 코드상 지원되지만 레포 어디에도 설정된 적이 없어 `ignore_commits`는 항상 빈 배열 — 기능은 살아있으나 실사용 실적 없음
- `Jekyll::LastModifiedAt::Determinator` (kind: gem 클래스) ← 정의: `jekyll-last-modified-at` gem(외부, 1.3.2) — 이 gem이 `:post_init`에 심는 seed 객체 타입을 detector로 사용(“아직 frontmatter 값 없음”의 판별 근거)
- `item.data["last_modified_at"]` 읽기(현재값이 Determinator인지 검사) (kind: doc.data) ← 정의: `jekyll-last-modified-at` gem이 최초 심음, 또는 저자가 frontmatter에 직접 기입

**defines (외부 소비 정의)**
- `item.data["last_modified_at"]`(git log 기반 계산값으로 덮어씀) (kind: doc.data/page.data) → 소비: `_layouts/recent.html`, `_layouts/single.html`, `_layouts/splash.html`, `_includes/seo.html`, `_includes/page__date.html` — 또한 `_plugins/hide_empty_subject_pages.rb`가 생성 과목홈에 한해 이 계산을 우회하도록 설계(생성 페이지는 git 이력이 없어 ENOENT 방지, 주석에 상호 인지 명시)

## _plugins/link_normalizer.rb
역할: production 빌드에서만(`Jekyll.env == "production"`) 글 본문의 내부 교차참조 링크 표시 텍스트(`[...](...)`)를 대상 글의 정본 제목/라벨/H2로 재작성. 소스 `.md`는 불변, `doc.content`만 변경. 모든 치환을 `scripts/audit/link-overrides.log`에 로그.

**uses (외부 정의 사용)**
- `Jekyll.env` (kind: Jekyll core) ← 정의: Jekyll core — production 게이트
- `site.posts.docs`, `doc.url`, `doc.data["title"]`, `doc.content` (kind: Jekyll core/frontmatter) ← 정의: 각 글
- `site.data["navigation"]["category-ko"/"category-en"]`(sections[].children[].{url,title}) (kind: _data) ← 정의: `_data/navigation.yml`
- 대상 글 본문의 `<ins id="...">**label**</ins>` 패턴(fenced_theorem_blocks.rb 변환 결과 소비), `## H2` 헤딩 텍스트 (kind: doc.content, 타 플러그인 산출물) ← 정의: `_plugins/fenced_theorem_blocks.rb`(라벨 렌더) 및 원문 마크다운(H2)

**defines (외부 소비 정의)**
- 변경된 `doc.content`(교차참조 표시 텍스트 재작성) (kind: doc.content) → 소비: 이후 kramdown 렌더 → 최종 페이지 HTML(독자가 보는 링크 텍스트)
- `scripts/audit/link-overrides.log`(gitignored, JSON lines + SUMMARY) (kind: file-artifact) → 소비: `scripts/audit/link_normalizer_run.sh`(마지막 줄 SUMMARY 파싱), `scripts/archived/triage_overrides.py`(reader/inspector) — `_posts/Misc/LLM_Workshop/2026-05-28-Link_Normalizer.md`는 이 로그를 언급하는 설명 글일 뿐 코드 소비처 아님

## _plugins/theorem-label-splitter.rb
역할: `:documents,:post_render`에서 렌더된 HTML의 정리박스 라벨(`<ins id><strong>정의 1 (이름)</strong></ins>`)을 "종류+번호"와 "(서술명)" 두 조각으로 쪼개 각각 다른 span/class로 감싼다. `.definition/.proposition/.example/.remark/.misc`만 대상.

**uses (외부 정의 사용)**
- `FencedTheoremBlocks::EXPLICIT_CLASSES` (kind: Ruby 상수) ← 정의: `_plugins/fenced_theorem_blocks.rb:83` — 정리 박스 class 목록의 단일 출처(파일 로딩은 알파벳순이라 f가 먼저 로드됨을 주석이 명시)
- `doc.output`, `doc.url` (kind: Jekyll core) ← 정의: Jekyll core — `theorem-label-splitter`는 `fenced_theorem_blocks`(:pre_render, HIGH)보다 뒤(:post_render)라 렌더된 `<ins id>`가 이미 존재한다는 순서 보장에 의존

**defines (외부 소비 정의)**
- 최종 HTML class `thm-head`/`thm-tag`/`thm-n`/`thm-name`/`thm-name-ko` (kind: doc.output) → 소비: `_sass/minimal-mistakes/_notices.scss`(스타일링) · `assets/js/custom/Citation.js:40`(`.thm-n[id], ins[id]` 셀렉터로 라벨 앵커 스캔, 원래 `<ins id>` 만 보던 걸 쪼개진 구조까지 보조 포함하도록 확장됨을 주석이 명시)
