import {
  COMMENT_ID_RE, PublicError, THREAD_RE, assertAllowedOrigin, corsHeaders, emailHash,
  encryptEmail, escapeHtml, hmacHex, htmlResponse, jsonResponse, makeCommentId,
  makePasswordRecord, randomHex, readJson, serializeComment, signToken,
  threadPermalink, validateCommentPayload, validateEditPayload, verifyHmacHex,
  verifyPassword, verifyToken, commentPath
} from "./lib.js";
import {
  assertReferencesExist, closePendingComment, closePendingEdit,
  createCommentEditPullRequest, createCommentPullRequest, deleteApprovedComment,
  getThreadComments
} from "./github.js";
import { notifyComments, removeSubscriptions } from "./notify.js";

const SUB_TTL = 400 * 24 * 60 * 60;

async function verifyTurnstile(request, env, token) {
  if (!token || typeof token !== "string" || !token.trim()) {
    throw new PublicError(403, "turnstile_required");
  }
  if (token.length > 2048) throw new PublicError(403, "turnstile_invalid");

  const expectedAction = (env.TURNSTILE_ACTION || "").trim();
  const expectedHostnames = new Set((env.TURNSTILE_HOSTNAMES || "")
    .split(",")
    .map((hostname) => hostname.trim().toLowerCase())
    .filter(Boolean));
  if (!env.TURNSTILE_SECRET || !expectedAction || expectedHostnames.size === 0) {
    throw new PublicError(503, "turnstile_unavailable");
  }

  const body = new URLSearchParams();
  body.set("secret", env.TURNSTILE_SECRET);
  body.set("response", token);
  const remoteIp = request.headers.get("cf-connecting-ip");
  if (remoteIp) body.set("remoteip", remoteIp);
  let result;
  try {
    const response = await fetch("https://challenges.cloudflare.com/turnstile/v0/siteverify", {
      method: "POST",
      headers: { "content-type": "application/x-www-form-urlencoded" },
      signal: AbortSignal.timeout(10_000),
      body
    });
    if (!response.ok) throw new Error("siteverify_http_error");
    result = await response.json();
  } catch {
    throw new PublicError(403, "turnstile_invalid");
  }
  if (!result?.success || result.action !== expectedAction ||
      !expectedHostnames.has(String(result.hostname || "").toLowerCase())) {
    throw new PublicError(403, "turnstile_invalid");
  }
}

async function handleComment(request, env, url) {
  assertAllowedOrigin(request, env);
  const { value: input } = await readJson(request);
  await verifyTurnstile(request, env, input.turnstile_token);
  const clean = validateCommentPayload(input);
  const references = await assertReferencesExist(env, clean);
  const now = new Date();
  const unixSeconds = Math.floor(now.getTime() / 1000);
  const id = makeCommentId(now);
  const suffix = randomHex(3);
  const comment = {
    id,
    name: clean.name,
    message: clean.message,
    date: now.toISOString(),
    replying_to: clean.replying_to,
    mentions: clean.mentions,
    notify: Boolean(clean.email),
    lang: clean.lang,
    thread: clean.thread
  };

  const started = performance.now();
  const passwordRecord = await makePasswordRecord(clean.password, env, now);
  const pbkdf2Ms = performance.now() - started;
  if (url.searchParams.get("dry") === "1") {
    return {
      status: 200,
      body: {
        ok: true,
        dry: true,
        id,
        sanitized: {
          name: comment.name,
          message: comment.message,
          thread: comment.thread,
          replying_to: comment.replying_to || null,
          mentions: comment.mentions,
          notify: comment.notify,
          lang: comment.lang
        },
        pbkdf2: { iterations: passwordRecord.iterations, elapsed_ms: Number(pbkdf2Ms.toFixed(3)) }
      }
    };
  }

  const path = commentPath(comment, unixSeconds, suffix);
  const yaml = serializeComment(comment);
  let pull;
  try {
    pull = await createCommentPullRequest(env, { comment, path, yaml, parent: references.parent });
    const writes = [env.COMMENTS_KV.put(`del:${id}`, JSON.stringify(passwordRecord))];
    if (clean.email) {
      writes.push(env.COMMENTS_KV.put(`sub:${id}`, JSON.stringify({
        emailEnc: await encryptEmail(clean.email, env),
        lang: clean.lang,
        threadKey: clean.thread,
        parentId: clean.replying_to || null,
        createdAt: now.toISOString()
      }), { expirationTtl: SUB_TTL }));
    }
    await Promise.all(writes);
  } catch {
    if (pull) {
      await closePendingComment(env, id).catch(() => {});
      await Promise.all([
        env.COMMENTS_KV.delete(`del:${id}`).catch(() => {}),
        env.COMMENTS_KV.delete(`sub:${id}`).catch(() => {})
      ]);
    }
    throw new PublicError(502, "submission_failed");
  }
  const deleteToken = await signToken(env.DELETE_HMAC_KEY, {
    purpose: "delete", id, threadKey: clean.thread
  });
  return {
    status: 201,
    body: { ok: true, id, delete_token: deleteToken, pending: true }
  };
}

function deletionPage({ token = "", id = "", thread = "", lang = "ko" }) {
  const ko = lang !== "en";
  const title = ko ? "댓글 삭제 확인" : "Confirm comment deletion";
  const warning = ko
    ? "삭제하면 사이트에서는 사라지지만 공개 저장소의 git 이력에는 남을 수 있습니다."
    : "Deletion removes the comment from the site, but it may remain in the public repository history.";
  const button = ko ? "댓글 삭제" : "Delete comment";
  return `<!doctype html><html lang="${ko ? "ko" : "en"}"><meta charset="utf-8"><meta name="viewport" content="width=device-width"><title>${title}</title>
    <style>body{font:16px system-ui;max-width:36rem;margin:4rem auto;padding:0 1rem}button{padding:.7rem 1rem;background:#b42318;color:#fff;border:0;border-radius:.3rem}</style>
    <h1>${title}</h1><p>${warning}</p>
    <form method="post" action="/v1/delete">
      <input type="hidden" name="token" value="${escapeHtml(token)}">
      <input type="hidden" name="id" value="${escapeHtml(id)}">
      <input type="hidden" name="thread" value="${escapeHtml(thread)}">
      <input type="hidden" name="confirm" value="true">
      <button type="submit">${button}</button>
    </form></html>`;
}

async function parseJsonOrForm(request) {
  const type = (request.headers.get("content-type") || "").toLowerCase();
  if (type.startsWith("application/json")) return (await readJson(request)).value;
  if (type.startsWith("application/x-www-form-urlencoded") || type.startsWith("multipart/form-data")) {
    return Object.fromEntries(await request.formData());
  }
  throw new PublicError(415, "content_type");
}

async function handleDeleteGet(env, url) {
  const token = url.searchParams.get("t") || "";
  if (!token) throw new PublicError(400, "invalid_token");
  const payload = await verifyToken(env.DELETE_HMAC_KEY, token, "delete");
  return htmlResponse(deletionPage({
    token,
    id: payload.id,
    thread: payload.threadKey || "",
    lang: payload.threadKey?.startsWith("en__") ? "en" : "ko"
  }));
}

// 삭제와 수정이 같은 삭제용 암호·같은 잠금 카운터(fail:<id>)를 쓴다. 실패 5회면
// 두 경로 모두 한 시간 잠긴다.
async function assertPassword(env, id, password) {
  const failed = Number.parseInt(await env.COMMENTS_KV.get(`fail:${id}`) || "0", 10);
  if (failed >= 5) throw new PublicError(429, "delete_locked");
  const record = await env.COMMENTS_KV.get(`del:${id}`, "json");
  if (!record) throw new PublicError(404, "comment_not_found");
  if (!(await verifyPassword(password, record, env))) {
    const next = failed + 1;
    await env.COMMENTS_KV.put(`fail:${id}`, String(next), { expirationTtl: 3600 });
    if (next >= 5) throw new PublicError(429, "delete_locked");
    throw new PublicError(403, "delete_auth_failed");
  }
  await env.COMMENTS_KV.delete(`fail:${id}`);
}

async function authenticateDeletion(env, input) {
  if (input.token) {
    const payload = await verifyToken(env.DELETE_HMAC_KEY, input.token, "delete");
    return { id: payload.id, thread: payload.threadKey || input.thread };
  }
  const id = String(input.id || "");
  const thread = String(input.thread || "");
  const password = typeof input.password === "string" ? input.password : "";
  if (!COMMENT_ID_RE.test(id) || !THREAD_RE.test(thread) || !password) {
    throw new PublicError(400, "invalid_delete_request");
  }
  await assertPassword(env, id, password);
  return { id, thread };
}

async function handleEdit(request, env) {
  assertAllowedOrigin(request, env);
  const { value: input } = await readJson(request);
  const clean = validateEditPayload(input);
  await assertPassword(env, clean.id, clean.password);

  // GitHub API 를 두드리는 경로라 성공 뒤 1분은 같은 댓글의 재수정을 막는다.
  if (await env.COMMENTS_KV.get(`edit:${clean.id}`)) throw new PublicError(429, "edit_too_soon");

  const comments = await getThreadComments(env, clean.thread);
  const target = comments.find((comment) => comment.id === clean.id);
  if (!target || target.deleted) throw new PublicError(404, "comment_not_found");
  if (String(target.message || "") === clean.message) throw new PublicError(400, "edit_unchanged");

  const now = new Date();
  const comment = {
    ...target,
    message: clean.message,
    edited: now.toISOString(),
    thread: clean.thread,
    lang: target.lang === "en" ? "en" : "ko"
  };
  let pull;
  try {
    pull = await createCommentEditPullRequest(env, {
      comment,
      path: target._path,
      yaml: serializeComment(comment),
      previous: target
    });
  } catch {
    throw new PublicError(502, "edit_failed");
  }
  await env.COMMENTS_KV.put(`edit:${clean.id}`, "1", { expirationTtl: 60 });
  return { ok: true, id: clean.id, pending: true, pull: pull.number };
}

async function handleDeletePost(request, env) {
  assertAllowedOrigin(request, env);
  const input = await parseJsonOrForm(request);
  if (!(input.confirm === true || input.confirm === "true")) {
    throw new PublicError(400, "confirmation_required");
  }
  const { id, thread } = await authenticateDeletion(env, input);
  if (!COMMENT_ID_RE.test(String(id || "")) || !THREAD_RE.test(String(thread || ""))) {
    throw new PublicError(400, "invalid_delete_request");
  }
  let result;
  try {
    result = await deleteApprovedComment(env, id, thread);
    if (!result) result = (await closePendingComment(env, id)) ? "pending_closed" : null;
    await closePendingEdit(env, id).catch(() => {});
  } catch {
    throw new PublicError(502, "delete_failed");
  }
  if (!result) throw new PublicError(404, "comment_not_found");
  await Promise.all([
    env.COMMENTS_KV.delete(`del:${id}`),
    env.COMMENTS_KV.delete(`sub:${id}`),
    env.COMMENTS_KV.delete(`fail:${id}`),
    env.COMMENTS_KV.delete(`edit:${id}`)
  ]);
  return { ok: true, id, result };
}

function unsubscribePage(token, payload) {
  const ko = payload.threadKey?.startsWith("ko__") ?? true;
  const title = ko ? "댓글 알림 수신거부" : "Unsubscribe from comment email";
  const scope = payload.scope === "thread"
    ? (ko ? "이 글의 댓글 알림을 끕니다." : "This disables email for this thread.")
    : (ko ? "모든 댓글 알림을 끕니다." : "This disables all comment email.");
  const button = ko ? "수신거부 확인" : "Confirm unsubscribe";
  return `<!doctype html><html lang="${ko ? "ko" : "en"}"><meta charset="utf-8"><meta name="viewport" content="width=device-width"><title>${title}</title>
    <style>body{font:16px system-ui;max-width:36rem;margin:4rem auto;padding:0 1rem}button{padding:.7rem 1rem}</style>
    <h1>${title}</h1><p>${scope}</p><form method="post" action="/v1/unsub?t=${encodeURIComponent(token)}">
    <input type="hidden" name="List-Unsubscribe" value="One-Click"><button type="submit">${button}</button></form></html>`;
}

async function handleUnsubscribeGet(env, url) {
  const token = url.searchParams.get("t") || "";
  const payload = await verifyToken(env.UNSUB_HMAC_KEY, token, "unsub");
  return htmlResponse(unsubscribePage(token, payload));
}

async function handleUnsubscribePost(request, env, url) {
  const input = await parseJsonOrForm(request);
  const token = url.searchParams.get("t") || input.t || "";
  const payload = await verifyToken(env.UNSUB_HMAC_KEY, token, "unsub");
  if (!payload.email || !["global", "thread"].includes(payload.scope)) {
    throw new PublicError(400, "invalid_token");
  }
  if (payload.scope === "thread" && !THREAD_RE.test(payload.threadKey || "")) {
    throw new PublicError(400, "invalid_token");
  }
  await removeSubscriptions(env, payload.email, payload.scope, payload.threadKey);
  return { ok: true, scope: payload.scope };
}

async function handleNotify(request, env) {
  const { value, raw } = await readJson(request, 5_000_000);
  const signature = request.headers.get("x-comments-signature") || "";
  if (!(await verifyHmacHex(env.NOTIFY_HMAC_KEY, raw, signature))) {
    throw new PublicError(401, "invalid_signature");
  }
  return { ok: true, ...(await notifyComments(env, value)) };
}

async function route(request, env) {
  const url = new URL(request.url);
  if (request.method === "OPTIONS") {
    assertAllowedOrigin(request, env);
    return new Response(null, { status: 204, headers: corsHeaders(request, env) });
  }
  if (request.method === "GET" && url.pathname === "/") {
    return jsonResponse({ ok: true, service: "math-jh-comments" });
  }
  if (url.pathname === "/v1/comment" && request.method === "POST") {
    const result = await handleComment(request, env, url);
    return jsonResponse(result.body, result.status, corsHeaders(request, env));
  }
  if (url.pathname === "/v1/edit" && request.method === "POST") {
    return jsonResponse(await handleEdit(request, env), 200, corsHeaders(request, env));
  }
  if (url.pathname === "/v1/delete" && request.method === "GET") return handleDeleteGet(env, url);
  if (url.pathname === "/v1/delete" && request.method === "POST") {
    return jsonResponse(await handleDeletePost(request, env), 200, corsHeaders(request, env));
  }
  if (url.pathname === "/v1/unsub" && request.method === "GET") return handleUnsubscribeGet(env, url);
  if (url.pathname === "/v1/unsub" && request.method === "POST") {
    return jsonResponse(await handleUnsubscribePost(request, env, url));
  }
  if (url.pathname === "/v1/notify" && request.method === "POST") {
    return jsonResponse(await handleNotify(request, env));
  }
  throw new PublicError(404, "not_found");
}

export default {
  async fetch(request, env) {
    try {
      return await route(request, env);
    } catch (error) {
      const status = error instanceof PublicError ? error.status : 500;
      const code = error instanceof PublicError ? error.code : "internal_error";
      return jsonResponse({ ok: false, code }, status, corsHeaders(request, env));
    }
  }
};

export { handleComment, handleDeletePost, handleEdit, handleNotify };
