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

  var BOX_SEL =
    '.definition,.proposition,.example,.remark,.misc,.proof,.proof--alone,.details';

  // _includes/scripts.html 의 본문 렌더 설정과 동일하게 유지할 것.
  var DELIMS = [
    { left: '$$', right: '$$', display: true },
    { left: '$', right: '$', display: false },
    { left: '\\(', right: '\\)', display: false },
    { left: '\\[', right: '\\]', display: true }
  ];

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
    // 복제본의 중복 id 제거 (원본 앵커와 충돌 방지)
    c.querySelectorAll('[id]').forEach(function (e) { e.removeAttribute('id'); });
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
