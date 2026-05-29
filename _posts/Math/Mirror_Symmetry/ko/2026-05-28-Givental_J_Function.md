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

[§두브로빈 접속, §§D-module](/ko/math/mirror_symmetry/dubrovin_connection#d-module)에서 우리는 quantum cohomology 측의 quantum differential equation (QDE)이 해 공간으로 $$\dim_\mathbb{C} H^\ast(X)$$ 차원의 flat section을 가짐을 보였고, 그 fundamental solution을 명시적으로 적은 것이 *Givental의 $$J$$-function*이라 예고했었다. 한편 [§가우스-마닌 접속, ⁋명제 7](/ko/math/mirror_symmetry/gauss-manin_connection#prop7)에서는 B-side에서 period matrix $$\mathcal{I}^a_p$$가 B-model connection $$\nabla^z_B$$의 fundamental solution matrix를 이루는 것을 살펴보았다. 우리가 예고했던 mirror theorem은 결국 A-side의 $$J$$-function과 B-side의 period matrix가 동일한 $$D$$-module의 fundamental solution이라는 statement로 구체화될 것이며, 이번 글이 그 주장에서 비어있는 A-side 자리를 채울 것이다.

## J-function의 정의

Smooth projective variety $$X$$, $$H^\ast(X, \mathbb{C})$$의 homogeneous basis $$\{ T_a \}_{a=0,\ldots,s}$$ ($$T_0 = 1$$), 그리고 이들이 주는 Poincaré dual basis $$\{ T^a \}$$를 생각하자. 이 중 $$H^2$$ 성분을 차지하는 부분을 (notation 단순화를 위해) $$\{ T_a \}_{a=1,\ldots,r}$$로 잡으면, [§두브로빈 접속, §§D-module](/ko/math/mirror_symmetry/dubrovin_connection#d-module)에서 도입한 flat coordinate $$t^a$$와 Novikov variable $$q_a := e^{t^a}$$ ($$a = 1, \ldots, r$$)가 정의된다. 편의상 

$$t_{(2)} := \sum_{b=1}^r t^b T_b$$

라 두면 $$q^\beta = e^{t_{(2)} \cdot \beta}$$이다. 한편 Dubrovin connection은 다음의 식

$$\nabla^z = \partial + z^{-1}\mathcal{C}$$

으로 정의되었는데, 이번 글에서 우리는 oscillating integral 쪽과 부호를 맞추기 위해 그 *dual Dubrovin connection*

$$\nabla^{z, \vee} := -\nabla^{-z} = \partial - z^{-1}\mathcal{C}$$

과 이 connection의 horizontal section equation

$$z\, q_a\partial_{q_a} s = T_a \qtimes s \qquad (a = 1, \ldots, r)\tag{$\ast$}$$

을 고려하기로 한다. 

이 방정식의 해를 구하기 위해 우선 $$z\rightarrow \infty$$인 상황을 보자. 그럼 $$z\rightarrow\infty$$일 때 $$z^{-1}\mathcal{C}$$ 항이 사라지면서 standard differential $$\partial$$로 degenerate하며, 따라서 ($$\ast$$)의 leading-order horizontal section은 $$\partial$$의 horizontal section, 즉 $$q$$에 무관한 constant section이 된다. 더 일반적으로, $$z\rightarrow \infty$$인 limit에서 사라지는 solution은

$$s=s_0+\frac{s_1}{z}+\frac{s_2}{z^2}+\cdots$$

의 꼴일 것이며, 위의 계산에서 $$0$$차항 $$s_0$$은 constant section으로 두면 된다는 것을 보았으므로 다음 꼴

$$s=1+\frac{s_1}{z}+\frac{s_2}{z^2}+\cdots$$

을 ($$\ast$$)에 직접 대입하면 recursive하게 $$s_i$$들을 구할 수 있다. 구체적으로, ($$\ast$$)의 양변을 $$z$$의 거듭제곱별로 정리하면, 좌변은 $$s_0$$이 상수이므로

$$z \cdot \sum_k z^{-k} q_a\partial_{q_a} s_k = \sum_k z^{-k} q_a\partial_{q_a} s_{k+1}$$

이고, 우변은 $$\sum_k z^{-k}\, T_a\qtimes s_k$$이므로 각각의 $$z^{-k}$$ 계수를 비교하여 일반적인 recursion

$$q_a\partial_{q_a} s_{k+1} = T_a \qtimes s_k \qquad (a = 1, \ldots, r,\; k \geq 0)$$

을 얻는다. 

Recursion의 첫 단계에 해당하는 $$k = 0$$에서는 $$T_a \qtimes 1 = T_a$$이므로, 별다른 quantum correction 없이 $$q_a\partial_{q_a} s_1 = T_a$$이 성립한다. 이제 양변을 $$q_a$$에 대해 적분하면

$$s_1=t_{(2)} + C_1,\qquad C_1\in H^\ast(X)$$

가 된다. 흥미로운 부분은 quantum correction이 처음 등장하는 $$k=1$$인데, recursion formula

$$q_a\partial_{q_a} s_2 = T_a \qtimes t_{(2)}=T_a\qtimes \left(\sum_{b=1}^r t^b T_b\right)$$

를 생각하면 이제 우변은 classical cup product $$T_a\smile t_{(2)}$$에 추가적으로 quantum correction

$$\sum_{\beta \neq 0} q^\beta \sum_c \left(\sum_{b=1}^r t^b\, \langle T_a, T_b, T^c\rangle_{0, 3, \beta}\right) T_c$$

부분을 갖는다. 한편 $$T_b \in H^2$$이므로 [\[사교기하학\] §Gromov-Witten 불변량, ⁋명제 4](/ko/math/symplectic_geometry/gromov_witten#prop4)의 결과

$$\langle T_a, T_b, T^c\rangle_{0, 3, \beta} = (T_b \cdot \beta)\langle T_a, T^c\rangle_{0, 2, \beta}$$

을 적용하면 다음의 식

$$T_a \qtimes t_{(2)} = T_a \smile t_{(2)} + \sum_{\beta \neq 0} q^\beta\, (t_{(2)} \cdot \beta) \sum_c \langle T_a, T^c\rangle_{0, 2, \beta}\, T_c$$

을 얻는다. 이제 이를 $$q_a$$에 대해 적분하자. Classical 부분 $$T_a \smile t_{(2)}$$의 antiderivative는 $$(t_{(2)})^2/2$$인데, 이는 $$q_a\partial_{q_a} = \partial_{t^a}$$임을 이용하여

$$\partial_{t^a}\bigl((t_{(2)})^2/2\bigr) = \partial_{t^a}\!\left(\frac{1}{2}\sum_{b, c} t^b t^c\, T_b \smile T_c\right) = \sum_c t^c\, T_a \smile T_c = T_a \smile t_{(2)}$$

로 직접 확인된다. Quantum 부분의 antiderivative는 $$q^\beta = e^{t_{(2)}\cdot \beta}$$로부터 오는 관계 $$q_a\partial_{q_a} q^\beta = (T_a \cdot \beta) q^\beta$$을 이용해 $$\beta$$별로 풀어내면, 각 $$\beta$$에 대해 $$q^\beta$$ 인자와 *primary* GW invariant ($$\psi$$-class 삽입 없는 descendant invariant $$\langle T_a, T^c\rangle_{0, 2, \beta}$$로 결정되는 $$H^\ast(X)$$-valued correction으로 정리되며, 따라서 $$s_2$$는 classical $$(t_{(2)})^2/2$$와 이 quantum correction의 합이 된다. 더 높은 $$z^{-k}$$ ($$k \geq 2$$) 차수에서는 같은 recursion을 따라 $$\tau_{k-1}(T_a)$$ 형태의 *gravitational descendant*가 차례로 누적되며, $$J$$-function은 결국 이렇게 강제되는 fundamental solution을 한 줄로 명시적으로 적은 것이다.

본격적인 정의를 시작하기 전에, 위의 계산에서 등장하는 *descendant* invariant ([\[사교기하학\] §Gromov-Witten 불변량, ⁋정의 2](/ko/math/symplectic_geometry/gromov_witten#def2))를 본 글의 표기에 맞춰 짧게 정리해 두자. Genus $$0$$, $$(n+1)$$-marked, class $$\beta$$의 stable map의 moduli space 

$$\overline{\mathcal{M}}_{0, n+1}(X, \beta)$$

위에는 각 marked point $$i$$에서의 evaluation map $$\ev_i: \overline{\mathcal{M}}_{0, n+1}(X, \beta) \to X$$와 universal cotangent line bundle $$\mathbb{L}_i$$가 정의된다. 직관적으로 $$\mathbb{L}_i$$는 $$i$$번째 marked point들에서의 cotangent space를 moduli space 위에서 붙여준 것이며, 이 때 이 universal cotangent line bundle의 first Chern class

$$\psi_i := c_1(\mathbb{L}_i) \in H^2(\overline{\mathcal{M}}_{0, n+1}(X, \beta))$$

를 *$$\psi$$-class*라 부른다. 임의의 cohomology class $$\gamma_i \in H^\ast(X)$$와 $$k_i \geq 0$$에 대해 *descendant GW invariant*는

$$\left\langle \tau_{k_1}(\gamma_1), \ldots, \tau_{k_{n+1}}(\gamma_{n+1})\right\rangle_{0, n+1, \beta} := \int_{[\overline{\mathcal{M}}_{0, n+1}(X, \beta)]^{\mathrm{vir}}} \prod_{i=1}^{n+1} \psi_i^{k_i} \smile \mathrm{ev}_i^\ast \gamma_i$$

로 정의된다. $$k_i = 0$$인 경우 *primary* invariant, 적어도 하나의 $$k_i \geq 1$$이면 *gravitational descendant*이다. 직관적으로 $$\psi_i$$는 marked point에서 곡선의 "접선 자유도"를 측정하며, 그 거듭제곱은 marked point에 jet 조건을 부여하는 효과를 갖는다.

$$J$$-function의 정의에 등장하는 기호 $$\langle \cdots, \frac{1}{z - \psi}\rangle$$는 마지막 marked point에 모든 차수의 $$\psi$$-거듭제곱을 한꺼번에 끼우는 generating function 표기이다.

$$\left\langle \gamma_1, \ldots, \gamma_n, \frac{\gamma_{n+1}}{z - \psi}\right\rangle_{0, n+1, \beta} = \sum_{k \geq 0} z^{-k-1} \left\langle \gamma_1, \ldots, \gamma_n, \tau_k(\gamma_{n+1})\right\rangle_{0, n+1, \beta}$$

### 정의

<div class="definition" markdown="1">

<ins id="def1">**정의 1**</ins> $$X$$의 (small) *Givental $$J$$-function<sub>Givental J-함수</sub>* $$J_X: (\mathbb{C}^\ast)^r \times \mathbb{C}^\ast \to H^\ast(X)$$는 다음으로 정의된다.

$$J_X(q, z) := e^{t_{(2)}/z}\left( 1 + \sum_{\substack{\beta \in \mathrm{NE}(X) \\ \beta \neq 0}} \sum_{a=0}^s q^\beta\, \left\langle \frac{T_a}{z(z - \psi)} \right\rangle_{0, 1, \beta} T^a \right)$$

여기서 $$\frac{1}{z(z-\psi)}$$는 한 marked point에 $$\sum_{k \geq 0} z^{-k-2} \psi^k$$ 형태로 끼워 모든 차수의 descendant를 모은다는 의미이다 (위 ⁋Descendant Gromov-Witten invariant 절 참고). 지수 인자 $$e^{t_{(2)}/z}$$는 $$H^2$$ 방향의 divisor equation을 흡수하는 normalization이며, 합 안에는 $$\beta \neq 0$$ 항만 남아 있다.

</div>

위 정의의 각 성분이 담고 있는 정보는 다음과 같이 읽힌다. $$z \to \infty$$의 leading term $$1$$은 모든 quantum 보정을 끈 *classical* limit이다. $$z^{-1}$$의 계수는 (괄호 안 GW sum의 insertion $$T_a/(z(z-\psi))$$이 $$z^{-2}$$ 차수부터 시작하므로) 순전히 $$e^{t_{(2)}/z}$$ prefactor에서 오는 $$t_{(2)} = \sum_b t^b T_b$$이며, GW invariant는 여기까지 끼어들지 않는다. $$z^{-2}$$의 계수에서 처음으로 $$(t_{(2)})^2/2$$ (prefactor)와 함께 *primary* GW invariant $$\sum_\beta q^\beta \sum_a \langle T_a\rangle_{0,1,\beta}\,T^a$$가 나타나며, 이는 $$\psi$$ 없이 단 한 점에 $$T_a$$의 pullback만 적분한 enumerative 수이다. 일반적으로 $$z^{-k}$$ ($$k \geq 2$$)의 계수에는 prefactor의 $$(t_{(2)})^k/k!$$와 더불어 $$\psi^{k-2}$$가 끼인 *gravitational descendant* $$\langle \tau_{k-2}(T_a)\rangle_{0,1,\beta}$$이 들어 있다. 즉 $$J$$-function은 모든 차수의 descendant invariant를 하나의 $$z$$-급수로 묶어 둔 *master* 생성함수이며, 그 묶음 자체가 ($$\ast$$)의 자연스러운 fundamental solution을 이룬다는 것이 다음 절의 내용이다.

## QDE의 fundamental solution

위 ⁋동기에서 본 ansatz는 ($$\ast$$)의 해의 형태가 "leading 1 + GW descendant 보정"의 꼴로 강제됨을 시사했고, [정의 1](#def1)의 $$J$$-function은 그 정확한 표현이다. 이를 명제로 정리하자.

[§가우스-마닌 접속, ⁋명제 7](/ko/math/mirror_symmetry/gauss-manin_connection#prop7)에서 B-side의 fundamental solution은 cohomology basis $$\{e_a\}$$와 thimble basis $$\{[\Gamma_p]\}$$ 사이의 period $$\mathcal{I}^a_p$$로 적힌 행렬이었다. A-side에서 그에 대응하는 행렬은 *Givental의 $$S$$-matrix*로 알려진 endomorphism-값 함수이며, $$J$$-function은 그 한 column이다.

<div class="proposition" markdown="1">

<ins id="prop2">**명제 2** ($$J$$-function as fundamental solution column)</ins> Endomorphism $$S(q, z) \in \End(H^\ast(X))$$를 다음의 matrix element

$$\eta\bigl(S(q,z)\,T_a,\, T_b\bigr) := \eta(T_a, T_b) + \sum_{\beta \neq 0} q^\beta \left\langle \frac{T_a}{z - \psi},\, T_b \right\rangle_{0, 2, \beta}$$

으로 정의하자 ($$\eta$$는 Poincaré pairing). 그러면

1. *(Flat section property)* $$S(q, z)$$의 각 column $$S(q, z) T_b$$는 dual small Dubrovin connection $$\nabla^{z, \vee}$$의 horizontal section이다. 즉
   
   $$z\, q_a\partial_{q_a} \bigl(S(q,z)T_b\bigr) = T_a \qtimes \bigl(S(q,z)T_b\bigr)\qquad (a = 1, \ldots, r).$$

2. *($$J$$ = $$T_0$$ column)* $$J_X(q, z) = e^{t_{(2)}/z}\, S(q, z)\, T_0$$가 성립한다. 특히 $$J$$ 자체도 ($$\ast$$)의 horizontal section이고,
   
   $$z\, q_a\partial_{q_a} J_X = T_a \qtimes J_X \qquad (a = 1, \ldots, r).$$

</div>

<details class="proof" markdown="1">
<summary>증명 개요</summary>

핵심은 두 가지 GW 공리, 즉 *string equation* (marked point에 $$T_0 = 1$$을 끼울 때의 reduction)과 *divisor equation* ($$H^2$$ class를 끼울 때의 $$T_a \cdot \beta$$ 인자)을 정합적으로 활용하는 것이다. 

(2)는 $$T_b = T_0 = 1$$을 대입했을 때 string equation $$\langle \tau_k(T_a), 1\rangle_{0,2,\beta} = \langle \tau_{k-1}(T_a)\rangle_{0,1,\beta}$$ ($$k \geq 1$$, $$\beta \neq 0$$, $$k = 0$$인 항은 vanishing)으로 marked point 하나가 사라지면서 $$z^{-1}\langle T_a/(z-\psi)\rangle$$로 정리되고, 이것이 정확히 [정의 1](#def1)의 small J 식 안에 들어 있는 $$\langle T_a/(z(z-\psi))\rangle$$이 됨을 확인하면 된다. (1)의 flat section property는 $$q_a\partial_{q_a}$$의 작용이 marked point에 $$T_a$$를 추가로 끼우는 효과 (divisor equation을 거꾸로 푼 것)임을 사용하면 $$z\, q_a\partial_{q_a}$$가 $$T_a$$ 삽입 + $$z$$-shift를 주고, 그 후 한 marked point를 $$T_b/(z-\psi)$$와 분리하는 *topological recursion relation* ($$\overline{M}_{0, n+1}$$의 $$\psi$$-class를 boundary divisor의 합으로 분해하는 관계식)을 통해 우변의 $$T_a \qtimes$$ 작용과 같아짐을 보인다. 자세한 계산은 [CK, Theorem 10.3.1] 또는 [MS, Chapter 28–29] 참조.

</details>

[명제 2](#prop2)는 $$J$$-function이 단순한 enumerative 데이터의 묶음을 넘어, A-model 측 fundamental solution matrix $$S$$의 한 열 (구체적으로 normalization element $$T_0 = 1$$에 해당하는 열)을 이룸을 보여준다. 다른 열들도 $$S$$의 정의식에 다른 $$T_b$$를 넣으면 직접 얻을 수 있으므로, 결국 small QDE의 모든 flat section은 GW invariant의 generating function으로 표현된다. 

특히 $$S$$ (혹은 그 한 열인 $$J$$)는 B-side의 period matrix $$\mathcal{I}^a_p$$ ([§가우스-마닌 접속, ⁋명제 7](/ko/math/mirror_symmetry/gauss-manin_connection#prop7))와 정확히 짝을 이룬다. 각 column이 한 flat section을 나타낸다는 의미에서 두 행렬은 같은 역할을 하는 객체이며, 이들이 서로 일치한다는 것이 다음 절의 mirror theorem의 기하학적 내용이다.

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

## Big quantum cohomology로의 확장

지금까지 다룬 small $$J$$-function은 [§두브로빈 접속, §§D-module](/ko/math/mirror_symmetry/dubrovin_connection#d-module)의 $$H^2$$ 방향만의 deformation을 base로 한 small quantum $$D$$-module에 대한 fundamental solution이었다. 같은 글의 앞부분에서 본 것처럼 Dubrovin connection 자체는 사실 $$H^\ast(X)$$ 전체 deformation을 base로 한 big quantum cohomology 위에서 정의되었으며, $$H^2$$ 방향만 본 small 버전은 이를 specialize한 것이었다. 같은 격상이 $$J$$-function에 대해서도 가능하며, 그것이 *big $$J$$-function*이다. 

Big 버전의 setup으로 가려면 $$H^\ast(X)$$의 일반적인 deformation parameter $$t = \sum_{a=0}^s t^a T_a$$를 도입해야 한다. 임의의 $$t \in H^\ast(X)$$에 대한 big quantum product $$\star_t$$는 [§두브로빈 접속, §§D-module](/ko/math/mirror_symmetry/dubrovin_connection#d-module)에서 본 대로 $$\mathcal{C}_\alpha = T_\alpha \star_t -$$로 Dubrovin connection의 connection $$1$$-form을 결정한다. 그 dual horizontal section equation은

$$z\,\partial_a s = T_a \star_t s\qquad (a = 0, 1, \ldots, s)$$

이며, 이것이 small case의 ($$\ast$$)를 $$H^\ast$$ 전체 방향으로 확장한 *big QDE*이다. 

<div class="definition" markdown="1">

<ins id="def7">**정의 7** (Big $$J$$-function)</ins> $$X$$의 *big Givental $$J$$-function* $$J_X^{\mathrm{big}}: H^\ast(X) \times \mathbb{C}^\ast \to H^\ast(X)$$는 다음으로 정의된다.

$$J_X^{\mathrm{big}}(t, z) := e^{t_{(2)}/z}\left( 1 + \sum_{\substack{\beta \in \mathrm{NE}(X),\, n \geq 0 \\ (\beta, n) \neq (0, 0)}} \sum_{a=0}^s \frac{q^\beta}{n!}\, \left\langle \frac{T_a}{z - \psi}, t, \ldots, t \right\rangle_{0, n+1, \beta} T^a \right)$$

여기서 첫 marked point에 $$T_a/(z-\psi)$$가 (즉 $$T_a$$의 pullback에 모든 차수의 $$\psi^k$$가 generating function 형태로) 끼이고, 나머지 $$n$$개 marked point에 모두 $$t \in H^\ast(X)$$가 삽입되어 총 $$n+1$$개 marked point를 이룬다.

</div>

Big J가 big QDE의 horizontal section을 이룬다는 사실은 [명제 2](#prop2)의 small 버전과 같은 논증 — $$\partial_a$$를 marked point 추가, $$\psi$$-class를 topological recursion relation으로 분해 — 을 모든 $$a = 0, \ldots, s$$에 대해 적용하면 그대로 따른다. 그리고 small J는 big J의 $$t = t_{(2)} \in H^2(X)$$ specialization으로 복원되는데, $$H^2$$ 삽입에 (descendant 보정항이 붙은) divisor equation을 $$n$$번 적용하면 $$t_{(2)}$$ 삽입들이 $$(t_{(2)} \cdot \beta)^n$$ 인자와 $$\psi$$-shift 보정으로 빠져나오고, 이들이 $$\sum_n (t_{(2)}\cdot \beta)^n/n! = q^\beta$$로 합산되며 $$\psi$$-shift 보정이 추가 $$z^{-1}$$ 인자를 만들어내어, 결과적으로 marked point가 $$1$$개로 줄어든 [정의 1](#def1)의 small J 형태가 그대로 복원된다. 

Big J-function이 담고 있는 추가 정보는 임의의 cohomology class들로 정해지는 모든 descendant invariant들이다. 이를 토대로 mirror theorem ([명제 3](#prop3))도 big 버전으로 격상되어 *전체* $$S$$-matrix와 *전체* period matrix의 일치를 주장하는 더 강한 statement가 되며, $$I = J$$ ([명제 5](#prop5))도 mirror map $$\tau(q)$$가 일반적으로 자명하지 않은 big version에서 더 풍부한 내용을 갖는다 (예시: Calabi-Yau hypersurface). 한편 우리의 주된 응용 대상인 toric Fano variety (특히 Fano index $$\geq 2$$) 와 partial flag variety 의 경우 mirror map이 trivial하거나 small 정보로 충분하여, 본 글의 main thread는 small case로 일관되게 진행하였다.

---

**참고문헌**

**[CK]** D. A. Cox, S. Katz, *Mirror Symmetry and Algebraic Geometry*, Mathematical Surveys and Monographs **68**, AMS, 1999.

**[MS]** K. Hori, S. Katz, A. Klemm, R. Pandharipande, R. Thomas, C. Vafa, R. Vakil, E. Zaslow, *Mirror Symmetry*, Clay Mathematics Monographs **1**, AMS, 2003.
