---
title: Pandoc
author: Issa Rice
created: 2014-10-31
date: 2014-10-31
status: notes
belief: possible
---

[Pandoc](http://johnmacfarlane.net/pandoc/index.html) is a convenient tool for converting documents between different formats---for instance to convert a markdown document into a PDF.
Another example: I [use Pandoc for this site](colophon) to convert from my markdown source documents to the HTML on the actual site.
With some creativity, one can use Pandoc to do accomplish some neat tasks.

# Installing

See my page on [[installing Haskell]] for more information.

# Going from markdown to HTML

To give a concrete example of going from markdown to HTML (besides the case of creating this site, as stated above), one might want to [compose an email in markdown and send it in HTML](https://www.quora.com/How-can-I-write-messages-in-Gmail-using-Markdown); how can this be done efficiently?

If you are on Linux and use a combination of tools like Vim and xclip in addition to Pandoc[^alternatives], then this can easily be achieved. After composing the email in Vim, simply write the buffer directly into Pandoc, convert the markdown to HTML, and send that into the clipboard with xclip:

[^alternatives]: Of course, these can all be replaced in part or whole with other
tools, as long as they have the necessary features. The editor must
either support markdown--HTML conversion and be able to use the
clipboard, or else be able to interact with the shell, for instance.

```
:w !pandoc -f markdown -t html | xclip -sel clip
```

Then just paste the results into Gmail using Control-V (or similar).

This procedure can then be bound to a command or a keyboard shortcut for
repeated use.

If you in addition choose to write the markdown buffer to a file, the
message will be locally backed up, as well as being on the Gmail servers
(which is good)---though you should really have a real backup method.


# Going from HTML to markdown

How about going the opposite direction?
A useful example here is if you want to [copy HTML from a website, retain its formatting, but convert it to markdown](https://www.quora.com/Is-there-a-service-or-program-that-lets-you-copy-text-from-a-website-directly-into-Markdown-retaining-all-formatting).

This is possible again using a combination of xclip and Pandoc.
After copying the HTML text from a website, one can do

```{.bash}
xclip -t text/html -o | pandoc -f html -t markdown
```

(Turn on the `-selection clip` flag on `xclip` if that doesn't work).

The other option, which is slighly more tedious, is to use something
like the online editor on WordPress and to paste in the HTML on the
"Visual" side and then go to the "Text" side to retrieve the converted
source for the HTML; then, place the source into a local HTML file (e.g.  `temp.html`) and run Pandoc on it using something like

```{.bash}
pandoc -o temp.md temp.html
```


# Pandoc filters

Using [pandocfilters](https://github.com/jgm/pandocfilters), one can trivially write scripts that modify the JSON representation of Pandoc documents.
For this website, I've written a custom URL filter that takes links of the form `[test](!STRING)` and converts them into a [DuckDuckGo bang expression](https://duckduckgo.com/bang.html).
For instance, writing `[Fishmans](!w)` will search Wikipedia for the string "Fishmans", and will take you to the page for the band Fishmans.

<!-- FIXME: write a more complete guide of how to use pandocfilers -->

I've also converted the Haskell filters on the Pandoc website to [their Python equivalents](https://github.com/riceissa/pandocfilters-examples).

# Filtering out messy HTML

From [this answer](http://stackoverflow.com/a/35812743/3422337):

```vim
:!%pandoc -f html -t markdown-raw_html-native_divs-native_spans
```

Or more fully:

```vim
:new
:r !xclip -sel clip -o -t text/html
:!%pandoc -f html -t markdown-raw_html-native_divs-native_spans --wrap=none
```
