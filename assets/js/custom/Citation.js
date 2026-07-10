/* Citation.js — (로컬 전용) 정리 라벨 클릭 → 교차참조 마크다운 복사.
 *
 * 글을 쓸 때 다른 정의/명제/정리를 인용하기 편하도록, 라벨을 클릭하면 정해진 포맷의
 * 교차참조 문자열을 클립보드에 넣는다:
 *
 *   [\[카테고리\] §글제목, ⁋정의 1](/ko/.../post#def1)
 *
 * production(math-jh.com) 에선 필요 없는 저작 보조 기능이라, 로컬 dev 와
 * preview.math-jh.com(저작용 프리뷰 터널) 에서만 활성화한다.
 *
 * NOTE: theorem-label-splitter.rb 가 라벨 <ins id> 를 <span class="thm-n" id> 으로
 * 쪼개므로 셀렉터는 .thm-n[id] 다(쪼개지지 않은 <ins id> 도 보조로 포함).
 */
document.addEventListener('DOMContentLoaded', function () {
  // 저작용 환경에서만. production(math-jh.com) 에선 no-op.
  var host = location.hostname;
  var AUTHORING =
    host === 'localhost' || host === '127.0.0.1' || host === 'preview.math-jh.com';
  if (!AUTHORING) return;

  // 1. 카테고리 (사이드바 nav 의 구·신 구조 모두 대응)
  var catElem =
    document.querySelector('nav.nav__list a.sidebar_title') ||
    document.querySelector('nav.nav__list a[href] > span.nav__sub-title') ||
    document.querySelector('nav.nav__list span.nav__sub-title');
  var category = catElem ? catElem.textContent.trim() : '';

  // 2. 글 제목
  var h1 = document.querySelector('h1');
  var postTitle = h1 ? h1.textContent.trim() : document.title.replace(/-.*$/, '').trim();

  // 3. 라벨 종류 정규식 (단일 출처: window.THEOREM_KINDS.labels)
  var kinds = (window.THEOREM_KINDS && window.THEOREM_KINDS.labels) || [];
  if (!kinds.length) return; // 어휘가 안 실렸으면 조용히 no-op
  var kindRe = new RegExp(
    '(' + kinds.map(function (k) { return k.replace(/[.*+?^${}()|[\]\\]/g, '\\$&'); }).join('|') + ')\\s*([0-9]+)'
  );

  // 4. 라벨마다 클릭 핸들러
  var labels = document.querySelectorAll('.thm-n[id], ins[id]');
  labels.forEach(function (el) {
    el.style.cursor = 'pointer';

    el.addEventListener('click', function (e) {
      // 종류+번호 추출. 종류 목록은 window.THEOREM_KINDS(=_plugins/fenced_theorem_blocks.rb
      // 의 KIND_MAP, head.html 이 실어 보냄)에서 온다 — 긴 것 우선 정렬이라 '보조정리'가
      // '정리'보다 먼저 매치된다. 예전엔 이 정규식이 목록을 따로 들고 있었고, remark 를
      // '참고'가 아니라 쓰이지도 않는 '주의'로 알고 있어 참고 라벨이 복사되지 않았다.
      var match = el.textContent.match(kindRe);
      if (!match) return;
      var type = match[1];
      var number = match[2];
      var anchor = el.id;
      var pagePath = window.location.pathname;

      var citation = `[\\[${category}\\] §${postTitle}, ⁋${type} ${number}](${pagePath}#${anchor})`;

      function legacyCopy() {
        var ta = document.createElement('textarea');
        ta.value = citation;
        ta.style.position = 'fixed';
        ta.style.opacity = '0';
        document.body.appendChild(ta);
        ta.select();
        document.execCommand('copy');
        document.body.removeChild(ta);
      }

      if (navigator.clipboard && window.isSecureContext) {
        // writeText 는 Promise 라 거부될 수 있다(포커스 없음·권한 등). 조용히
        // 실패하지 않도록 거부 시 execCommand 로 폴백한다.
        navigator.clipboard.writeText(citation).catch(legacyCopy);
      } else {
        legacyCopy();
      }

      // 복사 피드백 (배경 깜빡)
      el.style.transition = 'background 0.2s';
      el.style.background = 'rgba(180,220,255,0.4)';
      setTimeout(function () { el.style.background = ''; }, 400);

      e.stopPropagation();
    });
  });
});
