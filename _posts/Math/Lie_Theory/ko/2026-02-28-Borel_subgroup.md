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

[§근계](/ko/math/lie_theory/root_systems)에서 우리는 semisimple Lie algebra $\mathfrak{g}$의 root system $\Phi$를 정의하고, 그 대칭성을 Weyl group이 포착한다는 것을 확인하였다. 또한 [§원환면의 작용](/ko/math/lie_theory/torus_action)에서 compact Lie group $G$의 maximal torus $T$와 Weyl group $W=N(T)/T$의 관계를 살펴보았다. 이 글에서는 root system의 구조를 통해 Lie algebra를 분류하고, 이로부터 자연스럽게 등장하는 기하적 대상인 flag variety를 소개한다.

## Dynkin diagram

Root system $\Phi$의 구조는 simple root들 사이의 관계로 완전히 결정된다. [§근계, ⁋정의 16](/ko/math/lie_theory/root_systems#def16)에서 정의한 Cartan matrix는 이 관계를 행렬로 표현한 것이지만, 시각화를 통해 root system의 구조를 더 직관적으로 파악할 수 있다.

<div class="definition" markdown="1">

<ins id="def1">**정의 1**</ins> Root system $\Phi$와 simple root들의 모임 $\Delta=\{\alpha_1,\ldots,\alpha_l\}$에 대하여, $\Phi$의 *Dynkin diagram*은 다음과 같이 정의되는 그래프이다.

1. 각 simple root $\alpha_i$에 대해 하나의 vertex를 둔다.
2. 두 vertex $\alpha_i$, $\alpha_j$ ($i\neq j$) 사이에 $\lvert\langle\alpha_i,\alpha_j\rangle\rvert$개의 edge를 둔다.
3. 만일 $\lvert\alpha_i\rvert\neq\lvert\alpha_j\rvert$라면, 더 긴 root를 향하는 화살표를 edge에 추가한다.

</div>

Cartan matrix $A=(a_{ij})$에서 $a_{ij}=\langle\alpha_i,\alpha_j\rangle$이므로, Dynkin diagram은 Cartan matrix의 정보를 그래프로 표현한 것이라 생각할 수 있다. [§근계](/ko/math/lie_theory/root_systems)에서 살펴본 것과 같이 $a_{ij}\leq 0$이고 $a_{ij}=0$인 것은 $a_{ji}=0$인 것과 동치이므로, edge의 개수는 대칭적으로 결정된다. 또한 $a_{ij}\in\{0,-1,-2,-3\}$이므로 두 vertex 사이의 edge는 최대 3개이다.

<div class="example" markdown="1">

<ins id="ex2">**예시 2**</ins> [§근계, ⁋예시 13](/ko/math/lie_theory/root_systems#ex13)의 $\Phi(A_n)$을 생각하자. Simple root는 $\alpha_i=e_i-e_{i+1}$ ($1\leq i\leq n$)로 선택할 수 있다. 이들 사이의 내적을 계산하면

$$(\alpha_i,\alpha_j)=\begin{cases}2 & i=j\\ -1 & \lvert i-j\rvert=1\\ 0 & \text{otherwise}\end{cases}$$

이므로 $\langle\alpha_i,\alpha_j\rangle$은 $i=j$일 때 $2$, $\lvert i-j\rvert=1$일 때 $-1$, 그 외에는 $0$이다. 따라서 Dynkin diagram은 $n$개의 vertex가 chain으로 연결된 형태이며, 모든 root의 길이가 같으므로 화살표는 없다.

</div>

Dynkin diagram의 핵심 성질은 다음과 같다.

<div class="proposition" markdown="1">

<ins id="prop3">**명제 3**</ins> Dynkin diagram은 연결되어 있거나, 연결 성분들의 disjoint union으로 나타난다. 각 연결 성분은 irreducible root system에 대응한다.

</div>
<details class="proof" markdown="1">
<summary>증명</summary>

Dynkin diagram의 연결 성분들은 simple root들의 partition $\Delta=\Delta_1\sqcup\cdots\sqcup\Delta_k$를 정의한다. 각 $\Delta_i$로 생성되는 root subsystem $\Phi_i$를 생각하면, [§근계, ⁋명제 6](/ko/math/lie_theory/root_systems#prop6)에 의하여 서로 다른 $\Delta_i$에 속한 root들은 orthogonal이다. 따라서 $\Phi=\Phi_1\sqcup\cdots\sqcup\Phi_k$이고, 각 $\Phi_i$는 irreducible이다.

역으로 irreducible root system의 Dynkin diagram이 연결되어 있지 않다면 위의 논증에 의해 reducible이 되어 모순이다.

</details>

<div class="proposition" markdown="1">

<ins id="prop4">**명제 4**</ins> Dynkin diagram에 cycle이 존재하지 않는다. 즉, Dynkin diagram은 항상 tree 혹은 forest이다.

</div>
<details class="proof" markdown="1">
<summary>증명</summary>

귀류법으로 cycle $\alpha_{i_1},\ldots,\alpha_{i_k}=\alpha_{i_1}$이 존재한다 하자. Cycle 내의 edge 개수를 $k$라 하면, 각 edge에 대해 $\langle\alpha_{i_j},\alpha_{i_{j+1}}\rangle\neq 0$이고 따라서 $\langle\alpha_{i_j},\alpha_{i_{j+1}}\rangle\leq -1$이다.

이제 $\alpha=\sum_{j=1}^{k-1}\alpha_{i_j}$를 생각하자. 그럼

$$(\alpha,\alpha)=\sum_{j=1}^{k-1}(\alpha_{i_j},\alpha_{i_j})+2\sum_{j<\ell}(\alpha_{i_j},\alpha_{i_\ell})$$

이다. Cycle이므로 각 $\alpha_{i_j}$는 정확히 두 개의 이웃과 연결되어 있고, 따라서

$$(\alpha,\alpha)\leq 2(k-1)-2(k-1)=0$$

이다. 이는 inner product의 positive-definiteness에 모순이다.

</details>

<div class="proposition" markdown="1">

<ins id="prop5">**명제 5**</ins> Dynkin diagram에서 한 vertex에서 나가는 edge의 총 개수는 $4$를 넘지 않는다. 즉, 임의의 simple root $\alpha$에 대하여

$$\sum_{\beta\in\Delta,\beta\neq\alpha}\lvert\langle\alpha,\beta\rangle\rvert\leq 4$$

이다.

</div>
<details class="proof" markdown="1">
<summary>증명</summary>

Simple root $\alpha$에 수직인 초평면을 $H_\alpha$라 하자. $\alpha$와 이웃한 simple root들 $\beta_1,\ldots,\beta_m$을 생각하면, 각 $\beta_i$는 $H_\alpha$와 다른 각도를 이룬다. 

$\beta_i$를 $H_\alpha$에 정사영한 벡터들의 linear independence로부터 $m\leq 3$임을 보일 수 있다. 또한 각 $\beta_i$에 대해 $\lvert\langle\alpha,\beta_i\rangle\rvert\leq 3$이므로 총합은 $4$를 넘지 않는다.

</details>

## ADE 분류

이제 irreducible root system의 분류를 살펴보자. 앞선 명제들로부터 Dynkin diagram의 가능한 형태가 크게 제한된다.

<div class="proposition" markdown="1">

<ins id="thm6">**정리 6**</ins> Irreducible root system의 Dynkin diagram은 다음 type들 중 하나이다.

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

이 분류의 증명은 Dynkin diagram이 만족해야 할 조건들을 체계적으로 분석하는 것으로 이루어진다. 핵심 아이디어는 다음과 같다.

1. **Cycle이 없으므로** tree 형태여야 한다.
2. **Branching이 제한적이므로** 가능한 형태가 한정된다.
3. **Edge 개수의 제약으로부터** double edge와 triple edge의 위치가 결정된다.

자세한 증명은 생략하지만, 정리의 내용을 이해하는 데 있어 중요한 것은 각 type이 어떤 특징을 갖는지 아는 것이다.

<div class="example" markdown="1">

<ins id="ex7">**예시 7**</ins> 각 type에 대응하는 classical Lie algebra는 다음과 같다.

| Type | Lie algebra | Dimension |
|------|-------------|-----------|
| $A_n$ | $\mathfrak{sl}(n+1,\mathbb{C})$ | $n(n+2)$ |
| $B_n$ | $\mathfrak{so}(2n+1,\mathbb{C})$ | $n(2n+1)$ |
| $C_n$ | $\mathfrak{sp}(2n,\mathbb{C})$ | $n(2n+1)$ |
| $D_n$ | $\mathfrak{so}(2n,\mathbb{C})$ | $n(2n-1)$ |

Exceptional type들 $E_6, E_7, E_8, F_4, G_2$에 대응하는 Lie algebra들은 classical matrix algebra로 실현되지 않는다. 이들의 dimension은 각각 $78, 133, 248, 52, 14$이다.

</div>

### Simply-laced root system

모든 root의 길이가 같은 root system을 *simply-laced*라 부른다. 이들은 특별한 성질을 갖는다.

<div class="definition" markdown="1">

<ins id="def8">**정의 8**</ins> Root system $\Phi$가 *simply-laced*라는 것은 모든 $\alpha,\beta\in\Phi$에 대해 $\lvert\alpha\rvert=\lvert\beta\rvert$인 것이다. Equivalently, Dynkin diagram에 double edge나 triple edge가 없는 것이다.

</div>

Simply-laced root system은 정확히 $A_n$, $D_n$, $E_6$, $E_7$, $E_8$ type이며, 이들을 통칭하여 *ADE type*이라 부른다. ADE type은 다양한 수학적 상황에서 등장한다. 가령 du Val singularity의 분류, Platonic solid의 대칭군, 그리고 2차원 conformal field theory 등에서 ADE pattern이 나타난다.

## Borel subalgebra

이제 root system으로부터 자연스럽게 정의되는 Lie algebra의 subalgebra를 살펴보자. [§근계, ⁋정의 15](/ko/math/lie_theory/root_systems#def15)에서 positive root들의 모임 $\Phi^+$를 정의하였다. 이는 Weyl chamber를 하나 선택하는 것과 같으며, 이로부터 Lie algebra의 특별한 subalgebra를 정의할 수 있다.

<div class="definition" markdown="1">

<ins id="def9">**정의 9**</ins> Semisimple Lie algebra $\mathfrak{g}$, Cartan subalgebra $\mathfrak{h}$, 그리고 positive root들의 모임 $\Phi^+$에 대하여, *Borel subalgebra*는 다음의 subalgebra이다.

$$\mathfrak{b}=\mathfrak{h}\oplus\bigoplus_{\alpha\in\Phi^+}\mathfrak{g}_\alpha$$

이 때 $\mathfrak{n}=\bigoplus_{\alpha>0}\mathfrak{g}_\alpha$를 $\mathfrak{b}$의 *nilradical*이라 한다.

</div>

Borel subalgebra는 positive root들에 해당하는 root space들을 모두 포함하며, Cartan subalgebra를 포함하는 가장 큰 "upper triangular" 형태의 subalgebra로 생각할 수 있다.

<div class="proposition" markdown="1">

<ins id="prop10">**명제 10**</ins> Borel subalgebra $\mathfrak{b}$에 대하여 다음이 성립한다.

1. $\mathfrak{b}$는 solvable이다.
2. $\mathfrak{b}$는 $\mathfrak{g}$의 maximal solvable subalgebra이다.
3. $\mathfrak{b}$의 모든 conjugate은 어떤 Borel subalgebra이다. 즉, 임의의 $g\in G$에 대하여 $\Ad(g)\mathfrak{b}$는 어떤 positive system $\Phi'^+$에 대한 Borel subalgebra이다.

</div>
<details class="proof" markdown="1">
<summary>증명</summary>

(1) $\mathfrak{b}$의 derived series를 생각하자. $\mathfrak{b}^{(1)}=[\mathfrak{b},\mathfrak{b}]=\mathfrak{n}$이고, $\mathfrak{n}$은 nilpotent이므로 $\mathfrak{b}$는 solvable이다. 구체적으로 $\mathfrak{n}$은 strictly upper triangular matrix들의 algebra와 유사한 구조를 갖는다.

(2) $\mathfrak{b}$를 포함하는 solvable subalgebra $\mathfrak{s}$가 있다 하자. Root decomposition에 의하여 $\mathfrak{s}=\mathfrak{h}\oplus\bigoplus_{\alpha\in S}\mathfrak{g}_\alpha$의 꼴이어야 한다. 만일 $S$가 어떤 positive root를 포함하지 않는다면 $\mathfrak{s}\subset\mathfrak{b}$이고, 만일 $S$가 negative root를 포함한다면 $\mathfrak{s}$는 더 이상 solvable이 아니다. 따라서 $\mathfrak{s}=\mathfrak{b}$이다.

(3) $\Ad(g)\mathfrak{b}$는 다시 maximal solvable subalgebra이므로, 위의 (2)에 의하여 어떤 positive system에 대한 Borel subalgebra이다.

</details>

## Borel subgroup과 flag variety

이제 Lie group 관점으로 넘어가자. Complex semisimple Lie group $G_\mathbb{C}$에 대하여, Borel subalgebra $\mathfrak{b}$에 대응하는 Lie subgroup을 생각할 수 있다.

<div class="definition" markdown="1">

<ins id="def11">**정의 11**</ins> Complex semisimple Lie group $G_\mathbb{C}$의 *Borel subgroup* $B$는 Borel subalgebra $\mathfrak{b}$에 대응하는 connected Lie subgroup이다.

$$\mathfrak{b}=\Lie(B)$$

</div>

Borel subgroup $B$는 $G_\mathbb{C}$의 maximal connected solvable subgroup이다. 이제 quotient 공간을 정의하자.

<div class="definition" markdown="1">

<ins id="def12">**정의 12**</ins> Complex semisimple Lie group $G_\mathbb{C}$와 그 Borel subgroup $B$에 대하여, *flag variety*는 다음의 homogeneous space이다.

$$\mathcal{F}=G_\mathbb{C}/B$$

</div>

Flag variety라는 이름은 $\GL(n,\mathbb{C})$의 경우 $\mathcal{F}$가 $\mathbb{C}^n$의 complete flag들의 공간과 일치하기 때문에 붙여졌다. 일반적으로 flag variety는 projective variety이며, 이는 $G_\mathbb{C}$의 representation theory와 깊은 관계를 갖는다.

<div class="example" markdown="1">

<ins id="ex13">**예시 13**</ins> $G_\mathbb{C}=\GL(n,\mathbb{C})$인 경우를 생각하자. Borel subgroup $B$는 upper triangular matrix들의 모임이고, flag variety $\GL(n,\mathbb{C})/B$는 $\mathbb{C}^n$의 complete flag

$$0=V_0\subset V_1\subset V_2\subset\cdots\subset V_n=\mathbb{C}^n,\qquad \dim V_i=i$$

들의 공간과 일대일대응된다. 구체적으로 $gB\in\GL(n,\mathbb{C})/B$는 flag $V_i=\span\{ge_1,\ldots,ge_i\}$에 대응한다. 이 공간은 다음의 embedding

$$\GL(n,\mathbb{C})/B\hookrightarrow\mathbb{P}(\wedge^1\mathbb{C}^n)\times\mathbb{P}(\wedge^2\mathbb{C}^n)\times\cdots\times\mathbb{P}(\wedge^{n-1}\mathbb{C}^n)$$

을 통해 projective variety로 실현된다.

</div>

## Compact form과의 연결

이제 compact Lie group $G$와 그 complexification $G_\mathbb{C}$ 사이의 관계를 살펴보자. 이 연결은 두 관점 — compact group의 $G/T$와 complex group의 $G_\mathbb{C}/B$ — 사이의 bridge를 제공한다.

<div class="definition" markdown="1">

<ins id="def14">**정의 14**</ins> Complex Lie group $G_\mathbb{C}$의 *compact form*은 다음 조건을 만족하는 compact Lie group $G$이다.

1. $G$는 $G_\mathbb{C}$의 Lie subgroup이다.
2. $G$의 Lie algebra $\mathfrak{g}_0$는 $\mathfrak{g}$의 real form이다. 즉 $\mathfrak{g}=\mathfrak{g}_0\otimes_\mathbb{R}\mathbb{C}$이다.
3. $\mathfrak{g}_0$ 위에서 Killing form은 negative definite이다.

</div>

모든 complex semisimple Lie group은 compact form을 갖는다. 예를 들어 $\SL(n,\mathbb{C})$의 compact form은 $\SU(n)$이고, $\SO(n,\mathbb{C})$의 compact form은 $\SO(n)$이며, $\Sp(2n,\mathbb{C})$의 compact form은 $\Sp(n)=\Sp(2n,\mathbb{C})\cap\U(2n)$이다.

이제 핵심적인 결과를 서술한다.

<div class="proposition" markdown="1">

<ins id="prop15">**명제 15**</ins> Compact connected Lie group $G$와 그 complexification $G_\mathbb{C}$, maximal torus $T\subset G$, 그리고 대응하는 Borel subgroup $B\subset G_\mathbb{C}$에 대하여, 다음의 inclusion

$$G/T\hookrightarrow G_\mathbb{C}/B$$

은 homotopy equivalence이다. 특히 $G/T$와 $G_\mathbb{C}/B$는 같은 cohomology를 갖는다.

</div>
<details class="proof" markdown="1">
<summary>증명</summary>

$G_\mathbb{C}$의 Iwasawa decomposition $G_\mathbb{C}=G\cdot A\cdot N$을 생각하자. 여기서

- $A$는 $T$의 complexification에 해당하는 diagonalizable subgroup으로, $\mathfrak{a}=\mathfrak{t}\otimes_\mathbb{R}\mathbb{R}$에 의해 결정된다.
- $N=\exp(\mathfrak{n})$는 $\mathfrak{n}=\bigoplus_{\alpha>0}\mathfrak{g}_\alpha$에 대응하는 unipotent subgroup이다.

Borel subgroup $B$는 $B=A\cdot N$으로 분해되며, $G\cap B=T$이다. 이제 다음의 chain을 생각하자.

$$G/T\hookrightarrow G_\mathbb{C}/B=(G\cdot A\cdot N)/(A\cdot N)\cong G/(G\cap A\cdot N)=G/T$$

첫 번째 inclusion은 $G\hookrightarrow G_\mathbb{C}$로부터 유도되며, composition이 $G/T$의 identity map이므로 이 inclusion은 homotopy equivalence이다.

더 정확히는 $A\cdot N\cong\mathbb{R}^n$이므로 $G_\mathbb{C}/B\to G/T$는 deformation retraction을 유도한다.

</details>

이 결과는 compact Lie group 관점에서의 $G/T$와 complex Lie group 관점에서의 flag variety $G_\mathbb{C}/B$가 본질적으로 같은 대상임을 의미한다. 특히 $G/T$의 위상적 성질 — cohomology, homotopy group 등 — 을 연구하기 위해 flag variety의 대수기하적 성질을 활용할 수 있다.

## Bruhat decomposition

마지막으로 $G_\mathbb{C}$의 중요한 분해를 소개한다. 이 분해는 flag variety의 cell structure를 이해하는 데 핵심적이다.

<div class="proposition" markdown="1">

<ins id="prop16">**명제 16**</ins> Complex semisimple Lie group $G_\mathbb{C}$, Borel subgroup $B$, 그리고 Weyl group $W$에 대하여, 다음의 분해가 성립한다.

$$G_\mathbb{C}=\bigsqcup_{w\in W}BwB$$

이를 *Bruhat decomposition*이라 한다. 각 double coset $BwB$는 $G_\mathbb{C}$에서 locally closed subset이며, 그 closure는 다음과 같이 주어진다.

$$\overline{BwB}=\bigcup_{v\leq w}BvB$$

여기서 $\leq$는 Weyl group 위의 Bruhat order이다.

</div>
<details class="proof" markdown="1">
<summary>증명</summary>

우선 $G_\mathbb{C}=\bigcup_{w\in W}BwB$임을 보이자. 임의의 $g\in G_\mathbb{C}$에 대하여, $g^{-1}B\cap T\neq\emptyset$인지 확인한 후, Weyl group의 원소를 이용하여 $g$를 적절한 double coset으로 보낼 수 있다.

Disjointness를 보기 위해, $BwB=BvB$라 하자. 그럼 $wBw^{-1}=vBv^{-1}$이고, 이로부터 $w^{-1}v\in N(T)$이며 $w^{-1}v$는 $B$를 normalize한다. 그런데 $B\cap N(T)=T$이므로 $w^{-1}v\in T$이고, 따라서 $w=v$ in $W$이다.

Closure에 대한 진술은 Bruhat order의 정의로부터 따라나온다.

</details>

Bruhat decomposition은 flag variety $G_\mathbb{C}/B$의 cell decomposition을 제공한다. 각 $w\in W$에 대하여 $X_w=BwB/B$는 dimension $\ell(w)$의 affine space와 동형이고, 이들을 모으면 $G_\mathbb{C}/B$의 전체를 덮는다. 여기서 $\ell(w)$는 $w$의 *length*, 즉 $w$를 simple reflection들의 곱으로 표현할 때 필요한 최소 개수이다.

<div class="example" markdown="1">

<ins id="ex17">**예시 17**</ins> $G_\mathbb{C}=\GL(n,\mathbb{C})$인 경우, Weyl group $W\cong S_n$이고 각 permutation $\sigma\in S_n$에 대하여 $\ell(\sigma)$는 inversion의 개수이다. 

구체적으로 $\sigma$의 inversion은 $i<j$이면서 $\sigma(i)>\sigma(j)$인 쌍 $(i,j)$의 개수이다. Bruhat decomposition에 의해 $\GL(n,\mathbb{C})/B$는 $0$차원 cell (identity permutation, inversion $0$개)부터 $n(n-1)/2$차원 cell (reverse permutation, inversion 최대)까지의 cell decomposition를 갖는다.

이 cell decomposition로부터 $\GL(n,\mathbb{C})/B$의 cohomology를 계산할 수 있으며, 그 Betti number는 Weyl group의 Bruhat order에 의해 결정된다.

</div>

---

**참고문헌**

**[BtD]** Theodor Bröcker, Tammo tom Dieck, *Representations of Compact Lie Groups*, Graduate texts in mathematics, Springer, 1985.

**[Hum]** James E. Humphreys, *Linear Algebraic Groups*, Graduate texts in mathematics, Springer, 1975.

**[Spr]** T. A. Springer, *Linear Algebraic Groups*, Progress in mathematics, Birkhäuser, 1998.
