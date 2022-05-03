---
title: Content creation
author: Issa Rice
status: draft
---

This page is about **content creation**.
Narrowly, it is the act of writing online to spread useful information.
More broadly, it is the act of creating any sort of online content (i.e. in any media: text, image, video, audio) and publishing it online.
[Wikipedia has an article on content creation](https://en.wikipedia.org/wiki/Content_creation).
This page documents my thoughts on content creation: how to best organize information, how to effectively publish content, and how to have an impact on the world through content creation, among other things.

The following was inspired by discussions with [Vipul Naik](http://vipulnaik.com).

# Availability

This section considers how open one's content should be.
One definitely shouldn't “fetishize openness”, and ought to always consider to whom what you write will be useful (since if it's useful to no one, then one shouldn't bother publishing it).
Then again, it's sometimes hard to anticipate who will respond positively to what you write, which is one argument for greater openness.

See [[Content availability]] for more.

# Choosing a medium (or media)

There are several alternatives for sharing content online, including on a blog, on a static website, on a third-party site like Quora, on a Google group, a mailing list, Facebook statuses, and so on.
We examine several options below.
See also the chart [Where should I publish a given piece?](http://reducing-suffering.org/is-it-better-to-blog-or-formally-publish/#Where_should_I_publish_a_given_piece) by Brian Tomasik.


## Quora

Quora can be good in terms of gaining viewership, since for people who are not established as writers, it is much easier to be read on Quora than to attract readers to one's own site.
On the other hand, Quora is a third-party site that is not afraid of making radical decisions[^quora], so it is always a good idea to backup one's writings from there.

[^quora]: For instance they recently eliminated private blogs.

Christopher J. Su [says](https://www.quora.com/How-should-one-balance-the-potential-for-Quora-to-delete-ones-questions-answers-with-the-increased-viewership-one-obtains-compared-to-a-personal-website/answer/Christopher-J-Su):

> I tend to lean towards publishing content on websites where people can
> actually read it. Apart from exercising writing skills, saving for
> future reference, or reflecting on something, I find there aren't many
> other reasons to write content just for myself. Backing up content
> written on other websites is fairly trivial (especially if they have a
> public API, which unfortunately, Quora doesn't \[yet\]). Quora keeps a
> log of all content history, so your content isn't at risk of being
> lost forever as a result of editing. If Quora goes down, they'll most
> likely give a month's notice (at least), and in that timeframe before
> they shutdown for good, you should have enough time to grab your
> content and save it somewhere (when large content-based websites go
> down, people usually build export tools for them. For example,
> Posterous).
>
> If you really want to play it safe, you can crosspost your longer
> Quora answers to your personal website. I've seen a few people do that
> (some even just post a link to their website/blog as their answer on
> Quora).


## Blogs

A variety of arguments have been put forth both for and against blogs.
See [[Arguments for and against blogs]] for more.

## Static sites

See [Long Content](http://www.gwern.net/About#long-content) by gwern:

> One of my personal interests is applying the idea of the Long Now. What and how do you write a personal site with the long-term in mind?

But also keep “[not invented here](https://en.wikipedia.org/wiki/Not_invented_here)” in mind: are you reinventing the wheel?

Also many more websites use things like WordPress rather than static sites built using things like Jekyll or Hakyll.
So wonder: are you missing something that the "crowd" has?

See also [Static site generators focus on the wrong thing](https://news.ycombinator.com/item?id=7822233).

## More "advanced" content management systems like WordPress and MediaWiki

These tend to be very easy to install and use.
See more at “[Choice of content management system](http://info.cognitomentoring.org/wiki/Creating_your_personal_website#Choice_of_content_management_system)” on the Cognito Mentoring wiki.

## Google group

See "[What are the advantages of a blog versus a Google group or email list?](https://www.quora.com/What-are-the-advantages-of-a-blog-versus-a-Google-group-or-email-list)" on Quora.
<!-- I have to investigate this more, though Google groups seem to not be very popular.-->

## Mailing lists

Insufficient investigation.


## Crossposting

Crossposting content to different sites can be useful because different audiences respond differently to the same content.
It's possible to just host the content on your website and drop a link for other sites, but keep in mind that people may be too lazy to click on a link if they don't know why it might be relevant for them.
Including a quote or copy-pasting the whole article may be better.

# Contributing to another site

Consider whether publishing something on one's own site is preferable to publishing in a place where others can edit your work (e.g. Wikipedia).
Brian Tomasik writes in [Is It Better to Blog or Formally Publish? | Essays on Reducing Suffering](http://reducing-suffering.org/is-it-better-to-blog-or-formally-publish/):

> If what you want to write is not original, then consider adding the content to
> Wikipedia rather than reinventing wheels.

See also [Sponsored Wikipedia editing](http://vipulnaik.com/sponsored-wikipedia-editing/) and [The Value of Wikipedia Contributions in Social Sciences | Essays on Reducing Suffering](http://reducing-suffering.org/the-value-of-wikipedia-contributions-in-social-sciences/).

# Hosting options

Some media (like blogs) allow the choice of whether to host the content oneself (e.g. using WordPress's software on one's own servers), or to post all content "on the cloud", i.e. on a third-party's servers (e.g. on [WordPress.com](https://wordpress.com)).
We discuss the advantages and disadvantages of each.

## Self-hosted

- Depends a lot on how knowledgeable one is, although even if one isn't, it's a great learning opportunity.
- Usually costs money, though there might be special opportunities like the [Student Developer Pack](https://education.github.com/pack).

## Third-party

- If one isn't good about backing up one's content, then third-parties may do a better job serving your content.
Alex K. Chen [likes to emphasize](https://www.quora.com/How-does-Alex-K-Chen-make-backups-of-his-content-on-Quora/answer/Alex-K-Chen) that everything on Quora will last: "I do trust Quora more than I can trust myself".

- Consider the quote from [here](http://whatisresearch.wordpress.com/2007/01/09/wikis/):

    > However, I realized that putting up material on Wikipedia has some
    > limitations:
    >
    > * I cannot organize the article content of definition articles the way
    > I want
    > * I have very little control over the global structure, something
    > which is very crucial to effective navigation and exploration.
    > * I cannot put up original work and original ideas


# Topic ontology

This concerns things like a tagging system.

I think that tags are best implemented using [DAGs](https://en.wikipedia.org/wiki/Directed_acyclic_graph), but I haven't encountered software that actually does this.
WordPress, which has both categories and tags, uses a tree structure for its categories and simply has flat tags ([see here](https://wordpress.org/ideas/topic/allow-child-category-to-have-multiple-parents) for why we want something else).
Other implementations are similar; Hakyll tags are flat, for instance.


# Searching

Arguably people find your content most useful when they encounter it through a search; for instance Vipul Naik [writes](https://www.quora.com/Whats-the-relative-social-value-of-1-Quora-pageview-as-measured-by-Quora-stats-http-www-quora-com-stats-and-1-Wikipedia-pageview-as-measured-at-say-Wikipedia-article-traffic-statistics):

> I believe that views that are generated by direct search are considerably more valuable than views that are generated by clicking through things in one's feed. Direct search signals a specific desire to learn about the topic, whereas clicking links in one's feed is a quasi-passive activity.

Searching also tends to be the greatest source of hits for websites (source?).

As for finding content, Vipul Naik brings up the comparison between Google and DMOZ: almost nobody uses DMOZ's hierarchical system to find content nowadays.

It's unclear whether it's a good idea to rely on an external search (like Google) for one's site.
If all pages are static and can be pulled from GitHub, then it seems that one can (1) just search on GitHub; (2) search locally using a simple bash script that loops over files using `find` (or something similar).

If one uses WordPress or a third-party site, then one doesn't need to spend any time on navigation, since search is built-in.
For static sites, people will probably just use Google anyway, so spending time on navigation may not be worthwhile.


# Voice

The voice or style of writing isn't specific to sharing content online, but is nonetheless important to think about; we discuss some alternatives.

## The "non-voice"

It's very boring if the content is just in the form of "he said, she said", since (a) you sound less convincing because you're not saying what *you* think; (b) for instance on Quora, the answers are often opinion, so one must in each instance consider how reliable their answers are (and this may be seen as rude by some).

However, it is still possible to write in a deliberate fashion without being emotional.
See for instance [Academia as a career option](http://info.cognitomentoring.org/wiki/Academia_as_a_career_option).
This style of writing tends to be factual, but unlike a "he said, she said" form, still includes useful insight from oneself, and has a clear underlying motivation that is not just "let's collect opinions on this topic".

Citing sources is also important.

## Engaging, argumentative voice

The epitomical example of this style is [Slate Star Codex](http://slatestarcodex.com/).
If executed well, this style has the potential to "hook" the readers into reading more of what you write.

Paul Graham's [essays](http://paulgraham.com/essay.html) would probably fit under here as well.


# The tree structure of a website

I have a separate page on [[Using a tree structure for websites]].


## Content length

See for instance [this post](https://www.facebook.com/vipulnaik.r/posts/10202707831592850) by Vipul on Slate Star Codex being a blog with long posts.

# Thinking about impact

One can ask whether content creation has any lasting value---especially when done by people online (i.e. not through a publisher).
See [The value of content creation](./the-value-of-content-creation) for more.

# Some remaining questions

- The use of external links: is it a good idea to restrict the use of these so you can keep people on your site, and thus control how they see info?


- [This article](http://blog.subwiki.org/2009/02/02/the-goal-of-subject-wikis/) is interesting.

    > Some of the specific principles derived from this include: a high
    > level of *modularization with articles as the basic units*
    > combined with *pinpoint referencing*: it is easy and quick to get
    > an answer to a specific question. Each topic has its separate
    > article, achieving a high level of granularity and modularity.
    > Pinpoint referencing is achieved by canonical naming (the name of
    > a page on a topic is precisely that topic), good redirection and
    > disambiguation, excellent search features, and good-quality
    > categorization. Another principle is *strong internal linking*:
    > pages are linked to closely related pages in a way that symbolizes
    > and explains the manner of the relationship. This allows for
    > easier location of new facts, stimulation of curiosity, and
    > expansion of knowledge. Yet another principle is
    > *standardization*: standardization of page format for similar
    > pages, leading to predictability and reliability. A principle that
    > is important and not obvious is *genericity*: individual subject
    > wiki pages should largely make sense as independent entry points
    > into the wiki, so that people coming from outside can go straight
    > there. While they should link to other subject wiki entries, they
    > should not be dependent on them in a strong sense.  Most
    > important, there should be no *forced sequencing* of the entries
    > as in a textbook, where future entries depend on earlier ones.

- See [[Having ideas that are lying around]].

- Granularity/modularity

- Is it a good idea to post things like fiction online?

- Do we want pages to be in a tree-like structure, or just let tags do all the work?

- Talk about top down versus bottom up.

- Despite my criticisms of blogs, some of the most popular websites currently in existence are blogs.
Does this mean blogs are superior to e.g. static sites?

- Since I've only begun to write recently, how can I even know these considerations are correct?

- From [10 Types of Odd Friendships You're Probably Part Of - Wait But Why](http://waitbutwhy.com/2014/12/10-types-odd-friendships-youre-probably-part.html) (italics removed):

    > A note about listicles: So we know a lot of people hate listicles
    > and associate them with cheap, low-quality, traffic-driving,
    > link-bait articles. But here’s the thing—a list is a great format
    > for an article, and a format I was using on my old blog almost 10
    > years ago. In fact, my first listicle, 19 Things I Don’t
    > Understand, was published in August of 2005, a year before
    > Buzzfeed was even founded. Then, over the last few years, I
    > watched in horror as one of my favorite formats decided to
    > prostitute itself all over the internet as the default format for
    > lazy articles. Anyway the point is, A) I was doing listicles
    > before they were cool, and B) A list headline doesn’t mean it
    > can’t be a high-quality article, so C) Wait But Why will make a
    > listicle when it’s the best format for that post, and don’t be mad
    > at us cause it’s not what it looks like.

- Nick Bostrom in his [preface](http://www.anthropic-principle.com/?q=book/preamble#Pre) to *Anthropic Bias*:

    > One note to the reader before we start. Whether because of an
    > intrinsic organic quality of the subject matter or because of
    > defects in my presentation skills, I have found it difficult to
    > organize the exposition in a completely linear sequence where each
    > chapter can be fully comprehended without having read what comes
    > after. Instead, some important themes are revisited many times
    > over the course of this book, and some essential qualifications
    > are added in a piecemeal fashion. I would plead that the reader
    > not rush to a judgement until the last page has been reached and
    > the idea-complex has been grasped in its entirety.

# See also

Here is a (possibly partial) list of pages related to content creation on this site.
Note that some of them have already been linked to on this page.

- [[Anonymity]]
- [[Arguments for and against blogs]]
- [[Canonical naming]]
- [[Comments]]
- [[Content availability]]
- [[Content licensing]]
- [[Egoism of personal websites]]
- [[Good content]]
- [[Good entry point]]
- [[Having a personal website]]
- [[Having “ideas that are lying around”]]
- [[Jargon]]
- [[Linkability]]
- [[Linking effectively]]
- [[Long Content]]
- [[Not a dictionary]]
- [[Open Borders: The Case]]
- [[Overlinking]]
- [[Perfectionism]]
- [[Personal thoughts on licensing]]
- [[Quora]]
- [[Requirements for a website]]
- [[Single source publishing]]
- [[Tabular presentation]]
- [[Tag ontology]]
- [[The value of content creation]]
- [[Thoughts on using Reddit effectively]]
- [[Using a tree structure for websites]]
- [[Wikipedia]]
- [[mojix]]
- [[“He said, she said”]]
- [[wikiHow]]

# External links

- [Discussion (that never took off) on Vipul Naik's Facebook feed](https://www.facebook.com/vipulnaik.r/posts/10204192033496970)
