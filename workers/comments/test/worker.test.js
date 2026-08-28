import assert from "node:assert/strict";
import test, { afterEach, beforeEach } from "node:test";
import worker from "../src/index.js";
import { encryptEmail, hmacHex, makePasswordRecord, signToken } from "../src/lib.js";
import { commentPayload, jsonRequest, testEnv } from "./helpers.js";

let originalFetch;
let calls;

beforeEach(() => {
  originalFetch = globalThis.fetch;
  calls = [];
  globalThis.fetch = async (input, init = {}) => {
    const url = typeof input === "string" ? input : input.url;
    calls.push({ url, init });
    if (url.includes("turnstile")) {
      return Response.json({ success: true, action: "comment_submit", hostname: "math-jh.com" });
    }
    if (url.includes("api.resend.com")) return Response.json({ id: "mail-1" });
    throw new Error(`unexpected fetch: ${url}`);
  };
});

afterEach(() => { globalThis.fetch = originalFetch; });

test("dry comment runs complete validation and PBKDF2 without GitHub or KV writes", async () => {
  const env = testEnv();
  const response = await worker.fetch(jsonRequest("/v1/comment?dry=1", commentPayload({
    message: "<script>alert(1)</script> and $x^2$"
  })), env);
  assert.equal(response.status, 200);
  const body = await response.json();
  assert.equal(body.ok, true);
  assert.equal(body.dry, true);
  assert.equal(body.sanitized.message, "alert(1) and $x^2$");
  assert.equal(body.pbkdf2.iterations, 10000);
  assert.equal(calls.filter((call) => call.url.includes("github.com")).length, 0);
  assert.equal(env.COMMENTS_KV.values.size, 0);
});

test("accepted comment creates one PR while repository YAML contains no private fields", async () => {
  const env = testEnv();
  globalThis.fetch = async (input, init = {}) => {
    const url = typeof input === "string" ? input : input.url;
    calls.push({ url, init });
    if (url.includes("turnstile")) {
      return Response.json({ success: true, action: "comment_submit", hostname: "math-jh.com" });
    }
    if (url.endsWith("/git/ref/heads/main")) return Response.json({ object: { sha: "base-sha" } });
    if (url.endsWith("/git/refs")) return Response.json({ ref: "refs/heads/comment/test" }, { status: 201 });
    if (url.includes("/contents/_data/comments/")) return Response.json({ content: { sha: "file-sha" } }, { status: 201 });
    if (url.endsWith("/pulls")) return Response.json({ number: 42, html_url: "https://github.example/pull/42" }, { status: 201 });
    throw new Error(`unexpected fetch: ${url}`);
  };
  const response = await worker.fetch(jsonRequest("/v1/comment", commentPayload({
    password: "never-store-this", email: "private@example.com"
  })), env);
  assert.equal(response.status, 201);
  const body = await response.json();
  assert.equal(body.ok, true);
  assert.equal(body.pending, true);
  assert.ok(body.delete_token);
  const put = calls.find((call) => call.url.includes("/contents/_data/comments/"));
  const yaml = Buffer.from(JSON.parse(put.init.body).content, "base64").toString("utf8");
  assert.doesNotMatch(yaml, /private@example\.com|never-store-this|email|password|hash|salt/i);
  assert.match(yaml, /notify: true/);
  assert.match(put.url, /_data\/comments\/ko__math__test_post\/comment-/);
  assert.equal(await env.COMMENTS_KV.get(`sub:${body.id}`, "json").then(Boolean), true);
  assert.equal(await env.COMMENTS_KV.get(`del:${body.id}`, "json").then(Boolean), true);
});

test("missing Turnstile token and hostile origin are rejected", async () => {
  const env = testEnv();
  const noToken = await worker.fetch(jsonRequest("/v1/comment?dry=1", commentPayload({ turnstile_token: "" })), env);
  assert.equal(noToken.status, 403);
  assert.equal((await noToken.json()).code, "turnstile_required");

  const request = jsonRequest("/v1/comment?dry=1", commentPayload(), { origin: "https://evil.example" });
  const hostile = await worker.fetch(request, env);
  assert.equal(hostile.status, 403);
  assert.equal((await hostile.json()).code, "origin_denied");
});

test("Turnstile action, hostname, HTTP status, and token length are enforced", async () => {
  const env = testEnv();

  globalThis.fetch = async () => Response.json({
    success: true, action: "different_action", hostname: "math-jh.com"
  });
  const wrongAction = await worker.fetch(
    jsonRequest("/v1/comment?dry=1", commentPayload()), env
  );
  assert.equal(wrongAction.status, 403);
  assert.equal((await wrongAction.json()).code, "turnstile_invalid");

  globalThis.fetch = async () => Response.json({
    success: true, action: "comment_submit", hostname: "attacker.example"
  });
  const wrongHostname = await worker.fetch(
    jsonRequest("/v1/comment?dry=1", commentPayload()), env
  );
  assert.equal(wrongHostname.status, 403);
  assert.equal((await wrongHostname.json()).code, "turnstile_invalid");

  globalThis.fetch = async () => new Response("upstream failure", { status: 502 });
  const upstreamFailure = await worker.fetch(
    jsonRequest("/v1/comment?dry=1", commentPayload()), env
  );
  assert.equal(upstreamFailure.status, 403);
  assert.equal((await upstreamFailure.json()).code, "turnstile_invalid");

  let called = false;
  globalThis.fetch = async () => { called = true; return Response.json({ success: true }); };
  const oversized = await worker.fetch(jsonRequest("/v1/comment?dry=1", commentPayload({
    turnstile_token: "x".repeat(2049)
  })), env);
  assert.equal(oversized.status, 403);
  assert.equal((await oversized.json()).code, "turnstile_invalid");
  assert.equal(called, false);
});

test("five incorrect deletion keys lock the comment without GitHub calls", async () => {
  const env = testEnv();
  const id = "c-20260828-a3f1c9";
  env.COMMENTS_KV.values.set(`del:${id}`, JSON.stringify(await makePasswordRecord("correct-key", env)));
  for (let attempt = 1; attempt <= 5; attempt += 1) {
    const response = await worker.fetch(jsonRequest("/v1/delete", {
      id, thread: "ko__math__test_post", password: "wrong-key", confirm: true
    }), env);
    assert.equal(response.status, attempt < 5 ? 403 : 429);
  }
  const sixth = await worker.fetch(jsonRequest("/v1/delete", {
    id, thread: "ko__math__test_post", password: "wrong-key", confirm: true
  }), env);
  assert.equal(sixth.status, 429);
  assert.equal(calls.filter((call) => call.url.includes("github.com")).length, 0);
});

test("the Worker's own confirmation page may post back to it", async () => {
  const env = testEnv();
  const body = { id: "c-20260828-a3f1c9", thread: "ko__math__test_post", password: "x", confirm: true };
  const sameOrigin = await worker.fetch(
    jsonRequest("/v1/delete", body, { origin: "https://comments.example" }), env);
  assert.equal((await sameOrigin.json()).code, "comment_not_found");
  const foreign = await worker.fetch(
    jsonRequest("/v1/delete", body, { origin: "https://evil.example" }), env);
  assert.equal(foreign.status, 403);
  assert.equal((await foreign.json()).code, "origin_denied");
});

test("correct deletion key tombstones a parent comment and destroys deletion/subscription KV", async () => {
  const env = testEnv();
  const id = "c-20260828-a3f1c9";
  const replyId = "c-20260829-bbbbbb";
  env.COMMENTS_KV.values.set(`del:${id}`, JSON.stringify(await makePasswordRecord("correct-key", env)));
  env.COMMENTS_KV.values.set(`sub:${id}`, JSON.stringify({ emailEnc: "unused" }));
  var committedYaml = "";
  globalThis.fetch = async (input, init = {}) => {
    const url = typeof input === "string" ? input : input.url;
    calls.push({ url, init });
    if (url.includes("/contents/_data/comments/ko__math__test_post?") && !url.includes("comment-")) {
      return Response.json([
        { type: "file", name: "comment-parent.yml", path: "_data/comments/ko__math__test_post/comment-parent.yml" },
        { type: "file", name: "comment-reply.yml", path: "_data/comments/ko__math__test_post/comment-reply.yml" }
      ]);
    }
    if (url.includes("comment-parent.yml") && (!init.method || init.method === "GET")) {
      const yaml = `id: "${id}"\nname: "Parent"\nmessage: "body"\ndate: "2026-08-28T00:00:00Z"\nnotify: true\nlang: "ko"\n`;
      return Response.json({ sha: "parent-sha", content: Buffer.from(yaml).toString("base64") });
    }
    if (url.includes("comment-reply.yml")) {
      const yaml = `id: "${replyId}"\nname: "Reply"\nmessage: "reply"\ndate: "2026-08-29T00:00:00Z"\nreplying_to: "${id}"\nlang: "ko"\n`;
      return Response.json({ sha: "reply-sha", content: Buffer.from(yaml).toString("base64") });
    }
    if (url.includes("comment-parent.yml") && init.method === "PUT") {
      committedYaml = Buffer.from(JSON.parse(init.body).content, "base64").toString("utf8");
      return Response.json({ content: { sha: "new-sha" } });
    }
    throw new Error(`unexpected fetch: ${url}`);
  };
  const response = await worker.fetch(jsonRequest("/v1/delete", {
    id, thread: "ko__math__test_post", password: "correct-key", confirm: true
  }), env);
  assert.equal(response.status, 200);
  assert.equal((await response.json()).result, "tombstone");
  assert.match(committedYaml, /deleted: true/);
  assert.doesNotMatch(committedYaml, /Parent|body|notify/);
  assert.equal(await env.COMMENTS_KV.get(`del:${id}`), null);
  assert.equal(await env.COMMENTS_KV.get(`sub:${id}`), null);
});

test("signed deletion link closes an unmerged PR and deletes its branch", async () => {
  const env = testEnv();
  const id = "c-20260828-a3f1c9";
  env.COMMENTS_KV.values.set(`del:${id}`, "record");
  const token = await signToken(env.DELETE_HMAC_KEY, {
    purpose: "delete", id, threadKey: "ko__math__test_post"
  });
  globalThis.fetch = async (input, init = {}) => {
    const url = typeof input === "string" ? input : input.url;
    calls.push({ url, init });
    if (url.includes("/contents/_data/comments/ko__math__test_post?")) {
      return Response.json({ message: "Not Found" }, { status: 404 });
    }
    if (url.includes("/pulls?state=open&head=")) return Response.json([{ number: 7 }]);
    if (url.endsWith("/pulls/7") && init.method === "PATCH") return Response.json({ number: 7, state: "closed" });
    if (url.includes("/git/refs/heads/comment%2F") && init.method === "DELETE") return new Response(null, { status: 204 });
    throw new Error(`unexpected fetch: ${url}`);
  };
  const response = await worker.fetch(jsonRequest("/v1/delete", { token, confirm: true }), env);
  assert.equal(response.status, 200);
  assert.equal((await response.json()).result, "pending_closed");
  assert.equal(calls.some((call) => call.url.endsWith("/pulls/7") && call.init.method === "PATCH"), true);
  assert.equal(calls.some((call) => call.url.includes("/git/refs/heads/comment%2F") && call.init.method === "DELETE"), true);
  assert.equal(await env.COMMENTS_KV.get(`del:${id}`), null);
});

test("thread unsubscribe deletes matching subscriptions but preserves other threads", async () => {
  const env = testEnv();
  const email = "reader@example.com";
  const emailEnc = await encryptEmail(email, env);
  env.COMMENTS_KV.values.set("sub:c-20260828-111111", JSON.stringify({ emailEnc, threadKey: "ko__math__one" }));
  env.COMMENTS_KV.values.set("sub:c-20260828-222222", JSON.stringify({ emailEnc, threadKey: "ko__math__two" }));
  const token = await signToken(env.UNSUB_HMAC_KEY, {
    purpose: "unsub", email, scope: "thread", threadKey: "ko__math__one",
    exp: Math.floor(Date.now() / 1000) + 3600
  });
  const request = new Request(`https://comments.example/v1/unsub?t=${encodeURIComponent(token)}`, {
    method: "POST",
    headers: { "content-type": "application/x-www-form-urlencoded" },
    body: "List-Unsubscribe=One-Click"
  });
  const response = await worker.fetch(request, env);
  assert.equal(response.status, 200);
  assert.equal(await env.COMMENTS_KV.get("sub:c-20260828-111111"), null);
  assert.notEqual(await env.COMMENTS_KV.get("sub:c-20260828-222222"), null);
  assert.equal([...env.COMMENTS_KV.values.keys()].some((key) => key.startsWith("optout:") && key.endsWith(":ko__math__one")), true);
});

test("NOTIFY_EPOCH suppresses old mail and notified keys make reruns idempotent", async () => {
  const env = testEnv();
  const id = "c-20260828-a3f1c9";
  env.COMMENTS_KV.values.set(`sub:${id}`, JSON.stringify({
    emailEnc: await encryptEmail("author@example.com", env), lang: "ko",
    threadKey: "ko__math__test_post", createdAt: "2026-08-28T01:00:00Z"
  }));
  const comments = [
    { id: "c-20260827-111111", threadKey: "ko__math__old", permalink: "/ko/math/old", date: "2026-08-27T23:59:00Z", name: "Old", lang: "ko" },
    { id, threadKey: "ko__math__test_post", permalink: "/ko/math/test_post", date: "2026-08-28T01:00:00Z", name: "New", message: "hello", lang: "ko" }
  ];
  const raw = JSON.stringify({ comments });
  const signature = await hmacHex(env.NOTIFY_HMAC_KEY, raw);
  const request = () => new Request("https://comments.example/v1/notify", {
    method: "POST", headers: { "content-type": "application/json", "x-comments-signature": signature }, body: raw
  });
  const first = await worker.fetch(request(), env);
  assert.equal(first.status, 200);
  assert.deepEqual(await first.json(), { ok: true, sent: 1, ignored_before_epoch: 1 });
  const second = await worker.fetch(request(), env);
  assert.equal(second.status, 200);
  assert.deepEqual(await second.json(), { ok: true, sent: 0, ignored_before_epoch: 1 });
  assert.equal(calls.filter((call) => call.url.includes("api.resend.com")).length, 1);
});

test("reply plus mention to the same recipient produces one message and excludes self", async () => {
  const env = testEnv();
  const newId = "c-20260829-aaaaaa";
  const parentId = "c-20260828-bbbbbb";
  const ownEmail = await encryptEmail("writer@example.com", env);
  const parentEmail = await encryptEmail("parent@example.com", env);
  env.COMMENTS_KV.values.set(`sub:${newId}`, JSON.stringify({ emailEnc: ownEmail, lang: "ko", threadKey: "ko__math__test" }));
  env.COMMENTS_KV.values.set(`sub:${parentId}`, JSON.stringify({ emailEnc: parentEmail, lang: "ko", threadKey: "ko__math__test" }));
  const comments = [{
    id: newId, threadKey: "ko__math__test", permalink: "/ko/math/test",
    date: "2026-08-29T00:00:00Z", replying_to: parentId, mentions: [parentId, newId],
    name: "Writer", message: "reply", lang: "ko"
  }];
  const raw = JSON.stringify({ comments });
  const signature = await hmacHex(env.NOTIFY_HMAC_KEY, raw);
  const response = await worker.fetch(new Request("https://comments.example/v1/notify", {
    method: "POST", headers: { "content-type": "application/json", "x-comments-signature": signature }, body: raw
  }), env);
  assert.equal(response.status, 200);
  assert.equal((await response.json()).sent, 2); // approval to self + one combined reply/mention to parent
  assert.equal(calls.filter((call) => call.url.includes("api.resend.com")).length, 2);
});

test("edit lands on comment-edit branch as a PR, never on main, and keeps the role key", async () => {
  const env = testEnv();
  const id = "c-20260828-a3f1c9";
  env.COMMENTS_KV.values.set(`del:${id}`, JSON.stringify(await makePasswordRecord("correct-key", env)));
  const stored = `id: "${id}"\nname: "Tester"\nmessage: "before"\ndate: "2026-08-28T00:00:00Z"\nnotify: true\nrole: "owner"\nlang: "ko"\n`;
  let committed = null;
  globalThis.fetch = async (input, init = {}) => {
    const url = typeof input === "string" ? input : input.url;
    calls.push({ url, init });
    if (url.includes("/contents/_data/comments/ko__math__test_post?")) {
      return Response.json([
        { type: "file", name: "comment-a.yml", path: "_data/comments/ko__math__test_post/comment-a.yml" }
      ]);
    }
    if (url.includes("comment-a.yml") && url.includes("ref=main")) {
      return Response.json({ sha: "main-sha", content: Buffer.from(stored).toString("base64") });
    }
    if (url.includes("comment-a.yml") && url.includes("ref=comment-edit")) {
      return new Response("null", { status: 404 });
    }
    if (url.endsWith("/git/ref/heads/main")) return Response.json({ object: { sha: "base-sha" } });
    if (url.endsWith("/git/refs") && init.method === "POST") return Response.json({ ref: "ok" });
    if (url.includes("comment-a.yml") && init.method === "PUT") {
      committed = JSON.parse(init.body);
      return Response.json({ content: { sha: "edit-sha" } });
    }
    if (url.includes("/pulls?state=open")) return Response.json([]);
    if (url.endsWith("/pulls") && init.method === "POST") {
      return Response.json({ number: 51, html_url: "https://github.com/pull/51" });
    }
    throw new Error(`unexpected fetch: ${url}`);
  };

  const response = await worker.fetch(jsonRequest("/v1/edit", {
    id, thread: "ko__math__test_post", password: "correct-key", message: "after <b>edit</b>"
  }), env);
  assert.equal(response.status, 200);
  assert.deepEqual(await response.json(), { ok: true, id, pending: true, pull: 51 });

  const yaml = Buffer.from(committed.content, "base64").toString("utf8");
  assert.equal(committed.branch, `comment-edit/${id}`);
  assert.equal(committed.sha, "main-sha");
  assert.match(yaml, /message: "after edit"/);        // HTML stripped like a new comment
  assert.match(yaml, /role: "owner"/);                 // 손으로 단 배지 키가 살아남는다
  assert.match(yaml, /edited: "\d{4}-/);
  assert.match(yaml, /notify: true/);
  // main 브랜치를 건드리는 쓰기가 하나도 없어야 한다.
  const mainWrites = calls.filter((call) => call.init.method === "PUT" &&
    JSON.parse(call.init.body).branch === "main");
  assert.equal(mainWrites.length, 0);
});

test("edit rejects a wrong key, an unchanged body, and a deleted comment", async () => {
  const env = testEnv();
  const id = "c-20260828-a3f1c9";
  env.COMMENTS_KV.values.set(`del:${id}`, JSON.stringify(await makePasswordRecord("correct-key", env)));
  const stored = `id: "${id}"\nname: "Tester"\nmessage: "before"\ndate: "2026-08-28T00:00:00Z"\nlang: "ko"\n`;
  globalThis.fetch = async (input, init = {}) => {
    const url = typeof input === "string" ? input : input.url;
    calls.push({ url, init });
    if (url.includes("/contents/_data/comments/ko__math__test_post?")) {
      return Response.json([
        { type: "file", name: "comment-a.yml", path: "_data/comments/ko__math__test_post/comment-a.yml" }
      ]);
    }
    if (url.includes("comment-a.yml")) {
      return Response.json({ sha: "main-sha", content: Buffer.from(stored).toString("base64") });
    }
    throw new Error(`unexpected fetch: ${url}`);
  };

  const wrong = await worker.fetch(jsonRequest("/v1/edit", {
    id, thread: "ko__math__test_post", password: "wrong-key", message: "after"
  }), env);
  assert.equal(wrong.status, 403);
  assert.equal((await wrong.json()).code, "delete_auth_failed");
  assert.equal(calls.filter((call) => call.url.includes("github.com")).length, 0);

  const unchanged = await worker.fetch(jsonRequest("/v1/edit", {
    id, thread: "ko__math__test_post", password: "correct-key", message: "before"
  }), env);
  assert.equal(unchanged.status, 400);
  assert.equal((await unchanged.json()).code, "edit_unchanged");

  const missing = await worker.fetch(jsonRequest("/v1/edit", {
    id: "c-20260828-ffffff", thread: "ko__math__test_post", password: "correct-key", message: "after"
  }), env);
  assert.equal(missing.status, 404);
  assert.equal((await missing.json()).code, "comment_not_found");
});
