# frozen_string_literal: true
#
# scss_compile_cache.rb — `jekyll serve` 리빌드에서 바뀌지 않은 SCSS 는 다시 컴파일하지 않는다.
#
# Jekyll incremental 은 Sass 페이지(asset_file?)를 partial 의존성을 몰라 리빌드마다 무조건 다시
# 렌더한다. main.scss·main_dark.scss 가 각각 ~0.25s 라 watch 리빌드마다 ~0.5s 가 컴파일에
# 나갔다 (2026-10-31 측정). 그래서 converter 전체가 아니라 ::Sass.compile_string 호출 하나만
# 메모한다 — 소스맵 페이지 생성·sourceMappingURL 덧붙이기 같은 converter 의 나머지 일은
# 원래 코드가 매번 그대로 한다.
#
# 재사용 조건: (렌더된 SCSS 내용, 컴파일 옵션)이 같고, 지난 컴파일이 실제로 불러온 파일
# (CompileResult#loaded_urls) 각각의 mtime(ns)·크기·inode 와, load path 아래 디렉토리들의
# mtime 이 그대로일 것. 디렉토리 mtime 은 partial 이 새로 생기거나 지워져 @import 가 다른
# 파일로 풀리는 경우를 잡는다. 캐시는 SCSS 페이지(url)당 최신 결과 하나라 쌓이지 않는다.
#
# serve 일 때만 켠다 (Scss#convert 가 감싸는 동안만) — 일회성 build(CI)는 페이지마다 한 번
# 컴파일하니 얻을 것이 없다. 컴파일 에러는 캐시하지 않는다.
require "digest"
require "uri"

module ScssCompileCache
  CACHE = {} # sass url => { key:, result:, stamp: }

  module_function

  def file_stamp(path)
    st = File.stat(path)
    [st.mtime.to_i * 1_000_000_000 + st.mtime.nsec, st.size, st.ino]
  rescue SystemCallError
    nil
  end

  def stamp(loaded_paths, load_paths)
    dirs = Array(load_paths).flat_map { |root| Dir.glob(File.join(root, "**/")) }.sort
    [loaded_paths.map { |p| [p, file_stamp(p)] }, dirs.map { |d| [d, file_stamp(d)] }]
  end

  def local_paths(result)
    Array(result.loaded_urls).filter_map do |u|
      URI.decode_www_form_component(URI(u).path) if u.to_s.start_with?("file:")
    end.uniq
  end

  # ::Sass.compile_string 을 감싼다. Scss#convert 안에서만 메모가 켜진다.
  module CompileMemo
    def compile_string(source, **opts)
      return super unless Thread.current[:scss_compile_cache]

      key = begin
        Digest::SHA256.hexdigest(Marshal.dump([source, opts.sort_by { |k, _| k.to_s }]))
      rescue TypeError # 직렬화 못 하는 옵션(importer 등)이 끼면 메모하지 않는다
        return super
      end
      slot = opts[:url].to_s
      hit = CACHE[slot]
      if hit && hit[:key] == key && ScssCompileCache.stamp(hit[:loaded], opts[:load_paths]) == hit[:stamp]
        return hit[:result]
      end

      result = super
      loaded = ScssCompileCache.local_paths(result)
      CACHE[slot] = { key: key, result: result, loaded: loaded,
                      stamp: ScssCompileCache.stamp(loaded, opts[:load_paths]) }
      result
    end
  end

  module ConvertFlag
    def convert(content)
      return super unless @config["serving"]

      Thread.current[:scss_compile_cache] = true
      super
    ensure
      Thread.current[:scss_compile_cache] = nil
    end
  end
end

Sass.singleton_class.prepend(ScssCompileCache::CompileMemo)
Jekyll::Converters::Scss.prepend(ScssCompileCache::ConvertFlag)
