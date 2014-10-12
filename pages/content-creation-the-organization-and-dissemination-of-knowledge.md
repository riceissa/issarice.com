---
title: Content creation: the organization and dissemination of knowledge
tags: content creation, information
license: CC0
...

The following was inspired by discussions with VN.

## Openness/Availability of content

- how open to make content.
One definitely shouldn't "fetishize openness", and always consider to whom what you write will be useful.
Then again, it's sometimes hard to anticipate who will respond positively to what you write (that is one argument *for* openness).
copying what i wrote for CM wiki:

### Selecting an appropriate audience

There exists a spectrum for sharing information about oneself; i.e.
there is no dichotomy of either complete privacy or complete release of
information. Consider the gradual increase in visibility in the
following:

1.  Keeping one's data local (on one's own hard drive)
2.  Keeping data on a cloud service but available only to oneself (so
    that the service provider, such as Google, can potentially view or
    use the data)
3.  Keeping data on a cloud service but with the ability to invite other
    authorized users to view the data (e.g. restricted Facebook posts)
4.  Making the data public, but not locatable by search engines, so that
    effectively only people with the link can view the data (this is,
    for instance, what [GitHub](https://github.com/) does with its
    [secret
    gists](https://help.github.com/articles/about-gists#secret-gists))
5.  Releasing the data publicly and making it locatable by search
    engines

Additionally, in each case, one has the option of using one's real name
or a pseudonym (or, in some cases, staying anonymous). It is important
to know, then, that some of the pros and cons of privacy will only apply
to a certain part of this spectrum.

In terms of content sharing online, this means that one can attempt to
restrict the audience that receives specific content. Since your
interests are likely to not overlap completely with that of most people,
targeting content to an audience who shares a particular interest will
likely mean that (1) they will be happier seeing content that applies to
them, and (2) you will receive better feedback on what you post.
Restriction of the whole discussion may also mean that people will give
you more candid responses.

### Licensing

licensing? gwern likes CC0; some others use CC-BY or CC-BY-SA.
stallman also has some insight on this.

## Choosing a medium (or media)

There are several alternatives for sharing content online, including on a blog, on a static website, on a third-party site like Quora, on a Google group, a mailing list, Facebook statuses, and so on.


### Quora

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

### Blog

Gwern [says](http://www.gwern.net/About#long-content):

> I have read blogs for many years and most blog posts are the triumph of the hare over the tortoise. They are meant to be read by a few people on a weekday in 2004 and never again, and are quickly abandoned - and perhaps as Assange says, not a moment too soon. (But isn’t that sad? Isn’t it a terrible ROI for one’s time?) On the other hand, the best blogs always seem to be building something: they are rough drafts - works in progress. So I did not wish to write a blog.

What you write is essentially useless to your audience if it doesn't last (even though, like a diary, the act of writing something down may have been significant, and if the writing made an immediate impact on the people who read it).
AS gwern highlights, link rot is a huge problem, and human memory is highly fallible.
Ideally, you want to track each revision of a text so that even if you update it according to criticisms, people can still look back on the original to see the context in which comments were made.
(suggest git, or WP has version control too now, I guess)
In general it's best to plan in the *super long term*.

blogs are bad because they send off a bad impression if you haven't written a new post in a while; with static sites, it's harder to tell (nor does it really matter) if you haven't written anything in a while, because the content isn't displayed chronologically.
Think critically whether chronology is important for something you're writing: unless it's a diary or daily log or something, it's unlikely that organizing something by date will be useful for the reader.

Some good stuff about blogs: since people use RSS (or other notification system) to get content blogs ensure that people who want to read what you write get it when it comes out.
Also one FB people post articles often, but not many *pages* from static sites (since those mostly go through minor adjustments over a long course).
On FB, what wins is a coherent message packed into an article, not an exhaustive investigation spanning many many years.
so blogs might get you more publicity (at least while you have the energy to write continually).
that said, it *is* possible to set up RSS feeds on Hakyll and other static sites (Hakyll even has a blog option, after all!), but this will usually include minor adjustments or just when a page is first created; i.e. it isn't possible to tell when a page becomes "finished enough" when everything is a perpetual draft (like what gwern does).
Posting a monthly "what did I do this month" sort of thing would work too ( as gwern does with his website), but then... why not just make that announcement on FB or somewhere?

Dan Dascalescu discusses [here](http://wiki.dandascalescu.com/essays/difference_blog_wiki) the difference between a blog and a wiki.

If you want to convey your thoughts on a topic at a certain point in time, or in response to time-critical material, then a blog might be the best way to produce content[^blog].
[Timeless](http://timelessrepo.com/timeless) echoes this:

[^blog]:  (but version-controlled pages would work too)



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



### Static sites

 Long Content by gwern

> One of my personal interests is applying the idea of the Long Now. What and how do you write a personal site with the long-term in mind?

But also keep [this](https://en.wikipedia.org/wiki/Not_invented_here) in mind.

Consider also that *many many more* websites use things like WordPress instead of static sites like Jekyll or Hakyll.
So wonder: are you missing something that the "crowd" has?

### More "advanced" content management systems like WordPress and MediaWiki

hmmm not much for now. wordpress is very easy to install and use though.

### Google group

See "[What are the advantages of a blog versus a Google group or email list?](ihttps://www.quora.com/What-are-the-advantages-of-a-blog-versus-a-Google-group-or-email-list)" on Quora.
I have to investigate this more, though Google groups seem to not be very popular.

### Mailing lists

Insufficient investigation.


### Crossposting

 the importance of cross posting 



## Hosting options

Some media allow the choice of whether to host the content oneself, or to post all content "on the cloud", i.e. on a third-party's servers.
We discuss the advantages and disadvantages of each.

### Self-hosted

Linode definitely works, but is the cost worth it?

### Third party

AKC likes to emphasize that everything on Quora will last.

Consider the quote from [here](http://whatisresearch.wordpress.com/2007/01/09/wikis/):

> However, I realized that putting up material on Wikipedia has some
> limitations:
>
> * I cannot organize the article content of definition articles the way
> I want
> * I have very little control over the global structure, something
> which is very crucial to effective navigation and exploration.
> * I cannot put up original work and original ideas


## Topic ontology

This concerns things like a tagging system.

I think that tags are best implemented using [DAGs](https://en.wikipedia.org/wiki/Directed_acyclic_graph), but I haven't encountered software that actually does this.
WordPress, which has both categories and tags, uses a tree structure for its categories and simply has flat tags ([see here](https://wordpress.org/ideas/topic/allow-child-category-to-have-multiple-parents) for why we want something else).
Other implementations are similar; Hakyll tags are flat, for instance.


## Searching

searching? VS hierarchical structure: Google vs DMOZ (VN's comparison)

Is it a good idea to rely on external search (like Google)?
If all pages are static and can be pulled from GitHub, then it seems that one can (1) just search on GitHub, or (2) search locally using a simple bash script that loops over files using `find` (or something similar).

- how much effort to expend on navigation stuff



## Voice

The voice or style of writing isn't specific to sharing content online, but is nonetheless important to think about.

what to do about style? SSC? AKC? VN?

We discuss some alternatives.

### The "non-voice"

It's very boring if the content is just in the form of "he said, she said", since (a) you sound less convincing since you're not saying what *you* think, and (b) since e.g. on Quora, the answers are often opinion, one must in each instance consider how reliable their answers are (and this consideration may be considered rude by some).

- factual
- neutral tone
- citing sources?

### Engaging, argumentative voice

- potential to "hook" the readers into reading more of what you write



- the use of external links: is it a good idea to restrict the use of these so you can keep people on your site, and thus control how they see info?

anything less free than that is not very useful.

- [this article](http://blog.subwiki.org/2009/02/02/the-goal-of-subject-wikis/) is interesting.

- granularity/modularity

- is it a good idea to post things like fiction online?

- one question is, do we want pages to be in a tree-like structure?

consider:

````
                     effective altruism
                       /             \
           earning to give          direct impact
           /
        finance
````

etc.
Is it a good idea to have sections within the root that link out to the children?
An alternative (not mutually exclusive) is to let tagging take care of everything.
So by tagging all articles above with "effective altruism", we allow the reader to find all relevant information (but there is less structure here; it might be nice to have separate tags for each bigger nodes...).

## The tree structure of a website

VN's two questions: (1) "how specific should the individual leaf node pages be"? (2) "For a particular choice of leaves, how should we trade off the breadth vs depth of the tree?"
For (2): the question is essentially, "how many intermediate levels should we have?"

For (2):

consider that we have the following pages:

- how to use the `proof` environment  in LaTeX
- how to configure the `thmtools` package on LaTeX
- a list of math symbols in LaTeX
- how to set up Vim to work with LaTeX
- how to use emacs with LaTeX
- how to insert Japanese text in a LaTeX document
- how to typeset a Spanish LaTeX document
- how to mix languages in LaTeX

at one extreme, we could just have a "How to use LaTeX" page that links to all of the above pages. (this would be pushing breadth to the maximum)
On the other hand, we can have intermediate pages like "math and LaTeX", "editing a LaTeX document", and "using LaTeX in different languages", and then have the relevant pages linked from the intermediate pages (this has more depth than the first example).
at the other extreme (i.e. the most depth), we can have something like:

````
                    [How  to  use   LaTeX]
                    /       |          \
     [math and LaTeX] [editing LaTeX] [LaTeX and languages]
      /           \          |     \     /     |          \
 [math packages] symbols    emacs  vim mix  Japanese     Spanish
  /        \
thmtools  proof
````

above, the pages with brackets around them are "container pages" that link to the actual leaves. Note how there is a "math packages" node that contains the separate math environments, which creates a new intermediate level.

\(1) just asks whether all the bottom-most leaves should remain separate pages, or whether they should be combined into one (at the extreme).
"thmtools" and "proof" could be combined into a "math packages" page (which then wouldn't be a container), for instance.

talk about top down versus bottom up.

## Thinking about impact

how much impact can writing online make?
