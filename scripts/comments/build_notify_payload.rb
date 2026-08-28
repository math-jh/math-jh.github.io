#!/usr/bin/env ruby
# frozen_string_literal: true

require "date"
require "json"
require "pathname"
require "time"
require "yaml"

root = Pathname(ARGV[0] || File.expand_path("../..", __dir__))
comments_root = root.join("_data/comments")
comments = []

if comments_root.directory?
  comments_root.children.select(&:directory?).sort.each do |thread_dir|
    thread_key = thread_dir.basename.to_s
    # 허용 문자는 Worker 의 THREAD_RE 와 같아야 한다 (대소문자 보존, 하이픈 포함).
    # 키에서 되돌린 permalink 가 메일 링크가 되므로 대소문자를 접으면 404 가 된다.
    abort "invalid comment thread key: #{thread_key}" unless thread_key.match?(/\A(?:ko|en)__[A-Za-z0-9_-]{1,116}\z/) && thread_key.length <= 120

    thread_dir.glob("comment-*.{yml,yaml}").sort.each do |path|
      value = YAML.safe_load_file(path, permitted_classes: [Date, Time], aliases: false)
      abort "invalid comment YAML: #{path}" unless value.is_a?(Hash)
      next if value["deleted"]

      id = value["id"].to_s
      date = value["date"].to_s
      abort "invalid comment id: #{path}" unless id.match?(/\Ac-\d{8}-[a-f0-9]{6}\z/)
      abort "invalid comment date: #{path}" unless Time.iso8601(date)

      item = {
        id: id,
        threadKey: thread_key,
        permalink: "/#{thread_key.gsub("__", "/")}",
        date: date,
        name: value["name"].to_s,
        lang: value["lang"] == "en" ? "en" : "ko"
      }
      item[:replying_to] = value["replying_to"].to_s if value["replying_to"]
      item[:mentions] = Array(value["mentions"]).map(&:to_s).uniq.first(3) if value["mentions"]
      comments << item
    end
  end
end

comments.sort_by! { |item| [Time.iso8601(item[:date]), item[:id]] }
puts JSON.generate(comments: comments)
