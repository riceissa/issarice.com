---
layout: default
title: Zip in Python
comments: "yes"
math: "yes"
license: "CC-BY"
tags: math, python, computer-science
---

In mathematics, one can have a function $f: X \times Y\to Z$ and write
$f(x,y) = z$, where $x\in X, y\in Y, z\in Z$. Some books take care to
remark that since $X \times Y$ is the domain $(x,y)\in X\times Y$, one
should in fact write $f((x,y))=z$. In Python, this distinction is
accomplished using the star (`*`) in function calls.  So for example if
one had a sequence of parameters $(a_i)_{i=0}^n$, then one can write
$$
f(\star(a_i)_{i=n_0}^n) = f(a_{n_0}, \ldots, a_n)
$$

Now, the function `zip` in Python takes the $i$th element from each
iterable in some sequence, and forms a tuple for each $i$, then
places all these tuples in one final list.  Suppose we are given some
sequence $x = ((x_{i,j})_{j={m_0}}^m)_{i={n_0}}^n$. Incidentally,
this sequence can be visualized as a matrix-like structure like

$$
\begin{pmatrix}
(x_{n_0,m_0}, \ldots, x_{n_0,m}) \\
\vdots \\
(x_{n,m_0}, \ldots, x_{n,m})
\end{pmatrix}
$$

Now let us examine what $\mathrm{zip}(\star x)$ means.  The star
unpacks the first layer of the sequence, leaving us with
$\mathrm{zip}((x_{n_0,m_0}, \ldots, x_{n_0,m}), \ldots, (x_{n,m_0},
\ldots, x_{n,m}))$.  Now, $\mathrm{zip}$ will first take the
$m_0$ element from each sequence in the argument, forming the
sequence $(x_{n_0,m_0},\ldots,x_{n,m_0})$; this process continues
until we reach the sequence $(x_{n_0,m},\ldots,x_{n,m})$.  Finally,
$\mathrm{zip}$ will place everything in a sequence of its own, and
we obtain a matrix-like structure as follows.
$$
\begin{pmatrix}
(x_{n_0,m_0},\ldots,x_{n,m_0}) \\
\vdots \\
(x_{n_0,m},\ldots,x_{n,m})
\end{pmatrix}
$$
In other words, everything that was horizontal is now vertical, and the
converse holds as well. If we decide to repeat this operation, we get
the original matrix-like structure back.  In other words, $x =
\mathrm{zip}(\star\mathrm{zip}(\star x))$.

To give an example of this identity in Python:

``` python
>>> x = (1, 2, 3)
>>> y = (4, 5, 6)
>>> lst = [x, y]
>>> lst == zip(*zip(*lst))
True
```
