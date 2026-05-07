document.addEventListener('DOMContentLoaded', function() {
    // 1. Extract category — handle both old (<span><a class="sidebar_title">) and new (<a><span class="nav__sub-title">) sidebar structures
    let catElem = document.querySelector('nav.nav__list a.sidebar_title')
        || document.querySelector('nav.nav__list a[href] > span.nav__sub-title')
        || document.querySelector('nav.nav__list span.nav__sub-title');
    let category = catElem ? catElem.textContent.trim() : '';

    // 2. Extract post title
    let h1 = document.querySelector('h1');
    let postTitle = h1 ? h1.textContent.trim() : document.title.replace(/-.*$/, '').trim();

    // 3. For each <ins id=...>
    const insList = document.querySelectorAll('ins[id]');
    console.log('[Citation.js] attaching click handlers to', insList.length, 'ins[id] elements; category="' + category + '", postTitle="' + postTitle + '"');
    insList.forEach(function(ins) {
        ins.style.cursor = 'pointer'; // Show pointer on hover

        ins.addEventListener('click', function(e) {
            // Extract type and number — 따름정리 must appear before 정리 to avoid partial match
            const match = ins.textContent.match(/(따름정리|보조정리|정의|정리|명제|예시|주의|Corollary|Lemma|Definition|Theorem|Proposition|Example|Remark)\s*([0-9]+)/);
            if (!match) return;
            const type = match[1];
            const number = match[2];
            const insID = ins.id;
            const pagePath = window.location.pathname;

            const citation = `[\\[${category}\\] §${postTitle}, ⁋${type} ${number}](${pagePath}#${insID})`;

            if (navigator.clipboard && window.isSecureContext) {
                navigator.clipboard.writeText(citation);
            } else {
                const ta = document.createElement('textarea');
                ta.value = citation;
                ta.style.position = 'fixed';
                ta.style.opacity = '0';
                document.body.appendChild(ta);
                ta.select();
                document.execCommand('copy');
                document.body.removeChild(ta);
            }

            // Optional: quick feedback (flash the background)
            ins.style.transition = 'background 0.2s';
            ins.style.background = 'rgba(180,220,255,0.4)';
            setTimeout(function() {
                ins.style.background = '';
            }, 400);
            
            e.stopPropagation();
        });
    });
});
