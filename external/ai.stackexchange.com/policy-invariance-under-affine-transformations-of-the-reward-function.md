In the context of a Markov decision process, [this paper](https://arxiv.org/pdf/1902.09725.pdf) says "it is well-known that the optimal policy is invariant to positive affine transformation of the reward function".

On the other hand, exercise 3.7 of [Sutton and Barto](http://incompleteideas.net/book/the-book-2nd.html) gives an example of a robot in a maze:

> Imagine that you are designing a robot to run a maze. You decide to give it a reward of +1 for escaping from the maze and a reward of zero at all other times. The task seems to break down naturally into episodes—the successive runs through the maze—so you decide to treat it as an episodic task, where the goal is to maximize expected total reward (3.7). After running the learning agent for a while, you find that it is showing no improvement in escaping from the maze. What is going wrong? Have you effectively communicated to the agent what you want it to achieve?

It seems like the robot is not being rewarded for escaping quickly (escaping in 10 seconds gives it just as much reward as escaping in 1000 seconds). One fix seems to be to subtract 1 from each reward, so that each timestep the robot stays in the maze, it accumulates $-1$ in reward, and upon escape it gets zero reward. This seems to change the set of optimal policies (now there are way fewer policies which achieve the best possible return). In other words, a positive affine transformation $r \mapsto 1 \cdot r - 1$ seems to have changed the optimal policy.

How can I reconcile "the optimal policy is invariant to positive affine transformation of the reward function" with the maze example?
