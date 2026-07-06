document.addEventListener('DOMContentLoaded', function () {
    const textElement = document.querySelector('.typed-text');
    if (textElement) {
        const items = JSON.parse(textElement.dataset.text || '[]');
        let current = 0;
        let index = 0;
        let forward = true;

        function type() {
            const currentText = items[current] || '';
            if (forward) {
                textElement.textContent = currentText.slice(0, index + 1);
                index += 1;
                if (index === currentText.length) {
                    forward = false;
                    setTimeout(type, 1200);
                    return;
                }
            } else {
                textElement.textContent = currentText.slice(0, index - 1);
                index -= 1;
                if (index === 0) {
                    forward = true;
                    current = (current + 1) % items.length;
                }
            }
            setTimeout(type, forward ? 120 : 60);
        }

        if (items.length > 0) {
            type();
        }
    }

    const backToTop = document.getElementById('back-to-top');
    if (backToTop) {
        window.addEventListener('scroll', () => {
            if (window.pageYOffset > 400) {
                backToTop.style.display = 'flex';
            } else {
                backToTop.style.display = 'none';
            }
        });

        backToTop.addEventListener('click', () => {
            window.scrollTo({ top: 0, behavior: 'smooth' });
        });
    }
});
