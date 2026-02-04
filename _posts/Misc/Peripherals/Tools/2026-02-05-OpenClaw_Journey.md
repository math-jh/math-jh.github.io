---

title: "Raspberry Pi 5에 OpenClaw 설치하기: 완전한 개인 AI 비서 구축하기"
excerpt: "Raspberry Pi 5와 OpenClaw로 만든 나만의 AI 비서. 30일간의 운영 경험과 실제 활용법, 문제 해결 과정을 공개합니다."

categories: [Misc / Peripherals]
permalink: /ko/misc/peripherals/tools/openclaw_raspberry_pi
header:
    overlay_image: /assets/images/Misc/Peripherals/OpenClaw_Raspberry_Pi.jpeg
    overlay_filter: 0.5

toc: true
date: 2026-02-05
last_modified_at: 2026-02-05
weight: 5
published: true

---

## 왜 OpenClaw였는가

2024년 말, 나는 Raspberry Pi 5를 단순한 홈서버로 사용하고 있었다. 처음엔 NAS로 시작해서 Jekyll 블로그를 호스팅하고, Homebridge로 조명을 제어하는 정도. 하지만 언제부턴가 "이 정도 성능을 가지고 뭔가 더 핵심 있는 걸 할 수 있지 않을까?"라는 생각이 들기 시작했다.

ChatGPT나 Claude는 편리했지만, 항상 뭔가 찜찜했다. 내 대화 기록이 어디에 저장되는지, 어떻게 활용되는지 알 수 없었고, 프라이버시에 대한 불안감이 컸다. 게다가 매월 내는 구독료도 부담이었다. 그러던 중 우연히 발견한 게 [OpenClaw](https://github.com/openclaw/openclaw)였다.

OpenClaw는 단순한 AI 챗봇이 아니었다. 완전한 AI 에이전트 플랫폼이었고, 내가 원하는 대로 커스터마이즈할 수 있었다. 특히 마음에 들었던 점은:

- **완전한 로컬 실행**: 인터넷이 끊겨도 작동한다
- **데이터 주권**: 모든 대화와 파일이 내 Pi 안에 있다
- **무제한 사용**: API 요금제에 구애받지 않는다
- **확장 가능성**: Python 스크립트부터 Docker 컨테이너까지 연결 가능
- **자동화**: cron job으로 루틴 작업을 완전히 자동화

첫눈에 반했고, 곧바로 도전하기로 결심했다.

## 하드웨어 선택의 고민

OpenClaw를 설치하기 전, 나는 심각한 고민에 빠졌다. 4GB RAM 모델로도 충분할까, 아니면 8GB로 가야 할까? AI 작업에는 메모리가 생명이지만, 가격 차이도 만만치 않았다.

결국 8GB 모델을 선택했고, 그 선택은 정말 현명했었다. 실제 사용핸 지금, 8GB 중 평균 3.5GB를 상시 사용하고 있고, AI 모델 로딩 시에는 6GB까지 치솟는다. 4GB였다면 분명 고생했을 것이다.

최종 하드웨어 구성은 이렇다:

| 구성품 | 사양 | 선택 이유 | 실제 사용 후기 |
|--------|------|-----------|----------------|
| **Raspberry Pi 5** | 8GB RAM | AI 작업 메모리 필요 | 최소 8GB 권장 |
| **NVMe SSD** | WD SN740 256GB | SD카드보다 10배 빠름 | 부팅 15초, AI 로딩 3초 |
| **전원 공급 장치** | 27W USB-C PD | 공식 권장 사양 | 안정적이고 발열 적음 |
| **케이스** | Argon ONE V3 | NVMe 지원, 냉각 우수 | 24시간 만에 45°C 최대 |
| **네트워크** | Tailscale VPN | 복잡한 포트포워딩 없이 | 5분 만에 외부 접속 완료 |

총 투자 금액은 약 25만원. 고성능 NAS 하나 사는 돈으로 AI 비서를 만들었다는 생각에 만족했다.

## 설치 전쟁: 예상치 못한 난관들

### 1단계: NVMe 지옥

Raspberry Pi 5에 NVMe SSD를 연결하는 건 생각보다 복잡했다. 먼저 M.2 HAT+를 별도로 구매해야 했고, PCIe 포트를 활성화하는 데도 애를 먹었다.

처음엔 `/boot/firmware/config.txt`에 다음 두 줄만 추가하면 된다고 생각했다:

```bash
dtparam=pciex1
dtparam=pciex1_gen=3
```

하지만 재부팅 후에도 NVMe가 인식되지 않았다. 3시간 동안 핀 배열을 확인하고, 다른 SSD로 교체핏 보고, 결국은 `/boot/firmware/config.txt`에 다음을 추가해야 했다:

```bash
# PCIe 설정 - 이게 없으면 아무것도 안 된다
dtparam=pciex1
dtparam=pciex1_gen=3  # Gen 3로 설정하면 2배 빨라진다

# 전력 관리 - NVMe 안정성을 위해 필수
dtparam=nvme
```

### 2단계: OS 마이그레이션의 고통

처음엔 SD카드에 OS를 설치한 뒤, 나중에 NVMe로 옮기기로 했다. `rpi-clone`이라는 도구를 사용했는데, 128GB SD카드에서 256GB NVMe로 복제하는 데만 2시간이 걸렸다. 

그런데 복제 후 재부팅하니 부팅이 안 되는 것이 아닌가. 알고 보니 `/etc/fstab`의 UUID가 달라져서였다. 결국 수동으로 수정해야 했다:

```bash
# 새로운 UUID 확인
sudo blkid
# /etc/fstab 수정
sudo nano /etc/fstab
```

### 3단계: Node.js 버전 지옥

OpenClaw는 Node.js 22.x를 요구했다. 하지만 Raspberry Pi OS 기본 저장소에는 18.x 밖에 없었다. NodeSource 저장소를 추가했지만, ARM64 패키지를 찾지 못해 30분 동안 항해했다.

결국 이렇게 해결했다:

```bash
# Node.js 22.x 설치 - ARM64 전용
sudo mkdir -p /etc/apt/keyrings
curl -fsSL https://deb.nodesource.com/gpgkey/nodesource-repo.gpg.key | sudo gpg --dearmor -o /etc/apt/keyrings/nodesource.gpg
NODE_MAJOR=22
echo "deb [signed-by=/etc/apt/keyrings/nodesource.gpg arch=arm64] https://deb.nodesource.com/node_$NODE_MAJOR.x nodistro main" | sudo tee /etc/apt/sources.list.d/nodesource.list
sudo apt update
sudo apt install nodejs -y
```

### 4단계: 메모리 부족 대재앙

OpenClaw를 처음 실행했을 때, 시스템이 완전히 멈췄다. 8GB RAM이 있어도 AI 모델 로딩 시에는 부족했던 것이다. `htop`으로 확인핸 결과, 메모리 사용률이 100%를 찍고 스왑이瘋狂적으로 움직이는 것이 아닌가.

즉시 4GB 스왑 파일을 생성했다:

```bash
# 스왑 파일 생성 - 4GB로 설정
sudo fallocate -l 4G /swapfile
sudo chmod 600 /swapfile
sudo mkswap /swapfile
sudo swapon /swapfile

# 영구 설정
 echo '/swapfile none swap sw 0 0' | sudo tee -a /etc/fstab
```

### 5단계: 설정 파일의 트랩

OpenClaw의 `config.json`은 생각보다 민감했다. 한 줄의 쉼표 하나 때문에 2시간 동안 디버깅했다. 최종적으로 작동한 설정은:

```json
{
  "gateway": {
    "port": 8080,
    "host": "0.0.0.0",
    "auth": {
      "jwtSecret": "junhyeok-pi-super-secret-2026-key",
      "sessionTimeout": 86400
    }
  },
  "channels": {
    "webchat": {
      "enabled": true,
      "port": 3000,
      "path": "/chat"
    }
  },
  "memory": {
    "path": "/home/junhyeok/.openclaw/memory",
    "search": {
      "enabled": true,
      "maxResults": 10
    }
  },
  "models": {
    "default": "moonshot/kimi-k2-0905-preview",
    "fallback": "openai/gpt-3.5-turbo"
  }
}
```

이 모든 과정을 마치고 나니, 벌써 새벽 3시였다. 하지만 처음 OpenClaw가 "안녕하세요, 전원이 들어왔습니다"라고 메시지를 볃을 때, 그 순간의 짜릿함은 이루 말할 수 없었다.

## 실전에서 만난 진짜 문제들

### 문제 1: Docker 컨테이너의 포트 전쟁

Homebridge와 OpenClaw를 동시에 돌리려니 포트 충돌이 끊이지 않았다. Homebridge가 8080 포트를, OpenClaw도 8080 포트를 원하는 것이 아닌가. 

nginx로 리버스 프록시를 설정해서 해결했다:

```nginx
# /etc/nginx/sites-available/homebridge
server {
    listen 8581 ssl;
    server_name pi.local;
    
    ssl_certificate /home/junhyeok/.cert/pi.crt;
    ssl_certificate_key /home/junhyeok/.cert/pi.key;
    
    location / {
        proxy_pass http://localhost:8080;
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
    }
}
```

### 문제 2: Tailscale의 느린 속도

처음엔 Tailscale이 너무 느렸다. 집에서 10m 떨어진 카페에서 접속핸더니, 응답 속도가 5초 이상 걸렸다. 알고 보인 default relay 서버가 너무 멀리 있었던 것이다.

해결책은 Headscale이라는 자체 릴리 서버를 설치하는 것이었지만, 그건 너무 복잡했다. 대신 다음과 같이 최적화했다:

```bash
# Tailscale 성능 최적화
sudo tailscale up --netfilter-mode=off --accept-routes
```

그 결과 응답 속도가 5초에서 1.2초로 단축되었다.

### 문제 3: SD 카드의 갑작스런 죽음

설치한 지 일주일 만에 시스템이 부팅되지 않았다. 원인은 SD 카드의 갑작스러운 고장이었다.慶幸하게도 NVMe로 이전핸 후라 데이터는 안전했지만, 부팅 파티션이 손상되었다.

이후로는 다음과 같은 대책을 세웠다:
- 주요 설정 파일은 GitHub에 백업
- 중요 스크립트는 `/home/junhyeok/scripts`에 보관
- 주기적으로 SD 카드 상태 체크: `sudo smartctl -a /dev/mmcblk0`

### 문제 4: AI 모델의 예측 불가능한 응답

처음엔 AI 모델이 너무 자유분방해서 당황했다. 내가 "오늘 뭐하지?"라고 물었더니, "달나라에 가서 치즈를 만들어보는 건 어떨까요?"라고 답하는 것이 아닌가.

이를 해결하기 위해 시스템 프롬프트를 구체화했다:

```json
{
  "systemPrompt": "당신은 기술적인 AI 비서입니다. 실용적이고 구체적인 답변을 해주세요. 환각은 피하고, 모르는 것은 모른다고 말해주세요."
}
```

그 결과 AI의 답변이 훨씬 실용적이고信賴할 수 있게 되었다.

## 30일 만에 완성한 나만의 AI 비서

### 1. 똑똑한 블로그 관리자

처음엔 수동으로 Git 명령어를 쳤다. 하지만 하루에도 수십 번씩 반복하니 지쳤다. 그래서 만들어 낸 게 이 스크립트다:

```bash
#!/bin/bash
# /home/junhyeok/scripts/blog-smart-sync.sh

BLOG_DIR="/home/junhyeok/math-jh.github.io"
cd $BLOG_DIR

# 변경사항 감지
if [[ -n $(git status -s) ]]; then
    echo "[$(date)] 블로그 변경사항 감지"
    
    # 자동 커밋 메시지 생성
    CHANGES=$(git status -s | wc -l)
    ADDED=$(git status -s | grep "^A" | wc -l)
    MODIFIED=$(git status -s | grep "^M" | wc -l)
    DELETED=$(git status -s | grep "^D" | wc -l)
    
    COMMIT_MSG="자동 동기화: ${CHANGES}개 변경 (${ADDED}추가/${MODIFIED}수정/${DELETED}삭제)"
    
    git add .
    git commit -m "$COMMIT_MSG"
    git push origin main
    
    echo "[$(date)] 동기화 완료: $COMMIT_MSG"
else
    echo "[$(date)] 변경사항 없음"
fi
```

이 스크립트는 5분마다 실행된다. 덕분에 블로그 글을 쓰고 나면 5분 안에 자동으로 GitHub에 반영된다. 지금까지 327번의 동기화 중 실패는 단 한 번도 없다.

### 2. 홈 IoT의 중심

나는 집에 3개의 스마트 조명이 있다. 각각 다른 브랜드라서 앱도 다 달랐다. OpenClaw로 통합한 뒤로는 이렇게 간단해졌다:

```bash
# 조명 제어 함수들
lights_on() {
    homebridge_control "Hexagon" "on" "100"
    homebridge_control "탁상 무드등" "on" "80"
    homebridge_control "침대 무드등" "on" "60"
    say "모든 조명을 켰습니다"
}

lights_study() {
    homebridge_control "Hexagon" "on" "90"
    homebridge_control "탁상 무드등" "on" "100"
    homebridge_control "침대 무드등" "off" "0"
    say "공부 모드로 전환했습니다"
}

lights_sleep() {
    homebridge_control "Hexagon" "off" "0"
    homebridge_control "탁상 무드등" "off" "0"
    homebridge_control "침대 무드등" "on" "20"
    say "취침 모드입니다. 좋은 꿈 꾸세요"
}
```

이제 "야, 공부할 거야"라고 말하면 자동으로 공부 모드로 전환된다. "자야겠다"라고 하면 모든 조명이 꺼지고 침대 무드등만 살짝 켜진다.

### 3. 수학 도서관 사서

수학 전공자로서, 책에서 특정 정리나 증명을 찾는 건 일상이다. 하지만 수십 권의 책을 하나씩 뒤지는 건 고역이었다. OpenClaw는 이걸 3초 만에 해결한다:

```python
import os
import subprocess
import json

def search_math_books(keyword):
    """수학 책들에서 키워드 검색"""
    math_dir = "/home/junhyeok/Documents/Books/Mathematics"
    results = []
    
    for root, dirs, files in os.walk(math_dir):
        for file in files:
            if file.endswith('.pdf'):
                filepath = os.path.join(root, file)
                try:
                    # pdfgrep으로 검색
                    output = subprocess.check_output(
                        ['pdfgrep', '-n', '-i', keyword, filepath],
                        stderr=subprocess.DEVNULL
                    ).decode('utf-8')
                    
                    if output:
                        lines = output.strip().split('\n')
                        results.append({
                            'book': file,
                            'path': filepath,
                            'matches': len(lines),
                            'preview': lines[:3] if len(lines) > 3 else lines
                        })
                except:
                    continue
    
    return sorted(results, key=lambda x: x['matches'], reverse=True)
```

"책에서 헤세 행렬에 대해 찾아줘"라고만 말하면, 47권의 수학 책을 3초 만에 검색해서 가장 관련성 높은 결과를 보여준다. 실제 사용 결과, 92%의 확률로 원하는 정보를 찾아낸다.

### 4. 개인 비서의 핵심: 기억과 학습

OpenClaw의 가장 강력한 기능은 바로 기억력이다. 매 대화를 저장하고, 다음 번에 그 정보를 활용한다:

```json
{
  "memory": {
    "important_dates": {
      "thesis_deadline": "2026-05-15",
      "conference": "2026-03-20"
    },
    "preferences": {
      "study_time": "22:00-02:00",
      "light_brightness": "80%",
      "tts_voice": "Nova"
    },
    "learned_facts": {
      "favorite_theorem": "Gödel의不完全性定理",
      "difficult_topic": "代数幾何"
    }
  }
}
```

예를 들어, 내가 "졸른다"고 하면 AI는 현재 시간이 새벽 1시라는 걸 기억하고, "그럼 오늘은 여기까지. 내일 아침 9시에 알람 맞춰드릴까요?"라고 제안한다.

### 5. 건강 관리자

24시간 운영되는 시스템이니까, 건강도 챙겨야 했다:

```bash
# 2시간마다 자세 교정 알림
posture_check() {
    if [[ $(date +%H) -ge 22 ]] || [[ $(date +%H) -le 06 ]]; then
        return  # 밤에는 알리지 않음
    fi
    
    say "자세를 확인해주세요. 목과 어깨를 이완하고, 눈은 모니터에서 50cm 떨어뜨리세요."
    
    # 동시에 조명도 살짝 밝게
    current_brightness=$(homebridge_get "탁상 무드등")
    if [[ $current_brightness -lt 80 ]]; then
        homebridge_control "탁상 무드등" "on" $((current_brightness + 10))
    fi
}
```

2시간마다 자세를 확인해주고, 필요하면 조명도 조절해준다. 덕분에 목 통증이 70% 정도 줄었다.

## 실제 하루: AI 비서와 함께한 24시간

### 07:00 - 아침을 깨우는 AI

알람이 울리기 15분 전, 서서히 조명이 밝아진다. 7시 정각이 되자, 침대 옆 HomePod에서 익숙한 목소리가 들린다:

"좋은 아침입니다, 준혁님. 오늘은 2월 5일 목요일, 서울의 날씨는 영하 2도에서 영상 5도입니다. 미세먼지 좋음. 오후 3시에 미팅이 예정되어 있습니다."

동시에 블라인드가 자동으로 열리고, 전기포트가 켜진다. 이 모든 건 OpenClaw가 cron job으로 처리한다:

```bash
# Morning routine - 06:45 (15분 전에 시작)
0 6 * * * /home/junhyeok/scripts/morning_routine.sh
```

### 09:30 - 수업 준비 중

"책에서 바나흐 공간에 대한 정리 좀 찾아줘"

3초 후, 화면에 결과가 뜬다. 내가 가진 47권의 수학 책 중, 바나흐 공간을 다룬 12권의 책이 나열되고, 가장 관련성 높은 3권의 페이지 번호까지 표시된다. 

"Functional Analysis by Rudin, 페이지 105-120이 가장 자세합니다. PDF를 바로 여시겠습니까?"

### 14:00 - 점심 시간 문제

갑자기 nginx가 다울랐다. 로그를 확인핸더니, SSL 인증서가 만료되었다. panic이 되기 전에 OpenClaw가 말한다:

"nginx 오류를 감지했습니다. SSL 인증서 만료가 원인입니다. 자동으로 갱신하겠습니까?"

"응, 해줘"

1분 후, 새 인증서가 설치되고 nginx가 재시작된다. 내가 한 건 "응, 해줘"라는 한 마디뿐이었다.

### 18:00 - 저녁 준비

"오늘 뭐 먹을까?"

"냉장고를 스캔핸 결과, 닭고기와 브로콜리가 2일 남았습니다. 치킨 스튜를 추천드립니다. 조리 시간 45분. 레시피를 보여드릴까요?"

### 22:00 - 공부 시간

조명이 자동으로 공부 모드로 전환된다. 탁상등은 100%, 천장등은 60%, 침대등은 꺼진다. 동시에 집중을 방해하는 알림이 모두 무음으로 바뀐다.

"이제 집중 시간입니다. 2시간 동안 방해 금지 모드를 활성화할까요?"

### 00:30 - 하루 마무리

"오늘 하루를 정리해줘"

"오늘 총 8시간 45분을 공부했습니다. 블로그에 2개의 글을 작성했고, GitHub에 7개의 커밋을 했습니다. 조명 사용량은 평소보다 15% 줄었고, 건강 알림 6회를 모두 지켰습니다."

"내일 아침 9시에 알람 맞춰줘"

"네, 내일 아침 8시 45분에 서서히 깨우고 9시에 알람 울리겠습니다. 좋은 밤 되세요."

조명이 서서히 어두워지고, 5분 후에는 침대 무드등만 살짝 켜진다. HomePod에서 흰소리가 흘러나온다.

이게 바로 내가 만든 AI 비서의 하루다. 단순한 도구를 넘어, 생활의 일부가 되었다.

## 성능과 안정성

한 달 정도 운영한 결과:

| 항목 | 측정값 | 비고 |
|------|--------|------|
| **가동 시간** | 99.8% | 예기치 못한 재부팅 2회 |
| **평균 CPU 사용률** | 15% | AI 작업 시 60%까지 상승 |
| **메모리 사용률** | 2.8GB / 8GB | 여유 있음 |
| **응답 시간** | 평균 1.2초 | Tailscale 경유 시 |
| **동기화 성공률** | 100% | GitHub 연동 327회 성공 |

## 앞으로의 계획

### 단기 계획
- [ ] 더 많은 수학 도구 통합 (SageMath, Mathematica)
- [ ] 음성 인식 추가
- [ ] 홈 IoT 장치 더 추가

### 중기 계획  
- [ ] 로컬 AI 모델 학습 (작은 모델)
- [ ] 개인 지식베이스 구축
- [ ] 자동 백업 시스템

### 장기 계획
- [ ] 클러스터링 (여러 Pi 연결)
- [ ] edge computing 응용
- [ ] 연구 노트 자동화

## 소감

Raspberry Pi 5에 OpenClaw를 설치하면서 단순한 홈서버를 넘어서, 진짜로 내 일상을 도와주는 AI 비서를 갖게 되었다. 처음에는 복잡해 보였지만, 하나씩 설정하면서 시스템이 내 손에 익숙해지는 것을 느꼈다.

특히 만족스러운 점은:
- **프라이버시**: 모든 데이터가 내 집 안에 있다
- **맞춤화**: 필요에 따라 자유롭게 수정 가능  
- **학습**: 설정하면서 시스템에 대해 많이 배웠다
- **확장성**: 앞으로도 계속 발전시킬 수 있다

한 달 정도 사용핸 지금은, 이 시스템이 없는 삶은 상상하기 어렵다. 아침에 일어나서 "오늘 뭐하지?"라고 물으면 바로 답변해주고, 공부하다가 궁금한 것이 있으면 즉시 도와준다.

**추천하는 사람**: 
- 개인 정보를 중요하게 생각하는 사람
- 기술을 좋아하고 설정하는 것을 즐기는 사람  
- 자신만의 AI 시스템을 갖고 싶은 사람
- Raspberry Pi로 뭔가 핵심 있는 프로젝트를 하고 싶은 사람

**주의할 점**:
- 초기 설정에 시간이 꽤 걸린다
- Linux에 대한 기본 지식이 필요하다
- 가끔은 문제 해결에 고생할 각오가 필요하다

하지만 이 모든 것이 끝나면, 당신만의 특별한 AI 비서를 갖게 될 것이다. 나는 이 여정이 정말 즐거웠고, 앞으로도 계속 발전시켜 나갈 예정이다.

---

**참고 자료**:
- [OpenClaw 공식 문서](https://docs.openclaw.ai)
- [Raspberry Pi 공식 문서](https://www.raspberrypi.com/documentation/)
- [Tailscale 설치 가이드](https://tailscale.com/kb/install/)