Michael Sipser's _Introduction to the Theory of Computation_ states [Kleene's second recursion theorem](https://en.wikipedia.org/wiki/Kleene%27s_recursion_theorem#Kleene's_second_recursion_theorem) using Turing machines (rather than partial recursive functions and their indexes, as on Wikipedia). Sipser's book does not state the [Rogers fixed point theorem](https://en.wikipedia.org/wiki/Kleene%27s_recursion_theorem#Rogers's_fixed-point_theorem) in the same way, but one could for instance state it as follows:

**Fixed point theorem.** Let $F$ be a Turing machine which computes a function $f : \Sigma^* \to \Sigma^*$ (where $\Sigma^*$ is the set of all strings in some alphabet $\Sigma$). Then there exists a Turing machine $R$ which computes a function $r : \Sigma^* \to \Sigma^*$, and a Turing machine $T$ which computes a function $t : \Sigma^* \to \Sigma^*$, such that $f(\langle R\rangle) = \langle T\rangle$ and $r(w) = t(w)$ for all $w \in \Sigma^*$.

A proof of this theorem, similar to the proof of the recursion theorem in the book (and also similar to how one would typically write a quine), can be given as follows:

*Proof.* We build $R$ in three parts, $A,B,E$, where:

* $A$ is $P_{\langle BE\rangle}$ (here $P_w$ is a Turing machine that prints out $w$ and halts)
* $B$ is the Turing machine that, on input $w, \langle M\rangle$, computes $q(\langle M\rangle)$, combines the result with $\langle M\rangle$ to make a complete Turing machine, prints $w$ along with the description of this Turing machine, and halts. In other words, $B$ outputs $w, q(\langle M\rangle)\langle M\rangle$. Here $q(w)$ is the description of $P_w$, i.e. $q(w) = \langle P_w\rangle$.
* $E$ is an "eval" Turing machine that, on input $w, \langle M\rangle$, changes the tape contents to $\langle M\rangle$, runs $F$ (storing the result as $\langle T\rangle$), changes the tape contents to $w$, and runs $T$.

Given input $w$, $R$ runs as follows: First $A$ runs, and prints $\langle BE\rangle$ after the input so that the tape now contains $w,\langle BE\rangle$. Next, $B$ runs. $B$ computes $q(\langle BE\rangle) = \langle A\rangle$ and combines this with $\langle BE\rangle$. Thus, after $B$ finishes, the tape contains $w, \langle ABE\rangle = w, \langle R\rangle$. Finally $E$ runs. It first runs $F$ with input $\langle ABE\rangle = \langle R\rangle$, and stores $\langle T \rangle = f(\langle R\rangle)$. Then it runs $T$ on $w$, which results in $t(w)$ being left on the tape at the end. Since this is the final output of $R$ given the input $w$, we have $r(w) = t(w)$. $\Box$

I will ignore undefined values to simplify the question.

Translating the standard diagonalization proof of the fixed point theorem, we get:

Let $D$ be the Turing machine that, on input $\langle M\rangle$, runs $M$ on the input $\langle M\rangle$. Let $d : \Sigma^* \to \Sigma^*$ be the function computed by $D$.

Let $C$ be the Turing machine that, on input $w$, runs $D$ with the input $w$, and then runs $F$ with whatever is left on the tape. Let $c : \Sigma^* \to \Sigma^*$ be the function computed by $C$. Thus $c = f\circ d$.

Let $\langle R\rangle$ be $c(\langle C\rangle) = d(\langle C\rangle)$. $c = f\circ d$ so $d(\langle C\rangle) = f(d(\langle C\rangle))$. So we can take $\langle T \rangle = c(\langle C\rangle)$ as well.
