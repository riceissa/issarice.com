---
title: Linking effectively
#description: none
author: Issa Rice
creation_date: 2015-01-03
last_major_revision_date: 2015-07-05
language: English
# accepts "notes", "draft", "in progress", or "mostly finished"
status: notes
# accepts "certain", "highly likely", "likely", "possible", "unlikely", "highly unlikely", "remote", "impossible", "log", "emotional", or "fiction"
belief: possible
# accepts "CC0", "CC-BY", or "CC-BY-SA"
license: CC0
tags: writing, content creation
aliases: hyperlink, hyperlinks, hyperlinking effectively, effective linking
---

Some places to look:

- <http://www.catie.ca/sites/default/files/hyperlinking-04.pdf> (seems decent if basic)
- <http://www.digitalbusiness.gov.au/creating-your-website/creating-and-organising-content/using-hyperlinks-effectively/> (see the section near the bottom; seems to be overlap with the first link, but also has new info?)

Things to talk about:

- linking in PDFs versus HTML
- relative vs absolute links
- include examples
- linking in e.g. plaintext email, where *only* exposed links are possible
- URL shorteners?
    - using colon and parentheses effectively. remembering that some
      software won't be able to tell if adjacent punctuation is part of
      the link, so adding spaces that might look awkward accordingly
- long exposed links appear poorly on mobile browsers
- when to use linking style like (1, 2, 3) or (here, here, and here) or (more) (GiveWell does the third.)
- internal vs external links
- email obfuscation in links? (what pandoc does)
- referrer masking
- when to use footnotes, when to use links, when to use parentheses
- From LW boring advice: "Never post a web link that requires a reader to click on it to find out if they want to click on it."
- including the article. e.g. "\[the job posting\]" is better than "the \[job posting\]" (example from [The process of hiring our first cause-specific Program Officer](http://blog.givewell.org/2015/09/03/the-process-of-hiring-our-first-cause-specific-program-officer/), which uses the version I don't like..)
- semantic web: links with meanings

Links often emphasize text on a page. So consider the sentence “Stopping
X shouldn’t be a high priority.” It would be natural to hyperlink this
to something that argues this point like so: “Stopping X [shouldn’t be a
high priority].” This gets the emphasis right. But now what if we wanted
the following nuanced alternative?

“I don’t think stopping X should be a high priority.” Then consider the
straightforward hyperlink translation:

“I don’t think stopping X [should be a high priority].” Ah, but now
someone quickly scanning the article might now accidentally interpret
that stopping X should be a high priority!! Instead we want something
like:

“I [don’t think stopping X should be a high priority].” Or:

“I don’t think stopping X should be a [high priority].”

A general rule is, you should always image how a page would look if you
removed all the hyperlinks. So this means using words like “here” for
linking should be discouraged.
