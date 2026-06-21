---
title: "비교 정리"
description: "곡률과 위상·거리 사이를 잇는 두 고전적 비교 정리를 다룬다. 측지선의 변분에서 자연히 등장하는 Jacobi field와 conjugate point, 그리고 에너지의 제2변분이 정하는 index form을 도입한 뒤, Ricci curvature가 양으로 유계인 완비 manifold가 콤팩트이고 유한 fundamental group을 가진다는 Bonnet–Myers 정리와, sectional curvature가 비양인 단순연결 완비 manifold가 exponential map을 통해 유클리드 공간과 미분동형이라는 Cartan–Hadamard 정리를 증명한다."
excerpt: "Jacobi field, conjugate point, index form, Bonnet–Myers, Cartan–Hadamard"

categories: [Math / Riemannian Geometry]
permalink: /ko/math/riemannian_geometry/comparison_theorems
sidebar: 
    nav: "riemannian_geometry-ko"

date: 2026-06-21
weight: 9

published: false
---

[§리만 곡률, ⁋정의 2](/ko/math/riemannian_geometry/curvature#def2)에서 우리는 Riemannian manifold $$(M, g)$$의 곡률 텐서 $$R$$을 정의했고, [§지수사상, ⁋정리 9](/ko/math/riemannian_geometry/exponential_map#thm9)에 이르기까지 한 점 근방의 측지선이 exponential map을 통해 접공간 위로 선형화됨을 보았다. 곡률은 정의상 한 점에서의 무한소 자료이지만, 그것의 부호를 manifold 전체에서 통제하면 manifold의 *전역* 위상과 거리에 강한 제약이 걸린다. 이 글에서 다루는 두 정리가 그 전형이다. Ricci curvature가 양의 하한을 가지면 manifold는 콤팩트이고 fundamental group이 유한해지며 (Bonnet–Myers), sectional curvature가 어디서도 양이 아니면 단순연결 완비 manifold는 통째로 유클리드 공간과 미분동형이 된다 (Cartan–Hadamard). 두 정리 모두 곡률이 측지선 다발의 퍼짐을 어떻게 지배하는지를 측정하는 도구, 즉 Jacobi field와 에너지의 제2변분에서 나온다.

## 단면곡률과 Ricci curvature

곡률 텐서 $$R$$은 $$(1, 3)$$-tensor로서 정보가 많지만, 비교 정리에서 부호를 통제하는 대상은 그로부터 얻는 두 개의 스칼라·이차형식 형태의 곡률이다. 먼저 한 평면에 대응하는 단면곡률을 정의한다.

<div class="definition" markdown="1">

<ins id="def1">**정의 1**</ins> Riemannian manifold $$(M, g)$$의 점 $$p$$와 $$T_p M$$의 일차독립인 두 vector $$u, v$$에 대해, 이들이 펼치는 평면 $$\Pi = \span\{u, v\}$$의 *sectional curvature<sub>단면곡률</sub>*를

$$K(u, v) = \frac{\langle R(u, v) v,\, u\rangle}{\langle u, u\rangle \langle v, v\rangle - \langle u, v\rangle^2}$$

로 정의한다.

</div>

분모는 $$u, v$$가 펼치는 평행사변형의 넓이의 제곱으로, $$u, v$$가 일차독립일 때 양수이다. [§리만 곡률, ⁋명제 5](/ko/math/riemannian_geometry/curvature#prop5)의 대칭성을 사용하면 $$K(u, v)$$가 평면 $$\Pi$$에만 의존하고 그 안의 기저 $$\{u, v\}$$의 선택과 무관함을 확인할 수 있으므로, $$K$$를 $$2$$-평면들의 함수 $$K(\Pi)$$로 보아도 된다. 특히 $$u, v$$가 정규직교이면 분모가 $$1$$이 되어 $$K(u, v) = \langle R(u, v) v, u\rangle$$이다. $$2$$차원 manifold에서는 평면이 접공간 자신 하나뿐이므로 $$K$$가 점마다 하나의 수가 되며, 이것이 고전적인 Gauss curvature와 일치한다.

Ricci curvature는 단면곡률을 한 방향에 대해 평균낸 것으로, Bonnet–Myers에서 가정으로 쓰이는 곡률이다.

<div class="definition" markdown="1">

<ins id="def2">**정의 2**</ins> Riemannian manifold $$(M, g)$$의 점 $$p$$와 단위 vector $$v \in T_p M$$에 대해, *Ricci curvature<sub>리치 곡률</sub>* $$\operatorname{Ric}(v, v)$$를

$$\operatorname{Ric}(v, v) = \sum_{i=1}^{n-1} \langle R(e_i, v) v,\, e_i\rangle$$

로 정의한다. 여기서 $$(e_1, \ldots, e_{n-1}, v)$$는 $$T_p M$$의 정규직교기저이다.

</div>

이 합은 정규직교기저의 선택과 무관하며, $$v$$에 수직인 $$e_i$$들이 펼치는 평면들의 단면곡률의 합 $$\sum_{i=1}^{n-1} K(e_i, v)$$과 같다. 일반의 vector에 대해서는 $$\operatorname{Ric}$$을 쌍선형·대칭으로 확장하여 $$(0, 2)$$-tensor로 본다. $$\operatorname{Ric}(v, v) \ge (n-1)k$$라는 조건은 $$v$$에 수직인 $$n-1$$개 방향의 단면곡률 평균이 $$k$$ 이상이라는 뜻으로, 단면곡률을 점별로 모두 통제하는 것보다 약한 가정이다. 이 약한 가정만으로 전역 결과를 얻는 것이 Bonnet–Myers 정리의 강점이다.

## Jacobi field

비교 정리의 핵심 장치는 한 측지선을 다른 측지선들로 흔드는 변분의 변분장이다. [§측지선, ⁋정리 3](/ko/math/riemannian_geometry/geodesics#thm3)에서 곡선의 변분을 도입했는데, 변분의 각 곡선이 다시 측지선이 되도록 제한하면 변분장이 만족하는 이계 방정식을 곡률로 표현할 수 있다.

<div class="definition" markdown="1">

<ins id="def3">**정의 3**</ins> 측지선 $$\gamma : I \to M$$을 따른 vector field $$J$$가 *Jacobi equation<sub>야코비 방정식</sub>*

$$D_t^2 J + R(J, \dot\gamma)\dot\gamma = 0$$

을 모든 $$t \in I$$에서 만족할 때, $$J$$를 $$\gamma$$를 따른 *Jacobi field<sub>야코비 장</sub>*라 부른다. 여기서 $$D_t$$는 $$\gamma$$를 따른 covariant derivative이다.

</div>

Jacobi equation은 $$\gamma$$를 따른 vector field에 대한 선형 이계 상미분방정식이다. Local frame을 잡아 성분으로 풀어 쓰면 $$J$$의 성분에 대한 선형 이계 시스템이 되며, 그 계수는 $$\gamma$$를 따른 곡률 $$R(\cdot, \dot\gamma)\dot\gamma$$로 주어진다. 다음 명제는 이 방정식이 측지선의 변분에서 자연히 등장함을 보이고, 동시에 해의 존재와 유일성을 정리한다.

<div class="proposition" markdown="1">

<ins id="prop4">**명제 4**</ins> 측지선 $$\gamma : [a, b] \to M$$에 대해 다음이 성립한다.

1. 변분 $$\Gamma : (-\varepsilon, \varepsilon) \times [a, b] \to M$$의 각 곡선 $$t \mapsto \Gamma(s, t)$$가 측지선이면, 그 변분장 $$J(t) = \partial_s \Gamma\vert_{s=0}(t)$$는 $$\gamma$$를 따른 Jacobi field이다.
2. 임의의 $$t_0 \in [a, b]$$와 두 vector $$u, w \in T_{\gamma(t_0)} M$$에 대해, $$J(t_0) = u$$, $$D_t J(t_0) = w$$를 만족하는 Jacobi field $$J$$가 $$[a, b]$$ 위에서 유일하게 존재한다. 따라서 $$\gamma$$를 따른 Jacobi field들은 $$2n$$차원 vector space를 이룬다.

</div>

<details class="proof" markdown="1">
<summary>증명</summary>

(1) $$\Gamma$$의 각 곡선이 측지선이므로 $$D_t \partial_t \Gamma = 0$$이 모든 $$(s, t)$$에서 성립한다. 양변에 $$D_s$$를 적용하면 $$D_s D_t \partial_t \Gamma = 0$$이다. 곡률의 정의 [§리만 곡률, ⁋정의 2](/ko/math/riemannian_geometry/curvature#def2)를 곡선을 따른 covariant derivative에 적용한 교환관계

$$D_s D_t X - D_t D_s X = R(\partial_s \Gamma,\, \partial_t \Gamma)\, X$$

를 $$X = \partial_t \Gamma$$에 쓰면

$$D_s D_t \partial_t \Gamma = D_t D_s \partial_t \Gamma + R(\partial_s \Gamma, \partial_t \Gamma)\, \partial_t \Gamma$$

이다. 좌변이 $$0$$이고, [§측지선, ⁋정리 3](/ko/math/riemannian_geometry/geodesics#thm3)의 증명에서 쓴 대칭 보조정리 $$D_s \partial_t \Gamma = D_t \partial_s \Gamma$$에 의해 $$D_s \partial_t \Gamma = D_t \partial_s \Gamma$$이므로

$$0 = D_t D_t \partial_s \Gamma + R(\partial_s \Gamma, \partial_t \Gamma)\, \partial_t \Gamma$$

가 된다. $$s = 0$$에서 평가하면 $$\partial_s \Gamma\vert_{s=0} = J$$, $$\partial_t \Gamma\vert_{s=0} = \dot\gamma$$이므로

$$D_t^2 J + R(J, \dot\gamma)\dot\gamma = 0$$

을 얻어 $$J$$는 Jacobi field이다.

(2) $$\gamma$$를 따라 parallel orthonormal frame $$(E_1, \ldots, E_n)$$을 잡고 $$J = \sum_i J^i E_i$$로 쓰면, $$E_i$$들이 평행이므로 $$D_t^2 J = \sum_i \ddot J^i E_i$$이고, $$R(J, \dot\gamma)\dot\gamma = \sum_{i, j} J^j \langle R(E_j, \dot\gamma)\dot\gamma, E_i\rangle E_i$$이다. 따라서 Jacobi equation은

$$\ddot J^i(t) + \sum_{j} a^i_j(t)\, J^j(t) = 0, \qquad a^i_j(t) = \langle R(E_j, \dot\gamma)\dot\gamma, E_i\rangle$$

라는 선형 이계 상미분방정식 시스템이 되며, 그 계수 $$a^i_j$$는 $$t$$에 대해 매끄럽다. 선형 상미분방정식의 표준 이론에 의해 초기조건 $$J^i(t_0)$$, $$\dot J^i(t_0)$$를 주면 해가 $$[a, b]$$ 전체에서 유일하게 존재하며, 초기자료 $$(J(t_0), D_t J(t_0)) \in T_{\gamma(t_0)} M \times T_{\gamma(t_0)} M$$이 $$2n$$차원을 이루므로 Jacobi field들의 공간도 $$2n$$차원이다.

</details>

[명제 4](#prop4)는 Jacobi field를 "이웃한 측지선들이 $$\gamma$$로부터 무한소로 벌어지는 속도"로 해석하게 한다. 곡률이 이 벌어짐을 통제하는 방식이 Jacobi equation에 직접 나타난다. $$R(J, \dot\gamma)\dot\gamma$$의 부호가 음이면 (단면곡률이 음이면) 방정식은 $$\ddot J = (\text{양})\, J$$ 꼴이 되어 해가 지수적으로 발산하므로 측지선들이 빠르게 벌어지고, 부호가 양이면 (단면곡률이 양이면) $$\ddot J = -(\text{양})\, J$$ 꼴의 진동 방정식이 되어 벌어졌던 측지선들이 다시 모인다. 이 두 양상이 각각 Cartan–Hadamard와 Bonnet–Myers의 기하학적 뿌리이다.

측지선을 따라 두 점에서 변분장이 동시에 소멸하는 비자명한 Jacobi field가 있으면, 그 두 점은 측지선을 따라 이웃 측지선들이 다시 한 점으로 모이는 위치이다. 이를 다음과 같이 부른다.

<div class="definition" markdown="1">

<ins id="def5">**정의 5**</ins> 측지선 $$\gamma : [a, b] \to M$$ 위의 두 점 $$\gamma(t_0)$$, $$\gamma(t_1)$$ ($$t_0 < t_1$$)에 대해, $$J(t_0) = 0$$이고 $$J(t_1) = 0$$이면서 $$J \not\equiv 0$$인 Jacobi field $$J$$가 존재하면, $$\gamma(t_1)$$을 $$\gamma(t_0)$$을 따른 *conjugate point<sub>켤레점</sub>*라 부른다.

</div>

$$J(t_0) = 0$$인 Jacobi field는 정확히 $$\gamma(t_0)$$에서 출발하는 측지선들의 변분의 변분장이며, 이런 $$J$$가 $$t_1$$에서 다시 소멸한다는 것은 $$\gamma(t_0)$$에서 나온 측지선 다발이 무한소적으로 $$\gamma(t_1)$$에서 재초점됨을 뜻한다. Conjugate point는 또한 exponential map의 임계점과 정확히 대응한다. $$\gamma(t) = \exp_p(t v)$$ ($$p = \gamma(0)$$, $$v = \dot\gamma(0)$$) 꼴로 쓰면, $$J(0) = 0$$인 Jacobi field는 $$J(t) = (d\exp_p)_{tv}(t\, w)$$ 형태이고 ([§지수사상, ⁋보조정리 8](/ko/math/riemannian_geometry/exponential_map#lem8)의 변분장 계산과 같은 형태이다), 따라서 $$\gamma(t_1)$$이 conjugate point인 것은 $$(d\exp_p)_{t_1 v}$$가 비가역, 즉 $$t_1 v$$가 $$\exp_p$$의 임계점인 것과 동치이다. 이 동치성이 Cartan–Hadamard 증명에서 결정적으로 쓰인다.

## Index form과 에너지의 제2변분

측지선이 길이 또는 에너지를 *최소화*하는지를 판정하려면 [§측지선, ⁋정리 3](/ko/math/riemannian_geometry/geodesics#thm3)의 제1변분만으로는 부족하고, 임계점에서의 이차 거동, 즉 제2변분을 보아야 한다. 그 이차형식이 index form이다. 먼저 그것을 정의한다.

측지선 $$\gamma : [a, b] \to M$$에 대해, $$\gamma$$를 따른 vector field 중 양 끝에서 소멸하고 ($$V(a) = V(b) = 0$$) 조각마다 매끄러운 것들의 공간을 생각하자. 그 위에서 다음 대칭 쌍선형형식을 정의한다.

<div class="definition" markdown="1">

<ins id="def6">**정의 6**</ins> 측지선 $$\gamma : [a, b] \to M$$과 양 끝에서 소멸하는 $$\gamma$$를 따른 vector field $$V, W$$에 대해, *index form<sub>지표형식</sub>* $$I(V, W)$$를

$$I(V, W) = \int_a^b \Bigl( \langle D_t V,\, D_t W\rangle - \langle R(V, \dot\gamma)\dot\gamma,\, W\rangle \Bigr) \mathop{dt}$$

로 정의한다.

</div>

Index form이 측지선의 최소화 성질을 판정하는 도구임은 다음 제2변분 공식에서 드러난다. $$\gamma$$의 고정변분 $$\Gamma$$의 변분장이 $$V$$일 때, 에너지 $$E(s) = E(\gamma_s)$$의 $$s = 0$$에서의 이차도함수가 정확히 $$I(V, V)$$로 주어진다.

<div class="proposition" markdown="1">

<ins id="prop7">**명제 7 (에너지의 제2변분)**</ins> 측지선 $$\gamma : [a, b] \to M$$의 고정변분 $$\Gamma$$의 변분장을 $$V$$라 하자. 그럼

$$\left.\frac{d^2}{ds^2}\right\vert_{s=0} E(\gamma_s) = I(V, V) = \int_a^b \Bigl( \lVert D_t V\rVert^2 - \langle R(V, \dot\gamma)\dot\gamma,\, V\rangle \Bigr) \mathop{dt}$$

이 성립한다.

</div>

<details class="proof" markdown="1">
<summary>증명</summary>

[§측지선, ⁋정리 3](/ko/math/riemannian_geometry/geodesics#thm3)의 증명에서 $$\frac{d}{ds} E(\gamma_s) = \int_a^b \langle D_s \partial_t \Gamma, \partial_t \Gamma\rangle \mathop{dt}$$임을 보였다. 다시 $$s$$에 대해 미분하면 metric-compatibility에 의해

$$\frac{d^2}{ds^2} E(\gamma_s) = \int_a^b \Bigl( \langle D_s D_s \partial_t \Gamma,\, \partial_t \Gamma\rangle + \langle D_s \partial_t \Gamma,\, D_s \partial_t \Gamma\rangle \Bigr) \mathop{dt}$$

이다. 둘째 피적분항에 대칭 보조정리 $$D_s \partial_t \Gamma = D_t \partial_s \Gamma$$를 쓰면 $$\langle D_t \partial_s \Gamma, D_t \partial_s \Gamma\rangle$$이다. 첫째 항은 곡률 교환관계 $$D_s D_t \partial_s \Gamma = D_t D_s \partial_s \Gamma + R(\partial_s \Gamma, \partial_t \Gamma)\partial_s \Gamma$$를 사용하여

$$D_s D_s \partial_t \Gamma = D_s D_t \partial_s \Gamma = D_t D_s \partial_s \Gamma + R(\partial_s \Gamma, \partial_t \Gamma)\, \partial_s \Gamma$$

로 바꾼다. 이제 $$s = 0$$에서 평가하자. 변분이 고정변분이고 $$\gamma$$가 측지선이므로 $$\partial_t \Gamma\vert_{s=0} = \dot\gamma$$, $$\partial_s \Gamma\vert_{s=0} = V$$이다. 첫째 항의 $$D_t D_s \partial_s \Gamma$$ 부분은 metric-compatibility에 의해

$$\int_a^b \langle D_t D_s \partial_s \Gamma,\, \dot\gamma\rangle \mathop{dt} = \Bigl[\langle D_s \partial_s \Gamma,\, \dot\gamma\rangle\Bigr]_a^b - \int_a^b \langle D_s \partial_s \Gamma,\, D_t \dot\gamma\rangle \mathop{dt}$$

인데, $$\gamma$$가 측지선이라 $$D_t \dot\gamma = 0$$이고, 경계항은 $$\Gamma$$가 고정변분이라 각 $$s$$에서 $$\Gamma(s, a), \Gamma(s, b)$$가 상수이므로 $$\partial_s \Gamma(s, a) = \partial_s \Gamma(s, b) = 0$$이 되어 모두 소멸한다. 따라서 그 부분은 $$0$$이다. 남은 항을 모으면

$$\left.\frac{d^2}{ds^2}\right\vert_{s=0} E(\gamma_s) = \int_a^b \Bigl( \langle R(V, \dot\gamma)V,\, \dot\gamma\rangle + \lVert D_t V\rVert^2 \Bigr) \mathop{dt}$$

이 되는데, $$\langle R(V, \dot\gamma)V \cdots\rangle$$ 항의 부호를 [§리만 곡률, ⁋명제 5](/ko/math/riemannian_geometry/curvature#prop5)의 대칭성으로 정리하면 $$\langle R(V, \dot\gamma)\dot\gamma, V\rangle$$의 부호는 음이 되어

$$\left.\frac{d^2}{ds^2}\right\vert_{s=0} E(\gamma_s) = \int_a^b \Bigl( \lVert D_t V\rVert^2 - \langle R(V, \dot\gamma)\dot\gamma,\, V\rangle \Bigr) \mathop{dt} = I(V, V)$$

를 얻는다.

</details>

[명제 7](#prop7)에 따라, 측지선 $$\gamma$$가 에너지를 (따라서 충분히 가까운 곡선들 사이에서 길이를) 국소적으로 최소화하려면 모든 고정변분장 $$V$$에 대해 $$I(V, V) \ge 0$$이어야 한다. 거꾸로 어떤 $$V$$에서 $$I(V, V) < 0$$이면 그 방향으로 흔들어 더 짧은 곡선을 얻을 수 있으므로 $$\gamma$$는 최소화 곡선이 아니다. Index form의 부호를 곡률의 부호로 통제하는 것이 두 비교 정리의 공통 전략이다.

Index form의 부분적분 형태도 자주 쓰인다. 양 끝에서 소멸하는 매끄러운 $$V, W$$에 대해 $$\langle D_t V, D_t W\rangle$$를 부분적분하면

$$I(V, W) = -\int_a^b \langle D_t^2 V + R(V, \dot\gamma)\dot\gamma,\, W\rangle \mathop{dt}$$

이고, 따라서 $$I(V, W) = 0$$이 모든 $$W$$에 대해 성립하는 것은 $$V$$가 양 끝에서 소멸하는 Jacobi field인 것과 동치이다. 이는 index form의 퇴화 방향이 정확히 conjugate point에서 나오는 Jacobi field임을 말하며, conjugate point 너머에서 측지선이 더 이상 최소화하지 못한다는 사실의 근거가 된다.

## Bonnet–Myers 정리

이제 첫 비교 정리를 증명한다. Ricci curvature가 양의 하한을 가지면 측지선을 일정 길이 이상 늘릴 수 없다는 것이 핵심이다. 길이가 그 한계를 넘으면 index form이 음의 값을 가져 측지선이 최소화 곡선이기를 멈추기 때문이다.

<div class="proposition" markdown="1">

<ins id="thm8">**정리 8 (Bonnet–Myers)**</ins> $$(M, g)$$가 $$n$$차원 complete Riemannian manifold이고, 어떤 상수 $$k > 0$$에 대해 모든 단위 vector $$v$$에서

$$\operatorname{Ric}(v, v) \ge (n-1)k$$

가 성립한다고 하자. 그럼 $$M$$의 임의의 두 점 사이의 거리는 $$\pi/\sqrt{k}$$ 이하이다. 즉 $$\operatorname{diam}(M) \le \pi/\sqrt{k}$$이며, 따라서 $$M$$은 콤팩트하다.

</div>

<details class="proof" markdown="1">
<summary>증명</summary>

두 점 $$p, q \in M$$를 잡고 $$L := d(p, q)$$라 하자. $$M$$이 complete이므로 Hopf-Rinow 정리에 의해 $$p$$에서 $$q$$로 가는, 호의 길이로 매개화된 최소화 측지선 $$\gamma : [0, L] \to M$$이 존재한다 ($$\lVert \dot\gamma\rVert \equiv 1$$). $$L > \pi/\sqrt{k}$$라 가정하고 모순을 이끈다.

$$\gamma$$를 따라 $$\dot\gamma$$에 수직인 parallel orthonormal frame $$(E_1, \ldots, E_{n-1}, E_n = \dot\gamma)$$을 잡는다 ([§리만 곡률, ⁋정의 2](/ko/math/riemannian_geometry/curvature#def2) 이전에 쓴 parallel transport로 $$T_p M$$의 정규직교기저를 운반한 것이며, 측지선의 속도가 평행이라 직교성과 정규성이 보존된다). 각 $$i = 1, \ldots, n-1$$에 대해 양 끝에서 소멸하는 vector field

$$V_i(t) := \sin\!\Bigl(\frac{\pi t}{L}\Bigr)\, E_i(t)$$

를 놓자. $$E_i$$가 평행이므로 $$D_t V_i = \frac{\pi}{L}\cos(\frac{\pi t}{L})\, E_i$$이고, [명제 7](#prop7)의 index form은

$$I(V_i, V_i) = \int_0^L \Bigl( \frac{\pi^2}{L^2}\cos^2\!\frac{\pi t}{L} - \sin^2\!\frac{\pi t}{L}\,\langle R(E_i, \dot\gamma)\dot\gamma, E_i\rangle \Bigr) \mathop{dt}$$

이다. 이제 $$i$$에 대해 합하면, $$\sum_{i=1}^{n-1}\langle R(E_i, \dot\gamma)\dot\gamma, E_i\rangle = \operatorname{Ric}(\dot\gamma, \dot\gamma) \ge (n-1)k$$이므로

$$\sum_{i=1}^{n-1} I(V_i, V_i) \le \int_0^L \Bigl( (n-1)\frac{\pi^2}{L^2}\cos^2\!\frac{\pi t}{L} - (n-1)k\, \sin^2\!\frac{\pi t}{L} \Bigr) \mathop{dt} = (n-1)\int_0^L \Bigl( \frac{\pi^2}{L^2}\cos^2\!\frac{\pi t}{L} - k\sin^2\!\frac{\pi t}{L} \Bigr) \mathop{dt}$$

이다. $$\int_0^L \cos^2(\pi t/L)\mathop{dt} = \int_0^L \sin^2(\pi t/L)\mathop{dt} = L/2$$이므로 우변은

$$(n-1)\,\frac{L}{2}\Bigl( \frac{\pi^2}{L^2} - k \Bigr)$$

이다. 가정 $$L > \pi/\sqrt{k}$$는 $$\pi^2/L^2 < k$$를 뜻하므로 이 값은 음수이고, 따라서 적어도 하나의 $$i$$에서 $$I(V_i, V_i) < 0$$이다. [명제 7](#prop7)에 의해 변분장 $$V_i$$를 갖는 고정변분을 따라 흔들면 에너지가 (따라서 길이가) $$\gamma$$보다 작은 곡선이 존재하므로, $$\gamma$$는 $$p$$와 $$q$$ 사이의 최소화 곡선이 아니다. 이는 $$\gamma$$가 최소화 측지선이라는 데 모순이다. 따라서 $$L \le \pi/\sqrt{k}$$이다.

$$p, q$$가 임의였으므로 $$\operatorname{diam}(M) \le \pi/\sqrt{k} < \infty$$이다. Complete이고 거리유계인 manifold는 Hopf-Rinow 정리에 의해 닫힌 거리유계 집합이 콤팩트이므로 $$M = \bar B(p, \pi/\sqrt{k})$$ 자신이 콤팩트하다.

</details>

Bonnet–Myers 정리에서 직경의 상한 $$\pi/\sqrt{k}$$는 sharp이다. 반지름 $$1/\sqrt{k}$$의 둥근 구면 $$S^n$$은 모든 단면곡률이 $$k$$이므로 $$\operatorname{Ric} = (n-1)k$$를 등호로 만족하고, 그 직경이 정확히 $$\pi/\sqrt{k}$$이다. 콤팩트성으로부터 fundamental group에 대한 다음 결과가 곧바로 따라온다.

<div class="proposition" markdown="1">

<ins id="cor9">**따름정리 9**</ins> [정리 8](#thm8)의 가정 아래에서 $$M$$의 fundamental group $$\pi_1(M)$$은 유한군이다.

</div>

<details class="proof" markdown="1">
<summary>증명</summary>

$$M$$의 universal cover $$\pi : \tilde M \to M$$를 생각하자. $$\tilde M$$에 $$g$$를 끌어올린 metric $$\tilde g = \pi^\ast g$$를 주면 $$\pi$$는 국소등거리사상이고, 따라서 $$(\tilde M, \tilde g)$$의 곡률은 $$(M, g)$$의 곡률을 국소적으로 그대로 가지므로 $$\tilde M$$도 같은 Ricci 하한 $$\operatorname{Ric} \ge (n-1)k$$를 만족한다. 또한 콤팩트 manifold $$M$$은 complete이고, 그 universal cover $$\tilde M$$ 역시 끌어올린 metric에 대해 complete이다 (덮개사상을 따라 측지선이 들어올려지므로). 그럼 [정리 8](#thm8)을 $$(\tilde M, \tilde g)$$에 적용하여 $$\tilde M$$도 콤팩트하다.

한편 $$\pi : \tilde M \to M$$의 각 fiber $$\pi^{-1}(p)$$는 deck transformation group과 전단사이고, universal cover의 경우 이 group이 $$\pi_1(M)$$과 동형이다. $$\tilde M$$이 콤팩트하고 $$\pi$$가 덮개사상이므로 fiber $$\pi^{-1}(p)$$는 이산이며 콤팩트집합 $$\tilde M$$ 안에서 닫힌 이산집합, 즉 유한집합이다. 따라서 $$\pi_1(M) \cong \pi^{-1}(p)$$는 유한군이다.

</details>

[따름정리 9](#cor9)는 양의 Ricci curvature가 위상에 거는 제약을 잘 보여준다. 예컨대 $$\mathbb{R}^n$$이나 평탄 토러스 $$T^n$$, 또는 무한 fundamental group을 가진 어떤 manifold도 양의 하한을 갖는 Ricci curvature를 허용할 수 없다. 특히 $$\pi_1$$이 무한인 콤팩트 manifold는 양의 Ricci metric을 가질 수 없다.

## Cartan–Hadamard 정리

반대쪽 부호, 즉 단면곡률이 어디서도 양이 아닌 경우를 다룬다. 이때는 Jacobi field가 발산만 할 뿐 다시 소멸하지 못하므로 conjugate point가 없고, 그 결과 exponential map이 어디서도 임계점을 갖지 않아 전역 미분동형이 된다. 먼저 conjugate point의 부재를 보인다.

<div class="proposition" markdown="1">

<ins id="lem10">**보조정리 10**</ins> $$(M, g)$$의 모든 단면곡률이 $$K \le 0$$이라 하자. 그럼 임의의 측지선 $$\gamma$$ 위에는 conjugate point가 없다. 동치로, $$p \in M$$의 임의의 점에서 $$\exp_p$$는 정의역의 모든 점에서 비특이 (미분이 가역) 이다.

</div>

<details class="proof" markdown="1">
<summary>증명</summary>

측지선 $$\gamma$$를 따른 Jacobi field $$J$$로 $$J(t_0) = 0$$이고 $$J \not\equiv 0$$인 것을 잡고, $$f(t) := \langle J(t), J(t)\rangle$$을 보자. Metric-compatibility로

$$f'(t) = 2\langle D_t J, J\rangle, \qquad f''(t) = 2\langle D_t^2 J, J\rangle + 2\langle D_t J, D_t J\rangle$$

이고, Jacobi equation $$D_t^2 J = -R(J, \dot\gamma)\dot\gamma$$를 대입하면

$$f''(t) = 2\lVert D_t J\rVert^2 - 2\langle R(J, \dot\gamma)\dot\gamma,\, J\rangle$$

이다. $$J$$가 $$\dot\gamma$$에 수직인 부분만 따져도 되는데 (Jacobi equation은 $$\dot\gamma$$ 방향 성분과 수직 성분으로 분해되고 $$\dot\gamma$$ 방향 성분은 conjugate point를 만들지 않는다), 수직인 $$J$$에 대해 단면곡률의 정의 [정의 1](#def1)에서

$$\langle R(J, \dot\gamma)\dot\gamma,\, J\rangle = K(J, \dot\gamma)\,\bigl(\lVert J\rVert^2 \lVert\dot\gamma\rVert^2 - \langle J, \dot\gamma\rangle^2\bigr) = K(J, \dot\gamma)\,\lVert J\rVert^2 \lVert\dot\gamma\rVert^2 \le 0$$

이다 ($$K \le 0$$이고 $$\langle J, \dot\gamma\rangle = 0$$이므로). 따라서

$$f''(t) = 2\lVert D_t J\rVert^2 - 2\langle R(J, \dot\gamma)\dot\gamma, J\rangle \ge 0$$

이 되어 $$f$$는 볼록함수이다. $$J \not\equiv 0$$이고 $$J(t_0) = 0$$이므로 $$D_t J(t_0) \ne 0$$이고 (그렇지 않으면 [명제 4](#prop4)의 유일성에 의해 $$J \equiv 0$$), 따라서 $$f(t_0) = 0$$, $$f'(t_0) = 0$$, 그리고 $$f''(t_0) = 2\lVert D_t J(t_0)\rVert^2 > 0$$이다. 볼록이고 $$t_0$$에서 최솟값 $$0$$을 갖는 $$f$$는 $$t > t_0$$에서 $$f(t) > 0$$, 즉 $$J(t) \ne 0$$이다. 그러므로 $$J$$는 $$t_0$$ 이후 다시 소멸하지 않으며 conjugate point가 없다.

Conjugate point가 없다는 것은 [정의 5](#def5) 다음 문단에서 본 동치성에 의해 $$(d\exp_p)_{tv}$$가 모든 $$tv$$에서 가역, 즉 $$\exp_p$$가 정의역 전체에서 비특이임과 같다.

</details>

이제 단면곡률이 비양인 완비 단순연결 manifold의 전역 구조를 결정한다. $$\exp_p$$가 비특이일 뿐 아니라 전역 미분동형임을 보이는 것이 관건이며, 단순연결성이 그 도약을 가능하게 한다.

<div class="proposition" markdown="1">

<ins id="thm11">**정리 11 (Cartan–Hadamard)**</ins> $$(M, g)$$가 $$n$$차원 complete, 단순연결 Riemannian manifold이고 모든 단면곡률이 $$K \le 0$$이라 하자. 그럼 임의의 점 $$p \in M$$에서 exponential map

$$\exp_p : T_p M \to M$$

은 미분동형이다. 특히 $$M$$은 $$\mathbb{R}^n$$과 미분동형이고, $$M$$의 임의의 두 점은 유일한 측지선으로 이어지며 그 측지선이 최단 곡선이다.

</div>

<details class="proof" markdown="1">
<summary>증명</summary>

$$M$$이 complete이므로 Hopf-Rinow 정리에 의해 모든 측지선이 $$\mathbb{R}$$ 전체로 연장되어 $$\exp_p$$가 $$T_p M$$ 전체에서 정의된다. [보조정리 10](#lem10)에 의해 $$\exp_p$$는 모든 점에서 비특이이므로 국소 미분동형이다.

핵심은 $$\exp_p$$를 통해 $$T_p M$$ 위로 끌어올린 metric $$\tilde g := \exp_p^\ast g$$가 complete임을 보이는 것이다. $$\exp_p$$가 국소 미분동형이므로 $$\tilde g$$는 $$T_p M$$ 위의 매끄러운 Riemannian metric이고, $$\exp_p : (T_p M, \tilde g) \to (M, g)$$는 국소등거리사상이다. $$(T_p M, \tilde g)$$에서 원점을 지나는 직선 $$t \mapsto tv$$는 $$\exp_p$$ 아래에서 측지선 $$\gamma_v(t) = \exp_p(tv)$$로 보내지므로 ([§지수사상, ⁋보조정리 2](/ko/math/riemannian_geometry/exponential_map#lem2)) 이 직선들은 $$\tilde g$$의 측지선이며, 이들이 원점에서 모든 방향으로 모든 시간에 정의되므로 $$(T_p M, \tilde g)$$는 원점에서 geodesically complete이다. Hopf-Rinow 정리는 한 점에서의 geodesic completeness로부터 전체의 completeness를 주므로 $$(T_p M, \tilde g)$$는 complete이다.

이제 국소등거리사상이자 국소 미분동형인 $$\exp_p$$가 출발공간이 complete이고 도착공간이 연결일 때 덮개사상임을 쓴다 (완비 manifold 사이의 국소등거리 surjection은 덮개사상이라는 사실의 적용이며, surjectivity는 Hopf-Rinow에서 $$\exp_p$$의 상이 닫혀 있고 열려 있어 연결인 $$M$$ 전체가 되는 데서 나온다). 따라서 $$\exp_p : T_p M \to M$$은 덮개사상이다. $$T_p M \cong \mathbb{R}^n$$은 단순연결이므로 universal cover이고, $$M$$이 단순연결이라는 가정에서 덮개사상 $$\exp_p$$는 한 겹, 즉 미분동형이다.

$$\exp_p$$가 전단사이므로 임의의 $$q \in M$$에 대해 $$q = \exp_p(v)$$인 $$v$$가 유일하게 존재하고, 그 측지선 $$\gamma_v$$가 $$p$$와 $$q$$를 잇는 유일한 측지선이다. [§지수사상, ⁋정리 9](/ko/math/riemannian_geometry/exponential_map#thm9)의 Gauss lemma가 함의하듯 $$\exp_p$$가 미분동형인 영역에서 방사 측지선은 길이를 최소화하므로, 이 유일한 측지선이 $$p$$와 $$q$$ 사이의 최단 곡선이다.

</details>

[정리 11](#thm11)은 단면곡률이 비양인 단순연결 완비 manifold가 위상적으로 가장 단순한 manifold, 즉 $$\mathbb{R}^n$$임을 말한다. 이런 manifold를 *Cartan–Hadamard manifold*라 부르며, 유클리드 공간 $$\mathbb{R}^n$$ ($$K \equiv 0$$)과 hyperbolic space $$\mathbb{H}^n$$ ($$K \equiv -1$$)이 대표적인 예이다. 두 정리를 나란히 놓으면 곡률의 부호가 전역 위상에 미치는 영향이 선명하다. Ricci curvature의 양의 하한은 manifold를 콤팩트하게 닫아 fundamental group을 유한하게 만들고, 단면곡률의 비양성은 단순연결인 경우 manifold를 콤팩트성과 정반대인 $$\mathbb{R}^n$$으로 완전히 펼친다. 단면곡률의 부호가 [명제 4](#prop4) 뒤에서 본 Jacobi field의 수렴·발산 양상을 통해 측지선 다발의 거동을 지배하고, 그 거동이 다시 전역 구조로 번역되는 것이다.

---

**참고문헌**

**[dC]** Manfredo P. do Carmo, *Riemannian Geometry*, Birkhäuser, 1992.

**[CE]** Jeff Cheeger, David G. Ebin, *Comparison Theorems in Riemannian Geometry*, North-Holland, 1975.

**[Lee]** John M. Lee, *Introduction to Riemannian Manifolds*, Graduate Texts in Mathematics, Springer, 2019.

---
