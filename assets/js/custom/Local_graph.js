/* Local_graph.js — 우측 사이드바 목차 아래의 로컬 의존성 그래프(항상 표시).
 *
 * 현재 글의 2-hop 부분그래프(현재 글=가운데 금색, 직속 이웃=부각, 2-hop 바깥=흐림)를
 * 작은 캔버스에 그린다. 빈 곳 클릭 또는 ⤢ 버튼 → 화면 중앙 오버레이로 크게 보기.
 * 오버레이 헤더에 전체 그래프(/<lang>/graph/) 링크. 노드 클릭 = 그 글로 이동.
 *
 * force-graph 는 single 레이아웃이 수학 글에서만 로드한다.
 */
(function () {
  'use strict';

  function lend(x) { return typeof x === 'object' ? x.id : x; }
  function fade(c) {
    return c && c.indexOf('hsl(') === 0
      ? c.replace('hsl(', 'hsla(').replace(')', ',0.16)')
      : 'rgba(138,143,152,0.16)';
  }

  // (0,0) 중심으로 각 노드를 radiusFn(n) 반지름의 원으로 당기는 d3 force.
  function radial(radiusFn, strength) {
    var nodes;
    function force(alpha) {
      if (!nodes) return;
      for (var i = 0; i < nodes.length; i++) {
        var n = nodes[i], r = radiusFn(n);
        if (r == null) continue;
        var dx = n.x || 0, dy = n.y || 0;
        var dist = Math.sqrt(dx * dx + dy * dy) || 1e-6;
        var k = (r - dist) * strength * alpha / dist;
        n.vx += dx * k; n.vy += dy * k;
      }
    }
    force.initialize = function (_) { nodes = _; };
    return force;
  }

  function init() {
    var box = document.getElementById('localgraph-side');
    if (!box) return;
    var lang = box.dataset.lang || 'ko';
    var self = (box.dataset.self || location.pathname).replace(/\/$/, '');
    var t = lang === 'ko'
      ? { title: '이웃 그래프', expand: '크게 보기', full: '전체 그래프 →', none: '연결 정보가 없습니다.' }
      : { title: 'Local graph', expand: 'Expand', full: 'Full graph →', none: 'No links found.' };

    box.innerHTML =
      '<h4 class="nav__title"><span class="material-icons md-16">hub</span> ' + t.title +
      '<button class="lg-expand" type="button" title="' + t.expand + '" aria-label="' + t.expand + '">⤢</button></h4>' +
      '<div class="lg-canvas"></div>';
    var canvas = box.querySelector('.lg-canvas');
    var expandBtn = box.querySelector('.lg-expand');

    var overlay = document.createElement('div');
    overlay.className = 'lg-overlay';
    overlay.innerHTML =
      '<div class="lg-overlay__card"><div class="lg-overlay__head">' +
      '<span class="lg-overlay__title">' + t.title + '</span>' +
      '<a class="lg-overlay__full" href="/' + lang + '/graph/">' + t.full + '</a>' +
      '<button class="lg-overlay__close" type="button" aria-label="close">✕</button>' +
      '</div><div class="lg-overlay__canvas"></div></div>';
    document.body.appendChild(overlay);
    var ovCanvas = overlay.querySelector('.lg-overlay__canvas');

    var sub = null, smallGraph = null, ovGraph = null;

    function openOverlay() {
      if (!sub) return;
      overlay.classList.add('open');
      requestAnimationFrame(function () {
        if (!ovGraph) { ovGraph = renderInto(ovCanvas, true); }
        else {
          ovGraph.width(ovCanvas.clientWidth).height(ovCanvas.clientHeight);
          setTimeout(function () { ovGraph.zoomToFit(400, 24); }, 60);
        }
      });
    }
    function closeOverlay() { overlay.classList.remove('open'); }

    expandBtn.addEventListener('click', openOverlay);
    overlay.querySelector('.lg-overlay__close').addEventListener('click', closeOverlay);
    overlay.addEventListener('click', function (e) { if (e.target === overlay) closeOverlay(); });
    document.addEventListener('keydown', function (e) { if (e.key === 'Escape') closeOverlay(); });

    var tries = 0;
    (function ready() {
      if (typeof ForceGraph !== 'undefined') load();
      else if (tries++ < 50) setTimeout(ready, 100);
    })();

    function load() {
      fetch('/assets/data/graph-' + lang + '.json')
        .then(function (r) { return r.json(); })
        .then(compute)
        .catch(function () {});
    }

    function compute(data) {
      var nodes = {};
      data.nodes.forEach(function (n) { nodes[n.id] = n; });
      if (!nodes[self]) {
        canvas.innerHTML = '<p class="lg-empty">' + t.none + '</p>';
        expandBtn.style.display = 'none';
        return;
      }
      var adj = {};
      data.links.forEach(function (l) {
        var s = lend(l.source), tt = lend(l.target);
        (adj[s] = adj[s] || []).push(tt);
        (adj[tt] = adj[tt] || []).push(s);
      });
      var keep = {}; keep[self] = 0;
      var fr = [self];
      for (var h = 1; h <= 2; h++) {
        var nx = [];
        fr.forEach(function (id) {
          (adj[id] || []).forEach(function (nb) {
            if (!(nb in keep)) { keep[nb] = h; nx.push(nb); }
          });
        });
        fr = nx;
      }
      var inSub = {};
      var subNodes = Object.keys(keep).map(function (id) { inSub[id] = true; return nodes[id]; });
      var subLinks = data.links.filter(function (l) {
        return inSub[lend(l.source)] && inSub[lend(l.target)];
      });
      var direct = {};
      (adj[self] || []).forEach(function (x) { direct[x] = true; });
      var deg = {};
      subLinks.forEach(function (l) {
        var s = lend(l.source), tt = lend(l.target);
        deg[s] = (deg[s] || 0) + 1; deg[tt] = (deg[tt] || 0) + 1;
      });
      sub = { subNodes: subNodes, subLinks: subLinks, direct: direct, deg: deg, keep: keep };
      smallGraph = renderInto(canvas, false);
    }

    function renderInto(el, big) {
      var data = {
        nodes: sub.subNodes.map(function (n) { return Object.assign({}, n); }),
        links: sub.subLinks.map(function (l) { return { source: lend(l.source), target: lend(l.target) }; })
      };
      var deg = sub.deg, direct = sub.direct;
      var g = ForceGraph()(el)
        .graphData(data)
        .nodeId('id')
        .nodeRelSize(big ? 3.5 : 2.5)
        .nodeVal(function (n) { return n.id === self ? (big ? 11 : 7) : 1 + (deg[n.id] || 0) * 0.5; })
        .nodeColor(function (n) {
          if (n.id === self) return '#f0c674';
          if (direct[n.id]) return n.color || '#8a8f98';
          return fade(n.color);
        })
        .nodeLabel(function (n) { return n.title; })
        .linkColor(function (l) {
          var s = lend(l.source), t = lend(l.target);
          if (s === self) return 'rgba(107,58,0,0.9)';   // self cites someone (outward)
          if (t === self) return 'rgba(165,111,20,0.9)'; // someone cites self (inward)
          return 'rgba(130,132,142,0.3)';
        })
        .linkWidth(function (l) {
          return (lend(l.source) === self || lend(l.target) === self) ? 2 : 1;
        })
        .linkDirectionalArrowLength(5)
        .linkDirectionalArrowRelPos(0.96)
        .linkDirectionalArrowColor(function (l) {
          var s = lend(l.source), t = lend(l.target);
          if (s === self) return 'rgba(107,58,0,0.9)';
          if (t === self) return 'rgba(165,111,20,0.9)';
          return 'rgba(130,132,142,0.3)';
        })
        .linkCurvature(function (l) {
          var s = lend(l.source), t = lend(l.target);
          return (sub.subLinks || []).some(function (r) {
            return lend(r.source) === t && lend(r.target) === s;
          }) ? 0.25 : 0;
        })
        .nodeCanvasObjectMode(function () { return 'after'; })
        .nodeCanvasObject(function (n, ctx, scale) {
          var show = big || n.id === self || direct[n.id] || scale >= 2;
          if (!show) return;
          var fs = Math.max(3, (big ? 12 : 9) / scale);
          ctx.font = (n.id === self ? 'bold ' : '') + fs + 'px sans-serif';
          ctx.textAlign = 'center';
          ctx.textBaseline = 'top';
          ctx.fillStyle = n.id === self ? 'rgba(169,135,74,0.98)' : 'rgba(150,150,160,0.88)';
          ctx.fillText(n.title, n.x, n.y + (big ? 9 : 7) / scale);
        })
        .autoPauseRedraw(false)
        .onNodeClick(function (n) { if (n.url && n.id !== self) window.location.href = n.url; })
        .width(el.clientWidth)
        .height(el.clientHeight)
        .cooldownTicks(80)
        .onEngineStop(function () { g.zoomToFit(400, big ? 24 : 12); });

      if (!big) {
        // 소형: 정적 미니맵 — 빈 곳 클릭이면 크게 보기
        g.enableZoomInteraction(false).enablePanInteraction(false).enableNodeDrag(false)
          .onBackgroundClick(openOverlay);
      }
      // 동심원 레이아웃: hop 거리별 반지름의 원으로 당겨 전체가 원형이 되게.
      var RING = big ? 95 : 72;
      g.d3Force('radial', radial(function (n) { return (sub.keep[n.id] || 0) * RING; }, 0.92));
      if (g.d3Force('charge')) g.d3Force('charge').strength(-24); // 같은 고리 위 각도 분산용
      if (g.d3Force('link')) g.d3Force('link').distance(RING * 0.85).strength(0.12);
      if (g.d3ReheatSimulation) g.d3ReheatSimulation();
      return g;
    }

    window.addEventListener('resize', function () {
      if (smallGraph) smallGraph.width(canvas.clientWidth).height(canvas.clientHeight);
      if (ovGraph && overlay.classList.contains('open')) {
        ovGraph.width(ovCanvas.clientWidth).height(ovCanvas.clientHeight);
      }
    });
  }

  if (document.readyState !== 'loading') init();
  else document.addEventListener('DOMContentLoaded', init);
})();
