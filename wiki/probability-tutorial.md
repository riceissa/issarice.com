---
title: Probability tutorial
author: Issa Rice
date: 2017-12-29
created: 2017-12-29
---

Some motivation: I think probability and statistics are often confusing because the ontology of things like "random variable" and "distribution" are unclear/mysterious. Is a random variable really "random" or is it just a deterministic mathematical object (like everything else in math we like to work with)? Ever since starting to learn [Haskell](my-haskell-learning), I've been obsessed with asking what type a certain object has.

On notation: by $A \to B$ we mean the set of functions mapping some set $A$ to another set $B$. This is sometimes written $B^A$, because $|A\to B| = |B|^{|A|}$. And $f : A \to B$ is a "type annotation" and means $f$ is a function mapping $A$ to $B$. But combining these, we could also have written $f \in (A\to B)$, just like we write $x\in X$ to mean $x$ is in some set $X$. Using this notation we can say things like $(A \to B) \subset (A\times B)$.

The following questions should be converted to multiple choice questions.

When we write $X = x$, what is the type of $=$?

Answer: $(=) : (\Omega \to \mathbf R) \times \mathbf R \to \mathcal P (\Omega)$. Notice that $(=)$ is a binary function that does not return a boolean. This is no ordinary equals sign! By the way, what *is* the type of an ordinary equals sign?

Answer: $(=): A \times A \to \{\text{True}, \text{False}\}$, where $A$ can be any set.

When we write $\Pr (X = x)$, what is the type of $=$?

Answer: $(=) : (\Omega \to \mathbf R) \times \mathbf R \to \mathcal P(\Omega)$. Note that here the result feeds into $\Pr$, but that doesn't change the type of $(=)$.

If we take $X$ and $x$ as inputs to $f(X,x) = \Pr(X=x)$, what is the type of the function $f$ that produces this output?

Answer: The output is in $\mathbf R$ so we just have

$$f : (\Omega\to\mathbf R) \times \mathbf R \to \mathbf R$$

When we write $\Pr (X \leq x)$, what is the type of $\leq$?

Answer: $(\leq) : (\Omega \to \mathbf R) \times \mathbf{R} \to \mathbf R$.

What is the type of a Bernoulli distribution? First of all, it takes a real parameter between 0 and 1, so it's of the form $\mathrm{Bernoulli} : [0,1] \to A$ for some set $A$. What is $A$?

What is the type of a random variable $X$ with a Bernoulli distribution taking parameter $p$ (often written $X \sim \mathrm{Bernoulli}(p)$)? In particular, what is the sample space (since we already know $X : \Omega \to \mathbf R$ for some $\Omega$ just because $X$ is a random variable)?

Some books write $\Pr(\omega)$ (implying $\Pr_\Omega : \Omega \to \mathbf R$) while others write $\Pr(\{\omega\})$ (implying $\Pr_\Omega : \mathcal P(\Omega) \to \mathbf R$).

Another problem is the distinction between the probability density function $f_X(x)$ vs writing $\Pr(X=x)$. Wasserman discusses this a bit in _All of Statistics_, but I haven't seen other books talk about this.

Some books define expectation like

$$\mathrm E(X) = \sum_{\omega\in\Omega}(X(\omega) \Pr({\omega}))$$

while others define it like

$$\mathrm E(X) = \sum_{x\in\mathbf R} xp(x)$$

i.e. summing over the domain vs summing over the range. How do show the equivalence of these two definitions?

Some books define expectation as a sum/integral over the values a random variable takes, while others define it as a sum/integral over the sample space, but no book that I have seen connects these two definitions. The only thing I have seen here is <https://math.stackexchange.com/questions/1352884/equivalent-definitions-for-expected-value-of-random-variable>. To me, this feels like a basic pedagogic oversight in all the books that I've seen. Are these two definitions so obviously equivalent that one need not spend even a sentence connecting them?
