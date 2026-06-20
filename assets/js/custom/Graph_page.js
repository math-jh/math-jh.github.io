/* Graph_page.js — 전역 의존성 그래프(/ko/graph, /en/graph).
 * force-graph(2D canvas) + assets/data/graph-<lang>.json.
 * 노드=글(색=카테고리 hue, 크기=연결수), 엣지=교차참조.
 * 호버=이웃 강조, 클릭=이웃 강조 고정 + "글로 이동" 버튼(버튼 눌러야 이동).
 */
(function () {
  'use strict';

  function endpoints(l) {
    return [
      typeof l.source === 'object' ? l.source.id : l.source,
      typeof l.target === 'object' ? l.target.id : l.target
    ];
  }
  function lid(l) { var e = endpoints(l); return e[0] + '>' + e[1]; }
  function fade(c) {
    if (!c) return 'rgba(138,143,152,0.08)';
    return c.indexOf('hsl(') === 0
      ? c.replace('hsl(', 'hsla(').replace(')', ',0.08)')
      : 'rgba(138,143,152,0.08)';
  }

  function init() {
    var el = document.getElementById('xgraph');
    if (!el || typeof ForceGraph === 'undefined') return;
    var lang = el.dataset.lang || 'ko';

    var pop = document.getElementById('xgraph-pop');
    var popTitle = pop && pop.querySelector('.xpop-title');
    var popGo = pop && pop.querySelector('.xpop-go');

    var graph = null, data = null, deg = {}, adj = {};
    var hovered = null, selected = null;
    var hlNodes = new Set(), hlLinks = new Set();

    function maps(d) {
      deg = {}; adj = {};
      d.links.forEach(function (l) {
        var e = endpoints(l);
        deg[e[0]] = (deg[e[0]] || 0) + 1;
        deg[e[1]] = (deg[e[1]] || 0) + 1;
        (adj[e[0]] = adj[e[0]] || new Set()).add(e[1]);
        (adj[e[1]] = adj[e[1]] || new Set()).add(e[0]);
      });
    }

    function focusOn(node) {
      hlNodes = new Set(); hlLinks = new Set();
      if (node && data) {
        hlNodes.add(node.id);
        (adj[node.id] || new Set()).forEach(function (x) { hlNodes.add(x); });
        data.links.forEach(function (l) {
          var e = endpoints(l);
          if (e[0] === node.id || e[1] === node.id) hlLinks.add(lid(l));
        });
      }
    }
    function refocus() { focusOn(hovered || selected); }

    function showPop(node) {
      if (!pop) return;
      popTitle.textContent = node.title;
      popGo.setAttribute('href', node.url || '#');
      pop.classList.add('show');
      placePop();
    }
    function hidePop() { if (pop) pop.classList.remove('show'); }
    function placePop() {
      if (!pop || !selected || !pop.classList.contains('show')) return;
      var c = graph.graph2ScreenCoords(selected.x, selected.y);
      var r = el.getBoundingClientRect();
      pop.style.left = (r.left + c.x) + 'px';
      pop.style.top = (r.top + c.y) + 'px';
    }

    function drawLabel(node, ctx, scale) {
      var focused = hlNodes.size > 0 && hlNodes.has(node.id);
      if (scale < 1.5 && !focused) return;
      var fs = Math.max(3, 11 / scale);
      ctx.font = fs + 'px sans-serif';
      ctx.textAlign = 'center';
      ctx.textBaseline = 'top';
      ctx.fillStyle = focused ? 'rgba(169,135,74,0.97)' : 'rgba(150,150,160,0.8)';
      var rad = Math.sqrt(2 + (deg[node.id] || 0) * 0.9) * 5;
      ctx.fillText(node.title, node.x, node.y + rad / scale + 1);
    }

    function render(d) {
      data = d; maps(d);
      graph = ForceGraph()(el)
        .nodeId('id')
        .nodeRelSize(5)
        .nodeVal(function (n) { return 2 + (deg[n.id] || 0) * 0.9; })
        .nodeLabel(function () { return ''; }) // 라벨은 캔버스에 직접
        .nodeColor(function (n) {
          if (hlNodes.size && !hlNodes.has(n.id)) return fade(n.color);
          if (selected && n.id === selected.id) return '#f0c674';
          return n.color || '#8a8f98';
        })
        .linkColor(function (l) {
          return hlLinks.has(lid(l)) ? 'rgba(169,135,74,0.9)' : 'rgba(130,132,142,0.4)';
        })
        .linkWidth(function (l) { return hlLinks.has(lid(l)) ? 2.5 : 1; })
        .nodeCanvasObjectMode(function () { return 'after'; })
        .nodeCanvasObject(drawLabel)
        .onNodeHover(function (n) { hovered = n; refocus(); el.style.cursor = n ? 'pointer' : ''; })
        .onNodeClick(function (n) { selected = n; refocus(); showPop(n); })
        .onBackgroundClick(function () { selected = null; hidePop(); refocus(); })
        .onRenderFramePost(function () { placePop(); })
        .graphData(d);
      graph.d3VelocityDecay(0.3);
      if (graph.d3Force('charge')) graph.d3Force('charge').strength(-90);
    }

    fetch('/assets/data/graph-' + lang + '.json')
      .then(function (r) { return r.json(); })
      .then(render)
      .catch(function () {});

    if (popGo) popGo.addEventListener('click', function (e) { e.stopPropagation(); });
    window.addEventListener('resize', function () {
      if (graph) graph.width(el.clientWidth).height(el.clientHeight);
    });
  }

  if (document.readyState !== 'loading') init();
  else document.addEventListener('DOMContentLoaded', init);
})();
