---
title: "Compactness와 paracompactness"
description: "Tychonoff 정리로 compactness를 마무리하고, paracompact Hausdorff 공간에서 open cover에 종속된 단위분할이 존재함을 보인다."
excerpt: "Tychonoff theorem, paracompactness, and partition of unity"

categories: [Math / Topology]
permalink: /ko/math/topology/compactness
sidebar:
    nav: "topology-ko"

date: 2024-12-15
weight: 16


---

이제 우리는 옹골성과 관련된 남은 결과인 Tychonoff 정리를 살펴본다. 

## Tychonoff theorem

Compact space의 임의의 product는 다시 compact space가 된다. 만일 이 product가 유한이라면 이 결과는 보다 직관적인 방식으로 보일 수 있지만, 이 product가 무한하다면 이를 위해서는 다음 보조정리가 필요하다. 이는 [§옹골성과 필터의 수렴, ⁋명제 5](/ko/math/topology/filter_convergence#prop5)를 filter의 언어로 일반화한 것이다. 

::: 보조정리 1
위상공간 $X$가 compact인 것은 임의의 ultrafilter가 수렴하는 것과 동치이다.
:::
::: 증명
우선 $X$가 compact라 가정하고, 임의의 ultrafilter $\mathcal{F}$가 주어졌다 하자. 결론에 반하여 $\mathcal{F}$의 limit point가 존재하지 않는다 하자. 즉, 어떠한 $x\in X$에 대해서도 열린근방 $U_x$가 존재하여 $U_x\not\in \mathcal{F}$이도록 할 수 있다. 그럼 $X$의 compactness에 의하여 $X$의 유한한 subcover $U_{x_1},\ldots, U_{x_n}$이 존재한다. 

한편 [\[집합론\] §필터와 아이디얼, 갈루아 대응, ⁋명제 5](/ko/math/set_theory/filter_and_ideal#prop5)에 의하여 $\mathcal{F}$는 prime이다. 즉, 임의의 부분집합 $A\subseteq X$에 대하여, $A\in \mathcal{F}$ 혹은 $X\setminus A\in \mathcal{F}$ 중 정확히 하나가 성립한다. 그럼 이제 임의의 $A\in \mathcal{F}$에 대하여,

$$A=A\cap X=(A\cap U_{x_1})\cup \cdots\cup (A\cap U_{x_n})\in \mathcal{F}$$

이며, 가정에 의하여 $U_{x_i}\not\in \mathcal{F}$이므로 각각의 $A\cap U_{x_i}$들도 $\mathcal{F}$에 속하지 않으며 $\mathcal{F}$가 maximal이므로 $X\setminus (A\cap U_{x_i})\in \mathcal{F}$여야 한다. 그럼 이들의 유한한 교집합

$$X\setminus A=(X\setminus (A\cap U_{x_1}))\cap\cdots\cap (X\setminus (A\cap U_{x_n}))$$

도 $\mathcal{F}$에 속해야 하므로, 이는 $A$와 $X\setminus A$ 가운데 정확히 하나만 $\mathcal{F}$에 속한다는 사실에 모순이다. 

거꾸로 임의의 ultrafilter $\mathcal{F}$가 주어질 때마다 limit point $x$를 찾을 수 있다 하고, finite intersection property를 만족하는 $X$의 닫힌집합들의 family $\mathcal{A}$가 주어졌다 하자. 그럼 $\mathcal{A}$에 의해 생성되는 filter를 포함하는 ultrafilter $\mathcal{F}$를 생각할 수 있으며, 가정에 의해 $\mathcal{F}$는 limit point $x$를 가진다. 즉 $\mathcal{N}(x)\subseteq \mathcal{F}$이며, 따라서 임의의 $F\in \mathcal{F}$와 $x$의 임의의 근방 $U$에 대하여 $U\cap F\neq\emptyset$이다. 특히 임의의 $A\in \mathcal{A}$와 $x$의 임의의 근방 $U$에 대하여 $A\cap U\neq\emptyset$이므로, $x\in \cl(A)=A$가 항상 성립한다. 이로부터 $x\in\bigcap_{A\in \mathcal{A}}A$임을 알고, 따라서 [§옹골공간, ⁋명제 11](/ko/math/topology/compact_spaces#prop11)에 의해 원하는 결과를 얻는다.
:::

그럼 다음이 성립한다.

::: 정리 2 (Tychonoff)
Compact space들 $(X_i)_{i\in I}$의 product $X=\prod_{i\in I} X_i$는 compact이다. 거꾸로, 만일 $X\neq\emptyset$이며 product space $X$가 compact라면, 각각의 $X_i$들이 모두 compact이다.
:::
::: 증명
만일 $X$가 compact라면, 각각의 $X_i$들이 모두 compact라는 것은 $\pr_i$의 연속성과 [§옹골공간, ⁋명제 8](/ko/math/topology/compact_spaces#prop8)에 의해 자명하다.

반대 방향은 $X$ 위에 정의된 임의의 ultrafilter $\mathcal{F}$에 대하여, $\pr_i(\mathcal{F})$가 $X_i$의 ultrafilter base를 정의한다는 것을 확인한 후, $X_i$가 compact라는 가정과 [보조정리 1](#lem1)로부터 이 ultrafilter의 limit point $x_i$를 얻고, $x=(x_i)_{i\in I}$가 $\mathcal{F}$의 limit point임을 보일 수 있으므로 다시 [보조정리 1](#lem1)에 의해 증명이 완료된다. 
:::


## 국소적 옹골공간

Compactness는 위상공간이 지닐 수 있는 성질 가운데 가장 강력한 것에 속하지만, 정작 우리가 다루는 많은 공간은 compact가 아니다. Euclidean space $\mathbb{R}^n$은 유계가 아니어서 compact가 아니고, 뒤에서 다룰 topological manifold 역시 국소적으로만 Euclidean space를 닮았을 뿐 전체로는 compact일 이유가 없다. 그럼에도 이러한 공간들은 각 점 주위에서만큼은 compact 공간처럼 행동한다. 우리는 이 국소적인 성질을 분리해 내어, 전역적 compactness가 없는 공간에서도 compact 공간의 논증을 국소적으로 되살리고자 한다. 더 나아가 이러한 공간에 단 하나의 점을 더하는 것만으로 compact 공간을 얻을 수 있음을 보게 될 것이다.

우리는 각 점 주위의 옹골성이라는 이 국소적 조건을 다음과 같이 정식화한다.

::: 정의 3
위상공간 $X$가 점 $x\in X$에서 *locally compact<sub>국소적으로 옹골</sub>*라는 것은 $x$를 포함하는 $X$의 compact neighborhood가 존재하는 것이다. $X$가 모든 점에서 locally compact일 때 $X$를 *locally compact space<sub>국소적 옹골공간</sub>*이라 부른다. Locally compact이며 Hausdorff인 공간을 줄여 *LCH space*라 적기로 한다.
:::

여기에서 $x$의 neighborhood란 $x$를 포함하는 열린집합을 다시 품는 부분집합을 뜻하므로, compact neighborhood는 반드시 열린집합일 필요가 없다. 예컨대 $\mathbb{R}$에서 닫힌구간 $[-1,1]$은 $0$의 compact neighborhood이지만 열린집합은 아니다. 이처럼 정의는 compact인 근방 하나의 존재만을 요구하는 약한 형태이지만, 공간이 Hausdorff이면 이 조건이 훨씬 다루기 쉬운 형태로 다시 서술된다.

::: 명제 4
Hausdorff space $X$의 점 $x$에 대하여 다음 두 조건은 동치이다.

1. $X$는 $x$에서 locally compact이다.
2. $x$의 임의의 열린근방 $V$에 대하여, 열린집합 $W$가 존재하여 $x\in W$, $\cl(W)\subseteq V$이며 $\cl(W)$가 compact이다.
:::
::: 증명
둘째 조건에서 $V=X$로 두면 $\cl(W)$가 $x$를 품는 열린집합 $W$를 포함하는 compact 집합이 되어 $x$의 compact neighborhood를 이루므로, 둘째 조건은 첫째 조건을 함의한다.

거꾸로 $X$가 $x$에서 locally compact라 하고 $x$의 열린근방 $V$가 주어졌다 하자. $x$의 compact neighborhood $K$를 잡고 $U=\interior(K)$라 두면 $U$는 $x$를 품는 열린집합이며 $U\subseteq K$이다. 이제 $V$를 $V\cap U$로 바꾸어 처음부터 $V\subseteq U\subseteq K$라 가정하여도 무방하다. 더 작은 $V$에 대해 결론을 얻으면 원래의 $V$에 대해서도 결론이 성립하기 때문이다.

$K$는 compact Hausdorff space이므로 regular space이다. ([§옹골공간, ⁋보조정리 6](/ko/math/topology/compact_spaces#lem6)) 한편 $V\subseteq K$는 $X$의 열린집합이므로 부분공간 $K$에서도 열린집합이고, 따라서 $K\setminus V$는 $K$의 닫힌집합으로서 $x$를 포함하지 않는다. $K$의 regularity를 점 $x$와 닫힌집합 $K\setminus V$에 적용하면, $K$에서 열린 서로소인 두 집합 $P\ni x$와 $Q\supseteq K\setminus V$를 얻는다. $P\subseteq K\setminus Q\subseteq V$이고 $K\setminus Q$는 $K$의 닫힌집합이므로 $\cl_K(P)\subseteq K\setminus Q\subseteq V$이다.

이제 $W=P\cap U$라 두자. $P$는 $K$에서 열린집합이고 $U$는 $X$의 열린집합이며 $U\subseteq K$이므로 $W$는 $X$에서 열린집합이고 $x\in W$이다. $W\subseteq U\subseteq K$이고 $K$는 $X$의 닫힌집합이므로 ([§옹골공간, ⁋따름정리 5](/ko/math/topology/compact_spaces#cor5)) $\cl(W)\subseteq K$이다. 따라서 $\cl(W)=\cl(W)\cap K=\cl_K(W)\subseteq\cl_K(P)\subseteq V$이다. 끝으로 $\cl(W)$는 compact 집합 $K$의 닫힌 부분집합이므로 compact이다. ([§옹골공간, ⁋보조정리 3](/ko/math/topology/compact_spaces#lem3)) 이로써 둘째 조건이 성립한다.
:::

[명제 4](#prop4)의 둘째 조건은 LCH space에서 각 점이 compact closure를 갖는 열린집합들로 이루어진 neighborhood basis를 가진다는 것으로 읽을 수 있다. 이는 앞으로 국소적 논증을 펼칠 때마다 반복적으로 사용되며, one-point compactification의 Hausdorff성을 판정할 때에도 핵심적인 역할을 한다. 또한 이 성질로부터 임의의 LCH space가 regular임이 곧바로 따르는데, 점 $x$와 이를 포함하지 않는 닫힌집합 $C$가 주어지면 $V=X\setminus C$에 둘째 조건을 적용하여 얻은 $W$와 $X\setminus\cl(W)$가 $x$와 $C$를 분리하기 때문이다.

가장 기본적인 예로 Euclidean space $\mathbb{R}^n$이 LCH임을 들 수 있다. 임의의 점 $x$에 대하여 닫힌 공 $\{y:\lVert y-x\rVert\leq 1\}$은 Heine–Borel 정리에 의해 compact이고 열린 공을 품으므로 $x$의 compact neighborhood를 이루며, $\mathbb{R}^n$이 Hausdorff임은 이미 알고 있다. 마찬가지로 임의의 discrete space도 LCH인데, 각 점 $x$에 대하여 한원소집합 $\{x\}$이 열린 유한집합으로서 compact neighborhood가 되고 discrete space는 Hausdorff이기 때문이다. 조금 덜 자명한 예는 topological manifold이다.

::: 예시 5
각 점이 $\mathbb{R}^n$의 열린집합과 homeomorphic한 열린근방을 갖는 Hausdorff 공간은 LCH space이다. 뒤에서 정의할 topological manifold가 바로 이러한 공간이다. 실제로 그러한 공간 $M$의 각 점 $x$에 대하여 $\mathbb{R}^n$의 열린집합과 homeomorphic한 열린근방 $U$를 잡으면, 그 homeomorphism 아래에서 $x$에 대응하는 점이 $\mathbb{R}^n$에서 compact neighborhood를 가지므로 ($\mathbb{R}^n$이 LCH이기 때문이다) 이를 $U$로 되끌어 오면 $x$의 compact neighborhood를 얻는다.
:::

Locally compact이라는 조건은 얼핏 매우 약해 보이지만 결코 자동으로 주어지는 것은 아니다. 다음은 locally compact space가 아닌 대표적인 예이다.

::: 예시 6
유리수 공간 $\mathbb{Q}$는 $\mathbb{R}$의 부분공간으로서 어떤 점에서도 locally compact가 아니다. 대칭성에 의해 $0$에서 그렇지 않음을 보이면 충분하다. 결론에 반하여 $0$의 compact neighborhood $K\subseteq\mathbb{Q}$가 존재한다 하자. 그럼 $K$는 $0$을 품는 열린집합을 포함하므로 어떤 $\delta>0$에 대하여 $\mathbb{Q}\cap(-\delta,\delta)\subseteq K$이고, $0<r<\delta$를 하나 고정하면 $\mathbb{Q}\cap[-r,r]\subseteq K$이다.

Compactness는 부분공간이 놓인 주변 공간과 무관한 내재적 성질이므로 $K$는 $\mathbb{R}$의 부분공간으로서도 compact이고, $\mathbb{R}$이 Hausdorff이므로 $K$는 $\mathbb{R}$의 닫힌집합이다. ([§옹골공간, ⁋따름정리 5](/ko/math/topology/compact_spaces#cor5)) 그런데 $\mathbb{R}$에서 $\mathbb{Q}\cap[-r,r]$의 closure는 $[-r,r]$ 전체이므로, $K$가 닫힌집합이면서 $\mathbb{Q}\cap[-r,r]$을 포함한다는 사실로부터 $[-r,r]\subseteq K$를 얻는다. 이는 $K\subseteq\mathbb{Q}$이면서 $[-r,r]$이 무리수를 포함한다는 사실에 모순이다.
:::

국소적 옹골성은 적당한 부분공간으로 유전된다. 다만 임의의 부분공간이 아니라 열린집합이거나 닫힌집합인 부분공간에 한하여 그러하다.

::: 명제 7
LCH space $X$의 열린 부분공간과 닫힌 부분공간은 모두 LCH space이다.
:::
::: 증명
Hausdorff space의 부분공간은 다시 Hausdorff이므로 국소적 옹골성만 확인하면 된다.

먼저 $A\subseteq X$가 열린집합이라 하고 $x\in A$가 주어졌다 하자. $A$는 $x$의 $X$에서의 열린근방이므로 [명제 4](#prop4)의 둘째 조건에 의하여 $X$의 열린집합 $W$가 존재하여 $x\in W$이고 $\cl_X(W)\subseteq A$이며 $\cl_X(W)$가 compact이다. $\cl_X(W)\subseteq A$이므로 $A$에서의 closure $\cl_A(W)$는 $\cl_X(W)$와 같고, 이는 compact이면서 $A$에서 열린 $W$를 포함하므로 $x$의 $A$에서의 compact neighborhood이다.

이제 $A\subseteq X$가 닫힌집합이라 하고 $x\in A$가 주어졌다 하자. $X$에서 $x$의 compact neighborhood $K$를 잡고, $x$를 품는 $X$의 열린집합 $U\subseteq K$를 택한다. 그럼 $K\cap A$는 compact 집합 $K$의 닫힌 부분집합이므로 compact이고 ([§옹골공간, ⁋보조정리 3](/ko/math/topology/compact_spaces#lem3)), $U\cap A$는 $A$에서 열린집합으로서 $x$를 품고 $K\cap A$에 포함되므로 $K\cap A$는 $x$의 $A$에서의 compact neighborhood이다.
:::

## 일점 옹골화의 구성

Compact가 아닌 공간을 compact로 만드는 가장 경제적인 방법은 부족한 부분을 단 하나의 점으로 메우는 것이다. 직관적으로는 $\mathbb{R}$의 양끝으로 달아나는 점들을 하나의 무한원점으로 모아 원을 만드는 것과 같다. 우리는 이 옹골화를 임의의 위상공간에 대해 명시적으로 정식화하고, 그것이 compact 공간을 낳음을 보인 뒤, 그 구성이 언제 Hausdorff 공간을 낳는지까지 규명한다.

::: 정의 8
위상공간 $X$가 주어졌다 하자. $X$에 속하지 않는 새로운 점 하나를 $\infty$라 적고 집합 $X^+=X\cup\{\infty\}$을 생각한다. $X^+$의 부분집합 가운데 다음 두 종류를 열린집합으로 선언한다. 첫째로 $X$의 열린집합 $U$, 둘째로 $X$에서 compact이며 닫힌 부분집합 $C$에 대한 $X^+\setminus C$이다. 이렇게 얻은 위상공간 $X^+$를 $X$의 *one-point compactification<sub>일점 옹골화</sub>*, 또는 *Alexandroff compactification<sub>알렉산드로프 콤팩트화</sub>*이라 부른다.
:::

이 선언이 실제로 [§열린집합, ⁋정의 1](/ko/math/topology/open_sets#def1)의 위상 공리를 만족함을 확인해야 한다. 공집합은 $X$의 열린집합이므로 첫째 종류에 속하고, 공집합은 compact이며 닫힌집합이므로 $X^+=X^+\setminus\emptyset$은 둘째 종류에 속한다. 두 열린집합의 교집합에 대해서는 세 경우를 따진다. 첫째 종류 둘의 교집합은 $X$의 열린집합이다. 둘째 종류 둘의 교집합은 $(X^+\setminus C)\cap(X^+\setminus D)=X^+\setminus(C\cup D)$이고 $C\cup D$가 compact인 닫힌집합이므로 다시 둘째 종류이다. 서로 다른 종류의 교집합은 $U\cap(X^+\setminus C)=U\cap(X\setminus C)$이며 $C$가 닫힌집합이므로 $X\setminus C$가 열린집합이 되어 $X$의 열린집합, 곧 첫째 종류이다. 임의의 합집합에 대해서도 마찬가지로, 첫째 종류들의 합집합은 열린집합이고, 둘째 종류들의 합집합 $\bigcup_\alpha(X^+\setminus C_\alpha)=X^+\setminus\bigcap_\alpha C_\alpha$은 $\bigcap_\alpha C_\alpha$가 어떤 $C_\alpha$의 닫힌 부분집합으로서 compact이므로 ([§옹골공간, ⁋보조정리 3](/ko/math/topology/compact_spaces#lem3)) 둘째 종류이며, 두 종류가 섞인 합집합은 $U\cup(X^+\setminus C)=X^+\setminus(C\cap(X\setminus U))$인데 $C\cap(X\setminus U)$가 compact인 닫힌집합이므로 둘째 종류이다.

이 위상에서 $X$가 $X^+$에 어떻게 놓이는지를 먼저 정리한다.

::: 명제 9
포함사상 $X\hookrightarrow X^+$는 open embedding, 곧 $X$를 $X^+$의 열린 부분공간으로 놓는 homeomorphism이다. 또한 $X$가 $X^+$에서 조밀할 필요충분조건은 $X$가 compact가 아닌 것이다.
:::
::: 증명
$X$는 $X$의 열린집합이므로 [정의 8](#def8)의 첫째 종류로서 $X^+$의 열린집합이다. $X^+$의 열린집합을 $X$와 교차시키면, 첫째 종류 $U$에 대해서는 $U\cap X=U$이고 둘째 종류 $X^+\setminus C$에 대해서는 $(X^+\setminus C)\cap X=X\setminus C$인데 둘 다 $X$의 열린집합이며, 거꾸로 $X$의 임의의 열린집합은 첫째 종류로서 $X^+$에서 열린집합이다. 따라서 $X$ 위의 부분공간 위상은 원래의 위상과 일치하고, 포함사상은 열린 부분공간 위로의 homeomorphism이다.

$\{\infty\}=X^+\setminus X$는 열린집합 $X$의 여집합이므로 닫힌집합이다. $X$가 조밀하다는 것은 $\infty\in\cl(X)$인 것, 곧 $\infty$의 임의의 열린근방이 $X$와 만나는 것과 같다. $\infty$를 품는 열린집합은 반드시 둘째 종류 $X^+\setminus C$이며, 이것이 $X$와 만나는 것은 $X\setminus C\neq\emptyset$, 곧 $C\neq X$인 것과 같다. 따라서 $X$가 조밀하지 않을 필요충분조건은 어떤 compact인 닫힌집합 $C$에 대해 $C=X$인 것, 곧 $X$ 자신이 compact인 것이다.
:::

$X$가 compact인 경우에는 $X$ 자체가 compact이며 닫힌집합이므로 $\{\infty\}=X^+\setminus X$가 열린집합이 되어 $\infty$가 isolated point가 된다. 이 경우 $X^+$는 $X$에 isolated point 하나를 덧붙인 것에 지나지 않아 흥미롭지 않다. One-point compactification이 본래 의도한 역할을 하는 것은 $X$가 compact가 아닐 때이며, 이때 $\infty$는 $X$ 바깥으로 달아나는 모든 방향의 limit point 노릇을 한다.

::: 정리 10
임의의 위상공간 $X$에 대하여 $X^+$는 compact이다.
:::
::: 증명
$X^+$의 임의의 open covering $(O_i)_{i\in I}$이 주어졌다 하자. $\infty$를 덮는 열린집합 $O_j$가 적어도 하나 존재하며, 이는 반드시 둘째 종류이므로 $X$의 compact인 닫힌집합 $C$에 대해 $O_j=X^+\setminus C$로 적을 수 있다. 나머지 $(O_i)_{i\neq j}$은 $C\subseteq X^+\setminus O_j$을 덮어야 하며, 각 $O_i\cap X$는 $X$의 열린집합이므로 $(O_i\cap X)_{i\neq j}$은 $C$의 $X$에서의 open covering이다. $C$가 compact이므로 유한한 $J\subseteq I\setminus\{j\}$을 택하여 $C\subseteq\bigcup_{i\in J}(O_i\cap X)\subseteq\bigcup_{i\in J}O_i$이도록 할 수 있다. ([§옹골공간, ⁋명제 2](/ko/math/topology/compact_spaces#prop2)) 그럼 $(O_i)_{i\in J\cup\{j\}}$이 $X^+$를 덮는 finite subcover이다.
:::

## Hausdorff 판정과 보편성

One-point compactification은 어떤 공간에 대해서도 compact 공간을 낳지만, 그 결과가 다시 Hausdorff가 되는지는 별개의 문제이다. 예컨대 $\mathbb{Q}^+$은 compact이지만 Hausdorff가 아니다. 다음 정리는 $X^+$가 Hausdorff가 되는 조건이 정확히 앞서 정의한 국소적 옹골성임을 밝힌다.

::: 정리 11
위상공간 $X$에 대하여 $X^+$가 Hausdorff space일 필요충분조건은 $X$가 LCH space인 것이다.
:::
::: 증명
먼저 $X^+$가 Hausdorff라 하자. 부분공간 $X$는 Hausdorff space의 부분공간이므로 Hausdorff이다. 국소적 옹골성을 보이기 위해 $x\in X$를 고정하면, $X^+$의 Hausdorff성에 의해 $x$와 $\infty$를 분리하는 서로소인 열린집합 $U\ni x$와 $W\ni\infty$가 존재한다. $W$는 $\infty$를 품으므로 둘째 종류이고, 따라서 $X$의 compact인 닫힌집합 $C$에 대해 $W=X^+\setminus C$이다. $U\cap W=\emptyset$으로부터 $U\subseteq C$이고, $U$는 $\infty$를 품지 않으므로 $X$에 포함되는 열린집합이다. 따라서 $C$는 $x$를 품는 열린집합 $U$를 포함하는 compact 집합, 곧 $x$의 compact neighborhood이며 $X$는 $x$에서 locally compact이다.

거꾸로 $X$가 LCH라 하자. $X^+$의 서로 다른 두 점을 분리해야 한다. 두 점이 모두 $X$에 속하면 $X$가 Hausdorff이므로 이들을 $X$에서 분리하는 서로소인 열린집합을 얻고, 이들은 [정의 8](#def8)의 첫째 종류로서 $X^+$에서도 열린집합이다. 남은 경우는 한 점이 $x\in X$이고 다른 한 점이 $\infty$인 경우이다. $X$가 LCH이므로 [명제 4](#prop4)에 의하여 $x$의 열린근방 $U$가 존재하여 $K=\cl(U)$가 compact이다. $X$가 Hausdorff이므로 $K$는 닫힌집합이고 ([§옹골공간, ⁋따름정리 5](/ko/math/topology/compact_spaces#cor5)), 따라서 $X^+\setminus K$는 $\infty$를 품는 둘째 종류의 열린집합이다. $U\subseteq K$이므로 $U$와 $X^+\setminus K$는 서로소이며 각각 $x$와 $\infty$를 분리한다.
:::

[정리 10](#thm10)과 [정리 11](#thm11)를 합치면, $X$가 LCH space일 때 $X^+$는 compact Hausdorff space가 되고 [명제 9](#prop9)에 의해 $X$는 그 안에 열린 부분공간으로 매장된다. 특히 $X$가 compact가 아니라면 이 embedding은 조밀하다. 이것이 Alexandroff 정리의 존재 부분, 곧 임의의 LCH space가 어떤 compact Hausdorff space에 조밀한 열린 부분공간으로 매장된다는 사실이다. 남은 것은 이러한 옹골화가 본질적으로 유일하다는 사실이며, 이는 다음의 보편성으로 정식화된다.

::: 정리 12
LCH space $X$가 주어졌다 하자. Compact Hausdorff space $Y$와 점 $p\in Y$, 그리고 homeomorphism $\varphi:X\rightarrow Y\setminus\{p\}$이 주어졌다 하면, 유일한 homeomorphism $h:X^+\rightarrow Y$가 존재하여 $X$ 위에서 $h=\varphi$이고 $h(\infty)=p$이다.
:::
::: 증명
$\varphi$를 통해 $X$와 $Y\setminus\{p\}$을 동일시하고, $X$를 $Y$의 부분집합으로 본다. $Y$가 Hausdorff이므로 $\{p\}$는 $Y$의 닫힌집합이고, 따라서 $X=Y\setminus\{p\}$는 $Y$의 열린 부분공간이다. 즉 $X$의 위상은 $Y$로부터 유도된 부분공간 위상과 일치한다.

이제 $Y$의 열린집합이 정확히 $X^+$의 열린집합과 대응함을 보인다. $Y$의 열린집합 $O$가 $p$를 포함하지 않으면 $O\subseteq X$이고 $X$가 $Y$의 열린 부분공간이므로 $O$는 $X$의 열린집합, 곧 [정의 8](#def8)의 첫째 종류이다. 거꾸로 $X$의 열린집합은 $X$가 $Y$에서 열린집합이므로 $Y$의 열린집합이다. 한편 $Y$의 열린집합 $O$가 $p$를 포함하면 $Y\setminus O$는 compact 공간 $Y$의 닫힌집합이므로 compact이고 ([§옹골공간, ⁋보조정리 3](/ko/math/topology/compact_spaces#lem3)), $Y\setminus O\subseteq X$이며 $Y$에서 닫힌집합이므로 $X$에서도 닫힌집합이다. 따라서 $O=X^+\setminus(Y\setminus O)$은 $X$의 compact인 닫힌집합의 여집합, 곧 둘째 종류이다. 거꾸로 $X$의 compact인 닫힌집합 $C$에 대하여 $C$는 $Y$에서도 compact이고 $Y$가 Hausdorff이므로 닫힌집합이어서 ([§옹골공간, ⁋따름정리 5](/ko/math/topology/compact_spaces#cor5)) $Y\setminus C$는 $p$를 품는 $Y$의 열린집합이다.

그러므로 $p$를 $\infty$와 동일시하는 집합 사이의 대응 $h:X^+\rightarrow Y$는 열린집합을 열린집합으로, 그 역도 마찬가지로 대응시키는 전단사이며, 따라서 homeomorphism이다. $h$는 $X$ 위에서 $\varphi$와 일치하고 $\infty$를 $p$로 보내야 하므로 유일하다.
:::

[정리 12](#thm12)은 LCH space $X$에 한 점을 더해 compact Hausdorff space를 만드는 방법이 homeomorphism을 무시하면 오직 하나뿐임을 말한다. 이것이 Alexandroff 정리의 유일성 부분을 보편성의 언어로 서술한 것이다. 이 유일성 덕분에 우리는 이후 $X^+$를 그 구체적 구성과 무관하게 다룰 수 있고, 실제 계산에서는 임의의 편리한 compact Hausdorff model을 골라 $X^+$와 동일시하면 된다.

{% diagram Math/Topology/Locally_Compact_Spaces-1.svg width="6.23em" alt="일점 옹골화의 보편성" %}

::: 참고 13
One-point compactification은 Hausdorff 옹골화 가운데 가장 작은 것으로 특징지어진다. Compact가 아닌 LCH space $X$의 *Hausdorff 옹골화*란 $X$를 조밀한 부분공간으로 품는 compact Hausdorff space를 말하는데, 이러한 임의의 옹골화에서 출발하여 $X$ 바깥의 점들을 모두 하나로 뭉개면 $X^+$로 향하는 연속인 전사가 유일하게 얻어진다. 이 사실의 증명에는 LCH space가 Hausdorff space에 조밀하게 매장되면 항상 열린 부분공간이 된다는 관찰이 필요하며, 자세한 논증은 표준적인 문헌을 따른다. **[Mun]** 반대편 극단에는 완전정칙 공간이 가질 수 있는 가장 큰 Hausdorff 옹골화인 *Stone–Čech compactification*이 있으나, 이는 별도의 구성을 요구하므로 여기에서는 이름만 언급한다.
:::

## 일점 옹골화의 예

가장 익숙한 예는 Euclidean space의 one-point compactification이 구면이 된다는 사실이다.

::: 예시 14
$n$-구면 $S^n=\{x\in\mathbb{R}^{n+1}:\lVert x\rVert=1\}$의 북극 $N=(0,\ldots,0,1)$을 생각하자. Stereographic projection

$$\sigma:S^n\setminus\{N\}\rightarrow\mathbb{R}^n,\qquad \sigma(x_1,\ldots,x_{n+1})=\frac{1}{1-x_{n+1}}(x_1,\ldots,x_n)$$

은 $S^n\setminus\{N\}$과 $\mathbb{R}^n$ 사이의 homeomorphism임이 잘 알려져 있다. $S^n$은 $\mathbb{R}^{n+1}$의 닫힌 유계 부분집합이므로 Heine–Borel 정리에 의해 compact이고, 부분공간으로서 Hausdorff이다. 따라서 $S^n$은 compact Hausdorff space이고 $N$이라는 한 점을 제거한 것이 $\mathbb{R}^n$과 homeomorphic하므로, [정리 12](#thm12)에 의하여 유일한 homeomorphism

$$(\mathbb{R}^n)^+\cong S^n$$

이 성립하며 무한원점 $\infty$가 북극 $N$에 대응한다. 특히 $(\mathbb{R})^+$은 원 $S^1$이다.
:::

Discrete space의 one-point compactification은 수렴하는 점열이라는 매우 구체적인 그림을 준다.

::: 예시 15
자연수 집합 $\mathbb{N}=\{1,2,3,\ldots\}$에 discrete topology를 주자. 이는 discrete space로서 LCH이므로 [정리 11](#thm11)에 의하여 $\mathbb{N}^+$은 compact Hausdorff space이다. Discrete space에서 compact인 부분집합은 유한집합뿐이므로, $\mathbb{N}^+$에서 $\infty$의 열린근방은 유한집합의 여집합, 곧 $\infty$를 품는 cofinite set이다. 이는 정확히 $\mathbb{N}$의 점열이 $\infty$로 수렴한다는 것이 그 점열이 임의의 유한집합을 결국 벗어난다는 것과 같음을 뜻한다.

이 공간은 실수 안의 익숙한 집합으로 실현된다. 함수

$$f:\mathbb{N}^+\rightarrow\mathbb{R},\qquad f(n)=\frac1n\quad(n\in\mathbb{N}),\qquad f(\infty)=0$$

을 생각하면, $f$는 $\mathbb{N}^+$과 $\{0\}\cup\{1/n\mid n\geq 1\}$ 사이의 전단사이다. 각 $n\in\mathbb{N}$은 $\mathbb{N}^+$에서 isolated point이고 그 상 $1/n$도 $\{0\}\cup\{1/n\}$에서 isolated point이며, $\infty$의 cofinite 근방이 $0$의 근방으로 옮겨지므로 $f$는 연속이다. 정의역이 compact이고 공역이 Hausdorff이므로 [§옹골공간, ⁋명제 9](/ko/math/topology/compact_spaces#prop9)에 의하여 $f$는 homeomorphism이다. 즉 $\mathbb{N}^+$은 하나의 limit point를 지닌 수렴하는 점열과 homeomorphic이다.
:::

## 완전정칙성

One-point compactification은 존재론적 도구에 그치지 않고 LCH space의 내적 성질을 규명하는 데에도 쓰인다. Compact Hausdorff space는 normal이므로 ([§옹골공간, ⁋명제 7](/ko/math/topology/compact_spaces#prop7)) Urysohn 보조정리를 통해 풍부한 연속함수를 지니는데, 이 성질이 열린 부분공간을 거쳐 LCH space로 유전됨을 보인다.

::: 따름정리 16
임의의 LCH space는 completely regular이다. 따라서 임의의 LCH space는 Tychonoff space이다. ([§하우스도르프 공간, ⁋정의 3](/ko/math/topology/Hausdorff_spaces#def3))
:::
::: 증명
먼저 임의의 compact Hausdorff space $Y$가 completely regular임을 보인다. 점 $p\in Y$와 이를 포함하지 않는 닫힌집합 $C\subseteq Y$가 주어졌다 하자. $Y$는 Hausdorff이므로 $T_1$이고 따라서 $\{p\}$는 닫힌집합이며, $\{p\}$와 $C$는 서로소인 두 닫힌집합이다. $Y$는 normal이므로 ([§옹골공간, ⁋명제 7](/ko/math/topology/compact_spaces#prop7)) Urysohn 보조정리에 의하여 연속함수 $g:Y\rightarrow[0,1]$이 존재하여 $\{p\}$에서 $0$, $C$에서 $1$의 값을 갖는다. ([§Urysohn 보조정리와 Tietze 확장정리, ⁋정리 2](/ko/math/topology/urysohn_and_tietze#thm2)) 이는 곧 $p$와 $C$가 연속함수로 분리가능함을 뜻하므로 $Y$는 completely regular이다.

이제 $X$가 LCH라 하자. [정리 10](#thm10)과 [정리 11](#thm11)에 의하여 $X^+$는 compact Hausdorff space이므로 위에서 본 대로 completely regular이다. $X$는 [명제 9](#prop9)에 의해 $X^+$의 부분공간이다. 완전정칙성은 부분공간으로 유전됨을 보이자. $x\in X$와 이를 포함하지 않는 $X$의 닫힌집합 $C$가 주어지면, 부분공간의 닫힌집합의 성질에 의해 $X^+$의 닫힌집합 $C'$이 존재하여 $C=C'\cap X$이다. $x\in X$이고 $x\notin C$이므로 $x\notin C'$이며, $X^+$가 completely regular이므로 연속함수 $g:X^+\rightarrow[0,1]$이 존재하여 $g(x)=0$이고 $C'$에서 $1$의 값을 갖는다. $g$를 $X$로 제한한 $g\vert_X$는 연속함수로서 $x$와 $C\subseteq C'$을 분리하므로 $X$는 completely regular이다. 끝으로 $X$는 Hausdorff이므로 $T_0$이고, 따라서 $X$는 Tychonoff space이다.
:::

[따름정리 16](#cor16)는 LCH space 위에서 서로 다른 점을 가르거나 점과 닫힌집합을 가르는 연속함수를 언제나 얻을 수 있음을 보장한다. 이는 locally compact space가 해석학적 대상으로서 얼마나 잘 행동하는지를 말해 주는 기본적인 사실이며, 국소적으로 정의된 자료를 연속함수의 도움으로 전역적으로 이어 붙이는 여러 구성의 출발점이 된다.

---

**참고문헌**

**[Mun]** J. R. Munkres, *Topology*, 2nd ed., Prentice Hall, 2000.

**[Wil]** S. Willard, *General Topology*, Addison-Wesley, 1970.

**[Kel]** J. L. Kelley, *General Topology*, Springer, 1975.

## 국소성과 대역성의 가교

위상공간 위에서 우리가 다루려는 대상은 흔히 국소적으로 먼저 주어진다. 각 점 근방에서 정의된 연속함수, 국소적으로 얻어진 절단, 좌표조각마다 놓인 구성이 그러하다. 이러한 국소적 자료를 하나의 대역적 대상으로 이어 붙이려면, 각 조각을 자기 정의역 안에서 부드럽게 소멸시키면서 전체에 걸쳐 값이 겹치지 않게 배분하는 장치가 필요하다. 이 역할을 하는 표준적인 도구가 *partition of unity*이며, 그것이 자연스럽게 존재하는 무대가 바로 이 글에서 다루는 paracompact Hausdorff 공간이다.

Compactness는 임의의 열린 덮개에서 유한한 부분덮개를 뽑아낼 것을 요구하지만 ([§옹골공간, ⁋정의 1](/ko/math/topology/compact_spaces#def1)), 우리가 실제로 다루는 공간의 대부분은 compact가 아니다. Paracompactness는 유한성 대신 국소유한성을 요구하여 compactness를 알맞게 약화시킨 조건으로, compact 공간에서 성립하던 여러 논증을 국소적으로 되살릴 수 있게 해 준다. 우리는 이 개념을 도입하고, paracompact Hausdorff 공간이 normal임을 보인 뒤, 이를 발판으로 임의의 열린 덮개에 종속된 partition of unity를 언제나 구성할 수 있음을 증명한다.

## Paracompact 공간

열린 덮개를 더 잘게 쪼개어 각 조각이 원래 덮개의 어느 한 조각 안에 온전히 들어가도록 만드는 조작을 먼저 이름 붙인다.

::: 정의 17
위상공간 $X$의 두 덮개 $(U_i)_{i\in I}$와 $(V_j)_{j\in J}$가 주어졌다 하자. 후자가 전자의 *세분<sub>refinement</sub>*이라는 것은 임의의 $j\in J$에 대하여 $V_j\subseteq U_i$를 만족하는 $i\in I$가 존재하는 것이다. 세분 $(V_j)_{j\in J}$의 모든 원소가 열린집합일 때 이를 *open refinement<sub>열린 세분</sub>*라 부른다.
:::

세분은 부분덮개보다 훨씬 유연한 개념이다. 부분덮개가 원래 덮개의 조각들 가운데 일부를 그대로 골라내는 것인 데 반해, 세분은 각 조각을 원래의 어느 한 조각 안에 갇히기만 하면 자유롭게 잘게 나누는 것을 허용한다. 여기에 국소유한성을 결합하면 compactness를 대신할 새로운 유한성 조건을 얻는다. Family $(A_i)_{i\in I}$가 *locally finite*라는 것은 임의의 점이 유한 개의 $A_i$만을 만나는 근방을 갖는 것이었음을 상기한다. ([§집합의 내부, 폐포, 경계, ⁋정의 3](/ko/math/topology/other_concepts#def3))

::: 정의 18
위상공간 $X$가 *paracompact<sub>파라콤팩트</sub>*라는 것은 $X$의 임의의 open covering이 locally finite open refinement를 갖는 것이다.
:::

정의는 임의의 열린 덮개에 대하여 그것을 세분하는 국소유한 열린 덮개가 존재할 것을 요구한다. Compactness가 요구하는 것은 임의의 열린 덮개에서 유한 개만 남겨도 여전히 전체를 덮는다는 것인데, 유한 개의 열린집합으로 이루어진 덮개는 그 자체로 국소유한이므로, paracompactness는 compactness가 요구하는 유한성을 각 점 주위에서의 유한성으로 완화한 것이라 읽을 수 있다.

::: 명제 19
임의의 compact space는 paracompact이다.
:::
::: 증명
$X$가 compact space라 하고 open covering $(U_i)_{i\in I}$가 주어졌다 하자. Compactness에 의하여 유한한 $J\subseteq I$가 존재하여 $(U_j)_{j\in J}$가 여전히 $X$를 덮는다. ([§옹골공간, ⁋정의 1](/ko/math/topology/compact_spaces#def1)) 이 유한한 부분덮개는 원래 덮개의 open refinement이며, 유한한 family는 언제나 locally finite이므로 ([§집합의 내부, 폐포, 경계, ⁋정의 3](/ko/math/topology/other_concepts#def3)) 이는 $(U_i)_{i\in I}$의 locally finite open refinement이다. 따라서 $X$는 paracompact이다.
:::

Paracompactness가 compactness보다 실질적으로 넓은 조건임은 compact가 아닌 공간에서 확인해야 한다. 다음은 그 대표적인 경우로, 유한성이 전혀 없는 Euclidean space에서도 국소유한 세분을 명시적으로 만들어 낼 수 있음을 보여 준다.

::: 예시 20
Euclidean space $\mathbb{R}^n$은 paracompact이다. $\mathbb{R}^n$은 유계가 아니어서 compact가 아니지만, 원점을 중심으로 반경이 커지는 열린 공들로 공간을 소진시켜 국소유한 세분을 얻을 수 있다.

임의의 open covering $\mathcal{U}=(U_i)_{i\in I}$가 주어졌다 하자. 각 정수 $k\geq 1$에 대하여 반경 $k$인 열린 공 $B_k=\{x:\lVert x\rVert<k\}$을 두고, $B_0=B_{-1}=\emptyset$이라 약속한다. 그럼 껍질

$$A_k=\cl(B_k)\setminus B_{k-1}=\{x: k-1\leq\lVert x\rVert\leq k\}$$

은 $\mathbb{R}^n$의 닫힌 유계 부분집합이므로 Heine–Borel 정리에 의해 compact이고, 이들의 합집합은 $\mathbb{R}^n$ 전체이다. 한편

$$O_k=B_{k+1}\setminus\cl(B_{k-2})$$

은 열린집합으로 $A_k\subseteq O_k$를 만족한다. 여기서 $k\geq 3$이면 $O_k=\{x: k-2<\lVert x\rVert<k+1\}$이고, $k=1,2$일 때는 $B_{k-2}=\emptyset$이라 $\cl(B_{k-2})=\emptyset$이므로 $O_k=B_{k+1}$이다.

이제 각 $k$에 대하여 compact 집합 $A_k$를 다룬다. 각 $x\in A_k$는 어떤 $U_{i}$에 속하므로 $x\in U_i\cap O_k$이며, 이러한 열린집합들이 $A_k$를 덮는다. $A_k$가 compact이므로 유한 개의 $i$, 곧 유한집합 $F_k\subseteq I$를 택하여 $(U_i\cap O_k)_{i\in F_k}$이 $A_k$를 덮도록 할 수 있다. ([§옹골공간, ⁋명제 2](/ko/math/topology/compact_spaces#prop2)) 모든 $k\geq 1$에 걸쳐 모은 family

$$\mathcal{V}=(U_i\cap O_k)_{k\geq 1,i\in F_k}$$

를 생각하자. 각 원소는 열린집합이며 $U_i$에 포함되므로 $\mathcal{V}$는 $\mathcal{U}$의 open refinement이고, $A_k$들이 $\mathbb{R}^n$을 덮으므로 $\mathcal{V}$도 $\mathbb{R}^n$을 덮는다. 끝으로 $\mathcal{V}$가 locally finite임을 본다. 점 $x$에 대하여 $r=\lVert x\rVert$이라 두면 근방 $B_{r+1}=\{y:\lVert y\rVert<r+1\}$은 $O_k$와 만나는 경우 $k-2<r+1$, 곧 $k<r+3$일 때뿐이므로 유한 개의 $k$에 대해서만 $O_k$와 만난다. 각 $k$마다 $\mathcal{V}$의 원소는 유한 개($\lvert F_k\rvert$개)뿐이므로, $B_{r+1}$은 $\mathcal{V}$의 유한히 많은 원소만을 만난다. 따라서 $\mathcal{V}$는 locally finite open refinement이고 $\mathbb{R}^n$은 paracompact이다.
:::

이 예시의 논증은 $\mathbb{R}^n$의 특수성보다는 두 가지 성질, 곧 국소적 옹골성과 가산 개의 compact 집합으로의 소진에만 의존한다. 실제로 같은 방법으로 임의의 second countable LCH space, 나아가 가산 개의 compact 부분집합의 합집합으로 적히는 임의의 LCH space가 paracompact임을 보일 수 있다. 이는 뒤에서 다룰 topological manifold의 paracompactness의 바탕이 된다.

## Paracompact Hausdorff 공간의 정규성

Paracompactness의 위력은 Hausdorff 조건과 결합될 때 비로소 드러난다. Compact Hausdorff space가 normal이었던 것과 마찬가지로 ([§옹골공간, ⁋명제 7](/ko/math/topology/compact_spaces#prop7)), paracompact Hausdorff space도 normal임을 보이는 것이 이 절의 목표이다. 정규성이 확보되면 Urysohn 보조정리를 통해 풍부한 연속함수를 얻을 수 있고, 이것이 partition of unity 구성의 핵심 재료가 된다. ([§Urysohn 보조정리와 Tietze 확장정리, ⁋정리 2](/ko/math/topology/urysohn_and_tietze#thm2))

증명은 국소유한 family의 다음 성질에 반복적으로 의존한다. 국소유한 family에서는 합집합의 closure가 각 원소의 closure의 합집합과 일치하여, closure 연산이 무한 합집합과 자유롭게 교환된다.

::: 보조정리 21
위상공간 $X$의 부분집합들의 family $(A_i)_{i\in I}$가 locally finite라 하자. 그럼

$$\cl\Bigl(\bigcup_{i\in I} A_i\Bigr)=\bigcup_{i\in I}\cl(A_i)$$

가 성립한다.
:::
::: 증명
각 $i$에 대하여 $A_i\subseteq\bigcup_j A_j$이므로 $\cl(A_i)\subseteq\cl(\bigcup_j A_j)$이고, 따라서 $\bigcup_i\cl(A_i)\subseteq\cl(\bigcup_j A_j)$이다.

반대 포함을 위해 $\bigcup_i\cl(A_i)$가 닫힌집합임을 보이면 충분하다. 이 집합이 닫혀 있으면 $\bigcup_i A_i\subseteq\bigcup_i\cl(A_i)$의 closure 역시 $\bigcup_i\cl(A_i)$에 포함되기 때문이다. 먼저 family $(\cl(A_i))_{i\in I}$가 locally finite임을 관찰한다. 점 $x$의 근방 $V$가 $V\cap A_i\neq\emptyset$을 만족하는 $i$를 유한 개만 갖도록 잡을 수 있는데, $V$를 열린집합으로 택하면 $V\cap\cl(A_i)\neq\emptyset$일 때마다 $V$가 $\cl(A_i)$의 점의 근방이므로 $V\cap A_i\neq\emptyset$이다. 따라서 $V$는 유한 개의 $\cl(A_i)$만을 만나며, $(\cl(A_i))_{i\in I}$도 locally finite이다. 이는 닫힌집합들의 locally finite family이므로 그 합집합 $\bigcup_i\cl(A_i)$는 닫힌집합이다. ([§집합의 내부, 폐포, 경계, ⁋명제 4](/ko/math/topology/other_concepts#prop4))
:::

이제 paracompact Hausdorff space가 regular임을 먼저 보인다. 논증의 골격은 다음과 같다. 점과 닫힌집합을 분리하려 할 때, Hausdorff성으로부터 닫힌집합의 각 점을 그 점의 closure가 문제의 점을 피하도록 감싸는 열린집합을 얻고, 이들과 닫힌집합의 여집합으로 이루어진 열린 덮개를 paracompactness로 국소유한하게 세분한 뒤 [보조정리 21](#lem21)로 closure를 통제한다.

::: 명제 22
임의의 paracompact Hausdorff space는 regular space이다. ([§하우스도르프 공간, ⁋정의 3](/ko/math/topology/Hausdorff_spaces#def3))
:::
::: 증명
$X$가 paracompact Hausdorff space라 하고, 점 $a\in X$와 이를 포함하지 않는 닫힌집합 $B\subseteq X$가 주어졌다 하자. 각 $b\in B$에 대하여 $a\neq b$이므로 $X$의 Hausdorff성에 의해 서로소인 열린집합 $P_b\ni a$와 $U_b\ni b$가 존재한다. $U_b\subseteq X\setminus P_b$이고 $X\setminus P_b$는 닫힌집합이므로 $\cl(U_b)\subseteq X\setminus P_b$이며, 특히 $a\notin\cl(U_b)$이다.

Family $(U_b)_{b\in B}$에 열린집합 $X\setminus B$를 더하면 $X$의 open covering을 이룬다. $X$가 paracompact이므로 이 덮개의 locally finite open refinement $\mathcal{C}$를 택한다. $\mathcal{C}$의 원소 가운데 $B$와 만나는 것들을 모아 $\mathcal{D}=\{C\in\mathcal{C}\mid C\cap B\neq\emptyset\}$이라 두자. $\mathcal{D}$의 각 원소 $C$는 세분의 성질에 의해 $X\setminus B$나 어떤 $U_b$에 포함되는데, $C$가 $B$와 만나므로 $X\setminus B$에는 포함될 수 없고 따라서 어떤 $U_b$에 포함되어 $a\notin\cl(C)$이다. 또한 $B$의 각 점은 자신을 품는 $\mathcal{C}$의 원소에 속하고 그 원소는 $B$와 만나므로 $\mathcal{D}$에 든다. 즉 $\mathcal{D}$는 $B$를 덮는다.

$V=\bigcup\mathcal{D}$라 두면 $V$는 $B$를 포함하는 열린집합이다. $\mathcal{D}$는 locally finite family $\mathcal{C}$의 부분족이므로 locally finite이고, [보조정리 21](#lem21)에 의하여 $\cl(V)=\bigcup_{C\in\mathcal{D}}\cl(C)$이다. 각 $\cl(C)$가 $a$를 포함하지 않으므로 $a\notin\cl(V)$이다. 그럼 $W=X\setminus\cl(V)$은 $a$를 품는 열린집합이며 $V\supseteq B$와 서로소이다. 따라서 $a$와 $B$는 근방으로 분리가능하고 $X$는 regular이다.
:::

같은 논증을 점 $a$ 대신 닫힌집합 $A$에 대해 펼치면 정규성을 얻는다. 이때 Hausdorff성 대신 방금 증명한 regularity를 사용하여 $B$의 각 점을 감싸는 열린집합의 closure가 $A$를 피하도록 만든다.

::: 정리 23
임의의 paracompact Hausdorff space는 normal space이다. ([§하우스도르프 공간, ⁋정의 3](/ko/math/topology/Hausdorff_spaces#def3))
:::
::: 증명
$X$가 paracompact Hausdorff space라 하고 서로소인 두 닫힌집합 $A,B\subseteq X$가 주어졌다 하자. $X$는 [명제 22](#prop22)에 의하여 regular이다. 각 $b\in B$에 대하여 $b\notin A$이므로 regularity를 점 $b$와 닫힌집합 $A$에 적용하면 서로소인 열린집합 $U_b\ni b$와 $Q_b\supseteq A$를 얻는다. $U_b\subseteq X\setminus Q_b$이고 $X\setminus Q_b$가 닫힌집합이므로 $\cl(U_b)\subseteq X\setminus Q_b\subseteq X\setminus A$이며, 곧 $\cl(U_b)\cap A=\emptyset$이다.

Family $(U_b)_{b\in B}$에 열린집합 $X\setminus B$를 더한 open covering의 locally finite open refinement $\mathcal{C}$를 paracompactness로 택하고, $\mathcal{D}=\{C\in\mathcal{C}\mid C\cap B\neq\emptyset\}$이라 두자. [명제 22](#prop22)의 증명에서와 같이 $\mathcal{D}$의 각 원소는 어떤 $U_b$에 포함되어 $\cl(C)\cap A=\emptyset$이고, $\mathcal{D}$는 $B$를 덮는다.

$V=\bigcup\mathcal{D}$는 $B$를 포함하는 열린집합이며, $\mathcal{D}$가 locally finite이므로 [보조정리 21](#lem21)에 의하여 $\cl(V)=\bigcup_{C\in\mathcal{D}}\cl(C)$이고 이는 $A$와 서로소이다. 따라서 $W=X\setminus\cl(V)$은 $A$를 품는 열린집합으로 $V\supseteq B$와 서로소이다. 그럼 $V$와 $W$가 각각 $B$와 $A$를 담는 서로소인 열린집합이므로 $X$는 normal이다.
:::

[정리 23](#thm23)은 compact Hausdorff space가 normal이라는 사실의 진정한 일반화이다. 실제로 [명제 19](#prop19)에 의하여 compact space는 paracompact이므로, compact Hausdorff space가 normal이라는 결과는 [정리 23](#thm23)의 특수한 경우로 다시 얻어진다. 정규성이 확보되었으므로 우리는 이제 서로소인 두 닫힌집합을 가르는 연속함수를 언제나 얻을 수 있으며, 이것이 다음 절의 partition of unity 구성을 가능하게 한다.

Paracompact 공간의 가장 풍부한 공급원 가운데 하나는 metric space이다. 모든 metric space가 normal임은 이미 알고 있으나 ([§Urysohn 보조정리와 Tietze 확장정리, ⁋명제 4](/ko/math/topology/urysohn_and_tietze#prop4)), 사실 이들은 언제나 paracompact이기도 하다. 이는 A. H. Stone의 정리로 알려져 있다.

::: 정리 24 (Stone)
임의의 metric space는 paracompact이다.
:::
::: 증명
증명의 핵심 착상만 밝히고 세부는 표준적인 문헌을 따른다. **[Mun]** Metric $d$를 가진 공간 $X$와 open covering $(U_\alpha)_{\alpha\in J}$가 주어졌다 하자. 우선 선택공리를 사용하여 index set $J$에 well-ordering을 준다. 각 정수 $n\geq 1$과 각 $\alpha$에 대하여, $U_\alpha$의 점 가운데 경계로부터 적어도 $2^{-n}$만큼 떨어져 있고, 순서상 앞선 어떤 $U_\beta$의 그러한 대응 집합에도 이미 들어 있지 않으며, 이전 단계 $n'<n$에서 이미 덮인 점도 아닌 점들만을 남긴 뒤, 그 점들을 중심으로 반경 $2^{-n-1}$인 열린 공들을 합쳐 집합 $V_{n,\alpha}$을 정의한다. 이때 $\alpha$에 대한 well-ordering과 반경의 기하급수적 축소가 맞물려, family $(V_{n,\alpha})$는 $(U_\alpha)$를 세분하는 열린 덮개가 되며 동시에 locally finite이다. 각 점 $x$에 대하여, $x$가 처음 덮이는 단계의 지표 $n$을 보면 반경 $2^{-n-1}$ 정도의 근방이 유한히 많은 $V_{n',\alpha}$만을 만나기 때문이다. 따라서 $X$는 paracompact이다. 이 구성은 M. E. Rudin이 정리한 형태로 널리 알려져 있다.
:::

## 단위분할의 존재

이제 국소적 자료를 대역적으로 이어 붙이는 도구인 partition of unity를 정식화한다. 연속함수 $\phi:X\rightarrow[0,1]$의 *support<sub>지지</sub>*를 $\supp\phi=\cl(\{x\in X\mid\phi(x)\neq 0\})$으로 정의하며, 이는 $\phi$가 $0$이 아닌 값을 갖는 영역을 담는 가장 작은 닫힌집합이다.

::: 정의 25
위상공간 $X$ 위의 연속함수들의 family $(\phi_i)_{i\in I}$가 *partition of unity<sub>단위분할</sub>*이라는 것은 각 $\phi_i:X\rightarrow[0,1]$이 다음 두 조건을 만족하는 것이다.

1. Family $(\supp\phi_i)_{i\in I}$는 locally finite이다.
2. 임의의 $x\in X$에 대하여 $\sum_{i\in I}\phi_i(x)=1$이 성립한다.

나아가 $X$의 open covering $(U_i)_{i\in I}$가 주어졌을 때, 같은 index set으로 놓인 partition of unity $(\phi_i)_{i\in I}$가 모든 $i$에 대하여 $\supp\phi_i\subseteq U_i$를 만족하면 이를 *$(U_i)$에 종속된<sub>subordinate</sub>* partition of unity라 부른다.
:::

첫째 조건의 국소유한성은 둘째 조건의 합 $\sum_i\phi_i(x)$이 각 점의 어떤 근방에서 유한합으로 환원되어 실제로 의미를 가지도록 보장한다. 종속성 조건 $\supp\phi_i\subseteq U_i$은 각 $\phi_i$가 $U_i$ 바깥에서는 물론 $U_i$의 경계 부근에서까지 소멸함을 뜻하므로, $U_i$ 위에서만 정의된 국소적 자료에 $\phi_i$를 곱하면 그 곱을 $X$ 전체로 $0$을 채워 연속적으로 연장할 수 있게 된다. 이것이 partition of unity가 국소 구성을 대역화하는 원리이다.

존재 증명의 관건은 정규성만으로는 부족하고, 덮개를 두 번 "수축"시켜 닫힌집합이 여전히 전체를 덮게 만드는 데에 있다. 이를 위한 보조정리를 먼저 마련한다. Family $(U_i)_{i\in I}$가 *point-finite<sub>점별유한</sub>*라는 것은 각 점 $x\in X$가 유한 개의 $U_i$에만 속하는 것을 말하며, locally finite family는 언제나 point-finite이다.

::: 보조정리 26 (Shrinking lemma)
Normal space $X$의 point-finite open covering $(U_\alpha)_{\alpha\in J}$가 주어졌다 하자. 그럼 open covering $(V_\alpha)_{\alpha\in J}$가 존재하여 모든 $\alpha$에 대하여 $\cl(V_\alpha)\subseteq U_\alpha$가 성립한다.
:::
::: 증명
선택공리를 사용하여 index set $J$에 well-ordering을 준다. 우리는 초한귀납법으로 각 $\alpha\in J$마다 열린집합 $V_\alpha$를 정의하되, 다음의 불변식이 모든 단계에서 유지되도록 한다.

$$(\ast_\alpha)\qquad \{V_\beta\mid\beta<\alpha\}\cup\{U_\beta\mid\beta\geq\alpha\}\ \text{가}\ X\ \text{를 덮는다.}$$

먼저 $(\ast_\alpha)$가 임의의 $\alpha$에서 성립함을 point-finiteness로부터 확인한다. $\beta<\alpha$인 각 $\beta$에 대해 이미 $V_\beta$가 $\cl(V_\beta)\subseteq U_\beta$를 만족하도록 정의되었다고 하자. 점 $x\in X$가 주어지면 $x$는 유한 개의 $U_\gamma$에만 속한다. 만일 이들 가운데 $\gamma\geq\alpha$인 것이 있으면 $x$는 $U_\gamma$로 덮인다. 그렇지 않다면 $x\in U_\gamma$인 모든 $\gamma$는 $\alpha$보다 작으며, 이러한 $\gamma$ 가운데 가장 큰 것을 $\gamma_0$이라 하자. $\gamma_0$ 단계를 마친 뒤 성립하는 덮개성에 의하여 $x$는 $\{V_\beta\mid\beta\leq\gamma_0\}\cup\{U_\beta\mid\beta>\gamma_0\}$ 가운데 하나로 덮이는데, $\gamma_0$의 최대성에 의해 $\beta>\gamma_0$이면 $x\notin U_\beta$이므로 $x$는 어떤 $V_\beta$($\beta\leq\gamma_0<\alpha$)로 덮인다. 어느 경우든 $x$는 $(\ast_\alpha)$의 family로 덮이므로 $(\ast_\alpha)$가 성립한다.

이제 $\beta<\alpha$에 대해 $V_\beta$가 정의되었다 할 때 $V_\alpha$를 정의한다. 집합

$$C_\alpha=X\setminus\Bigl(\bigcup_{\beta<\alpha}V_\beta\cup\bigcup_{\beta>\alpha}U_\beta\Bigr)$$

은 닫힌집합이다. $(\ast_\alpha)$에 의하여 이 합집합의 밖에 있는 점, 곧 $C_\alpha$의 점은 어떤 $V_\beta$($\beta<\alpha$)나 $U_\beta$($\beta>\alpha$)에도 속하지 않으므로 반드시 $U_\alpha$에 속한다. 즉 $C_\alpha\subseteq U_\alpha$이다. $X$가 normal이므로 닫힌집합 $C_\alpha$와 이를 포함하는 열린집합 $U_\alpha$에 대하여 열린집합 $V_\alpha$가 존재하여 $C_\alpha\subseteq V_\alpha\subseteq\cl(V_\alpha)\subseteq U_\alpha$이도록 할 수 있다. ([§Urysohn 보조정리와 Tietze 확장정리, ⁋보조정리 1](/ko/math/topology/urysohn_and_tietze#lem1)) 그럼 $C_\alpha\subseteq V_\alpha$이므로 $\{V_\beta\mid\beta\leq\alpha\}\cup\{U_\beta\mid\beta>\alpha\}$이 $X$를 덮어 다음 단계의 불변식을 잇는다.

끝으로 이렇게 얻은 $(V_\alpha)_{\alpha\in J}$이 $X$를 덮음을 본다. 점 $x$가 속하는 $U_\gamma$는 유한 개뿐이므로 그 지표 가운데 가장 큰 것을 $\gamma_0$이라 하면, $\gamma_0$ 단계를 마친 뒤 성립하는 덮개성과 $\gamma_0$의 최대성에 의해 앞에서와 같이 $x$는 어떤 $V_\beta$($\beta\leq\gamma_0$)로 덮인다. 따라서 $(V_\alpha)_{\alpha\in J}$는 $X$의 open covering이며 각 $\alpha$에 대해 $\cl(V_\alpha)\subseteq U_\alpha$를 만족한다.
:::

Point-finiteness가 초한귀납의 극한 단계와 최종 단계에서 덮개성을 유지하는 데에 결정적으로 쓰였음에 유의한다. Well-ordering만으로는 무한히 많은 $U_\beta$를 한꺼번에 $V_\beta$로 갈아치울 때 어떤 점이 덮이지 않을 위험이 있으나, 각 점이 유한 개의 조각에만 속한다는 사실이 그 점이 덮이는 단계를 유한한 곳에서 붙들어 준다. 이제 주요 정리를 증명할 준비가 되었다.

::: 정리 27
Paracompact Hausdorff space $X$의 임의의 open covering $(U_\alpha)_{\alpha\in J}$에 대하여, $(U_\alpha)$에 종속된 partition of unity가 존재한다.
:::
::: 증명
증명은 네 단계로 이루어진다. 먼저 덮개를 같은 첨수로 놓인 국소유한 세분으로 바꾸고, 이를 두 번 수축시켜 닫힌 덮개를 얻은 뒤, Urysohn 보조정리로 각 조각의 bump 함수를 만들고, 마지막으로 이들을 정규화한다.

**(1) 정밀 국소유한 세분.** $X$가 paracompact이므로 $(U_\alpha)$의 locally finite open refinement $(W_\beta)_{\beta\in K}$이 존재한다. 세분의 정의에 의해 각 $\beta$마다 $W_\beta\subseteq U_{\alpha(\beta)}$인 $\alpha(\beta)\in J$를 하나 고른다. 이제 각 $\alpha\in J$에 대하여

$$V_\alpha=\bigcup\{W_\beta\mid\alpha(\beta)=\alpha\}$$

이라 두자 (해당하는 $\beta$가 없으면 $V_\alpha=\emptyset$). 그럼 $V_\alpha$는 열린집합이고 $V_\alpha\subseteq U_\alpha$이며, $W_\beta$들이 $X$를 덮으므로 $(V_\alpha)_{\alpha\in J}$도 $X$를 덮는다. 또한 점 $x$의 근방이 유한 개의 $W_\beta$만을 만나면 유한 개의 $V_\alpha$만을 만나므로 ($V_\alpha$와 만나는 근방은 $\alpha(\beta)=\alpha$인 어떤 $W_\beta$와도 만나기 때문이다) $(V_\alpha)_{\alpha\in J}$는 locally finite이다. 이로써 $V_\alpha\subseteq U_\alpha$를 만족하는 국소유한 open covering을 같은 index set $J$ 위에서 얻었다.

**(2) 두 번의 수축.** $X$는 [정리 23](#thm23)에 의하여 normal이고, locally finite인 $(V_\alpha)$는 point-finite이다. [보조정리 26](#lem26)을 $(V_\alpha)$에 적용하여 open covering $(P_\alpha)_{\alpha\in J}$을 얻는데, 모든 $\alpha$에 대해 $\cl(P_\alpha)\subseteq V_\alpha$이다. $P_\alpha\subseteq V_\alpha$이므로 $(P_\alpha)$도 point-finite이며, 여기에 [보조정리 26](#lem26)을 다시 적용하여 open covering $(Q_\alpha)_{\alpha\in J}$을 얻는다. 모든 $\alpha$에 대해 $\cl(Q_\alpha)\subseteq P_\alpha$이다. 정리하면 두 덮개 $(P_\alpha)$와 $(Q_\alpha)$가 모두 $X$를 덮으면서

$$\cl(Q_\alpha)\subseteq P_\alpha\subseteq\cl(P_\alpha)\subseteq V_\alpha\subseteq U_\alpha$$

를 만족한다.

**(3) Bump 함수.** 각 $\alpha$에 대하여 $\cl(Q_\alpha)$와 $X\setminus P_\alpha$는 서로소인 두 닫힌집합이다. $X$가 normal이므로 Urysohn 보조정리에 의하여 연속함수 $\psi_\alpha:X\rightarrow[0,1]$이 존재하여 $\cl(Q_\alpha)$에서 $1$의 값을, $X\setminus P_\alpha$에서 $0$의 값을 갖는다. ([§Urysohn 보조정리와 Tietze 확장정리, ⁋정리 2](/ko/math/topology/urysohn_and_tietze#thm2)) 그럼 $\{x\mid\psi_\alpha(x)\neq 0\}\subseteq P_\alpha$이므로

$$\supp\psi_\alpha=\cl(\{x\mid\psi_\alpha(x)\neq 0\})\subseteq\cl(P_\alpha)\subseteq V_\alpha\subseteq U_\alpha$$

이다. 특히 $(\supp\psi_\alpha)_{\alpha\in J}$는 $\supp\psi_\alpha\subseteq V_\alpha$이고 $(V_\alpha)$가 locally finite이므로 locally finite이다.

**(4) 정규화.** Family $(\psi_\alpha)$가 locally finite인 support를 가지므로, 각 점 $x$는 유한 개의 $\psi_\alpha$만이 $0$이 아닌 근방을 가진다. 그 근방 위에서 합 $\psi=\sum_{\alpha\in J}\psi_\alpha$은 유한합이고, 연속함수의 유한합은 연속이므로 $\psi$는 그 근방에서 연속이다. 연속성은 국소적 성질이므로 $\psi:X\rightarrow\mathbb{R}$은 연속함수이다. 또한 $(Q_\alpha)$가 $X$를 덮으므로 임의의 $x$는 어떤 $Q_\alpha$에 속하고, 그럼 $x\in\cl(Q_\alpha)$에서 $\psi_\alpha(x)=1$이므로 $\psi(x)\geq 1>0$이다. 따라서

$$\phi_\alpha=\frac{\psi_\alpha}{\psi}$$

로 정의하면 각 $\phi_\alpha:X\rightarrow[0,1]$은 연속함수이다 ($\psi$가 어디에서도 $0$이 아니기 때문이다). $\psi>0$이므로 $\{x\mid\phi_\alpha(x)\neq 0\}=\{x\mid\psi_\alpha(x)\neq 0\}$이고, 따라서 $\supp\phi_\alpha=\supp\psi_\alpha\subseteq U_\alpha$이며 $(\supp\phi_\alpha)$는 locally finite이다. 끝으로 각 $x$에서

$$\sum_{\alpha\in J}\phi_\alpha(x)=\frac{1}{\psi(x)}\sum_{\alpha\in J}\psi_\alpha(x)=\frac{\psi(x)}{\psi(x)}=1$$

이다. 그러므로 $(\phi_\alpha)_{\alpha\in J}$은 $(U_\alpha)$에 종속된 partition of unity이다.
:::

::: 참고 28
[정리 27](#thm27)의 역도 성립한다. 임의의 open covering $(U_i)_{i\in I}$에 대하여 이에 종속된 partition of unity $(\phi_i)_{i\in I}$이 존재하는 공간 $X$가 주어졌다 하자. 그럼 열린집합 $G_i=\{x\mid\phi_i(x)>0\}$은 $G_i\subseteq\supp\phi_i\subseteq U_i$를 만족하여 $(U_i)$의 open refinement를 이루고, $(\supp\phi_i)$가 locally finite이므로 $(G_i)$도 locally finite이며, $\sum_i\phi_i(x)=1$로부터 각 $x$에서 $\phi_i(x)>0$인 $i$가 존재하여 $(G_i)$가 $X$를 덮는다. 따라서 $X$는 paracompact이다. Hausdorff 조건을 함께 놓으면 이것은 위상공간이 paracompact Hausdorff인 것과 임의의 open covering이 종속 partition of unity를 허락하는 것이 동치라는 사실을 이룬다.
:::

## 국소 구성의 대역화

Partition of unity가 마련되면 국소적으로 정의된 자료를 대역적 대상으로 묶는 표준적인 절차가 열린다. 이 절에서는 그 원리를 연속함수의 경우로 예시한다.

::: 예시 29
Paracompact Hausdorff space $X$의 open covering $(U_\alpha)_{\alpha\in J}$이 주어지고, 각 $U_\alpha$ 위에서만 정의된 연속함수 $f_\alpha:U_\alpha\rightarrow\mathbb{R}$이 주어졌다 하자. [정리 27](#thm27)에 의하여 $(U_\alpha)$에 종속된 partition of unity $(\phi_\alpha)_{\alpha\in J}$을 택한다. 각 $\alpha$에 대하여 곱 $\phi_\alpha f_\alpha$은 $U_\alpha$ 위에서 연속이며, $\supp\phi_\alpha\subseteq U_\alpha$이 $X$의 닫힌집합이므로 이 곱을 $U_\alpha$ 바깥에서 $0$으로 두어 $X$ 전체에서 연속인 함수로 연장할 수 있다. 이 연장을 다시 $\phi_\alpha f_\alpha$로 적으면, family $(\supp\phi_\alpha)$가 locally finite이므로

$$f=\sum_{\alpha\in J}\phi_\alpha f_\alpha$$

은 각 점의 근방에서 유한합으로 환원되어 $X$ 전체에서 정의된 연속함수를 이룬다. 여기에서 $f$는 국소적 자료 $(f_\alpha)$를 partition of unity의 무게로 평균 낸 대역적 함수이다. 반대로 $X$ 위의 임의의 연속함수 $g$가 주어지면 $g=\sum_\alpha\phi_\alpha g$이 성립하여, $g$가 $U_\alpha$ 위의 조각 $\phi_\alpha g$들로 분해된다.
:::

이 구성이 가장 본질적으로 쓰이는 무대가 topological manifold이다. 우리는 이 절에서 topological manifold를 정의하고, 그것이 언제나 앞 절의 partition of unity를 허락하는 공간임을 확인한다. Topological manifold의 model은 우리가 잘 아는 Euclidean space $\mathbb{R}^m$이며, topological manifold란 국소적으로 이 model을 닮은 공간이다.

## 위상다양체

::: 정의 30
위상공간 $M$이 *locally Euclidean of dimension $m$<sub>$m$차원 국소 유클리드</sub>*이라는 것은 임의의 $x\in M$마다 $x$의 열린근방 $U$가 존재하여 $U$가 $\mathbb{R}^m$의 열린집합과 homeomorphic한 것이다.
:::

Locally Euclidean 조건은 topological manifold의 국소적 본질이지만 그것만으로는 지나치게 약하여, 여기에 두 가지 대역적 조건을 더한다.

::: 정의 31
Second countable이고 Hausdorff이며 locally Euclidean of dimension $m$인 공간을 *topological manifold of dimension $m$<sub>$m$차원 위상다양체</sub>*이라 부른다.
:::

Hausdorff와 second countability를 요구하는 까닭은 다음 정리에서 드러난다. 이 정리는 locally Euclidean 공간에서 second countability가 사실상 paracompactness와 같은 조건임을 말해 주며, 이로써 topological manifold가 앞 절에서 마련한 partition of unity의 무대에 정확히 놓임을 확인해 준다.

::: 정리 32
Hausdorff이고 locally Euclidean인 위상공간 $M$에 대하여, $M$이 second countable인 것은 $M$이 paracompact이고 가산 개의 connected component를 갖는 것과 동치이다. ([§연결공간, ⁋정의 7](/ko/math/topology/connected_spaces#def7))
:::
::: 증명
핵심 착상만 밝히고 세부는 **[Lee]**를 따른다. Locally Euclidean 조건에서 각 점은 $\mathbb{R}^m$의 열린집합과 위상동형인 근방을 가지므로 그 공간은 각 점에서 locally compact space처럼 행동한다. Second countable이면 [예시 20](#ex20)의 소진 논증을 일반화하여 $M$을 closure가 compact인 가산 개의 열린집합으로 덮을 수 있고, 이로부터 [명제 19](#prop19)의 유한성 논증과 같은 방식으로 국소유한 세분을 얻어 $M$이 paracompact임과 component가 가산임을 얻는다. 거꾸로 paracompact이고 component가 가산이면 각 component가 Lindelöf가 되어 가산 기저를 가지므로 $M$은 second countable이다.
:::

이 정리의 직접적인 귀결로 임의의 topological manifold $M$은 paracompact Hausdorff space이며, 따라서 [정리 27](#thm27)에 의하여 $M$의 임의의 좌표 덮개에 종속된 partition of unity가 존재한다. 이 사실 덕분에 각 좌표조각에서 Euclidean space의 언어로 정의한 대상을 다양체 전체로 이어 붙이는 일이 가능해지며, 이것이 partition of unity가 다양체론과 다발 이론에서 필수적인 도구로 쓰이는 이유이다.

---

**참고문헌**

**[Mun]** J. R. Munkres, *Topology*, 2nd ed., Prentice Hall, 2000.

**[Wil]** S. Willard, *General Topology*, Addison-Wesley, 1970.

**[Lee]** J. M. Lee, *Introduction to Topological Manifolds*, 2nd ed., Springer, 2011.
