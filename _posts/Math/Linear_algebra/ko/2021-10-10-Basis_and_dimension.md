---
layout: single
date: 2021-10-10
title: "기저와 차원"
categories: [Math / Linear Algebra]
permalink: /ko/math/linear_algebra/basis_and_dimension
header:
    overlay_image: /assets/images/Linear_algebra/Basis_and_dimension.png
    overlay_filter: 0.5
toc: true
toc_sticky: true
comments: true
sidebar: 
    nav: "preliminaries"
excerpt: "Basis and dimension"
lang: ko
weight: 2
---
<div class="notice--warning" markdown="1">

이 글은 현재 수정중입니다.

이 글은 예전에 쓴 글로, 서술 방향이 마음에 들지 않거나 표기법이 마음에 들지 않아 전체적으로 수정이 진행중입니다. 읽으실 때 참고해주세요.

</div>


우리는 지난 글의 마지막 부분에서 $F$-벡터공간 $F[\mathrm{x}]$를 살펴봤다. 그리고, 지나가는 말로 이야기했지만, $F[\mathrm{x}]$의 모든 원소는 집합 $S=\\{1,\mathrm{x},\mathrm{x}^2,\ldots\\}$의 원소들의 일차결합으로 나타낼 수 있다는 것도 살펴보았다. 이는 아주 좋은 성질인데, 이러한 집합이 주어진다면 우리는 벡터공간들의 모든 원소를 생각할 필요 없이, 이 집합의 원소들이 벡터공간의 원소들을 모두 표현해준다 생각하고 $S$만 생각하면 되기 때문이다. 지금 상황에서는 $S$도 무한집합이긴 하지만, 어쨌든 $F[\mathrm{x}]$는 uncountable이므로 $S$보다 훨씬 크다. 

## 생성집합

어쨌든, 이런 상황을 다음과 같이 정의한다.

<div class="definition" markdown="1">

<ins id="df1">**정의 1**</ins> $F$-벡터공간 $V$에 대하여, $V$의 부분집합 $S$가 $V$의 *생성집합*이라는 것은 임의의 $v\in V$에 대하여, 

$$v=\sum_{x\in S}\alpha_ss$$

를 만족하는 스칼라들의 finitely supported family $(\alpha_x)_{x\in S}$가 존재하는 것이다. 

</div>

즉, 일상적인 언어로 풀어쓰자면, $V$의 임의의 원소가 $S$의 원소들의 일차결합으로 항상 표현 가능한 것이다. 이러한 집합이 항상 존재한다는 것은 자명하다. $S=V$로 잡으면 되기 때문이다. 하지만 이는 썩 달가운 상황은 아니다. 우리는 앞서 말했듯 $S$가 $V$보다 좀 작아서, $V$를 보다 쉽게 살펴볼 수 있도록 해 주길 원하기 때문이다. 이 *작다*라는 것을 어떻게 정의할지는 조만간 다시 소개하기로 하고, 이 생성집합을 먼저 살펴보자.

우선 [정의 1](#df1)을 $V$의 임의의 부분공간 $W$로 확장하는 것은 일도 아니다. $W$도 어차피 $F$-벡터공간 구조를 $V$로부터 물려받으므로, 그냥 정의의 *$F$-벡터공간 $V$*를 *$V$의 부분공간 $W$*으로만 바꾸면 된다. 반대로, $V$의 어떤 부분집합 $S$가 주어졌을 때, $S$를 생성집합으로 갖는 $V$의 어떤 부분공간 $W$가 존재하는지는 그렇게까지 자명해보이진 않는다. 

<div class="definition" markdown="1">

<ins id="df2">**정의 2**</ins> $F$-벡터공간 $V$에 대하여, $V$의 부분집합 $S$를 포함하는 $V$의 부분공간 중 가장 작은 것을 $S$에 의해 *생성*된 부분공간이라 하고, $\operatorname{span}S$와 같이 표현한다.

</div>

이 정의 하에서 어렵지 않게 $\operatorname{span}S$가 유일함을 보일 수 있다. 만약 $W,W'$가 [정의 2](#df2)의 조건을 만족하는 두 개의 부분공간이라면, $W'$의 minimality에 의해 $W'\leq W$이고, $W$의 minimality에 의해 $W\leq W'$가 성립하기 때문이다.

하지만, 이 정의가 말이 되려면 다음 보조정리가 필요하다.

<div class="proposition" markdown="1">

<ins id="lem3">**보조정리 3**</ins> $F$-벡터공간 $V$와, $V$의 부분공간들 $\\{W_i\\}\_{i\in I}$ ($i$는 임의의 index set)에 대하여, $W=\bigcap_{i\in I} W_i$는 $V$의 부분공간이다.

</div>
<details class="proof" markdown="1">
<summary>증명</summary>

임의의 $w_1, w_2\in W$에 대하여, $w_1+w_2\in W$임을 보이자. $w_1$과 $w_2$ 각각이 $W$의 원소이므로, *모든* $i\in I$에 대하여 $w_1,w_2$는 $W_i$의 원소이고, 따라서 $w_1+w_2\in W_i$가 모든 $i$에 대해 성립한다. 이제 다시 $W$의 정의에 의해 $w_1+w_2\in W$가 성립한다.

이와 유사하게 임의의 $w\in W$와 $\alpha\in F$에 대하여

$$w\in W\implies w\in W_i\text{ for all $i$}\implies \alpha w\in W_i\text{ for all $i$}\implies \alpha w\in W$$

이므로 $W$는 스칼라곱에 대해서도 닫혀있고, $0\in W$도 자명하므로 $W$는 부분공간이 된다.

</details>

이제, 임의의 $S$에 대하여, *$S$를 포함하는 $V$의 부분공간들의 집합* $\\{W\_i\\}\_{i\in I}$는 공집합이 아니므로 (적어도 $V$를 포함하므로), 교집합 $\bigcap\_{i\in I} W_i$가 잘 정의되고 따라서 [정의 2](#df2) 또한 잘 정의된다. 그런데, 이 정의는 $\operatorname{span}S$의 존재성과 유일성을 보이기엔 좋지만, $\operatorname{span}S$가 정확히 어떻게 생겼는지에 대한 정보는 전혀 주지 않는다. 말하자면 일종의 top-down 방식인 것인데, $\operatorname{span}S$가 어떻게 생겼는지는 $S$부터 시작하는 bottom-up 방식이 조금 더 잘 보여줄 것이다.

<div class="proposition" markdown="1">

<ins id="lem4">**보조정리 4**</ins> $\operatorname{span}S$는 $S$의 원소로 이루어진 임의의 일차결합들의 집합과 같다.

</div>
<details class="proof" markdown="1">
<summary>증명</summary>

증명의 편의상, 잠시 *$S$의 원소로 이루어진 임의의 일차결합들의 집합*을 $\langle S\rangle$으로 표기하자. 그럼, $\langle S\rangle$의 두 원소 $v_1=\sum \alpha_xx$, $v_2=\sum\beta_xx$의 합은

$$v_1+v_2=\sum_{x\in S}(\alpha_x+\beta_x)x\in \langle S\rangle$$

이고, $\alpha v\in \langle S \rangle$가 임의의 $v\in\langle S\rangle$에 대해 성립하는 것 또한 자명하다. $0\in\langle S\rangle$이므로, $\langle S\rangle$ 또한 $S$를 포함하는 $V$의 부분공간이고, 따라서 $\operatorname{span}S$의 minimality에 의해 $\operatorname{span}S\leq \langle S\rangle$이다.

한편, [§Basic definition, 명제 17](/ko/math/linear_algebra/basic_definition#pp17)에 의하여, $S$를 포함하는 임의의 부분공간은 $S$의 원소들의 일차결합 또한 포함해야 하므로 $\langle S\rangle\leq\operatorname{span}S$가 성립한다.

</details>


## 일차독립

우리는 앞서 어떤 부분공간의 생성집합을 정의했다. 하지만, 이미 말했듯 우리는 이 생성집합이 될 수 있는 한 가장 작기를 원한다. 이 *작다*라는 개념을 정의할 때는 좀 주의가 필요하다. 이를 단순히 집합의 크기로 정의하는 것은 약간 부족하다. 예를 들어, 우리는 조만간 $F[\mathrm{x}]$를 생성하는 가장 작은 집합이 $\\{1,\mathrm{x},\mathrm{x}^2,\ldots\\}$인 것을 보일텐데, 이 집합에 $1+\mathrm{x}$을 넣어도 집합의 크기는 변하지 않지만 $1+\mathrm{x}$라는 원소는 원래 집합의 원소들의 일차결합으로 나타날 수 있으므로 사실 별 필요 없는 원소가 된다. 

이 *별 필요 없는 원소*라는 것은 다음과 같이 엄밀하게 정의할 수 있다. 

<div class="definition" markdown="1">

<ins id="df5">**정의 5**</ins> $F$-벡터공간 $V$에 대하여, $V$의 부분집합 $S$가 *일차독립*이라는 것은, 만일 어떤 finitely supported family $(\alpha_x)_{x\in S}$에 대하여

$$\sum_{x\in S} \alpha_xx=0$$

이 성립한다면, 반드시 $\alpha_x=0$이 *모든* $s$에 대해 성립하는 것이다.

</div>

이 정의가 표준적인 정의이긴 하지만, 이것이 어떻게 우리 상황을 해결해주는지는 그렇게 명확하지 않다. 앞선 예시를 우선 살펴보면,

$$0=1\cdot1+1\cdot\mathrm{x}-1\cdot(1+\mathrm{x})$$

가 되므로, 이 집합이 일차독립이 아니라는 것을 알 수 있다. 이런 상황을 *일차종속*이라고 표현하면 좋을 것이다. 더 일반적으로 다음이 성립한다.

<div class="proposition" markdown="1">

<ins id="pp6">**명제 6**</ins> $F$-벡터공간 $V$와 $V$의 임의의 부분집합 $S$에 대하여, $S$가 일차독립인 것은 $V$의 임의의 원소가 많아야 하나의 $S$의 일차결합으로 표현되는 것과 동치이다.

</div>
<details class="proof" markdown="1">
<summary>증명</summary>

우선, 뒤의 조건이 성립한다면, $0\in V$를 $S$의 일차결합으로 표현하는 방법은 많아야 하나일 것이고, 이 방법은 사실

$$0=\sum_{x\in S}0x$$

이다. 따라서 $S$는 일차독립이고, 반대 방향 implication만 보이면 충분하다.

결론에 반하여, $S$가 일차독립이지만, 어떤 $v\in V$에 대하여 $v$가 다음의 두 $S$의 일차결합

$$v=\sum_{x\in S}\alpha_xx=\sum_{x\in S}\beta_xx$$

으로 표현된다 가정하자. 물론, 여기에서 $(\alpha_x)$와 $(\beta_x)$는 각각 finitely supported family이다. 그럼 $0=v-v$이므로,

$$0=v-v=\sum_{x\in S}\alpha_xx-\sum_{x\in S}\beta_xx=\sum_{x\in S}(\alpha_x-\beta_x)x$$

인데, $S$가 일차독립이므로 정의에 의해 $\alpha_x-\beta_x$가 모든 $x\in S$에 대해 $0$이어야 한다. 이는 $\alpha_x=\beta_x$가 모든 $x$에 대해 성립한다는 말이므로, 이는 $\sum\alpha_xx$와 $\sum\beta_xx$가 서로 다른 표현이라는 것에 모순이다. 

</details>

## 벡터공간의 기저

<div class="definition" markdown="1">

<ins id="df7">**정의 7**</ins> $F$-벡터공간 $V$에 대하여, 집합 $\mathcal{B}\subset V$가 $V$의 *기저*라는 것은, $\mathcal{B}$가 일차독립이고, $\operatorname{span}\mathcal{B}=V$인 것이다.

</div>

앞선 [보조정리 4](#lem4), 그리고 [명제 6](#pp6)에 의하여, 이는 정확히 

> $V$의 임의의 원소 $v$가 주어질 때마다, 적당한 finitely supported family $(\alpha\_x)\_{x\in \mathcal{B}}$가 유일하게 존재하여
>
> $$v=\sum_{x\in \mathcal{B}}\alpha_xx.$$  
>

라 할 수 있다. 우리가 스칼라들을 표현할 때는 그리스 소문자를 사용하기로 약속하긴 했지만, 지금같은 상황에서는 $v$가 스칼라들의 family $(\alpha\_x)\_{x\in \mathcal{B}}$를 유일하게 결정해주므로, 이들 계수를 $\alpha_x$ 대신 $v_x$로 적기로 약속한다. 그럼 $F$의 원소들의 (finitely supported) family $(v\_x)\_{x\in \mathcal{B}}$를 벡터 $v$의 *기저 $\mathcal{B}$에 대한 좌표 표현*이라 부르고, $[v]\_\mathcal{B}$와 같이 표기한다. 어렵지 않게 $v\mapsto [v]\_\mathcal{B}$는 $V$와 $F^{\lvert\mathcal{B}\rvert}$간의 bijection임을 보일 수 있다.



몇 가지 예시를 살펴보자.

<div class="example" markdown="1">

<ins id="ex8">**예시 8**</ins> 자명한 $F$-벡터공간 $\\{0\\}$의 기저는 $\emptyset$으로 *정의*한다. 즉, $\\{0\\}$은 이 벡터공간의 기저가 아니다. 왜냐하면, $0=0\cdot 0=1\cdot 0$이기 때문에, $\\{0\\}$은 기저의 원소가 될 수 없기 때문이다.[^1] 이 공간의 부분집합이야 둘 뿐이니 $\\{0\\}$이 기저가 될 수 없다면 남은 선택은 하나뿐인데, $\emptyset$은 과연 $\\{0\\}$을 생성하는가의 문제가 있지만... 이는 그냥 $\sum_{x\in\emptyset}x=0$으로 정의해버리면 된다. 

</div>

물론 $\sum_{x\in\emptyset}x=0$으로 정의하는 것이 조금 걸릴 수는 있지만, 예를 들어 $\bigcap_{i\in\emptyset} X_i$를 전체집합으로 정의하거나, $\bigcup_{i\in \emptyset} X_i$를 공집합으로 정의하는 등의 일을 했던 걸 생각하면 조금은 마음이 편해진다.

<div class="example" markdown="1">

<ins id="ex9">**예시 9**</ins> 이번에는 $F$ 자기 자신을 $F$-벡터공간으로 생각하면, $\\{1\\}$이 $F$의 기저가 된다. 임의의 $\alpha\in F$에 대해서, $\alpha=\alpha\cdot 1$이므로 이 집합은 $F$를 생성하고, 또 $0=\alpha\cdot 1$을 만족하는 $\alpha\in F$는 $\alpha=0$뿐이므로 일차독립 조건도 만족한다.

더 일반적으로, $F$의 0이 아닌 임의의 원소를 하나 가져와서 이를 $x$라 하면, $\\{x\\}$는 $F$의 기저가 된다. $x\neq 0$이므로 $x$의 곱셈에 대한 역원 $x^{-1}$이 존재하며, 따라서 임의의 $\alpha\in F$에 대하여

$$\alpha=(\alpha x^{-1})\cdot x$$

가 성립하며 $0=\alpha\cdot x$를 만족하는 $\alpha$ 또한 $\alpha=0$ 뿐이기 때문이다. 

</div>

두 체 $K\supset F$가 주어졌다 하자. 우리는 $K$가 자연스러운 $F$-벡터공간 구조를 갖는다는 것을 알고 있다. 예를 들어, $K=\mathbb{C}$이고 $\mathbb{R}$인 경우가 그렇다. 이 때, $K=\mathbb{C}$의 $F$-basis를 찾는 것은 그렇게 어렵지 않다. 이 기저는 $\\{1,i\\}$이며, 실제로 임의의 $\mathbb{C}$의 원소는 $a+bi$꼴로 유일하게 표현되는 것을 쉽게 확인할 수 있다.  
하지만 이것이 항상 쉬운 것은 아니다, 예를 들어, $K=\mathbb{R}$, $F=\mathbb{Q}$인 경우가 그렇다. 물론 임의의 실수는 항상 십진법으로 표현 가능하므로, 예를 들어

$$\pi=3\cdot 1+1\cdot\frac{1}{10}+4\cdot\frac{1}{10^2}+\cdots$$

과 같이 표현하면 $\\{10^n\\}_{n=-\infty}^\infty$와 같이 표현할 수 있는 것이 아닌가 싶지만, 위 식은 $10^n$들의 일차결합이 아니었다는 것을 기억하자. 몇 번의 시행착오를 거치고 나면, $\mathbb{Q}$-벡터공간 $\mathbb{R}$의 기저를 찾는 일은 요원해보인다. 하지만:

<div class="proposition" markdown="1">

<ins id="thm10">**정리 10**</ins> 임의의 $F$-벡터공간 $V$는 기저를 갖는다.

</div>

이에 대한 증명은 Zorn's lemma를 사용해야 하므로 (즉 constructive하지 않다는 말이기도 하다), 별도의 글로 남겨두기로 한다.
 
예시를 몇 개만 더 살펴보자. 

<div class="example" markdown="1">

<ins id="ex11">**예시 11**</ins> 임의의 체 $F$에 대하여, 유클리드 $n$-공간 $F^n$은 다음 $n$개의 벡터들

$$\begin{pmatrix}1\\0\\\vdots\\ 0\end{pmatrix},\begin{pmatrix}0\\1\\\vdots\\ 0\end{pmatrix},\ldots,\begin{pmatrix}0\\0\\\vdots\\ 1\end{pmatrix}$$

을 기저로 갖는다. 이 기저들을 $F^n$의 *표준기저*라 부르고, 각각을 $e_1,\ldots,e_n$으로 표기한다. 물론, 표준기저가 있다는 말은 표준이 아닌 수많은 기저들이 있다는 말이기도 하다. 예를 들어,

$$\begin{pmatrix}-1\\0\\\vdots\\ 0\end{pmatrix},\begin{pmatrix}0\\-1\\\vdots\\ 0\end{pmatrix},\ldots,\begin{pmatrix}0\\0\\\vdots\\ -1\end{pmatrix}$$

또한 $F^n$의 기저가 되고, 

$$\begin{pmatrix}0\\1\\\vdots\\ 1\end{pmatrix},\begin{pmatrix}1\\0\\\vdots\\ 1\end{pmatrix},\ldots,\begin{pmatrix}1\\1\\\vdots\\ 0\end{pmatrix}$$

도 $F^n$의 기저가 된다는 것을 정의로부터 확인할 수 있다.

</div>
<div class="example" markdown="1">

<ins id="ex12">**예시 12**</ins> $F[\mathrm{x}]$는 집합 $\\{1,\mathrm{x},\mathrm{x}^2,\ldots\\}$을 기저로 갖는다. 반면, $F[[\mathrm{x}]]$는 이 집합을 기저로 갖지 않는다.  

</div>

## 벡터공간의 차원

[예시 9](#ex9)와 [예시 11](#ex11)을 보자. 우리는 이 예시들로부터, 어떤 벡터공간 $V$의 기저는 유일할 필요가 없다는 것을 알 수 있다. 그런데, 이 예시들을 보면 공통적으로 기저의 원소의 갯수들은 동일하게 유지된다는 것도 확인할 수 있다. 이는 우연이 아니다.

<div class="proposition" markdown="1">

<ins id="thm13">**정리 13**</ins> $F$-벡터공간 $V$에 대하여, $V$의 두 기저 $\mathcal{B}_1$, $\mathcal{B}_2$가 주어졌다면 $\lvert \mathcal{B}_1\rvert=\lvert \mathcal{B}_2\rvert$.

</div>

이 정리는 $\mathcal{B}_1$, $\mathcal{B}_2$가 무한한 경우도 포함한다. 이를 보이기 위해서는 세 단계가 필요하다.

1. 우선, 만일 $V$의 *어떤* 기저가 무한하다면, 다른 기저들도 반드시 무한하며 그 기저의 cardinality는 모두 동일하고,
2. 그러므로 $V$의 어떤 기저가 유한하다면, 다른 기저들도 모두 유한해야 한다.
3. 마지막으로, 만일 $V$의 두 유한한 기저가 주어진다면, 이들 두 기저의 원소의 갯수는 동일하다는 것을 보인다.

물론 이 정리도 지금 증명하자면 못할 것은 없지만, [정리 10](#thm10)과 마찬가지로 이를 증명하기 위해는 약간의 집합론적인 지식이 필요하므로 별도의 글로 분리한다. 다만 마지막 단계는 별다른 배경지식 없이도 증명할 수 있다.

<div class="proposition" markdown="1">

<ins id="lem14">**보조정리 14**</ins> $F$-벡터공간 $V$에 대하여, 만일 $\mathcal{B}_1$과 $\mathcal{B}_2$이 모두 $V$의 기저이고 유한하다면, $\lvert \mathcal{B}_1\rvert=\lvert \mathcal{B}_2\rvert$.

</div>
<details class="proof" markdown="1">
<summary>증명</summary>

$\mathcal{B}_1=\\{v_1,v_2,\ldots, v_m\\}$, 그리고 $\mathcal{B}_2=\\{u_1,u_2,\ldots, u_n\\}$이라 하고, $m=n$임을 보여야 한다. 결론에 반하여 $m>n$이라 하자.

우선 $v_1\in V$이므로, $v_1$은 $u_1$, $u_2$, $\ldots$, $u_n$들의 일차결합으로 나타낼 수 있다. 따라서 [명제 6](#pp6)에 의하여, 집합 $\\{v_1,u_1,u_2,\ldots, u_n\\}$은 일차종속이다. 즉, 모두 0은 아닌 스칼라들 $\beta_1$, $\alpha_1$, $\alpha_2$, $\ldots$, $\alpha_n$이 존재하여

$$\beta_1v_1+\alpha_1u_1+\alpha_2u_2+\cdots+\alpha_n u_n=0\tag{1}$$

이도록 할 수 있다. 여기서 $\beta_1$이 0이 될 수 없음은 자명하다. 만일 $\beta_1=0$이라면 위의 식은 

$$\alpha_1u_1+\alpha_2u_2+\cdots+\alpha_nu_n=0$$

이 되어, $u_1$, $u_2$, $\ldots$, $u_n$이 일차독립이라는 가정에 모순이기 때문이다. 또, 만일 모든 $\alpha_i$가 0이라면 $\beta_1v_1=0$인데, $\beta_1\neq 0$이므로 $v_1=0$이다. 이 경우 $\\{v_1, v_2, \ldots, v_m\\}$은 자명하게 일차종속이게 되므로, 어떤 0이 아닌 $\alpha_i$가 존재한다고 가정하자. 그럼 우리는 위의 식 (1)을 변형하여 다음의 식

$$u_i=\frac{\beta_1}{\alpha_i}v_1-\frac{\alpha_1}{\alpha_i}u_1-\cdots-\frac{\alpha_{i-1}}{\alpha_i}u_{i-1}-\frac{\alpha_{i+1}}{\alpha_i}u_{i+1}-\cdots-\frac{\alpha_n}{\alpha_i}u_n$$

을 얻는다. 따라서 만일 우리가 집합 $\\{v_1, u_1, u_2, \ldots, u_n\\}$에서 $u_i$를 빼더라도 이 집합은 여전히 $V$를 생성한다.  
한편, 이 집합은 일차독립이다. 어떠한 스칼라들 $\beta_1'$, $\alpha_1'$, $\ldots$, $\alpha_n'$에 대하여 

$$\beta_1'v_1+\alpha_1'u_1+\alpha_2'u_2+\cdots+\alpha_{i-1}'u_{i-1}+\alpha_{i+1}'u_{i+1}+\cdots+\alpha_n'u_n=0$$

이라고 한다면, 위에서와 같은 이유로 $\beta_1'\neq 0$이 되고, 따라서 

$$v_1=-\frac{\alpha_1'}{\beta_1'}u_1-\frac{\alpha_2'}{\beta_1'}u_2-\cdots-\frac{\alpha_{i-1}'}{\beta_1'}u_{i-1}-\frac{\alpha_{i+1}'}{\beta_1'}u_{i+1}-\cdots-\frac{\alpha_n'}{\beta_1'}u_n$$

을 식 (1)에 대입하면 우리는 0의 nontrivial한 일차결합을 얻는다. ($u_i$의 계수는 $\alpha_i\neq 0$이므로) 이는 $\\{u_1,u_2,\ldots,u_n\\}$이 일차독립이라는 가정에 모순이다.

따라서 우리는 $V$의 새로운 기저 $\\{v_1,u_1,u_2,\ldots,u_{i-1}, u_{i+1},\ldots, u_n\\}$을 얻었다. 일반성을 잃지 않고, 우리가 없앤 벡터가 $u_n$이었다고 한다면 이렇게 생긴 새 기저는 $\\{v_1, u_1, \ldots, u_{n-1}\\}$이다. 이제 다시 이 기저에 $v_2$를 넣어 $\\{v_2, v_1, u_1, u_2, \ldots, u_n\\}$을 생각하자.

$$\beta_2v_2+\beta_1v_1+\alpha_1u_1+\alpha_2u_2+\ldots+\alpha_{n-1}u_{n-1}=0$$

라 한다면 위와 같은 논리로 $\beta_2\neq 0$이고, $v_2=0$인 경우를 제외한다면 $\beta_1$, $\alpha_1$, $\ldots$, $\alpha_{n-1}$ 중 0이 아닌 계수가 존재한다. 만일 $\beta_1$이 유일한 nonzero coefficient라면, 위의 식은 $\beta_2v_2+\beta_1v_1=0$이 되므로 $\\{v_1,v_2\\}$가 일차종속이므로 증명이 끝난다.  
그렇지 않고 어떠한 $\alpha_i\neq 0$이 존재한다면, 우리는 위와 같은 과정을 반복하여 다시 새로운 기저 $\\{v_2,v_1,u_1,u_2,\ldots,u_{n-2}\\}$를 얻는다.

이 과정을 반복하다보면 두 가지의 가능성이 있다. 

1. 만일 이 과정이 어디에선가 멈춘다면, 

    $$\beta_kv_k+\beta_{k-1}v_{k-1}+\cdots+\beta_1v_1=0$$
    
    이 될 것이므로 $\\{v_1,v_2,\ldots,v_m\\}$은 일차종속이다. 
2. 그렇지 않다면, $n$번을 반복한 후 우리는 원래의 기저 $\\{u_1,u_2,\ldots, u_n\\}$을 새로운 기저 $\\{v_1, v_2, \ldots, v_n\\}$으로 완전하게 교체할 것이다. 이 경우, $v_{n+1}\in V$는 $\\{v_1, v_2, \ldots, v_n\\}$들의 일차결합으로 표현할 수 있으므로 $\\{v_1,v_2,\ldots, v_{n+1}\\}$은 일차종속이고 따라서 $\\{v_1,v_2,\ldots, v_m\\}$ 또한 마찬가지이다. 

어떠한 경우든 $\\{v_1,v_2,\ldots, v_m\\}$는 일차종속이고, 따라서 기저가 될 수 없으므로 모순.

</details>

사실 위 명제의 증명을 찬찬히 들여다보면, 우리는 원하는 것보다 더 강력한 것을 증명했다. 즉,

> 어떤 유한차원 $F$-벡터공간 $V$에 대하여, $V=\operatorname{span}S$를 만족하는 일차독립인 부분집합 $S\subset V$가 존재한다면, $\lvert S'\rvert\geq\lvert S\rvert$인 $V$의 임의의 부분집합 $S'$는 일차종속이다.[^2]

아무튼 위 명제 덕분에 다음을 정의할 수 있게 되었다.

<div class="definition" markdown="1">

<ins id="df15">**정의 15**</ins> $F$-벡터공간 $V$에 대하여, $V$의 기저의 cardinality를 $V$의 *차원*이라 하고, $\operatorname{dim}V$, 혹은 $F$를 강조할 필요가 있을 때는 $\operatorname{dim}_FV$로 적는다. 만일 $\operatorname{dim}V$가 유한이라면, $V$는 *유한차원* 벡터공간이고, 그렇지 않다면 $V$는 *무한차원* 벡터공간이다.

</div>

<div class="example" markdown="1">

<ins id="ex16">**예시 16**</ins> 

1. 자명한 벡터공간 $\\{0\\}$의 기저는 $\emptyset$이므로, 이 공간의 차원은 $\lvert\emptyset\rvert=0$이다.
2. 임의의 체 $F$에 대하여, $F$ 자기 자신은 1차원 $F$-벡터공간이다.
3. 임의의 체 $F$에 대하여, 유클리드 $n$-공간 $F^n$의 차원은 $\operatorname{dim}F^n=n$이다.
4. $\operatorname{dim}_\mathbb{R}\mathbb{C}=2$. 
5. $F[\mathrm{x}]$는 무한차원 벡터공간이다.

</div>

$V$가 유한차원 벡터공간이라는 것이 주어진다면 좋은 일들이 많이 생긴다. 동일한 결과가 무한차원일 때에도 성립하지만, 유한차원으로만 한정해서 생각할 경우 간단하거나, constructive한 방법으로 증명을 할 수 있는 경우도 있고, 혹은 아예 무한차원에서는 성립하지 않고 유한차원에서만 성립하는 명제도 있다. 이인석 교수님의 교재에서는 전자의 경우는 f.d.v.s., 후자의 경우는 **f.d.v.s.**와 같이 적어서 구별하고 있지만, 우리는 그냥 맘 편하게 모든 벡터공간들이 유한차원임을 가정하고 이야기를 진행하고, 무한차원의 이야기가 필요할 때에는 명시적으로 벡터공간이 무한차원임을 밝히기로 한다.

예를 들어, 다음의 명제는 Zorn's lemma를 통해 무한차원인 경우로 확장할 수 있지만 우리는 유한차원인 경우만 한정해서 생각하기로 한다.

<div class="proposition" markdown="1">

<ins id="pp17">**명제 17**</ins> $F$-벡터공간 $V$와 $V$의 임의의 일차독립인 부분집합 $S$에 대하여, $S$를 포함하는 $V$의 기저 $\mathcal{B}$가 존재한다.

</div>
<details class="proof" markdown="1">
<summary>증명</summary>

만약 $\operatorname{span}S=V$라면, 더 이상 증명할 것이 없다. 그렇지 않다면 $v\not\in\operatorname{span}S$인 $v\in V$가 존재한다. 이제 집합 $S_1=S\cup\\{v\\}$이라 하자. 그럼 $S_1$은 일차독립이다. 자명하게 $v\neq0$이며, 이제 $S_1$의 임의의 일차결합 

$$\sum_{x\in S_1} \alpha_xx=\sum_{x\in S}\alpha_xx+\alpha_vv=0$$  

이라 하면, $\alpha_v\neq 0$일 경우 $\alpha_vv$를 이항한 후 $-\alpha_v^{-1}$를 곱해주면 $v$를 $S$의 원소들의 일차결합으로 나타낼 수 있는데, 이는 $v$의 선택에 모순이기 때문이다. 따라서 $\alpha_v=0$이고, 그럼 $S$의 각 원소들은 일차독립이므로 $\alpha_x=0$이 모든 $x\in S$에 대해 성립한다. 따라서, $\alpha_x=0$이 모든 $x\in S_1$에 대해 성립한다.

이제 만일 $\operatorname{span}S_1=V$라면 다시 증명 끝이고, 그렇지 않다면 똑같은 방식으로 $S_2=S_1\cup\\{v'\\}$을 정의하여 반복할 수 있다. 물론 $S_2$가 일차독립이라는 것을 보여야 하지만, $v'$를 $V\setminus\operatorname{span}S_1$에서 뽑아왔기 때문에 이는 위에서 보인 것과 정확하게 같은 논리로 가능하다. 이 과정은 앞선 [보조정리 15](#lem15)에 의해, 많아야 $\dim V$번째 과정 안에 끝나고, 따라서 이 과정이 끝날 때 우리는 원하는 기저 $S_n$을 얻게 된다.[^3] 
</details>


한편, 이와 비슷한 느낌으로, 다음이 성립한다.

<div class="proposition" markdown="1">

<ins id="pp18">**명제 18**</ins> $F$-벡터공간 $V$와, $V$를 생성하는 부분집합 $S$에 대하여, $S$의 어떤 부분집합은 $V$의 기저가 된다.

</div>
<details class="proof" markdown="1">
<summary>증명</summary>

증명의 기본 아이디어는 [명제 17](#pp17)과 동일하지만, $S$는 무한집합일 수 있으므로 (대표적으로 $S=V$로 잡을 수도 있다.) $S$에서 원소를 하나하나 빼가는 것으로는 증명이 성립하지 않는다.

대신, [명제 17](#pp17)의 증명과 동일하게, 처음을 $S_0=\emptyset$으로 시작하자. ($\operatorname{span}\emptyset=\\{0\\}$이므로 make sense한다) 임의의 $S\setminus\operatorname{span}S_0$의 원소를 하나 택해 $x_1$이라 하자. 그 후 $S_1=S_0\cup\\{x_1\\}=\\{x_1\\}$이라 한 후, $S\setminus \operatorname{span}S_1$의 원소 $x_2$를 또 택하고...  
이 과정이 $V$의 기저로 끝나기 위해서는 $S\setminus\operatorname{span}S_n$이, $\operatorname{span}S_n=V$가 아닌 한은 공집합이 아니어야 한다. $S\setminus\operatorname{span}S_n=\emptyset$인 $n$이라 하자. 그럼 $S\setminus\operatorname{span}S_n=\emptyset$으로부터 $S\subset\operatorname{span}S_n$이다. 이제 양 변에 다시 $\operatorname{span}$을 취하자. [보조정리 4](#lem4)에 의하여, 이 때 포함관계는 바뀌지 않으며, $\operatorname{span}S_n$은 이미 부분공간이므로 [§Basic definition, 명제 17](/ko/math/linear_algebra/basic_definition#pp17)에 의하여 $\operatorname{span}\operatorname{span}S_n=\operatorname{span}S_n$이다. 즉,

$$V=\operatorname{span}S\subset\operatorname{span}\operatorname{span}S_n=\operatorname{span}S_n$$

이 되어, $\operatorname{span}S_n=V$여야 한다. 

</details>

마지막으로 두 개의 조금 일반적인 예시를 살펴보자.

<div class="example" markdown="1">

<ins id="ex19">**예시 19**</ins> 두 $F$-벡터공간 $V$, $W$가 주어졌다 하자. 그럼 이들의 *곱* $V\times W$는 임의의 $v\in V$, $w\in W$에 대하여 $(v,w)$의 꼴로 나타나는 벡터들의 벡터공간이다. 이들의 연산은 각각

$$(v_1, w_1)+(v_2,w_2)=(v_1+v_2,w_1+w_2),\quad\alpha(v,w)=(\alpha v,\alpha w)$$

으로 주어진다. 어렵지 않게, 만일 $\mathcal{B}_1$, $\mathcal{B}_2$가 각각 $V$, $W$의 기저들이라면, $V\times W$의 부분집합

$$\mathcal{B}=\{(x, y): x\in \mathcal{B}_2\text{ and }y\in \mathcal{B}_2\}$$

이 $V\times W$의 기저가 되는 것을 확인할 수 있다. 특히, 만일 $V$, $W$가 모두 유한차원이라면 $V\times W$도 그러하고 $\dim(V\times W)$는 $(\dim V)+(\dim W)$와 같게 된다.

</div>

<div class="example" markdown="1">

<ins id="ex20">**예시 20**</ins> 이번에는 $F$-벡터공간 $V$가 주어졌다 하고, $V$의 두 부분공간 $W_1$, $W_2$가 주어졌다 하자. 그럼 $V$의 부분공간 $W_1+W_2$는 

> 두 부분공간 $W_1$, $W_2$를 포함하는 $V$의 부분공간 중 가장 작은 것 (참고. [보조정리 3](#lem3))

으로 정의된다. 식으로 쓰자면 $W_1+W_2=\operatorname{span}(W_1\cup W_2)$라 할 수 있다. 

이제 $W_1,W_2$가 모두 유한차원이라 가정하고, $\dim(W_1+W_2)$를 계산해보자. 만약 $\mathcal{B}_1$, $\mathcal{B}_2$가 $W_1,W_2$ 각각의 기저라면, $\mathcal{B}_1\cup\mathcal{B}_2$가 $W_1+W_2$를 생성하는 것은 자명하다. 어차피 $W_1+W_2$의 임의의 원소는 항상 $W_1$의 원소들과 $W_2$의 원소들의 일차결합으로 주어지고, $W_1$의 원소들과 $W_2$의 원소들 각각은 다시 $\mathcal{B}_1$과 $\mathcal{B}_2$의 원소들의 일차결합으로 주어지기 때문이다. 문제는 $\mathcal{B}_1\cup\mathcal{B}_2$가 일차독립인 부분집합이라는 보장이 없기 때문에 $\dim(W_1+W_2)=\dim W_1+\dim W_2$이라고 주장할 수 없다는 것이다.[^4]

따라서, 약간의 trick이 필요하다. $W_1,W_2$이 각각 $m$, $n$차원이라 하고, $W_1\cap W_2$가 $k$차원이라 하자. 그럼 $W_1\cap W_2$의 기저 $\mathcal{B}\_0=\\{x_1,\ldots, x_k\\}$가 존재한다. 이 집합은 $W_1$과 $W_2$의 일차독립인 부분집합이므로, 이 집합을 포함하는 $W_1$과 $W_2$의 기저가 각각 존재한다. 이들을 $\mathcal{B}\_1$과 $\mathcal{B}\_2$라 하자. 그럼 

$$\mathcal{B}_1=\{y_1,\ldots, y_m\},\quad \mathcal{B}_2=\{z_1,\ldots, z_n\},\qquad y_1=z_1=x_1,\ldots, y_k=z_k=x_k$$

라 할 수 있다. 이제, 앞선 논의에 의해 다음의 집합 

$$\mathcal{B}_1\cup\mathcal{B}_2=\{x_1=y_1,\ldots, x_k=y_k, \quad y_{k+1}, \ldots, y_m,\quad z_{k+1},\ldots, z_n\}$$

은 $W_1+W_2$를 생성한다. 뿐만 아니라 이 집합은 일차독립이다. 이를 보이기 위해

$$\alpha_1x_1+\cdots+\alpha_kx_k+\beta_{k+1}y_{k+1}+\cdots+\beta_{m}y_m+\gamma_{k+1}z_{k+1}+\cdots+\gamma_{n}z_n=0\tag{2}$$

이라 하자. $\alpha_i=\beta_i+\gamma_i$를 만족하는 임의의 스칼라들 $\beta_i$, $\gamma_i$ ($i\leq k$)들에 대하여, 

$$\beta_1y_1+\cdots+\beta_ky_k+\beta_{k+1}y_{k+1}+\cdots+\beta_{m}y_m=-\gamma_1z_1-\cdots-\gamma_kz_k-\gamma_{k+1}z_{k+1}-\cdots-\gamma_{n}z_n$$

으로 적으면 좌변은 $W_1$의 원소, 우변은 $W_2$의 원소이므로 이 공통의 벡터는 $W_1\cap W_2$의 원소이다. $\mathcal{B}\_0$이 $W_1\cap W_2$의 기저이므로, 적당한 스칼라들 $\alpha_i'$들을 다시 잡아

$$\beta_1y_1+\cdots+\beta_my_m=\alpha_1'x_1+\cdots+\alpha_k'x_k=-\gamma_1z_1-\cdots-\gamma_nz_n$$

로 적을 수 있다. 그런데 첫째 등식의 경우, $\alpha_i'x_i$들을 다시 좌변으로 넘겨서 $\beta_iy_i$들과 합쳐주면

$$(\beta_1-\alpha_1')y_1+\cdots+(\beta_k-\alpha_k')y_k+\beta_{k+1}y_{k+1}+\cdots+\beta_my_m=0$$

이 되므로, $\mathcal{B}\_1$의 일차독립성에 의해 계수들이 모두 0이고, 특히 $\beta_{k+1}=\cdots=\beta_m=0$이다. 마찬가지로 둘째 등식에서 $\gamma_{k+1}=\cdots=\gamma_n=0$이고, 그럼 (2)에서 남는 식은 $\alpha_1x_1+\cdots+\alpha_kx_k=0$뿐인데 $x_1,\ldots,x_k$는 $W_1\cap W_2$의 기저이므로 다시 일차독립성에 의해 이들도 모두 0이다. 즉, $\mathcal{B}\_1\cup\mathcal{B}\_2$는 $W_1+W_2$를 생성하는 일차독립인 부분집합이고 따라서 $W_1+W_2$의 기저이다. 이제

$$\dim(W_1+W_2)=\lvert\mathcal{B}_1\cup\mathcal{B}_2\rvert=\lvert\mathcal{B}_1\rvert+\lvert\mathcal{B}_2\rvert-\lvert\mathcal{B}_0\rvert=\dim W_1+\dim W_2-\dim(W_1\cap W_2).$$

</div>

---
**Reference**

**[Goc]** M.S. Gockenbach, *Finite-dimensional linear algebra*, Discrete Mathematics and its applications, Taylor&Francis, 2011.

---

[^1]: 이는 자명한 벡터공간 뿐만 아니라 다른 곳에서도 마찬가지.
[^2]: 위 증명의 표기법대로라면, $S=\mathcal{B}\_1$, $S'=\mathcal{B}\_2$.
[^3]: 사실은 정확히 $n=\dim V-\lvert S\rvert$일 때 끝나겠지만. 
[^4]: 그리고 우변의 $\dim W_1+\dim W_2$라는 식이 나오는 과정도 탐탁잖다. 이 식은 $\lvert\mathcal{B}_1\cup\mathcal{B}_2\rvert=\lvert\mathcal{B}_1\rvert+\lvert\mathcal{B}_2\rvert$가 성립해야 하니...
