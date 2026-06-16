#!/usr/bin/env node
/*
 * KaTeX parse-error audit for all Math posts.
 *
 * Renders every $$...$$ block (and single-$ math inside <cap>/<phrase>/<em-ko>
 * tags) with the blog's OWN macros (assets/js/katex-macros.js) and the same
 * options as _includes/scripts.html (macros + strict:false) — but with
 * throwOnError:true, so it CATCHES anything that would otherwise render as a red
 * katex-error on the page. Loading the macros is essential: without them every
 * custom command (\Gr, \Spec, \Ad, …) is a false "undefined control sequence".
 *
 * Usage:  node scripts/audit/katex_audit.js
 * Exit:   0 if no parse errors, 1 otherwise. (Glyph warnings on stderr are noise.)
 */
const fs = require('fs');
const path = require('path');

const REPO = path.resolve(__dirname, '..', '..');
const katex = require(path.join(REPO, 'assets/katex/katex.min.js'));

// load window.KATEX_MACROS by executing the macro file with a window shim
const win = {};
new Function('window', fs.readFileSync(path.join(REPO, 'assets/js/katex-macros.js'), 'utf8'))(win);
const MACROS = win.KATEX_MACROS || {};

const MATH_ROOT = path.join(REPO, '_posts/Math');

function walk(d, acc) {
  for (const e of fs.readdirSync(d, { withFileTypes: true })) {
    const p = path.join(d, e.name);
    if (e.isDirectory()) walk(p, acc);
    else if (e.name.endsWith('.md') && e.name !== 'CLAUDE.md') acc.push(p);
  }
  return acc;
}

// drop frontmatter, fenced code blocks, {% raw %} blocks, and inline `code`
function stripNonMath(src) {
  const lines = src.split('\n');
  const out = [];
  let inFence = false, fence = '', inRaw = false, inFront = false;
  for (let i = 0; i < lines.length; i++) {
    const ln = lines[i];
    if (i === 0 && ln.trim() === '---') { inFront = true; continue; }
    if (inFront) { if (ln.trim() === '---') inFront = false; continue; }
    const fm = ln.match(/^(\s*)(```+|~~~+)/);
    if (!inFence && fm) { inFence = true; fence = fm[2][0]; continue; }
    else if (inFence) { if (ln.match(/^(\s*)(```+|~~~+)\s*$/) && ln.includes(fence)) inFence = false; continue; }
    if (ln.includes('{% raw %}')) inRaw = true;
    if (inRaw) { if (ln.includes('{% endraw %}')) inRaw = false; continue; }
    out.push(ln);
  }
  return out.join('\n').replace(/`[^`\n]*`/g, ' ');
}

function extract(src) {
  const text = stripNonMath(src);
  const items = [];
  let m;
  const dd = /\$\$([\s\S]+?)\$\$/g;           // $$ display $$
  while ((m = dd.exec(text)) !== null) items.push({ tex: m[1], display: true });
  const tag = /<(cap|phrase|em-ko)\b[^>]*>([\s\S]*?)<\/\1>/g;   // single-$ in custom inline tags
  let t;
  while ((t = tag.exec(text)) !== null) {
    const sre = /(?<!\$)\$(?!\$)([^$\n]+?)\$(?!\$)/g;
    let s;
    while ((s = sre.exec(t[2])) !== null) items.push({ tex: s[1], display: false });
  }
  return items;
}

const files = walk(MATH_ROOT, []);
let totalMath = 0, totalErr = 0;
const report = [];
for (const f of files) {
  const items = extract(fs.readFileSync(f, 'utf8'));
  const errs = [];
  for (const it of items) {
    totalMath++;
    try {
      katex.renderToString(it.tex, { macros: { ...MACROS }, strict: false, throwOnError: true, displayMode: it.display });
    } catch (e) {
      totalErr++;
      errs.push({
        msg: String(e.message || e).replace(/\n/g, ' ').slice(0, 160),
        tex: it.tex.trim().replace(/\s+/g, ' ').slice(0, 110),
      });
    }
  }
  if (errs.length) report.push({ file: path.relative(REPO, f), errs });
}

console.log(`posts scanned: ${files.length} | math exprs: ${totalMath} | parse errors: ${totalErr} | posts with errors: ${report.length}\n`);
for (const r of report) {
  console.log(`### ${r.file}  (${r.errs.length})`);
  for (const e of r.errs) console.log(`   ✗ ${e.msg}\n       in: ${e.tex}`);
}
process.exit(totalErr ? 1 : 0);
