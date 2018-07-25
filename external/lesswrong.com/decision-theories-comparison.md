% Comparison of decision theories
% Issa Rice
% 2018-07-24

# Comparison dimensions

My main motivation is to try to separate my understanding of TDT, UDT, and FDT.
Before trying to work on this comparison, they all seemed similar in that they considered acausal or logical correlations.

Therefore, I focus on three dimensions for comparison that I think best differentiate between these decision theories.

## Outermost iteration

action selection vs policy selection: when your decision algorithm runs,
does it output an action or a policy (a mapping from observations to
actions)?

From the expected utility formula of the decision theory,
you can tell action vs policy by seeing what variable comes beneath
the $\operatorname{arg\,max}$ operator; if it is $a\in\mathcal A$ then it is iterating over actions, and if it is $\pi \in \Pi$, then it is iterating over policies.
Even in the case of policy selection, what we eventually need to do is perform an action, so we call the policy that is returned to get the action.

## Updatelessness

updatelessness: before your decision algorithm returns an output,
does it first update on the observation that it is given? If so,
it is not updateless; if it doesn't it is updateless. This is
similar to how in Rawls's "veil of ignorance", you must pick your
moral principles, societal policies, etc., before you find out who
you are in the world.

I think updatelessness is the same as being [uncertain about where your decision algorithm is](http://acritch.com/deserving-trust/#grokking) because you are "ignoring" your observation by not conditioning on it.

How can you tell if a decision theory is
updateless? In its expected utility formula, if it conditions
on the data, i.e. the probability factor looks like
$P(\ldots\mid \ldots, \mathrm{O\small BS} = x)$,
where $x$ is the observation, then it is not updateless.

## Type of counterfactual

type of counterfactual used: as your decision algorithm runs, it might
construct hypotheticals (models of the world),
like "if I do _this_, then _that_ happens".

In the expected utility formula, if the probability factor
looks like
$P(\ldots\mid\ldots, \mathrm{A \small CT}=a)$ then it is evidential;
if it looks like $P(\ldots \mid \ldots, \mathtt{do}(\mathrm{A\small CT}=a))$ then it is causal;

I have seen the logical counterfactual written in many ways:

* $P(\ldots \mid\ldots, \mathtt{do}(\mathrm{\small FDT}(\ldots)=\ldots))$ e.g. in the [FDT paper](https://arxiv.org/pdf/1710.05060.pdf)
* $P(\ldots \mid\ldots, \mathtt{true}(\mathrm{\small FDT}(\ldots)=\ldots))$ e.g. in the [FDT paper](https://arxiv.org/pdf/1710.05060.pdf)
* $P(\ulcorner \mathrm{\small FDT}(\ldots)=\ldots\urcorner \mathbin{\Box\!\!\!\to} \ldots \mid\ldots)$ e.g. in [Hintze](https://intelligence.org/wp-content/uploads/2014/10/Hintze-Problem-Class-Dominance-In-Predictive-Dilemmas.pdf), p. 4
* $P(\ulcorner \mathrm{\small FDT}(\ldots)=\ldots\urcorner \triangleright \ldots \mid\ldots)$ e.g. on [Arbital](https://arbital.com/p/logical_dt/?l=5d6)

## Other dimensions that I ignore

* reflectively consistent: I think this is about whether an agent
  would use precommitment mechanisms or self-modify to use a
  different decision theory.  Can this be seen immediately from
  the expected utility formula? If not, it might be unlike the
  other three above.
* emphasis on graphical models
* reflective consistency ???
* dynamic consistency??? https://intelligence.org/files/TDT.pdf

# Comparison table along the given dimensions

|Decision theory|Outermost iteration|Updateless|Type of counterfactual|
|-------------|-----------------|-------------------------------|------------------------|
|UDT1|action|yes|logical|
|UDT1.1|policy|yes|logical|
|UDT2|algorithm|yes|logical|
|FDT (iterate over actions)|action|yes|logical|
|FDT (iterate over policies)|policy|yes|logical|
|Logical decision theory|unspecified|unspecified|logical|
|Policy-based CDT|policy|unspecified|causal|
|TDT|action|no|logical|
|CDT|action|no|causal|
|EDT ("naive EDT")|action|no|conditional|
|EDT with tickle defense|action|no?|?|
|Drescher's in _Good and Real_ |?|?|logical|

# Explanations of each decision theory

This section elaborates on the comparison above by giving an explicit expected value formula for each decision theory and explaining why each cell in the table takes that particular value.

## UDT1 and FDT (iterate over actions)

I will describe UDT1 and FDT's action variant together, because I think they
give the same decisions. The main differences between the two seem to be (1)
the way they are formalized, where FDT uses graphical models and UDT1 uses some
kind of non-graphical mathematical intuition module (or something); and (2) the
naming, where UDT1 emphasizes the "updateless" aspect and FDT emphasizes the
logical counterfactual aspect.

[UDT1](http://lesswrong.com/lw/15m/towards_a_new_decision_theory/)

$$\mathrm{UDT}_1(P,x) = \operatorname*{arg\,max}_{a\in \mathcal A} \sum_{j=1}^N \mathcal U(o_j)\cdot P(\mathrm{O\small UTCOME}=o_j \mid )$$

From the FDT paper:

$$\begin{align}\mathrm{FDT}(P,G,x) &= \operatorname*{arg\,max}_{a \in \mathcal A} \mathbb E(\mathcal U(\mathrm{O\small UTCOME}) \mid \mathtt{do}({\rm {\small FDT}}(\underline P,\underline G,\underline x)=a)) \\ &= \operatorname*{arg\,max}_{a\in \mathcal A} \sum_{j=1}^N \mathcal U(o_j)\cdot P(\mathrm{O\small UTCOME}=o_j\mid \mathtt{do}(\mathrm{\small FDT}(\underline P, \underline G, \underline x) = a))\end{align}$$

(see [comment](https://www.greaterwrong.com/posts/2THFt7BChfCgwYDeA/let-s-discuss-functional-decision-theory/comment/6xLQAfYu4rJTN3MWJ))

(see [comment](https://www.lesswrong.com/posts/9BYo6Q9qBMXWLjqPS/miri-decisions-are-for-making-bad-outcomes-inconsistent#JJBt6eitzzrWPukSp "“accepting FDT doesn't necessarily require a commitment to some of the philosophical ideas associated with updatelessness and logical prior probability that MIRI, Wei Dai, or other FDT proponents happen to accept”"))

## UDT1.1 and FDT (iterate over policies)

[UDT1.1](http://lesswrong.com/lw/1s5/explicit_optimization_of_global_strategy_fixing_a/), [Hintze](https://intelligence.org/wp-content/uploads/2014/10/Hintze-Problem-Class-Dominance-In-Predictive-Dilemmas.pdf)

(see [comment](https://www.greaterwrong.com/posts/2THFt7BChfCgwYDeA/let-s-discuss-functional-decision-theory/comment/6xLQAfYu4rJTN3MWJ))

(see [comment](https://www.lesswrong.com/posts/9BYo6Q9qBMXWLjqPS/miri-decisions-are-for-making-bad-outcomes-inconsistent#JJBt6eitzzrWPukSp "“accepting FDT doesn't necessarily require a commitment to some of the philosophical ideas associated with updatelessness and logical prior probability that MIRI, Wei Dai, or other FDT proponents happen to accept”"))

In UDT1.1, instead of iterating over actions to find the best one, we iterate over *policies* (mappings from observations to actions).

$$(\mathrm{UDT}_{1.1}(P,x))(x) = \left(\operatorname*{arg\,max}_{\pi\in \Pi} \sum_{j=1}^N \mathcal U(o_j)\cdot P(\mathrm{O\small UTCOME}=o_j \mid \mathtt{true}(\mathrm{\small UDT}_{1.1}(\underline P, \underline x) = \pi))\right)(x)$$

On the right hand side, the large expression on the left (the part inside and including the $\operatorname{arg\,max}$) returns a policy, so to get the action we call the policy on the observation $x$.

[FDT paper](https://arxiv.org/pdf/1710.05060.pdf) (p. 11, footnote 7):

> In the authors' preferred formalization of FDT, agents actually iterate over
> *policies* (mappings from observations to actions) rather than actions. This
> makes a difference in certain multi-agent dilemmas, but will not make a
> difference in this paper.

## TDT

(see [Hintze](https://intelligence.org/wp-content/uploads/2014/10/Hintze-Problem-Class-Dominance-In-Predictive-Dilemmas.pdf "“TDP's failure on the Curious Benefactor is straightforward. Upon seeing the coinflip has come up tails, it updates on the sensory data and realizes that it is in the causal branch where there is no possibility of getting a million.”") p. 11)

$$\mathrm{TDT}(P,x) = \operatorname*{arg\,max}_{a\in\mathcal A} \sum_{j=1}^N \mathcal U(o_j)\cdot P(\mathrm{O\small UTCOME} = o_j \mid \mathrm{O\small BS}=x, \mathtt{true}(\mathrm{\small TDT}(\underline P, \underline x) = a))$$

## UDT2

iterate over algorithms?

## LDT

See [arbital page](https://arbital.com/p/logical_dt/?l=5gc)

## Policy-based CDT

(see [Barnett](https://philpapers.org/archive/BARWDT-3.pdf) pp. 58-59)

## CDT

$$\begin{align}\mathrm{CDT}(P,G,x) &= \operatorname*{arg\,max}_{a \in\mathcal A} \mathbb E(\mathcal U(\mathrm{O\small UTCOME}) \mid \mathtt{do}(\mathrm{A\small CT}=a), \mathrm{O\small BS} = x) \\ &= \operatorname*{arg\,max}_{a \in\mathcal A} \sum_{j=1}^N \mathcal U(o_j)\cdot P(\mathrm{O\small UTCOME} = o_j \mid \mathtt{do}(\mathrm{A\small CT}=a), \mathrm{O\small BS} = x)\end{align}$$

## EDT

$$\begin{align}\mathrm{EDT}(P,x) &= \operatorname*{arg\,max}_{a \in\mathcal A} \mathbb E(\mathcal U(\mathrm{O\small UTCOME}) \mid \mathrm{O\small BS} = x, \mathrm{A\small CT}=a) \\ &= \operatorname*{arg\,max}_{a \in\mathcal A} \sum_{j=1}^N \mathcal U(o_j)\cdot P(\mathrm{O\small UTCOME} = o_j \mid \mathrm{O\small BS} = x, \mathrm{A\small CT}=a)\end{align}$$

I think i need to break down the idea of "updatelessness" further. My own understanding
is that it's just whether or not you condition on the sense date inside the probability
part of the expected utility formula. So under this interpretation, all versions of
FDT are updateless. But Caspar uses "updateless" for anything that doesn't need
precommitments to win Parfit's hitchhiker. Plus, if FDT is updateless, then Rob's comment
doesn't make sense; what are these philosophical issues around updatelessness that FDT
doesn't need to accept?

# Comparison on specific decision problems

If two decision theories are actually different, there should be some decision problem where they return different answers.

I think the FDT paper does a great job of distinguishing the logical-counterfactual decision theories from EDT and CDT.

Table of decision problems where the decision theories specified by a row and column return different answers.
The diagonal is blank because the decision theories are the same. The lower left triangle is blank because it repeats the entry in the mirror image (along the diagonal) spot.

| |UDT1/FDT-action|UDT1.1/FDT-policy|TDT|EDT|CDT|
|:---:|:----------:|:----------:|:----------:|:----------:|:----------:|
|UDT1/FDT-action|--|number assignment game|counter factual mugging?|smoking lesion|Newcomb's problem|
|UDT1.1/FDT-policy|--|--|Counterfactual mugging|smoking lesion|Newcomb's problem|
|TDT|--|--|--|Parfit's hitchhiker|Newcomb's problem|
|EDT|--|--|--|--|Newcomb's problem, smoking lesion|
|CDT|--|--|--|--|--|


## Distinguishing TDT from UDT1.1

curious benefactor/counterfactual mugging

## Distinguishing UDT1 from UDT1.1

the number assignment game in Wei Dai's UDT1.1 post.

## Distinguishing TDT from UDT1



# Other comparions

* https://www.greaterwrong.com/posts/cWEhuXQBxRwxmhER5/decision-theoretic-problems-and-theories-an-incomplete
* https://casparoesterheld.com/a-comprehensive-list-of-decision-theories/ My motivation is different from Caspar's; I mainly want to distinguish between all the UDTs, TDT, and FDT, so my columns are chosen in a way so as to differentiate between these DTs.
* Hintze's paper

