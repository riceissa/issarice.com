---
title: The irony of LaTeX
author: Issa Rice
created: 2024-09-12
date: 2024-09-12
---

(taking some notes here; i want to organize this better at some point)

- The Computer Modern font was never intended to look so thin. But because the font program that Knuth designed (Metafont) was so complicated to use, almost no one adjusted the "blacker" parameter of the font to a suitable value for their printer (actually this is not quite right; if you take a look at `modes.mf` that comes with TeX Live, you will see that tons of people added their own printer settings. But then the world moved away from Metafont's bitmapped fonts, onto things like Latin Modern, where it was no longer possible to adjust the blacker values!). And for whatever reason, the default value of blacker that everyone used in packaging up the fonts (e.g. Latin Modern) was zero? Or maybe this was fine in the beginning when printers tended to have the ink expand more. But the default situation has been bad for something like 30 years, and no easy solution has been available until New Computer Modern and MLModern came around in 2021 or so? I'm also a little confused whether the bitmapped Computer Modern font was any better than the vector versions (it shouldn't change the thickness?). I'm really confused why, despite the problem being so obvious to many, this problem went uncorrected for so long.
- In general, LaTeX makes it _possible_ to have good typesetting, but it takes work, and most people are not willing to put in that work. So it's quite possible that the creation of LaTeX has led to worse typesetting in the world overall. There's a lesson here about how Knuth was trying to solve a problem that he personally had, but his solution was not a good fit for most people (who don't know as much about typography, who are not motivated to learn about it, who just want a simple system they can use to produce good documents). Arguably it was Leslie Lamport's fault here... he's the one who created LaTeX as an "easy to use" package so that one did not have to learn raw TeX. LaTeX was just easy enough to force people to use it, the competition was just non-existent enough that it easily won(??), but also not good enough to produce good typesetting by default. In going from "hard to use, almost no one uses it" (TeX?) to "easy to use" (LaTeX?) is the decisive moment when a lot of care must be taken to get the defaults right. I think the situation is oddly similar to cryptography (programs like GPG are so hard to use that almost no one uses it; the easier-to-use stuff like Telegram are probably bad in various ways).

# See also

- [[Why use Computer Modern for mathematical typesetting]]