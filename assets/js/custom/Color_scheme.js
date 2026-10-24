---
# Liquid 처리용 front matter — 본문의 Liquid include 태그가 테마 코어를 삽입한다
---
/* Theme controller — 3-state: auto | light | dark.
 *
 * Dark/light live in one stylesheet (theme.css, merged at build time by
 * _plugins/theme_css.rb) and switch on <html data-theme="light|dark">.
 *
 *  - auto : follow the OS (prefers-color-scheme), live (matchMedia listener).
 *  - light/dark : pinned, ignores the OS.
 *
 * Choice persists in the MTHEME cookie.
 * This file is a head_script, so it runs before paint; head.html 의 pre-paint
 * 인라인이 같은 코어를 삽입해 더 이른 시점에 스타일시트를 맞춘다.
 *
 * 쿠키 파싱·모드 해석·data-theme 적용의 단일 출처는
 * _includes/js/theme-core.js (빌드 시 Liquid include 로 삽입).
 */
(function () {
  {% include js/theme-core.js %}

  function apply(mode, hooks) {
    if (!themeApply(mode, hooks)) return; // dark theme disabled site-wide
    syncUI(mode);
  }

  // 사용자·OS 가 테마를 바꿀 때는 <html> 에 theme-swapping 을 붙인 채로 data-theme 를 바꾼다.
  // 이 클래스가 $global-transition 대상(링크·버튼·img…)의 transition 을 끈다 — 규칙은
  // _sass/minimal-mistakes/_base.scss. 켜 둔 채 바꾸면 그 요소들이 옛 색에서 새 색으로
  // 0.2초씩 따라와, 한 번에 바뀌는 나머지 화면과 어긋난다.
  var swapping = 0; // 겹친 교체 수 — 마지막 교체가 끝날 때만 클래스를 뗀다

  function withoutTransitions() {
    var root = document.documentElement;
    return {
      before: function () {
        if (swapping++ === 0) root.classList.add('theme-swapping');
      },
      after: function () {
        void root.offsetHeight;             // 새 테마로 스타일을 확정한 뒤
        requestAnimationFrame(function () { // 그려진 다음 프레임에 되돌린다
          requestAnimationFrame(function () {
            if (--swapping === 0) root.classList.remove('theme-swapping');
          });
        });
      }
    };
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
    apply(mode, withoutTransitions());
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
    var onChange = function () { if (themeGetMode() === 'auto') apply('auto', withoutTransitions()); };
    if (mq.addEventListener) mq.addEventListener('change', onChange);
    else if (mq.addListener) mq.addListener(onChange); // older Safari
  }

  // Re-sync the menu highlight once the masthead exists.
  document.addEventListener('DOMContentLoaded', function () { apply(themeGetMode()); });
})();
