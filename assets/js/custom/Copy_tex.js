/* Copy_tex.js — 수식이 걸린 선택을 복사하면 클립보드 글자에 수식의 TeX 원문을 넣는다.
 *
 * KaTeX 출력은 보이는 .katex-html 과 화면에서 숨긴 .katex-mathml(MathML + 원문
 * <annotation>) 두 벌이라, 브라우저 기본 복사는 두 벌의 글자를 뒤섞어 내보낸다. 선택에
 * 수식이 있으면 수식마다 원문으로 바꾼 글자(인라인 $…$, 디스플레이 $$…$$)를 text/plain
 * 으로만 넣는다. text/html 은 넣지 않는다 — 붙여넣는 쪽이 HTML 을 먼저 쓰는데, KaTeX
 * HTML 은 KaTeX CSS 없이는 다시 뒤섞인 글자가 되고, 원문으로 바꿔 넣어도 HTML→마크다운
 * 변환기(Obsidian 등)가 \ 와 _ 를 이스케이프한다.
 *
 *  - 선택 끝이 수식 안에 걸리면 수식 전체로 넓힌다 (디스플레이 수식은 .katex-display 까지).
 *  - 문단 줄바꿈은 브라우저 복사처럼 남긴다: 바꾼 조각을 선택의 공통 조상 안, 화면 밖에
 *    잠깐 붙여 innerText 로 읽는다. textContent 는 블록 사이 줄바꿈을 버리고, 공통 조상
 *    안에 붙여야 그 자리에 걸린 CSS(숨김 등)가 원래처럼 적용된다.
 *  - 원문은 글에 쓴 그대로라 커스텀 매크로(katex-macros.js)는 펼쳐지지 않는다.
 */
(function () {
  'use strict';

  function mathAround(node) {
    var el = node instanceof Element ? node : node.parentElement;
    return el && (el.closest('.katex-display') || el.closest('.katex'));
  }

  document.addEventListener('copy', function (e) {
    var sel = window.getSelection();
    if (!e.clipboardData || !sel || sel.rangeCount !== 1 || sel.isCollapsed) return;

    var range = sel.getRangeAt(0).cloneRange();
    var start = mathAround(range.startContainer);
    if (start) range.setStartBefore(start);
    var end = mathAround(range.endContainer);
    if (end) range.setEndAfter(end);

    var frag = range.cloneContents();
    if (!frag.querySelector('.katex-mathml annotation')) return;

    frag.querySelectorAll('.katex').forEach(function (k) {
      var ann = k.querySelector('.katex-mathml annotation');
      if (!ann) return;
      var tex = ann.textContent.trim();
      var display = k.closest('.katex-display');
      if (display) {
        // 여러 줄 원문(aligned 등)의 줄바꿈을 살린다
        var block = document.createElement('div');
        block.style.whiteSpace = 'pre-wrap';
        block.textContent = '$$' + tex + '$$';
        display.replaceWith(block);
      } else {
        k.replaceWith(document.createTextNode('$' + tex + '$'));
      }
    });

    var host = range.commonAncestorContainer;
    if (!(host instanceof Element)) host = host.parentElement;
    var box = document.createElement('div');
    box.style.cssText = 'position:fixed;left:-99999px;top:0;';
    box.appendChild(frag);
    host.appendChild(box);
    var text = box.innerText;
    box.remove();

    e.clipboardData.setData('text/plain', text);
    e.preventDefault();
  });
})();
