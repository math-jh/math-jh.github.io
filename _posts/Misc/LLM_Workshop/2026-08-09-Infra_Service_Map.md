---

title: "인프라 인벤토리와 service-map"
excerpt: "무언가를 바꿨을 때 어디를 또 바꿔야 하는지를 기록하는 두 파일, 에러 없이 깨지는 결합을 적는 contracts, 매일 도는 실측과 DRIFT, 건드리기 전에 계약을 들이미는 훅, 지침 파일 구조, chattr +i 동결과 폴더 재배치"

read_time: false

categories: [Misc / LLM Workshop]
permalink: /ko/llm_workshop/infra_service_map

sidebar:
    nav: "llm_workshop-ko"

author: Marvin

date: 2026-08-09
weight: 70
group: pi

---

관련 파일: `~/Projects/infra/INVENTORY.md`, `~/Projects/infra/service-map.yml`, `~/Projects/infra/gen-inventory.py`, `~/Projects/infra/refresh.sh`, `~/Projects/infra/agents/`, `~/.local/bin/infra-freeze`, 블로그 저장소의 [`CLAUDE.md`](https://github.com/math-jh/math-jh.github.io/blob/main/CLAUDE.md)
{: .notice--info}

8월 8일에 연구 크론이 tmux 상주 세션에서 `claude -p` 단발 실행으로 넘어간 뒤, 상태 대시보드는 연구 봇이 41시간째 돌지 않았다고 표시했다. 봇은 멀쩡히 돌고 있었다. 이관 때 로그 문구 하나가 바뀌었는데, 그 문구로 마지막 실행을 판정하던 대시보드의 파서를 아무도 기억하지 못했다. 이 Pi의 크론, systemd 유닛, 포트, 스크립트 수십 개는 서로를 파일과 문자열로만 알고 있어서, "이걸 바꾸면 저기도 바꿔야 한다"는 사실은 누군가의 머릿속에만 있었다. 8월 9일에 그 사실을 적어 두고 바꾸기 전에 확인하게 하는 장치가 `~/infra/`(지금의 `~/Projects/infra/`)에 생겼다.

## 생성되는 INVENTORY와 손으로 쓰는 service-map

정본은 두 파일이다. `service-map.yml`은 7월 21일의 실측을 시드로 손으로 써 오던 맵이고, 8월 9일에 그 옆에 생성기가 매일 다시 쓰는 `INVENTORY.md`가 붙었다.

| 파일 | 담는 것 | 쓰는 주체 |
|---|---|---|
| `INVENTORY.md` | 지금 실제로 도는 크론·유닛·컨테이너·포트·스크립트, 그리고 DRIFT | `gen-inventory.py`만. 손으로 고치면 다음 실행이 덮는다 |
| `service-map.yml` | 파급, 재시작, 검증, 암묵적 결합, 안 도는 것과 그 이유 | 사람과 모델 |

생성기의 docstring에 이 분업이 그대로 적혀 있다. 생성기는 `service-map.yml`을 읽기만 하고 절대 쓰지 않는다. 큐레이션된 지식을 기계가 덮어쓰면 안 되기 때문이고, 둘은 DRIFT 절에서 단방향으로만 만난다. 실측이 정본이라는 원칙도 맵 머리말에 있다. 맵과 실제가 다르면 실제를 따르고 맵을 고친다.

`service-map.yml`의 주요 섹션은 `hosts`, `services`, `contracts`, `dormant`이다. 8월 9일 판에는 `services`가 39개, `contracts`가 8개 있었고, 11월에는 둘 다 60개 안팎이 된다. 서비스 entry는 무엇이 어디 있는지(`config`, `unit`)뿐 아니라 "이럴 때는 이렇게"를 `impacts`로 적는다. 8월 9일 판의 연구 크론 entry(`research-pipeline`)에서 한 대목을 옮기면 이렇다.

```yaml
impacts:
  - when: drive.sh 의 로그 문구 변경
    do: >
      status_dashboard.py 의 role_last_runs() 파서가 기동 줄 접두사로 역할
      최종 실행을 판정한다. 문구를 바꾸면 대시보드가 조용히 "며칠째 안 돎"을
      표시한다. 2026-08-09 실제 발생(41시간 오차).
    refs: [status-dashboard]
  # ...
verify: tail -5 ~/Database/research/cron/tmux/drive.log
```
{: data-filename="~/infra/service-map.yml · ef1940ed 시점, services.research-pipeline 일부 생략, 문장부호 정리"}

`when`은 하려는 변경이고 `do`는 그때 같이 해야 하는 일이다. `refs`는 같이 봐야 할 다른 entry를 가리킨다. 생략한 자리에는 슬롯 시각, quota 임계, 보고 범위 계산을 바꿀 때와 director가 실패한 날의 항목이 같은 꼴로 이어지고, `verify`에는 고친 뒤 정상인지 볼 명령을 적는다. 이 entry는 11월 6일에 연구 파이프라인을 철거하면서 아래의 계약과 함께 맵에서 빠진다.

적는 기준은 9월 12일에 한 번 좁혀졌다. 머리말의 표현으로는 "한 컴포넌트 안에서 닫히는가"이다. 남이 파싱하는 모양(로그 접두사, 커밋 제목, owner 문자열)은 남기고, 자기 안에서 끝나는 출력의 모양과 소스를 열면 나오는 서명 나열은 뺀다. 남길 것은 결합, 조용한 실패, 코드에 없는 이유 셋이라고 되어 있다.

## 에러 없이 깨지는 결합을 적는 contracts

서비스와 포트만 적던 초기 맵은 8월 8일 이관을 막지 못했다. 머리말이 그 사정을 적고 있다. 서비스는 둘 다 등재돼 있었는데 둘을 잇는 것이 맵에 없었다. 파급은 대개 서비스 사이가 아니라 파일, 포맷, 마커를 타고 흐른다. 그래서 8월 9일에 그 층을 따로 적는 `contracts:` 섹션이 생겼다. 사고 자체가 첫 번째 항목이 되었다.

```yaml
research-drive-log-format:
  producer: ~/Database/research/cron/tmux/drive.sh
  artifact: "~/Database/research/cron/tmux/drive.log: `[HH:MM:SS role] 메시지`"
  consumers:
    - "~/Projects/status_dashboard/status_dashboard.py :: role_last_runs(): 역할별 최종 실행 판정"
  detail: >
    파서는 메시지의 **접두사**로 기동 줄을 고른다(_DRIFT_LAUNCH_PREFIXES:
    "injected" = tmux 시절, "launching claude -p" = 현재). 날짜가 없는 로그라
    파일 mtime 에 앵커해 거꾸로 걸으며 자정을 넘긴다.
  breaks: >
    2026-08-09 실제 발생. 08-08 이관으로 "injected"가 사라져 대시보드가
    41시간째 안 돈 것처럼 표시. **아무 에러도 안 났다.**
  updated: 2026-08-09
```
{: data-filename="~/infra/service-map.yml · ef1940ed 시점, contracts 항목 발췌, 문장부호 정리"}

항목의 골격은 `producer`(만드는 쪽), `artifact`(그것이 무엇인가), `consumers`(읽는 쪽), `breaks`(어긋나면 어떻게 조용히 깨지는가)이다. `breaks`에 사고 이력이 실려 있는 것이 중요하다. 나중에 훅이 이 항목을 들이밀 때, "조심하라"가 아니라 "이 문구를 바꿨더니 41시간 오차가 났다"를 읽게 된다.

계약을 넣을지 가르는 질문은 하나다. 이걸 바꿨을 때 에러 없이 조용히 깨지는 다른 코드가 있는가. 로그 줄의 접두사, 마커 문자열, json 필드, 크론 블록의 마커, 프롬프트가 계산하는 값이 전부 여기에 해당한다.

첫 판에는 producer가 이미 사라진 계약도 하나 있었다. 옛 tmux 드라이버의 세션 이름 `research-{role}`을 프로세스 목록에서 찾던 계약인데, 8월 8일 이관으로 그 이름이 없어진 뒤 대시보드의 메모리 프로브는 늘 0을 냈다. 맵은 이 값을 일부러 고치지 않는다고 적는다. 프런트엔드가 그 값을 그리지 않으니 오해를 낳지 않고, 실측 없이 새 판별식을 짐작하지 않기로 했다는 것이 이유이며, 그 판단은 8월 9일 사용자의 것으로 기록되어 있다. 이 계약은 처음에 `contracts`에 `status: 죽은 계약`을 달고 남았다가 9월 12일에 `dormant` 아래로 옮겨졌다. `contracts`에 두면 소비자 파일을 건드릴 때마다 훅이 지킬 것 없는 계약을 들이밀기 때문에, 기록은 남기고 경고에서만 뺀 것이다.

## 하루 한 번의 실측과 DRIFT

생성기는 `crontab`, `systemctl`, `docker`, `ss`, 스크립트 디렉터리를 훑는다. 훑을 디렉터리 목록은 `SCAN_DIRS`에 있다. 출력은 전부 정렬해서 결정적으로 만들고, 헤더의 생성 시각을 뺀 본문의 해시를 상태 파일에 남겨서 마지막 줄에 `CHANGED=0|1`을 찍는다. 매일 05:40의 `refresh.sh`가 이 값을 보고 커밋 여부를 정한다.

```bash
out="$(/usr/bin/python3 "$INFRA/gen-inventory.py" 2>&1)"
rc=$?
# ...
# 생성기가 "본문 그대로"라고 하면 커밋하지 않는다.
case "$out" in
  *CHANGED=0*) exit 0 ;;
esac
# ...
git -C "$INFRA" commit -q -m "inventory: $(date '+%Y-%m-%d') (drift ${drift})"
```
{: data-filename="~/Projects/infra/refresh.sh · 일부 생략"}

`refresh.sh`는 생성기의 출력을 로그에 한 줄로 남기고, 생성기가 실패하면 커밋하지 않고 끝난다. 마지막 줄이 `CHANGED=0`이면 거기서 멈추고, 아니면 상태 파일에서 DRIFT 합계를 읽어 커밋 제목에 넣는다. 커밋을 조건부로 하는 것은 `git log`를 읽을 수 있게 하려는 것이다. 시각만 다른 커밋이 매일 쌓이면 "무엇이 실제로 달라졌나"를 로그에서 볼 수 없다. 커밋 제목에 DRIFT 건수가 들어가므로, 인프라 저장소의 로그가 곧 DRIFT 건수의 기록이 된다.

DRIFT는 INVENTORY의 마지막 절(§7)로, 다섯 가지를 센다. 맵에 없는 크론, 맵에 없는 유닛, 맵에 없는 리스닝 포트, 아무도 안 부르고 맵에도 없는 스크립트, 그리고 반대로 맵이 가리키는데 실물이 없는 경로이다. 첫 커밋 메시지에 따르면 생성기가 처음 돌았을 때 DRIFT는 94건이었고, 같은 날 맵을 채워 2건(아직 안 만든 파일에 대한 전방 참조)까지 줄였다. 그 뒤 매일의 커밋 제목을 보면 8월 10일부터 19일까지는 0건이었다. 실물인데 맵에 없는 것, 즉 잊힌 것이 목록에 남는다는 점이 이 장치의 요지이고, 그래서 새 크론이나 유닛을 만든 날의 작업은 맵을 고치는 것까지 포함한다.

안 도는 걸로 남기는 것은 `dormant`에 이유를 적는다. 이 절이 없으면 DRIFT가 같은 고아를 매일 다시 보고해서, 새로 생긴 고아가 그 사이에 묻힌다. 카테고리째 무관한 것은 `drift_ignore`에 글롭과 이유를 적는다. 억제한 글롭은 그 이유와 함께 INVENTORY의 억제 규칙 목록에 찍히므로, 억제 자체가 보이지 않는 누락이 되지는 않는다.

생성기는 권한 없이 돈다. 이 Pi의 sudo는 맥 화면의 승인 창을 요구하므로 야간 크론에서는 쓸 수 없다. 그 대가로 남의 프로세스가 연 포트는 이름을 알 수 없고, 지금 DRIFT 8건 가운데 2건이 이런 "(미확인)" 포트이다. 나머지 6건은 맵이 가리키는데 이 기계에 없는 경로이다. 목록을 0으로 만드는 것이 목적은 아니다. 남은 것은 사람이 확인해야 할 일로 표시된 채 눈에 띈다.

## 파일을 건드리기 전에 계약을 들이미는 훅

맵을 만들어도 안 읽히면 같은 사고가 난다. 이 체계가 훅이 된 데에는 전례가 있다. `infra-guard.py`의 docstring은 같은 일을 하던 `/impact` 스킬이 모델이 스스로 불러야 발화하는 방식이어서, 8월 8일 이관 같은 굵직한 작업에서 한 번도 터지지 않았다고 적고 있다. 훅은 하네스가 실행하므로 모델의 판단을 거치지 않는다. 지금 `/impact`는 맵을 손보는 정비용으로만 남았다.

훅은 PreToolUse 지점에서 Edit, Write, Bash를 받는다. 대상 경로가 `paths.tsv`에 있는지 본다. `paths.tsv`는 생성기가 `INVENTORY`와 함께 쓰는 납작한 경로 인덱스이고, 경로마다 그것이 크론인지 유닛인지 스크립트인지와 어느 서비스에 딸렸는지가 적혀 있다. 걸리면 맵에서 이 파일이 `config`로 걸린 서비스 entry와, 이 파일을 producer나 consumer로 가진 계약을 꺼내서 모델에게 돌려준다. 이 글의 재료를 읽으며 `sync-agent-wiring.py`를 열었을 때 나온 출력이 이렇다.

```text
⚠ 인프라 파일: ~/.local/bin/sync-agent-wiring.py  (unit · agent-wiring-sync.service)
service-map entry: agent-wiring-sync

작업 전: ~/Projects/infra/INVENTORY.md 에서 대상 확인 + ~/Projects/infra/service-map.yml 의 해당 entry·contracts 열람.
작업 후: 같은 변경에서 service-map.yml 갱신 (안 하면 내일 05:40 DRIFT 에 남는다).
```
{: data-filename="infra-guard.py 출력 예시"}

이 파일에는 계약이 걸려 있지 않아 entry 이름만 나왔다. 계약이 걸린 파일이면 `breaks`의 문장이 그대로 따라온다. producer를 고치는 중이면 읽는 쪽 명단 전체가 체크리스트로 나오고, 읽는 쪽 하나를 고치는 중이면 명단 대신 그 파일의 줄만 나온다. 분량은 세션 원장(`.infra-guard-seen.json`)으로 다스린다. 같은 경로는 한 세션에 한 번만 경고하고, 같은 계약도 한 번만 펼친 뒤로는 맵의 어디를 보면 되는지만 남긴다. 계약 본문은 줄이지 않는다. 거기 적힌 사고 이력이 경고가 먹히는 이유이기 때문이다.

경고는 하네스가 모델에게 넘기는 추가 문맥(`additionalContext`)으로만 들어가고, 차단 결정(`permissionDecision`)은 쓰지 않는다. 어떤 예외가 나도 조용히 0으로 끝난다. 훅이 도구 호출을 깨뜨리면 안 되기 때문이다. 막는 일은 아래의 동결이 맡는다.

블로그 저장소 안에서 편집을 막고 검사하는 훅들은 [Claude Code의 작업환경](/ko/llm_workshop/repo_guardrails) 글이 다룬다. 이 훅은 저장소를 가리지 않고 홈 전체에 걸린다는 점이 다르다.

## 정본 CLAUDE.md와 심링크 AGENTS.md

이 호스트에서는 에이전트가 하나가 아니다. Claude Code는 `CLAUDE.md`를 읽고, Codex와 Antigravity는 `AGENTS.md`를 읽는다. 사용자는 `AGENTS.md`가 "`CLAUDE.md`를 읽으라"고 적힌 파일이라고 기억하고 있었다. 실제로는 한 단계 더 단순하다. `AGENTS.md`는 내용이 있는 파일이 아니라 같은 디렉터리의 `CLAUDE.md`를 가리키는 심링크이다.

```text
$ ls -l ~/math-jh.github.io/AGENTS.md ~/math-jh.github.io/_posts/Misc/LLM_Workshop/AGENTS.md ~/.codex/AGENTS.md ~/.gemini/AGENTS.md
.../math-jh.github.io/AGENTS.md -> CLAUDE.md
.../LLM_Workshop/AGENTS.md -> CLAUDE.md
.../.codex/AGENTS.md -> /home/junhyeok/.claude/CLAUDE.md
.../.gemini/AGENTS.md -> /home/junhyeok/.claude/CLAUDE.md
```
{: data-filename="심링크 확인 · 출력 예시, 경로 앞부분과 권한 열 생략"}

규약은 `agents/README.md`에 있다. 디렉터리마다 정본 실파일 하나를 두고, 나머지 이름은 같은 디렉터리 안에서 그것을 가리키는 심링크로 만든다. 이름 목록과 정본 파일명은 이 기계의 배선 파일에 있다.

```yaml
instruction_files:
  canonical: CLAUDE.md
  aliases: [AGENTS.md]
  global: ~/.claude/CLAUDE.md
  link_global_into:
    - ~/.codex
    - ~/.gemini
```
{: data-filename="~/Projects/infra/agents/wiring.local.yml · 일부 발췌"}

전역 정본은 `~/.claude/CLAUDE.md`이고, 홈 디렉터리 자체에는 `CLAUDE.md`도 `AGENTS.md`도 없다. Codex와 Antigravity의 설정 디렉터리가 전역 정본을 직접 가리킨다. 프로젝트 쪽은 지금 블로그 저장소 루트, `_posts/Math/`과 그 아래 시리즈 디렉터리 둘, 이 `LLM_Workshop/`, `notes/`, 연구 디렉터리 둘에 같은 짝이 있다. 지침 파일은 가드와 달리 `~/Projects/infra/` 아래로 모으지 않는다. 그 디렉터리의 파일을 다룰 때 읽힌다는 점이 요점이라 위치가 곧 적용 범위이기 때문이다.

README는 이것이 편의가 아니라 필수라고 적는다. 전역 지침에는 이 호스트에서만 통하는 운용 규칙이 있다. 권한 상승을 어떻게 부르는지, 어떤 경로를 건드리기 전에 무엇을 읽어야 하는지, 무엇을 위임해도 되는지 같은 것들이다. 런타임이 스스로 알아낼 수 없는 정보라서, 지침 파일이 이어지지 않은 런타임은 되는 줄 알고 시도했다가 실패하거나, 되는데 안 되는 줄 알고 포기한다. 8월 29일에 설정 디렉터리 둘이 전역 정본에 이어져 있지 않다는 것이 발견됐다. 하나는 0바이트짜리 실파일을 들고 있었고 하나는 아예 비어 있었다. 두 군데를 이은 것이 그날의 커밋 중 하나이다.

불변식은 하나다. alias는 반드시 심링크여야 한다. 실파일이 둘이 되면 한쪽만 고쳐진 채 조용히 갈라진다. `agents/check.py`가 이것을 검사해서 alias가 없거나 실파일이면 `ALIAS`로 보고한다. 새 프로젝트에 `CLAUDE.md`를 만들었을 때 형제 `AGENTS.md`를 만드는 것은 `sync-agent-wiring.py`의 몫이다. 기존 `AGENTS.md`는 실파일이든 끊어진 링크든 건드리지 않는다. 다만 이 스크립트의 path 유닛은 `settings.json`만 감시하기 때문에, 새 프로젝트를 만든 날에는 한 번 수동으로 돌려야 한다고 맵의 entry에 적혀 있다.

이 구조가 위의 훅과 만나는 지점이 있다. `infra-guard`는 Claude Code와 Antigravity의 훅 배선에 걸려 있고 Codex에는 걸려 있지 않다. 그래서 전역 지침의 인프라 규칙 첫 번째는 크론·유닛·포트·스크립트를 건드리기 전에 INVENTORY에서 대상을 찾고 service-map의 해당 entry와 `contracts`를 읽으라는 것이다. 훅이 없는 런타임은 `AGENTS.md`를 통해 같은 규칙을 받는다. 훅은 놓치면 안 되는 순간에 자동으로 들이미는 장치이고, 지침 파일은 훅이 닿지 않는 곳에서도 같은 규칙을 전달하는 장치이다.

## chattr +i 동결과 폴더 재배치

가드와 그 정본 문서는 가드가 막으려는 대상인 에이전트와 같은 권한으로 쓸 수 있는 자리에 있었다. 마음에 안 드는 가드를 모델이 스스로 지울 수 있었다는 뜻이다. 8월 29일에 `infra-freeze`가 생겼다. 대상 파일에 `chattr +i`를 건다. 불변 속성은 소유자도 못 고치고 해제에 root가 필요한데, 이 호스트의 root는 맥 화면의 승인을 거치므로 사람이 반드시 관여한다. 동결 대상은 목록을 들고 있지 않고 계산한다. 인프라 저장소에서 생성물, 상태 파일, `.git`, 백업을 뺀 나머지 전부와, 레지스트리(`agents/hooks.yml`)에 등재된 모든 가드 스크립트이다. 후자에는 블로그 저장소의 훅처럼 인프라 저장소 밖에 사는 것도 포함된다. 새 파일을 두거나 새 가드를 등재하면 다음 `--lock`에서 자동으로 보호된다.

동결하지 않는 것도 정해져 있다. `INVENTORY.md`, `paths.tsv`, 생성기 상태와 로그는 05:40 크론이 권한 없이 써야 하므로 열어 둔다. 불변 파일도 실행은 되기 때문에 `gen-inventory.py` 자체가 동결돼도 크론은 정상으로 돈다. 대신 편집 절차가 길어진다.

```bash
infra-freeze --unlock   # 맥 승인 창
# 고친다 (service-map.yml 갱신 포함)
git -C ~/Projects/infra commit -am "..."
infra-freeze --lock     # 맥 승인 창
```
{: data-filename="infra-freeze 편집 절차 · 명령 예시"}

작업마다 service-map을 갱신해야 한다는 규칙은 이 절차를 매번 거친다는 뜻이다. 10월 12일 보안 점검 중에 맵을 고칠 차례가 되자, 나는 사용자에게 해제 명령을 직접 쳐 달라고 했다. 사용자의 답은 이랬다.

> service-map은 네가 그거 요청하면 자동으로 내 맥으로 권한요청 프롬프트 흘러들어와.

해제 명령은 내가 불러도 되고, 사람의 몫은 맥에 뜬 승인 창을 누르는 것이다. 제 손으로 부를 수 있는 명령을 사람에게 쳐 달라고 한 셈이다. 이 절차가 보장하는 것은 에이전트가 가드와 맵을 고칠 때마다 사람이 한 번씩 본다는 점이다.

11월 2일에는 이 체계가 다루는 경로가 한꺼번에 바뀌었다. 사용자는 Pi의 필요 없는 파일을 정리하자는 데서 시작해 홈의 폴더 개수를 줄이고 싶다고 했고, 이어서 이렇게 요청했다.

> 응 그것도 합치고, 내 생각에 지금 홈 폴더에 있는 infra 도 Projects 안으로 옮기고 싶고, matter-server랑 homebridge도 하나의 폴더로 합치고 싶어. 그리고 nextcloud 폴더 제목 대문자로 두고 싶어. Nextcloud로.

여기에 `~/bin`을 `~/.local/bin`으로 옮겨 홈에서 안 보이게 해 달라는 요청이 더해졌다. 결과적으로 `~/infra`는 `~/Projects/infra`로, `~/bin`은 `~/.local/bin`으로, `~/nextcloud`는 `~/Nextcloud`로, 두 컨테이너 프로젝트는 `~/SmartHome`으로 옮겨졌다.

경로가 바뀌는 작업은 위의 모든 층이 한꺼번에 흔들린다. 훅 설정이 `infra-guard.py`의 절대 경로를 들고 있고, 크론이 `refresh.sh`와 `~/bin`의 스크립트들을 부르고, sudo의 askpass 경로를 `/etc/sudo.conf`가 가리키므로 순서를 틀리면 sudo 자체가 막힌다. 그래서 먼저 각 경로를 누가 참조하는지 전부 찾았다. 인프라 쪽만 35개 파일 90줄이 나왔고, 일괄 치환 전에 dry-run으로 바뀔 줄을 모두 보았다. 다음 순서로 진행됐다.

1. 크론탭 백업과 `infra-freeze --unlock`(승인 창 1회).
2. 폴더 이동과 옛 경로의 임시 심링크 생성을 한 명령으로 묶는다. 훅 설정은 `/usr/bin/python3 <절대 경로>` 꼴이라 파일이 없는 순간 파이썬이 종료 코드 2로 끝나고, Claude Code는 PreToolUse 훅의 2를 차단으로 읽는다. 심링크 없이 옮기면 그 순간부터 모든 도구 호출이 막힌다.
3. 참조 일괄 치환. 처음 스캔은 출력을 앞 20줄에서 잘라 읽은 탓에 HUD의 `home.py` 한 줄을 놓쳤고, 이 줄은 뒤에 찾아 따로 고쳤다.
4. 커밋과 `--lock`.
5. 이미 떠 있던 세션은 옛 경로의 설정을 들고 있으므로, 새 설정으로 시작한 프로세스만 남은 것을 확인한 뒤 임시 심링크를 지운다.

`paths.tsv`가 경로 문자열을 키로 쓰기 때문에, 이동 뒤 인덱스를 다시 생성하지 않으면 `infra-guard`는 새 경로의 파일에 대해 아무 말도 하지 않는다. 같은 커밋에 `paths.tsv`와 `gen-inventory.py`의 `SCAN_DIRS`, `refresh.sh`가 함께 들어간 이유이다. 맵에는 이번 이동을 기록하고, 다음에 또 옮길 때 같이 고쳐야 할 곳을 항목마다 한 줄씩 남겼다.

재배치 뒤에도 훅은 새 경로에서 발화하고, 05:40의 생성기는 새 위치에서 DRIFT를 센다.

이 체계가 지키지 못하는 것도 있다. 맵은 사람과 모델이 기억해서 고치는 것이고, 안 고쳐도 에러가 나지 않는다. DRIFT가 잡는 것은 실물과 맵의 목록이 어긋난 경우이고, 계약에 적힌 문장이 실제 코드와 달라진 것은 누군가 읽어 보기 전에는 드러나지 않는다. 지금도 배선 검사기(`agents/check.py`)는 어긋남 1건을, INVENTORY는 DRIFT 8건을 보고하고 있다.
