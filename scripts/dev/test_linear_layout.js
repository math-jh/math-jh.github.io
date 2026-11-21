/* assets/js/custom/Linear_layout.js 의 불변식 테스트.
 *
 *   node --test scripts/dev/test_linear_layout.js
 *
 * 그래프 데이터의 선은 선수 글 → 후속 글이다 (forward 만 현재 글 → 나중 글).
 */
'use strict';
const assert = require('node:assert/strict');
const fs = require('node:fs');
const path = require('node:path');
const test = require('node:test');
const vm = require('node:vm');

const SOURCE = path.join(__dirname, '..', '..', 'assets', 'js', 'custom', 'Linear_layout.js');
const sandbox = { window: {} };
vm.runInNewContext(fs.readFileSync(SOURCE, 'utf8'), sandbox, { filename: SOURCE });
const L = sandbox.window.LinearLayout;

function node(id, category, weight) {
  return { id: id, title: id, category: category || 'c', weight: weight === undefined ? 1 : weight };
}
function link(source, target, relation) {
  return { source: source, target: target, relation: relation || 'required', weight: 1 };
}
function columnsOf(nodes, links) { return L.readingColumns({ nodes: nodes, links: links }).column; }

test('required 사슬은 왼쪽에서 오른쪽으로 놓인다', () => {
  const column = columnsOf([node('a'), node('b'), node('c')], [link('a', 'b'), link('b', 'c')]);
  assert.ok(column.a < column.b && column.b < column.c);
});

test('required 순환은 한 열에 묶이고, 순환 밖 글은 그 뒤에 온다', () => {
  const column = columnsOf([node('a'), node('b'), node('c')],
    [link('a', 'b'), link('b', 'a'), link('b', 'c')]);
  assert.equal(column.a, column.b);
  assert.ok(column.b < column.c);
});

test('weak 선수 글은 카테고리 순번이 뒤여도 후속 글보다 왼쪽이다', () => {
  // late 는 자기 카테고리의 여섯 번째 글이라 하한이 5 이고, early 는 다른 카테고리의 첫 글이다.
  const nodes = [0, 1, 2, 3, 4].map(i => node('pad' + i, 'x', i)).concat([node('late', 'x', 9), node('early', 'y', 1)]);
  const column = columnsOf(nodes, [link('late', 'early', 'weak')]);
  assert.ok(column.late < column.early);
});

test('required 사슬과 반대로 가는 weak 선은 버린다', () => {
  const column = columnsOf([node('a'), node('b'), node('c')],
    [link('a', 'b'), link('b', 'c'), link('c', 'a', 'weak')]);
  assert.ok(column.a < column.b && column.b < column.c);
});

test('서로를 weak 으로 가리키는 두 글도 배치된다', () => {
  const column = columnsOf([node('a'), node('b')], [link('a', 'b', 'weak'), link('b', 'a', 'weak')]);
  assert.notEqual(column.a, column.b);
});

test('선수 글이 없는 글은 밀려난 후속 글 바로 앞 열로 당겨진다', () => {
  // v 는 긴 사슬 끝의 weak 선에 밀려 오른쪽으로 가고, s 는 v 만 후속 글로 둔다.
  const nodes = [0, 1, 2, 3, 4].map(i => node('p' + i, 'x', i)).concat([node('s', 'y', 1), node('v', 'y', 2)]);
  const links = [0, 1, 2, 3].map(i => link('p' + i, 'p' + (i + 1))).concat([link('p4', 'v', 'weak'), link('s', 'v')]);
  const column = columnsOf(nodes, links);
  assert.ok(column.p4 < column.v);
  assert.equal(column.v - column.s, 1);
});

test('무작위 그래프: required 순서, 열 번호, 입력 순서 무관', () => {
  let seed = 7;
  const random = () => { seed = (seed * 1103515245 + 12345) & 0x7fffffff; return seed / 0x7fffffff; };
  const shuffled = list => {
    const out = list.slice();
    for (let i = out.length - 1; i > 0; i--) {
      const j = Math.floor(random() * (i + 1));
      [out[i], out[j]] = [out[j], out[i]];
    }
    return out;
  };
  for (let run = 0; run < 200; run++) {
    const count = 5 + Math.floor(random() * 50), nodes = [], links = [], seen = new Set();
    for (let i = 0; i < count; i++) {
      nodes.push(node('n' + i, 'c' + Math.floor(random() * 4), random() < 0.1 ? null : Math.floor(random() * 20)));
    }
    for (let k = Math.floor(random() * count * 3); k > 0; k--) {
      let a = Math.floor(random() * count), b = Math.floor(random() * count);
      if (a === b) continue;
      if (random() < 0.85 && a > b) [a, b] = [b, a];        // 대체로 앞 → 뒤, 가끔 거꾸로(순환)
      if (seen.has(a + '>' + b)) continue;
      seen.add(a + '>' + b);
      const r = random();
      links.push(link('n' + a, 'n' + b, r < 0.6 ? 'required' : r < 0.95 ? 'weak' : 'forward'));
    }
    const result = L.readingColumns({ nodes: nodes, links: links });
    const column = result.column;

    // 열 번호는 0 부터 빈 번호 없이 이어진다.
    const used = new Set(nodes.map(n => column[n.id]));
    assert.equal(used.size, result.columns);
    assert.equal(Math.min(...used), 0);
    assert.equal(Math.max(...used), result.columns - 1);

    // required 는 오른쪽에서 왼쪽으로 가지 않고, 같은 열이면 서로 required 로 닿는 순환이다.
    const next = {};
    links.forEach(l => { if (l.relation === 'required') (next[l.source] = next[l.source] || []).push(l.target); });
    const reaches = (from, to) => {
      const todo = [from], visited = new Set();
      while (todo.length) {
        const here = todo.pop();
        if (here === to) return true;
        if (visited.has(here)) continue;
        visited.add(here);
        (next[here] || []).forEach(n => todo.push(n));
      }
      return false;
    };
    links.forEach(l => {
      if (l.relation !== 'required') return;
      assert.ok(column[l.source] <= column[l.target]);
      if (column[l.source] === column[l.target]) assert.ok(reaches(l.target, l.source));
    });

    // 글·선의 나열 순서를 섞어도 열은 같다.
    const again = L.readingColumns({ nodes: shuffled(nodes), links: shuffled(links) }).column;
    nodes.forEach(n => assert.equal(again[n.id], column[n.id]));

    // 레인 배정까지 예외 없이 끝나고 모든 글이 레인을 받는다.
    const ranks = L.readingParents({ nodes: nodes, links: links }, column);
    const lanes = L.lanes(ranks.order, ranks.parents, ranks.depth, ranks.degree, column);
    nodes.forEach(n => assert.ok(Number.isInteger(lanes.lane[n.id])));
  }
});

// linkPath 가 내는 d 의 좌표를 명령별로 읽는다.
function commands(d) {
  const out = [];
  d.replace(/([MLC])([^MLC]*)/g, (_, name, rest) => {
    out.push({ name: name, numbers: rest.split(/[ ,]+/).filter(Boolean).map(Number) });
  });
  return out;
}

test('선은 M·L·C 명령만 쓴다 (Local_graph.js 의 trace 가 이 셋만 읽는다)', () => {
  const s = { x: 0, y: 0 };
  [[200, 0], [200, 36], [200, -36], [10, 24], [-200, 12], [-200, 0]].forEach(([x, y]) => {
    [true, false].forEach(first => {
      const d = L.linkPath(s, { x: x, y: y }, first, 1, 12);
      assert.match(d, /^M[-\d.,e ]+(?: [LC][-\d.,e ]+)+$/);
      assert.ok(!/NaN|Infinity|undefined/.test(d));
    });
  });
});

test('첫 부모 선은 같은 레인에서 직선이다', () => {
  assert.equal(L.linkPath({ x: 0, y: 0 }, { x: 200, y: 0 }, true, 1, 12), 'M0,0 L200,0');
});

test('합류선은 출발 글의 레인이 아니라 레인 사이 빈 줄을 따라 간다', () => {
  const gap = 12;
  [[200, 36, 6], [200, -36, -6], [200, 0, 6], [-200, 24, 6]].forEach(([x, y, row]) => {
    const line = commands(L.linkPath({ x: 0, y: 0 }, { x: x, y: y }, false, 1, gap)).find(c => c.name === 'L');
    assert.ok(line, 'no straight run');
    assert.equal(line.numbers[1], row);
  });
});
