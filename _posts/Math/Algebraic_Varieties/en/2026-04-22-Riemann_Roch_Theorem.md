---
title: "The Riemann–Roch Theorem for Curves"
excerpt: "The Riemann–Roch theorem for curves"

categories: [Math / Algebraic Varieties]
permalink: /en/math/algebraic_varieties/riemann_roch_theorem
sidebar:
    nav: "algebraic_varieties-en"

header:
    overlay_image: /assets/images/Math/Algebraic_Varieties/Riemann_Roch.png
    overlay_filter: 0.5

date: 2026-04-22
last_modified_at: 2026-05-04
weight: 15
translated_at: 2026-05-25T03:30:01+00:00
translation_source: kimi-cli
---
We now examine the complete linear system $$H^0(X, \mathcal{L})$$ of a line bundle $$\mathcal{L}$$, which we saw in [§Linear Systems, ⁋Definition 2](/en/math/algebraic_varieties/linear_systems#def2), in greater detail. We could have introduced this right after defining linear systems, but the proof requires Serre duality, so we postponed it.

## The Riemann–Roch Theorem

<div class="definition" markdown="1">

<ins id="def1">**Definition 1**</ins> For a divisor $$D$$ on a smooth projective curve $$C$$, we define the *Riemann–Roch dimension* as

$$\ell(D) = \dim H^0(C, \mathcal{O}_C(D)).$$

</div>

In general, we think of $$\mathcal{O}_X(D)$$ as the sheaf of rational functions that may have poles of order $$1$$ along $$D$$, so from this perspective $$H^0(C, \mathcal{O}_C(D))$$ can be regarded as a space of functions defined on $$X$$.

Recall that this space $$H^0(C, \mathcal{O}_C(D))$$ was first introduced in [§Linear Systems, ⁋Definition 2](/en/math/algebraic_varieties/linear_systems#def2). According to that definition, the space $$H^0(C, \mathcal{O}_C(D))$$ is the collection of divisors linearly equivalent to a given divisor $$D$$, and by projectivizing it we obtained the *complete linear system* $$\lvert \mathcal{O}_X(D)\rvert$$ of $$\mathcal{O}_C(D)$$. In this post, for convenience, we write this as $$\lvert D\rvert$$. Then the Riemann–Roch dimension above is one more than the projective dimension of $$\lvert D\rvert$$.

Now fix a point $$p\in C$$. Then the elements of $$\lvert D\rvert$$ passing through $$p$$ can be thought of, by definition, as the sections $$s$$ among the elements of $$H^0(C,\mathcal{O}_C(D))$$ satisfying $$s(p)=0$$. That is, such an $$s$$ is an element of $$H^0(C, \mathcal{O}_C(D))$$ satisfying $$\divisor(s)-p\geq 0$$, and through this we can verify that the collection of exactly these elements is precisely the global sections of

$$\mathcal{O}_C(D-p)\cong \mathcal{O}_C(D)\otimes \mathcal{O}_C(-p).$$

Therefore, if equality holds in $$H^0(C,\mathcal{O}_C(D-p))\subseteq H^0(C, \mathcal{O}_C(D))$$, this means that every element of $$\lvert D\rvert$$ passes through $$p$$, so $$p$$ becomes a base point of $$\lvert D\rvert$$. On the other hand, if $$\lvert D\rvert$$ is basepoint-free, then in [§Linear Systems](/en/math/algebraic_varieties/linear_systems) we used this to define a regular map $$\varphi_D:C\rightarrow \mathbb{P}^{\ell(D)-1}$$; from this perspective, the difference between $$\ell(D)$$ and $$\ell(D-p)$$ can be viewed as a correction term that the point $$p$$ imposes on the divisor $$D$$.

The Riemann–Roch theorem, which we will study in this post and the next, extends this idea in a certain sense: the canonical class $$K_C$$ plays a global role replacing that of the point $$p$$. Specifically, the formula we aim to prove is

$$\ell(D)-\ell(K_C-D)=\deg D+1-g,$$

where $$\deg D+1$$ is the expected value, $$g$$ is the loss coming from topological data of the curve, and $$\ell(K_C-D)$$ is a correction term arising from the positional relationship between the canonical class and $$D$$.

To see this, we first apply Serre duality to obtain

$$H^1(C, \mathcal{O}_C(D)) \cong H^0(C, \omega_C \otimes \mathcal{O}_C(-D))^\vee = H^0(C, \mathcal{O}_C(K_C - D))^\vee\tag{$1$}$$

([§Serre Duality, ⁋Proposition 2](/en/math/algebraic_varieties/serre_duality#prop2)). Recall here that the canonical divisor $$K_C$$ was the divisor corresponding to the canonical line bundle. Then by the following lemma, we can deduce that the terms appearing in the Euler characteristic of $$\mathcal{O}_C(D)$$ are only two. In this post we assume that $$\mathbb{K}$$ is an *infinite* field.

<div class="proposition" markdown="1">

<ins id="lem2">**Lemma 2**</ins> For any coherent sheaf $$\mathcal{F}$$ on a smooth projective curve $$C$$,

$$H^i(C, \mathcal{F}) = 0 \quad (i \ge 2)$$

holds.

</div>
<details class="proof" markdown="1">
<summary>Proof</summary>

Fix an embedding $$C\hookrightarrow \mathbb{P}^N$$. Then by a dimension count, there exist hyperplanes $$H_1,H_2$$ such that $$C\cap H_1\cap H_2=\emptyset$$. Thus, setting $$U_i=C\setminus H_i$$, we know that these form an affine open cover of $$C$$.

Now consider the Čech cohomology with respect to $$\{U_1,U_2\}$$. As briefly introduced right after [§Sheaf Cohomology, ⁋Proposition 12](/en/math/algebraic_varieties/sheaf_cohomology#prop12), any affine open cover of a projective variety satisfies the hypotheses of [§Sheaf Cohomology, ⁋Theorem 11](/en/math/algebraic_varieties/sheaf_cohomology#thm11), and therefore the sheaf cohomology we seek reduces exactly to the computation with respect to this affine open cover. Now the Čech complex is simply

$$\check{C}(\mathcal{U}, \mathcal{F}):\qquad \mathcal{F}(U_1)\oplus \mathcal{F}(U_2)\rightarrow \mathcal{F}(U_1\cap U_2)\rightarrow 0,$$

a complex of length 1, so $$\check{H}^i = 0\ (i \ge 2)$$ follows immediately.

</details>

Therefore, by this result, for any divisor $$D$$,

$$\rchi(\mathcal{O}_C(D)) = h^0(C, \mathcal{O}_C(D)) - h^1(C, \mathcal{O}_C(D))\tag{$2$}$$

holds. Here $$h^i$$ is shorthand for the dimension of $$H^i$$.

On the other hand, from a topological perspective we are well aware that the Euler characteristic of a genus $$g$$ compact Riemann surface $$S$$ is given by

$$\rchi(S)=2(1-g).$$

Here the Euler characteristic can be thought of using a triangulation as $$V-E+F$$ with vertex count $$V$$, edge count $$E$$, and face count $$F$$[^1], or it can be regarded as defined via differential-geometric tools such as the Gauss–Bonnet theorem.

In algebraic geometry we generally think of the underlying field $$\mathbb{K}$$ as the complex numbers, so the genus $$g$$ compact Riemann surface above is nothing but a one-dimensional curve $$C_S$$ from the algebraic-geometric viewpoint. Then the algebraic-geometric Euler characteristic is given by substituting $$D=0$$ into the formula ($$2$$) above:

$$\rchi(\mathcal{O}_{C_S})=h^0(C_S, \mathcal{O}_{C_S})-h^1(C_S, \mathcal{O}_{C_S}).$$

Meanwhile, just as one-dimensional holes appear via $$H^1$$ in topology, the one-dimensional holes in algebraic geometry—that is, the genus which is a two-dimensional hole from the topological perspective—are defined by $$g=h^1(C_S, \mathcal{O}_{C_S})$$, and since global sections are only constant functions, the Euler characteristic of $$C_S$$ is expressed as

$$\rchi(\mathcal{O}_{C_S})=h^0(C_S, \mathcal{O}_{C_S})-h^1(C_S, \mathcal{O}_{C_S})=1-g.$$

That this value is half of the topological Euler characteristic is no coincidence, and can be verified via Hodge theory, but this is irrelevant to our goal so we skip it for now. What is important is that the algebraic-geometric Euler characteristic and the value $$1-g$$ obtained when computing it for a curve are not arbitrary but a reinterpretation of the topological result.

The Riemann–Roch theorem, the subject of this post, adds one more step to this. The above computation was for the trivial sheaf $$\mathcal{O}_{C_S}$$ with nothing attached, so we consider the sheaf $$\mathcal{O}_{C_S}(D)$$ twisted by an arbitrary divisor $$D$$. Then the result of the Riemann–Roch theorem is that a correction term of size $$\deg D$$ appears.

<div class="proposition" markdown="1">

<ins id="prop3">**Proposition 3**</ins> (Riemann–Roch for curves) For a divisor $$D$$ on a smooth projective curve $$C$$,

$$\ell(D) - \ell(K_C - D) = \deg D + 1 - g$$

holds. Here $$g$$ is the genus of $$C$$, and $$K_C$$ is the canonical divisor.

</div>

<details class="proof" markdown="1">
<summary>Proof</summary>

By the above computations and definitions,

$$\rchi(\mathcal{O}_C(D)) = h^0(C, \mathcal{O}_C(D)) - h^1(C, \mathcal{O}_C(D)) = \ell(D) - \ell(K_C - D).$$

On the other hand, for an effective divisor $$D$$ there is a short exact sequence

$$0 \to \mathcal{O}_C \to \mathcal{O}_C(D) \to \mathcal{O}_D \to 0,$$

and then by additivity of the Euler characteristic, $$\rchi(\mathcal{O}_C(D)) = \rchi(\mathcal{O}_C) + \rchi(\mathcal{O}_D)$$.

Here $$\mathcal{O}_D$$ is a skyscraper sheaf of degree $$\deg D$$, so $$\rchi(\mathcal{O}_D) = \deg D$$, and as we saw above $$\rchi(\mathcal{O}_C)=1-g$$, so combining this with the previous formula yields the desired result. For a general (not necessarily effective) divisor, one expresses $$D$$ as a difference of effective divisors and applies the same additivity argument.

</details>

The above proof is clean, but its geometric content is compressed inside the Euler characteristic, so it may not be very intuitive. To remedy this, let us read the equation term by term. First, by definition

$$\ell(D) = \dim H^0(C, \mathcal{O}_C(D)),$$

and geometrically the space on the right-hand side is the collection of meromorphic functions satisfying

$$\divisor(f)+D\geq 0.$$

That is, $$D$$ forces the poles of $$f$$ to occur only within the support of $$D$$, and the order of the pole at each point $$p$$ is at most $$\operatorname{ord}_p D$$; thus as $$\deg D$$ grows, the allowed pole orders increase and so $$\ell(D)$$ grows.

Moreover, since in our situation $$C$$ is one-dimensional, an (effective) divisor is of the form $$D=\sum n_i p_i$$, and using this we can more quantitatively obtain the following inequality:

$$\ell(D)\leq \deg(D)+1\tag{$3$}$$

Specifically, if $$D = \sum n_i p_i$$ is effective, we can consider the linear map sending $$f\in H^0(C, \mathcal{O}_C(D))$$ to its principal part at each point $$p_i$$:

$$H^0(C, \mathcal{O}_C(D)) \longrightarrow \bigoplus_i \mathbb{K}^{n_i}\tag{$4$}$$

Intuitively, this is the map that, when $$f$$ is expressed by its principal part of the Laurent polynomial at the point $$p_i$$ as

$$\frac{a_{-n_i}}{(x-p_i)^{n_i}}+\frac{a_{-n_i-1}}{(x-p_i)^{n_i-1}}+\cdots +\frac{a_{-1}}{x-p_i},$$

sends

$$f\mapsto (a_{-n_i}, \ldots, a_{-1})$$

considered all at once for all $$p_i$$. Then the dimension of the target of the above linear map is $$\sum n_i = \deg D$$, and the kernel of this map is the global sections without poles, i.e. $$H^0(C, \mathcal{O}_C) = \mathbb{K}$$, from which we obtain $$\ell(D) \leq 1 + \deg D$$. If $$D$$ is not effective but $$\ell(D) > 0$$, then $$D$$ is linearly equivalent to some effective divisor, so the same inequality holds.

In general, for this inequality to become an equality the linear map must be surjective, but this does not always hold. To verify this, consider the long exact sequence obtained from the short exact sequence we examined in the proof of [Proposition 2](#prop2):

$$0\longrightarrow H^0(C,\mathcal{O}_C)\overset{i^\ast}{\longrightarrow} H^0(C,\mathcal{O}_C(D)) \overset{p^\ast}{\longrightarrow} H^0(C,\mathcal{O}_D) \overset{\delta}{\longrightarrow} H^1(C,\mathcal{O}_C)\overset{i^\ast}{\longrightarrow} H^1(C,\mathcal{O}_C(D))\to 0.$$

Here $$C$$ is a curve and $$D=\sum n_i p_i$$, so $$\mathcal{O}_D$$ is a skyscraper sheaf of degree $$D$$ with support $$\lvert D\rvert$$, and from this we know $$H^0(C, \mathcal{O}_C)=\bigoplus_i \mathbb{K}^{n_i}$$. Moreover, we know that the linear map ($$4$$) examined above actually coincides with $$p^\ast$$ in this long exact sequence, and from this the cokernel of $$p^\ast$$ can be computed by the following chain of isomorphisms:

$$\coker p^\ast=\frac{H^0(C, \mathcal{O}_D)}{\im p^\ast}=\frac{H^0(C, \mathcal{O}_D)}{\ker\delta}\cong \im\delta\cong\ker i^\ast,$$

and in particular its dimension is

$$\dim\coker p^\ast =\dim \ker (i^\ast: H^1(C,\mathcal{O}_C)\twoheadrightarrow H^1(C,\mathcal{O}_C(D)))=\dim H^1(C,\mathcal{O}_C)-\dim H^1(C,\mathcal{O}_C(D)).$$

If we apply formula (1) here, we know that

$$\dim\coker p^\ast=\dim H^1(C,\mathcal{O}_C)-\dim H^0(C,\mathcal{O}_C(K_C-D))^\vee=g-\ell(K_C-D).$$

From inequality ($$3$$), the difference between $$\deg(D)+1$$ and $$\ell(D)$$ is precisely the dimension of the cokernel, so these computations recover the result of [Proposition 3](#prop3). In other words, $$\ell(K_C-D)$$ measures how far $$\ell(D)$$ falls from its upper bound $$\deg D+1$$; this was originally a counting problem for $$1$$-forms vanishing along $$D$$, but we rewrote it as $$\ell(K_C-D)$$ using Serre duality.

As an example, consider the case where the degree of $$D$$ is very large so that $$\deg(K_C-D)<0$$. Then in this case $$\ell(K_C-D)=0$$, and therefore the Riemann–Roch theorem gives the formula

$$\ell(D)=\deg D+1-g.$$

That is, as the genus grows, the space created by a divisor of the same degree becomes smaller. However, in the general case the influence of $$\ell(K_C-D)$$ is added to this, and what one must be careful about here is that the term $$\ell(K_C-D)$$ can vary depending not only on the degree of $$D$$ but also on what relationship $$D$$ has with the canonical class $$K_C$$.

As another special example, substituting $$D=0$$ gives

$$\ell(0)-\ell(K_C)=\deg D+1-g,$$

and since $$\deg D=0$$ and $$\ell(0)=1$$, we find that $$\ell(K_C)=g$$. Now substituting $$D=K_C$$ gives

$$\ell(K_C)-\ell(0)=\deg K_C +1-g,$$

and from this we can recover the computation $$\deg(K_C)=2g-2$$ from [§Canonical Bundle, ⁋Example 10](/en/math/algebraic_varieties/canonical_bundle#ex10). In that example the degree-genus formula was mentioned as a well-known formula and $$\deg(K_C)$$ was obtained from it (and historically this is more justified), but shortly we will see in [Proposition 7](#prop7) that the degree-genus formula is a special case of the Riemann–Roch theorem.

In any case, summarizing the computations so far, we can think of $$\ell(D)$$ as the dimension of the complete linear system of $$D$$, $$\ell(K_C - D)$$ as a correction term that $$K_C$$ imposes on $$D$$, which disappears for large degree and reflects geometric information of $$K_C$$ for small degree.

<div class="example" markdown="1">

<ins id="ex4">**Example 4**</ins> **$$\mathbb{P}^1$$**: The genus of $$\mathbb{P}^1$$ is $$g = 0$$, and the canonical divisor is $$K_{\mathbb{P}^1} = -2H$$ ([§Canonical Bundle, ⁋Example 8](/en/math/algebraic_varieties/canonical_bundle#ex8)). On the other hand, in ([§Line Bundles and Vector Bundles, ⁋Example 12](/en/math/algebraic_varieties/line_bundles#ex12)) we showed that the global sections of $$\mathcal{O}_{\mathbb{P}^1}(d)$$ are the homogeneous polynomials of degree $$d$$, so we know that

$$\ell(dH) = d+1 \quad (d \ge 0), \qquad \ell(dH) = 0 \quad (d < 0)$$

holds. Now verifying the Riemann–Roch formula, for $$D = dH$$ we have $$\deg D = d$$ and $$K_C - D = (-2-d)H$$, so

$$\ell(dH) - \ell(-2H-dH) = d + 1 - 0 = d + 1,$$

and we can check that both sides agree at $$d+1$$.

</div>

<div class="example" markdown="1">

<ins id="ex5">**Example 5 (Elliptic curve)**</ins> In the genus $$1$$ case $$g = 1$$, we know from the above computations that $$\deg K_C=2g-2=0$$ and $$\ell(K_C)=g=1$$. Since $$\ell(K_C)=1>0$$, as we saw earlier there exists an effective divisor linearly equivalent to $$K_C$$, but since $$\deg K_C=0$$ and the only effective divisor of degree $$0$$ is $$0$$, we have $$K_C\sim 0$$. Using this, the Riemann–Roch formula becomes

$$\ell(D) - \ell(-D) = \deg D.$$

In particular, if $$\deg D > 0$$ then $$\ell(-D) = 0$$, so $$\ell(D) = \deg D$$.

The case $$\deg D=0$$ is the small-degree case mentioned above: first, from inequality ($$3$$) we must have $$\ell(D)=0$$ or $$\ell(D)=1$$. If $$\ell(D)=1$$, then there exists a unique effective divisor linearly equivalent to $$D$$, but its degree is $$0$$ so it is $$0$$. Therefore $$D\sim 0$$, and conversely if $$D\sim 0$$ then $$\mathcal{O}_C(D)\cong \mathcal{O}_C$$, so $$\ell(D)=1$$. That is, the term $$\ell(K_C-D)$$ becomes $$1$$ only when $$D$$ is linearly equivalent to $$0$$, and is $$0$$ otherwise.

</div>

Since $$K_C \sim 0$$, the Riemann–Roch theorem becomes especially simple on an elliptic curve. If $$\deg D > 0$$ the correction term $$\ell(K_C-D)=\ell(-D)$$ vanishes, so $$\ell(D)=\deg D$$ is completely determined, which shows that $$g=1$$ is the simplest non-trivial case in the process where the influence of the correction term becomes more complicated as the genus grows.

<div class="example" markdown="1">

<ins id="ex6">**Example 6 ($$g=2$$)**</ins> Now let us look at the one-step more complicated situation of $$g=2$$. In this case $$\deg K_C = 2g - 2 = 2$$ and $$\ell(K_C)=2$$, and substituting $$D=p$$ into [Proposition 3](#prop3) gives

$$\ell(p)-\ell(K_C-p)=2-g,$$

so since $$\ell(K_C-p)=\ell(K_C)-1<\ell(K_C)$$, the canonical map

$$\varphi_{K_C}:C\rightarrow \mathbb{P}^1$$

is well defined. Then a hyperplane in $$\mathbb{P}^1$$, that is, the preimage of a point in $$\mathbb{P}^1$$, becomes an effective divisor linearly equivalent to $$K_C$$, and from the fact that this is a degree $$2$$ map we can write $$K_C$$ as a sum of two points $$p_1+p_2$$.

Now let us apply Riemann–Roch to multiples $$D=d\cdot p$$ of a single point $$p$$ and examine how $$\ell(D)$$ varies with $$d$$. For small $$d$$, that is, where $$\ell(K_C-D)$$ is still alive, special phenomena appear, but as $$d$$ grows, $$\ell(D)$$ stabilizes linearly.

1. For $$d=1$$, if $$\ell(p)\ge 2$$ then a degree 1 map $$C\to\mathbb{P}^1$$ would exist, implying $$C\cong\mathbb{P}^1$$, which contradicts $$g=2$$; hence $$\ell(p)=1$$. By Riemann–Roch, $$\ell(K_C-p)=1$$.
2. For $$d=2$$, if $$2p\sim K_C$$ then $$\ell(2p)=2$$. In this case $$p$$ is called a *Weierstrass point*; this condition corresponds exactly to the situation where the preimage of some point under the canonical map $$\varphi_{K_C}$$ is doubled at $$p$$. For a generic point $$2p\not\sim K_C$$, so $$\ell(2p)=1$$.
3. For $$d\ge 3$$, we have $$\deg(K_C-D)=2-d<0$$, so $$\ell(K_C-D)=0$$, and therefore $$\ell(D)=d-1$$.

</div>

The canonical map $$\varphi_{K_C}: C \rightarrow \mathbb{P}^1$$ for $$g=2$$ that we examined in the above example was a 2:1 branched covering. More generally, among curves of genus $$g \ge 2$$, those for which a degree 2 covering to $$\mathbb{P}^1$$ exists are called *hyperelliptic curves*, and those for which no such covering exists are called *non-hyperelliptic curves*. Note that by convention the cases of genus $$0,1$$ are excluded from hyperelliptic curves.

Now let us examine the behavior of the morphism $$\varphi_{K_C} : C \rightarrow \mathbb{P}^{g-1}$$ defined by the complete linear system $$\lvert K_C\rvert$$ of the canonical bundle $$K_C$$ on a curve $$C$$ with $$g\geq 2$$. We verified above that $$\deg K_C = 2g - 2$$ and $$h^0(K_C) = g$$, so the codomain of $$\varphi_{K_C}$$ is $$\mathbb{P}^{g-1}$$. However, this is generally not a closed embedding, which we already confirmed in the $$g=2$$ case where it becomes a $$2:1$$ covering map. Computing this concretely, one finds that $$\varphi_{K_C}$$ arises as the composition of the Veronese map $$\mathbb{P}^1 \hookrightarrow \mathbb{P}^{g-1}$$ and the hyperelliptic covering $$C\rightarrow \mathbb{P}^1$$.

## Degree-genus formula

In [§Canonical Bundle, ⁋Example 10](/en/math/algebraic_varieties/canonical_bundle#ex10) we asserted the following proposition as a well-known fact to show that $$\deg K_C=2g-2$$, but now we can give a rigorous proof. Note, however, that this is exactly the opposite of that example: there the adjunction formula and degree-genus formula were used to prove $$\deg K_C=2g-2$$, whereas now we derive the degree-genus formula from the fact that $$\deg K_C=2g-2$$ and the adjunction formula. Note that the degree of $$K_C$$ was already obtained from Riemann–Roch before [Example 4](#ex4) (without using the degree-genus formula).

<div class="proposition" markdown="1">

<ins id="prop7">**Proposition 7 (Degree-genus formula)**</ins> For a smooth plane curve $$C \subset \mathbb{P}^2$$ of degree $$d$$,

$$g(C) = \frac{(d-1)(d-2)}{2}$$

holds.

</div>

<details class="proof" markdown="1">
<summary>Proof</summary>

By the adjunction formula ([§Canonical Bundle, ⁋Proposition 9](/en/math/algebraic_varieties/canonical_bundle#prop9)), $$K_C = (K_{\mathbb{P}^2} + C)\vert_C = (d-3)H\vert_C$$. Therefore $$\deg K_C = d(d-3)$$, and substituting this into $$\deg K_C = 2g - 2$$ yields

$$d(d-3) = 2g - 2 \implies g = \frac{d(d-3) + 2}{2} = \frac{(d-1)(d-2)}{2}.$$

</details>

This formula directly computes the geometric properties of plane curves. For example, the genus of a smooth plane cubic is 1, so it is the same as the elliptic curve treated in [Example 5](#ex5). On the other hand, for $$d = 1, 2$$ we have $$g = 0$$, reflecting that lines and conics are both birationally equivalent to $$\mathbb{P}^1$$ ([§Rational Maps, ⁋Proposition 10](/en/math/algebraic_varieties/rational_maps#prop10)).

<div class="example" markdown="1">

<ins id="ex8">**Example 8**</ins> Computing the genus according to degree $$d$$, for degree 3 (cubic) we have $$g = \frac{2 \cdot 1}{2} = 1$$, an elliptic curve; for degree 4 (quartic) we have $$g = \frac{3 \cdot 2}{2} = 3$$, and for degree 5 (quintic) we have $$g = \frac{4 \cdot 3}{2} = 6$$. Since the genus grows rapidly with degree, higher-dimensional smooth plane curves have increasingly complex topological structure.

</div>

---

**References**

**[Hart]** R. Hartshorne, *Algebraic Geometry*, Graduate Texts in Mathematics, Springer, 1977.
**[Sha]** I. R. Shafarevich, *Basic Algebraic Geometry I: Varieties in Projective Space*, Springer, 2013.

---

[^1]: This coincides with defining the Euler characteristic as the alternating sum of cohomology.
