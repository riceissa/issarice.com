---
title: Single source publishing
author: Issa Rice
created: 2015-01-01
date: 2015-01-01
status: notes
belief: possible
---

As part of this website, but also with publishing information in general (e.g. with my school projects, for instance), I've been very interested in things like [[digital preservation]], [durable links](durable-link), and [single source publishing](!w) (SSP).

Some thoughts:

- One approach is to write in a language whose set of features is the *intersection* of all the sets of features of output formats one is considering.
This way, for each thing one writes, there will be an equivalent in each of the output formats.
See for instance "[Why markdown, not $\mathrm{\LaTeX}$?](https://www.peterkrautzberger.org/0070/)":

    > When I started writing on the web, I began employing simpler and
    > simpler tools for writing mathematics. At first, because there was
    > no other way (presenting mathematics online before MathJax was
    > very hard) and after a while because writing is hard. Damn hard.
    > And any technical distraction seemd unwarranted.
    > 
    > The minimal style forced upon you by a tool like markdown makes
    > one thing crystal clear: nothing will save you when you write
    > badly. No fancy diagrams, no clever equation numbering, no
    > colorful plots.
    > 
    > I believe this reduction has helped me become a better writer,
    > mathematical and otherwise. When there’s your word and your word
    > alone to convey a mathematical idea, a line of thought, a delicate
    > proof, you will find the core of your mathematical writing talent,
    > the true heart of how you write your mathematics well.

    See also "[We need less powerful languages](http://lukeplant.me.uk/blog/posts/less-powerful-languages/)" by Luke Plant.

- Another approach is to take the *union* of the same sets of features.
This way, one has in a sense a "super language" that can deal with a lot more stuff.

Actually the distinction above seems to have been discussed many years ago in "[The Rule of Least Power](http://www.w3.org/2001/tag/doc/leastPower-2006-02-23.html)"!
It even declares:

> *Good Practice:* Use the least powerful language suitable for expressing
information, constraints or programs on the World Wide Web.

I think the people on cat-v would agree(?), and would probably go even further.

Some promising tools:

- Pandoc (used for this site)
- [Madoko](https://www.madoko.net/)
