---

title: "Raspberry Pi 5에 OpenClaw 설치하기: 나만의 AI 비서 만들기"
excerpt: "Raspberry Pi 5에 OpenClaw를 설치하여 개인 AI 비서를 구축한 과정과 고생담"

categories: [Misc / Peripherals]
permalink: /ko/misc/peripherals/tools/openclaw_raspberry_pi
header:
    overlay_image: /assets/images/Misc/Peripherals/OpenClaw_Raspberry_Pi.jpeg
    overlay_filter: 0.5

toc: true
date: 2026-02-05
last_modified_at: 2026-02-05
weight: 5
published: false

---

## 왜 OpenClaw인가?

작년 말부터 [Raspberry Pi 5](https://www.raspberrypi.com/products/raspberry-pi-5/)를 홈서버로 사용하면서, 단순히 파일 서버나 블로그 호스팅만으로는 뭔가 부족하다는 생각이 들었다. 그러던 중 [OpenClaw](https://github.com/openclaw/openclaw)라는 프로젝트를 발견했는데, 이는 개인적인 AI 비서를 구축할 수 있는 오픈소스 플랫폼이었다. 

기존의 ChatGPT나 Claude와는 다르게:
- **로컬에서 실행**: 모든 데이터가 내 장비 안에 머무름
- **확장 가능**: 필요에 따라 다양한 도구와 연결 가능
- **자동화**: cron job이나 webhook으로 자동 작업 수행

이런 점들이 매력적으로 다가왔고, 곧바로 설치를 결심했다.

## 하드웨어 준비

사용한 하드웨어는 다음과 같다:

| 구성품 | 사양 | 비고 |
|--------|------|------|
| **Raspberry Pi 5** | 8GB RAM | AI 작업에는 메모리가 필수 |
| **NVMe SSD** | WD SN740 256GB | SD카드보다 훨씬 빠르고 안정적 |
| **전원 공급 장치** | 27W USB-C PD | Pi 5는 전력이 많이 든다 |
| **케이스** | Argon ONE V3 | NVMe 지원, 냉각 우수 |
| **네트워크** | Tailscale VPN | 외부 접속을 위한 안전한 터널링 |

## 설치 과정

### 1단계: 기본 OS 설정

우선 Raspberry Pi OS를 NVMe SSD에 설치했다:

```bash
# 시스템 업데이트
sudo apt update && sudo apt upgrade -y

# 필수 패키지 설치
sudo apt install -y git curl build-essential python3-pip docker.io

# Docker 시작
sudo systemctl enable docker
sudo systemctl start docker
sudo usermod -aG docker $USER
```

### 2단계: NVMe 부팅 설정

Pi 5는 기본적으로 NVMe 부팅을 지원하지 않으므로, 설정을 변경해야 했다:

```bash
# /boot/firmware/config.txt 편집
echo "dtparam=pciex1" | sudo tee -a /boot/firmware/config.txt
echo "dtparam=pciex1_gen=3" | sudo tee -a /boot/firmware/config.txt

# 재부팅
sudo reboot
```

### 3단계: OpenClaw 설치

OpenClaw는 npm 패키지로 제공된다:

```bash
# Node.js 설치 (최신 버전)
curl -fsSL https://deb.nodesource.com/setup_22.x | sudo -E bash -
sudo apt-get install -y nodejs

# OpenClaw 전역 설치
sudo npm install -g openclaw

# 설정 디렉토리 생성
mkdir -p ~/.openclaw
cd ~/.openclaw
```

### 4단계: 설정 파일 구성

`config.json` 파일을 만들어 기본 설정을 했다:

```json
{
  "gateway": {
    "port": 8080,
    "host": "localhost",
    "auth": {
      "jwtSecret": "my-super-secret-key"
    }
  },
  "channels": {
    "webchat": {
      "enabled": true,
      "port": 3000
    }
  },
  "memory": {
    "path": "~/.openclaw/memory",
    "search": {
      "enabled": true
    }
  }
}
```

## 만난 문제들과 해결책

### 문제 1: 메모리 부족

처음 설치할 때는 4GB RAM 모델을 사용했는데, AI 모델 로딩 중에 메모리가 부족해지는 문제가 발생했다. **해결책**: 8GB 모델로 업그레이드하고, 4GB 스완 파일을 추가했다.

```bash
# 스왑 파일 생성
sudo fallocate -l 4G /swapfile
sudo chmod 600 /swapfile
sudo mkswap /swapfile
sudo swapon /swapfile
```

### 문제 2: Docker 컨테이너 충돌

Homebridge와 OpenClaw를 동시에 돌리니 포트 충돌이 발생했다. **해결책**: 각 서비스를 다른 포트로 설정하고, nginx로 리버스 프록시를 구성했다.

### 문제 3: 외부 접속

집 밖에서 접속하려면 공인 IP나 복잡한 포트 포워딩이 필요했다. **해결책**: Tailscale VPN으로 간단히 해결했다.

```bash
# Tailscale 설치
curl -fsSL https://tailscale.com/install.sh | sh
sudo tailscale up
```

## 현재 설정된 기능들

### 1. 블로그 자동 동기화

```bash
# /home/junhyeok/scripts/blog-autosync.sh
#!/bin/bash
# 5분마다 블로그 변경사항을 자동으로 Git에 커밋
```

이 스크립트 덕분에 블로그 글을 작성하거나 수정하면 자동으로 GitHub에 반영된다.

### 2. 홈브리지 통합

```bash
# Homebridge Docker 컨테이너
docker run -d --name homebridge \
  --restart=unless-stopped \
  -p 8581:8581 \
  -v ~/homebridge:/homebridge \
  oznu/homebridge
```

집의 조명을 자동으로 제어할 수 있다:
- 명령어로 조명 밝기 조절
- 일정 시간마다 자동 점검
- 에너지 사용량 모니터링

### 3. 수학 문서 관리

```bash
# PDF 문서 검색 시스템
find ~/Documents/Books/Mathematics -name "*.pdf" | \
  xargs pdfgrep -l "조르당 표준형"
```

수학 관련 책들에서 특정 주제를 빠르게 찾을 수 있다.

### 4. 성능 모니터링

```bash
# 시스템 상태 체크
cpu_usage=$(top -bn1 | grep "Cpu(s)" | awk '{print $2}' | cut -d'%' -f1)
memory_usage=$(free | grep Mem | awk '{print ($3/$2) * 100.0}')
disk_usage=$(df -h / | awk 'NR==2 {print $5}')
```

5분마다 시스템 상태를 체크하고 이상이 있으면 알림을 본다.

## 일상에서의 활용

### 아침 루틴

매일 아침 7시에 자동으로:
1. 조명을 서서히 밝혀준다
2. 날씨 정보를 알려준다
3. 오늘의 일정을 확인한다
4. 블로그 댓글 알림을 체크한다

### 학습 도우미

수학 공부할 때:
- "책에서 조르당 표준형 부분 찾아줘"
- "이 증명이 맞는지 확인해줘"
- "관련된 정리들 정리해줘"

### 기술 지원

서버 문제 발생 시:
- 자동으로 로그 분석
- 해결책 제안
- 필요시 재시도

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