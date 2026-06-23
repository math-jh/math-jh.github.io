---
title: "거리공간"
description: "두 점 사이의 거리라는 개념을 공리화한 거리공간을 정의하고, 여러 예를 든다. 거리로부터 수렴과 Cauchy 수열, 완비성을 일반화하여 실수에서 얻은 해석학의 언어를 추상적 공간으로 옮긴다."
excerpt: "거리공간의 공리, 수렴과 완비성, 위상으로의 연결"

categories: [Math / Analysis]
permalink: /ko/math/analysis/metric_spaces
sidebar: 
    nav: "analysis-ko"

date: 2026-06-02
weight: 6

published: false
---

지금까지의 해석학은 실수 위에서 전개되었다. 그러나 수렴·Cauchy·연속 같은 개념의 본질은 "두 대상이 얼마나 가까운가"라는 거리뿐이며, 그 거리가 몇 가지 자연스러운 성질만 만족하면 실수에서 했던 논증이 거의 그대로 옮겨 간다. 이러한 추상화가 거리공간이다.

## 거리공간의 정의

<div class="definition" markdown="1">

<ins id="def1">**정의 1**</ins> 집합 $$X$$와 함수 $$d : X \times X \to \mathbb{R}$$가 다음을 만족하면 $$(X, d)$$를 *거리공간<sub>metric space</sub>*, $$d$$를 *거리<sub>metric</sub>*라 한다. 모든 $$x, y, z \in X$$에 대하여

1. $$d(x, y) \geq 0$$이고, $$d(x, y) = 0$$인 것은 $$x = y$$인 것과 동치이다;
2. (대칭성) $$d(x, y) = d(y, x)$$;
3. (삼각부등식) $$d(x, z) \leq d(x, y) + d(y, z)$$.

</div>

<div class="example" markdown="1">

<ins id="ex2">**예시 2**</ins> 다음은 모두 거리공간이다.

- $$\mathbb{R}$$에 $$d(x, y) = \lvert x - y\rvert$$를 준 것. 우리가 다뤄 온 표준 거리이다.
- $$\mathbb{R}^n$$에 유클리드 거리 $$d(x, y) = \sqrt{\sum_{i=1}^n (x_i - y_i)^2}$$를 준 것.
- 임의의 집합 $$X$$에 $$x \neq y$$이면 $$d(x, y) = 1$$, $$x = y$$이면 $$0$$으로 준 *이산거리*.
- 닫힌구간 위의 연속함수들의 공간 $$C[a,b]$$에 $$d(f, g) = \sup_{x}\lvert f(x) - g(x)\rvert$$를 준 것.

</div>

## 수렴과 완비성

거리만 있으면 수렴과 Cauchy 조건을 [§수열의 수렴](/ko/math/analysis/convergence_of_sequences)·[§Cauchy 수열과 완비성](/ko/math/analysis/cauchy_sequences)에서와 똑같은 형태로 정의할 수 있다. $$\lvert a_n - L\rvert$$을 $$d(a_n, L)$$로 바꾸기만 하면 된다.

<div class="definition" markdown="1">

<ins id="def3">**정의 3**</ins> 거리공간 $$(X, d)$$의 점열 $$(x_n)$$이 $$x \in X$$로 *수렴*한다는 것은 $$d(x_n, x) \to 0$$인 것이다. $$(x_n)$$이 *Cauchy*라는 것은 임의의 $$\varepsilon > 0$$에 대해 $$N$$이 있어 $$m, n \geq N$$이면 $$d(x_m, x_n) < \varepsilon$$인 것이다. 중심 $$x$$, 반지름 $$r > 0$$의 *열린공<sub>open ball</sub>*은 $$B(x, r) = \{y \in X \mid d(x, y) < r\}$$이다.

</div>

실수에서와 마찬가지로 수렴하는 점열은 Cauchy이지만, 그 역은 공간에 따라 성립하지 않을 수 있다.

<div class="definition" markdown="1">

<ins id="def4">**정의 4**</ins> 거리공간 $$(X, d)$$에서 모든 Cauchy 점열이 (그 공간 안의 점으로) 수렴하면 $$(X, d)$$를 *완비<sub>complete</sub>*하다고 한다.

</div>

실수의 완비성 ([§Cauchy 수열과 완비성, ⁋정리 4](/ko/math/analysis/cauchy_sequences#thm4))은 곧 표준 거리를 준 $$\mathbb{R}$$이 완비 거리공간이라는 진술이다. 같은 논증을 좌표별로 적용하면 유클리드 공간 $$\mathbb{R}^n$$도 완비임을 얻는다. 반면 유리수 $$\mathbb{Q}$$나 개구간 $$(0,1)$$은 완비가 아니다 — 경계로 다가가는 Cauchy 점열의 극한이 빠져 있기 때문이다. 완비성은 부동점 정리를 비롯한 존재 정리들의 무대가 되며, 이는 [§미분방정식의 존재성과 유일성](/ko/math/analysis/existence_uniqueness_ode)에서 결정적으로 쓰인다.

## 거리의 기본 성질

거리공간의 공리 세 개는 짧지만, 실수에서 익숙하게 쓰던 부등식들을 모두 함의한다. 먼저 거리 자체가 두 변수에 대해 연속적으로 변한다는 사실, 곧 점을 조금 움직이면 거리도 조금밖에 변하지 않는다는 직관을 정량화하는 *역삼각부등식<sub>reverse triangle inequality</sub>*을 확인한다. 이 부등식은 수렴하는 점열의 거리를 다룰 때 거듭 쓰인다.

<div class="proposition" markdown="1">

<ins id="prop5">**명제 5**</ins> 거리공간 $$(X, d)$$의 임의의 세 점 $$x, y, z$$에 대하여

$$\lvert d(x, z) - d(y, z)\rvert \leq d(x, y)$$

가 성립한다.

</div>

<details class="proof" markdown="1">
<summary>증명</summary>

삼각부등식을 두 번 적용한다. 한편으로

$$\begin{aligned}
d(x, z) &\leq d(x, y) + d(y, z) \\
&\implies d(x, z) - d(y, z) \leq d(x, y)
\end{aligned}$$

이고, 다른 한편으로 $$x$$와 $$y$$의 역할을 바꾸면

$$\begin{aligned}
d(y, z) &\leq d(y, x) + d(x, z) = d(x, y) + d(x, z) \\
&\implies d(y, z) - d(x, z) \leq d(x, y)
\end{aligned}$$

이다. 둘째 줄에서는 대칭성 $$d(y, x) = d(x, y)$$를 썼다. 두 부등식을 합치면 $$d(x, z) - d(y, z)$$가 $$-d(x, y)$$ 이상이고 $$d(x, y)$$ 이하이므로, 절댓값으로 묶어 결론을 얻는다.

</details>

역삼각부등식의 직접적 귀결은 거리 함수의 연속성이다. 점열 $$(x_n)$$이 $$x$$로 수렴하면 [명제 5](#prop5)에 의해 임의의 고정점 $$z$$에 대해

$$\lvert d(x_n, z) - d(x, z)\rvert \leq d(x_n, x) \to 0$$

이므로 $$d(x_n, z) \to d(x, z)$$이다. 즉 수렴은 거리값의 수렴으로 그대로 전달된다. 이 관찰은 다음 명제의 유일성 증명에서 곧바로 쓰인다.

<div class="proposition" markdown="1">

<ins id="prop6">**명제 6**</ins> 거리공간에서 수렴하는 점열의 극한은 유일하다. 또한 수렴하는 점열은 모두 Cauchy이다.

</div>

<details class="proof" markdown="1">
<summary>증명</summary>

먼저 극한의 유일성을 보인다. $$(x_n)$$이 $$x$$와 $$x'$$ 두 점으로 동시에 수렴한다고 하자. 삼각부등식으로

$$0 \leq d(x, x') \leq d(x, x_n) + d(x_n, x')$$

이고, 우변의 두 항이 각각 $$0$$으로 가므로 $$d(x, x') = 0$$이다. 공리 1에 의해 $$x = x'$$이다.

다음으로 $$(x_n)$$이 $$x$$로 수렴하면 Cauchy임을 보인다. 임의의 $$\varepsilon > 0$$에 대해 $$N$$이 있어 $$n \geq N$$이면 $$d(x_n, x) < \varepsilon/2$$이다. 그러면 $$m, n \geq N$$일 때

$$\begin{aligned}
d(x_m, x_n) &\leq d(x_m, x) + d(x, x_n) \\
&< \frac{\varepsilon}{2} + \frac{\varepsilon}{2} = \varepsilon
\end{aligned}$$

이므로 $$(x_n)$$은 Cauchy이다.

</details>

[명제 6](#prop6)은 완비성의 정의 ([정의 4](#def4))를 다시 음미하게 한다. 어떤 거리공간에서든 수렴하면 Cauchy이지만, 완비공간이란 정확히 그 역까지 성립하여 "Cauchy"와 "수렴"이 같은 뜻이 되는 공간이다. 완비성이 깨지는 전형적 상황은 점열이 극한처럼 행동하는데 그 극한이 공간 밖에 있을 때이며, 아래 예시들에서 이를 구체적으로 본다.

## 예시

거리공간의 풍부함은 같은 바탕집합에 서로 다른 거리를 줄 수 있다는 데 있다. 유클리드 거리 외에도 $$\mathbb{R}^n$$에는 좌표의 절댓값 합 $$d_1(x, y) = \sum_{i=1}^n \lvert x_i - y_i\rvert$$이나 최대 절댓값 $$d_\infty(x, y) = \max_{1 \leq i \leq n} \lvert x_i - y_i\rvert$$로도 거리를 줄 수 있다. 각 좌표에서 실수의 삼각부등식 $$\lvert x_i - z_i\rvert \leq \lvert x_i - y_i\rvert + \lvert y_i - z_i\rvert$$이 성립하므로 양변을 더하면 $$d_1$$이, 최댓값을 취하면 $$d_\infty$$가 삼각부등식을 물려받는다. 이 세 거리는 같은 점에서 서로 다른 값을 줄 수 있지만, 임의의 $$x, y$$에서 부등식 사슬

$$d_\infty(x, y) \leq d_2(x, y) \leq d_1(x, y) \leq n\, d_\infty(x, y)$$

가 성립하여 서로를 상수배로 누른다. 따라서 한 거리로 수렴하는 점열은 나머지 두 거리로도 수렴하며, 세 거리는 $$\mathbb{R}^n$$에 같은 위상을 준다.

이산거리 ([예시 2](#ex2))는 거리공간이 얼마나 일반적인 대상인지를 보여 주는 극단적 예이다. 모든 서로 다른 두 점의 거리가 $$1$$이므로, 거리에 담긴 "가까움"의 정보가 사실상 없다.

<div class="example" markdown="1">

<ins id="ex7">**예시 7 (이산거리에서의 수렴)**</ins> 집합 $$X$$에 이산거리 $$d$$를 주자. 거리값이 $$0$$ 또는 $$1$$뿐이므로, $$\varepsilon = 1/2$$에 대해 $$d(x_n, x) < 1/2$$은 곧 $$d(x_n, x) = 0$$, 즉 $$x_n = x$$를 뜻한다. 따라서

$$x_n \to x \iff \text{어떤 } N \text{부터 } x_n = x \text{로 일정}$$

이다. 같은 이유로 Cauchy 점열은 결국 한 점으로 일정해지므로 수렴한다 — 이산거리 공간은 언제나 완비이다.

</div>

완비성이 깨지는 모습은 같은 점열을 더 큰 공간과 더 작은 공간에서 비교할 때 가장 선명하다.

<div class="example" markdown="1">

<ins id="ex8">**예시 8 (개구간의 비완비성)**</ins> 표준 거리를 준 개구간 $$X = (0, 1)$$을 생각하자. 점열 $$x_n = 1/n$$ ($$n \geq 2$$)은 $$X$$ 안에 있고, $$\mathbb{R}$$의 점 $$0$$으로 다가가므로

$$d(x_m, x_n) = \left\lvert \frac1m - \frac1n \right\rvert \leq \frac1m + \frac1n \to 0$$

이라 Cauchy이다. 그러나 $$X$$ 안에는 이 점열의 극한이 없다. 만일 $$x_n \to L \in (0,1)$$이라면 $$\mathbb{R}$$에서의 극한 유일성 ([명제 6](#prop6)) 에 의해 $$L = 0$$이어야 하는데 $$0 \notin (0,1)$$이기 때문이다. 따라서 $$(0,1)$$은 완비가 아니다. 반면 닫힌구간 $$[0,1]$$에서는 같은 점열이 $$0$$으로 수렴하며, 실제로 $$[0,1]$$은 완비이다 — 닫힌구간은 그 극한들을 모두 품고 있기 때문이다.

</div>

연속함수 공간의 sup 거리 ([예시 2](#ex2)) 는 무한차원 거리공간의 대표적 예이며, 그 완비성이 해석학의 여러 존재 정리를 떠받친다. $$C[a,b]$$에 sup 거리 $$d(f, g) = \sup_{x \in [a,b]} \lvert f(x) - g(x)\rvert$$를 주면, 이 거리에서 $$f_n \to f$$라는 것은 $$\sup_{x \in [a,b]} \lvert f_n(x) - f(x)\rvert \to 0$$, 곧 $$(f_n)$$이 $$f$$로 *균등수렴*한다는 것과 정확히 같다. 균등수렴하는 연속함수열의 극한은 다시 연속이므로 $$C[a,b]$$의 모든 sup-Cauchy 함수열은 어떤 연속함수로 수렴하며, 따라서 $$(C[a,b], d)$$는 완비 거리공간이다.

## 응용: 닫힌 부분공간과 고정점

완비 거리공간의 "닫힌" 부분집합은 다시 완비가 된다는 사실은, 큰 완비공간에서 출발해 그 안의 부분공간의 완비성을 거저 얻는 흔한 수단이다. 부분집합 $$Y \subseteq X$$가 *닫혀 있다<sub>closed</sub>*는 것은 $$Y$$ 안의 점열이 $$X$$에서 수렴할 때 그 극한이 다시 $$Y$$에 속한다는 것이다.

<div class="proposition" markdown="1">

<ins id="prop9">**명제 9**</ins> $$(X, d)$$가 완비이고 $$Y \subseteq X$$가 닫혀 있으면, $$Y$$에 $$d$$를 제한한 거리공간도 완비이다.

</div>

<details class="proof" markdown="1">
<summary>증명</summary>

$$(y_n)$$을 $$Y$$ 안의 Cauchy 점열이라 하자. $$Y$$에서의 거리는 $$X$$에서의 거리와 같으므로 $$(y_n)$$은 $$X$$에서도 Cauchy이고, $$X$$의 완비성에 의해 어떤 $$x \in X$$로 수렴한다.

$$\begin{aligned}
(y_n) \text{이 } X \text{에서 Cauchy} &\implies y_n \to x \text{ for some } x \in X \\
Y \text{가 닫힘},\ y_n \in Y &\implies x \in Y
\end{aligned}$$

따라서 극한 $$x$$는 $$Y$$에 속하고, $$(y_n)$$은 $$Y$$ 안의 점으로 수렴한다. $$Y$$ 안의 임의의 Cauchy 점열이 $$Y$$ 안에서 수렴하므로 $$Y$$는 완비이다.

</details>

이 명제는 닫힌구간 $$[a,b]$$가 완비라는 사실을 즉시 설명한다. $$[a,b]$$는 완비공간 $$\mathbb{R}$$의 닫힌 부분집합이므로 [명제 9](#prop9)에 의해 완비이고, [예시 8](#ex8)에서 본 $$(0,1)$$과의 차이가 바로 닫힘 여부에 있었던 것이다. 같은 논리로 $$\mathbb{R}^n$$의 닫힌 공이나 구면처럼 닫힌 집합들은 모두 완비 거리공간이 된다.

완비성이 마련해 주는 가장 중요한 도구는 *축약사상<sub>contraction</sub>*의 고정점이다. 거리를 일정 비율 $$\lambda < 1$$로 줄이는 사상 $$T$$, 곧 $$d(Tx, Ty) \leq \lambda\, d(x, y)$$를 만족하는 사상을 한 점에서 반복하면, 완비성 덕분에 그 반복열이 Cauchy가 되어 유일한 고정점으로 수렴한다. 가령 $$\mathbb{R}$$ 위의 $$T(x) = x/2 + 1$$은 비율 $$\lambda = 1/2$$의 축약사상이고, 그 반복은 유일한 고정점 $$2 = T(2)$$로 수렴한다. 이 현상을 일반화한 것이 완비 거리공간 위의 [§미분방정식의 존재성과 유일성, ⁋정리 2](/ko/math/analysis/existence_uniqueness_ode#thm2)이며, $$\mathbb{R}$$의 완비성이 수렴을 보장하는 핵심이었듯 완비성이 그 무대가 된다 ([§미분방정식의 존재성과 유일성, ⁋정리 2](/ko/math/analysis/existence_uniqueness_ode#thm2)).

## 위상으로의 연결

열린공은 거리공간에 "열린집합"이라는 위상적 구조를 부여하는 출발점이다. 거리공간은 [\[위상수학\] §열린집합](/ko/math/topology/open_sets)에서 공리적으로 도입하는 위상공간의 가장 중요한 예이며, 해석학의 거리 기반 개념들은 위상수학의 더 일반적인 틀 안에 자연스럽게 자리 잡는다.
