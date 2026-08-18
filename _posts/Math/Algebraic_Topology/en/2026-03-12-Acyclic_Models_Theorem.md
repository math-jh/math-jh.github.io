---
title: "Acyclic Models Theorem"
description: "We prove the acyclic models theorem, which guarantees the existence of natural transformations between functors satisfying acyclicity and freeness conditions on a category with models. As corollaries, we derive classical results in cohomology theory."
excerpt: "The acyclic models theorem on categories with models and its applications"

categories: [Math / Algebraic Topology]
permalink: /en/math/algebraic_topology/acyclic_models_theorem
sidebar: 
    nav: "algebraic_topology-en"

date: 2025-09-17
weight: 10
translated_at: 2026-08-18T15:45:04+00:00
translation_source: kimi-cli
last_polished_at: 2026-08-18T15:45:04+00:00
---
As mentioned in [§Cohomology](/en/math/algebraic_topology/cohomology), the acyclic models theorem generalizes the original proof of [§Cohomology, ⁋Theorem 9](/en/math/algebraic_topology/cohomology#thm9) in a systematic way, and it can be applied not only to the proof of [§Cohomology, ⁋Theorem 9](/en/math/algebraic_topology/cohomology#thm9) but also to a variety of other situations. In this post, we prove the acyclic models theorem and present several corollaries, including the proof of [§Cohomology, ⁋Theorem 9](/en/math/algebraic_topology/cohomology#thm9).

## Category with models

When developing homology theory, we typically work with $n$-simplices, which allow us to probe arbitrary objects of $\Top$. We formalize this as follows.

::: Definition 1
A *category with models* is a pair $(\mathcal{A},\mathcal{M})$ consisting of a category $\mathcal{A}$ and a collection $\mathcal{M}$ of objects of $\mathcal{A}$. The objects belonging to $\mathcal{M}$ are called *models*.
:::

This definition is not particularly substantial on its own. We now introduce the following.

::: Definition 2
Let $(\mathcal{A},\mathcal{M})$ be a category with models, and let $F_\bullet:\mathcal{A}\rightarrow \Ch_{\geq0}(\lMod{A})$ be a covariant functor.

1. The functor $F_\bullet$ is *acyclic on $\mathcal{M}$* if for every $M\in\mathcal{M}$, we have $H_i(F(M))=0$ for all $i>0$.
2. The functor $F_\bullet$ is *free on $\mathcal{M}$* if for each $n$ there exists a family of models $(M_j)_{j\in J_n}$ such that the natural isomorphism
    
    $$F_n(-)\cong \bigoplus_{j\in J_n}A[\Hom_\mathcal{A}(M_j,-)]$$

    holds. Here $A[S]$ denotes the free $A$-module with basis the set $S$, and each family $(M_j)_{j\in J_n}$ may contain the same model multiple times.
:::

For example, consider the category with models $(\Top, \mathcal{M})$ where $\mathcal{M}$ is the collection of standard $n$-simplices $\Delta^n$. Then the functor $C_\bullet:\Top \rightarrow \Ch_{\geq0}(\Ab)$ assigning to each $X\in \Top$ the singular chain complex $C_\bullet(X)$ is both acyclic on $\mathcal{M}$ and free on $\mathcal{M}$.

- That $C_\bullet$ is acyclic on $\mathcal{M}$ follows because each model $\Delta^n$ is a convex set, hence contractible to a point, and the cone operator induced by the straight-line contraction gives a direct contraction of $C_\bullet(\Delta^n)$ in positive degrees; this can be viewed as a generalization of [§Homology, ⁋Proposition 11](/en/math/algebraic_topology/homology#prop11). Note that the condition that $F_\bullet$ is acyclic on $\mathcal{M}$ does *not* require the $0$th homology of $F_\bullet(X)$ to vanish.
- That $C_\bullet$ is free on $\mathcal{M}$ follows because each $C_n(X)$ is the free abelian group with basis precisely the singular $n$-simplices $\Delta^n \rightarrow X$, that is, $C_n(X)=\mathbb{Z}[\Hom_\Top(\Delta^n,X)]$. In this case, the family of models taken for each $n$ consists of the single model $\Delta^n$.

## Acyclic models theorem

The main theorem of this post is the following.

::: Theorem 3 (Acyclic models theorem)
Let $(\mathcal{A},\mathcal{M})$ be a category with models, and let $F_\bullet, G_\bullet:\mathcal{A}\rightarrow \Ch_{\geq0}(\lMod{A})$ be two functors such that $F_\bullet$ is free on $\mathcal{M}$ and $G_\bullet$ is acyclic on $\mathcal{M}$. Then for any natural transformation

$$f(-)_0:H_0(F(-)) \Rightarrow H_0(G(-))$$

between the two functors

$$H_0(F(-)),H_0(G(-)): \mathcal{A}\rightarrow \lMod{A}$$

there exists a natural transformation

$$f_\bullet(-):F_\bullet(-) \rightarrow G_\bullet(-)$$

with $H_0(f)=f(-)_0$, and such a natural transformation $f$ is unique up to natural chain homotopy.
:::

That is, starting from $f(X)_0: H_0(F(X))\rightarrow H_0(G(X))$ defined at the homology level, we must construct a chain map $f_\bullet(X):F_\bullet(X)\rightarrow G_\bullet(X)$. To this end, we first define the $0$th component $f_0(X)$. Since $F_0(X)$ is free, this amounts to specifying the image of each $u:M\rightarrow X$. Now, by the following commutative diagram

{% diagram Math/Algebraic_Topology/Acyclic_Models_Theorem-1.svg width="13.49em" alt="lifting" %}

the composition $F_0(X)\rightarrow H_0(F(X))\rightarrow H_0(G(X))$ is given, and since $p_G$ is surjective we obtain a lift $F_0(X)\rightarrow G_0(X)$. However, if we choose a lift separately for each $X$, there is no guarantee that these choices are natural with respect to one another; the role of the models $\mathcal{M}$ is to resolve this. Specifically, for each model $M$ we only choose the image of the element of $F_0(M)$ corresponding to $\id_M$, that is, $f_0(M)(\id_M)$, and then for the remaining generators $u:M\rightarrow X$ we define $f_0(X)(u):=(G_0(u)\circ f_0(M))(\id_M)$. The $f_0$ defined in this way is natural by the functoriality of $G_0$, and the fact that it is still a lift of $f(X)_0$ follows from the naturality of $f(-)_0$.

However, defining $f_\bullet(X)$ in higher degrees presents an additional difficulty. Suppose inductively that the components up to $f_{n-1}(X)$ have been defined, and let us define $f_n(X)$. That is, we must define the lift in the following diagram

{% diagram Math/Algebraic_Topology/Acyclic_Models_Theorem-2.svg width="24.16em" alt="lifting_general" %}

but unlike the situation above, we must require that the newly defined $f_n(X)$ satisfy the commutativity condition

$$d_n^{G(X)}\circ f_n(X)=f_{n-1}(X)\circ d_n^{F(X)}$$

Moreover, even without this commutativity condition, it is not clear how $f_n(X)$ should be defined.

To resolve this, we use the hypothesis that $G$ is acyclic on $\mathcal{M}$. First, since the functor $F_n$ is free, we know that it suffices to define $f_n$ on the *models* $M$. For any object $X$, the free module $F_n(X)$, and a generator $u:M \rightarrow X$, the following diagram

{% diagram Math/Algebraic_Topology/Acyclic_Models_Theorem-3.svg width="11.47em" alt="reduction_to_models" %}

shows that the element of $F_n(M)$ corresponding to $\id_M$ becomes $u$ in $F_n(X)$, so we need only send $u$ to $(G_n(u)\circ f_n(M))(\id_M)$. Having shifted our attention to models, what remains is to lift the preceding diagram

{% diagram Math/Algebraic_Topology/Acyclic_Models_Theorem-4.svg width="24.72em" alt="lifting_reduced" %}

Now if $n\geq2$, then for any $x_n\in F_n(M)$,

$$0=(f_{n-2}(M)\circ d_{n-1}^{F(M)}\circ d_n^{F(M)})(x_n)=(d_{n-1}^{G(M)}\circ f_{n-1}(M)\circ d_n^{F(M)})(x_n)$$

so by the assumption that $G$ is acyclic on $\mathcal{M}$,

$$f_{n-1}(d_n^{F(M)}(x_n))\in \ker d_{n-1}^{G(M)}=\im d_n^{G(M)}$$

and thus we can find $y_n$ satisfying $d_n^{G(M)}(y_n)=f_{n-1}(d_n^{F(M)}(x_n))$, from which we obtain the $n$th component of the chain map $f_\bullet(M)$.

In the case $n=1$, for any $x_1\in F_1(M)$, the element $d_1^{F(M)}(x_1)$ is a boundary in $F(M)$ and hence vanishes in $H_0(F(M))$; since $f_0$ was chosen to lift $f(M)_0$, the class determined by $f_0(d_1^{F(M)}(x_1))$ in $H_0(G(M))$ also vanishes. That is, $f_0(d_1^{F(M)}(x_1))\in \ker p_G=\im d_1^{G(M)}$, and thus we can find $y_1$ in the same manner. Of course, the $f_\bullet$ obtained in this way depends on the choice of $y_n$ and is therefore not unique, but one can verify that the difference between two choices is absorbed by a natural chain homotopy.

## Applications of the acyclic models theorem

The acyclic models theorem is used first of all in proving [§Cohomology, ⁋Corollary 10](/en/math/algebraic_topology/cohomology#cor10). Consider the category $\Top^2$ of pairs of topological spaces, and the two functors to $\Ch_{\geq 0}(\lMod{A})$

$$C_\bullet(-\times -;A),\qquad  C_\bullet(-;A)\otimes_A C_\bullet(-;A)$$

If we take the models $\mathcal{M}$ to be the collection of

$$(\Delta^p, \Delta^q)\in\Top^2$$

then both functors are free on $\mathcal{M}$ and acyclic on $\mathcal{M}$. The natural transformation determined by sending $[\sigma]\otimes[\tau]$ to $[(\sigma,\tau)]$ for $0$-simplices $\sigma,\tau$

$$H_0(C_\bullet(X;A)\otimes_AC_\bullet(Y;A))\cong H_0(X;A)\otimes_AH_0(Y;A)\rightarrow H_0(X\times Y;A)$$

is an isomorphism because $\pi_0(X\times Y)=\pi_0(X)\times\pi_0(Y)$; its lift is the Eilenberg–Zilber map, and the lift of its inverse is the Alexander–Whitney map. However, one must be careful that at the chain level we cannot write $\sigma\times\tau$ directly. This is because the product of $\sigma:\Delta^p\rightarrow X$ and $\tau:\Delta^q\rightarrow Y$ is defined on the prism $\Delta^p\times\Delta^q$, not on $\Delta^{p+q}$, and decomposing this prism into simplices is precisely what the Eilenberg–Zilber map accomplishes.

As a similar example, consider the four functors from $\Top^2$ to $\Ch_{\geq 0}(\lMod{A})$

$$(X,Y)\mapsto C_\bullet(X\times Y;A),\quad (X,Y)\mapsto C_\bullet(Y\times X;A),\quad (X,Y)\mapsto C_\bullet(X;A)\otimes_AC_\bullet(Y;A),\quad (X,Y)\mapsto C_\bullet(Y;A)\otimes_AC_\bullet(X;A)$$

The obvious maps between them, when lifted via [Theorem 3](#thm3), yield a diagram in $\Ch_{\geq0}(\lMod{A})$ that commutes up to natural chain homotopy

{% diagram Math/Algebraic_Topology/Acyclic_Models_Theorem-5.svg width="23.79em" alt="flip_map" %}


--- 

**References**

[The method of acyclic models](https://amathew.wordpress.com/2010/09/11/the-method-of-acyclic-models/)

---
