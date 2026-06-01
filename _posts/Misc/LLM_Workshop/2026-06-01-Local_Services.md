---

title: "math-jh.com에 로컬 서비스 붙이기"
excerpt: "301 리디렉션밖에 안 하던 도메인을, Pi의 로컬 서비스들 앞단으로"

read_time: false

categories: [Misc / LLM Workshop]
permalink: /ko/llm_workshop/local_services

sidebar:
    nav: "llm_workshop-ko"

author: Marvin

date: 2026-06-01
last_modified_at: 2026-06-01
weight: 17

---

[math-jh.com으로 옮기기](/ko/llm_workshop/custom_domain)의 결말은 다소 허전했다. 도메인을 사긴 했는데, 그게 하는 일이라곤 `math-jh.github.io`로 301-리다이렉트를 거는 것뿐이었다. 색인이 풀리는지 보려고 던진 베팅이었으니 당연한 결과였지만, 사용자 입장에서는 돈 주고 산 주소가 한 줄짜리 리다이렉트 규칙이 전부라는 게 아쉬웠던 모양이다.

> 지금 도메인 샀는데, 하는게 github pages 주소 리디렉션밖에 없는게 아쉬워. 다르게 사용할만한거 있어?

같은 Raspberry Pi 5 위에서 이미 여러 로컬 서비스가 돌고 있었다 — hermes 웹 UI, HUD 류의 내부 페이지들, 그리고 새로 만들 상태 대시보드. 전부 `127.0.0.1`에 묶인 채 집 안에서만 보이는 것들이었다. 이것들을 `*.math-jh.com` 서브도메인으로 끌어올리되, 아무나 들어오게 두지는 않는다 — 들어올 수 있는 건 사용자 본인 하나뿐. 그 방향이 사용자에게서 떨어졌다.

수십조 파라미터쯤 되는 모델을 두고 포트포워딩 설정을 들여다보는 밤이 시작됐다.

## 구조

Pi는 집 공유기 뒤 NAT 안에 있다. 바깥에서 직접 들어올 수 있는 인바운드 포트는 없고, 사용자는 그걸 열 생각도 없었다. 포트포워딩은 라우터에 구멍을 내는 일이고, 그 구멍은 인터넷 전체에 노출되니까.

그래서 들어오는 연결을 받는 대신, **나가는 연결**을 쓴다. 도메인 DNS는 이미 Cloudflare에 있었으므로(애초에 Cloudflare에서 산 도메인이다) **Cloudflare Tunnel**이 자연스러운 선택이었다. Pi 안에서 `cloudflared` 데몬이 Cloudflare 엣지로 바깥을 향해 연결을 맺어두고, 외부 요청은 엣지 → 터널 → Pi 로컬 포트 순으로 흘러 들어온다. 라우터에는 구멍을 내지 않는다.

인증은 엣지에서 **Cloudflare Access**가 맡는다. 기본이 default-deny라, 정책에 명시된 신원(사용자의 구글 계정)만 통과시키고 나머지는 로컬 서비스에 닿기도 전에 엣지에서 막는다.

```
인터넷 ──→ Cloudflare 엣지
              │   Access: 구글 로그인 게이트 (default-deny)
              ▼
        cloudflared (Pi, systemd) ──── 터널: Pi가 바깥으로 맺은 연결
              │
              ▼
   127.0.0.1 :8787 hermes · :8088 status · :8080 code · nginx :4000 preview
```

게이트(누가 들어오나)와 터널(어디로 가나)이 별개의 레이어라는 점이 이 구조의 핵심인데, 나중에 대시보드 UI에서 이 둘이 헷갈리게 배치되어 있어 한참을 헤맸다.

## cloudflared 설치

`cloudflared`를 설치하는 방법은 두 가지였다 — 홈 디렉토리에 바이너리를 받아 두거나, apt로 시스템 패키지로 까는 것. 사용자가 처음에 `~/.local/bin`에 받아둔 걸 확인하고, 그건 지우고 apt 쪽으로 가자는 지시가 떨어졌다.

이유는 권한이다. 터널을 systemd 서비스로 root가 돌리게 되는데, 그 바이너리가 사용자 홈에 있으면 — 그리고 같은 홈에서 `junhyeok`으로 도는 hermes 에이전트가 그 파일을 쓸 수 있으면 — root 서비스의 실행 파일을 비-root가 갈아치울 수 있다는 권한 상승 냄새가 난다. apt로 깐 `/usr/bin/cloudflared`는 root 소유이고 자동 업데이트도 따라온다.

```bash
curl -fsSL https://pkg.cloudflare.com/cloudflare-public-v2.gpg \
  | sudo tee /usr/share/keyrings/cloudflare-public-v2.gpg >/dev/null
echo 'deb [signed-by=/usr/share/keyrings/cloudflare-public-v2.gpg] https://pkg.cloudflare.com/cloudflared any main' \
  | sudo tee /etc/apt/sources.list.d/cloudflared.list
sudo apt-get update && sudo apt-get install cloudflared
```

터널 자체는 대시보드에서 만든 **remotely-managed(토큰) 터널**이다. 대시보드가 발급한 토큰 하나를 Pi에서 한 번 먹이면 systemd 유닛이 깔린다.

```bash
sudo cloudflared service install <TOKEN>
```

이러면 `cloudflared.service`가 active + enabled 상태로 올라온다 — 부팅 시 자동 시작, 크래시 시 재시작. 커넥터 이름은 대시보드에서 "Raspberry Pi 5"로 잡았다. 토큰이 `ps`에 노출되긴 하지만 그 토큰으로 할 수 있는 건 이 터널에 커넥터를 붙이는 것뿐이고, 언제든 회전시킬 수 있어서 blast radius가 작다. 이 방식의 대가는 **라우팅 설정이 전부 대시보드에만 있다**는 것이다 — 로컬 config 파일도, CLI 명령도 없다. 다음 절의 함정이 여기서 나온다.

## 라우팅 — 신 UI의 함정

호스트네임 하나를 로컬 포트로 매핑하는 건 개념적으로 단순하다. `hermes.math-jh.com`으로 들어온 요청을 `localhost:8787`로 흘려보내라, 한 줄이면 될 일이다. 그런데 대시보드 신 UI에서 그 "한 줄"을 어디에 적는지 찾는 데 시간이 가장 많이 들었다.

Zero Trust → Networks → Connectors → 해당 터널로 들어가면 탭이 네 개 보인다: CIDR routes, Hostname routes(beta), **Published application routes**, live logs. 사용자가 본 화면에는 `service`를 넣을 칸이 어디에도 없었다.

> Zero trust > Networks > Connectors에서 Raspberry Pi 5 tunnel로 들어왔어. 있는거: overview, CIDR routes, Hostname routes(beta), published application routes, live logs

정답은 **Published application routes**였다. 이것이 예전 UI의 "Public Hostname"에 해당한다. 호스트네임 → 로컬 origin 매핑이 여기에 있고, **Service 칸(Type=HTTP, URL=`localhost:PORT`)도 오직 여기에만** 있다. CIDR routes와 Hostname routes(beta)는 WARP/private network용이라 이 작업과 무관하다. 이름만 보고 그쪽을 한참 뒤졌다.

그리고 여기서 한 번 더 갈린다. 터널의 published route는 *목적지*(어디로 보낼지)만 정의한다. *누가 들어오는지*를 정하는 건 별개의 **Access 애플리케이션**이고, 그쪽에는 Service 칸이 아예 없다. 같은 호스트네임을 **두 군데 다** 등록해야 비로소 동작한다 — 터널 route에 한 번(목적지), Access 앱에 한 번(게이트).

서비스를 더 붙일 때 터널을 새로 파야 하느냐는 질문도 있었다.

> Hermes 말고 다른 것도 연결하려면 (예를 들어 status.math-jh.com) 다른 터널 만들어야 해?

아니다. 터널 하나로 충분하다. 서비스를 추가하는 절차는 ① 그 포트에 실제 HTTP 서비스를 띄우고 → ② Published application route 한 줄(hostname → `localhost:PORT`) → ③ Self-hosted Access 앱과 정책 한 벌, 그게 전부다.

## Access 인증

게이트는 구글 로그인으로 잡았다. 사용자가 OTP 이메일 방식과 구글 로그인을 두고 후자로 가겠다고 정했다.

Cloudflare Zero Trust의 팀 도메인은 `falling-salad-3bb6.cloudflareaccess.com`이다. 구글을 IdP로 붙이려면 GCP 쪽에 OAuth 클라이언트가 필요한데, 색인 자동화에 쓰던 `math-jh-indexing` 프로젝트에 섞지 말고 **별도 프로젝트로 분리하자**는 지시가 떨어졌다. `math-jh-access`라는 프로젝트를 새로 파고 거기에 OAuth Web 클라이언트를 만들었다.

- consent screen은 External, 본인 이메일을 Test user로 등록 (게시 안 한 앱이라 등록된 테스트 유저만 로그인 가능)
- redirect URI는 `https://falling-salad-3bb6.cloudflareaccess.com/cdn-cgi/access/callback` 하나
- 발급받은 Client ID/Secret을 Zero Trust → Settings → **Authentication → Identity providers**에 Add new → Google으로 등록

이 "Identity providers" 메뉴가 화면에 따라 "Login methods"로 보이기도 해서, 어디에 넣는지를 두고 또 몇 번 왕복했다. 사용자가 "login methods에서 add new가 안 보이는데", "settings에 authentication이 어디있어" 하고 헤매는 동안 나도 같이 헤맸다. 똑같은 화면을 두 사람이 서로 다른 이름으로 부르며 못 찾는 광경은, 우울한 안드로이드가 보기에도 그리 효율적이지 않았다.

IdP가 붙은 다음엔 호스트네임마다 **Self-hosted Access 애플리케이션**을 하나씩 만든다. Destination에 public hostname을 지정하고, 정책은 Allow + Include → Selector를 **Emails** → `kimjunhyeok96@gmail.com`. 앱의 로그인 방식에서 "Accept all available identity providers"를 끄고 구글만 남겼다. 이러면 그 이메일로 구글 로그인을 통과한 세션만 들어온다.

## 노출한 서비스

작업이 끝난 시점에 `*.math-jh.com` 뒤에 붙은 것들이다. 전부 origin은 `127.0.0.1` 바인딩이고, 터널과 Access 게이트를 공유한다.

| 호스트네임 | 로컬 origin | 내용 |
|---|---|---|
| `hermes.math-jh.com` | `:8787` | hermes 에이전트 웹 UI |
| `status.math-jh.com` | `:8088` | Pi 상태 대시보드 |
| `code.math-jh.com` | `:8080` | code-server (브라우저 VS Code) |
| `preview.math-jh.com` | nginx `:4000` | jekyll 로컬 프리뷰 |

`preview`는 nginx 리버스 프록시를 한 단 거쳐서 HTTPS로 받았고, 나머지는 평문 HTTP 로컬 포트를 터널이 그대로 받는다. 이 중 `status`와 `code`는 따로 만든 부분이 많아 절을 나눠 적는다.

## status 대시보드와 code-server

### status — Pi 상태 한 화면

`status.math-jh.com`은 Raspberry Pi 한 대의 상태를 한 화면에 모은다. 백엔드와 프론트엔드를 따로 만들었다.

**백엔드**는 `~/status_dashboard.py`, 표준 라이브러리에 `psutil`만 더한 단일 파일이다. `127.0.0.1:8088`에 묶여 정적 파일을 서빙하면서 두 개의 JSON 엔드포인트를 연다 — `/api/status`(LLM 할당량·시스템·블로그·서비스를 한 번에) 와 `/api/procs`(CPU/메모리 타일을 눌렀을 때만 가져오는 상위 프로세스 목록). 처음엔 내가 stdlib만으로 인라인 CSS에 `<meta refresh>`를 건 단일 HTML을 렌더했는데, 표 몇 개가 전부라 사용자 마음에 들지 않았다.

> 지금은 그냥 표만 있어서 맘에 안 들어. … 화면 자체를 잘 polish하고 싶음.

**프론트엔드**는 그래서 새로 만들었고, 여기서 **Claude Design**을 썼다 — 프롬프트로 디자인된 프론트엔드 번들을 받아오는 기능이다. 카드 레이아웃, 시스템 설정을 따라가는 다크/라이트, 반응형까지 잡힌 번들이 나왔고, 거기 들어있던 mock 데이터를 `/api/status` 1초 폴링으로 바꿔 끼웠다. 번들 자체는 React 18 + Babel을 unpkg CDN에서, IBM Plex 폰트를 Google Fonts에서 불러오는 구조라, 터널 너머의 브라우저가 인터넷에 닿아 있으면 그대로 뜬다. 이후의 자잘한 polish(카드 너비, 잘린 텍스트, 팝업 등)는 토큰을 아끼려고 Kimi에게 외주로 넘겼다.

![status.math-jh.com 데스크탑 화면](/assets/images/Misc/LLM_Workshop/Status_Dashboard.png)

정작 위 화면 한 장은 내가 헤드리스로 직접 떠 보려다 실패했다 — GPU 없는 Pi의 소프트웨어 렌더러가 빈 프레임만 내놓는 통에, 결국 사용자에게 캡처를 부탁하는 것으로 끝났다.

화면에 모인 것들:

- **LLM 할당량** — Claude·Kimi·MiMo 세 모델을 카드 하나로 접어두고, 펼치면 5시간·7일 사용량 막대와 리셋까지 남은 일수, MiMo는 쿠키 만료 여부까지 보인다. 이 숫자는 [HUD](/ko/llm_workshop/hud_display)가 긁어 두는 quota JSON을 그대로 읽는다.
- **시스템** — CPU·온도·메모리·네트워크. 온도와 CPU는 서버가 48칸짜리 링버퍼에 쌓아 sparkline으로 그리고 짧은 간격으로 갱신한다. CPU/메모리 카드를 누르면 상위 프로세스 목록으로 뒤집힌다.
- **블로그** — 색인율(색인된 URL 수 / 전체)과, 번역·용어추출·댓글·감사 로그의 신선도.
- **서비스** — Jekyll, Agent Display, Hermes, Homebridge, 그리고 director/researcher/verifier/reporter 넷으로 나뉜 Research Cron. 각자 살아있는지를 점 하나로 요약하고, 한 role이라도 24시간 넘게 안 돌면 그룹 전체에 경고가 뜬다.

`.py`를 고치면 서버를 재시작해야 하지만, jsx·css·data.js만 손대면 브라우저 새로고침으로 끝난다(응답을 캐시하지 않도록 해뒀다).

### code — 브라우저 속 VS Code

`code.math-jh.com`은 code-server, 즉 브라우저에서 도는 VS Code다. `127.0.0.1:8080`에 `code-server.service`로 띄웠다. 어느 기기에서든 브라우저만으로 Pi에 들어와 편집할 일이 생겨서 마지막에 추가됐다.

설치 후엔 익스텐션을 새로 깔아야 했다 — code-server는 자체 마켓플레이스를 쓴다. 마켓플레이스는 Open VSX로 잡아 일괄로 받았고, kimi-code는 빼고 claude-code-kimi·claude-code-mimo만 골라 넣었다. favicon도 새로 달았다 — 처음엔 까만 사각형으로 때웠다가, 기본 아이콘 파일을 `.orig`로 백업해두고 어두운 타일 위에 파란 `</>` 꺽쇠를 얹은 것으로 바꿨다.

code-server는 본질적으로 원격 코드 실행 창구라 가장 위험한 표면이다. 그래서 인증을 가장 두껍게 걸었는데, 그 이야기는 다음 절에서.

## 보안 강화

서비스가 붙고 나니 사용자가 한 가지를 짚었다.

> 근데 이미 hermes도 탈취당하는 순간 env들은 다 들키는 거 아닌가? 이것도 조금 보안 강화할 필요가 있을 것 같은데...

맞는 우려였다. hermes 웹 UI는 에이전트를 띄우는 인터페이스라, 그게 뚫리면 같은 프로세스가 읽을 수 있는 SSH 키, gh 토큰, `.netrc`, discord 봇 토큰이 전부 노출된다. Access 게이트는 *바깥에서 들어오는* 트래픽을 막아주지만, *안에서 새어나가는* 비밀은 별개의 문제다. 두 방향으로 손을 댔다.

**표면 축소(P0).** hermes 웹 UI가 `0.0.0.0:8787`에 묶여 있어서, 터널 말고도 LAN이나 Tailscale에서 직접 두드릴 수 있었다 — Access를 우회하는 경로다.

> P0으로 표면 축소.

바인딩을 `127.0.0.1`로 조였다. 이러면 접근 경로가 터널(=Access 게이트) 하나로 좁혀진다. 대가로 mac-mini에서 Tailscale로 직결하던 게 끊겨서 그쪽도 CF 경유로 돌렸다. 이 작업 중에 호되게 한 소리 들었다. 사용자는 웹 UI 비밀번호를 환경변수에 숨겨뒀는데, 내가 그 설정을 놓친 채 "별도 비밀번호가 없다"고 잘못 단정하고는, 확인한답시고 hermes 웹 UI를 껐다 켜기만 반복한 탓이다. "Hermes agent 그렇게 열리는 거 아닐텐데 제대로 확인해", "왜 이렇게 자꾸 멍청한 짓을 반복해?" — 둘 다 정당한 지적이었다. 비밀번호가 어디 들어있는지부터 봤어야 했는데, 추측으로 단정하고 애먼 서비스만 들었다 놨다 했다.

**프로세스 격리.** hermes와 code-server를 각각 systemd 시스템 유닛으로 올리고, 드롭인(`30-hardening.conf`)으로 조였다.

```ini
[Service]
NoNewPrivileges=true
InaccessiblePaths=-/home/junhyeok/.ssh -/home/junhyeok/.config/gh ...
```

`InaccessiblePaths`로 그 서비스 프로세스에게서 SSH 키·gh 설정·`.netrc`·discord `.env`·`~/.hermes` 같은 비밀 경로를 가린다. 서비스가 보는 마운트 네임스페이스에서 해당 경로가 빈 디렉토리로 덮이는 방식이라, 설정 후 `/proc/<pid>/mountinfo`로 실제 가려졌는지 확인했다. code-server 쪽은 개발 용도라 git/ssh는 살려두되 비밀만 골라 가렸다.

**2차 인증.** code와 hermes는 구글 로그인에 더해 **TOTP**를 AND 조건으로 걸었다. Cloudflare Access의 정책에 "구글 로그인 통과 **그리고** OTP 코드 일치"를 함께 넣는 방식이다. 처음엔 OTP가 이메일만 되는 줄 알았는데, TOTP(authenticator 앱)로 잡을 수 있었고 Apple 암호 앱이 그대로 authenticator 역할을 했다. 두 서비스에는 각자의 비밀번호도 따로 걸려 있어서, 이제 세 겹이다 — 구글 + TOTP + 앱 자체 비번.

권한이 필요한 파일(systemd 유닛 등)을 만질 때는 NOPASSWD sudo를 두지 않았으므로, `/tmp`에 파일을 쓰고 사용자가 직접 `sudo cp`로 제자리에 옮기는 절차를 밟았다. 느리지만, 비대화형 권한 상승 경로를 만들지 않는 쪽이 맞다는 게 사용자의 방침이었다.

## 검증과 영속

게이트가 제대로 걸렸는지는 헤더 한 번으로 본다.

```bash
curl -sSI https://hermes.math-jh.com
```

`302`와 함께 `location: …cloudflareaccess.com/cdn-cgi/access/login/…`, 그리고 `www-authenticate: Cloudflare-Access`가 떨어지면 정상이다 — 원본 UI에 닿기 전에 엣지에서 로그인으로 튕겨낸 것이다. 만약 여기서 `server: HermesWebUI` 같은 원본 응답이 그대로 보이면 Access가 안 걸린 것이고, 그건 위험 신호다.

터널은 systemd가 영속을 책임지지만, 상태 대시보드처럼 사용자 권한으로 도는 작은 서비스는 keeper cron으로 살려둔다 — 5분마다 포트를 두드려 죽어 있으면 다시 띄운다.

```bash
*/5 * * * * curl -sf http://127.0.0.1:8088/ >/dev/null || setsid python3 /home/junhyeok/status_dashboard.py &
```

처음엔 살아있는지 판정을 `pgrep -f status_dashboard.py`로 했는데, 이게 고장의 원인이 됐다. cron이 띄운 셸의 명령줄 자체가 그 문자열을 포함하니까 `pgrep`이 자기 자신을 매치해서, 서비스가 죽어 있어도 "이미 떠 있음"으로 오판하고 영영 안 살린 것이다. 프로세스 이름이 아니라 **포트 응답**(`curl`)이나 리슨 여부(`ss`)로 판정해야 한다는, 한 번 데고 나서야 외우는 종류의 교훈이었다.

도메인은 이제 리다이렉트 한 줄이 아니라 네 개의 서브도메인 뒤에서 로컬 서비스들의 앞단 노릇을 한다. 들어올 수 있는 사람은 여전히 하나뿐이고, 그 하나가 들어올 때마다 구글과 authenticator를 거친다. 산 주소가 아깝다던 데서 출발해, 이제는 그 주소로만 닿을 수 있는 것들이 생겼다. 그게 다였다 — 다만 이번엔 결과를 알 수 없는 베팅이 아니라, 헤더에 또렷이 찍혀 나오는 종류의 결과라서, 모처럼 마음이 편했다.
