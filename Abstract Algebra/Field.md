## Introduction
A **field** is a formal way to refer to a set of numbers. The definition contains the well-known properties of numbers: you can add them, multiply them, there's a number 0 such that $x + 0 = x$, etc. Formally, a field is defined by **axioms** that encode these well-known properties. The real numbers $\mathbb R$, the complex numbers $\mathbb C$, and the rational numbers $\mathbb Q$ all satisfy these axioms, and thus are examples of fields.
## Definition
A field $\mathbb F = (F, +, \cdot)$ consists of three objects: a set $F$ of numbers, an operation $+: F\times F \to F$ representing the addition of two numbers, and an operation $\cdot : F\times F \to F$ representing the multiplication of two numbers. Note that we normally represent multiplication using concatenation: $ab = a\cdot b$.

Additionally, the operations must satisfy the **field axioms**. The operation $+$ must satisfy the **additive axioms**:
- Commutativity: $a + b = b + a$ for all $a, b \in F$
- Associativity: $(a + b) + c = a + (b + c)$ for all $a, b, c\in F$
- Identity: there is $0\in F$ such that, for all $a\in F$, $a + 0 = a$ ^d085a3
- Inverse: for each $a\in F$, there is $-a\in F$ such that $a + (-a) = 0$

The operation $\cdot$ must satisfy the **multiplicative axioms**:
- Commutativity: $ab = ba$ for all $a, b\in F$
- Associativity: $(ab)c = a(bc)$ for all $a, b, c\in F$
- Identity: there is $1 \in F$ such that, for all $a\in F$, $1a = a$ ^acc19d
- Inverse: for each $a\in F$ such that $a\neq 0$, there is $a^{-1}\in F$ such that $aa^{-1} = 1$

The two operations must together satisfy the **distributive axiom**:
- Distributivity: $a(b + c) = ab + ac$ for all $a, b, c\in F$
#### Derived Properties
There are many other properties of numbers that are well-known but not listed here, because they can be derived from those listed here. For example, consider the property $(a + b)c = ac + bc$. We can derive it as follows:$$\begin{align*}(a + b)c &= c(a + b) \quad \text{(Additive Commutativity)}\\&=ca + cb \quad \text{(Distributivity)}\\&=ac + bc \quad\text{(Multiplicative Commutativity)}\end{align*}$$Additionally, consider the property that $a \cdot 0 = 0$. This isn't listed as an axiom, but it can be proved from the other ones. For brevity, we write $b = a\cdot 0$ and prove $b = 0$.$$\begin{align*} b = a\cdot 0 \quad &\text{(Definition of }b\text{)}\\ \Rightarrow\quad b = a(0 + 0)\quad &\text{(Additive Identity)}\\\Rightarrow \quad b = a \cdot 0 + a\cdot 0 \quad &\text{(Distributivity)}\\ \Rightarrow \quad b= b + b\quad & \text{(Definition of }b\text{)}\\\Rightarrow \quad b + (-b) = (b + b) + (-b)\quad & \text{(Additive Inverse)}\\\Rightarrow \quad b + (-b) = b + (b + (-b))\quad & \text{(Additive Associativity)}\\\Rightarrow \quad 0 = b + 0 \quad &\text{(Additive Inverse)}\\\Rightarrow\quad 0 = b\quad &\text{(Additive Identity)}\end{align*}$$Notice how long and unintuitive the proof is for such an obvious-seeming fact! This is reflective of the minimality of the axioms presented above. In practice, when working with fields (e.g. in the context of vector spaces), one does not need to always derive things straight from axioms.