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
# object: {source, url, original, canonical}.

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

  class << self
    attr_accessor :maps, :tracker_io

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
  LinkNormalizer.maps = LinkNormalizer::Maps.new(site)

  tracker_path = File.join(site.source, LinkNormalizer::TRACKER_REL)
  FileUtils.mkdir_p(File.dirname(tracker_path))
  LinkNormalizer.tracker_io = File.open(tracker_path, "w")
end

Jekyll::Hooks.register :documents, :pre_render do |doc|
  next unless doc.url =~ %r{\A/(ko|en)/}
  next unless doc.content.is_a?(String)
  new_content, diffs = LinkNormalizer.normalize(doc.content, doc.relative_path, doc.url)
  # Jekyll 4's Document#content= writer doesn't always replace @content for
  # posts; setting the ivar directly is the reliable mutation path.
  doc.instance_variable_set(:@content, new_content) unless diffs.empty?
  diffs.each do |d|
    LinkNormalizer.tracker_io.puts JSON.generate(d) rescue nil
  end
end

Jekyll::Hooks.register :site, :post_write do |_site|
  LinkNormalizer.tracker_io&.close
  LinkNormalizer.tracker_io = nil
end
