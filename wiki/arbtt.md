---
title: arbtt
author: Issa Rice
created: 2017-02-06
date: 2017-02-06
---

[arbtt](http://arbtt.nomeata.de/) is the "automatic, rule-based time tracker".
It is a time-tracking program that runs in the background, recording which
windows are open, which window has focus, and so on.
It has a separate `arbtt-stats` command that displays the recorded information
in various ways -- the user is expected to write suitable rules so that the
summary is interesting.

The documentation is pretty good, and will give an idea of what it can do:

* [Configuring the arbtt categorizer
  (arbtt-stats)](http://arbtt.nomeata.de/doc/users_guide/configuration.html)
* [Effective Use of
  Arbtt](http://arbtt.nomeata.de/doc/users_guide/effective-use.html) (by gwern)

As gwern's guide mentions, setting informative window titles is important.
Most of my time on the computer is spent in a web browser or on a terminal.
Both [Firefox](wiki/firefox.md) and Google Chrome already set good titles, so
for me the challenge was mostly trying to make sure the terminal application I
use sets titles correctly.

The configuration is split across three programs:

* Vim, which sets the title correctly under urxvt without tmux, but fails to do
  so under urxvt with tmux.
* tmux, which needs to be told to allow setting the title.
* Bash, to use the prompt function feature to set the window title to the
  previously-run command.

Shorten tmux pane titles with [this answer](https://superuser.com/questions/585007/tmux-configure-length-of-titles).

Potentially relevant is [this](https://stackoverflow.com/questions/14356857/how-to-show-current-command-in-tmux-pane-title).

Some problems:

* For long commands, it's problematic that the command that ran *right before*
  the long command is what gets displayed.
  For instance my music player is usually run once and lasts for days at a time
  in its own tmux window.
* Possible security problems with escape sequences?
* tmux 2.3 seems to offer the ability set the window title and pane title
  separately, but Ubuntu 16.10 has tmux 2.2, so the tmux status shows less
  useful information (although Vim does a good job of setting the title).

# See also

* [Software](wiki/software.md) for other software I use
