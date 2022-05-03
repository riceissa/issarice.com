---
title: Tag ontology
author: Issa Rice
created: 2015-08-04
date: 2015-08-04
status: notes
belief: possible
---

The topic of **tag** or **topic ontology** has always fascinated me

This concerns things like a tagging system.

I think that tags are best implemented using [DAGs](https://en.wikipedia.org/wiki/Directed_acyclic_graph), but I haven't encountered software that actually does this.
WordPress, which has both categories and tags, uses a tree structure for its categories and simply has flat tags ([see here](https://wordpress.org/ideas/topic/allow-child-category-to-have-multiple-parents) for why we want something else).
Other implementations are similar; Hakyll tags are flat, for instance.

My goal essentially is to implement "human-friendly" tagging.
Features of "human-friendly" tagging should have:

An alias system
:   I want to use "University of Washington" as a full tag name, but I should be able to just type "UW" or "uw" if I want, for example.

Parent/child relationships
:   If I tag something with "Python" the tagging system should know that this page is related to Python, so it's about programming as well, and tag it accordingly with "programming", for example.

The important consideration with tag implication is the following: if I tag a post with tag $A$, would I, in every case, have tagged it also with $B$?
If so, then $A\to B$, so $B$ should be a parent of $A$.
Note that *this idea of implication is distinct from a category system*.
In a category system, we might have "mathematician" be a parent of "Halmos", for instance.
But it doesn't follow that if a post is tagged "Halmos" it should also be tagged "mathematician"; a post explaining an exercise from one of Halmos's books should be tagged "Halmos" but should not be tagged "mathematician"---it has nothing to do with mathematicians!

In other words, the crucial consideration is: Can we produce a post that is tagged $A$ that should *not* be tagged $B$?
If "yes", then $A \not\to B$.

Another wording: if someone were to look at the tags page for $B$, would they be pleased to find *every single page* from $A$ included?

Quora uses DAGs for their topic ontology; see [Adam D'Angelo's answer to Are Quora topic hierarchies a directed acyclic graph?](https://www.quora.com/Are-Quora-topic-hierarchies-a-directed-acyclic-graph/answer/Adam-DAngelo):

> **Yes.** The topic parent/child relationships form a DAG. This means that
> there will never be a situation where A is a parent of B, and B is also a
> parent of A (or longer loops). In addition, topics can have multiple parent
> topics and multiple child topics.

I don't really agree with Quora's ontology system though, or at least I don't think it's suited to this blog

For instance look at the [organization page on David Hume](https://www.quora.com/David-Hume/organize).
The topic has parents:

- Economists
- Essayists
- Historians
- Philosophers

Moreover it says "A parent topic is a more general topic that fully includes everything in this topic. For example, Food would be a parent topic of French Food."
But is [What is the significance of Hume's inductive reasoning?](https://www.quora.com/What-is-the-significance-of-Humes-inductive-reasoning) a question that should be in the topic (to take the closest topic) "Philosophers"?
I think not.

see also [Trees, TreeViews, and UI](http://blog.codinghorror.com/trees-treeviews-and-ui/), [Google's War on Hierarchy, and the Death of Hierarchical Folders](https://web.archive.org/web/20060106062021/http://www.microcontentnews.com/articles/deathofhierarchy.htm)

with my tag ontology: *for the end-user*, it's as simple as Gmail's tagging system; there is no hierarchy.
Really, it's just *a shorthand for manually tagging something with multiple tags*; the system just understands what other tags you *would have applied*.

also tagging should be better than mere search. if one could generate the same list of pages merely by searching for a keyword, why take the time to tag everything?
e.g. tagging all articles that mention GiveWell with "GiveWell" isn't very helpful, since I can just search for "GiveWell".

There is also the problem of trust, which appears in both search and in tagging.
Basically, if a user can't trust that the information they want can be found using a particular method of content discovery, then they will stop using that (e.g. if a site-native search tool can't find any information, then users will start using Google with "site:"; if the site maintainer is lazy and doesn't tag pages systematically, then users will start to distrust it, preferring search instead).
