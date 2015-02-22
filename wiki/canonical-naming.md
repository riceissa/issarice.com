---
title: Canonical naming
#description: none
author: Issa Rice
creation-date: 2015-01-02
last-major-revision-date: 2015-01-02
language: English
# accepts "notes", "draft", "in progress", or "mostly finished"
#status: notes
# accepts "certain", "highly likely", "likely", "possible", "unlikely", "highly unlikely", "remote", "impossible", "log", "emotional", or "fiction"
#belief: 
# accepts "CC0", "CC-BY", or "CC-BY-SA"
license: CC-BY
tags: content creation
---

Vipul Naik defines **canonical naming** in "[The goal of subject wikis](http://blog.subwiki.org/2009/02/02/the-goal-of-subject-wikis/)" as a [naming convention](!w) where "the name of a page on a topic is precisely that topic".

On this site, I've tried to apply this principle.
For instance, there used to be a page called "Content creation: the organization and dissemination of knowledge", but this page was on the subject of content creation, so now it assumes the name "[Content creation]()", adhering to its canonical name.

The problem sometimes is to figure out *what the name of the topic actually is*.
I used to have a page called "Openness and availability of content", but this seemed redundant, so I changed this to "Availability of content"; yet now it seemed prolix, so I finally changed it to "Content availability".
This process of "distilling" titles until they reach their simplest and precisest form I consider to be part of canonicalizing names.

One problem this leads to of course is frequent renaming.
Jekyll (which I don't happen to use for this site) has a redirect plugin, which I implemented for this site's static site generator as well (see [About the site](about-the-site#colophon) for more); now I simply use the `aliases` keyword in the YAML header of a page to create aliases.
