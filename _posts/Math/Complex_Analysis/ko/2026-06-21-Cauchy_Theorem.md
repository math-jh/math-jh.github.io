---
title: "Cauchy 정리"
description: "f가 정칙이면 임의의 삼각형 경계에서 적분이 0이 된다는 Goursat 정리를 변의 이등분 반복으로 증명하고, 이로부터 볼록·star-shaped 영역에서 정칙함수가 원시함수를 가져 닫힌 경로 적분이 소멸함을 보인다. homotopy 불변성으로 확장하여 단순연결 영역에서 정칙함수의 닫힌 경로 적분이 0임을 확립하고 회전수를 정의한다."
excerpt: "Goursat 정리, 삼각형 이등분, star-shaped 영역, 원시함수, homotopy 불변, 단순연결, 회전수"

categories: [Math / Complex Analysis]
permalink: /ko/math/complex_analysis/cauchy_theorem
sidebar: 
    nav: "complex_analysis-ko"

date: 2026-06-21
weight: 4

published: false
---

복소적분 이론은 ([§복소적분](/ko/math/complex_analysis/complex_integration)) 원시함수를 갖는 함수의 닫힌 경로 적분이 $$0$$임을 알려 주었지만, 원시함수의 존재 자체는 손으로 확인해야 하는 별개의 문제로 남겨 두었다. Cauchy 정리는 이 빈틈을 메운다. 정칙성이라는 국소적 미분 조건만으로 닫힌 경로 적분의 소멸이라는 전역적 결론이 따라 나온다는 것이 그 내용이며, 복소해석학의 거의 모든 깊은 정리가 이 한 사실에서 갈라져 나온다. 출발점은 Goursat의 정리로, 정칙함수의 삼각형 경계 적분이 $$0$$임을 도함수의 연속성조차 가정하지 않고 순수하게 적분의 어림만으로 증명한다. 여기에서 볼록한 영역 위 원시함수의 구성이 따라 나오고, 영역의 위상을 들여오면 적분이 경로의 연속적 변형에 무관하다는 homotopy 불변성으로 확장된다. 끝으로 닫힌 경로가 한 점을 몇 번 감는지를 세는 회전수를 정의하여, 적분과 위상을 잇는 다리를 놓는다.

## Goursat 정리

복소적분에서 닫힌 경로 적분의 소멸을 끌어내는 가장 약한 출발점은, 정칙함수를 가장 단순한 닫힌 경로인 삼각형의 경계 위에서 적분하는 것이다. 놀라운 점은 이 적분이 항상 $$0$$이며, 그 증명에 도함수 $$f'$$의 연속성이나 Cauchy–Riemann 방정식의 정칙성 판정조차 필요하지 않다는 사실이다. 복소미분가능성의 정의 ([§정칙함수, ⁋정의 1](/ko/math/complex_analysis/holomorphic_functions#def1)) 가 주는 한 점에서의 일차 근사만으로 충분하다. 삼각형이라 함은 평면의 세 점 $$a, b, c$$가 이루는 닫힌 삼각형 영역을 가리키며, 그 경계 $$\partial T$$는 $$a \to b \to c \to a$$를 잇는 세 선분을 이어붙인 닫힌 곡선으로, piecewise $$C^1$$ 곡선 ([§복소적분, ⁋정의 1](/ko/math/complex_analysis/complex_integration#def1)) 이다.

<div class="proposition" markdown="1">

<ins id="thm1">**정리 1 (Goursat)**</ins> $$\Omega \subseteq \mathbb{C}$$가 열린집합이고 $$f$$가 $$\Omega$$에서 정칙이라 하자. 삼각형 $$T$$가 그 내부와 경계를 모두 포함하여 $$\Omega$$에 들어 있으면, 그 경계를 따른 적분은

$$\oint_{\partial T} f(z)\,dz = 0$$

이다.

</div>

<details class="proof" markdown="1">
<summary>증명</summary>

적분값의 크기를 $$I = \bigl\lvert \oint_{\partial T} f\,dz \bigr\rvert$$이라 두고, 삼각형을 반복하여 잘게 쪼개면서 $$I$$가 임의로 작아짐을 보인다.

**이등분.** 주어진 삼각형 $$T = T^{(0)}$$의 세 변의 중점을 이으면 $$T$$가 네 개의 합동인 작은 삼각형 $$T_1, T_2, T_3, T_4$$로 나뉜다. 가운데 삼각형의 경계는 바깥 세 삼각형의 변과 방향이 반대인 변을 공유하므로, 네 작은 삼각형의 경계 적분을 모두 더하면 내부 변에서의 적분이 상쇄되고 바깥 경계 $$\partial T$$의 적분만 남는다 ([§복소적분, ⁋명제 4](/ko/math/complex_analysis/complex_integration#prop4)의 역방향·이어붙이기 성질). 곧

$$\oint_{\partial T} f\,dz = \sum_{j=1}^{4} \oint_{\partial T_j} f\,dz$$

이다. 삼각부등식에 의해 적어도 한 $$j$$에 대해 $$\bigl\lvert \oint_{\partial T_j} f\,dz \bigr\rvert \geq \tfrac14 I$$이며, 그러한 삼각형 하나를 골라 $$T^{(1)}$$이라 한다.

**반복.** 같은 이등분을 되풀이하면, 삼각형의 감소열 $$T^{(0)} \supseteq T^{(1)} \supseteq T^{(2)} \supseteq \cdots$$이 얻어지고 각 단계에서

$$\left\lvert \oint_{\partial T^{(n)}} f\,dz \right\rvert \geq \frac{1}{4^n}\,I$$

이다. 한편 한 번 이등분할 때마다 둘레와 직경이 절반으로 줄므로, $$L = \mathrm{length}(\partial T^{(0)})$$, $$d = \operatorname{diam}(T^{(0)})$$이라 하면

$$\mathrm{length}(\partial T^{(n)}) = \frac{L}{2^n}, \qquad \operatorname{diam}(T^{(n)}) = \frac{d}{2^n}$$

이다. 삼각형들은 콤팩트이고 직경이 $$0$$으로 줄어드는 감소열이므로, 그 교집합은 단 한 점 $$z_0 = \bigcap_n T^{(n)}$$로 이루어지며 $$z_0 \in T \subseteq \Omega$$이다.

**$$z_0$$에서의 일차 근사.** $$f$$가 $$z_0$$에서 복소미분가능하므로, 임의의 $$\varepsilon > 0$$에 대해 $$\delta > 0$$이 있어 $$\lvert z - z_0\rvert < \delta$$이면

$$f(z) = f(z_0) + f'(z_0)(z - z_0) + r(z), \qquad \lvert r(z)\rvert \leq \varepsilon\,\lvert z - z_0\rvert$$

이다 (이는 차분비의 극한 정의를 풀어 쓴 것이다). $$n$$이 충분히 크면 $$\operatorname{diam}(T^{(n)}) = d/2^n < \delta$$이므로 $$T^{(n)}$$ 전체가 $$z_0$$의 $$\delta$$-근방에 들어간다. 그런데 일차다항식 $$z \mapsto f(z_0) + f'(z_0)(z - z_0)$$은 평면 전체에서 원시함수 $$f(z_0)z + \tfrac12 f'(z_0)(z - z_0)^2$$을 가지므로, 닫힌 경로 $$\partial T^{(n)}$$에서의 적분이 $$0$$이다 ([§복소적분, ⁋따름정리 9](/ko/math/complex_analysis/complex_integration#cor9)). 따라서

$$\oint_{\partial T^{(n)}} f\,dz = \oint_{\partial T^{(n)}} r(z)\,dz$$

이고, ML 부등식 ([§복소적분, ⁋명제 6](/ko/math/complex_analysis/complex_integration#prop6)) 을 적용하면 $$\partial T^{(n)}$$ 위에서 $$\lvert r(z)\rvert \leq \varepsilon\,\lvert z - z_0\rvert \leq \varepsilon\,\operatorname{diam}(T^{(n)}) = \varepsilon d/2^n$$이므로

$$\left\lvert \oint_{\partial T^{(n)}} f\,dz \right\rvert \leq \varepsilon\,\frac{d}{2^n} \cdot \mathrm{length}(\partial T^{(n)}) = \varepsilon\,\frac{d}{2^n}\cdot\frac{L}{2^n} = \frac{\varepsilon\, dL}{4^n}$$

이다.

**결론.** 두 어림을 합치면 $$\tfrac{1}{4^n} I \leq \tfrac{1}{4^n}\varepsilon dL$$, 곧 $$I \leq \varepsilon dL$$이다. $$\varepsilon > 0$$이 임의였고 $$d, L$$은 고정된 상수이므로 $$I = 0$$, 곧 $$\oint_{\partial T} f\,dz = 0$$이다.

</details>

Goursat 정리의 증명은 정칙성을 오직 한 점 $$z_0$$에서의 일차 근사로만 사용한다는 점에서 인상적이다. 적분을 잘게 쪼개면 각 조각 위에서 $$f$$가 거의 일차함수처럼 보이고, 일차함수는 원시함수를 가지므로 그 조각의 기여가 무시할 만큼 작아진다. 둘레와 직경이 각각 $$2^{-n}$$로 줄어 그 곱이 $$4^{-n}$$로 줄고, 이것이 적분값의 하한 $$4^{-n}I$$와 정확히 같은 비율로 상쇄되어 $$I = 0$$을 강제한다. 이 정리에서 삼각형을 직사각형이나 다른 다각형으로 바꿔도 같은 증명이 통하며, 실제로 다각형 영역을 삼각형으로 분할하면 임의의 다각형 경계로 즉시 확장된다.

## 볼록 영역에서의 원시함수와 Cauchy 정리

Goursat 정리는 삼각형이라는 특정 경로에 대한 진술이지만, 영역이 적당히 좋으면 이로부터 그 영역 위 정칙함수가 원시함수를 가짐을 끌어낼 수 있다. 핵심 발상은 고정된 한 점에서 $$z$$까지 선분을 따라 적분하여 원시함수 후보 $$F(z)$$를 만들고, 그 차분비를 작은 삼각형 위의 적분으로 표현한 뒤 Goursat 정리를 쓰는 것이다. 이 구성이 작동하려면 영역 안의 임의의 점을 기준점과 선분으로 이을 수 있어야 하며, 그 선분이 만드는 삼각형도 영역에 들어 있어야 한다. 이를 보장하는 가장 단순한 조건이 별모양성이다.

<div class="definition" markdown="1">

<ins id="def2">**정의 2**</ins> 영역 $$\Omega \subseteq \mathbb{C}$$가 *star-shaped<sub>별모양</sub>*라는 것은, 어떤 점 $$z_\ast \in \Omega$$이 있어 임의의 $$z \in \Omega$$에 대하여 $$z_\ast$$와 $$z$$를 잇는 선분 $$[z_\ast, z] = \{(1-t)z_\ast + tz \mid t \in [0, 1]\}$$이 통째로 $$\Omega$$에 들어 있는 것이다. 이러한 $$z_\ast$$를 $$\Omega$$의 *star center<sub>별중심</sub>*라 한다.

</div>

직관적으로 별모양 영역이란 어떤 한 점에서 영역 전체가 "보이는" 영역, 곧 그 점에서 임의의 점으로 똑바로 선을 그어도 영역 밖으로 나가지 않는 영역이다. 임의의 *convex<sub>볼록</sub>* 영역(임의의 두 점을 잇는 선분이 영역에 들어 있는 영역)은 모든 점이 별중심이 되므로 star-shaped이다. 가령 열린 원판이나 평면 전체, 또는 한 직선을 떼어 낸 반평면이 그러하다. 반면 원점을 뺀 평면 $$\mathbb{C}\setminus\{0\}$$은 별모양이 아닌데, 어떤 중심을 잡아도 그 중심과 원점을 잇는 직선의 반대쪽 점으로 가는 선분이 원점을 지나 영역을 벗어나기 때문이다. 이 차이가 바로 $$1/z$$의 적분이 소멸하지 않는 ([§복소적분, ⁋명제 10](/ko/math/complex_analysis/complex_integration#prop10)) 위상적 이유이다.

<div class="proposition" markdown="1">

<ins id="thm3">**정리 3 (star-shaped 영역의 원시함수)**</ins> $$\Omega \subseteq \mathbb{C}$$가 star-shaped 영역이고 $$f$$가 $$\Omega$$에서 정칙이라 하자. 그러면 $$f$$는 $$\Omega$$에서 원시함수 $$F$$를 가진다. 곧 $$\Omega$$에서 정칙이고 $$F' = f$$인 $$F$$가 존재한다.

</div>

<details class="proof" markdown="1">
<summary>증명</summary>

$$z_\ast$$를 $$\Omega$$의 별중심이라 하자. 각 $$z \in \Omega$$에 대해 선분 $$[z_\ast, z]$$가 $$\Omega$$에 들어 있으므로, 이 선분을 곡선으로 보아

$$F(z) = \int_{[z_\ast, z]} f(\zeta)\,d\zeta$$

로 정의한다. $$F$$가 $$z$$에서 복소미분가능하고 $$F'(z) = f(z)$$임을 보이면 된다.

점 $$z \in \Omega$$를 고정한다. $$\Omega$$가 열려 있으므로 작은 원판 $$B(z, \rho) \subseteq \Omega$$이 있고, $$\lvert h\rvert < \rho$$인 $$h$$에 대해 $$z + h \in \Omega$$이다. 세 점 $$z_\ast, z, z+h$$를 꼭짓점으로 하는 삼각형 $$T$$를 생각하자. 별중심의 성질로 변 $$[z_\ast, z]$$와 $$[z_\ast, z+h]$$가 $$\Omega$$에 들어 있고, 나머지 변 $$[z, z+h]$$는 $$B(z,\rho)$$ 안에 있어 역시 $$\Omega$$에 들어 있다. 더 나아가 별중심에서 이 삼각형의 각 변 위의 점으로 가는 선분이 모두 $$\Omega$$에 있으므로 삼각형의 내부도 $$\Omega$$에 포함되며, 따라서 Goursat 정리 (정리 1) 를 이 삼각형에 적용할 수 있다. 경계 $$z_\ast \to z \to z+h \to z_\ast$$를 따른 적분이 $$0$$이므로

$$\int_{[z_\ast, z]} f\,d\zeta + \int_{[z, z+h]} f\,d\zeta + \int_{[z+h, z_\ast]} f\,d\zeta = 0$$

이고, 역방향 적분의 부호 ([§복소적분, ⁋명제 4](/ko/math/complex_analysis/complex_integration#prop4)) 를 써서 정리하면

$$F(z+h) - F(z) = \int_{[z_\ast, z+h]} f\,d\zeta - \int_{[z_\ast, z]} f\,d\zeta = \int_{[z, z+h]} f\,d\zeta$$

이다. 이제 선분 $$[z, z+h]$$의 길이가 $$\lvert h\rvert$$이고 그 위에서 $$f(\zeta) = f(z) + (f(\zeta) - f(z))$$로 쪼개면, 상수 $$f(z)$$의 선분 적분은 원시함수 $$f(z)\zeta$$로 계산되어 $$f(z)\cdot h$$이므로

$$\frac{F(z+h) - F(z)}{h} - f(z) = \frac{1}{h}\int_{[z, z+h]} \bigl( f(\zeta) - f(z) \bigr)\,d\zeta$$

이다. $$f$$가 $$z$$에서 연속이므로 임의의 $$\varepsilon > 0$$에 대해 $$\lvert h\rvert$$이 충분히 작으면 선분 위에서 $$\lvert f(\zeta) - f(z)\rvert \leq \varepsilon$$이고, ML 부등식 ([§복소적분, ⁋명제 6](/ko/math/complex_analysis/complex_integration#prop6)) 으로 우변의 크기가

$$\frac{1}{\lvert h\rvert}\cdot \varepsilon \cdot \mathrm{length}([z, z+h]) = \frac{1}{\lvert h\rvert}\cdot \varepsilon\, \lvert h\rvert = \varepsilon$$

이하이다. 따라서 $$h \to 0$$일 때 차분비가 $$f(z)$$로 수렴하여 $$F'(z) = f(z)$$이다. $$z$$가 임의였으므로 $$F$$는 $$\Omega$$에서 $$f$$의 원시함수이다.

</details>

정리 3은 정칙성이라는 미분 조건을, 적분의 경로 독립성을 보장하는 원시함수의 존재로 번역한다. 그 다리가 바로 Goursat 정리이며, 원시함수의 차분비가 작은 삼각형 위의 적분으로 표현되고 그 적분이 $$0$$이라는 사실이 미분가능성을 낳는다. 원시함수가 존재하면 복소적분 이론의 일반 원리 ([§복소적분, ⁋따름정리 9](/ko/math/complex_analysis/complex_integration#cor9)) 에 의해 닫힌 경로 적분이 곧바로 소멸하므로, 다음 형태의 Cauchy 정리가 따라 나온다.

<div class="proposition" markdown="1">

<ins id="cor4">**따름정리 4 (Cauchy 정리, star-shaped 형태)**</ins> $$\Omega \subseteq \mathbb{C}$$가 star-shaped 영역이고 $$f$$가 $$\Omega$$에서 정칙이라 하자. 그러면 자취가 $$\Omega$$에 들어 있는 임의의 닫힌 piecewise $$C^1$$ 곡선 $$\gamma$$에 대하여

$$\oint_\gamma f(z)\,dz = 0$$

이다.

</div>

<details class="proof" markdown="1">
<summary>증명</summary>

정리 3에 의해 $$f$$는 $$\Omega$$에서 원시함수 $$F$$를 가진다. 자취가 $$\Omega$$에 들어 있는 닫힌 곡선 $$\gamma$$에 대해, 원시함수를 갖는 연속함수의 닫힌 경로 적분이 $$0$$이라는 사실 ([§복소적분, ⁋따름정리 9](/ko/math/complex_analysis/complex_integration#cor9)) 을 적용하면 $$\oint_\gamma f\,dz = 0$$이다.

</details>

따름정리 4는 닫힌 곡선의 모양에 아무런 제약을 두지 않는다. 영역이 star-shaped이기만 하면, 그 안의 어떤 복잡한 닫힌 경로를 따라 정칙함수를 적분해도 결과가 $$0$$이다. 가령 열린 원판 위에서 정칙인 함수는 그 원판 안의 어떤 닫힌 경로에서도 적분이 소멸한다. 다만 이 결론은 영역의 별모양성에 결정적으로 기댄다. $$1/z$$은 $$\mathbb{C}\setminus\{0\}$$에서 정칙이지만 이 영역이 별모양이 아니므로 정리가 적용되지 않고, 실제로 원점을 감는 원에서의 적분이 $$2\pi i \neq 0$$이다. 영역의 어떤 위상적 성질이 별모양성을 대신할 수 있는가가 다음 절의 물음이다.

## Homotopy 불변성

따름정리 4의 별모양 조건은 영역의 *모양*에 대한 구체적 요구라 다루기 번거롭다. 더 본질적인 조건은 위상적인 것으로, 두 경로가 영역 안에서 서로 연속적으로 변형될 수 있는가, 그리고 닫힌 경로가 영역 안에서 한 점으로 수축될 수 있는가이다. 이 변형 가능성을 homotopy로 정식화하면, 정칙함수의 적분이 경로의 연속적 변형에 무관함을 보일 수 있다. 먼저 같은 끝점을 갖는 두 경로 사이의 homotopy를 정의한다.

<div class="definition" markdown="1">

<ins id="def5">**정의 5**</ins> $$\Omega \subseteq \mathbb{C}$$가 영역이고 $$\gamma_0, \gamma_1 : [a, b] \to \Omega$$가 같은 시점 $$p = \gamma_0(a) = \gamma_1(a)$$와 같은 종점 $$q = \gamma_0(b) = \gamma_1(b)$$을 갖는 두 곡선이라 하자. 두 곡선이 $$\Omega$$ 안에서 *끝점을 고정하여 homotopic<sub>호모토픽</sub>*하다는 것은, 연속사상

$$H : [a, b] \times [0, 1] \to \Omega$$

이 있어 모든 $$t \in [a, b]$$와 $$s \in [0, 1]$$에 대하여

$$H(t, 0) = \gamma_0(t), \quad H(t, 1) = \gamma_1(t), \quad H(a, s) = p, \quad H(b, s) = q$$

를 만족하는 것이다. 각 $$s$$에 대해 곡선 $$\gamma_s(t) = H(t, s)$$는 $$\gamma_0$$에서 $$\gamma_1$$로 이어지는 중간 경로이다.

</div>

homotopy $$H$$는 한 곡선을 다른 곡선으로 끌고 가는 연속적인 변형을 매개변수 $$s$$로 기술한 것으로, $$s = 0$$에서 $$\gamma_0$$, $$s = 1$$에서 $$\gamma_1$$이며 변형 내내 양 끝점이 $$p, q$$에 고정된다. 닫힌 곡선의 경우에는 끝점 고정 대신 각 중간 곡선이 닫혀 있을 것을 요구하며 ($$H(a, s) = H(b, s)$$), 닫힌 곡선이 한 점으로 수축될 수 있을 때, 곧 어떤 상수 곡선과 homotopic할 때 그 곡선을 *null-homotopic<sub>영호모토픽</sub>*하다고 한다. 다음 정리가 적분 이론에서 homotopy가 가지는 의미를 밝힌다.

<div class="proposition" markdown="1">

<ins id="thm6">**정리 6 (Cauchy의 homotopy 정리)**</ins> $$\Omega \subseteq \mathbb{C}$$가 영역이고 $$f$$가 $$\Omega$$에서 정칙이라 하자. $$\gamma_0, \gamma_1$$이 $$\Omega$$ 안에서 끝점을 고정하여 homotopic한 두 piecewise $$C^1$$ 곡선이면

$$\int_{\gamma_0} f(z)\,dz = \int_{\gamma_1} f(z)\,dz$$

이다. 특히 $$\gamma$$가 $$\Omega$$ 안에서 null-homotopic한 닫힌 곡선이면 $$\oint_\gamma f\,dz = 0$$이다.

</div>

<details class="proof" markdown="1">
<summary>증명</summary>

$$H : [a, b] \times [0, 1] \to \Omega$$를 $$\gamma_0$$에서 $$\gamma_1$$로 가는 homotopy라 하자. 상 $$K = H([a,b]\times[0,1])$$은 콤팩트집합 위의 연속상이므로 콤팩트이고 $$\Omega$$에 들어 있다. 콤팩트집합 $$K$$와 닫힌집합 $$\mathbb{C}\setminus\Omega$$ 사이의 거리는 양수이므로, $$3r < \operatorname{dist}(K, \mathbb{C}\setminus\Omega)$$인 $$r > 0$$을 잡으면 $$K$$의 각 점을 중심으로 한 반지름 $$2r$$인 원판이 통째로 $$\Omega$$에 들어간다.

$$H$$가 콤팩트집합 위에서 균등연속이므로, 분할을 충분히 잘게 잡아 $$a = t_0 < t_1 < \cdots < t_n = b$$와 $$0 = s_0 < s_1 < \cdots < s_m = 1$$을 택하면, 각 작은 직사각형 $$[t_{i-1}, t_i]\times[s_{j-1}, s_j]$$의 $$H$$-상이 지름 $$r$$인 원판 안에 들어가도록 할 수 있다. 격자점의 상을 $$w_{i,j} = H(t_i, s_j)$$라 하자.

각 $$s_j$$에 대해 격자점 $$w_{0,j}, w_{1,j}, \ldots, w_{n,j}$$을 차례로 잇는 선분들로 이루어진 다각선 $$\Gamma_j$$를 생각한다. 이 다각선의 적분과 곡선 $$\gamma_{s_j}$$의 적분이 같고, 또 이웃한 두 다각선의 적분이 서로 같음을 보이면 된다.

이웃한 두 다각선 $$\Gamma_{j-1}$$과 $$\Gamma_j$$을 비교한다. 각 $$i$$에 대해 네 점 $$w_{i-1,j-1}, w_{i,j-1}, w_{i,j}, w_{i-1,j}$$은 모두 위 작은 직사각형들의 상에 속해 한 점에서 반지름 $$2r$$인 공통 원판 $$D_i \subseteq \Omega$$ 안에 들어간다. 원판은 볼록하여 star-shaped이므로, 이 네 점을 꼭짓점으로 하는 닫힌 다각형 경로를 따른 $$f$$의 적분이 따름정리 4에 의해 $$0$$이다. 이러한 사각형 적분들을 $$i = 1, \ldots, n$$에 대해 모두 더하면 인접한 사각형이 공유하는 세로변 $$[w_{i,j-1}, w_{i,j}]$$에서의 적분이 방향이 반대라 상쇄되고, 양 끝의 세로변은 homotopy가 끝점을 고정하므로 $$w_{0,j-1} = w_{0,j} = p$$, $$w_{n,j-1} = w_{n,j} = q$$이 되어 길이 $$0$$의 선분이라 기여가 없다. 남는 것은 위·아래 가로변뿐이므로

$$\int_{\Gamma_{j-1}} f\,dz = \int_{\Gamma_j} f\,dz$$

이다. $$j = 1, \ldots, m$$에 대해 이를 이으면 $$\int_{\Gamma_0} f\,dz = \int_{\Gamma_m} f\,dz$$이다.

끝으로 다각선 $$\Gamma_0$$과 곡선 $$\gamma_0$$의 적분이 같음을 본다. 각 $$i$$에 대해 호 $$\gamma_0\vert_{[t_{i-1}, t_i]}$$와 선분 $$[w_{i-1,0}, w_{i,0}]$$은 같은 끝점을 갖고 둘 다 공통 원판 $$D_i$$ 안에 있다. 이 원판 위에서 $$f$$가 원시함수를 가지므로 (정리 3) 두 경로의 적분이 끝값의 차로 같아져 일치하며 ([§복소적분, ⁋따름정리 9](/ko/math/complex_analysis/complex_integration#cor9)의 경로 독립), $$i$$에 대해 더하면 $$\int_{\gamma_0} f\,dz = \int_{\Gamma_0} f\,dz$$이다. 같은 논증으로 $$\int_{\gamma_1} f\,dz = \int_{\Gamma_m} f\,dz$$이므로, 위 결과와 합쳐 $$\int_{\gamma_0} f\,dz = \int_{\gamma_1} f\,dz$$를 얻는다.

null-homotopic한 닫힌 곡선의 경우, 닫힌 곡선에 대한 homotopy를 같은 방식으로 다루면 ($$H(a,s) = H(b,s)$$이라 양 끝 세로변이 길이 $$0$$ 대신 한 점으로 닫혀 상쇄됨) 그 적분이 상수 곡선의 적분과 같고, 상수 곡선의 적분은 $$0$$이다.

</details>

정리 6은 정칙함수의 적분이 경로 자체가 아니라 경로의 homotopy류에만 의존함을 말한다. 같은 두 끝점을 잇되 영역 안에서 서로 끌어당겨 포갤 수 있는 두 경로는 같은 적분값을 주고, 영역 안에서 한 점으로 오므릴 수 있는 닫힌 경로는 적분이 $$0$$이다. 별모양 영역에서는 임의의 닫힌 곡선이 별중심으로 직선을 따라 수축되어 null-homotopic하므로, 따름정리 4가 이 정리의 특수한 경우로 회복된다. 한편 $$\mathbb{C}\setminus\{0\}$$에서 원점을 감는 원은 원점이라는 구멍에 걸려 한 점으로 수축되지 못하므로 null-homotopic하지 않고, 정리 6은 그 적분이 $$0$$이라고 주장하지 않는다. 적분이 $$0$$이 됨을 보장하는 영역은 모든 닫힌 곡선이 수축되는 영역이며, 이것이 다음 정의이다.

<div class="definition" markdown="1">

<ins id="def7">**정의 7**</ins> 영역 $$\Omega \subseteq \mathbb{C}$$가 *simply connected<sub>단순연결</sub>*라는 것은, $$\Omega$$ 안의 임의의 닫힌 곡선이 $$\Omega$$ 안에서 null-homotopic한 것이다. 곧 어떤 닫힌 곡선도 $$\Omega$$ 안에 머물면서 한 점으로 연속적으로 수축될 수 있는 것이다.

</div>

단순연결 영역은 직관적으로 "구멍이 없는" 영역으로, 그 안의 어떤 고리도 영역을 벗어나지 않고 졸라매어 점으로 만들 수 있다. 별모양 영역은 모두 단순연결이며, 따라서 열린 원판이나 평면 전체, 반평면이 단순연결의 예이다. 반면 원점을 뺀 평면이나 환형 영역(annulus)은 구멍을 감는 고리가 수축되지 못하므로 단순연결이 아니다. 정리 6을 이 정의에 적용하면 Cauchy 정리의 가장 표준적인 형태가 나온다.

<div class="proposition" markdown="1">

<ins id="cor8">**따름정리 8 (Cauchy 정리, 단순연결 형태)**</ins> $$\Omega \subseteq \mathbb{C}$$가 단순연결 영역이고 $$f$$가 $$\Omega$$에서 정칙이라 하자. 그러면 자취가 $$\Omega$$에 들어 있는 임의의 닫힌 piecewise $$C^1$$ 곡선 $$\gamma$$에 대하여

$$\oint_\gamma f(z)\,dz = 0$$

이다. 따라서 $$f$$는 $$\Omega$$에서 원시함수를 가진다.

</div>

<details class="proof" markdown="1">
<summary>증명</summary>

$$\Omega$$가 단순연결이므로 자취가 $$\Omega$$에 들어 있는 임의의 닫힌 곡선 $$\gamma$$는 $$\Omega$$ 안에서 null-homotopic하고, 정리 6에 의해 $$\oint_\gamma f\,dz = 0$$이다. 모든 닫힌 경로에서 적분이 소멸하므로 적분이 경로에 무관하며, 기준점 $$z_0 \in \Omega$$를 하나 고정하고 $$z_0$$에서 $$z$$까지 자취가 $$\Omega$$에 든 임의의 곡선을 따라 $$F(z) = \int f\,d\zeta$$로 정의하면 (영역은 연결되어 있어 경로가 존재하고, 경로 독립성으로 값이 잘 정의된다) 정리 3의 증명과 같은 국소 논증으로 $$F' = f$$임이 따라 나와 $$F$$가 원시함수이다.

</details>

따름정리 8은 영역의 위상만으로 정칙함수의 적분 거동을 완전히 결정한다. 단순연결이라는 전역적 조건과 정칙성이라는 국소적 조건이 만나면, 경로의 형태와 무관하게 닫힌 적분이 소멸하고 원시함수가 전역적으로 존재한다. 이는 정리 3의 별모양 가정을 위상적으로 가장 약화한 형태이며, 가령 단순연결 영역에서는 $$0$$이 아닌 정칙함수가 로그와 거듭제곱근을 단일하게 정의받는 등 여러 전역적 구성을 가능하게 한다. 단순연결이 아닌 영역에서 적분이 얼마나 어긋나는지는 닫힌 경로가 구멍을 감는 횟수로 측정되며, 이를 재는 양이 회전수이다.

## 회전수

단순연결이 아닌 영역에서는 닫힌 경로가 한 점으로 수축되지 못하고, 그 장애는 경로가 영역의 구멍을 몇 번 감는가에서 비롯한다. 이 감는 횟수를 정수로 정확히 재는 것이 회전수이며, 그 정의 자체가 핵심 계산 $$\oint dz/z = 2\pi i$$ ([§복소적분, ⁋명제 10](/ko/math/complex_analysis/complex_integration#prop10)) 를 일반화한 적분으로 주어진다.

<div class="definition" markdown="1">

<ins id="def9">**정의 9**</ins> $$\gamma : [a, b] \to \mathbb{C}$$가 닫힌 piecewise $$C^1$$ 곡선이고 $$z_0$$이 그 자취 위에 있지 않은 점이라 하자. $$\gamma$$의 $$z_0$$에 대한 *winding number<sub>회전수</sub>*를

$$n(\gamma, z_0) = \frac{1}{2\pi i}\oint_\gamma \frac{dz}{z - z_0}$$

으로 정의한다.

</div>

회전수는 닫힌 경로 $$\gamma$$가 점 $$z_0$$의 둘레를 반시계방향으로 몇 바퀴 도는지를 세는 정수이다. 적분 $$\oint_\gamma dz/(z - z_0)$$의 피적분함수 $$1/(z - z_0)$$은 $$z_0$$을 중심으로 한 편각의 미소 변화를 재므로, 경로를 한 바퀴 돌며 그 편각의 총 변화량을 모은 것이 적분이고, 이를 $$2\pi i$$로 나누면 회전 횟수가 된다. 가령 $$z_0$$을 중심으로 반시계방향으로 한 번 도는 원에 대해서는 명제 10의 계산에서 $$n(\gamma, z_0) = 1$$이고, 같은 원을 거꾸로 돌면 $$-1$$, $$z_0$$을 감지 않는 경로에 대해서는 $$0$$이다. 이 양이 항상 정수임을 보인다.

<div class="proposition" markdown="1">

<ins id="prop10">**명제 10**</ins> 정의 9의 가정 아래, 회전수 $$n(\gamma, z_0)$$은 정수이다.

</div>

<details class="proof" markdown="1">
<summary>증명</summary>

평행이동으로 $$z_0 = 0$$이라 두어도 일반성을 잃지 않으며, $$\gamma : [a, b] \to \mathbb{C}\setminus\{0\}$$이 닫힌 곡선이다. 함수

$$g(t) = \int_a^t \frac{\gamma'(\tau)}{\gamma(\tau)}\,d\tau$$

를 생각하면, 이는 $$[a, b]$$에서 연속이고 분할점을 뺀 곳에서 $$g'(t) = \gamma'(t)/\gamma(t)$$이다. 함수 $$e^{-g(t)}\gamma(t)$$를 미분하면, 그러한 점에서

$$\frac{d}{dt}\bigl( e^{-g(t)}\gamma(t) \bigr) = e^{-g(t)}\bigl( -g'(t)\gamma(t) + \gamma'(t) \bigr) = e^{-g(t)}\bigl( -\gamma'(t) + \gamma'(t) \bigr) = 0$$

이다. 이 함수는 연속이고 도함수가 유한 개의 점을 빼고 $$0$$이므로 $$[a, b]$$에서 상수이다. 따라서 모든 $$t$$에 대해 $$e^{-g(t)}\gamma(t) = e^{-g(a)}\gamma(a) = \gamma(a)$$ ($$g(a) = 0$$이므로) 이고, 곧 $$\gamma(t) = \gamma(a)\,e^{g(t)}$$이다.

$$\gamma$$가 닫혀 있어 $$\gamma(b) = \gamma(a) \neq 0$$이므로 $$e^{g(b)} = \gamma(b)/\gamma(a) = 1$$이다. 복소지수가 $$1$$이 되는 것은 그 지수가 $$2\pi i$$의 정수배일 때 ([§정칙함수, ⁋정의 10](/ko/math/complex_analysis/holomorphic_functions#def10)의 지수함수와 Euler 공식에서 $$e^{w} = 1 \iff w \in 2\pi i\,\mathbb{Z}$$) 이므로, $$g(b) = 2\pi i\,k$$인 정수 $$k$$가 있다. 그런데 정의에 의해

$$g(b) = \int_a^b \frac{\gamma'(\tau)}{\gamma(\tau)}\,d\tau = \oint_\gamma \frac{dz}{z}$$

이므로 $$n(\gamma, 0) = g(b)/(2\pi i) = k$$는 정수이다.

</details>

명제 10의 증명은 회전수의 정수성이 곧 복소지수의 주기성 $$e^w = 1 \iff w \in 2\pi i\,\mathbb{Z}$$에서 비롯함을 드러낸다. 적분 $$g(b)$$는 경로를 따라 누적된 $$\log\gamma$$의 변화량이고, 경로가 닫혀 출발점으로 돌아오면 $$\gamma$$의 절댓값은 제자리이되 편각만 $$2\pi$$의 정수배만큼 어긋날 수 있는데, 그 정수가 바로 회전수이다. 이로써 회전수는 닫힌 경로가 한 점을 감는 위상적 횟수를 적분으로 포착하며, 단순연결이 아닌 영역에서 Cauchy 정리가 어긋나는 정도를 정량화하는 도구가 된다. 가령 $$f$$가 $$z_0$$을 뺀 영역에서 정칙일 때 닫힌 경로 적분이 $$n(\gamma, z_0)$$에 비례하여 결정되는 현상이 적분공식과 잔여정리에서 본격적으로 전개된다.

---

**참고문헌**

**[Ahl]** L.V. Ahlfors, *Complex analysis*, 3rd ed., McGraw–Hill, 1979.

**[Con]** J.B. Conway, *Functions of one complex variable I*, 2nd ed., Graduate Texts in Mathematics 11, Springer, 1978.

**[SS]** E.M. Stein, R. Shakarchi, *Complex analysis*, Princeton Lectures in Analysis II, Princeton University Press, 2003.
</content>
</invoke>
