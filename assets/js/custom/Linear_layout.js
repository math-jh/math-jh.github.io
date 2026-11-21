/* Linear_layout.js — 의존성 그래프의 선형 배치. git 커밋 그래프의 본선(first-parent) 문법을
 * 빌린다 — x 는 읽는 순서의 열이고 y 는 레인이다. 각 글은 선수 글 하나를 '첫 부모'로 골라 그
 * 레인을 이어 간다.
 *
 * 전역 그래프 페이지의 선형 보기(Graph_page.js)와 수학 글 사이드바의 로컬 그래프
 * (Local_graph.js)가 같이 쓴다. 열·첫 부모·레인과 선·라벨 상자의 모양은 여기서 정하고,
 * 화면 크기에 맞춘 x·y 배치와 그리기는 각 쪽이 한다. window.LinearLayout 으로 내보낸다.
 *
 * 불변식 테스트: node --test scripts/dev/test_linear_layout.js
 */
(function () {
  'use strict';

  function endpoints(l) {
    return [typeof l.source === 'object' ? l.source.id : l.source,
            typeof l.target === 'object' ? l.target.id : l.target];
  }
  function lid(l) {
    if (l.__lid) return l.__lid;
    var e = endpoints(l); return e[0] + '>' + e[1];
  }

  // 글마다 고정된 [0, 1) 값 (FNV-1a). 배치의 흔들림이 새로고침마다 바뀌지 않게 한다.
  function unitHash(text) {
    var h = 2166136261;
    for (var i = 0; i < text.length; i++) { h ^= text.charCodeAt(i); h = Math.imul(h, 16777619); }
    return ((h >>> 0) % 10000) / 10000;
  }

  /* 열: required SCC를 한 층으로 축약한 뒤 forward, weak 순으로 순환 없는 소프트
     제약을 더한다. 그래서 선수 글은 required든 weak든 후속 글보다 왼쪽 열에 온다.
     예외는 required 사슬이나 먼저 넣은 소프트 제약과 반대로 가는 선뿐이다. weak는
     required·forward만으로 낸 층에서 여유가 큰 선부터 넣는다 — 순환에서 버려지는
     쪽이 그 층과 가장 크게 어긋난 선이 되고, 열도 덜 늘어난다.
     카테고리 안의 순번(weight 순으로 0, 1, 2…)은 층의 하한으로만 쓴다. 선이 없는
     글이 한 열에 쌓이지 않고 가로로 흩어지게 하는 값이고, 카테고리 안의 순서를
     지켜 주지는 않는다 — 선수 글에 밀린 글은 같은 카테고리의 뒤 글보다 오른쪽에
     올 수 있다. */
  function readingColumns(data) {
    var nodes = data.nodes, reqAdj = {};
    nodes.forEach(function (n) { reqAdj[n.id] = []; });
    data.links.forEach(function (l) {
      var e = endpoints(l);
      if (l.relation === 'required' && reqAdj[e[0]]) reqAdj[e[0]].push(e[1]);
    });

    var serial = 0, stack = [], onStack = {}, index = {}, low = {}, compOf = {}, comps = [];
    function visit(id) {
      index[id] = serial; low[id] = serial; serial += 1;
      stack.push(id); onStack[id] = true;
      (reqAdj[id] || []).forEach(function (next) {
        if (index[next] === undefined) { visit(next); low[id] = Math.min(low[id], low[next]); }
        else if (onStack[next]) low[id] = Math.min(low[id], index[next]);
      });
      if (low[id] !== index[id]) return;
      var comp = [], member;
      do {
        member = stack.pop(); onStack[member] = false;
        compOf[member] = comps.length; comp.push(member);
      } while (member !== id);
      comps.push(comp);
    }
    nodes.forEach(function (n) { if (index[n.id] === undefined) visit(n.id); });

    var adj = comps.map(function () { return new Set(); });
    function addEdge(a, b) { if (a !== b) adj[a].add(b); }
    data.links.forEach(function (l) {
      if (l.relation !== 'required') return;
      var e = endpoints(l); addEdge(compOf[e[0]], compOf[e[1]]);
    });
    function reaches(from, target) {
      var todo = [from], seen = new Set();
      while (todo.length) {
        var here = todo.pop();
        if (here === target) return true;
        if (seen.has(here)) continue;
        seen.add(here); adj[here].forEach(function (next) { todo.push(next); });
      }
      return false;
    }
    // 소프트 제약 한 묶음을 순서대로 더한다. 이미 있는 순서와 순환을 만드는 선은 버린다.
    function addSoft(links) {
      links.forEach(function (l) {
        var e = endpoints(l), a = compOf[e[0]], b = compOf[e[1]];
        if (a !== b && !reaches(b, a)) addEdge(a, b);
      });
    }

    // raw weight는 카테고리 사이에서 비교할 수 없다. 각 카테고리를 따로 정렬해
    // 빈 구간을 제거한 순번만 층의 하한으로 넘긴다.
    var categoryNodes = {}, categoryRank = {};
    nodes.forEach(function (n) {
      var category = n.category || '';
      (categoryNodes[category] = categoryNodes[category] || []).push(n);
    });
    Object.keys(categoryNodes).forEach(function (category) {
      categoryNodes[category].sort(function (a, b) {
        var aw = Number(a.weight), bw = Number(b.weight);
        var aMissing = a.weight === null || a.weight === undefined || a.weight === '' || !isFinite(aw);
        var bMissing = b.weight === null || b.weight === undefined || b.weight === '' || !isFinite(bw);
        return aMissing - bMissing || (aMissing ? 0 : aw - bw) ||
          a.title.localeCompare(b.title) || a.id.localeCompare(b.id);
      }).forEach(function (n, i) { categoryRank[n.id] = i; });
    });
    var base = comps.map(function (members) {
      return members.reduce(function (best, id) {
        return Math.max(best, categoryRank[id] || 0);
      }, 0);
    });
    // 지금까지 넣은 제약으로 낸 층. 선이 가리키는 쪽이 늘 더 뒤 층이다.
    function layers() {
      var indeg = comps.map(function () { return 0; });
      adj.forEach(function (nexts) { nexts.forEach(function (v) { indeg[v] += 1; }); });
      var rank = base.slice();
      var ready = comps.map(function (_, i) { return i; }).filter(function (i) { return indeg[i] === 0; });
      while (ready.length) {
        var current = ready.pop();
        adj[current].forEach(function (next) {
          rank[next] = Math.max(rank[next], rank[current] + 1);
          indeg[next] -= 1;
          if (indeg[next] === 0) ready.push(next);
        });
      }
      return rank;
    }

    function byLid(a, b) { return lid(a).localeCompare(lid(b)); }
    addSoft(data.links.filter(function (l) { return l.relation === 'forward'; }).sort(byLid));
    var before = layers();
    function slack(l) { var e = endpoints(l); return before[compOf[e[1]]] - before[compOf[e[0]]]; }
    addSoft(data.links.filter(function (l) { return l.relation === 'weak'; })
      .sort(function (a, b) { return slack(b) - slack(a) || byLid(a, b); }));
    var rank = layers();

    /* 당기기. layers 는 글을 놓일 수 있는 가장 왼쪽 층에 두므로, 후속 글이 다른 선수 글에
       밀려 오른쪽으로 가도 이 글은 제자리에 남아 둘 사이가 벌어진다. 뒤 층부터 훑으며 글마다
       후속 글 바로 앞 층까지의 범위 안에서 이웃(선수·후속 글)들의 가운데 층으로 옮긴다.
       오른쪽으로만 옮기므로 이미 지켜진 순서는 그대로다. */
    var back = comps.map(function () { return []; });
    adj.forEach(function (nexts, from) { nexts.forEach(function (to) { back[to].push(from); }); });
    comps.map(function (_, i) { return i; })
      .sort(function (a, b) { return rank[b] - rank[a] || a - b; })
      .forEach(function (c) {
        if (!adj[c].size) return;
        var around = back[c].map(function (p) { return rank[p]; }), latest = Infinity;
        adj[c].forEach(function (next) { around.push(rank[next]); latest = Math.min(latest, rank[next] - 1); });
        around.sort(function (a, b) { return a - b; });
        var middle = around[Math.floor((around.length - 1) / 2)];
        rank[c] = Math.max(rank[c], Math.min(latest, middle));
      });

    var used = Array.from(new Set(rank)).sort(function (a, b) { return a - b; });
    var compressed = {}; used.forEach(function (value, i) { compressed[value] = i; });
    var column = {};
    nodes.forEach(function (n) { column[n.id] = compressed[rank[compOf[n.id]]]; });
    return { column: column, columns: used.length };
  }

  // 열 순서대로 늘어놓은 글 목록. 같은 열 안은 id 순이다.
  function columnOrder(ids, column) {
    return ids.slice().sort(function (a, b) {
      return column[a] - column[b] || (a < b ? -1 : a > b ? 1 : 0);
    });
  }

  // 첫 부모 후보는 왼쪽 열에 있는 required 선수 글이다. 깊이 = 진입점에서 오는 가장 긴 사슬.
  function readingParents(data, column) {
    var order = columnOrder(data.nodes.map(function (n) { return n.id; }), column);
    var degree = {}, parents = {};
    order.forEach(function (id) { parents[id] = []; });
    data.links.forEach(function (l) {
      var e = endpoints(l);
      degree[e[0]] = (degree[e[0]] || 0) + 1;
      degree[e[1]] = (degree[e[1]] || 0) + 1;
      if (l.relation === 'required' && parents[e[1]] && column[e[0]] < column[e[1]]) parents[e[1]].push(e[0]);
    });
    var depth = {};
    order.forEach(function (id) {
      depth[id] = parents[id].reduce(function (m, p) { return Math.max(m, depth[p] + 1); }, 0);
    });
    return { order: order, parents: parents, depth: depth, degree: degree };
  }

  /* 레인. order 는 열 순서의 글 목록이고 parents 는 그 글들 안의 첫 부모 후보다. 0 번 레인의
     본류는 anchor 에서 첫 부모를 거슬러 올라간 사슬이고, anchor 가 없으면 가장 깊은 글에서
     거슬러 올라간다. 본류는 anchor 뒤로도 레인을 이어 가는 자식을 따라 계속된다. */
  function lanes(order, parents, depth, degree, column, anchor) {
    var kids = {};
    order.forEach(function (id) { kids[id] = []; });
    // 가장 깊은 선수 글. 여럿이면 연결이 많은 글, 그래도 같으면 가까운 열.
    var firstParent = {};
    order.forEach(function (id) {
      var best = null;
      parents[id].forEach(function (p) {
        if (!best) { best = p; return; }
        var dp = depth[p] - depth[best], gp = (degree[p] || 0) - (degree[best] || 0);
        var cp = column[p] - column[best];
        if (dp > 0 || !dp && (gp > 0 || !gp && (cp > 0 || !cp && p < best))) best = p;
      });
      if (best) { firstParent[id] = best; kids[best].push(id); }
    });

    var tip = anchor || order.reduce(function (best, id) {
      if (!best) return id;
      var dd = depth[id] - depth[best];
      return dd > 0 || !dd && (degree[id] || 0) > (degree[best] || 0) ? id : best;
    }, null);
    var trunk = new Set();
    for (var step = tip; step; step = firstParent[step]) trunk.add(step);

    // 어느 자식이 부모의 레인을 이어 가는가: 본류 위의 자식, 없으면 뒤로 가장 길게 이어지는 자식.
    var reach = {};
    order.slice().reverse().forEach(function (id) {
      reach[id] = kids[id].reduce(function (m, c) { return Math.max(m, reach[c] + 1); }, 0);
    });
    var heir = {};
    order.forEach(function (id) {
      var best = null;
      kids[id].forEach(function (c) {
        if (best && trunk.has(best)) return;
        if (!best || trunk.has(c) || reach[c] > reach[best] ||
            reach[c] === reach[best] && (column[c] < column[best] || column[c] === column[best] && c < best)) best = c;
      });
      if (best) heir[id] = best;
    });
    var chains = [];
    order.forEach(function (id) {
      if (firstParent[id] && heir[firstParent[id]] === id) return;
      var members = [id];
      for (var x = id; heir[x]; x = heir[x]) members.push(heir[x]);
      chains.push({
        members: members, trunk: trunk.has(id),
        start: firstParent[id] ? column[firstParent[id]] : column[id],
        end: column[members[members.length - 1]]
      });
    });

    /* 레인 배정 (gitamine 의 '곧은 가지'). 한 사슬은 갈라져 나온 부모의 열부터 끝 열까지
       한 레인을 점유하고, 끝나면 그 레인을 다음 사슬이 다시 쓴다. 본류가 0 이고 나머지는
       왼쪽부터 훑으며 0 에 가장 가까운 빈 레인(+1, −1, +2, −2 …)을 받는다. */
    chains.sort(function (a, b) {
      return (b.trunk - a.trunk) || a.start - b.start || (b.end - b.start) - (a.end - a.start) ||
        (a.members[0] < b.members[0] ? -1 : 1);
    });
    var occupied = {}, lane = {}, minLane = 0, maxLane = 0;
    function laneFree(l, s, e) {
      return (occupied[l] || []).every(function (r) { return e < r[0] || s > r[1]; });
    }
    chains.forEach(function (chain) {
      var l = 0;
      if (!chain.trunk) {
        for (var k = 1; !l; k++) {
          if (laneFree(k, chain.start, chain.end)) l = k;
          else if (laneFree(-k, chain.start, chain.end)) l = -k;
        }
      }
      (occupied[l] = occupied[l] || []).push([chain.start, chain.end]);
      minLane = Math.min(minLane, l); maxLane = Math.max(maxLane, l);
      chain.members.forEach(function (id) { lane[id] = l; });
    });
    return { firstParent: firstParent, lane: lane, minLane: minLane, maxLane: maxLane };
  }

  /* x: 열 간격은 양옆 열의 글 수로 정한다 — 빽빽한 곳은 넓게, 성긴 곳은 좁게. 거기에
     열마다 고정된 작은 흔들림을 더하고, 같은 열 안의 글도 양옆 간격의 30% 안에서 엇갈리게
     둔다. 열이 격자로 줄 서 보이지 않게 하려는 것이고, 30% 라 열 순서는 뒤집히지 않는다.
     x0 은 첫 열의 x 다. */
  function spreadColumns(order, column, columns, x0) {
    var perColumn = [], gaps = [], columnX = [x0], c;
    for (c = 0; c < columns; c++) perColumn.push(0);
    order.forEach(function (id) { perColumn[column[id]] += 1; });
    for (c = 0; c < columns - 1; c++) {
      gaps.push(30 + 8.5 * Math.sqrt(perColumn[c] + perColumn[c + 1]) + (unitHash('gap' + c) - 0.5) * 14);
      columnX.push(columnX[c] + gaps[c]);
    }
    var x = {};
    order.forEach(function (id) {
      var col = column[id];
      var room = Math.min(col > 0 ? gaps[col - 1] : 40, col < columns - 1 ? gaps[col] : 40) * 0.3;
      x[id] = columnX[col] + (unitHash(id) * 2 - 1) * room;
    });
    return { columnX: columnX, x: x };
  }

  /* 선 모양. 첫 부모 선은 레인 위의 직선이고, 갈라지는 자리에서는 부모 바로 뒤에서 한 번
     휘어 자기 레인으로 들어간다. 그 밖의 선(오른쪽으로 가는 합류선, 왼쪽으로 가는 순환 안의
     required·weak 일부)은 레인 위를 달리지 않는다 — 그 레인의 점들을 꿰어 그 글들과도 이어진
     것처럼 보이기 때문이다. 출발 글에서 도착 글 쪽으로 반 레인 휘어 나와 레인 사이 빈 줄을
     따라 가다가 도착 직전에 휜다. 같은 레인의 글로 가는 합류선도 빈 줄로 나갔다가 돌아온다.
     휘는 구간은 낙차가 클수록 길게 잡아 꺾임이 세로로 서지 않게 한다. k 는 휘는 구간의 길이
     배율이고, 열 간격이 좁은 그림에서 줄여 쓴다. gap 은 레인 간격이다. */
  function linkPath(s, t, isFirstParent, k, gap) {
    if (!s || !t) return '';
    k = k || 1;
    var dx = t.x - s.x, dy = t.y - s.y;
    function bend(drop) { return Math.max(20 * k, Math.abs(drop) * 0.45 + 14 * k); }
    if (dx > -24 * k && dx < 24 * k) {
      // 같은 열 안의 선.
      return 'M' + s.x + ',' + s.y + ' C' + (s.x + 34 * k) + ',' + s.y + ' ' +
        (t.x - 34 * k) + ',' + t.y + ' ' + t.x + ',' + t.y;
    }
    if (isFirstParent && dx > 0) {
      if (!dy) return 'M' + s.x + ',' + s.y + ' L' + t.x + ',' + t.y;
      var run = Math.min(dx * 0.8, bend(dy));
      return 'M' + s.x + ',' + s.y + ' C' + (s.x + run / 2) + ',' + s.y + ' ' +
        (s.x + run / 2) + ',' + t.y + ' ' + (s.x + run) + ',' + t.y + ' L' + t.x + ',' + t.y;
    }
    var way = dx < 0 ? -1 : 1;
    var y = s.y + (dy < 0 ? -1 : 1) * (gap || 12 * k) / 2;
    var leave = bend(y - s.y), enter = bend(t.y - y), fit = Math.min(1, way * dx / (leave + enter));
    leave *= fit * way; enter *= fit * way;
    return 'M' + s.x + ',' + s.y + ' C' + (s.x + leave / 2) + ',' + s.y + ' ' +
      (s.x + leave / 2) + ',' + y + ' ' + (s.x + leave) + ',' + y + ' L' + (t.x - enter) + ',' + y +
      ' C' + (t.x - enter / 2) + ',' + y + ' ' + (t.x - enter / 2) + ',' + t.y + ' ' + t.x + ',' + t.y;
  }

  /* 라벨 자리. 'right'·'left' 는 점 옆에 가로로, 'above'·'below' 는 점 오른쪽 위나 아래로
     32° 비스듬히. 자리마다 글상자의 네 꼭짓점을 구해 두면 boxesOverlap 이 분리축으로 겹침을
     판정한다 — 가로 라벨과 비스듬한 라벨이 섞여도 된다. width 는 10.5px 로 잰 글자 폭이고,
     x·y 는 점에서 본 글자 시작점이다. */
  function labelBox(p, r, width, spot, size, bold) {
    var w = width * size / 10.5 * (bold ? 1.07 : 1) + 2;
    var x = spot === 'right' ? r + 5 : spot === 'left' ? -(r + 3) - w : 3;
    var y = spot === 'right' || spot === 'left' ? 4 : spot === 'above' ? -(r + 2) : r + 8;
    var angle = spot === 'above' ? -32 : spot === 'below' ? 32 : 0;
    var ascent = size * 0.8 + 1, descent = size * 0.25 + 1;
    var cos = Math.cos(angle * Math.PI / 180), sin = Math.sin(angle * Math.PI / 180);
    var box = { x: x, y: y, angle: angle, corners: [],
      minX: Infinity, maxX: -Infinity, minY: Infinity, maxY: -Infinity };
    [[-1, -ascent], [w, -ascent], [w, descent], [-1, descent]].forEach(function (c) {
      var q = { x: p.x + x + c[0] * cos - c[1] * sin, y: p.y + y + c[0] * sin + c[1] * cos };
      box.corners.push(q);
      box.minX = Math.min(box.minX, q.x); box.maxX = Math.max(box.maxX, q.x);
      box.minY = Math.min(box.minY, q.y); box.maxY = Math.max(box.maxY, q.y);
    });
    return box;
  }
  function boxesOverlap(a, b) {
    if (a.maxX < b.minX || b.maxX < a.minX || a.maxY < b.minY || b.maxY < a.minY) return false;
    var polys = [a.corners, b.corners];
    for (var p = 0; p < 2; p++) {
      for (var i = 0; i < 4; i++) {
        var p1 = polys[p][i], p2 = polys[p][(i + 1) % 4];
        var nx = p2.y - p1.y, ny = p1.x - p2.x;
        var range = polys.map(function (poly) {
          var lo = Infinity, hi = -Infinity;
          poly.forEach(function (q) {
            var d = q.x * nx + q.y * ny;
            if (d < lo) lo = d;
            if (d > hi) hi = d;
          });
          return [lo, hi];
        });
        if (range[0][1] < range[1][0] || range[1][1] < range[0][0]) return false;
      }
    }
    return true;
  }

  window.LinearLayout = {
    endpoints: endpoints, lid: lid, unitHash: unitHash,
    readingColumns: readingColumns, columnOrder: columnOrder, readingParents: readingParents,
    lanes: lanes, spreadColumns: spreadColumns,
    linkPath: linkPath, labelBox: labelBox, boxesOverlap: boxesOverlap
  };
})();
