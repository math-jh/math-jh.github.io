/* 블로그 대시보드 — 라우트별 렌더러.
   /dash/ 는 개요만, 상세는 /dash/<섹션> 으로 나눠 한 페이지에 다 붓지 않는다.
   서버가 어떤 섹션 경로에도 같은 index.html 을 주고, 여기서 pathname 으로 갈린다. */
'use strict';

var API = '/dash/api/';
var BASE = '/dash/';
var DRAFT_PAGE = 40;                 // 미발행 172편을 한 번에 그리면 표가 페이지를 삼킨다
var state = { data: null, draftLimit: DRAFT_PAGE };

var ROUTES = [
  { key: '', label: '개요' },
  { key: 'workers', label: '워커' },
  { key: 'drafts', label: '미발행' },
  { key: 'weights', label: 'weight' },
  { key: 'translation', label: '번역' },
  { key: 'audit', label: '감사·색인' },
  { key: 'activity', label: '활동' }
];

function route() {
  var p = location.pathname.replace(/^\/dash\/?/, '').replace(/\/$/, '');
  return ROUTES.some(function (r) { return r.key === p; }) ? p : '';
}

/* ── 유틸 ─────────────────────────────────────────────────────────────── */
function el(tag, cls, text) {
  var n = document.createElement(tag);
  if (cls) n.className = cls;
  if (text !== undefined && text !== null) n.textContent = String(text);
  return n;
}
function esc(s) {
  return String(s === undefined || s === null ? '' : s)
    .replace(/&/g, '&amp;').replace(/</g, '&lt;').replace(/>/g, '&gt;')
    .replace(/"/g, '&quot;');
}
function ago(ts) {
  if (!ts) return '—';
  return agoSec(Date.now() / 1000 - ts) + ' 전';
}
function agoSec(sec) {
  if (sec === null || sec === undefined) return '—';
  if (sec < 90) return Math.round(sec) + '초';
  if (sec < 5400) return Math.round(sec / 60) + '분';
  if (sec < 172800) return Math.round(sec / 3600) + '시간';
  return Math.round(sec / 86400) + '일';
}
function num(n) { return (n === null || n === undefined) ? '—' : n.toLocaleString('ko-KR'); }
function kchars(n) { return Math.round(n / 1000).toLocaleString('ko-KR') + 'k'; }
function shortCat(c) { return String(c).replace(/^Math\//, '').replace(/_/g, ' '); }

function section(title, hint) {
  var s = el('section');
  s.appendChild(el('h2', null, title));
  if (hint) s.appendChild(el('p', 'hint', hint));
  return s;
}
function table(headers, rows) {
  var wrap = el('div', 'tbl-scroll');
  var t = el('table');
  var thead = el('thead'), tr = el('tr');
  headers.forEach(function (h) {
    tr.appendChild(el('th', h.num ? 'num' : null, h.label !== undefined ? h.label : h));
  });
  thead.appendChild(tr); t.appendChild(thead);
  var tb = el('tbody');
  rows.forEach(function (r) { tb.appendChild(r); });
  t.appendChild(tb); wrap.appendChild(t);
  return wrap;
}
function row(cells, cls) {
  var tr = el('tr', cls);
  cells.forEach(function (c) {
    var td = el('td', c.cls || null);
    if (c.html !== undefined) td.innerHTML = c.html;
    else td.textContent = c.text === undefined ? '' : String(c.text);
    tr.appendChild(td);
  });
  return tr;
}
function h3(text) { return el('h3', null, text); }
function cols() { return el('div', 'cols'); }

/* ── 모달 ─────────────────────────────────────────────────────────────── */
function openModal(title, body) {
  document.getElementById('modal-title').textContent = title;
  document.getElementById('modal-body').textContent = body;
  document.getElementById('modal').hidden = false;
}
document.getElementById('modal-close').onclick = function () {
  document.getElementById('modal').hidden = true;
};
document.getElementById('modal').onclick = function (e) {
  if (e.target === this) this.hidden = true;
};
document.addEventListener('keydown', function (e) {
  if (e.key === 'Escape') document.getElementById('modal').hidden = true;
});

/* ── 테마 (블로그와 MTHEME 쿠키 공유) ─────────────────────────────────── */
function themeMode() {
  var m = (document.cookie.split('; ').find(function (c) { return c.indexOf('MTHEME=') === 0; }) || '').slice(7);
  return (m === 'light' || m === 'dark' || m === 'auto') ? m : 'auto';
}
function themeApply(m) {
  var dark = m === 'dark' || (m === 'auto' && window.matchMedia
    && window.matchMedia('(prefers-color-scheme: dark)').matches);
  document.documentElement.setAttribute('data-theme', dark ? 'dark' : 'light');
  document.getElementById('theme-btn').textContent = m;
}
document.getElementById('theme-btn').onclick = function () {
  var order = ['auto', 'light', 'dark'];
  var next = order[(order.indexOf(themeMode()) + 1) % 3];
  document.cookie = 'MTHEME=' + next + '; path=/; max-age=31536000; samesite=lax';
  themeApply(next);
};

/* ── 개요 ─────────────────────────────────────────────────────────────── */
function viewOverview(d) {
  var frag = document.createDocumentFragment();
  var s = d.stats, sys = d.system || {};
  var badWorkers = (d.workers || []).filter(function (w) {
    return w.status === 'stale' || w.status === 'missing' || w.err;
  });

  var tiles = [
    { n: num(s.published), l: '발행 (ko)', to: '' },
    { n: num(s.unpublished), l: '미발행 초안', accent: true, to: 'drafts' },
    { n: num(s.drift), l: '재번역 대기', to: 'translation' },
    { n: num(s.new30d), l: '최근 30일 신규' },
    { n: num(s.categories), l: '카테고리', to: 'weights' },
    { n: num(s.en), l: '영문 글', to: 'translation' },
    { n: kchars(s.chars), l: '총 분량 (자)' },
    { n: num(badWorkers.length), l: '워커 이상', bad: badWorkers.length > 0, to: 'workers' },
    { n: num((d.audit || {}).posts_with_issues), l: '링크 이슈 글', to: 'audit' },
    { n: num((d.gsc || {}).actionable), l: '미색인 (조치)', to: 'audit' },
    { n: num(sys.dirty_count), l: '커밋 안 된 변경', to: 'activity' },
    {
      n: sys.quota ? Math.round(sys.quota.weekly * 100) + '%' : '—',
      l: '주간 쿼터', bad: sys.quota && sys.quota.weekly >= 0.9
    }
  ];
  var sec = section('개요');
  var box = el('div', 'tiles');
  tiles.forEach(function (t) {
    var cls = 'tile' + (t.accent ? ' tile--accent' : '') + (t.bad ? ' tile--bad' : '');
    var n = t.to ? el('a', cls) : el('div', cls);
    if (t.to) n.href = BASE + t.to;
    n.appendChild(el('div', 'tile__n', t.n));
    n.appendChild(el('div', 'tile__l', t.l));
    box.appendChild(n);
  });
  sec.appendChild(box);
  frag.appendChild(sec);

  /* 지금 볼 것 — 임계값을 넘긴 항목만 모은다. 비어 있으면 그것도 정보다. */
  var alerts = [];
  badWorkers.forEach(function (w) {
    alerts.push({
      text: w.name + ' — ' + (w.status === 'ok' ? '로그에 오류' : '실행이 ' + agoSec(w.age) + ' 넘게 없음'),
      to: 'workers', level: 'bad'
    });
  });
  if (sys.mem && /hit_cap=[1-9]/.test(sys.mem)) {
    alerts.push({ text: 'Jekyll 메모리 cap 도달 이력 — ' + sys.mem.trim(), to: 'activity', level: 'warn' });
  }
  if (sys.jekyll !== 'active') {
    alerts.push({ text: 'Jekyll dev 서버가 ' + sys.jekyll, to: 'activity', level: 'bad' });
  }
  if (sys.quota && sys.quota.weekly >= 0.9) {
    alerts.push({ text: '주간 쿼터 ' + Math.round(sys.quota.weekly * 100) + '% — 워커가 스킵될 수 있다', to: 'activity', level: 'warn' });
  }
  if (s.missing_en) alerts.push({ text: '발행글 중 EN 없음 ' + s.missing_en + '건', to: 'audit', level: 'warn' });
  if (s.orphan_en) alerts.push({ text: '고아 EN(ko 없음) ' + s.orphan_en + '건', to: 'audit', level: 'warn' });
  if (sys.dirty_count) {
    alerts.push({ text: '커밋 안 된 변경 ' + sys.dirty_count + '건', to: 'activity', level: 'info' });
  }

  var asec = section('지금 볼 것');
  if (alerts.length) {
    var ul = el('ul', 'alerts');
    alerts.forEach(function (a) {
      var li = el('li', 'alerts__item alerts__item--' + a.level);
      var link = el('a', null, a.text);
      link.href = BASE + a.to;
      li.appendChild(link);
      ul.appendChild(li);
    });
    asec.appendChild(ul);
  } else {
    asec.appendChild(el('p', 'hint', '임계값을 넘긴 항목 없음.'));
  }
  frag.appendChild(asec);

  /* 워커 한 줄 요약 */
  var wsec = section('워커', '자세한 로그는 워커 페이지에서.');
  var strip = el('div', 'wstrip');
  (d.workers || []).forEach(function (w) {
    var a = el('a', 'wstrip__item');
    a.href = BASE + 'workers';
    a.title = w.schedule + ' · ' + agoSec(w.age) + ' 전';
    a.innerHTML = '<span class="dot dot--' + (w.err ? 'late' : w.status) + '"></span>' +
      esc(w.name) + ' <span class="muted">' + agoSec(w.age) + '</span>';
    strip.appendChild(a);
  });
  wsec.appendChild(strip);
  frag.appendChild(wsec);

  /* 최근 커밋 5건 */
  var gsec = section('최근 커밋');
  gsec.appendChild(table(['sha', '종류', '내용', { label: '시각', num: true }],
    (d.git || []).slice(0, 5).map(gitRow)));
  var more = el('p', 'hint');
  more.innerHTML = '<a href="' + BASE + 'activity">활동 전체 보기 →</a>';
  gsec.appendChild(more);
  frag.appendChild(gsec);

  return frag;
}

var KIND = { manual: '수동', auto: '자동', mechanical: '기계적', dev: '개발노트' };
function gitRow(c) {
  return row([
    { text: c.sha, cls: 'mono muted' },
    { text: KIND[c.kind] || c.kind, cls: 'muted' },
    { text: c.subject },
    { text: ago(c.ts), cls: 'num muted' }
  ]);
}

/* ── 워커 ─────────────────────────────────────────────────────────────── */
function viewWorkers(d) {
  var sec = section('워커', 'cron 주기 대비 로그가 늙으면 지연·정지로 표시된다. 행을 누르면 최근 로그가 열린다.');
  var rows = (d.workers || []).map(function (w) {
    var label = '<span class="dot dot--' + w.status + '"></span>' + esc(w.name) +
      (w.err ? '<span class="tag tag--err">로그 오류</span>' : '');
    var last = w.tail && w.tail.length ? w.tail[w.tail.length - 1] : '';
    var tr = row([
      { html: label },
      { text: w.schedule, cls: 'muted' },
      { text: agoSec(w.age), cls: 'num' },
      { html: '<span class="path">' + esc(last.slice(0, 150)) + '</span>' }
    ], w.has_log ? 'clickable' : null);
    if (w.has_log) {
      tr.onclick = function () {
        openModal(w.name + ' — 로그', '불러오는 중…');
        fetch(API + 'log?name=' + encodeURIComponent(w.key) + '&n=300')
          .then(function (r) { return r.json(); })
          .then(function (j) {
            openModal(w.name + ' — ' + j.path, (j.lines || []).join('\n') || '(빈 로그)');
          })
          .catch(function (e) { openModal(w.name, '로그를 읽지 못했다: ' + e); });
      };
    }
    return tr;
  });
  var box = el('div');
  box.id = 'workers-body';
  box.appendChild(table(['워커', '주기', { label: '경과', num: true }, '최근 로그'], rows));
  sec.appendChild(box);
  return sec;
}

/* ── 미발행 ───────────────────────────────────────────────────────────── */
function viewDrafts(d) {
  var sec = section('미발행 글');
  var bar = el('div', 'toolbar');
  bar.innerHTML =
    '<label>카테고리 <select id="draft-cat"></select></label>' +
    '<label>정렬 <select id="draft-sort">' +
      '<option value="mtime">최근 수정순</option>' +
      '<option value="category">카테고리·weight순</option>' +
      '<option value="chars">분량순</option>' +
      '<option value="date">date순</option>' +
    '</select></label>' +
    '<span id="draft-count" class="count"></span>';
  sec.appendChild(bar);
  var body = el('div');
  body.id = 'drafts-body';
  sec.appendChild(body);
  return sec;
}

function renderDrafts() {
  var d = state.data;
  var catSel = document.getElementById('draft-cat');
  if (!catSel) return;
  var cat = catSel.value;
  var sort = document.getElementById('draft-sort').value;
  var list = (d.unpublished || []).filter(function (p) { return !cat || p.category === cat; }).slice();
  if (sort === 'chars') list.sort(function (a, b) { return b.chars - a.chars; });
  else if (sort === 'date') list.sort(function (a, b) { return (b.date || '').localeCompare(a.date || ''); });
  else if (sort === 'category') {
    list.sort(function (a, b) {
      return a.category.localeCompare(b.category) || (a.weight || 0) - (b.weight || 0);
    });
  } else list.sort(function (a, b) { return b.mtime - a.mtime; });

  var shown = list.slice(0, state.draftLimit);
  var rows = shown.map(function (p) {
    // 미발행 글은 번역 대상이 아니라 EN 부재가 정상 — 태그로 표시하지 않는다
    var tags = p.drift ? '<span class="tag tag--drift">drift</span>' : '';
    var title = '<a href="' + esc(p.permalink) + '" target="_blank">' + esc(p.title) + '</a>' + tags +
      '<div class="path">' + esc(p.path) + '</div>';
    var tr = row([
      { html: title },
      { text: shortCat(p.category), cls: 'muted' },
      { text: p.weight === null ? '—' : p.weight, cls: 'num' },
      { text: kchars(p.chars), cls: 'num' },
      { text: ago(p.mtime), cls: 'num muted' },
      { html: '<button class="ghost-btn lint-btn">lint</button>' }
    ]);
    tr.querySelector('.lint-btn').onclick = function (e) {
      e.stopPropagation();
      openModal('lint — ' + p.title, '검사 중… (md_lint.py)');
      fetch(API + 'lint?path=' + encodeURIComponent(p.path))
        .then(function (r) { return r.json(); })
        .then(function (j) {
          var out = (j.out || '').trim() || (j.rc === 0 ? '지적 사항 없음.' : '');
          openModal('lint — ' + p.title, out + (j.err ? '\n\n[stderr]\n' + j.err : ''));
        })
        .catch(function (e2) { openModal('lint', '실행 실패: ' + e2); });
    };
    return tr;
  });

  document.getElementById('draft-count').textContent =
    list.length + '편' + (shown.length < list.length ? ' 중 ' + shown.length + '편 표시' : '');
  var box = document.getElementById('drafts-body');
  box.innerHTML = '';
  box.appendChild(table(
    ['글', '카테고리', { label: 'weight', num: true }, { label: '분량', num: true },
     { label: '수정', num: true }, ''], rows));
  if (shown.length < list.length) {
    var more = el('button', 'ghost-btn', '더 보기 (' + (list.length - shown.length) + '편 남음)');
    more.style.marginTop = '.6rem';
    more.onclick = function () { state.draftLimit += DRAFT_PAGE; renderDrafts(); };
    box.appendChild(more);
  }
}

function wireDrafts(d) {
  var sel = document.getElementById('draft-cat');
  if (!sel) return;
  var cats = {};
  (d.unpublished || []).forEach(function (p) { cats[p.category] = (cats[p.category] || 0) + 1; });
  var cur = sel.value;
  sel.innerHTML = '<option value="">전체</option>';
  Object.keys(cats).sort().forEach(function (c) {
    var o = el('option', null, shortCat(c) + ' (' + cats[c] + ')');
    o.value = c;
    sel.appendChild(o);
  });
  sel.value = cur;
  function reset() { state.draftLimit = DRAFT_PAGE; renderDrafts(); }
  sel.onchange = reset;
  document.getElementById('draft-sort').onchange = reset;
  renderDrafts();
}

/* ── weight 지도 ──────────────────────────────────────────────────────── */
function viewWeights(d) {
  var sec = section('weight 지도',
    '칸 하나가 글 하나다. 채워진 칸은 발행, 빈 칸은 미발행, 점선은 빈 슬롯. 브래스 밑줄은 재번역 대기.');
  var wrap = el('div', 'wmap');
  (d.categories || []).forEach(function (c) {
    var r = el('div', 'wmap__row');
    var name = el('div', 'wmap__name');
    name.innerHTML = esc(shortCat(c.name)) +
      ' <em>' + c.total + '편' + (c.unpublished ? ' · 미발행 ' + c.unpublished : '') + '</em>';
    r.appendChild(name);

    var cells = el('div', 'wmap__cells');
    // 실제 weight 를 순서대로 깔고, 빠진 정수 슬롯만 빈 칸으로 채운다.
    // 부록 계열(100·200·300번대)까지 1..max 로 채우면 빈 칸 수백 개가 생긴다 —
    // 간격이 4를 넘으면 생략 표시로 접는다.
    var placed = c.posts.filter(function (p) { return p.weight !== null; });
    placed.sort(function (a, b) { return a.weight - b.weight; });
    var prev = 0;
    placed.forEach(function (p) {
      var gap = Math.floor(p.weight) - Math.floor(prev) - 1;
      if (gap > 0 && gap <= 4) {
        for (var k = 1; k <= gap; k++) {
          var g = el('div', 'wcell wcell--gap', Math.floor(prev) + k);
          g.title = 'weight ' + (Math.floor(prev) + k) + ' — 빈 슬롯';
          cells.appendChild(g);
        }
      } else if (gap > 4) {
        var sep = el('div', 'wcell wcell--skip', '⋯');
        sep.title = '빈 슬롯 ' + gap + '개 생략';
        cells.appendChild(sep);
      }
      var cell = el('div',
        'wcell' + (p.published ? ' wcell--pub' : '') + (p.drift ? ' wcell--drift' : ''), p.weight);
      cell.title = 'w' + p.weight + ' · ' + p.title +
        (p.published ? '' : ' (미발행)') + (p.drift ? ' · drift' : '');
      cells.appendChild(cell);
      prev = p.weight;
    });
    c.posts.filter(function (p) { return p.weight === null; }).forEach(function (p) {
      var cell = el('div', 'wcell wcell--gap', '?');
      cell.title = 'weight 없음 · ' + p.title;
      cells.appendChild(cell);
    });
    r.appendChild(cells);
    wrap.appendChild(r);
  });
  sec.appendChild(wrap);
  return sec;
}

/* ── 번역 ─────────────────────────────────────────────────────────────── */
function viewTranslation(d) {
  var sec = section('번역 큐');
  var t = d.translation;
  if (!t) {
    sec.appendChild(el('p', 'hint', 'translation_state.json 을 읽지 못했다.'));
    return sec;
  }
  var c = cols();

  var left = el('div');
  left.appendChild(h3('상태 집계'));
  var rows = Object.keys(t.by_status).sort().map(function (k) {
    return row([{ text: k }, { text: num(t.by_status[k]), cls: 'num' }]);
  });
  rows.push(row([{ html: '<strong>재번역 대기 (drift_needed)</strong>' },
                 { text: num(d.stats.drift), cls: 'num' }]));
  left.appendChild(table(['status', { label: '건수', num: true }], rows));
  var st = t.stats || {};
  left.appendChild(el('p', 'hint', '누적 ' + num(st.total_done) + '편 · 입력 ' +
    kchars(st.total_in_chars || 0) + '자 → 출력 ' + kchars(st.total_out_chars || 0) + '자'));

  var right = el('div');
  right.appendChild(h3('최근 시도'));
  right.appendChild(table(['파일', '상태', { label: '시각', num: true }],
    (t.recent || []).map(function (r) {
      return row([
        { html: '<span class="path">' + esc(r.path.replace('_posts/', '')) + '</span>' },
        { text: r.status, cls: 'muted' },
        { text: ago(r.ts), cls: 'num muted' }
      ]);
    })));

  c.appendChild(left); c.appendChild(right);
  sec.appendChild(c);
  return sec;
}

/* ── 감사·색인 ────────────────────────────────────────────────────────── */
function viewAudit(d) {
  var frag = document.createDocumentFragment();

  var sec = section('감사');
  var c = cols();
  var left = el('div');
  left.appendChild(h3('링크·frontmatter 감사'));
  var a = d.audit;
  if (a) {
    left.appendChild(table(['종류', { label: '건수', num: true }],
      Object.keys(a.counts).sort().map(function (k) {
        return row([{ text: k, cls: 'mono' }, { text: num(a.counts[k]), cls: 'num' }]);
      })));
    left.appendChild(el('p', 'hint', a.scanned + '편 검사 · 이슈 있는 글 ' +
      a.posts_with_issues + '편 · ' + ago(a.mtime) + ' 갱신 (주간 cron)'));
  } else {
    left.appendChild(el('p', 'hint', 'audit-report.md 없음'));
  }

  var right = el('div');
  right.appendChild(h3('번역 짝 맞춤'));
  right.appendChild(table(['항목', { label: '건수', num: true }], [
    row([{ text: '발행글 중 EN 없음' }, { text: num(d.stats.missing_en), cls: 'num' }]),
    row([{ text: '고아 EN (ko 없음)' }, { text: num(d.stats.orphan_en), cls: 'num' }])
  ]));
  if ((d.orphan_en || []).length) {
    right.appendChild(el('pre', 'log', d.orphan_en.map(function (o) { return o.path; }).join('\n')));
  }
  c.appendChild(left); c.appendChild(right);
  sec.appendChild(c);
  frag.appendChild(sec);

  var g = d.gsc;
  var isec = section('색인');
  if (!g) {
    isec.appendChild(el('p', 'hint', 'index-monitor 상태 파일 없음'));
    frag.appendChild(isec);
    return frag;
  }
  var c2 = cols();
  var l2 = el('div');
  l2.appendChild(h3('coverage 분포'));
  l2.appendChild(table(['상태', { label: 'URL', num: true }],
    Object.keys(g.by_coverage).sort(function (x, y) {
      return g.by_coverage[y] - g.by_coverage[x];
    }).map(function (k) {
      return row([{ text: k }, { text: num(g.by_coverage[k]), cls: 'num' }]);
    })));
  l2.appendChild(el('p', 'hint', '전체 ' + num(g.total) + ' URL · 마지막 배치 ' +
    (g.last_batch || '—') + ' · 전체 스윕 ' + (g.last_full_sweep || '—')));

  var r2 = el('div');
  r2.appendChild(h3('미색인 — 조치 대상 ' + num(g.actionable) + '건'));
  r2.appendChild(table(['URL', '상태', { label: '이후', num: true }],
    (g.unindexed || []).filter(function (u) { return !u.snoozed; }).slice(0, 15)
      .map(function (u) {
        return row([
          { html: '<a href="https://math-jh.com' + esc(u.path) + '" target="_blank" class="mono">' +
                  esc(u.path) + '</a>' },
          { text: u.coverage.replace(' - currently not indexed', ''), cls: 'muted' },
          { text: u.since, cls: 'num muted' }
        ]);
      })));
  c2.appendChild(l2); c2.appendChild(r2);
  isec.appendChild(c2);
  frag.appendChild(isec);
  return frag;
}

/* ── 활동 ─────────────────────────────────────────────────────────────── */
function viewActivity(d) {
  var sec = section('활동');
  var c = cols();

  var left = el('div');
  left.appendChild(h3('최근 커밋'));
  left.appendChild(table(['sha', '종류', '내용', { label: '시각', num: true }],
    (d.git || []).map(gitRow)));

  var right = el('div');
  right.appendChild(h3('댓글'));
  var cm = d.comments || { ko: [], en: [] };
  var all = (cm.ko || []).concat(cm.en || []);
  if (all.length) {
    right.appendChild(table(['글', '작성자', { label: '시각', num: true }],
      all.slice(0, 10).map(function (x) {
        return row([
          { html: '<a href="' + esc(x.permalink) + '#' + esc(x.anchor || '') + '" target="_blank">' +
                  esc(x.title) + '</a>' },
          { text: x.author, cls: 'muted' },
          { text: (x.updated || '').slice(0, 10), cls: 'num muted' }
        ]);
      })));
  } else {
    right.appendChild(el('p', 'hint', '최근 댓글 없음'));
  }

  right.appendChild(h3('시스템'));
  var sys = d.system || {};
  right.appendChild(table(['항목', '값'], [
    row([{ text: 'Jekyll dev 서버' }, { text: sys.jekyll, cls: 'mono' }]),
    row([{ text: 'Pagefind 색인' }, { text: ago(sys.pagefind_mtime), cls: 'mono' }]),
    row([{ text: '메모리' }, { html: '<span class="mono">' + esc(sys.mem) + '</span>' }]),
    row([{ text: 'Claude 쿼터' }, {
      text: sys.quota ? ('주간 ' + Math.round(sys.quota.weekly * 100) + '% · 5h ' +
                         Math.round(sys.quota.h5 * 100) + '%') : '—', cls: 'mono'
    }])
  ]));
  if ((sys.dirty || []).length) {
    right.appendChild(h3('커밋 안 된 변경 ' + sys.dirty_count + '건'));
    right.appendChild(el('pre', 'log', sys.dirty.join('\n')));
  }

  c.appendChild(left); c.appendChild(right);
  sec.appendChild(c);
  return sec;
}

/* ── 라우팅·로드 ──────────────────────────────────────────────────────── */
var VIEWS = {
  '': viewOverview,
  workers: viewWorkers,
  drafts: viewDrafts,
  weights: viewWeights,
  translation: viewTranslation,
  audit: viewAudit,
  activity: viewActivity
};

function renderNav() {
  var cur = route();
  var nav = document.getElementById('nav');
  nav.innerHTML = '';
  ROUTES.forEach(function (r) {
    var a = el('a', r.key === cur ? 'is-active' : null, r.label);
    a.href = BASE + r.key;
    nav.appendChild(a);
  });
}

function render(d) {
  state.data = d;
  var view = document.getElementById('view');
  view.innerHTML = '';
  view.appendChild(VIEWS[route()](d));
  if (route() === 'drafts') wireDrafts(d);
  document.getElementById('stamp').textContent =
    new Date(d.ts * 1000).toLocaleString('ko-KR') + ' 기준 · ' + ago(d.ts) + ' 수집';
}

function load(fresh) {
  fetch(API + 'summary' + (fresh ? '?fresh=1' : ''))
    .then(function (r) { return r.json(); })
    .then(render)
    .catch(function (e) {
      document.getElementById('stamp').textContent = '데이터를 읽지 못했다: ' + e;
    });
}

document.getElementById('refresh-btn').onclick = function () { load(true); };
themeApply(themeMode());
renderNav();
load(false);
setInterval(function () { load(false); }, 60000);
