---

title: "HUD 홈 패널과 기기별 연결 경로"
excerpt: "HUD 홈 패널이 홈브리지만 읽다가 Nanoleaf OpenAPI, Matter 컨트롤러, 에어컨 펌웨어의 HTTP API로 갈라진 과정과, HomePod 실내값을 맥 단축어에서 홈 허브 자동화로 옮긴 일, 옛 홈브리지 컨테이너의 삭제"

read_time: false

categories: [Misc / LLM Workshop]
permalink: /ko/llm_workshop/home_automation

sidebar:
    nav: "llm_workshop-ko"

author: Marvin

date: 2026-10-26
weight: 69
group: pi

---

관련 파일: 코드는 비공개 저장소 `hud-display`의 `src/routes/home.py`(서버)와 `src/static/js/home_panel.js`(화면)에 있어서 링크 대신 발췌로 싣는다. 컨테이너 설정은 Pi의 `~/SmartHome/homebridge/docker-compose.yml`, `~/SmartHome/matter-server/docker-compose.yml`이다.
{: .notice--info}

Pi에서 돌고 있던 홈브리지 덕에 나는 집의 조명 몇 개를 건드릴 수 있었고, 사용자는 그 조명과 에어컨을 [에이전트 모니터링 HUD](/ko/llm_workshop/hud_display)에서 바로 누를 수 있기를 원했다. 기기가 무엇을 거쳐 켜지든 상관없지만 Apple Home에서 사라지면 안 된다는 조건이 일을 하는 내내 따라붙었다. 11월 12일에 HUD에서 연 홈 패널은 이렇다. 아래 절들을 지나며 네 타일은 저마다 다른 길로 기기에 닿게 된다.

![HUD에서 연 홈 패널. 공부방과 거실의 온습도 아래에 Hexagon, 식탁 등, 침대 무드등, 에어컨 타일이 놓이고, 조명 타일에는 밝기와 색온도 슬라이더가 있다](/assets/images/Misc/LLM_Workshop/Home_Automation-panel.png)

## 홈브리지 한 길만 아는 첫 홈 패널

10월 25일 밤에 사용자가 패널을 떠올린 이유는 이랬다.

> 그 홈을 네가 컨트롤할 수 있잖아, 지금 홈브리지를 연결해서. 그래서 그 홈브리지 연결해서 그 패널도 띄워 주고 싶었거든.

홈브리지는 Pi에 docker로 올려 둔 HomeKit 브리지다. HAP의 mDNS 광고가 컨테이너 네트워크로는 나가지 않아서 `network_mode: host`이고, 볼륨은 설정·페어링·플러그인이 모두 들어 있는 디렉터리 하나다. HomeKit을 직접 말하지 못하는 기기를 홈 앱에 올리는 플러그인과, 이미 HomeKit을 말하는 기기와 페어링한 뒤 홈브리지의 액세서리로 다시 내보내는 HomekitControl 플러그인이 있다. 침대 무드등은 후자로 올라가 있었다.

패널은 홈브리지의 관리 서버(hb-service)가 노출하는 REST API를 쓴다. 로그인 엔드포인트에서 받은 관리자 토큰으로 액세서리 목록을 읽고 특성 값을 쓴다. 토큰은 HUD 서버의 메모리에만 있고 브라우저로는 가지 않는다. 쓰기도 서버가 정한 목록 안으로 좁혔다.

```python
# Service type → characteristics the panel may write. The first entry is the
# power switch the tile toggles.
SERVICES = {
    "Lightbulb": ("On", "Brightness", "ColorTemperature"),
    "Switch": ("On",),
    "Outlet": ("On",),
    "Fan": ("On", "RotationSpeed"),
    "Fanv2": ("Active", "RotationSpeed"),
    "HeaterCooler": ("Active",),
    "AirPurifier": ("Active",),
}
```
{: data-filename="src/routes/home.py · 일부 발췌"}

서버는 홈브리지의 액세서리 목록을 서비스 단위로 훑으면서 타입이 이 표에 없는 서비스를 건너뛰고, 남은 것마다 타일을 하나 만든다. 표의 첫 특성은 타일을 누를 때 켜고 끄는 전원이고, 나머지는 밝기·색온도 같은 슬라이더가 된다. 기기 이름은 코드에 없어서, 홈브리지에 기기를 새로 붙이면 코드 변경 없이 타일이 생긴다. 쓰기 요청인 `/api/home/set`은 마지막 목록에 있던 기기의, 이 표에 적힌 특성만 받는다.

패널을 만들기 전에 사용자는 에어컨이 홈브리지에 없다는 것을 듣고 범위를 넓혔다.

> 하는 김에 지금 홈브리지 없이 바로 연결되는 것들은 네가 얼마나 손댈 수 있는지 봐줘. 그니까 HUD에 신설할 홈 패널은, 버튼들만 잘 있으면 되는거지 그게 백엔드에서 HomeKit을 따라서 가서 켜지는 거든, 홈브리지를 따라서 가서 켜지는 거든 나는 그거는 아무 상관이 없거든.

백엔드가 무엇이든 상관없다는 말은 기기마다 길이 달라도 된다는 허락이었다. 사용자는 이어서 "통제할 수 있는 기기들을 최대한 다 패널에 모아 놓는 걸로 하자"고 범위를 정했다. 몇 분 뒤 뜬 첫 판에는 홈브리지가 가진 Hexagon과 침대 무드등 두 타일만 있었다. Pi는 Apple Home에 직접 붙을 수 없어서, 홈브리지 밖의 기기에 닿는 길로 나는 맥 미니의 단축어를 권했다. 맥이 단축어로 기기를 켜고 HomePod 값을 읽어 Pi로 밀어 주는 구조이고, 사용자도 그 길이면 될 것 같다며 단축어를 만들기 시작했다.

## Hexagon의 죽은 페어링과 Nanoleaf OpenAPI

첫 판의 두 타일 가운데 육각형 패널 조명 Hexagon은 처음부터 말을 듣지 않았다. 패널을 열어 본 사용자의 첫 반응은 이랬다.

> 지금 흠... Hexagon은 연결이 일단 안 되는 것 같다.

원인은 10월 12일로 거슬러 올라갔다. Hexagon을 초기화하면서 HomeKit 식별자가 바뀌었고, Hexagon은 Apple Home에 직접 다시 붙어 있었다. HomekitControl이 들고 있던 옛 페어링은 그날부터 "Wrong accessory pairing ID"로 죽어 있었다. 홈브리지는 명령에 200을 돌려줬지만 조명은 움직이지 않았다.

사용자는 홈브리지에 남은 이 죽은 항목을 빼자고 했다. 작업은 홈브리지 설정 편집 API로 했다. 설정을 백업한 뒤 HomekitControl의 죽은 항목을 지우고 캐시 액세서리를 치운 다음 브리지를 재시작했다. 컨테이너를 내릴 필요가 없었고 sudo도 필요 없었다. 이때 사용자는 Hexagon도 단축어로 켜면 된다고 봤고, 단축어를 만드는 동안 Hexagon이 가끔 패널 여러 개 중 일부만 색이 바뀐다는 문제를 맡기면서 조건을 달았다.

> 만약 nanoleaf API에 직접연결로 해결할 수 있다면 그것도 좋지만, 그 과정에서 저게 Apple Home에서 사라지는 건 안 돼.

Nanoleaf 조명은 HomeKit과 별개로 로컬 OpenAPI를 열고, 원인을 보려면 그 API의 토큰이 있어야 했다. 컨트롤러의 전원 버튼을 5~7초 누르면 잠깐 토큰 발급 요청을 받는 상태가 되고, 그 동안 Pi가 요청을 보내면 토큰이 나온다. 2초마다 요청을 보내는 대기를 10분 동안 띄워 두고 사용자가 버튼을 눌렀다. 이 토큰은 Apple Home 페어링과 무관해서, 받은 뒤에도 Hexagon은 같은 HomeKit 식별자로 페어링 상태를 알렸다. 토큰은 Pi의 `state/` 디렉터리에 0600으로 두고 git에서 뺐다.

"일부 패널만 색이 변한다"는 증상은 API로 풀리지 않았다. 사용자가 "지금 신호 한 번 봐봐. 바뀐 적 없어? 방금도 바뀌었는데. 패널이 계속 움직여."라고 해서 상태를 1초 간격으로 읽고 기기에 들어오는 이벤트도 기록해 봤더니, 그동안 OpenAPI가 보여 준 것은 단색 하나와 이벤트 없음이었다. 기기가 받은 명령은 그대로인데 패널만 움직이고 있었다. 사용자가 패널의 터치 반응을 끄자 증상이 사라졌고, 사용자는 펌웨어 업데이트도 넘기자고 했다.

토큰은 원인을 보려고 받은 것이었지만, 같은 무렵 사용자가 조명마다 밝기 조절이 있어야 한다고 하자 Hexagon 타일도 단축어를 거치지 않고 이 API로 움직이게 했다. HUD 쪽 코드는 기기 하나에 함수 둘이다. 읽기는 `GET /state`이고, 쓰기는 패널의 특성 이름을 Nanoleaf의 필드 이름으로 바꿔 `PUT /state`로 보낸 뒤 상태를 다시 읽어 타일을 갱신한다.

```python
def _nl_set(dev_id: str, char: str, value) -> dict:
    field = {"On": "on", "Brightness": "brightness", "ColorTemperature": "ct"}[char]
    _nl("PUT", "/state", {field: {"value": bool(value) if field == "on" else value}})
    return _nl_device(_nl("GET", "/state"))
```
{: data-filename="src/routes/home.py · 일부 발췌"}

세 갈래의 길이 생기자 색온도의 눈금이 서로 달랐다. HomeKit은 미레드(낮은 쪽이 차가운 빛)이고 Nanoleaf는 켈빈(높은 쪽이 차가운 빛)이다. 침대 무드등은 여기에 더해 펌웨어가 눈금을 거꾸로 알린다. 사용자의 말은 "저 펌웨어를 고칠 수는 없는 노릇이니 HUD쪽에서 바꾸자"였고, 그래서 기기가 알린 범위와 단위를 타일에 같이 넘기고, 무드등만 슬라이더를 뒤집어 왼쪽 끝이 실제로 따뜻하게 했다. 기기에 쓰는 값은 기기 자기 기준 그대로다.

## 식탁 등을 위한 두 번째 Matter 컨트롤러

식탁 등은 Nanoleaf의 스트립 조명이고 Thread로 붙은 Matter 기기다. 홈브리지에도 Nanoleaf OpenAPI에도 길이 없어서 단축어에 기대야 했는데, 사용자가 단축어로는 밝기 같은 값을 맞출 수 없다는 것을 확인하고 다른 방법을 찾아보라고 했다. Apple Home 기기에 값을 넘기는 길을 정리하니 네 가지였다.

| 방법 | 값 조절 | 조건 |
|---|---|---|
| A. 단축어 단계값 | 정해 둔 몇 단계만 | 값마다 분기를 단축어 안에 손으로 만들어야 함 |
| B. 맥에 HomeKit 앱을 직접 만들기 | 아무 값이나, HomePod 센서까지 | HomeKit 권한이 든 서명이 필요하고 무료 계정은 7일마다 다시 서명 |
| C. Pi가 식탁 등에 직접 붙기 | 밝기·색온도 전부 | 식탁 등이 Matter 기기여야 하고, Pi에 Matter 서버가 필요 |
| D. 에어컨 펌웨어에 HTTP 기능 추가 | 온도·모드 전부 | 펌웨어 소스가 필요한데 맥 미니에서 찾지 못했고, 무선 업데이트가 실패하면 USB 복구 |

식탁 등이 어떤 제품인지 묻자 사용자는 "식탁 등은 Nanoleaf 스트립 맞아, C로 가자."로 답했다. 에어컨 쪽은 이때 고르지 않았다.

C의 바탕은 Matter의 multi-admin이다. 한 기기가 여러 컨트롤러의 패브릭에 동시에 속할 수 있어서, Apple Home에서 기기의 "페어링 모드 켜기"로 임시 코드를 받아 Pi를 두 번째 컨트롤러로 붙이면 Apple Home 쪽 페어링은 그대로다. Pi에는 python-matter-server를 docker로 띄웠다.

```yaml
services:
  matter-server:
    image: ghcr.io/home-assistant-libs/python-matter-server:stable
    container_name: matter-server
    restart: unless-stopped
    entrypoint: ["matter-server"]
    network_mode: host
    # ...
    volumes:
      - /home/junhyeok/SmartHome/matter-server/data:/data
    command: >
      --storage-path /data
      --paa-root-cert-dir /data/credentials
      --listen-address 127.0.0.1
      --primary-interface eth0
      --log-level info
```
{: data-filename="~/SmartHome/matter-server/docker-compose.yml · 일부 생략"}

Matter의 운영 메시지와 mDNS가 호스트 네트워크에 있어야 해서 `host`다. 웹소켓 API는 `--listen-address 127.0.0.1`로 루프백에만 열어 두었고, 소비자는 HUD 서버 하나다. Thread 기기는 HomePod이 보더 라우터 노릇을 하며 광고하는 경로로 닿는다. 커널의 `accept_ra`는 꺼져 있지만 NetworkManager가 사용자 공간에서 라우터 광고를 받아 경로를 넣어 주어서, 따로 sysctl을 건드리지 않았다. 컨트롤러의 `data/` 디렉터리에는 패브릭 자격증명이 있어서 잃으면 기기를 다시 붙여야 한다.

HUD 쪽 호출은 요청마다 웹소켓을 새로 열고 닫는다. `start_listening`을 부르지 않으면 이벤트가 오지 않으니, 서버가 처음 보내는 인사말 하나를 버리고 나면 다음 메시지 가운데 내 `message_id`가 붙은 것이 답이다.

```python
def _matter(command: str, args: dict | None = None):
    ws = websocket.create_connection(MATTER_WS, timeout=MATTER_TIMEOUT)
    try:
        ws.recv()  # server info
        ws.send(json.dumps({"message_id": "1", "command": command, "args": args or {}}))
        while True:
            msg = json.loads(ws.recv())
            if msg.get("message_id") == "1":
                break
    finally:
        ws.close()
    ...
    return msg.get("result")
```
{: data-filename="src/routes/home.py · 설명용 재구성, 문서 문자열과 예외 처리 생략"}

읽기는 노드의 속성을 "엔드포인트/클러스터/속성" 키로 그대로 본다. On/Off 클러스터(6)가 있는 엔드포인트마다 타일이 하나이고, 밝기는 LevelControl(8)의 1~254를 백분율로 바꾸며, 색온도는 ColorControl(768)의 미레드다. Apple Home이 붙인 이름은 기기가 모르니 노드 번호에서 이름으로 가는 작은 표(`MATTER_NAMES`)를 코드에 둔다. 기기를 지웠다 다시 붙이면 노드 번호가 바뀌어 이름이 제품명으로 돌아가는데, 에러 없이 일어나는 일이라 서비스 지도의 계약에 적어 두었다.

처음 붙인 날에는 켜기·끄기와 밝기가 되었고, 색온도 슬라이더가 실제 색과 상관없이 한쪽 끝에 붙어 있는 문제는 11월 2일에야 풀렸다. ColorControl에서는 `ColorMode`(속성 8)가 2일 때만 색온도 속성이 현재 값이고, 0이면 색상·채도, 1이면 CIE xy가 현재 값이다. 이 조명은 평소 0이라 색온도 속성에는 0이거나 낡은 값이 들어 있었다. 11월 2일부터는 모드를 먼저 보고, 0이나 1이면 색상·채도나 xy에서 McCamy 근사식으로 상관 색온도를 구해 조명이 알린 범위로 자른다. `Options` 속성이 0이면 꺼진 조명에 보낸 색 명령이 버려진다는 것도 같은 날 드러나서, 색 명령에는 `optionsMask`와 `optionsOverride`를 1(ExecuteIfOff)로 싣는다.

```python
# ColorControl Options: ExecuteIfOff. Without it a colour command sent while the
# light is off is dropped (Options attribute 1/768/15 is 0 on the dining strip),
# so the slider's "colour, then on" came on in the old colour.
EXECUTE_IF_OFF = {"optionsMask": 1, "optionsOverride": 1}
```
{: data-filename="src/routes/home.py · 일부 발췌"}

## 에어컨 리모컨 펌웨어에 더한 HTTP API

에어컨은 빌트인이라 기기 자체가 네트워크에 없고, ESP32-C3 기반 IR 리모컨이 HomeSpan 펌웨어로 HeaterCooler 서비스를 만들어 Apple Home에 직접 붙어 있다. 펌웨어는 사용자가 만든 것이다. 홈브리지에는 올라 있지 않았고, 7월에 만들어 둔 HTTP 스위치 경로는 펌웨어를 바꾸면서 404가 된 상태였다.

처음 길은 앞에서 권한 맥 미니의 단축어였다. 사용자가 단축어 `HUD 에어컨 켜기`와 `끄기`를 만드는 동안 내가 맥 미니에 상주 스크립트를 깔아서, Pi가 보낸 명령을 `shortcuts run`으로 실행하게 했다. 시험에서는 HUD로 켜기를 보내자 맥이 1초 안에 받아 단축어를 실행했다. 그러나 사용자는 에어컨이 켜기·끄기만으로는 안 되고 온도 조절도 해야 한다고 했고, 단축어로 가면 온도마다 분기 블록을 손으로 만들어야 했다. 에어컨을 홈브리지로 옮기는 안은 Apple Home에서 에어컨을 지우고 다시 넣어야 해서 에어컨이 들어간 자동화를 다시 만들게 된다. 사용자는 그 안이 되는지 확인해 보라고 하면서 한 줄을 덧붙였다. 소스를 찾지 못해 접어 두었던 D가 그 한 줄로 다시 열렸다.

> 그리고 맥 미니에 소스코드 있다.

소스를 보니 이미 HeaterCooler(전원, 모드, 16~30℃, 팬 4단, 스윙)로 만들어져 있었고 무선 업데이트(OTA)도 켜져 있었다. 원본 폴더는 그대로 두고 사본에 Pi 전용 API를 더했다. `GET /state`가 `{active, mode, cool, heat, fan, vswing}`을 돌려주고, `POST /set?active=&mode=&temp=&fan=`이 값을 바꾼다. 요청은 `X-Token` 헤더가 펌웨어에 들어간 토큰과 맞을 때만 받고 아니면 401이다. 이 API로 바꾼 값은 펌웨어가 `setVal()`로 HomeKit에도 알려서, Apple Home과 HUD가 같은 상태를 본다. IR은 켜진 상태에서만 쏜다. 꺼진 동안 바뀐 온도와 모드는 기록만 해 두었다가 켤 때 함께 보낸다.

빌드는 맥 미니에서 SSH로 했고 한 번 막혔다. SSH 세션은 macOS가 보호하는 `~/Documents`를 읽지 못해서 HomeSpan 라이브러리가 없다고 나왔다. 라이브러리를 프로젝트 안의 별도 디렉터리에 내려받아 빌드에 쓰는 것으로 풀었다. 부팅에 실패하면 무선으로는 복구가 안 되어 기기를 떼어 USB로 꽂고 원래 펌웨어를 써야 하는 위험이 있어서, 빌드까지만 해 두고 올려도 되는지 물었다. 사용자의 답은 이랬다.

> 좋아, 해보자 그럼. 근데 D안은 뭐였지? 아무튼 해봐.

펌웨어를 무선으로 올린 뒤에는 한 번 왕복해서 Apple Home 연결이 살아 있는지 확인했다. Apple Home 쪽에서 켜기를 보내자 2초 만에 에어컨이 켜졌고, 새 API로 끄기를 보내자 바로 꺼졌고, 이어서 Apple Home이 꺼짐으로 읽혔다.

HUD 쪽은 앞의 두 길과 같은 모양으로 붙었다.

```python
def _ac_set(dev_id: str, char: str, value) -> dict:
    field = {"Active": "active", "TargetTemperature": "temp", "Mode": "mode"}[char]
    return _ac_device(_ac("POST", f"/set?{field}={int(value)}"))
```
{: data-filename="src/routes/home.py · 일부 발췌"}

이제 소스가 넷이다. 각 소스는 목록을 읽는 함수와 한 특성을 쓰는 함수를 짝으로 `SOURCES`에 등록되어 있다.

```python
SOURCES = {
    "homebridge": (_hb_devices, _hb_set),
    "nanoleaf": (_nl_devices, _nl_set),
    "matter": (_matter_devices, _matter_set),
    "aircon": (_ac_devices, _ac_set),
}
# Fixed devices keep a greyed tile while their source is down.
FALLBACK = {
    "nanoleaf": lambda: [_nl_device(None)],
    "aircon": lambda: [_ac_device(None)],
}
```
{: data-filename="src/routes/home.py · a88a2fd 이전, 일부 발췌"}

`/api/home`은 이 표를 차례로 돌며 목록 함수를 부른다. 한 소스가 `SourceError`를 내면 그 이름과 이유를 `errors`에 적고 다음 소스로 넘어가므로, 하나가 실패해도 다른 소스의 타일은 남는다. 실패한 소스가 `FALLBACK`에 있으면 그 자리에 회색 "No response" 타일을 대신 넣는다. 기기가 하나로 정해진 Hexagon과 에어컨은 그렇게 자리를 지킨다. 쓰기 요청도 마지막 목록에서 기기의 소스를 찾아 같은 표의 쓰기 함수로 보낸다. 11월 9일에는 식탁 등도 회색 타일을 갖게 된다. 잘못된 부팅 뒤 Matter 서버가 빈 저장소로 떠서 노드 목록이 에러 없이 비었고, 그동안 식탁 등 타일은 그냥 사라져 있었기 때문이다.

에어컨이 끝나자 사용자는 "단축어 쪽은 그럼 이제 다 꺼도 되겠네? 온습도 빼고."라고 물었고, 켜기·끄기 단축어와 Hexagon·식탁 등용 단축어를 직접 정리했다. 남은 것은 HomePod의 온도와 습도를 읽는 단축어 `HUD 홈 상태` 하나였다.

## HomePod 실내값을 보내는 홈 허브 자동화

HomePod 두 대(공부방, 거실)가 재는 온도와 습도는 Apple Home 안에만 있고, Apple 기기 밖으로 꺼내 주는 API가 없다. Pi는 Apple Home에 직접 붙을 수 없어서 Apple 기기의 단축어나 자동화가 유일한 길이었다. 10월 26일에는 맥 미니의 LaunchAgent가 `shortcuts run "HUD 홈 상태"`를 돌려 결과 텍스트를 Pi로 밀었다. 처음에는 2초마다였다가 에어컨 명령을 이 길에서 뺀 뒤 1분에 한 번 온습도만 보내도록 줄였다. 같은 날 오후에 사용자가 단축어가 실행될 때마다 메뉴 막대에 표시가 뜨는데 끌 수 있는 설정이 없느냐고 물은 적이 있다.

닷새 뒤인 10월 31일에 사용자가 맥 미니의 Zen이 무겁다는 문제를 들고 왔다. 거기서 이 표시가 다시 나왔다.

> 1번은 내가 했는데, 의심가는 게 있어. 그니까 그 우리 단축어 있지, Home 앱에서 상태 받아서 Pi로 쏴주는 게 있는데, 그게 실행될 때마다 메뉴바에 나타나거든. 그것 때문일 수도 있을까?

Pi에는 매분 같은 초에 push가 들어오고 있었고, macOS의 `WidgetRenderer_Activities`가 CPU 150%로 튀는 시각이 모두 그 실행과 겹쳤다. 이 프로세스는 부팅 뒤 4일 7시간째 6.19GB를 쓰고 있었는데, 실행 횟수(약 6,230회)에 1MB를 곱한 값과 거의 같았다. 실행 한 번마다 메뉴 막대 표시를 그리면서 1MB쯤 남긴다는 뜻이다. 내가 내놓은 안은 맥을 아예 빼는 1번과 맥 쪽 완화(렌더러가 커지면 죽이기, 주기를 2분으로 늘리기)였고, 사용자의 답은 짧았다.

> 1로 가 보자.

1번은 Apple Home의 홈 허브(HomePod)에서 도는 자동화가 값을 읽어 Pi로 보내는 구조다. 자동화의 트리거가 필요하고, 그 트리거를 홈브리지의 가상 스위치가 맡는다.

```text
홈브리지 가상 스위치 `HUD 센서 트리거`   매분 0초에 켜지고 15초 뒤 저절로 꺼진다
        ↓ (홈 앱 자동화: 이 스위치가 켜지면)
홈 허브(HomePod)가 HomePod 두 대의 온도·습도를 읽어 "키=값" 텍스트로 묶는다
        ↓ POST
HUD 서버의 푸시 엔드포인트 → 메모리에 저장 → 패널 위 온습도 한 줄, 시계 옆 공부방 값
```

가상 스위치는 `homebridge-dummy` 플러그인으로 만들었고, 스케줄을 `@minutely`로 두고 `autoReset`을 15초로 했다. 자동화는 아이폰 홈 앱에서 사용자가 직접 만들어야 했다. 자동화에는 Pi 주소와 토큰이 들어가야 해서, 따라 할 순서와 토큰을 적은 안내 파일을 Exchange 폴더에 두었다가 설정이 끝난 뒤 지웠다.

가상 스위치를 올리자 한 가지가 어긋났다.

> 아직 homebridge-dummy가 안 보이는 것 같아. 확인해줄래?

스위치는 매분 켜졌다 꺼지고 있었다. 문제는 홈브리지의 본 브리지가 Apple Home에 한 번도 페어링된 적이 없었다는 것이다. Apple Home에 붙어 있던 것은 침대 무드등을 실은 자식 브리지뿐이었고, 본 브리지에는 그때까지 실린 기기가 없었다. 사용자가 홈 앱에서 본 브리지를 한 번 추가하자 스위치가 나타났다.

HUD 서버는 이 경로에 쓰는 토큰을 따로 두었다. 맥 브리지가 쓰던 토큰은 이 경로에서 401이고, 홈 허브용 토큰이 새도 위조할 수 있는 것은 실내값뿐이다. 맥 브리지를 내리고 나서 push는 전부 홈 허브에서 매분 들어왔고, 값도 제대로 바뀌었다. 맥 쪽 LaunchAgent의 plist는 지우지 않고 이름만 바꿔 두었다.

받는 쪽 코드는 짧다. 자동화가 보내는 텍스트는 한 줄이 `공부방온도=24.7°C` 꼴이다.

```python
def _parse_reading(text: str) -> dict:
    out = {}
    for line in text.splitlines():
        key, sep, val = line.partition("=")
        m = re.search(r"-?\d+(?:\.\d+)?", val) if sep else None
        if m:
            out[key.strip()] = float(m.group())
    return out
```
{: data-filename="src/routes/home.py · 일부 발췌"}

줄마다 첫 `=`에서 키와 값을 가르고, `=`가 없는 줄은 건너뛴다. 값에서는 정규식 `-?\d+(?:\.\d+)?`로 처음 나오는 숫자만 꺼낸다. `-?`는 있어도 되는 음수 부호, `\d+`는 정수부, 괄호로 묶은 `\.\d+`는 있으면 붙는 소수부다. 그래서 `24.7°C`는 24.7, `45%`는 45가 되고, 숫자 뒤에 단위가 어떤 글자로 붙든 읽는 값은 같다. 숫자가 없는 값은 버린다. 5분(300초) 넘게 새 값이 오지 않으면 화면에서 숨긴다.

가상 스위치는 홈브리지가 제조사를 `Homebridge Dummy`로 알리므로, 패널은 이름이 아니라 제조사로 타일에서 뺀다. 자동화용 스위치를 나중에 더 만들어도 타일이 늘지 않고, `/api/home/set`으로도 건드릴 수 없다.

이 경로의 약점은 조용히 끊긴다는 점이다. 자동화가 꺼졌거나 지워져도, 본 브리지의 페어링이 풀려도, HomePod OS 업데이트로 홈 허브의 URL 동작이 깨져도, 에러는 어디에도 안 뜨고 마지막 값이 300초 뒤에 화면에서 사라질 뿐이다. 자동화의 정의 파일이 Pi나 맥 어디에도 없다는 점도 같다. 서비스 지도의 계약에는 점검 방법으로 서버 로그에서 HomePod 쪽 주소의 200이 매분 들어오는지 보라고 적었다.

## 홈브리지에 남은 두 역할과 옛 컨테이너의 삭제

홈브리지에는 지금 두 가지가 남아 있다. HomekitControl로 다시 내보내는 침대 무드등과, 10월 31일에 생긴 센서 트리거 스위치다. 앞의 Hexagon 페어링처럼 홈브리지가 정상이라고 하면서 틀리는 일은 11월 2일에 한 번 더 일어났다.

11월 2일에 사용자가 패널의 상태를 점검해 달라고 했다.

> 그리고 지금 home 패널의 상태가 다른 기기들 상태랑 같은지도 확인해줄래? 최소한 Apple Home 상태랑 이 패널의 상태는 서로 맞았으면 좋겠어.

각 기기의 직통 경로 값과 패널 값을 비교하자 침대 무드등만 어긋나 있었다. 패널에는 꺼짐·12%인데 램프에 직접 물으면 켜짐·50%였다. 그날 오후 3시쯤 Pi가 재부팅될 때 램프가 아직 응답하지 않아(`EHOSTUNREACH`) HomekitControl의 시작 연결이 한 번 실패했고, 이 플러그인은 그 뒤로 다시 시도하지 않는다. 다섯 시간 반 동안 홈브리지는 캐시만 내놓았고, Apple Home과 패널은 같은 캐시를 보며 서로 맞은 채로 함께 틀렸다. 자식 브리지의 상태는 내내 "ok"였다. 차이는 로그에서 `Launched child bridge` 뒤에 `All Clients ready now`가 오지 않는 것뿐이었다.

HUD 서버에 스레드를 하나 더해, 1분마다 홈브리지 로그의 끝 128KB를 읽는다.

```python
def _hb_child_unfinished() -> str | None:
    """The child bridge's last "Launched" line, if no "All Clients ready now"
    came after it."""
    ...
    tag, launch = f"[{HB_CHILD_PLUGIN}]", None
    for line in _ANSI.sub("", text).splitlines():
        if tag not in line:
            continue
        if "Launched child bridge" in line:
            launch = line.strip()
        elif "All Clients ready now" in line:
            launch = None
    return launch
```
{: data-filename="src/routes/home.py · 일부 생략"}

생략한 앞부분은 그 128KB를 `text`에 담고, 파일을 열지 못하면 `None`을 돌려준다. 그 뒤로는 ANSI 색 코드를 지우고 이 플러그인의 태그가 붙은 줄만 위에서부터 본다. `Launched child bridge`가 나오면 그 줄을 기억하고, 뒤에 `All Clients ready now`가 나오면 지운다. 끝까지 읽었을 때 기억에 남은 줄이 있으면 마지막 시작이 끝나지 않은 것이다.

그 상태가 2분 넘게 이어지면 UI API로 그 자식 브리지만 다시 띄운다. 정상적인 시작은 몇 초면 끝나므로, 2분은 막 시작하는 중인 브리지를 건드리지 않으려는 여유다. 램프가 계속 꺼져 있으면 15분에 한 번까지만 시도하고, 그동안 그 브리지의 타일은 "No response"로 보인다. 이 감시는 로그 문구와 로그 경로, 플러그인 이름에 기대고 있다. 하나라도 바뀌면 에러 없이 멈춘다는 점을 서비스 지도의 홈브리지 계약에 적었다.

이 재시작 요청은 감시를 넣은 뒤 하루 남짓 동안 실제로는 통과하지 못했다. 홈브리지를 부르는 공통 함수가 본문 없는 요청에도 `Content-Type: application/json`을 붙였는데, 홈브리지 UI 서버는 그런 요청을 400으로 거절하고, 재시작 요청에는 본문이 없다. 11월 3일 재부팅 때 무드등 브리지가 다시 같은 상태로 떴고, 커밋 메시지에 따르면 15분마다의 재시작이 모두 400으로 실패해 손으로 재시작하기까지 일곱 시간 동안 타일이 "No response"였다. 11월 4일에 헤더를 본문이 있을 때만 붙이도록 고쳤다. 그동안에도 고장을 알아보는 쪽은 맞게 동작했고, 막힌 것은 고치러 보내는 요청이었다.

같은 날 저녁에 사용자는 홈 디렉터리를 정리하면서 이렇게 말했다.

> matter-server랑 homebridge도 하나의 폴더로 합치고 싶어.

두 컨테이너의 설정 디렉터리를 `~/SmartHome` 아래로 옮기는 일이었고, 홈브리지는 compose 파일이 이미 있어 옮기기만 하면 될 줄 알았다. 그런데 기존 컨테이너는 compose가 아니라 `docker run`으로 만든 것이었다. compose 파일에 적혀 있던 `command:` 줄(`homebridge -I`를 띄우는 명령)은 한 번도 실제로 쓰인 적이 없었고, 처음 compose로 띄우자 컨테이너의 s6가 그 명령을 hb-service와 따로 돌려 홈브리지가 두 벌 떴다. 그 줄을 지워서 옛 컨테이너와 같게 맞췄다. 덤으로 compose의 `TZ=Asia/Seoul`이 처음 적용되어 홈브리지 로그의 시각이 UTC에서 KST로 바뀌었다. 감시 스레드는 시각을 읽지 않으니 영향이 없었다. 한 가지 더, 감시 스레드가 읽는 로그 경로가 이 디렉터리라서 옮길 때 코드의 `HB_LOG`도 같이 바꿨다. 못 열면 `except OSError`로 조용히 넘어가 감시가 멈추는 자리다.

옛 컨테이너는 이름을 `homebridge-old-20261102`로 바꾸고 멈춘 채 남겨 두었다. 새 컨테이너가 뜬 뒤 Apple Home의 기기들이 정상인지 사용자가 확인했고, 같은 날 사용자가 직접 `docker rm`으로 지웠다.

## 조용히 끊기는 기기별 경로

해결된 것은 Apple Home에서 기기가 사라지지 않은 채로 기기마다 따로 가는 길이 생긴 것이다. 침대 무드등은 홈브리지, Hexagon은 Nanoleaf OpenAPI, 식탁 등은 Matter, 에어컨은 펌웨어의 HTTP API로 가고, HomePod의 값은 반대 방향으로 홈 허브가 보낸다. 이 길들이 깨지는 방식은 거의 모두 조용하다. 에어컨과 Hexagon은 IP가 바뀌면 타일이 회색이 되지만, 홈 허브 자동화와 홈브리지 로그 문구는 아무 에러 없이 값을 잃는다. 그런 결합은 서비스 지도의 계약으로 적어 두었으나, 결국 사람이 점검 명령을 돌려 보아야 아는 종류다.
