---
title: "Root Systems"
excerpt: "Root systems obtained from the weight decomposition of the adjoint representation"

categories: [Math / Lie Theory]
permalink: /en/math/lie_theory/root_systems
header:
    overlay_image: /assets/images/Math/Lie_Theory/Root_Systems.png
    overlay_filter: 0.5
sidebar: 
    nav: "Lie_theory-en"

date: 2025-11-12
last_modified_at: 2026-02-24
weight: 3
translated_at: 2026-05-20T22:00:02+00:00
translation_source: kimi-cli
---
## Adjoint representation

A Lie group has a natural (finite-dimensional) representation $$\Ad: G \rightarrow \Aut(\mathfrak{g})$$. ([§Lie Groups, ⁋Definition 19](/en/math/lie_theory/Lie_groups#def19)) This is the differential at $$h=e$$ of the conjugation $$h\mapsto ghg^{-1}$$ defined by each $$g\in G$$, and if we regard both $$G$$ and $$\Aut(\mathfrak{g})$$ as Lie groups and differentiate this, we obtain a representation of $$\mathfrak{g}$$

$$\ad: \mathfrak{g}\rightarrow \Lie(\Aut(\mathfrak{g}))$$

and, keeping [§Lie Groups, ⁋Theorem 15](/en/math/lie_theory/Lie_groups#thm15) in mind, we may think that essentially all the information contained in $$\Ad$$ is captured here. Since the Lie algebra of a vector space is the space itself, we may regard $$\mathfrak{g}$$ as a representation space for itself, and in this case $$\ad$$ is explicitly given by

$$\ad(X)Y=[X,Y]$$

through which it is computed.

An important fact for using results from representation theory is that every finite-dimensional representation is unitary. The argument used to prove this result is that one can choose a $$G$$-invariant inner product on $$V$$; strictly speaking, since we are interested in orthogonal complements, it suffices to have a non-degenerate symmetric form. Now, there is a natural bilinear form on a Lie algebra.

<div class="definition" markdown="1">

<ins id="def1">**Definition 1**</ins> On a Lie algebra $$\mathfrak{g}$$, the symmetric bilinear form defined by the formula

$$K(X,Y)=\tr(\ad(X)\ad(Y))$$

is called the *Killing form*.

</div>

That the Killing form is symmetric and $$\mathbb{C}$$-bilinear is obvious from the definition. Moreover, this Killing form is already invariant under the adjoint action of $$G$$ without any additional maneuvering. That is, the formula

$$K(\Ad_g(X), \Ad_g(Y))=K(X,Y)$$

holds, and differentiating this at $$g=e$$ in the direction of $$Z$$ yields the following $$\ad$$-invariance:

$$0=\frac{d}{dt}\bigg\vert_{t=0}K(\Ad_{\exp(tZ)}X, \Ad_{\exp(tZ)},Y)=K([Z,X],Y)+K(X,[Z,Y])$$

What remains is the condition for it to be non-degenerate.

<div class="definition" markdown="1">

<ins id="def2">**Definition 2**</ins> A Lie algebra $$\mathfrak{g}$$ is called *simple* if it is a non-abelian Lie algebra and its only ideals are $$0$$ and itself. A Lie algebra that can be written as a direct sum of simple Lie algebras is called *semisimple*.

</div>

Then the following holds.

<div class="proposition" markdown="1">

<ins id="prop3">**Proposition 3**</ins> For a finite-dimensional Lie algebra $$\mathfrak{g}$$, the following are all equivalent.

1. $$\mathfrak{g}$$ is semisimple.
2. The Killing form is non-degenerate.
3. $$\mathfrak{g}$$ has no nonzero abelian ideal.
4. $$\mathfrak{g}$$ has no nonzero solvable ideal.
5. The radical of $$\mathfrak{g}$$ is $$0$$.

</div>

We omit the proof since it is not immediately important.

## Cartan subalgebras

One of the most powerful tools in linear algebra is diagonalization, and in the context of Lie groups we captured this through weight decomposition. ([§Torus Actions, ⁋Definition 4](/en/math/lie_theory/torus_action#def4)) The corresponding notion for Lie algebras is as follows.

<div class="definition" markdown="1">

<ins id="def4">**Definition 4**</ins> For a semisimple Lie algebra $$\mathfrak{g}$$, a *Cartan subalgebra* of $$\mathfrak{g}$$ is a maximal abelian subalgebra $$\mathfrak{h}$$ such that $$\ad(H)$$ is diagonalizable for all $$H\in\mathfrak{h}$$.

</div>

Two diagonalizable operators $$A,B$$ are simultaneously diagonalizable if and only if they commute, so by definition all elements of $$\mathfrak{h}$$ are simultaneously diagonalizable. Let us now decompose $$\mathfrak{g}$$ using the family $$\{H\in\mathfrak{h}\}$$ of simultaneously diagonalizable operators. If a *finite* family $$A_1,\ldots,A_n$$ of simultaneously diagonalizable operators is given, decomposing the space into simultaneous eigenspaces takes the form

$$$V=\bigoplus V_\alpha,\qquad \text{$$A_i v_\alpha=\lambda_i v_\alpha$$ for all $$v_\alpha\in V$$ for all $$i$$}$$$

However, in our present situation $$\mathfrak{h}$$ is a vector space, so it is better to choose a linear functional $$\alpha:\mathfrak{h}\rightarrow\mathbb{C}$$ and let $$\alpha(H)$$ play the role of the eigenvalue for each $$H$$. Thus we define as follows.

<div class="definition" markdown="1">

<ins id="def5">**Definition 5**</ins> For a semisimple Lie algebra $$\mathfrak{g}$$ and a Cartan subalgebra $$\mathfrak{h}$$ of $$\mathfrak{g}$$,

$$\Phi=\left\{\alpha\in \mathfrak{h}^\ast\setminus\{0\}\mid \mathfrak{g}_\alpha\neq 0\right\}$$

the elements of $$\Phi$$ are called the *roots* of $$\mathfrak{g}$$. Here

$$$\mathfrak{g}_\alpha=\left\{X\in \mathfrak{g}\mid [H,X]=\alpha(H)X\text{ for all $$H\in \mathfrak{h}$$}\right\}$$$

([§Lie Groups, ⁋Definition 19](/en/math/lie_theory/Lie_groups#def19))

</div>

By definition, $$\mathfrak{h}$$ acts on itself by $$0$$. That is, $$\mathfrak{h}$$ is the eigenspace with eigenvalue $$0$$ in the simultaneous eigenspace decomposition of $$\mathfrak{g}$$, and from this we obtain the decomposition

$$\mathfrak{g}=\mathfrak{h}\oplus\bigoplus_{\alpha\in \Phi}\mathfrak{g}_\alpha$$

That these satisfy the following proposition is obvious.

<div class="proposition" markdown="1">

<ins id="prop6">**Proposition 6**</ins> Let $$\mathfrak{g}$$ be a semisimple Lie algebra, $$\mathfrak{h}$$ a Cartan subalgebra, and consider its root decomposition

$$\mathfrak{g}=\mathfrak{h}\oplus\bigoplus_{\alpha\in\Phi}\mathfrak{g}_\alpha$$

and let $$K(-,-)$$ be the Killing form on $$\mathfrak{g}$$. Then the following hold.

1. For any $$\alpha,\beta\in\Phi$$, we have $$[\mathfrak{g}_\alpha,\mathfrak{g}_\beta]\subseteq\mathfrak{g}_{\alpha+\beta}$$.
2. If $$\alpha+\beta\neq 0$$, then $$\mathfrak{g}_\alpha$$ and $$\mathfrak{g}_\beta$$ are orthogonal with respect to $$K$$.
3. The restriction of the Killing form to $$\mathfrak{g}_\alpha\otimes\mathfrak{g}_{-\alpha}$$ is a nondegenerate pairing.

</div>
<details class="proof" markdown="1">
<summary>Proof</summary>

1. For any $$X\in\mathfrak{g}_\alpha$$, $$Y\in\mathfrak{g}_\beta$$, and $$H\in\mathfrak{h}$$,

    $$[H,[X,Y]]=[[H,X],Y]+[X,[H,Y]]=[\alpha(H)X,Y]+[X,\beta(H)Y]=(\alpha+\beta)(H)[X,Y]$$

    holds.
2. For any $$X\in\mathfrak{g}_\alpha$$, $$Y\in\mathfrak{g}_\beta$$, and $$H\in\mathfrak{h}$$, by the $$\ad$$-invariance of $$K$$ we have

    $$0=K([H,X],Y)+K(X,[H,Y])=K(\alpha(H),X)+K(X,\beta(H)Y)=(\alpha+\beta)(H)K(X,Y)$$

    Hence if $$\alpha+\beta\neq 0$$, then for this to always hold we must have $$K(X,Y)=0$$ always.
3. Since the Killing form is non-degenerate on $$\mathfrak{g}$$, for any given $$X\in\mathfrak{g}_\alpha$$ there exists $$Z\in\mathfrak{g}$$ such that $$K(X,Z)\neq 0$$. What we need to show is that we can choose $$Z\in\mathfrak{g}_{-\alpha}$$. This is obvious: if we root-decompose $$Z$$, then by the second result the components corresponding to parts other than $$-\alpha$$ pair with $$X$$ to give $$0$$ anyway.

</details>

## Example: $$\sl(2;\mathbb{C})$$

From [§Lie Groups, ⁋Proposition 12](/en/math/lie_theory/Lie_groups#prop12) we know that $$\sl(n;\mathbb{C})$$ is the set of $$n\times n$$ *traceless* matrices. Thus $$\sl(2;\mathbb{C})$$ has the following three elements as a basis:

$$H=\begin{pmatrix}1&0\\0&-1\end{pmatrix},\quad E=\begin{pmatrix}0&1\\0&0\end{pmatrix},\quad F=\begin{pmatrix}0&0\\1&0\end{pmatrix}$$

Hence the multiplicative structure of $$\sl(2;\mathbb{C})$$ is given by the commutation relations

$$[H,E]=2E,\quad [H,F]=-2F,\quad [E,F]=H$$

We show that any $$\sl(2;\mathbb{C})$$-representation decomposes as a direct sum of irreducible representations. This is an obvious result for compact Lie groups, but remember that for non-compact groups such as $$\SL(n,\mathbb{C})$$ the existence of a Haar measure is not guaranteed, so ideas such as averaging an inner product by integration cannot be used.

Let $$V$$ be an arbitrary finite-dimensional $$\sl_2$$-representation, and for each $$\lambda\in\mathbb{C}$$ define the weight space

$$V_\lambda=\{v\in V\mid H\cdot v=\lambda v\}$$

Then by the commutation relations seen above,

$$E\cdot V_\lambda\subset V_{\lambda+2},\qquad F\cdot V_\lambda\subset V_{\lambda-2}$$

hold. For this reason we also call $$E$$ and $$F$$ the *raising operator* and *lowering operator*, respectively. On the other hand, since $$V$$ is finite-dimensional, in the weight decomposition

$$V=\bigoplus_{\lambda} V_\lambda$$

there exists a $$\mu$$ such that $$V_\mu\neq 0$$ but $$V_{\mu+2}=0$$. Such a $$\mu$$ is called the *highest weight*, and elements of $$V_\mu$$ are called *highest weight vectors*. Then for a highest weight vector $$v$$ we know the two equations

$$H\cdot v=\mu v,\qquad E\cdot v=0$$

hold.

<div class="proposition" markdown="1">

<ins id="prop7">**Proposition 7**</ins> For any highest weight vector $$v_0\in V_\mu$$, define

$$v_j=\frac{1}{j!}F^j v_0$$

Then the following hold:

$$H\cdot v_j=(\mu-2j)v_j,\quad F\cdot v_j=(j+1)v_{j+1},\quad E\cdot v_j=(\mu-j+1)v_{j-1}.$$

</div>
<details class="proof" markdown="1">
<summary>Proof</summary>

The first two equations are obvious, so it suffices to prove the equation for $$E$$. We proceed by induction. The case $$j=0$$ is obvious, and if the given formula holds for $$j$$ then

$$E\cdot v_{j+1}=\frac{1}{j+1}EF\cdot v_j=\frac{1}{j+1}(FE+H)\cdot v_j$$

and by the induction hypothesis

$$E\cdot v_j=(\mu-j+1)v_{j-1}$$

and from the formula for $$H$$ we have $$H\cdot v_j=(\mu-2j)v_j$$, so substituting these gives the desired result.

</details>

Since $$V$$ is finite-dimensional, there exists a smallest integer $$m$$ such that $$v_{m+1}=0$$. Then for this $$m$$,

$$0=E\cdot v_{m+1}=(\mu-m)v_m$$

and from the minimality of $$m$$ we see that $$\mu=m$$. That is, the highest weight must be a nonnegative integer.

<div class="definition" markdown="1">

<ins id="def8">**Definition 8**</ins> For a fixed integer $$m\geq 0$$, we define the $$\sl_2$$-representation $$V(m)$$ on the $$m+1$$ vectors $$v_0,\ldots,v_m$$ by the action of [Proposition 7](#prop7):

$$H\cdot v_j=(m-2j)v_j,\quad F\cdot v_j=(j+1)v_{j+1},\quad E\cdot v_j=(m-j+1)v_{j-1}$$

with $$v_{-1}=v_{m+1}=0$$.

</div>

It is not difficult to show that $$V(m)$$ is irreducible. Now, for an arbitrary $$\sl_2$$-representation $$V$$, we can decompose $$V$$ into irreducible $$\sl_2$$-representations by finding a highest weight of $$V$$, applying [Proposition 7](#prop7) to the corresponding highest weight vector, and repeating this process if any highest weight vectors remain.

## Root systems

The above example of an $$\sl_2$$-representation plays a major role in what follows. First, let us define the following.

<div class="definition" markdown="1">

<ins id="def9">**Definition 9**</ins> Fix a finite-dimensional vector space $$V$$ and an inner product $$(-,-)$$ on it. A finite set $$\Phi$$ of non-zero vectors in $$V$$ is called a *root system* if the following conditions are satisfied.

1. The elements of $$\Phi$$ span $$V$$.
2. If $$\alpha\in\Phi$$ and $$c\in\mathbb{R}$$, then $$c\alpha\in\Phi$$ only if $$c=\pm 1$$.
3. For each root $$\alpha\in\Phi$$, the set $$\Phi$$ is closed under the reflection $$s_\alpha$$ in the hyperplane perpendicular to $$\alpha$$. That is, for any $$\alpha,\beta\in\Phi$$,

    $$s_\alpha(\beta):=\beta-2\frac{(\beta,\alpha)}{(\alpha,\alpha)}\alpha\in \Phi$$

4. For any roots $$\alpha,\beta\in\Phi$$, the number

    $$\langle \beta,\alpha\rangle:=2\frac{(\beta,\alpha)}{(\alpha,\alpha)}$$

    is always an integer.

</div>

Now fix a Cartan subalgebra $$\mathfrak{h}$$ of a semisimple complex Lie algebra $$\mathfrak{g}$$. Then the following holds.

<div class="proposition" markdown="1">

<ins id="lem10">**Lemma 10**</ins> For a semisimple Lie algebra $$\mathfrak{g}$$, a Cartan subalgebra $$\mathfrak{h}$$, and the root decomposition

$$\mathfrak{g}=\mathfrak{h}\oplus\bigoplus_{\alpha\in \Phi} \mathfrak{g}_\alpha$$

the following hold.

1. For any $$\alpha,\beta\in\Phi$$, we have $$[\mathfrak{g}_\alpha,\mathfrak{g}_\beta]\subseteq \mathfrak{g}_{\alpha+\beta}$$.
2. If $$\alpha+\beta\neq 0$$, then $$\mathfrak{g}_\alpha$$ and $$\mathfrak{g}_\beta$$ are orthogonal.
3. The restriction of the Killing form defined on $$\mathfrak{g}$$ to $$\mathfrak{h}$$ is non-degenerate.
4. The restriction of the Killing form defined on $$\mathfrak{g}$$ to $$\mathfrak{g}_\alpha\times\mathfrak{g}_{-\alpha}\rightarrow\mathbb{C}$$ is non-degenerate.

</div>
<details class="proof" markdown="1">
<summary>Proof</summary>

The first claim is obvious. For the second claim, for any $$X_\alpha\in\mathfrak{g}_\alpha$$, $$X_\beta\in\mathfrak{g}_\beta$$, and any $$H\in\mathfrak{h}$$, from the $$\ad$$-invariance of $$K$$ we obtain the formula

$$0=K([H,X_\alpha],X_\beta)+K(X_\alpha, [H,X_\beta])=K(\alpha(H)X_\alpha, X_\beta)+K(X_\alpha,\beta(H)X_\beta)=(\alpha+\beta)(H)K(X_\alpha,X_\beta)$$

Hence if $$\alpha+\beta\neq 0$$, then $$\mathfrak{g}_\alpha$$ and $$\mathfrak{g}_\beta$$ are orthogonal with respect to $$K$$.

To prove the third claim, recall that for any $$H\in\mathfrak{h}$$ there exists $$X\in\mathfrak{g}$$ such that $$K(H,X)\neq 0$$. What we newly need to show is that we can choose $$X$$ from $$\mathfrak{h}$$. Writing $$X$$ in the form $$\sum X_\alpha$$ of the root decomposition, we know by the above result that when we apply $$K(H,-)$$, all $$X_\alpha$$ except $$X_0\in\mathfrak{h}$$ give $$0$$. Therefore $$K(H,H_0)\neq 0$$.

The fourth claim is proved in exactly the same way as the third.

</details>

Now, since the Killing form defined on $$\mathfrak{g}$$ is also non-degenerate on $$\mathfrak{h}$$, we have the induced isomorphism

$$\mathfrak{h}\rightarrow \mathfrak{h}^\ast;\qquad H\mapsto K(H, -)$$

Then $$\Phi\subseteq\mathfrak{h}^\ast$$ is a spanning set of $$\mathfrak{h}^\ast$$. If there were an element of $$\mathfrak{h}^\ast$$ not expressible as a linear combination of elements of $$\Phi$$, then the corresponding element of $$\mathfrak{h}$$ would have to satisfy $$\alpha(H)=0$$ for all $$\alpha\in H$$. Now, for any root space $$\mathfrak{g}_\alpha$$, $$H$$ acts by

$$$[H,X]=\alpha(H)X=0\qquad\text{for all $$X\in \mathfrak{g}_\alpha$$}$$$

and since $$\mathfrak{h}$$ is abelian, it acts on itself by $$0$$. That is, considering the root decomposition of $$\mathfrak{g}$$, $$H$$ acts by $$0$$ on all elements of $$\mathfrak{g}$$, and from this we see that $$H$$ commutes with every element of $$\mathfrak{g}$$ under the Lie bracket. But by [Proposition 4](#prop4), $$\mathfrak{g}$$ cannot have a nonzero abelian ideal, and in particular we must have $$Z(\mathfrak{g})=0$$, so $$H=0$$.

From this we know that $$\Phi$$ spans $$\mathfrak{h}^\ast$$. However, $$\mathfrak{h}^\ast$$ is a complex vector space, and the Killing form defined on it is not guaranteed to be positive definite, so it is not an inner product. To remedy this, we consider the real span of the dual elements of $$\Phi$$ and show that the restriction of the Killing form to this subspace is positive definite. This requires a slightly more detailed analysis of the root decomposition.

For each root $$\alpha\in\Phi$$, the non-degeneracy of the Killing form gives the formula

$$$ \alpha(X)=K(H_\alpha,X)\qquad\text{for all $$X\in \mathfrak{h}$$} $$$

is satisfied by some $$H_\alpha\in\mathfrak{h}$$. Our first observation is the following lemma.

<div class="proposition" markdown="1">

<ins id="lem11">**Lemma 11**</ins> For any $$E\in\mathfrak{g}_\alpha$$ and $$F\in\mathfrak{g}_{-\alpha}$$, we have $$[E,F]=K(E,F)H_\alpha$$.

</div>
<details class="proof" markdown="1">
<summary>Proof</summary>

By the $$\ad$$-invariance of $$K$$,

$$K([E,F],H)=K(F,[H,E])$$

holds for all $$H\in\mathfrak{h}$$. On the other hand, since $$E\in\mathfrak{g}_\alpha$$,

$$[H,E]=\alpha(H)E=K(H_\alpha,H)E$$

and substituting this into the above equation gives

$$K([E,F],H)=K(F,[H,E])=K(F, K(H_\alpha,H)E)=K(H_\alpha,H)K(F
