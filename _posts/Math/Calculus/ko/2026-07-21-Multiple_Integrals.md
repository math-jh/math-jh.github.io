---
title: "다중적분"
description: "여러 변수 함수의 이중·삼중적분을 리만 합으로 정의하고, 반복적분으로 계산하는 푸비니 정리를 다룬다. 야코비 행렬식을 통한 변수변환 공식과 극좌표 적분을 예로 든다."
excerpt: "이중적분, 푸비니 정리, 변수변환과 야코비 행렬식"

categories: [Math / Calculus]
permalink: /ko/math/calculus/multiple_integrals
sidebar: 
    nav: "calculus-ko"

header:
    overlay_image: /assets/images/Math/Calculus/Multiple_Integrals.png
    overlay_filter: 0.5

date: 2026-07-21
last_modified_at: 2026-07-21

weight: 17

published: false
---

[§정적분](/ko/math/calculus/definite_integral)이 구간 위의 누적이었다면, 다중적분은 평면이나 공간의 영역 위의 누적 — 부피, 질량, 평균 — 을 잰다. [§다변수함수와 편미분](/ko/math/calculus/partial_derivatives)의 함수들을 적분하는 이 도구로 미적분학의 한 변수 이론이 고차원으로 완성된다.

## 이중적분

<div class="definition" markdown="1">

<ins id="def1">**정의 1**</ins> 직사각형 $$R = [a,b]\times[c,d]$$ 위의 유계함수 $$f(x,y)$$에 대하여, $$R$$을 작은 직사각형들로 분할하고 각 조각 $$R_{ij}$$에서 표본점 $$(x_i^\ast, y_j^\ast)$$을 택해 만든 리만 합 $$\sum_{i,j} f(x_i^\ast, y_j^\ast)\,\Delta A_{ij}$$이 분할을 잘게 할 때 한 값으로 수렴하면, 그 값을 $$f$$의 *이중적분*이라 하고

$$\iint_R f(x,y)\,dA$$

로 적는다. $$f \geq 0$$이면 이는 곡면 $$z = f(x,y)$$ 아래의 부피이다.

</div>

연속함수는 이중적분가능하다. 일반적인 영역 $$D$$ 위의 적분은 $$D$$를 포함하는 직사각형에서 $$D$$ 밖을 $$0$$으로 둔 함수를 적분하여 정의한다.

## 푸비니 정리

이중적분의 실제 계산은 한 변수씩 차례로 적분하는 반복적분으로 환원된다.

<div class="proposition" markdown="1">

<ins id="thm2">**정리 2 (푸비니)**</ins> $$f$$가 $$R = [a,b]\times[c,d]$$에서 연속이면

$$\iint_R f\,dA = \int_a^b\!\left(\int_c^d f(x,y)\,dy\right)dx = \int_c^d\!\left(\int_a^b f(x,y)\,dx\right)dy$$

이다. 즉 적분 순서를 바꿀 수 있다.

</div>

이로써 다중적분이 [§미적분의 기본정리](/ko/math/calculus/fundamental_theorem_of_calculus)와 적분법으로 계산하는 한 변수 적분들의 연쇄로 환원된다. 일반 영역에서는 적분 구간이 다른 변수에 의존한다: 가령 $$D = \{(x,y) \mid a\leq x\leq b,\ g_1(x)\leq y\leq g_2(x)\}$$이면 $$\iint_D f = \int_a^b\int_{g_1(x)}^{g_2(x)} f\,dy\,dx$$이다.

## 변수변환

한 변수의 치환적분에 대응하는 것이 다변수의 변수변환이며, 길이 비율 $$g'$$의 자리에 야코비 행렬식이 들어간다.

<div class="proposition" markdown="1">

<ins id="thm3">**정리 3 (변수변환)**</ins> 일대일 미분가능 사상 $$(x,y) = T(u,v)$$가 영역 $$D'$$을 $$D$$로 보내면

$$\iint_D f(x,y)\,dA = \iint_{D'} f(T(u,v))\,\lvert \det J_T(u,v)\rvert\,du\,dv$$

이다. 여기서 $$J_T = \begin{pmatrix} \partial x/\partial u & \partial x/\partial v \\ \partial y/\partial u & \partial y/\partial v\end{pmatrix}$$는 $$T$$의 야코비 행렬이다.

</div>

<div class="example" markdown="1">

<ins id="ex4">**예시 4**</ins> 극좌표 $$x = r\cos\theta$$, $$y = r\sin\theta$$의 야코비 행렬식은 $$\det J = r$$이므로 $$dA = r\,dr\,d\theta$$이다. 이를 이용해 단위원판 $$D$$에서 $$\iint_D e^{-(x^2+y^2)}\,dA = \int_0^{2\pi}\!\int_0^1 e^{-r^2}\,r\,dr\,d\theta = 2\pi\cdot\tfrac12(1 - e^{-1}) = \pi(1 - e^{-1})$$이다.

</div>

야코비 행렬식이 넓이의 국소 확대율로 나타나는 것은 미분을 선형사상으로 보는 관점에서 자연스럽다. 다중적분과 변수변환의 엄밀한 이론, 그리고 미분을 선형근사로 다루는 관점은 해석학 [\[해석학\] §다변수 미분](/ko/math/analysis/multivariable_differentiation)에서 전개된다. 이로써 한 변수에서 시작한 미적분학이 다변수로 일관되게 확장된다.
