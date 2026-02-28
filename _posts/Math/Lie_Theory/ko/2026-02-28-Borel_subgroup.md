---
title: "Borel subgroup과 flag variety"
excerpt: "Dynkin diagram, ADE 분류, 그리고 flag variety"

categories: [Math / Lie Theory]
permalink: /ko/math/lie_theory/borel_subgroup
header:
    overlay_image: /assets/images/Math/Lie_Theory/Borel_subgroup.png
    overlay_filter: 0.5
sidebar: 
    nav: "Lie_theory-ko"

date: 2026-02-28
last_modified_at: 2026-02-28
weight: 4

---

[§근계](/ko/math/lie_theory/root_systems)에서 우리는 semisimple Lie algebra $\mathfrak{g}$의 root system $\Phi$를 정의하고, 그 대칭성을 Weyl group이 포착한다는 것을 확인하였다. 이 글에서는 root system의 구조를 통해 Lie algebra를 분류하고, 이로부터 자연스럽게 등장하는 기하적 대상인 flag variety를 소개한다.

## Dynkin diagram

Root system $\Phi$의 구조는 simple root들 사이의 관계로 완전히 결정된다. 이 관계를 시각화하는 도구가 Dynkin diagram이다.

<div class="definition" markdown="1">

<ins id="def1">**정의 1**</ins> Root system $\Phi$와 simple root들의 모임 $\Delta=\{\alpha_1,\ldots,\alpha_l\}$에 대하여, $\Phi$의 *Dynkin diagram*은 다음과 같이 정의되는 그래프이다.

1. 각 simple root $\alpha_i$에 대해 하나의 vertex를 둔다.
2. 두 vertex $\alpha_i$, $\alpha_j$ 사이에 $\lvert\langle\alpha_i,\alpha_j\rangle\rvert$개의 edge를 둔다.
3. 만일 $\lvert\alpha_i\rvert\neq\lvert\alpha_j\rvert$라면, 더 긴 root를 향하는 화살표를 edge에 추가한다.

</div>

[§근계, ⁋정의 16](/ko/math/lie_theory/root_systems#def16)에서 정의한 Cartan matrix $A=(a_{ij})$는 $a_{ij}=\langle\alpha_i,\alpha_j\rangle$이므로, Dynkin diagram은 Cartan matrix의 정보를 그래프로 표현한 것이라 생각할 수 있다. 특히 $a_{ij}\leq 0$이고 $a_{ij}=0$인 것은 $a_{ji}=0$인 것과 동치이므로, edge의 개수는 대칭적으로 결정된다.

<div class="example" markdown="1">

<ins id="ex2">**예시 2**</ins> [§근계, ⁋예시 13](/ko/math/lie_theory/root_systems#ex13)의 $\Phi(A_n)$을 생각하자. Simple root는 $\alpha_i=e_i-e_{i+1}$ ($1\leq i\leq n$)로 선택할 수 있다. 이들 사이의 내적을 계산하면

$$(\alpha_i,\alpha_j)=\begin{cases}2 & i=j\\ -1 & \lvert i-j\rvert=1\\ 0 & \text{otherwise}\end{cases}$$

이므로 $\langle\alpha_i,\alpha_j\rangle$은 $i=j$일 때 $2$, $\lvert i-j\rvert=1$일 때 $-1$, 그 외에는 $0$이다. 따라서 Dynkin diagram은 $n$개의 vertex가 chain으로 연결된 형태이며, 모든 root의 길이가 같으므로 화살표는 없다.

</div>

Dynkin diagram의 핵심 성질은 다음과 같다.

<div class="proposition" markdown="1">

<ins id="prop3">**명제 3**</ins> Dynkin diagram은 연결되어 있거나, 연결 성분들의 disjoint union으로 나타난다. 각 연결 성분은 irreducible root system에 대응한다.

</div>

<div class="proposition" markdown="1">

<ins id="prop4">**명제 4**</ins> Dynkin diagram에 cycle이 존재하지 않는다. 즉, Dynkin diagram은 항상 tree 혹은 forest이다.

</div>

## ADE 분류

이제 irreducible root system의 분류를 살펴보자. 핵심 결과는 Dynkin diagram의 가능한 형태가 완전히 분류된다는 것이다.

<div class="proposition" markdown="1">

<ins id="thm5">**정리 5**</ins> Irreducible root system의 Dynkin diagram은 다음 type들 중 하나이다.

1. **Classical types:**
   - $A_n$ ($n\geq 1$): $n$개의 vertex가 chain으로 연결
   - $B_n$ ($n\geq 2$): $A_n$의 한쪽 끝에 double edge와 화살표 추가
   - $C_n$ ($n\geq 2$): $A_n$의 한쪽 끝에 double edge와 반대 방향 화살표 추가
   - $D_n$ ($n\geq 4$): $A_{n-1}$의 한쪽 끝에서 분기

2. **Exceptional types:**
   - $E_6, E_7, E_8$: 각각 6, 7, 8개의 vertex를 갖는 특별한 형태
   - $F_4$: 4개의 vertex, 중간에 double edge
   - $G_2$: 2개의 vertex, triple edge

</div>

이 분류의 증명은 Dynkin diagram이 만족해야 할 조건들을 체계적으로 분석하는 것으로 이루어지며, 여기서는 생략한다.

<div class="example" markdown="1">

<ins id="ex6">**예시 6**</ins> 각 type에 대응하는 classical Lie algebra는 다음과 같다.

| Type | Lie algebra | Dimension |
|------|-------------|-----------|
| $A_n$ | $\mathfrak{sl}(n+1,\mathbb{C})$ | $n(n+2)$ |
| $B_n$ | $\mathfrak{so}(2n+1,\mathbb{C})$ | $n(2n+1)$ |
| $C_n$ | $\mathfrak{sp}(2n,\mathbb{C})$ | $n(2n+1)$ |
| $D_n$ | $\mathfrak{so}(2n,\mathbb{C})$ | $n(2n-1)$ |

Exceptional type들 $E_6, E_7, E_8, F_4, G_2$에 대응하는 Lie algebra들은 classical matrix algebra로 실현되지 않는다.

</div>

### Simply-laced root system

모든 root의 길이가 같은 root system을 *simply-laced*라 부른다.

<div class="definition" markdown="1">

<ins id="def7">**정의 7**</ins> Root system $\Phi$가 *simply-laced*라는 것은 모든 $\alpha,\beta\in\Phi$에 대해 $\lvert\alpha\rvert=\lvert\beta\rvert$인 것이다. Equivalently, Dynkin diagram에 double edge나 triple edge가 없는 것이다.

</div>

Simply-laced root system은 정확히 $A_n$, $D_n$, $E_6$, $E_7$, $E_8$ type이며, 이들을 통칭하여 *ADE type*이라 부른다. 이들은 여러 수학적 상황에서 특별한 성질을 갖는다.

## Borel subalgebra

이제 root system으로부터 자연스럽게 정의되는 Lie algebra의 subalgebra를 살펴보자. [§근계, ⁋정의 15](/ko/math/lie_theory/root_systems#def15)에서 positive root들의 모임 $\Phi^+$를 정의하였다.

<div class="definition" markdown="1">

<ins id="def8">**정의 8**</ins> Semisimple Lie algebra $\mathfrak{g}$, Cartan subalgebra $\mathfrak{h}$, 그리고 positive root들의 모임 $\Phi^+$에 대하여, *Borel subalgebra*는 다음의 subalgebra이다.

$$\mathfrak{b}=\mathfrak{h}\oplus\bigoplus_{\alpha\in\Phi^+}\mathfrak{g}_\alpha$$

</div>

Borel subalgebra는 $\mathfrak{g}$의 maximal solvable subalgebra이다. 이를 확인하기 위해 다음을 관찰하자.

<div class="proposition" markdown="1">

<ins id="prop9">**명제 9**</ins> Borel subalgebra $\mathfrak{b}$에 대하여 다음이 성립한다.

1. $\mathfrak{b}$는 solvable이다.
2. $\mathfrak{b}$는 $\mathfrak{g}$의 maximal solvable subalgebra이다.
3. $\mathfrak{b}$의 모든 conjugate은 어떤 Borel subalgebra이다.

</div>
<details class="proof" markdown="1">
<summary>증명</summary>

(1) $\mathfrak{b}$의 derived algebra는 $\mathfrak{n}=\bigoplus_{\alpha>0}\mathfrak{g}_\alpha$이고, $\mathfrak{n}$는 nilpotent이므로 solvable이다. 따라서 $\mathfrak{b}$도 solvable이다.

(2) $\mathfrak{b}$를 포함하는 solvable subalgebra $\mathfrak{s}$가 있다 하자. [§근계, ⁋명제 6](/ko/math/lie_theory/root_systems#prop6)에 의하여 $\mathfrak{s}$는 $\mathfrak{g}_\alpha$들의 direct sum 형태이어야 하고, solvable이므로 negative root를 포함할 수 없다. 따라서 $\mathfrak{s}=\mathfrak{b}$이다.

(3) 임의의 $g\in G$에 대하여 $\Ad(g)\mathfrak{b}$는 다시 maximal solvable subalgebra이고, 모든 maximal solvable subalgebra는 어떤 Borel subalgebra의 형태를 갖는다.

</details>

## Borel subgroup과 flag variety

이제 Lie group 관점으로 넘어가자. Complex semisimple Lie group $G_\mathbb{C}$에 대하여, Borel subalgebra $\mathfrak{b}$에 대응하는 Lie subgroup을 생각할 수 있다.

<div class="definition" markdown="1">

<ins id="def10">**정의 10**</ins> Complex semisimple Lie group $G_\mathbb{C}$의 *Borel subgroup* $B$는 Borel subalgebra $\mathfrak{b}$에 대응하는 connected Lie subgroup이다.

$$\mathfrak{b}=\Lie(B)$$

</div>

Borel subgroup $B$는 $G_\mathbb{C}$의 maximal connected solvable subgroup이다. 이제 quotient 공간을 정의하자.

<div class="definition" markdown="1">

<ins id="def11">**정의 11**</ins> Complex semisimple Lie group $G_\mathbb{C}$와 그 Borel subgroup $B$에 대하여, *flag variety*는 다음의 homogeneous space이다.

$$\mathcal{F}=G_\mathbb{C}/B$$

</div>

Flag variety라는 이름은 $\GL(n,\mathbb{C})$의 경우 $\mathcal{F}$가 $\mathbb{C}^n$의 complete flag들의 공간과 일치하기 때문에 붙여졌다.

<div class="example" markdown="1">

<ins id="ex12">**예시 12**</ins> $G_\mathbb{C}=\GL(n,\mathbb{C})$인 경우를 생각하자. Borel subgroup $B$는 upper triangular matrix들의 모임이고, flag variety $\GL(n,\mathbb{C})/B$는 $\mathbb{C}^n$의 complete flag

$$0=V_0\subset V_1\subset V_2\subset\cdots\subset V_n=\mathbb{C}^n,\qquad \dim V_i=i$$

들의 공간과 일대일대응된다. 구체적으로 $gB\in\GL(n,\mathbb{C})/B$는 flag $V_i=\span\{ge_1,\ldots,ge_i\}$에 대응한다.

</div>

## Compact form과의 연결

이제 compact Lie group $G$와 그 complexification $G_\mathbb{C}$ 사이의 관계를 살펴보자.

<div class="definition" markdown="1">

<ins id="def13">**정의 13**</ins> Complex Lie group $G_\mathbb{C}$의 *compact form*은 다음 조건을 만족하는 compact Lie group $G$이다.

1. $G$는 $G_\mathbb{C}$의 Lie subgroup이다.
2. $G$의 Lie algebra $\mathfrak{g}_0$는 $\mathfrak{g}$의 real form이다. 즉 $\mathfrak{g}=\mathfrak{g}_0\otimes_\mathbb{R}\mathbb{C}$이다.

</div>

모든 complex semisimple Lie group은 compact form을 갖는다. 예를 들어 $\SL(n,\mathbb{C})$의 compact form은 $\SU(n)$이고, $\SO(n,\mathbb{C})$의 compact form은 $\SO(n)$이다.

이제 핵심적인 결과를 서술한다.

<div class="proposition" markdown="1">

<ins id="prop14">**명제 14**</ins> Compact connected Lie group $G$와 그 complexification $G_\mathbb{C}$, maximal torus $T$, 그리고 대응하는 Borel subgroup $B$에 대하여, 다음의 inclusion

$$G/T\hookrightarrow G_\mathbb{C}/B$$

은 homotopy equivalence이다.

</div>
<details class="proof" markdown="1">
<summary>증명</summary>

$G_\mathbb{C}$의 Iwasawa decomposition $G_\mathbb{C}=G\cdot A\cdot N$을 생각하자. 여기서 $A$는 $T$의 complexification에 해당하는 diagonalizable subgroup이고, $N=\exp(\mathfrak{n})$는 $\mathfrak{n}=\bigoplus_{\alpha>0}\mathfrak{g}_\alpha$에 대응하는 unipotent subgroup이다.

Borel subgroup $B$는 $B=A\cdot N$으로 분해되며, 따라서

$$G_\mathbb{C}/B=G\cdot A\cdot N/A\cdot N\cong G/(G\cap A\cdot N)=G/T$$

이다. 더 정확히는 $G/T\to G_\mathbb{C}/B$가 deformation retraction을 유도한다.

</details>

이 결과는 compact Lie group 관점에서의 $G/T$와 complex Lie group 관점에서의 flag variety $G_\mathbb{C}/B$가 본질적으로 같은 대상임을 의미한다. 특히 $G/T$의 위상적 성질을 연구하기 위해 flag variety의 대수기하적 성질을 활용할 수 있다.

## Bruhat decomposition

마지막으로 $G_\mathbb{C}$의 중요한 분해를 소개한다.

<div class="proposition" markdown="1">

<ins id="prop15">**명제 15**</ins> Complex semisimple Lie group $G_\mathbb{C}$, Borel subgroup $B$, 그리고 Weyl group $W$에 대하여, 다음의 분해가 성립한다.

$$G_\mathbb{C}=\bigsqcup_{w\in W}BwB$$

이를 *Bruhat decomposition*이라 한다.

</div>

Bruhat decomposition은 flag variety $G_\mathbb{C}/B$의 cell decomposition을 제공한다. 각 $w\in W$에 대하여 $BwB/B$는 dimension $\ell(w)$의 affine space와 동형이고, 이들을 모으면 $G_\mathbb{C}/B$의 전체를 덮는다. 여기서 $\ell(w)$는 $w$의 *length*, 즉 $w$를 simple reflection들의 곱으로 표현할 때 필요한 최소 개수이다.

<div class="example" markdown="1">

<ins id="ex16">**예시 16**</ins> $G_\mathbb{C}=\GL(n,\mathbb{C})$인 경우, Weyl group $W\cong S_n$이고 각 permutation $\sigma\in S_n$에 대하여 $\ell(\sigma)$는 inversion의 개수이다. Bruhat decomposition에 의해 $\GL(n,\mathbb{C})/B$는 $0$차원 cell부터 $n(n-1)/2$차원 cell까지의 cell decomposition을 갖는다.

</div>

---

**참고문헌**

**[BtD]** Theodor Bröcker, Tammo tom Dieck, *Representations of Compact Lie Groups*, Graduate texts in mathematics, Springer, 1985.

**[Hum]** James E. Humphreys, *Linear Algebraic Groups*, Graduate texts in mathematics, Springer, 1975.

**[Spr]** T. A. Springer, *Linear Algebraic Groups*, Progress in mathematics, Birkhäuser, 1998.
