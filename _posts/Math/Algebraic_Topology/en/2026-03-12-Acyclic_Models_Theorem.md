---
title: "Acyclic Models Theorem"
description: "We prove the acyclic models theorem, which guarantees the existence of natural transformations between functors satisfying acyclic and free conditions on a collection. As corollaries of this theorem, we derive existing results in cohomology theory."
excerpt: "Acyclic models theorem on a category with models and its applications"

categories: [Math / Algebraic Topology]
permalink: /en/math/algebraic_topology/acyclic_models_theorem
sidebar: 
    nav: "algebraic_topology-en"

date: 2025-09-17
weight: 10
translated_at: 2026-08-18T15:45:04+00:00
translation_source: kimi-cli
last_polished_at: 2026-09-21T19:15:04+00:00
translation_polish_source: antigravity-gemini-3.8-flash-high
---
As mentioned in [§Cohomology](/en/math/algebraic_topology/cohomology){: data-lid="i1fc7" data-relation="weak" }, the acyclic models theorem extends the original proof of [§Cohomology, ⁋Theorem 9](/en/math/algebraic_topology/cohomology#thm9){: data-lid="owu2o" data-relation="weak" } in a general way, and can be used not only to prove [§Cohomology, ⁋Theorem 9](/en/math/algebraic_topology/cohomology#thm9){: data-lid="s3j5w" data-relation="weak" } but also in various situations. In this post, we prove the acyclic models theorem and introduce several corollaries, including the proof of [§Cohomology, ⁋Theorem 9](/en/math/algebraic_topology/cohomology#thm9){: data-lid="e0tjj" data-relation="weak" }.

## Category with models

When developing homology theory, we usually work with $n$-simplices, which help us examine arbitrary objects of $\Top$. We can formulate this into a definition as follows.

::: Definition 1
A *category with models* means a pair consisting of a category $\mathcal{A}$ and a collection of objects of $\mathcal{A}$ denoted $\mathcal{M}$, written $(\mathcal{A},\mathcal{M})$. Here, we call the objects belonging to $\mathcal{M}$ *models*.
:::

This definition has little substance on its own. We now define the following.

::: Definition 2
Let $(\mathcal{A},\mathcal{M})$ be a category with models, and let $F_\bullet:\mathcal{A}\rightarrow \Ch_{\geq0}(\lMod{A})$ be a covariant functor.

1. The functor $F_\bullet$ is *acyclic on $\mathcal{M}$* if for each $M\in\mathcal{M}$, we have $H_i(F(M))=0$ for all $i>0$.
2. The functor $F_\bullet$ is *free on $\mathcal{M}$* if for each $n$ there exists a family of models $(M_j)_{j\in J_n}$ such that the natural isomorphism
    
    $$F_n(-)\cong \bigoplus_{j\in J_n}A[\Hom_\mathcal{A}(M_j,-)]$$

    holds. Here $A[S]$ denotes the free $A$-module with basis the set $S$, and each family $(M_j)_{j\in J_n}$ may contain the same model multiple times.
:::

For example, with the standard $n$-simplices $\Delta^n$ forming the collection $\mathcal{M}$ of models, consider the category with models $(\Top, \mathcal{M})$. Then, assigning to each $X\in \Top$ the chain complex of singular $n$-simplices $C_\bullet(X)$, the functor $C_\bullet:\Top \rightarrow \Ch_{\geq0}(\Ab)$ is both acyclic on $\mathcal{M}$ and free on $\mathcal{M}$.

- That $C_\bullet$ is acyclic on $\mathcal{M}$ follows because each model $\Delta^n$ is a convex set and hence contractible to a point, and the cone operator induced by that straight-line contraction directly contracts $C_\bullet(\Delta^n)$ for $i>0$; this can be viewed as a generalization of [§Homology, ⁋Proposition 11](/en/math/algebraic_topology/homology#prop11){: data-lid="cabl2" data-relation="weak" }. Note that the condition that the functor $F_\bullet$ is acyclic on $\mathcal{M}$ does *not require* that for $F_\bullet(X)$, the $0$th homology be $0$.
- That $C_\bullet$ is free on $\mathcal{M}$ follows because each $C_n(X)$ is the free abelian group with basis precisely the singular $n$-simplices $\Delta^n \rightarrow X$, that is, $C_n(X)=\mathbb{Z}[\Hom_\Top(\Delta^n,X)]$. In this case, the family of models taken for each $n$ consists of the single model $\Delta^n$.

## Acyclic models theorem

The main theorem of this post is the following.

::: Theorem 3 (Acyclic models theorem)
Let $(\mathcal{A},\mathcal{M})$ be a category with models, and let $F_\bullet, G_\bullet:\mathcal{A}\rightarrow \Ch_{\geq0}(\lMod{A})$ be two functors such that $F_\bullet$ is free on $\mathcal{M}$ and $G_\bullet$ is acyclic on $\mathcal{M}$. Then, for the two functors

$$H_0(F(-)),H_0(G(-)): \mathcal{A}\rightarrow \lMod{A}$$

whenever any natural transformation between them

$$f(-)_0:H_0(F(-)) \Rightarrow H_0(G(-))$$

is given, there exists a suitable natural transformation

$$f_\bullet(-):F_\bullet(-) \rightarrow G_\bullet(-)$$

such that $H_0(f)=f(-)_0$, and such a natural transformation $f$ is unique up to natural chain homotopy.
:::

That is, starting from $f(X)_0: H_0(F(X))\rightarrow H_0(G(X))$ defined at the homology level, we must construct a chain map $f_\bullet(X):F_\bullet(X)\rightarrow G_\bullet(X)$. To this end, for $f_\bullet(X)$, let us first define its $0$th component $f_0(X)$. Since $F_0(X)$ is free, this is equivalent to defining where each $u:M\rightarrow X$ is sent. Meanwhile, by the following commutative diagram

{% diagram Math/Algebraic_Topology/Acyclic_Models_Theorem-1.svg width="13.49em" alt="lifting" %}

the composite $F_0(X)\rightarrow H_0(F(X))\rightarrow H_0(G(X))$ is given, and since $p_G$ is surjective, we obtain a lifting $F_0(X)\rightarrow G_0(X)$ from this. However, if we choose a lifting separately for each $X$, there is no guarantee that these satisfy naturality with each other, and resolving this is the role of the models $\mathcal{M}$. That is, for each model $M$, we choose only where the element corresponding to $\id_M$ in $F_0(M)$ is sent, namely $f_0(M)(\id_M)$, and then for the remaining generators $u:M\rightarrow X$, we define $f_0(X)(u):=(G_0(u)\circ f_0(M))(\id_M)$. The $f_0$ defined in this way is natural from the functoriality of $G_0$, and that this is still a lift of $f(X)_0$ follows from the naturality of $f(-)_0$.

However, to define $f_\bullet(X)$ in higher degrees, there is a slight problem. Suppose inductively that the components up to $f_{n-1}(X)$ have been defined, and let us define $f_n(X)$. That is, we must define a lifting of the following diagram

{% diagram Math/Algebraic_Topology/Acyclic_Models_Theorem-2.svg width="24.16em" alt="lifting_general" %}

but unlike the situation above, we must require that the newly defined $f_n(X)$ satisfy the following commutativity condition

$$d_n^{G(X)}\circ f_n(X)=f_{n-1}(X)\circ d_n^{F(X)}$$

Moreover, it is not clear how $f_n(X)$ should be defined (even without the commutativity condition above).

To resolve this, we use the condition that $G$ is acyclic on $\mathcal{M}$. First, from the fact that the functor $F_n$ is free, we know that it suffices to define $f_n$ only on the *models* $M$. This is because, for any object $X$, free module $F_n(X)$, and generator $u:M \rightarrow X$, if we use the following diagram

{% diagram Math/Algebraic_Topology/Acyclic_Models_Theorem-3.svg width="11.47em" alt="reduction_to_models" %}

the element corresponding to $\id_M$ in $F_n(M)$ becomes $u$ in $F_n(X)$, and we need only send $u$ to $(G_n(u)\circ f_n(M))(\id_M)$. Now, once we shift our focus to the models, what we must do is lift the previous diagram

{% diagram Math/Algebraic_Topology/Acyclic_Models_Theorem-4.svg width="24.72em" alt="lifting_reduced" %}

Now if $n\geq2$, then for any $x_n\in F_n(M)$,

$$0=(f_{n-2}(M)\circ d_{n-1}^{F(M)}\circ d_n^{F(M)})(x_n)=(d_{n-1}^{G(M)}\circ f_{n-1}(M)\circ d_n^{F(M)})(x_n)$$

so from the assumption that $G$ is acyclic on $\mathcal{M}$,

$$f_{n-1}(d_n^{F(M)}(x_n))\in \ker d_{n-1}^{G(M)}=\im d_n^{G(M)}$$

and therefore, we can find, satisfying $d_n^{G(M)}(y_n)=f_{n-1}(d_n^{F(M)}(x_n))$, a $y_n$, from which we can construct for the chain map $f_\bullet(M)$ its $n$th component.

In the case of $n=1$, for any $x_1\in F_1(M)$, since $d_1^{F(M)}(x_1)$ is a boundary in $F(M)$, its class in $H_0(F(M))$ is $0$, and since $f_0$ was chosen to lift $f(M)_0$, the class determined by $f_0(d_1^{F(M)}(x_1))$ in $H_0(G(M))$ is also $0$. That is, $f_0(d_1^{F(M)}(x_1))\in \ker p_G=\im d_1^{G(M)}$, and thus we can find $y_1$ in the same manner. Of course, the $f_\bullet$ obtained in this way depends on the choice of $y_n$ and is therefore not unique, but one can verify that the difference between two choices is absorbed by a natural chain homotopy.

## Applications of the acyclic models theorem

The acyclic models theorem is used first of all in proving [§Cohomology, ⁋Corollary 10](/en/math/algebraic_topology/cohomology#cor10){: data-lid="nwwkc" data-relation="weak" }. Consider the category $\Top^2$ consisting of pairs of topological spaces, and consider the two functors from this category to $\Ch_{\geq 0}(\lMod{A})$

$$C_\bullet(-\times -;A),\qquad  C_\bullet(-;A)\otimes_A C_\bullet(-;A)$$

Now, if we take the models $\mathcal{M}$ to be the collection of

$$(\Delta^p, \Delta^q)\in\Top^2$$

they are all free on $\mathcal{M}$ and acyclic on $\mathcal{M}$. Now, for $0$-simplices $\sigma,\tau$, the natural transformation determined by the assignment sending $[\sigma]\otimes[\tau]$ to $[(\sigma,\tau)]$

$$H_0(C_\bullet(X;A)\otimes_AC_\bullet(Y;A))\cong H_0(X;A)\otimes_AH_0(Y;A)\rightarrow H_0(X\times Y;A)$$

is an isomorphism since $\pi_0(X\times Y)=\pi_0(X)\times\pi_0(Y)$, and then a lifting of this becomes the Eilenberg-Zilber map, and a lifting of its inverse becomes the Alexander-Whitney map. However, one should note that at the chain level, we cannot write $\sigma\times\tau$ directly. This is because the product of $\sigma:\Delta^p\rightarrow X$ and $\tau:\Delta^q\rightarrow Y$ is defined on the prism $\Delta^p\times\Delta^q$, not on $\Delta^{p+q}$, and decomposing this prism into simplices is precisely what the Eilenberg-Zilber map does.

As a similar example, if we consider the four functors from $\Top^2$ to $\Ch_{\geq 0}(\lMod{A})$

$$(X,Y)\mapsto C_\bullet(X\times Y;A),\quad (X,Y)\mapsto C_\bullet(Y\times X;A),\quad (X,Y)\mapsto C_\bullet(X;A)\otimes_AC_\bullet(Y;A),\quad (X,Y)\mapsto C_\bullet(Y;A)\otimes_AC_\bullet(X;A)$$

we can consider the obvious maps between them, and lifting these using [Theorem 3](#thm3){: data-lid="mm53x" data-relation="required" } yields a diagram in $\Ch_{\geq0}(\lMod{A})$

{% diagram Math/Algebraic_Topology/Acyclic_Models_Theorem-5.svg width="23.79em" alt="flip_map" %}

that commutes up to natural chain homotopy.


--- 

**References**

[The method of acyclic models](https://amathew.wordpress.com/2010/09/11/the-method-of-acyclic-models/)

---
