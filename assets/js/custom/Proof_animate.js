/* Proof_animate.js — 증명 블록 펼침/접힘 애니메이션 + QED 표식 이동·회전.
 *
 * 네이티브 <details> 는 즉시 튀어나와서, 박스 높이를 직접 애니메이트한다. 그러면
 * 내용이 부드럽게 드러나는 동안 QED 표식이 같은 박자로 회전하며 본문 끝으로 미끄러진다.
 *
 *  - 접힘: summary("증명") 오른쪽에 마름모(45°)로 대기.
 *  - 펼침: 회전(→정사각형)하며 우하단 끝으로 이동.
 *
 * 표식(.qed-mark)은 summary 의 자식이라 접혔을 때도 렌더되지만 .proof 기준 absolute 다.
 * 높이는 Web Animations API, 회전은 CSS(.qed-open 클래스), 위치는 top transition — 셋이
 * 같은 길이로 맞물린다. .qed-open 은 펼침·접힘 모두 애니메이션 *시작*에 토글하므로,
 * [open](=내용 삽입)이 접힘에서는 끝에야 제거돼도 회전은 접힘과 함께 매끄럽게 돈다.
 * prefers-reduced-motion 이면 애니메이션 없이 네이티브 토글만.
 */
(function () {
  'use strict';

  var DUR = 300;
  var reduce =
    window.matchMedia && window.matchMedia('(prefers-reduced-motion: reduce)').matches;

  function markTop(d, summary, mark, open) {
    var markH = mark.offsetHeight || 10;
    if (open) {
      var cs = getComputedStyle(d);
      return (
        d.offsetHeight -
        (parseFloat(cs.borderBottomWidth) || 0) -
        (parseFloat(cs.paddingBottom) || 0) -
        markH
      );
    }
    return summary.offsetTop + (summary.offsetHeight - markH) / 2;
  }

  function snap(mark, top) {
    var prev = mark.style.transition;
    mark.style.transition = 'none';
    mark.style.top = top + 'px';
    void mark.offsetHeight; // reflow
    mark.style.transition = prev || '';
  }

  function collapsedHeight(d, summary) {
    var cs = getComputedStyle(d);
    return (
      summary.offsetHeight +
      (parseFloat(cs.paddingTop) || 0) +
      (parseFloat(cs.paddingBottom) || 0) +
      (parseFloat(cs.borderTopWidth) || 0) +
      (parseFloat(cs.borderBottomWidth) || 0)
    );
  }

  function setup(d) {
    var summary = d.querySelector('summary');
    if (!summary) return;

    var mark = document.createElement('span');
    mark.className = 'qed-mark';
    summary.appendChild(mark);

    requestAnimationFrame(function () {
      d.classList.toggle('qed-open', d.open); // 초기 회전 상태
      snap(mark, markTop(d, summary, mark, d.open));
    });

    if (!reduce) {
      summary.addEventListener('click', function (e) {
        e.preventDefault();
        if (d.dataset.anim) return;
        d.dataset.anim = '1';
        d.style.overflow = 'hidden';

        if (!d.open) {
          var startH = d.offsetHeight;
          d.open = true; // 내용 삽입
          d.classList.add('qed-open'); // 회전 시작 (높이와 동기)
          var endH = d.offsetHeight;
          mark.style.top = markTop(d, summary, mark, true) + 'px'; // 끝으로 glide
          play(d, startH, endH);
        } else {
          var fromH = d.offsetHeight;
          var toH = collapsedHeight(d, summary);
          mark.style.top = markTop(d, summary, mark, false) + 'px'; // summary 로 glide
          d.classList.remove('qed-open'); // 회전 시작 (접힘과 동기); [open] 은 끝에서 제거
          play(d, fromH, toH, function () {
            d.open = false;
            snap(mark, markTop(d, summary, mark, false));
          });
        }
      });
    }

    // reduced-motion: 네이티브 토글만, 위치는 스냅
    d.addEventListener('toggle', function () {
      if (reduce) {
        d.classList.toggle('qed-open', d.open);
        snap(mark, markTop(d, summary, mark, d.open));
      }
    });

    var rt;
    window.addEventListener('resize', function () {
      clearTimeout(rt);
      rt = setTimeout(function () {
        if (!d.dataset.anim) snap(mark, markTop(d, summary, mark, d.open));
      }, 120);
    });

    function play(el, from, to, done) {
      var a = el.animate(
        [{ height: from + 'px' }, { height: to + 'px' }],
        { duration: DUR, easing: 'ease' }
      );
      a.onfinish = a.oncancel = function () {
        el.style.overflow = '';
        el.style.height = '';
        delete el.dataset.anim;
        if (done) done();
      };
    }
  }

  document.addEventListener('DOMContentLoaded', function () {
    document.querySelectorAll('details.proof, details.proof--alone').forEach(setup);
  });
})();
