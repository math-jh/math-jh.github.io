---
title: "Dolbeault 코호몰로지"
description: "복소다양체 위에서 외미분이 d = ∂ + ∂̄로 갈라지는 구조를 세우고, d² = 0으로부터 ∂² = ∂̄² = 0과 ∂∂̄ + ∂̄∂ = 0을 유도한다. ∂̄-복합체로 Dolbeault 코호몰로지 H^{p,q}를 정의하고, ∂̄-Poincaré 보조정리(Dolbeault–Grothendieck)를 거쳐 Dolbeault 정리 H^{p,q} ≅ H^q(X, Ω^p)를 fine resolution으로 증명한다. ℂ^n과 콤팩트 Riemann 곡면의 Hodge 수를 예시로 계산한다."
excerpt: "del과 del-bar 연산자, d = ∂ + ∂̄ 분해, Dolbeault 복합체, Dolbeault 코호몰로지, Hodge 수, ∂̄-Poincaré 보조정리, Dolbeault–Grothendieck, Dolbeault 정리, fine resolution, 정칙 p-형식 층, Riemann 곡면 genus"

categories: [Math / Complex Geometry]
permalink: /ko/math/complex_geometry/dolbeault_cohomology
sidebar:
    nav: "complex_geometry-ko"

date: 2026-06-22
weight: 3

published: false
---

거의 복소구조의 언어로 복소화 미분형식이 차수별로 $$(p,q)$$-형식으로 갈라짐을 보았다 ([§거의 복소구조, ⁋명제 7](/ko/math/complex_geometry/almost_complex_structures#prop7)). 그러나 이 분해는 형식 자체의 정적인 분류일 뿐, 그 위에서 작동하는 미분연산자 $$d$$가 이 분해와 어떻게 어울리는지는 아직 묻지 않았다. 매끄러운 다양체에서 $$d$$와 그로부터 얻는 de Rham 코호몰로지가 위상을 읽어냈듯이 ([\[미분다양체\] §미분형식, ⁋정리 2](/ko/math/manifolds/differential_forms#thm2)), 복소다양체에서는 $$d$$가 $$(p,q)$$-분해와 맞물려 두 연산자 $$\partial$$와 $$\bar\partial$$로 갈라지고, 그중 $$\bar\partial$$가 정칙성을 측정하는 복합체를 만든다.

이 글의 목표는 적분가능한 거의 복소구조, 곧 복소다양체 위에서 $$d = \partial + \bar\partial$$ 분해를 세우고, $$\bar\partial$$로부터 Dolbeault 코호몰로지 $$H^{p,q}_{\bar\partial}(X)$$를 정의하며, 그것이 정칙 $$p$$-형식의 층 $$\Omega^p$$의 층 코호몰로지 $$H^q(X, \Omega^p)$$와 일치한다는 Dolbeault 정리를 증명하는 것이다. 핵심 도구는 폴리디스크에서 $$\bar\partial$$-닫힌 형식이 항상 $$\bar\partial$$-완전하다는 $$\bar\partial$$-Poincaré 보조정리이며, 이것이 Dolbeault 복합체를 정칙형식 층의 fine resolution으로 바꿔준다.

## $$\partial$$와 $$\bar\partial$$ 연산자

복소다양체 $$X$$ 위에서 외미분 $$d$$는 복소화 형식에도 $$\mathbb{C}$$-선형으로 확장된다. 국소 정칙좌표 $$z_1, \ldots, z_n$$에서 $$(p,q)$$-형식은

$$
\omega = \sum_{\lvert I \rvert = p,\ \lvert J \rvert = q} f_{IJ}\, dz_I \wedge d\bar{z}_J, \qquad
dz_I = dz_{i_1} \wedge \cdots \wedge dz_{i_p},\ \ d\bar{z}_J = d\bar{z}_{j_1} \wedge \cdots \wedge d\bar{z}_{j_q}
$$

로 적힌다. 여기서 $$dz_I$$와 $$d\bar{z}_J$$는 상수계수 닫힌형식이므로 ($$d(dz_j) = d(d\bar z_j) = 0$$), $$d\omega$$는 계수 $$f_{IJ}$$의 외미분에서만 나온다. 그런데 함수의 외미분은

$$
df_{IJ} = \sum_{k} \frac{\partial f_{IJ}}{\partial z_k}\, dz_k + \sum_{k} \frac{\partial f_{IJ}}{\partial \bar{z}_k}\, d\bar{z}_k
$$

로 $$(1,0)$$-부분과 $$(0,1)$$-부분으로 자연히 갈라진다. 앞항을 wedge하면 형식의 차수가 $$(p+1,q)$$로, 뒷항을 wedge하면 $$(p,q+1)$$로 올라간다. 이 갈림이 $$\partial$$와 $$\bar\partial$$의 정의를 준다.

<div class="definition" markdown="1">

<ins id="def1">**정의 1**</ins> 복소다양체 $$X$$ 위의 $$(p,q)$$-형식 $$\omega = \sum_{I,J} f_{IJ}\, dz_I \wedge d\bar{z}_J$$에 대하여 *del 연산자<sub>del operator</sub>* $$\partial$$와 *del-bar 연산자<sub>del-bar operator</sub>* $$\bar\partial$$를 국소좌표에서

$$
\partial \omega = \sum_{I,J} \sum_{k} \frac{\partial f_{IJ}}{\partial z_k}\, dz_k \wedge dz_I \wedge d\bar{z}_J, \qquad
\bar\partial \omega = \sum_{I,J} \sum_{k} \frac{\partial f_{IJ}}{\partial \bar{z}_k}\, d\bar{z}_k \wedge dz_I \wedge d\bar{z}_J
$$

으로 정의한다. 그러면 $$\partial : \Omega^{p,q}(X) \to \Omega^{p+1,q}(X)$$이고 $$\bar\partial : \Omega^{p,q}(X) \to \Omega^{p,q+1}(X)$$이다.

</div>

위 정의는 좌표 표현으로 주어졌지만 좌표에 무관하게 잘 정의된다. 이를 보는 가장 깔끔한 방법은 $$\partial$$와 $$\bar\partial$$를 외미분 $$d$$의 성분으로 규정하는 것이다. $$(p,q)$$-형식에 $$d$$를 작용시키면 그 값은 $$(p+1,q)$$-형식과 $$(p,q+1)$$-형식의 합이며, $$\partial \omega$$와 $$\bar\partial \omega$$는 각각 그 두 성분이다. $$d$$가 좌표 무관이고 $$(p,q)$$-분해가 좌표 무관이므로 ([§거의 복소구조, ⁋명제 7](/ko/math/complex_geometry/almost_complex_structures#prop7)), 두 성분으로 추출한 $$\partial$$와 $$\bar\partial$$도 좌표에 무관하다. 다음 명제가 이 관점을 정식화한다.

<div class="proposition" markdown="1">

<ins id="prop2">**명제 2**</ins> 복소다양체 $$X$$ 위에서 외미분은 $$\Omega^{p,q}(X)$$ 위에서

$$
d = \partial + \bar\partial
$$

로 분해된다. 곧 임의의 $$(p,q)$$-형식 $$\omega$$에 대하여 $$d\omega$$의 $$(p+1,q)$$-성분은 $$\partial\omega$$, $$(p,q+1)$$-성분은 $$\bar\partial\omega$$이며, 다른 차수의 성분은 없다.

</div>

<details class="proof" markdown="1">
<summary>증명</summary>

$$X$$가 복소다양체이므로 그 표준 거의 복소구조는 적분가능하고 ([§거의 복소구조, ⁋정리 12](/ko/math/complex_geometry/almost_complex_structures#thm12)), 따라서 $$d(\Omega^{1,0}) \subseteq \Omega^{2,0} \oplus \Omega^{1,1}$$이 성립한다 ([§거의 복소구조, ⁋명제 11](/ko/math/complex_geometry/almost_complex_structures#prop11)의 동치조건 (3)). 켤레를 취하면 $$d(\Omega^{0,1}) \subseteq \Omega^{1,1} \oplus \Omega^{0,2}$$도 성립한다.

이제 국소좌표에서 $$\omega = \sum_{I,J} f_{IJ}\, dz_I \wedge d\bar{z}_J$$를 미분하자. $$d$$는 antiderivation이고 $$dz_j, d\bar{z}_j$$가 닫혀 있으므로

$$
d\omega = \sum_{I,J} df_{IJ} \wedge dz_I \wedge d\bar{z}_J
$$

이다. 함수 $$f_{IJ}$$에 대하여 $$df_{IJ} = \partial f_{IJ} + \bar\partial f_{IJ}$$이고, 여기서 $$\partial f_{IJ} = \sum_k (\partial f_{IJ}/\partial z_k)\, dz_k$$는 $$(1,0)$$-형식, $$\bar\partial f_{IJ} = \sum_k (\partial f_{IJ}/\partial \bar{z}_k)\, d\bar{z}_k$$는 $$(0,1)$$-형식이다. 위 표현에서 $$dz_I \wedge d\bar z_J$$가 차수 $$(p,q)$$이므로, $$\partial f_{IJ}$$를 wedge한 항은 정확히 $$(p+1,q)$$-형식이고 이들의 합이 [정의 1](#def1)의 $$\partial\omega$$이다. 마찬가지로 $$\bar\partial f_{IJ}$$를 wedge한 항은 $$(p,q+1)$$-형식이고 그 합이 $$\bar\partial\omega$$이다. 다른 차수의 항은 나타나지 않으므로 $$d\omega = \partial\omega + \bar\partial\omega$$이고 분해가 차수별로 성립한다.

</details>

이 분해는 본질적으로 $$X$$의 적분가능성에 의존한다. 적분가능하지 않은 거의 복소다양체에서는 $$d$$가 $$(p,q)$$-형식을 네 개의 차수 $$(p+2,q-1), (p+1,q), (p,q+1), (p-1,q+2)$$로 흩뜨려 $$d = \mu + \partial + \bar\partial + \bar\mu$$ 꼴이 되며, 두 여분의 항 $$\mu, \bar\mu$$가 정확히 Nijenhuis 텐서를 담는다. 복소다양체에서는 이 여분 항이 소멸하여 깔끔한 두 항 분해가 살아남고, 비로소 $$\bar\partial$$만으로 닫힌 복합체를 세울 수 있다.

## $$\partial$$와 $$\bar\partial$$의 멱영성

$$d = \partial + \bar\partial$$ 분해에 $$d^2 = 0$$을 대입하면 세 항이 차수별로 갈라져 각각 소멸해야 한다. 이것이 Dolbeault 복합체의 토대이다.

<div class="proposition" markdown="1">

<ins id="prop3">**명제 3**</ins> 복소다양체 $$X$$ 위에서 다음이 성립한다.

$$
\partial^2 = 0, \qquad \bar\partial^2 = 0, \qquad \partial \bar\partial + \bar\partial \partial = 0.
$$

</div>

<details class="proof" markdown="1">
<summary>증명</summary>

외미분은 $$d^2 = 0$$을 만족한다 ([\[미분다양체\] §미분형식, ⁋정리 2](/ko/math/manifolds/differential_forms#thm2)). [명제 2](#prop2)에 의해 $$(p,q)$$-형식 $$\omega$$에 대하여 $$d = \partial + \bar\partial$$이므로

$$
0 = d^2 \omega = (\partial + \bar\partial)(\partial + \bar\partial)\omega = \partial^2 \omega + (\partial\bar\partial + \bar\partial\partial)\omega + \bar\partial^2 \omega
$$

이다. 우변의 세 항은 각각 차수 $$(p+2,q)$$, $$(p+1,q+1)$$, $$(p,q+2)$$의 형식이다. 서로 다른 차수의 형식들의 합이 $$0$$이 되려면 각 차수의 성분이 따로 $$0$$이어야 하므로 ([명제 2](#prop2)와 같은 $$(p,q)$$-분해의 직합성에 의해),

$$
\partial^2 \omega = 0, \qquad (\partial\bar\partial + \bar\partial\partial)\omega = 0, \qquad \bar\partial^2 \omega = 0
$$

이 모든 $$\omega$$에 대해 성립한다. 따라서 $$\partial^2 = 0$$, $$\bar\partial^2 = 0$$, $$\partial\bar\partial + \bar\partial\partial = 0$$이다.

</details>

세 항등식 중 $$\bar\partial^2 = 0$$이 우리에게 직접 쓰이는 것으로, 이것이 $$\bar\partial$$를 미분으로 갖는 복합체를 가능하게 한다. 관계식 $$\partial\bar\partial = -\bar\partial\partial$$는 두 연산자가 반가환함을, 곧 $$(p,q)$$-형식의 격자 위에서 $$\partial$$(가로 방향)와 $$\bar\partial$$(세로 방향)가 만드는 사각형이 부호를 바꿔 닫힘을 뜻한다. 아래 그림은 이 이중복합체(double complex) 구조의 한 조각을 보여준다.

![Dolbeault 이중복합체의 (p,q) 격자 한 조각: 가로 del, 세로 del-bar 화살표와 반가환 사각형](/assets/images/Math/Complex_Geometry/Dolbeault_Cohomology-1.svg){:style="width:13.45em" class="invert" .align-center}

각 $$p$$를 고정하고 $$q$$만 변화시키면, 세로 방향 화살표들만 모아 $$\bar\partial^2 = 0$$인 복합체를 얻는다. 이것이 Dolbeault 복합체이다.

## Dolbeault 코호몰로지

고정된 $$p$$에 대하여 $$\bar\partial$$는 $$\Omega^{p,q}$$들을 $$q$$에 대해 한 칸씩 밀어 올리며 $$\bar\partial^2 = 0$$을 만족하므로, 이들은 cochain complex를 이룬다.

<div class="definition" markdown="1">

<ins id="def4">**정의 4**</ins> 복소다양체 $$X$$와 고정된 정수 $$p \geq 0$$에 대하여, $$\bar\partial$$를 미분으로 갖는 cochain complex

$$
0 \longrightarrow \Omega^{p,0}(X) \xrightarrow{\ \bar\partial\ } \Omega^{p,1}(X) \xrightarrow{\ \bar\partial\ } \Omega^{p,2}(X) \xrightarrow{\ \bar\partial\ } \cdots
$$

를 *Dolbeault complex<sub>Dolbeault 복합체</sub>*라 한다. 그 $$q$$번째 코호몰로지

$$
H^{p,q}_{\bar\partial}(X) = \frac{\ker\left( \bar\partial : \Omega^{p,q}(X) \to \Omega^{p,q+1}(X) \right)}{\Img\left( \bar\partial : \Omega^{p,q-1}(X) \to \Omega^{p,q}(X) \right)}
$$

를 $$X$$의 *Dolbeault cohomology<sub>Dolbeault 코호몰로지</sub>*라 한다. 그 복소차원 $$h^{p,q}(X) = \dim_{\mathbb{C}} H^{p,q}_{\bar\partial}(X)$$를 *Hodge number<sub>Hodge 수</sub>*라 한다.

</div>

$$\bar\partial\omega = 0$$인 형식을 *$$\bar\partial$$-닫힌<sub>$$\bar\partial$$-closed</sub>* 형식, $$\omega = \bar\partial\eta$$ 꼴인 형식을 *$$\bar\partial$$-완전<sub>$$\bar\partial$$-exact</sub>* 형식이라 한다. Dolbeault 코호몰로지는 $$\bar\partial$$-닫힌 형식을 $$\bar\partial$$-완전 형식으로 나눈 것이며, de Rham 코호몰로지가 $$d$$에 대해 측정하는 것과 같은 종류의 양을 $$\bar\partial$$에 대해 측정한다. 분모와 분자가 모두 잘 정의됨은 $$\bar\partial^2 = 0$$에서 따라온다. 곧 완전형식 $$\bar\partial\eta$$는 $$\bar\partial(\bar\partial\eta) = 0$$이므로 항상 닫혀 있어, $$\Img \subseteq \ker$$이고 몫이 의미를 가진다.

$$p = 0$$인 경우가 가장 기본적이다. $$\Omega^{0,0}(X)$$는 매끄러운 복소함수 전체이고, 함수 $$f$$가 $$\bar\partial f = 0$$을 만족하는 것은 모든 좌표에서 $$\partial f/\partial \bar{z}_k = 0$$, 곧 Cauchy–Riemann 방정식이 성립하는 것이므로 $$f$$가 정칙함수임과 동치이다. 따라서

$$
H^{0,0}_{\bar\partial}(X) = \ker\left( \bar\partial : \Omega^{0,0}(X) \to \Omega^{0,1}(X) \right) = \mathcal{O}(X)
$$

로 전역 정칙함수의 공간이 된다. $$X$$가 콤팩트 연결이면 이는 $$\mathbb{C}$$이다 ([§복소다양체, ⁋정리 14](/ko/math/complex_geometry/complex_manifolds#thm14)). 더 높은 $$q$$에서는 $$\bar\partial$$-방정식의 풀이가능성이 비자명한 정보가 되며, 이 정보가 정확히 정칙형식 층의 코호몰로지로 해석된다는 것이 이 글의 주된 결과이다. 그 다리를 놓는 국소 보조정리부터 세운다.

## $$\bar\partial$$-Poincaré 보조정리

de Rham 이론에서 Poincaré 보조정리는 볼록영역에서 닫힌형식이 완전함을 말하며, 이로부터 de Rham 복합체가 상수층의 fine resolution이 된다. $$\bar\partial$$에 대한 대응물은 폴리디스크에서 $$\bar\partial$$-닫힌 형식($$q \geq 1$$)이 $$\bar\partial$$-완전하다는 것으로, 이를 Dolbeault–Grothendieck 보조정리라 한다. 그 핵심은 한 변수 $$\bar\partial$$-방정식 $$\partial u/\partial\bar{z} = f$$를 Cauchy 적분으로 푸는 것이며, 변수 개수에 대한 귀납으로 일반 차원에 도달한다. 우선 한 변수의 비균질 Cauchy–Riemann 방정식을 다룬다.

<div class="proposition" markdown="1">

<ins id="lem5">**보조정리 5 (한 변수 $$\bar\partial$$-문제)**</ins> $$f$$가 닫힌원판 $$\overline{D} = \{ \zeta \in \mathbb{C} \mid \lvert \zeta \rvert \leq r \}$$의 근방에서 정의된 매끄러운 복소함수라 하자. 그러면

$$
u(\zeta) = \frac{1}{2\pi i} \int_{D} \frac{f(w)}{w - \zeta}\, dw \wedge d\bar{w}
$$

로 정의되는 함수 $$u$$는 $$D$$의 내부에서 매끄럽고

$$
\frac{\partial u}{\partial \bar{\zeta}} = f
$$

를 만족한다.

</div>

<details class="proof" markdown="1">
<summary>증명</summary>

적분의 분모에 $$w = \zeta$$에서 특이점이 있으나 $$1/(w-\zeta)$$가 국소적분가능하므로 ($$dw \wedge d\bar{w} = -2i\, dx\, dy$$를 극좌표로 보면 $$1/\lvert w - \zeta\rvert$$의 적분은 수렴) $$u$$는 잘 정의된다. 변수치환 $$w = \zeta + s$$로 특이점을 적분기호 밖으로 옮기면

$$
u(\zeta) = \frac{1}{2\pi i} \int \frac{f(\zeta + s)}{s}\, ds \wedge d\bar{s}
$$

이고, 이제 피적분함수의 $$\zeta$$-의존성이 매끄러운 $$f(\zeta + s)$$에만 있으므로 적분기호 아래에서 미분할 수 있다. $$\partial/\partial\bar\zeta$$를 적용하면

$$
\frac{\partial u}{\partial \bar{\zeta}}(\zeta) = \frac{1}{2\pi i} \int \frac{1}{s}\, \frac{\partial f}{\partial \bar{\zeta}}(\zeta + s)\, ds \wedge d\bar{s} = \frac{1}{2\pi i} \int_{D} \frac{1}{w - \zeta}\, \frac{\partial f}{\partial \bar{w}}(w)\, dw \wedge d\bar{w}
$$

이다 (다시 $$s = w - \zeta$$로 되돌리고 $$\partial f(\zeta+s)/\partial\bar\zeta = (\partial f/\partial\bar w)(\zeta+s)$$를 썼다). 이제 일반화된 Cauchy 적분공식을 적용한다. 매끄러운 함수 $$g$$와 영역 $$D$$에 대하여 Cauchy–Pompeiu 공식

$$
g(\zeta) = \frac{1}{2\pi i} \int_{\partial D} \frac{g(w)}{w - \zeta}\, dw + \frac{1}{2\pi i} \int_{D} \frac{1}{w - \zeta}\, \frac{\partial g}{\partial \bar{w}}\, dw \wedge d\bar{w}
$$

가 성립한다 (이는 Stokes 정리를 $$g(w)/(w-\zeta)$$의 미분형식에 적용해 얻는다). 이 공식을 $$g = f$$에 쓰면 우변 둘째 항이 위에서 계산한 $$\partial u/\partial\bar\zeta$$와 정확히 같다. 한편 $$D$$를 충분히 키워 $$f$$의 지지를 포함하는 더 큰 원판으로 두거나, 국소적으로 $$f$$에 차단함수를 곱해 컴팩트 지지로 만들면 경계적분 $$\int_{\partial D} f(w)/(w-\zeta)\, dw$$가 사라지도록 할 수 있고, 이때 $$\partial u/\partial\bar\zeta = f$$가 따라온다. 차단으로 바뀐 부분은 $$\zeta$$가 차단 영역 안쪽에 있는 한 $$f$$를 바꾸지 않으므로 국소적으로 원하는 등식이 성립한다.

</details>

이 한 변수 풀이를 변수 개수에 대한 귀납으로 끌어올리면 폴리디스크 전체에서의 결과를 얻는다. 표기를 위해 폴리디스크를 $$\Delta = \{ z \in \mathbb{C}^n \mid \lvert z_j \rvert < r_j \}$$로 적는다.

<div class="proposition" markdown="1">

<ins id="lem6">**보조정리 6 ($$\bar\partial$$-Poincaré 보조정리, Dolbeault–Grothendieck)**</ins> 폴리디스크 $$\Delta \subseteq \mathbb{C}^n$$ 위에서 $$q \geq 1$$이고 $$\omega \in \Omega^{p,q}(\Delta)$$가 $$\bar\partial\omega = 0$$이면, $$\eta \in \Omega^{p,q-1}(\Delta)$$가 존재하여 $$\omega = \bar\partial\eta$$이다. 따라서 $$q \geq 1$$에 대하여 $$H^{p,q}_{\bar\partial}(\Delta) = 0$$이다.

</div>

<details class="proof" markdown="1">
<summary>증명</summary>

$$p$$는 계산에 관여하지 않으므로 ($$dz_I$$ 인자는 $$\bar\partial$$를 통과해 그대로 남는다) $$p = 0$$인 경우를 보이면 충분하다. 증명은 $$\omega$$에 나타나는 $$d\bar{z}_k$$의 인덱스가 처음 몇 개 $$\{1, \ldots, m\}$$에만 들어 있는가에 대한 귀납으로 한다. 곧 $$\omega$$가 $$d\bar{z}_1, \ldots, d\bar{z}_m$$만 포함한다고 가정하고 $$m$$에 대해 귀납한다. $$m < q$$이면 $$\omega = 0$$이므로 자명하고, 귀납의 출발은 $$m = q$$이다.

$$(0,1)$$-형식의 경우, 곧 $$q = 1$$이고 $$\omega = \sum_{k=1}^n f_k\, d\bar{z}_k$$를 먼저 다루어 논법의 골격을 드러낸다. $$\bar\partial\omega = 0$$은 모든 $$k, l$$에 대하여

$$
\frac{\partial f_k}{\partial \bar{z}_l} = \frac{\partial f_l}{\partial \bar{z}_k}
$$

를 뜻한다. 형식이 $$d\bar{z}_1, \ldots, d\bar{z}_m$$만 포함한다는 귀납가정 아래에서, $$g$$를

$$
g(z) = \frac{1}{2\pi i} \int \frac{f_m(z_1, \ldots, z_{m-1}, w, z_{m+1}, \ldots, z_n)}{w - z_m}\, dw \wedge d\bar{w}
$$

로 정의하자. 곧 [보조정리 5](#lem5)의 한 변수 풀이를 $$m$$번째 변수에 적용한 것이다. 그러면 $$\partial g/\partial\bar{z}_m = f_m$$이다. 한편 $$l > m$$인 변수에 대해서는 $$f_m$$이 그 변수에 대해 정칙($$\partial f_m/\partial\bar{z}_l = 0$$, 형식에 $$d\bar z_l$$이 없으므로 닫힘조건에서 따라온다)이므로 적분기호 아래 미분으로 $$\partial g/\partial\bar{z}_l = 0$$ ($$l > m$$)이다. 이제

$$
\omega' = \omega - \bar\partial g
$$

를 보면, $$\bar\partial g = \sum_l (\partial g/\partial\bar{z}_l)\, d\bar{z}_l$$의 $$m$$번째 성분이 $$f_m$$과 정확히 상쇄되어 $$\omega'$$에는 $$d\bar{z}_m$$ 항이 없고, $$l > m$$ 성분도 추가되지 않으므로 $$\omega'$$는 $$d\bar{z}_1, \ldots, d\bar{z}_{m-1}$$만 포함한다. 또 $$\bar\partial\omega' = \bar\partial\omega - \bar\partial^2 g = 0$$이므로 $$\omega'$$도 $$\bar\partial$$-닫혀 있다. 귀납가정에 의해 $$\omega' = \bar\partial h$$인 $$h$$가 존재하고, 따라서

$$
\omega = \omega' + \bar\partial g = \bar\partial(h + g)
$$

로 $$\bar\partial$$-완전하다.

$$q \geq 2$$의 일반 경우도 같은 귀납이 작동한다. $$\omega$$를 $$\omega = d\bar{z}_m \wedge \alpha + \beta$$로 쓰되 $$\alpha, \beta$$가 $$d\bar{z}_m$$을 포함하지 않게 분해하고, $$\alpha$$의 각 계수에 위와 같이 $$m$$번째 변수의 Cauchy 적분을 적용해 만든 형식 $$\gamma$$로 $$\omega - \bar\partial\gamma$$에서 $$d\bar{z}_m$$ 항을 모두 제거한다. $$\bar\partial$$-닫힘조건이 이 제거 후에도 $$l > m$$ 인덱스가 다시 생기지 않도록 보장하므로, 포함된 인덱스 집합이 $$\{1, \ldots, m-1\}$$로 줄어든 닫힌형식을 얻고 귀납가정을 적용한다. $$m = q$$에서 시작해 $$m$$을 하나씩 줄여 $$m < q$$에 이르면 형식이 $$0$$이 되어 귀납이 끝난다.

엄밀히는 [보조정리 5](#lem5)가 닫힌원판 근방에서의 풀이를 주므로, 폴리디스크 $$\Delta$$ 전체에서의 결과를 얻으려면 $$\Delta$$를 안쪽 폴리디스크들의 증가열로 소진하고 각 단계의 풀이를 이어 붙이는 극한 논법이 필요하다. 각 콤팩트 부분폴리디스크에서 위 구성이 풀이를 주고, Mittag-Leffler 형 수렴 논법으로 전역 풀이로 이어붙이면 $$\Delta$$ 위의 $$\eta$$를 얻는다.

</details>

이 보조정리는 $$\bar\partial$$-코호몰로지가 순전히 국소적으로는 자명함을 말한다. 폴리디스크 위에서는 모든 $$\bar\partial$$-닫힌 형식($$q \geq 1$$)이 완전하므로 $$H^{p,q}_{\bar\partial}(\Delta) = 0$$이고, $$q = 0$$ 부분만 정칙 $$p$$-형식으로 살아남는다. 따라서 대역적인 $$H^{p,q}_{\bar\partial}(X)$$의 비자명함은 국소 정보가 아니라 폴리디스크들을 이어 붙이는 대역적 방식, 곧 위상에서 온다. 이 국소 자명성과 대역 비자명성의 간극을 정확히 재는 장치가 층 코호몰로지이며, 그 일치가 Dolbeault 정리이다.

## Dolbeault 정리

매끄러운 다양체에서 de Rham 정리는 de Rham 복합체가 상수층 $$\underline{\mathbb{R}}$$의 acyclic resolution임을 써서 de Rham 코호몰로지를 층 코호몰로지와 동일시했다. 복소다양체에서는 같은 추상 de Rham 논법이 $$\bar\partial$$-복합체에 적용되어, 정칙 $$p$$-형식의 층을 분해한다. 먼저 분해할 층을 정한다.

<div class="definition" markdown="1">

<ins id="def7">**정의 7**</ins> 복소다양체 $$X$$ 위의 *holomorphic $$p$$-form<sub>정칙 $$p$$-형식</sub>*의 층 $$\Omega^p$$를, 각 열린집합 $$U \subseteq X$$에 대하여 $$U$$ 위의 정칙 $$(p,0)$$-형식

$$
\Omega^p(U) = \{ \omega \in \Omega^{p,0}(U) \mid \bar\partial\omega = 0 \}
$$

들로 정의되는 층이라 한다. 곧 국소적으로 $$\omega = \sum_{\lvert I \rvert = p} f_I\, dz_I$$이되 모든 계수 $$f_I$$가 정칙인 형식들의 층이다.

</div>

$$p = 0$$일 때 $$\Omega^0$$은 정칙함수의 구조층 $$\mathcal{O}_X$$이다. $$p = 1$$일 때 $$\Omega^1$$은 정칙 1-형식의 층으로, 정칙여접다발의 정칙 단면들이 이루는 층 ([§복소다양체, ⁋정의 11](/ko/math/complex_geometry/complex_manifolds#def11))이다. 조건 $$\bar\partial\omega = 0$$은 $$(p,0)$$-형식의 계수에 대한 Cauchy–Riemann 방정식이며, 정의에 의해 $$\Omega^p = \ker(\bar\partial : \Omega^{p,0} \to \Omega^{p,1})$$로 $$\bar\partial$$-닫힌 $$(p,0)$$-형식들의 층이다. 이 층의 층 코호몰로지 $$H^q(X, \Omega^p)$$ ([\[대수다양체\] §층 코호몰로지, ⁋정의 1](/ko/math/algebraic_varieties/sheaf_cohomology#def1))가 Dolbeault 코호몰로지의 정체임을 보이려 한다.

추상 de Rham 논법의 핵심은 매끄러운 형식의 층 $$\mathcal{A}^{p,q}$$ (각 $$U$$에 $$\Omega^{p,q}(U)$$를 대응시키는 층)가 *fine sheaf<sub>미세층</sub>* 라는 점이다. 미세층은 임의의 열린덮개에 종속된 partition of unity를 가지는 층으로, 그러한 단위분할이 존재하면 그 층은 층 코호몰로지에서 acyclic하다. 매끄러운 함수의 단위분할이 $$\mathcal{A}^{p,q}$$의 단면에 그대로 곱해지므로 $$\mathcal{A}^{p,q}$$는 미세층이고, 따라서 모든 $$q' > 0$$에 대하여 $$H^{q'}(X, \mathcal{A}^{p,q}) = 0$$이다. 이제 $$\bar\partial$$-복합체가 $$\Omega^p$$의 분해임을 확인한다.

<div class="proposition" markdown="1">

<ins id="prop8">**명제 8**</ins> 복소다양체 $$X$$와 고정된 $$p \geq 0$$에 대하여, 층의 sequence

$$
0 \longrightarrow \Omega^p \longrightarrow \mathcal{A}^{p,0} \xrightarrow{\ \bar\partial\ } \mathcal{A}^{p,1} \xrightarrow{\ \bar\partial\ } \mathcal{A}^{p,2} \xrightarrow{\ \bar\partial\ } \cdots
$$

는 완전열이다. 곧 매끄러운 $$(p,q)$$-형식 층의 $$\bar\partial$$-복합체는 정칙 $$p$$-형식 층 $$\Omega^p$$의 분해이며, 각 $$\mathcal{A}^{p,q}$$가 미세층이므로 이는 fine resolution이다.

</div>

<details class="proof" markdown="1">
<summary>증명</summary>

완전성은 줄기(stalk) 수준에서, 곧 각 점의 임의로 작은 근방에서 확인하면 충분하다. 각 점은 폴리디스크 근방을 가지므로 [보조정리 6](#lem6)을 그러한 근방에서 쓸 수 있다.

먼저 $$\Omega^p \to \mathcal{A}^{p,0}$$의 위치에서의 완전성, 곧 $$\Omega^p = \ker(\bar\partial : \mathcal{A}^{p,0} \to \mathcal{A}^{p,1})$$이다. 이는 [정의 7](#def7) 그 자체이다. $$\Omega^p$$로의 사상은 포함사상이고, 정칙 $$(p,0)$$-형식이 정확히 $$\bar\partial$$로 죽는 매끄러운 $$(p,0)$$-형식이므로 이 위치에서 완전하다 ($$\Omega^p \to \mathcal{A}^{p,0}$$이 단사이고 그 상이 $$\bar\partial$$의 핵과 같다).

다음으로 $$q \geq 1$$에서 $$\ker(\bar\partial : \mathcal{A}^{p,q} \to \mathcal{A}^{p,q+1}) = \Img(\bar\partial : \mathcal{A}^{p,q-1} \to \mathcal{A}^{p,q})$$임을 보인다. 포함 $$\Img \subseteq \ker$$은 $$\bar\partial^2 = 0$$ ([명제 3](#prop3))에서 따라온다. 반대 포함을 줄기에서 본다. $$x \in X$$와 $$x$$ 근방의 $$\bar\partial$$-닫힌 $$(p,q)$$-형식 $$\omega$$의 줄기가 주어지면, $$x$$의 충분히 작은 폴리디스크 근방 $$\Delta$$를 잡아 $$\omega$$가 $$\Delta$$에서 정의된 $$\bar\partial$$-닫힌 형식이게 할 수 있다. [보조정리 6](#lem6)에 의해 $$\Delta$$에서 $$\omega = \bar\partial\eta$$인 $$\eta \in \mathcal{A}^{p,q-1}(\Delta)$$가 존재하므로, 줄기 수준에서 $$\omega$$는 $$\bar\partial$$의 상에 든다. 따라서 $$\ker \subseteq \Img$$이고 이 위치에서도 완전하다.

각 $$\mathcal{A}^{p,q}$$가 미세층임은 매끄러운 함수의 단위분할 $$\{\rho_i\}$$를 $$(p,q)$$-형식의 단면에 점별로 곱하는 연산 $$\omega \mapsto \rho_i\omega$$이 층사상이고 $$\sum_i \rho_i = 1$$을 주므로 따라온다. 따라서 sequence는 $$\Omega^p$$의 fine resolution이다.

</details>

미세층은 층 코호몰로지에서 acyclic하므로, 이 fine resolution으로부터 추상 de Rham 정리를 적용할 수 있다. 층 코호몰로지에서 acyclic resolution은 그 전역단면 복합체의 코호몰로지로 원래 층의 코호몰로지를 계산해 준다 ([\[대수다양체\] §층 코호몰로지, ⁋명제 17](/ko/math/algebraic_varieties/sheaf_cohomology#prop17)). 이를 위 분해에 적용하면 Dolbeault 정리가 나온다.

<div class="proposition" markdown="1">

<ins id="thm9">**정리 9 (Dolbeault)**</ins> 복소다양체 $$X$$와 정수 $$p, q \geq 0$$에 대하여, 표준적인 동형

$$
H^{p,q}_{\bar\partial}(X) \cong H^q(X, \Omega^p)
$$

이 성립한다. 곧 Dolbeault 코호몰로지는 정칙 $$p$$-형식 층의 $$q$$번째 층 코호몰로지와 일치한다.

</div>

<details class="proof" markdown="1">
<summary>증명</summary>

[명제 8](#prop8)에 의해

$$
0 \longrightarrow \Omega^p \longrightarrow \mathcal{A}^{p,0} \xrightarrow{\ \bar\partial\ } \mathcal{A}^{p,1} \xrightarrow{\ \bar\partial\ } \cdots
$$

는 $$\Omega^p$$의 분해이고, 각 $$\mathcal{A}^{p,q}$$는 미세층이라 $$\Gamma(X, -)$$-acyclic하다 (미세층은 모든 양의 차수 층 코호몰로지가 소멸한다). 따라서 이는 acyclic resolution이다.

acyclic resolution에 대한 추상 de Rham 정리 ([\[대수다양체\] §층 코호몰로지, ⁋명제 17](/ko/math/algebraic_varieties/sheaf_cohomology#prop17))는, $$0 \to \mathcal{F} \to \mathcal{A}^0 \to \mathcal{A}^1 \to \cdots$$이 $$\Gamma(X,-)$$-acyclic resolution이면

$$
H^q(X, \mathcal{F}) \cong \frac{\ker\left( \Gamma(X, \mathcal{A}^q) \to \Gamma(X, \mathcal{A}^{q+1}) \right)}{\Img\left( \Gamma(X, \mathcal{A}^{q-1}) \to \Gamma(X, \mathcal{A}^q) \right)}
$$

임을 준다. 우리 분해에 적용하면 $$\mathcal{F} = \Omega^p$$, $$\mathcal{A}^q = \mathcal{A}^{p,q}$$이고 전역단면은 $$\Gamma(X, \mathcal{A}^{p,q}) = \Omega^{p,q}(X)$$, 그 사이의 사상은 $$\bar\partial$$이다. 따라서

$$
H^q(X, \Omega^p) \cong \frac{\ker\left( \bar\partial : \Omega^{p,q}(X) \to \Omega^{p,q+1}(X) \right)}{\Img\left( \bar\partial : \Omega^{p,q-1}(X) \to \Omega^{p,q}(X) \right)} = H^{p,q}_{\bar\partial}(X)
$$

이다. 이 동형은 acyclic resolution이 유도하는 표준 사상이므로 자연스럽다.

</details>

Dolbeault 정리는 해석적으로 정의된 $$\bar\partial$$-코호몰로지를 층론적으로 정의된 $$H^q(X, \Omega^p)$$로 옮긴다. 이 일치 덕분에 두 세계의 도구를 자유로이 오갈 수 있다. 해석학 쪽에서는 $$\bar\partial$$-방정식의 풀이가능성으로 $$H^{p,q}$$의 소멸을 증명할 수 있고, 대수기하 쪽에서는 층 코호몰로지의 장치, 곧 긴 완전열·Serre 쌍대성·소멸정리 따위를 $$H^{p,q}$$에 그대로 쓸 수 있다. 특히 $$p = 0$$이면 $$H^{0,q}_{\bar\partial}(X) \cong H^q(X, \mathcal{O}_X)$$로, 구조층의 코호몰로지가 $$\bar\partial$$-코호몰로지로 계산된다.

## de Rham 코호몰로지와의 비교

복소다양체는 동시에 매끄러운 다양체이므로 복소계수 de Rham 코호몰로지 $$H^k_{\mathrm{dR}}(X, \mathbb{C})$$도 가진다. $$\Omega^k(X) \otimes \mathbb{C} = \bigoplus_{p+q=k} \Omega^{p,q}(X)$$라는 형식 수준의 분해가 있으므로, 코호몰로지 수준에서도

$$
H^k_{\mathrm{dR}}(X, \mathbb{C}) \cong \bigoplus_{p+q=k} H^{p,q}_{\bar\partial}(X)
$$

가 성립하기를 기대할 수 있다. 그러나 이 분해는 일반적인 복소다양체에서는 성립하지 않는다. 문제는 $$d = \partial + \bar\partial$$의 닫힘조건 $$d\omega = 0$$이 $$\partial\omega = 0$$과 $$\bar\partial\omega = 0$$을 따로 함의하지 않는다는 데 있다. $$d$$-닫힌 형식을 차수별로 쪼개면 각 조각이 $$\bar\partial$$-닫힌지가 보장되지 않으므로, $$d$$-코호몰로지류를 $$\bar\partial$$-코호몰로지류들로 자연히 분해할 수 없다.

이 분해가 성립하려면 $$X$$에 추가 구조가 필요하다. 적절한 추가 기하구조 아래에서는 위 직합 분해(Hodge 분해)와 더불어 $$H^{p,q}$$와 $$H^{q,p}$$ 사이의 켤레 대칭이 성립하며, 그 결과 de Rham Betti 수가 Hodge 수들의 합 $$b_k = \sum_{p+q=k} h^{p,q}$$로 쪼개진다. 일반적인 복소다양체에서는 이 등식이 깨지고 부등식 $$b_k \leq \sum_{p+q=k} h^{p,q}$$만 남는 것이 보통이다. 추가 구조가 무엇이고 그 아래에서 분해가 왜 성립하는지는 별도의 이론을 요구한다.

## 예시

가장 단순한 경우는 $$\mathbb{C}^n$$이며, $$\bar\partial$$-Poincaré 보조정리가 거의 모든 것을 소멸시킨다.

<div class="example" markdown="1">

<ins id="ex10">**예시 10 ($$\mathbb{C}^n$$의 Dolbeault 코호몰로지)**</ins> $$\mathbb{C}^n$$ 자체가 폴리디스크 (반지름 무한) 이므로 [보조정리 6](#lem6)이 적용되어, $$q \geq 1$$에 대하여

$$
H^{p,q}_{\bar\partial}(\mathbb{C}^n) = 0
$$

이다. $$q = 0$$인 경우 $$H^{p,0}_{\bar\partial}(\mathbb{C}^n)$$은 $$\bar\partial$$-닫힌 $$(p,0)$$-형식, 곧 정칙 $$p$$-형식의 공간 $$\Omega^p(\mathbb{C}^n)$$이며, 이는 정칙함수를 계수로 갖는 $$\sum_I f_I\, dz_I$$들로 이루어진 무한차원 공간이다. 특히 $$H^{0,0}_{\bar\partial}(\mathbb{C}^n) = \mathcal{O}(\mathbb{C}^n)$$은 전역 정칙함수 전체이다. $$\mathbb{C}^n$$이 콤팩트하지 않으므로 [§복소다양체, ⁋정리 14](/ko/math/complex_geometry/complex_manifolds#thm14)의 상수성은 적용되지 않고, 다항식을 비롯한 풍부한 정칙함수가 살아남는다.

</div>

콤팩트한 경우의 가장 기본적인 예는 복소차원 $$1$$의 Riemann 곡면이다. 차원이 $$1$$이므로 $$(p,q)$$는 $$p, q \in \{0, 1\}$$의 네 가지뿐이다.

<div class="example" markdown="1">

<ins id="ex11">**예시 11 (콤팩트 Riemann 곡면의 Hodge 수)**</ins> $$X$$를 genus $$g$$의 콤팩트 연결 Riemann 곡면이라 하자. 복소차원이 $$1$$이므로 Dolbeault 코호몰로지는 $$H^{0,0}, H^{1,0}, H^{0,1}, H^{1,1}$$의 넷이고, 그 Hodge 수는 다음과 같다.

먼저 $$H^{0,0}_{\bar\partial}(X) = \mathcal{O}(X) = \mathbb{C}$$이므로 $$h^{0,0} = 1$$이다 ([§복소다양체, ⁋정리 14](/ko/math/complex_geometry/complex_manifolds#thm14)에 의해 콤팩트 연결 복소다양체 위 정칙함수는 상수). 다음으로 $$H^{1,0}_{\bar\partial}(X)$$은 $$\bar\partial$$-닫힌 $$(1,0)$$-형식, 곧 전역 정칙 1-형식의 공간 $$\Omega^1(X)$$이다 (분모인 $$\bar\partial(\Omega^{1,-1}) $$는 차수가 음수라 없다). 콤팩트 Riemann 곡면 위 정칙 1-형식의 공간의 차원이 정확히 genus와 같다는 것은 Riemann 곡면론의 기본 사실로, 따라서 $$h^{1,0} = \dim_{\mathbb{C}} \Omega^1(X) = g$$이다. Dolbeault 정리로 $$h^{0,1} = \dim_{\mathbb{C}} H^1(X, \mathcal{O}_X)$$이고, Serre 쌍대성 $$H^1(X, \mathcal{O}_X) \cong H^0(X, \Omega^1)^\ast$$에 의해 $$h^{0,1} = h^{1,0} = g$$이다. 마지막으로 $$H^{1,1}_{\bar\partial}(X) \cong H^1(X, \Omega^1)$$이며, 이는 다시 Serre 쌍대성으로 $$H^0(X, \mathcal{O}_X)^\ast \cong \mathbb{C}$$와 동형이므로 $$h^{1,1} = 1$$이다.

정리하면 콤팩트 Riemann 곡면의 Hodge 수는 $$h^{0,0} = h^{1,1} = 1$$, $$h^{1,0} = h^{0,1} = g$$이다. 한편 위상적으로 $$X$$의 Betti 수는 $$b_0 = b_2 = 1$$, $$b_1 = 2g$$이므로, $$b_1 = h^{1,0} + h^{0,1} = 2g$$로 차수 $$1$$에서 Hodge 분해가 실제로 성립함을 확인할 수 있다. 곧 Riemann 곡면에서는 앞 절에서 일반적으로 깨진다고 한 분해가 회복되며, 이는 복소차원 $$1$$ 콤팩트 복소다양체가 갖추는 추가 기하구조의 한 귀결이다.

</div>

이 두 예시는 Dolbeault 코호몰로지의 두 얼굴을 보여준다. $$\mathbb{C}^n$$에서는 $$\bar\partial$$-Poincaré가 모든 고차 코호몰로지를 죽여 순전히 국소적인 정칙형식만 남고, 콤팩트 곡면에서는 콤팩트성과 Serre 쌍대성이 맞물려 Hodge 수가 genus라는 위상적 불변량으로 결정된다. 전자는 국소 자명성을, 후자는 대역적 강성을 대표한다. 일반 차원의 콤팩트 복소다양체에서 Hodge 수들이 만드는 대칭과 그 위상적 의미는 추가 기하구조를 갖춘 다양체에서 비로소 온전히 드러난다.

---

**참고문헌**

**[Huybrechts]** D. Huybrechts, *Complex Geometry: An Introduction*, Springer, 2005.

**[Griffiths–Harris]** P. Griffiths and J. Harris, *Principles of Algebraic Geometry*, Wiley, 1978.

**[Wells]** R. O. Wells, *Differential Analysis on Complex Manifolds*, 3rd ed., Springer, 2008.

**[Voisin]** C. Voisin, *Hodge Theory and Complex Algebraic Geometry I*, Cambridge University Press, 2002.

**[Hörmander]** L. Hörmander, *An Introduction to Complex Analysis in Several Variables*, 3rd ed., North-Holland, 1990.
