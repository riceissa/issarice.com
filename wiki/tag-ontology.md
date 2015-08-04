---
title: Tag ontology
#description: 
#feed_description: 
author: Issa Rice
creation_date: 2015-08-04
last_major_revision_date: 2015-08-04
language: English
# Possible values are "notes", "draft", "in progress", and
# "mostly finished"
status: notes
# Possible values are "certain", "highly likely", "likely", "possible",
# "unlikely", "highly unlikely", "remote", "impossible", "fiction", and
# "emotional"
belief: possible
# accepts "CC0", "CC-BY", or "CC-BY-SA"
license: CC-BY
tags: content creation
aliases: topic ontology
math: yes
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
