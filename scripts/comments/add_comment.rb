#!/usr/bin/env ruby
# frozen_string_literal: true

# 저장소에 직접 댓글 파일을 쓴다 — Marvin(또는 운영자)이 폼을 거치지 않고 다는 경로.
#
# 폼으로 들어온 댓글은 Worker 가 PR 로 올리고 KV 에 삭제용 암호를 남긴다. 이 경로는
# 그 둘 다 없다: 파일만 만들고, KV `del:<id>` 가 없으므로 **UI 의 수정·삭제 버튼은
# 이 댓글에 대해 `comment_not_found` 를 낸다.** 지우려면 파일을 지우면 된다.
#
# 형식은 Worker 의 lib.js :: serializeComment 와 같아야 한다. 어긋나면 조용히 깨지는
# 것이 아니라 CI 의 build_notify_payload.rb 가 abort 한다 (id·date·thread 정규식).

require "date"
require "json"
require "optparse"
require "pathname"
require "securerandom"
require "time"
require "yaml"

ROOT = Pathname(File.expand_path("../..", __dir__))
COMMENTS_ROOT = ROOT.join("_data/comments")
# Worker 의 THREAD_RE·COMMENT_ID_RE 와 같은 규칙 (대소문자 보존, 하이픈 허용).
THREAD_RE = /\A(?:ko|en)__[A-Za-z0-9_-]{1,116}\z/
COMMENT_ID_RE = /\Ac-\d{8}-[a-f0-9]{6}\z/

options = {
  name: "Marvin",
  role: "bot",
  mentions: [],
  date: nil,
  edited: nil,
  dry_run: false
}

parser = OptionParser.new do |opts|
  opts.banner = "Usage: ruby scripts/comments/add_comment.rb --permalink /ko/... --message-file FILE [options]"
  opts.on("--permalink PATH", "글의 permalink (예: /ko/llm_workshop/static_comments)") { |v| options[:permalink] = v }
  opts.on("--thread KEY", "스레드 키를 직접 지정 (permalink 대신)") { |v| options[:thread] = v }
  opts.on("--message-file FILE", "본문 파일 ('-' 면 stdin)") { |v| options[:message_file] = v }
  opts.on("--name NAME", "작성자 이름 (기본 Marvin)") { |v| options[:name] = v }
  opts.on("--role ROLE", "owner|bot|없음(--role '')") { |v| options[:role] = v }
  opts.on("--reply-to ID", "이 루트 댓글의 답글로 단다") { |v| options[:reply_to] = v }
  opts.on("--mention ID", "멘션 대상 (최대 3회 반복)") { |v| options[:mentions] << v }
  opts.on("--date ISO", "작성 시각 (기본 now, UTC ISO8601)") { |v| options[:date] = v }
  opts.on("--edited ISO", "수정 시각 — 넣으면 '수정됨' 표시가 붙는다") { |v| options[:edited] = v }
  opts.on("--tombstone ID", "본문·이름을 지우고 삭제 표시만 남긴다 (답글·멘션이 걸린 댓글용)") { |v| options[:tombstone] = v }
  opts.on("--dry-run", "쓰지 않고 결과만 출력") { options[:dry_run] = true }
end
parser.parse!

abort parser.banner unless options[:message_file] || options[:tombstone]

# --- 스레드 키 -----------------------------------------------------------------
thread =
  if options[:thread]
    options[:thread]
  elsif options[:permalink]
    options[:permalink].sub(%r{\A/}, "").sub(%r{/\z}, "").gsub("/", "__")
  else
    abort "--permalink 또는 --thread 가 필요하다"
  end
abort "invalid thread key: #{thread}" unless thread.match?(THREAD_RE) && thread.length <= 120

# permalink 오타로 아무도 안 보는 스레드가 생기는 것을 막는다.
permalink = "/#{thread.gsub("__", "/")}"
unless system("grep", "-rqlF", "permalink: #{permalink}", ROOT.join("_posts").to_s, out: File::NULL)
  abort "그 permalink 를 쓰는 글이 _posts 에 없다: #{permalink}"
end

# --- 삭제 표시(tombstone) -------------------------------------------------------
# 아무도 가리키지 않는 댓글은 tombstone 이 아니라 파일 삭제(rm)가 맞다. 여기서 참조를
# 실제로 세어 그 규칙을 강제한다. 형식은 Worker 의 serializeTombstone 과 같다.
if options[:tombstone]
  dir = COMMENTS_ROOT.join(thread)
  files = dir.glob("comment-*.{yml,yaml}").sort.map { |f| [f, YAML.safe_load_file(f, permitted_classes: [Date, Time], aliases: false)] }
  target_path, target = files.find { |_f, v| v["id"].to_s == options[:tombstone] }
  abort "그런 댓글이 없다: #{options[:tombstone]}" unless target
  referrers = files.count do |_f, v|
    v["id"].to_s != options[:tombstone] &&
      (v["replying_to"].to_s == options[:tombstone] || Array(v["mentions"]).map(&:to_s).include?(options[:tombstone]))
  end
  abort "가리키는 댓글이 없다 — tombstone 대신 파일을 지워라: #{target_path}" if referrers.zero?

  lines = ["id: #{target["id"].to_json}", "date: #{target["date"].to_json}"]
  lines << "replying_to: #{target["replying_to"].to_json}" if target["replying_to"]
  lines << "mentions: #{Array(target["mentions"]).to_json}" if Array(target["mentions"]).any?
  lines << "lang: #{target["lang"].to_json}" << "deleted: true"
  yaml = "#{lines.join("\n")}\n"
  if options[:dry_run]
    puts "# #{target_path.relative_path_from(ROOT)}"
    puts yaml
  else
    target_path.write(yaml)
    puts target_path.relative_path_from(ROOT)
  end
  exit 0
end

# --- 본문 ----------------------------------------------------------------------
message = (options[:message_file] == "-" ? $stdin.read : File.read(options[:message_file]))
message = message.gsub("\r\n", "\n").strip
abort "본문이 비어 있다" if message.empty?
abort "본문이 8000자를 넘는다" if message.length > 8000
# Worker 의 stripHtml 과 같은 경계 — kramdown IAL 은 HTML 없이도 속성을 만든다.
abort "본문에 HTML 꺾쇠나 kramdown IAL 이 있다" if message.match?(/[<>]/) || message.match?(/\{::?[^}\n]*\}/)

# --- 기존 스레드 읽기 (답글·멘션 대상 검증) ------------------------------------
thread_dir = COMMENTS_ROOT.join(thread)
existing = thread_dir.directory? ? thread_dir.glob("comment-*.{yml,yaml}").sort.map { |path|
  [path, YAML.safe_load_file(path, permitted_classes: [Date, Time], aliases: false)]
} : []
by_id = existing.to_h { |_path, value| [value["id"].to_s, value] }

if options[:reply_to]
  parent = by_id[options[:reply_to]]
  abort "답글 대상이 없다: #{options[:reply_to]}" unless parent
  abort "삭제된 댓글에는 답글을 달 수 없다" if parent["deleted"]
  # 스레드는 1단계뿐이다 (_includes/comments-providers/custom.html 의 렌더 구조).
  abort "답글에는 답글을 달 수 없다 (1단계 스레드)" if parent["replying_to"]
end

abort "멘션은 3개까지다" if options[:mentions].length > 3
options[:mentions].each do |id|
  target = by_id[id]
  abort "멘션 대상이 없다: #{id}" unless target
  abort "삭제된 댓글은 멘션할 수 없다: #{id}" if target["deleted"]
end

# --- 파일 ----------------------------------------------------------------------
now = options[:date] ? Time.iso8601(options[:date]).utc : Time.now.utc
suffix = SecureRandom.hex(3)
id = "c-#{now.strftime("%Y%m%d")}-#{SecureRandom.hex(3)}"
abort "생성된 id 가 규칙에 안 맞는다: #{id}" unless id.match?(COMMENT_ID_RE)
path = thread_dir.join("comment-#{now.to_i}-#{suffix}.yml")

# 필드 순서는 Worker 의 serializeComment 와 같게 유지한다.
lines = [
  "id: #{id.to_json}",
  "name: #{options[:name].to_json}",
  "message: #{message.to_json}",
  "date: #{now.strftime("%Y-%m-%dT%H:%M:%S.%LZ").to_json}"
]
lines << "replying_to: #{options[:reply_to].to_json}" if options[:reply_to]
lines << "mentions: #{options[:mentions].to_json}" unless options[:mentions].empty?
# notify 는 넣지 않는다 — KV 에 sub:<id> 가 없어 알림 대상이 없고, 있으면 거짓 표시가 된다.
lines << "role: #{options[:role].to_json}" unless options[:role].to_s.empty?
lines << "edited: #{Time.iso8601(options[:edited]).utc.strftime("%Y-%m-%dT%H:%M:%S.%LZ").to_json}" if options[:edited]
lines << "lang: #{(thread.start_with?("en__") ? "en" : "ko").to_json}"
yaml = "#{lines.join("\n")}\n"

if options[:dry_run]
  puts "# #{path.relative_path_from(ROOT)}"
  puts yaml
else
  thread_dir.mkpath
  path.write(yaml)
  puts path.relative_path_from(ROOT)
end
