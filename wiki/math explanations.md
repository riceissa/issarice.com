---
title: Math explanations
author: Issa Rice
created: 2017-12-25
date: 2018-10-10
status: notes
---

I've been thinking more about math explanations again (something I used to think a lot about when I was first learning abstract math) because I'm trying to get a good understanding of machine learning. In particular I'm thinking about what makes explanations good or bad. This is an [ignorant thinking](https://meteuphoric.wordpress.com/2011/08/27/in-defence-of-ignorant-thinking/) page for now, so don't expect me to know anything about the topic.

In my mind some things that make explanations good are:

- Writing for the right background. I think many books are not giving the background with sufficient specificity. Like they give general topics like "basic probability" without clarifying what that means, even though the meaning changes depending on location and generation.
- Anticipating questions. It really frustrates me when a writer explains something, then doesn't explain some follow up point that is important to me. On the other hand, it feels satisfying when I ask a question in my mind, and immediately in the next sentence or paragraph the writer answers it. I feel like this is especially important to do with written content. With in-person explanations or interactive discussions, it might be less important to anticipate everything beforehand. And anticipating everything is hard because there are a lot of things someone could ask.
- Giving good motivations. Not doing this properly would be things like giving a definition without writing about how it is thought of in practice, or giving alternative formulations and things like that.
- Giving good examples. I feel like this has something to do with writing good unit tests in software engineering. Like you want to get the good edge cases covered.
- (Maybe) Giving a list of examples first before giving the solutions to those examples, and inviting the reader to do the examples themselves. I noticed this in Boolos, Burgess, and Jeffrey's _Computability and Logic_. This style of writing essentially creates extra exercises for the reader.
- Filling in a lot of details. This is sort of similar to the anticipating questions one, but I get frustrated when a lot of steps are skipped. Because in writing the book, the author had to take the same mental steps, and yet they are not recording those steps! It's like they encode their steps into this really strangely terse format, and then when you read the text you have to do the decoding. Why not just write it out verbosely and save us a step?
- Notation. Maybe this is just me, but I generally don't like things like not explicitly bounding bounded variables (e.g. writing $\sum_i f(x_i)$ instead of $\sum_{i\in S} f(x_i)$; without the $i \in S$, the set from which the $i$ values takes is implicit, which means more work for the reader to keep track of such things), writing expressions but calling them functions (e.g. "let $f(x)$ be a function ..."), not introducing each variable (e.g. using variables like $f$ without saying "let $f : X \to Y$ be a function" first, or using $n$ without introduction even though it usually means a whole number), not exposing types (e.g. when using random variables and saying things like $P(X = x)$, what is the type of $=$?).
- For "tutorial" type material, an embedded/built-in "spaced repetition" type process where material from earlier chapters quietly shows up in later chapters to remind readers, possibly in slightly altered form to solidify understanding.
- When using terms, saying explicitly whether a term is commonly used in the field or whether it is made up on the spot or only used in some sub-communities. This is similar to how when explaining a controversial topic, one should be able to state the other side's views clearly (i.e. pass the Ideological Turing Test for other views).
- When giving an abstraction (e.g. definition), say it in multiple ways, and also give the reason you're defining it that way.
- Seriously, why don't all textbooks have multiple choice questions and [error-spotting exercises](https://learning.subwiki.org/wiki/Error-spotting_exercise) mixed in with the exposition?
- Explaining why naive versions one might come up with cannot be true. [Example](https://calculus.subwiki.org/wiki/Chain_rule_for_differentiation#Why_more_naive_chain_rules_don.27t_make_sense).
- Purposely going down wrong paths (while warning readers that it *is* a wrong path) that a naive reader would want to go down, just to illustrate why it doesn't work. Terence Tao mentions this in [this comment](https://gowers.wordpress.com/2007/09/11/what-might-an-expository-mathematical-wiki-be-like/#comment-14). You could think of this as a kind of imaginary Ideological Turing Test where one earnestly explores a mistaken path to show why it might seem reasonable, but then showing why it isn't actually the right approach.

  An [example](https://gowers.wordpress.com/2011/10/07/basic-logic-tips-for-handling-variables/) from Tim Gowers (go to the part in the post that
  says "Here’s what might have happened if I had struggled on with the
  sentence I was in the middle of writing").

  I think it might be difficult to make this interesting, because
  there are so many wrong paths that one could go down.  What seems like
  a "natural" wrong path to go down for one person might seem absurd to
  another person (who has a different background or personality).  It seems
  bad if these "going down wrong paths" in texts started to seem just tedious
  to go through (even the correct paths can seem tedious at times!).

  Another example is Michael Nielsen's bitcoin blog post, where he iteratively
  builds up the ideas of bitcoin by considering naive approaches to a digital
  currency, then fixing the problems in them.

- For exercises, I think it's important to explain somewhere what the exercise
  is intended to teach. Textbooks often warn that not doing the exercises will
  mean not actually learning the material (or similar). If this is truly the
  case, it should be straightforward to justify the importance of each
  exercise, but I never see this done in practice.  My personal experience has
  been that the vast majority of exercises are not that interesting or
  enlightening, and I have a hard time figuring what the exercise was for,
  other than an application of some trick. If explaining the point of the
  exercise spoils the exercise, it can be explained in some place other than
  immediately near the exercise.
- Sticking to standard terminology. While there are some imperfections in the standard terminology, it is often too confusing to switch between different terminology, so my preference is that explainers stick to the standard ones, or use defensive/fool-proof terminology/notation. Another option is to explain all the variations in terminology so that readers are not confused when they go read other books (Peter Smith's Gödel book does a great job of this), or to have some resource that all readers can use to find out the variations in terminology (I wish Wikipedia could be such a resource, but it's often very incomplete, even on common undergraduate topics).

  To give an example, Boolos, Burgess, and Jeffrey's _Computability and Logic_ uses "function" to mean "total or partial function", and "total function" to mean "function". This sort of thing is confusing because now there are two "claims" on the meaning of "function". (This actually becomes sort of a problem in the book because when introducing characteristic functions, the book does not clarify that these must be total.) A defensive writing style would avoid the word "function" and use "total or partial function" and "total function". Similarly in set theory, $\subset$ sometimes means "subset" and sometimes means "proper subset". A defensive style of writing would avoid this and use $\subseteq$ and $\subsetneq$.

- Given two concepts that could be mistaken for each other, there are
  four possibilities with four different ways to help the reader: $X
  \iff Y$ (prove that all $X$ are $Y$ and that all $Y$ are $X$); $X
  \implies Y$ and $Y \mathrel{{\not}\!\!\!{\implies}} X$ (prove that all $X$ are $Y$, and
  give an example of something that is $Y$ but not $X$; $Y \implies X$
  (similar to previous); and $X\mathrel{{\not}\!\!\!{\implies}} Y$ and $Y\mathrel{{\not}\!\!\!{\implies}} X$
  (give an example of something that is $X$ but not $Y$, and
  separately an example of something that is $Y$ but not $X$).
  For the last of these, I like the example given by Terence Tao in
  _Analysis I_ to illustrate how "disjoint" and "distinct" are
  entirely different concepts: $\{1,2,3\}$ and $\{2,3,4\}$ are
  distinct but not disjoint, and $\emptyset$ and $\emptyset$ are
  disjoint but not distinct.

  Another example from logic: complete set of formulas vs maximal
  consistent set of formulas. These seem to be equivalent in the
  standard formal systems we work with, but are there systems in which
  they are different? Is one necessarily stronger than the other?

- There is a kind of paternalism trade-off in explanations when deciding e.g.
  whether to ask the reader to prove a theorem before reading the proof in the
  book. Some authors will (1) just assume that the reader has enough "math
  culture" in them to know that they should try to prove the theorem before
  reading the proof; other authors will (2) gently prod the reader to prove
  the theorem before reading on (usually in the book's preface); still others
  will (3) just not have any sort of opinion on this, or say the reader ought
  to know best what to do. In terms of paternalism, I would say (2) is most
  paternalistic, followed by (1), and then (3) is least paternalistic.

  My current feeling is that books aimed at beginners (undergraduate level)
  and self-studiers should probably lean toward being paternalistic. For
  self-studiers, it is difficult sometimes to pick up on "math culture"
  without reading many different books or reading up on discussion threads (on
  MathOverflow, Reddit, math blogs, etc.).

  Just to give some examples:

  - Michael Nielsen's neural networks book has a
    [page](http://neuralnetworksanddeeplearning.com/exercises_and_problems.html)
    that explains his stance on exercises. I guess this doesn't fit into any
    of the (1)--(3) I listed above.
  - Tim Gowers has advice in his Cambridge teaching posts to the effect of
    (2), but maybe in his official lecture notes he emphasizes this less (so
    closer to (1)).
  - _Computability and Logic_ does some of (2), where they say "we'll show all
    the examples first, then the proofs later, so the reader can do them".
  - I like how in Goldrei's logic book, he mixes in exercises
    throughout the text, and often includes answers. I guess this is
    an instance of (2).

- Explaining the mental images/mental pictures that the author has.
- Anticipating common misconceptions and errors.
- When something introduced at an "introductory level" is slightly
  inaccurate or is a simplification, this should be mentioned (to
  avoid the learner memorizing definitions that will be superseded).

  Example: Tadelis's _Game Theory: An Introduction_ slowly introduces
  ideas like IESDS and rationalizability---first in the context of
  static games of complete information without mixed strategies, then
  with mixed strategies ("IESDS and Rationalizability Revisited").

  [Example](https://en.wikipedia.org/wiki/Extensive-form_game#Finite_extensive-form_games):
  "Some authors, particularly in introductory textbooks, initially
  define the extensive-form game as being just a game tree with
  payoffs (no imperfect or incomplete information), and add the other
  elements in subsequent chapters as refinements."

  Thing that might look like an example that I don't think is an
  example: teaching classical physics before relativity.

- Using lots of pictures (Pugh's analysis book emphasizes this). I
  find many verbal/formula-based explanations much harder to follow
  (it's often easier to just write down the formula myself).

- Giving full solutions to exercises. How should we distinguish
  "examples"/"theorems" from "exercises"? Normally we tend to think of
  "examples"/"theorems" as the proofs that some with solutions, and
  "exercises" as the proofs that the reader must fill in. But I think
  a better way to do this is for examples/theorems to be the ones that
  the reader can't be expected to give (examples that emphasize a
  certain point, a theorem that uses a particular new trick), and
  exercises to be everything else. I like the way Terence Tao leaves
  many things to exercises in his _Analysis I_.

  For solutions, I think it's additionally important to present
  _multiple_ solutions for each problem. At least one of the AoPS
  books (_Intermediate Counting & Probability_) does this to some
  extent, which I like. It's pretty annoying to work hard on an
  exercise, and think that I have got it, only to find the solution in
  the book does it some different way (which is a learning opportunity
  to be sure, but also means I can't really check my solution).

- Making the reader do a lot of work: Leary & Kristiansen's logic book
  uses a phrase that goes something like "the unique readability
  theorem is one of those results that's important to know and good to
  prove oneself, but boring to read". Actually I think many results
  are like this, at least in the weaker sense that they are
  interesting to read but more interesting if you prove it yourself.

  Also see generation/testing/pre-testing effect.

- Presenting multiple organizations of a material: the only way to do
  this right now is to just look at multiple books. But I think a good
  textbook should take the initiative and present multiple ways of
  doing things (both at the low level of multiple proofs of a theorem
  and at the high level of multiple ways of organizing the subject).
  See also reverse mathematics and John Stillwell's books.

- I think when people try to explain mathematics, by default they ask
  something like "how do I talk about this subject so as to cover all
  the main points?" But I think the important question is more like
  "how can I create a transformation such that, if I apply this
  transformation to other minds, they become competent in the
  subject?"

Tutorial vs reference style: some explanations are written in tutorial style, where there's a lot of context throughout the whole document, and you should just start at the beginning and walk through the document. There are also more reference style documents that depend on less immediate context. Some supposedly tutorial style writing can start to feel like reference style writing when they list a lot of theorems/proofs without much motivation.

Personally I find a lot of tutorial-based explanations difficult to follow because I can't keep a lot of things in my head at once, unless I'm the one generating the thoughts (for instance, when I'm programming I can keep many variables fresh in my mind, but when I'm reading someone else's code I find it difficult to do the same). I wish more [variable/term tables](https://machinelearning.subwiki.org/wiki/Summary_table_of_probability_terms#Table) were given in math explanations so that if one forgets the context one can periodically look it up again without scrolling all over the place.

Actually though, I suspect it's not the tutorial format that is the
problem, but rather the tutorial-writer's too-high expectations of the
tutorial-reader. If the writer took the effort to break things down
more and to have e.g. Anki cards available to help the reader, then I
think a tutorial format would still be the best way to learn.

Being clear about ontology helps, I think, and helps to avoid confusing exposition. Something I don't like is when $\frac{dy}{dx}$ is treated both as a function and as a variable. In my world, variables cannot change once you assign them a value. It doesn't make sense to talk about "let $x=3$ and see what happens as $x$ increases", because everything is static. If you want to talk about changes, you define a *static* lookup table, i.e. a function. And a function is not some machine that computes outputs from inputs; it is just a graph. Of course, once you learn the subject, you can freely go between various mental images (including ones that would be confusing to a beginner).

Maybe it makes sense for some people to think of variables as changing, but the fact remains that you *can* formalize this in logic without any moving parts.

On page 21 of [these notes](http://cs229.stanford.edu/section/cs229-linalg.pdf) the notational confusion of $\nabla f(Ax)$ (where $A$ is an $m$ by $n$ matrix and $f : \mathbf R^m \to \mathbf R^n$ is a function) is mentioned.

It seems like a lot of people complain about poor notation but then they just get used to it. Whereas I have something like a gag reflex to confusing notation and have difficulty understanding explanations until they use good notation.

My [[MATH 334]] page talks about the confusing notation of the chain rule too.

[This guide to backpropagation](http://www.cl.cam.ac.uk/archive/mjcg/plans/Backpropagation.pdf) by [Michael J. C. Gordon](!w) is interesting, especially since he spends a lot of time reviewing basic calculus results and understands functional programming (likes functions more than expressions, and defines types!). Unfortunately I find some *other* notational issues, like the difficulty of distinguishing between multiplication and function application (the latter is a space like in Haskell, but it's sort of hard to tell between an explicit space and the kerning).

Since in my experience most exposition is horrible, I am a big fan of shopping around to find the really good books. Not sure I've really succeeded in doing this for ML though.

# External links

- [Reflections on working through Tao's Analysis](https://machinelearning.subwiki.org/wiki/User:IssaRice/Reflections_on_working_through_Tao's_Analysis)
