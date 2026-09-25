---
title: "Riemannian Metrics"
description: "A Riemannian metric equips each tangent space of a smooth manifold with an inner product, giving it geometric structure. This post also explores representations in local coordinates and generalizations to pseudo-Riemannian metrics."
excerpt: "Riemannian metrics as positive-definite symmetric 2-tensors on the tangent bundle"

categories: [Math / Riemannian Geometry]
permalink: /en/math/riemannian_geometry/Riemannian_metric
sidebar: 
    nav: "riemannian_geometry-en"

date: 2022-12-16
weight: 1
translated_at: 2026-09-25T23:15:05+00:00
translation_source: antigravity-gemini-3.8-flash-high
---
## Riemannian Metrics

In [\[Differentiable Manifolds\] §Differential Forms](/en/math/manifolds/differential_forms){: data-lid="7vv5q" }, we used the exterior algebra to define the exterior algebra bundle

$$\bigwedge\nolimits(T^\ast M)\cong\bigoplus_{k=0}^n\bigwedge\nolimits^k(T^\ast M)$$

and defined a differential form as a smooth section of this bundle. A similar construction can be carried out using the symmetric algebra, and unlike the case of the exterior algebra, the case $k=2$ is of particular interest. This is because when $k=2$, the resulting elements of $\mathcal{S}^2(T^\ast M)$ define symmetric bilinear forms on $TM$.

Fix a point $p\in M$. Then for a smooth section $g\in\Gamma(\mathcal{S}^2(T^\ast M))$, its value $g_p$ is an element of $\mathcal{S}^2(T^\ast_pM)$. Now, through an argument identical to the one verified after [\[Differentiable Manifolds\] §Differential Forms, ⁋Definition 1](/en/math/manifolds/differential_forms#def1){: data-lid="wo700" }, we see that $\mathcal{S}^2(T^\ast_pM)\cong(\mathcal{S}^2(T_pM))^\ast$, and by [\[Multilinear Algebra\] §Tensor Algebra, ⁋Proposition 7](/en/math/multilinear_algebra/tensor_algebras#prop7){: data-lid="j7w90" }, we can view $g_p$ as a symmetric multilinear map from $T_pM\times T_pM$ to $\mathbb{R}$. Therefore, if we impose a suitable positive-definiteness condition on $g_p$, we can regard it as an inner product defined on $T_pM$. ([\[Linear Algebra\] §Inner Product Spaces, ⁋Definition 1](/en/math/linear_algebra/inner_product_spaces#def1){: data-lid="rwd4y" })

::: Definition 1
A *Riemannian metric* on a manifold $M$ means a smooth section $g\in\Gamma(\mathcal{S}^2(T^\ast M))$ that is positive-definite in the following sense:

> (Positive-definiteness) For every $p\in M$, $g_p(v,v)>0$ holds for all non-zero $v\in T_pM$.
:::

A smooth section $g \in \Gamma(\mathcal{S}^2(T^\ast M))$ obtained by weakening the positive-definiteness condition in the definition above to non-degeneracy is called a *pseudo-Riemannian metric*. In this case, $g_p$ is no longer an inner product, but it defines a non-degenerate symmetric bilinear form on $T_pM$.

As seen above, if $g$ is a Riemannian metric, then at any point $p$, $g_p(-,-)$ defines an inner product on $T_pM$, which we denote simply by $\langle -,-\rangle_g$. Also, a manifold equipped with a Riemannian metric $g$ is written as a pair $(M,g)$ and called a *Riemannian manifold*.

In particular, if around a point $p$ we choose a coordinate system $(U,(x^i))$, then $g$ can be expressed in the form

$$g=\sum_{i,j=1}^ng_{ij}\dd{x}^i\otimes \dd{x}^j$$

and here, $g$ being a Riemannian metric is equivalent to the $n\times n$ matrix $(g_{ij})$ being symmetric and positive-definite.

Suppose that on a vector space $V$, two inner products $g$ and $g'$ are given. Then $g+g'$, defined by

$$(g+g')(v,w)=g(v,w)+g'(v,w)$$

is also an inner product. Also, if $g$ is an inner product, then for any $\alpha>0$, multiplying by the constant $\alpha$ yields $\alpha g$, which is also an inner product. Now, since an inner product exists on Euclidean space, for any manifold $M$ we can well-define an inner product on each coordinate chart $(U,\varphi)$, and by summing them all via a partition of unity, we can construct a smooth section of $\mathcal{S}^2(T^\ast M)$. By the preceding observation, this section is a Riemannian metric. That is, every manifold can always be given a Riemannian metric.

## Musical isomorphism

From an algebraic perspective, one of the best consequences of a non-degenerate pairing is that it induces an isomorphism between $V$ and its dual space $V^\ast$. ([\[Linear Algebra\] §Bilinear Forms, §§Non-degenerate Bilinear Forms](/en/math/linear_algebra/bilinear_form#non-degenerate-bilinear-forms){: data-lid="5a3b6" }) Similarly, given a Riemannian metric $g$, $g$ induces via

$$\tilde{g}:TM\rightarrow T^\ast M;\qquad(p,v)\mapsto (p,\langle v,-\rangle)\tag{1}$$

an isomorphism between the two bundles $TM$ and $T^\ast M$. Through this, given any vector field $X$, we obtain a smooth section of $T^\ast M$, $\tilde{g}(X)$.

To examine this in more detail, let us fix a coordinate chart $(x^i)$. Then for any two vector fields

$$X=\sum_{i=1}^n X^i\frac{\partial}{\partial x^i},\quad Y=\sum_{i=1}^n Y^i\frac{\partial}{\partial x^i}$$

we have

$$\tilde{g}(X)(Y)=\sum_{i,j=1}^ng_{ij}\dd{x}^i(X)\dd{x}^j(Y)=\sum_{i,j=1}^ng_{ij}X^iY^j$$

Now, plugging into $Y$ the vectors $\partial/\partial x^j$, we see that $\tilde{g}(X)$ is given by

$$\tilde{g}(X)=\sum_{i,j=1}^n g_{ij}X^i\dd{x}^j$$

Often, $\sum_{i=1}^ng_{ij}X^i$ is abbreviated as $X_j$; then the expression above becomes $\tilde{g}(X)=\sum_{j=1}^nX_j \dd{x}^j$, so it looks as if the index of $X^i$ has been lowered. For this reason, with a slight play on notation, we denote the covector field $\tilde{g}(X)$ by $X^\flat$.

Of course, since (1) is an isomorphism, given any covector field $\omega$, one can also obtain the corresponding vector field. This vector field is (naturally) denoted by $\omega^\sharp$, and together these two are called the *musical isomorphism*. Of course, they are inverses of each other.

## Length of Curves

Meanwhile, a Riemannian metric finally allows us to do geometry on manifolds, such as measuring distances and angles. Recall that once an inner product is defined on any vector space $V$, via $\lVert v\rVert:=\sqrt{\langle v,v\rangle}$ we could endow $V$ with a metric.

::: Definition 2
Let $(M,g)$ be a Riemannian manifold, and let $\gamma:[a,b]\rightarrow M$ be a piecewise $C^\infty$ curve defined on it. Then, for $\gamma$, the *length* $\length(\gamma)$ is defined by

$$\length(\gamma)=\int_a^b\lVert\dot{\gamma}(t)\rVert_g\dd{t}$$
:::

The length of a curve defined in this way does not depend on the parametrization. Meanwhile, if $M$ is connected, we can make $M$ into a metric space via the definition above. To this end, it suffices to define

$$d_g(p,q)=\inf_{\gamma\text{ connecting }p,q}\length(\gamma)$$

## Normal bundle

Finally, we can define the concept of a *normal bundle*. Suppose a Riemannian manifold $M$ is given, and consider a submanifold $S$. Then by restricting $g$ to $S$, we obtain on $S$ a Riemannian metric $\iota^\ast g$. Through the relation induced by $\iota$,

$$\dd{\iota}(T_pS)\subseteq T_pM$$

we can view $T_pS$ as a subspace of $T_pM$, and therefore $T_pS$ is a direct summand of $T_pM$. In general, there is no canonical way to provide a complementary subspace of $T_pS$, but when $T_pM$ is an inner product space as it is now, we can define it to be $(T_pS)^\perp$. To each point $p$, attaching such a subspace $(T_pS)^\perp$ yields a vector bundle over $\iota(S)$, which we call the *normal bundle* of $S$ and write as $NS$.

---

**References**

**[Lee]** John M. Lee. *Introduction to Riemannian Manifolds*, Graduate texts in mathematics, Springer, 2019  

---
