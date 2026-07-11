---
title: "Bézout's Theorem"
description: "Bezout's theorem in algebraic geometry states that in projective space over an algebraically closed field, two curves with no common component intersect in a number of points equal to the product of their degrees. Taking multiplicity into account, two conics meet in exactly four points."
excerpt: "Bézout's theorem and its applications"

categories: [Math / Algebraic Varieties]
permalink: /en/math/algebraic_varieties/bezout_theorem
sidebar: 
    nav: "algebraic_varieties-en"

date: 2026-03-15
weight: 20

drift_needed: true
translated_at: 2026-07-11T00:30:01+00:00
translation_source: kimi-cli
---
We introduce Bézout's theorem, a classical result in algebraic geometry, in this post. Intuitively, suppose two curves $$C,D$$ on the plane are given. Then the number of intersection points of $$C$$ and $$D$$ depends on their degrees: for example, a conic $$\y=x^2$$ defined on the plane and a line generally meet at two points. Bézout's theorem is a generalization of this observation.

::: Proposition 1 (Bézout)
Over an algebraically closed field, inside $$\mathbb{P}^n$$, if hypersurfaces $$H_1, \ldots, H_n$$ of degrees $$d_1, \ldots, d_n$$ have no common component, then

$$\deg(H_1 \cap \cdots \cap H_n) = d_1 \cdots d_n$$

holds. Here the intersection is taken with multiplicity into account.
:::

In particular, inside $$\mathbb{P}^2$$ two curves of degrees $$m$$ and $$n$$ meet at $$mn$$ points. One should be somewhat careful that they must not have a common component; for instance, one cannot use this to compute the intersection of two identical curves.

::: Example 2 (Two conics)
Consider two conics in $$\mathbb{P}^2$$

$$C_1 = Z(\x_0^2 + \x_1^2 - \x_2^2),\qquad C_2 = Z(\x_0\x_1)$$

$$C_1$$ is the projectivization of a cone, and $$C_2$$ is the union of the two lines $$Z(\x_0)$$ and $$Z(\x_1)$$. Since these two curves share no common component, Bézout's theorem predicts $$2 \times 2 = 4$$ intersection points. Computing the intersection explicitly, when $$\x_0 = 0$$ we get $$\x_1^2 = \x_2^2$$, yielding $$[0:1:1]$$ and $$[0:1:-1]$$; when $$\x_1 = 0$$ we get $$\x_0^2 = \x_2^2$$, yielding $$[1:0:1]$$ and $$[1:0:-1]$$. Thus we verify that they meet in exactly four points.
:::

## Proof

Rather than proving the general case, we prove Bézout's theorem only in $$\mathbb{P}^2$$. For this purpose we use the following lemma.

::: Proposition 3 (Hilbert polynomial)
For the homogeneous coordinate ring $$S(X)$$ of a projective variety $$X \subseteq \mathbb{P}^n$$, we call the function $$H(t) = \dim_\mathbb{K} S(X)_t$$ the **Hilbert function** of $$X$$. By the Hilbert–Serre theorem, this function coincides with a polynomial $$P_X(t)$$ for $$t \gg 0$$, and we call this polynomial the **Hilbert polynomial** of $$X$$.

In particular, for a curve $$C = Z(F) \subseteq \mathbb{P}^2$$ of degree $$d$$, the Hilbert polynomial of $$S(C) = \mathbb{K}[\x_0, \x_1, \x_2]/(F)$$ is

$$P_C(t) = dt + \frac{d(3-d)}{2}$$

Here the degree of $$P_C$$ is $$1$$, the dimension of $$C$$; the leading coefficient is $$\deg C = d$$; and the constant term $$P_C(0) = \frac{d(3-d)}{2} = 1 - \frac{(d-1)(d-2)}{2}$$ is the arithmetic genus of $$C$$.
:::

The Hilbert function $$H(t)$$ counts the number of independent elements remaining after removing those homogeneous polynomials of degree $$t$$ that vanish on $$C$$—in other words, the number of homogeneous polynomials that act as distinct functions on $$C$$. As $$t$$ grows, this number behaves like a polynomial; its degree equals the dimension of $$C$$, namely $$1$$; its leading coefficient is proportional to the degree $$d$$; and its constant term equals the arithmetic genus $$1 - \frac{(d-1)(d-2)}{2}$$.

::: Proof
Let $$S = \mathbb{K}[\x_0, \x_1, \x_2]$$. The dimension of $$(S/(F))_t$$ equals the dimension of the space obtained from $$S_t$$ by removing the multiples of $$F$$. Since multiplication by $$\cdot F: S(-d) \to S$$ is injective, we obtain the following short exact sequence:

$$0 \to S(-d) \xrightarrow{\cdot F} S \to S/(F) \to 0$$

Because $$\dim_\mathbb{K} S_t = \binom{t+2}{2}$$, comparing dimensions in degree $$t$$ gives

$$\dim_\mathbb{K} (S/(F))_t = \binom{t+2}{2} - \binom{t-d+2}{2}$$

Expanding this yields

$$\frac{(t+2)(t+1)}{2} - \frac{(t-d+2)(t-d+1)}{2} = dt + \frac{d(3-d)}{2}$$

as desired.
:::

This result will be used crucially in the proof of the following [Proposition 5](#prop5).

::: Proposition 4
For a degree $$d$$ curve $$C = Z(F)$$ in $$\mathbb{P}^2$$, the intersection $$C \cap L$$ with any general line $$L$$ consists of exactly $$d$$ points (counted with multiplicity).
:::

This proposition is the simplest special case of Bézout's theorem. It provides the geometric intuition that a degree $$d$$ curve meets a general line in $$d$$ points.

::: Proof
Without loss of generality, let $$L = Z(\x_2)$$. Since $$C$$ is defined by a degree $$d$$ homogeneous polynomial $$F(\x_0, \x_1, \x_2)$$, substituting $$\x_2 = 0$$ in $$L \cap C$$ gives $$F(\x_0, \x_1, 0)$$. This is a degree $$d$$ homogeneous polynomial in $$\x_0, \x_1$$, and over an algebraically closed field it has exactly $$d$$ roots (counted with multiplicity). Since $$L$$ is general, $$F(\x_0, \x_1, 0)$$ is not the zero polynomial; otherwise $$\x_2$$ would be a factor of $$F$$, so $$C$$ would have $$L$$ as a component, contradicting the hypothesis.
:::

We now prove Proposition 1. The key consists of two points. First, we show that the sum of intersection multiplicities agrees with the dimension of a certain global algebraic object, and second, we compute that dimension precisely as $$mn$$ via the Hilbert polynomial.

::: Proposition 5
(Proof of Proposition 1) Two curves $$C = Z(F)$$ and $$D = Z(G)$$ of degrees $$m$$ and $$n$$ in $$\mathbb{P}^2$$ with no common component satisfy $$\sum_p i_p(C, D) = mn$$.
:::

::: Proof
We divide the proof into two steps.

**Step 1.** We first show the following equality.

> $$\sum_{p \in C \cap D} i_p(C, D) = \dim_\mathbb{K} (\mathbb{K}[\x_0, \x_1, \x_2]/(F, G))_t \qquad (t \gg 0)$$

That $$C \cap D$$ is a finite set is known from the assumption that $$C$$ and $$D$$ have no common component. ([§Dimension, ⁋Example 14](/en/math/algebraic_varieties/dimension#ex14)) For a point $$p = [a:b:c] \in C \cap D$$, assuming $$c \neq 0$$, we have $$p = (a/c, b/c)$$ in the coordinates on $$U_2$$, and for the dehomogenizations $$f, g \in \mathbb{K}[\x, \y]$$ of $$F, G$$,

$$i_p(C, D) = \dim_\mathbb{K} \mathcal{O}_{\mathbb{A}^2, p}/(f, g)$$

Since $$V(F, G)$$ is finite, $$f, g$$ generate a zero-dimensional ideal $$(f, g)$$ in the affine ring $$\mathbb{K}[\x, \y]$$, and by the Chinese remainder theorem,

$$\mathbb{K}[\x, \y]/(f, g) \cong \prod_{p \in V(f,g)} \mathcal{O}_{\mathbb{A}^2, p}/(f, g)$$

Thus $$\dim_\mathbb{K} \mathbb{K}[\x, \y]/(f, g) = \sum_p i_p(C, D)$$.

On the other hand, the Hilbert function $$H(t) = \dim_\mathbb{K} R_t$$ of the quotient $$R = S/(F, G)$$ of $$S = \mathbb{K}[\x_0, \x_1, \x_2]$$ becomes constant for $$t \gg 0$$ (proved in Step 2), and this constant value equals $$\dim_\mathbb{K} \mathbb{K}[\x, \y]/(f, g)$$. This is because when $$t \gg 0$$, there exist polynomials of degree $$t$$ that can independently adjust the values at each intersection point, so the evaluation map $$R_t \to \mathbb{K}^{\lvert V(F,G) \rvert}$$ is surjective.

**Step 2.** We now show that $$\dim_\mathbb{K} (\mathbb{K}[\x_0, \x_1, \x_2]/(F, G))_t = mn$$ for $$t \gg 0$$. Write $$S = \mathbb{K}[\x_0, \x_1, \x_2]$$. Since $$F, G$$ have no common irreducible factor, the multiplication maps $$\cdot F: S(-m) \to S$$ and $$\cdot G: S/(F)(-n) \to S/(F)$$ are both injective, and we obtain the following two short exact sequences.

$$0 \to S(-m) \xrightarrow{\cdot F} S \to S/(F) \to 0$$
$$0 \to S/(F)(-n) \xrightarrow{\cdot G} S/(F) \to S/(F, G) \to 0$$

Reading the degree as $$m$$ from [Proposition 3](#prop3), the Hilbert polynomial of $$S/(F)$$ has the form $$P_F(t) = mt + c_1$$. Applying the Hilbert polynomial to the second exact sequence, the Hilbert polynomial of $$S/(F, G)$$ is

$$P_{F,G}(t) = P_F(t) - P_F(t - n) = \bigl(mt + c_1\bigr) - \bigl(m(t-n) + c_1\bigr) = mn$$

Thus for $$t \gg 0$$, the dimension of $$(S/(F, G))_t$$ is the constant $$mn$$, and by Step 1 we have $$\sum_p i_p(C, D) = mn$$.
:::

## Generalization

So far we have proved Bézout's theorem only for curves in $$\mathbb{P}^2$$. To extend this to arbitrary projective spaces and general projective varieties, we need the Chow ring. The key fact is

$$\operatorname{CH}^\ast(\mathbb{P}^n) \cong \mathbb{Z}[H]/(H^{n+1})$$

Here $$H$$ is the hyperplane class, and a variety of codimension $$k$$ and degree $$d$$ has class $$dH^k$$. In particular, a hypersurface of degree $$d$$ corresponds to $$dH$$, so the intersection product of $$n$$ hypersurfaces $$H_1, \ldots, H_n$$ is

$$[H_1] \cdot [H_2] \cdots [H_n] = (d_1 H)(d_2 H) \cdots (d_n H) = d_1 d_2 \cdots d_n \cdot H^n$$

Since $$H^n$$ is the class of a point in $$\mathbb{P}^n$$ and its degree is 1, we obtain $$\deg(H_1 \cap \cdots \cap H_n) = d_1 \cdots d_n$$. Under this intuition, the generalized Bézout theorem is stated as follows.

::: Proposition 6 (Generalized Bézout theorem)
For two projective varieties $$V, W$$ in $$\mathbb{P}^n$$,

$$\deg(V \cap W) \leq \deg(V) \cdot \deg(W)$$

holds. Here $$\deg(V \cap W)$$ is the sum of the degrees of the irreducible components of $$V \cap W$$. Equality holds when $$V$$ and $$W$$ have a proper intersection (that is, when $$\operatorname{codim}(Z) = \operatorname{codim}(V) + \operatorname{codim}(W)$$ for every irreducible component $$Z$$ of $$V \cap W$$); in this case, assigning an intersection multiplicity $$m_Z$$ to each component $$Z$$ gives $$\sum_Z m_Z \deg(Z) = \deg(V) \cdot \deg(W)$$.
:::

::: Example 7 ($$\mathbb{P}^3$$)
Consider two quadric surfaces $$Q_1, Q_2$$ in $$\mathbb{P}^3$$. Since each has degree 2, when they intersect properly the intersection $$Q_1 \cap Q_2$$ is a curve of dimension 1 and degree 4. Concretely, taking $$Q_1 = Z(\x_0\x_3 - \x_1\x_2)$$ and $$Q_2 = Z(\x_0\x_2 - \x_1\x_3)$$, the intersection decomposes into four lines, and the sum of their degrees is still 4.
:::

The proof of Proposition 6 relies on the general theory of intersection theory via the Chow ring. For details, see [§Intersection Product](/en/math/algebraic_varieties/intersection_product). The inequality from [§Dimension, ⁋Example 14](/en/math/algebraic_varieties/dimension#ex14) reappears as one concerning the codimension of the components.

## Applications

### Cayley-Bacharach Theorem

::: Proposition 8 (Special case of Cayley-Bacharach theorem)
Let $$C_1 = Z(F_1)$$ and $$C_2 = Z(F_2)$$ be two cubic curves in $$\mathbb{P}^2$$ with no common component, meeting in proper intersection at nine distinct points $$p_1, \ldots, p_9$$. Then any cubic curve $$C_3 = Z(F_3)$$ passing through $$p_1, \ldots, p_8$$ also passes through $$p_9$$.
:::

::: Proof
Assume two cubic curves $$C_1, C_2$$ meet in proper intersection at nine distinct points $$p_1, \ldots, p_9$$. The space of degree-3 homogeneous polynomials $$\mathbb{K}[\x_0, \x_1, \x_2]_3$$ on $$\mathbb{P}^2$$ has dimension $$\binom{3+2}{2} = 10$$, and the condition that a curve pass through each point $$p_i$$ is a single linear condition, so $$V = \{F \in \mathbb{K}[\x_0, \x_1, \x_2]_3 : F(p_i) = 0 \text{ for } i = 1, \ldots, 8\}$$ is a subspace of dimension $$\dim V \ge 10 - 8 = 2$$. On the other hand, $$F_1, F_2 \in V$$ and $$C_1 \neq C_2$$, so $$F_1, F_2$$ are linearly independent. If the eight points are in general position then $$\dim V = 2$$, and $$F_1, F_2$$ form a basis of $$V$$. Hence for any $$F_3 \in V$$ there exist constants $$\alpha, \beta$$ such that $$F_3 = \alpha F_1 + \beta F_2$$. Substituting $$p_9$$ into both sides gives $$F_3(p_9) = \alpha F_1(p_9) + \beta F_2(p_9) = 0$$, so $$C_3$$ also passes through $$p_9$$.
:::

The intuition behind this result is as follows. The condition that a cubic pass through eight of the nine intersection points of two cubics imposes eight linear constraints on the space of cubics (which is 10-dimensional), leaving a 1-dimensional family whose members all pass through the ninth point as well. This shows that the $$3 \times 3 = 9$$ of Bézout's theorem is no accident.

### Pascal's theorem

::: Proposition 9 (Pascal's theorem)
For six points $$A, B, C, D, E, F$$ on a conic, if the three intersection points

$$P = \overline{AB} \cap \overline{DE},\quad Q = \overline{BC} \cap \overline{EF},\quad R = \overline{CD} \cap \overline{FA}$$

all exist, then these three points are collinear.
:::

::: Proof
Let us denote the conic by $$\Gamma$$. Define two cubic curves

$$X = \overline{AB} \cup \overline{CD} \cup \overline{EF},\quad Y = \overline{BC} \cup \overline{DE} \cup \overline{FA}.$$

Each is a union of three lines, hence a degree-3 curve. Under a general position assumption, $$X$$ and $$Y$$ have no common component.

Since $$X \cap Y$$ contains $$A, B, C, D, E, F$$ and $$P, Q, R$$, it contains at least nine distinct points. By Bézout's theorem, $$\sum_{p \in X \cap Y} i_p(X, Y) = 3 \times 3 = 9$$, so $$X \cap Y$$ consists exactly of these nine points, and the intersection multiplicity at each point is 1.

Now define a new cubic curve $$Z = \Gamma \cup \overline{PQ}$$. This is a degree-3 curve passing through eight of the nine points of $$X \cap Y$$, namely $$A, B, C, D, E, F$$ and $$P, Q$$. By [Proposition 8](#prop8), $$Z$$ must also pass through the ninth point $$R$$. Since $$R \in Z = \Gamma \cup \overline{PQ}$$, we have either $$R \in \Gamma$$ or $$R \in \overline{PQ}$$.

If $$R \in \Gamma$$, then we would have $$R = \overline{CD} \cap \overline{FA} \in \Gamma$$. However, by Bézout's theorem, $$\overline{CD}$$ and $$\Gamma$$ meet in at most two points, and since we already have $$C, D \in \Gamma$$, we get $$\overline{CD} \cap \Gamma = \{C, D\}$$. Similarly, $$\overline{FA} \cap \Gamma = \{F, A\}$$, so $$R \in \Gamma$$ is impossible. Therefore $$R \in \overline{PQ}$$, i.e., $$P, Q, R$$ are collinear.
:::

### Maximum Number of Double Points

Bézout's theorem gives an upper bound on the number of singular points of a plane curve.

::: Proposition 10
The maximum number of ordinary double points (double points with two distinct tangent lines) that an irreducible plane curve of degree $$d$$ can have is $$\binom{d-1}{2} = \frac{(d-1)(d-2)}{2}$$.
:::

::: Proof
Suppose an irreducible curve $$C$$ of degree $$d$$ has $$n$$ ordinary double points $$p_1, \ldots, p_n$$. The *genus* (geometric genus) $$g$$ of a curve is the genus of the smooth curve obtained by normalization. The genus of a smooth projective plane curve is given by the *genus-degree formula* as $$(d-1)(d-2)/2$$, and in the presence of singularities the genus decreases by the *$$\delta$$-invariant* $$\delta_p$$ of each singularity $$p$$. The $$\delta$$-invariant of an ordinary double point is $$\delta_{p_i} = 1$$. Therefore

$$g = \frac{(d-1)(d-2)}{2} - \sum_{i=1}^n \delta_{p_i} = \frac{(d-1)(d-2)}{2} - n$$

and since the geometric genus cannot be negative,

$$n \leq \frac{(d-1)(d-2)}{2}$$

This upper bound is achievable. For example, taking a smooth curve of degree $$d$$ and projecting it generally onto $$\mathbb{P}^2$$ yields an irreducible curve with exactly $$\frac{(d-1)(d-2)}{2}$$ ordinary double points.
:::

---

**References**

**[Hart]** R. Hartshorne, *Algebraic Geometry*, Graduate Texts in Mathematics, Springer, 1977.  
**[Ful]** W. Fulton, *Intersection Theory*, Springer, 1984.  
**[Sha]** I. R. Shafarevich, *Basic Algebraic Geometry I: Varieties in Projective Space*, Springer, 2013.
