import assert from "node:assert/strict";
import { createHmac } from "node:crypto";
import test from "node:test";
import {
  decryptEmail, derivePassword, encryptEmail, makePasswordRecord, parseCommentYaml,
  hmacHex, serializeComment, serializeTombstone, signToken, stripHtml, validateCommentPayload,
  verifyPassword, verifyToken, validateEditPayload
} from "../src/lib.js";
import { commentPayload, testEnv } from "./helpers.js";

test("HTML is removed while math delimiters remain", () => {
  assert.equal(stripHtml("<script>alert(1)</script> $x+y$ <b>bold</b>"), "alert(1) $x+y$ bold");
  assert.equal(stripHtml("<scr<script>ipt>alert(1)</scr</script>ipt>"), "alert(1)");
  assert.equal(stripHtml("Attribute probe\n{: onclick=\"alert(1)\"}"), "Attribute probe");
  assert.equal(stripHtml("Extension probe\n{::options parse_block_html=\"true\" /}"), "Extension probe");
});

test("validation enforces thread, unknown fields, timing, and link cap", () => {
  const valid = validateCommentPayload(commentPayload());
  assert.equal(valid.lang, "ko");
  assert.throws(() => validateCommentPayload(commentPayload({ thread: "../../_config" })), /invalid_thread/);
  assert.equal(
    validateCommentPayload(commentPayload({ thread: "ko__math__commutative_algebra__Jordan-Holder_theorem" })).thread,
    "ko__math__commutative_algebra__Jordan-Holder_theorem"
  );
  assert.throws(() => validateCommentPayload(commentPayload({ thread: "ko__math__a.b" })), /invalid_thread/);
  assert.throws(() => validateCommentPayload(commentPayload({ url: "https://spam.example" })), /unknown_field/);
  assert.throws(() => validateCommentPayload(commentPayload({ elapsed_ms: 2999 })), /too_fast/);
  assert.throws(() => validateCommentPayload(commentPayload({ honeypot: "bot" })), /honeypot/);
  assert.throws(() => validateCommentPayload(commentPayload({
    message: "https://a.example https://b.example https://c.example https://d.example"
  })), /too_many_links/);
  assert.throws(() => validateCommentPayload(commentPayload({
    message: "[click](javascript:alert(1))"
  })), /unsafe_content/);
});

test("YAML serializer contains no email, password, hash, or salt", () => {
  const yaml = serializeComment({
    id: "c-20260828-a3f1c9", name: "홍길동", message: "$x$", date: "2026-08-28T00:00:00Z",
    replying_to: "c-20260827-111111", mentions: ["c-20260826-222222"], notify: true, lang: "ko"
  });
  assert.deepEqual(parseCommentYaml(yaml), {
    id: "c-20260828-a3f1c9", name: "홍길동", message: "$x$", date: "2026-08-28T00:00:00Z",
    replying_to: "c-20260827-111111", mentions: ["c-20260826-222222"], notify: true, lang: "ko"
  });
  assert.doesNotMatch(yaml, /email|password|hash|salt|@/i);
});

test("tombstone drops identity, body, and notify", () => {
  const yaml = serializeTombstone({
    id: "c-20260828-a3f1c9", name: "Name", message: "secret", notify: true,
    date: "2026-08-28T00:00:00Z", lang: "ko"
  });
  assert.match(yaml, /deleted: true/);
  assert.doesNotMatch(yaml, /Name|secret|notify/);
});

test("email encryption round trips and does not expose plaintext", async () => {
  const env = testEnv();
  const encrypted = await encryptEmail("person@example.com", env);
  assert.doesNotMatch(encrypted, /person|example/);
  assert.equal(await decryptEmail(encrypted, env), "person@example.com");
});

test("PBKDF2 record verifies only the correct password", async () => {
  const env = testEnv();
  const record = await makePasswordRecord("deletion-only", env);
  assert.equal(await verifyPassword("deletion-only", record, env), true);
  assert.equal(await verifyPassword("wrong", record, env), false);
  assert.equal(record.iterations, 10000);
});

test("signed tokens reject tampering and wrong purpose", async () => {
  const env = testEnv();
  const token = await signToken(env.DELETE_HMAC_KEY, { purpose: "delete", id: "c-20260828-a3f1c9" });
  assert.equal((await verifyToken(env.DELETE_HMAC_KEY, token, "delete")).id, "c-20260828-a3f1c9");
  await assert.rejects(() => verifyToken(env.DELETE_HMAC_KEY, `${token}x`, "delete"), /invalid_token/);
  await assert.rejects(() => verifyToken(env.DELETE_HMAC_KEY, token, "unsub"), /invalid_token/);
});

test("HMAC secrets use the same raw string bytes as the notification workflow", async () => {
  const secret = "0123456789abcdef".repeat(4);
  const value = '{"comments":[]}';
  const expected = createHmac("sha256", secret).update(value).digest("hex");
  assert.equal(await hmacHex(secret, value), expected);
});

test("edit payload shares the message rules and rejects extra fields", () => {
  const base = {
    id: "c-20260828-a3f1c9",
    thread: "ko__math__test_post",
    password: "throwaway-key",
    message: "<b>after</b> $x^2$"
  };
  assert.equal(validateEditPayload(base).message, "after $x^2$");
  assert.throws(() => validateEditPayload({ ...base, name: "spoof" }), /unknown_field/);
  assert.throws(() => validateEditPayload({ ...base, id: "not-an-id" }), /invalid_edit_request/);
  assert.throws(() => validateEditPayload({ ...base, thread: "../../_config" }), /invalid_thread/);
  assert.throws(() => validateEditPayload({ ...base, password: "abc" }), /invalid_password/);
  assert.throws(() => validateEditPayload({ ...base, message: "   " }), /invalid_message/);
  assert.throws(() => validateEditPayload({
    ...base,
    message: "https://a.example https://b.example https://c.example https://d.example"
  }), /too_many_links/);
  assert.throws(() => validateEditPayload({
    ...base, message: "[click](javascript:alert(1))"
  }), /unsafe_content/);
});

test("serializer carries the hand-added role key and the edit timestamp", () => {
  const yaml = serializeComment({
    id: "c-20260828-a3f1c9", name: "Marvin", message: "body", date: "2026-08-28T00:00:00Z",
    role: "bot", edited: "2026-08-29T01:00:00Z", lang: "ko"
  });
  assert.match(yaml, /role: "bot"/);
  assert.match(yaml, /edited: "2026-08-29T01:00:00Z"/);
});
