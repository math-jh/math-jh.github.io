# scripts/dashboard — 블로그 운영 대시보드

`https://preview.math-jh.com/dash/`. 미발행 글 현황·워커 상태·파이프라인·번역 큐·감사·색인·활동을
한자리에서 본다. 레포에는 아무것도 쓰지 않는다 (쓰기는 `~/.local/state` 의 상태 파일 셋뿐:
kotypo 체크·검토 판정과 메모·비교기 판본 선택).

## 구성

| 파일 | 역할 |
| --- | --- |
| `server.py` | stdlib HTTP 서버(8089, 127.0.0.1). 정적 파일 + `/api/*` |
| `index.html` | 셸 (`#app` + 모달 + pre-paint 테마) |
| `app.js` | hash 라우팅 SPA — 마스트헤드·개요·상세 섹션 렌더러 전부 |
| `dashboard.css` | 블로그 스킨(`_sass/minimal-mistakes/skins/_custom{,-dark}.scss`)의 토큰·자체를 그대로 |
| `favicon-gauge5.svg` | 파비콘 — 본사이트 마크(네이비 타일 + 브래스 네모, 8/16/sw3) 안에 계기판 |
| `restart.sh` | 서버 재기동 |
| `deploy/` | nginx 조각·crontab 줄 사본 (둘 다 레포 밖이라 재현용) |
| `compare.{html,css,js}` | **범용 판본 비교기** — 임의 ref 두 개를 나란히 (아래 참고) |
| `audit-2026-08.{html,css,js}` | 2026-08 전수 감사 전용판 (ad-hoc 노트를 직접 읽는다. 그 감사가 끝나면 수명이 다한다) |
| `pagediff.py` | 구워진 두 판본의 본문을 블록 단위로 정렬해 마크된 HTML 두 벌을 만든다 |
| `compare.py` | 비교기 데이터층 — 판본·diff·감사(audit.json)·메모/검토 상태 |
| `snapshot.py` | 임의 git ref 를 구워 HTML 만 남기는 스냅샷 빌더 (CLI) |
| `notes_cli.py` | 메모 목록·삭제 (CLI) — 지시서를 반영한 세션이 자기가 처리한 메모를 지운다 |

## 페이지

**개요가 허브다** — 탭 네비 없음. `/dash/` 개요(판정 한 줄 + 24시간 실행 히트맵 + 지표 6장 +
"지금 볼 것" + 파이프라인 + 최근 커밋 + 섹션 색인)에서 각 섹션으로 들어가고 `← 개요로` 로 돌아온다.
라우팅은 hash: `#workers` `#pipeline` `#drafts` `#weights` `#translation` `#audit` `#index` `#activity`.
구 경로(`/dash/workers` 등)는 서버가 index.html 을 주고 app.js 가 hash 로 리다이렉트한다.
감사(`#audit`)와 색인(`#index`)은 별도 페이지다. 번역 큐에는 검증기 KO-TYPOS 지적 목록이
뜨고(행 클릭 → 지적 전문 모달), 감사의 이슈 종류 행을 클릭하면 글·줄 단위 상세 모달이 열린다
(`audit-report.md` 의 Actionable items 를 서버가 kind 별로 파싱).

디자인 원본: claude.ai/design 프로젝트 `design_handoff_dashboard/` 번들 (2026-07-30 확정,
토큰·조판·상호작용 스펙은 그 README 참조).

## 판본 비교기 (`/dash/compare.html`)

두 판본의 **구워진 본문**을 나란히 놓고 diff 를 본다. 입구는 마스트헤드 설정 메뉴의
'판본 비교'. 주소 해시에 상태가 실린다: `#p=<글 경로>&a=<감사 slug>&o=<이전>&n=<이후>`.

- **판본은 임의 ref** — 브랜치·태그·sha·`HEAD~3`·`worktree` 를 그대로 받는다. 아직 안 구운
  판본이면 '굽기' 단추가 뜨고, 백그라운드로 굽는 동안(≈100초) 진행이 표시된다. 캐시 키는
  **sha** 라 움직이는 브랜치를 골라도 그 시점 커밋으로 굳는다. 한 번에 하나만 굽는다
  (여유 RAM 2GB, 빌드가 1.5GB).
- **감사를 고르면** `notes/audit-<slug>/audit*.json` 의 지적이 붙는다. 형식·절차·감사를 돌리는
  모델에게 주는 규격은 `scripts/audit/AUDIT-PROTOCOL.md` 가 정본이고,
  `scripts/audit/validate_audit_json.py` 가 그 규격을 기계로 확인한다 (특히 인용문이 base
  판본에 그대로 있는지 — 틀리면 비교기에서 **에러 없이** 그 항목만 안 뜬다). 항목은 인용문으로 base 블록을 잡고, 그 블록의
  변경에 카드가 붙는다. **미반영 의심**(반영했다는데 그 블록에 변경이 없는 것)은 상단
  숫자를 눌러 목록으로 볼 수 있다 — diff 만 봐서는 안 보이는 부류다.
- 오른쪽 패널은 **작업 지시서 전용**이다: 위에 고정된 메모 폼, 아래로 쌓이는 메모, 맨 밑에
  `지시서 복사`(이 글) / `전체 복사`. 지적·전문을 읽는 건 전부 호버 카드가 맡는다.

## 감사 검토 비교기 (`/dash/audit-2026-08.html`)

2026-08 감사 전용판. 개요의 '감사 검토 대기' 타일이 입구다. 범용판과 달리 `by-category`·
`findings`·`applied*` 를 직접 읽는다 (그 감사가 규약 형식 이전에 돌았기 때문).

- **양쪽 다 판본을 고른다.** 스냅샷은 `snapshot.py <ref>` 로 미리 구워 둔 HTML(~95MB·100초,
  sha 로 캐시)이고, `워킹트리`를 고르면 라이브 dev 서버(4001) 응답을 그대로 쓴다(빌드 불필요):

      python3 scripts/dashboard/snapshot.py 4a061156^     # 2026-08 전수 감사 직전
      python3 scripts/dashboard/snapshot.py 2f3143a7      # 감사 반영 완료 시점
      python3 scripts/dashboard/snapshot.py --list

  **고른 짝은 파이에 남는다** (`~/.local/state/blog_dashboard_compare.json`). 대량 sweep 을
  검토할 때는 같은 두 판본을 며칠씩 오가므로 새로고침마다 기본값으로 돌아가면 성가시다.
  우선순위는 **주소 해시 > 지난번에 고른 것 > 기본값**이고, 기본값은 **가장 오래된 스냅샷 ↔
  가장 최근 스냅샷**이다(하나뿐이면 ↔ 워킹트리). 감사 선택도 같이 기억한다.
  (감사 전용판 `/dash/audit-2026-08.html` 은 `10a818f3 ↔ 워킹트리` 로 고정이라 이 저장을
  쓰지 않는다.)
  구간 전체를 훑는 검토에서 워킹트리를 오른쪽에 두면 크론(번역·용어 추출·terms-lint)이
  30 분마다 커밋해 검토 중에 대상이 움직이고, 그 편집이 감사 변경과 섞여 보인다.

- **정렬은 4 단계**(`pagediff.py` 머리주석): 블록 해시 정확 일치 → 못 붙인 틈 안에서만 유사도
  DP(단조 1:1·하한 0.6) → 짝지어진 블록 안 단어 diff → 마크. 라벨 id 는 가점으로만 쓴다
  (블록 하나 삽입에 뒤 형제가 전부 재번호되므로 하드 앵커로 쓰면 뒷부분이 통째로 어긋난다).
  유사도가 하한 아래면 짝짓지 않고 "통째 교체"로 보여준다 — 오정렬이 나도 화면은 안 짝지었을
  때와 같아진다.
- **안전망 둘**: `원문 diff` 버튼(= `git diff`, 정본)과 불일치 게이트. 게이트는 hunk 수가 아니라
  **바뀐 줄 수**로 판정한다 (한 hunk 가 절 하나를 덧붙이면 블록은 정당하게 여럿 바뀐다).
  실측: 423편에서 변경블록/변경줄 비는 중앙값 0.42·최대 0.75 라 임계 1.0 은 여유가 있다.
- **읽는 것은 호버, 쓰는 것은 레일.** 변경에 마우스를 올리면 이어붙은 감사 지적의 요약·수정안·
  **전문**이 뜬다 (전문은 diff payload 에 같이 실려 오므로 왕복이 없다). 오른쪽 레일은 지적
  목록이 아니라 **작업 패널**이다 — 클릭한 변경 하나의 판정 버튼 + 메모 + 지시서 복사.
  지적 원본은 `notes/audit-2026-08/by-category/*.md`(정본) · `findings/*.md`(전문) ·
  `applied*/`(반영 기록).
- **지적 ↔ 변경 잇기**는 정밀도 우선이다. 지적이 `$…$`·인용부호로 집어 말한 조각이 실제로 손댄
  자리에 나타날 때만 잇고, 못 이으면 호버에 "지적 없는 변경"으로 남긴다 (근거 없는 수정이야말로
  봐야 할 것이다). 반대로 **본문에 못 이은 지적**은 레일 머리에 모아 둔다 — 미반영일 수 있는
  것이고, diff 는 그것을 보여주지 못한다.
- **임의 위치 메모**: 본문에서 문장을 끌어 선택하면 그 자리가 잡히고 메모를 단다. 위치는
  **줄번호가 아니라 인용문 + 절 제목 + 정리 라벨**로 적는다 — 마크다운을 열지 않고 말로만
  지시하기 위해서고, 줄번호는 수정 한 번에 어긋나기 때문이다.
- **검토 판정·메모는** `~/.local/state/blog_dashboard_review.json` 에 병합 저장한다
  (`items` = 글 × 지적 id × 판정 × 메모, `posts` = 글 단위 검토함, `notes` = 임의 위치 메모).
- **Claude 에게 넘기기**: `지시서 복사` 버튼, 또는 세션에서 직접
  `curl -s http://127.0.0.1:8089/api/compare/instructions` (경로 없이 부르면 전체).
  승인은 빠지고 되돌리기·추가수정·메모만 인용문과 함께 나온다. 지시서 끝에는 **반영 후
  그 메모들을 지우는 명령**이 실린 id 와 함께 붙는다 (`notes_cli.py --del n123 …`) —
  id 로 지우므로 지시서를 만든 뒤 새로 적은 메모는 남는다.
- 호버 카드는 **드래그 중과 선택이 살아 있는 동안은 안 뜬다.** 문장을 끌어 메모를 다는 게
  주된 동작이라 카드가 그 위를 덮으면 안 된다 (누르는 순간 감추고, 선택이 남아 있으면
  다시 안 띄운다).
- **목록 필터**: 변경된 것만 · KO만 · 미검토만 · **개정 중(revising)만**. revising 플래그는
  워킹트리 frontmatter 에서 읽는다(고른 판본이 아니라). 검토를 마친 글은 목록 맨 아래로 내려간다.
- 단축키: `n`/`p` 변경 이동, `[`/`]` 글 이동, `m` 메모 쓰기, `s` 원문 diff, `Esc` 닫기.

## API

| 엔드포인트 | 내용 |
| --- | --- |
| `/api/summary` | 전 섹션 데이터 한 덩이 (45초 캐시, `?fresh=1` 로 무효화) |
| `/api/log?name=<key>` | 워커 로그 tail |
| `/api/lint?path=<repo상대경로>` | 글 하나에 `.agents/hooks/md_lint.py` CLI 실행 |
| `/api/kotypo` (GET/POST) | KO-TYPOS '수정' 체크 상태 — POST 는 전체 map 교체, `~/.local/state/blog_dashboard_kotypo.json` 에 저장 |
| `/api/compare/list?old=&new=&audit=` | 비교 대상 글 목록 + 스냅샷 목록 + 진행 집계 (비면 기본 짝) |
| `/api/compare/refs` | 판본 고르개용 — 브랜치·최근 커밋 40개·구워둔 스냅샷 |
| `/api/compare/audits` | 감사 목록 — `notes/audit-<slug>/audit*.json` 을 slug 별로 합쳐 센다 |
| `/api/compare/snapshot?ref=` · POST | 판본 상태 조회 / 굽기 시작 (백그라운드, 하나씩) |
| `/api/compare/snapshot-delete` (POST) | 구워둔 판본 삭제 (판본당 ~90MB) |
| `/api/compare/prefs` (GET/POST) | 범용 비교기가 마지막으로 고른 판본 짝·감사 |
| `/api/compare/diff?path=&old=&new=` | 마크된 pane HTML 두 벌 + hunk + 감사 지적 + 원문 diff |
| `/api/compare/finding?key=&id=` | 지적 전문 (findings 의 해당 절) |
| `/api/compare/instructions[?path=]` | 메모·판정을 붙여 쓸 수 있는 작업 지시서 (평문) |
| `/api/compare/macros?v=<sha\|worktree>` | 그 판본의 `katex-macros.js` |
| `/api/review` (POST) | 검토 판정·메모 — **항목 단위 병합** 저장 (kotypo 처럼 통째 교체하지 않는다). `kind`: `item`·`post`·`note`·`note-del`·`note-done` |

데이터 출처: `_posts` frontmatter 스캔, `scripts/translation/translation_state.json`,
각 워커 로그, `scripts/audit/audit-report.md`,
`scripts/index-monitor/state-com.json`, GitHub의 열린 `comment/*` PR, `git log`,
`systemctl --user is-active jekyll-blog`, `~/Projects/hud-display/state/claude_quota.json`.

## 손볼 때 알아야 할 것

- **재기동은 `./restart.sh` 로만.** 즉석 `pgrep -f`/`pkill -f` 는 부분 문자열 매치라
  경로를 언급만 한 셸까지 잡는다 — restart.sh 의 앵커된 패턴
  (`^/usr/bin/python3 [^ ]*/dashboard/server\.py$`)을 쓰는 이유. 서버 기동은
  절대경로 `/usr/bin/python3` 이어야 이 패턴·keeper cron 과 맞는다.
- **자산·API 참조는 절대경로(`/dash/…`, `/assets/…`)여야 한다.** 구 상세 경로에서
  상대경로가 다른 디렉토리로 풀린다. 폰트·아이콘은 블로그 자산(`/assets/css/fonts/`)을
  같은 오리진에서 재사용한다 (nginx 4000 이 Jekyll `_site` 를 서빙하므로 도달 가능).
- nginx 가 `/dash/` 접두사를 벗겨 보내므로 `server.py` 가 보는 경로에는 접두사가 없다.
- 테마는 블로그와 같은 `MTHEME` 쿠키(auto|light|dark)를 공유한다. FOUC 방지용 pre-paint
  스크립트가 index.html head 에 있다. 테마 선택은 마스트헤드 설정 메뉴(tune 아이콘,
  블로그 masthead 와 같은 꼴에서 언어만 뺀 것 — 테마 서브메뉴 + 블로그 링크) 안에 있고,
  워드마크 클릭은 대시보드 개요(`#`)로 온다.
- **ko/en 짝은 날짜 접두사를 뗀 slug 로 맞춘다.** en 파일은 번역 시점 날짜를 달고
  생성돼 ko 와 파일명이 다르다.
- `_posts/Misc/**` 는 `ko/en` 하위 폴더 없이 평평한 단일 언어다.
- weight 지도를 `1..max` 로 채우면 부록 계열(100·200·300번대) 때문에 빈 칸이 수백 개
  생긴다. 실제 weight 순서로 깔고 간격 4 초과는 생략 표시로 접는다.
- `_config.yml` 의 `exclude` 에 `scripts` 가 있어 이 디렉토리는 Jekyll 빌드에 안 들어간다.
  비교기가 프로덕션에 안 뜨는 근거도 이것이다 — 글이 아니라 대시보드에 둔 이유.

### 비교기 쪽 함정 (본문 CSS 와 한 문서에 산다)

- **`main.css` 와 `main_dark.css` 중 안 쓰는 쪽을 `disabled` 로 꺼야 한다.** 둘 다 살려 두면
  나중 것(dark)이 이겨 밝은 배경에 밝은 글자가 얹힌다 — 정리 박스 안 본문이 유령처럼 사라진다.
  대시보드 본체는 `data-theme` 만 세우면 되지만 비교기는 링크 토글까지 해야 한다
  (로직 원본은 `_includes/js/theme-core.js`).
- **`[hidden]` 은 클래스의 `display` 에 밀린다.** 모달·원문 패널처럼 클래스로 display 를 주는
  요소는 `[hidden]{display:none!important}` 로 다시 이겨 주지 않으면 처음부터 열려 있다.
- **`<ins>` 는 본문에서 이미 두 번 전용됐다** — 전역(`_base`)에서 밑줄 2px + `margin-right:1em`,
  정리 박스 안(`_notices`)에서는 굵은 산세리프 라벨. diff 의 삽입 표시로 쓰려면 둘 다 되돌려야
  한다 (안 그러면 낱말 사이가 1em 씩 벌어진다).
- **pane 마다 id 에 접두사(`L-`/`R-`)를 붙인다.** 도식 svg 는 `<defs>` 글리프를 `<use href="#…">`
  로 참조하는데, 한 문서에 두 판본이 있으면 **처음 만난 id** 로 해석돼 오른쪽 도식이 왼쪽
  글리프로 그려진다 — 에러 없이 틀린 그림이 나온다 (같은 계열: `367af0e5` xref 미리보기).
- 블록에 `<div>` 를 덧씌우지 않고 **자기 여는 태그에 속성을 얹는다**. 본문 CSS 가 `.page__content`
  의 자식 구조를 보므로 감싸면 조판이 미묘하게 달라져 diff 아닌 것이 diff 로 보인다.
- 증명은 `<details>` 라 기본이 접힘이다. pane 에서는 강제로 펴야 접힌 안쪽 변경이 안 샌다.
- 스냅샷 빌드는 worktree 를 쓰지 않는다(이 repo 는 read-only git 만 허용). `ls-tree`+`cat-file`
  로 풀고 `.git` 만 심볼릭 링크로 건다 — `last_modified_git.rb` 가 `git -C <source> log` 로
  날짜를 읽으므로 링크가 없으면 그 플러그인이 빈손이 된다.
