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
  // 더한다. weight는 아직 연결이 적은 노드의 초기 열만 정하는 보조값이다.
  function linearPositions(data) {
    var nodes = data.nodes, byId = {}, reqAdj = {};
    nodes.forEach(function (n) { byId[n.id] = n; reqAdj[n.id] = []; });
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
    var base = comps.map(function (members) {
      return members.reduce(function (best, id) {
        var weight = Number(byId[id].weight);
        return Math.max(best, isFinite(weight) && weight > 0 ? weight - 1 : 0);
      }, 0);
    });
    var rank = base.slice();
    var queue = comps.map(function (_, i) { return i; }).filter(function (i) { return indeg[i] === 0; });
    queue.sort(function (a, b) { return base[a] - base[b]; });
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
    Object.keys(layers).forEach(function (rawRank) {
      var layer = layers[rawRank];
      layer.sort(function (a, b) {
        return (a.category || '').localeCompare(b.category || '') ||
          (Number(a.weight) || 0) - (Number(b.weight) || 0) || a.title.localeCompare(b.title);
      });
      layer.forEach(function (n, i) {
        positions[n.id] = { x: Number(rawRank) * 175, y: (i - (layer.length - 1) / 2) * 52 };
      });
    });
    return positions;
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
    });
    function radius(n) { return Math.sqrt(2.0 + (deg[n.id] || 0) * 0.7) * 2.95; }
    var labelTop = Math.max(6, Math.round(data.nodes.length * 0.04));
    var hubCandidates = data.classified
      ? data.nodes.filter(function (n) { return (deg[n.id] || 0) > 0; })
      : data.nodes.slice();
    var hubSet = new Set(hubCandidates
      .sort(function (a, b) { return (deg[b.id] || 0) - (deg[a.id] || 0); })
      .slice(0, labelTop).map(function (n) { return n.id; }));

    var hovered = null, selected = null, query = '';
    var activeFams = new Set(families.map(function (f) { return f.key; }));
    var hlNodes = new Set(), hlLinks = new Set();
    var hoverCb = null, clickCb = null;

    function passesFilter(n) {
      var mc = !famKeys.has(n.family) || activeFams.has(n.family);
      var ms = !query || n.title.toLowerCase().indexOf(query) >= 0;
      return mc && ms;
    }
    function nodeState(n) {
      if (!passesFilter(n)) return 'off';
      if (hlNodes.size && !hlNodes.has(n.id)) return 'off';
      return 'on';
    }
    function focusOn(node) {
      hlNodes = new Set(); hlLinks = new Set();
      if (node) {
        hlNodes.add(node.id);
        (outAdj[node.id] || new Set()).forEach(function (x) { hlNodes.add(x); });
        (inAdj[node.id] || new Set()).forEach(function (x) { hlNodes.add(x); });
        data.links.forEach(function (l) {
          var e = endpoints(l);
          if (e[0] === node.id || e[1] === node.id) hlLinks.add(lid(l));
        });
      }
    }
    function refocus() { focusOn(hovered || selected); }

    // DOM: canvas + toolbar(layout/fit/reset) + popup (검색/범례 없음)
    stage.innerHTML = '';
    var canvasWrap = document.createElement('div');
    canvasWrap.className = 'gc-canvas';
    stage.appendChild(canvasWrap);

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
    pop.innerHTML = '<div class="gc-pop-title"></div><a class="gc-pop-go" href="#"></a>';
    stage.appendChild(pop);
    var popTitle = pop.querySelector('.gc-pop-title');
    var popGo = pop.querySelector('.gc-pop-go');
    popGo.textContent = cfg.openLabel;
    popGo.addEventListener('click', function (e) { e.stopPropagation(); });

    function showPop(n) {
      popTitle.textContent = n.title;
      popGo.setAttribute('href', n.url || '#');
      pop.classList.add('show');
      placePop();
    }
    function hidePop() { pop.classList.remove('show'); }
    function placePop() {
      if (!selected || !pop.classList.contains('show')) return;
      var c = graph.graph2ScreenCoords(selected.x, selected.y);
      pop.style.left = c.x + 'px';
      pop.style.top = c.y + 'px';
    }

    function hslaFade(hue, a) { return 'hsla(' + hue + ',38%,55%,' + a + ')'; }
    function draw(node, ctx, scale) {
      var st = nodeState(node);
      var r = radius(node);
      var sel = selected && selected.id === node.id;
      ctx.save();
      if (st === 'off') {
        ctx.fillStyle = hslaFade(node.hue, 0.12);
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
          : 'rgba(' + cfg.label + ',' + (hubSet.has(node.id) ? 0.6 : 0.82) + ')';
        ctx.fillText(node.title, node.x, node.y + r + 2.5 / scale);
      }
    }
    function pointerArea(node, color, ctx) {
      ctx.fillStyle = color;
      ctx.beginPath(); ctx.arc(node.x, node.y, radius(node), 0, 6.2832); ctx.fill();
    }
    function linkColor(l) {
      if (hlLinks.has(lid(l))) {
        var e = endpoints(l);
        var focused = hovered || selected;
        if (focused) {
          if (e[0] === focused.id) return 'rgba(' + cfg.accentOut + ',0.9)';
          if (e[1] === focused.id) return 'rgba(' + cfg.accentIn + ',0.9)';
        }
        return 'rgba(' + cfg.accent + ',0.85)';
      }
      var e = endpoints(l);
      var on = passesFilter(byId[e[0]]) && passesFilter(byId[e[1]]) && !hlLinks.size;
      if (!on) return 'rgba(' + cfg.link + ',0.05)';
      if (l.relation === 'weak') return 'rgba(' + cfg.link + ',0.2)';
      if (l.relation === 'forward') return 'rgba(' + cfg.link + ',0.3)';
      if (l.relation === 'required') return 'rgba(' + cfg.link + ',0.44)';
      return 'rgba(' + cfg.link + ',0.36)';
    }
    function linkDash(l) {
      if (l.relation === 'weak') return [2, 5];
      if (l.relation === 'forward') return [9, 5];
      return [];
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
      .linkDirectionalArrowColor(function (l) { return linkColor(l); })
      .linkCurvature(function (l) {
        var e = endpoints(l);
        return data.links.some(function (r) {
          var re = endpoints(r);
          return re[0] === e[1] && re[1] === e[0];
        }) ? 0.25 : 0;
      })
      .onNodeHover(function (n) { hovered = n; refocus(); canvasWrap.style.cursor = n ? 'pointer' : ''; if (hoverCb) hoverCb(n ? n.id : null); })
      .onNodeClick(function (n) { selected = n; refocus(); showPop(n); if (clickCb) clickCb(n ? n.id : null); })
      .onBackgroundClick(function () { selected = null; hidePop(); refocus(); if (clickCb) clickCb(null); })
      .onRenderFramePost(placePop)
      .graphData(data);

    // 기존 graph 페이지는 force-graph의 기본 실선을 그대로 사용한다.
    if (data.classified && graph.linkLineDash) graph.linkLineDash(linkDash);

    graph.d3VelocityDecay(0.34);
    graph.cooldownTicks(220);
    if (graph.d3Force('charge')) graph.d3Force('charge').strength(-260); // 반발 ↑
    if (graph.d3Force('link')) graph.d3Force('link').distance(34);
    graph.d3Force('gravity', radial(0.18)); // 중심 중력 ↑
    if (graph.d3ReheatSimulation) graph.d3ReheatSimulation();

    var fitted = false;
    graph.onEngineStop(function () { if (!fitted) { graph.zoomToFit(0, 30); fitted = true; } });

    var layoutMode = 'force';
    function setLayout(mode, button) {
      if (mode === layoutMode) return;
      layoutMode = mode;
      if (mode === 'linear') {
        var positions = linearPositions(data);
        data.nodes.forEach(function (n) {
          n.__forceX = n.x; n.__forceY = n.y;
          n.fx = positions[n.id].x; n.fy = positions[n.id].y;
          n.x = n.fx; n.y = n.fy;
        });
        if (graph.enableNodeDrag) graph.enableNodeDrag(false);
        button.innerHTML = ICON.force;
        button.title = cfg.forceLabel;
        button.setAttribute('aria-pressed', 'true');
      } else {
        data.nodes.forEach(function (n) {
          delete n.fx; delete n.fy;
          if (isFinite(n.__forceX)) n.x = n.__forceX;
          if (isFinite(n.__forceY)) n.y = n.__forceY;
        });
        if (graph.enableNodeDrag) graph.enableNodeDrag(true);
        button.innerHTML = ICON.tree;
        button.title = cfg.linearLabel;
        button.setAttribute('aria-pressed', 'false');
        if (graph.d3ReheatSimulation) graph.d3ReheatSimulation();
      }
      hidePop();
      window.setTimeout(function () { graph.zoomToFit(450, 30); }, 40);
    }

    top.querySelectorAll('.gc-btn').forEach(function (b) {
      b.addEventListener('click', function () {
        if (b.dataset.act === 'layout') { setLayout(layoutMode === 'force' ? 'linear' : 'force', b); }
        else if (b.dataset.act === 'fit') { graph.zoomToFit(450, 30); }
        else if (cfg.onReset) { cfg.onReset(); graph.zoomToFit(450, 30); }
        else { graph.zoomToFit(450, 30); }
      });
    });

    function size() {
      var w = canvasWrap.clientWidth, h = canvasWrap.clientHeight;
      if (w && h) graph.width(w).height(h);
    }
    size();
    if (window.ResizeObserver) new ResizeObserver(size).observe(canvasWrap);

    return {
      graph: graph, deg: deg, byId: byId,
      refit: function () { graph.zoomToFit(450, 30); },
      focus: function (id) { hovered = id ? byId[id] : null; refocus(); },
      setQuery: function (q) { query = (q || '').toLowerCase().trim(); },
      setFamilies: function (arr) { activeFams = new Set(arr); },
      select: function (id) {
        var n = id ? byId[id] : null;
        selected = n; refocus();
        if (n) { showPop(n); graph.centerAt(n.x, n.y, 450); } else hidePop();
      },
      clear: function () { selected = null; hovered = null; query = ''; activeFams = new Set(families.map(function (f) { return f.key; })); hidePop(); refocus(); },
      onHover: function (cb) { hoverCb = cb; },
      onClick: function (cb) { clickCb = cb; }
    };
  }

  /* ---------- index panel ---------- */
  function buildIndex(panel, data, deg, byId, families, card, lang) {
    var t = lang === 'ko'
      ? { index: '색인', posts: '개 글', search: '글 검색…', connected: '연결 많은 글' }
      : { index: 'INDEX', posts: 'posts', search: 'Search posts…', connected: 'MOST CONNECTED' };
    var famByKey = {}; families.forEach(function (f) { famByKey[f.key] = f; });
    var rowIndex = {}; // id -> [row els]

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
    });

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
    if (!stage || !panel || typeof ForceGraph === 'undefined') return;
    var lang = stage.dataset.lang || 'ko';
    var source = stage.dataset.graphSource || 'graph';
    var layoutToggle = stage.dataset.layoutToggle === 'true';

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
        var idx = buildIndex(panel, data, card.deg, card.byId, fams, card, lang);
        cfg.onReset = function () { card.clear(); idx.reset(); };
      })
      .catch(function () {});
  }

  if (document.readyState !== 'loading') init();
  else document.addEventListener('DOMContentLoaded', init);
})();
