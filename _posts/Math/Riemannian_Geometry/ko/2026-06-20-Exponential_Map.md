---
title: "지수사상"
description: "측지선의 자료를 한 점의 접공간 위로 모으는 exponential map을 도입한다. 측지선의 초기조건에 대한 매끄러운 의존성과 동차성으로부터 exponential map이 0의 star-shaped 근방에서 매끄러움을 보이고, 0에서의 미분이 항등사상임을 계산하여 역함수 정리로 normal neighborhood와 normal coordinate를 얻는다. Normal coordinate에서 metric과 Christoffel 기호의 값, Gauss lemma, 그리고 유클리드 공간과 구면에서의 예시를 다룬다."
excerpt: "측지선을 한 점의 접공간 위로 모으는 exponential map과 normal coordinate, 그리고 Gauss lemma"

categories: [Math / Riemannian Geometry]
permalink: /ko/math/riemannian_geometry/exponential_map
sidebar: 
    nav: "riemannian_geometry-ko"

date: 2026-06-20
weight: 6
published: false

---

[§측지선, ⁋정리 7](/ko/math/riemannian_geometry/geodesics#thm7)에서 우리는 Riemannian manifold $$(M, g)$$의 각 점 $$p$$와 vector $$v \in T_p M$$마다 초기조건 $$\gamma(0) = p$$, $$\dot\gamma(0) = v$$를 만족하는 측지선이 국소적으로 유일하게 존재함을 보았다. 이 측지선을 $$\gamma_v$$로 적기로 하자. 같은 글의 [§측지선, ⁋참고 10](/ko/math/riemannian_geometry/geodesics#rmk10)에서 예고했듯, 대응 $$v \mapsto \gamma_v(1)$$은 한 점의 접공간 위로 측지선의 자료를 모아 manifold의 국소 구조를 선형화하는 도구가 된다. 이 글에서는 이 대응, 즉 *exponential map*을 정식으로 도입하고, 그것이 매끄러운 국소 미분동형임을 보인 뒤, 이로부터 얻는 normal coordinate와 Gauss lemma를 다룬다.

## Exponential map의 정의

측지선은 그 정의역이 항상 $$\mathbb{R}$$ 전체일 필요가 없으므로, exponential map은 $$T_p M$$ 전체가 아니라 $$0$$의 적당한 근방 위에서만 정의된다. 다음 정의에서 그 정의역을 명시한다.

<div class="definition" markdown="1">

<ins id="def1">**정의 1**</ins> Riemannian manifold $$(M, g)$$의 점 $$p \in M$$에 대해, 집합

$$\mathcal{E}_p = \{v \in T_p M \mid \gamma_v \text{ is defined on an interval containing } [0, 1]\}$$

위에서 정의되는 *exponential map<sub>지수사상</sub>* $$\exp_p : \mathcal{E}_p \to M$$을

$$\exp_p(v) = \gamma_v(1)$$

로 정의한다. 여기서 $$\gamma_v$$는 [§측지선, ⁋정리 7](/ko/math/riemannian_geometry/geodesics#thm7)의 초기조건 $$\gamma_v(0) = p$$, $$\dot\gamma_v(0) = v$$를 만족하는 유일한 측지선이다.

</div>

$$v = 0$$에 대응하는 측지선은 상수곡선 $$\gamma_0(t) \equiv p$$이므로 $$0 \in \mathcal{E}_p$$이며 $$\exp_p(0) = p$$이다. Exponential map의 정의역 $$\mathcal{E}_p$$가 $$0$$의 한 근방을 포함한다는 사실과 그 위에서 $$\exp_p$$가 매끄럽다는 사실은 다음 절에서 측지선이 초기조건에 매끄럽게 의존한다는 성질로부터 보일 것이다. 정의에 앞서, exponential map이 어떻게 측지선 전체의 자료를 담는지를 보이는 동차성을 정리해 둔다.

다음 보조정리는 측지선을 정의하는 방정식이 매개변수 $$t$$의 일차 재척도에 대해 가지는 동차성<sub>homogeneity</sub>을 표현한다. 직관적으로, 초기속도를 $$s$$배 늘리면 같은 자취를 $$s$$배 빠르게 지나가는 측지선을 얻는다.

<div class="proposition" markdown="1">

<ins id="lem2">**보조정리 2**</ins> Riemannian manifold $$(M, g)$$의 점 $$p$$, vector $$v \in T_p M$$, 그리고 실수 $$s > 0$$에 대해, $$\gamma_v$$가 $$t = s$$에서 정의되면 $$\gamma_{sv}$$는 $$t = 1$$에서 정의되고

$$\gamma_{sv}(t) = \gamma_v(st)$$

가 두 측지선이 모두 정의되는 모든 $$t$$에서 성립한다. 특히 $$\exp_p(sv) = \gamma_v(s)$$이다.

</div>

<details class="proof" markdown="1">
<summary>증명</summary>

곡선 $$\sigma(t) := \gamma_v(st)$$를 정의하자. 연쇄법칙에 의해 $$\dot\sigma(t) = s\, \dot\gamma_v(st)$$이고, 곡선을 따른 covariant derivative에 대해 다시 연쇄법칙을 적용하면

$$D_t \dot\sigma(t) = D_t\bigl(s\, \dot\gamma_v(st)\bigr) = s^2\, (D_t \dot\gamma_v)(st)$$

이다. $$\gamma_v$$가 측지선이므로 $$D_t \dot\gamma_v \equiv 0$$이고, 따라서 $$D_t \dot\sigma \equiv 0$$이 되어 $$\sigma$$도 측지선이다. 또한 $$\sigma(0) = \gamma_v(0) = p$$이고 $$\dot\sigma(0) = s\, \dot\gamma_v(0) = sv$$이므로, $$\sigma$$는 초기조건 $$\sigma(0) = p$$, $$\dot\sigma(0) = sv$$를 만족하는 측지선이다. [§측지선, ⁋정리 7](/ko/math/riemannian_geometry/geodesics#thm7)의 유일성에 의해 $$\sigma = \gamma_{sv}$$이고, 따라서 $$\gamma_{sv}(t) = \gamma_v(st)$$이다. 여기에 $$t = 1$$을 대입하면 $$\exp_p(sv) = \gamma_{sv}(1) = \gamma_v(s)$$를 얻는다.

</details>

[보조정리 2](#lem2)는 한 vector $$v$$를 따르는 반직선 $$s \mapsto sv$$가 exponential map 아래에서 측지선 $$s \mapsto \gamma_v(s)$$로 보내짐을 말해 준다. 즉 exponential map은 $$T_p M$$의 원점을 지나는 직선들을 $$p$$를 지나는 측지선들로 옮기며, 이것이 exponential map이 $$p$$ 근방의 기하를 그 접공간 위로 끌어올리는 방식이다.

## 매끄러움과 0에서의 미분

Exponential map이 $$0$$의 근방에서 정의되고 매끄럽다는 사실은 상미분방정식 해의 초기조건에 대한 매끄러운 의존성에서 나온다. [§측지선, ⁋정리 7](/ko/math/riemannian_geometry/geodesics#thm7)의 증명에서 측지선 방정식은 $$TM$$ 위의 일계 상미분방정식 시스템으로 환원되었으며, 그 우변이 $$(\gamma, w)$$에 매끄럽게 의존하므로, 상미분방정식의 표준적 정리에 의해 그 흐름은 시간과 초기조건 모두에 매끄럽게 의존한다. 이를 exponential map에 적용한다.

<div class="proposition" markdown="1">

<ins id="prop3">**명제 3**</ins> Riemannian manifold $$(M, g)$$의 점 $$p$$에 대해, $$0 \in T_p M$$의 적당한 열린근방 $$V \subseteq \mathcal{E}_p$$가 존재하여 $$\exp_p : V \to M$$이 매끄럽다. 더욱이 $$V$$를 $$0$$에 대해 *star-shaped*인 것으로, 즉 $$v \in V$$이면 모든 $$0 \le s \le 1$$에 대해 $$sv \in V$$이도록 택할 수 있다.

</div>

<details class="proof" markdown="1">
<summary>증명</summary>

측지선 방정식의 흐름을 생각하자. [§측지선, ⁋정리 7](/ko/math/riemannian_geometry/geodesics#thm7)의 증명에서 보았듯, $$(p, v) \in TM$$을 초기조건 $$\gamma(0) = p$$, $$\dot\gamma(0) = v$$로 하는 측지선 $$\gamma_{(p, v)}(t)$$는 $$TM$$ 위의 일계 상미분방정식 시스템의 해이며, 그 우변은 매끄럽다. 상미분방정식 흐름의 초기조건과 시간에 대한 매끄러운 의존성에 의해, 점 $$(p, 0) \in TM$$의 적당한 열린근방 $$\mathcal{O} \subseteq TM$$과 $$\varepsilon > 0$$이 존재하여, $$(q, w) \in \mathcal{O}$$이면 측지선 $$\gamma_{(q, w)}(t)$$가 $$t \in (-\varepsilon, \varepsilon)$$에서 정의되고 $$(t, q, w)$$에 매끄럽게 의존한다.

이제 $$\delta > 0$$을 충분히 작게 잡아 집합 $$W := \{w \in T_p M \mid \lVert w \rVert_g < \delta\}$$이 $$\mathcal{O} \cap T_p M$$에 포함되고 $$\delta < \varepsilon$$이도록 하자. 그럼 각 $$w \in W$$에 대해 $$\gamma_w$$는 $$(-\varepsilon, \varepsilon) \supseteq [0, 1]$$ 위에서 정의되므로 $$W \subseteq \mathcal{E}_p$$이고, $$\exp_p(w) = \gamma_w(1)$$은 $$\gamma_{(p, w)}(1)$$이 $$w$$에 매끄럽게 의존하는 데서 $$W$$ 위에서 매끄럽다. 마지막으로 $$W$$는 $$\lVert \cdot \rVert_g$$에 대한 원점 중심의 열린 공이므로 $$0$$에 대해 star-shaped이다. 따라서 $$V := W$$로 두면 된다.

</details>

[보조정리 2](#lem2)는 $$V$$가 star-shaped이어야 하는 이유를 설명한다. $$v \in V$$가 $$\exp_p(v) = \gamma_v(1)$$이 정의되도록 한다면, 같은 측지선의 자취 위의 점 $$\gamma_v(s) = \exp_p(sv)$$ ($$0 \le s \le 1$$)도 정의되어야 자연스러우며, 이는 정확히 $$sv \in V$$를 요구하는 조건이다. 이제 exponential map의 핵심 성질, 즉 $$0$$에서의 미분을 계산한다. 여기서 우리는 vector space $$T_p M$$의 한 점 $$0$$에서의 접공간 $$T_0(T_p M)$$을 vector space 자신 $$T_p M$$과 표준적으로 동일시한다. 구체적으로, $$v \in T_p M$$을 곡선 $$t \mapsto tv$$의 $$t = 0$$에서의 속도벡터로 보는 동일시이다.

<div class="proposition" markdown="1">

<ins id="prop4">**명제 4**</ins> 위의 표준적 동일시 $$T_0(T_p M) \cong T_p M$$ 아래에서, exponential map $$\exp_p$$의 $$0$$에서의 미분은 항등사상이다. 즉

$$(d\exp_p)_0 = \id_{T_p M}$$

이다.

</div>

<details class="proof" markdown="1">
<summary>증명</summary>

임의의 $$v \in T_p M \cong T_0(T_p M)$$을 잡자. 동일시에 따라 $$v$$는 곡선 $$\tau(t) := tv$$ (값이 $$T_p M$$ 안에 있는 곡선)의 $$t = 0$$에서의 속도벡터로 표현된다. 미분의 정의에 의해, $$(d\exp_p)_0(v)$$는 합성곡선 $$t \mapsto \exp_p(\tau(t)) = \exp_p(tv)$$의 $$t = 0$$에서의 속도벡터이다. [보조정리 2](#lem2)에 의해 $$\exp_p(tv) = \gamma_v(t)$$이므로, 이 합성곡선은 측지선 $$\gamma_v$$ 자신이고, 따라서

$$(d\exp_p)_0(v) = \left.\frac{d}{dt}\right\vert_{t = 0} \exp_p(tv) = \left.\frac{d}{dt}\right\vert_{t = 0} \gamma_v(t) = \dot\gamma_v(0) = v$$

를 얻는다. $$v$$가 임의였으므로 $$(d\exp_p)_0 = \id_{T_p M}$$이다.

</details>

## Normal neighborhood와 normal coordinate

[명제 4](#prop4)에서 $$(d\exp_p)_0$$이 가역이므로, manifold 사이의 매끄러운 함수에 대한 역함수 정리를 적용할 수 있다. 이로부터 exponential map이 $$p$$ 근방에 좌표계를 부여한다.

<div class="definition" markdown="1">

<ins id="def5">**정의 5**</ins> Riemannian manifold $$(M, g)$$의 점 $$p$$에 대해, $$0$$의 star-shaped 열린근방 $$V \subseteq T_p M$$이 존재하여 $$\exp_p\vert_V : V \to \exp_p(V)$$가 미분동형이 될 때, 상 $$U := \exp_p(V)$$를 $$p$$의 *normal neighborhood<sub>정규근방</sub>*라 부른다.

</div>

<details class="proof" markdown="1">
<summary>증명 (normal neighborhood의 존재)</summary>

[명제 3](#prop3)에 의해 $$\exp_p$$는 $$0$$의 star-shaped 열린근방 위에서 매끄러우며, [명제 4](#prop4)에 의해 $$(d\exp_p)_0 = \id_{T_p M}$$은 isomorphism이다. 따라서 manifold 사이의 매끄러운 함수에 대한 역함수 정리 ([\[미분다양체\] §부분다양체와 역함수 정리, ⁋따름정리 5](/ko/math/manifolds/submanifolds#cor5))에 의해, $$0$$의 적당한 열린근방 $$V_0$$ 위에서 $$\exp_p$$가 $$V_0$$와 $$\exp_p(V_0)$$ 사이의 미분동형을 정의한다. $$V_0$$ 안에 $$0$$ 중심의 star-shaped 열린 공 $$V$$를 잡으면 ([명제 3](#prop3)의 증명처럼 $$\lVert \cdot \rVert_g$$에 대한 충분히 작은 공) $$\exp_p\vert_V$$도 미분동형이며, $$U = \exp_p(V)$$는 normal neighborhood이다.

</details>

Normal neighborhood 위에서 exponential map의 역사상은 $$T_p M$$ 위로의 매끄러운 좌표를 준다. 여기에 접공간의 정규직교기저를 통한 선형동형을 합성하면 manifold 위의 구체적인 좌표계를 얻는다.

<div class="definition" markdown="1">

<ins id="def6">**정의 6**</ins> $$p$$의 normal neighborhood $$U = \exp_p(V)$$와 $$T_p M$$의 $$g_p$$에 대한 정규직교기저 $$(E_1, \ldots, E_n)$$이 주어졌다 하자. 이 기저가 정하는 선형동형 $$E : \mathbb{R}^n \to T_p M$$, $$E(x^1, \ldots, x^n) = \sum_i x^i E_i$$에 대해, 합성

$$\varphi := E^{-1} \circ (\exp_p\vert_V)^{-1} : U \to \mathbb{R}^n$$

을 $$p$$를 중심으로 하는 *normal coordinate<sub>정규좌표</sub>*라 부른다.

</div>

정의에 의해 $$\varphi(p) = 0$$이며, 점 $$\exp_p(v) \in U$$의 normal coordinate는 $$v = \sum_i x^i E_i$$를 만족하는 $$(x^1, \ldots, x^n)$$이다. 이 좌표계가 가지는 특징적인 성질들을 모아 다음 명제로 정리한다. 핵심은 normal coordinate에서 $$p$$를 지나는 측지선들이 원점을 지나는 직선으로 보이고, 그 결과 $$p$$에서 metric과 접속이 가장 단순한 형태를 가진다는 것이다.

<div class="proposition" markdown="1">

<ins id="prop7">**명제 7**</ins> $$p$$를 중심으로 하는 normal coordinate $$(x^i)$$에서 다음이 성립한다.

1. 각 $$v = \sum_i v^i E_i \in V$$에 대해, 측지선 $$\gamma_v$$는 좌표상에서 원점을 지나는 직선 $$t \mapsto (t v^1, \ldots, t v^n)$$으로 표현된다 (이것이 정의되는 $$t$$에 대해).
2. metric의 성분은 $$p$$에서 $$g_{ij}(p) = \delta_{ij}$$이다.
3. Christoffel 기호는 $$p$$에서 모두 소멸한다. 즉 $$\Gamma_{ij}^k(p) = 0$$이다.

</div>

<details class="proof" markdown="1">
<summary>증명</summary>

(1) $$v = \sum_i v^i E_i \in V$$에 대해 [보조정리 2](#lem2)에 의해 $$\exp_p(tv) = \gamma_v(t)$$이고, $$tv = \sum_i (t v^i) E_i$$의 normal coordinate는 정의상 $$(t v^1, \ldots, t v^n)$$이다. 따라서 $$\varphi(\gamma_v(t)) = (t v^1, \ldots, t v^n)$$이 되어, $$\gamma_v$$는 좌표상에서 원점을 지나는 직선이다.

(2) Normal coordinate의 좌표기저 vector $$\partial_i\vert_p$$는 $$\varphi$$의 미분 $$d\varphi_p$$의 역, 즉 $$(d\varphi_p)^{-1}(e_i)$$이다. 한편 $$\varphi = E^{-1} \circ (\exp_p\vert_V)^{-1}$$이고 [명제 4](#prop4)에서 $$(d\exp_p)_0 = \id$$이므로, $$p$$에서의 미분은 $$d\varphi_p = E^{-1} \circ (d\exp_p)_0^{-1} = E^{-1}$$이며, 따라서 $$\partial_i\vert_p = E(e_i) = E_i$$이다. $$(E_i)$$가 $$g_p$$에 대한 정규직교기저이므로

$$g_{ij}(p) = g_p(\partial_i\vert_p, \partial_j\vert_p) = g_p(E_i, E_j) = \delta_{ij}$$

이다.

(3) $$v = \sum_i v^i E_i \in V$$를 임의로 잡자. (1)에 의해 $$\gamma_v(t)$$의 좌표성분은 $$\gamma_v^k(t) = t v^k$$이므로 $$\ddot\gamma_v^k(t) = 0$$이다. [§측지선, ⁋정의 4](/ko/math/riemannian_geometry/geodesics#def4) 직후의 좌표 측지선 방정식

$$\ddot\gamma_v^k(t) + \sum_{i, j} \Gamma_{ij}^k(\gamma_v(t))\, \dot\gamma_v^i(t)\, \dot\gamma_v^j(t) = 0$$

에 이를 대입하면, $$\dot\gamma_v^i(t) = v^i$$이므로

$$\sum_{i, j} \Gamma_{ij}^k(\gamma_v(t))\, v^i v^j = 0$$

이 모든 $$t$$에서 성립한다. $$t = 0$$에서 $$\gamma_v(0) = p$$이므로

$$\sum_{i, j} \Gamma_{ij}^k(p)\, v^i v^j = 0$$

이고, 이는 모든 $$v = (v^1, \ldots, v^n) \in \mathbb{R}^n$$ (충분히 작은 $$v$$, 따라서 척도조정으로 모든 $$v$$)에 대해 성립한다. 각 $$k$$에 대해 $$\sum_{i, j} \Gamma_{ij}^k(p) v^i v^j$$는 $$v$$에 대한 이차형식이고, Levi-Civita 접속은 torsion-free이므로 [§레비-치비타 접속, ⁋정의 3](/ko/math/riemannian_geometry/Levi-Civita_connection#def3)에 의해 $$\Gamma_{ij}^k(p) = \Gamma_{ji}^k(p)$$로 대칭이다. 대칭인 이차형식이 항등적으로 $$0$$이면 그 계수가 모두 $$0$$이므로 ($$v = E_i + E_j$$ 등을 대입해 편극화하면), $$\Gamma_{ij}^k(p) = 0$$을 얻는다.

</details>

[명제 7](#prop7)은 normal coordinate가 점 $$p$$에서 manifold를 "유클리드 공간에 일차근사적으로 가장 가깝게" 펴는 좌표임을 말해 준다. $$g_{ij}(p) = \delta_{ij}$$와 $$\Gamma_{ij}^k(p) = 0$$은 곡률을 계산할 때 한 점에서의 계산을 크게 단순화하는 도구가 된다. 다만 이 성질들은 일반적으로 점 $$p$$에서만 성립하며, $$p$$를 벗어나면 $$g_{ij}$$의 일차 도함수가 다시 나타날 수 있다 (오직 $$M$$이 평탄할 때만 좌표 전체에서 $$g_{ij} = \delta_{ij}$$로 둘 수 있다).

## Gauss lemma

Normal coordinate는 $$p$$를 지나는 측지선을 원점을 지나는 직선으로 펴므로, $$T_p M$$의 동심 구면이 normal neighborhood 안에서 어떤 자취로 보이는지를 물을 수 있다. Gauss lemma는 이 측지구면이 방사방향 측지선과 직교함을 말한다. 먼저 그 자취들에 이름을 붙인다. 반지름 $$r > 0$$에 대해, exponential map의 정의역 안의 구면 $$S_r := \{v \in V \mid \lVert v \rVert_g = r\}$$의 상 $$\exp_p(S_r)$$을 반지름 $$r$$의 *geodesic sphere<sub>측지구면</sub>*라 부른다.

Gauss lemma를 깔끔하게 진술하기 위해, exponential map의 미분이 방사벡터와 그에 수직인 벡터에 대해 어떻게 작용하는지를 비교한다. 다음 보조정리가 핵심 계산이다.

<div class="proposition" markdown="1">

<ins id="lem8">**보조정리 8**</ins> $$v \in V \setminus \{0\}$$에 대해, $$T_v(T_p M) \cong T_p M$$의 동일시 아래에서 $$v$$ 자신을 방사벡터로 본다. 그럼 임의의 $$w \in T_p M \cong T_v(T_p M)$$에 대해

$$\bigl\langle (d\exp_p)_v(v),\, (d\exp_p)_v(w) \bigr\rangle_{\exp_p(v)} = \langle v, w \rangle_p$$

가 성립한다.

</div>

<details class="proof" markdown="1">
<summary>증명</summary>

$$w$$를 $$v$$에 평행한 성분과 수직인 성분으로 나누면 양변이 모두 $$w$$에 대해 선형이므로, $$w = v$$인 경우와 $$\langle v, w \rangle_p = 0$$인 경우만 보이면 충분하다.

먼저 $$w = v$$인 경우. [명제 4](#prop4)의 증명과 같이 곡선 $$t \mapsto v + tv = (1 + t)v$$를 생각하면, [보조정리 2](#lem2)에 의해 $$\exp_p((1 + t)v) = \gamma_v(1 + t)$$이므로

$$(d\exp_p)_v(v) = \left.\frac{d}{dt}\right\vert_{t = 0} \gamma_v(1 + t) = \dot\gamma_v(1)$$

이다. 측지선의 속력은 [§측지선, ⁋명제 6](/ko/math/riemannian_geometry/geodesics#prop6)에 의해 상수이고 $$\dot\gamma_v(0) = v$$이므로, $$\lVert \dot\gamma_v(1) \rVert = \lVert v \rVert$$이다. 따라서

$$\langle (d\exp_p)_v(v), (d\exp_p)_v(v) \rangle = \lVert \dot\gamma_v(1) \rVert^2 = \lVert v \rVert^2 = \langle v, v \rangle_p$$

가 되어 $$w = v$$인 경우가 성립한다.

다음으로 $$\langle v, w \rangle_p = 0$$인 경우. $$w$$를 실현하는 변분을 잡는다. $$T_p M$$ 안에서 $$s \mapsto v(s)$$를 $$v(0) = v$$, $$\frac{d}{ds}\big\vert_{s=0} v(s) = w$$이고 $$\lVert v(s) \rVert_g \equiv \lVert v \rVert_g$$인 곡선으로 택한다 ($$\langle v, w\rangle_p = 0$$이므로 $$v$$ 중심 구면 위의 곡선으로 가능하다). 이제 변분

$$\Gamma(s, t) := \exp_p\bigl(t\, v(s)\bigr)$$

를 생각하자. 각 $$s$$에 대해 $$t \mapsto \Gamma(s, t)$$는 [보조정리 2](#lem2)에 의해 측지선 $$\gamma_{v(s)}$$이며, $$\Gamma(0, t) = \gamma_v(t)$$이다. 변분장은

$$J(t) := \left.\frac{\partial \Gamma}{\partial s}\right\vert_{s = 0}(t) = (d\exp_p)_{tv}(t w)$$

이고, 특히 $$t = 1$$에서 $$J(1) = (d\exp_p)_v(w)$$이다. 또한 $$\partial_t \Gamma(0, t) = \dot\gamma_v(t)$$이므로, 우리가 보이려는 것은 $$\langle J(1), \dot\gamma_v(1) \rangle = 0$$이다.

함수 $$f(t) := \langle J(t), \dot\gamma_v(t) \rangle$$를 생각하자. Metric-compatibility에 의해

$$\frac{d}{dt} f(t) = \langle D_t J,\, \dot\gamma_v \rangle + \langle J,\, D_t \dot\gamma_v \rangle$$

이고, $$\gamma_v$$가 측지선이므로 둘째 항은 $$0$$이다. 첫째 항을 위해 대칭 보조정리 $$D_t \partial_s \Gamma = D_s \partial_t \Gamma$$ ([§측지선, §§에너지의 제1변분](/ko/math/riemannian_geometry/geodesics#에너지의-제1변분)에서 사용한 것) 를 적용하면 $$D_t J = D_t \partial_s \Gamma\vert_{s=0} = D_s \partial_t \Gamma\vert_{s=0}$$이고, 따라서

$$\langle D_t J, \dot\gamma_v \rangle = \langle D_s \partial_t \Gamma, \partial_t \Gamma \rangle\big\vert_{s = 0} = \frac{1}{2} \left.\frac{\partial}{\partial s}\right\vert_{s = 0} \langle \partial_t \Gamma, \partial_t \Gamma \rangle$$

이다. 그런데 각 $$s$$에 대해 $$\partial_t \Gamma(s, t) = \dot\gamma_{v(s)}(t)$$의 크기는 측지선의 속력이라 상수이고 그 값은 $$\lVert \dot\gamma_{v(s)}(0) \rVert = \lVert v(s) \rVert = \lVert v \rVert$$로 $$s$$에 무관하다. 즉 $$\langle \partial_t \Gamma, \partial_t \Gamma \rangle \equiv \lVert v \rVert^2$$은 $$s$$에 대해 상수이므로 그 $$s$$-미분이 $$0$$이고, 따라서 $$\frac{d}{dt} f(t) = 0$$이다.

이로써 $$f$$는 상수이다. 한편 $$J(0) = (d\exp_p)_0(0) = 0$$이므로 $$f(0) = \langle J(0), \dot\gamma_v(0) \rangle = 0$$이고, 따라서 $$f \equiv 0$$이다. 특히 $$f(1) = \langle J(1), \dot\gamma_v(1) \rangle = \langle (d\exp_p)_v(w), (d\exp_p)_v(v) \rangle = 0 = \langle v, w \rangle_p$$를 얻는다.

</details>

[보조정리 8](#lem8)으로부터 Gauss lemma가 곧바로 따라 나온다.

<div class="proposition" markdown="1">

<ins id="thm9">**정리 9 (Gauss lemma)**</ins> Normal neighborhood $$U = \exp_p(V)$$ 안에서, $$p$$를 지나는 방사 측지선은 자신이 만나는 측지구면과 직교한다. 즉 $$v \in V \setminus \{0\}$$이고 $$q = \exp_p(v)$$이며 $$r = \lVert v \rVert_g$$이면, $$q$$에서 측지선 $$\gamma_v$$의 속도벡터 $$\dot\gamma_v(1)$$는 측지구면 $$\exp_p(S_r)$$의 $$q$$에서의 접공간에 수직이다.

</div>

<details class="proof" markdown="1">
<summary>증명</summary>

측지구면 $$\exp_p(S_r)$$의 $$q = \exp_p(v)$$에서의 접공간은, $$S_r = \{u \in V \mid \lVert u \rVert = r\}$$이 $$v$$에서 가지는 접공간을 $$(d\exp_p)_v$$로 보낸 것이다. $$S_r$$의 $$v$$에서의 접공간은 $$v$$에 수직인 vector들 $$\{w \in T_p M \mid \langle v, w \rangle_p = 0\}$$로 이루어지므로, $$\exp_p(S_r)$$의 $$q$$에서의 접벡터는 $$\langle v, w \rangle_p = 0$$인 $$w$$에 대한 $$(d\exp_p)_v(w)$$ 꼴이다.

한편 [보조정리 8](#lem8)의 증명에서 $$\dot\gamma_v(1) = (d\exp_p)_v(v)$$임을 보였다. 따라서 임의의 그러한 접벡터 $$(d\exp_p)_v(w)$$에 대해, [보조정리 8](#lem8)에 의해

$$\langle \dot\gamma_v(1),\, (d\exp_p)_v(w) \rangle_q = \langle (d\exp_p)_v(v),\, (d\exp_p)_v(w) \rangle_q = \langle v, w \rangle_p = 0$$

이다. 즉 $$\dot\gamma_v(1)$$는 측지구면의 모든 접벡터에 수직이다.

</details>

Gauss lemma는 normal neighborhood 안에서 exponential map이 방사방향으로는 *등거리*임을 (방사 측지선의 호의 길이가 $$T_p M$$에서의 거리 $$\lVert v \rVert$$와 같음을) 함의하며, 이는 측지선이 충분히 짧은 구간에서 길이를 최소화함을 증명하는 출발점이 된다. 이 사실은 [§측지선, ⁋따름정리 5](/ko/math/riemannian_geometry/geodesics#cor5) 뒤에서 언급했던 "측지선이 충분히 짧은 구간에서 최단곡선"이라는 주장을 정당화한다.

## 예시

가장 기본적인 두 예시에서 exponential map을 직접 계산한다.

<div class="example" markdown="1">

<ins id="ex10">**예시 10**</ins> 유클리드 공간 $$\mathbb{R}^n$$에 standard metric을 주자. [§측지선, ⁋예시 8](/ko/math/riemannian_geometry/geodesics#ex8)에서 보았듯 측지선은 직선 $$\gamma_v(t) = p + tv$$이며, 이는 모든 $$t \in \mathbb{R}$$에서 정의된다. 따라서 $$\mathcal{E}_p = T_p M = \mathbb{R}^n$$이고

$$\exp_p(v) = \gamma_v(1) = p + v$$

이다. 즉 $$T_p \mathbb{R}^n \cong \mathbb{R}^n$$을 표준적으로 $$\mathbb{R}^n$$과 동일시하면 exponential map은 평행이동 $$v \mapsto p + v$$이다. 이는 전체 위에서 미분동형이므로 $$\mathbb{R}^n$$ 전체가 임의의 $$p$$의 normal neighborhood이며, [명제 4](#prop4)의 $$(d\exp_p)_0 = \id$$도 평행이동의 미분이 항등사상이라는 사실로 직접 확인된다. 이 경우 normal coordinate는 ($$p$$를 원점으로 옮긴) 표준 데카르트 좌표이고, 모든 점에서 $$g_{ij} = \delta_{ij}$$, $$\Gamma_{ij}^k = 0$$이다.

</div>

<div class="example" markdown="1">

<ins id="ex11">**예시 11**</ins> $$\mathbb{R}^3$$에 매장된 단위 구면 $$S^2$$에 round metric을 주자. [§측지선, ⁋예시 9](/ko/math/riemannian_geometry/geodesics#ex9)에서 점 $$p \in S^2$$와 단위 vector $$v \in T_p S^2$$에 대한 측지선이 대원

$$\gamma_v(t) = (\cos t)\, p + (\sin t)\, v$$

임을 보았다. 일반의 $$v \in T_p S^2$$에 대해서는 [보조정리 2](#lem2)의 동차성으로 속력 $$\lVert v \rVert = r$$을 반영하면

$$\gamma_v(t) = (\cos rt)\, p + \frac{\sin rt}{r}\, v$$

이고, 따라서

$$\exp_p(v) = \gamma_v(1) = (\cos r)\, p + \frac{\sin r}{r}\, v, \qquad r = \lVert v \rVert$$

이다. 기하적으로 $$\exp_p$$는 접평면 $$T_p S^2$$의 vector $$v$$를, $$v$$ 방향의 대원을 따라 호의 길이 $$r = \lVert v \rVert$$만큼 나아간 점으로 보내는 *방사사상*이다. 이 사상은 $$r < \pi$$인 영역, 즉 열린 공 $$\{v \mid \lVert v \rVert < \pi\}$$ 위에서 미분동형이며, 그 상은 $$p$$의 대척점 $$-p$$를 제외한 $$S^2 \setminus \{-p\}$$로서 $$p$$의 normal neighborhood이다. 반지름 $$r$$의 측지구면 $$\exp_p(S_r)$$은 $$p$$로부터 측지거리 $$r$$만큼 떨어진 위도원이며, [정리 9](#thm9)가 말하듯 $$p$$에서 나오는 대원들(경도선)이 이 위도원들과 직교한다. $$r = \pi$$에서 $$\exp_p$$가 구면 $$S_\pi$$ 전체를 한 점 $$-p$$로 보내 미분동형이 깨지는 것은, normal neighborhood가 일반적으로 $$T_p M$$ 전체로 확장되지 않는 전형적인 예이다.

</div>

[예시 11](#ex11)에서 보듯 $$S^2$$의 exponential map은 한 점의 접평면에서 측지거리를 따라 구면을 펴는 사상이며, 이는 지도제작에서 한 점을 중심으로 한 *방위투영*의 기하적 모형이기도 하다. 일반의 Riemannian manifold에서도 exponential map은 같은 방식으로 접공간의 평탄한 기하를 측지선을 따라 manifold 위로 옮기며, 이로써 우리는 한 점 근방의 곡률 정보를 접공간 위의 좌표로 환원해 분석할 수 있다.

---

**참고문헌**

**[Lee]** John M. Lee, *Introduction to Riemannian Manifolds*, Graduate Texts in Mathematics, Springer, 2019.

**[dC]** Manfredo P. do Carmo, *Riemannian Geometry*, Birkhäuser, 1992.

---
