---
title: "Root Systems"
description: "This post characterizes simple and semisimple Lie algebras through the properties of the Killing form defined on the adjoint representation of a Lie algebra, and covers the foundations of root systems."
excerpt: "Root systems obtained from the weight decomposition of the adjoint representation"

categories: [Math / Lie Theory]
permalink: /en/math/lie_theory/root_systems
sidebar: 
    nav: "Lie_theory-en"

date: 2025-11-12
weight: 3
translated_at: 2026-05-31T16:30:04+00:00
translation_source: kimi-cli
last_polished_at: 2026-10-12T07:15:06+00:00
translation_polish_source: antigravity-gemini-3.8-flash-high
---
## Adjoint representation

Every Lie group carries a natural (finite-dimensional) representation $\Ad: G \rightarrow \Aut(\mathfrak{g})$. ([§Lie Groups, ⁋Definition 19](/en/math/lie_theory/Lie_groups#def19){: data-lid="n5zii" }) For each $g\in G$, this is the differential of the conjugation $h\mapsto ghg^{-1}$ at $h=e$, and if we regard both $G$ and $\Aut(\mathfrak{g})$ as Lie groups and differentiate this map, we obtain a representation of $\mathfrak{g}$

$$\ad: \mathfrak{g}\rightarrow \Lie(\Aut(\mathfrak{g}))$$

and considering [§Lie Groups, ⁋Theorem 15](/en/math/lie_theory/Lie_groups#thm15){: data-lid="rakza" }, we may essentially regard all the information known to $\Ad$ as being contained here. In any case, considering the Lie algebra of a vector space is the same as considering the space itself, so we can think of representing $\mathfrak{g}$ using the representation space $\mathfrak{g}$, and here $\ad$ can be computed explicitly via

$$\ad(X)Y=[X,Y]$$

What was important in using the results of representation theory was that any finite-dimensional representation is always unitary. The argument used to prove this result was that on $V$, we can choose a $G$-invariant inner product; strictly speaking, since we are interested in the orthogonal complement, having just a non-degenerate symmetric form is sufficient. However, on a Lie algebra there exists a natural bilinear form.

::: Definition 1
The symmetric bilinear form on a Lie algebra $\mathfrak{g}$ defined by the formula

$$K(X,Y)=\tr(\ad(X)\ad(Y))$$

is called the *Killing form*.
:::

That the Killing form is symmetric and $\mathbb{C}$-bilinear is obvious by definition. Even without any special manipulation, this Killing form is already invariant under the adjoint action by $G$. That is, the formula

$$K(\Ad_g(X), \Ad_g(Y))=K(X,Y)$$

holds, and differentiating this at $g=e$ in the direction of $Z$ yields the following $\ad$-invariance:

$$0=\frac{d}{\dd{t}}\bigg\vert_{t=0}K(\Ad_{\exp(tZ)}X, \Ad_{\exp(tZ)}Y)=K([Z,X],Y)+K(X,[Z,Y])$$

What remains is the condition for this to be non-degenerate.

::: Definition 2
For a Lie algebra $\mathfrak{g}$, being *simple* means that $\mathfrak{g}$ is a non-abelian Lie algebra and the only ideals of $\mathfrak{g}$ are $0$ and itself. A Lie algebra that can be written as a direct sum of simple Lie algebras is called *semisimple*.
:::

Then the following holds.

::: Proposition 3
For a finite-dimensional Lie algebra $\mathfrak{g}$, the following are all equivalent.

1. $\mathfrak{g}$ is semisimple.
2. The Killing form is non-degenerate.
3. $\mathfrak{g}$ has no nonzero abelian ideal.
4. $\mathfrak{g}$ has no nonzero solvable ideal.
5. The radical of $\mathfrak{g}$ is $0$.
:::

Since the proof of this is not immediately important, we skip it.

## Cartan subalgebra

One of the most powerful tools in linear algebra was diagonalization, and in Lie groups we captured this through weight decomposition. ([§Torus Actions, ⁋Definition 4](/en/math/lie_theory/torus_action#def4){: data-lid="59165" }) The corresponding notion for Lie algebras is as follows.

::: Definition 4
For a semisimple Lie algebra $\mathfrak{g}$, a *Cartan subalgebra* of $\mathfrak{g}$ is one such that $\ad(H)$ is diagonalizable for all $H\in \mathfrak{h}$, maximal among abelian subalgebras $\mathfrak{h}$.
:::

Since two diagonalizable operators $A,B$ are simultaneously diagonalizable if and only if they commute, by definition all elements of $\mathfrak{h}$ are simultaneously diagonalizable. Now, using the family $\{H\in \mathfrak{h}\}$ of simultaneously diagonalizable operators, let us decompose $\mathfrak{g}$. If a <em>finite</em> family of simultaneously diagonalizable operators $A_1,\ldots, A_n$ is given, decomposing the space into simultaneous eigenspaces takes the form

$$V=\bigoplus V_\alpha,\qquad \text{$A_i v_\alpha=\lambda_i v_\alpha$ for all $v_\alpha\in V_\alpha$ for all $i$}$$

but in our present situation, since $\mathfrak{h}$ is a vector space, it is better to choose a linear functional $\alpha: \mathfrak{h}\rightarrow \mathbb{C}$ and let $\alpha(H)$ play the role of the eigenvalue for each $H$. Thus we define as follows.

::: Definition 5
For a semisimple Lie algebra $\mathfrak{g}$ and $\mathfrak{g}$'s Cartan subalgebra $\mathfrak{h}$, the elements of

$$\Phi=\left\{\alpha\in \mathfrak{h}^\ast\setminus\{0\}\mid \mathfrak{g}_\alpha\neq 0\right\}$$

are called the *roots* of $\mathfrak{g}$. Here,

$$\mathfrak{g}_\alpha=\left\{X\in \mathfrak{g}\mid [H,X]=\alpha(H)X\text{ for all $H\in \mathfrak{h}$}\right\}$$

([§Lie Groups, ⁋Definition 19](/en/math/lie_theory/Lie_groups#def19){: data-lid="c0h8n" })
:::

By definition, $\mathfrak{h}$ acts on itself by $0$. That is, $\mathfrak{h}$ is, when $\mathfrak{g}$ is decomposed into simultaneous eigenspaces, the part corresponding to eigenvalue $0$, and from this we obtain the following decomposition:

$$\mathfrak{g}=\mathfrak{h}\oplus\bigoplus_{\alpha\in \Phi}\mathfrak{g}_\alpha$$

That these satisfy the following proposition is obvious.

::: Proposition 6
Consider a semisimple Lie algebra $\mathfrak{g}$, a Cartan subalgebra $\mathfrak{h}$, and its root decomposition

$$\mathfrak{g}=\mathfrak{h}\oplus\bigoplus_{\alpha\in\Phi}\mathfrak{g}_\alpha$$

and let $K(-,-)$ be the Killing form on $\mathfrak{g}$. The following hold.

1. For any $\alpha,\beta\in \Phi$, $[\mathfrak{g}_\alpha,\mathfrak{g}_\beta]\subseteq \mathfrak{g}_{\alpha+\beta}$ holds.
2. If $\alpha+\beta\neq 0$, then $\mathfrak{g}_\alpha$ and $\mathfrak{g}_\beta$ are orthogonal with respect to $K$.
3. The restriction of the Killing form to $\mathfrak{g}_\alpha\otimes \mathfrak{g}_{-\alpha}$ is a nondegenerate pairing.
:::
::: Proof
1. For any $X\in \mathfrak{g}_\alpha, Y\in \mathfrak{g}_\beta$, and $H\in \mathfrak{h}$,
    
    $$[H,[X,Y]]=[[H,X],Y]+[X,[H,Y]]=[\alpha(H)X,Y]+[X,\beta(H)Y]=(\alpha+\beta)(H)[X,Y]$$

    holds.
2. For any $X\in \mathfrak{g}_\alpha, Y\in \mathfrak{g}_\beta$, and $H\in \mathfrak{h}$, from the $\ad$-invariance of $K$,
    
    $$0=K([H,X],Y)+K(X,[H,Y])=K(\alpha(H)X,Y)+K(X,\beta(H)Y)=(\alpha+\beta)(H)K(X,Y)$$

    is obtained. If $\alpha+\beta\neq 0$, then for this equation to always hold, $K(X,Y)=0$ must always hold.
3. Since the Killing form is non-degenerate on $\mathfrak{g}$, whenever an arbitrary $X\in \mathfrak{g}_\alpha$ is given, there exists $Z\in \mathfrak{g}$ such that $K(X,Z)\neq 0$. What we must show is that we can choose $Z\in \mathfrak{g}_{-\alpha}$. This is clear because, after taking the root decomposition of $Z$, by the second result the components corresponding to the remaining parts other than $-\alpha$ give $0$ anyway when paired with $X$.
:::

## Example: $\sl(2;\mathbb{C})$

We know from [§Lie Groups, ⁋Proposition 12](/en/math/lie_theory/Lie_groups#prop12){: data-lid="onk9i" } that $\sl(n;\mathbb{C})$ is the set of $n\times n$ *traceless* matrices. Thus $\sl(2;\mathbb{C})$ has the following three elements as a basis:

$$H=\begin{pmatrix}1&0\\0&-1\end{pmatrix},\quad E=\begin{pmatrix}0&1\\0&0\end{pmatrix},\quad F=\begin{pmatrix}0&0\\1&0\end{pmatrix}$$

Therefore, the multiplication structure of $\sl(2;\mathbb{C})$ is obtained through the following commutation relations:

$$[H,E]=2E,\quad [H,F]=-2F,\quad [E,F]=H$$

We show that any $\sl(2;\mathbb{C})$-representation decomposes as a direct sum of irreducible representations. Remember that while this is a trivial result for compact Lie groups, for non-compact groups such as $\SL(n;\mathbb{C})$ the existence of a Haar measure is not guaranteed, and therefore ideas such as averaging an inner product via integration cannot be used.

Suppose an arbitrary finite-dimensional $\sl_2$-representation $V$ is given, and for each $\lambda\in \mathbb{C}$ define the weight space

$$V_\lambda=\{v\in V\mid H\cdot v=\lambda v\}$$

Then, by the commutation relations examined above,

$$E\cdot V_\lambda\subseteq V_{\lambda+2},\qquad F\cdot V_\lambda\subseteq V_{\lambda-2}$$

holds. For this reason, we also call $E,F$ the *raising operator* and *lowering operator*, respectively. On the other hand, since $V$ is finite-dimensional, if we consider the weight decomposition

$$V=\bigoplus_{\lambda} V_\lambda$$

there exists $\mu$ such that $V_\mu\neq 0$ but $V_{\mu+2}=0$ holds. Such a $\mu$ is called a *highest weight*, and an element of $V_\mu$ is called a *highest weight vector*. Then, for a highest weight vector $v$, we know that the following two equations

$$H\cdot v=\mu v,\qquad E\cdot v=0$$

hold.

::: Proposition 7
For any highest weight vector $v_0\in V_\mu$, if we define

$$v_j=\frac{1}{j!}F^j v_0$$

then the following hold:

$$H\cdot v_j=(\mu-2j)v_j,\quad F\cdot v_j=(j+1)v_{j+1},\quad E\cdot v_j=(\mu-j+1)v_{j-1}.$$
:::
::: Proof
The first two identities are obvious, so it suffices to show the identity for $E$. We proceed by induction. The case $j=0$ is obvious, and if the given identity holds for $j$, then

$$E\cdot v_{j+1}=\frac{1}{j+1}EF\cdot v_j=\frac{1}{j+1}(FE+H)\cdot v_j$$

and since by the induction hypothesis

$$E\cdot v_j=(\mu-j+1)v_{j-1}$$

and from the identity for $H$ we have $H\cdot v_j=(\mu-2j)v_j$, substituting these yields the desired result.
:::

Meanwhile, since $V$ is finite-dimensional, there exists a smallest integer $m$ such that $v_{m+1}=0$. Then for such $m$, from

$$0=E\cdot v_{m+1}=(\mu-m)v_m$$

and the minimality of $m$, we see that $\mu=m$ must hold. That is, the highest weight must be a non-negative integer.

::: Definition 8
For a fixed integer $m\geq 0$, we define the representation $V(m)$ of $\sl_2$ by specifying the $m+1$ vectors $v_0,\ldots, v_m$ and the action from [Proposition 7](#prop7){: data-lid="0dei6" }:

$$H\cdot v_j=(m-2j)v_j,\quad F\cdot v_j=(j+1)v_{j+1},\quad E\cdot v_j=(m-j+1)v_{j-1}$$

Here $v_{-1}=v_{m+1}=0$.
:::

It is not difficult to show that $V(m)$ is irreducible. Now for an arbitrary $\sl_2$-representation $V$, we can find the highest weight of $V$ and apply [Proposition 7](#prop7){: data-lid="wrcjp" } to the highest weight vector; if any highest weight vectors remain, we repeat this process, thereby decomposing $V$ into irreducible $\sl_2$-representations.

## Root systems

The above example of $\sl_2$-representations plays a major role in what follows. First let us define the following.

::: Definition 9
Fix a finite-dimensional vector space $V$ and an inner product $( -,-)$ defined on it. A finite set $\Phi$ of non-zero vectors in $V$ is called a *root system* if the following conditions are satisfied.

1. The elements of $\Phi$ span $V$.
2. If $\alpha\in \Phi$ and $c\in \mathbb{R}$, then $c\alpha\in \Phi$ only if $c=\pm 1$.
3. For each root $\alpha\in\Phi$, $\Phi$ is closed under the reflection $s_\alpha$ in the hyperplane perpendicular to $\alpha$. That is, for any $\alpha,\beta\in \Phi$,
    
    $$s_\alpha(\beta):=\beta-2\frac{(\beta,\alpha)}{(\alpha,\alpha)}\alpha\in \Phi$$

    holds.
4. For any roots $\alpha,\beta\in\Phi$, the expression
    
    $$\langle \beta,\alpha\rangle:=2\frac{(\beta,\alpha)}{(\alpha,\alpha)}$$

    is always an integer.
:::

Now fix a Cartan subalgebra $\mathfrak{h}$ of a semisimple complex Lie algebra $\mathfrak{g}$. Then first the following holds.

::: Lemma 10
For a semisimple Lie algebra $\mathfrak{g}$, a Cartan subalgebra $\mathfrak{h}$, and the root decomposition

$$\mathfrak{g}=\mathfrak{h}\oplus\bigoplus_{\alpha\in \Phi} \mathfrak{g}_\alpha$$

the following hold.

1. For any $\alpha,\beta\in \Phi$, $[\mathfrak{g}_\alpha,\mathfrak{g}_\beta]\subseteq \mathfrak{g}_{\alpha+\beta}$ holds.
2. If $\alpha+\beta\neq 0$, then $\mathfrak{g}_\alpha$ and $\mathfrak{g}_\beta$ are orthogonal.
3. The restriction of the Killing form defined on $\mathfrak{g}$ to $\mathfrak{h}$ is non-degenerate.
4. The Killing form defined on $\mathfrak{g}$ is non-degenerate when restricted to $\mathfrak{g}_\alpha\times \mathfrak{g}_{-\alpha} \rightarrow \mathbb{C}$.
:::
::: Proof
The first claim is obvious. For the second claim, for any $X_\alpha\in \mathfrak{g}_\alpha,X_\beta\in \mathfrak{g}_\beta$ and any $H\in \mathfrak{h}$, from $K$'s $\ad$-invariance we obtain the equation

$$0=K([H,X_\alpha],X_\beta)+K(X_\alpha, [H,X_\beta])=K(\alpha(H)X_\alpha, X_\beta)+K(X_\alpha,\beta(H)X_\beta)=(\alpha+\beta)(H)K(X_\alpha,X_\beta)$$

Therefore, if $\alpha+\beta\neq 0$, then $\mathfrak{g}_\alpha$ and $\mathfrak{g}_\beta$ are orthogonal with respect to $K$.

Now to show the third claim, recall that for any nonzero $H\in \mathfrak{h}$, there exists $X\in \mathfrak{g}$ such that $K(H,X)\neq 0$. What we newly need to show is that we can choose $X$ from $\mathfrak{h}$. To this end, writing $X$ in the form of a root decomposition $\sum X_\alpha$, by the above result we know that when taking $K(H,-)$, except for $X_0\in \mathfrak{h}$, all $X_\alpha$ give $0$. Hence $K(H,X_0)\neq 0$.

The fourth claim is proved in exactly the same way as the third.
:::

Now, since the Killing form defined on $\mathfrak{g}$ is non-degenerate on $\mathfrak{h}$ as well, the following isomorphism induced from this

$$\mathfrak{h}\rightarrow \mathfrak{h}^\ast;\qquad H\mapsto K(H, -)$$

exists. Then $\Phi\subseteq \mathfrak{h}^\ast$ is a spanning set of $\mathfrak{h}^\ast$. Suppose that as a linear combination of elements of $\Phi$, an element of $\mathfrak{h}^\ast$ cannot be expressed; then the corresponding element of $\mathfrak{h}$ must, for all $\alpha\in \Phi$, satisfy $\alpha(H)=0$. Now for any root space $\mathfrak{g}_\alpha$, $H$ acts by

$$[H,X]=\alpha(H)X=0\qquad\text{for all $X\in \mathfrak{g}_\alpha$}$$

and since $\mathfrak{h}$ is abelian, $H$ acts on it by $0$. That is, considering the root decomposition of $\mathfrak{g}$, $H$ acts on every element of $\mathfrak{g}$ by $0$, and from this we know that $H$ commutes with every element of $\mathfrak{g}$ under the Lie bracket. However, by [Proposition 3](#prop3){: data-lid="w0dv2" }, $\mathfrak{g}$ cannot have a nonzero abelian ideal, and in particular $Z(\mathfrak{g})=0$ must hold, so $H=0$.

From this we know that $\Phi$ spans $\mathfrak{h}^\ast$. However, $\mathfrak{h}^\ast$ is a complex vector space, and the Killing form defined on it is not guaranteed to be positive definite, so it is not an inner product. To resolve this, we consider the real span of the dual elements of $\Phi$ and show that the restriction of the Killing form to it becomes positive-definite. This requires a slightly more detailed analysis of the root decomposition.

For each root $\alpha\in\Phi$, by the non-degeneracy of the Killing form, the following equation

$$\alpha(X)=K(H_\alpha,X)\qquad\text{for all $X\in \mathfrak{h}$}$$

is satisfied by some $H_\alpha\in \mathfrak{h}$. Our first observation is the following lemma.

::: Lemma 11
For any $E\in \mathfrak{g}_\alpha$ and $F\in \mathfrak{g}_{-\alpha}$, we have $[E,F]=K(E,F)H_\alpha$.
:::
::: Proof
By the invariance of $K$ under $\ad$,

$$K([E,F],H)=K(F,[H,E])$$

holds for all $H\in \mathfrak{h}$. On the other hand, since $E\in \mathfrak{g}_\alpha$,

$$[H,E]=\alpha(H)E=K(H_\alpha,H)E$$

and substituting this into the above identity gives

$$K([E,F],H)=K(F,[H,E])=K(F, K(H_\alpha,H)E)=K(H_\alpha,H)K(F,E)=K(K(F,E)H_\alpha,H)$$

which holds for all $H$, yielding the desired result.
:::

On the other hand, from [Lemma 10](#lem10){: data-lid="4edh1" } we can choose $E\in \mathfrak{g}_\alpha$ and $F\in \mathfrak{g}_{-\alpha}$ such that $K(E,F)\neq 0$. Then from the above result, we know that they satisfy the relation

$$[E,F]=K(E,F)H_\alpha,\quad [H_\alpha,E]=\alpha(H_\alpha)E=K(\alpha,\alpha)E,\quad [H_\alpha,F]=-\alpha(H_\alpha)F=-K(\alpha,\alpha)F$$

This has a form similar to the commutation relations of the $\sl_2$-representation examined above, and indeed it is not difficult to show that $(\alpha,\alpha)\neq 0$. Therefore, we define

$$h_\alpha=\frac{2}{K(\alpha,\alpha)}H_\alpha$$

and similarly, through appropriate scaling in place of $E$ and $F$ to satisfy

$$(e_\alpha,f_\alpha)(\alpha,\alpha)=2$$

we can choose $e_\alpha\in \mathfrak{g}_\alpha$ and $f_\alpha\in \mathfrak{g}_{-\alpha}$, and these satisfy the following commutation relations

$$[e_\alpha,f_\alpha]=h_\alpha,\quad [h_\alpha,e_\alpha]=2e_\alpha,\quad [h_\alpha,f_\alpha]=-2f_\alpha$$

That is, they give a subalgebra of $\mathfrak{g}$ isomorphic to $\sl_2$. Let us denote this by $\sl_{2,\alpha}$. Then via the adjoint action we can regard $\mathfrak{g}$ as an $\sl_{2,\alpha}$-representation.

In particular, let us examine how $h_\alpha$ acts on the elements of $\mathfrak{g}$. First, in $\mathfrak{g}$, looking at how on the root space $\mathfrak{g}_\beta$ the adjoint action of $h_\alpha$ acts, since

$$[h_\alpha, x]=\beta(h_\alpha)x\qquad\text{for all $x\in \mathfrak{g}_\beta$}$$

$\mathfrak{g}_\beta$ is the weight space of weight $\beta(h_\alpha)$ for this action. But as we saw earlier, the weights of an $\sl_2$-representation are always integers, so we know that this value $\beta(h_\alpha)=\frac{2K(\alpha,\beta)}{K(\alpha,\alpha)}$ must be an integer. Also, since any weight subspace of an $\sl_2$ representation is $1$-dimensional, each $\mathfrak{g}_\beta$ is also $1$-dimensional.

Meanwhile, since we saw earlier that $\mathfrak{h}$ is generated by the $H_\alpha$, their scalar multiples $h_\alpha$ also generate $\mathfrak{h}$. As mentioned earlier, in order to give this a root system structure, we will consider the *real* vector space generated by the $h_\alpha$:

$$\mathfrak{h}_\mathbb{R}=\span_\mathbb{R}\{h_\alpha\mid \alpha\in\Phi\}$$

Then on this space, for two basis elements $h_\alpha,h_\beta$,

$$K(h_\alpha,h_\beta)=\tr_\mathfrak{g}(\ad h_\alpha\ad h_\beta)=\sum_{\gamma\in\Phi}\gamma(h_\alpha)\gamma(h_\beta)$$

holds. We proved earlier that these $\gamma(h_\alpha),\gamma(h_\beta)$ are integers, and therefore so is $K(h_\alpha,h_\beta)$. That is, when restricted to $\mathfrak{h}_\mathbb{R}$, $K$ is real-valued, and now for any $h\in \mathfrak{h}_\mathbb{R}$, it gives

$$K(h,h)=\tr(\ad_h\ad_h)=\sum_{\gamma\in\Phi}\gamma(h)^2\geq 0$$

If $K(h,h)=0$, then for all $\gamma\in\Phi$ we have $\gamma(h)=0$, and since $\Phi$ spans $\mathfrak{h}^\ast$, we have $h=0$. Therefore, we know that $K$ is positive definite on $\mathfrak{h}_\mathbb{R}$. In particular, transferring this back to $\mathfrak{h}^\ast$, we can verify that in $\mathfrak{h}^\ast$ the real span of $\Phi$ forms a Euclidean space, and in the process of showing this we also showed that these roots satisfy the fourth condition of [Definition 9](#def9){: data-lid="8vflr" }. Now what we need to show are the remaining conditions.

First, we must show that

$$s_\alpha(\beta)=\beta-\frac{2K(\alpha,\beta)}{K(\alpha,\alpha)}\alpha$$

obtained by applying the reflection operator, is again a root; this is clear because if $\beta(h_\alpha)\geq 0$, applying $\ad f_\alpha$, and if $\beta(h_\alpha)<0$, applying $\ad e_\alpha$ $\lvert \beta(h_\alpha)\rvert$ times yields an isomorphism between $\mathfrak{g}_\beta$ and $\mathfrak{g}_{s_\alpha(\beta)}$.

For the second condition, if we suppose that $\beta=c\alpha$, then in order for

$$\frac{2K(\alpha,\beta)}{K(\alpha,\alpha)}=2c,\quad \frac{2K(\alpha,\beta)}{K(\beta,\beta)}=\frac{2}{c}$$

to both be integers, $c$ must be one of $\pm 1$, $\pm 2$, or $\pm 1/2$, and transferring this back to $\sl_2$-representation theory and applying integrality yields the desired result. That is, we have proved the following.

::: Proposition 12
The collection $\Phi$ of roots defined in [Definition 5](#def5){: data-lid="86hpa" } is a root system of the Euclidean space formed by its real span in $\mathfrak{h}^\ast$.
:::

## Examples

Now let us examine the following examples.

::: Example 13
First consider the standard Euclidean space $\mathbb{R}^{n+1}$, and consider the subspace of $\mathbb{R}^{n+1}$

$$V_n=\left\{(x_1,\ldots, x_{n+1})\mid x_1+\cdots+x_{n+1}=0\right\}$$

We consider the subset of this vector space

$$\Phi(A_n)=\left\{e_i-e_j\mid 1\leq i\neq j\leq n+1\right\}$$

Then we know that this set satisfies all the conditions of [Definition 9](#def9){: data-lid="bwu4k" }. That the first condition, that $\Phi(A_n)$ spans $V_n$, and the second condition hold is obvious. For the third condition, for any vector $\mathbf{x}=(x_1,\ldots, x_{n+1})$ and any $\mathbf{e}_{ij}=e_i-e_j$, we have

$$s_{ij}(\mathbf{x})=\mathbf{x}-\langle \mathbf{x}, \mathbf{e}_{ij}\rangle\mathbf{e}_{ij}=(x_1,\ldots, x_{n+1})-(x_i-x_j)\mathbf{e}_{ij}$$

and this is given by swapping in $\mathbf{x}$ the $i$th and $j$th components. Therefore from this we know that the third condition of [Definition 9](#def9){: data-lid="krlma" } holds, and the fourth condition is obvious.
:::

Similarly, we can consider the following example.

::: Example 14
This time, consider the standard Euclidean space $\mathbb{R}^n$. We now consider the set

$$\Phi(D_n)=\left\{\pm e_i\pm e_j\mid 1\leq i \neq j\leq n\right\}$$

That these vectors span $\mathbb{R}^n$ is obvious. This time, we need to examine what reflections arbitrary $\mathbf{e}_{ij}^\pm =e_i\pm e_j$ define. We know that the $e_i-e_j$ swap, in a vector $\mathbf{x}$, the $i$th and $j$th components, and therefore it suffices to know what reflection $e_i+e_j$ defines. That is, considering the computation

$$s_{ij}^+(\mathbf{x})=\mathbf{x}-\langle\mathbf{x}, \mathbf{e}_{ij}^+\rangle\mathbf{e}_{ij}^+=(x_1,\ldots, x_n)-(x_i+x_j)\mathbf{e}_{ij}^+$$

$s_{ij}^+$ swaps the $i$th and $j$th components of the given vector and then reverses their signs as well.
:::

As can be seen from the above examples, not all roots are needed to describe a root system. For instance, in the case of $\Phi(A_n)$,

$$e_i-e_k=(e_i-e_j)+(e_j-e_k)$$

holds, and from this we know that to describe $\Phi(A_n)$ we only need elements of the form $e_i-e_{i+1}$. In a similar manner, we define the following.

::: Definition 15
For a root system $\Phi$, we say that a subset of $\Phi$, $\Phi^+$, is a subset of *positive roots* if for each root $\alpha\in \Phi$, exactly one of $\alpha$ and $-\alpha$ belongs to $\Phi^+$, and whenever any two $\alpha,\beta\in \Phi^+$ are given, if $\alpha+\beta$ is again a root, then $\alpha+\beta\in \Phi^+$ also holds. When a collection $\Phi^+$ of positive roots is fixed, for an element of $\Phi^+$, $\alpha$, to be a *simple root* means that $\alpha$ cannot be written as a sum of two elements of $\Phi^+$.
:::

Therefore, if we only know how the integer values

$$\langle\alpha_i,\alpha_j\rangle=2\frac{(\alpha_i,\alpha_j)}{(\alpha_j,\alpha_j)}$$

between simple roots are defined, we can know how, for an arbitrary root $\alpha_j$, the reflection $s_j$ moves another root $\alpha_i$.

Now suppose that a root system $\Phi$ and a collection of simple roots $\Delta=\left\{\alpha_1,\ldots, \alpha_l\right\}$ are fixed. Then the *Cartan matrix* is defined as follows.

::: Definition 16
In the above setting, the following matrix

$$A=(a_{ij})_{1\leq i,j\leq l},\qquad a_{ij}=\langle \alpha_i,\alpha_j\rangle$$

is called the *Cartan matrix*.
:::

By the definition of a root system, each entry $a_{ij}$ is an integer. It is also obvious that for each $i$, we have $a_{ii}=2$.

Meanwhile, from the identity

$$\langle\alpha,\beta\rangle \langle\beta,\alpha\rangle=4\frac{(\alpha,\beta)^2}{\lvert\alpha\rvert^2\lvert\beta\rvert^2}=4(\cos\theta)^2$$

and the fact that the left-hand side is an integer, we know that for any two roots $\alpha,\beta$, the only values that $\langle\alpha,\beta\rangle$ can take are $0, \pm 1, \pm 2, \pm 3$. Here, $\theta$ is the angle between the two roots $\alpha,\beta$, and the possible values that $\cos\theta$ can take are

$$0, \pm \frac{1}{2}, \pm \frac{\sqrt{2}}{2}, \pm \frac{\sqrt{3}}{2}, \pm 1$$

Here, the cases of $\pm 1$ are excluded by the second condition of [Definition 9](#def9){: data-lid="i7jp8" }, so roots can only form angles of $30$ degrees (or $150$ degrees), $45$ degrees (or $135$ degrees), $60$ degrees (or $120$ degrees), or $90$ degrees.

For the sake of an example, suppose the angle formed by two roots $\alpha,\beta$ is $30$ degrees or $150$ degrees. Then from

$$\langle\alpha,\beta\rangle\langle\beta,\alpha\rangle=3$$

$\langle\alpha,\beta\rangle$ must be $\pm 1$ or $\pm 3$. Now, from the fact that the value of the following expression

$$\langle \alpha,\beta\rangle =2\frac{(\alpha,\beta)}{\lvert\beta\rvert^2}=\frac{2\lvert\alpha\rvert\lvert\beta\rvert\cos\theta}{\lvert\beta\rvert^2}=\frac{\pm \sqrt{3}\lvert\alpha\rvert}{\lvert\beta\rvert}$$

is $\pm 1$ or $\pm 3$, we know that the ratio of the lengths of $\alpha$ and $\beta$ must be $\sqrt{3}$. Similarly, if the angle between two roots $\alpha,\beta$ is $45$ degrees or $135$ degrees, the ratio of the lengths of these two roots must be $\sqrt{2}$, and in the case of $60$ degrees or $120$ degrees, the ratio of lengths must be $1$.

## Weyl group

For each root $\alpha$ of a root system $\Phi$, the reflection $s_\alpha$ defines an automorphism of $\Phi$. Let us consider the group generated by these reflections.

::: Definition 17
The *Weyl group* of a root system $\Phi$ is the subgroup of $\Aut(\Phi)$ generated by the reflections $s_\alpha$ ($\alpha\in\Phi$).

$$W(\Phi)=\langle s_\alpha\mid \alpha\in\Phi\rangle$$
:::

The Weyl group is a finite group. Indeed, $W$ is a subgroup of the orthogonal group of the Euclidean space containing $\Phi$, and since $\Phi$ is a finite set, $W$ is also finite. In addition, by the third condition of [Definition 9](#def9){: data-lid="3bli7" }, the reflection $s_\alpha$ is the reflection across the hyperplane perpendicular to $\alpha$, so $W$ has the structure of a Coxeter group.

::: Example 18
For $\Phi(A_n)$ examined in [Example 13](#ex13){: data-lid="hy5hp" }, the reflection $s_{ij}$ corresponds to the transposition swapping the $i$th and $j$th coordinates. Hence $W(\Phi(A_n))\cong S_{n+1}$. For $\Phi(D_n)$ of [Example 14](#ex14){: data-lid="aj3ir" }, the reflections include both coordinate swaps and sign changes, so $W(\Phi(D_n))\cong(\mathbb{Z}/2\mathbb{Z})^{n-1}\rtimes S_n$.
:::

## Connection to Lie groups

So far we have defined the root system $\Phi$ of a semisimple Lie algebra $\mathfrak{g}$ and defined the Weyl group capturing its symmetry as the finite group generated by the reflections $s_\alpha$. On the other hand, in [§Torus Actions, §§Maximal tori](/en/math/lie_theory/torus_action#maximal-tori){: data-lid="ncqba" } we defined the Weyl group of a compact Lie group $G$ as $W=N(T)/T$. In this section we show that the two definitions naturally coincide.

First, let $\mathfrak{g}$ be the Lie algebra of a compact connected Lie group $G$. That $\mathfrak{g}$ is semisimple is equivalent to the universal cover of $G$ not having $\mathbb{R}^n$ as a factor. In this case, the Lie algebra $\mathfrak{t}$ of a maximal torus $T$ of $G$ becomes a Cartan subalgebra of $\mathfrak{g}$.

Now let us examine how $N(T)$ acts on $\mathfrak{t}^\ast$. For any $n\in N(T)$, the adjoint representation $\Ad(n)$ is an automorphism of $\mathfrak{g}$ and since $nTn^{-1}=T$, it preserves $\mathfrak{t}$. Therefore $\Ad(n)\vert_\mathfrak{t}$ is an automorphism of $\mathfrak{t}$, and dualizing this yields a linear action on $\mathfrak{t}^\ast$.

::: Proposition 19
The action of $N(T)$ on $\mathfrak{t}^\ast$ preserves the root system $\Phi$.
:::
::: Proof
For any $n\in N(T)$ and $\alpha\in\Phi$, it suffices to show that $\Ad(n)$ sends $\mathfrak{g}_\alpha$ to $\mathfrak{g}_{n\cdot\alpha}$. For any $X\in\mathfrak{g}_\alpha$ and $H\in\mathfrak{t}$,

$$[H,\Ad(n)X]=\Ad(n)[\Ad(n)^{-1}H,X]$$

and since $\Ad(n)^{-1}H\in\mathfrak{t}$ and $X\in\mathfrak{g}_\alpha$,

$$[\Ad(n)^{-1}H,X]=\alpha(\Ad(n)^{-1}H)X=(n^{-1}\cdot\alpha)(H)\cdot X$$

Therefore

$$[H,\Ad(n)X]=(n^{-1}\cdot\alpha)(H)\cdot\Ad(n)X$$

and this means $\Ad(n)X\in\mathfrak{g}_{n^{-1}\cdot\alpha}$. That is, $\Ad(n)$ sends $\mathfrak{g}_\alpha$ to $\mathfrak{g}_{n^{-1}\cdot\alpha}$, and from this we know that $n\cdot\alpha\in\Phi$.
:::

Thus we know that $W=N(T)/T$ has a well-defined action on $\mathfrak{t}^\ast$, and in particular on the root system $\Phi$. Now the key result is as follows.

::: Proposition 20
For each root $\alpha\in\Phi$, there exists $n_\alpha\in N(T)$ satisfying $\Ad(n_\alpha)\vert_\mathfrak{t}=s_\alpha$. Therefore the Weyl group $W=N(T)/T$ defined from the Lie group and the Weyl group of the root system are isomorphic.
:::
::: Proof
For any root $\alpha\in\Phi$, as examined earlier, $\sl_{2,\alpha}=\langle e_\alpha, f_\alpha, h_\alpha\rangle$ is a subalgebra of $\mathfrak{g}$ isomorphic to $\sl(2;\mathbb{C})$. The corresponding Lie subgroup $G_\alpha$ of $G$ is locally isomorphic to $\SU(2)$ or $\SO(3)$.

$G_\alpha$ intersects $T$ to form a one-dimensional torus $T_\alpha=T\cap G_\alpha$. Now we need to find an element of $N(T)$ whose $\Ad$-action induces the reflection $s_\alpha$ on $\mathfrak{t}$. For this purpose consider the element

$$n_\alpha=\exp(e_\alpha)\exp(-f_\alpha)\exp(e_\alpha)$$

By computation in $\SU(2)$ this corresponds to

$$\begin{pmatrix}0&1\\-1&0\end{pmatrix}$$

and this element sends elements of $T_\alpha$ to $t\mapsto t^{-1}$. Therefore $\Ad(n_\alpha)$ sends $h_\alpha$ to $-h_\alpha$ and preserves $\ker\alpha$. That is, $\Ad(n_\alpha)\vert_\mathfrak{t}=s_\alpha$.

Finally, let us verify that $n_\alpha\in N(T)$. Since $\Ad(n_\alpha)$ preserves $\mathfrak{t}$, $n_\alpha Tn_\alpha^{-1}$ and $T$ have the same Lie algebra, and since both are connected, $n_\alpha Tn_\alpha^{-1}=T$.
:::

From this we know that the Weyl groups from the two perspectives are essentially the same object. From the Lie group perspective, $W=N(T)/T$ captures the conjugation action on the maximal torus, while from the Lie algebra perspective, $W$ captures the symmetry of the root system. The agreement of the two definitions is a concrete expression of the fact that the structure of a compact Lie group is completely determined by the root system of its Lie algebra.

Integrating these two perspectives, the geometric objects that naturally emerge from a root system, namely Borel subgroups and flag varieties, are treated in [§Borel Subgroups](/en/math/lie_theory/borel_subgroup){: data-lid="mro1u" }.

---

**References**

**[Hum]** J. E. Humphreys, *Introduction to Lie algebras and representation theory*, Graduate Texts in Mathematics, Springer, 1972.  
**[FH]** W. Fulton and J. Harris, *Representation theory: a first course*, Graduate Texts in Mathematics, Springer, 1991.
