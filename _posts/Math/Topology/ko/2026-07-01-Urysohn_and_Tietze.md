---
title: "Urysohn 보조정리와 Tietze 확장정리"
description: "정규공간에서 서로소인 닫힌집합을 분리하는 연속함수의 존재(Urysohn 보조정리)를 dyadic 유리수 구성으로 증명하고, 이를 이용해 Tietze 확장정리와 Urysohn 거리화정리를 얻는다."
excerpt: "Urysohn's lemma, the Tietze extension theorem, and the Urysohn metrization theorem"

categories: [Math / Topology]
permalink: /ko/math/topology/urysohn_and_tietze
sidebar: 
    nav: "topology-ko"

date: 2026-07-01
last_modified_at: 2026-07-01
weight: 16.4

published: false

---

## 분리공리와 연속함수

앞선 글에서 우리는 위상공간이 점이나 닫힌집합을 얼마나 잘 분리하는지에 따라 여러 층위의 separation axiom을 도입하였다. ([§하우스도르프 공간, ⁋정의 3](/ko/math/topology/Hausdorff_spaces#def3)) 이들 조건은 그 자체로는 열린집합의 존재를 요구하는 순수하게 위상적인 진술에 지나지 않는다. 그러나 위상공간을 다루는 실제 상황에서 우리가 진정으로 다루고자 하는 대상은 공간 위에서 정의된 연속함수이며, separation axiom의 힘은 이러한 조건이 서로소인 닫힌집합을 실제로 갈라놓는 연속함수를 만들어 낼 때 비로소 드러난다.

이 점을 명확히 하자. [§하우스도르프 공간, ⁋정의 3](/ko/math/topology/Hausdorff_spaces#def3)에서 두 부분집합 $A,B$가 연속함수로 분리가능하다는 것은 연속함수 $f:X\rightarrow\mathbb{R}$이 존재하여 $A\subseteq f^{-1}(\{0\})$이고 $B\subseteq f^{-1}(\{1\})$인 것으로 정의하였다. 이는 근방으로 분리가능하다는 조건보다 훨씬 강하다. 근방에 의한 분리는 두 집합을 감싸는 서로소인 열린집합만을 요구하지만, 연속함수에 의한 분리는 두 집합 사이의 모든 중간 단계를 연속적으로 이어 주는 실숫값 척도를 요구하기 때문이다.

이 글의 목표는 normal space에서 서로소인 닫힌집합이 언제나 연속함수로 분리가능함을 보이는 것이다. 이것이 Urysohn 보조정리이며, 여기에서 파생되는 Tietze 확장정리와 Urysohn 거리화정리는 일반위상수학에서 연속함수의 존재를 다루는 가장 기본적인 도구가 된다. 우리는 [§하우스도르프 공간, ⁋정의 3](/ko/math/topology/Hausdorff_spaces#def3)의 용어를 따라, 서로소인 두 닫힌집합이 언제나 근방으로 분리가능한 공간을 *normal space<sub>정규공간</sub>*라 부른다. 이 정의에는 $T_1$ 조건이 포함되지 않으므로, normal이라는 조건만으로는 점이 닫혀 있을 필요조차 없다는 점에 유의한다.

## Urysohn 보조정리

Urysohn 보조정리의 증명은 정규성을 반복적으로 사용하여 두 닫힌집합 사이를 촘촘하게 채우는 열린집합들의 사슬을 만들고, 각 점이 이 사슬 안으로 처음 들어가는 지점을 실숫값으로 읽어 내는 데에 있다. 그 핵심은 다음의 보간 보조정리로, 이것이 곧 정규성을 열린집합의 언어로 다시 서술한 것이다.

::: 보조정리 1
Normal space $X$에서 닫힌집합 $C$와 열린집합 $U$가 $C\subseteq U$를 만족한다 하자. 그럼 열린집합 $V$가 존재하여

$$C\subseteq V\subseteq\cl(V)\subseteq U$$

가 성립한다.
:::
::: 증명
$C$와 $X\setminus U$는 서로소인 두 닫힌집합이다. $X$가 normal이므로 이들을 분리하는 서로소인 열린집합 $V\supseteq C$와 $W\supseteq X\setminus U$가 존재한다. $V\cap W=\emptyset$이므로 $V\subseteq X\setminus W$이고, $X\setminus W$는 닫힌집합이므로 $\cl(V)\subseteq X\setminus W$이다. 한편 $X\setminus U\subseteq W$로부터 $X\setminus W\subseteq U$를 얻으므로

$$C\subseteq V\subseteq\cl(V)\subseteq X\setminus W\subseteq U$$

가 성립한다.
:::

역으로 임의의 닫힌집합과 그를 포함하는 열린집합 사이에 위와 같은 $V$가 항상 끼어들 수 있는 공간은 normal임을 같은 논증을 되짚어 확인할 수 있다. 즉 [보조정리 1](#lem1)의 조건은 정규성과 동치이다. 우리는 이 보간 성질을 dyadic 유리수로 색인된 사슬을 세우는 데에 반복 적용할 것이다.

::: 정리 2
(Urysohn's lemma) Normal space $X$와 서로소인 두 닫힌집합 $A,B\subseteq X$가 주어졌다 하자. 그럼 연속함수 $f:X\rightarrow[0,1]$이 존재하여 모든 $a\in A$에 대해 $f(a)=0$이고 모든 $b\in B$에 대해 $f(b)=1$이다.
:::
::: 증명
구간 $[0,1]$에 속하는 dyadic 유리수들의 집합

$$D=\{k/2^n\mid n\geq 0,\ 0\leq k\leq 2^n\}$$

을 생각하자. 우리는 각 $r\in D$마다 열린집합 $U_r$을 정의하되, 다음 성질을 유지하고자 한다.

$$r<s\implies\cl(U_r)\subseteq U_s\tag{$\ast$}$$

먼저 $U_1:=X\setminus B$로 둔다. 이는 $A$를 포함하는 열린집합이다. 닫힌집합 $A\subseteq U_1$에 [보조정리 1](#lem1)을 적용하여 열린집합 $U_0$을 잡아 $A\subseteq U_0\subseteq\cl(U_0)\subseteq U_1$이 성립하도록 한다.

이제 분모가 $2^n$인 dyadic 유리수들에 대한 $U_r$이 성질 $(\ast)$를 만족하도록 정의되었다 가정하고, 새로 등장하는 $r=(2j+1)/2^{n+1}$을 처리하자. 이 $r$은 이미 정의된 두 연속한 값 $p=j/2^n$과 $q=(j+1)/2^n$ 사이에 있으며 $\cl(U_p)\subseteq U_q$가 성립한다. 닫힌집합 $\cl(U_p)$와 이를 포함하는 열린집합 $U_q$에 다시 [보조정리 1](#lem1)을 적용하여 열린집합 $U_r$을 잡아

$$\cl(U_p)\subseteq U_r\subseteq\cl(U_r)\subseteq U_q$$

가 성립하도록 한다. 이렇게 하면 $(\ast)$가 유지된 채로 모든 $r\in D$에 대한 $U_r$이 정의된다.

이제 함수 $f:X\rightarrow[0,1]$을

$$f(x)=\inf\{r\in D\mid x\in U_r\}$$

로 정의하되, $x$가 어떤 $U_r$에도 속하지 않는 경우 그 값을 $1$로 약속한다. $D\subseteq[0,1]$이므로 $f$는 $[0,1]$로 값을 갖는다. 임의의 $a\in A$는 $U_0$에 속하므로 $f(a)=0$이고, 임의의 $b\in B$는 모든 $r$에 대해 $U_r\subseteq U_1=X\setminus B$이므로 어떤 $U_r$에도 속하지 않아 $f(b)=1$이다.

$f$의 연속성을 보이기 위해 다음 두 관찰을 확인한다. 첫째, $x\in\cl(U_r)$이면 $f(x)\leq r$이다. 실제로 $s>r$인 임의의 $s\in D$에 대하여 $(\ast)$에 의해 $\cl(U_r)\subseteq U_s$이므로 $x\in U_s$이고, 따라서 $f(x)\leq s$가 모든 $s>r$에 대해 성립하여 $f(x)\leq r$이다. 둘째, $x\notin U_r$이면 $f(x)\geq r$이다. 실제로 $s<r$인 임의의 $s\in D$에 대하여 $(\ast)$에 의해 $U_s\subseteq\cl(U_s)\subseteq U_r$이므로 $x\notin U_s$이고, 따라서 $f(x)$의 정의에 등장하는 하한은 $r$ 미만의 값을 포함하지 않아 $f(x)\geq r$이다.

이제 $x_0\in X$를 고정하고 $y_0=f(x_0)$을 포함하는 임의의 열린구간 $(c,d)$가 주어졌다 하자. $D$가 $[0,1]$에서 조밀하므로 $c<p<y_0<q<d$를 만족하는 dyadic 유리수 $p,q\in D$를 잡을 수 있다. (단 $y_0=0$인 경우에는 $p$를 생략하고, $y_0=1$인 경우에는 $q$를 생략한다.) 이제

$$V=U_q\setminus\cl(U_p)$$

라 두면 $V$는 열린집합이다. $f(x_0)<q$이므로 어떤 $r<q$에 대해 $x_0\in U_r\subseteq U_q$이고, $f(x_0)>p$이므로 첫째 관찰의 대우에 의해 $x_0\notin\cl(U_p)$이다. 따라서 $x_0\in V$이다. 끝으로 임의의 $x\in V$에 대하여, $x\in U_q$이므로 첫째 관찰에서 $f(x)\leq q<d$이고, $x\notin\cl(U_p)\supseteq U_p$이므로 둘째 관찰에서 $f(x)\geq p>c$이다. 즉 $f(V)\subseteq(c,d)$이므로 $f$는 $x_0$에서 연속이다.
:::

이 증명에서 정규성은 오직 [보조정리 1](#lem1)을 통해서만, 그러나 무한히 여러 번 사용되었다. Dyadic 유리수를 색인으로 택한 이유도 여기에 있다. 새로운 값은 언제나 이미 정의된 두 이웃 값 사이의 중점으로 등장하므로, 각 단계에서 보간이 정확히 한 번씩 필요하고 그 결과 사슬 $(U_r)$이 $[0,1]$ 전체를 조밀하게 덮게 된다.

::: 참고 3
[정리 2](#thm2)는 정규성의 성격을 근본적으로 바꾸어 준다. Normal space에서 서로소인 두 닫힌집합은 [§하우스도르프 공간, ⁋정의 3](/ko/math/topology/Hausdorff_spaces#def3)의 연속함수로 분리가능 조건을 항상 만족하며, 역으로 서로소인 임의의 두 닫힌집합이 연속함수로 분리가능한 공간은 자명하게 근방으로도 분리가능하므로 normal이다. 따라서 정규성은 근방에 의한 분리와 연속함수에 의한 분리가 서로소인 닫힌집합에 대해 일치하는 조건으로 다시 규정된다.
:::

## 정규공간의 예

Urysohn 보조정리가 공허하지 않으려면 normal space가 실제로 풍부하게 존재해야 한다. 우리는 두 개의 큰 부류를 확인한다. 하나는 compact Hausdorff space이고, 다른 하나는 metric space이다.

첫째 부류는 이미 확인된 바 있다. Compact Hausdorff space는 normal이다. ([§옹골공간, ⁋명제 7](/ko/math/topology/compact_spaces#prop7)) 따라서 임의의 compact Hausdorff space에서 서로소인 두 닫힌집합은 [정리 2](#thm2)에 의해 연속함수로 분리된다.

둘째 부류인 metric space는 거리함수 자체가 분리의 척도를 직접 제공한다. Metric space $(X,d)$와 공집합이 아닌 부분집합 $S\subseteq X$에 대하여, 점 $x$에서 $S$까지의 거리를

$$d(x,S)=\inf_{s\in S}d(x,s)$$

로 정의한다. 삼각부등식으로부터 $\lvert d(x,S)-d(y,S)\rvert\leq d(x,y)$가 성립하므로 함수 $x\mapsto d(x,S)$는 연속이며, $S$가 닫힌집합일 때 $d(x,S)=0$인 것과 $x\in S$인 것이 동치이다.

::: 명제 4
모든 metric space는 normal space이다.
:::
::: 증명
Metric space $(X,d)$의 서로소인 두 닫힌집합 $A,B$가 주어졌다 하자. 함수

$$g(x)=d(x,A)-d(x,B)$$

는 두 연속함수의 차이이므로 연속이다. 이제

$$U=g^{-1}((-\infty,0)),\qquad V=g^{-1}((0,\infty))$$

라 두면 $U,V$는 연속함수의 preimage로서 열린집합이며 서로소이다. 임의의 $a\in A$에 대하여 $d(a,A)=0$이고, $a\notin B$이며 $B$가 닫힌집합이므로 $d(a,B)>0$이다. 따라서 $g(a)<0$이 되어 $a\in U$이고, 같은 이유로 $B\subseteq V$이다. 이로써 $A,B$가 서로소인 열린집합 $U,V$로 분리되었다.
:::

[명제 4](#prop4)의 증명에서 등장한 함수

$$x\mapsto\frac{d(x,A)}{d(x,A)+d(x,B)}$$

는 사실 $A$에서 $0$, $B$에서 $1$의 값을 갖는 연속함수를 명시적으로 제공하므로, metric space에서는 [정리 2](#thm2)의 결론이 dyadic 사슬을 거치지 않고도 직접 확인된다. Urysohn 보조정리의 진정한 내용은 이러한 거리함수가 주어지지 않은 일반적인 normal space에서도 같은 결론이 성립한다는 데에 있다.

## Tietze 확장정리

Urysohn 보조정리는 두 개의 값 $0$과 $1$을 미리 지정된 두 닫힌집합에서 실현하는 연속함수를 만들어 낸다. Tietze 확장정리는 이를 극한까지 밀어붙인 것으로, 닫힌집합 위에서 미리 주어진 임의의 연속함수를 공간 전체로 연속적으로 확장한다. 그 증명은 Urysohn 함수를 이용해 목표 함수를 단계마다 일정 비율씩 근사하고, 그 오차 항들을 급수로 합하는 데에 있다. 우선 한 단계의 근사를 담당하는 보조정리를 세운다.

::: 보조정리 5
Normal space $X$의 닫힌집합 $A$와 연속함수 $g:A\rightarrow\mathbb{R}$이 주어졌다 하고, 어떤 $r>0$에 대하여 모든 $a\in A$에서 $\lvert g(a)\rvert\leq r$이라 하자. 그럼 연속함수 $h:X\rightarrow\mathbb{R}$이 존재하여 모든 $x\in X$에서 $\lvert h(x)\rvert\leq r/3$이고, 모든 $a\in A$에서 $\lvert g(a)-h(a)\rvert\leq 2r/3$이다.
:::
::: 증명
두 집합

$$B=g^{-1}([-r,-r/3]),\qquad C=g^{-1}([r/3,r])$$

를 생각하자. $g$가 $A$에서 연속이므로 $B,C$는 $A$의 닫힌집합이고, $A$가 $X$의 닫힌집합이므로 $B,C$는 $X$의 닫힌집합이기도 하다. 또한 $B,C$는 서로소이다. [정리 2](#thm2)를 $X$의 서로소인 두 닫힌집합 $B,C$에 적용하고 그 값을 $[-r/3,r/3]$로 재조정하면, 연속함수 $h:X\rightarrow[-r/3,r/3]$이 존재하여 $B$에서 $-r/3$의 값을, $C$에서 $r/3$의 값을 갖는다. (두 집합 가운데 하나가 공집합인 경우에도 상수함수를 택하면 되므로 결론은 유지된다.)

이제 $\lvert h(x)\rvert\leq r/3$은 정의상 성립한다. 오차를 확인하기 위해 $a\in A$를 세 경우로 나눈다. $a\in B$이면 $g(a)\in[-r,-r/3]$이고 $h(a)=-r/3$이므로 $\lvert g(a)-h(a)\rvert\leq 2r/3$이다. $a\in C$이면 symmetric으로 같은 부등식을 얻는다. $a$가 $B$에도 $C$에도 속하지 않으면 $g(a)\in(-r/3,r/3)$이고 $h(a)\in[-r/3,r/3]$이므로 그 차이의 절댓값은 $2r/3$을 넘지 않는다.
:::

::: 정리 6
(Tietze extension theorem) Normal space $X$의 닫힌집합 $A$와 연속함수 $f:A\rightarrow[a,b]$가 주어졌다 하자. 그럼 연속함수 $F:X\rightarrow[a,b]$이 존재하여 $F\vert_A=f$이다.
:::
::: 증명
$[a,b]$와 $[-1,1]$ 사이의 affine한 homeomorphism을 통해 $[a,b]=[-1,1]$인 경우만 다루면 충분하다. [보조정리 5](#lem5)를 $g=f$와 $r=1$에 적용하여 연속함수 $h_1:X\rightarrow\mathbb{R}$을 얻는다. 이는 모든 $x$에서 $\lvert h_1(x)\rvert\leq 1/3$이고 모든 $a\in A$에서 $\lvert f(a)-h_1(a)\rvert\leq 2/3$을 만족한다.

이제 $A$ 위에서 $f-h_1$은 $2/3$으로 유계인 연속함수이므로, 여기에 [보조정리 5](#lem5)를 $r=2/3$으로 적용하여 $\lvert h_2(x)\rvert\leq (1/3)(2/3)$이고 $A$ 위에서 $\lvert f-h_1-h_2\rvert\leq(2/3)^2$인 연속함수 $h_2$를 얻는다. 이를 귀납적으로 반복하면 연속함수들의 열 $(h_n)$을 얻어, 모든 $n\geq 1$에 대하여

$$\lvert h_n(x)\rvert\leq\frac{1}{3}\left(\frac{2}{3}\right)^{n-1}\quad(x\in X),\qquad\left\lvert f(a)-\sum_{k=1}^n h_k(a)\right\rvert\leq\left(\frac{2}{3}\right)^n\quad(a\in A)$$

가 성립한다. 이제 부분합 $S_n=\sum_{k=1}^n h_k$을 생각하자. 위의 첫째 부등식과

$$\sum_{n=1}^\infty\frac{1}{3}\left(\frac{2}{3}\right)^{n-1}=1$$

로부터, 임의의 $\epsilon>0$에 대해 $N$을 충분히 크게 잡아 모든 $x\in X$에서 $\lvert F(x)-S_N(x)\rvert\leq(2/3)^N<\epsilon/3$이도록 할 수 있다. 여기서 $F(x)=\sum_{n=1}^\infty h_n(x)$은 각 점에서 절대수렴하는 급수의 합으로 잘 정의되며, $\lvert F(x)\rvert\leq 1$이므로 $F:X\rightarrow[-1,1]$이다.

$F$의 연속성을 보이자. $x_0\in X$와 $\epsilon>0$이 주어졌다 하고 위와 같이 $N$을 택한다. $S_N$은 유한 개의 연속함수의 합이므로 연속이고, 따라서 $x_0$의 근방 $W$가 존재하여 모든 $x\in W$에서 $\lvert S_N(x)-S_N(x_0)\rvert<\epsilon/3$이다. 그럼 $x\in W$에 대하여

$$\lvert F(x)-F(x_0)\rvert\leq\lvert F(x)-S_N(x)\rvert+\lvert S_N(x)-S_N(x_0)\rvert+\lvert S_N(x_0)-F(x_0)\rvert<\epsilon$$

이므로 $F$는 $x_0$에서 연속이다. 끝으로 둘째 부등식에서 $n\rightarrow\infty$의 극한을 취하면 모든 $a\in A$에서 $F(a)=f(a)$이므로 $F$는 $f$의 확장이다.
:::

Tietze 확장정리는 목표 구간이 유계인 경우를 다루지만, 이를 발판으로 삼아 실수 전체를 값으로 갖는 함수의 확장 또한 얻을 수 있다.

::: 따름정리 7
Normal space $X$의 닫힌집합 $A$와 연속함수 $f:A\rightarrow\mathbb{R}$이 주어졌다 하자. 그럼 연속함수 $F:X\rightarrow\mathbb{R}$이 존재하여 $F\vert_A=f$이다.
:::
::: 증명
$t\mapsto t/(1+\lvert t\rvert)$은 $\mathbb{R}$과 열린구간 $(-1,1)$ 사이의 homeomorphism이므로, 이를 $f$에 합성하여 얻은 연속함수는 $A\rightarrow(-1,1)\subseteq[-1,1]$로 볼 수 있다. [정리 6](#thm6)에 의하여 이를 연속함수 $G:X\rightarrow[-1,1]$로 확장한다. 문제는 $G$가 $X$의 일부에서 값 $\pm 1$을 가질 수 있어 곧바로 $(-1,1)$로 돌아갈 수 없다는 데에 있다.

이 값을 밀어내기 위해 닫힌집합

$$D=G^{-1}(\{-1,1\})$$

를 생각하자. $A$ 위에서 $G$는 $(-1,1)$의 값을 가지므로 $D\cap A=\emptyset$이고, $D$와 $A$는 서로소인 두 닫힌집합이다. [정리 2](#thm2)에 의하여 연속함수 $\psi:X\rightarrow[0,1]$을 잡아 $D$에서 $0$, $A$에서 $1$의 값을 갖도록 한다. 그럼 곱 $\psi G$는 연속이며, $\lvert G(x)\rvert=1$인 점에서는 $\psi(x)=0$이라 $\psi(x)G(x)=0$이고 그 밖의 점에서는 $\lvert\psi(x)G(x)\rvert\leq\lvert G(x)\rvert<1$이므로, $\psi G$는 $X$ 전체에서 $(-1,1)$의 값을 갖는다. 또한 $A$에서 $\psi=1$이므로 $\psi G$는 $A$에서 $G$와, 따라서 $f$를 $(-1,1)$로 옮긴 함수와 일치한다. 이제 homeomorphism $(-1,1)\rightarrow\mathbb{R}$을 다시 합성하면 원하는 확장 $F:X\rightarrow\mathbb{R}$을 얻는다.
:::

## Urysohn 거리화정리

지금까지의 결과는 normal space가 연속함수를 얼마나 풍부하게 지니는지를 보여 준다. 이 풍부함을 극한까지 활용하면, 적당한 가산성 조건 아래에서 위상 자체가 거리로부터 유도됨을 보일 수 있다. 이것이 Urysohn 거리화정리이다. 우리는 $X$가 가산 개의 원소로 이루어진 base를 가질 때 ([§위상공간의 기저, ⁋정의 1](/ko/math/topology/topological_bases#def1)) $X$를 second countable이라 부른다. ([§옹골성과 필터의 수렴, ⁋정의 10](/ko/math/topology/filter_convergence#def10))

증명의 첫 단계는 우리가 다루는 공간이 실제로 normal이어서 Urysohn 보조정리를 사용할 수 있음을 확인하는 것이다.

::: 보조정리 8
Regular space가 Lindelöf이면 normal이다. 특히 second countable인 regular space는 normal이다.
:::
::: 증명
Regular Lindelöf space $X$의 서로소인 두 닫힌집합 $A,B$가 주어졌다 하자. 각 $a\in A$에 대하여 $a\notin B$이고 $X$가 regular이므로, $a$의 열린근방 $U_a$를 잡아 $\cl(U_a)\cap B=\emptyset$이도록 할 수 있다. 실제로 regular의 정의에 의해 $a$와 닫힌집합 $B$를 분리하는 서로소인 열린집합 $U_a\ni a$, $W\supseteq B$가 존재하고, $U_a\subseteq X\setminus W$로부터 $\cl(U_a)\subseteq X\setminus W\subseteq X\setminus B$이기 때문이다. 이제 $\{U_a\}_{a\in A}$에 열린집합 $X\setminus A$를 더한 모임은 $X$의 open cover이고, $X$가 Lindelöf이므로 가산 부분덮개가 존재한다. 여기에서 $X\setminus A$를 다시 빼면 $A$를 덮는 가산 부분모임 $\{U_n\}_{n\geq 1}$을 얻는다. 각 $U_n$은 $\cl(U_n)\cap B=\emptyset$을 만족한다. 같은 방식으로 $B$를 덮는 가산 개의 열린집합 $\{V_n\}_{n\geq 1}$을 잡아 $\cl(V_n)\cap A=\emptyset$이도록 한다.

이제 두 모임을 서로 잘라내어

$$U_n'=U_n\setminus\bigcup_{k=1}^n\cl(V_k),\qquad V_n'=V_n\setminus\bigcup_{k=1}^n\cl(U_k)$$

로 둔다. 이들은 닫힌집합을 유한 개 뺀 것이므로 열린집합이다. 이제 $U'=\bigcup_n U_n'$과 $V'=\bigcup_n V_n'$을 생각하자. 임의의 $a\in A$는 어떤 $U_n$에 속하고 모든 $k$에 대해 $a\notin\cl(V_k)$이므로 $a\in U_n'$이다. 따라서 $A\subseteq U'$이고 symmetric으로 $B\subseteq V'$이다. 끝으로 $U'\cap V'=\emptyset$임을 보이자. 어떤 $x$가 $U_m'\cap V_n'$에 속한다고 하면 일반성을 잃지 않고 $m\leq n$이라 할 수 있는데, $x\in U_m'\subseteq U_m$이므로 $x\in\cl(U_m)$이고, 한편 $x\in V_n'$의 정의에서 $m\leq n$이므로 $x\notin\cl(U_m)$이어야 하여 모순이다. 따라서 $A,B$는 서로소인 열린집합 $U',V'$로 분리된다.

둘째 주장은 second countable space가 Lindelöf라는 사실로부터 즉시 따른다. ([§옹골성과 필터의 수렴, ⁋명제 12](/ko/math/topology/filter_convergence#prop12))
:::

이제 주 정리를 서술한다. 우리의 규약에서 $T_3$-space는 $T_0$이며 regular인 공간을 뜻하고, 이는 [§하우스도르프 공간, ⁋정의 3](/ko/math/topology/Hausdorff_spaces#def3)에서 확인한 것처럼 Hausdorff이며 따라서 $T_1$이다.

::: 정리 9
(Urysohn metrization theorem) Second countable인 $T_3$-space는 metrizable이다.
:::
::: 증명
증명의 핵심은 $X$를 Hilbert cube $[0,1]^{\mathbb{N}}$의 부분공간으로 매장하는 것이다. Hilbert cube는

$$\rho((x_n),(y_n))=\sum_{n=1}^\infty\frac{\lvert x_n-y_n\rvert}{2^n}$$

이 정의하는 거리로 metrizable이며, metric space의 부분공간은 다시 metric space이므로, $X$가 $[0,1]^{\mathbb{N}}$의 부분공간과 위상동형임을 보이면 충분하다.

먼저 $X$는 [보조정리 8](#lem8)에 의해 normal이므로 [정리 2](#thm2)를 사용할 수 있다. $X$의 가산 base $\{B_n\}_{n\geq 1}$을 고정하고, $\cl(B_m)\subseteq B_n$을 만족하는 순서쌍 $(m,n)$마다 [정리 2](#thm2)를 서로소인 두 닫힌집합 $\cl(B_m)$과 $X\setminus B_n$에 적용하여, $\cl(B_m)$에서 $1$의 값을, $X\setminus B_n$에서 $0$의 값을 갖는 연속함수를 하나씩 얻는다. 이러한 순서쌍은 가산 개이므로 이렇게 얻은 함수들을 $f_1,f_2,\ldots$로 나열할 수 있다.

이 함수족은 점과 닫힌집합을 분리한다. 즉 점 $x$와 이를 포함하지 않는 닫힌집합 $C$가 주어지면, $x\in X\setminus C$이고 base의 정의에서 $x\in B_n\subseteq X\setminus C$인 $B_n$이 존재한다. $X$가 regular이므로 [보조정리 1](#lem1)과 같은 방식으로 $x\in B_m\subseteq\cl(B_m)\subseteq B_n$인 base 원소 $B_m$을 잡을 수 있고, 이 순서쌍 $(m,n)$에 대응하는 함수 $f_k$는 $f_k(x)=1$이며 $C\subseteq X\setminus B_n$ 위에서 $0$의 값을 갖는다.

이제 함수

$$F:X\rightarrow[0,1]^{\mathbb{N}},\qquad F(x)=(f_1(x),f_2(x),\ldots)$$

를 정의한다. 각 좌표함수 $f_k$가 연속이므로 $F$는 연속이다. $F$가 단사임은 $X$가 $T_1$인 데에서 따른다. 서로 다른 두 점 $x\neq y$에 대해 $\{y\}$는 닫힌집합이고 $x\notin\{y\}$이므로 위의 분리 성질에서 어떤 $f_k$가 $f_k(x)=1$, $f_k(y)=0$이 되기 때문이다. 끝으로 $F$가 상 위로의 homeomorphism임을 보이려면 $F$가 열린 사상임을, 즉 $X$의 열린집합 $U$에 대해 $F(U)$가 $F(X)$에서 열려 있음을 확인하면 된다. $x\in U$가 주어지면 위의 분리 성질에서 $f_k(x)>0$이고 $X\setminus U$ 위에서 $f_k=0$인 $f_k$가 존재하므로, $k$번째 좌표가 양수인 $[0,1]^{\mathbb{N}}$의 열린집합과 $F(X)$의 교집합은 $F(x)$를 포함하며 $F(U)$ 안에 놓인다. 이로써 $F$는 상 위로의 homeomorphism이 되어 $X$는 metrizable이다.

여기서 사용한 매장 보조사실, 즉 점과 닫힌집합을 분리하는 연속함수족이 항상 곱공간으로의 매장을 낳는다는 사실과 Hilbert cube의 거리화 가능성에 대한 세부 논증은 표준적인 문헌을 따른다. **[Mun]**
:::

이 정리는 second countable이라는 가산성 조건이 붙는 순간 위상적 separation axiom과 거리 구조가 사실상 같은 것임을 말해 준다. 이로써 우리는 추상적인 위상공간과 익숙한 metric space 사이의 간극이 생각보다 좁다는 사실을 확인한다.

Urysohn 보조정리로 얻어지는 연속함수는 이후 다양한 국소적 구성을 전역적으로 이어 붙이는 데에 쓰인다. 특히 open covering에 종속되어 합이 항상 $1$이 되는 연속함수들의 모임인 partition of unity의 존재가 바로 이러한 Urysohn 함수 위에 세워진다.

---

**참고문헌**

**[Mun]** J. R. Munkres, *Topology*, 2nd ed., Prentice Hall, 2000.

**[Wil]** S. Willard, *General Topology*, Addison-Wesley, 1970.

**[Kel]** J. L. Kelley, *General Topology*, Springer, 1975.
