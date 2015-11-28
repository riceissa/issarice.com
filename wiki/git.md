---
title: Git
description: A collection of useful/often-forgotten git commands
last_major_revision_date: 
license: "CC-BY"
tags: git, linux
aliases: git-commands, a-collection-of-often-forgotten-git-commands
---

Some useful commands:

- View all unadded files, including ones in <code>.gitignore</code>.

    ```bash
    git add -Anf
    ```

    `-A`: all; `-n`: dry run; `-f`: force files in `.gitignore`.

    See [this question](http://stackoverflow.com/questions/3801321/git-list-only-untracked-files-also-custom-commands).

- Dealing with submodules

    ```bash
    git submodule update --init 
    git submodule foreach git pull origin master
    ```

    See [here](http://stackoverflow.com/questions/5828324/update-git-submodule) and [here](http://blog.jacius.info/git-submodule-cheat-sheet/).

- [Getting Japanese to display](https://stackoverflow.com/questions/4144417/how-to-handle-asian-characters-in-file-names-in-git-on-os-x):

    ```bash
    git config --global core.quotepath false
    ```

- Check when the last revision date for a page on this site was last modified:

    ~~~{.bash}
    git blame -L '/last_major_revision_date: /,+1' wiki/PAGENAME.md
    ~~~

# Weird behavior

I'm documenting some weird behavior I've observed.

In `~/.gitconfig`:

```{.bash}
[core]
    pager = less -+S -r
```

Then running `git diff --color 3cc00f112bf~1 3cc00f112bf` in the [CP Wiki repo](https://github.com/riceissa/causeprioritization). This causes colors to show up, but the header doesn't show up at first. If you hit `G` to go to the bottom, then hit `g` to get back up, you can see the header.  You can do some pretty weird things with this, e.g. `git diff --color 3cc00f112bf~1 3cc00f112bf | fold | less -r` will make the color fade out in some regions, and you can also see strange character marks.

For reference, my `.gitconfig`:

``` {.bash}
[user]
    email = riceissa@gmail.com
    name = Issa Rice
[core]
    pager = less -+S
[pager]
    log = perl /usr/share/doc/git/contrib/diff-highlight/diff-highlight | less -+S
    show = perl /usr/share/doc/git/contrib/diff-highlight/diff-highlight | less -+S
    diff = perl /usr/share/doc/git/contrib/diff-highlight/diff-highlight | less -+S
[alias]
    # From https://git.wiki.kernel.org/index.php/Aliases#What.27s_new.3F
    new = !sh -c 'git log $1@{1}..$1@{0} "$@"'
    # See https://gist.github.com/mwhite/6887990 for where a lot of
    # these came from
    a = add
    # list branches sorted by last modified
    b = "!git for-each-ref --sort='-authordate' --format='%(authordate)%09%(objectname:short)%09%(refname)' refs/heads | sed -e 's-refs/heads/--'"
    br = branch
    c = commit
    ca = commit -a --verbose
    cam = commit -a -m
    ci = commit
    cm = commit -m
    co = checkout
    cob = checkout -b
    d = diff
    dc = diff --cached
    df = diff
    diff = diff --color
    ds = diff --stat
    # list aliases
    la = "!git config -l | grep alias | cut -c 7-"
    logn = log --name-only
    pullb = pull bitbucket master
    pullg = pull github master
    pullgh = pull github master
    pulll = pull origin master
    pullo = pull origin master
    pushb = push bitbucket master
    pushg = push github master
    pushgh = push github master
    pushh = push origin master
    pusho = push origin master
    s = status -s
    st = status
    wd = diff --color-words
    wdiff = diff --color-words
```

- <https://stackoverflow.com/questions/4144417/how-to-handle-asian-characters-in-file-names-in-git-on-os-x>
- [How do I change the remote a git branch is tracking?](http://stackoverflow.com/questions/4878249/how-do-i-change-the-remote-a-git-branch-is-tracking)
- [How to color the Git console in Ubuntu?](http://stackoverflow.com/questions/10998792/how-to-color-the-git-console-in-ubuntu)
