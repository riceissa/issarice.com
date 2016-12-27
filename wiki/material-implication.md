---
title: Material implication
author: Issa Rice
comments: "yes"
status: notes
belief: possible
---

This document outlines some of the common explanations surrounding the
material implication connective in propositional logic.  The connective
is most commondly represented using an arrow such as $\to$ or
$\implies$ (even $\supset$ in older texts), and when placed
between two propositions as in “$p \to q$”, is supposed to mean “if $p$, then $q$”. Moreover, this connective is defined as a truth function as follows.

- $p \to q$ is true when $p$ is false or when $q$ is true
- $p \to q$ is false when $p$ is true and $q$ is false

In other words, $p\to q$ is equivalent to writing $\neg p \vee q$.
A problem arises when working off this definition, however, because the
conditions for truth given above do not correspond to the natural
language sense of “if $p$, then $q$”. The purpose of this
document then is to explain why the material implication is defined as
it is, and to aid in an intuitive understanding of the connective.


Two Naive Examples
==================

Consider the conditional proposition “if one is in Berkeley, then one is
in California”. We wish to know when this proposition is false and when
it is true. To analyze this proposition, we consider various cases:

-   Consider first when one is in Berkeley and one is in California. Is
    “if one is in Berkeley, then one is in California” true? It seems
    so, since this is exactly what the proposition claims.

-   Consider next when one is in Berkeley but not in California. Since
    Berkeley is located within California, this is impossible; however,
    if it *were* true, it would certainly be an anomaly. We might thus
    reason that in this case, the conditional proposition would be
    false.

-   Finally consider when one is not in Berkeley (regardless of whether
    one is in California; one could be in Los Angeles, in which case one
    would be outside of Berkeley but still in California, or one could
    be in London, in which case one would be outside of both Berkeley
    and California). In this case, one could still entertain the idea of
    *if* one is in Berkeley; i.e., one can *assume* that one is in
    Berkeley, and conclude that in this case, one would also be in
    California.

From the above analysis, we might conclude that the conditional
proposition indeed is the same as the material conditional; the
conditional proposition “if one is in Berkeley, then one is in
California” was seen to be false only when the antecedent is true and
the consequent is false, and true otherwise. As the title of this
section implies, however, this analysis is naive in that it works in
favor of human intuition, and conveniently hides problems with the
approach. The next example shows how a similar example can work against
human intuition.

Consider the conditional proposition “if one is in Berkeley, then one is
in Massachusetts”. We present a similar analysis of this proposition:

-   Consider when one is in Berkeley and one is in Massachusetts. We
    might say this is precisely what the proposition claims, and
    therefore it is true. We might also say that this situation is
    impossible, and so the proposition is false. We will give the
    benefit of the doubt to the proposition and say it is true in this
    case.

-   Consider next when one is in Berkeley but not in Massachusetts. The
    situation is possible, but it directly contradicts what is claimed
    by the proposition, so we can conclude that it is false.

-   Finally consider when one is not in Berkeley. One can still proceed,
    as in the last example, by thinking *if* one is in Berkeley, and
    asking whether one is in Massachusetts in that case. One certainly
    is not in Massachusetts even if one assumes one is in Berkeley, so
    we conclude the proposition to be false in this case.

From our preceding analysis, we obtain a new truth table for the
conditional proposition:

   $p$   $q$   $p\rightarrow q$
  ----- ----- ------------------
    T     T           T
    T     F           F
    F     T           F
    F     F           F

This seems strange, and indeed especially strange if we want to use the
conditional proposition in a mathematical context—for this, as mentioned
earlier, the proposition should only depend on properties of a formal
system, presumably only the truth values of the constituent
propositions, i.e., the truth values of $p$ and $q$. We presumably also
want the conditional proposition to have a systematic method of
evaluating the truth; one thing to note is that the material conditional
already achieves this. To attempt to resolve this issue, we will now
move on and consider various other analyses. We may conclude this
section by saying that perhaps our examples were not well chosen; better
examples could have been found within pure mathematics. This remark,
however, simply cements the title for this section.



# Tarski

> The divergency between the usage of the phrase “*if…, then…*” in
> ordinary language and its usage in mathematical logic has been at the
> root of lengthy and even passionate discussions,—in which, by the way,
> professional logicians took only a minor part. (It is perhaps
> surprising, that considerably less attention was paid to the analogous
> divergency in the case of the word “*or*”.) It has been objected that
> logicians, on account of their adoption of the concept of material
> implication, arrived at paradoxes and even at plain nonsense. This has
> resulted in an outcry for a reform of logic, and in particular, for
> bringing about a far-reaching rapprochement between logic and ordinary
> language with regard to the use of implication.
> 
> It would be hard to grant that these criticisms are well founded.
> There is no phrase in ordinary language which has a precisely determined
> meaning. It would scarcely be possible to find two people who would use
> every word with exactly the same meaning, and even in the language of a
> single person the meaning of a given word may vary from one period of
> the person's life to another. Moreover, the meaning of words of everyday
> language is usually very complicated; it depends not only on the
> external form of the word, but also on the circumstances in which it is
> uttered, and sometimes even on subjective psychological factors. If a
> scientist wants to transfer a concept from everyday life into a science
> and to establish general laws concerning this concept, he (or she) must
> always make its content clearer, more precise, and simpler, and free it
> from inessential attributes; it does not matter here whether he is a
> logician who is concerned with the phrase “*if…, then…*”, or, for
> instance, a physicist wanting to establish the exact meaning of the word
> “*metal*”. In whatever way the scientist realizes his task, the resulting
> usage of the term will deviate more or less from the practice of
> everyday language. If, however, he states explicitly in what sense he
> decides to use the term, and if afterwards he acts always in accordance
> with this decision, then nobody will be in a position to object, or to
> argue that his procedure leads to nonsensical results.

# Ramsey


The following is taken from the Stanford Encyclopedia of Philosophy[^1]
and written by Ramsey. Note that the notation for negation has been
changed.

> If two people are arguing ‘If $p$, then $q$?’ and are both in doubt as
> to $p$, they are adding $p$ hypothetically to their stock of knowledge
> and arguing on that basis about $q$; so that in a sense ‘If $p$, $q$’
> and ‘If $p$, $\neg q$’ are contradictories. We can say that they are
> fixing their degree of belief in $q$ given $p$. If $p$ turns out
> false, these degrees of belief are rendered *void*. If either party
> believes *not* $p$ for certain, the question ceases to mean anything
> to him except as a question about what follows from certain laws or
> hypotheses.

[^1]: <http://plato.stanford.edu/entries/logic-conditionals/#RamTesConTheCon>


The number analogy
==================

[sec:The number analogy]

One can also construct the following analogy. Let T and F be $1$ and $0$
respectively; so to each proposition a number is assigned. Then define
$\neg p := |p-1|$; define $p\wedge q := \min(p,q) = pq$; define
$p\vee q := \max(p,q) = p+q-pq$; define $$p\to q :=
\begin{cases}
    1, &\text{ if }p\leq q; \\
    0, &\text{ if }p>q;
\end{cases}$$ and finally define $$p\leftrightarrow q :=
\begin{cases}
    1, &\text{ if }p=q\\
    0, &\ \mathrm{if }\ p\ne q
\end{cases}$$

Furthering the analogy
----------------------

[sub:Furthering the analogy] The following is originally from a Google
Buzz that Terence Tao posted[^2]. The conditional proposition “if $p$,
then $q$” is the same as “$p$ is at most as true as $q$” and “$q$ is at
least as true as $p$”. This can easily be seen using the number analogy
and some logical equivalences. First note that
$p\to q = p\leftrightarrow (p\wedge q) = p\leftrightarrow\min(p,q)$
because for any $p$ and $q$, each produces the same digit. (Note in
particular that each only produces a $0$ when $p=1$ and $q=0$.) Consider
what $p\leftrightarrow\min(p,q)$ is stating. It says that $p$ is the
same as the lesser of $p$ and $q$; so even if $p$ is large, it cannot
exceed $q$; i.e., $p$ is at most $q$.

Now note that $p\to q = q \leftrightarrow \max(p,q)$. We see that
$q\leftrightarrow \max(p,q)$ says $q$ is the same as the greater of $p$
and $q$; so even if $q$ is small, it cannot be smaller than $p$; i.e.,
$q$ is at least $p$.

In fact, something exactly like this happens in fuzzy logic.

[^2]: <https://profiles.google.com/114134834346472219368/buzz/YNHWb5mzEKP>

# Subset analogy

It's possible to think of $p\to q$ as $P \subseteq Q$.
Indeed, we need only define $P = \{1 : p\}, Q = \{1 : q\}$, so that we have the correspondence:



 $p$   $q$   $p \to q$       $P$          $Q$       $P \subseteq Q$
----- ----- -----------  -----------  -----------  -----------------
  T     T        T         $\{1\}$      $\{1\}$         T
  T     F        F         $\{1\}$    $\emptyset$       F
  F     T        T       $\emptyset$    $\{1\}$         T
  F     F        T       $\emptyset$  $\emptyset$       T

In this sense, the vacuous implication $\mathrm{F}\to q$ for any proposition $q$ becomes the similarly vacuous $\emptyset\subseteq Q$ for any set $Q$; see [Halmos's explanation](#halmos) for the latter.

# Halmos


As Halmos states in his *Naive Set Theory* (page 8),

> The empty set is a subset of every set, or, in other words,
> $\emptyset\subset A$ for every $A$. To establish this, we might argue
> as follows. It is to be proved that every element in $\emptyset$
> belongs to $A$; since there are no elements in $\emptyset$, the
> condition is automatically fulfilled. The reasoning is correct but
> perhaps unsatisfying. Since it is a typical example of a frequent
> phenomenon, a condition holding in the “vacuous” sense, a word of
> advice to the inexperienced reader might be in order. To prove that
> something is true about the empty set, prove that it cannot be false.
> How, for instance, could it be false that $\emptyset\subset A$? It
> could be false only if $\emptyset$ had an element that did not belong
> to $A$. Since $\emptyset$ has no elements at all, this is absurd.
> Conclusion: $\emptyset\subset A$ is not false, and therefore
> $\emptyset\subset A$ for every $A$.

