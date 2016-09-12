---
title: Vim and newlines
author: Issa Rice
date: 2016-09-12
created: 2016-09-12
---

Questions:

  * Does Vim use NUL to represent newlines, or vice versa?
  * Why does Vim represent NUL and newlines the same way sometimes?
    Is it just some historical thing, or is there still a valid technical
    reason for doing this?
  * What do `\n`, `\r`, `^J`, and `^@` mean in different contexts?
    For instance `\n` means something different on each side of `:substitute`.
  * Why does Vim append `^J` to the end of a register ending in
    `^M`? For instance, try `:let @a='a^M'` then `:reg a`, where
    `^M` is inserted by doing `<C-V><C-M>`.
  * How does this newline representation come into play with the different line
    endings used on Windows, Mac, and Unix?

Some references to check out:

  * ["Newlines and nulls in Vim script"][vw]
  * Various help pages

[vw]: http://vim.wikia.com/wiki/Newlines_and_nulls_in_Vim_script "“Newlines and nulls in Vim script”. Vim Tips Wiki."
