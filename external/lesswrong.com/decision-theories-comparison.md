% Comparison of decision theories
% Issa Rice
% 2018-07-24

# Comparison dimensions

My main motivation is to try to separate my understanding of TDT, UDT, and FDT.
Before trying to work on this comparison, they all seemed similar in that they considered acausal or logical correlations.

Therefore, I focus on three dimensions for this comparison that I think best differentiate between these decision theories.

Some differences decision theories might have:

TODO explain where the "you don't know which instance of the algorithm you are" idea fits in.

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
you are in the world. How can you tell if a decision theory is
updateless? In its expected utility formula, if it conditions
on the data, i.e. the probability factor looks like Pr(...|*s*),
where *s* is the data, then it is not updateless.

## Type of counterfactual

type of counterfactual used: as your decision algorithm runs, it might
construct hypotheticals (models of the world),
like "if I do _this_, then _that_ happens".
In the expected utility formula, if the probability factor
looks like Pr(...|Obs=x, Act=a) then it is evidential;
if it looks like Pr(...|Obs=x, do(Act=a)) then it is causal;
if it looks like Pr(...|do(FDT(...)=a) then it is logical. (?)

## Other dimensions that I ignore

* reflectively consistent: I think this is about whether an agent
  would use precommitment mechanisms or self-modify to use a
  different decision theory.  Can this be seen immediately from
  the expected utility formula? If not, it might be unlike the
  other three above.
* emphasis on graphical models
* reflective consistency ???
* dynamic consistency??? https://intelligence.org/files/TDT.pdf

# Summary table

|Decision theory|Outermost iteration|Updateless|Type of counterfactual|
|-------------|-----------------|-------------------------------|------------------------|
|UDT1|action (see [comment](https://www.greaterwrong.com/posts/2THFt7BChfCgwYDeA/let-s-discuss-functional-decision-theory/comment/6xLQAfYu4rJTN3MWJ))             | yes                           | logical                    |
|UDT1.1|policy (see [comment](https://www.greaterwrong.com/posts/2THFt7BChfCgwYDeA/let-s-discuss-functional-decision-theory/comment/6xLQAfYu4rJTN3MWJ))             | yes                           | logical                    |
|UDT2|algorithm|?|?|
|FDT (iterate over actions)|action (see [comment](https://www.greaterwrong.com/posts/2THFt7BChfCgwYDeA/let-s-discuss-functional-decision-theory/comment/6xLQAfYu4rJTN3MWJ))              | yes (see [comment](https://www.lesswrong.com/posts/9BYo6Q9qBMXWLjqPS/miri-decisions-are-for-making-bad-outcomes-inconsistent#JJBt6eitzzrWPukSp "“accepting FDT doesn't necessarily require a commitment to some of the philosophical ideas associated with updatelessness and logical prior probability that MIRI, Wei Dai, or other FDT proponents happen to accept”"))                           | logical                    |
|FDT (iterate over policies)|policy| yes (see [comment](https://www.lesswrong.com/posts/9BYo6Q9qBMXWLjqPS/miri-decisions-are-for-making-bad-outcomes-inconsistent#JJBt6eitzzrWPukSp "“accepting FDT doesn't necessarily require a commitment to some of the philosophical ideas associated with updatelessness and logical prior probability that MIRI, Wei Dai, or other FDT proponents happen to accept”")) | logical |
|[Logical decision theory](https://arbital.com/p/logical_dt/?l=5gc)|unspecified| unspecified | logical |
|Policy-based CDT|policy| yes, but there is a choice (see [Barnett](https://philpapers.org/archive/BARWDT-3.pdf) pp. 58-59)                          | causal                    |
|TDT |action| no (see [Hintze](https://intelligence.org/wp-content/uploads/2014/10/Hintze-Problem-Class-Dominance-In-Predictive-Dilemmas.pdf "“TDP's failure on the Curious Benefactor is straightforward. Upon seeing the coinflip has come up tails, it updates on the sensory data and realizes that it is in the causal branch where there is no possibility of getting a million.”") p. 11) | logical?|
|CDT |action| no? | causal|
|EDT ("naive EDT") |action| no? | conditional |
|EDT with tickle defense |action| no? | ? |
|Drescher's in _Good and Real_ | ? | ? | logical |

# Explanations of each decision theory

## UDT1

$$\mathrm{UDT}_1(P,x) = \operatorname*{arg\,max}_{a\in \mathcal A} \sum_{o_j \in \mathcal O} u(o_j)\cdot P(\mathrm{O\small UTCOME}=o_j \mid )$$

## UDT1.1

In UDT1.1, instead of iterating over actions to find the best one, we iterate over *policies* (mappings from observations to actions).

$$\mathrm{UDT}_{1.1}(P,x) = \underbrace{\left(\operatorname*{arg\,max}_{\pi\in \Pi} \sum_{o_j \in \mathcal O} u(o_j)\cdot P(\mathrm{O\small UTCOME}=o_j \mid \mathtt{true}(\mathrm{\small UDT}_{1.1}(\underline P, \underline x) = \pi))\right)}_{\text{returns policy}}\underbrace{(x)}_{\text{calls the policy returned}}$$

## UDT 2

iterate over algorithms?

## FDT (iterate over actions)

From the FDT paper:

$$\mathrm{FDT}(P,G,x) = \operatorname*{arg\,max}_{a \in \mathcal A} \mathbb E(V \mid \mathtt{do}({\rm {\small FDT}}(\underline P,\underline G,\underline x)=a))$$

## CDT

$$\begin{align}\mathrm{CDT}(P,G,x) &= \operatorname*{arg\,max}_{a \in\mathcal A} \mathbb E(V \mid \mathtt{do}(\mathrm {Act} = a), \mathrm{Obs} = x) \\ &= \operatorname*{arg\,max}_{a \in\mathcal A} \sum_{o_j \in \mathcal O} u(o_j)\cdot P(\mathrm{Outcome} = o_j \mid \mathtt{do}(\mathrm{Act} = a), \mathrm{Obs} = x)\end{align}$$

## EDT

$$\begin{align}\mathrm{EDT}(P,x) &= \operatorname*{arg\,max}_{a \in\mathcal A} \mathbb E(V \mid \mathrm {Act} = a, \mathrm{Obs} = x) \\ &= \operatorname*{arg\,max}_{a \in\mathcal A} \sum_{o_j \in \mathcal O} u(o_j)\cdot P(\mathrm{O\small UTCOME} = o_j \mid \mathrm{Act} = a, \mathrm{Obs} = x)\end{align}$$

I think i need to break down the idea of "updatelessness" further. My own understanding
is that it's just whether or not you condition on the sense date inside the probability
part of the expected utility formula. So under this interpretation, all versions of
FDT are updateless. But Caspar uses "updateless" for anything that doesn't need
precommitments to win Parfit's hitchhiker. Plus, if FDT is updateless, then Rob's comment
doesn't make sense; what are these philosophical issues around updatelessness that FDT
doesn't need to accept?

# Other comparions

* https://www.greaterwrong.com/posts/cWEhuXQBxRwxmhER5/decision-theoretic-problems-and-theories-an-incomplete
* https://casparoesterheld.com/a-comprehensive-list-of-decision-theories/ My motivation is different from Caspar's; I mainly want to distinguish between all the UDTs, TDT, and FDT, so my columns are chosen in a way so as to differentiate between these DTs.
* Hintze's paper

