---
title: "영점과 일치정리"
description: "항등적으로 0이 아닌 정칙함수의 영점이 고립되어 있고 유한 위수를 가짐을 보인 뒤, 이를 바탕으로 연결 영역에서 정칙함수가 집적점을 갖는 집합에서의 값으로 완전히 결정된다는 일치정리를 증명한다. 이어 비상수 정칙함수의 절댓값이 내부에서 최댓값을 갖지 못한다는 최대절댓값 원리와 단위원판의 자기사상을 통제하는 Schwarz 보조정리를 다룬다."
excerpt: "영점의 고립성, 영점의 위수, 일치정리, 해석적 접속, 최대절댓값 원리, Schwarz 보조정리"

categories: [Math / Complex Analysis]
permalink: /ko/math/complex_analysis/zeros_and_identity_theorem
sidebar: 
    nav: "complex_analysis-ko"

date: 2026-06-21
weight: 7

published: false
---

정칙함수가 각 점 근방에서 자신의 Taylor 급수와 일치한다는 사실은 ([§멱급수와 해석성, ⁋정리 3](/ko/math/complex_analysis/power_series_and_analyticity#thm3)) 그 국소적 거동에 강한 제약을 건다. 가장 먼저 드러나는 것이 영점의 거동이다. 항등적으로 $$0$$이 아닌 정칙함수의 영점에서는 Taylor 급수의 상수항이 사라지되 어느 유한한 차수의 계수는 살아남아야 하고, 이로부터 영점이 $$(z - z_0)^m$$이라는 정확한 인수를 내놓으며 ([§멱급수와 해석성, ⁋명제 6](/ko/math/complex_analysis/power_series_and_analyticity#prop6)) 서로 떨어져 고립된다는 결론이 나온다. 영점이 고립된다는 이 국소적 사실을 연결성과 결합하면, 두 정칙함수가 집적점을 갖는 작은 집합에서만 일치해도 영역 전체에서 일치한다는 일치정리에 이른다. 정칙함수는 이렇듯 극히 적은 자료로 완전히 결정되는 강직한 대상이며, 이 강직성은 최대절댓값 원리와 단위원판의 자기사상을 통제하는 Schwarz 보조정리로 이어진다. 이 글에서 다루는 결과들은 모두 멱급수 전개라는 하나의 원천에서 흘러나온다.

## 영점의 고립성

영점의 위수와 그에 따른 인수분해는 이미 멱급수 전개의 직접적 귀결로 확립되었다 ([§멱급수와 해석성, ⁋정의 5](/ko/math/complex_analysis/power_series_and_analyticity#def5), [⁋명제 6](/ko/math/complex_analysis/power_series_and_analyticity#prop6)). 여기서는 그 인수분해가 함의하는 위상적 사실, 곧 영점이 서로 떨어져 고립되어 있다는 명제를 정식으로 적고 증명한다. 핵심은 인수분해 $$f(z) = (z - z_0)^m g(z)$$에서 남는 인수 $$g$$가 영점에서 $$0$$이 아니므로, 연속성에 의해 그 근방 전체에서 $$0$$에서 떨어져 있다는 데 있다.

<div class="definition" markdown="1">

<ins id="def1">**정의 1 (고립점)**</ins> 집합 $$S \subseteq \mathbb{C}$$의 점 $$z_0 \in S$$가 $$S$$의 *isolated point<sub>고립점</sub>*라는 것은, $$z_0$$의 어떤 근방 $$D(z_0, \varepsilon)$$ 안에서 $$S$$의 점이 $$z_0$$ 하나뿐인 것, 곧

$$D(z_0, \varepsilon) \cap S = \{z_0\}$$

인 $$\varepsilon > 0$$이 존재하는 것을 뜻한다. $$S$$의 모든 점이 고립점이면 $$S$$를 *discrete set<sub>이산집합</sub>*이라 한다.

</div>

고립점이라는 개념은 영점이 모여 있지 않고 흩어져 있다는 상황을 정확히 포착한다. 정칙함수 $$f$$의 영점집합을 $$Z(f) = \{z : f(z) = 0\}$$이라 적으면, 다음 명제는 $$f$$가 항등적으로 $$0$$이 아닌 한 $$Z(f)$$의 모든 점이 고립점임을 말한다.

<div class="proposition" markdown="1">

<ins id="prop2">**명제 2 (영점의 고립성)**</ins> $$f$$가 점 $$z_0$$의 한 근방에서 정칙이고 $$f(z_0) = 0$$이라 하자. 그러면 다음 둘 중 정확히 하나가 성립한다.

1. $$f$$가 $$z_0$$의 어떤 근방에서 항등적으로 $$0$$이다.
2. $$z_0$$이 $$f$$의 영점집합의 고립점이다. 곧 어떤 $$\varepsilon > 0$$이 있어 $$0 < \lvert z - z_0\rvert < \varepsilon$$인 모든 $$z$$에서 $$f(z) \neq 0$$이다.

</div>

<details class="proof" markdown="1">
<summary>증명</summary>

$$z_0$$의 한 원판 $$D(z_0, R)$$에서 $$f$$가 정칙이므로 정리에 의해 ([§멱급수와 해석성, ⁋정리 1](/ko/math/complex_analysis/power_series_and_analyticity#thm1)) 그 원판에서 $$f(z) = \sum_{n=0}^{\infty} a_n (z - z_0)^n$$, $$a_n = f^{(n)}(z_0)/n!$$이다.

만일 모든 $$n$$에 대해 $$a_n = 0$$이면 Taylor 급수가 항등적으로 $$0$$이므로 $$f$$가 $$D(z_0, R)$$에서 항등적으로 $$0$$이 되어 경우 (1)이 성립한다.

그렇지 않으면 $$a_n \neq 0$$인 $$n$$이 존재하므로 $$m = \min\{n : a_n \neq 0\}$$이 잘 정의되고, $$a_0 = f(z_0) = 0$$이므로 $$m \geq 1$$이다. 곧 $$f$$는 $$z_0$$에서 위수 $$m$$인 영점을 가져 ([§멱급수와 해석성, ⁋정의 5](/ko/math/complex_analysis/power_series_and_analyticity#def5)), 인수분해 ([§멱급수와 해석성, ⁋명제 6](/ko/math/complex_analysis/power_series_and_analyticity#prop6)) 에 의해 $$z_0$$의 어떤 근방에서 정칙이고 $$g(z_0) \neq 0$$인 $$g$$가 있어

$$f(z) = (z - z_0)^m\,g(z)$$

이다. $$g$$가 $$z_0$$에서 정칙이므로 연속이고 $$g(z_0) \neq 0$$이므로, 연속성에 의해 어떤 $$\varepsilon > 0$$이 있어 $$\lvert z - z_0\rvert < \varepsilon$$인 모든 $$z$$에서 $$g(z) \neq 0$$이다. 이러한 $$z$$ 가운데 $$z \neq z_0$$이면 $$(z - z_0)^m \neq 0$$이고 $$g(z) \neq 0$$이므로 $$f(z) \neq 0$$이다. 따라서 $$z_0$$은 $$f$$의 영점집합의 고립점이 되어 경우 (2)가 성립한다.

두 경우는 양립할 수 없다. (1)이면 $$z_0$$의 임의의 근방에 $$z_0$$ 아닌 영점이 가득하므로 (2)에 어긋나고, (2)이면 구멍낸 근방에 영점이 없으므로 (1)에 어긋난다.

</details>

명제 2는 정칙함수의 영점이 가질 수 있는 두 가지 극단을 가른다. 한 점에서 모든 Taylor 계수가 사라지면 함수가 그 근방에서 통째로 소멸하고, 그렇지 않으면 그 영점은 주위에 다른 영점을 두지 않은 채 홀로 떨어진다. 그 사이의 중간, 가령 영점이 한 점에 수렴하면서도 함수가 항등적으로 $$0$$은 아닌 상황은 정칙함수에서 일어날 수 없다. 이 사실이 다음 절의 일치정리를 떠받친다. 영점이 집적할 수 있는 유일한 길이 함수가 국소적으로 소멸하는 것뿐이라면, 영점의 집적은 곧 함수의 광역적 소멸로 번지기 때문이다.

## 일치정리

정칙함수가 적은 자료로 결정된다는 강직성이 가장 선명하게 드러나는 곳이 일치정리이다. 두 정칙함수가 어떤 집적점을 갖는 집합에서 일치하면, 그 차가 집적점을 갖는 영점집합을 가지므로 명제 2에 의해 국소적으로 소멸하고, 이 국소적 소멸이 연결성을 따라 영역 전체로 퍼져 두 함수가 어디서나 일치하게 된다. 우선 차함수의 소멸로 문제를 환원하는 형태로 적은 뒤, 두 함수의 일치라는 일상적 형태로 옮긴다.

<div class="proposition" markdown="1">

<ins id="thm3">**정리 3 (일치정리)**</ins> $$\Omega \subseteq \mathbb{C}$$가 연결 열린집합이고 $$f, g$$가 $$\Omega$$에서 정칙이라 하자. 만일 두 함수가 일치하는 집합

$$S = \{z \in \Omega : f(z) = g(z)\}$$

이 $$\Omega$$ 안에 집적점을 가지면, 곧 어떤 점 $$z_\ast \in \Omega$$과 $$S$$의 서로 다른 점들의 수열 $$z_k \to z_\ast$$이 존재하면, $$\Omega$$ 전체에서 $$f = g$$이다.

</div>

<details class="proof" markdown="1">
<summary>증명</summary>

$$h = f - g$$로 두면 $$h$$는 $$\Omega$$에서 정칙이고 ([§정칙함수, ⁋명제 3](/ko/math/complex_analysis/holomorphic_functions#prop3)) $$S = Z(h) = \{z : h(z) = 0\}$$이다. $$S$$가 $$\Omega$$ 안에 집적점 $$z_\ast$$을 가진다고 가정한다. $$h$$가 연속이고 $$z_k \to z_\ast$$, $$h(z_k) = 0$$이므로 $$h(z_\ast) = \lim_k h(z_k) = 0$$이다. 또 $$z_k$$들이 서로 다르므로 $$z_\ast$$의 임의의 근방에 $$z_\ast$$ 아닌 영점 $$z_k$$이 무한히 들어 있어, $$z_\ast$$은 $$Z(h)$$의 고립점이 아니다. 명제 2에 의해 그렇다면 $$h$$가 $$z_\ast$$의 어떤 근방에서 항등적으로 $$0$$이어야 한다.

이제 이 국소적 소멸을 $$\Omega$$ 전체로 확장한다.

$$A = \{z \in \Omega : h \text{가 } z \text{의 어떤 근방에서 항등적으로 } 0\}$$

이라 두자. 방금 본 대로 $$z_\ast \in A$$이므로 $$A \neq \varnothing$$이다. 정의상 $$A$$는 열려 있다. $$A$$가 $$\Omega$$에서 닫혀 있음을 보이면, $$\Omega$$가 연결이고 $$A$$가 공집합 아닌 열린·닫힌 부분집합이므로 $$A = \Omega$$이 된다.

$$A$$가 닫혀 있음을 보이기 위해 $$\Omega$$ 안의 점 $$w$$가 $$A$$의 폐포에 속한다고, 곧 $$A$$의 점들의 수열 $$w_j \to w$$이 있다고 하자. 각 $$w_j$$의 근방에서 $$h \equiv 0$$이므로 특히 $$h(w_j) = 0$$이고, $$h$$의 연속성에서 $$h(w) = 0$$이다. 더구나 $$w_j \to w$$이고 $$w_j$$들은 ($$j$$가 클 때) $$w$$ 아닌 $$h$$의 영점이므로 $$w$$ 역시 $$Z(h)$$의 고립점이 아니다. 다시 명제 2에 의해 $$h$$가 $$w$$의 어떤 근방에서 항등적으로 $$0$$이고, 따라서 $$w \in A$$이다. 이로써 $$A$$가 $$\Omega$$에서 닫혀 있다.

연결성에 의해 $$A = \Omega$$이므로 $$h$$가 $$\Omega$$ 전체에서 항등적으로 $$0$$이고, 곧 $$\Omega$$에서 $$f = g$$이다.

</details>

일치정리는 정칙함수가 그래프의 한 조각으로 전체가 정해지는 대상임을 말한다. 연결 영역 위의 정칙함수는 집적점을 갖는 임의의 집합, 가령 한 점에 모여드는 수열이나 아무리 짧은 곡선 조각 위에서의 값만으로 영역 전체에서 유일하게 결정된다. 실변수의 매끄러운 함수와의 차이는 여기서 극명하다. 실축의 한 구간에서 $$0$$이면서 다른 구간에서는 $$0$$이 아닌 매끄러운 함수는 얼마든지 있지만, 그러한 함수는 결코 정칙일 수 없다.

집적점이 $$\Omega$$ *안*에 있어야 한다는 조건은 본질적이다. 가령 $$\sin(\pi/z)$$는 $$\Omega = \mathbb{C} \setminus \{0\}$$에서 정칙이고 그 영점 $$1/k$$ ($$k \in \mathbb{Z} \setminus \{0\}$$) 이 $$0$$으로 집적하지만, 집적점 $$0$$은 $$\Omega$$에 속하지 않으므로 함수가 항등적으로 $$0$$일 필요가 없다. 일치정리의 가장 흔한 쓰임 가운데 하나는 실축에서 알려진 항등식을 복소영역으로 끌어올리는 것이다. 두 정칙함수가 실축의 한 구간에서 일치하면, 그 구간이 집적점을 가지므로 두 함수가 공통 정칙영역 전체에서 일치한다. 실변수의 항등식 $$\sin^2 x + \cos^2 x = 1$$이나 $$e^{x+y} = e^x e^y$$이 곧장 복소변수로 넘어가는 것이 이 원리의 사례이다.

<div class="example" markdown="1">

<ins id="ex4">**예시 4 (항등식의 해석적 접속)**</ins> 함수방정식 $$e^{z+w} = e^z e^w$$을 모든 $$z, w \in \mathbb{C}$$에 대해 일치정리로 확립한다. $$w$$를 임의의 고정된 복소수로 두고 두 함수

$$F(z) = e^{z+w}, \qquad G(z) = e^z e^w$$

을 생각하면 둘 다 $$z$$에 대해 전해석함수이다. 한편 실변수 $$z = x \in \mathbb{R}$$이고 $$w$$ 또한 실수일 때는 실지수함수의 덧셈공식에서 $$F(x) = G(x)$$이다. 그러나 우선 $$w$$를 실수로 고정하면 $$F$$와 $$G$$가 실축 전체에서 일치하고, 실축은 $$\mathbb{C}$$ 안에 집적점을 가지므로 정리 3에 의해 모든 $$z \in \mathbb{C}$$에서 $$F(z) = G(z)$$이다. 다음으로 $$z$$를 임의의 복소수로 고정하고 이번에는 $$w$$를 변수로 보면, 두 전해석함수 $$w \mapsto e^{z+w}$$과 $$w \mapsto e^z e^w$$이 실축 $$w \in \mathbb{R}$$에서 (방금 보인 등식에서) 일치하므로, 같은 논법으로 모든 $$w \in \mathbb{C}$$에서 일치한다. 따라서 등식이 모든 복소수쌍에서 성립한다. 실축에서의 한 항등식이 두 번의 해석적 접속을 거쳐 복소평면 전체로 번진 것이다.

</div>

## 최대절댓값 원리

정칙함수의 강직성은 그 절댓값의 거동에도 나타난다. 비상수 정칙함수의 절댓값은 영역 내부의 어느 점에서도 국소적 최댓값에 이를 수 없으며, 따라서 유계영역에서 절댓값의 최댓값은 항상 경계에서 달성된다. 이 최대절댓값 원리는 평균값 성질에서 곧장 따라 나온다. 정칙함수의 한 점에서의 값은 그 점을 중심으로 하는 임의의 원 위에서의 평균이므로 ([§Cauchy 적분공식, ⁋따름정리 7](/ko/math/complex_analysis/cauchy_integral_formula#cor7)), 중심에서의 절댓값이 원 위 모든 값보다 작지 않다면 원 위에서 절댓값이 줄곧 같은 값을 유지할 수밖에 없기 때문이다.

<div class="proposition" markdown="1">

<ins id="thm5">**정리 5 (최대절댓값 원리)**</ins> $$\Omega \subseteq \mathbb{C}$$가 연결 열린집합이고 $$f$$가 $$\Omega$$에서 정칙이라 하자. 만일 $$\lvert f\rvert$$가 $$\Omega$$의 어떤 점 $$z_0$$에서 국소적 최댓값에 이르면, 곧 $$z_0$$의 어떤 근방 안의 모든 $$z$$에서 $$\lvert f(z)\rvert \leq \lvert f(z_0)\rvert$$이면, $$f$$는 $$\Omega$$에서 상수이다.

</div>

<details class="proof" markdown="1">
<summary>증명</summary>

$$z_0$$의 근방 $$D(z_0, \delta) \subseteq \Omega$$에서 $$\lvert f(z)\rvert \leq \lvert f(z_0)\rvert$$이 성립한다고 하자. $$0 < r < \delta$$인 각 $$r$$에 대해 평균값 성질 ([§Cauchy 적분공식, ⁋따름정리 7](/ko/math/complex_analysis/cauchy_integral_formula#cor7)) 에서

$$f(z_0) = \frac{1}{2\pi}\int_0^{2\pi} f(z_0 + re^{i\theta})\,d\theta$$

이므로 양변의 절댓값을 취하고 삼각부등식을 쓰면

$$\lvert f(z_0)\rvert \leq \frac{1}{2\pi}\int_0^{2\pi} \lvert f(z_0 + re^{i\theta})\rvert\,d\theta \leq \frac{1}{2\pi}\int_0^{2\pi} \lvert f(z_0)\rvert\,d\theta = \lvert f(z_0)\rvert$$

이다. 마지막 부등식은 $$\lvert f(z_0 + re^{i\theta})\rvert \leq \lvert f(z_0)\rvert$$ 때문이다. 양 끝이 같으므로 두 부등식이 모두 등호이고, 특히

$$\frac{1}{2\pi}\int_0^{2\pi}\bigl(\lvert f(z_0)\rvert - \lvert f(z_0 + re^{i\theta})\rvert\bigr)\,d\theta = 0$$

이다. 피적분함수는 연속이고 음이 아니므로, 그 적분이 $$0$$이려면 항등적으로 $$0$$이어야 한다. 곧 모든 $$\theta$$에서 $$\lvert f(z_0 + re^{i\theta})\rvert = \lvert f(z_0)\rvert$$이다. $$r \in (0, \delta)$$이 임의였으므로 $$\lvert f\rvert$$는 $$D(z_0, \delta)$$ 전체에서 상수 $$\lvert f(z_0)\rvert$$이다.

이제 정칙함수의 절댓값이 한 열린집합에서 상수이면 그 함수 자체가 상수임을 본다. $$c = \lvert f(z_0)\rvert$$이라 하자. $$c = 0$$이면 $$D(z_0, \delta)$$에서 $$f \equiv 0$$이다. $$c > 0$$이면 $$D(z_0, \delta)$$에서 $$\lvert f\rvert^2 = f\bar f = c^2$$이 상수이다. $$f = u + iv$$로 적으면 $$u^2 + v^2 = c^2$$을 $$x, y$$로 편미분하여 $$u u_x + v v_x = 0$$, $$u u_y + v v_y = 0$$을 얻고, Cauchy–Riemann 방정식 ([§정칙함수, ⁋정리 5](/ko/math/complex_analysis/holomorphic_functions#thm5)) $$u_x = v_y$$, $$u_y = -v_x$$을 대입하면 이 둘은

$$u\,u_x - v\,u_y = 0, \qquad u\,u_y + v\,u_x = 0$$

이 된다. 이를 $$(u_x, u_y)$$에 대한 선형방정식으로 보면 계수행렬식이 $$u^2 + v^2 = c^2 > 0$$이므로 유일해는 $$u_x = u_y = 0$$이고, 다시 Cauchy–Riemann에서 $$v_x = v_y = 0$$이다. 따라서 $$f' = u_x + i v_x = 0$$이 $$D(z_0, \delta)$$에서 성립하여 $$f$$가 그 원판에서 상수이다.

어느 경우든 $$f$$는 $$z_0$$의 한 근방에서 상수이다. 그렇다면 $$f$$와 상수함수 $$f(z_0)$$이 집적점을 갖는 집합(그 근방 전체)에서 일치하므로, 연결 영역 $$\Omega$$에서 일치정리 ([정리 3](#thm3)) 에 의해 $$f$$는 $$\Omega$$ 전체에서 상수 $$f(z_0)$$이다.

</details>

최대절댓값 원리는 정칙함수의 절댓값이 평탄한 봉우리를 가질 수 없음을 말한다. 절댓값이 내부의 한 점에서 주변보다 크거나 같아지는 순간 함수는 상수로 무너지므로, 비상수 정칙함수의 절댓값에는 내부의 국소적 최댓값이 아예 존재하지 않는다. 이 원리를 유계영역에 적용하면 최댓값의 위치가 경계로 밀려난다는 다음 형태가 나온다.

<div class="proposition" markdown="1">

<ins id="cor6">**따름정리 6 (경계에서의 최댓값)**</ins> $$\Omega \subseteq \mathbb{C}$$가 유계 연결 열린집합이고 $$f$$가 $$\Omega$$에서 정칙이며 폐포 $$\overline{\Omega}$$에서 연속이라 하자. 그러면 $$\lvert f\rvert$$는 경계 $$\partial\Omega$$ 위에서 최댓값에 이른다. 곧

$$\max_{z \in \overline{\Omega}}\lvert f(z)\rvert = \max_{z \in \partial\Omega}\lvert f(z)\rvert$$

이다.

</div>

<details class="proof" markdown="1">
<summary>증명</summary>

$$\overline{\Omega}$$이 유계이고 닫혀 있으므로 콤팩트이고, $$\lvert f\rvert$$가 그 위에서 연속이므로 어떤 점 $$z_\ast \in \overline{\Omega}$$에서 최댓값 $$M = \lvert f(z_\ast)\rvert$$에 이른다. 만일 $$z_\ast \in \partial\Omega$$이면 최댓값이 경계에서 달성되어 증명이 끝난다.

그렇지 않고 $$z_\ast \in \Omega$$이라 하자. 그러면 $$\lvert f\rvert$$가 $$\overline{\Omega}$$ 전체의 최댓값을 내부점 $$z_\ast$$에서 가지므로 특히 $$z_\ast$$에서 국소적 최댓값에 이르고, 최대절댓값 원리 ([정리 5](#thm5)) 에 의해 $$f$$는 연결집합 $$\Omega$$에서 상수이다. $$f$$가 $$\overline{\Omega}$$에서 연속이므로 $$\overline{\Omega}$$ 전체에서도 같은 상수이고, 따라서 $$\lvert f\rvert$$가 $$\partial\Omega$$ 위에서도 같은 값 $$M$$을 가진다 (유계영역의 경계는 공집합이 아니다). 어느 경우든 최댓값은 경계에서 달성된다.

</details>

따름정리 6은 정칙함수의 절댓값을 추정하는 데 자주 쓰인다. 영역 안에서 $$\lvert f\rvert$$의 크기를 가늠하려면 경계에서의 크기만 통제하면 충분하다. 가령 한 영역에서 정칙이고 경계에서 절댓값이 $$1$$을 넘지 않는 함수는 영역 내부에서도 절댓값이 $$1$$을 넘지 않는다. 이 관찰이 다음 절의 Schwarz 보조정리에서 결정적으로 쓰인다.

## Schwarz 보조정리

최대절댓값 원리의 가장 깔끔한 응용 가운데 하나가 Schwarz 보조정리이다. 단위원판을 자기 자신으로 보내며 원점을 고정하는 정칙함수는 원점 근처에서 그리 빠르게 자라지 못하도록 강하게 제약된다. 이 제약은 $$f(z)/z$$에 최대절댓값 원리를 적용하여 얻으며, 등호가 성립하는 극단의 경우가 회전뿐임까지 정확히 가려낸다. 단위원판을 $$\mathbb{D} = \{z \in \mathbb{C} : \lvert z\rvert < 1\}$$로 적는다.

<div class="proposition" markdown="1">

<ins id="thm7">**정리 7 (Schwarz 보조정리)**</ins> $$f : \mathbb{D} \to \mathbb{D}$$가 정칙이고 $$f(0) = 0$$이라 하자. 그러면 다음이 성립한다.

1. 모든 $$z \in \mathbb{D}$$에 대해 $$\lvert f(z)\rvert \leq \lvert z\rvert$$이고, $$\lvert f'(0)\rvert \leq 1$$이다.
2. 만일 어떤 $$z_0 \neq 0$$에서 $$\lvert f(z_0)\rvert = \lvert z_0\rvert$$이거나 $$\lvert f'(0)\rvert = 1$$이면, 어떤 상수 $$\lambda$$ ($$\lvert\lambda\rvert = 1$$) 가 있어 모든 $$z \in \mathbb{D}$$에서 $$f(z) = \lambda z$$이다. 곧 $$f$$는 회전이다.

</div>

<details class="proof" markdown="1">
<summary>증명</summary>

$$f(0) = 0$$이므로 $$f$$는 원점에서 위수 $$\geq 1$$인 영점을 가지고, 인수분해 ([§멱급수와 해석성, ⁋명제 6](/ko/math/complex_analysis/power_series_and_analyticity#prop6)) 에 의해 $$\mathbb{D}$$에서 정칙인 $$g$$가 있어 $$f(z) = z\,g(z)$$이다. 구체적으로 $$f(z) = \sum_{n=1}^{\infty} a_n z^n$$이면 $$g(z) = \sum_{n=1}^{\infty} a_n z^{n-1} = \sum_{k=0}^{\infty} a_{k+1} z^k$$이고, 특히 $$g(0) = a_1 = f'(0)$$이다.

이제 $$0 < r < 1$$을 고정하고 닫힌 원판 $$\overline{D(0, r)}$$에 따름정리 6을 적용한다. 경계원 $$\lvert z\rvert = r$$ 위에서는 $$\lvert f(z)\rvert < 1$$이므로 (치역이 $$\mathbb{D}$$에 들어 있다)

$$\lvert g(z)\rvert = \frac{\lvert f(z)\rvert}{\lvert z\rvert} < \frac{1}{r}$$

이고, $$g$$가 $$\overline{D(0,r)}$$에서 정칙이므로 최댓값이 경계에서 달성되어 ([따름정리 6](#cor6)) $$\overline{D(0, r)}$$ 안의 모든 $$z$$에서 $$\lvert g(z)\rvert \leq 1/r$$이다. 여기서 $$r \to 1^-$$로 보내면, $$\mathbb{D}$$의 각 고정된 $$z$$에 대해 $$\lvert g(z)\rvert \leq 1/r$$이 $$r < 1$$이 $$\lvert z\rvert$$보다 큰 한 성립하므로

$$\lvert g(z)\rvert \leq 1, \qquad z \in \mathbb{D}$$

이다. 곧 모든 $$z \in \mathbb{D}$$에서 $$\lvert f(z)\rvert = \lvert z\rvert\,\lvert g(z)\rvert \leq \lvert z\rvert$$이고, $$z = 0$$에서 $$\lvert f'(0)\rvert = \lvert g(0)\rvert \leq 1$$이다. 이로써 (1)이 증명된다.

(2)를 위해 등호의 경우를 본다. 어떤 $$z_0 \neq 0$$에서 $$\lvert f(z_0)\rvert = \lvert z_0\rvert$$이면 $$\lvert g(z_0)\rvert = 1$$이고, $$\lvert f'(0)\rvert = 1$$이면 $$\lvert g(0)\rvert = 1$$이다. 어느 경우든 $$\mathbb{D}$$ 안의 한 점에서 $$\lvert g\rvert$$가 그 상한 $$1$$에 이르므로, $$\lvert g\rvert$$가 내부점에서 최댓값 $$1$$을 가진다. 최대절댓값 원리 ([정리 5](#thm5)) 에 의해 $$g$$는 연결영역 $$\mathbb{D}$$에서 상수이고, 그 절댓값이 $$1$$이므로 $$g(z) \equiv \lambda$$ ($$\lvert\lambda\rvert = 1$$) 이다. 따라서 $$f(z) = \lambda z$$이다.

</details>

Schwarz 보조정리는 원점을 고정하는 단위원판의 자기사상이 원점 근방에서 항등사상보다 더 빠르게 자랄 수 없음을 말한다. $$\lvert f(z)\rvert \leq \lvert z\rvert$$은 각 점에서 함수값이 원점에 더 가까워짐을, $$\lvert f'(0)\rvert \leq 1$$은 원점에서의 확대율이 $$1$$을 넘지 못함을 뜻한다. 등호의 경우가 회전 $$f(z) = \lambda z$$뿐이라는 두 번째 진술은 이 부등식이 비상수 자기사상에 대해서는 결코 포화되지 않는 엄격한 부등식임을 말해 준다. 이 보조정리는 단위원판의 정칙 자기동형사상을 분류하는 출발점이 되며, 그로부터 단위원판 위의 자연스러운 거리인 쌍곡거리가 정칙사상에 의해 늘어나지 않는다는 사실로 이어진다.

<div class="example" markdown="1">

<ins id="ex8">**예시 8 (원점을 고정하는 자기동형사상)**</ins> $$f : \mathbb{D} \to \mathbb{D}$$가 정칙인 전단사이고 그 역함수도 정칙이며 $$f(0) = 0$$이라 하자. 곧 $$f$$는 원점을 고정하는 단위원판의 정칙 자기동형사상이다. 이러한 $$f$$가 회전뿐임을 Schwarz 보조정리로 보인다. $$f$$와 그 역함수 $$f^{-1}$$ 모두 $$\mathbb{D}$$를 $$\mathbb{D}$$로 보내고 원점을 고정하므로, 정리 7의 (1)을 양쪽에 적용하면

$$\lvert f'(0)\rvert \leq 1, \qquad \lvert (f^{-1})'(0)\rvert \leq 1$$

이다. 한편 $$f^{-1}(f(z)) = z$$을 미분하고 $$z = 0$$을 대입하면 연쇄법칙에서 $$(f^{-1})'(0)\,f'(0) = 1$$이므로 $$\lvert f'(0)\rvert\,\lvert (f^{-1})'(0)\rvert = 1$$이다. 두 절댓값이 모두 $$1$$ 이하인데 그 곱이 $$1$$이려면 각각 정확히 $$1$$이어야 한다. 따라서 $$\lvert f'(0)\rvert = 1$$이고, 정리 7의 (2)에 의해 어떤 $$\lambda$$ ($$\lvert\lambda\rvert = 1$$) 가 있어 $$f(z) = \lambda z$$이다. 곧 원점을 고정하는 단위원판의 자기동형사상은 정확히 회전들이다.

</div>

---

**참고문헌**

**[Ahl]** L.V. Ahlfors, *Complex analysis*, 3rd ed., McGraw–Hill, 1979.

**[Con]** J.B. Conway, *Functions of one complex variable I*, 2nd ed., Graduate Texts in Mathematics 11, Springer, 1978.

**[SS]** E.M. Stein, R. Shakarchi, *Complex analysis*, Princeton Lectures in Analysis II, Princeton University Press, 2003.
