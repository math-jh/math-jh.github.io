# 빈 카테고리의 과목홈(subject home)을 빌드에서 제외한다.
#
# 과목홈은 `_pages/{ko,en}/Math-*.md` 처럼 layout: archive_custom 을 쓰고, permalink
# 의 첫 구간 뒤가 카테고리 슬러그다:
#
#   "Math / Category Theory"  →  /ko/category_theory/
#   "Math / Gromov-Witten Theory" → /ko/gromov-witten_theory/
#
# (subject-grid.html · _layouts/default.html 의 hero hue 조회와 같은 규칙:
#  " / " 뒤를 소문자로 바꾸고 공백을 _ 로.)
#
# 해당 카테고리에 그 언어의 글이 하나도 없으면 페이지를 site.pages 에서 빼서 아예
# 빌드하지 않는다. 덕분에 _config.yml 의 categories-*_order 에 미발행 카테고리를
# 남겨 둬도 빈 과목홈이 생기지 않는다 (카테고리 목록 페이지 쪽 숨김은
# _layouts/categories-*.html 이 담당).
#
# published: false 초안은 Jekyll 이 site.posts 에서 이미 제외하므로, production 에서는
# 숨고 `--unpublished` 로 띄운 로컬 프리뷰에서는 정상적으로 보인다.
#
# 슬러그가 어떤 카테고리와도 안 맞는 archive_custom 페이지(/ko/math/ 같은 허브)는
# 손대지 않는다. frontmatter 에 `category:` 를 직접 적어 두면 그 값이 우선한다.

module HideEmptySubjectPages
  LAYOUT = "archive_custom".freeze

  module_function

  def slug_for(category)
    category.split(" / ").last.to_s.downcase.tr(" ", "_")
  end

  def lang_of(url)
    return "en" if url.start_with?("/en/")
    return "ko" if url.start_with?("/ko/")

    nil
  end

  # _config.yml 의 순서 목록과 hues.yml 키를 합쳐 "슬러그 → 카테고리명" 표를 만든다.
  # 글이 0편인 카테고리도 여기에는 남아 있어야 하므로 site.categories 는 쓸 수 없다.
  def slug_index(site)
    names = []
    hues = site.data["hues"]
    names.concat(hues.keys) if hues.is_a?(Hash)
    %w[categories-ko_order categories-en_order].each do |key|
      list = site.config[key]
      names.concat(list) if list.is_a?(Array)
    end

    names.uniq.each_with_object({}) { |name, acc| acc[slug_for(name)] = name }
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
end

Jekyll::Hooks.register :site, :post_read do |site|
  by_slug = HideEmptySubjectPages.slug_index(site)
  counts = HideEmptySubjectPages.post_counts(site)
  skipped = []

  site.pages.reject! do |page|
    next false unless page.data["layout"] == HideEmptySubjectPages::LAYOUT

    lang = HideEmptySubjectPages.lang_of(page.url)
    next false if lang.nil?

    slug = HideEmptySubjectPages.slug_of_page(page.url)
    category = page.data["category"] || by_slug[slug]
    next false if category.nil?          # 허브 페이지(/ko/math/) 등은 그대로 둔다
    next false unless counts[[category, lang]].zero?

    skipped << "#{page.url} (#{category})"
    true
  end

  unless skipped.empty?
    Jekyll.logger.info "EmptyCategories:",
                       "skipped #{skipped.size} empty subject page(s): #{skipped.join(', ')}"
  end
end
