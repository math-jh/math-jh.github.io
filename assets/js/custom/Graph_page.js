/* Graph_page.js — 전역 의존성 그래프 페이지(/ko/graph, /en/graph)와
 * 분류 기반 학습 그래프(/ko/dependencies, /en/dependencies).
 *
 * 핸드오프 graphcard.js 포팅: 항상-다크 Brass 카드(force-graph 래퍼 + 툴바 + 팝업) +
 * 왼쪽 인덱스 패널(검색 · family 필터 · MOST CONNECTED · 카테고리 아코디언). 인덱스와
 * 그래프는 외부 API(focus/select/setQuery/setFamilies/onHover/onClick)로 양방향 연동.
 * 데이터는 기존대로 graph-<lang>.json. 카드 내 검색/범례는 인덱스가 가지므로 제외.
 */
(function () {
  'use strict';

  function endpoints(l) {
    return [typeof l.source === 'object' ? l.source.id : l.source,
            typeof l.target === 'object' ? l.target.id : l.target];
  }
  function lid(l) { var e = endpoints(l); return e[0] + '>' + e[1]; }
  // SVG는 나중에 붙은 요소가 위에 그려진다. 의미가 약한 링크부터 칠하고,
  // 포커스된 링크는 relation과 무관하게 마지막 층으로 올린다.
  function linearLinkPaintOrder(link, highlighted) {
    var relationOrder = link.relation === 'weak' ? 0 : link.relation === 'forward' ? 1 : 2;
    return (highlighted ? 3 : 0) + relationOrder;
  }
  function prettify(slug) {
    return slug.split('_').map(function (w) { return w ? w[0].toUpperCase() + w.slice(1) : w; }).join(' ');
  }
  // 모든 노드를 (0,0)으로 당기는 선형 중심 중력 d3 force.
  function radial(strength) {
    var nodes;
    function force(alpha) {
      if (!nodes) return;
      for (var i = 0; i < nodes.length; i++) {
        var n = nodes[i];
        n.vx += -(n.x || 0) * strength * alpha;
        n.vy += -(n.y || 0) * strength * alpha;
      }
    }
    force.initialize = function (_) { nodes = _; };
    return force;
  }

  // required SCC를 한 층으로 축약한 뒤 forward를 순환 없는 소프트 제약으로
  // 더한다. 가로 층은 오직 의존 그래프의 위상 깊이로 정하고, 카테고리 안에서만
  // 의미가 있는 weight는 같은 층의 노드를 안정적으로 정렬할 때만 쓴다.
  function linearPositions(data, viewportWidth, viewportHeight) {
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
    data.links.filter(function (l) { return l.relation === 'forward'; })
      .sort(function (a, b) { return lid(a).localeCompare(lid(b)); })
      .forEach(function (l) {
        var e = endpoints(l), a = compOf[e[0]], b = compOf[e[1]];
        if (a !== b && !reaches(b, a)) addEdge(a, b);
      });

    var indeg = comps.map(function () { return 0; });
    adj.forEach(function (nexts) { nexts.forEach(function (v) { indeg[v] += 1; }); });
    var rank = comps.map(function () { return 0; });
    var queue = comps.map(function (_, i) { return i; }).filter(function (i) { return indeg[i] === 0; });
    queue.sort(function (a, b) { return a - b; });
    while (queue.length) {
      var current = queue.shift();
      adj[current].forEach(function (next) {
        rank[next] = Math.max(rank[next], rank[current] + 1);
        indeg[next] -= 1;
        if (indeg[next] === 0) { queue.push(next); queue.sort(function (a, b) { return rank[a] - rank[b]; }); }
      });
    }

    var used = Array.from(new Set(rank)).sort(function (a, b) { return a - b; });
    var compressed = {}; used.forEach(function (value, i) { compressed[value] = i; });
    var layers = {};
    nodes.forEach(function (n) {
      var r = compressed[rank[compOf[n.id]]];
      (layers[r] = layers[r] || []).push(n);
    });
    var positions = {};
    // rowGap 은 행 사이에 가로 레인이 지날 골을 남겨야 한다 — 점 반지름 최대 7px 을
    // 양쪽에서 빼고 레인 2층(±3.5px)이 들어갈 폭이 나오는 값이다.
    var columnGap = 66, rowGap = 28, padX = 56, padY = 52;
    var capacity = Math.max(1, Math.floor((viewportHeight - 2 * padY) / rowGap) + 1);
    var visualColumn = 0;
    Object.keys(layers).sort(function (a, b) { return Number(a) - Number(b); }).forEach(function (rawRank) {
      var layer = layers[rawRank];
      layer.sort(function (a, b) {
        return (a.category || '').localeCompare(b.category || '') ||
          (Number(a.weight) || 0) - (Number(b.weight) || 0) || a.title.localeCompare(b.title);
      });
      for (var start = 0; start < layer.length; start += capacity) {
        var chunk = layer.slice(start, start + capacity);
        // 열마다 제 개수로 중심을 잡으면 홀짝에 따라 행이 rowGap/2 만큼 어긋나
        // 두 벌의 격자가 생긴다. 그러면 행 사이 골이 남의 행 위로 떨어져 레인이
        // 노드를 관통한다 — 중심 오프셋을 정수 칸으로 반올림해 격자를 하나로 둔다.
        var center = Math.round((chunk.length - 1) / 2);
        chunk.forEach(function (n, i) {
          positions[n.id] = { column: visualColumn, y: (i - center) * rowGap };
        });
        visualColumn += 1;
      }
    });
    var width = Math.max(viewportWidth, padX * 2 + Math.max(0, visualColumn - 1) * columnGap);
    Object.keys(positions).forEach(function (id) {
      positions[id].x = padX + positions[id].column * columnGap;
      positions[id].y += viewportHeight / 2;
      delete positions[id].column;
    });
    return { positions: positions, width: width, height: viewportHeight, rowGap: rowGap };
  }

  /* 필터 칩(family) 정의는 그래프 JSON 이 실어 온다 (_data/categories.yml 의
     families → _plugins/graph_data.rb). 예전엔 여기 상수로 한 벌 더 있었고, JSON 에만
     있는 family 는 칩이 없어 노드가 회색(misc)으로 떨어졌다. 아래는 옛 JSON 을 위한
     폴백일 뿐이다. */
  var FAMILIES_FALLBACK = [
    { key: 'foundations', label: 'Foundations', label_ko: '기초', hue: 258 },
    { key: 'algebra', label: 'Algebra', label_ko: '대수', hue: 220 },
    { key: 'analysis', label: 'Analysis', label_ko: '해석', hue: 188 },
    { key: 'geometry', label: 'Geometry', label_ko: '기하', hue: 24 }
  ];


  var ICON = {
    search: '<svg viewBox="0 0 16 16" width="13" height="13" aria-hidden="true"><circle cx="7" cy="7" r="4.2" fill="none" stroke="currentColor" stroke-width="1.4"/><line x1="10.2" y1="10.2" x2="14" y2="14" stroke="currentColor" stroke-width="1.4" stroke-linecap="round"/></svg>',
    caret: '<svg class="gi-caret" viewBox="0 0 16 16" width="9" height="9" aria-hidden="true"><path d="M5 3l6 5-6 5" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/></svg>',
    tree: '<svg viewBox="0 0 16 16" width="15" height="15" aria-hidden="true"><path d="M3 3v10M3 5h4c2.2 0 2.2-2 4.5-2H13M3 11h4c2.2 0 2.2 2 4.5 2H13" fill="none" stroke="currentColor" stroke-width="1.4" stroke-linecap="round"/><circle cx="3" cy="3" r="1.4" fill="currentColor"/><circle cx="13" cy="3" r="1.4" fill="currentColor"/><circle cx="13" cy="13" r="1.4" fill="currentColor"/></svg>',
    force: '<svg viewBox="0 0 16 16" width="15" height="15" aria-hidden="true"><path d="M3.2 4.1l4.4 3.3 5.1-3M7.6 7.4l-2 5M7.6 7.4l5.2 4.3" fill="none" stroke="currentColor" stroke-width="1.2"/><circle cx="3" cy="4" r="1.7" fill="currentColor"/><circle cx="12.8" cy="3.9" r="1.7" fill="currentColor"/><circle cx="7.6" cy="7.5" r="1.7" fill="currentColor"/><circle cx="5.5" cy="12.7" r="1.7" fill="currentColor"/><circle cx="12.9" cy="11.8" r="1.7" fill="currentColor"/></svg>',
    fit: '<svg viewBox="0 0 16 16" width="15" height="15"><path d="M2 5.5V2.5h3M14 5.5V2.5h-3M2 10.5v3h3M14 10.5v3h-3" fill="none" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"/></svg>',
    reset: '<svg viewBox="0 0 16 16" width="15" height="15"><path d="M13 8a5 5 0 1 1-1.6-3.7M13 2.2V5h-2.8" fill="none" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"/></svg>'
  };

  /* ---------- card engine (graphcard.js 포팅) ---------- */
  function createGraphCard(stage, data, families, cfg) {
    var famKeys = new Set(families.map(function (f) { return f.key; }));
    var deg = {}, outAdj = {}, inAdj = {}, byId = {};
    var requiredIn = {}, weakIn = {}, forwardOut = {};
    data.nodes.forEach(function (n) {
      byId[n.id] = n;
      n.__c = n.family === 'misc'
        ? 'hsl(' + n.hue + ',0%,58%)'
        : 'hsl(' + n.hue + ',' + cfg.nodeSat + '%,' + cfg.nodeLight + '%)';
    });
    data.links.forEach(function (l) {
      var e = endpoints(l);
      deg[e[0]] = (deg[e[0]] || 0) + 1;
      deg[e[1]] = (deg[e[1]] || 0) + 1;
      (outAdj[e[0]] = outAdj[e[0]] || new Set()).add(e[1]);
      (inAdj[e[1]] = inAdj[e[1]] || new Set()).add(e[0]);
      if (l.relation === 'required') (requiredIn[e[1]] = requiredIn[e[1]] || []).push(l);
      else if (l.relation === 'weak') (weakIn[e[1]] = weakIn[e[1]] || []).push(l);
      else if (l.relation === 'forward') (forwardOut[e[0]] = forwardOut[e[0]] || []).push(l);
    });

    var hovered = null, selected = null, query = '', layoutMode = 'force';
    var activeFams = new Set(families.map(function (f) { return f.key; }));
    var hlNodes = new Set(), hlLinks = new Set();
    var hoverCb = null, clickCb = null, linearGeometry = null, linearLanes = {};
    var linearNodeEls = [], linearLinkEls = [];

    function radius(n) {
      var value = Math.sqrt(2.0 + (deg[n.id] || 0) * 0.7) * 2.95;
      return layoutMode === 'linear' ? Math.max(5.5, value) : value;
    }
    var labelTop = Math.max(6, Math.round(data.nodes.length * 0.04));
    var hubCandidates = data.classified
      ? data.nodes.filter(function (n) { return (deg[n.id] || 0) > 0; })
      : data.nodes.slice();
    var hubSet = new Set(hubCandidates
      .sort(function (a, b) { return (deg[b.id] || 0) - (deg[a.id] || 0); })
      .slice(0, labelTop).map(function (n) { return n.id; }));

    function passesFilter(n) {
      var mc = !famKeys.has(n.family) || activeFams.has(n.family);
      var ms = !query || n.title.toLowerCase().indexOf(query) >= 0;
      return mc && ms;
    }
    function activeFocus() {
      return layoutMode === 'linear' ? (selected || hovered) : (hovered || selected);
    }
    function nodeState(n) {
      if (!passesFilter(n)) return 'off';
      if (hlNodes.size && !hlNodes.has(n.id)) return 'off';
      if (layoutMode === 'linear' && !hlNodes.size) return 'idle';
      return 'on';
    }
    function addHighlightedLink(link) {
      var e = endpoints(link);
      hlNodes.add(e[0]); hlNodes.add(e[1]); hlLinks.add(lid(link));
    }
    function focusForce(node) {
      hlNodes = new Set(); hlLinks = new Set();
      if (!node) return;
      hlNodes.add(node.id);
      (outAdj[node.id] || new Set()).forEach(function (x) { hlNodes.add(x); });
      (inAdj[node.id] || new Set()).forEach(function (x) { hlNodes.add(x); });
      data.links.forEach(function (l) {
        var e = endpoints(l);
        if (e[0] === node.id || e[1] === node.id) hlLinks.add(lid(l));
      });
    }
    /* 이 노드를 고르면 함께 켜지는 엣지들. 레인 배정기도 같은 집합을 쓴다 —
       한 번에 같이 보이는 선끼리만 높이를 다투면 된다. */
    function linearFocusLinks(id) {
      var out = [];
      // Only the chosen article may branch to optional context. Weak edges point
      // cited -> citing, while forward edges point citing -> later reading.
      (weakIn[id] || []).forEach(function (l) { out.push(l); });
      (forwardOut[id] || []).forEach(function (l) { out.push(l); });

      // Required edges point prerequisite -> dependent. Walk only upstream and
      // never expand weak/forward edges from prerequisites reached on this walk.
      var todo = [id], seen = new Set();
      while (todo.length) {
        var here = todo.pop();
        if (seen.has(here)) continue;
        seen.add(here);
        (requiredIn[here] || []).forEach(function (link) {
          var source = endpoints(link)[0];
          out.push(link);
          if (!seen.has(source)) todo.push(source);
        });
      }
      return out;
    }
    function focusLinear(node) {
      hlNodes = new Set(); hlLinks = new Set();
      if (!node) return;
      hlNodes.add(node.id);
      linearFocusLinks(node.id).forEach(addHighlightedLink);
    }
    function refocus() {
      var node = activeFocus();
      if (layoutMode === 'linear') focusLinear(node);
      else focusForce(node);
      updateLinearStyles();
    }

    // DOM: native horizontal viewport + canvas surface + fixed toolbar/card.
    stage.innerHTML = '';
    var canvasViewport = document.createElement('div');
    canvasViewport.className = 'gc-viewport';
    var canvasWrap = document.createElement('div');
    canvasWrap.className = 'gc-canvas';
    canvasViewport.appendChild(canvasWrap);
    var linearSvg = document.createElementNS('http://www.w3.org/2000/svg', 'svg');
    linearSvg.setAttribute('class', 'gc-linear');
    linearSvg.setAttribute('role', 'img');
    linearSvg.setAttribute('aria-label', cfg.linearLabel);
    canvasViewport.appendChild(linearSvg);
    stage.appendChild(canvasViewport);

    var top = document.createElement('div');
    top.className = 'gc-top';
    top.innerHTML = (cfg.layoutToggle
      ? '<button class="gc-btn" data-act="layout" aria-pressed="false" title="' + cfg.linearLabel + '">' + ICON.tree + '</button>'
      : '') +
      '<button class="gc-btn" data-act="fit" title="Zoom to fit">' + ICON.fit + '</button>' +
      '<button class="gc-btn" data-act="reset" title="Reset view">' + ICON.reset + '</button>';
    stage.appendChild(top);

    var pop = document.createElement('div');
    pop.className = 'gc-pop';
    pop.innerHTML = '<button class="gc-pop-close" type="button" aria-label="Close">&times;</button>' +
      '<div class="gc-pop-title"></div><a class="gc-pop-go" href="#"></a>';
    stage.appendChild(pop);
    var popTitle = pop.querySelector('.gc-pop-title');
    var popGo = pop.querySelector('.gc-pop-go');
    var popClose = pop.querySelector('.gc-pop-close');
    [top, pop].forEach(function (overlay) {
      ['pointerdown', 'pointerup', 'click', 'dblclick'].forEach(function (type) {
        overlay.addEventListener(type, function (event) { event.stopPropagation(); });
      });
    });
    popGo.textContent = cfg.openLabel;
    popGo.addEventListener('click', function (e) { e.stopPropagation(); });

    function showPop(n) {
      popTitle.textContent = n.title;
      popGo.setAttribute('href', n.url || '#');
      pop.classList.add('show');
    }
    function hidePop() { pop.classList.remove('show'); }
    function notifySelection() { if (clickCb) clickCb(selected ? selected.id : null); }
    function clearSelection() {
      selected = null; hidePop(); refocus(); notifySelection();
    }
    function selectNode(node) {
      if (node && selected && selected.id === node.id) clearSelection();
      else {
        selected = node; refocus();
        if (node) { showPop(node); centerActive(); } else hidePop();
        notifySelection();
      }
    }
    popClose.addEventListener('click', function (e) { e.stopPropagation(); clearSelection(); });
    linearSvg.addEventListener('click', clearSelection);

    function svgElement(name, attrs) {
      var el = document.createElementNS('http://www.w3.org/2000/svg', name);
      Object.keys(attrs || {}).forEach(function (key) { el.setAttribute(key, attrs[key]); });
      return el;
    }
    /* 가로 레인의 높이 배정.
       기본은 출발 노드의 행 위(오프셋 0)에 그대로 눕히는 것이다. 비키는 경우는 둘뿐:
       레인이 남의 점을 관통할 때, 그리고 **한 번에 같이 켜지는 다른 레인**과 겹칠 때.
       서로 다른 선택에서만 보이는 레인끼리는 겹쳐도 화면에 함께 뜨지 않으니 내버려 둔다.
       비켜야 하면 행 사이 골(행에서 rowGap/2, 한 골에 2층)로 내려간다. */
    function assignLanes() {
      linearLanes = {};
      if (!linearGeometry) return;
      var gap = linearGeometry.rowGap || 28, SUB = 3.5, CLEAR = 5;
      var minY = 18, maxY = linearGeometry.height - 24;
      // 너무 멀리 밀어내면 짧은 엣지가 화면 반대편까지 내려간다 — 골 4칸까지만 본다.
      var bands = Math.min(4, Math.ceil(linearGeometry.height / gap) + 1);
      function slots(prefer) {
        var out = [0];
        for (var band = 0; band < bands; band++) {
          var mid = gap / 2 + band * gap;
          [-SUB, SUB].forEach(function (sub) {
            [prefer, -prefer].forEach(function (side) { out.push(side * (mid + sub)); });
          });
        }
        return out;
      }

      // 어떤 선택에서 켜지는지 — 링크별·노드별로. 레인과 상대(다른 레인이든 점이든)가
      // 이 집합을 공유할 때만 자리를 다툰다. 함께 뜨지 않으면 겹쳐도 보이지 않는다.
      var linkFocus = {}, nodeFocus = {};
      function mark(store, key, id) { (store[key] = store[key] || new Set()).add(id); }
      data.nodes.forEach(function (n) {
        mark(nodeFocus, n.id, n.id);
        linearFocusLinks(n.id).forEach(function (l) {
          var ends = endpoints(l);
          mark(linkFocus, lid(l), n.id);
          mark(nodeFocus, ends[0], n.id);
          mark(nodeFocus, ends[1], n.id);
        });
      });
      function shares(a, b) {
        if (!a || !b) return false;
        var small = a, large = b;
        if (small.size > large.size) { small = b; large = a; }
        var shared = false;
        small.forEach(function (id) { if (large.has(id)) shared = true; });
        return shared;
      }

      // 행별 노드 목록 — 레인이 같이 켜지는 점을 지나는지 보는 데 쓴다.
      var rows = {};
      data.nodes.forEach(function (n) {
        var p = linearGeometry.positions[n.id];
        if (p) (rows[p.y] = rows[p.y] || []).push({ id: n.id, x: p.x, r: radius(n) });
      });
      var rowKeys = Object.keys(rows).map(Number);
      function crossesNode(key, y, x0, x1) {
        return rowKeys.some(function (ry) {
          if (Math.abs(ry - y) > 12) return false;
          return rows[ry].some(function (n) {
            return n.x > x0 + 1 && n.x < x1 - 1 && Math.abs(ry - y) < n.r + 2.5 &&
              shares(linkFocus[key], nodeFocus[n.id]);
          });
        });
      }

      var placed = [];
      var pending = [];
      data.links.forEach(function (link) {
        var e = endpoints(link);
        var s = linearGeometry.positions[e[0]], t = linearGeometry.positions[e[1]];
        if (!s || !t || Math.abs(t.x - s.x) < 16) return;   // 수직 가지는 laneX 를 쓴다
        pending.push({ key: lid(link), relation: link.relation, base: s.y,
                       x0: Math.min(s.x, t.x), x1: Math.max(s.x, t.x) });
      });
      // 왼쪽부터 훑어 나가며 칠한다 (구간 그래프 greedy 의 표준 순서).
      pending.sort(function (a, b) { return a.x0 - b.x0 || a.x1 - b.x1; });
      pending.forEach(function (lane) {
        var options = slots(lane.relation === 'weak' ? -1 : 1);
        var chosen = null, best = null, bestCost = Infinity;
        for (var i = 0; i < options.length; i++) {
          var y = lane.base + options[i];
          if (y < minY || y > maxY) continue;
          if (crossesNode(lane.key, y, lane.x0, lane.x1)) continue;
          // 빈 층이 하나도 없을 때를 대비해 겹치는 길이의 합을 재 둔다.
          var cost = 0;
          placed.forEach(function (other) {
            if (Math.abs(other.y - y) >= CLEAR) return;
            var overlap = Math.min(other.x1, lane.x1) - Math.max(other.x0, lane.x0);
            if (overlap > 4 && shares(linkFocus[other.key], linkFocus[lane.key])) cost += overlap;
          });
          if (cost === 0) { chosen = y; break; }
          if (cost < bestCost) { bestCost = cost; best = y; }
        }
        if (chosen === null) chosen = best === null ? lane.base : best;
        placed.push({ key: lane.key, y: chosen, x0: lane.x0, x1: lane.x1 });
        linearLanes[lane.key] = chosen;
      });
    }
    function gitPath(link, index) {
      var e = endpoints(link);
      var source = linearGeometry.positions[e[0]], target = linearGeometry.positions[e[1]];
      if (!source || !target) return '';
      var sx = source.x, sy = source.y, tx = target.x, ty = target.y;
      var dx = tx - sx;

      /* 노드 → 사선 직선 → (고정 반지름 모서리) → 레인 직선 → (모서리) → 사선 직선 → 노드.
         모서리만 2차 베지에로 둥글리므로 낙차는 곡선이 아니라 사선이 흡수한다. */
      function routedPath(start, end, laneStart, laneEnd, mainDirection) {
        function unit(from, to) {
          var ux = to.x - from.x, uy = to.y - from.y;
          var length = Math.sqrt(ux * ux + uy * uy) || 1;
          return { x: ux / length, y: uy / length };
        }
        function span(from, to) {
          return Math.sqrt(Math.pow(to.x - from.x, 2) + Math.pow(to.y - from.y, 2));
        }
        var cornerRadius = 12;
        var sourceDirection = unit(start, laneStart);
        var targetDirection = unit(laneEnd, end);
        var sourceRadius = radius(byId[e[0]]);
        var targetRadius = radius(byId[e[1]]) + 3;
        var sourceEdge = {
          x: start.x + sourceDirection.x * sourceRadius,
          y: start.y + sourceDirection.y * sourceRadius
        };
        var targetEdge = {
          x: end.x - targetDirection.x * targetRadius,
          y: end.y - targetDirection.y * targetRadius
        };
        // 짧은 변에서는 반지름이 그 변의 절반을 넘지 않게 줄인다 — 넘으면 두 모서리가 겹친다.
        var laneHalf = span(laneStart, laneEnd) / 2;
        var sourceCorner = Math.min(cornerRadius, span(sourceEdge, laneStart) / 2, laneHalf);
        var targetCorner = Math.min(cornerRadius, span(laneEnd, targetEdge) / 2, laneHalf);
        return 'M' + sourceEdge.x + ',' + sourceEdge.y +
          ' L' + (laneStart.x - sourceDirection.x * sourceCorner) + ',' + (laneStart.y - sourceDirection.y * sourceCorner) +
          ' Q' + laneStart.x + ',' + laneStart.y +
          ' ' + (laneStart.x + mainDirection.x * sourceCorner) + ',' + (laneStart.y + mainDirection.y * sourceCorner) +
          ' L' + (laneEnd.x - mainDirection.x * targetCorner) + ',' + (laneEnd.y - mainDirection.y * targetCorner) +
          ' Q' + laneEnd.x + ',' + laneEnd.y +
          ' ' + (laneEnd.x + targetDirection.x * targetCorner) + ',' + (laneEnd.y + targetDirection.y * targetCorner) +
          ' L' + targetEdge.x + ',' + targetEdge.y;
      }

      if (Math.abs(dx) < 16) {
        var side = sx < linearGeometry.width / 2 ? 1 : -1;
        var laneX = sx + side * (20 + (index % 3) * 7);
        laneX = Math.max(16, Math.min(linearGeometry.width - 16, laneX));
        var verticalDirection = ty >= sy ? 1 : -1;
        var verticalCurve = Math.min(24, Math.max(8, Math.abs(ty - sy) * 0.28));
        return routedPath(
          { x: sx, y: sy }, { x: tx, y: ty },
          { x: laneX, y: sy + verticalDirection * verticalCurve },
          { x: laneX, y: ty - verticalDirection * verticalCurve },
          { x: 0, y: verticalDirection }
        );
      }
      var direction = dx > 0 ? 1 : -1;
      var laneY = linearLanes[lid(link)];
      if (laneY === undefined) laneY = sy;
      laneY = Math.max(18, Math.min(linearGeometry.height - 24, laneY));

      // 사선 구간의 가로 길이. 낙차가 클수록 벌려 기울기를 SLOPE_LIMIT 아래로 누른다.
      var MIN_RUN = 22, MAX_RUN = 120, SLOPE_LIMIT = 1.3, MIN_LANE = 26;
      function runFor(drop) {
        return Math.max(MIN_RUN, Math.min(MAX_RUN, drop / SLOPE_LIMIT));
      }
      var sourceRun = runFor(Math.abs(laneY - sy));
      var targetRun = runFor(Math.abs(ty - laneY));
      // 두 사선이 가로 간격을 다 먹으면 레인이 사라진다 — 남는 폭 안으로 비례 축소.
      var budget = Math.max(0, Math.abs(dx) - MIN_LANE);
      if (sourceRun + targetRun > budget) {
        var scale = budget / (sourceRun + targetRun);
        sourceRun *= scale; targetRun *= scale;
      }
      return routedPath(
        { x: sx, y: sy }, { x: tx, y: ty },
        { x: sx + direction * sourceRun, y: laneY },
        { x: tx - direction * targetRun, y: laneY },
        { x: direction, y: 0 }
      );
    }
    function updateLinearStyles() {
      if (!linearGeometry) return;
      linearLinkEls.forEach(function (entry) {
        var link = entry.link;
        var color = linkColor(link);
        entry.path.setAttribute('stroke', color);
        entry.arrow.setAttribute('fill', arrowColor(link));
        entry.path.setAttribute('stroke-width', hlLinks.has(lid(link)) ? '2.4' :
          (link.relation === 'required' ? '1.2' : link.relation === 'weak' ? '0.85' : '1'));
      });
      // 링크마다 선과 화살촉을 한 묶음으로 두고, 약한 관계부터 DOM 앞쪽에
      // 재배치한다. 하이라이트가 바뀔 때도 선택된 링크 전체가 맨 위로 올라간다.
      linearLinkEls.slice().sort(function (a, b) {
        return linearLinkPaintOrder(a.link, hlLinks.has(lid(a.link))) -
            linearLinkPaintOrder(b.link, hlLinks.has(lid(b.link))) || a.order - b.order;
      }).forEach(function (entry) { entry.group.parentNode.appendChild(entry.group); });
      linearNodeEls.forEach(function (entry) {
        var node = entry.node;
        var state = nodeState(node);
        var isSelected = selected && selected.id === node.id;
        var focused = hlNodes.size > 0 && hlNodes.has(node.id);
        var matched = query && node.title.toLowerCase().indexOf(query) >= 0;
        entry.dot.setAttribute('r', radius(node));
        entry.dot.setAttribute('fill', isSelected ? 'rgb(' + cfg.accent + ')' : node.__c);
        entry.dot.setAttribute('fill-opacity', state === 'off' ? '0.09' : state === 'idle' ? '0.3' : '1');
        entry.dot.setAttribute('stroke', isSelected ? 'rgba(' + cfg.accent + ',0.62)' : 'none');
        entry.dot.setAttribute('stroke-width', isSelected ? '2' : '0');
        entry.label.style.display = state !== 'off' && (focused || matched || hubSet.has(node.id)) ? '' : 'none';
        entry.label.setAttribute('fill', focused || matched
          ? 'rgba(' + cfg.labelHi + ',0.98)'
          : 'rgba(' + cfg.label + ',' + (state === 'idle' ? '0.46' : '0.72') + ')');
        entry.label.setAttribute('font-weight', focused || matched ? '600' : '400');
      });
    }
    function renderLinear() {
      linearSvg.innerHTML = '';
      linearNodeEls = []; linearLinkEls = [];
      linearSvg.setAttribute('width', Math.ceil(linearGeometry.width));
      linearSvg.setAttribute('height', Math.ceil(linearGeometry.height));
      linearSvg.setAttribute('viewBox', '0 0 ' + linearGeometry.width + ' ' + linearGeometry.height);
      linearSvg.style.width = Math.ceil(linearGeometry.width) + 'px';
      linearSvg.style.height = Math.ceil(linearGeometry.height) + 'px';

      var linksGroup = svgElement('g', { class: 'gc-linear__links' });
      var pendingLinks = [];
      data.links.forEach(function (link, index) {
        var group = svgElement('g', { class: 'gc-linear__link' });
        var path = svgElement('path', {
          d: gitPath(link, index), fill: 'none', 'stroke-linecap': 'round',
          'stroke-linejoin': 'round', 'vector-effect': 'non-scaling-stroke'
        });
        if (link.relation === 'weak') path.setAttribute('stroke-dasharray', '2 5');
        else if (link.relation === 'forward') path.setAttribute('stroke-dasharray', '9 5');
        group.appendChild(path); linksGroup.appendChild(group);
        pendingLinks.push({ link: link, path: path, group: group, order: index });
      });
      linearSvg.appendChild(linksGroup);
      pendingLinks.forEach(function (entry) {
        var length = entry.path.getTotalLength();
        var middle = length / 2;
        var point = entry.path.getPointAtLength(middle);
        var before = entry.path.getPointAtLength(Math.max(0, middle - 0.75));
        var after = entry.path.getPointAtLength(Math.min(length, middle + 0.75));
        var angle = Math.atan2(after.y - before.y, after.x - before.x) * 180 / Math.PI;
        var arrow = svgElement('path', {
          d: 'M-4,-3 L4,0 L-4,3 Z',
          transform: 'translate(' + point.x + ' ' + point.y + ') rotate(' + angle + ')',
          'aria-hidden': 'true', 'pointer-events': 'none'
        });
        entry.group.appendChild(arrow);
        linearLinkEls.push({
          link: entry.link, path: entry.path, arrow: arrow,
          group: entry.group, order: entry.order
        });
      });

      var nodesGroup = svgElement('g', { class: 'gc-linear__nodes' });
      data.nodes.forEach(function (node) {
        var p = linearGeometry.positions[node.id];
        var group = svgElement('g', {
          class: 'gc-linear__node', transform: 'translate(' + p.x + ' ' + p.y + ')',
          tabindex: '0', role: 'button', 'aria-label': node.title
        });
        var hit = svgElement('circle', { r: '11', fill: 'transparent' });
        var dot = svgElement('circle', { r: radius(node) });
        var label = svgElement('text', { x: '0', y: radius(node) + 13, 'text-anchor': 'middle' });
        label.textContent = node.title;
        var title = svgElement('title'); title.textContent = node.title; group.appendChild(title);
        group.appendChild(hit); group.appendChild(dot); group.appendChild(label);
        group.addEventListener('mouseenter', function () {
          hovered = node; refocus(); if (hoverCb) hoverCb(node.id);
        });
        group.addEventListener('mouseleave', function () {
          if (hovered && hovered.id === node.id) hovered = null;
          refocus(); if (hoverCb) hoverCb(null);
        });
        group.addEventListener('click', function (event) { event.stopPropagation(); selectNode(node); });
        group.addEventListener('keydown', function (event) {
          if (event.key === 'Enter' || event.key === ' ') {
            event.preventDefault(); event.stopPropagation(); selectNode(node);
          }
        });
        nodesGroup.appendChild(group);
        linearNodeEls.push({ node: node, dot: dot, label: label });
      });
      linearSvg.appendChild(nodesGroup);
      updateLinearStyles();
    }

    function hslaFade(hue, a) { return 'hsla(' + hue + ',38%,55%,' + a + ')'; }
    function draw(node, ctx, scale) {
      var st = nodeState(node);
      var r = radius(node);
      var sel = selected && selected.id === node.id;
      ctx.save();
      if (st === 'off' || st === 'idle') {
        ctx.fillStyle = hslaFade(node.hue, st === 'idle' ? 0.3 : 0.09);
        ctx.beginPath(); ctx.arc(node.x, node.y, r, 0, 6.2832); ctx.fill();
      } else {
        if (cfg.glow) { ctx.shadowColor = node.__c; ctx.shadowBlur = cfg.glow; }
        ctx.fillStyle = sel ? 'rgb(' + cfg.accent + ')' : node.__c;
        ctx.beginPath(); ctx.arc(node.x, node.y, r, 0, 6.2832); ctx.fill();
        ctx.shadowBlur = 0;
        if (sel) {
          ctx.lineWidth = 2 / scale;
          ctx.strokeStyle = 'rgba(' + cfg.accent + ',0.55)';
          ctx.beginPath(); ctx.arc(node.x, node.y, r + 3 / scale, 0, 6.2832); ctx.stroke();
        }
      }
      ctx.restore();

      var focused = hlNodes.size > 0 && hlNodes.has(node.id);
      var matched = query && node.title.toLowerCase().indexOf(query) >= 0;
      if (st !== 'off' && (focused || matched || hubSet.has(node.id))) {
        var emph = focused || matched;
        var fs = Math.max(3.5, (emph ? 11.5 : 10) / scale);
        ctx.font = (emph ? '600 ' : '') + fs + 'px ' + cfg.font;
        ctx.textAlign = 'center'; ctx.textBaseline = 'top';
        ctx.fillStyle = emph
          ? 'rgba(' + cfg.labelHi + ',0.98)'
          : 'rgba(' + cfg.label + ',' + (st === 'idle' ? 0.46 : 0.72) + ')';
        ctx.fillText(node.title, node.x, node.y + r + 2.5 / scale);
      }
    }
    function pointerArea(node, color, ctx) {
      ctx.fillStyle = color;
      ctx.beginPath(); ctx.arc(node.x, node.y, Math.max(11, radius(node)), 0, 6.2832); ctx.fill();
    }
    function linkColor(l) {
      if (hlLinks.has(lid(l))) {
        var highlightedEnds = endpoints(l);
        var focused = activeFocus();
        if (layoutMode === 'linear') {
          if (focused && l.relation === 'forward' && highlightedEnds[0] === focused.id) {
            return 'rgba(' + cfg.accentOut + ',0.9)';
          }
          return 'rgba(' + cfg.accent + ',0.85)';
        }
        if (focused) {
          if (highlightedEnds[0] === focused.id) return 'rgba(' + cfg.accentOut + ',0.9)';
          if (highlightedEnds[1] === focused.id) return 'rgba(' + cfg.accentIn + ',0.9)';
        }
        return 'rgba(' + cfg.accent + ',0.85)';
      }
      var e = endpoints(l);
      var on = passesFilter(byId[e[0]]) && passesFilter(byId[e[1]]) && !activeFocus();
      if (!on) return 'rgba(' + cfg.link + ',0.035)';
      if (layoutMode === 'linear') {
        if (l.relation === 'weak') return 'rgba(' + cfg.link + ',0.1)';
        if (l.relation === 'forward') return 'rgba(' + cfg.link + ',0.14)';
        return 'rgba(' + cfg.link + ',0.2)';
      }
      if (l.relation === 'weak') return 'rgba(' + cfg.link + ',0.2)';
      if (l.relation === 'forward') return 'rgba(' + cfg.link + ',0.3)';
      if (l.relation === 'required') return 'rgba(' + cfg.link + ',0.44)';
      return 'rgba(' + cfg.link + ',0.36)';
    }
    // Dependencies의 화살촉은 반투명 면으로 그리면 뒤의 링크가 비쳐 보인다.
    // 카드의 주 배경색 위에서 보이던 색을 미리 합성해 불투명 RGB로 만들고,
    // weak는 면적 때문에 점선보다 도드라지지 않도록 배경 쪽으로 더 누른다.
    function arrowColor(l) {
      var color = linkColor(l);
      if (!data.classified) return color;
      var rgba = color.match(/^rgba?\(\s*([\d.]+)\s*,\s*([\d.]+)\s*,\s*([\d.]+)(?:\s*,\s*([\d.]+))?\s*\)$/);
      if (!rgba) return color;
      var background = [20, 21, 25];
      var alpha = rgba[4] === undefined ? 1 : Number(rgba[4]);
      if (l.relation === 'weak') alpha *= 0.55;
      alpha = Math.max(0, Math.min(1, alpha));
      return 'rgb(' + [1, 2, 3].map(function (index) {
        return Math.round(background[index - 1] * (1 - alpha) + Number(rgba[index]) * alpha);
      }).join(',') + ')';
    }
    function linkDash(l) {
      if (l.relation === 'weak') return [2, 5];
      if (l.relation === 'forward') return [9, 5];
      return [];
    }
    function linkCurve(l) {
      var e = endpoints(l);
      return data.links.some(function (r) {
        var re = endpoints(r);
        return re[0] === e[1] && re[1] === e[0];
      }) ? 0.25 : 0;
    }

    var graph = ForceGraph()(canvasWrap)
      .backgroundColor('rgba(0,0,0,0)')
      .autoPauseRedraw(false)
      .nodeId('id')
      .nodeRelSize(5)
      .nodeVal(function (n) { return Math.pow(radius(n) / 5, 2); })
      .nodeColor(function () { return 'rgba(0,0,0,0)'; })
      .nodeCanvasObjectMode(function () { return 'replace'; })
      .nodeCanvasObject(draw)
      .nodePointerAreaPaint(pointerArea)
      .linkColor(linkColor)
      .linkWidth(function (l) {
        if (hlLinks.has(lid(l))) return 2.4;
        if (l.relation === 'required') return 1.2;
        if (l.relation === 'weak') return 0.85;
        return 1;
      })
      .linkDirectionalArrowLength(15)
      .linkDirectionalArrowRelPos(0.45)
      .linkDirectionalArrowColor(arrowColor)
      .linkCurvature(linkCurve)
      .onNodeHover(function (n) {
        hovered = n; refocus(); canvasWrap.style.cursor = n ? 'pointer' : '';
        if (hoverCb) hoverCb(n ? n.id : null);
      })
      .onNodeClick(selectNode)
      .onBackgroundClick(clearSelection)
      .graphData(data);

    // 기존 graph 페이지는 force-graph의 기본 실선을 그대로 사용한다.
    if (data.classified && graph.linkLineDash) graph.linkLineDash(linkDash);

    graph.d3VelocityDecay(0.34);
    graph.cooldownTicks(220);
    if (graph.d3Force('charge')) graph.d3Force('charge').strength(-260);
    if (graph.d3Force('link')) graph.d3Force('link').distance(34);
    graph.d3Force('gravity', radial(0.18));
    if (graph.d3ReheatSimulation) graph.d3ReheatSimulation();

    var fitted = false;
    graph.onEngineStop(function () {
      if (!fitted && layoutMode === 'force') { graph.zoomToFit(0, 30); fitted = true; }
    });

    function flipShell(linear) {
      var index = stage.parentElement.querySelector('.graph-index');
      var elements = [stage, index].filter(Boolean);
      var first = elements.map(function (el) { return el.getBoundingClientRect(); });
      document.body.classList.toggle('dependencies-linear', linear);
      if (window.matchMedia && window.matchMedia('(prefers-reduced-motion: reduce)').matches) return;
      var last = elements.map(function (el) { return el.getBoundingClientRect(); });
      elements.forEach(function (el, i) {
        if (!first[i].width || !first[i].height || !last[i].width || !last[i].height) return;
        el.style.transformOrigin = 'top left';
        el.style.transition = 'none';
        el.style.transform = 'translate(' + (first[i].left - last[i].left) + 'px,' +
          (first[i].top - last[i].top) + 'px) scale(' +
          (first[i].width / last[i].width) + ',' + (first[i].height / last[i].height) + ')';
      });
      stage.offsetWidth;
      window.requestAnimationFrame(function () {
        elements.forEach(function (el) {
          el.style.transition = 'transform 450ms cubic-bezier(.22,.61,.36,1)';
          el.style.transform = 'none';
        });
      });
      window.setTimeout(function () {
        elements.forEach(function (el) {
          el.style.removeProperty('transition'); el.style.removeProperty('transform');
          el.style.removeProperty('transform-origin');
        });
      }, 500);
    }

    function applyLinearGeometry() {
      var viewportWidth = canvasViewport.clientWidth;
      var viewportHeight = canvasViewport.clientHeight;
      if (!viewportWidth || !viewportHeight) return;
      linearGeometry = linearPositions(data, viewportWidth, viewportHeight);
      assignLanes();
      renderLinear();
    }
    function sizeForce() {
      var w = canvasViewport.clientWidth, h = canvasViewport.clientHeight;
      if (!w || !h) return;
      canvasWrap.style.width = '100%'; canvasWrap.style.height = '100%';
      graph.width(w).height(h);
    }
    function centerActive() {
      var node = activeFocus();
      if (layoutMode === 'linear') {
        if (!linearGeometry || !node) {
          canvasViewport.scrollTo({ left: 0, behavior: 'smooth' });
          return;
        }
        var x = linearGeometry.positions[node.id].x - canvasViewport.clientWidth / 2;
        var max = Math.max(0, linearGeometry.width - canvasViewport.clientWidth);
        canvasViewport.scrollTo({ left: Math.max(0, Math.min(max, x)), behavior: 'smooth' });
      } else if (node) graph.centerAt(node.x, node.y, 450);
      else graph.zoomToFit(450, 30);
    }
    function fitForceSelection() {
      if (!selected) {
        graph.zoomToFit(450, 30);
        return;
      }
      var visibleIds = new Set([selected.id]);
      (outAdj[selected.id] || new Set()).forEach(function (id) { visibleIds.add(id); });
      (inAdj[selected.id] || new Set()).forEach(function (id) { visibleIds.add(id); });
      var bbox = graph.getGraphBbox(function (node) { return visibleIds.has(node.id); });
      if (!bbox) return;
      var padding = 44;
      var width = Math.max(1, bbox.x[1] - bbox.x[0]);
      var height = Math.max(1, bbox.y[1] - bbox.y[0]);
      var zoom = Math.min(
        8,
        Math.max(1, (canvasViewport.clientWidth - padding * 2) / width),
        Math.max(1, (canvasViewport.clientHeight - padding * 2) / height)
      );
      graph.centerAt((bbox.x[0] + bbox.x[1]) / 2, (bbox.y[0] + bbox.y[1]) / 2, 450);
      graph.zoom(zoom, 450);
    }
    function afterLayout(fn) {
      window.requestAnimationFrame(function () { window.requestAnimationFrame(fn); });
    }
    function setLayout(mode, button) {
      if (mode === layoutMode) return;
      var linear = mode === 'linear';
      layoutMode = mode;
      stage.dataset.layoutMode = mode;
      flipShell(linear);
      refocus();
      if (linear) {
        if (graph.enableNodeDrag) graph.enableNodeDrag(false);
        if (graph.enableZoomPanInteraction) graph.enableZoomPanInteraction(false);
        button.innerHTML = ICON.force; button.title = cfg.forceLabel;
        button.setAttribute('aria-pressed', 'true');
        afterLayout(function () { applyLinearGeometry(); centerActive(); });
      } else {
        linearGeometry = null;
        if (graph.enableNodeDrag) graph.enableNodeDrag(true);
        if (graph.enableZoomPanInteraction) graph.enableZoomPanInteraction(true);
        button.innerHTML = ICON.tree; button.title = cfg.linearLabel;
        button.setAttribute('aria-pressed', 'false');
        afterLayout(function () {
          sizeForce();
          if (graph.d3ReheatSimulation) graph.d3ReheatSimulation();
          graph.zoomToFit(450, 30);
        });
      }
    }

    top.querySelectorAll('.gc-btn').forEach(function (b) {
      b.addEventListener('click', function () {
        if (b.dataset.act === 'layout') setLayout(layoutMode === 'force' ? 'linear' : 'force', b);
        else if (b.dataset.act === 'fit') {
          if (layoutMode === 'linear') centerActive();
          else fitForceSelection();
        }
        else if (cfg.onReset) { cfg.onReset(); if (layoutMode === 'force') graph.zoomToFit(450, 30); }
        else if (layoutMode === 'force') graph.zoomToFit(450, 30);
      });
    });

    function size() {
      if (layoutMode === 'linear') applyLinearGeometry();
      else sizeForce();
    }
    size();
    if (window.ResizeObserver) new ResizeObserver(size).observe(canvasViewport);

    return {
      graph: graph, deg: deg, byId: byId,
      refit: centerActive,
      focus: function (id) { hovered = id ? byId[id] : null; refocus(); },
      setQuery: function (q) { query = (q || '').toLowerCase().trim(); refocus(); },
      setFamilies: function (arr) { activeFams = new Set(arr); refocus(); },
      select: function (id) {
        var n = id ? byId[id] : null;
        if (n) selectNode(n); else clearSelection();
      },
      clear: function () {
        selected = null; hovered = null; query = '';
        activeFams = new Set(families.map(function (f) { return f.key; }));
        hidePop(); refocus(); canvasViewport.scrollLeft = 0; notifySelection();
      },
      onHover: function (cb) { hoverCb = cb; },
      onClick: function (cb) { clickCb = cb; }
    };
  }

  /* ---------- index panel ---------- */
  function buildIndex(panel, summary, data, deg, byId, families, card, lang) {
    var t = lang === 'ko'
      ? {
          index: '색인', posts: '개 글', search: '글 검색…', connected: '연결 많은 글',
          selected: '선택한 글', earliest: '가장 앞선 선수 글', opens: '이 글이 열어주는 글',
          selectHint: '그래프의 노드를 클릭하면 그 글의 선수 글과 이어지는 글을 여기에 고정해 볼 수 있습니다.',
          noPrereqs: 'required로 연결된 선수 글이 없습니다.',
          noOpens: '이 글을 선수로 삼는 글이 아직 없습니다.',
          countPre: '선수 ', countPost: '편'
        }
      : {
          index: 'INDEX', posts: 'posts', search: 'Search posts…', connected: 'MOST CONNECTED',
          selected: 'SELECTED POST', earliest: 'EARLIEST PREREQUISITES', opens: 'UNLOCKED BY THIS',
          selectHint: 'Click a graph node to pin its prerequisites and what it leads to here.',
          noPrereqs: 'This post has no required prerequisites.',
          noOpens: 'No post lists this one as a prerequisite yet.',
          countPre: '', countPost: ' prerequisites'
        };
    var famByKey = {}; families.forEach(function (f) { famByKey[f.key] = f; });
    var rowIndex = {}; // id -> [row els]
    var requiredParents = {}, requiredChildren = {};
    data.nodes.forEach(function (n) { requiredParents[n.id] = []; requiredChildren[n.id] = []; });
    data.links.forEach(function (link) {
      if (link.relation !== 'required') return;
      var e = endpoints(link);
      if (requiredParents[e[1]]) requiredParents[e[1]].push(e[0]);
      if (requiredChildren[e[0]]) requiredChildren[e[0]].push(e[1]);
    });

    // required 만 따라간 도달 집합 (자기 자신 제외).
    function closure(id, adj) {
      var seen = new Set(), todo = [id];
      while (todo.length) {
        var current = todo.pop();
        (adj[current] || []).forEach(function (next) {
          if (seen.has(next)) return;
          seen.add(next); todo.push(next);
        });
      }
      seen.delete(id);
      return seen;
    }
    function byWeightThenTitle(a, b) {
      return (Number(a.weight) || 0) - (Number(b.weight) || 0) ||
        a.title.localeCompare(b.title, lang);
    }

    function earliestPrerequisites(id) {
      var reachable = closure(id, requiredParents);
      var roots = Array.from(reachable).filter(function (candidate) {
        return !(requiredParents[candidate] || []).some(function (parent) {
          return reachable.has(parent);
        });
      });
      // required 관계에 순환이 있으면 뿌리가 안 남는다 — 그때는 가장 이른 층으로 대신한다.
      if (!roots.length && reachable.size) {
        var ancestors = Array.from(reachable);
        var minWeight = Math.min.apply(null, ancestors.map(function (candidate) {
          return Number(byId[candidate].weight) || 0;
        }));
        roots = ancestors.filter(function (candidate) {
          return (Number(byId[candidate].weight) || 0) === minWeight;
        });
      }
      return roots.map(function (root) { return byId[root]; }).filter(Boolean)
        .sort(function (a, b) { return a.title.localeCompare(b.title, lang); });
    }

    /* 선수 폐포의 규모와 분야 구성 한 줄 — "선수 9편 · 기초 5 · 대수 4".
       뿌리 목록만으로는 그 뒤에 몇 편이 더 있는지, 어느 분야인지가 안 보인다. */
    function prerequisiteMeta(reachable) {
      if (!reachable.size) return '';
      var byFamily = {};
      reachable.forEach(function (id) {
        var key = (byId[id] || {}).family;
        if (key) byFamily[key] = (byFamily[key] || 0) + 1;
      });
      var parts = Object.keys(byFamily).sort(function (a, b) {
        return byFamily[b] - byFamily[a] || a.localeCompare(b);
      }).map(function (key) {
        var fam = famByKey[key] || {};
        var label = (lang === 'ko' && fam.label_ko) ? fam.label_ko : (fam.label || key);
        return label + ' ' + byFamily[key];
      });
      return [t.countPre + reachable.size + t.countPost].concat(parts).join(' · ');
    }

    function renderSummary(id) {
      if (!summary) return;
      summary.innerHTML = '';
      var node = id ? byId[id] : null;
      if (!node) {
        var hint = document.createElement('p'); hint.className = 'gs-empty';
        hint.textContent = t.selectHint; summary.appendChild(hint); return;
      }
      function kicker(text) {
        var el = document.createElement('div');
        el.className = 'gs-kicker'; el.textContent = text;
        summary.appendChild(el);
      }
      function note(text, cls) {
        var el = document.createElement('p');
        el.className = cls; el.textContent = text;
        summary.appendChild(el);
      }
      function list(items) {
        var ul = document.createElement('ul'); ul.className = 'gs-prereqs';
        items.forEach(function (n) {
          var li = document.createElement('li'); li.className = 'gs-prereq';
          var link = document.createElement('a');
          link.href = n.url; link.textContent = n.title;
          li.appendChild(link); ul.appendChild(li);
        });
        summary.appendChild(ul);
      }

      kicker(t.selected);
      var title = document.createElement('a'); title.className = 'gs-title';
      title.href = node.url; title.textContent = node.title; summary.appendChild(title);

      kicker(t.earliest);
      var ancestors = closure(id, requiredParents);
      var roots = earliestPrerequisites(id);
      if (roots.length) {
        var meta = prerequisiteMeta(ancestors);
        if (meta) note(meta, 'gs-meta');
        list(roots);
      } else {
        note(t.noPrereqs, 'gs-empty');
      }

      kicker(t.opens);
      var opens = Array.from(closure(id, requiredChildren))
        .map(function (x) { return byId[x]; }).filter(Boolean).sort(byWeightThenTitle);
      if (opens.length) list(opens);
      else note(t.noOpens, 'gs-empty');
    }

    function reg(id, el) { (rowIndex[id] = rowIndex[id] || []).push(el); }
    function rowEl(n) {
      var row = document.createElement('div');
      row.className = 'gi-row'; row.dataset.id = n.id;
      row.innerHTML = '<i style="background:' + n.color + '"></i><span class="gi-title"></span><span class="gi-deg">' + (deg[n.id] || 0) + '</span>';
      row.querySelector('.gi-title').textContent = n.title;
      row.addEventListener('mouseenter', function () { card.focus(n.id); });
      row.addEventListener('mouseleave', function () { card.focus(null); });
      row.addEventListener('click', function () { card.select(n.id); });
      reg(n.id, row);
      return row;
    }

    // categories
    var cats = {};
    data.nodes.forEach(function (n) {
      (cats[n.category] || (cats[n.category] = { family: n.family, color: n.color, nodes: [] })).nodes.push(n);
    });
    Object.keys(cats).forEach(function (k) {
      cats[k].nodes.sort(function (a, b) { return (deg[b.id] || 0) - (deg[a.id] || 0); });
    });

    panel.innerHTML = '';
    var head = document.createElement('div'); head.className = 'gi-head';
    head.innerHTML = '<b>' + t.index + '</b><span class="gi-count">' + data.nodes.length + ' ' + t.posts + '</span>';
    panel.appendChild(head);

    var search = document.createElement('div'); search.className = 'gi-search';
    search.innerHTML = ICON.search + '<input type="text" spellcheck="false">';
    var input = search.querySelector('input'); input.placeholder = t.search;
    panel.appendChild(search);

    var fams = document.createElement('div'); fams.className = 'gi-fams';
    families.forEach(function (f) {
      var chip = document.createElement('button');
      chip.className = 'gi-chip on'; chip.dataset.fam = f.key;
      chip.innerHTML = '<i style="background:hsl(' + f.hue + ',55%,60%)"></i>' + (lang === 'ko' ? f.label_ko : f.label);
      chip.addEventListener('click', function () { chip.classList.toggle('on'); applyFilter(); });
      fams.appendChild(chip);
    });
    panel.appendChild(fams);

    var list = document.createElement('div'); list.className = 'gi-list';
    panel.appendChild(list);

    // MOST CONNECTED
    var hubTitle = document.createElement('div'); hubTitle.className = 'gi-section';
    hubTitle.textContent = t.connected;
    list.appendChild(hubTitle);
    var hubRows = [];
    data.nodes.slice().sort(function (a, b) { return (deg[b.id] || 0) - (deg[a.id] || 0); })
      .slice(0, 6).forEach(function (n) { var r = rowEl(n); hubRows.push({ el: r, node: n }); list.appendChild(r); });

    // families -> categories
    var catEntries = [];
    families.forEach(function (f) {
      var catsInFam = Object.keys(cats).filter(function (c) { return cats[c].family === f.key; }).sort();
      if (!catsInFam.length) return;
      var divider = document.createElement('div'); divider.className = 'gi-section';
      divider.innerHTML = '<i style="background:hsl(' + f.hue + ',55%,60%)"></i>' + (lang === 'ko' ? f.label_ko : f.label);
      list.appendChild(divider);
      var dividerCats = [];
      catsInFam.forEach(function (c) {
        var cat = cats[c];
        var wrap = document.createElement('div'); wrap.className = 'gi-cat';
        var chead = document.createElement('div'); chead.className = 'gi-cat-head';
        chead.innerHTML = ICON.caret + '<span class="gi-cat-dot" style="background:' + cat.color + '"></span><span class="gi-cat-name"></span><span class="gi-cat-count">' + cat.nodes.length + '</span>';
        chead.querySelector('.gi-cat-name').textContent = prettify(c);
        var body = document.createElement('div'); body.className = 'gi-cat-body';
        var rows = cat.nodes.map(function (n) { var r = rowEl(n); body.appendChild(r); return { el: r, node: n }; });
        chead.addEventListener('click', function () { wrap.classList.toggle('open'); });
        wrap.appendChild(chead); wrap.appendChild(body);
        list.appendChild(wrap);
        var entry = { family: f.key, wrap: wrap, head: chead, rows: rows };
        catEntries.push(entry); dividerCats.push(entry);
      });
      catEntries.dividers = catEntries.dividers || [];
      catEntries.dividers.push({ el: divider, family: f.key, cats: dividerCats });
    });

    function activeFamSet() {
      var s = new Set();
      fams.querySelectorAll('.gi-chip.on').forEach(function (c) { s.add(c.dataset.fam); });
      return s;
    }
    function applyFilter() {
      var q = input.value.toLowerCase().trim();
      var af = activeFamSet();
      card.setQuery(q); card.setFamilies(Array.from(af));

      // MOST CONNECTED
      var hubAny = false;
      hubRows.forEach(function (h) {
        var ok = af.has(h.node.family) && (!q || h.node.title.toLowerCase().indexOf(q) >= 0);
        h.el.classList.toggle('hidden', !ok); if (ok) hubAny = true;
      });
      hubTitle.classList.toggle('hidden', !hubAny);

      // categories
      catEntries.forEach(function (ce) {
        var famOn = af.has(ce.family);
        var any = false;
        ce.rows.forEach(function (r) {
          var ok = famOn && (!q || r.node.title.toLowerCase().indexOf(q) >= 0);
          r.el.classList.toggle('hidden', !ok); if (ok) any = true;
        });
        var show = famOn && (!q || any);
        ce.head.classList.toggle('hidden', !show);
        ce.wrap.style.display = show ? '' : 'none';
        if (q && any) ce.wrap.classList.add('open');
      });

      // dividers
      (catEntries.dividers || []).forEach(function (d) {
        var any = d.cats.some(function (c) { return c.wrap.style.display !== 'none'; });
        d.el.classList.toggle('hidden', !any);
      });
    }

    input.addEventListener('input', applyFilter);

    // graph -> index
    var hot = [];
    card.onHover(function (id) {
      hot.forEach(function (el) { el.classList.remove('hot'); }); hot = [];
      if (id && rowIndex[id]) { rowIndex[id].forEach(function (el) { el.classList.add('hot'); hot.push(el); }); }
    });
    var selEls = [];
    card.onClick(function (id) {
      selEls.forEach(function (el) { el.classList.remove('sel'); }); selEls = [];
      if (id && rowIndex[id]) { rowIndex[id].forEach(function (el) { el.classList.add('sel'); selEls.push(el); }); }
      renderSummary(id);
    });
    renderSummary(null);

    // reset button also clears the index UI
    return {
      reset: function () {
        input.value = '';
        fams.querySelectorAll('.gi-chip').forEach(function (c) { c.classList.add('on'); });
        applyFilter();
      }
    };
  }

  function init() {
    var stage = document.getElementById('xgraph');
    var panel = document.getElementById('graph-index');
    var summary = document.getElementById('graph-selection');
    if (!stage || !panel || typeof ForceGraph === 'undefined') return;
    var lang = stage.dataset.lang || 'ko';
    var source = stage.dataset.graphSource || 'graph';
    var layoutToggle = stage.dataset.layoutToggle === 'true';
    if (layoutToggle) {
      document.body.classList.add('dependencies-page');
      stage.dataset.layoutMode = 'force';
    }

    fetch('/assets/data/' + source + '-' + lang + '.json')
      .then(function (r) { return r.json(); })
      .then(function (data) {
        var cfg = {
          nodeSat: 48, nodeLight: 60, glow: 14,
          accent: '240,198,116', link: '150,150,160',
          accentIn: '165,111,20', accentOut: '107,58,0',
          label: '174,168,150', labelHi: '240,198,116',
          font: '"MySansSerifFont", system-ui, sans-serif',
          openLabel: lang === 'ko' ? '글로 이동 →' : 'Open post →',
          layoutToggle: layoutToggle,
          linearLabel: lang === 'ko' ? '선형 학습 보기' : 'Linear learning view',
          forceLabel: lang === 'ko' ? '힘 기반 그래프로 돌아가기' : 'Return to force-directed graph'
        };
        var fams = (data.families && data.families.length) ? data.families : FAMILIES_FALLBACK;
        var card = createGraphCard(stage, data, fams, cfg);
        if (!card) return;
        var idx = buildIndex(panel, summary, data, card.deg, card.byId, fams, card, lang);
        cfg.onReset = function () { card.clear(); idx.reset(); };
      })
      .catch(function () {});
  }

  if (document.readyState !== 'loading') init();
  else document.addEventListener('DOMContentLoaded', init);
})();
