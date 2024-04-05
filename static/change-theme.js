// License: CC0 https://creativecommons.org/publicdomain/zero/1.0/

function change_theme_read_cookie(name) {
  var cookies = document.cookie.split(';');
  for (var i = 0; i < cookies.length; i++) {
    var cs = cookies[i].split('=');
    if (cs[0].trimLeft() == name) {
      return cs.slice(1).join('=');
    }
  }
  return null;
}

function change_theme_text_width() {
  if (document.body.classList.contains("wide")) {
    document.body.classList.remove("wide");
    document.cookie = 'textWidthCookie=; expires=Thu, 01 Jan 1970 00:00:00 UTC; path=/';
    if (document.body.classList.contains("bigtable-temp")) {
      document.body.classList.remove("bigtable-temp");
      document.body.classList.add("bigtable");
    }
  } else {
    document.body.classList.add("wide");
    document.cookie = 'textWidthCookie=wide; max-age=31536000; path=/';
    if (document.body.classList.contains("bigtable")) {
      document.body.classList.remove("bigtable");
      document.body.classList.add("bigtable-temp");
    }
  }
}

function change_theme_color() {
  if (document.body.classList.contains("light")) {
    document.body.classList.remove("light");
    document.body.classList.add("dark");
    document.cookie = 'colorCookie=dark; max-age=31536000; path=/';
  } else if (document.body.classList.contains("dark")) {
    document.body.classList.remove("dark");
    document.cookie = 'colorCookie=; expires=Thu, 01 Jan 1970 00:00:00 UTC; path=/';
  } else {
    document.body.classList.add("light");
    document.cookie = 'colorCookie=light; max-age=31536000; path=/';
  }
}

function change_theme_font_family() {
  if (document.body.classList.contains("sans")) {
    document.body.classList.remove("sans");
    document.cookie = 'fontFamilyCookie=; expires=Thu, 01 Jan 1970 00:00:00 UTC; path=/';
  } else {
    document.body.classList.add("sans");
    document.cookie = 'fontFamilyCookie=sans; max-age=31536000; path=/';
  }
}

function change_theme_table() {
  if (document.body.classList.contains("wikitable")) {
    document.body.classList.remove("wikitable");
    document.cookie = 'tableCookie=; expires=Thu, 01 Jan 1970 00:00:00 UTC; path=/';
  } else {
    document.body.classList.add("wikitable");
    document.cookie = 'tableCookie=wikitable; max-age=31536000; path=/';
  }
}

// This one should not save the current setting in a cookie, because if you
// click through to a new page, you are by definition in "movement mode" rather
// than "absorption mode".
function change_reader_mode() {
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
}

document.addEventListener('keydown', function(event) {
  if (event.key === 't' && event.target.tagName !== 'INPUT' && event.target.tagName !== 'TEXTAREA') {
    change_reader_mode();
  }
});

function change_theme_set_color(color) {
  const site_specific_preferred_color = localStorage.getItem("color");
  if (site_specific_preferred_color) {
    if (site_specific_preferred_color !== color) {
      document.body.classList.remove(site_specific_preferred_color);
      document.body.classList.add(color);
      localStorage.setItem("color", color);
    }
  } else {
    localStorage.setItem("color", color);
  }
}

function set_theme_from_local_storage() {
  const site_specific_preferred_color = localStorage.getItem("color");
  const os_prefers_dark = window.matchMedia("(prefers-color-scheme: dark)").matches;
  if ((site_specific_preferred_color === "light") || (site_specific_preferred_color === "dark")) {
    // If the user has specifically chosen issarice.com to be a specific color,
    // then honor that over the OS/browser-level preference.
    document.body.classList.add(site_specific_preferred_color);
  } else {
    // Otherwise, default to the OS/browser-level preference.
    if (os_prefers_dark) {
      document.body.classList.add("dark");
    }
  }
}

function set_theme_from_cookies() {
  if (change_theme_read_cookie("textWidthCookie")) {
    document.body.classList.add("wide");
    if (document.body.classList.contains("bigtable")) {
      document.body.classList.remove("bigtable");
      document.body.classList.add("bigtable-temp");
    }
  }
  if (change_theme_read_cookie("fontFamilyCookie")) {
    document.body.classList.add("sans");
  }
  if (change_theme_read_cookie("tableCookie")) {
    document.body.classList.add("wikitable");
  }
  if (change_theme_read_cookie("colorCookie") == "light") {
    document.body.classList.add("light");
  } else if (change_theme_read_cookie("colorCookie") == "dark") {
    document.body.classList.add("dark");
  }
}
