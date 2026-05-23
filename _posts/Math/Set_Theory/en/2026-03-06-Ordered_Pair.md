---
title: "Ordered Pairs"
excerpt: "Subset relations and the definition of ordered pairs"

categories: [Math / Set Theory]
permalink: /en/math/set_theory/ordered_pair

header:
    overlay_image: /assets/images/Math/Set_Theory/Ordered_Pair.png
    overlay_filter: 0.5

sidebar: 
    nav: "set_theory-en"

date: 2021-08-09
last_modified_at: 2022-11-21

weight: 2
translated_at: 2026-05-23T16:30:02+00:00
translation_source: kimi-cli
---
## Subset Relations

<div class="definition" markdown="1">

<ins id="def1">**Definition 1**</ins> The statement $$A\subseteq B$$ means that for any $$x$$, the proposition $$x\in A\implies x\in B$$ is always true.

</div>

The following two propositions are properties of $$\subset$$.

<div class="proposition" markdown="1">

<ins id="prop2">**Proposition 2**</ins> $$A\subseteq A$$ always holds.

</div>
<details class="proof" markdown="1">
<summary>Proof</summary>

$$x\in A\implies x\in A$$ is always true.

</details>

<div class="proposition" markdown="1">

<ins id="prop3">**Proposition 3**</ins> If $$A\subseteq B$$ and $$B\subseteq C$$, then $$A\subseteq C$$.

</div>
<details class="proof" markdown="1">
<summary>Proof</summary>

First, the hypothesis means that for any $$x$$, the two propositions $$x\in A\implies x\in B$$ and $$x\in B\implies x\in C$$ are true. Hence, by syllogism, $$x\in A\implies x\in C$$ is also true, and since $$x$$ was arbitrary, $$A\subseteq C$$ holds.

</details>

From the two propositions above, we see that $$\subseteq$$ is an order relation among sets. ([§Definition of Order Relations, ⁋Definition 1](/en/math/set_theory/order_relations#def1))

## Ordered Pairs

Virtually the only tool we use in set theory is a binary relation, and the language expressing it is the ordered pair. For example, the binary relation $$\subseteq$$ examined above can be thought of as the “set”

$$\subseteq=\{(A,B),(B,C),\cdots\}$$

consisting of ordered pairs $$(A,B)$$ satisfying $$A\subseteq B$$.[^1] Similarly, a function $$y=f(x)$$ can be thought of as the following set

$$F=\{(x_1,f(x_1)), (x_2,f(x_2)),\cdots\}$$

and an *equivalence relation*, which we have not yet defined, can also be represented as a set of ordered pairs in this way.

However, among the sets we have defined, there is no tool that can play the role of the ordered pair learned in middle and high school. For instance, since $$\{A,B\}=\{B,A\}$$, simply using the axiom of pair once does not allow us to distinguish the order of $$A$$ and $$B$$.

<div class="definition" markdown="1">

<ins id="def4">**Definition 4**</ins> We define the *ordered pair* $$(x,y)$$ as the set $$\big\{\{x\}, \{x,y\}\big\}$$.

</div>

For the above definition to make sense, we must first show the following lemma.[^2]

<div class="proposition" markdown="1">

<ins id="lem5">**Lemma 5**</ins> For any two sets $$x$$, $$y$$, the set $$(x,y)$$ always exists and is unique.

</div>
<details class="proof" markdown="1">
<summary>Proof</summary>

The sets $$\{x\}=\{x,x\}$$ and $$\{x,y\}$$ each exist by the axiom of pair, and therefore the set $$\big\{\{x\}, \{x,y\}\big\}$$ also exists by the axiom of pair again.

For uniqueness, $$\{x\}=\{x,x\}$$ and $$\{x,y\}$$ are first determined uniquely, and then the set $$(x,y)$$ obtained by applying the axiom of pair to them is also determined uniquely; this can be checked by using extensionality twice.

</details>

We have checked that the ordered pair $$(x,y)$$ is well-defined, but we must verify that this ordered pair satisfies $$(x,y)\neq (y,x)$$ for general $$x,y$$.

<div class="proposition" markdown="1">

<ins id="prop6">**Proposition 6**</ins> For two ordered pairs $$(x,y)$$, $$(x',y')$$, the statement <phrase>$(x,y)=(x',y')$</phrase> and the statement <phrase>$x=x'$ and $y=y'$</phrase> are equivalent.

</div>
<details class="proof" markdown="1">
<summary>Proof</summary>

If $$x=x'$$ and $$y=y'$$, then $$(x,y)=(x',y')$$ is obvious, because $$\{x\}=\{x'\}$$ and $$\{x,y\}=\{x',y'\}$$.

Now conversely suppose $$(x,y)=(x',y')$$. By definition,

$$\big\{\{x\},\{x,y\}\big\}=\big\{\{x'\},\{x',y'\}\big\}$$

holds. Since exactly one of $$x=y$$ and $$x\neq y$$ must hold, we divide into two cases.

- If $$x=y$$, the left-hand side of the above equation becomes

    $$\big\{\{x\},\{x,x\}\big\}=\big\{\{x\},\{x\}\big\}=\big\{\{x\}\big\}$$

    so $$\big\{\{x\}\big\}=\big\{\{x'\},\{x',y'\}\big\}$$. Hence $$\{x\}=\{x'\}=\{x',y'\}$$, so $$x=x'=y'$$ and therefore $$x=x'=y=y'$$. That is, $$x=x'$$ and $$y=y'$$, so this case is done.

- The remaining case is $$x\neq y$$. In this case, $$\{x,y\}\neq\{x'\}$$, so for the two ordered pairs to be equal, we must have $$\{x\}=\{x'\}$$ and $$\{x,y\}=\{x',y'\}$$. Then from $$\{x\}=\{x'\}$$ we get $$x=x'$$, and from $$\{x,y\}=\{x',y'\}$$ we get $$y=y'$$. Hence this case is also done.

</details>

Consider the set

$$\bigcup z=\{x\}\cup\{x,y\}=\{x,y\}$$

Now define the property

> $$P(s)$$: There exists some $$t$$ such that $$z=(s,t)$$.

Then we obtain the subset

$$\left\{s\in\bigcup z\mid P(s)\right\}$$

of the preceding set $$\bigcup z$$. This set is the singleton $$\{x\}$$. If we similarly define the property $$Q$$ appropriately, we obtain the singleton $$\{y\}$$.

<div class="definition" markdown="1">

<ins id="def7">**Definition 7**</ins> For the two sets $$\{x\}$$, $$\{y\}$$ obtained by the above process, we call the unique element $$x$$ of $$\{x\}$$ the *first component* of $$z=(x,y)$$, and the unique element $$y$$ of $$\{y\}$$ the *second component* of $$z=(x,y)$$, and denote them respectively by

$$x=\pr_1 z,\qquad y=\pr_2 z$$

</div>

Here $$\pr$$ is short for **pr**ojection. Meanwhile, we can define the product $$A\times B$$ of two sets $$A$$, $$B$$ as follows.

<div class="definition" markdown="1">

<ins id="def8">**Definition 8**</ins> For two sets $$A$$, $$B$$, we call the set

$$\{z\mid(z=(x,y))\wedge (x\in A)\wedge(y\in B)\}$$

the *cartesian product* of $$A$$ and $$B$$, and simply denote it by $$A\times B$$.

Also, similarly to [Definition 7](#def7), we call the sets $$A$$ and $$B$$ the first and second components of $$A\times B$$.

</div>

To know when two product sets $$A\times B$$ and $$A'\times B'$$ are equal, it suffices to determine precisely when one product set is contained in the other.

<div class="proposition" markdown="1">

<ins id="prop9">**Proposition 9**</ins> For two nonempty sets $$A'$$, $$B'$$, the statement <phrase>$A'\times B'\subseteq A\times B$</phrase> and the statement <phrase>$A'\subseteq A$ and $B'\subseteq B$</phrase> are equivalent.

</div>
<details class="proof" markdown="1">
<summary>Proof</summary>

First, assume $$A'\times B'\subseteq A\times B$$. To show $$A'\subseteq A$$, let an arbitrary $$a'\in A'$$ be given and show $$a'\in A$$.
Since $$B'$$ is nonempty, there exists some element $$b'\in B'$$. Hence $$(a',b')\in A'\times B'$$, and since $$A'\times B'\subseteq A\times B$$, we have $$(a',b')\in A\times B$$ and so $$a'\in A$$. Similarly, $$B'\subseteq B$$ can be shown.

Conversely, suppose $$A'\subseteq A$$ and $$B'\subseteq B$$. We must show that for any $$z'\in A'\times B'$$, we have $$z'\in A\times B$$.
Let $$z'=(a',b')$$. That is, $$a'\in A'$$, $$b'\in B'$$, but by hypothesis $$a'$$ and $$b'$$ are also elements of $$A$$ and $$B$$, so $$(a,b)\in A\times B$$.

</details>

When one of $$A,B$$ is empty, the following proposition applies.

<div class="proposition" markdown="1">

<ins id="prop10">**Proposition 10**</ins> For two sets $$A$$, $$B$$, the statement <phrase>$A\times B=\emptyset$</phrase> and the statement <phrase>$A=\emptyset$ or $B=\emptyset$</phrase> are equivalent.

</div>
<details class="proof" markdown="1">
<summary>Proof</summary>

First suppose $$A\times B=\emptyset$$. If both $$A$$ and $$B$$ are nonempty, then we can pick some $$a\in A$$ and $$b\in B$$, so $$(a,b)\in A\times B$$, which is a contradiction.

Conversely, assume $$A$$ or $$B$$ is empty. Once again, if we deny the conclusion and suppose $$A\times B$$ is nonempty, then there exists some element $$(a,b)\in A\times B$$. Hence $$a\in A$$ and $$b\in B$$, which contradicts the assumption that $$A$$ or $$B$$ is empty. Q.E.D.

</details>

---
**References**

**[HJJ]** K. Hrbacek, T.J. Jeck, and T. Jech. *Introduction to Set Theory*. Lecture Notes in Pure and Applied Mathematics. M. Dekker, 1978.  
**[Bou]** N. Bourbaki, <i>Theory of Sets</i>. Elements of mathematics. Springer Berlin-Heidelberg, 2013.

---

[^1]: Of course this “set” is not a set. ([§ZFC Axioms, ⁋Example 4](/en/math/set_theory/zfc_axioms#ex4))
[^2]: From the end of the proof of this lemma onward, we no longer mention the axioms used in the proof process.
