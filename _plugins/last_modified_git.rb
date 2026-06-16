# frozen_string_literal: true

require "time"
require "shellwords"

#
# `last_modified_at` policy (see also the "last_modified_git" LLM Workshop post).
#
#   (a) An explicit `last_modified_at` in a post's FRONTMATTER wins — a manual
#       override for the rare case where git is wrong.
#   (b) Otherwise the value is the file's most recent git commit time, EXCEPT
#       commits whose message contains the skip marker `[lastmod-skip]`, or whose
#       SHA is listed in `_config.yml` under `last-modified-at: ignore_commits`,
#       are skipped. This keeps mechanical mass-edits — diagram batches, notation
#       sweeps, link normalisation, the frontmatter-strip commit itself — from
#       bumping every post's "real" modification date.
#
# Detecting (a) without re-reading files: the jekyll-last-modified-at gem seeds a
# `Determinator` OBJECT at :post_init; YAML frontmatter (parsed afterwards) over-
# writes it with a Date/Time/String. So at :post_read, a value that is still a
# Determinator means "no frontmatter date here" and we compute from git; anything
# else is an author-supplied date and we leave it alone.
#
# Runs at :site/:post_read (after all docs/pages are read + frontmatter merged,
# before rendering) so aggregation pages (recent, sitemap, feed) see the same
# corrected values. Per-path memoised for the build, so `serve --incremental`
# stays cheap.
#
# Requires full git history at build (CI: actions/checkout fetch-depth: 0).
module Jekyll
  module LastModifiedAt
    GIT_TIME_CACHE = {}                       # path => Time, memoised per build
    SKIP_MARKER = "[lastmod-skip]"            # commits whose message carries this are ignored
    MAX_WALK = 80                             # safety cap on history depth per file

    # Most recent commit time for `path`, skipping skip-marked / blacklisted
    # commits. Falls back to the absolute newest commit if every candidate is
    # skipped, and to nil if the file has no git history yet.
    def self.last_real_commit_time(source, path, ignore_shas)
      raw = `git -C #{Shellwords.escape(source)} log --no-merges --max-count=#{MAX_WALK} -z \
             --format=#{Shellwords.escape('%H%x1f%cI%x1f%B')} -- #{Shellwords.escape(path.to_s)} 2>/dev/null`
      newest = nil
      raw.split("\x00").each do |rec|
        next if rec.empty?
        sha, iso, msg = rec.split("\x1f", 3)
        next if sha.nil? || iso.nil?
        t = (Time.parse(iso) rescue nil)
        next if t.nil?
        newest ||= t                                          # remember newest for fallback
        next if msg && msg.include?(SKIP_MARKER)              # skip mechanical commits
        next if ignore_shas.any? { |s| !s.empty? && sha.start_with?(s) }
        return t                                              # newest non-skipped commit
      end
      newest
    end

    Jekyll::Hooks.register(:site, :post_read) do |site|
      ignore = Array(site.config.dig("last-modified-at", "ignore_commits")).map(&:to_s)
      items = []
      site.collections.each_value { |coll| items.concat(coll.docs) }
      items.concat(site.pages)
      items.each do |item|
        next unless item.respond_to?(:data) && item.respond_to?(:path) && item.path

        cur = item.data["last_modified_at"]
        # (a) an author-supplied frontmatter date (anything but the gem's seed) wins
        next unless cur.nil? || cur.is_a?(Jekyll::LastModifiedAt::Determinator)

        t = GIT_TIME_CACHE[item.path] ||= last_real_commit_time(site.source, item.path, ignore)
        item.data["last_modified_at"] = t if t
      end
    end
  end
end
