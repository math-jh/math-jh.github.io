# frozen_string_literal: true

# 댓글을 글 HTML 밖의 조각 파일로 낸다 — 검색엔진이 댓글을 색인하지 않게 하려는 것이다.
#
#   /comments/<스레드 키>.html     그 글의 댓글 목록   (_includes/comments-thread.html)
#   /comments/recent-<ko|en>.html  사이드바 '최근 댓글' (_includes/comments-recent.html)
#
# 글 페이지(_includes/comments-providers/custom.html)와 사이드바(_includes/nav_recents.html)는
# 이 주소만 data-src 로 들고, Comments.js 가 불러와 끼운다. robots.txt 가 /comments/ 를 막으므로
# Googlebot 의 렌더러는 조각을 가져오지 않고, 렌더된 글에도 댓글이 없다. 경로는 이 파일·두
# include 의 data-src·robots.txt 네 곳이 같이 안다 — 어긋나면 댓글이 조용히 사라지거나(404)
# 다시 색인된다 (service-map contracts.comment-fragments).
#
# 레이아웃·sitemap 없이 조각 그대로 낸다. 파일이 없는 페이지라 dev 서버(--incremental)도
# 빌드마다 다시 렌더하므로, _data/comments 만 바뀌어도 조각은 새 데이터를 읽는다.
Jekyll::Hooks.register :site, :post_read do |site|
  next unless site.config.dig("comments", "provider") == "custom"

  # Worker·add_comment.rb 의 THREAD_RE 와 같다 (contracts.comments-thread-key).
  thread_re = /\A(?:ko|en)__[A-Za-z0-9_-]{1,116}\z/
  add = lambda do |name, content|
    page = Jekyll::PageWithoutAFile.new(site, site.source, "comments", name)
    page.data.merge!(
      "layout"     => nil,
      "permalink"  => "/comments/#{name}",
      "sitemap"    => false,
      "regenerate" => true
    )
    page.content = content
    site.pages << page
  end

  (site.data["comments"] || {}).each_key do |thread|
    next unless thread.to_s.match?(thread_re)

    add.call("#{thread}.html", %({% include comments-thread.html thread_key="#{thread}" %}))
  end
  %w[ko en].each do |lang|
    add.call("recent-#{lang}.html", %({% include comments-recent.html lang="#{lang}" %}))
  end
end
