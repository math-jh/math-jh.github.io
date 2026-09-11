# frozen_string_literal: true
#
# graph_data.rb — 의존성 그래프 데이터 생성기.
#
# 빌드 끝(:site, :post_write)에 각 글의 "다른 글로의 교차참조"를 모아 force-graph 가
# 읽을 JSON 을 언어별로 떨군다:
#
#   assets/data/dependencies-ko.json , assets/data/dependencies-en.json
#   { "nodes": [{id,title,url,category,weight}],
#     "links": [{source,target,weight,relation,relations}] }
#
#   node = 글,  edge = 분류(data-relation)된 인용. required·weak 은 선수 글 → 후속 글로
#   방향을 뒤집고, forward 는 현재 글 → 나중 글이라는 원래 방향을 유지한다.
#
# 렌더된 본문(doc.content, 레이아웃·사이드바 제외)만 스캔하므로 nav/사이드바의 글
# 링크는 엣지로 잡히지 않는다. 전역 그래프(/dependencies)와 로컬 그래프(글별 2-hop)가 공유.
require "json"
require "fileutils"

module GraphData
  LANGS = %w[ko en].freeze
  RELATION_PRIORITY = { "weak" => 0, "forward" => 1, "required" => 2 }.freeze
  RECOMMENDATION_LIMIT = 3

  # 분류가 끝난 링크만 그래프에 넣는다. 보통 post_write 시점의 d.content 는 raw
  # Markdown이지만 빌드 경로에 따라 렌더된 HTML일 수도 있으므로 두 표현을 모두 지원한다.
  RAW_CLASSIFIED_LINK_RE = %r!\]\((/(?:ko|en)/[A-Za-z0-9_\-/]+?)(?:#[^)\s]*)?\)\{:[^}]*\bdata-relation=["'](required|weak|forward)["'][^}]*\}!.freeze
  HTML_ANCHOR_RE = %r{<a\b[^>]*>}.freeze
  HTML_HREF_RE = %r{\bhref=["'](/(?:ko|en)/[A-Za-z0-9_\-/]+?)(?:#[^"']*)?["']}.freeze
  HTML_RELATION_RE = /\bdata-relation=["'](required|weak|forward)["']/.freeze


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

  def classified_links(text)
    found = []
    text.to_s.scan(RAW_CLASSIFIED_LINK_RE) { |url, relation| found << [url, relation] }
    text.to_s.scan(HTML_ANCHOR_RE) do |anchor|
      href = anchor.match(HTML_HREF_RE)
      relation = anchor.match(HTML_RELATION_RE)
      found << [href[1], relation[1]] if href && relation
    end
    found
  end

  # Build the citation-level semantic model once and share it between the graph
  # JSON and the per-post reading blocks.  `classified_by_source` deliberately
  # records self-links and links to pages outside the graph: the display contract
  # is "hide everything when this post has no classified IAL at all", not "hide
  # everything when this post has no usable inter-post edge".
  def dependency_model(site, lang)
    docs = site.posts.docs.select { |d| d.url.start_with?("/#{lang}/math/") }
    by_url = {}
    docs.each { |d| by_url[norm(d.url)] = d }

    classified_by_source = {}
    cited_pairs = {}
    docs.each do |d|
      src = norm(d.url)
      links = classified_links(d.content)
      classified_by_source[src] = true unless links.empty?

      links.each do |raw_target, relation|
        tgt = norm(raw_target)
        next if tgt == src || !by_url.key?(tgt)

        key = [src, tgt]
        entry = (cited_pairs[key] ||= {
          counts: Hash.new(0), weight: 0, relation: "weak"
        })
        entry[:counts][relation] += 1
        entry[:weight] += 1
        if RELATION_PRIORITY[relation] > RELATION_PRIORITY[entry[:relation]]
          entry[:relation] = relation
        end
      end
    end

    {
      docs: docs,
      by_url: by_url,
      classified_by_source: classified_by_source,
      cited_pairs: cited_pairs
    }
  end

  def reading_entry(doc, extra = {})
    {
      "title" => (doc.data["title"] || doc.basename).to_s,
      "url" => doc.url
    }.merge(extra)
  end

  def reachable_from(start, adjacency)
    seen = {}
    stack = Array(adjacency[start]).dup
    until stack.empty?
      node = stack.pop
      next if seen[node]

      seen[node] = true
      stack.concat(Array(adjacency[node]))
    end
    seen
  end

  # Stable topological ranking of recommendation candidates.  Required paths
  # win over every popularity signal; within the same available frontier, direct
  # citation count is the strength signal.  Reciprocal reachability means a
  # required SCC, so those candidates are tied rather than deadlocking the sort.
  def rank_recommendations(candidates, cited_pairs, by_url)
    required_adjacency = Hash.new { |h, k| h[k] = [] }
    cited_pairs.each do |(src, tgt), entry|
      required_adjacency[tgt] << src if entry[:relation] == "required"
    end

    urls = candidates.keys
    reachability = {}
    urls.each { |url| reachability[url] = reachable_from(url, required_adjacency) }

    outgoing = Hash.new { |h, k| h[k] = [] }
    indegree = Hash.new(0)
    urls.combination(2) do |left, right|
      left_before = reachability[left][right]
      right_before = reachability[right][left]
      next if left_before == right_before # incomparable, or in the same SCC

      source, target = left_before ? [left, right] : [right, left]
      outgoing[source] << target
      indegree[target] += 1
    end

    sort_key = lambda do |url|
      candidate = candidates[url]
      doc = by_url[url]
      relation_rank = candidate[:relations].map { |r| RELATION_PRIORITY[r] }.max || 0
      [
        -candidate[:strength],
        -relation_rank,
        doc.data["weight"] ? doc.data["weight"].to_i : (1 << 30),
        (doc.data["title"] || doc.basename).to_s,
        url
      ]
    end

    ready = urls.select { |url| indegree[url].zero? }.sort_by(&sort_key)
    ordered = []
    until ready.empty?
      url = ready.shift
      ordered << url
      outgoing[url].each do |target|
        indegree[target] -= 1
        if indegree[target].zero?
          ready << target
          ready.sort_by!(&sort_key)
        end
      end
    end

    # The SCC rule above should make the candidate constraint graph acyclic.
    # Keep an explicit deterministic fallback so malformed future data cannot
    # make recommendations disappear silently.
    ordered.concat((urls - ordered).sort_by(&sort_key))
    ordered
  end

  def semantic_navigation(site, lang, current_url, limit: RECOMMENDATION_LIMIT, model: nil)
    model ||= dependency_model(site, lang)
    current = norm(current_url)
    return nil unless model[:classified_by_source][current]

    required = []
    weak = []
    model[:cited_pairs].each do |(src, tgt), entry|
      next unless src == current

      target_doc = model[:by_url][tgt]
      case entry[:relation]
      when "required"
        required << reading_entry(target_doc)
      when "weak"
        weak << reading_entry(target_doc)
      end
    end

    entry_sort = lambda do |entry|
      doc = model[:by_url][norm(entry["url"])]
      [doc.data["weight"] ? doc.data["weight"].to_i : (1 << 30), entry["title"], entry["url"]]
    end
    required.sort_by!(&entry_sort)
    weak.sort_by!(&entry_sort)

    candidates = {}
    add_candidate = lambda do |url, relation, strength|
      candidate = (candidates[url] ||= { strength: 0, relations: [] })
      candidate[:strength] += strength
      candidate[:relations] << relation unless candidate[:relations].include?(relation)
    end

    model[:cited_pairs].each do |(src, tgt), entry|
      if tgt == current && %w[required weak].include?(entry[:relation])
        add_candidate.call(src, entry[:relation], entry[:weight])
      elsif src == current && entry[:relation] == "forward"
        add_candidate.call(tgt, "forward", entry[:weight])
      end
    end

    current_doc = model[:by_url][current]
    current_weight = current_doc.data["weight"]&.to_i
    weight_next_doc = if current_weight
      model[:docs]
        .select do |doc|
          doc_weight = doc.data["weight"]&.to_i
          category_of(doc) == category_of(current_doc) && doc_weight && doc_weight > current_weight
        end
        .min_by do |doc|
          [doc.data["weight"].to_i, (doc.data["title"] || doc.basename).to_s, doc.url]
        end
    end
    weight_next_url = weight_next_doc && norm(weight_next_doc.url)

    next_reads = rank_recommendations(candidates, model[:cited_pairs], model[:by_url])
      .reject { |url| url == weight_next_url }
      .first(limit)
      .map do |url|
        candidate = candidates[url]
        reading_entry(model[:by_url][url], {
          "strength" => candidate[:strength],
          "relations" => candidate[:relations]
        })
      end

    {
      "required" => required,
      "weak" => weak,
      "weight_next" => weight_next_doc && reading_entry(weight_next_doc),
      "next" => next_reads
    }
  end

  # Semantic dependency data for /<lang>/dependencies only.
  #
  # Aggregation happens twice. First, all citations from A to B are collapsed and
  # required wins over forward/weak. Then semantic directions are assigned and
  # reciprocal citations that reinforce the same prerequisite direction are merged.
  def build_dependencies(site, lang)
    hmap = hue_map(site)
    fmap = family_map(site)
    model = dependency_model(site, lang)
    docs = model[:docs]

    nodes = docs.map do |d|
      cat = category_of(d)
      {
        id: norm(d.url),
        title: (d.data["title"] || d.basename).to_s,
        url: d.url,
        category: cat,
        weight: d.data["weight"]&.to_i,
        hue: (hmap[cat] || 0),
        family: (fmap[cat] || "misc"),
        color: color_for(cat, hmap)
      }
    end

    directed = {}
    model[:cited_pairs].each do |(src, tgt), entry|
      relation = entry[:relation]
      edge_key = relation == "forward" ? [src, tgt] : [tgt, src]
      edge = (directed[edge_key] ||= {
        counts: Hash.new(0), weight: 0, relation: "weak"
      })
      entry[:counts].each { |kind, count| edge[:counts][kind] += count }
      edge[:weight] += entry[:weight]
      if RELATION_PRIORITY[relation] > RELATION_PRIORITY[edge[:relation]]
        edge[:relation] = relation
      end
    end

    links = directed.map do |(source, target), entry|
      {
        source: source,
        target: target,
        weight: entry[:weight],
        relation: entry[:relation],
        relations: entry[:counts]
      }
    end
    { nodes: nodes, links: links, families: families(site), classified: true }
  end
end

Jekyll::Hooks.register :site, :pre_render do |site|
  GraphData::LANGS.each do |lang|
    model = GraphData.dependency_model(site, lang)
    site.posts.docs.each do |doc|
      next unless doc.url.start_with?("/#{lang}/math/")

      doc.data.delete("semantic_navigation")
      navigation = GraphData.semantic_navigation(site, lang, doc.url, model: model)
      doc.data["semantic_navigation"] = navigation if navigation
    end
  end
end

Jekyll::Hooks.register :site, :post_write do |site|
  dir = File.join(site.dest, "assets", "data")
  GraphData::LANGS.each do |lang|
    data = GraphData.build_dependencies(site, lang)
    next if data[:nodes].empty?
    FileUtils.mkdir_p(dir)
    File.write(File.join(dir, "dependencies-#{lang}.json"), JSON.generate(data))
  end
end
