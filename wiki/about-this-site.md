---
title: About this site
description: site info, tools used to build the site
tags: site-info, general
created: 2014-09-14
date: 2015-01-14
license: CC0
aliases: about-this-site, site
---

*This page is about this site; for information about myself, see [About]().*

# Philosophy

This site is my attempt to realize [gwern]’s idea of [Long
Content]()---i.e. the goal is to incrementally update the pages so as to
produce useful, lasting content.[^cy] It is also an [open notebook](http://wcm1.web.rice.edu/open-notebook-history.html) of sorts. In particular, I strive to make
all the source files used to produce this site human-readable (by
writing pages in [Pandoc] markdown and storing them in [plain text](http://wcm1.web.rice.edu/my-academic-book-in-plain-text.html)), version-controlled (with [git](!w Git_\(software\))), and
freely-licensed (all pages are *at least* [CC-BY], with some in the public
domain[^copy]; the [software used to make this site](colophon) is all
free software).  I also like to [release early, release often][rero][^agile]; I
actually don't deploy the site as often, but I try to commit to the git
repository often---so my site is the result of many incremental updates[^aaron].

[^agile]: See also [Random Ideas and Suggestions | Essays on Reducing Suffering: Agile Projects](http://reducing-suffering.org/random-ideas-and-suggestions/#Agile_projects).

[^aaron]: I realize that [Aaron Swartz](http://www.aaronsw.com/weblog/archive) likes to "[Release Late, Release Rarely](http://www.aaronsw.com/weblog/rlrr)" to the public:

    > When you look at something you’re working on, no matter what it
    > is, you can’t help but see past the actual thing to the ideas that
    > inspired it, your plans for extending it, the emotions you’ve tied
    > to it. But when others look at it, all they see is a piece of
    > junk.
    >
    > You only get one chance to make a first impression; why have it be
    > “junk”? Once that’s associated with your name or project, it’s
    > tough to scrape off. Even people who didn’t see it themselves may
    > have heard about it second-hand. And once they hear about it,
    > they’re not likely to see for themselves. Life’s too short to
    > waste it on junk.

    While I think there's merit in what Swartz says, here are a few things I'll say to counter it:

    - I use [belief]() and [status]() tags to explicitly signal how "complete" or "ready" I think my pages are for the public.
    - I only deploy the site about once per month, so a lot of the most "rough" edits tend to be fixed during the time between deployments (so most of the public won't see them anyway---and if they ever want to see those "rough" edits, they can always dig around in the [Git repository](https://github.com/riceissa/issarice.com)).


[gwern]: http://gwern.net
[cc-by]: https://creativecommons.org/licenses/by/4.0/
[pandoc]: http://johnmacfarlane.net/pandoc/
[rero]: https://en.wikipedia.org/wiki/Release_early,_release_often

[^cy]: Of course, more cynically, [one could quote Scott Alexander](https://web.archive.org/web/20130118212124/http://raikoth.net/) about the reason many people have personal websites:

    > You know how if you're under the age of thirty you have to have a
    > personal webpage with your name, your photo, your resume, and then
    > a link to your blog or something like that?
    >
    > Well, this is mine. Plus a little extra.

    In this case, this site would just be my attempt to "be cool",
    instead of serving useful content.

[^copy]: So content will be copied, making the data safe; "lots of copies keep stuff safe", etc.

Inspired by [Vipul Naik](http://vipulnaik.com), I am also experimenting with the [tree structure](./using-a-tree-structure-for-websites) of this site. In particular, I think many of gwern's pages are too long, so I like to siphon off content to new pages once a section on a page matures enough, etc.


# Colophon

I use Pandoc and a Makefile to produce this site, which is then hosted via Linode.
For details, see [Colophon]().

<!--
# Getting updates

I have an [Atom feed](http://issarice.com/atom.xml) for this site.
For more ways to get updates, see [Feed]().-->

# Belief and status tags

I use [status]() and [belief]() markers on this site, both of which
are ideas I got from gwern's site. These are both meant to tell the
reader how the author regards the content on a page. I find that it's
mostly useful in cases where I want to say "I've only briefly thought
about this topic, and haven't really spent much effort working on this
page, so even though I think it's worth making public, you shouldn't
take this page very seriously, nor should you think that I believe the
things I'm writing"---but don't want to keep repeating that all the time
(so I just tag these pages with "*Status: notes; belief: possible*" or
something).
