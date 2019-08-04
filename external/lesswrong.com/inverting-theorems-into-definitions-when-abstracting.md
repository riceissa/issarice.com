This post describes a pattern of abstraction that is common in mathematics, which I haven't seen described in explicit terms elsewhere. I would appreciate pointers to any existing discussions. Also, I would appreciate more examples of this phenomenon, as well as corrections and other insights!

Note on prerequisites for this post: in the opening example below, I assume familiarity with linear algebra and plane geometry, so this post probably won't make much sense without at least some superficial knowledge of these subjects. In the second part of the post, I give a bunch of further examples of the phenomenon, but these examples are all independent, so if you haven't studied a particular subject before, that specific example might not make sense, but you can just skip it and move on to the ones you do understand.

There is something peculiar about the dependency of the following concepts in math:

* Pythagorean theorem
* Law of cosines
* Angle between two vectors
* Dot product
* Inner product

In the Euclidean geometry of $\mathbf R^2$ (the plane) and $\mathbf R^3$ (three-dimensional space), one typically goes through a series of steps like this:

1. Using the [axioms of Euclidean geometry](https://en.wikipedia.org/wiki/Euclidean_geometry#Axioms) (in particular the [parallel postulate](https://en.wikipedia.org/wiki/Parallel_postulate)), we prove the [Pythagorean theorem](https://en.wikipedia.org/wiki/Pythagorean_theorem).
2. We take the right angle to have angle $\pi/2$ and calculate other angles in terms of this one.
3. The Pythagorean theorem allows us to prove the [law of cosines](https://en.wikipedia.org/wiki/Law_of_cosines) (there are many proofs of the law of cosines, but this is one way to do it).
4. Now we make the [Cartesian leap](https://en.wikipedia.org/wiki/Cartesian_coordinate_system) to analytic geometry, and start treating points as strings of numbers in some coordinate system. In particular, the Pythagorean theorem now gives us a formula for the distance between two points, and the law of cosines can also be restated in terms of coordinates.
5. Playing around with the law of cosines (stated in terms of coordinates) yields the [formula](https://en.wikipedia.org/wiki/Dot_product#Definition) $x_1y_1 + x_2y_2 = \|(x_1,x_2)\| \|(y_1,y_2)\| \cos \theta$, where $(x_1,x_2)$ and $(y_1,y_2)$ are two vectors and $\theta$ is the angle between them (and similarly for three dimensions), which motivates us to define the dot product (as being precisely this quantity).

In other words, we take angle and distance as primitive, and derive the inner product (which is the dot product in the case of Euclidean spaces).

But now, consider what we do in (abstract) linear algebra:

1. We have a vector space, which is a structured space satisfying some [funny axioms](https://en.wikipedia.org/wiki/Vector_space#Definition).
2. We define an inner product $\langle v,w\rangle$ between two vectors $v$ and $w$, which again satisfies some [funny properties](https://en.wikipedia.org/wiki/Inner_product_space#Definition).
3. Using the inner product, we _define_ the length of a vector $v$ as $\|v\| = \sqrt{\langle v,v\rangle}$, and the distance between two vectors $v$ and $w$ as $\|v-w\|$.
4. Using the inner product, we _define_ the angle between two non-zero vectors $v$ and $w$ as the unique number $\theta \in [0,\pi]$ satisfying $\cos \theta = \frac{\langle v,w\rangle}{\|v\| \|w\|}$.
5. Using these definitions of length and angle, we can now verify the Pythagorean theorem and law of cosines.

In other words, we have now taken the inner product as primitive, and derived angle, length, and distance from it.

Here is a shot at describing the general phenomenon:

* We start in a concrete domain, where we have two notions $A$ and $B$, where $A$ is a definition and $B$ is some theorem. (In the example above, $A$ is length/angle and $B$ is the inner product, or rather, $B$ is the theorem which states the equivalence of the algebraic and geometric expressions for the dot product.)
* We find some abstractions/generalizations of the concrete domain.
* We realize that in the abstract setting, we want to talk about $A$ and $B$, but it's not so easy to see how to talk about them (because the setting is so abstract).
* At some point, someone realizes that instead of trying to define $A$ directly (as in the concrete case), it's better to generalize/"find the principles" that make $B$ tick. We factor out these principles as axioms of $B$.
* Finally, using $B$, we can define $A$.
* We go back and check that in the concrete domain, we can do this same inverted process.

Here is a table that summarizes this process:

|Notion|Concrete case|Generalized case|
|------|-------------|----------------|
|$A$|primitive; defined on its own terms|defined in terms of $B$|
|$B$|a theorem|defined axiomatically|

In what sense is this pattern of generalization "allowed"? I don't have a satisfying answer here, other than saying that generalizing in this particular way turned out to be useful/interesting. It seems to me that there is a large amount of trial-and-error and art involved in picking the correct theorem to use as the $B$ in the process. I will also say that explicitly verbalizing this process has made me more comfortable about inner product spaces (previously, I just had a vague feeling that "something is not right").

Here are some other examples of this sort of thing in math. In the following examples, the step of using $B$ to define $A$ does not take place (in this sense, the inner product case seems exceptional; I would greatly appreciate hearing about more examples like it).

* Metric spaces: in Euclidean geometry, the triangle inequality is a theorem. But in the theory of metric spaces, the triangle inequality is taken as part of the definition of a metric.
* Sine and cosine: in middle school, we define these functions in terms of angles and ratios of side lengths of a triangle. Then we can prove various things about them, like the power series expansion. When we generalize to complex inputs, we then take the series expansion as the definition.
* Probability: in elementary probability, we define the probability of an event as the number of successful outcomes divided by the number of all possible outcomes. Then we notice that this definition satisfies [some properties](https://en.wikipedia.org/wiki/Probability_axioms#Axioms), namely: (1) the probability is always nonnegative; (2) if an event happens for certain, then its probability is $1$; (3) if we have some mutually exclusive events, then we can find the probability that at least one of them happens by summing their individual probabilities. When we generalize to cases where the outcomes are crazy (namely, countably or uncountably infinite), instead of defining probability as a ratio, we take the properties (1), (2), (3) as the definition.
* Conditional probability: when working with finite sets, we can define the conditional probability as $P(A \mid B) := \frac{|A \cap B|}{|B|}$. We then see that if $\Omega$ is the (finite) sample space, we have $P(A \mid B) = \frac{|A \cap B|}{|B|} = \frac{|A \cap B|/|\Omega|}{|B|/|\Omega|} = \frac{P(A \cap B)}{P(B)}$. But now when we move to infinite sets, we just define the conditional probability as $P(A \mid B) := \frac{P(A \cap B)}{P(B)}$.
* Convergence in metric spaces: in basic real analysis in $\mathbf R$, we say that $\lim_{n\to\infty} a_n = L$ if the sequence $(a_n)_{n=0}^\infty$ satisfies some epsilon condition (this is the definition). Then we can prove that $\lim_{n\to\infty} a_n = L$ if and only if $\lim_{n\to\infty} |a_n - L| = 0$. Then in more general metric spaces, we define "$\lim_{n\to\infty} a_n = L$" to mean that $\lim_{n\to\infty} d(a_n, L) = 0$. (Actually, this example is a little cheating, since we can just take the epsilon condition and swap in $d(a_n,L)$ for $|a_n-L|$.)
* Differentiability: in single-variable calculus, we define the derivative to be $f'(x_0) := \lim_{x \to x_0} \frac{f(x) - f(x_0)}{x-x_0}$ if this limit exists. We can then prove that $f'(x_0) = L$ if and only if $\lim_{x\to x_0} \frac{|f(x) - (f(x_0) + L(x-x_0))|}{|x-x_0|} =0$. This latter limit is an expression that makes sense in the several-variable setting, and is what we use to define differentiability.
* Continuity: in basic real analysis, we define continuity using an epsilon–delta condition. Later, we prove that this is equivalent to some statement involving open sets. Then in general topology we take the open sets statement as the definition of continuity.
* (Informal.) Arithmetic: in elementary school arithmetic, we "intuitively apprehend" the rational numbers. We discover (as theorems) that two rational numbers $a/b$ and $c/d$ are equal if and only if $ad = bc$, and that the rationals have the addition rule $a/b + c/d = (ad+bc)/(bd)$. But in the formal construction of number systems, we define the rationals as equivalence classes of pairs of integers (with second coordinate is non-zero), where $(a,b) \sim (c,d)$ iff $ad=bc$, and define addition on the rationals by $(a,b) + (c,d) := (ad+bc,bd)$. Here we aren't really even generalizing anything, just formalizing our intuitions.
* (Somewhat speculative.) Variance: if a random variable $X$ has a normal distribution, its probability density can be parametrized by two parameters, $\mu$ and $\sigma^2$, which have intuitive appeal (by varying these parameters, we can change the shape of the bell curve in predictable ways). Then we find out that $\sigma^2$ has the property $\sigma^2 = \mathbf E[(X-\mu)^2]$. This motivates us to define the variance as $\mathbf E[(X-\mu)^2]$ for other random variables (which might not have such nice parametrizations).
