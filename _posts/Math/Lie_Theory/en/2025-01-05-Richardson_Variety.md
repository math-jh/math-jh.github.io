---
title: "Richardson Variety"
excerpt: "The definition and basic geometric properties of Richardson varieties, defined as the intersection of Schubert varieties and opposite Schubert varieties"

categories: [Math / Lie Theory]
permalink: /en/math/lie_theory/richardson_variety
sidebar:
    nav: "Lie_theory-en"

date: 2025-01-05
last_modified_at: 2025-01-05
weight: 6
translated_at: 2026-05-28T11:36:15+00:00
translation_source: kimi-cli
published: false
---
As we saw in [§Bruhat Decomposition and Parabolic Subgroups](/en/math/lie_theory/bruhat_decomposition), the generalized flag variety $$X = G/P$$ decomposes into a disjoint union of Bruhat cells. Each Bruhat cell is an orbit of the Borel subgroup $$B$$, and its Zariski closure, the Schubert variety, forms an important closed subvariety of $$X$$. However, orbits in only one direction are often insufficient to fully describe the intersection theory or symmetry of $$X$$, and one must frequently consider the intersection of two cell structures coming from different directions. The Richardson variety is precisely the object corresponding to such an intersection, defined via the intersection of a Schubert variety and an opposite Schubert variety. In this post we examine the basic definition and properties of Richardson varieties, particularly the reason they become smooth affine varieties, from an intuitive viewpoint, and then discuss their concrete appearance in the Grassmannian.

## Opposite Borel and Opposite Bruhat Cell

We fix a connected semisimple algebraic group $$G$$ over the complex numbers $$\mathbb{C}$$, with Borel subgroup $$B$$ and maximal torus $$T = B \cap B^-$$. Here $$B^-$$ is the Borel subgroup opposite to $$B$$, that is, the **opposite Borel**. Concretely, if $$B$$ is given by upper triangular matrices, then $$B^-$$ corresponds to lower triangular matrices, and $$B \cap B^- = T$$ holds. For an element $$w$$ of the Weyl group $$W = N_G(T)/T$$, the Bruhat cell defined in [§Bruhat Decomposition, ⁋Definition 16](/en/math/lie_theory/bruhat_decomposition#def16) is the orbit of $$B$$

$$X_w^\circ = BwP/P$$

given by. Symmetrically, considering the orbit of $$B^-$$ we have the following.

<div class="definition" markdown="1">

<ins id="def1">**Definition 1**</ins> For $$w \in W$$, the set

$$X^w_\circ = B^- w P/P$$

is called the **opposite Bruhat cell**. Its Zariski closure $$\overline{X^w_\circ}$$ is called the **opposite Schubert variety**, denoted by $$X^w$$.

</div>

Since the opposite Bruhat cell $$X^w_\circ$$ is an orbit for the action of $$B^-$$ on $$X$$, it is isomorphic to an affine space, just like a Bruhat cell. In particular, the dimension of $$X^w_\circ$$ is $$\dim(G/P) - \ell(w)$$. These opposite cells provide another cell decomposition of $$X$$,

$$X = \bigsqcup_{w \in W^P} X^w_\circ,$$

which sits in a mutually transversal position with respect to the original Bruhat decomposition.

## Definition of Richardson Variety

We now consider the intersection of two cell structures in different directions, namely the $$B$$-orbit and the $$B^-$$-orbit. Given two permutations $$u, w \in W^P$$, the Schubert variety $$X_w$$ is the Zariski closure of $$X_w^\circ$$, and the opposite Schubert variety $$X^u$$ is the Zariski closure of $$X^u_\circ$$. We define their intersection as follows.

<div class="definition" markdown="1">

<ins id="def2">**Definition 2**</ins> For $$u, w \in W^P$$, the set

$$R_{u,w} = X_w \cap X^u$$

is called the **Richardson variety**. Moreover, the intersection with lower-dimensional parts removed,

$$\mathring{R}_{u,w} = X_w^\circ \cap X^u_\circ,$$

is called the **open Richardson variety**.

</div>

The Richardson variety first appeared in the work of Richardson, and subsequently plays an important role in the geometric interpretation of [§Kazhdan-Lusztig Polynomial](/en/math/lie_theory/kazhdan_lusztig) and in the $$K$$-theory of flag varieties. As can be seen from the definition, $$R_{u,w}$$ is a closed subvariety of $$X$$, and $$\mathring{R}_{u,w}$$ is a Zariski open subset of $$R_{u,w}$$.

<div class="proposition" markdown="1">

<ins id="prop3">**Proposition 3**</ins> The open Richardson variety $$\mathring{R}_{u,w}$$ is nonempty if and only if $$u \leq w$$ holds in the Bruhat order. When this condition is satisfied, $$\mathring{R}_{u,w}$$ is a smooth affine variety of dimension $$\ell(w) - \ell(u)$$, and is irreducible.

</div>
<details class="proof" markdown="1">
<summary>Proof</summary>

Since $$X_w^\circ$$ is an orbit of $$B$$ and $$X^u_\circ$$ is an orbit of $$B^-$$, both are locally closed subsets of $$X$$. By the Bruhat decomposition, $$X_w^\circ \cong \mathbb{C}^{\ell(w)}$$ and $$X^u_\circ \cong \mathbb{C}^{\dim(G/P) - \ell(u)}$$, and these belong to different cell decompositions of $$X$$. For the two cells to intersect nontrivially, the Bruhat order $$u \leq w$$ must hold between the corresponding Weyl group elements. This follows from the results of Deodhar [Deo85] and Kazhdan-Lusztig [KL80]; specifically, $$X_w^\circ \cap X^u_\circ \neq \emptyset \iff u \leq w$$, and in this case the intersection is a smooth irreducible affine variety of dimension $$\ell(w) - \ell(u)$$.

When $$u \leq w$$ holds, $$X_w^\circ$$ and $$X^u_\circ$$ meet **transversally** on $$X$$. This is because $$B$$ and $$B^-$$ provide opposite tangent directions at a point of $$X$$. Concretely, for any $$x \in \mathring{R}_{u,w}$$, the tangent space is given by

$$T_x \mathring{R}_{u,w} = T_x X_w^\circ \cap T_x X^u_\circ,$$

and by a dimension count, the dimension of this intersection is $$\ell(w) - \ell(u)$$. In particular, this dimension is nonnegative, and when $$u = w$$ it collapses to a point. From this transversality we obtain that $$\mathring{R}_{u,w}$$ is a smooth irreducible affine variety.

</details>

The essence of Proposition [Proposition 3](#prop3) is that when two different cell decompositions intersect transversally, their intersection naturally inherits good geometric properties. Although a Schubert variety itself generally has singularities, taking the intersection with an opposite Schubert variety causes the singular directions to "cancel" each other, leaving a smooth structure.

<div class="example" markdown="1">

<ins id="ex4">**Example 4**</ins> When $$u = w$$, $$\mathring{R}_{w,w} = X_w^\circ \cap X^w_\circ$$ consists of a single point. This is because $$X_w$$ and $$X^w$$ meet each other only at the single point $$wP/P$$. On the other hand, if $$u = e$$ (the identity element) and $$w = w_0^P$$ (the longest element of $$W^P$$), then $$\mathring{R}_{e, w_0^P}$$ coincides with a certain open subset of $$X$$; in this case the Richardson variety becomes the largest open cell of $$X$$.

</div>

## Concrete Appearance in the Grassmannian

Let us now examine concretely the case of the Grassmannian $$X = \operatorname{Gr}(k, n)$$. Here $$G = \operatorname{GL}_n(\mathbb{C})$$, and $$P$$ is the parabolic subgroup consisting of upper block triangular matrices of block sizes $$k$$ and $$n-k$$. The Weyl group is $$W = S_n$$, and $$W_P = S_k \times S_{n-k}$$ is the Weyl group of $$P$$. The minimal length coset representatives $$W^P \subset W$$ are the set of permutations having the shortest length in each coset $$w W_P$$.

The Schubert variety $$X_w$$ is indexed by an element $$w \in W^P$$, which can also be described in the language of Young diagrams or partitions. Likewise, the opposite Schubert variety $$X^v$$ is also indexed by $$v \in W^P$$. Their intersection, the Richardson variety $$R_{v,w}$$, becomes the object that concretely exhibits the transversal intersection of the two cell structures on the Grassmannian.

On the Grassmannian $$\operatorname{Gr}(k, n)$$, the open Richardson variety $$\mathring{R}_{v,w}$$ can be realized as a subset of an affine space with the following coordinates. The Schubert cell $$X_w^\circ$$ corresponding to $$w \in W^P$$ is described as the set of points satisfying certain rank conditions in the space of $$k \times (n-k)$$ matrices, and the opposite cell $$X^v_\circ$$ imposes additional rank conditions that are transversal to these. In the intersection $$\mathring{R}_{v,w}$$, these two conditions are satisfied simultaneously, so that some of the Plücker coordinates serve as coordinate functions.

<div class="example" markdown="1">

<ins id="ex5">**Example 5**</ins> For $$X = \operatorname{Gr}(2, 4)$$, the elements of $$W^P$$ are given by the six $$(2,2)$$-shuffles examined in [§Bruhat Decomposition and Parabolic Subgroups, ⁋Example 15](/en/math/lie_theory/bruhat_decomposition#ex15). Among these, the open Richardson variety $$\mathring{R}_{1234, 3412}$$ for $$v = 1234$$ (the identity element) and $$w = 3412$$ (the longest element) corresponds to the largest open cell of $$\operatorname{Gr}(2,4)$$, and is an affine variety of dimension $$\ell(3412) - \ell(1234) = 4$$. On the other hand, if $$v = w = 1324$$, then $$\mathring{R}_{1324, 1324}$$ consists of a single point.

</div>

Such a coordinatization allows us to treat the coordinate ring structure of the Richardson variety explicitly, and this serves as a basic starting point for subsequent $$K$$-theoretic computations or concrete descriptions of cohomology classes.

---

**References**

**[KL80]** D. Kazhdan, G. Lusztig, *Schubert varieties and Poincaré duality*, Geometry of the Laplace operator, Proc. Sympos. Pure Math. **36**, AMS, 1980.

**[Deo85]** V. V. Deodhar, *On some geometric aspects of Bruhat orderings. I. A finer decomposition of Bruhat cells*, Invent. Math. **79** (1985), 499--511.

**[Ric92]** R. W. Richardson, *Intersections of double cosets in algebraic groups*, Indag. Math. **3** (1992), 69--77.
