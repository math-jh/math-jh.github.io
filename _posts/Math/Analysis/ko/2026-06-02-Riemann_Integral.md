---
title: "Riemann 적분"
description: "다르부의 상합과 하합으로 Riemann 적분을 엄밀하게 정의하고, 적분가능성의 판정 기준을 제시한다. 컴팩트구간 위의 연속함수가 균등연속성을 통해 적분가능함을 증명한다."
excerpt: "다르부 상합·하합, 적분가능성 판정, 연속함수의 적분가능성"

categories: [Math / Analysis]
permalink: /ko/math/analysis/riemann_integral
sidebar: 
    nav: "analysis-ko"

date: 2026-06-02
weight: 14

published: false
---

[\[미적분학\] §정적분](/ko/math/calculus/definite_integral)에서 정적분을 리만 합의 극한으로 도입하면서, 연속함수의 적분가능성은 증명 없이 받아들였다. 이제 [§컴팩트성](/ko/math/analysis/compactness)과 균등연속성을 갖추었으므로, 적분을 엄밀하게 정초하고 그 사실을 증명한다.

## 다르부 상합과 하합

극한을 직접 다루는 대신, 위와 아래에서 죄어 오는 두 합을 쓴다.

<div class="definition" markdown="1">

<ins id="def1">**정의 1**</ins> 유계함수 $$f : [a,b] \to \mathbb{R}$$와 분할 $$P : a = x_0 < \cdots < x_n = b$$에 대하여, 각 부분구간에서 $$m_i = \inf_{[x_{i-1}, x_i]} f$$, $$M_i = \sup_{[x_{i-1}, x_i]} f$$로 두고

$$L(P, f) = \sum_{i=1}^n m_i\,\Delta x_i, \qquad U(P, f) = \sum_{i=1}^n M_i\,\Delta x_i$$

를 각각 *하합<sub>lower sum</sub>*과 *상합<sub>upper sum</sub>*이라 한다.

</div>

상합과 하합은 곡선 아래 넓이를 위와 아래에서 근사하는 직사각형 띠의 넓이 합으로, 각 부분구간에서 함수의 최솟값을 높이로 삼은 안쪽 띠가 하합, 최댓값을 높이로 삼은 바깥쪽 띠가 상합이다. 분할을 더 잘게 쪼갤수록 안쪽 띠는 점점 커지고 바깥쪽 띠는 점점 작아지므로, 두 합이 가운데에서 만나는 값이 있다면 그것을 넓이라 부를 만하다.

이 단조성을 정확히 적자. 분할 $$P$$의 *세분<sub>refinement</sub>* $$P'$$ (즉 $$P \subseteq P'$$) 에 대하여 언제나

$$L(P, f) \leq L(P', f) \leq U(P', f) \leq U(P, f)$$

가 성립한다. 점 하나를 추가하는 경우만 보이면 귀납으로 충분한데, 부분구간 $$[x_{i-1}, x_i]$$에 점 $$c$$를 넣어 두 조각으로 나누면 좁은 구간의 하한이 넓은 구간의 하한보다 작지 않으므로 $$m' = \inf_{[x_{i-1},c]} f \geq m_i$$, $$m'' = \inf_{[c, x_i]} f \geq m_i$$이고

$$\begin{aligned}
m'\,(c - x_{i-1}) + m''\,(x_i - c) &\geq m_i\,(c - x_{i-1}) + m_i\,(x_i - c) \\
&= m_i\,(x_i - x_{i-1}) = m_i\,\Delta x_i
\end{aligned}$$

이어서 $$L(P', f) \geq L(P, f)$$, 대칭적으로 $$U(P', f) \leq U(P, f)$$이다. 따라서 임의의 두 분할 $$P, Q$$에 대해 공통세분 $$P \cup Q$$를 잡으면

$$L(P, f) \leq L(P \cup Q, f) \leq U(P \cup Q, f) \leq U(Q, f)$$

이므로, 모든 하합이 모든 상합의 하계가 된다. 그러므로 *하적분* $$\underline{\int} f = \sup_P L(P, f)$$과 *상적분* $$\overline{\int} f = \inf_P U(P, f)$$이 존재하고 $$\underline{\int} f \leq \overline{\int} f$$이다.

<div class="definition" markdown="1">

<ins id="def2">**정의 2**</ins> $$\underline{\int} f = \overline{\int} f$$일 때 $$f$$가 $$[a,b]$$에서 *Riemann 적분가능*하다고 하고, 그 공통값을 $$\int_a^b f$$로 적는다.

</div>

## 적분가능성 판정

상합과 하합의 차를 임의로 작게 만들 수 있는지가 적분가능성을 결정한다.

<div class="proposition" markdown="1">

<ins id="thm3">**정리 3 (Riemann 판정법)**</ins> 유계함수 $$f$$가 적분가능한 것은, 임의의 $$\varepsilon > 0$$에 대하여 $$U(P, f) - L(P, f) < \varepsilon$$인 분할 $$P$$가 존재하는 것과 동치이다.

</div>

<details class="proof" markdown="1">
<summary>증명</summary>

그런 $$P$$가 있으면 $$0 \leq \overline{\int} f - \underline{\int} f \leq U(P,f) - L(P,f) < \varepsilon$$이 임의의 $$\varepsilon$$에 대해 성립하므로 상적분과 하적분이 같다. 역으로 적분가능하면, 상적분·하적분의 정의에서 $$U(P_1, f) < \overline{\int} f + \varepsilon/2$$, $$L(P_2, f) > \underline{\int} f - \varepsilon/2$$인 분할이 있고, 두 분할의 공통세분 $$P$$를 잡으면 $$U(P,f) - L(P,f) < \varepsilon$$이다.

</details>

## 연속함수의 적분가능성

<div class="proposition" markdown="1">

<ins id="thm4">**정리 4**</ins> $$[a,b]$$에서 연속인 함수는 Riemann 적분가능하다.

</div>

<details class="proof" markdown="1">
<summary>증명</summary>

$$f$$는 컴팩트구간 $$[a,b]$$에서 연속이므로 균등연속이다 ([§연속함수의 성질, ⁋정리 4](/ko/math/analysis/continuous_functions#thm4)). 임의의 $$\varepsilon > 0$$에 대해, 균등연속성으로 $$\lvert x - y\rvert < \delta$$이면 $$\lvert f(x) - f(y)\rvert < \dfrac{\varepsilon}{b - a}$$이게 하는 $$\delta$$가 있다. 너비가 $$\delta$$ 미만인 분할 $$P$$를 잡으면, 각 부분구간에서 $$f$$가 (컴팩트성으로) 최댓값과 최솟값을 가지므로 $$M_i - m_i \leq \dfrac{\varepsilon}{b-a}$$이고

$$U(P, f) - L(P, f) = \sum_i (M_i - m_i)\Delta x_i \leq \frac{\varepsilon}{b-a}\sum_i \Delta x_i = \varepsilon$$

이다. 정리 3에 의해 $$f$$는 적분가능하다.

</details>

정리 4의 증명에서 핵심은 균등연속성이 부분구간 너비 $$\delta$$를 *위치에 무관하게* 한꺼번에 통제한다는 데 있다. 만약 보통의 연속성만 썼다면 $$\delta$$가 점마다 달라져 진동 $$M_i - m_i$$를 일률적으로 작게 만들 수 없었을 것이고, 그렇기에 [§컴팩트성](/ko/math/analysis/compactness)을 통해 얻은 하이네–칸토어 정리가 결정적이었다.

## 예시와 계산

추상적인 정의가 익숙한 적분값을 실제로 내놓는지 확인하기 위해, 가장 단순한 함수들에서 다르부 합을 직접 계산해 보자.

<div class="example" markdown="1">

<ins id="ex5">**예시 5 (일차함수의 적분)**</ins> $$f(x) = x$$를 $$[0, b]$$에서 적분한다. 구간을 $$n$$등분하여 $$x_i = \dfrac{ib}{n}$$, $$\Delta x_i = \dfrac{b}{n}$$로 두면, $$f$$가 증가함수이므로 각 부분구간 $$[x_{i-1}, x_i]$$에서 $$m_i = x_{i-1}$$, $$M_i = x_i$$이다. 따라서

$$\begin{aligned}
U(P_n, f) &= \sum_{i=1}^n \frac{ib}{n}\cdot\frac{b}{n} = \frac{b^2}{n^2}\sum_{i=1}^n i = \frac{b^2}{n^2}\cdot\frac{n(n+1)}{2} = \frac{b^2}{2}\Bigl(1 + \frac1n\Bigr), \\
L(P_n, f) &= \sum_{i=1}^n \frac{(i-1)b}{n}\cdot\frac{b}{n} = \frac{b^2}{n^2}\cdot\frac{(n-1)n}{2} = \frac{b^2}{2}\Bigl(1 - \frac1n\Bigr)
\end{aligned}$$

이다. $$U(P_n, f) - L(P_n, f) = \dfrac{b^2}{n} \to 0$$이므로 정리 3에 의해 $$f$$는 적분가능하고, 두 합이 공통으로 수렴하는 값

$$\int_0^b x\,dx = \frac{b^2}{2}$$

이 적분값이다.

</div>

같은 방식으로 $$f(x) = x^2$$에 대해 거듭제곱 합 공식 $$\sum_{i=1}^n i^2 = \dfrac{n(n+1)(2n+1)}{6}$$을 쓰면 $$\int_0^b x^2\,dx = \dfrac{b^3}{3}$$을 얻으며, 이런 직접 계산은 다음 글의 미적분의 기본정리가 적분을 역도함수로 환원하기 전까지 유일한 계산 수단이었다. 적분가능성이 보장되더라도 정의만으로는 합의 극한을 일일이 따져야 한다는 점에서, 기본정리의 위력이 여기서 미리 드러난다.

다음 예시는 적분 불가능한 함수가 실제로 존재함을 보여, 정의 2의 조건이 공허하지 않음을 확인한다.

<div class="example" markdown="1">

<ins id="ex6">**예시 6 (디리클레 함수)**</ins> $$f : [0,1] \to \mathbb{R}$$를 유리수에서 $$1$$, 무리수에서 $$0$$으로 정의하자. 임의의 분할 $$P$$의 각 부분구간은 양의 길이를 가지므로 그 안에 유리수와 무리수를 모두 포함한다. 따라서 모든 $$i$$에 대해

$$m_i = \inf_{[x_{i-1},x_i]} f = 0, \qquad M_i = \sup_{[x_{i-1},x_i]} f = 1$$

이고, 이로부터

$$L(P, f) = \sum_i 0\cdot\Delta x_i = 0, \qquad U(P, f) = \sum_i 1\cdot\Delta x_i = 1$$

이 모든 분할에서 성립한다. 그러므로 $$\underline{\int} f = 0 \neq 1 = \overline{\int} f$$이고, 디리클레 함수는 Riemann 적분 불가능하다.

</div>

디리클레 함수는 모든 점에서 불연속이라는 점에서 정리 4의 가설과 정반대 극단에 있다. 불연속점이 얼마나 많아야 적분가능성이 깨지는가는 정교한 질문으로, 르베그의 판정 기준에 따르면 Riemann 적분가능성은 불연속점 집합이 (측도 영의 의미에서) 충분히 작은 것과 동치이다. 그 정밀한 형태는 측도론을 필요로 하지만, 연속성을 넘어서는 충분조건 하나는 다르부 틀 안에서 곧바로 증명된다.

## 적분가능성의 충분조건

<div class="proposition" markdown="1">

<ins id="prop7">**명제 7**</ins> $$[a,b]$$에서 단조인 (증가 또는 감소) 유계함수는 Riemann 적분가능하다.

</div>

<details class="proof" markdown="1">
<summary>증명</summary>

$$f$$가 증가한다고 하자 (감소는 대칭이다). 구간을 $$n$$등분하여 $$\Delta x_i = \dfrac{b-a}{n}$$로 두면, 증가성으로 각 부분구간에서 $$m_i = f(x_{i-1})$$, $$M_i = f(x_i)$$이다. 따라서 합이 망원경처럼 소거되어

$$\begin{aligned}
U(P_n, f) - L(P_n, f) &= \sum_{i=1}^n \bigl(f(x_i) - f(x_{i-1})\bigr)\,\frac{b-a}{n} \\
&= \frac{b-a}{n}\sum_{i=1}^n \bigl(f(x_i) - f(x_{i-1})\bigr) \\
&= \frac{b-a}{n}\bigl(f(b) - f(a)\bigr)
\end{aligned}$$

가 된다. 우변은 $$n \to \infty$$일 때 $$0$$으로 가므로, 임의의 $$\varepsilon > 0$$에 대해 $$U(P_n, f) - L(P_n, f) < \varepsilon$$이 되는 $$n$$이 있다. 정리 3에 의해 $$f$$는 적분가능하다.

</details>

단조함수는 점프 불연속을 가질 수 있으며, 그 불연속점은 가산개까지 허용된다. 예컨대 $$[0,1]$$ 위에서 각 $$\dfrac1k$$에서 높이 $$2^{-k}$$만큼 뛰는 계단형 증가함수는 무한히 많은 불연속점을 가지지만 명제 7에 의해 적분가능하다. 이는 연속성이 적분가능성의 *필요* 조건은 아님을 분명히 보여 준다. 다음 예시는 그 경계를 더 좁혀, 불연속점이 단 하나일 때를 직접 다룬다.

<div class="example" markdown="1">

<ins id="ex8">**예시 8 (한 점 불연속)**</ins> $$g : [0,1] \to \mathbb{R}$$를 $$x > 0$$에서 $$g(x) = 0$$, $$g(0) = 1$$로 정의하자. $$g$$는 $$0$$에서만 불연속이다. 작은 $$\varepsilon > 0$$에 대해 분할 $$P : 0 < \varepsilon < 1$$을 잡으면, 첫 부분구간 $$[0, \varepsilon]$$에서 $$M_1 = 1$$, $$m_1 = 0$$이고 둘째 부분구간 $$[\varepsilon, 1]$$에서 $$M_2 = m_2 = 0$$이므로

$$U(P, g) - L(P, g) = (1 - 0)\cdot\varepsilon + 0\cdot(1 - \varepsilon) = \varepsilon$$

이다. $$\varepsilon$$을 임의로 작게 잡을 수 있으므로 정리 3에 의해 $$g$$는 적분가능하고, $$U(P, g) = \varepsilon \to 0$$이므로 $$\int_0^1 g = 0$$이다. 한 점에서의 함숫값 변경은 적분값에 영향을 주지 않는다.

</div>

예시 8의 논법은 유한개의 불연속점에 그대로 확장된다. 각 불연속점을 폭 $$\varepsilon$$의 작은 구간으로 에워싸 그곳의 진동을 가두고, 나머지 컴팩트한 부분에서는 정리 4의 균등연속 논법을 적용하면 상합과 하합의 차를 임의로 작게 만들 수 있다. 따라서 *유한개의 점을 제외하고 연속인 유계함수는 적분가능하다*. 이렇게 다르부 틀은 연속함수를 넘어선 넓은 부류의 적분가능성을 통일적으로 다룬다.

## 적분의 기본 성질

마지막으로, 적분이 기댓대로 행동함을 보이는 구조적 성질들을 다르부 합에서 직접 끌어낸다.

<div class="proposition" markdown="1">

<ins id="prop9">**명제 9 (선형성과 단조성)**</ins> $$f, g$$가 $$[a,b]$$에서 적분가능하면 $$f + g$$와 $$cf$$ ($$c \in \mathbb{R}$$) 도 적분가능하고

$$\int_a^b (f + g) = \int_a^b f + \int_a^b g, \qquad \int_a^b cf = c\int_a^b f$$

이다. 또한 $$[a,b]$$에서 $$f \leq g$$이면 $$\displaystyle\int_a^b f \leq \int_a^b g$$이다.

</div>

<details class="proof" markdown="1">
<summary>증명</summary>

합에 대해, 임의의 부분구간에서 하한·상한이 $$\inf(f+g) \geq \inf f + \inf g$$, $$\sup(f+g) \leq \sup f + \sup g$$를 만족하므로

$$L(P,f) + L(P,g) \leq L(P, f+g) \leq U(P, f+g) \leq U(P,f) + U(P,g)$$

이다. 적분가능성으로 양 끝의 차를 $$\varepsilon$$ 미만으로 만드는 공통세분을 잡으면 가운데도 그러하여 $$f+g$$가 적분가능하고, 같은 부등식에서 세 적분이 모두 같은 값으로 죄어들어 $$\int(f+g) = \int f + \int g$$가 된다. 상수배는 $$c \geq 0$$이면 하한·상한이 $$c$$배로 곱해지고 $$c < 0$$이면 하한과 상한의 역할이 바뀔 뿐이므로 곧바로 따른다. 단조성은 $$f \leq g$$일 때 모든 분할에서 $$L(P, f) \leq L(P, g)$$이고 상한을 취하면 $$\int f = \underline{\int} f \leq \underline{\int} g = \int g$$임에서 나온다.

</details>

단조성에서 $$g = \lvert f\rvert$$, $$-\lvert f\rvert \leq f \leq \lvert f\rvert$$를 쓰면 적분의 삼각부등식 $$\bigl\lvert \int_a^b f\bigr\rvert \leq \int_a^b \lvert f\rvert$$도 따라 나온다. 마지막으로 적분 영역을 쪼개고 이어 붙이는 성질을 본다.

<div class="proposition" markdown="1">

<ins id="prop10">**명제 10 (구간가법성)**</ins> $$a < c < b$$일 때, $$f$$가 $$[a,b]$$에서 적분가능한 것은 $$[a,c]$$와 $$[c,b]$$에서 각각 적분가능한 것과 동치이며, 이때

$$\int_a^b f = \int_a^c f + \int_c^b f$$

이다.

</div>

<details class="proof" markdown="1">
<summary>증명</summary>

분할에 점 $$c$$를 추가해도 세분이 다르부 합을 나쁘게 만들지 않으므로, 적분가능성을 따질 때 $$c$$를 분점으로 포함하는 분할만 고려해도 된다. 그런 분할 $$P$$는 $$[a,c]$$의 분할 $$P_1$$과 $$[c,b]$$의 분할 $$P_2$$로 갈라지고

$$U(P, f) - L(P, f) = \bigl(U(P_1, f) - L(P_1, f)\bigr) + \bigl(U(P_2, f) - L(P_2, f)\bigr)$$

이 성립한다. 좌변을 $$\varepsilon$$ 미만으로 만들 수 있음과 두 괄호를 각각 작게 만들 수 있음은 (둘 다 음이 아니므로) 동치이고, 이로써 적분가능성의 동치가 따른다. 더불어 $$L(P_1, f) + L(P_2, f) = L(P, f)$$의 상한을 취하면 적분값의 가법성 $$\int_a^b f = \int_a^c f + \int_c^b f$$를 얻는다.

</details>

이로써 [\[미적분학\] §정적분, ⁋정리 3](/ko/math/calculus/definite_integral#thm3)에서 받아들였던 연속함수의 적분가능성이 완비성에 기초하여 증명되었고, 같은 다르부 틀에서 선형성·구간가법성·단조성도 모두 따라 나왔다. 미분과 적분을 잇는 다리는 다음 글 [§미적분의 기본정리](/ko/math/analysis/fundamental_theorem_of_calculus)에서 엄밀하게 세운다.
