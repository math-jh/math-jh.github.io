---
title: "Root System의 분류"
excerpt: "A_n, B_n, C_n, D_n series, Cartan matrices, Dynkin diagrams"

categories: [Math / Lie Theory]
permalink: /ko/math/Lie_theory/root_systems_classification
header:
    overlay_image: /assets/images/Math/Lie_Theory/Root_systems.png
    overlay_filter: 0.5
sidebar: 
    nav: "Lie_theory-ko"

date: 2026-02-20
last_modified_at: 2026-02-20
weight: 4

---

## Root System의 분류

우리는 이제 root system의 분류 문제로 들어간다. 이 분류는 semisimple Lie 대수의 분류와 직접적으로 연결되며, 리 군과 리 대수의 구조를 이해하는 데 핵심적인 역할을 한다.

<div class="definition" markdown="1">

<ins id="def1">**정의 1**</ins> root system $\Phi$가 *irreducible*하다고 하면, $\Phi$를 더 작은 root system의 분리집합(direct sum)으로 표현할 수 없다는 의미이다. 즉, $\Phi$는 하나의 connected component로 이루어져 있다.

</div>

Irreducible root system의 분류는 Dynkin diagram의 분류와 정확히 일치한다.

<div class="theorem" markdown="1">

<ins id="thm2">**정리 2** (Dynkin의 분류)</ins> 모든 irreducible finite-dimensional root system은 다음의 종류들 중 하나입니다: 

1. **Classical types**: $A_n$, $B_n$, $C_n$, $D_n$ for $n \geq 1$.
2. **Exceptional types**: $E_6$, $E_7$, $E_8$, $F_4$, $G_2$.

여기서 $n$은 rank(기저의 원소 개수)를 의미한다.

</div>

## Classical Root Systems

### $A_n$ type

<div class="example" markdown="1">

<ins id="ex3">**예시 3**</ins> $A_n$ type은 $n+1$차원 공간에서 정의되며, $A_n$ root system은 다음과 같이 정의된다:

$$\Phi = \{e_i - e_j \mid 1 \leq i \neq j \leq n+1\} \subset \mathbb{R}^{n+1}.$$

기저 $\Delta$는 다음과 같은 $n$개의 simple root으로 구성된다:

$$\Delta = \{\alpha_1 = e_1 - e_2, \alpha_2 = e_2 - e_3, \dots, \alpha_n = e_n - e_{n+1}\}.$$

Cartan matrix $A$는 $n \times n$ 행렬로, $A_{ii} = 2$, $A_{i,i+1} = A_{i+1,i} = -1$, 그리고 나머지 원소는 $0$이다.

Dynkin diagram은 다음과 같은 형태이다: ○─○─○─...─○ ($n$개의 node).

</div>

<div class="proposition" markdown="1">

<ins id="prop4">**명제 4**</ins> $A_n$ root system은 $\mathfrak{su}(n+1)$의 근계와 동일하다. $\Phi$의 cardinality는 $n(n+1)$이며, positive root의 개수는 $\frac{n(n+1)}{2}$이다.

</div>

### $B_n$ type

<div class="example" markdown="1">

<ins id="ex5">**예시 5**</ins> $B_n$ type은 $n$차원 공간에서 정의되며, 다음과 같은 root system을 가진다:

$$\Phi = \{\pm e_i \pm e_j \mid 1 \leq i < j \leq n\} \cup \{\pm e_i \mid 1 \leq i \leq n\} \subset \mathbb{R}^n.$$

기저 $\Delta$는 다음과 같다:

$$\Delta = \{\alpha_1 = e_1 - e_2, \alpha_2 = e_2 - e_3, \dots, \alpha_{n-1} = e_{n-1} - e_n, \alpha_n = e_n\}.$$

Cartan matrix $A$는 $n \times n$ 행렬로, $A_{ii} = 2$, $A_{i,i+1} = A_{i+1,i} = -1$ for $i=1,\dots,n-1$, $A_{n,n-1} = -2$, 그리고 나머지 원소는 $0$이다.

Dynkin diagram은 다음과 같다: ○─○─○─...─○⇒○ (마지막 node는 black node).

</div>

<div class="proposition" markdown="1">

<ins id="prop6">**명제 6**</ins> $B_n$ root system은 $\mathfrak{so}(2n+1)$의 근계와 동일하다. $\Phi$의 cardinality는 $2n^2$이며, positive root의 개수는 $n^2$이다.

</div>

### $C_n$ type

<div class="example" markdown="1">

<ins id="ex7">**예시 7**</ins> $C_n$ type은 $n$차원 공간에서 정의되며, 다음과 같은 root system을 가진다:

$$\Phi = \{\pm e_i \pm e_j \mid 1 \leq i < j \leq n\} \cup \{\pm 2e_i \mid 1 \leq i \leq n\} \subset \mathbb{R}^n.$$

기저 $\Delta$는 다음과 같다:

$$\Delta = \{\alpha_1 = e_1 - e_2, \alpha_2 = e_2 - e_3, \dots, \alpha_{n-1} = e_{n-1} - e_n, \alpha_n = 2e_n\}.$$

Cartan matrix $A$는 $n \times n$ 행렬로, $A_{ii} = 2$, $A_{i,i+1} = A_{i+1,i} = -1$ for $i=1,\dots,n-1$, $A_{n,n-1} = -1$, 그리고 $A_{n,n-1}$이 $-2$가 아닌 점을 제외하면 $B_n$과 유사하다.

Dynkin diagram은 다음과 같다: ○─○─○─...─○⇐○ (마지막 node는 black node).

</div>

<div class="proposition" markdown="1">

<ins id="prop8">**명제 8**</ins> $C_n$ root system은 $\mathfrak{sp}(2n)$의 근계와 동일하다. $\Phi$의 cardinality는 $2n^2$이며, positive root의 개수는 $n^2$이다.

</div>

### $D_n$ type

<div class="example" markdown="1">

<ins id="ex9">**예시 9**</ins> $D_n$ type은 $n$차원 공간에서 정의되며, 다음과 같은 root system을 가진다:

$$\Phi = \{\pm e_i \pm e_j \mid 1 \leq i < j \leq n\} \subset \mathbb{R}^n.$$

기저 $\Delta$는 다음과 같다:

$$\Delta = \{\alpha_1 = e_1 - e_2, \alpha_2 = e_2 - e_3, \dots, \alpha_{n-1} = e_{n-1} - e_n, \alpha_n = e_{n-1} + e_n\}.$$

Cartan matrix $A$는 $n \times n$ 행렬로, $A_{ii} = 2$, $A_{i,i+1} = A_{i+1,i} = -1$ for $i=1,\dots,n-2$, $A_{n-1,n} = A_{n,n-1} = -1$, 그리고 $A_{n-1,n} = A_{n,n-1} = -1$이다.

Dynkin diagram은 다음과 같다: ○─○─○─...─○

```plaintext
    ○
   /
○─○─○─...─○
   \
    ○
```

</div>

<div class="proposition" markdown="1">

<ins id="prop10">**명제 10**</ins> $D_n$ root system은 $\mathfrak{so}(2n)$의 근계와 동일하다. $\Phi$의 cardinality는 $2n(n-1)$이며, positive root의 개수는 $n(n-1)$이다.

</div>

## Exceptional Root Systems

<div class="definition" markdown="1">

<ins id="def11">**정의 11**</ins> exceptional root system은 $E_6$, $E_7$, $E_8$, $F_4$, $G_2$로 분류된다. 이들은 classical types과는 다르게, 자연스럽게 등장하는 리 대수의 근계이지만, 상대적으로 복잡한 구조를 가진다.

</div>

<div class="example" markdown="1">

<ins id="ex12">**예시 12**</ins> $G_2$ type은 가장 간단한 exceptional root system으로, 6차원 공간에서 정의된다. $\Phi$는 12개의 root으로 구성되어 있다. 이들의 angles는 $30^\circ$, $60^\circ$, $90^\circ$, $150^\circ$ 등이 있다.

</div>

<div class="theorem" markdown="1">

<ins id="thm13">**정리 13**</ins> 모든 finite-dimensional irreducible root system은 $(A_n, B_n, C_n, D_n, E_6, E_7, E_8, F_4, G_2)$ 중 하나이다. 이 분류는 Dynkin diagram의 분류와 정확히 일치한다.

</div>

## Dynkin Diagrams

<div class="definition" markdown="1">

<ins id="def14">**정의 14**</ins> Root system의 *Dynkin diagram*은 기저 $\Delta$의 graph로, 각 node는 simple root를 나타내고, node 간의 edge는 두 simple root 사이의 각도에 따라 다음과 같이 연결된다:

- 각도가 $120^\circ$: single edge (○─○)
- 각도가 $135^\circ$: double edge (○═○)
- 각도가 $150^\circ$: triple edge (○≡○)

edge의 방향은 더 긴 root에서 더 짧은 root를 향한다.

</div>

<div class="proposition" markdown="1">

<ins id="prop15">**명제 15**</ins> Dynkin diagram은 root system의 구조를 완전히 결정한다. 즉, 두 root system이 같은 Dynkin diagram을 가지면, 그들은 isomorphic하다.

</div>

<div class="example" markdown="1">

<ins id="ex16">**예시 16**</ins> $A_3$의 Dynkin diagram은 ○─○─○이다. $D_4$의 Dynkin diagram은 center node에 세 개의 node가 연결된 모양이다.

</div>

## Cartan Matrix와 Dynkin Diagram의 관계

<div class="proposition" markdown="1">

<ins id="prop17">**명제 17**</ins> Cartan matrix $A$는 Dynkin diagram의 adjacency matrix와 유사하다. 구체적으로, $A_{ij}$는 node $i$와 node $j$ 사이의 connection type을 결정한다.

</div>

<div class="proof" markdown="1">

<details class="proof" markdown="1">
<summary>증명</summary>

Cartan matrix의 성질에 따르면, $A_{ij} \cdot A_{ji}$ 값에 따라 edge의 type이 결정된다:

- $A_{ij} = A_{ji} = -1$: single edge (○─○)
- $A_{ij} = -2, A_{ji} = -1$ 또는 그 반대: double edge (○═○)
- $A_{ij} = -3, A_{ji} = -1$ 또는 그 반대: triple edge (○≡○)

따라서 Cartan matrix는 Dynkin diagram의 모든 정보를 포함한다.

</details>
</div>

---

**참고문헌**

**[Humph]** J. E. Humphreys, *Introduction to Lie Algebras and Representation Theory*, Springer, 1972  
**[Var]** V. S. Varadarajan, *Lie Groups, Lie Algebras, and Their Representations*, Springer, 1984  
**[Knapp]** A. W. Knapp, *Lie Groups Beyond an Introduction*, Birkhäuser, 2002  
**[Ser]** J.-P. Serre, *Complex Semisimple Lie Algebras*, Springer, 2000
