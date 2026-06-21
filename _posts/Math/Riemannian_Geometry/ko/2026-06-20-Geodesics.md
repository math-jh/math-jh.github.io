---
title: "측지선"
description: "곡선의 길이 범함수와 에너지 범함수를 도입하고, 에너지의 제1변분으로부터 Levi-Civita 접속에 대한 측지선 방정식을 유도한다. 측지선이 에너지의 임계 곡선이라는 사실과, 측지선 ODE의 국소적 존재성과 유일성, 그리고 유클리드 공간과 구면에서의 예시를 다룬다."
excerpt: "에너지 범함수의 임계 곡선으로서의 측지선과 측지선 방정식"

categories: [Math / Riemannian Geometry]
permalink: /ko/math/riemannian_geometry/geodesics
sidebar: 
    nav: "riemannian_geometry-ko"

date: 2026-06-20
weight: 5
published: false

---

[§리만 계량, ⁋정의 2](/ko/math/riemannian_geometry/Riemannian_metric#def2)에서 우리는 Riemannian manifold $$(M, g)$$ 위의 곡선 $$\gamma$$에 길이를 부여했다. 유클리드 공간에서 두 점을 잇는 최단 곡선은 직선이며, 직선은 가속도가 $$0$$인 곡선이기도 하다. 일반적인 Riemannian manifold에서 "가속도가 $$0$$"이라는 조건을 정식화하려면 곡선을 따른 미분, 즉 [§접속, ⁋정의 1](/ko/math/riemannian_geometry/connection#def1)의 connection이 필요하다. 이 글에서는 길이와 더불어 다루기 쉬운 *에너지* 범함수를 도입하고, 그 제1변분을 통해 가속도가 소멸하는 곡선, 즉 *측지선*을 에너지의 임계 곡선으로 특징짓는다.

## 길이 범함수와 에너지 범함수

곡선 $$\gamma : [a, b] \to M$$의 길이는 적분 $$\length(\gamma) = \int_a^b \lVert \dot\gamma(t)\rVert_g \mathop{dt}$$로 주어진다. 이 범함수는 피적분함수에 제곱근이 들어 있어 변분을 계산할 때 다루기 번거로우며, 또한 $$\dot\gamma(t) = 0$$인 점에서 미분가능하지 않다. 더불어 길이는 [§리만 계량, ⁋정의 2](/ko/math/riemannian_geometry/Riemannian_metric#def2) 직후에 언급했듯 reparametrization에 불변이므로 그 임계 곡선이 유일한 parametrization을 결정하지 못한다. 이러한 이유로 우리는 제곱근을 없앤 다음의 범함수를 함께 도입한다.

<div class="definition" markdown="1">

<ins id="def1">**정의 1**</ins> Riemannian manifold $$(M, g)$$ 위의 곡선 $$\gamma : [a, b] \to M$$의 *에너지<sub>energy</sub>* $$E(\gamma)$$는 다음의 식

$$E(\gamma) = \frac{1}{2} \int_a^b \lVert \dot\gamma(t)\rVert_g^2 \mathop{dt} = \frac{1}{2}\int_a^b \langle \dot\gamma(t), \dot\gamma(t)\rangle_g \mathop{dt}$$

으로 정의된다.

</div>

상수 $$1/2$$은 본질적인 것이 아니라 뒤의 제1변분 공식에서 인수 $$2$$를 상쇄하기 위한 관례적 선택이다. 길이와 달리 에너지의 피적분함수 $$\langle \dot\gamma, \dot\gamma\rangle$$는 $$\dot\gamma$$에 대해 매끄러우며, 또한 reparametrization에 의존한다. 다음 명제는 두 범함수가 Cauchy-Schwarz 부등식으로 연결되며, 그 등호가 성립하는 경우가 정확히 *일정한 속력*으로 움직이는 parametrization임을 보여준다.

<div class="proposition" markdown="1">

<ins id="prop2">**명제 2**</ins> 곡선 $$\gamma : [a, b] \to M$$에 대해 다음의 부등식

$$\length(\gamma)^2 \le 2(b - a)\, E(\gamma)$$

이 성립하며, 등호가 성립하는 것은 $$\lVert \dot\gamma(t)\rVert_g$$가 $$[a, b]$$ 위에서 상수인 것, 즉 $$\gamma$$가 일정한 속력을 갖는 것과 동치이다.

</div>

<details class="proof" markdown="1">
<summary>증명</summary>

$$L^2([a, b])$$의 두 함수 $$f(t) = \lVert \dot\gamma(t)\rVert_g$$와 $$h(t) \equiv 1$$에 Cauchy-Schwarz 부등식 $$\left(\int_a^b f h \mathop{dt}\right)^2 \le \int_a^b f^2 \mathop{dt} \int_a^b h^2 \mathop{dt}$$을 적용하면

$$\length(\gamma)^2 = \left(\int_a^b \lVert \dot\gamma(t)\rVert_g \mathop{dt}\right)^2 \le \left(\int_a^b \lVert \dot\gamma(t)\rVert_g^2 \mathop{dt}\right)\left(\int_a^b 1 \mathop{dt}\right) = 2(b - a)\, E(\gamma)$$

를 얻는다. Cauchy-Schwarz 부등식의 등호 조건은 $$f$$와 $$h$$가 일차종속, 즉 $$f$$가 상수배 $$h$$인 것이므로, 여기서는 $$\lVert \dot\gamma(t)\rVert_g$$가 상수인 것과 동치이다.

</details>

따라서 일정한 속력을 갖는 곡선들만 비교한다면 에너지를 최소화하는 것과 길이를 최소화하는 것이 일치한다. 임의의 곡선은 (속력이 $$0$$인 점이 없을 때) 호의 길이로 reparametrize해 일정한 속력을 갖도록 만들 수 있으므로, 길이의 최소화 문제를 에너지의 최소화 문제로 옮겨 다루어도 일반성을 잃지 않는다. 이것이 우리가 다루기 쉬운 에너지를 통해 측지선을 정의하는 근거이다.

## 에너지의 제1변분

에너지의 임계 곡선을 찾기 위해 곡선을 한 매개변수만큼 흔드는 변분을 도입한다. 곡선 $$\gamma : [a, b] \to M$$의 *변분<sub>variation</sub>*이란 매끄러운 함수 $$\Gamma : (-\varepsilon, \varepsilon) \times [a, b] \to M$$으로서 $$\Gamma(0, t) = \gamma(t)$$를 만족하는 것을 말한다. 각 $$s$$에 대해 $$\gamma_s(t) := \Gamma(s, t)$$는 곡선이며, $$s = 0$$에서의 무한소 변화량

$$V(t) := \left.\frac{\partial \Gamma}{\partial s}\right\vert_{s = 0}(t) \in T_{\gamma(t)} M$$

을 그 변분의 *변분장<sub>variation field</sub>*이라 부른다. 끝점을 고정하는 변분, 즉 모든 $$s$$에 대해 $$\Gamma(s, a) = \gamma(a)$$와 $$\Gamma(s, b) = \gamma(b)$$를 만족하는 변분을 *고정변분<sub>proper variation</sub>*이라 부르며, 이 경우 $$V(a) = V(b) = 0$$이다.

이제 곡선을 따른 미분을 명시하기 위해, $$\Gamma$$를 따라 정의된 vector field $$\partial_t \Gamma$$와 $$\partial_s \Gamma$$를 생각한다. Levi-Civita 접속 $$\nabla$$는 곡선을 따른 covariant derivative $$D_t, D_s$$를 유도하며, $$\Gamma$$의 좌표성분에 대한 직접적인 계산으로부터 다음의 *대칭 보조정리*

$$D_s \partial_t \Gamma = D_t \partial_s \Gamma$$

가 성립한다. 이는 Levi-Civita 접속이 torsion-free, 즉 [§레비-치비타 접속, ⁋정의 3](/ko/math/riemannian_geometry/Levi-Civita_connection#def3)에서 $$\Gamma_{ij}^k = \Gamma_{ji}^k$$가 성립하는 데서 비롯한다. 이 사실을 이용해 에너지의 제1변분을 계산한다.

<div class="proposition" markdown="1">

<ins id="thm3">**정리 3 (에너지의 제1변분)**</ins> 곡선 $$\gamma : [a, b] \to M$$의 변분 $$\Gamma$$와 그 변분장 $$V$$에 대해, $$E(s) := E(\gamma_s)$$라 두면 다음의 식

$$\left.\frac{d}{ds}\right\vert_{s = 0} E(\gamma_s) = \langle V(b), \dot\gamma(b)\rangle - \langle V(a), \dot\gamma(a)\rangle - \int_a^b \langle V(t),\, D_t \dot\gamma(t)\rangle \mathop{dt}$$

이 성립한다. 특히 $$\Gamma$$가 고정변분이면 우변의 경계항이 소멸하여

$$\left.\frac{d}{ds}\right\vert_{s = 0} E(\gamma_s) = -\int_a^b \langle V(t),\, D_t \dot\gamma(t)\rangle \mathop{dt}$$

이다.

</div>

<details class="proof" markdown="1">
<summary>증명</summary>

$$E(\gamma_s) = \frac{1}{2}\int_a^b \langle \partial_t \Gamma, \partial_t \Gamma\rangle \mathop{dt}$$이므로 적분기호 안에서 $$s$$에 대해 미분하면, $$\nabla$$가 metric과 compatible, 즉 [§레비-치비타 접속, ⁋정의 1](/ko/math/riemannian_geometry/Levi-Civita_connection#def1)의 식이 곡선을 따른 미분 $$D_s$$에 대해서도 성립하므로

$$\frac{d}{ds} E(\gamma_s) = \frac{1}{2}\int_a^b \partial_s \langle \partial_t \Gamma, \partial_t \Gamma\rangle \mathop{dt} = \int_a^b \langle D_s \partial_t \Gamma,\, \partial_t \Gamma\rangle \mathop{dt}$$

을 얻는다. 여기에 대칭 보조정리 $$D_s \partial_t \Gamma = D_t \partial_s \Gamma$$를 대입하면

$$\frac{d}{ds} E(\gamma_s) = \int_a^b \langle D_t \partial_s \Gamma,\, \partial_t \Gamma\rangle \mathop{dt}$$

이 된다. 한편 metric-compatibility로부터 다음의 곱미분

$$\frac{d}{dt}\langle \partial_s \Gamma,\, \partial_t \Gamma\rangle = \langle D_t \partial_s \Gamma,\, \partial_t \Gamma\rangle + \langle \partial_s \Gamma,\, D_t \partial_t \Gamma\rangle$$

이 성립하므로, 이를 위 적분에 대입하고 미적분학의 기본정리를 적용하면

$$\frac{d}{ds} E(\gamma_s) = \int_a^b \frac{d}{dt}\langle \partial_s \Gamma,\, \partial_t \Gamma\rangle \mathop{dt} - \int_a^b \langle \partial_s \Gamma,\, D_t \partial_t \Gamma\rangle \mathop{dt} = \Bigl[\langle \partial_s \Gamma,\, \partial_t \Gamma\rangle\Bigr]_a^b - \int_a^b \langle \partial_s \Gamma,\, D_t \partial_t \Gamma\rangle \mathop{dt}$$

가 된다. 이제 $$s = 0$$에서 평가하면 $$\partial_s \Gamma\vert_{s = 0} = V$$, $$\partial_t \Gamma\vert_{s = 0} = \dot\gamma$$, $$D_t \partial_t \Gamma\vert_{s = 0} = D_t \dot\gamma$$이므로

$$\left.\frac{d}{ds}\right\vert_{s = 0} E(\gamma_s) = \langle V(b), \dot\gamma(b)\rangle - \langle V(a), \dot\gamma(a)\rangle - \int_a^b \langle V,\, D_t \dot\gamma\rangle \mathop{dt}$$

을 얻는다. 고정변분의 경우 $$V(a) = V(b) = 0$$이므로 경계항이 소멸한다.

</details>

여기서 $$D_t \dot\gamma$$는 곡선 $$\gamma$$ 자신의 속도장 $$\dot\gamma$$를 $$\gamma$$를 따라 covariant하게 미분한 것으로, $$\gamma$$의 *가속도<sub>acceleration</sub>*에 해당한다. 이를 $$\nabla_{\dot\gamma} \dot\gamma$$로도 적는다. 제1변분 공식은 임의의 고정변분에 대한 에너지의 변화가 가속도 $$D_t \dot\gamma$$와 변분장 $$V$$의 내적의 적분으로 통제됨을 말해 준다. 따라서 $$\gamma$$가 에너지의 임계 곡선이려면 이 적분이 모든 $$V$$에 대해 소멸해야 하고, 이는 가속도 자체가 소멸함을 강제한다.

## 측지선 방정식

가속도가 소멸하는 곡선을 정식으로 정의한다.

<div class="definition" markdown="1">

<ins id="def4">**정의 4**</ins> Riemannian manifold $$(M, g)$$의 Levi-Civita 접속 $$\nabla$$에 대해, 곡선 $$\gamma : I \to M$$이 다음의 식

$$\nabla_{\dot\gamma} \dot\gamma = D_t \dot\gamma = 0$$

을 모든 $$t \in I$$에서 만족할 때 $$\gamma$$를 *geodesic<sub>측지선</sub>*이라 부르고, 위의 식을 *측지선 방정식<sub>geodesic equation</sub>*이라 부른다.

</div>

측지선 방정식은 [§레비-치비타 접속, ⁋정의 8](/ko/math/riemannian_geometry/Levi-Civita_connection#def8)의 언어로 다시 읽으면, 속도장 $$\dot\gamma$$가 곡선 $$\gamma$$ 자신을 따라 parallel vector field인 것과 같다. 즉 측지선이란 *자신의 속도를 평행 운반하며 나아가는* 곡선이다. Local coordinate $$(x^i)$$에서 $$\gamma(t) = (\gamma^1(t), \ldots, \gamma^n(t))$$로 쓰면, $$\nabla_{\dot\gamma}\dot\gamma$$를 [§레비-치비타 접속, ⁋명제 9](/ko/math/riemannian_geometry/Levi-Civita_connection#prop9)의 증명에서와 같이 Christoffel 기호로 풀어 측지선 방정식은 다음의 식

$$\ddot\gamma^k(t) + \sum_{i, j = 1}^n \Gamma_{ij}^k(\gamma(t))\, \dot\gamma^i(t)\, \dot\gamma^j(t) = 0, \qquad k = 1, \ldots, n$$

으로 표현된다. 이는 $$\gamma^k$$들에 대한 $$n$$개의 이계 비선형 상미분방정식 시스템이다.

먼저 측지선이 [정리 3](#thm3)이 예고한 대로 정확히 에너지의 임계 곡선임을 확인한다.

<div class="proposition" markdown="1">

<ins id="cor5">**따름정리 5**</ins> 곡선 $$\gamma : [a, b] \to M$$이 측지선인 것과, 끝점을 고정하는 모든 고정변분 $$\Gamma$$에 대해 $$\left.\frac{d}{ds}\right\vert_{s = 0} E(\gamma_s) = 0$$이 성립하는 것은 동치이다.

</div>

<details class="proof" markdown="1">
<summary>증명</summary>

$$\gamma$$가 측지선이면 $$D_t \dot\gamma = 0$$이므로 [정리 3](#thm3)의 고정변분 공식 우변의 피적분함수가 항등적으로 $$0$$이 되어 모든 고정변분에 대해 제1변분이 소멸한다.

역으로 모든 고정변분에 대해 제1변분이 소멸한다 하자. [정리 3](#thm3)에 의해 모든 고정변분장 $$V$$에 대해 $$\int_a^b \langle V, D_t \dot\gamma\rangle \mathop{dt} = 0$$이다. $$D_t \dot\gamma$$가 어떤 점 $$t_0 \in (a, b)$$에서 $$0$$이 아니라고 가정하자. $$\varphi : [a, b] \to [0, \infty)$$를 $$\varphi(t_0) > 0$$이고 $$\varphi(a) = \varphi(b) = 0$$이며 $$t_0$$의 작은 근방 밖에서 $$0$$인 bump function이라 하면, $$V(t) := \varphi(t)\, D_t \dot\gamma(t)$$는 $$V(a) = V(b) = 0$$을 만족하는 곡선 $$\gamma$$ 위의 vector field이며 어떤 고정변분의 변분장으로 실현된다. 이때

$$\int_a^b \langle V, D_t \dot\gamma\rangle \mathop{dt} = \int_a^b \varphi(t)\, \lVert D_t \dot\gamma(t)\rVert_g^2 \mathop{dt} > 0$$

이 되어 가정에 모순이다. 따라서 $$D_t \dot\gamma \equiv 0$$, 즉 $$\gamma$$는 측지선이다.

</details>

[따름정리 5](#cor5)는 측지선이 정확히 에너지 범함수의 Euler-Lagrange 방정식을 푸는 곡선임을 말해 준다. [명제 2](#prop2)와 결합하면, 측지선은 일정한 속력을 가지므로 (다음 명제) 동시에 길이의 임계 곡선이기도 하다. 다만 측지선이 항상 길이의 *최소화* 곡선인 것은 아니며, 충분히 짧은 구간에서만 그러함을 보일 수 있다.

측지선이 일정한 속력을 갖는다는 사실은 위에서 언급했듯 metric-compatibility의 직접적 귀결이다.

<div class="proposition" markdown="1">

<ins id="prop6">**명제 6**</ins> 측지선 $$\gamma : I \to M$$의 속력 $$\lVert \dot\gamma(t)\rVert_g$$는 $$I$$ 위에서 상수이다.

</div>

<details class="proof" markdown="1">
<summary>증명</summary>

$$f(t) := \langle \dot\gamma(t), \dot\gamma(t)\rangle$$라 두자. Metric-compatibility로부터

$$\frac{d}{dt} f(t) = \frac{d}{dt}\langle \dot\gamma, \dot\gamma\rangle = 2\langle D_t \dot\gamma,\, \dot\gamma\rangle$$

이고, $$\gamma$$가 측지선이므로 $$D_t \dot\gamma = 0$$이다. 따라서 $$f$$의 미분이 항등적으로 $$0$$이 되어 $$\lVert \dot\gamma\rVert_g = \sqrt{f}$$는 상수이다.

</details>

## 국소적 존재성과 유일성

측지선 방정식이 이계 상미분방정식 시스템이라는 사실로부터, 한 점에서의 위치와 속도를 주면 측지선이 국소적으로 유일하게 결정된다.

<div class="proposition" markdown="1">

<ins id="thm7">**정리 7 (측지선의 국소적 존재성과 유일성)**</ins> Riemannian manifold $$(M, g)$$의 점 $$p \in M$$과 vector $$v \in T_p M$$, 그리고 $$t_0 \in \mathbb{R}$$이 주어졌다 하자. 그럼 $$t_0$$의 어떤 열린구간 $$I \ni t_0$$ 위에서 정의된 측지선 $$\gamma : I \to M$$으로서 초기조건

$$\gamma(t_0) = p, \qquad \dot\gamma(t_0) = v$$

를 만족하는 것이 존재한다. 또한 이러한 두 측지선은 그 정의역의 공통부분에서 일치한다.

</div>

<details class="proof" markdown="1">
<summary>증명</summary>

$$p$$ 근방의 local coordinate $$(U, (x^i))$$를 잡자. 이 좌표계에서 측지선 방정식은 $$\gamma^k$$들에 대한 이계 상미분방정식 시스템

$$\ddot\gamma^k = -\sum_{i, j = 1}^n \Gamma_{ij}^k(\gamma)\, \dot\gamma^i\, \dot\gamma^j, \qquad k = 1, \ldots, n$$

이다. 새로운 변수 $$w^k := \dot\gamma^k$$를 도입하면 이를 일계 시스템

$$\dot\gamma^k = w^k, \qquad \dot w^k = -\sum_{i, j = 1}^n \Gamma_{ij}^k(\gamma)\, w^i\, w^j, \qquad k = 1, \ldots, n$$

으로 환원할 수 있다. 우변은 $$(\gamma^k, w^k)$$에 대해 매끄러우며, [§레비-치비타 접속, ⁋명제 6](/ko/math/riemannian_geometry/Levi-Civita_connection#prop6)에 의해 $$\Gamma_{ij}^k$$가 매끄러운 함수이므로 특히 국소적으로 Lipschitz이다. 따라서 상미분방정식의 Picard-Lindelöf 정리에 의해 초기조건 $$\gamma^k(t_0) = p^k$$, $$w^k(t_0) = v^k$$를 만족하는 해가 $$t_0$$의 어떤 열린구간 위에서 유일하게 존재한다. 이 해의 첫 성분 $$\gamma = (\gamma^k)$$가 원하는 측지선이며, Picard-Lindelöf 정리의 유일성으로부터 두 측지선은 정의역의 공통부분에서 일치한다.

</details>

위 정리의 해가 정의되는 구간 $$I$$는 일반적으로 $$\mathbb{R}$$ 전체가 아닐 수 있다. 임의의 시간에 대해 측지선이 항상 정의되는 manifold를 *geodesically complete<sub>측지적으로 완비된</sub>*이라 부르며, 이는 Hopf-Rinow 정리를 통해 거리공간으로서의 완비성과 동치임이 알려져 있다. 측지선의 정의역을 최대한 늘려 얻는 자료가 exponential map의 출발점이 된다 ([참고 10](#rmk10)).

## 예시

가장 기본적인 두 예시를 살펴본다.

<div class="example" markdown="1">

<ins id="ex8">**예시 8**</ins> 유클리드 공간 $$\mathbb{R}^n$$에 standard metric $$g_{ij} = \delta_{ij}$$를 주자. [§레비-치비타 접속, ⁋예시 7](/ko/math/riemannian_geometry/Levi-Civita_connection#ex7)에서 보았듯 모든 Christoffel 기호가 $$0$$이므로, 측지선 방정식은

$$\ddot\gamma^k(t) = 0, \qquad k = 1, \ldots, n$$

으로 환원된다. 따라서 측지선은 정확히 $$\gamma(t) = p + t v$$ 꼴의 (일정한 속력으로 매개화된) 직선들이다. 이는 유클리드 공간에서 두 점을 잇는 최단 곡선이 직선이라는 익숙한 사실과 일치한다.

</div>

<div class="example" markdown="1">

<ins id="ex9">**예시 9**</ins> $$\mathbb{R}^3$$에 매장된 단위 구면 $$S^2$$에 standard round metric, 즉 $$\iota : S^2 \hookrightarrow \mathbb{R}^3$$로 유도된 metric을 주자. 한 점 $$p \in S^2$$와 단위 vector $$v \in T_p S^2$$를 잡고, $$p$$와 $$v$$가 펼치는 $$\mathbb{R}^3$$의 평면 $$P = \span\{p, v\}$$를 생각하자. 이 평면이 구면과 만나는 교선은 *대원<sub>great circle</sub>*

$$\gamma(t) = (\cos t)\, p + (\sin t)\, v$$

이며, 우리는 이것이 측지선임을 보인다. 직접 미분하면 $$\mathbb{R}^3$$에서의 가속도는

$$\ddot\gamma(t) = -(\cos t)\, p - (\sin t)\, v = -\gamma(t)$$

이다. 한편 $$S^2$$의 점 $$\gamma(t)$$에서 단위 법선벡터는 위치벡터 $$\gamma(t)$$ 자신이므로, $$\ddot\gamma(t) = -\gamma(t)$$는 모든 $$t$$에서 $$T_{\gamma(t)} S^2$$에 수직이다. 매장된 submanifold의 Levi-Civita 접속에 대한 가속도 $$D_t \dot\gamma$$는 주변 공간 $$\mathbb{R}^3$$에서의 가속도 $$\ddot\gamma$$를 접공간 $$T_{\gamma(t)} S^2$$로 정사영한 것과 같다는 사실을 적용하면, 접성분이 $$0$$이므로 $$D_t \dot\gamma = 0$$이다. 따라서 대원은 측지선이며, [정리 7](#thm7)의 유일성에 의해 $$S^2$$의 측지선은 정확히 대원들 (을 일정한 속력으로 매개화한 곡선들) 임을 알 수 있다.

</div>

[예시 9](#ex9)에서 사용한 "주변 공간의 가속도를 접공간으로 정사영한 것이 곡선 위의 covariant derivative"라는 사실은 [§리만 계량, §§Normal bundle](/ko/math/riemannian_geometry/Riemannian_metric#normal-bundle)에서 도입한 tangential-normal 분해를 곡선의 가속도에 적용한 것이다. 이 관찰은 일반적인 매장된 submanifold의 측지선을 다룰 때 핵심적인 도구가 된다.

<div class="remark" markdown="1">

<ins id="rmk10">**참고 10**</ins> [정리 7](#thm7)은 각 $$(p, v) \in TM$$마다 그 점에서 출발하는 유일한 측지선 $$\gamma_v$$를 대응시킨다. $$v$$를 적절히 줄여 측지선이 $$t = 1$$까지 정의되도록 하면, 대응 $$v \mapsto \gamma_v(1)$$은 $$T_p M$$의 한 근방에서 $$M$$으로의 매끄러운 함수를 정의하는데, 이를 점 $$p$$에서의 *exponential map*이라 부른다. Exponential map은 측지선의 자료를 한 점의 접공간 위로 모아 manifold의 국소 구조를 선형화하는 도구이다.

</div>

---

**참고문헌**

**[Lee]** John M. Lee, *Introduction to Riemannian Manifolds*, Graduate Texts in Mathematics, Springer, 2019.

**[dC]** Manfredo P. do Carmo, *Riemannian Geometry*, Birkhäuser, 1992.

---
