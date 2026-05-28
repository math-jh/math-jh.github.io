# frozen_string_literal: true

# Build-time link display normalizer.
#
# Rewrites internal cross-reference link display text in post bodies so that
# the rendered HTML always uses the canonical target title, label, and
# section heading, regardless of what the author wrote in source markdown.
# The source markdown files are NOT modified; only Jekyll's in-memory
# document content is touched.
#
# Patterns handled in display text:
#   1. `\[Category\] §Title, ⁋Label N`     — page+label, with category bracket
#   2. `\[Category\] §Title, §§H2 section`  — page+H2, with category bracket
#   3. `\[Category\] §Title`                — page link with category bracket
#   4. `§Title, ⁋Label N`                   — page+label, no category bracket
#   5. `§Title, §§H2 section`               — page+H2, no category bracket
#   6. `§Title`                             — bare page link
#   7. `Label N` with `(#labelN)` anchor    — in-document self-reference
#   8. plain term (e.g. `Set Theory`)       — category landing pages / terms
#
# Resolution rules:
#   - title:    target post's frontmatter title
#   - category: navigation.yml category-{ko,en} display name
#               — OMITTED if source and target are in the same category
#   - label:    `<ins id="…">**Label N**</ins>` text in the target post
#   - §§ H2:    `## …` heading text in the target post (slug match)
#   - in-doc:   look up label / H2 in the *source* doc itself
#
# Every override is logged to `scripts/audit/link-overrides.log` (gitignored,
# truncated at the start of each build). Each entry is a single-line JSON
# object: {source, url, original, canonical, bucket}.
#
# Buckets:
#   cosmetic/label-enrich  — plugin added a descriptive parenthetical to the
#                            label from the target's `<ins>` content
#                            (e.g. "예시 1" → "예시 1 (러셀의 역설)"). Source
#                            is fine; this is the plugin doing its job.
#   cosmetic/label-trim    — author's text had an extra parenthetical
#                            (e.g. `Proposition 6 (1)` referring to part 1
#                            of a multi-part statement) that the plugin
#                            stripped. Source carries human-added context
#                            that's lost in canonical — worth a glance.
#   cosmetic/same-cat-omit — source/target are in the same category so the
#                            plugin dropped the `\[Cat\]` bracket. Author
#                            could remove the bracket from source, but it's
#                            harmless either way.
#   title-drift            — target page title, category name, or section
#                            name changed; source displays stale text.
#                            Worth fixing in source.
#   anchor-dropped         — target anchor (#prop8 etc.) no longer exists;
#                            the `⁋Label N` tail was stripped. Source has
#                            a broken anchor.
#
# At end of build a final SUMMARY line is appended with bucket counts.

require "json"
require "fileutils"

module LinkNormalizer
  TRACKER_REL = File.join("scripts", "audit", "link-overrides.log")

  # display = capture 1; url = capture 2. URL may be an internal post path
  # (/ko/... or /en/...) or a same-document anchor (#labelN, #h2-slug).
  LINK_RE = /\[((?:[^\[\]]|\\\[|\\\])*?)\]\(((?:\/(?:ko|en)\/|#)[^\s)]*)\)/

  H2_RE = /^##(?!#)\s+(.+?)\s*$/

  class Maps
    attr_reader :title_by_url, :label_by_anchor, :h2_by_anchor, :category_by_lang

    def initialize(site)
      @title_by_url = {}
      @label_by_anchor = {}
      @h2_by_anchor = {}
      @category_by_lang = { "ko" => {}, "en" => {} }

      site.posts.docs.each do |doc|
        next unless doc.url =~ %r{\A/(ko|en)/}
        url = normalize_url(doc.url)
        title = (doc.data["title"] || "").to_s.strip
        @title_by_url[url] = title unless title.empty?

        body = doc.content.to_s
        body.scan(/<ins\s+id="([^"]+)">\s*\*\*([^*]+?)\*\*\s*<\/ins>/) do |id, label|
          @label_by_anchor["#{url}##{id}"] = label.strip
        end
        body.scan(H2_RE) do |h2|
          text = h2[0].strip
          slug = kramdown_slug(text)
          @h2_by_anchor["#{url}##{slug}"] = text
        end
      end

      build_category_map(site)
    end

    # Approximate kramdown auto_ids slug: lowercase, spaces -> '-', drop most
    # punctuation, keep Hangul + Han ideographs (the blog actually uses these
    # in anchors, e.g. `#극한의-보편성질`).
    def kramdown_slug(text)
      s = text.dup
      s.gsub!(/[^[:alnum:][:space:]一-鿿가-힯\-]+/, "")
      s.strip!
      s.gsub!(/\s+/, "-")
      s.downcase!
      s
    end

    def self.normalize_url(url)
      url.sub(/\.html\z/, "").sub(/\/\z/, "")
    end

    def normalize_url(url)
      self.class.normalize_url(url)
    end

    private

    def build_category_map(site)
      nav = site.data["navigation"] || {}
      %w[category-ko category-en].each do |key|
        sections = nav[key]
        next unless sections.is_a?(Array)
        lang = key.split("-").last
        sections.each do |section|
          children = (section.is_a?(Hash) ? section["children"] : nil) || []
          children.each do |cat|
            next unless cat.is_a?(Hash)
            url = cat["url"].to_s.sub(%r{\A/?}, "").sub(%r{/\z}, "")
            next if url.empty?
            slug = url.split("/").last
            title = (cat["title"] || "").to_s.strip
            @category_by_lang[lang][slug] = title unless title.empty?
          end
        end
      end
    end
  end

  # Classify an (original, canonical) pair into one of:
  #   cosmetic | title-drift | anchor-dropped
  module Triage
    CAT_RE   = /\A\\\[([^\]]+)\\\]\s*(.*)\z/
    TAIL_RE  = /,\s*([⁋§]{1,2}.*)\z/

    module_function

    def classify(original, canonical)
      o_cat, o_rest = split_cat(original)
      c_cat, c_rest = split_cat(canonical)

      if o_cat && c_cat && o_cat != c_cat
        return "title-drift/category-renamed"
      end

      # Same-category [Cat] bracket dropped by the plugin while rest is
      # otherwise identical → cosmetic/same-cat-omit.
      if o_cat && c_cat.nil? && o_rest == c_rest
        return "cosmetic/same-cat-omit"
      end

      o_sec, o_tail = split_tail(o_rest)
      c_sec, c_tail = split_tail(c_rest)

      if o_tail && c_tail.nil?
        # Footnote / 각주 references look like an anchor-drop but really
        # the plugin just doesn't track footnote anchors (#fn:N). Tag them
        # separately so they're not confused with broken anchors.
        return "title-drift/footnote-stripped" if o_tail =~ /\A(footnote|각주)\b/i
        return "anchor-dropped"
      end

      if o_sec != c_sec
        return paren_subbucket(o_sec, c_sec) if paren_add?(o_sec, c_sec)
        return "title-drift/section-renamed"
      end

      if o_tail != c_tail
        ot = strip_marker(o_tail.to_s)
        ct = strip_marker(c_tail.to_s)
        return paren_subbucket(ot, ct) if paren_add?(ot, ct)
        return "title-drift/label-renamed"
      end

      "cosmetic"
    end

    # Which direction was the parenthetical added?
    #   label-enrich: canonical has the extra `(…)` → plugin enriched
    #   label-trim:   original had the extra `(…)` → plugin stripped
    def paren_subbucket(a, b)
      return "cosmetic/label-enrich" if b.length > a.length
      "cosmetic/label-trim"
    end

    def split_cat(s)
      m = s.match(CAT_RE)
      m ? [m[1], m[2]] : [nil, s]
    end

    def split_tail(s)
      m = s.match(TAIL_RE)
      m ? [s[0...m.begin(0)].strip, m[1].strip] : [s.strip, nil]
    end

    def strip_marker(t)
      t.sub(/\A[⁋§]{1,2}\s*/, "")
    end

    def paren_add?(a, b)
      return true if !a.empty? && b.start_with?(a) && b =~ /\A#{Regexp.escape(a)}\s*\(.*\)\z/
      return true if !b.empty? && a.start_with?(b) && a =~ /\A#{Regexp.escape(b)}\s*\(.*\)\z/
      false
    end
  end

  class << self
    attr_accessor :maps, :tracker_io, :bucket_counts

    def category_slug_from_url(url)
      m = url.to_s.match(%r{\A/(?:ko|en)/(?:math/)?([A-Za-z0-9_]+)(?:/|$|#)})
      m ? m[1] : nil
    end

    # Returns [new_content, diffs]
    def normalize(content, source_path, source_url)
      source_cat = category_slug_from_url(source_url)
      source_url_norm = Maps.normalize_url(source_url)
      diffs = []
      new_content = content.gsub(LINK_RE) do |match|
        display = Regexp.last_match(1)
        url = Regexp.last_match(2)
        canonical = canonical_display(display, url, source_cat, source_url_norm)
        if canonical && canonical != display
          diffs << {
            "source" => source_path,
            "url" => url,
            "original" => display,
            "canonical" => canonical,
            "bucket" => Triage.classify(display, canonical),
          }
          "[#{canonical}](#{url})"
        else
          match
        end
      end
      [new_content, diffs]
    end

    def canonical_display(display, url, source_cat, source_url)
      if url.start_with?("#")
        canonical_indoc(display, url, source_url)
      else
        canonical_external(display, url, source_cat)
      end
    end

    # In-document refs: just the label text or H2 heading text.
    def canonical_indoc(_display, url, source_url)
      anchor = url[1..]
      key = "#{source_url}##{anchor}"
      maps.label_by_anchor[key] || maps.h2_by_anchor[key]
    end

    def canonical_external(display, url, source_cat)
      url_path, anchor = url.split("#", 2)
      url_path = url_path.sub(%r{/\z}, "")
      lang = url_path.start_with?("/ko/") ? "ko" : "en"

      target_title = maps.title_by_url[url_path]
      target_cat = category_slug_from_url(url_path)
      cat_name = target_cat ? maps.category_by_lang[lang][target_cat] : nil

      # Category landing page (e.g., /ko/set_theory)
      if target_title.nil? && cat_name && url_path.count("/") <= 2
        return cat_name if !display.include?("\\[") && !display.include?("§")
        target_title = cat_name
      end
      return nil if target_title.nil?

      label_text = anchor ? maps.label_by_anchor["#{url_path}##{anchor}"] : nil
      h2_text    = anchor ? maps.h2_by_anchor["#{url_path}##{anchor}"]    : nil

      has_cat = display.start_with?("\\[")
      has_h2  = display.include?("§§")
      # `§` only when it's the page marker (§foo), not the H2 marker (§§foo).
      # has_section: the display contains §Title, regardless of §§ presence.
      has_section = display =~ /(^|[^§])§[^§]/ ? true : false
      has_label   = display.include?("⁋")

      # Same-category source/target: drop the [Category] bracket.
      same_cat = source_cat && target_cat && source_cat == target_cat

      pieces = []
      if has_cat && cat_name && !same_cat
        pieces << "\\[#{cat_name}\\]"
      end
      if has_section
        pieces << "§#{target_title}"
      elsif !has_cat && !has_label && !has_h2
        # Plain term — just the title.
        pieces << target_title
      end

      if has_h2 && h2_text
        pieces << target_title if pieces.empty?
        pieces[-1] = "#{pieces[-1]}, §§#{h2_text}"
      elsif has_label && label_text
        pieces << target_title if pieces.empty?
        pieces[-1] = "#{pieces[-1]}, ⁋#{label_text}"
      end
      pieces.empty? ? nil : pieces.join(" ")
    end
  end
end

Jekyll::Hooks.register :site, :pre_render do |site|
  # Skip during local livereload serve — only run on production CI builds.
  # Avoids overhead on every save and prevents the daemon's stale-plugin
  # rebuilds from clobbering the tracker log.
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
  # Jekyll 4's Document#content= writer doesn't always replace @content for
  # posts; setting the ivar directly is the reliable mutation path.
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
    %w[
      cosmetic
      cosmetic/label-enrich
      cosmetic/label-trim
      cosmetic/same-cat-omit
      title-drift
      title-drift/section-renamed
      title-drift/category-renamed
      title-drift/label-renamed
      title-drift/footnote-stripped
      anchor-dropped
    ].each { |k| summary[k] = counts[k] || 0 }
    io.puts JSON.generate(summary) rescue nil
    io.close
  end
  LinkNormalizer.tracker_io = nil
  LinkNormalizer.bucket_counts = nil
end
