/* 의존성 링크 전면 재판정(섀도 원장)의 사람 쪽 화면 — 감사 페이지(#audit) 아래쪽.
   데이터는 /api/shadow (60초 폴링과 무관하게 이 블록이 직접 읽는다 — 판정 중에
   주기 렌더가 입력 칸을 날리지 않도록 app.js 의 load() 는 감사 페이지를 다시 그리지
   않는다). 동작은 /api/shadow/<동작> POST.
   판정 기준은 scripts/dependency-classifier/criteria.md 한 곳에만 있고, "?" 가 그
   파일을 렌더해 보여 준다 — 프롬프트가 넣는 것과 같은 글이다. */
'use strict';

var SH = {
  data: null, tab: 'queue', busy: false, err: '',
  detail: {},      /* lid → {source_context, target_context} */
  reveal: {},      /* 감사 lid → 서버가 돌려준 공개 정보 */
  note: {},        /* lid·qid → 쓰던 설명 */
  pv: null,        /* 미리보기 중인 링크 (lid·permalink·path·line) */
  modal: null,     /* 근거 모달에 띄운 lid — 문맥이 늦게 와도 그 모달에만 넣는다 */
  pilot: null,     /* /api/shadow/pilot — 판정 대기 아래에 읽기 전용으로 붙인다 */
  pilotAll: false  /* 파일럿에서 만장일치 링크도 보이기 */
};
var SH_REL = { required: '필수', weak: '배경', forward: '예고' };
var SH_TABS = [['queue', '판정 대기'], ['audit', '감사'], ['drafts', '판례 초안'],
               ['book', '판례·쟁점'], ['settled', '최근 판정']];

/* ── 마크다운 (판정 기준·판례 본문용 — 제목·목록·굵게·인라인 코드·문단만) ── */
function shMd(src) {
  var lines = String(src || '').split('\n'), out = [], list = 0, para = [];
  function inline(s) {
    return esc(s).replace(/`([^`]+)`/g, '<code>$1</code>')
      .replace(/\*\*([^*]+)\*\*/g, '<strong>$1</strong>');
  }
  function flush() { if (para.length) { out.push('<p>' + inline(para.join(' ')) + '</p>'); para = []; } }
  function closeTo(d) { while (list > d) { out.push('</ul>'); list--; } }
  lines.forEach(function (ln) {
    var h = ln.match(/^(#{1,6})\s+(.*)$/), li = ln.match(/^(\s*)[-*]\s+(.*)$/);
    if (h) { flush(); closeTo(0); out.push('<h' + Math.min(h[1].length + 1, 6) + '>' + inline(h[2]) +
                                           '</h' + Math.min(h[1].length + 1, 6) + '>'); return; }
    if (li) {
      flush();
      var depth = Math.floor(li[1].length / 2) + 1;
      while (list < depth) { out.push('<ul>'); list++; }
      closeTo(depth);
      out.push('<li>' + inline(li[2]) + '</li>');
      return;
    }
    if (!ln.trim()) { flush(); closeTo(0); return; }
    if (list && /^\s+/.test(ln)) { out[out.length - 1] = out[out.length - 1].replace(/<\/li>$/, ' ' + inline(ln.trim()) + '</li>'); return; }
    closeTo(0);
    para.push(ln.trim());
  });
  flush(); closeTo(0);
  return out.join('\n');
}
function shMath(node) {
  if (window.renderMathInElement) {
    window.renderMathInElement(node, { delimiters: window.KATEX_DELIMITERS, macros: window.KATEX_MACROS,
                                       strict: false, throwOnError: false });
  }
}

/* ── 서버 ─────────────────────────────────────────────────────────────── */
function shPost(action, body) {
  SH.busy = true; SH.err = '';
  return fetch(API + 'shadow/' + action, {
    method: 'POST', headers: { 'Content-Type': 'application/json', 'X-Dash-Action': '1' },
    body: JSON.stringify(body)
  }).then(function (r) { return r.json(); }).then(function (j) {
    SH.busy = false;
    if (!j.ok) { SH.err = j.error || '실패'; shRender(); throw new Error(SH.err); }
    return j;
  }, function (e) { SH.busy = false; SH.err = String(e); shRender(); throw e; });
}
function shLoad() {
  shLoadPilot();
  return fetch(API + 'shadow').then(function (r) { return r.json(); }).then(function (j) {
    if (!j.ok) { SH.err = j.error || '읽기 실패'; } else { SH.data = j; }
    shRender();
  }, function (e) { SH.err = String(e); shRender(); });
}
var SH_LOADING = {};
/* unit 은 큐 밖의 링크(파일럿)일 때만 넘긴다. */
function shDetail(lid, then, unit) {
  if (SH.detail[lid]) { if (then) then(); return; }
  if (SH_LOADING[lid]) return;
  SH_LOADING[lid] = true;
  fetch(API + 'shadow/link?lid=' + encodeURIComponent(lid) + (unit ? '&unit=' + encodeURIComponent(unit) : ''))
    .then(function (r) { return r.json(); })
    .then(function (j) { delete SH_LOADING[lid]; if (j.ok) SH.detail[lid] = j; shRender(); if (then) then(); },
          function () { delete SH_LOADING[lid]; });
}

/* ── 미리보기 ─────────────────────────────────────────────────────────── */
/* 고른 링크가 있는 글을 dev 서버(4001)에서 구워진 채로 오른쪽 칸에 늘 띄우고 그 링크를
   짚는다. 링크 행을 누르면 고르고, 아무것도 안 골랐으면 보이는 목록의 첫 링크를 고른다.
   칸은 #shadow-root 밖에 있어 shRender 가 건드리지 않는다 — 다시 만들면 iframe 이
   글을 처음부터 다시 굽는다. 구워진 글의 <a> 에도 data-lid 가 남아 있어 그걸로
   찾는다. livereload 로 프레임이 다시 뜨면 onload 가 같은 일을 다시 한다. */
function shMark(frame) {
  var k = SH.pv, doc;
  if (!k) return;
  try { doc = frame.contentDocument; } catch (e) { return; }
  if (!doc || !doc.body) return;
  if (!doc.getElementById('dash-hl')) {
    var st = doc.createElement('style');
    st.id = 'dash-hl';
    st.textContent = '.dash-hl{outline:2px solid #b3541e;outline-offset:3px;' +
      'background:rgba(179,84,30,.14)}';
    (doc.head || doc.body).appendChild(st);
  }
  Array.prototype.forEach.call(doc.querySelectorAll('.dash-hl'), function (a) {
    a.classList.remove('dash-hl');
  });
  var hit = doc.querySelector('a[data-lid="' + k.lid + '"]');
  if (!hit) return;
  hit.classList.add('dash-hl');
  /* 프레임 안에서만 스크롤한다 — scrollIntoView 는 바깥 대시보드 페이지까지 끌고 간다. */
  var win = frame.contentWindow;
  win.scrollTo(0, Math.max(0, hit.getBoundingClientRect().top + win.scrollY
                              - win.innerHeight * 0.4));
}
function shPaint() {
  var pane = document.getElementById('sh-preview');
  if (!pane) return;
  var k = SH.pv;
  if (!k) {
    pane.innerHTML = '<p class="hint">왼쪽에서 링크를 고르면 그 링크가 있는 글을 구워진 채로 ' +
      '띄운다. 링크에 마우스를 올리면 가리키는 대상도 보인다.</p>';
    return;
  }
  var frame = pane.querySelector('iframe');
  if (!frame || frame.__permalink !== k.permalink) {
    pane.innerHTML = '';
    var head = el('div', 'sh-pv__head');
    head.appendChild(el('span', 'path'));
    var open = el('a', 'sh-pv__open', '새 탭 ↗');
    open.target = '_blank';
    head.appendChild(open);
    pane.appendChild(head);
    frame = el('iframe', 'sh-pv__frame');
    frame.__permalink = k.permalink;
    /* 글꼴·KaTeX 가 늦게 자리를 잡으면 줄이 밀리므로 조금 뒤 한 번 더 짚는다. */
    frame.onload = function () { shMark(frame); setTimeout(function () { shMark(frame); }, 1200); };
    frame.src = k.permalink;
    pane.appendChild(frame);
  } else {
    shMark(frame);
  }
  pane.querySelector('.path').textContent = String(k.path || '').replace(/^_posts\//, '') + ':' + k.line;
  pane.querySelector('.sh-pv__open').href = k.permalink;
}
/* 고르기는 다시 그리지 않고 표시만 옮긴다 — 다시 그리면 쓰던 설명 칸의 포커스가 날아간다. */
function shSelect(x) {
  if (!x.permalink) return;
  SH.pv = { lid: x.lid, permalink: x.permalink, path: x.path, line: x.line };
  Array.prototype.forEach.call(document.querySelectorAll('#shadow-root .sh-item'), function (r) {
    r.classList.toggle('sh-item--sel', r.dataset.lid === x.lid);
  });
  shPaint();
}
var SH_SEEN = {}, SH_FIRST = null;   /* 한 번 그릴 때 보인 링크들 — 고른 게 사라지면 첫 링크로 */
function shPick(row, x) {
  row.dataset.lid = x.lid;
  if (!x.permalink) return;
  SH_SEEN[x.lid] = true;
  if (!SH_FIRST) SH_FIRST = x;
  row.classList.add('sh-item--pick');
  if (SH.pv && SH.pv.lid === x.lid) row.classList.add('sh-item--sel');
  row.onclick = function (e) {
    if (e.target.closest('button, select, textarea, input, a, label')) return;
    shSelect(x);
  };
}

/* ── 조각 ─────────────────────────────────────────────────────────────── */
function shBtn(label, cls, fn, disabled) {
  var b = el('button', 'ghost-btn' + (cls ? ' ' + cls : ''), label);
  b.disabled = !!disabled || SH.busy;
  b.onclick = fn;
  return b;
}
function shVotes(votes) {
  var w = el('span', 'sh-votes');
  ['S1', 'S2', 'S3'].forEach(function (s) {
    var v = votes && votes[s];
    var c = el('span', 'sh-vote sh-vote--' + (v || 'none'), s + ' ' + (SH_REL[v] || '—'));
    w.appendChild(c);
  });
  return w;
}
function shWhere(x) {
  var w = el('div', 'sh-where');
  w.innerHTML = '<span class="path">' + esc(String(x.path || '').replace(/^_posts\//, '')) +
    '</span><span class="muted">:' + esc(x.line) + '</span> ' +
    (x.decisive ? '<span class="tag tag--drift">화면 영향</span>' : '') +
    (x.same_page ? '<span class="tag">같은 글</span>' : '') +
    (x.kind === 'recheck' ? '<span class="tag">재검토</span>' : '');
  var m = el('div', 'sh-markup', x.markup || '');
  w.appendChild(m);
  return w;
}
function shCtxHtml(lid) {
  var d = SH.detail[lid];
  if (!d) return '<p class="hint">문맥 읽는 중…</p>';
  if (d.gone) return '<p class="hint">이 링크는 글에서 사라졌다.</p>';
  return '<div class="sh-ctx"><div class="sh-ctx__src"><b>소스</b><div>' + esc(d.source_context || '') +
    '</div></div><div class="sh-ctx__tgt"><b>대상 ' + esc(d.target || '') + '</b><div>' +
    esc(d.target_context || '') + '</div></div></div>';
}
function shContext(lid, unit) {
  var box = el('div');
  if (!SH.detail[lid]) { box.appendChild(shBtn('문맥 보기', null, function () { shDetail(lid, null, unit); })); return box; }
  box.innerHTML = shCtxHtml(lid);
  setTimeout(function () { shMath(box); }, 0);
  return box;
}
/* 근거 보기 — 옛 링크 보류 화면의 모달처럼, 링크 문장과 대상, 모델별 판정과 근거를 한 창에.
   문맥은 늦게 올 수 있어 자리만 두고, 그 모달이 아직 열려 있을 때만 채운다. */
function shReasons(x, stages, keys, unit) {
  SH.modal = x.lid;
  shSelect(x);
  openModalHtml('의존성 링크 — ' + String(x.path || '').replace(/^_posts\//, '') + ':' + (x.line || '?'),
    '<div class="sh-m"><p class="sh-m__link"><code>' + esc(x.markup || x.lid) + '</code></p>' +
    '<div id="sh-m-ctx">' + shCtxHtml(x.lid) + '</div>' + shStages(stages, keys).outerHTML + '</div>');
  if (SH.detail[x.lid]) return;
  shDetail(x.lid, function () {
    var box = document.getElementById('sh-m-ctx');
    if (!box || SH.modal !== x.lid || document.getElementById('modal').hidden) return;
    box.innerHTML = shCtxHtml(x.lid);
    shMath(box);
  }, unit);
}
function shStages(stages, keys) {
  var w = el('div', 'sh-stages');
  (keys || ['S1', 'S2', 'S3']).forEach(function (s) {
    var v = stages && stages[s];
    if (!v) return;
    var r = v.step1 || {};
    var c = el('div', 'sh-stage');
    var h = '<div class="sh-stage__h">' + esc(s) + ' ' + esc(v.model) + ' — <b>' + esc(SH_REL[r.relation] || r.relation) + '</b>' +
      ' <span class="muted">필요 ' + esc(r.need || '—') + (r.need_kind ? '(' + esc(r.need_kind) + ')' : '') +
      ' · 제공 ' + esc(r.provided || '—') + (r.preview ? ' · 예고' : '') +
      (r.inconsistent ? ' · <span class="bad">자기모순</span>' : '') + '</span></div>' +
      '<div class="sh-q">“' + esc(r.evidence || '') + '”</div>' +
      '<div>' + esc(r.reason || '') + '</div>';
    if (r.other_side) h += '<div class="muted">반대쪽: ' + esc(r.other_side) + '</div>';
    if (r.flip_condition) h += '<div class="muted">뒤집힐 조건: ' + esc(r.flip_condition) + '</div>';
    if (v.step4) {
      h += '<div class="sh-step4">재검토: <b>' + esc(SH_REL[v.step4.relation] || v.step4.relation) + '</b> · 판례 ' +
        esc(v.step4.precedent) + (v.step4.pending ? ' · 쟁점 ' + esc(v.step4.pending) : '') +
        (v.step4.reason ? '<div>' + esc(v.step4.reason) + '</div>' : '') +
        (v.step4.note ? '<div class="muted">차이 메모: ' + esc(v.step4.note) + '</div>' : '') + '</div>';
    }
    c.innerHTML = h;
    w.appendChild(c);
  });
  setTimeout(function () { shMath(w); }, 0);
  return w;
}
function shNoteBox(key, placeholder) {
  var ta = el('textarea', 'sh-note');
  ta.placeholder = placeholder;
  ta.value = SH.note[key] || '';
  ta.oninput = function () { SH.note[key] = ta.value; };
  return ta;
}

/* ── 판정 대기 ───────────────────────────────────────────────────────── */
function shQueue(d) {
  var frag = document.createDocumentFragment();
  if (!d.human.length) frag.appendChild(el('p', 'hint', '판정을 기다리는 링크가 없다.'));
  var openQs = d.pending || [];
  d.human.forEach(function (g) {
    var box = el('div', 'sh-group');
    var head = el('div', 'sh-group__h');
    if (g.issue) {
      head.innerHTML = '<b>' + esc(g.issue) + '</b> ' + esc(g.description || '') +
        ' <span class="muted">(' + esc(g.question || '?') + ' · ' + g.items.length + '건)</span>';
      var tools = el('span', 'sh-tools');
      tools.appendChild(shBtn('쟁점 보기·고치기', null, function () { shEditIssue(g); }));
      tools.appendChild(shBtn('판례로 등록', null, function () { shRegister(g); }));
      tools.appendChild(shBtn('쟁점 아님(닫기)', null, function () {
        if (confirm(g.issue + ' 을(를) 닫을까?')) shPost('close', { id: g.issue, action: 'dismiss' }).then(shLoad);
      }));
      head.appendChild(tools);
    } else {
      head.innerHTML = '<b>쟁점 없음</b> <span class="muted">(' + g.items.length + '건)</span>';
    }
    box.appendChild(head);
    g.items.forEach(function (x) { box.appendChild(shItem(x, g, openQs)); });
    frag.appendChild(box);
  });
  frag.appendChild(shPilot());
  return frag;
}
function shItem(x, g, openQs) {
  var row = el('div', 'sh-item');
  var top = el('div', 'sh-item__top');
  top.appendChild(shWhere(x));
  top.appendChild(shVotes(x.votes));
  top.appendChild(shBtn('근거 보기', null, function () { shReasons(x, x.stages); }));
  shPick(row, x);
  row.appendChild(top);
  var act = el('div', 'sh-act');
  ['required', 'weak', 'forward'].forEach(function (rel) {
    act.appendChild(shBtn(SH_REL[rel] + ' (' + rel + ')', 'sh-rel sh-rel--' + rel, function () {
      shPost('rule', { lid: x.lid, relation: rel, explanation: SH.note[x.lid] || '' })
        .then(function () { delete SH.note[x.lid]; shLoad(); });
    }));
  });
  var mv = el('select', 'sh-move');
  mv.innerHTML = '<option value="">다른 쟁점으로…</option>' +
    openQs.filter(function (q) { return q.id !== g.issue; }).map(function (q) {
      return '<option value="' + esc(q.id) + '">' + esc(q.id + ' — ' + q.description) + '</option>';
    }).join('') + '<option value="__new">새 쟁점 만들기</option>';
  mv.onchange = function () {
    var v = mv.value;
    if (!v) return;
    if (v === '__new') {
      var question = prompt('어느 질문이 애매한가? (preview / need / provided)', 'provided');
      if (!question) return;
      var statement = prompt('쟁점 진술 (일반형 질문)');
      if (!statement) return;
      var description = prompt('한 줄 설명 (80자 이내)');
      if (!description) return;
      shPost('move', { lid: x.lid, from: g.issue, new: { question: question, statement: statement, description: description } }).then(shLoad);
    } else {
      shPost('move', { lid: x.lid, from: g.issue, to: v }).then(shLoad);
    }
  };
  act.appendChild(mv);
  row.appendChild(act);
  row.appendChild(shNoteBox(x.lid, '설명 (선택) — 쓰면 판정과 함께 digest 로 넘어가 판례 초안이 된다'));
  return row;
}
function shEditIssue(g) {
  var html = '<div class="sh-md">' + shMd(g.body || '') + '</div>';
  openModalHtml(g.issue + ' — ' + (g.description || ''), html);
  var rich = document.getElementById('modal-rich');
  var d = el('input', 'sh-input'); d.value = g.description || ''; d.maxLength = 80;
  var st = el('textarea', 'sh-note'); st.placeholder = '쟁점 진술을 고치려면 여기에 (비우면 그대로)';
  var save = el('button', 'ghost-btn', '저장');
  save.onclick = function () {
    shPost('issue', { id: g.issue, description: d.value, statement: st.value }).then(function () {
      document.getElementById('modal').hidden = true; shLoad();
    });
  };
  var form = el('div', 'sh-form');
  form.appendChild(el('label', null, '한 줄 설명')); form.appendChild(d);
  form.appendChild(el('label', null, '쟁점 진술')); form.appendChild(st);
  form.appendChild(save);
  rich.appendChild(form);
}
function shRegister(g) {
  var ex = prompt(g.issue + ' 을(를) 판례로 등록한다. 판정한 링크만 실린다.\n설명 (선택):', SH.note[g.issue] || '');
  if (ex === null) return;
  shPost('register', { qid: g.issue, explanation: ex }).then(function () {
    alert('digest 대기열에 넣었다. 다음 틱에 초안이 생긴다 (판례 초안 탭).'); shLoad();
  });
}

/* ── 감사 ─────────────────────────────────────────────────────────────── */
function shAudit(d) {
  var frag = document.createDocumentFragment();
  frag.appendChild(el('p', 'hint', '만장일치로 끝난 링크의 표본이다. 모델들의 답은 고른 뒤에 공개된다. ' +
    '만장일치와 다르게 고르면 설명을 써야 판정이 들어간다.'));
  if (!d.audit.length) { frag.appendChild(el('p', 'hint', '감사할 표본이 없다.')); return frag; }
  d.audit.forEach(function (x) {
    var row = el('div', 'sh-item');
    var top = el('div', 'sh-item__top');
    top.appendChild(shWhere(x));
    top.appendChild(el('span', 'tag', x.stratum || ''));
    shPick(row, x);
    row.appendChild(top);
    if (!SH.detail[x.lid]) shDetail(x.lid);
    row.appendChild(shContext(x.lid));
    var rv = SH.reveal[x.lid];
    var act = el('div', 'sh-act');
    ['required', 'weak', 'forward'].forEach(function (rel) {
      act.appendChild(shBtn(SH_REL[rel] + ' (' + rel + ')', 'sh-rel sh-rel--' + rel, function () {
        shPost('audit', { lid: x.lid, relation: rel, explanation: SH.note['a:' + x.lid] || '' }).then(function (j) {
          if (j.need_explanation) { SH.reveal[x.lid] = j.reveal; shRender(); return; }
          delete SH.reveal[x.lid]; delete SH.note['a:' + x.lid];
          SH.err = j.match ? '일치 — ' + x.lid : '반영 — ' + x.lid + ' (digest 로 넘어갔다)';
          shLoad();
        });
      }));
    });
    row.appendChild(act);
    if (rv) {
      var p = el('div', 'sh-reveal');
      p.appendChild(el('p', null, '만장일치 값: ' + (SH_REL[rv.final] || rv.final) + ' — 다르게 고르려면 이유를 쓰고 다시 누른다.'));
      p.appendChild(shStages(rv.stages));
      p.appendChild(shNoteBox('a:' + x.lid, '왜 만장일치가 틀렸는지 (필수)'));
      row.appendChild(p);
    }
    frag.appendChild(row);
  });
  return frag;
}

/* ── 판례 초안 ───────────────────────────────────────────────────────── */
function shDrafts(d) {
  var frag = document.createDocumentFragment();
  if (!d.drafts.length) { frag.appendChild(el('p', 'hint', 'digest 가 만든 초안이 없다.')); return frag; }
  d.drafts.forEach(function (it) {
    var dr = it.draft, job = it.job || {};
    var box = el('div', 'sh-group');
    var label = { 'new': '새 판례', amend: dr.precedent + ' 보강', conflict: dr.precedent + ' 과(와) 충돌', none: '판례 아님' }[dr.action];
    box.appendChild(el('div', 'sh-group__h', it.id + ' — ' + label + ' (' + (job.kind || '') + (job.qid ? ' · ' + job.qid : '') + ')'));
    var ex = el('div', 'sh-q', '사용자 설명: ' + (job.explanation || '(없음)'));
    box.appendChild(ex);
    var fields = {};
    [['description', '한 줄 설명 (80자)'], ['issue', '쟁점'], ['ruling', '판정'], ['reason', '이유'], ['principle', '원칙 초안']].forEach(function (f) {
      box.appendChild(el('label', 'sh-label', f[1]));
      var t = f[0] === 'description' ? el('input', 'sh-input') : el('textarea', 'sh-note');
      t.value = dr[f[0]] || '';
      fields[f[0]] = t;
      box.appendChild(t);
    });
    if (dr.conflict_note) box.appendChild(el('p', 'hint', '충돌: ' + dr.conflict_note));
    box.appendChild(el('p', 'hint', '관계 ' + (dr.relation || '—') + ' · 질문 ' + dr.question +
      ' · 대표 예시 ' + (dr.examples || []).join(', ') + (dr.not_covered ? ' · 해당 없음 ' + dr.not_covered.lid : '')));
    var rc = el('label', 'sh-check');
    var cb = el('input'); cb.type = 'checkbox'; cb.checked = true;
    rc.appendChild(cb);
    rc.appendChild(document.createTextNode(' 다시 볼 후보 ' + (dr.recheck || []).length + '건도 함께 승인'));
    box.appendChild(rc);
    var choice = null;
    if (dr.action === 'conflict') {
      var sel = el('select', 'sh-move');
      sel.innerHTML = '<option value="supersede">기존 판례를 고친다 (새 판례가 대체)</option>' +
        '<option value="distinguish">구별되는 경우로 본다 (기존 판례에 해당 없음 추가)</option>';
      choice = sel;
      box.appendChild(sel);
    }
    var act = el('div', 'sh-act');
    act.appendChild(shBtn('승인', null, function () {
      var edited = {};
      Object.keys(fields).forEach(function (k) { edited[k] = fields[k].value; });
      shPost('draft', { id: it.id, action: 'approve', edited: edited, choice: choice ? choice.value : null,
                        accept_recheck: cb.checked }).then(shLoad);
    }, dr.action === 'none'));
    act.appendChild(shBtn('버리기', null, function () {
      if (confirm(it.id + ' 초안을 버릴까?')) shPost('draft', { id: it.id, action: 'discard' }).then(shLoad);
    }));
    box.appendChild(act);
    (dr.consolidation || []).forEach(function (c) {
      var line = el('div', 'sh-act');
      line.appendChild(el('span', null, '정리안: ' + c.kind + ' ' + (c.ids || []).join(', ') + ' — ' + (c.note || '')));
      line.appendChild(shBtn('적용', null, function () { shPost('consolidate', { kind: c.kind, ids: c.ids }).then(shLoad); }));
      box.appendChild(line);
    });
    frag.appendChild(box);
  });
  return frag;
}

/* ── 판례·쟁점 ───────────────────────────────────────────────────────── */
function shBook(d) {
  var frag = document.createDocumentFragment();
  frag.appendChild(el('h3', null, '판례'));
  if (!d.precedents.length) frag.appendChild(el('p', 'hint', '아직 판례가 없다.'));
  d.precedents.forEach(function (p) {
    var row = el('div', 'sh-item');
    var top = el('div', 'sh-item__top');
    top.innerHTML = '<b>' + esc(p.id) + '</b> <span class="tag">' + esc(p.status) + '</span> ' + esc(p.description) +
      ' <span class="muted">(' + esc(p.question || '') + ' → ' + esc(p.relation || '') + ' · 적용 ' + p.applied +
      ' · 감사 ' + p.audits + (p.audit_errors ? ' · <span class="bad">감사 오류 ' + p.audit_errors + '</span>' : '') + ')</span>';
    row.appendChild(top);
    var act = el('div', 'sh-act');
    act.appendChild(shBtn('본문', null, function () { openModalHtml(p.id, '<div class="sh-md">' + shMd(p.body) + '</div>'); }));
    if (p.status === 'active') {
      act.appendChild(shBtn('한 줄 설명 고치기', null, function () {
        var v = prompt('한 줄 설명 (80자 이내)', p.description);
        if (v) shPost('precedent', { id: p.id, action: 'describe', description: v }).then(shLoad);
      }));
      act.appendChild(shBtn('철회', null, function () {
        if (confirm(p.id + ' 을(를) 철회할까? 이 판례로 판정된 링크는 다시 본다.')) shPost('precedent', { id: p.id, action: 'revoke' }).then(shLoad);
      }));
    }
    row.appendChild(act);
    frag.appendChild(row);
  });
  frag.appendChild(el('h3', null, '열린 판례 대기'));
  if (!d.pending.length) frag.appendChild(el('p', 'hint', '열린 쟁점이 없다.'));
  d.pending.forEach(function (q) {
    var row = el('div', 'sh-item');
    var top = el('div', 'sh-item__top');
    top.innerHTML = '<b>' + esc(q.id) + '</b> ' + esc(q.description) + ' <span class="muted">(' + esc(q.question || '') +
      ' · 링크 ' + q.links.length + ' · ' + esc(q.raised_by || '') + ')</span>';
    row.appendChild(top);
    var act = el('div', 'sh-act');
    act.appendChild(shBtn('본문·고치기', null, function () { shEditIssue({ issue: q.id, description: q.description, body: q.body }); }));
    act.appendChild(shBtn('판례로 등록', null, function () { shRegister({ issue: q.id }); }));
    var into = el('select', 'sh-move');
    into.innerHTML = '<option value="">다른 쟁점에 합치기…</option>' + d.pending.filter(function (o) { return o.id !== q.id; })
      .map(function (o) { return '<option value="' + esc(o.id) + '">' + esc(o.id + ' — ' + o.description) + '</option>'; }).join('');
    into.onchange = function () {
      if (into.value && confirm(q.id + ' 을(를) ' + into.value + ' 에 합칠까?')) shPost('close', { id: q.id, action: 'merge', into: into.value }).then(shLoad);
    };
    act.appendChild(into);
    row.appendChild(act);
    frag.appendChild(row);
  });
  return frag;
}

function shSettled(d) {
  var frag = document.createDocumentFragment();
  if (!d.settled.length) { frag.appendChild(el('p', 'hint', '아직 사람이 내린 판정이 없다.')); return frag; }
  d.settled.forEach(function (x) {
    var row = el('div', 'sh-item');
    var top = el('div', 'sh-item__top');
    top.innerHTML = '<b>' + esc(x.lid) + '</b> → ' + esc(SH_REL[x.relation] || x.relation) +
      ' <span class="muted">(' + esc(x.how === 'audit' ? '감사' : '판정') + ' · ' + ago(x.at) + ')</span>';
    top.appendChild(shBtn('되돌리기', null, function () {
      if (confirm(x.lid + ' 판정을 되돌릴까?')) shPost('reopen', { lid: x.lid }).then(shLoad);
    }));
    shPick(row, x);
    row.appendChild(top);
    if (x.path) row.appendChild(shWhere(x));
    frag.appendChild(row);
  });
  return frag;
}

/* ── 파일럿 ──────────────────────────────────────────────────────────── */
/* 신호 파일럿(shadow_classifier.py --pilot)의 판정 — 판정 대기 아래에 읽기 전용으로 붙인다.
   S1 은 agy 두 번(둘이 갈리면 세 번)의 다수결이고, 그 셋은 근거 보기에서 따로 보인다.
   파일럿은 큐를 쓰지 않으므로 여기서 판정할 것은 없다. 새로 읽기로 갱신한다. */
var SH_PILOT_KEYS = ['S1a', 'S1b', 'S1c', 'S2', 'S3'];
function shLoadPilot() {
  return fetch(API + 'shadow/pilot').then(function (r) { return r.json(); }).then(function (j) {
    if (j.ok) { SH.pilot = j; shRender(); }
  }, function () { });
}
function shPilotItem(x, unit, models) {
  var row = el('div', 'sh-item');
  var top = el('div', 'sh-item__top');
  top.appendChild(shWhere(x));
  top.appendChild(shVotes({ S1: x.s1, S2: x.runs.S2 && x.runs.S2.relation, S3: x.runs.S3 && x.runs.S3.relation }));
  top.appendChild(el('span', 'sh-agy', 'agy ' + ['S1a', 'S1b', 'S1c'].map(function (k) {
    return x.runs[k] ? (SH_REL[x.runs[k].relation] || x.runs[k].relation) : '—';
  }).join('·')));
  top.appendChild(shBtn('근거 보기', null, function () {
    var stages = {};
    SH_PILOT_KEYS.forEach(function (k) { if (x.runs[k]) stages[k] = { model: models[k], step1: x.runs[k] }; });
    shReasons(x, stages, SH_PILOT_KEYS, unit);
  }));
  shPick(row, x);
  row.appendChild(top);
  return row;
}
function shPilot() {
  var frag = document.createDocumentFragment();
  var p = SH.pilot;
  if (!p || !p.posts.length) return frag;
  var s = p.summary;
  frag.appendChild(el('h3', 'sh-sub', '파일럿 (읽기 전용)'));
  frag.appendChild(el('p', 'hint', '글 ' + s.posts + '편 · 링크 ' + s.links + ' · 세 차수가 끝난 링크 ' + s.done +
    ' · 만장일치 ' + s.unanimous + ' (agy 첫 답만 쓰면 ' + s.unanimous_s1a + ')'));
  if (p.last) frag.appendChild(el('p', 'hint', '마지막 기록 ' + p.last));
  (p.quota || []).forEach(function (q) { frag.appendChild(el('p', 'hint', q)); });
  var lab = el('label', 'sh-check');
  var cb = el('input'); cb.type = 'checkbox'; cb.checked = SH.pilotAll;
  cb.onchange = function () { SH.pilotAll = cb.checked; shRender(); };
  lab.appendChild(cb);
  lab.appendChild(document.createTextNode(' 만장일치 링크도 보기'));
  frag.appendChild(lab);
  /* 지금 도는 글이 맨 위에 오도록 최근 것부터. */
  p.posts.slice().reverse().forEach(function (post) {
    var box = el('div', 'sh-group');
    var done = post.links.filter(function (x) { return x.done; });
    var unan = done.filter(function (x) { return x.unanimous; });
    var errs = Object.keys(post.errors || {});
    box.appendChild(el('div', 'sh-group__h', String(post.unit || '').split('+')[0].replace(/^_posts\//, '') +
      ' — 링크 ' + post.links.length + ' · 끝남 ' + done.length + ' · 만장일치 ' + unan.length +
      ' · 돈 차수 ' + post.ran.join(' ') + (errs.length ? ' · 답 없음 ' + errs.join(' ') : '')));
    var shown = post.links.filter(function (x) { return SH.pilotAll || !x.unanimous; })
      .sort(function (a, b) { return (a.unanimous ? 1 : 0) - (b.unanimous ? 1 : 0); });
    if (!shown.length) box.appendChild(el('p', 'hint', '갈린 링크가 없다.'));
    shown.forEach(function (x) { box.appendChild(shPilotItem(x, post.unit, p.models)); });
    frag.appendChild(box);
  });
  return frag;
}

/* ── 페이지 ──────────────────────────────────────────────────────────── */
function shRender() {
  var root = document.getElementById('shadow-root');
  if (!root) return;
  var y = window.scrollY;
  root.innerHTML = '';
  SH_SEEN = {}; SH_FIRST = null;
  var d = SH.data;
  var bar = el('div', 'sh-bar');
  if (d) {
    var p = d.progress, st = p.stages || {};
    bar.innerHTML = '<span>판정 대기 <b>' + p.human + '</b></span><span>감사 <b>' + p.audit + '</b></span>' +
      '<span>초안 <b>' + p.drafts + '</b></span><span>섀도 원장 <b>' + num(p.ledger) + '</b></span>' +
      '<span class="muted">글 ' + p.units + ' · 끝남 ' + (st.done || 0) + ' · S1 대기 ' + (st.S1 || 0) +
      ' · S2 대기 ' + (st.S2 || 0) + ' · S3 대기 ' + (st.S3 || 0) +
      (p.digest ? ' · digest ' + p.digest : '') + (p.recheck ? ' · 재검토 ' + p.recheck : '') + '</span>';
  }
  var help = el('button', 'ghost-btn sh-help', '?');
  help.title = '판정 기준';
  help.onclick = function () { if (d) openModalHtml('판정 기준 (criteria.md)', '<div class="sh-md">' + shMd(d.criteria) + '</div>'); };
  help.onmouseenter = function () {
    if (!d || document.getElementById('sh-pop')) return;
    var pop = el('div', 'sh-pop'); pop.id = 'sh-pop'; pop.innerHTML = '<div class="sh-md">' + shMd(d.criteria) + '</div>';
    help.parentNode.appendChild(pop);
  };
  help.onmouseleave = function () { var p = document.getElementById('sh-pop'); if (p) p.remove(); };
  bar.appendChild(help);
  root.appendChild(bar);
  if (SH.err) root.appendChild(el('p', 'sh-msg', SH.err));
  var tabs = el('div', 'sh-tabs');
  SH_TABS.forEach(function (t) {
    var b = el('button', 'ghost-btn' + (SH.tab === t[0] ? ' sh-tab--on' : ''), t[1]);
    b.onclick = function () { SH.tab = t[0]; SH.err = ''; shRender(); };
    tabs.appendChild(b);
  });
  tabs.appendChild(shBtn('새로 읽기', null, function () { shLoad(); }));
  root.appendChild(tabs);
  if (!d) { root.appendChild(el('p', 'hint', '읽는 중…')); return; }
  if (d.progress.errors && d.progress.errors.length) {
    root.appendChild(el('p', 'sh-msg', '실패한 글: ' + d.progress.errors.map(function (e) { return e.unit.split('+')[0].replace(/^_posts\//, '') + ' — ' + (e.error || '').slice(0, 120); }).join(' / ')));
  }
  var body = el('div', 'sh-body');
  body.appendChild({ queue: shQueue, audit: shAudit, drafts: shDrafts, book: shBook, settled: shSettled }[SH.tab](d));
  root.appendChild(body);
  window.scrollTo(0, y);
  if ((!SH.pv || !SH_SEEN[SH.pv.lid]) && SH_FIRST) shSelect(SH_FIRST);
}

window.secShadow = function () {
  var cols = el('div', 'sh-cols');
  var root = el('div', 'sh');
  root.id = 'shadow-root';
  var pane = el('div', 'sh-pv');
  pane.id = 'sh-preview';
  cols.appendChild(root);
  cols.appendChild(pane);
  setTimeout(function () { shRender(); shPaint(); shLoad(); }, 0);
  return cols;
};
