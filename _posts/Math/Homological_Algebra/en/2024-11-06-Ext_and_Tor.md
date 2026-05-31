---
title: "Ext and Tor"
description: "We define Ext as the right derived functor of the Hom functor and Tor as the left derived functor of the tensor product, and examine their computation via projective and injective resolutions and the associated long exact sequences."
excerpt: "Definitions and properties of Ext and Tor, the derived functors of Hom and tensor"

categories: [Math / Homological Algebra]
permalink: /en/math/homological_algebra/ext_and_tor
header:
    overlay_image: /assets/images/Math/Homological_Algebra/Ext_and_Tor.png
    overlay_filter: 0.5
sidebar:
    nav: "homological_algebra-en"

date: 2024-11-06
last_modified_at: 2026-04-09
weight: 6
translated_at: 2026-05-31T14:30:04+00:00
translation_source: kimi-cli
last_polished_at: 2026-05-31T14:30:04+00:00
---
In the previous post we defined right/left derived functors for general left/right exact functors. In this post we study the derived functors of the left exact functor $$\Hom$$ and the right exact functor $$\otimes$$ defined on $$\lMod{A}$$.

## The Ext Functor

For any $$M\in\lMod{A}$$, the functor $$\Hom_\lMod{A}(M,-)$$ is a left exact functor from $$\lMod{A}$$ to $$\Ab$$. Thus we make the following definition.

<div class="definition" markdown="1">

<ins id="def1">**Definition 1**</ins> We define the right derived functor of the left exact functor $$\Hom_\lMod{A}(M,-):\lMod{A} \rightarrow \Ab$$ by

$$\Ext_A^i(M,N)=R^i\Hom_\lMod{A}(M,-)(N)$$

and call these the *$$\Ext$$ groups*.

</div>

$$\Hom_\lMod{A}(-,N)$$ is an exact functor if and only if $$N$$ is an injective object. ([\[Multilinear Algebra\] §Projective, Injective, and Flat Modules, ⁋Definition 3](/en/math/multilinear_algebra/various_modules#def3)) From the viewpoint of derived functors, if $$N$$ were an injective module then $$0 \rightarrow N \rightarrow N \rightarrow 0$$ would be an injective resolution, so we would know that $$\Ext_A^1(M,N)=0$$ for all $$M$$. Then for any short exact sequence

$$0 \rightarrow M_1 \rightarrow M_2 \rightarrow M_3 \rightarrow 0$$

applying $$\Hom_\lMod{A}(-,N)$$ and considering the associated long exact sequence of derived functors

$$\begin{aligned}0 &\rightarrow \Hom_\lMod{A}(M_3, N) \rightarrow \Hom_\lMod{A}(M_2, N) \rightarrow \Hom_\lMod{A}(M_1, N)\\
&\rightarrow\Ext_A^1(M_3,N) \rightarrow\Ext_A^1(M_2,N) \rightarrow\cdots\end{aligned}$$

we see from $$\Ext_A^1(M_3,N)=0$$ that $$\Hom_\lMod{A}(-,N)$$ is exact.

On the other hand, instead of [Definition 1](#def1), we could have defined $$\Ext$$ as the right derived functor of the left exact functor $$\Hom_\lMod{A}(-,N):\lMod{A} \rightarrow \Ab$$ for a fixed $$N$$. That these two definitions agree is verified in [Proposition 3](#prop3) below.

## The Tor Functor

For any $$N\in\rMod{A}$$, the functor $$-\otimes_A N$$ is a right exact functor from $$\lMod{A}$$ to $$\Ab$$, so we may consider its left derived functor.

<div class="definition" markdown="1">

<ins id="def2">**Definition 2**</ins> We define the left derived functor of the right exact functor $$-\otimes_A N:\lMod{A} \rightarrow \Ab$$ by

$$\Tor_i^A(M,N)=L_i(-\otimes_A N)(M)$$

and call these the *$$\Tor$$ groups*.

</div>

To compute $$\Tor$$ we must use a projective resolution of $$M$$. Thus, just as in the computation above, if $$M$$ were a projective $$A$$-module then $$0 \rightarrow M \rightarrow M \rightarrow 0$$ would be a projective resolution of $$M$$, and from this $$\Tor_1^A(M,N)=0$$ would hold for all $$N$$. In other words, we see once again that every projective $$A$$-module is a flat $$A$$-module.

## Balancing

Essentially $$\Hom$$ and $$\otimes$$ are bifunctors taking two objects. Hence, depending on which of the two inputs we replace by an injective resolution or a projective resolution, different results might arise, which would be undesirable. For example, to compute $$\Ext_A^i(M,N)$$, we could use a projective resolution $$P_\bullet\rightarrow M\rightarrow 0$$ of $$M$$ and take the $$i$$-th cohomology of

$$0\rightarrow \Hom_{\lMod{A}}(M, N)\rightarrow \Hom_{\lMod{A}}(P_0,N)\rightarrow \Hom_{\lMod{A}}(P_1, N)\rightarrow\cdots$$

or we could use an injective resolution $$0\rightarrow N\rightarrow I^\bullet$$ of $$N$$ and consider

$$0\rightarrow \Hom_{\lMod{A}}(M, N)\rightarrow \Hom_{\lMod{A}}(M, I^0)\rightarrow \Hom_{\lMod{A}}(M, I^1)\rightarrow\cdots$$

Only if these two results agree can we say that $$\Ext$$ is "well" defined. Likewise, the value of $$\Tor^A_i(M,N)$$ should not depend on which of the following two chain complexes we choose:

$$\cdots\rightarrow P_1\otimes_AN \rightarrow P_0\otimes_AN \rightarrow M\otimes_AN\rightarrow0$$

and

$$\cdots \rightarrow M\otimes_AN_1\rightarrow M\otimes_AN_0\rightarrow M\otimes_A N\rightarrow0$$.

We must therefore compare the cohomologies they yield. The proof strategy is to consider a double complex whose $$(p,q)$$-entry is $$\Hom_{\lMod{A}}(P_q, I^p)$$ (or, in the tensor case, $$P_p\otimes P'_q$$). ([§Homology, ⁋Definition 4](/en/math/homological_algebra/homology#def4))

<div class="proposition" markdown="1">

<ins id="prop3">**Proposition 3**</ins> For two $$A$$-modules $$M \in \lMod{A}$$, $$N \in \lMod{A}$$, and their projective resolution $$P_\bullet\rightarrow M\rightarrow 0$$ and injective resolution $$0\rightarrow N\rightarrow I^\bullet$$, the following isomorphism holds:

$$H^n(\Hom_\lMod{A}(M, I^\bullet)) \cong H^n(\Hom_\lMod{A}(P_\bullet, N))$$

Here $$P_\bullet \to M$$ is a projective resolution of $$M$$, and $$N \to I^\bullet$$ is an injective resolution of $$N$$.

</div>

<details class="proof" markdown="1">
<summary>Proof</summary>

Consider the double complex

$$K^{p,q}=\Hom_\lMod{A}(P_q, I^p)$$

The horizontal differential $$d_h:K^{p,q} \rightarrow K^{p+1,q}$$ is obtained by applying $$\Hom_\lMod{A}(P_q,-)$$ to $$I^p\rightarrow I^{p+1}$$, and similarly the vertical differential $$d_v: K^{p,q}\rightarrow K^{p,q+1}$$ is obtained by applying $$\Hom_\lMod{A}(-,I^p)$$ to $$P_{q+1}\rightarrow P_q$$. Now consider the total complex $$\Tot(K)^\bullet$$ of this double complex. ([§Homology, ⁋Definition 5](/en/math/homological_algebra/homology#def5)) Then the stated isomorphism is obtained by computing the $$n$$-th cohomology of $$\Tot(K)^\bullet$$ in two different ways.

To verify this, we first check that the cohomologies of the rows $$K^{\bullet, q}$$ and columns $$K^{p,\bullet}$$ of the cochain complex are given by

$$H^q(K^{p, \bullet}) = \begin{cases} \Hom_\lMod{A}(M, I^p) & q = 0 \\ 0 & q > 0, \end{cases}\qquad H^p(K^{\bullet, q}) = \begin{cases} \Hom_\lMod{A}(P_q, N) & p = 0 \\ 0 & p > 0. \end{cases}\tag{$\ast$}$$

Here, the vanishing of cohomology follows from the definitions of projective and injective modules. ([\[Multilinear Algebra\] §Projective, Injective, and Flat Modules, ⁋Definition 3](/en/math/multilinear_algebra/various_modules#def3))

As in the computation carried out right after [§Homology, ⁋Definition 5](/en/math/homological_algebra/homology#def5), computing the cohomology of the total complex requires some care because the differentials mix the terms. For this we use a *filtration*.

First, consider the filtration on $$\Tot(K)^\bullet$$ defined by

$$F^p \Tot(K)^k = \bigoplus_{\substack{i \geq p \\ i+q=k}} K^{i,q}$$

This extracts, in degree $$k$$ of the total complex, only those terms whose horizontal component is at least $$p$$; by definition $$F^0\Tot(K)^\bullet=\Tot(K)^\bullet$$, and it is obvious that $$F^p\Tot(K)^k=0$$ for $$p>k$$.

Now the inclusion induces a short exact sequence

$$0 \rightarrow F^{p+1} \Tot(K)^k \rightarrow F^{p} \Tot(K)^k \rightarrow K^{p, k-p} \rightarrow 0$$

and promoting this to complexes yields

$$0 \rightarrow F^{p+1}\Tot(K)^\bullet \rightarrow F^p \Tot(K)^\bullet \rightarrow K^{p, \bullet-p} \rightarrow 0$$

That is, although the cohomology of $$\Tot(K)^\bullet$$ is difficult to compute directly, imposing a filtration relates it to the cohomology of the columns, so we can exploit the computation ($$\ast$$) above.

Now let us compute $$H^n(F^p\Tot(K)^\bullet)$$ for a fixed $$n$$, and from this deduce $$H^n(F^0\Tot(K)^\bullet)=H^n(\Tot(K)^\bullet)$$. From the short exact sequence above we obtain the long exact sequence in cohomology

$$\cdots\rightarrow H^{n-1}(K^{p, \bullet-p})\rightarrow H^n(F^{p+1}\Tot(K)^\bullet)\rightarrow H^n(F^p\Tot(K)^\bullet)\rightarrow H^n(K^{p, \bullet-p})\rightarrow \cdots$$

and from ($$\ast$$) we see that

$$H^n(F^p\Tot(K)^\bullet)\cong H^n(F^{p+1}\Tot(K)^\bullet)\tag{$\ast\ast$}$$

holds in all parts except the nontrivial parts of $$H^{n-1}(K^{p,\bullet-p})$$ and $$H^n(K^{p,\bullet-p})$$, that is, except when $$p=n$$ or $$p=n-1$$.

Now consider the case $$p=n$$. The long exact sequence is

$$0=H^n(F^{n+1}\Tot(K)^\bullet)\rightarrow H^n(F^n\Tot(K)^\bullet)\rightarrow \Hom_\lMod{A}(M, I^n)\rightarrow H^{n+1}(F^{n+1}\Tot(K)^\bullet)\rightarrow \cdots$$

and from this we know that $$H^n(F^n\Tot(K)^\bullet)$$ is the kernel of the connecting homomorphism

$$\delta_n:\Hom_\lMod{A}(M, I^n)\rightarrow H^{n+1}(F^{n+1}\Tot(K)^\bullet)$$

By the same logic $$H^{n+1}(F^{n+1}\Tot(K)^\bullet)$$ embeds into $$\Hom_\lMod{A}(M, I^{n+1})$$, and an explicit computation shows that $$\delta_n$$ comes exactly from $$\Hom_\lMod{A}(M, I^n)\rightarrow \Hom_\lMod{A}(M, I^{n+1})$$. Hence

$$H^n(F^n\Tot(K)^\bullet)=\ker\left(\Hom_\lMod{A}(M, I^n)\rightarrow \Hom_\lMod{A}(M, I^{n+1})\right)$$

Now analyzing the cohomology long exact sequence for the case $$p=n-1$$ on the basis of this,

$$\cdots \longrightarrow \Hom_\lMod{A}(M, I^{n-1}) \overset{\delta_{n-1}}{\longrightarrow} H^n(F^n\Tot(K)^\bullet) \longrightarrow H^n(F^{n-1}\Tot(K)^\bullet) \longrightarrow 0$$

we see that $$H^n(F^{n-1}\Tot(K)^\bullet)$$ is the cokernel of the connecting homomorphism $$\delta_{n-1}$$. Here $$H^n(F^n\Tot(K)^\bullet)$$ was already found in the case $$p=n$$, and the connecting homomorphism $$\delta_{n-1}$$ again comes from $$\Hom_\lMod{A}(M, I^{n-1})\rightarrow \Hom_\lMod{A}(M, I^{n})$$, so we obtain

$$H^n(F^{n-1}\Tot(K)^\bullet)=\frac{\ker(\Hom_\lMod{A}(M, I^n) \to \Hom_\lMod{A}(M, I^{n+1}))}{\im(\Hom_\lMod{A}(M, I^{n-1}) \to \Hom_\lMod{A}(M, I^n))}$$

Now for $$p< n-1$$, using the isomorphism ($$\ast\ast$$) we see that every case is isomorphic to the case $$p=n-1$$, and in particular

$$H^n(\Tot(K)^\bullet) = H^n(F^0\Tot(K)^\bullet) = H^n(F^1\Tot(K)^\bullet) = \cdots = H^n(F^{n-1}\Tot(K)^\bullet) = H^n(\Hom_\lMod{A}(M, I^\bullet))$$

Similarly, computing with the following filtration on $$\Tot(K)^\bullet$$,

$$G^q \Tot(K)^k = \bigoplus_{\substack{j \geq q \\ p+j=k}} K^{p,j}$$

we obtain $$H^n(\Tot(K)^\bullet) = H^n(\Hom_\lMod{A}(P_\bullet, N))$$, and from this we get the desired result.

</details>

In a similar way one can prove balancing for $$\Tor$$. The proof structure is the same; the only difference is that projective modules are flat modules ([\[Multilinear Algebra\] §Projective, Injective, and Flat Modules, ⁋Definition 7](/en/math/multilinear_algebra/various_modules#def7)), and this is used to handle the computation. We omit the detailed proof.

<div class="proposition" markdown="1">

<ins id="prop4">**Proposition 4**</ins> For two $$A$$-modules $$M \in \lMod{A}$$, $$N \in \lMod{A}$$, and their projective resolutions $$P_\bullet\rightarrow M\rightarrow 0$$, $$P_\bullet'\rightarrow N\rightarrow 0$$,

$$H_n(P_\bullet \otimes_A N) \cong H_n(M \otimes_A P'_\bullet)$$

holds.

</div>

## Examples

Finally, let us look at computations of Ext and Tor a little more concretely.

<div class="proposition" markdown="1">

<ins id="prop5">**Proposition 5**</ins> For two integers $$n, m \in \mathbb{Z}$$, the following holds:

$$\Tor_i^\mathbb{Z}(\mathbb{Z}/n\mathbb{Z}, \mathbb{Z}/m\mathbb{Z}) \cong \begin{cases} \mathbb{Z}/(n,m)\mathbb{Z} & i = 0, 1\\ 0 & i \geq 2. \end{cases}$$

Here $$(m,n)$$ is the greatest common divisor of $$m$$ and $$n$$.

</div>

<details class="proof" markdown="1">
<summary>Proof</summary>

The case $$i=0$$ is a standard computation, so let us verify that the sequence

$$0 \rightarrow \mathbb{Z}\rightarrow \mathbb{Z}\rightarrow \mathbb{Z}/n\mathbb{Z}\rightarrow 0$$

constitutes a projective resolution $$P_\bullet\rightarrow \mathbb{Z}/n\mathbb{Z}\rightarrow 0$$ of $$\mathbb{Z}/n\mathbb{Z}$$. Here the first map is multiplication by $$n$$ on $$\mathbb{Z}$$. To compute $$\Tor$$ we apply $$-\otimes_\mathbb{Z}\mathbb{Z}/m\mathbb{Z}$$ to this. Since $$\mathbb{Z}\otimes_\mathbb{Z}\mathbb{Z}/m\mathbb{Z}=\mathbb{Z}/m\mathbb{Z}$$, the projective resolution after taking the tensor product is

$$0\rightarrow \mathbb{Z}/m\mathbb{Z}\rightarrow \mathbb{Z}/m\mathbb{Z}\rightarrow 0$$

and thus the first homology is

$$H_1(P_\bullet)=\ker(\cdot n)= \{a \in \mathbb{Z}/m\mathbb{Z} \mid na \equiv 0 \pmod{m}\}=\mathbb{Z}/(m,n)\mathbb{Z}$$

which gives the desired result.

</details>

This proposition reveals the origin of the name $$\Tor$$: $$\Tor_1^\mathbb{Z}(\mathbb{Z}/n\mathbb{Z}, \mathbb{Z}/m\mathbb{Z})$$ is nontrivial exactly when $$(n,m) > 1$$, i.e. when there exists an $$n$$-torsion element in $$\mathbb{Z}/m\mathbb{Z}$$, and then the greatest common divisor $$(n,m)$$ can be thought of as measuring the amount of torsion.

We can examine the analogous statement for $$\Ext$$ in a similar way.

<div class="proposition" markdown="1">

<ins id="prop6">**Proposition 6**</ins> For any abelian group $$A$$ and $$n \in \mathbb{Z}$$, the following holds:

$$\Ext^i_\mathbb{Z}(\mathbb{Z}/n\mathbb{Z}, A) \cong \begin{cases} A[n] & i = 0, \\ A/nA & i = 1, \\ 0 & i \geq 2. \end{cases}$$

Here $$A[n] = \{a \in A \mid na = 0\}$$ is the $$n$$-torsion subgroup.

</div>

<details class="proof" markdown="1">
<summary>Proof</summary>

Consider the same projective resolution as in [Proposition 5](#prop5),

$$0 \rightarrow \mathbb{Z}\rightarrow \mathbb{Z}\rightarrow \mathbb{Z}/n\mathbb{Z}\rightarrow 0$$

and apply $$\Hom_\mathbb{Z}(-,A)$$. Then $$\Hom_\mathbb{Z}(\mathbb{Z},A)$$ is determined by the image of $$1$$, so $$\Hom_\mathbb{Z}(\mathbb{Z}, A)\cong A$$, and from this we obtain the complex

$$0 \to A \xrightarrow{\cdot n} A \to 0$$

Here the first map is $$a \mapsto na$$, and therefore the first cohomology is

$$\Ext^1_\mathbb{Z}(\mathbb{Z}/n\mathbb{Z}, A) \cong \coker(\cdot n ) = A/nA$$

That $$\Hom_\mathbb{Z}(\mathbb{Z}/n\mathbb{Z}, A)=A[n]$$ is a simple computation.

</details>

More generally, $$\Ext^1(M,N)$$ is connected to equivalence classes of short exact sequences of the form $$0 \to N \to E \to M \to 0$$, i.e. extensions of $$M$$ by $$N$$, which can be seen through Yoneda Ext. ([Wikipedia](https://en.wikipedia.org/wiki/Ext_functor)) Although less intuitive than [Proposition 5](#prop5), [Proposition 6](#prop6) can also be said to show the origin of the name $$\Ext$$ in this sense.

Finally we define the following.

<div class="definition" markdown="1">

<ins id="def7">**Definition 7**</ins> Let a commutative ring $$A$$, a free $$A$$-module $$F$$ of rank $$n$$, and an $$A$$-linear map $$\varphi : F \to A$$ be given. Then the *Koszul complex* $$K(\varphi)_\bullet$$ is the exterior algebra $$K=\bigwedge F$$ equipped with a chain complex structure as follows:

1. For each $$i$$, $$K_i = \bigwedge\nolimits^i F$$.
2. For each $$i$$, $$d_i: K_i \to K_{i-1}$$ is a graded derivation of degree $$-1$$ uniquely determined by the formula $$d(f) = \varphi(f)$$ and the Leibniz rule

    $$d(\xi \wedge \eta) = d(\xi) \wedge \eta + (-1)^{\degree(\xi)} \, \xi \wedge d(\eta)$$.

</div>

Defining the augmentation map $$\epsilon: K_0=A\to A/\im\varphi$$ as the canonical projection, we can regard $$K(\varphi)_\bullet$$ as a resolution of $$A/\im\varphi$$. For convenience, fix a basis $$e_1, \ldots, e_n$$ of $$F$$ and set $$\x_i = \varphi(e_i)$$; then $$\im\varphi = (\x_1, \ldots, \x_n)$$, so we also write this as $$K_\bullet(\x_1, \ldots, \x_n)$$.

If $$\x_1, \ldots, \x_n$$ is a regular sequence in $$A$$, then the Koszul complex becomes a *free resolution* of $$A/(\x_1, \ldots, \x_n)$$. ([\[Commutative Algebra\] §Regular Local Rings, ⁋Definition 2](/en/math/commutative_algebra/regular_local_rings#def2)) That is,

$$0 \to K_n \to \cdots \to K_1 \xrightarrow{d_1} A \xrightarrow{\epsilon} A/(\x_1, \ldots, \x_n) \to 0$$

is exact.

We prove this by induction on $$n$$. The case $$n = 0$$ is trivial, so assume that $$K(\x_1, \ldots, \x_{n-1})$$ is exact for $$n-1$$ elements.

Since $$\x_n$$ is the last element of the regular sequence, $$\x_n$$ is a non-zerodivisor on $$A/(\x_1, \ldots, \x_{n-1})$$. Therefore, letting $$\bar{\x}_i$$ be the image of $$\x_i$$ in $$A/(\x_n)$$, the sequence $$\bar{\x}_1, \ldots, \bar{\x}_{n-1}$$ becomes a regular sequence in $$A/(\x_n)$$, and by the inductive hypothesis $$K'_\bullet = K(\bar{\x}_1, \ldots, \bar{\x}_{n-1})$$ is a free resolution of $$A/(\x_1, \ldots, \x_n)$$.

Now observing $$K(\x_1, \ldots, \x_n)_i$$, by definition

$$K(\x_1, \ldots, \x_n)_i \cong K'_i \oplus K'_{i-1} \cdot e_n$$

and $$d_i$$ has the form of the matrix

$$d_i = \begin{pmatrix} d'_i & (-1)^i \x_n \\ 0 & d'_{i-1} \end{pmatrix}$$

If $$(\alpha, \beta) \in \ker d_i$$, then $$d'_{i-1}(\beta) = 0$$, so by the inductive hypothesis there exists $$\gamma$$ with $$\beta = d'_i(\gamma)$$. Moreover $$d'_i(\alpha) = (-1)^{i+1} \x_n \beta$$, so $$d'_i(\alpha + (-1)^{i+1} \x_n \gamma) = 0$$, and again by the inductive hypothesis $$\alpha + (-1)^{i+1} \x_n \gamma \in \im d'_{i+1}$$. Hence $$\ker d_i \subseteq \im d_{i+1}$$, and the reverse inclusion is obvious.

This applies especially well to the case where $$A=\mathbb{K}[\x_1,\ldots, \x_n]$$ is a polynomial algebra over a field $$\mathbb{K}$$ and $$(\x_1,\ldots, \x_n)$$ is a regular sequence. In this case $$F=\bigoplus_1^nAe_i$$ and the augmentation map is given by $$e_i\mapsto \x_i$$. By the discussion above the Koszul complex becomes a free resolution of $$\mathbb{K}$$, and since each $$K_i$$ is a free $$A$$-module, applying $$-\otimes_A\mathbb{K}$$ yields the complex

$$0 \to \bigwedge\nolimits^n \mathbb{K}^n \to \cdots \to \bigwedge\nolimits^1 \mathbb{K}^n \to \bigwedge\nolimits^0 \mathbb{K}^n \to 0$$

which is a resolution of $$A/(\x_1,\ldots, \x_n)\cong \mathbb{K}$$. On the other hand, since $$d_i$$ is induced from $$\varphi$$, applying $$-\otimes_A \mathbb{K}$$ sends all $$\x_j$$-coefficients to $$0$$, so $$d_i \otimes 1 = 0$$. Therefore we obtain

$$\Tor_i^A(\mathbb{K}, \mathbb{K}) = H_i(K_\bullet \otimes_A \mathbb{K}) = K_i \otimes_A \mathbb{K} \cong \bigwedge\nolimits^i_{\mathbb{K}}(\mathbb{K}^n).$$

This computation is later used to show that the global dimension of the polynomial ring $$\mathbb{K}[\x_1, \ldots, \x_n]$$ is $$n$$. ([##ref##](global-dimension/호몰로지?가환대수?))
