---

title: "Retraction and Section"
excerpt: "Properties of Surjective and Injective Functions"

categories: [Math / Set Theory]
permalink: /en/math/set_theory/retraction_and_section
header:
    overlay_image: /assets/images/Math/Set_Theory/Retraction_and_section.png
    overlay_filter: 0.5
sidebar: 
    nav: "set_theory-en"

toc: false
toc_sticky: false

date: 2026-03-06
last_modified_at: 2026-03-06
weight: 7

---

The end of the previous post enables us to give new characterizations of injective and surjective functions. ([§Operations on Functions, ⁋Remark](/en/math/set_theory/operation_of_functions#rmk1))

<div class="proposition" markdown="1">

<ins id="prop1">**Proposition 1**</ins> Consider a function $$f:A\rightarrow B$$. If there exists $$r:B\rightarrow A$$ such that $$r\circ f=\id_A$$, then $$f$$ is injective. If there exists $$s:B\rightarrow A$$ such that $$f\circ s=\id_B$$, then $$f$$ is surjective.

Conversely, if $$f$$ is surjective, then there exists $$s:B\rightarrow A$$ such that $$f\circ s=\id_B$$, and if $$f$$ is injective, then there exists $$r:B\rightarrow A$$ such that $$r\circ f=\id_A$$.

</div>
<details class="proof" markdown="1">
<summary>Proof</summary>

The second part was already proved in the previous post, so we need only establish the first part. Suppose $$r\circ f=\id_A$$. If $$f(x)=f(y)$$, then

$$x=\id_{A}(x)=(r\circ f)(x)=r\circ(f(x))=r\circ(f(y))=(r\circ f)(y)=\id_{A}(y)=y$$

so $$f$$ is injective. Similarly, if $$f\circ s=\id_{B}$$, then for any $$y\in B$$,

$$y=\id_{B}(y)=(f\circ s)(y)=f(s(y))$$

so $$y\in f(A)$$, and hence $$f$$ is surjective.

</details>

Thus a function $$f:A\rightarrow B$$ is injective if and only if there exists $$r:B\rightarrow A$$ making the diagram

![injection](/assets/images/Math/Set_Theory/Retraction_and_section-1.png){:style="width:6em" class="invert" .align-center}

commute. A function $$f:A\rightarrow B$$ is surjective if and only if there exists $$s:B\rightarrow A$$ making the diagram

![surjection](/assets/images/Math/Set_Theory/Retraction_and_section-2.png){:style="width:6em" class="invert" .align-center}

commute. Such $$r$$ and $$s$$ have names.

<div class="definition" markdown="1">

<ins id="def2">**Definition 2**</ins> Let $$f$$ be an injective function from $$A$$ to $$B$$. A function $$r:B\rightarrow A$$ satisfying $$r\circ f=\id_A$$ is called a *retraction* of $$f$$.

If $$f$$ is a surjective function from $$A$$ to $$B$$, a function $$s:B\rightarrow A$$ satisfying $$f\circ s=\id_B$$ is called a *section* of $$f$$.

</div>

If $$f$$ is injective with retraction $$r$$, then $$f$$ may be viewed as a section of $$r$$; conversely, if $$f$$ is surjective with section $$s$$, then $$f$$ may be viewed as a retraction of $$s$$. Hence a retraction is surjective and a section is injective.

For a function $$f:A \rightarrow B$$ and subsets $$X\subseteq A$$, $$Y\subseteq B$$, the two inclusions

$$X\subseteq f^{-1}(f(X)),\qquad f(f^{-1}(Y))\subseteq Y$$

always hold, and the proofs are immediate. If $$f$$ is injective, then for $$r$$ defined as in [§Operations on Functions, ⁋Remark](/en/math/set_theory/operation_of_functions#rmk1),

$$f^{-1}(f(X))=r(f(X))=\id_A(X)=X$$

If $$f$$ is surjective, then for $$s$$ defined as in [§Operations on Functions, ⁋Remark](/en/math/set_theory/operation_of_functions#rmk1),

$$Y=\id_B(Y)=f(s(Y))\subseteq f(f^{-1}(Y))$$

so the above inclusions become equalities. The following proposition is straightforward to prove, but the results are worth remembering.

<div class="proposition" markdown="1">

<ins id="prop3">**Proposition 3**</ins> Let $$f:A\rightarrow B$$ and $$f':B\rightarrow C$$ be functions, and set $$f''=f'\circ f$$.

1. If $$f$$ and $$f'$$ are both injective, then so is $$f''$$.
   Moreover, if $$r$$ and $$r'$$ are retractions of $$f$$ and $$f'$$ respectively, then $$r\circ r'$$ is a retraction of $$f''$$.
2. If $$f$$ and $$f'$$ are both surjective, then so is $$f''$$.
   Moreover, if $$s$$ and $$s'$$ are sections of $$f$$ and $$f'$$ respectively, then $$s\circ s'$$ is a section of $$f''$$.
3. If $$f''$$ is injective, then $$f$$ is also injective.
   In particular, if $$r''$$ is a retraction of $$f''$$, then $$r''\circ f'$$ is a retraction of $$f$$.
4. If $$f''$$ is surjective, then $$f'$$ is also surjective.
   In particular, if $$s''$$ is a section of $$f''$$, then $$f\circ s''$$ is a section of $$f'$$.
</div>

<details class="proof" markdown="1">
<summary>Proof</summary>

1. Suppose $$f''(a_1)=f''(a_2)$$. Then $$f'(f(a_1))=f'(f(a_2))$$, and since $$f'$$ and $$f$$ are injective in succession, we obtain $$a_1=a_2$$. Hence $$f''$$ is injective.
    Now let $$r$$ and $$r'$$ be retractions of $$f$$ and $$f'$$ respectively, i.e., $$r\circ f=\id_A$$ and $$r'\circ f'=\id_B$$. Then for any $$a\in A$$,

      $$((r\circ r')\circ(f'\circ f))(a)=(r\circ\id_{B}\circ f)(a)=(r\circ f)(a)=\id_{A}(a)=a$$

    so $$r\circ r'$$ is a retraction of $$f''$$.

2. Let $$c\in C$$. Since $$f'$$ is surjective, there exists $$b\in B$$ with $$f'(b)=c$$. Since $$f$$ is surjective, there exists $$a\in A$$ with $$f(a)=b$$. Thus $$f''(a)=c$$, and $$f''$$ is surjective. Now let $$s$$ and $$s'$$ be sections of $$f$$ and $$f'$$ respectively. For any $$c\in C$$,

      $$((f'\circ f)\circ(s\circ s'))(c)=(f'\circ\id_{B}\circ s')(c)=(f'\circ s')(c)=\id_{C}(c)=c$$

    so $$s\circ s'$$ is a section of $$f''$$.

3. Let $$a_1$$, $$a_2\in A$$ and suppose $$f(a_1)=f(a_2)$$. Then $$f''(a_1)=f'(f(a_1))=f'(f(a_2))=f''(a_2)$$, and since $$f''$$ is injective, $$a_1=a_2$$. Hence $$f$$ is injective. For any $$a\in A$$,

     $$((r''\circ f')\circ f)(a)=(r''\circ f'')(a)=\id_A(a)=a $$

    so $$r''\circ f'$$ is a retraction of $$f$$.

4. Since $$f''$$ is surjective, for any $$c\in C$$ there exists $$a\in A$$ with $$f''(a)=c$$. Thus $$f'(f(a))=c$$, so $$f(a)=b\in B$$ satisfies $$f'(b)=c$$. Moreover, for any $$c\in C$$,

     $$(f'\circ(f\circ s''))(c)=(f''\circ s'')(c)=\id_C(c)=c.$$  

</details>

<div class="proposition" markdown="1">

<ins id="prop4">**Proposition 4**</ins>

1. Let $$A,B,C$$ be sets, and let $$g:A\rightarrow B$$ be a surjection and $$f:A\rightarrow C$$ a function. Then <phrase>there exists $$h:B\rightarrow C$$ with $$f=h\circ g$$</phrase> if and only if <phrase>$$(g(x)=g(y))\implies(f(x)=f(y))$$</phrase>.
   If these equivalent conditions hold, then $$h$$ satisfying $$f=h\circ g$$ is uniquely determined by $$f$$; moreover, if $$s$$ is a section of $$g$$, then $$h=f\circ s$$.
2. Let $$A,B,C$$ be sets, and let $$g:A\rightarrow B$$ be an injection and $$f:C\rightarrow B$$ a function. Then <phrase>there exists a function $$h:C\rightarrow A$$ such that $$f=g\circ h$$</phrase> if and only if <phrase>$$f(C)\subseteq g(A)$$</phrase>.
   If these equivalent conditions hold, then $$h$$ is uniquely determined by $$f$$; moreover, if $$r$$ is a retraction of $$g$$, then $$h=r\circ f$$.
</div>

The result in part 1 states that there exists $$h$$ making the diagram

![surjection](/assets/images/Math/Set_Theory/Retraction_and_section-3.png){:style="width:6em"  class="invert" .align-center}

commute. Part 2 states that there exists $$h$$ making the diagram

![injection](/assets/images/Math/Set_Theory/Retraction_and_section-4.png){:style="width:6em"  class="invert" .align-center}

commute.

<details class="proof--alone" markdown="1">
<summary>Proof of Proposition 4</summary>

1. Suppose $$f=h\circ g$$. If $$g(x)=g(y)$$, then

    $$ f(x)=(h\circ g)(x)=h(g(x))=h(g(y))=(h\circ g)(y)=f(y)$$

    so $$(g(x)=g(y))\implies(f(x)=f(y))$$ holds. We must prove the converse to establish the equivalence, and also show that when these conditions hold, $$h$$ is uniquely determined as $$h=f\circ s$$.
    First observe that if these conditions hold, $$h$$ must be unique. The value of $$h$$ is determined by its values on each $$y\in B$$. Since $$g$$ is surjective, for any section $$s$$ of $$g$$, we have $$s(y)=x$$ for some $$x$$. Then

    $$h(y)=(f\circ s)(y)=f(x)$$

    Even if another section $$s'$$ exists with $$s'(y)=x'$$, we have

    $$g(x)=g(s(y))=y=g(s'(y))=g(x')$$

    so by the second of the equivalent conditions, $$f(x)=f(x')$$. Hence $$h(y)$$ is independent of the choice of $$s$$. Thus $$h$$, if it exists, is unique.
    
    Now we prove the converse direction. Suppose $$(g(x)=g(y))\implies(f(x)=f(y))$$. Let $$s$$ be a section of $$g$$, and define $$h=f\circ s$$ as suggested by the uniqueness proof. For any $$x\in A$$,

    $$(h\circ g)(x)=((f\circ s)\circ g)(x)=f(s(g(x)))$$

    On the other hand,

    $$g(s(g(x)))=\id_B(g(x))=g(x)$$

    so by hypothesis $$f(s(g(x)))=f(x)$$. Hence $$h(g(x))=f(x)$$, and such an $$h$$ exists.

2. Suppose $$f=g\circ h$$. For any $$y\in f(C)$$, write $$y=f(x)$$; then $$y=f(x)=g(h(x))\in g(A)$$, so $$f(C)\subseteq g(A)$$ is immediate. As in part 1, we first establish uniqueness of $$h$$. Since $$h$$ is defined by the condition $$f=g\circ h$$, to show that $$h$$ has a uniquely determined value at each $$y\in G$$, it suffices to show that the right-hand side of

    $$h(y)=(\id_A\circ h)(y)=((r\circ g)\circ h)(y)=(r \circ f)(y)$$

    has the same value regardless of the choice of retraction $$r$$. Since $$r\circ g=r'\circ g=\id_A$$, for any $$g(x)\in g(A)$$ we have $$r(g(x))=x=r'(g(x))$$. That is, $$r\vert_{g(A)}=r'\vert_{g(A)}$$. By the second of the equivalent conditions, $$r$$ and $$r'$$ must agree on $$f(y)\in f(C)\subseteq g(A)$$. Hence $$h$$, if it exists, is unique.
    
    Now we prove the converse. Define $$h=r\circ f$$ as suggested by the uniqueness proof. If $$f(C)\subseteq g(A)$$, then for any $$x\in C$$,

    $$(g\circ h)(x)=(g\circ(r\circ f))(x)=(g\circ r)(f(x))$$

    Since $$f(x)\in f(C)\subseteq g(A)$$, write $$f(x)=g(y)$$. Then

    $$(g\circ r)(f(x))=(g\circ r)(g(y))=(g\circ(r\circ g))(y)=(g\circ\id_A)(y)=g(y)=f(x)$$

    so $$(g\circ h)(x)=f(x)$$ holds for all $$x\in C$$. Thus such an $$h$$ exists.

</details>



---
**References**

**[Bou]** N. Bourbaki, <i>Theory of Sets</i>. Elements of mathematics. Springer Berlin-Heidelberg, 2013.

---
