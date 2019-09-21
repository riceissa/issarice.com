I have been trying to understand all the iterative/recursive approaches to AI alignment. The approaches I am aware of are:

- ALBA (I get the vague impression that this has been superseded by iterated amplification, so I haven't looked into it)
- HCH (weak and strong)
- Iterated amplification (IDA)
- Debate
- Meta-execution
- (Recursive) reward modeling
- Factored cognition
- Factored evaluation

(I think that some of these, like HCH, aren't strictly speaking an approach to AI alignment, but they are still iterative/recursive things discussed in the context of AI alignment, so I want to better understand them.)

One way of phrasing what I am trying to do is to come up with a "minimal set" of parameters/dimensions along which to compare these different approaches, so that I can take a basic template, then set the parameters to obtain each of the above approaches as an instance.

Here are the parameters/dimensions that I have come up with so far:

- capability of agents: I think in HCH, the agents are human-level. In the other approaches, my understanding is that the capability of the agents increases as more and more rounds of amplification/distillation take place.
- allowed communication: It seems like [weak and strong HCH](https://ai-alignment.com/strong-hch-bedb0dc08d4e) differ in the kind of communication that is allowed between the assistants (with strong HCH allowing more flexible communication). Within IDA, there is [low bandwidth vs high bandwidth oversight](https://www.lesswrong.com/posts/yxzrKb2vFXRkwndQ4/understanding-iterated-distillation-and-amplification-claims), which seems like a similar parameter. I'm not sure what the other approaches allow.
- training method during distillation step: I think [IDA leaves the training method flexible](https://www.lesswrong.com/s/EmDuGeRw749sD3GKd/p/HqLxuZ4LhaFhmAHWk). According to [this post](https://www.lesswrong.com/posts/NTwA3J99RPkgmp6jh/an-62-are-adversarial-examples-caused-by-real-but), factored cognition seems to use imitation learning and factored evaluation seems to use reinforcement learning. I think recursive reward modeling also uses reinforcement learning. HCH seems to be just about the amplification step (?), so no training method is used. I'm not sure about the others.
- entity who "splits the questions", coordinates everything during amplification, or selects the branches: In factored cognition, factored evaluation, IDA, and HCH, it seems like the human splits the questions. In Debate, the branches are chosen by the two AIs in the debate (who are in an adversarial relationship).
- entity who does the evaluation/gives feedback ("the overseer"): It seems like in factored evaluation, the human gives feedback. In Debate, the final judgment is provided by the human. My understanding is that in [IDA, the nature of the overseer is flexible](https://www.lesswrong.com/s/EmDuGeRw749sD3GKd/p/7Hr8t6xwuuxBTqADK) ("For example, Arthur could advise Hugh on how to define a better overseer; Arthur could offer advice in real-time to help Hugh be a better overseer; or Arthur could directly act as an overseer for his more powerful successor").
- what the overseer does (i.e. what kind of feedback is provided): I think the overseer can be passive/active depending on the distillation method (see my comment [here](https://www.lesswrong.com/posts/HqLxuZ4LhaFhmAHWk/iterated-distillation-and-amplification-1#92FzkKHZ9az8dezSH)), so maybe this parameter isn't required in a "minimal set".
- required number of human feedback per round: In Debate, there is one feedback at the end of a debate round. In factored evaluation, it seems like the human must provide feedback at each node in the question tree (or a separate human at each node in the question tree).
- depth of recursion: It seems like IDA limits the depth of the recursion to one step, whereas the other approaches seem to allow arbitrary depth (see my comment [here](https://www.lesswrong.com/posts/Djs38EWYZG8o7JMWY/paul-s-research-agenda-faq#rHc4rSpZzM8jZvdd3)).
- separation of task performance vs evaluation/oversight: It seems like in factored evaluation, there is an entity who does the task itself (the experts at the bottom of [this diagram](https://ought.org/images/presentations/2019-delegation/2019-eag-delegation-web.050.jpeg)), and a separate entity who evaluates the work of the experts (the "factored evaluation" box in the same diagram), but in factored cognition, there is just the entity doing the task.

I would appreciate hearing about more parameters/dimensions that I have missed, and also any help filling in some of the values for the parameters (including corrections to any of my speculations above).

Ideally, there would be a table with the parameters as columns and each of the approaches as rows (possibly transposed), like the table in [this post](https://www.lesswrong.com/posts/bnY3L48TtDrKTzGRb/ai-safety-success-stories). I would be willing to produce such a write-up assuming I am able to fill in enough of the values that it becomes useful.

If anyone thinks this kind of comparison is useless/framed in the wrong way, please let me know. (I would also want to know what the correct framing is!)
