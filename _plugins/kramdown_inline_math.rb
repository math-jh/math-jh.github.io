# frozen_string_literal: true
#
# kramdown 이 single `$...$` 도 인라인 수식으로 인식하게 한다.
#
# kramdown 의 수식 문법은 `$$...$$` 뿐이다 (span/math.rb 의 INLINE_MATH_START).
# `$...$` 는 수식으로 안 잡히므로 그 안의 내용이 마크다운 파서에 그대로 노출되고,
# 그러면 조용히 망가진다:
#
#     $V^*$와 $a*b$        ->  $V^<em>$와 $a</em>b$
#     $a|b$                ->  <table> ...            (표로 바뀐다)
#     $\{x \mid x>0\}$     ->  ${x \mid x>0}$         (\{ 의 백슬래시가 먹힌다)
#     $f'(x)$              ->  $f’(x)$                (smart quotes)
#
# 그래서 예전에는 인라인 수식까지 전부 `$$...$$` 로 적었다. 여기서 파서를 넓혀
# `$...$` 도 `$$...$$` 와 똑같이 **verbatim** 으로 떠내면, 수식 안에서 마크다운이
# 실행되는 일 자체가 없어진다. 결과물도 동일하게 `\(...\)` 다.
#
# 규칙:
#   - `$$...$$` 는 그대로 (줄을 넘어갈 수 있다).
#   - `$...$` 는 한 줄 안에서 닫혀야 하고, 안에 `$` 가 없어야 한다.
#     ("$5 와 $10" 같은 산문이 통째로 수식이 되는 사고를 줄인다.)
#   - `\$` 는 kramdown 의 escaped_chars 파서가 먼저 먹으므로 여기 안 걸린다.
#   - 코드 스팬·코드 블록 안에서는 span 파서가 아예 안 돌므로 안전하다.
#
# display 수식은 건드리지 않는다. 문단을 통째로 차지하는 `$$...$$` 는 여전히
# block math (`\[...\]`) 로 간다 (BLOCK_MATH_START).

require "kramdown/parser/kramdown/math"

module Kramdown
  module Parser
    class Kramdown
      # kramdown 내부를 건드리는 패치다. gem 이 올라가며 수식 파서 모양이 바뀌면
      # 조용히 오작동하는 대신 빌드를 세운다.
      _p = parser(:inline_math)
      if _p.nil? || _p.start_re != /\$\$(.*?)\$\$/m || _p.span_start != '\$'
        raise "kramdown 의 inline_math 파서가 예상과 다르다 (kramdown #{::Kramdown::VERSION}). " \
              "_plugins/kramdown_inline_math.rb 를 새 버전에 맞춰 다시 확인할 것."
      end

      # define_parser 는 같은 이름의 재등록을 거부하므로, 이미 등록된 파서의
      # start_re 를 갈아끼운다. span_start('\$')·메서드 이름은 그대로 둔다.
      _p.start_re = /\$\$(.*?)\$\$|\$(?!\$)([^$\n]+?)\$(?!\$)/m

      def parse_inline_math
        start_line_number = @src.current_line_number
        @src.pos += @src.matched_size
        math = @src[1] || @src[2]
        @tree.children << Element.new(:math, math.strip, nil,
                                      category: :span, location: start_line_number)
      end
    end
  end
end

# smart_quotes 파서가 수식보다 먼저 등록돼 있는데, 그 시작 정규식이 /[^\\]?["']/ 라
# **앞 글자 하나를 얹어서** 매치한다. 그래서 `$'$` (prime 을 수식으로 쓴 "정의 6′")
# 의 `$` 자리를 smart_quotes 가 가로채 `$’$` 로 만들어 버린다. `$$'$$` 는 우연히
# 안 걸렸을 뿐이다. 수식이 먼저 보도록 순서를 바꾼다.
#
# `$` 자리에서 start_re 가 매치되는 span 파서는 smart_quotes 뿐이므로(emphasis 는 `*`,
# codespan 은 백틱, link 는 `[` … 로 시작한다), 이 재배치가 건드리는 것은 정확히
# "`$` 바로 뒤에 따옴표가 오는 경우" 하나다.
module MathJhInlineMathFirst
  def initialize(source, options)
    super
    return unless @span_parsers.include?(:inline_math) && @span_parsers.include?(:smart_quotes)

    @span_parsers.delete(:inline_math)
    @span_parsers.insert(@span_parsers.index(:smart_quotes), :inline_math)
  end
end
Kramdown::Parser::Kramdown.prepend(MathJhInlineMathFirst)
