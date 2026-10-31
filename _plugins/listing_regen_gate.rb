# frozen_string_literal: true
#
# listing_regen_gate.rb — serve 의 watch 리빌드에서, 목록·데이터 페이지는 그 입력이 그대로면
# 다시 렌더하지 않는다.
#
# 과목홈 54개·Misc 목록·Terms·Notations(archive_custom), 카테고리 아카이브(categories),
# 최근 글(recent), terms.json 은 regenerate: true 이고 sitemap.xml 은 소스 없는 생성
# 페이지라, 글 하나의 본문만 고쳐도 리빌드마다 65개가 전부 다시 렌더됐다 (~3s,
# 2026-10-31 측정). 이 페이지들은 글 본문을 읽지 않는다. 그래서 각자 실제로 읽는 입력을
# 지문으로 묶어, 지난 빌드와 같고 출력 파일이 있으면 Regenerator 가 건너뛰게 한다.
#
# 묶음 둘 (모두 _layouts·_includes 파일 stamp, 전체 문서·페이지 URL 목록(seo.html 의
# hreflang), 자기 페이지들의 데이터·소스 내용을 공통으로 넣는다):
#   terms     — /ko/terms·/ko/notations·terms.json. _data 전부를 본다 (terms·notations 포함).
#               글의 frontmatter·요약문은 안 본다.
#   structure — 과목홈·Misc 목록(archive_custom)·카테고리 아카이브(categories)·최근 글
#               (recent)·sitemap. _data 는 terms·notations 를 빼고, 글은 목록 구조를 정하는
#               필드만(STRUCTURE_FIELDS — 제목·카테고리·순서·게시일·permalink·sitemap 등)
#               본다. **수정일(last_modified_at)과 요약문(excerpt)은 일부러 뺐다**: 즉시
#               반영할 것은 글 추가·삭제(와 드문 구조 필드 변경)뿐이고, 수정일·요약문은
#               정기 재시작(RuntimeMaxSec=3h)·full-rebuild 때 반영되면 된다는 사용자 결정
#               (2026-10-31). 그래서 최근 글의 수정일·요약, sitemap 의 lastmod, 과목 카드·
#               아카이브의 요약은 그때까지 옛것일 수 있다.
# 공통 제외: _data 의 link_relations*(글 페이지만 읽고 분류기 틱마다 바뀐다)·page_urls(URL
# 목록으로 대신). read_time 이 켜진 글은 본문까지 넣는다 (page__meta 가 단어 수를 센다).
# 프로세스 첫 빌드와, 빌드가 중간에 실패한 다음 빌드는 지문 비교 없이 전부 렌더한다
# (지문은 post_write 에서만 확정한다).
#
# 대상은 아래 상수로 고른 페이지뿐이다 — 피드(본문을 싣는다)·CSS·글은 손대지 않는다.
# 대상 페이지가 새 입력(글 본문, 다른 필드, 다른 _data)을 읽기 시작하면 해당 묶음 지문에도
# 넣어야 한다 — 안 그러면 그 변경이 미리보기에 안 뜬다.
# serve 의 incremental 에서만 켠다; 일회성 build(CI)에는 영향이 없다.
require "digest"

module ListingRegenGate
  TERMS_URLS = %w[/ko/terms /ko/notations /assets/data/terms.json].freeze
  STRUCTURE_LAYOUTS = %w[archive_custom categories recent].freeze
  STRUCTURE_URLS = %w[/sitemap.xml].freeze
  EXCLUDED_DATA = %w[link_relations link_relations_next page_urls].freeze
  TERMS_DATA = %w[terms notations].freeze
  # archive-single·subject-cards·page__meta·nav_recents·categories·recent 레이아웃과 sitemap 이
  # 글에서 읽는 필드 중 즉시 반영할 것 (last_modified_at·excerpt 는 지연 반영 — 위 주석)
  STRUCTURE_FIELDS = %w[title categories category weight date permalink header link
                        published sitemap read_time show_date words_per_minute].freeze
  STATE = { terms: {}, structure: {} } # 묶음 => { current:, last: }

  module_function

  def group_of(page)
    return nil unless page.is_a?(Jekyll::Page)
    return :terms if TERMS_URLS.include?(page.url)
    return :structure if STRUCTURE_LAYOUTS.include?(page.data["layout"]) || STRUCTURE_URLS.include?(page.url)

    nil
  end

  def gated?(page)
    !group_of(page).nil?
  end

  # 값만 보는 정규 직렬화를 digest 에 흘려 넣는다. Marshal 은 한 덩어리 안에서 같은
  # 객체를 두 번 만나면 링크로 적어서, 값이 같아도 객체 공유 모양이 빌드마다 달라지면
  # 바이트가 달라진다 — 그래서 지문으로 쓰지 않는다. 모르는 타입은 inspect (주소가 섞이면
  # 지문이 매번 달라져 그냥 다시 렌더할 뿐이니, 틀리더라도 안전한 쪽이다).
  def canon(obj, out)
    case obj
    when Hash
      out << "{"
      obj.each { |k, v| canon(k, out); out << "=>"; canon(v, out); out << "," }
      out << "}"
    when Array
      out << "["
      obj.each { |v| canon(v, out); out << "," }
      out << "]"
    when String then out << "s" << obj.bytesize.to_s << ":" << obj
    when Symbol then out << ":" << obj.to_s << ";"
    when Integer, Float, true, false, nil then out << obj.inspect << ";"
    when Time then out << "t" << obj.strftime("%Y-%m-%dT%H:%M:%S.%N%z") << ";"
    when Date then out << "d" << obj.iso8601 << ";"
    else
      if defined?(Jekyll::LastModifiedAt::Determinator) && obj.is_a?(Jekyll::LastModifiedAt::Determinator)
        out << "lm:" << obj.page_path.to_s << ";"
      else
        out << "?" << obj.inspect << ";"
      end
    end
    out
  end

  def file_stamp(path)
    st = File.stat(path)
    "#{path}\0#{st.mtime.to_i}.#{st.mtime.nsec}\0#{st.size}\0#{st.ino}\0"
  rescue SystemCallError
    "#{path}\0-\0"
  end

  def own_pages(site, group, out)
    site.pages.select { |p| group_of(p) == group }.sort_by { |p| [p.url, p.relative_path.to_s] }.each do |page|
      out << page.url << "\0" << page.relative_path.to_s << "\0"
      canon(page.data.reject { |k, _| k == "regenerate" }, out)
      out << page.content.to_s << "\0"
    end
  end

  # { terms:, structure: } 각 hex. 공통 부분은 한 번만 계산한다.
  def fingerprints(site)
    docs = site.collections.each_value.flat_map(&:docs).sort_by(&:path)
    common = Digest::SHA256.new
    %w[layouts_dir includes_dir].each do |key|
      dir = site.in_source_dir(site.config[key] || "_#{key.delete_suffix('_dir')}")
      Dir.glob(File.join(dir, "**", "*")).sort.each { |f| common << file_stamp(f) }
    end
    common << (docs.map(&:url) + site.pages.map(&:url)).sort.join("\0")
    data = site.data.reject { |k, _| EXCLUDED_DATA.include?(k) }
    common << "|data|"
    canon(data.reject { |k, _| TERMS_DATA.include?(k) }, common)
    common = common.hexdigest

    terms = Digest::SHA256.new << common
    canon(data.select { |k, _| TERMS_DATA.include?(k) }, terms)
    own_pages(site, :terms, terms)

    structure = Digest::SHA256.new << common
    docs.each do |doc|
      structure << "#{doc.relative_path}\0#{doc.url}\0"
      canon(doc.data.slice(*STRUCTURE_FIELDS), structure)
      structure << doc.content.to_s if doc.data["read_time"]
    end
    own_pages(site, :structure, structure)
    # sitemap 이 읽는 페이지 쪽 입력 — 페이지 데이터(sitemap: false 등)와 정적 파일 목록
    site.pages.sort_by { |p| [p.url, p.relative_path.to_s] }.each do |page|
      structure << page.url << "\0"
      canon(page.data.reject { |k, _| %w[regenerate last_modified_at].include?(k) }, structure)
    end
    structure << site.static_files.map(&:relative_path).sort.join("\0")

    { terms: terms.hexdigest, structure: structure.hexdigest }
  end

  def skip?(site, page)
    group = group_of(page) or return false
    state = STATE[group]
    state[:current] && state[:current] == state[:last] && File.exist?(page.destination(site.dest))
  end

  module Regen
    def regenerate?(document)
      return false if ListingRegenGate.skip?(site, document)

      super
    end
  end
end

Jekyll::Regenerator.prepend(ListingRegenGate::Regen)

# 다른 pre_render 훅(graph_data·page_url_index 등)이 끝난 뒤에 계산한다.
Jekyll::Hooks.register :site, :pre_render, priority: Jekyll::Hooks::PRIORITY_MAP[:low] do |site|
  fps = site.config["serving"] && site.incremental? ? ListingRegenGate.fingerprints(site) : {}
  ListingRegenGate::STATE.each { |group, state| state[:current] = fps[group] }
end

# 쓰기까지 끝난 빌드의 지문만 다음 빌드의 비교 기준이 된다.
Jekyll::Hooks.register :site, :post_write do |_site|
  ListingRegenGate::STATE.each_value { |state| state[:last] = state[:current] }
end
