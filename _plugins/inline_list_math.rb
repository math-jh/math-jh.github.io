# frozen_string_literal: true
#
# Inline math in single-item list entries.
#
# This blog writes ALL math as $$...$$ — single $ is unsafe because kramdown
# parses _ / * inside it as emphasis before KaTeX ever sees it. kramdown turns
# $$...$$ into DISPLAY math (\[...\]) when it is the sole content of a block, and
# into INLINE math (\(...\)) when it sits inside running text. A list item that
# contains only $$...$$ is therefore emitted as a centered display block:
#
#     1. $$(a^{-1})^{-1}=a$$   ->   <li>\[(a^{-1})^{-1}=a\]</li>   (centered)
#
# which reads wrong in a numbered/bulleted list. This hook rewrites just that
# case back to inline — <li>\[…\]</li> -> <li>\(…\)</li> — so the math sits on
# the line like the item's text. Standalone-paragraph display math (\[…\] that is
# NOT the lone child of an <li>) is untouched, so real centered equations stay.
#
# Runs at :post_render on the final HTML. The capture is safe: KaTeX \[…\] math
# never contains a literal "\]" except the closing delimiter, so the non-greedy
# group cannot overshoot, and the trailing \s*</li> guarantees the math is the
# item's only content.
module InlineListMath
  PATTERN = %r{(<li\b[^>]*>)\s*\\\[(.+?)\\\]\s*(</li>)}m

  def self.process(html)
    html.gsub(PATTERN) { "#{Regexp.last_match(1)}\\(#{Regexp.last_match(2)}\\)#{Regexp.last_match(3)}" }
  end
end

Jekyll::Hooks.register([:documents, :pages], :post_render) do |doc|
  output = doc.output
  next unless output&.include?('\[')                 # cheap skip: no display math
  next unless (doc.output_ext || '.html') == '.html' # leave feed.xml etc. alone
  doc.output = InlineListMath.process(output)
end
