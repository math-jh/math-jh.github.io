---
title: "Root system의 torus action 해석"
excerpt: "Lie algebra 대신 Cartan torus action으로 root system, Dynkin diagram, ADE classification을 이해하기"

categories: [Math / Lie Groups]
permalink: /ko/math/lie_groups/torus_root_system
header:
    overlay_image: /assets/images/Math/Lie_Theory/Torus_Root_Systems.png
    overlay_filter: 0.5
sidebar: 
    nav: "Lie_theory-ko"

date: 2026-02-23
last_modified_at: 2026-02-23
weight: 3
---

## 1. 서론: Torus action으로의 관점 전환

Lie algebra의 root system은 본질적으로 **Cartan torus의 representation theory**에서 자연스럽게 등장합니다. 이 글에서는 Lie algebra의 관점이 아닌, **torus action**으로 root system을 재해석하고, 이를 통해 Dynkin diagram과 ADE classification을 자연스럽게 도출해냅니다.

기존의 Lie algebra 중심 접근법:
- Root system = $\mathfrak{g}$의 decomposition
- Root = $\mathfrak{h}^*$의 원소

새로운 torus action 중심 접근법:
- Root system = Cartan torus $T$ action의 eigenvalue spectrum
- Root = torus action의 weight (character)

---

## 2. Cartan torus와 torus action

### 2.1 Cartan torus의 정의

Semisimple Lie algebra $\mathfrak{g}$와 그의 Cartan subalgebra $\mathfrak{h}$에 대하여, 우리는 다음과 같은 관계를 압니다:

<div class="definition" markdown="1">

<ins id="def1">**정의 1**</ins> Cartan torus $T$는 Cartan subalgebra $\mathfrak{h}$의 exponential image로 정의됩니다:

$$T = \exp(\mathfrak{h}) \cong \mathfrak{h}/\Lambda \cong (S^1)^r$$

where $\Lambda$ is the lattice of integral elements in $\mathfrak{h}$.

</div>

### 2.2 Torus action의 자연스러운 등장

Lie group $G$가 주어졌을 때, 자연스러운 torus action이 있습니다:

<div class="definition" markdown="1">

<ins id="def2">**정의 2**</ins> $G$의 **Cartan torus** $T$는 $G$의 maximal torus로, $T$의 adjoint action:

$$\Ad: T \times \mathfrak{g} \to \mathfrak{g}, \quad (t, X) \mapsto tXt^{-1}$$

을 consideration합니다.

</div>

이 action은 $\mathfrak{g}$를 $T$-module로 만듭니다.

---

## 3. Weight decomposition과 root system의 torus action 해석

### 3.1 Weight decomposition

Torus $T$의 representations는 모든 irreducible component가 1차원이라는 사실을 이용합니다. $\mathfrak{g}$의 adjoint representation을 $T$-module로 보자면:

<div class="definition" markdown="1">

<ins id="def3">**정의 3**</ins> $\mathfrak{g}$의 $T$-module structure에서, 각각의 weight $\lambda \in \mathfrak{h}^*$에 대하여:

$$\mathfrak{g}_\lambda = \{ X \in \mathfrak{g} \mid t \cdot X = \lambda(t) X \text{ for all } t \in T \}$$

을 **weight space**라 합니다. 여기서 $\lambda(t) = e^{2\pi i \lambda(\log t)}$입니다.

</div>

### 3.2 Root system의 torus action적 의미

기존의 root definition:

$$\mathfrak{g}_\alpha = \{ X \in \mathfrak{g} \mid [H, X] = \alpha(H) X \text{ for all } H \in \mathfrak{h} \}$$

이제 이는 torus action에서 자연스럽게 유도됩니다:

$$\mathfrak{g}_\alpha = \{ X \in \mathfrak{g} \mid t \cdot X = e^{2\pi i \alpha(\log t)} X \text{ for all } t \in T \}$$

따라서 **root $\alpha$는 본질적으로 torus action의 eigenvalue**입니다.

---

## 4. Dynkin diagram과 ADE classification

### 4.1 Root system의 geometry

Root system $\Phi$는 torus action에서 자연스럽게 등장합니다. 더 정확히 말하면:

<div class="definition" markdown="1">

<ins id="def4">**정의 4**</ins> Torus action의 eigenvalue spectrum이기는 root set $\Phi$는 다음과 같은 조건을 만족합니다:

1. $\Phi$의 원소들이 $\mathfrak{h}^*$를 spanning
2. $\alpha \in \Phi \implies -\alpha \in \Phi$
3. $\Phi$는 reflection $s_\alpha(\beta) = \beta - 2\frac{(\beta,\alpha)}{(\alpha,\alpha)}\alpha$에 닫혀 있음
4. $\langle \beta, \alpha \rangle = 2\frac{(\beta,\alpha)}{(\alpha,\alpha)} \in \mathbb{Z}$

</div>

### 4.2 Dynkin diagram의 등장

Torus action에서 root system을 분석할 때, **simple roots** $\Delta = \{ \alpha_1, \ldots, \alpha_l \}$을 선택합니다. 이들을 graph로 표현하면 Dynkin diagram이 됩니다.

<div class="example" markdown="1">

<ins id="ex5">**예시 5**</ins> **Dynkin diagram**은 다음과 같은 정보를 encoding합니다:

- 각 vertex = simple root
- vertex 사이의 edge = root들의 각도와 길이 비율
- edge의 방향 = root들의 길이 비율이 다를 때

</div>

### 4.3 ADE classification

Torus action에서 자연스럽게 등장하는 Dynkin diagram은 다음 세 종류로 분류됩니다:

<div class="proposition" markdown="1">

<ins id="prop6">**명제 6** (ADE Classification)</ins> Simply-connected semisimple Lie algebra는 다음 세 종류로 분류됩니다:

1. **Type A_n** ($n \geq 1$): $\mathfrak{sl}_{n+1}(\mathbb{C})$의 Dynkin diagram

2. **Type D_n** ($n \geq 4$): $\mathfrak{so}_{2n}(\mathbb{C})$의 Dynkin diagram

3. **Type E_6, E_7, E_8**: 예외적(exceptional) Lie algebra의 Dynkin diagram

</div>

<div class="example" markdown="1">

<ins id="ex7">**예시 7**</ins> 구체적인 예시:

- **A_1**: $\mathfrak{sl}_2(\mathbb{C})$, Dynkin diagram = • (single vertex)
- **A_2**: $\mathfrak{sl}_3(\mathbb{C})$, Dynkin diagram = •—• (two vertices connected)
- **D_4**: $\mathfrak{so}_8(\mathbb{C})$, Dynkin diagram = "fork" 모양 (3개의 branch)

</div>

---

## 5. Borel subalgebra의 등장

### 5.1 Borel subalgebra의 torus action적 정의

Borel subalgebra는 **Cartan torus action의 invariant subspace**으로 자연스럽게 등장합니다.

<div class="definition" markdown="1">

<ins id="def8">**정의 8**</ins> Cartan torus $T$의 action에서, **positive roots** $\Phi^+ \subset \Phi$를 선택하면:

$$\mathfrak{b} = \mathfrak{h} \oplus \bigoplus_{\alpha \in \Phi^+} \mathfrak{g}_\alpha$$

을 **Borel subalgebra**라 합니다. 이는 $T$-invariant subspace입니다.

</div>

### 5.2 Borel subalgebra의 자연스러운 등장 시점

Borel subalgebra는 다음과 같은 경우에 자연스럽게 등장합니다:

1. **Torus action의 정규화**: $T$-module의 decomposition에서 positive/negative 구조 선택
2. **Flag variety의 stabilizer**: $G/B$에서 $B$의 Lie algebra
3. **Parabolic subalgebra의 시작점**: Borel subalgebra를 포함하는 larger subalgebra

<div class="proposition" markdown="1">

<ins id="prop9">**명제 9**</ins> Borel subalgebra $\mathfrak{b}$는 다음 조건을 만족합니다:

1. $\mathfrak{b}$는 $T$-invariant (torus action에 닫혀 있음)
2. $\mathfrak{b}$는 solvable
3. $\mathfrak{b}$는 maximal solvable subalgebra

</div>

---

## 6. Flag variety의 등장

### 6.1 Flag variety의 torus action적 해석

Flag variety는 **Cartan torus orbit space**로 자연스럽게 등장합니다.

<div class="definition" markdown="1">

<ins id="def10">**정의 10**</ins> **Flag variety** $G/B$는 Borel subgroup $B$의 right coset space입니다. Cartan torus $T$는 $G/B$ 위에 다음과 같이 action합니다:

$$t \cdot (gB) = (gt)B, \quad t \in T, \, gB \in G/B$$

</div>

### 6.2 Flag variety의 torus orbit

Flag variety에서 torus action은 **toric variety**의 구조를 가집니다:

<div class="example" markdown="1">

<ins id="ex11">**예시 11**</ins> **Flag variety의 torus orbits**:

- **Torus fixed points**: $G/B$의 torus fixed points는 $G/B$의 **vertices**에 해당
- **Torus orbits**: 각 orbit는 torus action의 eigenvalue spectrum에 따라 분류됨
- **Flag variety = torus orbit space**: $G/B$는 torus orbits의 모임

</div>

### 6.3 Flag variety와 root system의 관계

Flag variety의 geometry는 root system과 깊은 관련이 있습니다:

<div class="proposition" markdown="1">

<ins id="prop12">**명제 12**</ins> Flag variety $G/B$의 **Torus invariant subvarieties**는 root system의 subset과一一対應합니다:

- Positive roots $\Phi^+$ ↔ Borel subgroup $B$의 Lie algebra
- Simple roots $\Delta$ ↔ $G/B$의 facet 구조
- Weyl group $W$ ↔ $G/B$의 symmetry group

</div>

---

## 7. ADE 분류 예시: Torus action 관점에서

### 7.1 Type A_n의 torus action

<div class="example" markdown="1">

<ins id="ex13">**예시 13**</ins> **Type A_n**의 torus action:

- $G = \mathrm{SL}_{n+1}(\mathbb{C})$, $T = \{ \mathrm{diag}(t_1, \ldots, t_{n+1}) \mid \prod t_i = 1 \}$
- $T$-action: $t \cdot X = t X t^{-1}$
- Root system: $\Phi = \{ e_i - e_j \mid 1 \leq i \neq j \leq n+1 \}$
- Simple roots: $\alpha_i = e_i - e_{i+1}$
- Flag variety: $\mathrm{SL}_{n+1}/B$ = full flag variety

</div>

### 7.2 Type D_n의 torus action

<div class="example" markdown="1">

<ins id="ex14">**예시 14**</ins> **Type D_n**의 torus action:

- $G = \mathrm{SO}_{2n}(\mathbb{C})$, $T$ = diagonal matrices with $\pm 1$ entries
- Root system: $\Phi = \{ \pm e_i \pm e_j \mid 1 \leq i < j \leq n \}$
- Simple roots: $\alpha_i = e_i - e_{i+1} \ (1 \leq i < n), \ \alpha_n = e_{n-1} + e_n$
- Flag variety: $\mathrm{SO}_{2n}/B$ = orthogonal flag variety

</div>

### 7.3 Exceptional types (E_6, E_7, E_8)

<div class="example" markdown="1">

<ins id="ex15">**예시 15**</ins> **Exceptional Lie algebras**:

- **E_6**: 78-dimensional, root system in $\mathbb{R}^6$
- **E_7**: 133-dimensional, root system in $\mathbb{R}^7$
- **E_8**: 248-dimensional, root system in $\mathbb{R}^8$

Flag varieties are corresponding homogeneous spaces with rich geometry.

</div>

---

## 8. 결론

이 글에서는 **Lie algebra의 root system**을 **Cartan torus action**으로 재해석했습니다:

1. **Root system** = Torus action의 eigenvalue spectrum
2. **Dynkin diagram** = Root system의 graphical representation
3. **ADE classification** = Simply-connected Lie algebras의 분류
4. **Borel subalgebra** = Torus invariant subspace
5. **Flag variety** = Torus orbit space

이 관점은 **Lie theory**와 **toric geometry**를 연결하며, representation theory, algebraic geometry, symplectic geometry等多个 분야에서 자연스럽게 등장합니다.

---

**참고문헌**

**[Hum]** J. E. Humphreys, *Introduction to Lie algebras and representation theory*, Springer, 1972.

**[Kna]** J.-P. Knapp, *Lie groups beyond an introduction*, Birkhäuser, 2002.

**[Fal]** W. Fulton, *Young tableaux: with applications to representation theory and geometry*, Cambridge University Press, 1997.
