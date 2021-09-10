In my opinion, the truth-table definition of material implication is disturbing because "if ..., then ..." is used in mathematics in two distinct ways (and no similar distinction exists for the other connectives like NOT, AND, and OR):

1. "If $p$, then $q$" means that you can start out with $p$, make some deductions, and end up with $q$.
2. As the truth table definition.

These end up being the same in classical logic, of course, but they are *conceptually distinct*. I think what is necessary is to connect these two concepts. In other words, for the truth table definition to make sense, and for a logical connective to be called an "implication", it has to be shown equivalent to the deductive sense. In mathematical logic we have the distinction between $\{p\} \vdash q$ and $\vdash p\to q$, which are shown to be equivalent by the [deduction theorem](https://en.wikipedia.org/wiki/Deduction_theorem) (and its converse), but I believe it is possible to show this same kind of thing without bringing in all of the scary formal notation from mathematical logic.

I have a [longer essay](https://riceissa.github.io/material-conditional/) that implements the above strategy for explaining the material implication.
