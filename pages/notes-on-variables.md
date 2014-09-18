---
layout: default
title: Notes on variables
comments: "yes"
disqus-id: 25c65bb3f6a6be18ce493ca199a4a3a6620f376b
math: "yes"
license: "CC-BY"
tags: math, logic
---

things to talk about eventually:

- $p \leftrightarrow q$ vs $p \equiv q$.
- Propositional functions: view them as $f: \{\mathrm{T},\mathrm{F}\}^n\to \{\mathrm{T},\mathrm{F}\}$?
  The tautologies are all $f$ such that for any $x\in \{\mathrm{T},\mathrm{F}\}^n$, we have $f(x) = \mathrm{T}$?

    Now, for some $x\in \{\mathrm{T},\mathrm{F}\}^n$, what do we make of the statement $f(x)$? Is it true or false?

- bound variables in expressions like $\int_a^b f(x)\, dx$ and
  $\sum_{i=0}^n f(i)$ vs in ones like $\exists x P(x)$

- why different results for partial and total derivative? cf. Tao's
  analysis book

    > Tao's example: take $f$ defined by $f(x,y) = (x^2, y^2)$.
    > Then $\displaystyle \frac{\partial f}{\partial x} = (2x,0)$,
    > whereas $\displaystyle \frac{d}{dx}f(x,x) = (2x,2x)$.

- transfer pdf notes

- what do we make of statements like "when $x=3$..."?

- How do we make sense of things like the partial derivative, where one variable is "moving" while the others stay "constant"?

- "as $x$ gets larger..."

- "$a_n \to \infty$ as $n\to 5$"


- $ax + b = 0$


Concepts to discuss:

- parameter, arbitrary fixed constant, , flowing letters, meta-variables
- distinction between bound universals and free arbitrary variables
- undefined/unspecified/unknown/undetermined
- known constants vs unknown constants
- undefined constants vs variables
- declaration of variable type
- variable assignment
- [here](http://math.stackexchange.com/questions/24284/is-the-variable-in-let-y-fx-free-bound-or-neither) is an example of when variables can lead to confusion.
- temporary (new) constants


## Questions

- What is the difference between a parameter and a variable?
- What is the difference between a variable and a meta-variable?
- In expressions like $ax + b$, is there an essential difference between $x$ and the other letters, even when we say that $x$ is a variable while $a$ and $b$ are constants?
- What does it mean to define some variable $y$ as a function of another variable $x$?
    - e.g. what does it mean to say something like "as $y$ gets larger, $x$ also gets larger"?
        - Two possible interpretations: (1) Treat $y = f(x)$ as a
          condition, and look at different possibilities like "if $x =
          1$, then $y = f(1)$", and so on. (2) treat $y$ as a machine that outputs different things for different inputs. So as $x$ is "adjusted", $y$ is affected too.
