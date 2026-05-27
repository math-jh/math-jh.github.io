---
title: "Riemannian Metric"
excerpt: "The Riemannian metric as a positive-definite symmetric 2-tensor on the tangent bundle"

categories: [Math / Riemannian Geometry]
permalink: /en/math/riemannian_geometry/Riemannian_metric
header:
    overlay_image: /assets/images/Math/Riemannian_Geometry/Riemannian_Metric.png
    overlay_filter: 0.5
sidebar: 
    nav: "riemannian_geometry-en"

date: 2022-12-16
last_modified_at: 2022-12-16
weight: 1
translated_at: 2026-05-22T11:00:02+00:00
translation_source: kimi-cli
---
## Riemannian Metric

We defined the exterior algebra bundle

$$\bigwedge\nolimits(T^\ast M)\cong\bigoplus_{k=0}^n\bigwedge\nolimits^k(T^\ast M)$$

using exterior algebra in [\[Differentiable Manifolds\] §Differential Forms](/en/math/manifold/differential_forms), and defined a smooth section of this bundle as a differential form. We can do something similar using the symmetric algebra, and unlike the exterior algebra, the case $$k=2$$ is of interest. This is because the elements of $$\mathcal{S}^2(T^\ast M)$$ arising when $$k=2$$ define symmetric bilinear forms on $$TM$$.

Fix a point $$p\in M$$. Then $$g_p$$ is an element of $$\mathcal{S}^2(T^\ast_pM)$$. Now, by the same argument we checked after [\[Differentiable Manifolds\] §Differential Forms, ⁋Definition 1](/en/math/manifold/differential_forms#def1), we can see that $$\mathcal{S}^2(T^\ast_pM)\cong(\mathcal{S}^2(T_pM))^\ast$$, and by [\[Multilinear Algebra\] §Tensor Algebras, ⁋Proposition 11](/en/math/multilinear_algebra/tensor_algebras#prop11), we can think of $$g_p$$ as a symmetric multilinear map from $$T_pM\times T_pM$$ to $$\mathbb{R}$$. Therefore, if we only impose an appropriate non-degeneracy condition on $$g_p$$, we can regard it as an inner product defined on $$T_pM$$. ([\[Linear Algebra\] §Inner Product Spaces, ⁋Definition 1](/en/math/linear_algebra/inner_product_spaces))

<div class="definition" markdown="1">

<ins id="def1">**Definition 1**</ins> A *Riemannian metric* on a manifold $$M$$ is a smooth section $$g\in\Gamma(\mathcal{S}^2(T^\ast M))$$ that is positive-definite in the following sense.

> (Positive-definiteness) For any $$p\in M$$, $$g_p(v,v)>0$$ holds for all nonzero $$v\in T_pM$$.

</div>

If we weaken the positive-definiteness condition in the above definition to non-degeneracy, the smooth section $$g \in \Gamma(\mathcal{S}^2(T^\ast M))$$ is called a *pseudo-Riemannian metric*. In this case, $$g_p$$ is no longer an inner product, but it defines a non-degenerate symmetric bilinear form on $$T_pM$$.

As we saw above, if $$g$$ is a Riemannian metric, then at any point $$p$$, $$g_p(-,-)$$ defines an inner product on $$T_pM$$, so we denote it simply by $$\langle -,-\rangle_g$$.

In particular, if we take a coordinate system $$(U,(x^i))$$ in a neighborhood of a point $$p$$, then we can express $$g$$ in the form

$$g=\sum_{i,j=1}^ng_{ij}dx^i\otimes dx^j$$

and in this case, $$g$$ being a Riemannian metric is equivalent to the $$n\times n$$ matrix $$(g_{ij})$$ being symmetric and positive-definite.

Suppose two inner products $$g$$ and $$g'$$ are given on a vector space $$V$$. Then the $$g+g'$$ defined by the formula

$$(g+g')(v,w)=g(v,w)+g'(v,w)$$

is also an inner product. Also, if $$g$$ is an inner product, then $$\alpha g$$, where $$\alpha$$ is a nonzero constant, is also an inner product. Now since Euclidean space has an inner product, we can define an inner product on each coordinate chart $$(U,\varphi)$$ of any manifold $$M$$, and by adding them all together via a partition of unity, we can create a function on $$M$$. By the preceding observation, this function becomes a Riemannian metric. That is, any manifold always admits a Riemannian metric.

## Musical Isomorphism

From an algebraic point of view, one of the best consequences of a non-degenerate pairing is that this pairing induces an isomorphism between $$V$$ and its dual space $$V^\ast$$. ([\[Linear Algebra\] §Bilinear Forms, §§Nondegenerate Bilinear Forms](/en/math/linear_algebra/bilinear_form#non-degenerate-bilinear-forms)) Likewise, if a Riemannian metric $$g$$ is given, then $$g$$ induces an isomorphism between the two bundles $$TM$$ and $$T^\ast M$$ through the formula

$$\tilde{g}:T_pM\rightarrow T_p^\ast M;\qquad(p,v)\mapsto (p,\langle v,-\rangle)\tag{1}$$

Through this, given any vector field $$X$$, we obtain a smooth section $$\tilde{g}(X)$$ of $$T^\ast M$$.

To examine this in more detail, fix a coordinate chart $$(x^i)$$. Then for any two vector fields

$$X=\sum_{i=1}^n X^i\frac{\partial}{\partial x^i},\quad Y=\sum_{i=1}^n Y^i\frac{\partial}{\partial x^i}$$

we have

$$\tilde{g}(X)(Y)=\sum_{i,j=1}^ng_{ij}dx^i(X)\otimes dx^j(Y)=\sum_{i,j=1}^ng_{ij}X^iY^j$$

Now if we substitute $$\partial/\partial x^j$$ for $$Y$$, we can see that $$\tilde{g}(X)$$ is given by the formula

$$\tilde{g}(X)=\sum_{i,j=1}^n g_{ij}X^idx^j$$

We sometimes abbreviate $$\sum_{i=1}^ng_{ij}X^i$$ as $$X_j$$; then the above formula becomes $$\tilde{g}(X)=\sum_{j=1}^nX_j dx^j$$, so it looks as if the index of $$X^i$$ has been lowered. For this reason, with a slight notational trick, we denote the covector field $$\tilde{g}(X)$$ by $$X^\flat$$.

Of course, since (1) is an isomorphism, given any covector field $$\omega$$ we can also obtain the corresponding vector field. This vector field is (naturally) denoted by $$\omega^\sharp$$, and together these are called the *musical isomorphism*. Of course, these two are inverses of each other.

## Length of a Curve

Meanwhile, a Riemannian metric finally allows us to do geometry on a manifold, such as measuring distances and angles. Recall that if an inner product is defined on any vector space $$V$$, then we can endow $$V$$ with a distance via $$\lVert v\rVert:=\sqrt{\langle v,v\rangle}$$.

<div class="definition" markdown="1">

<ins id="def2">**Definition 2**</ins> Let $$(M,g)$$ be a Riemannian manifold, and let $$\gamma:[a,b]\rightarrow M$$ be a curve defined on it. Then the *length* $$\length(\gamma)$$ of $$\gamma$$ is defined by the formula

$$\length(\gamma)=\int_a^b\lVert\dot{\gamma}(t)\rVert_g\mathop{dt}$$

</div>

The length of a curve defined in this way does not depend on the parametrization. Meanwhile, through the above definition we can make $$M$$ into a metric space. To do this, we simply define

$$d_g(p,q)=\inf_{\gamma\text{ connecting }p,q}\length(\gamma)$$

## Normal Bundle

Finally, we can define the notion of a *normal bundle*. Let an arbitrary Riemannian manifold $$M$$ be given, and consider a submanifold $$S$$. Then by restricting $$g$$ to $$S$$, we obtain a Riemannian metric $$\iota^\ast g$$ on $$S$$. By the

$$d\iota(T_pS)\subseteq T_pM$$

induced by $$\iota$$, we can regard $$T_pS$$ as a subspace of $$T_pM$$, and therefore $$T_pS$$ is a direct summand of $$T_pM$$. In general, there is no canonical way to give a complementary subspace of $$T_pS$$, but when $$T_pM$$ is an inner product space as it is now, we can define it as $$(T_pS)^\perp$$. The vector bundle over $$\iota(S)$$ with such bundles $$(T_pS)^\perp$$ attached at each point $$p$$ is called the *normal bundle* of $$S$$ and is denoted by $$NS$$.

---

**References**

**[Lee]** John M. Lee. *Introduction to Riemannian Manifolds*, Graduate texts in mathematics, Springer, 2019  

---
