# Undecidability of semantic implication of arbitrary sets of sentences in first-order logic?

(I started writing up this question, then realized my mistake.)

I am trying to collect equivalent formulations of the undecidability of first-order logic (the _Entscheidungsproblem_), which states that there is no algorithm that takes as input a sentence in first-order logic and decides whether or not the sentence is valid.

I know that the undecidability of validity is equivalent to the undecidability of semantic implication of finite sets of sentences, in the sense that an algorithm for each problem can be used to solve the other problem. On the one hand, if semantic implication of finite sets of sentences is decidable, then take $\emptyset$ as the set of sentences to decide validity. On the other hand, if validity is decidable, then if $\Gamma = \{\gamma_1, \ldots, \gamma_n\}$ and $\phi$ are inputs, form the sentence $(\gamma_1\wedge \cdots \wedge \gamma_n) \to \phi$ and test its validity. (I learned this trick from [these](https://math.stackexchange.com/a/2190149/35525) [two](https://math.stackexchange.com/a/696106/35525) answers.)

I am also aware that, by Gödel's completeness theorem, undecidability of validity is equivalent to the undecidability of provability.

I also know that undecidability of validity is equivalent to undecidability of satisfiability. This follows from exercises 1 and 2 in [this tutorial](https://www.cs.nmsu.edu/historical-projects/Projects/FoLundecidability.pdf) (see [this question](https://math.stackexchange.com/questions/3004349/g%C3%B6dels-completeness-theorem-and-the-undecidability-of-first-order-logic) for solutions).

What I am wondering is if undecidability of validity is equivalent to the undecidability of semantic implication of _arbitrary_ (i.e. not restricted to finite) sets of sentences. If semantic implication is decidable, it is again possible to take $\emptyset$ as the set of sentences to decide validity. For the converse (**this is the part I am not sure about**), suppose we can decide validity. Let $\Gamma$ be a set of sentences and $\phi$ be a sentence. Then:

- $\Gamma \models \phi$
- iff $\Gamma \vdash \phi$ (by Gödel's completeness theorem)
- iff there is a derivation of $\phi$ from $\Gamma$ (expanding definition of $\vdash$)
- iff there is a derivation of $\phi$ from some finite subset of $\Gamma$ (derivations are finite)
- iff there is some subset $\Delta \subseteq \Gamma$ such that $\Delta \vdash \phi$ (rewriting using $\vdash$)
- iff there is some subset $\Delta \subseteq \Gamma$ such that $\Delta \models \phi$ (by Gödel's completeness theorem)
- iff ... actually this is where the proof fails: we can decide each $(\delta_1 \wedge \cdots \wedge \delta_n) \to \phi$ but we also need to find the $\Delta$ set
