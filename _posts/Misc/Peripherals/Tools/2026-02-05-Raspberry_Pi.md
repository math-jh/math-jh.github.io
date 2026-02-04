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

작년 말부터 RPi5를 사용했다던가, 특정 케이스를 샀다던가 하는 