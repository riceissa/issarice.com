Comment made at <https://www.greaterwrong.com/posts/FZkLa3GRLW97fpknG/diagonalization-fixed-point-exercises/comment/MSLkNSawi2etXWYnJ>


Attempted solution and some thoughts on #9:

:::spoiler

Define a formula $\xi(v)$ taking one free variable such that $\xi(\ulcorner \theta \urcorner) \leftrightarrow f(\phi, f(\theta,\theta))$.

Now define $\psi$ as $\xi(\ulcorner\xi\urcorner)$. By the definition of $f$ we have $\psi \leftrightarrow f(\xi,\xi)$.

We have $$\phi(\ulcorner\psi\urcorner) \leftrightarrow f(\phi,\psi) \leftrightarrow f(\phi, f(\xi,\xi)) \leftrightarrow \xi(\ulcorner \xi\urcorner) \leftrightarrow \psi$$

(The first step follows by the defini)

Things I'm not sure about:

* I don't think we can assume that the formula $\xi$ exists without doing more work or assuming more about $f$ than is given in the problem statement. In the presentations of Gödel incompleteness that I have seen, the equivalent of $f$ takes Gödel numbers of formulas rather than the formulas themselves.
* The assumption about the quantifier complexity of $S_0$ and $S_1$ was barely used. It was just given to us in the type signature for $f$, and the same proof would have worked without this assumption, so I am confused about why the problem includes this assumption.

:::
