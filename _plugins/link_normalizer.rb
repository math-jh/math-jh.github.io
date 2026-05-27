# frozen_string_literal: true

# Build-time link display normalizer.
#
# Rewrites internal cross-reference link display text in post bodies so that
# the rendered HTML always uses the canonical target title and label,
# regardless of what the author wrote in source markdown. The source markdown
# files are NOT modified; only Jekyll's in-memory document content is touched.
#
# Patterns handled in display text:
#   1. `\[Category\] §Title, ⁋Label N`  ← most common form with anchor
#   2. `\[Category\] §Title`             ← page link with category bracket
#   3. `§Title, ⁋Label N`                ← page+label, no category bracket
#   4. `§Title`                          ← bare page link
#   5. plain term (e.g. `Set Theory`)    ← category landing pages / terms
#
# For each detected link, the plugin computes a canonical display by:
#   - looking up the target post's frontmatter title from its URL
#   - looking up `<ins id="...">**Label N**</ins>` text for any #anchor
#   - looking up category display name from _data/navigation.yml
#
# Every override is logged to `scripts/audit/link-overrides.log` (gitignored,
# truncated at the start of each build). Each entry is a single-line JSON
# object: {source, url, original, canonical}.
#
# Applies to both /ko/ and /en/ documents — KO bodies resolve targets in KO
# space, EN bodies in EN space.

require "json"
require "fileutils"

module LinkNormalizer
  TRACKER_REL = File.join("scripts", "audit", "link-overrides.log")

  # display = group 1 (allows escaped \[ \] inside), url = group 2
  LINK_RE = /\[((?:[^\[\]]|\\\[|\\\])*?)\]\((\/(?:ko|en)\/[^\s)]+)\)/

  class Maps
    attr_reader :title_by_url, :label_by_anchor, :category_by_lang

    def initialize(site)
      @title_by_url = {}
      @label_by_anchor = {}
      @category_by_lang = { "ko" => {}, "en" => {} }

      site.posts.docs.each do |doc|
        next unless doc.url =~ %r{\A/(ko|en)/}
        url = doc.url.sub(/\.html\z/, "").sub(/\/\z/, "")
        title = (doc.data["title"] || "").to_s.strip
        @title_by_url[url] = title unless title.empty?

        # Capture <ins id="...">**Label N**</ins> labels for in-page anchors
        doc.content.to_s.scan(
          /<ins\s+id="([^"]+)">\s*\*\*([^*]+?)\*\*\s*<\/ins>/
        ) do |id, label|
          key = "#{url}##{id}"
          @label_by_anchor[key] = label.strip
        end
      end

      build_category_map(site)
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

    # Returns [new_content, diffs] where diffs is an array of hashes.
    def normalize(content, source_path)
      diffs = []
      new_content = content.gsub(LINK_RE) do |match|
        display = Regexp.last_match(1)
        url = Regexp.last_match(2)
        canonical = canonical_display(display, url)
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

    def canonical_display(display, url)
      url_path, anchor = url.split("#", 2)
      url_path = url_path.sub(%r{/\z}, "")
      lang = url_path.start_with?("/ko/") ? "ko" : "en"

      target_title = maps.title_by_url[url_path]

      # Category slug: matches /lang/CAT or /lang/math/CAT
      cat_slug = nil
      if url_path =~ %r{\A/(?:ko|en)/(?:math/)?([A-Za-z0-9_]+)(?:/|$)}
        cat_slug = Regexp.last_match(1)
      end
      cat_name = cat_slug ? maps.category_by_lang[lang][cat_slug] : nil

      # Category landing page (e.g., /ko/set_theory) — no specific post
      if target_title.nil? && cat_name && url_path.count("/") <= 2
        # Display is the category name itself
        return cat_name if !display.include?("\\[") && !display.include?("§")
        target_title = cat_name
      end

      return nil if target_title.nil?

      label_text = anchor ? maps.label_by_anchor["#{url_path}##{anchor}"] : nil

      has_cat = display.start_with?("\\[")
      has_sec = display.include?("§")
      has_lab = display.include?("⁋")

      pieces = []
      pieces << "\\[#{cat_name}\\]" if has_cat && cat_name
      if has_sec
        pieces << "§#{target_title}"
      elsif !has_cat && !has_lab
        # Plain text — use bare title
        pieces << target_title
      end
      if has_lab && label_text
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
  new_content, diffs = LinkNormalizer.normalize(doc.content, doc.relative_path)
  # Jekyll 4's Document#content= writer doesn't always replace the
  # underlying @content for posts; setting the ivar directly is the
  # reliable path. (Confirmed by post_render diagnostic 2026-05-27.)
  doc.instance_variable_set(:@content, new_content) unless diffs.empty?
  diffs.each do |d|
    LinkNormalizer.tracker_io.puts JSON.generate(d) rescue nil
  end
end

Jekyll::Hooks.register :site, :post_write do |_site|
  LinkNormalizer.tracker_io&.close
  LinkNormalizer.tracker_io = nil
end
