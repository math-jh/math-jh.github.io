/* Print_fit.js — 인쇄할 때 넓은 디스플레이 수식을 본문 폭에 맞춰 줄인다.
 *
 * 화면에서는 넘치는 수식을 가로 스크롤로 보지만 종이에는 스크롤이 없다. 줄일 비율은
 * 인쇄 레이아웃의 본문 폭으로 정해지는데, beforeprint 시점의 레이아웃은 아직 화면
 * 것이다. 그래서 여기서는 폭과 무관한 값 — 수식의 자연 폭을 수식 글자 크기(em)로 잰
 * 값 — 만 재어 .katex-display 에 --eq-w 로 달고, 실제 축소는 _print.scss 가 인쇄
 * 레이아웃에서 디스플레이 폭(100cqi)을 그 값으로 나눠 정한다.
 */
(function () {
  'use strict';

  var GAP = 0.5; // 수식과 \tag 사이·좌우 여유 (em)

  window.addEventListener('beforeprint', function () {
    document.querySelectorAll('.katex-display > .katex').forEach(function (k) {
      var html = k.querySelector('.katex-html');
      var fs = parseFloat(getComputedStyle(k).fontSize);
      if (!html || !fs) return;
      // .base 는 줄 단위 inline-block 조각, .tag 는 오른쪽 끝에 absolute 로 붙는 번호
      var w = 0;
      for (var i = 0; i < html.children.length; i++) {
        var c = html.children[i];
        if (c.classList.contains('base') || c.classList.contains('tag')) {
          w += c.getBoundingClientRect().width;
        }
      }
      if (w) k.parentNode.style.setProperty('--eq-w', (w / fs + GAP).toFixed(3));
    });
  });
})();
