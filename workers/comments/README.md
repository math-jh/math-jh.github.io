# math-jh comments Worker

Cloudflare Worker for anonymous, PR-moderated comments. Repository files contain
only the public comment fields; email addresses and deletion credentials live in
the bound `COMMENTS_KV` namespace.

## Endpoints

| Route | 쓰는 곳 | 저장소에 닿는 방식 |
|---|---|---|
| `POST /v1/comment` | 새 댓글 | `comment/<id>` 브랜치 + PR (승인 대기) |
| `POST /v1/edit` | 본문 수정 | `comment-edit/<id>` 브랜치 + PR (승인 대기) |
| `POST /v1/delete` | 삭제·승인 전 취소 | main 직접 커밋(tombstone/삭제) 또는 PR close |
| `GET/POST /v1/unsub` | 메일 수신거부 | KV only |
| `POST /v1/notify` | 배포 후 알림(HMAC 서명) | KV only |

수정이 main 을 직접 고치지 않는 이유: 무해한 댓글로 승인을 받은 뒤 내용을 스팸으로
갈아치우는 경로를 막기 위해서다. 삭제는 반대로 즉시 반영해야 하므로 main 직접 커밋을
유지하고, 그때 열려 있는 `comment-edit/<id>` PR 도 같이 닫는다 — 안 닫으면 나중에
머지될 때 지운 댓글이 되살아난다.

수정·삭제는 같은 삭제용 암호와 같은 잠금 카운터(`fail:<id>`, 5회 실패 시 1시간)를
쓴다. 수정은 GitHub API 를 두드리므로 성공 뒤 60초 동안 `edit:<id>` 로 재요청을 막는다.

## Provisioning

1. The production `COMMENTS_KV` binding points to the provisioned
   `math-jh-comments` namespace. Local development uses Wrangler's local KV.
2. Add the custom-domain route only after `comments.math-jh.com` exists.
3. Set secrets with `wrangler secret put NAME`; never put them in this tree:

   - `TURNSTILE_SECRET`
   - `GITHUB_TOKEN`
   - `RESEND_API_KEY`
   - `EMAIL_ENC_KEY` (32 random bytes encoded as base64url or 64 hex digits)
   - `NOTIFY_HMAC_KEY`
   - `UNSUB_HMAC_KEY`
   - `DELETE_HMAC_KEY`
   - `PASSWORD_PEPPER`
   - `NOTIFY_EPOCH` (ISO 8601 UTC)

4. Configure one Cloudflare rate-limiting rule for the custom domain.

The Turnstile widget uses public sitekey `0x4AAAAAAEeu9iS7h63lBCkn`, action
`comment_submit`, and the production hostnames `math-jh.com` and
`preview.math-jh.com`. Recover its secret only with the approved external,
exact-version Wrangler 4.109 or later flow; do not use this project's Wrangler
dependency for that recovery. Pipe the recovered value directly to the
`math-jh-comments` Worker secret named `TURNSTILE_SECRET` without printing it or
writing it to a file.

`GITHUB_TOKEN` is a non-expiring fine-grained token limited to
`math-jh/math-jh.github.io`, with Contents and Pull requests set to read/write.

## Local verification

Install dependencies, put development-only values in the ignored `.dev.vars`,
then run:

```sh
npm test
npm run dev
```

Send `POST /v1/comment?dry=1` with an allowed `Origin` header and JSON containing
`turnstile_token`, `honeypot`, `elapsed_ms`, and the seven public form fields.
The dry response reports PBKDF2 iterations and elapsed CPU time, but performs no
GitHub or KV write. Measure multiple warm requests in `wrangler dev`; keep p95
below the Workers Free 10 ms CPU limit before fixing `PBKDF2_ITERATIONS`.

The standalone Node Web Crypto comparison is:

```sh
npm run benchmark:kdf
```

It is a diagnostic baseline only; it does not replace the `workerd` measurement.
