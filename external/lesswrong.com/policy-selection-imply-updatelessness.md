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
