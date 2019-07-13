I have noticed that there seem to be two ways to prove the Rogers fixed point theorem, and I'm wondering if there is some sort of relationship between them (e.g. are they somehow essentially the same proof?).

Michael Sipser's _Introduction to the Theory of Computation_ states [Kleene's second recursion theorem](https://en.wikipedia.org/wiki/Kleene%27s_recursion_theorem#Kleene's_second_recursion_theorem) using Turing machines (rather than partial recursive functions and their indexes, as on Wikipedia). Sipser's book does not state the [Rogers fixed point theorem](https://en.wikipedia.org/wiki/Kleene%27s_recursion_theorem#Rogers's_fixed-point_theorem) in the same way, but one could for instance state it as follows:

**Fixed point theorem.** Let $F$ be a Turing machine which computes a function $f : \Sigma^* \to \Sigma^*$ (where $\Sigma^*$ is the set of all strings in some alphabet $\Sigma$). Then there exists a Turing machine $R$ which computes a function $r : \Sigma^* \to \Sigma^*$, and a Turing machine $T$ which computes a function $t : \Sigma^* \to \Sigma^*$, such that $f(\langle R\rangle) = \langle T\rangle$ and $r(w) = t(w)$ for all $w \in \Sigma^*$.

A proof of this theorem, similar to the proof of the recursion theorem in the book (and also similar to how one would typically write a quine), can be given as follows:

*Proof.* We build $R$ in three parts, $A,B,E$, where:

* $A$ is $P_{\langle BE\rangle}$ (here $P_w$ is a Turing machine that prints out $w$ and halts)
* $B$ is the Turing machine that, on input $w, \langle M\rangle$, computes $q(\langle M\rangle)$, combines the result with $\langle M\rangle$ to make a complete Turing machine, prints $w$ along with the description of this Turing machine, and halts. In other words, $B$ outputs $w, q(\langle M\rangle)\langle M\rangle$. Here $q(w)$ is the description of $P_w$, i.e. $q(w) = \langle P_w\rangle$.
* $E$ is an "eval" Turing machine that, on input $w, \langle M\rangle$, changes the tape contents to $\langle M\rangle$, runs $F$ (storing the result as $\langle T\rangle$), changes the tape contents to $w$, and runs $T$.

Given input $w$, $R$ runs as follows: First $A$ runs, and prints $\langle BE\rangle$ after the input so that the tape now contains $w,\langle BE\rangle$. Next, $B$ runs. $B$ computes $q(\langle BE\rangle) = \langle A\rangle$ and combines this with $\langle BE\rangle$. Thus, after $B$ finishes, the tape contains $w, \langle ABE\rangle = w, \langle R\rangle$. Finally $E$ runs. It first runs $F$ with input $\langle ABE\rangle = \langle R\rangle$, and stores $\langle T \rangle = f(\langle R\rangle)$. Then it runs $T$ on $w$, which results in $t(w)$ being left on the tape at the end. Since this is the final output of $R$ given the input $w$, we have $r(w) = t(w)$. $\Box$

The fixed point theorem can also be proved in a [different way](https://en.wikipedia.org/wiki/Kleene's_recursion_theorem#Proof_of_the_fixed-point_theorem), by constructing a diagonal function.

Before I wrote down the proof of the fixed point theorem in Sipser's style, I had thought it would come out basically the same way as the standard diagonalization proof. However, now that I look at the proofs side-by-side, I am having trouble actually picking out connections between them (e.g. Where does the quine version make use of a diagonal function? Is it somehow implicit in the proof? Does the diagonalization proof tell me how to write a quine?)

If the proofs are genuinely different, that seems interesting to me, and I would have follow-up questions like, is it possible to prove other diagonalization theorems (e.g. Cantor's theorem, Russell's paradox, the diagonalization lemma in logic) in a quine-like way?

If the proofs are actually basically the same, I would like to be able to explicitly construct parallels between them, so that I can see at a glance that they are the same.
