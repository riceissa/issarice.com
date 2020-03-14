I am working through Sutton and Barto's [RL book](http://www.incompleteideas.net/book/the-book.html). So far in the text, when backup diagrams are drawn, the reward and next state are iterated together (i.e. the equations always have $\sum_{s',r}$), because the text uses the four-place function $p(s',r|s,a)$. Starting from a solid circle (state-action pair), each edge has a reward labeled along the edge and the next state labeled on the open circle. (See page 59 for an example diagram, or see Figure 3.4 [here](http://www.incompleteideas.net/book/ebook/node34.html).)

However, exercise 3.29 asks to rewrite the Bellman equations in terms of $p(s'|s,a)$ and $r(s,a)$. This means that the reward is an expected value (i.e. we don't want to iterate over rewards like $\sum_r \cdots (r + \cdots)$), whereas the next states should be iterated (i.e. we want something like $\sum_{s'} p(s'|s,a) (\cdots)$).

I think writing the Bellman equations themselves isn't too difficult; my current guess is that they look like this: $$v_\pi(s) = \sum_a \pi(a|s) \left(r(s,a) + \gamma \sum_{s'} p(s'|s,a) v_\pi(s')\right)$$

$$q_\pi(s,a) = r(s,a) + \gamma \sum_{s'} p(s'|s,a) \sum_{a'} \pi(a'|s') q_\pi(s',a')$$

My problem instead is that I want to be able to draw the backup diagrams corresponding to these equations. Given the "vocabulary" for backup diagrams given in the book (e.g. solid circle = state-action pair, open circle = state, rewards along the edge, probabilities below nodes, maxing over denoted by an arc), I don't know how to represent the fact that the reward and next state are treated differently. Two ideas that don't seem to work:

* If I draw a bunch of edges after the solid circle, that looks like I'm iterating over rewards.
* If I come up with a special kind of edge that represents an expected reward, then it looks like only a single next state is being considered.
