---title: "Algebraic Groups"
excerpt: "Algebraic group action"

categories: [Math / Scheme Theory]
permalink: /en/math/scheme_theory/algebraic_groups
sidebar: 
    nav: "scheme_theory-en"

header:
    overlay_image: /assets/images/Math/Algebraic_Varieties/Algebraic_Groups.png
    overlay_filter: 0.5

date: 2026-03-11
last_modified_at: 2026-03-11
weight: 17
translated_at: 2026-05-28T11:36:15+00:00
translation_source: kimi-cli
---
## Algebraic Groups

We know many examples of mathematical objects acting on other objects. Algebraically, the most important example is perhaps a group acting on a vector space; geometrically, there are Lie group actions. Since algebraic geometry endows algebraic objects with geometric meaning, the action of an algebraic group appears as a form that unifies these two perspectives well. In this post, for convenience we set $$\mathbb{k}=\mathbb{C}$$ throughout.

First, the following definition is obvious.

<div class="definition" markdown="1">

<ins id="def1">**Definition 1**</ins> An *algebraic group* $$G$$ is an algebraic variety satisfying the following conditions:

1. $$G$$ has a group structure.
2. Multiplication $$m: G \times G \to G$$ and inverse $$i: G \to G$$ are both morphisms of varieties.

</div>

As with Lie groups, the most important examples are usually matrix groups.

<div class="example" markdown="1">

<ins id="ex2">**Example 2**</ins> The most basic examples are as follows:

1. The *general linear group* $$\GL(n, \mathbb{C}) = \{A \in M_{n \times n}(\mathbb{C}) \mid \det A \ne 0\}$$ has the structure of an algebraic group as an open subvariety of $$\mathbb{C}^{n\times n}$$.
2. The *special linear group* $$\SL(n, \mathbb{C}) = \{A \in \GL(n, \mathbb{C}) \mid \det A = 1\}$$ is an algebraic group as a closed subvariety of $$\GL(n, \mathbb{C})$$.
3. The two abelian groups $$\mathbb{G}_a = \mathbb{C}$$ (addition) and $$\mathbb{G}_m = \mathbb{C}^\ast$$ (multiplication) are both one-dimensional algebraic groups.

</div>

Among algebraic groups, those that play a particularly important role are, of course, *affine algebraic groups*.

<div class="definition" markdown="1">

<ins id="def3">**Definition 3**</ins> An algebraic group $$G$$ is called an *affine algebraic group* if $$G$$ is an affine variety.

</div>

## Actions of Algebraic Groups

We now define how an algebraic group acts on an algebraic variety.

<div class="definition" markdown="1">

<ins id="def4">**Definition 4**</ins> An *action* of an algebraic group $$G$$ on an algebraic variety $$X$$ is a morphism

$$\alpha: G \times X \to X$$

satisfying the following conditions:

1. $$\alpha(e, x) = x$$ for all $$x \in X$$ (identity)
2. $$\alpha(g, \alpha(h, x)) = \alpha(gh, x)$$ for all $$g, h \in G$$, $$x \in X$$ (associativity)

</div>

In principle, an algebraic group action is obtained by examining how an affine algebraic group acts on an affine variety and then gluing these together appropriately. To examine this case more closely, consider an affine algebraic group $$G = \Spec(A)$$ acting on an affine variety $$X = \Spec(B)$$. Since $$\Spec$$ is a contravariant functor, the action $$G \times X \to X$$ translates into a structure on the coordinate ring. Specifically, it provides the following data.

<div class="definition" markdown="1">

<ins id="def5">**Definition 5**</ins> For an affine algebraic group $$G = \Spec(A)$$ and an affine variety $$X = \Spec(B)$$, a *comodule structure* corresponding to an action of $$G$$ on $$X$$ is an algebra homomorphism

$$\rho: B \to B \otimes_\mathbb{C} A$$

satisfying the following conditions:

1. (Coassociativity) $$(\rho \otimes \id_A) \circ \rho = (\id_B \otimes \Delta) \circ \rho$$
2. (Counit) $$(\id_B \otimes \epsilon) \circ \rho = \id_B$$

</div>

Here $$\Delta: A \to A \otimes A$$ is the comultiplication induced from the multiplication on $$G$$, and $$\epsilon: A \to \mathbb{C}$$ is the counit induced from the identity element.

## Representations of Algebraic Groups

Just as with Lie groups, algebraic groups can be better understood through representation theory.

<div class="definition" markdown="1">

<ins id="def6">**Definition 6**</ins> A *representation* of an algebraic group $$G$$ is a finite-dimensional vector space $$V$$ and a group homomorphism

$$\rho: G \to \GL(V)$$

such that $$G \times V \to V$$ is a morphism.

</div>

Then the following definition is also the same as in Lie groups.

<div class="definition" markdown="1">

<ins id="def7">**Definition 7**</ins> The *character* $$\chi_\rho: G \to \mathbb{C}$$ of a representation $$\rho: G \to \GL(V)$$ is defined by

$$\chi_\rho(g) = \tr(\rho(g))$$

</div>

Moreover, as we see in the following proposition, representations of algebraic groups also possess both algebraic and geometric natures simultaneously.

<div class="proposition" markdown="1">

<ins id="prop8">**Proposition 8**</ins> A representation $$\rho: G \to \GL(V)$$ of an affine algebraic group $$G = \Spec(A)$$ is in one-to-one correspondence with a comodule structure $$V \to V \otimes_\mathbb{C} A$$ on $$V$$.

</div>

<details class="proof" markdown="1">
<summary>Proof</summary>

Given a representation $$\rho: G \to \GL(V)$$, this induces $$G \times V \to V$$, and by the contravariance of $$\Spec$$ we obtain $$V^\ast \to V^\ast \otimes A$$.

Conversely, given a comodule structure $$V \to V \otimes A$$, for each $$g \in G$$ we obtain $$V \to V \otimes \mathbb{C} \cong V$$ via the evaluation map $$\operatorname{ev}_g: A \to \mathbb{C}$$, and this defines a representation.

</details>

## Algebraic Tori and Weight Decomposition

Among algebraic groups, one of the objects we encounter most frequently is a torus $$T$$. We have already examined one-dimensional tori. ([Example 2](#ex2))

<div class="definition" markdown="1">

<ins id="def9">**Definition 9**</ins> An *algebraic torus* is an algebraic group isomorphic to a finite direct sum of $$\mathbb{G}_m = \mathbb{C}^\ast$$. That is, there exists an algebraic group satisfying

$$T \cong (\mathbb{C}^\ast)^n$$

for some $$n \ge 1$$.

</div>

In Lie groups, we saw that a torus decomposes into one-dimensional representations and that the information about each of these is encoded in characters. Let us do the same here.

<div class="definition" markdown="1">

<ins id="def10">**Definition 10**</ins> A *character* $$\rchi: T \to \mathbb{C}^\ast$$ of a torus $$T = (\mathbb{C}^\ast)^n$$ is defined as follows. For each coordinate $$t_i \in \mathbb{C}^\ast$$,

$$\rchi(t_1, \ldots, t_n) = t_1^{a_1} \cdots t_n^{a_n}$$

where $$a_i \in \mathbb{Z}$$ and $$a = (a_1, \ldots, a_n) \in \mathbb{Z}^n$$.

</div>

The product of two characters $$\rchi^a$$ and $$\rchi^b$$ is defined by

$$\rchi^a \cdot \rchi^b = \rchi^{a+b}$$

This corresponds to addition in $$\mathbb{Z}^n$$

$$a + b = (a_1 + b_1, \ldots, a_n + b_n)$$

The set of characters $$X^\ast(T) = \{\rchi^a \mid a \in \mathbb{Z}^n\}$$ forms an abelian group under this product, and is called the *character group* of the torus $$T$$.

It is not hard to show that $$\rchi: T \to \mathbb{C}^\ast$$ is a group homomorphism.

<div class="proposition" markdown="1">

<ins id="prop11">**Proposition 11**</ins> The coordinate ring of a torus $$T = (\mathbb{C}^\ast)^n$$ is isomorphic to the polynomial ring in the characters $$\mathbb{C}[\rchi_1^{\pm 1}, \ldots, \rchi_n^{\pm 1}]$$. Here $$\rchi_i(t_1, \ldots, t_n) = t_i$$ is the character corresponding to the $$i$$-th coordinate.

</div>

<details class="proof" markdown="1">
<summary>Proof</summary>

Since the torus $$T = (\mathbb{C}^\ast)^n$$ is the direct product of $$n$$ copies of $$\mathbb{C}^\ast$$, its coordinate ring is the tensor product of the coordinate rings of each $$\mathbb{C}^\ast$$. We know that the coordinate ring of $$\mathbb{C}^\ast = \mathbb{C} \setminus \{0\}$$ is $$\mathbb{C}[x, x^{-1}]$$. ([§Schemes, ⁋Example 10](/en/math/scheme_theory/schemes#ex10))

Therefore the coordinate ring of $$T$$ is

$$\mathbb{C}[x_1, x_1^{-1}] \otimes \cdots \otimes \mathbb{C}[x_n, x_n^{-1}] \cong \mathbb{C}[x_1, x_1^{-1}, \ldots, x_n, x_n^{-1}]$$

Each $$x_i$$ corresponds to the $$i$$-th coordinate function $$\rchi_i: T \to \mathbb{C}^\ast$$, defined by $$\rchi_i(t_1, \ldots, t_n) = t_i$$. This is exactly a character of the torus, and its inverse $$\rchi_i^{-1}$$ is likewise a character.

Therefore the coordinate ring of $$T$$ coincides with the polynomial ring generated by all the characters.

</details>

When a torus $$T$$ acts on an affine variety $$X = \Spec(A)$$, the coordinate ring $$A$$ decomposes into weight spaces.

<div class="proposition" markdown="1">

<ins id="prop12">**Proposition 12**</ins> When a torus $$T$$ acts on an affine variety $$X = \Spec(A)$$, the coordinate ring $$A$$ decomposes into weight spaces:

$$A = \bigoplus_{\rchi \in X^\ast(T)} A_\rchi$$

Here $$X^\ast(T)$$ is the character group of the torus, and each weight space $$A_\rchi$$ is defined by

$$A_\rchi = \{f \in A \mid t \cdot f = \rchi(t) f \text{ for all } t \in T\}$$

</div>

<details class="proof" markdown="1">
<summary>Proof</summary>

Given a torus action $$T \times X \to X$$, we can define an action on the coordinate ring $$A$$ by $$t \cdot f = f(t)$$. This action is linear, and each element $$f$$ of the coordinate ring can be decomposed into eigenvectors with eigenvalues. Since these eigenvalues coincide with the characters of the torus, $$A$$ decomposes as a direct sum of weight spaces.

</details>

## Quotient Varieties

On an algebraic variety with a given action, we often wish to construct a *quotient variety*. However, such objects are well defined primarily in algebraic settings; even for topological spaces, the simplest geometric objects, this is not always well defined. The same is true in the world of algebraic varieties.

<div class="definition" markdown="1">

<ins id="def13">**Definition 13**</ins> When an algebraic group $$G$$ acts on an algebraic variety $$X$$, we define the following.

- *Orbit*: $$G \cdot x = \{g \cdot x \mid g \in G\} \subseteq X$$
- *Stabilizer*: $$G_x = \{g \in G \mid g \cdot x = x\} \le G$$
- *Fixed point set*: $$X^G = \{x \in X \mid g \cdot x = x \text{ for all } g \in G\}$$

</div>

To construct a quotient, we must examine $$G$$-invariant functions.

<div class="definition" markdown="1">

<ins id="def14">**Definition 14**</ins> When an affine algebraic group $$G$$ acts on an affine variety $$X = \Spec(A)$$, the *invariant ring* $$A^G$$ with respect to the corresponding comodule structure $$\rho: A \to A \otimes_\mathbb{C} \mathbb{C}[G]$$ is defined by

$$A^G = \{a \in A \mid \rho(a) = a \otimes 1\}$$

This is a subalgebra of $$A$$.

</div>

The elements of the invariant ring capture the symmetries that are unchanged by the group action. If we regard elements of the coordinate ring $$A$$ as functions on $$\Spec A$$, then geometrically the elements of $$A^G$$ become constant functions on each orbit. Therefore the space $$\Spec(A^G)$$ constructed from them can be thought of as a good approximation to the orbit space $$X/G$$. However, the problem is that $$A^G$$ may not behave well algebraically.

<div class="definition" markdown="1">

<ins id="def15">**Definition 15**</ins> An affine algebraic group $$G$$ is called *reductive* if every finite-dimensional representation of $$G$$ is completely reducible. That is, any representation $$V$$ decomposes as a direct sum of irreducible representations.

</div>

If $$G$$ is a reductive group, then by the Hilbert basis theorem and Nagata's theorem one can show that the invariant ring $$A^G$$ is always finitely generated, and hence $$\Spec(A^G)$$ becomes a well-defined affine variety.

<div class="example" markdown="1">

<ins id="ex16">**Example 16**</ins> Most algebraic groups we deal with are reductive.

1. The *algebraic torus* $$(\mathbb{C}^\ast)^n$$ is reductive.
2. The *general linear group* $$\GL(n, \mathbb{C})$$ is reductive.
3. The *special linear group* $$\SL(n, \mathbb{C})$$ is reductive.
4. The *orthogonal group* and *unitary group* $$\operatorname{O}(n)$$, $$\operatorname{U}(n)$$, etc., are also reductive.

By contrast, $$\mathbb{G}_a = \mathbb{C}$$ is not reductive.

</div>

The content regarding the finite generation of $$A^G$$ mentioned after [Definition 15](#def15) is usually discussed in Geometric Invariant Theory (GIT), and through this we can define the quotient for a reductive group action.

<div class="definition" markdown="1">

<ins id="def17">**Definition 17**</ins> When a reductive group $$G$$ acts on an affine variety $$X = \Spec(A)$$, the *GIT quotient* $$X /\!/ G$$ is defined by

$$X /\!/ G = \Spec(A^G)$$

</div>

As examined above, the GIT quotient $$X /\!/ G$$ is geometrically a good approximation to the orbit space $$X/G$$; this means that the GIT quotient satisfies the universal property that a quotient should satisfy.

The discussion so far has been for affine varieties, and the situation is more complicated for projective varieties. For example, suppose $$\mathbb{C}^\ast$$ acts on $$\mathbb{P}^1 = \{[x:y]\}$$ by

$$t \cdot [x:y] = [tx:y]$$

In the homogeneous coordinate ring $$\mathbb{C}[x,y]$$, if $$t$$ acts by scaling $$x$$ by $$t$$ and $$y$$ by $$1$$, then in the degree $$d$$ component $$\mathbb{C}_d[x,y]$$ the monomial $$x^a y^{d-a}$$ is acted on by $$t$$ as $$t^a$$. That is, each monomial has a different weight.

In this case the only $$G$$-invariant subspace of $$\mathbb{C}_d[x,y]$$ is $$y^d$$, and $$A_d^G = \mathbb{C} \cdot y^d$$ is well defined. However, for an action on a general projective variety, if the action does not extend to all of $$\mathbb{P}^n$$, the grading and the action may not be compatible and $$A_d^G$$ may not be well defined.

<div class="definition" markdown="1">

<ins id="def18">**Definition 18**</ins> A *linearization* of an action of a reductive group $$G$$ on a projective variety $$X$$ is an extension of the action to an action of $$G$$ on $$\mathbb{P}^n$$ satisfying the following:

1. $$X \subseteq \mathbb{P}^n$$ is $$G$$-invariant
2. The $$G$$-action on $$\mathbb{P}^n$$ is linear (that is, it lifts to $$\GL(n+1, \mathbb{C})$$)

</div>

Linearization resolves this problem. A linear action preserves each degree $$d$$ component $$A_d$$ of the homogeneous coordinate ring, so $$G$$ acts well on $$A_d$$ and therefore we can form $$A_d^G$$. In the example above, the action is already linear, $$A_d^G = \mathbb{C} \cdot y^d$$, and we can construct the quotient as

$$\mathbb{P}^1 /\!/ \mathbb{C}^\ast = \Proj\left(\bigoplus_{d \ge 0} \mathbb{C} \cdot y^d\right) = \{[1]\} \cong \mathrm{pt}$$

Once a linearization is given, we can define *stable* and *semistable* points.

<div class="definition" markdown="1">

<ins id="def19">**Definition 19**</ins> For a $$G$$-action on $$X \subseteq \mathbb{P}^n$$ with a given linearization:

- A point $$x \in X$$ is *semistable* if there exists a non-constant $$G$$-invariant homogeneous polynomial $$f$$ such that $$f(x) \ne 0$$.
- A point $$x \in X$$ is *stable* if it satisfies the following conditions:
  1. $$x$$ is semistable
  2. $$G_x$$ is a finite group
  3. The orbit $$G \cdot x$$ is a closed set

We denote the set of semistable points by $$X^{\mathrm{ss}}$$ and the set of stable points by $$X^{\mathrm{s}}$$.

</div>

<div class="definition" markdown="1">

<ins id="def20">**Definition 20**</ins> The *GIT quotient* for a $$G$$-action on a projective variety $$X$$ with a given linearization is defined by

$$X /\!/ G = \Proj\left(\bigoplus_{d \ge 0} A_d^G\right)$$

Here $$A_d$$ is the degree $$d$$ component of the homogeneous coordinate ring of $$X$$.

</div>

Just as in the affine case discussed above, the GIT quotient of a projective variety is also a sufficiently good approximation. Moreover, in this case $$X/\!/G$$ can be regarded as a compactification of the orbit space of semistable points.

---

**References**

**[Spr]** T. A. Springer, *Linear Algebraic Groups*, Birkhäuser, 1998.  
**[Hum]** J. E. Humphreys, *Linear Algebraic Groups*, Springer, 1975.  
**[Mil]** J. S. Milne, *Algebraic Groups*, Cambridge University Press, 2017.  
**[MFK]** D. Mumford, J. Fogarty, F. Kirwan, *Geometric Invariant Theory*, Springer, 1994.
