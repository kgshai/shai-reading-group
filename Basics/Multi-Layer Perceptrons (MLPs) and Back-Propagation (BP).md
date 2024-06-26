Dependencies: [[Linear Regression with Gradient Descent]]

Learning Resources: 
- [Wikipedia article on Back-Propagation](https://en.wikipedia.org/wiki/Backpropagation) 
- [Towards Data Science explainer on Back-Propagation](https://towardsdatascience.com/understanding-backpropagation-abcc509ca9d0)
- [189 cheat sheet (see section on Neural Networks to learn about MLPs)](https://github.com/szhu/cs189-cheatsheet/blob/master/189-cheat-sheet-nominicards.pdf)

Historical Resources: 
- [Back-Propagation Paper (Rumelhart et al., 1986)](https://www.nature.com/articles/323533a0)
- [Report on the Multi-layer Perceptron (Rosenblatt, 1957)](https://blogs.umass.edu/brain-wars/files/2016/03/rosenblatt-1957.pdf)
# Summary
We've seen how gradient descent can be used to obtain solutions for linear regression problems. In this note, we will see how gradient descent generalizes to more power *nonlinear* models, unlike linear regression. Specifically, we will:
- Show how stacked linear transformations without nonlinearities reduce to a linear model
- Develop the concept of a **Multi-Layer Perceptron (MLP)**, which consists of stacked linear transformations with alternating element-wise nonlinearities
- Show an example of an element-wise nonlinearity, specifically the $\operatorname{ReLU}$ nonlinearity
- Demonstrate the expressive power of this nonlinearity by giving an argument as to why an 2-layer, infinite-width $\operatorname{ReLU}$ MLP can represent any continuous function
- Walk through the derivation of the Back-Propagation (BP) algorithm to calculate the gradient of the mean-squared error loss function ($L^2$) with respect to the parameters of a 2-layer MLP
- Generalize the BP algorithm for a 2-layer MLP to a deeper MLP
- Discuss how the BP algorithm for deep MLPs can be generalized to the class of differentiable models representable in modern automatic differentiation software
# Introduction
In the previous note, we saw how we arrive at the same solution as least squares linear regression by doing gradient descent. But this seems useless: least squares linear regression gives us the same result as gradient descent, with only one computation. In this note, we'll see how gradient descent, unlike the LS-solution, generalizes to more powerful *nonlinear* models.

We'll look at the canonical nonlinear model of modern ML: the **Multi-Layer Perceptron (MLP)**.
#### Can we make complex models by stacking Linear Regression?
First, let's think about stacking linear regression. Instead of learning a model $\vec f(\vec x)$ that represents the output $\vec y$ as a linear combination of elements of $\vec x$, what if we represented them as a linear combination of a linear combination of inputs?$$\begin{align*} \text{Linear Regression: }&\quad \vec y = \vec f(\vec x) = W\vec x, \qquad\vec x\underbrace{\longrightarrow}_{W} \vec y\\\text{Deeper Linear Regression: }&\quad \vec y = \vec f(\vec x) = W^{(2)}W^{(1)}\vec x \qquad \vec x \underbrace{\longrightarrow}_{W^{(1)}} \vec h \underbrace{\longrightarrow}_{W^{(2)}} \vec y\end{align*}$$This is an interesting idea, but it won't change anything, because if $\vec y = W^{(2)}W^{(1)}\vec x$, then $\vec y = W\vec x$ for $W = W^{(1)}W^{(2)}$. If we try to learn $W^{(1)}$ and $W^{(2)}$ via gradient descent, we will end up with the same least-squares solution, with the weight matrix $W = W^{(1)}W^{(2)}$. (After finishing this note, you can try proving this yourself!) Just stacking linear transformations does not increase the *expressive power* of our model.
#### Adding nonlinearities to create Multi-Layer Perceptrons
What if we add a nonlinearity instead? This is the core idea behind the **Multi-Layer Perceptron**. For a given element-wise **nonlinear** function $\sigma$, we can create the following model, originally called the **perceptron**, or now often called the **2-layer perceptron**: $$\text{(2-layer) Perceptron: }\quad \vec y = \vec f(\vec x) = W^{(2)}\sigma\left(W^{(1)}\vec x\right)\qquad \vec x \underbrace{\longrightarrow}_{W^{(1)}} \vec a \underbrace{\longrightarrow}_{\sigma} \vec h \underbrace{\longrightarrow}_{W^{(2)}} \vec y$$To clarify, $\sigma$ can be thought of as a nonlinear function $\sigma: \mathbb{R}\to\mathbb{R}$, or a standard function mapping from real numbers to real numbers like we know and love from high school (secondary school) math. When we apply $\sigma$ to $\vec a$, we apply it independently to each dimension, so$$\sigma(\vec a) = \begin{pmatrix}\sigma(a_1) \\ \sigma(a_2)\\\vdots\\\sigma(a_n)\end{pmatrix} = \begin{pmatrix}h_1 \\ h_2\\\vdots\\h_n\end{pmatrix} = \vec h$$$\sigma$ is called the **activation function**, $\vec a$ is commonly called the **pre-activation**, and $\vec h$ is commonly referred to as the **activation**. The intermediaries $\vec a$ and $\vec h$, when put together, are generally called a **hidden layer**, since it's entirely internal to the model: only $\vec y$ and $\vec x$ will appear in the [[Linear Regression with Gradient Descent#^54bd3d|loss function]] that we optimize during gradient descent. Lastly, to make the perceptron work really well, we can add **biases**, or constant vectors that are considered learned parameters like the weight matrices:$$\text{Perceptron with bias: }\quad \vec y = \vec f(\vec x) = W^{(2)}\sigma\left(W^{(1)}\vec x + \vec b^{(1)}\right) + \vec b^{(2)}\qquad \vec x \underbrace{\longrightarrow}_{W^{(1)}, \vec b^{(1)}} \vec a \underbrace{\longrightarrow}_{\sigma} \vec h \underbrace{\longrightarrow}_{W^{(2)}, \vec b^{(2)}} \vec y$$
#### Analyzing Expressive Power with an Example
One question you might ask immediately: does adding an nonlinearity really increase expressive power that much? To think about this, consider the following nonlinearity:$$\operatorname{ReLU}(x) = \begin{cases} x & \text{if } x > 0\\0 & \text{otherwise}\end{cases}$$Imagine we are trying to represent a 1d-to-1d function $f^*: \mathbb{R}\to \mathbb{R}$. Here's an example function that is nonlinear: $f^*(x)=x^3 - 9x$

Let's consider a perceptron where $\vec x = x \in\mathbb{R}$, $\vec y = y\in\mathbb{R}$, and $\vec a, \vec h\in\mathbb{R}^N$. For starters, let's set $N = 1$, so our hidden layer has dimension 1. This will end up looking like a shifted and scaled version of the $\operatorname{ReLU}$ function shown above: it'll be a piecewise linear function with 1 elbow, or two piecewise linear segments. (Vertical shifting is controlled by $b^{(2)}$ and horizontal shifting by $b^{(1)}$; vertical scaling by $W^{(2)}$ and horizontal scaling by $W^{(1)}$). An example is plotted in the image below, with the $\operatorname{ReLU}$ MLP shown in blue and an example polynomial shown in orange.

![](Images/MLPBP/1_elbow.png)
If we set $N = 2$, we can think of the result as the sum of two shifted/scaled $\operatorname{ReLU}$ functions, so we can represent any piecewise linear function with 2 elbows (three piecewise linear segments). An example is plotted in the image below, with the $\operatorname{ReLU}$ MLP shown in blue and an example polynomial shown in orange.
![](Images/MLPBP/2_elbow.png)
As $N\to\infty$, the number of elbows in our piecewise linear function increases to $\infty$, and we can represent piecewise linear functions with more and more segments. Any continuous function can be approximated as a piecewise linear function as the number of segments increases to $\infty$, so we find that as our hidden layer gets larger, a perceptron can represent *any continuous function*! This is a simple variety of a class of theorems called **Universal Approximation Theorems**, which state conditions under which a neural network can represent all functions from a certain class. In this case, we found that infinite-width 1-layer perceptrons can represent all continuous functions. Studying neural networks in the limit as all layer widths tend to $\infty$ is a huge topic in neural network theory.



```python
import numpy as np
from matplotlib import pyplot as plt
from matplotlib.widgets import Button, Slider
X = np.linspace(-4, 4, 1000)
Y = X * X * X - 9 * X
plt.plot(X, Y)
plt.show()


# The parametrized function to be plotted
def f(X, w1, w2, b1, b2):
    return w2 * np.maximum(w1 * X + b1, np.zeros_like(X)) + b2

# Define initial parameters
init_w1 = 5
init_w2 = 3
init_b1 = -3
init_b2 = 3
init_lr = -6

# Create the figure and the line that we will manipulate
fig, ax = plt.subplots()
line, = ax.plot(X, f(X, init_w1, init_w2, init_b1, init_b2), lw=2)
ax.plot(X, Y, lw=2)
ax.set_ylim(-40, 40)

# adjust the main plot to make room for the sliders
fig.subplots_adjust(left=0.25, bottom=0.5)

# Make a horizontal slider to control the frequency.
axw1 = fig.add_axes([0.25, 0.35, 0.65, 0.03])
w1_slider = Slider(
    ax=axw1,
    label='W1',
    valmin=-10,
    valmax=10,
    valinit=init_w1,
)

axb1 = fig.add_axes([0.25, 0.3, 0.65, 0.03])
b1_slider = Slider(
    ax=axb1,
    label='b1',
    valmin=-10,
    valmax=10,
    valinit=init_b1,
)

# Make a vertically oriented slider to control the amplitude
axw2 = fig.add_axes([0.25, 0.25, 0.65, 0.03])
w2_slider = Slider(
    ax=axw2,
    label="W2",
    valmin=-10,
    valmax=10,
    valinit=init_w2
)

axb2 = fig.add_axes([0.25, 0.2, 0.65, 0.03])
b2_slider = Slider(
    ax=axb2,
    label='b2',
    valmin=-10,
    valmax=10,
    valinit=init_b2,
)

axlr = fig.add_axes([0.25, 0.1, 0.65, 0.03])
lr_slider = Slider(
    ax = axlr,
    label="log(learning rate)",
    valmin=-10,
    valmax=0,
    valinit=init_lr
)


# The function to be called anytime a slider's value changes
def update(val):
    line.set_ydata(f(X, w1_slider.val, w2_slider.val, b1_slider.val, b2_slider.val))
    fig.canvas.draw_idle()


# register the update function with each slider
w1_slider.on_changed(update)
w2_slider.on_changed(update)
b1_slider.on_changed(update)
b2_slider.on_changed(update)

# Create a `matplotlib.widgets.Button` to reset the sliders to initial values.
resetax = fig.add_axes([0.8, 0.025, 0.1, 0.04])
button = Button(resetax, 'Reset', hovercolor='0.975')
learnax = fig.add_axes([0.6, 0.025, 0.1, 0.04])
learnbutton = Button(learnax, 'GD Step', hovercolor='0.975')


def reset(event):
    w1_slider.reset()
    w2_slider.reset()
    b1_slider.reset()
    b2_slider.reset()
button.on_clicked(reset)

def learn(event):
    w1 = w1_slider.val
    w2 = w2_slider.val
    b1 = b1_slider.val
    b2 = b2_slider.val
    lr = lr_slider.val
    h = np.maximum(w1 * X + b1, np.zeros_like(X))
    dw2 = 2 * np.dot(w2 * h + b2 - Y, h)
    db2 = 2 * np.dot(w2 * h + b2 - Y, np.ones_like(h))
    dw1 = 2 * np.dot(w2 * h + b2 - Y, w2 * np.where(w1 * X + b1 < 0, np.zeros_like(X), X))
    db1 = 2 * np.dot(w2 * h + b2 - Y, w2 * np.where(w1 * X + b1 < 0, np.zeros_like(X), np.ones_like(X)))
    w1_slider.set_val(w1 - (10 ** lr) * dw1)
    w2_slider.set_val(w2 - (10 ** lr) * dw2)
    b1_slider.set_val(b1 - (10 ** lr) * db1)
    b2_slider.set_val(b2 - (10 ** lr) * db2)
    line.set_ydata(f(X, w1_slider.val, w2_slider.val, b1_slider.val, b2_slider.val))
    fig.canvas.draw_idle()
learnbutton.on_clicked(learn)

plt.show()
```
#### Gradient Descent for Perceptrons
Let's see how gradient descent works to adjust the weights of a 1-layer perceptron. We'll suppose we have $\vec x\in\mathbb{R}^I$, $\vec y\in\mathbb{R}^O$, and $\vec a, \vec h\in\mathbb{R}^N$, so our input has dimension $I$, our output has dimension $O$, and our hidden layer has dimension $N$. We suppose are given the **loss function** $L(\hat y, \vec y) = \Big\lVert\vec f_\theta(\vec x) - \vec y\Big\rVert_2^2$, where $\hat y = \vec f_\theta(\vec x)$ is the predicted value of $\vec y$. We've gathered the weight matrices into **parameters** $\theta = (W^{(1)}, W^{(2)}, \vec b^{(1)}, \vec b^{(2)})$ of the model; we often think of this as a vector in a **parameter space**, and with this intuition, [[Linear Regression with Gradient Descent#^0c8da6|gradient descent finds the direction in parameter space that decreases the loss the most]] (at least, based on what the loss surface looks like around the current parameters). Now, we derive the gradients for the 1-layer perceptron parameters. First, we note the following relations describing the perceptron:
$$\begin{align*}L &= \sum_i (\hat y_i - y_i)^2\\\hat y_i &= \sum_j W^{(2)}_{ij}h_j +  b^{(2)}_i\\h_i &= \sigma(a_i)\\ a_i &= \sum_j W^{(1)}_{ij}x_j + b^{(1)}_j\end{align*}$$
We can use the chain rule to derive parameter gradients based on these relations. We'll first demonstrate what this looks like for $W^{(2)}$ in order to develop notation, before moving onto $W^{(1)}$. Consider the gradient with respect to $W^{(2)}$:$$\begin{align*}\frac{\partial L}{\partial W^{(2)}_{jk}} &= \sum_{i}\frac{\partial L}{\partial \hat y_i}\frac{\partial \hat y_i}{\partial W^{(2)}_{jk}}\\&=2\sum_i (\hat y_i - y_i)\frac{\partial \hat y_i}{\partial W^{(2)}_{jk}} \end{align*}$$The term $\frac{\partial \hat y_i}{\partial W^{(2)}_{jk}}$ is just $h_k$ when $i = j$, and is zero otherwise (check this using the relations above). This fact can be expressed in mathematical notation using the Kronecker Delta symbol, $\delta_{ij}$: $$\delta_{ij} = \begin{cases} 1 & i = j\\0 & i\neq j\end{cases}$$Using this notation, we can write $$\begin{align*}\frac{\partial L}{\partial W^{(2)}_{jk}} &= 2\sum_{i}(\hat y_i - y_i)\frac{\partial \hat y_i}{\partial W^{(2)}_{jk}}\\&=2\sum_i (\hat y_i - y_i)\delta_{ij}h_k\\&=2h_k\sum_i (\hat y_i - y_i)\delta_{ij} \end{align*}$$Now observe that due to the Kronecker Delta, all terms of the sum drop out except for the one for which $i = j$. Generally, *we can evaluate an expression involving a sum over an index $i$ and a Kronecker delta with indices $ij$ by simply replacing $i$ with $j$ everywhere in the term*. Using this fact,$$\begin{align*}\frac{\partial L}{\partial W^{(2)}_{jk}} &=2h_k\sum_i (\hat y_i - y_i)\delta_{ij}\\&=2 (\hat y_j - y_j) h_k \end{align*}$$Now that we've seen how we can derive the gradients with respect to $W^{(2)}$ in index notation, we'll derive the gradients with respect to all other parameters using this notation:$$\begin{align*}\frac{\partial L}{\partial b^{(2)}_j}&=\sum_{i}\frac{\partial L}{\partial \hat y_i}\frac{\partial \hat y_i}{\partial b^{(2)}_{j}}\\&=\sum_{i}2(\hat y_i - y_i)\delta_{ij}\\&=2(\hat y_j - y_j)\\\frac{\partial L}{\partial W^{(1)}_{jk}}&=\sum_{i}\frac{\partial L}{\partial \hat y_i}\frac{\partial \hat y_i}{\partial W^{(1)}_{jk}}\\&= \sum_{i, \ell}\frac{\partial L}{\partial \hat y_i}\frac{\partial \hat y_i}{\partial h_\ell}\frac{\partial h_\ell}{\partial W^{(1)}_{jk}}\\&=\sum_{i, \ell}\frac{\partial L}{\partial \hat y_i}\frac{\partial \hat y_i}{\partial h_\ell}\frac{\partial h_\ell}{\partial a_\ell}\frac{\partial a_\ell}{\partial W^{(1)}_{jk}}\\&=\sum_{i, \ell}\left(2(\hat y_i - y_i)\right)\left(W^{(2)}_{i\ell}\right)\left(\frac{\partial \sigma}{\partial x} \bigg\vert_{x = a_\ell}\right)\left(\delta_{\ell j} x_k\right)\\&=\sum_{i}\left(2(\hat y_i - y_i)\right)\left(W^{(2)}_{ij}\right)\left(\frac{\partial \sigma}{\partial x} \bigg\vert_{x = a_j}\right) x_k\\&=\left(\sum_{i}2(\hat y_i - y_i)W^{(2)}_{ij}\right)\left(\frac{\partial \sigma}{\partial x} \bigg\vert_{x = a_j}\right) x_k\\\frac{\partial L}{\partial b^{(1)}_{j}}&=\sum_{i}\frac{\partial L}{\partial \hat y_i}\frac{\partial \hat y_i}{\partial b^{(1)}_{j}}\\&= \sum_{i, \ell}\frac{\partial L}{\partial \hat y_i}\frac{\partial \hat y_i}{\partial h_\ell}\frac{\partial h_\ell}{\partial b^{(1)}_{j}}\\&=\sum_{i, \ell}\frac{\partial L}{\partial \hat y_i}\frac{\partial \hat y_i}{\partial h_\ell}\frac{\partial h_\ell}{\partial a_\ell}\frac{\partial a_\ell}{\partial b^{(1)}_{j}}\\&=\sum_{i, \ell}\left(2(\hat y_i - y_i)\right)\left(W^{(2)}_{i\ell}\right)\left(\frac{\partial \sigma}{\partial x} \bigg\vert_{x = a_\ell}\right)\left(\delta_{\ell j} \right)\\&=\sum_{i}\left(2(\hat y_i - y_i)\right)\left(W^{(2)}_{ij}\right)\left(\frac{\partial \sigma}{\partial x} \bigg\vert_{x = a_j}\right) \\&=\left(\sum_{i}2(\hat y_i - y_i)W^{(2)}_{ij}\right)\left(\frac{\partial \sigma}{\partial x} \bigg\vert_{x = a_j}\right) \end{align*}$$Note that this expression involves intermediates $h_k$ and $\hat y_j$ which are calculated inside the MLP, rather than being parameters themselves. A key step in the Back-Propagation algorithm is to save these intermediates when calculating MLP outputs (this is known as the forward pass) so they can be reused when we calculate gradients (this is known as the backward pass).

#### Generalizing to Deep MLPs

#### Generalizing to Deep Differentiable Models, A.K.A. Neural Networks

# Analysis
#### Gradient Descent on Stacked Linear Regression
In this section, we derive 