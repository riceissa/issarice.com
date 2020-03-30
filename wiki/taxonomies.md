---
title: Taxonomies
author: Issa Rice
created: 2018-04-26
date: 2018-04-26
# documentkind:
status: notes
# belief:
---

This page is a linkdump of my readings and thoughts related to taxonomies. I am interested in taxonomies for similar reasons to [timelines](https://timelines.issarice.com/wiki/Main_Page): they are both useful ways to organize information. For the moment taxonomies are just a continual interest (in contrast to timelines, where I have written many already).

The figures in this paper are interesting <http://www.landwehr.org/1994secflawtaxcsurv.pdf>

Some Wikipedia searches:

- <https://en.wikipedia.org/wiki/Special:PrefixIndex/Taxonomy_of>
- <https://en.wikipedia.org/w/index.php?title=Special%3APrefixIndex&prefix=Table+of&namespace=0&hideredirects=1>
- <https://en.wikipedia.org/w/index.php?title=Special%3APrefixIndex&prefix=Anatomy+of&namespace=0&hideredirects=1>

Section 1.4 of *[Ethical Intuitionism](https://en.wikipedia.org/wiki/Ethical_Intuitionism_(book))* by [Michael Huemer](https://en.wikipedia.org/wiki/Michael_Huemer) has two taxonomies of metaethical views (I've replaced the figures with ASCII drawings because I don't want to bother uploading images):

> As the preceding section suggests, metaethical theories are traditionally
> divided first into realist and anti-realist views, and then into two forms of
> realism and three forms of anti-realism:
>
> ```
>            Naturalism
>           /
>    Realism
>   /       \
>  /         Intuitionism
> /
> \
>  \              Subjectivism
>   \            /
>    Anti-Realism -- Non-Cognitivism
>                \
>                 Nihilism
> ```
>
> This is not the most illuminating way of classifying positions. It implies
> that the most fundamental division in metaethics is between realists and
> anti-realists over the question of objectivity. The dispute between
> naturalism and intuitionism is then seen as relatively minor, with the
> naturalists being much closer to the intuitionists than they are, say, to the
> subjectivists. That isn't how I see things. As I see it, the most fundamental
> division in metaethics is between the intuitionists, on the one hand, and
> everyone else, on the other. I would classify the positions as follows:
>
> ```
>    Dualism -- Intuitionism
>   /
>  /                      Subjectivism
> /                      /
> \          Reductionism
>  \        /            \
>   \      /              Naturalism
>    Monism
>          \               Non-Cognitivism
>           \             /
>            Eliminativism
>                         \
>                          Nihilism
> ```

(By the way, Wei Dai also has a [classification of metaethical views](http://lesswrong.com/lw/khf/six_plausible_metaethical_alternatives/), which is a list rather than a tree. Tommy Crow also has a somewhat different [taxonomy](https://www.lesswrong.com/posts/jJsdXwvpKHPcHoCEs/categorization-of-meta-ethical-theories-a-flowchart).)

I think the hard thing about taxonomies is that they're a mess to deal with in terms of markup. Timelines are linear so they are easy to enter using a text editor (or just about any software tool).

Also it's non-obvious how to introduce interactivity (in the way that, say, timelines can easily be sorted by column to obtain different "views"). So taking Huemer's example, I think there should be a way to transform one tree into the other. Taking inspiration from SQL-like databases, we can let each position be a row, and each property be a field (column):

|Position|Realist?|Dualist?|Reductionist?|
|-------------|-----|-----|-----|
|Naturalism|Yes|No|Yes|
|Intuitionism|Yes|Yes|n.a.|
|Subjectivism|No|No|Yes|
|Non-Cognitivism|No|No|No|
|Nihilism|No|No|No|

Now using the above table, the first taxonomy can be created by classifying by
the "Realist" column, and the second taxonomy can be created by classifying by
the "Dualist" column followed by the "Reductionist" column. But now couldn't we
do something like classify by "Reductionist" first followed by "Realist"? We
could, and we end up with the following tree:

```
                Realism -- Naturalism
               /
   Reductionist
  /            \
 /              Anti-Realism -- Subjectivism
/
---Eliminativist -- Non-Cognitivism
\               \
 \               Nihilism
  \
   Intuitionist
```

I'm not sure how useful the above taxonomy is though (I suspect it's not
useful). But this means making a taxonomy requires some sort of mysterious
"taste" factor. How can we tell beforehand which taxonomies will be
enlightening, and which ones will be useless? It would be nice to have some way
of telling this without spending a lot of effort making a bunch of taxonomies.
In contrast, timelines are fairly easy to make because you can just start
adding events in chronological order, and eventually you end up with a useful
tool.

Another example. I've been trying to understand my personal archiving needs. Here's one taxonomy I came up with:

- Original/private work (including work by others that isn't well-archived)
  - Large binary
    - Personal photos, movies, etc.
    - Large website scrapes
    - Browsing cache
  - Small
    - Working drafts
    - Written pieces by friends/people I know e.g. deleted Quora answers
- Mainstream (i.e. I can re-download even if I lose it)
  - Large binary
    - Mainstream music
    - Mainstream movies
  - Small
    - Journal articles, ebooks, etc.

but maybe it's not the best (evidenced by my feeling fuzzy about this and not quite grokking it)

Another example. Wikipedia has a lot of templates at the bottom of pages, and one topical template is <https://en.wikipedia.org/wiki/Template:Cryptocurrencies>. So this is a "taxonomy" (single-layered) that's based on the underlying verification mechanism. But each currency has more information it could be categorized under (market cap, whether there's a ceiling amount, built-in anonymity, etc.)

From ["This Transhumanist Records Everything Around Him So His Mind Will Live Forever"](https://motherboard.vice.com/en_us/article/4xangw/this-transhumanist-records-everything-around-him-so-his-mind-will-live-forever), an article about Alexey Turchin (who happens to be active in EA/R):

> Since, according to Turchin, fewer and fewer people want to spend time
> reading books, he lays out his arguments in sprawling "concept maps," a type
> of flowchart which are often further developed into other sub-maps, in an
> eternal branching-out.

(not really a taxonomy, but it's interesting how certain people fixate on certain output formats)

Vipul has pointed me to [Airtable](https://en.wikipedia.org/wiki/Airtable), which is like a cross between databases and spreadsheets. Again, not exactly a taxonomy but interesting.

<https://bartoc.org/en>

Example entry: <https://bartoc.org/en/node/527>

Wikipedia page: <https://en.wikipedia.org/wiki/BARTOC>

<https://en.wikipedia.org/wiki/Category:Equivalence_classes>

# See also

- [Tabular presentation]()
