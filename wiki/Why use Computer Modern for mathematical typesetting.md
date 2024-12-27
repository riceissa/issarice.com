---
title: Why use Computer Modern for mathematical typesetting?
author: Issa Rice
created: 2024-10-06
date: 2024-10-06
---

- It fairly clearly distinguishes some similar-looking characters like the lowercase "v" and the Greek letter nu: $v$ vs $\nu$, lowercase "a" vs Greek alpha: $a$ vs $\alpha$.
- The parentheses are a bit taller so without any special effort (e.g. the use of `\left(\right)` it encloses subscripts and superscripts). e.g. see $(a^5_3)$.
- It emulates the look of classical mathematics papers and textbooks. Perhaps math papers and books look this way for bad reasons, but I don't think many of us actually know whether that's true.
- It's already in use by a lot of textbooks and papers and MathJax, WordPress. People are used to seeing it. This is important for mathematical typesetting because in math it's often important to be able to distinguish single letters in a context-free way (i.e. without being able to rely on surrounding letters). When I read texts using other mathematics fonts, I'm often confused e.g. "is this a script f? or maybe it's fraktur?", "is this symbol in bold, or is it just the way this font looks?"

The main (and rather large) downside is the Computer Modern is a very delicate font, so its appearance depends a lot on the "viewing conditions" (quality of the monitor, quality of your PDF font rendering system, quality of your printer/paper). Sometimes it can look quite good, other times it is mostly okay with some weird artifacts, and other times it's awful. In particular, it often comes out looking too thin, and even the thicker variant New Computer Modern can look kind of blurry on some PDF viewers I have tried. So despite its good design, it *may* be best to stick to Computer Modern in situations where one can control the output device.