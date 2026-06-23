---
title: "미분방정식의 존재성과 유일성"
description: "완비 거리공간 위의 축약사상 원리를 증명하고, 미분방정식의 초기값 문제를 적분방정식으로 바꾸어 그 해의 존재와 유일성을 보이는 피카르–린델뢰프 정리를 확립한다."
excerpt: "축약사상 원리, 립시츠 조건, 피카르–린델뢰프 정리"

categories: [Math / Analysis]
permalink: /ko/math/analysis/existence_uniqueness_ode
sidebar: 
    nav: "analysis-ko"

date: 2026-06-02
weight: 21

drift_needed: true

published: false
---

미분방정식은 함수와 그 도함수의 관계로 함수를 규정한다. 가장 기본적인 물음은 주어진 초기 조건 아래 해가 존재하는가, 그리고 유일한가이다. 해가 없으면 모형이 무의미하고 해가 여럿이면 미래가 초기 상태로 결정되지 않으니, 어떤 조건 아래 초기값 문제가 잘 정의되는가를 가려내는 것이 미분방정식 이론의 출발점이 된다. 이 글에서는 해석학의 존재 정리를 떠받치는 축약사상 원리를 증명하고, 이를 미분방정식에 적용한다.

우리가 택하는 전략은 미분방정식을 적분방정식으로 바꾸고, 그 적분방정식의 해를 어떤 사상의 *고정점<sub>fixed point</sub>*으로 보는 것이다. 그러면 문제는 추상적인 거리공간 위에서 사상이 고정점을 가지는가라는 순수 해석학의 문제로 환원되고, 이 환원은 축약사상 원리라는 하나의 정리로 깔끔하게 해결된다. 이러한 발상은 미분방정식뿐 아니라 적분방정식, 함수방정식, 수치해석의 반복법 등 해석학 전반에서 되풀이된다.

## 축약사상 원리

거리공간 위의 사상이 두 점 사이의 거리를 일정 비율 이상으로 줄인다면, 그 사상을 반복 적용할 때 점들이 한곳으로 모일 것이라는 직관은 자연스럽다. 이 직관을 정확히 다듬은 것이 축약사상의 개념이다.

<div class="definition" markdown="1">

<ins id="def1">**정의 1**</ins> 거리공간 $$(X, d)$$의 사상 $$T : X \to X$$가 *축약사상<sub>contraction</sub>*이라는 것은, 어떤 상수 $$0 \leq \lambda < 1$$에 대하여 모든 $$x, y$$에서 $$d(T x, T y) \leq \lambda\, d(x, y)$$인 것이다.

</div>

상수 $$\lambda$$를 *축약상수<sub>contraction constant</sub>*라 부른다. 부등식이 모든 점에서 같은 $$\lambda$$로 성립해야 한다는 점, 그리고 $$\lambda$$가 $$1$$보다 *진성으로* 작아야 한다는 점이 핵심이다. 만약 $$\lambda = 1$$만 보장된다면, 즉 $$d(Tx, Ty) \leq d(x, y)$$인 경우에는 $$T$$를 *비확장사상<sub>nonexpansive map</sub>*이라 부르며, 이때는 고정점이 존재하지 않거나 유일하지 않을 수 있다. 예컨대 실직선 위의 평행이동 $$Tx = x + 1$$은 거리를 정확히 보존하지만 고정점이 없다.

<div class="proposition" markdown="1">

<ins id="thm2">**정리 2 (바나흐 고정점 정리)**</ins> 완비 거리공간 위의 축약사상 $$T$$는 유일한 고정점 $$x^\ast = T x^\ast$$를 가지며, 임의의 출발점 $$x_0$$에서 시작한 반복 $$x_{n+1} = T x_n$$이 그 고정점으로 수렴한다.

</div>

<details class="proof" markdown="1">
<summary>증명</summary>

먼저 연속한 두 항 사이의 거리가 기하급수적으로 줄어듦을 본다. 축약 조건을 반복 적용하면

$$\begin{aligned}
d(x_{n+1}, x_n) &= d(Tx_n, Tx_{n-1}) \leq \lambda\, d(x_n, x_{n-1}) \\
&\leq \lambda^2 d(x_{n-1}, x_{n-2}) \leq \cdots \leq \lambda^n d(x_1, x_0)
\end{aligned}$$

을 얻는다. 이제 $$m > n$$에 대해 삼각부등식을 $$m - n$$번 적용하고 위 평가와 등비급수의 합을 쓰면

$$\begin{aligned}
d(x_m, x_n) &\leq \sum_{k=n}^{m-1} d(x_{k+1}, x_k) \leq \sum_{k=n}^{m-1}\lambda^k d(x_1, x_0) \\
&\leq d(x_1, x_0)\sum_{k=n}^{\infty}\lambda^k = \frac{\lambda^n}{1 - \lambda}\,d(x_1, x_0)
\end{aligned}$$

이다. 우변은 $$n \to \infty$$일 때 ($$0 \leq \lambda < 1$$이므로) $$0$$으로 가고, 이는 $$m, n$$에 관해 균등하게 작아지므로 $$(x_n)$$은 Cauchy 수열이다. 공간이 완비이므로 ([§거리공간, ⁋정의 4](/ko/math/analysis/metric_spaces#def4)) 극한 $$x_n \to x^\ast$$이 존재한다.

이 극한이 고정점임을 보인다. 축약사상은 $$d(Tx, Ty) \leq \lambda\, d(x, y)$$에서 곧바로 연속이므로

$$x^\ast = \lim_{n\to\infty} x_{n+1} = \lim_{n\to\infty} T x_n = T\Bigl(\lim_{n\to\infty} x_n\Bigr) = T x^\ast$$

이다. 마지막으로 유일성을 본다. $$x^\ast, y^\ast$$가 둘 다 고정점이면

$$d(x^\ast, y^\ast) = d(Tx^\ast, Ty^\ast) \leq \lambda\, d(x^\ast, y^\ast)$$

이고, $$\lambda < 1$$이므로 $$(1 - \lambda)\,d(x^\ast, y^\ast) \leq 0$$이 되어 $$d(x^\ast, y^\ast) = 0$$, 곧 $$x^\ast = y^\ast$$이다.

</details>

위 증명은 고정점의 존재와 유일성뿐 아니라 *수렴 속도*에 대한 정량적 정보까지 준다. 부등식 $$d(x_m, x_n) \leq \lambda^n/(1-\lambda) \cdot d(x_1, x_0)$$에서 $$m \to \infty$$로 보내면

$$d(x_n, x^\ast) \leq \frac{\lambda^n}{1 - \lambda}\,d(x_1, x_0)$$

라는 *선험적 오차 평가<sub>a priori error estimate</sub>*를 얻는다. 즉 반복 $$n$$번이면 오차가 $$\lambda^n$$의 비율로 줄어드는데, 이를 *선형 수렴<sub>linear convergence</sub>*이라 한다. 이 평가는 수치적으로 고정점을 근사할 때 몇 번 반복해야 원하는 정밀도에 도달하는지를 미리 알려 준다.

## 피카르–린델뢰프 정리

이제 초기값 문제

$$y'(t) = f(t, y(t)), \qquad y(t_0) = y_0$$

를 생각한다. 여기서 $$f$$는 평면의 한 영역에서 정의된 함수이고, 우리가 찾는 것은 그래프가 그 영역 안에 머물면서 위 방정식을 만족하는 함수 $$y$$이다. 해의 존재·유일성은 $$f$$가 둘째 변수에 대해 다음 조건을 만족할 때 보장된다.

립시츠 조건이 등장하는 까닭은 다음과 같다. $$f$$가 단지 연속이기만 하면 페아노 정리에 의해 해의 존재는 보장되지만 유일성은 보장되지 않는다. 유일성을 끌어내려면 $$f$$가 둘째 변수에 대해 변하는 정도를 일정하게 제어해야 하는데, 그 제어 조건이 바로 립시츠 조건이다. 이 조건은 미분가능성보다는 약하고 연속성보다는 강한, 중간 세기의 정칙성이다.

<div class="definition" markdown="1">

<ins id="def3">**정의 3**</ins> $$f(t, y)$$가 $$y$$에 대해 *립시츠 조건<sub>Lipschitz condition</sub>*을 만족한다는 것은, 상수 $$L$$이 존재하여 $$\lvert f(t, y_1) - f(t, y_2)\rvert \leq L\lvert y_1 - y_2\rvert$$이 성립하는 것이다.

</div>

상수 $$L$$을 *립시츠 상수<sub>Lipschitz constant</sub>*라 부른다. 기하적으로 이 조건은 같은 $$t$$에서 그래프 $$y \mapsto f(t, y)$$의 두 점을 잇는 모든 할선의 기울기가 $$\lvert$$기울기$$\rvert \leq L$$로 균등하게 유계임을 뜻한다. 만약 $$f$$가 둘째 변수에 대해 연속미분가능하고 $$\partial f / \partial y$$가 유계이면, [§[§평균값 정리와 테일러 정리, ⁋정리 3](/ko/math/analysis/mean_value_theorem#thm3)와 테일러 정리, ⁋정리 3](/ko/math/analysis/mean_value_theorem#thm3)에 의해

$$\lvert f(t, y_1) - f(t, y_2)\rvert = \left\lvert \frac{\partial f}{\partial y}(t, \xi)\right\rvert\,\lvert y_1 - y_2\rvert \leq L\,\lvert y_1 - y_2\rvert$$

이 성립하므로 ($$L = \sup\lvert \partial f / \partial y\rvert$$), 립시츠 조건은 자동으로 만족된다. 이것이 실제 응용에서 립시츠 조건을 확인하는 가장 흔한 방법이다.

<div class="proposition" markdown="1">

<ins id="thm4">**정리 4 (피카르–린델뢰프)**</ins> $$f$$가 $$(t_0, y_0)$$ 근방에서 연속이고 $$y$$에 대해 립시츠 조건을 만족하면, $$t_0$$의 어떤 닫힌구간 $$I$$ 위에서 초기값 문제의 해가 유일하게 존재한다.

</div>

<details class="proof" markdown="1">
<summary>증명</summary>

미분방정식과 초기 조건을 적분하면, 미적분의 기본정리 ([§미적분의 기본정리, ⁋정리 3](/ko/math/analysis/fundamental_theorem_of_calculus#thm3))에 의해 문제는 적분방정식

$$y(t) = y_0 + \int_{t_0}^t f(s, y(s))\,ds$$

와 동치이다. 실제로 $$y$$가 미분방정식의 해이면 양변을 $$t_0$$에서 $$t$$까지 적분하여 위 식을 얻고, 거꾸로 위 적분방정식을 만족하는 연속함수 $$y$$는 우변이 $$t$$에 대해 미분가능하므로 미분하면 $$y'(t) = f(t, y(t))$$를 얻고 $$t = t_0$$을 대입하면 $$y(t_0) = y_0$$을 얻는다. 적분방정식 형태가 유리한 이유는 미분이라는 까다로운 연산이 사라지고, 연속함수만 다루면 되기 때문이다.

우변을 연속함수 $$y$$에 대응시키는 *피카르 작용소<sub>Picard operator</sub>*

$$(Ty)(t) = y_0 + \int_{t_0}^t f(s, y(s))\,ds$$

를 생각하자. 그러면 적분방정식의 해는 정확히 $$T$$의 고정점 $$Ty = y$$이다. 충분히 짧은 닫힌구간 $$I = [t_0 - h, t_0 + h]$$ 위에서 연속함수들의 공간 $$C(I)$$에 상한노름 $$\lVert g\rVert_\infty = \sup_{t\in I}\lvert g(t)\rvert$$을 주면 이는 완비 거리공간이다. 두 연속함수 $$y_1, y_2$$에 대해, 립시츠 조건을 적분 안에서 적용하면

$$\begin{aligned}
\lvert (Ty_1)(t) - (Ty_2)(t)\rvert &= \left\lvert \int_{t_0}^t \bigl(f(s, y_1(s)) - f(s, y_2(s))\bigr)\,ds\right\rvert \\
&\leq \int_{t_0}^t \lvert f(s, y_1(s)) - f(s, y_2(s))\rvert\,ds \\
&\leq \int_{t_0}^t L\,\lvert y_1(s) - y_2(s)\rvert\,ds \\
&\leq L\,\lvert t - t_0\rvert\,\lVert y_1 - y_2\rVert_\infty \leq L h\,\lVert y_1 - y_2\rVert_\infty
\end{aligned}$$

이 모든 $$t \in I$$에서 성립한다. 좌변의 상한을 취하면

$$\lVert Ty_1 - Ty_2\rVert_\infty \leq L h\,\lVert y_1 - y_2\rVert_\infty$$

이다. 이제 구간의 반폭 $$h$$를 $$Lh < 1$$이 되도록, 가령 $$h < 1/L$$로 잡으면 $$T$$가 축약상수 $$\lambda = Lh$$인 축약사상이 된다. [정리 2](#thm2)에 의해 $$T$$는 유일한 고정점 $$y \in C(I)$$를 가지며, 이 $$y$$가 초기값 문제의 유일한 해이다.

</details>

증명에서 구간의 길이를 $$Lh < 1$$이 되도록 줄인 점에 주목하자. 이는 해가 *국소적으로* 존재함만을 보장한다. 즉 초기점 $$t_0$$ 근방의 작은 구간에서만 해가 보장되며, 그 구간이 전 구간으로 확장되는지는 별개의 문제이다. 한편 립시츠 상수가 작거나 구간이 짧을수록 작용소의 축약 효과가 강해 피카르 반복이 빠르게 수렴한다. 다음에서는 이 반복을 실제로 수행해 해를 구하는 예를 본다.

## 예시와 계산

피카르 정리의 증명은 단순한 존재 보장에 그치지 않고, 해를 구체적으로 구하는 절차인 피카르 반복을 제공한다. 임의의 출발 함수(보통 상수함수 $$y_0 \equiv y_0$$)에서 시작해 작용소 $$T$$를 거듭 적용하면 그 극한이 해가 된다. 가령 $$y' = y$$, $$y(0) = 1$$에서 $$y_0 \equiv 1$$로 출발하면 반복은 지수함수의 부분합 $$y_n(t) = \sum_{k=0}^n t^k/k!$$을 차례로 내놓고, 극한 $$e^t$$가 곧 해이다. 우변이 $$t$$와 $$y$$ 모두에 의존해도 절차는 그대로 작동하여, $$y' = t + y$$, $$y(0) = 0$$의 반복은 해 $$y = e^t - 1 - t$$로 수렴한다.

반대로 립시츠 조건이 빠지면 유일성이 어떻게 깨지는지를 명시적인 반례로 본다.

<div class="example" markdown="1">

<ins id="ex5">**예시 5 (유일성의 실패)**</ins> $$y' = \sqrt{\lvert y\rvert}$$, $$y(0) = 0$$을 생각하자. 여기서 $$f(t, y) = \sqrt{\lvert y\rvert}$$는 연속이지만 $$y = 0$$ 근방에서

$$\frac{\lvert f(t, y) - f(t, 0)\rvert}{\lvert y - 0\rvert} = \frac{\sqrt{\lvert y\rvert}}{\lvert y\rvert} = \frac{1}{\sqrt{\lvert y\rvert}} \to \infty \qquad (y \to 0)$$

이므로 립시츠 조건을 만족하지 않는다. 이때 항등적으로 $$0$$인 함수 $$y \equiv 0$$이 해이지만, 동시에

$$y(t) = \begin{cases} t^2/4, & t \geq 0 \\ 0, & t < 0 \end{cases}$$

도 해이다 ($$t \geq 0$$에서 $$y' = t/2 = \sqrt{t^2/4} = \sqrt{y}$$). 더 나아가 임의의 $$a > 0$$에 대해 $$t \leq a$$에서는 $$0$$이고 $$t > a$$에서는 $$(t - a)^2/4$$인 함수도 모두 해이므로, 해가 무수히 많다. 립시츠 조건의 부재가 유일성을 송두리째 무너뜨림을 보여 준다.

</div>

## 응용

존재 구간이 국소적이라는 한계는 우변의 정칙성에 따라 극복되기도 하고 본질적으로 남기도 한다. 다음 명제는 립시츠 조건이 *전역적*으로 성립할 때 해가 전 구간으로 확장됨을 보인다.

<div class="proposition" markdown="1">

<ins id="prop6">**명제 6 (전역 존재)**</ins> $$f(t, y)$$가 띠 영역 $$\lvert t - t_0\rvert \leq a$$, $$y \in \mathbb{R}$$ 전체에서 연속이고 $$y$$에 대해 상수 $$L$$의 전역 립시츠 조건을 만족하면, 초기값 문제의 해가 구간 $$[t_0 - a, t_0 + a]$$ 전체에서 유일하게 존재한다.

</div>

<details class="proof" markdown="1">
<summary>증명</summary>

피카르 반복 $$y_{n+1} = Ty_n$$을 $$y_0 \equiv y_0$$에서 시작하자. 연속한 두 근사의 차를 평가한다. $$M = \sup_{\lvert t - t_0\rvert \leq a}\lvert f(t, y_0)\rvert$$로 두면

$$\lvert y_1(t) - y_0(t)\rvert = \left\lvert \int_{t_0}^t f(s, y_0)\,ds\right\rvert \leq M\,\lvert t - t_0\rvert$$

이고, 귀납적으로 립시츠 조건을 반복 적용하면

$$\begin{aligned}
\lvert y_{n+1}(t) - y_n(t)\rvert &\leq \int_{t_0}^t L\,\lvert y_n(s) - y_{n-1}(s)\rvert\,ds \\
&\leq M\,\frac{L^n \lvert t - t_0\rvert^{n+1}}{(n+1)!}
\end{aligned}$$

을 얻는다. 따라서 $$\lvert t - t_0\rvert \leq a$$에서 $$\lVert y_{n+1} - y_n\rVert_\infty \leq M (La)^{n+1}/(L\,(n+1)!)$$이고, 우변은 지수급수의 항이라 그 합이 유한하다. 망원합 $$y_n = y_0 + \sum_{k=0}^{n-1}(y_{k+1} - y_k)$$이 상한노름에서 절대수렴하므로 $$y_n$$은 어떤 연속함수 $$y$$로 균등수렴하고, 극한에서 $$y = Ty$$이다. 유일성은 [정리 4](#thm4)의 논법을 구간 전체에서 그뢴발 부등식으로 잇거나, 구간을 길이 $$1/(2L)$$ 이하의 조각으로 나누어 각 조각에서 [정리 2](#thm2)를 적용해 얻는다.

</details>

[명제 6](#prop6)의 핵심은 립시츠 상수 $$L$$이 $$y$$의 크기에 무관하게 *하나의 상수*로 잡힌다는 데 있다. 그러면 피카르 반복의 차가 $$L^n / n!$$의 빠르기로 줄어 구간 길이에 관계없이 수렴하므로, [정리 4](#thm4)에서 구간을 줄일 필요가 없어진다. 전역 립시츠 조건이 성립하는 가장 중요한 경우가 우변이 $$y$$에 대해 선형인 방정식이다. 실제로 $$y' = a(t)\,y + b(t)$$에서 $$a, b$$가 닫힌구간 $$I$$에서 연속이면 $$\lvert a(t)\rvert$$이 $$I$$에서 유계라 그 상한 $$L$$이 전역 립시츠 상수가 되고, [명제 6](#prop6)에 의해 해가 $$I$$ 전체에서 유일하게 존재한다. 가령 $$y' = -2t\,y$$의 해 $$e^{-t^2}$$처럼 선형 방정식의 해는 정의 구간 밖으로 폭발하지 않고 끝까지 살아남는다. 반면 비선형 방정식에서는 해가 유한 시간에 발산할 수 있다.

<div class="example" markdown="1">

<ins id="ex7">**예시 7 (유한 시간 폭발)**</ins> $$y' = y^2$$, $$y(0) = 1$$을 보자. 여기서 $$f(t, y) = y^2$$는 임의의 유계 영역에서는 립시츠 조건을 만족하므로 국소해가 존재하고, 변수분리로

$$\int \frac{dy}{y^2} = \int dt \;\Longrightarrow\; -\frac{1}{y} = t + C$$

를 풀면 $$y(0) = 1$$에서 $$C = -1$$, 곧

$$y(t) = \frac{1}{1 - t}$$

이다. 이 해는 $$t \to 1^-$$에서 $$+\infty$$로 발산하므로 구간 $$[0, 1)$$ 너머로 연장되지 않는다. $$\partial f / \partial y = 2y$$가 $$y$$와 함께 무한히 커져 전역 립시츠 조건이 깨지는 것이 폭발의 원인이며, [정리 4](#thm4)의 국소성이 본질적임을 보여 준다.

</div>

마지막으로 피카르 정리가 직접 주는 정량적 귀결 하나를 정리해 둔다. 증명의 오차 평가를 그대로 옮긴 것이다.

<div class="proposition" markdown="1">

<ins id="prop8">**명제 8 (반복의 오차)**</ins> [정리 4](#thm4)의 가정 아래, 피카르 반복 $$y_n = T^n y_0$$과 참해 $$y$$ 사이에는

$$\lVert y_n - y\rVert_\infty \leq \frac{(Lh)^n}{1 - Lh}\,\lVert y_1 - y_0\rVert_\infty$$

이 성립한다. 여기서 $$h$$는 [정리 4](#thm4)에서 잡은 구간의 반폭이고 $$Lh < 1$$이다.

</div>

<details class="proof" markdown="1">
<summary>증명</summary>

작용소 $$T$$는 $$C(I)$$ 위에서 축약상수 $$\lambda = Lh < 1$$의 축약사상이고 $$y$$는 그 고정점이므로, [정리 2](#thm2)의 증명에서 얻은 선험적 오차 평가

$$d(x_n, x^\ast) \leq \frac{\lambda^n}{1 - \lambda}\,d(x_1, x_0)$$

을 $$x_n = y_n$$, $$x^\ast = y$$, $$\lambda = Lh$$에 그대로 적용하면 주장하는 부등식을 얻는다.

</details>

이 평가 덕분에 피카르 반복은 단순한 존재 증명의 도구를 넘어, 정해진 오차 안에서 해를 근사하는 실제 계산법이 된다. $$Lh$$가 작을수록 한 번의 반복으로 오차가 더 크게 줄어든다.

이렇게 축약사상 원리는 미분방정식의 초기값 문제를 고정점 문제로 환원하여, 해의 존재·유일성을 한꺼번에 그리고 구성적으로 확립한다. $$f$$가 $$y$$에 대해 선형이면 립시츠 조건이 전역적으로 성립하여 해가 구간 전체로 확장된다([명제 6](#prop6)).
