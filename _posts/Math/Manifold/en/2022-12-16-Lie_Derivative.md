---
title: "Lie Derivative"
excerpt: "Lie derivative and Lie bracket"

categories: [Math / Manifold]
permalink: /en/math/manifold/Lie_derivative
header:
    overlay_image: /assets/images/Math/Manifold/Lie_Derivative.png
    overlay_filter: 0.5
sidebar: 
    nav: "manifold-en"

date: 2022-12-16
last_modified_at: 2022-12-16
weight: 14
translated_at: 2026-05-28T11:36:15+00:00
translation_source: kimi-cli
---
## Directional Derivative of a Function and the Lie Derivative

Consider a function $$f$$ defined on a manifold $$M$$. By definition, the directional derivative of $$f$$ at a point $$p\in M$$ in the direction of $$v\in T_pM$$ is equal to $$v(f)$$. The main reason we cannot use the usual differential

$$\lim_{t \rightarrow0}\frac{f(p+tv)-f(p)}{t}$$

on $$M$$ is that $$p+tv$$ is not defined. However, if an appropriate $$C^\infty$$ curve $$\gamma$$ on $$M$$ is given with $$\gamma(0)=p$$ and $$\gamma'(0)=v$$, then we know that the value of the directional derivative can be computed by the formula

$$\lim_{h\rightarrow 0}\frac{f(\gamma(h))-f(p)}{h}\tag{1}$$

([§Examples of Differentials, ⁋Definition 1](/en/math/manifold/examples_of_differentials#def1)) 

Now suppose a vector field $$X$$ on $$M$$ is given, and consider the problem of finding the directional derivative $$X_pf$$ at each point $$p$$ in the direction of $$X_p$$. Geometrically, this is equivalent to choosing, for each point $$p$$, a curve $$\gamma_p$$ satisfying $$\gamma(0)=p$$ and $$\gamma'(0)=X_p$$, and applying formula (1) above. But we know that such a curve satisfying this property always exists. ([§Vector Fields, ⁋Theorem 6](/en/math/manifold/vector_fields#thm6))

<div class="definition" markdown="1">
 
<ins id="def1">**Definition 1**</ins> Fix a manifold $$M$$ and a vector field $$X$$ defined on it, and suppose a function $$f:M\rightarrow\mathbb{R}$$ is given. Then the *Lie derivative* $$\mathcal{L}_Xf$$ of $$f$$ is the function defined by the formula

$$(\mathcal{L}_Xf)(p)=\lim_{t\rightarrow 0}\frac{f(\phi^t(p))-f(\phi^0(p))}{t}=\lim_{t\rightarrow 0}\frac{f(\phi^t(p))-f(p)}{t}$$

</div> 

Of course, by the preceding argument this is none other than the directional derivative $$X_pf$$. However, the $$\phi^t$$ used here provides not merely a way to differentiate functions, but a way to differentiate everything else defined on $$M$$.

## Lie Derivative of Vector Fields

The simplest example is the derivative of a vector field. Since a vector field $$Y$$ is a map from $$M$$ to $$TM$$, one might attempt to differentiate it using a method similar to [Definition 1](#def1) above, but this is no trivial matter. There is a more fundamental issue here than for functions: $$Y(\phi^t(p))$$ is an element of $$T_{\phi^t(p)}$$, whereas $$Y(p)$$ is an element of $$T_pM$$, so there is no way to compute their difference $$Y_{\phi^t(p)}-Y_p$$ to begin with. 

Nevertheless, it is possible to differentiate it in our situation. Recalling [§Vector Fields, ⁋Theorem 6](/en/math/manifold/vector_fields#thm6), since $$\phi^t$$ is a diffeomorphism, $$d\phi^t$$ induces an isomorphism from $$T_pM$$ to $$T_{\phi^t(p)}$$. Moreover, from the same theorem we also know that the inverse of this isomorphism is $$d\phi^{-t}$$. Therefore, by pulling $$Y_{\phi^t(p)}$$ back to $$T_pM$$ via $$d\phi^{-t}$$, we can define it as follows.

<div class="definition" markdown="1">

<ins id="def2">**Definition 2**</ins> Fix a manifold $$M$$ and a vector field $$X$$ defined on it, and suppose another vector field $$Y:M\rightarrow TM$$ is given. Then the *Lie derivative* $$\mathcal{L}_XY$$ of $$Y$$ is the vector field defined by the formula

$$(\mathcal{L}_XY)_p=\lim_{t\rightarrow 0}\frac{(d\phi^{-t})_{\phi^t(p)}(Y_{\phi^t(p)})-Y_p}{t}$$

</div>

## Lie Derivative of Differential Forms

Of course, we can continue defining derivatives in this manner. For example, the following is the method for differentiating a differential form with respect to a vector field $$X$$.

<div class="definition" markdown="1">

<ins id="def3">**Definition 3**</ins> Fix a manifold $$M$$ and a vector field $$X$$ defined on it, and suppose a differential form $$\omega\in\Omega^\ast(M)$$ is given. Then the *Lie derivative* $$\mathcal{L}_X\omega$$ of $$\omega$$ is the differential form defined by the formula

$$(\mathcal{L}_X\omega)_p=\frac{d}{dt}\bigg|_{t=0}(\phi^t)^\ast\omega_{\phi^t(p)}=\lim_{t\rightarrow 0}\frac{(\phi^t)^\ast\omega_{\phi^t(p)}-\omega_p}{t}$$

</div>

Moreover, it is not difficult to extend this definition to arbitrary tensor fields. Since this is not something we will use right away, we skip it.

Some parts of the following proposition have already been proved, and some are new, but we omit the proofs as writing them all out would be too lengthy.

<div class="proposition" markdown="1">

<ins id="prop4">**Proposition 4**</ins> For any $$X\in\mathfrak{X}(M)$$, the following hold.

1. For any $$f\in C^\infty(M)$$, we have $$\mathcal{L}_Xf=X(f)$$.
2. For any $$Y\in \mathfrak{X}(M)$$, we have $$\mathcal{L}_XY=[X,Y]$$.
3. $$\mathcal{L}_X$$ is a derivation on $$\Omega^\ast(M)$$ and commutes with $$d$$.
4. $$\mathcal{L}_X=\iota_X\circ d+d\circ\iota_X$$.
5. For any $$\omega\in\Omega^k(M)$$ and $$X_0, X_1,\ldots, X_k\in\mathfrak{X}(M)$$,
    
    $$\mathcal{L}_{X_0}(\omega(X_1,\ldots, X_k))=(\mathcal{L}_{X_0}\omega)(X_1,\ldots, X_k)+\sum_{i=1}^k\omega(X_1,\ldots, X_{i-1}, \mathcal{L}_{X_0}X_i,X_{i+1},\ldots, X_k)$$

6. For any $$\omega\in\Omega^k(M)$$ and $$X_0, X_1,\ldots, X_k\in\mathfrak{X}(M)$$,

    $$\begin{aligned}d\omega(X_0,\ldots, X_k)&=\sum_{i=0}^k(-1)^iX_i\omega(X_0,\ldots, \hat{X}_i,\ldots, X_k)\\&\phantom{==}+\sum_{i<j}(-1)^{i+j}\omega([X_i, X_j], X_0,\ldots, \hat{X}_i,\ldots, \hat{X}_j,\ldots, X_k)\end{aligned}$$

In 5 and 6, the hat indicates that the corresponding entry is omitted.

</div>

The first result of this proposition is something we have already verified. The bracket $$[-,-]$$ appearing in the second and sixth results is an operation between vector fields called the *Lie bracket*; we will only briefly touch upon it in this post and cover the details in the next post. In any case, the key point of the second, fifth, and sixth results is that when computing $$\mathcal{L}_X$$, one can obtain the Lie derivative through relatively simple algebraic computations instead of following the original definition. The fourth result is known as Cartan's formula.

## Lie Bracket

$$\mathfrak{X}(M)$$ is not a $$C^\infty(M)$$-algebra in general. Computing $$(XY)(fg)$$ directly, we find that

$$(XY)(fg)=X(f(Yg)+g(Yf))=(Xf)(Yg)+f(XY)g+(Xg)(Yf)+g(XY)f\tag{2}$$

In other words, the two terms $$(Xf)(Yg)$$ and $$(Xg)(Yf)$$ are what prevent $$XY$$ from satisfying the Leibniz rule, and therefore we define the following.

<div class="definition" markdown="1">

<ins id="def5">**Definition 5**</ins> For $$X,Y\in\mathfrak{X}(M)$$, the element $$[X,Y]\in\mathfrak{X}(M)$$ is defined by the formula

$$[X,Y]f=X(Yf)-Y(Xf)$$

</div>

Of course, for this definition to make sense we must verify that the right-hand side actually gives an element of $$\mathfrak{X}(M)$$, but this can be done by swapping the roles of $$X$$ and $$Y$$ in formula (2) above to obtain $$(YX)(fg)$$, and then subtracting. Since this definition was designed from the outset to cancel the two problematic terms, the Leibniz rule will naturally hold.

The vector field $$[X,Y]$$ defined in this way is called the *Lie bracket* of $$X$$ and $$Y$$. Since this definition will be very important later, it seems worthwhile to collect a few results in advance.

Suppose a $$C^\infty$$ map $$F:M\rightarrow N$$ between two manifolds $$M$$ and $$N$$ is given. Then $$dF_p:T_pM\rightarrow T_{F(p)}N$$ is the map that sends a tangent vector $$v$$ defined at a point $$p$$ of $$M$$ to the tangent vector $$dF_p(v)$$ defined at the point $$F(p)$$ of $$N$$. However, this is not generally possible for vector fields. That is, even if a vector field $$X$$ defined on $$M$$ is given, we cannot use $$dF_p$$, etc., to create a vector field defined on $$N$$.

For example, if $$F$$ is not surjective, there is no natural way to assign a tangent vector at a point $$q\in N$$ that does not belong to the image of $$F$$. Even if we resolve this by restricting the codomain, for instance, if $$F$$ is not injective and $$F(p_1)=F(p_2)=q\in N$$, we would also have to decide which of $$dF_{p_1} v_1$$ and $$dF_{p_2} v_2$$ to choose as the tangent vector at this common point $$q$$.

Therefore, rather than trying to push $$X\in\mathfrak{X}(M)$$ forward through $$F$$, it is wiser to look for an already given $$Y\in\mathfrak{X}(N)$$ that satisfies the desired property.

<div class="definition" markdown="1">

<ins id="def6">**Definition 6**</ins> Let $$F:M\rightarrow N$$ be a $$C^\infty$$ map. If $$X\in\mathfrak{X}(M)$$ and $$Y\in\mathfrak{X}(N)$$ satisfy the equation

$$dF_p(X_p)=Y_{F(p)}$$

for all $$p\in M$$, then we say that $$X$$ and $$Y$$ are *$$F$$-related*.

</div>

In other words, $$X$$ and $$Y$$ being $$F$$-related means that the following diagram commutes.

![F-related](/assets/images/Math/Manifold/Lie_Derivative-1.png){:style="width:7.4em" class="invert" .align-center}

As we can see by applying the fact that $$X$$ is $$C^\infty$$ (from [Proposition 2](#prop2)) to each function $$f$$, whether $$X$$ and $$Y$$ are $$F$$-related can also be determined by applying them to each function.

<div class="proposition" markdown="1">

<ins id="prop7">**Proposition 7**</ins> Let $$F:M\rightarrow N$$ be a $$C^\infty$$ map, and let $$X\in\mathfrak{X}(M)$$ and $$Y\in\mathfrak{X}(N)$$. Then $$X$$ and $$Y$$ are $$F$$-related if and only if for any $$f$$,

$$X(f\circ F)=(Yf)\circ F$$

</div>
<details class="proof" markdown="1">
<summary>Proof</summary>

For any point $$p\in M$$,

$$X(f\circ F)(p)=X_p(f\circ F)=dF_p(X_p)f$$

and

$$((Yf)\circ F)(p)=(Yf)(F(p))=Y_{F(p)}f$$

Therefore the two given conditions are equivalent.

</details>

At first we pointed out that if $$F$$ is neither surjective nor injective, it is not natural to find a $$Y\in\mathfrak{X}(N)$$ that is $$F$$-related to a given $$X\in\mathfrak{X}(M)$$ through $$F$$; however, if $$F$$ is a diffeomorphism, then the following natural choice exists.

<div class="proposition" markdown="1">

<ins id="prop8">**Proposition 8**</ins> If $$F:M\rightarrow N$$ is a diffeomorphism, then for every $$X\in\mathfrak{X}(M)$$ there exists a unique $$Y\in\mathfrak{X}(N)$$ such that $$X$$ and $$Y$$ are $$F$$-related.

</div>
<details class="proof" markdown="1">
<summary>Proof</summary>

For each $$q\in N$$ there exists a unique $$p\in M$$ such that $$F(p)=q$$. Thus, for each point $$q\in N$$, we define $$Y$$ by the formula

$$Y_q=dF_p(X_p)\qquad (F(p)=q)$$

Since the above formula must hold for $$Y$$ to be $$F$$-related to $$X$$, the uniqueness of such a $$Y$$ is obvious. Moreover, $$Y:N\rightarrow TN$$ is now the composition of the following $$C^\infty$$ maps

$$N\overset{F^{-1}}{\longrightarrow}M\overset{X}{\longrightarrow}TM\overset{dF}{\longrightarrow}TN$$

and therefore $$Y$$ is $$C^\infty$$.

</details>

<div class="proposition" markdown="1">

<ins id="prop9">**Proposition 9**</ins> Let $$F:M\rightarrow N$$ be a $$C^\infty$$ map. If for $$i=1,2$$ we have $$X_i\in\mathfrak{X}(M)$$, $$Y_i\in\mathfrak{X}(N)$$, and $$X_i$$ and $$Y_i$$ are $$F$$-related, then $$[X_1,X_2]$$ is $$F$$-related to $$[Y_1,Y_2]$$.

</div>
<details class="proof" markdown="1">
<summary>Proof</summary>

We must show that the formula

$$dF_p([X_1,X_2]_p)=[Y_1,Y_2]_{F(p)}$$

holds for all $$p$$. Now for any function $$f$$ defined in a neighborhood of $$F(p)$$,

$$\begin{aligned}dF_p([X_1,X_2]_p)f&=[X_1,X_2]_p(f\circ F)\\
&=(X_1)_p(X_2(f\circ F))-(X_2)_p(X_1(f\circ F))\\
&=(X_1)_p((Y_2f)\circ F)-(X_2)_p((Y_1f)\circ F)\\
&=dF_p(X_1)_p(Y_2f)-dF_p(X_2)_p(Y_1f)\\
&=(Y_1)_{F(p)}(Y_2f)-(Y_2)_{F(p)}(Y_1f)\\
&=[Y_1,Y_2]_{F(p)}f\end{aligned}$$

Thus we obtain the desired conclusion.

</details>

---

**References**

**[War]** Frank W. Warner. *Foundations of Differentiable Manifolds and Lie Groups*, Graduate texts in mathematics, Springer, 2013  
**[Lee]** John M. Lee. *Introduction to Smooth Manifolds*, Graduate texts in mathematics, Springer, 2012  

---
