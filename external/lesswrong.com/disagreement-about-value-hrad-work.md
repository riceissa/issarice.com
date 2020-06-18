# Plausible cases for HRAD work, and locating the crux in the "realism about rationality" debate

This post is my attempt to summarize and distill all of the major public debates about MIRI's [highly reliable agent designs](https://intelligence.org/files/TechnicalAgenda.pdf) (HRAD) work (which includes work on decision theory), including the discussions in [Realism about rationality](https://www.greaterwrong.com/posts/suxvE2ddnYMPJN9HD/realism-about-rationality) and Daniel Dewey's [My current thoughts on MIRI's "highly reliable agent design" work](https://forum.effectivealtruism.org/posts/SEL9PW8jozrvLnkb4/my-current-thoughts-on-miri-s-highly-reliable-agent-design). Part of the difficulty with discussing the value of HRAD work is that it's not even clear what the disagreement is about, so my summary takes the form of multiple possible "worlds" we might be in; each world consists of a positive case for doing HRAD work, along with the potential objections to that case, which results in one or more cruxes.

In this post, the pro-HRAD stance is something like "HRAD work is the most important kind of technical research in AI alignment; it is the overwhelming priority and we're pretty much screwed if we under-invest in this kind of research" and the anti-HRAD stance is something like "HRAD work seems significantly less promising than other technical AI alignment agendas, such as the approaches to directly align machine learning systems (e.g. iterated amplification)". There is a much [weaker pro-HRAD stance](https://www.greaterwrong.com/posts/JSjagTDGdz2y6nNE3/on-the-purposes-of-decision-theory-research/comment/GBZt6scwpAseroYjR), which is something like "HRAD work is interesting and doing more of it adds value, but it's not necessarily the most important kind of technical AI alignment research to be working on"; this post is not about this weaker stance.

TODO: use full name for first appearance of each person's name, except for daniel dewey since there are multiple daniels in ai safety

## Clarifying some terms

Before describing the various worlds, I want to present some distinctions that have come up in discussions about HRAD, which will be relevant when distinguishing between the worlds.

### Levels of abstraction vs levels of indirection

The idea of levels of abstraction was introduced in the context of HRAD work by Rohin Shah, and is described in [this comment](https://www.greaterwrong.com/posts/suxvE2ddnYMPJN9HD/realism-about-rationality/comment/YMNwHcPNPd4pDK7MR) (start from "When groups of humans try to build complicated stuff"). For more background, see [these](https://en.wikipedia.org/wiki/Abstraction_%28computer_science%29#Levels_of_abstraction) [articles](https://en.wikipedia.org/wiki/Leaky_abstraction) on Wikipedia.

Later on, in [this comment](https://www.greaterwrong.com/posts/suxvE2ddnYMPJN9HD/realism-about-rationality/comment/aNHTM9iwfrCeAcHtn) Rohin gave a somewhat different "levels" idea, which I've decided to call "levels of indirection". The relevant levels of indirection is the sequence HRAD → machine learning → AGI. Even though levels of indirection are different from levels of abstraction, the idea is that the same principle applies, where the more levels there are, the harder it becomes for a theory to apply to the final level.

### Precise vs imprecise theory

A precise theory is one which can scale to 2+ levels of abstraction/indirection.

An imprecise theory is one which can scale to at most 1 level of abstraction/indirection.

More intuitively, a precise theory is more mathy, rigorous, and exact like pure math and physics, and an imprecise theory is less mathy, like economics and psychology.

### Building agents from the ground up vs understanding the behavior of rational agents and predicting roughly what they will do

This distinction comes from Abram Demski's [comment](https://www.greaterwrong.com/posts/suxvE2ddnYMPJN9HD/realism-about-rationality/comment/3f6fadtcv8FsgwKsz). However, I'm not confident I've understood this distinction in the way that Abram intended it, so what I describe below may be a slightly different distinction.

Building agents from the ground up means having a precise theory of rationality that allows us to build an AGI in a satisfying way, e.g. where someone with [security mindset](https://www.greaterwrong.com/posts/8gqrbnW758qjHFTrH/security-mindset-and-ordinary-paranoia) can be confident that it is aligned. Importantly, we allow the AGI to be built using whatever way is safest or most theoretically satisfying, rather than requiring that the AGI be built using whatever methods are mainstream, like current machine learning methods.

Understanding the behavior of rational agents and predicting roughly what they will do means being handed an arbitrary agent implemented in some way (e.g. via blackbox ML) and then being able to predict how it will act.

I think of the difference between these two as the difference between existential and universal quantification: "there exists x such that P(x)" and "for all x we have P(x)", where P(x) is something like "we can understand and predict how x will act in a satisfying way". The former only says that we can build some AGI using the precise theory that we understand well, whereas the latter says we have to deal with whatever kind of AGI that ends up being developed using methods we might not understand well.

## World 1

### Case for HRAD

The goal of HRAD research is to generally become less confused about things like counterfactual reasoning and logical uncertainty. Becoming less confused about these things will: help AGI builders avoid, detect, and fix safety issues; help AGI builders predict or explain safety issues; help to conceptually clarify the AI alignment problem; and help us be satisfied that the AGI is doing what we want.

For this case, it is not important for the final product of HRAD to be a precise theory. Even if the final theory of embedded agency is imprecise, or even if there *is no* "final say" on the topic, if we are merely much less confused than we are now, that is still good enough to help us ensure AI systems are aligned.

### Why I think we might be in this world

The main reason I think we might be in this world is that people at MIRI frequently seem to be saying something like it. However, they also seem to be saying different things in other places, so I'm not confident we are actually in this world. Here are some examples:

- [Eliezer Yudkowsky](https://intelligence.org/files/OpenPhil2016Supplement.pdf#page=13): "Techniques you can actually adapt in a safe AI, come the day, will probably have very simple cores — the sort of core concept that takes up three paragraphs, where any reviewer who didn’t spend five years struggling on the problem themselves will think, “Oh I could have thought of that.” Someday there may be a book full of clever and difficult things to say about the simple core — contrast the simplicity of the core concept of causal models, versus the complexity of proving all the clever things Judea Pearl had to say about causal models. But the planetary benefit is mainly from posing understandable problems crisply enough so that people can see they are open, and then from the simpler abstract properties of a found solution — complicated aspects will not carry over to real AIs later."
- [Rob Bensinger](https://www.greaterwrong.com/posts/uKbxi2EJ3KBNRDGpL/comment-on-decision-theory): "We’re working on decision theory because there’s a cluster of confusing issues here (e.g., counterfactuals, updatelessness, coordination) that represent a lot of holes or anomalies in our current best understanding of what high-quality reasoning is and how it works." and phrases like "developing an understanding of roughly what counterfactuals are and how they work" and "very roughly how/why it works"  -- This post then doesn't really specify whether or not the final output is expected to be precise. (The analogy with probability theory and rockets gestures at precise theories, but the post doesn't come out and say it.)
- [Abram Demski](https://www.greaterwrong.com/posts/suxvE2ddnYMPJN9HD/realism-about-rationality/comment/XEbNPAyvjpTcGufLm): "I don't think there's a true rationality out there in the world, or a true decision theory out there in the world, or even a true notion of intelligence out there in the world. I work on agent foundations because there's *still something I'm confused about* even after that, and furthermore, AI safety work seems fairly hopeless while still so radically confused about the-phenomena-which-we-use-intelligence-and-rationality-and-agency-and-decision-theory-to-describe."
- [Nate Soares](https://forum.effectivealtruism.org/posts/SEL9PW8jozrvLnkb4/my-current-thoughts-on-miri-s-highly-reliable-agent-design?commentId=D3PDv7kqJuByt8TRr): "The main case for HRAD problems is that we expect them to help in a gestalt way with many different known failure modes (and, plausibly, unknown ones). E.g., 'developing a basic understanding of counterfactual reasoning improves our ability to understand the first AGI systems in a general way, and if we understand AGI better it's likelier we can build systems to address deception, edge instantiation, goal instability, and a number of other problems'."
- In the [deconfusion](https://intelligence.org/2018/11/22/2018-update-our-new-research-directions/#section2) section of MIRI's 2018 update, some of the examples of deconfusion are not precise/mathematical in nature (e.g. see the paragraph starting with "In 1998, conversations about AI risk and technological singularity scenarios often went in circles in a funny sort of way" and the list after "Among the bits of conceptual progress that MIRI contributed to are"). There are more mathematical examples in the post, but the fact that there are also non-mathematical examples suggests that having a precise theory of rationality is not important to the case for HRAD work. There's also the quote "As AI researchers explore the space of optimizers, what will it take to ensure that the first highly capable optimizers that researchers find are optimizers they know how to aim at chosen tasks? I’m not sure, because I’m still in some sense confused about the question."

### The crux

One way to reject this case for HRAD work is by saying that imprecise theories of rationality are insufficient for helping to align AI systems. This is what Rohin does in [this comment](https://www.greaterwrong.com/posts/suxvE2ddnYMPJN9HD/realism-about-rationality/comment/iSubbXvKW7uM6rus6) where he says imprecise theories cannot build things "2+ levels above".

There is a separate potential rejection, which is to say that either HRAD work will never result in precise theories or that even a precise theory is insufficient for helping to align AI systems. However, these move the crux to a place where they apply to more restricted worlds where the goal of HRAD work is specifically to come up with a precise theory, so these will be covered in the other worlds below.

## World 2

### Case for HRAD

The goal of HRAD research is to come up with a theory of rationality that is so precise that it allows one to build an agent from the ground up. Deconfusion is still important, as with world 1, but in this case we don't merely want any kind of deconfusion, but specifically deconfusion which is accompanied by a precise theory of rationality.

For this case, HRAD research isn't intended to produce a precise theory about how to predict ML systems, or to be able to make precise predictions about what ML systems will do. Instead, the idea is that the precise theory of rationality will help AGI builders avoid, detect, and fix safety issues; predict or explain safety issues; help to conceptually clarify the AI alignment problem; and help us be satisfied that the AGI is doing what we want. In other words, instead of directly using a precise theory about understanding/predicting rational agents in general, we use the precise theory about rationality to help us *roughly* predict what rational agents will do in general (including ML systems).

### Why I think we might be in this world

This seems to be what Abram is saying in [this comment](https://www.greaterwrong.com/posts/suxvE2ddnYMPJN9HD/realism-about-rationality/comment/3f6fadtcv8FsgwKsz) (see especially the part after "I guess there's a tricky interpretational issue here").

It also seems to match what Rohin is saying in [these](https://www.greaterwrong.com/posts/suxvE2ddnYMPJN9HD/realism-about-rationality/comment/iSubbXvKW7uM6rus6) and [two](https://www.greaterwrong.com/posts/suxvE2ddnYMPJN9HD/realism-about-rationality/comment/YMNwHcPNPd4pDK7MR) comments.

The examples MIRI people sometimes give for precedents of HRAD-ish work, like the work done by [Turing](https://forum.effectivealtruism.org/posts/SEL9PW8jozrvLnkb4/my-current-thoughts-on-miri-s-highly-reliable-agent-design?commentId=Z6TbXivpjxWyc8NYM), [Shannon](https://intelligence.org/2015/07/27/miris-approach/), and [Maxwell](https://intelligence.org/2018/11/22/2018-update-our-new-research-directions/#section2), are precise mathematical theories.

### The crux

There seem to be two possible rejections of this case:

- We can reject the existence of the precise theory of rationality. This is what Rohin does in [this comment](https://www.greaterwrong.com/posts/suxvE2ddnYMPJN9HD/realism-about-rationality/comment/YMNwHcPNPd4pDK7MR) and [this comment](https://www.greaterwrong.com/posts/suxvE2ddnYMPJN9HD/realism-about-rationality/comment/iSubbXvKW7uM6rus6) where he says "MIRI's theories will always be the relatively-imprecise theories that can't scale to '2+ levels above'."
- We can argue that even a precise theory of rationality is insufficient for helping to align AI systems. i think daniel dewey is doing this.

## World 3

### Case for HRAD

The goal of HRAD research is to directly come up with a precise theory for understanding the behavior of rational agents and predicting what they will do. Deconfusion is still important, as with worlds 1 and 2, but in this case we don't merely want any kind of deconfusion, but specifically deconfusion which is accompanied by a precise theory that allows us to predict agents' behavior in general. And a precise theory is important, but we don't merely want a precise theory that lets us *build* an agent; we want our theory to act like a box that takes in an arbitrary agent (such as one built using ML and other black boxes) and allows us to analyze its behavior.

This theory can then be used to help AGI builders avoid, detect, and fix safety issues; predict or explain safety issues; help to conceptually clarify the AI alignment problem; and help us be satisfied that the AGI is doing what we want.

### Why I think we might be in this world

I mostly don't think we're in this world, but some critics might think we are?

e.g. Abram says in https://www.greaterwrong.com/posts/suxvE2ddnYMPJN9HD/realism-about-rationality/comment/3f6fadtcv8FsgwKsz "I can see how Ricraz would read statements of the first type [i.e. having precise understanding of rationality] as suggesting very strong claims of the second type [i.e. being able to understand the behavior of agents in general]."

Daniel Dewey might also expect to be in this world?

### The crux

rejected by Rohin https://www.greaterwrong.com/posts/suxvE2ddnYMPJN9HD/realism-about-rationality/comment/iSubbXvKW7uM6rus6 "MIRI’s theories will always be the relatively-imprecise theories that can’t scale to “2+ levels above”." This is the same rejection as in world 2.

## Moving forward

I think it would be great to get HRAD proponents/opponents to be like "we're definitely in world X, and not any of the other worlds" or even be like "actually, the case for HRAD really is disjunctive, so both of the cases in worlds X and Y apply".

If I missed any additional possible worlds, or if I described one of the worlds incorrectly, I am interested in hearing about it.

If it becomes clear which world we are in, then the next step is to drill down on the crux.


*Thanks to Ben Cottier, Rohin Shah, and Joe Bernstein for feedback on this post.*
