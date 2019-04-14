My solution for #12:

::: spoiler
Suppose for the sake of contradiction that such a formula $\phi$ exists. By the diagonal lemma applied to $\neg \phi$, there is some sentence $\psi$ such that, provably, $\neg\phi(\ulcorner \psi\urcorner) \leftrightarrow \psi$. By the soundness of our theory, in fact $\neg\phi(\ulcorner \psi\urcorner) \leftrightarrow \psi$. But by the property for $\phi$ we also have $\phi(\ulcorner \psi\urcorner) \leftrightarrow \psi$, which means $\neg\phi(\ulcorner \psi\urcorner) \leftrightarrow \phi(\ulcorner \psi\urcorner)$, a contradiction.

This seems to be the "semantic" version of the theorem, where the property for $\phi$ is stated outside the system. There is also a "syntactic" version where the property for $\phi$ is stated within the system.
:::
