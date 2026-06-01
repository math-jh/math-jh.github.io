# frozen_string_literal: true
#
# Make git commit time the authoritative `last_modified_at`, overriding any
# (now-legacy, possibly stale) value still sitting in post frontmatter.
#
# Why a custom hook instead of just deleting the frontmatter field?
#   The jekyll-last-modified-at gem seeds `last_modified_at` at :post_init, but
#   Jekyll parses/merges frontmatter *after* init, so a frontmatter
#   `last_modified_at` silently wins — which is why hand-maintained values go
#   stale. We re-seed after the whole site is read (and frontmatter merged) so
#   the git-derived value always wins.
#
#   We deliberately do NOT bulk-strip the frontmatter lines: a single commit
#   removing the field touches every file, so `git log -n1 -- <file>` would
#   then return that strip commit for all of them and every post's
#   last_modified_at would collapse to the strip time. Leaving the (now inert)
#   frontmatter lines in place keeps each file's true last-commit date intact.
#
# Runs at :site/:post_read (once, after all docs/pages are read but before any
# rendering) so aggregation pages (e.g. recent) also observe corrected values.
# A process-level cache means each file's git date is computed at most once per
# build, so `jekyll serve --incremental` rebuilds stay cheap.
#
# Requires full git history at build time (CI: actions/checkout fetch-depth: 0).
# Without it the gem falls back to file mtime and all dates become checkout time.
module Jekyll
  module LastModifiedAt
    GIT_TIME_CACHE = {} # path => Time, memoized for the lifetime of the process

    Jekyll::Hooks.register(:site, :post_read) do |site|
      format = site.config.dig("last-modified-at", "date-format")
      items = []
      site.collections.each_value { |coll| items.concat(coll.docs) }
      items.concat(site.pages)
      items.each do |item|
        next unless item.respond_to?(:data) && item.respond_to?(:path) && item.path

        item.data["last_modified_at"] =
          GIT_TIME_CACHE[item.path] ||=
            Determinator.new(site.source, item.path, format).to_liquid
      end
    end
  end
end
