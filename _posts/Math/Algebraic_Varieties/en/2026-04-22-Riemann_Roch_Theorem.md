---
title: "The Riemann–Roch Theorem for Curves"
description: "We discuss the Riemann–Roch theorem for curves, examine the meaning of complete linear systems and the Riemann–Roch dimension, and then derive the formula of the theorem through its relationship with the canonical divisor."
excerpt: "The Riemann–Roch theorem for curves"

categories: [Math / Algebraic Varieties]
permalink: /en/math/algebraic_varieties/riemann_roch_theorem
sidebar:
    nav: "algebraic_varieties-en"

date: 2026-04-22
weight: 16
translated_at: 2026-08-19T01:15:04+00:00
translation_source: kimi-cli
last_polished_at: 2026-09-27T23:15:06+00:00
translation_polish_source: antigravity-gemini-3.8-flash-high
---
We now examine in more detail, for the line bundle $\mathcal{L}$ examined in [§Linear Systems, ⁋Definition 2](/en/math/algebraic_varieties/linear_systems#def2){: data-lid="e3o65" }, the global section space $H^0(X, \mathcal{L})$ that produces the complete linear system. This could have been introduced right after introducing linear systems, but because the proof requires Serre duality, we postponed it. 

## Riemann–Roch Theorem

::: Definition 1
On a smooth projective curve $C$, for a divisor $D$, we define the *Riemann–Roch dimension* by

$$\ell(D) = \dim H^0(C, \mathcal{O}_C(D))$$

:::

In general, since we regard $\mathcal{O}_C(D)$ as the sheaf of rational functions that along $D$ may have at each point $p$ poles of order at most $\operatorname{ord}_p D$, from this viewpoint $H^0(C, \mathcal{O}_C(D))$ can be thought of as a space of functions defined on $C$. 

Recall that this space $H^0(C, \mathcal{O}_C(D))$ was first introduced in [§Linear Systems, ⁋Definition 2](/en/math/algebraic_varieties/linear_systems#def2){: data-lid="5558a" }. According to it, the nonzero sections of the space $H^0(C, \mathcal{O}_C(D))$ define effective divisors linearly equivalent to the given divisor $D$, and by projectivizing this space we could obtain the *complete linear system* of $\mathcal{O}_C(D)$, $\lvert \mathcal{O}_C(D)\rvert$. In this post, for convenience we write this as $\lvert D\rvert$. Then the Riemann–Roch dimension above is the projective dimension of $\lvert D\rvert$ plus $1$. 

Now fix a point $p\in C$. Then the elements passing through $p$ in $\lvert D\rvert$ can, by definition, be thought of as those sections among the elements of $H^0(C,\mathcal{O}_C(D))$ that satisfy $s(p)=0$. That is, such $s$ are sections satisfying $\divisor(s)-p\geq 0$ in $H^0(C, \mathcal{O}_C(D))$, and through this we can verify that the collection of exactly these elements consists of the global sections of

$$\mathcal{O}_C(D-p)\cong \mathcal{O}_C(D)\otimes \mathcal{O}_C(-p)$$

Therefore, if equality holds in $H^0(C,\mathcal{O}_C(D-p))\subseteq H^0(C, \mathcal{O}_C(D))$, this means that every element of $\lvert D\rvert$ passes through $p$, so $p$ becomes a base point of $\lvert D\rvert$. On the other hand, if $\lvert D\rvert$ is basepoint-free, in [§Linear Systems](/en/math/algebraic_varieties/linear_systems){: data-lid="sk1fe" } we could use it to define a regular map $\varphi_D:C\rightarrow \mathbb{P}^{\ell(D)-1}$; from this perspective, the difference between $\ell(D)$ and $\ell(D-p)$ can be viewed as a correction term that the point $p$ imposes on the divisor $D$. 

Then the Riemann–Roch theorem, which we examine in this post and the next, extends this in a certain sense, with the canonical class $K_C$ playing a global role that replaces the role of the point $p$. Specifically, the formula we wish to prove is

$$\ell(D)-\ell(K_C-D)=\deg D+1-g$$

where $\deg D+1$ is the expected value, $g$ is the loss imposed by the topological data of the curve, and $\ell(K_C-D)$ is the correction term imposed by the relative position between the canonical class and $D$. 

To see this, first applying Serre duality gives

$$H^1(C, \mathcal{O}_C(D)) \cong H^0(C, \omega_C \otimes \mathcal{O}_C(-D))^\vee = H^0(C, \mathcal{O}_C(K_C - D))^\vee\tag{$1$}$$

([§Serre Duality, ⁋Proposition 2](/en/math/algebraic_varieties/serre_duality#prop2){: data-lid="6qko6" }). Recall that here the canonical divisor $K_C$ was the divisor corresponding to the canonical line bundle. Then by the following lemma, we can deduce that only two terms appear in the Euler characteristic of $\mathcal{O}_C(D)$. In this post, we assume that $\mathbb{K}$ is an *infinite* field.

::: Lemma 2
On a smooth projective curve $C$, for any coherent sheaf $\mathcal{F}$,

$$H^i(C, \mathcal{F}) = 0 \quad (i \ge 2)$$

holds.
:::
::: Proof
Fixing an embedding $C\hookrightarrow \mathbb{P}^N$, by a dimension count there exist hyperplanes satisfying $C\cap H_1\cap H_2=\emptyset$, namely $H_1,H_2$. Therefore, setting $U_i=C\setminus H_i$, we know that these form an affine open cover of $C$.

Now consider the Čech cohomology for $\{U_1,U_2\}$. As was briefly introduced shortly after [§Sheaf Cohomology, ⁋Proposition 12](/en/math/algebraic_varieties/sheaf_cohomology#prop12){: data-lid="2fn80" }, any affine open cover of a projective variety satisfies the hypotheses of [§Sheaf Cohomology, ⁋Theorem 11](/en/math/algebraic_varieties/sheaf_cohomology#thm11){: data-lid="n7lv0" }, so the sheaf cohomology we seek reduces exactly to the computation for this affine open cover. Now, since the Čech complex is simply

$$\check{C}(\mathcal{U}, \mathcal{F}):\qquad \mathcal{F}(U_1)\oplus \mathcal{F}(U_2)\rightarrow \mathcal{F}(U_1\cap U_2)\rightarrow 0$$

a complex of length 1, $\check{H}^i = 0\ (i \ge 2)$ follows immediately.
:::

Therefore, by this result, for any divisor $D$,

$$\rchi(\mathcal{O}_C(D)) = h^0(C, \mathcal{O}_C(D)) - h^1(C, \mathcal{O}_C(D))\tag{$2$}$$

holds. Here, $h^i$ is shorthand notation for the dimension of $H^i$.

Meanwhile, from a topological perspective, we know well that the Euler characteristic of a genus $g$ compact Riemann surface $S$ is given by

$$\rchi(S)=2(1-g)$$

Here, the Euler characteristic can be thought of via a triangulation using the number of vertices $V$, the number of edges $E$, and the number of faces $F$ as $V-E+F$[^1], or it can be regarded as defined using differential-geometric tools such as the Gauss–Bonnet theorem.

In algebraic geometry, we generally regard the underlying field $\mathbb{K}$ as the complex numbers, so the genus $g$ compact Riemann surface above is nothing but a one-dimensional curve $C_S$ from the viewpoint of algebraic geometry. Then, the Euler characteristic from the viewpoint of algebraic geometry is therefore given by substituting $D=0$ into equation ($2$) above:

$$\rchi(\mathcal{O}_{C_S})=h^0(C_S, \mathcal{O}_{C_S})-h^1(C_S, \mathcal{O}_{C_S})$$

Meanwhile, just as a $1$-dimensional hole in topology manifests through $H^1$, the 1-dimensional hole in algebraic geometry, namely the genus, is defined by $g=h^1(C_S, \mathcal{O}_{C_S})$, and since the only global sections are constant functions, the Euler characteristic of $C_S$ appears as

$$\rchi(\mathcal{O}_{C_S})=h^0(C_S, \mathcal{O}_{C_S})-h^1(C_S, \mathcal{O}_{C_S})=1-g$$

That this value is half the topological Euler characteristic is no coincidence, and can be verified through Hodge theory; however, since this is irrelevant to our goal, we set it aside for now. What is important is that the Euler characteristic in algebraic geometry, and the fact that its value turns out to be $1-g$ when computed on a curve, is not an arbitrary outcome but rather a reinterpretation of the topological result.

The Riemann–Roch theorem, the subject of this post, adds one further step to this. Since the computation above was for the trivial sheaf $\mathcal{O}_{C_S}$ with nothing attached, one considers twisting it by an arbitrary divisor $D$ to obtain the sheaf $\mathcal{O}_{C_S}(D)$. Then the result of the Riemann–Roch theorem is that a correction term of $\deg D$ appears.

::: Proposition 3
(Riemann–Roch for curves) On a smooth projective curve $C$, for a divisor $D$,

$$\ell(D) - \ell(K_C - D) = \deg D + 1 - g$$

holds. Here $g$ is the genus of $C$, and $K_C$ is the canonical divisor.
:::

::: Proof
By the computations and definitions above,

$$\rchi(\mathcal{O}_C(D)) = h^0(C, \mathcal{O}_C(D)) - h^1(C, \mathcal{O}_C(D)) = \ell(D) - \ell(K_C - D)$$

Meanwhile, for an effective divisor $D$, there exists a short exact sequence

$$0 \rightarrow \mathcal{O}_C \rightarrow \mathcal{O}_C(D) \rightarrow \mathcal{O}_D \rightarrow 0$$

and then by additivity of the Euler characteristic, $\rchi(\mathcal{O}_C(D)) = \rchi(\mathcal{O}_C) + \rchi(\mathcal{O}_D)$.

Here, since $\mathcal{O}_D$ is a skyscraper sheaf of degree $\deg D$, we have $\rchi(\mathcal{O}_D) = \deg D$, and as seen above, $\rchi(\mathcal{O}_C)=1-g$; combining this with the preceding equation yields the desired result. For a general (not effective) divisor, it suffices to express $D$ as the difference with an effective divisor $D'$ and then apply the same additivity argument.
:::

The proof above is clean, but its geometric content is compressed inside the Euler characteristic, so it may not be immediately intuitive. To supplement this, let us read the equality term by term. First, by definition,

$$\ell(D) = \dim H^0(C, \mathcal{O}_C(D))$$

and here the space $H^0(C, \mathcal{O}_C(D))$ on the right-hand side is geometrically the collection of meromorphic functions satisfying

$$\divisor(f)+D\geq 0$$

That is, $D$ forces the poles of $f$ to occur only inside the support of $D$, and the order of the pole at each point $p$ to be at most $\operatorname{ord}_p D$; consequently, as $\deg D$ grows, the allowed pole order also increases, so $\ell(D)$ increases.

Moreover, since in our situation $C$ is $1$-dimensional, an (effective) divisor is of the form $D=\sum n_i p_i$, and using this, when $\ell(D)>0$ for a divisor $D$, we can obtain more quantitatively the following inequality:

$$\ell(D)\leq \deg(D)+1\tag{$3$}$$

Specifically, if $D = \sum n_i p_i$ is effective, we can consider the linear map sending $f\in H^0(C, \mathcal{O}_C(D))$ to its principal part at each point $p_i$:

$$H^0(C, \mathcal{O}_C(D)) \longrightarrow \bigoplus_i \mathbb{K}^{n_i}\tag{$4$}$$

Intuitively, when the principal part of the Laurent polynomial of $f$ at the point $p_i$ is expressed as the following formula

$$\frac{a_{-n_i}}{(x-p_i)^{n_i}}+\frac{a_{-n_i+1}}{(x-p_i)^{n_i-1}}+\cdots +\frac{a_{-1}}{x-p_i}$$

this is the function considering

$$f\mapsto (a_{-n_i}, \ldots, a_{-1})$$

simultaneously for all $p_i$. Then the dimension of the right-hand side of the above linear map is $\sum n_i = \deg D$, and the kernel of this map is equal to the global sections having no poles, that is, $H^0(C, \mathcal{O}_C) = \mathbb{K}$, from which we obtain $\ell(D) \leq 1 + \deg D$. If $D$ is not effective but $\ell(D) > 0$, then $D$ is linearly equivalent to some effective divisor, so the same inequality holds.

In general, for this formula to become an equality, the linear map must be surjective, but this does not always hold. To verify this, consider the short exact sequence examined in the proof of [Proposition 3](#prop3){: data-lid="pe306" }

$$0\longrightarrow \mathcal{O}_C\overset{i}{\longrightarrow} \mathcal{O}_C(D)\overset{p}{\longrightarrow} \mathcal{O}_D\longrightarrow 0$$

and the long exact sequence obtained from it:

$$0\longrightarrow H^0(C,\mathcal{O}_C)\overset{i^\ast}{\longrightarrow} H^0(C,\mathcal{O}_C(D)) \overset{p^\ast}{\longrightarrow} H^0(C,\mathcal{O}_D) \overset{\delta}{\longrightarrow} H^1(C,\mathcal{O}_C)\overset{i^\ast}{\longrightarrow} H^1(C,\mathcal{O}_C(D))\rightarrow 0$$

Here, since $C$ is a curve and $D=\sum n_i p_i$, the sheaf $\mathcal{O}_D$ is a skyscraper sheaf having the support of $D$ of degree $\deg D$, and from this we know that $H^0(C, \mathcal{O}_D)=\bigoplus_i \mathbb{K}^{n_i}$. Moreover, we know that the linear map ($4$) examined above actually coincides with $p^\ast$ in this long exact sequence, and from this, the cokernel of $p^\ast$ can be obtained via the following chain of isomorphisms:

$$\coker p^\ast=\frac{H^0(C, \mathcal{O}_D)}{\im p^\ast}=\frac{H^0(C, \mathcal{O}_D)}{\ker\delta}\cong \im\delta\cong\ker i^\ast$$

and in particular its dimension is

$$\dim\coker p^\ast =\dim \ker (i^\ast: H^1(C, \mathcal{O}_C)\twoheadrightarrow H^1(C, \mathcal{O}_C(D)))=\dim H^1(C, \mathcal{O}_C)-\dim H^1(C, \mathcal{O}_C(D))$$

If we apply equation (1) here, we see that

$$\dim\coker p^\ast=\dim H^1(C, \mathcal{O}_C)-\dim H^0(C, \mathcal{O}_C(K_C-D))^\vee=g-\ell(K_C-D)$$

Since the difference between $\deg(D)+1$ and $\ell(D)$ in the inequality ($3$) above is precisely the dimension of the cokernel, these computations recover the result of [Proposition 3](#prop3){: data-lid="lk2wi" }. That is, in other words, $\ell(K_C-D)$ is a quantity that measures how far $\ell(D)$ falls below its upper bound $\deg D+1$; while this is originally a problem of counting, along $D$, vanishing $1$-forms, Serre duality was used to rewrite it as $\ell(K_C-D)$.

For example, consider the case where $\deg D$ is very large and satisfies $\deg(K_C-D)<0$. Then in this case $\ell(K_C-D)=0$, and therefore the Riemann–Roch theorem gives the formula

$$\ell(D)=\deg D+1-g$$

That is, as the genus grows, the space formed by divisors of the same degree becomes narrower. In the general case, however, the effect of $\ell(K_C-D)$ is added here, and what should be noted is that by definition the term $\ell(K_C-D)$ can vary depending not only on the degree of $D$, but also on how $D$ is related to the canonical class $K_C$.

As another special example, if we substitute $D=0$, then from

$$\ell(0)-\ell(K_C)=\deg D+1-g$$

since $\deg D=0$ and $\ell(0)=1$, we know that $\ell(K_C)=g$ holds. Now, if we substitute $D=K_C$, then

$$\ell(K_C)-\ell(0)=\deg K_C +1-g$$

and from this we can recover the computation $\deg(K_C)=2g-2$ in [§Canonical Line Bundle, ⁋Example 10](/en/math/algebraic_varieties/canonical_bundle#ex10){: data-lid="ici1z" }. In that example, the degree-genus formula was mentioned as a well-known formula and $\deg(K_C)$ was obtained from it (and this is more plausible in a historical context), but in a moment we will see in [Proposition 7](#prop7){: data-lid="em01e" } that the degree-genus formula is a special case of the Riemann–Roch theorem.

In any case, summarizing the computations so far, one can think of $\ell(D)$ as the dimension of the complete linear system of $D$, and $\ell(K_C - D)$ as a correction term that $K_C$ imposes on $D$, which vanishes for large degree and reflects the geometric information of $K_C$ for small degree.

::: Example 4
**$\mathbb{P}^1$**: The genus of $\mathbb{P}^1$ is $g = 0$, and the canonical divisor is $K_{\mathbb{P}^1} = -2H$ ([§Canonical Line Bundle, ⁋Example 8](/en/math/algebraic_varieties/canonical_bundle#ex8){: data-lid="37laf" }). On the other hand, we showed in [§Line Bundles and Vector Bundles, ⁋Example 16](/en/math/algebraic_varieties/line_bundles#ex16){: data-lid="85tmq" } that the global sections of $\mathcal{O}_{\mathbb{P}^1}(d)$ are the homogeneous polynomials of degree $d$, so we know that

$$\ell(dH) = d+1 \quad (d \ge 0), \qquad \ell(dH) = 0 \quad (d < 0)$$

holds. Now checking the Riemann–Roch formula, for $D = dH$ we have $\deg D = d$ and $K_C - D = (-2-d)H$, so

$$\ell(dH) - \ell(-2H-dH) = d + 1 - 0 = d + 1$$

and we can verify that both sides agree at $d+1$.
:::

::: Example 5 (Elliptic curve)
In the genus $1$ case $g = 1$, we know from the above computations that $\deg K_C=2g-2=0$ and $\ell(K_C)=g=1$. Since $\ell(K_C)=1>0$, as noted earlier there exists an effective divisor linearly equivalent to $K_C$; but $\deg K_C=0$ and the only effective divisor of degree $0$ is $0$, so $K_C\sim 0$. Using this, if we look at Riemann–Roch again, it becomes

$$\ell(D) - \ell(-D) = \deg D$$

In particular, if $\deg D > 0$ then $\ell(-D) = 0$, so $\ell(D) = \deg D$.

The case $\deg D=0$ is the small-degree situation mentioned above; first, from inequality ($3$), we must have $\ell(D)=0$ or $\ell(D)=1$. If $\ell(D)=1$, there exists a unique effective divisor linearly equivalent to $D$, and since its degree is $0$, this is $0$. Therefore $D\sim 0$, and conversely if $D\sim 0$ then $\mathcal{O}_C(D)\cong \mathcal{O}_C$, so $\ell(D)=1$. That is, only when $D$ is linearly equivalent to $0$ does the term $\ell(K_C-D)$ become $1$, and otherwise it becomes $0$.
:::

Since $K_C \sim 0$, Riemann–Roch is especially simple on an elliptic curve. When $\deg D > 0$, the correction term $\ell(K_C-D)=\ell(-D)$ vanishes, so $\ell(D)=\deg D$ is completely determined; this shows that $g=1$ is the simplest non-trivial case in the progression where the influence of the correction term grows more intricate as the genus increases.

::: Example 6 ($g=2$)
Now let us look at the case $g=2$, which is one step more complicated. In this case, $\deg K_C = 2g - 2 = 2$ and $\ell(K_C)=2$, and substituting $D=p$ into [Proposition 3](#prop3){: data-lid="1khga" }, we obtain

$$\ell(p)-\ell(K_C-p)=2-g$$

Here, if $\ell(p)\ge 2$, there exists a degree 1 morphism $C\rightarrow\mathbb{P}^1$ so that $C\cong\mathbb{P}^1$, which contradicts $g=2$; hence $\ell(p)=1$, and since $2-g=0$ in the above equation, $\ell(K_C-p)=\ell(p)=1=\ell(K_C)-1<\ell(K_C)$. As this holds for all $p\in C$, $\lvert K_C\rvert$ is basepoint-free, and therefore the canonical map

$$\varphi_{K_C}:C\rightarrow \mathbb{P}^1$$

is well-defined. Then the preimage of a hyperplane in $\mathbb{P}^1$, that is, of a point in $\mathbb{P}^1$, is an effective divisor linearly equivalent to $K_C$, and from the fact that this is a degree $2$ map, we can write $K_C$ as a sum of two points $p_1+p_2$.

Now, for a point $p$, let us apply Riemann-Roch to its multiples $D=d\cdot p$ to see how $\ell(D)$ varies with $d$. For small $d$, that is, where $\ell(K_C-D)$ survives, a special phenomenon appears, but as $d$ grows, $\ell(D)$ stabilizes linearly.

1. The case $d=1$ was already examined above: $\ell(p)=1$, and by Riemann-Roch, $\ell(K_C-p)=1$.
2. In the case $d=2$, if $2p\sim K_C$, then $\ell(2p)=2$. In this case, $p$ is called a *Weierstrass point*; this condition corresponds exactly to the situation where the preimage of a point under the canonical map $\varphi_{K_C}$ above overlaps at $p$. At a general point, $2p\not\sim K_C$, so $\ell(2p)=1$.
3. If $d\ge 3$, then $\deg(K_C-D)=2-d<0$, so $\ell(K_C-D)=0$, and therefore $\ell(D)=d-1$.
:::

For $g=2$, the canonical map $\varphi_{K_C}: C \rightarrow \mathbb{P}^1$ examined in the example above was a 2:1 branched covering. More generally, among curves of genus $g \ge 2$, those for which there exists a degree 2 covering to $\mathbb{P}^1$ are called *hyperelliptic curves*, and otherwise they are called *non-hyperelliptic curves*. Note that by convention, the cases of genus $0,1$ are excluded from hyperelliptic curves.

Now, for $g\geq 2$, on $C$, associated with the canonical bundle $K_C$, the complete linear system $\lvert K_C\rvert$ defines a morphism $\varphi_{K_C} : C \rightarrow \mathbb{P}^{g-1}$; let us examine its properties. Since we verified above that $\deg K_C = 2g - 2$ and $h^0(K_C) = g$, the codomain of $\varphi_{K_C}$ is $\mathbb{P}^{g-1}$. However, this is not a closed embedding when $C$ is hyperelliptic; we already confirmed this from the fact that in the case $g=2$, this becomes a $2:1$ covering map. If we compute this concretely, we see that $\varphi_{K_C}$ arises as the composition of the Veronese map $\mathbb{P}^1 \hookrightarrow \mathbb{P}^{g-1}$ and the hyperelliptic covering $C\rightarrow \mathbb{P}^1$.

## Degree-genus formula

In [§Canonical Line Bundle, ⁋Example 10](/en/math/algebraic_varieties/canonical_bundle#ex10){: data-lid="ssxo8" }, we asserted the following proposition as a well-known fact in order to show that $\deg K_C=2g-2$, but now we can give a rigorous proof of it. However, this proceeds in the exact opposite direction to that example: in that example, we proved that $\deg K_C=2g-2$ using the adjunction formula and the degree-genus formula, but now we derive the degree-genus formula from the fact that $\deg K_C=2g-2$ and the adjunction formula. Note that the degree of $K_C$ was already obtained from Riemann-Roch (without using the degree-genus formula) before [Example 4](#ex4){: data-lid="2zcj4" } above.

::: Proposition 7 (Degree-genus formula)
For a degree $d$ smooth plane curve $C \subseteq \mathbb{P}^2$,

$$g(C) = \frac{(d-1)(d-2)}{2}$$

holds.
:::

::: Proof
By the adjunction formula of [§Canonical Line Bundle, ⁋Proposition 9](/en/math/algebraic_varieties/canonical_bundle#prop9){: data-lid="p82wt" }, $K_C = (K_{\mathbb{P}^2} + C)\vert_C = (d-3)H\vert_C$. Hence $\deg K_C = d(d-3)$, and substituting this into $\deg K_C = 2g - 2$ yields

$$d(d-3) = 2g - 2 \implies g = \frac{d(d-3) + 2}{2} = \frac{(d-1)(d-2)}{2}$$

:::

This formula directly computes the geometric properties of plane curves. For example, a smooth plane cubic has genus 1, so it is an elliptic curve as treated in [Example 5](#ex5){: data-lid="karg6" }. On the other hand, for $d = 1, 2$ we obtain $g = 0$, reflecting that both lines and conics are birationally equivalent to $\mathbb{P}^1$. A line is itself isomorphic to $\mathbb{P}^1$, and for a smooth conic the projection from a point on it gives a birational map between the conic and $\mathbb{P}^1$; by [§Rational Maps, ⁋Proposition 10](/en/math/algebraic_varieties/rational_maps#prop10){: data-lid="j7otg" } this is equivalent to their function fields being isomorphic.

::: Example 8
Computing the genus by degree $d$: for degree 3 (cubic) we have $g = \frac{2 \cdot 1}{2} = 1$, an elliptic curve; for degree 4 (quartic) we have $g = \frac{3 \cdot 2}{2} = 3$; and for degree 5 (quintic) we have $g = \frac{4 \cdot 3}{2} = 6$. Since the genus grows rapidly with degree, smooth plane curves of higher degree have increasingly complex topological structure.
:::

---

**References**

**[Hart]** R. Hartshorne, *Algebraic Geometry*, Graduate Texts in Mathematics, Springer, 1977.  
**[Sha]** I. R. Shafarevich, *Basic Algebraic Geometry I: Varieties in Projective Space*, Springer, 2013.

---

[^1]: This agrees with defining the Euler characteristic as the alternating sum of cohomology.
