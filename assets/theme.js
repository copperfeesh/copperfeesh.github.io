(function() {
    function getPreferredTheme() {
        const saved = localStorage.getItem('theme');
        if (saved) return saved;
        return window.matchMedia('(prefers-color-scheme: dark)').matches ? 'dark' : 'light';
    }

    function updateToggleAria(theme) {
        const btn = document.getElementById('theme-toggle');
        if (btn) {
            btn.setAttribute('aria-label', theme === 'dark' ? 'Switch to light mode' : 'Switch to dark mode');
            btn.setAttribute('title', theme === 'dark' ? 'Switch to light mode' : 'Switch to dark mode');
        }
    }

    function init() {
        const btn = document.getElementById('theme-toggle');
        if (!btn) return;

        updateToggleAria(document.documentElement.getAttribute('data-theme') || getPreferredTheme());

        btn.addEventListener('click', function() {
            const current = document.documentElement.getAttribute('data-theme') || 
                           (window.matchMedia('(prefers-color-scheme: dark)').matches ? 'dark' : 'light');
            const next = current === 'dark' ? 'light' : 'dark';
            
            document.documentElement.setAttribute('data-theme', next);
            localStorage.setItem('theme', next);
            updateToggleAria(next);
        });
    }

    if (document.readyState === 'loading') {
        document.addEventListener('DOMContentLoaded', init);
    } else {
        init();
    }
})();
