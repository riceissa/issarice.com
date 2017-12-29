---
title: Probability tutorial
author: Issa Rice
date: 2017-12-29
created: 2017-12-29
---

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
