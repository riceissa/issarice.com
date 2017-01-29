---
title: Emacs
author: Issa Rice
created: 2017-01-29
date: 2017-01-29
---

I use the text editor GNU Emacs for various tasks that my main text editor,
[Vim](wiki/vim.md), does not handle well.

As I have written [elsewhere](http://vim.wikia.com/wiki/Working_with_long_lines?useskin=monobook),
Vim does a poor job of handling files with long lines.
When programming or writing prose under my control, this is not a problem:
the programming languages I tend to use have ways of forcing a linebreak, and
markup languages like Markdown and LaTeX allow single linebreaks within
paragraphs.

However, I still manage to encounter some files with long lines, most prominently
when editing the English Wikipedia, where it is standard for paragraphs to consist
of a single long line.
For simple edits, just using the browser's text field suffices, but for more involved
editing tasks I've found it useful to learn Emacs.
With a bit of practice, Emacs becomes much more efficient than the standard CUA
keybindings will allow.

I also use Org mode.
Ever since [taking up contract
work](https://contractwork.vipulnaik.com/worker.php?worker=Issa+Rice),
I've found a need to schedule many tasks days or weeks in advance, to
the point where I can't keep all of it straight in my head.
In junior high and high school I had used paper planners, but since
I now have no artificial restriction on computer use, it makes sense to
track my tasks in a version-controlled plain text file.
Prior to using Org mode, I had used a text file where lines began with the
scheduled date, so that I could sort the file to make the imminent tasks
"float" up to the top, but then I wanted to add intervals so that I could say
something like "reschedule this task one month after I complete it" -- and
reasoned that there ought to be someone who automated this in a plain text
environment.

I consider myself an Emacs novice.
