---
title: "피카드 그룹 (Picard Group)"
excerpt: "Picard group of algebraic varieties"

categories: [Math / Algebraic Geometry]
permalink: /ko/math/algebraic_geometry/picard_group
sidebar:
    nav: "algebraic_geometry-ko"

header:
    overlay_image: /assets/images/Math/Algebraic_Geometry/Picard_Group.png
    overlay_filter: 0.5

date: 2026-03-12
last_modified_at: 2026-03-15
weight: 11

---

피카드 그룹(Picard group)은 대수다양체 위의 line bundle들의 isomorphism 클래스들로 구성된 abelian group이다. 이 그룹은 다양체의 "topology" (cohomology)와 밀접한 관계가 있으며, 다양체의 어떤 "twist"를 포착한다. 이 절에서 우리는 Picard group의 정의, 주요 예시, 그리고 그 기하학적 의미를 살펴볼 것이다.

## 정의

피카드 그룹의 기본 아이디어는 line bundle들을 "equivalence"에 의해 group으로 만드는 것이다. Equivalence relation은 isomorphism이며, group operation은 tensor product이다.

<div class="definition" markdown="1">

<ins id="def1">**정의 1**</ins> 다양체 $$X$$ 위의 *Picard group* $$\mathrm{Pic}(X)$$는 다음과 같이 정의된다.\n\n$$\mathrm{Pic}(X) = \mathrm{Hom}(\mathrm{Pic}(X), \mathbb{Z})$$\n\n여기서 $$\mathrm{Hom}$$은 line bundle들의 isomorphism classes의 set이고, group operation은 tensor product이다. Zero element은 trivial line bundle $$\mathcal{O}_X$$이다.\n\n</div>

기하학적으로, Picard group는 "나침반의 방향"을 측정한다. 즉, 어떤 line bundle이 기본 line bundle (trivial bundle)과 "twisted"되었는지를 측정한다. Picard group의 zero element은 trivial bundle $$\mathcal{O}_X$$이며, inverse는 dual bundle $$\mathcal{L}^\vee$$이다.

<div class="proposition" markdown="1">

<ins id="prop2">**명제 2**</ins> 피카드 그룹 $$\mathrm{Pic}(X)$$는 abelian group이다.\n\n</div>

<details class="proof" markdown="1">
<summary>증명</summary>

Line bundle tensor product은 commutative이므로, $$\mathrm{Pic}(X)$$도 commutative abelian group이다. Identity element은 trivial bundle $$\mathcal{O}_X$$이고, inverse는 dual bundle $$\mathcal{L}^\vee$$이다. Associativity과 inverses는 tensor product property로부터 증명된다.\n\n</details>

<div class="proposition" markdown="1">

<ins id="prop3">**명제 3**</ins> 다양체 $$X$$ 위의 피카드 그룹 $$\mathrm{Pic}(X)$$와 divisor class group $$\mathrm{Cl}(X)$$는 isomorphic하다.\n\n</div>

<details class="proof" markdown="1">
<summary>증명</summary>

Divisor $$D$$에 associated line bundle $$\mathcal{L}_D$$를 정의하고, line bundle $$\mathcal{L}$$에 associated divisor $$\mathrm{div}(\mathcal{L})$$를 정의한다. Principal divisor에 대해 trivial bundle을 유도하므로, quotient는 isomorphic하다. This isomorphism is natural.\n\n</details>

## 주요 예시

Picard group의 주요 예시를 살펴보겠다. 이들은 Picard group의 구조를 이해하는 데 중요하다.

<div class="example" markdown="1">

<ins id="ex4">**예시 4**</ins> **Affine space** $$\mathbb{A}^n$$\n\n$$\mathrm{Pic}(\mathbb{A}^n) = 0$$\n\n이유는 모든 line bundle이 trivial bundle과 isomorphic이기 때문이다. Affine space는 "contractible"하여 모든 line bundle이 pullback을 통해 trivial화될 수 있다.\n\n</div>

<div class="example" markdown="1">

<ins id="ex5">**예시 5**</ins> **Projective space** $$\mathbb{P}^n$$\n\n$$\mathrm{Pic}(\mathbb{P}^n) \cong \mathbb{Z}$$\n\n이 그룹은 hyperplane bundle $$\mathcal{O}_{\mathbb{P}^n}(1)$$에 의해 생성된다. $$k$$-times tensor $$\mathcal{O}_{\mathbb{P}^n}(k)$$는 degree $$k$$를 가진다. 이는 Picard group가 "torsion-free"임을 보여준다.\n\n</div>

<div class="example" markdown="1">

<ins id="ex6">**예시 6**</ins> **Singular curves**\n\nSingular curve $$X$$의 Picard group는 singular point에 따라 달라진다. $$X$$가 smooth이면 $$\mathrm{Pic}(X)$$는 finitely generated abelian group이지만, singular인 경우 "torsion" component가 추가될 수 있다.\n\n</div>

<div class="example" markdown="1">

<ins id="ex7">**예시 7**</ins> **Abelian varieties**\n\nAbelian variety $$A$$의 Picard group는 축소되지 않고, 쌍유리동치 invariant이다. $$\mathrm{Pic}(A) \cong \mathrm{Pic}^0(A) \oplus \mathrm{NS}(A)$$ where $$\mathrm{Pic}^0(A)$$는 torsion-free part.\n\n</div>

<div class="example" markdown="1">

<ins id="ex8">**예시 8**</ins> **K3 surfaces**\n\nK3 surface $$X$$의 Picard group는 0 $$\leq$$ rank $$\leq$$ 20이다. Maximal rank 20일 때, Picard number $$\rho(X) = 20$$이라고 부른다. 이는 K3 surface의 topology에 강하게 의존한다.\n\n</div>

## 떼러 (Torsion)

Picard group의 torsion component는 line bundle이 "finite order"를 가지는 경우이다.

<div class="definition" markdown="1">

<ins id="def9">**정의 9**</ins> Picard group $$\mathrm{Pic}(X)$$의 *torsion subgroup* $$\mathrm{Pic}^t(X)$$는 finite order를 가지는 element들의 집합이다.\n\n</div>

기하학적으로, torsion line bundles는 "부분적으로" contractible한 것과 관련이 있다. 이들은 "phase transition"이나 "vortex"와 같은 현상을 설명하는 데 사용된다.

<div class="proposition" markdown="1">

<ins id="prop10">**명제 10**</ins> Projective space $$\mathbb{P}^n$$의 Picard group는 torsion-free이다. $$\mathrm{Pic}^t(\mathbb{P}^n) = 0$$.\n\n</div>

<details class="proof" markdown="1">
<summary>증명</summary>

Picard group $$\mathrm{Pic}(\mathbb{P}^n) \cong \mathbb{Z}$$는 free abelian group이므로, torsion element가 없다. 이는 hyperplane bundle $$\mathcal{O}_{\mathbb{P}^n}(1)$$이 primitive generator임을 보여준다.\n\n</details>

## Cohomology와의 연결

Picard group는 cohomology와 밀접한 관계가 있다. 특히, H^1(X, O_X^\ast)와의 연결이 중요하다.

<div class="proposition" markdown="1">

<ins id="prop11">**명제 11**</ins> 피카드 그룹 $$\mathrm{Pic}(X)$$는 $$H^1(X, \mathcal{O}_X^\ast)$$와 isomorphic하다.\n\n</div>

<details class="proof" markdown="1">
<summary>증명</summary>

Line bundle은 Čech cohomology $$H^1(X, \mathcal{O}_X^\ast)$$의 class로 정의된다. Transition functions $$g_{ij} \in \mathcal{O}_X(U_i \cap U_j)^\ast$$은 cocycle이고, 이들의 equivalence class는 line bundle이다. This isomorphism is natural.\n\n</details>

<div class="proposition" markdown="1">

<ins id="prop12">**명제 12**</ins> Smooth projective variety $$X$$의 Picard group는 다음과 같은 exact sequence를 갖는다.\n\n$$0 \to \mathrm{Pic}^0(X) \to \mathrm{Pic}(X) \to \mathrm{NS}(X) \to 0$$\n\n</div>

<details class="proof" markdown="1">
<summary>증명</summary>

Exact sequence from Cech cohomology. $$\mathrm{Pic}^0(X)$$ is torsion-free part and $$\mathrm{NS}(X)$$ is Néron-Severi group. This sequence splits.\n\n</details>

## Application: Base Change

Picard group은 base change에 어떻게 작용하는지를 이해하는 데 중요하다.

<div class="proposition" markdown="1">

<ins id="prop13">**명제 13**</ins> 기역 다양체 $$X$$ 위의 line bundle $$\mathcal{L}$$가 base field $$\mathbb{K}$$에서 trivial이면, $$X_K$$에서도 trivial이다.\n\n</div>

<details class="proof" markdown="1">
<summary>증명</summary>

Base field 확장 $$K/\mathbb{K}$$에 대해, pullback $$\mathcal{L}_K = \mathcal{L} \otimes_{\mathbb{K}} K$$는 tensor product이므로, trivial line bundle의 tensor product은 trivial이다.\n\n</details>

---\n\n**참고문헌**\n\n**[Har]** J. Harris, *Algebraic Geometry: A First Course*, Springer, 1992.\n**[Sha]** I. R. Shafarevich, *Basic Algebraic Geometry I: Varieties in Projective Space*, Springer, 2013.\n**[Gr]** P. Griffiths and J. Harris, *Principles of Algebraic Geometry*, Wiley, 1978.\n**[Ful]** W. Fulton, *Intersection Theory*, Springer, 1984.\n