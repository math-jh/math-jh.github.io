/* Local_graph.js — 수학 글 우측 사이드바, 목차 아래의 로컬 의존성 그래프(항상 표시).
 *
 * 현재 글의 선수 글(required 를 두 단계 거슬러)과 후속 글(두 단계 따라 내려가)을 의존성
 * 페이지 선형 보기와 같은 레인 문법(Linear_layout.js)으로 그린다. 왼쪽이 선수 글, 오른쪽이
 * 후속 글이고, 현재 글에서 첫 부모를 거슬러 올라간 사슬과 현재 글 뒤로 이어지는 사슬이 0 번
 * 레인이다. weak·forward 는 현재 글에 바로 닿는 것만 넣는다. 현재 글은 상자 한가운데에 두고,
 * 열 간격이 너무 좁아질 만큼 넓은 그래프는 양옆을 잘라 낸다.
 *
 * 평상시에는 라벨 없이 점과 선만 보인다. 점을 짚으면 그 글과 바로 이어진 선과 글이 켜지고
 * 라벨이 뜬다. 점 클릭 = 그 글로 이동. 빈 곳 클릭 또는 ⤢ 버튼 → 화면 중앙 오버레이로 크게
 * 보기. 사이드바는 라이트·다크 스킨을 따르므로 색은 local-graph.scss 의 변수로 칠한다.
 */
(function () {
  'use strict';

  var SVG_NS = 'http://www.w3.org/2000/svg';
  function svgEl(name, attrs) {
    var el = document.createElementNS(SVG_NS, name);
    Object.keys(attrs || {}).forEach(function (key) { el.setAttribute(key, attrs[key]); });
    return el;
  }

  /* 현재 글 둘레의 부분그래프와 그 열·레인. 첫 부모 고르기(깊이·연결 수)는 전역 그래프
     기준이라, 첫 부모가 부분그래프 안에 있으면 의존성 페이지와 같은 선을 고른다. */
  function localModel(data, self) {
    var L = window.LinearLayout;
    var byId = {};
    data.nodes.forEach(function (n) { byId[n.id] = n; });
    if (!byId[self]) return null;
    var reqIn = {}, reqOut = {};
    data.links.forEach(function (l) {
      if (l.relation !== 'required') return;
      var e = L.endpoints(l);
      (reqOut[e[0]] = reqOut[e[0]] || []).push(e[1]);
      (reqIn[e[1]] = reqIn[e[1]] || []).push(e[0]);
    });
    // 현재 글에서 몇 단계 떨어졌는가. 선수 쪽과 후속 쪽을 따로 센다.
    var hops = {};
    function walk(adj) {
      var found = new Set(), frontier = [self];
      for (var hop = 1; hop <= 2; hop++) {
        var next = [];
        frontier.forEach(function (id) {
          (adj[id] || []).forEach(function (x) {
            if (x !== self && !found.has(x)) { found.add(x); hops[x] = hops[x] || hop; next.push(x); }
          });
        });
        frontier = next;
      }
      return found;
    }
    var up = walk(reqIn), down = walk(reqOut);
    // 모든 관계의 선은 앞에 읽을 글에서 뒤에 읽을 글로 간다. 현재 글로 들어오는 weak·forward 의
    // 출발 글은 선수 쪽, 현재 글에서 나가는 쪽의 도착 글은 후속 쪽이다.
    data.links.forEach(function (l) {
      if (l.relation === 'required') return;
      var e = L.endpoints(l);
      if (e[1] === self && !down.has(e[0])) { up.add(e[0]); hops[e[0]] = 1; }
      else if (e[0] === self && !up.has(e[1])) { down.add(e[1]); hops[e[1]] = 1; }
    });
    down.forEach(function (id) { if (up.has(id)) down.delete(id); });
    var keep = new Set([self]);
    up.forEach(function (id) { keep.add(id); });
    down.forEach(function (id) { keep.add(id); });
    if (keep.size < 2) return null;
    var links = data.links.filter(function (l) {
      var e = L.endpoints(l);
      return keep.has(e[0]) && keep.has(e[1]);
    });

    /* 열: 현재 글이 0 이다. 선수 글은 현재 글까지 가는 가장 긴 사슬만큼 왼쪽에, 후속 글은
       현재 글에서 오는 가장 긴 사슬만큼 오른쪽에 둔다. 사슬은 전역 읽는 순서를 따라가는 선만
       잇는다. 같은 열에 묶인 순환 안에서는 현재 글에서 먼 글을 앞으로 친다. 사이드바가 좁아서
       전역 열을 그대로 쓰면 열이 수십 개로 벌어진다. */
    var global = L.readingColumns(data);
    var ranks = L.readingParents(data, global.column);
    var layer = {};
    layer[self] = 0;
    function settle(side, outward) {
      var ids = Array.from(side).sort(function (a, b) {
        return global.column[a] - global.column[b] ||
          (outward ? hops[b] - hops[a] : hops[a] - hops[b]) || (a < b ? -1 : a > b ? 1 : 0);
      });
      var at = {};
      ids.forEach(function (id, i) { at[id] = i; });
      if (outward) ids.reverse();
      ids.forEach(function (id) {
        var best = null;
        links.forEach(function (l) {
          var e = L.endpoints(l), other = outward ? e[1] : e[0];
          if ((outward ? e[0] : e[1]) !== id) return;
          if (other !== self && !(side.has(other) && (outward ? at[other] > at[id] : at[other] < at[id]))) return;
          var x = layer[other] + (outward ? -1 : 1);
          if (best === null || (outward ? x < best : x > best)) best = x;
        });
        layer[id] = best === null ? (outward ? -1 : 1) : best;
      });
    }
    settle(up, true);
    settle(down, false);
    var ids = Array.from(keep);
    var used = Array.from(new Set(ids.map(function (id) { return layer[id]; })))
      .sort(function (a, b) { return a - b; });
    var column = {};
    ids.forEach(function (id) { column[id] = used.indexOf(layer[id]); });
    var order = L.columnOrder(ids, column);
    var parents = {};
    order.forEach(function (id) {
      parents[id] = ranks.parents[id].filter(function (p) { return keep.has(p) && column[p] < column[id]; });
    });
    var lanes = L.lanes(order, parents, ranks.depth, ranks.degree, column, self);
    var firstParent = lanes.firstParent, lane = lanes.lane;

    /* 평상시에 그리는 선: 첫 부모 선, 현재 글에 닿는 선 전부, 그리고 이 둘만으로는 현재 글
       쪽으로 이어지는 선이 없는 글마다 다리 하나 — 선수 글이면 오른쪽의 선수 글(또는 현재 글)로
       가는 선, 후속 글이면 왼쪽의 후속 글(또는 현재 글)에서 오는 선이다. required 를 먼저 고르고,
       그다음 가까운 열, 가까운 레인 순이다. 그래서 어느 점에서든 그려진 선만 따라 현재 글까지
       간다. 현재 글과 서로 요구하는 순환의 되돌아가는 선은 왼쪽으로 가므로 짚을 때만 보인다. */
    var drawn = new Set();
    links.forEach(function (l) {
      var e = L.endpoints(l);
      if (column[e[1]] <= column[e[0]]) return;
      if (e[0] === self || e[1] === self || firstParent[e[1]] === e[0]) drawn.add(L.lid(l));
    });
    function bridge(id, side, outward) {
      function far(l) { var e = L.endpoints(l); return outward ? e[1] : e[0]; }
      var candidates = links.filter(function (l) {
        var e = L.endpoints(l), x = far(l);
        if ((outward ? e[0] : e[1]) !== id || x !== self && !side.has(x)) return false;
        return outward ? column[x] > column[id] : column[x] < column[id];
      });
      if (!candidates.length || candidates.some(function (l) { return drawn.has(L.lid(l)); })) return;
      function rank(l) {
        var x = far(l);
        return [l.relation === 'required' ? 0 : 1, Math.abs(column[x] - column[id]), Math.abs(lane[x] - lane[id])];
      }
      candidates.sort(function (a, b) {
        var ra = rank(a), rb = rank(b);
        return ra[0] - rb[0] || ra[1] - rb[1] || ra[2] - rb[2] || L.lid(a).localeCompare(L.lid(b));
      });
      drawn.add(L.lid(candidates[0]));
    }
    up.forEach(function (id) { bridge(id, up, true); });
    down.forEach(function (id) { bridge(id, down, false); });

    return {
      self: self, byId: byId, order: order, links: links, drawn: drawn,
      column: column, columns: used.length, lane: lane, firstParent: firstParent,
      degree: ranks.degree
    };
  }

  function init() {
    var box = document.getElementById('localgraph-side');
    if (!box || !window.LinearLayout) return;
    var L = window.LinearLayout;
    var lang = box.dataset.lang || 'ko';
    var self = (box.dataset.self || location.pathname).replace(/\/$/, '');
    var t = lang === 'ko'
      ? { title: '의존성', expand: '크게 보기', full: '전체 그래프', none: '연결 정보가 없습니다.' }
      : { title: 'Dependencies', expand: 'Expand', full: 'Full graph', none: 'No links found.' };

    box.innerHTML =
      '<h4 class="nav__title"><span class="material-icons md-16">graph_8</span> ' + t.title +
      '<button class="lg-expand" type="button" title="' + t.expand + '" aria-label="' + t.expand + '"><span class="material-icons md-16">zoom_out_map</span></button></h4>' +
      '<div class="lg-canvas"></div>';
    var canvas = box.querySelector('.lg-canvas');
    var expandBtn = box.querySelector('.lg-expand');

    var overlay = document.createElement('div');
    overlay.className = 'lg-overlay';
    // 전체 그래프 링크는 헤더 안, 제목 바로 옆.
    overlay.innerHTML =
      '<div class="lg-overlay__card"><div class="lg-overlay__head">' +
      '<span class="lg-overlay__title">' + t.title + '</span>' +
      '<a class="lg-overlay__full" href="/' + lang + '/dependencies" title="' + t.full + '" aria-label="' + t.full + '">' + t.full + '<span class="material-icons md-14">graph_3</span></a>' +
      '<button class="lg-overlay__close" type="button" aria-label="close">✕</button>' +
      '</div><div class="lg-overlay__canvas"></div></div>';
    document.body.appendChild(overlay);
    var ovCanvas = overlay.querySelector('.lg-overlay__canvas');

    var model = null;

    function openOverlay() {
      if (!model) return;
      overlay.classList.add('open');
      requestAnimationFrame(function () { render(ovCanvas, true); });
    }
    function closeOverlay() { overlay.classList.remove('open'); }

    expandBtn.addEventListener('click', openOverlay);
    overlay.querySelector('.lg-overlay__close').addEventListener('click', closeOverlay);
    overlay.addEventListener('click', function (e) { if (e.target === overlay) closeOverlay(); });
    document.addEventListener('keydown', function (e) { if (e.key === 'Escape') closeOverlay(); });

    fetch('/assets/data/dependencies-' + lang + '.json')
      .then(function (r) { return r.json(); })
      .then(function (data) {
        model = localModel(data, self);
        if (!model) {
          canvas.innerHTML = '<p class="lg-empty">' + t.none + '</p>';
          expandBtn.style.display = 'none';
          return;
        }
        render(canvas, false);
      })
      .catch(function () {});

    /* 상자 크기에 맞춘 좌표. 현재 글을 상자 한가운데 둔다. x 배율은 현재 글 양옆 중 먼 쪽이
       상자 반폭에 들어가게 정하되, 평균 열 간격이 minStep 보다 좁아지면 거기서 멈추고 바깥은
       잘라 낸다. 열이 적어 maxStep 보다 벌어질 때도 멈춘다. y 는 상자 안에 보이는 글들의 레인이
       반높이에 들어가게 정한다. k 는 선이 휘는 구간의 길이 배율이다. */
    function place(W, H, big) {
      var spread = L.spreadColumns(model.order, model.column, model.columns, 0);
      var avg = model.columns > 1 ? spread.columnX[model.columns - 1] / (model.columns - 1) : 1;
      var padX = big ? 44 : 12, padY = big ? 32 : 14;
      var minStep = big ? 36 : 16, maxStep = big ? 90 : 30;
      var selfX = spread.x[self], side = 0;
      model.order.forEach(function (id) { side = Math.max(side, Math.abs(spread.x[id] - selfX)); });
      var sx = side > 0 ? (W / 2 - padX) / side : maxStep / avg;
      sx = Math.max(minStep / avg, Math.min(maxStep / avg, sx));
      var cx = W / 2, cy = H / 2, xs = {}, reach = 0;
      model.order.forEach(function (id) {
        xs[id] = cx + (spread.x[id] - selfX) * sx;
        if (xs[id] >= 0 && xs[id] <= W) reach = Math.max(reach, Math.abs(model.lane[id]));
      });
      var gap = reach ? Math.min(big ? 24 : 14, (H / 2 - padY) / reach) : 0;
      var positions = {};
      model.order.forEach(function (id) {
        positions[id] = { x: xs[id], y: cy + model.lane[id] * gap };
      });
      return { positions: positions, k: Math.min(1, sx), gap: gap, step: avg * sx };
    }

    function render(el, big) {
      var W = el.clientWidth, H = el.clientHeight;
      if (W < 40 || H < 40) return;
      var geo = place(W, H, big);
      el.innerHTML = '';
      var svg = svgEl('svg', {
        class: 'lg-svg' + (big ? ' lg-svg--big' : ''), width: W, height: H,
        viewBox: '0 0 ' + W + ' ' + H, role: 'img', 'aria-label': t.title
      });
      el.appendChild(svg);

      // 레인이나 열이 촘촘하면 이웃 점과 겹치지 않게 줄인다.
      var room = Math.min(geo.gap ? geo.gap * 0.42 : Infinity, geo.step ? geo.step * 0.45 : Infinity);
      function radius(id) {
        if (id === self) return big ? 5.5 : 4.5;
        var d = Math.sqrt(model.degree[id] || 0);
        var r = big ? Math.min(4.4, 2.2 + 0.32 * d) : Math.min(3.6, 1.8 + 0.28 * d);
        return Math.min(r, Math.max(1.4, room));
      }
      // 글의 색상(hue)만 넘기고 밝기는 스킨이 정한다.
      function tone(target, n) {
        target.style.setProperty('--h', n.hue);
        if (n.family === 'misc') target.style.setProperty('--s', '0%');
      }

      // 방향은 왼쪽→오른쪽 읽는 순서가 말해 주므로 화살촉은 두지 않는다.
      var linksGroup = svgEl('g', { class: 'lg-links' });
      var linkEls = model.links.map(function (link, index) {
        var e = L.endpoints(link);
        var path = svgEl('path', {
          class: 'lg-link',
          d: L.linkPath(geo.positions[e[0]], geo.positions[e[1]], model.firstParent[e[1]] === e[0], geo.k)
        });
        if (link.relation === 'weak') path.setAttribute('stroke-dasharray', '2 5');
        else if (link.relation === 'forward') path.setAttribute('stroke-dasharray', '9 5');
        tone(path, model.byId[e[1]]);
        linksGroup.appendChild(path);
        return { link: link, path: path, order: index, ends: e, drawn: model.drawn.has(L.lid(link)) };
      });
      svg.appendChild(linksGroup);

      var nodesGroup = svgEl('g', { class: 'lg-nodes' });
      // 라벨은 점들 위의 따로 된 층이다. 점 묶음 안에 두면 뒤에 그려지는 점이 라벨을 가린다.
      var labelsGroup = svgEl('g', { class: 'lg-labels', 'aria-hidden': 'true' });
      var hitRadius = big ? Math.max(6, Math.min(11, geo.gap * 0.55 || 11)) : Math.max(5, Math.min(9, geo.gap * 0.55 || 9));
      var nodeEls = {};
      // 현재 글의 점은 맨 위에 그린다.
      model.order.filter(function (id) { return id !== self; }).concat([self]).forEach(function (id) {
        var n = model.byId[id], p = geo.positions[id];
        var group = svgEl('g', {
          class: 'lg-node' + (id === self ? ' is-self' : ''),
          transform: 'translate(' + p.x + ' ' + p.y + ')'
        });
        tone(group, n);
        var title = svgEl('title'); title.textContent = n.title; group.appendChild(title);
        group.appendChild(svgEl('circle', { class: 'lg-hit', r: hitRadius }));
        group.appendChild(svgEl('circle', { class: 'lg-dot', r: radius(id) }));
        var label = svgEl('text', { class: 'lg-label' + (id === self ? ' is-self' : '') });
        label.textContent = n.title;
        labelsGroup.appendChild(label);
        group.addEventListener('mouseenter', function () { focus(id); });
        group.addEventListener('mouseleave', function () { focus(null); });
        group.addEventListener('click', function (event) {
          event.stopPropagation();
          if (n.url && id !== self) window.location.href = n.url;
        });
        nodesGroup.appendChild(group);
        nodeEls[id] = { group: group, label: label, width: 0 };
      });
      svg.appendChild(nodesGroup);
      svg.appendChild(labelsGroup);
      if (!big) svg.addEventListener('click', openOverlay);

      // 라벨 폭은 처음 띄울 때 잰다. 사이드바가 숨어 있으면 0 이 나오니 글자 수로 어림한다.
      function labelWidth(id) {
        var entry = nodeEls[id];
        if (!entry.width) {
          try { entry.width = entry.label.getComputedTextLength(); } catch (e) { /* 렌더 전 */ }
        }
        return entry.width || model.byId[id].title.length * 9.5;
      }

      function clampedBox(p, r, w) {
        var size = big ? 12 : 11;
        var text = w * size / 10.5 * 1.07;
        if (text > W - 4) { size = size * (W - 4) / text; text = W - 4; }
        var left = Math.max(2, Math.min(W - 2 - text, p.x - text / 2));
        var y = p.y - r - 5 < size + 2 ? r + size + 3 : -(r + 5);
        return { x: left - p.x, y: y, angle: 0, size: size,
          minX: left, maxX: left + text, minY: p.y + y - size, maxY: p.y + y + 2 };
      }
      /* 라벨은 짚은 글이 먼저 자리를 잡고, 이어진 글은 연결 수 순으로 겹치지 않는 자리에만
         뜬다. 상자 밖으로 나가는 자리는 쓰지 않는다. */
      function placeLabels(focusId, neighbors) {
        Object.keys(nodeEls).forEach(function (id) { nodeEls[id].label.style.display = 'none'; });
        if (!focusId) return;
        var rest = Array.from(neighbors).filter(function (id) { return id !== focusId; });
        rest.sort(function (a, b) {
          return (model.degree[b] || 0) - (model.degree[a] || 0) || (a < b ? -1 : 1);
        });
        var placed = [];
        [focusId].concat(rest).forEach(function (id) {
          var main = id === focusId;
          var size = big ? (main ? 12 : 10.5) : (main ? 11 : 9.5);
          var spots = main ? ['right', 'left', 'above', 'below'] : ['above', 'below', 'right', 'left'];
          var p = geo.positions[id], r = radius(id), w = labelWidth(id), box = null, fallback = null;
          for (var i = 0; i < spots.length && !box; i++) {
            var trial = L.labelBox(p, r, w, spots[i], size, main);
            if (trial.minX < 2 || trial.maxX > W - 2 || trial.minY < 2 || trial.maxY > H - 2) continue;
            if (!fallback) fallback = trial;
            if (!placed.some(function (other) { return L.boxesOverlap(trial, other); })) box = trial;
          }
          // 짚은 글의 라벨은 겹쳐도 띄운다. 어느 자리도 상자 안에 들지 않으면 점 위에 가로로
          // 놓되 상자 안으로 밀어 넣고, 그래도 넓으면 글자를 줄인다.
          if (!box && main) box = fallback || clampedBox(p, r, w);
          if (!box) return;
          if (box.size) size = box.size;
          placed.push(box);
          var label = nodeEls[id].label, x = p.x + box.x, y = p.y + box.y;
          label.style.display = '';
          label.style.fontSize = size + 'px';
          label.classList.toggle('is-main', main);
          label.setAttribute('x', x);
          label.setAttribute('y', y);
          if (box.angle) label.setAttribute('transform', 'rotate(' + box.angle + ' ' + x + ' ' + y + ')');
          else label.removeAttribute('transform');
        });
      }

      /* 짚은 글이 없으면 평상시 선(model.drawn)을 글의 색으로 그린다. 짚으면 그 글에 닿는 선이
         모두 같은 굵기의 brass 로 켜지고, 나머지 평상시 선과 점은 흐려진다. */
      function focus(id) {
        var hl = new Set(), lit = new Set();
        if (id) {
          lit.add(id);
          linkEls.forEach(function (entry) {
            if (entry.ends[0] !== id && entry.ends[1] !== id) return;
            hl.add(entry); lit.add(entry.ends[0]); lit.add(entry.ends[1]);
          });
        }
        linkEls.forEach(function (entry) {
          var cls = 'lg-link';
          if (hl.has(entry)) cls += ' is-hl';
          else if (entry.drawn) cls += id ? ' is-dim' : ' is-on';
          entry.path.setAttribute('class', cls);
        });
        // 약한 관계부터 앞에 두고, 켜진 선은 맨 위층에 올린다.
        linkEls.slice().sort(function (a, b) {
          return paintOrder(a, hl.has(a)) - paintOrder(b, hl.has(b)) || a.order - b.order;
        }).forEach(function (entry) { linksGroup.appendChild(entry.path); });
        Object.keys(nodeEls).forEach(function (key) {
          var group = nodeEls[key].group;
          group.classList.toggle('is-hl', !!id && lit.has(key));
          group.classList.toggle('is-off', !!id && !lit.has(key));
        });
        placeLabels(id, lit);
      }
      function paintOrder(entry, highlighted) {
        var relation = entry.link.relation;
        return (highlighted ? 3 : 0) + (relation === 'weak' ? 0 : relation === 'forward' ? 1 : 2);
      }
      focus(null);
    }

    var resizeQueued = false;
    window.addEventListener('resize', function () {
      if (!model || resizeQueued) return;
      resizeQueued = true;
      requestAnimationFrame(function () {
        resizeQueued = false;
        render(canvas, false);
        if (overlay.classList.contains('open')) render(ovCanvas, true);
      });
    });
  }

  if (document.readyState !== 'loading') init();
  else document.addEventListener('DOMContentLoaded', init);
})();
