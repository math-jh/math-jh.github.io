---
title: "다중적분"
description: "여러 변수 함수의 이중·삼중적분을 리만 합으로 정의하고, 반복적분으로 계산하는 푸비니 정리를 다룬다. 야코비 행렬식을 통한 변수변환과 극좌표 적분, 가우스 적분, 부피·질량 응용을 worked 예시로 본다."
excerpt: "이중적분, 푸비니 정리, 변수변환과 야코비 행렬식"

categories: [Math / Calculus]
permalink: /ko/math/calculus/multiple_integrals
sidebar: 
    nav: "calculus-ko"

header:
    overlay_image: /assets/images/Math/Calculus/Multiple_Integrals.png
    overlay_filter: 0.5

date: 2026-06-02
last_modified_at: 2026-06-02
weight: 17

published: false
---

[§정적분](/ko/math/calculus/definite_integral)이 구간 위의 누적이었다면, 다중적분은 평면이나 공간의 영역 위의 누적 — 부피, 질량, 평균, 무게중심 — 을 잰다. [§다변수함수와 편미분](/ko/math/calculus/partial_derivatives)의 함수들을 적분하는 이 도구로 미적분학의 한 변수 이론이 고차원으로 완성된다.

## 이중적분

<div class="definition" markdown="1">

<ins id="def1">**정의 1**</ins> 직사각형 $$R = [a,b]\times[c,d]$$ 위의 유계함수 $$f(x,y)$$에 대하여, $$R$$을 작은 직사각형 $$R_{ij}$$ (넓이 $$\Delta A_{ij}$$) 들로 분할하고 각 조각에서 표본점 $$(x_i^\ast, y_j^\ast)$$을 택해 만든 리만 합

$$\sum_{i,j} f(x_i^\ast, y_j^\ast)\,\Delta A_{ij}$$

이 분할을 잘게 할 때 한 값으로 수렴하면, 그 값을 $$f$$의 *이중적분*이라 하고 $$\displaystyle\iint_R f(x,y)\,dA$$로 적는다.

</div>

$$f \geq 0$$이면 이중적분은 밑면이 $$R$$이고 윗면이 곡면 $$z = f(x,y)$$인 입체의 부피이다. 한 변수 정적분이 넓이였던 것이 한 차원 올라간 셈이다. 리만 합의 각 항 $$f(x_i^\ast, y_j^\ast)\,\Delta A_{ij}$$은 밑면 넓이 $$\Delta A_{ij}$$에 높이 $$f(x_i^\ast, y_j^\ast)$$를 곱한 가느다란 기둥의 부피이고, 이 기둥들을 모아 입체를 근사한 뒤 분할을 무한히 잘게 하는 극한이 이중적분이다.

연속함수는 이중적분가능하며, 직사각형이 아닌 일반 영역 $$D$$ 위의 적분은 $$D$$를 포함하는 직사각형에서 $$D$$ 밖을 $$0$$으로 둔 함수를 적분하여 정의한다. 이렇게 확장해도 $$D$$의 경계가 매끄러운 곡선들로 이루어져 있으면 그 위에서 함수가 연속인 한 적분값은 잘 정의된다.

적분의 기본 성질도 한 변수의 경우와 똑같이 성립한다. 선형성으로 $$\iint_D (\alpha f + \beta g)\,dA = \alpha\iint_D f\,dA + \beta\iint_D g\,dA$$이고, 단조성으로 $$f \leq g$$이면 $$\iint_D f\,dA \leq \iint_D g\,dA$$이며, 영역가법성으로 $$D = D_1 \cup D_2$$가 겹치지 않는 두 조각의 합집합이면 $$\iint_D f\,dA = \iint_{D_1} f\,dA + \iint_{D_2} f\,dA$$이다. 특히 $$f \equiv 1$$을 넣으면 $$\iint_D dA$$가 영역 $$D$$의 넓이를 준다.

## 푸비니 정리

이중적분의 정의는 이차원 극한이라 직접 계산이 어렵다. 다행히 한 변수씩 차례로 적분하는 *반복적분*으로 환원된다.

<div class="proposition" markdown="1">

<ins id="thm2">**정리 2 (푸비니)**</ins> $$f$$가 $$R = [a,b]\times[c,d]$$에서 연속이면

$$\iint_R f\,dA = \int_a^b\!\left(\int_c^d f(x,y)\,dy\right)dx = \int_c^d\!\left(\int_a^b f(x,y)\,dx\right)dy$$

이다. 즉 적분 순서를 바꿀 수 있다.

</div>

안쪽 적분은 한 변수를 상수로 고정하고 다른 변수로 적분하는 보통의 정적분이므로, 다중적분이 [§미적분의 기본정리](/ko/math/calculus/fundamental_theorem_of_calculus)와 적분법으로 푸는 한 변수 적분들의 연쇄로 환원된다.

<div class="example" markdown="1">

<ins id="ex3">**예시 3**</ins> $$R = [0,1]\times[0,2]$$에서 $$\displaystyle\iint_R xy\,dA$$를 구하자. 푸비니로 안쪽 $$y$$ 적분에서 $$x$$를 상수로 보면

$$\begin{aligned}
\iint_R xy\,dA &= \int_0^1\!\left(\int_0^2 xy\,dy\right)dx \\
&= \int_0^1 x\Bigl[\tfrac{y^2}{2}\Bigr]_{y=0}^{y=2}\,dx \\
&= \int_0^1 2x\,dx = \bigl[x^2\bigr]_0^1 = 1
\end{aligned}$$

이다. 순서를 바꾸어 $$x$$부터 적분해도

$$\int_0^2\!\left(\int_0^1 xy\,dx\right)dy = \int_0^2 y\Bigl[\tfrac{x^2}{2}\Bigr]_0^1\,dy = \int_0^2 \tfrac{y}{2}\,dy = 1$$

로 같은 값이 나온다. 피적분함수가 $$f(x,y) = g(x)h(y)$$처럼 변수분리되고 영역이 직사각형이면, 이중적분은 두 한 변수 적분의 곱 $$\bigl(\int_a^b g\bigr)\bigl(\int_c^d h\bigr)$$으로 분해된다.

</div>

일반 영역에서는 적분 구간이 다른 변수에 의존한다. $$D = \{(x,y) \mid a\leq x\leq b,\ g_1(x)\leq y\leq g_2(x)\}$$이면 $$\displaystyle\iint_D f = \int_a^b\!\int_{g_1(x)}^{g_2(x)} f(x,y)\,dy\,dx$$이다.

<div class="example" markdown="1">

<ins id="ex4">**예시 4 (삼각형 영역)**</ins> $$D$$를 $$(0,0), (1,0), (1,1)$$을 꼭짓점으로 하는 삼각형, 곧 $$0 \leq x \leq 1$$, $$0 \leq y \leq x$$라 하면

$$\begin{aligned}
\iint_D (x + y)\,dA &= \int_0^1\!\int_0^x (x+y)\,dy\,dx \\
&= \int_0^1\Bigl[xy + \tfrac{y^2}{2}\Bigr]_{y=0}^{y=x} dx \\
&= \int_0^1\Bigl(x^2 + \tfrac{x^2}{2}\Bigr)dx = \int_0^1 \tfrac32 x^2\,dx = \frac12
\end{aligned}$$

이다. 영역의 모양에 따라 안쪽 적분의 끝값이 바깥 변수의 함수가 됨에 유의한다.

</div>

같은 영역을 $$y$$부터 적분하려면 영역을 $$y$$ 기준으로 다시 기술해야 한다. 삼각형 $$D$$는 $$0 \leq y \leq 1$$, $$y \leq x \leq 1$$로도 적히므로 $$\iint_D (x+y)\,dA = \int_0^1\!\int_y^1 (x+y)\,dx\,dy$$이고, 계산하면 역시 $$\tfrac12$$이다. 적분 순서를 어떻게 잡느냐는 답을 바꾸지 않지만, 한쪽 순서로는 안쪽 적분이 초등함수로 풀리는 반면 다른 순서로는 풀리지 않는 일이 흔하다. 가령 $$\int_0^1\!\int_x^1 e^{y^2}\,dy\,dx$$는 $$e^{y^2}$$의 부정적분이 초등함수가 아니라 안쪽부터 풀 수 없지만, 영역 $$\{0 \leq x \leq y \leq 1\}$$의 순서를 바꾸어 $$\int_0^1\!\int_0^y e^{y^2}\,dx\,dy = \int_0^1 y\,e^{y^2}\,dy = \tfrac12(e - 1)$$로 깔끔히 풀린다. 이처럼 *적분 순서 교환*은 단순한 형식 조작이 아니라 실용적인 계산 전략이다.

## 변수변환

한 변수의 치환적분에 대응하는 것이 다변수의 변수변환이며, 길이 비율 $$g'$$의 자리에 야코비 행렬식이 들어간다.

<div class="proposition" markdown="1">

<ins id="thm5">**정리 5 (변수변환)**</ins> 일대일 $$C^1$$ 사상 $$(x,y) = T(u,v)$$가 영역 $$D'$$을 $$D$$로 보내고 야코비 행렬식이 $$D'$$에서 $$0$$이 아니면

$$\iint_D f(x,y)\,dA = \iint_{D'} f(T(u,v))\,\lvert \det J_T(u,v)\rvert\,du\,dv$$

이다. 여기서 $$J_T = \begin{pmatrix} \partial x/\partial u & \partial x/\partial v \\ \partial y/\partial u & \partial y/\partial v\end{pmatrix}$$는 $$T$$의 야코비 행렬이다.

</div>

야코비 행렬식 $$\lvert\det J_T\rvert$$은 $$T$$가 넓이를 늘이는 국소 비율로, 한 변수에서 $$dx = g'(u)\,du$$의 $$\lvert g'\rvert$$에 해당한다. 직관적으로 보면, $$(u,v)$$ 평면의 작은 직사각형 $$[u, u+\Delta u]\times[v, v+\Delta v]$$은 $$T$$에 의해 $$(x,y)$$ 평면의 작은 평행사변형으로 옮겨지는데, 그 두 변은 근사적으로 $$T_u\,\Delta u$$와 $$T_v\,\Delta v$$ ($$T_u, T_v$$는 $$T$$의 편도함수 벡터) 이다. 두 벡터가 이루는 평행사변형의 넓이가 바로 $$\lvert\det J_T\rvert\,\Delta u\,\Delta v$$이므로, 넓이 원소는

$$dA = \lvert\det J_T(u,v)\rvert\,du\,dv$$

로 변환된다. 이 식을 리만 합에 대입해 극한을 취한 것이 정리 5이며, 절댓값을 붙이는 이유는 넓이가 항상 양수이기 때문이다 (한 변수의 치환적분에서 적분 구간의 방향이 부호를 흡수하던 것과 대비된다). 가장 흔한 변환이 극좌표이다.

<div class="example" markdown="1">

<ins id="ex6">**예시 6 (극좌표)**</ins> 극좌표 $$x = r\cos\theta$$, $$y = r\sin\theta$$의 야코비 행렬식은

$$\det J = \det\begin{pmatrix}\cos\theta & -r\sin\theta \\ \sin\theta & r\cos\theta\end{pmatrix} = r$$

이므로 $$dA = r\,dr\,d\theta$$이다. 이를 이용해 단위원판 $$D$$에서

$$\iint_D e^{-(x^2+y^2)}\,dA = \int_0^{2\pi}\!\int_0^1 e^{-r^2}\,r\,dr\,d\theta = 2\pi\cdot\tfrac12(1 - e^{-1}) = \pi(1 - e^{-1})$$

이다. 직교좌표로는 풀리지 않던 적분이 극좌표에서 $$r\,dr$$ 덕분에 깔끔히 풀린다.

</div>

<div class="example" markdown="1">

<ins id="ex7">**예시 7 (가우스 적분)**</ins> 한 변수로는 초등함수로 안 풀리는 $$I = \displaystyle\int_{-\infty}^{\infty} e^{-x^2}\,dx$$를 다중적분으로 구한다. 곱 $$I^2$$을 두 개의 독립 변수에 대한 적분으로 보아 하나로 묶으면

$$\begin{aligned}
I^2 &= \left(\int_{-\infty}^\infty e^{-x^2}\,dx\right)\!\left(\int_{-\infty}^\infty e^{-y^2}\,dy\right) \\
&= \iint_{\mathbb{R}^2} e^{-x^2}e^{-y^2}\,dA = \iint_{\mathbb{R}^2} e^{-(x^2+y^2)}\,dA
\end{aligned}$$

이고, 이를 극좌표로 바꾸면 $$x^2 + y^2 = r^2$$이라

$$\begin{aligned}
I^2 &= \int_0^{2\pi}\!\int_0^\infty e^{-r^2}\,r\,dr\,d\theta \\
&= \int_0^{2\pi}\!\Bigl[-\tfrac12 e^{-r^2}\Bigr]_{r=0}^{r=\infty}\,d\theta = \int_0^{2\pi}\tfrac12\,d\theta = \pi
\end{aligned}$$

이므로 $$I = \sqrt\pi$$이다. 차원을 하나 올려 회전대칭을 활용하는 이 기법이 가우스 적분의 고전적 풀이이다. 핵심은 직교좌표에서 풀리지 않던 안쪽 적분이 극좌표에서 생긴 여분의 인자 $$r$$ 덕분에 $$e^{-r^2}\,r$$의 부정적분 $$-\tfrac12 e^{-r^2}$$로 닫힌다는 데 있다.

</div>

## 삼중적분과 응용

삼중적분 $$\iiint_E f\,dV$$도 같은 방식으로 정의된다. 공간의 입체 $$E$$를 작은 상자 $$E_{ijk}$$ (부피 $$\Delta V_{ijk}$$) 로 분할하고 리만 합 $$\sum f\,\Delta V_{ijk}$$의 극한을 취하면 되며, 푸비니 정리에 의해 세 변수에 걸친 반복적분으로 환원된다. $$f \equiv 1$$이면 $$\iiint_E dV$$는 $$E$$의 부피, 일반적인 밀도 $$\rho(x,y,z)$$이면 $$\iiint_E \rho\,dV$$는 $$E$$의 질량을 준다.

<div class="example" markdown="1">

<ins id="ex8">**예시 8 (부피)**</ins> 평면 $$x + y + z = 1$$과 좌표평면들로 둘러싸인 사면체 $$E$$ ($$x, y, z \geq 0$$) 의 부피는 안쪽 $$z$$ 적분의 위끝이 $$z = 1 - x - y$$임에 주의하여

$$\begin{aligned}
\iiint_E dV &= \int_0^1\!\int_0^{1-x}\!\int_0^{1-x-y} dz\,dy\,dx \\
&= \int_0^1\!\int_0^{1-x}(1-x-y)\,dy\,dx \\
&= \int_0^1\Bigl[(1-x)y - \tfrac{y^2}{2}\Bigr]_{y=0}^{y=1-x}dx \\
&= \int_0^1 \frac{(1-x)^2}{2}\,dx = \Bigl[-\frac{(1-x)^3}{6}\Bigr]_0^1 = \frac16
\end{aligned}$$

이다. 안쪽부터 차례로 적분하며, 각 단계의 끝값이 바깥 변수에 의존한다.

</div>

<div class="example" markdown="1">

<ins id="ex9">**예시 9 (무게중심)**</ins> 밀도가 균일한 평판 $$D$$의 무게중심 $$(\bar x, \bar y)$$는 $$\bar x = \dfrac{1}{A}\iint_D x\,dA$$ ($$A$$는 넓이) 등으로 주어진다. 반원판 $$D = \{x^2 + y^2 \leq 1,\ y \geq 0\}$$이면 대칭성으로 $$\bar x = 0$$이고, 극좌표로

$$\iint_D y\,dA = \int_0^\pi\!\int_0^1 (r\sin\theta)\,r\,dr\,d\theta = \int_0^\pi \sin\theta\,d\theta\cdot\int_0^1 r^2\,dr = 2\cdot\frac13 = \frac23$$

이므로 $$\bar y = \dfrac{2/3}{\pi/2} = \dfrac{4}{3\pi}$$이다.

</div>

삼차원에서도 변수변환은 그대로 통하며, 구·원기둥 영역에서는 구면좌표와 원기둥좌표가 특히 유용하다. *원기둥좌표<sub>cylindrical coordinates</sub>* $$(r, \theta, z)$$는 평면의 극좌표에 높이 $$z$$를 더한 것으로, $$x = r\cos\theta$$, $$y = r\sin\theta$$, $$z = z$$이고 야코비 행렬식이 $$r$$이라 $$dV = r\,dr\,d\theta\,dz$$이다. *구면좌표<sub>spherical coordinates</sub>* $$(\rho, \phi, \theta)$$는 원점으로부터의 거리 $$\rho$$, 양의 $$z$$축과의 각 $$\phi$$, 방위각 $$\theta$$로 점을 나타내며

$$x = \rho\sin\phi\cos\theta, \quad y = \rho\sin\phi\sin\theta, \quad z = \rho\cos\phi$$

이다. 그 야코비 행렬식을 계산하면 $$\det J = \rho^2\sin\phi$$이므로 $$dV = \rho^2\sin\phi\,d\rho\,d\phi\,d\theta$$이다.

<div class="example" markdown="1">

<ins id="ex10">**예시 10 (공의 부피)**</ins> 반지름 $$R$$인 공 $$E = \{x^2 + y^2 + z^2 \leq R^2\}$$의 부피는 구면좌표에서 $$0 \leq \rho \leq R$$, $$0 \leq \phi \leq \pi$$, $$0 \leq \theta \leq 2\pi$$이므로

$$\begin{aligned}
\iiint_E dV &= \int_0^{2\pi}\!\int_0^\pi\!\int_0^R \rho^2\sin\phi\,d\rho\,d\phi\,d\theta \\
&= \left(\int_0^{2\pi} d\theta\right)\!\left(\int_0^\pi \sin\phi\,d\phi\right)\!\left(\int_0^R \rho^2\,d\rho\right) \\
&= 2\pi\cdot 2\cdot\frac{R^3}{3} = \frac{4}{3}\pi R^3
\end{aligned}$$

이다. 세 변수가 분리되어 세 한 변수 적분의 곱이 되는 것이 구면좌표의 위력이다.

</div>

<div class="example" markdown="1">

<ins id="ex11">**예시 11 (원기둥좌표)**</ins> 포물면 $$z = x^2 + y^2$$ 아래, 평면 $$z = 4$$ 위의 입체 $$E$$의 부피를 구하자. 원기둥좌표에서 $$z = r^2$$ 위, $$z = 4$$ 아래이고 $$r^2 \leq 4$$이므로 $$0 \leq r \leq 2$$, $$0 \leq \theta \leq 2\pi$$이다. 따라서

$$\begin{aligned}
\iiint_E dV &= \int_0^{2\pi}\!\int_0^2\!\int_{r^2}^4 r\,dz\,dr\,d\theta \\
&= \int_0^{2\pi}\!\int_0^2 (4 - r^2)\,r\,dr\,d\theta \\
&= 2\pi\int_0^2 (4r - r^3)\,dr = 2\pi\Bigl[2r^2 - \tfrac{r^4}{4}\Bigr]_0^2 = 2\pi\cdot 4 = 8\pi
\end{aligned}$$

이다. 회전대칭이 있는 입체에서는 원기둥좌표가 적분을 크게 줄여 준다.

</div>

## 예시와 계산

마지막으로 다중적분의 두 가지 전형적인 쓰임 — 함수의 평균과 적분 순서 교환 — 을 worked 예시로 본다. 영역 $$D$$ 위에서 함수 $$f$$의 *평균값<sub>average value</sub>*은 $$\dfrac{1}{\operatorname{area}(D)}\iint_D f\,dA$$로 정의되며, 한 변수 적분의 평균값을 다차원으로 옮긴 것이다.

<div class="example" markdown="1">

<ins id="ex12">**예시 12 (평균값)**</ins> 단위원판 $$D = \{x^2 + y^2 \leq 1\}$$ 위에서 $$f(x,y) = x^2 + y^2$$의 평균값을 구하자. $$\operatorname{area}(D) = \pi$$이고, 극좌표로

$$\iint_D (x^2 + y^2)\,dA = \int_0^{2\pi}\!\int_0^1 r^2\cdot r\,dr\,d\theta = 2\pi\int_0^1 r^3\,dr = 2\pi\cdot\frac14 = \frac{\pi}{2}$$

이므로 평균값은 $$\dfrac{1}{\pi}\cdot\dfrac{\pi}{2} = \dfrac12$$이다. 원판 위에서 중심으로부터의 거리 제곱의 평균이 $$\tfrac12$$임을 뜻한다.

</div>

<div class="example" markdown="1">

<ins id="ex13">**예시 13 (적분 순서 교환)**</ins> $$\displaystyle\int_0^1\!\int_{\sqrt{x}}^1 \sin(\pi y^3)\,dy\,dx$$를 구하자. 안쪽에서 $$\sin(\pi y^3)$$를 $$y$$로 적분하는 것은 초등함수로 불가능하므로 순서를 바꾼다. 영역은 $$0 \leq x \leq 1$$, $$\sqrt{x} \leq y \leq 1$$, 곧 $$0 \leq y \leq 1$$, $$0 \leq x \leq y^2$$이므로

$$\begin{aligned}
\int_0^1\!\int_{\sqrt{x}}^1 \sin(\pi y^3)\,dy\,dx &= \int_0^1\!\int_0^{y^2} \sin(\pi y^3)\,dx\,dy \\
&= \int_0^1 y^2\sin(\pi y^3)\,dy \\
&= \Bigl[-\frac{1}{3\pi}\cos(\pi y^3)\Bigr]_0^1 = \frac{2}{3\pi}
\end{aligned}$$

이다. 바깥 변수가 영역의 끝값으로 들어오면서 새로 생긴 인자 $$y^2$$가 안쪽 적분을 치환적분으로 닫아 준다.

</div>

야코비 행렬식이 넓이·부피의 국소 확대율로 나타나는 것은 미분을 선형사상으로 보는 관점에서 자연스러우며, 다중적분과 변수변환의 엄밀한 이론 — 적분가능성의 조건, 푸비니 정리의 가설, 변수변환 정리의 증명 — 은 해석학 [\[해석학\] §다변수 미분](/ko/math/analysis/multivariable_differentiation)에서 전개된다. 이로써 한 변수에서 시작한 미적분학이 다변수로 일관되게 확장된다.
