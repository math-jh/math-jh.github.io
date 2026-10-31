# frozen_string_literal: true
#
# filter_cache_reset.rb — `jekyll serve` 리빌드마다 site.filter_cache 를 비운다.
#
# Jekyll 4.4.1 의 Site#filter_cache 는 initialize 에서 한 번 `{}` 로 만들어지고
# reset(리빌드마다 호출)에서는 비워지지 않는다. 그런데 sort·where·group_by 등이 쓰는
# item_property 메모(filter_cache[:item_property][property][item])는 **문서 객체를 키로**
# 잡는다. 리빌드는 문서 830여 개를 새로 만들므로, 옛 문서가 키로 붙잡혀 한 번도 풀려나지
# 않는다 — 리빌드당 약 28MB 씩 쌓여, 크론이 _data 를 자주 건드리는 날 3시간 수명 안에
# cgroup 한도(1536M)를 넘겨 OOM kill 이 났다 (2026-09~10 에 82건).
#
# 2026-10-31 힙 덤프로 확인: 리빌드 4회 뒤 Document 3320개(=830×4)가 살아 있었고, 옛 문서의
# 참조 경로가 ROOT → Site → filter_cache → :item_property → 속성 → 문서 였다.
#
# 비워도 안전하다: 순수 메모라 같은 빌드 안에서 다시 채워진다. 일회성 build(CI)는 리빌드가
# 없으니 영향이 없다. Jekyll 이 reset 에서 이 캐시를 비우게 되면 이 파일은 지워도 된다.
Jekyll::Hooks.register :site, :after_reset do |site|
  site.filter_cache.clear
end
