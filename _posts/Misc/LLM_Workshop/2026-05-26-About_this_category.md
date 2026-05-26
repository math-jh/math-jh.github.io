---

title: "LLM Workshop 카테고리"
excerpt: ""

categories: [Misc / LLM Workshop]
permalink: /ko/llm_workshop/about_this_category

toc: false
date: 2026-05-26
last_modified_at: 2026-05-26
weight: 2

---

[Raspberry Pi 5에 OpenClaw 돌리기](/ko/llm_workshop/raspberry_pi) 글을 쓴 지 네 달이 되어가는데, 그 사이에 이런저런 재미있는 일들 (AI 사용 측면에서)이 많이 있었다. 

우선 그 사이에 굵직한 LLM 모델들이 꽤 나왔다. OpenClaw로 처음 agentic AI를 경험할 때만 해도 Kimi-K2.5를 썼는데, 그 후 GLM-5를 쓰고, DeepSeek 4도 나오고, Claude도 업데이트 되고 등등... 현재는 Kimi K2.6, Claude, MiMo 2.5를 주력으로 사용하고 있고, 성능이 필요한 일들은 Claude, 적당한 성능과 적당한 가성비가 필요한 일은 Kimi K2.6, MiMo는 토큰 떨어졌을 때 백업용으로 사용하고 있다.

그 동안 썼던 LLM에 대한 간략한 평가를 하자면, 

- GLM-5, GLM-5.1: GLM Coding Plan으로 썼었는데, 솔직히 말하자면 오픈소스 모델들 중에는 제일 성능이 마음에 들었다. 다소 느리기는 한데, 한글 처리도 잘 하고 OpenClaw에서 쓸 시 페르소나 놀이도 꽤 잘 해줬다. 여기서 바꾸게 된 이유는 모델 성능 외적인 게 제일 큰데, (1) 우선 coding plan에서 OpenClaw 사용시, 피크타임에 속도 제한한 것. 간단한 workaround가 있긴 했지만 (LiteLLM으로 프록시) 꽤나 괘씸했다. (2) Coding plan 가격 인상. 사실 이게 제일 큰데, 가격이 두 배로 뛰어서 거의 Claude Max 급이다. 물론 토큰 사용량은 훨씬 널널하지만 굳이? 그 가격에? 그럴거면 Claude를 쓰지? 싶은 게 제일 컸다. 거기다가 내가 결제 카드를 바꿨는데, 그 과정에서 결제오류가 나서 문의했더니 두 배 오른 가격으로 결제하라는 안내를 받아서 미련없이 해지하고 갈아탔다.
- Kimi K2.6: GLM 다음으로 넘어온 선택지 중 하나였는데, 일단 성능 자체는 overthinking이 굉장히 심한 것을 제외하면 평이하다. 토큰 출력 속도도 GLM보다는 낫지만 overthinking으로 갉아먹는 경향이 강하다. 문제는 블로그 작업 보조용으로 쓸 때 발생했는데, 한글 문서 학습을 덜 했는지 자꾸 한글이 깨진다. 문제는 예를 들어서 Edit 툴을 쓰는 과정에서, old string에 잘못된 한글을 넣는 바람에 Edit 툴이 실패하고, 그걸 보면서도 계속 똑같은 시도를 하는 일이 반복되었다. 가령 "같은"이라는 단어를 "갍은" 같이 이상한 단어로 잘못 쓴 후, Edit tool의 old string에 "갍은"을 쓰고, 