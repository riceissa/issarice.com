---
title: Digital preservation
author: Issa Rice
created: 2015-01-01
date: 2016-07-09
---

For now, this will be somewhat of a  backup of my [Quora blog on the topic](https://www.quora.com/Issa-Rice/Data-Archiving), which is now not being maintained.
(I'm trying to integrate content from here to more fitting pages.)

Thoughts on storing information in a useful/easily-accessible way. Archiving, backups, single-source publishing, source code management, redundancy (local, cloud), link rot, etc. Essentially, how can we best store thoughts so that later (a day? month? years?) we can easily find them again.

# Requirements for good data archiving solutions


Some ideas for now:

-   Pandoc-flavored markdown
-   LaTeX, then use LaTeX2WP or LaTeX–HTML converters (the benefit of
    this is that printing is covered, as long as your LaTeX skills are
    decent)
-   raw HTML (no)
-   using different formats for different content may be possible, e.g.
    using markdown for most content, but switching to LaTeX for
    math-heavy content.




# Static page generation

-   [Static Site Generators](http://staticsitegenerators.net/) —complete(?) list
-   [Static site generators](http://www.mzlinux.org/?q=node/415)
-   [Jekyll • Simple, blog-aware, static sites](http://jekyllrb.com/)
-   [Hakyll - Home](http://jaspervdj.be/hakyll/)
-   [Switching from Jekyll to Hakyll](http://mark.reid.name/blog/switching-to-hakyll.html)
-   [The Switch to Hakyll](http://www.blaenkdenum.com/posts/the-switch-to-hakyll/)


Best Jekyll doc seems to be the video available from here:
[algonquindesign/jekyll](https://github.com/algonquindesign/jekyll).
Okay, so I've finally figured out how to use jekyll in conjunction with
Github. My test website is up on [Hello world](http://riceissa.github.io/abc/index.html).
See [riceissa/abc](https://github.com/riceissa/abc/tree/gh-pages)
for the source. The trickiest part was modifying all of jekyll's default
internal links (e.g. automatically generated links to blog posts) to use
`{{site.baseurl}}`, so that it worked both locally and
through Github pages.

I'm still trying to figure out how to do math properly through jekyll,
because at the moment I must use two backslashes, since one gets eaten
up by Markdown (pandoc can prevent this, so either switch to hakyll or
use a plugin for jekyll?—does Github even allow plugins for jekyll?)


# More on link rot and the Internet Archive (EDIT: found the speech!!)

Ones with a star (\*) are more useful.

-   [Why URL shorteners suck](http://boingboing.net/2009/04/04/why-url-shorteners-s.html)
-   [URL shorteners suck less, thanks to the Internet Archive and 301Works](http://boingboing.net/2009/11/13/url-shorteners-suck.html)
-   [URLTeam - Archiveteam](https://web.archive.org/web/20131105102512/http://archiveteam.org/index.php?title=TinyURL)
-   [URLTE.AM](http://urlte.am/)
-   [Learn From History: Why The Internet Archive Is So Important](http://flippa.com/blog/learn-from-history-why-the-internet-archive-is-so-important/)
-   [Brewster's trillions: Internet Archive strives to keep web history alive](http://www.theguardian.com/technology/2013/apr/26/brewster-kahle-internet-archive)
-   [on url shorteners](https://web.archive.org/web/20131016131625/http://joshua.schachter.org/2009/04/on-url-shorteners.html)
-   [301works-faq : Free Download & Streaming : Internet Archive](https://archive.org/details/301works-faq)


I'm still trying to find that speech about link rot and URL shorteners.

EDIT: I found the speech: [The Splendiferous Story of Archive Team](http://ascii.textfiles.com/archives/3029).
The guy's name is [Jason Scott Sadofsky](https://en.wikipedia.org/wiki/Jason_Scott_Sadofsky) and
he seems to have a lot of stuff e.g. [T E X T F I L E S](http://textfiles.com/jason/). He actually seems to be part
of the [Archiveteam](http://archiveteam.org/index.php?title=Main_Page),
which makes him even cooler. (How did I find the speech again after two
days of trying? [So that I can get better at finding old things.]
Through this article: [This Group Is Saving The Web From Itself (And Rescuing Your Stuff)](http://www.huffingtonpost.com/2013/03/27/jason-scott-archive-team_n_2965368.html),
where I got his name. My search terms on Google to find that article
were "saving the internet archive"; after I recognized the name, I just
Googled "jason scott", and found his Wikipedia page and website, whose
design I remembered from when I read the speech before.)

The relevant bit on URL shorteners is:


> URL shorteners may be one of the worst ideas, one of the most backward
> ideas, to come out of the last five years. In very recent times,
> per-site shorteners, where a website registers a smaller version of
> its hostname and provides a single small link for a more complicated
> piece of content within it.. those are fine. But these general-purpose
> URL shorteners, with their shady or fragile setups and utter
> dependence upon them, well. If we lose TinyURL or
> [bit.ly](http://bit.ly), millions of weblogs,
> essays, and non-archived tweets lose their meaning. Instantly.


# Terminally Incoherent

from Luke.

-   [Personal Backups](http://www.terminally-incoherent.com/blog/2012/06/04/personal-backups/)
-   [Putting your Vim files under version control](http://www.terminally-incoherent.com/blog/2012/03/12/putting-your-vim-files-under-version-control/)
-   [You Need Backups](http://www.terminally-incoherent.com/blog/2013/10/02/you-need-backups/)
-   [Backing up your work: Common Sense 101](http://www.terminally-incoherent.com/blog/2010/09/06/backing-up-your-work-common-sense-101/)
-   [Maybe the Backup Problem Will Resolve Itself In Time](http://www.terminally-incoherent.com/blog/2008/11/11/maybe-the-backup-problem-will-resolve-itself-in-time/)
-   [Backup is not just for geeks](http://www.terminally-incoherent.com/blog/2007/10/24/backup-is-not-just-for-geeks/)


The message is clear.

Also example of backing up dotfiles: [maciakl/.dotfiles](https://github.com/maciakl/.dotfiles).
Somewhere I remember reading a post about how to set this up nicely (by
Luke), but can't seem to locate it at the moment.


# Gwern on archiving

[Archiving URLs](http://www.gwern.net/Archiving%20URLs) see also
<http://www.gwern.net/About#long-content>. I can't
believe I had forgotten about this! Okay and linked on the first page is
this: <http://www.gwern.net/docs/2011-muflax-backup.pdf>
(from muflax).


# URL shortening

where is the speech that
someone at [Digital Library of Free Books, Movies, Music & Wayback Machine](http://archive.org) made about how URL
shortening sites cause a lot of link rot?

EDIT: Okay I found this at least:
<http://www.archiveteam.org/index.php?title=URLTeam>
and this links to [Why URL shorteners are bad](http://web.archive.org/web/20131025182943/http://rield.com/faq/why-url-shorteners-are-bad).
Not bad.

EDIT2: Okay finally found it. See [More on link rot and the Internet Archive (EDIT: found the speech!!)](http://www.quora.com/Issa-Rice/Data-Archiving/More-on-link-rot-and-the-Internet-Archive-EDIT-found-the-speech).


# What do people do about archiving information that they don't own?

e.g. a journal article that
you didn't write. This sort of thing could be very useful for people to
have access to. Storing them locally wouldn't be a problem, and putting
them up online shouldn't cause too much trouble either. Websites like
<http://archive.org> always just archive
whatever they can find anyway.

Actually, how does [Digital Library of Free Books, Movies, Music & Wayback Machine](http://archive.org) deal with
copyright issues?


# Git/GitHub

See [What are some unconventional and unique uses of Git?](http://www.quora.com/What-are-some-unconventional-and-unique-uses-of-Git)
and also the article linked in the description of the question (<http://www.wired.com/wiredenterprise/2012/02/github-revisited/>).

Git in particular is excellent in terms of having a local mirror as well
as one online (e.g. by using Github/Bitbucket), along with all of the
changes that have been made. This makes the data redundant/safe. It
doesn't seem to be bad either in terms of sharing, since everything will
be in plaintext. Posting on Quora might be a problem though, since it
doesn't use Markdown or the like.

I suppose the other big problem with using source-control is the
question of storing binary data. Use a different place to store those?
(e.g. putting all plaintext on Github but uploading photos to Wordpress,
and linking them?) Deal with binaries in git as well, and make many
small projects so that it doesn't slow down git?


# Random questions (not Quora-quality yet)

Some of these have
probably already been asked, so.

-   Is single-sourcing worth one's time for most things?
    For some things?
-   How important is grammar/capitalization for recording most thoughts?
    (cf AKC's post [on wordpress?] about grammar not being important)
-   Is Evernote reliable?
-   How do I easily create multiple mirrors of my data, both locally and online?
-   How do I reliable backup online data?
-   How do I keep a revision list of online data?—version control it somehow?
    how?
-   Why is Quora's search feature unreliable at finding the information I want?
    e.g. it can't find comments.
-   Why does Quora make everything so hard to find?
    —e.g. there are no chronological lists of all posts of a user, no place to find all the posts I've upvoted, and so on.
-   How do I make sharing easier between Quora and other sites?


# External mirroring

The way I see it, external page savers like the Internet Archive and WebCite shouldn't be trusted; rather, they're a convenient way to avoid copyright violations (since they're hosting the files, not you); and they provide a time buffer for you to get local copies.

I don't think I should be surprised at all by this, but I was quite impressed with [Perma.cc](http://perma.cc)'s [contingency plan](https://perma.cc/contingency-plan), which seems like an obvious improvement over standard web services that simply shut down and give no notice[^quora].

# Archive buttons

On Firefox, I have the following archive buttons:

![](archive-buttons.png)

From left to right, these are [Pinboard](https://pinboard.in/), Zotero,
archive.is, and Archive.org. The Archive.org button is a bookmarklet with the
code:

```
javascript:void(window.open('https://web.archive.org/save/'+location.href))
```

I also have the Scrapbook plugin for Firefox.
This allows me to quickly create copies that are local (Scrapbook and Zotero), private network (Pinboard), and public network (Archive.org).

[^quora]: In the case of Quora, private blogs were almost immediately disabled and deleted after announcement (though archives were emailed out to owners); Google reader gave [under three months](https://en.wikipedia.org/wiki/Google_Reader#Discontinuation) to backup data.
