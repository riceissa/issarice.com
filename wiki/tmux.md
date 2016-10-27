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

    # Use 256 colors
    set -g default-terminal "screen-256color"

    set-option -g default-shell /bin/zsh

    # Make <C-[> work properly in Vim
    set -s escape-time 0

    unbind C-b
    #set -g prefix C-q
    #bind C-q send-prefix
    set -g prefix C-Space
    # this one is to pass in a literal one right?
    bind C-Space send-prefix

    # tmux changed its mouse options in going from 2.0 to 2.1, so we make it work
    # in all versions.
    # for tmux >= 2.1
    set -g mouse on
    # for tmux < 2.1
    #set -g mode-mouse on
    #set -g mouse-resize-pane on
    #set -g mouse-select-pane on
    #set -g mouse-select-window on

    set -g history-limit 10000

    # Use Vi keys; see http://blog.sanctum.geek.nz/vi-mode-in-tmux/ and
    # https://robots.thoughtbot.com/love-hate-tmux
    set-window-option -g mode-keys vi
    bind-key -t vi-copy 'v' begin-selection
    bind-key -t vi-copy 'y' copy-selection
    bind -t vi-copy Escape cancel
    #bind h select-pane -L
    #bind j select-pane -D
    #bind k select-pane -U
    #bind l select-pane -R

    # for newer tmux? from http://unix.stackexchange.com/questions/146825/tmux-new-pane-has-home-directory-as-default-instead-of-previous-directory
    # This preserves the directory when splitting panes.
    bind '%' split-window -h -c '#{pane_current_path}'  # Split panes horizontal
    bind '"' split-window -v -c '#{pane_current_path}'  # Split panes vertically

    # Also note that tmux doesn't process ~/.bashrc so do
    # `echo 'source ~/.bashrc' >> ~/.bash_profile`; see
    # http://stackoverflow.com/a/16225913 for more
