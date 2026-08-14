/* Xref_preview.js — 정리 상호참조 호버 미리보기.
 *
 * 본문의 #앵커 링크(정의/명제/정리/증명 …을 가리키는 교차참조)에 마우스를 올리면,
 * 그 대상 박스를 작은 카드로 띄운다. 스크롤해서 위로 올라가거나 다른 글로 넘어가지
 * 않고도 무엇을 가리키는지 바로 확인할 수 있다.
 *
 *  - 같은 페이지: 이미 KaTeX 가 렌더된 DOM 박스를 그대로 복제.
 *  - 다른 글: 그 페이지 HTML 을 fetch(캐시)해서 박스를 뽑고 KaTeX 를 재렌더.
 *
 * 읽기 보조 기능이라 production·local 공통으로 동작한다. 순수 vanilla, 의존성 없음.
 */
(function () {
  'use strict';

  // 박스 class 목록의 단일 출처는 _plugins/fenced_theorem_blocks.rb 이고,
  // head.html 이 window.THEOREM_KINDS 로 실어 보낸다. 예전엔 여기 하드코딩돼 있었다.
  var TK = window.THEOREM_KINDS || {};
  var BOX_SEL = (TK.boxes || []).concat(TK.collapsibles || [])
    .map(function (c) { return '.' + c; })
    .join(',') ||
    '.definition,.proposition,.example,.remark,.misc,.proof,.proof--alone,.details';

  // 본문 렌더(scripts.html)와 같은 딜리미터 — 단일 출처 katex-macros.js
  // (head_scripts 에서 이 파일보다 먼저 로드됨. 이중 SoT 감사 [13], 2026-07-22)
  var DELIMS = window.KATEX_DELIMITERS;

  var docCache = {}; // path -> Promise<Document|null>
  var card = null;
  var showT = null;
  var hideT = null;

  function getCard() {
    if (card) return card;
    card = document.createElement('div');
    card.className = 'xref-preview';
    card.addEventListener('mouseenter', function () { clearTimeout(hideT); });
    card.addEventListener('mouseleave', scheduleHide);
    document.body.appendChild(card);
    return card;
  }

  function scheduleHide() {
    clearTimeout(showT);
    hideT = setTimeout(function () {
      if (card) card.classList.remove('is-visible');
    }, 180);
  }

  function boxFrom(doc, id) {
    var el = doc.getElementById(id);
    return el ? el.closest(BOX_SEL) : null;
  }

  function fetchDoc(path) {
    if (!docCache[path]) {
      docCache[path] = fetch(path)
        .then(function (r) { return r.ok ? r.text() : null; })
        .then(function (t) {
          return t ? new DOMParser().parseFromString(t, 'text/html') : null;
        })
        .catch(function () { return null; });
    }
    return docCache[path];
  }

  function renderMath(el) {
    if (typeof window.renderMathInElement === 'function') {
      try {
        window.renderMathInElement(el, {
          delimiters: DELIMS,
          macros: window.KATEX_MACROS,
          strict: false,
          throwOnError: false
        });
      } catch (e) { /* noop */ }
    }
  }

  function present(link, box, needRender) {
    if (!box) return;
    var c = getCard();
    c.innerHTML = box.outerHTML;
    // 복제본의 중복 id 제거 (원본 앵커와 충돌 방지). 단 svg 안은 건드리지 않는다 —
    // 도식 svg 는 <defs> 에 글리프를 두고 <use xlink:href="#…"> 로 참조하므로, id 를
    // 지우면 참조가 전부 끊겨 카드에 아무것도 안 그려진다.
    c.querySelectorAll('[id]').forEach(function (e) {
      if (e.closest('svg')) return;
      e.removeAttribute('id');
    });
    if (needRender) renderMath(c);

    c.classList.add('is-visible');
    // 링크 근처에 배치하되 뷰포트 밖으로 안 나가게 클램프
    var r = link.getBoundingClientRect();
    var cw = c.offsetWidth;
    var ch = c.offsetHeight;
    var left = Math.max(8, Math.min(r.left, window.innerWidth - cw - 12));
    var top = r.bottom + 8;
    if (top + ch > window.innerHeight - 8 && r.top - ch - 8 > 0) {
      top = r.top - ch - 8; // 아래 공간이 부족하면 위로
    }
    c.style.left = left + 'px';
    c.style.top = Math.max(8, top) + 'px';
  }

  function onEnter(e) {
    var a = e.currentTarget;
    var url;
    try {
      url = new URL(a.getAttribute('href'), location.href);
    } catch (_) { return; }
    if (url.origin !== location.origin || !url.hash) return;

    var id = decodeURIComponent(url.hash.slice(1));
    if (!id) return;

    clearTimeout(hideT);
    showT = setTimeout(function () {
      if (url.pathname === location.pathname) {
        present(a, boxFrom(document, id), false); // 같은 페이지: 이미 렌더됨
      } else {
        fetchDoc(url.pathname).then(function (doc) {
          if (doc) present(a, boxFrom(doc, id), true); // 다른 글: 재렌더
        });
      }
    }, 140);
  }

  document.addEventListener('DOMContentLoaded', function () {
    var links = document.querySelectorAll('.page__content a[href*="#"]');
    links.forEach(function (a) {
      a.addEventListener('mouseenter', onEnter);
      a.addEventListener('mouseleave', scheduleHide);
    });
  });
})();
