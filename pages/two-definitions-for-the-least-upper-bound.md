---
layout: default
title: Two definitions for the least upper bound
math: "yes"
comments: "yes"
disqus-id: 1596b07fb543d452926cdbe2d4ecc483edcb1c81
tags: math
---

The definition for the least upper bound seems to be given in two nearly identical ways, and I wanted to show that these definitions are, in fact, equivalent, so here is a little note.

Consider the following three statements regarding some set of real numbers `\(X\)`, and real numbers `\(M,N\in \mathbf{R}\)`.

1. `\(M \geq x\)` for all `\(x\in X\)`.
2. Let `\(N\geq x\)` for all `\(x\in X\)`; then `\(M\leq N\)`.
3. Let `\(N<M\)`; then there is some `\(x\in X\)` such that `\(x>N\)`.

My impression is that most books use (1) and (2) above to define `\(M=\sup X\)` as the least upper bound of `\(X\)`.
(To me, at least, this seems most intuitive, since we actually “see” that out of all the upper bounds of `\(X\)`, `\(M\)` is indeed the least.)
However, some books e.g. Ross in *Elementary Analysis* (p 21; it’s actually not part of the real definition, but (1) and (3) are the only “formal” parts given) seem to use (1) and (3) instead.

Our task, then, is to show that

- (1) and (2) together imply (3), and that
- (1) and (3) together imply (2).

*Proof*.
To show the first implication, suppose (1) and (2) are true.
We want to show (3).
Let `\(N<M\)`.
We need to find `\(x\in X\)` such that `\(x>N\)`.
Suppose for the sake of contradiction that such `\(x\)` does not exist, i.e., for all `\(x\in X\)` we have `\(x\leq N\)`.
Then by (2) we have `\(M\leq N\)`.
But `\(N<M\)`, which is a contradiction.

Now suppose (1) and (3) are true; we would like to show (2).
Let `\(N\geq x\)` for all `\(x\in X\)`.
We now need `\(M\leq N\)`.
Suppose for the sake of contradiction that `\(M\not\leq N\)`, i.e., `\(M>N\)`.
Then, by (3), there is some `\(x\in X\)` such that `\(x>N\)`.
This contradicts the above, where `\(N\)` was an upper bound for `\(X\)`. `\(\square\)`
