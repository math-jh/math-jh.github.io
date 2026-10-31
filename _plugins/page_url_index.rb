# frozen_string_literal: true
#
# page_url_index.rb — seo.html 이 다른 언어판(hreflang) 짝을 찾을 때 쓰는 URL 집합.
#
# seo.html 은 렌더되는 페이지마다 site.posts(830편)와 site.pages 를 Liquid 로 끝까지 훑어
# 짝 URL 을 가진 글·페이지가 있는지 찾았다 — 페이지당 ~13ms, watch 리빌드마다 ~0.85s
# (2026-10-31 측정; 과목홈처럼 짝이 글이 아닌 페이지는 매번 전부 훑는다). 템플릿이 쓰는 것은
# "그 URL 이 있는가" 뿐이라 렌더 직전에 한 번 집합을 만들어 site.data.page_urls 로 넘긴다.
# site.data 는 빌드마다 새로 읽히니 이 집합도 빌드마다 새로 만들어진다.
Jekyll::Hooks.register :site, :pre_render do |site|
  urls = {}
  site.posts.docs.each { |doc| urls[doc.url] = true }
  site.pages.each { |page| urls[page.url] = true }
  site.data["page_urls"] = urls
end
