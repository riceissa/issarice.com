---
title: CSE 390 (for CSE 142)
author: Issa Rice
created: 2014-12-11
date: 2015-01-14
status: draft
---

This is my course review for CSE 390 at the University of Washington.
I took the course in autumn 2014 with [Stuart Reges](http://homes.cs.washington.edu/~reges/) (as part of [[CSE 142]]), and in winter 2015 with Adam Blank (as part of [[CSE 143]]).
Below I will talk about my experience from autumn 2014; for my experience from winter 2015, see [[CSE 390 (for CSE 143)]].

CSE 390 was by far the most enjoyable course of the quarter.
The university doesn't seem to have strict guidelines for how professors conduct the course, so I suspect the course differs significantly depending on the professor with whom one takes the course.

# Basic structure

As Reges discussed during the first meeting, the course sessions were divided roughly in two parts: the first half would be a discussion based on a book we would read throughout the quarter (for us, it was [Our Final Invention: Artificial Intelligence and the End of the Human Era](https://en.wikipedia.org/wiki/Our_Final_Invention)), while the other half would be a discussion about a topic related to computer science chosen by Reges.

He said to the effect that during his years at Stanford, what he remembered most from his one math class was a TA (or professor?) who would talk about all of the ideas that interested him---so that this course is an attempt for Reges to "recreate the experience".

# The book

Barrat's book was a bit basic for me, since I had already been reading [[LessWrong]] for several years prior to the course.
The content seemed a bit repetitive, and often the arguments seemed to be based solely on Barrat's opinion (which seemed dubious, since he is apparently a documentary maker, and not an expert in AI).
Reges, as well as the class, seemed to find the content repetitive as well.
Although Reges did say that superintelligence is something we have to be concerned about, I got the impression that the class was unconvinced by the idea of a superintelligence.

# Topics that were discussed

As best as I can remember (I forgot to keep a written list), here are all the topics discussed in the second half of each session, roughly in chronological order.

- Reges discussed the topic "What is a meme?"
    - Reference to Richard Dawkins
    - We also read Robert Frost's "The Road Not Taken", though I forget the reason we did this

- Introduction to the idea of meta (Reges' personal obsession)
    - The question posed was: which of there is more, knowledge or meta-knowledge?
    - Muddy children or blue eyes puzzle: see [the relevant xkcd page](https://xkcd.com/blue_eyes.html)

- Dunbar's number; what makes humans unique?
    - I think the question was something like "Why do animals know so much when they're born, but humans don't know anything when they're born?"
    - The idea that humans have culture

- [Card trick](https://web.archive.org/web/20160505181015/http://cs4hs.cs.washington.edu/content/Resources/SessionMaterials/bin-o-slides/Stuart_Reges_cryptography.pdf)
    - Reges gives the anecdote that in one class where he posed the card trick, two students figured it out: one who had solved the puzzle on their own, and one who was resourceful enough to Google "Reges card trick" ...
    - This also happens to be the same one given by Yishan Wong in his answer to "[What's the hardest puzzle question asked at PayPal?](https://www.quora.com/What-s-the-hardest-puzzle-question-asked-at-PayPal/answer/Yishan-Wong)"

- Modular arithmetic and RSA encryption

- [Rubik's cube](!w)
    - We listed some properties of the Rubik's cube

- Automata/Turing machine
    - We used [jflap](http://www.jflap.org/) to make an automaton that figured out if a string was palindromic or not (I think)

- Lack of American pride
    - This one was not really CS, but was amusing nonetheless.
    Essentially, Reges brought in a bunch of books published in the year 1900(?---I think, or perhaps it was 1901), and asked us to take a look through them.
    The thrust was: we found their American exceptionalism, pride, etc., comical; so Reges posed the question: in 100 years, what will people find comical about *us*?
    He gave the thought-experiment of trying to imagine a poster in a second grade classroom that said "The 20th century was the American century."---and how most people would object to this being placed in the classroom (e.g. "it's propaganda!")---but also that no one could really deny this.
    His conclusion was that in 100 years, people will find our reluctance to be proud to be comical.

- History of mathematics (I think this is basically all covered in Logicomix):
    - Cantor
    - Russell
    - Gödel
    - Diagonalization (in particular, we prove that the reals are uncountable[^proof] and discuss the [halting problem](!w))

[^proof]: Watch out for this proof though; Reges might neglect the fact that some reals can be represented in multiple ways in the decimal system.
I pointed this out to him, and he admitted that he likes the subset proof better.

- Is human communication digital or analogue?
    - [Chinese whispers](!w)
    - His main point was that *language* is digital; i.e. that if one wanted to make an exact copy of a message, one could[^whisper].
    However, he also argued that prior to language, people communicated in an analogue fashion, using grunts, pointing at things, etc.
    He said that whenever people way "oh I just can't quite express my feelings" they are essentially saying that on a visceral or analogue sense they understand, but that they can't "encode" the feeling digitally.
    Another example in this category he gave was when people say "I know *exactly* how you feel".

[^whisper]: For this reason, he argued vehemently that most people get the wrong message from Chinese whispers, namely that humans are bad at copying messages.
What the message *should* be, according to Reges, is that *in principle*, i.e. given enough motivation to try, humans *can* succeed at the game.

# Other aspects

Perhaps what made the course entertaining was a number of anecdotes Reges told about famous people he had interacted with (including Peter Thiel and Steve Jobs).
