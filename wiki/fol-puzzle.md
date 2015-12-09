---
title: FOL puzzle
math: yes
---

*I seem to have written this a long time ago, and it was on one of my
backup drives.  It's not too interesting, and I think Tim Gowers posted
something similar (it may have been the dual of what I describe here) a
while ago.  Still, it's better to put it up here than just have it
locally.*

Definitions
===========

\[Iff\] For concision, we abbreviate “if and only if” by “iff”, as is
standard.

\[Natural number\]The are the counting numbers $0,1,2,3,\ldots$ . The
set of all natural numbers is denoted $\mathbf{N}$.

\[\]Since some authors do not consider $0$ to be a natural number, to
avoid ambiguity, we sometimes call the natural numbers . The set of all
natural numbers is sometimes also denoted $\mathbb{N}$.

\[Integer\]The are the numbers
$\ldots, -3, -2, -1, 0, 1, 2, 3, \ldots$ .

\[Assumptions\]We assume the reader is familiar with the integers. In
particular, we assume addition and multiplication on the integers. We
also assume the reader is familiar with concepts such as and . The
trichotomy of integers (i.e., that for each integer exactly one of the
following conditions holds: (1) the integer is positive, (2) the integer
is negative, (3) the integer is zero) is assumed. The curious reader
should see Terence Tao’s *Analysis I*. Ordering the integers is less
intuitive so we will provide the relevant definitions.

\[Ordering the integers\]Let $a,b$ be integers. Then we say and write
$a\leq b$ iff there is some natural number $c$ such that $b=c+a$. If
$a\leq b$, we also say and write $b\geq a$.

\[\]If $n$ is an integer, $n$ is positive iff $1\leq n$.

Left as an exercise; a formal proof is unnecessary.

\[Divisibility\] Let $d,n$ be integers. We then say and write $d\mid n$
iff there exists an integer $c$ such that $n=cd$. Here $d$ is called a
of $n$. If $d$ does not divide $n$, we write $d\nmid n$.

Properties of divisibility
==========================

We now prove several properties of divisibility.

\[Divisibility is reflexive\] If $n$ is an integer, then $n\mid n$.

Let $n$ be an integer. We need an integer $c$ such that $n=cn$. So let
$c=1$. Since $n=1n$, we are done.

\[Divisibility is transitive\] Let $d,m,n$ be integers. If $d\mid m$ and
$m\mid n$, then $d\mid n$.

Let $d,m,n$ be integers. Since $d\mid m$, there is some integer $a$ such
that $m=ad$. Also, since $m\mid n$, there is some integer $b$ such that
$n=bm$. We need to show $d\mid n$; i.e., we need to find an integer $c$
such that $n=cd$. But $n=bm=b(ad)=(ba)d$. So by setting $c=ba$, we are
done.

\[Multiplication property\] Let $c,d,n$ be integers. If $d\mid n$, then
$cd\mid cn$.

Let $c,d,n$ be integers. Since $d\mid n$, there is some integer $a$ such
that $n=ad$. We need to show $cd\mid cn$; i.e., we need some integer $b$
such that $cn=b(cd)$. But $cn=c(ad)=a(cd)$, so by setting $b=a$ we are
done.

We also have something similar in the other direction:

\[Cancellation\] Let $a,d,n$ be integers. If $ad\mid an$ and $a\ne0$,
then $d\mid n$.

Let $a,d,n$ be integers. Since $ad\mid an$, there is some integer $c$
such that $an=c(ad)$. Since $a\ne0$, we can divide both sides of this
equation by $a$ to get $n=cd$. So $d$ divides $n$, as desired.

\[One divides every integer\] Let $n$ be an integer. Then $1\mid n$.

Let $n$ be an integer. Since $n=n1$, we are done.

\[Every integer divides zero\] Let $n$ be an integer. Then $n\mid0$.

Let $n$ be an integer. Since $0=0n$, we are done.

\[Zero divides only zero\] Let $n$ be an integer. If $0\mid n$, then
$n=0$.

Let $n$ be an integer. Since $0\mid n$, there is some integer $c$ such
that $n=c0$. But $c0=0$ so $n=0$.

\[Linearity property\] Let $a,b,d,m,n$ be integers. If $d\mid m$ and
$d\mid n$, then $d\mid(am+bn)$.

Let $a,b,d,m,n$ be integers. Since $d\mid m$ and $d\mid n$, we have
$m=jd$ and $n=kd$ for some integers $j,k$. But $am+bn=ajd+bkd=(aj+bk)d$,
so we are done.

\[\]Let $a,b$ be integers. If $a>1$ and $b>0$, then $ab>1$.

\[\]Let $a,b$ be integers. If $ab=1$, then $a,b=1$ or $a,b=-1$.

\[Only one or negative one divides one\] Let $n$ be an integer. If
$n\mid1$, then $n=1$ or $n=-1$.

\[\] If $d\mid n$ and $n\ne0$, then $|d|\le|n|$ (comparison property);

\[\] If $d$ and $n$ are positive and $d\mid n$, then $d\le n$
(alternative formulation of the comparison property);

\[\] Let $a,b$ be integers. If $a\mid b$ and $b\mid a$, then $|a|=|b|$.

Let $a,b$ be integers. Since $a\mid b$, there is some integer $c$ such
that $b=ca$. In the same way, $a=db$ for some integer $d$. $a=d(ca)$
$1=dc$

\[\] Let $d,n$ be integers. If $d\mid n$ and $d\ne0$, then
$(n/d)\mid n$.

Let $d,n$ be integers. We need to show there is some integer $k$ such
that $n=k(n/d)$ Since $d\ne0$, $n/d$ is an integer. Let $k=d$. Then
$d(n/d)=n$ so we are done.

Prime numbers
=============

Recall the definition of a prime number:

\[Prime number\]\[prime\] Let $p$ be an integer. Then $p$ is a iff $p>1$
and the only positive divisors of $p$ are $1$ and $p$.

Let us prove that an alternative definition for the primes is equivalent
to the one given.

The following is an equivalent definition for the prime numbers.

> Let $p$ be an integer. Then $p$ is a iff $p>1$ and there are no
> integers $a>1$ and $b>1$ such that $p=ab$.

In other words, an integer $p$ is prime in the sense of \[prime\] iff it
is prime in the sense of the above definition.

First we show that the original definition implies the alternative
definition. Let $p$ be an integer. To state the argument clearly, let

-   $A$ be the proposition “$p>1$”;

-   $B$ be the proposition “the only positive divisors of $p$ are $1$
    and $p$”; and

-   $C$ be the proposition “there are no integers $a>1$ and $b>1$ such
    that $p=ab$”.

\[Since we are using the letter “$p$” to denote an integer, we use the
letters “$A,B,C\ldots$” for propositions instead of “$p,q,r,\ldots$” to
avoid confusion.\]

To show that the first definition implies the alternative definition, we
must show $$(A\text{ and }B)\to(A\text{ and }C).$$ Note, however, that
this is the same thing as proving $$(A\text{ and }B)\to C.$$ Note
further that this is equivalent to $A\to(B\to C)$, which is equivalent
to $A\to(\neg C\to\neg B)$; it is this final proposition that we will
prove.

Suppose $p>1$. Furthermore suppose there exist integers $a>1$ and $b>1$
such that $p=ab$. We want to show $\neg B$, which is equivalent to
showing that there exists a positive integer $c$ such that $c\mid p$ but
$c\ne p$ and $c\ne 1$. We note that $a>1$ and $a\mid p$, so $a$ is a
positive divisor of $p$. Since $a>1$, we also have $a\ne1$; thus we need
only show $a\ne p$. Suppose $a=p$. Then we can multiply both sides of
the equation by $b$ to obtain $ab=pb$. Since $ab=p$ (by assumption), we
have $p=pb$. Since $p\ne0$, we can use cancellation to obtain $b=1$, but
we assumed $b>1$, and in particular $b\ne1$, so we arrive at a
contradiction. So by choosing $c:=a$, we obtain $\neg B$.

Now we prove that the alternative definition implies the original
definition, which will complete the logical equivalence. This time we
use a proof by contradiction, which was also used in the first part. Our
general approach is:
$$(A\text{ and }\neg B\text{ and }C) \to \text{a contradiction (a false proposition).}$$
\[This statement is logically equivalent to
$(A\text{ and }C)\to(A\text{ and }B)$, which is what we want to show,
since both statements are false iff $A$ is true, $B$ is false, and $C$
is true.\]

Suppose $p>1$, there is a positive integer $d\not\in\{1,p\}$ with
$d\mid p$, and there are no integers $a,b>1$ with $p=ab$. Since
$d\mid p$, we know that there is some $t$ with $p=td$. If we can show
$d,t>1$, we get a contradiction. Since $d$ is a positive integer with
$d\ne 1$, we have $d>1$. Since $p=td$ and $p,d$ are positive, we know
$t>0$. Suppose $t=1$; then $p=d$, which contradicts our assumption. So
$t\ne1$, and we get $t>1$. This completes the proof.

Let $n$ be an integer. Then $n$ is iff there exists an integer $k$ such
that $n=2k$. Also, $n$ is iff there exists an integer $k$ such that
$n=2k+1$.

We see that $2\mid n$ for all even integers $n$ because $n$ can be
written as $2k$, and $2\mid 2k$.

\[2ngtn\] Let $n>0$ be an integer. Then $2n>n$.

By assumption, we have $n>0$. Adding $n$ to both sides of the
inequality, we obtain $n+n>n$, which completes the proof since $n+n=2n$.

\[mn0\] The natural number solutions to the equation $$m+n=1$$ are $m=0$
and $n=1$, or else $m=1$ and $n=0$.

Let $m,n$ be natural numbers. We must show
$m+n=1\to (m=0\wedge n=1)\vee(m=1\wedge n=0)$. Suppose for the sake of
contradiction that the consequent is false. Then we obtain
$(m=0\to n\ne1)\wedge(n=0\to m\ne1)$. Suppose $m=0$. Then $m+n=1$ so
$0+n=n=1$, a contradiction.

\[0k1\] There is no integer $k$ such that $0<k<1$.

Suppose for the sake of contradiction that there is some
$k\in\mathbf{Z}$ such that $0<k<1$. Separating the two inequalities we
obtain $0<k$ and $k<1$. Decomposing these further, we get $k=0+m$ for
some $m\in\mathbf{N}$, $k\ne0$, $1=k+n$ for some $n\in\mathbf{N}$, and
$k\ne1$. From the first of these we obtain $k=m$, and from the third we
obtain $k=1-n$. Combining these, we get $k=m=1-n$, which, by adding $n$
to all sides, becomes $k+n=m+n=1$. Using \[mn0\] we see that $m=0=k$ or
$m=1=k$; in either case this results in a contradiction.

\[1noteven\] $1$ is not even.

Suppose for the sake of contradiction that $1$ is even. Then there
exists some integer $k$ such that $1=2k$ Note that $k$ must be positive.
By \[2ngtn\], we see that $1=2k>k$, so $k<1$. But by \[0k1\] we know
that there cannot be such an integer. Hence $1$ is not even.

\[oddnoteven\] Let $n$ be an integer. Then $n$ is even if and only if
$n$ is not odd.

Note that this is equivalent to showing that $n$ is even or odd, but not
both. We first show that $n$ is even or odd. We use induction on the
natural numbers. For the base case, $0=2\cdot0$ and we are done. Now
suppose inductively that $n$ is even or odd. If $n$ is even, then $n=2k$
for some integer $k$ so that $n+1=2k+1$ (thus $n+1$ is odd). If $n$ is
odd, then $n=2k+1$ for some integer $k$ so that $n+1=2(k+1)$ (thus $n+1$
is even). This closes the induction, so every positive integer is even
or odd.

Now we show that every negative integer is even or odd. Let $n$ be a
negative integer. Then $n=-k$ for some positive integer $k$. Suppose $k$
is even. Then $k=2j$ for some $j$ so that $n=-k=-2j=2(-j)$ (so that $n$
is even). Now suppose $k$ is odd. Then $k=2j+1$ for some integer $j$ so
that $n=-k=-j-1=-2j-1+1-1=-2j-2+1=2(-j-1)+1$ (so that $n$ is odd).

Now we show that every integer cannot be both even and odd. Suppose for
the sake of contradiction that $n$ is an integer that is both even and
odd. Then there are integers $k,j$ such that $n=2k=2j+1$. This implies
that $2(k-j)=1$.

Now, for the sake of contradiction, suppose that $n$ is both even and
odd. Then there is an integer $k$ such that $n=2k$, and there is an
integer $j$ such that $n=2j+1$. We then have $2k=2j+1$, which implies
$2(k-j)=1$. So if we can show that $1$ is not even, then we are done.
But this was already shown in \[1noteven\].

\[onlyevenprime\] Let $p$ be a prime number with $p\ne2$. Then $p$ is
odd. In other words, $2$ is the only even integer.

Let $p\ne2$ be a prime number. Suppose for the sake of contradiction
that $p$ is even. Then we have $2\mid p$. We know that $2$ is a positive
integer. We also know $2\ne1$ and $2\ne p$. Since $p$ is prime, we have
$2\nmid p$. But this contradicts our previous hypothesis, so $p$ must be
odd.

Now consider the following example:

Let $n$ be an integer. Let $A$ be the proposition “$n\ne2$”, $B$ be the
proposition “$n$ is prime”, and $C$ be the proposition “$n$ is odd”.
Then $(A\wedge B)\to C$ is true because of the previous proposition. But
$(A\wedge B)\to C\equiv (A\to C)\vee(B\to C)$. So it must be the case
that “if $n\ne2$, then $n$ is odd; or, if $n$ is prime, then $n$ is
odd”. But this last proposition is false because $4\ne2$ but $4$ is not
odd. Also, $2$ is prime, but $2$ is even. Therefore,
$(A\wedge B)\to C\not\equiv (A\to C)\vee(B\to C)$.

This last example is tempting yet in fact false. To see this, consider
the fact that the integers can be partitioned into three cases as
follows:

1.  \[istwo\] $n=2$;

2.  \[iseven\] $n\ne2$ and $n$ is even;

3.  \[isodd\] $n\ne2$ and $n$ is odd.

The latter two cases cover all of when $n\ne2$ thanks to proposition
\[oddnoteven\]. Now suppose that $n=2$; i.e., that we are in case
(\[istwo\]). Then $A\to C$ is vacuously true, so that the entire
proposition is true. Now suppose we are in case (\[iseven\]). Then by
proposition (\[onlyevenprime\]), $n$ is not prime. But then $B\to C$ is
vacuously true, so the entire proposition is true. Now suppose we are in
case (\[isodd\]). Then $A\to C$ is trivially true since $C$ is true.
Therefore the entire proposition is true. Thus, for every $n$, the
proposition is true.
