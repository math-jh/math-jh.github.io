---
title: "Lie Groups"
excerpt: "Definition and properties of Lie groups"

categories: [Math / Lie Theory]
permalink: /en/math/lie_theory/Lie_groups
header:
    overlay_image: /assets/images/Math/Lie_Theory/Lie_Groups.png
    overlay_filter: 0.5
sidebar: 
    nav: "Lie_theory-en"

date: 2023-01-23
last_modified_at: 2025-11-06
weight: 1
translated_at: 2026-05-28T11:36:15+00:00
translation_source: kimi-cli
---
In this category of posts, we cover Lie groups and Lie algebras. The definition of a Lie group is very simple.

<div class="definition" markdown="1">

<ins id="def1">**Definition 1**</ins> A group $$G$$ is called a *Lie group* if $$G$$ itself carries a manifold structure such that, with respect to this manifold structure, the map

$$G\times G\rightarrow G;\qquad (x,y)\mapsto xy^{-1}$$

is $$C^\infty$$.

</div>

That is, a Lie group is itself a group, and at the same time a smooth manifold equipped with a differentiable structure that makes the two operations defining the group—multiplication and inversion—smooth. More generally, a topological space in which the group operations are continuous is called a *topological group*, but we do not need this generalization right now.

A morphism between two Lie groups $$G, H$$ is then a smooth map $$f:G \rightarrow H$$ that is simultaneously a group homomorphism. These data define the category $$\LieGrp$$, and the notion of isomorphism here is obvious.

Here are some examples of Lie groups.

<div class="example" markdown="1">

<ins id="ex2">**Example 2**</ins> Any finite-dimensional $$\mathbb{R}$$-vector space $$\mathbb{R}^n$$ becomes a Lie group under addition. This is obvious because the map

$$\mathbb{R}^n \times \mathbb{R}^n\rightarrow \mathbb{R}^n;\quad (\mathbf{x},\mathbf{y})\mapsto \mathbf{x}-\mathbf{y}$$

is smooth.

</div>

<div class="example" markdown="1">

<ins id="ex3">**Example 3**</ins> The $$1$$-torus $$S^1$$ becomes a Lie group when viewed as the multiplicative subgroup of $$\mathbb{C}$$

$$S^1=\left\{z\in \mathbb{C}\mid \lvert z\rvert=1\right\}$$

More generally, for any Lie groups $$G, H$$, the product $$G\times H$$ is also easily seen to be a Lie group, so any $$n$$-torus

$$T^n=(S^1)^n$$

is a Lie group. For example, $$T^2$$ behaves like a vector space with one point serving as the identity and the great circles passing through that point in the equatorial direction and in the perpendicular direction as *axes*, which arises from the isomorphism

$$\mathbb{R}/\mathbb{Z}\rightarrow S^1;\quad t\mapsto e^{2\pi i t}$$

</div>

A slightly more complicated and widely used example than the two above is the following.

<div class="example" markdown="1">

<ins id="ex4">**Example 4**</ins> The space $$\Mat_{n\times k}(\mathbb{R})$$ of arbitrary $$n\times k$$ matrices is an $$nk$$-dimensional vector space and at the same time a smooth manifold. Now, considering specifically the space of $$n\times n$$ matrices, the smooth function $$\det:\Mat_{n\times n}(\mathbb{R})\rightarrow \mathbb{R}$$ defined on these matrices determines the following open submanifold:

$$\GL(n; \mathbb{R}) =\left\{A\in \Mat_{n\times n}(\mathbb{R})\mid \det(A)\neq 0\right\}$$

On this, matrix multiplication and inversion are well defined; matrix multiplication is merely a polynomial function, and inversion is merely a rational function whose denominator does not vanish. That is, $$\GL(n; \mathbb{R})$$ is a Lie group under multiplication, and since the original manifold $$\Mat_{n\times n}(\mathbb{R})$$ is $$n^2$$-dimensional, so is $$\GL(n; \mathbb{R})$$.

Now, considering again $$\det:\GL(n; \mathbb{R})\rightarrow \mathbb{R}^\times$$, we can define the subset $$\SL(n; \mathbb{R})$$ of $$\GL(n;\mathbb{R})$$ through the formula

$$\SL(n;\mathbb{R})=\left\{A\in \GL(n; \mathbb{R})\mid \det(A)=1\right\}$$

This function is a polynomial in the entries of the matrix, hence smooth, and a short calculation shows that it is regular at every point. From [[Differential Manifolds] §Implicit Function Theorem, ⁋Corollary 4](/en/math/manifold/implicit_function_theorem#cor4), $$\SL(n;\mathbb{R})$$ becomes an $$n^2-1$$-dimensional manifold. The multiplication and inversion of $$\GL(n;\mathbb{R})$$ also restrict well to $$\SL(n;\mathbb{R})$$, and therefore $$\SL(n; \mathbb{R})$$ is also a Lie group.

In a similar way, one can verify that classical matrix groups such as $$\Omat(n)$$, $$\SO(n)$$, $$\Umat(n)$$, $$\SU(n)$$, etc., also carry Lie group structures. More generally, [Theorem 5](#thm5) below shows that any closed subgroup of $$\GL(n;\mathbb{R})$$ is automatically a Lie group.

</div>

On the other hand, even without knowing what the determinant looks like, information about what $$\SL(n;\mathbb{R})$$ looks like as a group comes from linear algebra. The following theorem for an arbitrary Lie group $$G$$ shows more generally that any *closed* subgroup is always an embedded submanifold.

<div class="proposition" markdown="1">

<ins id="thm5">**Theorem 5 (Cartan's closed subgroup theorem)**</ins> For a Lie group $$G$$ and a closed subgroup $$H \subseteq G$$, $$H$$ naturally carries the structure of an embedded smooth submanifold of $$G$$, and with this structure $$H$$ itself becomes a Lie group.

</div>

## Lie Algebras

As mentioned above, the concept of a Lie group itself is quite simple. Then the interesting properties of Lie groups concern how they interact with each other. One of the simplest results is that for a Lie group, it is easy to find nontrivial diffeomorphisms from the group to itself.

<div class="definition" markdown="1">

<ins id="def6">**Definition 6**</ins> For a Lie group $$G$$ and any element $$g\in G$$, the *left translation* $$L_g$$ by $$g$$ is the $$C^\infty$$ map defined by

$$L_g:G\rightarrow G;\qquad x\mapsto gx$$

Similarly, the right translation $$R_g$$ is defined by

$$R_g:G\rightarrow G;\qquad x\mapsto xg$$

</div>

These are not Lie group homomorphisms, but they are smooth maps by definition, and their inverses are given by $$L_{g^{-1}}$$ and $$R_{g^{-1}}$$ respectively, so they are diffeomorphisms.

When we deal with a Lie group and vector fields defined on it, we are interested only in those vector fields preserved by these left translations. That is, we define the following.

<div class="definition" markdown="1">

<ins id="def7">**Definition 7**</ins> A vector field $$X$$ defined on a Lie group $$G$$ is called *left invariant* if $$X$$ is $$L_g$$-related to itself.

</div>

That is, the equation

$$d(L_g)\circ X=X\circ L_g$$

holds, or more explicitly, for any $$p\in G$$,

$$\left(d(L_g)\right)(X_p)=X_{gp}$$

always holds. From the above equation, we can see that to specify a left invariant vector field $$X$$ defined on $$G$$, it suffices to know its value $$X_p$$ at *only a single point* $$p\in G$$, and of course the most natural choice of $$p$$ is the identity element $$e$$ of $$G$$. Also, since the values of $$X$$ at each point are defined in this way, one can guess that the fact that $$X$$ is left-invariant does not reduce its smoothness.

In other words, left-invariant vector fields defined on $$G$$ are exactly the same as the tangent space $$T_eG$$ at the identity of $$G$$. On the other hand, in [[Differential Manifolds] §Lie Derivative, ⁋Definition 5](/en/math/manifold/Lie_derivative#def5) we defined an operation $$[-,-]$$ that makes $$\mathfrak{X}(G)$$ a $$C^\infty(G)$$-algebra, so one of our questions is whether the collection of left-invariant vector fields forms a subalgebra under this operation. Let us first consider the following definition generalizing $$[-,-]$$.

<div class="definition" markdown="1">

<ins id="def8">**Definition 8**</ins> An $$\mathbb{R}$$-vector space $$\mathfrak{g}$$ is called a *Lie algebra* over $$\mathbb{R}$$ if a *Lie bracket* $$[-,-]:\mathfrak{g}\times\mathfrak{g}\rightarrow\mathfrak{g}$$ is defined on it satisfying the following two conditions:

1. (anticommutativity) $$[x,y]=-[y,x]$$,
2. (Jacobi identity) $$[[x,y],z]+[[y,z],x]+[[z,x],y]=0$$

</div>

Then the following proposition holds.

<div class="proposition" markdown="1">

<ins id="prop9">**Proposition 9**</ins> Let a Lie group $$G$$ be given, and let $$\mathfrak{g}$$ be the collection of all left invariant vector fields defined on $$G$$.

1. $$\mathfrak{g}$$ is an $$\mathbb{R}$$-vector space, and defining $$\alpha:\mathfrak{g} \rightarrow T_eG$$ by the formula
    
    $$\alpha(X)=X_e$$
    
    makes $$\alpha$$ an isomorphism.
2. Any $$X\in\mathfrak{g}$$ is $$C^\infty$$.
3. For any $$X,Y\in\mathfrak{g}$$, the Lie bracket $$[X,Y]$$ of $$X$$ and $$Y$$ is also left-invariant, and therefore $$\mathfrak{g}$$ becomes a Lie algebra over $$\mathbb{R}$$.

</div>
<details class="proof" markdown="1">
<summary>Proof</summary>

1. That $$\mathfrak{g}$$ is an $$\mathbb{R}$$-vector space under addition and scalar multiplication of vector fields is obvious, and that $$\alpha$$ is a linear map is also obvious. Now we must show that $$\alpha$$ is an isomorphism; since $$T_eG$$ is a finite-dimensional vector space, it suffices to show that $$\alpha$$ is bijective. First, assuming that there exist two $$X,Y\in\mathfrak{g}$$ satisfying $$\alpha(X)=\alpha(Y)$$, then for any $$g\in G$$,
  
    $$X_g=(dL_g)_e(X_e)=(dL_g)_e(Y_e)=Y_g$$

    so $$X=Y$$. Conversely, for any $$v\in T_eG$$, defining $$X_g$$ as $$(dL_g)_e(v)$$ gives a left invariant vector field $$X$$, and it is obvious that $$\alpha(X)=v$$.
2. To show that $$X\in\mathfrak{g}$$ is $$C^\infty$$, it suffices to show that $$Xf$$ is $$C^\infty$$ for an arbitrary function $$f$$. ([[Differential Manifolds] §Vector Fields, ⁋Proposition 2](/en/math/manifold/vector_fields#prop2)) On the other hand, for any $$p\in G$$,
    
    $$(Xf)(p)=X_pf=(dL_p)_e(X_e)f=X_e(f\circ L_p)$$
    
    so this is again the problem of showing that the map $$p\mapsto X_e(f\circ L_p)$$ is $$C^\infty$$. Writing the multiplication of $$G$$ as $$m:G\times G\rightarrow G$$, and denoting the two natural embeddings from $$G$$ to $$G\times G$$ by

    $$\iota_1^p: x\mapsto (x,p),\qquad \iota_2^p:x\mapsto (p,x)$$

    choose a $$C^\infty$$ vector field $$Y_e=X_e$$ and consider the new vector field $$(0,Y)$$ defined on $$G\times G$$. Then $$f\circ m$$ is a $$C^\infty$$ function and $$(0,Y)$$ is a $$C^\infty$$ vector field, so $$(0,Y)(f\circ m)$$ is a $$C^\infty$$ function, and therefore the composition $$\bigl((0,Y)(f\circ m)\bigr)\circ\iota_1^e$$ is also $$C^\infty$$. However, for any $$p\in G$$, through the isomorphism

    $$T_{(x,y)}(M\times N)\cong T_xM\oplus T_yN$$

    we have

    $$\begin{aligned}\bigl((0,Y)(f\circ m)\bigr)(\iota_1^e(p))&=(0,Y)_{(p,e)}(f\circ m)=0_p(f\circ m\circ\iota_1^e)+Y_e(f\circ m\circ\iota_2^p)\\&=X_e(f\circ m\circ\iota_2^p)=X_e(f\circ L_p)\end{aligned}$$

    so we obtain the desired result.
3. This is obvious by [[Differential Manifolds] §Lie Derivative, ⁋Proposition 9](/en/math/manifold/Lie_derivative#prop9).

</details>

The Lie algebra $$\mathfrak{g}$$ obtained through the above process is called the *Lie algebra of $$G$$*. In general, when a Lie group is written as $$G$$, it is customary to denote its Lie algebra by the corresponding Fraktur lowercase $$\mathfrak{g}$$.

As a special example, consider the group $$\Diff(M)$$ of diffeomorphisms from a manifold $$M$$ to itself; this can be thought of as an infinite-dimensional Lie group. The tangent space at the identity $$\id_M$$ of this Lie group is a suitable equivalence class of curves in $$\Diff(M)$$ passing through $$\id_M$$, and thinking of [[Differential Manifolds] §Vector Fields, ⁋Theorem 6](/en/math/manifold/vector_fields#thm6), this information is exactly contained in $$\mathfrak{X}(M)$$. In this way, the Lie algebra $$\mathfrak{g}$$ of a Lie group $$G$$ defines the infinitesimal action when $$G$$ acts on itself.

<div class="example" markdown="1">

<ins id="ex10">**Example 10**</ins> In the cases of [Example 2](#ex2), [Example 3](#ex3), and $$\GL(n;\mathbb{R})$$ from [Example 4](#ex4), all come from vector spaces, so their tangent spaces are isomorphic to the original vector spaces respectively. That is, for $$\mathbb{R}^n$$ its tangent space is $$\mathbb{R}^n$$ itself, and similarly for the $$n$$-torus $$T^n\cong \mathbb{R}^n/\mathbb{Z}^n$$, the tangent space at each point is the same as $$\mathbb{R}^n$$ before taking the quotient topology. For $$\GL(n;\mathbb{R})$$, since it is an open submanifold of the vector space $$\Mat_n(\mathbb{R})$$, likewise the tangent space at each point is the same as $$\Mat_n(\mathbb{R})$$.

</div>

However, to find the Lie algebra of $$\SL(n;\mathbb{R})$$ requires a slightly more complicated calculation. Specifically, we need to know the differential of the determinant map $$\GL(n; \mathbb{R})\rightarrow \mathbb{R}$$.

## Matrix Exponential

For any finite-dimensional vector space over $$\mathbb{R}$$, the way to define a norm is topologically unique, and the norm thus defined gives a complete metric by the completeness of $$\mathbb{R}$$. In particular, when the operator norm is given on $$\Mat_n(\mathbb{R})$$, the formula

$$\lVert XY\rVert\leq\lVert X\rVert\lVert Y\rVert$$

holds, so combining these facts we can see that for any $$X\in\Mat_n(\mathbb{R})$$ the following *matrix exponential*

$$\exp(X)=\sum_{k=0}^\infty\frac{X^k}{k!}$$

is well defined.

The following proposition is basically a result of linear algebra and calculus.

<div class="proposition" markdown="1">

<ins id="prop11">**Proposition 11**</ins> For any $$X\in\Mat_n(\mathbb{R})$$,

$$\frac{d}{dt}\exp(tX)=X\exp(tX)=\exp(tX)X$$

holds.

</div>

In general, since matrix multiplication is not commutative, the formula

$$\exp(A)\exp(B)=\exp(A+B)$$

does *not* hold. However, if two matrices $$A,B$$ commute then this formula holds, and in particular from the calculation

$$\exp(tX)\exp(-tX)=\exp(tX-tX)=\exp(O)=I$$

we know that $$\exp(tX)$$ always has an inverse matrix. That is, the curve

$$t\mapsto \exp(tX)$$

is a curve in $$\GL(n; \mathbb{R})$$, and the derivative of this curve at $$t=0$$ is

$$\frac{d}{dt}\exp(tX)\bigg\vert_{t=0}=X$$

which is obvious from the preceding proposition. To explain this geometrically, the above curve means that when an arbitrary tangent vector

$$X\in T_I\GL(n;\mathbb{R})=\Mat_n(\mathbb{R})$$

at $$I=\exp(O)$$ is given, the map $$t\mapsto \exp(tX)$$ is a curve whose velocity at the point $$I$$ is $$X$$.

Now, finding the tangent vector to $$\SL(n;\mathbb{R})$$ is the same as picking out those matrices $$X$$ for which this curve stays (at least for a short time) in $$\SL(n;\mathbb{R})$$. For this we can use the following proposition.

<div class="proposition" markdown="1">

<ins id="prop12">**Proposition 12**</ins> For any $$X\in\Mat_n(\mathbb{R})$$, $$\det(\exp X)=\exp(\tr X)$$ holds.

</div>

This too can be solved using elementary linear algebra. Then from

$$\det(\exp tX)=\exp(\tr(tX))=\exp(t\cdot\tr X)$$

we know that $$X$$ satisfying this must exactly satisfy $$\tr X=0$$. That is, the tangent space of $$\SL(n;\mathbb{R})$$ consists of matrices satisfying $$\tr X=0$$, and this condition defines an $$n^2-1$$-dimensional vector space.

The following is a generalization of the left-invariant vector field examined above.

<div class="definition" markdown="1">

<ins id="def13">**Definition 13**</ins> A form $$\omega$$ defined on a Lie group $$G$$ is called *left invariant* if $$(dL_g)\omega=\omega$$ holds for any $$g\in G$$. The collection of left invariant $$k$$-forms defined on $$G$$ is denoted $$\Omega_\text{l.inv}^k(G)$$, and the collection of all left invariant forms defined on $$G$$ is denoted $$\Omega_\text{l.inv}^\ast(G)$$.

</div>

In particular, elements of $$\Omega_\text{l.inv}^1(G)$$ are called *Maurer-Cartan forms*.

In the same way as [Proposition 9](#prop9), the following proposition can be proved.
    
<div class="proposition" markdown="1">

<ins id="prop14">**Proposition 14**</ins> For a Lie group $$G$$ and $$\Omega_\text{l.inv}^\ast(G)$$, the following hold.

1. Any element of $$\Omega_\text{l.inv}^\ast(G)$$ is $$C^\infty$$.
2. $$\Omega_\text{l.inv}^\ast(G)$$ is a $$C^\infty(G)$$-subalgebra of $$\Omega^\ast(G)$$, and the map $$\omega\mapsto\omega_e$$ is a $$C^\infty(G)$$-algebra isomorphism from $$\Omega_\text{l.inv}^\ast(G)$$ to $$\bigwedge(T_e^\ast G)$$.
3. For any $$\omega\in\Omega_\text{l.inv}^1(G)$$ and left invariant vector field $$X$$, $$\omega(X)$$ is a constant function defined on $$G$$.
4. For any $$\omega\in\Omega_\text{l.inv}^1(G)$$ and $$X,Y\in\mathfrak{g}$$,
    
    $$d\omega(X,Y)=-\omega[X,Y]$$

    holds.
5. For a basis $$X_1,\ldots, X_d$$ of $$\mathfrak{g}$$ and its dual basis $$\omega_1,\ldots,\omega_d$$, there exist $$d^3$$ constants $$c_{ij}^k$$ satisfying the formula
    
    $$[X_i,X_j]=\sum_{k=1}^d c_{ij}^kX_k$$

    These satisfy the two conditions

    $$c_{ij}^k+c_{ji}^k=0,\qquad\sum_r (c_{ij}^rc_{rk}^s+c_{jk}^rc_{ri}^s+c_{ki}^rc_{rj}^s)=0\quad\text{for all $s$}$$

    and therefore the formula

    $$d\omega_i=\sum_{j < k} c_{jk}^i\omega_k\wedge\omega_j$$

    holds.

</div>

## Lie Correspondence

For any manifold, its tangent space can be thought of as germs of curves as above. Therefore, for any Lie group $$G$$ and its Lie algebra $$\mathfrak{g}$$, whenever an element of $$\mathfrak{g}$$ is given we can associate a curve in $$G$$. In this way, the Lie algebra can reveal all information about the Lie group. More precisely, to read off information about $$G$$ through curves in this way, the way of associating curves must be unique (up to homotopy) and must exist, so the Lie algebra contains all information about simply connected Lie groups. In this section, we shall examine this correspondence in a bit more detail, but omitting proofs.

The Lie correspondence is a collection of results concerning the following kinds of relationships between Lie groups and Lie algebras.

<div class="proposition" markdown="1">

<ins id="thm15">**Theorem 15**</ins> The following hold.

1. Let Lie groups $$G,H$$ be given, and let a homomorphism $$L:\mathfrak{g} \rightarrow \mathfrak{h}$$ between their Lie algebras $$\mathfrak{g},\mathfrak{h}$$ be given. If $$G$$ is simply connected, then there exists a unique homomorphism $$F:G \rightarrow H$$ satisfying $$dF=L$$.
2. For any finite-dimensional real Lie algebra $$\mathfrak{g}$$, there exists a simply connected Lie group $$G$$ having $$\mathfrak{g}$$ as its Lie algebra.

</div>

That is, in other words, the functor $$\Lie:\LieGrp \rightarrow \LieAlg$$ from $$\LieGrp$$ to $$\LieAlg$$ gives an equivalence of the two categories when restricted to the full subcategory of $$\LieGrp$$ consisting of simply connected Lie groups.

Apart from this category-theoretic result, this theorem also allows us to define an exponential map similar to the matrix exponential for any Lie group $$G$$ and its Lie algebra $$\mathfrak{g}$$. This is because $$(\mathbb{R},+)$$ is a 1-dimensional simply connected Lie group, so its Lie algebra is also 1-dimensional, and thus a Lie algebra homomorphism from it to another Lie algebra is uniquely determined by where the basis $$d/dt$$ goes; when $$d/dt$$ is sent to $$X\in \mathfrak{g}$$, applying [Theorem 15](#thm15) to this Lie algebra homomorphism yields the Lie group homomorphism $$\gamma: \mathbb{R}\rightarrow G$$ that defines the desired curve.

<div class="definition" markdown="1">

<ins id="def16">**Definition 16**</ins> For any Lie group $$G$$ and its Lie algebra $$\mathfrak{g}$$, and an element $$X\in \mathfrak{g}$$, let us denote the curve obtained through the above process by $$\gamma_X$$. Then define $$\exp:\mathfrak{g}\rightarrow G$$ by $$X\mapsto \gamma_X(1)$$.

</div>

In particular, when $$G$$ is a matrix Lie group as examined above, we can verify that this definition gives the matrix exponential.

Intuitively, the Lie algebra reads off information about the Lie group using the exponential. To say that we know the information about a Lie group, we must be able to recover at least locally the group operation of the Lie group. This is obtained from the following result.

<div class="proposition" markdown="1">

<ins id="thm17">**Theorem 17 (Baker-Campbell-Hausdorff)**</ins> For a Lie group $$G$$ and its Lie algebra $$\mathfrak{g}$$, and $$X,Y\in \mathfrak{g}$$, the formula

$$\exp(X)\exp(Y)=\exp\left(X+Y+\frac{1}{2}[X,Y]+\frac{1}{12}[X,[X,Y]]+\frac{1}{12}[Y,[Y,X]]+\cdots\right)$$

holds.

</div>

Strictly speaking, the above "theorem" lacks information about the coefficients of the terms corresponding to $$\cdots$$, but these coefficients are rarely needed in concrete applications. What is important is that when two elements (of the Lie group) in the directions specified by the Lie algebra elements $$X,Y$$ are multiplied, their product lies in the direction corresponding to the linear combination of $$X,Y$$ and the sum of their Lie brackets, and if $$X,Y$$ are sufficiently small vectors then this series also converges. On the other hand, in a Lie group $$G$$, any element near the identity $$e$$ can be written in the form $$g=\exp(X)$$, so this theorem contains exactly all information about the group operation of $$G$$ (near the identity). More concretely, we can view the Lie algebra $$\mathfrak{g}$$ as a manifold and $$\exp: \mathfrak{g}\rightarrow G$$ as a smooth map between manifolds, and then the differential at $$0\in \mathfrak{g}$$ is exactly $$\id_\mathfrak{g}$$. Therefore, there exists a suitable neighborhood $$U$$ of $$0$$ in $$\mathfrak{g}$$ such that $$\exp$$ defines a diffeomorphism between $$U$$ and $$\exp(U)$$ (in particular, the inverse $$\log$$ of the local diffeomorphism exists), but we cannot assert how the exponential map behaves outside this $$U$$.

When we learned [Theorem 15](#thm15) above, one natural question is whether, given a Lie group $$G$$ and its Lie algebra $$\mathfrak{g}$$, and a Lie subalgebra $$\mathfrak{h}$$ of $$\mathfrak{g}$$, there exists a Lie subgroup $$H$$ of $$G$$ having $$\mathfrak{h}$$ as its tangent space at the identity. However, by definition a Lie subalgebra is closed under the Lie bracket, so by [[Differential Manifolds] §Distribution, ⁋Theorem 3](/en/math/manifold/distribution#thm3) this defines a submanifold of $$G$$. These will also have the group operation by [Theorem 17](#thm17) above, but the problem is that, as pointed out earlier, this theorem is effective only in a local region. However, if $$G$$ were simply connected, there would be no topological obstacle to extending this to all of $$G$$, so the following theorem holds.

<div class="proposition" markdown="1">

<ins id="thm18">**Theorem 18**</ins> When a simply connected Lie group $$G$$ and its Lie algebra $$\mathfrak{g}$$, and a Lie subalgebra $$\mathfrak{h}$$ of $$\mathfrak{g}$$ are given, there exists a Lie subgroup $$H$$ of $$G$$ having $$\mathfrak{h}$$ as its Lie algebra.

</div>

## Classification of Abelian Lie Groups

Finally, we now carry out the classification of abelian Lie groups. By definition, an abelian Lie group is one whose group operation is commutative. Now consider the inner automorphism

$$\rho_g: G \rightarrow G; \quad h\mapsto \rho_g(h)=ghg^{-1}$$

([[Algebraic Structures] §Group Actions, ⁋Proposition 9](/en/math/algebraic_structures/group_actions#prop9)) This is a Lie group automorphism, and therefore differentiating it at the identity $$h=e$$ gives $$d\rho_g: \mathfrak{g}\rightarrow \mathfrak{g}$$, which becomes a Lie algebra automorphism.

<div class="definition" markdown="1">

<ins id="def19">**Definition 19**</ins> For a Lie group $$G$$, the correspondence

$$\Ad:G\rightarrow \Aut(\mathfrak{g});\quad g\mapsto d\rho_g$$

is called the *adjoint representation* of $$G$$. The map

$$\ad: \mathfrak{g}\rightarrow \Lie(\Aut(\mathfrak{g}))$$

obtained by differentiating this is called the *adjoint representation* of $$\mathfrak{g}$$.

</div>

Then by definition, within a sufficiently small range, the adjoint representation of $$G$$ is exactly the same as looking at the Lie derivative, and therefore by [[Differential Manifolds] §Lie Derivative, ⁋Proposition 4](/en/math/manifold/Lie_derivative#prop4) the formula

$$\ad(X)Y =[X,Y]$$

holds. Moreover, the following holds.

<div class="proposition" markdown="1">

<ins id="thm20">**Theorem 20**</ins> For a connected compact Lie group $$G$$, the following hold.

1. $$d(\exp(e))=\id_\mathfrak{g}$$
2. $$\Ad\circ\exp=\exp_{\GL(\mathfrak{g})}\circ \ad$$
3. $$\rho_x\circ\exp=\exp\circ\Ad(x)$$

</div>

If $$G$$ were an abelian group, then $$\rho_g$$ would simply be the identity map, and therefore $$\Ad_g(X)=X$$ would hold for any $$g\in G$$ and any $$X\in \mathfrak{g}$$, and thus the adjoint representation of $$\mathfrak{g}$$, being its differential, would be $$0$$. That is, for any abelian Lie group, the Lie bracket of its Lie algebra is always $$0$$, and we call this an *abelian* Lie algebra. This is not an awkward name because by [Definition 8](#def8) this is the only way for an anticommutative Lie bracket to also be commutative.

Then, when $$G$$ is abelian, in particular by [Theorem 17](#thm17) we have $$\exp(X+Y)=\exp(X)\exp(Y)$$. That is, $$\exp$$ is a group homomorphism. Moreover, in this case the expression inside $$\exp$$ on the right-hand side of [Theorem 17](#thm17) necessarily converges, and this results in $$\exp$$ being a *surjective* group homomorphism (when $$G$$ is connected). Therefore, by the first isomorphism theorem,

$$G\cong \mathfrak{g}/\ker(\exp)$$

Now $$\mathfrak{g}$$ is an $$n$$-dimensional $$\mathbb{R}$$-vector space, and since $$\exp$$ is a local diffeomorphism, $$\ker(\exp)$$ becomes a *discrete* additive subgroup. It is well known that this is $$\mathbb{Z}^k$$, and therefore

$$G\cong \mathfrak{g}/\ker(\exp)\cong \mathbb{R}^n/\mathbb{Z}^k\cong T^k\times \mathbb{R}^{n-k}$$

That is, a connected abelian Lie group is necessarily a product of a torus and $$\mathbb{R}^k$$, and in particular a compact connected abelian Lie group is necessarily a torus.

---

**References**

**[War]** Frank W. Warner. *Foundations of Differentiable Manifolds and Lie Groups*, Graduate texts in mathematics, Springer, 2013  

---
