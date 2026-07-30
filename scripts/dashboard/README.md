# scripts/dashboard — 블로그 운영 대시보드

`https://preview.math-jh.com/dash/`. 미발행 글 현황·워커 상태·번역 큐·감사·색인·활동을
한자리에서 본다. 읽기 전용이다 — 레포에 아무것도 쓰지 않는다.

## 구성

| 파일 | 역할 |
| --- | --- |
| `server.py` | stdlib HTTP 서버(8089, 127.0.0.1). 정적 파일 + `/api/*` |
| `index.html` | 공통 셸. 섹션 경로 전부 이 파일을 받는다 |
| `app.js` | `location.pathname` 으로 뷰를 고르는 렌더러 |
| `dashboard.css` | 블로그 스킨(`_sass/minimal-mistakes/skins/_custom{,-dark}.scss`)의 색·폰트를 따른다 |
| `favicon-hammer3.svg` | 적용 중인 파비콘. 나머지 `favicon-*.svg` 는 탈락 후보 |
| `restart.sh` | 서버 재기동 |
| `deploy/` | nginx 조각·crontab 줄 사본 (둘 다 레포 밖이라 재현용) |

## 페이지

`/dash/` 는 개요만 둔다 (타일 · "지금 볼 것" 임계값 알림 · 워커 한 줄 요약 · 최근 커밋).
상세는 `/dash/workers`, `/dash/drafts`, `/dash/weights`, `/dash/translation`,
`/dash/audit`, `/dash/activity`.

## API

| 엔드포인트 | 내용 |
| --- | --- |
| `/api/summary` | 전 섹션 데이터 한 덩이 (45초 캐시, `?fresh=1` 로 무효화) |
| `/api/log?name=<key>` | 워커 로그 tail |
| `/api/lint?path=<repo상대경로>` | 글 하나에 `.claude/hooks/md_lint.py` CLI 실행 |

데이터 출처: `_posts` frontmatter 스캔, `scripts/translation/translation_state.json`,
각 워커 로그, `scripts/audit/audit-report.md`,
`scripts/index-monitor/state-com.json`, `_data/recent_comments.yml`, `git log`,
`systemctl --user is-active jekyll-blog`, `~/Projects/hud-display/state/claude_quota.json`.

## 손볼 때 알아야 할 것

- **재기동은 `./restart.sh` 로만.** `pgrep -f dashboard/server.py` 를 셸 명령줄에 직접
  쓰면 그 명령줄까지 패턴에 걸려 자기 자신을 죽인다 (겪은 사고: 구 프로세스 생존 +
  신 프로세스 포트 충돌사). 실행은 절대경로로 — keeper cron 과 패턴을 맞춘다.
- **자산·API 참조는 절대경로(`/dash/…`)여야 한다.** 상세 경로(`/dash/drafts`)에서
  상대경로가 다른 디렉토리로 풀린다.
- nginx 가 `/dash/` 접두사를 벗겨 보내므로 `server.py` 가 보는 경로에는 접두사가 없다.
- **ko/en 짝은 날짜 접두사를 뗀 slug 로 맞춘다.** en 파일은 번역 시점 날짜를 달고
  생성돼 ko 와 파일명이 다르다.
- `_posts/Misc/**` 는 `ko/en` 하위 폴더 없이 평평한 단일 언어다.
- weight 지도를 `1..max` 로 채우면 부록 계열(100·200·300번대) 때문에 빈 칸이 수백 개
  생긴다. 실제 weight 순서로 깔고 간격 4 초과는 생략 표시로 접는다.
- `_config.yml` 의 `exclude` 에 `scripts` 가 있어 이 디렉토리는 Jekyll 빌드에 안 들어간다.
