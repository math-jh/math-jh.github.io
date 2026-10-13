---
title: "고계 편도함수와 극값"
description: "고계 편도함수를 정의하고, 편미분의 순서가 바뀌어도 값이 같다는 Schwarz 정리를 증명하며 순서가 바뀌는 반례를 제시한다. 이를 이용해 2차 다변수 테일러 정리를 얻고, Hessian 행렬의 부호로 임계점이 극대·극소·안장점 중 어느 것인지 판정하는 방법과 판정이 되지 않는 경우를 다룬다."
excerpt: "편미분의 순서교환, 2차 테일러 정리, Hessian 판정"

categories: [Math / Analysis]
permalink: /ko/math/analysis/higher_derivatives_and_extrema
sidebar: 
    nav: "analysis-ko"

date: 2026-10-13
weight: 26

published: false

---

[§다변수 미분, ⁋정의 1](/ko/math/analysis/multivariable_differentiation#def1)에서 다변수함수의 미분을 일차근사로 정의하고 [§다변수 미분, ⁋정리 5](/ko/math/analysis/multivariable_differentiation#thm5)에서 편도함수가 연속이면 미분가능함을 보았다. 일변수에서 $f'(a)=0$인 점의 성격을 $f''(a)$의 부호가 결정하듯, 다변수에서 극값을 판정하려면 이계 편도함수가 필요하다. 이 글에서는 고계 편도함수를 정의하고, 이계 편도함수들이 이루는 Hessian 행렬이 $f$의 이차 근사를 주도록 테일러 정리를 확장한 뒤, 이를 극값 판정에 적용한다. 그 과정에서 편미분을 취하는 순서가 결과에 영향을 주는지가 먼저 문제가 된다.

## 고계 편도함수

$U\subseteq\mathbb{R}^n$이 열린집합이고 $f:U\rightarrow\mathbb{R}$라 하자. $f$의 편도함수 $\partial_j f=\partial f/\partial x_j$가 $U$ 위에서 존재하면 이는 다시 $U$ 위의 함수이므로 편미분을 한 번 더 취할 수 있다.

::: 정의 1
$\partial_j f$의 $x_i$에 대한 편도함수를

$$\partial_i\partial_j f=\frac{\partial^2 f}{\partial x_i\partial x_j}=\frac{\partial}{\partial x_i}\left(\frac{\partial f}{\partial x_j}\right)$$

로 적고 *이계 편도함수<sub>second-order partial derivative</sub>*라 한다. 같은 방식으로 $k$계 편도함수 $\partial_{i_1}\cdots\partial_{i_k}f$를 귀납적으로 정의한다. 모든 $k$계 이하의 편도함수가 존재하고 연속일 때 $f$를 *$C^k$ 함수*라 하고, 모든 $k$에 대해 $C^k$이면 *$C^\infty$ 함수*라 한다. $f$가 $C^2$일 때 $a\in U$에서 이계 편도함수들을 모은 $n\times n$ 행렬

$$H_f(a)=\bigl(\partial_i\partial_j f(a)\bigr)_{i,j=1}^n$$

을 $f$의 $a$에서의 *Hessian 행렬*이라 한다.
:::

이 글에서 $\partial_i\partial_j$는 $j$번째 변수로 먼저 미분하고 $i$번째 변수로 나중에 미분하는 것을 뜻한다. 이 순서가 의미를 가지려면 $\partial_i\partial_j f$와 $\partial_j\partial_i f$가 일반적으로 달라질 수 있어야 하는데, 실제로 그런 함수가 존재한다.

::: 예시 2 (편미분의 순서가 바뀌는 함수)
$\mathbb{R}^2$ 위의 함수

$$f(x,y)=\begin{cases}\frac{xy(x^2-y^2)}{x^2+y^2}, & (x,y)\neq(0,0),\\[1ex] 0, & (x,y)=(0,0)\end{cases}$$

를 생각하자. $y\neq 0$이면

$$\frac{f(h,y)-f(0,y)}{h}=\frac{y(h^2-y^2)}{h^2+y^2}\rightarrow -y\qquad(h\rightarrow 0)$$

이므로 $\partial_x f(0,y)=-y$이고, $y=0$일 때는 $f(h,0)=0$이어서 $\partial_x f(0,0)=0=-y$이다. 따라서 $\partial_x f(0,y)=-y$가 모든 $y$에 대해 성립한다. 같은 방식으로 $\partial_y f(x,0)=x$를 얻는다. 그러므로

$$\partial_y\partial_x f(0,0)=\frac{d}{\dd{y}}\bigl(\partial_x f(0,y)\bigr)\Big\vert_{y=0}=-1,\qquad \partial_x\partial_y f(0,0)=\frac{d}{\dd{x}}\bigl(\partial_y f(x,0)\bigr)\Big\vert_{x=0}=1$$

이고 두 혼합 편도함수의 값이 다르다. 원점이 아닌 점에서는

$$\partial_x\partial_y f(x,y)=\partial_y\partial_x f(x,y)=\frac{(x^2-y^2)(x^4+10x^2y^2+y^4)}{(x^2+y^2)^3}$$

인데, 이 식은 $x$축 위($y=0$)에서 $1$, $y$축 위($x=0$)에서 $-1$이므로 원점에서 연속이 아니다. 아래 [정리 3](#thm3)의 가정이 깨지는 곳이 바로 이 불연속이다.
:::

## 편미분의 순서교환

혼합 편도함수가 연속이라는 가정이 있으면 [예시 2](#ex2)와 같은 일이 일어나지 않는다. 아래 정리는 연속성을 한 혼합 편도함수에 대해서만, 그것도 한 점에서만 요구하는 형태로 적는다.

::: 정리 3 (Schwarz 정리)
$U\subseteq\mathbb{R}^n$이 열린집합이고 $i\neq j$라 하자. $f:U\rightarrow\mathbb{R}$에 대하여 $\partial_i f$, $\partial_j f$, $\partial_j\partial_i f$가 $U$ 위에서 존재하고 $\partial_j\partial_i f$가 $a\in U$에서 연속이면, $\partial_i\partial_j f(a)$가 존재하고

$$\partial_i\partial_j f(a)=\partial_j\partial_i f(a)$$

이다.
:::

::: 증명
$x_i, x_j$ 이외의 좌표는 $a$의 값으로 고정하고 $x=x_i$, $y=x_j$로 적으면, $a=(a_1,a_2)$에 대하여 $\partial_x f$, $\partial_y f$, $\partial_y\partial_x f$가 $(a_1,a_2)$를 포함하는 어떤 열린 직사각형 $R$ 위에서 존재하는 두 변수의 함수 $f(x,y)$를 다루는 것이다. $\varepsilon>0$이 주어졌다고 하자. $\partial_y\partial_x f$가 $a$에서 연속이므로, $R$에 포함되는 어떤 $\delta>0$이 있어 $\lvert x-a_1\rvert<\delta$, $\lvert y-a_2\rvert<\delta$이면

$$\lvert \partial_y\partial_x f(x,y)-\partial_y\partial_x f(a)\rvert<\varepsilon \tag{1}$$

이다. $0<\lvert h\rvert<\delta$, $0<\lvert k\rvert<\delta$에 대하여 이중 차분

$$\Delta(h,k)=f(a_1+h,a_2+k)-f(a_1+h,a_2)-f(a_1,a_2+k)+f(a_1,a_2)$$

를 두 방식으로 계산한다. 먼저 $u(t)=f(t,a_2+k)-f(t,a_2)$라 하면 $\Delta(h,k)=u(a_1+h)-u(a_1)$이고, $\partial_x f$가 존재하므로 $u$는 미분가능하며 $u'(t)=\partial_x f(t,a_2+k)-\partial_x f(t,a_2)$이다. [§평균값 정리와 테일러 정리, ⁋정리 3](/ko/math/analysis/mean_value_theorem#thm3)을 적용하면 $a_1$과 $a_1+h$ 사이의 어떤 $\xi$에 대하여

$$\Delta(h,k)=h\bigl(\partial_x f(\xi,a_2+k)-\partial_x f(\xi,a_2)\bigr)$$

이다. 이제 $s\mapsto\partial_x f(\xi,s)$는 $\partial_y\partial_x f$가 존재하므로 미분가능하고, 도함수는 $\partial_y\partial_x f(\xi,s)$이다. [§평균값 정리와 테일러 정리, ⁋정리 3](/ko/math/analysis/mean_value_theorem#thm3)을 한 번 더 적용하면 $a_2$와 $a_2+k$ 사이의 어떤 $\eta$에 대하여

$$\frac{\Delta(h,k)}{hk}=\partial_y\partial_x f(\xi,\eta)$$

이고, $(\xi,\eta)$가 $a$로부터 각 좌표에서 $\delta$ 이내에 있으므로 (1)에 의하여

$$\left\lvert\frac{\Delta(h,k)}{hk}-\partial_y\partial_x f(a)\right\rvert<\varepsilon \tag{2}$$

이다. 다른 한편 $h$를 고정하고 $k\rightarrow 0$으로 보내면, $\partial_y f$가 $(a_1+h,a_2)$와 $(a_1,a_2)$에서 존재하므로

$$\frac{\Delta(h,k)}{k}\rightarrow \partial_y f(a_1+h,a_2)-\partial_y f(a_1,a_2)$$

이다. (2)에서 $k\rightarrow 0$으로 극한을 취하면 부등호가 $\le$로 약해지긴 하지만, 모든 $0<\lvert h\rvert<\delta$에 대하여

$$\left\lvert\frac{\partial_y f(a_1+h,a_2)-\partial_y f(a_1,a_2)}{h}-\partial_y\partial_x f(a)\right\rvert\le\varepsilon$$

을 얻는다. $\varepsilon$은 임의였으므로 좌변의 차분비는 $h\rightarrow 0$일 때 $\partial_y\partial_x f(a)$로 수렴한다. 이 극한이 정의상 $\partial_x\partial_y f(a)$이므로 증명이 끝난다.
:::

[예시 2](#ex2)에서는 $\partial_y\partial_x f$가 원점에서 불연속이어서 이 정리를 쓸 수 없고, 실제로 결론도 성립하지 않았다. 반대로 $f$가 $C^2$이면 모든 $i\neq j$에 대해 두 혼합 편도함수가 모두 연속이므로 [정리 3](#thm3)이 적용되어 Hessian 행렬 $H_f(a)$는 symmetric matrix가 된다. 더 높은 계수에서도 같은 결론이 성립한다.

::: 따름정리 4
$f$가 $U$ 위의 $C^k$ 함수이면, $k$계 이하의 편도함수는 미분하는 변수의 순서에 의존하지 않는다. 즉 $\{1,\dots,k\}$의 임의의 순열 $\sigma$에 대하여 $\partial_{i_1}\cdots\partial_{i_k}f=\partial_{i_{\sigma(1)}}\cdots\partial_{i_{\sigma(k)}}f$이다.
:::

::: 증명
임의의 순열은 이웃한 두 자리의 교환의 합성이다. 이웃한 두 미분 $\partial_{i_m}\partial_{i_{m+1}}$을 교환하는 것은, 그 안쪽의 $k-m-1$번 미분을 한 함수 $g=\partial_{i_{m+2}}\cdots\partial_{i_k}f$가 $C^2$이므로 [정리 3](#thm3)에 의해 $\partial_{i_m}\partial_{i_{m+1}}g=\partial_{i_{m+1}}\partial_{i_m}g$로 허용되고, 바깥쪽 미분은 양변에 똑같이 적용된다.
:::

## 2차 테일러 정리

[§평균값 정리와 테일러 정리, ⁋정리 9](/ko/math/analysis/mean_value_theorem#thm9)를 선분 위로 제한한 함수에 적용하면 다변수 테일러 정리를 얻는다. 이때 이계 편도함수의 대칭성이 쓰여 식이 이차형식 꼴로 정리된다.

::: 정리 5 (2차 테일러 정리)
$f$가 열린집합 $U\subseteq\mathbb{R}^n$ 위의 $C^2$ 함수이고, 선분 $\{a+th: 0\le t\le 1\}$이 $U$에 포함된다고 하자. 그러면 어떤 $\theta\in(0,1)$이 있어

$$f(a+h)=f(a)+\sum_{i=1}^n\partial_i f(a)h_i+\frac12\sum_{i,j=1}^n\partial_i\partial_j f(a+\theta h)h_ih_j$$

이다. 또한 $a\in U$에서 $h\rightarrow 0$일 때

$$f(a+h)=f(a)+\sum_{i=1}^n\partial_i f(a)h_i+\frac12\sum_{i,j=1}^n\partial_i\partial_j f(a)h_ih_j+o(\lVert h\rVert^2)$$

이다.
:::

::: 증명
$\varphi(t)=f(a+th)$라 하자. $C^1$ 함수는 미분가능하므로([§다변수 미분, ⁋정리 5](/ko/math/analysis/multivariable_differentiation#thm5)) [§다변수 미분, ⁋정리 7](/ko/math/analysis/multivariable_differentiation#thm7)에 의하여 $\varphi'(t)=\sum_i\partial_i f(a+th)h_i$이다. 각 $\partial_i f$도 $C^1$이므로 연쇄법칙을 다시 적용하면

$$\varphi''(t)=\sum_{i,j=1}^n\partial_j\partial_i f(a+th)h_ih_j$$

이고, 이는 $f$가 $C^2$이므로 연속이다. 일변수 [§평균값 정리와 테일러 정리, ⁋정리 9](/ko/math/analysis/mean_value_theorem#thm9)의 Lagrange 나머지 꼴에 의하여 $\varphi(1)=\varphi(0)+\varphi'(0)+\varphi''(\theta)/2$인 $\theta\in(0,1)$이 존재한다. 이를 풀어 쓰면 첫째 식이다. 이때 $\partial_j\partial_i f=\partial_i\partial_j f$는 [정리 3](#thm3)에 의한 것이다.

둘째 식은 첫째 식에서 얻는다. $\varepsilon>0$이 주어졌을 때 이계 편도함수들이 $a$에서 연속이므로 $\lVert h\rVert<\delta$이면 모든 $i,j$에 대하여 $\lvert\partial_i\partial_j f(a+\theta h)-\partial_i\partial_j f(a)\rvert<\varepsilon$이 되는 $\delta>0$이 있다. $\lvert h_i\rvert\le\lVert h\rVert$이므로 첫째 식과 둘째 식의 차는

$$\left\lvert\frac12\sum_{i,j}\bigl(\partial_i\partial_j f(a+\theta h)-\partial_i\partial_j f(a)\bigr)h_ih_j\right\rvert\le\frac{n^2\varepsilon}{2}\lVert h\rVert^2$$

이하이다. $\varepsilon$이 임의이므로 나머지는 $o(\lVert h\rVert^2)$이다.
:::

이차 항 $\sum_{i,j}\partial_i\partial_j f(a)h_ih_j$는 Hessian 행렬이 정하는 이차형식이며, 이를 $Q_a(h)$로 적는다. $a$가 아래에서 보듯 $\nabla f(a)=0$인 점이면 일차 항이 사라지므로 $f(a+h)-f(a)$의 거동은 $Q_a(h)$가 결정한다.

## 이차형식의 부호

symmetric matrix $A$와 그 이차형식 $Q(h)=\sum_{i,j}A_{ij}h_ih_j$가 *positive definite*라는 것은 모든 $h\neq 0$에 대하여 $Q(h)>0$인 것이고, *negative definite*라는 것은 모든 $h\neq 0$에 대하여 $Q(h)<0$인 것이며, *indefinite*라는 것은 $Q$가 양의 값과 음의 값을 모두 갖는 것이다. 어느 경우도 아닌 것은 $Q\ge 0$ 또는 $Q\le 0$이면서 $Q(h)=0$인 $h\neq 0$이 있는 경우이다.

일반적인 $n$에 대한 판정은 선형대수학의 결과이다. 실수 symmetric matrix는 [\[선형대수학\] §스펙트럼 정리, ⁋정리 5](/ko/math/linear_algebra/spectral_theorem#thm5)에 의하여 orthogonal basis로 대각화되므로 $Q$는 고윳값 $\lambda_1,\dots,\lambda_n$에 대해 $\sum\lambda_ia_i^2$ 꼴이 되고, 따라서 positive definite인 것은 모든 고윳값이 양수인 것, negative definite인 것은 모든 고윳값이 음수인 것, indefinite인 것은 양의 고윳값과 음의 고윳값이 모두 있는 것과 동치이다. 부호를 이루는 양·음·영의 개수가 기저의 선택에 의존하지 않는다는 것이 [\[선형대수학\] §이차형식과 실베스터 관성법칙, ⁋정리 3](/ko/math/linear_algebra/quadratic_forms#thm3)의 내용이며, 그래서 이 판정은 어떤 좌표에서 계산해도 같은 결과를 준다. 고윳값을 구하지 않고 leading principal minor만으로도 판정할 수 있다. $A$의 왼쪽 위 $k\times k$ 부분행렬의 행렬식을 $\Delta_k$라 하면, $A$가 positive definite인 것은 $\Delta_1,\dots,\Delta_n$이 모두 양수인 것과 동치이고, negative definite인 것은 모든 $k$에 대해 $(-1)^k\Delta_k>0$인 것과 동치이다 (Sylvester 판정법).

실제 문제는 대부분 $n=2$이므로 이 경우를 직접 확인해 둔다.

::: 명제 6
symmetric matrix $A=\begin{pmatrix}a&b\\b&c\end{pmatrix}$와 $\Delta=ac-b^2$에 대하여 다음이 성립한다.

1. $\Delta>0$이고 $a>0$이면 positive definite이고, $\Delta>0$이고 $a<0$이면 negative definite이다.
2. $\Delta<0$이면 indefinite이다.
3. $\Delta=0$이면 $Q\ge 0$ 또는 $Q\le 0$이고 $Q(h)=0$인 $h\neq 0$이 있다. 즉 definite도 indefinite도 아니다.
:::

::: 증명
$a\neq 0$이면 제곱완성에 의하여

$$Q(h)=ah_1^2+2bh_1h_2+ch_2^2=a\left(h_1+\frac ba h_2\right)^2+\frac{\Delta}{a}h_2^2 \tag{3}$$

이다. $\Delta>0$이면 $ac>b^2\ge 0$이므로 $a\neq 0$이고 $a$와 $\Delta/a$의 부호가 같다. 따라서 $h\neq 0$일 때 (3)의 두 항은 모두 $a$와 같은 부호이거나 $0$이고, 둘 다 $0$이면 $h_2=0$, 이어서 $h_1=0$이므로 $h=0$이다. 이것이 1이다. $\Delta<0$일 때 $a\neq 0$이면 (3)의 두 계수 $a$, $\Delta/a$가 반대 부호이므로 $Q$는 양·음의 값을 모두 갖는다. $a=0$이면 $\Delta=-b^2<0$에서 $b\neq 0$이고 $Q(h_1,1)=2bh_1+c$가 $h_1$에 따라 양·음의 값을 모두 가진다. 이것이 2이다. $\Delta=0$이고 $a\neq 0$이면 (3)에서 $Q(h)=a(h_1+(b/a)h_2)^2$이 $a$의 부호를 따르며 $h=(-b,a)\neq 0$에서 $0$이다. $\Delta=0$이고 $a=0$이면 $b=0$이어서 $Q(h)=ch_2^2$이고 $h=(1,0)$에서 $0$이다. 이것이 3이다.
:::

## 극값의 판정

$f$가 $a$에서 *극솟값<sub>local minimum</sub>*을 가진다는 것은 $a$ 근방의 모든 $x$에 대하여 $f(x)\ge f(a)$인 것이고, 엄격한 부등호가 $x\neq a$에서 성립하면 *strict*하다고 한다. 극댓값도 같고 이 둘을 극값이라 부른다. $a$가 극값이고 $f$의 편도함수가 존재하면 각 좌표축 방향으로 제한한 일변수함수 $t\mapsto f(a+te_i)$가 $t=0$에서 극값을 가지므로 [§미분, ⁋명제 5](/ko/math/analysis/differentiation#prop5)에 의해 그 도함수 $\partial_i f(a)$는 $0$이다. 따라서 $\nabla f(a)=0$이며, 이 조건을 만족하는 점을 *critical point*라 한다. 극값은 critical point 중에서만 찾으면 되지만, 그 역은 성립하지 않는다. $f(x,y)=x^2-y^2$의 원점이 그 예이다. 아래 정리는 이차 항으로 둘을 구분한다.

::: 정리 7 (이계 도함수 판정법)
$f$가 열린집합 $U\subseteq\mathbb{R}^n$ 위의 $C^2$ 함수이고 $a\in U$가 critical point라 하자.

1. $H_f(a)$가 positive definite이면 $f$는 $a$에서 strict 극솟값을 가진다. $H_f(a)$가 negative definite이면 strict 극댓값을 가진다.
2. $H_f(a)$가 indefinite이면 $a$는 극값이 아니다. 이러한 점을 *saddle point<sub>안장점</sub>*이라 한다.
3. $f$가 $a$에서 극솟값을 가지면 $H_f(a)$는 $Q_a\ge 0$이다. 극댓값이면 $Q_a\le 0$이다.
:::

::: 증명
$\nabla f(a)=0$이므로 [정리 5](#thm5)의 둘째 식은 $f(a+h)-f(a)=Q_a(h)/2+r(h)$, $r(h)=o(\lVert h\rVert^2)$가 된다.

1. 단위구면 $S=\{\lVert u\rVert=1\}$는 컴팩트하고 $Q_a$는 연속이므로 ([§컴팩트성, ⁋정리 7](/ko/math/analysis/compactness#thm7), [§연속함수의 성질, ⁋따름정리 2](/ko/math/analysis/continuous_functions#cor2)) $S$ 위에서 최솟값 $m$을 갖고, positive definite이므로 $m>0$이다. $Q_a$는 이차 동차이므로 모든 $h$에 대해 $Q_a(h)\ge m\lVert h\rVert^2$이다. $\varepsilon=m/4$로 잡으면, $\lVert h\rVert<\delta$일 때 $\lvert r(h)\rvert\le\varepsilon\lVert h\rVert^2$인 $\delta>0$이 있고, 이때 $h\neq 0$이면 $f(a+h)-f(a)\ge(m/2-m/4)\lVert h\rVert^2>0$이다. negative definite인 경우는 $-f$에 적용하면 된다. 여기서 $\varepsilon$을 $m$의 절반보다 작게 잡는 것이 핵심이다. $Q_a$가 주는 이득 $m/2$를 나머지의 상한이 넘지 못해야 하기 때문이다.
2. $Q_a(u)>0$, $Q_a(v)<0$인 $u,v$를 잡는다. $f(a+tu)-f(a)=t^2\bigl(Q_a(u)/2+r(tu)/t^2\bigr)$에서 $r(tu)/t^2\rightarrow 0$이므로 $\lvert t\rvert$가 충분히 작고 $t\neq 0$이면 괄호 안은 양수이다. $v$에 대해서는 음수이다. 따라서 $a$의 임의 근방에 $f(x)>f(a)$인 점과 $f(x)<f(a)$인 점이 모두 있다.
3. 어떤 $u$에 대해 $Q_a(u)<0$이면 2와 같은 계산으로 작은 $t\neq 0$에서 $f(a+tu)<f(a)$가 되어 극솟값이라는 가정에 모순이다. 극댓값은 $-f$에 적용한다.
:::

$n=2$이고 $\nabla f(a)=0$이면 [명제 6](#prop6)을 이용하여 판정을 $D=\partial_x^2 f\cdot\partial_y^2 f-(\partial_x\partial_y f)^2$ (Hessian의 행렬식)으로 쓸 수 있다. $D>0$이고 $\partial_x^2 f(a)>0$이면 극솟값, $D>0$이고 $\partial_x^2 f(a)<0$이면 극댓값, $D<0$이면 saddle point이다. $D>0$이면 $\partial_x^2 f$와 $\partial_y^2 f$의 부호가 같으므로 둘 중 하나로 확인해도 된다.

가령 $f(x,y)=x^3-3xy+y^3$에서 $\partial_xf=3x^2-3y$, $\partial_yf=3y^2-3x$이므로 critical point는 $y=x^2$, $x=y^2$에서 $x^4=x$를 풀어 $(0,0)$과 $(1,1)$이다. Hessian은 $\begin{pmatrix}6x&-3\\-3&6y\end{pmatrix}$이므로 $(0,0)$에서 $D=-9<0$이어서 saddle point이고, $(1,1)$에서는 $D=27>0$, $\partial_x^2f=6>0$이어서 극솟값 $f(1,1)=-1$을 가진다. 이 극솟값은 최솟값이 아니다. $f(x,x)=2x^3-3x^2$이 $x\rightarrow-\infty$에서 $-\infty$로 가기 때문이다. 이 판정법이 알려주는 것은 critical point 근방의 거동뿐이다.

## 판정이 되지 않는 경우

[정리 7](#thm7)의 1과 2는 충분조건이고, 3은 필요조건이다. 따라서 $H_f(a)$가 definite도 indefinite도 아닌 경우, 즉 $Q_a\ge 0$이면서 $Q_a(h)=0$인 $h\neq 0$이 있는 경우에는 이 판정법만으로 결론을 낼 수 없다. 이차 항이 사라지는 방향에서는 삼차 이상의 항이 거동을 결정하기 때문이다.

::: 예시 8 (같은 Hessian, 다른 결과)
$f(x,y)=x^4+y^4$, $g(x,y)=-x^4-y^4$, $h(x,y)=x^2+y^3$의 원점은 모두 critical point이다. $H_f(0)=H_g(0)=0$이고 $H_h(0)=\begin{pmatrix}2&0\\0&0\end{pmatrix}$로 모두 definite가 아닌 semidefinite이지만, 결과는 서로 다르다. $f$는 원점 밖에서 $f>0=f(0)$이므로 strict 극솟값을 가지고, $g$는 마찬가지로 strict 극댓값을 가진다. $h$는 $h(0,y)=y^3$이 $y>0$에서 양수, $y<0$에서 음수이므로 극값이 아니다. 같은 Hessian $\diag(2,0)$을 갖는 $x^2+y^4$는 극솟값을 갖는다는 점에서 $h$와 대비된다.
:::

semidefinite인 경우에 흔히 하는 실수는 방향마다 확인해 보고 결론을 내리는 것이다. 원점을 지나는 모든 직선에 제한했을 때 극솟값이 되어도 원점이 극솟값이라는 보장은 없다.

::: 예시 9 (모든 직선 위에서 극소이나 극솟값이 아닌 점)
$f(x,y)=(y-x^2)(y-2x^2)=y^2-3x^2y+2x^4$는 $\nabla f(0)=0$이고 $H_f(0)=\begin{pmatrix}0&0\\0&2\end{pmatrix}$이다. 직선 $y=mx$ ($m\neq 0$)에 제한하면 $f=x^2(m-x)(m-2x)$이고 $x\neq 0$이 작을 때 $m^2x^2$ 근처의 양수이며, $y=0$에서는 $f=2x^4>0$, $x=0$에서는 $f=y^2>0$이다. 따라서 원점을 지나는 모든 직선 위에서 $f$는 원점에서 strict 극솟값을 갖는다. 그러나 포물선 $y=3x^2/2$ 위에서는 $f(x,3x^2/2)=(x^2/2)(-x^2/2)=-x^4/4<0$이므로 원점은 $f$의 극솟값이 아니다.
:::

이 예시에서 $f$가 음수가 되는 영역은 두 포물선 $y=x^2$과 $y=2x^2$ 사이의 영역이며, 원점에서 접선이 $x$축으로 같은 이 영역은 어떤 직선과도 원점 근방에서 만나지 않는다. 직선만 검사하면 이 영역을 놓친다는 것이 이 예시의 요점이다.

---

**참고문헌**

**[Rud]** W. Rudin, *Principles of mathematical analysis*, 3rd ed., McGraw-Hill, 1976.
