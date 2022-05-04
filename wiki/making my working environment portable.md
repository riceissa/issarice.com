---
title: Making my working environment portable
author: Issa Rice
date: 2016-08-28
---

Just some notes for now.

-   Making configuration files for common programs (Vim, etc.) available
    online.
    -   Difficulties with this: different operating systems might have
        different software or versions of the same software available, making
        configuration files apply inconsistently; some parts of configuration
        files refer to local parts in the file system that might not exist in
        all systems (e.g. my music player configuration file points to an
        external drive that only exists for my laptop) and these programs might
        not offer ways to make configuration files conditional on existence of
        such paths (Git's `~/.gitconfig` has no support for conditionally
        setting options, tmux only has a dreadful
        [`if-shell`](https://shapeshed.com/custom-vim-bindings-in-tmux-2-4/),
        etc.); some operating systems ship with their own default
        configuration files (e.g. Debian ships with `debian.vim` which does
        things like disable modelines in Vim, others ship with default versions
        of `~/.bashrc`), which presents difficulties with respect to merging
        these separate configuration files.
-   Placing more things in public/online (especially on GitHub) so they're
    easily accessible.
-   Dealing with "cloud software"
-   Also the problem of remembering passwords when using an arbitrary computer
-   One problem I've had: I like to use Linux Mint for my main computer, but
    some of my old computers (which I use once in a while) have Debian, and UW
    CSE lab computers use Fedora. Dealing with different distros and versions
    of software on computers is slightly tricky (e.g. compiling documents with
    LaTeX or Pandoc could yield different output). Even dealing with Vim
    plugins is slightly tricky, since e.g. Fedora's Vim doesn't seem to have
    Python (so things like UltiSnips don't work) -- actually, I just needed to
    use the `vimx` binary.
-   Most of the time this isn't such a big deal. I have a laptop that I can
    take with me pretty much anywhere, so everything is already set up in terms
    of software (though there is still the challenge of setting up the physical
    working surface).
-   One way to deal with this is to learn how to work efficiently with the
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

    But even with this approach, there remains the problem of different
    operating systems shipping with different versions or stock configuration
    files.
    Ubuntu 16.10 ships with the bash aliases `ll`, `la`, and `l` for easy
    access to some common flags on `ls`.
    But Debian 8 comments these lines out!
    To access to clipboard on Vim, on Debian-based distros I must install the
    GUI Vim package, and use the `vim` binary.
    But on Fedora, I must use the `vimx` binary.
    These are portable userland utilities, and yet due to a difference of
    convention, one's actual "working environment" is not truly portable.

  <!-- * The [principle of temporal locality][loc] says that the same values are accessed frequently. In terms of web URLs, this means that if I visit each of Facebook and Gmail once, then Firefox will remember a much larger fraction of the -->

Particularly when editing text, I find it incredibly irritating when it takes a
lot of time to go from my thoughts to the form of text on the screen.
Learning [Vim](vim) has helped with this, possibly to a great extent
(it is difficult to know because I learned it in small increments -- being
forced to use a primitive editor and finding the experience jarring perhaps
gives a good idea of how much I have internalized).

It is possible to detect each cause of editing slowness and add some speedup
each time, but the writing of mappings, plugins, or of researching them *itself
takes a lot of time*.
The plugins could have strange bugs in them that could screw me up down the
line (in some unforeseen way), which is rarer for the "core program".
I've found it difficult to anticipate in advance what kinds of configuration
saves me time in the long run, which ones I decide to stick to, and which ones
I end up *forgetting*.

Software configuration is also incredibly fragile.
Some examples:

- I wrote a series of mappings in Vim to make copy-pasting easier.
  Unfortunately, the particular way in which I was calling Vim script functions
  [caused older versions of Vim to crash](https://github.com/riceissa/vim-cuaccp/blob/595787e9e9a0ee68143fedb4124fedb663f7d1d1/plugin/cuaccp.vim#L17-L24).
  I didn't track the time it took to trace the cause and fix my mappings, but
  it was probably a few hours.
  <!-- rewrite: Was spending these few hours in frustration to make copy-pasting using this
  mapping not crash Vim so that I would save time each time I copy-pasted
  something in older versions of Vim and save myself from minor frustration
  each time I copy-pasted worth it? -->

- Newer versions of [Git](git) require adding `default = simple` in the
  push section of one's configuration file in order to preserve the old pushing
  behavior.
  But in older versions of Git, having this line causes Git to spit out an
  error.
  Moreover, the Git configuration syntax does not allow conditional (e.g. on
  Git version) settings.
  This means one must rely on some shell script to generate that line
  conditionally, or to keep two copies of the Git configuration file, or to
  manually remove that line when using older versions of Git, or something like
  that.
  For now I have opted for the final approach, because I rarely use older
  versions of Git.
  But this is the kind of interesting (and frustrating, depending on one's
  mood) problems one runs into in trying to make one's working environment
  portable.

In a "getting things done" mindset, I tend to view the act of configuring
software similarly to writing software or reading information or hiring
someone.
There is some cost to me in the process, and hopefully I get something useful
out of it that helps me accomplish my goals.
What is different?
With software configuration, the cost involved is mainly the research and
experimentation time, as well as some frustration when the software doesn't
work after configuring.
The mental experience is also a little different, because I have to deal with
idiosyncrasies of the configuration API provided by the particular software in
question.

TODO talk about "configuration bankruptcy"; I've encountered the concept most
frequently as ".emacs bankruptcy".

More generic software rant: I encounter *a lot* of small software-related
nuisances in my daily life.
And, having learned how to program, I know that, theoretically, I could spend
time digging into each problem, contacting the software author or whatever
(most of the software I use is free software and actively maintained, so this
is possible), filing a bug report or working to trace the error/fix it.
But would I do that for such a small nuisance?
For any *particular* nuisance, it seems like the total amount of time lost from
it is less than the expected time it would take for me to fix the problem.
So in the long run, the problems that get fixed are the serious flaws, or the
ones that are fun to fix, or that seem easy to fix, and so on, and I'm left
with generally good software that just doesn't work *quite* right.

Aside: the "SAAS approach" to this problem is to create one instance of the
environment, which eliminates the need for portability.

# External links

-   [How to Efficiently Work Offline](http://www.wikihow.com/Efficiently-Work-Offline) by Vipul Naik
-   ["Is It Worth the Time?"](https://xkcd.com/1205/) (yes, it's xkcd, but the
    table is somewhat useful in giving a sense of the tradeoff involved)

[loc]: https://en.wikipedia.org/wiki/Locality_of_reference
