---
title: Software I use
author: Issa Rice
date: 2024-04-30
---

This page lists software that I currently use.

- [[Firefox]] for web browsing. I prefer Firefox because it does a better job of remembering
  pages I have visited in the past, which is important for me.
  (Chrome seems to have a short memory, and many things don't show up when I
  type it in the address bar.)
- [[Anki]] for spaced repetition
- Windows 10 on laptop, and Ubuntu LTS and Debian stable on server
- KeePassXC
- [Emacs](emacs) org mode, and Emacs in general for prose (Emacs handles long lines better than Vim, and when text isn't line-based like in code I find navigation more intuitive in Emacs). On the other hand, I find Emacs to be quite terrible for code editing because it doesn't operate on "logical lines" the way Vim does, and code editing on Emacs also causes wrist pain for me.
- f.lux
- [spaced inbox](https://github.com/riceissa/spaced-inbox)
- Sumatra PDF -- seems like a pretty great PDF/DJVU/ebook reader. I really like that it provides tabs, which most PDF readers don't. It also displays epubs just like a PDF whereas most epub readers try to do weird pagination stuff that just makes it harder to read the book.  For large or permanent PDFs (i.e. ones that I download onto my computer) I use Sumatra. For random PDFs I come across while browsing the web, I usually just use the built-in PDF viewer in Firefox.
- Obsidian -- for editing this website
- [pdftextfmt](https://github.com/riceissa/pdftextfmt/) for cleaning up copied text from PDFs
- SuperMemo
- [iTunes 12.7.4.80](https://discussions.apple.com/docs/DOC-6562#versions) for syncing with my old iPod Touch gen 2
- Git-Bash
- WSL 2 -- development on Windows is very annoying but at least WSL gives me a sane Linux environment
- FreeTube
- GnuCash -- I would like to switch to a plaintext accounting system one day, but I think they are too error-prone and unintuitive to use; see [this thread](https://www.reddit.com/r/plaintextaccounting/comments/1bh3x7o/toward_a_more_intuitive_input_syntax_for_plain/) where I proposed an alternative syntax.
- Command-line tools
	- [[tmux]]
	- GNU userland, mainly because that's what comes with Debian and Ubuntu and is what I'm most used to.
	- fzf, mostly for recalling commands in bash with CTRL-R.
	- ripgrep -- replaces grep/ag. I still do use grep on places where I can't get ripgrep. But ripgrep has saner defaults so I don't even need to bother to look up which flags to use.
	- GHCi as a desktop calculator
	- Pandoc
	- [[Exuberant Ctags]]
	- yt-dlp
	- [[Newsbeuter]] (actually called Newsboat now)
	- [[Vim]] (mostly Neovim since about July or August 2020) with [various plugins](https://github.com/riceissa/dotfiles/blob/master/.vimrc#L8-L42) for most text editing.
	- [[Git]]
	- Bash for my shell (I've tried both zsh and fish but found them more annoying than useful. For example, zsh's Ctrl-w only deletes back to punctuation rather than to whitespace. I think bash+fzf is sufficient to make the command line really pleasant to use)
	- I use a modified version of Solarized Light as a colorscheme in my terminal. By default, Solarized has various shades of gray in its 16-color palette, which makes some console programs difficult to use; I therefore replace those colors with the equivalents from Tango. You can see the [resulting values][colors].
	- urlwatch

Web apps (I'm ignoring social media/messaging, passive content consumption services like YouTube, video call apps, and LLMs):

- Gmail
- Google Calendar
- Google Voice
- Roam Research
- Remnote -- not a heavy user, but I am trying this out as a way to combine note-taking and flashcards. Before I used it I thought it was crappy software, but [this podcast episode](https://open.spotify.com/episode/3ZI6NxCOWJ066rGlv16gxp) convinced me to give it a try.
- WordPress.com
- Overleaf

Programs in trial mode:

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
