---
title: Software I use
author: Issa Rice
date: 2020-01-15
---

This page lists software that I currently use.

- [[tmux]]
- [[chrome|Google Chrome]] and [[Firefox]] for web browsing. These days I try to
  do most of my browsing in Firefox, because it does a better job of remembering
  pages I have visited in the past, which is important for me.
  (Chrome seems to have a short memory, and many things don't show up when I
  type it in the address bar).
  But Chrome is faster (especially on JavaScript-heavy sites), so I use it for
  sites like Gmail and Facebook, and then I'm often lazy so end up following
  links from within Chrome instead of copying the URL and visiting in Firefox.
  (For most JavaScript-heavy web apps, often the easiest way to use them is to
  run them under an incognito Chrome window, rather than manually enabling a
  bunch of domains on NoScript or uMatrix.) (Update: Since April 2021 when I bought a new computer, I've just been using Firefox since Firefox is now fast enough even for the JavaScript-heavy web apps, at least for now...)
- [[Vim]] (mostly Neovim since about July or August 2020) with [various plugins](https://github.com/riceissa/dotfiles/blob/master/.vimrc#L8-L41) for most text editing.
- [[Git]]
- [[Anki]] for spaced repetition
- [[ELinks]], Links, or Lynx for lightweight browsing depending on what I want.
  ELinks has tabbed browsing which I find easy to use, but Links can show
  images with the `-g` flag. Lynx seems to do correct checking for SSL certificates and
  additionally has `-localhost -dump` that is suitable for producing plain text
  dumps of webpages.
- [[Exuberant Ctags]]
- [[Music On Console]] (MOC) for music
- [[Newsbeuter]] (actually called Newsboat now)
- Ubuntu on laptop, and Ubuntu and Debian on server
- KDE Plasma as a desktop environment (I used to use MATE but tried KDE on a whim and found that it has fewer annoying bugs)
- KeePassX
- Bash for my shell (I've tried both zsh and fish but found them more annoying than useful. I think bash+fzf is sufficient to make the command line really pleasant to use)
- Pandoc
- I use a modified version of Solarized Light as a colorscheme in my terminal.
  By default, Solarized has various shades of gray in its 16-color palette,
  which makes some console programs difficult to use; I therefore replace those
  colors with the equivalents from Tango.
  You can see the [resulting values][colors].
- IPython (now called Jupyter Qt console)
- kitty (terminal emulator) -- the only annoying things so far are that when I resize the window, some gaps appear, and when I try to attach to a tmux session via ssh it fails (there's some way to fix it by copying terminfo files, but it seemed complicated so I haven't tried it yet).
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
- Emacs+mozc for Japanese and Russian input (I should use something like ibus but they require restarting the computer and they also stop working after upgrades and such. Since I don't use Japanese/Russian input much, doing everything via Emacs has been acceptable to me so far.)
- Flameshot
- spaced inbox (written myself)
- urlwatch
- Steven Black's [hosts](https://raw.githubusercontent.com/StevenBlack/hosts/master/alternates/gambling-porn/hosts) file
- Xournal, for signing some contracts (Xournal allows one to draw over the PDF and then export the result as PDF)
- Sumatra PDF -- seems like a pretty great PDF/DJVU/ebook reader. I really like that it provides tabs, which most PDF readers don't.
- Obsidian -- for editing this website. I use [this filter](https://github.com/riceissa/pandoc-wikilinks-filter) that I wrote which makes the same Markdown files that work on Obsidian also be compilable using Pandoc. Actually it looks like at some point (probably after I wrote my own filter) Pandoc implemented [alternative wikilink syntaxes](https://pandoc.org/MANUAL.html#extension-wikilinks_title_after_pipe) so I should probably just use that instead.
- SuperMemo

Web apps (I'm ignoring social media, passive content consumption services like YouTube, and video conferencing apps):

- Gmail, Google Calendar, Google Forms
- Roam
- Duolingo
- WordPress

Programs in trial mode:

- arbtt
- ripgrep
- broot
- fdfind

# See also

- [[Colophon]]
- [[Account names]], for SaaS
- [[Firefox]] for my Firefox plugins

# External links

- ["Choosing Software"][choose] by gwern

[choose]: https://www.gwern.net/Choosing%20Software "gwern. “Choosing Software - Gwern.net”."
[colors]: https://github.com/riceissa/dotfiles/blob/3631d8f2a129daab502682557fd37580ad656519/.Xresources#L29-L93
