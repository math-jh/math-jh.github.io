---title: "Differentials"
excerpt: "The differential between two tangent spaces"

categories: [Math / Manifold]
permalink: /en/math/manifold/differentials
header:
    overlay_image: /assets/images/Math/Manifold/Differentials.png
    overlay_filter: 0.5
sidebar: 
    nav: "manifold-en"

date: 2022-06-15
last_modified_at: 2022-06-15
weight: 5
translated_at: 2026-05-28T11:36:15+00:00
translation_source: kimi-cli
---
We previously defined the tangent space $$T_pM$$ of a manifold $$M$$, showed that its dimension is the same as that of the original manifold $$M$$, and also defined its natural basis. In this post we define functions between two manifolds and examine how they behave on tangent spaces.

## Functions between Smooth Manifolds

<div class="definition" markdown="1">

<ins id="def1">**Definition 1**</ins> Let two manifolds $$M,N$$ be given. A function $$F:M\rightarrow N$$ is said to be $$C^\infty$$ at a point $$p\in M$$ if there exist a coordinate system $$(U,\varphi)$$ containing $$p$$ and a coordinate system $$(V,\psi)$$ with $$F(U)\subseteq V$$ such that $$\psi\circ F\circ\varphi^{-1}$$ is $$C^\infty$$.

![smooth_map](/assets/images/Math/Manifold/Differentials-1.png){:style="width:500px" class="invert" .align-center}
<cap>[Lee], p.34. Fig. 2.2</cap>

If $$F$$ is $$C^\infty$$ at every point, we simply call it a $$C^\infty$$ function.

</div>

As before when we defined $$C^\infty$$ functions from a manifold to $$\mathbb{R}$$, we should show that this definition is independent of the choice of coordinate system, but this is essentially the same as what we proved after [§Smooth Manifolds, ⁋Definition 2](/en/math/manifold/smooth_manifolds#def2), so we omit it.

<div class="proposition" markdown="1">

<ins id="prop2">**Proposition 2**</ins> Let two manifolds $$M,N$$ be given. If $$F:M\rightarrow N$$ is $$C^\infty$$ at a point $$p\in M$$, then this function is continuous at $$p$$.

</div>
<details class="proof" markdown="1">
<summary>Proof</summary>

Assume the situation of [Definition 1](#def1) as is. Then first, the function $$\psi\circ F\circ\varphi^{-1}:\varphi(U)\rightarrow\psi(V)$$ between Euclidean spaces is $$C^\infty$$. Since this function is differentiable, it is obviously continuous. But $$\varphi$$ and $$\psi$$ are both homeomorphisms, so

$$F=\psi^{-1}\circ(\psi\circ F\circ\varphi^{-1})\circ\varphi$$

is continuous as a composition of continuous functions.

</details>


<div class="example" markdown="1">

<ins id="ex3">**Example 3**</ins> $$\id_M:M\rightarrow M$$ is obviously a $$C^\infty$$ function. More generally, if we give any open subset $$U\subseteq M$$ the open submanifold structure ([§Examples of Manifolds, ⁋Definition 3](/en/math/manifold/examples_of_manifolds#def3)), the inclusion map $$U\hookrightarrow M$$ is a $$C^\infty$$ function.

</div>

<div class="example" markdown="1">

<ins id="ex4">**Example 4**</ins> For any two manifolds $$M,N$$, the constant map sending every point $$p\in M$$ to a fixed point $$q\in N$$ is $$C^\infty$$.

</div>

We have now defined the manifolds, which are the objects we deal with, and the functions between manifolds. The following proposition can be checked without difficulty.

<div class="proposition" markdown="1">

<ins id="prop5">**Proposition 5**</ins> For three manifolds $$M,N,P$$, if both $$F:M\rightarrow N$$ and $$G:N\rightarrow P$$ are $$C^\infty$$, then their composition $$G\circ F$$ is also $$C^\infty$$.

</div>

Then it is clear that isomorphisms between manifolds should be defined as follows.

<div class="definition" markdown="1">

<ins id="def6">**Definition 6**</ins> If for two manifolds $$M,N$$, there exist $$F:M\rightarrow N$$ and $$G:N\rightarrow M$$ such that $$G\circ F=\id_M$$ and $$F\circ G=\id_N$$, then we call each of $$F$$ and $$G$$ a *diffeomorphism*, and say that $$F$$ and $$G$$ are *diffeomorphic*.

</div>

Thus, manifolds and smooth functions form the category $$\Man$$.

<div class="remark" markdown="1">

<ins id="rmk1">**Remark**</ins> We can give distinct smooth structures on the same topological manifold $$M$$ that are diffeomorphic to each other but not identical. Define two smooth structures $$\mathcal{A}_1$$, $$\mathcal{A}_2$$ by the single charts $$(\mathbb{R},\id_\mathbb{R})$$ and $$(\mathbb{R}, x\mapsto x^{3})$$, respectively. Then $$\mathcal{A}_1$$ and $$\mathcal{A}_2$$ define different smooth structures. ([§Smooth Manifolds, ⁋Example 4](/en/math/manifold/smooth_manifolds#ex4))  
For convenience, let us denote $$(M,\mathcal{A}_1)$$ by $$M_1$$, $$(M,\mathcal{A}_2)$$ by $$M_2$$, $$\varphi=\id_\mathbb{R}$$, and $$\psi=(x\mapsto x^3)$$.

These two manifolds $$M_1, M_2$$ are diffeomorphic to each other. Define the function $$F$$ from $$M_1$$ to $$M_2$$ by $$x\mapsto x^{1/3}$$. Then obviously $$F^{-1}$$ is defined by $$y\mapsto y^3$$. By definition $$F$$ is $$C^\infty$$. For any point $$p\in M_1$$, if we take the two coordinate systems $$(\mathbb{R},\varphi)$$ and $$(\mathbb{R},\psi)$$ defined on $$M_1$$ and $$M_2$$ respectively, it is obvious that $$p\in\mathbb{R}$$ and $$F(\mathbb{R})\subset\mathbb{R}$$, and since they satisfy

$$(\psi\circ F\circ \varphi^{-1})(t)=t$$

we have that $$\psi\circ\varphi^{-1}$$ is $$C^\infty$$.  
Moreover, $$F^{-1}$$ is also $$C^\infty$$, because similarly for any point $$q\in M_2$$, if we take the same coordinate systems as above, then $$q\in\mathbb{R}$$ and $$F^{-1}(\mathbb{R})\subset\mathbb{R}$$ hold, and moreover

$$(\psi^{-1}\circ F^{-1}\circ \varphi)(s)=s$$

holds.

</div>

## Differentials

A manifold is basically a space where differentiation is possible, so in order to understand a function between manifolds we must know how this function transforms differentials, that is, elements of the tangent space.

Let a $$C^\infty$$ function $$F:M\rightarrow N$$ between two manifolds be given. The function $$F$$ naturally induces the function $$F^\ast:\mathcal{C}_{N,F(p)}^\infty\rightarrow \mathcal{C}_{M,p}^\infty$$ defined by the formula

$$g\mapsto g\circ F$$

Moreover, for any $$f,g\in \mathcal{C}_{N,F(p)}^\infty$$ and any real number $$\alpha\in\mathbb{R}$$,

$$F^\ast(f+g)=(f+g)\circ F=f\circ F+g\circ F=F^\ast(f)+F^\ast(g),\quad F^\ast(\alpha f)=(\alpha f)\circ F=\alpha(f\circ F)=\alpha F^\ast(f)$$

hold, so $$F^\ast$$ is a linear map between two $$\mathbb{R}$$-vector spaces.

On the other hand, $$T_pM$$ and $$T_{F(p)}N$$ are the elements among linear maps from $$\mathcal{C}^\infty_{M,p}$$ and $$\mathcal{C}^\infty_{N,F(p)}$$ to $$\mathbb{R}$$ that satisfy the Leibniz rule, so they become subspaces of the respective dual spaces $$(\mathcal{C}^\infty_{M,p})^\ast$$ and $$(\mathcal{C}^\infty_{N,F(p)})^\ast$$. Therefore, we can consider the dual map $$(F^\ast)^\ast:(\mathcal{C}^\infty_{M,p})^\ast\rightarrow(\mathcal{C}^\infty_{N,F(p)})^\ast$$ of the linear map $$F^\ast:\mathcal{C}^\infty_{N,F(p)}\rightarrow \mathcal{C}^\infty_{M,p}$$ obtained above.

![differential](/assets/images/Math/Manifold/Differentials-2.png){:style="width:17.6em" class="invert" .align-center}

Explicitly, this is the function defined for any linear map $$L\in (\mathcal{C}^\infty_{M,p})^\ast$$ by

$$(F^\ast)^\ast(L)=L\circ F^\ast$$

Restricting this definition to $$T_pM$$, we obtain the desired definition.

Before that, let us reorganize the above discussion from the viewpoint of elements of the vector spaces: $$(F^\ast)^\ast\vert_{T_pM}$$ sends any $$v\in T_pM$$ to $$v\circ F^\ast\in (\mathcal{C}^\infty_{N,F(p)})^\ast$$. On the other hand, since $$v\circ F^\ast$$ is an element of $$(\mathcal{C}^\infty_{N,F(p)})^\ast$$, it is defined by how it acts on any $$g\in \mathcal{C}^\infty_{N,F(p)}$$, namely

$$(v\circ F^\ast)(g)=v(F^\ast(g))=v(g\circ F)$$

Moreover, this $$v\circ F^\ast$$ defined in this way actually belongs to $$T_{F(p)}N$$. That is, it satisfies the Leibniz rule. This follows from the formula

$$\begin{aligned}(v\circ F^\ast)(fg)&=v(F^\ast(fg))=v((f\circ F)(g\circ F))\\
&=(f\circ F)(p)v(g\circ F)+(g\circ F)(p) v(f\circ F)\\
&=f(F(p))(v\circ F^\ast)(g)+g(F(p))(v\circ F^\ast)(f)\end{aligned}$$

Summarizing the discussion so far, we have the following.

<div class="definition" markdown="1">

<ins id="def7">**Definition 7**</ins> Let $$F:M\rightarrow N$$ be a $$C^\infty$$ function between two manifolds. For any $$p\in M$$, the *differential* of $$F$$ at the point $$p$$, $$dF_p:T_pM\rightarrow T_{F(p)}N$$, is the linear map defined for any $$v\in T_pM$$ and any $$g\in \mathcal{C}^\infty_{N,F(p)}$$ by

$$(dF_p(v))g=v(g\circ F)$$

</div>

Several consequences are obvious from the definition. First, for $$\id_M:M\rightarrow M$$, $$d(\id_M)_p$$ is always the identity $$\id_{T_pM}$$ from $$T_pM$$ to $$T_pM$$. This is clear from the formula in [Definition 7](#def7). Also, for three manifolds $$M,N,P$$, if $$F:M\rightarrow N$$ and $$G:N\rightarrow P$$ are $$C^\infty$$, then the formula

$$d(G\circ F)_p=(dG_{F(p)})\circ (dF_p)$$

holds. This is obvious either from the fact that the pullback used to define the differential preserves composition well, or likewise by directly substituting $$G\circ F$$ into the formula of [Definition 7](#def7). From this we can show that for a diffeomorphism $$F$$, $$dF_p$$ is always an isomorphism between vector spaces.

However, among $$C^\infty$$ functions for which the differential is an isomorphism, there are very many that are not diffeomorphisms.

<div class="proposition" markdown="1">

<ins id="prop8">**Proposition 8**</ins> For a manifold $$M$$ and an open submanifold $$U$$ of $$M$$, the inclusion map $$\iota:U\hookrightarrow M$$ induces an isomorphism between tangent spaces for every $$p\in U$$. That is, $$d\iota_p$$ is always an isomorphism.

</div>
<details class="proof" markdown="1">
<summary>Proof</summary>

This is obvious because $$\iota^\ast$$ induces an isomorphism between $$\mathcal{C}^\infty_{U,p}$$ and $$\mathcal{C}^\infty_{M,\iota(p)}$$. In fact, from the beginning there is no harm in regarding the two vector spaces as the same.

</details>

## Basis of Tangent Spaces and Differentials

Regarding $$\mathbb{R}^m$$ as an $$m$$-dimensional manifold, we can see that the way we defined tangent vectors is exactly the same as directional vectors in $$\mathbb{R}^m$$. In this case, for any $$p\in\mathbb{R}^m$$, the standard $$m$$ vectors of $$\mathbb{R}^m$$ based at the point $$p$$ define directional derivatives in their respective directions, and we agreed to write these as

$$\frac{\partial}{\partial r^1}\bigg|_p,\cdots,\frac{\partial}{\partial r^m}\bigg|_p$$

For a general manifold, we chose a coordinate system $$(U,\varphi)$$ containing $$p\in M$$, and then expressed tangent vectors using the component functions $$x^1,\ldots, x^m$$ of $$\varphi$$ as

$$\frac{\partial}{\partial x^1}\bigg|_p,\cdots,\frac{\partial}{\partial x^m}\bigg|_p$$

Then, for any $$f\in C^\infty_p(M)$$,

$$\frac{\partial}{\partial x^i}\bigg|_pf=\frac{\partial}{\partial r^i}\bigg|_p (f\circ\varphi^{-1})$$

holds. However, keeping [Definition 7](#def7) in mind and looking at this formula again, we can see that it has exactly the same form as the differential of $$\varphi^{-1}:\varphi(U)\rightarrow U$$.[^1] In other words, the basis of the tangent space is nothing other than the $$m$$ bases of the tangent space $$T_{\varphi(p)}\mathbb{R}^m$$ of $$\mathbb{R}^m$$ transferred via the differential $$d\varphi^{-1}_{\varphi(p)}$$.

From a more linear-algebraic point of view, if $$\mathcal{B}$$ is the standard basis of $$\mathbb{R}^m$$ and $$\mathcal{C}$$ is the basis of $$T_pM$$ consisting of the $$\partial/\partial x^i$$, then the matrix representation of the linear map $$d\varphi^{-1}_{\varphi(p)}$$ from $$(T_{\varphi(p)}\mathbb{R}^n, \mathcal{B})$$ to $$(T_pM, \mathcal{C})$$ can be said to be exactly the identity matrix.

More generally, let $$M,N$$ be manifolds of dimensions $$m,n$$ respectively, and let $$F:M\rightarrow N$$ be any $$C^\infty$$ function. Then for a fixed $$p\in M$$, there exist a coordinate system $$(U,\varphi)$$ containing $$p$$ and a coordinate system $$(V,\psi)$$ containing $$F(U)$$ such that $$\psi\circ F\circ\varphi^{-1}$$ is $$C^\infty$$. Now let $$\varphi=(x^i)_{i=1}^{m}$$ and $$\psi=(y^j)_{j=1}^n$$. Then likewise the bases of the tangent spaces $$T_pM$$ and $$T_{F(p)}N$$ are given respectively by

$$\frac{\partial}{\partial x^1}\bigg|_p,\cdots,\frac{\partial}{\partial x^m}\bigg|_p,\quad\text{and}\quad\frac{\partial}{\partial y^1}\bigg|_{F(p)},\cdots\frac{\partial}{\partial y^n}\bigg|_{F(p)}$$

Let us now represent $$dF_p$$ as a matrix via these. To do this, we need to express the vector to which each $$\partial/\partial x^i$$ is sent by $$dF_p$$ as a linear combination of the $$\partial/\partial y^j$$. That is, we need only find the coefficients $$a_{ji}$$ in

$$dF_p\left(\frac{\partial}{\partial x^i}\bigg|_p\right)=a_{1i}\frac{\partial}{\partial y^1}\bigg|_{F(p)}+\cdots+a_{ni}\frac{\partial}{\partial y^n}\bigg|_{F(p)}$$

But since the $$\partial/\partial y^j$$ are the dual basis of the elements $$y^j+\mathfrak{n}^2$$ of $$\mathfrak{n}/\mathfrak{n}^2$$, to do this we simply apply both sides to the function $$y^j$$.[^2] Namely, from

$$dF_p\left(\frac{\partial}{\partial x^i}\bigg|_p\right)y^j=a_{1i}\frac{\partial}{\partial y^1}\bigg|_{F(p)}y^j+\cdots+a_{ji}\frac{\partial}{\partial y^j}\bigg|_{F(p)}y^j+\cdots+a_{ni}\frac{\partial}{\partial y^n}\bigg|_{F(p)}y^j$$

by the definition of the dual basis the right-hand side leaves only $$a_{ji}$$, so

$$dF_p\left(\frac{\partial}{\partial x^i}\bigg|_p\right)y^j=a_{ji}$$

and from this we see that the matrix representation of $$dF_p$$ with respect to the two bases $$\partial/\partial x^i$$ and $$\partial/\partial y^j$$ is the matrix

$$\begin{pmatrix}\partial(y^1\circ F)/\partial x^1&\partial(y^1\circ F)/\partial x^2&\cdots&\partial(y^1\circ F)/\partial x^m\\\partial(y^2\circ F)/\partial x^1&\partial(y^2\circ F)/\partial x^2&\cdots&\partial(y^2\circ F)/\partial x^m\\\vdots&\vdots&\ddots&\vdots\\\partial(y^n\circ F)/\partial x^1&\partial(y^n\circ F)/\partial x^2&\cdots&\partial(y^n\circ F)/\partial x^m\end{pmatrix}$$

That is, this is nothing but the Jacobian of the function $$\psi\circ F\circ\varphi^{-1}$$ between Euclidean spaces.

In particular, if $$M=N$$ and $$F=\id_M$$ but we choose different coordinate systems $$(U, \varphi)$$ and $$(V,\psi)$$, this becomes the Jacobian matrix of the transition map $$\psi\circ\varphi^{-1}$$.


---

**References**

**[War]** Frank W. Warner. *Foundations of Differentiable Manifolds and Lie Groups*, Graduate texts in mathematics, Springer, 2013  
**[Lee]** John M. Lee. *Introduction to Smooth Manifolds*, Graduate texts in mathematics, Springer, 2012  

---

[^1]: Of course, for this $$\varphi^{-1}$$ must be $$C^\infty$$, but since the smooth structure on $$U$$ was transferred from the smooth structure on $$\varphi(U)$$ from the beginning, $$\varphi^{-1}$$ is even a diffeomorphism.
[^2]: For convenience we have assumed $$\psi(F(p))=0$$.
