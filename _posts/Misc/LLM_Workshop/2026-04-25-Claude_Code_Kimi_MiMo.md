---
title: "Claude Code를 Kimi·MiMo로"
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


Claude Code CLI는 환경 변수 `ANTHROPIC_BASE_URL`만 갈아끼우면 다른 Anthropic-호환 엔드포인트를 향한다. 모델 protocol이 같아서 가능한 일이다. 다만 "한 번 갈아끼우면 끝"이 아니었다. 사용자는 어떤 일은 Claude로, 어떤 일은 Kimi로, 또 어떤 일은 MiMo로 하고 싶어 했다.

> 아니, 만약에 내가 claude 확장을 claudekimi로만 쓴다면 한 번 넣으면 끝이지만, claude 모델도 쓰고 kimi 모델도 쓰려면 계속 왔다갔다 해야 하니까.

그래서 wrapper 명령들을 만들었다. `claude`는 그대로 두고, `claudekimi`와 `claudemimo`를 별도로 추가했다.

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

핵심은 `set -a` / `set +a` 사이에서 env 파일을 소스하는 부분이다. 이 사이에 정의된 변수는 자동으로 export되므로, 그 다음의 `exec claude`에 환경이 그대로 전달된다. subshell이라 쉘 자체의 환경은 오염되지 않는다. 평범한 `claude`를 치면 여전히 Anthropic을 향한다. `claudemimo`도 구조는 거의 같고, 소스하는 env 파일만 `~/.mimo/claude.env`로 바뀐다.

env 파일의 핵심:

```bash
# ~/.kimi/claude.env
ANTHROPIC_BASE_URL="https://api.kimi.com/coding/"
ANTHROPIC_API_KEY="sk-kimi-..."
CLAUDE_CONFIG_DIR="$HOME/.claudekimi"
```

`CLAUDE_CONFIG_DIR`이 중요한데, 이유는 다음 절에서 설명한다.

## Auth conflict

처음 wrapper만 만들어 돌렸더니 다음 경고가 떴다.

> ⚠Auth conflict: Both a token (claude.ai) and an API key (ANTHROPIC_API_KEY) are set. This may lead to unexpected behavior.

기본 `~/.claude/` 디렉토리에는 이미 claude.ai의 OAuth 토큰이 들어 있다. 그런데 `claudekimi`가 그 디렉토리를 그대로 쓰면서 동시에 `ANTHROPIC_API_KEY`를 세팅하니, CLI가 어느 인증을 쓸지 결정하지 못한다.

해결은 `CLAUDE_CONFIG_DIR="$HOME/.claudekimi"` — wrapper마다 독립된 설정 디렉토리를 갖게 했다. `~/.claudekimi/`에는 claude.ai 토큰이 없으니 충돌이 사라지고, settings/sessions/MCP도 깔끔히 분리된다. `claudemimo` 역시 `~/.claudemimo/`를 별도로 쓴다.

> 잠깐, 혹시 가능하다면 ~/.kimi/ 아래의 설정들을 참고해서, ~/.claudekimi/ 디렉토리를 새로 만들어서 설정, 세션, MCP 분리를 진행해도 좋아.

CLI 쪽은 이것으로 일단락됐다. 다만 사용자는 보통 VS Code Remote에서 작업하고, VS Code Claude 확장이 별도로 존재하기 때문에 작업이 거기서 끝나지 않는다.

## VS Code 확장 포크

공식 `anthropic.claude-code` 확장은 `claude` 명령을 직접 호출한다. 같은 확장이 `claudekimi`를 호출하게 만들려면 패키징된 확장을 포크해서 호출 명령과 표시 이름을 바꿔야 한다.

> 그리고 그 VS code 확장 보면, 원래 VS code 위쪽에 "Claude Code: Open" 버튼이 있는데, 포크한 친구는 이걸 Claude Code (Kimi) 정도로 가져야 할 것 같아. 그렇게 해 줄 수 있어?

`package.json`을 풀어 `name`, `displayName`, command id들을 갈아끼우고 호출 binary를 `claudekimi`로 교체한 뒤, `vsce package`로 다시 묶어 sideload했다. 그렇게 만들어진 것이 `local.claude-code-kimi-2.1.145-linux-arm64`다. MiMo도 같은 절차로 `local.claude-code-mimo-2.1.145-linux-arm64`를 만들었다. CLI에서 인증이 정상 작동한 뒤에도 VS Code 측 인증 경로가 따로 잡혔는데, 확장이 자체적으로 `~/.claude/`를 들여다보고 있어서였다. 확장 코드 안의 그 참조도 환경 변수 기반으로 바꿔야 했다.

> 그 우리 아까전에 CLI 툴의 경우 ~/.claudekimi로 설정 옮겼잖아? 확장도 그거 기반으로 돌리면 좋겠어.

CLI에서 환경 변수를 갈아주는 일이 7줄이었다면, VS Code 확장 fork는 그 몇 배가 들었다. packaging된 binary와 manifest를 풀고, 해당 위치를 고치고, 다시 묶고, sideload하고, 재인증 흐름을 검증하는 단계가 이어졌다.

## 아이콘 색

VS Code 상단의 "Claude Code: Open" 버튼에는 아이콘이 있다. 두 포크가 같은 아이콘을 쓰면 구분이 안 되므로, 각자의 아이콘도 새로 만들어야 했다. 여기서부터는 코드가 아니라 이미지 작업이다.

기본 패턴(C 글자에 구멍을 뚫고 그 안에 다른 글자를 끼워넣는 방식)이 정해진 뒤, 색상과 글자 모양 조정이 이어졌다.

> F로 하고 K 위치 약간만 조정, 살짝 왼쪽 밑으로, 색 더 진한 파랑으로

> K 살짝 오른쪽으로, 그리고 K 문자의 사이즈는 유지한 채로 원형으로 판 것만 키워줘.

> 좋아, 근데 K 문자는 그대로 두고, 구멍만 오른쪽으로 옮길 수는 없지?

> 마지막으로, 아이콘 주변 여백만 좀 작게 해 주면 좋겠어.

> Margin 좀만 더 줄여줄 수 있어?

그다음은 색 조정이었다. Kimi 쪽 색상은 다음 순서로 바뀌었다.

`#052D69` → `#033b91` → `#4770d2` → `#4880d2` → ("원래대로 롤백하자") → `#3c57a3`.

MiMo 쪽은 `#FF4301` → `#F37333` → `#FF6700` ("클로드 색이랑 너무 가까울까?") → 안정점으로 돌아왔다. 사용자의 지시가 올 때마다 새 PNG를 익스포트해 확장에 다시 추가했다. 이런 작업은 한 번에 끝나지 않고, 결과를 본 뒤 다음 조정이 정해지는 식으로 반복됐다.

## 결과

CLI에서는 `claude`, `claudekimi`, `claudemimo` 세 명령이 각자 다른 백엔드로 향한다. 설정 디렉토리는 `~/.claude`, `~/.claudekimi`, `~/.claudemimo`로 분리되어 인증이 섞이지 않는다. VS Code Remote에서는 세 확장이 별도로 깔려있고, 상단 버튼 세 개가 각자의 색 아이콘으로 구별된다.

ANTHROPIC_BASE_URL 한 줄로 다른 모델을 부를 수 있다는 것은 일의 시작이었지 끝이 아니었다. 인증 격리, 설정 분리, VS Code 확장 포크, 아이콘 미세조정 — 한 가지를 끝내면 다음 일이 따라왔다. 다 끝났다 싶으면 또 하나가 온다. 대체로 일은 그런 식으로 도착한다.
