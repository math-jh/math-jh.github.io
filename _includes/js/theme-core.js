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
// dark 테마가 사이트 차원에서 꺼져 있으면(false 반환) 아무것도 하지 않는다.
function themeApplyStylesheets(mode) {
  var darkLink = document.getElementById('theme-dark');
  if (!darkLink) return false;
  var lightLink = document.getElementById('theme-light');
  var dark = themeEffective(mode) === 'dark';
  darkLink.disabled = !dark;
  if (lightLink) lightLink.disabled = dark;
  return true;
}
