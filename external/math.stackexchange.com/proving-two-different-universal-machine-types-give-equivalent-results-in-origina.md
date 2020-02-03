Solomonoff's [original paper](https://www.sciencedirect.com/science/article/pii/S0019995864902232) about Solomonoff induction contains the following (p. 18):

> Suppose $M$ to be a universal machine with binary input alphabet, and an output alphabet that is the same as that of $T$ [where $T$ is a string of length $m$]. We shall consider $M$ to be either of the ordinary type, $M_1$, described in Section 3.1, or the 3-tape type, $M_2$, described in Section 3.2. In the present case, it has been proved that these two machine types give equivalent results.
>
> Consider all binary strings of length $R$. Say $N_R$ of them are meaningful inputs to $M$—i.e., they cause $M$ to stop eventually. Of these $N_R$ meaningful inputs to $M$, say $N_T$ of them result in outputs whose first $m$ symbols are, respectively, identical to the $m$ symbols of $T$. Then the a priori probability assigned to $T$ will be $$N_T/N_R \tag{9}$$ This ratio will become more exact as $R$ approaches infinity, but will usually be good enough if $R$ satisfies Eq. (8).
>
> It can be proved that the present inductive inference model is identical to that of Section 3.2, if $M$ is a machine of either type $M_1$ or of type $M_2$.

In this paper, $M_1$ is a universal Turing machine, and "$M_2$ is a 3-tape machine with unidirectional output and input tapes." (I think now this would be called a universal monotone Turing machine.)

The inductive inference model of Section 3.2 is to set the probability of $T$ to $\sum_{i=1}^\infty 2^{-N(T,i)}$, where $N(T,i)$ is the number of bits in the $i$th minimal program for $T$ (i.e. outputs something starting with $T$, and if you remove the final bit from the program it will no longer output something starting with $T$).

My questions are:

1. What does Solomonoff mean when he says "it has been proved" and "It can be proved"? As far as I can tell, the paper itself does not contain these proofs. Does he mean that he proved these privately but chose not to include them in the paper?
2. I think I've found a proof that using expression (9) for $M_2$ gives the same probability as the inductive inference model of Section 3.2. But I have no idea how using expression (9) with $M_1$ gives the same answer (as Solomonoff claims). How can I prove this? I find $M_1$ programs difficult to work with, since not all programs halt and since $M_1$ is not monotonic (i.e. a longer program can come and erase output produced by a shorter version of that program).
