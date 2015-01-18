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
