---
title: "Connection"
description: "We define a connection on a vector bundle to introduce covariant differentiation, and discuss the key properties of covariant differentiation that depend on the Leibniz rule and local properties of vector fields."
excerpt: "Differentiation on a vector bundle"

categories: [Math / Riemannian Geometry]
permalink: /en/math/riemannian_geometry/connection
sidebar: 
    nav: "riemannian_geometry-en"

date: 2022-12-16
last_modified_at: 2022-12-16
weight: 2
translated_at: 2026-06-01T21:30:01+00:00
translation_source: kimi-cli
last_polished_at: 2026-06-01T21:30:01+00:00
---
## Connections and Covariant Differentiation

Using the Lie derivative, we can differentiate vector fields or differential forms, but it is impossible to extend this concept to sections $$\Gamma(E)$$ of an arbitrary vector bundle $$\pi:E\rightarrow M$$. On the tangent bundle $$TM$$, given two points $$p,q$$ on an integral flow $$\phi$$, there exists a natural isomorphism $$d\phi^{-t}$$ connecting the two tangent spaces $$T_pM$$ and $$T_qM$$; however, no such map exists between two fibers $$E_p$$ and $$E_q$$ of an arbitrary vector bundle $$E$$. Therefore, we additionally define a *connection* that joins these fibers.

<div class="definition" markdown="1">

<ins id="def1">**Definition 1**</ins> Given a vector bundle $$E\rightarrow M$$ over a manifold $$M$$, a *connection* $$\nabla:\mathfrak{X}(M)\times\Gamma(E)\rightarrow\Gamma(E)$$ on $$E$$ is a map satisfying the following conditions.

1. (Tensoriality) $$\nabla_XY$$ is $$C^\infty$$-linear in the first argument.
2. (Linearity) $$\nabla_XY$$ is $$\mathbb{R}$$-linear in the second argument.
3. For any $$f\in C^\infty(M)$$, $$\nabla$$ satisfies the Leibniz rule
    
    $$\nabla_X(fY)=f\nabla_XY+(Xf)Y$$

</div>

Here, $$\nabla_XY$$ is also called the *covariant derivative* of $$Y$$ in the direction of $$X$$. The following proposition shows that to compute $$(\nabla_XY)_p$$, it suffices to know $$X$$ and $$Y$$ in a neighborhood of $$p$$.

<div class="proposition" markdown="1">

<ins id="prop2">**Proposition 2**</ins> Let $$M$$ be a manifold, and let $$X\in\mathfrak{X}(M)$$ and $$Y\in\Gamma(E)$$. For any point $$p\in M$$, $$(\nabla_XY)_p$$ depends only on

1. the value $$X_p$$ of the vector field $$X$$ at $$p$$,
2. the restriction $$Y\vert_U$$ of the vector field $$Y$$ to an open neighborhood $$U$$ of $$p$$.

</div>
<details class="proof" markdown="1">
<summary>Proof</summary>

First, we show that $$(\nabla_XY)_p$$ depends only on the vector field in an open neighborhood $$U$$ of $$p$$. To show that $$(\nabla_XY_1)_p=(\nabla_XY_2)_p$$ whenever two vector fields $$Y_1,Y_2$$ agree on an open neighborhood $$U$$ of $$p$$, it suffices to show that if a vector field $$Y$$ is identically zero on an open neighborhood $$U$$, then $$(\nabla_XY)_p=0$$. Let $$\varphi$$ be a bump function satisfying $$\supp(\varphi)\subseteq U$$ and $$\varphi(p)=1$$; then the vector field $$\varphi Y$$ is identically zero on all of $$M$$. Therefore, by the second condition of [Definition 1](#def1), $$\nabla_X(\varphi Y)=0$$. On the other hand, by the Leibniz rule,

$$0=\nabla_X(\varphi Y)=\varphi\nabla_XY+(X\varphi)Y$$

and evaluating the right-hand side at $$p$$ yields

$$\varphi(p)(\nabla_XY)_p+(X\varphi)(p)Y_p=(\nabla_XY)_p$$

so $$(\nabla_XY)_p=0$$.

Now we show that $$\nabla_XY$$ depends only on the vector $$X_p$$ at $$p$$. As above, it suffices to assume $$X_p=0$$ and show that $$(\nabla_XY)_p=0$$. Take a coordinate chart $$(U,(x^i))$$ in a neighborhood of $$p$$, and write $$X$$ with respect to this coordinate system as

$$X=X^1\frac{\partial}{\partial x^1}+\cdots+X^n\frac{\partial}{\partial x^n}$$

Then

$$(\nabla_XY)_p=(\nabla_{\sum X^i\frac{\partial}{\partial x^i}}Y)_p=\left(\sum_{i=1}^n X^i\nabla_{\partial/\partial x^i} Y\right)_p$$

and since $$X^i(p)=0$$ for all $$i$$, we obtain the desired result.

</details>

## Covariant Differentiation on the Tangent Bundle

In particular, let us examine a connection defined on the tangent bundle $$TM\rightarrow M$$. Then $$\nabla$$ is a map from $$\mathfrak{X}(M)\times\mathfrak{X}(M)$$ to $$\mathfrak{X}(M)$$. It should be noted that although the Lie derivative and a connection are both concepts devised to formalize differentiation, they yield different results. For instance, for the Lie derivative

$$\mathcal{L}_{fX}Y=[fX,Y]=fX(Y)-Y(fX)=fX(Y)-(Yf)X-fY(X)=f[X,Y]-(Yf)X=f\mathcal{L}_XY-(Yf)X$$

whereas, by definition,

$$\nabla_{fX}Y=f\nabla_XY$$

so one can always choose $$Y$$ and $$f$$ appropriately such that $$\nabla_{fX}Y\neq\mathcal{L}_{fX}Y$$.

Now, considering a connection defined on $$TM$$, [Proposition 2](#prop2) implies that the value of $$\nabla_XY$$ at a point $$p$$ is completely determined by local frames $$(E_i)$$ in a neighborhood of $$p$$. This is because

$$(\nabla_XY)_p=\nabla_{\sum X^i(p)E_i(p)}\left(\sum Y^i(p)E_i(p)\right)$$

holds. On the other hand,

$$\nabla_X\left(\sum_{j=1}^n Y^jE_j\right)=\sum_{j=1}^n \nabla_X(Y^jE_j)=\sum_{j=1}^n\left(Y^j\nabla_XE_j+X(Y^j)E_j\right)=\sum_{i,j=1}^nX^iY^j\nabla_{E_i}E_j+\sum_{j=1}^n X(Y^j)E_j\tag{1}$$

so $$\nabla_XY$$ is completely determined by the $$n^2$$ vector fields $$\nabla_{E_i}E_j$$. Writing each vector field $$\nabla_{E_i}E_j$$ as a linear combination of the $$E_k$$'s,

$$\nabla_{E_i}E_j=\Gamma_{ij}^k E_k$$

there exist $$n^3$$ $$C^\infty$$ functions $$\Gamma_{ij}^k$$ satisfying this. Then equation (1) above can be written as

$$\nabla_XY=\sum_{k=1}^n\left(\sum_{i,j=1}^nX(Y^k)+X^iY^j\Gamma_{ij}^k\right)E_k$$

<div class="definition" markdown="1">

<ins id="def3">**Definition 3**</ins> The $$n^3$$ functions $$\Gamma_{ij}^k$$ defined above are called the *connection coefficients*.

</div>

On the other hand, the tangent bundle over any manifold $$M$$ always admits a connection. To verify this, just as with a Riemannian metric, one can take the connection on Euclidean space

$$\nabla_vY:=v(Y^1)\frac{\partial}{\partial x^i}+\cdots+v(Y^n)\frac{\partial}{\partial x^n}$$

and patch it together via a partition of unity.

## Covariant Differentiation on the Cotangent Bundle

We show that a connection $$\nabla$$ defined on the tangent bundle $$TM$$ extends nicely to any $$(r,s)$$-tensor field $$\mathcal{T}^{r,s}(M)$$. ([]()) To do this, we must first specify how $$\nabla$$ extends to the cotangent bundle $$T^\ast M$$.

<div class="proposition" markdown="1">

<ins id="prop4">**Proposition 4**</ins> Let $$M$$ be a manifold and let $$\nabla$$ be a connection on the tangent bundle $$TM$$. Define a map $$\nabla^\ast:\mathfrak{X}(M)\times\Gamma(T^\ast M)\rightarrow\Gamma(T^\ast M)$$ by the formula

$$(\nabla_X^\ast\alpha)_p(Y)=X\bigl(\alpha(Y)\bigr)-\alpha_p\bigl(\nabla_XY\bigr)_p$$

Then $$\nabla^\ast$$ is a connection on $$T^\ast M$$.

</div>
<details class="proof" markdown="1">
<summary>Proof</summary>

First, one can show that $$\nabla^\ast\alpha$$ defined by the expression on the right-hand side is a $$1$$-form, so the codomain of $$\nabla^\ast$$ is unproblematic.

That $$\nabla^\ast$$ actually satisfies the conditions for a connection is obvious except for the Leibniz rule. In fact, the Leibniz rule also follows immediately from

$$\begin{aligned}(\nabla_X^\ast f\alpha)_pY&=X(f\cdot\alpha(Y))-(f\alpha)_p(\nabla_XY)_p\\&=(Xf)(\alpha(Y))+f(p)\bigl(X(\alpha(Y))-\alpha_p(\nabla_XY)_p\bigr)\\&=\bigl((Xf)\alpha+f\nabla_X\alpha\bigr)Y\end{aligned}$$

</details>

By a slight abuse of notation, we write the $$\nabla^\ast$$ defined above also as $$\nabla$$.

## Covariant Differentiation on Tensor Fields

Now we can finally extend the connection on $$TM$$ to $$(r,s)$$-tensor fields $$\mathcal{T}^{r,s}(M)$$. As above, we shall write this connection also as $$\nabla$$.

<div class="proposition" markdown="1">

<ins id="prop5">**Proposition 5**</ins> Let $$\nabla$$ be a connection on the tangent bundle $$TM\rightarrow M$$. Then $$\nabla$$ can be extended to all tensor fields $$\mathcal{T}^{r,s}(M)$$ satisfying the following two conditions

$$\nabla_X(F\otimes G)=(\nabla_X F)\otimes G+F\otimes(\nabla_XG),\qquad\nabla_X(F+G)=\nabla_XF+\nabla_XG$$

and the extension is uniquely determined by the additional condition that $$\nabla_Xf=Xf$$ for $$\mathcal{T}^{0,0}M$$.

</div>

An arbitrary $$(r,s)$$-tensor $$F$$ can be regarded as the same as the following linear map

$$\underbrace{\Omega^1(M)\times\cdots\times \Omega^1(M)}_\text{\small $r$ times}\times\underbrace{\mathfrak{X}(M)\times\cdots\times \mathfrak{X}(M)}_\text{\small $s$ times}\rightarrow C^\infty(M)$$

so $$\nabla_XF$$ is uniquely determined by its values on $$\omega^1,\ldots,\omega^r\in\Omega^1(M)$$ and $$Y_1,\ldots, Y_s\in\mathfrak{X}(M)$$. For example, applying the Leibniz rule to a simple tensor $$F=X_1\otimes\cdots\otimes X_r\otimes\alpha^1\otimes\cdots\otimes\alpha^s\in\mathcal{T}^{r,s}(M)$$ yields

$$\begin{aligned}\nabla_X(X_1\otimes\cdots\otimes X_r\otimes\alpha^1\otimes\cdots\otimes\alpha^s)&=(\nabla_XX_1)\otimes X_2\otimes\cdots\otimes X_r\otimes\alpha^1\otimes\cdots\alpha^s\\
&\phantom{=aa}+\cdots\\
&\phantom{=aaaa}+X_1\otimes X_2\otimes\cdots\otimes(\nabla_XX_r)\otimes\alpha^1\otimes\cdots\otimes\alpha^s\\
&\phantom{=aaaaaa}+X_1\otimes\cdots X_r\otimes(\nabla_X\alpha^1)\otimes\alpha^2\otimes\cdots\otimes\alpha^s\\
&\phantom{=aaaaaaaa}+\cdots\\
&\phantom{=aaaaaaaaaa}+X_1\otimes\cdots\otimes X_r\otimes\alpha^1\otimes\alpha^2\otimes\cdots\otimes(\nabla_X\alpha^s)\end{aligned}$$

so, computing the value of $$\nabla_XF$$ on $$\omega^1,\ldots,\omega^r\in\Omega^1(M)$$ and $$Y_1,\ldots, Y_s\in\mathfrak{X}(M)$$, we obtain

$$\sum_{i=1}^r\omega^1(X_1)\omega^2(X_2)\cdots\omega^i(\nabla_XX_i)\cdots\omega^r(X_r)\alpha^1(Y_1)\cdots\alpha^s(Y_s)+\sum_{j=1}^s\omega^1(X_1)\cdots\omega^r(X_r)\left(X(\alpha^j(Y^j))-\alpha^j(\nabla_XY^j)\right)$$

and, replacing the first sum on the right-hand side using

$$\omega^i(\nabla_XX_i)=X(\omega^i(X_i))-(\nabla_X\omega^i)(X_i)$$

we obtain the formula

$$\begin{aligned}\nabla_XF(\omega_1,\ldots,\omega^r,Y_1,\ldots, Y_s)&=X(F(\omega^1,\ldots,\omega^r,Y_1,\ldots, Y_s))\\
&\phantom{=aa}-\sum_{i=1}^r F(\omega^1,\ldots,\nabla_X\omega^i,\ldots,\omega^r,Y_1,\ldots, Y_s)\\
&\phantom{=aaaa}-\sum_{j=1}^s F(\omega^1,\ldots, \omega^r,Y_1,\ldots, \nabla_XY_j,\ldots, Y_s)\end{aligned}$$

This formula holds for all simple $$(r,s)$$-tensors, so it also holds for all $$(r,s)$$-tensors. That this $$\nabla$$ satisfies the desired conditions and is uniquely determined by the condition $$\nabla_Xf=Xf$$ is now a straightforward computation.

## Total Connection

Consider the connection $$\nabla$$ on $$\mathcal{T}^{r,s}(M)$$ defined above. For any $$(r,s)$$-tensor $$F$$, we can think of $$\nabla F$$ as an $$(r,s+1)$$-tensor taking $$r$$ $$1$$-forms $$\omega^1,\ldots,\omega^r$$ and $$s+1$$ vector fields $$Y_1,\ldots, Y_s, X$$ and yielding the $$C^\infty(M)$$ function

$$(\nabla_XF)(\omega^1,\ldots,\omega^r,Y_1,\ldots, Y_s)$$

In particular, applying $$\nabla$$ to a $$(0,0)$$-tensor, i.e., a $$C^\infty$$ function $$f$$, yields a $$(0,1)$$-tensor $$\nabla f$$. By definition, the covector $$\nabla f$$ is defined by the formula

$$X\mapsto \nabla_Xf=Xf$$

On the other hand, setting $$M=\mathbb{R}^m$$ and, as in [§Riemannian Metric, §§Musical Isomorphism](/en/math/riemannian_geometry/Riemannian_metric#musical-isomorphism), regarding the gradient vector $$\operatorname{grad} f$$ of a function $$f$$ as the covector defined by the formula

$$X\mapsto \langle X, \operatorname{grad} f\rangle$$

then by the property of the gradient vector, we know that $$\langle X,\operatorname{grad} f\rangle=Xf$$. This explains why the gradient vector has traditionally also been denoted by $$\nabla f$$. To treat this on a general manifold, a Riemannian metric is inevitably required, so we postpone the details to the next post.

Now the *second covariant derivative* $$\nabla_{X,Y}^2 F$$ is defined as the $$(r,s)$$-tensor $$\nabla_{X,Y}^2F$$ satisfying the formula

$$\nabla_{X,Y}^2F(\ldots)=(\nabla^2 F)(\cdots, Y,X)$$

This $$\nabla_{X,Y}^2F$$ is $$C^\infty(M)$$-linear in $$Y$$, but $$\nabla_X\nabla_Y$$ is not $$C^\infty$$-linear in $$Y$$, so in general $$\nabla_{X,Y}^2\neq\nabla_X\nabla_Y$$. However, the following holds.

<div class="proposition" markdown="1">

<ins id="prop6">**Proposition 6**</ins> For any $$(r,s)$$-tensor $$F$$,

$$\nabla_{X,Y}^2F=\nabla_X(\nabla_YF)-\nabla_{\nabla_XY}F$$

holds.

</div>
<details class="proof" markdown="1">
<summary>Proof</summary>

One need only plug $$(\omega^1,\ldots,\omega^r,Z_1,\ldots,Z_s)$$ into the right-hand side.

</details>

In particular, applying this to a $$(0,0)$$-tensor $$C^\infty(M)$$ yields the *covariant Hessian* $$\nabla^2 u$$. 

---

**References**

**[Lee]** John M. Lee. *Introduction to Riemannian Manifolds*, Graduate texts in mathematics, Springer, 2019  

---
