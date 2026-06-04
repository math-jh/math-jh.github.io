/* Recent-posts overlay — open the /xx/recent/ page in a backdrop popup
 * (mirrors the search overlay) instead of navigating away. The standalone page
 * still works for no-JS users and direct links (progressive enhancement).
 *
 * Trigger: any link to /ko/recent/ or /en/recent/ (the "최근 글" header in the
 * recents sidebar block).
 * Close: X button, Esc, or backdrop click — no navigation, "closes like a window".
 */
(function () {
  var overlay, body, loaded = {};

  function currentLang() {
    return (window.location.pathname.split('/')[1] === 'en') ? 'en' : 'ko';
  }

  function recentUrl() {
    return '/' + currentLang() + '/recent/';
  }

  function open() {
    if (!overlay) return;
    overlay.classList.add('is--visible');
    overlay.setAttribute('aria-hidden', 'false');
    document.body.classList.add('overflow--hidden'); // reuse theme's scroll lock
    load();
  }

  function close() {
    if (!overlay) return;
    overlay.classList.remove('is--visible');
    overlay.setAttribute('aria-hidden', 'true');
    document.body.classList.remove('overflow--hidden');
  }

  function load() {
    var url = recentUrl();
    if (loaded[url]) return;
    body.innerHTML = '<p style="opacity:.6">…</p>';
    fetch(url)
      .then(function (r) { return r.text(); })
      .then(function (html) {
        var doc = new DOMParser().parseFromString(html, 'text/html');
        var parts = doc.querySelectorAll('.page__title, .entries-list');
        var out = '';
        for (var i = 0; i < parts.length; i++) { out += parts[i].outerHTML; }
        body.innerHTML = out || '<p>비어 있습니다.</p>';
        loaded[url] = true;
      })
      .catch(function () { body.innerHTML = '<p>최근 글을 불러오지 못했습니다.</p>'; });
  }

  document.addEventListener('DOMContentLoaded', function () {
    overlay = document.getElementById('recent-overlay');
    body = document.getElementById('recent-overlay-body');
    if (!overlay || !body) return;

    // Intercept any link to the recent page → open as overlay.
    var triggers = document.querySelectorAll('a[href$="/recent/"], a[href$="/recent"]');
    for (var i = 0; i < triggers.length; i++) {
      if (triggers[i].closest('#recent-overlay')) continue; // skip in-overlay links
      triggers[i].addEventListener('click', function (e) { e.preventDefault(); open(); });
    }

    // Close: X button or backdrop click.
    overlay.addEventListener('click', function (e) {
      if (e.target === overlay || e.target.closest('.recent-content__close')) close();
    });

    // Close: Esc.
    document.addEventListener('keyup', function (e) {
      if (e.keyCode === 27 && overlay.classList.contains('is--visible')) close();
    });
  });
})();
