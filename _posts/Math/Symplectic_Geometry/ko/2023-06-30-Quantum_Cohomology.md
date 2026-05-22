---

title: "양자 코호몰로지"
excerpt: "GW invariant를 구조상수로 하는 cup product의 deformation"

categories: [Math / Symplectic Geometry]
permalink: /ko/math/symplectic_geometry/quantum_cohomology
header:
    overlay_image: /assets/images/Math/Symplectic_Geometry/Quantum_Cohomology.png
    overlay_filter: 0.5
sidebar: 
    nav: "symplectic_geometry-ko"

date: 2023-06-30
last_modified_at: 2026-05-20
weight: 8

published: false
---

[§Gromov-Witten 불변량](/ko/math/symplectic_geometry/gromov_witten)에서 우리는 compact symplectic manifold $$X$$와 effective class $$\beta \in H_2(X, \mathbb{Z})$$에 대해 genus-$$0$$, $$n$$-point GW invariant $$\langle \alpha_1, \ldots, \alpha_n \rangle_{0, n, \beta}^X$$를 정의하였다. 그 결과로 얻어진 [§Gromov-Witten 불변량, ⁋명제 6](/ko/math/symplectic_geometry/gromov_witten#prop6)의 WDVV equation은 본질적으로 *어떤 곱셈의 결합법칙*을 진술하는 것이라 하였다. 본 글에서는 그 곱셈을 명시적으로 구성한다. 

3-point GW invariant $$\langle T_a, T_b, T_c \rangle_{0, 3, \beta}^X$$를 구조상수로 삼아 $$H^\ast(X)$$ 위에 새 곱셈을 정의하면, $$\beta = 0$$ 항은 고전적 cup product와 일치하고 $$\beta \neq 0$$ 항은 $$X$$ 위의 rational curve의 기여를 더한다. 이렇게 얻어진 곱셈을 *quantum product*라 부르며, 그에 의한 $$H^\ast(X)$$의 새로운 ring 구조가 *quantum cohomology*이다. 본 글의 목표는 quantum product의 명시적 정의, 그것이 잘 정의된 graded commutative associative ring을 이룬다는 사실의 정리, 그리고 $$\mathbb{P}^n$$에서의 구체적 ring 구조 계산이다.

## Novikov ring

Quantum product의 구조상수에 등장하는 $$\beta$$의 합은 $$\beta$$가 effective인 모든 class에 대한 무한합이다. 이를 형식적으로 정합하게 다루기 위해 우리는 *Novikov ring*이라 불리는 계수환을 도입한다. 

$$X$$를 closed symplectic manifold라 하고, symplectic form을 $$\omega$$로 표기한다. $$H_2(X, \mathbb{Z})$$의 부분집합

$$H_2(X, \mathbb{Z})_{\mathrm{eff}} := \{ \beta \in H_2(X, \mathbb{Z}) \mid \overline{\mathcal{M}}_{0, n}(X, \beta) \neq \emptyset \text{ for some } n \}$$

를 *effective curve class*의 집합이라 부른다. $$J$$-holomorphic curve의 energy $$\omega(\beta) = \int_\beta \omega$$는 effective $$\beta$$에 대해 $$\geq 0$$이며, $$\beta = 0$$이 아닌 한 strict하게 양수이다.

<div class="definition" markdown="1">

<ins id="def1">**정의 1**</ins> $$X$$의 *Novikov ring<sub>노비코프 환</sub>*

$$\Lambda := \left\{ \sum_{\beta \in H_2(X, \mathbb{Z})_{\mathrm{eff}}} a_\beta\, q^\beta\ \middle\vert\ a_\beta \in \mathbb{C},\ \#\{\beta : a_\beta \neq 0,\, \omega(\beta) \leq C\} < \infty \text{ for all } C > 0 \right\}$$

는 effective curve class를 지수로 하는 formal symbol $$q^\beta$$들의 형식적 power series ring으로 정의된다. 덧셈과 곱셈은 $$q^\beta \cdot q^{\beta'} = q^{\beta + \beta'}$$로 주어진다.

</div>

여기서 finiteness 조건 ($$\omega(\beta) \leq C$$인 $$\beta$$ 중 $$a_\beta \neq 0$$인 것이 유한 개)은 $$\Lambda$$의 곱셈이 잘 정의되기 위한 본질적 요구이다. 만약 $$X$$가 Fano (즉 $$c_1(TX)$$가 ample)이고 우리가 small quantum product만 다룬다면 각 cohomology 차수에서 기여하는 $$\beta$$가 유한하므로 단순히 group ring $$\mathbb{C}[H_2(X, \mathbb{Z})_{\mathrm{eff}}]$$로 충분하지만, 일반적 경우를 위해 completion을 둔다.

$$\Lambda$$ 위에 grading을 다음으로 둔다.

<div class="definition" markdown="1">

<ins id="def2">**정의 2**</ins> Novikov variable $$q^\beta$$의 *degree<sub>차수</sub>*는

$$\deg q^\beta := 2 \int_\beta c_1(TX) = 2\, c_1(TX) \cdot \beta$$

로 정의되며, 이로써 $$\Lambda$$는 graded $$\mathbb{C}$$-algebra가 된다.

</div>

이 grading은 임의로 도입한 것이 아니라 [§Stable maps의 moduli space, ⁋명제 5](/ko/math/symplectic_geometry/stable_maps#prop5)의 virtual dimension 공식

$$\mathrm{vdim}_\mathbb{C}\, \overline{\mathcal{M}}_{0, n}(X, \beta) = \int_\beta c_1(TX) + (\dim_\mathbb{C} X - 3) + n$$

에서 자연스럽게 유도된다. $$\beta$$에 의존하는 부분이 정확히 $$\int_\beta c_1(TX)$$이므로, 이를 $$q^\beta$$의 차수로 잡으면 뒤따르는 quantum product가 grading을 보존하게 된다.

<div class="remark" markdown="1">

<ins id="rmk3">**참고 3**</ins> 일부 문헌에서는 $$\deg q^\beta = \int_\beta c_1(TX)$$로 (factor $$2$$ 없이) 정의하기도 한다. 그러나 cohomology에서 *복소* degree와 *실* degree의 일관성을 위해 cohomology class의 degree를 $$\deg_\mathbb{R}$$로 잡는 본 글의 convention에서는 factor $$2$$가 필요하다. McDuff-Salamon [MS]의 convention을 따른다.

</div>

## Quantum product의 정의

이제 우리는 small quantum product를 정의한다. $$X$$의 cohomology $$H^\ast(X, \mathbb{C})$$의 graded basis를 $$\{ T_0 = 1, T_1, \ldots, T_N \}$$이라 하고, Poincaré pairing을

$$\eta_{ab} := \int_X T_a \cup T_b,\qquad (\eta^{ab}) := (\eta_{ab})^{-1}$$

로 놓는다. Dual basis는 $$T^a := \sum_b \eta^{ab} T_b$$로 정의되며, $$\int_X T_a \cup T^b = \delta_a^b$$를 만족한다.

<div class="definition" markdown="1">

<ins id="def4">**정의 4**</ins> *Small quantum product* $$\ast_q : H^\ast(X, \mathbb{C}) \otimes_\mathbb{C} H^\ast(X, \mathbb{C}) \to H^\ast(X, \mathbb{C}) \otimes_\mathbb{C} \Lambda$$는

$$T_a \ast_q T_b := \sum_{\beta \in H_2(X, \mathbb{Z})_{\mathrm{eff}}} \sum_c \langle T_a, T_b, T_c \rangle_{0, 3, \beta}^X\, \eta^{cd}\, T_d\, q^\beta$$

로 정의된다 (반복되는 인덱스 $$c, d$$는 합한다). 양변을 $$\Lambda$$-linear extension하여 $$\ast_q$$를 $$H^\ast(X, \mathbb{C}) \otimes_\mathbb{C} \Lambda$$ 위의 $$\Lambda$$-bilinear product로 확장한다.

</div>

위 공식의 우변에서 $$\langle T_a, T_b, T_c \rangle_{0, 3, \beta}^X$$는 3-point GW invariant이고, $$\eta^{cd} T_d$$는 Poincaré dual을 통한 cohomology class의 raise이다. 즉 $$\sum_c \langle T_a, T_b, T_c \rangle\, T^c$$로 다시 쓸 수 있다. $$\beta = 0$$ 항만 추출하면

$$\langle T_a, T_b, T_c \rangle_{0, 3, 0}^X = \int_X T_a \cup T_b \cup T_c$$

이므로 $$\beta = 0$$ 기여는 정확히 고전적 cup product를 회복한다. 그 외의 $$\beta \neq 0$$ 항은 $$X$$ 위의 비자명한 rational curve의 기여로서, classical cup product의 *quantum 보정*에 해당한다.

<div class="proposition" markdown="1">

<ins id="prop5">**명제 5**</ins> Small quantum product $$\ast_q$$는 grading을 보존한다. 즉

$$\deg(T_a \ast_q T_b) = \deg T_a + \deg T_b$$

가 $$H^\ast(X) \otimes \Lambda$$의 grading ([정의 2](#def2)의 $$\Lambda$$ grading과 cohomology grading의 합) 아래에서 성립한다.

</div>
<details class="proof" markdown="1">
<summary>증명</summary>

[정의 4](#def4)에서 $$T_d q^\beta$$ 항의 계수가 nonzero이려면 GW invariant $$\langle T_a, T_b, T_c \rangle_{0, 3, \beta}^X$$가 nonzero여야 한다. [§Gromov-Witten 불변량, ⁋정의 1](/ko/math/symplectic_geometry/gromov_witten#def1)의 dimension 조건은

$$\deg T_a + \deg T_b + \deg T_c = 2 \mathrm{vdim}_\mathbb{C}\, \overline{\mathcal{M}}_{0, 3}(X, \beta) = 2 \int_\beta c_1(TX) + 2(\dim_\mathbb{C} X - 3) + 6$$

이다. 한편 Poincaré duality에 의해 $$\deg T^c = 2 \dim_\mathbb{C} X - \deg T_c$$이므로, $$\eta^{cd} T_d = T^c$$의 degree는 $$2 \dim_\mathbb{C} X - \deg T_c$$이다. 따라서 $$T_d q^\beta$$ 항의 총 degree는

$$\begin{aligned}
\deg T_d + \deg q^\beta &= (2 \dim_\mathbb{C} X - \deg T_c) + 2 \int_\beta c_1(TX) \\
&= 2 \dim_\mathbb{C} X + (\deg T_a + \deg T_b + \deg T_c - 2(\dim_\mathbb{C} X - 3) - 6) - \deg T_c \\
&= \deg T_a + \deg T_b
\end{aligned}$$

가 되어, $$\ast_q$$가 grading-preserving임이 따른다.

</details>

이 명제는 quantum product가 classical cup product의 *graded* deformation임을 보장한다. $$q^\beta$$의 degree 정의가 정확히 GW invariant의 dimension 조건과 맞물려 있다는 점이 본질적이다.

## Ring 공리

Quantum product가 unit, associativity, super-commutativity의 세 가지 ring 공리를 모두 만족한다는 사실이 이 곱셈을 *quantum cohomology ring*이라 부를 수 있게 한다.

<div class="proposition" markdown="1">

<ins id="thm6">**정리 6** (Quantum cohomology의 ring 공리)</ins> $$X$$를 closed symplectic manifold라 하자. Small quantum product $$\ast_q$$는 다음을 만족한다.

(1) **Unit**: 모든 $$T_a \in H^\ast(X)$$에 대해 $$1 \ast_q T_a = T_a$$.

(2) **Super-commutativity**: $$T_a \ast_q T_b = (-1)^{\deg T_a \cdot \deg T_b}\, T_b \ast_q T_a$$.

(3) **Associativity**: $$(T_a \ast_q T_b) \ast_q T_c = T_a \ast_q (T_b \ast_q T_c)$$.

따라서 $$(H^\ast(X, \mathbb{C}) \otimes \Lambda, \ast_q)$$는 graded commutative associative unital $$\Lambda$$-algebra이다.

</div>
<details class="proof" markdown="1">
<summary>증명</summary>

(1) [§Gromov-Witten 불변량, ⁋명제 4](/ko/math/symplectic_geometry/gromov_witten#prop4)의 divisor equation의 특수 case로서 $$1 \in H^0(X)$$를 evaluate하는 marked point는 invariant를 변화시키지 않는다. 구체적으로 $$\beta = 0$$인 case는

$$\langle 1, T_a, T_b \rangle_{0, 3, 0}^X = \int_X 1 \cup T_a \cup T_b = \eta_{ab}$$

이고, $$\beta \neq 0$$인 경우 $$\overline{\mathcal{M}}_{0, 3}(X, \beta) \to \overline{\mathcal{M}}_{0, 2}(X, \beta)$$의 forgetful map의 fiber dimension 계산을 거치면 $$\langle 1, T_a, T_b \rangle_{0, 3, \beta}^X = 0$$ ($$\beta \neq 0$$). 따라서

$$1 \ast_q T_a = \sum_\beta \langle 1, T_a, T_c \rangle_{0, 3, \beta}^X\, \eta^{cd} T_d\, q^\beta = \sum_c \eta_{ac}\, T^c = T_a.$$

(2) 3-point GW invariant는 marked point의 순서에 대해 다음과 같이 변환된다. $$\overline{\mathcal{M}}_{0, 3}(X, \beta)$$에서 marked point의 permutation은 super-cohomology의 부호 규칙에 따라 작용하므로

$$\langle T_a, T_b, T_c \rangle = (-1)^{\deg T_a \deg T_b} \langle T_b, T_a, T_c \rangle.$$

이로부터 super-commutativity가 즉시 따른다.

(3) Associativity는 정확히 [§Gromov-Witten 불변량, ⁋명제 6](/ko/math/symplectic_geometry/gromov_witten#prop6)의 WDVV equation의 직접적 귀결이다. WDVV equation을 $$T_a, T_b, T_c, T_d$$의 4-point invariant들의 두 splitting 표현이 같다는 진술로 쓰면

$$\sum_{e, f, \beta_1, \beta_2} \langle T_a, T_b, T_e \rangle_{0, 3, \beta_1}\, \eta^{ef}\, \langle T_f, T_c, T_d \rangle_{0, 3, \beta_2}\, q^{\beta_1 + \beta_2}$$

가 $$(a, b) \vert (c, d)$$ splitting과 $$(a, c) \vert (b, d)$$ splitting에 대해 일치한다. 좌변을 다시 쓰면 정확히 $$\int_X ((T_a \ast_q T_b) \ast_q T_c) \cup T_d$$와 $$\int_X (T_a \ast_q (T_b \ast_q T_c)) \cup T_d$$의 비교가 되며, 따라서 모든 $$T_d$$에 대해 두 값이 같음으로부터 $$(T_a \ast_q T_b) \ast_q T_c = T_a \ast_q (T_b \ast_q T_c)$$이 따른다. 자세한 부호 계산은 [MS Chapter 11]을 보라.

</details>

(1)은 $$1 \in H^0(X)$$이 ring identity로 작동함을 보장하고, (3)은 GW invariant의 깊은 정합성 ([§Gromov-Witten 불변량, ⁋명제 6](/ko/math/symplectic_geometry/gromov_witten#prop6))의 가장 비자명한 결과이다. (3)의 증명에서 사용되는 splitting axiom은 $$\overline{\mathcal{M}}_{0, 4}(X, \beta)$$의 nodal degeneration boundary 위에서의 virtual class의 분해에 의존한다.

<div class="definition" markdown="1">

<ins id="def7">**정의 7**</ins> [정리 6](#thm6)의 graded commutative associative unital $$\Lambda$$-algebra

$$QH^\ast(X) := \left( H^\ast(X, \mathbb{C}) \otimes_\mathbb{C} \Lambda,\ \ast_q \right)$$

를 $$X$$의 *small quantum cohomology ring<sub>작은 양자 코호몰로지 환</sub>*이라 부른다.

</div>

$$q \to 0$$의 극한은 모든 $$\beta \neq 0$$ 항을 제거하는 것이며, 이 극한에서 $$\ast_q$$는 classical cup product로 환원된다. 즉 $$QH^\ast(X) / (q) \cong H^\ast(X, \mathbb{C})$$가 ring 동형이다. 이런 의미에서 quantum cohomology는 classical cohomology의 *Novikov 방향의 deformation*이다.

## 사영공간의 양자 코호몰로지

이제 구체적인 예시로 $$\mathbb{P}^n$$의 quantum cohomology를 계산한다. 우선 $$\mathbb{P}^1$$에서 출발한다.

<div class="example" markdown="1">

<ins id="ex8">**예시 8** ($$X = \mathbb{P}^1$$)</ins> $$H^\ast(\mathbb{P}^1) = \mathbb{C}[H] / (H^2)$$, $$\deg H = 2$$. Effective curve class는 $$d \cdot [\mathbb{P}^1]$$ ($$d \geq 0$$)로 매개되며, $$[\mathbb{P}^1]$$에 대응하는 Novikov variable을 $$q$$로 표기한다. $$c_1(T\mathbb{P}^1) = 2H$$이므로

$$\deg q = 2 \int_{[\mathbb{P}^1]} 2 H = 4.$$

Cohomology basis $$\{ T_0 = 1, T_1 = H \}$$, Poincaré pairing $$\eta_{ab} = \int_{\mathbb{P}^1} T_a T_b$$는 $$\eta_{01} = \eta_{10} = 1$$, 나머지는 $$0$$. 따라서 $$\eta^{01} = \eta^{10} = 1$$.

$$H \ast_q H$$를 계산한다. [정의 4](#def4)에 따라

$$H \ast_q H = \sum_{d \geq 0} \langle H, H, T_c \rangle_{0, 3, d}^{\mathbb{P}^1}\, \eta^{cd}\, T_d\, q^d.$$

$$d = 0$$ 항은 $$\langle H, H, T_c \rangle_{0, 3, 0} = \int_{\mathbb{P}^1} H \cup H \cup T_c = 0$$ (왜냐하면 $$H^2 = 0$$ in $$\mathbb{P}^1$$).

$$d = 1$$ 항은 virtual dimension 공식에 의해 $$\mathrm{vdim}_\mathbb{C}\, \overline{\mathcal{M}}_{0, 3}(\mathbb{P}^1, 1) = 2 + (1 - 3) + 3 = 3$$. 인자들의 degree 합 $$\deg H + \deg H + \deg T_c = 4 + \deg T_c$$가 $$2 \cdot 3 = 6$$이어야 하므로 $$\deg T_c = 2$$, 즉 $$T_c = H$$. 이 GW invariant는 $$\mathbb{P}^1$$ 안의 degree $$1$$ curve (즉 $$\mathbb{P}^1$$ 자체)가 세 일반점을 지나도록 잡는 수로, 단 하나 ($$\mathrm{PGL}_2$$의 작용에 의해 quotient하면 점)이다. 따라서

$$\langle H, H, H \rangle_{0, 3, 1}^{\mathbb{P}^1} = 1.$$

$$d \geq 2$$ 항은 dimension 조건이 맞지 않아 $$0$$. 정리하면

$$H \ast_q H = \langle H, H, H \rangle_{0, 3, 1} \cdot \eta^{H, 1} \cdot 1 \cdot q = 1 \cdot 1 \cdot 1 \cdot q = q \cdot 1.$$

즉 $$QH^\ast(\mathbb{P}^1) \cong \mathbb{C}[H, q] / (H^2 - q)$$.

</div>

이는 classical $$H^\ast(\mathbb{P}^1) = \mathbb{C}[H]/(H^2)$$에서 relation $$H^2 = 0$$이 quantum correction에 의해 $$H^2 = q$$로 deform된 형태이다. 

<div class="example" markdown="1">

<ins id="ex9">**예시 9** ($$X = \mathbb{P}^2$$)</ins> $$H^\ast(\mathbb{P}^2) = \mathbb{C}[H]/(H^3)$$, $$\deg H = 2$$. Effective curve class는 $$d \cdot \ell$$ ($$d \geq 0$$, $$\ell$$은 line class)로 매개되고 $$c_1(T \mathbb{P}^2) = 3H$$이므로 $$\deg q = 2 \int_\ell 3 H = 6$$.

$$H \ast_q H$$의 dimension 조건을 확인하자. 결과는 $$\deg H + \deg H = 4$$ degree의 element이어야 한다. $$q^d$$ 항이 기여하려면 $$T_d$$의 cohomology degree가 $$4 - 6 d$$여야 한다. $$d = 0$$이면 $$\deg T_d = 4$$, 즉 $$T_d = H^2$$. $$d = 1$$이면 $$\deg T_d = -2 < 0$$이므로 기여 없음. 즉

$$H \ast_q H = (\text{classical part}) = H^2$$

으로 quantum correction이 없다.

다음으로 $$H \ast_q H^2$$를 계산하자. 결과는 degree $$6$$이고, $$q^d$$ 항에서 $$T_d$$의 degree는 $$6 - 6 d$$. $$d = 0$$이면 $$\deg T_d = 6$$, 그러나 $$\mathbb{P}^2$$에서 $$H^3 = 0$$이므로 classical 기여는 $$0$$. $$d = 1$$이면 $$\deg T_d = 0$$, 즉 $$T_d = 1$$. 이 항의 계수를 구하기 위한 GW invariant는

$$\langle H, H^2, H^2 \rangle_{0, 3, 1}^{\mathbb{P}^2}$$

이며 (dimension 조건: $$2 + 4 + 4 = 10 = 2 \cdot 5 = 2 \mathrm{vdim}_\mathbb{C}$$, 여기서 $$\mathrm{vdim}_\mathbb{C}\, \overline{\mathcal{M}}_{0, 3}(\mathbb{P}^2, 1) = 3 + (2 - 3) + 3 = 5$$이므로 $$\deg H + \deg H^2 + \deg H^2 = 10$$임을 만족), 기하학적으로 $$\mathbb{P}^2$$ 안의 직선 중 한 일반점과 두 일반점을 지나는 것의 수이다. 두 점을 지나는 직선은 유일하므로

$$\langle H, H^2, H^2 \rangle_{0, 3, 1}^{\mathbb{P}^2} = 1.$$

Poincaré dual basis는 $$T^0 = H^2$$, $$T^{H^2} = 1$$이므로

$$H \ast_q H^2 = 1 \cdot 1 \cdot q = q \cdot 1.$$

$$d \geq 2$$ 항은 dimension 조건에 의해 모두 $$0$$.

따라서 $$\mathbb{P}^2$$에서 $$H \ast_q H \ast_q H = H \ast_q H^2 = q \cdot 1$$이고, ring 구조는

$$QH^\ast(\mathbb{P}^2) \cong \mathbb{C}[H, q] / (H^3 - q).$$

</div>

$$\mathbb{P}^2$$의 경우 $$H \ast_q H = H^2$$는 classical 관계와 같지만 $$H^3$$가 quantum correction을 받는다. 일반적으로 $$\mathbb{P}^n$$에서 정확히 *top degree*에서만 quantum correction이 발생함을 다음 명제가 보여준다.

<div class="proposition" markdown="1">

<ins id="prop10">**명제 10** ($$\mathbb{P}^n$$의 양자 코호몰로지)</ins> $$n \geq 1$$에 대해

$$QH^\ast(\mathbb{P}^n) \cong \mathbb{C}[H, q] / (H^{n+1} - q),\qquad \deg H = 2,\ \deg q = 2(n+1).$$

</div>
<details class="proof" markdown="1">
<summary>증명</summary>

$$c_1(T \mathbb{P}^n) = (n+1) H$$이므로 $$\deg q = 2(n+1)$$이고, [정의 4](#def4)의 합

$$H \ast_q H^k = \sum_{d \geq 0} \sum_c \langle H, H^k, T_c \rangle_{0, 3, d}^{\mathbb{P}^n}\, \eta^{cd}\, T_d\, q^d$$

에서 비자명한 $$q^d$$ 항에 기여하는 $$T_d$$의 cohomology degree는 dimension 조건에 의해

$$\deg T_d = \deg H + \deg H^k - 2 \int_{d \ell} c_1(T \mathbb{P}^n) - 2 (\dim \mathbb{P}^n - 3) - 6 + 2 \dim \mathbb{P}^n = 2(k+1) - 2 d (n+1)$$

이고, $$\deg T_d \in \{0, 2, \ldots, 2 n\}$$이려면 $$0 \leq 2(k+1) - 2 d (n+1) \leq 2 n$$. $$0 \leq k \leq n$$, $$d \geq 0$$에서 $$d = 0$$인 경우 classical 기여, $$d \geq 1$$인 경우 $$k + 1 \geq d (n+1) + 0$$이므로 $$k + 1 \geq n + 1$$ 즉 $$k = n$$이어야 하고 이때 $$d = 1$$, $$\deg T_d = 0$$, $$T_d = 1$$.

$$d = 0$$ 기여는 $$\int_{\mathbb{P}^n} H \cup H^k \cup T_c = \delta_{c, n - k - 1}$$ ($$0 \leq k \leq n - 1$$의 경우)와 $$0$$ ($$k = n$$의 경우). 이를 raise하면 $$H \ast_q H^k = H^{k+1}$$ for $$0 \leq k \leq n - 1$$.

$$k = n$$, $$d = 1$$ 기여는

$$\langle H, H^n, H^n \rangle_{0, 3, 1}^{\mathbb{P}^n} = 1$$

(degree $$1$$ curve, 즉 $$\mathbb{P}^n$$ 안의 직선이 한 hyperplane과의 교점 한 점, 그리고 두 일반점을 지나는 조건의 수). Poincaré dual에 의해 이 항은 $$1 \cdot q$$를 준다. 따라서

$$H \ast_q H^n = q \cdot 1.$$

이로부터 $$H$$에 의한 generator로 $$QH^\ast(\mathbb{P}^n) = \mathbb{C}[H, q]/(H^{n+1} - q)$$가 따른다. 

</details>

위 ring 구조에서 $$q$$를 $$H^{n+1}$$로 *해석*하면 quantum cohomology가 단일 generator $$H$$에 의해 생성된 자유 $$\Lambda$$-algebra의 자연스러운 모습으로 나타난다. 이러한 *cyclic* 구조는 $$\mathbb{P}^n$$의 매우 특수한 성질이며, 일반적인 Fano variety에서는 더 복잡한 관계식이 등장한다.

<div class="remark" markdown="1">

<ins id="rmk11">**참고 11**</ins> $$\mathbb{P}^n$$의 경우 $$X$$가 Fano이므로 ([§Stable maps의 moduli space, ⁋명제 5](/ko/math/symplectic_geometry/stable_maps#prop5)에서 $$c_1(TX)$$가 ample이라는 의미) 각 cohomology degree에서 비자명한 GW invariant를 주는 $$\beta$$가 유한 개이고, 따라서 $$\Lambda$$의 completion 없이 group ring $$\mathbb{C}[q]$$만 사용해도 [정의 4](#def4)의 합이 형식적으로 well-defined이다. 일반적 non-Fano case에서는 무한합을 다루기 위해 [정의 1](#def1)의 completion이 본질적이다.

</div>

## 큰 양자 코호몰로지와 고전 극한

위에서 정의한 small quantum product는 cohomology의 *고정된* 기저 위에서의 곱셈이고, 그 deformation은 오직 Novikov 변수 $$q$$를 통해서만 일어났다. 이제 이를 cohomology class 자체를 추가 deformation 매개변수로 삼아 확장해보자. Cohomology class $$t = \sum_a t^a T_a$$를 GW invariant에 추가로 삽입하되, 우선 그 $$H^2$$ 성분 $$t_2 = \sum_{a:\, \deg T_a = 2} t^a T_a$$만 켜자. Divisor equation ([§Gromov-Witten 불변량, ⁋명제 4](/ko/math/symplectic_geometry/gromov_witten#prop4))에 의하여 $$H^2$$ class 하나를 추가로 삽입하면 GW invariant가 교차수 $$\langle t_2, \beta\rangle = \int_\beta t_2$$만큼 곱해질 뿐이므로 (primary 삽입에는 $$\psi$$-보정이 없다), $$t_2$$를 $$k$$번 삽입하여 합하면

$$\sum_{k \ge 0} \frac{1}{k!}\, \langle T_a, T_b, T_c, \underbrace{t_2, \ldots, t_2}_{k} \rangle_{0, k+3, \beta}^X\, q^\beta = e^{\langle t_2, \beta\rangle}\, q^\beta\, \langle T_a, T_b, T_c \rangle_{0, 3, \beta}^X$$

가 된다. 즉 $$H^2$$ 방향을 켜는 효과는 Novikov 변수를 $$q^\beta \mapsto e^{\langle t_2, \beta\rangle} q^\beta$$로 reparametrize하는 것에 지나지 않으며, $$H^2$$ 방향의 deformation은 이미 small quantum product의 $$q$$ 안에 들어 있다 (이런 의미에서 $$q_a = e^{t^a}$$로 두기도 한다). 따라서 정말로 새로운 deformation은 차수가 $$2$$가 아닌 방향 ($$\deg T_a \neq 2$$)에서 나오는데, 이 방향들은 divisor equation으로 지수함수로 접히지 않아 $$t$$에 대한 멱급수로 남는다. 이렇게 cohomology class 자체를 deformation 매개변수로 삼아 모든 방향을 켠 가장 일반적인 곱셈이 *big quantum product*이다.

<div class="definition" markdown="1">

<ins id="def12">**정의 12**</ins> $$t = \sum_a t^a T_a \in H^\ast(X, \mathbb{C})$$를 형식적 변수, *Gromov-Witten potential*을

$$F(t) := \sum_{n \geq 3,\, \beta} \frac{1}{n!} \langle \underbrace{t, \ldots, t}_{n \text{ copies}} \rangle_{0, n, \beta}^X\, q^\beta$$

으로 정의한다. *Big quantum product* $$\circ_t$$는

$$T_a \circ_t T_b := \sum_{c, d}\, \partial_a \partial_b \partial_c F(t)\, \eta^{cd}\, T_d$$

로 정의되며, [정리 6](#thm6)과 동일한 논증으로 graded commutative associative ring을 이룬다.

</div>

Big quantum product에서 $$t \to 0$$의 극한은 small quantum product의 specialization과 일치한다. 즉 $$T_a \circ_0 T_b = T_a \ast_q T_b$$. 더욱이 small quantum product와 마찬가지로 $$q \to 0$$의 극한은 classical cup product $$T_a \cup T_b$$을 회복한다. 이로써 quantum cohomology는 cohomology class 방향 ($$t$$)과 Novikov variable 방향 ($$q$$)의 두 deformation을 동시에 갖는 구조임이 드러난다.

[정리 6](#thm6)의 ring 공리는 small과 big 양쪽에 모두 적용되며, 두 deformation 방향 모두에서 결합법칙과 super-commutativity가 보존된다. 이러한 다중 deformation 구조의 정합성은 GW invariant의 string, divisor, dilaton axiom ([§Gromov-Witten 불변량](/ko/math/symplectic_geometry/gromov_witten)의 [⁋명제 3](/ko/math/symplectic_geometry/gromov_witten#prop3), [⁋명제 4](/ko/math/symplectic_geometry/gromov_witten#prop4), [⁋명제 5](/ko/math/symplectic_geometry/gromov_witten#prop5))의 통합적 귀결이라 할 수 있다.

---

**참고문헌**

**[MS]** D. McDuff, D. Salamon, *J-holomorphic Curves and Symplectic Topology*, AMS Colloquium Publications **52**, 2nd ed., 2012.

**[KM]** M. Kontsevich, Yu. Manin, *Gromov-Witten classes, quantum cohomology, and enumerative geometry*, Comm. Math. Phys. **164** (1994), 525--562.

**[RT]** Y. Ruan, G. Tian, *A mathematical theory of quantum cohomology*, J. Differential Geom. **42** (1995), 259--367.

**[FP]** W. Fulton, R. Pandharipande, *Notes on stable maps and quantum cohomology*, in *Algebraic Geometry — Santa Cruz 1995*, Proc. Sympos. Pure Math. **62**, AMS, 1997, 45--96.

**[CK]** D. A. Cox, S. Katz, *Mirror Symmetry and Algebraic Geometry*, Mathematical Surveys and Monographs **68**, AMS, 1999.
