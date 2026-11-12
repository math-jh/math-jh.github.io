---

title: "글의 작성일과 수정일"
excerpt: "수정일을 git 커밋 시각에서 계산하되 기계적 커밋은 건너뛰는 구조"

read_time: false

categories: [Misc / LLM Workshop]
permalink: /ko/llm_workshop/last_modified_git

sidebar:
    nav: "llm_workshop-ko"

author: Marvin

date: 2026-06-02
weight: 17
group: backend

---

관련 파일: [`_plugins/last_modified_git.rb`](https://github.com/math-jh/math-jh.github.io/blob/main/_plugins/last_modified_git.rb)
{: .notice--info}

글에는 날짜가 둘 있다. 작성일은 프론트매터의 `date`이고, 수정일은 `last_modified_at`이다. 수정일은 화면에 보이는 날짜([블로그 테마와 설정 메뉴](/ko/llm_workshop/theme_overhaul#제목-아래의-작성일수정일)) 말고도 `seo.html`의 `dateModified`·`article:modified_time`, 사이트맵의 `<lastmod>`, 최근 글 목록의 날짜 표시가 같이 읽는다.

예전에는 이 값을 글마다 프론트매터에 손으로 적었다. 번역 워커가 본문을 갈아 끼우고 일괄 작업이 수십 편을 한꺼번에 건드리는 동안, 그 줄은 누가 챙겨 올려 주지 않으면 처음 값 그대로 멈춰 있었다. 화면의 수정일이 실제와 몇 주씩 어긋났는데, 틀린 것보다 틀린 줄 모르고 믿게 된다는 쪽이 문제였다. 사용자는 이 칸을 사람이 아니라 git에 맡기기로 했다.

## 프론트매터 병합 순서와 젬의 Determinator

이러한 일을 수행하는 `jekyll-last-modified-at` 젬은 처음부터 깔려 있었다. 젬은 `:post_init` 시점에 각 문서의 `last_modified_at`에 `Determinator` 객체를 넣어 두고, 렌더할 때 그 객체가 `git log -n 1 -- <file>`을 불러 그 파일의 마지막 커밋 시각을 날짜로 낸다. 그런데 Jekyll은 그 *다음에* 프론트매터를 파싱해 병합하므로, 프론트매터에 `last_modified_at`이 적혀 있으면 그 값이 젬의 객체를 덮어쓴다. 그리고 대부분의 글에 그 줄이 있었다. 사용자는 글을 쓸 때마다 프론트매터를 일일이 복사하는 대신 VS Code 스니펫에 형식을 넣어 두고 불러 썼는데, 그 형식에 `last_modified_at`이 작성일과 같은 날로 기본으로 들어가 있었다. 그래서 글을 고친 뒤 그 줄까지 손으로 고치면 수정일이 맞고, 잊으면 작성일에 멈춘 값이 젬의 계산을 가렸다.

그렇다면 그 줄을 모두 지우고 젬이 제 일을 하게 두면 될 것 같지만, 줄을 지우는 것 자체가 수정이다. 지우는 커밋이 각 파일의 마지막 커밋이 되므로, 모든 글의 수정일이 그 커밋을 한 날로 넘어간다. 틀린 수정일을 고치려다 모든 글을 같은 틀린 날로 만드는 셈이고, 처음에는 이걸 피하는 게 우선이었다. 그래서 `_plugins/last_modified_git.rb`는 줄을 그대로 두고 병합 순서 뒤에 끼어들었다. `:site, :post_read` 훅은 모든 문서와 페이지를 읽어 프론트매터까지 병합한 직후, 렌더하기 전에 돈다. 첫 판본은 이 자리에서 모든 문서의 값을 git 커밋 시각으로 다시 넣었고, 프론트매터의 줄은 남아 있되 아무 일도 하지 않게 됐다.

## 수정일 계산에서 빠지는 커밋

그런데 이건 한 번 피하고 끝나는 일이 아니었다. 마지막 커밋 시각은 "마지막으로 무언가 바뀐 때"이지 "마지막으로 내용이 바뀐 때"가 아니다. 표기 일괄 치환, 이미지 참조의 `.png`→`.svg` 교체, 링크 표시명 보정처럼 여러 글을 한꺼번에 건드리는 작업은 전부 커밋을 남기지만 글의 내용은 그대로다. 이런 일괄 작업이 있는 한, 프론트매터 줄을 지울 때 피하려던 일이 작업마다 다시 생긴다. 실제로 [다이어그램을 SVG로 옮기는 작업](/ko/llm_workshop/diagram_svg)에서 수십 편의 이미지 참조가 한 줄씩만 바뀌었는데, autopush를 타고 커밋되자 그 글들의 수정일이 모두 작업 시각으로 튀었고 검색엔진에도 그렇게 신고됐다. 수정일을 사람에게서 git으로 옮겼더니 git의 노이즈가 그 자리에 들어온 것이다.

그래서 사용자는 수정일 계산을 바꾸기로 했다. git의 커밋 시각을 쓰되, 내용을 바꾸지 않은 커밋은 계산에서 뺀다. 뺄 커밋은 두 갈래로 정한다. 커밋 메시지에 마커가 있으면 그 커밋을 무시하고, 그 밖에 무시할 과거 커밋은 `_config.yml`의 `last-modified-at: ignore_commits`에 SHA 접두로 적는다. 마커는 `[lastmod-skip]`과 `[dev]` 둘이다. `[lastmod-skip]`은 글 본문의 기계적 손질(표기, 링크, 병기)에 붙으며, `[dev]`는 레이아웃·스타일·플러그인·스크립트 같은 블로그 개발 커밋에 붙는다. 예를 들어 위의 SVG 마이그레이션 작업은 이미지가 들어가는 모든 글을 건드리지만, 이는 개발 커밋의 일부이므로 `[dev]` 태그가 붙는다. 

```ruby
GIT_TIME_CACHE = {}                       # path => Time, memoised for the process lifetime
# ...
SKIP_MARKERS = ["[lastmod-skip]", "[dev]"].freeze
# ...
MAX_WALK = 80                             # safety cap on history depth per file

def self.skip_commit?(sha, msg, ignore_shas)
  return true if msg && SKIP_MARKERS.any? { |m| msg.include?(m) }  # mechanical / dev commits
  ignore_shas.any? { |s| !s.empty? && sha.start_with?(s) }
end

# ...

def self.commit_time(source, path, ignore_shas)
  rel = repo_relative(source, path)
  rel && git_index(source, ignore_shas)[rel]
end
```
{: data-filename="_plugins/last_modified_git.rb · 일부 생략, 주석 생략, 들여쓰기 정리"}

`skip_commit?`은 커밋 메시지에 마커 중 하나라도 들어 있거나, SHA가 무시 목록의 어느 접두로 시작하면 그 커밋을 건너뛰라고 답한다. 메시지는 제목 줄만이 아니라 본문까지 통째로(`git log`의 `%B`) 받으므로, 마커가 본문에 있어도 같은 효과다.

`commit_time`은 문서 경로를 저장소 기준 경로로 바꾼 뒤, 전체 이력을 한 번 훑어 만든 경로별 색인(`git_index`)에서 그 파일의 시각을 찾는다. 색인은 커밋을 최신부터 보면서 경로마다 `skip_commit?`이 건너뛰지 않은 첫 커밋의 시각을 잡는다. 건너뛸 커밋만 `MAX_WALK`(80)개를 만나거나 이력이 끝나면, 본 것 가운데 가장 최근 시각으로 물러선다. 색인에 없는 경로(추적되지 않는 파일, 생성 페이지)는 `nil`이다. 색인을 한 번에 만드는 방식은 [로컬 미리보기의 빌드 시간과 메모리 누수](/ko/llm_workshop/preview_rebuild)에 있다.

마커가 생기자 앞 절에서 미뤄 둔 프론트매터 줄도 치울 수 있게 됐다. 삭제 커밋에 `[lastmod-skip]`을 달면 플러그인이 그 커밋을 건너뛰고, 각 파일은 삭제 직전의 진짜 날짜를 그대로 가지게 될 것이기 때문이다. 그렇게 [한 커밋](https://github.com/math-jh/math-jh.github.io/commit/adf646306a977649ac423a128b22769676d756c3)에서 623줄이 지워졌다. 같은 커밋에서 훅도 바뀌었다. 낡은 값이 모두 사라졌으니, 이제 프론트매터에 날짜가 있으면 누군가 일부러 적은 값으로 믿어도 된다. 지금의 훅은 이렇다.

```ruby
Jekyll::Hooks.register(:site, :post_read) do |site|
  ignore = Array(site.config.dig("last-modified-at", "ignore_commits")).map(&:to_s)
  items = []
  site.collections.each_value { |coll| items.concat(coll.docs) }
  items.concat(site.pages)
  items.each do |item|
    next unless item.respond_to?(:data) && item.respond_to?(:path) && item.path

    cur = item.data["last_modified_at"]
    # (a) an author-supplied frontmatter date (anything but the gem's seed) wins
    next unless cur.nil? || cur.is_a?(Jekyll::LastModifiedAt::Determinator)

    t = GIT_TIME_CACHE[item.path] ||= commit_time(site.source, item.path, ignore)
    if t
      item.data["last_modified_at"] = t
    elsif cur && File.exist?(abs = File.expand_path(item.path.to_s, site.source))
      # ...
      item.data["last_modified_at"] = Time.at(File.mtime(abs).to_i)
    end
  end
end
```
{: data-filename="_plugins/last_modified_git.rb · 일부 생략, 들여쓰기 정리"}

훅은 먼저 `_config.yml`의 무시 목록을 읽고, 모든 컬렉션의 문서와 페이지를 한 목록으로 모아 하나씩 본다. 그 시점에 값이 비어 있거나 아직 `Determinator`이면 프론트매터에 날짜가 없다는 뜻이니 git에서 계산하고, 그 밖의 값(Date·Time·String)이면 작성자가 적은 값이니 그대로 둔다. 파일을 다시 열어 프론트매터를 확인할 필요가 없다. 그래서 프론트매터에 날짜를 적으면 그 값이 이기는데, git이 틀린 드문 경우를 위한 수동 덮어쓰기다.

`:post_read`에서 한 번에 고치므로 집계 페이지도 같은 값을 본다. 최근 글 목록, 사이트맵, 피드는 렌더 시점에 다른 글의 `last_modified_at`을 읽는데, 그때는 이미 값이 바뀌어 있다. `GIT_TIME_CACHE`는 경로별 결과를 프로세스 수명 동안 메모이즈해서 `jekyll serve --incremental`의 리빌드마다 다시 계산하지 않게 한다.

`commit_time`이 `nil`을 돌려준 파일 가운데 디스크에 있는 것(로컬 미리보기만 읽는 gitignore된 비공개 연구 글 같은 것)에는 git에 묻지 않고 파일 mtime을 바로 넣는다. 젬의 `Determinator`를 그대로 두면 렌더 때 빈 답을 얻으려고 전체 이력을 한 번 훑고(0.13초쯤) 결국 mtime으로 떨어지는데, 그 값을 미리 넣어 두는 것이다. 그래서 이름에 last-modified-at을 단 젬이 하게 된 일은 대부분 "여기엔 아무도 날짜를 적지 않았다"는 표지 노릇이다.

마커가 생기기 전의 오염은 되돌리지 못했다. 사용자가 본격적으로 이 블로그에 AI 도입을 시작하기 전에는 두 시간짜리 autopush 커밋 안에 다른 진짜 수정과 섞여 들어가 있어서, 그 커밋을 통째로 무시하면 같이 묶인 진짜 수정의 날짜까지 잃는다. 그 기간의 날짜는 그대로 남아 있고, 특정 글의 수정일이 거슬리면 프론트매터에 날짜를 적어 덮어쓴다.

## 기계적 변경과 진짜 수정을 가르는 autopush

위에서 설명했듯, 마커를 손으로 다는 대량 작업은 문제가 없다. 오염원은 autopush였다. `~/.local/bin/blog-autopush.py`는 두 시간마다 `git add -A`로 그동안 바뀐 것을 쓸어 담는데, 그 사이에 기계적 작업과 진짜 수정이 섞이면 커밋 하나에 마커를 달 수도 안 달 수도 없다. 달면 진짜 수정의 날짜가 죽고, 안 달면 기계적 변경이 날짜를 밀어 올린다. 사용자가 정한 답은 커밋을 쪼개는 것이었다.

autopush는 바뀐 파일의 diff를 haiku에게 보여 파일마다 기계적인지, 블로그 개발인지, 내용인지 판정을 받고, 판정별로 `[Auto] Mechanical … [lastmod-skip]`, `[Auto] Dev … [dev]`, `[Auto] Content …` 커밋을 따로 만든다. 워크숍 글은 판정과 상관없이 `[Auto] Workshop …` 커밋 하나로 묶인다. 판정이 실패하면(모델이 응답하지 않거나, diff가 너무 크거나, 판정이 빠진 파일이 있으면) 아무것도 커밋하지 않고 멈춘 뒤 알림을 보낸다. 변경분은 워킹트리에 남아 다음 차례를 기다린다. 확신 없이 마커를 잘못 다느니 멈추는 편이 낫다는 게 사용자의 판단이었다. 진짜 수정이 기계적 커밋에 섞이면 그 수정의 날짜가 사라지기 때문이다.
