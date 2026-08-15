// 본문의 영문 낱말을 <span lang="en"> 으로 감싼다.
//
// 글 전체는 lang="ko" 라 브라우저가 영문 하이픈 패턴을 꺼내지 않는다 — 그 상태에서는
// hyphens: auto 가 무음이다. 낱말 단위로 lang 을 바꿔줘야 비로소 하이픈이 걸린다.
// 목적은 양끝맞춤에서 한 줄이 메워야 할 폭 자체를 줄이는 것이다 (TeX 이 한국어 문서
// 안의 라틴 낱말도 하이픈으로 쪼개는 것과 같은 이유). 하이픈을 켜는 규칙은 CSS 쪽
// (_page.scss 의 `[lang="en"] { hyphens: auto }`) 이고, 여기서는 감싸기만 한다.
//
// KaTeX 렌더가 끝난 뒤에 불러야 한다 — 그 전에는 수식이 아직 `$...$` 텍스트라
// 그 안의 영문까지 감싸버려 파싱이 깨진다. 호출부는 _includes/scripts.html 한 곳.
(function () {
  // 길이 제한 없이 라틴 낱말을 전부 감싼다. 이 스팬은 두 가지를 나른다:
  // hyphens(긴 낱말에만 의미가 있다)와 _page.scss 의 `text-justify: inter-word`
  // (길이와 무관하게 모든 라틴 낱말에 필요하다). 뒤엣것 때문에 임계값을 둘 수 없다.
  // 예전의 "6자 이상" 조건에서는 5자 이하가 스팬 밖에 남아 부모의 inter-character
  // 를 그대로 받았고, "total space" 처럼 짧은 낱말이 이어지면 그 구간만 글자 사이가
  // 벌어졌다.
  // 앞뒤에 공백 없이 붙은 기호(§, 괄호, 쉼표 …)까지 함께 감싼다: 브라우저는 낱말이
  // 다른 요소에서 시작하면 하이픈을 걸지 않으므로, "§Compactness" 처럼 기호가 붙은
  // 경우 기호가 스팬 밖에 남으면 그 낱말만 하이픈이 죽는다. 한글은 밖에 둔다.
  var WORD = /[^\s가-힣]*[A-Za-z][A-Za-z'-]*[^\s가-힣]*/g;
  var SKIP = '.katex, code, pre, [lang="en"]';

  function wrapWords(text) {
    var v = text.nodeValue;
    var frag = document.createDocumentFragment();
    var last = 0, m;

    WORD.lastIndex = 0;
    while ((m = WORD.exec(v))) {
      if (m.index > last) frag.appendChild(document.createTextNode(v.slice(last, m.index)));
      var span = document.createElement('span');
      span.lang = 'en';
      span.textContent = m[0];
      frag.appendChild(span);
      last = m.index + m[0].length;
    }
    if (last === 0) return;                                  // 감쌀 게 없었다
    if (last < v.length) frag.appendChild(document.createTextNode(v.slice(last)));
    text.parentNode.replaceChild(frag, text);
  }

  window.hyphenateLatin = function (root) {
    if (!root || !root.querySelectorAll) return;
    // EN 페이지는 문서 lang 이 이미 en 이라 감쌀 이유가 없다 (_page.scss 의 :lang(en) 규칙)
    if ((document.documentElement.lang || '').slice(0, 2) === 'en') return;

    // 양끝맞춤이 걸리는 문단·목록만 대상으로 한다 (제목·캡션은 제외)
    root.querySelectorAll('p, li').forEach(function (block) {
      var walker = document.createTreeWalker(block, NodeFilter.SHOW_TEXT, null);
      var targets = [], node;

      while ((node = walker.nextNode())) {
        var parent = node.parentNode;
        if (!parent || !parent.closest || parent.closest(SKIP)) continue;
        WORD.lastIndex = 0;
        if (WORD.test(node.nodeValue)) targets.push(node);
      }

      targets.forEach(wrapWords);   // 순회가 끝난 뒤 교체한다 (walker 무효화 방지)
    });
  };
})();
