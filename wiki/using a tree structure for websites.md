---
title: Using a tree structure for websites
author: Issa Rice
created: 2014-12-27
date: 2014-12-27
status: notes
---

Note
:    This page is part of my series on [[Content creation: the organization and dissemination of knowledge]].

A website may be thought of as having a rooted [tree structure](http://en.wikipedia.org/wiki/Tree_%28graph_theory%29); we look at this concept more closely here.

Vipul Naik considers two questions

1. How specific should the individual leaf node pages be?
In other words, at the bottommost places of the tree, how much content should be in those pages?

2. For a particular choice of leaves, how should we trade off the breadth versus depth of the tree?
In other words, how many intermediate levels should the tree have?

To understand the two questions better, consider the following pages that might be on a website:

- How to use the `proof` environment  in LaTeX (called "proof" below)
- How to configure the `thmtools` package on LaTeX ("thmtools")
- A list of math symbols in LaTeX ("symbols")
- How to use [[Vim]] with LaTeX ("Vim")
- How to use [[Emacs]] with LaTeX ("Emacs")
- How to typeset a Japanese LaTeX document ("Japanese")
- How to typeset a Spanish LaTeX document ("Spanish")
- How to mix languages in LaTeX ("mix")

Question (1) asks whether all of these deserve a page: is it better to have a single comprehensive page (at one extreme) or be as modular as possible (at the other extreme)?
Between these extremes, we could combine just some pages; for instance, "proof" and "thmtools" could be combined into a "math packages" page.

For question (2), *given that* each of the above deserve a page, we want to know how to organize the list as a tree.
At one extreme, we could just have a "How to use LaTeX" container-page that links to all of the above pages.
This would be pushing *breadth* to the maximum, and would look like the following (any page with brackets around them are container-pages that link to the actual leaves.):

```
    [       How         to        use        LaTeX       ]
    /      /         /     |     |      \         \      \
proof  thmtools  symbols  Vim  Emacs  Japanese  Spanish  mix
```

On the other hand, we can have intermediate pages like "Math and LaTeX", "Editing LaTeX", and "LaTeX and languages" all under "How to use LaTeX", and then have the relevant pages linked under the intermediate pages.
This has more depth than the first example, and looks like:

```
            [     How     to    use    LaTeX    ]
            /                |                  \
    [Math and LaTeX]   [Editing LaTeX] [LaTeX and languages]
    /      |       \       |     |       /         |      \
proof  thmtools  symbols  Vim  Emacs  Japanese  Spanish  mix
```

At the other extreme (i.e. the most depth), we can make a "math packages" container-page that creates a new level and have something like:

````
                    [How   to   use   LaTeX]
                    /         |            \
     [Math and LaTeX]     [Editing LaTeX]  [LaTeX and languages]
      /           \           |      \         |        |     \
 [Math packages]  symbols    Vim    Emacs   Japanese Spanish mix
  /        \
proof  thmtools
````

Some points:

- Most users will not care about the tree structure of a page or set of related pages.
See [Trees, TreeViews, and UI](http://blog.codinghorror.com/trees-treeviews-and-ui/) for more on this.
If a page has many levels of sections (e.g. chapter, section, subsection, subsubsection, etc.), it becomes very difficult to process where in that tree one is.
- Besides search, the primary way in which content is now discovered is through sharing on social media.
I think it's good practice to make one's content [linkable](linkability), which means that each page should be a [[good entry point]] and be easy to process.

See also [a comment by Viliam_Bur](http://lesswrong.com/lw/k8q/moving_on_from_cognito_mentoring/ax6q) on [[LessWrong]], talking about the [Cognito Mentoring wiki](http://info.cognitomentoring.org/wiki/Main_Page):


> Seems to me that your current wiki structure uses too much
> introductions, too much redirection. For example: On the main page, you
> have a link to "What we offer and why". Why not put that into the main
> page? The page "What we offer and why" contains a link to "Learning
> portal"; the page "Learning portal" contains a link to "Our category on
> the benefits of learning particular subjects" (and also directly to
> math, algebra and economics; this part well-done!), and the page
> "Category:Subject learning benefits" contains a link to e.g. "Chemistry
> learning benefits". And the "Chemistry learning benefits" contains a
> text "We're still working on this page, so check back later!" (and a
> hyperlink to a useful topic). -- Uhm, seriously? It takes *four* clicks
> to discover the page about to chemistry, only to learn that you have
> almost nothing about chemistry?
> 
> On the other hand, I guess I understand how this all happened. This is a
> "top down" approach: you create a huge abstract structure where you want
> to fill the details later. This feels very high-status. But it's
> optimized for how you feel about it, not for the convenience of the
> reader. -- I suggest the opposite, "bottom up" approach. You have the
> valuable pieces of information (for example the external link to quora
> article about learning chemistry). That's the value you provide, and you
> want to navigate the reader there as easily as possible. So you build
> the navigation pages around the content you already have, not around the
> content you wish you had.
> 
> For example, one external hyperlink is not enough to make a separate
> page about chemistry. You probably have more such links for other
> subjects, so it makes sense to create a page "Advice about specific
> subjects", divide it to subjects by headers and subheaders, and put the
> links there. (In future, when you have more than 10 chemistry-related
> links, or perhaps if you have 5 chemistry-related links but you also
> provide a short summary below the link, *then* it's the right time to
> create a separate "Advice about Chemistry" page.) And your *main page*
> should link directly to the "Advice about specific subjects" page,
> because that's one of the main things you provide. There: Just two
> clicks, and the reader is reading the Quora article. There is the same
> information there as before, it's just easier to find.

# See also

- [Google's War on Hierarchy, and the Death of Hierarchical Folders](https://web.archive.org/web/20060106062021/http://www.microcontentnews.com/articles/deathofhierarchy.htm)
