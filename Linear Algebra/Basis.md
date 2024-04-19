Dependencies: [[Linear Independence]]
Resources: [Axler Section 2B](https://linear.axler.net/LADR4e.pdf)
## Introduction
Motivated by the need for a "coordinate system" for vector spaces, we showed that linear independence [[Linear Independence#^7da064|guarantees]] that the coefficients of a linear combination are unique. This implies that, given vectors $\vec x_1, \dots, \vec x_n\in\mathcal V$, if this list is linearly independent, and if $\operatorname{span}\{\vec x_1, \dots, \vec x_n\} = \mathcal V$, then every vector $\vec y\in\mathcal V$ can be expressed as a unique linear combination $\vec y = a_1\vec x_1 + \dots + a_n\vec x_n$. Thus $\vec y$ can be associated with the "coordinates" $(a_1, \dots, a_n)$. There is a name for the vectors $\vec x_1, \dots, \vec x_n$ which both span $\mathcal V$ and are linearly independent: a **basis** for $\mathcal V$.

## Definition
A list $\vec x_1, \dots, \vec x_n$ of vectors in $\mathcal V$ is a **basis** when any vector $\vec y\in\mathcal V$ can be expressed as $\vec y = a_1 \vec x_1 + \dots + a_n\vec x_n$ for a *unique* list of constants $a_1, \dots, a_n\in\mathbb F$. The list $\vec x_1, \dots, \vec x_n$ is a basis if and only if it is linearly independent *and* spans $\mathcal V$.

## Lemmas
**Lemma 1**: Every spanning list contains a basis.
*Proof*: Suppose $\vec x_1, \dots, \vec x_n$ spans $\mathcal V$, but is linearly dependent. We will remove vectors until it is linearly independent. (We start by removing any zero vectors.) Because the list is linearly dependent, we have $a_1 \vec x_1 + \dots + a_n\vec x_n = 0$, with $a_i \neq 0$ for some $i\in\{1, \dots, n\}$. Then, $$\vec x_i = -\sum_{\substack{1\leq j\leq n\\j\neq i}} \frac{a_j}{a_i} \vec x_j$$so $\vec x_i \in\operatorname{span}\{x_j \mid 1\leq j\leq n, j\neq i\}$, i.e. $\vec x_i$ is in the span of the remaining vectors in the list. By [[Linear Combinations and Span#^27ec1a|span lemma 1]], this implies $\operatorname{span}\{x_j \mid 1\leq j\leq n, j\neq i\} = \operatorname{span}\{\vec x_1, \dots, \vec x_n\} = \mathcal V$, i.e. we can remove $\vec x_i$ and obtain a list of vectors which is still spanning. We renumber the remaining vectors to create a list $\vec x_1, \dots, \vec x_{n-1}$, and then we repeat this step until the list is linearly independent. This happens after at most $n$ steps, since the empty list is linearly independent. By this procedure we obtain a linearly independent spanning set, or equivalently, a basis.
**Lemma 2**: All finite-dimensional vector spaces $\mathcal V$ (defined as those with a finite spanning list) have a basis.
*Proof*: By definition, there is a finite list of vectors that spans $\mathcal V$. Lemma 1 tells us that this list can be reduced to a basis.
**Lemma 3**: All 

Left out: 2.32 every linearly independent list extends to a basis, every subspace of 