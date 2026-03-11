---
title: "그라스만다양체"
excerpt: "Grassmannians as parameter spaces of linear subspaces"

categories: [Math / Algebraic Geometry]
permalink: /ko/math/algebraic_geometry/grassmannians
sidebar: 
    nav: "algebraic_geometry-ko"

header:
    overlay_image: /assets/images/Math/Algebraic_Geometry/Grassmannians.png
    overlay_filter: 0.5

date: 2026-03-12
last_modified_at: 2026-03-12
weight: 8

---

그라스만다양체는 선형부분공간들의 모임에 자연스러운 구조를 부여한 것이다. 이는 대수기하학에서 가장 중요한 예시 중 하나이며, 많은 다양체들이 그라스만다양체의 닫힌부분다양체로 나타난다.

## 그라스만다양체의 정의

<div class="definition" markdown="1">

<ins id="def1">**정의 1**</ins> $n$차원 벡터공간 $V$의 $k$차원 부분공간들의 집합을 *Grassmannian<sub>그라스만다양체</sub>* $G(k, V)$ 또는 $G(k, n)$이라 부른다.

</div>

<div class="example" markdown="1">

<ins id="ex2">**예시 2**</ins>

1. $G(1, n+1) = \mathbb{P}^n$ (직선들의 공간 = 사영공간)
2. $G(n-1, n) = \mathbb{P}^{n-1}$ (hyperplane들의 공간)
3. $G(2, 4)$는 $\mathbb{P}^3$의 직선들의 공간이다.

</div>

## Plücker Embedding

$G(k, n)$을 사영공간에 embedding할 수 있다.

<div class="definition" markdown="1">

<ins id="def3">**정의 3**</ins> *Plücker embedding* $\iota: G(k, n) \to \mathbb{P}(\bigwedge^k \mathbb{K}^n)$을 다음과 같이 정의한다. $k$차원 부분공간 $W = \text{span}(v_1, \ldots, v_k)$에 대해

$$\iota(W) = [v_1 \wedge v_2 \wedge \cdots \wedge v_k]$$

</div>

<div class="proposition" markdown="1">

<ins id="prop4">**명제 4**</ins> Plücker embedding은 well-defined이며 injective이다.

</div>

<details class="proof" markdown="1">
<summary>증명</summary>

$W$의 다른 basis $w_1, \ldots, w_k$를 선택하면 $w_i = \sum_j a_{ij} v_j$이고, 따라서 $w_1 \wedge \cdots \wedge w_k = \det(a_{ij}) v_1 \wedge \cdots \wedge v_k$이다. $\det(a_{ij}) \ne 0$이므로 $[w_1 \wedge \cdots \wedge w_k] = [v_1 \wedge \cdots \wedge v_k]$이다.

Injectivity: $W_1 \ne W_2$이면 서로 다른 decomposable $k$-vector를 주므로 $\iota(W_1) \ne \iota(W_2)$이다.

</details>

$\mathbb{P}(\bigwedge^k \mathbb{K}^n) \cong \mathbb{P}^{\binom{n}{k}-1}$이므로, $G(k, n)$을 $\mathbb{P}^{\binom{n}{k}-1}$의 부분집합으로 볼 수 있다.

<div class="theorem" markdown="1">

<ins id="thm5">**정리 5**</ins> Plücker embedding의 image는 $\mathbb{P}^{\binom{n}{k}-1}$의 사영다양체이다.

</div>

<div class="proposition" markdown="1">

<ins id="prop6">**명제 6**</ins> $\dim G(k, n) = k(n - k)$이다.

</div>

<details class="proof" markdown="1">
<summary>증명</summary>

$G(k, n)$은 $n \times k$ 행렬의 rank $k$인 것들의 $\text{GL}_k(\mathbb{K})$-orbit으로 생각할 수 있다. 이는 $nk - k^2 = k(n-k)$차원이다.

</details>

## Plücker Relations

$G(k, n)$을 정의하는 방정식들을 *Plücker relations*라 부른다.

<div class="proposition" markdown="1">

<ins id="prop7">**명제 7**</ins> $v \in \bigwedge^k \mathbb{K}^n$이 decomposable (즉, $v = v_1 \wedge \cdots \wedge v_k$)일 필요충분조건는 모든 $w \in \bigwedge^{k-1} \mathbb{K}^n$에 대해

$$(v \wedge w) \wedge (v \wedge w) = 0$$

인 것이다.

</div>

이 조건을 좌표로 쓰면 Plücker relations를 얻는다.

<div class="example" markdown="1">

<ins id="ex8">**예시 8**</ins> $G(2, 4)$의 경우, Plücker coordinates를 $p_{ij} = x_i \wedge x_j$라 하면 ($1 \le i < j \le 4$), 유일한 Plücker relation은

$$p_{12} p_{34} - p_{13} p_{24} + p_{14} p_{23} = 0$$

이다. 따라서 $G(2, 4) \subset \mathbb{P}^5$는 하나의 quadratic hypersurface이다.

</div>

## Affine Cover

$G(k, n)$은 $\binom{n}{k}$개의 아핀공간으로 덮을 수 있다.

<div class="definition" markdown="1">

<ins id="def9">**정의 9**</ins> 각 $k$개의 index들 $I = \{i_1 < \cdots < i_k\}$에 대해 open set $U_I$를

$$U_I = \{W \in G(k, n) \mid \text{projection } W \to \text{span}(e_{i_1}, \ldots, e_{i_k}) \text{ is an isomorphism}\}$$

으로 정의한다.

</div>

<div class="proposition" markdown="1">

<ins id="prop10">**명제 10**</ins> 각 $U_I \cong \mathbb{A}^{k(n-k)}$이다.

</div>

<details class="proof" markdown="1">
<summary>증명</summary>

$U_I$의 원소 $W$는 $k \times n$ 행렬로 표현되며, $I$에 해당하는 $k \times k$ minor가 invertible이다. 이를 identity로 normalize하면 나머지 $k(n-k)$개의 entry들이 자유롭다.

</details>

## Schubert Varieties

$G(k, n)$의 중요한 닫힌부분다양체들로 *Schubert varieties*가 있다.

<div class="definition" markdown="1">

<ins id="def11">**정의 11**</ins> Flag $0 = V_0 \subset V_1 \subset \cdots \subset V_n = \mathbb{K}^n$과 partition $\lambda = (\lambda_1 \ge \cdots \ge \lambda_k \ge 0)$에 대해 *Schubert variety* $\Omega_\lambda$를

$$\Omega_\lambda = \{W \in G(k, n) \mid \dim(W \cap V_{n-k+i-\lambda_i}) \ge i \text{ for all } i\}$$

으로 정의한다.

</div>

<div class="proposition" markdown="1">

<ins id="prop12">**명제 12**</ins> $\dim \Omega_\lambda = |\lambda| = \lambda_1 + \cdots + \lambda_k$이다.

</div>

<div class="example" markdown="1">

<ins id="ex13">**예시 13**</ins> $G(2, 4)$에서:

- $\Omega_{(0,0)} = G(2,4)$ (전체)
- $\Omega_{(1,0)}$: hyperplane section
- $\Omega_{(2,0)}$: $\mathbb{P}^2$
- $\Omega_{(1,1)}$: $\mathbb{P}^1 \times \mathbb{P}^1$
- $\Omega_{(2,1)}$: $\mathbb{P}^1$
- $\Omega_{(2,2)}$: point

</div>

## Applications

<div class="example" markdown="1">

<ins id="ex14">**예시 14**</ins> **$\mathbb{P}^3$의 직선들**: $G(2, 4)$는 $\mathbb{P}^3$의 직선들의 공간이다. 두 직선이 만나는 조건은 Plücker coordinates로 표현된다.

</div>

<div class="example" markdown="1">

<ins id="ex15">**예시 15**</ins> **Moduli of vector bundles**: 그라스만다양체는 vector bundle들의 moduli space를 연구하는 데 사용된다.

</div>

---

**참고문헌**

**[Har]** J. Harris, *Algebraic Geometry: A First Course*, Springer, 1992.  
**[GH]** P. Griffiths and J. Harris, *Principles of Algebraic Geometry*, Wiley, 1978.  
**[Ful]** W. Fulton, *Young Tableaux*, Cambridge University Press, 1997.
