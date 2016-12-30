---
title: tmux
author: Issa Rice
date: 2016-10-27
created: 2016-10-26
---

For now, this page is mostly a placeholder.

I use tmux to spawn multiple shell sessions while I work.
Even though I mainly use Terminator (which supports tabs and window splitting)
as my terminal emulator, I find that tmux gives me enough flexibility (through
its windows and panes) that I don't use the corresponding features in
Terminator.
On my servers, I keep a tmux session running so that I can attach to it to
continue working where I stopped.

My tmux configuration file is [available on GitHub][conf].

Besides working in tmux, I make use of tmux in a [shell script][keep] that runs
as a cron job.
The script just opens and quits Vim and Mutt in a tmux session; the cron job
runs every minute to keep Vim and Mutt in memory.

[conf]: https://github.com/riceissa/dotfiles/blob/master/.tmux.conf
[keep]: https://github.com/riceissa/dotfiles/blob/master/.local/bin/keep_vim_mutt.sh
