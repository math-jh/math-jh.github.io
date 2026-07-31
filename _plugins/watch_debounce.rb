# frozen_string_literal: true
#
# watch_debounce.rb — 자동 재생성(livereload watch)에 디바운스 주입.
#
# jekyll-watch 의 build_listener 는 listen 의 wait_for_delay 를 기본값(0.1s)으로
# 두어 파일 변경마다 즉시 리빌드가 돈다. 대량 편집 버스트에선 리빌드가 연쇄돼
# 메모리 버스트(cgroup 캡 스래싱)를 만들므로, 첫 변경 후 BLOG_WATCH_DELAY 초
# (기본 30) 동안 변경을 모아 한 번만 리빌드하게 한다.
#
# serve --watch 에서만 의미가 있고 일회성 build(CI)에는 영향이 없다.

require "jekyll-watch"

module Jekyll
  module Watcher
    def build_listener(site, options)
      Listen.to(
        options["source"],
        :ignore         => listen_ignore_paths(options),
        :force_polling  => options["force_polling"],
        :wait_for_delay => Float(ENV.fetch("BLOG_WATCH_DELAY", 30)),
        &listen_handler(site)
      )
    end
  end
end
