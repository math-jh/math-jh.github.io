// 테마 코어 — 쿠키 파싱 · 3-상태(auto|light|dark) 해석 ·
// 스타일시트(theme-light/theme-dark) 토글의 단일 출처.
// 소비자 2곳이 빌드 시 Liquid include 태그로 삽입한다:
//   _includes/head.html              — pre-paint 인라인 (FOUC 킬)
//   assets/js/custom/Color_scheme.js — 컨트롤러 (UI·리스너·쿠키 쓰기)
// 런타임 사본은 2개지만 소스는 이 파일 하나다. 함수들은 각 소비자의 IIFE
// 안에서만 살므로 전역을 오염시키지 않는다.
function themeGetCookie(name) {
  var parts = document.cookie.split('; ');
  for (var i = 0; i < parts.length; i++) {
    if (parts[i].indexOf(name + '=') === 0) return parts[i].slice(name.length + 1);
  }
  return null;
}

function themeGetMode() {
  var v = themeGetCookie('MTHEME');
  if (v === 'light' || v === 'dark' || v === 'auto') return v;
  return 'auto';
}

function themeEffective(mode) {
  if (mode === 'dark') return 'dark';
  if (mode === 'light') return 'light';
  return (window.matchMedia && window.matchMedia('(prefers-color-scheme: dark)').matches)
    ? 'dark' : 'light';
}

// 스타일시트 토글만 담당 — 메뉴 하이라이트 등 UI 동기화는 컨트롤러 몫.
// 켤 쪽을 먼저 켜고, 그 시트가 붙은 뒤(link.sheet)에야 끌 쪽을 끈다. disabled 를
// 푼 link 는 브라우저가 시트를 다시 붙이는데 이게 비동기일 수 있어서, 끄기를 먼저 하면
// 그 사이 두 시트가 다 빠진 무스타일 프레임이 그려진다. 둘이 겹치는 동안은 문서 순서상
// 뒤인 theme-dark 가 이긴다. 대기 중에 새 교체가 들어오면 앞의 교체는 손을 뗀다.
// hooks({before, after})가 주어지면 실제 교체가 있을 때만 그 앞뒤로 부른다.
// dark 테마가 사이트 차원에서 꺼져 있으면(false 반환) 아무것도 하지 않는다.
var themeSwapSeq = 0;

function themeApplyStylesheets(mode, hooks) {
  var darkLink = document.getElementById('theme-dark');
  if (!darkLink) return false;
  var lightLink = document.getElementById('theme-light');
  var dark = themeEffective(mode) === 'dark';
  var on = dark ? darkLink : lightLink;
  var off = dark ? lightLink : darkLink;
  if (on && !on.disabled && (!off || off.disabled)) return true;
  var seq = ++themeSwapSeq;
  var frames = 0;
  if (hooks) hooks.before();
  if (on) on.disabled = false;
  (function finish() {
    if (seq !== themeSwapSeq) { if (hooks) hooks.after(); return; }
    if (on && !on.sheet && ++frames < 600) { requestAnimationFrame(finish); return; }
    if (off) off.disabled = true;
    if (hooks) hooks.after();
  })();
  return true;
}
