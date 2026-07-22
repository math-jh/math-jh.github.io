---
# Liquid 처리용 front matter — 본문의 Liquid include 태그가 테마 코어를 삽입한다
---
/* Theme controller — 3-state: auto | light | dark.
 *
 * Dark/light is a stylesheet swap (main.css <-> main_dark.css), toggled by
 * disabling one <link> (ids: theme-light / theme-dark).
 *
 *  - auto : follow the OS (prefers-color-scheme), live (matchMedia listener).
 *  - light/dark : pinned, ignores the OS.
 *
 * Choice persists in the MTHEME cookie.
 * This file is a head_script, so it runs before paint; head.html 의 pre-paint
 * 인라인이 같은 코어를 삽입해 더 이른 시점에 스타일시트를 맞춘다.
 *
 * 쿠키 파싱·모드 해석·스타일시트 토글의 단일 출처는
 * _includes/js/theme-core.js (빌드 시 Liquid include 로 삽입).
 */
(function () {
  {% include js/theme-core.js %}

  function apply(mode) {
    if (!themeApplyStylesheets(mode)) return; // dark theme disabled site-wide
    syncUI(mode);
  }

  function syncUI(mode) {
    var items = document.querySelectorAll('.settings-subitem');
    for (var i = 0; i < items.length; i++) {
      items[i].classList.toggle('active', items[i].getAttribute('data-theme-mode') === mode);
    }
  }

  // ---- public (called from masthead markup) ----

  window.setTheme = function (mode, ev) {
    if (ev) ev.stopPropagation();
    document.cookie = 'MTHEME=' + mode + '; path=/; max-age=31536000';
    apply(mode);
  };

  window.toggleThemeSubmenu = function (ev) {
    if (ev) ev.stopPropagation();
    var sub = document.getElementById('theme-submenu');
    var parent = document.getElementById('theme-parent');
    if (sub) sub.classList.toggle('show');
    if (parent) parent.classList.toggle('expanded');
  };

  // Apply immediately (head-time) so the swap is correct before paint.
  apply(themeGetMode());

  // Follow the OS live while in auto mode.
  if (window.matchMedia) {
    var mq = window.matchMedia('(prefers-color-scheme: dark)');
    var onChange = function () { if (themeGetMode() === 'auto') apply('auto'); };
    if (mq.addEventListener) mq.addEventListener('change', onChange);
    else if (mq.addListener) mq.addListener(onChange); // older Safari
  }

  // Re-sync the menu highlight once the masthead exists.
  document.addEventListener('DOMContentLoaded', function () { apply(themeGetMode()); });
})();
