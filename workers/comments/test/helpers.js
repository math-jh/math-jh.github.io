export class MemoryKV {
  constructor(entries = {}) {
    this.values = new Map(Object.entries(entries));
  }
  async get(key, type) {
    const value = this.values.get(key);
    if (value === undefined) return null;
    if (type === "json") return JSON.parse(value);
    return value;
  }
  async put(key, value) { this.values.set(key, String(value)); }
  async delete(key) { this.values.delete(key); }
  async list({ prefix = "" } = {}) {
    return {
      keys: [...this.values.keys()].filter((key) => key.startsWith(prefix)).map((name) => ({ name })),
      list_complete: true
    };
  }
}

export function testEnv(overrides = {}) {
  return {
    ALLOWED_ORIGINS: "https://math-jh.com,https://preview.math-jh.com",
    TURNSTILE_SECRET: "turnstile-secret",
    TURNSTILE_ACTION: "comment_submit",
    TURNSTILE_HOSTNAMES: "math-jh.com,preview.math-jh.com",
    GITHUB_OWNER: "math-jh",
    GITHUB_REPO: "math-jh.github.io",
    GITHUB_BRANCH: "main",
    GITHUB_TOKEN: "github-token",
    PASSWORD_PEPPER: "pepper-that-is-not-in-kv",
    PBKDF2_ITERATIONS: "10000",
    EMAIL_ENC_KEY: "AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA",
    NOTIFY_HMAC_KEY: "notify-hmac-key-with-enough-entropy",
    UNSUB_HMAC_KEY: "unsub-hmac-key-with-enough-entropy",
    DELETE_HMAC_KEY: "delete-hmac-key-with-enough-entropy",
    RESEND_API_KEY: "resend-key",
    NOTIFY_EPOCH: "2026-08-28T00:00:00Z",
    COMMENTS_KV: new MemoryKV(),
    ...overrides
  };
}

export function commentPayload(overrides = {}) {
  return {
    turnstile_token: "valid-token",
    honeypot: "",
    elapsed_ms: 3500,
    name: "Tester",
    password: "throwaway-key",
    email: "test@example.com",
    message: "A comment with $x^2$.",
    thread: "ko__math__test_post",
    replying_to: "",
    mentions: [],
    ...overrides
  };
}

export function jsonRequest(path, value, headers = {}) {
  return new Request(`https://comments.example${path}`, {
    method: "POST",
    headers: { "content-type": "application/json", origin: "https://math-jh.com", ...headers },
    body: JSON.stringify(value)
  });
}
