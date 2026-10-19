---
title: "Differentials"
description: "This post defines functions between two differentiable manifolds, proves their continuity, and examines examples such as inclusion maps and constant functions. It also explores actions on tangent bridge spaces."
excerpt: "The differential between two tangent spaces"

categories: [Math / Manifolds]
permalink: /en/math/manifolds/differentials
sidebar: 
    nav: "manifolds-en"

date: 2022-06-15
weight: 5
translated_at: 2026-06-01T05:30:06+00:00
translation_source: kimi-cli
last_polished_at: 2026-10-19T19:15:06+00:00
translation_polish_source: antigravity-gemini-3.8-flash-high
---
We previously defined, for a manifold $M$, the tangent space $T_pM$, showed that their dimension equals that of the original manifold $M$, and also defined a natural basis of $T_pM$. In this post, we define functions between two manifolds and examine how they behave on tangent spaces.

## Functions between Smooth Manifolds

::: Definition 1
Let two manifolds $M,N$ be given. A function $F:M\rightarrow N$ is said, at a point $p\in M$, to be $C^\infty$ if there exist, containing $p$, a suitable coordinate system $(U,\varphi)$ and, with $F(U)\subseteq V$, a suitable coordinate system $(V,\psi)$ such that $\psi\circ F\circ\varphi^{-1}$ is $C^\infty$.

{% diagram Math/Manifolds/Differentials-1.png width="500px" alt="smooth_map" %}
<cap>[Lee], p.34. Fig. 2.2</cap>

If $F$ is $C^\infty$ at every point, we simply call it a $C^\infty$ function.
:::

As when we previously defined a function from a manifold to $\mathbb{R}$ to be $C^\infty$, one should show that this definition is also independent of the choice of coordinate system; but since this is basically identical to what was proved after [§Smooth Manifolds, ⁋Definition 2](/en/math/manifolds/smooth_manifolds#def2){: data-lid="ppfgm" }, we omit it.

::: Proposition 2
Let two manifolds $M,N$ be given. If $F:M\rightarrow N$ is, at a point $p\in M$, $C^\infty$, then this function is continuous at $p$.
:::
::: Proof
Assume the situation of [Definition 1](#def1){: data-lid="4inbc" }. Then first, the function $\psi\circ F\circ\varphi^{-1}:\varphi(U)\rightarrow\psi(V)$ between Euclidean spaces is $C^\infty$. Since this function is differentiable, it is naturally continuous. However, $\varphi$ and $\psi$ are both homeomorphisms, so

$$F=\psi^{-1}\circ(\psi\circ F\circ\varphi^{-1})\circ\varphi$$

is continuous as a composition of continuous functions.
:::


::: Example 3
$\id_M:M\rightarrow M$ is obviously a $C^\infty$ function. More generally, if any open subset $U\subseteq M$ is given the open submanifold structure ([§Examples of Differentiable Manifolds, ⁋Definition 3](/en/math/manifolds/examples_of_manifolds#def3){: data-lid="83oiz" }), the inclusion map $U\hookrightarrow M$ is a $C^\infty$ function.
:::

::: Example 4
For any two manifolds $M,N$, the constant function sending every point of $M$, $p\in M$, to a fixed point $q\in N$ is $C^\infty$.
:::

We have now defined manifolds, our objects of study, as well as functions between manifolds. It is not difficult to verify that the following proposition holds.

::: Proposition 5
For three manifolds $M,N,P$, if both $F:M\rightarrow N$ and $G:N\rightarrow P$ are $C^\infty$, then their composition $G\circ F$ is also $C^\infty$.
:::

It is then clear that isomorphisms between manifolds should be defined as follows.

::: Definition 6
If for two manifolds $M,N$, there exist $C^\infty$ functions $F:M\rightarrow N$ and $G:N\rightarrow M$ respectively such that $G\circ F=\id_M$ and $F\circ G=\id_N$, then each of $F$ and $G$ is called a *diffeomorphism*, and $M$ and $N$ are said to be *diffeomorphic*.
:::

Thus, manifolds and smooth functions form the category $\Man$.

::: remark Remark {#rmk}
One can endow the same topological manifold $M$ with smooth structures that are diffeomorphic but not identical. Let us define two smooth structures $\mathcal{A}_1$, $\mathcal{A}_2$ by the single charts $(\mathbb{R},\id_\mathbb{R})$, $(\mathbb{R}, x\mapsto x^{3})$, respectively. Then $\mathcal{A}_1$ and $\mathcal{A}_2$ define different smooth structures. ([§Smooth Manifolds, ⁋Example 4](/en/math/manifolds/smooth_manifolds#ex4){: data-lid="7fwon" })  
For convenience, let us denote $(M,\mathcal{A}_1)$ by $M_1$ and $(M,\mathcal{A}_2)$ by $M_2$, and let $\varphi=\id_\mathbb{R}$ and $\psi=(x\mapsto x^3)$. 

These two manifolds $M_1, M_2$ are diffeomorphic to each other. From $M_1$ to $M_2$, define a function $F$ by $x\mapsto x^{1/3}$. Then obviously $F^{-1}$ is defined by $y\mapsto y^3$. By definition, $F$ is $C^\infty$. This is because, for any point $p\in M_1$, if we take on $M_1$ and $M_2$ the two coordinate systems $(\mathbb{R},\varphi)$ and $(\mathbb{R},\psi)$ defined respectively, it is obvious that $p\in\mathbb{R}$ and $F(\mathbb{R})\subseteq\mathbb{R}$ are satisfied, and furthermore, since they satisfy

$$(\psi\circ F\circ \varphi^{-1})(t)=t$$

$\psi\circ F\circ\varphi^{-1}$ is $C^\infty$.  
Not only that, $F^{-1}$ is also $C^\infty$; this is because, similarly, for any point $q\in M_2$, if we take the same coordinate systems as above, $q\in\mathbb{R}$ and $F^{-1}(\mathbb{R})\subseteq\mathbb{R}$ hold, and also

$$(\varphi\circ F^{-1}\circ \psi^{-1})(s)=s$$

holds. 
:::

## Differentials

A manifold is fundamentally a space where differentiation can be performed; hence, to understand a function between manifolds, we must know how this function transforms derivations, that is, elements of the tangent space. 

Suppose a $C^\infty$ function $F:M\rightarrow N$ between two manifolds is given, and fix an arbitrary point $p\in M$. The function $F$ naturally induces, via the formula

$$g\mapsto g\circ F$$

the function $F^\ast:\mathcal{C}_{N,F(p)}^\infty\rightarrow \mathcal{C}_{M,p}^\infty$ defined by it. Moreover, for any $f,g\in \mathcal{C}_{N,F(p)}^\infty$ and real number $\alpha\in\mathbb{R}$,

$$F^\ast(f+g)=(f+g)\circ F=f\circ F+g\circ F=F^\ast(f)+F^\ast(g),\quad F^\ast(\alpha f)=(\alpha f)\circ F=\alpha(f\circ F)=\alpha F^\ast(f)$$

holds, so $F^\ast$ is a linear map between two $\mathbb{R}$-vector spaces. 

Meanwhile, since $T_pM$ and $T_{F(p)}N$ are the elements among the linear maps from $\mathcal{C}^\infty_{M,p}$ and $\mathcal{C}^\infty_{N,F(p)}$ to $\mathbb{R}$ that satisfy the Leibniz rule, they are subspaces of the respective dual spaces $(\mathcal{C}^\infty_{M,p})^\ast$ and $(\mathcal{C}^\infty_{N,F(p)})^\ast$. Therefore, for the linear map $F^\ast:\mathcal{C}^\infty_{N,F(p)}\rightarrow \mathcal{C}^\infty_{M,p}$ obtained above, we can consider its dual map $(F^\ast)^\ast:(\mathcal{C}^\infty_{M,p})^\ast\rightarrow(\mathcal{C}^\infty_{N,F(p)})^\ast$. 

{% diagram Math/Manifolds/Differentials-2.svg width="18.52em" alt="differential" %}

Explicitly, this is the function defined for any linear map $L\in (\mathcal{C}^\infty_{M,p})^\ast$ by

$$(F^\ast)^\ast(L)=L\circ F^\ast$$

Now, restricting this definition to $T_pM$ yields the desired definition.

Before that, to restate the above discussion from the viewpoint of the elements of the vector spaces, $(F^\ast)^\ast\vert_{T_pM}$ sends any $v\in T_pM$ to $v\circ F^\ast\in (\mathcal{C}^\infty_{N,F(p)})^\ast$. Meanwhile, since $v\circ F^\ast$ is an element of $(\mathcal{C}^\infty_{N,F(p)})^\ast$, it is defined through how it acts on an arbitrary $g\in \mathcal{C}^\infty_{N,F(p)}$, which is defined by

$$(v\circ F^\ast)(g)=v(F^\ast(g))=v(g\circ F)$$

Moreover, $v\circ F^\ast$ defined in this way actually belongs to $T_{F(p)}N$. That is, it satisfies the Leibniz rule. This is obtained from the following formula:

$$\begin{aligned}(v\circ F^\ast)(fg)&=v(F^\ast(fg))=v((f\circ F)(g\circ F))\\
&=(f\circ F)(p)v(g\circ F)+(g\circ F)(p) v(f\circ F)\\
&=f(F(p))(v\circ F^\ast)(g)+g(F(p))(v\circ F^\ast)(f)\end{aligned}$$

Summarizing the discussion so far yields the following.

::: Definition 7
Let $F:M\rightarrow N$ be a $C^\infty$ function between two manifolds. For any $p\in M$, the *differential* of $F$ at the point $p$, $\dd{F_p}:T_pM\rightarrow T_{F(p)}N$, is the linear map defined for any $v\in T_pM$ and any $g\in \mathcal{C}^\infty_{N,F(p)}$ by

$$(\dd{F_p}(v))g=v(g\circ F)$$
:::

Several consequences are immediate from the definition. First, for $\id_M:M\rightarrow M$, $\dd{(\id_M)_p}$ is always the identity from $T_pM$ to $T_pM$, namely $\id_{T_pM}$. This is clear from the formula in [Definition 7](#def7){: data-lid="esjrg" }. Also, for three manifolds $M,N,P$, if $F:M\rightarrow N$ and $G:N\rightarrow P$ are $C^\infty$, then the formula

$$\dd{(G\circ F)_p}=(\dd{G_{F(p)}})\circ (\dd{F_p})$$

holds. This is obvious either from the fact that the pullback used to define the differential preserves composition, or likewise by directly substituting $G\circ F$ into the formula of [Definition 7](#def7){: data-lid="rpk1o" }. From this one can show, among other things, that for a diffeomorphism $F$, $\dd{F_p}$ is always an isomorphism of vector spaces.

However, there are very many $C^\infty$ functions whose differential is an isomorphism but which are not diffeomorphisms.

::: Proposition 8
For a manifold $M$ and $M$'s open submanifold $U$, the inclusion map $\iota:U\hookrightarrow M$ induces an isomorphism between tangent spaces for every $p\in U$. That is, $\dd{\iota_p}$ is always an isomorphism.
:::
::: Proof
Since germs are determined on arbitrarily small neighborhoods of a point, the map $\iota^\ast:\mathcal{C}^\infty_{M,\iota(p)}\rightarrow\mathcal{C}^\infty_{U,p}$ given by restriction is an isomorphism of $\mathbb{R}$-algebras, and therefore its dual is also an isomorphism and preserves the Leibniz rule in both directions, so $\dd{\iota_p}:T_pU\rightarrow T_{\iota(p)}M$ is an isomorphism. In fact, from the outset there is no harm in regarding the two vector spaces as identical.
:::

## Bases of Tangent Spaces and Differentials

If we view $\mathbb{R}^m$ as an $m$-dimensional manifold, we can see that the way we defined tangent vectors is exactly identical to directional vectors in $\mathbb{R}^m$. In this case, for any $p\in\mathbb{R}^m$, based at the point $p$, the standard vectors of $\mathbb{R}^m$, $m$ in number, define directional derivatives in their respective directions, and we agreed to write these as

$$\frac{\partial}{\partial r^1}\bigg\vert_p,\cdots,\frac{\partial}{\partial r^m}\bigg\vert_p$$

In the case of a general manifold, after choosing a coordinate system containing $p\in M$, $(U,\varphi)$, we expressed tangent vectors using $\varphi$'s component functions $x^1,\ldots, x^m$ as

$$\frac{\partial}{\partial x^1}\bigg\vert_p,\cdots,\frac{\partial}{\partial x^m}\bigg\vert_p$$

Here, for any $f\in \mathcal{C}^\infty_{M,p}$,

$$\frac{\partial}{\partial x^i}\bigg\vert_pf=\frac{\partial}{\partial r^i}\bigg\vert_{\varphi(p)} (f\circ\varphi^{-1})$$

holds. However, keeping [Definition 7](#def7){: data-lid="42cgj" } in mind and examining this formula again, we see that it has the same form as the differential of $\varphi^{-1}:\varphi(U)\rightarrow U$.[^1] That is, the basis of the tangent space is nothing other than transferring, from $\mathbb{R}^m$'s tangent space $T_{\varphi(p)}\mathbb{R}^m$, the $m$ basis vectors via the differential $\dd{\varphi}^{-1}_{\varphi(p)}$.

To view this from a more linear-algebraic perspective, if we let $\mathcal{B}$ be the standard basis of $\mathbb{R}^m$ and $\mathcal{C}$ be the basis consisting of the $\partial/\partial x^i$ for $T_pM$, then from $(T_{\varphi(p)}\mathbb{R}^m, \mathcal{B})$ to $(T_pM, \mathcal{C})$, the matrix representation of the linear map $\dd{\varphi}^{-1}_{\varphi(p)}$ is precisely the identity matrix.

More generally, let $M,N$ be manifolds of dimensions $m,n$ respectively, and let $F:M\rightarrow N$ be any $C^\infty$ function. Then for a fixed $p\in M$, there exist a coordinate system containing $p$, $(U,\varphi)$, and a coordinate system containing $F(U)$, $(V,\psi)$, such that $\psi\circ F\circ\varphi^{-1}$ is $C^\infty$. Now let $\varphi=(x^i)_{i=1}^{m}$ and $\psi=(y^j)_{j=1}^n$. Then likewise, the bases of the tangent spaces $T_pM$ and $T_{F(p)}N$ are given respectively by

$$\frac{\partial}{\partial x^1}\bigg\vert_p,\cdots,\frac{\partial}{\partial x^m}\bigg\vert_p,\quad\text{and}\quad\frac{\partial}{\partial y^1}\bigg\vert_{F(p)},\cdots\frac{\partial}{\partial y^n}\bigg\vert_{F(p)}$$

Let us now represent $\dd{F_p}$ as a matrix with respect to these. To do this, it suffices to express the vector to which each $\partial/\partial x^i$ is sent via $\dd{F_p}$ as a linear combination of the $\partial/\partial y^j$. That is, in

$$\dd{F_p}\left(\frac{\partial}{\partial x^i}\bigg\vert_p\right)=a_{1i}\frac{\partial}{\partial y^1}\bigg\vert_{F(p)}+\cdots+a_{ni}\frac{\partial}{\partial y^n}\bigg\vert_{F(p)}$$

it suffices to find each of the coefficients $a_{ji}$. However, if we denote the maximal ideal of $\mathcal{C}^\infty_{N,F(p)}$ by $\mathfrak{n}$, since as seen in [§Cotangent Space, ⁋Definition 3](/en/math/manifolds/cotangent_space#def3){: data-lid="6g66l" } anyway, the $\partial/\partial y^j$ are the dual basis to the elements of $\mathfrak{n}/\mathfrak{n}^2$, $y^j+\mathfrak{n}^2$, for this it suffices to apply both sides to the function $y^j$.[^2] That is, from

$$\dd{F_p}\left(\frac{\partial}{\partial x^i}\bigg\vert_p\right)y^j=a_{1i}\frac{\partial}{\partial y^1}\bigg\vert_{F(p)}y^j+\cdots+a_{ji}\frac{\partial}{\partial y^j}\bigg\vert_{F(p)}y^j+\cdots+a_{ni}\frac{\partial}{\partial y^n}\bigg\vert_{F(p)}y^j$$

by the definition of the dual basis only $a_{ji}$ remains on the right-hand side, so

$$\dd{F_p}\left(\frac{\partial}{\partial x^i}\bigg\vert_p\right)y^j=a_{ji}$$

and from this we see that the matrix representation of $\dd{F_p}$ with respect to the two bases $\partial/\partial x^i$ and $\partial/\partial y^j$ is the matrix

$$\begin{pmatrix}\partial(y^1\circ F)/\partial x^1&\partial(y^1\circ F)/\partial x^2&\cdots&\partial(y^1\circ F)/\partial x^m\\\partial(y^2\circ F)/\partial x^1&\partial(y^2\circ F)/\partial x^2&\cdots&\partial(y^2\circ F)/\partial x^m\\\vdots&\vdots&\ddots&\vdots\\\partial(y^n\circ F)/\partial x^1&\partial(y^n\circ F)/\partial x^2&\cdots&\partial(y^n\circ F)/\partial x^m\end{pmatrix}$$

That is, this is nothing but the Jacobian of the function $\psi\circ F\circ\varphi^{-1}$ between Euclidean spaces.

In particular, if $M=N$ and $F=\id_M$ but we choose different coordinate systems $(U, \varphi)$ and $(V,\psi)$, this will be the Jacobian matrix of the transition map $\psi\circ\varphi^{-1}$.


---

**References**

**[War]** Frank W. Warner. *Foundations of Differentiable Manifolds and Lie Groups*, Graduate texts in mathematics, Springer, 2013  
**[Lee]** John M. Lee. *Introduction to Smooth Manifolds*, Graduate texts in mathematics, Springer, 2012

---

[^1]: Of course, for this $\varphi^{-1}$ must be $C^\infty$, but since the differentiable structure on $U$ is itself just the differentiable structure of $\varphi(U)$ transferred over in the first place, $\varphi^{-1}$ is in fact a diffeomorphism.
[^2]: For convenience, we assumed $\psi(F(p))=0$.
