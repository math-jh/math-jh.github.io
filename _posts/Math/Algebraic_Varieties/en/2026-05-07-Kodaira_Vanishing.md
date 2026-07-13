---
title: "Kodaira Vanishing Theorem"
description: "While Serre vanishing guarantees cohomology vanishing only in sufficiently high degrees, the Kodaira vanishing theorem shows that higher cohomology always vanishes for the tensor product of the canonical bundle and any ample bundle, in all degrees. We examine its uses and applications in algebraic geometry."
permalink: /en/math/algebraic_varieties/kodaira_vanishing
excerpt: "The Kodaira vanishing theorem and its applications"
categories: [Math / Algebraic Varieties]

sidebar:
    nav: "algebraic_varieties-en"
    
date: 2026-05-07
weight: 17
translated_at: 2026-07-11T08:30:02+00:00
translation_source: kimi-cli
last_polished_at: 2026-07-11T08:30:02+00:00
---
[§Cohomology of Projective Spaces, ⁋Proposition 4](/en/math/algebraic_varieties/cohomology_of_projective_spaces#prop4)'s Serre vanishing theorem guarantees that for an ample line bundle $\mathcal{L}$ and a coherent sheaf $\mathcal{F}$ on a projective variety, we have $H^i(X, \mathcal{F} \otimes \mathcal{L}^{\otimes m}) = 0$ ($i > 0$) for sufficiently large $m$. However, this result is merely an asymptotic property and gives no information whatsoever about the specific value of $m$ at which vanishing begins.

The Kodaira vanishing theorem is a far more refined result, guaranteeing that the higher cohomology of the tensor product $\omega_X \otimes \mathcal{L}$ of the canonical bundle $\omega_X$ and an ample line bundle $\mathcal{L}$ *always* vanishes. In this article, we examine the Kodaira vanishing theorem, its applications, and how this theorem is used in algebraic geometry.

## Kodaira Vanishing Theorem

The basic setup we consider is as follows. Let $X$ be an $n$-dimensional smooth projective variety, $\mathcal{L}$ an ample line bundle on $X$, and $\omega_X = \det \Omega_X^1 = \Omega_X^n$ the canonical line bundle. ([§Canonical Bundle, ⁋Definition 5](/en/math/algebraic_varieties/canonical_bundle#def5)) The Kodaira vanishing theorem can then be stated as follows.

::: Proposition 1 (Kodaira vanishing)
Let $X$ be an $n$-dimensional smooth projective variety and let $\mathcal{L}$ be an ample line bundle. Then for every $p > 0$,
 
$$H^p(X, \omega_X \otimes \mathcal{L}) = 0$$

holds. More generally, for all $p,q$ satisfying $p+q>n$,

$$H^p(X, \Omega^q\otimes \mathcal{L})=0$$

holds.
:::

The first statement is obtained from the second by setting $q=n$. The proof of this proposition involves quite technical aspects, so in this post we focus on how it is used in algebraic geometry rather than giving a rigorous proof.

As the statement of the proposition shows, Kodaira vanishing kills the higher cohomology after twisting by the canonical bundle. Using Serre duality, this can be rewritten as the following equivalent statement.

::: Proposition 2
Under the assumptions of [Proposition 1](#prop1), for all $p < n$,

$$H^p(X, \mathcal{L}^{-1}) = 0$$

holds.
:::

::: Proof
By Serre duality from [§Serre Duality](/en/math/algebraic_varieties/serre_duality),

$$H^p(X, \mathcal{L}^{-1}) \cong H^{n-p}(X, \omega_X \otimes \mathcal{L})^\vee$$

holds. If $p < n$ then $n - p > 0$, so by [Proposition 1](#prop1) the right-hand side is $0$.
:::

These two formulations are completely equivalent via Serre duality, as we saw in the proof above, so we may use whichever is more convenient depending on the situation.

The simplest nontrivial example where Kodaira vanishing applies is projective space $X = \mathbb{P}^n$.

::: Example 3
We verified in [§Standard Line Bundles, ⁋Proposition 7](/en/math/algebraic_varieties/canonical_bundle#prop7) that

$$\omega_{\mathbb{P}^n} \cong \mathcal{O}(-n-1)$$

and in [§Line Bundles and Vector Bundles, ⁋Example 12](/en/math/algebraic_varieties/line_bundles#ex12) that every line bundle on $\mathbb{P}^n$ is of the form $\mathcal{O}(d)$. Among these, the $\mathcal{O}(d)$ with $d>0$ are ample line bundles. Thus, Kodaira vanishing asserts that the vanishing

$$H^p(\mathbb{P}^n, \mathcal{O}(d - n - 1)) = 0$$

holds for all $d>0$ and all $i>0$.

Since we know the cohomology of every line bundle from [§Cohomology of Projective Spaces, ⁋Proposition 1](/en/math/algebraic_varieties/cohomology_of_projective_spaces#prop1), we can verify this directly. According to it,

$$H^q(\mathbb{P}^n, \mathcal{O}(k)) = \begin{cases}
\mathbb{K}[\x_0, \ldots, \x_n]_k & q = 0, k \geq 0 \\
\mathbb{K}[\x_0^{-1}, \ldots, \x_n^{-1}]_{-k-n-1} & q = n, k \leq -n-1 \\
0 & \text{otherwise}
\end{cases}$$

and from this, all cohomology automatically vanishes for $q\neq 0$, so our concern is only when $q=n$. Now, according to the formula above, for this to be nonzero we must have $k\leq -n-1$. But in our situation $k=d-n-1$ and $d>0$, so this is impossible, and hence we can verify the Kodaira vanishing theorem again.
:::

## Applications of the Kodaira Vanishing Theorem

Now we examine the applications of the Kodaira vanishing theorem as previewed earlier. First, by the Riemann–Roch theorem from the previous post, for a divisor $D$ on a surface $S$,

$$\rchi(\mathcal{O}_S(D)) = \frac{1}{2} D \cdot (D - K_S) + \rchi(\mathcal{O}_S)$$

([§Riemann–Roch Theorem for Surfaces, ⁋Proposition 4](/en/math/algebraic_varieties/riemann_roch_surfaces#prop4)). The power of this formula lies in the fact that $\rchi$ can be computed purely from algebraic and topological data, but the problem is that $\rchi$ is the alternating sum of $h^0, h^1, h^2$. Thus, when we simply want to know $h^0(S, \mathcal{O}_S(D))$, we must determine the values of the higher cohomologies separately, so the Riemann–Roch formula alone is insufficient to obtain a direct answer.

In such a situation, to use the Kodaira vanishing theorem, suppose $\mathcal{L}\cong \mathcal{O}_S(L)$ is an ample line bundle. Then we know

$$\omega_S\otimes \mathcal{L}\cong \mathcal{O}_S(K_S+L)$$

and substituting this above yields

$$\rchi(S, \omega_S \otimes \mathcal{L}) = h^0(S, \omega_S \otimes \mathcal{L})$$

so by computing only the right-hand side of the Riemann–Roch formula we immediately obtain $h^0(S, \omega_S \otimes \mathcal{L})$.

Another application is the computation of plurigenera. The plurigenus $P_m(X)$ of a smooth projective variety $X$ is a generalization of the geometric genus $p_g(X)$, and is a birational invariant of surfaces. ([§Riemann–Roch Theorem for Surfaces, ⁋Definition 12](/en/math/algebraic_varieties/riemann_roch_surfaces#def12)) Kodaira vanishing can be used directly in computing these invariants.

For instance, in the case of a curve $C$, we know that its birational class is determined by the genus, and the plurigenus $P_m(g)$ is given as a function of $g$ (and $m$). That is, for a curve $C$ the plurigenus is not a particularly interesting invariant. The interesting case is for higher-dimensional objects such as surfaces, where the birational invariant is not determined by a single number and all the plurigenera become genuinely necessary.

As seen in [§Riemann–Roch Theorem for Surfaces](/en/math/algebraic_varieties/riemann_roch_surfaces), for a divisor $D$ on a surface $S$ the Riemann–Roch formula is

$$\rchi(\mathcal{O}_S(D)) = \frac{1}{2} D \cdot (D - K_S) + \rchi(\mathcal{O}_S)$$

and to compute the plurigenera we use $\omega_S^{\otimes m} \cong \mathcal{O}_S(mK_S)$ and substitute $D = mK_S$ to obtain

$$\rchi(\mathcal{O}_S(mK_S)) = \frac{m(m-1)}{2} K_S^2 + \rchi(\mathcal{O}_S)$$

Now if $m \geq 2$ and $K_S$ is ample, then $(m-1)K_S$ is also ample, so applying [Proposition 1](#prop1) to $mK_S = K_S + (m-1)K_S$ yields $h^1 = h^2 = 0$. Therefore, from this formula we can directly compute $P_m(S) = h^0(S, \mathcal{O}_S(mK_S))$.

On the other hand, in such cases the expression for plurigenera can be thought of as asymptotically quadratic. This leads to

::: Definition 4
The *Kodaira dimension* $\kappa(X)$ of a smooth projective variety $X$ is defined as follows. If $P_m(X) = 0$ for all $m \geq 1$, then $\kappa(X) = -\infty$. Otherwise, $\kappa(X)$ is defined as the smallest integer $\kappa \geq 0$ satisfying $P_m(X) = O(m^\kappa)$. That is,

$$\kappa(X) = \min\{k \in \mathbb{Z}_{\geq 0} : P_m(X) = O(m^k)\}$$

Equivalently, it can also be written as

$$\kappa(X) = \limsup_{m \to \infty} \frac{\log P_m(X)}{\log m}$$

:::

From the computation above, we know that for a surface, $\kappa \in \{-\infty, 0, 1, 2\}$. The [Enriques–Kodaira classification](https://en.wikipedia.org/wiki/Enriques-Kodaira_classification) classifies surfaces broadly by Kodaira dimension, and in the cases $\kappa=0$ and $\kappa=-\infty$, it provides further detailed classification using the geometric genus $p_g$ and the irregularity $q$.

In [§Linear Systems, ⁋Definition 9](/en/math/algebraic_varieties/linear_systems#def9), we defined that a line bundle $\mathcal{L}$ is very ample if the map $\varphi_{\mathcal{L}}: X \to \mathbb{P}(\Gamma(X, \mathcal{L}))$ defined by the complete linear system $\lvert \mathcal{L} \rvert$ is a closed embedding. At the time, we did not have the language of sheaf cohomology, but now that we have introduced it, we can use this a bit more effectively.

First, suppose a very ample line bundle $\mathcal{L}$ is given, and consider the closed embedding $\varphi_\mathcal{L}: X\rightarrow \mathbb{P}^N$ defined by it. Then from the fact that $\varphi$ is an embedding, we know that $\varphi_\mathcal{L}(p)\neq \varphi_\mathcal{L}(q)$ holds, and moreover, since $\varphi_\mathcal{L}$ is a closed embedding, $d\varphi_\mathcal{L}$ is injective, and thus the dual map on cotangent spaces $\mathfrak{m}_{\varphi_{\mathcal{L}}(p)}/\mathfrak{m}_{\varphi_{\mathcal{L}}(p)}^2 \longrightarrow \mathfrak{m}_p/\mathfrak{m}_p^2$ is surjective. From this, we know that the following two results hold.

1. *$\varphi_\mathcal{L}$ separates points.* That is, for any two distinct closed points $p, q \in X$, there exists a global section $s \in H^0(X, \mathcal{L})$ such that $s(p) = 0$ and $s(q) \neq 0$.
2. *$\varphi_\mathcal{L}$ separates tangent vectors.* That is, for any closed point $p \in X$, the collection of sections vanishing at $p$, $\{ s \in H^0(X, \mathcal{L}) : s(p) = 0 \}$, spans the vector space $\mathfrak{m}_p\mathcal{L}_p / \mathfrak{m}_p^2\mathcal{L}_p$ corresponding to the cotangent space.

The first condition means that the evaluation map

$$H^0(X, \mathcal{L}) \longrightarrow \mathcal{L}_p \oplus \mathcal{L}_q$$

is surjective, and the second condition means that the image of the restriction map by sections vanishing at $p$,

$$\{s \in H^0(X, \mathcal{L}) : s(p) = 0\} \longrightarrow \mathfrak{m}_p\mathcal{L}_p / \mathfrak{m}_p^2\mathcal{L}_p$$

spans the entire $\mathfrak{m}_p\mathcal{L}_p / \mathfrak{m}_p^2\mathcal{L}_p$. It is not difficult to verify that the converses of these also hold. That is, the following holds.

::: Proposition 5
For a line bundle $\mathcal{L}$ on a projective variety $X$, $\mathcal{L}$ being very ample is equivalent to satisfying the two separation conditions above simultaneously.
:::

Now let us examine how these separation conditions are verified via cohomology. First, for (1), consider the closed subvariety $Z = \{p\} \cup \{q\}$ containing two distinct points $p \neq q$. For the ideal sheaf $\mathcal{I}_Z$ defining $Z$, we obtain the short exact sequence

$$0 \longrightarrow \mathcal{I}_Z \otimes \mathcal{L}^{\otimes m} \longrightarrow \mathcal{L}^{\otimes m} \longrightarrow \mathcal{L}^{\otimes m} \otimes \mathcal{O}_Z \longrightarrow 0$$

Here $\mathcal{L}^{\otimes m} \otimes \mathcal{O}_Z$ is a line bundle on $Z$, and

$$H^0(Z, \mathcal{L}^{\otimes m}\rvert_Z) \cong \mathcal{L}^{\otimes m}_p \oplus \mathcal{L}^{\otimes m}_q$$

From this, consider the induced long exact sequence

$$H^0(X, \mathcal{L}^{\otimes m}) \longrightarrow H^0(Z, \mathcal{L}^{\otimes m}\rvert_Z) \longrightarrow H^1(X, \mathcal{I}_Z \otimes \mathcal{L}^{\otimes m})$$

If $H^1(X, \mathcal{I}_Z \otimes \mathcal{L}^{\otimes m}) = 0$, then the evaluation map becomes surjective, and we see that separation of points holds.

Likewise, for (2), consider the first infinitesimal neighborhood of the point $p$, $\operatorname{Spec}(\mathcal{O}_{X,p}/\mathfrak{m}_p^2)$, and let $\mathcal{I}_p$ be the ideal sheaf of $p$. From the short exact sequence

$$0 \longrightarrow \mathcal{I}_p^2 \otimes \mathcal{L}^{\otimes m} \longrightarrow \mathcal{L}^{\otimes m} \longrightarrow \mathcal{L}^{\otimes m} \otimes (\mathcal{O}_X / \mathcal{I}_p^2) \longrightarrow 0$$

the induced long exact sequence

$$H^0(X, \mathcal{L}^{\otimes m}) \longrightarrow H^0(Z, \mathcal{L}^{\otimes m}\rvert_Z) \longrightarrow H^1(X, \mathcal{I}_p^2 \otimes \mathcal{L}^{\otimes m})$$

shows that if $H^1(X, \mathcal{I}_p^2 \otimes \mathcal{L}^{\otimes m}) = 0$, then separation of tangent vectors holds.

Concretely, if $\mathcal{L}$ is ample, Kodaira vanishing guarantees $H^i(X, \omega_X \otimes \mathcal{L}^{\otimes m}) = 0$ for $i > 0$. Using a suitable twist and Serre duality, the above $H^1$ groups also vanish, so one can show that for sufficiently large $m$ the sections of $\mathcal{L}^{\otimes m}$ satisfy the separation conditions. This is the key ingredient used in the proof of [Proposition 6](#prop6). Moreover, the condition that the embedding given by $\mathcal{L}^{\otimes m}$ is not only very ample but also projectively normal can be obtained by verifying the surjectivity of the related multiplication map

$$S^\mu H^0(X, \mathcal{L}^{\otimes m}) \longrightarrow H^0(X, \mathcal{L}^{\otimes \mu m})$$

through Kodaira vanishing. Such vanishing ensures that higher cohomology does not obstruct the generation of sections, allowing us to treat the abundance of the linear system quantitatively.


## Kodaira Embedding Theorem

The most famous application of Kodaira vanishing is the Kodaira embedding theorem. However, since this takes us into the realm of complex manifolds, we only briefly introduce it here. First, a compact complex manifold $X$ is called a **Kähler manifold** if there are a compatible Riemannian metric, symplectic form, and complex structure defined on $X$. In this case, given a Hermitian metric $h$ on a line bundle $\mathcal{L}$, its curvature form $\Theta_h$ is defined, and $\mathcal{L}$ is called **positive** if $\frac{i}{2\pi}\Theta_h$ is a positive definite $(1,1)$-form. Then the following holds.

::: Proposition 6 (Kodaira embedding)
Let $X$ be a compact Kähler manifold and $\mathcal{L}$ a positive line bundle. Then for sufficiently large $k$, $\mathcal{L}^{\otimes k}$ is very ample; in particular, $\mathcal{L}$ is an ample line bundle. Therefore $X$ is a projective variety.
:::

That is, using this proposition we can show that a Kähler manifold becomes a projective variety.

---

**References**

**[Har]** R. Hartshorne, *Algebraic Geometry*, Graduate Texts in Mathematics, Springer, 1977.  
**[Laz]** R. Lazarsfeld, *Positivity in Algebraic Geometry I & II*, Ergebnisse der Mathematik, Springer, 2004.  
**[Kod]** K. Kodaira, *On a differential-geometric method in the theory of analytic stacks*, Proceedings of the National Academy of Sciences, 1953.
