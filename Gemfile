source "https://rubygems.org"

gem "jekyll", "~> 4.3"
gem "webrick", "~> 1.7"
gem "tzinfo-data", platforms: [:mingw, :mswin, :x64_mingw]
# Removed (2026-06-17 cleanup):
#  - minimal-mistakes-jekyll: theme is fully vendored (no theme:/remote_theme:),
#    and every plugin it pulled that we use is declared explicitly below.
#  - kramdown-parser-gfm: redundant — jekyll already depends on it transitively.
#  - nokogiri, faraday-retry: explicit-only, nothing depends on them (the latter
#    was only relevant to the octokit/jekyll-gist chain, removed with the theme gem).

group :jekyll_plugins do
  gem "jekyll-last-modified-at"
  gem "jekyll-feed"
  gem "jekyll-seo-tag"
  gem "jekyll-sitemap"
  gem "jekyll-paginate"
  gem "jekyll-include-cache"
end
