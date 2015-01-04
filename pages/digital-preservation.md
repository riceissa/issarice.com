---
title: Digital preservation
#description: none
author: Issa Rice
creation-date: 2015-01-01
last-major-revision-date: 2015-01-01
language: English
# accepts "notes", "draft", "in progress", or "mostly finished"
#status: notes
# accepts "certain", "highly likely", "likely", "possible", "unlikely", "highly unlikely", "remote", "impossible", "log", "emotional", or "fiction"
#belief: 
# accepts "CC0", "CC-BY", or "CC-BY-SA"
license: CC-BY
tags: untagged
...

For now, this will be somewhat of a  backup of my [Quora blog on the topic](https://www.quora.com/Issa-Rice/Data-Archiving), which is now not being maintained.
(I'm trying to integrate content from here to more fitting pages.)

Thoughts on storing information in a useful/easily-accessible way. Archiving, backups, single-source publishing, source code management, redundancy (local, cloud), link rot, etc. Essentially, how can we best store thoughts so that later (a day? month? years?) we can easily find them again.

# Requirements for good data archiving solutions


Some ideas for now:\

-   Pandoc-flavored markdown
-   LaTeX, then use LaTeX2WP or LaTeX–HTML converters (the benefit of
    this is that printing is covered, as long as your LaTeX skills are
    decent)
-   raw HTML (no)
-   using different formats for different content may be possible, e.g.
    using markdown for most content, but switching to LaTeX for
    math-heavy content.

\


# Static page generation


<span id="__w2_q0XsWSm_toggle_link"
href="https://www.quora.com/Issa-Rice/Data-Archiving/Static-page-generation#"><span
id="ld_lfpnuo_10164"><span id="ld_lfpnuo_10165"></span></span></span>

-   <span id="qlink_k0">[Static Site
    Generators](http://staticsitegenerators.net/)</span> —complete(?)
    list
-   <span id="qlink_k1">[Static site
    generators](http://www.mzlinux.org/?q=node/415)</span>
-   <span id="qlink_k2">[Jekyll • Simple, blog-aware, static
    sites](http://jekyllrb.com/)</span>\
-   <span id="qlink_k3">[Hakyll -
    Home](http://jaspervdj.be/hakyll/)</span>
-   <span id="qlink_k4">[Switching from Jekyll to
    Hakyll](http://mark.reid.name/blog/switching-to-hakyll.html)</span>\
-   <span id="qlink_k5">[The Switch to
    Hakyll](http://www.blaenkdenum.com/posts/the-switch-to-hakyll/)</span>

\
Best Jekyll doc seems to be the video available from here: <span
id="qlink_k6">[algonquindesign/jekyll](https://github.com/algonquindesign/jekyll)</span>.
Okay, so I've finally figured out how to use jekyll in conjunction with
Github. My test website is up on <span id="qlink_k7">[Hello
world](http://riceissa.github.io/abc/index.html)</span>. See <span
id="qlink_k8">[riceissa/abc](https://github.com/riceissa/abc/tree/gh-pages)</span>
for the source. The trickiest part was modifying all of jekyll's default
internal links (e.g. automatically generated links to blog posts) to use
[code]{{site.baseurl}}[/code], so that it worked both locally and
through Github pages.\
\
I'm still trying to figure out how to do math properly through jekyll,
because at the moment I must use two backslashes, since one gets eaten
up by Markdown (pandoc can prevent this, so either switch to hakyll or
use a plugin for jekyll?—does Github even allow plugins for jekyll?)\


# More on link rot and the Internet Archive (EDIT: found the speech!!)


<span id="__w2_IqfkMEw_toggle_link"
href="https://www.quora.com/Issa-Rice/Data-Archiving#"><span
id="ld_kuwnal_1295"><span id="ld_kuwnal_1296">Ones with a star (\*) are
more useful.\
</span></span></span>

-   <span id="qlink_k0">[Why URL shorteners suck \*\
    ](http://boingboing.net/2009/04/04/why-url-shorteners-s.html)</span>
-   <span id="qlink_k1">[URL shorteners suck less, thanks to the
    Internet Archive and
    301Works](http://boingboing.net/2009/11/13/url-shorteners-suck.html)</span>
-   <span id="qlink_k2">[URLTeam -
    Archiveteam](https://web.archive.org/web/20131105102512/http://archiveteam.org/index.php?title=TinyURL)</span>
-   <span id="qlink_k3">[URLTE.AM](http://urlte.am/)</span>\
-   <span id="qlink_k4">[Learn From History: Why The Internet Archive Is
    So
    Important](http://flippa.com/blog/learn-from-history-why-the-internet-archive-is-so-important/)</span>
-   <span id="qlink_k5">[Brewster's trillions: Internet Archive strives
    to keep web history
    alive](http://www.theguardian.com/technology/2013/apr/26/brewster-kahle-internet-archive)</span>
-   <span id="qlink_k6">[on url
    shorteners](https://web.archive.org/web/20131016131625/http://joshua.schachter.org/2009/04/on-url-shorteners.html)</span> \*
-   <span id="qlink_k7">[301works-faq : Free Download & Streaming :
    Internet Archive](https://archive.org/details/301works-faq)</span>

\
I'm still trying to find that speech about link rot and URL shorteners.\
\
EDIT: I found the speech: <span id="qlink_k8">[The Splendiferous Story
of Archive Team](http://ascii.textfiles.com/archives/3029)</span>. The
guy's name is <span id="qlink_k9">[Jason Scott
Sadofsky](https://en.wikipedia.org/wiki/Jason_Scott_Sadofsky)</span> and
he seems to have a lot of stuff e.g. <span id="qlink_k10">[T E X T F I L
E S](http://textfiles.com/jason/)</span>. He actually seems to be part
of the <span
id="qlink_k11">[Archiveteam](http://archiveteam.org/index.php?title=Main_Page)</span>,
which makes him even cooler. (How did I find the speech again after two
days of trying? [So that I can get better at finding old things.]
Through this article: <span id="qlink_k12">[This Group Is Saving The Web
From Itself (And Rescuing Your
Stuff)](http://www.huffingtonpost.com/2013/03/27/jason-scott-archive-team_n_2965368.html)</span>,
where I got his name. My search terms on Google to find that article
were "saving the internet archive"; after I recognized the name, I just
Googled "jason scott", and found his Wikipedia page and website, whose
design I remembered from when I read the speech before.)\
\
The relevant bit on URL shorteners is:\
\

> URL shorteners may be one of the worst ideas, one of the most backward
> ideas, to come out of the last five years. In very recent times,
> per-site shorteners, where a website registers a smaller version of
> its hostname and provides a single small link for a more complicated
> piece of content within it.. those are fine. But these general-purpose
> URL shorteners, with their shady or fragile setups and utter
> dependence upon them, well. If we lose TinyURL or <span
> id="qlink_k13">[bit.ly](http://bit.ly)</span>, millions of weblogs,
> essays, and non-archived tweets lose their meaning. Instantly.

\


# Terminally Incoherent


<span id="__w2_WzHAwWE_toggle_link"
href="https://www.quora.com/Issa-Rice/Data-Archiving#"><span
id="ld_kuwnal_1305"><span id="ld_kuwnal_1306">from Luke.\
\
</span></span></span>

-   <span id="qlink_k0">[Personal
    Backups](http://www.terminally-incoherent.com/blog/2012/06/04/personal-backups/)</span>
-   <span id="qlink_k1">[Putting your Vim files under version
    control](http://www.terminally-incoherent.com/blog/2012/03/12/putting-your-vim-files-under-version-control/)</span>
-   <span id="qlink_k2">[You Need
    Backups](http://www.terminally-incoherent.com/blog/2013/10/02/you-need-backups/)</span>
-   <span id="qlink_k3">[Backing up your work: Common Sense
    101](http://www.terminally-incoherent.com/blog/2010/09/06/backing-up-your-work-common-sense-101/)</span>
-   <span id="qlink_k4">[Maybe the Backup Problem Will Resolve Itself In
    Time](http://www.terminally-incoherent.com/blog/2008/11/11/maybe-the-backup-problem-will-resolve-itself-in-time/)</span>
-   <span id="qlink_k5">[Backup is not just for
    geeks](http://www.terminally-incoherent.com/blog/2007/10/24/backup-is-not-just-for-geeks/)</span>

\
The message is clear.\
\
Also example of backing up dotfiles: <span
id="qlink_k6">[maciakl/.dotfiles](https://github.com/maciakl/.dotfiles)</span>.
Somewhere I remember reading a post about how to set this up nicely (by
Luke), but can't seem to locate it at the moment.\


# Gwern on archiving


<span id="__w2_dHBNQJA_toggle_link"
href="https://www.quora.com/Issa-Rice/Data-Archiving#"><span
id="ld_xdwftr_136"><span id="ld_xdwftr_137"><span
id="qlink_k0">[Archiving
URLs](http://www.gwern.net/Archiving%20URLs)</span> see also <span
id="qlink_k1"><http://www.gwern.net/About#long-content></span>. I can't
believe I had forgotten about this! Okay and linked on the first page is
this: <span
id="qlink_k2"><http://www.gwern.net/docs/2011-muflax-backup.pdf></span>
(from muflax).\
</span></span></span>


# URL shortening


<span id="__w2_sUYvISi_toggle_link"
href="https://www.quora.com/Issa-Rice/Data-Archiving#"><span
id="ld_xdwftr_130"><span id="ld_xdwftr_131">where is the speech that
someone at <span id="qlink_k0">[Digital Library of Free Books, Movies,
Music & Wayback Machine](http://archive.org)</span> made about how URL
shortening sites cause a lot of link rot?\
\
EDIT: Okay I found this at least: <span
id="qlink_k1"><http://www.archiveteam.org/index.php?title=URLTeam></span>
and this links to <span id="qlink_k2">[Why URL shorteners are
bad](http://web.archive.org/web/20131025182943/http://rield.com/faq/why-url-shorteners-are-bad)</span>.
Not bad.\
\
EDIT2: Okay finally found it. See <span id="qlink_k3">[More on link rot
and the Internet Archive (EDIT: found the
speech!!)](http://www.quora.com/Issa-Rice/Data-Archiving/More-on-link-rot-and-the-Internet-Archive-EDIT-found-the-speech)</span>.\
</span></span></span>


# What do people do about archiving information that they don't own?


<span id="__w2_eFBuOOv_toggle_link"
href="https://www.quora.com/Issa-Rice/Data-Archiving#"><span
id="ld_xdwftr_122"><span id="ld_xdwftr_123">e.g. a journal article that
you didn't write. This sort of thing could be very useful for people to
have access to. Storing them locally wouldn't be a problem, and putting
them up online shouldn't cause too much trouble either. Websites like
<span id="qlink_k0"><http://archive.org></span> always just archive
whatever they can find anyway.\
\
Actually, how does <span id="qlink_k1">[Digital Library of Free Books,
Movies, Music & Wayback Machine](http://archive.org)</span> deal with
copyright issues?\
</span></span></span>


# Git/GitHub


<span id="__w2_dTDF8Xu_toggle_link"
href="https://www.quora.com/Issa-Rice/Data-Archiving#"><span
id="ld_fshlva_1100"><span id="ld_fshlva_1101">See <span
id="qlink_k0">[What are some unconventional and unique uses of
Git?](http://www.quora.com/What-are-some-unconventional-and-unique-uses-of-Git)</span>
and also the article linked in the description of the question ( <span
id="qlink_k1"><http://www.wired.com/wiredenterprise/2012/02/github-revisited/></span>
).\
\
Git in particular is excellent in terms of having a local mirror as well
as one online (e.g. by using Github/Bitbucket), along with all of the
changes that have been made. This makes the data redundant/safe. It
doesn't seem to be bad either in terms of sharing, since everything will
be in plaintext. Posting on Quora might be a problem though, since it
doesn't use Markdown or the like.\
\
I suppose the other big problem with using source-control is the
question of storing binary data. Use a different place to store those?
(e.g. putting all plaintext on Github but uploading photos to Wordpress,
and linking them?) Deal with binaries in git as well, and make many
small projects so that it doesn't slow down git?\
</span></span></span>


# Random questions (not Quora-quality yet)


<span id="__w2_KuS5ZIK_toggle_link"
href="https://www.quora.com/Issa-Rice/Data-Archiving#"><span
id="ld_fshlva_1104"><span id="ld_fshlva_1105">Some of these have
probably already been asked, so.\
\
</span></span></span>

-   Is single-sourcing worth one's time for most things? For some
    things?
-   How important is grammar/capitalization for recording most thoughts?
    (cf AKC's post [on wordpress?] about grammar not being important)
-   Is Evernote reliable?
-   How do I easily create multiple mirrors of my data, both locally and
    online?
-   How do I reliable backup online data?
-   How do I keep a revision list of online data?—version control it
    somehow? how?\
-   Why is Quora's search feature unreliable at finding the information
    I want? e.g. it can't find comments.\
-   Why does Quora make everything so hard to find? —e.g. there are no
    chronological lists of all posts of a user, no place to find all the
    posts I've upvoted, and so on.
-   How do I make sharing easier between Quora and other sites?

\


# External mirroring

The way I see it, external page savers like the Internet Archive and WebCite shouldn't be trusted; rather, they're a convenient way to avoid copyright violations (since they're hosting the files, not you); and they provide a time buffer for you to get local copies.
