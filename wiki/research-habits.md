---
title: Research habits
author: Issa Rice
date: 2016-06-20
---

# General habits

- Make or add to Wikipedia pages in the course of reading about a topic.
- Frequently Google for information to build understanding of the base rates in the area you're reading about.
- Google the topic with the names of various organizations or movements or ideologies (to build intuition for what various people think about the topic).
    - Similarly, Google the topic along with terms like "criticisms of", "critique", "sucks", "wrong", "bad", etc. to see what opponents think.
    (More generally, there are two ways to build intuition on a topic: to obtain representative data so you understand the base rates, and to collect many (especially extreme) anecdotes so you have a good idea of the space of possibilities of opinion.
    The strategy of this bullet point helps with the latter.)
- Email relevant people for more information if you can't find what you're looking for (and remember to follow up if they don't respond).
- Archive your online sources to combat linkrot.
I use the Scrapbook addon in Firefox (local archive), as well as Pinboard (personal online archive) and Archive.org (public online archive).
- Tabulating information as you come across it will help to make things more explicit, especially by revealing all of the relevant dimensions and exposing the empty cells in the table.
Examples: [Tabular summary of unschooling literature](http://causeprioritization.org/Tabular%20summary%20of%20unschooling%20literature), [User:Issa Rice/Priors for CP](http://causeprioritization.org/User:Issa%20Rice/Priors%20for%20CP), some of the pages on Subwiki.

# Common frustrations

- Copying text from PDFs can be frustrating.
Sometimes using a different PDF viewer helps (e.g. Firefox's PDF viewer followed by Atril/Evince in case of severe formatting issues).
In [Vim]() I also have:

    ```vim
    " filter text pasted from PDFs, so that formatting is suitable; progress
    " ongoing; join must be called at the very end because vim assigns <line1> and
    " <line2> when the command is invoked, so we can't change the boundaries of the
    " line markers; for the same reason, we can't regex replace new lines
    command! -range FilterPDFText silent <line1>,<line2>s/$/ /e | silent <line1>,<line2>s/\-\s\+$//e | silent <line1>,<line2>s/\s\+/ /ge | silent <line1>,<line2>s/^\s\+//e | <line1>,<line2>join!

    nnoremap <leader>q :'{,'}FilterPDFText<CR>:s/\s\+$//e<CR>O<Esc>jo<Esc>kgqip

    ```

    which will do some simple regex replacement to get a decent output in most cases.

- Generating citations for webpages is tedious.
For this reason I wrote a [citation generator for Wikipedia](https://github.com/riceissa/citation-generator), which does something like 80% of the work for 80% of websites.

# External links

- [Carl Shulman's research advice](https://docs.google.com/document/d/1_yuuheVqp1quDfkuRcpoW_HO7jPaI7QnRjF1zl_VovU/edit) (quite coincidentally, [Claire Zabel shared](https://www.facebook.com/claire.zabel/posts/10210316635098601) Carl's advice on the same day I began working on this page)
- [gwern's notes on organizing information](https://www.gwern.net/About#information-organizing)
