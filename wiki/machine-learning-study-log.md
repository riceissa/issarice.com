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

looks mysterious because I didn't know the [conversion rule from probability of the event to the expectation of the indicator of the event](https://www.statlect.com/fundamentals-of-probability/indicator-functions).

2018-01-01: studied some probability and made [this page](https://machinelearning.subwiki.org/wiki/Summary_table_of_probability_terms). I think Rosenthal's _A First Look at Rigorous Probability Theory_ was the most book here.

??: I started reading Andrew Ng's course notes for CS229, and explored more textbooks.

(Lots of reading in AI strategy and other topics unrelated to AI safety here, so not much progress on machine learning.)

2018-01-31: started reading <http://neuralnetworksanddeeplearning.com/chap1.html>.

2018-02-01: continued reading chapter 1.

2018-02-04: finished chapter 1, starting on chapter 2 (backpropagation). Reread [this post](http://colah.github.io/posts/2015-08-Backprop/) and looked at a bunch of other explanations of backpropagation. Nielsen's explanation is usually clear but with backpropagation I find myself quite confused. I think the treatment of partial derivatives as *variables* rather than as just *functions* is a notational convention I dislike.

2018-02-05: thought more about backpropagation, and looked back at some explanations of the multivariable chain rule (Tao's *Analysis II*, Pugh's real analysis, Folland's *Advanced Calculus*, David Massey's multivariable calculus book). I remember being unsatisfied with explanations of the chain rule several years ago, and it *still* seems to me that the explanations are unsatisfactory. On the other hand, writing something myself that I would be satisfied with would take a long time and I'm not sure I could pull it off. I think connecting the chain rule to computational graphs (something Chris Olah and Folland do but the others don't) is good for exposition, especially since with neural networks you already are working with the graph. Once you have the chain rule, you can use the graph as a mnemonic, but is it possible to *see* the proof of the chain rule by staring at the graph?

2018-02-06: something that confuses me about gradient descent in neural networks is that we seem to be adjusting the weights at each individual neuron using gradient descent, but what we really want to do is to perform gradient descent with respect to the cost function (in terms of all weights and biases) of the *whole* network. It's not intuitively clear to me why working on each neuron in isolation really does gradient descent for the whole network. For instance, the weights for the neurons in the earlier layers are being adjusted for the old output, but by the time backpropagation gets to these early weights, the weights further downstream in the network have changed! How do the "demons" (to use Nielsen's analogy) in the earlier layers know to adjust even as their attempts are "thwarted" by demons in later layers?

Let's say we have some cost function $C$ that we're trying to minimize. What is the type of $C$? It gives a cost as a real number, so we can write $C : ? \to \mathbf R$. It takes as input all the weights in our network, and each weight is a matrix, so it looks like the cost function takes something in $\mathbf R^{(L-1)\times N \times M}$, where $L$ is the number of layers, $N$ is the maximum number of neurons in layers except the first, and $M$ is the maximum number of neurons in layers except the last, or something like that. I say "maximum" we need at least that much in dimension to accommodate all the weights, but since many of those weights will take up less dimension, there will be some sort of "blanks"; I'm not sure what these look like. (I think this is part of why I'm not satisfied by any of the explanations of backpropagation that I have seen, because I don't think any of them have mentioned these "blanks".) (ETA2018-02-26: I think this line of thinking if wrong. The actual dimension of the domain is the total number of *cells* in all the weight matrices, and you can think of the cost function as taking the individual cells as inputs rather than the matrices.)

So $\nabla C$ will consist of coordinates $\frac{\partial C}{\partial W^\ell_{jk}} : \mathbf R^{(L-1)\times M\times N} \to \mathbf R$.

2018-02-07: reading about lagrange multipliers and backpropagation:

- [Backprop is not just the chain rule](https://timvieira.github.io/blog/post/2017/08/18/backprop-is-not-just-the-chain-rule/)
- [Evaluating ∇f(x) is as fast as f(x)](https://timvieira.github.io/blog/post/2016/09/25/evaluating-fx-is-as-fast-as-fx/)
- [Understanding Lagrange Multipliers](https://danstronger.wordpress.com/2015/08/08/lagrange-multipliers/)
- [Lagrange Multipliers without Permanent Scarring](https://people.eecs.berkeley.edu/~klein/papers/lagrange-multipliers.pdf)

2018-02-19: continued with chapter 3.

2018-02-20: continued with chapter 3.

2018-02-21: continued with chapter 3.

2018-02-25: continued a little with chapter 3.

2018-02-26: completed chapter 3.

I've been doing most of the math/thought exercises but I've been skipping the programming ones because they seem really straightforward. I'd rather work on an actual project than doing tiny programming stuff, since I already did a bunch of the latter in Ng's course. With the thought exercises, it's difficult to tell if I'm going in the right direction.

I am "skipping" chapter 4 because I actually read it some time ago (before I even began the rest of the book).

So now I'm starting with chapter 5.

Sadly, it looks like I've forgotten a lot of the more advanced "algebra tricks" I learned in high school. This book would have been much easier to go through about five years ago.

Finished chapter 5.

2018-02-27: starting on chapter 6.

2018-02-28: continued with chapter 6.

(I think there was one or two days in between here where I read more
of chapter 6, but I forgot to record.)

2018-03-04: finished chapter 6. I didn't do any of the exercises/problems here.

Finished appendix.

Looked through the [Wikipedia page on convolutional neural network](https://en.wikipedia.org/wiki/Convolutional_neural_network), which I probably looked at a long time ago (but it didn't make any sense at that point).

Quickly looked at <http://ufldl.stanford.edu/tutorial/supervised/ConvolutionalNeuralNetwork/>.

Read <http://colah.github.io/posts/2014-07-Conv-Nets-Modular/> again, which makes much more sense now that I've read Nielsen's book.

Read <http://colah.github.io/posts/2014-07-Understanding-Convolutions/> again.

Started reading <http://www.deeplearningbook.org/contents/mlp.html>.

2018-03-05: read <http://rll.berkeley.edu/deeprlcourse/f17docs/lecture_1_introduction.pdf>

Reading chapters 1--2 of [Ng's thesis](http://rll.berkeley.edu/deeprlcourse/docs/ng-thesis.pdf).

From page 13:

> But because of the Markov property of MDPs (informally, that the
> future is conditionally independent of the past given the current
> state), to attain the optimal expected sum of rewards, it suffices
> to choose actions only \[as\] a function of the current state $s_t$.
> \[Rather than as a function of the previous and current states
> $s_0, \ldots, s_t$.\]

The above isn't intuitively obvious to me. I should spend some time
later thinking about it.
