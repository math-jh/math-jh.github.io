const encoder = new TextEncoder();
const decoder = new TextDecoder();

export const COMMENT_FIELDS = new Set([
  "name", "password", "email", "message", "thread", "replying_to", "mentions"
]);
export const CONTROL_FIELDS = new Set(["turnstile_token", "honeypot", "elapsed_ms"]);
export const EDIT_FIELDS = new Set(["id", "thread", "password", "message"]);
export const COMMENT_ID_RE = /^c-\d{8}-[a-f0-9]{6}$/;
// 키는 page.url 과 1:1 이다. 대소문자를 보존하고 하이픈을 허용한다 — permalink 에
// 대문자나 `-` 를 쓰는 글이 있고(Jordan-Holder_theorem), 접으면 키에서 URL 을
// 되돌릴 수 없다. 경로 조작 방어는 점·슬래시가 없다는 것으로 유지된다.
export const THREAD_RE = /^(?:ko|en)__[A-Za-z0-9_-]{1,116}$/;

export class PublicError extends Error {
  constructor(status, code) {
    super(code);
    this.status = status;
    this.code = code;
  }
}

export function jsonResponse(body, status = 200, headers = {}) {
  return new Response(JSON.stringify(body), {
    status,
    headers: { "content-type": "application/json; charset=utf-8", ...headers }
  });
}

export function htmlResponse(body, status = 200, headers = {}) {
  return new Response(body, {
    status,
    headers: {
      "content-type": "text/html; charset=utf-8",
      "x-content-type-options": "nosniff",
      "content-security-policy": "default-src 'none'; style-src 'unsafe-inline'; form-action 'self'; base-uri 'none'",
      ...headers
    }
  });
}

export function corsHeaders(request, env) {
  const origin = request.headers.get("origin") || "";
  const allowed = String(env.ALLOWED_ORIGINS || "")
    .split(",").map((item) => item.trim()).filter(Boolean);
  if (!allowed.includes(origin)) return {};
  return {
    "access-control-allow-origin": origin,
    "access-control-allow-methods": "GET, POST, OPTIONS",
    "access-control-allow-headers": "content-type, x-comments-signature",
    "access-control-max-age": "86400",
    vary: "Origin"
  };
}

export function assertAllowedOrigin(request, env) {
  const origin = request.headers.get("origin");
  if (!origin) return;
  // 삭제·수신거부 확인 페이지는 Worker 자신이 서빙하고 자기 자신에게 form POST 한다.
  // 브라우저가 그 POST 에도 Origin 을 붙이므로 same-origin 을 먼저 통과시킨다.
  if (origin === new URL(request.url).origin) return;
  const allowed = String(env.ALLOWED_ORIGINS || "")
    .split(",").map((item) => item.trim()).filter(Boolean);
  if (!allowed.includes(origin)) throw new PublicError(403, "origin_denied");
}

export async function readJson(request, maxBytes = 20_000) {
  const type = request.headers.get("content-type") || "";
  if (!type.toLowerCase().startsWith("application/json")) {
    throw new PublicError(415, "content_type");
  }
  const raw = await request.text();
  if (encoder.encode(raw).byteLength > maxBytes) throw new PublicError(413, "too_large");
  try {
    const value = JSON.parse(raw);
    if (!value || Array.isArray(value) || typeof value !== "object") throw new Error();
    return { value, raw };
  } catch {
    throw new PublicError(400, "invalid_json");
  }
}

export function stripHtml(input) {
  let value = String(input).replace(/\0/g, "").replace(/<!--[\s\S]*?-->/g, "");
  let previous;
  do {
    previous = value;
    value = value.replace(/<[^<>]*>/g, "");
  } while (value !== previous);
  return value
    .replace(/[<>]/g, "")
    // Kramdown IAL/extension blocks can otherwise turn plain Markdown into
    // event attributes such as `<p onclick=...>` during the Jekyll build.
    .replace(/\{::?[^}\n]*\}/g, "")
    .replace(/\r\n?/g, "\n")
    .trim();
}

export function validateCommentPayload(input) {
  const allowed = new Set([...COMMENT_FIELDS, ...CONTROL_FIELDS]);
  for (const key of Object.keys(input)) {
    if (!allowed.has(key)) throw new PublicError(400, "unknown_field");
  }
  for (const key of [...COMMENT_FIELDS, ...CONTROL_FIELDS]) {
    if (!(key in input) && !["email", "replying_to", "mentions"].includes(key)) {
      throw new PublicError(400, "missing_field");
    }
  }
  if (String(input.honeypot || "") !== "") throw new PublicError(400, "honeypot");
  if (!Number.isFinite(input.elapsed_ms) || input.elapsed_ms < 3000) {
    throw new PublicError(400, "too_fast");
  }

  const name = stripHtml(input.name).replace(/\s+/g, " ");
  const password = typeof input.password === "string" ? input.password : "";
  const email = String(input.email || "").trim().toLowerCase();
  const message = stripHtml(input.message);
  const thread = String(input.thread || "");
  const replyingTo = String(input.replying_to || "");
  const mentions = input.mentions === undefined ? [] : input.mentions;

  if (!name || [...name].length > 60) throw new PublicError(400, "invalid_name");
  if ([...password].length < 4 || [...password].length > 128) {
    throw new PublicError(400, "invalid_password");
  }
  validateMessage(message);
  if (!THREAD_RE.test(thread) || thread.length > 120) throw new PublicError(400, "invalid_thread");
  if (email && (email.length > 254 || !/^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(email))) {
    throw new PublicError(400, "invalid_email");
  }
  if (replyingTo && !COMMENT_ID_RE.test(replyingTo)) {
    throw new PublicError(400, "invalid_reply");
  }
  if (!Array.isArray(mentions) || mentions.length > 3) {
    throw new PublicError(400, "invalid_mentions");
  }
  const cleanMentions = [...new Set(mentions.map(String))];
  if (cleanMentions.length !== mentions.length || cleanMentions.some((id) => !COMMENT_ID_RE.test(id))) {
    throw new PublicError(400, "invalid_mentions");
  }

  return {
    name, password, email, message, thread,
    replying_to: replyingTo || undefined,
    mentions: cleanMentions,
    lang: thread.startsWith("ko__") ? "ko" : "en"
  };
}

// 본문 규칙은 신규 작성과 수정이 공유한다 — 한쪽만 고치면 수정 경로가 링크·스킴
// 상한을 우회하는 구멍이 된다.
export function validateMessage(message) {
  if (!message || [...message].length > 8000) throw new PublicError(400, "invalid_message");
  const links = message.match(/(?:https?:\/\/|www\.)[^\s<>()]+/gi) || [];
  if (links.length >= 4) throw new PublicError(400, "too_many_links");
  if (/(?:javascript|vbscript|data)\s*:/i.test(message)) {
    throw new PublicError(400, "unsafe_content");
  }
  return message;
}

export function validateEditPayload(input) {
  for (const key of Object.keys(input)) {
    if (!EDIT_FIELDS.has(key)) throw new PublicError(400, "unknown_field");
  }
  for (const key of EDIT_FIELDS) {
    if (!(key in input)) throw new PublicError(400, "missing_field");
  }
  const id = String(input.id || "");
  const thread = String(input.thread || "");
  const password = typeof input.password === "string" ? input.password : "";
  const message = stripHtml(input.message);
  if (!COMMENT_ID_RE.test(id)) throw new PublicError(400, "invalid_edit_request");
  if (!THREAD_RE.test(thread) || thread.length > 120) throw new PublicError(400, "invalid_thread");
  if ([...password].length < 4 || [...password].length > 128) {
    throw new PublicError(400, "invalid_password");
  }
  validateMessage(message);
  return { id, thread, password, message };
}

export function makeCommentId(now = new Date()) {
  const day = now.toISOString().slice(0, 10).replaceAll("-", "");
  return `c-${day}-${randomHex(3)}`;
}

export function randomHex(bytes) {
  const value = new Uint8Array(bytes);
  crypto.getRandomValues(value);
  return [...value].map((part) => part.toString(16).padStart(2, "0")).join("");
}

export function threadPermalink(thread) {
  return `/${thread.split("__").join("/")}`;
}

export function threadTitle(thread) {
  return thread.split("__").at(-1).replaceAll("_", " ");
}

export function commentPath(comment, unixSeconds, suffix) {
  return `_data/comments/${comment.thread}/comment-${unixSeconds}-${suffix}.yml`;
}

export function serializeComment(comment) {
  const lines = [
    `id: ${JSON.stringify(comment.id)}`,
    `name: ${JSON.stringify(comment.name)}`,
    `message: ${JSON.stringify(comment.message)}`,
    `date: ${JSON.stringify(comment.date)}`
  ];
  if (comment.replying_to) lines.push(`replying_to: ${JSON.stringify(comment.replying_to)}`);
  if (comment.mentions?.length) lines.push(`mentions: ${JSON.stringify(comment.mentions)}`);
  if (comment.notify) lines.push("notify: true");
  // role 은 손으로 다는 키(owner·bot; _includes/comment.html 이 배지로 읽는다).
  // 수정 경로가 파일을 다시 쓸 때 여기서 보존되지 않으면 배지가 조용히 사라진다.
  if (comment.role) lines.push(`role: ${JSON.stringify(comment.role)}`);
  if (comment.edited) lines.push(`edited: ${JSON.stringify(comment.edited)}`);
  lines.push(`lang: ${JSON.stringify(comment.lang)}`);
  return `${lines.join("\n")}\n`;
}

export function serializeTombstone(comment) {
  const lines = [
    `id: ${JSON.stringify(comment.id)}`,
    `date: ${JSON.stringify(comment.date)}`
  ];
  if (comment.replying_to) lines.push(`replying_to: ${JSON.stringify(comment.replying_to)}`);
  if (comment.mentions?.length) lines.push(`mentions: ${JSON.stringify(comment.mentions)}`);
  lines.push(`lang: ${JSON.stringify(comment.lang)}`, "deleted: true");
  return `${lines.join("\n")}\n`;
}

export function parseCommentYaml(source) {
  const result = {};
  for (const line of String(source).split("\n")) {
    const match = line.match(/^([a-z_]+):\s*(.+)$/);
    if (!match) continue;
    const [, key, raw] = match;
    if (raw === "true" || raw === "false") result[key] = raw === "true";
    else {
      try { result[key] = JSON.parse(raw); } catch { result[key] = raw; }
    }
  }
  return result;
}

function bytesToBase64(bytes) {
  let binary = "";
  for (const byte of bytes) binary += String.fromCharCode(byte);
  return btoa(binary);
}

function base64ToBytes(value) {
  const binary = atob(value);
  return Uint8Array.from(binary, (char) => char.charCodeAt(0));
}

export function base64UrlEncode(bytes) {
  return bytesToBase64(bytes).replaceAll("+", "-").replaceAll("/", "_").replace(/=+$/, "");
}

export function base64UrlDecode(value) {
  const normalized = value.replaceAll("-", "+").replaceAll("_", "/");
  return base64ToBytes(normalized + "=".repeat((4 - normalized.length % 4) % 4));
}

function secretBytes(secret, expectedBytes = null) {
  const value = String(secret || "");
  let bytes;
  if (/^[a-f0-9]+$/i.test(value) && value.length % 2 === 0) {
    bytes = Uint8Array.from(value.match(/../g) || [], (part) => Number.parseInt(part, 16));
  } else if (/^[A-Za-z0-9_-]+$/.test(value)) {
    try { bytes = base64UrlDecode(value); } catch { bytes = encoder.encode(value); }
  } else {
    bytes = encoder.encode(value);
  }
  if (expectedBytes && bytes.byteLength !== expectedBytes) {
    throw new Error(`secret must decode to ${expectedBytes} bytes`);
  }
  return bytes;
}

async function hmacBytes(secret, value) {
  const keyBytes = encoder.encode(String(secret || ""));
  if (keyBytes.byteLength < 32) throw new Error("HMAC secret is too short");
  const key = await crypto.subtle.importKey(
    "raw", keyBytes, { name: "HMAC", hash: "SHA-256" }, false, ["sign", "verify"]
  );
  return new Uint8Array(await crypto.subtle.sign("HMAC", key, encoder.encode(value)));
}

export async function hmacHex(secret, value) {
  return [...await hmacBytes(secret, value)]
    .map((byte) => byte.toString(16).padStart(2, "0")).join("");
}

export async function verifyHmacHex(secret, value, signature) {
  if (!/^[a-f0-9]{64}$/i.test(String(signature || ""))) return false;
  const expected = await hmacHex(secret, value);
  let mismatch = 0;
  for (let index = 0; index < expected.length; index += 1) {
    mismatch |= expected.charCodeAt(index) ^ signature.toLowerCase().charCodeAt(index);
  }
  return mismatch === 0;
}

export async function signToken(secret, payload) {
  const encoded = base64UrlEncode(encoder.encode(JSON.stringify(payload)));
  return `${encoded}.${base64UrlEncode(await hmacBytes(secret, encoded))}`;
}

export async function verifyToken(secret, token, purpose) {
  const [encoded, signature, extra] = String(token || "").split(".");
  if (!encoded || !signature || extra) throw new PublicError(400, "invalid_token");
  const expected = await hmacBytes(secret, encoded);
  const actual = base64UrlDecode(signature);
  if (actual.length !== expected.length) throw new PublicError(400, "invalid_token");
  let mismatch = 0;
  for (let index = 0; index < expected.length; index += 1) mismatch |= expected[index] ^ actual[index];
  if (mismatch) throw new PublicError(400, "invalid_token");
  let payload;
  try { payload = JSON.parse(decoder.decode(base64UrlDecode(encoded))); } catch {
    throw new PublicError(400, "invalid_token");
  }
  if (payload.purpose !== purpose) throw new PublicError(400, "invalid_token");
  if (payload.exp && Date.now() >= payload.exp * 1000) throw new PublicError(400, "expired_token");
  return payload;
}

export async function derivePassword(password, pepper, salt, iterations) {
  const pepperBytes = encoder.encode(String(pepper || ""));
  const passwordBytes = encoder.encode(password);
  const combined = new Uint8Array(pepperBytes.length + passwordBytes.length);
  combined.set(pepperBytes);
  combined.set(passwordBytes, pepperBytes.length);
  const material = await crypto.subtle.importKey("raw", combined, "PBKDF2", false, ["deriveBits"]);
  const bits = await crypto.subtle.deriveBits(
    { name: "PBKDF2", hash: "SHA-256", salt: base64UrlDecode(salt), iterations },
    material,
    256
  );
  return base64UrlEncode(new Uint8Array(bits));
}

export async function makePasswordRecord(password, env, now = new Date()) {
  const salt = base64UrlEncode(crypto.getRandomValues(new Uint8Array(16)));
  const iterations = Number.parseInt(env.PBKDF2_ITERATIONS, 10);
  if (!Number.isInteger(iterations) || iterations < 1) throw new Error("invalid PBKDF2_ITERATIONS");
  return {
    salt,
    hash: await derivePassword(password, env.PASSWORD_PEPPER, salt, iterations),
    iterations,
    createdAt: now.toISOString()
  };
}

export async function verifyPassword(password, record, env) {
  const actual = await derivePassword(
    password, env.PASSWORD_PEPPER, record.salt,
    Number.parseInt(record.iterations || env.PBKDF2_ITERATIONS, 10)
  );
  if (actual.length !== record.hash.length) return false;
  let mismatch = 0;
  for (let index = 0; index < actual.length; index += 1) {
    mismatch |= actual.charCodeAt(index) ^ record.hash.charCodeAt(index);
  }
  return mismatch === 0;
}

export async function encryptEmail(email, env) {
  const key = await crypto.subtle.importKey(
    "raw", secretBytes(env.EMAIL_ENC_KEY, 32), { name: "AES-GCM" }, false, ["encrypt"]
  );
  const iv = crypto.getRandomValues(new Uint8Array(12));
  const cipher = await crypto.subtle.encrypt({ name: "AES-GCM", iv }, key, encoder.encode(email));
  return `v1.${base64UrlEncode(iv)}.${base64UrlEncode(new Uint8Array(cipher))}`;
}

export async function decryptEmail(value, env) {
  const [version, ivRaw, cipherRaw] = String(value || "").split(".");
  if (version !== "v1" || !ivRaw || !cipherRaw) throw new Error("invalid encrypted email");
  const key = await crypto.subtle.importKey(
    "raw", secretBytes(env.EMAIL_ENC_KEY, 32), { name: "AES-GCM" }, false, ["decrypt"]
  );
  const plain = await crypto.subtle.decrypt(
    { name: "AES-GCM", iv: base64UrlDecode(ivRaw) }, key, base64UrlDecode(cipherRaw)
  );
  return decoder.decode(plain);
}

export async function emailHash(email, env) {
  return hmacHex(env.UNSUB_HMAC_KEY, email.trim().toLowerCase());
}

export function utf8ToBase64(value) {
  return bytesToBase64(encoder.encode(value));
}

export function base64ToUtf8(value) {
  return decoder.decode(base64ToBytes(value.replace(/\s/g, "")));
}

export function escapeHtml(value) {
  return String(value).replace(/[&<>"']/g, (char) => ({
    "&": "&amp;", "<": "&lt;", ">": "&gt;", '"': "&quot;", "'": "&#39;"
  })[char]);
}
