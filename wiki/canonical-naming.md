---
title: Canonical naming
author: Issa Rice
created: 2015-01-02
date: 2015-02-22
---

Vipul Naik defines **canonical naming** in "[The goal of subject wikis](http://blog.subwiki.org/2009/02/02/the-goal-of-subject-wikis/)" as a [naming convention](!w) where "the name of a page on a topic is precisely that topic".

On this site, I've tried to apply this principle.
For instance, there used to be a page called "Content creation: the organization and dissemination of knowledge", but this page was on the subject of content creation, so now it assumes the name "[Content creation]()", adhering to its canonical name.

The problem sometimes is to figure out *what the name of the topic actually is*.
I used to have a page called "Openness and availability of content", but this seemed redundant, so I changed this to "Availability of content"; yet now it seemed prolix, so I finally changed it to "Content availability".
This process of "distilling" titles until they reach their simplest and precisest form I consider to be part of canonicalizing names.

One problem this leads to of course is frequent renaming.
Jekyll (which I don't happen to use for this site) has a redirect plugin, which I implemented for this site's static site generator as well (see [Colophon]() for more); now I simply use the `aliases` keyword in the YAML header of a page to create aliases.

On a subject-specific website about subject X, canonical naming of topic Y
leads to a page that describes Y as it relates to or fits into X.
What about canonical naming on a personal site, such as this one?
It might answer the question "What are this person's thoughts on this topic?"
But on biographical pages this adds an unnecessary layer, for the previous
question expands to "What are this person's thoughts on this person's
biography?"
One might also want to know what the person's thoughts are on the topic *now*
vs 10 years ago, and how it evolved.
To some extent this can be captured using [versioning](versioning-prose).
This line of thought leads to some interesting possibilities:

* Perhaps canonical naming is *too simplified* and is unnatural for organizing
  content.
* Perhaps personal sites are unsuitable for storing content.
