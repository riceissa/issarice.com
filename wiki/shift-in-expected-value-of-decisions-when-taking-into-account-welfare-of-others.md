---
title: Shift in expected value of decisions when taking into account welfare of others
author: Issa Rice
created: 2018-01-03
date: 2018-01-03
# documentkind:
# status:
# belief:
---

This page makes a basic point, which is that the expected value of personal
decisions shifts when taking into account others' welfare.

Suppose you have a choice between doing something (M) and not doing the thing
(NM). Suppose also that doing the thing can end up as good (GM) or bad (BM).
For concreteness, and to make the exposition clearer, suppose M is the act of
marriage. In that case, NM is choosing not to marry, GM is a good marriage, and
BM is a bad marriage.

Now suppose the utility of each case is described as follows. Beware that I am
just making up numbers! This is just a proof-of-concept to make the general
point!

|Outcome|Utility for self|Utility for others|
|-------|----------------|------------------|
|NM     | $-10$          | $+100$           |
|GM     | $+10$          | $+110$           |
|BM     | $-20$          | $0$              |

A caricature of the situation goes like this:

NM
:   You don't marry, so you take a personal hit to welfare, because you're
    lonely all your life.  On the other hand, you can still pursue altruistic
    activities mostly normally, so utility for others is high.

GM
:   You marry, and it's a good marriage so are happy. Because you are feeling
    good, your altruistic endeavors also go well, so you get a bonus there.

BM
:   You are in a bad marriage, so you take a hit to utility. Maybe you become
    severely depressed, or commit suicide, or you have to pay alimony so you
    can't donate. The individual capacity to suffer is limited, but your
    altruistic output can suffer dramatically.

Now suppose the probability of GM is 0.6. In that case for NM you have:

$$
u_\text{self}(\mathrm{NM}) &= -10 \\
u_\text{self}(\mathrm M)   &= 10p - 20(1-p) \\
                           &= 30p - 20 \\
                           &= -2
$$

Note that the problem I discuss matters much more for people with very high
"altruistic potential".
