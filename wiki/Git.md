---
title: Git
author: Issa Rice
created: 2013-03-18
date: 2016-12-29
---

I use Git to version-control my writings and software.

I tend to use Git both on the command-line as well as in Vim using
[fugitive.vim](https://github.com/tpope/vim-fugitive) and
[gv.vim](https://github.com/junegunn/gv.vim).
I also tend to look through commits and other information on GitHub (`:Gbrowse`
makes it easy to go directly from Vim to the listing on GitHub).

For my Git configuration, see my [`.gitconfig`][gitconfig] and
[`.cvsignore`](https://github.com/riceissa/dotfiles/blob/master/.cvsignore)
([global ignore file](https://github.com/tpope/vim-pathogen#faq "Tim Pope. “tpope/vim-pathogen”. GitHub. Retrieved November 20, 2017.")).

# Some useful commands

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

- Check when the last revision date for a page on this site was last modified:

    ~~~{.bash}
    git blame -L '/date: /,+1' wiki/PAGENAME.md
    ~~~

# Weird behavior

I'm documenting some weird behavior I've observed.

In `~/.gitconfig`:

```{.bash}
[core]
    pager = less -+S -r
```

Then running `git diff --color 3cc00f112bf~1 3cc00f112bf` in the [CP Wiki repo](https://github.com/riceissa/causeprioritization). This causes colors to show up, but the header doesn't show up at first. If you hit `G` to go to the bottom, then hit `g` to get back up, you can see the header.  You can do some pretty weird things with this, e.g. `git diff --color 3cc00f112bf~1 3cc00f112bf | fold | less -r` will make the color fade out in some regions, and you can also see strange character marks.

- [How do I change the remote a git branch is tracking?](http://stackoverflow.com/questions/4878249/how-do-i-change-the-remote-a-git-branch-is-tracking)
- [How to color the Git console in Ubuntu?](http://stackoverflow.com/questions/10998792/how-to-color-the-git-console-in-ubuntu)

# See also

* [[Software]] for more about the software I use

[gitconfig]: https://github.com/riceissa/dotfiles/blob/master/.gitconfig
