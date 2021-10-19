# Does the following proof work for (a special case of) the deduction theorem?

Posted at https://math.stackexchange.com/questions/4281589/does-the-following-proof-work-for-a-special-case-of-the-deduction-theorem

I am interested in showing that $\{P\} \vdash Q$ if and only if $\vdash P \to Q$. This is a limited version of the deduction theorem where the "background" set of assumptions $\Delta$ happens to be empty.

The typical proof of the forward/"only if" direction is by induction. However, I am wondering if a proof like the following could also work. A few notes about my "proof system" before I give the attempted proof. My real interest in the deduction theorem is to try to better understand the material implication. So I don't want to "bake in" a meaning for "$\to$" by giving axioms that are suggestive. This leads to:

* I think I want to be working in a Hilbertian system, rather than a natural deduction system (which "bakes in" too much meaning into "$\to$"). This seems to work out since the deduction theorem isn't interesting in a natural deduction system anyway(?).
* I want to define "$P \to Q$" as a shorthand for "$\lnot P \lor Q$", rather than by directly giving axioms for "$\to$" that are suggestive of it having something to do with deduction.

With that out of the way, here is my attempted proof (I'll just do the forward/"only if" direction):

> **Attempted proof.** Suppose $\{P\} \vdash Q$. We have two cases, $P$ or $\lnot P$. If $P$, then since $\{P\} \vdash Q$ we have $Q$, so we have $\lnot P \lor Q$. On the other hand, if $\lnot P$ then we immediately have $\lnot P \lor Q$. In either case we have shown $\lnot P \lor Q$ so we are done.

A few questions I have about this:

* Does the above proof actually work?
* Am I essentially giving a semantic proof of the deduction theorem? If so, am I relying on soundness and/or completeness?
* I realize I am not exactly working inside the system/kind of cavalier about whether I am inside or outside the system. This is partly because I don't really have a system I am working with (as I explained above), and partly because I am not entirely sure what I am doing. But can this proof be turned into a more formal proof? If the proof can't be formalized, why not/what goes wrong?
* If the above proof works, why is the proof typically given using induction?
