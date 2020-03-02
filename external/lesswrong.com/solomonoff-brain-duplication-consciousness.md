# What does Solomonoff induction say about brain duplication/consciousness?

Back in 2012, in a [thread](https://www.greaterwrong.com/posts/PXoWk554FZ4Gpfvah/causal-reference/comment/5K9ewNasTGWmkfQdM) on LW, Carl Shulman wrote a couple of comments connecting Solomonoff induction to brain duplication, epiphenomenalism, functionalism, David Chalmers's "psychophysical laws", and other ideas in consciousness.

The [first comment](https://www.greaterwrong.com/posts/PXoWk554FZ4Gpfvah/causal-reference/comment/pFbkDEFnTS8exmmKu) says:

> It seems that you get similar questions as a natural outgrowth of simple computational models of thought. E.g. if one performs Solomonoff induction on the stream of camera inputs to a robot, what kind of short programs will dominate the probability distribution over the next input? Not just programs that simulate the physics of our universe: one would also need additional code to "read off" the part of the simulated universe that corresponded to the camera inputs. That additional code looks like epiphenomenal mind-stuff. Using this framework you can pose questions like "if the camera is expected to be rebuilt using different but functionally equivalent materials, will his change the inputs Solomonoff induction predicts?" or "if the camera is about to be duplicated, which copy's inputs will be predicted by Solomonoff induction?"
>
> If we go beyond Solomonoff induction to allow actions, then you get questions that map pretty well to debates about "free will."

The [second comment](https://www.greaterwrong.com/posts/PXoWk554FZ4Gpfvah/causal-reference/comment/auu9giBwDFc9tFsZQ) says:

> The code simulating a physical universe doesn't need to make any reference to which brain or camera in the simulation is being "read off" to provide the sensory input stream. The additional code takes the simulation, which is a complete picture of the world according to the laws of physics as they are seen by the creatures in the simulation, and outputs a sensory stream. This function is directly analogous to what dualist/epiphenomenalist philosopher of mind David Chalmers calls "psychophysical laws."

Carl's comments pose the questions you can ask/highlight the connection, but they don't answer those questions. I would be interested in references to other places discussing this idea, or answers to these questions.

Here are some of my own confused thoughts (I'm still trying to learn algorithmic information theory, so I would appreciate hearing any corrections):

- If the camera is duplicated, it seems to take a longer program to track/read off two cameras in the physical world instead of just one, so Solomonoff induction would seem to prefer a bit sequence where only one camera's inputs are visible. However, there seems to be a symmetry between the two cameras, in that neither one takes a longer program to track. So right before the camera is duplicated, Solomonoff induction "knows" that it will be in just one of the cameras soon, but doesn't know which one. If we are using the variant of Solomonoff induction that puts a probability distribution over sequences, then the probability mass will split in half between the two copies' views. Is this right? If we are using the variant of Solomonoff induction that just prints out bits, then I don't know what happens; does it just flip a coin to decide which camera's view to print?
- If the camera is rebuilt using different but functionally equivalent materials, I guess it would be possible to track the inputs to the new camera, but wouldn't it be even simpler to stop tracking the physical world altogether (and just return a blank camera view)?
- In general, any time anything "drastic" happens to the camera (like a rock falling on it), it seems like one of the shortest programs is to just assume the camera stops working (or does something else that's weird-but-simple, like just "reading off" a fixed location without motion). But I'm not sure how to classify what counts as "drastic".
