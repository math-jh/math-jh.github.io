---
title: "Operations on Binary Relations"
description: "We define the inverse and composition of binary relations, prove properties of the inverse and the associativity of composition, and discuss a proposition about the inverse of the composition of two binary relations."
excerpt: "Inverse and Composition of Binary Relations"

categories: [Math / Set Theory]
permalink: /en/math/set_theory/operation_of_binary_relations


sidebar: 
    nav: "set_theory-en"

date: 2022-11-22

weight: 4
translated_at: 2026-06-02T19:00:02+00:00
translation_source: kimi-cli
last_polished_at: 2026-11-03T23:15:06+00:00
translation_polish_source: antigravity-gemini-3.8-flash-high
---
We now define the inverse of a binary relation, and their composition.

## Inverse of Binary Relations

::: Definition 1
Let $R$ be a binary relation. Then the binary relation consisting, for all $(x,y)\in R$, of all $(y,x)$ is called the *inverse* of $R$, and is denoted by $R^{-1}$. Also, the set $R^{-1}(X)$ is called the *preimage* of $X$. If $R^{-1}=R$, then $R$ is said to be *symmetric*.
:::

Explicitly, $R^{-1}$ is the set for which the formula

$$(x,y)\in R\iff (y,x)\in R^{-1}$$

holds. 

The set $R^{-1}(X)$ can be viewed either under the binary relation $R$ as the preimage of $X$, or under $R$'s inverse relation $R^{-1}$ as the image of $X$. However, by the definition of $R^{-1}$, whichever of these viewpoints we adopt yields the same set, so there is no room for confusion.

::: Proposition 2
The inverse of $R^{-1}$ is $R$. Moreover, $\pr_1R^{-1}=\pr_2R$ and $\pr_2R^{-1}=\pr_1R$.
:::
::: Proof
The first claim is immediate from the formula

$$(x,y)\in R\iff (y,x)\in R^{-1}\iff (x,y)\in (R^{-1})^{-1}$$ 

Consider the second claim. If $x\in\pr_1R^{-1}$, there exists some $y$ such that $(x,y)\in R^{-1}$. Since $(y,x)\in R$, it follows that $x\in\pr_2R$. Reversing this argument proves that $\pr_2R\subseteq\pr_1R^{-1}$.

For $\pr_2R^{-1}=\pr_1R$, which has not yet been shown, it suffices to replace $R$ by $R^{-1}$ in the claim just proved.   
:::

For given sets $A,B$, $A\times B$ was the largest binary relation having $A$ as source and $B$ as target. Thus, from the two formulas

$$\pr_1(A\times B)^{-1}=\pr_2(A\times B)=B,\qquad \pr_2(A\times B)^{-1}=\pr_1(A\times B)=A$$

we have $(A\times B)^{-1}\subseteq B\times A$. Conversely, if $(y,x)\in B\times A$, then $x\in A$ and $y\in B$, so $(x,y)\in A\times B$, and therefore $(y,x)\in (A\times B)^{-1}$; hence $(A\times B)^{-1}=B\times A$ holds.

## Composition of Binary Relations

::: Definition 3
Let $R_1$ and $R_2$ be binary relations. The *composition* $R_2\circ R_1$ of these two binary relations is the set consisting, whenever $(x,y)\in R_1$ and $(y,z)\in R_2$ for some $y$, of all ordered pairs $(x,z)$.
:::

It is natural to wonder how the composition of binary relations defined in this way relates to the inverse defined above.

::: Proposition 4
Let $R_1$, $R_2$ be binary relations. Then the inverse of $R_2\circ R_1$ is $R_1^{-1}\circ R_2^{-1}$.
:::
::: Proof
$(z,x)\in (R_2\circ R_1)^{-1}$ is equivalent to $(x,z)\in R_2\circ R_1$. This in turn is equivalent to the existence of some $y$ such that $(x,y)\in R_1$ and $(y,z)\in R_2$. A $y$ satisfying this condition also satisfies the condition that $(y,x)\in R_1^{-1}$ and $(z,y)\in R_2^{-1}$, so by the definition of composition, $(z,x)\in R_1^{-1}\circ R_2^{-1}$ holds. The converse direction can be shown in the same way.
:::

In addition, the composition of binary relations is associative.

::: Proposition 5
Composition of binary relations is associative. That is, for three binary relations $R_1,R_2,R_3$, 

$$(R_3\circ R_2)\circ R_1=R_3\circ(R_2\circ R_1)$$

holds.
:::
::: Proof
It suffices to show that for any $(x,w)$, being an element of $(R_3\circ R_2)\circ R_1$ is equivalent to being an element of $R_3\circ(R_2\circ R_1)$.  

First, $(x,w)\in (R_3\circ R_2)\circ R_1$ is equivalent to the existence of some $y$ such that $(x,y)\in R_1$ and $(y,w)\in R_3\circ R_2$. But the latter condition is again equivalent to the existence of some $z$ such that $(y,z)\in R_2$ and $(z,w)\in R_3$, so this condition is equivalent to $(x,z)\in R_2\circ R_1$ and $(z,w)\in R_3$. Therefore this is equivalent to $(x,w)\in R_3\circ(R_2\circ R_1)$.
:::

Therefore, there is no problem in expressing this common result $(R_3\circ R_2)\circ R_1=R_3\circ(R_2\circ R_1)$ without parentheses as $R_3\circ R_2\circ R_1$. 

Now, the remaining propositions deal with how the image of a set changes under the inverse of a binary relation and the composition of binary relations defined above.

::: Proposition 6
Let $R_1$, $R_2$ be binary relations and let $A$ be a set. Then

$$(R_2\circ R_1)(A)=R_2(R_1(A))$$

holds.
:::
::: Proof
We proceed as in the preceding proposition. 

For any $z$, the statement $z\in (R_2\circ R_1)(A)$ is equivalent to the existence of some $x\in A$ such that $(x,z)\in R_2\circ R_1$. But this is again equivalent to the existence of some $y$ such that $(x,y)\in R_1$ and $(y,z)\in R_2$. Since $y\in R_1(A)$, we have $z\in R_2(R_1(A))$. Reversing this logic gives the proof in the opposite direction.
:::

::: Proposition 7
Let $(R,A,B)$ be a binary relation, and let $X\subseteq A$, $Y\subseteq B$. Then 

1. $R^{-1}(R(X))\supset X\cap\pr_1R$  
2. $R(R^{-1}(Y))\supset Y\cap\pr_2R$  

hold, respectively.
:::
::: Proof
Before beginning the proof in earnest, since the two formulas above must hold for <em>all</em> $R$, they must also hold when substituting $R^{-1}$ in place of $R$. Therefore, once we show 1, 2 is immediate by [Proposition 2](#prop2){: data-lid="0ektm" }.  

Now let $x\in X\cap\pr_1R$. Then from $x\in\pr_1R$, there exists some $y$ such that $(x,y)\in R$, and since $x\in X$, this $y$ satisfies $y\in R(X)$. Now $(y,x)\in R^{-1}$, so $x\in R^{-1}(R(X))$.
:::

::: Proposition 8
Let $R_1$, $R_2$ be binary relations. Then the following two formulas hold:

$$\pr_1(R_2\circ R_1)=R_1^{-1}(\pr_1R_2),\quad \pr_2(R_2\circ R_1)=R_2(\pr_2R_1).$$
:::
::: Proof
This is immediate from the following chain of implications:

$$\begin{aligned}
    x\in\pr_1(R_2\circ R_1)&\iff \exists z\big((x,z)\in R_2\circ R_1\big)\\
    &\iff\exists y,z\big(((x,y)\in R_1)\wedge((y,z)\in R_2)\big)\\
    &\iff\exists y\big(((x,y)\in R_1)\wedge(y\in\pr_1R_2)\big)\\
    &\iff x\in R_1^{-1}(\pr_1 R_2).
\end{aligned}$$

The second formula can be shown similarly.
:::

Finally, we introduce a special binary relation.

::: Definition 9
For a set $A$, $\Delta_A$ denotes the binary relation

$$\Delta_A=\{(x,x)\mid x\in A\}$$

This is called the *diagonal* of $A\times A$.
:::

By definition $\pr_1\Delta_A=\pr_2\Delta_A=A$, so we may regard this as the binary relation

$$\left(\Delta_A,A,A\right)$$

In the next post we can show that this relation is a function, and we call it the *identity function* defined on the set $A$. For a binary relation $R_1$ having $A$ as source, or a binary relation $R_2$ having $A$ as target, the two formulas

$$R_1\circ\Delta_A=R_1,\qquad \Delta_A\circ R_2=R_2$$

always hold, so it is not unnatural to call $(\Delta_A,A,A)$ the identity function.

---
**References**

**[Bou]** N. Bourbaki, *Theory of Sets*. Elements of mathematics. Springer Berlin-Heidelberg, 2013.

---
