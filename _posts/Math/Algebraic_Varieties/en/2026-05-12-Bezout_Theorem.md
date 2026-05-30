---
title: "Bézout's Theorem"
description: "Bezout's theorem in algebraic geometry states that in projective space over an algebraically closed field, two curves with no common component intersect in a number of points equal to the product of their degrees. Taking multiplicity into account, two conics meet in exactly four points."
excerpt: "Bézout's theorem and its applications"

categories: [Math / Algebraic Varieties]
permalink: /en/math/algebraic_varieties/bezout_theorem
sidebar: 
    nav: "algebraic_varieties-en"

header:
    overlay_image: /assets/images/Math/Algebraic_Varieties/Bezout_Theorem.png
    overlay_filter: 0.5

date: 2026-03-15
last_modified_at: 2026-04-02
weight: 20
translated_at: 2026-05-30T11:00:05+00:00
translation_source: kimi-cli
last_polished_at: 2026-05-30T11:00:05+00:00
---
In this post we introduce Bézout's theorem, a classical result in algebraic geometry. Intuitively, given two curves $$C,D$$ in the plane, the number of their intersection points depends on their degrees: for instance, the parabola $$\y=x^2$$ and a line in the plane generally meet at two points. Bézout's theorem generalizes this observation.

<div class="proposition" markdown="1">

<ins id="prop1">**Proposition 1 (Bézout)**</ins> In $$\mathbb{P}^n$$ over an algebraically closed field, if hypersurfaces $$H_1, \ldots, H_n$$ of degrees $$d_1, \ldots, d_n$$ have no common component, then

$$\deg(H_1 \cap \cdots \cap H_n) = d_1 \cdots d_n$$

holds. Here the intersection is taken with multiplicity.

</div>

In particular, two curves of degrees $$m,n$$ in $$\mathbb{P}^2$$ meet at $$mn$$ points. Care must be taken that they share no common component; for instance, two identical curves cannot be analyzed in this way.

<div class="example" markdown="1">

<ins id="ex2">**Example 2 (Two conics)**</ins> Consider two conics in $$\mathbb{P}^2$$

$$C_1 = Z(\x_0^2 + \x_1^2 - \x_2^2),\qquad C_2 = Z(\x_0\x_1)$$

$$C_1$$ is the projectivization of a cone, and $$C_2$$ is the union of the two lines $$Z(\x_0)$$ and $$Z(\x_1)$$. These two curves have no common component, so by Bézout's theorem they should have $$2 \times 2 = 4$$ intersection points. Indeed, computing the intersection: when $$\x_0 = 0$$ we obtain $$\x_1^2 = \x_2^2$$, yielding $$[0:1:1]$$ and $$[0:1:-1]$$; when $$\x_1 = 0$$ we obtain $$\x_0^2 = \x_2^2$$, yielding $$[1:0:1]$$ and $$[1:0:-1]$$. Thus they meet at exactly four points.

</div>

## Proof

Rather than proving the general case, we prove Bézout's theorem in $$\mathbb{P}^2$$. For this we use the following lemma.

<div class="proposition" markdown="1">

<ins id="prop3">**Proposition 3 (Hilbert polynomial)**</ins> For a projective variety $$X \subseteq \mathbb{P}^n$$ with homogeneous coordinate ring $$S(X)$$, the function $$H(t) = \dim_\mathbb{K} S(X)_t$$ is called the **Hilbert function** of $$X$$. By the Hilbert–Serre theorem, this function agrees with a polynomial $$P_X(t)$$ for $$t \gg 0$$, and this polynomial is called the **Hilbert polynomial** of $$X$$.

In particular, for a curve $$C = Z(F) \subseteq \mathbb{P}^2$$ of degree $$d$$, the Hilbert polynomial of $$S(C) = \mathbb{K}[\x_0, \x_1, \x_2]/(F)$$ is

$$P_C(t) = dt + \frac{d(3-d)}{2}$$

Here the degree of $$P_C$$ is $$1$$, the dimension of $$C$$; the leading coefficient is $$\deg C = d$$; and the constant term $$P_C(0) = \frac{d(3-d)}{2} = 1 - \frac{(d-1)(d-2)}{2}$$ is the arithmetic genus of $$C$$.

</div>

The Hilbert function $$H(t)$$ counts the number of independent homogeneous polynomials of degree $$t$$ that do not vanish identically on $$C$$—in other words, the number of homogeneous polynomials that act as distinct functions on $$C$$. As $$t$$ grows, this number grows polynomially; its degree equals $$1$$, the dimension of $$C$$; its leading coefficient is proportional to the degree $$d$$; and its constant term equals the arithmetic genus $$1 - \frac{(d-1)(d-2)}{2}$$.

<details class="proof" markdown="1">
<summary>Proof</summary>

Let $$S = \mathbb{K}[\x_0, \x_1, \x_2]$$. The dimension of $$(S/(F))_t$$ equals the dimension of the space obtained from $$S_t$$ by removing the multiples of $$F$$. Since multiplication by $$F$$, $$\cdot F: S(-d) \to S$$, is injective, we obtain the short exact sequence

$$0 \to S(-d) \xrightarrow{\cdot F} S \to S/(F) \to 0$$

Since $$\dim_\mathbb{K} S_t = \binom{t+2}{2}$$, comparing dimensions in degree $$t$$ gives

$$\dim_\mathbb{K} (S/(F))_t = \binom{t+2}{2} - \binom{t-d+2}{2}$$

Expanding this,

$$\frac{(t+2)(t+1)}{2} - \frac{(t-d+2)(t-d+1)}{2} = dt + \frac{d(3-d)}{2}$$

which yields the claim.

</details>

This result is used crucially in the proof of [Proposition 5](#prop5) below.

<div class="proposition" markdown="1">

<ins id="prop4">**Proposition 4**</ins> For a curve $$C = Z(F)$$ of degree $$d$$ in $$\mathbb{P}^2$$, the intersection $$C \cap L$$ with a general line $$L$$ consists of exactly $$d$$ points (counted with multiplicity).

</div>

This proposition is the simplest special case of Bézout's theorem. It captures the geometric intuition that a curve of degree $$d$$ meets a general line in $$d$$ points.

<details class="proof" markdown="1">
<summary>Proof</summary>

Without loss of generality, let $$L = Z(\x_2)$$. Since $$C$$ is defined by a homogeneous polynomial $$F(\x_0, \x_1, \x_2)$$ of degree $$d$$, substituting $$\x_2 = 0$$ in $$L \cap C$$ yields $$F(\x_0, \x_1, 0)$$. This is a homogeneous polynomial of degree $$d$$ in $$\x_0, \x_1$$, and over an algebraically closed field it has exactly $$d$$ roots (counted with multiplicity). Since $$L$$ is general, $$F(\x_0, \x_1, 0)$$ is not the zero polynomial; otherwise $$\x_2$$ would divide $$F$$, so $$C$$ would contain $$L$$ as a component, contradicting the hypothesis.

</details>

We now prove Proposition 1. The argument has two main parts. First we show that the sum of intersection multiplicities equals the dimension of a global algebraic object, and second we compute that dimension to be exactly $$mn$$ using the Hilbert polynomial.

<div class="proposition" markdown="1">

<ins id="prop5">**Proposition 5**</ins> (Proof of Proposition 1) If two curves $$C = Z(F)$$, $$D = Z(G)$$ of degrees $$m$$, $$n$$ in $$\mathbb{P}^2$$ have no common component, then $$\sum_p i_p(C, D) = mn$$.

</div>

<details class="proof" markdown="1">
<summary>Proof</summary>

We divide the proof into two steps.

**Step 1.** We first establish the equality

> $$\sum_{p \in C \cap D} i_p(C, D) = \dim_\mathbb{K} (\mathbb{K}[\x_0, \x_1, \x_2]/(F, G))_t \qquad (t \gg 0)$$

That $$C \cap D$$ is finite follows from the hypothesis that $$C$$ and $$D$$ have no common component. ([§Dimension, ⁋Example 14](/en/math/algebraic_varieties/dimension#ex14)) For a point $$p = [a:b:c] \in C \cap D$$, assuming $$c \neq 0$$, we have coordinates $$p = (a/c, b/c)$$ in $$U_2$$, and for the dehomogenizations $$f, g \in \mathbb{K}[\x, \y]$$ of $$F, G$$,

$$i_p(C, D) = \dim_\mathbb{K} \mathcal{O}_{\mathbb{A}^2, p}/(f, g)$$

Since $$V(F, G)$$ is finite, $$f, g$$ generate a zero-dimensional ideal $$(f, g)$$ in the affine ring $$\mathbb{K}[\x, \y]$$, and by the Chinese remainder theorem

$$\mathbb{K}[\x, \y]/(f, g) \cong \prod_{p \in V(f,g)} \mathcal{O}_{\mathbb{A}^2, p}/(f, g)$$

Therefore $$\dim_\mathbb{K} \mathbb{K}[\x, \y]/(f, g) = \sum_p i_p(C, D)$$.

On the other hand, the Hilbert function $$H(t) = \dim_\mathbb{K} R_t$$ of the quotient $$R = S/(F, G)$$ of $$S = \mathbb{K}[\x_0, \x_1, \x_2]$$ becomes constant for $$t \gg 0$$ (proved in Step 2), and this constant equals $$\dim_\mathbb{K} \mathbb{K}[\x, \y]/(f, g)$$. Indeed, for $$t \gg 0$$ there exist polynomials of degree $$t$$ that can be adjusted independently at each intersection point, so the evaluation map $$R_t \to \mathbb{K}^{\lvert V(F,G) \rvert}$$ is surjective.

**Step 2.** We now show that $$\dim_\mathbb{K} (\mathbb{K}[\x_0, \x_1, \x_2]/(F, G))_t = mn$$ for $$t \gg 0$$. Write $$S = \mathbb{K}[\x_0, \x_1, \x_2]$$. Since $$F, G$$ have no common irreducible factor, the multiplication maps $$\cdot F: S(-m) \to S$$ and $$\cdot G: S/(F)(-n) \to S/(F)$$ are both injective, yielding the two short exact sequences

$$0 \to S(-m) \xrightarrow{\cdot F} S \to S/(F) \to 0$$
$$0 \to S/(F)(-n) \xrightarrow{\cdot G} S/(F) \to S/(F, G) \to 0$$

Reading the degree as $$m$$ in Proposition 3 ([Proposition 3](#prop3)), the Hilbert polynomial of $$S/(F)$$ has the form $$P_F(t) = mt + c_1$$. Applying the Hilbert polynomial to the second exact sequence, the Hilbert polynomial of $$S/(F, G)$$ is

$$P_{F,G}(t) = P_F(t) - P_F(t - n) = \bigl(mt + c_1\bigr) - \bigl(m(t-n) + c_1\bigr) = mn$$

Hence for $$t \gg 0$$ the dimension of $$(S/(F, G))_t$$ is the constant $$mn$$, and by Step 1 we obtain $$\sum_p i_p(C, D) = mn$$.

</details>

## Generalization

So far we have proved Bézout's theorem only for curves in $$\mathbb{P}^2$$. To extend it to arbitrary projective spaces and general projective varieties, one needs the Chow ring. The key fact is

$$\operatorname{CH}^\ast(\mathbb{P}^n) \cong \mathbb{Z}[H]/(H^{n+1})$$

Here $$H$$ is the hyperplane class, and a variety of codimension $$k$$ and degree $$d$$ has class $$dH^k$$. In particular, a hypersurface of degree $$d$$ corresponds to $$dH$$, so the intersection product of $$n$$ hypersurfaces $$H_1, \ldots, H_n$$ is

$$[H_1] \cdot [H_2] \cdots [H_n] = (d_1 H)(d_2 H) \cdots (d_n H) = d_1 d_2 \cdots d_n \cdot H^n$$

Since $$H^n$$ is the class of a point in $$\mathbb{P}^n$$ and has degree 1, we obtain $$\deg(H_1 \cap \cdots \cap H_n) = d_1 \cdots d_n$$. With this intuition, the generalized Bézout theorem is stated as follows.

<div class="proposition" markdown="1">

<ins id="prop6">**Proposition 6 (Generalized Bézout's Theorem)**</ins> For two projective varieties $$V, W$$ in $$\mathbb{P}^n$$,

$$\deg(V \cap W) \leq \deg(V) \cdot \deg(W)$$

holds. Here $$\deg(V \cap W)$$ is the sum of the degrees of the irreducible components of $$V \cap W$$. Equality holds when $$V$$ and $$W$$ intersect properly (that is, when $$\operatorname{codim}(Z) = \operatorname{codim}(V) + \operatorname{codim}(W)$$ for every irreducible component $$Z$$ of $$V \cap W$$); in this case, assigning an intersection multiplicity $$m_Z$$ to each component $$Z$$, we have $$\sum_Z m_Z \deg(Z) = \deg(V) \cdot \deg(W)$$.

</div>

<div class="example" markdown="1">

<ins id="ex7">**Example 7 ($$\mathbb{P}^3$$)**</ins> Consider two quadric surfaces $$Q_1, Q_2$$ in $$\mathbb{P}^3$$. Each has degree 2, so when they intersect properly, the intersection $$Q_1 \cap Q_2$$ is a curve of dimension 1 and degree 4. Concretely, taking $$Q_1 = Z(\x_0\x_3 - \x_1\x_2)$$ and $$Q_2 = Z(\x_0\x_2 - \x_1\x_3)$$, the intersection decomposes into four lines, and the sum of their degrees is still 4.

</div>

The proof of Proposition 6 relies on the general theory of intersection theory via the Chow ring. For details see [§Intersection Product](/en/math/algebraic_varieties/intersection_product). The inequality of ([§Dimension, ⁋Example 14](/en/math/algebraic_varieties/dimension#ex14)) reappears in terms of the codimensions of components.

## Applications

### Cayley–Bacharach Theorem

<div class="proposition" markdown="1">

<ins id="prop8">**Proposition 8 (Special case of the Cayley–Bacharach theorem)**</ins> Suppose two cubic curves $$C_1 = Z(F_1)$$, $$C_2 = Z(F_2)$$ in $$\mathbb{P}^2$$ have no common component and meet in nine distinct points $$p_1, \ldots, p_9$$ as a proper intersection. Then any cubic curve $$C_3 = Z(F_3)$$ passing through $$p_1, \ldots, p_8$$ also passes through $$p_9$$.

</div>

<details class="proof" markdown="1">
<summary>Proof</summary>

Assume that the two cubic curves $$C_1, C_2$$ meet in nine distinct points $$p_1, \ldots, p_9$$ as a proper intersection. The space $$\mathbb{K}[\x_0, \x_1, \x_2]_3$$ of homogeneous polynomials of degree 3 on $$\mathbb{P}^2$$ has dimension $$\binom{3+2}{2} = 10$$, and the condition of passing through each point $$p_i$$ imposes one linear condition. Hence the subspace $$V = \{F \in \mathbb{K}[\x_0, \x_1, \x_2]_3 : F(p_i) = 0 \text{ for } i = 1, \ldots, 8\}$$ has dimension $$\dim V \ge 10 - 8 = 2$$. On the other hand, $$F_1, F_2 \in V$$, and since $$C_1 \neq C_2$$, the polynomials $$F_1, F_2$$ are linearly independent. If the eight points are in general position, then $$\dim V = 2$$ and $$F_1, F_2$$ form a basis of $$V$$. Therefore, for any $$F_3 \in V$$ there exist constants $$\alpha, \beta$$ such that $$F_3 = \alpha F_1 + \beta F_2$$. Evaluating both sides at $$p_9$$ gives $$F_3(p_9) = \alpha F_1(p_9) + \beta F_2(p_9) = 0$$, so $$C_3$$ passes through $$p_9$$ as well.</details>

The intuition behind this result is as follows. The condition of passing through eight of the nine intersection points of two cubics imposes eight linear constraints on the space of cubics (which is 10-dimensional), leaving a 1-dimensional space whose elements all pass through the ninth point as well. This shows that the outcome $$3 \times 3 = 9$$ from Bézout's theorem is no accident.

### Pascal's Theorem

<div class="proposition" markdown="1">

<ins id="prop9">**Proposition 9 (Pascal's Theorem)**</ins> Given six points $$A, B, C, D, E, F$$ on a conic, if the three intersection points

$$P = \overline{AB} \cap \overline{DE},\quad Q = \overline{BC} \cap \overline{EF},\quad R = \overline{CD} \cap \overline{FA}$$

all exist, then these three points are collinear.

</div>

<details class="proof" markdown="1">
<summary>Proof</summary>

Let $$\Gamma$$ denote the conic. Define two cubic curves

$$X = \overline{AB} \cup \overline{CD} \cup \overline{EF},\quad Y = \overline{BC} \cup \overline{DE} \cup \overline{FA}.$$

Each is the union of three lines, hence a curve of degree 3. Under the general position hypothesis, $$X$$ and $$Y$$ have no common component.

Since $$X \cap Y$$ contains $$A, B, C, D, E, F$$ and $$P, Q, R$$, it contains at least nine distinct points. By Bézout's theorem, $$\sum_{p \in X \cap Y} i_p(X, Y) = 3 \times 3 = 9$$; hence $$X \cap Y$$ consists exactly of these nine points, and the intersection multiplicity at each point is 1.

Now define a new cubic curve $$Z = \Gamma \cup \overline{PQ}$$. This is a curve of degree 3 passing through eight of the nine points of $$X \cap Y$$, namely $$A, B, C, D, E, F$$ and $$P, Q$$. By Proposition 8 ([Proposition 8](#prop8)), $$Z$$ must also pass through the ninth point $$R$$. Since $$R \in Z = \Gamma \cup \overline{PQ}$$, we have either $$R \in \Gamma$$ or $$R \in \overline{PQ}$$.

If $$R \in \Gamma$$, then we would have $$R = \overline{CD} \cap \overline{FA} \in \Gamma$$. However, by Bézout's theorem, $$\overline{CD}$$ and $$\Gamma$$ meet in at most two points; since $$C, D \in \Gamma$$ already, we have $$\overline{CD} \cap \Gamma = \{C, D\}$$. Likewise $$\overline{FA} \cap \Gamma = \{F, A\}$$, so $$R$$ cannot lie in $$\Gamma$$. Therefore $$R \in \overline{PQ}$$; that is, $$P, Q, R$$ are collinear.

</details>

### Maximum Number of Double Points

Bézout's theorem yields an upper bound on the number of singular points of a plane curve.

<div class="proposition" markdown="1">

<ins id="prop10">**Proposition 10**</ins> The maximum number of ordinary double points (double points with two distinct tangents) that an irreducible plane curve of degree $$d$$ can have is $$\binom{d-1}{2} = \frac{(d-1)(d-2)}{2}$$.

</div>

<details class="proof" markdown="1">
<summary>Proof</summary>

Suppose an irreducible curve $$C$$ of degree $$d$$ has $$n$$ ordinary double points $$p_1, \ldots, p_n$$. The *genus* (geometric genus) $$g$$ of the curve is the genus of the smooth curve obtained by normalization. The genus of a smooth projective plane curve is given by the *genus–degree formula* as $$(d-1)(d-2)/2$$; in the presence of singularities, the genus decreases by the *$$\delta$$-invariant* $$\delta_p$$ at each singular point $$p$$. For an ordinary double point the $$\delta$$-invariant is $$\delta_{p_i} = 1$$. Therefore

$$g = \frac{(d-1)(d-2)}{2} - \sum_{i=1}^n \delta_{p_i} = \frac{(d-1)(d-2)}{2} - n$$

and since the geometric genus cannot be negative,

$$n \leq \frac{(d-1)(d-2)}{2}$$

This bound is sharp. For example, projecting a smooth curve of degree $$d$$ generally into $$\mathbb{P}^2$$ yields an irreducible curve with exactly $$\frac{(d-1)(d-2)}{2}$$ ordinary double points.

</details>

---

**References**

**[Hart]** R. Hartshorne, *Algebraic Geometry*, Graduate Texts in Mathematics, Springer, 1977.  
**[Ful]** W. Fulton, *Intersection Theory*, Springer, 1984.  
**[Sha]** I. R. Shafarevich, *Basic Algebraic Geometry I: Varieties in Projective Space*, Springer, 2013.
