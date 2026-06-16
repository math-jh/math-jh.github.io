---
title: "Root Systems"
description: "This post characterizes simple and semisimple Lie algebras through the properties of the Killing form defined on the adjoint representation, and covers the foundations of root systems."
excerpt: "Root systems obtained from the weight decomposition of the adjoint representation"

categories: [Math / Lie Theory]
permalink: /en/math/lie_theory/root_systems
sidebar: 
    nav: "Lie_theory-en"

date: 2025-11-12
weight: 3
translated_at: 2026-05-31T16:30:04+00:00
translation_source: kimi-cli
last_polished_at: 2026-05-31T16:30:04+00:00
---
## Adjoint representation

Every Lie group carries a natural (finite-dimensional) representation $$\Ad: G \rightarrow \Aut(\mathfrak{g})$$. ([§Lie Groups, ⁋Definition 19](/en/math/lie_theory/Lie_groups#def19)) This is the differential at $$h=e$$ of the conjugation $$h\mapsto ghg^{-1}$$ defined by each $$g\in G$$, and if we regard both $$G$$ and $$\Aut(\mathfrak{g})$$ as Lie groups and differentiate this map, we obtain a representation of $$\mathfrak{g}$$

$$\ad: \mathfrak{g}\rightarrow \Lie(\Aut(\mathfrak{g}))$$

and by [§Lie Groups, ⁋Theorem 15](/en/math/lie_theory/Lie_groups#thm15) we may essentially regard all the information encoded in $$\Ad$$ as already captured here. Since taking the Lie algebra of a vector space is the same as considering the space itself, we may view $$\mathfrak{g}$$ as a representation space for itself, and in this case $$\ad$$ is given explicitly by

$$\ad(X)Y=[X,Y].$$

What was important in applying the results of representation theory was that every finite-dimensional representation is unitary. The argument used to prove this was that we can choose a $$G$$-invariant inner product on $$V$$; to be precise, since we are interested in orthogonal complements, it suffices to have a non-degenerate symmetric form. And there is a natural bilinear form on any Lie algebra.

<div class="definition" markdown="1">

<ins id="def1">**Definition 1**</ins> The symmetric bilinear form on a Lie algebra $$\mathfrak{g}$$ defined by the formula

$$K(X,Y)=\tr(\ad(X)\ad(Y))$$

is called the *Killing form*.

</div>

That the Killing form is symmetric and $$\mathbb{C}$$-bilinear is obvious from the definition. Moreover, the Killing form is already invariant under the adjoint action of $$G$$ without any further manipulation. That is, the identity

$$K(\Ad_g(X), \Ad_g(Y))=K(X,Y)$$

holds, and differentiating this at $$g=e$$ in the direction of $$Z$$ yields the following $$\ad$$-invariance:

$$0=\frac{d}{dt}\bigg\vert_{t=0}K(\Ad_{\exp(tZ)}X, \Ad_{\exp(tZ)},Y)=K([Z,X],Y)+K(X,[Z,Y]).$$

What remains is the condition for this form to be non-degenerate.

<div class="definition" markdown="1">

<ins id="def2">**Definition 2**</ins> A Lie algebra $$\mathfrak{g}$$ is called *simple* if it is non-abelian and its only ideals are $$0$$ and itself. A Lie algebra that can be written as a direct sum of simple Lie algebras is called *semisimple*.

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

We will skip the proof, as it is not immediately needed.

## Cartan subalgebra

One of the most powerful tools in linear algebra was diagonalization, and in the theory of Lie groups we captured this through weight decomposition. ([§Torus Actions, ⁋Definition 4](/en/math/lie_theory/torus_action#def4)) The corresponding notion for Lie algebras is as follows.

<div class="definition" markdown="1">

<ins id="def4">**Definition 4**</ins> For a semisimple Lie algebra $$\mathfrak{g}$$, a *Cartan subalgebra* of $$\mathfrak{g}$$ is a maximal abelian subalgebra $$\mathfrak{h}$$ such that $$\ad(H)$$ is diagonalizable for every $$H\in \mathfrak{h}$$.

</div>

Since two diagonalizable operators $$A,B$$ are simultaneously diagonalizable if and only if they commute, all elements of $$\mathfrak{h}$$ are simultaneously diagonalizable by definition. Let us now decompose $$\mathfrak{g}$$ using the family of simultaneously diagonalizable operators $$\{H\in \mathfrak{h}\}$$. If a <em>finite</em> family of simultaneously diagonalizable operators $$A_1,\ldots, A_n$$ is given, decomposing the space into simultaneous eigenspaces takes the form

$$V=\bigoplus V_\alpha,\qquad \text{$A_i v_\alpha=\lambda_i v_\alpha$ for all $v_\alpha\in V$ for all $i$}$$

but in our present situation, since $$\mathfrak{h}$$ is a vector space, it is better to choose a linear functional $$\alpha: \mathfrak{h}\rightarrow \mathbb{C}$$ and let $$\alpha(H)$$ play the role of the eigenvalue for each $$H$$. Thus we make the following definition.

<div class="definition" markdown="1">

<ins id="def5">**Definition 5**</ins> For a semisimple Lie algebra $$\mathfrak{g}$$ and a Cartan subalgebra $$\mathfrak{h}$$ of $$\mathfrak{g}$$, the elements of

$$\Phi=\left\{\alpha\in \mathfrak{h}^\ast\setminus\{0\}\mid \mathfrak{g}_\alpha\neq 0\right\}$$

are called the *roots* of $$\mathfrak{g}$$. Here

$$\mathfrak{g}_\alpha=\left\{X\in \mathfrak{g}\mid [H,X]=\alpha(H)X\text{ for all $H\in \mathfrak{h}$}\right\}.$$

([§Lie Groups, ⁋Definition 19](/en/math/lie_theory/Lie_groups#def19))

</div>

By definition, $$\mathfrak{h}$$ acts on itself by $$0$$. That is, $$\mathfrak{h}$$ is the eigenspace with eigenvalue $$0$$ when $$\mathfrak{g}$$ is decomposed into simultaneous eigenspaces, and from this we obtain the decomposition

$$\mathfrak{g}=\mathfrak{h}\oplus\bigoplus_{\alpha\in \Phi}\mathfrak{g}_\alpha.$$

That these satisfy the following proposition is obvious.

<div class="proposition" markdown="1">

<ins id="prop6">**Proposition 6**</ins> Let $$\mathfrak{g}$$ be a semisimple Lie algebra, $$\mathfrak{h}$$ a Cartan subalgebra, and consider the root decomposition

$$\mathfrak{g}=\mathfrak{h}\oplus\bigoplus_{\alpha\in\Phi}\mathfrak{g}_\alpha,$$

and let $$K(-,-)$$ be the Killing form on $$\mathfrak{g}$$. The following hold.

1. For any $$\alpha,\beta\in \Phi$$, we have $$[\mathfrak{g}_\alpha,\mathfrak{g}_\beta]\subseteq \mathfrak{g}_{\alpha+\beta}$$.
2. If $$\alpha+\beta\neq 0$$, then $$\mathfrak{g}_\alpha$$ and $$\mathfrak{g}_\beta$$ are orthogonal with respect to $$K$$.
3. The restriction of the Killing form to $$\mathfrak{g}_\alpha\otimes \mathfrak{g}_{-\alpha}$$ is a nondegenerate pairing.

</div>
<details class="proof" markdown="1">
<summary>Proof</summary>

1. For any $$X\in \mathfrak{g}_\alpha, Y\in \mathfrak{g}_\beta$$, and $$H\in \mathfrak{h}$$,
    
    $$[H,[X,Y]]=[[H,X],Y]+[X,[H,Y]]=[\alpha(H)X,Y]+[X,\beta(H)Y]=(\alpha+\beta)(H)[X,Y]$$

    holds.
2. For any $$X\in \mathfrak{g}_\alpha, Y\in \mathfrak{g}_\beta$$, and $$H\in \mathfrak{h}$$, by the $$\ad$$-invariance of $$K$$ we obtain
    
    $$0=K([H,X],Y)+K(X,[H,Y])=K(\alpha(H),X)+K(X,\beta(H)Y)=(\alpha+\beta)(H)K(X,Y).$$

    If $$\alpha+\beta\neq 0$$, then for this identity to hold for all $$H$$ we must have $$K(X,Y)=0$$.
3. Since the Killing form is non-degenerate on $$\mathfrak{g}$$, for any given $$X\in \mathfrak{g}_\alpha$$ there exists $$Z\in \mathfrak{g}$$ such that $$K(X,Z)\neq 0$$. What we need to show is that we can choose $$Z\in \mathfrak{g}_{-\alpha}$$. This is clear because if we decompose $$Z$$ according to the root decomposition, then by the second result the components corresponding to roots other than $$-\alpha$$ pair trivially with $$X$$ anyway.

</details>

## Example: $$\sl(2;\mathbb{C})$$

We know from [§Lie Groups, ⁋Proposition 12](/en/math/lie_theory/Lie_groups#prop12) that $$\sl(n;\mathbb{C})$$ is the set of $$n\times n$$ *traceless* matrices. Thus $$\sl(2;\mathbb{C})$$ has the following three elements as a basis:

$$H=\begin{pmatrix}1&0\\0&-1\end{pmatrix},\quad E=\begin{pmatrix}0&1\\0&0\end{pmatrix},\quad F=\begin{pmatrix}0&0\\1&0\end{pmatrix}.$$

Hence the multiplication structure of $$\sl(2;\mathbb{C})$$ is given by the following commutation relations:

$$[H,E]=2E,\quad [H,F]=-2F,\quad [E,F]=H.$$

We show that any $$\sl(2;\mathbb{C})$$-representation decomposes as a direct sum of irreducible representations. This is an obvious result for compact Lie groups, but remember that for non-compact groups such as $$\SL(n,\mathbb{C})$$ the existence of a Haar measure is not guaranteed, so ideas such as averaging an inner product via integration cannot be used.

Let an arbitrary finite-dimensional $$\sl_2$$-representation $$V$$ be given, and for each $$\lambda\in \mathbb{C}$$ define the weight space

$$V_\lambda=\{v\in V\mid H\cdot v=\lambda v\}.$$

Then by the commutation relations examined above,

$$E\cdot V_\lambda\subset V_{\lambda+2},\qquad F\cdot V_\lambda\subset V_{\lambda-2}$$

hold. For this reason we also call $$E$$ and $$F$$ the *raising operator* and *lowering operator*, respectively. On the other hand, since $$V$$ is finite-dimensional, in the weight decomposition

$$V=\bigoplus_{\lambda} V_\lambda$$

there exists $$\mu$$ such that $$V_\mu\neq 0$$ but $$V_{\mu+2}=0$$. Such a $$\mu$$ is called the *highest weight*, and an element of $$V_\mu$$ is called a *highest weight vector*. Then for a highest weight vector $$v$$ we know that the following two identities hold:

$$H\cdot v=\mu v,\qquad E\cdot v=0.$$

<div class="proposition" markdown="1">

<ins id="prop7">**Proposition 7**</ins> For any highest weight vector $$v_0\in V_\mu$$, defining

$$v_j=\frac{1}{j!}F^j v_0$$

the following hold:

$$H\cdot v_j=(\mu-2j)v_j,\quad F\cdot v_j=(j+1)v_{j+1},\quad E\cdot v_j=(\mu-j+1)v_{j-1}.$$

</div>
<details class="proof" markdown="1">
<summary>Proof</summary>

The first two identities are obvious, so it suffices to show the identity for $$E$$. We proceed by induction. The case $$j=0$$ is obvious, and if the given identity holds for $$j$$ then

$$E\cdot v_{j+1}=\frac{1}{j+1}EF\cdot v_j=\frac{1}{j+1}(FE+H)\cdot v_j$$

and by the induction hypothesis

$$E\cdot v_j=(\mu-j+1)v_{j-1}$$

and from the identity for $$H$$ we have $$H\cdot v_j=(\mu-2j)v_j$$, so substituting these yields the desired result.

</details>

Since $$V$$ is finite-dimensional, there exists a smallest integer $$m$$ such that $$v_{m+1}=0$$. Then for this $$m$$,

$$0=E\cdot v_{m+1}=(\mu-m)v_m$$

and by the minimality of $$m$$ we see that $$\mu=m$$ must hold. That is, the highest weight must be a non-negative integer.

<div class="definition" markdown="1">

<ins id="def8">**Definition 8**</ins> For a fixed integer $$m\geq 0$$, we define the $$\sl_2$$-representation $$V(m)$$ by the $$m+1$$ vectors $$v_0,\ldots, v_m$$ and the action from [Proposition 7](#prop7):

$$H\cdot v_j=(m-2j)v_j,\quad F\cdot v_j=(j+1)v_{j+1},\quad E\cdot v_j=(m-j+1)v_{j-1}.$$

Here $$v_{-1}=v_{m+1}=0$$.

</div>

It is not difficult to show that $$V(m)$$ is irreducible. Now for an arbitrary $$\sl_2$$-representation $$V$$, we can find the highest weight of $$V$$ and apply [Proposition 7](#prop7) to the highest weight vector; if any highest weight vectors remain, we repeat this process, thereby decomposing $$V$$ into irreducible $$\sl_2$$-representations.

## Root systems

The above example of $$\sl_2$$-representations plays a major role in what follows. First let us define the following.

<div class="definition" markdown="1">

<ins id="def9">**Definition 9**</ins> Fix a finite-dimensional vector space $$V$$ and an inner product $$( -,-)$$ on it. A finite set $$\Phi$$ of non-zero vectors in $$V$$ is called a *root system* if the following conditions are satisfied.

1. The elements of $$\Phi$$ span $$V$$.
2. If $$\alpha\in \Phi$$ and $$c\in \mathbb{R}$$, then $$c\alpha\in \Phi$$ only if $$c=\pm 1$$.
3. For each root $$\alpha\in\Phi$$, $$\Phi$$ is closed under the reflection $$s_\alpha$$ in the hyperplane perpendicular to $$\alpha$$. That is, for any $$\alpha,\beta\in \Phi$$,
    
    $$s_\alpha(\beta):=\beta-2\frac{(\beta,\alpha)}{(\alpha,\alpha)}\alpha\in \Phi.$$

4. For any roots $$\alpha,\beta\in\Phi$$, the quantity
    
    $$\langle \beta,\alpha\rangle:=2\frac{(\beta,\alpha)}{(\alpha,\alpha)}$$

    is always an integer.

</div>

Now fix a Cartan subalgebra $$\mathfrak{h}$$ of a semisimple complex Lie algebra $$\mathfrak{g}$$. Then first the following holds.

<div class="proposition" markdown="1">

<ins id="lem10">**Lemma 10**</ins> For a semisimple Lie algebra $$\mathfrak{g}$$, a Cartan subalgebra $$\mathfrak{h}$$, and the root decomposition

$$\mathfrak{g}=\mathfrak{h}\oplus\bigoplus_{\alpha\in \Phi} \mathfrak{g}_\alpha,$$

the following hold.

1. For any $$\alpha,\beta\in \Phi$$, we have $$[\mathfrak{g}_\alpha,\mathfrak{g}_\beta]\subseteq \mathfrak{g}_{\alpha+\beta}$$.
2. If $$\alpha+\beta\neq 0$$, then $$\mathfrak{g}_\alpha$$ and $$\mathfrak{g}_\beta$$ are orthogonal.
3. The restriction of the Killing form on $$\mathfrak{g}$$ to $$\mathfrak{h}$$ is non-degenerate.
4. The restriction of the Killing form on $$\mathfrak{g}$$ to $$\mathfrak{g}_\alpha\times \mathfrak{g}_{-\alpha} \rightarrow \mathbb{C}$$ is non-degenerate.

</div>
<details class="proof" markdown="1">
<summary>Proof</summary>

The first claim is obvious. For the second claim, for any $$X_\alpha\in \mathfrak{g}_\alpha, X_\beta\in \mathfrak{g}_\beta$$ and any $$H\in \mathfrak{h}$$, by the $$\ad$$-invariance of $$K$$ we obtain the identity

$$0=K([H,X_\alpha],X_\beta)+K(X_\alpha, [H,X_\beta])=K(\alpha(H)X_\alpha, X_\beta)+K(X_\alpha,\beta(H)X_\beta)=(\alpha+\beta)(H)K(X_\alpha,X_\beta).$$

Therefore if $$\alpha+\beta\neq 0$$, then $$\mathfrak{g}_\alpha$$ and $$\mathfrak{g}_\beta$$ are orthogonal with respect to $$K$$.

To show the third claim, recall that for any $$H\in \mathfrak{h}$$ there exists $$X\in \mathfrak{g}$$ such that $$K(H,X)\neq 0$$. What we newly need to show is that we can choose $$X$$ from $$\mathfrak{h}$$. Writing $$X$$ in the form of a root decomposition $$\sum X_\alpha$$, by the above result we know that when we apply $$K(H,-)$$, all $$X_\alpha$$ except $$X_0\in \mathfrak{h}$$ give $$0$$. Hence $$K(H,H_0)\neq 0$$.

The fourth claim is proved in exactly the same way as the third.

</details>

Since the Killing form defined on $$\mathfrak{g}$$ is also non-degenerate on $$\mathfrak{h}$$, the following isomorphism induced from it exists:

$$\mathfrak{h}\rightarrow \mathfrak{h}^\ast;\qquad H\mapsto K(H, -).$$

Then $$\Phi\subseteq \mathfrak{h}^\ast$$ is a spanning set of $$\mathfrak{h}^\ast$$. If there were an element of $$\mathfrak{h}^\ast$$ not expressible as a linear combination of elements of $$\Phi$$, the corresponding element of $$\mathfrak{h}$$ would have to satisfy $$\alpha(H)=0$$ for all $$\alpha\in \Phi$$. Now for any root space $$\mathfrak{g}_\alpha$$, $$H$$ acts by

$$[H,X]=\alpha(H)X=0\qquad\text{for all $X\in \mathfrak{g}_\alpha$}$$

and since $$\mathfrak{h}$$ is abelian it acts by $$0$$ on itself. That is, considering the root decomposition of $$\mathfrak{g}$$, $$H$$ acts by $$0$$ on every element of $$\mathfrak{g}$$, and from this we know that $$H$$ commutes with every element of $$\mathfrak{g}$$ under the Lie bracket. But by [Proposition 3](#prop3), $$\mathfrak{g}$$ cannot have a nonzero abelian ideal, and in particular $$Z(\mathfrak{g})=0$$ must hold, so $$H=0$$.

From this we know that $$\Phi$$ spans $$\mathfrak{h}^\ast$$. However, $$\mathfrak{h}^\ast$$ is a complex vector space, and the Killing form defined on it is not guaranteed to be positive definite, so it is not an inner product. To remedy this, we consider the real span of the dual elements of $$\Phi$$ and show that the restriction of the Killing form to it becomes positive-definite. This requires a somewhat more detailed analysis of the root decomposition.

For each root $$\alpha\in\Phi$$, by the non-degeneracy of the Killing form there exists $$H_\alpha\in \mathfrak{h}$$ satisfying

$$\alpha(X)=K(H_\alpha,X)\qquad\text{for all $X\in \mathfrak{h}$}.$$

Our first observation is the following lemma.

<div class="proposition" markdown="1">

<ins id="lem11">**Lemma 11**</ins> For any $$E\in \mathfrak{g}_\alpha$$ and $$F\in \mathfrak{g}_{-\alpha}$$, we have $$[E,F]=K(E,F)H_\alpha$$.

</div>
<details class="proof" markdown="1">
<summary>Proof</summary>

By the $$\ad$$-invariance of $$K$$,

$$K([E,F],H)=K(F,[H,E])$$

holds for all $$H\in \mathfrak{h}$$. On the other hand, since $$E\in \mathfrak{g}_\alpha$$,

$$[H,E]=\alpha(H)E=K(H_\alpha,H)E$$

and substituting this into the above identity gives

$$K([E,F],H)=K(F,[H,E])=K(F, K(H_\alpha,H)E)=K(H_\alpha,H)K(F,E)=K(K(F,E)H_\alpha,H)$$

which holds for all $$H$$, yielding the desired result.

</details>

On the other hand, from [Lemma 10](#lem10) we can choose $$E\in \mathfrak{g}_\alpha$$ and $$F\in \mathfrak{g}_{-\alpha}$$ such that $$K(E,F)\neq 0$$. Then by the above result they satisfy the relations

$$[E,F]=K(E,F)H_\alpha,\quad [H_\alpha,E]=\alpha(H_\alpha)E=K(\alpha,\alpha)E,\quad [H_\alpha,F]=-\alpha(H_\alpha)F=-K(\alpha,\alpha)F.$$

This has a form similar to the commutation relations of the $$\sl_2$$-representation examined above, and indeed it is not difficult to show that $$(\alpha,\alpha)\neq 0$$. Therefore, defining

$$h_\alpha=\frac{2}{K(\alpha,\alpha)}H_\alpha$$

and similarly by appropriate scaling of $$E$$ and $$F$$ we can choose $$e_\alpha\in \mathfrak{g}_\alpha$$ and $$f_\alpha\in \mathfrak{g}_{-\alpha}$$ satisfying

$$(e_\alpha,f_\alpha)(\alpha,\alpha)=2$$

and these satisfy the commutation relations

$$[e_\alpha,f_\alpha]=h_\alpha,\quad [h_\alpha,e_\alpha]=2e_\alpha,\quad [h_\alpha,f_\alpha]=-2f_\alpha.$$

That is, they give a subalgebra of $$\mathfrak{g}$$ isomorphic to $$\sl_2$$. Let us denote this by $$\sl_{2,\alpha}$$. Then via the adjoint action we can regard $$\mathfrak{g}$$ as an $$\sl_{2,\alpha}$$-representation.

In particular, let us examine how $$h_\alpha$$ acts on the elements of $$\mathfrak{g}$$. First, looking at how the adjoint action of $$h_\alpha$$ acts on a root space $$\mathfrak{g}_\beta$$ of $$\mathfrak{g}$$,

$$[h_\alpha, x]=\beta(h_\alpha)x\qquad\text{for all $x\in \mathfrak{g}_\beta$}$$

so $$\mathfrak{g}_\beta$$ is the weight space of weight $$\beta(h_\alpha)$$ for this action. But as we saw earlier, the weights of an $$\sl_2$$-representation are always integers, so this value $$\beta(h_\alpha)=\frac{2K(\alpha,\beta)}{K(\alpha,\alpha)}$$ must be an integer. Also, since any weight subspace of an $$\sl_2$$ representation is $$1$$-dimensional, each $$\mathfrak{g}_\beta$$ is also $$1$$-dimensional.

On the other hand, since we saw earlier that $$\mathfrak{h}$$ is generated by the $$H_\alpha$$, the $$h_\alpha$$, being constant multiples of them, also generate $$\mathfrak{h}$$. As mentioned earlier, to endow this with a root system structure we consider the *real* vector space generated by the $$h_\alpha$$:

$$\mathfrak{h}_\mathbb{R}=\span_\mathbb{R}\{h_\alpha\mid \alpha\in\Phi\}.$$

Then for two bases $$h_\alpha,h_\beta$$ on this space,

$$K(h_\alpha,h_\beta)=\tr_\mathfrak{g}(\ad h_\alpha\ad h_\beta)=\sum_{\gamma\in\Phi}\gamma(h_\alpha)\gamma(h_\beta)$$

holds. We proved earlier that these $$\gamma(h_\alpha),\gamma(h_\beta)$$ are integers, and therefore so is $$K(h_\alpha,h_\beta)$$. That is, the restriction of $$K$$ to $$\mathfrak{h}_\mathbb{R}$$ is real-valued, and now for any $$h\in \mathfrak{h}_\mathbb{R}$$,

$$K(h,h)=\tr(\ad_h\ad_h)=\sum_{\gamma\in\Phi}\gamma(h)^2\geq 0$$

so we know that $$K$$ is positive definite on $$\mathfrak{h}_\mathbb{R}$$. In particular, transferring this back to $$\mathfrak{h}^\ast$$, we can verify that the real span of $$\Phi$$ in $$\mathfrak{h}^\ast$$ forms a Euclidean space, and in the process of showing this we also showed that these roots satisfy the fourth condition of [Definition 9](#def9). Now what we need to show are the remaining conditions.

First we need to show that applying the reflection operator

$$s_\alpha(\beta)=\beta-\frac{2K(\alpha,\beta)}{K(\alpha,\alpha)}\alpha$$

again yields a root; this is obvious because applying $$\ad f_\alpha$$ $$\lvert \beta(h_\alpha)\rvert$$ times yields an isomorphism between $$\mathfrak{g}_\beta$$ and $$\mathfrak{g}_{s_\alpha(\beta)}$$.

For the second condition, if $$\beta=c\alpha$$ then

$$\frac{2K(\alpha,\beta)}{K(\alpha,\alpha)}=2c,\quad \frac{2K(\alpha,\beta)}{K(\beta,\beta)}=\frac{2}{c}$$

must both be integers, so $$c$$ must be one of $$\pm 1$$, $$\pm 2$$, $$\pm 1/2$$, and applying $$\sl_2$$-representation theory and integrality again yields the desired result. That is, we have proved the following.

<div class="proposition" markdown="1">

<ins id="prop12">**Proposition 12**</ins> The set $$\Phi$$ of roots defined in [Definition 4](#def4) is a root system in $$\mathfrak{h}^\ast$$.

</div>

## Examples

Now let us examine the following examples.

<div class="example" markdown="1">

<ins id="ex13">**Example 13**</ins> First consider the standard Euclidean space $$\mathbb{R}^{n+1}$$ and the subspace

$$V_n=\left\{(x_1,\ldots, x_{n+1}\mid x_1+\cdots+x_{n+1}=0\right\}.$$

We consider the subset of this vector space

$$\Phi(A_n)=\left\{e_i-e_j\mid 1\leq i\neq j\leq n+1\right\}.$$

Then we know that this set satisfies all the conditions of [Definition 5](#def5). That $$\Phi(A_n)$$ spans $$V_n$$, and that the second condition holds, are obvious. For the third condition, for any vector $$\mathbf{x}=(x_1,\ldots, x_{n+1})$$ and any $$\mathbf{e}_{ij}=e_i-e_j$$, the formula

$$s_{ij}(\mathbf{x})=\mathbf{x}-\langle \mathbf{x}, \mathbf{e}_{ij}\rangle\mathbf{e}_{ij}=(x_1,\ldots, x_{n+1})-(x_i-x_j)\mathbf{e}_{ij}$$

and this is given by swapping the $$i$$th and $$j$$th components of $$\mathbf{x}$$. Hence from this we know that the third condition of [Definition 5](#def5) holds, and the fourth condition is obvious.

</div>

Similarly we can consider the following example.

<div class="example" markdown="1">

<ins id="ex14">**Example 14**</ins> This time consider the standard Euclidean space $$\mathbb{R}^n$$. This time we consider the set

$$\Phi(D_n)=\left\{\pm e_i\pm e_j\mid 1\leq i \neq j\leq n\right\}.$$

That these vectors span $$\mathbb{R}^n$$ is obvious. This time we need to examine what reflections the $$\mathbf{e}_{ij}^\pm =e_i\pm e_j$$ define. We know that the $$e_i-e_j$$ swap the $$i$$th and $$j$$th components of a vector $$\mathbf{x}$$, and therefore it suffices to know what reflection $$e_i+e_j$$ defines. That is, considering the computation

$$s_{ij}^+(\mathbf{x})=\mathbf{x}-\langle\mathbf{x}, \mathbf{e}_{ij}^+\rangle\mathbf{e}_{ij}^+=(x_1,\ldots, x_n)-(x_i+x_j)\mathbf{e}_{ij}$$

we see that $$s_{ij}^+$$ swaps the $$i$$th and $$j$$th components of the given vector and then flips their signs.

</div>

As can be seen from the above examples, not all roots are needed to describe a root system. For instance, in the case of $$\Phi(A_n)$$,

$$e_i-e_k=(e_i-e_j)+(e_j-e_k)$$

holds, and from this we know that to describe $$\Phi(A_n)$$ we only need elements of the form $$e_i-e_{i+1}$$. In a similar manner we define the following.

<div class="definition" markdown="1">

<ins id="def15">**Definition 15**</ins> For a root system $$\Phi$$, a subset $$\Phi^+$$ of $$\Phi$$ is called a set of *positive roots* if for each root $$\alpha\in \Phi$$, exactly one of $$\alpha$$ and $$-\alpha$$ belongs to $$\Phi^+$$, and whenever $$\alpha,\beta\in \Phi^+$$ are given, $$\alpha+\beta\in \Phi^+$$ also holds. Fixing a set of positive roots $$\Phi^+$$, an element $$\alpha\in \Phi^+$$ is called a *simple root* if $$\alpha$$ cannot be written as a sum of two elements of $$\Phi^+$$.

</div>

Thus if we only know how the integer values

$$\langle\alpha_i,\alpha_j\rangle=2\frac{(\alpha_i,\alpha_j)}{(\alpha_j,\alpha_j)}$$

between simple roots are defined, we can know how the reflection $$s_j$$ corresponding to an arbitrary root $$\alpha_j$$ moves another root $$\alpha_i$$.

Now suppose a root system $$\Phi$$ and a set of simple roots $$\Delta=\left\{\alpha_1,\ldots, \alpha_l\right\}$$ are fixed. Then the *Cartan matrix* is defined as follows.

<div class="definition" markdown="1">

<ins id="def16">**Definition 16**</ins> In the above setting, the matrix

$$A=(a_{ij})_{1\leq i,j\leq l},\qquad a_{ij}=\langle \alpha_i,\alpha_j\rangle$$

is called the *Cartan matrix*.

</div>

By the definition of a root system, each entry $$a_{ij}$$ is an integer. Also it is obvious that for each $$i$$ we have $$a_{ii}=2$$.

On the other hand, from the identity

$$\langle\alpha,\beta\rangle \langle\beta,\alpha\rangle=4\frac{(\alpha,\beta)^2}{\lvert\alpha\rvert^2\lvert\beta\rvert^2}=4(\cos\theta)^2$$

and the fact that the left-hand side is an integer, we know that for any two roots $$\alpha,\beta$$ the possible values of $$\langle\alpha,\beta\rangle$$ are only $$0, \pm 1, \pm 2$$. Here $$\cos\theta$$ is the angle between the two roots $$\alpha,\beta$$, and the possible values it can take are

$$0, \pm \frac{1}{2}, \pm \frac{\sqrt{2}}{2}, \pm \frac{\sqrt{3}}{2}, \pm 1.$$

The cases $$\pm 1$$ are excluded by the second condition of [Definition 5](#def5), so roots can only form angles of $$30$$ degrees (or $$150$$ degrees), $$45$$ degrees (or $$135$$ degrees), or $$60$$ degrees (or $$120$$ degrees).

For example, suppose two roots $$\alpha,\beta$$ form an angle of $$30$$ or $$150$$ degrees. Then from

$$\langle\alpha,\beta\rangle\langle\beta,\alpha\rangle=3$$

we see that $$\langle\alpha,\beta\rangle$$ must be $$\pm 1$$ or $$\pm 3$$. Now from the identity

$$\langle \alpha,\beta\rangle =2\frac{(\alpha,\beta)}{\lvert\beta\rvert^2}=\frac{2\lvert\alpha\rvert\lvert\beta\rvert\cos\theta}{\lvert\beta\rvert^2}=\frac{\pm \sqrt{3}\lvert\alpha\rvert}{\lvert\beta\rvert}$$

taking the value $$\pm 1$$ or $$\pm 3$$, we know that the ratio of the lengths of $$\alpha$$ and $$\beta$$ must be $$\sqrt{3}$$. Similarly, if the angle between two roots $$\alpha,\beta$$ is $$45$$ or $$135$$ degrees, their length ratio must be $$\sqrt{2}$$, and if the angle is $$60$$ or $$120$$ degrees, the length ratio must be $$1$$.

## Weyl group

For each root $$\alpha$$ of a root system $$\Phi$$, the reflection $$s_\alpha$$ defines an automorphism of $$\Phi$$. Let us consider the group generated by these reflections.

<div class="definition" markdown="1">

<ins id="def17">**Definition 17**</ins> The *Weyl group* of a root system $$\Phi$$ is the subgroup of $$\Aut(\Phi)$$ generated by the reflections $$s_\alpha$$ ($$\alpha\in\Phi$$).

$$W(\Phi)=\langle s_\alpha\mid \alpha\in\Phi\rangle$$

</div>

The Weyl group is a finite group. Indeed, $$W$$ is a subgroup of the orthogonal group of the Euclidean space containing $$\Phi$$, and since $$\Phi$$ is a finite set, $$W$$ is also finite. Also, as checked in [Proposition 12](#prop12), since the reflection $$s_\alpha$$ is the reflection in the hyperplane perpendicular to $$\alpha$$, $$W$$ has the structure of a Coxeter group.

<div class="example" markdown="1">

<ins id="ex18">**Example 18**</ins> For $$\Phi(A_n)$$ examined in [Example 13](#ex13), the reflection $$s_{ij}$$ corresponds to the transposition swapping the $$i$$th and $$j$$th coordinates. Hence $$W(\Phi(A_n))\cong S_{n+1}$$. For $$\Phi(D_n)$$ of [Example 14](#ex14), the reflections include both coordinate swaps and sign changes, so $$W(\Phi(D_n))\cong(\mathbb{Z}/2\mathbb{Z})^{n-1}\rtimes S_n$$.

</div>

## Connection to Lie groups

So far we have defined the root system $$\Phi$$ of a semisimple Lie algebra $$\mathfrak{g}$$ and defined the Weyl group capturing its symmetry as the finite group generated by the reflections $$s_\alpha$$. On the other hand, in [§Torus Actions, §§Maximal tori](/en/math/lie_theory/torus_action#maximal-tori) we defined the Weyl group of a compact Lie group $$G$$ as $$W=N(T)/T$$. In this section we show that the two definitions naturally coincide.

First, let $$\mathfrak{g}$$ be the Lie algebra of a compact connected Lie group $$G$$. That $$\mathfrak{g}$$ is semisimple is equivalent to the universal cover of $$G$$ not having $$\mathbb{R}^n$$ as a factor. In this case, the Lie algebra $$\mathfrak{t}$$ of a maximal torus $$T$$ of $$G$$ becomes a Cartan subalgebra of $$\mathfrak{g}$$.

Now let us examine how $$N(T)$$ acts on $$\mathfrak{t}^\ast$$. For any $$n\in N(T)$$, the adjoint representation $$\Ad(n)$$ is an automorphism of $$\mathfrak{g}$$ and since $$nTn^{-1}=T$$, it preserves $$\mathfrak{t}$$. Therefore $$\Ad(n)\vert_\mathfrak{t}$$ is an automorphism of $$\mathfrak{t}$$, and dualizing this yields a linear action on $$\mathfrak{t}^\ast$$.

<div class="proposition" markdown="1">

<ins id="prop19">**Proposition 19**</ins> The action of $$N(T)$$ on $$\mathfrak{t}^\ast$$ preserves the root system $$\Phi$$.

</div>
<details class="proof" markdown="1">
<summary>Proof</summary>

For any $$n\in N(T)$$ and $$\alpha\in\Phi$$, it suffices to show that $$\Ad(n)$$ sends $$\mathfrak{g}_\alpha$$ to $$\mathfrak{g}_{n\cdot\alpha}$$. For any $$X\in\mathfrak{g}_\alpha$$ and $$H\in\mathfrak{t}$$,

$$[H,\Ad(n)X]=\Ad(n)[\Ad(n)^{-1}H,X]$$

and since $$\Ad(n)^{-1}H\in\mathfrak{t}$$ and $$X\in\mathfrak{g}_\alpha$$,

$$[\Ad(n)^{-1}H,X]=\alpha(\Ad(n)^{-1}H)X=(n^{-1}\cdot\alpha)(H)\cdot X.$$

Therefore

$$[H,\Ad(n)X]=(n^{-1}\cdot\alpha)(H)\cdot\Ad(n)X$$

and this means $$\Ad(n)X\in\mathfrak{g}_{n^{-1}\cdot\alpha}$$. That is, $$\Ad(n)$$ sends $$\mathfrak{g}_\alpha$$ to $$\mathfrak{g}_{n^{-1}\cdot\alpha}$$, and from this we know that $$n\cdot\alpha\in\Phi$$.

</details>

Thus we know that $$W=N(T)/T$$ has a well-defined action on $$\mathfrak{t}^\ast$$, and in particular on the root system $$\Phi$$. Now the key result is as follows.

<div class="proposition" markdown="1">

<ins id="prop20">**Proposition 20**</ins> For each root $$\alpha\in\Phi$$, there exists $$n_\alpha\in N(T)$$ satisfying $$\Ad(n_\alpha)\vert_\mathfrak{t}=s_\alpha$$. Therefore the Weyl group $$W=N(T)/T$$ defined from the Lie group and the Weyl group of the root system are isomorphic.

</div>
<details class="proof" markdown="1">
<summary>Proof</summary>

For any root $$\alpha\in\Phi$$, as examined earlier, $$\sl_{2,\alpha}=\langle e_\alpha, f_\alpha, h_\alpha\rangle$$ is a subalgebra of $$\mathfrak{g}$$ isomorphic to $$\sl(2;\mathbb{C})$$. The corresponding Lie subgroup $$G_\alpha$$ of $$G$$ is locally isomorphic to $$\SU(2)$$ or $$\SO(3)$$.

$$G_\alpha$$ intersects $$T$$ to form a $$1$$-dimensional torus $$T_\alpha=T\cap G_\alpha$$. Now we need to find an element of $$N(T)$$ whose $$\Ad$$-action induces the reflection $$s_\alpha$$ on $$\mathfrak{t}$$. For this purpose consider the element

$$n_\alpha=\exp(e_\alpha)\exp(-f_\alpha)\exp(e_\alpha).$$

By computation in $$\SU(2)$$ this corresponds to

$$\begin{pmatrix}0&1\\-1&0\end{pmatrix}$$

and this element sends elements of $$T_\alpha$$ to their inverses $$t\mapsto t^{-1}$$. Therefore $$\Ad(n_\alpha)$$ sends $$h_\alpha$$ to $$-h_\alpha$$ and preserves $$\ker\alpha$$. That is, $$\Ad(n_\alpha)\vert_\mathfrak{t}=s_\alpha$$.

Finally, let us verify that $$n_\alpha\in N(T)$$. Since $$\Ad(n_\alpha)$$ preserves $$\mathfrak{t}$$, $$n_\alpha Tn_\alpha^{-1}$$ and $$T$$ have the same Lie algebra, and since both are connected, $$n_\alpha Tn_\alpha^{-1}=T$$.

</details>

From this we know that the Weyl groups from the two perspectives are essentially the same object. From the Lie group perspective, $$W=N(T)/T$$ captures the conjugation action on the maximal torus, while from the Lie algebra perspective, $$W$$ captures the symmetry of the root system. The agreement of the two definitions is a concrete expression of the fact that the structure of a compact Lie group is completely determined by the root system of its Lie algebra.

Integrating these two perspectives, the geometric objects that naturally emerge from a root system, namely Borel subgroups and flag varieties, are treated in [§Borel Subgroups](/en/math/lie_theory/borel_subgroup).
