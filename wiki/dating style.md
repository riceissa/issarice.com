---
title: Dating style
date: 2016-06-22
author: Issa Rice
---

- I asked [What does dcterms\.date denote?](http://stackoverflow.com/questions/37981652/what-does-dcterms-date-denote) on Stack Overflow.
- [Dublin Core](!w) [defines](http://dublincore.org/documents/dcmi-terms/) several dating mechanisms, including the date when a resource became available, when it was created, when it was accepted, when it was submitted, when it was issued, and when it was modified.
There is also the mysterious (see above question) bare "date" field.
- By default, Pandoc uses the `date` or `date-meta` YAML fields -- but what are these the dates of?
- For blogs, a "date" could probably just mean the date a post was first published.
But what about for a site like this one or gwern's?
Here the creation date is not very useful, since all it tells you is when the author first came up with the idea to write the page -- something that would be more appropriately placed in a "History" or "Changelog" section on the page.
Nor is the date of the latest edit very useful -- what if the latest edit just fixed a typo but added nothing substantive?
For this reason, I like borrowing the idea of [versioning](https://en.wikipedia.org/wiki/Software_versioning) from software: in addition to releasing [all of the commits](https://github.com/riceissa/issarice.com), I can make the "date" be of some sort of milestone for the page.
In practice I call this the "last substantive revision date".
- Even with "last substantive revision date", there is a problem, because the substantive revision might have been in a single part of the page, so that most of the page is still quite old.
Of course, there are things like [git blame](https://git-scm.com/docs/git-blame) that can tell you the last modification date of every single sentence (since each line in the source Markdown files on this site is a sentence), but is there an easier way to convey this sort of information to readers?
(Of course, we don't require of software that every part of it is up-to-date!)

# See also

* [[Versioning prose]]
