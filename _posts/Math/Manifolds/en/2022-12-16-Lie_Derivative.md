---
title: "Lie Derivative"
description: "We define the Lie derivative of functions, vector fields, and differential forms on a manifold, and explain its geometric meaning through its relationship with the directional derivative expression along curves."
excerpt: "Lie derivative and Lie bracket"

categories: [Math / Manifolds]
permalink: /en/math/manifolds/Lie_derivative
sidebar: 
    nav: "manifolds-en"

date: 2022-12-16
weight: 13
translated_at: 2026-06-01T09:30:04+00:00
translation_source: kimi-cli
last_polished_at: 2026-10-21T03:15:06+00:00
translation_polish_source: antigravity-gemini-3.8-flash-high
---
## Directional Derivative of a Function and the Lie Derivative

Consider a function $f$ defined on a manifold $M$. By definition, the directional derivative of $f$ at a point $p\in M$ in the direction of $v\in T_pM$ is equal to $v(f)$. The chief reason we cannot use the *ordinary* derivative

$$\lim_{t \rightarrow0}\frac{f(p+tv)-f(p)}{t}$$

on $M$ is that $p+tv$ is not defined. However, if a suitable $C^\infty$ curve $\gamma$ on $M$ is given with $\gamma(0)=p$ and $\gamma'(0)=v$, then through the formula

$$\lim_{h\rightarrow 0}\frac{f(\gamma(h))-f(p)}{h}\tag{1}$$

we know that we can obtain the value of the directional derivative. ([§Examples of Differentials, ⁋Definition 1](/en/math/manifolds/examples_of_differentials#def1){: data-lid="4gvw6" }) 

Now suppose a vector field $X$ on $M$ is given, and consider the problem of finding the directional derivative $X_pf$ at each point $p$ in the direction of $X_p$. Geometrically, as above, this is equivalent to choosing, for every point $p$, a curve $\gamma_p$ satisfying $\gamma(0)=p$ and $\gamma'(0)=X_p$, and applying formula (1) above. But we know that a curve satisfying this property necessarily exists. ([§Vector Fields, ⁋Theorem 6](/en/math/manifolds/vector_fields#thm6){: data-lid="xfxlz" })

::: Definition 1
Fix a manifold $M$ and a vector field $X$ defined on it, let $\phi^t$ be the function defined by the integral flows of $X$, and suppose a function $f\in C^\infty(M)$ is given. Then the *Lie derivative* $\mathcal{L}_Xf$ of $f$ is the function defined by the formula

$$(\mathcal{L}_Xf)(p)=\lim_{t\rightarrow 0}\frac{f(\phi^t(p))-f(\phi^0(p))}{t}=\lim_{t\rightarrow 0}\frac{f(\phi^t(p))-f(p)}{t}$$
:::

Of course, by the preceding argument this is no different from the directional derivative $X_pf$. However, $\phi^t$ used here is not simply a function, but provides a way to differentiate everything else defined on $M$.

## Lie Derivative of Vector Fields

The simplest example is the derivative of a vector field. Since a vector field $Y$ is a function from $M$ to $TM$, one might attempt differentiation using a method similar to [Definition 1](#def1){: data-lid="axa3b" } above, but this is no easy task. There is a slightly more fundamental problem here than for the derivative of a function: while $Y(\phi^t(p))$ is an element of $T_{\phi^t(p)}M$, $Y(p)$ is an element of $T_pM$, so there is no way in the first place to compute their difference $Y_{\phi^t(p)}-Y_p$. 

Nevertheless, in our setting it is possible to differentiate this. Recalling [§Vector Fields, ⁋Theorem 6](/en/math/manifolds/vector_fields#thm6){: data-lid="0es5w" }, since $\phi^t$ is a diffeomorphism, $\dd{\phi}^t$ induces an isomorphism from $T_pM$ to $T_{\phi^t(p)}M$. Furthermore, from the same theorem we know that the inverse of this isomorphism is $\dd{\phi}^{-t}$. Therefore, by bringing $Y_{\phi^t(p)}$ to $T_pM$ via $\dd{\phi}^{-t}$, we can define it as follows.

::: Definition 2
Fix a manifold $M$ and a vector field $X$ defined on it, and suppose another vector field $Y:M\rightarrow TM$ is given. Then the *Lie derivative* $\mathcal{L}_XY$ of $Y$ is the vector field defined by the formula

$$(\mathcal{L}_XY)_p=\lim_{t\rightarrow 0}\frac{(\dd{\phi}^{-t})_{\phi^t(p)}(Y_{\phi^t(p)})-Y_p}{t}$$
:::

## Lie Derivative of Differential Forms

Of course, we can continue defining in this manner. For example, the following is the method for differentiating a differential form with respect to a vector field $X$.

::: Definition 3
Fix a manifold $M$ and a vector field $X$ defined on it, and suppose a differential form $\omega\in\Omega^\ast(M)$ is given. Then the *Lie derivative* $\mathcal{L}_X\omega$ of $\omega$ is the differential form defined by the formula

$$(\mathcal{L}_X\omega)_p=\frac{d}{\dd{t}}\bigg\vert_{t=0}(\phi^t)^\ast\omega_{\phi^t(p)}=\lim_{t\rightarrow 0}\frac{(\phi^t)^\ast\omega_{\phi^t(p)}-\omega_p}{t}$$
:::

Moreover, it is not difficult to extend this definition to arbitrary tensor fields. Since we will not need this immediately, we omit it.

Some parts of the following proposition have already been proved, and some are new, but we omit all proofs as they would be too lengthy to write out in full. (For the proof, see **[War]**.)

::: Proposition 4
For any $X\in\mathfrak{X}(M)$, the following hold.

1. For any $f\in C^\infty(M)$, $\mathcal{L}_Xf=X(f)$.
2. For any $Y\in \mathfrak{X}(M)$, $\mathcal{L}_XY=[X,Y]$.
3. $\mathcal{L}_X$ is a derivation from $\Omega^\ast(M)$ to $\Omega^\ast(M)$ and commutes with $d$.
4. $\mathcal{L}_X=\iota_X\circ d+d\circ\iota_X$.
5. For any $\omega\in\Omega^k(M)$ and $X_0, X_1,\ldots, X_k\in\mathfrak{X}(M)$,
    
    $$\mathcal{L}_{X_0}(\omega(X_1,\ldots, X_k))=(\mathcal{L}_{X_0}\omega)(X_1,\ldots, X_k)+\sum_{i=1}^k\omega(X_1,\ldots, X_{i-1}, \mathcal{L}_{X_0}X_i,X_{i+1},\ldots, X_k)$$

6. For any $\omega\in\Omega^k(M)$ and $X_0, X_1,\ldots, X_k\in\mathfrak{X}(M)$,

    $$\begin{aligned}\dd{\omega}(X_0,\ldots, X_k)&=\sum_{i=0}^k(-1)^iX_i\omega(X_0,\ldots, \hat{X}_i,\ldots, X_k)\\&\phantom{==}+\sum_{i<j}(-1)^{i+j}\omega([X_i, X_j], X_0,\ldots, \hat{X}_i,\ldots, \hat{X}_j,\ldots, X_k)\end{aligned}$$

In 5 and 6, the hat indicates that the given component is omitted.
:::

The first result of this proposition is something we have already verified. The $[-,-]$ appearing in the second and sixth results is an operation between vector fields called the *Lie bracket*; we only touch upon it briefly in this post and will treat it in detail in the next post. At any rate, the key point of the second, fifth, and sixth results is that when computing $\mathcal{L}_X$, one can obtain the Lie derivative through relatively simple algebraic computations alone, instead of following the original definition. The fourth result is known as Cartan's formula.

## Lie Bracket

In a general setting, $\mathfrak{X}(M)$ is not a $C^\infty(M)$-algebra. If we compute $(XY)(fg)$ directly,

$$(XY)(fg)=X(f(Yg)+g(Yf))=(Xf)(Yg)+f(XY)g+(Xg)(Yf)+g(XY)f\tag{2}$$

we can verify that this holds. In other words, what prevents $XY$ from satisfying the Leibniz rule is the two terms $(Xf)(Yg)$ and $(Xg)(Yf)$, and therefore we define the following.

::: Definition 5
For $X,Y\in\mathfrak{X}(M)$, $[X,Y]\in\mathfrak{X}(M)$ is the element defined by the formula

$$[X,Y]f=X(Yf)-Y(Xf)$$
:::

Of course, for this definition to make sense, one must verify that the expression on the right-hand side actually yields an element of $\mathfrak{X}(M)$, but this can be done by interchanging the roles of $X$ and $Y$ in formula (2) calculated above to obtain $(YX)(fg)$, and then subtracting. Since this definition was designed from the outset to eliminate the two problematic terms, the Leibniz rule will naturally hold. Also, that the $[X,Y]$ obtained in this way is a $C^\infty$ vector field follows by substituting $X(Yf)-Y(Xf)$ into the third condition of [§Vector Fields, ⁋Proposition 2](/en/math/manifolds/vector_fields#prop2){: data-lid="ha3ux" }.

The vector field $[X,Y]$ defined in this way is called the *Lie bracket* of $X$ and $Y$. Since this definition will be of great importance later, it seems worthwhile to collect a few results in advance.

Suppose that between two manifolds $M,N$, a $C^\infty$ map $F:M\rightarrow N$ is given. Then $\dd{F_p}:T_pM\rightarrow T_{F(p)}N$ is the map that sends, on $M$ at a point $p$, a tangent vector $v$ defined there to $N$ at the point $F(p)$ as the tangent vector $\dd{F_p}(v)$. In general, however, this need not be possible for vector fields. That is, even if a vector field on $M$, $X$, is given, one cannot produce through $\dd{F_p}$ or the like a vector field defined on $N$.

For instance, if $F$ is not surjective, there is no natural way, for a point outside the image of $F$, namely $q\in N$, to assign a tangent vector. Even if one resolves this by restricting the codomain or the like, if $F$ is not injective and $F(p_1)=F(p_2)=q\in N$, one must also decide, for the tangent vector at this common point $q$, which of $\dd{F_{p_1}} v_1$ and $\dd{F_{p_2}} v_2$ to choose.

Therefore, rather than attempting to move $X\in\mathfrak{X}(M)$ via $F$, it is wiser to examine the case in which an already given $Y\in\mathfrak{X}(N)$ satisfies the desired property.

::: Definition 6
Let $F:M\rightarrow N$ be a $C^\infty$ map. If $X\in\mathfrak{X}(M)$ and $Y\in\mathfrak{X}(N)$ satisfy the equation

$$\dd{F_p}(X_p)=Y_{F(p)}$$

for all $p\in M$, then $X$ and $Y$ are said to be *$F$-related*.
:::

In other words, $X$ and $Y$ being $F$-related means that the following diagram commutes.

{% diagram Math/Manifolds/Lie_Derivative-1.svg width="7.49em" alt="F-related" %}

Just as in [§Vector Fields, ⁋Proposition 2](/en/math/manifolds/vector_fields#prop2){: data-lid="eu3wt" } one can determine that $X$ is $C^\infty$ by applying it to each function $f$, whether $X$ and $Y$ are $F$-related can likewise be determined by applying them to each function.

::: Proposition 7
Let $F:M\rightarrow N$ be a $C^\infty$ map, and let $X\in\mathfrak{X}(M)$, $Y\in\mathfrak{X}(N)$. Then $X,Y$ are $F$-related if and only if for any open set $V\subseteq N$ and $f\in C^\infty(V)$, the equation

$$X(f\circ F)=(Yf)\circ F$$

holds.
:::
::: Proof
For any point $p\in M$,

$$X(f\circ F)(p)=X_p(f\circ F)=\dd{F_p}(X_p)f$$

and

$$((Yf)\circ F)(p)=(Yf)(F(p))=Y_{F(p)}f$$

Therefore, the two given conditions are equivalent.
:::

Earlier, we pointed out that if $F$ is neither surjective nor injective, finding through $F$, for $X\in\mathfrak{X}(M)$, an $F$-related $Y\in\mathfrak{X}(N)$ is not natural; however, if $F$ is a diffeomorphism, the following natural choice exists.

::: Proposition 8
If $F:M\rightarrow N$ is a diffeomorphism, then for each $X\in\mathfrak{X}(M)$, there exists a unique $Y\in\mathfrak{X}(N)$ such that $X,Y$ are $F$-related.
:::
::: Proof
For each $q\in N$, there exists a unique $p\in M$ such that $F(p)=q$. Thus, for each point $q\in N$, we define $Y$ by the formula

$$Y_q=\dd{F_p}(X_p)\qquad (F(p)=q)$$

Since the above formula must hold for $Y$, with respect to $X$, to be $F$-related, the uniqueness of such a $Y$ is obvious. Moreover, $Y:N\rightarrow TN$ is now the composition of the following $C^\infty$ maps

$$N\overset{F^{-1}}{\rightarrow}M\overset{X}{\rightarrow}TM\overset{\dd{F}}{\rightarrow}TN$$

and therefore $Y$ is $C^\infty$.
:::

::: Proposition 9
Let $F:M\rightarrow N$ be $C^\infty$. If for $i=1,2$ we have $X_i\in\mathfrak{X}(M)$, $Y_i\in\mathfrak{X}(N)$, and $X_i$ and $Y_i$ are $F$-related, then $[X_1,X_2]$ is $F$-related to $[Y_1,Y_2]$.
:::
::: Proof
We must show that the formula

$$\dd{F_p}([X_1,X_2]_p)=[Y_1,Y_2]_{F(p)}$$

holds for all $p$. Now for any function $f$ defined in a neighborhood of $F(p)$,

$$\begin{aligned}\dd{F_p}([X_1,X_2]_p)f&=[X_1,X_2]_p(f\circ F)\\
&=(X_1)_p(X_2(f\circ F))-(X_2)_p(X_1(f\circ F))\\
&=(X_1)_p((Y_2f)\circ F)-(X_2)_p((Y_1f)\circ F)\\
&=\dd{F_p}\bigl((X_1)_p\bigr)(Y_2f)-\dd{F_p}\bigl((X_2)_p\bigr)(Y_1f)\\
&=(Y_1)_{F(p)}(Y_2f)-(Y_2)_{F(p)}(Y_1f)\\
&=[Y_1,Y_2]_{F(p)}f\end{aligned}$$

so we obtain the desired conclusion.
:::

---

**References**

**[War]** Frank W. Warner. *Foundations of Differentiable Manifolds and Lie Groups*, Graduate texts in mathematics, Springer, 2013  
**[Lee]** John M. Lee. *Introduction to Smooth Manifolds*, Graduate texts in mathematics, Springer, 2012

---
