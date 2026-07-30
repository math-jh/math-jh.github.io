/* 블로그 대시보드 — 개요가 허브인 hash 라우팅 SPA.
   탭 네비 없음: 진입은 개요의 지표·알림·섹션 색인, 복귀는 각 페이지의 '개요로'.
   데이터는 /api/summary 스냅샷 하나 (60초 폴링, 실패 시 마지막 스냅샷 유지). */
'use strict';

/* 구 경로(/dash/workers 등)로 들어오면 hash 라우트로 넘긴다. */
(function () {
  var m = location.pathname.match(/^\/dash\/(workers|pipeline|drafts|weights|translation|audit|index|activity)\/?$/);
  if (m) location.replace('/dash/#' + m[1]);
})();

var API = '/dash/api/';
var DRAFT_PAGE = 20;
var state = {
  data: null,
  stampErr: false,
  draftCat: '', draftSort: 'mtime', draftLimit: DRAFT_PAGE,
  wSortKey: 'un', wSortDesc: true
};

/* 워커·파이프라인은 별도 페이지 없이 개요에서 소화한다 — 워커 행은 로그
   모달 직결, 파이프라인은 개요 우측 칼럼에 상주. */
var ROUTES = ['drafts', 'weights', 'translation', 'audit', 'index', 'activity'];
var SECTION_LABEL = { drafts: '미발행', weights: 'weight 지도', translation: '번역 큐', audit: '감사', index: '색인', activity: '활동' };
var PAGE_DESC = {
  drafts: '미발행 초안 목록·필터·lint', weights: '카테고리별 weight 눈금자',
  translation: '번역 상태 집계·KO-TYPOS·최근 시도', audit: '링크·frontmatter 감사와 번역 짝 맞춤',
  index: 'GSC 색인 분포와 조치 대상', activity: '커밋·댓글·시스템 상태'
};

function route() {
  var p = location.hash.replace(/^#/, '');
  return ROUTES.indexOf(p) >= 0 ? p : '';
}
function link(k) { return '#' + (k || ''); }

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
function agoSec(sec) {
  if (sec === null || sec === undefined) return '—';
  if (sec < 90) return Math.round(sec) + '초';
  if (sec < 5400) return Math.round(sec / 60) + '분';
  if (sec < 172800) return Math.round(sec / 3600) + '시간';
  return Math.round(sec / 86400) + '일';
}
function ago(ts) {
  if (!ts) return '—';
  return agoSec(Date.now() / 1000 - ts) + ' 전';
}
function agoIso(iso) {
  var t = Date.parse(iso || '');
  return isNaN(t) ? '—' : ago(t / 1000);
}
function num(n) { return (n === null || n === undefined) ? '—' : n.toLocaleString('ko-KR'); }
function kchars(n) { return Math.round((n || 0) / 1000).toLocaleString('ko-KR') + 'k'; }
function shortCat(c) { return String(c).replace(/^Math\//, '').replace(/_/g, ' '); }
function pct(a, b) { return b ? Math.round(a / b * 100) : 0; }

function secNode(title, meta) {
  var s = el('section', 'sec'), hd = el('div', 'sec__hd');
  hd.appendChild(el('h2', null, title));
  hd.appendChild(el('div', 'rule'));
  if (meta) hd.appendChild(el('div', 'meta', meta));
  s.appendChild(hd);
  return s;
}
function table(headers, rows) {
  var wrap = el('div', 'tbl-scroll'), t = el('table'), thead = el('thead'), tr = el('tr');
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
var KIND = { manual: '수동', auto: '자동' };
function gitRow(c) {
  return row([
    { text: c.sha, cls: 'mono muted' },
    { text: KIND[c.kind] || c.kind, cls: 'muted sans nowrap' },
    { text: c.subject },
    { text: ago(c.ts), cls: 'num muted nowrap' }
  ]);
}
function badWorkers(d) {
  return (d.workers || []).filter(function (w) {
    return w.status === 'stale' || w.status === 'missing' || w.err;
  });
}
/* ── 모달 ─────────────────────────────────────────────────────────────── */
function openModal(title, body) {
  document.getElementById('modal-title').textContent = title;
  document.getElementById('modal-body').textContent = body;
  document.getElementById('modal').hidden = false;
}
function wireModal() {
  document.getElementById('modal-close').onclick = function () {
    document.getElementById('modal').hidden = true;
  };
  document.getElementById('modal').onclick = function (e) {
    if (e.target === this) this.hidden = true;
  };
  document.addEventListener('keydown', function (e) {
    if (e.key === 'Escape') document.getElementById('modal').hidden = true;
  });
}

/* ── 테마 — 블로그와 MTHEME 쿠키 공유, 3단(자동/라이트/다크) 드롭다운 ──── */
function themeMode() {
  var m = (document.cookie.split('; ').find(function (c) { return c.indexOf('MTHEME=') === 0; }) || '').slice(7);
  return (m === 'light' || m === 'dark' || m === 'auto') ? m : 'auto';
}
function applyTheme(mode, persist) {
  var dark = mode === 'dark' || (mode === 'auto' && window.matchMedia
    && window.matchMedia('(prefers-color-scheme: dark)').matches);
  document.documentElement.setAttribute('data-theme', dark ? 'dark' : 'light');
  if (persist) document.cookie = 'MTHEME=' + mode + '; path=/; max-age=31536000; samesite=lax';
}
if (window.matchMedia) {
  window.matchMedia('(prefers-color-scheme: dark)').addEventListener('change', function () {
    if (themeMode() === 'auto') applyTheme('auto');
  });
}
/* 바깥 클릭으로 드롭다운 닫기 — 마스트헤드가 렌더마다 새로 만들어지므로 위임 한 개로. */
document.addEventListener('click', function () {
  var m = document.querySelector('.theme-menu.show');
  if (m) m.classList.remove('show');
});

var THEME_ICON = { auto: 'brightness_auto', light: 'light_mode', dark: 'dark_mode' };
function themeMenu() {
  var box = el('div', 'mh__menu');
  var btn = el('button', 'mh__btn');
  btn.title = '테마'; btn.setAttribute('aria-label', '테마');
  function btnIcon(m) {
    btn.innerHTML = '<i class="material-icons">' + THEME_ICON[m] +
      '</i><i class="material-icons dropdown-arrow">arrow_drop_down</i>';
  }
  btnIcon(themeMode());
  var ul = el('ul', 'theme-menu');
  [['auto', '자동'], ['light', '라이트'], ['dark', '다크']].forEach(function (m) {
    var li = el('li', themeMode() === m[0] ? 'active' : null);
    li.innerHTML = '<span>' + m[1] + '</span><i class="material-icons check">done</i>';
    li.onclick = function (e) {
      e.stopPropagation();
      applyTheme(m[0], true);
      [].forEach.call(ul.children, function (x, i) {
        x.className = i === ['auto', 'light', 'dark'].indexOf(m[0]) ? 'active' : '';
      });
      btnIcon(m[0]);
      ul.classList.remove('show');
    };
    ul.appendChild(li);
  });
  btn.onclick = function (e) { e.stopPropagation(); ul.classList.toggle('show'); };
  box.appendChild(btn); box.appendChild(ul);
  return box;
}

/* ── 마스트헤드 ───────────────────────────────────────────────────────── */
function stampText(d) {
  return new Date(d.ts * 1000).toLocaleString('ko-KR') + ' · ' + ago(d.ts) + ' 수집' +
    (state.stampErr ? ' (갱신 실패)' : '');
}
function masthead(d) {
  var mh = el('div', 'mh'), inner = el('div', 'mh__inner'), nav = el('div', 'mh__nav');
  var title = el('a', 'site-title');
  title.href = '/';
  title.title = '블로그 홈으로';
  title.innerHTML = 'BLACK<span class="site-title__box">BOX</span><span class="site-title__dash">Dashboard</span>';
  nav.appendChild(title);
  nav.appendChild(el('div', 'mh__spacer'));
  var stamp = el('div', 'mh__stamp' + (state.stampErr ? ' mh__stamp--err' : ''), stampText(d));
  nav.appendChild(stamp);
  var rb = el('button', 'mh__btn');
  rb.title = '새로고침'; rb.setAttribute('aria-label', '새로고침');
  rb.innerHTML = '<i class="material-icons">refresh</i>';
  rb.onclick = function () {
    rb.style.opacity = .4;
    setTimeout(function () { rb.style.opacity = 1; }, 260);
    load(true);
  };
  nav.appendChild(rb);
  nav.appendChild(themeMenu());
  inner.appendChild(nav); mh.appendChild(inner);
  return mh;
}

/* ── 판정·알림 규칙 ───────────────────────────────────────────────────── */
function alertsOf(d) {
  var out = [], s = d.stats, sys = d.system || {}, g = d.gsc;
  badWorkers(d).forEach(function (w) {
    out.push({
      level: 'bad',
      text: w.name + ' — ' + (w.status === 'missing' ? '로그 파일 없음'
        : w.err ? '로그에 오류' : '실행이 ' + agoSec(w.age) + ' 넘게 없음'),
      sub: '누르면 로그가 열린다', worker: w.has_log ? w : null
    });
  });
  if (sys.jekyll !== 'active') out.push({ level: 'bad', text: 'Jekyll dev 서버가 ' + sys.jekyll, to: 'activity' });
  if (sys.mem && /hit_cap=[1-9]/.test(sys.mem)) out.push({ level: 'warn', text: 'Jekyll 메모리 cap 도달 이력', sub: sys.mem.trim(), to: 'activity' });
  if (sys.quota && sys.quota.weekly >= .9) out.push({ level: 'warn', text: '주간 쿼터 ' + Math.round(sys.quota.weekly * 100) + '% — 워커가 스킵될 수 있다', to: 'activity' });
  if (s.missing_en) out.push({ level: 'warn', text: '발행글 중 EN 없음 ' + s.missing_en + '건', to: 'audit' });
  if (s.orphan_en) out.push({ level: 'warn', text: '고아 EN(ko 없음) ' + s.orphan_en + '건', to: 'audit' });
  if (g && g.actionable) {
    var oldest = (g.unindexed || []).filter(function (u) { return !u.snoozed; })[0];
    out.push({
      level: 'info', text: '색인 요청 넣을 만한 URL ' + g.actionable + '건',
      sub: oldest ? '가장 오래된 건 ' + oldest.since + ' 이후 미색인' : '', to: 'index'
    });
  }
  if (s.drift) out.push({ level: 'info', text: '재번역 대기 ' + s.drift + '편', sub: 'ko 본문이 바뀐 뒤 en 이 따라오지 않은 글', to: 'translation' });
  if (sys.dirty_count) out.push({
    level: 'info', text: '커밋 안 된 변경 ' + sys.dirty_count + '건',
    sub: (sys.dirty || [])[0] + (sys.dirty_count > 1 ? ' 외 ' + (sys.dirty_count - 1) + '건' : ''), to: 'activity'
  });
  return out;
}
function verdict(d) {
  var bad = badWorkers(d), ws = (d.workers || []).length;
  if (bad.length) return {
    ok: false, head: '워커 ' + bad.length + '개 점검 필요',
    sub: bad.map(function (w) { return w.name; }).join(' · ') + ' 의 로그가 주기보다 늙었다.'
  };
  return {
    ok: true, head: '워커 ' + ws + '개 모두 정상',
    sub: '급한 일은 없다. 미발행 ' + num(d.stats.unpublished) + '편 · 재번역 대기 ' + num(d.stats.drift) +
      '편 · 색인 조치 ' + num((d.gsc || {}).actionable) + '건 — 오늘 안 해도 무너지지 않는 일.'
  };
}

/* ── 워커 로그 모달 ───────────────────────────────────────────────────── */
function openWorkerLog(w) {
  openModal(w.name + ' — 로그', '불러오는 중…');
  fetch(API + 'log?name=' + encodeURIComponent(w.key) + '&n=300')
    .then(function (r) { return r.json(); })
    .then(function (j) {
      openModal(w.name + ' — ' + j.path, (j.lines || []).join('\n') || '(빈 로그)');
    })
    .catch(function (e) { openModal(w.name, '로그를 읽지 못했다: ' + e); });
}

/* ── 개요 ─────────────────────────────────────────────────────────────── */
function overview(d) {
  var frag = document.createDocumentFragment(), s = d.stats, sys = d.system || {}, v = verdict(d);
  var g = d.gsc, drafts = d.unpublished || [];

  var vp = el('div', 'panel verdict'), left = el('div');
  left.innerHTML = '<h1 class="verdict__h' + (v.ok ? '' : ' verdict__h--warn') + '"><i></i>' + esc(v.head) + '</h1>' +
    '<p class="verdict__s">' + esc(v.sub) + '</p>';
  var right = el('div');
  right.appendChild(el('p', 'panel__t', '최근 24시간 실행 기록'));
  var beats = el('div', 'beats');
  var nowSec = Date.now() / 1000;
  (d.workers || []).forEach(function (w) {
    var a = el('div', 'beat' + (w.has_log ? ' clickable' : ''));
    var ticks = '';
    (w.runs || []).forEach(function (ts) {
      var frac = (1 - (nowSec - ts) / 86400) * 100;
      if (frac >= 0 && frac <= 100) ticks += '<i style="left:' + frac.toFixed(2) + '%"></i>';
    });
    a.innerHTML = '<span><span class="dot dot--' + w.status + '"></span>' + esc(w.name) +
      (w.err ? '<span class="tag tag--err">로그 오류</span>' : '') + '</span>' +
      '<span class="beat__track">' + ticks + '</span>' +
      '<span class="beat__age">' + (w.age == null ? '—' : agoSec(w.age) + ' 전') + '</span>';
    if (w.has_log) a.onclick = function () { openWorkerLog(w); };
    beats.appendChild(a);
  });
  right.appendChild(beats);
  var ax = el('div', 'beats__axis');
  ax.innerHTML = '<div></div><div><span>-24h</span><span>-18h</span><span>-12h</span><span>-6h</span><span>지금</span></div><div></div>';
  right.appendChild(ax);
  var note = el('div', 'beats__note');
  note.innerHTML = '<span><i></i>실제 실행 (로그 타임스탬프)</span><span>오른쪽 끝이 지금</span><span>행을 누르면 로그 300줄</span>';
  right.appendChild(note);
  vp.appendChild(left); vp.appendChild(right); frag.appendChild(vp);

  var driftDrafts = drafts.filter(function (x) { return x.drift; }).length;
  var mets = [
    { n: num(s.unpublished), l: '미발행 초안', to: 'drafts', accent: true,
      d: (drafts[0] ? '최근 수정 ' + ago(drafts[0].mtime) : '초안 없음') + ' · drift 표시 ' + driftDrafts + '편' },
    { n: num(s.drift), l: '재번역 대기', to: 'translation', accent: true,
      d: 'ko 가 바뀐 뒤 en 이 따라오지 않은 글' },
    { n: num(g ? g.actionable : null), l: '색인 조치 대상', to: 'index', accent: true,
      d: 'Crawled·Discovered 이면서 미색인' },
    { n: num(s.published), l: '발행 ko', to: 'weights',
      d: '영문 ' + num(s.en) + '편 (' + pct(s.en, s.published) + '%) · 30일 신규 ' + s.new30d },
    { n: num(d.audit ? d.audit.posts_with_issues : null), l: '링크 이슈 글', to: 'audit',
      d: d.audit ? d.audit.scanned + '편 검사 · ' + ago(d.audit.mtime) + ' 갱신' : 'audit-report.md 없음' },
    { n: num(sys.dirty_count), l: '커밋 안 된 변경', to: 'activity',
      d: sys.dirty_count ? (sys.dirty[0] || '').replace(/^[ MADRCU?!]+/, '') : 'working tree clean' }
  ];
  var g3 = el('div', 'grid3');
  mets.forEach(function (m) {
    var a = el('a', 'panel metric' + (m.accent ? ' metric--accent' : ''));
    a.href = link(m.to);
    a.innerHTML = '<div class="panel__t">' + esc(m.l) + '</div><div class="metric__n">' + m.n +
      '</div><div class="metric__d">' + esc(m.d) + '</div>';
    g3.appendChild(a);
  });
  frag.appendChild(g3);

  var cols = el('div', 'cols'), cl = el('div', 'panel'), cr = el('div', 'panel');
  cl.appendChild(el('p', 'panel__t', '지금 볼 것'));
  var al = alertsOf(d);
  if (al.length) {
    var ul = el('ul', 'todo');
    al.forEach(function (a) {
      var li = el('li', a.level === 'bad' ? 'bad' : (a.level === 'warn' ? 'warn' : null));
      li.innerHTML = '<a href="' + (a.worker ? 'javascript:void(0)' : link(a.to)) + '">' + esc(a.text) + '</a>' +
        (a.sub ? '<small>' + esc(a.sub) + '</small>' : '');
      if (a.worker) li.querySelector('a').onclick = function () { openWorkerLog(a.worker); };
      ul.appendChild(li);
    });
    cl.appendChild(ul);
  } else cl.appendChild(el('p', 'hint', '임계값을 넘긴 항목 없음.'));
  cr.appendChild(el('p', 'panel__t', '파이프라인'));
  cr.appendChild(secPipeline(d));
  cols.appendChild(cl); cols.appendChild(cr); frag.appendChild(cols);

  var gp = el('div', 'panel');
  gp.style.marginBottom = '1.4rem';
  gp.appendChild(el('p', 'panel__t', '최근 커밋'));
  gp.appendChild(table(['sha', '종류', '내용', { label: '시각', num: true }], (d.git || []).slice(0, 6).map(gitRow)));
  var q = el('div', 'quota');
  q.innerHTML = '<div>Jekyll dev<b>' + esc(sys.jekyll) + '</b></div>' +
    '<div>Pagefind<b>' + ago(sys.pagefind_mtime) + '</b></div>' +
    '<div>주간 쿼터<b>' + (sys.quota ? Math.round(sys.quota.weekly * 100) + '%' : '—') + '</b></div>' +
    '<div>5h 쿼터<b>' + (sys.quota ? Math.round(sys.quota.h5 * 100) + '%' : '—') + '</b></div>' +
    '<div style="margin-left:auto"><a href="' + link('activity') + '">활동 전체 →</a></div>';
  gp.appendChild(q); frag.appendChild(gp);

  return frag;
}

/* ── 파이프라인 ───────────────────────────────────────────────────────── */
function secPipeline(d) {
  var st = d.stats, g = d.gsc || {};
  var s = secNode('파이프라인', '초안에서 색인까지');
  s.appendChild(el('p', 'hint', '글 하나가 통과하는 단계별 잔량. 막대는 최대 단계 대비 비율이다.'));
  var stages = [
    { l: '초안 (미발행)', n: st.unpublished },
    { l: '발행 ko', n: st.published },
    { l: '번역 완료 en', n: st.en },
    { l: '재번역 대기', n: st.drift },
    { l: '색인 완료', n: (g.by_coverage || {})['Submitted and indexed'] || 0 },
    { l: '색인 조치 대상', n: g.actionable || 0 }
  ];
  var max = Math.max.apply(null, stages.map(function (x) { return x.n || 0; })) || 1;
  var box = el('div', 'pipe');
  stages.forEach(function (x) {
    var r = el('div', 'pipe__row');
    r.appendChild(el('div', null, x.l));
    var bar = el('div', 'pipe__bar'), i = el('i');
    i.style.width = Math.max(1, (x.n || 0) / max * 100) + '%';
    bar.appendChild(i);
    r.appendChild(bar);
    r.appendChild(el('div', 'pipe__n', num(x.n)));
    box.appendChild(r);
  });
  s.appendChild(box);
  s.appendChild(el('p', 'pipe__note', '발행 ' + num(st.published) + '편 중 ' + num(st.en) +
    '편이 영문을 가진다 (' + pct(st.en, st.published) + '%). 색인은 en·ko 합산 ' +
    num(g.total) + ' URL 기준.'));
  return s;
}

/* ── 미발행 ───────────────────────────────────────────────────────────── */
function secDrafts(d) {
  var s = secNode('미발행 글', num(d.stats.unpublished) + '편');
  var bar = el('div', 'toolbar');
  bar.innerHTML = '<label>카테고리 <select id="draft-cat"></select></label>' +
    '<label>정렬 <select id="draft-sort">' +
      '<option value="mtime">최근 수정순</option>' +
      '<option value="category">카테고리·weight순</option>' +
      '<option value="chars">분량순</option>' +
    '</select></label>' +
    '<span id="draft-count" class="count"></span>';
  s.appendChild(bar);
  var body = el('div'); body.id = 'drafts-body'; s.appendChild(body);
  setTimeout(function () { wireDrafts(d); }, 0);
  return s;
}
function wireDrafts(d) {
  var sel = document.getElementById('draft-cat');
  if (!sel) return;
  var cats = {};
  (d.unpublished || []).forEach(function (p) { cats[p.category] = (cats[p.category] || 0) + 1; });
  sel.innerHTML = '<option value="">전체</option>';
  Object.keys(cats).sort().forEach(function (c) {
    var o = el('option', null, shortCat(c) + ' (' + cats[c] + ')');
    o.value = c;
    sel.appendChild(o);
  });
  sel.value = cats[state.draftCat] ? state.draftCat : '';
  var srt = document.getElementById('draft-sort');
  srt.value = state.draftSort;
  function reset() {
    state.draftCat = sel.value;
    state.draftSort = srt.value;
    state.draftLimit = DRAFT_PAGE;
    renderDrafts(d);
  }
  sel.onchange = reset;
  srt.onchange = reset;
  renderDrafts(d);
}
function renderDrafts(d) {
  var cat = state.draftCat, sort = state.draftSort;
  var list = (d.unpublished || []).filter(function (p) { return !cat || p.category === cat; }).slice();
  if (sort === 'chars') list.sort(function (a, b) { return b.chars - a.chars; });
  else if (sort === 'category') list.sort(function (a, b) {
    return a.category.localeCompare(b.category) || (a.weight || 0) - (b.weight || 0);
  });
  else list.sort(function (a, b) { return b.mtime - a.mtime; });
  var shown = list.slice(0, state.draftLimit);
  var rows = shown.map(function (p) {
    var tr = row([
      { html: '<a href="' + esc(p.permalink) + '" target="_blank">' + esc(p.title) + '</a>' +
              (p.drift ? '<span class="tag tag--drift">drift</span>' : '') +
              '<div class="path">' + esc(p.path) + '</div>' },
      { text: shortCat(p.category), cls: 'muted sans' },
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
    num(list.length) + '편 중 ' + shown.length + '편 표시' + (cat ? ' · ' + shortCat(cat) : '');
  var box = document.getElementById('drafts-body');
  box.innerHTML = '';
  box.appendChild(table(
    ['글', '카테고리', { label: 'weight', num: true }, { label: '분량', num: true },
     { label: '수정', num: true }, ''], rows));
  if (shown.length < list.length) {
    var more = el('button', 'ghost-btn', '더 보기 (' + (list.length - shown.length) + '편 남음)');
    more.style.marginTop = '1.2rem';
    more.onclick = function () { state.draftLimit += DRAFT_PAGE; renderDrafts(d); };
    box.appendChild(more);
  }
}

/* ── weight 지도 — 눈금자. 발행분은 낮고 조용한 회색, 미발행만 키 크고 brass. ── */
function secWeights(d) {
  var cats = d.categories || [], open = cats.filter(function (c) { return c.unpublished; }).length;
  var s = secNode('weight 지도', cats.length + ' 카테고리 · 미발행 있는 곳 ' + open);
  var bar = el('div', 'toolbar');
  bar.innerHTML = '<label>정렬 <select id="wsort">' +
      '<option value="un">미발행 수</option><option value="name">이름</option><option value="rate">완결률</option>' +
    '</select>' +
    '<button id="wdir" class="ghost-btn wdir" title="오름차순/내림차순"><i class="material-icons">arrow_downward</i></button></label>' +
    '<span class="count">눈금 하나 = 글 하나 · 왼쪽부터 weight 오름차순 · 커서를 올리면 weight</span>';
  s.appendChild(bar);
  var key = el('div', 'wkey');
  key.innerHTML = '<span><i class="wt"></i> 발행</span><span><i class="wt wt--un"></i> 미발행</span>' +
    '<span><i class="wt wt--gap" style="width:14px"></i> 빈 weight 슬롯</span>' +
    '<span><i class="wt wt--un wt--drift"></i> 재번역 대기</span><span>⋯ 빈 슬롯 5칸 이상 생략</span>';
  s.appendChild(key);
  var wrap = el('div', 'wmap'); wrap.id = 'wmap'; s.appendChild(wrap);
  setTimeout(function () {
    var sel = document.getElementById('wsort'), dir = document.getElementById('wdir');
    if (!sel) return;
    sel.value = state.wSortKey;
    function dirIcon() {
      dir.innerHTML = '<i class="material-icons">' + (state.wSortDesc ? 'arrow_downward' : 'arrow_upward') + '</i>';
    }
    dirIcon();
    sel.onchange = function () { state.wSortKey = sel.value; renderWeights(d); };
    dir.onclick = function () { state.wSortDesc = !state.wSortDesc; dirIcon(); renderWeights(d); };
    wireWTip();
    renderWeights(d);
  }, 0);
  return s;
}
/* 커서 판독 — 눈금이 7px 로 좁아 native title 은 실질적으로 안 뜬다. 직접 띄운다. */
function wireWTip() {
  var tip = document.getElementById('wtip');
  if (!tip) { tip = el('div'); tip.id = 'wtip'; document.body.appendChild(tip); }
  var wrap = document.getElementById('wmap');
  wrap.addEventListener('mousemove', function (e) {
    var t = e.target.closest ? e.target.closest('.wt') : null;
    if (!t || !t.dataset.tip) { tip.className = ''; return; }
    tip.textContent = t.dataset.tip;
    tip.style.left = (t.getBoundingClientRect().left + t.offsetWidth / 2) + 'px';
    tip.style.top = t.getBoundingClientRect().top + 'px';
    tip.className = 'on';
  });
  wrap.addEventListener('mouseleave', function () { tip.className = ''; });
}
function renderWeights(d) {
  var wrap = document.getElementById('wmap');
  if (!wrap) return;
  var mode = state.wSortKey, cats = (d.categories || []).slice();
  if (mode === 'name') cats.sort(function (a, b) { return shortCat(a.name).localeCompare(shortCat(b.name)); });
  else if (mode === 'rate') cats.sort(function (a, b) {
    return (a.total - a.unpublished) / (a.total || 1) - (b.total - b.unpublished) / (b.total || 1);
  });
  else cats.sort(function (a, b) { return a.unpublished - b.unpublished || shortCat(a.name).localeCompare(shortCat(b.name)); });
  if (state.wSortDesc) cats.reverse();
  wrap.innerHTML = '';
  cats.forEach(function (c) {
    var r = el('div', 'wrow' + (c.unpublished ? '' : ' wrow--done'));
    r.appendChild(el('div', 'wname', shortCat(c.name)));
    var ruler = el('div', 'wruler');
    var placed = c.posts.filter(function (p) { return p.weight !== null && p.weight !== undefined; })
      .slice().sort(function (a, b) { return a.weight - b.weight; });
    var prev = 0;
    placed.forEach(function (p) {
      var gap = Math.floor(p.weight) - Math.floor(prev) - 1;
      if (gap > 0 && gap <= 4) {
        for (var k = 1; k <= gap; k++) {
          var gcell = el('div', 'wt wt--gap');
          gcell.dataset.tip = 'w' + (Math.floor(prev) + k) + ' · 빈 슬롯';
          ruler.appendChild(gcell);
        }
      } else if (gap > 4) {
        var sp = el('div', 'wt wt--skip', '⋯');
        sp.dataset.tip = '빈 슬롯 ' + gap + '칸 생략';
        ruler.appendChild(sp);
      }
      var t = el('div', 'wt' + (p.published ? '' : ' wt--un') + (p.drift ? ' wt--drift' : ''));
      t.dataset.tip = 'w' + p.weight + (p.published ? ' · 발행' : ' · 미발행') + (p.drift ? ' · 재번역 대기' : '');
      ruler.appendChild(t);
      prev = p.weight;
    });
    r.appendChild(ruler);
    var sum = el('div', 'wsum');
    sum.innerHTML = c.unpublished ? '<b>' + c.unpublished + '</b> / ' + c.total : '— / ' + c.total;
    sum.title = c.total + '편 중 미발행 ' + c.unpublished + '편';
    r.appendChild(sum);
    wrap.appendChild(r);
  });
}

/* ── 번역 ─────────────────────────────────────────────────────────────── */
function secTranslation(d) {
  var t = d.translation;
  var s = secNode('번역 큐', t ? num((t.stats || {}).total_done) + '편 누적' : null);
  if (!t) { s.appendChild(el('p', 'hint', 'translation_state.json 을 읽지 못했다.')); return s; }
  var c = el('div', 'cols2'), left = el('div'), right = el('div');
  left.appendChild(el('h3', null, '상태 집계'));
  var rows = Object.keys(t.by_status).sort().map(function (k) {
    return row([{ text: k, cls: 'mono' }, { text: num(t.by_status[k]), cls: 'num' }]);
  });
  rows.push(row([{ text: '재번역 대기 (drift_needed)', cls: 'mono' }, { text: num(d.stats.drift), cls: 'num' }]));
  left.appendChild(table(['status', { label: '건수', num: true }], rows));
  var st = t.stats || {};
  left.appendChild(el('p', 'hint', '누적 ' + num(st.total_done) + '편 · 입력 ' + kchars(st.total_in_chars) +
    '자 → 출력 ' + kchars(st.total_out_chars) + '자' +
    (st.total_in_chars ? ' (압축률 ' + pct(st.total_out_chars, st.total_in_chars) + '%)' : '')));
  /* KO-TYPOS — EN 검증기가 번역 중 KO 원문 오타를 교정하며 남긴 지적.
     다음 재검증 때까지 verdict 에 남으므로, KO 를 고쳤어도 표시가 유지될 수 있다.
     '수정' 체크는 localStorage 에 (path@verified_at) 키로 저장한다 — 새로고침에도
     유지되고, 같은 파일이 재검증되어 verified_at 이 바뀌면 체크가 풀린다. */
  var typos = t.ko_typos || [];
  var doneMap = (function () {
    try { return JSON.parse(localStorage.getItem('dash-kotypo-done') || '{}'); }
    catch (e) { return {}; }
  })();
  var liveKeys = {};
  left.appendChild(el('h3', null, '한글 오타 지적 (KO-TYPOS) — ' + typos.length + '편'));
  if (typos.length) {
    left.appendChild(table(['파일', { label: '건수', num: true }, { label: '검증', num: true }, { label: '수정', num: true }],
      typos.map(function (k) {
        var key = k.path + '@' + (k.verified_at || '');
        liveKeys[key] = true;
        var tr = row([
          { html: '<span class="path">' + esc(k.path.replace(/^_posts\//, '')) + '</span>' },
          { text: k.items.length, cls: 'num' },
          { text: agoIso(k.verified_at), cls: 'num muted' },
          { html: '<input type="checkbox" class="typo-chk"' + (doneMap[key] ? ' checked' : '') + '>', cls: 'num' }
        ], 'clickable' + (doneMap[key] ? ' typo-done' : ''));
        tr.onclick = function () {
          openModal('KO-TYPOS — ' + k.path,
            k.items.map(function (x) { return '- ' + x; }).join('\n') +
            '\n\n(검증 ' + (k.verified_at || '—') + ' · KO 를 고친 뒤에도 다음 재검증까지 표시가 남는다)');
        };
        var chk = tr.querySelector('.typo-chk');
        chk.onclick = function (e) { e.stopPropagation(); };
        chk.onchange = function () {
          if (chk.checked) doneMap[key] = 1; else delete doneMap[key];
          tr.classList.toggle('typo-done', chk.checked);
          try { localStorage.setItem('dash-kotypo-done', JSON.stringify(doneMap)); } catch (e) { }
        };
        return tr;
      })));
    /* 사라진 지적(재검증 통과 등)의 키는 정리한다. */
    var pruned = {};
    Object.keys(doneMap).forEach(function (k) { if (liveKeys[k]) pruned[k] = 1; });
    try { localStorage.setItem('dash-kotypo-done', JSON.stringify(pruned)); } catch (e) { }
    left.appendChild(el('p', 'hint', '행을 누르면 지적 내용 전체가 열린다. EN 은 이미 교정된 상태다. 수정 체크는 이 브라우저에 저장되며, 재검증으로 검증 시각이 바뀌면 풀린다.'));
  } else {
    left.appendChild(el('p', 'hint', '검증기가 지적한 한글 오타 없음.'));
  }
  right.appendChild(el('h3', null, '최근 시도'));
  right.appendChild(table(['파일', '상태', { label: '시각', num: true }], (t.recent || []).map(function (r) {
    return row([
      { html: '<span class="path">' + esc(r.path.replace(/^_posts\//, '')) + '</span>' },
      { text: r.status, cls: 'muted sans' },
      { text: ago(r.ts), cls: 'num muted' }
    ]);
  })));
  c.appendChild(left); c.appendChild(right); s.appendChild(c);
  return s;
}

/* ── 감사 ─────────────────────────────────────────────────────────────── */
function secAudit(d) {
  var a = d.audit;
  var s = secNode('감사', a ? ago(a.mtime) + ' 갱신' : null);
  var c = el('div', 'cols2'), left = el('div'), right = el('div');
  left.appendChild(el('h3', null, '링크·frontmatter'));
  if (a) {
    var det = a.details || {};
    left.appendChild(table(['종류', { label: '건수', num: true }],
      Object.keys(a.counts).sort(function (x, y) { return a.counts[y] - a.counts[x]; }).map(function (k) {
        var items = det[k] || [];
        var tr = row([
          { text: k, cls: 'mono' },
          { text: num(a.counts[k]), cls: 'num' }
        ], items.length ? 'clickable' : null);
        if (items.length) {
          tr.onclick = function () {
            openModal(k + ' — ' + num(a.counts[k]) + '건',
              items.map(function (x) { return '- ' + x; }).join('\n'));
          };
        }
        return tr;
      })));
    left.appendChild(el('p', 'hint', a.scanned + '편 검사 · 이슈 있는 글 ' + a.posts_with_issues +
      '편 · ' + ago(a.mtime) + ' 갱신 (주간 cron, 일 05:00) · 행을 누르면 글·줄 단위 상세'));
  } else left.appendChild(el('p', 'hint', 'audit-report.md 없음'));
  right.appendChild(el('h3', null, '번역 짝 맞춤'));
  right.appendChild(table(['항목', { label: '건수', num: true }], [
    row([{ text: '발행글 중 EN 없음' }, { text: num(d.stats.missing_en), cls: 'num' }]),
    row([{ text: '고아 EN (ko 없음)' }, { text: num(d.stats.orphan_en), cls: 'num' }])
  ]));
  right.appendChild(el('p', 'hint', '둘 다 0이면 ko/en 짝이 온전하다.'));
  if ((d.orphan_en || []).length) {
    right.appendChild(el('pre', 'log', d.orphan_en.map(function (o) { return o.path; }).join('\n')));
  }
  c.appendChild(left); c.appendChild(right); s.appendChild(c);
  return s;
}

/* ── 색인 ─────────────────────────────────────────────────────────────── */
function secIndex(d) {
  var g = d.gsc;
  var s = secNode('색인', g ? num(g.total) + ' URL' : null);
  if (!g) { s.appendChild(el('p', 'hint', 'index-monitor 상태 파일 없음')); return s; }
  var c = el('div', 'cols2'), l = el('div'), r = el('div');
  l.appendChild(el('h3', null, 'coverage 분포'));
  l.appendChild(table(['상태', { label: 'URL', num: true }],
    Object.keys(g.by_coverage).sort(function (x, y) { return g.by_coverage[y] - g.by_coverage[x]; }).map(function (k) {
      return row([{ text: k }, { text: num(g.by_coverage[k]), cls: 'num' }]);
    })));
  l.appendChild(el('p', 'hint', '전체 ' + num(g.total) + ' URL · 마지막 배치 ' + (g.last_batch || '—') +
    ' · 전체 스윕 ' + (g.last_full_sweep || '—')));
  var act = (g.unindexed || []).filter(function (u) { return !u.snoozed; }).slice(0, 15);
  r.appendChild(el('h3', null, '미색인 — 조치 대상 ' + num(g.actionable) + '건'));
  r.appendChild(table(['URL', '상태', { label: '이후', num: true }], act.map(function (u) {
    return row([
      { html: '<a href="https://math-jh.com' + esc(u.path) + '" target="_blank" class="mono">' + esc(u.path) + '</a>' },
      { text: (u.coverage || '').replace(' - currently not indexed', ''), cls: 'muted sans' },
      { text: u.since, cls: 'num muted' }
    ]);
  })));
  r.appendChild(el('p', 'hint', '오래된 것부터 색인 요청을 넣는다. 전체 ' + num(g.actionable) +
    '건 중 ' + act.length + '건 표시.'));
  c.appendChild(l); c.appendChild(r); s.appendChild(c);
  return s;
}

/* ── 활동 ─────────────────────────────────────────────────────────────── */
function secActivity(d) {
  var s = secNode('활동'), c = el('div', 'cols2'), left = el('div'), right = el('div');
  left.appendChild(el('h3', null, '최근 커밋'));
  left.appendChild(table(['sha', '종류', '내용', { label: '시각', num: true }], (d.git || []).slice(0, 18).map(gitRow)));
  var sys = d.system || {};
  right.appendChild(el('h3', null, '시스템'));
  right.appendChild(table(['항목', '값'], [
    row([{ text: 'Jekyll dev 서버', cls: 'nowrap' }, { text: sys.jekyll, cls: 'mono' }]),
    row([{ text: 'Pagefind 색인', cls: 'nowrap' }, { text: ago(sys.pagefind_mtime), cls: 'mono' }]),
    row([{ text: '메모리', cls: 'nowrap' }, { html: '<span class="mono">' + esc((sys.mem || '').trim()) + '</span>' }]),
    row([{ text: 'Claude 쿼터', cls: 'nowrap' }, {
      text: sys.quota ? '주간 ' + Math.round(sys.quota.weekly * 100) + '% · 5h ' +
        Math.round(sys.quota.h5 * 100) + '%' : '—', cls: 'mono'
    }])
  ]));
  if ((sys.dirty || []).length) {
    right.appendChild(el('h3', null, '커밋 안 된 변경 ' + sys.dirty_count + '건'));
    right.appendChild(el('pre', 'log', sys.dirty.join('\n')));
  }
  right.appendChild(el('h3', null, '댓글'));
  var cm = d.comments || {};
  var all = (cm.ko || []).concat(cm.en || []);
  if (all.length) {
    right.appendChild(table(['글', '작성자', { label: '시각', num: true }], all.slice(0, 10).map(function (x) {
      return row([
        { html: '<a href="' + esc(x.permalink) + (x.anchor ? '#' + esc(x.anchor) : '') + '" target="_blank">' + esc(x.title) + '</a>' },
        { text: x.author, cls: 'muted sans' },
        { text: (x.updated || '').slice(0, 10), cls: 'num muted' }
      ]);
    })));
  } else right.appendChild(el('p', 'hint', '최근 댓글 없음'));
  c.appendChild(left); c.appendChild(right); s.appendChild(c);
  return s;
}

var SECTIONS = {
  drafts: secDrafts, weights: secWeights,
  translation: secTranslation, audit: secAudit, index: secIndex, activity: secActivity
};

/* ── 페이지 셸 · 렌더 · 로드 ──────────────────────────────────────────── */
function page(d, rt) {
  var frag = document.createDocumentFragment();
  var back = el('a', 'back');
  back.href = link('');
  back.innerHTML = '<i class="material-icons">arrow_back</i>개요로';
  frag.appendChild(back);
  var h = el('h1', 'page__h');
  h.innerHTML = esc(SECTION_LABEL[rt]) + '<em>' + esc(PAGE_DESC[rt]) + '</em>';
  frag.appendChild(h);
  var box = el('div', 'sec--panel');
  box.appendChild(SECTIONS[rt](d));
  frag.appendChild(box);
  return frag;
}

function render() {
  var d = state.data;
  if (!d) return;
  var rt = route();
  var app = document.getElementById('app');
  app.innerHTML = '';
  app.appendChild(masthead(d));
  var shell = el('div', 'shell');
  shell.appendChild(rt ? page(d, rt) : overview(d));
  app.appendChild(shell);
  document.title = (rt ? SECTION_LABEL[rt] + ' — ' : '') + 'Blackbox Dashboard';
}

function load(fresh) {
  fetch(API + 'summary' + (fresh ? '?fresh=1' : ''))
    .then(function (r) { return r.json(); })
    .then(function (d) {
      state.data = d;
      state.stampErr = false;
      render();
    })
    .catch(function (e) {
      state.stampErr = true;
      var st = document.querySelector('.mh__stamp');
      if (st) {
        st.classList.add('mh__stamp--err');
        if (st.textContent.indexOf('갱신 실패') < 0) st.textContent += ' (갱신 실패)';
      }
      if (!state.data) {
        document.getElementById('app').innerHTML =
          '<div class="shell"><p class="hint">데이터를 읽지 못했다: ' + esc(e) + '</p></div>';
      }
    });
}

window.addEventListener('hashchange', function () { window.scrollTo(0, 0); render(); });
wireModal();
applyTheme(themeMode());
load(false);
setInterval(function () { load(false); }, 60000);
/* 수집 스탬프의 '몇 초 전'은 렌더 시점에 굳으므로 매초 따로 갱신한다. */
setInterval(function () {
  var st = document.querySelector('.mh__stamp');
  if (st && state.data) st.textContent = stampText(state.data);
}, 1000);
