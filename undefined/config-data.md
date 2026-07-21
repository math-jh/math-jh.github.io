# _config.yml · Gemfile · _data/*

## _config.yml
역할: Jekyll 사이트 전역 설정(테마 스킨·SEO·댓글·플러그인·defaults·head_scripts 등). `site.*`로 전 레이어에 노출된다.

**uses (외부 정의 사용)**
- 없음 (이 파일 자체가 최상위 정의 소스이며, 다른 데이터 파일을 참조하지 않는다. 단 주석에서 `_data/categories.yml`을 "카테고리 목록·순서 관리처"로 문서화한다.)

**defines (외부 소비 정의)**
- `site.minimal_mistakes_skin` (config) → 소비: `assets/css/main.scss:14` (라이트 스킨 @import 선택)
- `site.dark_skin` (config) → 소비: `assets/css/main_dark.scss:11`
- `site.dark_theme` (config, bool) → 소비: `_includes/masthead.html`(43,71), `_includes/head.html:33`
- `site.multilingual` (config, bool) → 소비: `_includes/masthead.html`(7,43,88), `_includes/category-list.html:19`, `_includes/breadcrumbs.html:24`
- `site.locale` (config) → 소비: 전역 73곳(`_includes/seo.html`, `footer.html`, `comments.html`, `masthead.html`, `nav_recents.html` 등) — `lang`/`site.data.ui-text[lang]` 조회 키로 재사용
- `site.title` / `site.title_separator` / `site.subtitle` / `site.name` / `site.description` / `site.description_en` → 소비: `_includes/seo.html`, `masthead.html`, `footer.html` (description_en은 EN 페이지 전용 폴백, `seo.html:35`)
- `site.url` / `site.baseurl` → 소비: `_includes/seo.html:9-10` (canonical URL 조합)
- `site.repository` → 소비: `_includes/comments-providers/{giscus,utterances,staticman,staticman_v2}.html`, `_includes/comments.html` (댓글 provider의 GitHub repo 슬러그)
- `site.teaser` → 소비: `_includes/archive-single.html:4` (폴백 티저 이미지)
- `site.logo` / `site.masthead_title` → 소비: `_includes/masthead.html`(1,9,17,21)
- `site.breadcrumbs` (현재 false) → 소비: `_layouts/archive.html:11`, `_layouts/single.html:20`, `_layouts/archive_custom.html:12` — 값이 false라 분기는 항상 꺼져 있음(죽은 게 아니라 의도적 off)
- `site.words_per_minute` → 소비: `_includes/page__meta.html:23` (읽기시간 계산 폴백)
- `site.comments.provider` / `site.comments.giscus.*` → 소비: `_layouts/single.html:88`, `_includes/comments.html`, `_includes/comments-providers/giscus.html` — 현재 활성 provider가 giscus라 `disqus/discourse/facebook/utterances/staticman` 하위 키들은 대응 템플릿(`_includes/comments-providers/*.html`)에 소비처는 있으나 런타임에 타지 않음
- `site.atom_feed.{path,hide}` → 소비: `_includes/footer.html:15-16`, `_includes/head.html:9-10`
- `site.search` (== true) → 소비: `_layouts/default.html:111`, `_includes/masthead.html:37`, `_includes/scripts.html:9`
- `site.google_site_verification` / `bing_site_verification` / `naver_site_verification` / `yandex_site_verification` / `baidu_site_verification` → 소비: `_includes/seo.html` (244-260 각 meta 태그)
- `site.twitter.username` / `site.facebook.{publisher,app_id}` → 소비: `_includes/seo.html`(129-164)
- `site.og_image` → 소비: `_includes/seo.html` (사용 확인, OG 이미지 폴백)
- `site.social.{type,name,links}` → 소비: `_includes/seo.html`(230-238, JSON-LD)
- `site.analytics.provider` / `site.analytics.google.{tracking_id,anonymize_ip}` → 소비: `_includes/analytics.html`, `_includes/analytics-providers/google-gtag.html` (활성 provider)
- `site.author.*` (name/url/avatar/bio/location/email/links) → 소비: `_includes/author-profile.html`, `_includes/seo.html:78,217` — `author.links`의 6개 항목은 전부 `url:` 이 주석 처리돼 있어 `link.label and link.url` 조건을 못 넘고 실제로는 하나도 렌더되지 않음(데이터상 dead)
- `site.footer.links` → 소비: `_includes/footer.html` (GitHub 항목만 url 有, 나머지 5개는 author.links와 같은 이유로 미렌더)
- `site.category_archive.{type,path}` → 소비: `_includes/breadcrumbs.html:1`, `_includes/page__taxonomy.html:5`, `_includes/category-list.html`
- `site.github` (`github: [metadata]`) → 소비(시도): `_includes/seo.html:12` `site.github.url` — **정의 미발견 ⚠**: `jekyll-github-metadata` gem이 Gemfile/Gemfile.lock에 없어 빌드 시 `site.github`가 채워지지 않음. 게다가 `site.url`이 항상 truthy라 이 폴백 라인 자체가 도달 불가 — 이중으로 죽은 설정
- `site.defaults` (posts scope: layout/author_profile/read_time/show_date/toc/toc_sticky/comments/share) → 소비: 이 값들이 `page.*`로 전개되어 `_layouts/single.html`(toc:57-59, toc_sticky:58, share:83, comments:88) 등 전역에서 읽힘
- `site.head_scripts` (배열) → 소비: `_includes/head.html:58-59` (`<script>` 루프)
- `site.include` / `site.exclude` / `site.keep_files` / `encoding` / `markdown_ext` / `markdown` / `highlighter` / `kramdown.*` / `sass.*` / `timezone` → Jekyll 코어/gem이 직접 읽는 빌드 설정(Liquid `site.*` 노출 대상 아님). `sass.silence_deprecations`는 jekyll-sass-converter가, `kramdown.*`는 kramdown 파서가 소비
- `site.plugins` (jekyll-sitemap/jekyll-feed/jekyll-include-cache/jekyll-last-modified-at) → 소비: Bundler가 Gemfile의 `jekyll_plugins` 그룹과 대조해 로드. **Gemfile과 완전히 일치**(불일치 없음)
- `last-modified-at.ignore_commits` (문서화만, 실제 키 없음) → 소비: `_plugins/last_modified_git.rb:58` `site.config.dig("last-modified-at", "ignore_commits")` — **정의 미발견(옵션) ⚠**: 현재 `_config.yml`에 이 키 자체가 없어 항상 빈 배열로 폴백. 있어야 할 훅은 준비돼 있으나 아직 값을 넣은 적 없음(기능은 정상, 데이터만 비어 있음)

**dead keys (소비처 전무 확인, ⚠)**
- `search_full_content`, `search_provider`, `lunr.search_within_pages`, `algolia.*`(application_id/index_name/search_only_api_key/powered_by/files_to_exclude), `google.search_engine_id`, `google.instant_search` — 실제 검색은 `search: true` + pagefind 바이너리(`scripts/reindex-pagefind.sh`, `_includes/search/pagefind-search-scripts.html`)로 완전히 별도 구현되어 있어, 이 테마 기본 검색 설정 블록 전체가 죽어 있음. `_includes/search/*.html` 어디에도 `site.lunr`/`site.algolia`/`site.search_provider` 참조 없음
- `site.alexa_site_verification` — `_includes/seo.html:250`에서 소비를 "시도"하지만 `_config.yml`에 해당 키가 아예 없음(다른 site_verification들과 달리 빈 자리조차 없음) — 반대 방향의 **정의 미발견 ⚠** (used-but-never-declared)

---

## Gemfile
역할: Ruby 의존성 선언. 테마(minimal-mistakes)는 완전히 벤더링되어 있어 `gem "minimal-mistakes-jekyll"` 자체가 없음(2026-06-17 정리).

**uses (외부 정의 사용)**
- 없음

**defines (외부 소비 정의)**
- `jekyll` (~> 4.3) → 소비: 전체 빌드(Jekyll 코어)
- `webrick` → 소비: `jekyll serve` (Ruby 3+ 필수 의존성)
- `tzinfo-data` (mingw/mswin/x64_mingw only) → 소비: 없음(Linux/macOS 빌드 환경이라 플랫폼 조건에 걸리지 않음 — 실질적으로 이 환경에서는 로드 안 됨, Windows 대비용)
- `jekyll_plugins` 그룹의 4개 gem(jekyll-last-modified-at/jekyll-feed/jekyll-sitemap/jekyll-include-cache) → 소비: `_config.yml`의 `plugins:` 목록과 **1:1 일치**. 각 gem의 런타임 훅: `jekyll-last-modified-at`는 `_plugins/last_modified_git.rb`가 `Determinator` 객체를 오버라이드하는 방식으로 개입, `jekyll-sitemap`은 `/sitemap.xml` 생성, `jekyll-feed`는 `/feed.xml`(head.html의 atom_feed 링크와 별개 경로), `jekyll-include-cache`는 `{% include_cached %}` 태그 제공(사용처는 html 그룹 담당)
- `.github/dependabot.yml` → Gemfile을 bundler 생태계로 감시(의존성 업데이트 PR 생성)

---

## _data/authors.yml
역할: 저자 프로필 매핑(`page.author` 문자열 → 표시 정보). 현재 "Marvin"(LLM 페르소나) 한 항목뿐 — 사이트 소유자(K)는 `_config.yml`의 `author:` 블록을 그대로 씀.

**uses (외부 정의 사용)**
- 없음

**defines (외부 소비 정의)**
- `Marvin.{name,avatar,bio,ai}` (스키마: name/avatar/ai/bio) → 소비:
  - `_includes/seo.html:79` `site.data.authors[author]` (JSON-LD author 대체)
  - `_includes/author-profile.html:1-2` (프로필 카드: name/avatar/bio 렌더, `author.ai`로 about-Marvin 링크 분기)
  - `_includes/ai-author-notice.html:7-18` (`_ai_author.ai`가 true면 `_data/ui-text.yml`의 `ai_post_notice`를 `_ai_author.name`으로 치환해 경고 배너 렌더)
- 소비 트리거(file-artifact 결합): `_posts/**/*.md` frontmatter `author: Marvin` (29개 파일, 예: `_posts/Misc/LLM_Workshop/*.md`) — 이 문자열이 `authors.yml`의 키와 정확히 일치해야 매핑됨

---

## _data/categories.yml
역할: 카테고리 마스터(목록·순서·섹션·색·과목홈 소개문) — 단일 source of truth. YAML 매핑 삽입 순서 = 표시 순서.

**uses (외부 정의 사용)**
- 없음

**defines (외부 소비 정의)**
- `families.{key}.{label,label_ko,hue}` → 소비: `_plugins/graph_data.rb:77-81`(`families(site)` 함수, 그래프 JSON의 필터 칩 데이터로 그대로 전송) → 그래프 JS(`assets/js/custom/Graph_page.js`, 다른 그룹 담당)가 최종 소비
- `sections.{key}.{ko,en,family}` → 소비: `_plugins/graph_data.rb:59`(family 매핑), `_plugins/hide_empty_subject_pages.rb:75`(`home_sections` 생성, `site.data["home_sections"]`로 재노출) → `_includes/subject-grid.html`, `_includes/nav_list`가 `site.data.home_sections`로 소비
- `subjects.{"Math / X"}.{ko,section,hue,sat,l,excerpt_ko,excerpt_en}` → 소비:
  - `.ko` : `_layouts/single.html:43`, `_includes/page__hero.html:36`, `_includes/subject-grid.html:34`, `_layouts/categories.html`(39-61), `_includes/nav_list:40,80`
  - `.hue/.sat/.l` : `_layouts/default.html:62-89`(→ `--hero-hue/--hero-sat/--hero-l` 인라인 CSS 변수 → `_sass/minimal-mistakes/_page.scss`, `_sass/_subject-cards.scss`가 소비), `_layouts/categories.html`(→ `--cat-hue/--cat-sat/--cat-l`)
  - `.section` : `_plugins/graph_data.rb:64`(family 역참조), `_plugins/hide_empty_subject_pages.rb:77`(home_sections 그룹핑)
  - `.excerpt_ko/.excerpt_en` : `_plugins/hide_empty_subject_pages.rb:187` (`doc.data["excerpt"]`로 심어 과목홈 생성 시 사용, 언어 없으면 경고만 내고 빈 excerpt로 생성)
  - 키 이름 자체(`"Math / Set Theory"` 등) : **file-artifact 결합** — `_posts/**/*.md`의 frontmatter `categories:` 문자열과 정확히 일치해야 함(주석 §9에 명시). 불일치 시 조용히 매칭 실패(하드 에러 없음)
  - `scripts/generate-thumbnails.js:32` — `_data/categories.yml`을 직접 YAML 파싱해 subjects 순서로 썸네일 번호(01, 02, …) 부여

---

## _data/navigation.yml
역할: 마스트헤드 메인 링크 + 큐레이션 사이드바(수동 관리분). 카테고리 자동 사이드바는 여기 없이 `_includes/nav_list`가 `_data/categories.yml`에서 파생한다.

**uses (외부 정의 사용)**
- 없음 (단, `mirror_symmetry-ko` 블록 주석이 `_data/categories.yml` 파생 자동사이드바와의 역할 분담을 문서화)

**defines (외부 소비 정의)**
- `main` (배열: title/url/lang/icon) → 소비: `_includes/masthead.html:25` (마스트헤드 최상단 링크, lang으로 ko/en 분기)
- `blog_development-ko` / `mirror_symmetry-ko` / `mirror_symmetry-en` (배열: title/children[{title,url}]) → 소비: `_includes/nav_list:1,51-68` via `include.nav` 파라미터, 호출측: `_includes/sidebar.html:12,15` → `page.sidebar.nav` (frontmatter 키) — **file-artifact 결합**: 이 3개 키를 `sidebar: nav:` 값으로 쓰는 tracked 포스트/페이지가 실존해야 소비됨(현재 실측: `blog_development-ko`, `mirror_symmetry-ko`, `mirror_symmetry-en`, `llm_workshop-ko` 등 사용됨. 단 `llm_workshop-ko`는 이 파일에 블록이 없어 auto-sidebar(categories.yml 파생) 경로로 정상 폴백)
- `mirror_symmetry-ko-research` → **소비처 없음(현재 tracked repo 기준) ⚠** — 파일 자체 주석(76-86행)에 "MR stream 연구용 로컬 전용, gitignore 처리된 포스트만 참조, 라이브 공개 안 함"이라 명시돼 있어 의도된 미소비. `grep -rl "mirror_symmetry-ko-research" _posts/ _pages/` 결과 0건으로 실측 일치
- 그 외 카테고리(`algebraic_structures-ko`, `calculus-en` 등 50여 개, 각 포스트 frontmatter `sidebar.nav`에서 실사용) → 이 파일에 블록이 없어 `_includes/nav_list:30-43`의 auto-cat 경로(카테고리 slug ↔ `_data/categories.yml` subjects 대조)로 전부 처리됨 — 설계상 정상(주석에 명시)

---

## _data/recent_comments.yml
역할: `scripts/comments/fetch_recent_comments.py` cron이 giscus discussion을 폴링해 자동 생성하는 산출물. 손으로 편집 금지(파일 자체 주석).
스키마: `{ko|en}[]` 배열, 각 항목 `{permalink, title, author, updated, anchor}`.

**uses (외부 정의 사용)**
- 없음 (전체가 스크립트 산출물)

**defines (외부 소비 정의)**
- `ko[]`/`en[]` (permalink/title/author/anchor) → 소비: `_includes/nav_recents.html:11,29-37` (`site.data.recent_comments[_lang]`, 사이드바 "최근 댓글" 목록 렌더)
- `updated` 필드 → **소비처 미발견(dead) ⚠**: `fetch_recent_comments.py`가 매번 기록하지만 `nav_recents.html`은 permalink/title/author/anchor만 읽고 updated는 참조하지 않음(정렬도 이미 스크립트 쪽에서 끝낸 상태로 저장되는 것으로 보임)
- 쓰기측(file-artifact): `scripts/comments/fetch_recent_comments.py:49` `DATA_PATH` — cron이 이 경로에 직접 덮어씀

---

## _data/terms.yml (872 항목, 스키마만)
역할: `/ko/terms` 찾아보기 페이지의 유일한 데이터 소스이자, 용어 영어화 정책("primary")의 source of truth. 구조: 알파벳 최상위 키(A, B, …) → 항목 배열. 항목 스키마: `id/en/ko/primary?/note?/defs[]/refs[]/see[]`. `defs`/`refs`는 `{label,url}`, `see`는 `{id,label,lang?}`.

**uses (외부 정의 사용)**
- 없음 (터미널 데이터 파일). 단 `defs[].url`/`refs[].url`이 블로그 글 permalink를 가리켜 사실상 `_posts/**`와 링크로 결합돼 있음(URL 실재성은 lint 스크립트가 검증)

**defines (외부 소비 정의)**
- `id` → 소비: `_pages/ko/Terms.md:32` (`id="{{ t.id }}"` 앵커), `see[].id`가 다른 항목의 id를 앵커 참조(`#idx-...` 아니라 `#{{ s.id }}`) — cross-entry 결합
- `en` / `ko` / `primary` → 소비: `_pages/ko/Terms.md:32-38` (검색용 data-search 속성 + primary에 따라 굵게/보조 표기 스위치)
- `defs[].{label,url}` / `refs[].{label,url}` → 소비: `_pages/ko/Terms.md:40-53` (정의 위치·참고 문서 링크 렌더)
- `see[].{id,label,lang}` → 소비: `_pages/ko/Terms.md:54-60` (`lang=="ko"`면 `<em-ko>` 래핑)
- 최상위 알파벳 키 순회(`pair[0]`) → 소비: `_pages/ko/Terms.md:14-18` (알파벳 바로가기 nav)
- **file-artifact 결합 (스크립트군, `scripts/term-extraction/*.py`)**:
  - 읽기+쓰기: `terms_lint.py`(`--fix`로 파일 자체 정규화, 실패 시 `.bak` 백업), `term_extract_worker.py`(cron 워커, LLM 제안 → 스키마 검증 게이트 → append, 직접 LLM 쓰기 금지 원칙)
  - 읽기 전용: `terms_usage_lint.py`(primary vs 본문 실사용 대조 리포트), `deprecated_terms_lint.py`(primary:en 항목의 ko형이 prose에 있는지 검사), `usage_dominance.py`, `terms_search.py`, `gloss_stage.py`/`gloss_backfill.py`(defs/refs 보강), `hybrids.py`, `mech_sweep.py`, `gen_flip_review.py`
  - `.claude/hooks/terms_lint_hook.py` — `_data/terms.yml` 편집을 감지해 `terms_lint.py` 자동 실행(PostToolUse 훅)
  - `.claude/hooks/md_lint.py:320-367,439` — 이 파일을 직접 로드해 `primary: en` 항목의 ko 표기가 새 글 본문에 쓰이면 실시간 경고(용어 영어화 강제 메커니즘의 핵심 데이터 소스)

---

## _data/ui-text.yml (2052줄, 다국어 UI 문자열)
역할: 레이아웃/인클루드의 하드코딩 문자열을 언어별로 분리. `en`(+ en-US/CA/GB/AU 별칭), `ko`(+ ko-KR 별칭)만 실사용, 나머지 32개 언어 블록(es/fr/tr/pt/it/zh/de/ne/ru/lt/gr/sv/nl/id/vi/da/pl/ja/sk/hu/ro/pa/fa/ml/th/hi/ca/ga/fi/my/no/he/ar/sw)은 **소비처 없음**.

**uses (외부 정의 사용)**
- 없음

**defines (외부 소비 정의)**
- 대다수 키(`theme_*`, `skip_primary_nav/skip_content/skip_footer`, `breadcrumb_*`, `menu_label`, `toc_label`, `tags_label`, `categories_label`, `date_label`, `comments_*`, `related_label`, `follow_label`, `feed_label`, `powered_by`, `website_label`, `email_label`, `recent_posts`, `recent_comments`, `kimi_translation_notice`, `ai_post_notice`, `comment_form_*`, `comment_btn_*`, `comment_success_msg`, `comment_error_msg`, `loading_label`, `back_to_top`, `share_on_label`, `page`, `pagination_previous/next`, `ext_link_label`, `less_than`, `minute_read`, `more_label`) → 소비: `_includes/masthead.html`, `footer.html`, `comments.html`, `comments-providers/{giscus,staticman,staticman_v2,utterances,disqus,discourse,facebook}.html`, `author-profile.html`, `category-list.html`, `tag-list.html`, `translation-notice.html`, `ai-author-notice.html`, `skip-links.html`, `page__hero.html`, `page__date.html`, `page__meta.html`, `nav_recents.html`, `post_pagination.html`, `breadcrumbs.html`, `social-share.html`, `seo.html`, `_layouts/{categories,single}.html` (모두 `site.data.ui-text[lang].<key>` 패턴, lang은 항상 "ko" 또는 "en"으로 정규화됨)
- **소비처 미발견(dead) ⚠** (en 블록 기준, 코드베이스 전체 검색 0건): `skip_links`, `search_label_text`, `search_placeholder_text`, `search_algolia_no_results`, `results_found`, `undefined_wpm`, `recents_label`, `cancel_reply`, `reply_to_en`, `reply_to_ko` — 테마 스캐폴딩 잔재(알골리아/lunr 검색·구식 staticman 댓글 폼의 문자열이라 `_config.yml`의 dead search 블록과 짝을 이룸)
- 32개 미사용 언어 블록(es/fr/tr/…/sw) 전체 → **소비처 없음**: `site.locale`이 항상 "ko-KR"이고 `lang` 변수는 페이지 URL prefix(`/ko/`, `/en/`)로만 "ko"/"en"으로 정규화되므로(예: `_includes/seo.html:3-6` 패턴이 전역 반복) 다른 언어 키로 조회되는 경로가 아예 없음
