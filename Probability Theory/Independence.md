Dependencies: [[Joint, Marginal, and Conditional Distributions]]

## Introduction
We've introduced the joint, marginal, and conditional distributions to reason about probabilities of two (or more) random variables. In particular, the conditional distribution provides information about how two random variables depend on one another. One natural question that arises is: what is the conditional distribution of $Y\mid X$ when $Y$ does not depend on $X$? In this case, the conditional distribution should not depend on $X$: we would have $P_{Y\mid X}(y\mid x) = f(y)$. To find the function $f$, note that by the definition of the marginal over $Y$:$$P_Y(y) = \sum_{x} P_{Y\mid X}(y\mid x) P_X(x) = f(y)\sum_x P_X(x) = f(y)$$so therefore $f$ is the marginal $P_Y$, and we see that when two random variables $X, Y$ are **independent**, the conditional $Y\mid X$ is equal to the marginal over $Y$ for all values of $X$. Equivalently, in terms of the joint distribution:$$P_{X, Y}(x, y) = P_{Y\mid X}(y\mid x) P_X(x) = P_Y(y) P_X(x)$$so the joint distribution of two independent variables is simply the product of the marginals. 

Note that this occurs if and only if the joint distribution can be factored into expressions $f(x)$ and $g(y)$ that only depend on one variable. Our definition of independence establishes that the joint distribution of independent variables can be factored as such. To see that this factorization implies independence, let $F = \sum_x f(x)$ and $G = \sum_y g(y)$, and first note that since the total probability must be 1, we have $$1 = \sum_{x, y}P_{X, Y}(x, y) = \sum_{x, y} f(x) g(y) = \left(\sum_x f(x)\right)\left(\sum_y g(y)\right) = FG$$ Now, we compute the marginals and confirm independence:$$\begin{align*}\\P_X(x) &= \sum_y P_{X, Y}(x, y) = \sum_y f(x) g(y) = f(x)\sum_y g(y) = Gf(x) = \dfrac{f(x)}{F}\\ P_Y(y) &= \sum_x P_{X, Y}(x, y)=\sum_x f(x) g(y) = g(y) \sum_x f(x) = Fg(y) = \dfrac{g(y)}{G} \\\Rightarrow\quad P_X(x)P_Y(y)&= \dfrac{f(x)g(y)}{FG} = \dfrac{P_{X, Y}(x, y)}{1}\end{align*}$$We put the marginals in the form that involves division by $F$ and $G$ since this can be interpreted as a "normalization" of the functions $f$ and $g$ to ensure they sum to 1. This makes sense since the marginals must sum to 1.
 ^bc25af

## Definition
Two random variables are called **independent** when the joint distribution is the product of the marginals: $$P_{X, Y}(x, y) = P_X(x)P_Y(y)$$Or, equivalently, when the joint distribution can be factored as $P_{X, Y}(x, y) = f(x)g(y)$, in which case the marginals are given by the normalizations of $f$ and $g$: $$P_X(x) = \dfrac{f(x)}{\sum_x f(x)}\quad\quad P_Y(y) = \dfrac{g(y)}{\sum_y g(y)}$$