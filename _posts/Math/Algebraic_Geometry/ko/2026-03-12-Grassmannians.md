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
last_modified_at: 2026-03-15
weight: 7

---

지금까지 우리는 아핀공간과 사영공간의 부분집합으로 정의되는 [사영다양체](/ko/math/algebraic_geometry/projective_varieties)들을 살펴보았다. 이 절에서 우리는 더 일반적인 종류의 다양체인 그라스만다양체를 소개한다. 그라스만다양체는 선형부분공간들의 모임에 자연스러운 구조를 부여한 것으로, 대수기하학에서 가장 중요한 예시 중 하나이다. 많은 흥미로운 다양체들이 그라스만다양체의 닫힌부분다양체로 나타나며, 그라스만다양체 자체도 다양한 기하학적 문제에서 등장한다.

그라스만다양체의 핵심 아이디어는 "공간들의 공간"을 정의하는 것이다. 단순히 점들의 집합이 아니라, 선형부분공간이라는 "기하학적 대상"들의 집합에 대수적 구조를 부여하는 것이다. 이는 moduli space (모듈리 공간)의 가장 기본적인 예시이며, 현대 대수기하학에서 매우 중요한 개념이다.

## 그라스만다양체의 정의

$$n$$차원 벡터공간 $$V$$의 $$k$$차원 부분공간들을 모아놓은 집합을 생각해보자. 이 집합은 단순한 집합이 아니라, 자연스러운 위상과 대수적 구조를 갖는다. 이것이 그라스만다양체이다. 직관적으로, 그라스만다양체는 "선형부분공간들의 parameter space"이다.

<div class="definition" markdown="1">

<ins id="def1">**정의 1**</ins> $$n$$차원 벡터공간 $$V$$의 $$k$$차원 부분공간들의 집합을 *Grassmannian<sub>그라스만다양체</sub>* $$G(k, V)$$ 또는 $$G(k, n)$$이라 부른다.

</div>

기하학적으로, $$G(k, n)$$은 $$\mathbb{A}^n$$ (또는 $$\mathbb{P}^{n-1}$$)의 $$k$$차원 선형부분공간들의 *parameter space*이다. 즉, $$G(k, n)$$의 각 점은 하나의 $$k$$차원 부분공간에 대응된다. 예를 들어, $$G(1, 3)$$은 $$\mathbb{P}^2$$의 직선들의 공간이고, $$G(2, 4)$$는 $$\mathbb{P}^3$$의 직선들의 공간이다.

<div class="example" markdown="1">

<ins id="ex2">**예시 2**</ins> 그라스만다양체의 기본 예시들이다.

1. $$G(1, n+1) = \mathbb{P}^n$$이다. 1차원 부분공간은 원점을 지나는 직선이고, 이는 사영공간의 점에 대응된다. 따라서 직선들의 공간은 사영공간과 같다. 이는 그라스만다양체가 사영공간을 일반화함을 보여준다.
2. $$G(n-1, n) = \mathbb{P}^{n-1}$$이다. $$(n-1)$$차원 부분공간은 hyperplane이고, 이는 법벡터 (modulo scalar)에 의해 결정된다. 따라서 hyperplane들의 공간은 $$\mathbb{P}^{n-1}$$이다. 이는 "duality"의 관점에서 이해할 수 있다.
3. $$G(2, 4)$$는 $$\mathbb{P}^3$$의 직선들의 공간이다. 이는 4차원 공간의 2차원 부분공간들의 모임으로, $$\mathbb{P}^3$$의 각 직선에 대응된다. $$\dim G(2, 4) = 2 \cdot (4-2) = 4$$이므로, $$\mathbb{P}^3$$의 직선들은 4개의 parameter로 결정된다. 이는 직선이 "어디를 지나는가" (3 parameters)와 "어떤 방향인가" (1 parameter)로 결정됨을 반영한다.

</div>

## Plücker Embedding

그라스만다양체 $$G(k, n)$$를 사영공간의 부분집합으로 실현하는 가장 자연스러운 방법은 Plücker embedding이다. 이는 exterior product (외적)를 사용한다. 먼저 exterior product를 간략히 설명하자.

$$V$$가 $$n$$차원 벡터공간일 때, *exterior power* $$\bigwedge^k V$$는 $$V$$의 $$k$$개 원소들로 만드는 multilinear 연산의 공간이다. 구체적으로, $$\bigwedge^k V$$의 원소는 형식적 기호 $$v_1 \wedge \cdots \wedge v_k$$들의 선형결합으로 나타내며, 이 기호들은 다음 성질을 만족한다:

- **교환 법칙**: 두 벡터를 교환하면 부호가 바뀐다. 즉, $$v_i \wedge v_j = -v_j \wedge v_i$$이다. 이로부터 같은 벡터의 외적은 0이 된다: $$v \wedge v = 0$$.
- **Multilinearity**: 각 변수에 대해 선형이다. 즉, $$(av + bw) \wedge v_2 \wedge \cdots \wedge v_k = a(v \wedge v_2 \wedge \cdots \wedge v_k) + b(w \wedge v_2 \wedge \cdots \wedge v_k)$$이다.

이러한 성질로부터 핵심적인 결과가 따른다: $$v_1, \ldots, v_k$$가 linearly dependent하면 $$v_1 \wedge \cdots \wedge v_k = 0$$이다. 역으로, $$k$$개의 linearly independent한 벡터들의 외적은 0이 아니며, $$\bigwedge^k V$$의 원소 중 이러한 꼴의 원소를 *decomposable*이라 부른다. $$\dim \bigwedge^k V = \binom{n}{k}$$이다.

기하학적으로, $$v_1 \wedge \cdots \wedge v_k$$는 이 벡터들이 결정하는 $$k$$차원 평행면체의 "oriented volume"을 나타낸다. 이는 Plücker embedding의 핵심 아이디어이다: 부분공간 $$W = \operatorname{span}(v_1, \ldots, v_k)$$를 $$v_1 \wedge \cdots \wedge v_k$$라는 하나의 벡터로 대응시키면, $$W$$의 기하학적 정보를 exterior power의 원소로 인코딩할 수 있다.

<div class="definition" markdown="1">

<ins id="def3">**정의 3**</ins> *Plücker embedding* $$\iota: G(k, n) \to \mathbb{P}(\bigwedge^k \mathbb{K}^n)$$을 다음과 같이 정의한다. $$k$$차원 부분공간 $$W = \operatorname{span}(v_1, \ldots, v_k)$$에 대해

$$\iota(W) = [v_1 \wedge v_2 \wedge \cdots \wedge v_k]$$

이다.

</div>

여기서 $$\bigwedge^k \mathbb{K}^n$$은 $$\mathbb{K}^n$$의 $$k$$번째 exterior power이고, $$v_1 \wedge \cdots \wedge v_k$$는 decomposable $$k$$-vector이다. $$\dim \bigwedge^k \mathbb{K}^n = \binom{n}{k}$$이므로, $$\mathbb{P}(\bigwedge^k \mathbb{K}^n) \cong \mathbb{P}^{\binom{n}{k}-1}$$이다.

<div class="proposition" markdown="1">

<ins id="prop4">**명제 4**</ins> Plücker embedding은 well-defined이며 injective이다.

</div>

<details class="proof" markdown="1">
<summary>증명</summary>

**Well-defined**: $$W$$의 다른 basis $$w_1, \ldots, w_k$$를 선택하자. 그럼 $$w_i = \sum_{j=1}^k a_{ij} v_j$$ for some invertible matrix $$(a_{ij})$$이다. Exterior product의 multilinearity에 의해

$$w_1 \wedge \cdots \wedge w_k = \det(a_{ij}) v_1 \wedge \cdots \wedge v_k$$

이다. $$\det(a_{ij}) \ne 0$$이므로 $$[w_1 \wedge \cdots \wedge w_k] = [v_1 \wedge \cdots \wedge v_k]$$이다. 따라서 $$\iota(W)$$는 basis의 선택에 의존하지 않는다.

**Injectivity**: $$W_1 \ne W_2$$라 하고 $$\iota(W_1) = \iota(W_2)$$라 가정하자. 즉, $$[v_1 \wedge \cdots \wedge v_k] = [w_1 \wedge \cdots \wedge w_k]$$인 것이므로, 0이 아닌 스칼라 $$c$$에 대해 $$v_1 \wedge \cdots \wedge v_k = c \, w_1 \wedge \cdots \wedge w_k$$이다. $$W_1 \ne W_2$$이므로, $$W_1$$에 속하지 않는 $$W_2$$의 nonzero 벡터 $$u$$가 존재한다 (또는 그 역). $$u \in W_2 \setminus W_1$$이라 하자. $$u$$를 $$w_1, \ldots, w_k$$의 선형결합으로 쓰면 $$u = \sum a_i w_i$$이며, 적어도 하나의 계수 $$a_j \ne 0$$이다. 이제 양변에 $$u$$를 외적하면

$$v_1 \wedge \cdots \wedge v_k \wedge u = c \, w_1 \wedge \cdots \wedge w_k \wedge u = 0$$

이다 (오른쪽은 $$u$$가 $$w_i$$들의 선형결합이므로 0). 그런데 $$u \notin W_1 = \operatorname{span}(v_1, \ldots, v_k)$$이므로 $$v_1, \ldots, v_k, u$$는 linearly independent이고, 따라서 $$v_1 \wedge \cdots \wedge v_k \wedge u \ne 0$$이다. 이는 모순이다. 따라서 $$\iota(W_1) \ne \iota(W_2)$$이다.

</details>

$$\iota$$의 image가 사영다양체인지 확인해보자.

<div class="proposition" markdown="1">

<ins id="prop5">**명제 5**</ins> Plücker embedding의 image는 $$\mathbb{P}^{\binom{n}{k}-1}$$의 사영다양체이다. 즉, $$G(k, n)$$은 사영다양체이다.

</div>

이 명제의 핵심은 Plücker embedding의 image가 사영공간에서 polynomial equations로 정의된 닫힌집합이라는 것이다. 구체적으로, $$k$$-vector $$v$$가 decomposable (즉, $$v = v_1 \wedge \cdots \wedge v_k$$의 꼴)일 조건은 *Plücker relations*라 불리는 polynomial equations로 표현된다. 이 방정식들의 해집합은 사영공간의 닫힌집합이고, $$\iota$$의 image는 정확히 이 해집합이다. 따라서 $$G(k, n) \cong \operatorname{im} \iota$$는 사영다양체이다. Plücker relations의 구체적인 형태는 다음 절에서 다룬다. 이 정리는 그라스만다양체가 "well-behaved" 대수적 대상임을 보여준다.

<div class="proposition" markdown="1">

<ins id="prop6">**명제 6**</ins> $$\dim G(k, n) = k(n - k)$$이다.

</div>

<details class="proof" markdown="1">
<summary>증명</summary>

$$G(k, n)$$의 원소 $$W$$는 $$n \times k$$ 행렬 $$A$$의 column space로 표현된다. 여기서 $$A$$의 rank는 $$k$$이다. 두 행렬 $$A, A'$$가 같은 column space를 갖는 것은 $$A' = A B$$ for some $$B \in \operatorname{GL}_k(\mathbb{K})$$인 것과 동치이다. 따라서

$$G(k, n) \cong \{A \in \operatorname{Mat}_{n \times k}(\mathbb{K}) \mid \operatorname{rank}(A) = k\} / \operatorname{GL}_k(\mathbb{K})$$

이다. Rank $$k$$인 $$n \times k$$ 행렬들의 공간은 $$nk$$차원이고, $$\operatorname{GL}_k(\mathbb{K})$$는 $$k^2$$차원이므로

$$\dim G(k, n) = nk - k^2 = k(n-k)$$

이다.

</details>

이 결과는 직관적으로 타당하다. $$k$$차원 부분공간을 결정하려면 $$k$$개의 basis 벡터가 필요하고, 각 벡터는 $$n$$개의 좌표를 갖는다. 하지만 basis의 선택에 $$k^2$$의 자유도가 있으므로, $$nk - k^2 = k(n-k)$$개의 "진짜 parameter"가 남는다.

## Plücker Relations

Plücker embedding의 image를 정의하는 방정식들을 *Plücker relations*라 부른다. 이들은 exterior product의 성질에서 유래한다. Plücker relations는 그라스만다양체를 "explicitly" 정의하는 방정식들을 제공한다.

$$\bigwedge^k \mathbb{K}^n$$의 모든 원소가 decomposable (즉, $$v_1 \wedge \cdots \wedge v_k$$의 꼴)인 것은 아니다. 예를 들어 $$\bigwedge^2 \mathbb{K}^4$$에서 $$e_1 \wedge e_2 + e_3 \wedge e_4$$는 decomposable이 아니다. Plücker relations는 어떤 $$k$$-vector가 decomposable일 조건을 명시한다. Decomposable $$k$$-vector만이 그라스만다양체의 점에 대응된다.

<div class="proposition" markdown="1">

<ins id="prop7">**명제 7**</ins> $$v \in \bigwedge^k \mathbb{K}^n$$이 decomposable일 필요충분조건은 모든 $$w \in \bigwedge^{k-1} \mathbb{K}^n$$에 대해

$$(v \wedge w) \wedge (v \wedge w) = 0 \in \bigwedge^{2k} \mathbb{K}^n$$

인 것이다.

</div>

이 조건을 Plücker coordinates로 쓰면 구체적인 방정식들을 얻는다. Plücker coordinates $$p_{i_1 \cdots i_k}$$는 $$v = \sum_{i_1 < \cdots < i_k} p_{i_1 \cdots i_k} e_{i_1} \wedge \cdots \wedge e_{i_k}$$에서의 계수들이다. 이들은 $$G(k, n)$$의 "자연스러운 좌표계"이다.

<div class="example" markdown="1">

<ins id="ex8">**예시 8**</ins> **$$G(2, 4)$$의 Plücker relation**: $$G(2, 4)$$를 생각하자. Plücker coordinates는 $$p_{12}, p_{13}, p_{14}, p_{23}, p_{24}, p_{34}$$이고, 이는 $$\mathbb{P}^5$$의 homogeneous coordinates이다. 유일한 Plücker relation은

$$p_{12} p_{34} - p_{13} p_{24} + p_{14} p_{23} = 0$$

이다. 이는 quadratic equation이므로 $$G(2, 4)$$는 $$\mathbb{P}^5$$의 quadric hypersurface이다. 기하학적으로, $$G(2, 4)$$는 4차원 quadric이며 smooth하다. 이 방정식은 $$\mathbb{P}^3$$의 두 직선이 만날 조건을 Plücker coordinates로 표현한 것과 관련이 있다.

</div>

Plücker relations의 기하학적 의미는 다음과 같다. $$W \in G(k, n)$$이 주어지면, Plücker coordinates $$p_{i_1 \cdots i_k}$$는 $$W$$를 나타내는 행렬의 $$k \times k$$ minors (up to sign)이다. Plücker relation은 이들 minors 사이의 관계식이다. 이는 "선형대수적 identity"가 "기하학적 방정식"으로 나타남을 보여준다.

## Affine Cover

Plücker embedding을 통해 $$G(k, n)$$이 [사영다양체](/ko/math/algebraic_geometry/projective_varieties)임을 보았다. 그러나 사영다양체 자체는 닫힌조건으로 정의되므로, 직접적으로 다루기가 어려울 수 있다. 이에 대한 해결책은 $$G(k, n)$$을 유한개의 아핀 variety들로 덮는 것이다. 이렇게 하면 각 아핀 조각에서 선형대수적 방법으로 좌표를 부여하고 계산할 수 있으며, 그 결과를 이어붙여 전체 그라스만다양체의 구조를 이해할 수 있다. 또한 이 cover는 $$G(k, n)$$이 [준사영다양체](/ko/math/algebraic_geometry/quasi_projective_varieties)임을 보여준다.

<div class="definition" markdown="1">

<ins id="def9">**정의 9**</ins> 각 $$k$$개의 index들 $$I = \{i_1 < \cdots < i_k\}$$에 대해 open set $$U_I$$를

$$U_I = \{W \in G(k, n) \mid \text{projection } W \to \operatorname{span}(e_{i_1}, \ldots, e_{i_k}) \text{ is an isomorphism}\}$$

으로 정의한다.

</div>

기하학적으로, $$U_I$$는 "$$W$$가 좌표들 $$x_{i_1}, \ldots, x_{i_k}$$으로 uniquely project되는" 부분공간들의 모임이다. 이는 $$W$$를 나타내는 $$n \times k$$ 행렬에서 $$I$$에 해당하는 $$k \times k$$ minor가 nonzero라는 것과 같다. 각 $$U_I$$는 그라스만다양체의 "coordinate chart"이다.

<div class="proposition" markdown="1">

<ins id="prop10">**명제 10**</ins> 각 $$U_I \cong \mathbb{A}^{k(n-k)}$$이다.

</div>

<details class="proof" markdown="1">
<summary>증명</summary>

$$I = \{1, 2, \ldots, k\}$$인 경우를 보이자 (일반성을 잃지 않음). $$W \in U_I$$를 나타내는 $$n \times k$$ 행렬 $$A$$에서, 상위 $$k \times k$$ minor가 nonzero이다. 행 연산을 통해 이 minor를 identity matrix로 만들 수 있다:

$$A = \begin{pmatrix} I_k \\ B \end{pmatrix}$$

여기서 $$B$$는 $$(n-k) \times k$$ 행렬이다. $$B$$의 $$k(n-k)$$개의 entry들이 $$W$$를 완전히 결정하며, 이들 사이에 어떤 constraint도 없다. 따라서 $$U_I \cong \mathbb{A}^{k(n-k)}$$이다.

</details>

이 증명에서 보듯, $$U_I$$에서의 좌표계는 $$k(n-k)$$개의 자유로운 parameter들이다. 이들은 $$W$$를 나타내는 행렬에서 "non-trivial한 부분"에 해당한다. 즉, 상위 $$k \times k$$ block이 identity로 고정된 후, 나머지 $$(n-k) \times k$$ block이 자유롭게 변할 수 있다.

## Schubert Varieties

그라스만다양체의 가장 중요한 닫힌부분다양체들은 Schubert varieties이다. 이들은 flag (깃발)와 관련된 기하학적 조건으로 정의된다. Schubert varieties는 intersection theory의 기본 도구이다.

먼저 flag와 partition의 개념을 정의하자. *Flag*는 서로 포함관계를 이루는 부분공간들의 사슬 $$0 = V_0 \subset V_1 \subset \cdots \subset V_n = \mathbb{K}^n$$이다. 여기서 각 $$V_i$$는 $$i$$차원 부분공간이다. Flag는 "기준이 되는 부분공간들의 체인"을 제공한다. *Partition*은 조건 $$\lambda_1 \ge \lambda_2 \ge \cdots \ge \lambda_k \ge 0$$을 만족하는 정수열 $$\lambda = (\lambda_1, \ldots, \lambda_k)$$이다. Partition의 *크기*는 $$\lvert\lambda\rvert = \lambda_1 + \cdots + \lambda_k$$로 정의한다. Flag와 partition이 만나면, partition이 flag의 각 단계와 "얼마나 교차하는지"를 수치화하여 Schubert variety를 정의하는 데 사용된다.

<div class="definition" markdown="1">

<ins id="def11">**정의 11**</ins> *Flag* $$0 = V_0 \subset V_1 \subset \cdots \subset V_n = \mathbb{K}^n$$와 partition $$\lambda = (\lambda_1 \ge \cdots \ge \lambda_k \ge 0)$$ (단, $$\lambda_1 \le n-k$$)에 대해 *Schubert variety* $$\Omega_\lambda$$를

$$\Omega_\lambda = \{W \in G(k, n) \mid \dim(W \cap V_{n-k+i-\lambda_i}) \ge i \text{ for all } i = 1, \ldots, k\}$$

으로 정의한다.

</div>

Schubert variety의 정의는 복잡해 보이지만, 기하학적 의미는 명확하다. $$\Omega_\lambda$$는 주어진 flag와 특정한 "교차 조건"을 만족하는 부분공간 $$W$$들의 모임이다. 조건 $$\dim(W \cap V_{n-k+i-\lambda_i}) \ge i$$는 $$W$$가 $$V_{n-k+i-\lambda_i}$$와 적어도 $$i$$차원만큼 교차해야 함을 의미한다. 이는 "$$W$$가 얼마나 '특별한' 위치에 있는가"를 측정한다.

<div class="proposition" markdown="1">

<ins id="prop12">**명제 12**</ins> $$\dim \Omega_\lambda = \lvert\lambda\rvert = \lambda_1 + \cdots + \lambda_k$$이다.

</div>

<details class="proof" markdown="1">
<summary>증명</summary>

Standard flag $$V_i = \operatorname{span}(e_1, \ldots, e_i)$$를 사용하자. $$\Omega_\lambda$$의 codimension을 계산하면, $$G(k, n)$$의 affine chart $$U_{\{1,\ldots,k\}}$$에서 $$W$$는 행렬 $$\begin{pmatrix} I_k \\ B \end{pmatrix}$$로 나타내어진다. 여기서 $$B = (b_{ij})$$는 $$(n-k) \times k$$ 행렬이다.

조건 $$\dim(W \cap V_{n-k+i-\lambda_i}) \ge i$$를 $$B$$의 entry들에 대한 제약조건으로 번역하자. $$W$$의 처음 $$j$$개 basis vector가 $$V_{n-k+i-\lambda_i}$$에 포함되려면, $$B$$의 관련된 entry들이 0이어야 한다. 구체적으로, 각 $$i = 1, \ldots, k$$에 대해 $$\lambda_i$$개의 독립적인 linear condition이 $$B$$의 entry들에 부과된다. 예를 들어 $$i = 1$$일 때, $$W$$의 첫 번째 basis vector가 $$V_{n-k+1-\lambda_1}$$에 속하면 $$B$$의 처음 $$\lambda_1$$개 row의 첫 번째 column이 0이어야 한다. 이를 모든 $$i$$에 대해 반복하면, 총 $$\sum_{i=1}^k \lambda_i = \lvert\lambda\rvert$$개의 독립적인 조건이 나온다.

이러한 조건들은 서로 독립이며 (각 조건이 $$B$$의 서로 다른 entry에 관련됨), 따라서 $$\Omega_\lambda$$의 codimension은 $$\lvert\lambda\rvert$$이다. 따라서

$$\dim \Omega_\lambda = \dim G(k, n) - \lvert\lambda\rvert = k(n-k) - (k(n-k) - \lvert\lambda\rvert) = \lvert\lambda\rvert$$

이다.

</details>

<div class="example" markdown="1">

<ins id="ex13">**예시 13**</ins> **$$G(2, 4)$$의 Schubert varieties**: $$G(2, 4)$$에서 가능한 partitions은 $$(0,0)$$, $$(1,0)$$, $$(2,0)$$, $$(1,1)$$, $$(2,1)$$, $$(2,2)$$이다.

- $$\Omega_{(0,0)} = G(2,4)$$: 전체 그라스만다양체 (조건 없음). "가장 일반적인" 부분공간들.
- $$\Omega_{(1,0)}$$: hyperplane section, $$\dim = 1$$. $$W$$가 특정 3차원 부분공간과 1차원 이상 교차하는 조건. "약간 특별한" 부분공간들.
- $$\Omega_{(2,0)} \cong \mathbb{P}^2$$, $$\dim = 2$$. $$W$$가 특정 2차원 부분공간을 포함하는 조건. "특정 평면을 포함하는" 직선들.
- $$\Omega_{(1,1)} \cong \mathbb{P}^1 \times \mathbb{P}^1$$, $$\dim = 2$$. $$W$$가 두 개의 3차원 부분공간과 각각 1차원 이상 교차하는 조건. "두 hyperplane의 교차"에 있는 직선들.
- $$\Omega_{(2,1)} \cong \mathbb{P}^1$$, $$\dim = 1$$. $$W$$가 특정 2차원 부분공간을 포함하고 특정 3차원 부분공간과 2차원 이상 교차하는 조건. "매우 특별한" 직선들.
- $$\Omega_{(2,2)}$$: single point, $$\dim = 0$$. $$W$$가 특정 2차원 부분공간과 같은 조건. "완전히 결정된" 부분공간.

</div>

<div class="misc" markdown="1">

Schubert varieties의 중요성은 다음과 같다:

1. **Cell decomposition**: $$G(k, n)$$은 Schubert cells (Schubert varieties의 interior)들의 disjoint union으로 분해된다. 이를 통해 그라스만다양체에 CW 복합체 구조를 부여할 수 있으며, 위상적 성질을 조합적으로 계산할 수 있다.
2. **Cohomology**[^1]: Schubert varieties의 cohomology classes는 $$G(k, n)$$의 cohomology ring의 basis를 이룬다. 이러한 basis 원소들을 *Schubert classes*라 부르며, 그라스만다양체의 위상적 불변량을 계산하는 핵심 도구이다.
3. **Intersection theory**: Schubert calculus는 Schubert varieties의 교차를 계산하는 방법이다. 이는 enumerative geometry의 핵심으로, "몇 개의 부분공간이 주어진 조건을 만족하는가"라는 기하학적 질문에 구체적인 수치적 답을 제공한다.

</div>

## 응용

<div class="example" markdown="1">

<ins id="ex14">**예시 14**</ins> **$$\mathbb{P}^3$$의 직선들**: $$G(2, 4)$$는 $$\mathbb{P}^3$$의 직선들의 공간이다. $$\mathbb{P}^3$$의 두 직선 $$L_1, L_2$$가 만나는 조건은 Plücker coordinates로 다음과 같이 표현된다. $$L_1, L_2$$의 Plücker coordinates를 $$p_{ij}, q_{ij}$$라 하면, $$L_1$$과 $$L_2$$가 만날 필요충분조건은

$$p_{12} q_{34} - p_{13} q_{24} + p_{14} q_{23} + p_{23} q_{14} - p_{24} q_{13} + p_{34} q_{12} = 0$$

이다. 이는 $$G(2, 4)$$ 위의 bilinear form이다. 기하학적으로, 이 식은 두 직선의 "상대적 위치"를 Plücker coordinates로 표현한 것이다. 이는 선형대수적 조건이 기하학적 조건과 어떻게 연결되는지를 보여주는 좋은 예시이다.

</div>

<div class="example" markdown="1">

<ins id="ex15">**예시 15**</ins> **Veronese embedding과 Segre embedding**: 그라스만다양체는 다른 중요한 embedding들의 일반화이다.

<div class="misc" markdown="1">

- Veronese embedding $$\mathbb{P}^n \to \mathbb{P}^N$$은 $$G(1, n+1) \to \mathbb{P}^n$$의 "higher degree" 버전으로 볼 수 있다. 이는 사영공간을 "고차원" 공간으로 embedding하는 방법이다.
- Segre embedding $$\mathbb{P}^m \times \mathbb{P}^n \to \mathbb{P}^{mn+m+n}$$은 product의 embedding이다. $$\mathbb{P}^1 \times \mathbb{P}^1$$은 $$G(2, 4)$$의 Schubert variety $$\Omega_{(1,1)}$$와 isomorphic하다. 이는 product variety가 그라스만다양체의 부분다양체로 나타남을 보여준다.

</div>

</div>

<div class="example" markdown="1">

<ins id="ex16">**예시 16**</ins> **Moduli of vector bundles**[^2]: 그라스만다양체는 vector bundle들의 moduli space를 연구하는 기본 도구이다. 주어진 vector bundle $$E$$ on $$X$$의 [section](https://en.wikipedia.org/wiki/Section_(fiber_bundle))들의 공간 $$H^0(X, E)$$의 $$k$$차원 부분공간들의 모임은 $$G(k, H^0(X, E))$$의 닫힌부분다양체로 나타난다. 이를 통해 vector bundle의 성질을 기하학적으로 연구할 수 있다. 예를 들어, [line bundle](https://en.wikipedia.org/wiki/Line_bundle)[^3]의 section들의 공간은 사영공간이고, 이들의 부분공간들의 모임은 그라스만다양체이다. 이는 "vector bundle의 기하학"과 "선형대수의 기하학"을 연결한다.

</div>

---

[^1]: *Cohomology ring*은 다양체의 위상적 불변량을 대수적으로 나타내는 구조이다. 이 글의 범위를 넘어서는 개념이지만, Schubert varieties의 cohomology classes가 그라스만다양체의 cohomology ring의 basis를 이룬다는 사실은 이론대수기하학에서 중요한 정리이다.

[^2]: *Vector bundle*은 다양체 위의 점마다 벡터공간을 대응시키는 구조이다. 이 개념은 이 글의 선행 내용에서 정의되지 않았으므로, 이 예시는 참고용으로만 이해하면 된다.

[^3]: *Line bundle*은 rank 1인 vector bundle로, 다양체 위의 각 점에 1차원 벡터공간을 대응시키는 구조이다. 가장 기본적인 예시로는 사영공간의 tautological line bundle $$\mathcal{O}(-1)$$이 있다.

---

**참고문헌**

**[Har]** J. Harris, *Algebraic Geometry: A First Course*, Springer, 1992.  
**[GH]** P. Griffiths and J. Harris, *Principles of Algebraic Geometry*, Wiley, 1978.  
**[Ful]** W. Fulton, *Young Tableaux*, Cambridge University Press, 1997.
