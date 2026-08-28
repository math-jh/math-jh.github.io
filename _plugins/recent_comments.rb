# frozen_string_literal: true

require "time"

# `_data/comments/<thread>/comment-*.yml`에서 언어별 최근 댓글 5건을 파생한다.
# 외부 API·생성 파일 없이 같은 빌드 안에서 사이드바 데이터가 갱신된다.
Jekyll::Hooks.register :site, :post_read do |site|
  next unless site.config.dig("comments", "provider") == "custom"

  posts = site.posts.docs.each_with_object({}) do |post, index|
    key = post.url.sub(%r{\A/}, "").gsub("/", "__").downcase
    index[key] = post
  end
  recent = { "ko" => [], "en" => [] }

  (site.data["comments"] || {}).each do |thread, files|
    lang = thread.to_s.start_with?("en__") ? "en" : "ko"
    post = posts[thread.to_s]
    next unless post && files.respond_to?(:each_value)

    files.each_value do |comment|
      next unless comment.is_a?(Hash) && comment["id"] && comment["date"]
      next if comment["deleted"]

      begin
        timestamp = Time.parse(comment["date"].to_s)
      rescue ArgumentError
        next
      end
      recent[lang] << {
        "id" => comment["id"],
        "anchor" => "comment-#{comment["id"]}",
        "author" => comment["name"],
        "title" => post.data["title"].to_s,
        "permalink" => post.url,
        "date" => timestamp
      }
    end
  end

  recent.each_value { |comments| comments.replace(comments.sort_by { |item| item["date"] }.last(5).reverse) }
  site.data["recent_comments"] = recent
end
