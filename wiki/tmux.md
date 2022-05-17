---
title: tmux
author: Issa Rice
date: 2017-03-26
created: 2016-10-26
---

For now, this page is mostly a placeholder.

I use tmux to spawn multiple shell sessions while I work.
On my servers, I keep a tmux session running so that I can attach to it to
continue working where I stopped.

My tmux configuration file is [available on GitHub][conf].

Besides working in tmux, I make use of tmux in a [shell script][keep] that runs
as a cron job.
The script just opens and quits Vim and Mutt in a tmux session; the cron job
runs every minute to keep Vim and Mutt in memory.

# See also

* [[software I use]] for more about the software I use

[conf]: https://github.com/riceissa/dotfiles/blob/master/.tmux.conf
[keep]: https://github.com/riceissa/dotfiles/blob/master/.local/bin/keep_vim_mutt.sh
