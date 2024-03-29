---
title: Japanese input on the command line (framebuffer)
tags: japan, linux
---


# Upshot

- `uim-fep` seems to be the best option, on Bash.
- Using [[Emacs]] is quite possibly the best way overall, even if you’re a hardcore [[Vim]] user (like me)

## Things to add (it has been a while...):

- Where to place the config files?
- Graphical Emacs has a setup wizard which produces its own config files (even for Japanese input); what did I do with those?

# uim-fep

(at the moment I forgot where I was supposed to place this...)

```scheme
;; -*- mode: scheme -*-
;; Place this file as ~/.uim.  This file overrides any settings from
;; files in ~/.uim.d/customs

(define default-im-name 'anthy)

(define generic-on-key '("<IgnoreShift><Control>\\"))
(define generic-on-key? (make-key-predicate '("<IgnoreShift><Control>\\")))
(define generic-off-key '("<IgnoreShift><Control>\\"))
(define generic-off-key? (make-key-predicate '("<IgnoreShift><Control>\\")))

(define generic-shrink-key? '("<Control>j"))
(define generic-extend-key? '("<Control>k"))
(define anthy-shrink-segment-key? 'generic-shrink-key?)
(define anthy-extend-segment-key? 'generic-extend-key?)
```

Run this using `uim-fep -u anthy` or just `uim-fep` if you have `(define default-im-name 'anthy)` in `~/.uim`.

Also run `uim-pref-gtk` to get a graphical settings menu.


- `Ctrl`-`i` is eaten up by Bash (since it seems to get confused with the tab character), so one cannot set it to use as one of the user-defined keys.


# Emacs

I have the following in my `~/.emacs`.

```scheme
(set-fontset-font "fontset-default"
          'japanese-jisx0208
          '("IPAexGothic" . "iso10646-1"))
(prefer-coding-system 'utf-8)

;; This speeds up input?
(if (>= emacs-major-version 23)
    (setq anthy-accept-timeout 1))
```

Basic usage:

1. Start emacs using `emacs -nw`.
2. Type `Ctrl`-`\` which prompts the user for an input method.
3. Type `japanese-anthy`.

**2017 update**: I am never on the framebuffer these days, but for Japanese
input on Emacs I have switched to mozc.
The relevant config lines are [here](https://github.com/riceissa/dotfiles/blob/222c30966090592933fe208a565530ea5d08a455/.emacs.d/init.el#L13-L20).

# Packages to install (Debian)

- anthy-el, uim-anthy, uim-fep

