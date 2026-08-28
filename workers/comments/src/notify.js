import {
  PublicError, decryptEmail, emailHash, escapeHtml, signToken, threadPermalink
} from "./lib.js";

const SUB_TTL = 400 * 24 * 60 * 60;

function workerBase(env) {
  return env.COMMENTS_BASE_URL || "https://comments.math-jh.com";
}

async function subscription(env, id) {
  if (!id) return null;
  const record = await env.COMMENTS_KV.get(`sub:${id}`, "json");
  if (!record?.emailEnc) return null;
  return { ...record, id, email: await decryptEmail(record.emailEnc, env) };
}

async function optedOut(env, email, threadKey) {
  const hash = await emailHash(email, env);
  const [global, thread] = await Promise.all([
    env.COMMENTS_KV.get(`optout:${hash}`),
    env.COMMENTS_KV.get(`optout:${hash}:${threadKey}`)
  ]);
  return Boolean(global || thread);
}

async function unsubscribeLinks(env, email, threadKey) {
  const exp = Math.floor(Date.now() / 1000) + SUB_TTL;
  const globalToken = await signToken(env.UNSUB_HMAC_KEY, {
    purpose: "unsub", email, scope: "global", exp
  });
  const threadToken = await signToken(env.UNSUB_HMAC_KEY, {
    purpose: "unsub", email, scope: "thread", threadKey, exp
  });
  return {
    global: `${workerBase(env)}/v1/unsub?t=${encodeURIComponent(globalToken)}`,
    thread: `${workerBase(env)}/v1/unsub?t=${encodeURIComponent(threadToken)}`,
    globalToken
  };
}

async function deletionLink(env, id, threadKey) {
  const token = await signToken(env.DELETE_HMAC_KEY, { purpose: "delete", id, threadKey });
  return `${workerBase(env)}/v1/delete?t=${encodeURIComponent(token)}`;
}

function copyFor(lang, comment, reasons) {
  const isKo = lang === "ko";
  const reason = reasons.has("approved")
    ? (isKo ? "댓글이 승인되었습니다." : "Your comment was approved.")
    : reasons.has("reply") && reasons.has("mention")
      ? (isKo ? "댓글에 답글과 멘션이 등록되었습니다." : "A reply and mention were added to your comment.")
      : reasons.has("reply")
        ? (isKo ? "댓글에 답글이 등록되었습니다." : "A reply was added to your comment.")
        : (isKo ? "댓글에서 회원님을 멘션했습니다." : "You were mentioned in a comment.");
  return {
    subject: isKo ? `[Blackbox] ${reason}` : `[Blackbox] ${reason}`,
    reason,
    by: isKo ? `${comment.name} 작성` : `By ${comment.name}`,
    view: isKo ? "댓글 보기" : "View comment",
    remove: isKo ? "내 댓글 삭제" : "Delete my comment",
    unsubThread: isKo ? "이 글의 알림 끄기" : "Unsubscribe from this thread",
    unsubGlobal: isKo ? "모든 댓글 알림 끄기" : "Unsubscribe from all comment email"
  };
}

async function sendEmail(env, { recipient, comment, reasons }) {
  const lang = recipient.lang === "en" ? "en" : "ko";
  const copy = copyFor(lang, comment, reasons);
  const permalink = `https://math-jh.com${comment.permalink || threadPermalink(comment.threadKey)}#comment-${comment.id}`;
  const unsub = await unsubscribeLinks(env, recipient.email, comment.threadKey);
  const remove = await deletionLink(env, recipient.id, recipient.threadKey);
  const text = [
    copy.reason,
    copy.by,
    "",
    comment.message || "",
    "",
    `${copy.view}: ${permalink}`,
    `${copy.remove}: ${remove}`,
    `${copy.unsubThread}: ${unsub.thread}`,
    `${copy.unsubGlobal}: ${unsub.global}`
  ].join("\n");
  const html = `<!doctype html><html><body>
    <p>${escapeHtml(copy.reason)}</p>
    <p><strong>${escapeHtml(copy.by)}</strong></p>
    <blockquote>${escapeHtml(comment.message || "").replaceAll("\n", "<br>")}</blockquote>
    <p><a href="${escapeHtml(permalink)}">${escapeHtml(copy.view)}</a></p>
    <p><a href="${escapeHtml(remove)}">${escapeHtml(copy.remove)}</a></p>
    <hr><p><a href="${escapeHtml(unsub.thread)}">${escapeHtml(copy.unsubThread)}</a> ·
    <a href="${escapeHtml(unsub.global)}">${escapeHtml(copy.unsubGlobal)}</a></p>
  </body></html>`;
  const recipientHash = await emailHash(recipient.email, env);
  const response = await fetch("https://api.resend.com/emails", {
    method: "POST",
    headers: {
      authorization: `Bearer ${env.RESEND_API_KEY}`,
      "content-type": "application/json",
      "idempotency-key": `comment/${comment.id}/${recipientHash.slice(0, 24)}`
    },
    body: JSON.stringify({
      from: "Marvin <marvin@math-jh.com>",
      to: [recipient.email],
      reply_to: "marvin@math-jh.com",
      subject: copy.subject,
      text,
      html,
      headers: {
        "List-Unsubscribe": `<${unsub.global}>`,
        "List-Unsubscribe-Post": "List-Unsubscribe=One-Click"
      }
    })
  });
  if (!response.ok) throw new Error(`Resend API ${response.status}`);
}

export async function notifyComments(env, input) {
  if (!Array.isArray(input.comments) || input.comments.length > 10_000) {
    throw new PublicError(400, "invalid_payload");
  }
  const epoch = Date.parse(env.NOTIFY_EPOCH || "");
  if (!Number.isFinite(epoch)) throw new Error("invalid NOTIFY_EPOCH");
  let sent = 0;
  let ignoredBeforeEpoch = 0;

  for (const raw of input.comments) {
    const comment = {
      id: String(raw.id || ""),
      threadKey: String(raw.threadKey || ""),
      permalink: String(raw.permalink || ""),
      date: String(raw.date || ""),
      replying_to: raw.replying_to ? String(raw.replying_to) : undefined,
      mentions: Array.isArray(raw.mentions) ? [...new Set(raw.mentions.map(String))].slice(0, 3) : [],
      name: String(raw.name || ""),
      message: String(raw.message || ""),
      lang: raw.lang === "en" ? "en" : "ko"
    };
    const timestamp = Date.parse(comment.date);
    if (!comment.id || !comment.threadKey || !Number.isFinite(timestamp)) {
      throw new PublicError(400, "invalid_payload");
    }
    if (timestamp < epoch) {
      ignoredBeforeEpoch += 1;
      continue;
    }

    const kinds = {
      approved: !(await env.COMMENTS_KV.get(`notified:${comment.id}:approved`)),
      reply: Boolean(comment.replying_to) && !(await env.COMMENTS_KV.get(`notified:${comment.id}:reply`)),
      mention: comment.mentions.length > 0 && !(await env.COMMENTS_KV.get(`notified:${comment.id}:mention`))
    };
    if (!Object.values(kinds).some(Boolean)) continue;

    const own = await subscription(env, comment.id);
    const targets = [];
    if (kinds.approved && own) targets.push({ sub: own, reason: "approved" });
    if (kinds.reply) {
      const parent = await subscription(env, comment.replying_to);
      if (parent) targets.push({ sub: parent, reason: "reply" });
    }
    if (kinds.mention) {
      for (const id of comment.mentions) {
        const mentioned = await subscription(env, id);
        if (mentioned) targets.push({ sub: mentioned, reason: "mention" });
      }
    }

    const recipients = new Map();
    for (const target of targets) {
      if (target.reason !== "approved" && own && target.sub.email === own.email) continue;
      if (await optedOut(env, target.sub.email, comment.threadKey)) continue;
      const key = await emailHash(target.sub.email, env);
      const entry = recipients.get(key) || { ...target.sub, reasons: new Set() };
      entry.reasons.add(target.reason);
      recipients.set(key, entry);
    }
    for (const recipient of recipients.values()) {
      await sendEmail(env, { recipient, comment, reasons: recipient.reasons });
      sent += 1;
    }
    const writes = [];
    if (kinds.approved) writes.push(env.COMMENTS_KV.put(`notified:${comment.id}:approved`, "1"));
    if (kinds.reply) writes.push(env.COMMENTS_KV.put(`notified:${comment.id}:reply`, "1"));
    if (kinds.mention) writes.push(env.COMMENTS_KV.put(`notified:${comment.id}:mention`, "1"));
    await Promise.all(writes);
  }
  return { sent, ignored_before_epoch: ignoredBeforeEpoch };
}

export async function removeSubscriptions(env, email, scope, threadKey) {
  const hash = await emailHash(email, env);
  const optoutKey = scope === "thread" ? `optout:${hash}:${threadKey}` : `optout:${hash}`;
  await env.COMMENTS_KV.put(optoutKey, "1");
  let cursor;
  do {
    const listed = await env.COMMENTS_KV.list({ prefix: "sub:", cursor });
    for (const key of listed.keys) {
      const record = await env.COMMENTS_KV.get(key.name, "json");
      if (!record?.emailEnc || (scope === "thread" && record.threadKey !== threadKey)) continue;
      let candidate;
      try { candidate = await decryptEmail(record.emailEnc, env); } catch { continue; }
      if (candidate.trim().toLowerCase() === email.trim().toLowerCase()) {
        await env.COMMENTS_KV.delete(key.name);
      }
    }
    cursor = listed.list_complete ? undefined : listed.cursor;
  } while (cursor);
}
