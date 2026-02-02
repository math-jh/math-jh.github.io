document.addEventListener('DOMContentLoaded', function() {
    // 1. Extract category
    let catElem = document.querySelector('nav.nav__list span.nav__sub-title a.sidebar_title');
    let category = catElem ? catElem.textContent.trim() : '';

    // 2. Extract post title
    let h1 = document.querySelector('h1');
    let postTitle = h1 ? h1.textContent.trim() : document.title.replace(/-.*$/, '').trim();

    // 3. For each <ins id=...>
    document.querySelectorAll('ins[id]').forEach(function(ins) {
        ins.style.cursor = 'pointer'; // Show pointer on hover
        
        ins.addEventListener('click', function(e) {
            // Extract type and number
            const match = ins.textContent.match(/(정의|정리|명제|예시|보조정리|Corollary|Lemma|Definition|Theorem|Proposition|Example|Remark|주의)\s*([0-9]+)/);
            if (!match) return;
            const type = match[1];
            const number = match[2];
            const insID = ins.id;
            const pagePath = window.location.pathname;

            const citation = `[\\[${category}\\] §${postTitle}, ⁋${type} ${number}](${pagePath}#${insID})`;

            // Try modern Clipboard API first, fallback to execCommand
            const copyToClipboard = (text) => {
                if (navigator.clipboard && window.isSecureContext) {
                    return navigator.clipboard.writeText(text);
                } else {
                    // Fallback for non-secure contexts or older browsers
                    const textArea = document.createElement('textarea');
                    textArea.value = text;
                    textArea.style.position = 'fixed';
                    textArea.style.left = '-9999px';
                    document.body.appendChild(textArea);
                    textArea.focus();
                    textArea.select();
                    try {
                        document.execCommand('copy');
                        document.body.removeChild(textArea);
                        return Promise.resolve();
                    } catch (err) {
                        document.body.removeChild(textArea);
                        return Promise.reject(err);
                    }
                }
            };

            copyToClipboard(citation).then(() => {
                // Success feedback (flash the background)
                ins.style.transition = 'background 0.2s';
                ins.style.background = 'rgba(180,220,255,0.4)';
                setTimeout(function() {
                    ins.style.background = '';
                }, 400);
            }).catch(err => {
                console.error('Failed to copy citation:', err);
            });
            
            e.stopPropagation();
        });
    });
});
