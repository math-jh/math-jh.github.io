---
title: "편각원리와 Rouché 정리"
description: "유리형함수의 대수적 미분 f'/f의 닫힌 경로 적분이 영점 수에서 극 수를 뺀 값이며 이것이 상의 원점에 대한 회전수와 같다는 편각원리를 유수정리로 증명한다. 이로부터 우세한 항이 영점 수를 결정한다는 Rouché 정리, 비상수 정칙함수가 국소적으로 m-대-1 사상이라는 사실과 열린사상정리, 그리고 단사 정칙함수의 역의 정칙성과 최대절댓값 원리를 유도한다."
excerpt: "argument principle, 편각원리, 대수적 미분 f'/f, Z-P, 회전수, Rouché 정리, 열린사상정리, 국소 m-대-1, 단사 정칙함수의 역, 최대절댓값 원리"

categories: [Math / Complex Analysis]
permalink: /ko/math/complex_analysis/argument_principle
sidebar: 
    nav: "complex_analysis-ko"

date: 2026-06-21
weight: 10

published: false
---

정칙함수의 영점은 고립되어 유한 위수를 가지며 ([§영점과 일치정리, ⁋명제 2](/ko/math/complex_analysis/zeros_and_identity_theorem#prop2)), 유리형함수의 극 역시 유한 위수를 가진다 ([§고립특이점과 Laurent 급수, ⁋명제 6](/ko/math/complex_analysis/isolated_singularities#prop6)). 한 영역 안에서 이러한 영점과 극이 각각 몇 개나 있는지를 세는 일은 함수의 거동을 파악하는 데 핵심적이지만, 영점과 극의 위치를 일일이 찾지 않고 그 개수만을 알아내는 길이 있다면 훨씬 강력하다. 편각원리는 바로 그 길을 연다. 대수적 미분 $$f'/f$$을 닫힌 경로를 따라 적분하면, 그 값이 경로 안의 영점 수에서 극 수를 뺀 것을 정확히 세어 준다. 이 양은 동시에 상곡선 $$f \circ \gamma$$이 원점을 감는 횟수, 곧 편각의 총 증가량으로도 읽히므로 위상적 의미를 가진다. 편각원리는 그 자체로 영점·극의 계수를 주는 동시에, 함수를 작게 섭동해도 영점 수가 변하지 않는다는 Rouché 정리를 낳고, 거기서 다시 비상수 정칙함수가 열린집합을 열린집합으로 보낸다는 열린사상정리와 단사 정칙함수의 역의 정칙성이 흘러나온다. 이 글은 유수정리를 출발점으로 삼아 이 일련의 결과를 차례로 확립한다.

## 유리형함수와 편각원리

편각원리를 진술하려면 영점과 극을 한꺼번에 다루는 함수 부류가 필요하다. 한 영역에서 고립된 극을 제외하면 정칙인 함수를 유리형함수라 부르며, 유리함수와 $$\tan z$$, $$1/\sin z$$ 같은 함수가 모두 여기에 속한다. 영점과 극은 모두 $$(z - z_0)$$의 정수 멱으로 표현되는 국소적 거동이므로, 위수를 부호까지 포함한 하나의 정수로 다루면 둘을 통일적으로 셀 수 있다.

<div class="definition" markdown="1">

<ins id="def1">**정의 1 (유리형함수)**</ins> 열린집합 $$\Omega \subseteq \mathbb{C}$$ 위의 함수 $$f$$가 $$\Omega$$에서 *meromorphic<sub>유리형</sub>*이라는 것은, $$\Omega$$ 안에 집적점을 갖지 않는 어떤 부분집합 $$P \subseteq \Omega$$이 있어 $$f$$가 $$\Omega \setminus P$$에서 정칙이고 $$P$$의 각 점에서 극을 가지는 것을 뜻한다.

</div>

극집합 $$P$$이 $$\Omega$$ 안에 집적점을 갖지 않는다는 조건은 극이 서로 떨어져 흩어져 있음을 보장하며, 따라서 $$\Omega$$의 임의의 콤팩트 부분집합 안에는 유한개의 극만 들어 있다. 유리형함수의 영점 역시 항등적으로 $$0$$이 아닌 한 고립되어 있으므로 ([§영점과 일치정리, ⁋명제 2](/ko/math/complex_analysis/zeros_and_identity_theorem#prop2)), 영점과 극은 모두 콤팩트 영역 안에서 유한하다. 영점 $$z_0$$ 근방에서는 위수 $$m \geq 1$$에 대해 $$f(z) = (z - z_0)^m g(z)$$ ($$g(z_0) \neq 0$$, $$g$$ 정칙) 이고 ([§멱급수와 해석성, ⁋명제 6](/ko/math/complex_analysis/power_series_and_analyticity#prop6)), 극 $$z_0$$ 근방에서는 위수 $$m \geq 1$$에 대해 $$f(z) = (z - z_0)^{-m} h(z)$$ ($$h(z_0) \neq 0$$, $$h$$ 정칙) 이다 ([§고립특이점과 Laurent 급수, ⁋명제 6](/ko/math/complex_analysis/isolated_singularities#prop6)). 두 경우를 통일하여, 영점에서는 양의 정수, 극에서는 음의 정수, 그 밖에서는 $$0$$인 부호 있는 위수를 도입하면 다음 보조정리가 $$f'/f$$의 거동을 결정한다.

<div class="proposition" markdown="1">

<ins id="lem2">**보조정리 2 (대수적 미분의 유수)**</ins> $$f$$가 $$z_0$$의 한 근방에서 유리형이고 $$z_0$$에서 항등적으로 $$0$$이 아니라 하자. $$z_0$$이 $$f$$의 위수 $$m$$인 영점이면 $$f'/f$$은 $$z_0$$에서 유수 $$m$$인 단순극을 가지고, $$z_0$$이 위수 $$m$$인 극이면 $$f'/f$$은 $$z_0$$에서 유수 $$-m$$인 단순극을 가진다. 곧 어느 경우든

$$\operatorname{Res}_{z = z_0}\frac{f'}{f} = \operatorname{ord}_{z_0} f$$

이다. 여기서 $$\operatorname{ord}_{z_0} f$$은 영점에서는 그 위수, 극에서는 위수의 음수, 그 밖에서는 $$0$$인 부호 있는 위수이다.

</div>

<details class="proof" markdown="1">
<summary>증명</summary>

$$z_0$$이 위수 $$m$$인 영점인 경우와 위수 $$m$$인 극인 경우를 한꺼번에 다룬다. 부호 있는 위수를 $$k = \operatorname{ord}_{z_0} f$$이라 두면, 영점이면 $$k = m \geq 1$$, 극이면 $$k = -m \leq -1$$이고, 어느 쪽이든 $$z_0$$의 어떤 구멍 뚫린 근방에서 정칙이고 $$\varphi(z_0) \neq 0$$인 함수 $$\varphi$$이 있어

$$f(z) = (z - z_0)^k\,\varphi(z)$$

이다. 영점의 경우는 인수분해 ([§멱급수와 해석성, ⁋명제 6](/ko/math/complex_analysis/power_series_and_analyticity#prop6)) 에서 $$\varphi = g$$이고, 극의 경우는 극의 특징 ([§고립특이점과 Laurent 급수, ⁋명제 6](/ko/math/complex_analysis/isolated_singularities#prop6)) 에서 $$\varphi = h$$이다. 양변에 로그미분을 적용한다. 곱의 미분으로

$$f'(z) = k(z - z_0)^{k-1}\varphi(z) + (z - z_0)^k\varphi'(z)$$

이므로, $$f(z) = (z - z_0)^k\varphi(z)$$으로 나누면 $$z \neq z_0$$인 점에서

$$\frac{f'(z)}{f(z)} = \frac{k}{z - z_0} + \frac{\varphi'(z)}{\varphi(z)}$$

이다. $$\varphi$$이 $$z_0$$에서 정칙이고 $$\varphi(z_0) \neq 0$$이므로 $$\varphi'/\varphi$$은 $$z_0$$에서 정칙이고, 따라서 위 식의 둘째 항은 $$z_0$$에서 정칙이다. 그러므로 $$f'/f$$의 $$z_0$$에서의 주부는 $$k/(z - z_0)$$뿐이며, 이는 $$f'/f$$이 $$z_0$$에서 유수 $$k$$인 단순극을 가짐을 뜻한다 ([§유수정리, ⁋정의 1](/ko/math/complex_analysis/residue_theorem#def1)). 곧 $$\operatorname{Res}_{z = z_0}(f'/f) = k = \operatorname{ord}_{z_0} f$$이다.

</details>

보조정리 2의 핵심은 로그미분 $$f'/f = (\log f)'$$이 곱셈적 구조를 덧셈적 구조로 바꾼다는 데 있다. 인수 $$(z - z_0)^k$$은 $$f'/f$$에 $$k/(z - z_0)$$이라는 항을 내놓고, $$0$$이 아닌 인수 $$\varphi$$은 정칙한 기여만 하므로 흔적을 남기지 않는다. 그 결과 $$f'/f$$의 유수가 정확히 부호 있는 위수를 읽어 낸다. 영점은 양의 유수로, 극은 음의 유수로 나타나므로, 이를 한 경로 안에서 합하면 영점 수와 극 수의 차가 나온다. 이것이 편각원리이다.

<div class="proposition" markdown="1">

<ins id="thm3">**정리 3 (편각원리)**</ins> $$\Omega \subseteq \mathbb{C}$$가 단순연결 영역이고 $$f$$가 $$\Omega$$에서 유리형이며 항등적으로 $$0$$이 아니라 하자. $$\gamma$$이 $$\Omega$$ 안의 양의 방향 단순 닫힌 곡선이고 그 자취 위에 $$f$$의 영점도 극도 없다고 하자. 그러면

$$\frac{1}{2\pi i}\oint_\gamma \frac{f'(z)}{f(z)}\,dz = Z - P$$

이다. 여기서 $$Z$$은 $$\gamma$$ 안쪽에 있는 $$f$$의 영점의 개수, $$P$$은 극의 개수이며, 각각 위수를 세어 (위수 $$m$$인 영점·극은 $$m$$번) 헤아린다. 더 나아가 이 값은 상곡선 $$f \circ \gamma$$의 원점에 대한 회전수와 같다. 곧

$$Z - P = n(f \circ \gamma,\, 0)$$

이다.

</div>

<details class="proof" markdown="1">
<summary>증명</summary>

$$\gamma$$의 자취와 그 안쪽이 이루는 콤팩트 집합 안에는 $$f$$의 영점과 극이 유한개만 들어 있다. 이들을 $$z_1, \dots, z_r$$이라 하고 각각의 부호 있는 위수를 $$k_j = \operatorname{ord}_{z_j} f$$이라 하자. 함수 $$f'/f$$은 $$\Omega$$에서 이 점들을 제외하면 정칙이고, 보조정리 2에 의해 각 $$z_j$$에서 유수 $$k_j$$인 단순극을 가진다. $$\gamma$$의 자취 위에는 영점도 극도 없으므로 $$f'/f$$이 자취 위에서 정칙이다. $$\gamma$$이 양의 방향 단순 닫힌 곡선이므로 안쪽 점에 대한 회전수는 $$1$$, 바깥 점에 대한 회전수는 $$0$$이고, 유수정리 ([§유수정리, ⁋정리 2](/ko/math/complex_analysis/residue_theorem#thm2)) 에 의해

$$\frac{1}{2\pi i}\oint_\gamma\frac{f'(z)}{f(z)}\,dz = \sum_{z_j \text{ 안쪽}} \operatorname{Res}_{z = z_j}\frac{f'}{f} = \sum_{z_j \text{ 안쪽}} k_j$$

이다. 안쪽 영점에서는 $$k_j$$이 그 위수만큼 양수이고 안쪽 극에서는 그 위수만큼 음수이므로, 위수를 세어 더한 이 합은 정확히 $$Z - P$$이다.

남은 것은 이 적분이 상곡선의 회전수와 같음을 보이는 일이다. $$\gamma : [a, b] \to \mathbb{C}$$이 piecewise $$C^1$$ 매개변수화이면 합성곡선 $$\sigma = f \circ \gamma$$ 역시 piecewise $$C^1$$이고, 그 자취 위에 $$f$$의 영점이 없으므로 $$\sigma(t) = f(\gamma(t)) \neq 0$$이다. 곧 $$\sigma$$은 원점을 지나지 않는 닫힌 곡선이다. 치환 $$w = f(z)$$, $$dw = f'(z)\,dz$$으로

$$\oint_\gamma\frac{f'(z)}{f(z)}\,dz = \int_a^b\frac{f'(\gamma(t))\,\gamma'(t)}{f(\gamma(t))}\,dt = \int_a^b\frac{\sigma'(t)}{\sigma(t)}\,dt = \oint_\sigma\frac{dw}{w}$$

이고, 회전수의 정의 ([§Cauchy 정리, ⁋정의 9](/ko/math/complex_analysis/cauchy_theorem#def9)) 에 의해 마지막 적분이 $$2\pi i\, n(\sigma, 0)$$이다. 따라서

$$\frac{1}{2\pi i}\oint_\gamma\frac{f'(z)}{f(z)}\,dz = n(f \circ \gamma,\, 0)$$

이고, 이를 앞의 등식과 합치면 $$Z - P = n(f \circ \gamma, 0)$$을 얻는다.

</details>

정리 3의 이름은 그 마지막 등식에서 온다. $$\oint_\gamma f'/f\,dz$$은 곧 $$\oint_\sigma dw/w = \oint_\sigma d(\log w)$$이고, $$\log w = \log\lvert w\rvert + i\arg w$$의 실수부는 닫힌 곡선을 한 바퀴 돌면 제자리로 돌아와 기여가 $$0$$이므로, 살아남는 것은 편각 $$\arg w$$의 총 변화량이다. 곧 적분의 값은 $$z$$이 $$\gamma$$을 한 바퀴 도는 동안 $$f(z)$$의 편각이 $$2\pi$$의 몇 배만큼 증가했는가를 센다. 이 편각의 총 증가량이 상곡선이 원점을 감는 횟수이고, 동시에 그것이 안쪽 영점 수에서 극 수를 뺀 값과 같다는 것이 편각원리의 내용이다. 정칙함수의 경우 극이 없어 $$P = 0$$이므로, 적분은 곧 안쪽 영점의 개수를 위수까지 세어 준다.

<div class="example" markdown="1">

<ins id="ex4">**예시 4 (다항식의 영점 수)**</ins> $$p(z) = z^4 - 5z + 1$$의 영점 가운데 단위원판 $$\lvert z\rvert < 1$$ 안에 있는 것의 개수를 편각원리로 센다. $$p$$은 다항식이라 전해석함수이고 극이 없으므로 ($$P = 0$$), 단위원 $$\gamma(\theta) = e^{i\theta}$$ ($$0 \leq \theta \leq 2\pi$$) 위에 영점이 없는 한 안쪽 영점 수 $$Z$$은 상곡선 $$p \circ \gamma$$의 원점에 대한 회전수와 같다. 먼저 단위원 위에 영점이 없음을 확인한다. $$\lvert z\rvert = 1$$이면 삼각부등식으로

$$\lvert p(z)\rvert = \lvert {-5z} + (z^4 + 1)\rvert \geq \lvert 5z\rvert - \lvert z^4 + 1\rvert \geq 5 - (\lvert z\rvert^4 + 1) = 5 - 2 = 3 > 0$$

이므로 단위원 위에 영점이 없다. 따라서 안쪽 영점 수는 상곡선 $$p \circ \gamma$$의 회전수와 같고, 회전수를 직접 추적하는 대신 다음 절의 Rouché 정리를 쓰면 계산이 즉시 끝난다. 위 어림에서 이미 단위원 위 $$\lvert {-5z}\rvert = 5$$이 나머지 $$\lvert z^4 + 1\rvert \leq 2$$을 압도하므로, $$-5z$$을 우세항으로 삼아 영점 수를 셀 수 있다. 이 예는 명제 5의 적용에서 마무리한다.

</div>

## Rouché 정리

편각원리는 영점 수를 상곡선의 회전수로 바꾸어 주는데, 회전수는 곡선을 연속적으로 변형해도 원점을 가로지르지 않는 한 변하지 않는 위상적 불변량이다. 이 안정성을 함수의 섭동으로 옮긴 것이 Rouché 정리이다. 두 함수 $$f$$과 $$f + g$$을 비교할 때, 경계에서 $$g$$이 $$f$$보다 작으면 상곡선이 원점을 감는 횟수가 바뀔 수 없고, 따라서 두 함수의 안쪽 영점 수가 같아진다. 이는 영점 수를 직접 세기 어려운 함수를, 영점 수가 자명한 우세항과 비교하여 알아내는 강력한 도구가 된다.

<div class="proposition" markdown="1">

<ins id="prop5">**명제 5 (Rouché 정리)**</ins> $$\Omega \subseteq \mathbb{C}$$가 단순연결 영역이고 $$f, g$$이 $$\Omega$$에서 정칙이라 하자. $$\gamma$$이 $$\Omega$$ 안의 양의 방향 단순 닫힌 곡선이고, 그 자취 위의 모든 점에서

$$\lvert g(z)\rvert < \lvert f(z)\rvert$$

이라 하자. 그러면 $$f$$과 $$f + g$$은 $$\gamma$$ 안쪽에서 위수를 세어 같은 개수의 영점을 가진다.

</div>

<details class="proof" markdown="1">
<summary>증명</summary>

먼저 두 함수가 자취 위에서 영점을 갖지 않음을 본다. $$\gamma$$ 위에서 $$\lvert g\rvert < \lvert f\rvert$$이므로 특히 $$\lvert f(z)\rvert > \lvert g(z)\rvert \geq 0$$이라 $$f(z) \neq 0$$이고, 또 $$\lvert f(z) + g(z)\rvert \geq \lvert f(z)\rvert - \lvert g(z)\rvert > 0$$이라 $$(f+g)(z) \neq 0$$이다. 따라서 $$f$$과 $$f + g$$ 모두 자취 위에 영점이 없어 편각원리를 적용할 수 있다. 둘 다 정칙이라 극이 없으므로, $$f$$의 안쪽 영점 수를 $$Z_f$$, $$f + g$$의 안쪽 영점 수를 $$Z_{f+g}$$이라 하면 정리 3에 의해

$$Z_f = n(f \circ \gamma,\, 0), \qquad Z_{f+g} = n\bigl((f+g) \circ \gamma,\, 0\bigr)$$

이다.

이제 두 회전수가 같음을 보인다. 자취 위에서 $$f(z) \neq 0$$이므로 몫함수

$$h(z) = \frac{f(z) + g(z)}{f(z)} = 1 + \frac{g(z)}{f(z)}$$

이 자취 위에서 잘 정의된다. 가정 $$\lvert g\rvert < \lvert f\rvert$$에서 $$\lvert g(z)/f(z)\rvert < 1$$이므로, 자취 위의 모든 점에서

$$\lvert h(z) - 1\rvert = \left\lvert\frac{g(z)}{f(z)}\right\rvert < 1$$

이다. 곧 상곡선 $$h \circ \gamma$$은 중심 $$1$$, 반지름 $$1$$인 열린 원판 $$D(1, 1)$$ 안에 통째로 들어 있다. 이 원판은 원점을 그 경계에조차 포함하지 않으므로, $$h \circ \gamma$$은 원점을 감을 수 없어 $$n(h \circ \gamma, 0) = 0$$이다. 실제로 원점을 품지 않는 단순연결 영역 $$D(1,1)$$ 위에서 $$1/w$$은 원시함수 $$\log w$$ (주가지) 을 가지므로 $$\oint_{h \circ \gamma} dw/w = 0$$이고, 따라서 회전수가 $$0$$이다.

한편 $$(f + g) \circ \gamma = (f \circ \gamma)\cdot(h \circ \gamma)$$이고, 원점을 지나지 않는 두 닫힌 곡선의 곱에 대해 회전수는 더해진다. 이는

$$\frac{(fh)'}{fh} = \frac{f'}{f} + \frac{h'}{h}$$

을 $$\gamma$$ 위에서 적분하고 $$2\pi i$$로 나눈 것이 회전수의 합임에서 나온다. 따라서

$$n\bigl((f+g)\circ\gamma,\,0\bigr) = n(f\circ\gamma,\,0) + n(h\circ\gamma,\,0) = n(f\circ\gamma,\,0) + 0$$

이고, 곧 $$Z_{f+g} = Z_f$$이다.

</details>

명제 5는 영점 수를 세는 문제를 가장 단순한 함수와의 비교로 환원한다. 어떤 정칙함수를 우세한 항 $$f$$과 작은 보정 $$g$$으로 갈라, 경계에서 $$\lvert g\rvert < \lvert f\rvert$$임만 확인하면 전체의 영점 수가 우세항 $$f$$의 영점 수와 같아진다. 우세항으로는 보통 영점 수가 한눈에 보이는 단항식이나 다항식을 택한다. 가정에서 부등식이 자취 위에서 엄격해야 하는 까닭은, 등호가 허용되면 상곡선이 원점에 닿아 회전수가 정의되지 않거나 비교가 무너질 수 있기 때문이다. 예시 4의 다항식에 이를 적용한다.

<div class="example" markdown="1">

<ins id="ex6">**예시 6 (Rouché에 의한 영점 계수)**</ins> 다시 $$p(z) = z^4 - 5z + 1$$의 단위원판 $$\lvert z\rvert < 1$$ 안 영점 수를 구한다. 우세항을 어떻게 고르느냐가 관건이다. 단위원 $$\lvert z\rvert = 1$$ 위에서 $$\lvert z^4\rvert = 1$$로 가장 작으므로 최고차항 $$z^4$$을 우세항으로 삼는 비교는 통하지 않는다. 대신 일차항이 가장 크므로 $$f(z) = -5z$$, $$g(z) = z^4 + 1$$으로 갈라 본다. 단위원 위에서

$$\lvert g(z)\rvert = \lvert z^4 + 1\rvert \leq \lvert z\rvert^4 + 1 = 2 < 5 = \lvert {-5z}\rvert = \lvert f(z)\rvert$$

이므로 명제 5의 가정이 엄격하게 성립한다. $$f(z) = -5z$$은 $$\lvert z\rvert < 1$$ 안에서 $$z = 0$$이라는 단순영점 하나만 가지므로, $$p = f + g$$ 역시 단위원판 안에서 위수를 세어 정확히 한 개의 영점을 가진다.

나머지 세 영점의 위치도 같은 방식으로 좁힐 수 있다. 반지름을 키워 $$\lvert z\rvert = 2$$ 위에서 보면 $$\lvert z^4\rvert = 16$$이고 $$\lvert {-5z} + 1\rvert \leq 11 < 16$$이므로, 이번에는 $$f(z) = z^4$$, $$g(z) = -5z + 1$$으로 갈라 명제 5를 적용하면 $$p$$은 $$\lvert z\rvert < 2$$ 안에서 $$z^4$$과 같은 $$4$$개의 영점을 가진다. 곧 네 영점이 모두 $$\lvert z\rvert < 2$$ 안에 있고, 그 가운데 정확히 하나만 단위원판 안에 있으므로 나머지 셋은 환형 영역 $$1 < \lvert z\rvert < 2$$에 놓인다. 이렇게 Rouché 정리를 여러 반지름에 거듭 적용하면 영점의 분포를 환형 영역 단위로 가둘 수 있다.

</div>

명제 5는 대수학의 기본정리를 단번에 준다. $$n$$차 다항식 $$p(z) = z^n + a_{n-1}z^{n-1} + \cdots + a_0$$에서 $$f(z) = z^n$$을 우세항, $$g(z) = a_{n-1}z^{n-1} + \cdots + a_0$$을 보정으로 잡으면, $$\lvert z\rvert = R$$이 충분히 클 때 $$\lvert g(z)\rvert \leq (\lvert a_{n-1}\rvert + \cdots + \lvert a_0\rvert) R^{n-1} < R^n = \lvert f(z)\rvert$$이므로, $$p$$은 $$\lvert z\rvert < R$$ 안에서 $$z^n$$과 같은 $$n$$개의 영점을 위수까지 세어 가진다. $$R$$을 키우면 모든 영점이 포함되므로, $$p$$은 정확히 $$n$$개의 영점을 (중복도까지) 가진다.

## 열린사상정리

편각원리는 영점 수를 세는 데 그치지 않고, 정칙함수가 값을 취하는 방식 자체에 대한 위상적 정보를 준다. 한 점 $$z_0$$에서 $$f(z_0) = w_0$$이면 $$z_0$$은 $$f - w_0$$의 영점이고, $$w_0$$에 가까운 값 $$w$$을 취하는 점의 개수는 $$f - w$$의 영점 수이다. Rouché 정리는 $$w$$이 $$w_0$$에 충분히 가까운 한 이 영점 수가 변하지 않음을 보장하므로, $$f$$이 $$w_0$$ 근방의 모든 값을 같은 횟수로 취한다는 결론이 나온다. 이로부터 비상수 정칙함수가 국소적으로 일정한 겹수의 사상이라는 사실과, 상이 항상 열려 있다는 열린사상정리가 따라 나온다.

<div class="proposition" markdown="1">

<ins id="thm7">**정리 7 (국소 $$m$$-대-1 사상)**</ins> $$f$$이 $$z_0$$의 한 근방에서 정칙이고 $$w_0 = f(z_0)$$이라 하자. $$f - w_0$$이 $$z_0$$에서 위수 $$m \geq 1$$인 영점을 가진다고 하면, 적당히 작은 $$\delta > 0$$과 그에 대응하는 $$\varepsilon > 0$$이 있어 다음이 성립한다. $$0 < \lvert w - w_0\rvert < \varepsilon$$인 모든 $$w$$에 대해, 방정식 $$f(z) = w$$은 구멍 뚫린 원판 $$0 < \lvert z - z_0\rvert < \delta$$ 안에서 정확히 $$m$$개의 서로 다른 단순해를 가진다.

</div>

<details class="proof" markdown="1">
<summary>증명</summary>

$$F(z) = f(z) - w_0$$으로 두면 $$F$$은 $$z_0$$에서 위수 $$m$$인 영점을 가진다. 영점이 고립되어 있고 ([§영점과 일치정리, ⁋명제 2](/ko/math/complex_analysis/zeros_and_identity_theorem#prop2)) $$F'$$ 역시 비상수라 그 영점도 고립되어 있으므로, 충분히 작은 $$\delta > 0$$을 골라 닫힌 원판 $$\overline{D(z_0, \delta)}$$ 안에서 $$F$$의 영점이 $$z_0$$ 하나뿐이고 $$F'$$의 영점도 $$z_0$$ 외에는 없도록 할 수 있다. 그러면 경계원 $$\lvert z - z_0\rvert = \delta$$ 위에서 $$F(z) \neq 0$$이므로

$$\varepsilon = \min_{\lvert z - z_0\rvert = \delta}\lvert F(z)\rvert = \min_{\lvert z - z_0\rvert = \delta}\lvert f(z) - w_0\rvert > 0$$

이 양수이다 (콤팩트 집합 위 연속함수의 최솟값).

이제 $$0 < \lvert w - w_0\rvert < \varepsilon$$인 $$w$$을 고정하고 $$f(z) - w = F(z) - (w - w_0)$$으로 쓴다. 경계원 위에서 $$\lvert -(w - w_0)\rvert = \lvert w - w_0\rvert < \varepsilon \leq \lvert F(z)\rvert$$이므로, Rouché 정리 (명제 5) 를 $$F$$ (우세항) 과 $$-(w - w_0)$$ (보정) 에 적용하면 $$f - w = F - (w - w_0)$$은 $$D(z_0, \delta)$$ 안에서 $$F$$과 같은 개수, 곧 위수를 세어 $$m$$개의 영점을 가진다.

이 $$m$$개의 영점이 서로 다른 단순영점임을 본다. $$w \neq w_0$$이므로 $$z_0$$은 더 이상 $$f - w$$의 영점이 아니고, 따라서 모든 영점은 구멍 뚫린 원판 $$0 < \lvert z - z_0\rvert < \delta$$ 안에 있다. 그곳에서는 $$F'(z) = f'(z) \neq 0$$이므로, $$f(z) = w$$인 각 영점 $$\zeta$$에서 $$(f - w)'(\zeta) = f'(\zeta) \neq 0$$이라 그 영점은 위수 $$1$$인 단순영점이다. 단순영점은 서로 다른 점으로만 셈해지므로, 위수를 세어 $$m$$개라는 것은 곧 서로 다른 $$m$$개의 점이라는 뜻이다.

</details>

정리 7은 비상수 정칙함수가 각 점 근방에서 정확히 일정한 겹수로 값을 덮음을 말한다. $$f'(z_0) \neq 0$$인 점, 곧 $$m = 1$$인 점 근방에서는 $$f$$이 국소적으로 단사여서 일대일 사상이 되고, $$f'(z_0) = 0$$인 임계점 근방에서는 위수 $$m \geq 2$$만큼 여러 겹으로 값을 취한다. 이 사실은 바로 다음의 열린사상정리를 곧장 내놓는다. 정칙함수가 $$w_0$$ 근방의 모든 값을 취한다면, 그 상은 $$w_0$$의 한 근방을 통째로 포함하므로 열려 있을 수밖에 없기 때문이다.

<div class="proposition" markdown="1">

<ins id="thm8">**정리 8 (열린사상정리)**</ins> $$\Omega \subseteq \mathbb{C}$$가 연결 열린집합이고 $$f$$이 $$\Omega$$에서 정칙이며 상수가 아니라 하자. 그러면 $$f$$은 *open map<sub>열린사상</sub>*이다. 곧 $$\Omega$$의 임의의 열린 부분집합 $$U$$에 대해 상 $$f(U)$$이 $$\mathbb{C}$$에서 열려 있다.

</div>

<details class="proof" markdown="1">
<summary>증명</summary>

$$U \subseteq \Omega$$이 열려 있다고 하고, $$w_0 \in f(U)$$을 임의로 잡아 $$f(U)$$이 $$w_0$$의 한 근방을 포함함을 보이면 된다. $$w_0 = f(z_0)$$인 $$z_0 \in U$$을 택한다. $$f$$이 연결 열린집합 $$\Omega$$에서 상수가 아니므로, 일치정리 ([§영점과 일치정리, ⁋정리 3](/ko/math/complex_analysis/zeros_and_identity_theorem#thm3)) 에 의해 $$f - w_0$$은 어떤 근방에서도 항등적으로 $$0$$이 아니고, 따라서 $$z_0$$에서 유한한 위수 $$m \geq 1$$인 영점을 가진다.

정리 7을 $$f$$과 $$z_0$$에 적용한다. 정리 7이 주는 $$\delta > 0$$과 $$\varepsilon > 0$$을, $$\overline{D(z_0, \delta)} \subseteq U$$이 되도록 $$\delta$$을 더 줄여 잡을 수 있다 ($$U$$이 열려 있으므로). 그러면 $$0 < \lvert w - w_0\rvert < \varepsilon$$인 모든 $$w$$에 대해 $$f(z) = w$$인 해가 $$D(z_0, \delta) \subseteq U$$ 안에 (적어도 하나) 존재하므로 $$w \in f(U)$$이다. 또 $$w = w_0$$ 자신도 $$f(z_0)$$으로서 $$f(U)$$에 든다. 따라서

$$D(w_0, \varepsilon) \subseteq f(U)$$

이고, $$w_0 \in f(U)$$이 임의였으므로 $$f(U)$$의 모든 점이 내부점이다. 곧 $$f(U)$$이 열려 있다.

</details>

열린사상정리는 정칙함수의 상이 결코 찌부러질 수 없음을 말한다. 실변수의 매끄러운 함수는 가령 상수가 아니면서도 상이 한 구간으로 닫혀 있을 수 있지만, 비상수 정칙함수의 상에는 그런 일이 없어 항상 열린집합으로 퍼진다. 이 정리에서 두 가지 중요한 귀결이 곧장 나온다. 하나는 단사 정칙함수의 역사상이 자동으로 정칙이 된다는 사실이고, 다른 하나는 최대절댓값 원리의 새로운 증명이다. 먼저 역사상의 정칙성을 본다.

<div class="proposition" markdown="1">

<ins id="cor9">**따름정리 9 (역사상의 정칙성)**</ins> $$\Omega \subseteq \mathbb{C}$$가 열린집합이고 $$f : \Omega \to \mathbb{C}$$이 정칙인 단사사상이라 하자. 그러면 상 $$\Omega' = f(\Omega)$$이 열린집합이고, 역사상 $$f^{-1} : \Omega' \to \Omega$$이 정칙이며 그 도함수는

$$(f^{-1})'(w) = \frac{1}{f'(f^{-1}(w))}$$

이다.

</div>

<details class="proof" markdown="1">
<summary>증명</summary>

$$f$$이 단사이고 비상수이므로 (단사함수는 상수일 수 없다) 열린사상정리 (정리 8) 에 의해 $$\Omega' = f(\Omega)$$이 열려 있고, 더 일반적으로 $$\Omega$$의 임의의 열린 부분집합의 상이 열려 있다. 이는 곧 $$f^{-1} : \Omega' \to \Omega$$이 연속임을 뜻한다. 임의의 열린집합 $$U \subseteq \Omega$$에 대해 $$(f^{-1})^{-1}(U) = f(U)$$이 열려 있기 때문이다.

다음으로 $$f$$의 도함수가 어디서도 $$0$$이 아님을 본다. 만일 어떤 $$z_0$$에서 $$f'(z_0) = 0$$이면 $$f - f(z_0)$$이 $$z_0$$에서 위수 $$m \geq 2$$인 영점을 가지므로, 정리 7에 의해 $$f$$이 $$z_0$$의 구멍 뚫린 근방에서 어떤 값 $$w$$을 $$m \geq 2$$번 취하여 단사성에 어긋난다. 따라서 모든 $$z \in \Omega$$에서 $$f'(z) \neq 0$$이다.

이제 $$f^{-1}$$의 복소미분가능성을 보인다. $$w_0 \in \Omega'$$을 고정하고 $$z_0 = f^{-1}(w_0)$$이라 하자. $$w \to w_0$$이면 $$f^{-1}$$의 연속성에서 $$z = f^{-1}(w) \to z_0$$이고, 단사성에서 $$w \neq w_0$$이면 $$z \neq z_0$$이다. 차분몫을 정리하면

$$\frac{f^{-1}(w) - f^{-1}(w_0)}{w - w_0} = \frac{z - z_0}{f(z) - f(z_0)} = \left(\frac{f(z) - f(z_0)}{z - z_0}\right)^{-1}$$

이고, $$w \to w_0$$일 때 $$z \to z_0$$이므로 오른쪽 괄호 안이 $$f'(z_0) \neq 0$$으로 수렴한다. 따라서 극한이 존재하여

$$(f^{-1})'(w_0) = \frac{1}{f'(z_0)} = \frac{1}{f'(f^{-1}(w_0))}$$

이다. $$w_0$$이 임의였으므로 $$f^{-1}$$이 $$\Omega'$$ 전체에서 정칙이다.

</details>

따름정리 9는 정칙성이라는 강한 조건 아래에서는 역함수의 미분가능성을 따로 가정할 필요가 없음을 말한다. 실변수에서 매끄러운 단사함수의 역이 매끄럽다는 보장에는 도함수가 $$0$$이 아니라는 조건이 필요하지만, 정칙 단사함수에서는 그 조건이 단사성에서 저절로 따라 나오고, 역의 정칙성까지 자동으로 보장된다. 이로써 정칙 단사사상은 그 상으로의 정칙동형사상이 되며, 이것이 등각동형사상 이론의 기초가 된다.

끝으로 열린사상정리는 최대절댓값 원리에 새로운 시야를 준다. 이미 평균값 성질로 증명한 이 원리를 ([§영점과 일치정리, ⁋정리 5](/ko/math/complex_analysis/zeros_and_identity_theorem#thm5)), 여기서는 상이 열려 있다는 사실만으로 다시 얻는다.

<div class="proposition" markdown="1">

<ins id="cor10">**따름정리 10 (열린사상정리에 의한 최대절댓값 원리)**</ins> $$\Omega \subseteq \mathbb{C}$$가 연결 열린집합이고 $$f$$이 $$\Omega$$에서 정칙이라 하자. 만일 $$\lvert f\rvert$$이 $$\Omega$$의 어떤 점 $$z_0$$에서 국소적 최댓값에 이르면 $$f$$은 $$\Omega$$에서 상수이다.

</div>

<details class="proof" markdown="1">
<summary>증명</summary>

$$f$$이 상수가 아니라고 가정하고 모순을 이끈다. $$f$$이 연결 열린집합에서 비상수이므로 열린사상정리 (정리 8) 에 의해 $$f$$은 열린사상이다. $$\lvert f\rvert$$이 $$z_0$$에서 국소적 최댓값에 이른다 함은, 어떤 근방 $$D(z_0, r) \subseteq \Omega$$ 안의 모든 $$z$$에서 $$\lvert f(z)\rvert \leq \lvert f(z_0)\rvert$$임을 뜻한다. 곧 상 $$f(D(z_0, r))$$이 닫힌 원판 $$\overline{D(0, \lvert f(z_0)\rvert)}$$ 안에 들어 있다.

그런데 $$w_0 = f(z_0)$$은 그 닫힌 원판의 경계 $$\lvert w\rvert = \lvert f(z_0)\rvert$$ 위의 점이다. 열린사상정리에서 $$f(D(z_0, r))$$은 열린집합이므로 $$w_0$$의 한 근방 $$D(w_0, \varepsilon)$$을 포함하는데, 이 근방에는 $$\lvert w\rvert > \lvert w_0\rvert$$인 점 (가령 $$w_0$$을 원점에서 멀어지는 방향으로 조금 옮긴 점) 이 반드시 들어 있다. 이는 $$f(D(z_0, r)) \subseteq \overline{D(0, \lvert f(z_0)\rvert)}$$에 어긋난다. 따라서 가정이 틀렸고, $$f$$은 $$\Omega$$에서 상수이다.

</details>

따름정리 10은 최대절댓값 원리가 본질적으로 열린사상정리의 한 표현임을 드러낸다. 정칙함수의 상이 열려 있다면 상의 어느 점도 원점에서의 거리가 국소적 최대가 될 수 없는데, 그 점 주위로 더 먼 점이 항상 상에 들어 있기 때문이다. 곧 $$\lvert f\rvert$$의 국소적 최댓값은 상이 열려 있다는 사실과 양립할 수 없고, 이를 피할 유일한 길이 $$f$$이 상수가 되어 상이 한 점으로 줄어드는 것이다. 평균값 성질을 거친 앞선 증명과 비교하면, 이 증명은 적분 어림 없이 순전히 위상적 논증만으로 같은 결론에 이른다.

---

**참고문헌**

**[Ahl]** L.V. Ahlfors, *Complex analysis*, 3rd ed., McGraw–Hill, 1979.

**[Con]** J.B. Conway, *Functions of one complex variable I*, 2nd ed., Graduate Texts in Mathematics 11, Springer, 1978.

**[SS]** E.M. Stein, R. Shakarchi, *Complex analysis*, Princeton Lectures in Analysis II, Princeton University Press, 2003.
</content>
</invoke>
