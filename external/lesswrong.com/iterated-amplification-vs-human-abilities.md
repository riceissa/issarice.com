# How does iterated amplification exceed human abilities?

When I first started learning about IDA, I thought that agents trained using IDA would be human-level after the first stage, i.e. that Distill(H) would be human-level. As I've [written about before](https://www.lesswrong.com/posts/FdfzFcRvqLf4k5eoQ/list-of-resolved-confusions-about-ida?commentId=bdcWwPhaZxiy7rxLb), Paul later clarified this, so my new understanding is that after the first stage, the distilled agent will be super-human in some respects and infra-human in others, but wouldn't be "basically human" in any sense.

But IDA is aiming to eventually be super-human in almost every way (because it's aiming to be competitive with unaligned AGI), so that raises some new questions:

1. If IDA isn't going to be human-level after the first stage, then at what stage does IDA become at-least-human-level in almost every way?
2. What exactly is the limitation that prevents the first stage of IDA from being human-level in almost every way?
3. When IDA eventually _does_ become at-least-human-level in almost every way, how is the limitation from (2) avoided?

That brings me to [Evans et al.](https://owainevans.github.io/pdfs/evans_ida_projects.pdf), which contains a description of IDA in section 0. The way IDA is set up in this paper leads me to believe that the answer to (2) above is that the human overseer cannot provide a sufficient number of demonstrations for the most difficult tasks. For example, maybe the human can provide enough demonstrations for the agent to learn to answer very simple questions (tasks in $T_0$ in the paper) but it's too time-consuming for the human to answer enough complicated questions (say, in $T_{100}$). My understanding is that IDA gets around this by having an amplified system that is itself automated (i.e. does not involve humans in a major way, so cannot be bottlenecked on the slowness of humans); this allows the amplified system to provide a sufficient number of demonstrations for the distillation step to work.

So in the above view, the answer to (2) is that the limitation is the number of demonstrations the human can provide, and the answer to (3) is that the human can seed the IDA process with sufficient demonstrations of easy tasks, after which the (automated) amplified system can provide sufficient demonstrations of the harder tasks. The answer to (1) is kind of vague: it's just the smallest $n$ for which $\bigcup_{i=0}^n T_i$ contains almost all tasks a human can do.

But the above view seems to conflict with what's in the [IDA post](https://ai-alignment.com/iterated-distillation-and-amplification-157debfd1616) and the [IDA paper](https://arxiv.org/abs/1810.08575). In both of those, the amplified system is described as a human doing the decompositions (so it will be slow, or else one would need to argue that the slowness of humans decomposing tasks doesn't meaningfully restrict the number of demonstrations). Also, the main benefit of amplification is described not as the ability to provide more demonstrations, but rather to provide demonstrations for more difficult tasks. Under this alternative view, the answers to questions (1), (2), (3) aren't clear to me.

*Thanks to Vipul Naik for reading through this question and giving feedback.*
