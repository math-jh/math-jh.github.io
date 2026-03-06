---

title: "Operations on Binary Relations"
excerpt: "Inverse and Composition of Binary Relations"

categories: [Math / Set Theory]
permalink: /en/math/set_theory/operation_of_binary_relations

header:
    overlay_image: /assets/images/Math/Set_Theory/Operation_of_binary_relations.png
    overlay_filter: 0.5

sidebar: 
    nav: "set_theory-en"

date: 2022-11-22
last_modified_at: 2022-11-22

weight: 4

---

We now define the inverse of binary relations and their composition.

## Inverse of a Binary Relation

<div class="definition" markdown="1">

<ins id="def1">**Definition 1**</ins> Let $R$ be a binary relation. The *inverse* of $R$, denoted by $R^{-1}$, is the binary relation consisting of all $(y,x)$ such that $(x,y)\in R$. Also, the set $R^{-1}(X)$ is called the *preimage* of $X$. If $R^{-1}=R$, then $R$ is said to be *symmetric*.

</div>

Explicitly, $R^{-1}$ is the set satisfying the following condition:

$$(x,y)\in R\iff (y,x)\in R^{-1}$$

The set $R^{-1}(X)$ can be viewed as the preimage of $X$ under the binary relation $R$, or as the image of $X$ under the inverse relation $R^{-1}$. However, by the definition of $R^{-1}$, either perspective yields the same set, so there is no room for confusion.

<div class="proposition" markdown="1">

<ins id="prop2">**Proposition 2**</ins> The inverse of $R^{-1}$ is $R$. Moreover, $\pr_1R^{-1}=\pr_2R$ and $\pr_2R^{-1}=\pr_1R$.

</div>
<details class="proof" markdown="1">
<summary>Proof</summary>

The first claim follows trivially from the following equation:

$$(x,y)\in R\iff (y,x)\in R^{-1}\iff (x,y)\in (R^{-1})^{-1}$$ 

For the second claim, if $x\in\pr_1R^{-1}$, then there exists some $y$ such that $(x,y)\in R^{-1}$. Now since $(y,x)\in R$, we have $x\in\pr_2R$. Reversing this argument proves $\pr_2R\subset\pr_1R^{-1}$.

For the case $\pr_2R^{-1}=\pr_1R$ which we have not yet shown, we can simply substitute $R^{-1}$ in place of $R$ in the claim just proven.

</details>

For given sets $A,B$, $A\times B$ was the largest binary relation having $A$ as source and $B$ as target. Therefore, from the two equations

$$\pr_1(A\times B)^{-1}=\pr_2(A\times B)=B,\qquad \pr_2(A\times B)^{-1}=\pr_1(A\times B)=A$$

we have $(A\times B)^{-1}\subseteq B\times A$. Conversely, if $(y,x)\in B\times A$, then $x\in A$ and $y\in B$, so $(x,y)\in A\times B$, and therefore $(y,x)\in (A\times B)^{-1}$. Thus $(A\times B)^{-1}=B\times A$ holds.

## Composition of Binary Relations

<div class="definition" markdown="1">

<ins id="def3">**Definition 3**</ins> Let $R\_1$ and $R\_2$ be binary relations. The *composition* $R\_2\circ R\_1$ of these two binary relations is the set of ordered pairs $(x,z)$ such that there exists $y$ with $(x,y)\in R\_1$ and $(y,z)\in R\_2$.

</div>

It is natural to wonder how the composition of binary relations defined above relates to the inverse defined earlier.

<div class="proposition" markdown="1">

<ins id="prop4">**Proposition 4**</ins> Let $R\_1$, $R\_2$ be binary relations. Then the inverse of $R\_2\circ R\_1$ is $R\_2^{-1}\circ R\_1^{-1}$.

</div>
<details class="proof" markdown="1">
<summary>Proof</summary>

$(z,x)\in (R\_2\circ R\_1)^{-1}$ is equivalent to $(x,z)\in R\_2\circ R\_1$. This is in turn equivalent to <phrase>there exists some $y$ such that $(x,y)\in R_1$ and $(y,z)\in R_2$</phrase>. Any $y$ satisfying this condition also satisfies <phrase>$(y,x)\in R_1^{-1}$ and $(z,y)\in R_2^{-1}$</phrase>, so by the definition of composition, $(z,x)\in R\_2^{-1}\circ R\_1^{-1}$ holds. The reverse direction can be shown similarly.

</details>

Furthermore, the composition of binary relations satisfies the associative law.

<div class="proposition" markdown="1">

<ins id="prop5">**Proposition 5**</ins> The composition of binary relations is associative. That is, for three binary relations $R\_1,R\_2,R\_3$,

$$(R_3\circ R_2)\circ R_1=R_3\circ(R_2\circ R_1)$$

holds.

</div>
<details class="proof" markdown="1">
<summary>Proof</summary>

It suffices to show that for any $(x,w)$, being an element of $(R\_3\circ R\_2)\circ R\_1$ is equivalent to being an element of $R\_3\circ(R\_2\circ R\_1)$.

First, $(x,w)\in (R\_3\circ R\_2)\circ R\_1$ is equivalent to <phrase>there exists some $y$ such that $(x,y)\in R_1$ and $(y,w)\in R_3\circ R_2$</phrase>. The latter condition is in turn equivalent to <phrase>there exists some $z$ such that $(y,z)\in R_2$ and $(z,w)\in R_3$</phrase>, so this condition is equivalent to <phrase>$(x,z)\in R_2\circ R_1$ and $(z,w)\in R_3$</phrase>. Therefore, this is equivalent to <phrase>$(x,w)\in R_3\circ(R_2\circ R_1)$</phrase>.

</details>

Therefore, we can express the common result $(R\_3\circ R\_2)\circ R\_1=R\_3\circ(R\_2\circ R\_1)$ as $R\_3\circ R\_2\circ R\_1$ without parentheses, without any problem.

The remaining propositions deal with how the image of a set changes under the inverse and composition of binary relations defined above.

<div class="proposition" markdown="1">

<ins id="prop6">**Proposition 6**</ins> Let $R\_1$, $R\_2$ be binary relations and $A$ be a set. Then

$$(R_2\circ R_1)(A)=R_2(R_1(A))$$

holds.

</div>
<details class="proof" markdown="1">
<summary>Proof</summary>

We proceed as in the previous proposition.

For any $z$, $z\in (R\_2\circ R\_1)(A)$ is equivalent to <phrase>there exists some $x\in X$ such that $(x,z)\in R_2\circ R_1$</phrase>. This is in turn equivalent to <phrase>there exists some $y$ such that $(x,y)\in R_1$ and $(y,z)\in R_2$</phrase>. Since $y\in R\_1(A)$, we have $z\in R\_2(R\_1(A))$. Reversing this logic gives the proof in the opposite direction.

</details>

<div class="proposition" markdown="1">

<ins id="prop7">**Proposition 7**</ins> Let $(R,A,B)$ be a binary relation, and let $X\subseteq A$ and $Y\subseteq B$. Then

1. $R^{-1}(R(X))\supset X\cap\pr_1R$  
2. $R(R^{-1}(Y))\supset Y\cap\pr_2R$  

hold respectively.

</div>
<details class="proof" markdown="1">
<summary>Proof</summary>

Before starting the proof in earnest, since the above two equations must hold for *all* $R$, they must also hold when $R^{-1}$ is substituted for $R$. Therefore, once we prove 1, statement 2 follows trivially from [Proposition 2](#prop2).

Now let $x\in X\cap\pr\_1R$. Then from $x\in\pr\_1R$, there exists some $y$ such that $(x,y)\in R$, and since $x\in X$, this $y$ satisfies $y\in R(X)$. Now since $(y,x)\in R^{-1}$, we have $x\in R^{-1}(R(X))$.

</details>

<div class="proposition" markdown="1">

<ins id="prop8">**Proposition 8**</ins> Let $R\_1$, $R\_2$ be binary relations. Then the following two equations hold:

$$ \pr_1(R_2\circ R_1)=R_1^{-1}(\pr_1R_2),\quad \pr_2(R_2\circ R_1)=R_2(\pr_2R_1).$$

</div>
<details class="proof" markdown="1">
<summary>Proof</summary>

This follows trivially from the following chain of implications:

$$\begin{aligned}
    x\in\pr_1(R_2\circ R_1)&\iff \exists z\big((x,z)\in R_2\circ R_1\big)\\
    &\iff\exists y,z\big(((x,y)\in R_1)\wedge((y,z)\in R_2)\big)\\
    &\iff\exists y\big(((x,y)\in R_1)\wedge(y\in\pr_1R_2)\big)\\
    &\iff x\in R_1^{-1}(\pr_1 R_2).
\end{aligned}$$

The second equation can be shown similarly.

</details>

Finally, we introduce a special binary relation.

<div class="definition" markdown="1">

<ins id="def9">**Definition 9**</ins> For a set $A$, $\Delta_A$ denotes the binary relation

$$\Delta_A=\{(x,x)\mid x\in A\}.$$

This is called the *diagonal* of $A\times A$.

</div>

By definition, $\pr_1\Delta_A=\pr_2\Delta_A=A$, so we can think of this as the binary relation

$$\left(\Delta_A,A,A\right).$$

In the next post, we can show that this relation becomes a function, called the *identity function* defined on set $A$. For a binary relation $R\_1$ having $A$ as source, or a binary relation $R\_2$ having $A$ as target, the two equations

$$R_1\circ\Delta_A=R_1,\qquad \Delta_A\circ R_2=R_2$$

always hold, so calling $(\Delta_A,A,A)$ the identity function is not awkward.

---
**References**

**[Bou]** N. Bourbaki, *Theory of Sets*. Elements of mathematics. Springer Berlin-Heidelberg, 2013.

---
