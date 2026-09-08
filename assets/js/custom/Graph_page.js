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
  function linearPositions(data, viewportWidth, viewportHeight) {
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
    var columnGap = 66, rowGap = 34, padX = 56, padY = 52;
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
        chunk.forEach(function (n, i) {
          positions[n.id] = {
            column: visualColumn,
            y: (i - (chunk.length - 1) / 2) * rowGap
          };
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
    return { positions: positions, width: width, height: viewportHeight };
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
    var hoverCb = null, clickCb = null, linearGeometry = null;
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
    function focusLinear(node) {
      hlNodes = new Set(); hlLinks = new Set();
      if (!node) return;
      hlNodes.add(node.id);

      // Only the chosen article may branch to optional context. Weak edges point
      // cited -> citing, while forward edges point citing -> later reading.
      (weakIn[node.id] || []).forEach(addHighlightedLink);
      (forwardOut[node.id] || []).forEach(addHighlightedLink);

      // Required edges point prerequisite -> dependent. Walk only upstream and
      // never expand weak/forward edges from prerequisites reached on this walk.
      var todo = [node.id], seen = new Set();
      while (todo.length) {
        var id = todo.pop();
        if (seen.has(id)) continue;
        seen.add(id);
        (requiredIn[id] || []).forEach(function (link) {
          var source = endpoints(link)[0];
          addHighlightedLink(link);
          if (!seen.has(source)) todo.push(source);
        });
      }
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
    function gitPath(link, index) {
      var e = endpoints(link);
      var source = linearGeometry.positions[e[0]], target = linearGeometry.positions[e[1]];
      if (!source || !target) return '';
      var sx = source.x, sy = source.y, tx = target.x, ty = target.y;
      var dx = tx - sx;
      if (Math.abs(dx) < 16) {
        var side = sx < linearGeometry.width / 2 ? 1 : -1;
        var laneX = sx + side * (20 + (index % 3) * 7);
        laneX = Math.max(16, Math.min(linearGeometry.width - 16, laneX));
        return 'M' + sx + ',' + sy + ' C' + laneX + ',' + sy + ' ' + laneX + ',' + ty + ' ' + tx + ',' + ty;
      }
      var direction = dx > 0 ? 1 : -1;
      sx += direction * radius(byId[e[0]]);
      tx -= direction * (radius(byId[e[1]]) + 3);
      dx = tx - sx;
      var stub = Math.min(18, Math.max(10, Math.abs(dx) / 3));
      var startX = sx + direction * stub;
      var endX = tx - direction * stub;
      var laneY = sy;
      if (link.relation === 'weak') laneY = Math.min(sy, ty) - 16 - (index % 3) * 5;
      else if (link.relation === 'forward') laneY = Math.max(sy, ty) + 16 + (index % 3) * 5;
      laneY = Math.max(18, Math.min(linearGeometry.height - 24, laneY));
      return 'M' + sx + ',' + sy +
        ' C' + startX + ',' + sy + ' ' + startX + ',' + laneY + ' ' + startX + ',' + laneY +
        ' L' + endX + ',' + laneY +
        ' C' + endX + ',' + laneY + ' ' + endX + ',' + ty + ' ' + tx + ',' + ty;
    }
    function updateLinearStyles() {
      if (!linearGeometry) return;
      linearLinkEls.forEach(function (entry) {
        var link = entry.link;
        entry.path.setAttribute('stroke', linkColor(link));
        entry.path.setAttribute('stroke-width', hlLinks.has(lid(link)) ? '2.4' :
          (link.relation === 'required' ? '1.2' : link.relation === 'weak' ? '0.85' : '1'));
      });
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

      var defs = svgElement('defs');
      var marker = svgElement('marker', {
        id: 'gc-linear-arrow', viewBox: '0 0 8 8', refX: '7', refY: '4',
        markerWidth: '7', markerHeight: '7', orient: 'auto', markerUnits: 'userSpaceOnUse'
      });
      marker.appendChild(svgElement('path', { d: 'M0,0 L8,4 L0,8 Z', fill: 'context-stroke' }));
      defs.appendChild(marker); linearSvg.appendChild(defs);

      var linksGroup = svgElement('g', { class: 'gc-linear__links' });
      data.links.forEach(function (link, index) {
        var path = svgElement('path', {
          d: gitPath(link, index), fill: 'none', 'stroke-linecap': 'round',
          'stroke-linejoin': 'round', 'vector-effect': 'non-scaling-stroke',
          'marker-end': 'url(#gc-linear-arrow)'
        });
        if (link.relation === 'weak') path.setAttribute('stroke-dasharray', '2 5');
        else if (link.relation === 'forward') path.setAttribute('stroke-dasharray', '9 5');
        linksGroup.appendChild(path); linearLinkEls.push({ link: link, path: path });
      });
      linearSvg.appendChild(linksGroup);

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
        if (focused) {
          if (highlightedEnds[0] === focused.id) return 'rgba(' + cfg.accentOut + ',0.9)';
          if (highlightedEnds[1] === focused.id) return 'rgba(' + cfg.accentIn + ',0.9)';
        }
        return 'rgba(' + cfg.accent + ',0.85)';
      }
      var e = endpoints(l);
      var on = passesFilter(byId[e[0]]) && passesFilter(byId[e[1]]) && !hlLinks.size;
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
      .linkDirectionalArrowColor(function (l) { return linkColor(l); })
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
        else if (b.dataset.act === 'fit') centerActive();
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
        var idx = buildIndex(panel, data, card.deg, card.byId, fams, card, lang);
        cfg.onReset = function () { card.clear(); idx.reset(); };
      })
      .catch(function () {});
  }

  if (document.readyState !== 'loading') init();
  else document.addEventListener('DOMContentLoaded', init);
})();
