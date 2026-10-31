# frozen_string_literal: true

require "time"
require "shellwords"
require "pathname"

#
# `last_modified_at` policy (see also the "last_modified_git" LLM Workshop post).
#
#   (a) An explicit `last_modified_at` in a post's FRONTMATTER wins — a manual
#       override for the rare case where git is wrong.
#   (b) Otherwise the value is the file's most recent git commit time, EXCEPT
#       commits carrying a skip marker in their message — `[lastmod-skip]` or
#       `[dev]` — or whose SHA is listed in `_config.yml` under
#       `last-modified-at: ignore_commits`. This keeps mechanical mass-edits —
#       diagram batches, notation sweeps, link normalisation, the frontmatter-strip
#       commit itself — from bumping every post's "real" modification date.
#
#       The two markers differ in intent, not in effect here:
#         `[lastmod-skip]` — cosmetic sweep over post prose (notation, links,
#                            glosses). Nothing for a reader to re-read.
#         `[dev]`          — a blog-infrastructure change: layouts, sass, plugins,
#                            scripts, config. Also used for a deliberate repo-wide
#                            markup migration that touches post bodies mechanically
#                            (e.g. the fenced-div migration), so such a migration can
#                            be one reviewable commit without bumping 600 dates.
#       `[dev]` is additionally the queue blogdev-bot (Marvin) reads to pick what to
#       write up, so only substantive infra work should carry it — see
#       scripts/blogdev-bot/dev_queue.py.
#
# Detecting (a) without re-reading files: the jekyll-last-modified-at gem seeds a
# `Determinator` OBJECT at :post_init; YAML frontmatter (parsed afterwards) over-
# writes it with a Date/Time/String. So at :post_read, a value that is still a
# Determinator means "no frontmatter date here" and we compute from git; anything
# else is an author-supplied date and we leave it alone.
#
# Runs at :site/:post_read (after all docs/pages are read + frontmatter merged,
# before rendering) so aggregation pages (recent, sitemap, feed) see the same
# corrected values. Per-path memoised for the process lifetime, so
# `serve --incremental` stays cheap.
#
# Dates come from ONE `git log` over the whole history (git_index), not one
# `git log -- <file>` per document: each per-file call re-walks all of history,
# ~0.12s apiece on the Pi, and ~960 of them were most of every cold start
# (2026-10-31: startup build 120s → 15s, clean build ~150s → 75s; the single
# walk takes ~0.6s; checked against the per-file query it replaced: 0 mismatches
# over every tracked .md/.html, both path forms). A path the index doesn't know
# has no git date, and git is never asked about it one by one: untracked or
# gitignored files (the private research posts the local preview reads) get
# their mtime directly — the value the gem would have reached after its own
# empty `git log` — since asking cost ~1.6s per watch rebuild, twice over (our
# per-file fallback, then the gem's Determinator at render). A post first
# committed while `serve` runs gets its git date at the next restart.
#
# Requires full git history at build (CI: actions/checkout fetch-depth: 0).
module Jekyll
  module LastModifiedAt
    GIT_TIME_CACHE = {}                       # path => Time, memoised for the process lifetime
    GIT_INDEX = {}                            # [source, ignore_shas] => { repo-relative path => Time }
    GIT_PREFIX = {}                           # source => its path inside the repo ("" at the root)
    # Commits whose message carries any of these are ignored when deriving the date.
    SKIP_MARKERS = ["[lastmod-skip]", "[dev]"].freeze
    SKIP_MARKER = SKIP_MARKERS.first          # kept for anything referencing the old name
    MAX_WALK = 80                             # safety cap on history depth per file

    def self.skip_commit?(sha, msg, ignore_shas)
      return true if msg && SKIP_MARKERS.any? { |m| msg.include?(m) }  # mechanical / dev commits
      ignore_shas.any? { |s| !s.empty? && sha.start_with?(s) }
    end

    # Last real commit time for every path at once, from a single walk. Commits
    # arrive newest first (same order as `git log -- <path>`), so a path takes the
    # first non-skipped commit that touches it; after MAX_WALK skipped commits, or
    # at the end of history, it falls back to the newest one it saw.
    # --no-renames: a rename then touches both paths, as `git log -- <path>` sees it.
    def self.git_index(source, ignore_shas)
      GIT_INDEX[[source.to_s, ignore_shas]] ||= begin
        raw = IO.popen(["git", "-C", source.to_s, "log", "--no-merges", "--no-renames", "-z",
                        "--name-only", "--format=%x1e%H%x1f%cI%x1f%B"], err: File::NULL, &:read).to_s
        raw.force_encoding(Encoding::UTF_8)
        resolved = {}
        pending = {}                          # path => [newest Time, commits seen]
        raw.split("\x1e").each do |rec|
          header, files = rec.split("\x00", 2)
          next if header.nil? || files.nil?
          sha, iso, msg = header.split("\x1f", 3)
          next if sha.nil? || iso.nil?
          t = (Time.parse(iso) rescue nil)
          next if t.nil?
          skip = skip_commit?(sha, msg, ignore_shas)
          files.split("\x00").each do |f|
            f = f.delete_prefix("\n")
            next if f.empty? || resolved.key?(f)
            st = (pending[f] ||= [t, 0])
            st[1] += 1
            if !skip
              resolved[f] = t
              pending.delete(f)
            elsif st[1] >= MAX_WALK
              resolved[f] = st[0]
              pending.delete(f)
            end
          end
        end
        pending.each { |f, (newest, _)| resolved[f] = newest }
        resolved
      end
    end

    # Index key for `path` (absolute for docs, source-relative for pages), or nil
    # if it lies outside the repo.
    def self.repo_relative(source, path)
      prefix = (GIT_PREFIX[source.to_s] ||=
        `git -C #{Shellwords.escape(source)} rev-parse --show-prefix 2>/dev/null`.chomp)
      rel = Pathname(File.expand_path(path.to_s, source))
              .relative_path_from(Pathname(File.expand_path(source))).to_s
      rel.start_with?("..") ? nil : prefix + rel
    end

    # Most recent non-skipped commit time for `path`, or nil if it has no history
    # in the index (untracked, gitignored, generated, or outside the repo).
    def self.commit_time(source, path, ignore_shas)
      rel = repo_relative(source, path)
      rel && git_index(source, ignore_shas)[rel]
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

        t = GIT_TIME_CACHE[item.path] ||= commit_time(site.source, item.path, ignore)
        if t
          item.data["last_modified_at"] = t
        elsif cur && File.exist?(abs = File.expand_path(item.path.to_s, site.source))
          # No git history (untracked / gitignored, e.g. the private research posts
          # the local preview reads). Left alone, the gem's Determinator runs
          # `git log -n 1 -- <file>` at render time — a full history walk, ~0.13s,
          # for an empty answer — and then falls back to the file's mtime. Put that
          # same value here without asking git (2026-10-31: 13 such spawns, 1.6s,
          # on every watch rebuild, mostly from posts listed on /recent/).
          item.data["last_modified_at"] = Time.at(File.mtime(abs).to_i)
        end
      end
    end
  end
end
