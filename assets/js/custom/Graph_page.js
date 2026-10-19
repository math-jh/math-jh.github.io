/* Graph_page.js — 분류 기반 전역 학습 그래프 페이지(/ko/dependencies, /en/dependencies).
 *
 * 핸드오프 graphcard.js 포팅: 항상-다크 Brass 카드(force-graph 래퍼 + 툴바 + 팝업) +
 * 왼쪽 인덱스 패널(검색 · family 필터 · MOST CONNECTED · 카테고리 아코디언). 인덱스와
 * 그래프는 외부 API(focus/select/setQuery/setFamilies/onHover/onClick)로 양방향 연동.
 * 데이터는 dependencies-<lang>.json. 카드 내 검색/범례는 인덱스가 가지므로 제외.
 */
(function () {
  'use strict';

  // 선형 보기의 열·레인·선 모양은 Linear_layout.js 가 정한다 (로컬 그래프와 공유).
  var Layout = window.LinearLayout;
  var endpoints = Layout.endpoints, lid = Layout.lid;
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

  /* 선형 보기 배치. 열과 레인은 Linear_layout.js 가 정하고, 가장 깊은 글에서 첫 부모를
     거슬러 올라간 사슬이 0 번 레인의 본류가 된다. 여기서는 카드 크기에 맞춰 x·y 를 놓는다. */
  function linearPositions(data, viewportWidth, viewportHeight) {
    var cols = Layout.readingColumns(data), column = cols.column, columns = cols.columns;
    var ranks = Layout.readingParents(data, column), order = ranks.order;
    var lanes = Layout.lanes(order, ranks.parents, ranks.depth, ranks.degree, column, null);
    var lane = lanes.lane, minLane = lanes.minLane, maxLane = lanes.maxLane;
    var spread = Layout.spreadColumns(order, column, columns, 48);
    // 오른쪽 여백은 본류 끝 글의 비스듬한 라벨이 들어갈 자리다.
    var width = Math.max(viewportWidth, Math.ceil(spread.columnX[columns - 1] + 170));

    // y: 레인 간격 15px. 카드에 다 안 들어가면 9px 까지 좁히고, 그래도 넘치면 세로로 스크롤한다.
    var padY = 26, span = Math.max(1, maxLane - minLane);
    var laneGap = Math.max(9, Math.min(15, (viewportHeight - 2 * padY) / span));
    var height = Math.max(viewportHeight, Math.ceil(span * laneGap + 2 * padY));
    var top = (height - span * laneGap) / 2;

    var positions = {};
    order.forEach(function (id) {
      positions[id] = { x: spread.x[id], y: top + (lane[id] - minLane) * laneGap };
    });
    return {
      positions: positions, width: width, height: height, laneGap: laneGap,
      column: column, lane: lane, firstParent: lanes.firstParent
    };
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
    reset: '<svg viewBox="0 0 16 16" width="15" height="15"><path d="M13 8a5 5 0 1 1-1.6-3.7M13 2.2V5h-2.8" fill="none" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"/></svg>',
    link: '<svg viewBox="0 0 16 16" width="12" height="12" aria-hidden="true"><path d="M6.8 9.2a3 3 0 0 0 4.2 0l2.1-2.1a3 3 0 0 0-4.2-4.2l-.9.9M9.2 6.8a3 3 0 0 0-4.2 0L2.9 8.9a3 3 0 0 0 4.2 4.2l.9-.9" fill="none" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"/></svg>'
  };

  /* ---------- card engine (graphcard.js 포팅) ---------- */
  function createGraphCard(stage, data, families, cfg) {
    var famKeys = new Set(families.map(function (f) { return f.key; }));
    var deg = {}, outAdj = {}, inAdj = {}, byId = {};
    var requiredIn = {}, weakIn = {}, forwardOut = {};
    // required 링크만의 전방 인접. 경로 탐색은 이 방향으로만 간다 — required 는
    // 선수 글 → 그 글을 읽는 글이고, weak·forward 는 읽는 순서를 강제하지 않는다.
    var requiredNext = {};
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
      if (l.relation === 'required') {
        (requiredIn[e[1]] = requiredIn[e[1]] || []).push(l);
        (requiredNext[e[0]] = requiredNext[e[0]] || []).push(l);
      }
      else if (l.relation === 'weak') (weakIn[e[1]] = weakIn[e[1]] || []).push(l);
      else if (l.relation === 'forward') (forwardOut[e[0]] = forwardOut[e[0]] || []).push(l);
    });

    /* 프레임마다 링크 전부를 훑는 접근자는 여기서 미리 값을 박아 둔다.
       force-graph 는 곡률·색·폭 접근자를 렌더 프레임마다 링크 하나하나에 호출하고,
       포인터 판정용 shadow canvas 가 같은 순회를 한 번 더 돈다. 접근자 안에서
       링크 목록을 다시 훑으면 그 한 번이 링크 수의 제곱이 된다. */
    (function precomputeLinkFields() {
      var seen = new Set();
      data.links.forEach(function (l) {
        var e = endpoints(l);
        l.__lid = e[0] + '>' + e[1];
        seen.add(l.__lid);
      });
      data.links.forEach(function (l) {
        var e = endpoints(l);
        // 마주 보는 링크가 있으면 둘이 겹쳐 한 줄로 보이므로 휘어 놓는다.
        l.__curve = seen.has(e[1] + '>' + e[0]) ? 0.25 : 0;
      });
    }());

    var hovered = null, selected = null, pairWith = null, query = '', layoutMode = 'force';
    var activeFams = new Set(families.map(function (f) { return f.key; }));
    var hlNodes = new Set(), hlLinks = new Set();
    /* 두 글을 고른 화면에만 쓰는 둘째 층. 경로 위의 선은 hlLinks(평소 강조색),
       경로 밖에서 경로로 들어오는 선은 여기(연한 악센트)에 담는다. 둘을 한
       집합에 넣으면 '이 길'과 '이 길로 들어오는 것'이 같은 굵기·같은 색이 되어
       경로가 묻힌다. */
    var hlSoftNodes = new Set(), hlSoftLinks = new Set();
    var hoverCb = null, clickCb = null, linearGeometry = null;
    var linearNodeEls = [], linearLinkEls = [];

    function radius(n) {
      // 선형 보기는 레인 간격이 15px 이라 점을 작게 둔다.
      if (layoutMode === 'linear') return Math.min(4.4, 2.2 + 0.32 * Math.sqrt(deg[n.id] || 0));
      return 2.6 + 0.8 * Math.sqrt(deg[n.id] || 0);
    }

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
      if (hlNodes.size && !hlNodes.has(n.id)) {
        return hlSoftNodes.has(n.id) ? 'idle' : 'off';
      }
      return 'on';
    }
    function addHighlightedLink(link) {
      var e = endpoints(link);
      hlNodes.add(e[0]); hlNodes.add(e[1]); hlLinks.add(lid(link));
    }
    function focusForce(node) {
      hlNodes = new Set(); hlLinks = new Set();
      hlSoftNodes = new Set(); hlSoftLinks = new Set();
      if (!node) return;
      hlNodes.add(node.id);
      (outAdj[node.id] || new Set()).forEach(function (x) { hlNodes.add(x); });
      (inAdj[node.id] || new Set()).forEach(function (x) { hlNodes.add(x); });
      data.links.forEach(function (l) {
        var e = endpoints(l);
        if (e[0] === node.id || e[1] === node.id) hlLinks.add(lid(l));
      });
    }
    /* 이 노드를 고르면 함께 켜지는 엣지들. 조상(required 를 거슬러 닿는 글)은 전부 켜지만,
       조상 사이의 선을 다 그리면 수백 개가 엉킨다. 그래서 그리는 선은
         1. 고른 글로 들어오는 선 전부 — 첫 부모가 아닌 다른 부모까지,
         2. 조상끼리의 첫 부모 선 전부 — 레인 위의 직선이다,
         3. 1·2 만으로는 오른쪽으로 나가는 선이 없는 조상(줄기 끝)에서 가장 가까운 오른쪽
            조상으로 가는 선 하나.
       3 이 있어서 켜진 어느 글에서든 그려진 선만 따라 고른 글까지 끊기지 않고 간다. */
    function linearFocusLinks(id) {
      var out = [];
      // Only the chosen article may branch to optional context. Weak edges point
      // cited -> citing, while forward edges point citing -> later reading.
      (weakIn[id] || []).forEach(function (l) { out.push(l); });
      (forwardOut[id] || []).forEach(function (l) { out.push(l); });

      // Required edges point prerequisite -> dependent. Walk only upstream and
      // never expand weak/forward edges from prerequisites reached on this walk.
      var inside = [], ancestors = new Set(), todo = [id], seen = new Set();
      while (todo.length) {
        var here = todo.pop();
        if (seen.has(here)) continue;
        seen.add(here);
        (requiredIn[here] || []).forEach(function (link) {
          var source = endpoints(link)[0];
          inside.push(link); ancestors.add(source);
          if (!seen.has(source)) todo.push(source);
        });
      }
      var geo = linearGeometry;
      if (!geo) return out.concat(inside);
      var leaves = new Set(), fromSource = {};
      inside.forEach(function (link) {
        var e = endpoints(link);
        if (e[1] === id || geo.firstParent[e[1]] === e[0]) { out.push(link); leaves.add(e[0]); }
        (fromSource[e[0]] = fromSource[e[0]] || []).push(link);
      });
      ancestors.forEach(function (source) {
        if (leaves.has(source)) return;
        var col = geo.column[source], lane = geo.lane[source];
        var options = fromSource[source].filter(function (link) { return geo.column[endpoints(link)[1]] > col; });
        if (!options.length) options = fromSource[source];
        options.sort(function (a, b) {
          var ta = endpoints(a)[1], tb = endpoints(b)[1];
          return geo.column[ta] - geo.column[tb] ||
            Math.abs(geo.lane[ta] - lane) - Math.abs(geo.lane[tb] - lane) || lid(a).localeCompare(lid(b));
        });
        out.push(options[0]);
      });
      return out;
    }
    function focusLinear(node) {
      hlNodes = new Set(); hlLinks = new Set();
      hlSoftNodes = new Set(); hlSoftLinks = new Set();
      if (!node) return;
      hlNodes.add(node.id);
      linearFocusLinks(node.id).forEach(addHighlightedLink);
    }
    /* force-graph 는 자기가 아는 prop 이 바뀌었을 때와 시뮬레이션이 도는 동안만
       다시 그린다. 강조·필터·검색은 그 바깥의 상태라 알려 줄 방법이 필요한데, 이
       빌드에는 refresh() 가 없다. 같은 배율로 zoom 을 다시 설정하면 화면상 무동작인
       채로 needsRedraw 가 선다. 이게 없으면 골라도 그림이 안 바뀐다. */
    var repaintQueued = false;
    function repaint() {
      if (!graph || repaintQueued) return;
      // 시뮬레이션이 도는 동안은 어차피 매 프레임 다시 그린다.
      if (graph.isEngineRunning && graph.isEngineRunning()) return;
      repaintQueued = true;
      window.requestAnimationFrame(function () {
        repaintQueued = false;
        try { graph.zoom(graph.zoom()); } catch (e) { /* 아직 붙기 전 */ }
      });
    }
    // required 를 앞(forward)이나 뒤로 따라간 도달 집합 (시작 글 포함).
    function requiredReach(startId, forward) {
      var seen = new Set([startId]), todo = [startId];
      while (todo.length) {
        var here = todo.pop();
        ((forward ? requiredNext : requiredIn)[here] || []).forEach(function (link) {
          var next = endpoints(link)[forward ? 1 : 0];
          if (!seen.has(next)) { seen.add(next); todo.push(next); }
        });
      }
      return seen;
    }
    /* A 에서 B 로 가는 required 경로 전부를 글 단위로 합친 것. 경로 수는 쌍에 따라
       수천만 개라 경로를 나열하지 않고, 어느 경로에든 오르는 글을 단계로 묶는다.
       단계는 A 로부터의 최장 거리다. x 가 y 의 선수 글이면 y 의 단계가 더 크므로
       단계 순서대로 읽으면 선수 관계가 지켜진다. 서로를 선수로 삼는 글(순환)은
       순서를 정할 수 없으니 한 덩어리로 묶어 같은 단계에 둔다. */
    function requiredBetween(fromId, toId) {
      if (fromId === toId) return null;
      var after = requiredReach(fromId, true);
      if (!after.has(toId)) return null;
      var before = requiredReach(toId, false);
      var ids = Array.from(after).filter(function (id) { return before.has(id); });
      var inside = new Set(ids);
      var links = [], next = {};
      ids.forEach(function (id) {
        next[id] = [];
        (requiredNext[id] || []).forEach(function (link) {
          var target = endpoints(link)[1];
          if (!inside.has(target)) return;
          links.push(link); next[id].push(target);
        });
      });

      // 순환 묶기 (Tarjan). 구간 안의 글만 돈다.
      var comp = {}, index = {}, low = {}, stack = [], onStack = new Set();
      var counter = 0, comps = 0;
      function strong(v) {
        index[v] = low[v] = counter++; stack.push(v); onStack.add(v);
        next[v].forEach(function (w) {
          if (index[w] === undefined) { strong(w); low[v] = Math.min(low[v], low[w]); }
          else if (onStack.has(w)) low[v] = Math.min(low[v], index[w]);
        });
        if (low[v] !== index[v]) return;
        var w;
        do { w = stack.pop(); onStack.delete(w); comp[w] = comps; } while (w !== v);
        comps += 1;
      }
      ids.forEach(function (id) { if (index[id] === undefined) strong(id); });

      // 묶은 그래프에서 A 의 덩어리로부터의 최장 거리.
      var compNext = [], indegree = [], level = [], k;
      for (k = 0; k < comps; k++) { compNext.push(new Set()); indegree.push(0); level.push(0); }
      ids.forEach(function (id) {
        next[id].forEach(function (target) {
          var a = comp[id], b = comp[target];
          if (a === b || compNext[a].has(b)) return;
          compNext[a].add(b); indegree[b] += 1;
        });
      });
      var ready = [];
      for (k = 0; k < comps; k++) if (!indegree[k]) ready.push(k);
      while (ready.length) {
        var c = ready.pop();
        compNext[c].forEach(function (d) {
          level[d] = Math.max(level[d], level[c] + 1);
          if (--indegree[d] === 0) ready.push(d);
        });
      }
      var steps = [];
      ids.forEach(function (id) {
        var s = level[comp[id]];
        (steps[s] = steps[s] || []).push(id);
      });
      return { nodes: ids, links: links, steps: steps };
    }
    // 어느 쪽이 선수 글인지는 고른 순서가 아니라 그래프가 정한다.
    function pairPath() {
      if (!selected || !pairWith) return null;
      return requiredBetween(selected.id, pairWith.id) ||
        requiredBetween(pairWith.id, selected.id);
    }
    function focusPair() {
      hlNodes = new Set(); hlLinks = new Set();
      hlSoftNodes = new Set(); hlSoftLinks = new Set();
      var path = pairPath();
      if (!path) { hlNodes.add(selected.id); hlNodes.add(pairWith.id); return; }
      path.nodes.forEach(function (id) { hlNodes.add(id); });
      path.links.forEach(function (l) { hlLinks.add(lid(l)); });
      /* 경로 위의 글을 읽으려면 경로 밖에서도 와야 하는 선. 바깥 폐포를 통째로
         켜면 백 편이 넘어 경로가 묻히므로, 경로에 **직접 닿는** 선만 그린다.
         그 뒤로 얼마나 더 있는지는 옆 패널의 뿌리 목록이 맡는다. */
      path.nodes.forEach(function (id) {
        (requiredIn[id] || []).forEach(function (link) {
          var source = endpoints(link)[0];
          if (hlNodes.has(source)) return;
          hlSoftNodes.add(source);
          hlSoftLinks.add(lid(link));
        });
      });
    }
    function refocus() {
      var node = activeFocus();
      if (selected && pairWith) { focusPair(); updateLinearStyles(); repaint(); return; }
      if (layoutMode === 'linear') focusLinear(node);
      else focusForce(node);
      updateLinearStyles();
      repaint();
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
    function notifySelection() {
      if (clickCb) clickCb(selected ? selected.id : null, pairWith ? pairWith.id : null);
    }
    function clearSelection() {
      selected = null; pairWith = null; hidePop(); refocus(); notifySelection();
    }
    /* 한 번 누르면 고르고, 같은 것을 다시 누르면 뺀다. 다른 것을 누르면 둘이 짝이
       되어 그 사이 경로를 본다. 짝이 있는데 제3의 노드를 누르면 그것 하나만 남는다 —
       셋을 잇는 화면이 없으니 그게 예측 가능한 쪽이다. */
    function selectNode(node) {
      if (!node) return clearSelection();
      if (selected && selected.id === node.id) {
        if (!pairWith) return clearSelection();
        selected = pairWith; pairWith = null;
      } else if (pairWith && pairWith.id === node.id) {
        pairWith = null;
      } else if (selected && !pairWith) {
        pairWith = node;
      } else {
        selected = node; pairWith = null;
      }
      refocus();
      if (selected) { showPop(selected); centerActive(); } else hidePop();
      notifySelection();
    }
    popClose.addEventListener('click', function (e) { e.stopPropagation(); clearSelection(); });
    linearSvg.addEventListener('click', clearSelection);

    function svgElement(name, attrs) {
      var el = document.createElementNS('http://www.w3.org/2000/svg', name);
      Object.keys(attrs || {}).forEach(function (key) { el.setAttribute(key, attrs[key]); });
      return el;
    }
    // 왼쪽으로 가는 선(순환 안의 required, weak 일부)은 고른 화면에서만 보인다.
    function linkPath(link) {
      var e = endpoints(link);
      return Layout.linkPath(linearGeometry.positions[e[0]], linearGeometry.positions[e[1]],
        linearGeometry.firstParent[e[1]] === e[0]);
    }
    // 고른 글의 라벨은 점 오른쪽에 가로로, 나머지는 점 오른쪽 위나 아래로 비스듬히 놓는다.
    function labelBox(entry, spot, size, bold) {
      return Layout.labelBox(linearGeometry.positions[entry.node.id], radius(entry.node),
        entry.width, spot, size, bold);
    }
    var boxesOverlap = Layout.boxesOverlap;
    /* 어느 라벨을 띄울지. 중요한 것부터 자리를 잡고, 겹치는 덜 중요한 라벨은 숨긴다:
       고른 글(짝이면 둘) > 검색어에 맞는 글 > 고른 글과 바로 이어진 글 > 그 밖의 켜진 글.
       고르거나 짚은 글도 검색어도 없으면 라벨을 띄우지 않는다. */
    function placeLinearLabels() {
      var focus = activeFocus(), pair = selected && pairWith;
      var primary = new Set(), direct = new Set(), focusing = hlNodes.size > 0;
      if (pair) { primary.add(selected.id); primary.add(pairWith.id); }
      else if (focus) {
        primary.add(focus.id);
        linearLinkEls.forEach(function (entry) {
          if (!hlLinks.has(lid(entry.link))) return;
          var e = endpoints(entry.link);
          if (e[1] === focus.id) direct.add(e[0]);
          else if (e[0] === focus.id) direct.add(e[1]);
        });
      }
      var candidates = [];
      linearNodeEls.forEach(function (entry) {
        var n = entry.node;
        entry.label.style.display = 'none';
        if (nodeState(n) === 'off') return;
        var matched = !!query && n.title.toLowerCase().indexOf(query) >= 0;
        var tier;
        if (primary.has(n.id)) tier = 0;
        else if (matched) tier = 1;
        else if (direct.has(n.id)) tier = 2;
        else if (focusing && hlNodes.has(n.id)) tier = 3;
        else return;
        candidates.push({ entry: entry, tier: tier, matched: matched });
      });
      candidates.sort(function (a, b) {
        return a.tier - b.tier || (deg[b.entry.node.id] || 0) - (deg[a.entry.node.id] || 0) ||
          (a.entry.node.id < b.entry.node.id ? -1 : 1);
      });
      var placed = [];
      candidates.forEach(function (c) {
        var main = c.tier === 0, size = main ? 12 : 10.5;
        var spots = main ? ['right', 'above', 'below'] : focusing ? ['above', 'below'] : ['below', 'above'];
        var box = null;
        for (var i = 0; i < spots.length && !box; i++) {
          var trial = labelBox(c.entry, spots[i], size, main);
          if (!placed.some(function (other) { return boxesOverlap(trial, other); })) box = trial;
        }
        // 고른 글의 라벨은 자리가 없어도 첫 자리에 띄운다.
        if (!box && main) box = labelBox(c.entry, spots[0], size, true);
        if (!box) return;
        placed.push(box);
        var label = c.entry.label, p = linearGeometry.positions[c.entry.node.id];
        var x = p.x + box.x, y = p.y + box.y;
        label.style.display = '';
        label.style.fontSize = size + 'px';
        label.style.fontWeight = main ? '600' : '400';
        label.setAttribute('x', x);
        label.setAttribute('y', y);
        if (box.angle) label.setAttribute('transform', 'rotate(' + box.angle + ' ' + x + ' ' + y + ')');
        else label.removeAttribute('transform');
        label.setAttribute('fill', 'rgba(' + (main ? cfg.accentLight : cfg.labelHi) + ',0.98)');
      });
    }
    // 글의 색을 투명도만 바꿔 쓴다. 두 보기의 흐린 점과 평상시 선이 이 색이다.
    function tint(n, alpha) {
      return n.family === 'misc'
        ? 'hsla(' + n.hue + ',0%,58%,' + alpha + ')'
        : 'hsla(' + n.hue + ',' + cfg.nodeSat + '%,' + cfg.nodeLight + '%,' + alpha + ')';
    }
    function updateLinearStyles() {
      if (!linearGeometry) return;
      var quiet = !activeFocus();
      linearLinkEls.forEach(function (entry) {
        var link = entry.link, key = lid(link), e = endpoints(link), path = entry.path;
        // 켜진 선은 모두 같은 굵기·진하기다. 레인 위 선과 합류선을 달리 칠하면 같은 길이
        // 중간에 끊겨 보인다.
        if (hlLinks.has(key) || hlSoftLinks.has(key)) {
          path.style.display = '';
          path.setAttribute('stroke', linkColor(link));
          path.setAttribute('stroke-width', hlLinks.has(key) ? '1.5' : '1.1');
          return;
        }
        // 평상시에 보이는 선은 첫 부모 선뿐이다. 나머지는 고르거나 짚을 때만 나온다.
        if (!entry.spine) { path.style.display = 'none'; return; }
        path.style.display = '';
        var on = quiet && passesFilter(byId[e[0]]) && passesFilter(byId[e[1]]);
        path.setAttribute('stroke', on ? tint(byId[e[1]], 0.5) : 'rgba(' + cfg.link + ',0.06)');
        path.setAttribute('stroke-width', '1.3');
      });
      // 약한 관계부터 DOM 앞쪽에 둔다. 강조된 선은 맨 위층이다.
      linearLinkEls.slice().sort(function (a, b) {
        return linearLinkPaintOrder(a.link, hlLinks.has(lid(a.link))) -
            linearLinkPaintOrder(b.link, hlLinks.has(lid(b.link))) || a.order - b.order;
      }).forEach(function (entry) { entry.path.parentNode.appendChild(entry.path); });
      linearNodeEls.forEach(function (entry) {
        var node = entry.node, state = nodeState(node);
        var isSelected = selected && selected.id === node.id;
        var opacity = state === 'off' ? '0.16' : state === 'idle' ? '0.45' : '1';
        entry.dot.setAttribute('r', isSelected ? 5.5 : radius(node));
        entry.dot.setAttribute('fill', isSelected ? 'rgb(' + cfg.accentLight + ')'
          : hlNodes.has(node.id) ? 'rgb(' + cfg.accent + ')' : node.__c);
        entry.dot.setAttribute('fill-opacity', opacity);
        entry.dot.setAttribute('stroke-opacity', opacity);
      });
      placeLinearLabels();
    }
    function renderLinear() {
      var geo = linearGeometry;
      linearSvg.innerHTML = '';
      linearNodeEls = []; linearLinkEls = [];
      linearSvg.setAttribute('width', Math.ceil(geo.width));
      linearSvg.setAttribute('height', Math.ceil(geo.height));
      linearSvg.setAttribute('viewBox', '0 0 ' + geo.width + ' ' + geo.height);
      linearSvg.style.width = Math.ceil(geo.width) + 'px';
      linearSvg.style.height = Math.ceil(geo.height) + 'px';

      // 방향은 왼쪽→오른쪽 읽는 순서가 말해 주므로 화살촉은 두지 않는다.
      var linksGroup = svgElement('g', { class: 'gc-linear__links' });
      data.links.forEach(function (link, index) {
        var e = endpoints(link);
        var path = svgElement('path', {
          d: linkPath(link), fill: 'none', 'stroke-linecap': 'round', 'stroke-linejoin': 'round'
        });
        if (link.relation === 'weak') path.setAttribute('stroke-dasharray', '2 5');
        else if (link.relation === 'forward') path.setAttribute('stroke-dasharray', '9 5');
        linksGroup.appendChild(path);
        linearLinkEls.push({ link: link, path: path, order: index, spine: geo.firstParent[e[1]] === e[0] });
      });
      linearSvg.appendChild(linksGroup);

      var nodesGroup = svgElement('g', { class: 'gc-linear__nodes' });
      // 라벨은 점들 위의 따로 된 층이다. 점 묶음 안에 두면 뒤에 그려지는 점이 라벨을 가린다.
      var labelsGroup = svgElement('g', { class: 'gc-linear__labels', 'aria-hidden': 'true' });
      // 누를 자리는 이웃 레인의 점과 겹치지 않을 만큼만.
      var hitRadius = Math.max(6, Math.min(11, geo.laneGap * 0.55));
      data.nodes.forEach(function (node) {
        var p = geo.positions[node.id];
        var group = svgElement('g', {
          class: 'gc-linear__node', transform: 'translate(' + p.x + ' ' + p.y + ')',
          tabindex: '0', role: 'button', 'aria-label': node.title
        });
        var hit = svgElement('circle', { r: hitRadius, fill: 'transparent' });
        var dot = svgElement('circle', { r: radius(node), stroke: 'rgb(15,16,20)', 'stroke-width': '1.4' });
        var label = svgElement('text', { x: p.x, y: p.y });
        label.textContent = node.title;
        labelsGroup.appendChild(label);
        var title = svgElement('title'); title.textContent = node.title; group.appendChild(title);
        group.appendChild(hit); group.appendChild(dot);
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
        linearNodeEls.push({ node: node, dot: dot, label: label, width: 0 });
      });
      linearSvg.appendChild(nodesGroup);
      linearSvg.appendChild(labelsGroup);
      // 라벨 폭은 그릴 때 한 번 잰다. 글꼴이 아직 안 왔으면 0 이 나오니 글자 수로 어림한다.
      linearNodeEls.forEach(function (entry) {
        var measured = 0;
        try { measured = entry.label.getComputedTextLength(); } catch (e) { /* 렌더 전 */ }
        entry.width = measured || entry.node.title.length * 9.5;
      });
      updateLinearStyles();
    }

    /* 힘 기반 보기의 점과 라벨은 선형 보기와 같은 문법이다. 고른 글은 밝은 brass 로 조금
       크게, 함께 켜진 글은 brass, 나머지는 제 색이고, 흐린 상태는 색은 두고 투명도만 낮춘다.
       점마다 어두운 테를 둘러 밑을 지나는 선과 갈라 준다. */
    function draw(node, ctx, scale) {
      var st = nodeState(node);
      var sel = selected && selected.id === node.id;
      var r = sel ? Math.max(radius(node) + 1.5, radius(node) * 1.3) : radius(node);
      ctx.save();
      ctx.globalAlpha = st === 'off' ? 0.16 : st === 'idle' ? 0.45 : 1;
      ctx.fillStyle = sel ? 'rgb(' + cfg.accentLight + ')'
        : hlNodes.has(node.id) ? 'rgb(' + cfg.accent + ')' : node.__c;
      ctx.beginPath(); ctx.arc(node.x, node.y, r, 0, 6.2832); ctx.fill();
      // 멀리서 보면 테가 점을 덮지 않게 반지름에 비례해 줄인다.
      ctx.lineWidth = Math.min(1.4 / scale, r * 0.4);
      ctx.strokeStyle = 'rgb(15,16,20)';
      ctx.stroke();
      ctx.restore();

      var focus = activeFocus();
      var main = focus && focus.id === node.id ||
        !!(selected && pairWith) && (selected.id === node.id || pairWith.id === node.id);
      var focused = hlNodes.size > 0 && hlNodes.has(node.id);
      var matched = query && node.title.toLowerCase().indexOf(query) >= 0;
      // 라벨은 고르거나 짚은 글과 그 이웃, 검색어에 맞는 글에만 띄운다.
      if (st !== 'off' && (main || focused || matched)) {
        var fs = Math.max(3.5, (main ? 12 : 10.5) / scale);
        var x = node.x, y = node.y + r + 2.5 / scale;
        ctx.font = (main ? '600 ' : '') + fs + 'px ' + cfg.font;
        ctx.textAlign = 'center'; ctx.textBaseline = 'top';
        ctx.lineJoin = 'round';
        ctx.lineWidth = 3 / scale;
        ctx.strokeStyle = 'rgba(15,16,20,0.9)';
        ctx.strokeText(node.title, x, y);
        ctx.fillStyle = 'rgba(' + (main ? cfg.accentLight : cfg.labelHi) + ',0.98)';
        ctx.fillText(node.title, x, y);
      }
    }
    function pointerArea(node, color, ctx) {
      ctx.fillStyle = color;
      ctx.beginPath(); ctx.arc(node.x, node.y, Math.max(11, radius(node)), 0, 6.2832); ctx.fill();
    }
    /* 켜진 선은 두 보기 모두 brass 한 색이다. 고른 글에서 나가는 forward 만 짙은 brass 로
       가른다. 평상시 선은 도착 글의 색으로 칠한다 — 선형 보기의 첫 부모 선과 같은 규칙이다. */
    function linkColor(l) {
      if (hlLinks.has(lid(l))) {
        var focused = activeFocus();
        if (focused && l.relation === 'forward' && endpoints(l)[0] === focused.id) {
          return 'rgba(' + cfg.accentOut + ',0.9)';
        }
        return 'rgba(' + cfg.accent + ',0.85)';
      }
      if (hlSoftLinks.has(lid(l))) return 'rgba(' + cfg.accent + ',0.3)';
      var e = endpoints(l);
      var on = passesFilter(byId[e[0]]) && passesFilter(byId[e[1]]) && !activeFocus();
      if (!on) return 'rgba(' + cfg.link + ',0.035)';
      // 접근자는 프레임마다 링크 수만큼 불리므로 색 문자열을 링크에 붙여 둔다.
      if (!l.__tint) {
        l.__tint = tint(byId[e[1]], l.relation === 'weak' ? 0.16 : l.relation === 'forward' ? 0.24 : 0.34);
      }
      return l.__tint;
    }
    // 화살촉은 링크와 같은 색·같은 투명도로 칠한다. 불투명하게 칠하면 면적이
    // 있는 만큼 뒤를 지나는 밝은 링크를 잘라 먹는다. weak 만 면적 때문에 점선보다
    // 도드라지므로 알파를 더 눌러 두고, 포커스된 링크는 brass 강조색을 그대로 쓴다.
    // 링크 색은 몇 가지 안 되는 문자열을 돌려쓰므로, 흐린 짝을 색마다 한 번만
    // 만들어 둔다. 정규식을 프레임마다 링크 수만큼 돌릴 이유가 없다.
    var fadedArrow = {};
    function arrowColor(l) {
      var color = linkColor(l);
      if (!data.classified || l.relation !== 'weak' || hlLinks.has(lid(l))) return color;
      if (fadedArrow[color] !== undefined) return fadedArrow[color];
      var rgba = color.match(/^rgba?\(\s*([\d.]+)\s*,\s*([\d.]+)\s*,\s*([\d.]+)(?:\s*,\s*([\d.]+))?\s*\)$/);
      var faded = color;
      if (rgba) {
        var alpha = (rgba[4] === undefined ? 1 : Number(rgba[4])) * 0.55;
        faded = 'rgba(' + rgba[1] + ',' + rgba[2] + ',' + rgba[3] + ',' + alpha + ')';
      }
      fadedArrow[color] = faded;
      return faded;
    }
    function linkDash(l) {
      if (l.relation === 'weak') return [2, 5];
      if (l.relation === 'forward') return [9, 5];
      return [];
    }
    function linkCurve(l) { return l.__curve || 0; }
    /* 화살촉은 링크마다 path 연산이라 제일 먼저 비싸진다. 멀리서 본 그림에서는
       수백 개가 겹쳐 방향이 읽히지도 않으므로, 방향을 실제로 읽을 수 있는 배율
       위에서만 그린다. 강조된 링크는 배율과 무관하게 그린다 — 그건 지금 따라가는
       선이다. */
    var ARROW_ZOOM = 1.1;
    var zoomLevel = 1;
    function arrowLength(l) {
      if (hlLinks.has(lid(l))) return 15;
      return zoomLevel >= ARROW_ZOOM ? 15 : 0;
    }

    var graph = ForceGraph()(canvasWrap)
      .backgroundColor('rgba(0,0,0,0)')
      .autoPauseRedraw(true)
      .nodeId('id')
      .nodeRelSize(5)
      .nodeVal(function (n) { return Math.pow(radius(n) / 5, 2); })
      .nodeColor(function () { return 'rgba(0,0,0,0)'; })
      .nodeCanvasObjectMode(function () { return 'replace'; })
      .nodeCanvasObject(draw)
      .nodePointerAreaPaint(pointerArea)
      .linkColor(linkColor)
      .linkWidth(function (l) {
        if (hlLinks.has(lid(l))) return 1.5;
        if (hlSoftLinks.has(lid(l))) return 1.1;
        if (l.relation === 'required') return 1.2;
        if (l.relation === 'weak') return 0.85;
        return 1;
      })
      .linkDirectionalArrowLength(arrowLength)
      .linkDirectionalArrowRelPos(0.45)
      .linkDirectionalArrowColor(arrowColor)
      .linkCurvature(linkCurve)
      .onNodeHover(function (n) {
        hovered = n; refocus(); canvasWrap.style.cursor = n ? 'pointer' : '';
        if (hoverCb) hoverCb(n ? n.id : null);
      })
      .onNodeClick(selectNode)
      .onBackgroundClick(clearSelection)
      .onZoom(function (t) { zoomLevel = t.k; })
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
      // 패널에서 짝을 지정한다. bId 가 없으면 짝만 풀고 aId 선택은 남긴다.
      pair: function (aId, bId) {
        var a = aId ? byId[aId] : null;
        if (!a) return clearSelection();
        selected = a;
        pairWith = bId && bId !== aId ? byId[bId] || null : null;
        refocus(); showPop(selected); centerActive(); notifySelection();
      },
      path: function (a, b) { return requiredBetween(a, b) || requiredBetween(b, a); },
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
          countPre: '선수 ', countPost: '편',
          pathTitle: '두 글 사이의 경로',
          pathMeta: function (steps, posts) { return steps + '단계 · 글 ' + posts + '편'; },
          noPath: '두 글은 required 로 이어져 있지 않습니다.',
          outside: '경로 밖에서 오는 선수 글',
          outsideMeta: function (roots, total) {
            return '바깥 선수 ' + total + '편 · 따로 시작해야 하는 글 ' + roots + '편';
          },
          noOutside: '경로 위의 글만으로 닫혀 있습니다.',
          showPath: '경로 보기', openPost: '글로 이동', back: '← 선택한 글로',
          more: function (n) { return '더보기 +' + n; }
        }
      : {
          index: 'INDEX', posts: 'posts', search: 'Search posts…', connected: 'MOST CONNECTED',
          selected: 'SELECTED POST', earliest: 'EARLIEST PREREQUISITES', opens: 'UNLOCKED BY THIS',
          selectHint: 'Click a graph node to pin its prerequisites and what it leads to here.',
          noPrereqs: 'This post has no required prerequisites.',
          noOpens: 'No post lists this one as a prerequisite yet.',
          countPre: '', countPost: ' prerequisites',
          pathTitle: 'PATH BETWEEN THE TWO',
          pathMeta: function (steps, posts) { return steps + ' steps · ' + posts + ' posts'; },
          noPath: 'The two posts are not linked by required edges.',
          outside: 'PREREQUISITES OFF THE PATH',
          outsideMeta: function (roots, total) {
            return total + ' off-path prerequisites · ' + roots + ' to start separately';
          },
          noOutside: 'The path is closed under its own prerequisites.',
          showPath: 'Show path', openPost: 'Open post', back: '← Back to selected post',
          more: function (n) { return 'Show ' + n + ' more'; }
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

    /* 경로 위 글들을 읽는 데 필요하지만 경로 밖에 있는 글. 전부 늘어놓으면 깊은
       구간에서 백 편이 넘으므로 그 바깥 가지들의 **뿌리만** 보인다 — 밖에서 따로
       시작해야 하는 자리다. 뿌리 = 바깥 집합 안에 선수 글이 없는 글. */
    function outsideRoots(pathIds) {
      var onPath = new Set(pathIds), outside = new Set();
      pathIds.forEach(function (id) {
        closure(id, requiredParents).forEach(function (x) {
          if (!onPath.has(x)) outside.add(x);
        });
      });
      var roots = Array.from(outside).filter(function (x) {
        return !(requiredParents[x] || []).some(function (parent) {
          return outside.has(parent);
        });
      });
      return {
        total: outside.size,
        roots: roots.map(function (x) { return byId[x]; })
          .filter(Boolean).sort(byWeightThenTitle)
      };
    }

    // 요약과 경로 두 렌더러가 같은 조각을 쓴다.
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
    /* pairFrom 이 있으면 항목 이름은 그 글과의 경로를 여는 버튼이 되고, 글로 가는
       링크는 옆의 링크 아이콘이 맡는다. */
    var LIST_MAX = 8;
    function postList(items, ordered, pairFrom) {
      var ul = document.createElement(ordered ? 'ol' : 'ul');
      ul.className = ordered ? 'gs-prereqs gs-path' : 'gs-prereqs';
      function item(n) {
        var li = document.createElement('li'); li.className = 'gs-prereq';
        if (pairFrom) {
          var pick = document.createElement('button');
          pick.type = 'button'; pick.className = 'gs-name';
          pick.textContent = n.title; pick.title = t.showPath;
          pick.addEventListener('click', function () { card.pair(pairFrom, n.id); });
          var go = document.createElement('a');
          go.className = 'gs-go'; go.href = n.url; go.innerHTML = ICON.link;
          go.title = t.openPost; go.setAttribute('aria-label', t.openPost + ': ' + n.title);
          li.appendChild(pick); li.appendChild(go);
        } else {
          var link = document.createElement('a');
          link.className = 'gs-name'; link.href = n.url; link.textContent = n.title;
          li.appendChild(link);
        }
        return li;
      }
      appendCapped(ul, items, item);
      summary.appendChild(ul);
    }
    // 항목이 여덟 개를 넘으면 일곱 개만 두고 여덟째 자리를 더보기가 차지한다.
    function appendCapped(container, items, render) {
      var shown = items.length > LIST_MAX ? items.slice(0, LIST_MAX - 1) : items;
      shown.forEach(function (x) { container.appendChild(render(x)); });
      if (shown.length === items.length) return;
      var moreItem = document.createElement('li'); moreItem.className = 'gs-more';
      var more = document.createElement('button');
      more.type = 'button'; more.textContent = t.more(items.length - shown.length);
      more.addEventListener('click', function () {
        container.removeChild(moreItem);
        items.slice(shown.length).forEach(function (x) { container.appendChild(render(x)); });
      });
      moreItem.appendChild(more); container.appendChild(moreItem);
    }
    // 단계 한 줄에 그 단계의 글을 모두 나란히 둔다. 같은 단계의 글끼리는 순서가 없다.
    function stepList(steps) {
      var ol = document.createElement('ol'); ol.className = 'gs-prereqs gs-path';
      appendCapped(ol, steps, function (ids) {
        var li = document.createElement('li'); li.className = 'gs-prereq gs-step';
        ids.map(function (x) { return byId[x]; }).filter(Boolean).sort(byWeightThenTitle)
          .forEach(function (n) {
            var link = document.createElement('a');
            link.className = 'gs-name'; link.href = n.url; link.textContent = n.title;
            li.appendChild(link);
          });
        return li;
      });
      summary.appendChild(ol);
    }

    /* 노드 두 개가 고른 상태일 때의 패널. 단일 선택 패널과는 별개다 — 묻는 게
       다르다. 여기서 묻는 건 "A 에서 B 까지 어떻게 가나"이고, 경로 계산은 카드가
       쥐고 있다(두 벌로 두면 강조된 선과 목록이 갈라진다). */
    function renderPath(aId, bId) {
      if (!summary) return;
      summary.innerHTML = '';
      var back = document.createElement('button');
      back.type = 'button'; back.className = 'gs-back'; back.textContent = t.back;
      back.addEventListener('click', function () { card.pair(aId, null); });
      summary.appendChild(back);
      var path = card.path ? card.path(aId, bId) : null;
      kicker(t.pathTitle);
      if (!path) {
        var ends = [byId[aId], byId[bId]].filter(Boolean);
        postList(ends);
        note(t.noPath, 'gs-empty');
        return;
      }
      note(t.pathMeta(path.steps.length, path.nodes.length), 'gs-meta');
      stepList(path.steps);

      kicker(t.outside);
      var off = outsideRoots(path.nodes);
      if (off.roots.length) {
        note(t.outsideMeta(off.roots.length, off.total), 'gs-meta');
        postList(off.roots);
      } else {
        note(t.noOutside, 'gs-empty');
      }
    }

    function renderSummary(id) {
      if (!summary) return;
      summary.innerHTML = '';
      var node = id ? byId[id] : null;
      if (!node) {
        var hint = document.createElement('p'); hint.className = 'gs-empty';
        hint.textContent = t.selectHint; summary.appendChild(hint); return;
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
        postList(roots, false, id);
      } else {
        note(t.noPrereqs, 'gs-empty');
      }

      kicker(t.opens);
      var opens = Array.from(closure(id, requiredChildren))
        .map(function (x) { return byId[x]; }).filter(Boolean).sort(byWeightThenTitle);
      if (opens.length) postList(opens, false, id);
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
    card.onClick(function (id, pairId) {
      selEls.forEach(function (el) { el.classList.remove('sel'); }); selEls = [];
      [id, pairId].forEach(function (key) {
        if (key && rowIndex[key]) {
          rowIndex[key].forEach(function (el) { el.classList.add('sel'); selEls.push(el); });
        }
      });
      if (id && pairId) renderPath(id, pairId);
      else renderSummary(id);
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
    var source = stage.dataset.graphSource || 'dependencies';
    var layoutToggle = stage.dataset.layoutToggle === 'true';
    if (layoutToggle) {
      document.body.classList.add('dependencies-page');
      stage.dataset.layoutMode = 'force';
    }

    fetch('/assets/data/' + source + '-' + lang + '.json')
      .then(function (r) { return r.json(); })
      .then(function (data) {
        var cfg = {
          nodeSat: 48, nodeLight: 60,
          accent: '240,198,116', accentLight: '255,236,190', link: '150,150,160',
          accentOut: '107,58,0',
          labelHi: '240,198,116',
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
