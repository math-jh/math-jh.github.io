# frozen_string_literal: true
#
# data_read_cache.rb — `jekyll serve` 리빌드에서 바뀌지 않은 _data 파일은 다시 파싱하지 않는다.
#
# DataReader 는 리빌드마다 _data 전부를 YAML 로 다시 읽는다. link_relations.yml·terms.yml
# 이 각각 ~0.5s 라 watch 리빌드마다 ~1.2s 가 여기서 나갔다 (2026-10-31 측정). 파일의
# mtime(ns)·크기·inode 가 지난번과 같으면 그때 파싱한 결과를 Marshal 사본으로 돌려준다.
# 매번 새 사본이라 빌드 중 누가 site.data 를 고쳐도 다음 빌드로 새지 않는다.
#
# serve 일 때만 켠다 — 일회성 build(CI)는 파일마다 한 번만 읽으니 얻을 것이 없다.
# 캐시는 파일 경로당 직렬화 결과 하나라 크기가 _data 크기에 묶인다 (filter_cache 처럼
# 빌드마다 새 객체를 키로 쌓지 않는다).
module Jekyll
  module DataReadCache
    CACHE = {} # path => [[mtime_ns, size, ino], Marshal bytes]

    def read_data_file(path)
      return super unless @site.config["serving"]

      st = File.stat(path)
      key = [st.mtime.to_i * 1_000_000_000 + st.mtime.nsec, st.size, st.ino]
      cached = CACHE[path]
      return Marshal.load(cached[1]) if cached && cached[0] == key

      data = super
      CACHE[path] = [key, Marshal.dump(data)]
      data
    end
  end

  DataReader.prepend(DataReadCache)
end
