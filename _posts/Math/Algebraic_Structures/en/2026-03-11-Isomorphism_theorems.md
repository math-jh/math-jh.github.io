---

title: "Isomorphism Theorems"
excerpt: "The isomorphism theorems"

categories: [Math / Algebraic Structures]
permalink: /en/math/algebraic_structures/isomorphism_theorems
header:
    overlay_image: /assets/images/Math/Algebraic_Structures/Isomorphism_theorems.png
    overlay_filter: 0.5
sidebar:
    nav: "algebraic_structures-en"

date: 2026-03-11
last_modified_at: 2026-03-11
weight: 6

---

## The First Isomorphism Theorem

We begin with a simple lemma.

<div class="proposition" markdown="1">

<ins id="lem1">**Lemma 1**</ins> For any homomorphism $$f:G\rightarrow G'$$, $$\ker f$$ is a normal subgroup of $$G$$.

</div>
<details class="proof" markdown="1">
<summary>Proof</summary>

For any $$g\in G$$ and $$x\in \ker f$$,

$$f(gxg^{-1})=f(g)f(x)f(g^{-1})=f(g)e'f(g)^{-1}=f(g)f(g)^{-1}=e'.$$

</details>

Now consider the equivalence relation defined by $$\ker f$$

$$x\sim y\iff xy^{-1}\ker f$$

From the equation

$$f(y)=e'f(y)=f(xy^{-1})f(y)=f(xy^{-1}y)=f(x)$$

we see that $$x\sim y\iff f(x)=f(y)$$. That is, $$\sim$$ is nothing but the equivalence relation defined by the function $$f$$ ([\[Set Theory\] §Examples of Equivalence Relations, ⁋Definition 2](/en/math/set_theory/examples_of_equivalence#def2)), and from the definition of quotient groups, the canonical map $$p:G\rightarrow G/\ker f$$ is a homomorphism. Now considering the canonical decomposition of $$f$$, we obtain a bijection $$h:G/\ker f\rightarrow\im f$$. Then for any $$[x], [x']\in G/\ker f$$,

$$h([x][x'])=h([xx'])=f(xx')=f(x)f(x')=h([x])h([x'])$$

so $$h$$ is a homomorphism, and therefore an isomorphism.

<div class="proposition" markdown="1">

<ins id="thm2">**Theorem 2 (The First Isomorphism Theorem)**</ins> For any homomorphism $$f:G\rightarrow G'$$, $$G/\ker f\cong \im f$$ always holds.

</div>

On the other hand, using [\[Set Theory\] §Examples of Equivalence Relations, ⁋Proposition 7](/en/math/set_theory/examples_of_equivalence#prop7), we obtain the following proposition.

<div class="proposition" markdown="1">

<ins id="prop3">**Proposition 3**</ins> For any homomorphism $$f:G\rightarrow G'$$ and normal subgroup $$N$$ of $$G$$, there exists $$\bar{f}:G/N\rightarrow G'$$ satisfying $$f=\bar{f}\circ p$$ if and only if $$N\leq \ker f$$.

</div>

## The Second Isomorphism Theorem

To prove the second isomorphism theorem, we need the following lemma. In the following proposition, $$N\vee K$$ denotes the smallest subgroup of $$G$$ containing the union $$N\cup K$$, i.e., $$\langle N\cup K\rangle$$, and $$NK$$ denotes the set

$$NK=\{nk\mid n\in N,k\in K\}$$

<div class="proposition" markdown="1">

<ins id="lem4">**Lemma 4**</ins> Let $$K$$ be a subgroup of a group $$G$$ and $$N$$ a normal subgroup of $$G$$. Then the following hold.

1. $$N\cap K$$ is a normal subgroup of $$K$$.
2. $$N$$ is a normal subgroup of $$N\vee K$$.
3. $$NK=N\vee K=KN$$ holds.

</div>
<details class="proof" markdown="1">
<summary>Proof</summary>

1. For any $$n\in N\cap K$$ and $$k\in K$$, $$knk^{-1}$$ is a product of elements of $$K$$, so it is an element of $$K$$, and at the same time, since $$N$$ is a normal subgroup of $$G$$, it is an element of $$N$$. Therefore, $$knk^{-1}\in N\cap K$$.
2. It is clear that $$N$$ is a subgroup of $$N\vee K$$. Also, for any $$g\in N\vee K$$ and $$n\in N$$, $$gng^{-1}\in N$$ holds.
3. For any $$nk\in NK$$, since $$n,k\in N\vee K$$, we have $$nk\in N\vee K$$. Thus it suffices to show the reverse inclusion. Consider the subset of $$G$$ containing all products $$n_1k_1\cdots n_rk_r$$ of elements of $$N$$ and $$K$$. It is easy to verify that this set is a subgroup, and since this subgroup contains both $$N$$ and $$K$$, it also contains $$N\vee K$$.[^1]
Therefore, every element of $$N\vee K$$ can be written in the form $$n_1k_1\cdots n_rk_r$$. Now since $$N$$ is a normal subgroup of $$N\vee K$$, there exists $$n_1'\in N$$ such that $$k_1n_2=n_2'k_1$$. Repeating this process, we can rewrite $$n_1k_1\cdots n_rk_r$$ in the form of an element of $$NK$$.

</details>

<div class="proposition" markdown="1">

<ins id="thm5">**Theorem 5 (The Second Isomorphism Theorem)**</ins> Let $$K$$ be a subgroup of a group $$G$$ and $$N$$ a normal subgroup of $$G$$. Then $$K/(N\cap K)\cong NK/N$$ holds.

</div>
<details class="proof" markdown="1">
<summary>Proof</summary>

From the previous lemma, $$N$$ is a normal subgroup of $$NK=N\vee K=KN$$. On the other hand, since $$K\subset NK$$, we can consider the composition of homomorphisms

$$K\overset{\iota}{\hookrightarrow}NK\overset{\pi}{\twoheadrightarrow}NK/N$$

Then

$$\ker(\pi\iota)=(\pi\iota)^{-1}(e)=\iota^{-1}(\ker\pi)=\iota^{-1}(N)=K\cap N$$

so applying the first isomorphism theorem to $$\pi\iota$$,

$$K/\ker(\pi\iota)=K/(K\cap N)\cong\im(\pi\iota)$$

is obtained. But every element of $$NK/N$$ has the form $$nkN$$, and for some $$n'\in N$$, we can write $$nk=kn'$$, so every element $$nkN$$ of $$NK/N$$ satisfies

$$nkN=kn'N=kN=\pi(k)=\pi(\iota(k))\in\im(\pi\iota)$$

and thus we obtain the desired result.

</details>

## The Third Isomorphism Theorem

<div class="proposition" markdown="1">

<ins id="thm6">**Theorem 6 (The Third Isomorphism Theorem)**</ins> Let $$H$$ and $$K$$ be normal subgroups of a group $$G$$ with $$K<H$$. Then $$H/K$$ is a normal subgroup of $$G/K$$, and $$(G/K)/(H/K)\cong G/H$$ holds.

</div>
<details class="proof" markdown="1">
<summary>Proof</summary>

See the decomposition after [\[Set Theory\] §Examples of Equivalence Relations, ⁋Definition 8](/en/math/set_theory/examples_of_equivalence#def8).

</details>

## The Fourth Isomorphism Theorem

The following theorem is used extensively, and while its proof is not difficult, there is too much to verify, so we omit the proof.

<div class="proposition" markdown="1">

<ins id="thm7">**Theorem 7 (The Fourth Isomorphism Theorem)**</ins> Let $$G$$ be a group and $$N$$ a normal subgroup of $$G$$. Then there exists an inclusion-preserving bijection between *the set of subgroups of $$G$$ containing $$N$$* and *the set of subgroups of $$G/N$$*. Moreover, this bijection preserves relations such as intersections, indices, and normal subgroups.

</div>

## Coequalizer of Homomorphisms

Now suppose two group homomorphisms $$f,g:G \rightarrow H$$ are given. We previously saw that the equalizer $$\Eq(f,g)$$ of $$f$$ and $$g$$ is always a subgroup of $$G$$. Their coequalizer is somewhat more complicated.

First, considering the universal property of coequalizers, $$q:H\rightarrow\CoEq(f,g)$$ is initial among those satisfying $$q\circ f=q\circ g$$. If we encountered this situation in $$\Set$$, we would define an equivalence relation $$\sim$$ on $$H$$ as the relation generated by

$$f(x)\sim g(x)\qquad\text{for all $x\in G$}$$

and then the projection $$H\rightarrow H/{\sim}$$ would be the coequalizer. However, in $$\Grp$$, we do not know whether $$\sim$$ defined above is compatible with the group operation of $$H$$. That is, the subset

$$S=\{f(x)g(x)^{-1}:x\in X\}$$

is not a normal subgroup, so $$H/S$$ is not defined.

To resolve this, let $$\overline{S}$$ be the *normal closure* of $$S$$, i.e., the smallest normal subgroup containing $$S$$. Then the quotient $$H/\overline{S}$$ of $$H$$ by $$\overline{S}$$ is well-defined.

<div class="proposition" markdown="1">

<ins id="prop8">**Proposition 8**</ins> The quotient $$q: H \rightarrow H/\overline{S}$$ defined as above is a coequalizer.

</div>
<details class="proof" markdown="1">
<summary>Proof</summary>

Suppose there exists an arbitrary group homomorphism $$q': G \rightarrow H'$$ satisfying $$q'\circ f=q'\circ g$$. Then by [Lemma 1](#lem1), $$\ker q'$$ is a normal subgroup, and by the condition $$q'\circ f=q'\circ g$$,

$$q'(f(x))=q'(g(x))\iff q'(f(x)g(x)^{-1})=e$$

so $$f(x)g(x)^{-1}\in\ker q'$$ holds for all $$x\in g$$. Therefore, by the definition of $$\overline{S}$$, $$\overline{S}\leq\ker q'$$, and applying [Proposition 3](#prop3) yields the desired result.

</details>

---

**References**

**[Bou]** Bourbaki, N. Algebra I. *Elements of Mathematics*. Springer. 1998.

---

[^1]: The reverse inclusion can also be easily shown.
