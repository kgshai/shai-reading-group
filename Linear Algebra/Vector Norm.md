Dependencies: [[Vector]]
## Introduction
Sometimes we need to measure the size of a vector. To do this, we use a **norm**, a function that takes vectors and returns a number. The most common norms belong to a family called the $L^p$ norms: $$\lVert \vec x\rVert_p  = \left(\sum_i \lvert x_i\rvert^p\right)^{1/p}$$The most famous of these is the $L^2$ norm, which measures Euclidean distance according to the Pythagorean theorem: $$\lVert x\rVert_2 = \sqrt{\sum_i \lvert x_i\rvert^2}$$(We have kept the absolute value because $x_i$ may be complex, but they can be ignored for real $x_i$. However, they cannot be ignored even for real $x_i$ for other values of $p$, including $p = 1$!)

All $L^p$ norms, including the $L^2$ norm, have the following properties:
- $\lVert \vec 0 \rVert = 0$
- $\lVert \vec x + \vec y\rVert \leq \lVert \vec x\rVert + \lVert \vec y\rVert$ (Triangle Inequality)
- For all $\alpha\in\mathbb R$, $\lVert \alpha\vec x\rVert = \lvert\alpha\rvert\cdot \lVert\vec x\rVert$ 
The rigorous definition of a norm is any function mapping vectors to real numbers that satisfies these properties.

In many applications, we wish to distinguish between zero and small, nonzero numbers. The $L^2$ norm is not sufficient for this because it squares the small, nonzero numbers, making them too small. For this, we use the $L^1$ norm: $\lVert\vec x\rVert_1 = \sum_i \lvert x_i\rvert$. Every time an element of $\vec x$ moves away from 0 by a small amount $\varepsilon$, the $L^1$ norm increases by $\varepsilon$.

One other norm that appears is the $L^{\infty}$ norm, also known as the **max norm**, equivalent to the maximum magnitude of any element of a vector: $\lVert \vec x\rVert_{\infty} = \max_i \lvert x_i\rvert$.

Lastly, we sometimes wish to measure the size of a matrix, for which we use a matrix equivalent of the $L^2$ norm, called the **Frobenius norm**: $\lVert A\rVert_F = \sqrt{\sum_{i, j} A_{ij}^2}$.