# Writing action-value function in terms of state-value function for a Markov decision process

Asked at https://math.stackexchange.com/questions/3143290/writing-action-value-function-in-terms-of-state-value-function-for-a-markov-deci

I am working through [Sutton and Barto's text on reinforcement learning (2nd edition)](http://incompleteideas.net/book/the-book-2nd.html), and am stuck on exercise 3.13 (p. 58). The exercise is to write $q_\pi$ in terms of $v_\pi$ and $p(s',r\mid s,a)$, where $q_\pi$ is the action-value function defined by $$q_\pi(s,a) := \mathbb E_\pi [G_t \mid S_t=s, A_t=a];$$ $v_\pi$ is the state-value function defined by $$v_\pi(s) := \mathbb E_\pi[G_t \mid S_t=s];$$ and $G_t$ is the discounted return $$G_t := \sum_{k=0}^\infty \gamma^k R_{t+k+1}.$$

My attempt so far is to write $G_t = R_{t+1} + \gamma G_{t+1}$ so that $$q_\pi(s,a) = \mathbb E_\pi[R_{t+1} \mid S_t=s,A_t=a] + \gamma \mathbb E_\pi[G_{t+1} \mid S_t=s,A_t=a].$$

Now $\mathbb E_\pi[G_{t+1} \mid S_t=s,A_t=a]$ becomes:

- $\sum_g g \Pr(G_{t+1}=g\mid S_t=s,A_t=a)$ (definition of expected value)
- $\sum_g g \sum_{s'} \Pr(G_{t+1}=g, S_{t+1}=s'\mid S_t=s,A_t=a)$ (law of total probability)
- $\sum_g g \sum_{s'} \Pr(G_{t+1}=g \mid S_t=s,A_t=a,S_{t+1}=s') \Pr(S_{t+1}=s' \mid S_t=s,A_t=a)$
    - (definition of conditional probability; the expression was too long so I've placed this parenthetical on the line below)
- $\sum_{s'} \Pr(S_{t+1}=s'\mid S_t=s,A_t=a) \sum_g g \Pr(G_{t+1}=g\mid S_t=s,A_t=a,S_{t+1}=s')$
    - (rearranging sums)
- $\sum_{s'}\Pr(S_{t+1}=s'\mid S_t=s,A_t=a) \mathbb E_\pi[G_{t+1} \mid S_t=s,A_t=a,S_{t+1}=s']$
    - (definition of expected value)

In turn, $\Pr(S_{t+1}=s'\mid S_t=s,A_t=a)$ can be written as $\sum_r p(s',r\mid s,a)$ (this is equation 3.5 in the book).

Similarly $\mathbb E_\pi[R_{t+1} \mid S_t=s,A_t=a]$ can be written as $\sum_{s'} \Pr(S_{t+1}=s'\mid S_t=s,A_t=a) \mathbb E_\pi[R_{t+1} \mid S_t=s,A_t=a,S_{t+1}=s']$ where $\mathbb E_\pi[R_{t+1} \mid S_t=s,A_t=a,S_{t+1}=s']$ can be written in terms of $p(s',r\mid s,a)$ (using equation 3.6 in the book).

So the only problem left is the expression $\mathbb E_\pi[G_{t+1} \mid S_t=s,A_t=a,S_{t+1}=s']$. If I squint my eyes, it looks like $v_\pi(s')$, and indeed, looking around, I see formulas indicating that it _should_ be $v_\pi(s')$ (e.g. PDF page 35 of [these slides](http://www0.cs.ucl.ac.uk/staff/d.silver/web/Teaching_files/MDP.pdf), page 13 of [these slides](https://www.cs.cmu.edu/~mgormley/courses/10601-s17/slides/lecture26-ri.pdf), and the equation given in [this section](https://en.wikipedia.org/wiki/Markov_decision_process#Reinforcement_learning)). But I don't see how to convince myself that this is the case. Sutton and Barto write that "the probability of each possible value for $S_t$ and $R_t$ depends only on the immediately preceding state and action, $S_{t-1}$ and $A_{t-1}$, and, given them, not at all on earlier states and actions" (p. 49). But here, we only have $S_{t+1}$ and not $A_{t+1}$, so we can't just ignore the "$S_t=s,A_t=a$" part. Given the policy $\pi$, the action $A_{t+1}$ is completely determined by $S_{t+1}$, so my attempt is to write:

- $\mathbb E_\pi[G_{t+1} \mid S_t=s,A_t=a,S_{t+1}=s']$
- $\sum_g g \Pr(G_{t+1}=g \mid S_t=s,A_t=a,S_{t+1}=s')$ (definition of expected value)
- $\sum_g g \sum_{a'} \Pr(G_{t+1}=g,A_{t+1}=a' \mid S_t=s,A_t=a,S_{t+1}=s')$ (law of total probability)
- $\sum_g g \sum_{a'} \Pr(G_{t+1}=g \mid S_t=s,A_t=a,S_{t+1}=s',A_{t+1}=a')\pi(a'\mid s')$
    - (definition of conditional probability)
- $\sum_g g \sum_{a'} \Pr(G_{t+1}=g \mid S_{t+1}=s',A_{t+1}=a')\pi(a'\mid s')$ (Markov property)
- $\sum_g g \sum_{a'} \Pr(G_{t+1}=g,A_{t+1}=a' \mid S_{t+1}=s')$ (definition of conditional probability)
- $\sum_g g \Pr(G_{t+1}=g\mid S_{t+1}=s')$ (law of total probability)
- $\mathbb E_\pi[G_{t+1} \mid S_{t+1}=s']$ (definition of expected value)

Is this reasoning valid?

My other confusion is that, supposing $\mathbb E_\pi[G_{t+1} \mid S_t=s,A_t=a,S_{t+1}=s'] = \mathbb E_\pi[G_{t+1} \mid S_{t+1}=s']$,  it seems like we could also say that $\mathbb E_\pi[R_t\mid S_{t-1}=s,A_{t-1}=a,S_t=s'] = \mathbb E_\pi[R_t \mid S_t=s']$. But if that's the case, I'm confused about why Sutton and Barto derive an expression for $r(s,a,s'):=\mathbb E_\pi[R_t\mid S_{t-1}=s,A_{t-1}=a,S_t=s']$ rather than one for $r(s')$ (which can be defined to equal $\mathbb E_\pi[R_t\mid S_t=s']$). In other words my question is something like "if the $s$ and $a$ in $r(s,a,s')$ don't matter, why include them in the notation?"
