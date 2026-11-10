/* 의존성 링크 전면 재판정(섀도 원장)의 사람 쪽 화면 — 감사 페이지(#audit) 아래쪽.
   데이터는 /api/shadow (60초 폴링과 무관하게 이 블록이 직접 읽는다 — 판정 중에
   주기 렌더가 입력 칸을 날리지 않도록 app.js 의 load() 는 감사 페이지를 다시 그리지
   않는다). 동작은 /api/shadow/<동작> POST.
   판정 기준은 scripts/dependency-classifier/criteria.md 한 곳에만 있고, "?" 가 그
   파일을 렌더해 보여 준다 — 프롬프트가 넣는 것과 같은 글이다. */
'use strict';

var SH = {
  data: null, tab: 'queue', busy: false, err: '',
  filter: null,    /* 판정 대기의 표결 필터 (SH_FILTERS) */
  reveal: {},      /* 감사 lid → 서버가 돌려준 공개 정보 */
  note: {},        /* lid·qid → 쓰던 설명 */
  pv: null,        /* 미리보기 중인 링크 (lid·permalink·target·소스와 대상의 '[카테고리] 글 제목') */
  after: null,     /* 판정한 링크 바로 아래 lid — 다시 그린 뒤 미리보기를 거기로 옮긴다 */
  pilot: null,     /* /api/shadow/pilot — 판정 대기 아래에 읽기 전용으로 붙인다 */
  pilotAll: false  /* 파일럿에서 만장일치 링크도 보이기 */
};
var SH_REL = { required: '필수', weak: '배경', forward: '예고' };
/* 서버가 링크마다 붙이는 quick 값(shadow_api._quick) — 하나만 고른다. */
var SH_FILTERS = [[null, '전체'], ['unanimous', '세 모델 만장일치'], ['pair', 'Claude·Codex 동의'],
                  ['forward', 'forward가 낀 표결']];
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
    /* 글의 링크 라벨은 `[\[집합론\] §…]`처럼 \[ \] 를 쓰므로 수식 구분자에서 뺀다 —
       글의 display 수식은 $$…$$ 뿐이다. */
    var delims = (window.KATEX_DELIMITERS || []).filter(function (d) { return d.left !== '\\['; });
    window.renderMathInElement(node, { delimiters: delims, macros: window.KATEX_MACROS,
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

/* ── 미리보기 ─────────────────────────────────────────────────────────── */
/* 오른쪽 칸에 고른 링크의 소스 글과 대상을 dev 서버(4001)에서 구워진 채로 위아래로 띄운다.
   위는 소스 글에서 그 링크를, 아래는 대상 글에서 가리키는 박스(앵커가 없으면 글 첫머리)를
   짚는다. 링크 행을 누르면 고르고, 아무것도 안 골랐으면 보이는 목록의 첫 링크를 고른다.
   칸은 #shadow-root 밖에 있어 shRender 가 건드리지 않는다 — 다시 만들면 iframe 이
   글을 처음부터 다시 굽는다. 구워진 글의 <a> 에도 data-lid 가 남아 있어 그걸로
   찾는다. livereload 로 프레임이 다시 뜨면 onload 가 같은 일을 다시 한다. */
function shHit(frame, find) {
  var doc;
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
  var win = frame.contentWindow;
  var hit = find(doc);
  if (!hit) { win.scrollTo(0, 0); return; }
  hit.classList.add('dash-hl');
  /* 프레임 안에서만 스크롤한다 — scrollIntoView 는 바깥 대시보드 페이지까지 끌고 간다. */
  win.scrollTo(0, Math.max(0, hit.getBoundingClientRect().top + win.scrollY
                              - win.innerHeight * 0.3));
}
/* 대상의 주소와 앵커. 같은 글 안의 링크(#thm3)는 소스 글을 다시 띄운다. */
function shTarget(k) {
  var t = String(k.target || '');
  var i = t.indexOf('#');
  return { url: i === 0 ? k.permalink : (i > 0 ? t.slice(0, i) : t),
           anchor: i >= 0 ? decodeURIComponent(t.slice(i + 1)) : '' };
}
function shFindSource(lid) {
  return function (doc) { return doc.querySelector('a[data-lid="' + lid + '"]'); };
}
/* 앵커는 박스 번호(span.thm-n)에 붙어 있다 — 박스 전체를 짚는다. */
function shFindTarget(anchor) {
  return function (doc) {
    var a = anchor && doc.getElementById(anchor);
    return a && (a.closest('.definition, .proposition, .example, .remark, .misc') || a);
  };
}
function shSlot(pane, cls, label, sub, url, find) {
  var slot = pane.querySelector('.' + cls);
  if (!slot) {
    slot = el('div', 'sh-pv__slot ' + cls);
    var head = el('div', 'sh-pv__head');
    head.appendChild(el('span', 'sh-pv__label', label));
    head.appendChild(el('span', 'sh-pv__sub'));
    var open = el('a', 'sh-pv__open', '새 탭 ↗');
    open.target = '_blank';
    head.appendChild(open);
    slot.appendChild(head);
    pane.appendChild(slot);
  }
  slot.querySelector('.sh-pv__open').href = url;
  slot.querySelector('.sh-pv__sub').textContent = sub || '';
  var frame = slot.querySelector('iframe');
  if (!frame || frame.__url !== url) {
    if (frame) frame.remove();
    frame = el('iframe', 'sh-pv__frame');
    frame.__url = url;
    /* 글꼴·KaTeX 가 늦게 자리를 잡으면 줄이 밀리므로 조금 뒤 한 번 더 짚는다. */
    frame.onload = function () {
      shHit(frame, frame.__find);
      setTimeout(function () { shHit(frame, frame.__find); }, 1200);
    };
    frame.src = url;
    slot.appendChild(frame);
  }
  frame.__find = find;
  shHit(frame, find);
}
function shPaint() {
  var pane = document.getElementById('sh-preview');
  if (!pane) return;
  var k = SH.pv;
  if (!k) {
    pane.innerHTML = '<p class="hint">왼쪽에서 링크를 고르면 위에 그 링크가 있는 글을, ' +
      '아래에 링크가 가리키는 대상을 구워진 채로 띄운다.</p>';
    return;
  }
  var hint = pane.querySelector('.hint');
  if (hint) hint.remove();
  shSlot(pane, 'sh-pv__slot--src', '소스', k.sourceLabel, k.permalink, shFindSource(k.lid));
  var t = shTarget(k);
  shSlot(pane, 'sh-pv__slot--tgt', '대상', k.targetLabel, t.url + (t.anchor ? '#' + encodeURIComponent(t.anchor) : ''),
         shFindTarget(t.anchor));
}
/* 고르기는 다시 그리지 않고 표시만 옮긴다 — 다시 그리면 쓰던 설명 칸의 포커스가 날아간다. */
function shSelect(x) {
  if (!x.permalink) return;
  SH.pv = { lid: x.lid, permalink: x.permalink, target: x.target,
            sourceLabel: x.source_label, targetLabel: x.target_label };
  Array.prototype.forEach.call(document.querySelectorAll('#shadow-root .sh-item'), function (r) {
    r.classList.toggle('sh-item--sel', r.dataset.lid === x.lid);
  });
  shPaint();
}
/* 한 번 그릴 때 보인 링크들 — 고른 게 사라지면 판정한 링크 바로 아래 링크로(SH.after),
   그것도 없으면 첫 링크로 */
var SH_SEEN = {}, SH_FIRST = null;
function shPick(row, x) {
  row.dataset.lid = x.lid;
  if (!x.permalink) return;
  SH_SEEN[x.lid] = x;
  if (!SH_FIRST) SH_FIRST = x;
  row.classList.add('sh-item--pick');
  if (SH.pv && SH.pv.lid === x.lid) row.classList.add('sh-item--sel');
  row.onclick = function (e) {
    if (e.target.closest('button, select, textarea, input, a, label')) return;
    shSelect(x);
  };
}
/* 판정 직전 화면에서 그 링크 바로 아래 링크 — 맨 아래였으면 바로 위 링크. 미리보기 중이
   아닌 링크를 판정했으면 null 이라 미리보기는 그대로 남는다. */
function shAfter(lid) {
  if (!SH.pv || SH.pv.lid !== lid) return null;
  var rows = Array.prototype.slice.call(document.querySelectorAll('#shadow-root .sh-item--pick'));
  var i = rows.findIndex(function (r) { return r.dataset.lid === lid; });
  if (i < 0) return null;
  var r = rows[i + 1] || rows[i - 1];
  return r ? r.dataset.lid : null;
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
/* 카드의 이름표는 lid 하나다 — 어디 있는 링크인지는 미리보기가 보여 준다. */
function shId(x) {
  return el('span', 'sh-lid', x.lid);
}
/* 근거 보기 — 모델별 판정과 근거. 링크 문장과 대상은 오른쪽 미리보기에 떠 있다. */
function shReasons(x, stages, keys) {
  shSelect(x);
  openModalHtml('근거 — ' + x.lid, '<div class="sh-m">' + shStages(stages, keys).outerHTML + '</div>');
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
    if (v.recheck) {
      var rc = v.recheck;
      h += '<div class="sh-step4">새 판례 ' + esc(rc.trigger || '') + '로 다시 봄 (표결): <b>' +
        esc(SH_REL[rc.relation] || rc.relation) + '</b> · 판례 ' + esc(rc.precedent || '—') +
        (rc.pending ? ' · 쟁점 ' + esc(rc.pending) : '') +
        (rc.reason ? '<div>' + esc(rc.reason) + '</div>' : '') + '</div>';
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
  /* 표결 필터 — 묶음은 늘 쟁점별이고, 필터는 그 안에서 맞는 링크만 남긴다. */
  var count = {};
  d.human.forEach(function (g) { g.items.forEach(function (x) { if (x.quick) count[x.quick] = (count[x.quick] || 0) + 1; }); });
  var bar = el('div', 'sh-filter');
  SH_FILTERS.forEach(function (f) {
    var b = el('button', 'sh-link' + (SH.filter === f[0] ? ' sh-filter--on' : ''),
               f[1] + (f[0] ? ' ' + (count[f[0]] || 0) : ''));
    b.onclick = function () { SH.filter = f[0]; SH.pv = null; shRender(); };
    bar.appendChild(b);
  });
  frag.appendChild(bar);
  d.human.forEach(function (g) {
    if (SH.filter) g = Object.assign({}, g, { items: g.items.filter(function (x) { return x.quick === SH.filter; }) });
    if (!g.items.length) return;
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
    g.items.forEach(function (x) { box.appendChild(shItem(x, g)); });
    frag.appendChild(box);
  });
  frag.appendChild(shPilot());
  return frag;
}
/* 판정한 링크를 서버 응답을 기다리지 않고 지금 화면에서 뺀다 — 전체 다시 읽기는 뒤따른다. */
function shDrop(lid) {
  var d = SH.data;
  if (!d) return;
  d.human = d.human.map(function (g) {
    return Object.assign({}, g, { items: g.items.filter(function (x) { return x.lid !== lid; }) });
  }).filter(function (g) { return g.items.length; });
  d.progress.human = Math.max(0, d.progress.human - 1);
}
/* 카드: lid·표결·근거 보기 한 줄, 그 아래 설명 칸, 맨 아래 판정 버튼. 설명은 쓰고 나서
   판정을 누르면 판정과 함께 digest 로 넘어간다. */
function shItem(x, g) {
  var row = el('div', 'sh-item');
  var top = el('div', 'sh-item__top');
  top.appendChild(shId(x));
  top.appendChild(shVotes(x.votes));
  var why = el('button', 'sh-link', '근거 보기');
  why.onclick = function () { shReasons(x, x.stages); };
  top.appendChild(why);
  shPick(row, x);
  row.appendChild(top);
  row.appendChild(shNoteBox(x.lid, '설명 (선택)'));
  var act = el('div', 'sh-act');
  ['required', 'weak', 'forward'].forEach(function (rel) {
    act.appendChild(shBtn(SH_REL[rel] + ' (' + rel + ')', 'sh-rel sh-rel--' + rel, function () {
      var after = shAfter(x.lid);
      shPost('rule', { lid: x.lid, relation: rel, explanation: SH.note[x.lid] || '' })
        .then(function () {
          delete SH.note[x.lid]; SH.after = after; shDrop(x.lid); shRender(); shLoad();
        });
    }));
  });
  row.appendChild(act);
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
    top.appendChild(shId(x));
    shPick(row, x);
    row.appendChild(top);
    var rv = SH.reveal[x.lid];
    var act = el('div', 'sh-act');
    ['required', 'weak', 'forward'].forEach(function (rel) {
      act.appendChild(shBtn(SH_REL[rel] + ' (' + rel + ')', 'sh-rel sh-rel--' + rel, function () {
        var after = shAfter(x.lid);
        shPost('audit', { lid: x.lid, relation: rel, explanation: SH.note['a:' + x.lid] || '' }).then(function (j) {
          if (j.need_explanation) { SH.reveal[x.lid] = j.reveal; shRender(); return; }
          delete SH.reveal[x.lid]; delete SH.note['a:' + x.lid];
          SH.err = j.match ? '일치 — ' + x.lid : '반영 — ' + x.lid + ' (digest 로 넘어갔다)';
          SH.after = after;
          shLoad();
        });
      }));
    });
    /* 공개된 뒤에는 설명을 쓰고 아래 버튼을 다시 누르는 순서라 버튼을 맨 아래에 둔다. */
    if (rv) {
      var p = el('div', 'sh-reveal');
      p.appendChild(el('p', null, '만장일치 값: ' + (SH_REL[rv.final] || rv.final) + ' — 다르게 고르려면 이유를 쓰고 다시 누른다.'));
      p.appendChild(shStages(rv.stages));
      p.appendChild(shNoteBox('a:' + x.lid, '왜 만장일치가 틀렸는지 (필수)'));
      row.appendChild(p);
    }
    row.appendChild(act);
    frag.appendChild(row);
  });
  return frag;
}

/* ── 판례 초안 ───────────────────────────────────────────────────────── */
/* 판례 초안 — 초안 하나가 카드 하나다. 한 줄 설명과 원칙 초안만 펴 두고 쟁점·판정·이유는
   "본문 보기"로 연다. 초안 글은 digest 가 쓴 그대로 승인한다(고칠 칸을 두지 않는다).
   정리안(승격·병합)은 초안마다 따로 붙어 오지만 초안과 무관하게 적용되므로 아래 한 묶음으로
   모아 판정 대기 카드와 같은 꼴로 보인다. */
var SH_DRAFT_KIND = { 'new': '새 판례', amend: '보강', conflict: '충돌', none: '판례 아님', merge: '병합' };
function shDraftCard(it) {
  var dr = it.draft;
  var row = el('div', 'sh-item');
  var top = el('div', 'sh-item__top');
  var what = SH_DRAFT_KIND[dr.action] || dr.action;
  if (dr.action === 'amend' || dr.action === 'conflict') what = dr.precedent + ' ' + what;
  if (dr.action === 'merge') what = dr.precedent + ' 에 ' + (dr.merged || []).join(', ') + ' ' + what;
  top.appendChild(el('span', 'sh-lid', what));
  top.appendChild(el('span', 'sh-vote sh-vote--' + (dr.relation || 'none'), SH_REL[dr.relation] || ''));
  var body = el('button', 'sh-link', '본문 보기');
  body.onclick = function () {
    var md = '## 쟁점\n' + (dr.issue || '') + '\n\n## 판정\n' + (dr.ruling || '') + '\n\n## 이유\n' + (dr.reason || '');
    openModalHtml(it.id + ' — ' + (dr.description || ''), '<div class="sh-md">' + shMd(md) + '</div>');
    shMath(document.getElementById('modal'));
  };
  top.appendChild(body);
  row.appendChild(top);
  row.appendChild(el('p', 'sh-draft__desc', dr.description || ''));
  if (dr.principle) row.appendChild(el('p', 'sh-draft__p', dr.principle));
  if (dr.conflict_note) row.appendChild(el('p', 'hint', '충돌: ' + dr.conflict_note));
  if (dr.note) row.appendChild(el('p', 'hint', '병합: ' + dr.note));
  var act = el('div', 'sh-act');
  var cb = null;
  if ((dr.recheck || []).length) {
    var rc = el('label', 'sh-act__check');
    cb = el('input'); cb.type = 'checkbox'; cb.checked = true;
    rc.appendChild(cb);
    rc.appendChild(document.createTextNode(' 다시 볼 후보 ' + dr.recheck.length + '건도 함께'));
    act.appendChild(rc);
  }
  var choice = null;
  if (dr.action === 'conflict') {
    choice = el('select');
    choice.innerHTML = '<option value="supersede">기존 판례를 새 판례로 대체</option>' +
      '<option value="distinguish">구별되는 경우로 보고 기존 판례에 해당 없음 추가</option>';
    act.appendChild(choice);
  }
  act.appendChild(shBtn('버리기', null, function () {
    if (confirm(it.id + ' 초안을 버릴까?')) shPost('draft', { id: it.id, action: 'discard' }).then(shLoad);
  }));
  act.appendChild(shBtn('승인', null, function () {
    shPost('draft', { id: it.id, action: 'approve', edited: null, choice: choice ? choice.value : null,
                      accept_recheck: cb ? cb.checked : false }).then(function (j) {
      var bad = j.consolidation_failed || [];
      SH.err = bad.length ? '정리안 적용 실패 — ' + bad.map(function (c) {
        return c.kind + ' ' + (c.ids || []).join('+') + ': ' + c.error; }).join(' / ') : '';
      shLoad();
    });
  }, dr.action === 'none'));
  row.appendChild(act);
  return row;
}
/* 정리안 카드 — 승격은 설명 없이, 병합만 이유 한 줄을 단다. */
function shConsolidationCard(c) {
  var row = el('div', 'sh-item');
  var top = el('div', 'sh-item__top');
  var ids = (c.ids || []).join(' + ');
  top.appendChild(el('span', 'sh-lid', c.kind === 'promote' ? ids + ' 승격' : ids + ' 병합'));
  row.appendChild(top);
  var go = shBtn('적용', null, function () { shPost('consolidate', { kind: c.kind, ids: c.ids }).then(shLoad); });
  /* 승격은 이름표뿐이라 버튼을 같은 줄 오른쪽에 둔다. */
  if (c.kind === 'promote' || !c.note) {
    go.classList.add('sh-top__end');
    top.appendChild(go);
    return row;
  }
  row.appendChild(el('p', 'sh-draft__p', c.note));
  var act = el('div', 'sh-act');
  act.appendChild(go);
  row.appendChild(act);
  return row;
}
function shDrafts(d) {
  var frag = document.createDocumentFragment();
  if (!d.drafts.length) { frag.appendChild(el('p', 'hint', 'digest 가 만든 초안이 없다.')); return frag; }
  var box = el('div', 'sh-group');
  var head = el('div', 'sh-group__h');
  head.innerHTML = '<b>판례 초안</b> <span class="muted">(' + d.drafts.length + '건)</span>';
  box.appendChild(head);
  d.drafts.forEach(function (it) { box.appendChild(shDraftCard(it)); });
  frag.appendChild(box);
  /* 같은 정리안이 여러 초안에 실려 올 수 있다 — 종류와 대상이 같으면 하나로 센다. */
  var seen = {}, props = [];
  d.drafts.forEach(function (it) {
    (it.draft.consolidation || []).forEach(function (c) {
      var key = c.kind + ':' + (c.ids || []).join(',');
      if (!seen[key]) { seen[key] = true; props.push(c); }
    });
  });
  if (props.length) {
    var pbox = el('div', 'sh-group');
    var h = el('div', 'sh-group__h');
    h.innerHTML = '<b>정리안</b> <span class="muted">(' + props.length + '건 · 초안을 승인하면 함께 적용된다)</span>';
    pbox.appendChild(h);
    props.sort(function (a, b) { return (a.kind === 'promote' ? 0 : 1) - (b.kind === 'promote' ? 0 : 1); });
    props.forEach(function (c) { pbox.appendChild(shConsolidationCard(c)); });
    frag.appendChild(pbox);
  }
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
      ' <span class="muted">(' + esc({ audit: '감사', tiebreak: 'Fable 판정' }[x.how] || '판정') + ' · ' + ago(x.at) + ')</span>';
    top.appendChild(shBtn('되돌리기', null, function () {
      if (confirm(x.lid + ' 판정을 되돌릴까?')) shPost('reopen', { lid: x.lid }).then(shLoad);
    }));
    shPick(row, x);
    row.appendChild(top);
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
  top.appendChild(shId(x));
  top.appendChild(shVotes({ S1: x.s1, S2: x.runs.S2 && x.runs.S2.relation, S3: x.runs.S3 && x.runs.S3.relation }));
  top.appendChild(el('span', 'sh-agy', 'agy ' + ['S1a', 'S1b', 'S1c'].map(function (k) {
    return x.runs[k] ? (SH_REL[x.runs[k].relation] || x.runs[k].relation) : '—';
  }).join('·')));
  var why = el('button', 'sh-link', '근거 보기');
  why.onclick = function () {
    var stages = {};
    SH_PILOT_KEYS.forEach(function (k) { if (x.runs[k]) stages[k] = { model: models[k], step1: x.runs[k] }; });
    shReasons(x, stages, SH_PILOT_KEYS);
  };
  top.appendChild(why);
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
  /* SH.after 는 쓸 때만 비운다 — 파일럿 읽기가 먼저 끝나 옛 데이터로 한 번 더 그려도 남도록. */
  if (!SH.pv || !SH_SEEN[SH.pv.lid]) {
    var next = (SH.after && SH_SEEN[SH.after]) || SH_FIRST;
    SH.after = null;
    if (next) {
      shSelect(next);
      /* 새로 고른 카드가 화면 밖이면 그 카드까지만 스크롤한다 — 화면 안이면 그대로 둔다. */
      var row = document.querySelector('#shadow-root .sh-item--sel');
      if (row) {
        var b = row.getBoundingClientRect();
        if (b.top < 0 || b.bottom > window.innerHeight) row.scrollIntoView({ block: 'center' });
      }
    }
  }
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

/* 고른 링크의 판정 단축키 — r 필수, w 배경, f 예고. 설명 칸·입력 칸에 쓰는 중이거나
   수정키를 같이 누르면 듣지 않는다. 고른 행의 버튼을 그대로 누르므로 동작은 버튼과 같다. */
document.addEventListener('keydown', function (e) {
  var rel = { r: 'required', w: 'weak', f: 'forward' }[e.key];
  if (!rel || e.ctrlKey || e.metaKey || e.altKey || e.repeat) return;
  if (e.target.closest && e.target.closest('input, textarea, select, [contenteditable]')) return;
  var row = document.querySelector('#shadow-root .sh-item--sel');
  var btn = row && row.querySelector('.sh-rel--' + rel);
  if (!btn || btn.disabled) return;
  e.preventDefault();
  btn.click();
});
