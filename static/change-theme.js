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
  } else {
    document.body.classList.add("wide");
    document.cookie = 'textWidthCookie=wide; max-age=31536000; path=/';
  }
}

function change_theme_color() {
  if (document.body.classList.contains("white")) {
    document.body.classList.remove("white");
    document.body.classList.add("dark");
    document.cookie = 'colorCookie=dark; max-age=31536000; path=/';
  } else if (document.body.classList.contains("dark")) {
    document.body.classList.remove("dark");
    document.cookie = 'colorCookie=; expires=Thu, 01 Jan 1970 00:00:00 UTC; path=/';
  } else {
    document.body.classList.add("white");
    document.cookie = 'colorCookie=white; max-age=31536000; path=/';
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

function set_theme_from_cookies() {
  if (change_theme_read_cookie("textWidthCookie")) {
    document.body.classList.add("wide");
  }
  if (change_theme_read_cookie("fontFamilyCookie")) {
    document.body.classList.add("sans");
  }
  if (change_theme_read_cookie("tableCookie")) {
    document.body.classList.add("wikitable");
  }
  if (change_theme_read_cookie("colorCookie") == "white") {
    document.body.classList.add("white");
  } else if (change_theme_read_cookie("colorCookie") == "dark") {
    document.body.classList.add("dark");
  }
}
