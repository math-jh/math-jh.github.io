import { performance } from "node:perf_hooks";
import { base64UrlEncode, derivePassword } from "../src/lib.js";

const salt = base64UrlEncode(crypto.getRandomValues(new Uint8Array(16)));
const samples = 25;
for (const iterations of [5_000, 7_500, 10_000, 12_500, 15_000, 20_000]) {
  await derivePassword("benchmark-password", "benchmark-pepper", salt, iterations);
  const values = [];
  for (let index = 0; index < samples; index += 1) {
    const started = performance.now();
    await derivePassword("benchmark-password", "benchmark-pepper", salt, iterations);
    values.push(performance.now() - started);
  }
  values.sort((a, b) => a - b);
  const median = values[Math.floor(values.length / 2)];
  const p95 = values[Math.floor(values.length * 0.95)];
  process.stdout.write(`${iterations}\tmedian=${median.toFixed(3)}ms\tp95=${p95.toFixed(3)}ms\n`);
}
