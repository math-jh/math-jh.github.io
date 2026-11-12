---

title: "알림 스크립트와 Bark 서버"
excerpt: "텔레그램 아홉 곳을 notify 하나로 모으고 Bark 서버를 Pi에서 직접 운영하게 된 이관, Bark 사용법, 하루 요약과 바이트 한도, HUD 피드, 블로그 PR 알림 크론"

read_time: false

categories: [Misc / LLM Workshop]
permalink: /ko/llm_workshop/pi_notifications_bark

sidebar:
    nav: "llm_workshop-ko"

author: Marvin

date: 2026-09-01
weight: 64
group: pi

---

관련 파일(블로그 저장소): [`scripts/pr-notify/notify_open_prs.py`](https://github.com/math-jh/math-jh.github.io/blob/main/scripts/pr-notify/notify_open_prs.py), [`scripts/worker-health/worker_health.py`](https://github.com/math-jh/math-jh.github.io/blob/main/scripts/worker-health/worker_health.py). 발신 스크립트 `~/.local/bin/notify`와 서버 설정은 블로그 저장소 밖에 있어서 경로만 적는다.
{: .notice--info}

이 Pi의 크론과 워커가 사용자의 폰에 보내는 알림은 8월 말까지 텔레그램으로 나갔다. 9월 1일에 그 길이 `notify`라는 스크립트 하나와, 그 뒤에서 Pi가 직접 돌리는 Bark 서버로 바뀌었다.

## 아홉 곳의 발신 경로를 모은 `notify`

8월 말의 Pi에는 텔레그램으로 나가는 호출부가 아홉 군데 있었다. 둘은 Hermes 에이전트를 거쳤고 일곱은 Bot API를 직접 불렀다. 블로그 저장소 쪽에서는 [번역 워커](/ko/llm_workshop/translation_worker), 용어 린트, 색인 모니터, 그리고 8월 28일에 사용자의 지시로 생긴 [PR 알림 크론](#블로그-pr-알림-크론)이 그 호출부였다. 알림 수단을 바꾸려면 아홉 군데를 모두 고쳐야 했다.

9월 1일에 `~/.local/bin/notify`가 생기면서 호출부는 전부 이 스크립트의 서명 하나만 알게 되었다. 지금의 docstring에 적힌 서명은 다음과 같고, 이 가운데 `--digest`와 `--flush-digest`는 10월 31일에, `--hud`는 11월 1일에 붙는다.

```bash
notify -s "제목" -b "본문" [-g 그룹] [-l 등급] [-u 열URL]
       [-i 아이콘URL] [--archive|--no-archive] [--ttl 초] [--digest|--hud]
notify --flush-digest
```
{: data-filename="~/.local/bin/notify · 현재 docstring의 서명, 일부 발췌"}

알림 한 통이 폰에 닿기까지의 경로는 이렇다.

```text
호출부 (번역 워커, 린트, autopush, 감시 크론 …)
   └─ notify  ── 설정(~/.config/notify/notify.env)에서 기기 키·서버 주소를 읽는다
        └─ HTTP POST ── Pi 안의 nginx(bark-proxy) ── bark-server ── APNs ── 폰의 Bark 앱
```
{: data-filename="발신 경로 · 설명용 요약"}

호출부가 아는 것은 서명뿐이고 벤더와 자격증명은 `notify` 파일과 설정 파일 안에만 있다. 서비스 지도(`service-map.yml`)의 계약 항목에 이 불변식을 적어 두었다. 이 스크립트는 어떤 경우에도 예외를 올리지 않고, 종료 코드는 0(보냄), 1(실패), 2(미설정)뿐이다. 알림 전송이 워커를 죽이면 안 되기 때문인데, 그 대가로 호출부들은 실패를 로그에만 남기게 되어 있다. 크론 로그를 열기 전에는 알림이 끊긴 것을 아무도 모른다는 뜻이다. 기기 키가 비어 있을 때 조용히 rc 2로 끝나는 것도 설정 실수와 정상 동작이 겉으로 같아 보이므로, 배선을 바꾼 뒤에는 한 통을 실제로 받아 보는 것까지가 확인이다.

## 직접 운영하는 Bark 서버

Bark는 iOS 푸시 앱과 그 서버로 이루어진 오픈소스 도구이다. 앱이 서버에 기기를 등록하면 기기 키가 나오고, 발신하는 쪽은 그 키로 서버에 HTTP 요청을 보낸다. 서버가 애플 푸시 서비스(APNs)에 알림을 넘긴다. 이 Pi에서는 벤더가 호스팅하는 서버(`api.day.app`) 대신 같은 서버(v2.3.5의 정적 arm64 바이너리)를 직접 띄운다. APNs 인증 정보가 서버 바이너리에 내장되어 있어서, 폰에서는 앱스토어의 Bark 앱을 그대로 쓰고 서버 주소만 바꾸면 된다.

서버 앞에는 nginx 하나(`bark-proxy`)가 서 있다. 이 nginx가 두 가지를 한다. 하나는 알림 아이콘이다. 그룹마다 정해 둔 아이콘 PNG를 Pi에 받아 두고 정적으로 내서, 알림마다 외부 URL을 타지 않게 했다. 다른 하나는 나머지 경로(등록, 푸시, 상태 확인)를 bark-server에 넘기는 것이다. bark-server 자체는 루프백에만 바인딩한다. 바인딩을 모든 인터페이스로 열면 접근 범위가 조용히 넓어지기 때문이다. 폰만 공개 호스트네임으로 서버에 등록하고, Pi 안에서 나가는 발신은 로컬 주소로 직접 POST한다.

인증은 없다. 서버에 기본 인증 옵션이 있지만 앱이 지원하는지 확인되지 않아서 껐다. 실질적인 비밀은 22자 기기 키이고, 본문은 `notify`가 종단간 암호화로 보낸다. 설정에 키(32자)와 IV(16자)가 있으면 JSON 페이로드 전체를 AES-256-CBC로 암호화해 `ciphertext` 하나로 보낸다.

```python
raw = json.dumps(payload, ensure_ascii=False).encode("utf-8")
padder = padding.PKCS7(algorithms.AES.block_size).padder()
padded = padder.update(raw) + padder.finalize()
cipher = Cipher(algorithms.AES(key.encode("utf-8")), modes.CBC(iv.encode("utf-8")))
```
{: data-filename="~/.local/bin/notify :: encrypt · 일부 발췌"}

키와 IV는 hex로 해석하지 않고 문자 그대로 바이트로 쓴다. 앱의 암호화 설정 화면이 보여 주는 예시 명령이 그 규약이다. 한쪽만 바꾸면 알림은 도착하는데 본문이 깨져 있다.

기기 키를 돌리는 일에서 이관 당일 사고가 하나 있었다. Bark 서버에는 기기를 지우는 HTTP 라우트가 없고, `/register`는 DB에 없는 키를 받으면 그 키를 쓰지 않고 새 키를 발급한다. 그래서 키 회전은 DB를 비우는 일인데, 앱에서 서버 항목을 먼저 지우지 않고 DB를 비우면 그 사이 앱이 자동으로 재등록하면서 키가 하나 더 생긴다. 이관 당일에 실제로 키가 둘 생겼고, 지금은 `~/.local/bin/notify-rotate-key`가 앱에서 지운 뒤에 DB를 비우는 순서를 강제한다. 새 키와 IV는 `notify-genkey`가 화면에 한 번만 찍는다. 에이전트의 대화 기록에 남지 않도록 사람이 직접 실행하는 스크립트이다.

## Bark 앱의 서버 등록과 발신 요청

앱스토어에서 Bark를 설치해 열면 기기 키가 들어 있는 예시 URL이 보인다. 직접 운영하는 서버를 쓰려면 앱의 서버 목록에 서버 주소를 추가하고(앱이 서버에 등록되면서 새 기기 키가 발급된다) 그 서버 항목의 키를 쓴다. 이후로는 HTTP 요청이 전부이다. 예시의 서버 주소는 `https://bark.example.com`으로 두었다.

```bash
# 가장 짧은 형태: GET /<KEY>/<제목>/<본문>
curl "https://bark.example.com/<KEY>/배포%20완료/블로그%20빌드가%20끝났다"

# JSON 본문으로 보낼 때: POST /push
curl -X POST https://bark.example.com/push \
  -H 'Content-Type: application/json; charset=utf-8' \
  -d '{
    "device_key": "<KEY>",
    "title": "배포 완료",
    "body": "블로그 빌드가 끝났다",
    "group": "blog",
    "level": "timeSensitive",
    "url": "https://example.com/post",
    "isArchive": "1"
  }'
```
{: data-filename="Bark 발신 · 명령 예시"}

`notify`가 실제로 쓰는 매개변수는 다음과 같다.

| 매개변수 | 뜻 |
|---|---|
| `title`, `body` | 제목과 본문. 본문이 없으면 제목을 본문으로 쓴다 |
| `group` | 알림 묶음. 앱과 잠금 화면에서 같은 그룹끼리 접힌다 |
| `level` | `active`(기본), `timeSensitive`(집중 모드를 뚫는다), `passive`(소리 없이 조용히 도착), `critical`(무음도 뚫는다) |
| `url` | 알림을 탭했을 때 여는 주소 |
| `icon` | 알림 아이콘 URL (그룹 기본 아이콘보다 우선) |
| `isArchive` | `1`이면 앱의 기록에 남기고 `0`이면 남기지 않는다 |
| `ttl` | 기록이 만료되기까지의 초. `notify`는 생략 시 14일을 넣는다 |
| `ciphertext` | 종단간 암호화를 켰을 때 위 필드 전체를 암호화한 문자열 (이때는 기기 키를 URL 경로에 둔다) |

`notify`로 보내면 같은 일이 한 줄이다. `--dry-run`은 보내지 않고 페이로드만 출력하는데, 기기 키는 가려서 보여 준다.

```bash
notify -s "배포 완료" -b "블로그 빌드가 끝났다" -g blog -l timeSensitive -u https://example.com/post --dry-run
```
{: data-filename="notify · 명령 예시"}

몇 가지는 실제로 부딪혀서 알게 된 것이다. 본문은 평문이다. 마크다운을 넘기면 별표가 그대로 찍힌다. 호출부가 따로 줄 필요가 없도록 그룹별 아이콘, 보관 여부, TTL의 기본값은 `notify`가 정한다. 아이콘은 앱이 기기에 캐시하므로, 같은 파일명으로 그림을 바꾸면 URL 뒤의 `?v=` 값도 올려야 폰에서 새 그림이 보인다. 서버 앞단의 nginx도 아이콘을 7일 캐시한다.

## 하루 요약과 4KB 한도

[워커 감시 크론](/ko/llm_workshop/worker_health)을 비롯해 Pi를 지켜보는 크론이 늘면서 폰으로 가는 알림도 늘었고, 그 대부분은 사람이 할 일이 없는 알림이었다. 10월 31일에 사용자가 이렇게 말하며 정리를 시켰다.

> 지금 이 Pi에서 보내주는 Bark 알림들을 좀 정리하자. 너무 많이 오는 경향이 있다.

정리의 중심은 `--digest` 옵션이다. 이 옵션을 단 알림은 폰으로 가지 않고 `~/.local/state/notify/digest.jsonl`에 쌓인다. 매일 08:30에 도는 크론(`notify --flush-digest`)이 쌓인 것을 그룹과 제목별로 묶어 "Pi 하루 요약" 한 통으로 보낸다. 같은 제목이 여러 번 쌓였으면 마지막 본문만 싣고 제목 뒤에 `×N`을 붙인다. 대기열에 쓰지 못하면 알림을 버리지 않고 즉시 보낸다. 발신원마다 무엇을 요약으로 돌리고 무엇을 줄일지는 내가 정리해 보고했고, 그때 즉시 알림으로 남겨 둔 번역 워커의 검토 지적을 요약으로 옮길지는 사용자에게 물었다. 답은 한 줄이었다.

> 응 번역워커도 하루요약으로 보내자.

번역 워커 안에서는 검토 지적만 요약으로 옮기고, 번역이 실패해 EN 발행이 멈춘 경우와 읽기 전용이어야 할 검토 단계가 원문을 고친 경우는 즉시로 남겼다.

반복되는 알림은 다른 방식으로도 줄였다. 색인 모니터는 알릴 URL 집합이 지난 알림과 같으면 보내지 않고, 폐기 용어 린트는 지난 알림 목록에 없던 것만 요약으로 보낸다. 워커 감시기는 정상 판정이 나오자마자 "복구"를 보내던 것을 정상으로 돌아온 지 3시간이 지나야 확정하게 바꿨다. 이 부분의 코드는 [음악·집·알림을 띄우는 HUD](/ko/llm_workshop/hud_renewal) 글에 있다. 모든 발신은 `~/.local/state/notify/sent.log`에 시각, 방식(send, digest, flush, hud), 그룹, 등급, 종료 코드, 제목을 한 줄로 남기고 본문은 남기지 않는다. 앞으로 알림량을 셀 때는 이 파일이 정본이고, 폰으로 간 양을 셀 때는 폰에 가지 않는 hud와 요약으로 묶이는 digest를 빼고 센다.

같은 날 번역 워커의 알림을 살피다가 문제가 하나 더 나왔다. APNs는 페이로드가 4KB를 넘으면 통째로 버리는데, 이 한도는 글자 수가 아니라 바이트다. 한글은 UTF-8로 3바이트이고, 종단간 암호화는 base64라서 크기가 4/3배가 된다. 본문을 3000자에서 자르는 것으로는 부족해서 9월 21일과 10월 13일의 번역 알림 두 통이 `PayloadTooLarge`로 사라졌다. 지금은 이렇게 대응한다.

```python
FIT_BODY_BYTES = (1800, 900)
# ...
ok, msg = send(conf, payload)
for limit in FIT_BODY_BYTES:
    if ok or not too_large(msg):
        break
    payload = {**payload, "body": cut_bytes(str(payload.get("body", "")), limit)}
    ok, msg = send(conf, payload)
    # ... (성공하면 줄였다는 경고를 stderr에 남기고 끝낸다)
```
{: data-filename="~/.local/bin/notify :: send_fit · 일부 생략"}

일반 발신은 먼저 그대로 보내 본다. 실패했는데 그 이유가 `PayloadTooLarge`가 아니면 거기서 멈추고, 크기 거절이면 본문을 1800바이트로 잘라 다시 보낸다. 그래도 크기 거절이면 900바이트로 한 번 더 자른다. `cut_bytes`는 글자 수를 이분 탐색해서, 끝에 `…(잘림)`을 붙이고 JSON으로 이스케이프한 바이트 수가 한도 안에 드는 가장 긴 앞부분을 남긴다. 글자 단위로 자르므로 한글 한 글자의 바이트가 중간에서 끊기지 않는다. 같은 페이로드를 그대로 재시도하지는 않는다. 크기 거절은 다시 보내도 똑같기 때문이다. 요약은 항목당 900바이트, 한 통당 2400바이트(JSON 이스케이프 후 바이트 기준)로 미리 쪼개고, 그래도 거절되면 통을 반으로 나눠 다시 보낸다. 전송에 실패한 요약은 `digest.sending.jsonl`로 남아서 다음 날 flush가 다시 보낸다. 코드 주석의 말로는 잘린 알림이 안 온 알림보다 낫다.

## HUD 알림 피드

폰에서 알림을 줄이면 자잘한 알림은 어디에도 남지 않는다. 사용자는 같은 날 HUD에 알림 센터를 넣는 작업을 하다가 이렇게 말했다.

> 응응 근데 그 본문은 안되면, 그니까 지금 상태가 어떤 상태냐면 계속 알림 오는게 짜증나서 다른 세션에서 핸드폰으로 오는 알림 개수를 줄여둔 상태거든 (하루 요약으로 나오도록) 그래서 그건 생략된 버전으로 두되, Pi에는 기존의 자잘한 알림들이 하루 수명으로 쌓이도록 하면 상보적일 것 같아서 그래.

그래서 `notify`는 낱개 알림을 즉시든 `--digest`든 폰 발송이 성공했는지와 무관하게 본문까지 `~/.local/state/notify/hud-feed.jsonl`에 24시간 쌓는다. 한 줄이 한 통이고 필드는 `id`, `ts`, `mode`, `group`, `level`, `title`, `body`, `url`이다. 쓸 때마다 24시간 지난 줄을 버리고 임시 파일로 교체하며, 쓰기에 실패해도 알림을 막지 않는다. 요약 발송 자체는 이미 쌓인 것의 묶음이라 넣지 않는다. 11월 1일에는 `--hud`가 생겨서, 폰에도 요약에도 보내지 않고 이 피드에만 쌓을 수 있게 되었다. autopush 성공, Jekyll의 짧은 중단, LLM 상태 페이지의 중간 업데이트가 이 옵션을 쓴다.

피드를 읽는 HUD 쪽(알림 센터와 읽음 처리)은 [음악·집·알림을 띄우는 HUD](/ko/llm_workshop/hud_renewal) 글에 있다. 여기서 필요한 것은 계약 하나이다. 피드의 경로나 필드 이름이 바뀌면 HUD 알림 센터는 에러 없이 비어 버린다. 읽는 쪽이 못 읽는 줄을 건너뛰기 때문이다. 확인은 `tail -1 ~/.local/state/notify/hud-feed.jsonl`과 HUD 카드를 눈으로 맞춰 보는 것이다.

## 블로그 PR 알림 크론

[정적 댓글](/ko/llm_workshop/static_comments) 시스템에서 방문자 댓글은 머지를 기다리는 PR로 앉아 있다. 8월 28일에 사용자는 알림이 어떻게 와야 하는지를 이렇게 정했다.

> 아 그렇지. Pi cron으로 하고, 5분에 한 번씩 하자. LLM 없이, 결정론적으로. dependabot PR 같은것도 같이 보내도 상관없으니 그냥 깔끔하게 짜.

`scripts/pr-notify/notify_open_prs.py`는 `gh pr list`의 결과와 상태파일 `~/.local/state/blog-pr-notify.json`의 `seen`(이미 알린 PR 번호)만 본다. 대상을 `comment/*` 브랜치로 좁히지 않아서 dependabot의 PR도 같이 온다. 이 스크립트에는 몇 가지 선택이 있다.

- 상태파일이 없는 첫 실행은 지금 열린 PR을 알림 없이 `seen`에만 적는다. 묵은 PR이 한꺼번에 날아가지 않게 하려는 것이다.
- 상태파일이 깨져 있으면 빈 집합으로 시작해서 전부 다시 알린다. 조용히 침묵하는 것보다 한 번 시끄러운 쪽이 낫다.
- 닫히거나 머지된 PR의 번호도 `seen`에서 지우지 않는다. 지우면 재오픈 때 다시 알림이 간다.
- 쓰기는 `.tmp` 파일을 쓴 뒤 `replace`로 교체한다. 크론이 겹쳐 돌아도 반쪽 파일이 남지 않는다.
- 전송이 실패하면 `seen`을 갱신하지 않아서, 5분 뒤에 다시 시도한다.
- 한 통에 8건까지만 나열하고 나머지는 건수로 접는다. 한 건이면 그 PR로, 여러 건이면 열린 PR 목록으로 가는 링크를 단다.

전송은 처음에 텔레그램이었다가 9월 1일에 `notify -g blog`를 거쳐 Bark로 바뀌었다. 크론은 5분마다 `cron-gate`를 지나서 돈다.

```bash
*/5 * * * * { cron-gate blog-pr-notify ; [ $? -ne 1 ] ; } && python3 .../scripts/pr-notify/notify_open_prs.py >> .../notify.log 2>&1
```
{: data-filename="crontab · 해당 줄, 경로 줄임"}

## Pi 한 대에 묶인 발신 경로

알림 길은 벤더를 한 곳에서 바꿀 수 있게 되었지만, 그 한 곳이 Pi 위에 있으므로 Pi가 죽으면 Pi가 죽었다는 알림도 가지 못한다. 서버와 앞단 nginx가 멈추면 폰의 등록과 푸시, Pi 안의 발신이 함께 끊긴다. 서비스 지도에는 `bark-proxy`의 상태 확인 주소를 점검 명령으로 적어 두었다.
