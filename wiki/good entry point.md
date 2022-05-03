---
title: Good entry point
author: Issa Rice
created: 2015-01-02
date: 2015-08-04
status: notes
---

A **good entry point** to a website or wiki is a page that is understandable and useful to someone coming from outside the site (e.g. from a search engine or external website).
In other words, a good entry point does not depend on content that is on other pages on the website for comprehension.

I am taking the idea of a good entry point from the [WikiWikiWeb](http://c2.com/cgi/wiki?FrontPage) [page on "Good Entry Point"](http://c2.com/cgi/wiki?GoodEntryPoint):


> [WardsWiki](http://c2.com/cgi/wiki?WardsWiki) consists of many thousands
> of pages, each almost equally important. Even the
> [FrontPage](http://c2.com/cgi/wiki?FrontPage) isn't *that* special. As a
> result people stumble into this site at some random point, presumably
> something relevant to a Web search. These visitors don't initially have
> the context provided by the page's neighbors.
>
> Turning this on its head, it becomes a problem for those wishing to
> create a [ValuablePage](http://c2.com/cgi/wiki?ValuablePage) for a broad
> section of the reading population.
>
> The often-quoted [WardCunningham](http://c2.com/cgi/wiki?WardCunningham)
> said on
> [WikiIsNotaDictionary](http://c2.com/cgi/wiki?WikiIsNotaDictionary),
>
> > [...] Ask yourself: if the page you cite were to be created, would
> > it serve Wiki well as a point of entry in this web of knowledge?


In "[The goal of subject wikis](http://blog.subwiki.org/2009/02/02/the-goal-of-subject-wikis/)", Vipul Naik writes:

> A principle that
> is important and not obvious is *genericity*: individual subject
> wiki pages should largely make sense as independent entry points
> into the wiki, so that people coming from outside can go straight
> there. While they should link to other subject wiki entries, they
> should not be dependent on them in a strong sense.  Most
> important, there should be no *forced sequencing* of the entries
> as in a textbook, where future entries depend on earlier ones.


The above sources speak mostly to the importance of having good entry points.
Below, we consider the advantages and disadvantages of trying to make many pages on the site good entry points.

# Advantages

- Doesn't waste time for the reader, who can just get the information they want without going through many other pages
- No forced sequencing
- Leads to higher quality pages, since one must put more effort into making them comprehensible (?)
- Easier exporting of the site.
In other words, in the future I might want to split up the site by e.g. subject[^split], and having roughly independent pages means I don't have to worry about dependency issues.
- Since a lot of web traffic now comes from social media, it's important to make pages "share-friendly", i.e. be useful to people coming in from e.g. Facebook shares, even if they're not familiar with your site.
(This is essentially the same point as in the case of search traffic.
In both cases, you should just assume that most people aren't familiar with your site.^[Though some sites use this "foreignness" well, as in the case of e.g. everything2 or AutoAdmit, which have a different "feel" to the site than most sites, which (for me) makes them more interesting.])

[^split]: This might be the case if my website begins to accumulate *a lot* of content.
Right now, even fairly large personal websites (like, say, gwern's) can be processed easily with Hakyll and uploaded as a static site.
On the other hand, Subwiki uses separate MediaWiki instances for its distinct subjects.
One problem is that Git may not be able to handle very large sites, though one could still "chop off" the history after a certain point and begin anew.
I don't imagine this site will ever grow to become something like the size of Wikipedia, so this concern should be rather small, but I do want to make this site *very future-oriented*, since I do want it to last for a *long* time.

# Disadvantages

- Inability to have "sequences" of pages?
- Duplication of content, like introductions?

# On this site

I have tried to make pages good entry points on here.
One specific "technique" here is that I try to add meta-notes in italics at the top for navigation, e.g. see my [[About]] page:

> *This page is about myself (Issa Rice); for information about this
> website, see [[About this site]].*

Another technique: the first paragraph of a page is usually a Wikipedia-style introduction, with bolded keyword and general introduction to the topic.
This allows readers to quickly tell if the page they're reading is something they want to be reading (sort of like how abstracts function in academic papers).

I also try to avoid [[jargon]].
