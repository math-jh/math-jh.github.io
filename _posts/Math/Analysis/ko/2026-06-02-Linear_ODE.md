---
title: "선형 미분방정식계"
description: "연속계수 linear system x'=A(t)x+b(t)의 해가 구간 전체에서 존재하고 유일함을 보이고, 해공간이 n차원 벡터공간임과 Liouville 공식을 얻는다. 상수변화법 공식, 행렬지수와 조르당 표준형을 이용한 상수계수계의 풀이, 고계 방정식의 1계 연립으로의 환원을 다룬다."
excerpt: "linear system의 전역 해, 기본행렬과 Wronskian, 상수변화법, 행렬지수, 고계 방정식의 환원"

categories: [Math / Analysis]
permalink: /ko/math/analysis/linear_ode
sidebar: 
    nav: "analysis-ko"

date: 2026-06-02
weight: 29

published: false

---

[§미분방정식의 존재성과 유일성, ⁋정리 4](/ko/math/analysis/existence_uniqueness_ode#thm4){: data-lid="elxwt" }에서 얻은 해는 local solution이다. 비선형 방정식 $y'=y^2$, $y(0)=1$의 해 $y=1/(1-t)$는 [§미분방정식의 존재성과 유일성, ⁋예시 9](/ko/math/analysis/existence_uniqueness_ode#ex9){: data-lid="ee6oq" }에서 보았듯이 $t=1$에서 발산하므로, 우변이 매끄러워도 해가 정의되는 구간은 우변만으로 정해지지 않는다. 이 글에서 다루는 linear system에서는 이런 일이 일어나지 않는다. 계수가 연속인 구간 전체에서 해가 존재하고, 해 전체의 모임은 유한차원 벡터공간이 되어 선형대수로 다룰 수 있다. 아래에서 $\mathbb{K}$는 $\mathbb{R}$ 또는 $\mathbb{C}$이고, $\mathbb{K}^n$에는 Euclid 노름 $\lVert\cdot\rVert$를, $n\times n$ 행렬에는 그로부터 유도된 작용소노름 $\lVert A\rVert$를 쓴다. 따라서 $\lVert Ax\rVert\le\lVert A\rVert\lVert x\rVert$이고 $\lVert AB\rVert\le\lVert A\rVert\lVert B\rVert$이다. 벡터값·행렬값 함수의 미분과 적분은 성분별로 정의하며, $\lVert\int f\rVert\le\int\lVert f\rVert$가 성립한다.

## 전역 해의 존재

::: 정의 1
$I$를 구간, $A:I\to M_n(\mathbb{K})$와 $b:I\to\mathbb{K}^n$을 연속함수라 하자. 미분가능한 $x:I\to\mathbb{K}^n$에 대한 방정식

$$x'(t)=A(t)x(t)+b(t)$$

을 *선형 미분방정식계<sub>linear system</sub>*라 한다. $b\equiv0$이면 *제차<sub>homogeneous</sub>*, 아니면 *비제차*라 한다.
:::

우변이 $x$에 대해 선형이므로 해의 크기가 우변에 의해 가속되는 일이 없다. 이 사실을 [§미분방정식의 존재성과 유일성, ⁋정리 4](/ko/math/analysis/existence_uniqueness_ode#thm4){: data-lid="s43o0" }의 Picard 반복이 구간 전체에서 수렴한다는 형태로 쓰면 다음을 얻는다.

::: 정리 2 (전역 존재와 유일성)
$A$, $b$가 구간 $I$에서 연속이라 하자. 임의의 $t_0\in I$, $x_0\in\mathbb{K}^n$에 대하여 $x(t_0)=x_0$을 만족하는 해 $x:I\to\mathbb{K}^n$이 존재하고, 유일하다.
:::

::: 증명
$x$가 초기조건을 만족하는 해인 것은 $x$가 연속이고

$$x(t)=x_0+\int_{t_0}^t\bigl(A(s)x(s)+b(s)\bigr)\dd{s}\qquad(t\in I)$$

를 만족하는 것과 같다. [§미적분의 기본정리, ⁋정리 2](/ko/math/analysis/fundamental_theorem_of_calculus#thm2){: data-lid="lyfcb" }에 의해 integral equation의 연속해는 미분가능하며, 거꾸로 해를 적분하면 [§미적분의 기본정리, ⁋정리 5](/ko/math/analysis/fundamental_theorem_of_calculus#thm5){: data-lid="05p40" }에 의해 integral equation을 얻기 때문이다.

우선 $t_0$을 포함하는 컴팩트 구간 $J=[\alpha,\beta]\subseteq I$ 위에서 증명한다. $M=\max_J\lVert A\rVert$, $B=\max_J\lVert b\rVert$라 하자. $t\mapsto\lVert A(t)\rVert$는 연속이므로 [§연속함수의 성질, ⁋따름정리 2](/ko/math/analysis/continuous_functions#cor2){: data-lid="mpdzy" }에 의하여 최댓값이 존재한다.

*유일성.* $x,y$가 같은 초기조건의 해이면 $u=x-y$는 $u(t)=\int_{t_0}^tA(s)u(s)\dd{s}$를 만족한다. $K=\max_J\lVert u\rVert$라 하면 $\lVert u(t)\rVert\le K M^k\lvert t-t_0\rvert^k/k!$가 모든 $k\ge0$에 대해 성립한다. $k=0$은 $K$의 정의이고, $k$에서 $k+1$로는

$$\lVert u(t)\rVert\le\Bigl\lvert\int_{t_0}^tM\cdot\frac{KM^k\lvert s-t_0\rvert^k}{k!}\dd{s}\Bigr\rvert=\frac{KM^{k+1}\lvert t-t_0\rvert^{k+1}}{(k+1)!}$$

로 얻는다. 우변은 $k\to\infty$일 때 $0$으로 가므로 $u\equiv0$이다.

*존재.* $x_0(t)\equiv x_0$으로 두고 $x_{k+1}(t)=x_0+\int_{t_0}^t(A(s)x_k(s)+b(s))\dd{s}$로 연속함수열을 정의한다. $d_k=x_{k+1}-x_k$라 하면 $d_0(t)=\int_{t_0}^t(A(s)x_0+b(s))\dd{s}$이므로 $\lVert d_0(t)\rVert\le C\lvert t-t_0\rvert$이다. 여기서 $C=M\lVert x_0\rVert+B$이다. 또 $d_k(t)=\int_{t_0}^tA(s)d_{k-1}(s)\dd{s}$이므로 유일성의 증명과 같은 귀납으로

$$\lVert d_k(t)\rVert\le\frac{CM^k\lvert t-t_0\rvert^{k+1}}{(k+1)!}\le\frac{CM^k(\beta-\alpha)^{k+1}}{(k+1)!}$$

를 얻는다. 우변의 급수는 $k$에 대해 수렴하므로, [§균등수렴, ⁋정리 4](/ko/math/analysis/uniform_convergence#thm4){: data-lid="tf2eg" }에 의해 $x_k=x_0+\sum_{j<k}d_j$는 $J$ 위에서 균등수렴한다. 극한을 $x$라 하면 [§균등수렴, ⁋정리 6](/ko/math/analysis/uniform_convergence#thm6){: data-lid="g0vja" }에 의하여 $x$는 연속이고, $\lVert A(s)x_k(s)-A(s)x(s)\rVert\le M\lVert x_k(s)-x(s)\rVert\to0$이 균등하므로 점화식에서 $k\to\infty$로 보내 integral equation을 얻는다.

일반적인 구간 $I$에서는 $t_0$을 포함하는 컴팩트 구간 $J_1\subseteq J_2\subseteq\cdots$로 $I$를 덮는다. 각 $J_m$ 위의 해는 유일성에 의해 서로 일치하므로 하나의 함수 $x:I\to\mathbb{K}^n$을 정하고, 이는 $I$ 위의 해이다. $I$ 위의 두 해는 모든 $J_m$ 위에서 일치하므로 유일하다.
:::

증명에서 $M$이 해의 크기에 의존하지 않는다는 점이 쓰였다. [§미분방정식의 존재성과 유일성, ⁋예시 9](/ko/math/analysis/existence_uniqueness_ode#ex9){: data-lid="cceve" }의 $y'=y^2$에서는 우변의 립시츠 상수가 $\lvert y\rvert$와 함께 커지므로 같은 평가가 구간 전체로 확장되지 않는다.

## 해공간

제차계 $x'=A(t)x$의 해 전체를 $S$로 쓴다. 해의 일차결합은 해이므로 $S$는 벡터공간이다.

::: 정리 3 (해공간)
$A$가 $I$에서 연속이라 하자.

(a) 각 $t_0\in I$에 대하여 $x\mapsto x(t_0)$는 $S$에서 $\mathbb{K}^n$으로의 벡터공간 isomorphism이다. 특히 $\dim S=n$이다.

(b) $x_1,\dots,x_k\in S$가 $S$의 원소로서 일차독립인 것은 어떤 $t_0\in I$에 대해 $x_1(t_0),\dots,x_k(t_0)$가 $\mathbb{K}^n$에서 일차독립인 것과 같고, 이는 모든 $t\in I$에 대해 그러한 것과 같다.

(c) 비제차계 $x'=A(t)x+b(t)$의 해 하나를 $x_p$라 하면 해 전체는 $x_p+S$이다.
:::

::: 증명
(a) 선형성은 자명하다. 단사성은 $x(t_0)=0$이면 $x\equiv0$이라는 [정리 2](#thm2){: data-lid="mrsdh" }의 유일성이고, 전사성은 임의의 $x_0$에 대한 해의 존재이다.

(b) 임의의 $t$에 대해 $\ev_t:x\mapsto x(t)$가 (a)에 의해 isomorphism이므로 일차독립성을 보존하고 반사한다. 따라서 $S$에서의 일차독립은 모든 $t$에서의 일차독립과 같고, 한 점에서의 일차독립과도 같다.

(c) $x$가 비제차계의 해이면 $x-x_p\in S$이고, 거꾸로 $x_p+z$ ($z\in S$)는 해이다.
:::

(b)의 결론은 서로 다른 함수 $n$개의 일차독립성이 *같은 linear system의 해*라는 조건 아래에서만 한 점에서 판정된다는 뜻이다. 가령 $(t,0)$과 $(0,t)$는 함수로서 일차독립이지만 $t=0$에서는 모두 $0$이므로, 이 둘은 연속계수 linear system의 해가 될 수 없다.

::: 정의 4 (기본행렬)
제차계 $x'=A(t)x$의 해 $x_1,\dots,x_n$이 $S$의 기저일 때, 이들을 열로 하는 행렬값 함수 $\Phi=(x_1\ \cdots\ x_n)$을 *기본행렬<sub>fundamental matrix</sub>*이라 한다.
:::

$\Phi$의 각 열이 해이므로 $\Phi'=A\Phi$이다. [정리 3](#thm3){: data-lid="vzzeh" }의 (b)에 의해 모든 $t\in I$에서 $\det\Phi(t)\ne0$이다. 역으로 $\Phi'=A\Phi$를 만족하고 어떤 한 점에서 가역인 행렬값 함수는 기본행렬이다. 제차계의 일반해는 $x(t)=\Phi(t)c$ ($c\in\mathbb{K}^n$)이고, 초기조건 $x(t_0)=x_0$을 만족하는 해는 $\Phi(t)\Phi(t_0)^{-1}x_0$이다.

연속성 가정은 빠질 수 없다. 스칼라 방정식 $tx'=x$는 $t\ne0$에서 $x'=(1/t)x$로 쓰이고, 계수 $1/t$가 $t=0$에서 연속이 아니다. $\mathbb{R}$ 위의 해는 $x=ct$ 꼴이어서 모두 $x(0)=0$이다. 따라서 $x(0)=1$을 만족하는 해는 없고, $x(0)=0$을 만족하는 해는 무수히 많아 [정리 3](#thm3){: data-lid="zy62e" }의 (a)가 깨진다.

## Wronskian과 Liouville 공식

기본행렬의 행렬식은 $A$의 trace만으로 결정된다.

::: 정리 5 (Liouville 공식)
$x_1,\dots,x_n\in S$이고 $W(t)=\det(x_1(t)\ \cdots\ x_n(t))$ (*Wronskian*)이라 하자. 그러면 $W'(t)=\tr A(t)W(t)$이고, 임의의 $t_0\in I$에 대하여

$$W(t)=W(t_0)\exp\Bigl(\int_{t_0}^t\tr A(s)\dd{s}\Bigr)$$

이다.
:::

::: 증명
$\Phi=(x_1\ \cdots\ x_n)$이라 하고 $\varphi_i$를 $\Phi$의 $i$번째 행이라 하자. [\[선형대수학\] §행렬식, ⁋정의 4](/ko/math/linear_algebra/determinant#def4){: data-lid="tx4gk" }에 의해 행렬식은 각 행에 대해 선형이므로 곱의 미분법칙에 의해

$$W'=\sum_{i=1}^n\det(\varphi_1,\dots,\varphi_i',\dots,\varphi_n)$$

이다. $\Phi'=A\Phi$의 $i$번째 행은 $\varphi_i'=\sum_ja_{ij}\varphi_j$이다. 이를 $i$번째 항에 넣어 전개하면 $j\ne i$인 항에는 같은 행 $\varphi_j$가 두 번 나타나 [\[선형대수학\] §행렬식, ⁋명제 3](/ko/math/linear_algebra/determinant#prop3){: data-lid="ozp7x" }에 의하여 행렬식이 $0$이 되고, $j=i$인 항만 $a_{ii}W$로 남는다. 따라서 $W'=\sum_ia_{ii}W=\tr A\cdot W$이다.

이제 $\bigl(W(t)e^{-\int_{t_0}^t\tr A}\bigr)'=(W'-\tr A\cdot W)e^{-\int_{t_0}^t\tr A}=0$이므로 $We^{-\int_{t_0}^t\tr A}$는 상수이고, $t=t_0$에서의 값이 $W(t_0)$이다.
:::

공식에서 지수함수는 $0$이 되지 않으므로 $W$는 한 점에서 $0$이면 항등적으로 $0$이다. 이는 [정리 3](#thm3){: data-lid="82fnj" }의 (b)를 $k=n$인 경우에 대해 다시 얻은 것이다. 같은 계의 해가 아닌 함수들에 대해서는 성립하지 않는 판정법이다.

## 상수변화법

비제차계의 해를 제차계의 기본행렬로 적는 방법을 본다. 제차계의 일반해 $\Phi(t)c$에서 상수 $c$가 비제차항을 흡수하도록 함수 $c(t)$로 바꾸어 $x=\Phi c$를 시도한다. 그러면 $x'=\Phi'c+\Phi c'=A\Phi c+\Phi c'=Ax+\Phi c'$이므로 $\Phi c'=b$이면 충분하고, 이는 $c'=\Phi^{-1}b$이다. 이 계산을 정리하면 다음과 같다.

::: 정리 6 (상수변화법)
$\Phi$가 제차계 $x'=A(t)x$의 기본행렬이고 $b$가 연속이라 하자. 초기조건 $x(t_0)=x_0$을 만족하는 $x'=A(t)x+b(t)$의 유일한 해는

$$x(t)=\Phi(t)\Phi(t_0)^{-1}x_0+\int_{t_0}^t\Phi(t)\Phi(s)^{-1}b(s)\dd{s}$$

이다.
:::

::: 증명
$\Phi(s)$의 성분은 연속이고 $\det\Phi(s)\ne0$이므로 역행렬은 여인자 공식에 의해 연속인 성분을 가진다. 따라서 $c(t)=\Phi(t_0)^{-1}x_0+\int_{t_0}^t\Phi(s)^{-1}b(s)\dd{s}$는 $C^1$이고 $c'=\Phi^{-1}b$이다. $x=\Phi c$로 두면 $x'=\Phi'c+\Phi c'=A\Phi c+b=Ax+b$이고 $x(t_0)=\Phi(t_0)c(t_0)=x_0$이다. 유일성은 [정리 2](#thm2){: data-lid="qih8p" }이다.
:::

첫 항은 제차해이고 적분항은 $x_0=0$일 때의 해, 곧 특수해이다. 행렬 $\Phi(t)\Phi(s)^{-1}$은 기본행렬의 선택에 의존하지 않는다. 다른 기본행렬은 가역행렬 $C$에 대해 $\Phi C$ 꼴이고, $\Phi C(\Phi C)^{-1}$ 계산에서 $C$가 소거되기 때문이다.

## 행렬지수

계수가 상수인 계 $x'=Ax$에서는 기본행렬을 명시적으로 쓸 수 있다. 스칼라 방정식 $x'=ax$의 해가 $e^{at}x_0$이므로 같은 꼴을 시도한다.

::: 정의 7
$A\in M_n(\mathbb{K})$에 대하여 *행렬지수<sub>matrix exponential</sub>*를

$$e^A=\sum_{k=0}^\infty\frac{A^k}{k!}$$

로 정의한다.
:::

$\lVert A^k/k!\rVert\le\lVert A\rVert^k/k!$이고 $\sum_k\lVert A\rVert^k/k!=e^{\lVert A\rVert}<\infty$이므로, [§무한급수와 수렴판정법, ⁋정리 6](/ko/math/analysis/series#thm6){: data-lid="k5iaq" }에 의하여 급수는 성분별로 절대수렴한다. 같은 평가로 $t\in[-R,R]$에서 $\sum_kt^kA^k/k!$는 [§균등수렴, ⁋정리 4](/ko/math/analysis/uniform_convergence#thm4){: data-lid="exsgk" }에 의해 균등수렴하고, 항별로 미분한 급수 $\sum_{k\ge1}t^{k-1}A^k/(k-1)!$도 같은 이유로 균등수렴한다. [§균등수렴, ⁋정리 9](/ko/math/analysis/uniform_convergence#thm9){: data-lid="umkb2" }에 의해 $e^{tA}$는 미분가능하고 $\frac{d}{\dd{t}}e^{tA}=Ae^{tA}=e^{tA}A$이다.

::: 명제 8 (행렬지수의 성질)
(a) $AB=BA$이면 $e^{A+B}=e^Ae^B$이다. 특히 $e^A$는 가역이고 $(e^A)^{-1}=e^{-A}$이다.

(b) $P$가 가역이면 $e^{PAP^{-1}}=Pe^AP^{-1}$이다.

(c) $\det e^{tA}=e^{t\tr A}$이다.

(d) $e^{tA}$는 제차계 $x'=Ax$의 기본행렬이고, 초기조건 $x(t_0)=x_0$을 만족하는 해는 $x(t)=e^{(t-t_0)A}x_0$이다. 비제차계 $x'=Ax+b(t)$의 해는

$$x(t)=e^{(t-t_0)A}x_0+\int_{t_0}^te^{(t-s)A}b(s)\dd{s}$$

이다.
:::

::: 증명
(a) $B$는 모든 $A^k$와 교환하므로, multiplication의 연속성에 의해 급수의 합 $e^{tA}$와도 교환한다. $F(t)=e^{tA}e^{tB}$라 하면

$$F'=Ae^{tA}e^{tB}+e^{tA}Be^{tB}=(A+B)F$$

이고 $F(0)=I$이다. $G(t)=e^{t(A+B)}$도 같은 방정식과 초기조건을 만족하므로, 각 열에 [정리 2](#thm2){: data-lid="4gf1b" }의 유일성을 적용하면 $F=G$이다. $t=1$을 넣으면 된다. 가역성은 $A$와 $-A$가 교환하므로 $e^Ae^{-A}=e^0=I$에서 나온다.

(b) $(PAP^{-1})^k=PA^kP^{-1}$이고 $X\mapsto PXP^{-1}$는 연속선형이므로 급수에 항별로 적용된다.

(c) $\Phi=e^{tA}$는 $\Phi'=A\Phi$를 만족하고 $\Phi(0)=I$이므로 $W=\det\Phi$에 [정리 5](#thm5){: data-lid="kdo0e" }를 쓰면 $W(t)=e^{t\tr A}$이다.

(d) 열 $e^{tA}e_j$는 미분 공식에 의해 해이고, $t=0$에서 $e_j$이므로 일차독립이다. 해의 공식은 $\Phi=e^{tA}$를 [정리 6](#thm6){: data-lid="i7ozd" }에 넣고 (a)에 의해 $\Phi(t)\Phi(s)^{-1}=e^{tA}e^{-sA}=e^{(t-s)A}$를 쓴 것이다.
:::

스칼라의 지수법칙에서 교환 조건이 빠지면 성립하지 않는다. 또 $e^{tA}$의 성분은 $e^{ta_{ij}}$가 아니다. 두 가지는 모두 흔한 오류이다.

::: 예시 9 (교환하지 않는 경우)
$A=\begin{pmatrix}0&1\\0&0\end{pmatrix}$, $B=\begin{pmatrix}0&0\\1&0\end{pmatrix}$이라 하자. $A^2=B^2=0$이므로 $e^A=I+A$, $e^B=I+B$이고

$$e^Ae^B=\begin{pmatrix}1&1\\0&1\end{pmatrix}\begin{pmatrix}1&0\\1&1\end{pmatrix}=\begin{pmatrix}2&1\\1&1\end{pmatrix}$$

이다. 반면 $S=A+B=\begin{pmatrix}0&1\\1&0\end{pmatrix}$는 $S^2=I$이므로 $S^{2m}=I$, $S^{2m+1}=S$이고 $e^{A+B}=\cosh(1)I+\sinh(1)S$이다. 이 행렬의 대각성분은 $\cosh(1)<2$이므로 $e^{A+B}\ne e^Ae^B$이다.
:::

같은 이유로 $A(t)$가 $t$에 따라 변하는 경우 $x(t)=\exp\bigl(\int_{t_0}^tA\bigr)x_0$는 일반적으로 해가 아니다. $\frac{d}{\dd{t}}e^{B(t)}=B'(t)e^{B(t)}$는 $B'$이 $B$와 교환할 때만 성립한다.

## Jordan canonical form을 이용한 계산

$e^{tA}$를 급수로 직접 더하는 대신 $A$의 Jordan canonical form을 쓴다. [\[선형대수학\] §조르당 표준형, ⁋정리 12](/ko/math/linear_algebra/Jordan_canonical_form#thm12){: data-lid="zmi7y" }에 의해 $\mathbb{C}$ 위에서 $A=PJP^{-1}$이고, $J$는 Jordan block $J_k(\lambda)=\lambda I_k+N_k$ ($N_k$는 대각선 바로 위에만 $1$을 가진 $k\times k$ 행렬)의 블록대각행렬이다. $A$가 실행렬이어도 급수는 실행렬의 급수이므로 $e^{tA}$는 실행렬이다. 복소수 위에서 계산하는 것은 중간 단계일 뿐이다.

::: 명제 10 (Jordan block의 지수)
(a) $e^{tA}=Pe^{tJ}P^{-1}$이고, $J=\diag(J_{k_1}(\lambda_1),\dots,J_{k_r}(\lambda_r))$이면 $e^{tJ}=\diag(e^{tJ_{k_1}(\lambda_1)},\dots,e^{tJ_{k_r}(\lambda_r)})$이다.

(b) Jordan block에 대하여

$$e^{tJ_k(\lambda)}=e^{\lambda t}\sum_{j=0}^{k-1}\frac{t^j}{j!}N_k^j$$

이고, 이 행렬의 $(i,i+j)$ 성분은 $e^{\lambda t}t^j/j!$, 나머지 성분은 $0$이다.
:::

::: 증명
(a) 첫 식은 [명제 8](#prop8){: data-lid="oko9q" }의 (b)이다. 블록대각행렬의 거듭제곱은 블록별 거듭제곱이므로 급수의 각 항이, 따라서 합이 블록별로 계산된다.

(b) $\lambda tI$와 $tN_k$는 교환하므로 [명제 8](#prop8){: data-lid="y7uh1" }의 (a)에 의해 $e^{tJ_k(\lambda)}=e^{\lambda t}e^{tN_k}$이다. $N_k$는 $k$번 곱하면 $0$이므로 $e^{tN_k}=\sum_{j<k}t^jN_k^j/j!$이고, $N_k^j$는 대각선에서 $j$칸 위에만 $1$을 가진 행렬이다.
:::

따라서 $A$의 고윳값이 $\lambda_1,\dots,\lambda_s$이고 $\lambda_i$에 속한 Jordan block의 최대 크기가 $m_i$이면, $e^{tA}$의 모든 성분과 모든 해의 모든 성분은 $t^je^{\lambda_it}$ ($0\le j<m_i$)의 일차결합이다. $A$가 대각화되면 $m_i=1$이어서 $e^{\lambda_it}$만 나타난다. 대각화되지 않을 때에만 $t^je^{\lambda t}$ ($j\ge1$)가 나타난다. 실행렬의 고윳값 $\lambda=a+i\omega$는 켤레와 쌍으로 나타나 $e^{at}\cos\omega t$, $e^{at}\sin\omega t$ 꼴의 실수 해를 준다. 가령 $A=aI+\omega\begin{pmatrix}0&-1\\1&0\end{pmatrix}$에서는 $\begin{pmatrix}0&-1\\1&0\end{pmatrix}^2=-I$이므로 $e^{tA}=e^{at}\begin{pmatrix}\cos\omega t&-\sin\omega t\\\sin\omega t&\cos\omega t\end{pmatrix}$이다.

::: 예시 11 (결손 고윳값)
$A=\begin{pmatrix}0&1\\-1&2\end{pmatrix}$의 특성다항식은 $(\lambda-1)^2$이다. $N=A-I=\begin{pmatrix}-1&1\\-1&1\end{pmatrix}$는 $0$이 아니고 $N^2=0$이므로 $A$는 대각화되지 않는다. $I$와 $N$이 교환하므로 $P$를 구하지 않고도

$$e^{tA}=e^te^{tN}=e^t(I+tN)=e^t\begin{pmatrix}1-t&t\\-t&1+t\end{pmatrix}$$

을 얻는다. 모든 해는 $e^t$와 $te^t$의 일차결합이며, 초기조건 $x(0)=(1,0)$의 해는 $e^t(1-t,-t)$이다.
:::

## 고계 방정식의 환원

$y^{(n)}+a_{n-1}(t)y^{(n-1)}+\cdots+a_0(t)y=g(t)$ ($a_i,g$는 $I$에서 연속)를 고계 선형 방정식이라 한다. $x_i=y^{(i-1)}$ ($i=1,\dots,n$)로 두면 $x_i'=x_{i+1}$ ($i<n$)이고 마지막 식이 방정식 자체이므로

$$x'=C(t)x+g(t)e_n,\qquad C(t)=\begin{pmatrix}0&1&&\\&\ddots&\ddots&\\&&0&1\\-a_0&-a_1&\cdots&-a_{n-1}\end{pmatrix}$$

을 얻는다. 여기서 $e_n=(0,\dots,0,1)$이다.

::: 명제 12 (1계 연립으로의 환원)
$C^n$급 함수 $y$가 고계 방정식의 해인 것은 $x=(y,y',\dots,y^{(n-1)})$이 위의 1계 연립의 해인 것과 같고, 이 대응은 해 전체 사이의 일대일대응이다.
:::

::: 증명
앞의 계산이 "$\Rightarrow$"이다. 역으로 $x$가 연립의 해이면 $y=x_1$로 둔다. 처음 $n-1$개의 식 $x_i'=x_{i+1}$에서 $x_i=y^{(i-1)}$이 되고, 마지막 식은 고계 방정식이다. 연립의 해 $x$는 $y$로부터 결정되므로 대응은 일대일이다.
:::

[정리 2](#thm2){: data-lid="nllni" }, [정리 3](#thm3){: data-lid="5pyvn" }, [정리 6](#thm6){: data-lid="whl6u" }이 그대로 옮겨진다. 초기조건 $y(t_0),\dots,y^{(n-1)}(t_0)$을 주면 $I$ 전체에서 해가 유일하게 존재하고, 제차 방정식의 해공간은 $n$차원이다. 해 $y_1,\dots,y_n$의 Wronskian $W=\det\bigl(y_j^{(i-1)}\bigr)_{i,j}$는 대응하는 기본행렬의 행렬식이다. $\tr C=-a_{n-1}$이므로 [정리 5](#thm5){: data-lid="kbfsn" }에서

$$W(t)=W(t_0)\exp\Bigl(-\int_{t_0}^ta_{n-1}(s)\dd{s}\Bigr)$$

을 얻는다. 특히 $a_{n-1}=0$이면 $W$는 상수이다.

::: 예시 13 (공명)
$y''-2y'+y=e^t$, $y(0)=y'(0)=0$을 풀자. $x=(y,y')$로 두면 $x'=Ax+(0,e^t)$이고 $A$는 [예시 11](#ex11){: data-lid="jvwhc" }의 행렬이다. [명제 8](#prop8){: data-lid="fqez3" }의 (d)에 의해

$$\begin{aligned}
x(t)&=\int_0^te^{t-s}(I+(t-s)N)\begin{pmatrix}0\\e^s\end{pmatrix}\dd{s}\\
&=e^t\int_0^t\begin{pmatrix}t-s\\1+t-s\end{pmatrix}\dd{s}=e^t\begin{pmatrix}t^2/2\\t+t^2/2\end{pmatrix}
\end{aligned}$$

이다. 여기서 $N\begin{pmatrix}0\\1\end{pmatrix}=\begin{pmatrix}1\\1\end{pmatrix}$을 썼다. 첫 성분에서 $y=t^2e^t/2$를 얻고, 둘째 성분은 $y'$과 일치한다. 비제차항 $e^t$가 제차해 $e^t$, $te^t$와 같은 지수를 가지므로 해에 $t^2$이 곱해진다.
:::

---

**참고문헌**

**[Rud]** W. Rudin, *Principles of mathematical analysis*, 3rd ed., McGraw-Hill, 1976.
