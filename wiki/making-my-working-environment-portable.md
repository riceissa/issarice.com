---
title: Making my working environment portable
author: Issa Rice
date: 2016-08-28
---

Just some notes for now.

  * Making configuration files for common programs (vim, etc.) available
    online.
      * Difficulties with this: different operating systems might have
        different software or versions of the same software available, making
        configuration files apply inconsistently; some parts of configuration
        files refer to local parts in the file system that might not exist in
        all systems (e.g. my music player configuration file points to an
        external drive that only exists for my laptop) and these programs might
        not offer ways to make configuration files conditional on existence of
        such paths; some operating systems ship with their own default
        configuration files (e.g. Debian ships with `debian.vim` which does
        things like disable modelines in Vim, others ship with default versions
        of `~/.bashrc`), which presents difficulties with respect to merging
        these separate configuration files.
  * Placing more things in public/online (especially on GitHub) so they're
    easily accessible.
  * Dealing with "cloud software"
  * Also the problem of remembering passwords when using an arbitrary computer
  * One problem I've had: I like to use Linux Mint for my main computer, but
    some of my old computers (which I use once in a while) have Debian, and UW
    CSE lab computers use Fedora. Dealing with different distros and versions
    of software on computers is slightly tricky (e.g. compiling documents with
    LaTeX or Pandoc could yield different output). Even dealing with Vim
    plugins is slightly tricky, since e.g. Fedora's Vim doesn't seem to have
    Python (so things like UltiSnips don't work) -- actually, I just needed to
    use the `vimx` binary.
  * Most of the time this isn't such a big deal. I have a laptop that I can
    take with me pretty much anywhere, so everything is already set up in terms
    of software (though there is still the challenge of setting up the physical
    working surface).
  * One way to deal with this is to learn how to work efficiently with the
    defaults of the most commonly available software.
    So something like knowing the shortcuts for Bash, Vim, and Firefox/Chrome.
    Though of course, if you're going to work for an extended period of time at
    a new machine, then it probably makes sense to try to copy over some config
    files.
    See also ["On Configuration"](http://sstephenson.us/posts/on-configuration).
    Rob Pike says something interesting in an
    [interview](https://usesthis.com/interviews/rob.pike/):

    > I don't install a lot of extra stuff on those Macs, mostly to reduce
    > maintenance. I like the freedom to wipe and reinstall without losing my
    > world

  <!-- * The [principle of temporal locality][loc] says that the same values are accessed frequently. In terms of web URLs, this means that if I visit each of Facebook and GMail once, then Firefox will remember a much larger fraction of the --> 

# External links

  * [How to Efficiently Work Offline](http://www.wikihow.com/Efficiently-Work-Offline) by Vipul Naik

[loc]: https://en.wikipedia.org/wiki/Locality_of_reference
