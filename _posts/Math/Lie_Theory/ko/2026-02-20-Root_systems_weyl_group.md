---
title: "Weyl group과 대칭성"
excerpt: "Weyl group의 정의, finite group property"

categories: [Math / Lie Theory]
permalink: /ko/math/Lie_theory/root_systems_weyl_group
header:
    overlay_image: /assets/images/Math/Lie_Theory/Root_systems.png
    overlay_filter: 0.5
sidebar: 
    nav: "Lie_theory-ko"

date: 2026-02-20
last_modified_at: 2026-02-20
weight: 5

---

## Weyl group의 정의

Root system의 대칭성을 연구하는 데 있어 Weyl group은 핵심적인 역할을 한다. Weyl group은 root system의 reflection들에 의해 생성되는 유한군으로, root system의 분류와 표현론에서 중요한 도구가 된다.

<div class="definition" markdown="1">

<ins id="def1">**정의 1**</ins> Root system $\Phi \subset V$에 대하여, 각 root $\alpha \in \Phi$에 대한 reflection $s_\alpha \in \Aut(V)$를 고려하자:

$$s_\alpha(v) = v - 2\frac{(\alpha, v)}{(\alpha, \alpha)}\alpha.$$

*$\Phi$에 대한 Weyl group* $W(\Phi)$는 이 reflection들에 의해 생성되는 $V$의 linear transformation군이다:

$$W(\Phi) = \langle s_\alpha \mid \alpha \in \Phi \rangle \leq \Aut(V).$$

</div>

<div class="example" markdown="1">

<ins id="ex2">**예시 2**</ins> $A_1$ root system는 $\Phi = \{\pm \alpha\}$로 구성된다. 이 경우 Weyl group은 두 원소 $1$과 $s_\alpha$로 구성된 순서 2의 군이다. 이는 $\mathbb{Z}_2$와 동형이다.

</div>

<div class="proposition" markdown="1">

<ins id="prop3">**명제 3**</ins> Weyl group $W(\Phi)$는 항상 finite group이다. 즉, $W(\Phi)$는 유한개의 원소를 가진다.

</div>

<div class="proof" markdown="1">

<details class="proof" markdown="1">
<summary>증명</summary>

Root system $\Phi$가 finite-dimensional vector space $V$의 유한 부분집합이라는 사실을 이용한다. $W(\Phi)$는 $\Phi$의 reflection들에 의해 생성되므로, 각 reflection $s_\alpha$는 $V$ 위의 isometry이다. $\Phi$가 finite-dimensional이므로, $W(\Phi)$는 $\Aut(V)$의 finite subgroup이다. 더 엄밀하게는, $W(\Phi)$는 $V$의 lattice (예: root lattice)를 보존하는 linear transformations의 group으로, 이는 O(V)의 finite subgroup이다.

</details>
</div>

## Weyl group의 구조

<div class="lemma" markdown="1">

<ins id="lemma4">**보조정리 4**</ins> 임의의 root system $\Phi$에 대하여, Weyl group $W(\Phi)$는 $\Phi$의 모든 root를 보존한다. 즉, $w(\Phi) = \Phi$ for all $w \in W(\Phi)$.

</div>

<div class="proof" markdown="1">

<details class="proof" markdown="1">
<summary>증명</summary>

$\Phi$의 정의에 따르면, 각 reflection $s_\alpha$는 $\Phi$를 보존한다. 따라서 $W(\Phi)$의 생성원들이 $\Phi$를 보존하므로, $W(\Phi)$의 모든 원소도 $\Phi$를 보존한다.

</details>
</div>

<div class="proposition" markdown="1">

<ins id="prop5">**명제 5**</ins> Weyl group $W(\Phi)$는 $\Phi$의 positive root 집합 $\Phi^+$의 permutation group의 subgroup이다.

</div>

## Weyl group의 길이 함수

Weyl group의 구조를 이해하기 위해 길이 함수(length function)를 정의한다.

<div class="definition" markdown="1">

<ins id="def6">**정의 6**</ins> 임의의 $w \in W(\Phi)$에 대하여, $w$의 *길이* $\ell(w)$를 $w$를 표현하는 reflection의 최소 개수로 정의한다.

</div>

<div class="example" markdown="1">

<ins id="ex7">**예시 7**</ins> $A_2$ root system의 Weyl group은 정6각군 $D_6$와 동형이다. 길이 함수는 reflection의 수를 의미한다.

</div>

<div class="proposition" markdown="1">

<ins id="prop8">**명제 8**</ins> $W(\Phi)$의 각 원소 $w$는 unique한 minimal expression을 가진다. 즉, $w$를 reflection의 곱으로 표현할 때, 표현식의 길이는 고정되어 있다.

</div>

## Fundamental Domain과 chamber

<div class="definition" markdown="1">

<ins id="def9">**정의 9**</ins> Root system $\Phi$의 *fundamental chamber* $C$는 다음을 만족하는 open cone이다:

$$C = \{ v \in V \mid (\alpha, v) > 0 \text{ for all } \alpha \in \Delta \},$$

여기서 $\Delta$는 simple roots의 집합이다.

</div>

<div class="proposition" markdown="1">

<ins id="prop10">**명제 10**</ins> Weyl group $W(\Phi)$는 fundamental chamber $C$의 closure $\overline{C}$에 자유롭게 작용한다. 즉, 각 chamber $C_w = w(\overline{C})$는 $W(\Phi)$의 원소 $w$에 의해 서로 다르며, 이들의 union은 entire space $V$를覆盖한다.

</div>

<div class="proof" markdown="1">

<details class="proof" markdown="1">
<summary>증명</summary>

$\Phi$의 분류에 따르면, chamber의 수는 $|W|$와 같다. $W(\Phi)$가 chamber들을 mapping하므로, chamber의 수는 Weyl group의 order와 일치한다.

</details>
</div>

## Weyl group의 성질

<div class="theorem" markdown="1">

<ins id="thm11">**정리 11**</ins> Weyl group $W(\Phi)$는 유한 reflection group이다. 구체적으로, $W(\Phi)$는 다음과 같은 성질을 가진다:

1. $W(\Phi)$는 finite group이다.
2. $W(\Phi)$는 reflection group이다: 생성원들이 reflection이다.
3. $W(\Phi)$는 root system $\Phi$의 구조를 완전히 결정한다.

</div>

<div class="lemma" markdown="1">

<ins id="lemma12">**보조정리 12**</ins> 임의의 $w \in W(\Phi)$에 대하여, $w$의 고정점 공간(固定點空間)은 $W(\Phi)$의 reflection hyperplane들의 합집합의 여집합이다.

</div>

## Weyl group과 Dynkin diagram

<div class="proposition" markdown="1">

<ins id="prop13">**명제 13**</ins> Weyl group $W(\Phi)$는 Cartan matrix 또는 Dynkin diagram을 통해 명시적으로 계산할 수 있다. 각 Dynkin diagram type에 대해 Weyl group의 구조가 결정된다.

</div>

<div class="example" markdown="1">

<ins id="ex14">**예시 14**</ins> 각 classical type의 Weyl group은 다음과 같다:

- $A_n$: symmetric group $S_{n+1}$
- $B_n$: hyperoctahedral group $C_2 \wr S_n$
- $C_n$: hyperoctahedral group $C_2 \wr S_n$ (same as $B_n$)
- $D_n$: subgroup of $S_{2n}$ with even number of transpositions

</div>

## Weyl group의 표기법

<div class="definition" markdown="1">

<ins id="def15">**정의 15**</ins> Weyl group의 표준 표기법에서, 각 reflection $s_i = s_{\alpha_i}$는 simple root $\alpha_i$에 대한 reflection이다. $W(\Phi)$는 generator $s_1, \dots, s_n$과 relation $s_i^2 = 1$, $(s_i s_j)^{m_{ij}} = 1$로 표현된다.

</div>

<div class="proposition" markdown="1">

<ins id="prop16">**명제 16**</ins> $m_{ij}$의 값은 Cartan matrix $A$의 entry에 의해 결정된다:

$$m_{ij} = 
\begin{cases}
2 & \text{if } A_{ij} = 0 \\
3 & \text{if } A_{ij} = -1 \\
4 & \text{if } A_{ij} = -2 \\
6 & \text{if } A_{ij} = -3
\end{cases}$$

</div>

## Weyl group의 order

<div class="theorem" markdown="1">

<ins id="thm17">**정리 17**</ins> Weyl group $W(\Phi)$의 order는 root system의 구조에 의해 결정된다. 각 classical type에 대해 명시적인 공식이 존재한다:

1. $|W(A_n)| = (n+1)!$
2. $|W(B_n)| = |W(C_n)| = 2^n n!$
3. $|W(D_n)| = 2^{n-1} n!$

</div>

<div class="proof" markdown="1">

<details class="proof" markdown="1">
<summary>증명</summary>

이 공식들은 Weyl group의 permutation representation과 reflection 수를 이용하여 유도된다. 예를 들어, $A_n$ type의 경우 Weyl group은 $n+1$개의 요소의 symmetric group과 동일하므로 order는 $(n+1)!$이다.

</details>
</div>

<div class="example" markdown="1">

<ins id="ex18">**예시 18**</ins> $E_8$ root system의 Weyl group은 order가 696,729,600인 엄청난 규모의 유한군이다.

</div>

---

**참고문헌**

**[Humph]** J. E. Humphreys, *Introduction to Lie Algebras and Representation Theory*, Springer, 1972  
**[Var]** V. S. Varadarajan, *Lie Groups, Lie Algebras, and Their Representations*, Springer, 1984  
**[Knapp]** A. W. Knapp, *Lie Groups Beyond an Introduction*, Birkhäuser, 2002  
**[Bou]** N. Bourbaki, *Lie Groups and Lie Algebras: Chapters 4-6*, Springer, 2002
