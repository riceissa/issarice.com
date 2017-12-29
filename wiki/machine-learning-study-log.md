---
title: Machine learning study log
author: Issa Rice
created: 2017-12-27
date: 2017-12-27
# documentkind:
# status:
# belief:
---

This is a study log of my progress in machine learning. I am trying to understand machine learning to get a better sense of AI safety (I think I understand the philosophical/strategic perspective well, having followed the output of the [rationality community]() since around 2010/2011, but I don't know much about ML itself or other technical details of AI development).

In parallel with learning ML, I am also reading more high level discussions about AI safety, but I won't cover that on this page. (Not sure where I'll cover it atm)

# Andrew Ng's Coursera course

Began the course on 2017-10-19.

Completed the course on 2017-12-08.

I worked on the course during my after-work hours and on weekends.

The course was easy for me, because I already knew programming. I didn't know any Octave but this wasn't really a problem as the course covers the basics and it is easy enough to look up additional syntax.

The course doesn't cover a lot of the math behind machine learning, which I think is another reason I felt the course was easy.

# After Ng -- reinforcement learning?

After Ng's course, I wasn't sure what to do next. I checked out some resources on reinforcement learning (e.g Sutton & Barto) but found them rather difficult/not explained well so I stopped.

# Understanding more math

I started looking around for more resources on the theory behind machine learning.

On 2017-12-26, I created [Comparison of machine learning textbooks](https://machinelearning.subwiki.org/wiki/Comparison_of_machine_learning_textbooks) because I got frustrated with being unable to keep all the ML books in my head (and the recommendations given in various online discussions).

2017-12-27: I got curious about [probably approximately correct learning](https://en.wikipedia.org/wiki/Probably_approximately_correct_learning) so decided to look through the textbooks on ML that covered that. I found [this post](https://jeremykun.com/2014/01/02/probably-approximately-correct-a-formal-theory-of-learning/) which seems to be better at explaining PAC than any of the textbooks.

2017-12-28: I think I keep getting stuck on parts of textbooks that rely on results from probability, which I don't know very well. Steps that rely on probability results look like magic to me, and I don't like them. Even something supposedly simple like (taken from Mohri et al)

$$\Pr_{x\sim D} [h(x) \ne c(x)] = \mathrm{E}_{x\sim D} [1_{h(x) \ne c(x)}]$$

looks mysterious because I didn't know the conversion rule from probability of the event to the expectation of the indicator of the event.
