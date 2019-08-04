This post describes a pattern of abstraction that is common in mathematics, but which I haven't seen described in explicit terms elsewhere. I would appreciate pointers to any existing discussions.

Note on prerequisites for this post: in the opening example below, I assume familiarity with linear algebra and plane geometry, so this post probably won't make much sense without at least some superficial knowledge of these subjects. In the second part of the post, I give a bunch of further examples of the phenomenon, but these examples are all independent, so if you haven't studied a particular subject before, that example might not make sense, but you can just skip it and move on to the ones you do understand.

There is something peculiar about the dependency of the following concepts in math:

* Pythagorean theorem
* Law of cosines
* Angle between two vectors
* Dot product
* Inner product

One of the most striking examples of generalization in mathematics is the definition of the inner product. The inner product is typically [defined](https://en.wikipedia.org/wiki/Inner_product_space#Definition) using a list of funny properties. But these properties came from somewhere, and it is often a good bet to look at some concrete motivating examples, to see where the abstract definition came from.

So let us look at the Euclidean geometry of $\mathbf R^2$ (the plane) and $\mathbf R^3$ (three-dimensional space). I will give just a brief outline here, as a detailed discussion of Euclidean geometry would obscure the main point.

To get to the inner product (dot product) in Euclidean geometry, one typically goes through a series of steps like this:

1. Using the [axioms of Euclidean geometry](https://en.wikipedia.org/wiki/Euclidean_geometry#Axioms) (in particular the [parallel postulate](https://en.wikipedia.org/wiki/Parallel_postulate)), we prove the [Pythagorean theorem](https://en.wikipedia.org/wiki/Pythagorean_theorem).
2. We take the right angle to have angle $\pi/2$ and calculate other angles in terms of this one.
3. The Pythagorean theorem allows us to prove the [law of cosines](https://en.wikipedia.org/wiki/Law_of_cosines).
4. Now we make the [Cartesian leap](https://en.wikipedia.org/wiki/Cartesian_coordinate_system) to analytic geometry, and start treating points as strings of numbers in some coordinate system. In particular, the Pythagorean theorem now gives us a formula for the distance between two points, and the law of cosines can also be restated in terms of coordinates.
5. Playing around with the law of cosines (stated in terms of coordinates) yields the formula $x_1y_1 + x_2y_2 = \|(x_1,x_2)\| \|(y_1,y_2)\| \cos \theta$ (and similarly for three dimensions), which motivates us to define the dot product (as the quantity equaling $x_1y_1 + x_2y_2 = \|(x_1,x_2)\| \|(y_1,y_2)\| \cos \theta$).

In other words, we take angle and distance as primitive, and derive the inner product (which is the dot product).

But now, consider what we do in (abstract) linear algebra:

1. We have a vector space, which is a structured space satisfying some [funny axioms](https://en.wikipedia.org/wiki/Vector_space#Definition).
2. We define an inner product $\langle v,w\rangle$ between two vectors $v$ and $w$, which again satisfies some funny properties.
3. Using the inner product, we _define_ the length of a vector $v$ as $\|v\| = \sqrt{\langle v,v\rangle}$.
4. Using the inner product, we _define_ the angle between two vectors $v$ and $w$ as the unique number $\theta \in [0,\pi]$ satisfying $\cos \theta = \frac{\langle v,w\rangle}{\|v\| \|w\|}$.
5. Using these definitions of length and angle, we can now verify the Pythagorean theorem and law of cosines.

In other words, we have now taken the inner product as primitive, and derived angle and distance (length) from it.

Here is a shot at describing the general phenomenon:

* We start in a concrete domain, where we have notions A and B, where A is a definition and B is some theorem.
* We find some abstractions/generalizations of the concrete domain
* We realize that in the abstract setting, we want to talk about A and B, but it's not so easy to see how to talk about them (because the setting is so abstract)
* At some point, someone realizes that instead of trying to define A directly, it's better to generalize/"find the principles" that make B tick. We factor out these principles as axioms of B.
* Finally, using B, we can define A.
* We go back and check that in the concrete domain, we can do this same inverted process.

Here are some other examples of this sort of thing in math. In the following examples, the step of using $B$ to define $A$ does not take place.

* Metric spaces: in Euclidean geometry, the triangle inequality is a ''theorem''. But in the theory of metric spaces, the triangle inequality is taken as part of the ''definition''.
