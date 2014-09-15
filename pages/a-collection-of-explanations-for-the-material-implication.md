---
layout: default
title: A collection of explanations for the material implication
comments: "yes"
math: "yes"
license: "CC-BY"
tags: math
---

This document outlines some of the common explanations surrounding the
material implication connective in propositional logic.  The connective
is most commondly represented using an arrow such as `\(\to\)` or
`\(\implies\)` (even `\(\supset\)` in older texts), and when placed
between two propositions as in “`\(p \to q\)`”, is supposed to mean “if `\(p\)`, then `\(q\)`”. Moreover, this connective is defined as a truth function as follows.

- `\(p \to q\)` is true when `\(p\)` is false or when `\(q\)` is true
- `\(p \to q\)` is false when `\(p\)` is true and `\(q\)` is false

In other words, `\(p\to q\)` is equivalent to writing `\(\neg p \vee q\)`.
A problem arises when working off this definition, however, because the
conditions for truth given above do not correspond to the natural
language sense of “if `\(p\)`, then `\(q\)`”. The purpose of this
document then is to explain why the material implication is defined as
it is, and to aid in an intuitive understanding of the connective.

## Tarski

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
