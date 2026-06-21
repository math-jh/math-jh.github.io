---
title: "고립특이점과 Laurent 급수"
description: "구멍 뚫린 원판에서 정칙인 함수가 음의 멱까지 허용하는 Laurent 급수로 전개됨을 Cauchy 적분공식으로 보이고, 그 주부의 항 수에 따라 고립특이점을 removable, pole, essential의 셋으로 분류한다. Riemann 가제거 정리, 극에서 함수가 무한대로 발산함, Casorati–Weierstrass 정리, 그리고 무한대에서의 거동까지 다룬다."
excerpt: "Laurent 급수, 고립특이점 분류, removable singularity, pole과 위수, essential singularity, Riemann 가제거 정리, Casorati–Weierstrass, 무한대에서의 거동"

categories: [Math / Complex Analysis]
permalink: /ko/math/complex_analysis/isolated_singularities
sidebar: 
    nav: "complex_analysis-ko"

date: 2026-06-21
weight: 8

published: false
---

정칙함수는 정칙 영역 안의 각 점 근방에서 자신의 Taylor 급수로 전개되어 ([§멱급수와 해석성, ⁋정리 1](/ko/math/complex_analysis/power_series_and_analyticity#thm1)) 그곳에서의 거동이 완전히 통제되었다. 그러나 분석에서 정작 흥미로운 점은 함수가 정칙성을 잃는 자리, 곧 특이점이다. $$1/z$$의 원점이나 $$e^{1/z}$$의 원점처럼, 함수가 한 점만 빼고 그 주위에서 정칙인 상황을 *고립특이점<sub>isolated singularity</sub>*이라 부른다. 이런 점 근방에서는 Taylor 급수만으로 전개가 불가능한데, 함수가 그 점에서 정의되지도 정칙이지도 않기 때문이다. 그 대신 음의 멱 $$(z - z_0)^{-1}, (z - z_0)^{-2}, \dots$$까지 허용하는 더 넓은 급수, 곧 Laurent 급수가 등장한다. Laurent 급수에서 음의 멱이 모인 부분, 곧 주부가 특이점의 본성을 그대로 읽어 준다. 주부가 아예 없으면 특이점은 사실 메울 수 있는 가짜 특이점이고, 음의 멱이 유한 개면 극이며, 무한히 많으면 본질적 특이점이다. 이 글은 Laurent 전개를 확립한 뒤 이 셋의 분류와 각각의 해석적 거동을 다룬다.

## 환형 영역에서의 Laurent 전개

Taylor 전개는 함수가 원판 *전체*에서 정칙임을 요구했다. 고립특이점을 다루려면 중심을 도려낸 영역, 곧 환형 영역에서 정칙인 함수를 전개해야 한다. 핵심 발상은 Taylor 전개에서와 같이 Cauchy 적분공식의 핵을 기하급수로 펼치는 것이되, 이번에는 안쪽 경계원과 바깥쪽 경계원 두 개를 쓴다는 점이 다르다. 바깥 원에서는 $$1/(w - z)$$를 양의 멱으로, 안쪽 원에서는 음의 멱으로 전개하여 두 급수를 합치면, 양·음 양쪽 멱을 모두 가진 Laurent 급수가 나온다.

<div class="definition" markdown="1">

<ins id="def1">**정의 1 (환형 영역과 Laurent 급수)**</ins> $$0 \leq r < R \leq \infty$$과 $$z_0 \in \mathbb{C}$$에 대하여 집합

$$A(z_0; r, R) = \{\,z \in \mathbb{C} : r < \lvert z - z_0\rvert < R\,\}$$

을 중심 $$z_0$$의 *환형 영역<sub>annulus</sub>*이라 한다. 또 양·음의 정수 지수를 모두 허용하는 양방향 급수

$$\sum_{n=-\infty}^{\infty} a_n (z - z_0)^n$$

을 $$z_0$$을 중심으로 하는 *Laurent 급수<sub>Laurent series</sub>*라 하고, 이 급수가 한 점에서 수렴한다는 것은 양의 멱 부분 $$\sum_{n=0}^{\infty} a_n (z - z_0)^n$$과 음의 멱 부분 $$\sum_{n=1}^{\infty} a_{-n}(z - z_0)^{-n}$$이 모두 수렴하는 것을 뜻한다.

</div>

음의 멱 부분 $$\sum_{n=1}^{\infty} a_{-n}(z - z_0)^{-n}$$을 Laurent 급수의 *principal part<sub>주부</sub>*라 부르고, 양의 멱 부분을 *regular part<sub>정칙부</sub>*라 부른다. 변수치환 $$\zeta = (z - z_0)^{-1}$$로 보면 주부는 $$\zeta$$에 대한 보통의 멱급수 $$\sum_{n=1}^{\infty} a_{-n}\zeta^n$$이므로 어떤 $$\lvert\zeta\rvert < 1/r$$, 곧 $$\lvert z - z_0\rvert > r$$에서 수렴하고, 정칙부는 어떤 $$\lvert z - z_0\rvert < R$$에서 수렴한다. 따라서 $$r < R$$인 경우 Laurent 급수는 환형 영역 $$A(z_0; r, R)$$에서 수렴하며, 이 영역이 바로 전개가 사는 자리이다.

<div class="proposition" markdown="1">

<ins id="thm2">**정리 2 (Laurent 전개)**</ins> $$f$$가 환형 영역 $$A = A(z_0; r, R)$$에서 정칙이라 하자. 그러면 $$f$$는 $$A$$에서 Laurent 급수

$$f(z) = \sum_{n=-\infty}^{\infty} a_n (z - z_0)^n$$

으로 표현되며, 그 계수는 $$r < \rho < R$$인 임의의 $$\rho$$에 대해

$$a_n = \frac{1}{2\pi i}\oint_{\lvert w - z_0\rvert = \rho} \frac{f(w)}{(w - z_0)^{n+1}}\,dw \qquad (n \in \mathbb{Z})$$

로 주어진다. 이 전개와 계수는 유일하게 결정되며, 급수는 $$A$$의 임의의 콤팩트 부분집합에서 절대·균등수렴한다.

</div>

<details class="proof" markdown="1">
<summary>증명</summary>

$$z \in A$$을 고정하고 $$r < \rho_1 < \lvert z - z_0\rvert < \rho_2 < R$$이 되도록 두 반지름을 잡는다. $$f$$가 닫힌 환형 영역 $$\{\rho_1 \leq \lvert w - z_0\rvert \leq \rho_2\}$$를 품는 영역에서 정칙이므로, 이 닫힌 환형 영역의 두 경계원에 Cauchy의 homotopy 정리 ([§Cauchy 정리, ⁋정리 6](/ko/math/complex_analysis/cauchy_theorem#thm6))를 적용해 얻는 환형 영역에서의 Cauchy 적분공식에 의해

$$f(z) = \frac{1}{2\pi i}\oint_{\lvert w - z_0\rvert = \rho_2}\frac{f(w)}{w - z}\,dw \;-\; \frac{1}{2\pi i}\oint_{\lvert w - z_0\rvert = \rho_1}\frac{f(w)}{w - z}\,dw$$

이다. 이 환형 영역 형태는 두 경계원을 반대 방향으로 도는 닫힌 경로에 Cauchy 적분공식을 적용한 것으로, 안쪽 원의 부호가 음인 것은 그 방향이 영역의 경계로서 시계방향이기 때문이다.

바깥 원 위에서는 $$\lvert w - z_0\rvert = \rho_2 > \lvert z - z_0\rvert$$이므로 Taylor 전개에서와 똑같이 핵을 양의 멱으로 전개한다. 곧

$$\frac{1}{w - z} = \frac{1}{(w - z_0)\bigl(1 - \frac{z - z_0}{w - z_0}\bigr)} = \sum_{n=0}^{\infty}\frac{(z - z_0)^n}{(w - z_0)^{n+1}}$$

이고 공비의 크기가 $$\lvert z - z_0\rvert/\rho_2 < 1$$로 $$w$$에 무관하게 위로 유계이므로 바깥 원 위에서 균등수렴한다. 따라서 합과 적분을 바꿔

$$\frac{1}{2\pi i}\oint_{\lvert w - z_0\rvert = \rho_2}\frac{f(w)}{w - z}\,dw = \sum_{n=0}^{\infty}\left(\frac{1}{2\pi i}\oint_{\lvert w - z_0\rvert = \rho_2}\frac{f(w)}{(w - z_0)^{n+1}}\,dw\right)(z - z_0)^n$$

을 얻는다.

안쪽 원 위에서는 $$\lvert w - z_0\rvert = \rho_1 < \lvert z - z_0\rvert$$이므로 이번에는 역할을 바꾸어 $$1/(z - z_0)$$을 공비로 하는 기하급수로 전개한다. 곧

$$\frac{1}{w - z} = \frac{-1}{(z - z_0)\bigl(1 - \frac{w - z_0}{z - z_0}\bigr)} = -\sum_{m=0}^{\infty}\frac{(w - z_0)^m}{(z - z_0)^{m+1}}$$

이고 공비의 크기가 $$\rho_1/\lvert z - z_0\rvert < 1$$로 안쪽 원 위에서 균등수렴한다. 앞의 음부호와 함께 합과 적분을 바꾸면

$$-\frac{1}{2\pi i}\oint_{\lvert w - z_0\rvert = \rho_1}\frac{f(w)}{w - z}\,dw = \sum_{m=0}^{\infty}\left(\frac{1}{2\pi i}\oint_{\lvert w - z_0\rvert = \rho_1}f(w)(w - z_0)^m\,dw\right)(z - z_0)^{-(m+1)}$$

이 된다. $$n = -(m+1)$$로 지수를 바꾸면 이 항들은 $$n \leq -1$$인 음의 멱이고, 그 계수는 $$\frac{1}{2\pi i}\oint_{\rho_1} f(w)(w - z_0)^{-n-1}\,dw$$이다.

두 합을 더하면 $$f(z) = \sum_{n=-\infty}^{\infty} a_n (z - z_0)^n$$을 얻는데, 양의 지수 계수는 $$\rho_2$$ 원 위의 적분으로, 음의 지수 계수는 $$\rho_1$$ 원 위의 적분으로 나온다. 그런데 $$f(w)/(w - z_0)^{n+1}$$이 환형 영역에서 정칙이므로, 두 경계원이 환형 영역 안에서 서로 homotopic하므로 적분경로를 변형해도 적분값이 변하지 않는다 (Cauchy의 homotopy 정리 ([§Cauchy 정리, ⁋정리 6](/ko/math/complex_analysis/cauchy_theorem#thm6))). 따라서 $$r < \rho < R$$인 임의의 $$\rho$$에 대해 같은 공식이 성립하여 주장하는 계수식을 얻는다.

유일성을 위해 $$f(z) = \sum_{n} b_n (z - z_0)^n$$이 $$A$$에서 수렴하는 또 다른 Laurent 표현이라 하자. 이 급수는 각 원 $$\lvert z - z_0\rvert = \rho$$ 위에서 균등수렴하므로, 양변에 $$(z - z_0)^{-k-1}$$을 곱하고 그 원 위에서 항별로 적분하면 $$\oint (z - z_0)^{m-k-1}\,dz = 2\pi i\,\delta_{m,k}$$ (정수 멱의 적분) 에 의해 오직 $$m = k$$ 항만 살아남아

$$\frac{1}{2\pi i}\oint_{\lvert z - z_0\rvert = \rho} \frac{f(z)}{(z - z_0)^{k+1}}\,dz = b_k$$

이 된다. 이는 위에서 얻은 $$a_k$$의 공식과 같으므로 $$b_k = a_k$$이고, 전개가 유일하다. 절대·균등수렴은 정칙부와 주부가 각각 자신의 수렴원판·수렴 외부영역의 콤팩트 부분집합에서 멱급수로서 절대·균등수렴하기 때문이다.

</details>

정리 2는 Taylor 전개의 환형 영역 판본으로, 함수가 중심에서 정칙일 필요를 음의 멱을 허용하는 대가로 떼어 낸 것이다. $$f$$가 사실 원판 $$D(z_0, R)$$ 전체에서 정칙이면 $$n < 0$$인 계수의 적분 피적분함수 $$f(w)(w - z_0)^{-n-1}$$이 원판 안에서 정칙이므로 Cauchy 정리에 의해 그 적분이 모두 $$0$$이 되어, Laurent 급수가 Taylor 급수로 되돌아간다. 음의 멱 계수가 살아남느냐 아니냐가 곧 중심에서 함수가 정칙으로 메워지느냐를 가르며, 이것이 다음 절의 분류를 떠받친다. 한 가지 주의할 점은 같은 함수라도 중심이 같은 서로 다른 환형 영역에서는 서로 다른 Laurent 전개를 가질 수 있다는 것이다. 유일성은 어디까지나 하나의 고정된 환형 영역 안에서의 이야기이다.

<div class="example" markdown="1">

<ins id="ex3">**예시 3 (영역에 따라 달라지는 전개)**</ins> 함수 $$f(z) = \dfrac{1}{z(z - 1)} = \dfrac{1}{z - 1} - \dfrac{1}{z}$$은 $$z = 0$$과 $$z = 1$$ 두 곳에서만 특이하므로, 원점을 중심으로 두 개의 환형 영역 $$0 < \lvert z\rvert < 1$$과 $$1 < \lvert z\rvert < \infty$$에서 각각 정칙이다. 안쪽 영역 $$0 < \lvert z\rvert < 1$$에서는 $$\lvert z\rvert < 1$$이므로 $$\dfrac{1}{z - 1} = -\dfrac{1}{1 - z} = -\sum_{n=0}^{\infty} z^n$$으로 전개하여

$$f(z) = -\frac{1}{z} - \sum_{n=0}^{\infty} z^n \qquad (0 < \lvert z\rvert < 1)$$

을 얻고, 주부는 $$-1/z$$ 한 항뿐이다. 바깥 영역 $$1 < \lvert z\rvert < \infty$$에서는 $$\lvert 1/z\rvert < 1$$이므로 $$\dfrac{1}{z - 1} = \dfrac{1}{z}\cdot\dfrac{1}{1 - 1/z} = \sum_{n=1}^{\infty} z^{-n}$$으로 전개하여

$$f(z) = \sum_{n=1}^{\infty} z^{-n} - \frac{1}{z} = \sum_{n=2}^{\infty} z^{-n} \qquad (1 < \lvert z\rvert < \infty)$$

을 얻고, 이번에는 전개가 통째로 음의 멱으로만 이루어진다. 같은 함수, 같은 중심이지만 두 환형 영역에서 Laurent 전개가 전혀 다르다.

</div>

## 고립특이점의 분류

이제 함수가 한 점만 빼고 그 주위에서 정칙인 상황을 정식으로 다룬다. 그러한 점을 도려낸 환형 영역 $$0 < \lvert z - z_0\rvert < R$$에서 정칙함수는 정리 2에 의해 Laurent 급수를 가지며, 그 주부의 항 수가 특이점의 본성을 결정한다.

<div class="definition" markdown="1">

<ins id="def4">**정의 4 (고립특이점과 그 분류)**</ins> $$f$$가 어떤 $$R > 0$$에 대해 구멍 뚫린 원판 $$0 < \lvert z - z_0\rvert < R$$에서 정칙이지만 $$z_0$$ 자체에서는 정칙이 아니라 하자. 이때 $$z_0$$을 $$f$$의 *isolated singularity<sub>고립특이점</sub>*이라 한다. $$z_0$$을 중심으로 하는 이 환형 영역에서의 Laurent 전개 $$f(z) = \sum_{n=-\infty}^{\infty} a_n (z - z_0)^n$$의 주부에 따라 고립특이점을 다음 셋으로 분류한다.

1. 모든 $$n < 0$$에서 $$a_n = 0$$이면, 곧 주부가 없으면 $$z_0$$을 *removable singularity<sub>가제거 특이점</sub>*이라 한다.
2. 음의 지수 계수 가운데 $$0$$이 아닌 것이 유한 개이면, 곧 어떤 $$m \geq 1$$이 있어 $$a_{-m} \neq 0$$이고 모든 $$n < -m$$에서 $$a_n = 0$$이면 $$z_0$$을 위수 $$m$$인 *pole<sub>극</sub>*이라 한다.
3. 음의 지수 계수 가운데 $$0$$이 아닌 것이 무한히 많으면 $$z_0$$을 *essential singularity<sub>본질적 특이점</sub>*이라 한다.

</div>

이 분류는 주부가 가진 항의 개수가 $$0$$이냐, 유한이냐, 무한이냐는 단순한 기준에 따른 것이지만, 곧 보겠듯이 각 경우 함수가 $$z_0$$ 근방에서 보이는 거동이 질적으로 완전히 다르다. 위수 $$1$$인 극을 *simple pole<sub>단순극</sub>*이라 부른다. 예시 3의 $$f(z) = 1/(z(z-1))$$은 영역 $$0 < \lvert z\rvert < 1$$에서의 전개 주부가 $$-1/z$$ 한 항이므로 원점에서 단순극을 가지고, $$e^{1/z} = \sum_{n=0}^{\infty} \frac{1}{n!}z^{-n}$$은 모든 음의 멱이 살아 있으므로 원점에서 본질적 특이점을 가진다. 분류가 영역 선택과 무관함을 짚어 둘 필요가 있다. 고립특이점의 분류는 항상 $$z_0$$에 *가장 가까운* 환형 영역, 곧 $$0 < \lvert z - z_0\rvert < R$$ 형태에서의 전개로 정의하므로 (예시 3의 바깥 영역 같은 다른 환형 영역이 아니라), 분류는 함수와 점 $$z_0$$에 의해 일의적으로 결정된다.

## Removable singularity와 Riemann 가제거 정리

가제거 특이점은 이름 그대로 메울 수 있는 가짜 특이점이다. 주부가 없으면 Laurent 급수가 보통의 멱급수가 되어 $$z_0$$에서 정칙함수로 수렴하므로, $$f(z_0)$$의 값을 그 멱급수의 상수항으로 정의해 주기만 하면 특이점이 사라진다. 놀라운 점은 이 가제거성을 판정하는 데 Laurent 계수를 들여다볼 필요조차 없고, 함수가 특이점 근방에서 유계라는 약한 조건만으로 충분하다는 것이다.

<div class="proposition" markdown="1">

<ins id="thm5">**정리 5 (Riemann 가제거 정리)**</ins> $$f$$가 구멍 뚫린 원판 $$0 < \lvert z - z_0\rvert < R$$에서 정칙이라 하자. 그러면 다음 세 조건은 동치이다.

1. $$z_0$$이 $$f$$의 가제거 특이점이다.
2. $$f$$가 $$z_0$$의 어떤 구멍 뚫린 근방에서 유계이다.
3. $$\lim_{z \to z_0}(z - z_0)f(z) = 0$$이다.

이 경우 $$f$$는 $$z_0$$에서 정칙함수로 유일하게 확장된다.

</div>

<details class="proof" markdown="1">
<summary>증명</summary>

$$(1) \Rightarrow (2)$$. 주부가 없으면 $$f(z) = \sum_{n=0}^{\infty} a_n(z - z_0)^n$$이 $$0 < \lvert z - z_0\rvert < R$$에서 성립하는데, 이 멱급수는 $$z_0$$에서도 수렴하여 정칙함수를 정의한다 ([§정칙함수, ⁋정리 9](/ko/math/complex_analysis/holomorphic_functions#thm9)). 정칙함수는 연속이므로 $$z_0$$의 한 근방에서 유계이다.

$$(2) \Rightarrow (3)$$. $$0 < \lvert z - z_0\rvert < \delta$$에서 $$\lvert f(z)\rvert \leq M$$이라 하면 $$\lvert (z - z_0)f(z)\rvert \leq M\lvert z - z_0\rvert \to 0$$이므로 (3)이 따른다.

$$(3) \Rightarrow (1)$$. 함수 $$h(z) = (z - z_0)^2 f(z)$$를 생각하고 $$h(z_0) = 0$$으로 정의하자. $$z \neq z_0$$에서 $$h$$는 정칙이고, $$z_0$$에서는 차분비

$$\frac{h(z) - h(z_0)}{z - z_0} = \frac{(z - z_0)^2 f(z)}{z - z_0} = (z - z_0)f(z) \xrightarrow[z \to z_0]{} 0$$

이 가정 (3)에 의해 $$0$$으로 수렴하므로 $$h'(z_0) = 0$$이 존재한다. 따라서 $$h$$는 $$z_0$$을 포함한 원판 $$D(z_0, R)$$ 전체에서 정칙이고, $$h(z_0) = 0$$, $$h'(z_0) = 0$$이므로 그 Taylor 전개는 ([§멱급수와 해석성, ⁋정리 1](/ko/math/complex_analysis/power_series_and_analyticity#thm1)) $$n = 2$$부터 시작한다. 곧 $$h(z) = \sum_{n=2}^{\infty} c_n (z - z_0)^n$$이고, $$(z - z_0)^2$$으로 나누면

$$f(z) = \frac{h(z)}{(z - z_0)^2} = \sum_{n=2}^{\infty} c_n (z - z_0)^{n-2} = \sum_{k=0}^{\infty} c_{k+2}(z - z_0)^k$$

이 $$0 < \lvert z - z_0\rvert < R$$에서 성립한다. 이는 주부가 없는 Laurent 전개이므로 $$z_0$$은 가제거 특이점이다.

끝으로 확장의 정칙성과 유일성을 본다. 주부 없는 전개 $$f(z) = \sum_{k=0}^{\infty} c_{k+2}(z - z_0)^k$$의 우변은 $$z_0$$에서도 정칙한 함수를 정의하므로, $$f(z_0) = c_2$$로 두면 $$f$$가 $$D(z_0, R)$$ 전체에서 정칙이 된다. 유일성은 일치정리에서 나온다 ([§영점과 일치정리, ⁋정리 3](/ko/math/complex_analysis/zeros_and_identity_theorem#thm3)). 두 정칙확장은 구멍 뚫린 원판에서 일치하고 그 영역이 집적점을 가지므로 $$z_0$$에서도 같은 값을 가져야 한다.

</details>

정리 5의 가장 강력한 점은 (2)이다. 정칙함수가 한 점 근방에서 유계이기만 하면 그 점의 특이성은 환상에 지나지 않으며, 함수를 정칙하게 메울 수 있다. 실변수에서는 유계인 매끄러운 함수가 한 점에서 진동하며 정칙으로 확장되지 못하는 경우가 흔하지만, 복소변수에서는 유계성 하나가 특이점을 완전히 무력화한다. 전형적인 쓰임은 몫함수의 특이점 해소이다. 가령 $$\dfrac{\sin z}{z}$$은 원점에서 정의되지 않지만, $$\sin z = z - z^3/6 + \cdots$$이므로 원점 근방에서 $$\lvert \sin z/z\rvert$$이 유계이고, 따라서 원점은 가제거 특이점이어서 $$\sin z/z$$에 $$z = 0$$에서 값 $$1$$을 주면 전해석함수가 된다.

## Pole에서의 거동

극은 함수가 무한대로 깔끔하게 발산하는 특이점이다. 주부가 유한 개의 음의 멱으로 이루어지므로, 가장 낮은 음의 멱이 발산의 차수를 정확히 결정한다. 위수 $$m$$인 극은 $$1/(z - z_0)^m$$과 같은 속도로 터지며, 이 발산은 영점의 인수분해를 뒤집은 인수분해로 깔끔하게 기술된다.

<div class="proposition" markdown="1">

<ins id="prop6">**명제 6 (극의 특징과 발산)**</ins> $$f$$가 $$z_0$$에서 고립특이점을 가진다고 하자. 다음 세 조건은 동치이며, 각 경우 $$z_0$$은 위수 $$m$$인 극이다.

1. $$z_0$$이 $$f$$의 위수 $$m$$인 극이다.
2. $$z_0$$의 어떤 구멍 뚫린 근방에서 정칙이고 $$g(z_0) \neq 0$$인 함수 $$g$$가 있어 $$f(z) = (z - z_0)^{-m}g(z)$$이며, $$g$$는 $$z_0$$에서 정칙으로 확장된다.
3. $$1/f$$가 $$z_0$$에서 (가제거 특이점을 메운 뒤) 위수 $$m$$인 영점을 가진다.

특히 $$z_0$$이 $$f$$의 극이면 $$\lim_{z \to z_0}\lvert f(z)\rvert = \infty$$이다.

</div>

<details class="proof" markdown="1">
<summary>증명</summary>

$$(1) \Rightarrow (2)$$. 위수 $$m$$인 극이면 Laurent 전개가 $$f(z) = \sum_{n=-m}^{\infty} a_n (z - z_0)^n$$ ($$a_{-m} \neq 0$$) 이다. $$(z - z_0)^m$$을 묶어내면

$$f(z) = (z - z_0)^{-m}\sum_{n=-m}^{\infty} a_n (z - z_0)^{n+m} = (z - z_0)^{-m}\sum_{k=0}^{\infty} a_{k-m}(z - z_0)^k$$

이고, $$g(z) = \sum_{k=0}^{\infty} a_{k-m}(z - z_0)^k$$로 두면 이 멱급수는 $$z_0$$에서 정칙으로 확장되며 ([§정칙함수, ⁋정리 9](/ko/math/complex_analysis/holomorphic_functions#thm9)) $$g(z_0) = a_{-m} \neq 0$$이다.

$$(2) \Rightarrow (1)$$. $$g$$가 $$z_0$$에서 정칙이고 $$g(z_0) \neq 0$$이면 $$g(z) = \sum_{k=0}^{\infty} b_k (z - z_0)^k$$ ($$b_0 = g(z_0) \neq 0$$) 이고, $$f(z) = (z - z_0)^{-m}g(z) = \sum_{k=0}^{\infty} b_k (z - z_0)^{k-m}$$이다. 이는 가장 낮은 멱이 $$-m$$이고 그 계수 $$b_0 \neq 0$$인 Laurent 전개이므로 $$z_0$$은 위수 $$m$$인 극이다.

$$(2) \Leftrightarrow (3)$$. (2)에서 $$g(z_0) \neq 0$$이고 $$g$$가 정칙이므로 연속성에 의해 $$z_0$$의 어떤 근방에서 $$g$$가 $$0$$이 아니고, 따라서 그 근방에서

$$\frac{1}{f(z)} = (z - z_0)^m \frac{1}{g(z)}$$

이다. $$1/g$$은 $$g(z_0) \neq 0$$이므로 $$z_0$$에서 정칙이고 $$(1/g)(z_0) = 1/g(z_0) \neq 0$$이다. 곧 $$1/f$$는 인수 $$(z - z_0)^m$$에 $$z_0$$에서 사라지지 않는 정칙함수를 곱한 꼴이므로, 영점의 인수분해 ([§멱급수와 해석성, ⁋명제 6](/ko/math/complex_analysis/power_series_and_analyticity#prop6)) 에 의해 $$z_0$$에서 위수 $$m$$인 영점을 가진다. 역으로 $$1/f$$가 $$z_0$$에서 위수 $$m$$인 영점을 가지면 같은 인수분해로 $$1/f(z) = (z - z_0)^m h(z)$$ ($$h(z_0) \neq 0$$) 이고, 역수를 취하면 $$f(z) = (z - z_0)^{-m}(1/h(z))$$이 (2)의 꼴이다.

발산은 (2)에서 곧장 나온다. $$z \to z_0$$일 때 $$\lvert g(z)\rvert \to \lvert g(z_0)\rvert > 0$$이고 $$\lvert z - z_0\rvert^{-m} \to \infty$$이므로 $$\lvert f(z)\rvert = \lvert z - z_0\rvert^{-m}\lvert g(z)\rvert \to \infty$$이다.

</details>

명제 6은 극을 영점의 거울상으로 본다. 위수 $$m$$인 영점이 인수 $$(z - z_0)^m$$을 내놓았듯이 ([§멱급수와 해석성, ⁋명제 6](/ko/math/complex_analysis/power_series_and_analyticity#prop6)), 위수 $$m$$인 극은 인수 $$(z - z_0)^{-m}$$을 내놓고, 두 거동은 역수를 취하는 조작으로 정확히 맞바뀐다. 이 대응 덕분에 극의 위수 계산은 영점의 위수 계산으로 환원된다. 가령 $$f(z) = \dfrac{z + 1}{z^2(z - 1)}$$의 원점에서의 극의 위수는 분모 $$z^2(z-1)$$이 원점에서 가지는 영점의 위수가 $$2$$이고 분자가 원점에서 $$1 \neq 0$$이므로 $$2$$이다. 마지막 발산 진술은 극과 다른 두 종류의 특이점을 가르는 결정적 기준이기도 하다. 가제거 특이점에서는 함수가 유계이고 본질적 특이점에서는 곧 보겠듯이 극한이 아예 존재하지 않으므로, $$z_0$$에서 $$\lvert f\rvert$$이 무한대로 발산하는 것은 정확히 극인 경우뿐이다.

<div class="example" markdown="1">

<ins id="ex7">**예시 7 (극의 위수 판정)**</ins> 함수 $$f(z) = \dfrac{1}{\sin z}$$의 고립특이점과 그 위수를 살핀다. $$\sin z$$의 영점은 $$z = k\pi$$ ($$k \in \mathbb{Z}$$) 이고, 각 영점에서 $$(\sin z)' = \cos(k\pi) = (-1)^k \neq 0$$이므로 모두 단순영점이다 ([§멱급수와 해석성, ⁋정의 5](/ko/math/complex_analysis/power_series_and_analyticity#def5) 뒤의 단순영점 판정). 따라서 명제 6의 조건 (3)에 의해 $$1/\sin z$$는 각 $$z = k\pi$$에서 위수 $$1$$인 극, 곧 단순극을 가진다. 다른 점에서는 $$\sin z \neq 0$$이어서 $$f$$가 정칙이므로, $$f$$의 특이점은 정수 $$k$$에 대한 $$k\pi$$들뿐이고 모두 단순극이다.

</div>

## Essential singularity와 Casorati–Weierstrass 정리

본질적 특이점은 함수가 길들지 않는 가장 거친 특이점이다. 가제거 특이점에서 함수는 한 값으로 수렴하고 극에서는 무한대라는 한 방향으로 발산하지만, 본질적 특이점에서는 함수가 어느 쪽으로도 정착하지 못한다. $$e^{1/z}$$의 원점이 그 표본인데, 실축을 따라 $$0$$으로 다가가면 한쪽에서는 $$\infty$$로 터지고 다른 쪽에서는 $$0$$으로 잦아들며, 허축을 따라 다가가면 절댓값이 $$1$$인 채로 진동한다. Casorati–Weierstrass 정리는 이 무질서를 정밀하게 포착하여, 본질적 특이점 근방에서 함수값이 복소평면 전체에 조밀하게 흩어짐을 말한다.

<div class="proposition" markdown="1">

<ins id="thm8">**정리 8 (Casorati–Weierstrass)**</ins> $$z_0$$이 $$f$$의 본질적 특이점이라 하자. 그러면 $$z_0$$의 임의의 구멍 뚫린 근방 $$U = \{0 < \lvert z - z_0\rvert < \delta\}$$의 상 $$f(U)$$은 $$\mathbb{C}$$에서 조밀하다. 곧 임의의 $$w \in \mathbb{C}$$과 임의의 $$\varepsilon > 0$$에 대하여 $$U$$ 안의 어떤 $$z$$가 있어 $$\lvert f(z) - w\rvert < \varepsilon$$이다.

</div>

<details class="proof" markdown="1">
<summary>증명</summary>

귀류법을 쓴다. 결론이 거짓이라면 어떤 $$w \in \mathbb{C}$$과 $$\varepsilon > 0$$, 그리고 어떤 구멍 뚫린 근방 $$U = \{0 < \lvert z - z_0\rvert < \delta\}$$이 있어, 모든 $$z \in U$$에서 $$\lvert f(z) - w\rvert \geq \varepsilon$$이다. 곧 $$f(U)$$이 $$w$$ 둘레의 반지름 $$\varepsilon$$인 원판을 피한다.

이때 함수

$$g(z) = \frac{1}{f(z) - w}$$

을 $$U$$에서 생각하면, $$\lvert f(z) - w\rvert \geq \varepsilon$$이므로 분모가 $$U$$에서 사라지지 않아 $$g$$가 $$U$$에서 정칙이고, 더구나

$$\lvert g(z)\rvert = \frac{1}{\lvert f(z) - w\rvert} \leq \frac{1}{\varepsilon}$$

으로 $$U$$에서 유계이다. 따라서 Riemann 가제거 정리 ([정리 5](#thm5)) 에 의해 $$z_0$$은 $$g$$의 가제거 특이점이고, $$g$$는 $$z_0$$에서 정칙함수로 확장된다. 확장된 $$g$$의 $$z_0$$에서의 값 $$g(z_0)$$에 따라 두 경우로 나뉜다.

$$g(z_0) \neq 0$$이면 $$f(z) - w = 1/g(z)$$이 $$z_0$$에서 정칙이고 ($$g(z_0) \neq 0$$이므로) 그 값이 $$1/g(z_0)$$으로 유한하다. 그러면 $$f$$ 자신이 $$z_0$$ 근방에서 유계이므로 다시 정리 5에 의해 $$z_0$$이 $$f$$의 가제거 특이점이 되어, $$z_0$$이 본질적 특이점이라는 가정에 어긋난다.

$$g(z_0) = 0$$이면 $$g$$가 $$z_0$$에서 정칙이고 ($$g = 1/(f - w)$$이 $$U$$에서 결코 $$0$$이 될 수 없으므로 $$g$$는 $$U$$에서 항등적으로 $$0$$이 아니다) 어떤 위수 $$m \geq 1$$인 영점을 가진다. 그러면 명제 6의 (3)에 의해 $$f(z) - w = 1/g(z)$$이 $$z_0$$에서 위수 $$m$$인 극을 가지고, 상수 $$w$$를 더해도 극의 본성은 변하지 않으므로 $$f$$ 역시 $$z_0$$에서 위수 $$m$$인 극을 가진다. 이는 다시 $$z_0$$이 본질적 특이점이라는 가정에 어긋난다.

두 경우 모두 모순이므로, $$f(U)$$이 어떤 원판을 피한다는 가정이 틀렸다. 곧 임의의 $$w$$의 임의의 근방이 $$f(U)$$과 만나며, $$f(U)$$이 $$\mathbb{C}$$에서 조밀하다.

</details>

Casorati–Weierstrass 정리는 세 종류의 고립특이점을 함수값의 극한 거동으로 완전히 구별하게 해 준다. 가제거 특이점에서는 $$\lim_{z \to z_0} f(z)$$이 (유한한 값으로) 존재하고, 극에서는 $$\lim_{z \to z_0}\lvert f(z)\rvert = \infty$$로 한 방향으로 확정되며, 본질적 특이점에서는 함수값이 평면 어디에나 임의로 가깝게 다가가므로 어떤 극한도 존재하지 않는다. 이 세 가지가 서로 배타적이고 빠짐없으므로, 극한 거동만 보아도 특이점의 종류를 판정할 수 있다. 정리의 결론은 사실 더 강화될 수 있어서, 본질적 특이점 근방에서 함수값이 단지 조밀하게 흩어지는 데 그치지 않고 많아야 한 점을 제외한 모든 복소수값을 무한히 자주 취한다 (Picard의 큰 정리). $$e^{1/z}$$이 원점 근방에서 $$0$$만 제외하고 모든 복소수값을 취하는 것이 그 예이다.

## 무한대에서의 거동

지금까지는 유한한 점에서의 특이점만 다루었다. 함수의 큰 $$\lvert z\rvert$$에서의 거동도 같은 틀로 분석할 수 있는데, 변수치환 $$z \mapsto 1/z$$로 무한대를 원점으로 끌어오면 된다. 이로써 다항식이 무한대에서 극을, $$e^z$$이 무한대에서 본질적 특이점을 가진다는 직관이 정확한 의미를 얻는다.

<div class="definition" markdown="1">

<ins id="def9">**정의 9 (무한대에서의 특이점)**</ins> $$f$$가 어떤 $$\rho > 0$$에 대해 $$\lvert z\rvert > \rho$$에서 정칙이라 하자. 함수 $$\tilde{f}(\zeta) = f(1/\zeta)$$를 생각하면 $$\tilde{f}$$는 구멍 뚫린 원판 $$0 < \lvert\zeta\rvert < 1/\rho$$에서 정칙이다. $$f$$가 $$\infty$$에서 가지는 특이점의 종류를 $$\tilde{f}$$가 $$\zeta = 0$$에서 가지는 특이점의 종류로 정의한다. 곧 $$\tilde{f}$$가 $$0$$에서 가제거 특이점·위수 $$m$$인 극·본질적 특이점을 가지면, $$f$$가 $$\infty$$에서 각각 가제거 특이점·위수 $$m$$인 극·본질적 특이점을 가진다고 한다.

</div>

치환 $$z = 1/\zeta$$에서 $$\lvert z\rvert > \rho$$가 $$0 < \lvert\zeta\rvert < 1/\rho$$로 옮겨지므로, $$\lvert z\rvert > \rho$$에서의 $$f$$의 Laurent 전개 $$f(z) = \sum_{n} a_n z^n$$은 $$\tilde{f}(\zeta) = \sum_n a_n \zeta^{-n}$$이 되어 두 전개의 지수 부호가 뒤집힌다. 따라서 무한대에서의 분류는 $$f$$의 전개에서 *양의* 멱의 거동으로 읽힌다. $$f$$의 전개에 양의 멱이 없으면 ($$a_n = 0$$ for $$n > 0$$) $$\infty$$이 가제거 특이점이고, 양의 멱이 유한 개로 가장 높은 것이 $$z^m$$이면 ($$a_m \neq 0$$, $$a_n = 0$$ for $$n > m$$) $$\infty$$이 위수 $$m$$인 극이며, 양의 멱이 무한히 많으면 본질적 특이점이다. 차수 $$m$$인 다항식 $$p(z) = a_m z^m + \cdots + a_0$$은 양의 멱이 $$z^m$$까지 정확히 유한 개이므로 $$\infty$$에서 위수 $$m$$인 극을 가지고, $$e^z = \sum_{n \geq 0} z^n/n!$$은 양의 멱이 무한히 많으므로 ([§정칙함수, ⁋정의 10](/ko/math/complex_analysis/holomorphic_functions#def10)) $$\infty$$에서 본질적 특이점을 가진다.

이 관점이 곧장 주는 깔끔한 결과 하나는 전해석함수의 분류이다. 전해석함수가 무한대에서 길들기만 하면 그 모양이 다항식으로 강제된다.

<div class="proposition" markdown="1">

<ins id="prop10">**명제 10 (무한대에서 극을 가지는 전해석함수)**</ins> $$f$$가 entire function이고 $$\infty$$에서 가제거 특이점 또는 극을 가진다고 하자. 그러면 $$f$$는 다항식이다. 특히 $$\infty$$이 가제거 특이점이면 $$f$$는 상수이고, $$\infty$$이 위수 $$m$$인 극이면 $$f$$는 차수 $$m$$인 다항식이다.

</div>

<details class="proof" markdown="1">
<summary>증명</summary>

$$f$$가 entire function이므로 평면 전체에서 Taylor 전개 $$f(z) = \sum_{n=0}^{\infty} a_n z^n$$을 가진다 ([§멱급수와 해석성, ⁋정리 1](/ko/math/complex_analysis/power_series_and_analyticity#thm1)). 이것이 곧 $$\lvert z\rvert > 0$$에서의 Laurent 전개이기도 하므로, 무한대에서의 거동은 위에서 본 대로 양의 멱의 거동으로 읽힌다.

$$\infty$$이 가제거 특이점이면 양의 멱이 모두 사라져 ($$n > 0$$에서 $$a_n = 0$$) $$f(z) = a_0$$이 상수이다. $$\infty$$이 위수 $$m$$인 극이면 가장 높은 양의 멱이 $$z^m$$이고 ($$a_m \neq 0$$, $$n > m$$에서 $$a_n = 0$$) 따라서

$$f(z) = \sum_{n=0}^{m} a_n z^n$$

이 차수 $$m$$인 다항식이다. 두 경우 모두 $$f$$가 다항식이다.

</details>

명제 10은 다항식을 무한대에서의 거동으로 특징짓는다. 전해석함수 가운데 무한대에서 가장 거칠지 않게, 곧 본질적 특이점 없이 행동하는 것은 정확히 다항식뿐이며, 본질적 특이점을 가지는 전해석함수는 $$e^z$$이나 $$\sin z$$처럼 다항식이 아닌 초월적 entire function이다. 가제거 특이점인 경우가 상수라는 결론은 Liouville 정리 ([§Cauchy 적분공식, ⁋따름정리 5](/ko/math/complex_analysis/cauchy_integral_formula#cor5)) 와도 맞물린다. $$\infty$$에서 가제거 특이점을 가지는 전해석함수는 큰 $$\lvert z\rvert$$에서 유계이고 평면의 나머지에서도 연속이므로 평면 전체에서 유계여서, Liouville 정리로 곧장 상수임이 따른다.

---

**참고문헌**

**[Ahl]** L.V. Ahlfors, *Complex analysis*, 3rd ed., McGraw–Hill, 1979.

**[Con]** J.B. Conway, *Functions of one complex variable I*, 2nd ed., Graduate Texts in Mathematics 11, Springer, 1978.

**[SS]** E.M. Stein, R. Shakarchi, *Complex analysis*, Princeton Lectures in Analysis II, Princeton University Press, 2003.
