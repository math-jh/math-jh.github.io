---
title: "역함수 정리와 음함수 정리"
description: "연속미분가능 사상의 미분이 한 점에서 가역이면 그 점 근방에서 함수가 국소적으로 가역임을 보이는 역함수 정리를, 축약사상 원리를 이용해 증명한다. 그 따름정리로 음함수 정리를 끌어낸다."
excerpt: "역함수 정리, 축약사상, 음함수 정리"

categories: [Math / Analysis]
permalink: /ko/math/analysis/inverse_function_theorem
sidebar: 
    nav: "analysis-ko"

header:
    overlay_image: /assets/images/Math/Analysis/Inverse_Function_Theorem.png
    overlay_filter: 0.5

date: 2026-06-02
last_modified_at: 2026-06-02
weight: 20

published: false
---

[§다변수 미분](/ko/math/analysis/multivariable_differentiation)에서 미분을 선형사상 $$Df(a)$$로 보았다. 선형사상이 가역이면 그것이 근사하는 함수도 국소적으로 가역이리라 기대할 수 있다. 이 직관을 엄밀하게 만든 것이 역함수 정리이며, 다변수 미적분의 가장 깊은 정리 중 하나이다.

## 역함수 정리

<div class="proposition" markdown="1">

<ins id="thm1">**정리 1 (역함수 정리)**</ins> $$f : \mathbb{R}^n \to \mathbb{R}^n$$이 점 $$a$$ 근방에서 $$C^1$$이고 $$Df(a)$$가 가역이면, $$a$$의 어떤 근방에서 $$f$$는 그 상 위로의 일대일 대응이며, 그 역함수 $$f^{-1}$$도 $$C^1$$이고

$$D f^{-1}(f(a)) = \bigl(Df(a)\bigr)^{-1}$$

이다.

</div>

<details class="proof" markdown="1">
<summary>증명 (개요)</summary>

$$Df(a) = A$$를 합성으로 보정하여 $$A = I$$로 두어도 좋다. $$y$$를 고정하고 $$f(x) = y$$를 푸는 것은 사상

$$T_y(x) = x - \bigl(f(x) - y\bigr)$$

의 고정점을 찾는 것과 같다. $$DT_y(x) = I - Df(x)$$이고 $$Df$$가 $$a$$에서 $$I$$이며 연속이므로, $$a$$의 작은 근방에서 $$\lVert DT_y(x)\rVert \leq \tfrac12$$로 만들 수 있다. 그러면 평균값 부등식에 의해 $$T_y$$가 축약사상이고, 그 근방을 닫힌 공으로 잡으면 완비 거리공간 ([§거리공간, ⁋정의 4](/ko/math/analysis/metric_spaces#def4)) 위의 축약사상이 된다. 축약사상 원리 ([§미분방정식의 존재성과 유일성, ⁋정리 2](/ko/math/analysis/existence_uniqueness_ode#thm2))에 의해 각 $$y$$에 대해 유일한 고정점 $$x = f^{-1}(y)$$가 존재하므로 $$f$$가 국소적으로 일대일 대응이다. 역함수의 미분가능성과 $$Df^{-1} = (Df)^{-1}$$은 연쇄법칙을 $$f^{-1}\circ f = \mathrm{id}$$에 적용하여 얻는다.

</details>

가역성은 국소적임에 유의한다. $$Df(a)$$가 모든 점에서 가역이어도 $$f$$가 전역적으로 일대일일 필요는 없다 — 예컨대 복소평면을 $$\mathbb{R}^2$$로 본 $$f(x,y) = (e^x\cos y, e^x\sin y)$$는 모든 점에서 미분이 가역이지만 $$y$$에 대해 $$2\pi$$ 주기로 같은 값을 갖는다.

## 음함수 정리

역함수 정리의 직접적 귀결로, 방정식 $$F(x, y) = 0$$이 언제 $$y$$를 $$x$$의 함수로 국소적으로 푸는지를 알 수 있다.

<div class="proposition" markdown="1">

<ins id="thm2">**정리 2 (음함수 정리)**</ins> $$F : \mathbb{R}^n \times \mathbb{R}^m \to \mathbb{R}^m$$이 $$C^1$$이고 $$F(a, b) = 0$$이며, $$y$$에 대한 편미분 행렬 $$D_y F(a,b)$$가 가역이면, $$a$$의 근방에서 정의된 $$C^1$$ 함수 $$g$$가 유일하게 존재하여 $$g(a) = b$$이고 그 근방에서 $$F(x, g(x)) = 0$$이다.

</div>

<details class="proof" markdown="1">
<summary>증명</summary>

사상 $$\Phi(x, y) = (x, F(x, y))$$를 생각하면 $$D\Phi(a,b)$$는 $$D_yF(a,b)$$가 가역이므로 가역이다. 역함수 정리를 $$\Phi$$에 적용하면 국소적 역사상이 있고, 그 둘째 성분으로부터 $$F(x, y) = 0$$을 만족하는 $$y = g(x)$$를 얻는다.

</details>

<div class="example" markdown="1">

<ins id="ex3">**예시 3**</ins> 단위원 $$F(x,y) = x^2 + y^2 - 1 = 0$$에서 $$\partial F/\partial y = 2y$$이므로, $$y \neq 0$$인 점 근방에서는 $$y = g(x)$$로 풀린다 (실제로 $$y = \pm\sqrt{1 - x^2}$$). $$y = 0$$인 점 $$(\pm 1, 0)$$에서는 조건이 깨지고, 그곳에서 원은 수직 접선을 가져 $$y$$를 $$x$$의 함수로 쓸 수 없다.

</div>

역함수 정리의 증명에 쓰인 축약사상 원리는 해석학에서 존재·유일성을 보이는 가장 강력한 도구이다. 다음 글 [§미분방정식의 존재성과 유일성](/ko/math/analysis/existence_uniqueness_ode)에서 이를 정식으로 증명하고, 미분방정식의 해의 존재에 적용한다.
