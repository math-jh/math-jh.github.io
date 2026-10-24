/* Print_fit.js — 인쇄 직전에 화면 DOM 을 종이 조판에 맞게 손본다 (스타일은 _print.scss).
 *
 *  - 넓은 디스플레이 수식: 화면에서는 넘치는 수식을 가로 스크롤로 보지만 종이에는
 *    스크롤이 없다. 줄일 비율은 인쇄 레이아웃의 본문 폭으로 정해지는데, beforeprint
 *    시점의 레이아웃은 아직 화면 것이다. 그래서 여기서는 폭과 무관한 값 — 수식의 자연
 *    폭을 수식 글자 크기(em)로 잰 값 — 만 재어 .katex-display 에 --eq-w 로 달고, 실제
 *    축소는 _print.scss 가 디스플레이 폭(100cqi)을 그 값으로 나눠 정한다.
 *  - 증명·접기 박스 라벨: 종이에서는 라벨을 본문 첫 줄 앞에 붙인다("증명. …"). 정리
 *    박스 라벨은 원래 첫 <p> 안에 있지만 summary 는 <p> 밖의 블록이라, 펼친 박스마다
 *    라벨 사본(.runin-label)을 첫 문단 앞에 넣고 박스에 .print-runin 을 단다.
 *  - 증명 끝 QED: 화면의 .qed-mark 는 박스 기준 absolute 라, 증명이 쪽을 넘으면 첫 쪽
 *    조각의 아래에 앉아 본문과 겹친다. 마지막 줄 끝에 사본(.qed-print)을 붙인다.
 *  넣은 것은 afterprint 에 되돌린다.
 *
 * 인쇄 전용 글꼴(MyPrintSansFont, fonts.scss)은 화면에서 쓰이지 않아 저절로는 받지
 * 않는다. 인쇄 레이아웃이 처음 쓸 때 받기 시작하면 첫 인쇄가 대체 글꼴로 나갈 수 있어,
 * 페이지가 다 뜬 뒤 미리 받아 둔다 (화면의 나눔고딕과 같은 파일이라 대개 캐시에서 온다).
 */
(function () {
  'use strict';

  var GAP = 0.5; // 수식과 \tag 사이·좌우 여유 (em)
  var TK = window.THEOREM_KINDS || {};
  var COLLAPSIBLE = (TK.collapsibles || ['proof', 'proof--alone', 'details'])
    .map(function (c) { return 'details.' + c + '[open]'; })
    .join(',');

  function measureDisplays() {
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
  }

  function addRuninLabels() {
    document.querySelectorAll(COLLAPSIBLE).forEach(function (d) {
      var summary = d.querySelector(':scope > summary');
      if (!summary) return;
      var tag = summary.querySelector('.thm-tag') || summary;
      var label = document.createElement('span');
      label.className = 'runin-label';
      label.textContent = tag.textContent.trim();

      // 첫 내용이 문단이 아니면(수식·목록으로 시작) 라벨만 담을 문단을 새로 만든다.
      var first = summary.nextElementSibling;
      if (!first || first.tagName !== 'P') {
        var p = document.createElement('p');
        p.className = 'runin-only';
        d.insertBefore(p, first);
        first = p;
      }
      first.insertBefore(document.createTextNode(' '), first.firstChild);
      first.insertBefore(label, first.firstChild);
      d.classList.add('print-runin');

      if (summary.querySelector('.qed-mark')) addQed(d, summary);
    });
  }

  // 마지막 문단·항목이면 그 끝에 float 로(마지막 줄 오른쪽), 디스플레이 수식이면 그 수식
  // 오른쪽 아래에, 그 밖(그림 등)이면 새 줄에 붙인다.
  function addQed(d, summary) {
    var qed = document.createElement('span');
    qed.className = 'qed-print';
    var last = d.lastElementChild;
    while (last && (last.tagName === 'UL' || last.tagName === 'OL')) last = last.lastElementChild;
    if (last && last !== summary && last.classList.contains('katex-display')) {
      last.appendChild(qed);
    } else if (last && last !== summary && (last.tagName === 'P' || last.tagName === 'LI')) {
      last.appendChild(qed);
      last.classList.add('qed-host');
    } else {
      var p = document.createElement('p');
      p.className = 'runin-only qed-host';
      p.appendChild(qed);
      d.appendChild(p);
    }
  }

  function removeRunins() {
    document.querySelectorAll('details.print-runin').forEach(function (d) {
      d.querySelectorAll('.runin-label').forEach(function (label) {
        var space = label.nextSibling;
        if (space && space.nodeType === Node.TEXT_NODE && space.nodeValue === ' ') space.remove();
        label.remove();
      });
      d.querySelectorAll('.qed-print').forEach(function (q) { q.remove(); });
      d.querySelectorAll('.qed-host').forEach(function (h) { h.classList.remove('qed-host'); });
      d.querySelectorAll(':scope > p.runin-only').forEach(function (p) { p.remove(); });
      d.classList.remove('print-runin');
    });
  }

  window.addEventListener('beforeprint', function () {
    measureDisplays();
    addRuninLabels();
  });
  window.addEventListener('afterprint', removeRunins);

  window.addEventListener('load', function () {
    if (!document.fonts || !document.fonts.load) return;
    // '가A' — 한글 face 와 그 밖(라틴) face 를 함께 받도록
    document.fonts.load('1em MyPrintSansFont', '가A');
    document.fonts.load('bold 1em MyPrintSansFont', '가A');
  });
})();
