---
title: "Kodaira Vanishing Theorem"
description: "While the Serre vanishing theorem guarantees cohomology vanishing only in sufficiently high degrees, the Kodaira vanishing theorem shows that higher cohomology always vanishes in all degrees for the tensor product of the canonical line bundle and an ample line bundle. We also explore its uses and applications in algebraic geometry."
permalink: /en/math/algebraic_varieties/kodaira_vanishing
excerpt: "The Kodaira vanishing theorem and its applications"
categories: [Math / Algebraic Varieties]

sidebar:
    nav: "algebraic_varieties-en"
    
date: 2026-05-07
weight: 18
translated_at: 2026-08-19T02:15:04+00:00
translation_source: kimi-cli
last_polished_at: 2026-09-28T11:15:06+00:00
translation_polish_source: antigravity-gemini-3.8-flash-high
---
[§Cohomology of Projective Space, ⁋Proposition 7](/en/math/algebraic_varieties/cohomology_of_projective_spaces#prop7){: data-lid="oybpy" }'s Serre vanishing theorem guarantees that for an ample line bundle $\mathcal{L}$ and a coherent sheaf $\mathcal{F}$ on a projective variety, for sufficiently large $m$, $H^i(X, \mathcal{F} \otimes \mathcal{L}^{\otimes m}) = 0$ ($i > 0$) holds. However, this result is merely an asymptotic property and gives no information about specifically from which $m$ vanishing begins.

The Kodaira vanishing theorem is a far more refined result, guaranteeing that for the canonical bundle $\omega_X$ and an ample line bundle $\mathcal{L}$, the higher cohomology of the tensor product $\omega_X \otimes \mathcal{L}$ *always* vanishes. In this post we examine the Kodaira vanishing theorem, its applications, and how this theorem is used in algebraic geometry.

## Kodaira Vanishing Theorem

The basic setup we will consider is as follows. $X$ is an $n$-dimensional smooth projective variety, $\mathcal{L}$ is an ample line bundle on $X$, and $\omega_X = \det \Omega_X^1 = \Omega_X^n$ is the canonical line bundle. ([§Canonical Line Bundle, ⁋Definition 5](/en/math/algebraic_varieties/canonical_bundle#def5){: data-lid="2g869" }) Then the Kodaira vanishing theorem can be written as follows.

::: Proposition 1 (Kodaira vanishing)
When $\operatorname{char}\mathbb{K} = 0$, let an $n$-dimensional smooth projective variety $X$ and an ample line bundle $\mathcal{L}$ be given. Then for all $p > 0$,
 
$$H^p(X, \omega_X \otimes \mathcal{L}) = 0$$

holds. More generally, whenever $p+q>n$, for such $p,q$,

$$H^p(X, \Omega^q\otimes \mathcal{L})=0$$

holds. 
:::

The first statement is obtained from the second by setting $q=n$, and we have already seen it in [§The Riemann-Roch Theorem on Surfaces, ⁋Proposition 7](/en/math/algebraic_varieties/riemann_roch_surfaces#prop7){: data-lid="cptbb" }. The second statement extends this to an arbitrary form degree $q$ and is called Akizuki–Nakano vanishing. The proof of this proposition is quite technical, so in this post we focus on how it is used in algebraic geometry rather than giving a rigorous proof.

As can be seen from the statement of the proposition, Kodaira vanishing eliminates higher cohomology after twisting by the canonical bundle. Using Serre duality, this can be rewritten as the following equivalent statement.

::: Proposition 2
Under the hypotheses of [Proposition 1](#prop1){: data-lid="difla" }, for all $p < n$,

$$H^p(X, \mathcal{L}^{-1}) = 0$$

holds.
:::

::: Proof
By Serre duality from [§Serre Duality](/en/math/algebraic_varieties/serre_duality){: data-lid="nniht" },

$$H^p(X, \mathcal{L}^{-1}) \cong H^{n-p}(X, \omega_X \otimes \mathcal{L})^\vee$$

holds. If $p < n$, then $n - p > 0$, so by [Proposition 1](#prop1){: data-lid="7zppm" } the right-hand side is $0$.
:::

Since these two formulations are completely equivalent via Serre duality, as seen in the proof above, we may use whichever is more convenient in a given situation.

It is on projective space $X = \mathbb{P}^n$ that Kodaira vanishing provides the simplest nontrivial example.

::: Example 3
From the Euler exact sequence in [§Canonical Line Bundle, ⁋Proposition 7](/en/math/algebraic_varieties/canonical_bundle#prop7){: data-lid="s1t2w" }, we verified that

$$\omega_{\mathbb{P}^n} \cong \mathcal{O}(-n-1)$$

and in [§Line Bundles and Vector Bundles, ⁋Example 12](/en/math/algebraic_varieties/line_bundles#ex12){: data-lid="j1xc3" } we verified that any line bundle on $\mathbb{P}^n$ is of the form $\mathcal{O}(d)$. Among these, for $d>0$, the $\mathcal{O}(d)$ are ample line bundles. Therefore, Kodaira vanishing asserts that the vanishing

$$H^p(\mathbb{P}^n, \mathcal{O}(d - n - 1)) = 0$$

holds for all $d>0$ and all $p>0$.

Since we know the cohomology of every line bundle through [§Cohomology of Projective Space, ⁋Proposition 1](/en/math/algebraic_varieties/cohomology_of_projective_spaces#prop1){: data-lid="b57uc" }, we can verify this directly. According to this,

$$H^q(\mathbb{P}^n, \mathcal{O}(k)) = \begin{cases}
\mathbb{K}[\x_0, \ldots, \x_n]_k & q = 0, k \geq 0 \\
\mathbb{K}[\x_0^{-1}, \ldots, \x_n^{-1}]_{-k-n-1} & q = n, k \leq -n-1 \\
0 & \text{otherwise}
\end{cases}$$

and since all cohomology automatically vanishes for $q\neq 0, n$, our only concern is when $q=n$. Now, according to the formula above, for this to be nonzero, $k\leq -n-1$ must hold. However, in our situation $k=d-n-1$ and $d>0$, so this is impossible, and thus we can verify the Kodaira vanishing theorem again.
:::

## Applications of the Kodaira Vanishing Theorem

Now, as previewed earlier, we examine applications of the Kodaira vanishing theorem. First, according to the Riemann–Roch theorem from the previous post, for a surface $S$ and a divisor $D$ on it,

$$\rchi(\mathcal{O}_S(D)) = \frac{1}{2} D \cdot (D - K_S) + \rchi(\mathcal{O}_S)$$

is given. ([§The Riemann-Roch Theorem on Surfaces, ⁋Proposition 4](/en/math/algebraic_varieties/riemann_roch_surfaces#prop4){: data-lid="wvvyf" }) The power of this formula lies in the fact that $\rchi$ can be computed purely from algebraic and topological data, but the problem is that $\rchi$ is the alternating sum of $h^0, h^1, h^2$. Thus, when we simply want to know $h^0(S, \mathcal{O}_S(D))$, we must determine the values of the higher cohomologies separately, so the Riemann–Roch formula alone does not give a direct answer.

In this situation, to use the Kodaira vanishing theorem, if we suppose that $\mathcal{L}\cong \mathcal{O}_S(L)$ is an ample line bundle, we know that

$$\omega_S\otimes \mathcal{L}\cong \mathcal{O}_S(K_S+L)$$

and substituting this above and using $h^1(S, \omega_S \otimes \mathcal{L}) = h^2(S, \omega_S \otimes \mathcal{L}) = 0$ from [Proposition 1](#prop1){: data-lid="jyw93" }, we obtain

$$\rchi(S, \omega_S \otimes \mathcal{L}) = h^0(S, \omega_S \otimes \mathcal{L})$$

and therefore we can obtain $h^0(S, \omega_S \otimes \mathcal{L})$ directly just by computing the right-hand side of the Riemann–Roch formula.

Another application is the computation of plurigenera. The plurigenus $P_m(X)$ of a smooth projective variety $X$ is a generalization of the geometric genus $p_g(X)$ and is a birational invariant of surfaces. ([§The Riemann-Roch Theorem on Surfaces, ⁋Definition 12](/en/math/algebraic_varieties/riemann_roch_surfaces#def12){: data-lid="xcg60" }) Kodaira vanishing can be used directly to compute these invariants.

For example, in the case of a curve $C$, we know that its plurigenera are determined by the genus, and in fact $P_m(g)$ is given as a function of $g$ (and $m$). That is, essentially for a curve $C$, the plurigenus is not an interesting invariant. The case where this is interesting is in higher dimensions such as surfaces, where birational invariants are not determined by a single number and all plurigenera become genuinely necessary.

As seen in [§The Riemann-Roch Theorem on Surfaces](/en/math/algebraic_varieties/riemann_roch_surfaces){: data-lid="tbmti" }, for a surface $S$ and a divisor $D$ on it, the Riemann–Roch formula is given by

$$\rchi(\mathcal{O}_S(D)) = \frac{1}{2} D \cdot (D - K_S) + \rchi(\mathcal{O}_S)$$

and to compute plurigenera, using $\omega_S^{\otimes m} \cong \mathcal{O}_S(mK_S)$ and substituting $D = mK_S$, we get

$$\rchi(\mathcal{O}_S(mK_S)) = \frac{m(m-1)}{2} K_S^2 + \rchi(\mathcal{O}_S)$$

Now, if $m \geq 2$ and $K_S$ is ample, then $(m-1)K_S$ is also ample, so applying [Proposition 1](#prop1){: data-lid="tx4ui" } to $mK_S = K_S + (m-1)K_S$ yields $h^1 = h^2 = 0$. Therefore, from this formula we can directly compute $P_m(S) = h^0(S, \mathcal{O}_S(mK_S))$.

Meanwhile, in this case, the expression for the plurigenera can be thought of as being asymptotically quadratic. This leads to the following definition.

::: Definition 4
For a smooth projective variety $X$, the *Kodaira dimension* $\kappa(X)$ is defined as follows. If for all $m \geq 1$ we have $P_m(X) = 0$, then $\kappa(X) = -\infty$. Otherwise, $\kappa(X)$ is defined as the smallest integer satisfying $P_m(X) = O(m^\kappa)$ with $\kappa \geq 0$. That is,

$$\kappa(X) = \min\{k \in \mathbb{Z}_{\geq 0} \mid P_m(X) = O(m^k)\}$$

Equivalently, it can also be written as

$$\kappa(X) = \limsup_{m \rightarrow \infty} \frac{\log P_m(X)}{\log m}$$
:::

That the set over which the minimum is taken in the above definition is nonempty follows from the fact that $P_m(X) = O(m^{\dim X})$ holds for any smooth projective variety; from this we know that $\kappa(X)$ is well-defined and at the same time $\kappa(X) \leq \dim X$ always holds. Hence for surfaces, $\kappa \in \{-\infty, 0, 1, 2\}$. The [Enriques–Kodaira classification](https://en.wikipedia.org/wiki/Enriques-Kodaira_classification) classifies surfaces largely by Kodaira dimension, and for the cases $\kappa=0$ and $\kappa=-\infty$ it provides an additional detailed classification using the geometric genus $p_g$ and the irregularity $q$.

In [§Linear Systems, ⁋Definition 9](/en/math/algebraic_varieties/linear_systems#def9){: data-lid="qw9z5" }, we defined a line bundle $\mathcal{L}$ being very ample to mean that the complete linear system $\lvert \mathcal{L} \rvert$ defines a morphism $\varphi_{\mathcal{L}}: X \rightarrow \mathbb{P}(\Gamma(X, \mathcal{L}))$ that is a closed embedding. At that time we did not yet have the language of sheaf cohomology, but now that we have introduced sheaf cohomology, we can put it to better use.

First, suppose that a very ample line bundle $\mathcal{L}$ is given, and consider the closed embedding $\varphi_\mathcal{L}: X\rightarrow \mathbb{P}^N$ defined by it. Then, from $\varphi$ being an embedding, we know that $\varphi_\mathcal{L}(p)\neq \varphi_\mathcal{L}(q)$ holds; furthermore, since $\varphi_\mathcal{L}$ is a closed embedding, $\dd{\varphi_\mathcal{L}}$ is injective, and hence the dual map on the cotangent space $\mathfrak{m}_{\varphi_{\mathcal{L}}(p)}/\mathfrak{m}_{\varphi_{\mathcal{L}}(p)}^2 \longrightarrow \mathfrak{m}_p/\mathfrak{m}_p^2$ is surjective. From this we know that the following two results hold.

1. *$\varphi_\mathcal{L}$ separates points.* That is, for any two distinct closed points $p, q \in X$, there exists, satisfying $s(p) = 0$ and $s(q) \neq 0$, a global section $s \in H^0(X, \mathcal{L})$.
2. *$\varphi_\mathcal{L}$ separates tangent vectors.* That is, for any closed point $p \in X$, the collection of sections vanishing at $p$, $\{ s \in H^0(X, \mathcal{L}) \mid s(p) = 0 \}$, spans the vector space $\mathfrak{m}_p\mathcal{L}_p / \mathfrak{m}_p^2\mathcal{L}_p$ corresponding to the cotangent space.

The first condition means that the evaluation map

$$H^0(X, \mathcal{L}) \longrightarrow \mathcal{L}_p \oplus \mathcal{L}_q$$

is surjective, and the second condition means that the image of the restriction map on sections vanishing at $p$,

$$\{s \in H^0(X, \mathcal{L}) \mid s(p) = 0\} \longrightarrow \mathfrak{m}_p\mathcal{L}_p / \mathfrak{m}_p^2\mathcal{L}_p$$

spans the entire $\mathfrak{m}_p\mathcal{L}_p / \mathfrak{m}_p^2\mathcal{L}_p$. It is not difficult to check that their converses also hold. That is, the following holds.

::: Proposition 5
For a projective variety $X$ over an algebraically closed field and a line bundle $\mathcal{L}$ on it, $\mathcal{L}$ being very ample is equivalent to simultaneously satisfying the two separation conditions above.
:::

Now suppose $\mathcal{L}$ is an ample line bundle, and let us examine how these separation conditions are verified for $\mathcal{L}^{\otimes m}$ via cohomology. First, in the case of (1), if for two points $p \neq q$ we consider the closed subset $Z = \{p\} \cup \{q\}$ containing them, then for the ideal sheaf defining $Z$, $\mathcal{I}_Z$, we obtain the short exact sequence

$$0 \longrightarrow \mathcal{I}_Z \otimes \mathcal{L}^{\otimes m} \longrightarrow \mathcal{L}^{\otimes m} \longrightarrow \mathcal{L}^{\otimes m} \otimes \mathcal{O}_Z \longrightarrow 0$$

Here $\mathcal{L}^{\otimes m} \otimes \mathcal{O}_Z$ is a line bundle on $Z$, and

$$H^0(Z, \mathcal{L}^{\otimes m}\rvert_Z) \cong \mathcal{L}^{\otimes m}_p \oplus \mathcal{L}^{\otimes m}_q$$

holds. Considering the long exact sequence

$$H^0(X, \mathcal{L}^{\otimes m}) \longrightarrow H^0(Z, \mathcal{L}^{\otimes m}\rvert_Z) \longrightarrow H^1(X, \mathcal{I}_Z \otimes \mathcal{L}^{\otimes m})$$

induced from this, we see that if $H^1(X, \mathcal{I}_Z \otimes \mathcal{L}^{\otimes m}) = 0$, the evaluation map becomes surjective and separation of points holds.

Similarly, in the case of (2), if we consider the first infinitesimal neighborhood of the point $p$, $\Spec(\mathcal{O}_{X,p}/\mathfrak{m}_p^2)$, and let $\mathcal{I}_p$ be the ideal sheaf of $p$, then from the short exact sequence

$$0 \longrightarrow \mathcal{I}_p^2 \otimes \mathcal{L}^{\otimes m} \longrightarrow \mathcal{L}^{\otimes m} \longrightarrow \mathcal{L}^{\otimes m} \otimes (\mathcal{O}_X / \mathcal{I}_p^2) \longrightarrow 0$$

the induced long exact sequence

$$H^0(X, \mathcal{L}^{\otimes m}) \longrightarrow H^0(X, \mathcal{L}^{\otimes m} \otimes (\mathcal{O}_X / \mathcal{I}_p^2)) \longrightarrow H^1(X, \mathcal{I}_p^2 \otimes \mathcal{L}^{\otimes m})$$

shows that if $H^1(X, \mathcal{I}_p^2 \otimes \mathcal{L}^{\otimes m}) = 0$, then separation of tangent vectors holds.

Since $\mathcal{I}_Z$ and $\mathcal{I}_p^2$ are coherent sheaves, applying [§Cohomology of Projective Space, ⁋Proposition 7](/en/math/algebraic_varieties/cohomology_of_projective_spaces#prop7){: data-lid="upowc" } to $\mathcal{F} = \mathcal{I}_Z$ and $\mathcal{F} = \mathcal{I}_p^2$, for sufficiently large $m$, the two $H^1$ above both vanish. Therefore, the sections of $\mathcal{L}^{\otimes m}$ satisfy both separation conditions, and by [Proposition 5](#prop5){: data-lid="7k0ct" }, $\mathcal{L}^{\otimes m}$ is very ample. That is, for an ample line bundle, for *all* sufficiently large $m$, $\mathcal{L}^{\otimes m}$ is very ample.

Meanwhile, Kodaira vanishing enters the classical proof of [Proposition 6](#prop6){: data-lid="hld30" } in a different way. In that proof, on the blow-up of $p$ and $q$, $\pi: \widetilde{X} \rightarrow X$, one applies vanishing to a line bundle with the twist lowered by the exceptional divisor, so that the object of vanishing becomes a line bundle again, reducing to the form of [Proposition 1](#prop1){: data-lid="467qy" }. Furthermore, the condition that $\mathcal{L}^{\otimes m}$ be not only very ample but also that the embedding it defines be projectively normal can be obtained by verifying the surjectivity of the related multiplication map

$$S^\mu H^0(X, \mathcal{L}^{\otimes m}) \longrightarrow H^0(X, \mathcal{L}^{\otimes \mu m})$$

and what supplies the necessary vanishing together with a concrete range of $m$ is the Castelnuovo-Mumford regularity from [§Cohomology of Projective Space, §§Regularity](/en/math/algebraic_varieties/cohomology_of_projective_spaces#regularity){: data-lid="orywe" }. Such vanishing guarantees that higher cohomology does not obstruct the generation of sections, allowing one to handle the abundance of linear systems quantitatively.


## Kodaira Embedding Theorem

The most famous application of Kodaira vanishing is the Kodaira embedding theorem. However, this ventures somewhat into the realm of complex manifolds, so we only briefly introduce it here. First, that a compact complex manifold $X$ is a *Kähler manifold* means that a mutually compatible Riemannian metric, symplectic form, and complex structure are defined on $X$. In this case, if a line bundle $\mathcal{L}$ is given a Hermitian metric $h$, its curvature form $\Theta_h$ is defined, and $\mathcal{L}$ being *positive* means that $\frac{i}{2\pi}\Theta_h$ is a positive definite $(1,1)$-form. Then the following holds.

::: Proposition 6 (Kodaira embedding)
Let $X$ be a compact Kähler manifold and $\mathcal{L}$ a positive line bundle. Then for sufficiently large $k$, $\mathcal{L}^{\otimes k}$ is very ample, and in particular $\mathcal{L}$ is an ample line bundle. Hence $X$ is a projective variety.
:::

That is, using this proposition one can show that a Kähler manifold is a projective variety.

---

**References**

**[Hart]** R. Hartshorne, *Algebraic Geometry*, Graduate Texts in Mathematics, Springer, 1977.  
**[Laz]** R. Lazarsfeld, *Positivity in Algebraic Geometry I & II*, Ergebnisse der Mathematik, Springer, 2004.  
**[Kod]** K. Kodaira, *On a differential-geometric method in the theory of analytic stacks*, Proceedings of the National Academy of Sciences, 1953.
