---
title: Emacs
author: Issa Rice
created: 2017-01-29
date: 2017-07-18
---

I use the text editor GNU Emacs for various tasks that my main text editor,
[Vim](vim), does not handle well.

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
I now have no artificial restriction on computer use
(in school, some teachers would not allow laptops in class, and taking a laptop
around to all my classes would have been annoying), it makes sense to
track my tasks in a version-controlled plain text file.
Prior to using Org mode, I had used a text file where lines began with the
scheduled date, so that I could sort the file to make the imminent tasks
"float" up to the top, but then I wanted to add intervals so that I could say
something like "reschedule this task one month after I complete it" -- and
reasoned that there ought to be someone who automated this in a plain text
environment.

I almost always use the graphical version of Emacs rather than the terminal
version.
This is because the terminal version is limited in multiple respects (Emacs
relies on a lot of chording that doesn't come through on a terminal emulator,
the terminal version doesn't allow mouse interaction, the terminal version
makes access to the menu -- which I like for modes I am not familiar with --
cumbersome, doesn't allow easy access to the system clipboard).
Note that this situation is the opposite of that in Vim: in Vim, the graphical
version is rather limited because it cannot access a full terminal emulator
(moreover, Vim doesn't rely on a lot of chording, allows mouse access even from
the terminal, and so on, so the caveats of terminal Emacs do not apply).

You can view my [`init.el`](https://github.com/riceissa/dotfiles/blob/master/.emacs.d/init.el)
in my dotfiles repository.

# Org mode routine

The following is how I usually use Org mode.
Since I don't know many of the more complicated features of Org mode,
I tend to stick to the basics.

-   I have a single Org file called `todo.org`.

-   Several times each day, I do `C-c a a` to open the agenda split window.
    I then use `n` and `p` to move between tasks, and usually hit `TAB` to
    open the task in a separate split window.
    From there, I can edit or reschedule (`C-c C-s`) or mark the task as
    done (`C-c C-t d`).
    After marking as done I archive with `C-c C-x C-a` (as long as there are no
    clocked periods for the task; otherwise I like to keep completed tasks around so
    that the clock table shows a more complete picture).

-   I create new tasks with `C-c c t`.

-   I also use Org mode for clocking tasks as I work.
    I move to the item being clocked with `C-c C-x C-j`.
    To clock in, I use `C-c C-x C-i` and to clock out
    I use `C-c C-x C-o`.
    I used to have a separate "Timesheet" section containing all clocked tasks
    with general task names like "Miscellaneous Wikipedia work", but these days
    I just clock tasks on the specific tasks themselves. This allows for a more granular look at what I have been working on. (It sounds obvious in
    retrospect that this new system is better, but it took me some time to realize this.)

-   I have a clock table with `:block today` that shows the time tracked for
    the current day.
    I update this table with `C-c C-c`.
    I have a second clock table with the current month's interval, e.g.
    `:tstart "<2017-07-01>" :tend "<2017-08-01>"` for the month of July 2017. This way I can get a rough
    idea of how much I have been working for the current month.
    Occasionally I create temporary clock tables within a task (to see how much total time I have spent on a task) or for all time (to try to get a long-term view of what I've been spending time on).

-   The whole file is tracked in [Git](git).
    I have a defined function to quickly snapshot the current state of the file.

-   I only track my time on weekdays, so that I can spend my weekends more "freely" without having to think about what I'm working on. I hope that this helps with relaxation and doing things more spontaneously, but I'm not sure how well it works.

# See also

- [More software I use](software%20I%20use.md)
