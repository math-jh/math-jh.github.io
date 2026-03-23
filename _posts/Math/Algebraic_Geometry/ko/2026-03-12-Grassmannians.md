---
title: "그라스만 다양체"
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

이번 글에서 $$V$$는 항상 $$n$$차원 공간으로 가정한다. 

물론 이것이 variety 구조를 갖는다는 것은 별도로 보여야 하지만, 핵심적인 결과는 이것이 variety 구조를 가질 뿐 아니라 $$\mathbb{A}^n$$에서 각각의 $$k$$-plane들의 위치관계까지 잘 보존하는 구조를 주므로 큰 신경을 쓰지 않아도 우리가 원하는대로 행동한다는 것이다. 

<div class="example" markdown="1">

<ins id="ex2">**예시 2**</ins> 가령, $$\Gr(1, n+1)$$은 $$n+1$$차원 벡터공간 $$\mathbb{K}^{n+1}$$의 line들의 공간이므로, 정의에 의해 이는 $$\mathbb{P}^n$$과 같다. 곧 Grassmannian 위의 variety 구조를 정의한 후에는 이 두 구조가 정확히 같다는 것을 알게 될 것이다. 

기존에 없던 예시 중 가장 간단한 것은 $$\Gr(2,4)$$이다. 이는 $$4$$차원 공간의 $$2$$차원 부분공간들의 모임이다. Grassmannian을 다룰 때는 이 예시가 toy example로서 기능할 것이다. 

</div>

언제나 그렇듯이 variety 구조를 주기 위해서는 affine cover를 생각해서 affine-local하게 접근하면 된다. 이를 위해 다음을 정의한다. 

<div class="definition" markdown="1">

<ins id="def3">**정의 3**</ins> 각 $$k$$개의 index들 $$I = \{i_1 < \cdots < i_k\}$$에 대해 open set $$U_I$$를

$$U_I = \{W \in \Gr(k, V) \mid \text{projection } W \to \operatorname{span}(e_{i_1}, \ldots, e_{i_k}) \text{ is an isomorphism}\}$$

으로 정의한다.

</div>

$$V$$의 basis $$e_1,\ldots, e_n$$을 고정하고, $$W$$를 span하는 각각의 벡터들 $$w_1,\ldots, w_k$$을 사용하면 $$W$$는 다음 $$k\times n$$ 행렬

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

이 증명에서 보듯, $$U_I$$에서의 좌표계는 $$k(n-k)$$개의 자유로운 parameter들이다. 이들은 $$W$$를 나타내는 행렬에서 "non-trivial한 부분"에 해당한다. 즉, $$I$$가 정의하는 $$k \times k$$ block이 identity로 고정된 후, 나머지 $$(n-k) \times k$$ block이 자유롭게 변할 수 있다. 

그럼 임의의 $$W\in \Gr(k,V)$$에 대하여 $$W$$를 포함하는 affine open cover가 존재함은 자명하다. 뿐만 아니라 $$U_I$$에서 $$U_J$$로의 transition map 또한 regular map이라는 것이 자명하므로, 이를 통해 $$\Gr(k,V)$$ 위에 variety 구조가 주어진다. 물론 이것이 quasi-projective임을 보이기 위해서는 명시적인 projective embedding이 필요하지만, 우선은 다음이 성립한다. 

<div class="proposition" markdown="1">

<ins id="prop5">**명제 5**</ins> $$\dim \Gr(k, V) = k(n - k)$$이다.

</div>

## Plücker Embedding

이제 우리는 Grassmannian이 quasi-projective variety임을 보인다. 즉, Grassmannian에서 적당한 projective space로의 embedding을 정의한다. 

<div class="definition" markdown="1">

<ins id="def6">**정의 6**</ins> *Plücker embedding* $$\iota: \Gr(k, V) \to \mathbb{P}(\bigwedge^k V)$$는 $$k$$차원 부분공간 $$W = \operatorname{span}(v_1, \ldots, v_k)$$에 다음의 원소

$$\iota(W) = [v_1 \wedge v_2 \wedge \cdots \wedge v_k]$$

를 대응시키는 함수이다. ([\[다중선형대수힉\] §텐서대수, ⁋정의 10](/ko/math/multilinear_algebra/tensor_algebras#def10))

</div>

그럼 다음이 성립한다. 

<div class="proposition" markdown="1">

<ins id="prop7">**명제 7**</ins> Plücker embedding은 well-defined이며 injective이다.

</div>

<details class="proof" markdown="1">
<summary>증명</summary>

Plücker embedding이 잘 정의된다는 것은 $$W$$의 다른 basis를 택했을 때 위의 값이 변하지 않는다는 것이다. 그런데 $$W$$의 다른 basis를 택한다면, $$v_1\wedge\cdots\wedge v_k$$는 change-of-basis matrix의 determinant만큼만 scaling되므로, 이를 $$\mathbb{P}(\bigwedge^k V)$$로 보내면 어차피 같은 점을 지정한다. 비슷한 논증을 거꾸로 하면 injectivity 또한 쉽게 보일 수 있다. 

</details>

뿐만 아니라, $$\iota$$는 $$\Gr(k,V)$$를 $$\mathbb{P}(\bigwedge^kV)$$의 *closed* subvariety로서 정의한다. 이를 위해 $$\iota$$의 image를 살펴보면, $$\iota$$의 image는 정확하게 *decomposable* vector들, 즉 다음의 꼴

$$v_1\wedge\cdots\wedge v_k$$

로 나타나는 벡터들로 이루어진 것을 알 수 있다. 따라서 $$\iota$$의 image가 closed subvariety임을 주장하기 위해서는 이들을 zero set으로 갖는 다항식을 정의하면 되고, 이는 wedge product의 성질로부터 다음의 *Plücker relations*

$$\sum_{r=1}^{k+1} (-1)^r p_{i_1 \cdots i_{k-1} j_r} p_{j_1 \cdots \widehat{j_r} \cdots j_{k+1}} = 0\tag{$\ast$}$$

을 통해 얻어진다. 여기서 $$i_1 < \cdots < i_{k-1}$$과 $$j_1 < \cdots < j_{k+1}$$은 $$\{1, \ldots, n\}$$의 임의의 부분집합이며, $$\widehat{j_r}$$은 $$j_r$$을 생략한다는 의미이다. 이 방정식들은 모든 가능한 $$i$$들과 $$j$$들에 대해 성립한다. 이를 통해 다음을 얻는다. 

<div class="proposition" markdown="1">

<ins id="prop8">**명제 8**</ins> Plücker embedding의 image는 $$\mathbb{P}^{\binom{n}{k}-1}$$의 closed subvariety이며, 따라서 $$\Gr(k,V)$$는 projective variety이다. 

</div>

<div class="example" markdown="1">

<ins id="ex9">**예시 9**</ins> $$\Gr(2,4)$$에서 Plücker relation ($$\ast$$)을 살펴보자. Plücker coordinates는 $$p_{12}, p_{13}, p_{14}, p_{23}, p_{24}, p_{34}$$이고, 이것이 $$\mathbb{P}^5$$의 homogeneous coordinates이다. 그럼 Plücker relation은 유일한 3-term relation

$$p_{12} p_{34} - p_{13} p_{24} + p_{14} p_{23} = 0$$

으로 주어진다. 이는 quadratic equation이므로 $$\Gr(2, 4)$$는 $$\mathbb{P}^5$$의 quadric hypersurface이다. 만일 $$V$$의 차원이 높아진다면 이러한 equation이 더 여러개 나올 것이며, $$k$$가 커진다면 각각의 equation들의 항이 더 많아질 것이다. 

</div>

## Schubert Varieties

Grassmannian은 일종의 cell structure가 주어져서 조합론적인 관점에서 이해할 수 있다. 이를 위해 우선 flag와 partition의 개념을 정의한다.

<div class="definition" markdown="1">

<ins id="def10">**정의 10**</ins> $$n$$차원 벡터공간 $$V$$의 *flag<sub>깃발</sub>*은 다음과 같은 부분공간들의 chain

$$F_\bullet:\qquad 0 = F_0 \subset F_1 \subset F_2 \subset \cdots \subset F_n = V$$

이다. 여기서 $$\dim F_i = i$$이다.

</div>

<div class="example" markdown="1">

<ins id="ex11">**예시 11**</ins> $$V = \mathbb{K}^n$$에 standard basis $$e_1, \ldots, e_n$$이 주어져 있을 때, *standard flag*은

$$F_i = \operatorname{span}(e_1, \ldots, e_i)$$

으로 정의된다.

</div>

이제 $$\Gr(k, V)$$의 원소인 $$k$$차원 부분공간 $$W$$가 주어졌을 때, 이 $$W$$와 flag $$F_\bullet$$이 어떻게 만나는지를 단계별로 추적할 수 있다. 수열

$$0 = \dim(W \cap F_0) \leq \dim(W \cap F_1) \leq \cdots \leq \dim(W \cap F_n) = k$$

을 생각하면, 각 단계에서 차원은 최대 $$1$$씩 증가한다. 이 정보를 간결하게 나타내기 위해 partition을 사용한다.

<div class="definition" markdown="1">

<ins id="def12">**정의 12**</ins> $$k$$개의 정수들로 이루어진 수열 $$\lambda = (\lambda_1, \ldots, \lambda_k)$$가 다음 조건

$$\lambda_1 \geq \lambda_2 \geq \cdots \geq \lambda_k \geq 0,\qquad \lambda_1 \leq n - k$$

을 만족할 때 이를 *partition<sub>분할</sub>*이라 부른다. Partition $$\lambda$$의 *크기*는 $$\lvert \lambda \rvert = \sum_{i=1}^{k} \lambda_i$$로 정의된다.

</div>

Partition은 기하학적으로 *Young diagram*으로 시각화할 수 있다. 이는 $$\lambda_1$$개의 box가 있는 첫 번째 row, $$\lambda_2$$개의 box가 있는 두 번째 row, ..., $$\lambda_k$$개의 box가 있는 $$k$$번째 row로 구성된다. 이는 Schubert calculus라 불리는 연산을 쉽게 하도록 도와주지만, 이는 어차피 intersection, 혹은 cohomology에서의 곱셈을 할 때 필요한 것이므로 아직은 소개하지 않는다. 그 대신 다음을 정의한다. 

<div class="definition" markdown="1">

<ins id="def13">**정의 13**</ins> Flag $$F_\bullet$$과 partition $$\lambda = (\lambda_1, \ldots, \lambda_k)$$에 대해, *Schubert variety<sub>슈베르트 다양체</sub>* $$\Omega_\lambda(F_\bullet)$$를 다음의 조건

$$\dim(W \cap F_{n - k + i - \lambda_i}) \geq i \quad\text{for all } 1 \leq i \leq k$$

을 만족하는 $$W \in \Gr(k, V)$$들의 집합으로 정의한다.

</div>

이 조건은 $$W$$와 flag의 교집합의 차원이 특정 패턴을 따른다는 것을 의미한다. 구체적으로, $$W$$는 $$F_{n-k+i-\lambda_i}$$를 최소 $$i$$차원에서 만나야 한다. Partition 조건 $$\lambda_1 \leq n - k$$은 첫 번째 부등식 $$\dim(W \cap F_{n - k + 1 - \lambda_1}) \geq 1$$에서 $$n - k + 1 - \lambda_1 \geq 1$$이 되도록 보장한다.

<div class="proposition" markdown="1">

<ins id="prop14">**명제 14**</ins> Schubert variety $$\Omega_\lambda(F_\bullet)$$는 $$\Gr(k, V)$$의 closed subvariety이며, 그 차원은 $$\lvert \lambda \rvert$$이다.

</div>

<details class="proof" markdown="1">
<summary>증명</summary>

$$\Omega_\lambda(F_\bullet)$$가 closed인 것은 정의 조건이 regular function들의 zero set으로 주어지기 때문이다.

차원을 계산하기 위해, $$\Omega_\lambda(F_\bullet)$$의 (open) *Schubert cell* $$\Omega_\lambda^\circ(F_\bullet)$$를 고려한다. 이는 정의 조건에서 부등식을 등식으로 바꾼 것

$$\dim(W \cap F_{n - k + i - \lambda_i}) = i \quad\text{for all } 1 \leq i \leq k$$

으로 얻어지며, $$\Omega_\lambda(F_\bullet)$$의 open dense subset이다. 이 cell의 차원을 계산하면 $$\lambda_1 + \cdots + \lambda_k = \lvert \lambda \rvert$$이 되며, 따라서 $$\Omega_\lambda(F_\bullet)$$의 차원 또한 $$\lvert \lambda \rvert$$이다.

</details>

Schubert varietie들은 Grassmannian의 *cell decomposition*을 제공한다. 즉, 서로 다른 partition $$\lambda$$에 해당하는 Schubert cell들 $$\Omega_\lambda^\circ(F_\bullet)$$들은 $$\Gr(k, V)$$에 cell complex 구조를 주며, 각 cell은 affine space $$\mathbb{A}^{\lvert \lambda \rvert}$$와 isomorphic하다. 이를 통해 Grassmannian의 위상적, 조합론적 성질을 연구할 수 있다.

---

**참고문헌**

**[Harris]** J. Harris, *Algebraic Geometry: A First Course*, Springer, 1992.  
**[GH]** P. Griffiths and J. Harris, *Principles of Algebraic Geometry*, Wiley, 1978.  
**[Ful]** W. Fulton, *Young Tableaux*, Cambridge University Press