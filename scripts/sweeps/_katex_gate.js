// dd_apply.py 의 렌더 게이트. {macrosJs, texs} JSON 을 받아 실패한 것만 돌려준다.
// 매크로는 정규식으로 긁지 않고 katex-macros.js 를 실제로 실행해 읽는다
// (전개형에 JSON 이 아닌 이스케이프가 섞여 있어 정적 파싱이 깨진다).
const fs = require('fs');
const vm = require('vm');
const katex = require('katex');

const { macrosJs, texs } = JSON.parse(fs.readFileSync(process.argv[2], 'utf8'));
const sandbox = { window: {} };
vm.createContext(sandbox);
vm.runInContext(fs.readFileSync(macrosJs, 'utf8'), sandbox);
const macros = sandbox.window.KATEX_MACROS || {};

const bad = [];
for (const item of texs) {
  const tex = typeof item === 'string' ? item : item.tex;
  const displayMode = typeof item === 'string' ? false : !!item.display;
  try {
    katex.renderToString(tex, {
      output: 'html', throwOnError: true, strict: false, displayMode,
      macros: Object.assign({}, macros),
    });
  } catch (e) {
    bad.push(tex.slice(0, 60) + ' -> ' + String(e.message).slice(0, 90));
  }
}
process.stdout.write(JSON.stringify(bad));
