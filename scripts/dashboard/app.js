/* 블로그 대시보드 — 개요가 허브인 SPA. 섹션마다 실제 경로(/dash/audit …)가 있고,
   같은 탭 안의 이동은 pushState 라 다시 불러오지 않는다. 서버는 섹션 경로에 index.html 을 준다.
   탭 네비 없음: 진입은 개요의 지표 카드(크론 제어는 실행 기록 머리의 일시정지 건수),
   복귀는 각 페이지의 '개요로'.
   데이터는 /api/summary 스냅샷 하나 (60초 폴링, 실패 시 마지막 스냅샷 유지). */
'use strict';

var API = '/dash/api/';
var DRAFT_PAGE = 20;
/* Pi 대시보드(status_dashboard, :8088) — Cloudflare Access 뒤의 status 서브도메인 (service-map). */
var PI_DASHBOARD = 'https://status.math-jh.com/';
var state = {
  data: null,
  stampErr: false,
  kotypoDone: {},
  draftLimit: DRAFT_PAGE,
  wSortKey: 'un', wSortDesc: true,
  wOpen: null, wHi: null,          /* 미발행: 펼친 카테고리, 짚은 글(경로) */
  kt: { key: null, i: null },      /* 번역 큐: 고른 원문 지적 글(요청 키)과 지적(detail 색인) */
  ktNote: {},                      /* 원문 지적 메모 칸에 쓰던 글 (요청 키별) */
  tSig: null,                      /* 번역 큐 데이터 지문 — 같으면 주기 렌더를 건너뛴다 */
  heat: null                       /* 개요 잔디 {key: 최근 커밋 sha, data: /api/heat} */
};

/* 워커는 별도 페이지 없이 개요의 실행 기록에서 소화한다 — 워커 행은 로그 모달 직결.
   개요는 판정·실행 기록과 지표 카드뿐이고, 숫자의 내역은 카드가 가리키는 페이지에 있다.
   weight 지도는 미발행 페이지에 합쳤다 — /dash/weights 는 /dash/drafts 로 보낸다. */
var ROUTES = ['drafts', 'translation', 'audit', 'index', 'activity', 'cron'];
var SECTION_LABEL = { drafts: '미발행', translation: '번역 큐', audit: '감사', index: '색인', activity: '활동', cron: '크론 제어' };
var PAGE_DESC = {
  drafts: '카테고리별 weight 지도와 미발행 글',
  translation: '지금 큐·한글 원문 지적·최근 시도', audit: '링크·frontmatter 감사, 번역 짝 맞춤, 링크 재판정',
  index: 'GSC 색인 분포와 조치 대상', activity: '커밋·대기 댓글 PR·시스템 상태',
  cron: '블로그 크론 워커 일시정지·재개'
};

function routeOf(pathname) {
  var m = pathname.match(/^\/dash\/([^\/]*)\/?$/);
  return m && ROUTES.indexOf(m[1]) >= 0 ? m[1] : '';
}
function route() { return routeOf(location.pathname); }
function link(k) { return '/dash/' + (k || ''); }

/* hash 주소(/dash/#audit — 북마크·알림 링크)는 같은 섹션의 경로로 바꾼다. 처음 열 때와,
   이미 열린 탭에서 hash 만 바뀔 때(문서를 다시 읽지 않는다) 둘 다 부른다.
   workers·pipeline 은 따로 페이지가 없고 개요에 있다. weights 는 미발행에 합쳤다. 바꿨으면 true. */
function hashToPath() {
  var h = location.hash.replace(/^#/, '');
  var to = ROUTES.indexOf(h) >= 0 ? h
    : (h === 'weights' || /^\/dash\/weights\/?$/.test(location.pathname)) ? 'drafts'
    : (h === 'workers' || h === 'pipeline' || /^\/dash\/(workers|pipeline)\/?$/.test(location.pathname)) ? ''
    : null;
  if (to === null) return false;
  history.replaceState(null, '', link(to));
  return true;
}
hashToPath();

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
var KST_SHORT = new Intl.DateTimeFormat('en-CA', {
  timeZone: 'Asia/Seoul', month: '2-digit', day: '2-digit',
  hour: '2-digit', minute: '2-digit', hourCycle: 'h23'
});
function shortKst(iso) {
  var t = Date.parse(iso || '');
  if (isNaN(t)) return '—';
  var parts = {};
  KST_SHORT.formatToParts(new Date(t)).forEach(function (p) {
    if (p.type !== 'literal') parts[p.type] = p.value;
  });
  return parts.month + '-' + parts.day + ' ' + parts.hour + ':' + parts.minute;
}
function num(n) { return (n === null || n === undefined) ? '—' : n.toLocaleString('ko-KR'); }
function kchars(n) { return Math.round((n || 0) / 1000).toLocaleString('ko-KR') + 'k'; }
function shortCat(c) { return String(c).replace(/^Math\//, '').replace(/_/g, ' '); }
function pct(a, b) { return b ? Math.round(a / b * 100) : 0; }

/* 글을 부르는 이름 '[카테고리] 제목' — 서버가 붙인다(server.py :: post_label). KO 글은
   categories 의 글마다, 감사·색인이 가리키는 EN 글과 permalink 는 d.labels 에 있다.
   이름을 못 찾으면(지워진 글 등) 경로를 그대로 쓴다. */
var LABELS = {}, PERMALINKS = {};   /* PERMALINKS: KO 글 경로 → permalink (미리보기용) */
function indexLabels(d) {
  LABELS = {}; PERMALINKS = {};
  (d.categories || []).forEach(function (c) {
    (c.posts || []).forEach(function (p) {
      if (p.path && p.permalink) PERMALINKS[p.path] = p.permalink;
      if (p.path) LABELS[p.path] = p.label;
      if (p.permalink) LABELS[p.permalink] = p.label;
    });
  });
  (d.orphan_en || []).forEach(function (o) { LABELS[o.path] = o.label; });
  Object.keys(d.labels || {}).forEach(function (k) { LABELS[k] = d.labels[k]; });
}
function postLabel(key) {
  key = String(key || '');
  return LABELS[key] || LABELS['_posts/' + key] || key.replace(/^_posts\//, '');
}
/* 마크다운 원문 조각의 링크는 라벨만 남긴다 — 주소와 {: … } IAL 은 뗀다.
   텍스트용이다. HTML 로 그릴 때는 shadow.js 의 shText. */
function mdPlain(s) {
  return String(s || '').replace(/\[((?:\\.|[^\]\\])*)\]\([^)\s]*\)(\{:[^}]*\})?/g, function (_, l) {
    return l.replace(/\\([\[\]])/g, '$1');
  }).replace(/\{:\s*data-lid=[^}]*\}/g, '');
}
/* 읽는 법·동작 설명은 화면에 늘 펴 두지 않고 '?' 뒤에 둔다 — 올리면 풍선, 누르면 모달. */
function helpBtn(title, text) {
  var b = el('button', 'ghost-btn help-btn', '?');
  b.type = 'button';
  b.title = text;
  b.onclick = function (e) { e.preventDefault(); e.stopPropagation(); openModal(title, text); };
  return b;
}
/* 소제목 한 줄 — 왼쪽 제목, 오른쪽 끝에 덧붙일 단추(extra)와 '?'. */
function h3Help(label, text, extra) {
  var h = el('h3', 'h3-row');
  h.appendChild(el('span', null, label));
  if (extra) h.appendChild(extra);
  if (text) h.appendChild(helpBtn(label, text));
  return h;
}

function secNode(title, meta) {
  var s = el('section', 'sec'), hd = el('div', 'sec__hd');
  hd.appendChild(el('h2', null, title));
  hd.appendChild(el('div', 'rule'));
  if (meta) hd.appendChild(el('div', 'meta', meta));
  s.appendChild(hd);
  return s;
}
function table(headers, rows, cls) {
  var wrap = el('div', 'tbl-scroll'), t = el('table', cls || null), thead = el('thead'), tr = el('tr');
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
    if (c.title) td.title = c.title;
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
    /* 일시정지 중이면 로그가 늙는 게 정상 — 의도된 정지를 고장으로 세지 않는다. */
    if (w.paused) return false;
    return w.status === 'stale' || w.status === 'missing' || w.err;
  });
}
function pausedCount(d) { return ((d.cron || {}).paused) || 0; }
/* 클립보드 복사 — 블로그 본문의 인용 라벨 복사(Citation.js)와 같은 방식.
   preview.math-jh.com 은 https 라 secure context 이고, http 로 직접 들어온
   경우를 위해 execCommand 폴백을 남긴다. */
function copyText(text, node) {
  function legacy() {
    var ta = document.createElement('textarea');
    ta.value = text;
    ta.style.position = 'fixed';
    ta.style.opacity = '0';
    document.body.appendChild(ta);
    ta.select();
    try { document.execCommand('copy'); } catch (e) { }
    document.body.removeChild(ta);
  }
  if (navigator.clipboard && window.isSecureContext) {
    navigator.clipboard.writeText(text).catch(legacy);
  } else {
    legacy();
  }
  if (node) {
    node.classList.add('copied');
    setTimeout(function () { node.classList.remove('copied'); }, 600);
  }
}
/* ── 모달 ─────────────────────────────────────────────────────────────── */
function openModal(title, body) {
  document.querySelector('.modal__box').classList.remove('modal__box--wide');
  document.getElementById('modal-title').textContent = title;
  document.getElementById('modal-body').textContent = body;
  document.getElementById('modal-body').hidden = false;
  document.getElementById('modal-rich').hidden = true;
  document.getElementById('modal').hidden = false;
}
/* KO 원문 지적 상세 — 항목마다 줄번호·판정, 문제, 수정. 인용문은 싣지 않는다(오른쪽 미리보기가
   그 문단을 짚는다 — ktFind). VALID 는 Codex가
   확정한 이유만, UNSURE·미검토는 원 지적과 Codex 의견을 나란히 보인다. 기각(FALSE)은
   맨 아래 접힌 칸으로 보낸다. 판정 필드가 없는 옛 항목은 주장 문자열 그대로 둔다. */
/* 모델 서술에 $ 없이 섞인 LaTeX(\alpha\smile\beta, `\x`)를 $…$ 로 감싼다.
   이미 $ 로 싸인 구간은 건드리지 않는다. 한 토막은 \명령 을 포함하는 ASCII 수식
   문자 연속이고, 한글·끝의 구두점·공백에서 끊는다. 중괄호가 안 맞으면 그대로 둔다. */
function wrapBareTex(s) {
  if (!s || s.indexOf('\\') < 0) return s;
  return s.split(/(\$\$[\s\S]*?\$\$|\$[^$]*\$)/).map(function (seg, i) {
    if (i % 2) return seg;
    seg = seg.replace(/`([^`]*\\[A-Za-z][^`]*)`/g, '$$$1$$');
    return seg.split(/(\$[^$]*\$)/).map(function (part, j) {
      if (j % 2) return part;
      return part.replace(/[A-Za-z0-9^_{}()\[\]|+\-=<>*'\/]*\\[A-Za-z]+[A-Za-z0-9\\^_{}()\[\]|+\-=<>*'\/:,.;! ]*/g,
        function (run) {
          var m = run.match(/^([\s\S]*?)([\s,.;:!]*)$/);
          var body = m[1], tail = m[2];
          var depth = 0;
          for (var c = 0; c < body.length; c++) {
            if (body[c] === '{') depth++;
            else if (body[c] === '}' && --depth < 0) return run;
          }
          return depth ? run : '$' + body + '$' + tail;
        });
    }).join('');
  }).join('');
}
function koReviewHtml(det, k, rejected, stuck) {
  var rank = { VALID: 0, UNSURE: 1, FALSE: 3 };
  var items = det.slice().sort(function (a, b) {
    var ra = a.verdict in rank ? rank[a.verdict] : 2, rb = b.verdict in rank ? rank[b.verdict] : 2;
    return ra - rb || (a.line || 1e9) - (b.line || 1e9);
  });
  function field(label, text, cls) {
    return text ? '<dt' + (cls ? ' class="' + cls + '"' : '') + '>' + label + '</dt><dd>' + esc(wrapBareTex(text)) + '</dd>' : '';
  }
  function one(x) {
    var v = x.verdict || '미검토';
    var head = '<span class="kr__loc">' + (x.line ? 'L' + x.line : '위치 미상') + '</span>' +
      '<span class="kr__v kr__v--' + (x.verdict || 'none').toLowerCase() + '">' + esc(v) + '</span>' +
      (x.kind && x.kind !== 'ERROR' ? '<span class="kr__kind">' + esc(x.kind) + '</span>' : '') +
      '<span class="kr__miss" hidden>원문에서 못 찾음 — 이미 고쳤을 수 있다</span>' +
      (x.source ? '<span class="kr__src">' + esc(x.source) + '</span>' : '');
    var body = '', rows = '';
    if (x.verdict === 'VALID' && x.why) {
      rows += field('문제', x.why);
    } else {
      rows += field('지적', x.issue || (x.quote ? '' : x.text));
      rows += field('Codex', x.why);
    }
    rows += field('수정', x.fix || x.suggested, 'kr__fix');
    if (rows) body += '<dl class="kr__rows">' + rows + '</dl>';
    return '<li class="kr__item" data-i="' + det.indexOf(x) + '">' + '<div class="kr__head">' + head + '</div>' +
      body + '</li>';
  }
  var live = items.filter(function (x) { return x.verdict !== 'FALSE'; });
  var dead = items.filter(function (x) { return x.verdict === 'FALSE'; });
  var html = '<ol class="kr">' + live.map(one).join('') + '</ol>';
  if (dead.length) {
    html += '<details class="kr__false"><summary>Codex 기각 ' + dead.length + '건</summary>' +
      '<ol class="kr">' + dead.map(one).join('') + '</ol></details>';
  }
  if (stuck) {
    html += '<div class="kr__reject kr__stuck"><b>후속 처리 막힘 · ' + stuck.count + '회 연속 대기' +
      (stuck.at ? ' · 마지막 ' + esc(agoIso(stuck.at)) : '') + '</b>' +
      '<p>' + esc(stuck.reason) + '</p></div>';
  }
  if (rejected) {
    html += '<div class="kr__reject"><b>지난 후속 승인 거절' +
      (k.followup_rejected_at ? ' · ' + esc(k.followup_rejected_at) : '') + '</b>' +
      '<p>' + esc(rejected) + '</p></div>';
  }
  html += '<div class="kr__note"><label for="kr-note">후속 검증 모델에게 전할 말</label>' +
    '<textarea id="kr-note" rows="4" maxlength="4000" placeholder="예: 2번은 이 글의 convention상 의도된 표현이라 고치지 않았다. / 3번은 정의 2를 고쳐서 해결했다.">' +
    esc(k.note || '') + '</textarea>' +
    '<div class="kr__note-bar"><button type="button" id="kr-note-save" class="ghost-btn">저장</button>' +
    '<span id="kr-note-status" class="muted">' + (k.note_at ? '저장됨 · ' + esc(k.note_at) : '') + '</span></div></div>';
  return html;
}
/* 구조가 있는 본문용 — html 은 호출부가 esc() 로 만든 것만 넘긴다. wide 면 두 칸짜리 넓은 창. */
function openModalHtml(title, html, wide) {
  document.querySelector('.modal__box').classList.toggle('modal__box--wide', !!wide);
  document.getElementById('modal-title').textContent = title;
  var rich = document.getElementById('modal-rich');
  rich.innerHTML = html;
  rich.scrollTop = 0;
  if (window.renderMathInElement) {
    window.renderMathInElement(rich, {
      delimiters: window.KATEX_DELIMITERS, macros: window.KATEX_MACROS,
      strict: false, throwOnError: false
    });
  }
  rich.hidden = false;
  document.getElementById('modal-body').hidden = true;
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
  var s = document.querySelector('.settings-submenu.show');
  if (s) s.classList.remove('show');
  var p = document.querySelector('.theme-menu li.open');
  if (p) p.classList.remove('open');
});

/* 블로그 masthead 설정 메뉴와 같은 꼴(언어 제외): 테마 ▸ 3단 서브메뉴 + 블로그 링크 */
function settingsMenu() {
  var box = el('div', 'mh__menu');
  var btn = el('button', 'mh__btn');
  btn.title = '설정'; btn.setAttribute('aria-label', '설정');
  btn.innerHTML = '<i class="material-icons">tune</i>' +
    '<i class="material-icons dropdown-arrow">arrow_drop_down</i>';
  var ul = el('ul', 'theme-menu');

  var parent = el('li');
  parent.innerHTML = '<span>테마</span><i class="material-icons caret">chevron_right</i>';
  var sub = el('ul', 'settings-submenu');
  [['auto', '자동'], ['light', '라이트'], ['dark', '다크']].forEach(function (m) {
    var li = el('li', themeMode() === m[0] ? 'active' : null);
    li.innerHTML = '<span>' + m[1] + '</span><i class="material-icons check">done</i>';
    li.onclick = function (e) {
      e.stopPropagation();
      applyTheme(m[0], true);
      [].forEach.call(sub.children, function (x, i) {
        x.className = i === ['auto', 'light', 'dark'].indexOf(m[0]) ? 'active' : '';
      });
    };
    sub.appendChild(li);
  });
  parent.onclick = function (e) {
    e.stopPropagation();
    sub.classList.toggle('show');
    parent.classList.toggle('open');
  };

  /* 판본 비교기는 SPA 밖의 독립 문서라 hash 라우트로 못 간다 — 메뉴에서 직접 건다. */
  var cmp = el('li');
  cmp.innerHTML = '<span>판본 비교</span><i class="material-icons go">arrow_forward</i>';
  cmp.onclick = function () { location.href = '/dash/compare.html'; };

  var blog = el('li');
  blog.innerHTML = '<span>블로그</span><i class="material-icons go">arrow_forward</i>';
  blog.onclick = function () { location.href = '/'; };

  ul.appendChild(parent); ul.appendChild(sub); ul.appendChild(cmp); ul.appendChild(blog);
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
  title.href = link('');
  title.title = '대시보드 홈으로';
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
  nav.appendChild(settingsMenu());
  inner.appendChild(nav); mh.appendChild(inner);
  return mh;
}

/* ── 판정 ─────────────────────────────────────────────────────────────── */
/* 판정 아래 문장에는 지표 카드가 세지 않는 이상만 적는다 — 카드에 있는 숫자는 되풀이하지 않는다. */
function warningsOf(d) {
  var out = [], s = d.stats, sys = d.system || {};
  if (sys.jekyll !== 'active') out.push('Jekyll dev 서버가 ' + sys.jekyll);
  if (sys.mem && /hit_cap=[1-9]/.test(sys.mem)) out.push('Jekyll 메모리 cap 도달 이력');
  if (sys.quota && sys.quota.weekly >= .9) out.push('주간 쿼터 ' + Math.round(sys.quota.weekly * 100) + '% — 워커가 스킵될 수 있다');
  if (s.missing_en) out.push('발행글 중 EN 없음 ' + s.missing_en + '건');
  if (s.orphan_en) out.push('고아 EN(ko 없음) ' + s.orphan_en + '건');
  return out;
}
function verdict(d) {
  var bad = badWorkers(d), ws = (d.workers || []).length, pz = pausedCount(d);
  var pnote = pz ? ' 일시정지 ' + pz + '건은 따로 세지 않았다.' : '';
  var warn = warningsOf(d), wnote = warn.length ? ' ' + warn.join(' · ') + '.' : '';
  if (bad.length) return {
    ok: false, head: '워커 ' + bad.length + '개 점검 필요',
    sub: bad.map(function (w) { return w.name; }).join(' · ') + ' 의 로그가 주기보다 늙었다.' + pnote + wnote
  };
  return {
    ok: true, head: '워커 ' + ws + '개 모두 정상' + (pz ? ' (정지 ' + pz + ')' : ''),
    sub: (warn.length ? wnote.slice(1) : '급한 일은 없다.') + pnote
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

/* ── 수정량 잔디 — KO 글 git 수정량, 최근 53주 ───────────────────────────── */
/* 열 하나가 한 주(월요일이 맨 위), 칸 하나가 하루. 색은 brass 한 색의 다섯 단계 — 0 은 빈 칸,
   나머지는 수정이 있었던 날들의 4분위로 나눈다(하루치가 수만 줄인 일괄 치환 날이 있어 고정 구간은
   쓸 수 없다). 데이터는 GET /api/heat (server.py :: heat_days, HEAD 가 바뀔 때만 다시 센다)이고
   최근 커밋 sha 가 같으면 주기 렌더마다 다시 받지 않는다. */
var HEAT_WD = ['월', '화', '수', '목', '금', '토', '일'];
var HEAT_HELP = 'KO 글이 날마다 얼마나 고쳐졌는지다 — git 커밋의 줄 추가+삭제를 한국 시간 날짜로 모은다. ' +
  '워커가 쓰는 커밋([Cron]·[Dash])은 빼고, 작업 트리를 짝수 정시에 주워 담는 [Auto] 커밋은 센다. ' +
  'EN 글·코드·데이터 파일은 세지 않는다.\n\ngit 에서 빠진 로컬 KO 글(.git/info/exclude — 비공개 연구 스트림)은 ' +
  '대시보드가 2시간마다(한국 시간 짝수 정시 2분 전) 따로 스냅샷을 찍어 그 차이를 같이 센다. ' +
  '첫 스냅샷(기준선) 이전 날짜에는 로컬 글 수정이 잡히지 않는다. 의존성 분류기가 로컬 글에 직접 붙이는 ' +
  '링크 식별자(data-lid)는 지우고 비교하므로 세지 않는다.\n\n칸 색은 다섯 단계다. 빈 칸은 수정이 없던 날이고, 나머지 네 단계는 ' +
  '수정이 있었던 날들을 줄 수로 4등분한 것이다(가장 진한 칸이 상위 25%). 단계별 줄 수는 아래 범례에 ' +
  '커서를 올리면 뜬다.\n\n칸에 커서를 올리면 그날의 줄 수와 커밋 수가, 누르면 그날의 커밋과 고친 글이 뜬다.';
function heatPanel(d) {
  var p = el('div', 'panel heat');
  var hd = el('p', 'panel__t panel__t--row');
  var t = el('span', 'panel__t-l', 'KO 글 수정량 — 최근 1년');
  t.appendChild(helpBtn('KO 글 수정량', HEAT_HELP));
  hd.appendChild(t);
  var sum = el('span', 'heat__sum');
  hd.appendChild(sum);
  p.appendChild(hd);
  var body = el('div', 'heat__body');
  p.appendChild(body);
  if (state.heat) heatPaint(body, sum, state.heat);
  else body.appendChild(el('p', 'hint', '수정량을 세는 중…'));
  /* 서버 캐시라 매 렌더 받아도 싸다. 지문(레포 HEAD + 로컬 스냅샷 HEAD)이 같으면 다시 그리지 않는다. */
  fetch(API + 'heat').then(function (r) { return r.json(); }).then(function (j) {
    if (j.pending) return;   /* 서버가 아직 세는 중 — 다음 주기 렌더에서 다시 받는다 */
    if (state.heat && state.heat.sig === j.sig && state.heat.today === j.today) return;
    state.heat = j;
    heatPaint(body, sum, j);
  }).catch(function () { });
  return p;
}
function heatPaint(body, sum, j) {
  var days = j.days || {}, today = j.today, DAY = 86400000;
  var t0 = Date.UTC(+today.slice(0, 4), +today.slice(5, 7) - 1, +today.slice(8, 10));
  var start = t0 - (52 * 7 + (new Date(t0).getUTCDay() + 6) % 7) * DAY;   /* 52주 전 월요일 */
  function iso(ms) { return new Date(ms).toISOString().slice(0, 10); }
  var inWin = Object.keys(days).filter(function (k) { return k >= iso(start) && k <= today; });
  var vals = inWin.map(function (k) { return days[k][0] + days[k][1]; })
    .filter(function (v) { return v > 0; }).sort(function (a, b) { return a - b; });
  var q = [.25, .5, .75].map(function (f) { return vals[Math.floor((vals.length - 1) * f)] || 0; });
  function level(v) { return !v ? 0 : v <= q[0] ? 1 : v <= q[1] ? 2 : v <= q[2] ? 3 : 4; }
  var add = 0, del = 0;
  inWin.forEach(function (k) { add += days[k][0]; del += days[k][1]; });
  sum.textContent = '고친 날 ' + num(vals.length) + '일 · +' + num(add) + ' −' + num(del) + '줄';

  body.innerHTML = '';
  var grid = el('div', 'heat__grid');
  grid.appendChild(el('span'));
  for (var w = 0; w < 53; w++) {
    var m = new Date(start + w * 7 * DAY).getUTCMonth();
    var pm = w ? new Date(start + (w - 1) * 7 * DAY).getUTCMonth() : -1;
    grid.appendChild(el('span', 'heat__m', m !== pm ? (m + 1) + '월' : ''));
  }
  for (var r = 0; r < 7; r++) {
    grid.appendChild(el('span', 'heat__wd', r % 2 ? '' : HEAT_WD[r]));
    for (w = 0; w < 53; w++) {
      var ds = iso(start + (w * 7 + r) * DAY), v = days[ds], tot = v ? v[0] + v[1] : 0;
      var c = el('i', 'heat__c heat__c--' + (ds > today ? 'none' : level(tot)) + (ds === today ? ' heat__c--today' : ''));
      if (ds <= today) {
        c.dataset.tip = ds + ' (' + HEAT_WD[r] + ') · ' + (v ? '+' + num(v[0]) + ' −' + num(v[1]) + '줄' +
          (v[2] ? ' · 커밋 ' + v[2] : '') + (v[3] ? ' · 로컬 글 ' + num(v[3]) + '줄' : '') : '수정 없음');
      }
      if (tot) c.onclick = heatDay.bind(null, ds);
      grid.appendChild(c);
    }
  }
  body.appendChild(grid);
  var foot = el('div', 'heat__foot');
  foot.appendChild(el('span', null, '적음'));
  var bounds = ['수정 없음', '1–' + num(q[0]) + '줄', num(q[0] + 1) + '–' + num(q[1]) + '줄',
                num(q[1] + 1) + '–' + num(q[2]) + '줄', num(q[2] + 1) + '줄 이상'];
  bounds.forEach(function (b, i) {
    var s = el('i', 'heat__c heat__c--' + i);
    s.dataset.tip = b;
    foot.appendChild(s);
  });
  foot.appendChild(el('span', null, '많음'));
  body.appendChild(foot);
  wireTip(body);
}
function heatDay(ds) {
  openModal(ds + ' — KO 글 수정', '불러오는 중…');
  fetch(API + 'heat/day?d=' + encodeURIComponent(ds)).then(function (r) { return r.json(); }).then(function (j) {
    var nLocal = j.commits.filter(function (c) { return c.local; }).length;
    var counts = [j.commits.length - nLocal ? '커밋 ' + (j.commits.length - nLocal) : '',
                  nLocal ? '로컬 스냅샷 ' + nLocal : ''].filter(Boolean).join(' · ');
    openModal(ds + ' — KO 글 수정 (' + counts + ')', j.commits.map(function (c) {
      /* 일괄 치환 커밋은 글이 수백 편이라 앞 여덟 편만 적는다. */
      var shown = c.files.slice(0, 8).map(function (f) { return '    ' + f; });
      if (c.files.length > 8) shown.push('    … 외 ' + (c.files.length - 8) + '편');
      return (c.local ? '로컬    ' : c.sha + '  ') + c.subject + '\n  +' + num(c.add) + ' −' + num(c.dele) +
        '줄 · 글 ' + c.files.length + '편\n' + shown.join('\n');
    }).join('\n\n') || '(커밋 없음)');
  }).catch(function (e) { openModal(ds, '읽지 못했다: ' + e); });
}

/* ── 개요 ─────────────────────────────────────────────────────────────── */
function overview(d) {
  var frag = document.createDocumentFragment(), s = d.stats, sys = d.system || {}, v = verdict(d);
  var g = d.gsc, drafts = d.unpublished || [];

  var vp = el('div', 'panel verdict'), left = el('div');
  left.innerHTML = '<h1 class="verdict__h' + (v.ok ? '' : ' verdict__h--warn') + '"><i></i>' + esc(v.head) + '</h1>' +
    '<p class="verdict__s">' + esc(v.sub) + '</p>';
  var right = el('div');
  /* 제목 줄 오른쪽 끝이 크론 제어로 가는 유일한 입구다 — 링크를 따로 두지 않고
     정지 건수 자체를 링크로 쓴다. 글꼴·색은 제목과 같고 hover 에서만 금색. */
  var beatsHd = el('p', 'panel__t panel__t--row');
  var beatsT = el('span', 'panel__t-l', '최근 24시간 실행 기록');
  beatsT.appendChild(helpBtn('최근 24시간 실행 기록',
    '눈금 하나가 실제 실행 한 번이다(로그 타임스탬프). 오른쪽 끝이 지금, 왼쪽 끝이 24시간 전이다. ' +
    '오른쪽 숫자는 마지막 실행에서 지난 시간이다. 행을 누르면 그 워커의 로그 끝 300줄이 열린다. ' +
    '오른쪽 위 일시정지 건수를 누르면 크론 제어로 간다.'));
  beatsHd.appendChild(beatsT);
  var cronLink = el('a', 'panel__t-link',
    pausedCount(d) ? '일시정지 ' + pausedCount(d) + '건' : '일시정지 없음');
  cronLink.href = link('cron');
  beatsHd.appendChild(cronLink);
  right.appendChild(beatsHd);
  var beats = el('div', 'beats');
  var nowSec = Date.now() / 1000;
  (d.workers || []).forEach(function (w) {
    var a = el('div', 'beat' + (w.has_log ? ' clickable' : ''));
    var ticks = '';
    (w.runs || []).forEach(function (ts) {
      var frac = (1 - (nowSec - ts) / 86400) * 100;
      if (frac >= 0 && frac <= 100) ticks += '<i style="left:' + frac.toFixed(2) + '%"></i>';
    });
    a.innerHTML = '<span><span class="dot dot--' + (w.paused ? 'paused' : w.status) + '"></span>' + esc(w.name) +
      (w.paused ? '<span class="tag">정지</span>' : '') +
      (w.err && !w.paused ? '<span class="tag tag--err">로그 오류</span>' : '') + '</span>' +
      '<span class="beat__track">' + ticks + '</span>' +
      '<span class="beat__age">' + (w.age == null ? '—' : agoSec(w.age) + ' 전') + '</span>';
    if (w.has_log) a.onclick = function () { openWorkerLog(w); };
    beats.appendChild(a);
  });
  right.appendChild(beats);
  var ax = el('div', 'beats__axis');
  ax.innerHTML = '<div></div><div><span>-24h</span><span>-18h</span><span>-12h</span><span>-6h</span><span>지금</span></div><div></div>';
  right.appendChild(ax);
  vp.appendChild(left); vp.appendChild(right); frag.appendChild(vp);
  frag.appendChild(heatPanel(d));

  var driftDrafts = drafts.filter(function (x) { return x.drift; }).length;
  /* 번역 카드의 큰 숫자는 한글 원문 지적이다 — 번역 큐 페이지가 주로 하는 일이고, 재번역 대기는
     거의 늘 0이라 설명 줄에 둔다. 세는 것은 Codex가 오탐(FALSE)으로 판정하지 않은 것뿐이다. */
  var kt = d.translation || {};
  var ktLive = (kt.ko_typo_actionable || 0) + (kt.ko_typo_unreviewed || 0);
  /* 페이지마다 한 장, 시스템은 Pi 대시보드(status.math-jh.com)로 가는 한 장 — 여섯 장이 같은 크기다.
     미발행은 발행 쪽 숫자를, 번역은 큐 숫자를 설명 줄에 싣는다. */
  var tq = (kt.queue || {}).buckets;
  var mem = /cur=(\S+).*max=(\S+)/.exec(sys.mem || '');
  var mets = [
    { n: num(s.unpublished), l: '미발행 초안', to: 'drafts', accent: true,
      d: '발행 ' + num(s.published) + '편 · 영문 ' + pct(s.en, s.published) + '% · 30일 신규 ' + s.new30d +
        (s.revising ? ' · 개정 중 ' + s.revising + '편' : '') + (driftDrafts ? ' · drift 표시 초안 ' + driftDrafts + '편' : '') },
    { n: num(ktLive), l: '한글 원문 지적', to: 'translation', accent: true,
      d: (kt.ko_typo_unreviewed ? '미검토 ' + kt.ko_typo_unreviewed + '건 · ' : '') +
        (tq ? '재번역 대기 ' + num(tq.drift.length) + '편 · 폴리싱 대기 ' + num(tq.polish.length) + '편'
            : '번역 큐 집계 중') },
    { n: num(g ? g.actionable : null), l: '색인 조치 대상', to: 'index', accent: true,
      d: 'Crawled·Discovered 이면서 미색인' },
    { n: num(d.audit ? d.audit.posts_with_issues : null), l: '링크 이슈 글', to: 'audit',
      d: d.audit ? d.audit.scanned + '편 검사 · ' + ago(d.audit.mtime) + ' 갱신' : 'audit-report.md 없음' },
    { n: num(sys.dirty_count), l: '커밋 안 된 변경', to: 'activity',
      d: (sys.dirty_count ? '' : 'working tree clean · ') + '미push ' + num(sys.unpushed || 0) + '건' +
        ((d.comment_prs || {}).count ? ' · 승인 대기 댓글 PR ' + d.comment_prs.count + '건' : '') },
    { n: sys.quota ? Math.round(sys.quota.weekly * 100) + '%' : '—', l: '시스템', href: PI_DASHBOARD,
      d: 'Claude 주간 쿼터' + (sys.quota ? ' (5h ' + Math.round(sys.quota.h5 * 100) + '%)' : '') +
        ' · Jekyll dev ' + (sys.jekyll || '—') + ' · Pagefind 재색인 ' + ago(sys.pagefind_mtime) +
        (mem ? ' · dev 서버 메모리 ' + mem[1] + ' / ' + mem[2] : '') }
  ];
  var g3 = el('div', 'grid3');
  mets.forEach(function (m) {
    var a = el('a', 'panel metric' + (m.accent ? ' metric--accent' : ''));
    a.href = m.href || link(m.to);
    a.innerHTML = '<div class="panel__t">' + esc(m.l) + '</div><div class="metric__n">' + m.n +
      '</div><div class="metric__d">' + esc(m.d) + '</div>';
    g3.appendChild(a);
  });
  frag.appendChild(g3);
  return frag;
}

/* ── 미발행 — weight 지도와 미발행 글 목록 한 페이지 ─────────────────────── */
/* 위는 카테고리별 weight 눈금자(발행분은 낮고 조용한 회색, 미발행만 키 크고 brass). 행을 누르면
   그 카테고리의 미발행 글이 행 바로 아래에 weight 순으로 펼쳐지고(한 번에 한 카테고리), 눈금을
   누르면 그 글의 카테고리를 펼쳐 그 글을 짚는다. 아래는 카테고리를 가리지 않은 최근 수정순 목록. */
function lintModal(p) {
  openModal('lint — ' + (p.label || p.title), '검사 중… (md_lint.py)');
  fetch(API + 'lint?path=' + encodeURIComponent(p.path))
    .then(function (r) { return r.json(); })
    .then(function (j) {
      var out = (j.out || '').trim() || (j.rc === 0 ? '지적 사항 없음.' : '');
      openModal('lint — ' + (p.label || p.title), out + (j.err ? '\n\n[stderr]\n' + j.err : ''));
    })
    .catch(function (e2) { openModal('lint', '실행 실패: ' + e2); });
}
function draftTable(list, hiPath) {
  return table(['글', { label: 'weight', num: true }, { label: '분량', num: true },
                { label: '수정', num: true }, ''], list.map(function (p) {
    var tr = row([
      { html: '<a href="' + esc(p.permalink) + '" target="_blank">' + esc(p.label || p.title) + '</a>' +
              (p.drift ? '<span class="tag tag--drift">drift</span>' : '') },
      { text: p.weight === null ? '—' : p.weight, cls: 'num' },
      { text: kchars(p.chars), cls: 'num' },
      { text: ago(p.mtime), cls: 'num muted' },
      { html: '<button class="ghost-btn lint-btn">lint</button>' }
    ], hiPath && p.path === hiPath ? 'is-hi' : null);
    tr.querySelector('.lint-btn').onclick = function (e) { e.stopPropagation(); lintModal(p); };
    return tr;
  }));
}
function renderDrafts(d) {
  var box = document.getElementById('drafts-body');
  if (!box) return;
  var list = (d.unpublished || []).slice().sort(function (a, b) { return b.mtime - a.mtime; });
  var shown = list.slice(0, state.draftLimit);
  document.getElementById('draft-count').textContent = num(list.length) + '편 중 ' + shown.length + '편';
  box.innerHTML = '';
  box.appendChild(draftTable(shown));
  if (shown.length < list.length) {
    var more = el('button', 'ghost-btn', '더 보기 (' + (list.length - shown.length) + '편 남음)');
    more.style.marginTop = '1.2rem';
    more.onclick = function () { state.draftLimit += DRAFT_PAGE; renderDrafts(d); };
    box.appendChild(more);
  }
}
function secDrafts(d) {
  var cats = d.categories || [], open = cats.filter(function (c) { return c.unpublished; }).length;
  var s = secNode('미발행', cats.length + ' 카테고리 · 미발행 있는 곳 ' + open);
  var bar = el('div', 'toolbar');
  bar.innerHTML = '<label>정렬 <select id="wsort">' +
      '<option value="un">미발행 수</option><option value="site">카테고리 순서</option>' +
      '<option value="name">이름</option><option value="rate">완결률</option>' +
    '</select>' +
    '<button id="wdir" class="ghost-btn wdir" title="오름차순/내림차순"><i class="material-icons">arrow_downward</i></button></label>';
  s.appendChild(bar);
  var key = el('div', 'wkey');
  key.innerHTML = '<span><i class="wt"></i> 발행</span><span><i class="wt wt--un"></i> 미발행</span>' +
    '<span><i class="wt wt--gap" style="width:14px"></i> 빈 weight 슬롯</span>' +
    '<span><i class="wt wt--un wt--drift"></i> 재번역 대기</span><span>⋯ 빈 슬롯 5칸 이상 생략</span>';
  s.appendChild(key);
  var wrap = el('div', 'wmap'); wrap.id = 'wmap'; s.appendChild(wrap);
  var rh = el('h3', 'h3-row drafts-recent');
  rh.appendChild(el('span', null, '최근 수정한 미발행 글'));
  var cnt = el('span', 'count'); cnt.id = 'draft-count';
  rh.appendChild(cnt);
  s.appendChild(rh);
  var body = el('div'); body.id = 'drafts-body'; s.appendChild(body);
  setTimeout(function () {
    renderDrafts(d);
    var sel = document.getElementById('wsort'), dir = document.getElementById('wdir');
    if (!sel) return;
    sel.value = state.wSortKey;
    function dirIcon() {
      dir.innerHTML = '<i class="material-icons">' + (state.wSortDesc ? 'arrow_downward' : 'arrow_upward') + '</i>';
    }
    dirIcon();
    sel.onchange = function () {
      state.wSortKey = sel.value;
      /* 카테고리 순서는 내림차순이 무의미하다 — 선택 시 정방향으로 맞춘다. */
      if (sel.value === 'site' && state.wSortDesc) { state.wSortDesc = false; dirIcon(); }
      renderWeights(d);
    };
    dir.onclick = function () { state.wSortDesc = !state.wSortDesc; dirIcon(); renderWeights(d); };
    wireTip(document.getElementById('wmap'));
    renderWeights(d);
  }, 0);
  return s;
}
/* 커서 판독 — weight 눈금·잔디 칸이 작아 native title 은 실질적으로 안 뜬다. data-tip 을 직접 띄운다. */
function wireTip(wrap) {
  var tip = document.getElementById('wtip');
  if (!tip) { tip = el('div'); tip.id = 'wtip'; document.body.appendChild(tip); }
  wrap.addEventListener('mousemove', function (e) {
    var t = e.target.closest ? e.target.closest('[data-tip]') : null;
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
  if (mode === 'site') cats.sort(function (a, b) {
    return (a.order || 0) - (b.order || 0) || shortCat(a.name).localeCompare(shortCat(b.name));
  });
  else if (mode === 'name') cats.sort(function (a, b) { return shortCat(a.name).localeCompare(shortCat(b.name)); });
  else if (mode === 'rate') cats.sort(function (a, b) {
    return (a.total - a.unpublished) / (a.total || 1) - (b.total - b.unpublished) / (b.total || 1);
  });
  else cats.sort(function (a, b) { return a.unpublished - b.unpublished || shortCat(a.name).localeCompare(shortCat(b.name)); });
  if (state.wSortDesc) cats.reverse();
  wrap.innerHTML = '';
  var hiRow = null;
  cats.forEach(function (c) {
    var isOpen = state.wOpen === c.name;
    var r = el('div', 'wrow' + (c.unpublished ? '' : ' wrow--done') + (isOpen ? ' wrow--open' : ''));
    r.onclick = function () {
      state.wOpen = isOpen ? null : c.name;
      state.wHi = null;
      renderWeights(d);
    };
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
      t.dataset.tip = (p.label || p.title) + ' · w' + p.weight + (p.published ? ' · 발행' : ' · 미발행') +
        (p.drift ? ' · 재번역 대기' : '');
      t.onclick = function (e) {
        e.stopPropagation();
        state.wOpen = c.name;
        state.wHi = p.published ? null : p.path;
        renderWeights(d);
      };
      ruler.appendChild(t);
      prev = p.weight;
    });
    r.appendChild(ruler);
    var sum = el('div', 'wsum');
    sum.innerHTML = c.unpublished ? '<b>' + c.unpublished + '</b> / ' + c.total : '— / ' + c.total;
    sum.title = c.total + '편 중 미발행 ' + c.unpublished + '편';
    r.appendChild(sum);
    wrap.appendChild(r);
    if (!isOpen) return;
    /* 펼친 카테고리 — 미발행 글을 weight 순으로 (weight 없는 글은 끝에). */
    var panel = el('div', 'wpanel');
    var un = c.posts.filter(function (p) { return !p.published; }).sort(function (a, b) {
      return (a.weight === null) - (b.weight === null) || (a.weight || 0) - (b.weight || 0);
    });
    if (un.length) panel.appendChild(draftTable(un, state.wHi));
    else panel.appendChild(el('p', 'hint', '미발행 글이 없다.'));
    wrap.appendChild(panel);
    hiRow = panel.querySelector('tr.is-hi');
  });
  if (hiRow) {
    var b = hiRow.getBoundingClientRect();
    if (b.top < 0 || b.bottom > window.innerHeight) hiRow.scrollIntoView({ block: 'center' });
  }
}

/* ── 번역 ─────────────────────────────────────────────────────────────── */
/* 지금 큐 — 글마다 워커가 어느 단계에서 집을지 (translate_worker.py --queue 가
   find_next_target 과 같은 조건으로 판정). 순서가 곧 워커의 선택 순서다.
   opt 행은 0편이면 숨긴다. g 는 막대의 색 묶음 — 워커가 할 일(brass), 끝남(ok),
   건너뜀·보류·제외(회색). 이름과 편수는 막대 아래 목록이 싣고, 색은 묶음을 알아보는 데만 쓴다. */
var TQ_ROWS = [
  { k: 'pending', l: '신규 번역 대기', d: 'EN 이 없는 발행 글', g: 'todo' },
  { k: 'drift', l: '재번역 대기', d: 'drift_needed 표시가 있는 발행 글', g: 'todo' },
  { k: 'polish', l: '폴리싱 대기', d: 'EN 이 현재 폴리싱 태그 이전 판본 (폴리싱이 검증까지 한다)', g: 'todo' },
  { k: 'verify', l: '검증 대기', d: '폴리싱 때 검증을 못 마친 글', opt: true, g: 'todo' },
  { k: 'done', l: '완료', d: '현재 태그로 폴리싱·검증까지 끝남', g: 'done' },
  { k: 'draft', l: '건너뜀 · 초안', d: 'published: false', g: 'skip' },
  { k: 'revising', l: '건너뜀 · 개정 중', d: 'revising: true', g: 'skip' },
  { k: 'stub', l: '건너뜀 · 스텁', d: '본문 300자 미만', opt: true, g: 'skip' },
  { k: 'await_lid', l: '보류 · 링크 식별자 대기', d: 'data-lid 없는 내부 링크가 있음', opt: true, g: 'skip' },
  { k: 'backoff', l: '보류 · 실패 백오프', d: '실패 뒤 24시간 대기', opt: true, g: 'skip' },
  { k: 'manual', l: '제외 · 수동 번역', d: 'EN 이 워커 번역이 아님', opt: true, g: 'skip' }
];
/* 지금 큐 — 맨 위 얇은 막대가 전체 글이 단계별로 어떻게 나뉘는지, 그 아래 목록이 단계별 편수.
   0편인 단계는 막대에 그리지 않는다. 행을 누르면 그 단계의 글 목록. */
function tqueueView(q) {
  var box = el('div', 'tq');
  var held = {};
  (q.held_drift || []).forEach(function (p) { held[p] = true; });
  var rows = TQ_ROWS.filter(function (r) { return !r.opt || (q.buckets[r.k] || []).length; });
  var total = rows.reduce(function (a, r) { return a + (q.buckets[r.k] || []).length; }, 0) || 1;
  var bar = el('div', 'tq__bar');
  rows.forEach(function (r) {
    var n = (q.buckets[r.k] || []).length;
    if (!n) return;
    var seg = el('i', 'tq__seg tq--' + r.g);
    seg.style.flexGrow = n;
    seg.title = r.l + ' ' + num(n) + '편 (' + pct(n, total) + '%)';
    bar.appendChild(seg);
  });
  box.appendChild(bar);
  box.appendChild(table(['단계', { label: '편', num: true }], rows.map(function (r) {
    var paths = q.buckets[r.k] || [];
    var nHeld = paths.filter(function (p) { return held[p]; }).length;
    var tr = row([
      { html: '<i class="tq__sw tq--' + r.g + '"></i>' + esc(r.l) },
      { html: num(paths.length) + (nHeld ? ' <span class="muted">(drift 표시 ' + nHeld + ')</span>' : ''), cls: 'num' }
    ], paths.length ? 'clickable' : null);
    if (paths.length) {
      tr.onclick = function () {
        openModal(r.l + ' — ' + num(paths.length) + '편', paths.map(function (p) {
          return postLabel(p) + (held[p] ? '   · drift_needed 표시' : '');
        }).join('\n'));
      };
    }
    return tr;
  }), 'tq__list'));
  return box;
}
/* 최근 시도 — 넓은 모달 두 칸. 왼쪽은 글·상태·시각, 오른쪽은 고른 글의 마지막 시도 로그
   (GET /api/translog — 번역 워커 로그에서 그 글의 `translating (…)` 줄부터 잘라 온다). */
function openRecentAttempts(t) {
  openModalHtml('번역 워커 — 최근 시도',
    '<div class="tl"><div class="tl__list"></div>' +
    '<pre class="tl__log">왼쪽에서 글을 누르면 그 글의 마지막 시도 로그가 여기 뜬다.</pre></div>', true);
  var list = document.querySelector('#modal-rich .tl__list');
  var log = document.querySelector('#modal-rich .tl__log');
  var rows = (t.recent || []).map(function (r) {
    var tr = row([
      { text: postLabel(r.path) },
      { text: r.status, cls: 'muted sans nowrap' },
      { text: ago(r.ts), cls: 'num muted nowrap' }
    ], 'clickable');
    tr.onclick = function () {
      Array.prototype.forEach.call(list.querySelectorAll('tr.is-sel'), function (x) { x.classList.remove('is-sel'); });
      tr.classList.add('is-sel');
      log.textContent = '불러오는 중…';
      fetch(API + 'translog?path=' + encodeURIComponent(r.path))
        .then(function (res) { return res.json(); })
        .then(function (j) {
          /* 구간 안의 경로는 고른 글의 KO·EN 파일뿐이라 KO·EN 으로 줄이고, 글 이름은 맨 위에 한 번. */
          var lines = (j.lines || []).map(function (ln) {
            return ln.replace(/_posts\/\S+?\/(ko|en)\/[^\s)]+?\.md/g, function (_, lang) { return lang.toUpperCase(); });
          });
          log.textContent = lines.length ? postLabel(r.path) + '\n\n' + lines.join('\n')
            : '(로그에서 이 글의 시도를 찾지 못했다)';
          log.scrollTop = 0;
        })
        .catch(function (e) { log.textContent = '로그를 읽지 못했다: ' + e; });
    };
    return tr;
  });
  list.appendChild(table(['글', '상태', { label: '시각', num: true }], rows));
}
function secTranslation(d) {
  var t = d.translation;
  var s = secNode('번역 큐', t ? num((t.stats || {}).total_done) + '편 누적' : null);
  if (!t) { s.appendChild(el('p', 'hint', 'translation_state.json 을 읽지 못했다.')); return s; }
  var left = el('div', 'kt-queue');
  var q = t.queue;
  var recentBtn = el('button', 'ghost-btn h3-row__btn', '최근 시도');
  recentBtn.type = 'button';
  recentBtn.onclick = function () { openRecentAttempts(t); };
  left.appendChild(h3Help('지금 큐', '워커가 위 단계부터 차례로 집는다. 초안·개정 중인 글은 drift_needed 표시가 ' +
    '있어도 건너뛰고, 발행되거나 revising 이 빠지면 그때 해당 단계로 들어간다. 행을 누르면 그 단계의 글 목록이 ' +
    '열린다.\n\n' + TQ_ROWS.map(function (r) { return r.l + ' — ' + r.d; }).join('\n') +
    '\n\n현재 폴리싱 태그: ' + ((q && q.polish_tag) || '—') +
    '\n\n막대 색은 묶음이다 — 워커가 할 일은 금색, 끝난 글은 초록, 건너뜀·보류·제외는 회색.', recentBtn));
  if (q) {
    left.appendChild(tqueueView(q));
  } else {
    left.appendChild(el('p', 'hint', t.queue_error ? '큐 집계 실패: ' + t.queue_error
      : '큐를 집계하는 중이다 (몇 초). 잠시 뒤 새로고침.'));
  }
  var st = t.stats || {};
  left.appendChild(el('p', 'hint', '누적 ' + num(st.total_done) + '편 · 입력 ' + kchars(st.total_in_chars) +
    '자 → 출력 ' + kchars(st.total_out_chars) + '자' +
    (st.total_in_chars ? ' (압축률 ' + pct(st.total_out_chars, st.total_in_chars) + '%)' : '')));
  /* 한글 원문 지적 — Gemini 후보를 Codex가 오류/설명 누락으로 검증한 목록.
     '수정 완료' 체크는 해결 표시가 아니라 후속 워커 요청이다. 02시부터 4시간마다
     Antigravity가 EN을 맞추고 Codex가 KO/EN diff를 통과시켜야 목록에서 사라진다.
     왼쪽이 목록(ktRender), 오른쪽이 KO 원문 미리보기(ktPaint)다. 지금 큐는 목록 아래. */
  var typos = t.ko_typos || [];
  var doneMap = state.kotypoDone;
  var rows = typos.map(function (k) {
    var det = k.detail || k.items.map(function (x) { return { text: x }; });
    return { k: k, key: k.path + '@' + (k.verified_at || ''), det: det,
             rejected: k.followup_rejection || '', stuck: k.followup_stuck,
             nFalse: det.filter(function (x) { return x.verdict === 'FALSE'; }).length };
  });
  var liveKeys = {};
  rows.forEach(function (r) { liveKeys[r.key] = true; });
  /* 사라진 지적(재검증 통과 등)의 키는 정리한다. */
  var stale = Object.keys(doneMap).filter(function (k) { return !liveKeys[k]; });
  if (stale.length) {
    stale.forEach(function (k) { delete doneMap[k]; });
    saveKotypoDone();
  }
  var main = el('div');
  main.appendChild(h3Help('한글 원문 지적 — ' + typos.length + '편', typos.length ? KT_HELP : ''));
  var list = el('div', 'kt-list');
  main.appendChild(list);
  main.appendChild(left);
  if (!rows.length) {
    list.appendChild(el('p', 'hint', '검증된 한글 오류·설명 누락 없음.'));
    s.appendChild(main);
    return s;
  }
  if (!liveKeys[state.kt.key]) state.kt = { key: rows[0].key, i: null };
  var cols = el('div', 'sh-cols kt-cols'), pane = el('div', 'sh-pv kt-pv');
  pane.id = 'kt-preview';
  cols.appendChild(main); cols.appendChild(pane); s.appendChild(cols);
  setTimeout(function () { ktRender(list, rows); }, 0);
  return s;
}

/* ── 한글 원문 지적 — 왼쪽 목록, 오른쪽 KO 원문 미리보기 ─────────────────── */
var KT_HELP = '글을 누르면 그 글의 지적이 펼쳐지고(한 번에 한 편), 지적을 누르면 오른쪽 미리보기가 그 인용문이 ' +
  '있는 문단을 짚는다. 원문에서 인용문을 못 찾으면 그 지적에 표시가 붙는다 — 대개 이미 고친 문장이다.\n\n' +
  '판정(VALID·UNSURE·기각)은 Codex 검토 결과다. 한글을 고친 뒤 수정 완료를 체크하면 02:15부터 4시간마다 ' +
  '후속 워커가 EN을 맞추고 Codex가 KO·EN diff를 검증한다. Codex가 거절하면 체크가 자동 해제되고 사유가 남는다. ' +
  'KO·EN diff가 승인된 경우에만 목록에서 사라진다.\n\n' +
  '메모 칸의 글은 EN 수정안을 만드는 모델과 판정하는 Codex가 함께 읽는다. 메모가 있으면 KO를 고치지 않은 ' +
  '지적도 판정에 넘어간다(오탐 해명 등). 승인되면 메모도 지워진다.';
/* 번역 큐 데이터 지문 — 주기 렌더가 같은 데이터로 미리보기 iframe 을 다시 굽지 않게 한다. */
function tSig(d, done) { return JSON.stringify([d && d.translation, done]); }
function saveKotypoDone() {
  state.tSig = tSig(state.data, state.kotypoDone);
  fetch(API + 'kotypo', {
    method: 'POST',
    headers: { 'Content-Type': 'application/json', 'X-Dash-Action': '1' },
    body: JSON.stringify(state.kotypoDone)
  }).catch(function () { });
}
/* 인용문을 비교할 꼴 — 공백을 하나로, kramdown 이 바꾸는 따옴표·줄임표·대시를 되돌린다. */
function ktNorm(s) {
  return String(s).replace(/[“”]/g, '"').replace(/[‘’]/g, "'").replace(/…/g, '...')
    .replace(/—/g, '---').replace(/–/g, '--').replace(/\s+/g, ' ').trim();
}
/* 지적 인용문이 있는 자리 — 수식 밖 조각(6자 이상, 긴 것부터 셋)이 든 가장 작은 블록. 조각이
   없거나 못 찾으면 수식을 KaTeX 가 남긴 TeX 주석(annotation)에서 찾는다. 결과로 그 지적의
   '원문에서 못 찾음' 표시를 켜고 끈다. */
function ktFind(x, li) {
  var q = String(x.quote || '');
  var frags = mdPlain(q).replace(/\$\$[\s\S]*?\$\$|\$[^$]*\$/g, '\u0000').replace(/[*`]/g, '')
    .split('\u0000').map(ktNorm).filter(function (f) { return f.length >= 6; })
    .sort(function (a, b) { return b.length - a.length; }).slice(0, 3);
  var tex = q.replace(/[\s$]/g, '').slice(0, 40);
  return function (doc) {
    var root = doc.querySelector('.page__content') || doc.body, hit = null;
    if (frags.length) {
      var blocks = Array.prototype.map.call(
        root.querySelectorAll('p, li, td, th, dd, dt, h1, h2, h3, h4, h5, figcaption, blockquote'),
        function (b) { return { b: b, t: ktNorm(b.textContent) }; });
      for (var j = 0; j < frags.length && !hit; j++) {
        var best = null;
        blocks.forEach(function (o) {
          if (o.t.indexOf(frags[j]) >= 0 && (!best || o.t.length < best.t.length)) best = o;
        });
        hit = best && best.b;
      }
    }
    if (!hit && tex.length >= 6) {
      var anns = root.querySelectorAll('annotation');
      for (var a = 0; a < anns.length && !hit; a++) {
        if (anns[a].textContent.replace(/\s/g, '').indexOf(tex) >= 0) {
          hit = anns[a].closest('.katex-display') || anns[a].closest('.katex');
        }
      }
    }
    var miss = li && li.querySelector('.kr__miss');
    if (miss) miss.hidden = !!hit;
    return hit;
  };
}
/* 오른쪽 칸 — dev 서버의 구워진 KO 글(shadow.js 의 shSlot·shHit). 같은 글이면 iframe 은 그대로
   두고 짚는 자리만 옮긴다. */
function ktPaint(k, x, li) {
  var pane = document.getElementById('kt-preview');
  if (!pane || !x) return;
  var url = PERMALINKS[k.path];
  if (!url) { pane.innerHTML = '<p class="hint">이 글의 주소를 찾지 못했다.</p>'; return; }
  var hint = pane.querySelector('.hint');
  if (hint) hint.remove();
  shSlot(pane, 'sh-pv__slot--src', '원문', postLabel(k.path), url, ktFind(x, li));
}
function ktRender(list, rows) {
  var doneMap = state.kotypoDone;
  list.innerHTML = '';
  rows.forEach(function (r) {
    var k = r.k, key = r.key, open = state.kt.key === key, done = !!doneMap[key];
    var box = el('div', 'kt-post' + (open ? ' kt-post--open' : '') + (done ? ' kt-post--done' : ''));
    var head = el('div', 'kt-post__h');
    head.innerHTML = '<span class="kt-post__t">' + esc(postLabel(k.path)) + '</span>' +
      '<span class="kt-post__n">' + (k.live == null ? k.items.length : k.live) + '건' +
        (r.nFalse ? ' <span class="muted">(+오탐 ' + r.nFalse + ')</span>' : '') + '</span>' +
      '<span class="kt-post__at">' + esc(agoIso(k.verified_at)) + '</span>' +
      '<label class="kt-post__done"><input type="checkbox" class="typo-chk"' + (done ? ' checked' : '') +
        '> 수정 완료</label>';
    box.appendChild(head);
    head.onclick = function (e) {
      if (open || e.target.closest('label')) return;
      state.kt = { key: key, i: null };
      ktRender(list, rows);
    };
    var chk = head.querySelector('.typo-chk');
    chk.onchange = function () {
      if (chk.checked) doneMap[key] = 1; else delete doneMap[key];
      saveKotypoDone();
      ktRender(list, rows);
    };
    /* 접힌 글은 머리 아래에 상태 꼬리표만 — 펼친 글은 본문이 같은 내용을 자세히 싣는다. */
    if (!open) {
      var tags = (k.note ? '<span class="typo-note">메모 있음</span>' : '') +
        (r.rejected ? '<span class="typo-reject">승인 거절: ' + esc(r.rejected) + '</span>' : '') +
        (r.stuck && done ? '<span class="typo-stuck">후속 처리 막힘 ' + r.stuck.count + '회: ' +
          esc(r.stuck.reason) + '</span>' : '');
      if (tags) { var tg = el('div', 'kt-post__tags'); tg.innerHTML = tags; box.appendChild(tg); }
      list.appendChild(box);
      return;
    }
    var body = el('div', 'kt-post__b');
    body.innerHTML = koReviewHtml(r.det, k, r.rejected, done ? r.stuck : null);
    box.appendChild(body);
    list.appendChild(box);
    shMath(body);
    var first = body.querySelector('ol.kr > .kr__item[data-i]');
    if (state.kt.i == null || !body.querySelector('.kr__item[data-i="' + state.kt.i + '"]')) {
      state.kt.i = first ? +first.dataset.i : null;
    }
    Array.prototype.forEach.call(body.querySelectorAll('.kr__item[data-i]'), function (li) {
      var i = +li.dataset.i;
      li.classList.toggle('kr__item--sel', i === state.kt.i);
      li.onclick = function () {
        state.kt.i = i;
        Array.prototype.forEach.call(body.querySelectorAll('.kr__item--sel'), function (o) {
          o.classList.remove('kr__item--sel');
        });
        li.classList.add('kr__item--sel');
        ktPaint(k, r.det[i], li);
      };
      if (i === state.kt.i) ktPaint(k, r.det[i], li);
    });
    var note = body.querySelector('#kr-note'), stat = body.querySelector('#kr-note-status');
    if (state.ktNote[key] != null) note.value = state.ktNote[key];
    note.oninput = function () { state.ktNote[key] = note.value; };
    body.querySelector('#kr-note-save').onclick = function () {
      stat.textContent = '저장 중…';
      fetch(API + 'kotypo-note', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json', 'X-Dash-Action': '1' },
        body: JSON.stringify({ key: key, note: note.value })
      }).then(function (res) { return res.json(); }).then(function (res) {
        if (!res.ok) throw new Error(res.error || 'error');
        k.note = res.note; k.note_at = res.at;
        delete state.ktNote[key];
        stat.textContent = res.note ? '저장됨 · ' + res.at : '메모 지움';
      }).catch(function (e) { stat.textContent = '저장 실패: ' + e.message; });
    };
  });
}

/* ── 감사 ─────────────────────────────────────────────────────────────── */
/* 주간 감사(scripts/audit/check_links.py)의 지적 종류 — 무엇을 보고 어떻게 읽는지. */
var AUDIT_KIND = {
  internal_link_broken: { l: '깨진 내부 링크',
    d: '본문의 [표시](/ko/…) 링크가 배포본에서 열리지 않는다. 대상이 초안(published: false)이면 ' +
       '발행 글에서 404 가 나고, EN 링크는 대상의 EN 판이 아직 없을 때 걸린다. 초안끼리의 링크는 ' +
       '세지 않는다. 앵커(#thm8)가 대상 글에 실제로 있는지는 보지 않는다.' },
  fixme_marker: { l: 'FIXME·TODO 표시',
    d: '본문(코드·수식 밖)에 FIXME·TODO·XXX 가 남은 줄. 대개 <!-- TODO: 서지 확인 --> 같은 작성 ' +
       '메모다. HTML 주석이라 화면에는 안 보이지만 손이 덜 간 자리라는 표시다.' },
  permalink_convention: { l: 'permalink 규약 위반',
    d: 'permalink 가 /{언어}/{카테고리}/… 로 시작하지 않는다. 카테고리 구간은 폴더 경로나 ' +
       'frontmatter categories 의 과목 슬러그(하이픈 보존, 예: gromov-witten_theory) 중 하나와 맞으면 된다.' },
  permalink_missing: { l: 'permalink 없음', d: 'frontmatter 에 permalink 가 없는 글.' },
  image_missing: { l: '없는 이미지', d: '본문 ![…](경로) 가 가리키는 파일이 디스크에 없다.' },
  empty_link: { l: '빈 링크', d: '[…]() 처럼 대상이 빈 링크.' },
  placeholder_ref: { l: '##ref 자리표시', d: '작성 중 남긴 ##ref 참조 자리표시.' },
  placeholder_img: { l: 'img 자리표시', d: '![img](img) 같은 이미지 자리표시.' }
};
/* "경로[ (초안)] — 상세" 줄들을 글별로 묶는다. 글은 '[카테고리] 제목'으로, 상세의 링크는 라벨만. */
function auditGrouped(items) {
  var order = [], by = {};
  items.forEach(function (x) {
    var i = x.indexOf(' — ');
    var head = i < 0 ? x : x.slice(0, i), rest = i < 0 ? '' : mdPlain(x.slice(i + 3));
    var draft = / \(초안\)$/.test(head);
    var path = postLabel(head.replace(/ \(초안\)$/, '')) + (draft ? ' (초안)' : '');
    if (!by[path]) { by[path] = []; order.push(path); }
    if (rest) by[path].push(rest);
  });
  return order.map(function (p) {
    return p + by[p].map(function (r) { return '\n  ' + r; }).join('');
  }).join('\n\n');
}
function secAudit(d) {
  var a = d.audit;
  var s = secNode('감사', a ? ago(a.mtime) + ' 갱신' : null);
  var c = el('div', 'cols2'), left = el('div'), right = el('div');
  left.appendChild(h3Help('링크·frontmatter', a ? '주간 cron(일 05:00)의 scripts/audit/check_links.py 결과다. ' +
    '행을 누르면 글·줄 단위 상세가 열린다.\n\n' + Object.keys(AUDIT_KIND).map(function (k) {
      return AUDIT_KIND[k].l + ' — ' + AUDIT_KIND[k].d;
    }).join('\n\n') : ''));
  if (a) {
    var det = a.details || {};
    left.appendChild(table(['종류', { label: '건수', num: true }],
      Object.keys(a.counts).sort(function (x, y) { return a.counts[y] - a.counts[x]; }).map(function (k) {
        var items = det[k] || [], info = AUDIT_KIND[k] || { l: k, d: '' };
        var tr = row([
          { text: info.l, title: k },
          { text: num(a.counts[k]), cls: 'num' }
        ], items.length ? 'clickable' : null);
        if (items.length) {
          tr.onclick = function () {
            openModal(info.l + ' — ' + num(a.counts[k]) + '건',
              (info.d ? info.d + '\n\n' : '') + auditGrouped(items));
          };
        }
        return tr;
      })));
    left.appendChild(el('p', 'hint', a.scanned + '편 검사 · 이슈 있는 글 ' + a.posts_with_issues +
      '편 · ' + ago(a.mtime) + ' 갱신'));
  } else left.appendChild(el('p', 'hint', 'audit-report.md 없음'));
  right.appendChild(h3Help('번역 짝 맞춤', '둘 다 0이면 ko/en 짝이 온전하다. 짝은 같은 카테고리 안에서 ' +
    '날짜 접두사를 뗀 파일 이름으로 맞춘다.'));
  right.appendChild(table(['항목', { label: '건수', num: true }], [
    row([{ text: '발행글 중 EN 없음' }, { text: num(d.stats.missing_en), cls: 'num' }]),
    row([{ text: '고아 EN (ko 없음)' }, { text: num(d.stats.orphan_en), cls: 'num' }])
  ]));
  if ((d.orphan_en || []).length) {
    right.appendChild(el('pre', 'log', d.orphan_en.map(function (o) { return o.label || o.path; }).join('\n')));
  }
  c.appendChild(left); c.appendChild(right); s.appendChild(c);
  /* 의존성 링크 전면 재판정은 폭을 다 쓴다 — 판정 대기·감사·판례 (shadow.js). */
  var sh = el('div', 'sh-wrap');
  sh.appendChild(el('h3', null, '링크 재판정'));
  sh.appendChild(window.secShadow(d));
  s.appendChild(sh);
  return s;
}

/* ── 색인 ─────────────────────────────────────────────────────────────── */
function secIndex(d) {
  var g = d.gsc;
  var s = secNode('색인', g ? num(g.total) + ' URL' : null);
  if (!g) { s.appendChild(el('p', 'hint', 'index-monitor 상태 파일 없음')); return s; }
  var c = el('div', 'cols2'), l = el('div'), r = el('div');
  l.appendChild(h3Help('coverage 분포', 'GSC URL 검사 결과의 coverage 상태별 URL 수다. 매일 03:00 ' +
    'index-monitor 가 일부(배치)를 다시 검사하고, 전체 스윕은 가끔 돈다.'));
  l.appendChild(table(['상태', { label: 'URL', num: true }],
    Object.keys(g.by_coverage).sort(function (x, y) { return g.by_coverage[y] - g.by_coverage[x]; }).map(function (k) {
      return row([{ text: k }, { text: num(g.by_coverage[k]), cls: 'num' }]);
    })));
  l.appendChild(el('p', 'hint', '전체 ' + num(g.total) + ' URL · 마지막 배치 ' + (g.last_batch || '—') +
    ' · 전체 스윕 ' + (g.last_full_sweep || '—')));
  /* 색인 요청 추천 — index-monitor 와 같은 순위 규칙(index_ranking.py)으로 고른
     10건. URL 을 누르면 이동이 아니라 완결된 링크가 클립보드로 복사된다:
     그대로 GSC 검색창에 붙여 넣고 색인 요청을 누르는 흐름. */
  var host = g.host || 'https://math-jh.com';
  var rec = g.recommend || [];
  r.appendChild(h3Help('미색인 — 조치 대상 ' + num(g.actionable) + '건',
    '글을 누르면 그 글의 ' + host + '/… 완결된 주소가 클립보드로 복사된다 — GSC 검색창에 붙여 넣고 ' +
    '색인 요청을 누르면 된다. ' +
    (g.recommend_src === 'batch'
      ? '오늘 03:00 배치(' + (g.last_batch || '—') + ')를 그대로 보여 준다.'
      : g.recommend_src === 'computed'
        ? '오늘 배치가 아직 없어 같은 규칙(index_ranking.py)으로 지금 골랐다.'
        : '추천할 URL이 없다.') +
    ' 전체 조치 대상 ' + num(g.actionable) + '건 중 ' + rec.length + '건이다.'));
  r.appendChild(table(['글 (누르면 주소 복사)', '상태', { label: '이후', num: true }], rec.map(function (u) {
    var tr = row([
      { html: '<button type="button" class="copy-url" title="' + esc(host + u.path) + '">' +
              esc(postLabel(u.path)) + '</button>' },
      { text: (u.coverage || '미검사').replace(' - currently not indexed', ''), cls: 'muted sans' },
      { text: u.since, cls: 'num muted' }
    ]);
    var b = tr.querySelector('button');
    b.onclick = function () { copyText(host + u.path, b); };
    return tr;
  })));
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
  right.appendChild(el('h3', null, '승인 대기 댓글 PR'));
  var cm = d.comment_prs || {};
  var pending = cm.items || [];
  if (cm.error) {
    right.appendChild(el('p', 'hint', 'GitHub PR 조회 실패: ' + cm.error));
  } else if (pending.length) {
    right.appendChild(table(['PR', '제목', { label: '생성', num: true }], pending.slice(0, 10).map(function (x) {
      return row([
        { html: '<a href="' + esc(x.url) + '" target="_blank">#' + esc(x.number) + '</a>' },
        { text: x.title },
        { text: x.created_at ? ago(Date.parse(x.created_at) / 1000) : '—', cls: 'num muted nowrap' }
      ]);
    })));
  } else right.appendChild(el('p', 'hint', '대기 PR 없음'));
  c.appendChild(left); c.appendChild(right); s.appendChild(c);
  return s;
}

/* ── 크론 제어 ─────────────────────────────────────────────────────────── */
/* 정지·재개는 서버의 cron-gate 로만 나간다 — crontab 은 런타임에 건드리지 않는다.
   정지 상태의 정본은 ~/.local/state/cron-pause/<id>.json 이고, 대시보드가 죽어도
   `cron-gate --resume <id>` 로 손으로 풀 수 있다. */
function cronAction(job, btn, action) {
  var was = btn.textContent;
  btn.disabled = true;
  btn.textContent = '…';
  fetch(API + 'cron/' + action, {
    method: 'POST',
    headers: { 'Content-Type': 'application/json', 'X-Dash-Action': '1' },
    body: JSON.stringify({ id: job.id })
  })
    .then(function (r) {
      return r.json().catch(function () { return {}; }).then(function (d) {
        if (!r.ok || !d.ok) throw new Error(d.error || ('HTTP ' + r.status));
        return d;
      });
    })
    .then(function () { load(true); })   /* 서버 상태로 다시 그린다 */
    .catch(function (e) {
      btn.disabled = false;
      btn.textContent = was;
      var w = document.getElementById('cron-err');
      if (w) w.textContent = job.name + ': ' + (e.message || e);
    });
}

/* 크론 표현식을 한국어 문장으로 — 원문은 셀 title 에 남긴다.
   해석하지 못한 꼴은 표현식을 그대로 돌려준다 (틀린 한국어보다 낫다). */
var CRON_DOW = ['일', '월', '화', '수', '목', '금', '토'];
function cronField(f) {
  if (f === '*') return { kind: 'any' };
  var m = /^(\*|(\d+)-(\d+))\/(\d+)$/.exec(f);
  if (m) return { kind: 'step', step: +m[4],
                  from: m[2] === undefined ? null : +m[2],
                  to: m[3] === undefined ? null : +m[3] };
  if (/^\d+(,\d+)*$/.test(f)) return { kind: 'list', values: f.split(',').map(Number) };
  return { kind: 'raw' };
}
function cronText(expr) {
  if (!expr) return '';
  var f = String(expr).trim().split(/\s+/);
  if (f.length !== 5) return expr;
  var mi = cronField(f[0]), hr = cronField(f[1]), dow = cronField(f[4]);
  if (f[2] !== '*' || f[3] !== '*' || mi.kind === 'raw' || hr.kind === 'raw') return expr;
  function p2(n) { return (n < 10 ? '0' : '') + n; }

  /* 요일 한정은 매시/N분 꼴과 섞이면 문장이 길어지기만 한다 — 정시 지정에만 붙인다. */
  var day = '매일';
  if (dow.kind === 'list') {
    day = '매주 ' + dow.values.map(function (d) { return CRON_DOW[d % 7] + '요일'; }).join('·');
  } else if (dow.kind !== 'any') return expr;

  if (hr.kind === 'any') {
    if (dow.kind !== 'any') return expr;
    if (mi.kind === 'any') return '매분';
    if (mi.kind === 'step') {
      return mi.from === null ? mi.step + '분 간격'
        : '매시 ' + p2(mi.from) + '분부터 ' + mi.step + '분 간격';
    }
    return '매시 ' + mi.values.map(function (m) { return p2(m) + '분'; }).join('·');
  }
  if (mi.kind !== 'list' || mi.values.length !== 1) return expr;
  if (hr.kind === 'step') {
    if (dow.kind !== 'any') return expr;
    var firstHour = hr.from === null ? 0 : hr.from;
    return '매일 ' + p2(firstHour) + ':' + p2(mi.values[0]) + '부터 ' + hr.step + '시간 간격';
  }
  return day + ' ' + hr.values.map(function (h) {
    return p2(h) + ':' + p2(mi.values[0]);
  }).join(', ');
}

function systemdTimerText(expr) {
  var m = /^\*-\*-\*\s+(\d{2})\/(\d+):(\d{2}):(\d{2})$/.exec(String(expr || '').trim());
  if (!m) return expr || 'systemd 타이머';
  return '매일 ' + m[1] + ':' + m[3] + '부터 ' + Number(m[2]) + '시간 간격';
}

function secCron(d) {
  var c = d.cron || { items: [], paused: 0 };
  var s = secNode('크론 제어', c.items.length + '개 · 정지 ' + c.paused);
  var rows = c.items.map(function (j) {
    var pauseText = j.userPaused && j.quotaPaused ? '수동+쿼터 정지' :
      (j.quotaPaused ? '쿼터 정지' : '정지됨');
    var tr = row([
      { html: '<span class="dot dot--' + (j.paused ? 'paused' : 'ok') + '"></span>' +
              esc(j.name) + (j.timer ? '<span class="tag">timer</span>' : '') },
      { text: j.timer ? systemdTimerText(j.schedule)
              : (cronText(j.schedule) || (j.missing ? '게이트 없음' : '')),
        title: j.schedule, cls: 'muted nowrap' },
      { text: j.paused ? (j.until ? pauseText + ' · 만료 ' + shortKst(j.until) : pauseText) : '실행 중',
        cls: 'muted' },
      { html: '<span class="cron-actions">' +
              (j.quotaPaused ? '<button data-action="force-resume" class="ghost-btn ghost-btn--force-resume"' +
               (j.missing ? ' disabled' : '') + '>강제재개</button>' : '') +
              '<button data-action="' + (j.userPaused ? 'resume' : 'pause') + '" class="ghost-btn"' +
              (j.missing ? ' disabled' : '') + '>' + (j.userPaused ? '재개' : '정지') + '</button>' +
              '</span>', cls: 'num' }
    ], j.paused ? 'is-paused' : null);
    Array.prototype.forEach.call(tr.querySelectorAll('button[data-action]'), function (btn) {
      if (!j.missing) btn.onclick = function () { cronAction(j, btn, btn.getAttribute('data-action')); };
    });
    return tr;
  });
  s.appendChild(table(['잡', '스케줄', '상태', { label: '', num: true }], rows, 'cron-table'));
  var err = el('p', 'hint', '');
  err.id = 'cron-err';
  err.style.color = 'var(--bad)';
  s.appendChild(err);
  return s;
}

var SECTIONS = {
  drafts: secDrafts,
  translation: secTranslation, audit: secAudit, index: secIndex, activity: secActivity,
  cron: secCron
};
/* 페이지 전체에 걸린 설명 — 제목 줄 오른쪽 끝 '?'. 소제목마다 걸린 설명은 h3Help. */
var PAGE_HELP = {
  drafts: '위는 카테고리별 weight 지도다. 눈금 하나가 글 하나이고, 왼쪽부터 weight 오름차순으로 놓인다. ' +
    '키 큰 금색이 미발행, 낮은 회색이 발행, 위에 검은 띠가 있으면 재번역 대기다. 빈 weight 는 옅은 칸으로, ' +
    '5칸 이상 빈 구간은 ⋯ 하나로 줄인다. 오른쪽 숫자는 미발행 / 전체.\n\n' +
    '행을 누르면 그 카테고리의 미발행 글이 행 아래에 weight 순으로 펼쳐진다(한 번에 한 카테고리, ' +
    '다시 누르면 접힌다). 눈금을 누르면 그 글의 카테고리를 펼치고 그 글을 짚는다. 커서를 올리면 글 이름과 ' +
    'weight 가 뜬다.\n\n아래 목록은 카테고리를 가리지 않고 최근에 고친 미발행 글이다. lint 는 md_lint.py 를 ' +
    '그 글 하나에 돌린 결과를 보인다.',
  cron: '정지는 crontab 을 고치지 않는다 — 각 크론 라인 앞의 cron-gate 가 상태파일을 보고 스킵한다. ' +
    '쿼터 정지 중에는 초록 강제재개와 회색 정지를 함께 쓸 수 있고, 강제재개 권한은 해당 quota reset에서 끝난다. ' +
    'autopush 만 systemd 타이머라 systemctl --user stop 으로 멈추며, 재부팅하면 자동 복귀한다. ' +
    '연구 파이프라인(director·verifier·reporter)은 Pi 대시보드(:8088)에 있다.'
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
  if (PAGE_HELP[rt]) h.appendChild(helpBtn(SECTION_LABEL[rt], PAGE_HELP[rt]));
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
  state.shown = rt;
  var app = document.getElementById('app');
  app.innerHTML = '';
  app.appendChild(masthead(d));
  var shell = el('div', 'shell');
  shell.appendChild(rt ? page(d, rt) : overview(d));
  app.appendChild(shell);
  document.title = (rt ? SECTION_LABEL[rt] + ' — ' : '') + 'Blackbox Dashboard';
}

function load(fresh) {
  Promise.all([
    fetch(API + 'summary' + (fresh ? '?fresh=1' : '')).then(function (r) { return r.json(); }),
    /* KO-TYPOS 수정 체크 — 서버(~/.local/state)에 저장돼 기기 간 공유된다.
       읽기 실패는 치명적이지 않으니 마지막으로 아는 값으로 계속 간다. */
    fetch(API + 'kotypo').then(function (r) { return r.json(); })
      .catch(function () { return state.kotypoDone; })
  ])
    .then(function (rs) {
      var hadData = !!state.data;
      state.data = rs[0];
      indexLabels(state.data);
      state.kotypoDone = rs[1] || {};
      /* 구 저장소(localStorage) 1회 이전 — 서버 도입 전 체크를 살린다. */
      try {
        var old = JSON.parse(localStorage.getItem('dash-kotypo-done') || '{}');
        if (Object.keys(old).length) {
          Object.keys(old).forEach(function (k) { state.kotypoDone[k] = 1; });
          localStorage.removeItem('dash-kotypo-done');
          fetch(API + 'kotypo', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json', 'X-Dash-Action': '1' },
            body: JSON.stringify(state.kotypoDone)
          }).catch(function () { });
        }
      } catch (e) { }
      state.stampErr = false;
      /* 번역 큐는 원문 미리보기 iframe 과 메모 칸이 있어 데이터가 그대로면 다시 그리지 않는다. */
      var sig = tSig(state.data, state.kotypoDone), sameT = sig === state.tSig;
      state.tSig = sig;
      if (route() === 'translation' && hadData && sameT) return;
      if (route() === 'audit' && hadData) {
        /* 감사 페이지의 링크 재판정은 자기 데이터를 따로 읽는다. 다시 그리면 쓰던
           설명이 날아간다. 위쪽 감사 숫자는 주간 갱신이라 처음 그린 값으로 충분하다. */
        return;
      }
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

/* 같은 탭에서 섹션으로 가는 평범한 왼쪽 클릭만 가로채 pushState 로 넘긴다.
   Cmd·Ctrl·Shift·Alt·가운데 클릭과 target 이 붙은 링크는 브라우저 기본 동작(새 탭·새 창)으로 둔다. */
document.addEventListener('click', function (e) {
  if (e.defaultPrevented || e.button !== 0 || e.metaKey || e.ctrlKey || e.shiftKey || e.altKey) return;
  var a = e.target.closest('a[href]');
  if (!a || a.target || a.hasAttribute('download')) return;
  var u = new URL(a.href, location.href);
  if (u.origin !== location.origin || u.search || u.hash) return;
  var to = routeOf(u.pathname);
  if (!to && !/^\/dash\/?$/.test(u.pathname)) return;
  e.preventDefault();
  if (to === route()) return;
  history.pushState(null, '', link(to));
  window.scrollTo(0, 0);
  render();
});
/* 뒤로·앞으로, 그리고 열린 탭에서 hash 주소로 간 경우. 섹션이 그대로면 다시 그리지 않는다. */
function syncRoute() {
  if (hashToPath()) window.scrollTo(0, 0);
  if (route() !== state.shown) render();
}
window.addEventListener('popstate', syncRoute);
window.addEventListener('hashchange', syncRoute);
wireModal();
applyTheme(themeMode());
load(false);
setInterval(function () { load(false); }, 60000);
/* 수집 스탬프의 '몇 초 전'은 렌더 시점에 굳으므로 매초 따로 갱신한다. */
setInterval(function () {
  var st = document.querySelector('.mh__stamp');
  if (st && state.data) st.textContent = stampText(state.data);
}, 1000);
