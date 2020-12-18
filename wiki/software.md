---
title: Software
author: Issa Rice
date: 2020-01-15
---

This page lists software I use or have used. I don't include web apps or plugins.
This page is a placeholder for now.

- [tmux]()
- Google Chrome and [Firefox]() for web browsing. These days I do most of my browsing in Chrome, because it's faster especially on JavaScript-heavy sites.
  (For most JavaScript-heavy web apps, often the easiest way to use them is to
  run them under an incognito Chrome window, rather than manually enabling a
  bunch of domains on NoScript or uMatrix.)
  I still use Firefox and like Firefox's handling of browsing history better (Chrome seems to have a short memory, and many things don't show up when I type it in the address bar).
- [Vim]() (mostly Neovim since about July or August 2020) with [various plugins](https://github.com/riceissa/dotfiles/blob/master/.vimrc#L8-L41) for most text editing.
- [Git]()
- Anki for spaced repetition
- [ELinks](), Links, or Lynx for lightweight browsing depending on what I want.
  ELinks has tabbed browsing which I find easy to use, but Links can show
  images with the `-g` flag. Lynx seems to do correct checking for SSL certificates and
  additionally has `-localhost -dump` that is suitable for producing plain text
  dumps of webpages.
- [Exuberant Ctags]()
- [Music On Console]() (MOC) for music
- [Newsbeuter]() (actually called Newsboat now)
- Ubuntu on laptop, and Ubuntu and Debian on server
- MATE as a desktop environment (MATE color selection tool is surprisingly useful)
- KeePassX
- Bash for my shell
- Pandoc
- I use a modified version of Solarized Light as a colorscheme in my terminal.
  By default, Solarized has various shades of gray in its 16-color palette,
  which makes some console programs difficult to use; I therefore replace those
  colors with the equivalents from Tango.
  You can see the [resulting values][colors].
- IPython (now called Jupyter Qt console)
- rxvt-unicode a.k.a. urxvt
  No strong preference for the most part, except that I dislike it when the
  terminal emulator intercepts Alt key mappings, like `Alt`-`f`.
- PDF.js or Atril or the Chrome PDF viewer for most PDF files.
  For short PDFs, PDF.js suffices, but for longer PDFs I usually download a
  copy and read them on Atril.
- `youtube-dl`
- GNU userland, mainly because that's what comes with Debian and Ubuntu and
  is what I'm most used to.
  I also install moreutils for `sponge`.
- [rsync](rsync)
- I often use `less` (e.g. instead of `tail -f` I use `less +F`)
- fzf, mostly for recalling commands in bash with CTRL-R.
- [Emacs](emacs) org mode, and Emacs in general for prose (Emacs handles long lines better than Vim, and when text isn't line-based like in code I find navigation more intuitive in Emacs)
- Zim Wiki for a local private wiki
- Python3 as a desktop calculator
- ag
- Foliate as ebook reader. I used to use FBReader/Calibre but both of them broke after an Ubuntu upgrade.
- Telegram desktop app -- I tried signing up via the web app but it didn't work so I installed the desktop app. Now that I have an account though, I could probably get away with using the web app.
- Redshift
- Tux Paint to make drawings for my [Tao Analysis Solutions](https://taoanalysis.wordpress.com/) blog
- Emacs+mozc for Japanese input

Programs in trial mode:

- arbtt

# See also

- [Colophon]()
- [Account names](account-names), for SaaS

# External links

- ["Choosing Software"][choose] by gwern

[choose]: https://www.gwern.net/Choosing%20Software "gwern. “Choosing Software - Gwern.net”."
[colors]: https://github.com/riceissa/dotfiles/blob/3631d8f2a129daab502682557fd37580ad656519/.Xresources#L29-L93
