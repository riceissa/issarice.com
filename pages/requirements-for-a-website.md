---
title: Requirements for a website
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

What makes a good website, especially one that lasts a long time?
gwern has some ideas, namely his twin ideas of [Long Site](http://www.gwern.net/About#long-site) and [Long Content]().
gwern quotes Julian Assange, but it is worth doing so here as well[^assange]:

[^assange]: From "[Self destructing paper](http://web.archive.org/web/20071020051936/http://iq.org/#Selfdestructingpaper)".
2006-12-05.


> The internet is self destructing
> paper. A place where anything written is soon destroyed by rapacious
> competition and the only preservation is to forever copy writing from
> sheet to sheet faster than they can burn.
> 
> If it's worth writing, it's worth keeping. If it can be kept, it might
> be worth writing. Would your store your brain in a startup company's
> vat? If you store your writing on a 3rd party site like blogger,
> livejournal or even on your own site, but in the complex format used by
> blog/wiki software de jour you will *lose it forever* as soon as
> hypersonic wings of internet labor flows direct people's energies
> elsewhere. For most information published on the internet, perhaps that
> is *not a moment to soon*, but how can the muse of originality soar when
> immolating transience brushes every feather?
> 
> Readers have asked what software is used to run IQ.ORG. A mere page of
> handwritten ruby constructs the site out the most robust future proof
> storage form imaginable. A flat directory of text or html files. The
> directory, like any directory can be backed up, edited, emailed, zipped,
> transported, printed, trapped in amber etc.

Regarding his publishing system, he writes, "it's gold until civilization collapses, the neoluddites take control, or both, but then we will have other adventures to please us..."



-   compatibility with git
-   ability to use math (LaTeX, mathjax, images if desperate)
-   some option for single-source publishing? (to PDF [to print] and
    HTML would be nice)
-   *not* WYSIWYG (because let's be honest, WYSIWYG isn't very good in
    terms of producing precise content)\
-   but must have mostly readable syntax (LaTeX is fine, since I'm so
    used to it, but HTML is ugly); Markdown-type syntax is great
-   content must stay on a local drive, and be "pushed" to a possibly
    off-site place for hosting (like Github)
-   ability to merge different sources; e.g. one person writes an
    article, another works on it by adding a few things; but if the
    first person does not want the changes of the second person, yet the
    second person wants changes from the first person, then the second
    must be able to keep pulling changes from the first. <span
    id="qlink_k0">[How does Git merge
    work?](http://www.quora.com/How-does-Git-merge-work)</span> may be
    useful.\
