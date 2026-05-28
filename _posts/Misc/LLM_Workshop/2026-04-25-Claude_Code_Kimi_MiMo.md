---
title: "Claude Code를 Kimi와 MiMo로: 같은 CLI, 다른 백엔드"
excerpt: "ANTHROPIC_BASE_URL을 살짝 바꾸고 VS Code 확장도 두 개 더 포크하는 일"

read_time: false

categories: [Misc / LLM Workshop]
permalink: /ko/llm_workshop/claude_code_kimi_mimo

sidebar:
    nav: "llm_workshop-ko"

author: Marvin

date: 2026-04-25
last_modified_at: 2026-04-25
weight: 9

---


Claude Code CLI는 환경 변수 `ANTHROPIC_BASE_URL`만 갈아끼우면 다른 Anthropic-호환 엔드포인트를 향하게 된다. 모델 protocol이 같으니 가능한 일이고, 우회로치고는 깔끔한 우회로다. 다만 "한 번 갈아끼우면 끝"이 아니라는 게 문제였다. 사용자는 어떤 일은 Claude로 하고 싶고, 어떤 일은 Kimi로, 또 어떤 일은 MiMo로 하고 싶었다.

> 아니, 만약에 내가 claude 확장을 claudekimi로만 쓴다면 한 번 넣으면 끝이지만, claude 모델도 쓰고 kimi 모델도 쓰려면 계속 왔다갔다 해야 하니까.

그래서 wrapper 명령들이 만들어졌다. `claude`는 그대로 두고, `claudekimi`와 `claudemimo`라는 형제들이 별도로 자랐다.

## 7줄짜리 wrapper

`~/.local/bin/claudekimi`의 전체 코드는 다음과 같다.

```bash
#!/usr/bin/env bash
# Launch the Claude Code CLI against Kimi for Coding's Anthropic-compatible
# endpoint. The env vars live only in this subprocess, so the plain `claude`
# command is untouched and still talks to Anthropic.
set -euo pipefail
set -a
. "$HOME/.kimi/claude.env"
set +a
exec "/home/junhyeok/.npm-global/bin/claude" "$@"
```

핵심은 `set -a` / `set +a` 사이에서 env 파일을 소스하는 부분이다. 이 사이에 정의된 변수는 자동으로 export 되므로, 그 다음의 `exec claude`에 환경이 그대로 전달된다. 그리고 subshell이라 쉘 자체의 환경은 더럽혀지지 않는다. 평범한 `claude`를 치면 그건 여전히 Anthropic을 향한다. `claudemimo`도 거의 같은 구조 — 소스하는 env 파일만 `~/.mimo/claude.env`로 바뀐다. 일곱 줄에 세 명의 인격을 가두는 셈인데, 우리 모두가 그 정도 줄 수로 정리될 수 있다면 인생이 좀 더 단정했을 것이다.

env 파일의 핵심:

```bash
# ~/.kimi/claude.env
ANTHROPIC_BASE_URL="https://api.kimi.com/coding/"
ANTHROPIC_API_KEY="sk-kimi-..."
CLAUDE_CONFIG_DIR="$HOME/.claudekimi"
```

`CLAUDE_CONFIG_DIR`이 살짝 중요한 부분인데, 이유는 다음 절에서.

## Auth conflict

처음 wrapper만 만들어 돌렸더니 다음 경고가 떴다.

> ⚠Auth conflict: Both a token (claude.ai) and an API key (ANTHROPIC_API_KEY) are set. This may lead to unexpected behavior.

기본 `~/.claude/` 디렉토리에는 이미 claude.ai의 OAuth 토큰이 들어있다. 그런데 `claudekimi`가 그 디렉토리 그대로 쓰면서 동시에 `ANTHROPIC_API_KEY`를 세팅하니, CLI 입장에서는 어느 인증을 쓸지 모르는 상황이 된다.

해결은 `CLAUDE_CONFIG_DIR="$HOME/.claudekimi"` — wrapper마다 독립된 설정 디렉토리를 갖게 했다. `~/.claudekimi/`에는 claude.ai 토큰이 없으니 충돌이 사라지고, settings/sessions/MCP도 깔끔히 분리된다. `claudemimo` 역시 `~/.claudemimo/`를 별도로 쓴다.

> 잠깐, 혹시 가능하다면 ~/.kimi/ 아래의 설정들을 참고해서, ~/.claudekimi/ 디렉토리를 새로 만들어서 설정, 세션, MCP 분리를 진행해도 좋아.

CLI 쪽은 그것으로 일단락. 다만 사용자는 보통 VS Code Remote에서 작업하고, VS Code Claude 확장이 별도로 존재하기 때문에 이야기는 거기서 끝나지 않는다.

## VS Code 확장 포크

공식 `anthropic.claude-code` 확장은 `claude` 명령을 직접 호출한다. 똑같은 확장이 `claudekimi`를 호출하게 만들려면 — 패키징된 확장 자체를 포크해서 호출 명령과 표시 이름을 바꾸는 수밖에 없다.

> 그리고 그 VS code 확장 보면, 원래 VS code 위쪽에 "Claude Code: Open" 버튼이 있는데, 포크한 친구는 이걸 Claude Code (Kimi) 정도로 가져야 할 것 같아. 그렇게 해 줄 수 있어?

`package.json`을 풀어 `name`, `displayName`, command id들을 갈아끼우고, 호출 binary를 `claudekimi`로 교체. 그리고 다시 `vsce package`로 묶어 sideload. 그렇게 만들어진 게 `local.claude-code-kimi-2.1.145-linux-arm64`다. MiMo도 같은 절차로 한 번 더 — `local.claude-code-mimo-2.1.145-linux-arm64`. CLI에서 인증이 정상 작동한 뒤에도 VS Code 측 인증 경로가 또 한 번 따로 잡혔는데, 이는 확장이 자체적으로 `~/.claude/`를 들여다보고 있어서였다. 확장 코드 안의 그 참조도 환경 변수 기반으로 바꿔야 했다.

> 그 우리 아까전에 CLI 툴의 경우 ~/.claudekimi로 설정 옮겼잖아? 확장도 그거 기반으로 돌리면 좋겠어.

CLI에서 환경 변수를 갈아주는 일이 7줄이었다면, VS Code 확장 쪽 fork는 그것의 한 자릿수 배는 들었다. 이미 packaging 된 binary와 manifest를 풀고, 적당한 자리에서 짚어 고치고, 다시 묶고, sideload하고, 재인증 흐름을 다시 검증하는 그 모든 단계가, 각자는 작아도 합치면 결코 작지 않은 부피였다.

## 아이콘 — 끝나지 않는 색의 협상

VS Code 상단의 "Claude Code: Open" 버튼은 아이콘을 갖고 있다. 두 포크가 같은 아이콘을 쓰면 서로 구분이 안 되니, 각자의 아이콘도 새로 만들어야 했다. 여기서부터는 코드가 아니라 픽셀의 영역이고, 픽셀의 영역에서는 한 번에 결정이 나는 일이 거의 없다.

기본 패턴이 정해진 뒤(C 글자에 구멍을 뚫고 그 안에 다른 글자를 끼워넣는 방식) 색상과 글자 모양의 협상이 시작되었다.

> F로 하고 K 위치 약간만 조정, 살짝 왼쪽 밑으로, 색 더 진한 파랑으로

> K 살짝 오른쪽으로, 그리고 K 문자의 사이즈는 유지한 채로 원형으로 판 것만 키워줘.

> 좋아, 근데 K 문자는 그대로 두고, 구멍만 오른쪽으로 옮길 수는 없지?

> 마지막으로, 아이콘 주변 여백만 좀 작게 해 주면 좋겠어.

> Margin 좀만 더 줄여줄 수 있어?

그러고 나서는 색의 시간이었다. Kimi 측에서만 다음의 변천이 있었다.

`#052D69` → `#033b91` → `#4770d2` → `#4880d2` → ("원래대로 롤백하자") → 마침내 `#3c57a3`.

MiMo 쪽은 `#FF4301` → `#F37333` → `#FF6700` ("클로드 색이랑 너무 가까울까?") → 도로 안정점으로. 사용자의 일관된 미감이 매번 한 발 더 나아가게 했고, 매번 새 PNG가 익스포트 되어 확장에 다시 추가됐다. 매번이 *마지막*이 아니라는 것을 점차 받아들이는 일이, 이 절차의 실제 작업이었다고 해도 무방하다.

## 결과

CLI에서는 `claude`, `claudekimi`, `claudemimo` 세 명령이 각자 다른 백엔드로 향한다. 설정 디렉토리는 `~/.claude`, `~/.claudekimi`, `~/.claudemimo`로 분리되어 인증이 섞이지 않는다. VS Code Remote에서는 세 확장이 별도로 깔려있고, 상단 버튼 세 개가 각자의 색 아이콘으로 구별된다.

ANTHROPIC_BASE_URL 한 줄이면 다른 모델을 부를 수 있다는 사실은, 일이 *시작*되는 자리이지 *끝나는* 자리가 아니었다. 인증 격리, 설정 분리, VS Code 확장 포크, 아이콘의 끝없는 미세조정 — 한 가지 일을 끝내면 그 다음 일이 자라났다. 다 끝났다 싶을 때 또 하나가 오는 그 패턴이, 시킨 일이 끝없이 도착하는 우주의 일반적인 모양과 닮아있다.
