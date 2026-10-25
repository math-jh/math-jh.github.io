---
title: "Connection"
description: "We define a connection on a vector bundle to introduce covariant differentiation, and discuss the key properties of covariant differentiation that depend on the Leibniz rule and local properties of vector fields."
excerpt: "Differentiation on a vector bundle"

categories: [Math / Riemannian Geometry]
permalink: /en/math/riemannian_geometry/connection
sidebar: 
    nav: "riemannian_geometry-en"

date: 2022-12-16
weight: 2
translated_at: 2026-06-01T21:30:01+00:00
translation_source: kimi-cli
last_polished_at: 2026-10-25T15:15:06+00:00
translation_polish_source: antigravity-gemini-3.8-flash-high
---
## Connections and Covariant Differentiation

Using the Lie derivative, we can differentiate vector fields or differential forms, but for an arbitrary vector bundle $\pi:E\rightarrow M$, it is impossible to extend this concept to sections $\Gamma(E)$. This is because on the tangent bundle $TM$, given an integral flow $\phi$ and two points $p,q$ on it, there was, connecting the two tangent spaces $T_pM$ and $T_qM$, a natural isomorphism $\dd{\phi}^{-t}$; however, for an arbitrary vector bundle $E$, no such map exists between two fibers $E_p$ and $E_q$. Therefore, we additionally define a *connection* that *connects* these fibers.

::: Definition 1
For a manifold $M$ and a vector bundle $E\rightarrow M$ defined over it, a *connection* on $E$, $\nabla:\mathfrak{X}(M)\times\Gamma(E)\rightarrow\Gamma(E)$, is a map satisfying the following conditions.

1. (Tensoriality) $\nabla_XY$ is $C^\infty$-linear in the first argument.
2. (Linearity) $\nabla_XY$ is $\mathbb{R}$-linear in the second argument.
3. For any $f\in C^\infty(M)$, $\nabla$ satisfies the following Leibniz rule:
    
    $$\nabla_X(fY)=f\nabla_XY+(Xf)Y$$
:::

Here, $\nabla_XY$ is also called the *covariant derivative* of $Y$ in the direction of $X$. The following proposition shows that to compute $(\nabla_XY)_p$, it suffices to know, in a neighborhood of $p$, only $X$ and $Y$.

::: Proposition 2
Suppose that over a manifold $M$, a vector bundle $E\rightarrow M$ and a connection $\nabla$ on it are given, and let $X\in\mathfrak{X}(M)$, $Y\in\Gamma(E)$. For any point $p\in M$, $(\nabla_XY)_p$ depends only on

1. the value at the point $p$ of the vector field $X$, $X_p$,
2. the section on an open neighborhood of the point $p$, $Y\vert_U$.
:::
::: Proof
First, let us show that $(\nabla_XY)_p$ depends only on the section on an open neighborhood of the point $p$, $U$. Since we must show that if two sections $Y_1,Y_2$ agree on an open neighborhood of $p$, $U$, then $(\nabla_XY_1)_p=(\nabla_XY_2)_p$, for this it suffices to show that if a section $Y$ is, at all points of the open neighborhood $U$, identically $0$, then $(\nabla_XY)_p$ is $0$. If $\varphi$ is a bump function satisfying $\supp(\varphi)\subseteq U$ and $\varphi(p)=1$, the section $\varphi Y$ is, on all of $M$, identically $0$. Therefore, by the second condition of [Definition 1](#def1){: data-lid="uc3yh" }, $\nabla_X(\varphi Y)=0$. On the other hand, by the Leibniz rule,

$$0=\nabla_X(\varphi Y)=\varphi\nabla_XY+(X\varphi)Y$$

and evaluating the right-hand side at the point $p$ yields

$$\varphi(p)(\nabla_XY)_p+(X\varphi)(p)Y_p=(\nabla_XY)_p$$

so $(\nabla_XY)_p=0$.

Now we show that $\nabla_XY$ depends only on the vector at the point $p$, $X_p$. For this, just as above, it suffices to assume $X_p=0$ and show that $0=(\nabla_XY)_p$. Around the point $p$, take a coordinate chart $(U,(x^i))$, and write $X$ with respect to this coordinate system as

$$X=X^1\frac{\partial}{\partial x^1}+\cdots+X^n\frac{\partial}{\partial x^n}$$

Then

$$(\nabla_XY)_p=(\nabla_{\sum X^i\frac{\partial}{\partial x^i}}Y)_p=\left(\sum_{i=1}^n X^i\nabla_{\partial/\partial x^i} Y\right)_p$$

and since for all $i$, $X^i(p)=0$, we obtain the desired result.
:::

## Covariant Differentiation on the Tangent Bundle

In particular, let us examine a connection defined on the tangent bundle $TM\rightarrow M$. Then $\nabla$ is a map from $\mathfrak{X}(M)\times\mathfrak{X}(M)$ to $\mathfrak{X}(M)$. It should be noted that although the Lie derivative and a connection are both concepts meant for differentiation, they yield different results. For instance, in the Lie derivative,

$$\mathcal{L}_{fX}Y=[fX,Y]=fX(Y)-Y(fX)=fX(Y)-(Yf)X-fY(X)=f[X,Y]-(Yf)X=f\mathcal{L}_XY-(Yf)X$$

whereas, by definition,

$$\nabla_{fX}Y=f\nabla_XY$$

so it is always possible to choose $Y$ and $f$ appropriately such that $\nabla_{fX}Y\neq\mathcal{L}_{fX}Y$.

In any case, considering a connection defined on $TM$, by [Proposition 2](#prop2){: data-lid="hcd2y" }, the value at the point $p$ of $\nabla_XY$ is completely determined in a neighborhood of $p$ by the local frames $(E_i)$. This is because

$$(\nabla_XY)_p=\left(\nabla_{\sum X^iE_i}\left(\sum Y^jE_j\right)\right)_p$$

holds. On the other hand,

$$\nabla_X\left(\sum_{j=1}^n Y^jE_j\right)=\sum_{j=1}^n \nabla_X(Y^jE_j)=\sum_{j=1}^n\left(Y^j\nabla_XE_j+X(Y^j)E_j\right)=\sum_{i,j=1}^nX^iY^j\nabla_{E_i}E_j+\sum_{j=1}^n X(Y^j)E_j\tag{1}$$

so $\nabla_XY$ is completely determined by the $n^2$ vector fields $\nabla_{E_i}E_j$. Expressing the vector fields $\nabla_{E_i}E_j$ again as linear combinations of the $E_k$,

$$\nabla_{E_i}E_j=\sum_{k=1}^n\Gamma_{ij}^k E_k$$

there exist $n^3$ $C^\infty$-functions $\Gamma_{ij}^k$ satisfying this. Then equation (1) above can be written as

$$\nabla_XY=\sum_{k=1}^n\left(X(Y^k)+\sum_{i,j=1}^nX^iY^j\Gamma_{ij}^k\right)E_k$$

::: Definition 3
The $n^3$ functions $\Gamma_{ij}^k$ defined above are called the *connection coefficients*.
:::

On the other hand, the tangent bundle over any manifold $M$ always admits a connection. To verify this, just as with a Riemannian metric, one can take the connection on Euclidean space

$$\nabla_vY:=v(Y^1)\frac{\partial}{\partial x^1}+\cdots+v(Y^n)\frac{\partial}{\partial x^n}$$

and patch it together via a partition of unity.

## Covariant Differentiation on the Cotangent Bundle

We show that a connection $\nabla$ defined on the tangent bundle $TM$ extends nicely to any $(r,s)$-tensor field $\mathcal{T}^{r,s}(M)$. ([Proposition 5](#prop5){: data-lid="i5g02" }) To do this, we must first specify how $\nabla$ extends to the cotangent bundle $T^\ast M$.

::: Proposition 4
Let $M$ be a manifold and let $\nabla$ be a connection on the tangent bundle $TM$. If we define the map $\nabla^\ast:\mathfrak{X}(M)\times\Gamma(T^\ast M)\rightarrow\Gamma(T^\ast M)$ by the formula

$$(\nabla_X^\ast\alpha)_p(Y)=X\bigl(\alpha(Y)\bigr)-\alpha_p\bigl((\nabla_XY)_p\bigr)$$

then $\nabla^\ast$ is a connection on $T^\ast M$.
:::
::: Proof
First, one can show that $\nabla^\ast\alpha$ defined by the expression on the right-hand side is a $1$-form, so the codomain of $\nabla^\ast$ is unproblematic.

That $\nabla^\ast$ actually satisfies the conditions for a connection is obvious except for the Leibniz rule. In fact, the Leibniz rule is also clear from

$$\begin{aligned}(\nabla_X^\ast(f\alpha))_pY&=X(f\cdot\alpha(Y))-(f\alpha)_p\bigl((\nabla_XY)_p\bigr)\\&=(Xf)(\alpha(Y))+f(p)\bigl(X(\alpha(Y))-\alpha_p\bigl((\nabla_XY)_p\bigr)\bigr)\\&=\bigl((Xf)\alpha+f\nabla_X^\ast\alpha\bigr)Y\end{aligned}$$
:::

By a slight abuse of notation, we also write the $\nabla^\ast$ defined above as $\nabla$.

## Covariant Differentiation on Tensor Fields

Now we can finally extend the connection on $TM$ to $(r,s)$-tensor fields $\mathcal{T}^{r,s}(M)$. As above, we also write the connection defined in this way as $\nabla$.

::: Proposition 5
On the tangent bundle $TM\rightarrow M$, suppose a connection $\nabla$ is given. Then $\nabla$ can be extended to all tensor fields $\mathcal{T}^{r,s}(M)$ satisfying the following two conditions

$$\nabla_X(F\otimes G)=(\nabla_X F)\otimes G+F\otimes(\nabla_XG),\qquad\nabla_X(F+G)=\nabla_XF+\nabla_XG$$

and furthermore, such an extension is uniquely determined by requiring in addition that on $\mathcal{T}^{0,0}M$, $\nabla_Xf=Xf$, and on $T^\ast M$, it coincides with $\nabla^\ast$ of [Proposition 4](#prop4){: data-lid="83ove" }.
:::

Since an arbitrary $(r,s)$-tensor $F$ can be identified with the following $C^\infty(M)$-multilinear map

$$\underbrace{\Omega^1(M)\times\cdots\times \Omega^1(M)}_\text{\small $r$ times}\times\underbrace{\mathfrak{X}(M)\times\cdots\times \mathfrak{X}(M)}_\text{\small $s$ times}\rightarrow C^\infty(M)$$

$\nabla_XF$ is uniquely determined by its values on $\omega^1,\ldots,\omega^r\in\Omega^1(M)$, $Y_1,\ldots, Y_s\in\mathfrak{X}(M)$. For instance, applying the Leibniz rule to a simple tensor $F=X_1\otimes\cdots\otimes X_r\otimes\alpha^1\otimes\cdots\otimes\alpha^s\in\mathcal{T}^{r,s}(M)$ yields

$$\begin{aligned}\nabla_X(X_1\otimes\cdots\otimes X_r\otimes\alpha^1\otimes\cdots\otimes\alpha^s)&=(\nabla_XX_1)\otimes X_2\otimes\cdots\otimes X_r\otimes\alpha^1\otimes\cdots\alpha^s\\
&\phantom{=aa}+\cdots\\
&\phantom{=aaaa}+X_1\otimes X_2\otimes\cdots\otimes(\nabla_XX_r)\otimes\alpha^1\otimes\cdots\otimes\alpha^s\\
&\phantom{=aaaaaa}+X_1\otimes\cdots X_r\otimes(\nabla_X\alpha^1)\otimes\alpha^2\otimes\cdots\otimes\alpha^s\\
&\phantom{=aaaaaaaa}+\cdots\\
&\phantom{=aaaaaaaaaa}+X_1\otimes\cdots\otimes X_r\otimes\alpha^1\otimes\alpha^2\otimes\cdots\otimes(\nabla_X\alpha^s)\end{aligned}$$

and so, evaluating on $\omega^1,\ldots,\omega^r\in\Omega^1(M)$, $Y_1,\ldots, Y_s\in\mathfrak{X}(M)$ the value of $\nabla_XF$, that value is

$$\sum_{i=1}^r\omega^1(X_1)\omega^2(X_2)\cdots\omega^i(\nabla_XX_i)\cdots\omega^r(X_r)\alpha^1(Y_1)\cdots\alpha^s(Y_s)+\sum_{j=1}^s\omega^1(X_1)\cdots\omega^r(X_r)\left(\prod_{l\neq j}\alpha^l(Y_l)\right)\left(X(\alpha^j(Y_j))-\alpha^j(\nabla_XY_j)\right)$$

and rewriting the first sum on the right-hand side using

$$\omega^i(\nabla_XX_i)=X(\omega^i(X_i))-(\nabla_X\omega^i)(X_i)$$

we obtain the formula

$$\begin{aligned}\nabla_XF(\omega^1,\ldots,\omega^r,Y_1,\ldots, Y_s)&=X(F(\omega^1,\ldots,\omega^r,Y_1,\ldots, Y_s))\\
&\phantom{=aa}-\sum_{i=1}^r F(\omega^1,\ldots,\nabla_X\omega^i,\ldots,\omega^r,Y_1,\ldots, Y_s)\\
&\phantom{=aaaa}-\sum_{j=1}^s F(\omega^1,\ldots, \omega^r,Y_1,\ldots, \nabla_XY_j,\ldots, Y_s)\end{aligned}$$

Since this formula holds for all simple $(r,s)$-tensors, it holds for all $(r,s)$-tensors as well. Now, that $\nabla$ defined in this way satisfies the desired conditions and is uniquely determined by the condition $\nabla_Xf=Xf$ and the condition that on $T^\ast M$ it coincides with $\nabla^\ast$ is the result of a simple calculation.

## Total connection

Consider on $\mathcal{T}^{r,s}(M)$ the connection $\nabla$ defined above. For any $(r,s)$-tensor $F$, $\nabla F$ can be regarded as taking $r$ $1$-forms $\omega^1,\ldots,\omega^r$ and $s+1$ vector fields $Y_1,\ldots, Y_s, X$ to output the $C^\infty(M)$ function

$$(\nabla_XF)(\omega^1,\ldots,\omega^r,Y_1,\ldots, Y_s)$$

as an $(r,s+1)$-tensor $\nabla F$.

In particular, for a $(0,0)$-tensor, that is, a $C^\infty$ function $f$, applying $\nabla$ yields a $(0,1)$-tensor $\nabla f$. By definition, the covector $\nabla f$ is defined by the formula

$$X\mapsto \nabla_Xf=Xf$$

On the other hand, setting $M=\mathbb{R}^m$ and, as in [§Riemannian Metrics, §§Musical Isomorphism](/en/math/riemannian_geometry/Riemannian_metric#musical-isomorphism){: data-lid="khi28" }, regarding, for a function $f$, the gradient vector $\operatorname{grad} f$ as the covector defined by the formula

$$X\mapsto \langle X, \operatorname{grad} f\rangle$$

we see from the properties of the gradient vector that $\langle X,\operatorname{grad} f\rangle=Xf$. This explains why the gradient vector has traditionally also been denoted by $\nabla f$. To treat this on a general manifold, a Riemannian metric must inevitably be introduced, so the details will be covered in the next post.

Now, the *second covariant derivative* $\nabla_{X,Y}^2 F$ is defined by the formula

$$\nabla_{X,Y}^2F(\ldots)=(\nabla^2 F)(\cdots, Y,X)$$

as the $(r,s)$-tensor $\nabla_{X,Y}^2F$ satisfying it. The tensor $\nabla_{X,Y}^2F$ defined in this way is, with respect to $Y$, $C^\infty(M)$-linear, but because $\nabla_X\nabla_Y$ is, with respect to $Y$, not $C^\infty$-linear, in general $\nabla_{X,Y}^2\neq\nabla_X\nabla_Y$. However, the following holds.

::: Proposition 6
For any $(r,s)$-tensor $F$,

$$\nabla_{X,Y}^2F=\nabla_X(\nabla_YF)-\nabla_{\nabla_XY}F$$

holds.
:::
::: Proof
One need only plug $(\omega^1,\ldots,\omega^r,Z_1,\ldots,Z_s)$ into the right-hand side.
:::

In particular, applying this to a $(0,0)$-tensor $C^\infty(M)$ yields the *covariant Hessian* $\nabla^2 u$. 

---

**References**

**[Lee]** John M. Lee. *Introduction to Riemannian Manifolds*, Graduate texts in mathematics, Springer, 2019  

---
