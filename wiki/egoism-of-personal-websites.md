---
title: Egoism of personal websites
#description: 
#feed_description: 
author: Issa Rice
creation_date: 2015-10-20
last_major_revision_date: 2015-10-20
language: English
# Possible values are "notes", "draft", "in progress", and
# "mostly finished"
status: notes
# Possible values are "certain", "highly likely", "likely", "possible",
# "unlikely", "highly unlikely", "remote", "impossible", "fiction", and
# "emotional"
#belief: possible
# accepts "CC0", "CC-BY", or "CC-BY-SA"
license: CC0
tags: untagged
#aliases: 
---

In content creation, one important decision to make is the venue.
This follows from the observation that given identical written content, it can make a big difference where that content is hosted.

While content creation can provide [value for the creator](http://issarice.com/the-value-of-content-creation#value-for-the-creator), this is unlikely to be as big of a consideration.
Even if value for the creator is foremost, we can still try to achieve both kinds of value (to the creator, to the world) [separately](http://lesswrong.com/lw/6z/purchase_fuzzies_and_utilons_separately/).
If the biggest factor for one in creating online content is that useful information is processed by the greatest number of people, how much content should one's personal site have?
In other words, given the choice of where to publish among places like one's personal site, Quora, Wikipedia, reddit, and so on, how should one decide where to publish a particular piece of written content? 

In general one should publish content in the canonical location.

Some factors to consider are:

Durability of location
:   Sure, it is possible to backup content even if external sites go down, but what of the people who actually read your content?
It would be a nuisance to have links suddenly disappear, and search results take time to update (and who knows if you'll be at the top now). 

Locatability
:   I think it's probably easier to locate content *by person* than *what they said*.

> This is partly because of my style of contribution. I’ve always
> preferred to work on existing applications and libraries than to go
> write my own. I’ve always preferred to take someone else’s work and
> bring it up to snuff than write a clean implementation of my own. I’ve
> always preferred prodding the author or maintainer to do the right
> thing than to drop a large batch of patches onto them.
>
> [...]
> 
> It is much better to find some people who have tried in the past to
> solve a problem and bring them together to solve it, than to solve it
> yourself - even if it means being a footnote (or less) in the
> announcement. What’s important is that it got done, and people will be
> using it. Not the credit. It is a high accomplishment indeed to factor
> out a bit of functionality into a library and make every possible user
> actually use it. Would that more Haskellers had this mindset! Indeed,
> would that more people in general had this mindset; as it is, people
> have bad habits of repeatedly failing when they think they have
> special information, are highly overconfident even in objective areas
> with quick feedback, and badly overestimate how many good ideas they
> can come up with - indeed, most good ideas are Not Invented Here. One
> should be able to draw upon the wisdom of others.

<http://www.gwern.net/Links#collaboration-style>

Why are blogs still such a useful source of info?

Why am I downloading Quora answers only from the same users?

Because in the end (regrettably) the best info still comes from very few of the same people. There is an egoism involved here that I dislike

also another thing: im really trying to “dismantle” my website in the sense that i’d rather not host the things on there under the domain issarice.com, b/c that’s too egoistic. im glad i ported my critiques list to the EA wiki.

reconciling:

- value making snapshots of my thought available
- it’s a bit of an egoistic thing to be doing (why is writing about yourself more important than writing about something that is more useful to others?)
- will anyone read it?
- creating a "resume" of sorts. it might still be nice to link to *everything* you've done.

 publishing something to your personal webstie–and egoistic place in the first place–is a META statement as well, that you think what you write is worth ppls time


contributing to content-relevant sites. so e.g my reddit user guide.
sure, i could have published it on my site (and i still could, since
it’s public domain), but the *content* is most relevant to CM. i could
also just do all my CP research on my personal site. maybe gwern would do this (it would be like his SRS review that is on his site). but no, the
*content-relevant* location would be on a site that addresses CP
directly, i.e. cp wiki.

in general… if you do it right, then you personal site should end up with:

-   personal information (e.g. contact info,
    bio, links to ALL YOUR OTHER CONTENT (even if external))
-   scraps/drafts (that would end up elsewhere when more polished/when
    the time is right)
-   stuff that is so random that there isn’t really any place that it
    belongs to OR the places where it does belong are so unreliable that
    you have no choice but to put it on your site (this is one reason i
    keep answers from quora on my site). i mean, also, i did make sure to
    backup my reddit article on github gist too. maybe my site would be
    better (theoretically, since my site only compiles md files, i
    *could* just put it with a different extension and then it
    wouldn’t compile)

… hmm actually, a personal site might be a
great place to just store stuff so it doesn’t get lost. it’s more for
*you* than for others. like, a backup place. but in general the
content that is to be viewed by *others* should be placed in more
content-relevant places. but also what linus torvalds says about letting other people keep backups for you.

<http://info.cognitomentoring.org/wiki/Creating_your_personal_website#Website_as_personal_identity>

another idea is to put everything online (even notes are more useful in public than on just your harddrive, and even things that don't belong on external sites can be useful to have on one's personal site), but in a separate location on your website, e.g. in a different directory from all your written content/bio data.

the attitude i want to adopt is something more like what [why the lucky stiff](https://en.wikipedia.org/wiki/Why_the_lucky_stiff) said in [his final appearance](https://archive.org/stream/136875051WhySCompletePrinterSpoolAsOneBook/136875051--why-s-complete-printer-spool-as-one-book_djvu.txt):

> Now I want to make it perfectly clear that these papers and all my
> other works in life belong to the general public. In fact, I also
> would like to turn myself over to all of you as well. This was
> actually done several years ago, but in an embarrassingly disorganized
> manner. I like what you've done with the character, but I'd like to
> step into his tattered suit for the next hundred pages and a day. And
> after that, I'm yours again. Do what you must do! I always enjoy
> seeing what happens to me.

several dangers of adding content to a place you don't control:

- it could be removed ("ruthlessly edited")
- licensing issues; in particular, the site may have a more restrictive license than what i like (CC0) -- in this case, self-hosting a CC0 copy is desirable.
- it makes sense to write in a format from which it is easy to escape. I think pandoc markdown is one of the best, because it is both plaintext and benefits from the ability to convert to many different formats (e.g. mediawiki, LaTeX, HTML) so that if one needs to continue work in another format this is possible without too much hassle.
There is a bit of difficulty with complicated structure when dealing with e.g. math.
For complicated mathematical texts, it's useful to define macros, which is difficult to do if one wants to write for the web (MathJax is by far the best way to display formulas, but there is no way to define macros).
In addition in math it's useful to have different environments for e.g. "theorem", "corollary", "proof", and so on, but there is no way for pandoc to detect these.
The lesson might just be that it's impossible for the moment to "single source publish", so that one must be prepared to spend some time converting between formats as the need arises (this is still better than what was once required---e.g. manually typesetting text, or copying entire books by hand!).

In general I prefer openness, and an attitude of having "nothing to hide" rather than a standard of secrecy about one's thoughts.

There are some content that can be justified being sorted chronologically (as in a blog), though I think there should be a presumption in favor of topic-centric organization.
Likewise I think it can be justified to collect content by author of the piece (as in a personal site or CV), though again by the presumption in favor of topic-centric organization of content, it would be more useful *in a larger number of cases* to have topic-specific sites instead.

What are some possible publishing venues?

- Wikipedia, for general overviews of topics
- wikiHow, for how-to guides
- LessWrong
- reddit, which has a wiki feature for some subreddits now
- EA Forum
- Facebook
- Quora, Stack Exchange sites
- Topic-specific sites
- discussion forums? -- and more ephemeral forms of communication ...
- there are some other content creation sites, like erowid and everything2.
- personal site, for everything else

In some sense, the fact that some personal sites can grow so elaborately is an indictment against the web, since there exist no platforms that can take in content in an organized manner.
