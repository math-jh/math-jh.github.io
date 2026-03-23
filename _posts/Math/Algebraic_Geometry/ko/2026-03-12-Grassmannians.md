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
last_modified_at: 2026-03-24
weight: 7

---

우리는 특수한 다양체를 하나 소개하며 대수기하학의 기본적인 연구대상들에 대한 소개를 마무리한다. 

정의에 의해 projective space $$\mathbb{P}^n$$은 $$\mathbb{A}^{n+1}$$의 직선들의 공간이다. 이번 글에서 소개할 Grassmannian은 이를 일반화한 것으로, $$\mathbb{A}^n$$의 $$k$$차원 linear subspace들의 공간이다. 

## 그라스만 다양체의 정의

<div class="definition" markdown="1">

<ins id="def1">**정의 1**</ins> $$n$$차원 벡터공간 $$V$$의 $$k$$차원 부분공간들의 집합을 *Grassmannian<sub>그라스만다양체</sub>* $$\Gr(k, V)$$ 또는 $$\Gr(k, n)$$이라 부른다.

</div>

물론 이것이 variety 구조를 갖는다는 것은 별도로 보여야 하지만, 핵심적인 결과는 이것이 variety 구조를 가질 뿐 아니라 $$\mathbb{A}^n$$에서 각각의 $$k$$-plane들의 위치관계까지 잘 보존하는 구조를 주므로 큰 신경을 쓰지 않아도 우리가 원하는대로 행동한다는 것이다. 

<div class="example" markdown="1">

<ins id="ex2">**예시 2**</ins> 가령, $$\Gr(1, n+1)$$은 $$n+1$$차원 벡터공간 $$\mathbb{K}^{n+1}$$의 line들의 공간이므로, 정의에 의해 이는 $$\mathbb{P}^n$$과 같다. 곧 Grassmannian 위의 variety 구조를 정의한 후에는 이 두 구조가 정확히 같다는 것을 알게 될 것이다. 

기존에 없던 예시 중 가장 간단한 것은 $$\Gr(2,4)$$이다. 이는 $$4$$차원 공간의 $$2$$차원 부분공간들의 모임이다. Grassmannian을 다룰 때는 이 예시가 toy example로서 기능할 것이다. 

</div>

언제나 그렇듯이 variety 구조를 주기 위해서는 affine cover를 생각해서 affine-local하게 접근하면 된다. 이를 위해 다음을 정의한다. 

<div class="definition" markdown="1">

<ins id="def3">**정의 3**</ins> 각 $$k$$개의 index들 $$I = \{i_1 < \cdots < i_k\}$$에 대해 open set $$U_I$$를

$$U_I = \{W \in \Gr(k, n) \mid \text{projection } W \to \operatorname{span}(e_{i_1}, \ldots, e_{i_k}) \text{ is an isomorphism}\}$$

으로 정의한다.

</div>

Standard basis $$e_1,\ldots, e_n$$을 고정하고, $$W$$를 span하는 각각의 벡터들 $$w_1,\ldots, w_k$$을 사용하면 $$W$$는 다음 $$k\times n$$ 행렬

$$\begin{pmatrix}w_1\\\vdots\\w_k\end{pmatrix}=\begin{pmatrix}w_{1,1}&w_{1,2}&\cdots &w_{1,n}\\ \vdots&\vdots&\ddots&\vdots\\ w_{k,1}&w_{k,2}&\cdots&w_{k,n}\end{pmatrix}$$

의 row space이다. 그럼 $$U_I$$를 정의하는 조건은 정확하게 index set $$I$$에 해당하는 column들 $$i_1,\ldots, i_k$$을 사용하여 만든 $$k\times k$$ 행렬이 invertible인 것과 동치이다. 그럼 다음이 성립한다. 

<div class="proposition" markdown="1">

<ins id="prop4">**명제 4**</ins> 각 $$U_I \cong \mathbb{A}^{k(n-k)}$$이다.

</div>

<details class="proof" markdown="1">
<summary>증명</summary>

일반성을 잃지 않고 $$I = \{1, 2, \ldots, k\}$$인 경우를 보이자. 즉 $$W \in U_I$$를 나타내는 $$k \times n$$ 행렬 $$A$$에서, 좌측 $$k \times k$$ minor가 nonzero이다. 행 연산을 통해 이 minor를 다음의 꼴

$$A = \begin{pmatrix} I_k & B \end{pmatrix}$$

과 같이 만들자. 여기서 $$B$$는 $$k \times (n-k)$$ 행렬이다. 그럼 $$B$$의 $$k(n-k)$$개의 entry들이 $$W$$를 완전히 결정하며, 이들 사이에 어떤 constraint도 없다. 따라서 $$U_I \cong \mathbb{A}^{k(n-k)}$$이다.

</details>

이 증명에서 보듯, $$U_I$$에서의 좌표계는 $$k(n-k)$$개의 자유로운 parameter들이다. 이들은 $$W$$를 나타내는 행렬에서 "non-trivial한 부분"에 해당한다. 즉, $$I$$가 정의하는 $$k \times k$$ block이 identity로 고정된 후, 나머지 $$(n-k) \times k$$ block이 자유롭게 변할 수 있다. 특히 다음이 성립한다.

<div class="proposition" markdown="1">

<ins id="prop5">**명제 5**</ins> $$\dim \Gr(k, n) = k(n - k)$$이다.

</div>

## Plücker Embedding

위의 설명은 

이제 $$\Gr(k, n)$$를 사영공간의 부분집합으로 실현하는 Plücker embedding을 소개한다. 이는 exterior product (외적)를 사용한다. $$\bigwedge^k V$$는 alternating $$k$$-linear form들의 공간으로, 자세한 정의와 성질은 [§텐서대수, ⁋정의 10](/ko/math/multilinear_algebra/tensor_algebras#def10)과 [§텐서대수, ⁋명제 13](/ko/math/multilinear_algebra/tensor_algebras#prop13)을 참조하라. 여기서는 Plücker embedding에 필요한 핵심 성질만 요약한다.

$$v_1 \wedge \cdots \wedge v_k$$ 꼴의 원소를 *decomposable*이라 부르며, $$v_1, \ldots, v_k$$가 linearly independent일 때에만 0이 아니다. $$\dim \bigwedge^k V = \binom{n}{k}$$이다. Plücker embedding의 핵심 아이디어는 부분공간 $$W = \operatorname{span}(v_1, \ldots, v_k)$$를 $$v_1 \wedge \cdots \wedge v_k$$라는 하나의 벡터로 대응시켜 $$W$$의 기하학적 정보를 exterior power의 원소로 인코딩하는 것이다.

<div class="definition" markdown="1">

<ins id="def5">**정의 5**</ins> *Plücker embedding* $$\iota: \Gr(k, n) \to \mathbb{P}(\bigwedge^k \mathbb{K}^n)$$을 다음과 같이 정의한다. $$k$$차원 부분공간 $$W = \operatorname{span}(v_1, \ldots, v_k)$$에 대해

$$\iota(W) = [v_1 \wedge v_2 \wedge \cdots \wedge v_k]$$

이다.

</div>

여기서 $$\bigwedge^k \mathbb{K}^n$$은 $$\mathbb{K}^n$$의 $$k$$번째 exterior power이고, $$v_1 \wedge \cdots \wedge v_k$$는 decomposable $$k$$-vector이다. $$\dim \bigwedge^k \mathbb{K}^n = \binom{n}{k}$$이므로, $$\mathbb{P}(\bigwedge^k \mathbb{K}^n) \cong \mathbb{P}^{\binom{n}{k}-1}$$이다.

<div class="proposition" markdown="1">

<ins id="prop6">**명제 6**</ins> Plücker embedding은 well-defined이며 injective이다.

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

<ins id="prop7">**명제 7**</ins> Plücker embedding의 image는 $$\mathbb{P}^{\binom{n}{k}-1}$$의 사영다양체이다. 위에서 이미 $$\Gr(k, n)$$에 variety 구조를 부여했으므로, 이 명제는 $$\Gr(k, n)$$이 *사영*다양체임을 보여준다.

</div>

이 명제의 핵심은 Plücker embedding의 image가 사영공간에서 polynomial equations로 정의된 닫힌집합이라는 것이다. 구체적으로, $$k$$-vector $$v$$가 decomposable (즉, $$v = v_1 \wedge \cdots \wedge v_k$$의 꼴)일 조건은 *Plücker relations*라 불리는 polynomial equations로 표현된다. 이 방정식들의 해집합은 사영공간의 닫힌집합이고, $$\iota$$의 image는 정확히 이 해집합이다. 따라서 $$\Gr(k, n) \cong \operatorname{im} \iota$$는 사영다양체이다. Plücker relations의 구체적인 형태는 다음 절에서 다룬다. 이 정리는 그라스만다양체가 "well-behaved" 대수적 대상임을 보여준다.



## Plücker Relations

Plücker embedding의 image를 정의하는 방정식들을 *Plücker relations*라 부른다. 이들은 exterior product의 성질에서 유래한다. Plücker relations는 그라스만다양체를 "explicitly" 정의하는 방정식들을 제공한다.

$$\bigwedge^k \mathbb{K}^n$$의 모든 원소가 decomposable (즉, $$v_1 \wedge \cdots \wedge v_k$$의 꼴)인 것은 아니다. 예를 들어 $$\bigwedge^2 \mathbb{K}^4$$에서 $$e_1 \wedge e_2 + e_3 \wedge e_4$$는 decomposable이 아니다. Plücker relations는 어떤 $$k$$-vector가 decomposable일 조건을 명시한다. Decomposable $$k$$-vector만이 그라스만다양체의 점에 대응된다.

<div class="proposition" markdown="1">

<ins id="prop9">**명제 9**</ins> $$v \in \bigwedge^k \mathbb{K}^n$$이 decomposable일 필요충분조건은 모든 $$w \in \bigwedge^{k-1} \mathbb{K}^n$$에 대해

$$(v \wedge w) \wedge (v \wedge w) = 0 \in \bigwedge^{2k} \mathbb{K}^n$$

인 것이다.

</div>

이 조건을 Plücker coordinates로 쓰면 구체적인 방정식들을 얻는다. Plücker coordinates $$p_{i_1 \cdots i_k}$$는 $$v = \sum_{i_1 < \cdots < i_k} p_{i_1 \cdots i_k} e_{i_1} \wedge \cdots \wedge e_{i_k}$$에서의 계수들이다. 이들은 $$\Gr(k, n)$$의 "자연스러운 좌표계"이다.

<div class="example" markdown="1">

<ins id="ex10">**예시 10**</ins> **$$\Gr(2, 4)$$의 Plücker relation**: $$\Gr(2, 4)$$를 생각하자. Plücker coordinates는 $$p_{12}, p_{13}, p_{14}, p_{23}, p_{24}, p_{34}$$이고, 이는 $$\mathbb{P}^5$$의 homogeneous coordinates이다. 유일한 Plücker relation은

$$p_{12} p_{34} - p_{13} p_{24} + p_{14} p_{23} = 0$$

이다. 이는 quadratic equation이므로 $$\Gr(2, 4)$$는 $$\mathbb{P}^5$$의 quadric hypersurface이다. 기하학적으로, $$\Gr(2, 4)$$는 4차원 quadric이며 smooth하다. 이 방정식은 $$\mathbb{P}^3$$의 두 직선이 만날 조건을 Plücker coordinates로 표현한 것과 관련이 있다.

</div>

Plücker relations의 기하학적 의미는 다음과 같다. $$W \in \Gr(k, n)$$이 주어지면, Plücker coordinates $$p_{i_1 \cdots i_k}$$는 $$W$$를 나타내는 행렬의 $$k \times k$$ minors (up to sign)이다. Plücker relation은 이들 minors 사이의 관계식이다. 이는 "선형대수적 identity"가 "기하학적 방정식"으로 나타남을 보여준다.

## Schubert Varieties

그라스만다양체의 가장 중요한 닫힌부분다양체들은 Schubert varieties이다. 이들은 flag (깃발)와 관련된 기하학적 조건으로 정의된다. Schubert varieties는 intersection theory의 기본 도구이다.

먼저 flag와 partition의 개념을 정의하자. *Flag*는 서로 포함관계를 이루는 부분공간들의 사슬 $$0 = V_0 \subset V_1 \subset \cdots \subset V_n = \mathbb{K}^n$$이다. 여기서 각 $$V_i$$는 $$i$$차원 부분공간이다. Flag는 "기준이 되는 부분공간들의 체인"을 제공한다. *Partition*은 조건 $$\lambda_1 \ge \lambda_2 \ge \cdots \ge \lambda_k \ge 0$$을 만족하는 정수열 $$\lambda = (\lambda_1, \ldots, \lambda_k)$$이다. Partition의 *크기*는 $$\lvert\lambda\rvert = \lambda_1 + \cdots + \lambda_k$$로 정의한다. Flag와 partition이 만나면, partition이 flag의 각 단계와 "얼마나 교차하는지"를 수치화하여 Schubert variety를 정의하는 데 사용된다.

<div class="definition" markdown="1">

<ins id="def11">**정의 11**</ins> *Flag* $$0 = V_0 \subset V_1 \subset \cdots \subset V_n = \mathbb{K}^n$$와 partition $$\lambda = (\lambda_1 \ge \cdots \ge \lambda_k \ge 0)$$ (단, $$\lambda_1 \le n-k$$)에 대해 *Schubert variety* $$\Omega_\lambda$$를

$$\Omega_\lambda = \{W \in \Gr(k, n) \mid \dim(W \cap V_{n-k+i-\lambda_i}) \ge i \text{ for all } i = 1, \ldots, k\}$$

으로 정의한다.

</div>

Schubert variety의 정의는 복잡해 보이지만, 기하학적 의미는 명확하다. $$\Omega_\lambda$$는 주어진 flag와 특정한 "교차 조건"을 만족하는 부분공간 $$W$$들의 모임이다. 조건 $$\dim(W \cap V_{n-k+i-\lambda_i}) \ge i$$는 $$W$$가 $$V_{n-k+i-\lambda_i}$$와 적어도 $$i$$차원만큼 교차해야 함을 의미한다. 이는 "$$W$$가 얼마나 '특별한' 위치에 있는가"를 측정한다.

<div class="proposition" markdown="1">

<ins id="prop12">**명제 12**</ins> $$\dim \Omega_\lambda = \lvert\lambda\rvert = \lambda_1 + \cdots + \lambda_k$$이다.

</div>

<details class="proof" markdown="1">
<summary>증명</summary>

Standard flag $$V_i = \operatorname{span}(e_1, \ldots, e_i)$$를 사용하자. $$\Omega_\lambda$$의 codimension을 계산하면, $$\Gr(k, n)$$의 affine chart $$U_{\{1,\ldots,k\}}$$에서 $$W$$는 행렬 $$\begin{pmatrix} I_k \\ B \end{pmatrix}$$로 나타내어진다. 여기서 $$B = (b_{ij})$$는 $$(n-k) \times k$$ 행렬이다.

조건 $$\dim(W \cap V_{n-k+i-\lambda_i}) \ge i$$를 $$B$$의 entry들에 대한 제약조건으로 번역하자. $$W$$의 처음 $$j$$개 basis vector가 $$V_{n-k+i-\lambda_i}$$에 포함되려면, $$B$$의 관련된 entry들이 0이어야 한다. 구체적으로, 각 $$i = 1, \ldots, k$$에 대해 $$\lambda_i$$개의 독립적인 linear condition이 $$B$$의 entry들에 부과된다. 예를 들어 $$i = 1$$일 때, $$W$$의 첫 번째 basis vector가 $$V_{n-k+1-\lambda_1}$$에 속하면 $$B$$의 처음 $$\lambda_1$$개 row의 첫 번째 column이 0이어야 한다. 이를 모든 $$i$$에 대해 반복하면, 총 $$\sum_{i=1}^k \lambda_i = \lvert\lambda\rvert$$개의 독립적인 조건이 나온다.

이러한 조건들은 서로 독립이며 (각 조건이 $$B$$의 서로 다른 entry에 관련됨), 따라서 $$\Omega_\lambda$$의 codimension은 $$\lvert\lambda\rvert$$이다. 따라서

$$\dim \Omega_\lambda = \dim \Gr(k, n) - \lvert\lambda\rvert = k(n-k) - (k(n-k) - \lvert\lambda\rvert) = \lvert\lambda\rvert$$

이다.

</details>

<div class="example" markdown="1">

<ins id="ex13">**예시 13**</ins> **$$\Gr(2, 4)$$의 Schubert varieties**: $$\Gr(2, 4)$$에서 가능한 partitions은 $$(0,0)$$, $$(1,0)$$, $$(2,0)$$, $$(1,1)$$, $$(2,1)$$, $$(2,2)$$이다.

- $$\Omega_{(0,0)} = \Gr(2,4)$$: 전체 그라스만다양체 (조건 없음). "가장 일반적인" 부분공간들.
- $$\Omega_{(1,0)}$$: hyperplane section, $$\dim = 1$$. $$W$$가 특정 3차원 부분공간과 1차원 이상 교차하는 조건. "약간 특별한" 부분공간들.
- $$\Omega_{(2,0)} \cong \mathbb{P}^2$$, $$\dim = 2$$. $$W$$가 특정 2차원 부분공간을 포함하는 조건. "특정 평면을 포함하는" 직선들.
- $$\Omega_{(1,1)} \cong \mathbb{P}^1 \times \mathbb{P}^1$$, $$\dim = 2$$. $$W$$가 두 개의 3차원 부분공간과 각각 1차원 이상 교차하는 조건. "두 hyperplane의 교차"에 있는 직선들.
- $$\Omega_{(2,1)} \cong \mathbb{P}^1$$, $$\dim = 1$$. $$W$$가 특정 2차원 부분공간을 포함하고 특정 3차원 부분공간과 2차원 이상 교차하는 조건. "매우 특별한" 직선들.
- $$\Omega_{(2,2)}$$: single point, $$\dim = 0$$. $$W$$가 특정 2차원 부분공간과 같은 조건. "완전히 결정된" 부분공간.

</div>

<div class="misc" markdown="1">

Schubert varieties의 중요성은 다음과 같다:

1. **Cell decomposition**: $$\Gr(k, n)$$은 Schubert cells (Schubert varieties의 interior)들의 disjoint union으로 분해된다. 이를 통해 그라스만다양체에 CW 복합체 구조를 부여할 수 있으며, 위상적 성질을 조합적으로 계산할 수 있다.
2. **Cohomology**[^1]: Schubert varieties의 cohomology classes는 $$\Gr(k, n)$$의 cohomology ring의 basis를 이룬다. 이러한 basis 원소들을 *Schubert classes*라 부르며, 그라스만다양체의 위상적 불변량을 계산하는 핵심 도구이다.
3. **Intersection theory**: Schubert calculus는 Schubert varieties의 교차를 계산하는 방법이다. 이는 enumerative geometry의 핵심으로, "몇 개의 부분공간이 주어진 조건을 만족하는가"라는 기하학적 질문에 구체적인 수치적 답을 제공한다.

</div>

## 응용

<div class="example" markdown="1">

<ins id="ex14">**예시 14**</ins> **$$\mathbb{P}^3$$의 직선들**: $$\Gr(2, 4)$$는 $$\mathbb{P}^3$$의 직선들의 공간이다. $$\mathbb{P}^3$$의 두 직선 $$L_1, L_2$$가 만나는 조건은 Plücker coordinates로 다음과 같이 표현된다. $$L_1, L_2$$의 Plücker coordinates를 $$p_{ij}, q_{ij}$$라 하면, $$L_1$$과 $$L_2$$가 만날 필요충분조건은

$$p_{12} q_{34} - p_{13} q_{24} + p_{14} q_{23} + p_{23} q_{14} - p_{24} q_{13} + p_{34} q_{12} = 0$$

이다. 이는 $$\Gr(2, 4)$$ 위의 bilinear form이다. 기하학적으로, 이 식은 두 직선의 "상대적 위치"를 Plücker coordinates로 표현한 것이다. 이는 선형대수적 조건이 기하학적 조건과 어떻게 연결되는지를 보여주는 좋은 예시이다.

</div>

<div class="example" markdown="1">

<ins id="ex15">**예시 15**</ins> **Veronese embedding과 Segre embedding**: 그라스만다양체는 다른 중요한 embedding들의 일반화이다.

<div class="misc" markdown="1">

- Veronese embedding $$\mathbb{P}^n \to \mathbb{P}^N$$은 $$\Gr(1, n+1) \to \mathbb{P}^n$$의 "higher degree" 버전으로 볼 수 있다. 이는 사영공간을 "고차원" 공간으로 embedding하는 방법이다.
- Segre embedding $$\mathbb{P}^m \times \mathbb{P}^n \to \mathbb{P}^{mn+m+n}$$은 product의 embedding이다. $$\mathbb{P}^1 \times \mathbb{P}^1$$은 $$\Gr(2, 4)$$의 Schubert variety $$\Omega_{(1,1)}$$와 isomorphic하다. 이는 product variety가 그라스만다양체의 부분다양체로 나타남을 보여준다.

</div>

</div>

<div class="example" markdown="1">

<ins id="ex16">**예시 16**</ins> **Moduli of vector bundles**[^2]: 그라스만다양체는 vector bundle들의 moduli space를 연구하는 기본 도구이다. 주어진 vector bundle $$E$$ on $$X$$의 [section](https://en.wikipedia.org/wiki/Section_(fiber_bundle))들의 공간 $$H^0(X, E)$$의 $$k$$차원 부분공간들의 모임은 $$\Gr(k, H^0(X, E))$$의 닫힌부분다양체로 나타난다. 이를 통해 vector bundle의 성질을 기하학적으로 연구할 수 있다. 예를 들어, [line bundle](https://en.wikipedia.org/wiki/Line_bundle)[^3]의 section들의 공간은 사영공간이고, 이들의 부분공간들의 모임은 그라스만다양체이다. 이는 "vector bundle의 기하학"과 "선형대수의 기하학"을 연결한다.

</div>

---

[^1]: *Cohomology ring*은 다양체의 위상적 불변량을 대수적으로 나타내는 구조이다. 이 글의 범위를 넘어서는 개념이지만, Schubert varieties의 cohomology classes가 그라스만다양체의 cohomology ring의 basis를 이룬다는 사실은 이론대수기하학에서 중요한 정리이다.

[^2]: *Vector bundle*은 다양체 위의 점마다 벡터공간을 대응시키는 구조이다. 이 개념은 이 글의 선행 내용에서 정의되지 않았으므로, 이 예시는 참고용으로만 이해하면 된다.

[^3]: *Line bundle*은 rank 1인 vector bundle로, 다양체 위의 각 점에 1차원 벡터공간을 대응시키는 구조이다. 가장 기본적인 예시로는 사영공간의 tautological line bundle $$\mathcal{O}(-1)$$이 있다.

---

**참고문헌**

**[Har]** J. Harris, *Algebraic Geometry: A First Course*, Springer, 1992.  
**[GH]** P. Griffiths and J. Harris, *Principles of Algebraic Geometry*, Wiley, 1978.  
**[Ful]** W. Fulton, *Young Tableaux*, Cambridge University Press