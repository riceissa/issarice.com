Showing continuous function on a closed interval is bounded via uniform continuity?


In _Analysis I_, Tao writes:

> **Remark 9.9.17.** One should compare Lemma 9.6.3, Proposition 9.9.15, and Theorem 9.9.16 with each other. No two of these results imply the third, but they are all consistent with each other.

For reference, here are the three results:

> **Lemma 9.6.3.** Let $a < b$ be real numbers, and let $f : [a,b] \to \mathbf R$ be a function continuous on $[a,b]$. Then $f$ is a bounded function.

<!-- -->

> **Proposition 9.9.15.** Let $X$ be a subset of $\mathbf R$, and let $f : X \to \mathbf R$ be a uniformly continuous function. Suppose that $E$ is a bounded subset of $X$. Then $f(E)$ is also bounded.

<!-- -->

> **Theorem 9.9.16.** Let $a < b$ be real numbers, and let $f : [a,b] \to \mathbf R$ be a function which is continuous on $[a,b]$. Then $f$ is also uniformly continuous.

I am confused as to why Proposition 9.9.15 and Theorem 9.9.16 don't imply Lemma 9.6.3. The reasoning goes like this: let $f : [a,b] \to \mathbf R$ be continuous on $[a,b]$. Then by Theorem 9.9.16, $f$ is uniformly continuous. Since $f$ is uniformly continuous and $[a,b] \subset \mathbf R$ is bounded, by Proposition 9.9.15 $f([a,b])$ is bounded. But this means $f$ is bounded, so we have Lemma 9.6.3.

What is wrong with the reasoning above? Alternatively, is the remark wrong?
