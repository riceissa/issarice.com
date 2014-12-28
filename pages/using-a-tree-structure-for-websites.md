---
title: Using a tree structure for websites
#description: none
author: Issa Rice
creation-date: 2014-12-27
last-major-revision-date: 2014-12-27
language: English
# accepts "notes", "draft", "in progress", or "mostly finished"
status: notes
# accepts "certain", "highly likely", "likely", "possible", "unlikely", "highly unlikely", "remote", "impossible", "log", "emotional", or "fiction"
#belief: 
# accepts "CC0", "CC-BY", or "CC-BY-SA"
license: pd
tags: content creation
...

Note
:    This page is part of my series on [Content creation: the organization and dissemination of knowledge]().

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
- How to use Vim with LaTeX ("Vim")
- How to use Emacs with LaTeX ("Emacs")
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

