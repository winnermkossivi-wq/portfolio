(function () {
    'use strict';

    var scrollingUp = false;
    var lastScrollY = window.scrollY || 0;

    window.addEventListener('scroll', function () {
        var y = window.scrollY || 0;
        scrollingUp = y < lastScrollY;
        lastScrollY = y;
    }, { passive: true });

    var reduceMotion = window.matchMedia && window.matchMedia('(prefers-reduced-motion: reduce)').matches;

    function showAll(elements) {
        for (var i = 0; i < elements.length; i++) {
            elements[i].classList.add('reveal-visible');
        }
    }

    function init() {
        var elements = document.querySelectorAll('.reveal');

        if (reduceMotion || typeof IntersectionObserver === 'undefined') {
            showAll(elements);
            return;
        }

        var observer = new IntersectionObserver(function (entries) {
            for (var i = 0; i < entries.length; i++) {
                var entry = entries[i];
                var el = entry.target;

                if (entry.isIntersecting) {
                    if (el.classList.contains('reveal-visible')) continue;
                    el.style.setProperty('--reveal-offset', scrollingUp ? '-30px' : '30px');
                    void el.offsetHeight;
                    el.classList.add('reveal-visible');
                } else {
                    el.classList.remove('reveal-visible');
                }
            }
        }, { threshold: 0.15 });

        for (var j = 0; j < elements.length; j++) {
            observer.observe(elements[j]);
        }
    }

    var loader = document.getElementById('loader-screen');
    if (!loader) {
        init();
        return;
    }

    var attempts = 0;
    (function waitForLoader() {
        if (!document.getElementById('loader-screen') || attempts >= 100) {
            init();
            return;
        }
        attempts += 1;
        setTimeout(waitForLoader, 100);
    })();
})();