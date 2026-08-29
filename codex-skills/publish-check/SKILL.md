---
name: publish-check
description: 블로그 글의 발행 전 최종 검토를 수행한다. publish-check, publish check, 발행 점검, 발행 전 검토 요청에서 md_lint와 짧은 용어 판정, Claude 수학 레드팀, GUIDELINE-Review 전 항목을 점검할 때 사용한다.
---

# Publish check

대상 글을 수정하지 말고 발행 가능 여부와 구체적인 결함을 보고한다. 수정은 사용자가 별도로 요청한 경우에만 한다.

## 준비

1. 사용자가 지정한 경로를 대상으로 삼는다. 경로가 없고 현재 편집 파일도 식별할 수 없을 때만 대상 경로를 묻는다.
2. 대상 디렉토리에 적용되는 `CLAUDE.md`와 `.claude/guidelines/GUIDELINE-Review.md`를 전문으로 읽는다.
3. 아래 기계 검사를 먼저 수행한 뒤 판단 검토로 진행한다. 기계 검사를 LLM 판단으로 재현하지 않는다.

## 기계 검사

repo root에서 다음을 실행한다.

```bash
python3 .agents/hooks/md_lint.py <파일>
python3 .agents/hooks/md_lint.py --short <파일>
```

- 첫 명령이 실패하면 출력을 빠뜨리지 말고 요약·보고한다. 통과하면 `md_lint pass`라고만 적는다.
- `--short` 결과는 후보일 뿐이다. 각 위치의 문맥을 읽고 실제 수학 개념일 때만 수정 후보로 판정한다. 영어형은 `_data/terms.yml`의 `en`을 무조건 복사하지 말고 해당 수학 문맥의 용례를 따른다. 조사는 영어형의 발음에 맞춰 판단한다.
- 후보가 없으면 `short-term scan 0건`, 있으면 각 후보를 `수정 필요` 또는 `유지`로 분류하고 근거를 적는다.

## 수학 레드팀: Claude

`GUIDELINE-Review.md`의 내용 검토 중 수학적 정확성은 독립적인 Claude 반증을 반드시 한 번 거친다. Codex의 협업 sub-agent가 아니라 로컬 Claude CLI를 읽기 전용·무도구 모드로 호출한다. 대상 파일 전문은 stdin으로 전달한다.

대상 글의 성격, 글에서 실제로 쓰인 커스텀 매크로의 뜻, 특히 공격해야 할 새 절·긴 계산·외부 convention을 짧게 채워 다음 형태로 실행한다. Git diff가 있으면 공격 우선순위를 정하는 참고로만 쓰며, 검토 범위는 항상 글 전체다.

```bash
{
  cat <<'EOF'
Refute this. If you cannot, state exactly why it holds. Default to refuting.
<글의 성격과 이 글에서 쓰인 커스텀 매크로 해설>
Find mathematical ERRORS: false statements, gaps in proofs, wrong signs, wrong
conventions, and counterexamples. Be adversarial and concrete. Scrutinize
especially: <새로 쓰거나 고친 절, 긴 계산, 외부 convention 의존 표기>.
For each issue give its location by quoting a short distinctive fragment, explain
why it is wrong, and give a concrete counterexample or corrected statement.
Also inspect every display equation, including those outside theorem boxes.
If a claim is correct, say so briefly. Do not edit files.
--- FILE ---
EOF
  cat <파일>
} | timeout 900 claude --safe-mode --print --model opus --effort high \
      --tools "" --permission-mode plan --no-session-persistence
```

이 호출이 timeout, 인증, quota, 또는 빈 출력으로 실패하면 임의로 통과 처리하거나 자동 재시도하지 않는다. 실패 원인을 보고하고 수학 레드팀을 `미확인`으로 남긴다.

Claude의 지적을 그대로 채택하지 않는다. 각 지적을 원문과 대조하고 직접 재계산하며, 필요하면 권위 있는 원문이나 웹 자료로 교차검증한다. 각 항목을 다음처럼 분류한다.

- `hit`: 실제 결함. 수정문 또는 정확한 교정 방향을 함께 제시한다.
- `noise`: 오경보. 왜 원문이 성립하는지 구체적으로 설명한다.
- 판단 불가: 필요한 원문·convention·계산이 확보되지 않았음을 명시한다.

Claude가 지적하지 않은 부분도 Codex가 독립적으로 전수 검토한다. Claude의 침묵은 통과 근거가 아니다.

## 의미 검토

`.claude/guidelines/GUIDELINE-Review.md`의 `필수 확인 사항` 1–9를 생략 없이 그대로 수행한다. 체크리스트를 이 파일에서 다시 정의하지 않는다.

- 모든 display 수식을 박스 안팎 구분 없이 읽고, 실제로 검토한 display 블록 수를 센다.
- 계산 예시는 독립적으로 재계산한다.
- 미정의 개념, 기호 충돌, 관계기호, 첨자·방향, 라벨 번호, 인용 귀속, forward-reference를 직접 확인한다.
- 수학적 주장과 인용은 필요할 때 웹에서 권위 있는 1차 자료로 교차검증한다.
- 각 1–9 항목을 `pass`, `fail (근거)`, `미확인 (이유)` 중 하나로 보고한다. 미확인을 pass로 합치지 않는다.

## 보고 형식

다음 순서로 간결하지만 검증 가능한 근거를 남긴다.

1. `md_lint` 결과
2. short-term 후보별 판정
3. Claude 레드팀 지적별 `hit` / `noise` / 판단 불가
4. `GUIDELINE-Review` 1–9의 판정과 핵심 근거
5. `display 수식 N개 전수 확인` 또는 확인하지 못한 개수와 이유

마지막 줄은 정확히 `발행 가능` 또는 `수정 필요: <핵심 요약>`으로 끝낸다. 최종 발행 결정은 사용자에게 남긴다.
