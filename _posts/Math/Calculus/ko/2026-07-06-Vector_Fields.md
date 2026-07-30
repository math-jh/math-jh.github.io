---
title: "벡터장"
description: "공간의 각 점에 벡터를 대응시키는 벡터장을 도입하고, 기울기장과 보존장·퍼텐셜을 정의한다. 발산과 회전을 정의하고 그 의미를 살피며, curl(grad)=0·div(curl)=0과 보존장의 무회전성을 보인다."
excerpt: "벡터장과 기울기장, 보존장과 퍼텐셜, 발산과 회전, 미분 항등식"

categories: [Math / Calculus]
permalink: /ko/math/calculus/vector_fields
sidebar: 
    nav: "calculus-ko"

date: 2026-07-06
weight: 16
---

우리가 궁극적으로 다루고 싶은 것은 일반적인 함수 $\mathbb{R}^m\rightarrow\mathbb{R}^n$의 미적분학이다. 우리는 우선 [§곡선과 벡터함수](/ko/math/calculus/vector_functions)에서는 공역의 차원을, [§다변수함수와 편미분](/ko/math/calculus/partial_derivatives) 이후에서는 정의역의 차원을 올려 이를 준비했다. 이제 두 방향을 하나로 합쳐 정의역과 공역이 모두 여러 차원인 일반적인 경우를 시작한다. 특히 우리가 관심있는 경우는 정의역과 공역의 차원이 같은 $\mathbb{R}^n\rightarrow\mathbb{R}^n$이 가장 자연스러운 대상으로, 그럼 이 함수는 $n$차원 벡터를 받아 $n$차원 벡터를 내놓는 함수이다. 

## 벡터장

다만, 실질적으로는 우리가 사용할 수 있는 강력한 연산 중 하나인 외적이 $3$차원에서만 정의되므로, 우리는 대부분 $3$차원, 그리고 그 부분공간인 $2$차원에서 논의를 펼치게 된다. 어쨌든 다음의 정의들은 일반적인 차원에서도 말이 되는 것들이다. 

::: 정의 1
영역 $D \subseteq \mathbb{R}^n$의 각 점 $\mathbf{x}$에 벡터 $\mathbf{F}(\mathbf{x}) \in \mathbb{R}^n$을 대응시키는 함수 $\mathbf{F}\colon D \rightarrow \mathbb{R}^n$을 *벡터장<sub>vector field</sub>*이라 한다. 평면에서는 $\mathbf{F}(x,y) = (P(x,y), Q(x,y))$, 공간에서는 $\mathbf{F}(x,y,z) = (P, Q, R)$로 적고, 각 성분 $P, Q, R$가 $C^1$이면 $\mathbf{F}$를 $C^1$ 벡터장이라 한다.
:::

벡터장은 각 점에 그 점에서 출발하는 화살표를 꽂은 그림으로 이해하는 것이 가장 직관적이다. 가령, 유체의 흐름이라면 각 점에서의 유속을 표현한 것은 벡터장을 이룬다. 우리는 이미 이런 대상을 하나 알고 있다. ([§다변수함수와 편미분, ⁋정의 2](/ko/math/calculus/partial_derivatives#def2))

::: 정의 2
$C^1$ 스칼라함수 $f$의 기울기 $\nabla f = (\partial f/\partial x_1, \ldots, \partial f/\partial x_n)$로 주어지는 벡터장을 $f$의 *기울기장<sub>gradient field</sub>*이라 한다. 어떤 스칼라함수 $f$에 대해 $\mathbf{F} = \nabla f$로 쓸 수 있는 벡터장 $\mathbf{F}$를 *보존장<sub>conservative field</sub>*이라 하고, 그 $f$를 $\mathbf{F}$의 *potential<sub>퍼텐셜</sub>*이라 한다.
:::

## 발산과 회전

한편, 모든 벡터장이 보존장은 아니므로, 주어진 $\mathbf{F}$가 어떤 $f$의 기울기인지를 판정하는 것이 중심 문제가 된다. 이러한 판정에 쓰이는 연산이 다음의 정의에 있는 연산들로, 특히 $\curl$을 정의하기 위해서는 외적이 필요하므로 우리는 별수없이 $3$차원으로 내려와야 한다. 

::: 정의 3
$C^1$ 벡터장 $\mathbf{F} = (P, Q, R)$의 *발산<sub>divergence</sub>*은 스칼라장

$$\divergence \mathbf{F} = \nabla \cdot \mathbf{F} = \frac{\partial P}{\partial x} + \frac{\partial Q}{\partial y} + \frac{\partial R}{\partial z}$$

이고, *회전<sub>curl</sub>*은 벡터장

$$\curl \mathbf{F} = \nabla \times \mathbf{F} = \left(\frac{\partial R}{\partial y} - \frac{\partial Q}{\partial z},\ \frac{\partial P}{\partial z} - \frac{\partial R}{\partial x},\ \frac{\partial Q}{\partial x} - \frac{\partial P}{\partial y}\right)$$

이다. 
:::

위의 두 표기 $\nabla\cdot \mathbf{F}$와 $\nabla \times \mathbf{F}$는 형식적인 것으로, $\nabla = (\partial_x, \partial_y, \partial_z)$를 벡터로 보아 내적과 외적을 취한 것이다.

::: 예시 4
지름 방향으로 뻗는 $\mathbf{F}(x,y,z) = (x, y, z)$는 $\divergence \mathbf{F} = 1 + 1 + 1 = 3$으로 어디서나 양의 값을 갖는다. 이는 직관적으로 이 벡터장이 모든 점에서 <em-ko>나가는</em-ko> 방향임을 알려주는 계산이다. 한편 $\curl \mathbf{F} = 0$이다. 이는 $\mathbf{F}$가 회전하는 성분은 전혀 없이 순수하게 바깥으로 나가는 성분만으로 이루어졌다는 의미로 생각할 수 있다.

이와 대조되는 예시로, $z$축 둘레로 도는 $\mathbf{G}(x,y,z) = (-y, x, 0)$은 $\divergence \mathbf{G} = 0$이지만 $\curl \mathbf{G} = (0, 0, 2)$로 $z$축을 중심으로 도는 벡터장임을 알 수 있다.
:::

이제 이들이 어떻게 주어진 벡터장이 보존장인지를 판별하는지 살펴보자. 이를 위해서는 우선 다음이 필요하다. 

::: 명제 5
$C^2$ 함수 $f$와 $C^2$ 벡터장 $\mathbf{F}$에 대해

$$\curl(\nabla f) = 0, \qquad \divergence(\curl \mathbf{F}) = 0$$

이다.
:::

::: 증명
$\nabla f = (f_x, f_y, f_z)$의 회전의 첫 성분은 $\partial_y f_z - \partial_z f_y = f_{zy} - f_{yz}$인데, 이는 [§다변수함수와 편미분, ⁋정리 7](/ko/math/calculus/partial_derivatives#thm7)에 의해 $0$이며 나머지 두 성분도 같은 이유로 $0$이다. 또 $\curl \mathbf{F} = (R_y - Q_z,\ P_z - R_x,\ Q_x - P_y)$의 발산은

$$\partial_x(R_y - Q_z) + \partial_y(P_z - R_x) + \partial_z(Q_x - P_y) = (R_{yx} - R_{xy}) + (P_{zy} - P_{yz}) + (Q_{xz} - Q_{zx})$$

로 묶이고, 각 괄호에 다시 [§다변수함수와 편미분, ⁋정리 7](/ko/math/calculus/partial_derivatives#thm7)를 적용하여 $0$임을 보일 수 있다.
:::

첫 항등식은 보존장 판정의 필요조건을 준다. 만일 $\mathbf{F} = \nabla f$이면 $\curl \mathbf{F} = \curl(\nabla f) = 0$이므로, 회전이 $0$이 아닌 벡터장은 결코 보존장이 될 수 없기 때문이다. 즉 다음이 성립한다. 

::: 명제 6
보존장은 무회전이다. 즉 $C^1$ 벡터장 $\mathbf{F}$가 보존장이면 $\curl \mathbf{F} = 0$이다. 평면벡터장 $\mathbf{F} = (P, Q)$의 경우 이는 $\partial Q/\partial x = \partial P/\partial y$와 같다.
:::

단, 이 조건은 필요조건일 뿐이며, 그 역은 성립하지 않는다. 흥미로운 점은 이 역이 정의역의 모양에 달려 있다는 것으로, 만일 정의역에 "구멍"이 없으면 그 역도 성립하지만, 구멍이 있으면 무회전이면서도 보존장이 아닌 벡터장이 존재한다. 

::: 예시 7
$\mathbf{F} = (2xy,\ x^2 + z,\ y)$를 보자. 이것의 회전을 계산하면

$$\curl \mathbf{F} = (\partial_y y - \partial_z(x^2+z),\ \partial_z(2xy) - \partial_x y,\ \partial_x(x^2+z) - \partial_y(2xy)) = (1 - 1,\ 0,\ 2x - 2x) = 0$$

이라 보존장일 가능성이 있다. 따라서 $\mathbf{F}=\nabla f$를 만족하는 $f$를 찾을 수 있는지 살펴보자. 

이러한 $f$는 우선 첫째 성분에 의해 $f_x = 2xy$를 만족해야 하므로, $f = x^2 y + g(y, z)$의 꼴이어야 한다. 이제 이를 $y$에 대해 미분하면 $f_y = x^2 + g_y$이고, 만일 $\mathbf{F}$가 보존장이었다면 이 값이 $\mathbf{F}$의 둘째 성분 $x^2 + z$와 맞아야 하므로 $g_y = z$, 즉 $g = yz + h(z)$여야 한다. 이제 마지막으로 이를 다시 $f$에 넣고 $z$로 미분한 후 계수를 맞춰주면, $f_z = y + h'(z) = y$여야 하므로 $h' = 0$이다. 따라서 $f = x^2 y + yz$가 potential이 될 수 있으며, 실제로 $\mathbf{F} = \nabla f$이 성립한다. 
:::

---

**참고문헌**

**[Ste]** J. Stewart, *Calculus*, 8th ed., Cengage Learning, 2016.  
**[Kim]** 김홍종, *미적분학 1·2*, 제3개정판, 서울대학교출판문화원, 2020.
