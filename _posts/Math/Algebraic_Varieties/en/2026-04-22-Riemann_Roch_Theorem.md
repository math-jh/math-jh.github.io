---
title: "The Riemann–Roch Theorem for Curves"
description: "We discuss the Riemann–Roch theorem for curves, examine the meaning of complete linear systems and the Riemann–Roch dimension, and then derive the theorem's formula through its relationship with the canonical divisor."
excerpt: "The Riemann–Roch theorem for curves"

categories: [Math / Algebraic Varieties]
permalink: /en/math/algebraic_varieties/riemann_roch_theorem
sidebar:
    nav: "algebraic_varieties-en"

date: 2026-04-22
weight: 16
translated_at: 2026-08-19T01:15:04+00:00
translation_source: kimi-cli
last_polished_at: 2026-08-19T01:15:04+00:00
---
We now examine in more detail the global section space $H^0(X, \mathcal{L})$ that produces the complete linear system of a line bundle $\mathcal{L}$, which we already encountered in [§Linear Systems, ⁋Definition 2](/en/math/algebraic_varieties/linear_systems#def2). We could have introduced this right after defining linear systems, but the proof requires Serre duality, so we postponed it.

## Riemann–Roch Theorem

::: Definition 1
For a divisor $D$ on a smooth projective curve $C$, we define the *Riemann–Roch dimension* as

$$\ell(D) = \dim H^0(C, \mathcal{O}_C(D))$$

:::

In general, we regard $\mathcal{O}_C(D)$ as the sheaf of rational functions that may have poles of order at most $\operatorname{ord}_p D$ at each point $p$ prescribed by $D$, so from this viewpoint $H^0(C, \mathcal{O}_C(D))$ can be thought of as a space of functions defined on $C$.

Recall that this space $H^0(C, \mathcal{O}_C(D))$ was first introduced in [§Linear Systems, ⁋Definition 2](/en/math/algebraic_varieties/linear_systems#def2). According to that discussion, the nonzero sections of $H^0(C, \mathcal{O}_C(D))$ define effective divisors linearly equivalent to the given divisor $D$, and projectivizing this space yields the *complete linear system* $\lvert \mathcal{O}_C(D)\rvert$ of $\mathcal{O}_C(D)$. For convenience we shall write this as $\lvert D\rvert$ in this post. Then the Riemann–Roch dimension defined above equals the projective dimension of $\lvert D\rvert$ plus $1$.

Now fix a point $p\in C$. By definition, the elements of $\lvert D\rvert$ passing through $p$ are precisely those sections in $H^0(C,\mathcal{O}_C(D))$ satisfying $s(p)=0$. That is, such $s$ are elements of $H^0(C, \mathcal{O}_C(D))$ with $\divisor(s)-p\geq 0$, and one verifies that the collection of exactly these elements forms the global sections of

$$\mathcal{O}_C(D-p)\cong \mathcal{O}_C(D)\otimes \mathcal{O}_C(-p)$$

Hence, if equality holds in the inclusion $H^0(C,\mathcal{O}_C(D-p))\subseteq H^0(C, \mathcal{O}_C(D))$, this means every element of $\lvert D\rvert$ passes through $p$, so $p$ is a base point of $\lvert D\rvert$. Conversely, if $\lvert D\rvert$ is basepoint-free, then as in [§Linear Systems](/en/math/algebraic_varieties/linear_systems) we can use it to define a regular map $\varphi_D:C\rightarrow \mathbb{P}^{\ell(D)-1}$; from this perspective the difference between $\ell(D)$ and $\ell(D-p)$ can be viewed as a correction term imposed by the point $p$ on the divisor $D$.

The Riemann–Roch theorem, which we examine in this post and the next, extends this idea in a certain sense: the canonical class $K_C$ plays a global role that replaces the point $p$. Specifically, the formula we wish to prove is

$$\ell(D)-\ell(K_C-D)=\deg D+1-g$$

where $\deg D+1$ is the expected value, $g$ is the loss due to the topological data of the curve, and $\ell(K_C-D)$ is the correction term arising from the positional relationship between the canonical class and $D$.

To see this, we first apply Serre duality to obtain

$$H^1(C, \mathcal{O}_C(D)) \cong H^0(C, \omega_C \otimes \mathcal{O}_C(-D))^\vee = H^0(C, \mathcal{O}_C(K_C - D))^\vee\tag{$1$}$$

([§Serre Duality, ⁋Proposition 2](/en/math/algebraic_varieties/serre_duality#prop2)). Recall that the canonical divisor $K_C$ corresponds to the canonical line bundle. Then by the following lemma we can deduce that only two terms appear in the Euler characteristic of $\mathcal{O}_C(D)$. In this post we assume that $\mathbb{K}$ is an *infinite* field.

::: Lemma 2
For any coherent sheaf $\mathcal{F}$ on a smooth projective curve $C$,

$$H^i(C, \mathcal{F}) = 0 \quad (i \ge 2)$$

holds.
:::
::: Proof
Fix an embedding $C\hookrightarrow \mathbb{P}^N$. By a dimension count, there exist hyperplanes $H_1,H_2$ such that $C\cap H_1\cap H_2=\emptyset$. Setting $U_i=C\setminus H_i$, we know that these form an affine open cover of $C$.

Now consider the Čech cohomology for $\{U_1,U_2\}$. As was briefly mentioned shortly after [§Sheaf Cohomology, ⁋Proposition 12](/en/math/algebraic_varieties/sheaf_cohomology#prop12), any affine open cover of a projective variety satisfies the hypotheses of [§Sheaf Cohomology, ⁋Theorem 11](/en/math/algebraic_varieties/sheaf_cohomology#thm11), so the sheaf cohomology we seek reduces exactly to the computation for this affine open cover. Since the Čech complex is simply

$$\check{C}(\mathcal{U}, \mathcal{F}):\qquad \mathcal{F}(U_1)\oplus \mathcal{F}(U_2)\rightarrow \mathcal{F}(U_1\cap U_2)\rightarrow 0$$

a complex of length 1, it follows immediately that $\check{H}^i = 0\ (i \ge 2)$.
:::

Therefore, by this result, for any divisor $D$ we have

$$\rchi(\mathcal{O}_C(D)) = h^0(C, \mathcal{O}_C(D)) - h^1(C, \mathcal{O}_C(D))\tag{$2$}$$

where $h^i$ is shorthand for the dimension of $H^i$.

On the other hand, from the topological perspective we well know that the Euler characteristic of a compact Riemann surface $S$ of genus $g$ is given by

$$\rchi(S)=2(1-g)$$

Here the Euler characteristic can be understood via triangulation as $V-E+F$ with $V$, $E$, and $F$ the numbers of vertices, edges, and faces[^1], or it can be taken as defined by differential-geometric tools such as the Gauss–Bonnet theorem.

In algebraic geometry we generally regard the underlying field $\mathbb{K}$ as the complex numbers, so the genus $g$ compact Riemann surface above is nothing but a one-dimensional curve $C_S$ from the algebraic-geometric viewpoint. Then the Euler characteristic in the algebraic-geometric sense is obtained by substituting $D=0$ into formula ($2$):

$$\rchi(\mathcal{O}_{C_S})=h^0(C_S, \mathcal{O}_{C_S})-h^1(C_S, \mathcal{O}_{C_S})$$

Meanwhile, just as one-dimensional holes in topology are detected by $H^1$, the one-dimensional holes in algebraic geometry, namely the genus, are given by $g=h^1(C_S, \mathcal{O}_{C_S})$, and since global sections are only constant functions, the Euler characteristic of $C_S$ is

$$\rchi(\mathcal{O}_{C_S})=h^0(C_S, \mathcal{O}_{C_S})-h^1(C_S, \mathcal{O}_{C_S})=1-g$$

That this value is half the topological Euler characteristic is no coincidence, and can be verified through Hodge theory; however, this is irrelevant to our present goal, so we set it aside. What matters is that the Euler characteristic in algebraic geometry, and its value $1-g$ for a curve, is not an arbitrary outcome but rather a reinterpretation of the topological result.

The Riemann–Roch theorem, the subject of this post, adds one further step. The computation above was for the trivial sheaf $\mathcal{O}_{C_S}$ with nothing attached; we now consider the sheaf $\mathcal{O}_{C_S}(D)$ twisted by an arbitrary divisor $D$. The conclusion of the Riemann–Roch theorem is that a correction term of $\deg D$ appears.

::: Proposition 3
(Riemann–Roch for curves) For a divisor $D$ on a smooth projective curve $C$,

$$\ell(D) - \ell(K_C - D) = \deg D + 1 - g$$

holds. Here $g$ is the genus of $C$, and $K_C$ is the canonical divisor.
:::

::: Proof
By the computations and definitions above,

$$\rchi(\mathcal{O}_C(D)) = h^0(C, \mathcal{O}_C(D)) - h^1(C, \mathcal{O}_C(D)) = \ell(D) - \ell(K_C - D)$$

On the other hand, for an effective divisor $D$ there is a short exact sequence

$$0 \rightarrow \mathcal{O}_C \rightarrow \mathcal{O}_C(D) \rightarrow \mathcal{O}_D \rightarrow 0$$

and by additivity of the Euler characteristic, $\rchi(\mathcal{O}_C(D)) = \rchi(\mathcal{O}_C) + \rchi(\mathcal{O}_D)$.

Here $\mathcal{O}_D$ is a skyscraper sheaf of degree $\deg D$, so $\rchi(\mathcal{O}_D) = \deg D$, and as we saw above $\rchi(\mathcal{O}_C)=1-g$; combining this with the preceding formula yields the desired result. For a general (not necessarily effective) divisor, write $D$ as a difference of effective divisors and apply the same additivity argument.
:::

The proof above is clean, but its geometric content is compressed inside the Euler characteristic, so it may not be immediately intuitive. To remedy this, let us read the equality term by term. First, by definition

$$\ell(D) = \dim H^0(C, \mathcal{O}_C(D))$$

and geometrically the space on the right-hand side, $H^0(C, \mathcal{O}_C(D))$, is the collection of meromorphic functions satisfying

$$\divisor(f)+D\geq 0$$

That is, $D$ forces the poles of $f$ to occur only inside the support of $D$, and the order of the pole at each point $p$ to be at most $\operatorname{ord}_p D$; consequently, as $\deg D$ grows the allowed pole orders increase and so does $\ell(D)$.

Moreover, since in our situation $C$ is one-dimensional, any (effective) divisor has the form $D=\sum n_i p_i$, and using this we can obtain the following more quantitative inequality for any divisor $D$ with $\ell(D)>0$:

$$\ell(D)\leq \deg(D)+1\tag{$3$}$$

Specifically, if $D = \sum n_i p_i$ is effective, consider the linear map sending $f\in H^0(C, \mathcal{O}_C(D))$ to its principal part at each point $p_i$:

$$H^0(C, \mathcal{O}_C(D)) \longrightarrow \bigoplus_i \mathbb{K}^{n_i}\tag{$4$}$$

Intuitively, when $f$ is expressed with the principal part of its Laurent polynomial at $p_i$ as

$$\frac{a_{-n_i}}{(x-p_i)^{n_i}}+\frac{a_{-n_i+1}}{(x-p_i)^{n_i-1}}+\cdots +\frac{a_{-1}}{x-p_i}$$

this map is

$$f\mapsto (a_{-n_i}, \ldots, a_{-1})$$

considered for all $p_i$ simultaneously. Then the dimension of the target of the above linear map is $\sum n_i = \deg D$, and its kernel consists of the pole-free global sections, i.e. $H^0(C, \mathcal{O}_C) = \mathbb{K}$, whence $\ell(D) \leq 1 + \deg D$. If $D$ is not effective but $\ell(D) > 0$, then $D$ is linearly equivalent to some effective divisor, so the same inequality holds.

In general, for this inequality to be an equality the linear map must be surjective, but this is not always the case. To see why, consider the long exact sequence induced by the short exact sequence examined in the proof of [Proposition 3](#prop3):

$$0\longrightarrow \mathcal{O}_C\overset{i}{\longrightarrow} \mathcal{O}_C(D)\overset{p}{\longrightarrow} \mathcal{O}_D\longrightarrow 0$$

$$0\longrightarrow H^0(C,\mathcal{O}_C)\overset{i^\ast}{\longrightarrow} H^0(C,\mathcal{O}_C(D)) \overset{p^\ast}{\longrightarrow} H^0(C,\mathcal{O}_D) \overset{\delta}{\longrightarrow} H^1(C,\mathcal{O}_C)\overset{i^\ast}{\longrightarrow} H^1(C,\mathcal{O}_C(D))\rightarrow 0$$

Since $C$ is a curve and $D=\sum n_i p_i$, the sheaf $\mathcal{O}_D$ is a skyscraper sheaf of degree $\deg D$ supported on the support of $D$, so $H^0(C, \mathcal{O}_D)=\bigoplus_i \mathbb{K}^{n_i}$. Moreover, the linear map ($4$) examined above actually coincides with $p^\ast$ in this long exact sequence; hence the cokernel of $p^\ast$ can be computed via the chain of isomorphisms

$$\coker p^\ast=\frac{H^0(C, \mathcal{O}_D)}{\im p^\ast}=\frac{H^0(C, \mathcal{O}_D)}{\ker\delta}\cong \im\delta\cong\ker i^\ast$$

and in particular its dimension is

$$\dim\coker p^\ast =\dim \ker (i^\ast: H^1(C, \mathcal{O}_C)\twoheadrightarrow H^1(C, \mathcal{O}_C(D)))=\dim H^1(C, \mathcal{O}_C)-\dim H^1(C, \mathcal{O}_C(D))$$

Applying formula (1), we obtain

$$\dim\coker p^\ast=\dim H^1(C, \mathcal{O}_C)-\dim H^0(C, \mathcal{O}_C(K_C-D))^\vee=g-\ell(K_C-D)$$

In the inequality ($3$), the gap between $\deg(D)+1$ and $\ell(D)$ is precisely the dimension of this cokernel, so these computations recover the result of [Proposition 3](#prop3). In other words, $\ell(K_C-D)$ measures how far $\ell(D)$ falls below its upper bound $\deg D+1$; originally this was a counting problem for $1$-forms vanishing along $D$, but Serre duality rewrites it as $\ell(K_C-D)$.

For example, suppose $\deg D$ is very large, so that $\deg(K_C-D)<0$. Then $\ell(K_C-D)=0$, and the Riemann–Roch theorem gives

$$\ell(D)=\deg D+1-g$$

That is, as the genus increases, the space produced by divisors of the same degree becomes smaller. In general, however, the term $\ell(K_C-D)$ contributes as well, and it must be noted that this term can vary depending not only on the degree of $D$ but also on the geometric relationship between $D$ and the canonical class $K_C$.

As another special case, substituting $D=0$ yields

$$\ell(0)-\ell(K_C)=\deg D+1-g$$

where $\deg D=0$ and $\ell(0)=1$, so we find $\ell(K_C)=g$. Substituting $D=K_C$ then gives

$$\ell(K_C)-\ell(0)=\deg K_C +1-g$$

and from this we recover the computation $\deg(K_C)=2g-2$ from [§Canonical Line Bundle, ⁋Example 10](/en/math/algebraic_varieties/canonical_bundle#ex10). In that example the degree-genus formula was invoked as a well-known fact to obtain $\deg(K_C)$ (which is historically more justified), but shortly we shall see in [Proposition 7](#prop7) that the degree-genus formula is in fact a special case of the Riemann–Roch theorem.

Summarizing the computations so far, $\ell(D)$ is the dimension of the complete linear system of $D$, while $\ell(K_C - D)$ is the correction term that $K_C$ imposes on $D$; for large degree this correction term vanishes, whereas for small degree it reflects the geometric information of $K_C$.

::: Example 4
**$\mathbb{P}^1$**: The genus of $\mathbb{P}^1$ is $g = 0$, and the canonical divisor is $K_{\mathbb{P}^1} = -2H$ ([§Canonical Line Bundle, ⁋Example 8](/en/math/algebraic_varieties/canonical_bundle#ex8)). On the other hand, we showed in [§Line Bundles and Vector Bundles, ⁋Example 16](/en/math/algebraic_varieties/line_bundles#ex16) that the global sections of $\mathcal{O}_{\mathbb{P}^1}(d)$ are the homogeneous polynomials of degree $d$, so

$$\ell(dH) = d+1 \quad (d \ge 0), \qquad \ell(dH) = 0 \quad (d < 0)$$

Verifying the Riemann–Roch formula, for $D = dH$ we have $\deg D = d$ and $K_C - D = (-2-d)H$, whence

$$\ell(dH) - \ell(-2H-dH) = d + 1 - 0 = d + 1$$

and both sides agree.
:::

::: Example 5 (Elliptic curve)
In the genus $1$ case $g = 1$, the above computations give $\deg K_C=2g-2=0$ and $\ell(K_C)=g=1$. Since $\ell(K_C)=1>0$, as noted earlier there exists an effective divisor linearly equivalent to $K_C$; but $\deg K_C=0$ and the only effective divisor of degree $0$ is $0$, so $K_C\sim 0$. Using this, Riemann–Roch becomes

$$\ell(D) - \ell(-D) = \deg D$$

In particular, if $\deg D > 0$ then $\ell(-D) = 0$, so $\ell(D) = \deg D$.

The case $\deg D=0$ is the small-degree situation mentioned above. From inequality ($3$) we must have $\ell(D)=0$ or $\ell(D)=1$. If $\ell(D)=1$, there exists a unique effective divisor linearly equivalent to $D$, but its degree is $0$, so it is $0$. Therefore $D\sim 0$, and conversely if $D\sim 0$ then $\mathcal{O}_C(D)\cong \mathcal{O}_C$, so $\ell(D)=1$. Thus the term $\ell(K_C-D)$ equals $1$ precisely when $D\sim 0$, and $0$ otherwise.
:::

Since $K_C \sim 0$, Riemann–Roch is especially simple on an elliptic curve. When $\deg D > 0$, the correction term $\ell(K_C-D)=\ell(-D)$ vanishes and $\ell(D)=\deg D$ is completely determined. This shows that $g=1$ is the simplest non-trivial case in the progression where the influence of correction terms grows more intricate as the genus increases.

::: Example 6 ($g=2$)
Now consider the next more complicated case, $g=2$. Here $\deg K_C = 2g - 2 = 2$ and $\ell(K_C)=2$, and substituting $D=p$ into [Proposition 3](#prop3) yields

$$\ell(p)-\ell(K_C-p)=2-g$$

If $\ell(p)\ge 2$, there would exist a degree 1 morphism $C\rightarrow\mathbb{P}^1$, forcing $C\cong\mathbb{P}^1$ and contradicting $g=2$; hence $\ell(p)=1$. Since $2-g=0$, we obtain $\ell(K_C-p)=\ell(p)=1=\ell(K_C)-1<\ell(K_C)$. As this holds for every $p\in C$, the linear system $\lvert K_C\rvert$ is basepoint-free, and therefore the canonical map

$$\varphi_{K_C}:C\rightarrow \mathbb{P}^1$$

is well-defined. The preimage of a hyperplane in $\mathbb{P}^1$ (that is, of a point in $\mathbb{P}^1$) is an effective divisor linearly equivalent to $K_C$, and since this is a degree $2$ map we can write $K_C$ as a sum of two points $p_1+p_2$.

Now apply Riemann–Roch to multiples $D=d\cdot p$ of a single point $p$ and examine how $\ell(D)$ varies with $d$. For small $d$, where $\ell(K_C-D)$ is still active, special phenomena occur, but as $d$ grows $\ell(D)$ stabilizes linearly.

1. The case $d=1$ was already examined above: $\ell(p)=1$ and by Riemann–Roch $\ell(K_C-p)=1$.
2. For $d=2$, if $2p\sim K_C$ then $\ell(2p)=2$. The point $p$ is then called a *Weierstrass point*; this condition corresponds exactly to the situation where the preimage of some point under the canonical map $\varphi_{K_C}$ is ramified at $p$. For a generic point $2p\not\sim K_C$, so $\ell(2p)=1$.
3. For $d\ge 3$, we have $\deg(K_C-D)=2-d<0$, so $\ell(K_C-D)=0$ and therefore $\ell(D)=d-1$.
:::

The canonical map $\varphi_{K_C}: C \rightarrow \mathbb{P}^1$ for $g=2$ examined above is a 2:1 branched covering. More generally, among curves of genus $g \ge 2$, those admitting a degree 2 covering of $\mathbb{P}^1$ are called *hyperelliptic curves*, and those not of this form are called *non-hyperelliptic curves*. By convention, the cases of genus $0$ and $1$ are excluded from hyperelliptic curves.

Now let us examine the properties of the morphism $\varphi_{K_C} : C \rightarrow \mathbb{P}^{g-1}$ defined by the complete linear system $\lvert K_C\rvert$ of the canonical bundle $K_C$ for $C$ with $g\geq 2$. We verified above that $\deg K_C = 2g - 2$ and $h^0(K_C) = g$, so the target of $\varphi_{K_C}$ is $\mathbb{P}^{g-1}$. However, this is not a closed embedding when $C$ is hyperelliptic; we already saw this for $g=2$, where it becomes a 2:1 covering map. Computing concretely, one finds that $\varphi_{K_C}$ factors as the composition of the Veronese embedding $\mathbb{P}^1 \hookrightarrow \mathbb{P}^{g-1}$ with the hyperelliptic covering $C\rightarrow \mathbb{P}^1$.

## Degree-Genus Formula

In [§Canonical Line Bundle, ⁋Example 10](/en/math/algebraic_varieties/canonical_bundle#ex10) we asserted the following proposition as a well-known fact in order to show that $\deg K_C=2g-2$, but now we can prove it rigorously. This proceeds in exactly the opposite direction to that example: there the degree-genus formula and adjunction formula were used to prove $\deg K_C=2g-2$, whereas now we derive the degree-genus formula from $\deg K_C=2g-2$ together with the adjunction formula. Note that the degree of $K_C$ was already obtained from Riemann–Roch (without using the degree-genus formula) before [Example 4](#ex4) above.

::: Proposition 7 (Degree-genus formula)
For a smooth plane curve $C \subseteq \mathbb{P}^2$ of degree $d$,

$$g(C) = \frac{(d-1)(d-2)}{2}$$

holds.
:::

::: Proof
By the adjunction formula of [§Canonical Line Bundle, ⁋Proposition 9](/en/math/algebraic_varieties/canonical_bundle#prop9), $K_C = (K_{\mathbb{P}^2} + C)\vert_C = (d-3)H\vert_C$. Hence $\deg K_C = d(d-3)$, and substituting into $\deg K_C = 2g - 2$ yields

$$d(d-3) = 2g - 2 \implies g = \frac{d(d-3) + 2}{2} = \frac{(d-1)(d-2)}{2}$$

:::

This formula gives a direct computation of the geometric invariants of plane curves. For example, a smooth plane cubic has genus 1, so it is an elliptic curve as treated in [Example 5](#ex5). On the other hand, for $d = 1, 2$ we obtain $g = 0$, reflecting that both lines and smooth conics are birationally equivalent to $\mathbb{P}^1$. A line is itself isomorphic to $\mathbb{P}^1$, and for a smooth conic the projection from a point on it gives a birational map between the conic and $\mathbb{P}^1$; by [§Rational Maps, ⁋Proposition 10](/en/math/algebraic_varieties/rational_maps#prop10) this is equivalent to their function fields being isomorphic.

::: Example 8
Computing the genus by degree $d$: for degree 3 (cubic) we have $g = \frac{2 \cdot 1}{2} = 1$, an elliptic curve; for degree 4 (quartic) we have $g = \frac{3 \cdot 2}{2} = 3$; and for degree 5 (quintic) we have $g = \frac{4 \cdot 3}{2} = 6$. Since the genus grows rapidly with degree, smooth plane curves of higher degree have increasingly complex topological structure.
:::

---

**References**

**[Hart]** R. Hartshorne, *Algebraic Geometry*, Graduate Texts in Mathematics, Springer, 1977.  
**[Sha]** I. R. Shafarevich, *Basic Algebraic Geometry I: Varieties in Projective Space*, Springer, 2013.

---

[^1]: This agrees with defining the Euler characteristic as the alternating sum of cohomology.
