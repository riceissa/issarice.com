---
title: Math explanations
author: Issa Rice
created: 2017-12-25
---

I've been thinking more about math explanations again (something I used to think a lot about when I was first learning abstract math) because I'm trying to get a good understanding of machine learning, particularly what makes them good or bad. This is an [ignorant thinking](https://meteuphoric.wordpress.com/2011/08/27/in-defence-of-ignorant-thinking/) page for now, so don't expect me to know anything about the topic.

In my mind some things that make explanations good are:

- Writing for the right background. I think many books are not giving the background with sufficient specificity. Like they give general topics like "basic probability" without clarifying what that means, even though the meaning changes depending on location and generation.
- Anticipating questions. It really frustrates me when a writer explains something, then doesn't explain some follow up point that is important to me. On the other hand, it feels satisfying when I ask a question in my mind, and immediately in the next sentence or paragraph the writer answers it. I feel like this is especially import to do with written content. With in-person explanations or interactive discussions, it might be less important to anticipate everything beforehand. And anticipating everything is hard because there are a lot of things someone could ask.
- Giving good motivations. Not doing this properly would be things like giving a definition without writing about how it is thought of in practice, or giving alternative formulations and things like that.
- Giving good examples. I feel like this has something to do with writing good unit tests in software engineering. Like you want to get the good edge cases covered.
- Filling in a lot of details. This is sort of similar to the anticipating questions one, but I get frustrated when a lot of steps are skipped. Because in writing the book, the author had to take the same mental steps, and yet they are not recording those steps! It's like they encode their steps into this really strangely terse format, and then when you read the text you have to do the decoding. Why not just write it out verbosely and save us a step?
- Notation. Maybe this is just me, but I generally don't like things like not explicitly bounding bounded variables (e.g. writing $\sum_i f(x_i)$ instead of $\sum_{i\in S} f(x_i)$), writing expressions but calling them functions (e.g. "let $f(x)$ be a function ..."), not introducing each variable (e.g. using variables like $f$ without saying "let $f : X \to Y$ be a function" first), not exposing types (e.g. when using random variables and saying things like $P(X = x)$, what is the type of $=$?).

Tutorial vs reference style: some explanations are written in tutorial style, where there's a lot of context throughout the whole document, and you should just start at the beginning and walk through the document. There are also more reference style documents that depend on less immediate context. Some supposedly tutorial style writing can start to feel like reference style writing when they list a lot of theorems/proofs without much motivation.

Since in my experience most exposition is horrible, I am a big fan of shopping around to find the really good books. Not sure I've really succeeded in doing this for ML though.
