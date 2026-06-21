/* Theme controller — 3-state: auto | light | dark.
 *
 * Dark/light is a stylesheet swap (main.css <-> main_dark.css), toggled by
 * disabling one <link> (ids: theme-light / theme-dark).
 *
 *  - auto : follow the OS (prefers-color-scheme), live (matchMedia listener).
 *  - light/dark : pinned, ignores the OS.
 *
 * Choice persists in the MTHEME cookie (legacy MDARK Y/N is migrated on read).
 * This file is a head_script, so it runs before paint; a tiny inline twin in
 * head.html applies the stylesheet even earlier to fully kill FOUC.
 */
(function () {
  function getCookie(name) {
    var parts = document.cookie.split('; ');
    for (var i = 0; i < parts.length; i++) {
      if (parts[i].indexOf(name + '=') === 0) return parts[i].slice(name.length + 1);
    }
    return null;
  }

  function getTheme() {
    var v = getCookie('MTHEME');
    if (v === 'light' || v === 'dark' || v === 'auto') return v;
    var legacy = getCookie('MDARK'); // migrate old 2-state cookie
    if (legacy === 'Y') return 'dark';
    if (legacy === 'N') return 'light';
    return 'auto';
  }

  function systemPrefersDark() {
    return !!(window.matchMedia && window.matchMedia('(prefers-color-scheme: dark)').matches);
  }

  function effective(mode) {
    if (mode === 'dark') return 'dark';
    if (mode === 'light') return 'light';
    return systemPrefersDark() ? 'dark' : 'light';
  }

  function apply(mode) {
    var darkLink = document.getElementById('theme-dark');
    if (!darkLink) return; // dark theme disabled site-wide
    var lightLink = document.getElementById('theme-light');
    var dark = effective(mode) === 'dark';
    darkLink.disabled = !dark;
    if (lightLink) lightLink.disabled = dark;
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
  apply(getTheme());

  // Follow the OS live while in auto mode.
  if (window.matchMedia) {
    var mq = window.matchMedia('(prefers-color-scheme: dark)');
    var onChange = function () { if (getTheme() === 'auto') apply('auto'); };
    if (mq.addEventListener) mq.addEventListener('change', onChange);
    else if (mq.addListener) mq.addListener(onChange); // older Safari
  }

  // Re-sync the menu highlight once the masthead exists.
  document.addEventListener('DOMContentLoaded', function () { apply(getTheme()); });
})();
