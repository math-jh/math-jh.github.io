---
title: "연속함수의 성질"
description: "연속함수가 컴팩트집합을 컴팩트집합으로 보냄을 보이고, 그로부터 최대·최소 정리를 증명한다. 컴팩트집합 위의 연속함수가 균등연속이라는 하이네–칸토어 정리도 다룬다."
excerpt: "컴팩트성의 보존, 최대·최소 정리, 균등연속성"

categories: [Math / Analysis]
permalink: /ko/math/analysis/continuous_functions
sidebar: 
    nav: "analysis-ko"

header:
    overlay_image: /assets/images/Math/Analysis/Continuous_Functions.png
    overlay_filter: 0.5

date: 2026-06-02
last_modified_at: 2026-06-02
weight: 10

published: false
---

[\[미적분학\] §연속함수](/ko/math/calculus/continuity)에서 우리는 최대·최소 정리를 증명 없이 도구로 받아들였다. 이제 [§컴팩트성](/ko/math/analysis/compactness)을 갖추었으므로 이를 증명할 수 있다. 핵심은 연속함수가 컴팩트성을 보존한다는 단 하나의 사실이다.

연속성은 정의역의 위상적 성질이 상으로 옮겨 가는지를 묻는 관점에서 보면 가장 잘 이해된다. 연속함수가 열린집합의 역상을 열린집합으로 보낸다는 ([§함수의 극한과 연속, ⁋명제 3](/ko/math/analysis/limits_and_continuity#prop3)) 위상적 특징화는, 정의역의 구조가 아니라 정의역 위에서 측정되는 양들의 거동을 통제한다. 그러나 컴팩트성·연결성과 같은 "전역적" 성질은 역상이 아니라 상의 방향으로 보존되며, 바로 이 보존이 해석학의 존재 정리들 — 최댓값의 존재, 중간값의 존재 — 을 떠받친다. 이 글에서 우리는 그중 컴팩트성의 보존을 출발점으로 삼아, 거기서 최대·최소 정리와 균등연속성을 차례로 끌어낸다.

## 컴팩트성의 보존

<div class="proposition" markdown="1">

<ins id="thm1">**정리 1**</ins> $$f : X \to Y$$가 연속이고 $$K \subseteq X$$가 점렬컴팩트이면, 상 $$f(K)$$도 점렬컴팩트이다.

</div>

<details class="proof" markdown="1">
<summary>증명</summary>

$$f(K)$$의 점열 $$(y_n)$$을 택하면 $$y_n = f(x_n)$$인 $$x_n \in K$$이 있다. $$K$$가 점렬컴팩트이므로 $$x_{n_k} \to x \in K$$인 부분수열이 있고, $$f$$의 연속성과 점열 특징화 ([§함수의 극한과 연속, ⁋명제 2](/ko/math/analysis/limits_and_continuity#prop2))에 의해

$$y_{n_k} = f(x_{n_k}) \longrightarrow f(x) \in f(K)$$

이다. 따라서 $$(y_n)$$이 $$f(K)$$ 안의 점으로 수렴하는 부분수열을 가지므로 $$f(K)$$는 점렬컴팩트이다.

</details>

증명에서 본질적으로 쓰인 것은 연속성의 점열 특징화 하나뿐이며, 정의역과 공역의 차원이나 구체적 구조는 전혀 개입하지 않는다. 그 결과 정리 1은 임의의 거리공간 사이의 연속함수에 그대로 적용된다. 한편 컴팩트성과 달리 닫힘이나 유계성은 연속함수가 보존하지 않음을 유의해야 한다 — 예컨대 $$f(x) = \arctan x$$는 닫힌집합 $$\mathbb{R}$$를 유계인 열린구간 $$(-\tfrac\pi2, \tfrac\pi2)$$로 보내고, $$g(x) = 1/x$$는 유계가 아닌 닫힌집합 $$(0, 1]$$ 위에서 유계가 아닌 상을 만든다. 컴팩트성이 닫힘과 유계의 결합이라는 점([§컴팩트성, ⁋정리 2](/ko/math/analysis/compactness#thm2))을 떠올리면, 두 성질이 따로따로는 깨지지만 묶어 놓으면 보존된다는 사실이 더욱 두드러진다.

## 최대·최소 정리

실숫값 연속함수에 정리 1을 적용하면 최댓값과 최솟값의 존재가 곧바로 따른다. 핵심 관찰은 $$\mathbb{R}$$의 점렬컴팩트 부분집합이 자신의 상한과 하한을 원소로 포함한다는 것이다. 닫혀 있고 유계인 집합은 상·하한이 존재하며, 닫힘 때문에 그 극한값이 집합 안에 들어오기 때문이다. 따라서 $$f$$의 상 $$f(K)$$가 점렬컴팩트라는 정리 1의 결론만으로 최댓값·최솟값이 실현된다.

<div class="proposition" markdown="1">

<ins id="cor2">**따름정리 2 (최대·최소 정리)**</ins> $$K$$가 점렬컴팩트이고 $$f : K \to \mathbb{R}$$가 연속이면, $$f$$는 $$K$$에서 최댓값과 최솟값을 가진다. 특히 닫힌구간 $$[a,b]$$에서 연속인 함수는 최댓값과 최솟값을 가진다.

</div>

<details class="proof" markdown="1">
<summary>증명</summary>

정리 1에 의해 $$f(K) \subseteq \mathbb{R}$$는 점렬컴팩트이고, 하이네–보렐 정리 ([§컴팩트성, ⁋정리 2](/ko/math/analysis/compactness#thm2))에 의해 닫혀 있고 유계이다. 유계이므로

$$M = \sup f(K)$$

가 존재한다 ([§실수의 완비성, ⁋정의 2](/ko/math/analysis/completeness_of_reals#def2)). 상한의 근사 성질로부터 각 $$n$$에 대해

$$M - \tfrac1n < y_n \leq M, \qquad y_n \in f(K)$$

인 $$y_n$$을 고를 수 있고, 따라서 $$y_n \to M$$이다. $$f(K)$$가 닫혀 있으므로 그 극한 $$M$$도 $$f(K)$$의 원소이다. 즉 $$M = f(x_{\max})$$인 $$x_{\max} \in K$$가 있어 $$M$$이 최댓값이다. 하한 $$m = \inf f(K)$$에 대해서도 같은 논증을 적용하면 $$m = f(x_{\min})$$인 $$x_{\min} \in K$$가 있어 최솟값이 실현된다. 마지막 주장은 닫힌구간 $$[a,b]$$가 닫혀 있고 유계여서 점렬컴팩트이므로 곧바로 따른다.

</details>

이로써 [\[미적분학\] §연속함수, ⁋정리 3](/ko/math/calculus/continuity#thm3)에서 받아들였던 최대·최소 정리가 완비성에 기초하여 증명되었고, 그것에 의존하던 [\[미적분학\] §평균값 정리](/ko/math/calculus/mean_value_theorem)의 롤의 정리도 정당화된다.

## 균등연속성

보통의 연속에서는 주어진 $$\varepsilon$$에 대해 고르는 $$\delta$$가 점 $$a$$마다 달라질 수 있다. 함수가 가파른 곳에서는 작은 $$\delta$$가, 완만한 곳에서는 큰 $$\delta$$가 필요하기 때문이다. 만일 어떤 곳에서는 $$\delta$$가 한없이 작아져야 한다면, 모든 점에 공통으로 통하는 양의 $$\delta$$를 잡을 수 없다. 균등연속은 바로 그런 공통의 $$\delta$$를 잡을 수 있다는 한층 강한 조건이며, 컴팩트성은 정의역이 "유한히 통제"되도록 만들어 이 강화를 가능하게 한다.

<div class="definition" markdown="1">

<ins id="def3">**정의 3**</ins> $$f : X \to Y$$가 *균등연속<sub>uniformly continuous</sub>*이라는 것은, 임의의 $$\varepsilon > 0$$에 대하여 $$\delta > 0$$이 존재하여 ($$x$$에 무관하게) 모든 $$x, x'$$에 대해 $$d_X(x, x') < \delta$$이면 $$d_Y(f(x), f(x')) < \varepsilon$$인 것이다.

</div>

정의 1의 연속과의 차이는 한정사의 순서에 있다. 점별 연속은 $$\varepsilon$$과 점 $$a$$를 먼저 받은 뒤 $$\delta$$를 고르는 반면, 균등연속은 $$\varepsilon$$만 받고 모든 점에 동시에 통하는 $$\delta$$를 고른다. 기호로 적으면, 점별 연속이

$$\forall \varepsilon\, \forall a\, \exists \delta\, \forall x : \bigl(d_X(x, a) < \delta \implies d_Y(f(x), f(a)) < \varepsilon\bigr)$$

인 데 비해, 균등연속은 $$\delta$$를 $$a$$보다 앞으로 끌어내어

$$\forall \varepsilon\, \exists \delta\, \forall x\, \forall x' : \bigl(d_X(x, x') < \delta \implies d_Y(f(x), f(x')) < \varepsilon\bigr)$$

이다. $$\exists \delta$$가 $$\forall a$$보다 안쪽에 있는지 바깥쪽에 있는지가 두 개념을 가른다. 균등연속이면 분명히 연속이지만, 그 역은 일반적으로 성립하지 않는다.

<div class="proposition" markdown="1">

<ins id="thm4">**정리 4 (하이네–칸토어)**</ins> 점렬컴팩트집합 위에서 연속인 함수는 균등연속이다.

</div>

<details class="proof" markdown="1">
<summary>증명</summary>

$$f$$가 $$K$$에서 연속이지만 균등연속이 아니라 하자. 그러면 어떤 $$\varepsilon > 0$$에 대해, 모든 $$\delta = 1/n$$이 실패하여

$$d_X(x_n, x_n') < \tfrac1n \quad\text{이면서}\quad d_Y\bigl(f(x_n), f(x_n')\bigr) \geq \varepsilon$$

인 두 점열 $$(x_n), (x_n')$$이 있다. $$K$$가 점렬컴팩트이므로 $$x_{n_k} \to x \in K$$인 부분수열이 있고, 짝지어진 점 $$x_{n_k}'$$도

$$d_X(x_{n_k}', x) \leq d_X(x_{n_k}', x_{n_k}) + d_X(x_{n_k}, x) < \tfrac{1}{n_k} + d_X(x_{n_k}, x) \longrightarrow 0$$

이므로 같은 $$x$$로 수렴한다. 그런데 연속성과 점열 특징화에 의해

$$\begin{aligned}
d_Y\bigl(f(x_{n_k}), f(x_{n_k}')\bigr)
&\leq d_Y\bigl(f(x_{n_k}), f(x)\bigr) + d_Y\bigl(f(x), f(x_{n_k}')\bigr) \\
&\longrightarrow 0 + 0 = 0
\end{aligned}$$

이어서 두 상의 거리가 $$0$$으로 가야 한다. 이는 그 거리가 모든 $$k$$에서 $$\varepsilon$$ 이상이라는 데 모순이다. 따라서 $$f$$는 균등연속이다.

</details>

증명은 컴팩트성을 점열로 두 번 — 한 번은 $$(x_n)$$의 수렴 부분수열을 뽑기 위해 — 사용했을 뿐, 함수의 구체적 형태에는 의존하지 않는다. 컴팩트성이 빠지면 결론이 무너진다는 것을 다음 절의 예시들에서 직접 확인한다.

## 예시와 계산

이제 위 정리들이 실제로 어떻게 작동하는지, 그리고 가정이 빠졌을 때 어떻게 무너지는지를 구체적인 함수들로 확인한다. 먼저 최대·최소 정리의 두 가정 — 정의역의 컴팩트성과 함수의 연속성 — 이 각각 필수임을 본다.

<div class="example" markdown="1">

<ins id="ex5">**예시 5 (최대·최소 정리의 가정)**</ins> 정의역이 컴팩트가 아니면 최댓값·최솟값이 사라질 수 있다. 열린구간 $$(0, 1)$$ 위의 항등함수 $$f(x) = x$$는 연속이지만

$$\sup_{x \in (0,1)} x = 1, \qquad \inf_{x \in (0,1)} x = 0$$

이 모두 함숫값으로 도달되지 않아 최댓값도 최솟값도 없다. 닫혀 있으나 유계가 아닌 정의역에서도 마찬가지로, $$g : \mathbb{R} \to \mathbb{R}$$, $$g(x) = x$$는 최댓값이 없다.

함수가 연속이 아니어도 결론이 깨진다. 컴팩트한 정의역 $$[0, 1]$$ 위에서

$$h(x) = \begin{cases} x, & 0 \leq x < 1, \\ 0, & x = 1 \end{cases}$$

로 두면 $$h$$의 상한은 $$1$$이지만 $$x = 1$$에서의 불연속 때문에 어떤 점에서도 값 $$1$$을 취하지 않아 최댓값이 없다. 두 가정이 함께 있어야만 따름정리 2가 성립함이 드러난다.

</div>

다음으로 균등연속과 단순 연속의 차이를 가르는 표준 예시를 본다. 정의역이 컴팩트가 아닐 때 연속이지만 균등연속이 아닌 함수가 어떻게 나타나는지 보여 준다.

<div class="example" markdown="1">

<ins id="ex6">**예시 6 (연속이지만 균등연속이 아닌 함수)**</ins> $$f : (0, 1] \to \mathbb{R}$$, $$f(x) = 1/x$$를 보자. 점 $$x_n = \tfrac1n$$과 $$x_n' = \tfrac{1}{n+1}$$을 택하면

$$\lvert x_n - x_n' \rvert = \frac1n - \frac{1}{n+1} = \frac{1}{n(n+1)} \longrightarrow 0$$

이지만

$$\lvert f(x_n) - f(x_n') \rvert = \lvert n - (n+1) \rvert = 1$$

이 항상 $$1$$이다. 따라서 $$\varepsilon = 1$$에 대해서는 어떤 $$\delta > 0$$도 통하지 않아 $$f$$는 균등연속이 아니다. 원점 근처에서 함수가 한없이 가팔라져 공통의 $$\delta$$를 허용하지 않기 때문이다. 정의역 $$(0, 1]$$이 닫혀 있지 않아 — 따라서 컴팩트가 아니어서 — 정리 4의 가정이 충족되지 않는 것과 정확히 맞물린다.

같은 현상은 $$g : \mathbb{R} \to \mathbb{R}$$, $$g(x) = x^2$$에서도 나타난다. $$x_n = n + \tfrac1n$$, $$x_n' = n$$이면 $$\lvert x_n - x_n'\rvert = \tfrac1n \to 0$$이지만

$$\lvert g(x_n) - g(x_n') \rvert = \Bigl(n + \tfrac1n\Bigr)^2 - n^2 = 2 + \frac{1}{n^2} > 2$$

이어서 $$\varepsilon = 2$$가 좌절된다. 여기서는 정의역이 유계가 아니어서 컴팩트성이 깨진다.

</div>

반대로 정의역을 컴팩트하게 제한하면 정리 4가 균등연속을 보장한다. 같은 $$x^2$$이라도 닫힌구간 위에서는 사정이 달라진다.

<div class="example" markdown="1">

<ins id="ex7">**예시 7 (컴팩트 정의역에서의 균등연속)**</ins> $$f(x) = x^2$$를 닫힌구간 $$[0, R]$$로 제한하면 정리 4에 의해 균등연속이며, 이를 직접 확인할 수 있다. $$x, x' \in [0, R]$$에 대해

$$\begin{aligned}
\lvert f(x) - f(x') \rvert &= \lvert x^2 - x'^2 \rvert = \lvert x + x' \rvert \cdot \lvert x - x' \rvert \\
&\leq 2R \cdot \lvert x - x' \rvert
\end{aligned}$$

이므로, 주어진 $$\varepsilon > 0$$에 대해 $$\delta = \dfrac{\varepsilon}{2R}$$로 두면 $$\lvert x - x'\rvert < \delta$$일 때 $$\lvert f(x) - f(x')\rvert < \varepsilon$$이 모든 점에 공통으로 성립한다. $$\delta$$가 점 $$x$$와 무관하게 잡혔으므로 이는 정의 3의 균등연속이다. 인수 $$\lvert x + x'\rvert$$가 컴팩트 정의역에서 $$2R$$로 유계라는 점이 결정적이었다.

</div>

위 예시 7에서 본 부등식 $$\lvert f(x) - f(x')\rvert \leq 2R\,\lvert x - x'\rvert$$은 함숫값의 변화가 변수의 변화에 상수배로 묶이는 형태이다. 이런 조건은 균등연속을 자동으로 함의하는 유용한 충분조건이다.

<div class="definition" markdown="1">

<ins id="def8">**정의 8**</ins> $$f : X \to Y$$가 *립시츠<sub>Lipschitz</sub> 연속*이라는 것은, 어떤 상수 $$L \geq 0$$이 존재하여 모든 $$x, x' \in X$$에 대해

$$d_Y\bigl(f(x), f(x')\bigr) \leq L \cdot d_X(x, x')$$

이 성립하는 것이다. 이때 $$L$$을 *립시츠 상수<sub>Lipschitz constant</sub>*라 한다.

</div>

<div class="proposition" markdown="1">

<ins id="prop9">**명제 9**</ins> 립시츠 연속인 함수는 균등연속이다.

</div>

<details class="proof" markdown="1">
<summary>증명</summary>

$$L = 0$$이면 $$f$$는 상수함수여서 자명하므로 $$L > 0$$이라 하자. 주어진 $$\varepsilon > 0$$에 대해 $$\delta = \dfrac{\varepsilon}{L}$$로 두면, $$d_X(x, x') < \delta$$일 때

$$d_Y\bigl(f(x), f(x')\bigr) \leq L \cdot d_X(x, x') < L \cdot \frac{\varepsilon}{L} = \varepsilon$$

이다. 이 $$\delta$$는 $$x$$에 무관하게 선택되었으므로 $$f$$는 균등연속이다.

</details>

예시 7의 $$f(x) = x^2$$는 $$[0, R]$$ 위에서 립시츠 상수 $$2R$$로 립시츠 연속이며, 명제 9가 곧바로 그 균등연속을 준다. 그러나 립시츠 연속은 균등연속보다 진정으로 강한 조건이다. $$[0, 1]$$ 위의 $$f(x) = \sqrt{x}$$는 정리 4에 의해 균등연속이지만, 원점 근처에서

$$\frac{\lvert \sqrt{x} - \sqrt{0}\,\rvert}{\lvert x - 0\rvert} = \frac{1}{\sqrt{x}} \longrightarrow \infty$$

이어서 어떤 유한한 립시츠 상수로도 묶이지 않는다. 즉 립시츠 연속, 균등연속, 단순 연속은 갈수록 약해지는 세 단계의 조건이며, 컴팩트 정의역 위에서는 가운데 두 조건이 연속과 합쳐진다.

균등연속성은 연속함수의 적분가능성을 증명하는 데 핵심적으로 쓰여, 다음 글들에서 [§Riemann 적분](/ko/math/analysis/riemann_integral)의 기초가 된다. 한편 연속함수가 보존하는 또 하나의 성질인 연결성과, 그로부터 따라 나오는 중간값 정리는 [§연결성과 중간값 정리](/ko/math/analysis/connectedness)에서 다룬다.
