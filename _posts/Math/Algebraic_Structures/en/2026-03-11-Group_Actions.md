---

title: "Group Actions"
excerpt: "Group action"

categories: [Math / Algebraic Structures]
permalink: /en/math/algebraic_structures/group_actions
header:
    overlay_image: /assets/images/Math/Algebraic_Structures/Group_actions.png
    overlay_filter: 0.5
sidebar: 
    nav: "algebraic_structures-en"

date: 2026-03-11
last_modified_at: 2026-03-11
weight: 11

---

When dealing with complex algebraic structures, one effective strategy is to examine how a given algebraic object acts on another algebraic object, rather than analyzing the structure directly. We are particularly interested in group actions, but as always, we begin by considering the more general case of a monoid acting on a set.

## Monoids Acting on Sets

<div class="definition" markdown="1">

<ins id="def1">**Definition 1**</ins> Fix a monoidal category $$(\mathcal{A},\otimes, I)$$ and a monoid object $$(A,\cdot, 1)$$ in $$\mathcal{A}$$. A morphism $$\rho: A\otimes E\rightarrow E$$ is called a *left action* of $$A$$ on an object $$E\in\obj(\mathcal{A})$$ if the following two diagrams commute.

![left_module](/assets/images/Math/Algebraic_Structures/Modules-1.png){:style="width:30em" class="invert" .align-center}

Here, $$I\otimes E \rightarrow E$$ is the left unitor. We denote this situation by $$A\circlearrowright E$$.

Similarly, a morphism $$\rho: E\otimes A\rightarrow E$$ is called a *right action* of $$A$$ on an object $$E\in\obj(\mathcal{A})$$ if the following two diagrams commute.

![right_module](/assets/images/Math/Algebraic_Structures/Modules-2.png){:style="width:30em" class="invert" .align-center}

Again, $$E\otimes I \rightarrow E$$ is the right unitor. We denote this situation by $$E \circlearrowleft A$$.

</div>

Fix a monoid object $$(M,\cdot,1)$$ in the monoidal category $$(\Set,\times, I)$$. We can then consider a left action of $$M$$ on an arbitrary set $$E$$. By [\[Set Theory\] §Product of Sets, ⁋Proposition 4](/en/math/set_theory/product_of_sets#prop4), we have

$$\Hom_\Set(M\times E,E)\cong\Hom_\Set(M,\Hom_\Set(E,E))\cong\Hom_\Set(M, \End(E))$$

so any left action defines a function $$M \rightarrow \End(E)$$. The commutativity of the two diagrams in [Definition 1](#def1) is equivalent to this function being a monoid homomorphism.

In other words, for $$M$$ to act on $$E$$ from the left means that for any $$\alpha,\beta\in M$$ and $$x\in E$$, the following equalities hold:

$$(\alpha\beta)\cdot x=\alpha\cdot(\beta\cdot x),\qquad e\cdot x=x$$

In general, we consider actions from the left as described above, but sometimes acting from the right is more natural. The following definition shows that these are in fact equivalent.

<div class="definition" markdown="1">

<ins id="def2">**Definition 2**</ins> For any magma $$(M,\ast)$$, the *opposite magma* $$(M^\op,\ast^\op)$$ is defined as follows:

1. As a set, $$M^\op=M$$.
2. For any $$x,y\in A^\op$$, we define $$x\ast^\op y$$ to be $$y\ast x$$.

</div>

One can verify that a right $$M$$-action is the same as a left $$M^\op$$-action. Rewriting this, we have

$$x\cdot(\beta\alpha)=(x\cdot\beta)\cdot\alpha,\qquad x\cdot e=x$$

Thus, left actions and right actions differ only in notation and are essentially the same concept. Therefore, in developing general theory, we will assume all actions are left actions.

<div class="example" markdown="1">

<ins id="ex3">**Example 3**</ins> Let a monoid $$M$$ and an $$M$$-set $$E$$ be given. Then $$\mathcal{P}(E)$$ naturally carries an $$M$$-set structure. For any $$\alpha\in M$$ and $$A\in \mathcal{P}(E)$$, define $$\alpha\cdot A$$ by the formula

$$\alpha\cdot A=\{\alpha\cdot a\mid a\in A\}$$

Then

$$(\alpha\beta)\cdot A=\{(\alpha\beta)\cdot a\mid a\in A\}=\{\alpha\cdot(\beta\cdot a)\mid a\in A\}=\alpha\cdot\{\beta\cdot a\mid a\in A\}=\alpha\cdot(\beta\cdot A)$$

so this defines an $$M$$-action on $$\mathcal{P}(E)$$.

</div>

For convenience, we make the following definition.

<div class="definition" markdown="1">

<ins id="def4">**Definition 4**</ins> When a monoid $$M$$ defines a left action on a set $$E$$, we call $$E$$ together with this action a (left) $$M$$-set.

</div>

## $$M$$-set Homomorphisms

<div class="definition" markdown="1">

<ins id="def5">**Definition 5**</ins> Fix a monoid $$M$$, and let $$E,E'$$ be $$M$$-sets. A function $$f:E\rightarrow E'$$ is called an *$$M$$-set homomorphism* if for all $$x\in E$$ and $$\alpha\in M$$,

$$f(\alpha\cdot x)=\alpha\cdot f(x)$$

holds.

</div>

It is easy to verify that the composition of $$M$$-set homomorphisms is again an $$M$$-set homomorphism, and the identity function is an $$M$$-set homomorphism. Thus, the collection of (left) $$M$$-sets forms a category, which we denote by $$\lset{M}$$.

Fix any monoid homomorphism $$\phi:M \rightarrow M'$$. Then for any $$M'$$-set $$E$$, the composition

$$M\overset{\phi}{\longrightarrow}M'\overset{\rho}{\longrightarrow}\End(E)$$

allows us to regard $$E$$ as an $$M$$-set. We denote this action by $$\phi^\ast\rho$$. Explicitly, $$\phi^\ast\rho$$ is the action defined for any $$\alpha\in M$$ and $$x\in E$$ by

$$(\phi^\ast\rho)(\alpha)(x)=\rho(\phi(\alpha))(x)$$

Now let two $$M'$$-actions $$\rho:M' \rightarrow \End(E)$$ and $$\rho':M' \rightarrow \End(E)$$ be given, along with an $$M'$$-homomorphism $$f:E \rightarrow E'$$ between them. Then for any $$\alpha\in M$$ and $$x\in E$$,

$$f((\phi^\ast\rho)(\alpha)(x))=f(\rho(\phi(\alpha))(x))=\rho'(\phi(\alpha))(f(x))=(\phi^\ast\rho')(f(x))$$

holds. Thus, any monoid homomorphism $$\phi:M \rightarrow M'$$ defines a functor from $$\lset{M'}$$ to $$\lset{M}$$. In particular, if $$\iota$$ is the inclusion of a submonoid, this is simply the restriction of the monoid action.

On the other hand, if $$(E_i)$$ is a collection of $$M$$-sets, their product $$\prod E_i$$ becomes an $$M$$-set with the action defined by

$$\alpha\cdot(x_i)_{i\in I}=(\alpha\cdot x_i)_{i\in I}$$

Similarly, a subset $$F$$ of an $$M$$-set $$E$$ is called an $$M$$-subset if it satisfies

$$x\in F\implies \alpha\cdot x\text{ for all $\alpha\in F$}$$

Also, if an equivalence relation $$\sim$$ on an $$M$$-set is compatible with the $$M$$-action, that is, if

$$x\sim y\implies\alpha\cdot x\sim\alpha\cdot y$$

is always true, then $$E/\mathnormal{\sim}$$ naturally carries an $$M$$-set structure.

## Stabilizer, Fixer

<div class="definition" markdown="1">

<ins id="def6">**Definition 6**</ins> Let $$A$$ be a subset of an $$M$$-set $$E$$.
- The *stabilizer* of $$A$$ is the set of all $$\alpha$$ satisfying $$\alpha A\subseteq A$$, denoted by $$\stab (A)$$.
- The *strict stabilizer* of $$A$$ is the set of all $$\alpha$$ satisfying $$\alpha A=A$$, denoted by $$\Stab(A)$$.
- The *fixer* of $$A$$ is the set of all $$\alpha$$ satisfying $$\alpha a=a$$ for all $$a\in A$$, denoted by $$\Fix(A)$$.

</div>

For any subset $$A$$, we have $$\Fix(A)\subseteq \Stab(A)\subseteq \stab(A)$$. Also, it is clear that $$e\in\Fix(A)$$.

<div class="proposition" markdown="1">

<ins id="prop7">**Proposition 7**</ins> For an $$M$$-set $$E$$ and its subset $$A$$, the sets $$\stab(A)$$, $$\Stab (A)$$, and $$\Fix(A)$$ are submonoids of $$M$$.

</div>
<details class="proof" markdown="1">
<summary>Proof</summary>

It suffices to show that these sets are closed under multiplication. If $$\alpha,\beta\in\stab(A)$$, then

$$(\alpha\beta)A=\alpha(\beta A)\subseteq \alpha A\subseteq A$$

so $$\alpha\beta\in \stab(A)$$. Similarly, if $$\alpha,\beta\in\Stab(A)$$, then

$$(\alpha\beta)A=\alpha(\beta A)=\alpha A=A$$

so $$\alpha\beta\in \Stab(A)$$. Finally, if $$\alpha,\beta\in\Fix(A)$$, then for any $$a\in A$$,

$$(\alpha\beta)a=\alpha(\beta a)=\alpha a=a$$

so $$\alpha\beta\in \Fix(A)$$.

</details>

<div class="proposition" markdown="1">

<ins id="cor8">**Corollary 8**</ins> Let a group $$G$$ be given. For a $$G$$-set $$E$$ and its subset $$A$$, the sets $$\Stab (A)$$ and $$\Fix(A)$$ are subgroups of $$G$$, and in particular, $$\Fix(A)$$ is a normal subgroup of $$\Stab(A)$$.

</div>
<details class="proof" markdown="1">
<summary>Proof</summary>

For the first claim, it suffices to show that the given sets are closed under inverses. For any $$\alpha\in\Stab(A)$$, we have

$$A=(\alpha^{-1}\alpha)A=\alpha^{-1}(\alpha A)=\alpha^{-1}A$$

and for any $$\alpha\in\Fix(A)$$ and $$a\in A$$,

$$a=(\alpha^{-1}\alpha)a=\alpha^{-1}(\alpha a)=\alpha^{-1}a$$

which establishes the claim. For the second claim, let $$\alpha\in\Fix(A)$$ and $$\beta\in\Stab(A)$$ be given. For any $$a\in A$$, we compute

$$(\beta\alpha\beta^{-1})a=\beta(\alpha(\beta^{-1}a))=\beta\beta^{-1}a=a$$

so $$\beta\alpha\beta^{-1}\in\Fix(A)$$, and the result follows.

</details>

From the proof of the above corollary, we see that when a group $$G$$ acts on a set $$E$$, the map $$\rho_g$$ is necessarily bijective. That is, $$\im\rho\subseteq \Aut(E)$$ always holds.

## Inner Automorphisms

Now we consider the case where the set $$E$$ is equipped with additional structure. For instance, suppose $$E$$ also has a monoid structure, and a given monoid $$M$$ acts on $$E$$. Then the $$M$$-action is given by a monoid homomorphism $$M \rightarrow\End(E)=\End_\Mon(E)$$.

In particular, consider the case where a group $$G$$ acts on itself. That is, suppose $$\rho:G\rightarrow\End(G)=\End_\Grp(G)$$ is given. From the proof of [Corollary 8](#cor8), we know that the image of $$\rho$$ consists entirely of bijections. Since a bijective group homomorphism is always a group isomorphism ([§Algebraic Structures, ⁋Definition 6](/en/math/algebraic_structures/algebraic_structures#def6)), we conclude that if $$G$$ acts on itself, this action must take the form of a group homomorphism $$G \rightarrow \Aut(G)$$.

Among group actions defined on itself, the following example is particularly noteworthy.

<div class="proposition" markdown="1">

<ins id="prop9">**Proposition 9**</ins> For any element $$g$$ of a group $$G$$, define $$\rho_g\in\Aut(G)$$ by the formula

$$\rho_g(x)=gxg^{-1}$$

Then the correspondence $$\rho:g\mapsto \rho_g$$ is a group homomorphism.

</div>
<details class="proof" markdown="1">
<summary>Proof</summary>

For any $$x,y\in G$$,

$$\rho_g(xy)=g(xy)g^{-1}=(gxg^{-1})(gyg^{-1})=\rho_g(x)\rho_g(y)$$

holds, so $$\rho_g$$ is a group homomorphism. Therefore, $$\im\rho\subseteq\Aut(G)$$.

On the other hand, for any $$g,h\in G$$ and $$x\in G$$,

$$\rho_{gh}(x)=(gh)x(gh)^{-1}=g(hxh^{-1})g^{-1}=(\rho_g\circ\rho_h)(x)$$

so $$\rho_{gh}=\rho_g\circ\rho_h$$. Thus, $$\rho:g\mapsto \rho_g$$ is a group homomorphism from $$G$$ to $$\Aut(G)$$.

</details>

<div class="definition" markdown="1">

<ins id="def10">**Definition 10**</ins> Let a group $$G$$ be given. The automorphism $$\rho_g$$ from [Proposition 9](#prop9) is called the *inner automorphism* defined by $$g$$, and their collection is denoted by $$\Inn(G)$$.

</div>

<div class="proposition" markdown="1">

<ins id="prop11">**Proposition 11**</ins> For a group $$G$$, the collection $$\Inn(G)$$ of inner automorphisms is a normal subgroup of $$\Aut(G)$$.

</div>
<details class="proof" markdown="1">
<summary>Proof</summary>

Since $$\Inn(G)$$ is the image of the group homomorphism $$\rho:G\rightarrow\Aut(G)$$, it is clearly a subgroup of $$\Aut(G)$$. Therefore, it suffices to show that $$\Inn(G)$$ is a *normal* subgroup.

Choose any $$f\in\Aut(G)$$ and fix $$g\in G$$. We need to show that $$f\circ\rho_g\circ f^{-1}\in \Inn(G)$$. For any $$x\in G$$,

$$(f\circ\rho_g\circ f^{-1})(x)=f(gf^{-1}(x)g^{-1})=f(g)xf(g^{-1})=\rho_{f(g)}(x)$$

which is clear.

</details>

On the other hand, $$\rho:G\rightarrow\Inn(G)$$ is surjective, so by the first isomorphism theorem,

$$G/\ker\rho\cong\Inn(G)$$

holds. The kernel $$\ker\rho$$ also has a special name.

<div class="definition" markdown="1">

<ins id="def12">**Definition 12**</ins> For a group $$G$$ and the group homomorphism $$\rho:G\rightarrow\Inn(G)$$ defined in [Proposition 9](#prop9), the kernel $$\ker\rho$$ is called the *center* of $$G$$ and is denoted by $$C(G)$$.

</div>

By definition,

$$g\in\ker\rho\iff\rho_g=\id_G\iff gxg^{-1}=x\quad\text{for all $x\in G$}$$

so the fixer $$\Fix(G)$$ when $$G$$ acts on itself by inner automorphisms is exactly $$C(G)$$. More generally, for any subset $$A\subseteq G$$, we define the *centralizer* $$C_G(A)$$ of $$A$$ to be the fixer $$\Fix(A)$$. Similarly, we define the *normalizer* $$N_G(A)$$ of $$A$$ to be $$\Stab(A)$$.

## Orbit-Stabilizer Theorem

We now return to considering group actions on general sets. First, we make the following definition.

<div class="definition" markdown="1">

<ins id="def13">**Definition 13**</ins> Let a group $$G$$ act on a set $$E$$. The *orbit* of an element $$x\in E$$ is the set

$$G\cdot x=\{g\cdot x\mid g\in G\}$$

</div>

Then the relation on $$E$$ defined by

$$x\sim y\iff G\cdot x=G\cdot y\tag{$\ast$}$$

is an equivalence relation, so the quotient set $$E/{\sim}$$ is well-defined and consists of orbits.

<div class="proposition" markdown="1">

<ins id="thm14">**Theorem 14 (Orbit-stabilizer theorem)**</ins> Let a group $$G$$ act on a set $$E$$. Then

$$\lvert G\cdot x\rvert=[G:\Stab(x)]$$

holds.

</div>
<details class="proof" markdown="1">
<summary>Proof</summary>

Define the function $$p:G \rightarrow G\cdot x$$ by $$g\mapsto g\cdot x$$. By the definition of $$G\cdot x$$, this function is surjective. On the other hand, $$p(g_1)=p(g_2)\iff g_1^{-1}g_2\in \Stab(x)$$, so the desired result follows from the canonical decomposition discussed after [\[Set Theory\] §Examples of Equivalence Relations, ⁋Proposition 7](/en/math/set_theory/examples_of_equivalence#prop7).

</details>

Therefore, if $$G$$ is finite, then by [§Quotient Groups, ⁋Proposition 5](/en/math/algebraic_structures/quotient_groups), we obtain

$$\lvert G\cdot x\rvert=\frac{\lvert G\rvert}{\lvert\Stab(x)\rvert}\tag{$\ast\ast$}$$

Similarly, suppose $$G$$ is finite and acts on a finite set $$E$$. Define $$E^g$$ to be the set of elements fixed by $$g$$:

$$E^g=\{x\in E\mid g\cdot x=x\}$$

Then

$$\sum_{g\in G}\lvert E^g\rvert=\# \{(g, x)\in G\times E: g\cdot x=x\}=\sum_{x\in X}\lvert \Stab(x)\rvert$$

holds. Now from $$(\ast\ast)$$,

$$\sum_{x\in X}\lvert \Stab(x)\rvert=\sum_{x\in X}\frac{\lvert G\rvert}{\lvert G\cdot x\rvert}$$

On the other hand, considering the quotient set $$E/{\sim}$$ defined by $$(\ast)$$, the above sum can be rewritten as

$$\sum_{x\in X}\frac{\lvert G\rvert}{\lvert G\cdot x\rvert}=\lvert G\rvert\sum_{O\in E/{\sim}}\sum_{x\in O}\frac{1}{\lvert O\rvert}=\lvert G\rvert\sum_{O\in E/{\sim}} 1=\lvert G\rvert\lvert E/{\sim}\rvert$$

From this, we obtain the following lemma.

<div class="proposition" markdown="1">

<ins id="lem15">**Lemma 15**</ins> Let a finite group $$G$$ act on a finite set $$E$$, and let $$E/{\sim}$$ be the quotient set of $$E$$ consisting of orbits. Then

$$\lvert E/{\sim}\rvert=\frac{1}{\lvert G\rvert}\sum_{g\in G}\lvert E^g\rvert$$

holds.

</div>

---

**References**

**[Bou]** Bourbaki, N. Algebra I. *Elements of Mathematics*. Springer. 1998.  

---
