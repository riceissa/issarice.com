---
title: Vim
#description: 
author: Issa Rice
creation_date: 2015-02-28
last_major_revision_date: 2015-02-28
language: English
# accepts "notes", "draft", "in progress", or "mostly finished"
status: notes
# accepts "certain", "highly likely", "likely", "possible", "unlikely", "highly unlikely", "remote", "impossible", "log", "emotional", or "fiction"
belief: possible
# accepts "CC0", "CC-BY", or "CC-BY-SA"
license: CC-BY
tags: vim, computing
#aliases: 
---

I'm still learning more about Vim even today, even though I started using it back in 2011 (or even before that).
One thing I learned really recently is that Vim has very sophisticated ex mode features.
I had always been frustrated by the fact that ex mode seemed way too limited, since I couldn't even get bash-style keys like `<C-a>` to go to the beginning of the line to work.
But it turns out I was wrong; see `:h cmdline.txt` for more, as well as `:h usr_20.txt`, which is referenced in the first help page.
But for instance, you can type `q:` to enter essentially insert mode within ex mode, which allows you to do regular Vi keys to edit commands.
I also learned that `<C-b>` is the right way to go to the beginning of a line in ex mode; you can change this with `cnoremap <C-a> <C-b>` too though; also see `:h emacs-keys` to make keybindings more "sane".
