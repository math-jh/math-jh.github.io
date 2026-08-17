/* 판본 비교기 — 스냅샷(이전) ↔ 워킹트리(현재) 를 구워진 상태로 나란히 본다.
 *
 * 서버가 이미 정렬·마크까지 끝낸 HTML 두 벌을 준다 (pagediff.py). 여기서 하는 일은
 *   (1) 두 pane 에 넣고 각 판본의 매크로로 KaTeX 를 돌리고
 *   (2) data-op 닻으로 스크롤을 맞추고
 *   (3) data-h 로 변경 사이를 오가고
 *   (4) 오른쪽 레일에서 감사 지적에 판정을 찍는 것
 * 뿐이다.
 *
 * 매크로가 판본마다 다를 수 있어(구간 안에 katex-macros.js 변경이 있었다) pane 별로
 * 다른 macros 객체를 넘긴다. 같은 걸 쓰면 옛 본문의 수식이 통째로 빨간 에러가 되어
 * diff 가 아니라 렌더 실패를 보게 된다.
 */
(function () {
  'use strict';

  var $ = function (id) { return document.getElementById(id); };
  var state = {
    old: '', new: '', audit: '', refs: {}, path: '', data: null, posts: [], snaps: [],
    hunk: -1, macros: {}, ops: { l: [], r: [] }, lock: false,
    anchor: null,   // 선택으로 잡은 메모 위치 (인용문 기반)
    notes: []
  };

  // ── 유틸 ────────────────────────────────────────────────────────────────
  function api(path) {
    return fetch('/dash' + path, { credentials: 'same-origin' }).then(function (r) {
      if (!r.ok) {
        return r.text().then(function (t) {
          var msg = t;
          try { msg = JSON.parse(t).error || t; } catch (e) { /* 평문 그대로 */ }
          throw new Error(msg || String(r.status));
        });
      }
      return r.json();
    });
  }
  function post(path, body) {
    return fetch('/dash' + path, {
      method: 'POST', credentials: 'same-origin',
      headers: { 'Content-Type': 'application/json', 'X-Dash-Action': '1' },
      body: JSON.stringify(body)
    }).then(function (r) { return r.json(); });
  }
  function esc(s) {
    return String(s == null ? '' : s).replace(/[&<>"]/g, function (c) {
      return { '&': '&amp;', '<': '&lt;', '>': '&gt;', '"': '&quot;' }[c];
    });
  }
  function loadScript(src) {
    return new Promise(function (res, rej) {
      var s = document.createElement('script');
      s.src = src; s.onload = res; s.onerror = rej;
      document.head.appendChild(s);
    });
  }

  // 판본별 매크로 — katex-macros.js 는 window 전역에 쓰므로 로드 직후 붙잡아 둔다.
  function macrosFor(version) {
    if (state.macros[version]) return Promise.resolve(state.macros[version]);
    return loadScript('/dash/api/compare/macros?v=' + encodeURIComponent(version))
      .then(function () {
        state.macros[version] = {
          macros: Object.assign({}, window.KATEX_MACROS),
          delims: window.KATEX_DELIMITERS
        };
        return state.macros[version];
      });
  }

  // ── 목록 ────────────────────────────────────────────────────────────────
  function loadList() {
    return api('/api/compare/list?old=' + encodeURIComponent(state.old)
               + '&new=' + encodeURIComponent(state.new)
               + '&audit=' + encodeURIComponent(state.audit)).then(function (d) {
      state.posts = d.posts; state.snaps = d.snapshots;
      state.old = state.old || d.old || '';
      state.new = state.new || d.new || 'worktree';
      fillVersions();
      renderList();
      $('list-counts').textContent =
        d.counts.changed + '편 변경 · ' + d.counts.done + '편 검토함 · 개정 중 '
        + d.counts.revising + '편';
    });
  }

  /* 판본 고르개는 임의 ref 를 받는다 — 브랜치·태그·sha·HEAD~3·worktree.
     스냅샷은 sha 로 캐시되므로, 움직이는 브랜치를 골라도 항상 그 시점 커밋으로 굳는다. */
  function fillVersions() {
    var seen = {}, opts = [];
    function add(v, label) {
      if (!v || seen[v]) return;
      seen[v] = 1;
      opts.push('<option value="' + esc(v) + '">' + esc(label) + '</option>');
    }
    add('worktree', '워킹트리 (지금)');
    state.snaps.forEach(function (x) {
      add(x.short, '구움 · ' + (x.committed || '').slice(0, 16).replace('T', ' ')
        + ' · ' + (x.subject || '').slice(0, 40));
    });
    (state.refs.branches || []).forEach(function (b) { add(b, '브랜치'); });
    (state.refs.commits || []).forEach(function (c) {
      add(c.short, (c.committed || '').slice(0, 16).replace('T', ' ') + ' · '
        + (c.subject || '').slice(0, 48));
    });
    $('refs').innerHTML = opts.join('');
    if (document.activeElement !== $('old-ver')) $('old-ver').value = state.old || '';
    if (document.activeElement !== $('new-ver')) $('new-ver').value = state.new || 'worktree';
  }

  /* 고른 판본이 아직 안 구워졌으면 굽기 단추를 낸다. 굽는 동안(≈100초) 폴링한다. */
  function checkVersions() {
    var want = [$('old-ver').value.trim(), $('new-ver').value.trim()].filter(Boolean);
    return Promise.all(want.map(function (v) {
      return api('/api/compare/snapshot?ref=' + encodeURIComponent(v))
        .then(function (st) { return { ref: v, st: st }; })
        .catch(function () { return { ref: v, st: { state: 'unknown' } }; });
    })).then(function (rs) {
      var bad = rs.filter(function (r) { return r.st.state !== 'ready' && r.ref !== 'worktree'; });
      var box = $('build-state');
      if (!bad.length) { box.innerHTML = ''; return true; }
      var b = bad[0];
      if (b.st.state === 'unknown') {
        box.innerHTML = '<span class="cmp-warn">알 수 없는 ref: ' + esc(b.ref) + '</span>';
        return false;
      }
      if (b.st.state === 'running') {
        box.innerHTML = '<span class="cmp-dim">굽는 중 ' + esc(b.st.short.slice(0, 8))
          + ' … (약 100초)</span>';
        setTimeout(function () { checkVersions().then(function (ok) { if (ok) reload(); }); }, 5000);
        return false;
      }
      box.innerHTML = '<button class="cmp-btn" id="do-build">' + esc(b.ref)
        + ' 굽기 (약 100초)</button>';
      $('do-build').onclick = function () {
        post('/api/compare/snapshot', { ref: b.ref }).then(function (r) {
          if (r.state === 'busy') {
            alert('다른 판본을 굽는 중이다 (' + r.short.slice(0, 8) + '). 끝나면 다시 눌러라.');
            return;
          }
          checkVersions();
        });
      };
      return false;
    });
  }

  /* 주소에 상태를 싣는다 — 판본·감사·글을 그대로 북마크하거나 남에게 넘길 수 있게. */
  function syncHash() {
    var q = [];
    if (state.path) q.push('p=' + encodeURIComponent(state.path));
    if (state.audit) q.push('a=' + encodeURIComponent(state.audit));
    if (state.old) q.push('o=' + encodeURIComponent(state.old));
    if (state.new && state.new !== 'worktree') q.push('n=' + encodeURIComponent(state.new));
    location.hash = q.join('&');
  }

  function readHash() {
    var out = {};
    location.hash.replace(/^#/, '').split('&').forEach(function (kv) {
      var i = kv.indexOf('=');
      if (i > 0) out[kv.slice(0, i)] = decodeURIComponent(kv.slice(i + 1));
    });
    return out;
  }

  function reload() {
    state.old = $('old-ver').value.trim();
    state.new = $('new-ver').value.trim() || 'worktree';
    savePrefs();
    loadList().then(function () { if (state.path) loadDiff(state.path); });
  }

  /* 고른 판본 짝·감사는 파이에 남긴다 — 대량 sweep 검토는 같은 두 판본을 며칠 오가므로
     새로고침마다 기본값으로 돌아가면 성가시다. 브라우저 저장소가 아니라 서버에 두어
     기기가 바뀌어도 따라오게 한다 (메모와 같은 방식). */
  function savePrefs() {
    post('/api/compare/prefs', {
      old: state.old, new: state.new, audit: state.audit
    }).catch(function () { /* 저장 실패는 화면을 막지 않는다 */ });
  }

  function visiblePosts() {
    var q = $('q').value.trim().toLowerCase();
    var onlyChanged = $('f-changed').checked;
    var onlyKo = $('f-ko').checked;
    var onlyUndone = $('f-undone').checked;
    var onlyRevising = $('f-revising').checked;
    return state.posts.filter(function (p) {
      if (onlyChanged && !p.changed) return false;
      if (onlyKo && p.lang !== 'ko') return false;
      if (onlyUndone && p.done) return false;
      if (onlyRevising && !p.revising) return false;
      if (q && (p.title + ' ' + p.path).toLowerCase().indexOf(q) < 0) return false;
      return true;
    });
  }

  function renderList() {
    var rows = visiblePosts();
    $('list').innerHTML = rows.map(function (p) {
      var badges = '';
      if (p.open) badges += '<span class="r-badge b-open">잔여 ' + p.open + '</span>';
      if (p.verdict === 'needs_user') badges += '<span class="r-badge b-user">판단</span>';
      if (p.revising) badges += '<span class="r-badge b-rev">개정 중</span>';
      else if (!p.published) badges += '<span class="r-badge">미발행</span>';
      return '<li class="cmp-row' + (p.path === state.path ? ' is-active' : '')
        + (p.done ? ' is-done' : '') + '" data-path="' + esc(p.path) + '">'
        + '<span class="r-title">' + esc(p.title) + badges + '</span>'
        + '<span class="r-meta">' + esc(p.category) + ' · 지적 ' + p.items
        + (p.reviewed ? ' · 판정 ' + p.reviewed : '')
        + (p.changed ? '' : ' · 변경 없음') + '</span></li>';
    }).join('');
  }

  // ── diff 적재 ───────────────────────────────────────────────────────────
  function loadDiff(path) {
    state.path = path;
    renderList();
    syncHash();
    $('left').innerHTML = '<p class="cmp-dim">불러오는 중…</p>';
    $('right').innerHTML = '';
    return api('/api/compare/diff?path=' + encodeURIComponent(path)
      + '&old=' + encodeURIComponent(state.old)
      + '&new=' + encodeURIComponent(state.new || 'worktree')
      + '&audit=' + encodeURIComponent(state.audit))
      .then(function (d) {
        state.data = d;
        return Promise.all([macrosFor(state.old),
                            macrosFor(state.new || 'worktree')]).then(function (m) {
          paint(d, m[0], m[1]);
        });
      })
      .catch(function (e) {
        $('left').innerHTML = '<p class="cmp-warn">' + esc(e.message) + '</p>';
        $('right').innerHTML = '';
      });
  }

  function paint(d, mOld, mNew) {
    var L = $('left'), R = $('right');
    var row = state.posts.filter(function (p) { return p.path === state.path; })[0] || {};
    L.innerHTML = d.left; R.innerHTML = d.right;
    [L, R].forEach(function (el) {
      // 조판 규칙(_page.scss)이 :lang(ko) 로 갈린다 — 양끝맞춤·하이픈이 여기 달렸다.
      el.setAttribute('lang', row.lang || 'ko');
      // 증명은 <details> 라 기본이 접힘이다. 접힌 안쪽 변경이 안 보이면 검토가 샌다.
      el.querySelectorAll('details').forEach(function (x) { x.open = true; });
    });
    try { renderMathInElement(L, opts(mOld)); } catch (e) { /* noop */ }
    try { renderMathInElement(R, opts(mNew)); } catch (e) { /* noop */ }
    // 사이트와 같은 순서: KaTeX 렌더 뒤에 영문 낱말을 lang=en 스팬으로 감싼다.
    if (window.hyphenateLatin) { try { window.hyphenateLatin(L); window.hyphenateLatin(R); } catch (e) { /* noop */ } }

    state.ops.l = Array.prototype.slice.call(L.querySelectorAll('[data-op]'));
    state.ops.r = Array.prototype.slice.call(R.querySelectorAll('[data-op]'));
    state.hunk = -1;

    $('head-l').textContent = '이전 · ' + verLabel(state.old);
    $('head-r').textContent = '이후 · ' + verLabel(state.new) + ' · ' + d.post.permalink;

    var s = d.stats;
    var a = d.audit || {};
    var items = a.items || [];
    // 반영했다는데 그 블록에 변경이 없는 것 = diff 로는 절대 안 보이는 부류.
    var suspects = items.filter(function (i) { return i.suspect; });
    var unmatched = items.filter(function (i) { return i.match === 'unmatched'; });
    $('cmp-stats').innerHTML = '블록 ' + s.blocks_old + '→' + s.blocks_new
      + ' · 변경 <b>' + s.changed + '</b> (수정 ' + s.edited + ' · 추가 ' + s.added
      + ' · 삭제 ' + s.deleted + ')'
      + (items.length ? ' · 지적 ' + items.length + ' (연결 ' + s.linked + ')' : '')
      + (suspects.length
          ? ' <span class="cmp-warn js-suspects">· 미반영 의심 ' + suspects.length + '건</span>'
          : '')
      + (unmatched.length ? ' <span class="cmp-dim">· 인용문 미매칭 ' + unmatched.length + '</span>' : '')
      + (d.source.suspect ? ' <span class="cmp-warn">· 원문과 불일치</span>' : '');
    var sus = document.querySelector('.js-suspects');
    if (sus) sus.onclick = function () { showSuspects(suspects); };
    $('hunk-pos').textContent = s.changed ? '0/' + s.changed : '–';
    $('done-toggle').classList.toggle('is-on', !!d.post.done);

    $('src-body').textContent = d.source.text || '(원문 diff 없음)';
    if (d.source.suspect) showSrc(true);   // 정렬이 깨진 것으로 보이면 정본을 먼저 보여준다

    renderRail(d);
  }

  function verLabel(v) {
    if (!v || v === 'worktree') return '워킹트리 (지금)';
    var s = state.snaps.filter(function (x) { return x.short === v; })[0] || {};
    return v.slice(0, 8) + (s.committed ? ' · ' + s.committed.slice(0, 16).replace('T', ' ') : '')
      + (s.subject ? ' · ' + s.subject.slice(0, 40) : '');
  }

  function opts(m) {
    return {
      delimiters: m.delims, macros: m.macros, strict: false, throwOnError: false
    };
  }

  // ── 스크롤 동기화 ───────────────────────────────────────────────────────
  // data-op 은 양쪽에 다 있는 블록에만 같은 번호로 붙어 있다 (삭제·추가된 블록은
  // 한쪽에만 있다). 그래서 "화면 맨 위 블록의 짝" 을 찾아 그 위치를 맞추면 된다.
  function syncScroll(src, dst, srcOps, dstOps) {
    if (!$('sync').checked || state.lock) return;
    var top = src.getBoundingClientRect().top;
    // 맨 위 블록이 한쪽에만 있는 것(추가·삭제된 블록)이면 짝이 없다. 거기서 포기하면
    // 큰 삽입 주위가 통째로 동기화 사각지대가 된다 — 하필 제일 볼 곳이다.
    // 짝이 있는 다음 닻까지 밀고 나간다.
    var anchor = null, twin = null;
    for (var i = 0; i < srcOps.length && !twin; i++) {
      if (srcOps[i].getBoundingClientRect().bottom <= top + 4) continue;
      var op = srcOps[i].getAttribute('data-op');
      for (var j = 0; j < dstOps.length; j++) {
        if (dstOps[j].getAttribute('data-op') === op) {
          anchor = srcOps[i]; twin = dstOps[j]; break;
        }
      }
    }
    if (!twin) return;
    var delta = anchor.getBoundingClientRect().top - top;
    state.lock = true;
    dst.scrollTop += twin.getBoundingClientRect().top - dst.getBoundingClientRect().top - delta;
    requestAnimationFrame(function () { state.lock = false; });
  }

  // ── 변경 사이 이동 ──────────────────────────────────────────────────────
  function gotoHunk(i) {
    var hs = (state.data && state.data.hunks) || [];
    if (!hs.length) return;
    i = Math.max(0, Math.min(hs.length - 1, i));
    state.hunk = i;
    var id = hs[i].id;
    var sel = '[data-h="' + id + '"]';
    var r = $('right').querySelector(sel), l = $('left').querySelector(sel);
    document.querySelectorAll('.d-blk.is-cur').forEach(function (e) { e.classList.remove('is-cur'); });
    [l, r].forEach(function (e) { if (e) e.classList.add('is-cur'); });
    var primary = r || l;
    var pane = primary === r ? $('right') : $('left');
    state.lock = true;
    pane.scrollTop += primary.getBoundingClientRect().top - pane.getBoundingClientRect().top - 90;
    requestAnimationFrame(function () {
      state.lock = false;
      if (primary === r) syncScroll($('right'), $('left'), state.ops.r, state.ops.l);
      else syncScroll($('left'), $('right'), state.ops.l, state.ops.r);
    });
    $('hunk-pos').textContent = (i + 1) + '/' + hs.length;
  }

  // ── 호버: 이 변경이 왜 생겼는지 ─────────────────────────────────────────
  // 감사 지적은 본문 조각을 수식·인용부호로 집어 말한다. 서버가 그 조각이 실제로
  // 손댄 자리에 나타나는 변경에만 data-item 을 달아 둔다. 못 이은 변경은 숨기지 않고
  // "지적 없는 변경" 으로 보여준다 — 근거 없는 수정이야말로 봐야 할 것이다.
  function tipFor(el) {
    var h = el.getAttribute('data-h');
    if (!h || !state.data) return null;
    var ids = (el.getAttribute('data-item') || '').split(' ').filter(Boolean);
    var items = (state.data.audit.items || []).filter(function (i) {
      return ids.indexOf(i.id) >= 0;
    });
    var head = '<b>변경 #' + esc(h) + '</b>';
    if (!items.length) {
      return head + (state.audit
        ? '<div class="tip-none">이어붙은 감사 지적 없음 — 근거를 직접 확인할 것</div>'
        : '<div class="tip-none cmp-dim">감사를 고르면 이 변경의 근거가 여기 뜬다.</div>');
    }
    return head + items.map(itemCard).join('');
  }

  function itemCard(it) {
    return '<div class="tip-item">'
      + '<span class="rail-id">' + esc(it.id) + '</span>'
      + (it.kind ? '<span class="rail-lines"> ' + esc(it.kind) + '</span>' : '')
      + (it.status ? '<span class="rail-lines"> · ' + esc(it.status) + '</span>' : '')
      + (it.suspect ? '<div class="tip-suspect">' + esc(it.suspect) + '</div>' : '')
      + '<p>' + esc(it.summary || '') + '</p>'
      + (it.fix ? '<p class="rail-fix">수정안: ' + esc(it.fix) + '</p>' : '')
      + (it.resolution ? '<p class="rail-fix">처리: ' + esc(it.resolution) + '</p>' : '')
      // 전문까지 호버에 싣는다 — 레일은 지시를 쓰는 자리라 읽을 것은 여기서 끝내야 한다.
      + (it.detail ? '<div class="tip-detail">' + md(it.detail) + '</div>' : '')
      + '</div>';
  }

  /* 미반영 의심 목록 — 클릭하면 그 블록으로 데려간다. diff 에는 안 보이는 부류라
     따로 꺼내 보여줘야 한다. */
  function showSuspects(items) {
    var html = items.map(function (it) {
      return '<div class="rail-item"><span class="rail-id">' + esc(it.id) + '</span> '
        + '<button class="cmp-btn js-goto" data-op="' + (it.ops[0] != null ? it.ops[0] : '')
        + '">본문에서 보기</button>'
        + '<div class="tip-suspect">' + esc(it.suspect) + '</div>'
        + '<p>' + esc(it.summary || '') + '</p>'
        + (it.quote ? '<div class="note-quote">“' + esc(it.quote) + '”</div>' : '')
        + '</div>';
    }).join('');
    showModal('미반영 의심 ' + items.length + '건', '', html);
    $('modal-body').querySelectorAll('.js-goto').forEach(function (b) {
      b.onclick = function () {
        $('modal').hidden = true;
        gotoOp(b.getAttribute('data-op'));
      };
    });
  }

  function gotoOp(op) {
    if (op === '' || op == null) return;
    var el = $('right').querySelector('[data-op="' + op + '"]')
      || $('left').querySelector('[data-op="' + op + '"]');
    if (!el) return;
    var pane = el.closest('.cmp-doc');
    document.querySelectorAll('.d-blk.is-cur').forEach(function (e) { e.classList.remove('is-cur'); });
    el.classList.add('is-cur');
    state.lock = true;
    pane.scrollTop += el.getBoundingClientRect().top - pane.getBoundingClientRect().top - 90;
    requestAnimationFrame(function () { state.lock = false; });
  }

  /* 감사 전문은 마크다운이다. 문단·강조·제목만 최소로 살린다. */
  function md(text) {
    return esc(text)
      .replace(/^##\s+(.+)$/gm, '<h4>$1</h4>')
      .replace(/\*\*(.+?)\*\*/g, '<b>$1</b>')
      .replace(/`([^`]+)`/g, '<code>$1</code>')
      .replace(/\n\n/g, '<br><br>');
  }

  // 카드는 **표시된 변경 위에서만** 뜬다. 블록 전체(`[data-h]`)를 잡으면 그 문단
  // 어디에 올려도 카드가 떠서, 안 뜨는 곳이 거의 없어진다.
  //   .d-tok               낱말·수식 단위 마크 (수정된 자리)
  //   .d-new / .d-gone     통째 추가·삭제된 블록
  //   .d-atomic            도식·표처럼 안을 쪼개지 않는 블록
  var TIP_SEL = '.d-tok, .d-blk.d-new, .d-blk.d-gone, .d-blk.d-atomic';

  /* 카드가 드래그를 가리면 안 된다 — 문장을 끌어 메모를 다는 게 이 화면의 주된
     동작이라, 누르는 순간 감추고 버튼을 놓을 때까지, 그리고 선택이 살아 있는 동안은
     띄우지 않는다. */
  document.addEventListener('mousedown', function () {
    state.dragging = true;
    $('tip').hidden = true;
  });
  document.addEventListener('mouseup', function () { state.dragging = false; });

  function tipBlocked() {
    if (state.dragging) return true;
    var sel = window.getSelection();
    return !!(sel && !sel.isCollapsed && String(sel).trim());
  }

  function bindTips(pane) {
    pane.addEventListener('mouseover', function (e) {
      if (tipBlocked()) { $('tip').hidden = true; return; }
      var el = e.target.closest(TIP_SEL);
      if (!el) { $('tip').hidden = true; return; }
      var html = tipFor(el);
      if (!html) return;
      var tip = $('tip');
      tip.innerHTML = html;
      tip.hidden = false;
      renderTipMath(tip);
      var r = el.getBoundingClientRect();
      var top = r.bottom + 6, left = Math.min(r.left, window.innerWidth - 380);
      if (top + tip.offsetHeight > window.innerHeight) top = Math.max(8, r.top - tip.offsetHeight - 6);
      tip.style.top = top + 'px';
      tip.style.left = Math.max(8, left) + 'px';
    });
    pane.addEventListener('mouseout', function (e) {
      if (!e.relatedTarget || !e.relatedTarget.closest(TIP_SEL)) $('tip').hidden = true;
    });
  }

  /* 감사 지적문은 블로그 글과 같은 관례로 수식을 적는다($…$). 카드에 날것으로 두면
     읽을 수가 없으므로 본문 pane 과 같은 매크로로 렌더한다. */
  function renderTipMath(tip) {
    var m = state.macros[state.new] || state.macros[state.old];
    if (!m || !window.renderMathInElement) return;
    try { renderMathInElement(tip, opts(m)); } catch (e) { /* noop */ }
  }

  // ── 작업 패널 ───────────────────────────────────────────────────────────
  function renderRail(d) {
    // 작업 패널은 지시서만 담는다. 지적·변경 내용은 호버 카드 몫이다.
    renderNotes(d.notes || []);
  }

  function renderNotes(notes) {
    state.notes = notes;
    $('rail-notes').innerHTML = notes.length
      ? '<div class="cmp-noteshead">메모 ' + notes.length + '건</div>' + notes.map(function (n) {
        var where = [n.heading, n.label].filter(Boolean).join(' · ');
        return '<div class="note' + (n.status === 'done' ? ' is-done' : '') + '" data-id="'
          + esc(n.id) + '">'
          + '<div class="note-loc">' + esc(where || '(글 전체)') + '</div>'
          + (n.quote ? '<div class="note-quote">“' + esc(n.quote) + '”</div>' : '')
          + '<div class="note-text">' + esc(n.text) + '</div>'
          + '<div class="rail-acts">'
          + '<button class="cmp-btn js-note-find">본문에서 찾기</button>'
          + '<button class="cmp-btn js-note-done">' + (n.status === 'done' ? '되돌리기' : '처리함') + '</button>'
          + '<button class="cmp-btn js-note-del">삭제</button>'
          + '</div></div>';
      }).join('')
      : '<div class="cmp-noteshead">메모 없음</div>';
    // 인용문은 소스 그대로 저장하지만(지시서가 그걸로 grep 한다) 읽을 때는 렌더한다.
    renderTipMath($('rail-notes'));
  }

  // ── 임의 위치 메모: 위치는 줄번호가 아니라 인용문으로 잡는다 ─────────────
  // 마크다운을 열지 않고 말로만 지시할 수 있어야 한다. 인용문 + 절 제목 + 정리 라벨이면
  // 받는 쪽이 grep 한 번에 그 자리를 찾는다. 줄번호는 수정 한 번에 어긋난다.
  /* 선택 영역을 **마크다운에 가까운 꼴**로 되돌린다.
     KaTeX 는 MathML 사본(.katex-mathml)을 숨겨 두므로 그냥 toString() 하면 수식이 두 번
     들어가고, 남는 것도 렌더된 글리프라 소스에서 grep 이 안 된다. 각 수식을 TeX 원문
     (annotation)으로 되돌려 놓으면 인용문을 그대로 마크다운에서 찾을 수 있다. */
  function selectionAsSource(sel) {
    var box = document.createElement('div');
    box.appendChild(sel.getRangeAt(0).cloneContents());
    box.querySelectorAll('.katex').forEach(function (k) {
      var tex = k.querySelector('annotation[encoding="application/x-tex"]');
      k.replaceWith(document.createTextNode(tex ? '$' + tex.textContent.trim() + '$' : ''));
    });
    // 병기 첨자(<sub>영문</sub>)는 본문 흐름이 아니므로 인용에서 뺀다.
    box.querySelectorAll('sub').forEach(function (s) { s.remove(); });
    return box.textContent.replace(/[­​]/g, '').replace(/\s+/g, ' ').trim();
  }

  function captureSelection() {
    var sel = window.getSelection();
    if (!sel || sel.isCollapsed) return;
    var node = sel.anchorNode;
    var pane = node && node.parentElement && node.parentElement.closest('.cmp-doc');
    if (!pane) return;
    var quote = selectionAsSource(sel).slice(0, 400);
    if (quote.length < 2) return;
    var blk = node.parentElement.closest('[data-op]');
    var heading = '', label = '';
    if (blk) {
      var lab = blk.querySelector('.thm-n');
      if (lab) label = lab.textContent.trim();
      var prev = blk;
      while ((prev = prev.previousElementSibling)) {
        if (/^H[1-4]$/.test(prev.tagName)) { heading = prev.textContent.trim(); break; }
      }
    }
    state.anchor = {
      side: pane.id === 'left' ? 'old' : 'new',
      heading: heading, label: label, quote: quote
    };
    $('note-loc').innerHTML = '<b>' + esc([heading, label].filter(Boolean).join(' · ') || '(글 전체)')
      + '</b><div class="note-quote">“' + esc(quote) + '”</div>';
    $('note-text').focus();
  }

  function clearAnchor() {
    state.anchor = null;
    $('note-loc').textContent = '본문에서 문장을 끌어 선택하면 그 자리에 메모가 달린다.';
  }

  /* 메모의 인용문을 본문에서 도로 찾아 그 자리로 데려간다 (위치가 줄번호가 아니라
     인용문이므로, 찾기도 문자열로 한다). */
  function findQuote(note) {
    if (!note.quote) return;
    var pane = note.side === 'old' ? $('left') : $('right');
    var needle = note.quote.replace(/\s+/g, ' ').trim().slice(0, 40);
    var blocks = pane.querySelectorAll('[data-op]');
    for (var i = 0; i < blocks.length; i++) {
      if (blocks[i].textContent.replace(/\s+/g, ' ').indexOf(needle) >= 0) {
        document.querySelectorAll('.d-blk.is-cur').forEach(function (e) { e.classList.remove('is-cur'); });
        blocks[i].classList.add('is-cur');
        state.lock = true;
        pane.scrollTop += blocks[i].getBoundingClientRect().top
          - pane.getBoundingClientRect().top - 90;
        requestAnimationFrame(function () { state.lock = false; });
        return;
      }
    }
    alert('이 판본 본문에서 인용문을 못 찾았다 (그 사이 문장이 바뀌었을 수 있다).');
  }

  // ── 원문 diff · 모달 ────────────────────────────────────────────────────
  function showSrc(on) {
    $('src-panel').hidden = !on;
    $('src-toggle').classList.toggle('is-on', on);
  }
  function showModal(title, text, html) {
    $('modal-title').textContent = title;
    $('modal-body').innerHTML = html != null ? html : md(text);
    $('modal').hidden = false;
    renderTipMath($('modal-body'));
  }

  // ── 배선 ────────────────────────────────────────────────────────────────
  function wire() {
    $('list').addEventListener('click', function (e) {
      var row = e.target.closest('.cmp-row');
      if (row) loadDiff(row.getAttribute('data-path'));
    });
    ['q', 'f-changed', 'f-ko', 'f-undone', 'f-revising'].forEach(function (id) {
      $(id).addEventListener('input', renderList);
    });
    ['old-ver', 'new-ver'].forEach(function (id) {
      $(id).addEventListener('change', function () {
        checkVersions().then(function (ok) { if (ok) reload(); });
      });
      $(id).addEventListener('keydown', function (e) {
        if (e.key === 'Enter') { e.preventDefault(); this.blur(); }
      });
    });
    $('apply-vers').addEventListener('click', function () {
      checkVersions().then(function (ok) { if (ok) reload(); });
    });
    $('audit-sel').addEventListener('change', function () {
      state.audit = this.value;
      syncHash();
      savePrefs();
      // 감사에는 대상 판본(base_ref)이 박혀 있다 — 고르면 '이전' 을 그것으로 맞춘다.
      var run = (state.audits || []).filter(function (a) { return a.slug === state.audit; })[0];
      if (run && run.base_ref) $('old-ver').value = run.base_ref.slice(0, 12);
      checkVersions().then(function (ok) { if (ok) reload(); });
    });
    $('next-h').addEventListener('click', function () { gotoHunk(state.hunk + 1); });
    $('prev-h').addEventListener('click', function () { gotoHunk(state.hunk - 1); });
    $('src-toggle').addEventListener('click', function () { showSrc($('src-panel').hidden); });
    $('src-close').addEventListener('click', function () { showSrc(false); });
    $('rail-toggle').addEventListener('click', function () {
      document.querySelector('.cmp-main').classList.toggle('no-rail');
    });
    $('done-toggle').addEventListener('click', function () {
      if (!state.path) return;
      var on = !$('done-toggle').classList.contains('is-on');
      post('/api/review', { kind: 'post', path: state.path, status: on ? 'done' : 'open' })
        .then(function (r) {
          if (!r.ok) return;
          $('done-toggle').classList.toggle('is-on', on);
          var p = state.posts.filter(function (x) { return x.path === state.path; })[0];
          if (p) { p.done = on; renderList(); }
        });
    });

    // ── 메모 ──────────────────────────────────────────────────────────────
    $('note-form').addEventListener('submit', function (e) {
      e.preventDefault();
      var text = $('note-text').value.trim();
      if (!text || !state.path) return;
      var a = state.anchor || {};
      post('/api/review', {
        kind: 'note', path: state.path, text: text,
        side: a.side || 'new', heading: a.heading || '', label: a.label || '',
        quote: a.quote || ''
      }).then(function (r) {
        if (!r.ok) { alert('저장 실패: ' + (r.error || '')); return; }
        $('note-text').value = '';
        clearAnchor();
        renderNotes(r.state.notes.filter(function (n) { return n.path === state.path; }));
      });
    });
    $('note-text').addEventListener('keydown', function (e) {
      if ((e.metaKey || e.ctrlKey) && e.key === 'Enter') {
        e.preventDefault();
        $('note-form').dispatchEvent(new Event('submit', { cancelable: true }));
      }
    });
    $('note-clear').addEventListener('click', clearAnchor);
    function copyInstructions(scope) {
      var q = '?old=' + encodeURIComponent(state.old)
        + '&new=' + encodeURIComponent(state.new || 'worktree')
        + (scope === 'post' ? '&path=' + encodeURIComponent(state.path) : '');
      var btn = scope === 'post' ? $('copy-inst') : $('copy-all');
      fetch('/dash/api/compare/instructions' + q, { credentials: 'same-origin' })
        .then(function (r) { return r.text(); })
        .then(function (t) {
          if (!t.trim()) { alert('아직 넘길 메모가 없다.'); return; }
          navigator.clipboard.writeText(t).then(function () {
            var was = btn.textContent;
            btn.textContent = '복사됨';
            setTimeout(function () { btn.textContent = was; }, 1500);
          }, function () { showModal('지시서', t); });
        });
    }
    $('copy-inst').addEventListener('click', function () { copyInstructions('post'); });
    $('copy-all').addEventListener('click', function () { copyInstructions('all'); });

    $('rail-notes').addEventListener('click', function (e) {
      var box = e.target.closest('.note');
      if (!box) return;
      var id = box.getAttribute('data-id');
      var note = (state.notes || []).filter(function (n) { return n.id === id; })[0] || {};
      if (e.target.classList.contains('js-note-del')) {
        post('/api/review', { kind: 'note-del', id: id, path: state.path })
          .then(function (r) {
            if (r.ok) renderNotes(r.state.notes.filter(function (n) { return n.path === state.path; }));
          });
      } else if (e.target.classList.contains('js-note-done')) {
        post('/api/review', { kind: 'note-done', id: id, path: state.path,
                              status: note.status === 'done' ? 'open' : 'done' })
          .then(function (r) {
            if (r.ok) renderNotes(r.state.notes.filter(function (n) { return n.path === state.path; }));
          });
      } else if (e.target.classList.contains('js-note-find')) {
        findQuote(note);
      }
    });

    $('modal-close').addEventListener('click', function () { $('modal').hidden = true; });
    $('modal').addEventListener('click', function (e) {
      if (e.target === $('modal')) $('modal').hidden = true;
    });

    var L = $('left'), R = $('right');
    L.addEventListener('scroll', function () { syncScroll(L, R, state.ops.l, state.ops.r); });
    R.addEventListener('scroll', function () { syncScroll(R, L, state.ops.r, state.ops.l); });
    bindTips(L); bindTips(R);
    [L, R].forEach(function (pane) {
      pane.addEventListener('mouseup', captureSelection);
    });

    document.addEventListener('keydown', function (e) {
      if (/^(INPUT|TEXTAREA|SELECT)$/.test(e.target.tagName)) return;
      if (e.key === 'n') gotoHunk(state.hunk + 1);
      else if (e.key === 'p') gotoHunk(state.hunk - 1);
      else if (e.key === 'm') { e.preventDefault(); $('note-text').focus(); }
      else if (e.key === 's') showSrc($('src-panel').hidden);
      else if (e.key === 'Escape') { $('modal').hidden = true; showSrc(false); }
      else if (e.key === '[' || e.key === ']') {
        var rows = visiblePosts();
        var at = rows.findIndex(function (p) { return p.path === state.path; });
        var nxt = rows[at + (e.key === ']' ? 1 : -1)];
        if (nxt) loadDiff(nxt.path);
      }
    });
  }

  // ── 시작 ────────────────────────────────────────────────────────────────
  wire();
  Promise.all([
    api('/api/compare/refs').catch(function () { return {}; }),
    api('/api/compare/audits').catch(function () { return []; }),
    api('/api/compare/prefs').catch(function () { return {}; })
  ]).then(function (r) {
    state.refs = r[0] || {};
    state.audits = r[1] || [];
    var saved = r[2] || {};
    $('audit-sel').innerHTML = '<option value="">(없음)</option>'
      + state.audits.map(function (a) {
        return '<option value="' + esc(a.slug) + '">' + esc(a.slug) + ' · '
          + esc(a.title || '') + ' (' + a.posts + '편)</option>';
      }).join('');
    // 기본은 감사 없이 "가장 최근 커밋 ↔ 워킹트리". 구워둔 스냅샷이 있으면 그중
    // 최신을 이전으로 쓴다 (굽는 시간을 안 기다려도 되도록).
    // 우선순위: 주소 해시(남이 보내준 링크) > 지난번에 고른 것 > 기본값
    var h = readHash();
    var snaps = (state.refs.snapshots || []);
    state.audit = h.a || saved.audit || '';
    state.old = h.o || saved.old || (snaps.length ? snaps[0].short : 'HEAD');
    state.new = h.n || saved.new || 'worktree';
    $('audit-sel').value = state.audit;
    fillVersions();
    return checkVersions();
  }).then(function () {
    return loadList();
  }).then(function () {
    var want = readHash().p;
    if (want) loadDiff(want);
  }).catch(function (e) {
    $('left').innerHTML = '<p class="cmp-warn">' + esc(e.message) + '</p>';
  });
})();
