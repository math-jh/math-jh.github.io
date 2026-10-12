---
title: "Lie Groups"
description: "A Lie group is a group on a smooth manifold whose group operations of multiplication and inversion are both smooth. Examples include vector spaces, tori, and general linear groups."
excerpt: "Definition and properties of Lie groups"

categories: [Math / Lie Theory]
permalink: /en/math/lie_theory/Lie_groups
sidebar: 
    nav: "Lie_theory-en"

date: 2023-01-23
weight: 1
translated_at: 2026-05-31T16:00:05+00:00
translation_source: kimi-cli
last_polished_at: 2026-10-12T03:15:06+00:00
translation_polish_source: antigravity-gemini-3.8-flash-high
---
In the posts in this category, we cover Lie groups and Lie algebras. The definition of a Lie group is very simple.

::: Definition 1
A group $G$ is called a *Lie group* if $G$ itself carries a manifold structure such that, with respect to this manifold structure, the following map

$$G\times G\rightarrow G;\qquad (x,y)\mapsto xy^{-1}$$

is $C^\infty$.
:::

That is, a Lie group is itself a group, and at the same time a smooth manifold equipped with a differentiable structure that makes the two operations defining this group, multiplication and inverse, smooth. More generally, we call a topological space in which the group operations are continuous a *topological group*, but such a generalization is not immediately needed.

Then a morphism between two Lie groups $G, H$ means a smooth map $f:G \rightarrow H$ that is simultaneously a group homomorphism. These data define the category $\LieGrp$, and the notion of isomorphism here is also obvious.

The following are examples of Lie groups.

::: Example 2
Any finite-dimensional $\mathbb{R}$-vector space $\mathbb{R}^n$ becomes a Lie group with addition as its operation. This is obvious because the following function

$$\mathbb{R}^n \times \mathbb{R}^n\rightarrow \mathbb{R}^n;\quad (\mathbf{x},\mathbf{y})\mapsto \mathbf{x}-\mathbf{y}$$

is smooth.
:::

::: Example 3
The $1$-torus $S^1$, when viewed as the multiplicative subgroup of $\mathbb{C}$

$$S^1=\left\{z\in \mathbb{C}: \lvert z\rvert=1\right\}$$

becomes a Lie group. More generally, since it is easy to show that for any Lie groups $G, H$, $G\times H$ is also a Lie group, any $n$-torus

$$T^n=(S^1)^n$$

is a Lie group. For example, $T^2$ behaves like a vector space with a point serving as the identity, and the great circles passing through that point in the equatorial direction and in the perpendicular direction as *axes*; this is obtained from the following isomorphism

$$\mathbb{R}/\mathbb{Z}\rightarrow S^1;\quad t\mapsto e^{2\pi i t}$$
:::

A slightly more complicated and more widely used example than the two examples above is the following.

::: Example 4
The space of arbitrary $n\times k$ matrices, $\Mat_{n\times k}(\mathbb{R})$, is an $nk$-dimensional vector space and simultaneously a smooth manifold. Now, considering specifically the space of $n\times n$ matrices, the smooth function $\det:\Mat_{n\times n}(\mathbb{R})\rightarrow \mathbb{R}$ defined on these matrices defines the following open submanifold:

$$\GL(n; \mathbb{R}) =\left\{A\in \Mat_{n\times n}(\mathbb{R})\mid \det(A)\neq 0\right\}$$

Now, on this, multiplication and inversion of matrices are well-defined; here matrix multiplication is merely a polynomial function, and inversion is merely a rational function whose denominator is not $0$. That is, $\GL(n; \mathbb{R})$ is a Lie group with multiplication as its operation, and since the original manifold $\Mat_{n\times n}(\mathbb{R})$ is $n^2$-dimensional, so is the dimension of $\GL(n; \mathbb{R})$.

Now, considering again $\det:\GL(n; \mathbb{R})\rightarrow \mathbb{R}^\times$, via the equation

$$\SL(n;\mathbb{R})=\left\{A\in \GL(n; \mathbb{R})\mid \det(A)=1\right\}$$

we can define the subset of $\GL(n;\mathbb{R})$, $\SL(n; \mathbb{R})$. This function is a polynomial in the entries of the matrix, hence smooth, and a short calculation shows that it is regular at every point. By [\[Differential Manifolds\] §Implicit Function Theorem, ⁋Corollary 4](/en/math/manifolds/implicit_function_theorem#cor4){: data-lid="g6h91" }, $\SL(n;\mathbb{R})$ becomes an $n^2-1$-dimensional manifold. Here, the multiplication and inversion of $\GL(n;\mathbb{R})$ also restrict well to $\SL(n;\mathbb{R})$, and therefore $\SL(n; \mathbb{R})$ is also a Lie group.

In a similar way, one can verify that matrix groups such as the classical matrix groups $\Omat(n)$, $\SO(n)$, $\Umat(n)$, $\SU(n)$, etc., also carry Lie group structures. More generally, through [Theorem 5](#thm5){: data-lid="tie8d" } below, one can see that any closed subgroup of $\GL(n;\mathbb{R})$ is automatically a Lie group.
:::

On the other hand, even without knowing what the determinant looks like, information about what $\SL(n;\mathbb{R})$ looks like as a group comes from linear algebra. The following theorem for an arbitrary Lie group $G$ shows more generally that any *closed* subgroup is always an embedded submanifold.

::: Theorem 5 (Cartan's closed subgroup theorem)
For a Lie group $G$ and its closed subgroup $H \subseteq G$, $H$ naturally carries the structure of an embedded smooth submanifold of $G$, and under this structure $H$ itself becomes a Lie group.
:::

## Lie Algebras

As mentioned above, the concept of a Lie group itself is quite simple. The interesting properties of Lie groups then concern how they interact. One of the simplest results is that for a Lie group, it is easy to find nontrivial diffeomorphisms from the group to itself.

::: Definition 6
For a Lie group $G$ and any element of $G$, $g\in G$, the *left translation* by $g$, $L_g$, is defined by

$$L_g:G\rightarrow G;\qquad x\mapsto gx$$

as a $C^\infty$ function. Similarly, right translation $R_g$ is defined by

$$R_g:G\rightarrow G;\qquad x\mapsto xg$$
:::

These are not Lie group homomorphisms, but they are smooth maps by definition, and their inverses are given by $L_{g^{-1}}$ and $R_{g^{-1}}$ respectively, so they are diffeomorphisms.

When we deal with a Lie group and vector fields defined on it, we are interested only in those vector fields preserved by these left translations. That is, we define the following.

::: Definition 7
For a Lie group $G$ and a vector field $X$ defined on it, that $X$ is *left invariant* means that for any $g\in G$, $X$ is $L_g$-related to itself.
:::

That is, the equation

$$\dd{(L_g)}\circ X=X\circ L_g$$

holds, and more explicitly, for any $p\in G$,

$$\left(\dd{(L_g)}\right)(X_p)=X_{gp}$$

always holds. From the above equation, we can see that to specify on $G$ a left-invariant vector field $X$, it suffices to know, at *only a single point* $p\in G$, the value $X_p$, and of course the most natural choice of $p$ is the identity element of $G$, $e$. Also, since the value of $X$ at each point is defined in this way, one can also guess that the fact that $X$ is left-invariant will yield the smoothness of $X$.

In other words, a left-invariant vector field defined on $G$ is precisely the same as the tangent space of $G$ at the identity, $T_eG$. On the other hand, in [\[Differential Manifolds\] §Lie Derivative, ⁋Definition 5](/en/math/manifolds/Lie_derivative#def5){: data-lid="vayua" }, to make $\mathfrak{X}(G)$ a Lie algebra over $\mathbb{R}$ we defined an operation $[-,-]$, so whether the collection of left-invariant vector fields forms a subalgebra under this operation is also one of our questions. First, let us consider the following definition generalizing $[-,-]$.

::: Definition 8
That an $\mathbb{R}$-vector space $\mathfrak{g}$ is a *Lie algebra* defined over $\mathbb{R}$ means that, satisfying the following two conditions:

1. (anticommutativity) $[x,y]=-[y,x]$,
2. (Jacobi identity) $[[x,y],z]+[[y,z],x]+[[z,x],y]=0$

an $\mathbb{R}$-bilinear *Lie bracket* $[-,-]:\mathfrak{g}\times\mathfrak{g}\rightarrow\mathfrak{g}$ is defined on it.
:::

Then the following proposition holds.

::: Proposition 9
Suppose a Lie group $G$ is given, and let $\mathfrak{g}$ be the collection of all left-invariant vector fields defined on $G$.

1. $\mathfrak{g}$ is an $\mathbb{R}$-vector space, and if we define $\alpha:\mathfrak{g} \rightarrow T_eG$ by the formula
    
    $$\alpha(X)=X_e$$
    
    then $\alpha$ becomes an isomorphism.
2. Any $X\in\mathfrak{g}$ is $C^\infty$.
3. For any $X,Y\in\mathfrak{g}$, the Lie bracket of $X$ and $Y$, $[X,Y]$, is also left-invariant, and therefore $\mathfrak{g}$ becomes a Lie algebra defined over $\mathbb{R}$.
:::
::: Proof
1. It is obvious that $\mathfrak{g}$ is an $\mathbb{R}$-vector space under addition and scalar multiplication of vector fields, and it is also obvious that $\alpha$ is a linear map. Now we must show that $\alpha$ is an isomorphism; since $T_eG$ is a finite-dimensional vector space, it suffices to show that $\alpha$ is bijective. First, assuming that $\alpha(X)=\alpha(Y)$ holds for two $X,Y\in\mathfrak{g}$, then for any $g\in G$,
  
    $$X_g=(\dd{L_g})_e(X_e)=(\dd{L_g})_e(Y_e)=Y_g$$

    so $X=Y$. Conversely, for any $v\in T_eG$, if we define $X_g$ by $(\dd{L_g})_e(v)$, then it is obvious that $X$ is a left-invariant vector field and satisfies $\alpha(X)=v$.
2. To show that $X\in\mathfrak{g}$ is $C^\infty$, it suffices to show that for an arbitrary function $f$, $Xf$ is $C^\infty$. ([\[Differential Manifolds\] §Vector Fields, ⁋Proposition 2](/en/math/manifolds/vector_fields#prop2){: data-lid="xu8xk" }) On the other hand, for any $p\in G$,
    
    $$(Xf)(p)=X_pf=(\dd{L_p})_e(X_e)f=X_e(f\circ L_p)$$
    
    so this is again equivalent to showing that the function $p\mapsto X_e(f\circ L_p)$ is $C^\infty$. Writing the multiplication of $G$ as $m:G\times G\rightarrow G$, denoting the two natural embeddings from $G$ to $G\times G$ by

    $$\iota_1^p: x\mapsto (x,p),\qquad \iota_2^p:x\mapsto (p,x)$$

    and choosing a vector field satisfying $Y_e=X_e$ that is $C^\infty$, let us consider the new vector field defined on $G\times G$, $(0,Y)$. Then $f\circ m$ is a $C^\infty$ function and $(0,Y)$ is a $C^\infty$ vector field, so $(0,Y)(f\circ m)$ is a $C^\infty$ function, and therefore the composition $\bigl((0,Y)(f\circ m)\bigr)\circ\iota_1^e$ is also $C^\infty$. Now, for any $p\in G$, through the isomorphism

    $$T_{(x,y)}(M\times N)\cong T_xM\oplus T_yN$$

    we have

    $$\begin{aligned}\bigl((0,Y)(f\circ m)\bigr)(\iota_1^e(p))&=(0,Y)_{(p,e)}(f\circ m)=0_p(f\circ m\circ\iota_1^e)+Y_e(f\circ m\circ\iota_2^p)\\&=X_e(f\circ m\circ\iota_2^p)=X_e(f\circ L_p)\end{aligned}$$

    so we obtain the desired result.
3. This is obvious by [\[Differential Manifolds\] §Lie Derivative, ⁋Proposition 9](/en/math/manifolds/Lie_derivative#prop9){: data-lid="zhs7c" }.
:::

The Lie algebra $\mathfrak{g}$ obtained through the above process is called the *Lie algebra of $G$*. In general, when a Lie group is written as $G$, it is customary to use the corresponding lowercase Fraktur $\mathfrak{g}$ to denote the Lie algebra of $G$.

As a special example, if for an arbitrary manifold $M$ we consider the group $\Diff(M)$ of diffeomorphisms to itself, this can be regarded as an infinite-dimensional Lie group. The tangent space of this Lie group at the identity $\id_M$ is a suitable equivalence class of curves passing through $\id_M$ in $\Diff(M)$, and considering [\[Differential Manifolds\] §Vector Fields, ⁋Theorem 6](/en/math/manifolds/vector_fields#thm6){: data-lid="aymg8" }, this information is precisely contained in $\mathfrak{X}(M)$. In this way, for a Lie group $G$, the Lie algebra $\mathfrak{g}$ defines the infinitesimal action when $G$ acts on itself.

::: Example 10
Since the previous [Example 2](#ex2){: data-lid="hqbds" }, [Example 3](#ex3){: data-lid="427al" }, and $\GL(n;\mathbb{R})$ of [Example 4](#ex4){: data-lid="be31p" } all come from vector spaces, their tangent spaces are each isomorphic to the original vector space. That is, for $\mathbb{R}^n$, its tangent space is $\mathbb{R}^n$ itself, and similarly for the $n$-torus $T^n\cong \mathbb{R}^n/\mathbb{Z}^n$, the tangent space at each point is the same as $\mathbb{R}^n$ before taking the quotient topology. For $\GL(n;\mathbb{R})$, since it is an open submanifold of the vector space $\Mat_n(\mathbb{R})$, the tangent space at each point is likewise the same as $\Mat_n(\mathbb{R})$.
:::

However, finding the Lie algebra of $\SL(n;\mathbb{R})$ requires a slightly more complicated calculation. Specifically, we need to know the differential of the determinant map $\GL(n; \mathbb{R})\rightarrow \mathbb{R}$.

## Matrix Exponential

For any finite-dimensional vector space defined over $\mathbb{R}$, the way to define a norm is topologically unique, and a norm defined this way defines a complete metric by the completeness of $\mathbb{R}$. In particular, when the operator norm is given on $\Mat_n(\mathbb{R})$, the formula

$$\lVert XY\rVert\leq\lVert X\rVert\lVert Y\rVert$$

holds, so combining these facts we can see that for any $X\in\Mat_n(\mathbb{R})$ the following *matrix exponential*

$$\exp(X)=\sum_{k=0}^\infty\frac{X^k}{k!}$$

is well defined.

The following proposition is basically a result of linear algebra and calculus.

::: Proposition 11
For any $X\in\Mat_n(\mathbb{R})$,

$$\frac{d}{\dd{t}}\exp(tX)=X\exp(tX)=\exp(tX)X$$

holds.
:::

In general, since matrix multiplication is not commutative, the formula

$$\exp(A)\exp(B)=\exp(A+B)$$

does *not* hold. However, if two matrices $A,B$ commute, then this formula holds, and in particular from the calculation

$$\exp(tX)\exp(-tX)=\exp(tX-tX)=\exp(O)=I$$

we know that $\exp(tX)$ always has an inverse matrix. That is, the following curve

$$t\mapsto \exp(tX)$$

is a curve in $\GL(n; \mathbb{R})$, and that the derivative of this curve at $t=0$ is

$$\frac{d}{\dd{t}}\exp(tX)\bigg\vert_{t=0}=X$$

is obvious by the preceding proposition. To explain this geometrically, the above curve means that when an arbitrary tangent vector at $I=\exp(O)$,

$$X\in T_I\GL(n;\mathbb{R})=\Mat_n(\mathbb{R})$$

is given, $t\mapsto \exp(tX)$ is a curve whose velocity at the point $I$ is $X$.

Now, finding the tangent vectors of $\SL(n;\mathbb{R})$ is equivalent to singling out, so that this curve stays (at least for a short time) in $\SL(n;\mathbb{R})$, those matrices $X$. For this, we can use the following proposition.

::: Proposition 12
For any $X\in\Mat_n(\mathbb{R})$, $\det(\exp X)=\exp(\tr X)$ holds.
:::

This too can be solved using elementary linear algebra. Then from

$$\det(\exp tX)=\exp(\tr(tX))=\exp(t\cdot\tr X)$$

we know that $X$ satisfying this must satisfy $\tr X=0$ exactly. That is, the tangent space of $\SL(n;\mathbb{R})$ consists of matrices satisfying $\tr X=0$, and this condition defines an $n^2-1$-dimensional vector space.

The following is a generalization of the left-invariant vector field examined above.

::: Definition 13
On a Lie group $G$, a form $\omega$ is called *left invariant* if for any $g\in G$, $L_g^\ast\omega=\omega$ holds. On $G$, the collection of left invariant $k$-forms is denoted by $\Omega_\text{l.inv}^k(G)$, and the collection of all left invariant forms on $G$ is denoted by $\Omega_\text{l.inv}^\ast(G)$.
:::

In particular, elements of $\Omega_\text{l.inv}^1(G)$ are called *Maurer-Cartan forms*.

In the same way as [Proposition 9](#prop9){: data-lid="agqg2" }, the following proposition can be proved.

::: Proposition 14
For a Lie group $G$ and $\Omega_\text{l.inv}^\ast(G)$, the following hold.

1. Any element of $\Omega_\text{l.inv}^\ast(G)$ is $C^\infty$. 
2. $\Omega_\text{l.inv}^\ast(G)$ is, within $\Omega^\ast(G)$, an $\mathbb{R}$-subalgebra, and the map $\omega\mapsto\omega_e$ from $\Omega_\text{l.inv}^\ast(G)$ to $\bigwedge(T_e^\ast G)$ is an $\mathbb{R}$-algebra isomorphism.
3. For any $\omega\in\Omega_\text{l.inv}^1(G)$ and left invariant vector field $X$, $\omega(X)$ is a constant function defined on $G$.
4. For any $\omega\in\Omega_\text{l.inv}^1(G)$ and $X,Y\in\mathfrak{g}$,
    
    $$\dd{\omega}(X,Y)=-\omega[X,Y]$$

    holds.
5. For $\mathfrak{g}$, with a basis $X_1,\ldots, X_d$ and its dual basis $\omega_1,\ldots,\omega_d$, there exist, satisfying the following formula
    
    $$[X_i,X_j]=\sum_{k=1}^d c_{ij}^kX_k$$

    $d^3$ constants $c_{ij}^k$. These satisfy the two conditions

    $$c_{ij}^k+c_{ji}^k=0,\qquad\sum_r (c_{ij}^rc_{rk}^s+c_{jk}^rc_{ri}^s+c_{ki}^rc_{rj}^s)=0\quad\text{for all $s$}$$

    and therefore the following formula

    $$\dd{\omega_i}=\sum_{j < k} c_{jk}^i\omega_k\wedge\omega_j$$

    holds.
:::

## Lie Correspondence

For any manifold, its tangent space can be thought of as germs of curves as above. Therefore, for any Lie group $G$ and its Lie algebra $\mathfrak{g}$, whenever an element of $\mathfrak{g}$ is given we can associate a curve in $G$. In this way, the Lie algebra can reveal all information about the Lie group. More precisely, to read off information about $G$ through curves in this way, the way of associating curves must be unique (up to homotopy) and must exist, so the Lie algebra contains all information about simply connected Lie groups. In this section, we shall examine this correspondence in a bit more detail, but omitting proofs.

The Lie correspondence is a collection of results concerning relationships of the following kind between Lie groups and Lie algebras.

::: Theorem 15
The following hold.

1. Let Lie groups $G,H$ be given, and between their Lie algebras $\mathfrak{g},\mathfrak{h}$, let a homomorphism $L:\mathfrak{g} \rightarrow \mathfrak{h}$ be given. If $G$ is simply connected, then satisfying $\dd{F}=L$, there uniquely exists a homomorphism $F:G \rightarrow H$.
2. For any finite-dimensional real Lie algebra $\mathfrak{g}$, there exists, with $\mathfrak{g}$ as its Lie algebra, a simply connected Lie group $G$.
:::

That is, in other words, the functor from $\LieGrp$ to $\LieAlg$, $\Lie:\LieGrp \rightarrow \LieAlg$, gives an equivalence of the two categories when restricted to the full subcategory of $\LieGrp$ consisting of simply connected Lie groups.

Aside from category-theoretic results, this theorem allows us, for example, to define an exponential map similar to the matrix exponential for any Lie group $G$ and its Lie algebra $\mathfrak{g}$. This is because $(\mathbb{R},+)$ is a 1-dimensional simply connected Lie group, so its Lie algebra is also 1-dimensional, and thus a Lie algebra homomorphism from here to another Lie algebra is uniquely determined by where the basis $d/\dd{t}$ goes; if $d/\dd{t}$ is sent to $X\in \mathfrak{g}$, applying [Theorem 15](#thm15){: data-lid="n81nj" } to this Lie algebra homomorphism yields the Lie group homomorphism $\gamma: \mathbb{R}\rightarrow G$ that defines the desired curve.

::: Definition 16
For any Lie group $G$ and its Lie algebra $\mathfrak{g}$, and an element $X\in \mathfrak{g}$, let us denote the curve obtained through the above process by $\gamma_X$. Then we define $\exp:\mathfrak{g}\rightarrow G$ by $X\mapsto \gamma_X(1)$.
:::

In particular, when $G$ is a matrix Lie group as examined above, we can verify that this definition gives the matrix exponential.

Intuitively, the Lie algebra reads off information about the Lie group using the exponential. For this to be said to know information about the Lie group, we must be able to recover information about the group operation of the Lie group at least locally. This is obtained from the following result.

::: Theorem 17 (Baker-Campbell-Hausdorff)
For a Lie group $G$, its Lie algebra $\mathfrak{g}$, and $X,Y\in \mathfrak{g}$, the formula

$$\exp(X)\exp(Y)=\exp\left(X+Y+\frac{1}{2}[X,Y]+\frac{1}{12}[X,[X,Y]]+\frac{1}{12}[Y,[Y,X]]+\cdots\right)$$

holds.
:::

Strictly speaking, the above "theorem" lacks information about the coefficients of the terms corresponding to $\cdots$, but these coefficients are rarely needed concretely. What is important is that when two elements (of the Lie group) in the directions specified by the Lie algebra elements $X,Y$ are multiplied, their product is in the direction corresponding to a linear combination of $X,Y$ and the sum of their Lie brackets, and if $X,Y$ are sufficiently small vectors, this series also converges. On the other hand, in a Lie group $G$, any element near the identity $e$ can be written in the form $g=\exp(X)$, so this theorem contains precisely all information about the group operation of $G$ (near the identity). More concretely, we can view the Lie algebra $\mathfrak{g}$ as a manifold and think of $\exp: \mathfrak{g}\rightarrow G$ as a smooth map between manifolds, where the differential at $0\in \mathfrak{g}$ is precisely $\id_\mathfrak{g}$. Therefore, in $\mathfrak{g}$, there exists a suitable neighborhood of $0$, $U$, such that $\exp$ defines a diffeomorphism between $U$ and $\exp(U)$ (in particular, the inverse $\log$ of the local diffeomorphism exists), but we cannot assert how the exponential map behaves outside this $U$.

Upon learning [Theorem 15](#thm15){: data-lid="e1oh4" } above, one natural question would be whether, given a Lie group $G$, its Lie algebra $\mathfrak{g}$, and a Lie subalgebra of $\mathfrak{g}$, $\mathfrak{h}$, there exists, with $\mathfrak{h}$ as its tangent space at the identity, a Lie subgroup of $G$, $H$. However, by definition a Lie subalgebra is closed under the Lie bracket, so by [\[Differential Manifolds\] §Distribution, ⁋Theorem 3](/en/math/manifolds/distribution#thm3){: data-lid="nl83g" } this defines a submanifold of $G$. This will also have a group operation by [Theorem 17](#thm17){: data-lid="sqt1y" } above, but the problem is that, as pointed out earlier, this theorem is effective only in a local region. However, if $G$ were simply connected, there would be no topological obstacle to extending this to all of $G$, so the following theorem holds.

::: Theorem 18
Given a simply connected Lie group $G$, its Lie algebra $\mathfrak{g}$, and a Lie subalgebra of $\mathfrak{g}$, $\mathfrak{h}$, there exists, with $\mathfrak{h}$ as its Lie algebra, a Lie subgroup of $G$, $H$.
:::

## Classification of Abelian Lie Groups

Finally, we now carry out the classification of abelian Lie groups. By definition, an abelian Lie group is one whose group operation is commutative. Now consider the inner automorphism

$$\rho_g: G \rightarrow G; \quad h\mapsto \rho_g(h)=ghg^{-1}$$

([\[Algebraic Structures\] §Group Action, ⁋Proposition 9](/en/math/algebraic_structures/group_actions#prop9){: data-lid="tnvix" }). This is a Lie group automorphism, and therefore differentiating it at the identity $h=e$ gives $\dd{\rho_g}: \mathfrak{g}\rightarrow \mathfrak{g}$, which is a Lie algebra automorphism.

::: Definition 19
For a Lie group $G$, the correspondence

$$\Ad:G\rightarrow \Aut(\mathfrak{g});\quad g\mapsto \dd{\rho_g}$$

is called the *adjoint representation* of $G$. The map

$$\ad: \mathfrak{g}\rightarrow \Lie(\Aut(\mathfrak{g}))$$

obtained by differentiating this is called the *adjoint representation* of $\mathfrak{g}$.
:::

Then, since the flow of a left-invariant vector field $X$ is given by the right translation $R_{\exp(tX)}$, within a sufficiently small range the adjoint representation of $G$ is exactly the same as looking at the Lie derivative, and therefore by [\[Differential Manifolds\] §Lie Derivative, ⁋Proposition 4](/en/math/manifolds/Lie_derivative#prop4){: data-lid="1jly4" } the formula

$$\ad(X)Y =[X,Y]$$

holds. Moreover, the following holds.

::: Theorem 20
For a connected compact Lie group $G$, the following hold.

1. $\dd{\exp}_0=\id_\mathfrak{g}$
2. $\Ad\circ\exp=\exp_{\GL(\mathfrak{g})}\circ \ad$
3. $\rho_x\circ\exp=\exp\circ\Ad(x)$
:::

If $G$ were an abelian group, then $\rho_g$ would simply be the identity map, and therefore $\Ad_g(X)=X$ would hold for any $g\in G$ and any $X\in \mathfrak{g}$, and thus the adjoint representation of $\mathfrak{g}$, being its differential, would be $0$. That is, for any abelian Lie group, the Lie bracket of its Lie algebra is always $0$, and we call this an *abelian* Lie algebra. This is not an awkward name because by [Definition 8](#def8){: data-lid="teexh" } this is the only way for an anticommutative Lie bracket to also be commutative.

Then, when $G$ is abelian, in particular by [Theorem 17](#thm17){: data-lid="d6029" } we have $\exp(X+Y)=\exp(X)\exp(Y)$. That is, $\exp$ is a group homomorphism. Moreover, in this case the expression inside $\exp$ on the right-hand side of [Theorem 17](#thm17){: data-lid="ocmgz" } necessarily converges, and this results in $\exp$ being a *surjective* group homomorphism (when $G$ is connected). Therefore, by the first isomorphism theorem,

$$G\cong \mathfrak{g}/\ker(\exp)$$

Now $\mathfrak{g}$ is an $n$-dimensional $\mathbb{R}$-vector space, and since $\exp$ is a local diffeomorphism, $\ker(\exp)$ becomes a *discrete* additive subgroup. It is well known that this is $\mathbb{Z}^k$, and therefore

$$G\cong \mathfrak{g}/\ker(\exp)\cong \mathbb{R}^n/\mathbb{Z}^k\cong T^k\times \mathbb{R}^{n-k}$$

That is, a connected abelian Lie group is necessarily a product of a torus and $\mathbb{R}^{n-k}$, and in particular a compact connected abelian Lie group is necessarily a torus.

---

**References**

**[War]** Frank W. Warner. *Foundations of Differentiable Manifolds and Lie Groups*, Graduate texts in mathematics, Springer, 2013  

---
