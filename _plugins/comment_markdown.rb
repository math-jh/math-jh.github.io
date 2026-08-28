# frozen_string_literal: true

# 댓글의 `$...$`를 Markdown보다 먼저 마스킹한다. 일반 kramdown span parser는
# 본문에서는 잘 작동하지만, 댓글을 `markdownify`할 때 `$a|b$`의 pipe를 표 문법이
# 먼저 가져가 수식이 깨질 수 있다. code span/fence 안의 달러는 그대로 둔다.
require "cgi"

module CommentMarkdown
  TOKEN_PREFIX = "COMMENTMATHTOKEN".freeze

  module_function

  def mask_math(source)
    text = source.to_s
    tokens = []
    output = +""
    index = 0
    code_ticks = 0

    while index < text.length
      if text[index] == "`"
        run = text[index..].match(/\A`+/)[0].length
        if code_ticks.zero?
          code_ticks = run
        elsif run == code_ticks
          code_ticks = 0
        end
        output << "`" * run
        index += run
        next
      end

      if code_ticks.zero? && text[index] == "$" && (index.zero? || text[index - 1] != "\\")
        width = text[index, 2] == "$$" ? 2 : 1
        closing = find_closing_dollars(text, index + width, width)
        if closing
          math = text[(index + width)...closing]
          standalone = width == 2 && display_delimiters?(text, index, closing + width)
          token = "#{TOKEN_PREFIX}#{tokens.length}X"
          tokens << [math, standalone]
          output << token
          index = closing + width
          next
        end
      end

      output << text[index]
      index += 1
    end
    [output, tokens]
  end

  def find_closing_dollars(text, start, width)
    needle = "$" * width
    cursor = start
    while (found = text.index(needle, cursor))
      return nil if width == 1 && text[start...found].include?("\n")
      return found if found.zero? || text[found - 1] != "\\"

      cursor = found + width
    end
    nil
  end

  def display_delimiters?(text, opening, ending)
    before = text[0...opening].split("\n", -1).last.to_s.strip
    after = text[ending..].to_s.split("\n", 2).first.to_s.strip
    before.empty? && after.empty?
  end

  def restore_math(html, tokens)
    tokens.each_with_index.reduce(html) do |result, ((math, display), index)|
      delimiter = display ? ["\\[", "\\]"] : ["\\(", "\\)"]
      result.gsub("#{TOKEN_PREFIX}#{index}X", "#{delimiter[0]}#{CGI.escapeHTML(math.strip)}#{delimiter[1]}")
    end
  end

  def remove_kramdown_extensions(source)
    # Worker에서도 제거하지만, 수기 이전 데이터나 과거 파일도 같은 안전 경계를
    # 지나게 한다. IAL(`{: ...}`)은 HTML 없이도 onclick 같은 속성을 만들 수 있다.
    source.gsub(/\{::?[^}\n]*\}/, "")
  end

  module Filter
    def comment_markdown(input)
      masked, tokens = CommentMarkdown.mask_math(input)
      masked = CommentMarkdown.remove_kramdown_extensions(masked)
      site = @context.registers[:site]
      converter = site.find_converter_instance(Jekyll::Converters::Markdown)
      CommentMarkdown.restore_math(converter.convert(masked), tokens)
    end
  end
end

Liquid::Template.register_filter(CommentMarkdown::Filter)
