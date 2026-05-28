---
title: "Givental J-function과 Mirror Theorem"
description: "기본 정의에서 출발해 양자미분방정식의 기본해로서의 성질을 증명하고, 토릭 파노 다양체의 명시적 hypergeometric 함수와 거울 정리의 관계까지 다룬다."
excerpt: "Quantum differential equation의 fundamental solution과 I=J 정리"

categories: [Math / Mirror Symmetry]
permalink: /ko/math/mirror_symmetry/givental_j_function
sidebar: 
    nav: "mirror_symmetry-ko"

header:
    overlay_image: /assets/images/Math/Mirror_Symmetry/Givental_J_Function.png
    overlay_filter: 0.5

date: 2026-05-28
last_modified_at: 2026-05-28
weight: 6

published: false
---

[§두브로빈 접속, ⁋§D-module](/ko/math/mirror_symmetry/dubrovin_connection#d-module)에서 우리는 quantum cohomology 측의 quantum differential equation (QDE)이 해 공간으로 $$\dim_\mathbb{C} H^\ast(X)$$ 차원의 flat section을 가짐을 보였고, 그 fundamental solution을 명시적으로 적은 것이 *Givental의 $$J$$-function*이라 예고했었다. 한편 [§가우스-마닌 접속, ⁋명제 7](/ko/math/mirror_symmetry/gauss-manin_connection#prop7)에서는 B-side에서 period matrix $$\mathcal{I}^a_p$$가 B-model connection $$\nabla^z_B$$의 fundamental solution matrix를 이루는 것을 살펴보았다. [§두브로빈 접속, ⁋주장 4](/ko/math/mirror_symmetry/dubrovin_connection#conj4)의 mirror theorem은 결국 A-side의 $$J$$-function과 B-side의 period matrix가 동일한 $$D$$-module의 fundamental solution이라는 statement로 구체화될 것이며, 이번 글이 그 짝맞춤의 A-side를 마무리한다.

이번 글에서 우리는 $$J$$-function을 그 형태가 어디서 오는지를 motivation에서부터 짚으면서 정의하고, 그것이 quantum $$D$$-module의 fundamental solution matrix $$S(t, z)$$의 한 열을 이룸을 보인다. 그 후 mirror theorem이 이 $$J$$-function을 [§가우스-마닌 접속, ⁋명제 7](/ko/math/mirror_symmetry/gauss-manin_connection#prop7)의 period matrix와 동일시한다는 사실을 진술한 뒤, toric Fano variety의 경우의 explicit form인 *$$I$$-function*과 *$$I = J$$* 정리, 그리고 $$\mathbb{P}^n$$의 예시로 마무리한다.

## J-function의 정의

$$X$$를 smooth projective variety, $$\{ T_a \}_{a=0,\ldots,s}$$를 $$H^\ast(X, \mathbb{C})$$의 homogeneous basis ($$T_0 = 1$$), $$\{ T^a \}$$를 Poincaré dual basis라 하자. $$\{ t^a \}$$를 $$T_a$$에 대응하는 flat coordinate라 하고, $$t \in H^\ast(X, \mathbb{C})$$의 $$H^2$$ 성분을 $$t_{(2)} := \sum_{a:\,\deg T_a = 2} t^a T_a$$로 표기한다 (Novikov 변수 $$q = e^{t_{(2)}}$$). Dubrovin 글에서는 $$H^2$$ 방향만 본 small QDE를 적었으므로 index의 범위가 $$1, \ldots, r$$이었지만, 여기서는 모든 deformation 방향을 한꺼번에 보는 big QDE까지 다루므로 index가 $$0, 1, \ldots, s$$로 확장된다 (small은 $$t = t_{(2)}$$로 specialize해서 얻는다).

$$J$$-function의 형태가 어디서 오는지를 먼저 들여다보자. [§두브로빈 접속, ⁋§D-module](/ko/math/mirror_symmetry/dubrovin_connection#d-module)의 QDE는 부호 컨벤션 $$\nabla^z = \partial + z^{-1}\mathcal{C}$$를 따라 $$z\,\partial_a s + T_a \star_t s = 0$$의 형태였다. 한편 우리는 J-function이 만족할 ODE를 oscillating integral 측과 부호를 맞춰 쓰기 위해 (그래야 [§가우스-마닌 접속, ⁋명제 7](/ko/math/mirror_symmetry/gauss-manin_connection#prop7)의 $$z\,\partial_{q_i}\mathcal{I} = M_i\mathcal{I}$$ 형태와 직접 맞춘다), 부호를 뒤집어 *dual* Dubrovin connection $$\nabla^{z, \vee} := -\nabla^{-z} = \partial - z^{-1}\mathcal{C}$$의 horizontal section equation

$$z\, \partial_a s = T_a \star_t s\qquad (a = 0, \ldots, s)\tag{$\ast$}$$

으로 쓴다. 어느 쪽이든 $$z \mapsto -z$$ 치환으로 서로 옮겨가므로 본질적으로 같은 D-module이다. 

이제 ($$\ast$$)의 해를 만들기 위해, 우변에 quantum product이 있어 모든 $$\beta \in \mathrm{NE}(X)$$의 GW 보정을 끌어모은다는 사실을 받아들이고, $$z\rightarrow \infty$$의 ansatz로 풀어보자. $$z\to \infty$$일 때 $$z\cdot \partial_a s\rightarrow 0$$이려면 leading term $$s_0$$이 $$t$$에 무관해야 하므로 자연스러운 normalization은 $$s_0 = 1\in H^0(X)$$이다. 그 다음 차수에서 $$s = 1 + s_1/z + s_2/z^2 + \cdots$$를 ($$\ast$$)에 대입해 $$z^0$$ 계수를 보면 $$\partial_a s_1 = T_a$$가 되므로 $$s_1$$의 linear part는 $$t$$ 자체이고 그 보정은 모든 *primary* GW invariant들의 생성함수가 된다. 더 높은 $$z^{-k}$$ 차수에서는 quantum product의 $$t$$-의존성 자체에서 오는 정보, 즉 *gravitational descendant*가 차례로 끌려나온다. $$J$$-function은 결국 이렇게 강제되는 fundamental solution을 한 줄로 명시적으로 적은 것이다.

### Descendant Gromov-Witten invariant

위 ansatz에서 등장하는 *descendant* invariant를 짧게 정리해 두자. Genus-$$0$$, $$(n+1)$$-marked, class $$\beta$$의 stable map의 moduli space 

$$\overline{\mathcal{M}}_{0, n+1}(X, \beta)$$

위에는 각 marked point $$i$$에서의 evaluation map $$\mathrm{ev}_i: \overline{\mathcal{M}}_{0, n+1}(X, \beta) \to X$$와 universal cotangent line bundle $$\mathbb{L}_i$$가 정의된다. 후자의 first Chern class

$$\psi_i := c_1(\mathbb{L}_i) \in H^2(\overline{\mathcal{M}}_{0, n+1}(X, \beta))$$

를 *psi-class*라 부른다. 임의의 cohomology class $$\gamma_i \in H^\ast(X)$$와 $$k_i \geq 0$$에 대해 *descendant GW invariant*는

$$\left\langle \tau_{k_1}(\gamma_1), \ldots, \tau_{k_{n+1}}(\gamma_{n+1})\right\rangle_{0, n+1, \beta} := \int_{[\overline{\mathcal{M}}_{0, n+1}(X, \beta)]^{\mathrm{vir}}} \prod_{i=1}^{n+1} \psi_i^{k_i} \cup \mathrm{ev}_i^\ast \gamma_i$$

로 정의된다. $$k_i = 0$$인 경우 *primary* invariant, 적어도 하나의 $$k_i \geq 1$$이면 *gravitational descendant*이다. 직관적으로 $$\psi_i$$는 marked point에서 곡선의 "접선 자유도"를 측정하며, 그 거듭제곱은 marked point에 jet 조건을 부여하는 효과를 갖는다.

$$J$$-function의 정의에 등장하는 기호 $$\langle \cdots, \frac{1}{z - \psi}\rangle$$는 마지막 marked point에 모든 차수의 $$\psi$$-거듭제곱을 한꺼번에 끼우는 generating function 표기이다.

$$\left\langle \gamma_1, \ldots, \gamma_n, \frac{\gamma_{n+1}}{z - \psi}\right\rangle_{0, n+1, \beta} = \sum_{k \geq 0} z^{-k-1} \left\langle \gamma_1, \ldots, \gamma_n, \tau_k(\gamma_{n+1})\right\rangle_{0, n+1, \beta}$$

### 정의

<div class="definition" markdown="1">

<ins id="def1">**정의 1**</ins> $$X$$의 *Givental $$J$$-function* $$J_X: H^\ast(X) \times \mathbb{C}^\ast \to H^\ast(X)$$는 다음으로 정의된다.

$$J_X(t, z) := e^{t_{(2)}/z}\left( 1 + \sum_{\substack{\beta \in \mathrm{NE}(X) \\ (\beta, n) \neq (0, 0)}} \sum_{a=0}^s \frac{q^\beta}{n!}\, \left\langle T_a, t, \ldots, t, \frac{1}{z - \psi} \right\rangle_{0, n+1, \beta} T^a \right)$$

여기서 $$\frac{1}{z-\psi}$$는 마지막 marked point에 $$\sum_{k \geq 0} z^{-k-1} \psi^k$$ 형태로 끼워 모든 차수의 descendant를 모은다는 의미이다 (위 ⁋Descendant Gromov-Witten invariant 절 참고). 지수 인자 $$e^{t_{(2)}/z}$$는 $$H^2$$ 방향의 divisor equation을 흡수하는 normalization이다.

$$t = t_{(2)}$$만 켠 *small* $$J$$-function은

$$J_X(q, z) = 1 + \sum_{\beta \neq 0} \sum_{a} q^\beta\, \left\langle \frac{T_a}{z(z - \psi)} \right\rangle_{0, 1, \beta} T^a$$

의 형태를 가진다.

</div>

Small form의 환원은 다음과 같다. $$t = t_{(2)} \in H^2(X)$$로 specialize하면 $$\langle T_a, t, \ldots, t, \tfrac{1}{z-\psi}\rangle_{0, n+1, \beta}$$의 $$t$$ 자리에 들어가는 class가 모두 $$H^2$$ class이고, [§양자 코호몰로지](/ko/math/symplectic_geometry/quantum_cohomology)에서 본 *divisor equation* $$\langle t, \gamma_1, \ldots, \gamma_n\rangle_{0, n+1, \beta} = (t \cdot \beta)\langle \gamma_1, \ldots, \gamma_n\rangle_{0, n, \beta}$$ ($$t \in H^2$$) 를 $$n$$번 적용하면 $$t$$ 삽입들이 $$(t\cdot \beta)^n/n!$$로 빠져나오고, 이것이 $$\sum_n (t\cdot \beta)^n/n! = e^{t\cdot \beta} = q^\beta$$로 정확히 합산되어 앞의 $$e^{t_{(2)}/z}$$와 결합한다. 결과적으로 marked point 수가 $$1$$로 줄어든 형태가 위의 small J이며, 본 글에서는 주로 이 형태를 사용한다.

위 정의의 각 성분이 무엇을 담고 있는지 항별로 정리하면 다음과 같다.

- $$z \to \infty$$ leading term $$1$$은 *classical* limit (모든 $$\beta \neq 0$$ 보정을 끄고, $$\psi$$ 거듭제곱을 끄면 남는 부분).
- $$z^{-1}$$의 계수는 *primary* GW invariant $$\langle T_a\rangle_{0,1,\beta}$$ 즉 $$\psi$$ 없이 단 한 점에서 $$T_a$$의 pull-back만 적분한 enumerative 수.
- $$z^{-2}$$의 계수는 *gravitational descendant* $$\langle \tau_1(T_a)\rangle_{0,1,\beta}$$ 즉 $$\psi^1$$이 한 번 끼인 적분.
- 일반적으로 $$z^{-k-1}$$의 계수는 $$\tau_k(T_a)$$의 $$\beta$$별 합.

즉 $$J$$-function은 모든 차수의 descendant invariant를 하나의 $$z$$-급수로 묶어 둔 *master* 생성함수이며, 그 묶음 자체가 ($$\ast$$)의 자연스러운 fundamental solution을 이룬다는 것이 다음 절의 내용이다.

## QDE의 fundamental solution

위 ⁋동기에서 본 ansatz는 ($$\ast$$)의 해의 형태가 "leading 1 + GW descendant 보정"의 꼴로 강제됨을 시사했고, [정의 1](#def1)의 $$J$$-function은 그 정확한 표현이다. 이를 명제로 정리하자. 

[§가우스-마닌 접속, ⁋명제 7](/ko/math/mirror_symmetry/gauss-manin_connection#prop7)에서 B-side의 fundamental solution matrix는 cohomology basis $$\{e_a\}$$와 thimble basis $$\{[\Gamma_p]\}$$ 사이의 period $$\mathcal{I}^a_p$$로 적힌 행렬이었다. A-side에서 그에 정확히 대응하는 행렬은 *Givental의 $$S$$-matrix*로 알려진 endomorphism-값 함수이며, $$J$$-function은 그 한 column이다.

<div class="proposition" markdown="1">

<ins id="prop2">**명제 2** ($$J$$-function as fundamental solution column)</ins> Endomorphism $$S(t, z) \in \End(H^\ast(X))$$를 다음의 matrix element

$$\eta\bigl(S(t,z)\,T_a,\, T_b\bigr) := \eta(T_a, T_b) + \sum_{\substack{\beta \in \mathrm{NE}(X), n \geq 0 \\ (\beta, n) \neq (0, 0)}} \frac{1}{n!} \left\langle T_a, t, \ldots, t, \frac{T_b}{z - \psi} \right\rangle_{0, n+2, \beta}$$

으로 정의하자 ($$\eta$$는 Poincaré pairing). 그러면

1. *(Flat section property)* $$S(t, z)$$의 각 column $$S(t, z) T_b$$는 dual Dubrovin connection $$\nabla^{z, \vee}$$의 horizontal section이다. 즉

$$z\, \partial_a \bigl(S(t,z)T_b\bigr) = T_a \star_t \bigl(S(t,z)T_b\bigr).$$

2. *($$J$$ = $$T_0$$ column)* $$J_X(t, z) = e^{t_{(2)}/z}\, S(t, z)\, T_0$$가 성립한다. 특히 $$J$$ 자체도 ($$\ast$$)의 horizontal section이고,

$$z\, \partial_a J_X = T_a \star_t J_X \qquad (a = 0, 1, \ldots, s).$$

</div>

<details class="proof" markdown="1">
<summary>증명 개요</summary>

핵심은 두 가지 GW 공리, 즉 *string equation* (marked point에 $$T_0 = 1$$을 끼울 때의 reduction)과 *divisor equation* ($$H^2$$ class를 끼울 때의 $$T_a \cdot \beta$$ 인자), 그리고 *topological recursion relation* ($$\psi$$-class를 boundary divisor로 분해하는 $$\overline{M}_{0, n+1}$$ 위의 관계식)을 정합적으로 활용하는 것이다. 

(2)는 $$T_b = T_0 = 1$$을 대입하면 string equation을 통해 $$1$$ 삽입이 다른 marked point의 $$\psi$$-차수를 한 단계 낮추는 형태로 reduce되고, 그 후 적절히 항을 재배열하면 [정의 1](#def1)의 big J가 그대로 복원됨을 확인하면 된다. (1)의 flat section property는 $$\partial_a$$ 미분이 marked point의 추가와 등가임을 사용하면 $$z\partial_a$$의 작용이 marked point에 $$T_a$$를 추가로 끼우는 효과로 정리되고, 그 후 한 marked point를 $$\frac{T_b}{z-\psi}$$와 분리하는 *topological recursion relation* ($$\overline{M}_{0, n+1}$$의 $$\psi$$-class를 boundary divisor의 합으로 분해하는 관계식)을 통해 우변의 $$T_a \star_t$$ 작용과 같아짐을 보인다. 자세한 계산은 [CK, Theorem 10.3.1] 또는 [MS, Chapter 28-29] 참조.

</details>

[명제 2](#prop2)는 $$J$$-function이 단순한 enumerative 데이터의 묶음을 넘어, A-model 측 fundamental solution matrix $$S$$의 *한 열 (구체적으로 normalization element $$T_0 = 1$$에 해당하는 열)*을 이룸을 보여준다. 다른 열들은 $$J$$를 미분하여 복원할 수 있고 ($$z\partial_a J = T_a\star_t J$$의 우변이 곧 $$T_a$$-column에 해당), 결국 $$J$$ 한 줄이 전체 $$S$$ 행렬을, 따라서 quantum $$D$$-module의 모든 데이터를 인코딩한다. 

이 점에서 $$S$$ (혹은 그 표현인 $$J$$)는 B-side의 period matrix $$\mathcal{I}^a_p$$ ([§가우스-마닌 접속, ⁋명제 7](/ko/math/mirror_symmetry/gauss-manin_connection#prop7))와 정확히 짝을 이룬다. 각 column이 한 flat section을 나타낸다는 의미에서 두 행렬은 같은 역할을 하는 객체이며, 이들이 서로 일치한다는 것이 다음 절의 mirror theorem의 기하학적 내용이다.

## Mirror theorem (B-model의 oscillating integral과의 대응)

이제 두 fundamental solution 행렬을 짝지을 수 있다. [§두브로빈 접속, ⁋주장 4](/ko/math/mirror_symmetry/dubrovin_connection#conj4)의 $$D$$-module isomorphism $$\Phi: H_A \xrightarrow{\sim} H_B$$는 A-side의 $$S$$-matrix ([명제 2](#prop2))를 B-side의 period matrix $$\mathcal{I}$$ ([§가우스-마닌 접속, ⁋명제 7](/ko/math/mirror_symmetry/gauss-manin_connection#prop7))와 동일시한다. $$J$$-function이 $$S$$의 $$T_0$$-열이었음을 떠올리면, 그 mirror image는 $$\mathcal{I}$$의 한 특별한 열에 해당한다.

<div class="proposition" markdown="1">

<ins id="prop3">**명제 3** (Mirror theorem, $$J$$-function form)</ins> Mirror pair $$(X, \check{X})$$에 대해, $$X$$의 $$J$$-function은 $$T_0 = 1$$ normalization에 대응하는 특정 Lefschetz thimble $$\Gamma_0$$ (large radius limit 근방에서 결정되는 *distinguished* thimble)에 대한 oscillating integral의 cohomology basis $$\{T^a\}$$ 성분들로 적힌다. 즉

$$J_X(q, z) \;=\; \sum_a J^a(q, z)\, T^a,\qquad J^a(q, z) \;=\; \frac{1}{(2\pi i z)^N}\int_{\Gamma_0} T_a\, e^{W_q/z}\,\omega$$

가 (normalization을 흡수하고 나면) 성립한다. 여기서 $$\Phi$$ 아래 $$T_a$$는 [§가우스-마닌 접속](/ko/math/mirror_symmetry/gauss-manin_connection#prop7)의 basis $$\{e_a\}$$로 매핑된 것이다. 특히 $$z \to 0$$ stationary phase asymptotic ([§가우스-마닌 접속, ⁋명제 3](/ko/math/mirror_symmetry/gauss-manin_connection#prop3))은 $$W_q$$의 critical point들에 의한 합으로 풀어지며, 그 leading order의 critical value들 $$\{W_q(p)\}$$가 quantum cohomology의 canonical coordinate들을 복원한다 ([§거울대칭 개요](/ko/math/mirror_symmetry/overview)의 ring isomorphism $$\Jac(W_q) \cong QH^\ast(X_\Sigma)$$의 직접적 격상).

</div>

<details class="proof" markdown="1">
<summary>증명 개요</summary>

이 동형은 mirror pair마다 별도로 증명되어야 하는 깊은 정리이다. 핵심은 $$J$$-function이 만족하는 QDE ([명제 2](#prop2))와 period matrix가 만족하는 Picard-Fuchs 시스템 ([§가우스-마닌 접속, ⁋명제 7](/ko/math/mirror_symmetry/gauss-manin_connection#prop7))이 동일한 $$D$$-module을 정의함을 보이고, 양 변의 $$z \to \infty$$ 초기조건이 distinguished thimble $$\Gamma_0$$에 대한 적분을 통해 일치함을 확인하는 것이다. Calabi-Yau hypersurface in toric variety의 경우 Givental과 Lian-Liu-Yau가 이를 증명하였으며, toric Fano의 명시적 형태는 [명제 5](#prop5)에서 다룬다.

</details>

[명제 3](#prop3)은 mirror symmetry의 *가장 강한 표현*으로, A-model에서 정의되는 descendant GW invariant 전체가 B-model의 period 적분으로 복원된다는 주장이다. [§거울대칭 개요](/ko/math/mirror_symmetry/overview)에서 다룬 *ring*-level mirror symmetry $$QH^\ast(X) \cong \Jac(W_q)$$는 이 statement의 $$z \to 0$$ leading order에 해당하고, 명제 3은 이를 $$z \in \mathbb{C}^\ast$$ 전체로 확장한 statement이다. Calabi-Yau hypersurface in toric variety의 경우 Givental·Lian-Liu-Yau가 이를 증명하였고, toric Fano variety의 경우 다음 절의 *$$I = J$$* 정리가 그 explicit 형태를 제공한다.

## Toric Fano variety: $$I$$-function과 $$I = J$$ 정리

Toric Fano variety의 경우 B-model 측의 oscillating integral은 명시적인 *hypergeometric* 형태로 계산된다. 이를 통해 정의되는 객체가 *$$I$$-function*이며, $$J$$-function의 toric mirror counterpart로 작동한다.

<div class="definition" markdown="1">

<ins id="def4">**정의 4** (Givental의 $$I$$-function)</ins> $$X$$를 smooth projective toric Fano variety, $$D_1, \ldots, D_N$$을 toric divisor, $$\beta \in H_2(X, \mathbb{Z})$$를 effective curve class라 하자. $$X$$의 *$$I$$-function*은 다음으로 정의된다.

$$I_X(q, z) := e^{t_{(2)}/z} \sum_{\beta \in \mathrm{NE}(X)} q^\beta \prod_{i=1}^N \frac{\prod_{k=-\infty}^{0} (D_i + kz)}{\prod_{k=-\infty}^{D_i \cdot \beta}(D_i + kz)}$$

여기서 형식상 등장하는 $$-\infty$$로의 무한곱은 분자와 분모에서 정확히 상쇄되어 실제로는 $$D_i \cdot \beta$$의 부호에 따라 유한곱 (혹은 그 역수)으로 환원된다. $$I_X(q, z)$$는 $$X$$의 Hori-Vafa mirror $$\check{X}$$ 위의 oscillating integral을 charge (GKZ) 데이터로 직접 전개해 얻어진다.

</div>

[정의 4](#def4)의 식은 외관상 복잡하지만, 정해진 charge 데이터로부터 *손으로* 적을 수 있다는 점이 핵심이다 (다음 절 예시 참조). 이제 $$I$$-function과 $$J$$-function의 관계를 진술한다.

<div class="proposition" markdown="1">

<ins id="prop5">**명제 5** (Givental의 mirror theorem)</ins> $$X$$가 smooth projective toric Fano variety일 때, $$X$$의 $$I$$-function과 $$J$$-function은 다음 관계를 만족한다.

$$J_X(\tau(q), z) = I_X(q, z)$$

여기서 $$\tau(q)$$는 $$I$$-function의 asymptotic expansion

$$I_X(q, z) = 1 + \tau(q)/z + O(z^{-2})$$

으로부터 정의되는 **mirror map**이다. $$X$$가 **semi-positive** (즉, $$-K_X \cdot \beta \geq 0$$이 모든 effective curve class $$\beta$$에 대해 성립)이면 $$I_X$$와 $$J_X$$는 이 (일반적으로 비자명한) mirror map을 통한 좌표변환으로 일치한다. 나아가 $$I_X = 1 + O(z^{-1})$$, 즉 $$z^0$$ 차수에 leading $$1$$ 외의 보정항이 없으면 mirror map은 trivial하여 $$J_X(q, z) = I_X(q, z)$$가 성립하는데, 이는 특히 Fano index가 $$2$$ 이상인 경우에 해당한다.

</div>

<details class="proof" markdown="1">
<summary>증명 개요</summary>

$$I$$-function의 hypergeometric 곱은 $$X$$의 Hori-Vafa mirror $$\check{X}$$ 위의 oscillating integral을 charge (GKZ) 데이터로 전개하여 직접 얻어지며, 이것이 [명제 2](#prop2)의 QDE와 동일한 미분방정식을 만족함을 보이는 것이 핵심이다. 두 해가 모두 $$z \to \infty$$에서 $$1 + O(z^{-1})$$의 점근형을 가지므로, asymptotic expansion의 $$z^{-1}$$ 계수로 정의되는 mirror map $$\tau(q)$$를 통한 좌표변환 후 일치한다. 자세한 증명은 [CK, §11], [MS, Chapter 29] 참조.

</details>

[명제 5](#prop5)는 [명제 3](#prop3)의 명시적 형태로, mirror symmetry를 *계산 가능한* tool로 변환한다. $$J$$-function의 추상적인 Gromov-Witten 정의로부터는 직접 계산이 어렵지만, $$I$$-function의 hypergeometric 형태는 charge matrix로부터 손으로 적을 수 있기 때문이다.

## 예시: $$\mathbb{P}^n$$

<div class="example" markdown="1">

<ins id="ex6">**예시 6** ($$X = \mathbb{P}^n$$)</ins> $$\mathbb{P}^n$$의 fan은 $$v_0 = -(1,\ldots,1)$$, $$v_i = e_i$$를 갖고, hyperplane class $$H$$가 $$H^2$$을 생성한다 ($$\Pic(\mathbb{P}^n) = \mathbb{Z} H$$). Effective curve class는 $$d H^\vee$$ ($$d \geq 0$$)로 매개되며, $$D_i \cdot dH^\vee = d$$이므로 $$I$$-function 공식은

$$I_{\mathbb{P}^n}(q, z) = e^{H \ln q /z} \sum_{d \geq 0} \frac{q^d}{\prod_{j=1}^d (H + jz)^{n+1}}$$

이 된다. $$H^{n+1} = 0$$이므로 분모의 $$(H + jz)^{-(n+1)}$$를 $$z^{-1}$$의 멱으로 전개하면 첫 몇 차수가 명시적으로 풀린다.

$$I_{\mathbb{P}^n}(q, z) = 1 + \frac{H \ln q}{z} + \frac{(H \ln q)^2}{2 z^2} + \cdots + q\, \frac{1}{(H+z)^{n+1}} + \cdots$$

$$\mathbb{P}^n$$은 $$-K_{\mathbb{P}^n} = (n+1) H$$이므로 Fano index가 $$n+1 \geq 2$$이고, 따라서 [명제 5](#prop5)에 의해 $$I_{\mathbb{P}^n} = 1 + O(z^{-1})$$이 되어 mirror map은 trivial하고

$$J_{\mathbb{P}^n}(q, z) = I_{\mathbb{P}^n}(q, z)$$

이다.

B-side와의 직접 짝맞춤은 [§가우스-마닌 접속, ⁋예시 8](/ko/math/mirror_symmetry/gauss-manin_connection#ex8)에서 이미 절반이 끝나있다. 그 예시에서 우리는 period matrix의 첫 column $$\mathcal{I}^0_p$$가 만족하는 ODE

$$(z\partial_q)(qz\partial_q)^n\,\mathcal{I}^0_p \;=\; \mathcal{I}^0_p \tag{$\dagger$}$$

를 도출했다. [명제 3](#prop3)의 mirror theorem이 옳다면 $$I_{\mathbb{P}^n}$$의 $$H^0$$-coefficient

$$\Phi_0(q, z) \;:=\; \sum_{d \geq 0} \frac{q^d}{(d!)^{n+1}\,z^{(n+1)d}}$$

(위의 hypergeometric 곱 식에서 $$H = 0$$으로 specialize한 것) 또한 ($$\dagger$$)를 만족해야 한다. 직접 계산하면 $$qz\partial_q$$의 작용은 항별로 $$d$$를 끌어내고 $$z^{-1}$$ 인자를 붙이므로

$$(qz\partial_q)^n\Phi_0 = \sum_{d\geq 0}\frac{d^n\, q^d}{(d!)^{n+1}\,z^{(n+1)d - n}},$$

이고 다시 $$z\partial_q$$를 작용시키면 $$d$$를 한번 더 끌어내고 $$d$$를 $$d - 1$$로 shift시켜

$$(z\partial_q)(qz\partial_q)^n\Phi_0 = \sum_{d \geq 1}\frac{d^{n+1}\,q^{d-1}}{(d!)^{n+1}\,z^{(n+1)d - n - 1}} = \sum_{d' \geq 0}\frac{(d'+1)^{n+1}\,q^{d'}}{((d'+1)!)^{n+1}\,z^{(n+1)d'}} = \Phi_0$$

가 정확히 성립한다. 따라서 $$I_{\mathbb{P}^n}$$이 만족하는 hypergeometric ODE와 B-side의 Gauss-Manin ODE가 동일하며, 두 fundamental solution이 $$z \to \infty$$에서 같은 normalization $$1 + O(z^{-1})$$을 가지므로 $$J_{\mathbb{P}^n} = I_{\mathbb{P}^n}$$이 곧 [§가우스-마닌 접속, ⁋예시 8](/ko/math/mirror_symmetry/gauss-manin_connection#ex8)의 oscillating integral과 일치한다는 의미가 된다. 

[명제 3](#prop3)의 stationary phase 측면 또한 [§가우스-마닌 접속, ⁋예시 8](/ko/math/mirror_symmetry/gauss-manin_connection#ex8)에서 이미 계산해 두었다. 즉 $$W_q$$의 $$n+1$$개 critical point $$x_\zeta = \zeta\, q^{1/(n+1)}$$에서의 critical value $$(n+1)\zeta q^{1/(n+1)}$$과 Hessian determinant $$(n+1)(\zeta q^{1/(n+1)})^{-n}$$이 [§가우스-마닌 접속, ⁋명제 3](/ko/math/mirror_symmetry/gauss-manin_connection#prop3)의 stationary phase formula에 대입되어 oscillating integral의 $$z\to 0^+$$ asymptotic을 주며, 이것이 $$I_{\mathbb{P}^n}(q, z)$$의 $$z \to 0$$ asymptotic과도 일치한다 ([CK, §11.2]).

</div>

이 예시는 mirror symmetry가 추상적인 동형이 아니라 *구체적인 hypergeometric 함수의 일치*로 실현됨을 보여준다. 일반적인 toric Fano variety의 경우 비슷한 명시적 계산이 charge matrix로부터 진행되며, 그 모든 사례에서 [명제 5](#prop5)의 $$I = J$$ 정리가 mirror symmetry의 실용적인 검증을 제공한다.

---

**참고문헌**

**[CK]** D. A. Cox, S. Katz, *Mirror Symmetry and Algebraic Geometry*, Mathematical Surveys and Monographs **68**, AMS, 1999.

**[MS]** K. Hori, S. Katz, A. Klemm, R. Pandharipande, R. Thomas, C. Vafa, R. Vakil, E. Zaslow, *Mirror Symmetry*, Clay Mathematics Monographs **1**, AMS, 2003.
