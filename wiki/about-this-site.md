---
title: About this site
author: Issa Rice
created: 2014-09-14
date: 2016-11-13
---

*This page is about this site; for information about myself, see [About]().*

# Philosophy

While the general feeling and content on this site has stayed the same since
when I created it in September 2014, my overall thinking of it and goals for it
have changed somewhat.
Originally, this site was intended as a place where I could:

  * place most of my writings regardless of content (biographical information,
    technical content, opinion pieces, etc.) and style (random notes, polished
    articles, etc.)
  * ensure that the content's existence would be for the long-term, so that I
    could add a little bit of information at a time, knowing that the site
    would exist whenever I next wanted to work on the same page
  * canonically establish my [personal identity][cm_personal_web] online.

As of November 2016, now that the site has existed for over two years in its
current form, here are my thoughts on the above points:

  * With the site having been around for a while, I have a good idea of how
    many [pageviews the site gets](analytics-for-this-site) -- it's not very
    many.
    If I want my writings to be read, I need to either ramp up on promoting my
    content or publish in places that have more readership.
    I've mostly opted for the latter, and keep many writings now in an
    [`external`][external] directory in the site's Git repository.
    As a result, this site has become a place for my biographical information
    as well as random notes that don't belong anywhere else.
    This does make this site less useful on its own, but I'm fine with the
    trade-off.
  * The site has survived so far, despite going through several changes in the
    static site generator that is used, the style of Markdown, and the
    organization of pages.
    I still have the full version-controlled history thanks to [Git]().
    Since I am religious about mirroring content I write on external sites to
    the `external` directory, even if a site for which I write goes down, I can
    ensure that at least my own contributions are here for the long-term.
  * I'm mostly happy about having been able to canonically establish my
    personal identity.
    The domain name of this site did change from riceissa.com to the current
    issarice.com, and I've reorganized biographical pages a few times, but
    currently, I have an [About]() page, a page for my online [account
    names](), and so forth.

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

# History

The direct ancestor of this website is riceissa.github.com (which now redirects
to [riceissa.github.io][gh_site] after GitHub reorganized their domains), which
has the same "static site flavor" to it, and which I used until I bought my own
VPS and domain names (see "[Colophon](#colophon)" below for details).

There was also a [riceissa-notes](https://github.com/riceissa/riceissa-notes)
repository that I created that apparently never took off (writing in late 2016,
I don't even remember making it).

This site used to be canonically available at <http://riceissa.com>, but I
think in late 2014 I make <http://issarice.com> the canonical domain.

I think in July 2015 I added the [`_archive`](https://issarice.com/_archive/)
directory to the site, which allows access to *some* past compiled versions of
the site (although the source files are accessible for *every* version thanks
to Git).

In late October 2016, I finally added HTTPS support.

# Colophon

I use Pandoc and a Makefile to produce this site, which is then hosted via Linode.
For details, see [Colophon]().

# Getting updates

I plan to add an Atom feed for this site at some point.
For now, see the [list of pages on this site sorted by date of last substantive
revision][subs] and the [list of all page on this site sorted by date of last
modification][mod].

<!-- I have an [Atom feed](http://issarice.com/atom.xml) for this site. -->
<!-- For more ways to get updates, see [Feed](). -->

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

[cc-by]: https://creativecommons.org/licenses/by/4.0/
[external]: https://github.com/riceissa/issarice.com/tree/master/external
[gh_site]: https://riceissa.github.io/
[gwern]: http://gwern.net
[mod]: _all
[pandoc]: http://johnmacfarlane.net/pandoc/
[rero]: https://en.wikipedia.org/wiki/Release_early,_release_often
[subs]: _all_date
[cm_personal_web]: http://info.cognitomentoring.org/wiki/Creating_your_personal_website
