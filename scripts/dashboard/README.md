# scripts/dashboard — 블로그 운영 대시보드

`https://preview.math-jh.com/dash/`. 미발행 글 현황·워커 상태·파이프라인·번역 큐·감사·색인·활동을
한자리에서 본다. 읽기 전용이다 — 레포에 아무것도 쓰지 않는다.

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

## API

| 엔드포인트 | 내용 |
| --- | --- |
| `/api/summary` | 전 섹션 데이터 한 덩이 (45초 캐시, `?fresh=1` 로 무효화) |
| `/api/log?name=<key>` | 워커 로그 tail |
| `/api/lint?path=<repo상대경로>` | 글 하나에 `.claude/hooks/md_lint.py` CLI 실행 |
| `/api/kotypo` (GET/POST) | KO-TYPOS '수정' 체크 상태 — POST 는 전체 map 교체, `~/.local/state/blog_dashboard_kotypo.json` 에 저장 (서버의 유일한 쓰기) |

데이터 출처: `_posts` frontmatter 스캔, `scripts/translation/translation_state.json`,
각 워커 로그, `scripts/audit/audit-report.md`,
`scripts/index-monitor/state-com.json`, `_data/recent_comments.yml`, `git log`,
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
