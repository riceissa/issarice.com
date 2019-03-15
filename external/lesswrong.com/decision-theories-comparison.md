% Comparison of decision theories
% Issa Rice
% 2018-10-10

TODO: fix straight quotes/curly quotes (done at one point, but do this again before publishing), dashes, and bare URLs

# Introduction

This post is a comparison of various existing decision theories, with a focus
on decision theories that use logical counterfactuals (a.k.a. the kinds of decision theories most discussed on LessWrong). The post compares the
decision theories along outermost iteration (action vs policy vs algorithm),
updatelessness (updateless or updateful), and type of counterfactual used
(causal, conditional, logical). It then explains the decision theories in more
detail, in particular giving an expected utility formula for each. The post then gives
examples of specific existing decision problems where the decision theories
give different answers.

## Value-added

There are some other comparisons of decision theories (see the “Other comparions” section),
but they either (1)
don’t focus on logical-counterfactual decision theories; or (2) are outdated
(written before the new functional/logical decision theory terms came about).

To give a more personal motivation, after reading through a bunch of papers and posts about these
decision theories, and feeling like I understood the basic ideas, I still
remained highly confused about basic things like “How is UDT different from
FDT?”, “Why was TDT deprecated?”, and “If TDT performs worse than FDT, then
what’s one decision problem where they give different outputs?”
This post hopes to clarify these and other questions.

None of the decision theory material in this post is novel. I am still learning
the basics myself, and I would appreciate any corrections (even about subtle/nitpicky stuff).

## Audience

This post is intended for people who are [similarly](https://www.greaterwrong.com/posts/xJRPWBfJQcbWaoCLp/making-equilibrium-cdt-into-fdt-in-one-easy-step/comment/n7auEbvrH5DoC6Tvt) [confused](https://www.lesswrong.com/posts/2THFt7BChfCgwYDeA/let-s-discuss-functional-decision-theory) about the
differences between TDT, UDT, FDT, and LDT. In terms of reader background assumed,
it would be good to know the statements to some standard decision theory
problems (Newcomb’s problem, smoking lesion, Parfit’s hitchhiker, transparent
box Newcomb’s problem, counterfactual mugging) and the “correct” answers to
them, and having enough background in math to understand the expected utility
formulas.

If you don’t have the background, I would recommend reading
chapters 5 and 6 of
Gary Drescher’s [*Good and Real*](https://www.gwern.net/docs/statistics/decision/2006-drescher-goodandreal.pdf) (explains well the idea of subjunctive means--end relations),
the [FDT paper](https://arxiv.org/pdf/1710.05060.pdf) (explains well how FDT’s action selection variant works, and how FDT differs from CDT and EDT),
[“Cheating Death in Damascus”](https://intelligence.org/files/DeathInDamascus.pdf), and
[“Toward Idealized Decision Theory”](https://arxiv.org/pdf/1507.01986.pdf) (explains the difference between policy selection and logical counterfactuals well), and understanding
what Wei Dai calls “decision theoretic thinking” (see comments:
[1](https://www.lesswrong.com/posts/g8xh9R7RaNitKtkaa/explicit-optimization-of-global-strategy-fixing-a-bug-in#FMvBDD7fNQSd3B3qd),
[2](https://www.lesswrong.com/posts/gkAecqbuPw4iggiub/common-mistakes-people-make-when-thinking-about-decision#uXrbGTefqvek9kkzf),
[3](https://www.lesswrong.com/posts/GfHdNfqxe3cSCfpHL/the-absent-minded-driver#Hrtu69eAh86KFNgBC)).
I think a lot of (especially old) content on decision theory is confusingly
written or unfriendly to beginners, and would recommend skipping around to find
explanations that “click”.

TODO maybe also recommend https://www.lesswrong.com/posts/af9MjBqF2hgu3EN6r/decision-theories-a-less-wrong-primer

# Comparison dimensions

My main motivation is to try to distinguish between TDT, UDT, and FDT, so I
focus on three dimensions for comparison that I think best display the differences
between these decision theories.

## Outermost iteration

All of the decision theories in this post iterate through some set of “options” (intentionally vague)
at the outermost layer of execution to find the best “option”. However, the
nature of these “options” differs among the various theories.
Most decision theories iterate through either *actions* or *policies*.
When a decision theory iterates through actions (to find the best action),
it is doing “action selection”, and the decision theory outputs a single action.
When a decision theory iterates through policies (to find the best policy),
it is doing “policy selection”, and outputs a single *policy*, which is an
observation-to-action mapping. To get an action out of a decision theory
that does policy selection (because what we really care about is knowing which
action to take), we must *call* the policy on the actual observation.

From the expected utility formula of the decision theory,
you can tell action vs policy selection by seeing what variable comes beneath
the $\operatorname{arg\,max}$ operator; if it is $a\in\mathcal A$ (or similar) then it is iterating over actions, and if it is $\pi \in \Pi$ (or similar), then it is iterating over policies.

One exception to the above is UDT2, which seems to iterate over *algorithms*.

## Updatelessness

In some decision problems, the agent makes an observation, and has the choice
of updating on this observation before acting. Two examples of this are: in
counterfactual mugging, where the agent makes the observation that the coin has
come up tails; and in the transparent box Newcomb’s problem, where the agent
sees whether the big box is full or empty.

If the decision algorithm updates on the observation, it is *updateful* (a.k.a.
“not updateless”). If it doesn’t update on the observation, it is
*updateless*.

This idea is similar to how in Rawls’s “[veil of ignorance](https://en.wikipedia.org/wiki/Veil_of_ignorance)”, you must pick your
moral principles, societal policies, etc., before you find out who
you are in the world or as if you don’t know who you are in the world.

How can you tell if a decision theory is
updateless? In its expected utility formula, if it conditions
on the observation, it is updateful. In this case
the probability factor looks like
$P(\ldots\mid \ldots, \mathrm{O\small BS} = x)$,
where $x$ is the observation.
If a decision theory is updateless, the conditioning on
“$\mathrm{O\small BS} = x$” is absent.
Updatelessness only makes a difference in decision problems that
have observations.

on uncertainty about where you are:

I think updatelessness is the same as being [uncertain about where your decision algorithm is](http://acritch.com/deserving-trust/#grokking) because you are “ignoring” your observation by not conditioning on it.

https://www.lesswrong.com/posts/Qyix5Z5YPSGYxf7GG/less-wrong-q-and-a-with-eliezer-yudkowsky-video-answers#BrWSWrwaategHEkvh -- when stated like this, it sounds more like logical counterfactuals...

this explanation also emphasizes this: https://www.lesswrong.com/posts/zztyZ4SKy7suZBpbk/another-attempt-to-explain-udt

There seem to be different meanings of "updateless". See the section below,
“What are all the different meanings of ‘updateless’ used in the wild?”, for
more information on this.

## Type of counterfactual

In the course of reasoning about a decision problem, the agent
can construct counterfactuals or hypotheticals like “if I do *this*,
then *that* happens”. There are several different kinds of counterfactuals,
and decision theories are divided among them.

The three types of counterfactuals that will concern us are:

* Causal.
* Conditional/evidential.
* Logical.

The distinctions between these are explained clearly in the [FDT paper](https://arxiv.org/pdf/1710.05060.pdf)
so I recommend reading that.

In the expected utility formula, if the probability factor
looks like
$P(\ldots\mid\ldots, \mathrm{A \small CT}=a)$ then it is evidential;
if it looks like $P(\ldots \mid \ldots, \mathtt{do}(\mathrm{A\small CT}=a))$ then it is causal;

I have seen the logical counterfactual written in many ways:

* $P(\ldots \mid\ldots, \mathtt{do}(\mathrm{\small DT}(\ldots)=\ldots))$ e.g. in the [FDT paper](https://arxiv.org/pdf/1710.05060.pdf), p. 14
* $P(\ldots \mid\ldots, \mathtt{true}(\mathrm{\small DT}(\ldots)=\ldots))$ e.g. in the [FDT paper](https://arxiv.org/pdf/1710.05060.pdf), p. 14
* $P(\ulcorner \mathrm{\small DT}(\ldots)=\ldots\urcorner \mathbin{\Box\kern-7mu\rightarrow} \ldots \mid\ldots)$ e.g. in [Hintze](https://intelligence.org/wp-content/uploads/2014/10/Hintze-Problem-Class-Dominance-In-Predictive-Dilemmas.pdf), p. 4
* $P(\ulcorner \mathrm{\small DT}(\ldots)=\ldots\urcorner \triangleright \ldots \mid\ldots)$ e.g. on [Arbital](https://arbital.com/p/logical_dt/?l=5d6)

## Other dimensions that I ignore

* reflectively consistent: I think this is about whether an agent
  would use precommitment mechanisms or self-modify to use a
  different decision theory.  Can this be seen immediately from
  the expected utility formula? If not, it might be unlike the
  other three above. My current guess is that reflective consistency
  is a higher-level property that follows from the above three.
* emphasis on graphical models
* reflective consistency ???
* dynamic consistency??? https://intelligence.org/files/TDT.pdf
* a lot of recent developments like plugging in logical inductors into the decision theory.

# Comparison table along the given dimensions

Given the comparison dimensions above, the decision theories can be summarized as follows:

|Decision theory|Outermost iteration|Updateless|Type of counterfactual|
|--------------------------|------------|--------------|-------------|
|Updateless decision theory 1 (UDT1)|action|yes|logical|
|Updateless decision theory 1.1 (UDT1.1)|policy|yes|logical|
|Updateless decision theory 2 (UDT2)|algorithm|yes|logical|
|Functional decision theory, iterating over actions (FDT-action)|action|yes|logical|
|Functional decision theory, iterating over policies (FDT-policy)|policy|yes|logical|
|Logical decision theory (LDT)|unspecified|unspecified|logical|
|Timeless decision theory (TDT)|action|no|logical|
|Causal decision theory (CDT)|action|no|causal|
|Evidential decision theory (EDT, “naive EDT”)|action|no|conditional|

The general “shape” of the expected utility formulas will be:

$$\operatorname*{arg\,max}_{\color{blue}{\text{outermost}\\ \ \text{iteration}}} \sum_{j=1}^N \mathcal U(o_j)\cdot P(\mathrm{O\small UTCOME}=o_j \mid \color{red}{\text{updatelessness}}, \color{green}{\text{counterfactual}})$$

Or sometimes:

$$\operatorname*{arg\,max}_{\color{blue}{\text{outermost}\\ \ \text{iteration}}} \sum_{j=1}^N \mathcal U(o_j)\cdot P(\color{green}{\text{counterfactual}} \mathbin{\Box\kern-7mu\rightarrow} \mathrm{O\small UTCOME}=o_j \mid \color{red}{\text{updatelessness}})$$

# Explanations of each decision theory

This section elaborates on the comparison above by giving an explicit expected value formula for each decision theory and explaining why each cell in the table takes that particular value.

## UDT1 and FDT (iterate over actions)

I will describe UDT1 and FDT’s action variant together, because I think they
give the same decisions. The main differences between the two seem to be (1)
the way they are formalized, where FDT uses graphical models and UDT1 uses some
kind of non-graphical mathematical intuition module (or something); and (2) the
naming, where UDT1 emphasizes the “updateless” aspect and FDT emphasizes the
logical counterfactual aspect.

[UDT1](http://lesswrong.com/lw/15m/towards_a_new_decision_theory/)

also see https://casparoesterheld.files.wordpress.com/2017/08/updateless_decision_theory-1.pdf

$$\mathrm{UDT}_1(P,x) = \operatorname*{arg\,max}_{a\in \mathcal A} \sum_{j=1}^N \mathcal U(o_j)\cdot P(\mathrm{O\small UTCOME}=o_j \mid )$$

From the FDT paper:

$$\begin{align}\mathrm{FDT}(P,G,x) &= \operatorname*{arg\,max}_{a \in \mathcal A} \mathbb E(\mathcal U(\mathrm{O\small UTCOME}) \mid \mathtt{do}(\mathrm{\small FDT}(\underline P,\underline G,\underline x)=a)) \\ &= \operatorname*{arg\,max}_{a\in \mathcal A} \sum_{j=1}^N \mathcal U(o_j)\cdot P(\mathrm{O\small UTCOME}=o_j\mid \mathtt{do}(\mathrm{\small FDT}(\underline P, \underline G, \underline x) = a))\end{align}$$

(see [comment](https://www.greaterwrong.com/posts/2THFt7BChfCgwYDeA/let-s-discuss-functional-decision-theory/comment/6xLQAfYu4rJTN3MWJ))

(see [comment](https://www.lesswrong.com/posts/9BYo6Q9qBMXWLjqPS/miri-decisions-are-for-making-bad-outcomes-inconsistent#JJBt6eitzzrWPukSp "“accepting FDT doesn’t necessarily require a commitment to some of the philosophical ideas associated with updatelessness and logical prior probability that MIRI, Wei Dai, or other FDT proponents happen to accept”"))

also see https://www.lesswrong.com/posts/cAMhvPgMQJzhrpNdN/publication-of-anthropic-decision-theory#nW4bPcheDJ4ZAHCNb

Tyrrell McAllister writes UDT1 like this:

$$\operatorname*{arg\,max}_{Y\in \mathbf Y} \sum_{E\in\mathbf E} M(X,Y,E)\cdot U(E)$$

Here $M$ is the mathematical intuition that gives ...

In our own notation, this might look like TODO: give expression

I’m not sure if this is right. But the important point is that UDT1:

* Does action selection due to the $a\in\mathcal A$ or $Y\in\mathbf Y$
* Uses logical counterfactuals, either via FDT-like notation or via the mathematical intuition
* Does not condition on the observation, because there is no
  $\mathrm{O\small BS}=x$ (the McAllister paper doesn’t even mention observations)

The above three explain the values for UDT1 in the comparison table.

## UDT1.1 and FDT (iterate over policies)

[UDT1.1](http://lesswrong.com/lw/1s5/explicit_optimization_of_global_strategy_fixing_a/), [Hintze](https://intelligence.org/wp-content/uploads/2014/10/Hintze-Problem-Class-Dominance-In-Predictive-Dilemmas.pdf)

also see https://casparoesterheld.files.wordpress.com/2017/08/updateless_decision_theory-1.pdf

(see [comment](https://www.greaterwrong.com/posts/2THFt7BChfCgwYDeA/let-s-discuss-functional-decision-theory/comment/6xLQAfYu4rJTN3MWJ))

(see [comment](https://www.lesswrong.com/posts/9BYo6Q9qBMXWLjqPS/miri-decisions-are-for-making-bad-outcomes-inconsistent#JJBt6eitzzrWPukSp "“accepting FDT doesn’t necessarily require a commitment to some of the philosophical ideas associated with updatelessness and logical prior probability that MIRI, Wei Dai, or other FDT proponents happen to accept”"))

also see https://www.lesswrong.com/posts/cAMhvPgMQJzhrpNdN/publication-of-anthropic-decision-theory#nW4bPcheDJ4ZAHCNb

In UDT1.1, instead of iterating over actions to find the best one, we iterate over *policies* (mappings from observations to actions).

$$(\mathrm{UDT}_{1.1}(P,x))(x) = \left(\operatorname*{arg\,max}_{\pi\in \Pi} \sum_{j=1}^N \mathcal U(o_j)\cdot P(\mathrm{O\small UTCOME}=o_j \mid \mathtt{true}(\mathrm{\small UDT}_{1.1}(\underline P, \underline x) = \pi))\right)(x)$$

On the right hand side, the large expression on the left (the part inside and including the $\operatorname{arg\,max}$) returns a policy, so to get the action we call the policy on the observation $x$.

[FDT paper](https://arxiv.org/pdf/1710.05060.pdf) (p. 11, footnote 7):

> In the authors’ preferred formalization of FDT, agents actually iterate over
> *policies* (mappings from observations to actions) rather than actions. This
> makes a difference in certain multi-agent dilemmas, but will not make a
> difference in this paper.

Again using Tyrrell McAllister’s notation, UDT1.1 looks like:

$$\mathrm{UDT}_{1.1}(\mathbf X, \mathbf Y, \mathbf E, M, \mathbf I) = \operatorname*{arg\,max}_{f\in \mathbf I} \sum_{E\in\mathbf E} M(f,E)\cdot U(E)$$

Hintze writes UDT as follows:

$$\operatorname*{arg\,max}_{f} \sum_{j=1}^n \mathcal U(o_j) \cdot P(\ulcorner \mathrm{UDT} := f : s\mapsto a \urcorner \mathbin{\Box\kern-7mu\rightarrow} o_j)$$

Again what is important here is that UDT1.1:

* Does action selection because the outermost iteration is over policies
* Uses logical counterfactuals
* Does not condition on the observation

## TDT

My understanding of TDT is mainly from
[Hintze](https://intelligence.org/wp-content/uploads/2014/10/Hintze-Problem-Class-Dominance-In-Predictive-Dilemmas.pdf).
I am aware of the [TDT paper](https://intelligence.org/files/TDT.pdf) and skimmed it a while back,
but did not revisit it in the course of writing this post.

[Hintze](https://intelligence.org/wp-content/uploads/2014/10/Hintze-Problem-Class-Dominance-In-Predictive-Dilemmas.pdf "“TDP’s failure on the Curious Benefactor is straightforward. Upon seeing the coinflip has come up tails, it updates on the sensory data and realizes that it is in the causal branch where there is no possibility of getting a million.”") p. 11

$$\mathrm{TDT}(P,x) = \operatorname*{arg\,max}_{a\in\mathcal A} \sum_{j=1}^N \mathcal U(o_j)\cdot P(\mathrm{O\small UTCOME} = o_j \mid \mathrm{O\small BS}=x, \mathtt{true}(\mathrm{\small TDT}(\underline P, \underline x) = a))$$

TDT performs action selection as can be seen from the “$\operatorname*{arg\,max}_{a\in\mathcal A}$”.
It is updateful because the probability factor looks like
$P(\ldots \mid \mathrm{O\small BS}=x, \ldots)$, i.e. it conditions on
$\mathrm{O\small BS}=x$.
It uses logical counterfactuals because of the
$\mathtt{true}(\mathrm{\small TDT}(\underline P, \underline x) = a)$.

this page says TDT is updateful https://arbital.com/p/updateless_dt/

https://intelligence.org/2017/03/18/new-paper-cheating-death-in-damascus/ describes TDT as “a theory by MIRI senior researcher Eliezer Yudkowsky that made the mistake of conditioning on observations”.

## UDT2

I know very little about UDT2, but based on [this
comment](http://lesswrong.com/lw/jhj/functional_side_effects/adhy) by Wei Dai
and [this
post](https://www.lesswrong.com/posts/wXxPmc9W6kPb6i7vj/notes-on-logical-priors-from-the-miri-workshop)
by Vladimir Slepnev, it seems to iterate over algorithms rather than actions or
policies, and I am assuming it didn’t abandon updatelessness and logical counterfactuals.

The following search queries might have more information:

* [“UDT2”](https://www.greaterwrong.com/search?q=%22UDT2%22)
* [site:agentfoundations.org “UDT2”](https://www.google.com/search?q=site%3Aagentfoundations.org%20%22UDT2%22)
* [site:lesswrong.com “UDT2”](https://www.google.com/search?q=site%3Alesswrong.com%20%22UDT2%22)

## LDT

LDT seems to be an umbrella decision theory that only requires the use of
logical counterfactuals, leaving the iteration type and updatelessness
unspecified. So my understanding is that UDT1, UDT1.1, UDT2, FDT, and TDT are
all logical decision theories.
See [this Arbital page](https://arbital.com/p/logical_dt/?l=5gc), which says:

> “Logical decision theories” are really a family of recently proposed decision
> theories, none of which stands out as being clearly ahead of the others in
> all regards, but which are allegedly all better than causal decision theory.

The page also calls TDT a logical decision theory (listed under “non-general
but useful logical decision theories”).

## CDT

$$\begin{align}\mathrm{CDT}(P,G,x) &= \operatorname*{arg\,max}_{a \in\mathcal A} \mathbb E(\mathcal U(\mathrm{O\small UTCOME}) \mid \mathtt{do}(\mathrm{A\small CT}=a), \mathrm{O\small BS} = x) \\ &= \operatorname*{arg\,max}_{a \in\mathcal A} \sum_{j=1}^N \mathcal U(o_j)\cdot P(\mathrm{O\small UTCOME} = o_j \mid \mathtt{do}(\mathrm{A\small CT}=a), \mathrm{O\small BS} = x)\end{align}$$

## EDT

$$\begin{align}\mathrm{EDT}(P,x) &= \operatorname*{arg\,max}_{a \in\mathcal A} \mathbb E(\mathcal U(\mathrm{O\small UTCOME}) \mid \mathrm{O\small BS} = x, \mathrm{A\small CT}=a) \\ &= \operatorname*{arg\,max}_{a \in\mathcal A} \sum_{j=1}^N \mathcal U(o_j)\cdot P(\mathrm{O\small UTCOME} = o_j \mid \mathrm{O\small BS} = x, \mathrm{A\small CT}=a)\end{align}$$

# Comparison on specific decision problems

If two decision theories are actually different, there should be some decision problem where they return different answers.

I think the FDT paper does a great job of distinguishing the logical-counterfactual decision theories from EDT and CDT.
However, it doesn’t distinguish between different logical-counterfactual decision theories.

The following is a table that shows the disagreements between decision theories.
For each pair of decision theories specified by a row and column, the decision problem named in the cell is one where the decision theories return different answers.
The diagonal is blank because the decision theories are the same. The lower left triangle is blank because it repeats the entries in the mirror image (along the diagonal) spots.

| |UDT1.1/FDT-policy|UDT1/FDT-action|TDT|EDT|CDT|
|:---:|:----------:|:----------:|:----------:|:----------:|:----------:|
|**UDT1.1/FDT-policy**|--|Number assignment problem described in the [UDT1.1 post](https://www.lesswrong.com/posts/g8xh9R7RaNitKtkaa/explicit-optimization-of-global-strategy-fixing-a-bug-in) (both UDT1 copies output “A”, the UDT1.1 copies output “A” and “B”)|[Counterfactual mugging](https://wiki.lesswrong.com/wiki/Counterfactual_mugging) (TDT refuses, UDT1.1 pays)|[Parfit’s hitchhiker](https://wiki.lesswrong.com/wiki/Parfit%27s_hitchhiker) (EDT refuses, UDT1.1 pays)|[Newcomb’s problem](https://wiki.lesswrong.com/wiki/Newcomb%27s_problem) (CDT two-boxes, UDT1.1 one-boxes)|
|**UDT1/FDT-action**|--|--|counterfactual mugging? (TDT refuses, UDT1 pays?)|Parfit’s hitchhiker (EDT refuses, UDT1 pays)|Newcomb’s problem (CDT two-boxes, UDT1 one-boxes)|
|**TDT**|--|--|--|Parfit’s hitchhiker (EDT refuses, TDT pays)|Newcomb’s problem (CDT two-boxes, TDT one-boxes)|
|**EDT**|--|--|--|--|Newcomb’s problem (CDT two-boxes, EDT one-boxes)|
|**CDT**|--|--|--|--|--|


## Distinguishing TDT from UDT1.1

curious benefactor/counterfactual mugging

## Distinguishing UDT1 from UDT1.1

the number assignment game in Wei Dai’s UDT1.1 post.

## Distinguishing TDT from UDT1

# Remaining questions

## Does policy selection imply updatelessness?

There was no decision theory in this post that did policy selection and was
simultaneously updateful. Is this always the case, or is it an accident of
history (i.e. that UDT1, with its updatelessness, came first, and the fix to
UDT1.1 involved policy selection, so we never saw a decision theory that used
policy selection without updatelessness)?

On the one hand, I can reason from the expected utility formula: I can just
modify the UDT1.1 formula to condition on the observation, forcing it to be
updateful.

On the other hand,

> Updateless decision theories maximize over policies -- mappings from sense
> inputs to actions -- instead of using their sense inputs to update their
> beliefs, and then selecting actions using the updated model.

from https://arbital.com/p/updateless_dt/

and:

> An important feature quietly introduced in the above formula for $\mathsf Q$,
> is that $\mathsf Q$ chooses *policies* (mappings from sensory observations
> $s$ to actions) rather than outputting actions directly. This makes
> functional decision theory updateless, a feature with deep ramifications and
> justifications that pretty much require digging into the longer articles.

from https://arbital.com/p/logical_dt/?l=5gc

From [“Toward Idealized Decision Theory”](https://arxiv.org/pdf/1507.01986.pdf) (p. 8):

> A decision theory that identifies the best *policy* in a given scenario (and
> prescribes acting accordingly) better captures the notion of “the best
> available action” than a decision theory which considers actions alone.
> Variants of decision theory using policy selection are “updateless” (as
> agents following the prescriptions of policy selection pick a policy before
> they update on their observations), and this is the first of two ideas \[the
> other being logical counterfactuals\] behind the *updateless decision theory*
> (UDT) of Dai ([2009](http://lesswrong.com/lw/15m/towards_a_new_decision_theory/)).

This leads me to think policy selection implies updatelessness, or policy selection and updateless are somehow lumped together, or that there
is a meaning of the term “updateless” that *means* “does policy selection”.
See also the next question in this section.

also talk about policy-based CDT, which seems to allow leaving updatelessness
unspecified.

## What are all the different meanings of “updateless” used in the wild?

I think i need to break down the idea of “updatelessness” further. My own understanding
is that it’s just whether or not you condition on the sense date inside the probability
part of the expected utility formula. So under this interpretation, all versions of
TDT is not updateless. But Caspar uses “updateless” for anything that doesn’t need
precommitments to win Parfit’s hitchhiker, making TDT updateless.

Plus, if FDT is updateless, then Rob’s comment
doesn’t make sense; what are these philosophical issues around updatelessness that FDT
doesn’t need to accept?

Also by the previous subsection, “updateless” might sometimes be used to mean
“does policy selection”. If this is the case, then some versions of FDT are
“updateless” while others are not.

https://www.lesswrong.com/posts/pneKTZG9KqnSe2RdQ/two-types-of-updatelessness abram demski distinguishes between “all-upside updatelessness” and “mixed-upside updatelessness”. Post also talks about policy selection as distinct from updatelessness.

https://agentfoundations.org/item?id=1711 apparently there is a parameter $f$ here that determines the level of updatelessness.

“Lately there’s been a bit more doubt about updatelessness (in full generality instead of the partial version attained by policy selection) as being an achievable desiderata.” https://agentfoundations.org/item?id=1797 So this also seems to mean that policy selection doesn’t necessarily imply updatelessness.

“An updateless agent is one that does not update on its observations, but instead chooses what action it wants itself to output upon being input those observations.” https://agentfoundations.org/item?id=1689 The post distinguishes between empirical updatelessness and logical updatelessness.

page 3 of https://github.com/tsvibt/public-pdfs/blob/master/decision-theory/notation/main.pdf talks about being “updateless with respect to $o$” for some observation $o$.

## Quoting/dequoting

* I’m not totally clear on all the intricacies of quoting/dequoting/quining/recursively referring to your decision algorithm.

## Other decision theories

Here are some other decision theories that I’ve encountered, but for which I
don’t know how how to fill in the values in the outermost
iteration/updateless/type of counterfactual table.

* EDT with tickle defense
* Drescher’s in _Good and Real_
  “despite being motivated by similar intuitions in Newcomblike cases, it is unclear whether or not the similarity between Drescher-style subjunctive dependence and FDT-style subjunctive dependence is merely verbal.” https://philpapers.org/archive/BARWDT-3.pdf
* Policy-based CDT (see [Barnett](https://philpapers.org/archive/BARWDT-3.pdf) pp. 58-59)


# Other comparisons

Here are some existing comparisons between decision theories that I found
useful, along with reasons why I felt the current post was needed.

* [“Decision-theoretic problems and Theories; An (Incomplete) comparative list”](https://www.lesswrong.com/posts/cWEhuXQBxRwxmhER5/decision-theoretic-problems-and-theories-an-incomplete) by somervta.
  This list is useful and modern but doesn’t include the different versions of UDT and FDT.
* [“A comprehensive list of decision
  theories”](https://casparoesterheld.com/a-comprehensive-list-of-decision-theories/)
  by Caspar Oesterheld and/or Johannes Treutlein. I think my motivation is
  different from that of the author(s) of this list; I mainly want to
  distinguish between all the UDTs, TDT, and FDT, so my tables and columns of
  those tables are chosen in a way so as to make the differences apparent.
* [“Problem Class Dominance in Predictive
  Dilemmas”](https://intelligence.org/wp-content/uploads/2014/10/Hintze-Problem-Class-Dominance-In-Predictive-Dilemmas.pdf)
  by Daniel Hintze. This paper is from 2014 so doesn’t include the FDT/LDT
  terminology, and also doesn’t include the various versions of UDT.
* [“Timeline of decision theory”](https://timelines.issarice.com/wiki/Timeline_of_decision_theory).
  This is an incomplete timeline I’ve been working on sporadically. It gives a
  chronological ordering of some decision theories and decision problems with a
  focus on logical-counterfactual decision theories, but doesn't really compare
  them.

# Meta information on this post

## Version history

* 2018-07-23 to 2018-08-10: Initial work on this post.
* 2018-08-11 to 2018-10-09: Post sat dormant.
* 2018-10-10: copyediting.
* ??: Initial version published.

## License

To the extent possible under law, Issa Rice has waived all copyright and
related or neighboring rights to the content in this post. This work is
published from: United States. See the [CC0 1.0 Universal Public Domain
Dedication](https://creativecommons.org/publicdomain/zero/1.0/) for more information.
