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

  # _data/categories.yml 의 subjects("Math / Set Theory" → {ko, section, hue, sat, l})를
  # slug(set_theory) → hue 로.
  def hue_map(site)
    map = {}
    subjects(site).each do |key, val|
      next unless val.is_a?(Hash) && val["hue"]

      map[slug_of(key)] = val["hue"]
    end
    map
  end

  # slug → family(필터 칩·family 색). subjects 의 section 을 sections 의 family 로 옮긴다.
  # 예전에는 이 표가 여기 상수로 하드코딩돼 있었고, 거기 빠진 카테고리(복소해석학·
  # 복소기하학·층론·스택·유도대수기하·GW)가 조용히 "misc" 로 떨어져 그래프에서
  # 채도 0 의 회색 노드로 그려졌다. 이제 categories.yml 한 곳에서 파생한다.
  def family_map(site)
    sections = (site.data["categories"] || {})["sections"] || {}
    map = {}
    subjects(site).each do |key, val|
      next unless val.is_a?(Hash)

      section = sections[val["section"]] || {}
      map[slug_of(key)] = section["family"] || "misc"
    end
    map
  end

  def subjects(site)
    ((site.data["categories"] || {})["subjects"] || {})
  end

  # 필터 칩용 family 목록. Graph_page.js 가 data.families 로 받는다 — 예전엔 거기
  # FAMILIES 상수로 한 벌 더 있어서, categories.yml 에 family 를 추가해도 JS 가
  # 모르면 그 노드가 조용히 "misc"(채도 0 회색)로 떨어졌다.
  def families(site)
    ((site.data["categories"] || {})["families"] || {}).map do |key, val|
      { key: key, label: val["label"], label_ko: val["label_ko"], hue: val["hue"] }
    end
  end

  def slug_of(category)
    category.to_s.split(" / ").last.to_s.downcase.gsub(" ", "_")
  end

  def color_for(cat, hmap)
    h = hmap[cat]
    h ? "hsl(#{h}, 55%, 60%)" : "#8a8f98" # hues 없는 카테고리(llm_workshop 등)는 회색
  end

  def build(site, lang)
    hmap = hue_map(site)
    fmap = family_map(site)
    # 수학 글만(/<lang>/math/…). llm_workshop·blog_development·독서노트 등 메타 글 제외.
    docs = site.posts.docs.select { |d| d.url.start_with?("/#{lang}/math/") }
    by_url = {}
    docs.each { |d| by_url[norm(d.url)] = true }

    # category/weight lookup for filtering real prerequisites
    meta = {}
    docs.each do |d|
      cat = category_of(d)
      meta[norm(d.url)] = { category: cat, weight: d.data["weight"]&.to_i }
    end

    nodes = docs.map do |d|
      cat = category_of(d)
      {
        id: norm(d.url),
        title: (d.data["title"] || d.basename).to_s,
        url: d.url,
        category: cat,
        hue: (hmap[cat] || 0),
        family: (fmap[cat] || "misc"),
        color: color_for(cat, hmap)
      }
    end

    # edge direction: prerequisite -> dependent.
    # A link A -> B in post content means "A cites/uses B", i.e. A depends on B.
    # The dependency graph stores the reverse direction B -> A so arrows point from
    # prerequisite to dependent.
    #
    # Same-category forward citations (lighter post cites heavier post) are ignored,
    # because within a category weights define the reading order; such links are
    # previews/forward references, not real dependencies. Cross-category citations
    # are always reversed since weights are not comparable across categories.
    edges = Hash.new(0)
    docs.each do |d|
      src = norm(d.url)
      txt = d.content.to_s
      LINK_RES.each do |re|
        txt.scan(re) do |m|
          tgt = norm(m[0])
          next if tgt == src || !by_url.key?(tgt)

          s_meta = meta[src]
          t_meta = meta[tgt]
          same_cat = s_meta && t_meta && s_meta[:category] == t_meta[:category]

          if same_cat
            # Only keep edges where the citing post is heavier than the cited post.
            next unless s_meta[:weight] && t_meta[:weight]
            next unless s_meta[:weight] > t_meta[:weight]
          end

          edges[[tgt, src]] += 1
        end
      end
    end

    links = edges.map { |(s, t), w| { source: s, target: t, weight: w } }
    { nodes: nodes, links: links, families: families(site) }
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
