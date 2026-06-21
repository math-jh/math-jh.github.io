---
title: "Riemann 사상정리"
description: "단순연결인 ℂ의 진부분 열린집합이 단위원판과 등각동형이고, 한 점의 정규화 조건으로 그 사상이 유일함을 증명한다. 도구로 국소 유계 정칙족이 정규족이라는 Montel 정리를 확립하고, 단사 정칙사상의 모임에서 도함수의 절댓값을 최대화하는 극값사상을 추출한 뒤, 그것이 전사임을 Schwarz 보조정리로, 전체가 단사임을 Hurwitz 정리로 보인다."
excerpt: "Riemann mapping theorem, 등각동형, 단순연결, 단위원판, normal family, Montel 정리, Hurwitz 정리, 극값사상, Schwarz 보조정리"

categories: [Math / Complex Analysis]
permalink: /ko/math/complex_analysis/riemann_mapping_theorem
sidebar: 
    nav: "complex_analysis-ko"

date: 2026-06-21
weight: 12

published: false
---

두 영역 사이에 정칙 전단사사상이 존재하는지, 곧 두 영역이 등각동형인지를 묻는 문제는 복소해석학의 한 중심에 놓인다. 정칙 전단사사상은 도함수가 어디서도 소멸하지 않아 각을 보존하는 등각사상이 되므로 ([§등각사상과 Möbius 변환, ⁋명제 3](/ko/math/complex_analysis/conformal_maps#prop3)), 한 영역 위의 정칙함수론 전체가 등각동형사상을 통해 다른 영역으로 고스란히 옮겨진다. 그런데 등각동형의 후보가 될 수 있는 영역은 놀랍도록 적다. Riemann 사상정리는 $$\mathbb{C}$$ 전체가 아닌 단순연결 열린집합이라면, 그 모양이 아무리 복잡하더라도 예외 없이 단위원판과 등각동형임을 단언한다. 곧 위상적 조건인 단순연결성 하나만으로 등각형 분류가 끝나며, $$\mathbb{C}$$와 그 진부분집합이라는 단 두 개의 등각동형류만 남는다. 이 글은 그 증명을 전개한다. 핵심 도구는 국소적으로 유계인 정칙함수족이 정규족을 이룬다는 Montel 정리이며, 이를 써서 단위원판으로 가는 단사 정칙사상 가운데 한 점에서 도함수의 절댓값을 최대화하는 극값사상을 추출하고, 그 극값성이 사상을 전사로 강제함을 보인다. 단사성은 Hurwitz 정리가 보장한다.

## 정규족과 Montel 정리

증명의 전략은 변분적이다. 단위원판으로 가는 적당한 정칙사상들의 모임을 잡고 그 안에서 어떤 양을 최대화하는 원소를 찾는데, 이 최대화가 의미를 가지려면 최대화 수열의 극한이 다시 같은 모임 안에 머물러야 한다. 함수열의 극한을 다루는 콤팩트성의 언어가 정규족이다. 한 함수족이 정규족이라는 것은 그 안의 어떤 함수열에서든 콤팩트 집합 위에서 균등수렴하는 부분열을 뽑아낼 수 있다는 뜻이며, 이는 유계 수열에서 수렴 부분열을 뽑는 Bolzano–Weierstrass 정리의 함수공간 판본에 해당한다.

<div class="definition" markdown="1">

<ins id="def1">**정의 1 (정규족)**</ins> 열린집합 $$\Omega \subseteq \mathbb{C}$$ 위의 정칙함수들의 모임 $$\mathcal{F}$$가 *normal family<sub>정규족</sub>*라는 것은, $$\mathcal{F}$$의 임의의 함수열 $$(f_n)$$이 $$\Omega$$의 모든 콤팩트 부분집합 위에서 균등수렴하는 부분열 $$(f_{n_k})$$을 가지는 것을 뜻한다. 그 극한함수가 $$\mathcal{F}$$에 속할 것까지는 요구하지 않는다.

</div>

콤팩트 집합 위에서의 균등수렴을 보통 *국소균등수렴<sub>locally uniform convergence</sub>*이라 부르며, 이는 $$\Omega$$의 각 점이 그 위에서 균등수렴이 일어나는 근방을 가진다는 조건과 같다. 정칙함수열이 이렇게 국소균등수렴하면 그 극한도 정칙이므로, 정규족의 함수열에서 뽑은 부분열의 극한은 언제나 $$\Omega$$ 위의 정칙함수가 된다. 정규족의 정의 자체는 추상적이어서 어떤 족이 정규족인지 가려내는 판정법이 필요한데, 그 가장 강력한 형태가 Montel 정리이다. 그것은 함수값이 콤팩트 집합마다 유계라는 단순한 조건만으로 정규성을 이끌어 낸다. 증명의 두 축은 도함수의 유계성에서 나오는 동등연속성과, 가산조밀집합 위에서의 대각선논법이다. 먼저 유계성이 도함수의 유계성으로, 곧 동등연속성으로 옮겨짐을 본다.

<div class="proposition" markdown="1">

<ins id="lem2">**보조정리 2 (국소유계족의 동등연속성)**</ins> $$\mathcal{F}$$가 열린집합 $$\Omega \subseteq \mathbb{C}$$ 위의 정칙함수족이고 $$\Omega$$의 각 콤팩트 부분집합 위에서 *국소유계<sub>locally bounded</sub>*하다고 하자. 곧 임의의 콤팩트 집합 $$K \subseteq \Omega$$에 대하여 어떤 상수 $$M_K$$가 있어 모든 $$f \in \mathcal{F}$$과 $$z \in K$$에서 $$\lvert f(z)\rvert \leq M_K$$이다. 그러면 $$\mathcal{F}$$은 $$\Omega$$의 각 콤팩트 부분집합 위에서 동등연속이다. 곧 임의의 콤팩트 집합 $$K \subseteq \Omega$$과 $$\varepsilon > 0$$에 대하여 어떤 $$\delta > 0$$이 있어, $$z, w \in K$$이고 $$\lvert z - w\rvert < \delta$$이면 모든 $$f \in \mathcal{F}$$에서 $$\lvert f(z) - f(w)\rvert < \varepsilon$$이다.

</div>

<details class="proof" markdown="1">
<summary>증명</summary>

콤팩트 집합 $$K \subseteq \Omega$$을 고정한다. $$K$$이 $$\Omega$$의 콤팩트 부분집합이므로 그것과 $$\partial\Omega$$ 사이의 거리 $$3r = \operatorname{dist}(K, \partial\Omega) > 0$$이 양수이다 ($$\Omega = \mathbb{C}$$이면 $$r$$을 임의의 양수로 둔다). $$K$$의 각 점을 중심으로 반지름 $$2r$$인 닫힌 원판들의 합집합

$$L = \{\,z \in \mathbb{C} : \operatorname{dist}(z, K) \leq 2r\,\}$$

은 $$\Omega$$에 포함되는 콤팩트 집합이므로, 가정에 의해 어떤 상수 $$M = M_L$$이 있어 모든 $$f \in \mathcal{F}$$과 $$\zeta \in L$$에서 $$\lvert f(\zeta)\rvert \leq M$$이다.

이제 $$z, w \in K$$이고 $$\lvert z - w\rvert < r$$이라 하자. 중심 $$z$$, 반지름 $$2r$$인 원 $$\gamma$$ 위의 점 $$\zeta$$은 $$L$$에 속하고, $$z$$과 $$w$$ 모두 이 원의 내부에 있다 ($$\lvert z - w\rvert < r < 2r$$이므로). Cauchy 적분공식 ([§Cauchy 적분공식, ⁋정리 1](/ko/math/complex_analysis/cauchy_integral_formula#thm1)) 을 두 점에서 적용하여 빼면

$$f(z) - f(w) = \frac{1}{2\pi i}\oint_\gamma f(\zeta)\left(\frac{1}{\zeta - z} - \frac{1}{\zeta - w}\right)d\zeta = \frac{z - w}{2\pi i}\oint_\gamma \frac{f(\zeta)}{(\zeta - z)(\zeta - w)}\,d\zeta$$

이다. 원 $$\gamma$$ 위에서 $$\lvert \zeta - z\rvert = 2r$$이고, $$\lvert \zeta - w\rvert \geq \lvert \zeta - z\rvert - \lvert z - w\rvert > 2r - r = r$$이다. 따라서 피적분함수의 크기는 $$\lvert f(\zeta)\rvert / (\lvert \zeta - z\rvert\,\lvert \zeta - w\rvert) \leq M/(2r \cdot r)$$로 위로 유계이고, $$\gamma$$의 길이가 $$2\pi(2r) = 4\pi r$$이므로

$$\lvert f(z) - f(w)\rvert \leq \frac{\lvert z - w\rvert}{2\pi}\cdot\frac{M}{2r^2}\cdot 4\pi r = \frac{M}{r}\,\lvert z - w\rvert$$

이다. 이 어림은 $$f \in \mathcal{F}$$에 무관한 상수 $$M/r$$만을 담으므로, 주어진 $$\varepsilon > 0$$에 대해 $$\delta = \min(r, r\varepsilon/M)$$으로 두면 $$z, w \in K$$이고 $$\lvert z - w\rvert < \delta$$일 때 모든 $$f \in \mathcal{F}$$에서 $$\lvert f(z) - f(w)\rvert \leq (M/r)\lvert z - w\rvert < \varepsilon$$이다. 곧 $$\mathcal{F}$$이 $$K$$ 위에서 동등연속이다.

</details>

보조정리 2의 요점은 정칙함수의 도함수가 함숫값으로 제어된다는 데 있다. 실변수의 유계함수족은 얼마든지 가파르게 진동할 수 있어 동등연속성을 기대할 수 없지만, 정칙함수는 Cauchy 적분공식을 통해 한 점에서의 미분이 주위 원 위의 값들의 평균으로 표현되므로, 값이 유계이면 그 변화율도 자동으로 유계가 된다. 이 동등연속성이 Arzelà–Ascoli 형 논증과 결합하면 곧장 정규성을 준다.

<div class="proposition" markdown="1">

<ins id="thm3">**정리 3 (Montel)**</ins> $$\mathcal{F}$$가 열린집합 $$\Omega \subseteq \mathbb{C}$$ 위의 정칙함수족이고 $$\Omega$$의 각 콤팩트 부분집합 위에서 국소유계하다고 하자. 그러면 $$\mathcal{F}$$은 정규족이다.

</div>

<details class="proof" markdown="1">
<summary>증명</summary>

$$\mathcal{F}$$의 임의의 함수열 $$(f_n)$$을 잡아, $$\Omega$$의 모든 콤팩트 부분집합 위에서 균등수렴하는 부분열을 뽑는다.

먼저 $$\Omega$$ 안의 가산조밀집합 $$E = \{w_1, w_2, \dots\}$$을 택한다 (가령 $$\Omega$$에 속하는 유리좌표점 전체). 수열 $$(f_n(w_1))$$은 가정의 국소유계성에서 ($$\{w_1\}$$이 콤팩트이므로) 유계인 복소수열이고, Bolzano–Weierstrass 정리에 의해 수렴 부분열 $$(f_{n}^{(1)})$$을 가진다. 이 부분열에서 다시 점 $$w_2$$에서의 값이 수렴하도록 부분열 $$(f_n^{(2)})$$을 뽑고, 이를 거듭하면 부분열의 사슬 $$(f_n^{(1)}) \supseteq (f_n^{(2)}) \supseteq \cdots$$을 얻는데, $$(f_n^{(k)})$$은 $$w_1, \dots, w_k$$ 모두에서 수렴한다. 대각선열 $$g_n = f_n^{(n)}$$을 잡으면, 각 $$j$$에 대해 $$(g_n)$$은 $$n \geq j$$부터 $$(f_n^{(j)})$$의 부분열이므로 $$w_j$$에서 수렴한다. 곧 $$(g_n)$$은 $$E$$의 모든 점에서 수렴하는 $$(f_n)$$의 부분열이다.

이제 $$(g_n)$$이 $$\Omega$$의 임의의 콤팩트 집합 $$K$$ 위에서 균등수렴함을 보인다. 콤팩트성을 다루기 위해 $$K$$을 조금 부풀린 콤팩트 집합 $$K' = \{z : \operatorname{dist}(z, K) \leq \rho\} \subseteq \Omega$$ ($$\rho > 0$$ 충분히 작게) 위에서 작업한다. $$\varepsilon > 0$$이 주어졌을 때, 보조정리 2에 의해 $$K'$$ 위에서 $$\mathcal{F}$$이 동등연속이므로 어떤 $$\delta \in (0, \rho)$$이 있어 $$z, w \in K'$$, $$\lvert z - w\rvert < \delta$$이면 모든 $$n$$에서 $$\lvert g_n(z) - g_n(w)\rvert < \varepsilon/3$$이다. $$K$$이 콤팩트이므로 반지름 $$\delta$$인 원판들로 유한 덮개를 이루고, 각 원판의 중심을 $$E$$의 점으로 잡을 수 있다 ($$E$$이 조밀하므로). 이렇게 얻은 유한 개의 점 $$w_{j_1}, \dots, w_{j_p} \in E \cap K'$$은 $$K$$의 각 점이 그 가운데 적어도 하나와 거리 $$\delta$$ 안에 있도록 한다.

유한 개의 점 $$w_{j_1}, \dots, w_{j_p}$$ 각각에서 $$(g_n)$$이 수렴하므로 Cauchy 수열이고, 따라서 어떤 $$N$$이 있어 $$m, n \geq N$$이면 모든 $$i = 1, \dots, p$$에서 $$\lvert g_n(w_{j_i}) - g_m(w_{j_i})\rvert < \varepsilon/3$$이다. 이제 임의의 $$z \in K$$을 잡고, $$\lvert z - w_{j_i}\rvert < \delta$$인 중심 $$w_{j_i}$$을 고른다. $$m, n \geq N$$에 대해 삼각부등식으로

$$\lvert g_n(z) - g_m(z)\rvert \leq \lvert g_n(z) - g_n(w_{j_i})\rvert + \lvert g_n(w_{j_i}) - g_m(w_{j_i})\rvert + \lvert g_m(w_{j_i}) - g_m(z)\rvert < \frac{\varepsilon}{3} + \frac{\varepsilon}{3} + \frac{\varepsilon}{3} = \varepsilon$$

이다. 첫째와 셋째 항은 동등연속성에서, 둘째 항은 유한 개 점에서의 Cauchy 성질에서 나왔다. 이 어림이 $$z \in K$$에 무관한 $$N$$으로 성립하므로, $$(g_n)$$은 $$K$$ 위에서 균등 Cauchy 수열이고, $$\mathbb{C}$$의 완비성에 의해 $$K$$ 위에서 균등수렴한다. $$K$$이 임의의 콤팩트 집합이었으므로 $$(g_n)$$은 $$\Omega$$의 모든 콤팩트 부분집합 위에서 균등수렴한다. 따라서 $$\mathcal{F}$$은 정규족이다.

</details>

Montel 정리는 정칙함수족에 대한 콤팩트성 판정을 함숫값의 유계성이라는 검증하기 쉬운 조건으로 환원한다. 단위원판으로 가는 사상들은 그 값이 절댓값 $$1$$ 이하로 한꺼번에 유계이므로 자동으로 국소유계하고, 따라서 Montel 정리에 의해 정규족을 이룬다. 이것이 증명에서 극값사상을 추출할 때 쓰는 콤팩트성의 원천이다. 한편 극한사상이 다시 단사임을 보장하려면 단사 정칙함수열의 극한에 관한 사실이 필요한데, 그것이 Hurwitz 정리이다.

## Hurwitz 정리

정규족에서 뽑은 극한이 단사성을 잃지 않는지를 통제하려면, 단사 정칙함수열의 국소균등극한이 단사이거나 상수임을 알아야 한다. 이는 영점의 개수가 국소균등수렴 아래 안정적이라는 더 일반적인 사실의 특수한 경우이며, 그 안정성은 영점 수를 경계적분으로 세는 편각원리에서 나온다. 함수열이 균등수렴하면 그 대수적 미분 $$f_n'/f_n$$도 균등수렴하므로, 경계 위의 적분이 극한과 어울려 영점 수가 보존된다.

<div class="proposition" markdown="1">

<ins id="thm4">**정리 4 (Hurwitz)**</ins> $$\Omega \subseteq \mathbb{C}$$가 연결 열린집합이고 정칙함수열 $$(f_n)$$이 $$\Omega$$의 콤팩트 부분집합 위에서 정칙함수 $$f$$로 균등수렴한다고 하자. 만일 각 $$f_n$$이 $$\Omega$$에서 영점을 갖지 않으면, $$f$$은 $$\Omega$$에서 항등적으로 $$0$$이거나 영점을 갖지 않는다.

</div>

<details class="proof" markdown="1">
<summary>증명</summary>

국소균등극한 $$f$$은 정칙이다. $$f$$이 항등적으로 $$0$$이 아니라고 하고, $$f$$이 영점을 갖지 않음을 보인다. 어떤 $$z_0 \in \Omega$$에서 $$f(z_0) = 0$$이라 가정하여 모순을 이끈다. $$f$$의 영점이 고립되어 있으므로 ([§영점과 일치정리, ⁋명제 2](/ko/math/complex_analysis/zeros_and_identity_theorem#prop2)), 충분히 작은 $$\rho > 0$$을 잡아 닫힌 원판 $$\overline{D(z_0, \rho)} \subseteq \Omega$$ 안에서 $$f$$의 영점이 $$z_0$$ 하나뿐이도록 할 수 있다. 그러면 경계원 $$\gamma : \lvert z - z_0\rvert = \rho$$ 위에서 $$f(z) \neq 0$$이므로

$$\mu = \min_{z \in \gamma}\lvert f(z)\rvert > 0$$

이 양수이다 (콤팩트 집합 위 연속함수의 최솟값).

$$(f_n)$$이 $$\gamma$$ 위에서 $$f$$로 균등수렴하므로, 충분히 큰 $$n$$에 대해 $$\gamma$$ 위의 모든 점에서 $$\lvert f_n(z) - f(z)\rvert < \mu \leq \lvert f(z)\rvert$$이다. Rouché 정리 ([§편각원리와 Rouché 정리, ⁋명제 5](/ko/math/complex_analysis/argument_principle#prop5)) 를 $$f$$ (우세항) 과 $$f_n - f$$ (보정) 에 적용하면, $$f_n = f + (f_n - f)$$은 $$D(z_0, \rho)$$ 안에서 $$f$$과 같은 개수의 영점을 가진다. $$f$$은 그 안에서 $$z_0$$이라는 영점을 (위수만큼) 적어도 하나 가지므로, $$f_n$$도 $$D(z_0, \rho)$$ 안에서 적어도 하나의 영점을 가진다. 이는 $$f_n$$이 영점을 갖지 않는다는 가정에 어긋난다. 따라서 $$f$$은 $$\Omega$$에서 영점을 갖지 않는다.

</details>

Hurwitz 정리는 영점을 갖지 않는다는 성질이 국소균등극한 아래 보존됨을 말하되, 극한이 통째로 $$0$$으로 무너지는 퇴화의 가능성만을 예외로 남긴다. 이 정리에서 단사성에 관한 따름정리가 곧장 나온다. 단사 정칙함수열의 극한은 단사이거나 상수인데, 단사성을 깨는 유일한 길이 상수로 무너지는 것이기 때문이다.

<div class="proposition" markdown="1">

<ins id="cor5">**따름정리 5 (단사성의 보존)**</ins> $$\Omega \subseteq \mathbb{C}$$가 연결 열린집합이고 단사 정칙함수열 $$(f_n)$$이 $$\Omega$$의 콤팩트 부분집합 위에서 정칙함수 $$f$$로 균등수렴한다고 하자. 그러면 $$f$$은 단사이거나 상수이다.

</div>

<details class="proof" markdown="1">
<summary>증명</summary>

$$f$$이 상수가 아니라고 하고 단사임을 보인다. 단사성에 어긋난다고 가정하여, 서로 다른 두 점 $$a, b \in \Omega$$ ($$a \neq b$$) 에서 $$f(a) = f(b) = c$$이라 하자. 두 보조 함수열을 생각한다. 점 $$b$$을 포함하지 않는 연결 열린집합 $$\Omega' = \Omega \setminus \{b\}$$ 위에서 함수열

$$g_n(z) = f_n(z) - f_n(b)$$

을 본다. 각 $$f_n$$이 단사이므로 $$z \neq b$$이면 $$f_n(z) \neq f_n(b)$$, 곧 $$g_n(z) \neq 0$$이다. 따라서 $$g_n$$은 $$\Omega'$$에서 영점을 갖지 않는다. 한편 $$(f_n)$$이 $$f$$로, $$(f_n(b))$$이 $$f(b) = c$$로 수렴하므로 $$(g_n)$$은 $$\Omega'$$의 콤팩트 부분집합 위에서

$$g(z) = f(z) - c$$

로 균등수렴한다. 점 $$a \in \Omega'$$에서 $$g(a) = f(a) - c = 0$$이므로 $$g$$은 $$\Omega'$$에서 영점을 가진다. Hurwitz 정리 (정리 4) 에 의해, $$\Omega'$$에서 영점을 갖지 않는 $$g_n$$들의 극한 $$g$$이 영점을 가지려면 $$g$$이 $$\Omega'$$에서 항등적으로 $$0$$이어야 한다. 곧 $$\Omega'$$에서 $$f \equiv c$$이고, 연속성에서 $$\Omega$$ 전체에서 $$f \equiv c$$이라 $$f$$이 상수이다. 이는 $$f$$이 상수가 아니라는 가정에 어긋난다. 따라서 $$f$$은 단사이다.

</details>

따름정리 5는 극값사상을 추출할 때 그 극한이 단사성을 유지하도록 보장하는 마지막 부품이다. 단사 정칙사상들의 모임에서 콤팩트성으로 극한을 뽑으면, 그 극한은 상수가 아니기만 하면 다시 단사여서 같은 모임에 머문다. 이제 Montel 정리와 따름정리 5를 손에 쥐었으니, 이를 결합하여 Riemann 사상정리를 증명한다.

## Riemann 사상정리

정리의 진술부터 정확히 한다. $$\mathbb{C}$$ 전체는 단위원판과 등각동형일 수 없는데, $$\mathbb{C}$$ 위의 유계 전해석함수가 상수뿐이라는 Liouville 정리가 단위원판으로 가는 비상수 사상의 존재를 막기 때문이다. 따라서 영역이 $$\mathbb{C}$$의 진부분집합이라는 조건이 필수적이며, 단순연결성과 함께 이 둘이 정확히 충분조건이 됨이 정리의 내용이다. 사상의 유일성을 위해 한 점에서의 정규화를 덧붙인다.

<div class="proposition" markdown="1">

<ins id="thm6">**정리 6 (Riemann 사상정리)**</ins> $$\Omega \subsetneq \mathbb{C}$$가 공집합이 아닌 단순연결 열린집합이라 하자. 그러면 임의로 고정한 점 $$z_0 \in \Omega$$에 대하여, $$\Omega$$를 단위원판 $$\mathbb{D} = \{z : \lvert z\rvert < 1\}$$ 위로 보내는 정칙 전단사사상 $$f : \Omega \to \mathbb{D}$$이 존재하며, 그 가운데

$$f(z_0) = 0, \qquad f'(z_0) > 0$$

을 만족하는 것이 유일하게 하나 있다. 특히 $$\Omega$$은 $$\mathbb{D}$$와 등각동형이다.

</div>

증명은 존재성과 유일성으로 나뉜다. 유일성은 단위원판의 자기동형사상 분류에서 곧장 따라 나오므로 이를 먼저 처리하고, 존재성은 다음 절들에서 변분적 구성으로 확립한다.

<details class="proof" markdown="1">
<summary>유일성의 증명</summary>

$$f, g : \Omega \to \mathbb{D}$$이 모두 정규화 조건을 만족하는 정칙 전단사사상이라 하자. 합성 $$h = g \circ f^{-1} : \mathbb{D} \to \mathbb{D}$$은 정칙 전단사사상이고 그 역사상도 정칙이므로 ([§편각원리와 Rouché 정리, ⁋따름정리 9](/ko/math/complex_analysis/argument_principle#cor9)), $$\mathbb{D}$$의 정칙 자기동형사상이다. 또 $$f(z_0) = g(z_0) = 0$$이므로 $$h(0) = g(f^{-1}(0)) = g(z_0) = 0$$이라 $$h$$은 원점을 고정한다. 원점을 고정하는 단위원판의 자기동형사상은 회전뿐이므로 ([§영점과 일치정리, ⁋예시 8](/ko/math/complex_analysis/zeros_and_identity_theorem#ex8)), 어떤 실수 $$\theta$$에 대해 $$h(w) = e^{i\theta}w$$이다.

이제 정규화의 둘째 조건을 쓴다. $$g = h \circ f$$이므로 연쇄법칙으로 $$g'(z_0) = h'(f(z_0))\,f'(z_0) = h'(0)\,f'(z_0) = e^{i\theta}f'(z_0)$$이다. 가정에서 $$f'(z_0) > 0$$과 $$g'(z_0) > 0$$이 모두 양의 실수이므로, $$e^{i\theta} = g'(z_0)/f'(z_0)$$도 양의 실수이고 절댓값이 $$1$$이라 $$e^{i\theta} = 1$$이다. 따라서 $$h = \mathrm{id}$$이고 $$g = f$$이다.

</details>

유일성의 논증은 두 정규화 사상의 차이가 원점을 고정하는 자기동형사상, 곧 회전으로 환원되고, 도함수가 양의 실수라는 조건이 그 회전을 항등으로 못 박음을 보인다. 정규화 조건 $$f'(z_0) > 0$$은 사상을 회전의 자유도만큼 고정하는 위상고정 장치인 셈이다. 남은 것은 존재성이며, 이를 위해 단위원판으로 가는 단사 정칙사상들의 모임을 도입한다.

## 후보족의 비어 있지 않음

존재성 증명의 무대는 다음 함수족이다. $$z_0 \in \Omega$$을 고정한 채, $$\Omega$$를 단위원판 안으로 단사로 보내며 $$z_0$$을 원점으로 옮기는 정칙사상 전체를 모은다.

$$\mathcal{F} = \{\, f : \Omega \to \mathbb{D} \mid f \text{ 정칙},\ f \text{ 단사},\ f(z_0) = 0 \,\}.$$

이 족 안에서 $$\lvert f'(z_0)\rvert$$을 최대화하는 원소를 찾고, 그것이 전사임을 보이는 것이 전략이다. 변분이 의미를 가지려면 우선 $$\mathcal{F}$$이 비어 있지 않아야 하는데, 여기서 단순연결성이 결정적으로 쓰인다. $$\Omega$$이 $$\mathbb{C}$$의 진부분집합이라 어떤 점 $$a \notin \Omega$$이 있고, $$\Omega$$이 단순연결이라 $$z - a$$의 정칙 제곱근을 $$\Omega$$ 위에서 뽑을 수 있다. 이 제곱근이 $$\mathcal{F}$$의 원소를 만드는 씨앗이다.

<div class="proposition" markdown="1">

<ins id="lem7">**보조정리 7 ($$\mathcal{F}$$의 비어 있지 않음)**</ins> $$\Omega \subsetneq \mathbb{C}$$가 공집합이 아닌 단순연결 열린집합이고 $$z_0 \in \Omega$$이라 하자. 그러면 위의 족 $$\mathcal{F}$$은 비어 있지 않다.

</div>

<details class="proof" markdown="1">
<summary>증명</summary>

$$\Omega \neq \mathbb{C}$$이므로 $$a \notin \Omega$$인 점 $$a$$을 택한다. 그러면 $$z - a$$은 $$\Omega$$에서 영점을 갖지 않는 정칙함수이다. $$\Omega$$이 단순연결이므로 이 함수의 정칙 제곱근이 존재한다. 곧 어떤 정칙함수 $$\varphi : \Omega \to \mathbb{C}$$이 있어

$$\varphi(z)^2 = z - a \qquad (z \in \Omega)$$

이다 (단순연결 영역에서 영점 없는 정칙함수는 정칙 로그를 가지므로, $$\varphi = \exp(\tfrac{1}{2}\log(z - a))$$으로 제곱근이 정의된다).

먼저 $$\varphi$$이 단사임을 본다. $$\varphi(z_1) = \varphi(z_2)$$이면 양변을 제곱하여 $$z_1 - a = z_2 - a$$, 곧 $$z_1 = z_2$$이다. 또 $$\varphi$$은 더 강한 성질을 가진다. $$\varphi(z_1) = -\varphi(z_2)$$이어도 양변을 제곱하면 $$z_1 = z_2$$이 되어 $$\varphi(z_1) = -\varphi(z_1)$$, 곧 $$\varphi(z_1) = 0$$인데, $$\varphi(z_1)^2 = z_1 - a \neq 0$$이라 이는 불가능하다. 따라서 $$\varphi$$의 상 $$\varphi(\Omega)$$은 어떤 점 $$w$$을 포함하면 $$-w$$은 포함하지 않는다.

$$\varphi$$은 비상수 정칙 단사사상이므로 열린사상이고 ([§편각원리와 Rouché 정리, ⁋정리 8](/ko/math/complex_analysis/argument_principle#thm8)), 따라서 $$\varphi(\Omega)$$은 어떤 점 $$w_0 = \varphi(z_0)$$을 중심으로 하는 원판 $$D(w_0, r) \subseteq \varphi(\Omega)$$ ($$r > 0$$) 을 포함한다. 방금 본 성질에서 $$\varphi(\Omega)$$은 원판 $$D(-w_0, r)$$과 만나지 않는다 ($$D(-w_0, r)$$의 점 $$-w$$은 $$w \in D(w_0, r) \subseteq \varphi(\Omega)$$에 대응하는데 그러한 $$-w$$은 상에 없으므로). 곧 모든 $$z \in \Omega$$에서

$$\lvert \varphi(z) + w_0\rvert \geq r$$

이다. 이로써 $$\varphi(\Omega)$$이 한 원판을 통째로 비껴가므로, 그 여백을 이용해 $$\varphi$$을 단위원판 안으로 밀어 넣는다. 사상

$$\psi(z) = \frac{r}{2\,(\varphi(z) + w_0)}$$

을 보면, 분모의 절댓값이 $$r$$ 이상이므로 $$\lvert \psi(z)\rvert \leq r/(2r) = 1/2 < 1$$이라 $$\psi : \Omega \to \mathbb{D}$$이다. 또 $$\psi$$은 단사인 $$\varphi$$에 Möbius 변환 ([§등각사상과 Möbius 변환, ⁋정의 4](/ko/math/complex_analysis/conformal_maps#def4)) 을 합성한 것이라 단사이고 정칙이다.

끝으로 $$z_0$$을 원점으로 옮기도록 보정한다. $$b = \psi(z_0) \in \mathbb{D}$$이라 두고, 단위원판의 자기동형사상 $$\varphi_b(w) = (w - b)/(1 - \bar b w)$$ ([§등각사상과 Möbius 변환, ⁋명제 11](/ko/math/complex_analysis/conformal_maps#prop11)) 을 합성하여

$$f = \varphi_b \circ \psi : \Omega \to \mathbb{D}$$

을 정의하면, $$f$$은 정칙이고 단사이며 ($$\varphi_b$$이 $$\mathbb{D}$$의 자기동형사상이므로) $$f(z_0) = \varphi_b(b) = 0$$이다. 따라서 $$f \in \mathcal{F}$$이고 $$\mathcal{F} \neq \varnothing$$이다.

</details>

보조정리 7은 단순연결성을 두 곳에서 쓴다. 하나는 영점 없는 정칙함수 $$z - a$$의 정칙 제곱근을 뽑는 데이고, 다른 하나는 그 제곱근이 상에서 한 원판을 통째로 비껴가게 만드는 데이다. 제곱근의 두 가지 $$\pm\varphi$$ 가운데 한쪽만 상에 나타난다는 사실이 핵심 장치로, 이 빈 원판을 반전으로 단위원판 안에 가두어 $$\mathcal{F}$$의 첫 원소를 짓는다. 정칙 제곱근의 존재 자체가 단순연결성의 직접적 귀결이므로, 이 보조정리에서 정리의 위상적 가정이 본질적으로 소비된다. 이제 비어 있지 않은 $$\mathcal{F}$$ 위에서 극값사상을 추출한다.

## 극값사상의 추출과 전사성

후보족 $$\mathcal{F}$$ 위에서 도함수의 절댓값 $$\lvert f'(z_0)\rvert$$을 최대화하는 사상을 찾는다. 이 최댓값이 실제로 달성됨을 Montel 정리가 보장하고, 그 극값사상이 단사임을 Hurwitz 정리의 따름정리가 보장하며, 마지막으로 그 사상이 전사일 수밖에 없음을 Schwarz 보조정리가 강제한다.

<div class="proposition" markdown="1">

<ins id="thm8">**정리 8 (극값사상의 전사성)**</ins> $$\Omega \subsetneq \mathbb{C}$$가 공집합이 아닌 단순연결 열린집합이고 $$z_0 \in \Omega$$이라 하자. 양

$$M = \sup_{f \in \mathcal{F}} \lvert f'(z_0)\rvert$$

은 유한하고 양수이며, 이 상한을 달성하는 $$f^\ast \in \mathcal{F}$$이 존재한다. 더 나아가 이러한 극값사상 $$f^\ast$$은 $$\Omega$$를 $$\mathbb{D}$$ 위로 보내는 전사사상이다.

</div>

<details class="proof" markdown="1">
<summary>증명</summary>

먼저 $$M$$이 양수임을 본다. 보조정리 7로 어떤 $$f_1 \in \mathcal{F}$$이 존재하고, $$f_1$$이 단사이므로 그 도함수가 어디서도 $$0$$이 아니라 ([§등각사상과 Möbius 변환, ⁋명제 3](/ko/math/complex_analysis/conformal_maps#prop3)) $$\lvert f_1'(z_0)\rvert > 0$$이다. 따라서 $$M \geq \lvert f_1'(z_0)\rvert > 0$$이다.

다음으로 $$M$$이 유한하고 달성됨을 본다. $$\overline{D(z_0, \rho)} \subseteq \Omega$$인 $$\rho > 0$$을 잡고 경계원 $$\lvert z - z_0\rvert = \rho$$ 위에서 Cauchy 미분공식 ([§Cauchy 적분공식, ⁋정리 2](/ko/math/complex_analysis/cauchy_integral_formula#thm2)) 을 쓰면, 모든 $$f \in \mathcal{F}$$에서 $$\lvert f\rvert \leq 1$$이므로

$$\lvert f'(z_0)\rvert = \left\lvert\frac{1}{2\pi i}\oint_{\lvert z - z_0\rvert = \rho}\frac{f(z)}{(z - z_0)^2}\,dz\right\rvert \leq \frac{1}{2\pi}\cdot\frac{1}{\rho^2}\cdot 2\pi\rho = \frac{1}{\rho}$$

이라 $$M \leq 1/\rho < \infty$$이다. 상한의 정의에서 $$\lvert f_n'(z_0)\rvert \to M$$인 함수열 $$(f_n) \subseteq \mathcal{F}$$을 택한다. $$\mathcal{F}$$의 모든 함수가 절댓값 $$1$$로 유계라 국소유계하므로 Montel 정리 (정리 3) 에 의해 $$\mathcal{F}$$은 정규족이고, $$(f_n)$$의 부분열이 $$\Omega$$의 콤팩트 부분집합 위에서 어떤 정칙함수 $$f^\ast$$로 균등수렴한다. 이 부분열을 다시 $$(f_n)$$이라 적는다.

$$f^\ast$$이 $$\mathcal{F}$$에 속함을 확인한다. 국소균등수렴에서 도함수도 국소균등수렴하므로 $$f^\ast{}'(z_0) = \lim_n f_n'(z_0)$$이고 $$\lvert f^\ast{}'(z_0)\rvert = M > 0$$이라 $$f^\ast$$은 비상수이다. 각 $$f_n$$이 단사이므로 따름정리 5에 의해 그 극한 $$f^\ast$$은 단사이거나 상수인데, 방금 비상수임을 보았으니 단사이다. 또 각 $$f_n$$이 $$\mathbb{D}$$로 가므로 $$\lvert f^\ast\rvert \leq 1$$이고, $$f^\ast$$이 비상수 정칙사상이라 열린사상이므로 ([§편각원리와 Rouché 정리, ⁋정리 8](/ko/math/complex_analysis/argument_principle#thm8)) 그 상이 열려 있어 경계 $$\lvert w\rvert = 1$$에 닿을 수 없다. 따라서 $$\lvert f^\ast\rvert < 1$$, 곧 $$f^\ast : \Omega \to \mathbb{D}$$이다. 끝으로 $$f^\ast(z_0) = \lim_n f_n(z_0) = 0$$이다. 그러므로 $$f^\ast \in \mathcal{F}$$이고 $$\lvert f^\ast{}'(z_0)\rvert = M$$이라 상한이 달성된다.

이제 $$f^\ast$$이 전사임을 보인다. 전사가 아니라고 가정하여, 어떤 $$\alpha \in \mathbb{D}$$이 $$f^\ast$$의 상에 들지 않는다고 하자. 곧 모든 $$z \in \Omega$$에서 $$f^\ast(z) \neq \alpha$$이다. 이때 $$\lvert f^\ast{}'(z_0)\rvert$$을 더 크게 만드는 $$\mathcal{F}$$의 원소를 짜내어 극값성에 모순을 일으킨다. 단위원판의 자기동형사상 $$\varphi_\alpha(w) = (w - \alpha)/(1 - \bar\alpha w)$$ ([§등각사상과 Möbius 변환, ⁋명제 11](/ko/math/complex_analysis/conformal_maps#prop11)) 을 합성한 함수

$$F(z) = \varphi_\alpha(f^\ast(z)) = \frac{f^\ast(z) - \alpha}{1 - \bar\alpha f^\ast(z)}$$

을 본다. $$F : \Omega \to \mathbb{D}$$은 정칙 단사이고, $$f^\ast$$이 $$\alpha$$을 취하지 않으므로 $$F$$은 $$\Omega$$에서 영점을 갖지 않는다. $$\Omega$$이 단순연결이고 $$F$$가 영점을 갖지 않으므로, 단순연결 영역 위 영점 없는 정칙함수가 정칙 제곱근을 가진다는 사실에 의해 영점 없는 $$F$$의 정칙 제곱근

$$G(z), \qquad G(z)^2 = F(z)$$

이 존재한다. $$\lvert F\rvert < 1$$이므로 $$\lvert G\rvert < 1$$이라 $$G : \Omega \to \mathbb{D}$$이고, 제곱이 단사인 $$F$$이므로 $$G$$도 단사이다 ($$G(z_1) = G(z_2)$$이면 제곱하여 $$F(z_1) = F(z_2)$$, 곧 $$z_1 = z_2$$).

이제 $$z_0$$을 원점으로 옮기도록 보정한다. $$\beta = G(z_0) \in \mathbb{D}$$이라 두고 $$h = \varphi_\beta \circ G$$, 곧

$$h(z) = \frac{G(z) - \beta}{1 - \bar\beta G(z)}$$

을 정의하면 $$h \in \mathcal{F}$$이다 ($$h$$은 정칙 단사이고 $$\mathbb{D}$$로 가며 $$h(z_0) = 0$$). $$h$$의 도함수를 $$z_0$$에서 계산하기 위해 $$f^\ast$$을 $$h$$으로 되돌리는 사상을 구성한다. 제곱사상 $$s(w) = w^2$$과 위에서 쓴 자기동형사상들로

$$f^\ast = \varphi_\alpha^{-1} \circ s \circ \varphi_\beta^{-1} \circ h =: \Phi \circ h, \qquad \Phi = \varphi_\alpha^{-1} \circ s \circ \varphi_\beta^{-1}$$

이 성립한다 (실제로 $$\varphi_\beta^{-1}(h) = G$$, $$s(G) = G^2 = F$$, $$\varphi_\alpha^{-1}(F) = f^\ast$$). 여기서 $$\Phi : \mathbb{D} \to \mathbb{D}$$은 정칙이고 $$\Phi(0) = \varphi_\alpha^{-1}(s(\varphi_\beta^{-1}(0))) = \varphi_\alpha^{-1}(s(\beta))$$인데, $$s(\beta) = \beta^2 = G(z_0)^2 = F(z_0) = \varphi_\alpha(f^\ast(z_0)) = \varphi_\alpha(0)$$이므로 $$\Phi(0) = \varphi_\alpha^{-1}(\varphi_\alpha(0)) = 0$$이다. 곧 $$\Phi$$은 원점을 고정하는 $$\mathbb{D} \to \mathbb{D}$$ 정칙사상이다.

$$\Phi$$은 자기동형사상이 아니다. 자기동형사상들의 합성 사이에 제곱사상 $$s(w) = w^2$$이 끼어 있는데, $$s$$은 $$\mathbb{D}$$ 위에서 단사가 아니라 ($$\pm w$$이 같은 값을 주므로) 자기동형사상이 될 수 없고, 따라서 그 합성 $$\Phi$$도 단사가 아니어서 자기동형사상이 아니다. 그러므로 Schwarz 보조정리 ([§영점과 일치정리, ⁋정리 7](/ko/math/complex_analysis/zeros_and_identity_theorem#thm7)) 의 등호조건에서, 원점을 고정하지만 회전이 아닌 정칙사상은 도함수의 절댓값이 엄격히 $$1$$ 미만이다. 곧

$$\lvert \Phi'(0)\rvert < 1$$

이다. 연쇄법칙으로 $$f^\ast{}'(z_0) = \Phi'(h(z_0))\,h'(z_0) = \Phi'(0)\,h'(z_0)$$이므로

$$M = \lvert f^\ast{}'(z_0)\rvert = \lvert \Phi'(0)\rvert\,\lvert h'(z_0)\rvert < \lvert h'(z_0)\rvert$$

이다. 그런데 $$h \in \mathcal{F}$$이므로 $$\lvert h'(z_0)\rvert \leq M$$이어야 하는데 이는 $$M < \lvert h'(z_0)\rvert \leq M$$이라는 모순이다. 따라서 $$f^\ast$$은 전사이다.

</details>

정리 8의 전사성 논증이 증명 전체의 정수이다. 극값사상이 한 점 $$\alpha$$을 놓쳤다고 가정하면, 그 빈자리를 제곱근으로 메워 도함수를 더 키운 새 사상을 만들 수 있는데, 이는 $$\lvert f'(z_0)\rvert$$이 이미 최대였다는 데 모순이다. 도함수를 키우는 메커니즘은 제곱사상 $$w \mapsto w^2$$이 단위원판을 자기 자신으로 두 겹 덮으면서 원점 근처를 늘인다는 사실이며, Schwarz 보조정리가 그 늘림을 정량적으로 $$\lvert \Phi'(0)\rvert < 1$$로 포착한다. 곧 전사성은 빈틈을 허용하지 않는 극값성의 직접적 귀결이고, 이로써 $$f^\ast : \Omega \to \mathbb{D}$$은 정칙 전단사사상이다.

이제 정리 6의 존재성이 마무리된다. 정리 8의 극값사상 $$f^\ast$$은 $$\Omega$$를 $$\mathbb{D}$$ 위로 보내는 정칙 전단사사상이고 $$f^\ast(z_0) = 0$$을 만족한다. 도함수 조건만 맞추면 되는데, $$f^\ast{}'(z_0) = \lvert f^\ast{}'(z_0)\rvert e^{i\vartheta}$$ ($$\vartheta = \arg f^\ast{}'(z_0)$$) 으로 적고 회전 $$e^{-i\vartheta}$$을 합성한 $$f = e^{-i\vartheta}f^\ast$$을 보면, 이 역시 $$\mathbb{D}$$로 가는 정칙 전단사사상이고 $$f(z_0) = 0$$이며

$$f'(z_0) = e^{-i\vartheta}f^\ast{}'(z_0) = e^{-i\vartheta}\lvert f^\ast{}'(z_0)\rvert e^{i\vartheta} = \lvert f^\ast{}'(z_0)\rvert = M > 0$$

이라 $$f'(z_0) > 0$$이다. 따라서 정규화 조건을 만족하는 정칙 전단사사상 $$f : \Omega \to \mathbb{D}$$이 존재하고, 이미 보인 유일성과 합쳐 정리 6이 증명된다. $$\Omega$$이 $$\mathbb{D}$$와 등각동형이라는 결론은 정칙 전단사사상 $$f$$이 등각사상이라는 사실 ([§등각사상과 Möbius 변환, ⁋명제 3](/ko/math/complex_analysis/conformal_maps#prop3)) 에서 곧장 따라 나온다.

<div class="remark" markdown="1">

<ins id="rmk9">**참고 9 (경계 거동)**</ins> Riemann 사상정리는 등각동형사상의 존재만을 단언할 뿐, 그 사상이 영역의 경계까지 연속적으로 확장되는지는 말하지 않는다. 경계가 충분히 좋은 경우, 가령 $$\partial\Omega$$이 Jordan 곡선이면 사상이 폐포 $$\overline{\Omega}$$에서 $$\overline{\mathbb{D}}$$로의 위상동형으로 확장된다는 것이 Carathéodory의 정리이지만, 일반적인 단순연결 영역에서는 경계가 프랙탈처럼 거칠어 그러한 확장이 성립하지 않을 수 있다. 본문의 변분적 증명은 내부에서의 등각동형만을 다루므로 경계 거동과는 무관하게 작동한다.

</div>

참고 9가 강조하듯, 정리의 내용은 철저히 영역 내부에 관한 것이다. 단순연결성이라는 위상적 가정만으로 내부의 등각형이 단위원판 하나로 통일된다는 사실은, 복소해석학에서 위상과 등각기하가 맞물리는 가장 깊은 지점 가운데 하나이다. 단순연결이 아닌 영역에서는 사정이 전혀 달라, 가령 환형 영역들은 그 안팎 반지름의 비라는 등각불변량으로 서로 구별되어 단 하나의 표준영역으로 환원되지 않는다.

---

**참고문헌**

**[Ahl]** L.V. Ahlfors, *Complex analysis*, 3rd ed., McGraw–Hill, 1979.

**[Con]** J.B. Conway, *Functions of one complex variable I*, 2nd ed., Graduate Texts in Mathematics 11, Springer, 1978.

**[Rud]** W. Rudin, *Real and complex analysis*, 3rd ed., McGraw–Hill, 1987.

**[SS]** E.M. Stein, R. Shakarchi, *Complex analysis*, Princeton Lectures in Analysis II, Princeton University Press, 2003.
</content>
</invoke>
