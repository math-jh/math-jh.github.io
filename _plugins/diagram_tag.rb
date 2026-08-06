# 다이어그램 임베드 통일 태그.
#
#   {% diagram Math/Toric_Geometry/Toric_Varieties-1.svg width="20em" alt="..." %}
#
# SVG는 페이지에 인라인해 색이 CSS 체계(_sass/_diagram-colors.scss)를 따르게
# 하고, 색 열거가 불가능한 green-ramp 예외 4파일과 PNG는 종전과 동일한
# <img class="invert">로 렌더한다 (다크에서 invert 필터).
#
# 인라인 시 dvisvgm 글리프 id(g1-101 등)가 페이지 안에서 충돌하므로 경로
# 해시(+같은 파일 재등장 순번)로 네임스페이싱한다. 출력은 한 줄로 눌러서
# 인용 블록(>) 안의 임베드가 kramdown에서 깨지지 않게 한다.
require 'digest'

module Jekyll
  class DiagramTag < Liquid::Tag
    EXCEPTIONS = %w[
      Math/Algebraic_Topology/Homology-3.svg
      Math/Algebraic_Topology/Homology-5.svg
      Math/Algebraic_Topology/Poincare_Duality-3.svg
      Math/Algebraic_Topology/Poincare_Duality-5.svg
    ].freeze

    # 개정 중인 글은 CI에서 과거 판본으로 되돌려 빌드되고(scripts/ci/freeze_revising_posts.py),
    # 그때 내용이 달라진 자산은 frozen/<sha8>/ 아래 전용 사본으로 떠서 참조가 바뀐다.
    # 예외 목록 조회는 원래 경로 기준이어야 하므로 이 접두사를 떼고 본다.
    FROZEN_PREFIX = %r{\Afrozen/[0-9a-f]{8}/}

    def initialize(tag_name, markup, tokens)
      super
      m = markup.strip.match(/\A(\S+)\s*(.*)\z/m)
      raise Liquid::SyntaxError, "diagram: 경로가 없다: #{markup.inspect}" unless m
      @path = m[1]
      @attrs = {}
      m[2].scan(/(\w+)="([^"]*)"/) { |k, v| @attrs[k] = v }
    end

    def render(context)
      site = context.registers[:site]
      file = File.join(site.source, 'assets/images', @path)
      raise "diagram: 파일 없음 assets/images/#{@path}" unless File.file?(file)

      width = @attrs['width']
      style = width ? %( style="width:#{width}") : ''
      alt = @attrs['alt'].to_s

      if @path.end_with?('.png') || EXCEPTIONS.include?(@path.sub(FROZEN_PREFIX, ''))
        return %(<img src="/assets/images/#{@path}" alt="#{attr_escape(alt)}" class="invert align-center"#{style} />)
      end

      svg = File.read(file, encoding: 'utf-8')
                .sub(/\A<\?xml[^>]*\?>\s*/, '')
                .gsub(/<!--.*?-->/m, '')
      svg = namespace_ids(svg, id_prefix(context))
      svg = svg.sub('<svg ', %(<svg style="width:100%;height:auto" ))
      svg = svg.gsub(/\s*\n\s*/, ' ').strip
      label = alt.empty? ? '' : %( role="img" aria-label="#{attr_escape(alt)}")
      %(<figure class="diagram align-center"#{style}#{label}>#{svg}</figure>)
    end

    private

    def attr_escape(s)
      s.gsub('&', '&amp;').gsub('<', '&lt;').gsub('"', '&quot;')
    end

    # registers는 문서 렌더마다 새로 만들어지므로 순번은 페이지 단위로 결정적이다.
    def id_prefix(context)
      seen = (context.registers[:diagram_seen] ||= Hash.new(0))
      n = (seen[@path] += 1)
      "d#{Digest::MD5.hexdigest(@path)[0, 6]}#{n > 1 ? "x#{n}" : ''}-"
    end

    def namespace_ids(svg, pre)
      svg.gsub("id='", "id='#{pre}")
         .gsub("href='#", "href='##{pre}")
         .gsub('url(#', "url(##{pre}")
    end
  end
end

Liquid::Template.register_tag('diagram', Jekyll::DiagramTag)
