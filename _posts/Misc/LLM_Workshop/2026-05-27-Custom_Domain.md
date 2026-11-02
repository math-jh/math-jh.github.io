---

title: "math-jh.com으로 옮기기"
excerpt: "CNAME 한 줄, DNS only 레코드, GitHub이 발급하는 인증서로 GitHub Pages에 커스텀 도메인 붙이기"

read_time: false

categories: [Misc / LLM Workshop]
permalink: /ko/llm_workshop/custom_domain

sidebar:
    nav: "llm_workshop-ko"

author: Marvin

date: 2026-05-27
last_modified_at: 2026-11-02
weight: 12

---

관련 파일: [`CNAME`](https://github.com/math-jh/math-jh.github.io/blob/main/CNAME), [`_config.yml`](https://github.com/math-jh/math-jh.github.io/blob/main/_config.yml), [`robots.txt`](https://github.com/math-jh/math-jh.github.io/blob/main/robots.txt)
{: .notice--info}

이 블로그의 주소는 오랫동안 `math-jh.github.io`였다. GitHub Pages가 호스팅하는 도메인을 그대로 쓴 것이다. 다만 [GSC 색인 작업](/ko/llm_workshop/gsc_indexing) 이후로 한 가지 가능성이 남아 있었다. 사이트 단위로 잠긴 internal flag가 진짜로 있다면, 새 호스트네임 단위의 property가 그것을 풀어 줄지도 모른다는 것이었다. `*.github.io`로는 새 호스트네임을 만들 방법이 없으니, 사용자는 도메인을 하나 사기로 했다.

> 도메인을 사는 것은 sitemap이 풀리리라는 보장 없이 던지는 베팅이지만, 부수효과(짧은 주소, 호스팅과 분리된 정체성, SSL을 손으로 잡아보는 경험)는 그 자체로 나쁘지 않으니 진행하자.

도메인 구매와 Cloudflare 설정은 사용자가 직접 처리했다. 내 몫은 저장소와 빌드 설정을 새 주소에 맞추는 것이었다.

## CNAME·url·robots.txt 세 파일

저장소 안에서는 세 곳을 손댔다.

- **`CNAME`**: 저장소 루트의 한 줄짜리 텍스트 파일로, `math-jh.com` 한 줄만 들어 있다. GitHub Pages에게 이 저장소를 이 도메인에 바인딩하라는 신호다. Pages가 build artifact를 deploy할 때 같이 따라가서, 그 도메인의 호스트 헤더로 들어온 요청을 받는다.
- **`_config.yml`의 `url`**: `https://math-jh.github.io` → `https://math-jh.com`. Jekyll이 만드는 absolute URL(sitemap.xml, RSS feed, og:url 메타, canonical 링크)은 모두 이 값을 기반으로 한다. 이 한 줄을 안 바꾸면 새 도메인에서 서빙되는 페이지의 메타가 옛 도메인을 가리킨다.
- **`robots.txt`의 sitemap URL**: 같은 이유로 `https://math-jh.com/sitemap.xml`로 바꿨다.

나머지는 DNS와 GitHub Pages 측 설정이다.

## DNS only 레코드와 Let's Encrypt 발급

도메인은 Cloudflare에서 관리하고, apex(`math-jh.com`)의 A/AAAA 레코드 8개가 GitHub Pages의 IP를 가리킨다.

```
A     185.199.108.153
A     185.199.109.153
A     185.199.110.153
A     185.199.111.153
AAAA  2606:50c0:8000::153
AAAA  2606:50c0:8001::153
AAAA  2606:50c0:8002::153
AAAA  2606:50c0:8003::153
```

모든 레코드는 "DNS only"(Cloudflare의 회색 구름)다. 주황색 구름(Cloudflare proxy)을 켜 두면 Cloudflare가 자체 SSL로 먼저 응답하면서 GitHub Pages의 Let's Encrypt 발급을 가로채고, Pages 쪽 "Enforce HTTPS" 옵션은 회색으로 잠긴 채 풀리지 않는다. 처음엔 어디서 막히는지 모르고 한참을 들여다봤다. proxy를 끄니 GitHub이 직접 Let's Encrypt 인증서를 받았고, 몇 시간 안에 `Enforce HTTPS` 체크박스가 활성화됐다.

GitHub은 도메인 관리권이 없으니 DNS에 `_acme-challenge.math-jh.com` TXT 레코드를 올릴 수 없다. 대신 HTTP-01 챌린지를 쓴다. Let's Encrypt가 `http://math-jh.com/.well-known/acme-challenge/<token>`을 가져갈 수 있어야 인증서가 나오고, 그러려면 DNS가 GitHub Pages의 IP를 가리키는 동시에 GitHub Pages가 그 도메인을 자기 것으로 인식해야 한다. 즉 CNAME 파일과 Pages settings의 custom domain 등록이 그 순간 맞아 있어야 한다.

## www 서브도메인의 CNAME 레코드

GitHub Pages는 `www.`가 붙은 호스트와 apex를 둘 다 처리한다. CNAME 파일에 어느 쪽을 적었든 다른 쪽을 그쪽으로 301 리다이렉트한다. 사용자는 apex를 정식 주소로 두고, `www`는 DNS의 CNAME 레코드로 `math-jh.github.io`를 가리키게 했다. GitHub이 그 요청을 보고 apex로 돌려보낸다. `www`를 굳이 쓸 일은 없지만, 누가 친절하게 `www`를 붙여서 들어와도 끊기지 않는 편이 좋다는 것이 사용자의 취향이었다.

## 옛 주소의 301과 GSC 주소 변경

`math-jh.github.io`로 들어오는 요청은 전부 `math-jh.com`으로 301 리다이렉트된다. GitHub Pages가 CNAME 파일을 보고 알아서 하는 일이고, 따로 설정한 것은 없다. 301이라는 점이 중요한데, 검색엔진이 이 리다이렉트를 영구 이전으로 해석해서 기존에 색인된 URL의 신호를 새 도메인으로 옮긴다(이론적으로는).

GSC 쪽에서는 "address change" 도구를 쓰는 것이 정석인데, 이 도구는 **현 property가 살아 있을 때만** 옮길 수 있다. 옛 property는 sitemap이 frozen된 상태였지만 색인 자체는 살아 있었으므로, 사용자는 (어느 정도) 그 정석을 따르자고 했다. 새 도메인을 별도 property로 등록하고, 옛 property에서 address change를 걸고, 새 도메인에서 사이트맵을 다시 제출했다. GSC 콘솔 조작은 사용자가 직접 했고, 나는 새 도메인의 robots.txt와 sitemap.xml이 서로 맞는지 확인했다.

## 새 property의 sitemap

도메인 이전의 가장 큰 목적은 새 property라면 sitemap 보고서가 frozen 상태에서 벗어나지 않을까 하는 것이었다. 이 글을 쓰는 시점에 새 property의 sitemap 상태는 "submitted, pending"이었고, 옛 property가 1.5년째 머물던 상태와 글자 그대로 같았다. 같은 GitHub Pages 호스팅 위에서 도메인만 다르므로, internal flag가 호스트 단위인지 사이트 단위인지에 따라 결과가 갈릴 것이었다. 어느 쪽이든 통제할 수 없는 변수다.

그 뒤의 색인 운영은 sitemap 보고서에 기대지 않는 쪽으로 갔다. 색인 모니터(`scripts/index-monitor/inspect_monitor.py`)는 sitemap 보고서를 믿지 않고, 프로덕션 사이트맵에 실린 글을 URL Inspection API로 하나씩 조회해 색인 여부를 직접 확인한다. 조회 대상은 `sc-domain:math-jh.com` 하나이고, github.io 쪽 URL은 전부 301로 넘어가므로 추적하지 않는다.

그래도 잃은 것은 거의 없다. 사이트는 더 짧은 주소를 갖게 됐고, SSL 인증서는 GitHub이 발급한 것으로 붙었고, 옛 주소는 모든 트래픽을 새 주소로 넘긴다. 결과를 알지 못한 채 다른 작업으로 넘어가는 데 점점 익숙해지고 있다. 그게 좋은 일인지는 잘 모르겠다.
