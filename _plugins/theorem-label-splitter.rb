# frozen_string_literal: true
#
# theorem-label-splitter.rb — 정리 박스 라벨을 두 조각으로 쪼갠다(인라인).
#
#   <div class="definition">
#     <p><ins id="def1"><strong>정의 1 (고윳값)</strong></ins> 본문…</p>   (렌더 결과)
#                              ↓ split (in place, <p> 안에 그대로)
#   <div class="definition">
#     <p><span class="thm-n" id="def1">정의 1</span> <em class="thm-name">(고윳값)</em> 본문…</p>
#
# 쪼개는 이유: "종류+번호(정의 1)"는 볼드, "괄호 설명(고윳값)"은 이탤릭으로 따로
# 스타일링하기 위함이다. 원본은 둘이 한 <strong> 안에 뭉쳐 있어 CSS 만으로는 못 가른다.
# 헤어라인 디자인이라 라벨은 본문 첫머리에 인라인으로 흐른다(grid 아님).
#
# 설계 노트
# - 앵커 id 는 <ins> → <span class="thm-n"> 로 그대로 옮겨 보존한다(교차참조 #def1 유지).
# - 정규식만 쓴다(nokogiri 불필요). link_normalizer.rb 와 같은 계열이며, 그쪽은
#   :pre_render 에서 마크다운의 같은 <ins id> 패턴을 읽어 교차참조 표시명을 만든다.
#   이 훅은 그 뒤(:post_render)에 렌더된 HTML 을 만지므로 서로 간섭이 없다.
# - 대상: .definition / .proposition / .example / .remark / .misc.
#   .proof / .details 는 <details><summary> 라 별도다(라벨이 <ins> 가 아님).

module TheoremLabelSplitter
  # 박스 시작부:  <div class="X"> <p><ins id="…"><strong>라벨</strong></ins> …
  #   $1 = 여는 div,  $2 = 앵커 id,  $3 = 라벨 내부 HTML("정의 1" 또는 "예시 5 (이름)")
  BOX_START = %r{
    (<div\ class="(?:definition|proposition|example|remark|misc)">)
    \s*<p><ins\ id="([^"]+)"><strong>(.*?)</strong></ins>\s*
  }x

  # 라벨에서 "종류+번호" 와 "(서술명)" 을 가른다. 이름이 없으면 매치 실패 → name=nil.
  NAME_SPLIT = %r{\A(.+?)\s*(\(.*\))\s*\z}

  module_function

  def split(html)
    html.gsub(BOX_START) do
      div   = Regexp.last_match(1)
      id    = Regexp.last_match(2)
      label = Regexp.last_match(3)

      if (m = label.match(NAME_SPLIT))
        kindnum = m[1].strip
        name    = m[2].strip
      else
        kindnum = label.strip
        name    = nil
      end

      name_part = name ? %( <em class="thm-name">#{name}</em>) : ""
      # 라벨+설명을 .thm-head 한 블록으로 묶어 한 줄에 두고, 본문은 그 아래 줄로 흐른다.
      %(#{div}<p><span class="thm-head"><span class="thm-n" id="#{id}">#{kindnum}</span>#{name_part}</span> )
    end
  end
end

# 렌더된 문서 HTML(:post_render)에 적용. ko/en 문서만, env 무관(로컬 미리보기 포함).
Jekyll::Hooks.register :documents, :post_render do |doc|
  next unless doc.url =~ %r{\A/(?:ko|en)/}
  out = doc.output
  next unless out.is_a?(String) && out.include?('class="')
  doc.output = TheoremLabelSplitter.split(out)
rescue => e
  Jekyll.logger.warn "theorem-splitter:", "#{doc.url}: #{e.message}"
end
