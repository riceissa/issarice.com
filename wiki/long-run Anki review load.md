---
title: Long-run Anki review load
author: Issa Rice
created: 2023-07-09
date: 2023-07-09
---

Let's say you add $c$ cards to Anki per day. To simplify calculations for now, let's say the ease factor is an integer, which we'll call $a$, and you never get cards wrong, so each card is reviewed on the day it is created, then $a$ days later; after that, $a^2$ days later; after that, $a^3$ days later, and so on. What does the long-run review load look like? In other words how many cards will be due on day $D$ for some large $D$?

On day $D$, there will be:

- $c$ cards due that were created that day,
- $c$ cards that were created $a$ days ago that are now due,
- $c$ cards that were created $a + a^2$ days ago that are now due,
- ...
- $c$ cards that were created $a + a^2 + \cdots + a^k$ days ago that are now due,

where $k$ is the largest $k$ such that $a + a^2 + \cdots + a^k \leq D$.

The sum $$a + a^2 + \cdots + a^k = \frac{a^{k+1} - a}{a-1}$$ by the geometric series formula.

So we want $\frac{a^{k+1} - a}{a-1} \leq D$. For simplicity, we can just assume $D$ is chosen to be a day such that a $k$ exists that makes the two values exactly equal. Solving for $k$, we get $k = \log_a((a-1)D + a) - 1$.

The actual number of cards due on day $D$ is $c(k+1)$, so finally we obtain $$c\log_a((a-1)D + a)$$ for the number of cards due.

For some reason, prior to going through the math above, I had the mistaken impression that because of spaced repetition's exponential spacing rule, no matter how long I kept using Anki I'd have roughly the same amount of reviews each day. But you can see this is wrong: the review load is logarithmic in the number of days, so the review load grows without bound!

So in the limit of indefinite lifespan, we have a few possibilities:

- We give up on learning new facts after a certain point, or learn fewer and fewer facts as time goes on.
- We "eat the cost", agreeing to the unbounded review load as time goes on.
- We keep deleting cards as time goes on -- maybe once "basic" facts are absorbed, we can delete them and instead have a smaller number of "synthesis" cards or something.
- We use a "superexponential" backoff schedule -- something that makes cards go further out, enough to keep the review load constant.
- (Some sort of technological breakthrough that makes spaced repetition practice unnecessary.)

I find the first three options quite sad (I don't want to stop learning, I don't want burdensome reviews, and I don't want data loss)! And I'm not sure how feasible the third option is. The fourth option is, well, probably what will end up happening but depends on thinking about AI probably so is outside the scope of this note.

Of course, the behavior in the limit might not concern us if we only expect to live a typical human lifespan, and so we can hope the constants are nice enough that the review load stays small. Taking $c=5$ and $a=2.5$ (we started out assuming $a$ is an integer, but there's nothing in the final formula that requires it to be such), we get:

|Year|Review load at start of year|
|-|-:|
|1|5|
|2|34|
|3|38|
|4|40|
|5|42|
|6|43|
|7|44|
|8|45|
|9|46|
|10|46|
|11|47|
|12|47|
|13|48|
|14|48|
|15|49|
|16|49|
|17|50|
|18|50|
|19|50|
|20|50|
|21|51|
|22|51|
|23|51|
|24|52|
|25|52|
|26|52|
|27|52|
|28|52|
|29|53|
|30|53|
|31|53|
|32|53|
|33|53|
|34|53|
|35|54|
|36|54|
|37|54|
|38|54|
|39|54|
|40|54|
|41|55|
|42|55|
|43|55|
|44|55|
|45|55|
|46|55|
|47|55|
|48|55|
|49|56|
|50|56|

# Appendix: simulation

Here's some Python code that will simulate reviews:

```python
#!/usr/bin/env python3

from math import ceil

# each day will be a list of integers giving the interval lengths of the cards
# that are reviewed on that day
days = []

final_load = []

def inner_append(lst, int_idx, val):
    if len(lst) < int_idx + 1:
        for _ in range(int_idx - len(lst) + 1):
            lst.append([])
    lst[int_idx].append(val)

if __name__ == "__main__":
    for n in range(365*50+1):
        # new cards added on this day
        for _ in range(5):
            inner_append(days, int_idx=n, val=3)

        # record the review load for this day
        final_load.append(len(days[n]))

        # do the reviews
        for card in list(days[n]):
            inner_append(days, int_idx=n + card, val=card * 3)
            days[n].remove(card)

        # print("days:", days)
        # print("final_load:", final_load)
    for year in range(50):
        print(f"year {year}: {final_load[365*year]}")
```