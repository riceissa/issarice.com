# Plausible cases for HRAD work, and locating the crux in the "realism about rationality" debate

This post is my attempt to summarize and distill all of the major public debates about MIRI's [highly reliable agent designs](https://intelligence.org/files/TechnicalAgenda.pdf) (HRAD) work (which includes work on decision theory), including the discussions in [Realism about rationality](https://www.lesswrong.com/posts/suxvE2ddnYMPJN9HD/realism-about-rationality) and Daniel Dewey's [My current thoughts on MIRI's "highly reliable agent design" work](https://forum.effectivealtruism.org/posts/SEL9PW8jozrvLnkb4/my-current-thoughts-on-miri-s-highly-reliable-agent-design). Part of the difficulty with discussing HRAD work is that it's not even clear what the disagreement is about, so my summary takes the form of multiple possible "worlds" we might be in; each world consists of a positive case for doing HRAD work, along with the potential objections to that case.

## Clarifying some terms

Before describing the various worlds, I want to present some distinctions that have come up in discussions about HRAD.

### Precise vs imprecise theory

### Levels of abstraction vs levels of indirection

- "2+ levels"

### Building agents from the ground up vs understanding the behavior of rational agents and predicting what they will do

This distinction comes from Abram Demski's [comment](https://www.greaterwrong.com/posts/suxvE2ddnYMPJN9HD/realism-about-rationality/comment/3f6fadtcv8FsgwKsz).



## World 1

### Case for HRAD

The goal of HRAD research is to generally become less confused about things like counterfactual reasoning and logical uncertainty. Becoming less confused about these things will help AGI builders avoid, detect, and fix safety issues; predict or explain safety issues; and help us be satisfied that the AGI is doing what we want.

For this case, it is not important for the final product of HRAD to be a precise theory. Even if the final theory of embedded agency is imprecise, or even if there *is no* "final say" on the topic, if we are merely much less confused than we are now, that is still good enough to help us ensure AI systems are aligned.

### Why I think we might be in this world

The main reason I think we might be in this world is that people at MIRI frequently seem to be saying something like it. However, they also seem to be saying different things in other places, so I'm not confident we are actually in this world. Here are some examples:

- [Eliezer Yudkowsky](https://intelligence.org/files/OpenPhil2016Supplement.pdf#page=13): "Techniques you can actually adapt in a safe AI, come the day, will probably have very simple cores — the sort of core concept that takes up three paragraphs, where any reviewer who didn’t spend five years struggling on the problem themselves will think, “Oh I could have thought of that.” Someday there may be a book full of clever and difficult things to say about the simple core — contrast the simplicity of the core concept of causal models, versus the complexity of proving all the clever things Judea Pearl had to say about causal models. But the planetary benefit is mainly from posing understandable problems crisply enough so that people can see they are open, and then from the simpler abstract properties of a found solution — complicated aspects will not carry over to real AIs later."
- [Rob Bensinger](https://www.greaterwrong.com/posts/uKbxi2EJ3KBNRDGpL/comment-on-decision-theory): "We’re working on decision theory because there’s a cluster of confusing issues here (e.g., counterfactuals, updatelessness, coordination) that represent a lot of holes or anomalies in our current best understanding of what high-quality reasoning is and how it works." and phrases like "developing an understanding of roughly what counterfactuals are and how they work" and "very roughly how/why it works"  -- This post then doesn't really specify whether or not the final output is expected to be precise. (The analogy with probability theory and rockets gestures at precise theories, but the post doesn't come out and say it.)
- [Abram Demski](https://www.lesswrong.com/posts/suxvE2ddnYMPJN9HD/realism-about-rationality?commentId=XEbNPAyvjpTcGufLm): "I don't think there's a true rationality out there in the world, or a true decision theory out there in the world, or even a true notion of intelligence out there in the world. I work on agent foundations because there's *still something I'm confused about* even after that, and furthermore, AI safety work seems fairly hopeless while still so radically confused about the-phenomena-which-we-use-intelligence-and-rationality-and-agency-and-decision-theory-to-describe."
- [Nate Soares](https://forum.effectivealtruism.org/posts/SEL9PW8jozrvLnkb4/my-current-thoughts-on-miri-s-highly-reliable-agent-design?commentId=D3PDv7kqJuByt8TRr): "The main case for HRAD problems is that we expect them to help in a gestalt way with many different known failure modes (and, plausibly, unknown ones). E.g., 'developing a basic understanding of counterfactual reasoning improves our ability to understand the first AGI systems in a general way, and if we understand AGI better it's likelier we can build systems to address deception, edge instantiation, goal instability, and a number of other problems'."
- In the [deconfusion](https://intelligence.org/2018/11/22/2018-update-our-new-research-directions/#section2) section of MIRI's 2018 update, some of the examples of deconfusion are not precise/mathematical in nature (e.g. see the paragraph starting with "In 1998, conversations about AI risk and technological singularity scenarios often went in circles in a funny sort of way" and the list after "Among the bits of conceptual progress that MIRI contributed to are"). There are more mathematical examples in the post, but the fact that there are also non-mathematical examples suggests that having a precise theory of rationality is not important to the case for HRAD work. There's also the quote "As AI researchers explore the space of optimizers, what will it take to ensure that the first highly capable optimizers that researchers find are optimizers they know how to aim at chosen tasks? I’m not sure, because I’m still in some sense confused about the question."

are there examples here from wei dai? -- does wei require a precise theory or not?

### The crux

One way to reject this case for HRAD work is by saying that imprecise theories of rationality are insufficient for helping to align AI systems. This is what Rohin does in [this comment](https://www.lesswrong.com/posts/suxvE2ddnYMPJN9HD/realism-about-rationality?commentId=iSubbXvKW7uM6rus6) where he says imprecise theories cannot build things "2+ levels above".

There is a separate potential rejection, which is to say that either HRAD work will never result in precise theories or that even a precise theory is insufficient for helping to align AI systems. However, these move the crux to a place where they apply to more restricted worlds where the goal of HRAD work is specifically to come up with a precise theory, so these will be covered in the other worlds below.

## World 2

### Case for HRAD

The goal of HRAD research is to come up with a theory of rationality that is so precise that it allows one to build an agent from the ground up. Deconfusion is still important, as with world 1, but in this case we don't merely want any kind of deconfusion, but specifically deconfusion which is accompanied by a precise theory of rationality.

For this case, HRAD research isn't intended to produce a precise theory about how to predict ML systems, or to be able to make precise predictions about what ML systems will do. Instead, the idea is that the precise theory of rationality will help AGI builders avoid, detect, and fix safety issues; predict or explain safety issues; and help us be satisfied that the AGI is doing what we want. In other words, instead of directly using a precise theory about understanding/predicting rational agents in general, we use the precise theory about rationality to help us *roughly* predict what rational agents will do in general (including ML systems).

### Why I think we might be in this world

This seems to be what Abram is saying in https://www.greaterwrong.com/posts/suxvE2ddnYMPJN9HD/realism-about-rationality/comment/3f6fadtcv8FsgwKsz

It also seems to match what Rohin is saying in https://www.lesswrong.com/posts/suxvE2ddnYMPJN9HD/realism-about-rationality?commentId=iSubbXvKW7uM6rus6 and https://www.greaterwrong.com/posts/suxvE2ddnYMPJN9HD/realism-about-rationality/comment/YMNwHcPNPd4pDK7MR

### The crux

There seem to be two possible rejections here:

- rejecting the existence of the precise theory using (3).
- via (4), which is what i think daniel dewey is doing


## World 3

### Case for HRAD

HRAD work can produce precise theories of predicting ML systems, which can scale 2+ levels. This theory can then be used to detect/fix problems and ensure the safety of AGI systems.

### Why I think we might be in this world

I mostly don't think we're in this world, but some critics might think we are?

e.g. Abram says in https://www.greaterwrong.com/posts/suxvE2ddnYMPJN9HD/realism-about-rationality/comment/3f6fadtcv8FsgwKsz "I can see how Ricraz would read statements of the first type as suggesting very strong claims of the second type."

Daniel Dewey might also expect to be in this world?

### The crux

rejected by (3)



## Moving forward

I think it would be great to get HRAD proponents to be like "we're definitely in world X, and not any of the other worlds" or even be like "actually, the case for HRAD really is disjunctive, so both of the cases in worlds X and Y apply".



rohin's three-step argument: ok, let's see if it applies to shannon's work in chess.
1. this is a general statement
2. doesn't apply to chess?
3. so is shannon's theory imprecise? i would guess it's precise. so this might be the disanalogy with what miri is attempting.

# Is the disagreement about the value of HRAD work about success criteria or about ability to achieve agreed-upon aims?



Something I feel confused about is the extent to which the disagreement is about success criteria vs MIRI's ability to achieve agreed-upon aims. That's a very abstract way of phrasing it, so I want to be more concrete about what I mean.

(Throughout this post I will attribute beliefs to both MIRI and HRAD skeptics. Obviously both groups are heterogeneous and not everyone within a given group will have the same opinion, etc. I don't think it makes a big difference but if you think it does, feel free to suggest some better wording.)

1. "Disagreement is about success criteria" framing: MIRI has one set of success criteria for HRAD work, which is something like "conceptually clarifies the alignment problem; does a thing analogous to the work of Shannon, Turing, Pearl; helps people avoid mistakes analogous to the use of null-terminated strings in C" (let's call these criteria A). Skeptics of HRAD work have another set of criteria for success, which is something like "axiomatically blah blah" (let's call these criteria B). Skeptics agree that criteria A are achievable, but believe that achieving criteria A is insufficient for actually being useful for aligning an AGI. Instead, to be helpful for aligning an AGI, HRAD work must achieve criteria B, and either MIRI isn't even working toward criteria B or else HRAD work won't accomplish criteria B, so HRAD work won't be useful for aligning an AGI.
2. "Disagreement is about MIRI's ability to achieve agreed-upon aims" framing: Both MIRI and skeptics agree on what counts as success for HRAD work, i.e. there is some single success criterion that both sides agree on, which is some mixture of the criteria I listed above. The disagreement is instead about whether MIRI can achieve those goals.


you need to achieve this more difficult thing B; only doing A is insufficient. -- disagreement about success criteria

vs

both sides agree that X is the success criteria.
but then skeptics are like "well i don't think you can do X"
