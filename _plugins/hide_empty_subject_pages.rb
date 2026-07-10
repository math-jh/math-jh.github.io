# 빈 카테고리의 과목홈(subject home)을 빌드에서 제외하고, 실제로 살아남은 과목홈
# 목록을 `site.data["subject_pages"]` 로 노출한다.
#
# 과목홈은 `_pages/{ko,en}/Math-*.md` 처럼 layout: archive_custom 을 쓰고, permalink
# 의 첫 구간 뒤가 카테고리 슬러그다:
#
#   "Math / Category Theory"       →  /ko/category_theory/
#   "Math / Gromov-Witten Theory"  →  /ko/gromov-witten_theory/
#
# (subject-grid.html · nav_list · _layouts/default.html 의 hero hue 조회와 같은 규칙:
#  " / " 뒤를 소문자로 바꾸고 공백을 _ 로. 하이픈은 그대로 둔다.)
#
# 해당 카테고리에 그 언어의 글이 하나도 없으면 페이지를 site.pages 에서 빼서 아예
# 빌드하지 않는다. 덕분에 _data/categories.yml 에 미발행 카테고리를 남겨 둬도
# 빈 과목홈이 생기지 않는다 (카테고리 목록 페이지 쪽 숨김은
# _layouts/categories-*.html 이 담당한다).
#
# published: false 초안은 Jekyll 이 site.posts 에서 이미 제외하므로, production 에서는
# 숨고 `--unpublished` 로 띄운 로컬 프리뷰에서는 정상적으로 보인다.
#
# site.data["subject_pages"] = { "ko" => { "Math / Calculus" => "/ko/calculus/", … }, "en" => {…} }
#   → 카테고리 → 그 언어 과목홈의 **실제 URL**. _includes/subject-grid.html 의 홈 카드와
#     _includes/nav_list 의 카테고리 사이드바가 이걸로 링크를 만든다. 과목홈이 안
#     만들어졌으면(빈 카테고리이거나 애초에 페이지 파일이 없거나) 항목도 안 나온다.
#     슬러그로 URL 을 조립하면 끝 슬래시 없는 permalink(/ko/peripherals)를 틀리게
#     만든다 — 실제로 홈의 "주변기기" 카드가 404 였다. 그래서 page.url 을 그대로 쓴다.
#
# 살아남은 과목홈에는 두 값을 되돌려 심는다 (frontmatter 에 적어 둘 필요가 없다):
#   page.category — permalink 슬러그에서 푼 카테고리명. _layouts/archive_custom.html
#                   이 이걸로 과목 카드를 그린다.
#   page.eyebrow  — _data/categories.yml 의 그 과목이 속한 섹션명(언어별).
#                   frontmatter 에 eyebrow 가 있으면 그 값이 우선한다.
# 예전에는 과목홈마다 hero_hue/eyebrow 를 손으로 적었는데, hero_hue 는 50개 중 44개가
# _data/categories.yml 과 어긋난 채 죽어 있었고(슬러그 조회가 먼저 이겨서 안 터졌을 뿐),
# eyebrow 는 Scheme Theory 가 "대수학"으로 잘못 적혀 있었다. 둘 다 여기서 파생한다.
#
# 슬러그가 어떤 카테고리와도 안 맞는 archive_custom 페이지(/ko/math/ 같은 허브)는
# 손대지 않는다. frontmatter 에 `category:` 를 직접 적어 두면 그 값이 우선한다.

module HideEmptySubjectPages
  LAYOUT = "archive_custom".freeze
  LANGS = %w[ko en].freeze

  module_function

  def slug_for(category)
    category.split(" / ").last.to_s.downcase.tr(" ", "_")
  end

  def lang_of(url)
    LANGS.find { |lang| url.start_with?("/#{lang}/") }
  end

  # _data/categories.yml 의 subjects (카테고리명 → { ko, section, hue, sat, l })
  def subjects(site)
    table = site.data["categories"]
    return {} unless table.is_a?(Hash)

    table["subjects"].is_a?(Hash) ? table["subjects"] : {}
  end

  # "슬러그 → 카테고리명" 표. 글이 0편인 카테고리도 들어 있어야 하므로
  # site.categories 가 아니라 마스터 목록(_data/categories.yml)에서 만든다.
  def slug_index(site)
    subjects(site).keys.each_with_object({}) { |name, acc| acc[slug_for(name)] = name }
  end

  # subjects 의 `section:` 으로 홈 그리드용 그룹을 만든다 (섹션 순서 = 첫 등장 순서).
  # 예전에는 이 목록이 _data/home_sections.yml 에 한 벌 더 있었고, 두 파일이 어긋나
  # 정수론·해석학 카드가 홈에서 통째로 빠져 있었다. 이제 한 곳에서 파생한다.
  def home_sections(site)
    names = (site.data["categories"] || {})["sections"] || {}
    grouped = {}
    subjects(site).each do |category, info|
      key = info["section"]
      next if key.nil?

      grouped[key] ||= []
      grouped[key] << category
    end

    grouped.map do |key, members|
      label = names[key] || {}
      { "ko" => label["ko"], "en" => label["en"], "subjects" => members }
    end
  end

  # (카테고리, 언어) → 글 수
  def post_counts(site)
    tally = Hash.new(0)
    site.posts.docs.each do |doc|
      lang = lang_of(doc.url)
      next if lang.nil?

      Array(doc.data["categories"]).each { |cat| tally[[cat, lang]] += 1 }
    end
    tally
  end

  # /ko/category_theory/ → "category_theory"
  def slug_of_page(url)
    url.split("/").reject(&:empty?)[1]
  end

  # 카테고리 → 그 과목이 속한 섹션명 (언어별).
  def eyebrow_index(sections)
    index = {}
    sections.each do |section|
      Array(section["subjects"]).each do |subject|
        LANGS.each { |lang| index[[subject, lang]] = section[lang] if section[lang] }
      end
    end
    index
  end

  # 이 페이지가 담당하는 (카테고리, 언어). 과목홈이 아니면 nil.
  def subject_of(page, by_slug)
    return nil unless page.data["layout"] == LAYOUT

    lang = lang_of(page.url)
    return nil if lang.nil?

    slug = slug_of_page(page.url)
    category = page.data["category"] || by_slug[slug]
    return nil if category.nil? # 허브 페이지(/ko/math/) 등

    [category, lang]
  end
end

Jekyll::Hooks.register :site, :post_read do |site|
  # 홈 그리드·사이드바가 쓰는 그룹 뷰를 categories.yml 에서 파생해 심는다.
  sections = HideEmptySubjectPages.home_sections(site)
  site.data["home_sections"] = sections

  by_slug = HideEmptySubjectPages.slug_index(site)
  counts = HideEmptySubjectPages.post_counts(site)
  skipped = []

  site.pages.reject! do |page|
    subject = HideEmptySubjectPages.subject_of(page, by_slug)
    next false if subject.nil?
    next false unless counts[subject].zero?

    skipped << "#{page.url} (#{subject.first})"
    true
  end

  # 살아남은 과목홈: 카테고리·eyebrow 를 심고, 홈 카드용 목록을 만든다.
  eyebrows = HideEmptySubjectPages.eyebrow_index(sections)
  built = HideEmptySubjectPages::LANGS.each_with_object({}) { |lang, acc| acc[lang] = {} }
  site.pages.each do |page|
    subject = HideEmptySubjectPages.subject_of(page, by_slug)
    next if subject.nil?

    category, lang = subject
    page.data["category"] = category
    page.data["eyebrow"] ||= eyebrows[subject]
    built[lang][category] = page.url
  end
  site.data["subject_pages"] = built

  # 반대 방향의 구멍: 글은 있는데 과목홈 .md 가 없는 카테고리. 조용히 홈 카드와
  # 사이드바에서 빠지고 /{lang}/{slug}/ 가 404 가 된다 (복소해석학·복소기하학이
  # 초안 12편·6편을 두고도 이 상태였다). 빌드가 알려주게 한다.
  counts.each do |(category, lang), count|
    next unless count.positive?
    next if built[lang].key?(category)

    slug = HideEmptySubjectPages.slug_for(category)
    Jekyll.logger.warn "SubjectPages:",
                       "'#{category}' 에 #{lang} 글이 #{count}편 있는데 과목홈이 없습니다 — " \
                       "_pages/#{lang}/ 에 permalink /#{lang}/#{slug}/ 인 " \
                       "layout: archive_custom 페이지를 만드세요"
  end

  Jekyll.logger.info "SubjectPages:",
                     "built #{built['ko'].size} ko / #{built['en'].size} en"
  unless skipped.empty?
    Jekyll.logger.info "SubjectPages:",
                       "skipped #{skipped.size} empty: #{skipped.join(', ')}"
  end
end
