# frozen_string_literal: true

require "digest"

# 테마 시트 병합 — 라이트/다크 엔트리(assets/css/main.scss · main_dark.scss)의 컴파일 결과를
# 한 장(assets/css/theme.css)으로 합친다. 블로그 페이지는 이 한 장만 링크하고, 테마는
# <html data-theme="dark|light"> 속성으로 바꾼다 (_includes/js/theme-core.js). 시트를 갈아
# 끼우지 않으므로 전환 때 시트를 다시 붙이거나(비동기라 그 사이 무스타일 프레임이 생길 수
# 있다) 선택자를 처음부터 다시 맞출 일이 없다.
#
# 두 엔트리는 같은 SCSS 를 스킨 변수만 달리 컴파일하므로 규칙 구조가 같다. 그래서
#   - 값이 다른 선언 → var(--tv-N). 라이트 값은 :root, 다크 값은 :root[data-theme=dark]
#   - var 로 바꿀 수 없는 규칙(선언 목록·!important 가 다름, CSS 전역 키워드 값, 같은 속성이
#     한 규칙에 둘 이상 — 미지원 값 폴백 패턴) → 라이트판·다크판 두 벌을 같은 자리에 범위를
#     달아 둔다: :where(html:not([data-theme=dark])) … / :where(html[data-theme=dark]) …
#   - 한쪽에만 있는 꼬리 규칙(main_dark.scss 인라인) → 그쪽 범위만 달아 둔다
# :where() 는 명시도가 0 이라 범위를 달아도 원래 규칙의 명시도와 순서가 그대로다.
#
# 게이트 — 어기면 빌드를 멈춘다:
#   1. 파서 왕복: 다시 직렬화한 결과가 입력과 바이트 단위로 같다 (두 입력 모두)
#   2. 병합 결과를 라이트·다크로 펼치면 원래 main.css · main_dark.css 와 바이트 단위로 같다
#   3. 꼬리가 아닌 자리에서 규칙 구조(선택자·at-rule prelude)가 어긋나면 그 자리를 짚어 멈춘다
# main.css · main_dark.css 도 그대로 발행된다 — 대시보드 판본 비교기(scripts/dashboard/
# compare.html · audit-2026-08.html)가 두 장을 직접 토글한다.
module ThemeCss
  LIGHT_URL  = "/assets/css/main.css"
  DARK_URL   = "/assets/css/main_dark.css"
  OUT_DIR    = "assets/css" # 입력과 같은 디렉터리 — 값 속 상대 url() 이 똑같이 풀리도록
  OUT_NAME   = "theme.css"
  VAR        = "--tv-"
  DARK_ATTR  = "[data-theme=dark]"
  LIGHT_ATTR = ":not([data-theme=dark])"
  BOM        = "\xEF\xBB\xBF".b # 파싱은 바이트 문자열로 한다 — 구분 문자가 전부 ASCII 이고,
                                # UTF-8 문자열의 s[i] 는 매번 앞에서부터 글자를 센다
  NESTED_AT  = %w[media supports container layer document scope].freeze # 블록 안이 규칙 목록
  KEYFRAMES  = /\A@(?:-[a-z]+-)?keyframes\b/i
  CSS_WIDE   = %w[inherit initial unset revert revert-layer].freeze
  IMPORTANT  = /\s*!\s*important\s*\z/i
  SPECIAL    = /["'\/(){}\[\];]/
  SOURCEMAP  = %r{\A/\*# sourceMappingURL=}

  class Error < StandardError; end

  # 파싱 노드
  Stmt      = Struct.new(:text)              # 블록 없는 문장(@charset·@import …;)·주석·공백
  Rule      = Struct.new(:prelude, :decls)   # decls: 최상위 ';' 로 자른 원문 조각 (끝 빈 조각 = 끝 ';')
  AtBlock   = Struct.new(:prelude, :children) # 규칙 목록을 담는 at-rule (@media … · @keyframes)
  DeclBlock = Struct.new(:prelude, :body)    # 선언을 담는 at-rule (@font-face · @page …)

  # 병합 노드
  Same  = Struct.new(:node)                  # 두 쪽이 같은 노드
  VRule = Struct.new(:prelude, :items)       # items: String(공통 조각) | VDecl
  VDecl = Struct.new(:light, :dark, :merged) # 선언 조각 원문(라이트·다크)과 병합 조각
  MAt   = Struct.new(:prelude, :children)    # 규칙 목록 at-rule, 자식은 병합 노드
  Fork  = Struct.new(:light, :dark)          # 라이트판·다크판 노드 (한쪽 nil = 꼬리)
  Pair  = Struct.new(:light, :dark, :merged) # 끝의 sourceMappingURL 주석 등 (병합본엔 안 넣음)

  Ctx = Struct.new(:vars, :swapped, :forks, :tails)

  module_function

  # ---- 진입점 ----

  def merge(light_utf8, dark_utf8)
    light_css = light_utf8.b
    dark_css  = dark_utf8.b
    lbom, light = strip_bom(light_css)
    dbom, dark  = strip_bom(dark_css)
    lnodes = parse_list(light)
    dnodes = parse_list(dark)
    roundtrip!(lnodes, light, LIGHT_URL)
    roundtrip!(dnodes, dark, DARK_URL)

    ltrail = pop_trailer!(lnodes)
    dtrail = pop_trailer!(dnodes)
    ctx = Ctx.new({}, 0, 0, 0)
    merged = merge_list(lnodes, dnodes, ctx, "최상위", false)
    merged << Pair.new(ltrail, dtrail, "")

    expanded!(lbom + expand(merged, :light), light_css, LIGHT_URL)
    expanded!(dbom + expand(merged, :dark), dark_css, DARK_URL)

    lead = merged.take_while { |m| m.is_a?(Same) && m.node.is_a?(Stmt) }
    css  = (lbom.empty? && dbom.empty? ? "" : BOM) + emit(lead) + var_blocks(ctx.vars) +
           emit(merged.drop(lead.size))
    stats = "var #{ctx.vars.size}개(선언 #{ctx.swapped}곳) · 두 벌 #{ctx.forks}개 · " \
            "한쪽 전용 #{ctx.tails}개 · #{light_css.bytesize + dark_css.bytesize}B → #{css.bytesize}B"
    [css.force_encoding(Encoding::UTF_8), stats]
  end

  def cached_merge(light_css, dark_css)
    key = Digest::SHA256.hexdigest("#{light_css}\0#{dark_css}")
    return @cached[1] if @cached && @cached[0] == key

    css, stats = merge(light_css, dark_css)
    Jekyll.logger.info "ThemeCss:", stats
    @cached = [key, css]
    css
  end

  # ---- 파서 ----

  def strip_bom(s)
    s.start_with?(BOM) ? [BOM, s.byteslice(BOM.bytesize..)] : ["".b, s]
  end

  def parse_list(s)
    nodes = []
    i = 0
    n = s.length
    while i < n
      if s[i].match?(/\s/)
        j = i
        j += 1 while j < n && s[j].match?(/\s/)
        nodes << Stmt.new(s[i...j])
        i = j
        next
      end
      if s[i, 2] == "/*"
        e = s.index("*/", i + 2) or raise Error, "닫히지 않은 주석: #{s[i, 60].inspect}"
        nodes << Stmt.new(s[i...(e + 2)])
        i = e + 2
        next
      end
      j = find_stop(s, i) or raise Error, "끝나지 않은 문장: #{s[i, 80].inspect}"
      if s[j] == ";"
        nodes << Stmt.new(s[i..j])
        i = j + 1
        next
      end
      prelude = s[i...j]
      k = match_brace(s, j)
      body = s[(j + 1)...k]
      nodes << if !prelude.start_with?("@")
                 Rule.new(prelude, split_decls(body))
               elsif NESTED_AT.include?(prelude[/\A@([-\w]+)/, 1].to_s.downcase) || prelude.match?(KEYFRAMES)
                 AtBlock.new(prelude, parse_list(body))
               else
                 DeclBlock.new(prelude, body)
               end
      i = k + 1
    end
    nodes
  end

  # s[i..] 에서 괄호 밖의 첫 '{' 또는 ';' 위치. 문자열·주석은 건너뛴다.
  def find_stop(s, i)
    depth = 0
    while (j = s.index(SPECIAL, i))
      c = s[j]
      if c == '"' || c == "'"
        i = skip_string(s, j)
        next
      end
      if c == "/" && s[j + 1] == "*"
        e = s.index("*/", j + 2) or raise Error, "닫히지 않은 주석: #{s[j, 60].inspect}"
        i = e + 2
        next
      end
      case c
      when "(", "[" then depth += 1
      when ")", "]" then depth -= 1
      when "{", ";" then return j if depth.zero?
      when "}" then raise Error, "짝 없는 '}': #{s[[j - 40, 0].max, 80].inspect}" if depth.zero?
      end
      i = j + 1
    end
    nil
  end

  # s[j] == '{' 의 짝 '}' 위치. 괄호 안의 중괄호와 문자열·주석은 세지 않는다.
  def match_brace(s, j)
    i = j + 1
    braces = 1
    parens = 0
    while (k = s.index(SPECIAL, i))
      c = s[k]
      if c == '"' || c == "'"
        i = skip_string(s, k)
        next
      end
      if c == "/" && s[k + 1] == "*"
        e = s.index("*/", k + 2) or raise Error, "닫히지 않은 주석: #{s[k, 60].inspect}"
        i = e + 2
        next
      end
      case c
      when "(", "[" then parens += 1
      when ")", "]" then parens -= 1
      when "{" then braces += 1 if parens.zero?
      when "}"
        if parens.zero?
          braces -= 1
          return k if braces.zero?
        end
      end
      i = k + 1
    end
    raise Error, "닫히지 않은 블록: #{s[j, 80].inspect}"
  end

  def skip_string(s, j)
    quote = s[j]
    stop = quote == '"' ? /["\\]/ : /['\\]/
    k = j + 1
    while (m = s.index(stop, k))
      return m + 1 if s[m] == quote

      k = m + 2 # 백슬래시 이스케이프
    end
    raise Error, "닫히지 않은 문자열: #{s[j, 60].inspect}"
  end

  # 선언 블록을 최상위 ';' 로 자른다. 조각을 ';' 로 다시 이으면 원문 그대로다.
  def split_decls(body)
    pieces = []
    start = 0
    i = 0
    depth = 0
    while (j = body.index(SPECIAL, i))
      c = body[j]
      if c == '"' || c == "'"
        i = skip_string(body, j)
        next
      end
      if c == "/" && body[j + 1] == "*"
        e = body.index("*/", j + 2) or raise Error, "닫히지 않은 주석: #{body[j, 60].inspect}"
        i = e + 2
        next
      end
      case c
      when "(", "[", "{" then depth += 1
      when ")", "]", "}" then depth -= 1
      when ";"
        if depth.zero?
          pieces << body[start...j]
          start = j + 1
        end
      end
      i = j + 1
    end
    pieces << body[start..]
  end

  # 선언 조각 → [속성, 값]. 콜론이 없으면(주석·빈 조각) [nil, nil].
  def split_decl(piece)
    k = piece.index(":")
    return [nil, nil] if k.nil? || piece.lstrip.start_with?("/*")

    [piece[0...k], piece[(k + 1)..]]
  end

  def ser(node)
    case node
    when Stmt      then node.text
    when Rule      then "#{node.prelude}{#{node.decls.join(";")}}"
    when AtBlock   then "#{node.prelude}{#{node.children.map { |c| ser(c) }.join}}"
    when DeclBlock then "#{node.prelude}{#{node.body}}"
    end
  end

  def head(node)
    node.is_a?(Stmt) ? node.text : node.prelude
  end

  def roundtrip!(nodes, src, label)
    out = nodes.map { |x| ser(x) }.join
    return if out == src

    at = first_diff(out, src)
    raise Error, "#{label} 파서 왕복 실패 (#{at}자째): #{src[[at - 40, 0].max, 80].inspect}"
  end

  def expanded!(got, want, label)
    return if got == want

    at = first_diff(got, want)
    raise Error, "병합본을 펼친 결과가 #{label} 와 다르다 (#{at}자째): " \
                 "원본 #{want[[at - 40, 0].max, 80].inspect} / 펼침 #{got[[at - 40, 0].max, 80].inspect}"
  end

  def first_diff(a, b)
    i = 0
    i += 1 while i < a.length && i < b.length && a[i] == b[i]
    i
  end

  # 끝의 공백·sourceMappingURL 주석을 떼어 원문으로 돌려준다 (두 쪽 파일명이 달라서).
  def pop_trailer!(nodes)
    tail = []
    while (last = nodes.last).is_a?(Stmt) && (last.text.strip.empty? || last.text.match?(SOURCEMAP))
      tail.unshift(nodes.pop.text)
    end
    tail.join
  end

  # ---- 병합 ----

  def merge_list(ls, ds, ctx, path, keyframes)
    n = [ls.size, ds.size].min
    out = (0...n).map { |i| merge_node(ls[i], ds[i], ctx, path, keyframes) }
    rest = ls.drop(n).map { |x| Fork.new(x, nil) } + ds.drop(n).map { |x| Fork.new(nil, x) }
    raise Error, "#{path}: @keyframes 안에서 한쪽에만 있는 단계" if keyframes && !rest.empty?

    ctx.tails += rest.count { |f| !f.light.is_a?(Stmt) && !f.dark.is_a?(Stmt) }
    out + rest
  end

  def merge_node(l, d, ctx, path, keyframes)
    unless l.class == d.class && head(l) == head(d)
      raise Error, "#{path} 에서 라이트/다크 규칙 구조가 어긋난다: " \
                   "#{head(l).to_s[0, 100].inspect} ≠ #{head(d).to_s[0, 100].inspect}"
    end

    case l
    when Stmt then Same.new(l)
    when DeclBlock
      return Same.new(l) if l.body == d.body

      raise Error, "#{path} > #{l.prelude}: 선언 블록 at-rule 은 테마별로 다를 수 없다"
    when AtBlock
      MAt.new(l.prelude, merge_list(l.children, d.children, ctx, "#{path} > #{l.prelude}",
                                    keyframes || l.prelude.match?(KEYFRAMES)))
    when Rule
      return Same.new(l) if l.decls == d.decls

      items = var_items(l, d, ctx)
      return VRule.new(l.prelude, items) if items
      raise Error, "#{path} > #{l.prelude}: @keyframes 단계는 두 벌로 나눌 수 없다" if keyframes

      ctx.forks += 1
      Fork.new(l, d)
    end
  end

  # 값만 다른 선언들을 var() 로 바꾼 조각 목록. 바꿀 수 없으면 nil (→ 규칙째 두 벌).
  def var_items(l, d, ctx)
    return nil unless l.decls.size == d.decls.size

    props = l.decls.map { |p| split_decl(p)[0]&.strip&.downcase }.compact
    dups = props.tally.select { |_, c| c > 1 }.keys
    # 먼저 전부 판정하고, 하나라도 안 되면 var 를 하나도 등록하지 않고 nil
    plan = l.decls.zip(d.decls).map do |lp, dp|
      next lp if lp == dp

      lprop, lval = split_decl(lp)
      dprop, dval = split_decl(dp)
      return nil if lprop.nil? || lprop != dprop || dups.include?(lprop.strip.downcase)

      limp = lval[IMPORTANT]
      dimp = dval[IMPORTANT]
      return nil unless limp.nil? == dimp.nil?

      lv = limp ? lval[0...-limp.length] : lval
      dv = dimp ? dval[0...-dimp.length] : dval
      return nil if [lv, dv].any? { |v| v.strip.empty? || CSS_WIDE.include?(v.strip.downcase) }

      [lp, dp, lprop, limp.to_s, lv, dv]
    end
    plan.map do |it|
      next it if it.is_a?(String)

      lp, dp, lprop, imp, lv, dv = it
      name = (ctx.vars[[lv, dv]] ||= "#{VAR}#{ctx.vars.size + 1}")
      ctx.swapped += 1
      VDecl.new(lp, dp, "#{lprop}:var(#{name})#{imp}")
    end
  end

  # ---- 직렬화 ----

  def expand(nodes, side)
    nodes.map do |m|
      case m
      when Same  then ser(m.node)
      when VRule then "#{m.prelude}{#{m.items.map { |it| it.is_a?(VDecl) ? it[side] : it }.join(";")}}"
      when MAt   then "#{m.prelude}{#{expand(m.children, side)}}"
      when Fork  then (n = m[side]) ? ser(n) : ""
      when Pair  then m[side]
      end
    end.join
  end

  def emit(nodes)
    nodes.map do |m|
      case m
      when Same  then ser(m.node)
      when VRule then "#{m.prelude}{#{m.items.map { |it| it.is_a?(VDecl) ? it.merged : it }.join(";")}}"
      when MAt   then "#{m.prelude}{#{emit(m.children)}}"
      when Fork  then [[m.light, LIGHT_ATTR], [m.dark, DARK_ATTR]].map { |n, a| n ? scoped(n, a) : "" }.join
      when Pair  then m.merged
      end
    end.join
  end

  def var_blocks(vars)
    return "" if vars.empty?

    light = vars.map { |(lv, _), name| "#{name}:#{lv}" }.join(";")
    dark  = vars.map { |(_, dv), name| "#{name}:#{dv}" }.join(";")
    ":root{#{light}}:root#{DARK_ATTR}{#{dark}}"
  end

  def scoped(node, attr)
    case node
    when Rule then "#{scope_selectors(node.prelude, attr)}{#{node.decls.join(";")}}"
    when Stmt then node.text.strip.empty? || node.text.start_with?("/*") ? node.text : raise(Error, "테마 범위로 감쌀 수 없는 문장: #{node.text[0, 80].inspect}")
    when AtBlock
      raise Error, "@keyframes 는 테마 범위로 감쌀 수 없다: #{node.prelude}" if node.prelude.match?(KEYFRAMES)

      "#{node.prelude}{#{node.children.map { |c| scoped(c, attr) }.join}}"
    else raise Error, "테마 범위로 감쌀 수 없는 블록: #{head(node)[0, 80].inspect}"
    end
  end

  # 선택자 목록의 각 선택자에 테마 조건을 단다. html·:root 로 시작하면 그 자리에 붙인다
  # (html 은 html 의 자손이 아니므로 앞에 조상 조건을 달 수 없다).
  def scope_selectors(list, attr)
    split_top(list, ",").map do |sel|
      lead = sel[/\A\s*/]
      body = sel[lead.length..]
      if (m = body.match(/\A(?:html|:root)(?![-\w])/i))
        "#{lead}#{m[0]}:where(#{attr})#{body[m[0].length..]}"
      else
        "#{lead}:where(html#{attr}) #{body}"
      end
    end.join(",")
  end

  def split_top(s, sep)
    out = []
    start = 0
    i = 0
    depth = 0
    while (j = s.index(/["'()\[\]#{Regexp.escape(sep)}]/, i))
      c = s[j]
      if c == '"' || c == "'"
        i = skip_string(s, j)
        next
      end
      case c
      when "(", "[" then depth += 1
      when ")", "]" then depth -= 1
      when sep
        if depth.zero?
          out << s[start...j]
          start = j + 1
        end
      end
      i = j + 1
    end
    out << s[start..]
  end

  # ---- Jekyll 배선 ----

  class Generator < Jekyll::Generator
    safe true
    priority :lowest

    def generate(site)
      return unless site.config["dark_theme"]

      page = Jekyll::PageWithoutAFile.new(site, site.source, OUT_DIR, OUT_NAME)
      page.data.merge!("layout" => "none", "sitemap" => false, "search" => false, "regenerate" => true)
      page.content = ""
      site.pages << page
    end
  end
end

Jekyll::Hooks.register :site, :post_render do |site|
  next unless site.config["dark_theme"]

  pages = site.pages.to_h { |p| [p.url, p] }
  out   = pages["/#{ThemeCss::OUT_DIR}/#{ThemeCss::OUT_NAME}"]
  light = pages[ThemeCss::LIGHT_URL]
  dark  = pages[ThemeCss::DARK_URL]
  unless out && light&.output && dark&.output
    raise ThemeCss::Error, "theme.css 를 만들 입력이 없다 (#{ThemeCss::LIGHT_URL}·#{ThemeCss::DARK_URL} 렌더 결과)"
  end

  out.output = ThemeCss.cached_merge(light.output, dark.output)
end
