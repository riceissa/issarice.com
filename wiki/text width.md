---
title: Text width
author: Issa Rice
created: 2017-10-17
date: 2017-10-17
---

When reading something continuously, it is nice to have the text width of the
page rather short, so that the reader's eyes don't have to travel too far to
find the next line.

When scanning a page, looking for information, it is nice to have the text
width *wide* so that more content fits on the page. This allows the eyes to
scan more content looking for the spot to begin reading. Otherwise the reader
has to scroll the page while also scanning with the eyes.

What if we allow the reader to freely toggle between the two? This is something
that is now possible thanks to client-side scripting on the web. As an
experiment, I have implemented a crude version of this idea. At the top of each
page there is a menu item labeled "Change {text width, color, font, table}";
clicking on "text width" will toggle between an almost-full window width and a
more compact width. Note that this requires JavaScript to be enabled for
`issarice.com`. Persistence is achieved through cookies, which are only ever
used for setting the theme. You can [see the source code of the script](https://github.com/riceissa/issarice.com/blob/master/static/change-theme.js).

# See also

- [[adaptive typography]], which expands this idea further