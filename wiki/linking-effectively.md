---
title: Linking effectively
author: Issa Rice
date: 2016-07-12
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
- email obfuscation in links? (what Pandoc does)
- referrer masking
- when to use footnotes, when to use links, when to use parentheses
- From LW boring advice: "Never post a web link that requires a reader to click on it to find out if they want to click on it."
- including the article. e.g. "\[the job posting\]" is better than "the \[job posting\]" (example from [The process of hiring our first cause-specific Program Officer](http://blog.givewell.org/2015/09/03/the-process-of-hiring-our-first-cause-specific-program-officer/), which uses the version I don't like..)
- semantic web: links with meanings
- Do surrounding quotes count as part of the link?
In other words, should we prefer `["Article Title"]` or `"[Article Title]"`?
An analogue with book titles cannot be made, because both `[*Book Title*]` and `*[Book Title]*` appear the same.
Consider also fragments that include the quoted thing on one end, e.g. `see [my Quora answer to the question "Should I eat?"]`, where excluding the quotes is impossible.
- Wikipedia likes to give full citations as a *way to combat linkrot*.
Indeed, the [argument](https://en.wikipedia.org/wiki/Wikipedia:Citing_sources#Handling_links_in_citations) is that it is easier to find a linkrotted source if there's other information like title of article, author name (someone to contact if the article cannot be found elsewhere), etc.
However, I find inline linking to be more emphatic (it conveys a different message than footnotes or parenthetical citations).
One way to have the best of both worlds is to be [aggressive about archiving](digital-preservation) and to have a mechanism for detecting broken URLs (which you should be doing anyway).

Links often emphasize text on a page (in many browsers links are underlined and colored differently). So consider the sentence “Stopping
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

A general rule is, you should always imagine how a page would look if you
removed all the hyperlinks. So this means using words like “here” for
linking should be discouraged.

---

Pandoc has `-M links-as-notes:true`, but, while this exposes all URLs in the
document, it also messes up the footnote numbering in the sense that an HTML
version will have footnotes that increase more slowly (and there is no
one-to-one correspondence).

If the full citation is only needed so people can locate the material, one
idea might be to include the citation information in the title text of the
URL. In Pandoc markdown this is accomplished by

```markdown
[link text](http://example.com "title text here")
```

One problem is that in PDFs, the title text is lost (though it might be
possible to show them by writing an appropriate Pandoc filter).

Pandoc also provides a full citation filter through `pandoc-citeproc`, but I'm
not sure this is worth it in most cases. Inline linking did *something* right
by making it more intuitive and emphatic to click on things, and it would feel
like returning to an inferior system to go back to academic citations. Of
course, link rot is the major downside of inline links, but there are also
others (like not having access to the full citation, so not being able to
search for something using the citation information).

There is also the issue of including quotes from the destination. In academic
citations (and also on Wikipedia), it's possible to include quotes directly in
footnotes, so that even if the destination disappears, the actually-relevant
piece of information is safe.

See also a [Markdown style guide from Google][google guide]:

> Titling your links as "link" or "here" tells the reader precisely nothing
> when quickly scanning your doc and is a waste of space:
>
>     See the syntax guide for more info: [link](syntax_guide.md).
>     Or, check out the style guide [here](style_guide.md).
>     DO NOT DO THIS.
>
> Instead, write the sentence naturally, then go back and wrap the most
> appropriate phrase with the link:
>
>     See the [syntax guide](syntax_guide.md) for more info.
>     Or, check out the [style guide](style_guide.md).

# See also

- [Durable link]()

[google guide]: https://github.com/google/styleguide/blob/3591b2e540cbcb07423e02d20eee482165776603/docguide/style.md#use-informative-markdown-link-titles
