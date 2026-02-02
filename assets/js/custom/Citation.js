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
            // Matches: 정의 1, 정리 2, 명제 3, 예시 4, 보조정리 5, Definition 1, Theorem 2, etc.
            // Allows optional punctuation like "정리 1." or "Theorem 1:"
            const match = ins.textContent.match(/(정의|정리|명제|예시|보조정리|Corollary|Lemma|Definition|Theorem|Proposition|Example|Remark|주의)\s*[\.\-:]?\s*([0-9]+)/);
            if (!match) {
                console.log('Citation.js: No match for text:', ins.textContent);
                return;
            }
            const type = match[1];
            const number = match[2];
            const insID = ins.id;
            const pagePath = window.location.pathname;

            const citation = `[\\[${category}\] §${postTitle}, ⁋${type} ${number}](${pagePath}#${insID})`;
            console.log('Citation.js: Copying citation:', citation);

            // Try modern Clipboard API first, fallback to execCommand
            const copyToClipboard = (text) => {
                if (navigator.clipboard && window.isSecureContext) {
                    return navigator.clipboard.writeText(text);
                } else {
                    // Fallback for non-secure contexts (HTTP) or older browsers
                    return new Promise((resolve, reject) => {
                        const textArea = document.createElement('textarea');
                        textArea.value = text;
                        textArea.style.position = 'fixed';
                        textArea.style.left = '-9999px';
                        textArea.style.top = '0';
                        document.body.appendChild(textArea);
                        textArea.focus();
                        textArea.select();
                        try {
                            const success = document.execCommand('copy');
                            document.body.removeChild(textArea);
                            if (success) {
                                resolve();
                            } else {
                                reject(new Error('execCommand copy failed'));
                            }
                        } catch (err) {
                            document.body.removeChild(textArea);
                            reject(err);
                        }
                    });
                }
            };

            copyToClipboard(citation).then(() => {
                // Success feedback (flash the background)
                ins.style.transition = 'background 0.2s';
                ins.style.background = 'rgba(180,220,255,0.4)';
                setTimeout(function() {
                    ins.style.background = '';
                }, 400);
                console.log('Citation.js: Successfully copied to clipboard');
            }).catch(err => {
                console.error('Citation.js: Failed to copy citation:', err);
                // Show the citation so user can manually copy it
                alert('클립보드 복사에 실패했습니다. 수동으로 복사해주세요:\n\n' + citation);
            });
            
            e.stopPropagation();
        });
    });
});
