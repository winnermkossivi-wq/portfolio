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

(function () {
    'use strict';

    var DEVICON = 'https://cdn.jsdelivr.net/gh/devicons/devicon@latest/icons/';
    var ALIAS = {
        html: 'html5',
        css: 'css3',
        js: 'javascript',
        vue: 'vuejs',
        'vue.js': 'vuejs',
        reactjs: 'react',
        'react.js': 'react',
        postgres: 'postgresql',
        node: 'nodejs',
        'node.js': 'nodejs',
        next: 'nextjs',
        'next.js': 'nextjs',
        tailwind: 'tailwindcss',
        'tailwind css': 'tailwindcss',
        'c++': 'cplusplus',
        'c#': 'csharp'
    };

    function slug(nom) {
        var base = (nom || '').toLowerCase().trim();
        if (ALIAS[base]) return ALIAS[base];
        return base
            .replace(/\./g, '')
            .replace(/\s+/g, '-')
            .replace(/[^a-z0-9+#-]/g, '');
    }

    function chargerLogo(span) {
        var racine = slug(span.getAttribute('data-outil'));
        if (!racine) return;
        var variantes = [racine + '-original', racine + '-plain'];
        var i = 0;

        (function essayer() {
            if (i >= variantes.length) return;
            var img = document.createElement('img');
            img.alt = '';
            img.setAttribute('aria-hidden', 'true');
            img.onload = function () {
                span.innerHTML = '';
                span.appendChild(img);
            };
            img.onerror = function () {
                i += 1;
                essayer();
            };
            img.src = DEVICON + racine + '/' + variantes[i] + '.svg';
        })();
    }

    var icones = document.querySelectorAll('.outil-icone[data-outil]');
    for (var a = 0; a < icones.length; a++) {
        chargerLogo(icones[a]);
    }

    var anim = document.documentElement.classList.contains('js-anim');
    if (!anim || typeof IntersectionObserver === 'undefined') return;

    var pourcentages = document.querySelectorAll('.outil-pct');
    for (var b = 0; b < pourcentages.length; b++) {
        pourcentages[b].textContent = '0%';
    }

    function compter(el, cible) {
        var debut = null;
        var duree = 1100;
        function etape(ts) {
            if (debut === null) debut = ts;
            var p = Math.min((ts - debut) / duree, 1);
            var adouci = 1 - Math.pow(1 - p, 3);
            el.textContent = Math.round(adouci * cible) + '%';
            if (p < 1) requestAnimationFrame(etape);
        }
        requestAnimationFrame(etape);
    }

    var cartes = document.querySelectorAll('.outil-carte');

    var observer = new IntersectionObserver(function (entrees) {
        for (var n = 0; n < entrees.length; n++) {
            if (!entrees[n].isIntersecting) continue;
            observer.unobserve(entrees[n].target);
            var outils = entrees[n].target.querySelectorAll('.outil');
            for (var k = 0; k < outils.length; k++) {
                (function (outil, rang) {
                    setTimeout(function () {
                        outil.classList.add('est-rempli');
                        var pct = outil.querySelector('.outil-pct');
                        var cible = parseInt(outil.getAttribute('data-niveau'), 10) || 0;
                        if (pct) compter(pct, cible);
                    }, rang * 120);
                })(outils[k], k);
            }
        }
    }, { threshold: 0.3 });

    for (var c = 0; c < cartes.length; c++) {
        observer.observe(cartes[c]);
    }
})();