# frozen_string_literal: true
#
# Break opportunities inside inline code.
#
# 인라인 코드에 든 파일 경로는 공백이 없어 브라우저에 낱말 하나다. 한 줄에 들어가는
# 길이면 통째로 다음 줄로 밀려나므로 앞줄 끝에 큰 공백이 남고, 경로를 여럿 나열한
# 문단은 항목마다 줄이 바뀐다. 구분자 뒤에 <wbr> 를 넣어 그 자리에서만 줄이 바뀌게
# 한다 — overflow-wrap 처럼 낱말 한가운데를 끊지 않으므로 읽는 사람이 없는 경계를
# 보지 않고, <wbr> 는 복사할 때 문자가 끼지 않아 경로를 그대로 복사할 수 있다.
#
# 규칙:
#   - <pre> 안(코드블럭)은 건드리지 않는다. 거기는 폭이 넘치면 가로 스크롤이 답이다.
#   - 구분자는 / . - 세 개다. 밑줄 뒤에서는 끊지 않고 밑줄 앞으로 넘긴다
#     (`skins/_custom` 은 `skins/` 에서 끊어 `_custom` 을 다음 줄로 보낸다) — 줄 끝에
#     남은 밑줄은 다음 줄과의 경계가 안 보인다.
#   - 구분자 앞에 최소 두 글자가 있어야 넣는다. 맨 앞 `_includes` 의 밑줄처럼 짧은
#     조각이 줄 끝에 홀로 남는 것을 막는다.
#   - 연속된 구분자(`/.../`)는 뒤에 한 번만 넣는다.
#   - <code> 안의 태그와 문자 엔티티는 건너뛰고 텍스트에만 넣는다.
#   - 짧은 코드(MIN_LENGTH 미만)는 애초에 줄을 밀어내지 않으므로 그냥 둔다.
#
# Runs at :post_render on the final HTML.
module InlineCodeWbr
  MIN_LENGTH = 16

  PRE_BLOCK = %r{<pre\b.*?</pre>}m
  CODE_SPAN = %r{(<code\b[^>]*>)(.*?)(</code>)}m
  MARKUP    = %r{(?:<[^>]*>|&[^;\s]{1,10};)}
  SEPARATOR = %r{(?<=\w\w)([/.\-]+)(_*)(?=\w)}

  def self.process(html)
    split_keeping(html, PRE_BLOCK).map do |chunk|
      chunk.start_with?('<pre') ? chunk : process_code_spans(chunk)
    end.join
  end

  def self.process_code_spans(chunk)
    chunk.gsub(CODE_SPAN) do
      open_tag, inner, close_tag = Regexp.last_match(1), Regexp.last_match(2), Regexp.last_match(3)
      next "#{open_tag}#{inner}#{close_tag}" if inner.length < MIN_LENGTH

      injected = split_keeping(inner, MARKUP).map do |part|
        next part if part.start_with?('<', '&')

        part.gsub(SEPARATOR) { "#{Regexp.last_match(1)}<wbr>#{Regexp.last_match(2)}" }
      end.join
      "#{open_tag}#{injected}#{close_tag}"
    end
  end

  # String#split with a capturing group keeps the delimiters, so the segments can
  # be rebuilt in order with only the non-delimiter ones rewritten.
  def self.split_keeping(str, pattern)
    str.split(/(#{pattern})/m).reject(&:empty?)
  end
end

Jekyll::Hooks.register([:documents, :pages], :post_render) do |doc|
  output = doc.output
  next unless output&.include?('<code')
  next unless (doc.output_ext || '.html') == '.html' # leave feed.xml etc. alone
  doc.output = InlineCodeWbr.process(output)
end
