---
title: "실수의 완비성"
description: "실수를 순서체로 두고 상한 성질(최소상계 성질)을 공리로 받아들인다. 상한의 ε-특성화를 증명하고, 유리수 집합에서 이 성질이 어떻게 깨지는지 계산한 뒤, 상한 성질로부터 아르키메데스 성질, 유리수의 조밀성, 양의 제곱근의 존재를 유도한다."
excerpt: "순서체, 상한 성질, 상한의 ε-특성화, 아르키메데스 성질, 유리수의 조밀성, 제곱근의 존재"

categories: [Math / Analysis]
permalink: /ko/math/analysis/completeness_of_reals
sidebar: 
    nav: "analysis-ko"

date: 2026-06-02
weight: 1

published: false

---

유리수 $\mathbb{Q}$는 사칙연산과 대소관계를 모두 갖추고 있으므로 대수적으로나 순서의 측면에서나 부족한 것이 없어 보인다. 그러나 $x^2=2$를 만족하는 유리수는 없고, 이는 $\mathbb{Q}$ 안에서 $x^2<2$인 수들을 아무리 위로 밀어 올려도 도달할 점이 $\mathbb{Q}$ 안에 없다는 뜻이다. 해석학에서 극한, 최댓값, 중간값, 적분의 존재를 보장하는 모든 정리는 실수에는 이런 빈틈이 없다는 사실에 기댄다. 이 글에서는 그 사실을 상한 성질이라는 공리로 적고, 공리가 실제로 무엇을 보장하는지 증명으로 확인한다.

## 순서체

::: 정의 1
체 $F$ 위의 total order $\leq$가 다음 두 조건을 만족하면 $(F,\leq)$를 *순서체*라 한다.

1. $a\leq b$이면 모든 $c\in F$에 대해 $a+c\leq b+c$이다.
2. $0\leq a$이고 $0\leq b$이면 $0\leq ab$이다.
:::

$\mathbb{Q}$와 $\mathbb{R}$은 모두 순서체이다. 이 정의에서 $1>0$, 모든 $a$에 대해 $a^2\geq 0$, $0<a<b$이면 $a^2<b^2$, $c>0$이면 $a<b$에서 $ac<bc$ 같은 통상의 부등식 규칙이 따르고, 아래에서는 이 규칙들을 따로 언급하지 않고 쓴다. 순서체의 공리만으로는 $\mathbb{Q}$와 $\mathbb{R}$을 구별할 수 없다. 둘을 가르는 것은 다음 절의 공리 하나이다.

## 상한과 상한 성질

::: 정의 2
순서체 $F$의 subset $S$와 원소 $M\in F$에 대하여, 모든 $s\in S$에 대해 $s\leq M$이면 $M$을 $S$의 *upper bound<sub>상계</sub>*라 하고, upper bound가 존재하면 $S$는 위로 유계라 한다. $S$의 upper bound 가운데 가장 작은 것이 존재하면 이를 $S$의 *supremum<sub>상한</sub>* 또는 *least upper bound<sub>최소상계</sub>*라 하고 $\sup S$로 적는다. Lower bound와 *infimum* $\inf S$는 부등호를 반대로 하여 같은 방식으로 정의한다.
:::

$\sup S$가 존재하더라도 $S$의 원소일 필요는 없다. $S=[0,1)$의 upper bound는 $1$ 이상의 수 전체이므로 $\sup S=1$이지만 $1\notin S$이고, $S$에는 최댓값이 없다. $\sup S\in S$일 때에만 $\sup S$가 $S$의 최댓값 $\max S$가 된다. 또 $S=\emptyset$이면 모든 수가 upper bound이므로 가장 작은 것이 없고, 위로 유계가 아닌 집합은 upper bound 자체가 없다. 그래서 아래의 공리는 공집합이 아니고 위로 유계인 집합에 대해서만 말한다.

::: 정의 3 (상한 성질)
순서체 $F$가 다음을 만족하면 $F$는 *상한 성질<sub>least upper bound property</sub>*을 갖는다고 하고 *완비*라 한다. 공집합이 아니고 위로 유계인 모든 $S\subseteq F$는 $F$ 안에 $\sup S$를 갖는다.
:::

실수체 $\mathbb{R}$은 상한 성질을 갖는 순서체로 정의한다. 이 글의 모든 결과는 $\mathbb{R}$이 이 공리를 만족한다는 사실만 사용한다.

하한에 대한 대응 성질은 따로 공리로 둘 필요가 없다. $S$가 공집합이 아니고 아래로 유계이면 $-S=\{-s\mid s\in S\}$는 위로 유계이다. $S$의 lower bound $m$에 대해 $-m$이 $-S$의 upper bound이기 때문이다. 그러면 $\alpha=\sup(-S)$가 존재하고, $m$이 $S$의 lower bound인 것과 $-m$이 $-S$의 upper bound인 것이 동치이므로 $-\alpha$가 $S$의 가장 큰 lower bound, 곧 $\inf S$이다.

## 상한의 ε-특성화

[정의 2](#def2)는 "가장 작은 upper bound"라는 최소성 조건을 담고 있어 직접 쓰기 불편하다. 실제 증명에서는 다음 형태로 바꾸어 쓴다.

::: 명제 4 (상한의 ε-특성화)
$S\subseteq\mathbb{R}$이 공집합이 아니라 하고 $\alpha\in\mathbb{R}$이라 하자. $\alpha=\sup S$인 것은 다음 두 조건이 모두 성립하는 것과 동치이다.

1. 모든 $s\in S$에 대해 $s\leq\alpha$이다.
2. 모든 $\varepsilon>0$에 대해 $s>\alpha-\varepsilon$인 $s\in S$가 존재한다.
:::

::: 증명
$\alpha=\sup S$라 하자. 조건 1은 $\alpha$가 upper bound라는 것 자체이다. $\varepsilon>0$이 주어졌다고 하자. $\alpha-\varepsilon<\alpha$이고 $\alpha$가 가장 작은 upper bound이므로 $\alpha-\varepsilon$은 upper bound가 아니다. 즉 $s\leq\alpha-\varepsilon$가 성립하지 않는 $s\in S$가 있고, 이는 $s>\alpha-\varepsilon$이라는 뜻이다.

역으로 두 조건이 성립한다고 하자. 조건 1에 의해 $\alpha$는 upper bound이다. $\beta<\alpha$인 $\beta$가 upper bound라고 가정하고 $\varepsilon=\alpha-\beta>0$으로 잡으면, 조건 2에 의해 $s>\alpha-\varepsilon=\beta$인 $s\in S$가 존재하여 $\beta$가 upper bound라는 가정에 모순이다. 따라서 모든 upper bound는 $\alpha$ 이상이고 $\alpha=\sup S$이다.
:::

조건 2에서 $\varepsilon$이 임의의 양수라는 점이 핵심이다. 임의의 $\varepsilon>0$에 대해 $\alpha-\varepsilon$이 upper bound가 아니라는 것은 $\alpha$보다 작은 수는 모두 upper bound가 아니라는 말과 같다. 한 번 지나가는 $\varepsilon$에 대해서만 성립하는 주장으로는 이 동치가 얻어지지 않는다. 이 명제는 이후의 모든 글에서 수열의 극한과 상한을 연결할 때 쓰인다.

## 유리수의 불완비성

상한 성질은 $\mathbb{Q}$에서 성립하지 않는다. 다음 계산은 그 실패가 어떤 구조로 일어나는지를 보여 준다.

::: 예시 5 ($\mathbb{Q}$에서 상한을 갖지 않는 집합)
$S=\{x\in\mathbb{Q}\mid x^2<2\}$는 공집합이 아니고($1\in S$) 위로 유계이지만($2$가 upper bound이다) $\mathbb{Q}$ 안에 상한을 갖지 않는다.

먼저 $q^2=2$인 $q\in\mathbb{Q}$가 없음을 보인다. $q=p/r$이 기약분수(자연수 $p,r$)이고 $p^2=2r^2$이라 하자. 그러면 $p^2$이 짝수이므로 $p$가 짝수이다. $p=2t$를 대입하면 $r^2=2t^2$이어서 $r$도 짝수가 되고, 이는 기약분수라는 가정에 모순이다. 이로부터 $\mathbb{Q}$의 양수 $q$는 $q^2<2$이거나 $q^2>2$이다.

이제 양의 유리수 $q$에 대해

$$q'=q-\frac{q^2-2}{q+2}=\frac{2q+2}{q+2}$$

로 정의하자. 이 식은 $q'$이 $q$보다 $(q^2-2)/(q+2)$만큼 작아지도록 잡은 것이고, 분모 $q+2$는 $q'^2-2$를 계산했을 때 $q^2-2$의 배수가 되도록 고른 것이다. 실제로 계산하면

$$\begin{aligned}
q'^2-2 &= \frac{(2q+2)^2-2(q+2)^2}{(q+2)^2} \\
&= \frac{2q^2-4}{(q+2)^2} = \frac{2(q^2-2)}{(q+2)^2}
\end{aligned}$$

이다. 따라서 $q'$은 양의 유리수이고, $q^2<2$이면 $q'>q$이면서 $q'^2<2$이며, $q^2>2$이면 $q'<q$이면서 $q'^2>2$이다.

$S$가 $\mathbb{Q}$ 안에 상한 $\beta$를 가졌다고 하자. $1\in S$이므로 $\beta\geq 1>0$이고, 위에서 $\beta^2\neq 2$이다. $\beta^2<2$이면 $\beta'>\beta$이면서 $\beta'^2<2$이므로 $\beta'\in S$가 되어 $\beta$가 upper bound라는 데 모순이다. $\beta^2>2$이면 $\beta'<\beta$이고 $\beta'^2>2$이다. 이때 $\beta'$은 $S$의 upper bound이다. 실제로 $x\in S$가 양수이면 $x^2<2<\beta'^2$에서 $x<\beta'$이고, $x\leq 0$이면 $x<\beta'$은 자명하다. 이는 $\beta$가 가장 작은 upper bound라는 데 모순이다.
:::

같은 집합 $S$를 $\mathbb{R}$ 안에서 보면 상한을 가지며, 그 값이 아래에서 구성하는 $\sqrt{2}$이다. $\mathbb{Q}$에서 $S$의 upper bound 전체는 $\sqrt{2}$보다 큰 유리수들의 집합이고, 이 집합에는 가장 작은 원소가 없다. 완비성은 이 "있어야 할 최솟값이 빠져 있는" 상황이 $\mathbb{R}$에서는 일어나지 않는다는 공리이다.

## 아르키메데스 성질

자연수가 한없이 커진다는 사실은 당연해 보이지만 순서체의 공리에서 나오지 않는다. 이것을 증명하는 데 상한 성질이 필요하다.

::: 정리 6 (Archimedean property)
임의의 실수 $x$에 대하여 $n>x$인 자연수 $n$이 존재한다. 따라서 임의의 $\varepsilon>0$에 대해 $1/n<\varepsilon$인 자연수 $n$이 존재한다.
:::

::: 증명
$\mathbb{N}$이 위로 유계라고 가정하자. $\mathbb{N}$은 공집합이 아니므로 $\alpha=\sup\mathbb{N}$이 존재한다. $\alpha-1<\alpha$이므로 $\alpha-1$은 upper bound가 아니고, $n>\alpha-1$인 자연수 $n$이 있다. 그러면 자연수 $n+1$이 $n+1>\alpha$를 만족하여 $\alpha$가 upper bound라는 데 모순이다. 따라서 $\mathbb{N}$은 위로 유계가 아니고, 임의의 $x$는 $\mathbb{N}$의 upper bound가 될 수 없으므로 $n>x$인 $n\in\mathbb{N}$이 있다. 둘째 주장은 $x=1/\varepsilon$에 적용하면 $n>1/\varepsilon$, 곧 $1/n<\varepsilon$을 얻는다.
:::

이 증명에서 $\alpha-1$을 쓴 것은 $\mathbb{N}$이 $1$씩 커지는 집합이어서 $\alpha-1$ 바로 위에 원소가 있으면 $\alpha$를 넘는 원소가 만들어지기 때문이다. [정리 6](#thm6)의 둘째 형태는 $\varepsilon$-논증에서 "$\varepsilon$보다 작은 $1/n$을 잡는다"는 단계에 그대로 쓰인다.

다음 예시는 상한 성질을 빼면 [정리 6](#thm6)이 실제로 무너짐을 보인다.

::: 예시 7 (Archimedean property가 없는 순서체)
$\mathbb{R}$ 위의 rational function field $\mathbb{R}(x)$에서 $f=p/q$ ($p,q$는 polynomial, $q\neq 0$)를 $p$와 $q$의 최고차 계수의 부호가 같을 때 양수로 정의하면 $\mathbb{R}(x)$는 순서체가 된다. 이 순서에서 모든 자연수 $n$에 대해 $x-n$의 최고차 계수는 $1>0$이므로 $x>n$이다. 즉 $\mathbb{N}$은 $x$를 upper bound로 가지며 위로 유계이다. 그러나 $\mathbb{N}$은 상한을 갖지 않는다. $\beta$가 upper bound이면 모든 $n$에 대해 $n+1\leq\beta$이므로 $\beta-1$도 upper bound이고, $\beta-1<\beta$이어서 가장 작은 upper bound가 없기 때문이다.
:::

따라서 Archimedean property는 순서체 일반의 성질이 아니라 완비성의 귀결이다. 역은 성립하지 않는다. $\mathbb{Q}$는 Archimedean property를 갖지만 완비가 아니다.

## 유리수의 조밀성

::: 정리 8 (유리수의 density)
실수 $a<b$에 대하여 $a<q<b$인 유리수 $q$가 존재한다.
:::

::: 증명
$b-a>0$이므로 [정리 6](#thm6)에 의하여 $1/n<b-a$인 자연수 $n$을 잡을 수 있다. 이는 $nb-na>1$이라는 뜻이다. 이제 $na$ 바로 위의 정수를 찾는다. [정리 6](#thm6)에서 $n'>-na$인 자연수 $n'$이 있고, 정수 집합 $\{k\in\mathbb{Z}\mid k>na\}$은 $-n'$을 하계로 갖는 공집합이 아닌 집합이므로 최솟값 $m$을 갖는다. $m$이 최소이므로 $m-1\leq na$이고, 따라서

$$na<m\leq na+1<nb$$

이다. 각 변을 $n$으로 나누면 $a<m/n<b$이다.
:::

$n$을 $1/n<b-a$로 고르는 이유는, 간격이 $1/n$인 점 $m/n$ 가운데 길이가 $b-a$인 구간에 반드시 하나가 들어가려면 그 간격이 구간 길이보다 작아야 하기 때문이다. [정리 8](#thm8)을 $(a,q)$와 같은 구간에 되풀이하여 적용하면 $(a,b)$ 안에 유리수가 무한히 많음을 얻는다. 무리수에 대해서도 같은 결론이 성립한다. 아래 절에서 $\sqrt{2}$가 무리수임을 확인하고 나면, $a<b$에 대해 $a-\sqrt{2}<q<b-\sqrt{2}$인 유리수 $q$를 잡아 $q+\sqrt{2}\in(a,b)$가 무리수임을 얻는다. 유리수와 무리수 모두 $\mathbb{R}$ 안에서 *dense*하다.

## 제곱근의 존재

[예시 5](#ex5)에서 $\mathbb{Q}$에는 없던 $\sqrt{2}$가 $\mathbb{R}$에는 존재한다. 같은 집합의 상한을 취하는 것이 증명의 구조이다.

::: 정리 9 (양의 제곱근의 존재)
임의의 실수 $c>0$에 대하여 $\alpha^2=c$인 양의 실수 $\alpha$가 유일하게 존재한다. 이를 $\sqrt{c}$로 적는다.
:::

::: 증명
$S=\{x>0\mid x^2<c\}$라 하자. $x_0=c/(1+c)$는 $0<x_0<1$이고 $x_0<c$이므로 $x_0^2<x_0<c$이어서 $x_0\in S$이다. 또 $x\geq 1+c$이면 $x\geq 1$에서 $x^2\geq x\geq 1+c>c$이므로 $x\notin S$이다. 즉 $1+c$는 $S$의 upper bound이다. [정의 3](#def3)에 의해 $\alpha=\sup S$가 존재하고, $x_0\in S$이므로 $\alpha>0$이다. $\alpha^2<c$와 $\alpha^2>c$를 각각 배제한다.

$\alpha^2<c$라 하자. $0<h<1$인 $h$에 대하여 $h^2<h$이므로

$$\begin{aligned}
(\alpha+h)^2 &= \alpha^2+2\alpha h+h^2 \\
&< \alpha^2+(2\alpha+1)h
\end{aligned}$$

이다. 우변이 $c$ 이하가 되도록 $h=\min\{1/2,(c-\alpha^2)/(2\alpha+1)\}$로 잡으면 $(2\alpha+1)h\leq c-\alpha^2$이어서 $(\alpha+h)^2<c$이다. 따라서 $\alpha+h\in S$이고 $\alpha+h>\alpha$이므로 $\alpha$가 upper bound라는 데 모순이다. ($h$에 $1/2$ 같은 상한을 둔 것은 $h^2<h$를 쓰기 위해 $h<1$이 필요하기 때문이다.)

$\alpha^2>c$라 하자. $k=(\alpha^2-c)/(2\alpha)$로 두면 $k>0$이고 $k<\alpha^2/(2\alpha)=\alpha/2$이므로 $\alpha-k>0$이다. $k^2>0$이므로

$$\begin{aligned}
(\alpha-k)^2 &= \alpha^2-2\alpha k+k^2 \\
&> \alpha^2-2\alpha k = c
\end{aligned}$$

이다. $x\in S$이면 $x^2<c<(\alpha-k)^2$이고 $x,\alpha-k$가 모두 양수이므로 $x<\alpha-k$이다. 따라서 $\alpha-k$는 $\alpha$보다 작은 upper bound가 되어 $\alpha$가 가장 작은 upper bound라는 데 모순이다. $k$는 $2\alpha k=\alpha^2-c$가 되도록, 곧 $(\alpha-k)^2$의 일차 근사가 정확히 $c$가 되도록 고른 값이다.

두 경우가 모두 불가능하므로 $\alpha^2=c$이다. $0<\alpha<\beta$이면 $\alpha^2<\beta^2$이므로 $\alpha^2=\beta^2=c$인 서로 다른 양수는 없고, 유일성이 성립한다.
:::

$c=2$인 경우가 $\sqrt{2}$의 존재이다. [예시 5](#ex5)에서 $\mathbb{Q}$에는 $\alpha^2=2$인 수가 없음을 보였으므로 $\sqrt{2}$는 무리수이다. 이 정리는 $\sqrt{2}$의 존재가 체의 공리나 순서의 공리가 아니라 상한 성질에서 나온다는 것을 보여 준다. 같은 방식으로 $n$제곱근의 존재도 증명할 수 있으나 $h$와 $k$를 고르는 계산이 길어진다.

다음 글에서는 이 글의 [명제 4](#prop4)와 [정리 6](#thm6)을 이용하여 수열의 수렴을 정의하고 다룬다.

---

**참고문헌**

**[Rud]** W. Rudin, *Principles of mathematical analysis*, 3rd ed., McGraw-Hill, 1976.
