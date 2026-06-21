---
title: "Hodge 이론"
description: "콤팩트 Kähler 다양체 위에서 Hodge star와 d·∂·∂̄의 형식 수반작용소, 그로부터 정의되는 Laplace 작용소와 조화형식을 세운다. 타원작용소 이론의 귀결인 Hodge 정리로 각 de Rham 코호몰로지류에 유일한 조화 대표가 대응함을 서술하고, Kähler 항등식에서 따라오는 Δ_d = 2Δ_∂̄를 이용해 조화형식이 (p,q)-차수로 쪼개짐을 본다. 이로부터 Hodge 분해 H^k(X,ℂ) = ⊕_{p+q=k} H^{p,q}, Hodge 대칭 h^{p,q} = h^{q,p}, 홀수 Betti 수가 짝수라는 위상적 귀결, Hodge 다이아몬드, 그리고 hard Lefschetz 정리를 유도한다."
excerpt: "Hodge star, 수반작용소 d^*·∂^*·∂̄^*, Laplace 작용소, 조화형식, Hodge 정리, 조화 대표, Δ_d = 2Δ_∂̄, Hodge 분해, H^{p,q}≅H^q(X,Ω^p), Hodge 대칭, Hodge 수, 홀수 Betti 수는 짝수, Hodge 다이아몬드, CP^n, Lefschetz 연산자, hard Lefschetz 정리"

categories: [Math / Complex Geometry]
permalink: /ko/math/complex_geometry/hodge_theory
sidebar:
    nav: "complex_geometry-ko"

date: 2026-06-22
weight: 5

published: false
---

복소다양체에서 외미분이 $$d = \partial + \bar\partial$$로 갈라지고, 그로부터 정칙성을 재는 Dolbeault 코호몰로지 $$H^{p,q}_{\bar\partial}(X)$$가 나옴을 보았다 ([§Dolbeault 코호몰로지, ⁋정의 4](/ko/math/complex_geometry/dolbeault_cohomology#def4)). 같은 글에서 우리는 de Rham 코호몰로지의 $$(p,q)$$-분해

$$
H^k_{\mathrm{dR}}(X, \mathbb{C}) \overset{?}{\cong} \bigoplus_{p+q=k} H^{p,q}_{\bar\partial}(X)
$$

가 일반 복소다양체에서는 성립하지 않으며, 그것이 성립하려면 추가 기하구조가 필요함을 예고하였다. 그 추가 구조가 바로 Kähler 조건 $$d\omega = 0$$이며 ([§Kähler 다양체, ⁋정의 3](/ko/math/complex_geometry/kahler_manifolds#def3)), 거기서 따라오는 Kähler 항등식 ([§Kähler 다양체, ⁋정리 12](/ko/math/complex_geometry/kahler_manifolds#thm12))이 위 분해를 콤팩트 Kähler 다양체에서 정확히 성립하게 만든다. 이 분해와 그에 동반하는 대칭을 규명하는 것이 Hodge 이론이며, 그것이 콤팩트 Kähler 다양체의 위상에 부과하는 제약이 이 글의 주제이다.

핵심 발상은 코호몰로지류마다 표준 대표원을 고르는 것이다. de Rham 코호몰로지류 $$[\alpha] \in H^k_{\mathrm{dR}}(X)$$는 $$\alpha + d\beta$$ 꼴의 닫힌형식 전체로 이루어진 affine 공간이며, 그 가운데 어느 하나를 본받아 류 전체를 다룰 자연스러운 방법이 없다. 그러나 리만 계량을 도입하면 형식들에 길이가 생기고, 각 류에서 $$L^2$$-노름을 최소화하는 유일한 대표원을 고를 수 있다. 이 최소 대표원이 *조화형식<sub>harmonic form</sub>*이며, Laplace 작용소의 핵으로 특징지어진다. 조화형식들의 공간 $$\mathcal{H}^k$$가 코호몰로지를 그대로 실현한다는 것이 Hodge 정리이고, Kähler 조건 아래에서 $$\mathcal{H}^k$$가 $$(p,q)$$-차수로 쪼개진다는 것이 Hodge 분해이다.

## Hodge star와 수반작용소

콤팩트 지향 리만다양체 $$(M, g)$$ 위에서 형식들에 점별 내적과 전역 $$L^2$$-내적을 부여하는 데서 출발한다. 차원을 $$m = \dim_{\mathbb{R}} M$$이라 하자. 계량 $$g$$는 각 점에서 여접공간 $$T_x^\ast M$$에 내적을 주고, 이를 외대수 $$\Lambda^k T_x^\ast M$$로 끌어올리면 $$k$$-형식들에 점별 내적 $$\langle \cdot, \cdot \rangle_x$$가 생긴다. 지향성은 표준 부피형식 $$\mathrm{vol}_g$$를 정해 주며, 이 둘을 결합하면 차수를 바꾸는 선형 동형이 따라온다.

<div class="definition" markdown="1">

<ins id="def1">**정의 1**</ins> 콤팩트 지향 리만다양체 $$(M, g)$$의 차원을 $$m$$이라 하자. *Hodge star operator<sub>Hodge 별작용소</sub>* $$\ast : \Lambda^k T^\ast M \to \Lambda^{m-k} T^\ast M$$를, 모든 $$k$$-형식 $$\alpha, \beta$$에 대하여

$$
\alpha \wedge \ast\beta = \langle \alpha, \beta \rangle\, \mathrm{vol}_g
$$

가 성립하도록 정의되는 유일한 선형사상이라 한다.

</div>

이 식이 $$\ast\beta$$를 유일하게 결정함은 wedge 곱 $$\Lambda^k \times \Lambda^{m-k} \to \Lambda^m$$이 비퇴화 쌍선형형식이기 때문이다. 곧 좌변 $$\alpha \wedge \ast\beta$$가 모든 $$\alpha$$에 대해 우변과 같아야 한다는 조건이 $$\ast\beta \in \Lambda^{m-k}$$를 한 점씩 결정한다. 정규직교 기저 $$e_1, \ldots, e_m$$에서는 $$\ast(e_{i_1} \wedge \cdots \wedge e_{i_k}) = \pm\, e_{j_1} \wedge \cdots \wedge e_{j_{m-k}}$$로, 보각 인덱스의 곱에 지향이 정하는 부호를 붙인 것이다. Hodge star는 두 번 적용하면 부호만 남겨 항등작용소에 가까워진다. 곧 $$k$$-형식 위에서 $$\ast\ast = (-1)^{k(m-k)}$$이다.

전역 내적은 이 점별 내적을 콤팩트성으로 적분하여 얻는다.

<div class="definition" markdown="1">

<ins id="def2">**정의 2**</ins> 콤팩트 지향 리만다양체 $$M$$ 위의 두 매끄러운 $$k$$-형식 $$\alpha, \beta$$에 대하여 *$$L^2$$-inner product<sub>$$L^2$$-내적</sub>*를

$$
(\alpha, \beta) = \int_M \langle \alpha, \beta \rangle\, \mathrm{vol}_g = \int_M \alpha \wedge \ast\beta
$$

로 정의한다. 이는 매끄러운 $$k$$-형식 공간 $$\Omega^k(M)$$ 위의 양의 정부호 내적이다.

</div>

둘째 등식은 [정의 1](#def1)에서 즉시 따라오며, $$\langle \cdot, \cdot \rangle$$이 각 점에서 양의 정부호이고 $$M$$이 콤팩트라 적분이 유한하므로 $$(\cdot, \cdot)$$은 양의 정부호 내적이 된다. 복소값 형식에 대해서는 둘째 변수에 복소켤레를 넣어 $$(\alpha, \beta) = \int_M \alpha \wedge \ast\bar\beta$$로 두면 Hermitian 내적이 된다. 이 $$L^2$$-내적이 있어야 외미분 $$d$$의 수반작용소를 말할 수 있다.

<div class="definition" markdown="1">

<ins id="def3">**정의 3**</ins> 콤팩트 지향 리만다양체 $$M$$ 위에서 외미분 $$d : \Omega^k(M) \to \Omega^{k+1}(M)$$의 *형식 수반작용소<sub>formal adjoint</sub>* $$d^\ast : \Omega^{k+1}(M) \to \Omega^k(M)$$를, 모든 $$\alpha \in \Omega^k$$, $$\beta \in \Omega^{k+1}$$에 대하여

$$
(d\alpha, \beta) = (\alpha, d^\ast\beta)
$$

가 성립하는 작용소로 정의한다. 명시적으로, $$p$$-형식 위에서 $$d^\ast = (-1)^{m(p+1)+1} \ast d\, \ast$$이며, 이는 차수를 하나 내린다.

</div>

수반작용소가 존재하고 유일함은 Stokes 정리에서 나온다. $$M$$이 경계 없는 콤팩트 다양체이므로 $$\int_M d(\alpha \wedge \ast\beta) = 0$$이고, $$d(\alpha \wedge \ast\beta) = d\alpha \wedge \ast\beta + (-1)^k \alpha \wedge d(\ast\beta)$$를 전개하여 $$\ast\ast$$의 부호를 정리하면 위 명시 공식이 $$(d\alpha, \beta) = (\alpha, d^\ast\beta)$$를 만족함을 직접 확인할 수 있다. 작용소 $$d$$가 차수를 하나 올리는 반면 $$d^\ast$$는 하나 내리며, $$d^2 = 0$$에서 $$(d^\ast)^2 = 0$$이 따라온다. 복소다양체에서는 같은 방식으로 $$\partial$$과 $$\bar\partial$$의 수반작용소 $$\partial^\ast$$, $$\bar\partial^\ast$$를 $$L^2$$-내적에 대해 정의하며 ([§Kähler 다양체, ⁋정리 12](/ko/math/complex_geometry/kahler_manifolds#thm12)에서 이미 도입), $$\partial^\ast = -\ast\bar\partial\ast$$, $$\bar\partial^\ast = -\ast\partial\ast$$ 꼴이다 (Hodge star가 $$\partial$$과 $$\bar\partial$$를 맞바꾸므로 수반에 켤레 작용소가 나타난다).

## Laplace 작용소와 조화형식

리만 계량과 수반작용소가 갖추어지면, 각 미분작용소에 그 자신과 수반작용소를 결합한 이차 작용소를 붙일 수 있다. 이것이 형식 위의 Laplace 작용소이며, 그 핵이 조화형식이다.

<div class="definition" markdown="1">

<ins id="def4">**정의 4**</ins> 콤팩트 지향 리만다양체 $$M$$ 위에서 *Hodge–de Rham Laplacian<sub>Hodge–de Rham Laplace 작용소</sub>* $$\Delta_d : \Omega^k(M) \to \Omega^k(M)$$를

$$
\Delta_d = d d^\ast + d^\ast d
$$

로 정의한다. $$\Delta_d \alpha = 0$$인 형식 $$\alpha$$를 *harmonic form<sub>조화형식</sub>*이라 하고, 콤팩트 $$M$$ 위의 조화 $$k$$-형식 전체의 공간을

$$
\mathcal{H}^k(M) = \{ \alpha \in \Omega^k(M) \mid \Delta_d \alpha = 0 \}
$$

로 적는다.

</div>

작용소 $$\Delta_d$$는 차수를 보존하는 이차 미분작용소이며, $$d$$와 $$d^\ast$$가 서로 수반이므로 $$L^2$$-내적에 대해 자기수반이다. 곧 $$(\Delta_d\alpha, \beta) = (\alpha, \Delta_d\beta)$$이다. 조화형식은 단순히 $$\Delta_d$$로 죽는 형식인데, 콤팩트성 덕분에 이 조건이 훨씬 강한 조건과 동치가 된다.

<div class="proposition" markdown="1">

<ins id="prop5">**명제 5**</ins> 콤팩트 지향 리만다양체 $$M$$ 위의 $$k$$-형식 $$\alpha$$에 대하여 다음이 동치이다.

1. $$\alpha$$는 조화형식이다. 곧 $$\Delta_d \alpha = 0$$.
2. $$d\alpha = 0$$이고 $$d^\ast\alpha = 0$$이다.

</div>

<details class="proof" markdown="1">
<summary>증명</summary>

(2) ⟹ (1)은 정의에서 즉각적이다. $$d\alpha = 0$$, $$d^\ast\alpha = 0$$이면 $$\Delta_d\alpha = d d^\ast\alpha + d^\ast d\alpha = 0 + 0 = 0$$이다.

(1) ⟹ (2)에서 콤팩트성이 쓰인다. $$\Delta_d\alpha = 0$$이라 하고 $$\alpha$$ 자신과의 $$L^2$$-내적을 취하면, $$d$$와 $$d^\ast$$가 수반관계이므로

$$
0 = (\Delta_d\alpha, \alpha) = (d d^\ast\alpha, \alpha) + (d^\ast d\alpha, \alpha) = (d^\ast\alpha, d^\ast\alpha) + (d\alpha, d\alpha) = \lVert d^\ast\alpha \rVert^2 + \lVert d\alpha \rVert^2
$$

이다. 두 항이 모두 음이 아닌 실수인데 그 합이 $$0$$이므로 각각 $$0$$이고, $$L^2$$-내적이 양의 정부호이므로 $$d\alpha = 0$$, $$d^\ast\alpha = 0$$이 따라온다.

</details>

이 동치는 조화형식이 닫힌형식임을 보장한다. 조화형식은 $$d\alpha = 0$$이므로 코호몰로지류 $$[\alpha] \in H^k_{\mathrm{dR}}(M)$$를 정의하며, 동시에 $$d^\ast\alpha = 0$$이라는 추가 조건이 그 류 안에서 $$\alpha$$를 특별한 위치에 놓는다. 닫힌형식 $$\alpha + d\beta$$ 가운데 $$\alpha$$가 조화라는 것은 그것이 같은 류 안에서 $$L^2$$-노름을 최소화한다는 것과 같다. $$\lVert \alpha + d\beta \rVert^2 = \lVert \alpha \rVert^2 + 2(\alpha, d\beta) + \lVert d\beta \rVert^2 = \lVert \alpha \rVert^2 + 2(d^\ast\alpha, \beta) + \lVert d\beta \rVert^2 = \lVert \alpha \rVert^2 + \lVert d\beta \rVert^2 \geq \lVert \alpha \rVert^2$$이기 때문이다 (여기서 $$d^\ast\alpha = 0$$을 썼다). 곧 조화 대표원은 각 류에서 가장 짧은 형식이다.

## Hodge 정리

조화형식이 각 코호몰로지류에서 노름 최소 대표라는 관찰은, 그러한 대표가 실제로 존재하고 유일한가라는 물음을 남긴다. 이것이 Hodge 이론의 해석적 심장이며, 그 답은 $$\Delta_d$$가 타원작용소라는 사실에서 나오는 깊은 결과이다.

<div class="proposition" markdown="1">

<ins id="thm6">**정리 6 (Hodge 정리)**</ins> $$M$$을 콤팩트 지향 리만다양체라 하자. 그러면 각 $$k$$에 대하여 조화 $$k$$-형식 공간 $$\mathcal{H}^k(M)$$은 유한차원이고, $$L^2$$-직교분해

$$
\Omega^k(M) = \mathcal{H}^k(M) \oplus d\,\Omega^{k-1}(M) \oplus d^\ast\,\Omega^{k+1}(M)
$$

이 성립한다. 따라서 각 de Rham 코호몰로지류는 유일한 조화 대표원을 가지며, 표준적인 동형

$$
H^k_{\mathrm{dR}}(M, \mathbb{R}) \cong \mathcal{H}^k(M)
$$

이 성립한다.

</div>

<details class="proof" markdown="1">
<summary>증명</summary>

분해 자체는 타원작용소 이론의 결과이므로 그 핵심 입력만 인용하고, 거기서 코호몰로지와의 동형을 끌어내는 부분을 증명한다.

작용소 $$\Delta_d$$는 콤팩트 다양체 위의 자기수반 이차 타원작용소이다. 타원성은 그 주표상 $$\sigma(\Delta_d)(\xi) = -\lvert \xi \rvert^2 \cdot \mathrm{id}$$이 $$\xi \neq 0$$에서 가역이라는 데서 나오며, 콤팩트 다양체 위 자기수반 타원작용소에 대한 일반론(Fredholm 이론과 타원 정칙성)이 다음을 준다. 핵 $$\mathcal{H}^k = \ker\Delta_d$$는 유한차원이고, $$L^2$$-직교분해 $$\Omega^k = \ker\Delta_d \oplus \Img\Delta_d$$가 성립하며, $$\Img\Delta_d = \Img(d d^\ast + d^\ast d)$$이다. 여기까지가 인용하는 해석적 사실이다.

이제 $$\Img\Delta_d = d\,\Omega^{k-1} \oplus d^\ast\,\Omega^{k+1}$$임을 본다. 포함 $$\supseteq$$의 직교성부터 본다. $$d\eta$$와 $$d^\ast\zeta$$의 내적은 $$(d\eta, d^\ast\zeta) = (d d\eta, \zeta) = 0$$이므로 두 부분공간은 직교한다. 또 $$\Delta_d\gamma = d(d^\ast\gamma) + d^\ast(d\gamma) \in d\,\Omega^{k-1} + d^\ast\,\Omega^{k+1}$$이므로 $$\Img\Delta_d \subseteq d\,\Omega^{k-1} \oplus d^\ast\,\Omega^{k+1}$$이다. 역으로 $$d\eta$$를 분해의 셋째 직교성으로 본다. $$d\eta$$는 $$\mathcal{H}^k$$와 직교한다 (조화 $$\alpha$$에 대해 $$(d\eta, \alpha) = (\eta, d^\ast\alpha) = 0$$, [명제 5](#prop5)). 마찬가지로 $$d^\ast\zeta$$도 $$\mathcal{H}^k$$와 직교한다 ($$(d^\ast\zeta, \alpha) = (\zeta, d\alpha) = 0$$). 따라서 $$d\,\Omega^{k-1} \oplus d^\ast\,\Omega^{k+1} \subseteq (\mathcal{H}^k)^\perp = \Img\Delta_d$$이고, 위 포함과 합쳐 등식이 성립한다. 이로써

$$
\Omega^k(M) = \mathcal{H}^k(M) \oplus d\,\Omega^{k-1}(M) \oplus d^\ast\,\Omega^{k+1}(M)
$$

을 얻는다.

이 분해로부터 코호몰로지와의 동형을 끌어낸다. 닫힌 $$k$$-형식 $$\alpha$$를 위 분해로 $$\alpha = h + d\eta + d^\ast\zeta$$로 쓰면, $$d\alpha = 0$$이고 $$dh = 0$$ (조화는 닫힘), $$d(d\eta) = 0$$이므로 $$d(d^\ast\zeta) = 0$$이다. 그러면 $$0 = (d d^\ast\zeta, \zeta) = (d^\ast\zeta, d^\ast\zeta) = \lVert d^\ast\zeta \rVert^2$$이 되어 $$d^\ast\zeta = 0$$이다. 따라서 닫힌형식은 $$\alpha = h + d\eta$$ 꼴, 곧 조화 부분과 완전 부분의 합으로만 쓰인다. 이는 코호몰로지류 $$[\alpha] = [h]$$가 유일한 조화 대표 $$h$$를 가짐을 뜻한다. 존재는 방금 보인 분해가 주고, 유일성은 두 조화형식이 코호몰로지에서 같으면 그 차 $$h_1 - h_2 = d\beta$$가 조화이자 완전형식인데, $$(d\beta, d\beta) = (\beta, d^\ast d\beta)$$에서 $$d^\ast(d\beta) = \Delta_d(d\beta) - d d^\ast d\beta$$를 따져 $$\Delta_d(d\beta)=0$$이고 $$d^\ast(d\beta)=0$$이면 $$(d\beta,d\beta)=(\beta, d^\ast d \beta)=0$$, 곧 $$d\beta = 0$$이 되어 두 대표가 같음에서 나온다. 따라서 $$[\alpha] \mapsto h$$가 잘 정의된 선형동형 $$H^k_{\mathrm{dR}}(M, \mathbb{R}) \cong \mathcal{H}^k(M)$$을 준다.

</details>

Hodge 정리는 위상적 불변량인 de Rham 코호몰로지를 해석적·계량적 대상인 조화형식으로 실현한다. 코호몰로지류라는 형식들의 무한차원 affine 공간이, 계량을 하나 정하는 순간 유한차원의 유일한 점 $$\mathcal{H}^k$$로 응축되는 것이다. 이 정리는 임의의 콤팩트 지향 리만다양체에서 성립하며, 복소구조나 Kähler 조건을 전혀 요구하지 않는다. 복소다양체에서는 같은 논법이 $$\bar\partial$$에 대해서도 작동하여, $$\Delta_{\bar\partial} = \bar\partial\bar\partial^\ast + \bar\partial^\ast\bar\partial$$의 핵 $$\mathcal{H}^{p,q}_{\bar\partial}$$가 Dolbeault 코호몰로지를 실현한다. 곧 콤팩트 Hermitian 다양체에서 $$H^{p,q}_{\bar\partial}(X) \cong \mathcal{H}^{p,q}_{\bar\partial}(X)$$가 성립한다. 여기서 $$\Delta_d$$와 $$\Delta_{\bar\partial}$$는 서로 무관한 작용소이며, 이 둘을 묶는 것이 바로 Kähler 조건이다.

## Kähler 조건과 Laplace 작용소

콤팩트 Hermitian 다양체에는 세 종류의 Laplace 작용소가 산다. 외미분에서 온 $$\Delta_d = d d^\ast + d^\ast d$$, 그리고 $$\partial$$·$$\bar\partial$$에서 온

$$
\Delta_\partial = \partial\partial^\ast + \partial^\ast\partial, \qquad \Delta_{\bar\partial} = \bar\partial\bar\partial^\ast + \bar\partial^\ast\bar\partial
$$

이다. 일반 Hermitian 다양체에서는 이 셋이 서로 다른 작용소이며, 특히 $$\Delta_d$$가 차수보존인 반면 $$\Delta_\partial$$, $$\Delta_{\bar\partial}$$는 $$(p,q)$$-차수를 보존한다. Kähler 조건은 이 셋을 상수배로 묶어, $$\Delta_d$$의 조화형식이 자동으로 $$(p,q)$$-차수로 갈라지게 한다.

<div class="proposition" markdown="1">

<ins id="thm7">**정리 7 (Kähler Laplace 항등식)**</ins> $$(X, J, g)$$가 Kähler 다양체이면

$$
\Delta_d = 2\,\Delta_\partial = 2\,\Delta_{\bar\partial}
$$

이 성립한다. 특히 $$\Delta_d$$는 $$(p,q)$$-차수를 보존하며, 콤팩트 Kähler 다양체에서 조화 $$k$$-형식 공간은

$$
\mathcal{H}^k_d(X) = \bigoplus_{p+q=k} \mathcal{H}^{p,q}_{\bar\partial}(X)
$$

로 직합 분해된다. 여기서 $$\mathcal{H}^{p,q}_{\bar\partial}(X) = \{ \alpha \in \Omega^{p,q}(X) \mid \Delta_{\bar\partial}\alpha = 0 \}$$이다.

</div>

<details class="proof" markdown="1">
<summary>증명</summary>

Kähler 항등식 ([§Kähler 다양체, ⁋정리 12](/ko/math/complex_geometry/kahler_manifolds#thm12)) $$[\Lambda, \bar\partial] = -i\,\partial^\ast$$, $$[\Lambda, \partial] = i\,\bar\partial^\ast$$에서 출발한다. 둘째 항등식을 수반으로 옮기면 $$\partial^\ast = i[\bar\partial, L]$$ 류의 동반관계가 따라오나, 직접 계산에는 위 두 식과 $$\partial^\ast = i[\Lambda, \bar\partial]$$의 부호만 쓰면 충분하다.

먼저 $$\Delta_\partial = \Delta_{\bar\partial}$$를 본다. $$\partial^\ast = i[\Lambda, \bar\partial] = i(\Lambda\bar\partial - \bar\partial\Lambda)$$이므로

$$
\Delta_\partial = \partial\partial^\ast + \partial^\ast\partial = i\big( \partial(\Lambda\bar\partial - \bar\partial\Lambda) + (\Lambda\bar\partial - \bar\partial\Lambda)\partial \big)
$$

이다. 이를 전개하고 $$\partial\bar\partial = -\bar\partial\partial$$ ([§Dolbeault 코호몰로지, ⁋명제 3](/ko/math/complex_geometry/dolbeault_cohomology#prop3))를 써서 정리하면 $$\Delta_\partial = \Delta_{\bar\partial}$$가 따라온다. 마찬가지로 $$\bar\partial^\ast = -i[\Lambda, \partial]$$를 $$\Delta_{\bar\partial}$$에 대입해 같은 표현을 얻으면 두 작용소가 같음이 확인된다. 핵심은 $$\partial$$과 $$\bar\partial$$가 반가환하고, $$L$$·$$\Lambda$$와의 교환자가 위 항등식으로 주어진다는 데 있다.

다음으로 $$\Delta_d = \Delta_\partial + \Delta_{\bar\partial}$$를 본다. $$d = \partial + \bar\partial$$, $$d^\ast = \partial^\ast + \bar\partial^\ast$$이므로

$$
\Delta_d = (\partial + \bar\partial)(\partial^\ast + \bar\partial^\ast) + (\partial^\ast + \bar\partial^\ast)(\partial + \bar\partial) = \Delta_\partial + \Delta_{\bar\partial} + (\partial\bar\partial^\ast + \bar\partial^\ast\partial) + (\bar\partial\partial^\ast + \partial^\ast\bar\partial)
$$

이다. 마지막 두 괄호의 교차항이 Kähler 항등식 아래에서 소멸함을 보이면 된다. $$\bar\partial^\ast = -i[\Lambda, \partial]$$를 쓰면 $$\partial\bar\partial^\ast + \bar\partial^\ast\partial = -i\big( \partial\Lambda\partial - \partial\partial\Lambda + \Lambda\partial\partial - \partial\Lambda\partial \big) = -i(-\partial^2\Lambda + \Lambda\partial^2) = 0$$이다 ($$\partial^2 = 0$$). 켤레로 $$\bar\partial\partial^\ast + \partial^\ast\bar\partial = 0$$도 따라온다. 따라서 교차항이 모두 사라져 $$\Delta_d = \Delta_\partial + \Delta_{\bar\partial} = 2\Delta_{\bar\partial}$$이다 ($$\Delta_\partial = \Delta_{\bar\partial}$$이므로). 같은 이유로 $$\Delta_d = 2\Delta_\partial$$이다.

마지막으로 차수분해를 본다. $$\Delta_{\bar\partial}$$가 $$(p,q)$$-차수를 보존하므로 $$\Delta_d = 2\Delta_{\bar\partial}$$도 차수를 보존한다. 따라서 $$k$$-형식 $$\alpha = \sum_{p+q=k}\alpha^{p,q}$$가 $$\Delta_d\alpha = 0$$인 것은 각 차수 성분이 $$\Delta_d\alpha^{p,q} = 0$$, 곧 $$\Delta_{\bar\partial}\alpha^{p,q} = 0$$인 것과 동치이다. 그러므로 $$\mathcal{H}^k_d(X) = \bigoplus_{p+q=k}\mathcal{H}^{p,q}_{\bar\partial}(X)$$이다.

</details>

이 정리가 Hodge 이론의 전환점이다. 등식 $$\Delta_d = 2\Delta_{\bar\partial}$$은 Kähler 조건에서만 성립하며, 일반 Hermitian 다양체에서는 두 Laplace 작용소가 일치하지 않고 따라서 조화형식의 차수분해도 깨진다. 콤팩트 Kähler 다양체에서는 [정리 6](#thm6)의 조화 표현과 위 차수분해가 맞물려, de Rham 코호몰로지가 차수별로 쪼개진다. 이 차수보존성이 다음 절의 Hodge 분해를 즉시 낳는다.

## Hodge 분해와 Hodge 대칭

이제 콤팩트 Kähler 다양체에서 de Rham 코호몰로지의 $$(p,q)$$-분해를 정식화하고, 그것에 동반하는 복소켤레 대칭을 끌어낸다.

<div class="definition" markdown="1">

<ins id="def8">**정의 8**</ins> 콤팩트 Kähler 다양체 $$X$$에 대하여, $$(p,q)$$-차수의 *Hodge 부분공간<sub>Hodge subspace</sub>*을

$$
H^{p,q}(X) = \{ [\alpha] \in H^{p+q}_{\mathrm{dR}}(X, \mathbb{C}) \mid \alpha \in \mathcal{H}^{p,q}_{\bar\partial}(X) \}
$$

로, 곧 $$(p,q)$$-차수의 조화형식이 대표하는 de Rham 코호몰로지류들의 공간으로 정의한다. 그 복소차원 $$h^{p,q}(X) = \dim_{\mathbb{C}} H^{p,q}(X)$$를 *Hodge number<sub>Hodge 수</sub>*라 한다.

</div>

[정리 7](#thm7)에 의해 $$\mathcal{H}^{p,q}_{\bar\partial}(X) \subseteq \mathcal{H}^{p+q}_d(X)$$이므로, 각 $$(p,q)$$-조화형식은 닫힌형식이고 de Rham 류를 잘 정의한다. 또 콤팩트 Hermitian 다양체에서 Dolbeault 코호몰로지가 $$\bar\partial$$-조화형식으로 실현되므로 ([정리 6](#thm6)의 $$\bar\partial$$-판본), $$H^{p,q}(X)$$는 $$H^{p,q}_{\bar\partial}(X)$$와 자연히 동형이다. 곧 $$H^{p,q}(X) \cong H^{p,q}_{\bar\partial}(X) \cong H^q(X, \Omega^p)$$로, 마지막 동형은 Dolbeault 정리 ([§Dolbeault 코호몰로지, ⁋정리 9](/ko/math/complex_geometry/dolbeault_cohomology#thm9))에서 온다. 이 동일시가 Hodge 수가 [§Dolbeault 코호몰로지, ⁋정의 4](/ko/math/complex_geometry/dolbeault_cohomology#def4)의 Hodge 수와 일치함을 보장한다.

<div class="proposition" markdown="1">

<ins id="thm9">**정리 9 (Hodge 분해와 Hodge 대칭)**</ins> $$X$$를 콤팩트 Kähler 다양체라 하자. 그러면 각 $$k$$에 대하여 직합 분해

$$
H^k_{\mathrm{dR}}(X, \mathbb{C}) = \bigoplus_{p+q=k} H^{p,q}(X), \qquad H^{p,q}(X) \cong H^q(X, \Omega^p)
$$

이 성립하고, 복소켤레에 대한 대칭

$$
\overline{H^{p,q}(X)} = H^{q,p}(X)
$$

이 성립한다. 따라서 Hodge 수에 대해 $$h^{p,q}(X) = h^{q,p}(X)$$이다.

</div>

<details class="proof" markdown="1">
<summary>증명</summary>

분해부터 본다. [정리 6](#thm6)으로 $$H^k_{\mathrm{dR}}(X, \mathbb{C}) \cong \mathcal{H}^k_d(X)$$이고, [정리 7](#thm7)로 $$\mathcal{H}^k_d(X) = \bigoplus_{p+q=k}\mathcal{H}^{p,q}_{\bar\partial}(X)$$이다. 우변의 각 직합 성분 $$\mathcal{H}^{p,q}_{\bar\partial}(X)$$가 대표하는 코호몰로지류들이 정확히 [정의 8](#def8)의 $$H^{p,q}(X)$$이므로, 이 동형들을 합치면

$$
H^k_{\mathrm{dR}}(X, \mathbb{C}) = \bigoplus_{p+q=k} H^{p,q}(X)
$$

이다. 둘째 동형 $$H^{p,q}(X) \cong H^q(X, \Omega^p)$$은 $$\mathcal{H}^{p,q}_{\bar\partial}(X) \cong H^{p,q}_{\bar\partial}(X)$$ ([정리 6](#thm6)의 $$\bar\partial$$-판)과 Dolbeault 정리 ([§Dolbeault 코호몰로지, ⁋정리 9](/ko/math/complex_geometry/dolbeault_cohomology#thm9))를 잇대어 얻는다.

대칭을 본다. 계량 $$g$$가 실계량이고 $$X$$가 Kähler이므로 Laplace 작용소 $$\Delta_d$$는 실작용소이고 복소켤레와 교환한다. 곧 $$\alpha$$가 조화이면 $$\bar\alpha$$도 조화이다. 한편 복소켤레는 $$(p,q)$$-형식을 $$(q,p)$$-형식으로 보낸다 (좌표에서 $$\overline{dz_I \wedge d\bar{z}_J} = d\bar{z}_I \wedge dz_J$$이므로 정칙·반정칙 인덱스가 맞바뀐다). 따라서 켤레사상 $$\alpha \mapsto \bar\alpha$$는 $$\mathcal{H}^{p,q}_{\bar\partial}(X)$$를 $$\mathcal{H}^{q,p}_{\bar\partial}(X)$$로 보내는 $$\mathbb{R}$$-선형 동형(반선형 $$\mathbb{C}$$-동형)이다. 이것이 코호몰로지 수준에서 $$\overline{H^{p,q}(X)} = H^{q,p}(X)$$를 준다. 반선형 동형은 복소차원을 보존하므로 $$h^{p,q}(X) = \dim_{\mathbb{C}} H^{p,q}(X) = \dim_{\mathbb{C}} H^{q,p}(X) = h^{q,p}(X)$$이다.

</details>

Hodge 분해는 [§Dolbeault 코호몰로지](/ko/math/complex_geometry/dolbeault_cohomology)에서 예고한 등식 $$H^k_{\mathrm{dR}}(X, \mathbb{C}) = \bigoplus_{p+q=k} H^{p,q}$$가 콤팩트 Kähler 다양체에서 정확히 성립함을 확인해 준다. 결정적으로 이 분해는 Kähler 조건에 의존한다. 일반 콤팩트 복소다양체에서는 $$\Delta_d \neq 2\Delta_{\bar\partial}$$라 조화형식의 차수분해가 깨지고, 그 결과 위 직합이 성립하지 않는다. 예컨대 Hopf 곡면은 콤팩트 복소다양체이지만 $$b_1 = 1$$이 홀수라, 아래에서 보듯 Hodge 분해가 부과하는 짝수성 제약을 어겨 Kähler 계량을 가질 수 없다. Hodge 대칭은 정칙과 반정칙을 맞바꾸는 복소켤레가 코호몰로지에 남기는 흔적으로, 이로부터 Hodge 수의 표가 대각선에 대해 대칭이 된다.

## 위상적 귀결

Hodge 분해와 Hodge 대칭은 콤팩트 Kähler 다양체의 Betti 수에 직접적인 산술적 제약을 부과한다. 이는 콤팩트 복소다양체가 Kähler가 되기 위한 필요조건을 위상만으로 검출하게 해 준다.

<div class="proposition" markdown="1">

<ins id="cor10">**따름정리 10**</ins> $$X$$를 콤팩트 Kähler 다양체라 하자. 그러면 Betti 수 $$b_k(X) = \dim_{\mathbb{C}} H^k_{\mathrm{dR}}(X, \mathbb{C})$$에 대하여

$$
b_k(X) = \sum_{p+q=k} h^{p,q}(X)
$$

이고, 홀수 차수 Betti 수는 모두 짝수이다. 곧 모든 $$k$$에 대해 $$b_{2k+1}(X)$$는 짝수이다.

</div>

<details class="proof" markdown="1">
<summary>증명</summary>

[정리 9](#thm9)의 직합 분해에서 차원을 세면 $$b_k(X) = \dim_{\mathbb{C}} H^k_{\mathrm{dR}}(X, \mathbb{C}) = \sum_{p+q=k} \dim_{\mathbb{C}} H^{p,q}(X) = \sum_{p+q=k} h^{p,q}(X)$$이다.

홀수 차수의 경우 $$k = 2l+1$$로 두면, 합 $$\sum_{p+q=2l+1} h^{p,q}$$의 항들은 $$p \neq q$$인 쌍 $$(p,q)$$로만 이루어진다 ($$p + q$$가 홀수라 $$p = q$$가 불가능). 이 항들은 Hodge 대칭 $$h^{p,q} = h^{q,p}$$ ([정리 9](#thm9))에 의해 $$(p,q)$$와 $$(q,p)$$가 같은 값을 갖는 쌍으로 묶이며, 두 인덱스가 서로 다르므로 각 쌍이 서로 다른 두 항을 준다. 따라서

$$
b_{2l+1}(X) = \sum_{p+q=2l+1} h^{p,q}(X) = 2 \sum_{\substack{p+q=2l+1 \\ p < q}} h^{p,q}(X)
$$

로 $$2$$의 배수이다. 곧 홀수 차수 Betti 수는 짝수이다.

</details>

가장 단순한 경우 $$k = 1$$에서 $$b_1(X) = h^{1,0}(X) + h^{0,1}(X) = 2 h^{1,0}(X)$$로, 첫 Betti 수가 정칙 1-형식 공간 차원의 두 배가 된다. 이 짝수성은 콤팩트 복소다양체가 Kähler인지를 가르는 가장 손쉬운 장애이다. Hopf 곡면 $$S^1 \times S^3$$은 콤팩트 복소다양체이면서 $$b_1 = 1$$이 홀수이므로, 어떤 Hermitian 계량으로도 Kähler 구조를 가질 수 없다 ([§Kähler 다양체, ⁋명제 11](/ko/math/complex_geometry/kahler_manifolds#prop11)이 짝수 차수에 준 장애를 홀수 차수로 보완한다). 이로써 Kähler 조건은 짝수 Betti 수의 양성($$b_{2k} \geq 1$$)과 홀수 Betti 수의 짝수성이라는 두 위상적 제약을 동시에 부과한다.

Hodge 수들을 차수에 따라 마름모꼴로 배열한 것을 Hodge 다이아몬드라 부르며, 이는 한 콤팩트 Kähler 다양체의 코호몰로지 구조를 한눈에 담는다. $$h^{p,q}$$를 $$(p,q)$$ 위치에 두고 위에서 아래로 $$k = p + q$$가 커지도록 쌓으면, Hodge 대칭은 수직축에 대한 좌우 대칭으로, 복소차원 $$n$$의 Poincaré 쌍대성 ([\[대수적 위상수학\] §푸앵카레 쌍대성, ⁋정리 11](/ko/math/algebraic_topology/Poincare_duality#thm11))에서 오는 $$h^{p,q} = h^{n-p, n-q}$$는 중심에 대한 점대칭으로 나타난다. 아래 그림은 복소곡면($$n = 2$$)의 Hodge 다이아몬드를 보여준다.

![복소곡면 n=2의 Hodge 다이아몬드: h^{p,q}를 마름모꼴로 배열, 수직축 좌우대칭이 Hodge 대칭](/assets/images/Math/Complex_Geometry/Hodge_Theory-1.svg){:style="width:22.97em" class="invert" .align-center}

복소곡면의 경우 $$h^{0,0} = h^{2,2} = 1$$ (연결성과 Poincaré 쌍대), $$h^{1,0} = h^{0,1} = h^{2,1} = h^{1,2}$$ (Hodge 대칭과 Poincaré 쌍대로 모두 같은 값 $$q$$, 곧 irregularity), $$h^{2,0} = h^{0,2}$$ (geometric genus $$p_g$$), 그리고 가운데 $$h^{1,1}$$이 자리한다. 이로부터 $$b_0 = b_4 = 1$$, $$b_1 = b_3 = 2q$$, $$b_2 = 2p_g + h^{1,1}$$로 모든 Betti 수가 Hodge 수로 표현된다.

가장 깔끔한 예는 복소사영공간이다.

<div class="example" markdown="1">

<ins id="ex11">**예시 11 ($$\mathbb{CP}^n$$의 Hodge 다이아몬드)**</ins> 복소사영공간 $$\mathbb{CP}^n$$은 Fubini–Study 계량에 대해 콤팩트 Kähler 다양체이다 ([§Kähler 다양체, ⁋예시 8](/ko/math/complex_geometry/kahler_manifolds#ex8)). 그 코호몰로지는

$$
H^k_{\mathrm{dR}}(\mathbb{CP}^n, \mathbb{C}) = \begin{cases} \mathbb{C} & k = 0, 2, 4, \ldots, 2n \\ 0 & \text{그 외} \end{cases}
$$

로, $$0$$이 아닌 코호몰로지는 짝수 차수에만 있고 각각 $$1$$차원이며 Kähler 형식의 거듭제곱 $$[\omega^p]$$가 생성한다. 따라서 Hodge 분해에서 $$H^{2p}_{\mathrm{dR}} = H^{p,p}(\mathbb{CP}^n)$$만 비고 나머지 $$H^{p,q}$$ ($$p \neq q$$)는 모두 $$0$$이다. 곧 Hodge 수는

$$
h^{p,q}(\mathbb{CP}^n) = \begin{cases} 1 & p = q,\ 0 \leq p \leq n \\ 0 & p \neq q \end{cases}
$$

이다. Hodge 다이아몬드는 수직 중심축에만 $$1$$이 일렬로 놓이고 나머지가 모두 $$0$$인 형태가 된다. Betti 수는 $$b_{2p} = h^{p,p} = 1$$, $$b_{2p+1} = 0$$으로, 홀수 Betti 수가 모두 $$0$$ (짝수)이라 [따름정리 10](#cor10)과 부합한다.

</div>

$$\mathbb{CP}^n$$의 Hodge 다이아몬드가 대각선($$p = q$$)에만 무게가 실리는 것은 그 코호몰로지가 순전히 algebraic class, 곧 부분다양체의 류로만 채워진다는 사실을 반영한다. 일반 콤팩트 Kähler 다양체에서는 $$p \neq q$$인 칸도 비지 않으며, 그 비대각 Hodge 수가 다양체의 정칙기하적 복잡성을 잰다. 예컨대 genus $$g$$의 Riemann 곡면 ($$n = 1$$)은 $$h^{0,0} = h^{1,1} = 1$$, $$h^{1,0} = h^{0,1} = g$$로 ([§Dolbeault 코호몰로지, ⁋예시 11](/ko/math/complex_geometry/dolbeault_cohomology#ex11)), 비대각 항 $$g$$가 곡면의 위상적 복잡성을 담는다.

## Lefschetz 연산자와 hard Lefschetz 정리

Kähler 형식 $$\omega$$는 코호몰로지에 한 가지 추가 구조를 더 새긴다. Kähler 류 $$[\omega] \in H^2(X, \mathbb{R})$$와의 cup 곱이 코호몰로지에 작용하는 연산자가 되며, 이것이 Hodge 분해와 어울려 강력한 대칭을 낳는다.

<div class="definition" markdown="1">

<ins id="def12">**정의 12**</ins> 콤팩트 Kähler 다양체 $$X$$ ($$n = \dim_{\mathbb{C}} X$$)의 *Lefschetz operator<sub>Lefschetz 연산자</sub>* $$L : H^k(X, \mathbb{C}) \to H^{k+2}(X, \mathbb{C})$$를 Kähler 류와의 곱

$$
L([\alpha]) = [\omega \wedge \alpha] = [\omega] \cup [\alpha]
$$

로 정의한다. 그 $$L^2$$-수반작용소 $$\Lambda : H^k(X, \mathbb{C}) \to H^{k-2}(X, \mathbb{C})$$를 *contraction operator<sub>축약 연산자</sub>*라 한다.

</div>

연산자 $$L$$이 코호몰로지에서 잘 정의됨은 $$\omega$$가 닫힌형식이라 닫힌형식을 닫힌형식으로, 완전형식을 완전형식으로 보내기 때문이다. $$L$$은 차수를 $$2$$씩 올리며, $$\omega$$가 실 $$(1,1)$$-형식이므로 $$H^{p,q}$$를 $$H^{p+1, q+1}$$로 보내 Hodge 분해와 어울린다. 형식 수준에서 $$L$$과 $$\Lambda = L^\ast$$는 [§Kähler 다양체, ⁋정리 12](/ko/math/complex_geometry/kahler_manifolds#thm12)의 Kähler 항등식에 나온 바로 그 작용소들이며, 코호몰로지로 내려와 다음 정리를 만족한다.

<div class="proposition" markdown="1">

<ins id="thm13">**정리 13 (Hard Lefschetz 정리)**</ins> $$X$$를 콤팩트 Kähler 다양체, $$n = \dim_{\mathbb{C}} X$$라 하자. 그러면 각 $$0 \leq k \leq n$$에 대하여 $$L$$의 거듭제곱

$$
L^{n-k} : H^k(X, \mathbb{C}) \xrightarrow{\ \cong\ } H^{2n-k}(X, \mathbb{C})
$$

은 동형이다. 더 나아가 $$k$$번째 *primitive cohomology<sub>원시 코호몰로지</sub>*를 $$P^k = \ker(L^{n-k+1} : H^k \to H^{2n-k+2})$$로 두면, *Lefschetz 분해<sub>Lefschetz decomposition</sub>*

$$
H^k(X, \mathbb{C}) = \bigoplus_{j \geq 0} L^j\, P^{k-2j}
$$

이 성립한다.

</div>

이 정리는 Hodge 정리와 같은 타원작용소 이론의 산물로, $$L$$, $$\Lambda$$, 그리고 차수를 세는 작용소 $$H = [L, \Lambda]$$가 콤팩트 Kähler 다양체의 조화형식 공간 위에서 $$\mathfrak{sl}_2$$의 표현을 이룬다는 사실에서 따라온다. 그 표현론적 구조가 $$L^{n-k}$$의 동형성과 primitive 분해를 동시에 강제한다. 우리는 이 정리를 증명 없이 인용하며, 그 형식 수준의 핵심 입력인 Kähler 항등식은 [§Kähler 다양체, ⁋정리 12](/ko/math/complex_geometry/kahler_manifolds#thm12)에서 이미 확보하였다. Hard Lefschetz 정리의 한 가지 즉각적 귀결은 Betti 수의 단봉성, 곧 $$b_0 \leq b_2 \leq \cdots \leq b_{2\lfloor n/2 \rfloor}$$이며 ($$L^{n-k}$$가 단사라 $$b_k \leq b_{2n-k}$$이고 Poincaré 쌍대로 $$b_k = b_{2n-k}$$, 또 $$L$$이 $$k \leq n-1$$에서 단사라 $$b_k \leq b_{k+2}$$), 이는 콤팩트 Kähler 다양체의 Hodge 다이아몬드가 중앙으로 갈수록 넓어지는 형태임을 뜻한다. $$\mathbb{CP}^n$$의 Hodge 다이아몬드에서 $$L : H^{2p} \to H^{2p+2}$$이 $$0 \leq p \leq n-1$$에서 동형이라는 것이 그 가장 단순한 예이며 ([예시 11](#ex11)), 거기서 모든 짝수 코호몰로지가 $$[\omega^p]$$로 생성됨이 바로 $$L^p[\,1\,] = [\omega^p]$$의 비소멸로 설명된다.

---

**참고문헌**

**[Huybrechts]** D. Huybrechts, *Complex Geometry: An Introduction*, Springer, 2005.

**[Griffiths–Harris]** P. Griffiths and J. Harris, *Principles of Algebraic Geometry*, Wiley, 1978.

**[Voisin]** C. Voisin, *Hodge Theory and Complex Algebraic Geometry I*, Cambridge University Press, 2002.

**[Wells]** R. O. Wells, *Differential Analysis on Complex Manifolds*, 3rd ed., Springer, 2008.

**[Warner]** F. W. Warner, *Foundations of Differentiable Manifolds and Lie Groups*, Springer, 1983.
