# Singular value decomposition: reconciling the "maximal stretching" and spectral theorem views
# In singular value decomposition, how does the spectral theorem discover the maximal stretching vector?

Looking around at various proofs of the singular value decomposition, I have seen two strategies, which I describe below. Let $V$ and $U$ be inner product spaces and $T\colon V\to U$ be a linear map.

1. The idea for the first strategy is to look at the "maximal stretching" of the unit sphere under $T$. Once we find the vector corresponding to this maximal stretching, we ignore the subspace spanned by that vector and continue inductively in the orthogonal complement.

   More concretely, define $v_1$ to be the vector $v\in V$ with $\|v\| =1$ for which the "stretching" $\|Tv\|$ is largest. (Such a vector exists [by compactness](https://math.stackexchange.com/questions/1218376/compactness-argument-in-svd-existence-proof).) Then let $\sigma_1 = \|Tv_1\|$ and $u_1 = \frac{1}{\sigma_1} Tv_1$. We can then show for any $v\in V$ orthogonal to $v_1$ that $Tv$ is orthogonal to $Tv_1$. This means that if we extend $v_1$ to an orthonormal basis $v_1, \ldots, v_n$ of $V$ and $u_1$ to an orthonormal basis $u_1,\ldots,u_m$ of $U$ then the matrix of $T$ with respect to these bases looks like:

   $$\mathcal M(T, (v_1,\ldots,v_n), (u_1,\ldots,u_m)) = \begin{pmatrix}\sigma_1 & 0 \\ 0 & B\end{pmatrix}$$

   And now we can proceed inductively on the linear map defined by $B$.

2. The idea for the second strategy is to apply the spectral theorem to $T^*T$ or $\sqrt{T^*T}$ to get an orthonormal basis of $V$; then we define vectors in $U$ and show that it is orthonormal and has the SVD property we want.

   We start with the observation that $T^*T$ is self-adjoint, so we can apply to spectral theorem to it, obtaining an orthonormal basis $v_1,\ldots,v_n$ consisting of eigenvectors of $T^*T$, so that $T^*Tv_j = \lambda_j v_j$ for $j\in\{1,\ldots,n\}$. Now let $u_j = \lambda_j^{-1/2}Tv_j$. Then

   $$\begin{align}\langle u_j,u_k\rangle &= \lambda_j^{-1/2}\lambda_k^{-1/2}\langle Tv_j,Tv_k \rangle \\ &= \lambda_j^{-1/2}\lambda_k^{-1/2}\langle T^*Tv_j,v_k \rangle \\ &= \lambda_j^{1/2}\lambda_k^{-1/2}\langle v_j,v_k \rangle \end{align}$$

   so that if $j\neq k$ then $\langle u_j,u_k\rangle = 0$ and if $j=k$ then $\langle u_j,u_k\rangle = 1$. This shows that $u_1,\ldots,u_m$ are orthonormal.

My general aim is to try to reconcile these two approaches. But more specifically, my question is, how is the second approach able to find these maximal stretching vectors $v_1,\ldots,v_n$ (my understanding is that the SVD is unique up to )? It is even able to do this without using compactness. It is the spectral theorem that finds the basis $v_1,\ldots,v_n$, and looking at Axler's _Linear Algebra Done Right_ (third edition), this is found using Schur's theorem (6.38 in the book), which uses 6.37, which applies the Gram--Schmidt procedure to the basis of the upper-triangular matrix.

Something that seems strange to me: in Gram--Schmidt, the initial vector is taken as given and only normalized in length. So how can this vector show up in the SVD? -- this is b/c we use the basis from upper-triangular, which is found via existence of an eigenvalue.

I can kind of see how Gram--Schmidt is performing an iterative optimization similar to the iterative maximization in approach (1).
