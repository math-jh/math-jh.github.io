/* 찾아보기 미니 오버레이 — 검색 우선.
 *
 * 최근 글 오버레이(Recent_overlay.js)는 페이지를 통째로 가져와 심지만, 색인은
 * 그 방식이 맞지 않는다: 853항목·450KB 인 데다, innerHTML 로 심은 페이지의
 * <script> 는 실행되지 않아 색인의 검색·스크롤 스파이가 죽는다. 그래서 여기서는
 * /assets/data/terms.json (표제어 + 로케이터만) 을 한 번 받아 검색 결과만 그린다.
 *
 * 트리거: /ko/terms 로 가는 링크(사이드바 '찾아보기' 등).
 *   - 색인 페이지 자신에서는 가로채지 않는다 (거기 검색창이 이미 있다).
 *   - 오버레이 안의 링크('전체 색인 보기')도 가로채지 않는다.
 * 전체 색인 페이지는 그대로 남아 무JS·딥링크(/ko/terms#eigenvector)를 담당한다.
 */
(function () {
  var INDEX_URL = '/ko/terms';
  var DATA_URL = '/assets/data/terms.json';
  var MAX_ROWS = 40;

  var overlay, input, list, terms = null, loading = false;
  var rows = [], sel = -1;

  // 검색 키: 대소문자·수식 껍데기($, \mathfrak{a} → a)를 벗긴다. 색인 페이지의
  // data-search 와 같은 취지지만, 매크로까지 풀어 "a" 로도 \mathfrak{a} 가 잡힌다.
  //
  // NFD 로 분해한 뒤 라틴 결합 부호만 지운다. 두 가지가 동시에 해결된다:
  //   Čech → cech   ("cech" 로 찾힌다)
  //   고윳값 → ㄱㅗㅇㅠㅅ…  (한글은 자모로 남아 "고유" 가 "고윳값" 에 걸린다.
  //   음절 단위로 비교하면 종성이 붙는 순간 못 찾는다.)
  function norm(s) {
    return (s || '')
      .toLowerCase()
      .replace(/\$/g, '')
      .replace(/\\[a-z]+\s*\{([^{}]*)\}/gi, '$1')
      .replace(/\\[a-z]+/gi, '')
      .normalize('NFD')
      .replace(/\p{Mn}/gu, '') // 결합 부호(라틴 액센트)만 제거 — 한글 자모(Lo)는 남는다
      .replace(/\s+/g, ' ')
      .trim();
  }

  function open() {
    if (!overlay) return;
    overlay.classList.add('is--visible');
    overlay.setAttribute('aria-hidden', 'false');
    document.body.classList.add('overflow--hidden'); // 테마의 스크롤 잠금 재사용
    load();
    // 팝업이 그려진 다음 프레임에 포커스 (모바일에서 스크롤 튀는 것 방지)
    requestAnimationFrame(function () { input.focus(); input.select(); });
  }

  function close() {
    if (!overlay) return;
    overlay.classList.remove('is--visible');
    overlay.setAttribute('aria-hidden', 'true');
    document.body.classList.remove('overflow--hidden');
  }

  function load() {
    if (terms || loading) return;
    loading = true;
    fetch(DATA_URL)
      .then(function (r) { return r.json(); })
      .then(function (data) {
        terms = data;
        for (var i = 0; i < terms.length; i++) {
          terms[i]._e = norm(terms[i].e);
          terms[i]._k = norm(terms[i].k);
        }
        loading = false;
        render(); // 로딩 중에 이미 타이핑했을 수 있다
      })
      .catch(function () {
        loading = false;
        list.innerHTML = '<li class="terms-content__hint">용어 목록을 불러오지 못했습니다. ' +
          '<a href="' + INDEX_URL + '">전체 색인</a>을 열어 보세요.</li>';
      });
  }

  // 순위: 표제어 앞머리 일치 > 단어 앞머리 일치 > 아무 데나 포함.
  function score(t, q) {
    if (t._e.indexOf(q) === 0 || t._k.indexOf(q) === 0) return 0;
    if ((' ' + t._e).indexOf(' ' + q) !== -1 || (' ' + t._k).indexOf(' ' + q) !== -1) return 1;
    if (t._e.indexOf(q) !== -1 || t._k.indexOf(q) !== -1) return 2;
    return -1;
  }

  function esc(s) {
    return (s || '').replace(/&/g, '&amp;').replace(/</g, '&lt;').replace(/>/g, '&gt;').replace(/"/g, '&quot;');
  }

  function rowHtml(t) {
    var head = t.p === 'ko'
      ? '<span class="terms-content__alt">' + esc(t.e) + ' · </span><b>' + esc(t.k) + '</b>'
      : '<b>' + esc(t.e) + '</b>' + (t.k ? '<span class="terms-content__alt"> · ' + esc(t.k) + '</span>' : '');
    var locs = '';
    if (t.d) {
      for (var i = 0; i < t.d.length; i++) {
        locs += (i ? ' · ' : '') + '<a href="' + esc(t.d[i][1]) + '">' + esc(t.d[i][0]) + '</a>';
      }
    }
    return '<li class="terms-content__row">' +
      '<a class="terms-content__head" href="' + INDEX_URL + '#' + esc(t.i) + '">' + head + '</a>' +
      '<span class="terms-content__locs">' + locs + '</span></li>';
  }

  function render() {
    var q = norm(input.value);
    sel = -1;
    if (!terms) {
      list.innerHTML = q ? '<li class="terms-content__hint">…</li>' : '';
      return;
    }
    if (!q) {
      list.innerHTML = '<li class="terms-content__hint">용어를 입력하세요. 영문·한글 모두 찾습니다.</li>';
      rows = [];
      return;
    }

    var hits = [];
    for (var i = 0; i < terms.length; i++) {
      var s = score(terms[i], q);
      if (s >= 0) hits.push([s, terms[i]]);
    }
    hits.sort(function (a, b) { return a[0] - b[0] || a[1]._e.localeCompare(b[1]._e); });

    if (!hits.length) {
      list.innerHTML = '<li class="terms-content__hint">일치하는 용어가 없습니다.</li>';
      rows = [];
      return;
    }

    var html = '';
    for (var j = 0; j < hits.length && j < MAX_ROWS; j++) html += rowHtml(hits[j][1]);
    if (hits.length > MAX_ROWS) {
      html += '<li class="terms-content__hint">…그 밖에 ' + (hits.length - MAX_ROWS) + '개. ' +
        '<a href="' + INDEX_URL + '">전체 색인</a>에서 좁혀 보세요.</li>';
    }
    list.innerHTML = html;
    rows = [].slice.call(list.querySelectorAll('.terms-content__row'));
    list.scrollTop = 0;

    // 표제어에 수식이 있는 항목($T_2$-space 등) — KaTeX 가 이미 로드돼 있으면 그린다.
    if (window.renderMathInElement) {
      try {
        renderMathInElement(list, {
          delimiters: [
            { left: '$$', right: '$$', display: false },
            { left: '$', right: '$', display: false }
          ],
          macros: window.KATEX_MACROS,
          strict: false,
          throwOnError: false
        });
      } catch (e) { /* 표제어는 원문 그대로 남는다 */ }
    }
  }

  // 선택 이동. 상태를 [0, n] 으로 옮겨 순환시킨다 (0 = 선택 없음, 1..n = 각 줄).
  function move(d) {
    if (!rows.length) return;
    if (sel >= 0) rows[sel].classList.remove('is--sel');
    var n = rows.length;
    sel = ((sel + 1 + d) % (n + 1) + (n + 1)) % (n + 1) - 1;
    if (sel >= 0) {
      rows[sel].classList.add('is--sel');
      var r = rows[sel].getBoundingClientRect(), box = list.getBoundingClientRect();
      if (r.top < box.top || r.bottom > box.bottom) rows[sel].scrollIntoView({ block: 'nearest' });
    }
  }

  // Enter: 선택된 줄(없으면 첫 줄)의 로케이터로. 로케이터가 없는 항목이면 색인 앵커로.
  function go() {
    var row = rows[sel >= 0 ? sel : 0];
    if (!row) return;
    var link = row.querySelector('.terms-content__locs a') || row.querySelector('.terms-content__head');
    if (link) window.location.href = link.getAttribute('href');
  }

  document.addEventListener('DOMContentLoaded', function () {
    overlay = document.getElementById('terms-overlay');
    if (!overlay) return;
    input = document.getElementById('terms-overlay-input');
    list = document.getElementById('terms-overlay-list');
    if (!input || !list) return;

    // 색인 페이지 자신에서는 오버레이를 걸지 않는다 (그 페이지가 곧 색인이다).
    var here = window.location.pathname.replace(/\/$/, '');
    if (here !== INDEX_URL) {
      var triggers = document.querySelectorAll('a[href$="/ko/terms"], a[href$="/ko/terms/"]');
      for (var i = 0; i < triggers.length; i++) {
        if (triggers[i].closest('#terms-overlay')) continue; // 오버레이 안의 링크는 그대로
        if (triggers[i].hasAttribute('data-no-overlay')) continue; // 실제 페이지로 보내는 링크 (About 본문 등)
        triggers[i].addEventListener('click', function (e) { e.preventDefault(); open(); });
      }
    }

    input.addEventListener('input', render);
    input.addEventListener('keydown', function (e) {
      if (e.key === 'ArrowDown') { e.preventDefault(); move(1); }
      else if (e.key === 'ArrowUp') { e.preventDefault(); move(-1); }
      else if (e.key === 'Enter') { e.preventDefault(); go(); }
    });

    // 닫기: X 버튼 또는 배경 클릭
    overlay.addEventListener('click', function (e) {
      if (e.target === overlay || e.target.closest('.terms-content__close')) close();
    });

    // 닫기: Esc
    document.addEventListener('keyup', function (e) {
      if (e.keyCode === 27 && overlay.classList.contains('is--visible')) close();
    });
  });
})();
