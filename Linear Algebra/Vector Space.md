Dependencies: [[Field]]
## Introduction
A vector space is a set of objects called **vectors**, which can be added to each other, as well as scaled up/down by numbers, in this case called **scalars**. We denote vectors using a hat: $\vec x$. We denote scalars using the notation for variables: $c$. 

Some simple examples include $\mathbb R^2$, which is the set of pairs of numbers in $\mathbb R$ with addition and scalar multiplication defined as follows: $$\begin{align*}(x_1, y_1) + (x_2, y_2) = (x_1 + x_2, y_1 + y_2)\quad&\text{for all}\quad x_1, x_2, y_1, y_2 \in \mathbb R\\c(x, y) = (cx, cy)\quad &\text{for all}\quad c, x, y\in\mathbb R\end{align*}$$Another example: the functions $f:\mathbb R\to\mathbb R$ mapping real numbers to real numbers, where vector addition simply adds the output of functions for each input, and scalar multiplication by $c\in\mathbb R$ simply scales the output of a function on each input.

Note that the vectors in the above examples are very different, but have some similar properties. For example, in both cases, $c (\vec x + \vec y) = c\vec x + c\vec y$ for scalars $c$ and vectors $\vec x, \vec y$. The properties we need to derive useful results about vectors and vector spaces are called the **vector space axioms**, and together they comprise the formal definition of vector spaces.
## Definition
A vector space $\mathcal V = (V, \mathbb F, +, \cdot)$ consists of four objects: a set $V$ of vectors, a [[Field|field]] $\mathbb F$ of scalars, and operations $+ : V\times V \to V$ and $\cdot: \mathbb F\times V \to V$ representing vector addition and scalar multiplication, respectively. (We typically exclude the $\cdot$ symbol for scalar multiplication, like so: $c\vec x = c\cdot\vec x$.) 

Crucially, the operations must satisfy the **vector space axioms**. The operation $+$ must satisfy the **additive axioms**:
- Commutativity: $\vec x + \vec y = \vec y + \vec x$ for all $\vec x, \vec y \in V$
- Associativity: $(\vec x + \vec y) + \vec z = \vec x + (\vec y + \vec z)$ for all $\vec x, \vec y, \vec z\in V$
- Identity: there is $\vec 0\in V$ such that, for all $x\in V$, $x +\vec 0 = x$
- Inverse: for all $\vec x\in V$, there is $-\vec x \in V$ such that $\vec x + (-\vec x) = 0$

Additionally, the scalar multiplication operation $\cdot$ must satisfy the **multiplicative axioms**. (Note that these axioms reference the [[Field#^d085a3|field additive identity]] $0$ and [[Field#^acc19d|field multiplicative identity]] $1$, the former of which should not be confused with the vector additive identity $\vec 0$.)
- Additive Identity: the additive identity $0\in\mathbb F$ must satisfy $0\vec x = \vec 0$ for all $\vec x \in V$
- Multiplicative Identity: the multiplicative identity $1\in\mathbb F$ must satisfy $1\vec x = \vec x$ for all $\vec x \in V$
- Associativity: $(cd) \vec x = c(d\vec x)$ for all $c, d\in\mathbb F$ and $\vec x \in V$

Finally, the two operations must satisfy the **distributive axioms**:
- Additive Distribution: $c(\vec x + \vec y) = c\vec x + c\vec y$ for all $c\in\mathbb F$ and $\vec x, \vec y \in V$
- Multiplicative Distribution: $(c + d)\vec x = c\vec x + d\vec x$ for all $c, d \in\mathbb F$ and $\vec x\in V$

When all these axioms are satisfied, we have a vector space. We write $\vec x \in\mathcal V$ to mean that $\vec x \in V$ and $V$ is the set component of a vector space. We often write $\mathcal V = (V, \mathbb F)$ to specify a field for the vector space when the vector addition and scalar multiplication operations are obvious or implied.

## Examples
We provide some elementary examples of vector spaces:
- $\mathbb R^n = \{(x_1, x_2, \dots, x_n)\mid x_1, \dots, x_n \in \mathbb R\}$ consists of length-$n$ lists of real numbers. Addition and scalar multiplication are defined as follows: $$\begin{align*}(x_1, x_2, \dots, x_n) + (y_1, y_2, \dots, y_n) &= (x_1 + y_1, x_2 + y_2, \dots, x_n + y_n)\\c(x_1, x_2, \dots, x_n) &= (cx_1, cx_2, \dots, cx_n)\end{align*}$$where the addition and multiplication on the right hand side (e.g. $x_1 + y_1$, $cx_1$) refer to addition and multiplication of real numbers. An element $(x_1, x_2, \dots, x_n)\in\mathbb R^n$ can be visualized as an arrow in $n$-dimensional space starting at the origin at ending at the coordinates $(x_1, x_2, \dots, x_n)$. Vector addition can be visualized as chaining arrows end-to-end, and multiplication can be visualized as scaling the length of the arrow without changing the direction.
- $\mathbb C^n = \{(x_1, x_2, \dots, x_n)\mid x_1, \dots, x_n \in \mathbb C\}$ consists of length-$n$ lists of complex numbers. Addition and scalar multiplication are defined as in $\mathbb R^n$, except we use addition and multiplication of complex numbers (rather than reals).
- For any field $\mathbb F$, we can construct a vector space $\mathbb F^n$, where addition and scalar multiplication are defined as in $\mathbb R^n$ and $\mathbb C^n$. We will later see that many interesting vector spaces (precisely, finite-dimensional vector spaces) can be represented using $\mathbb F^n$ (precisely, they are isomorphic).
- $F = \{f: \mathbb R \to\mathbb R\}$, the set of functions from real numbers to real numbers, is a vector space. Addition and scalar multiplication are defined naturally:$(f_1 + f_2)(x) = f_1(x) + f_2(x)$, and $(cf)(x) = c\cdot f(x)$. They can be visualized as graphs in the 2D plane, with addition and scalar multiplication visualized as usual.