---
title: Git
description: A collection of useful/often-forgotten git commands
last-major-revision-date: 
license: "CC-BY"
tags: git, linux
aliases: git-commands, a-collection-of-often-forgotten-git-commands
---


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

[Getting Japanese to display](https://stackoverflow.com/questions/4144417/how-to-handle-asian-characters-in-file-names-in-git-on-os-x):

```bash
git config --global core.quotepath false
```

# Weird behavior

I'm documenting some weird behavior I've observed.

In `~/.gitconfig`:

```
[core]
    pager = less -+S -r
```

Then running `git diff --color 3cc00f112bf~1 3cc00f112bf` in the [CP Wiki repo](https://github.com/riceissa/causeprioritization). This causes colors to show up, but the header doesn't show up at first. If you hit `G` to go to the bottom, then hit `g` to get back up, you can see the header.  You can do some pretty weird things with this, e.g. `git diff --color 3cc00f112bf~1 3cc00f112bf | fold | less -r` will make the color fade out in some regions, and you can also see strange character marks.
