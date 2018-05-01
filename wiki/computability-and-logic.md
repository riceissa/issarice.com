---
title: Computability and Logic
created: 2018-04-30
date: 2018-04-30
status: notes
---

This page contains scribbles and random musings as I process the contents of *Computability and Logic*. It's not really for public consumption (unless you happen to care about my specific confusions).

Something that bugs me is that there is a classification of (partial) recursive(ly enumerable) sets, functions, etc. but textbooks seem to only state *some* of these results, rather than presenting a table with *all* the results visible at once.

Let $f : \mathbf N \to \mathbf N$ be a partial or total function.
If the {domain / range} of $f$ is {recursively enumerable / enumerable in increasing order} then $f$ is \_\_\_\_.

Let $A \subset \mathbf N$ be a {recursive / recursively enumerable / recursively enumerable in increasing order} set. Then $A$ can be the {domain / range} of a {recursive / partial recursive / primitive recursive} function.

Also there are multiple ways to pass between functions and sets here.

- One way to go from a set to a function is to take the characteristic function of the set.
- Another way to go from a set to a function is to make a function enumerate (possibly in increasing order) the set.
- Another way to go from a set to a function is to make the set the domain or range.
- Given a (partial) function, we can take the domain or range to get a set.
- We can define some relation, then quantify over some subset of the variables until we get a dimension we want, then define a set using that relation.
- Set theoretically, a function *is* a set. But I don't think you can say anything interesting about the set that the function happens to be.
