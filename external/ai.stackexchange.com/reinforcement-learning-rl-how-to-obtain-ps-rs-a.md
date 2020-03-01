At first, like Neil Slater says, I thought this could only be solved using the expected rewards instead of actual rewards, or else there wasn't enough information to solve it. But now I think there might be a way to solve this question. Here is my thinking on this problem (I would be curious for anyone's thoughts, as I am working through this book myself).

I think the key part is where the book says:

> Each can collected by the robot counts as a unit reward, whereas a reward of $-3$ results whenever the robot has to be rescued.

This means that the reward set is actually $\mathcal R = \{0, 1, -3\}$ (we assume that in each timestep, the robot can only collect one can).

Now using $$r(s,a,s') = \sum_r r \frac{p(s',r\mid s,a)}{p(s'\mid s,a)} \tag{3.6}$$ and $$p(s'\mid s,a) = \sum_r p(s',r\mid s,a)\tag{3.4}$$ it seems possible to solve for all the probabilities. I'll do an example for $(s,a,s') = (\mathtt{high}, \mathtt{search}, \mathtt{high})$ and leave the rest to you.

Equation 3.6 gives $$r_\mathtt{search} = 0\cdot \frac{p(s', 0 \mid s,a)}{\alpha} + 1\cdot \frac{p(s', 1 \mid s,a)}{\alpha} -3\cdot \frac{p(s', -3 \mid s,a)}{\alpha}$$ Since $p(s', -3 \mid s,a) = 0$ (it's impossible for the robot to have to be rescued, since we started in the "high" state), we get $p(s', 1 \mid s,a) = \alpha r_\mathtt{search}$.

Now equation 3.4 gives $$\alpha = p(s', 0 \mid s,a) + p(s', 1 \mid s,a) + p(s', -3 \mid s,a)$$ which solves to $p(s', 0 \mid s,a) = \alpha - \alpha r_\mathtt{search}$.

So the first two rows of the table will look like:

$$\begin{array}{cccc|c}
s& a & s' & r & p(s',r\mid s,a)\\ \hline
\mathtt{high} & \mathtt{search} & \mathtt{high} & 1 & \alpha r_\mathtt{search}\\
\mathtt{high} & \mathtt{search} & \mathtt{high} & 0 & \alpha (1- r_\mathtt{search})
\end{array}$$
