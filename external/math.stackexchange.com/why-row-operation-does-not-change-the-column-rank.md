Here is an elaboration on Lord Shark the Unknown's answer. Let $A$ be the original matrix, let $E$ be an elementary matrix, and let $B := EA$ be the new matrix. Let $k$ be the dimension of the column space of $A$, and let $r$ be the dimension of the column space of $B$. Then there is some way to choose $k$ of the columns of $A$ that are linearly independent. After we apply the row operations to these columns, the new list (which lives in the column space of $B$) is also linearly independent, so we must have $r \geq k$. Now we can do the same thing starting with the columns of $B$: choose $r$ that are linearly independent, apply the inverse row operation, obtain $r$ linearly independent vectors in the column space of $A$, and conclude $k \geq r$.

---

Here is a more explicit/concrete answer.

Let $A$ be an $m\times n$ matrix and let $C_1,\ldots,C_n$ be the columns of $A$. If $e_1,\ldots,e_n$ is the standard basis, this means $Ae_j = C_j$ for $j \in \{1,\ldots,n\}$. If $E$ is an elementary matrix, then the result of applying this row operation to $A$ is $B:=EA$. So the columns of $B$ are $Be_j = EAe_j = EC_j$. In other words, to get the columns of the new matrix, we can just apply the row operation separately to each column.


We want to show that $\dim \operatorname{span}(C_1,\ldots,C_n) = \dim \operatorname{span}(EC_1,\ldots,EC_n)$. Every spanning list contains a basis, so we can choose columns $C_{n_1},\ldots,C_{n_k}$ of $A$ which are linearly independent and which span the column space of $A$ (i.e. $\operatorname{span}(C_1,\ldots,C_n) = \operatorname{span}(C_{n_1},\ldots,C_{n_k})$).

Now consider the list $EC_{n_1},\ldots,EC_{n_k}$, which are the corresponding columns of $B$. We claim that this is a basis for the column space of $B$. Suppose $a_1EC_{n_1} + \cdots + a_kEC_{n_k} = 0$ for some choice of constants $a_1,\ldots,a_k$. Then we can apply $E^{-1}$ to both sides to conclude that $a_1C_{n_1} + \cdots + a_kC_{n_k} = 0$. Since $C_{n_1},\ldots,C_{n_k}$ are linearly independent, we must have $a_1 = \cdots = a_k = 0$. Thus $EC_{n_1},\ldots,EC_{n_k}$ are linearly independent.

Now let $v:=b_1EC_1 + \cdots + b_nEC_n$ be a vector in the column space of $B$. Applying $E^{-1}$ we obtain $E^{-1}v= b_1C_1 + \cdots + b_nC_n$. Thus $E^{-1}v$ is in the column space of $A$. Since $C_{n_1},\ldots,C_{n_k}$ is a basis for the column space of $A$, this means we can write $E^{-1}v = c_1C_{n_1} + \cdots + c_kC_{n_k}$ for some choice of constants $c_1,\ldots,c_k$. Applying $E$ we have $v = EE^{-1}v = c_1EC_{n_1} + \cdots + c_kEC_{n_k}$. Thus we have written $v$ as a linear combination of $EC_{n_1},\ldots,EC_{n_k}$, so this list spans the column space of $B$.

Thus $EC_{n_1},\ldots,EC_{n_k}$ is a basis of $\operatorname{span}(EC_1,\ldots,EC_n)$. Now we have $$\begin{align}\dim \operatorname{span}(C_1,\ldots,C_n) &= \dim\operatorname{span}(C_{n_1},\ldots,C_{n_k}) \\ &=k \\ &= \dim\operatorname{span}(EC_{n_1},\ldots,EC_{n_k}) \\ &= \dim\operatorname{span}(EC_1,\ldots,EC_n)\end{align}$$
