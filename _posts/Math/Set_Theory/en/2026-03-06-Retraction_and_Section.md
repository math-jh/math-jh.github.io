---
title: "Retraction and Section"
description: "We discuss the definitions of retractions for injective functions and sections for surjective functions, and show that these are respectively surjective and injective."
excerpt: "Properties of surjective and injective functions"

categories: [Math / Set Theory]
permalink: /en/math/set_theory/retraction_and_section
sidebar: 
    nav: "set_theory-en"

toc: false
toc_sticky: false

date: 2021-08-15
weight: 7
translated_at: 2026-06-02T12:00:01+00:00
translation_source: kimi-cli
last_polished_at: 2026-11-01T11:15:06+00:00
translation_polish_source: antigravity-gemini-3.8-flash-high
---
The end of the previous post enables us to give new definitions of injective and surjective functions. ([§Operations on Functions, ⁋Remark 6](/en/math/set_theory/operation_of_functions#rmk6){: data-lid="fwqv2" })

::: Proposition 1
Consider a function $f:A\rightarrow B$. If there exists some $r:B\rightarrow A$ such that $r\circ f=\id_A$, then $f$ is injective. Also, if there exists some $s:B\rightarrow A$ such that $f\circ s=\id_B$, then $f$ is surjective.  

Conversely, if $f$ is surjective, then there exists some $s:B\rightarrow A$ such that $f\circ s=\id_B$, and if $A\neq\emptyset$ and $f$ is injective, then there exists some $r:B\rightarrow A$ such that $r\circ f=\id_A$.
:::
::: Proof
The second part was already proved in the previous post. Therefore, we only need to show the first part. First, suppose $r\circ f=\id_A$. If $f(x)=f(y)$, then 

$$x=\id_{A}(x)=(r\circ f)(x)=r(f(x))=r(f(y))=(r\circ f)(y)=\id_{A}(y)=y$$ 

so $f$ is injective. Similarly, if $f\circ s=\id_{B}$, then for any $y\in B$,

$$y=\id_{B}(y)=(f\circ s)(y)=f(s(y))$$ 

so $y\in f(A)$, and therefore $f$ is surjective.
:::

Therefore, that a function $f:A\rightarrow B$ is injective means that there is $r:B\rightarrow A$ making the diagram 

{% diagram Math/Set_Theory/Retraction_and_Section-1.svg width="5.54em" alt="injection" %}

commute, and that $f:A\rightarrow B$ is surjective means that there is $s:B\rightarrow A$ making the diagram

{% diagram Math/Set_Theory/Retraction_and_Section-2.svg width="5.59em" alt="surjection" %}

commute. There are also names for $r,s$ satisfying these properties.

::: Definition 2
Let $f$ be an injective function from $A$ to $B$. Then, satisfying $r\circ f=\id_A$, a function $r:B\rightarrow A$ is called a *retraction* of $f$.  
If $f$ is a surjective function from $A$ to $B$, then, satisfying $f\circ s=\id_B$, a function $s:B\rightarrow A$ is called a *section* of $f$.
:::

If $f$ is an injective function and $r$ is a retraction, then $f$ can be viewed as a section of $r$, and conversely, if $f$ is a surjective function and $s$ is a section, then $f$ can also be viewed as a retraction of $s$. Therefore, a retraction is surjective and a section is injective.

Meanwhile, for a function $f:A \rightarrow B$ and $X\subseteq A, Y\subseteq B$, the following two expressions

$$X\subseteq f^{-1}(f(X)),\qquad f(f^{-1}(Y))\subseteq Y$$

always hold. Indeed, if $x\in X$, then $f(x)\in f(X)$, so $x\in f^{-1}(f(X))$, and if $y\in f(f^{-1}(Y))$, then there exists $x\in f^{-1}(Y)$ such that $y=f(x)$, so $y=f(x)\in Y$. If $f$ is injective, then for $r$ defined as in [§Operations on Functions, ⁋Remark 6](/en/math/set_theory/operation_of_functions#rmk6){: data-lid="fp9tu" },

$$f^{-1}(f(X))=r(f(X))=\id_A(X)=X$$

and if $f$ is surjective, then likewise for $s$ defined as in [§Operations on Functions, ⁋Remark 6](/en/math/set_theory/operation_of_functions#rmk6){: data-lid="uo8tg" },

$$Y=\id_B(Y)=f(s(Y))\subseteq f(f^{-1}(Y))$$

so the above expressions become equalities. The proofs of the following proposition are all not difficult, but the results are worth remembering.

::: Proposition 3
For two functions $f:A\rightarrow B$ and $f':B\rightarrow C$, let $f''=f'\circ f$.

1. If both $f$ and $f'$ are injective, then so is $f''$.  
   In this case, if $r$ and $r'$ are retractions of $f$ and $f'$ respectively, then $r\circ r'$ is a retraction of $f''$.
2. If both $f$ and $f'$ are surjective, then so is $f''$.  
   In this case, if $s$ and $s'$ are sections of $f$ and $f'$ respectively, then $s\circ s'$ is a section of $f''$.
3. If $f''$ is injective, then $f$ is also injective.  
   In particular, if $r''$ is a retraction of $f''$, then $r''\circ f'$ is a retraction of $f$.
4. If $f''$ is surjective, then $f'$ is also surjective.  
   In particular, if $s''$ is a section of $f''$, then $f\circ s''$ is a section of $f'$.
:::

::: Proof
1. First, suppose $f''(a_1)=f''(a_2)$. Then $f'(f(a_1))=f'(f(a_2))$, and applying the injectivity of $f'$ and then that of $f$ in order, we obtain $a_1=a_2$. That is, $f''$ is injective.  
    Now let $r$ and $r'$ be retractions of $f$ and $f'$ respectively, that is, $r\circ f=\id_A$ and $r'\circ f'=\id_B$. Then for any $a\in A$, 

      $$((r\circ r')\circ(f'\circ f))(a)=(r\circ\id_{B}\circ f)(a)=(r\circ f)(a)=\id_{A}(a)=a$$  
    
    so $r\circ r'$ is a retraction of $f''$.

2. Let $c\in C$. Then since $f'$ is surjective, there exists $b\in B$ such that $f'(b)=c$. Now since $f$ is again surjective, there exists $a\in A$ such that $f(a)=b$. Therefore $f''(a)=c$, and $f''$ is surjective. Now if $s$ and $s'$ are sections of $f$ and $f'$ respectively, then for any $c\in C$,

      $$((f'\circ f)\circ(s\circ s'))(c)=(f'\circ\id_{B}\circ s')(c)=(f'\circ s')(c)=\id_{C}(c)=c$$  
    
    so $s\circ s'$ is a section of $f''$.

3. For some $a_1$, $a_2\in A$, suppose $f(a_1)=f(a_2)$. Then $f''(a_1)=f'(f(a_1))=f'(f(a_2))=f''(a_2)$, and since $f''$ is injective, $a_1=a_2$. Therefore $f$ is also injective. Now for any $a\in A$,   

     $$((r''\circ f')\circ f)(a)=(r''\circ f'')(a)=\id_A(a)=a $$ 

    so $r''\circ f'$ is a retraction of $f$.

4. Since $f''$ is surjective, for any $c\in C$ there exists $a\in A$ such that $f''(a)=c$. Therefore $f'(f(a))=c$, so $f(a)=b\in B$ satisfies $f'(b)=c$. Also, for any $c\in C$,  

     $$(f'\circ(f\circ s''))(c)=(f''\circ s'')(c)=\id_C(c)=c$$

    so $f\circ s''$ is a section of $f'$.
:::

::: Proposition 4
1. Let $A,B,C$ be sets, and consider a surjection $g:A\rightarrow B$ and a function $f:A\rightarrow C$. Then the existence of $h:B\rightarrow C$ satisfying $f=h\circ g$ is equivalent to $(g(x)=g(y))\implies(f(x)=f(y))$ holding.  
   If these conditions are satisfied, then $h$ satisfying $f=h\circ g$ is uniquely determined by $f$, and if $s$ is a section of $g$, then $h=f\circ s$. 
2. Let $A,B,C$ be sets, and consider an injection $g:A\rightarrow B$ and a function $f:C\rightarrow B$. Then the existence of a function $h:C\rightarrow A$ such that $f=g\circ h$ is equivalent to $f(C)\subseteq g(A)$.  
   If these conditions are satisfied, then $h$ is uniquely determined by $f$, and if $r$ is a retraction of $g$, then $h=r\circ f$.
:::

The result of part 1 is that there exists $h$ making the following diagram

{% diagram Math/Set_Theory/Retraction_and_Section-3.svg width="5.94em" alt="surjection" %}

commute, and the case of part 2 is that there exists $h$ making the following diagram

{% diagram Math/Set_Theory/Retraction_and_Section-4.svg width="5.94em" alt="injection" %}

commute.

::: Proof (Proposition 4)
1. First, suppose $f=h\circ g$. If $g(x)=g(y)$, then  

    $$ f(x)=(h\circ g)(x)=h(g(x))=h(g(y))=(h\circ g)(y)=f(y)$$  

    so $(g(x)=g(y))\implies(f(x)=f(y))$ holds. We must show the converse direction of this proposition to show that these two conditions are equivalent, and also show that when these two equivalent conditions are satisfied, $h$ is uniquely determined as $h=f\circ s$.   
    First, let us observe that if these conditions are satisfied, $h$ must be unique.  
    The function $h$ is determined by its values at each element $y$ in $B$, and since $g$ is a surjection, for some section $s$ of $g$ we can have $s(y)=x$. Now  

    $$h(y)=h(g(s(y)))=(h\circ g)(s(y))=(f\circ s)(y)=f(x)$$  

    holds. Even if there exists another section $s'$ such that $s'(y)=x'$, since 

    $$g(x)=g(s(y))=y=g(s'(y))=g(x')$$  

    it follows from the latter of the equivalent conditions that $f(x)=f(x')$, and therefore the value of $h(y)$ is the same regardless of the choice of $s$. That is, $h$, if it exists, is unique.
      
    Now we must prove the converse direction of the given equivalence. Assume $(g(x)=g(y))\implies(f(x)=f(y))$. Let $s$ be a section of $g$, and taking a hint from the uniqueness proof, define $h=f\circ s$. Then for any $x\in A$,   

    $$(h\circ g)(x)=((f\circ s)\circ g)(x)=f(s(g(x)))$$  

    holds. On the other hand, since  

    $$g(s(g(x)))=\id_B(g(x))=g(x)$$  

    by the given condition we have $f(s(g(x)))=f(x)$. That is, since $h(g(x))=f(x)$, there exists $h$ satisfying the given condition.

2. First, suppose $f=g\circ h$. Then, for any $y\in f(C)$, if we let $y=f(x)$, since $y=f(x)=g(h(x))\in g(A)$, it is clear that $f(C)\subseteq g(A)$. As in the proof of 1, let us first show the uniqueness of $h$. Since $h$ is defined as a function satisfying $f=g\circ h$, to show that $h$ has a unique value for any $y\in C$, it suffices to show that the right-hand side of the equation  

    $$h(y)=(\id_A\circ h)(y)=((r\circ g)\circ h)(y)=(r \circ f)(y)$$  

    has the same value regardless of the choice of retraction $r$. However, since $r\circ g=r'\circ g=\id_A$, for any $g(x)\in g(A)$ we have $r(g(x))=x=r'(g(x))$. That is, $r\vert_{g(A)}=r'\vert_{g(A)}$. Now, by the latter of the equivalent conditions, $r$ and $r'$ must have the same value on $f(y)\in f(C)\subseteq g(A)$. Therefore, $h$, if it exists, is unique.  

    Now we must show the converse direction. Taking a hint from the uniqueness proof, define $h=r\circ f$. If $f(C)\subseteq g(A)$, then for any $x\in C$,   

    $$(g\circ h)(x)=(g\circ(r\circ f))(x)=(g\circ r)(f(x))$$  

    holds. However, since $f(x)\in f(C)\subseteq g(A)$, if we let $f(x)=g(y)$, then   

    $$(g\circ r)(f(x))=(g\circ r)(g(y))=(g\circ(r\circ g))(y)=(g\circ\id_A)(y)=g(y)=f(x)$$  

    so $(g\circ h)(x)=f(x)$ holds for all $x\in C$. That is, there exists $h$ satisfying the given condition.
:::



---
**References**

**[Bou]** N. Bourbaki, <i>Theory of Sets</i>. Elements of mathematics. Springer Berlin-Heidelberg, 2013.

---
