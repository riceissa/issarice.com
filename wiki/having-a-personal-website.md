---
title: Having a personal website
#description: none
author: Issa Rice
creation-date: 2014-12-26
last-major-revision-date: 2014-12-26
language: English
# accepts "notes", "draft", "in progress", or "mostly finished"
status: notes
# accepts "certain", "highly likely", "likely", "possible", "unlikely", "highly unlikely", "remote", "impossible", "log", "emotional", or "fiction"
belief: possible
# accepts "CC0", "CC-BY", or "CC-BY-SA"
license: CC-BY
tags: content creation
---

This page describes my thoughts on having a personal website.
Having a personal website is part of [maintaining one's online presence](http://info.cognitomentoring.org/wiki/Maintaining_your_online_presence).



# Advantages

- Having a single place to store all of one's writings, social media profiles, etc., seems like a good idea
- Helps with being transparent to the world
- Gives a place to write one's opinions that don't fit anywhere else
- Practice with managing a website alone
- May be useful in terms of dating, because here the individual is much more important than the topic.

# Disadvantages

- Inherently egoistic
- Cost (good ones tend to have their own domain names, for instance)
- In general it seems like a bad idea to organize content by author than by topic; liking someone's writing about cooking doesn't say much about liking someone's writing about programming, for instance.
Having, say, one website about cooking (written by various people) and a separate one about programming (written by various people, some of whom may overlap with the cooking website) is much more likely to produce relevant results for everybody.

Compare the following organizations:

````
       A                B                 C
      / \              / \                |
   cook  prog     cook1  cook2           prog
````

versus

````
      [  cook  ]            [prog]
      /   |    \            /    \
    A     B1    B2         A      C
````

Ceteris paribus, the second organization is preferable because people are more likely to be interested in a topic than a person (?).

# Compromise?

One thing to note is that, even given the disadvantages of having one's own website, one can still have a website but primarily post in places other than one's own website, for instance in Facebook groups or on topic-specific websites.
For instance, I post all of my research relevant to [cause prioritization]() on the [Cause Prioritization Wiki](http://causeprioritization.org/).

In addition, there is often information that cannot fit in other places.
For instance, where does one put information about the account names one uses on various sites, or one's contact information?
Or if one wanted to write monthly updates on the progress one makes on various projects, like [gwern](FIXME) and [Vipul Naik](FIXME).


# Notes on having mine

- I expect to fairly often rename pages when I'm starting out, since I want pages to use [canonical naming]() but sometimes I'm careless or don't know what the standard name of a topic is.
Fixing is cheap, though.
For instance, I recently changed the page "Openness and availability of content" to the much simpler "[Content availability]()".
After the obvious `git mv` and changing of the title in the file itself, I had to look for all the references I made to that page throughout.
This is achieved by:
```{.bash}
egrep -i --color -n "*openness.and.avail*" pages/*
```
The periods are helpful because they catch both the hyphenated links (explicit) or the spaces (used for implicit internal linking).
