function lang_home() {
    var pathname = window.location.pathname.split('/');
    if (pathname[1] == "en" || pathname[1] == "ko"){
        window.location.href = "/" + pathname[1] + "/";
    }
    else {
        window.location.href = "/";
    }
}

function lang_select() {
    var pathname = window.location.pathname.split('/');

    if (pathname[1] !== "en" && pathname[1] !== "ko") {
        return;  // 언어 경로가 아니면 아무것도 하지 않음
    }

    var newlang = pathname[1] === "en" ? "/ko" : "/en";
    var newpathname = "";

    for (var i = 2; i < pathname.length; i++) {
        newpathname += "/";
        newpathname += pathname[i];
    }
    window.location.href = newlang + newpathname;
}

// Current page language ('ko' default).
function currentLang() {
    var seg = window.location.pathname.split('/')[1];
    return (seg === 'en') ? 'en' : 'ko';
}

// UI strings. window.__ui is injected per-build from _data/ui-text.yml in
// masthead.html, holding ALL languages so the include_cached masthead stays
// language-agnostic; JS then picks by page language. Hardcoded fallback keeps
// the menu labelled even if injection is missing.
function uiText(key) {
    var lang = currentLang();
    var dict = (window.__ui && window.__ui[lang]) || {};
    if (dict[key]) return dict[key];
    var fb = {
        ko: { theme_label: '테마', theme_auto: '자동', theme_light: '라이트', theme_dark: '다크', language_label: '언어' },
        en: { theme_label: 'Theme', theme_auto: 'Auto', theme_light: 'Light', theme_dark: 'Dark', language_label: 'Language' }
    };
    return (fb[lang] && fb[lang][key]) || '';
}

// Settings dropdown toggle
function toggleSettings(event) {
    event.stopPropagation();
    var menu = document.getElementById('settings-menu');
    if (menu) {
        menu.classList.toggle('show');
    }
}

// Close dropdown when clicking outside
document.addEventListener('click', function(e) {
    var menu = document.getElementById('settings-menu');
    if (menu && !e.target.closest('.settings-dropdown')) {
        menu.classList.remove('show');
    }
});

// ---- Language accordion (theme accordion lives in Color_scheme.js) ----

// Parent label: "언어" / "Language".
function updateLangLabel() {
    var label = document.getElementById('lang-label');
    if (label) label.textContent = uiText('language_label');
}

// Highlight the current page's language in the submenu.
function markActiveLang() {
    var cur = currentLang();
    var items = document.querySelectorAll('#lang-submenu .settings-subitem');
    for (var i = 0; i < items.length; i++) {
        items[i].classList.toggle('active', items[i].getAttribute('data-lang-target') === cur);
    }
}

// Expand/collapse the language submenu (mirrors toggleThemeSubmenu).
function toggleLangSubmenu(event) {
    if (event) event.stopPropagation();
    var sub = document.getElementById('lang-submenu');
    var parent = document.getElementById('lang-parent');
    if (sub) sub.classList.toggle('show');
    if (parent) parent.classList.toggle('expanded');
}

// Navigate to a specific language version of the current page.
function goLang(target, event) {
    if (event) event.stopPropagation();
    var pathname = window.location.pathname.split('/');
    if (pathname[1] !== 'en' && pathname[1] !== 'ko') return;
    if (pathname[1] === target) return; // already on this language
    var rest = '';
    for (var i = 2; i < pathname.length; i++) { rest += '/' + pathname[i]; }
    window.location.href = '/' + target + rest;
}

// ---- Theme accordion labels (localized; selection logic is in Color_scheme.js) ----

// Parent label: "테마" / "Theme".
function updateThemeLabel() {
    var label = document.getElementById('theme-label');
    if (label) label.textContent = uiText('theme_label');
}

// Leaf labels: 자동/라이트/다크 <-> Auto/Light/Dark.
function updateThemeLeaves() {
    var map = { auto: 'theme_auto', light: 'theme_light', dark: 'theme_dark' };
    var items = document.querySelectorAll('#theme-submenu .settings-subitem');
    for (var i = 0; i < items.length; i++) {
        var mode = items[i].getAttribute('data-theme-mode');
        var span = items[i].querySelector('span');
        if (span && map[mode]) span.textContent = uiText(map[mode]);
    }
}

// 페이지 로드 시 body에 data-lang 추가 + 라벨 로컬라이즈
function setPageLang() {
    document.body.setAttribute('data-lang', currentLang());
    updateLangLabel();
    markActiveLang();
    updateThemeLabel();
    updateThemeLeaves();
}

// 페이지 로드 시 실행
document.addEventListener('DOMContentLoaded', setPageLang);
