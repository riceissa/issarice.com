// License: CC0 https://creativecommons.org/publicdomain/zero/1.0/

// We use a self-executing anonymous function to create a separate namespace
// called change_theme. This way any functions we define here won't affect
// other scripts. See https://stackoverflow.com/a/5947280/3422337 . (The
// version here is a bit different because we aren't using jQuery so we don't
// have to pass that as an argument, and modern versions of JavaScript don't
// allow you to redefine undefined so we don't need to keep that as an argument
// either.)
(function(change_theme) {
    // body class : blank (light) or "dark" (dark)
    // local storage: blank (meaning auto), "auto", "light", or "dark"
    // color argument: "auto", "light", or "dark"

    function force_body_classlist(color) {
        const os_prefers_dark = window.matchMedia("(prefers-color-scheme: dark)").matches;
        if (color === "dark") {
            if (!document.body.classList.contains("dark")) {
                document.body.classList.add("dark");
            }
        } else if (color === "light") {
            if (document.body.classList.contains("dark")) {
                document.body.classList.remove("dark");
            }
        } else {
            // color === "auto"
            if (os_prefers_dark) {
                if (!document.body.classList.contains("dark")) {
                    document.body.classList.add("dark");
                }
            } else {
                if (document.body.classList.contains("dark")) {
                    document.body.classList.remove("dark");
                }
            }
        }
    }

    // This function runs every time the menu buttons (auto/light/dark) are
    // clicked.
    change_theme.set_color = function set_color(color) {
        force_body_classlist(color);
        localStorage.setItem("color", color);
    };

    // This function runs once on each page load.
    change_theme.set_theme_from_local_storage = function set_theme_from_local_storage() {
        const site_specific_preferred_color = localStorage.getItem("color") || "auto";
        const os_prefers_dark = window.matchMedia("(prefers-color-scheme: dark)").matches;
        if (site_specific_preferred_color === "dark") {
            // If the user has specifically chosen issarice.com to be in dark mode,
            // then honor that over the OS/browser-level preference.
            document.body.classList.add("dark");
        } else if ((site_specific_preferred_color === "auto") && os_prefers_dark) {
            // If the user has not set any specific setting for issarice.com, or has
            // set it to auto-mode, then use dark mode if the OS/browser wants it.
            document.body.classList.add("dark");
        }
    };

    // This one should not save the current setting in a cookie, because if you
    // click through to a new page, you are by definition in "movement mode" rather
    // than "absorption mode".
    change_theme.change_reader_mode = function change_reader_mode() {
        if (window.getSelection().toString() != "") {
            var closestZeroElem = window.getSelection().anchorNode.parentNode;
        } else {
            var mainElem = document.querySelector('main');
            // var mainElem = document.body;
            var childElems = mainElem.querySelectorAll('*');
            var closestZero = Infinity;
            var closestZeroElem = null;
            for (var i = 0; i < childElems.length; i++) {
                var rect = childElems[i].getBoundingClientRect();

                if (Math.abs(rect.top) < Math.abs(closestZero)) {
                    closestZeroElem = childElems[i];
                    closestZero = rect.top;
                }
            }
            // console.log(closestZeroElem);
            // console.log(closestZero);
        }

        if (document.body.classList.contains("absorption")) {
            var toc = document.querySelector('#TOC');
            if (toc) {
                var mainElem = document.querySelector('main');
                mainElem.before(toc);
                toc.style.position = 'fixed';
                toc.style.top = 0;
                toc.style.width = "150px";
                // toc.style.backgroundColor = "#eee8d5";
                mainElem.style.marginLeft = "150px";
            }

            document.body.classList.remove("absorption");
            document.getElementById("change-reader-mode-toggle").textContent = "movement";
        } else {
            var toc = document.querySelector('#TOC');
            if (toc) {
                var mainElem = document.querySelector('main');
                toc.style.position = "";
                toc.style.top = "";
                toc.style.width = "";
                // toc.style.backgroundColor = "#fdf6e3";
                mainElem.style.marginLeft = "";

                var titleBlock = document.querySelector('#title-block-header');
                titleBlock.after(toc);
            }


            document.body.classList.add("absorption");
            document.getElementById("change-reader-mode-toggle").textContent = "absorption";
        }

        closestZeroElem.scrollIntoView();
    };

    document.addEventListener('keydown', function(event) {
        if (event.key === 't' && event.target.tagName !== 'INPUT' && event.target.tagName !== 'TEXTAREA') {
            change_reader_mode();
        }
    });
}(window.change_theme = window.change_theme || {}));
