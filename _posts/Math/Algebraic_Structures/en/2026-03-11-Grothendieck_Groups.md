---
title: "Grothendieck Group"
description: "It covers the definition of the Grothendieck group, which constructs an abelian group from a commutative semigroup, and the proof of existence and uniqueness through the universal mapping problem."
excerpt: "The Grothendieck group and the definition of integers"

categories: [Math / Algebraic Structures]
permalink: /en/math/algebraic_structures/Grothendieck_groups
sidebar: 
    nav: "algebraic_structures-en"

date: 2021-09-04
weight: 3
translated_at: 2026-05-29T16:03:58+00:00
translation_source: kimi-cli
last_polished_at: 2026-09-04T15:15:05+00:00
translation_polish_source: antigravity-gemini-3.8-flash-high
---
In the previous post, we examined the definition of a monoid; as a prime example, the natural numbers defined in set theory form a commutative monoid under addition. In this post, we introduce a method for obtaining an abelian group from a commutative semigroup. 

First, considering the category $\Ab$ of abelian groups, any abelian group can be viewed as a commutative monoid by forgetting the information about its inverses, so there exists a forgetful functor $U: \Ab \rightarrow \cMon$. This functor is known to have a left adjoint $K:\cMon \rightarrow \Ab$, and writing out this adjunction yields the formula

$$\Hom_\Ab(K(M), G)\cong\Hom_\cMon(M, U(G))$$

. That is, given a commutative monoid $M$ and a monoid homomorphism $M\rightarrow U(G)$, we must be able to obtain a unique group homomorphism $K(M)\rightarrow G$. 

## Universal mapping problem

Now we must show the existence of the left adjoint $K$ described above. More generally, following our main reference **\[Bou\]**, we examine the process of obtaining an abelian group from a commutative *semigroup*. Meanwhile, using the unit of the adjunction, we can write out the property that $K$ must satisfy. 

> An abelian group $K(S)$ and a semigroup homomorphism $\eta_S:S\rightarrow K(S)$ are a pair satisfying the following property.  
>
>{% diagram Math/Algebraic_Structures/Grothendieck_Groups-1.svg width="6.91em" alt="universal_property" %}
>     
>(Universal mapping problem) Whenever an arbitrary abelian group $G$ and an arbitrary semigroup homomorphism $f:S\rightarrow G$ are given, there exists a unique *group homomorphism* $\bar{f}:K(S)\rightarrow G$ such that $f=\bar{f}\circ\eta_S$ holds.

Interpreting this intuitively, $K(S)$ can be thought of as the smallest abelian group obtained from $(S,+)$. 

$K(S)$ satisfying the above property is unique up to isomorphism.

::: Proposition 1
If an abelian group $H$ and a semigroup homomorphism $\eta_S'$ satisfy the above universal mapping problem, then $K(S)\cong H$ holds.
:::
::: Proof
First, consider the following diagram.

{% diagram Math/Algebraic_Structures/Grothendieck_Groups-2.svg width="6.91em" alt="uniqueness_1" %}

Then by the universal property, there exists $\bar{\eta}_S': K(S)\rightarrow H$ such that $\eta_S'= \bar{\eta}_S'\circ\eta_S$. Meanwhile, from the following diagram

{% diagram Math/Algebraic_Structures/Grothendieck_Groups-3.svg width="6.91em" alt="uniqueness_2" %}

using the universal property for $H$, there exists $\bar{\eta}_S:H\rightarrow K(S)$ such that $\eta_S=\bar{\eta}_S\circ\eta_S'$. Then

$$\bar{\eta}_S'\circ\bar{\eta}_S\circ\eta_S'=\bar{\eta}_S'\circ \eta_S=\eta_S'=\id_{H}\circ \eta_S' $$

and again by the universal property, since $f$ satisfying $f\circ \eta_S'=\eta_S'$ is unique, $f=\id_H=\bar{\eta}_S'\circ \bar{\eta}_S$ holds. Or, in the language of diagrams, since the map $H\rightarrow H$ making the following diagram commute is unique, we must have $\id_H=\bar{\eta}_S'\circ \bar{\eta}_S$.

{% diagram Math/Algebraic_Structures/Grothendieck_Groups-4.svg width="9.96em" alt="uniqueness_3" %}

Similarly, one can show that $\id_{K(S)}=\bar{\eta}_S\circ \bar{\eta}_S'$ holds, and therefore $K(S)\cong H$ holds.
:::

On the other hand, if $S$ was already an abelian group, $K(S)$ should turn out to be $S$ itself without the need to add other elements.

::: Proposition 2
If $S$ is an abelian group, the abelian group $K(S)$ satisfying the above universal mapping problem satisfies $K(S)\cong S$.
:::
::: Proof
Since $S$ and $\id_S$ trivially satisfy the universal property, by the preceding [Proposition 1](#prop1), any abelian group satisfying the universal property must be isomorphic to $S$.
:::

The two propositions above show that $K(S)$ satisfying the universal mapping problem is the abelian group we are seeking, but they do not show that $K(S)$ actually exists. 

## Definition of $K(S)$

The reason why $S$ cannot be an abelian group is that an identity element and inverses for arbitrary elements might not exist. Intuitively, this can be resolved by adding $0$ and *negative numbers*.

For a given commutative semigroup $(S,+)$, consider the product semigroup $S\times S$. ([§Algebraic Structures, ⁋Example 5](/en/math/algebraic_structures/algebraic_structures#ex5)) If we think of the second component of $S\times S$ as negative numbers, the equation

$$(a_1, b_1)+(a_2, b_2)=(a_1+a_2, b_1+b_2)$$

can be thought of as if representing

$$(a_1+a_2)-(b_1+b_2)=(a_1-b_1)+(a_2-b_2)$$

. 

Of course, even if we choose $a$ and $b$ differently, the difference $a-b$ can be the same value, so we define an equivalence relation $R$ on $S\times S$ as follows:

$$(a_1, b_1)\equiv (a_2, b_2)\pmod{R}\iff a_1+b_2+c=a_2+b_1+c\text{ for some $c\in S$}$$

First, we must show that this relation is an equivalence relation.

::: Lemma 3
The relation $R$ defined above is an equivalence relation compatible with the operation on the product semigroup $S\times S$.
:::
::: Proof
First, we show that $R$ is an equivalence relation. For any $(a,b)\in S\times S$, 

$$a+b+c=a+b+c$$

holds for any $c\in S$, so $(a,b)\equiv(a,b)$. Suppose $(a_1,b_1)\equiv (a_2,b_2)$. That is, for some $c\in S$,

$$a_1+b_2+c=a_2+b_1+c$$

holds. But this is precisely the condition for $(a_2,b_2)\equiv (a_1,b_1)$, so $R$ is symmetric. Finally, suppose $(a_1,b_1)\equiv(a_2,b_2)$ and $(a_2,b_2)\equiv (a_3,b_3)$. Then for some $c$, $c'$,

$$a_1+b_2+c=a_2+b_1+c,\qquad a_2+b_3+c'=a_3+b_2+c'$$

hold. Now adding the two equations, 

$$a_1+b_3+(a_2+b_2+c+c')=a_3+b_1+(a_2+b_2+c+c')$$

so $(a_1,b_1)\equiv(a_3,b_3)$ holds. That is, $R$ is an equivalence relation.

Now we must show that $R$ is compatible with the operation on $S\times S$. To this end, suppose $(a_1, b_1)\equiv(a_1',b_1')$ and $(a_2, b_2)\equiv (a_2',b_2')$. We must show that $(a_1+a_2, b_1+b_2)\equiv(a_1'+a_2', b_1'+b_2')$. From the given conditions, there exist suitable $c_1$, $c_2$ such that

$$a_1+b_1'+c_1=a_1'+b_1+c_1,\qquad a_2+b_2'+c_2=a_2'+b_2+c_2$$

hold. Now, adding the two equations,
$$(a_1+a_2)+(b_1'+b_2')+(c_1+c_2)=(a_1'+a_2')+(b_1+b_2)+(c_1+c_2)$$

holds, so by definition $(a_1+a_2, b_1+b_2)\equiv(a_1'+a_2', b_1'+b_2')\pmod{R}$ holds, and therefore $R$ is compatible with the operation on $S\times S$. 
:::

Therefore, $(S\times S)/R$ becomes a commutative semigroup. Let this be $K(S)$. 

::: Lemma 4
$K(S)$ is an abelian group.
:::
::: Proof
It suffices to show that $K(S)$ has an identity element and inverses. Since we think of $(a,b)$ as $a-b$, the identity element will be $(a,a)$, and the inverse of $(a,b)$ will be $-(a-b)=b-a$, that is, $(b,a)$. Let us prove this.

First, for any $c\in S$, we show that $[(c,c)]$ is an identity element. For any $[(a,b)]\in K(S)$,

$$[(a,b)]+[(c,c)]=[(a+c, b+c)]$$

holds. But since

$$(a+c)+b+d=(b+c)+a+d$$

holds for any $d\in S$, we have $(a+c, b+c)\equiv (a,b)$, and therefore $[(a+c, b+c)]=[(a,b)]$ holds. By commutativity, $[(c,c)]+[(a,b)]=[(a,b)]$ also naturally holds, so $[(c,c)]$ is an identity element of $K(S)$. 

Meanwhile, for any $[(a,b)]\in K(S)$,

$$[(a,b)]+[(b,a)]=[(a+b,a+b)]$$

so by the preceding argument, $[(a,b)]+[(b,a)]$ is an identity element of $K(S)$, and the same is true for $[(b,a)]+[(a,b)]$. Therefore, the inverse of any element of $K(S)$ exists, so $K(S)$ has the structure of a group. 
:::

Then $K(S)$ is the abelian group we were looking for. That is, $K(S)$ satisfies the above universal mapping problem.

::: Proposition 5
For a commutative semigroup $(S, +)$, the abelian group $K(S)$ constructed as above and the natural semigroup homomorphism $\eta_S:S\rightarrow K(S)$ satisfy the universal property.
:::
::: Proof
First, let us think about what the *natural semigroup homomorphism* from $S$ to $K(S)$ should be. Since we treat $(a,b)$ as $a-b$ in $K(S)$, we can see that $a$ corresponds in $K(S)$ to $(a+b)-b$, that is, $[(a+b, b)]$. Therefore, let us define $\eta_S$ by $a\mapsto[(a+a, a)]$. Of course, choosing any $b$ and defining it by $a\mapsto[(a+b,b)]$ yields the same value.

To prove the universal property, let an arbitrary abelian group $G$ and a semigroup homomorphism $f:S\rightarrow G$ be given. 

First, if $\bar{f}:K(S)\rightarrow G$ satisfying the given property exists, $\bar{f}$ must be unique. This is because for any $[(a,b)]$, 

$$\begin{aligned}\bar{f}\left([(a,b)]\right)&=\bar{f}\left([(a+(a+b), b+(a+b))]\right)=\bar{f}\left([(a+a,a)]+[(b, b+b)]\right)\\ &=\bar{f}\left([(a+a, a)]\right)+\bar{f}\left([(b,b+b)]\right)=\bar{f}\left(\eta_S(a)\right)-\bar{f}\left(\eta_S(b)\right)\\ &=f(a)-f(b)\end{aligned}$$

so the function values at each element are uniquely determined. 

Now, taking a hint from the uniqueness proof, let us define $\bar{f}([(a,b)])$ to be $f(a)-f(b)$. First, this is well-defined. That is, if $(a_1,b_1)\equiv(a_2,b_2)$, then $f(a_2)-f(b_2)=f(a_1)-f(b_1)$ holds. Since $(a_1,b_1)\equiv(a_2,b_2)$, there exists some $c\in S$ such that $a_1+b_2+c=a_2+b_1+c$, and therefore

$$f(a_1)+f(b_2)+f(c)=f(a_1+b_2+c)=f(a_2+b_1+c)=f(a_2)+f(b_1)+f(c)$$

so by subtracting $f(c)$ from both sides and rearranging appropriately, we obtain

$$f(a_1)-f(b_1)=f(a_2)-f(b_2)$$

. 

Also, $\bar{f}$ is a group homomorphism, because for any $[(a_1, b_1)]$, $[(a_2,b_2)]$,

$$\begin{aligned}\bar{f}\left([(a_1,b_1)]+[(a_2, b_2)]\right)&=\bar{f}\left([(a_1+a_2, b_1+b_2)]\right)=f(a_1+a_2)-f(b_1+b_2)\\&=f(a_1)+f(a_2)-f(b_1)-f(b_2)=(f(a_1)-f(b_1))+(f(a_2)-f(b_2))\\&=\bar{f}\left([(a_1, b_1)]\right)+\bar{f}\left([(a_2,b_2)]\right)\end{aligned}$$

holds. 

Finally, that $\bar{f}$ satisfies the given condition $f=\bar{f}\circ\eta_S$ is clear upon calculation.
:::

In this way, we have obtained the abelian group $K(S)$ we wanted. In particular, we can define the integers in a rigorous manner.

::: Definition 6
For the monoid $(\mathbb{N},+)$, the abelian group obtained through the above process is written as $(\mathbb{Z},+)$.
:::

## Monoid of fractions

In the discussion above, we obtained $K(S)$ by adding inverses of all elements of $S$. Meanwhile, looking at [Definition 6](#def6), what we actually do is add inverses only for the elements of the subset $\mathbb{N}\setminus\{0\}$ of $\mathbb{N}$. This can also be obtained by slightly modifying the discussions above; we omit the proofs and examine only the process.

Consider a commutative monoid $E$, a subset $S$ of $E$, and the submonoid $S'$ of $E$ generated by $S$. We also consider the operation of $E$ to be written multiplicatively. If we define the following relation on $E\times S'$:

$$(a,p)\equiv (b,q)\pmod{R}\iff aqs=bps\text{ for some $s\in S'$}$$

this relation is an equivalence relation compatible with the operation on $E\times S'$, and therefore $(E\times S')/R$ becomes a monoid.

::: Definition 7
The monoid $(E\times S')/R$ obtained as above is called the *monoid of fractions* of $E$ with denominator $S$ and is denoted by $E_S$. The element of this monoid having $(a,p)$ as a representative is denoted by $a/p$. 
:::

In this case, since $E$ is a monoid, unlike the discussion above, it has an identity element $1$. Then the canonical morphism corresponding to the homomorphism $\eta_S$ in [Proposition 5](#prop5) can be explicitly thought of as 

$$\epsilon:E\rightarrow E_S;\quad a\mapsto a/1$$

. 

---

**References**

**[Bou]** Bourbaki, N. Algebra I. *Elements of Mathematics*. Springer. 1998.  

---
