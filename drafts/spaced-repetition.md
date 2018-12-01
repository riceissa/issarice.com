some notes on spaced repetition.

# brief timeline of my usage

* first heard about anki/spaced repetition sometime in 2011-2013, and used it to memorize pretty random things
* stopped using it around 2014
* started using it again in mid-2018, mainly on math

# parallel reading

something i like about anki is that as long as i remember these
definitions, then i can take an arbitrary break from reading a book or
paper, and can return to it again when i get excited. so it allows for
"parallel reading", which is something i like to do but i wasn't so
good at before (due to forgetting things).

# learning things to use later

with spaced repetition it becomes possible to learn things just because
they seem interesting. without some sort of review mechanism, there is
the danger that one learns it "just because" but then forgets it soon
because it's not used for anything.

# creating front and back side separately

as i'm reading something and come up with questions, those
questions can be the front side of an anki card. then if/when i find
the answer, i can make the card (with the answer as the back side).
the problem is that i need to write down or remember the questions i
have. so it's a two-stage process, whereas with making cards for
definitions, i can just do it as i read the textbook.

# upper bound on interval

something i haven't seen discussed by spaced repetition advocates
is how there might be a "limit" to how long you can remember
something. if spaced repetition unboundedly keeps increasing the
interval of review, you might forget things anyway, even with SRS. the
limit might be 10 years, say. so if once review interval goes past 10
years, you just forget it after 10 years. Anki has a deck setting
to adjust this value.

of course, if this biological limit is more like 60 years, then it's
not a problem, because i will likely be dead before my memories'
review interval crosses the limit.

another thing i haven't seen discussed is how old people have worse
memories. so an SRS should probably start _decreasing_ the
interval as the user gets older.

# shifting interests over time

one danger with anki is that
the stuff i need to remember now has changed a lot compared to what i
was using anki for back in 2013 and 2014. This is possibly one reason
why i stopped using anki. (back then, i hadn't figured out how to use
it for math, other than memorizing integrals or trig identities or whatever.)
i memorized a lot of
things for classes, like literary techniques and spanish vocab. but
these things have become unimportant to me.

this also means that, if i want to keep using anki, i should liberally
delete (or suspend) cards from my deck if i no longer need them. the goal is to
keep using anki, and keeping bad cards makes that harder (because i'm
less excited).

# spaced repetition for problems

something i want
is this sort of problem solving review system, like anki. but instead
of these basic flash cards, i'm presented with a problem to solve. the
problem could be new, or it could be one i've seen before, or it could
be a variation on one i've seen before. and the idea is to keep me
sharp so i don't forget how to solve problems i've learned how to
solve.

maybe this sort of thing is possible using a separate anki deck with
custom spacing parameters. i think it would be annoying if i was asked
to solve the same problem 1 day later or 4 days later or whatever (at
the initial stages). so maybe the deck would be customized so that
even in the beginning ("learning stages" of the card) i would only be
shown the same problem after a week or more.

maybe the more important point is that i'd like this anki stuff
to be done automatically... i don't want to have to put in all this
effort to making my own cards, checking LaTeX formatting etc. etc. The
cards really should just be "created at the speed of thought".

the real kind of anki repetions i want
are very dynamic, where e.g. i'm asked to prove the chain rule, and if
i get stuck, it maybe asks a more basic question that's related. or it
drills down into a specific part of the proof. or it digs into where
exactly i'm confused, and makes more basic "cards" out of those. and
these resulting "cards" might not even be about things i know well
(i.e. it violates the "understand before you remember" rule from the
20 rules).

in short, it would be like having a conversation with somebody who
knew a lot of math and could explain things well. and this person
would be equipped with the review scheduling for the things i'm trying
to learn.

# forgetting surrounding parts

one worry i have with anki
is that i will remember the specific question-answer pairs for a long
time, but that as time goes on, i will remember _only_ those, and will
forget the general subject. so i might remember the intuition behind
newton's approximation, but i won't know how to apply it or won't
remember that it's useful in proving the chain rule. it's hard to
detect the things i forget. and right now, if a subject is still fresh
in my mind, it's not obvious to me that i will forget these "filler"
parts of the subject (i.e. the parts that haven't been ankified).

Feynman says that one can ["triangulate"](https://www.quora.com/Do-grad-school-students-remember-everything-they-were-taught-in-college-all-the-time/answer/Mark-Eichenlaub)
as one gains expertise, to fill in the missing parts.

# whether to retain partial understanding

sometimes, i'm only somewhat sure of a mathematical fact, and i don't
want to make a card for it and commit it to memory until i figure out
better whether it is true or not.

e.g. with aumann agreement, there are lots of things i figured out,
but also where i'm not certain my interpretation is correct. so
i don't want to start making lots of cards _yet_. but what if i never
figure it out? what if now i get bored of this and move on to another
thing, and never make the card?

it's like, i want to retain this partial understanding too! but _do_ i
want to retain this partial understanding?

# flexibility of key-value pairs (or: against "anki can't be used for complex structures")

i think people like to complain that anki is just key-value pairs, but
consider the following:

1. a deck with just (key1, value1), (key2, value2), ... where the different
   pairs have nothing to do with each other.
2. a deck with key-value pairs, where one key might talk about another
   key, or a key might talk about the value of another key. In other
   words, the key-value pairs have a greater structure about them.

examples of (2) might be:

- overlapping cloze deletions to memorize a list
- a linked list, where key\_j asks "what is
  key\_{j+1}
- a tree, where some cards ask for _two_ things, left and right.

My point is that using just key-value pairs, you can build way more
complicated structures. if you look at just the front/back sides of
anki cards _in isolation_ you will only see a dictionary. But if you
look at a deck more holistically, you can start to see greater
structure (in the decks that are made well).

# manual spacing for math

here's another spacing idea for learning math:
work for five days through a book, and then on the sixth day (say) you
go back to review the things you studied on the first day and try to
do the problems there (especially the hard ones). And on the seventh
day, you do that for what you studied the second day, and so on. So
after a while, each day you learn new things plus review what you did
five days ago. And then, maybe you also review what you did fourteen
days ago as well (after the fourteenth day). The idea is that you keep
adding reviews from days reaching back more into the past, but that
the review should take less time each round, so your total study time
shouldn't keep increasing.

i'm not sure how this compares to anki. i guess the anki algorithm is
more efficient and you only test small things each time. but on the
other hand, entering things into anki takes more time than just
flipping back in a book.

# burying cards to speed up review (technique for avoiding accumulation of reviews)

one day i got busy reading things and so procrastinated on doing my anki
reviews. finally it was nearing 1am and i'm like "ugh, well maybe i
can just do the ones that don't require a pencil and paper, and just
bury the cards that require paper". i did that, and ended up spending
only 14 mins on reviews, and reviewed 94 cards. the reviews felt
really easy too! i guess maybe the ones that require writing are just
much harder or something. or maybe the transition from screen to paper
to screen is somehow bad on my attention? it's pretty weird how easy
the review felt.

On the other hand, i really don't know how to convert the pencil-paper cards to
_not_ use paper. for example, i just don't trust myself to write kanji
"in my head" and be able to check with the answer. same with
complicated definitions (e.g. nested quantifiers). for these cases, i
think my current system (where i test the whole definition at once) is
the best. like it makes sure i actually know the whole thing.

so my main takeaway i guess is that if review seems tedious, just skip
the cards that make you struggle!

# overfitting in anki

i can tell when i am relying on the fact that a card is already in
anki. like, my brain goes "oh yea that one" and gives the answer. but
if i had seen the same "prompt" outside of anki, i would have to first
make sure it /is/ the same prompt; i can't just go "oh yeah i know
this", i have to make sure it really is like what i entered in anki.
so this is a bit concerning. like, can i really apply what i've
memorized in real life?

# confirmation bias

For storing ideas/quotes, i wonder if i am biased toward storing sentences in anki that i agree with,
so then i end up in a nasty process where i am remembering only
sentences i agree with. i should say that i _do_ store sentences i
find only "interesting" without necessarily agreeing or disagreeing
with it. sort of like, i just want to keep this sentence in my mind to
play with, so that i may discover its truth or falsefood as i gain more experience.
but i don't think i've entered anything i actively disagree with. and
i'm not sure i should, but it seems like that could combat some sort
of confirmation bias problem.
