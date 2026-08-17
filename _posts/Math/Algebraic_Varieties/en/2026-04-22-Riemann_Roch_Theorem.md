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
translated_at: 2026-08-17T14:16:17+00:00
translation_source: kimi-cli
---
We now examine in more detail the global section space $H^0(X, \mathcal{L})$ that produces the complete linear system of a line bundle $\mathcal{L}$, which we already encountered in [§Linear Systems, ⁋Definition 2](/en/math/algebraic_varieties/linear_systems#def2). We could have introduced this right after defining linear systems, but the proof requires Serre duality, so we postponed it.

## Riemann–Roch Theorem

::: Definition 1
For a divisor $D$ on a smooth projective curve $C$, we define the *Riemann–Roch dimension* as

$$\ell(D) = \dim H^0(C, \mathcal{O}_C(D))$$

:::

In general, we think of $\mathcal{O}_C(D)$ as the sheaf of rational functions that may have poles of order at most $\operatorname{ord}_p D$ at each point $p$ according to $D$, so from this perspective $H^0(C, \mathcal{O}_C(D))$ can be viewed as a space of functions defined on $C$.

Recall that this space $H^0(C, \mathcal{O}_C(D))$ was first introduced in [§Linear Systems, ⁋Definition 2](/en/math/algebraic_varieties/linear_systems#def2). According to that discussion, the nonzero sections of $H^0(C, \mathcal{O}_C(D))$ define effective divisors linearly equivalent to the given divisor $D$, and projectivizing this space yields the *complete linear system* $\lvert \mathcal{O}_C(D)\rvert$ of $\mathcal{O}_C(D)$. For convenience, we shall write this as $\lvert D\rvert$ in this post. Then the Riemann–Roch dimension defined above equals the projective dimension of $\lvert D\rvert$ plus $1$.

Now fix a point $p\in C$. Then the elements of $\lvert D\rvert$ passing through $p$ can be thought of, by definition, as those sections among the elements of $H^0(C,\mathcal{O}_C(D))$ satisfying $s(p)=0$. That is, such $s$ are elements of $H^0(C, \mathcal{O}_C(D))$ satisfying $\divisor(s)-p\geq 0$, and through this we can verify that the collection of exactly these elements is precisely the global section of

$$\mathcal{O}_C(D-p)\cong \mathcal{O}_C(D)\otimes \mathcal{O}_C(-p)$$

Therefore, if equality holds in $H^0(C,\mathcal{O}_C(D-p))\subseteq H^0(C, \mathcal{O}_C(D))$, this means that every element of $\lvert D\rvert$ passes through $p$, so $p$ becomes a base point of $\lvert D\rvert$. On the other hand, if $\lvert D\rvert$ is basepoint-free, then we could use this in [§Linear Systems](/en/math/algebraic_varieties/linear_systems) to define a regular map $\varphi_D:C\rightarrow \mathbb{P}^{\ell(D)-1}$, and from this perspective the difference between $\ell(D)$ and $\ell(D-p)$ can be viewed as a correction term that the point $p$ imposes on the divisor $D$.

Then the Riemann–Roch theorem, which we shall examine in this post and the next, extends this in a certain sense, with the canonical class $K_C$ playing a global role that replaces the role of the point $p$. Specifically, the formula we wish to prove is

$$\ell(D)-\ell(K_C-D)=\deg D+1-g$$

where $\deg D+1$ is the expected value, $g$ is the loss due to the topological data of the curve, and $\ell(K_C-D)$ is the correction term arising from the positional relationship between the canonical class and $D$.

To see this, we first apply Serre duality to obtain

$$H^1(C, \mathcal{O}_C(D)) \cong H^0(C, \omega_C \otimes \mathcal{O}_C(-D))^\vee = H^0(C, \mathcal{O}_C(K_C - D))^\vee\tag{$1$}$$

([§Serre Duality, ⁋Proposition 2](/en/math/algebraic_varieties/serre_duality#prop2)). Recall here that the canonical divisor $K_C$ was the divisor corresponding to the canonical line bundle. Then by the following lemma, we can deduce that the terms appearing in the Euler characteristic of $\mathcal{O}_C(D)$ are only two. In this post we assume that $\mathbb{K}$ is an *infinite* field.

::: Lemma 2
For any coherent sheaf $\mathcal{F}$ on a smooth projective curve $C$,

$$H^i(C, \mathcal{F}) = 0 \quad (i \ge 2)$$

holds.
:::
::: Proof
Fix an embedding $C\hookrightarrow \mathbb{P}^N$. By dimension count, there exist hyperplanes $H_1,H_2$ such that $C\cap H_1\cap H_2=\emptyset$. Thus, setting $U_i=C\setminus H_i$, we know that these form an affine open cover of $C$.

Now consider the Čech cohomology for $\{U_1,U_2\}$. As briefly introduced shortly after [§Sheaf Cohomology, ⁋Proposition 12](/en/math/algebraic_varieties/sheaf_cohomology#prop12), any affine open cover of a projective variety satisfies the hypotheses of [§Sheaf Cohomology, ⁋Theorem 11](/en/math/algebraic_varieties/sheaf_cohomology#thm11), and therefore the sheaf cohomology we seek reduces exactly to the computation for this affine open cover. Since the Čech complex becomes simply

$$\check{C}(\mathcal{U}, \mathcal{F}):\qquad \mathcal{F}(U_1)\oplus \mathcal{F}(U_2)\rightarrow \mathcal{F}(U_1\cap U_2)\rightarrow 0$$

a complex of length 1, it immediately follows that $\check{H}^i = 0\ (i \ge 2)$.
:::

Therefore, by this result, for any divisor $D$ we have

$$\rchi(\mathcal{O}_C(D)) = h^0(C, \mathcal{O}_C(D)) - h^1(C, \mathcal{O}_C(D))\tag{$2$}$$

where $h^i$ is shorthand notation for the dimension of $H^i$.

On the other hand, from the topological perspective we well know that the Euler characteristic of a genus $g$ compact Riemann surface $S$ is given by

$$\rchi(S)=2(1-g)$$

Here the Euler characteristic can be thought of using triangulation as $V-E+F$ with the number of vertices $V$, edges $E$, and faces $F$[^1], or it can be regarded as defined using differential-geometric tools such as the Gauss-Bonnet theorem.

In algebraic geometry we generally think of the underlying field $\mathbb{K}$ as the complex numbers, so the genus $g$ compact Riemann surface above is nothing but a one-dimensional curve $C_S$ from the algebraic-geometric viewpoint. Then the Euler characteristic in the algebraic-geometric sense is given by substituting $D=0$ into the formula ($2$) above:

$$\rchi(\mathcal{O}_{C_S})=h^0(C_S, \mathcal{O}_{C_S})-h^1(C_S, \mathcal{O}_{C_S})$$

Meanwhile, just as one-dimensional holes in topology appear through $H^1$, the one-dimensional holes in algebraic geometry, namely the genus, are defined by $g=h^1(C_S, \mathcal{O}_{C_S})$, and since global sections are only constant functions, the Euler characteristic of $C_S$ is expressed as

$$\rchi(\mathcal{O}_{C_S})=h^0(C_S, \mathcal{O}_{C_S})-h^1(C_S, \mathcal{O}_{C_S})=1-g$$

That this value is half the topological Euler characteristic is no coincidence, and can be verified through Hodge theory, but this is irrelevant to our goal so we shall pass over it for now. What is important is that the Euler characteristic in algebraic geometry, and its value $1-g$ when computed for a curve, is not an arbitrary outcome but rather a reinterpretation of the result from topology.

The Riemann–Roch theorem, the subject of this post, adds one more step to this. The above computation was for the trivial sheaf $\mathcal{O}_{C_S}$ with nothing attached, so we consider the sheaf $\mathcal{O}_{C_S}(D)$ twisted by an arbitrary divisor $D$. Then the result of the Riemann–Roch theorem is that a correction term of $\deg D$ appears.

::: Proposition 3
(Riemann–Roch for curves) For a divisor $D$ on a smooth projective curve $C$,

$$\ell(D) - \ell(K_C - D) = \deg D + 1 - g$$

holds. Here $g$ is the genus of $C$, and $K_C$ is the canonical divisor.
:::

::: Proof
By the above computations and definitions,

$$\rchi(\mathcal{O}_C(D)) = h^0(C, \mathcal{O}_C(D)) - h^1(C, \mathcal{O}_C(D)) = \ell(D) - \ell(K_C - D)$$

On the other hand, for an effective divisor $D$ there exists a short exact sequence

$$0 \rightarrow \mathcal{O}_C \rightarrow \mathcal{O}_C(D) \rightarrow \mathcal{O}_D \rightarrow 0$$

and then by additivity of the Euler characteristic, $\rchi(\mathcal{O}_C(D)) = \rchi(\mathcal{O}_C) + \rchi(\mathcal{O}_D)$.

Here $\mathcal{O}_D$ is a skyscraper sheaf of degree $\deg D$, so $\rchi(\mathcal{O}_D) = \deg D$, and as examined above $\rchi(\mathcal{O}_C)=1-g$, so combining this with the previous formula yields the desired result. For a general (not necessarily effective) divisor, we express $D$ as a difference of effective divisors and apply the same additivity argument.
:::

The above proof is clean, but its geometric content is compressed inside the Euler characteristic, so it may not be intuitively immediate. To supplement this, let us read the equality term by term. First, by definition

$$\ell(D) = \dim H^0(C, \mathcal{O}_C(D))$$

and geometrically the space on the right-hand side, $H^0(C, \mathcal{O}_C(D))$, is the collection of meromorphic functions satisfying

$$\divisor(f)+D\geq 0$$

That is, $D$ forces the poles of $f$ to occur only inside the support of $D$, and the order of the pole at each point $p$ to be at most $\operatorname{ord}_p D$, so as $\deg D$ increases the allowed pole orders also increase and thus $\ell(D)$ increases.

Moreover, since in our situation $C$ is one-dimensional, an (effective) divisor is of the form $D=\sum n_i p_i$, and using this we can more quantitatively obtain the following inequality for a divisor $D$ with $\ell(D)>0$:

$$\ell(D)\leq \deg(D)+1\tag{$3$}$$

Specifically, assuming $D = \sum n_i p_i$ is effective, we can consider the linear map sending $f\in H^0(C, \mathcal{O}_C(D))$ to its principal part at each point $p_i$:

$$H^0(C, \mathcal{O}_C(D)) \longrightarrow \bigoplus_i \mathbb{K}^{n_i}\tag{$4$}$$

Intuitively, this is the map that, when $f$ is expressed with the principal part of its Laurent polynomial at the point $p_i$ as

$$\frac{a_{-n_i}}{(x-p_i)^{n_i}}+\frac{a_{-n_i+1}}{(x-p_i)^{n_i-1}}+\cdots +\frac{a_{-1}}{x-p_i}$$

considers

$$f\mapsto (a_{-n_i}, \ldots, a_{-1})$$

for all $p_i$ at once. Then the dimension of the right-hand side of the above linear map is $\sum n_i = \deg D$, and its kernel is the global sections without poles, that is $H^0(C, \mathcal{O}_C) = \mathbb{K}$, from which we obtain $\ell(D) \leq 1 + \deg D$. If $D$ is not effective but $\ell(D) > 0$, then $D$ is linearly equivalent to some effective divisor, so the same inequality holds.

In general, for this inequality to become an equality the linear map must be surjective, but this does not always hold. To verify this, consider from the short exact sequence examined in the proof of [Proposition 3](#prop3)

$$0\longrightarrow \mathcal{O}_C\overset{i}{\longrightarrow} \mathcal{O}_C(D)\overset{p}{\longrightarrow} \mathcal{O}_D\longrightarrow 0$$

the long exact sequence

$$0\longrightarrow H^0(C,\mathcal{O}_C)\overset{i^\ast}{\longrightarrow} H^0(C,\mathcal{O}_C(D)) \overset{p^\ast}{\longrightarrow} H^0(C,\mathcal{O}_D) \overset{\delta}{\longrightarrow} H^1(C,\mathcal{O}_C)\overset{i^\ast}{\longrightarrow} H^1(C,\mathcal{O}_C(D))\rightarrow 0$$

Here since $C$ is a curve and $D=\sum n_i p_i$, $\mathcal{O}_D$ is a skyscraper sheaf of degree $\deg D$ supported on the support of $D$, and from this we know $H^0(C, \mathcal{O}_D)=\bigoplus_i \mathbb{K}^{n_i}$. Moreover, we know that the linear map ($4$) examined above actually coincides with $p^\ast$ in this long exact sequence, and from this the cokernel of $p^\ast$ can be computed through the following chain of isomorphisms:

$$\coker p^\ast=\frac{H^0(C, \mathcal{O}_D)}{\im p^\ast}=\frac{H^0(C, \mathcal{O}_D)}{\ker\delta}\cong \im\delta\cong\ker i^\ast$$

and in particular its dimension is

$$\dim\coker p^\ast =\dim \ker (i^\ast: H^1(C, \mathcal{O}_C)\twoheadrightarrow H^1(C, \mathcal{O}_C(D)))=\dim H^1(C, \mathcal{O}_C)-\dim H^1(C, \mathcal{O}_C(D))$$

If we apply formula (1) here, we know

$$\dim\coker p^\ast=\dim H^1(C, \mathcal{O}_C)-\dim H^0(C, \mathcal{O}_C(K_C-D))^\vee=g-\ell(K_C-D)$$

In the inequality ($3$) above, the difference between $\deg(D)+1$ and $\ell(D)$ is precisely the dimension of the cokernel, so these computations recover the result of [Proposition 3](#prop3). In other words, $\ell(K_C-D)$ is the quantity measuring how far $\ell(D)$ falls from its upper bound $\deg D+1$, which was originally a counting problem for $1$-forms vanishing along $D$ but was rewritten as $\ell(K_C-D)$ using Serre duality.

For example, consider the case where $\deg D$ is very large so that $\deg(K_C-D)<0$. Then in this case $\ell(K_C-D)=0$, and therefore the Riemann–Roch theorem gives the formula

$$\ell(D)=\deg D+1-g$$

That is, as the genus increases, the space created by divisors of the same degree becomes smaller. However, in general the influence of $\ell(K_C-D)$ is added to this, and what must be noted here is that the term $\ell(K_C-D)$ can vary depending not only on the degree of $D$ but also on what relationship $D$ has with the canonical class $K_C$.

As another special example, substituting $D=0$ gives

$$\ell(0)-\ell(K_C)=\deg D+1-g$$

where $\deg D=0$, $\ell(0)=1$, so we find that $\ell(K_C)=g$ holds. Now substituting $D=K_C$ gives

$$\ell(K_C)-\ell(0)=\deg K_C +1-g$$

and from this we can recover the computation $\deg(K_C)=2g-2$ from [§Canonical Line Bundle, ⁋Example 10](/en/math/algebraic_varieties/canonical_bundle#ex10). In that example the degree-genus formula was mentioned as a well-known formula and $\deg(K_C)$ was obtained from it (and this is more historically justified), but shortly we shall see in [Proposition 7](#prop7) that the degree-genus formula is a special case of the Riemann–Roch theorem.

In any case, summarizing the computations so far, $\ell(D)$ is the dimension of the complete linear system of $D$, $\ell(K_C - D)$ is the correction term that $K_C$ imposes on $D$, and for large degree this correction term disappears while for small degree it reflects the geometric information of $K_C$.

::: Example 4
**$\mathbb{P}^1$**: The genus of $\mathbb{P}^1$ is $g = 0$, and the canonical divisor is $K_{\mathbb{P}^1} = -2H$ ([§Canonical Line Bundle, ⁋Example 8](/en/math/algebraic_varieties/canonical_bundle#ex8)). On the other hand, we showed in [§Line Bundles and Vector Bundles, ⁋Example 16](/en/math/algebraic_varieties/line_bundles#ex16) that the global sections of $\mathcal{O}_{\mathbb{P}^1}(d)$ are homogeneous polynomials of degree $d$, so we know

$$\ell(dH) = d+1 \quad (d \ge 0), \qquad \ell(dH) = 0 \quad (d < 0)$$

holds. Now verifying the Riemann–Roch formula, for $D = dH$ we have $\deg D = d$ and $K_C - D = (-2-d)H$, so

$$\ell(dH) - \ell(-2H-dH) = d + 1 - 0 = d + 1$$

and both sides agree at $d+1$.
:::

::: Example 5 (Elliptic curve)
In the genus $1$ case $g = 1$, we know from the above computations that $\deg K_C=2g-2=0$ and $\ell(K_C)=g=1$. Since $\ell(K_C)=1>0$, as seen earlier there exists an effective divisor linearly equivalent to $K_C$, but $\deg K_C=0$ and the only effective divisor of degree $0$ is $0$, so $K_C\sim 0$. Using this, Riemann–Roch becomes

$$\ell(D) - \ell(-D) = \deg D$$

In particular, if $\deg D > 0$ then $\ell(-D) = 0$, so $\ell(D) = \deg D$.

The case $\deg D=0$ is the small-degree case mentioned above; first, from inequality ($3$) we must have $\ell(D)=0$ or $\ell(D)=1$. If $\ell(D)=1$, there exists a unique effective divisor linearly equivalent to $D$, but its degree is $0$ so this is $0$. Therefore $D\sim 0$, and conversely if $D\sim 0$ then $\mathcal{O}_C(D)\cong \mathcal{O}_C$, so $\ell(D)=1$. That is, the term $\ell(K_C-D)$ becomes $1$ only when $D$ is linearly equivalent to $0$, and $0$ otherwise.
:::

Since $K_C \sim 0$, Riemann–Roch becomes particularly simple on an elliptic curve. If $\deg D > 0$, the correction term $\ell(K_C-D)=\ell(-D)$ vanishes, so $\ell(D)=\deg D$ is completely determined, which shows that $g=1$ is the simplest non-trivial case in the process where the influence of correction terms becomes more complicated as the genus increases.

::: Example 6 ($g=2$)
Now let us look at the one-step more complicated case of $g=2$. In this case $\deg K_C = 2g - 2 = 2$ and $\ell(K_C)=2$, and substituting $D=p$ into [Proposition 3](#prop3) yields

$$\ell(p)-\ell(K_C-p)=2-g$$

If $\ell(p)\ge 2$, then there exists a degree 1 morphism $C\rightarrow\mathbb{P}^1$, which would imply $C\cong\mathbb{P}^1$, contradicting $g=2$, so $\ell(p)=1$, and since $2-g=0$ from the above formula, $\ell(K_C-p)=\ell(p)=1=\ell(K_C)-1<\ell(K_C)$. Since this holds for every $p\in C$, $\lvert K_C\rvert$ is basepoint-free, and therefore the canonical map

$$\varphi_{K_C}:C\rightarrow \mathbb{P}^1$$

is well-defined. Then the preimage of a hyperplane in $\mathbb{P}^1$, that is, of a point in $\mathbb{P}^1$, becomes an effective divisor linearly equivalent to $K_C$, and from the fact that this is a degree $2$ map we can write $K_C$ as a sum of two points $p_1+p_2$.

Now let us apply Riemann–Roch to multiples $D=d\cdot p$ of a single point $p$ and examine how $\ell(D)$ varies with $d$. For small $d$, that is, where $\ell(K_C-D)$ is still alive, special phenomena appear, but as $d$ increases $\ell(D)$ stabilizes linearly.

1. The case $d=1$ was already examined above: $\ell(p)=1$ and by Riemann–Roch $\ell(K_C-p)=1$.
2. For $d=2$, if $2p\sim K_C$ then $\ell(2p)=2$. In this case $p$ is called a *Weierstrass point*; this condition corresponds exactly to the situation where the preimage of some point under the canonical map $\varphi_{K_C}$ above is collapsed at $p$. For a generic point $2p\not\sim K_C$, so $\ell(2p)=1$.
3. For $d\ge 3$, we have $\deg(K_C-D)=2-d<0$, so $\ell(K_C-D)=0$, and therefore $\ell(D)=d-1$.
:::

The canonical map $\varphi_{K_C}: C \rightarrow \mathbb{P}^1$ for $g=2$ examined in the above example was a 2:1 branched covering. More generally, among curves of genus $g \ge 2$, those for which there exists a degree 2 covering to $\mathbb{P}^1$ are called *hyperelliptic curves*, and those not of this form are called *non-hyperelliptic curves*. Note that by convention the cases of genus $0,1$ are excluded from hyperelliptic curves.

Now let us examine the properties of the morphism $\varphi_{K_C} : C \rightarrow \mathbb{P}^{g-1}$ defined by the complete linear system $\lvert K_C\rvert$ of the canonical bundle $K_C$ for $C$ with $g\geq 2$. We have verified above that $\deg K_C = 2g - 2$ and $h^0(K_C) = g$, so the codomain of $\varphi_{K_C}$ is $\mathbb{P}^{g-1}$. However, this is not a closed embedding when $C$ is hyperelliptic, which we already confirmed in the case $g=2$ where this becomes a 2:1 covering map. Computing this concretely, one finds that $\varphi_{K_C}$ arises as the composition of the Veronese map $\mathbb{P}^1 \hookrightarrow \mathbb{P}^{g-1}$ with the hyperelliptic covering $C\rightarrow \mathbb{P}^1$.

## Degree-Genus Formula

In [§Canonical Line Bundle, ⁋Example 10](/en/math/algebraic_varieties/canonical_bundle#ex10) we asserted the following proposition as a well-known fact to show that $\deg K_C=2g-2$, but now we can prove it rigorously. However, this is exactly the opposite of that example: there the degree-genus formula and adjunction formula were used to prove $\deg K_C=2g-2$, whereas now we derive the degree-genus formula from the fact that $\deg K_C=2g-2$ and the adjunction formula. Note that the degree of $K_C$ was already obtained from Riemann–Roch (without using the degree-genus formula) before [Example 4](#ex4) above.

::: Proposition 7 (Degree-genus formula)
For a smooth plane curve $C \subseteq \mathbb{P}^2$ of degree $d$,

$$g(C) = \frac{(d-1)(d-2)}{2}$$

holds.
:::

::: Proof
By the adjunction formula of [§Canonical Line Bundle, ⁋Proposition 9](/en/math/algebraic_varieties/canonical_bundle#prop9), $K_C = (K_{\mathbb{P}^2} + C)\vert_C = (d-3)H\vert_C$. Therefore $\deg K_C = d(d-3)$, and substituting this into $\deg K_C = 2g - 2$ yields

$$d(d-3) = 2g - 2 \implies g = \frac{d(d-3) + 2}{2} = \frac{(d-1)(d-2)}{2}$$

:::

This formula directly computes the geometric properties of plane curves. For example, the genus of a smooth plane cubic is 1, so this is the same as the elliptic curve treated in [Example 5](#ex5). On the other hand, for $d = 1, 2$ we have $g = 0$, reflecting that both lines and conics are birationally equivalent to $\mathbb{P}^1$. A line is itself isomorphic to $\mathbb{P}^1$, and for a smooth conic the projection from a point on it gives a birational map between the conic and $\mathbb{P}^1$, so by [§Rational Maps, ⁋Proposition 10](/en/math/algebraic_varieties/rational_maps#prop10) this is equivalent to their function fields being isomorphic.

::: Example 8
Computing the genus according to degree $d$, for degree 3 (cubic) we have $g = \frac{2 \cdot 1}{2} = 1$, an elliptic curve; for degree 4 (quartic) we have $g = \frac{3 \cdot 2}{2} = 3$, and for degree 5 (quintic) we have $g = \frac{4 \cdot 3}{2} = 6$. Since the genus increases rapidly with degree, smooth plane curves of higher degree have increasingly complex topological structure.
:::

---

**References**

**[Hart]** R. Hartshorne, *Algebraic Geometry*, Graduate Texts in Mathematics, Springer, 1977.  
**[Sha]** I. R. Shafarevich, *Basic Algebraic Geometry I: Varieties in Projective Space*, Springer, 2013.

---

[^1]: This agrees with defining the Euler characteristic as the alternating sum of cohomology.
