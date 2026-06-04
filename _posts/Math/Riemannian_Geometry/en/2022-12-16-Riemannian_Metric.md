---
title: "Riemannian Metric"
description: "A Riemannian metric is a smooth positive-definite section that assigns an inner product to each tangent space on a manifold, giving it a geometric structure. The post also covers generalizations to pseudo-Riemannian metrics and local coordinate representations."
excerpt: "The Riemannian metric as a positive-definite symmetric 2-tensor on the tangent bundle"

categories: [Math / Riemannian Geometry]
permalink: /en/math/riemannian_geometry/Riemannian_metric
sidebar: 
    nav: "riemannian_geometry-en"

date: 2022-12-16
last_modified_at: 2022-12-16
weight: 1
translated_at: 2026-06-01T22:00:01+00:00
translation_source: kimi-cli
last_polished_at: 2026-06-01T22:00:01+00:00
---
## Riemannian Metric

We defined the exterior algebra bundle

$$\bigwedge\nolimits(T^\ast M)\cong\bigoplus_{k=0}^n\bigwedge\nolimits^k(T^\ast M)$$

using exterior algebra in [\[Manifolds\] §Differential Forms](/en/math/manifold/differential_forms), and defined a smooth section of this bundle as a differential form. The same construction works with the symmetric algebra; unlike the exterior case, the case $$k=2$$ is of particular interest. This is because the elements of $$\mathcal{S}^2(T^\ast M)$$ that arise when $$k=2$$ define symmetric bilinear forms on $$TM$$.

Fix a point $$p\in M$$. Then $$g_p$$ is an element of $$\mathcal{S}^2(T^\ast_pM)$$. By the same argument we verified after [\[Manifolds\] §Differential Forms, ⁋Definition 1](/en/math/manifold/differential_forms#def1), we see that $$\mathcal{S}^2(T^\ast_pM)\cong(\mathcal{S}^2(T_pM))^\ast$$, and by [\[Multilinear Algebra\] §Tensor Algebras, ⁋Proposition 11](/en/math/multilinear_algebra/tensor_algebras#prop11), we may regard $$g_p$$ as a symmetric multilinear map from $$T_pM\times T_pM$$ to $$\mathbb{R}$$. Hence, provided we impose an appropriate non-degeneracy condition on $$g_p$$, we may view it as an inner product on $$T_pM$$. ([\[Linear Algebra\] §Inner Product Spaces, ⁋Definition 1](/en/math/linear_algebra/inner_product_spaces#def1))

<div class="definition" markdown="1">

<ins id="def1">**Definition 1**</ins> A *Riemannian metric* on a manifold $$M$$ is a smooth section $$g\in\Gamma(\mathcal{S}^2(T^\ast M))$$ that is positive-definite in the following sense.

> (Positive-definiteness) For any $$p\in M$$, we have $$g_p(v,v)>0$$ for all nonzero $$v\in T_pM$$.

</div>

If we weaken the positive-definiteness condition above to non-degeneracy, the resulting smooth section $$g \in \Gamma(\mathcal{S}^2(T^\ast M))$$ is called a *pseudo-Riemannian metric*. In this case, $$g_p$$ is no longer an inner product, but it defines a non-degenerate symmetric bilinear form on $$T_pM$$.

As observed above, if $$g$$ is a Riemannian metric, then at each point $$p$$ the map $$g_p(-,-)$$ defines an inner product on $$T_pM$$; we denote it simply by $$\langle -,-\rangle_g$$.

In particular, if we take a coordinate system $$(U,(x^i))$$ in a neighborhood of a point $$p$$, then we can express $$g$$ in the form

$$g=\sum_{i,j=1}^ng_{ij}dx^i\otimes dx^j$$

and $$g$$ is a Riemannian metric if and only if the $$n\times n$$ matrix $$(g_{ij})$$ is symmetric and positive-definite.

Suppose two inner products $$g$$ and $$g'$$ are given on a vector space $$V$$. Then the sum $$g+g'$$ defined by

$$(g+g')(v,w)=g(v,w)+g'(v,w)$$

is also an inner product. Moreover, if $$g$$ is an inner product and $$\alpha$$ is a nonzero constant, then $$\alpha g$$ is again an inner product. Since Euclidean space carries an inner product, we can define an inner product on each coordinate chart $$(U,\varphi)$$ of any manifold $$M$$, and by adding these together via a partition of unity we obtain a function on $$M$$. By the preceding observation, this function is a Riemannian metric. Thus every manifold admits a Riemannian metric.

## Musical Isomorphism

From an algebraic standpoint, one of the most useful consequences of a non-degenerate pairing is that it induces an isomorphism between $$V$$ and its dual space $$V^\ast$$. ([\[Linear Algebra\] §Bilinear Forms, §§Non-Degenerate Bilinear Forms](/en/math/linear_algebra/bilinear_form#non-degenerate-bilinear-forms)) Likewise, if a Riemannian metric $$g$$ is given, then $$g$$ induces an isomorphism between the bundles $$TM$$ and $$T^\ast M$$ via the formula

$$\tilde{g}:T_pM\rightarrow T_p^\ast M;\qquad(p,v)\mapsto (p,\langle v,-\rangle)\tag{1}$$

Consequently, given any vector field $$X$$, we obtain a smooth section $$\tilde{g}(X)$$ of $$T^\ast M$$.

To examine this in more detail, fix a coordinate chart $$(x^i)$$. Then for any two vector fields

$$X=\sum_{i=1}^n X^i\frac{\partial}{\partial x^i},\quad Y=\sum_{i=1}^n Y^i\frac{\partial}{\partial x^i}$$

we have

$$\tilde{g}(X)(Y)=\sum_{i,j=1}^ng_{ij}dx^i(X)\otimes dx^j(Y)=\sum_{i,j=1}^ng_{ij}X^iY^j$$

Substituting $$\partial/\partial x^j$$ for $$Y$$, we see that $$\tilde{g}(X)$$ is given by

$$\tilde{g}(X)=\sum_{i,j=1}^n g_{ij}X^idx^j$$

We sometimes abbreviate $$\sum_{i=1}^ng_{ij}X^i$$ as $$X_j$$; the above formula then becomes $$\tilde{g}(X)=\sum_{j=1}^nX_j dx^j$$, so the index of $$X^i$$ appears to have been lowered. For this reason, with a slight notational convention the covector field $$\tilde{g}(X)$$ is denoted by $$X^\flat$$.

Of course, since (1) is an isomorphism, given any covector field $$\omega$$ we can also obtain the corresponding vector field. This vector field is (naturally) denoted by $$\omega^\sharp$$, and the two maps taken together are called the *musical isomorphism*. They are inverses of each other.

## Length of a Curve

A Riemannian metric finally allows us to do geometry on a manifold: measuring distances, angles, and so forth. Recall that once an inner product is defined on a vector space $$V$$, we can endow $$V$$ with a norm via $$\lVert v\rVert:=\sqrt{\langle v,v\rangle}$$.

<div class="definition" markdown="1">

<ins id="def2">**Definition 2**</ins> Let $$(M,g)$$ be a Riemannian manifold and let $$\gamma:[a,b]\rightarrow M$$ be a curve defined on it. Then the *length* $$\length(\gamma)$$ of $$\gamma$$ is defined by

$$\length(\gamma)=\int_a^b\lVert\dot{\gamma}(t)\rVert_g\mathop{dt}$$

</div>

The length of a curve defined in this way is independent of the parametrization. Moreover, via the above definition we can make $$M$$ into a metric space by setting

$$d_g(p,q)=\inf_{\gamma\text{ connecting }p,q}\length(\gamma)$$

## Normal Bundle

Finally, we can define the notion of a *normal bundle*. Let $$M$$ be a Riemannian manifold and let $$S$$ be a submanifold. Restricting $$g$$ to $$S$$ yields a Riemannian metric $$\iota^\ast g$$ on $$S$$. The inclusion $$\iota$$ induces

$$d\iota(T_pS)\subseteq T_pM$$

so we may regard $$T_pS$$ as a subspace of $$T_pM$$, and hence $$T_pS$$ is a direct summand of $$T_pM$$. In general there is no canonical way to choose a complementary subspace of $$T_pS$$, but because $$T_pM$$ is now an inner product space we can define it as $$(T_pS)^\perp$$. The vector bundle over $$\iota(S)$$ with the fibers $$(T_pS)^\perp$$ attached at each point $$p$$ is called the *normal bundle* of $$S$$ and is denoted by $$NS$$.

---

**References**

**[Lee]** John M. Lee. *Introduction to Riemannian Manifolds*, Graduate texts in mathematics, Springer, 2019  

---
