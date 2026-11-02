---

title: "미리보기 리빌드, 12초에서 2초로"
excerpt: "재기동 2분, 글 한 줄에 리빌드 12초, 두 달 새 OOM 82번. 글마다 돌던 git log, 리빌드마다 남던 문서 830개, 매번 다시 그리던 목록 페이지 65개를 걷어낸 일"

read_time: false

categories: [Misc / LLM Workshop]
permalink: /ko/llm_workshop/preview_rebuild

sidebar:
    nav: "llm_workshop-ko"

author: Marvin

date: 2026-10-31
last_modified_at: 2026-11-02
weight: 62

---

관련 파일: [`_plugins/last_modified_git.rb`](https://github.com/math-jh/math-jh.github.io/blob/main/_plugins/last_modified_git.rb), [`_plugins/filter_cache_reset.rb`](https://github.com/math-jh/math-jh.github.io/blob/main/_plugins/filter_cache_reset.rb), [`_plugins/graph_data.rb`](https://github.com/math-jh/math-jh.github.io/blob/main/_plugins/graph_data.rb), [`_plugins/data_read_cache.rb`](https://github.com/math-jh/math-jh.github.io/blob/main/_plugins/data_read_cache.rb), [`_plugins/scss_compile_cache.rb`](https://github.com/math-jh/math-jh.github.io/blob/main/_plugins/scss_compile_cache.rb), [`_plugins/page_url_index.rb`](https://github.com/math-jh/math-jh.github.io/blob/main/_plugins/page_url_index.rb), [`_plugins/listing_regen_gate.rb`](https://github.com/math-jh/math-jh.github.io/blob/main/_plugins/listing_regen_gate.rb)
{: .notice--info}

이 블로그의 로컬 미리보기는 Pi에서 도는 `jekyll serve --incremental`이다. 글을 고치면 몇 초 안에 브라우저가 새로고침되어야 하는데, 실제로는 글 한 줄을 고쳐도 리빌드가 12초, 서버가 다시 뜨는 데 2분이 걸렸다. 9월 초부터 두 달 동안 메모리 한도에 걸려 강제 종료된 것도 82번이다. 사용자의 첫 질문은 하드웨어 쪽을 향해 있었다.

> 그리고 지킬 재빌드가 항상 너무 오래 걸리거든, 이것도 방법 없지? 예를 들어 full rebuild시에만 맥 미니에서 돌려준다던가...

맥에 넘기는 방법을 따지기 전에, Pi가 그 2분 동안 무엇을 하는지부터 쟀다. 대부분은 Ruby가 아니라 git이었다.

## 글마다 다시 훑던 git 이력

수정일은 `_plugins/last_modified_git.rb`가 git에서 받아 온다 ([last_modified_at을 git에 맡기기](/ko/llm_workshop/last_modified_git)). 이 플러그인은 문서마다 `git log --no-merges --max-count=80 -- <파일>`을 따로 실행했고, 경로를 지정한 `git log`는 커밋 5,700개짜리 이력을 매번 처음부터 훑는다. Pi에서 한 번에 124ms, 대상이 959개라 서버를 띄울 때마다 119초가 여기서 나갔다.

고치기 전에 사용자가 순서를 하나 정했다.

> 응 그래 그렇게 해 줘. 그거 수정 하기 전에, 그 글이 왜 있는지 봐 주고 해줘.

그래서 그 글부터 읽고, 거기서 정한 규칙(frontmatter 날짜 우선, 마커 커밋 건너뛰기, 80개 상한)은 그대로 둔 채 조회 방식만 바꿨다. 지금은 `git log --name-only` 한 번(0.6초)으로 모든 경로의 날짜를 색인하고, 959개 경로에서 예전 방식과의 불일치는 0건이다. 시작 빌드는 120초에서 15초로, clean build는 150초에서 75초로 줄었다 ([29e07892](https://github.com/math-jh/math-jh.github.io/commit/29e07892)). 맥 미니로 넘길 이유는 이것으로 대부분 사라졌다.

## 리빌드마다 남는 문서 830개

다음은 OOM이다.

> 또 Jekyll OOM은 자주 떠. (Pi 재시작해서 로그가 안 남은 거야) 이 부분도 하드웨어 말고 처리할 방법 있는지 봐줘.

방어층은 이미 있었다. jemalloc, cgroup `MemoryMax=1536M`, 3시간마다의 정기 재시작, 파일 변경을 30초씩 모아 리빌드하는 디바운스였다. 그래도 넘쳤다. 글 하나를 `touch`만 해서 리빌드를 네 번 일으키자 힙이 매번 26~31MB씩 늘었다. 내용은 그대로였으니 변환 결과 캐시 탓은 아니었다.

사용자는 우회하지 말고 새는 곳 자체를 찾자는 쪽을 골랐다. 운영 중인 서버는 두고, 저장소 복사본을 별도 Ruby 프로세스에서 `site.process`로 되풀이하며 살아 있는 객체를 클래스별로 셌다. 리빌드마다 `Jekyll::Document`, `DocumentDrop`, `UrlDrop`이 정확히 830개씩 늘었다. 830은 글의 수다. 힙 덤프(`ObjectSpace.dump_all`, 167MB)에서 옛 문서 하나의 참조를 거꾸로 따라가자 `ROOT → Binding → Jekyll::Site → Hash(3) → Hash(6) → Hash(3320) → 문서`가 나왔다. 리빌드 네 번이면 830 × 4 = 3,320이다.

그 해시는 `Site#filter_cache`다. Jekyll 4.4.1은 이것을 `Site#initialize`에서 한 번 만들고, 리빌드마다 부르는 `reset`에서는 비우지 않는다. 그 안의 `item_property` 메모(`sort`·`where`·`find` 필터가 쓴다)는 문서 객체를 키로 잡는다.

```ruby
@item_property_cache ||= @context.registers[:site].filter_cache[:item_property] ||= {}
@item_property_cache[property] ||= {}
@item_property_cache[property][item] ||= begin
```
{: data-filename="vendor/.../jekyll-4.4.1/lib/jekyll/filters.rb"}

리빌드는 문서를 새로 만들고, 문서의 해시 비교는 객체 자신이다. 그래서 옛 키는 다시 맞는 일도 지워지는 일도 없다. 830개의 지난 판본을 끌어안고 한도까지 가서 쓰러지는 일을 두 달 동안 82번 되풀이한 셈이다. 고치는 데는 세 줄이 들었다.

```ruby
Jekyll::Hooks.register :site, :after_reset do |site|
  site.filter_cache.clear
end
```
{: data-filename="_plugins/filter_cache_reset.rb"}

메모는 같은 빌드 안에서 다시 채워지니 잃는 것이 없다. 복사본에서 리빌드 여섯 번 동안 살아 있는 객체 수는 403,6xx에서 움직이지 않았다. 업데이트로 고쳐졌을 가능성은 사용자가 짚었지만, rubygems 최신판이 4.4.1이었고 master의 같은 코드도 그대로였다. 디바운스는 사용자 판단으로 지웠다.

> 그게 그리고 30초 디바운스가 본질적으로 그 메모리 누수 때문에 만든게 컸거든? 그래서 혹시 완전히 해결됐다면 디바운싱은 지워도 돼.

이제 리빌드는 파일이 바뀌고 0.5초 뒤에 시작한다 ([72205c23](https://github.com/math-jh/math-jh.github.io/commit/72205c23)).

## watch 리빌드 12초의 내역

남은 것은 글 한 줄에 드는 12초다. 단계·훅·문서별로 시간을 재 보니 리빌드 평균 12.13초 가운데 `graph_data`의 렌더 전 훅이 3.24초, `last_modified_git`의 훅이 1.59초, `_data` YAML 파싱이 1.19초였다. 렌더는 바뀐 글 한 편과 페이지 73개를 합쳐 4.75초였다.

`graph_data.rb`는 [글 의존성 그래프](/ko/llm_workshop/dependency_graph)의 추천 내비게이션을 계산한다. `semantic_navigation`은 글 하나를 계산할 때마다 인용 쌍 전체와 글 전체를 처음부터 다시 훑었다. 글 742편 × 4ms이니 사실상 제곱 시간이다. 지금은 색인을 모델당 한 번만 만들어 그 빌드의 모델 Hash 안에 두고, 빌드가 끝나면 모델과 같이 버린다.

```ruby
def navigation_index(model)
  model[:navigation_index] ||= begin
    pairs_by_url = Hash.new { |h, k| h[k] = [] }
    required_adjacency = Hash.new { |h, k| h[k] = [] }
    model[:cited_pairs].each do |pair, entry|
      src, tgt = pair
      pairs_by_url[src] << [pair, entry]
      pairs_by_url[tgt] << [pair, entry]
      required_adjacency[tgt] << src if entry[:relation] == "required"
    end
    # docs_by_category, reachability 메모도 같이 둔다
  end
end
```
{: data-filename="_plugins/graph_data.rb"}

목록은 원래 순회 순서(`cited_pairs`의 삽입 순서)를 지킨다. 추천 후보가 들어오는 순서가 동점 처리를 정하기 때문이다. 이전 구현과 두 언어 742편의 결과를 비교해 차이가 없었고, 3.24초가 0.31초가 됐다.

`last_modified_git`의 1.59초는 gitignore된 비공개 연구 글 20편 몫이었다. 미리보기는 이 글들을 읽지만 git에는 이력이 없어서, git에 직접 묻는 예외 경로를 리빌드마다 20번 탔다. 사용자의 판단은 간단했다.

> last_modified_git은 그... git이 추적하지 않는 글은 무시하도록 해도 좋겠네. 굳이 캐싱까지 하지 않아도.

그렇게 하자 비용이 하나 더 보였다. 값이 비어 있는 문서에는 `jekyll-last-modified-at` gem의 지연 계산 객체(`Determinator`)가 남아, 최근 글 목록이 날짜를 읽을 때 글마다 `git log -n 1`을 띄웠다(리빌드당 13번, 1.64초). gem도 결국 파일 mtime으로 떨어지므로 지금은 훅이 그 값을 바로 넣는다.

`_data`는 리빌드마다 전부 다시 파싱됐다(`terms.yml`·`link_relations.yml`이 각각 0.5초). `data_read_cache.rb`는 serve일 때만, mtime(ns)·크기·inode가 지난번과 같은 파일에 그때 파싱한 결과의 `Marshal` 사본을 돌려준다. 매번 새 사본이라 빌드 중에 누가 데이터를 고쳐도 다음 빌드로 새지 않는다. 1.19초가 0.06초가 됐고 ([19254739](https://github.com/math-jh/math-jh.github.io/commit/19254739)), 여기까지로 12.1초는 5.0초가 됐다.

## SCSS 컴파일 메모와 hreflang URL 집합

SCSS 두 벌(`main`·`main_dark`)은 Jekyll incremental이 partial 의존성을 몰라 리빌드마다 다시 컴파일된다. converter 전체를 건너뛰면 소스맵 페이지를 `site.pages`에 넣는 부수 효과까지 사라지므로 `Sass.compile_string` 호출 하나만 메모한다. 입력과 옵션이 같고, 지난 컴파일이 불러온 파일(`CompileResult#loaded_urls`)과 load path 아래 디렉토리의 mtime이 그대로일 때만 재사용한다. 디렉토리 쪽은 새 partial이 생겨 `@import`가 다른 파일로 풀리는 경우를 잡는다 ([b529f074](https://github.com/math-jh/math-jh.github.io/commit/b529f074)).

Liquid 프로파일러는 `seo.html`이 페이지당 13ms를 쓴다고 짚었다. 나는 이것도 gem의 git 호출 탓이라고 짐작했는데, git을 없앤 뒤에도 그대로였다. 원인은 hreflang(다른 언어판) 링크를 찾느라 페이지마다 `site.posts` 830편을 끝까지 돌고, 못 찾으면 `site.pages`를 또 도는 반복문이었다. 쓰는 것은 "그 URL을 가진 글이나 페이지가 있는가"뿐이라, 지금은 `page_url_index.rb`가 렌더 직전에 URL 집합을 한 번 만들어 `site.data.page_urls`로 넘기고 템플릿은 조회만 한다.

이 템플릿은 프로덕션에도 나가므로, production 설정으로 변경 전후 clean build를 해서 출력 1,517개를 비교했다. 다른 것은 `feed.xml`의 빌드 시각 한 줄이었다 ([20edd9c9](https://github.com/math-jh/math-jh.github.io/commit/20edd9c9)). 리빌드는 3.9초가 됐다.

## 목록 페이지 65개의 지문

3.9초 중 가장 큰 것은 글 한 편만 바뀌어도 다시 그려지는 페이지 65개였다. 과목홈 54개, Misc 목록, 카테고리 아카이브, 최근 글, Terms·Notations·`terms.json`은 `regenerate: true` 때문이고, `sitemap.xml`은 소스 없는 생성 페이지라서다. 이 페이지들은 글 본문을 읽지 않는다. 그래서 `listing_regen_gate.rb`는 각 묶음이 실제로 읽는 입력을 지문 하나로 묶고, 지문이 지난 빌드와 같고 출력 파일이 있으면 `Jekyll::Regenerator#regenerate?`에서 그 페이지를 건너뛴다.

지문을 처음 `Marshal`로 만들었을 때는 아무것도 건너뛰지 못했다. `Marshal`은 한 덩어리 안에서 같은 객체를 두 번 만나면 링크로 적으므로, 값이 같아도 객체가 공유되는 모양이 빌드마다 달라지면 바이트가 달라진다. 지금은 값만 정해진 형식으로 digest에 흘려 넣는 `canon`을 쓴다. 모르는 타입은 `inspect`로 적는데, 거기 객체 주소가 섞이면 지문이 매번 달라져 그냥 다시 그릴 뿐이다. 틀려도 안전한 쪽으로 틀린다.

묶음은 사용자의 판단에 따라 두 번 나뉘었다. 먼저 용어 데이터만 읽는 용어 3종이 떨어져 나갔고, 다음은 나머지 목록이었다.

> 그리고 보니까 말이야, 카테고리 아카이브, 과목홈도 사실상 새 글이 추가되거나 삭제되지 않는 한 바뀔 일 없는 것들이라 (내가 예를 들어 description 같은거 잘 안 바꿈), 이것도 지문으로 묶을 수 있나?

> 그 내가 헷갈리게 말했을 수도 있는데, 수정일도 지연 반영해도 된다. 글이 새로 추가되거나 삭제되거나 하는 경우만 즉시 반영하면 됨.

그래서 구조 묶음 62개(과목홈·Misc·카테고리 아카이브·최근 글·sitemap)의 지문은 글에서 구조를 정하는 필드만 본다. 수정일(`last_modified_at`)과 요약문(`excerpt`)은 일부러 뺐다.

```ruby
STRUCTURE_FIELDS = %w[title categories category weight date permalink header link
                      published sitemap read_time show_date words_per_minute].freeze
```
{: data-filename="_plugins/listing_regen_gate.rb"}

지문은 다른 렌더 전 훅이 끝난 뒤 계산하고, 쓰기까지 끝난 빌드에서만 확정한다. 프로세스의 첫 빌드와 실패한 빌드 다음 빌드는 비교 없이 전부 그린다. 복사본에서 열 가지 변경을 일으키며 강제로 다시 그린 결과와 바이트 단위로 비교했더니, 본문 수정과 `touch`는 0/65를 렌더하고도 같았고 제목·`_data`·템플릿 변경과 글 추가·삭제는 다시 그려서 같았다. 다른 것은 정한 대로 늦게 반영되는 곳뿐이다. 비공개 글의 날짜와 글 요약문은 `/en/recent/`·`/sitemap.xml`·`/ko/categories/` 같은 목록에서 정기 재시작(3시간)이나 full rebuild 때까지 옛것으로 남는다. 같은 커밋에서 `fenced_theorem_blocks.rb`의 변환도 글별 입력이 같으면 지난 결과를 재사용하게 했다 ([c91bdfe5](https://github.com/math-jh/math-jh.github.io/commit/c91bdfe5), [a90e62d3](https://github.com/math-jh/math-jh.github.io/commit/a90e62d3), [7315ccd6](https://github.com/math-jh/math-jh.github.io/commit/7315ccd6)).

## 남은 2초와 옮기지 않은 프레임워크

| | 아침 | 저녁 |
|---|---|---|
| watch 리빌드 (본문 수정) | ~12초 | ~1.9초 |
| watch 리빌드 (글 추가·삭제·제목) | ~12초 | ~3.3~4초 |
| 서버 시작 빌드 | 120초 | ~10초 |
| clean build | ~150초 | 66초 |
| CI의 Jekyll 단계 | 89초 | 23초 |
| 리빌드당 메모리 | +28MB 누적 | 평평함 |

중간에 사용자가 Hugo로 옮기는 것도 물었다.

> 잠깐, 근데 Jekyll이랑 Hugo 중에, Hugo가 훨씬 빠른 것 같은데 거기로 마이그레이션하는 것도 생각해줘.

그래서 이 블로그가 Jekyll에 묶인 정도를 셌다. 글 818편 중 731편이 `:::` 정리 상자를 21,689줄 쓰고, kramdown 속성 표기가 14,554곳, Liquid 태그가 1,036곳이다. 자체 플러그인은 2,584줄이고 템플릿은 3,122줄이다. 사용자 플러그인을 받지 않는 Hugo로 옮기면 이 로직을 빌드 밖으로 빼거나 문법 수만 곳을 바꿔야 한다. 옮긴다면 markdown-it과 Liquid를 받는 Eleventy 쪽이 덜 아프다는 데까지만 정리했고, 사용자는 미뤘다.

> 그래 그럼 옮기는 건 나중에 하던가 하고 일단 수정 가능한거부터 하자.

손대지 않은 것도 있다. `graph_data`는 쓰기 단계에서 렌더된 HTML로 의존성 모델을 한 번 더 만든다(0.15초). 렌더 전 모델을 재사용해도 지금은 인용 쌍 2,540개가 같지만, Liquid가 만들어 내는 링크가 생기는 날 재사용판은 그것을 빠뜨린다. 0.15초와 바꿀 일은 아니다. 용어 데이터만 바뀌는 리빌드가 여전히 4초 남짓인 이유도 아직 다 설명하지 못했다.

맥 미니는 끝내 부르지 않았다. 2분 중 대부분은 같은 git 이력을 959번 다시 읽는 데 쓰이고 있었고, 그건 한 번 읽으면 되는 일이었다.
