To me, it seems like the two distinctions *are* different. There seem to be three levels to distinguish:

1. The reward (in the reinforcement learning sense) or the base objective (example: inclusive genetic fitness for humans)
2. A mechanism in the brain that dispenses pleasure or provides a proxy for the reward (example: pleasure in humans)
3. The actual goal/utility that the agent ends up pursuing (example: a reflective equilibrium for some human's values, which might have nothing to do with pleasure or inclusive genetic fitness)

The base objective vs mesa-objective distinction seems to be about (1) vs a combination of (2) and (3). The reward maximizer vs utility maximizer distinction seems to be about (2) vs (3), or maybe (1) vs (3).

Depending on the agent that is considered, only some of these levels may be present:

- A "dumb" RL-trained agent that engages in reward gaming. Only level (1), and there is no mesa-optimizer.
- A "dumb" RL-trained agent that engages in reward tampering. Only level (1), and there is no mesa-optimizer.
- A paperclip maximizer built from scratch. Only level (3), and there is no mesa-optimizer.
- A relatively "dumb" mesa-optimizer trained using RL might have just (1) (the base objective) and (2) (the mesa-objective). This kind of agent would be incentivized to tamper with its pleasure circuitry (in the sense of (2)), but wouldn't be incentivized to tamper with its RL-reward circuitry. (Example: rats wirehead to give themselves MAX_PLEASURE, but don't self-modify to delude themselves into thinking they have left many descendants.)
- If the training procedure somehow coughs up a mesa-optimizer that doesn't have a "pleasure center" in its brain (I don't know how this would happen, but it seems logically possible), there would just be (1) (the base objective) and (3) (the mesa-objective). This kind of agent wouldn't try to tamper with its utility function (in the sense of (3)), nor would it try to tamper with its RL-reward/base-objective to delude itself into thinking it has high rewards.

ETA: Here is a table that shows these distinctions varying independently:

| |**Utility maximizer**|**Reward maximizer**|
|-|-|-|
|**Optimizes for base objective (i.e. mesa-optimizer absent)**|Paperclip maximizer|"Dumb" RL-trained agent|
|**Optimizes for mesa-objective (i.e. mesa-optimizer present)**|Human in reflective equilibrium|Rats|
