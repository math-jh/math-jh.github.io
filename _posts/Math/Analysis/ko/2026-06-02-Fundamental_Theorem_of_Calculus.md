---
title: "미적분의 기본정리"
description: "가변상한 적분 F(x)=∫f의 연속성과 f가 연속인 점에서의 미분가능성(제1기본정리), 도함수의 적분으로 증분을 복원하는 제2기본정리를 증명한다. 도함수가 적분불가능한 반례와 연속성 가정이 빠진 반례를 확인하고, 부분적분·치환적분의 엄밀한 형태와 적분의 평균값 정리를 증명한다."
excerpt: "가변상한 적분의 미분, 제2기본정리, 부분적분·치환적분, 적분의 평균값 정리"

categories: [Math / Analysis]
permalink: /ko/math/analysis/fundamental_theorem_of_calculus
sidebar: 
    nav: "analysis-ko"

date: 2026-06-02
weight: 17

published: false

---

[§미분, ⁋정의 1](/ko/math/analysis/differentiation#def1)은 difference quotient의 극한으로, [§Riemann 적분, ⁋정의 4](/ko/math/analysis/riemann_integral#def4)는 분할에 따른 하합의 supremum과 상합의 infimum으로 정의되며, 정의만 보아서는 두 연산 사이에 어떤 관계도 보이지 않는다. 미적분의 기본정리는 이 둘이 서로를 되돌린다는 사실이다. 적분의 상한을 변수로 놓고 미분하면 피적분함수가 돌아오고(제1기본정리), 함수의 도함수를 적분하면 그 함수의 증분이 돌아온다(제2기본정리).

두 방향은 가정이 서로 다르다. 앞의 것은 피적분함수가 연속인 점에서만 성립하고, 뒤의 것은 도함수가 적분가능하다는 가정이 있어야 의미가 있다. 이 글은 두 정리를 각각에 필요한 가정 아래에서 증명하고, 가정이 빠지면 무엇이 무너지는지를 반례로 확인한 뒤, 부분적분·치환적분·적분의 평균값 정리를 이 위에서 엄밀하게 세운다.

이 글에서 $f$가 적분가능하다는 것은 $[a,b]$에서 Riemann 적분가능하다는 뜻이다. 다음 성질을 그대로 쓴다. [§Riemann 적분, ⁋정의 4](/ko/math/analysis/riemann_integral#def4)에 의하여 적분가능한 함수는 bounded이고, [§Riemann 적분, ⁋명제 12](/ko/math/analysis/riemann_integral#prop12)에 의하여 적분은 선형이며 단조이고, [§Riemann 적분, ⁋명제 16](/ko/math/analysis/riemann_integral#prop16)에 의하여 구간가법성 $\int_a^c f = \int_a^b f + \int_b^c f$가 성립한다. 또 [§Riemann 적분, ⁋명제 13](/ko/math/analysis/riemann_integral#prop13)에 의하여 $f$가 적분가능하면 $\lvert f\rvert$도 적분가능하고 $\bigl\lvert\int_a^b f\bigr\rvert \leq \int_a^b \lvert f\rvert$이며 적분가능한 함수의 곱은 적분가능하고, [§Riemann 적분, ⁋정리 6](/ko/math/analysis/riemann_integral#thm6)에 의하여 연속함수는 적분가능하다. 끝점의 대소와 무관하게 구간가법성을 쓰기 위해 $\int_y^x f = -\int_x^y f$, $\int_x^x f = 0$으로 약속한다.

## 가변상한 적분

$f$가 $[a,b]$에서 적분가능하면 각 $x \in [a,b]$에 대해 $[a,x]$ 위의 적분이 정해지므로

$$F(x) = \int_a^x f(t) \dd{t}$$

로 함수 $F : [a,b] \rightarrow \mathbb{R}$를 정의할 수 있다. 우리가 밝힐 것은 $f$의 성질이 $F$의 성질로 어떻게 옮겨 가는지이다. 먼저 $f$의 적분가능성만으로 $F$가 연속임을 보인다.

::: 명제 1
$f$가 $[a,b]$에서 적분가능하고 $\lvert f\rvert \leq M$이면, 모든 $x, y \in [a,b]$에 대해 $\lvert F(y) - F(x)\rvert \leq M\lvert y - x\rvert$이다. 특히 $F$는 연속이다.
:::

::: 증명
$f$가 bounded이므로 $M$이 존재한다. $x \leq y$라 하자. [§Riemann 적분, ⁋명제 16](/ko/math/analysis/riemann_integral#prop16)에 의해 $F(y) - F(x) = \int_x^y f$이므로

$$\begin{aligned}
\lvert F(y) - F(x)\rvert
&\leq \int_x^y \lvert f\rvert \\
&\leq M(y - x)
\end{aligned}$$

이다. $x > y$인 경우는 두 문자를 바꾸면 된다. $\varepsilon > 0$이 주어지면 $\delta = \varepsilon/M$이 $\lvert y - x\rvert < \delta$일 때 $\lvert F(y) - F(x)\rvert < \varepsilon$이 되게 하므로 $F$는 연속이다 ($M = 0$이면 $F \equiv 0$이다).
:::

$F$가 연속이라는 결론은 $f$가 불연속이어도 유지된다. 적분이 평균을 취하는 연산이라 $f$의 불연속이 $F$에서는 꺾임으로 완화되기 때문이다. 그러나 미분가능성은 다르다. 꺾임은 미분가능성을 깨므로, $F'$의 존재는 $f$의 연속성에 달려 있다.

::: 정리 2 (제1기본정리)
$f$가 $[a,b]$에서 적분가능하고 $x_0 \in [a,b]$에서 연속이면, $F$는 $x_0$에서 미분가능하고 $F'(x_0) = f(x_0)$이다. ($x_0$가 끝점이면 단측 도함수이다.)
:::

::: 증명
$h \neq 0$이고 $x_0 + h \in [a,b]$라 하자. [§Riemann 적분, ⁋명제 16](/ko/math/analysis/riemann_integral#prop16)으로 $F(x_0 + h) - F(x_0) = \int_{x_0}^{x_0+h} f$이다. 상수 $f(x_0)$는 $\int_{x_0}^{x_0+h} f(x_0) \dd{t} = f(x_0)h$를 만족하므로, 목표값과의 차이가 한 적분으로 묶인다.

$$\begin{aligned}
\frac{F(x_0 + h) - F(x_0)}{h} - f(x_0)
&= \frac{1}{h}\int_{x_0}^{x_0+h}\bigl(f(t) - f(x_0)\bigr)\dd{t}
\end{aligned}$$

$\varepsilon > 0$이 주어졌다 하자. $f$가 $x_0$에서 연속이므로 $\lvert t - x_0\rvert < \delta$이면 $\lvert f(t) - f(x_0)\rvert < \varepsilon$인 $\delta > 0$이 있다. 이 $\delta$는 $x_0$에서의 연속성만으로 정해지며 $h$나 $t$에 의존하지 않는다. $0 < \lvert h\rvert < \delta$이면 적분구간의 모든 점 $t$가 $\lvert t - x_0\rvert \leq \lvert h\rvert < \delta$를 만족하므로, 위 식의 절댓값은

$$\begin{aligned}
\left\lvert\frac{1}{h}\int_{x_0}^{x_0+h}\bigl(f(t) - f(x_0)\bigr)\dd{t}\right\rvert
&\leq \frac{1}{\lvert h\rvert}\left\lvert\int_{x_0}^{x_0+h}\lvert f(t) - f(x_0)\rvert\dd{t}\right\rvert \\
&\leq \frac{1}{\lvert h\rvert}\cdot\varepsilon\lvert h\rvert \\
&= \varepsilon
\end{aligned}$$

이하이다. 따라서 $h \rightarrow 0$일 때 difference quotient는 $f(x_0)$로 수렴한다.
:::

증명에서 보듯 $F'(x_0)$는 $x_0$ 근방에서 $f$의 평균값의 극한이다. 연속성은 이 평균이 $f(x_0)$로 모이게 하는 조건이고, 그것이 빠지면 결론도 무너진다.

::: 예시 3 (연속성이 빠진 경우)
$f$가 $[-1,1]$에서 $x < 0$이면 $0$, $x \geq 0$이면 $1$이라 하자. $f$는 적분가능하고 $F(x) = \int_{-1}^x f$는 $x \leq 0$에서 $0$, $x \geq 0$에서 $x$이다. 따라서 $F$는 연속이지만 $0$에서 좌미분계수 $0$과 우미분계수 $1$이 달라 미분가능하지 않다.

한 점의 값만 어긋나는 경우도 있다. $g(0) = 1$이고 $x \neq 0$이면 $g(x) = 0$이라 하면 $g$는 적분가능하고 적분값은 $0$이므로 $G(x) = \int_{-1}^x g \equiv 0$이다. $G$는 $0$에서 미분가능하지만 $G'(0) = 0 \neq g(0)$이다. 적분은 한 점의 값을 보지 못하므로, 불연속점에서는 $F'$가 존재하더라도 $f$와 일치할 이유가 없다.
:::

$f$가 구간 전체에서 연속이면 모든 점에서 $F' = f$이다. 즉 연속함수는 항상 원시함수를 가지며, $F$가 그 하나이다. 원시함수가 $F + C$ 꼴로 상수만큼만 다른 것은, 두 원시함수의 차가 도함수 $0$을 가져 [§평균값 정리와 테일러 정리, ⁋따름정리 4](/ko/math/analysis/mean_value_theorem#cor4)에 의해 상수이기 때문이다. 이 존재성은 closed form의 존재와 무관하다. $e^{-t^2}$의 원시함수는 초등함수로 표현되지 않지만, $\int_0^x e^{-t^2}\dd{t}$로서 존재하고 도함수가 $e^{-x^2}$임을 [정리 2](#thm2)가 보장한다.

적분의 한계가 $x$의 함수인 경우는 [§미분, ⁋정리 4](/ko/math/analysis/differentiation#thm4)로 처리된다.

::: 따름정리 4
$f$가 $[a,b]$에서 연속이고 $u, v : [c,d] \rightarrow [a,b]$가 미분가능하면, $\Phi(x) = \int_{v(x)}^{u(x)} f(t)\dd{t}$는 $[c,d]$에서 미분가능하고

$$\Phi'(x) = f\bigl(u(x)\bigr)u'(x) - f\bigl(v(x)\bigr)v'(x)$$

이다.
:::

::: 증명
$F(y) = \int_a^y f$라 하면 [정리 2](#thm2)에 의해 $F' = f$이고, [§Riemann 적분, ⁋명제 16](/ko/math/analysis/riemann_integral#prop16)에 의해 $\Phi = F\circ u - F\circ v$이다. $F$는 $[a,b]$에서 미분가능하고 $u(x) \in [a,b]$이므로 [§미분, ⁋정리 4](/ko/math/analysis/differentiation#thm4)를 쓸 수 있다. ($u(x)$가 $a$ 또는 $b$이면 $F'$는 단측 도함수이지만, $u(x+h) \in [a,b]$이므로 연쇄법칙의 증명은 그대로 유효하다.) 따라서 $(F\circ u)' = f(u)u'$이고, $v$도 마찬가지이다.
:::

## 제2기본정리

이제 반대 방향을 다룬다. 이번에는 $f$의 연속성을 요구하지 않는다. 함수 $G$가 주어지고 그 도함수가 적분가능하다는 것만 가정한다.

::: 정리 5 (제2기본정리)
$G : [a,b] \rightarrow \mathbb{R}$가 연속이고 $(a,b)$에서 미분가능하며, $f = G'$이 $(a,b)$에서 정의된 도함수를 $[a,b]$로 임의로 확장한 함수가 적분가능하다고 하자. 그러면

$$\int_a^b f = G(b) - G(a)$$

이다.
:::

::: 증명
분할 $P : a = x_0 < x_1 < \cdots < x_n = b$를 임의로 잡는다. 각 $[x_{i-1}, x_i]$에서 $G$는 연속이고 내부에서 미분가능하므로, [§평균값 정리와 테일러 정리, ⁋정리 3](/ko/math/analysis/mean_value_theorem#thm3)에 의해

$$G(x_i) - G(x_{i-1}) = f(t_i)\Delta x_i$$

인 $t_i \in (x_{i-1}, x_i)$이 있다. 여기서 $\Delta x_i = x_i - x_{i-1}$이고 $G'(t_i) = f(t_i)$를 썼다. 이를 $i = 1, \ldots, n$에 대해 더하면 좌변은 망원합으로 접힌다.

$$G(b) - G(a) = \sum_{i=1}^n f(t_i)\Delta x_i$$

$m_i = \inf_{[x_{i-1},x_i]} f$, $M_i = \sup_{[x_{i-1},x_i]} f$라 하면 $m_i \leq f(t_i) \leq M_i$이므로, 하합 $L(P,f)$와 상합 $U(P,f)$ 사이에

$$L(P,f) \leq G(b) - G(a) \leq U(P,f)$$

가 성립한다. $P$는 임의였고 $G(b) - G(a)$는 $P$에 의존하지 않으므로, 이는 $\sup_P L(P,f) \leq G(b) - G(a) \leq \inf_P U(P,f)$를 뜻한다. $f$가 적분가능하면 양 끝이 모두 $\int_a^b f$이므로 $\int_a^b f = G(b) - G(a)$이다.
:::

증명은 $f$가 적분가능하다는 사실을 마지막에 한 번만 쓴다. $G(b) - G(a)$가 모든 하합 이상, 모든 상합 이하인 수라는 것까지는 $f$에 대한 가정 없이 얻어지고, 적분가능성이 그런 수가 하나뿐임을 보장한다. 원시함수를 아는 경우에 적분이 끝점의 값으로 환원되는 것은 이 때문이다. $f$가 연속이면 [§Riemann 적분, ⁋정리 6](/ko/math/analysis/riemann_integral#thm6)에 의하여 $f$는 적분가능하므로 $G' = f$인 어떤 $G$로든 $\int_a^b f = G(b) - G(a)$이고, 이 값은 원시함수의 선택에 의존하지 않는다.

[정리 5](#thm5)의 두 가정은 모두 필요하다. $G$의 연속성이 끝점에서 빠지면, $G(x) = 0$ ($0 \leq x < 1$), $G(1) = 1$은 $(0,1)$에서 $G' = 0$이고 $\int_0^1 0 = 0 \neq G(1) - G(0)$이다. 증명에서 평균값 정리를 $[x_{i-1}, x_i]$ 전체에서 쓰기 때문에 끝점에서의 연속성이 필요하다. 한편 $G'$의 적분가능성이 빠지는 경우는 더 미묘하다. $G$가 모든 점에서 미분가능해도 $G'$가 적분가능하지 않을 수 있다.

::: 예시 6 (도함수가 적분가능하지 않은 경우)
$[0,1]$에서 $G(x) = x^2\sin(1/x^2)$ ($x \neq 0$), $G(0) = 0$이라 하자. $x \neq 0$에서는 곱의 미분법과 [§미분, ⁋정리 4](/ko/math/analysis/differentiation#thm4)로

$$G'(x) = 2x\sin\frac{1}{x^2} - \frac{2}{x}\cos\frac{1}{x^2}$$

이고, $0$에서는 $\lvert G(h)/h\rvert = \lvert h\sin(1/h^2)\rvert \leq \lvert h\rvert$이므로 $G'(0) = 0$이다. 따라서 $G$는 $[0,1]$ 전체에서 미분가능하다.

그러나 $G'$는 bounded가 아니다. $x_n = 1/\sqrt{2\pi n}$ ($n \geq 1$)으로 두면 $x_n \in (0,1]$이고 $\sin(1/x_n^2) = \sin(2\pi n) = 0$, $\cos(1/x_n^2) = 1$이므로

$$G'(x_n) = -\frac{2}{x_n} = -2\sqrt{2\pi n}$$

이 되어 $n \rightarrow \infty$일 때 $-\infty$로 발산한다. bounded가 아닌 함수는 [§Riemann 적분, ⁋정의 4](/ko/math/analysis/riemann_integral#def4)에 의하여 Riemann 적분가능하지 않으므로 $\int_0^1 G'$ 자체가 정의되지 않고, [정리 5](#thm5)의 등식은 의미를 잃는다. 이 경우 적분을 정의하는 쪽을 넓혀야 비로소 $G(1) - G(0)$을 복원할 수 있다.
:::

$G'$가 bounded이기만 하면 충분한 것도 아니다. 모든 점에서 미분가능하고 $G'$가 bounded이지만 Riemann 적분가능하지 않은 함수가 존재한다(Volterra의 예). 따라서 [정리 5](#thm5)의 가정은 $G'$의 적분가능성 자체여야 한다.

## 부분적분과 치환적분

제2기본정리는 적분을 원시함수의 끝점 값으로 바꾸므로, 미분법칙은 곧 적분법칙이 된다. 그 엄밀한 형태에서 요구되는 것은 연속미분가능성이 아니라 미분 결과의 적분가능성이다.

::: 명제 7 (부분적분)
$u, v$가 $[a,b]$에서 미분가능하고 $u', v'$이 적분가능하면

$$\int_a^b u v'\dd{x} = u(b)v(b) - u(a)v(a) - \int_a^b u'v\dd{x}$$

이다.
:::

::: 증명
$u, v$는 미분가능하므로 [§미분, ⁋명제 2](/ko/math/analysis/differentiation#prop2)에 의하여 연속이고, 따라서 [§Riemann 적분, ⁋정리 6](/ko/math/analysis/riemann_integral#thm6)에 의하여 적분가능하다. 적분가능한 함수의 곱은 [§Riemann 적분, ⁋명제 13](/ko/math/analysis/riemann_integral#prop13)에 의하여 적분가능하므로 $u'v$와 $uv'$이 적분가능하고, 곱의 미분법에 의해 $(uv)' = u'v + uv'$이며 이것도 [§Riemann 적분, ⁋명제 12](/ko/math/analysis/riemann_integral#prop12)에 의하여 적분가능하다. $uv$는 $[a,b]$에서 미분가능하므로 [정리 5](#thm5)를 $G = uv$에 적용하면

$$\begin{aligned}
u(b)v(b) - u(a)v(a)
&= \int_a^b (u'v + uv')\dd{x} \\
&= \int_a^b u'v\dd{x} + \int_a^b uv'\dd{x}
\end{aligned}$$

이다. 우변의 첫 항을 좌변으로 옮기면 된다.
:::

가령 $u = x$, $v = e^x$이면 $\int_0^1 xe^x\dd{x} = e - \int_0^1 e^x\dd{x} = 1$이다. 치환적분에서는 바깥 함수의 연속성이 원시함수의 존재를 보장하는 역할을 한다.

::: 명제 8 (치환적분)
$\varphi : [\alpha,\beta] \rightarrow \mathbb{R}$가 연속미분가능하고 $f$가 $\varphi([\alpha,\beta])$를 포함하는 구간 $I$에서 연속이면

$$\int_\alpha^\beta f\bigl(\varphi(t)\bigr)\varphi'(t)\dd{t} = \int_{\varphi(\alpha)}^{\varphi(\beta)} f(u)\dd{u}$$

이다.
:::

::: 증명
$c \in I$를 하나 잡고 $F(y) = \int_c^y f$라 하자. $f$가 $I$에서 연속이므로 [정리 2](#thm2)에 의해 $F$는 $I$에서 미분가능하고 $F' = f$이다. [§미분, ⁋정리 4](/ko/math/analysis/differentiation#thm4)에 의해 $F\circ\varphi$는 $[\alpha,\beta]$에서 미분가능하고

$$(F\circ\varphi)'(t) = f\bigl(\varphi(t)\bigr)\varphi'(t)$$

이다. 이 함수는 연속함수 $f\circ\varphi$와 $\varphi'$의 곱이므로 연속이고, 따라서 [§Riemann 적분, ⁋정리 6](/ko/math/analysis/riemann_integral#thm6)에 의하여 적분가능하다. [정리 5](#thm5)를 $G = F\circ\varphi$에 적용하면

$$\begin{aligned}
\int_\alpha^\beta f\bigl(\varphi(t)\bigr)\varphi'(t)\dd{t}
&= F\bigl(\varphi(\beta)\bigr) - F\bigl(\varphi(\alpha)\bigr) \\
&= \int_{\varphi(\alpha)}^{\varphi(\beta)} f(u)\dd{u}
\end{aligned}$$

이다. 마지막 등식은 [§Riemann 적분, ⁋명제 16](/ko/math/analysis/riemann_integral#prop16)이다.
:::

[명제 8](#prop8)은 $\varphi$가 단조이거나 일대일일 것을 요구하지 않는다. 요구되는 것은 $f$가 $\varphi$의 치역 전체에서 정의되고 연속이라는 점뿐이다. 가령 $\varphi(t) = t^2$이면 $\int_{-1}^{1} 2te^{t^2}\dd{t} = \int_1^1 e^u\dd{u} = 0$이다.

치환에서 실제로 틀리는 곳은 정리 자체가 아니라 $f(\varphi(t))$를 정리하는 단계이다. $f(x) = \sqrt{1 - x^2}$, $\varphi(t) = \sin t$로 두면 $f(\varphi(t)) = \lvert\cos t\rvert$이다. $[0,\pi/2]$에서는 $\lvert\cos t\rvert = \cos t$이므로 $\int_0^1\sqrt{1-x^2}\dd{x} = \int_0^{\pi/2}\cos^2 t\dd{t} = \pi/4$를 얻는다. 같은 치환을 $[0,\pi]$에 쓰면 $\varphi(0) = \varphi(\pi) = 0$이므로 우변이 $\int_0^0 = 0$이고, 좌변은 $\int_0^\pi\lvert\cos t\rvert\cos t\dd{t} = 0$이다. 여기서 $\lvert\cos t\rvert$를 $\cos t$로 바꿔 $\int_0^\pi\cos^2 t\dd{t} = \pi/2$로 계산하면 $0$과 어긋나는 오류가 된다.

## 적분의 평균값 정리

제1기본정리는 $F'(x_0)$가 $f$의 평균값의 극한임을 보였다. 이 평균이 실제로 $f$의 한 값과 같다는 것이 적분의 평균값 정리이다.

::: 정리 9 (적분의 평균값 정리)
$f$가 $[a,b]$에서 연속이면 $\int_a^b f = f(c)(b - a)$인 $c \in (a,b)$가 존재한다.
:::

::: 증명
$F(x) = \int_a^x f$라 하자. [명제 1](#prop1)에 의해 $F$는 $[a,b]$에서 연속이고, [정리 2](#thm2)에 의해 $(a,b)$에서 $F' = f$이다. [§평균값 정리와 테일러 정리, ⁋정리 3](/ko/math/analysis/mean_value_theorem#thm3)를 $F$에 적용하면 $F(b) - F(a) = F'(c)(b-a)$인 $c \in (a,b)$가 있고, $F(a) = 0$이므로 $\int_a^b f = f(c)(b-a)$이다.
:::

$f$가 연속이라는 가정은 빠질 수 없다. $f = 0$ ($0 \leq x < 1/2$), $f = 1$ ($1/2 \leq x \leq 1$)이면 $\int_0^1 f = 1/2$이지만 $f$의 값은 $0$과 $1$뿐이므로 $f(c) = 1/2$인 $c$가 없다. 연속성은 증명에서 $F' = f$를 얻는 데 쓰인다.

피적분함수에 가중치가 곱해진 경우에도 같은 형태가 성립한다. 다만 이번에는 $c$를 닫힌구간에서 잡는다.

::: 명제 10 (가중 평균값 정리)
$f$가 $[a,b]$에서 연속이고 $g$가 적분가능하며 $g \geq 0$이면, $\int_a^b fg = f(c)\int_a^b g$인 $c \in [a,b]$가 존재한다.
:::

::: 증명
$f$는 연속이므로 [§연속함수의 성질, ⁋따름정리 2](/ko/math/analysis/continuous_functions#cor2)에 의하여 최댓값 $M$과 최솟값 $m$을 갖는다. $g \geq 0$이므로 $mg \leq fg \leq Mg$이고 ($fg$는 [§Riemann 적분, ⁋명제 13](/ko/math/analysis/riemann_integral#prop13)에 의하여 적분가능하다), [§Riemann 적분, ⁋명제 12](/ko/math/analysis/riemann_integral#prop12)의 단조성에 의해

$$m\int_a^b g \leq \int_a^b fg \leq M\int_a^b g$$

이다. $\int_a^b g = 0$이면 $\int_a^b fg = 0$이므로 아무 $c$나 취하면 된다. $\int_a^b g > 0$이면 $\mu = \int_a^b fg\big/\int_a^b g$가 $m \leq \mu \leq M$을 만족한다. $m$과 $M$을 각각 취하는 두 점 사이에 [§연결성과 중간값 정리, ⁋따름정리 4](/ko/math/analysis/connectedness#cor4)를 적용하면 $f(c) = \mu$인 $c \in [a,b]$가 있다.
:::

$g \equiv 1$이면 [정리 9](#thm9)에서 $c$를 닫힌구간으로 넓힌 형태가 된다. $g \geq 0$이라는 가정은 $mg \leq fg \leq Mg$의 부등호 방향을 지키는 데 쓰이며, $g$의 부호가 바뀌면 이 부등식이 성립하지 않는다.

---

**참고문헌**

**[Rud]** W. Rudin, *Principles of mathematical analysis*, 3rd ed., McGraw-Hill, 1976.
