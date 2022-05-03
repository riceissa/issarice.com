---
title: "Mathematics and notation"
date: 2015-10-29
---

Despite mathematicians' apparent focus on notation, I've always found it difficult to navigate certain notation in math.
In fact, although I am only up to the level of undergraduate mathematics in the US, I might say that the chief difficulty so far has been with notation, not some intrinsic difficulty of the subject (for, if mathematics is merely verbal and a sequence of tautologies, then the ability to follow instructions is all that is necessary---until the instructions are obscured by poor notation!).

Part of the problem is that there is a lot in notation that is *implicit*.
When talking about mathematics in person, there is no need to specify all the context, because if anything is unclear, one can just ask and it will be clarified verbally.

I like what James Morrow (my math 334 instructor) said when discussing the multivariable chain rule:

$$
\frac{\partial z}{\partial x_1} = \frac{\partial z}{\partial y_1} \frac{\partial y_1}{\partial x_1} + \cdots + \frac{\partial z}{\partial y_n} \frac{\partial y_n}{\partial x_1}
$$

> Writing it down this way is okay, but you have to understand what the symbols mean [...] It's an efficient way to write it down [...] I think you'll get used to it [...] The exercises [in the book] are meant to show you that it's easy to mess it up [...] Chemists don't tell you which variable they're keeping constant [...] There's a lot that's implicit and it's hard to tell what's going on.

I also like [AbstractMath.org](https://web.archive.org/web/20170609022717/http://abstractmath.org/).

Another example with partial derivatives (inspired by an ambiguity that Terence Tao touched on in his *Analysis II*): define $f : \mathbf{R}^2 \to \mathbf{R}$ as $(x,y) \mapsto x^2$ and $g:\mathbf{R}^2 \to \mathbf{R}$ as $(x,y)\mapsto y^2$.
Observe that we have $f(x,x) = g(x,x) = x^2$.
Trick question: what is $\frac{\partial}{\partial x} x^2$?

If we mean to take $\frac{\partial f}{\partial x} (x,x)$, then this is
$$ \left.\frac{\partial f}{\partial x} (x,y) \right|_{(x,x)} = 2x$$
On the other hand, if we mean $\frac{\partial g}{\partial x} (x,x)$, then this is 
$$\left.\frac{\partial g}{\partial x} (x,y) \right|_{(x,x)} = 0$$

Folland gives other examples of when the partial derivative notation doesn't make any sense (it can mean two different things).
