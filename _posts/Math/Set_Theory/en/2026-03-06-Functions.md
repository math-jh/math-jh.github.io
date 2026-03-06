---

title: "Functions"
excerpt: "Basic Definition of Functions"

categories: [Math / Set Theory]
permalink: /en/math/set_theory/functions
header:
    overlay_image: /assets/images/Math/Set_Theory/Functions.png
    overlay_filter: 0.5
sidebar: 
    nav: "set_theory-en"

date: 2026-03-06
last_modified_at: 2026-03-06
weight: 5

---

In previous posts, we defined binary relations. Under this definition, the binary relation $<$ defined on the set of natural numbers $\mathbb{N}$ is the set

$${<}=\{(0,1),(0,2),\ldots, (1,2),(1,3),\ldots, \}$$

![elements](/assets/images/Math/Set_Theory/Functions-1.png){:style="width:14em" class="invert" .align-center}

Following the notation of [§Binary Relation, ⁋Definition 7](/en/math/set_theory/binary_relation#def7), ${<}(1)$ is the collection of all $n\in\mathbb{N}$ such that $(1,n)\in\mathbb{N}$, hence

$${<}(1)=\{2,3,\ldots\}$$

Conversely, given the information about the set ${<}(k)$ for every natural number $k$, the set $<$ can be recovered.

The discussion above applies equally to general binary relations $(R,A,B)$. Thus a binary relation $R$ may be viewed precisely as a rule assigning the set $R(a)$ to each $a\in A$. In this light, a function is a binary relation for which $R(a)$ is a singleton set for every $a\in A$.

## Definition of a Function

<div class="definition" markdown="1">

<ins id="def1">**Definition 1**</ins> For a non-empty set $A$, a binary relation $f=(F,A,B)$ is called a *function* if $A=\pr_1F$ and for each $x\in A$, the set $F(\{x\})$ is a singleton set.[^1]

</div>

The condition $A=\pr_1F$ means that every element $x$ of $A$ corresponds to *at least* one $y\in B$; the second condition means that every $x\in A$ corresponds to *at most* one $y\in B$. Hence $f=(F,A,B)$ is a function precisely when:

> For every $x\in A$, there exists a *unique* $y\in B$ such that $(x,y)\in F$.

This $y$ is called the *value* of $f$ at $x$, and the unique element of $F(\{x\})$ is denoted by $f(x)$. The set $A=\pr_1F$ is called the *domain* of $f$.

In keeping with this notation, the image of a set $X\subseteq A$ under the binary relation $F$ is written $f(X)$ rather than $F(X)$, and the preimage of a set $Y\subseteq B$ is written $f^{-1}(Y)$ rather than $F^{-1}(Y)$. ([§Binary Relation, ⁋Definition 5](/en/math/set_theory/binary_relation#def5) and [§Operations on Binary Relations, ⁋Definition 1](/en/math/set_theory/operation_of_binary_relations#def1)) The triple $f=(F,A,B)$ is written more concisely as $f:A\rightarrow B$.

The set

$$F=\{(x,y)\mid (y=f(x))\wedge(x\in A)\}$$

representing a function $f=(F,A,B)$ may also be regarded as the *graph of the function* drawn on the "coordinate plane" $A\times B$. More generally, a binary relation $R$ may likewise be regarded as the *graph of the binary relation*. A function $f$ is a *constant function* if $f(x)=f(x')$ for all $x,x'\in \pr_1 F$.

In certain contexts, expressions such as $f_x$ are used to denote function values. Under this notation, the domain of $f$ is called the *index set*, and $F$ is called a *family*. When $f=(F,I,A)$ is regarded as a family, $F$ is denoted by $(f\_i)\_{i\in I}$.

If $f$ is a function from a set $A$ to itself, then $x\in A$ is *fixed* by $f$ if $f(x)=x$.

<div class="definition" markdown="1">

<ins id="def2">**Definition 2**</ins> For any set $A$, the *identity function* $\id_A$ is defined as the triple $(\Delta_A,A,A)$. That is, $\id_A$ is the function given by $f(x)=x$ for every $x\in A$.

</div>

By definition, $\id_A$ is the function that fixes every element of $A$.

## Commutative Diagrams

When working with multiple functions, the following *diagrams* prove convenient.

![commutative_diagram](/assets/images/Math/Set_Theory/Functions-2.png){:style="width:14em"  class="invert" .align-center}

Here $A\overset{f}{\longrightarrow}B$ is a convenient notation for $f:A\rightarrow B$.

In the situation above, if $(i\circ g)(x)=(j\circ h)(x)$ for every $x\in B$, then the square

![commuting_square](/assets/images/Math/Set_Theory/Functions-3.png){:style="width:10em" class="invert" .align-center}

is said to *commute*. Similarly, the diagram

![commuting_triangle](/assets/images/Math/Set_Theory/Functions-4.png){:style="width:6em"  class="invert" .align-center}

is a *commutative diagram* if $h(x)=(f\circ g)(x)$ for all $x$. This situation is sometimes expressed concisely as $h=f\circ g$, a notation which implies not only that $H=F\circ G$ holds but also that the sources and targets on both sides coincide.

When working with diagrams, it is understood that for each object $A$, the function $\id_A$ from $A$ to itself is present, even when not explicitly indicated by arrows. Thus strictly speaking, the commutativity of the triangle above means not only $h=f\circ g$ but also

$${\id_B}\circ h=f\circ g,\qquad h\circ{\id_C}=f\circ{\id_A}\circ g,\quad\cdots$$

However, by the properties of the identity function discussed in [§Operations on Binary Relations, ⁋Definition 9](/en/math/set_theory/operation_of_binary_relations#def9), the above equations are all equivalent to $h=f\circ g$. On the other hand,

![commuting_triangle_2](/assets/images/Math/Set_Theory/Functions-5.png){:style="width:6em" class="invert" .align-center}

commuting means that all three conditions

$${\id_A}=g\circ h\circ f,\quad {\id_B}=f\circ g\circ h,\quad {\id_C}=h\circ f\circ g$$

hold. In particular, the diagram

![inverses](/assets/images/Math/Set_Theory/Functions-6.png){:style="width:6em" class="invert" .align-center}

commuting means that $g\circ f=\id_A$ and $f\circ g=\id_B$.

## Extension and Restriction of Functions

<div class="definition" markdown="1">

<ins id="def3">**Definition 3**</ins> Two functions $f=(F,A,B),f'=(F',A',B')$ are *compatible* on a set $S$ if $S$ is contained in the domains of both $f$ and $f'$, and $f(x)=f'(x)$ for all $x\in S$.

</div>

Let $f$ and $f'$ be two functions, and suppose $S=\pr\_1 F\cap\pr\_1 F'$ is non-empty. If the two functions are compatible on $S$, then a new function $g$ with domain $\pr\_1F\cup\pr\_1F'$ can be defined by

$$g(x)=\begin{cases}f(x)&x\in \pr_1F\setminus\pr_1F'\\ f(x)=f'(x)&x\in \pr_1F\cap\pr_1F'\\ f'(x)&x\in\pr_1F'\setminus\pr_1F\end{cases}$$

This situation is captured in the following definition.

<div class="definition" markdown="1">

<ins id="def4">**Definition 4**</ins> Let $f=(F,A,B)$ and $f'=(F',A',B')$ be functions. If $F\subseteq F'$ and $B\subseteq B'$, then $f'$ is called an *extension* of $f$, and we say that $f'$ extends $f$.

</div>

Conversely, a function may be restricted to a smaller domain. Let $f=(F,A,B)$ be a function and let $X\subseteq A$. If we define the relation $R$ by

> $(x\mathrel{R} y)$ if and only if $((x\in X)\wedge(y=f(x)))$

then $R$, the collection of all $(x,y)$ satisfying this condition, is a function whose domain is $X$. This leads to the following definition.

<div class="definition" markdown="1">

<ins id="def5">**Definition 5**</ins> The function $g$ defined above is called the *restriction* of $f$ to $X$, and is denoted by $f\|_{X}$.

</div>



---
**References**

**[Bou]** N. Bourbaki, *Theory of Sets*. Elements of mathematics. Springer Berlin-Heidelberg, 2013.

---

[^1]: Strictly speaking, we have not yet defined the cardinality of a set, but this condition can be expressed as $x,y\in R(a)\implies x=y$, for instance.