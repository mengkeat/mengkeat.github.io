---
title: "Beautiful Mathematical Notation on the Web"
description: "Implementing LaTeX-style mathematical equations in web content using KaTeX and modern markdown processors."
pubDate: 2024-01-15
tags: ["mathematics", "web-development", "katex", "markdown"]
featured: true
author: "Chris Meng"
---

# Beautiful Mathematical Notation on the Web

Mathematical notation on the web has come a long way. With tools like KaTeX, we can now render beautiful LaTeX-style equations.

## Why KaTeX?

KaTeX is a fast, self-contained JavaScript library for rendering math notation. It's faster than MathJax and produces consistent, high-quality output across all browsers.

## Basic Examples

### Famous Equations

Einstein's mass-energy equivalence:

$$E = mc^2$$

Euler's identity, often called the most beautiful equation in mathematics:

$$e^{i\pi} + 1 = 0$$

The Pythagorean theorem:

$$a^2 + b^2 = c^2$$

### Calculus

The definition of a derivative:

$$f'(x) = \lim_{h \to 0} \frac{f(x+h) - f(x)}{h}$$

A definite integral:

$$\int_a^b f(x) \, dx$$

The fundamental theorem of calculus:

$$\int_a^b f'(x) \, dx = f(b) - f(a)$$

### Linear Algebra

Matrix multiplication:

$$\begin{bmatrix} a & b \\ c & d \end{bmatrix} \begin{bmatrix} x \\ y \end{bmatrix} = \begin{bmatrix} ax + by \\ cx + dy \end{bmatrix}$$

Eigenvalue equation:

$$A\mathbf{v} = \lambda\mathbf{v}$$

### Statistics

Normal distribution probability density function:

$$f(x) = \frac{1}{\sigma\sqrt{2\pi}} e^{-\frac{1}{2}\left(\frac{x-\mu}{\sigma}\right)^2}$$

Bayes' theorem:

$$P(A|B) = \frac{P(B|A)P(A)}{P(B)}$$

### Inline Math

You can also include math inline, like $x = \frac{-b \pm \sqrt{b^2 - 4ac}}{2a}$ for the quadratic formula, or $\sum_{i=1}^n i = \frac{n(n+1)}{2}$ for the sum of first n natural numbers.

## Advanced Features

KaTeX supports complex mathematical notation including:

### Complex Fractions

$$\frac{\frac{a}{b}}{\frac{c}{d}} = \frac{ad}{bc}$$

### Summations and Products

$$\sum_{k=0}^{n} \binom{n}{k} x^k y^{n-k} = (x+y)^n$$

$$\prod_{i=1}^{n} x_i = x_1 \cdot x_2 \cdot \ldots \cdot x_n$$

### Greek Letters and Symbols

$$\alpha, \beta, \gamma, \Delta, \Theta, \Lambda, \Sigma, \Omega$$

$$\forall x \in \mathbb{R}, \exists y \in \mathbb{N} : x < y$$

### Boxed Equations

Sometimes you want to highlight important equations with a box:

<div class="equation-box">

$$\boxed{E = mc^2}$$

</div>

You can also box entire derivations:

<div class="equation-box">

$$\begin{align}
x &= \frac{-b \pm \sqrt{b^2 - 4ac}}{2a} \\
&= \frac{-b}{2a} \pm \frac{\sqrt{b^2 - 4ac}}{2a}
\end{align}$$

</div>