
## Introduction
This is a simple introduction for real vectors in finite-dimensional spaces. See the note on Vector Spaces for a more complete introduction.

A vector is a mathematical object that can be thought of as an arrow starting at the origin. Two vectors $\vec x$ and $\vec y$ can be added to produce a vector $\vec x + \vec y$, which can be visualized as moving the "start point" of the vector $\vec y$ to the tip of vector $\vec x$, and constructing a new vector $\vec x + \vec y$ that points to the new location of the tip of vector $\vec y$: ![vector addition](vec_add.svg)
A vector $\vec x$ can also be multiplied by a number $c$ to produce a vector $c \vec x$, a scaled version of the original vector:
![scalar multiplication](Images/Vector/vec_mult.png)

## Definition
A (real, finite-dimensional) vector is a list $(x_1, x_2, \dots, x_n)$, where $x_1, \dots, x_n\in\mathbb R$. Vectors can be added to each other:$$(x_1, \dots, x_n) + (y_1, \dots, y_n) = (x_1 + y_1, \dots, x_n + y_n)$$and multiplied by real numbers:$$c(x_1, \dots, x_n) = (cx_1, \dots, cx_n)$$