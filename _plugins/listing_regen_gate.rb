# frozen_string_literal: true
#
# listing_regen_gate.rb — serve 의 watch 리빌드에서, 목록·데이터 페이지는 그 입력이 그대로면
# 다시 렌더하지 않는다.
#
# 과목홈 54개·Misc 목록·Terms·Notations(archive_custom), 카테고리 아카이브(categories),
# 최근 글(recent), terms.json 은 regenerate: true 이고 sitemap.xml 은 소스 없는 생성
# 페이지라, 글 하나의 본문만 고쳐도 리빌드마다 65개가 전부 다시 렌더됐다 (~3s,
# 2026-10-31 측정). 이 페이지들이 읽는 것은 글 본문이 아니라 글의 frontmatter·요약문·
# 수정일·URL, _data, 페이지 목록, 템플릿이다. 그것들을 지문 하나로 묶어, 지난 빌드와
# 같고 출력 파일이 있으면 Regenerator 가 이 페이지들을 건너뛰게 한다.
#
# 지문에 넣는 것: _data 전부(link_relations*·page_urls 제외 — 목록 페이지는 안 읽고,
# 앞의 것은 분류기 틱마다 바뀐다), 모든 컬렉션 문서의 경로·URL·frontmatter·요약문
# (read_time 이 켜진 글은 본문까지 — page__meta 가 단어 수를 센다), 모든 페이지의
# URL·데이터와 대상 페이지의 소스 내용, 정적 파일 목록(sitemap), _layouts·_includes
# 파일 각각의 mtime·크기·inode. 프로세스 첫 빌드와, 빌드가 중간에 실패한 다음 빌드는
# 지문 비교 없이 전부 렌더한다 (지문은 post_write 에서만 확정한다).
#
# 대상은 아래 LAYOUTS·URLS 로 고른 것뿐이다 — 피드(본문을 싣는다)·CSS·글은 손대지 않는다.
# 새 목록 페이지가 본문을 읽기 시작하면(예: post.content) 여기 지문에도 넣어야 한다.
# serve 의 incremental 에서만 켠다; 일회성 build(CI)에는 영향이 없다.
require "digest"

module ListingRegenGate
  LAYOUTS = %w[archive_custom categories recent].freeze
  URLS = %w[/assets/data/terms.json /sitemap.xml].freeze
  EXCLUDED_DATA = %w[link_relations link_relations_next page_urls].freeze
  DOC_VOLATILE = %w[excerpt semantic_navigation regenerate].freeze
  STATE = { current: nil, last: nil }

  module_function

  def gated?(page)
    page.is_a?(Jekyll::Page) && (LAYOUTS.include?(page.data["layout"]) || URLS.include?(page.url))
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

  def fingerprint(site)
    d = Digest::SHA256.new
    canon(site.data.reject { |k, _| EXCLUDED_DATA.include?(k) }, d)
    site.collections.each_value.flat_map(&:docs).sort_by(&:path).each do |doc|
      d << doc.relative_path.to_s << "\0" << doc.url << "\0"
      canon(doc.data.reject { |k, _| DOC_VOLATILE.include?(k) }, d)
      excerpt = doc.data["excerpt"]
      d << (excerpt.respond_to?(:content) ? excerpt.content : excerpt).to_s << "\0"
      d << doc.content.to_s if doc.data["read_time"]
    end
    site.pages.sort_by { |p| [p.url, p.relative_path.to_s] }.each do |page|
      d << page.url << "\0" << page.relative_path.to_s << "\0"
      canon(page.data.reject { |k, _| k == "regenerate" }, d)
      d << page.content.to_s << "\0" if gated?(page)
    end
    d << site.static_files.map(&:relative_path).sort.join("\0")
    %w[layouts_dir includes_dir].each do |key|
      dir = site.in_source_dir(site.config[key] || "_#{key.delete_suffix('_dir')}")
      Dir.glob(File.join(dir, "**", "*")).sort.each { |f| d << file_stamp(f) }
    end
    d.hexdigest
  end

  def skip?(site, page)
    STATE[:current] && STATE[:current] == STATE[:last] && gated?(page) &&
      File.exist?(page.destination(site.dest))
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
  ListingRegenGate::STATE[:current] =
    (site.config["serving"] && site.incremental? ? ListingRegenGate.fingerprint(site) : nil)
end

# 쓰기까지 끝난 빌드의 지문만 다음 빌드의 비교 기준이 된다.
Jekyll::Hooks.register :site, :post_write do |_site|
  ListingRegenGate::STATE[:last] = ListingRegenGate::STATE[:current]
end
