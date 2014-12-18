---
title: "Content creation: the organization and dissemination of knowledge"
tags: content-creation, information
license: CC0
...

The following was inspired by discussions with [Vipul Naik](http://vipulnaik.com).

# Openness and availability of content

This section considers how open one's content should be.
One definitely shouldn't “fetishize openness”, and ought to always consider to whom what you write will be useful (since if it's useful to no one, then one shouldn't bother publishing it).
Then again, it's sometimes hard to anticipate who will respond positively to what you write, which is one argument for greater openness.

See [Openness and availability of content](./openness-and-availability-of-content) for more.

# Choosing a medium (or media)

There are several alternatives for sharing content online, including on a blog, on a static website, on a third-party site like Quora, on a Google group, a mailing list, Facebook statuses, and so on.
We examine several options below.


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

## Blog

gwern [says](http://www.gwern.net/About#long-content):

> I have read blogs for many years and most blog posts are the triumph of the hare over the tortoise. They are meant to be read by a few people on a weekday in 2004 and never again, and are quickly abandoned - and perhaps as Assange says, not a moment too soon. (But isn’t that sad? Isn’t it a terrible ROI for one’s time?) On the other hand, the best blogs always seem to be building something: they are rough drafts - works in progress. So I did not wish to write a blog.

What you write is essentially useless if it doesn't last[^last].
As gwern highlights, [link rot is a huge problem](http://www.gwern.net/Archiving%20URLs), and human memory is highly fallible.
Ideally, you want to track each revision of a text so that even if you update it according to criticisms, people can still look back on the original to see the context in which comments were made.
Something like [Git](http://git-scm.com/) is great, although now even WordPress has version control built in (not that users have access to past versions of an entry).
In general it's best to plan in the *super long term*.

[^last]: There are two arguments against this view:
(1) it is often said that the act of writing something down is significant in itself (think of a diary or a [learning blog](http://qchu.wordpress.com/about/): "They say that the best way to learn is to teach, and I figure blogging is close enough");
(2) if the writing makes an immediate and lasting impact on the people who read the content, then it might not matter whether the content survives or not.

Blogs are bad because they send off a bad impression if you haven't written a new post in a while; with static sites, it's harder to tell (nor does it really matter) if you haven't written anything in a while, because the content isn't displayed chronologically.
Think critically whether chronology is important for something you're writing: unless it's a diary or daily log or something, it's unlikely that organizing something by date will be useful for the reader.

Blogs can be good since if people use RSS (or another notification system) to get content, blogs ensure that people who want to read what you write get it when it comes out.
Also on Facebook people post articles often, but not many pages from static sites (since those mostly go through minor adjustments over a long course).
On Facebook, what wins is a coherent message packed into an article, not an exhaustive investigation spanning many years.
So blogs might get you more publicity (at least while you have the energy to write continually).
That said, it *is* possible to set up RSS feeds on Hakyll and using other static site generators (Hakyll even has a blog option, after all!), but this will usually include minor adjustments or just when a page is first created; i.e. it isn't possible to tell when a page becomes "finished enough" when everything is a perpetual draft (like what gwern does).
Posting a monthly "what I did this month" sort of thing would work too (as again gwern does with his website); but then, it's possible to just make that announcement on Facebook?

Dan Dascalescu discusses [here](http://wiki.dandascalescu.com/essays/difference_blog_wiki) the difference between a blog and a wiki.

If you want to convey your thoughts on a topic at a certain point in time, or in response to time-critical material, then a blog might be the best way to produce content[^blog].
[Timeless](http://timelessrepo.com/timeless) echoes this:

[^blog]:  But version-controlled pages would work too.

> A blog is perfect for writing about *changes*: a person’s life, the
> society in general, the progress of a project, or other events. The
> readers are encouraged to frequently visit the blog in order to keep up
> to date, and in some blogs (these days: *most* blogs) they can also post
> comments and take a part of the discussion.
>
> So simple and so effective that it has slowly taken over the internet,
> which isn’t *only* positive. Useful information is hidden beneath
> “September 2008”, but is still as relevant today. Posts with glaring
> mistakes are left online because all blog posts should be immutable.
> People forget to write down the context (in the technical world: version
> numbers, operation systems etc), so it’s impossible to know if the post
> still applies a few years later.
>
> The blog has become the norm, even in the places where it doesn’t fit
> *at all*.

The conclusion is essentially identical to gwern's:

> The goal of Timeless is that every articles should be *timeless*. Well,
> not timeless in the usual meaning of the word, but timeless as in every
> article should include enough context to be easily understandable if you
> discover it a month, a year or maybe even ten years later. The article
> should be regularly updated as we learn and discover new aspects of the
> topic.



## Static sites

See [Long Content](http://www.gwern.net/About#long-content) by gwern:

> One of my personal interests is applying the idea of the Long Now. What and how do you write a personal site with the long-term in mind?

But also keep “[not invented here](https://en.wikipedia.org/wiki/Not_invented_here)” in mind: are you reinventing the wheel?

Also many more websites use things like WordPress rather than static sites built using things like Jekyll or Hakyll.
So wonder: are you missing something that the "crowd" has?


## More "advanced" content management systems like WordPress and MediaWiki

These tend to be very easy to install and use.
See more at “[Choice of content management system](http://info.cognitomentoring.org/wiki/Creating_your_personal_website#Choice_of_content_management_system)” on the Cognito Mentoring wiki.

## Google group

See "[What are the advantages of a blog versus a Google group or email list?](ihttps://www.quora.com/What-are-the-advantages-of-a-blog-versus-a-Google-group-or-email-list)" on Quora.
<!-- I have to investigate this more, though Google groups seem to not be very popular.-->

## Mailing lists

Insufficient investigation.


## Crossposting

Crossposting content to different sites can be useful because different audiences respond differently to the same content.
It's possible to just host the content on your website and drop a link for other sites, but keep in mind that people may be too lazy to click on a link if they don't know why it might be relevant for them.
Including a quote or copy-pasting the whole article may be better.


# Hosting options

Some media (like blogs) allow the choice of whether to host the content oneself (e.g. using WordPress's software on one's own servers), or to post all content "on the cloud", i.e. on a third-party's servers (e.g. on [WordPress.com](https://wordpress.com)).
We discuss the advantages and disadvantages of each.

## Self-hosted

- Depends a lot on how knowledeable one is, although even if one isn't, it's a great learning opportunity.
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

A website may be thought of as having a rooted [tree structure](ihttp://en.wikipedia.org/wiki/Tree_%28graph_theory%29); we look at this concept more closely here.

Vipul Naik considers two questions

1. How specific should the individual leaf node pages be?
In other words, at the bottommost places of the tree, how much content should be in those pages?

2. For a particular choice of leaves, how should we trade off the breadth versus depth of the tree?
In other words, how many intermediate levels should the tree have?

To understand the two questions better, consider the following pages that might be on a website:

- How to use the `proof` environment  in LaTeX (called "proof" below)
- How to configure the `thmtools` package on LaTeX ("thmtools")
- A list of math symbols in LaTeX ("symbols")
- How to use Vim with LaTeX ("Vim")
- How to use Emacs with LaTeX ("Emacs")
- How to typeset a Japanese LaTeX document ("Japanese")
- How to typeset a Spanish LaTeX document ("Spanish")
- How to mix languages in LaTeX ("mix")

Question (1) asks whether all of these deserve a page: is it better to have a single comprehensive page (at one extreme) or be as modular as possible (at the other extreme)?
Between these extremes, we could combine just some pages; for instance, "proof" and "thmtools" could be combined into a "math packages" page.

For question (2), *given that* each of the above deserve a page, we want to know how to organize the list as a tree.
At one extreme, we could just have a "How to use LaTeX" container-page that links to all of the above pages.
This would be pushing *breadth* to the maximum, and would look like the following (any page with brackets around them are container-pages that link to the actual leaves.):

```
    [       How         to        use        LaTeX       ]
    /      /         /     |     |      \         \      \
proof  thmtools  symbols  Vim  Emacs  Japanese  Spanish  mix
```

On the other hand, we can have intermediate pages like "Math and LaTeX", "Editing LaTeX", and "LaTeX and languages" all under "How to use LaTeX", and then have the relevant pages linked under the intermediate pages.
This has more depth than the first example, and looks like:

```
            [     How     to    use    LaTeX    ]
            /                |                  \
    [Math and LaTeX]   [Editing LaTeX] [LaTeX and languages]
    /      |       \       |     |       /         |      \
proof  thmtools  symbols  Vim  Emacs  Japanese  Spanish  mix
```

At the other extreme (i.e. the most depth), we can make a "math packages" container-page that creates a new level and have something like:

````
                    [How   to   use   LaTeX]
                    /         |            \
     [Math and LaTeX]     [Editing LaTeX]  [LaTeX and languages]
      /           \           |      \         |        |     \
 [Math packages]  symbols    Vim    Emacs   Japanese Spanish mix
  /        \
proof  thmtools
````

## Content length

See for instance [this post](https://www.facebook.com/vipulnaik.r/posts/10202707831592850) by Vipul on Slate Star Codex being a blog with long posts.

# Thinking about impact

Here we consider how much impact writing online can make on the world.

- See [What's the relative social value of 1 Quora pageview (as measured by Quora stats http://www.quora.com/stats) and 1 Wikipedia pageview (as measured at, say, Wikipedia article traffic statistics)?](https://www.quora.com/Whats-the-relative-social-value-of-1-Quora-pageview-as-measured-by-Quora-stats-http-www-quora-com-stats-and-1-Wikipedia-pageview-as-measured-at-say-Wikipedia-article-traffic-statistics) for a comparison of Quora and Wikipedia.

- Easily-accessible online content can be useful for oneself; Terence Tao [says](http://terrytao.wordpress.com/career-advice/write-down-what-youve-done/):

    > There were many occasions early in my career when I read, heard
    > about, or stumbled upon some neat mathematical trick or argument,
    > and thought I understood it well enough that I didn’t need to
    > write it down; and then, say six months later, when I actually
    > needed to recall that trick, I couldn’t reconstruct it at all.
    > Eventually I resolved to write down (preferably on a computer) a
    > sketch of any interesting argument I came across – not necessarily
    > at a publication level of quality, but detailed enough that I
    > could then safely forget about the details, and readily recover
    > the argument from the sketch whenever the need arises.

- Within mathematics, [Terence Tao argues](http://terrytao.wordpress.com/career-advice/make-your-work-available/) that sharing online helps with networking:

    > In particular, your work will show up in search engine queries in
    > your topic (I have come across many an interesting paper this
    > way). This will help spread awareness of you and your work among
    > your colleagues, and hopefully lead to future collaborations, or
    > other people building upon (and citing) your papers.

- See [this post](https://www.facebook.com/vipulnaik.r/posts/10202840266223633) by Vipul Naik on whether there is low-hanging fruit for encouraging young people to work on side projects, including web content creation.

- See [this post](https://www.facebook.com/vipulnaik.r/posts/10202884940740468) by Vipul Naik on whether academic research or blogging produces more social value.

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

- See also [this post](https://www.facebook.com/groups/1520172064903930/permalink/1527384787515991/) by Vipul Naik on Libertarian Effective Altruists.

    > "Only a crisis-actual or perceived-produces real change. When that
    > crisis occurs, the actions that are taken depend on the ideas that are
    > lying around. That, I believe, is our basic function: to develop
    > alternatives to existing policies, to keep them alive and available
    > until the politically impossible becomes politically inevitable." --
    > [Milton Friedman](https://www.facebook.com/FriedmanMilton) (HT [Naomi
    > Klein](https://www.facebook.com/profile.php?id=634133341)). I think one
    > of the goals of libertarian(-ish) policy advocacy, such as free trade,
    > ending the drug war, open borders, deregulation, etc. is to create such
    > ideas that are lying around, so that followers of more mainstream
    > political ideologies can pick them up when a crisis (real or perceived)
    > strikes.
    > 
    > cf.
    > <https://www.facebook.com/groups/1520172064903930/permalink/1526940824227054/>
    > 
    > HT
    > [http://reason.com/archiv…/2008/…/26/defaming-milton-friedman](http://reason.com/archives/2008/09/26/defaming-milton-friedman)
    > for the quote
    > 
    > I think of sites like
    > [http://openborders.info](http://openborders.info/) (started by me, but
    > with many other active participants),
    > [http://www.policemisconduct.net](http://l.facebook.com/l.php?u=http%3A%2F%2Fwww.policemisconduct.net%2F&h=3AQEzYRDh&enc=AZNEb-oI1Mc1n4qiJ1_4ZYyptSn5iY4n9dkawz5WfZPtEKqE9uhcj_UyYrx0V8gYwEFHl_4T5jSd07xixQquSQI36-ivlthqc6kNDITe1qLkSexV2-pQSQiZGTqr72Zk8C9su23hko4cvZEaJrmu_dPg&s=1)
    > (no involvement from me), and the forthcoming Free Drugs website as
    > creating that base of "ideas lying around."
    > 
    > Thoughts?


- Granularity/modularity

- Is it a good idea to post things like fiction online?

- Do we want pages to be in a tree-like structure, or just let tags do all the work?

- Talk about top down versus bottom up.

- Despite my criticisms of blogs, some of the most popular websites currently in existence are blogs.
Does this mean blogs are superior to e.g. static sites?

- Since I've only begun to write recently, how can I even know these considerations are correct?
