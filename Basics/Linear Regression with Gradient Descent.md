Dependencies: [[Least Squares Linear Regression]]
External Resources: [Towards Data Science](https://towardsdatascience.com/linear-regression-using-gradient-descent-97a6c8700931)
Author: --- 

## Summary/TLDR
- high level, intuitive explanation before technical material (TLDR)
- statement of why we care
## Introduction
What if we had a more complicated model, and we couldn't use some of the geometric tricks we did above? We could alternatively find the optimal parameters $\vec\beta^*$ via **Gradient Descent**. We can start with any old value for $\vec\beta$, which we'll call $\vec\beta_0$. We'll choose $\vec\beta_0 = 0$. This is called an **initialization**. We iteratively calculate $\vec\beta_1, \vec \beta_2,$ and so on, so that each time we reduce the sum-of-squares, which we now call our **loss function** $L(\vec\beta) = \lVert X\vec\beta - \vec y\rVert^2_2$. But what direction should we nudge $\vec\beta$ to reduce the loss? ^54bd3d

We can again draw a picture, but this time, Instead of thinking about $\mathbb{R}^n$, we think about the **parameter space** $\mathbb R^m$. The picture is shown below, with a heat map showing the value of the loss function across parameter space, and lines showing level sets (parameter vectors $\vec\beta$ with constant loss $L(\vec\beta)$.) As you can see, the fastest path to the minimum takes small steps that are orthogonal to the level sets. Specifically, they move in the direction of the negative gradient, or  $-\nabla_{\vec\beta} L \vert_{\vec\beta_i}$. We'll show this formally using a Taylor Series around $\vec\beta_i$.
![[Screenshot 2023-10-06 at 3.56.24 PM.png]]
- move in direction of steepest descent
As we can see, we can minimize $L(\vec\beta)$ by taking small steps in the direction of *maximum local descent*. Locally, any continuous loss function looks linear, so near the current value $\vec\beta_i$ we can write out a Taylor series expansion, keeping only the linear term:
$$L(\vec\beta) \approx L(\vec\beta_i) + \nabla_{\vec\beta} L \vert_{\vec\beta_i} \cdot (\vec\beta-\vec\beta_i) \qquad (\beta \text{ near }\vec\beta_i)$$
The loss decreases the most when the dot product $\nabla_{\vec\beta} L \vert_{\vec\beta_i} \cdot (\vec\beta-\vec\beta_i)$ is as negative as possible. For fixed step length $\lVert \vec\beta-\vec\beta_i\rVert_2$, this occurs when $\vec\beta-\vec\beta_i$ points in the opposite direction as $\nabla_{\vec\beta} L \vert_{\vec\beta_i}$:$$\vec\beta_{i+1} - \vec\beta_i = -\alpha \nabla_{\vec\beta} L \vert_{\vec\beta_i} \quad\implies\quad \vec\beta_{i+1} = \vec\beta_i-\alpha \nabla_{\vec\beta} L \vert_{\vec\beta_i} $$ for an arbitrary step-size $\alpha$. The step-size is referred to as the **learning rate**.
#### Least-Squares Gradient Descent
Everything we stated above is valid for **any** loss function $L$. What about our sum-of-squares loss (can also be called an L2-loss, after the $L^2$-norm)? Here, we show that applying gradient descent repeatedly gets us closer to the standard solution derived above.$$\begin{align*}\nabla_{\vec\beta} L &= \nabla_{\vec\beta}\left[\lVert X\vec\beta - \vec y\rVert_2^2\right]\\&=\nabla_{\vec\beta}\left[\vec\beta^TX^TX\vec\beta - \vec y^TX\vec\beta-\vec\beta^TX^T\vec y + \vec y^T \vec y\right]\\&=2X^TX\vec\beta - 2X^T\vec y \\\implies \vec\beta_{i+1} - \vec\beta_i&=-\alpha\nabla_{\vec\beta} L\vert_{\vec\beta_i}=2\alpha X^T\vec y - 2\alpha X^TX\vec\beta_i\end{align*}$$From here, we can prove via induction that $$\vec\beta_k = \underbrace{(X^TX)^{-1}X^T\vec y}_{\vec\beta^*} +\underbrace{(1-\alpha)^k(\vec\beta_0 - (X^TX)^{-1}X^T\vec y)}_{\text{error at step }k}$$The proof is left as an exercise to the reader. A few things to notice here:
- The image shows that for this loss function, the gradient always points towards the optimal parameter vector. This is not true for more complicated models than linear regression. ^0c8da6
- When $\alpha = 0$, the sequence $\vec\beta_i$ makes no progress towards $\vec\beta^*$, instead staying at $\vec\beta_0$. 
- When $0 < \alpha < 1$, the sequence decays exponentially towards $\vec\beta^*$, getting there faster as $\alpha$ increases.
- When $\alpha = 1$, the sequence arrives at $\vec\beta^*$ in 1 step and stays there.
- When $1 < \alpha < 2$, the sequence oscillates around $\vec\beta^*$, but eventually converges on it.
- When $\alpha \geq 2$, the sequence diverges. The learning rate is too large to bring us towards $\vec\beta^*$.
- The pattern demonstrated above does generalize to more complicated models: gradient descent will oscillate or diverge if the learning rate is too large, and will move very slowly towards the optimal solution if the learning rate is too low.