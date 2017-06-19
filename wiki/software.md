---
title: Software
author: Issa Rice
date: 2017-03-27
---

This page lists software I use or have used.
This page is a placeholder for now.

- [tmux]()
- [Firefox]() for the vast majority of daily browsing; I also use Google Chrome
  for Facebook and Gmail, and occasionally for some other JavaScript-heavy sites
  that I don't want to view with Firefox.
  For most JavaScript-heavy web apps, often the easiest way to use them is to
  run them under an incognito Chrome window, rather than manually enabling a
  bunch of domains on NoScript or uMatrix.
- [Vim]() with various plugins for most text editing.
- [Git]()
- [ELinks](), Links, or Lynx for lightweight browsing depending on what I want.
  ELinks has tabbed browsing which I find easy to use, but Links can show
  images with the `-g` flag. Lynx seems to do correct checking for SSL certificates and
  additionally has `-localhost -dump` that is suitable for producing plain text
  dumps of webpages.
- [Exuberant Ctags]()
- [Music On Console]()
- [Newsbeuter]()
- Ubuntu on laptop and Ubuntu and Debian on server
- MATE as a desktop environment
- KeePassX
- Bash for my shell
- Pandoc
- [mutt]() for sending mail sometimes
- I use a modified version of Solarized Light as a colorscheme in my terminal.
  By default, Solarized has various shades of gray in its 16-color palette,
  which makes some console programs difficult to use; I therefore replace those
  colors with the equivalents from Tango.
  You can see the [resulting values][colors].
- IPython (now called Jupyter Qt console)
- htop
- rxvt-unicode a.k.a. urxvt
  No strong preference for the most part, except that I dislike it when the
  terminal emulator intercepts Alt key mappings, like `Alt`-`f`.
- Virtualbox
- PDF.js or MuPDF for most PDF files.
- Still looking for a good epub reader.
  I currently use FBReader but find the scrolling mechanism annoying.
- `youtube-dl`
- GNU userland, mainly because that's what comes with Debian and Ubuntu and
  is what I'm most used to.
  I also install moreutils for `sponge`.
- LibreOffice Calc for converting between CSV and XLS.
  I know almost nothing about it, but it seems to do what I want.
- I often use `less` (e.g. instead of `tail -f` I use `less +F`)
- fzf, mostly for recalling commands in bash with CTRL-R.

Programs in trial mode:

- ag
- `mpsyt`
- arbtt
- [Emacs](emacs) org mode
- `cmark-gfm` for Markdown processing; I've now used it for at least one blog
  post, and it is now [used on GitHub](https://githubengineering.com/a-formal-spec-for-github-markdown/).
  If more extensions are written for CommonMark (math, tables, metadata
  headers), and if the standard is adopted more widely, it probably makes sense
  to stop using Pandoc's Markdown.

# See also

- [Colophon]()

# External links

- ["Choosing Software"][choose] by gwern

[choose]: https://www.gwern.net/Choosing%20Software "gwern. “Choosing Software - Gwern.net”."
[colors]: https://github.com/riceissa/dotfiles/blob/3631d8f2a129daab502682557fd37580ad656519/.Xresources#L29-L93
