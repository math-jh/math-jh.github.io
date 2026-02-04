---

title: "Raspberry Pi 5에 Openclaw 돌리기"
excerpt: ""

categories: [Misc / Peripherals]
permalink: /ko/misc/peripherals/tools/raspberry_pi
header:
    overlay_image: /assets/images/Misc/Peripherals/Raspberry_Pi.jpeg
    overlay_filter: 0.5

toc: false
date: 2026-02-05
last_modified_at: 2026-02-05
weight: 4

---

일주일 쯤 전부터 `OpenClaw` (당시에는 `ClawdBot`)이 눈에 들어오기 시작했다. 간단히 말하자면 이는 agentic AI의 일종이다. Agentic AI는 작업의 능동성에서 기존의 AI들과 차별화된다. 예를 들어 프로그램을 전혀 모르는 나같은 사람이 AI로 바이브 코딩을 한다고 생각하면, 그 동안은 

1. AI를 통해 코드를 작성함
2. 해당 코드를 적용함.
3. 오류 발생, AI를 활용하여 다시 디버깅
4. 될 때까지 반복

이러한 과정을 수행했어야 한다. Agentic AI는 여기에서 코드를 적용하고, 디버깅을 하는 과정까지 AI가 알아서 수행한다. 즉 그 동안은 AI가 완성된 결과물을 내놓기 전에, 인간이 디버깅을 한다던가, 하다못해 AI가 제시한 코드 혹은 결과물을 복사 붙여넣기하는 것이 인간의 몫이었다면 agentic AI는 이 결과물을 내놓는 것 또한 AI가 진행하는 것이다. `OpenClaw`는 여기에서 더 나아가 이 agentic AI를 개인 PC에 설치한 것이라 생각하면 된다. 

장단점은 명확하다. 기존 AI에 비해서 훨씬 편리한 대신, 보안상의 우려가 매우 크다. 또, `OpenClaw`의 장점 중 하나는 AI의 기억을 마크다운 형태로 저장해서, 기억이 휘발되지 않도록 할 수 있다는 것이다. 가령, 다음 스크린샷은 `OpenClaw`에게, 블로그에 쓸 Raspberry Pi에 `OpenClaw` 설정하는 과정을 안내하는 글의 초안을 부탁했을 때의 반응이다. 

![](/assets/images/Math//Volumes/junhyeok/math-jh.github.io/_posts/Misc/Peripherals/Tools/2026-02-05-Raspberry_Pi.md/Raspberry_Pi-1.png){:style="width:em" class="invert" .align-center}

스크린샷들을 보면, 한 번의 명령으로 다음 과정들을 모두 수행하는 것을 확인할 수 있다. 

1. 블로그 폴더에서 Raspberry Pi 관련 글이 있을 것으로 추정되는 경로를 찾아본다. (내 `OpenClaw` 에이전트는 블로그 구조를 어느정도 알고있다.)
2. Raspberry Pi 관련 글을 찾고, 이 글의 내용을 읽어 그 글에 아무 내용도 없다는 것을 확인했다. 
3. 같은 경로에 `2026-02-05-OpenClaw_Journey.md`라는 제목의 새 파일을 만들어서, 이 파일에 원하는 글의 내용을 적는다. 

해당 파일의 내용은 다음과 같다. 

img

작년 말부터 RPi5를 사용했다던가, 특정 케이스를 샀다던가 하는 사실과 다른 것들이 들어있기는 하지만 대략적으로 글의 구색은 갖춘 것을 확인할 수 있다. 나는 `OpenClaw` 에이전트를 `Kimi-K2.5` 모델로 돌리고 있는데, 더 유려한 글을 쓴다고 평가받는 `Claude` 등등을 썼다면 사정이 조금 나았을 것이다. 

## Raspberry Pi 5

`OpenClaw`는 그 자체로 AI 모델을 탑재한 것이 아니라, 외부 AI 모델의 API를 받아와서 돌리는 플랫폼의 일종이다. 맨 처음의 이름인 `ClawdBot`만 해도 `Claude`를 염두에 둔 이름이다. 그러다가 상표권 문제로 `MoltBot`으로 바뀌었다가, 또 다시 `OpenClaw`로 바뀌었다. 그 이름의 변화만큼이나 기능 변화 등등도 활발하게 이루어지고 있어서, 이 글에서 구체적인 설정 방법을 이야기하는 것은 적절치 못할 것 같고 (당장 내일이면 outdated일지도 모르니...) 간략히 환경 설명과 활용법 공유 정도나 하려 한다. 

나는 원래 `Homebridge`용 Raspberry Pi Zero 2W를 갖고 있었어서, `OpenClaw` 이야기를 듣고 Raspberry Pi에 설치할 생각을 하는 것은 어찌보면 당연한 일이었다. 그러나 Raspberry Pi Zero는 아무래도 사양이 많이 딸려서, Raspberry Pi 5를 새로 구매했다. 여기서 가격 관련 부분을 짚고 넘어가지 않을 수가 없는데, agentic AI는 그 특성 상 API 소모가 아주 많다. 가령 내가 Raspberry Pi에 설치하고, 이것저것 설정한 게 2월 1일부터 2월 3일까지인데, 이 과정에서 API 사용료만 24달러가 넘게 깨졌다. 다행인 것은 `OpenClaw`는 `LM Studio`나 `Ollama` 같은 로컬 LLM도 연동해줄 수 있다는 것인데, 이를 위해서는... 다소 비싼 초기비용이 발생한다. 전력 소모와 성능 등등을 고려한다면 Mac Mini를 `OpenClaw` 전용 서버로 굴리는 것을 생각할 수 있겠지만, 단적으로 내 Mac Mini는 M4, 10코어에 16GB 모델인데 `LM Studio`로 조금 큰 파라미터 (9B정도)를 가진 LLM을 돌리면 RAM 사용량이 100%를 찍는다. 답답하지 않게 쓰려면 RAM 용량도 넉넉하고 저장공간도 뒷받침해주는 성능의 Mac Mini를 새로 구비해야 하는 것이다. 장기적으로 보면 이쪽이 이득일 것은 분명하지만, 내 API 사용량을 찬찬히 뜯어보면 어제, 오늘 쓴 비용은 합쳐서 3달러 정도. 



## 총평

