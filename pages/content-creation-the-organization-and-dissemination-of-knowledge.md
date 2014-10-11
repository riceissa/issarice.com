---
title: Content creation: the organization and dissemination of knowledge
tags: content creation, information
...

The following was inspired by discussions with VN.

## Major considerations

- how open to make content. copying what i wrote for CM wiki:

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




- static site vs more "advanced" things like WP, mediawiki, etc.
- blogs???
- Long Content by gwern

What you write is essentially useless to your audience if it doesn't last (even though, like a diary, the act of writing something down may have been significant, and if the writing made an immediate impact on the people who read it).
AS gwern highlights, link rot is a huge problem, and human memory is highly fallible.
Ideally, you want to track each revision of a text so that even if you update it according to criticisms, people can still look back on the original to see the context in which comments were made.
(suggest git, or WP has version control too now, I guess)
In general it's best to plan in the *super long term*.

blogs are bad because

- they send off a bad impression if you haven't written a new post in a while; with static sites, it's harder to tell (nor does it really matter) if you haven't written anything in a while, because the content isn't displayed chronologically.
Think critically whether chronology is important for something you're writing: unless it's a diary or daily log or something, it's unlikely that organizing something by date will be useful for the reader.

<!-- -->

- tagging system?

I think that tags are best implemented using [DAGs](https://en.wikipedia.org/wiki/Directed_acyclic_graph), but I haven't encountered software that actually does this.
WordPress, which has both categories and tags, uses a tree structure for its categories and simply has flat tags ([see here](https://wordpress.org/ideas/topic/allow-child-category-to-have-multiple-parents) for why we want something else).
Other implementations are similar; Hakyll tags are flat, for instance.

- searching? VS hierarchical structure: Google vs DMOZ (VN's comparison)

Is it a good idea to rely on external search (like Google)?
If all pages are static and can be pulled from GitHub, then it seems that one can (1) just search on GitHub, or (2) search locally using a simple bash script that loops over files using `find` (or something similar).

- how much effort to expend on navigation stuff

- hosting options
Linode definitely works, but is the cost worth it?

- what to do about style? SSC? AKC? VN?
- the use of external links: is it a good idea to restrict the use of these so you can keep people on your site, and thus control how they see info?

- licensing? gwern likes CC0; some others use CC-BY or CC-BY-SA.
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
