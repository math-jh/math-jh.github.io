# frozen_string_literal: true
#
# graph_data.rb — 의존성 그래프 데이터 생성기.
#
# 빌드 끝(:site, :post_write)에 각 글의 "다른 글로의 교차참조"를 모아 force-graph 가
# 읽을 JSON 을 언어별로 떨군다:
#
#   assets/data/graph-ko.json , assets/data/graph-en.json
#   { "nodes": [{id,title,url,category}], "links": [{source,target,weight}] }
#
#   node = 글,  edge = "글 A 가 글 B 의 정의/정리/절을 인용"(방향 A→B, weight=링크 수).
#
# 렌더된 본문(doc.content, 레이아웃·사이드바 제외)만 스캔하므로 nav/사이드바의 글
# 링크는 엣지로 잡히지 않는다. 전역 그래프(/graph)와 로컬 그래프(글별 2-hop)가 공유.
require "json"
require "fileutils"

module GraphData
  LANGS = %w[ko en].freeze
  # 본문 내부의 다른 글 링크. content 가 렌더된 HTML 일 수도(href=), incremental
  # 빌드라 raw 마크다운(](/...))일 수도 있어 둘 다 잡는다. 한 글은 둘 중 한 형태뿐이라
  # 중복 카운트 없음.
  LINK_RES = [
    %r{href="(/(?:ko|en)/[A-Za-z0-9_\-/]+?)(?:#[^"]*)?"},
    %r{\]\((/(?:ko|en)/[A-Za-z0-9_\-/]+?)(?:#[^)\s]*)?\)}
  ].freeze

  # 카테고리(slug) → family(필터 칩·구분선·family 색용). 표에 없으면 misc.
  FAMILY = {
    "linear_algebra" => "foundations", "calculus" => "foundations",
    "set_theory" => "foundations", "category_theory" => "foundations",
    "algebraic_structures" => "algebra", "group_theory" => "algebra",
    "ring_theory" => "algebra", "multilinear_algebra" => "algebra",
    "field_theory" => "algebra", "homological_algebra" => "algebra",
    "commutative_algebra" => "algebra", "representation_theory" => "algebra",
    "number_theory" => "algebra",
    "analysis" => "analysis",
    "topology" => "geometry", "algebraic_topology" => "geometry",
    "manifolds" => "geometry", "lie_theory" => "geometry",
    "riemannian_geometry" => "geometry", "algebraic_varieties" => "geometry",
    "scheme_theory" => "geometry", "toric_geometry" => "geometry",
    "mirror_symmetry" => "geometry", "symplectic_geometry" => "geometry"
  }.freeze

  module_function

  # 카테고리는 URL 에서 뽑는다: /ko/math/category_theory/slug -> "category_theory"
  def category_of(doc)
    seg = doc.url.split("/").reject(&:empty?)
    return seg[-2] if seg.length >= 3
    seg.length >= 2 ? seg[1] : ""
  end

  def norm(url)
    url.to_s.sub(/#.*\z/, "").sub(/\.html\z/, "").sub(%r{/\z}, "")
  end

  # _data/hues.yml(키 "Math / Set_Theory" → {hue, sat})을 slug(set_theory) → hue 로.
  def hue_map(site)
    map = {}
    (site.data["hues"] || {}).each do |key, val|
      next unless val.is_a?(Hash) && val["hue"]
      slug = key.to_s.split(" / ").last.to_s.downcase.gsub(" ", "_")
      map[slug] = val["hue"]
    end
    map
  end

  def color_for(cat, hmap)
    h = hmap[cat]
    h ? "hsl(#{h}, 55%, 60%)" : "#8a8f98" # hues 없는 카테고리(llm_workshop 등)는 회색
  end

  def build(site, lang)
    hmap = hue_map(site)
    # 수학 글만(/<lang>/math/…). llm_workshop·blog_development·독서노트 등 메타 글 제외.
    docs = site.posts.docs.select { |d| d.url.start_with?("/#{lang}/math/") }
    by_url = {}
    docs.each { |d| by_url[norm(d.url)] = true }

    nodes = docs.map do |d|
      cat = category_of(d)
      {
        id: norm(d.url),
        title: (d.data["title"] || d.basename).to_s,
        url: d.url,
        category: cat,
        hue: (hmap[cat] || 0),
        family: (FAMILY[cat] || "misc"),
        color: color_for(cat, hmap)
      }
    end

    edges = Hash.new(0)
    docs.each do |d|
      src = norm(d.url)
      txt = d.content.to_s
      LINK_RES.each do |re|
        txt.scan(re) do |m|
          tgt = norm(m[0])
          next if tgt == src || !by_url.key?(tgt)
          edges[[src, tgt]] += 1
        end
      end
    end

    links = edges.map { |(s, t), w| { source: s, target: t, weight: w } }
    { nodes: nodes, links: links }
  end
end

Jekyll::Hooks.register :site, :post_write do |site|
  dir = File.join(site.dest, "assets", "data")
  GraphData::LANGS.each do |lang|
    data = GraphData.build(site, lang)
    next if data[:nodes].empty?
    FileUtils.mkdir_p(dir)
    File.write(File.join(dir, "graph-#{lang}.json"), JSON.generate(data))
  end
end
