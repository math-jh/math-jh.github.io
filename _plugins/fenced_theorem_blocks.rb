# frozen_string_literal: true
#
# fenced_theorem_blocks.rb — pandoc 스타일 fenced-div 정리 박스 전처리기.
#
# 소스 마크다운의 `:::` 블록을 현행 코퍼스의 Style A HTML 패턴으로 **바이트 동일**하게
# 치환한다. 출력이 기존 손수-작성 HTML과 동일하므로 이후 파이프라인(kramdown,
# theorem-label-splitter.rb, CSS, Xref_preview.js, hover 카드)은 전부 무변경이다.
#
# ── 지원 문법 ──────────────────────────────────────────────────────────────
#
#   유도형(라벨에서 class·id 접두사·번호를 전부 유도):
#     ::: 정리 2 (Thom isomorphism)          ::: Theorem 2 (Thom isomorphism)
#     본문…                                   body…
#     :::                                     :::
#       →  <div class="proposition" markdown="1">
#
#          <ins id="thm2">**정리 2 (Thom isomorphism)**</ins> 본문…
#
#          </div>
#
#   유도형(이름 없음):  ::: 정의 1  →  <ins id="def1">**정의 1**</ins> …
#
#   명시형(비유도 라벨·커스텀 id 전용, 전 class, {#id} 필수):
#     ::: misc 주장 4 (Mirror theorem, $$D$$-module form) {#conj4}
#       →  <div class="misc" markdown="1">
#          <ins id="conj4">**주장 4 (Mirror theorem, $$D$$-module form)**</ins> …
#          </div>
#     ::: proposition 명제 5 {#prop-def3}
#       →  <div class="proposition" markdown="1">
#          <ins id="prop-def3">**명제 5**</ins> …
#          </div>
#     class ∈ definition/proposition/example/remark/misc. 유도 가능한 라벨은 유도형이
#     정본이고, 명시형은 라벨·anchor 를 verbatim 으로 받는다(라벨→id 유도 없음).
#
#   부착형 증명(제목 자동):
#     ::: 증명        →  <details class="proof" markdown="1">
#     본문…              <summary>증명</summary>
#     :::
#                        본문…
#
#                        </details>
#     (영어: ::: Proof  →  <summary>Proof</summary>)
#
#   단독형 증명(summary 자동 생성):
#     ::: 증명 (정리 4)   →  <summary>정리 4의 증명</summary>   (class="proof--alone")
#     ::: Proof (Theorem 4) →  <summary>Proof of Theorem 4</summary>
#
# ── 설계 노트 ──────────────────────────────────────────────────────────────
# - **라인 스캔 파서** (정규식 일괄치환 아님). ``` / ~~~ 코드펜스와 {% raw %} 구간
#   안의 `:::` 는 절대 건드리지 않는다(fence-aware). Liquid fence-blind 사고 방지.
# - `:site, :pre_render` 에 **priority 30(HIGH)** 로 등록 → link_normalizer.rb 의
#   Maps.new(:site,:pre_render, priority 20)·문서 훅(:documents,:pre_render, priority 20)
#   **보다 먼저** 돈다. 따라서 link_normalizer 는 변환이 끝난 `<ins id>` 를 읽어
#   교차참조 표시명을 정상적으로 만든다(코드 무변경).
# - 프로덕션 게이트 없음: 로컬 serve 를 포함한 모든 env 에서 돌아야 소스의 `:::` 가
#   렌더된다.

module FencedTheoremBlocks
  # 라벨 종류(첫 토큰) → [div class, id 접두사]. 한글·영어 매핑표.
  KIND_MAP = {
    "정의"     => %w[definition def],
    "명제"     => %w[proposition prop],
    "정리"     => %w[proposition thm],
    "보조정리" => %w[proposition lem],
    "따름정리" => %w[proposition cor],
    "예시"     => %w[example ex],
    "참고"     => %w[remark rmk],
    "Definition"  => %w[definition def],
    "Proposition" => %w[proposition prop],
    "Theorem"     => %w[proposition thm],
    "Lemma"       => %w[proposition lem],
    "Corollary"   => %w[proposition cor],
    "Example"     => %w[example ex],
    "Remark"      => %w[remark rmk],
  }.freeze

  # 유도형 라벨 매칭용 종류 alternation (긴 것 우선 — 방어적, \A 앵커라 사실상 무관).
  KIND_ALT = KIND_MAP.keys.sort_by { |k| -k.length }.map { |k| Regexp.escape(k) }.join("|")
  DERIVED_RE = /\A(#{KIND_ALT})[ \t]+(\d+)/

  # 명시형(비유도 라벨·커스텀 id 전용, 전 class):  <class> <라벨 verbatim> {#id}
  # class 는 소문자 div class 이므로 유도형 종류 키워드(정의/…/Definition/…)와 겹치지 않는다.
  EXPLICIT_CLASSES = %w[definition proposition example remark misc].freeze
  # 접기 박스(<details>). 라벨 번호가 없어 KIND_MAP 에는 없지만, 박스 어휘를 쓰는
  # 소비처(Xref_preview.js 의 셀렉터, _notices.scss)는 이것도 알아야 한다.
  COLLAPSIBLE_CLASSES = %w[proof proof--alone details].freeze
  EXPLICIT_ALT     = EXPLICIT_CLASSES.map { |c| Regexp.escape(c) }.join("|")
  EXPLICIT_RE      = /\A(#{EXPLICIT_ALT})[ \t]+(.+?)[ \t]*\{#([^}]+)\}[ \t]*\z/

  # 여는 펜스(라벨 있음) / 닫는 펜스(bare ':::').
  OPEN_RE  = /\A:::[ \t]+(.+?)[ \t]*\z/
  CLOSE_RE = /\A:::[ \t]*\z/

  # 코드펜스(``` / ~~~), 최대 3칸 들여쓰기 허용(CommonMark).
  FENCE_OPEN_RE  = /\A {0,3}(`{3,}|~{3,})/
  # 닫는 코드펜스: 펜스 문자만(+공백), info string 없음.
  FENCE_CLOSE_RE = /\A {0,3}(`{3,}|~{3,})[ \t]*\z/

  # Liquid raw 토글(자체 줄).
  RAW_OPEN_RE  = /\A\s*\{%\s*raw\s*%\}\s*\z/
  RAW_CLOSE_RE = /\A\s*\{%\s*endraw\s*%\}\s*\z/

  module_function

  # content(마크다운 본문) 전체를 변환해 반환. 변경이 없으면 원본 객체를 그대로 돌려준다.
  def convert(content)
    return content unless content.include?(":::")

    lines = content.split("\n", -1)
    out = []
    block = nil # nil 또는 { kind:, raw:, ...meta, body: [] }

    in_fence = false
    fence_char = nil
    fence_len = 0
    in_raw = false

    changed = false

    emit = lambda do |line|
      if block
        block[:body] << line
      else
        out << line
      end
    end

    lines.each do |line|
      # ── raw 구간 ──
      if in_raw
        emit.call(line)
        in_raw = false if line =~ RAW_CLOSE_RE
        next
      end
      if !in_fence && line =~ RAW_OPEN_RE
        emit.call(line)
        in_raw = true
        next
      end

      # ── 코드펜스 구간 ──
      if in_fence
        emit.call(line)
        if (m = line.match(FENCE_CLOSE_RE)) && m[1][0] == fence_char && m[1].length >= fence_len
          in_fence = false
        end
        next
      end
      if (m = line.match(FENCE_OPEN_RE))
        fence_char = m[1][0]
        fence_len = m[1].length
        in_fence = true
        emit.call(line)
        next
      end

      # ── 일반 줄(펜스/raw 밖) ──
      if block
        if line =~ CLOSE_RE
          out.concat(render_block(block))
          block = nil
          changed = true
        else
          block[:body] << line
        end
        next
      end

      if (m = line.match(OPEN_RE))
        header = parse_header(m[1], line)
        if header
          block = header.merge(body: [])
        else
          # 인식 불가 → 변환하지 않고 원본 줄 유지(마이그레이션 오류를 소스에 노출).
          warn_unrecognized(m[1])
          out << line
        end
        next
      end

      out << line
    end

    # 미종료 블록(방어적): 원본 그대로 흘려보낸다.
    if block
      warn_unterminated(block[:raw])
      out << block[:raw]
      out.concat(block[:body])
    end

    changed ? out.join("\n") : content
  end

  # 여는 펜스 라벨 → 블록 메타(Hash) 또는 nil(인식 불가).
  def parse_header(label, raw_line)
    # 1) 명시형(전 class): <class> <라벨 verbatim> {#id}
    if (m = label.match(EXPLICIT_RE))
      return { type: :box, cls: m[1], id: m[3], label: m[2], raw: raw_line }
    end

    # 2) 증명(부착형/단독형)
    if label == "증명"
      return { type: :proof, cls: "proof", summary: "증명", raw: raw_line }
    elsif (m = label.match(/\A증명[ \t]+\((.+)\)\z/))
      return { type: :proof, cls: "proof--alone", summary: "#{m[1]}의 증명", raw: raw_line }
    elsif label == "Proof"
      return { type: :proof, cls: "proof", summary: "Proof", raw: raw_line }
    elsif (m = label.match(/\AProof[ \t]+\((.+)\)\z/))
      return { type: :proof, cls: "proof--alone", summary: "Proof of #{m[1]}", raw: raw_line }
    end

    # 3) 유도형
    if (m = label.match(DERIVED_RE))
      cls, prefix = KIND_MAP[m[1]]
      return { type: :box, cls: cls, id: "#{prefix}#{m[2]}", label: label, raw: raw_line }
    end

    nil
  end

  # 블록 메타 + 본문 → Style A HTML 줄 배열.
  def render_block(block)
    block[:type] == :proof ? render_proof(block) : render_box(block)
  end

  def render_box(block)
    body = strip_blank_edges(block[:body])
    first = body.empty? ? "" : body[0]
    lines = []
    lines << %(<div class="#{block[:cls]}" markdown="1">)
    lines << ""
    lines << %(<ins id="#{block[:id]}">**#{block[:label]}**</ins> #{first})
    body.drop(1).each { |l| lines << l }
    lines << ""
    lines << "</div>"
    lines
  end

  def render_proof(block)
    body = strip_blank_edges(block[:body])
    lines = []
    lines << %(<details class="#{block[:cls]}" markdown="1">)
    lines << %(<summary>#{block[:summary]}</summary>)
    lines << ""
    body.each { |l| lines << l }
    lines << ""
    lines << "</details>"
    lines
  end

  # 본문 앞뒤의 빈 줄을 제거(Style A 는 <ins>·<summary> 뒤에 곧바로 내용이 붙는다).
  def strip_blank_edges(body)
    b = body.dup
    b.shift while !b.empty? && b.first.strip.empty?
    b.pop while !b.empty? && b.last.strip.empty?
    b
  end

  def warn_unrecognized(label)
    return unless defined?(Jekyll)
    Jekyll.logger.warn "fenced-theorem:", "unrecognized ::: label — left verbatim: #{label.inspect}"
  end

  def warn_unterminated(raw)
    return unless defined?(Jekyll)
    Jekyll.logger.warn "fenced-theorem:", "unterminated ::: block — left verbatim: #{raw.inspect}"
  end
end

# ── Jekyll 훅 등록 ──────────────────────────────────────────────────────────
# :site, :pre_render / priority 30(HIGH). link_normalizer.rb 의 Maps.new 및
# 문서 훅(둘 다 priority 20)보다 먼저 돌아, link_normalizer 가 변환된 <ins id> 를
# 읽도록 보장한다. env 게이트 없음(로컬 미리보기 포함 전 환경 적용).
if defined?(Jekyll::Hooks)
  # 정리 박스 어휘의 단일 출처. 예전에는 같은 목록이 네 곳에 복사돼 있었고
  # (theorem-label-splitter.rb / Citation.js / Xref_preview.js / _notices.scss),
  # 실제로 어긋나 있었다 — Citation.js 정규식이 remark 를 '참고' 가 아니라 쓰이지도
  # 않는 '주의' 로 알고 있어서, 참고 라벨(글에 87개)을 클릭해도 아무것도 복사되지
  # 않았다. 여기서 site.data 로 노출하고 head.html 이 window.THEOREM_KINDS 로 실어
  # 보낸다. Ruby 쪽 소비처는 FencedTheoremBlocks 의 상수를 직접 참조한다.
  Jekyll::Hooks.register :site, :post_read do |site|
    site.data["theorem_kinds"] = {
      # 정규식 alternation 용 — 긴 것 우선(보조정리가 정리보다 먼저 매치되도록).
      "labels" => FencedTheoremBlocks::KIND_MAP.keys.sort_by { |k| -k.length },
      # 라벨을 감싸는 div class
      "boxes" => FencedTheoremBlocks::EXPLICIT_CLASSES,
      # <details> 로 나오는 접기 박스 (라벨 번호가 없다)
      "collapsibles" => FencedTheoremBlocks::COLLAPSIBLE_CLASSES,
      # 라벨 종류 → 앵커 id 접두사
      "prefixes" => FencedTheoremBlocks::KIND_MAP.transform_values(&:last)
    }
  end

  Jekyll::Hooks.register :site, :pre_render, priority: Jekyll::Hooks::PRIORITY_MAP[:high] do |site|
    site.posts.docs.each do |doc|
      next unless doc.content.is_a?(String)

      converted = FencedTheoremBlocks.convert(doc.content)
      # link_normalizer 와 동일한 신뢰 경로: Jekyll 4 의 content= writer 가 항상
      # @content 를 갈아끼우지 않으므로 ivar 직접 주입.
      doc.instance_variable_set(:@content, converted) unless converted.equal?(doc.content)
    end
  end
end
