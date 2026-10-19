/* Local_graph.js — 수학 글 우측 사이드바, 목차 아래의 로컬 의존성 그래프(항상 표시).
 *
 * 현재 글의 선수 글(required 를 두 단계 거슬러)과 후속 글(두 단계 따라 내려가)을 의존성
 * 페이지 선형 보기와 같은 레인 문법(Linear_layout.js)으로 그린다. 왼쪽이 선수 글, 오른쪽이
 * 후속 글이고, 현재 글에서 첫 부모를 거슬러 올라간 사슬과 현재 글 뒤로 이어지는 사슬이 0 번
 * 레인이다. weak·forward 는 현재 글에 바로 닿는 것만 넣는다. 현재 글은 상자 가로 한가운데에
 * 두고, 열 간격이 너무 좁아질 만큼 넓은 그래프는 양옆을 잘라 낸다. 사이드바 상자의 높이는
 * 보이는 레인에 맞춘다.
 *
 * 평상시에는 현재 글 제목만 떠 있고 나머지는 점과 선뿐이다. 점을 짚으면 그 글과 바로 이어진
 * 선과 글이 켜지고 라벨이 뜬다. 점 클릭 = 그 글로 이동. 빈 곳 클릭 또는 ⤢ 버튼 → 화면 중앙
 * 오버레이로 크게 보기. 사이드바는 라이트·다크 스킨을 따르므로 색은 local-graph.scss 의 변수로
 * 칠한다.
 */
(function () {
  'use strict';

  var SVG_NS = 'http://www.w3.org/2000/svg';
  function svgEl(name, attrs) {
    var el = document.createElementNS(SVG_NS, name);
    Object.keys(attrs || {}).forEach(function (key) { el.setAttribute(key, attrs[key]); });
    return el;
  }

  // linkPath 가 만든 d(M·L·C 만 쓴다)를 따라 6px 안팎 간격으로 지나는 점을 짚는다.
  function trace(d, visit) {
    var at = null;
    (d.match(/[MLC][^MLC]*/g) || []).forEach(function (part) {
      var n = part.slice(1).trim().split(/[\s,]+/).map(Number);
      if (part[0] === 'M') { at = { x: n[0], y: n[1] }; visit(at.x, at.y); return; }
      var end = part[0] === 'L' ? { x: n[0], y: n[1] } : { x: n[4], y: n[5] };
      var c1 = part[0] === 'L' ? at : { x: n[0], y: n[1] }, c2 = part[0] === 'L' ? end : { x: n[2], y: n[3] };
      var reach = Math.hypot(c1.x - at.x, c1.y - at.y) + Math.hypot(c2.x - c1.x, c2.y - c1.y) + Math.hypot(end.x - c2.x, end.y - c2.y);
      for (var i = 1, steps = Math.max(2, Math.ceil(reach / 6)); i <= steps; i++) {
        var s = i / steps, u = 1 - s;
        visit(u * u * u * at.x + 3 * u * u * s * c1.x + 3 * u * s * s * c2.x + s * s * s * end.x,
          u * u * u * at.y + 3 * u * u * s * c1.y + 3 * u * s * s * c2.y + s * s * s * end.y);
      }
      at = end;
    });
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

    // 회전하지 않은 글상자. boxesOverlap 이 꼭짓점으로 판정하므로 꼭짓점도 채운다.
    function rectBox(minX, maxX, minY, maxY) {
      return { minX: minX, maxX: maxX, minY: minY, maxY: maxY,
        corners: [{ x: minX, y: minY }, { x: maxX, y: minY }, { x: maxX, y: maxY }, { x: minX, y: maxY }] };
    }

    /* 상자 크기에 맞춘 좌표. 현재 글을 가로 한가운데 둔다. x 배율은 현재 글 양옆 중 먼 쪽이
       상자 반폭에 들어가게 정하되, 평균 열 간격이 minStep 보다 좁아지면 거기서 멈춘다. 열이
       적어 maxStep 보다 벌어질 때도 멈춘다. 사이드바는 넘치는 양옆을 잘라 내고, 오버레이는 전부
       그려서 스크롤하게 한다. k 는 선이 휘는 구간의 길이 배율이다.

       세로 레인 간격은 보이는 레인 수로 정한다. 점이 있는 레인과, 평상시 선이 길게 눕는
       레인(첫 부모 선은 도착 글의 레인, 나머지는 출발 글의 레인)이다. 간격은 정해 둔 값(사이드바
       14px, 오버레이 24px)에서 시작해 높이가 limit 를 넘으면 좁히되 9px·14px 밑으로는 줄이지
       않는다. 높이는 그려질 점·평상시 선·현재 글 제목(cap)에 맞춘다.

       오버레이의 SVG 는 그려질 것을 다 담고, 현재 글을 화면 가운데로 스크롤할 수 있을 만큼
       현재 글 양옆을 띄운다. */
    function place(W, limit, big, cap) {
      var spread = L.spreadColumns(model.order, model.column, model.columns, 0);
      var avg = model.columns > 1 ? spread.columnX[model.columns - 1] / (model.columns - 1) : 1;
      var padX = big ? 44 : 12, padY = big ? 32 : 10;
      var minStep = big ? 36 : 16, maxStep = big ? 90 : 30;
      var selfX = spread.x[self], side = 0;
      model.order.forEach(function (id) { side = Math.max(side, Math.abs(spread.x[id] - selfX)); });
      var sx = side > 0 ? (W / 2 - padX) / side : maxStep / avg;
      sx = Math.max(minStep / avg, Math.min(maxStep / avg, sx));
      // 사이드바는 상자 좌표, 오버레이는 현재 글을 x = 0 에 둔 좌표다.
      var cx = big ? 0 : W / 2, xs = {}, lo = 0, hi = 0;
      function seen(a, b) { return big || b >= 0 && a <= W; }
      model.order.forEach(function (id) {
        xs[id] = cx + (spread.x[id] - selfX) * sx;
        if (seen(xs[id], xs[id])) { lo = Math.min(lo, model.lane[id]); hi = Math.max(hi, model.lane[id]); }
      });
      var drawn = model.links.filter(function (l) { return model.drawn.has(L.lid(l)); });
      drawn.forEach(function (l) {
        var e = L.endpoints(l), flat = model.lane[model.firstParent[e[1]] === e[0] ? e[1] : e[0]];
        if (seen(xs[e[0]], xs[e[1]])) { lo = Math.min(lo, flat); hi = Math.max(hi, flat); }
      });
      var span = hi - lo, room = limit - 2 * padY - cap.lines * cap.lineHeight;
      var gap = span ? Math.max(big ? 14 : 9, Math.min(big ? 24 : 14, room / span)) : 0;

      // 현재 글을 y = 0 에 두고 그려질 점과 평상시 선이 지나는 자리를 모은다.
      var rel = {}, r = big ? 5.5 : 4.5, top = -r, bottom = r, left = -r, right = r, dots = [];
      function touch(x, y, pad) {
        if (!seen(x, x)) return;
        top = Math.min(top, y - pad);
        bottom = Math.max(bottom, y + pad);
        left = Math.min(left, x - pad);
        right = Math.max(right, x + pad);
      }
      model.order.forEach(function (id) {
        var p = rel[id] = { x: xs[id], y: model.lane[id] * gap };
        touch(p.x, p.y, r);
        if (id !== self) dots.push(rectBox(p.x - 3, p.x + 3, p.y - 3, p.y + 3));
      });
      drawn.forEach(function (l) {
        var e = L.endpoints(l);
        trace(L.linkPath(rel[e[0]], rel[e[1]], model.firstParent[e[1]] === e[0], Math.min(1, sx)),
          function (x, y) { touch(x, y, 1); });
      });

      /* 현재 글 제목 자리. 짚은 글의 라벨처럼 점 오른쪽·왼쪽에 가로로, 그다음 오른쪽 위·아래로
         비스듬히 놓아 보고, 마지막으로 점 바로 위·아래에 가로로 가운데 맞춰 놓아 본다. 사이드바
         상자 가로 안에 드는 자리 가운데 다른 점을 가장 적게 덮는 곳을 고르고, 같으면 앞의 자리다.
         선은 덮어도 된다. 여러 줄로 나뉜 제목은 가운데 맞춘 자리에만 들어간다. */
      function centered(p, below) {
        var ascent = cap.size * 0.8 + 1, descent = cap.size * 0.25 + 1, block = (cap.lines - 1) * cap.lineHeight;
        var first = below ? p.y + r + 3 + ascent : p.y - r - 3 - descent - block;
        var box = rectBox(p.x - cap.width / 2 - 1, p.x + cap.width / 2 + 1, first - ascent, first + block + descent);
        box.x = 0; box.y = first - p.y; box.angle = 0; box.centered = true;
        return box;
      }
      var label = null, fewest = Infinity;
      var spots = cap.lines > 1 ? [] : ['right', 'left', 'above', 'below'].map(function (spot) {
        return L.labelBox(rel[self], r, cap.width * 10.5 / (cap.size * 1.07), spot, cap.size, true);
      });
      spots.concat([centered(rel[self], false), centered(rel[self], true)]).forEach(function (box) {
        if (!big && (box.minX < 2 || box.maxX > W - 2)) return;
        var hits = dots.filter(function (dot) { return L.boxesOverlap(box, dot); }).length;
        if (hits < fewest) { label = box; fewest = hits; }
      });
      top = Math.min(top, label.minY);
      bottom = Math.max(bottom, label.maxY);
      left = Math.min(left, label.minX);
      right = Math.max(right, label.maxX);

      // 점은 x 배율이 이미 padX 안쪽에 두었으니, 넘침은 제목까지 담아 12px 여백으로만 잰다.
      var ox = big ? Math.max(12 - left, W / 2) : 0;
      var SW = big ? Math.ceil(ox + Math.max(right + 12, W / 2)) : W;
      var SH = Math.ceil(bottom - top + 2 * padY), cy = padY - top;
      var positions = {};
      model.order.forEach(function (id) { positions[id] = { x: ox + rel[id].x, y: cy + rel[id].y }; });
      label.minX += ox;
      label.maxX += ox;
      label.minY += cy;
      label.maxY += cy;
      label.corners.forEach(function (c) { c.x += ox; c.y += cy; });
      return { positions: positions, k: Math.min(1, sx), gap: gap, step: avg * sx, W: SW, H: SH, label: label };
    }

    function render(el, big) {
      el.innerHTML = '';
      // 오버레이 캔버스 높이의 상한. 카드가 화면 높이의 84% 를 넘지 않게 한다.
      var W = el.clientWidth, limit = big
        ? Math.floor(window.innerHeight * 0.84) - overlay.querySelector('.lg-overlay__head').offsetHeight - 2
        : 240;
      if (W < 40 || limit < 40) return;
      var svg = svgEl('svg', {
        class: 'lg-svg' + (big ? ' lg-svg--big' : ''), role: 'img', 'aria-label': t.title
      });
      el.appendChild(svg);

      /* 현재 글 제목은 늘 띄운다. 상자보다 길면 낱말 단위로 줄을 나누고, 한 낱말이 넘치면 글자를
         줄인다. 폭은 SVG 안에서 잰다. */
      var cap = { size: big ? 12 : 11 };
      var capEl = svgEl('text', { class: 'lg-label is-self is-main' });
      capEl.style.fontSize = cap.size + 'px';
      svg.appendChild(capEl);
      function measure(s) {
        capEl.textContent = s;
        try { return capEl.getComputedTextLength(); } catch (e) { return s.length * cap.size * 0.9; }
      }
      var maxWidth = W - 8, lines = [], line = '';
      model.byId[self].title.split(' ').forEach(function (word) {
        var next = line ? line + ' ' + word : word;
        if (line && measure(next) > maxWidth) { lines.push(line); line = word; } else line = next;
      });
      lines.push(line);
      cap.width = Math.max.apply(null, lines.map(measure));
      if (cap.width > maxWidth) {
        cap.size *= maxWidth / cap.width;
        cap.width = maxWidth;
        capEl.style.fontSize = cap.size + 'px';
      }
      cap.lines = lines.length;
      cap.lineHeight = cap.size * 1.2;

      var geo = place(W, limit, big, cap), view = W, H = geo.H;
      W = geo.W;
      svg.setAttribute('width', W);
      svg.setAttribute('height', H);
      svg.setAttribute('viewBox', '0 0 ' + W + ' ' + H);
      el.style.height = (big ? Math.min(H, limit) : H) + 'px';
      if (big) {
        // 가로 스크롤바가 자리를 차지하면 그만큼 캔버스를 늘린다.
        el.style.height = Math.min(H, limit) + el.offsetHeight - el.clientHeight + 'px';
        el.scrollLeft = geo.positions[self].x - view / 2;
        el.scrollTop = geo.positions[self].y - el.clientHeight / 2;
      }
      // 제목 자리의 x·y 는 점에서 본 글자 시작점이고, 가운데 맞춘 자리면 글줄의 가운데다.
      var at = geo.positions[self], capX = at.x + geo.label.x, capY = at.y + geo.label.y;
      capEl.textContent = '';
      capEl.setAttribute('text-anchor', geo.label.centered ? 'middle' : 'start');
      capEl.setAttribute('y', capY);
      if (geo.label.angle) capEl.setAttribute('transform', 'rotate(' + geo.label.angle + ' ' + capX + ' ' + capY + ')');
      lines.forEach(function (text, i) {
        var span = svgEl('tspan', { x: capX, dy: i ? cap.lineHeight : 0 });
        span.textContent = text;
        capEl.appendChild(span);
      });

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
        var label = id === self ? capEl : svgEl('text', { class: 'lg-label' });
        if (id !== self) label.textContent = n.title;
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
        var box = rectBox(left, left + text, p.y + y - size, p.y + y + 2);
        box.x = left - p.x; box.y = y; box.angle = 0; box.size = size;
        return box;
      }
      /* 라벨은 짚은 글이 먼저 자리를 잡고, 이어진 글은 연결 수 순으로 겹치지 않는 자리에만
         뜬다. 상자 밖으로 나가는 자리와 현재 글 제목 자리는 쓰지 않는다. 현재 글의 라벨은 늘
         떠 있는 제목이라 움직이지 않는다. */
      function placeLabels(focusId, neighbors) {
        Object.keys(nodeEls).forEach(function (id) { if (id !== self) nodeEls[id].label.style.display = 'none'; });
        if (!focusId) return;
        var rest = Array.from(neighbors).filter(function (id) { return id !== focusId; });
        rest.sort(function (a, b) {
          return (model.degree[b] || 0) - (model.degree[a] || 0) || (a < b ? -1 : 1);
        });
        var placed = [geo.label];
        [focusId].concat(rest).forEach(function (id) {
          if (id === self) return;
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
