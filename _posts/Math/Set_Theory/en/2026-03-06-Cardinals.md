---

title: "Cardinals"
excerpt: "Definition of Cardinal number"

categories: [Math / Set Theory]
permalink: /en/math/set_theory/cardinals
header:
    overlay_image: /assets/images/Math/Set_Theory/Cardinals.png
    overlay_filter: 0.5
sidebar: 
    nav: "set_theory-en"

date: 2026-03-06
last_modified_at: 2026-03-06
weight: 24

---

## Review

Let us begin by briefly summarizing the key topics from the previous post. We constructed the natural numbers and then defined ordinal numbers, exploring their properties. Well-ordering, while not directly related to ordinal numbers, was another important topic. A well-ordering is defined as follows.

<div class="definition" markdown="1">

<ins id="def-3">**Definition**</ins> A totally ordered set $$R$$ defined on a set $$A$$ is a *well-ordering* if every non-empty subset $$X$$ of $$A$$ has a least element.

</div>

Furthermore, we proved that every set can be well-ordered, and this proof relied on the *Axiom of Choice*.

**The Axiom of Choice.** Every set has a choice function.
{: .misc}


<ins id="thm-2">**Theorem (Zermelo)**</ins> Every set $$A$$ can be well-ordered.
{: .proposition}

<ins id="thm-1">**Theorem (Zorn's lemma)**</ins> Every inductive set has a maximal element.
{: .proposition}

Among the proofs using this result, the following theorem will be useful for our purposes.

<div class="proposition" markdown="1">

<ins id="prop-0">**Proposition**</ins> Let $$A,B$$ be two well-ordered sets. Then at least one of the following holds.
1. There exists an order isomorphism from $$A$$ to a segment of $$B$$, or
2. There exists an order isomorphism from $$B$$ to a segment of $$A$$.

</div>

Finally, we observed that ordinal numbers allow us to rigorously define the size of a set.

In this post, we will define the size of a set in a somewhat less rigorous manner and define operations on these sizes.

## Basic Definitions

Let us begin. The cardinal of a set is a generalization of the size of a set, that is, the number of its elements. However, since we have not yet defined the natural numbers, we must take a different perspective. While we cannot define how large a set is, we can determine when two sets have the same size as follows.

<div class="definition" markdown="1">

<ins id="def1">**Definition 1**</ins> A set $$A$$ is *equipotent* to a set $$B$$ if there exists a bijection from $$A$$ to $$B$$.

</div>

Then

1. For any set $$A$$, $$\id_A$$ is a bijection from $$A$$ to $$A$$.
2. If there exists a bijection $$f:A\rightarrow B$$ between sets $$A,B$$, then its inverse $$f^{-1}:B\rightarrow A$$ is a bijection from $$B$$ to $$A$$.
3. The composition of two bijections is also a bijection.

From the above, the only condition from the definition of an equivalence relation that is not satisfied is that the above relation is reflexive <em-ko>on a particular set $$U$$</em-ko>, and thus if we can resolve the problem that a universal set does not exist, we can think of this relation as an equivalence relation defined on a universal set.

Although this is not a rigorous solution, we will proceed under the assumption that this problem has been resolved. (See: [Wikipedia, Class](https://en.wikipedia.org/wiki/Class_(set_theory)))

<div class="definition" markdown="1">

<ins id="def2">**Definition 2**</ins> A representative of the equivalence class of a set $$A$$ is called the *cardinal* of $$A$$, denoted by $$\card A$$.

</div>

Since the empty set is unique, $$\card\emptyset$$ is exactly $$\emptyset$$. When dealing with cardinals, we denote this set by $$\mathbf{0}$$. Singletons, such as $$\{a\}$$ and $$\{b\}$$, are all equipotent to each other, since $$\{(a,b)\}$$ is a bijection from $$\{a\}$$ to $$\{b\}$$. Let us denote this by $$\mathbf{1}$$. While these are not yet natural numbers, we will soon define operations on cardinals to treat them like natural numbers.

Before defining operations, let us first define an ordering relation between cardinals.

<div class="definition" markdown="1">

<ins id="def3">**Definition 3**</ins> The relation among cardinals

> $$\mathfrak{a}$$ is equipotent to a subset of $$\mathfrak{b}$$.

is an order relation, denoted by $$\mathfrak{a}\leq\mathfrak{b}$$.

</div>

Of course, we have not verified that this relation is actually an order relation. However, the only non-trivial part is antisymmetry.

<div class="proposition" markdown="1">

<ins id="lem4">**Lemma 4 (Cantor-Bernstein)**</ins> The relation $$\leq$$ above is antisymmetric.

</div>
<details class="proof" markdown="1">
<summary>Proof</summary>

Let $$\mathfrak{a}\leq\mathfrak{b}$$ and $$\mathfrak{b}\leq\mathfrak{a}$$ for two cardinals $$\mathfrak{a}$$ and $$\mathfrak{b}$$.

If $$i$$ is a bijection from $$\mathfrak{a}$$ to a subset of $$\mathfrak{b}$$, then $$i(\mathfrak{a})\subset\mathfrak{b}$$ and $$\mathfrak{a}$$ is equipotent to $$i(\mathfrak{a})$$. Therefore, it suffices to show that there exists a bijection between $$i(\mathfrak{a})$$ and $$\mathfrak{b}$$.  
Since $$\mathfrak{b}\leq\mathfrak{a}$$, there exists a bijection from $$\mathfrak{b}$$ to a subset of $$\mathfrak{a}$$, which can be viewed as an injection from $$\mathfrak{b}$$ to $$\mathfrak{a}$$. Since $$\mathfrak{a}$$ is equipotent to $$i(\mathfrak{a})$$, composing a bijection between these two with the previous injection yields an injection from $$\mathfrak{b}$$ to $$i(\mathfrak{a})$$. Call this $$f$$. Now let $$C_0=\mathfrak{b}\setminus i(\mathfrak{a})$$, define $$C_{n+1}=f(C_n)$$ inductively, and let $$C=\bigcup C_n$$. We will define $$h:\mathfrak{b}\rightarrow i(\mathfrak{a})$$ by the formula

$$h(x)=\begin{cases} f(x)&x\in C\\ x&x\not\in C\end{cases}$$

and show that it is a bijection from $$\mathfrak{b}$$ to $$i(\mathfrak{a})$$.

First, $$h$$ is a function from $$\mathfrak{b}$$ to $$i(\mathfrak{a})$$. That $$h$$ is well-defined is clear, and we only need to verify that the target of this function is $$i(\mathfrak{a})$$. If $$x\in C$$, then $$h(x)=f(x)\in i(\mathfrak{a})$$, which is clear. If $$x\not\in C$$, then $$x\not\in C_0$$, so $$x\not\in\mathfrak{b}\setminus i(\mathfrak{a})$$. Thus in this case as well, $$x\in i(\mathfrak{a})$$.

Also, $$h$$ is injective. If $$h(x)=h(y)$$, then in the case $$x,y\in C$$, we have $$f(x)=f(y)$$, and since $$f$$ is injective, $$x=y$$. In the case $$x,y\not\in C$$, clearly $$x=y$$.  
The non-trivial case is when one element is in $$C$$ and the other is not. Let $$x\in C$$ and $$y\not\in C$$. Then $$x\in C_n$$ for some $$n$$, and in particular $$h(x)=f(x)\in C_{n+1}\subseteq C$$, so $$h(x)\in C$$. On the other hand, $$h(y)=y$$, but since $$y\not\in C$$ by assumption, this contradicts the assumption that $$h(x)=h(y)$$. Therefore $$x=y$$ always holds, and $$h$$ is injective.

Finally, let us show that $$h$$ is surjective. For any $$y\in i(\mathfrak{a})$$, either $$y\in C$$ or $$y\not\in C$$. If $$y\not\in C$$, then by the definition of $$h$$, $$h(y)=y$$. If $$y\in C$$, then $$y\in C_{n}$$ for some $$n\geq 1$$. (Since $$y\in C_0=\mathfrak{b}\setminus i(\mathfrak{a})$$ is impossible.) Thus $$y\in f(C_{n-1})$$, so there exists $$x\in C_{n-1}$$ with $$y=f(x)$$. This $$x$$ is also an element of $$C$$, so $$h(x)=f(x)=y$$, and therefore $$h$$ is surjective.

</details>

Furthermore, any set of cardinals is a well-ordered set.

<div class="proposition" markdown="1">

<ins id="thm5">**Theorem 5**</ins> Any set $$A$$ of cardinals has a least element.

</div>
<details class="proof" markdown="1">
<summary>Proof</summary>

Consider the set $$A=\bigcup_{\mathfrak{a}\in E}\mathfrak{a}$$. Then every cardinal $$\mathfrak{a}\in E$$ is a subset of $$A$$.

By the well-ordering principle, there exists a well-ordering on this set. Denote it by $$\leq$$. Also, every subset of $$A$$ is equipotent to a segment of $$A$$ ([Proposition](#prop0) in Review). Thus for every cardinal $$\mathfrak{a}$$, the set of segments of $$A$$ that are equipotent to it is non-empty, and by the well-orderedness of $$A^\*$$, there exists a least element. Denote this element by $$\varphi(\mathfrak{a})$$.  
If we can show that $$\mathfrak{a}\leq\mathfrak{b}$$ is equivalent to $$\varphi(\mathfrak{a})\subset\varphi(\mathfrak{b})$$, then the proof will be complete from the well-orderedness of $$A$$.

First, it is clear that the latter condition implies the former. Conversely, suppose $$\mathfrak{a}\leq\mathfrak{b}$$, i.e., $$\mathfrak{a}$$ is equipotent to a subset of $$\mathfrak{b}=\varphi(\mathfrak{b})$$ (equality holds as cardinals). If $$\varphi(\mathfrak{b})\subset\varphi(\mathfrak{a})$$ and $$\varphi(\mathfrak{a})\neq\varphi(\mathfrak{b})$$, then there would exist some segment of $$\varphi(\mathfrak{b})$$ equipotent to $$\mathfrak{a}$$, contradicting the definition of $$\varphi(\mathfrak{b})$$. Therefore the two conditions are equivalent.

</details>

---
**References** 

**[Bou]** N. Bourbaki, <i>Theory of Sets</i>. Elements of mathematics. Springer Berlin-Heidelberg, 2013.

---
