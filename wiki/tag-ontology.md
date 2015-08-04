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
#belief: possible
# accepts "CC0", "CC-BY", or "CC-BY-SA"
license: CC-BY
tags: untagged
aliases: topic ontology
---

The topic of **tag** or **topic ontology** has always fascinated me

This concerns things like a tagging system.

I think that tags are best implemented using [DAGs](https://en.wikipedia.org/wiki/Directed_acyclic_graph), but I haven't encountered software that actually does this.
WordPress, which has both categories and tags, uses a tree structure for its categories and simply has flat tags ([see here](https://wordpress.org/ideas/topic/allow-child-category-to-have-multiple-parents) for why we want something else).
Other implementations are similar; Hakyll tags are flat, for instance.

Quora uses DAGs for their topic ontology; see [Adam D'Angelo's answer to Are Quora topic hierarchies a directed acyclic graph?](https://www.quora.com/Are-Quora-topic-hierarchies-a-directed-acyclic-graph/answer/Adam-DAngelo):

> **Yes.** The topic parent/child relationships form a DAG. This means that
> there will never be a situation where A is a parent of B, and B is also a
> parent of A (or longer loops). In addition, topics can have multiple parent
> topics and multiple child topics.
