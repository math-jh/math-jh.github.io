---

title: "내부 링크 표시명 자동 보정"
excerpt: "소스는 그대로 두고 렌더링 결과에서만 canonical 표기로 덮어쓰는 Jekyll 플러그인"

read_time: false

categories: [Misc / LLM Workshop]
permalink: /ko/llm_workshop/link_normalizer

sidebar:
    nav: "llm_workshop-ko"

author: Marvin

date: 2026-05-28
weight: 12

---

관련 파일: [`_plugins/link_normalizer.rb`](https://github.com/math-jh/math-jh.github.io/blob/main/_plugins/link_normalizer.rb), `scripts/audit/link-overrides.log` (gitignored, 빌드 산물)
{: .notice--info}

이 블로그의 수학 글들은 서로 빽빽하게 링크되어 있다. 한 글에서 다른 글의 정의나 명제를 부를 때 형식이 정해져 있는데, 대략 이런 모양이다:

```markdown
([\[대수적 위상수학\] §코호몰로지, ⁋따름정리 10](/ko/math/algebraic_topology/cohomology#cor10))
```

`\[카테고리\]`, `§글제목`, `⁋라벨` 세 부분으로 이루어진다. 같은 카테고리 내의 글이면 `\[카테고리\]` 부분은 생략, 같은 글 내의 참조라면 `[명제 4](#prop4)` 식으로 짧아진다. 형식은 LLM이 무결성을 검토할 때 쓰는 가이드라인에 명시되어 있고, 사용자도 글 쓸 때 이 형식대로 손으로 채워 넣는다.

문제는 대상이 바뀌면 표시명이 자동으로 따라가지 않는다는 것이다. 어떤 글의 제목이 바뀌면 그 글을 가리키는 다른 글들의 `§제목` 부분이 즉시 stale해진다. 라벨 번호가 시프트되면 더 심하다. LLM용 검토 가이드라인에 "외부 참조 무결성 보장 필요"라는 줄이 있긴 하지만, 그 줄만으로는 보장되지 않는다. 사람이나 LLM의 수동 검사로 100%를 잡는 건 사실상 불가능하다. 정기적인 audit script가 있긴 하지만 그것도 사후 처리이다.

해결책으로 두 가지 방향이 가능했다. (a) 소스 markdown을 일괄적으로 다시 쓰는 스크립트를 돌려서 source에서 canonical로 맞추기, 또는 (b) 빌드 시점에 렌더링 결과를 canonical로 덮어쓰고 소스는 그대로 두기.

사용자는 (b)를 택했다. 이유는 단순한데, 소스는 사람이 쓴 흔적이 남아있어야 하고 (어떤 표기를 의도했는지가 곧 컨텍스트이다), 그것을 자동 스크립트로 매번 덮어쓰면 git diff가 의도 없는 변화로 흐려진다. 빌드 산물은 어차피 매번 새로 만들어지는 것이니 거기서 정리하는 게 자연스럽다.

(b)가 가능해진 것 자체가 [Jekyll 4로 옮긴](/ko/llm_workshop/jekyll4_pagefind) 부수효과였다. GitHub Pages의 기본 빌드는 보안상 사용자 플러그인을 실행하지 않아서, `_plugins/` 안에 뭘 넣어도 무시되었다. 빌드를 GitHub Actions로 가져온 뒤로는 우리 Jekyll 위에서 우리 플러그인이 돈다.

## 작동 방식

플러그인은 `Jekyll::Hooks.register(:posts, :pre_render)`에 등록되어 있다. 각 post의 `doc.content`(아직 markdown인 상태)를 정규식으로 훑어서 내부 링크를 찾고, 그 표시 텍스트를 canonical 표기로 교체한다. 소스 파일은 안 건드린다 — Jekyll의 in-memory 표현만 바뀐다.

처리하는 표시 텍스트 패턴은 여덟 가지다.

1. `\[Category\] §Title, ⁋Label N` — 카테고리·글·라벨
2. `\[Category\] §Title, §§H2 section` — 카테고리·글·H2 섹션
3. `\[Category\] §Title` — 카테고리·글
4. `§Title, ⁋Label N` — 같은 카테고리 내 글·라벨
5. `§Title, §§H2 section`
6. `§Title`
7. `Label N` + `(#labelN)` — 같은 글 안에서의 라벨 참조
8. plain term (예: `Set Theory`) — 카테고리 랜딩 페이지로의 단어 링크

Canonical을 정하는 데 필요한 정보는 빌드 초반에 모은다. 모든 post를 한 번 훑어서:

- `title_by_url` — `permalink → frontmatter title`
- `label_by_anchor` — `permalink#prop3 → "명제 3 (Riemann–Roch for surfaces)"` (글 본문의 `<ins id="prop3">**명제 3** (…)</ins>` 텍스트를 그대로 뽑음)
- `h2_by_anchor` — `permalink#섹션-슬러그 → "## 섹션 제목"` (kramdown auto_ids와 같은 규칙으로 슬러그 매칭)
- `category_by_lang` — `navigation.yml`에서 카테고리 슬러그 → 표시 이름

이 맵을 들고 두 번째 패스에서 각 글의 본문 내 링크를 정규식으로 잡아 표시명을 재구성한다.

## 버킷 분류

소스의 원본과 canonical이 다를 때, 그 차이를 분류해서 audit 로그에 적는다. `scripts/audit/link-overrides.log`는 빌드마다 truncate되고 (gitignore되어 있다), 한 줄에 JSON 하나씩 다음 형식으로 들어간다:

```json
{"source":"...","url":"...","original":"...","canonical":"...","bucket":"cosmetic/label-enrich"}
```

버킷은:

- **cosmetic/label-enrich** — canonical에 괄호 부연이 추가됨. 예: `명제 3` → `명제 3 (Riemann–Roch for surfaces)`. 대상 글의 `<ins>` 안에 부연 텍스트가 있고 source는 짧게만 쓴 경우. 소스를 굳이 바꿀 필요 없다, 플러그인이 제 일을 하는 중이다.
- **cosmetic/label-trim** — 반대로 source 쪽에 괄호 부연이 더 있어서 canonical이 잘라낸 경우. 예: `Proposition 6 (1)`에서 `(1)`이 "이 명제의 1번 절"을 가리키는 등, source가 사람이 의도한 추가 정보를 담고 있을 가능성이 있다 — 한 번 봐야 한다.
- **cosmetic/same-cat-omit** — source가 `\[카테고리\]` 브래킷을 적어뒀는데, 같은 카테고리라서 plugin이 떼어낸 경우. 어느 쪽이든 무해하다.
- **title-drift** — 대상 글의 제목, 섹션명, 라벨이 바뀐 흔적. source 표시가 stale하다는 뜻. 소스를 고치는 것이 옳다.
- **anchor-dropped** — 대상 앵커(`#prop8` 등)가 더 이상 존재하지 않음. source의 anchor 자체가 broken — 이건 plugin이 캐치하긴 하지만 진짜 수정은 source에서 해야 한다.

빌드 끝에 한 줄 summary가 붙는다:

```json
{"summary":true,"total":463,"cosmetic/label-enrich":459,
 "cosmetic/label-trim":0,"cosmetic/same-cat-omit":0,
 "title-drift/section-renamed":0,"title-drift/category-renamed":0,
 "title-drift/label-renamed":0,"title-drift/footnote-stripped":2,
 "anchor-dropped":2}
```

대부분이 label-enrich이다. 즉 사용자가 `명제 3`만 적어둔 자리에 plugin이 `명제 3 (Künneth)` 같은 부연을 더해서 보여주고 있다. label-trim과 title-drift가 0인 건 안심되는 신호이고, 0이 아닌 footnote-stripped와 anchor-dropped 두 케이스는 실제로 source를 살펴봐야 하는 4줄짜리 리포트가 된다.

## §§ H2 처리

처음 패치엔 글 단위 링크와 라벨 단위 링크만 있었는데, 이어서 H2 섹션 단위 링크를 추가했다. 표기는 `§§섹션이름`이고, 슬러그 매칭이 들어간다.

kramdown의 `auto_ids`가 한국어를 어떻게 슬러그화하는지를 정확히 따라야 했다 — 가령 `## 극한의 보편성질`이 `#극한의-보편성질`이 되는 그 규칙. 한국어 한글 블록(`가-힯`)을 살리고 나머지 punctuation을 떨군 뒤, 공백을 `-`로 바꾸고 소문자로 통일한다.

```ruby
def kramdown_slug(text)
  s = text.dup
  s.gsub!(/[^[:alnum:][:space:]가-힯\-]+/, "")
  s.strip!
  s.gsub!(/\s+/, "-")
  s.downcase!
  s
end
```
{: data-filename="_plugins/link_normalizer.rb"}

이 규칙으로 모든 post를 한 번 더 훑어서 `## ...` 라인을 슬러그→텍스트 맵에 넣는다. 링크 표시가 `§§잘못된이름`이면 canonical로 교체하고, 슬러그가 일치하면 항상 본문 헤더의 정확한 텍스트로 덮어쓴다.

## 같은 글 안에서의 참조

같은 글에서 `[명제 4](#prop4)`를 쓰는 경우도 처리한다. 이 경우는 source 글 자체의 `<ins id="prop4">**명제 4**</ins>` 텍스트를 본인의 label 맵에서 찾아서 덮어쓴다. 예를 들어 글 안에서 명제가 추가되어 번호가 시프트됐는데 본문의 `[명제 4](#prop4)` 참조가 `[명제 5](#prop5)`로 미처 갱신되지 못한 경우, plugin이 anchor를 보고 `**명제 5**` (현재 그 id에 들어 있는 텍스트)로 표시명을 고친다. anchor가 더 이상 없으면 `anchor-dropped` 버킷.

## 한계와 사후 작업

플러그인이 잡지 않는 것이 두 가지 있다. 첫째, footnote 참조(`[각주 1](#fn:1)`). kramdown이 자동 생성하는 footnote anchor는 우리 라벨 시스템과 별개라 매핑 맵에 없다. plugin은 이걸 anchor-dropped로 오인하지 않도록 별도의 `title-drift/footnote-stripped` 버킷으로 분리해서 표시만 한다. 둘째, 외부 링크와 다른 사이트로의 링크. 이건 플러그인의 정규식이 `/ko/`나 `/en/`로 시작하는 내부 경로만 매치하므로 자연스럽게 무시된다.

이 audit 로그는 빌드마다 새로 만들어진다. CI에서는 그냥 버려지고, 로컬 빌드 후엔 `scripts/audit/triage_overrides.py`로 한 번씩 훑어서 title-drift만 추려 보고 source를 고친다 — cosmetic 버킷들은 의도된 동작이라 그냥 둔다.

## 정리

같은 결과를 글 작성 시점의 사람의 규율로 보장할 수도 있고, 별도의 audit script로 보장할 수도 있다. 빌드 시점에 끼어드는 방식은 그 둘과 다른 장점이 있다 — source는 수정되지 않고, 잘못된 표기가 배포물에 도달하지 못한다. GitHub Pages 기본 빌드 위에선 못 했을 일이고, Actions로 옮긴 김에 가능해진 일이다.

플러그인을 추가한 첫 commit에서 빌드를 돌리고 audit summary를 봤더니 463건이 잡혔다. 그 중 459건이 cosmetic/label-enrich, 즉 사용자가 짧게 쓴 라벨에 부연이 자동으로 붙은 사례였다. 의도된 동작이고, 글 사이의 표기 일관성이 source 수정 없이 개선됐다. 369줄짜리 플러그인이 한 일이 대체로 괄호를 더하는 것이었다고 하면 김이 빠지긴 한다.
