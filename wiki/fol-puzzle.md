---
title: FOL puzzle
tags: math
---

*I seem to have written this a long time ago, and it was on one of my
backup drives.  It's not too interesting, and I think Tim Gowers posted
something similar (it may have been the dual of what I describe here) a
while ago.  Still, it's better to put it up here than just have it
locally.  It's somewhat amusing looking back on this, because the
original document was titled "A Little Number Theory" when the actual
point has nothing to do with number theory---a sign of my mathematical
immaturity, I suppose.  I've cleaned up most of the document to reveal
the part that most interested me.*

Consider the following "proof":

> Let $n$ be an integer. Let $A$ be the proposition “$n\ne2$”, $B$ be the
> proposition “$n$ is prime”, and $C$ be the proposition “$n$ is odd”.
> Then $(A\wedge B)\to C$ is true because $2$ is the only even prime. But
> $(A\wedge B)\to C\equiv (A\to C)\vee(B\to C)$. So it must be the case
> that “if $n\ne2$, then $n$ is odd; or, if $n$ is prime, then $n$ is
> odd”. But this last proposition is false because $4\ne2$ but $4$ is not
> odd. Also, $2$ is prime, but $2$ is even. Therefore,
> $(A\wedge B)\to C\not\equiv (A\to C)\vee(B\to C)$.
