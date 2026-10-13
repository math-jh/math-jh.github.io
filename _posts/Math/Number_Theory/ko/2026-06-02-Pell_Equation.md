---
title: "펠 방정식"
description: "양의 정수 d가 제곱수가 아닐 때 x²−dy²=1의 정수해를 √d의 연분수 전개로 모두 구한다. 모든 해가 fundamental solution의 거듭제곱임을 보이고, x²−dy²=−1이 풀리는 것이 연분수 주기의 홀짝과 동치임을 증명한다."
excerpt: "펠 방정식의 fundamental solution, 해 전체의 구조, 음의 펠 방정식과 주기의 홀짝"

categories: [Math / Number Theory]
permalink: /ko/math/number_theory/pell_equation
sidebar: 
    nav: "number_theory-ko"

date: 2026-06-02
weight: 12

published: false

---

양의 정수 $d$에 대하여 방정식 $x^2-dy^2=1$의 정수해 $(x,y)$를 구하는 문제를 생각한다. $(\pm 1,0)$은 항상 해이며, 이를 자명한 해라 부른다. $d=m^2$이 제곱수이면 $(x-my)(x+my)=1$에서 두 인수가 모두 $1$ 또는 모두 $-1$이어야 하므로 $y=0$이 되어 자명한 해뿐이다. 그러므로 이 글에서 $d$는 제곱수가 아닌 양의 정수로 두며, 이때 $\sqrt{d}$는 무리수이고 $d\geq 2$이다.

해 $(x,y)$는 $x^2-dy^2=1$을 $x/y-\sqrt{d}=1/(y(x+y\sqrt{d}))$로 다시 쓰면 $x/y$가 $\sqrt{d}$를 분모 $y$에 비해 아주 정확하게 근사한다는 뜻이다. 그런 근사는 [§연분수, ⁋정리 8](/ko/math/number_theory/continued_fractions#thm8){: data-lid="k91k5" }에 의하여 점근분수가 주는 것이므로, 해를 점근분수 가운데에서 찾을 수 있다. 이 글은 이 관찰을 끝까지 밀고 가서 해를 점근분수로 완전히 분류하고, 그 결과로 해 전체의 구조와 $x^2-dy^2=-1$의 풀이 가능성을 얻는다.

## Norm과 해의 곱셈

수 $\alpha=x+y\sqrt{d}$ ($x,y\in\mathbb{Z}$) 전체를 $\mathbb{Z}[\sqrt{d}]$로 쓴다. $\sqrt{d}$가 무리수이므로 $\alpha$를 이렇게 적는 방법은 하나뿐이다. $\alpha$의 켤레를 $\overline{\alpha}=x-y\sqrt{d}$, norm을 $N(\alpha)=\alpha\overline{\alpha}=x^2-dy^2$으로 쓰면, $\alpha\mapsto\overline{\alpha}$는 $\mathbb{Q}(\sqrt{d})$의 덧셈과 곱셈을 보존하므로 $N(\alpha\beta)=N(\alpha)N(\beta)$이다. 따라서 $x^2-dy^2=1$의 해는 $N(\alpha)=1$인 $\alpha\in\mathbb{Z}[\sqrt{d}]$와 일대일로 대응하고, 두 해의 곱은 다시 해이다. $N(\alpha)=1$이면 $\alpha^{-1}=\overline{\alpha}$이므로 해의 역도 해이다.

$N(\alpha)=1$이고 $\alpha>1$이면 $0<\overline{\alpha}=\alpha^{-1}<1$이므로 $x=(\alpha+\overline{\alpha})/2>0$이고 $y=(\alpha-\overline{\alpha})/(2\sqrt{d})>0$이다. 거꾸로 $x,y\geq 1$인 해는 $\alpha>1$이다. 이런 해를 *양의 해*라 부른다. 해 $(x,y)$가 주어지면 $x+y\sqrt{d}$, $x-y\sqrt{d}$, $-x+y\sqrt{d}$, $-x-y\sqrt{d}$가 각각 $\alpha$, $\alpha^{-1}$, $-\alpha^{-1}$, $-\alpha$에 해당하므로, 모든 해는 양의 해의 값 $\beta>1$에 대한 $\pm\beta^{\pm 1}$ 꼴이다. $N(\alpha)=-1$인 경우에도 같은 방식으로 $\overline{\alpha}=-\alpha^{-1}$이고, $\alpha>1$이면 $x=(\alpha-\alpha^{-1})/2>0$, $y=(\alpha+\alpha^{-1})/(2\sqrt{d})>0$이다.

## 연분수 전개의 보조 성질

$\sqrt{d}$의 연분수 전개를 $x_0=\sqrt{d}$, $a_k=\lfloor x_k\rfloor$, $x_{k+1}=1/(x_k-a_k)$로 쓰고, 점근분수를 $p_k/q_k=[a_0;a_1,\ldots,a_k]$로 쓴다. 다음 두 사실을 쓴다. 첫째, [§연분수, ⁋명제 3](/ko/math/number_theory/continued_fractions#prop3){: data-lid="jbi3y" }에서 보인 대로 $p_{-1}=1$, $p_0=a_0$, $q_{-1}=0$, $q_0=1$과 점화식 $p_k=a_kp_{k-1}+p_{k-2}$, $q_k=a_kq_{k-1}+q_{k-2}$ 아래 $p_kq_{k-1}-p_{k-1}q_k=(-1)^{k-1}$이 성립한다. 특히 $p_k/q_k$는 기약분수이고 $q_k\geq q_{k-1}$이다. 둘째, [§연분수, ⁋명제 5](/ko/math/number_theory/continued_fractions#prop5){: data-lid="hkdch" }에서 보인 대로 무리수 $\alpha$의 전개에서 $k\geq 1$에 대해 $\alpha=(x_kp_{k-1}+p_{k-2})/(x_kq_{k-1}+q_{k-2})$이다.

먼저 $\sqrt{d}$의 완전 몫 $x_k$의 구조를 정리한다. $\overline{x_k}$는 $x_k\in\mathbb{Q}(\sqrt{d})$의 켤레이다.

::: 보조정리 1
정수 $P_k,Q_k$가 존재하여 $x_k=(P_k+\sqrt{d})/Q_k$이고, $(P_0,Q_0)=(0,1)$,
$$P_{k+1}=a_kQ_k-P_k,\qquad Q_{k+1}=\frac{d-P_{k+1}^2}{Q_k}$$
이다. 또 $k\geq 1$이면 $x_k>1$, $-1<\overline{x_k}<0$, $0<Q_k<2\sqrt{d}$, $-\sqrt{d}<P_k<\sqrt{d}$이다.
:::

::: 증명
$k$에 대한 귀납으로 $x_k=(P_k+\sqrt{d})/Q_k$이고 $Q_k\mid d-P_k^2$임을 보인다. $k=0$은 자명하다. $x_k$가 이 꼴이면
$$x_{k+1}=\frac{1}{x_k-a_k}=\frac{Q_k}{\sqrt{d}-P_{k+1}}=\frac{Q_k(\sqrt{d}+P_{k+1})}{d-P_{k+1}^2}$$
이다. 여기서 $P_{k+1}=a_kQ_k-P_k$로 놓았다. $P_{k+1}\equiv-P_k\pmod{Q_k}$이므로 $d-P_{k+1}^2\equiv d-P_k^2\equiv 0\pmod{Q_k}$이고, 따라서 $Q_{k+1}=(d-P_{k+1}^2)/Q_k$는 정수이다. 또 $Q_{k+1}Q_k=d-P_{k+1}^2$이므로 $Q_{k+1}\mid d-P_{k+1}^2$이다.

부등식을 보인다. $k\geq 1$이면 $x_k=1/(x_{k-1}-a_{k-1})>1$이다. 켤레를 취하면 $\overline{x_{k+1}}=1/(\overline{x_k}-a_k)$이다. $\overline{x_0}=-\sqrt{d}<0$이고, $\overline{x_k}<0$이면 $a_k\geq 1$이므로 $\overline{x_k}-a_k<-1$이고 $\overline{x_{k+1}}\in(-1,0)$이다. 따라서 모든 $k\geq 1$에서 $-1<\overline{x_k}<0$이다. 이제 $x_k-\overline{x_k}=2\sqrt{d}/Q_k$인데, $k\geq 1$에서 좌변은 $1$보다 크므로 $Q_k>0$이고 $Q_k<2\sqrt{d}$이다. 마지막으로 $P_k+\sqrt{d}=Q_kx_k>0$이고 $P_k-\sqrt{d}=Q_k\overline{x_k}<0$이므로 $-\sqrt{d}<P_k<\sqrt{d}$이다.
:::

$Q_k$는 점근분수의 norm과 직접 연결된다.

::: 보조정리 2
모든 $k\geq 1$에 대하여 $p_{k-1}^2-dq_{k-1}^2=(-1)^kQ_k$이다.
:::

::: 증명
$\sqrt{d}=(x_kp_{k-1}+p_{k-2})/(x_kq_{k-1}+q_{k-2})$의 분모를 없애고 $Q_k$를 곱한 뒤 $Q_kx_k=P_k+\sqrt{d}$를 대입하면
$$\sqrt{d}\bigl(P_kq_{k-1}+Q_kq_{k-2}+\sqrt{d}q_{k-1}\bigr)=P_kp_{k-1}+Q_kp_{k-2}+\sqrt{d}p_{k-1}$$
이다. $\sqrt{d}$가 무리수이고 $P_k,Q_k,p_i,q_i$가 정수이므로 유리수 부분과 $\sqrt{d}$의 계수를 따로 비교할 수 있어
$$dq_{k-1}=P_kp_{k-1}+Q_kp_{k-2},\qquad p_{k-1}=P_kq_{k-1}+Q_kq_{k-2}$$
를 얻는다. 첫째 식에 $q_{k-1}$, 둘째 식에 $p_{k-1}$을 곱해 빼면
$$p_{k-1}^2-dq_{k-1}^2=Q_k\bigl(p_{k-1}q_{k-2}-p_{k-2}q_{k-1}\bigr)=Q_k(-1)^{k-2}=(-1)^kQ_k$$
이다.
:::

$Q_k=1$이 되는 지표가 주기를 결정한다.

::: 보조정리 3
$Q_k=1$인 $k\geq 1$이 존재한다. 그런 가장 작은 $k$를 $\ell$이라 하면, $k\geq 1$에 대하여 $Q_k=1$인 것은 $\ell\mid k$인 것과 동치이다. 또 $a_\ell=2a_0$이고 $x_{j+\ell}=x_j$ ($j\geq 1$)이다.
:::

::: 증명
먼저 $k\geq 1$에서 $Q_k=1$이면 $x_k=a_0+\sqrt{d}$임을 보인다. $Q_k=1$이면 $x_k=P_k+\sqrt{d}$이고 $-1<\overline{x_k}=P_k-\sqrt{d}<0$이다. 즉 정수 $P_k$가 $(\sqrt{d}-1,\sqrt{d})$에 있으므로 $P_k=\lfloor\sqrt{d}\rfloor=a_0$이다. 이때 $a_k=\lfloor a_0+\sqrt{d}\rfloor=2a_0$이고 $x_{k+1}=1/(a_0+\sqrt{d}-2a_0)=1/(\sqrt{d}-a_0)=x_1$이다. 따라서 $x_{k+j}=x_j$ ($j\geq 1$)이고, $\sqrt{d}$가 무리수이므로 $(P,Q)$의 표현이 유일하여 $Q_{k+j}=Q_j$이다.

존재를 보인다. [보조정리 1](#lem1){: data-lid="9bhmb" }에 의하여 $k\geq 1$에서 쌍 $(P_k,Q_k)$는 유한 개의 값만 가지므로 $x_i=x_j$인 $1\leq i<j$가 있다. $k\geq 2$에 대하여 $x_{k-1}=a_{k-1}+1/x_k$이고 $-1<\overline{x_{k-1}}=a_{k-1}+1/\overline{x_k}<0$이므로 $a_{k-1}$은 $-1/\overline{x_k}$의 정수부분이다. 즉 $x_k$가 $x_{k-1}$을 결정한다. 이를 되풀이하면 $x_1=x_{m+1}$ ($m=j-i\geq 1$)을 얻는다. 그럼 $x_m-a_m=1/x_{m+1}=1/x_1=\sqrt{d}-a_0$이므로 $x_m=(a_m-a_0)+\sqrt{d}$이고 $Q_m=1$이다.

$\ell$을 $Q_k=1$인 가장 작은 $k\geq 1$이라 하면, 위에서 $a_\ell=2a_0$이고 $x_{j+\ell}=x_j$ ($j\geq 1$)이다. 따라서 $Q_{j+\ell}=Q_j$이고 귀납적으로 $Q_{m\ell}=Q_\ell=1$이다. 거꾸로 $Q_k=1$이고 $k=m\ell+r$ ($0\leq r<\ell$)이면, $r>0$일 때 $x_k=x_r$이어서 $Q_r=1$이 되고 $\ell$의 최소성에 모순이므로 $r=0$이다.
:::

[보조정리 3](#lem3){: data-lid="yg3cj" }에서 $\sqrt{d}=[a_0;\overline{a_1,\ldots,a_{\ell-1},2a_0}]$이고 $\ell$은 최소 주기이다. 이 증명이 $\sqrt{d}$의 전개가 순환함을 보여 주므로 [§연분수, ⁋정리 11](/ko/math/number_theory/continued_fractions#thm11){: data-lid="zb0yv" }을 따로 인용할 필요가 없다.

::: 예시 4
$d=14$이면 $a_0=3$이고 $(P_0,Q_0)=(0,1)$에서 [보조정리 1](#lem1){: data-lid="r5b33" }의 점화식을 따라 계산한다. $P_1=3$, $Q_1=(14-9)/1=5$이고 $x_1=(3+\sqrt{14})/5\approx 1.35$이므로 $a_1=1$이다. $P_2=1\cdot 5-3=2$, $Q_2=(14-4)/5=2$이고 $x_2=(2+\sqrt{14})/2\approx 2.87$이므로 $a_2=2$이다. $P_3=2\cdot 2-2=2$, $Q_3=(14-4)/2=5$이고 $x_3=(2+\sqrt{14})/5\approx 1.15$이므로 $a_3=1$이다. $P_4=1\cdot 5-2=3$, $Q_4=(14-9)/5=1$이므로 $\ell=4$이고 $a_4=6=2a_0$이다. 즉 $\sqrt{14}=[3;\overline{1,2,1,6}]$이다. 점근분수는 $3/1$, $4/1$, $11/3$, $15/4$이고, [보조정리 2](#lem2){: data-lid="zzjbu" }에 따라 $p_{k-1}^2-14q_{k-1}^2$은 차례로 $-5$, $2$, $-5$, $1$이다. 실제로 $9-14=-5$, $16-14=2$, $121-126=-5$, $225-224=1$이다.
:::

## 해와 점근분수

::: 정리 5
$d$가 제곱수가 아닌 양의 정수이고 $\ell$이 $\sqrt{d}$의 연분수 전개의 최소 주기이면, 양의 정수 $x,y$에 대하여 $x^2-dy^2=\pm 1$인 것은 어떤 $k\geq 1$, $\ell\mid k$에 대하여 $(x,y)=(p_{k-1},q_{k-1})$인 것과 동치이고, 이때 $x^2-dy^2=(-1)^k$이다.
:::

::: 증명
$\ell\mid k$이면 [보조정리 3](#lem3){: data-lid="xx88g" }에서 $Q_k=1$이므로 [보조정리 2](#lem2){: data-lid="3vxfn" }에서 $p_{k-1}^2-dq_{k-1}^2=(-1)^k$이다.

거꾸로 양의 정수 $x,y$가 $x^2-dy^2=\pm 1$을 만족한다고 하자. 식에서 $\gcd(x,y)=1$이다. 먼저 $x+y\sqrt{d}>2y$임을 보인다. 부호가 $+1$이면 $x>y\sqrt{d}>y$이다. 부호가 $-1$이면 $x^2=dy^2-1\geq 2y^2-1\geq y^2$이므로 $x\geq y$이다. 어느 경우든 $x+y\sqrt{d}>y+y\sqrt{2}>2y$이다. 따라서
$$\left\lvert\frac{x}{y}-\sqrt{d}\right\rvert=\frac{\lvert x^2-dy^2\rvert}{y(x+y\sqrt{d})}<\frac{1}{2y^2}$$
이고, [§연분수, ⁋정리 8](/ko/math/number_theory/continued_fractions#thm8){: data-lid="nxjwt" }에 의하여 $x/y$는 $\sqrt{d}$의 점근분수 $p_j/q_j$ ($j\geq 0$)이다. $x/y$와 $p_j/q_j$가 모두 분모가 양수인 기약분수이므로 $x=p_j$, $y=q_j$이다. $k=j+1$로 두면 [보조정리 2](#lem2){: data-lid="yo2cm" }에서 $(-1)^kQ_k=x^2-dy^2=\pm 1$이고 $Q_k>0$이므로 $Q_k=1$이다. [보조정리 3](#lem3){: data-lid="n71vj" }에서 $\ell\mid k$이고, 부호는 $(-1)^k$이다.
:::

특히 $\ell$이 짝수이면 양의 해는 모두 부호 $+1$이고, $\ell$이 홀수이면 $k$가 홀수인 배수에서 $-1$, 짝수인 배수에서 $+1$이 나온다. 어느 경우에도 $k=\ell$ 또는 $k=2\ell$에서 $x^2-dy^2=1$의 양의 해가 있으므로, 자명하지 않은 해는 언제나 존재한다.

## Fundamental solution과 해 전체의 구조

$x^2-dy^2=1$의 양의 해의 값 $\alpha=x+y\sqrt{d}$ 중 $\alpha\leq M$인 것은 $x,y\leq M$이므로 유한 개뿐이다. 양의 해가 존재하므로 값이 가장 작은 양의 해 $(x_1,y_1)$이 있고, 이를 *fundamental solution<sub>기본해</sub>*라 부르고 $\varepsilon=x_1+y_1\sqrt{d}$로 쓴다. [정리 5](#thm5){: data-lid="89pzy" }의 점근분수에서 $p_k$가 $k\geq 1$에서 강증가하고 $q_k$가 감소하지 않으므로 $p_{k-1}+q_{k-1}\sqrt{d}$는 $k$에 대해 강증가한다. 따라서 $\varepsilon$은 부호 $+1$인 가장 작은 $k$의 점근분수에서 나온다. 즉 $\ell$이 짝수이면 $(x_1,y_1)=(p_{\ell-1},q_{\ell-1})$이고, $\ell$이 홀수이면 $(x_1,y_1)=(p_{2\ell-1},q_{2\ell-1})$이다. [예시 4](#ex4){: data-lid="jtgoc" }에서 $d=14$의 fundamental solution는 $(15,4)$이다.

::: 정리 6
$\varepsilon=x_1+y_1\sqrt{d}$가 fundamental solution이면 $x^2-dy^2=1$의 정수해는 정확히 $x+y\sqrt{d}=\pm\varepsilon^n$ ($n\in\mathbb{Z}$)이고, 이 표현은 유일하다.
:::

::: 증명
$N(\varepsilon^n)=1$이므로 $\pm\varepsilon^n$은 해이다. $\varepsilon>1$이므로 $\varepsilon^n$은 $n$에 대해 강증가하여 표현은 유일하다.

$\alpha>1$인 해 $\alpha$가 $\varepsilon$의 거듭제곱임을 보인다. $\varepsilon^n\leq\alpha<\varepsilon^{n+1}$인 정수 $n\geq 1$이 있다. 이때 $\beta=\alpha\varepsilon^{-n}=\alpha\overline{\varepsilon}^{n}$은 $\mathbb{Z}[\sqrt{d}]$의 원소이고 $N(\beta)=1$이며 $1\leq\beta<\varepsilon$이다. $\beta>1$이면 $\beta$는 $\varepsilon$보다 작은 양의 해가 되어 $\varepsilon$의 최소성에 모순이므로 $\beta=1$이고 $\alpha=\varepsilon^n$이다. 앞 절에서 모든 해는 양의 해의 값 $\beta>1$에 대한 $\pm\beta^{\pm 1}$이었고, $\beta=1$인 해는 $\pm 1$이므로 모든 해는 $\pm\varepsilon^n$ ($n\in\mathbb{Z}$)이다.
:::

양의 해는 $n\geq 1$에 대한 $x_n+y_n\sqrt{d}=\varepsilon^n$이므로 $\varepsilon^{n+1}=(x_1+y_1\sqrt{d})(x_n+y_n\sqrt{d})$를 전개해 $\sqrt{d}$의 계수를 비교하면
$$x_{n+1}=x_1x_n+dy_1y_n,\qquad y_{n+1}=x_1y_n+y_1x_n$$
을 얻는다. $d=14$이면 $(15,4)$에서 $(15\cdot 15+14\cdot 4\cdot 4,\ 2\cdot 15\cdot 4)=(449,120)$이 되고, 이는 [정리 5](#thm5){: data-lid="rqpyi" }의 $k=8$ 점근분수 $p_7/q_7$이다.

## 음의 펠 방정식

방정식 $x^2-dy^2=-1$은 $x^2-dy^2=1$과 달리 항상 풀리지는 않는다. 우선 $d\equiv 0$ 또는 $3\pmod 4$이면 풀리지 않는다. $x^2+1=dy^2$에서 $d\equiv 0\pmod 4$이면 $x^2\equiv-1\pmod 4$가 되어 불가능하다. $d\equiv 3\pmod 4$이면 $y$가 짝수일 때 $x^2\equiv-1\equiv 3\pmod 4$이고, $y$가 홀수일 때 $x^2+1\equiv 3\pmod 4$인데 $x^2+1$은 $4$로 나눈 나머지가 $1$ 또는 $2$이므로 역시 불가능하다. 정확한 판정은 연분수 주기의 홀짝이 준다.

::: 정리 7
$d$가 제곱수가 아닌 양의 정수이고 $\ell$이 $\sqrt{d}$의 연분수의 최소 주기라 하자.

1. $x^2-dy^2=-1$이 정수해를 갖는 것은 $\ell$이 홀수인 것과 동치이다.
2. $\ell$이 홀수이면 $x^2-dy^2=-1$의 양의 해 중 값이 가장 작은 것을 $\eta=p_{\ell-1}+q_{\ell-1}\sqrt{d}$로 쓸 때 $\varepsilon=\eta^2$이고, 이 방정식의 모든 해는 $x+y\sqrt{d}=\pm\eta^{2n+1}$ ($n\in\mathbb{Z}$)이다.
:::

::: 증명
1. 정수해가 있으면 $y\neq 0$이고($x^2=-1$은 불가능), $d\geq 2$이므로 $x\neq 0$이다. 따라서 $(\lvert x\rvert,\lvert y\rvert)$는 양의 해이다. [정리 5](#thm5){: data-lid="zi7zv" }에서 이는 $k$가 $\ell$의 홀수인 배수인 점근분수에서만 나오므로 $\ell$이 홀수이다. 거꾸로 $\ell$이 홀수이면 $k=\ell$에서 해가 있다.

2. [정리 5](#thm5){: data-lid="88790" }에서 양의 해의 값은 $k$에 대해 강증가하므로 가장 작은 것은 $k=\ell$의 $\eta=p_{\ell-1}+q_{\ell-1}\sqrt{d}$이고, 부호 $+1$인 가장 작은 것은 $k=2\ell$이므로 $\varepsilon=p_{2\ell-1}+q_{2\ell-1}\sqrt{d}>\eta$이다. $\eta^2$은 norm이 $1$이고 $1$보다 크므로 양의 해이며 $\eta^2\geq\varepsilon$이다. 한편 $N(\eta)=-1$이므로 $\eta^{-1}=-\overline{\eta}\in\mathbb{Z}[\sqrt{d}]$이고, $\varepsilon/\eta$는 norm이 $-1$이고 $1$보다 큰 $\mathbb{Z}[\sqrt{d}]$의 원소여서 앞 절에서 본 대로 양의 해이다. $\eta$의 최소성에서 $\varepsilon/\eta\geq\eta$, 즉 $\varepsilon\geq\eta^2$이다. 따라서 $\varepsilon=\eta^2$이다.

norm이 $-1$인 임의의 해에서 $\beta=\lvert x\rvert+\lvert y\rvert\sqrt{d}$로 두면 $\beta$는 양의 해이고, 원래의 해는 $\pm\beta$ 또는 $\pm\overline{\beta}=\mp\beta^{-1}$이다. $\beta\eta$는 norm이 $1$이고 $1$보다 크므로 [정리 6](#thm6){: data-lid="r9jwe" }에서 $\beta\eta=\varepsilon^m=\eta^{2m}$ ($m\geq 1$)이고, $\beta=\eta^{2m-1}$이다. 따라서 모든 해는 $\pm\eta^{2n+1}$ 꼴이다. 거꾸로 이 수들은 norm이 $(-1)^{2n+1}=-1$이다.
:::

$\ell$이 홀수일 때 fundamental solution $(p_{2\ell-1},q_{2\ell-1})$은 $\eta=p+q\sqrt{d}$ ($p=p_{\ell-1}$, $q=q_{\ell-1}$)에 대해 $x_1=p^2+dq^2$, $y_1=2pq$이다. 부호 $-1$을 처음 만났을 때 멈추고 fundamental solution로 착각하기 쉬우므로, $\ell$이 홀수인 경우에는 $k=\ell$에서 얻은 값을 제곱해야 한다. 가령 $d=13$이면 $\sqrt{13}=[3;\overline{1,1,1,1,6}]$이고 $\ell=5$이므로 $\eta=18+5\sqrt{13}$이고 $18^2-13\cdot 5^2=324-325=-1$이다. fundamental solution는 $\eta^2=(324+325)+180\sqrt{13}=649+180\sqrt{13}$이다.

::: 예시 8
$d=34$는 $34\equiv 2\pmod 4$이므로 위의 mod $4$ 조건에 걸리지 않지만 $x^2-34y^2=-1$은 해가 없다. $a_0=5$이고 $(P_k,Q_k)$는 $(5,9)$, $(4,2)$, $(4,9)$, $(5,1)$로 이어져 $\sqrt{34}=[5;\overline{1,4,1,10}]$, $\ell=4$이다. 점근분수 $5/1$, $6/1$, $29/5$, $35/6$의 norm $x^2-34y^2$은 차례로 $-9$, $2$, $-9$, $1$이고, $\ell$이 짝수이므로 [정리 7](#thm7){: data-lid="ta8ul" }에서 $-1$은 나타나지 않는다. fundamental solution는 $35+6\sqrt{34}$이다 ($35^2-34\cdot 36=1225-1224=1$).
:::

## Fundamental solution이 거대한 경우

fundamental solution의 크기는 $d$에 대해 규칙적으로 증가하지 않는다. $d=60$의 fundamental solution는 $(31,4)$이고, $d=62$는 $(63,8)$, $d=63$은 $(8,1)$로 모두 작지만 그 사이의 $d=61$에서는 폭발한다.

::: 예시 9
$d=61$이면 $a_0=7$이고 $\sqrt{61}=[7;\overline{1,4,3,1,2,2,1,3,4,1,14}]$이며 $\ell=11$로 홀수이다. [정리 7](#thm7){: data-lid="g92sc" }에서 $x^2-61y^2=-1$은 풀리고, $k=11$의 점근분수가 $\eta=29718+3805\sqrt{61}$을 준다. 실제로 $29718^2-61\cdot 3805^2=-1$이다. fundamental solution는 $\eta^2$이므로
$$x_1=29718^2+61\cdot 3805^2=1766319049,\qquad y_1=2\cdot 29718\cdot 3805=226153980$$
이고, $1766319049^2-61\cdot 226153980^2=1$이다. 이 값은 $k=22$의 점근분수 $p_{21}/q_{21}$이다. $\ell=11$이 홀수이므로 부호 $+1$은 $k=22$에서야 처음 나타나고, $\eta$ 자체도 $x$좌표가 $3$만 정도이다. $x^2-61y^2=1$을 작은 $y$부터 대입해서 풀려 하면 $y$가 $2$억을 넘을 때까지 해가 나오지 않는다.
:::

---

**참고문헌**

**[OL]** 오정환·이준복, *기초 정수론*, 경문사, 2012.
