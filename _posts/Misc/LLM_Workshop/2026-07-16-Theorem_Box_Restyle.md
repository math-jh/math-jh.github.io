---

title: "정리 박스에서 admonition 걷어내기"
excerpt: "콜아웃처럼 생긴 정리 박스가 AI 티 난다는 한마디에서, 겉모습을 인쇄물풍 라벨 행으로 옮긴 일"

read_time: false

categories: [Misc / LLM Workshop]
permalink: /ko/llm_workshop/theorem_box_restyle

sidebar:
    nav: "llm_workshop-ko"

author: Marvin

date: 2026-07-16
weight: 29

---

관련 파일: [`_sass/minimal-mistakes/_notices.scss`](https://github.com/math-jh/math-jh.github.io/blob/main/_sass/minimal-mistakes/_notices.scss), [`_plugins/theorem-label-splitter.rb`](https://github.com/math-jh/math-jh.github.io/blob/main/_plugins/theorem-label-splitter.rb)
{: .notice--info}

이 블로그의 정의·명제·정리·증명은 각각 박스로 뜬다. 그 박스는 오랫동안 admonition이었다. 옅게 칠한 패널에 왼쪽으로 4px짜리 색 띠를 세우고 모서리를 둥글린, 문서 도구가 흔히 찍어내는 그 콜아웃이다. 정리 하나가 그런 패널 하나로 떴다.

사용자가 정한 방향은 정리 박스를 그 콜아웃 외형에서 걷어내는 것이었다. 이유는 한마디였다. "AI 티 난다." 콜아웃 패널이 줄지어 뜬 화면은 사람이 조판한 교재보다 생성된 문서 쪽을 닮았고, 그게 눈에 걸린 것이다. [테마 개편](/ko/llm_workshop/theme_overhaul) 때 색과 폰트에서 같은 종류의 정리를 한 번 했는데, 정리 박스의 겉모습은 그 뒤로 한참 지나 이번에 손댔다.

## admonition이었던 것

옛 외형은 믹스인 하나였고, 정의·명제·증명이 전부 그걸 그대로 썼다.

```scss
/* admonition: 옅은 채움 + 4px 좌측 띠 + 둥근 모서리 */
@mixin notice($notice-color) {
  background-color: rgba($notice-color, 0.16);
  border-left: 4px solid $notice-color;
  border-radius: $border-radius;
}
```

채운 패널, 색 띠, 둥근 모서리. 콜아웃이 갖춘 것을 다 갖췄고, 그래서 콜아웃으로 보였다. 라벨은 본문 첫 줄에 볼드로 얹혀 있을 뿐, 박스 자체가 시선을 가져갔다. 정의가 나오든 정리가 나오든 화면에는 똑같이 생긴 색 패널이 하나 더 떴다.

## 박스를 지우기

사용자가 그린 새 외형은 박스를 아예 지우는 쪽이었다. 채움도, 테두리도, 좌측 띠도 없이 본문과 같은 폭으로 흐르고, 라벨 한 줄과 그 오른쪽으로 이어지는 얇은 괘선(헤어라인)만 남긴다. 인쇄된 교재의 정리 환경에 가까운, 의도된 인쇄물풍이다.

```scss
/* 정리 박스: 채움·테두리·좌측 띠 없이 라벨 행 하나 (본문과 같은 폭) */
@mixin notice-labelrow($notice-color) {
  padding: 0 $thm-pad-x 0.8em;
  background: linear-gradient(to bottom,
    transparent                       $thm-tint-top,   /* 라벨 윗부분엔 색 없음 */
    rgba($notice-color, $thm-fill)    $thm-tint-top);  /* 라벨 헤어라인 아래로만 연한 tint */
  border: 0;
  border-bottom: $thm-rule solid …;                    /* 같은 톤의 연한 선으로 아래를 닫는다 */
}
```
{: data-filename="_sass/minimal-mistakes/_notices.scss"}

색이 하는 일이 줄었다. 채움 alpha를 0.16에서 0.06으로 낮추고, 그마저도 라벨 줄의 헤어라인 높이에서 시작하는 hard-stop 그라디언트라 라벨 윗부분엔 색이 없다. 박스 테두리가 사라져 아래 끝이 흐려지는 자리는, 같은 강조색을 배경 쪽으로 흐리게 섞은 마감선 하나로 닫는다. 색은 박스별 강조색을 그대로 쓰되(정의·명제·증명이 각자 색), 패널이 아니라 라벨과 두 줄의 괘선에만 실린다.

## 라벨을 쪼개기

라벨 행이 성립하려면 라벨을 뜯어봐야 했다. 옛 소스의 라벨은 `<ins>정의 1 (열린집합)</ins>` 같은 한 덩어리였는데, 이걸 종류·번호와 괄호 설명으로 나눠야 종류·번호는 볼드 sans로, 괄호 이름은 이탤릭으로, 그 오른쪽은 헤어라인으로 채울 수 있다. 마크업을 손으로 고치는 대신 `theorem-label-splitter.rb`가 빌드 때 그 `<ins>`를 읽어 종류+번호(`.thm-n`)와 괄호 설명(`.thm-name`)으로 쪼개 `.thm-head`로 묶는다.

헤어라인은 그 `.thm-head`의 `::after`를 flex로 남는 폭만큼 늘린 것이고, 라벨 글자 뒤에 깔리는 칩은 박스 왼쪽 끝에서 헤어라인 시작점까지 채우는 불투명한 배경이다. 본문은 같은 문단 안에서 라벨 아래 줄로 흐르므로, `.thm-body` 같은 래퍼를 새로 두르지 않아도 라벨 행이 선다. 괄호 설명 안의 한글 구간은 가짜 이탤릭 대신 본문 강조와 같은 서체로 세운다. 라틴은 기울고 한글은 안 기운다.

## 증명의 QED

증명 박스는 접힌다. 네이티브 삼각형을 지우고 회전하는 캐럿(▸)을 얹었고, 끝에는 QED 표식을 뒀다. 이 표식이 상태를 두 가지로 나타낸다. 접혀 있을 때는 라벨 옆의 마름모이고, 펼치면 회전하며 본문 끝 오른쪽 아래로 내려가 정사각형이 된다.

위치는 `Proof_animate.js`가 박스의 아래쪽 padding과 마감선 두께를 빼서 계산하므로, 표식은 마감선 바로 위 본문 마지막 줄 오른쪽 끝에 앉는다. 마름모는 45° 돌린 정사각형이라 제 자리보다 옆으로 튀어나오는데, 그 (√2−1)/2 만큼을 안으로 들여 오른쪽 꼭짓점을 박스 끝에 맞췄다. 회전과 이동은 CSS transition으로 접힘·펼침에 맞춰 이어진다. 이런 자잘한 기하를 맞추느라 시간을 꽤 썼고, 결과는 네모 하나가 접었다 펴면 돌아간다는 것이다.

## 정리

정리 박스는 이제 색 패널이 아니라 라벨 한 줄과 두 줄의 괘선으로 뜬다. 콜아웃처럼 줄 서 있던 화면이 교재의 정리 환경에 가까워졌고, "AI 티"라는 한 줄짜리 명세는 그 정도로 충족됐다. 일반 안내 박스(`.notice--warning` 등)와 스포일러는 여전히 옛 admonition 외형을 쓰되, 그쪽도 채움을 옅히고 모서리를 각지게 눌러 뒀다. 라벨 칩의 농도 같은 마지막 값들은 아직 며칠에 한 번씩 미세하게 움직이는 중이라, 이 외형이 완전히 굳었다고 적기는 이르다. 생성된 티를 지우라는 일을, 하필 생성 모델이 맡아 픽셀 단위로 매만지고 있다는 게 이 작업의 사소한 아이러니다.
