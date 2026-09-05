---
title: "차원"
description: "열린집합 covering의 차수를 이용해 위상공간의 차원을 정의하고, compact space의 covering dimension 및 유한차원 위상공간의 성질을 다룬다."
excerpt: "Covering dimension과 대수기하용 Krull dimension의 정의"

categories: [Math / Topology]
permalink: /ko/math/topology/dimension
drift_needed: true
sidebar: 
    nav: "topology-ko"

date: 2024-12-15
weight: 20

---

이번 글에서 우리는 위상공간의 차원을 정의한다. 우선 우리는 일반적으로 사용하는 차원을 정의한 후, [대수다양체](/ko/algebraic_varieties/)에서 사용할 차원의 개념을 따로 정의한다. 

## Covering dimension

편의상 **[Mun]**을 따라 이 절에서는 compact space의 차원만 정의한다. 기본적인 아이디어는 $X$의 점이 열린집합들로 몇 번 덮이는지를 재는 것인데, 물론 $X$는 하나의 열린집합 $X$로만 덮이므로, 이를 임의의 open covering을 이용해서 정의해야 할 것이며, open covering을 아무렇게나 주면 점 하나를 원하는만큼 많은 열린집합들로 덮을 수 있으므로 어떠한 종류의 최소성을 담보해야 할 것이다. 

우선 다음을 정의한다.

::: 정의 1
$X$의 부분집합들의 family $(U_i)_{i\in I}$가 $m+1$의 *order*를 갖는다는 것은 $X$의 어떠한 점도 $m+1$개보다 많은 $U_i$에 속하지 않으며, $X$의 어떠한 점 하나는 정확히 $m+1$개의 $U_i$들에 속하는 것이다.
:::

그럼 공간 $X$의 차원을 다음과 같이 정의할 수 있다. 

::: 정의 2
공간 $X$가 *유한차원<sub>finite dimensional</sub>*이라는 것은 적당한 $m$이 존재하여, 임의의 open covering $(U_i)_{i\in I}$가 주어질 때마다, order $m+1$ 이하짜리 $(U_i)$의 open refinement $(V_j)_{j\in J}$가 항상 존재하는 것이다. 이것이 가능하도록 하는 최소의 $m$을 $X$의 *차원<sub>dimension</sub>*으로 정의하고 $\dim X$로 적는다. 
:::

다소 주의할만한 것은 위상공간은 다음 그림과 같이 상당히 웃기게 생길 수 있으며, 이 때 우리는 이 위상공간의 차원을 두 성분의 차원 중 큰 것이 되도록 정의했다는 것이다.

img

한편 우리가 차원에 기대함직한 성질이 몇 가지 있는데, 그들 중 일부는 다음과 같다. 

::: 명제 3
$X$가 유한차원 위상공간이고 $Y$가 $X$의 closed subspace라면, $Y$도 유한차원이고 $\dim Y\leq\dim X$이다.
:::
::: 증명
$X$가 $d$차원 위상공간이라 하고, $Y$의 임의의 open covering $\{V_j\}$이 주어졌다 하자. 그럼 각각의 $V_j$마다 $V_j=U_j\cap Y$이도록 하는 $X$의 open subset $U_j$가 존재한다. 이제 $X$는 $U_j$들과, $X\setminus Y$로 덮을 수 있다. 그럼 이 covering의 order$\leq d+1$짜리 refinement가 존재하며, 이를 다시 $Y$와 교집합하면 $\{V_j\}$의 order$\leq d+1$짜리 refinement를 얻는다. 
:::

다음 명제는 [정의 2](#def2) 이후에 언급한 주의점을 더 수학적으로 다듬은 것이다.

::: 명제 4
만일 compact space $X$의 두 유한차원 closed subspace $Y,Z$가 존재하여 $X=Y\cup Z$라면, $\dim X=\max(\dim Y,\dim Z)$이다. 
:::
::: 증명
$Y,Z$가 closed subspace이므로 [명제 3](#prop3)에 의해 $\max(\dim Y,\dim Z)\leq \dim X$이다. 따라서 $m=\max(\dim Y,\dim Z)$라 할 때 $\dim X\leq m$임을 보이면 충분하다.

우선 다음을 관찰하자. 위상공간 $T$가 $\dim T\leq m$을 만족하고 $T$의 유한한 open covering $(V_1,\ldots,V_k)$이 주어졌다면, 각각의 $i$마다 $W_i\subseteq V_i$이고 order가 $m+1$ 이하인 open covering $(W_1,\ldots,W_k)$이 존재한다. 여기서 일부 $W_i$는 공집합일 수 있다. 실제로 차원의 정의에 의해 $(V_i)$의 order $\leq m+1$짜리 open refinement $(O_j)_{j\in J}$가 존재하고, 각각의 $j$마다 $O_j\subseteq V_{i(j)}$이도록 하는 index $i(j)$를 하나씩 택한 후

$$W_i=\bigcup_{i(j)=i}O_j$$

로 정의하면 된다. $(W_i)$가 $(V_i)$의 shrinking인 open covering임은 자명하고, 만일 점 $x$가 서로 다른 $W_{i_1},\ldots,W_{i_r}$들에 속한다면 $x$는 $i(j_1)=i_1,\ldots,i(j_r)=i_r$이도록 하는 서로 다른 $O_{j_1},\ldots,O_{j_r}$들에 속해야 하므로 $r\leq m+1$이다.

이제 $X$의 임의의 open covering이 주어졌다 하자. $X$가 compact이므로 유한한 subcovering $(U_1,\ldots,U_k)$을 택할 수 있고, 이것의 order $\leq m+1$짜리 open refinement를 찾으면 충분하다.

첫 번째 단계로 $Y$를 처리하자. $(U_i\cap Y)$는 $Y$의 유한한 open covering이고 $\dim Y\leq m$이므로, 위의 관찰에 의하여 $B_i\subseteq U_i\cap Y$이고 order $\leq m+1$이며 $Y$를 덮는, $Y$에서 열린 집합들 $(B_i)$가 존재한다. 각각의 $i$마다 $\tilde{B}_i\cap Y=B_i$이도록 하는 $X$의 열린집합 $\tilde{B}_i$를 택하고, 필요하다면 $U_i$와 교집합하여 $\tilde{B}_i\subseteq U_i$라 가정하자. 이제

$$W_i=\tilde{B}_i\cup (U_i\setminus Y)$$

로 정의하면, $Y$가 닫힌집합이므로 $W_i$들은 열린집합이고 $W_i\subseteq U_i$이다. $Y$의 점들은 어떤 $B_i$에 속하고 $Y$ 바깥의 점들은 어떤 $U_i\setminus Y$에 속하므로 $(W_i)$는 $X$의 open covering이다. 마지막으로 $y\in Y$에 대하여 $W_i\cap Y=\tilde{B}_i\cap Y=B_i$이므로, $y$가 속하는 $W_i$들의 개수는 $y$가 속하는 $B_i$들의 개수와 같아 $m+1$ 이하이다.

두 번째 단계로 같은 구성을 $Z$와 covering $(W_i)$에 적용하자. 즉 $(W_i\cap Z)$에 위의 관찰을 적용하여 $C_i\subseteq W_i\cap Z$이고 order $\leq m+1$이며 $Z$를 덮는, $Z$에서 열린 집합들 $(C_i)$를 얻고, $\tilde{C}_i\subseteq W_i$, $\tilde{C}_i\cap Z=C_i$이도록 하는 $X$의 열린집합들 $\tilde{C}_i$를 택한 후

$$V_i=\tilde{C}_i\cup(W_i\setminus Z)$$

로 정의한다. 그럼 첫 번째 단계에서와 마찬가지로 $(V_i)$는 $X$의 open covering이고 $V_i\subseteq W_i\subseteq U_i$이며, $Z$의 점들은 많아야 $m+1$개의 $V_i$들에 속한다. 한편 $Y$의 점 $y$에 대해서는 $y\in V_i$일 때마다 $y\in W_i$이므로, $y$가 속하는 $V_i$들의 개수는 첫 번째 단계에서 통제한 $W_i$들의 개수 이하, 즉 $m+1$ 이하이다. $X=Y\cup Z$이므로 $(V_i)$는 주어진 covering의 order $\leq m+1$짜리 open refinement이고, 따라서 $\dim X\leq m$이다.
:::

그리고 물론 우리는 $\mathbb{R}^n$의 차원이 $n$차원이기를 바란다. 그러나 이를 보이는 것은 쉽지는 않은데, 이는 기본적으로 현재 우리가 $\mathbb{R}^n$과 $\mathbb{R}^m$이 homeomorphic하지 않다는 것조차 보이기가 힘들기 때문이다. 그 대신 이보다 약한 다음의 명제는 정의로부터 쉽게 보일 수 있다.

::: 명제 5
$\mathbb{R}^n$의 임의의 compact subspace는 항상 $n$차원 이하이다.
:::
::: 증명
$A\subseteq\mathbb{R}^n$이 compact subspace라 하고, $A$의 임의의 open covering이 주어졌다 하자. Compact함에 의해 유한한 subcovering $(U_1,\ldots,U_k)$을 택할 수 있다.

우선 적당한 $\delta>0$이 존재하여, diameter가 $\delta$ 미만인 $A$의 임의의 부분집합이 어떤 $U_i$에 포함된다는 것을 보이자. 각각의 $x\in A$마다 $x\in U_{i(x)}$이도록 하는 index $i(x)$를 택하고, $A$ 안에서의 열린 공이 $B(x,2r_x)\subseteq U_{i(x)}$를 만족하도록 하는 $r_x>0$을 택하자. 그럼 $(B(x,r_x))_{x\in A}$는 $A$의 open covering이므로 유한 개의 $B(x_1,r_{x_1}),\ldots,B(x_l,r_{x_l})$이 $A$를 덮고, $\delta=\min(r_{x_1},\ldots,r_{x_l})$로 두면 된다. 실제로 diameter $<\delta$인 집합 $S$의 한 점 $y$가 $B(x_j,r_{x_j})$에 속한다면, 삼각부등식에 의해 $S\subseteq B(x_j,2r_{x_j})\subseteq U_{i(x_j)}$이기 때문이다.

이제 $\mathbb{R}^n$ 전체의 open covering으로서, order가 $n+1$ 이하이고 모든 원소의 diameter가 일정한 상수 이하인 것을 만든다. 정수점들을 꼭짓점으로 하는 단위격자를 생각하자. 여기서 *face*란 각각의 성분이 단위구간 $[k_i,k_i+1]$ 혹은 한 점 $\{k_i\}$ ($k_i\in\mathbb{Z}$)인 곱집합을 뜻하고, face의 차원은 성분 중 구간이 사용된 개수이다. $d$차원 face들의 모임을 $\mathcal{F}_d$라 하고, $d$차원 이하의 face들의 합집합을 $\sk_d$라 하자. 그럼 $\sk_n=\mathbb{R}^n$이다. 각각의 $d=0,1,\ldots,n$에 대하여 $r_d=8^{-(d+1)}$로 두고, 각각의 $F\in\mathcal{F}_d$마다

$$U_F=\left\{x\in\mathbb{R}^n\;\middle\vert\; \operatorname{dist}(x,F)<2r_d,\quad \operatorname{dist}(x,\sk_{d-1})>r_{d-1}\right\}$$

으로 정의하자. $d=0$일 때는 둘째 조건을 생략한다. 거리함수들이 연속이므로 $U_F$들은 열린집합이다.

이들이 $\mathbb{R}^n$을 덮는 것을 보이자. 임의의 $x$에 대하여 $\operatorname{dist}(x,\sk_d)\leq r_d$를 만족하는 가장 작은 $d$를 택하자. $\operatorname{dist}(x,\sk_n)=0\leq r_n$이므로 이러한 $d$가 존재한다. 그럼 $d$의 최소성에 의하여 $d>0$인 경우 $\operatorname{dist}(x,\sk_{d-1})>r_{d-1}$이고, $\operatorname{dist}(x,\sk_d)\leq r_d<2r_d$이므로 $\operatorname{dist}(x,F)<2r_d$이도록 하는 $F\in\mathcal{F}_d$가 존재한다. 즉 $x\in U_F$이다.

다음으로 같은 차원의 서로 다른 두 face $F\neq F'\in\mathcal{F}_d$에 대하여 $U_F\cap U_{F'}=\emptyset$임을 보이자. $x\in U_F\cap U_{F'}$가 존재한다면 $\lvert x-y\rvert<2r_d$, $\lvert x-y'\rvert<2r_d$이도록 하는 $y\in F$, $y'\in F'$이 존재하고, 특히 $\lvert y-y'\rvert<4r_d\leq 1/2$이다. 우선 $F\cap F'\neq\emptyset$인데, 그렇지 않다면 어느 한 성분에서 두 face의 구간들이 서로소이고, 정수 끝점을 갖는 서로소인 구간들 사이의 거리는 $1$ 이상이므로 $\lvert y-y'\rvert\geq 1$이 되어 모순이기 때문이다. 특히 $d=0$인 경우는 이미 모순이 얻어졌으므로, $d>0$이라 하자. $F\cap F'$는 성분별 교집합으로 주어지는 face이고, 만일 그 차원이 $d$라면 구간이 사용된 $d$개의 성분에서 두 face의 단위구간이 일치하고 나머지 성분에서도 두 점이 일치하여 $F=F'$이 되므로, $F\cap F'$의 차원은 $d-1$ 이하이다. 즉 $F\cap F'\subseteq\sk_{d-1}$이다.

이제 각 성분에서 $y_i$에 가장 가까운 $F_i'$의 점을 $z_i$라 하자. $y_i\in F_i'$라면 $z_i=y_i\in F_i\cap F_i'$이고, 그렇지 않다면 $z_i$는 $F_i'$의 끝점인데 $F_i\cap F_i'$의 임의의 점이 $y_i$와 $z_i$를 기준으로 $z_i$ 너머에 있으므로 구간 $F_i$가 $y_i$와 그 점을 모두 포함한다는 것으로부터 $z_i\in F_i\cap F_i'$이다. 또 $y_i'\in F_i'$이므로 $\lvert z_i-y_i\rvert=\operatorname{dist}(y_i,F_i')\leq\lvert y_i-y_i'\rvert$이다. 따라서 $z=(z_i)\in F\cap F'\subseteq \sk_{d-1}$이고 $\lvert y-z\rvert\leq\lvert y-y'\rvert$이므로

$$\operatorname{dist}(x,\sk_{d-1})\leq \lvert x-y\rvert+\lvert y-z\rvert\leq \lvert x-y\rvert+\lvert y-y'\rvert<2r_d+4r_d=6r_d<8r_d=r_{d-1}$$

이 되어 $x\in U_F$의 둘째 조건에 모순이다.

따라서 각각의 점은 차원 $d$마다 많아야 하나의 $U_F$ ($F\in\mathcal{F}_d$)에 속하고, 차원은 $0$부터 $n$까지이므로 $(U_F)$의 order는 $n+1$ 이하이다. 또 각각의 $U_F$는 $F$로부터 거리 $2r_d$ 미만의 점들로 이루어져 있으므로 그 diameter는 $\operatorname{diam}F+4r_d\leq\sqrt{n}+1/2$ 이하이다.

마지막으로 scaling을 적용하자. $\lambda=\delta/(\sqrt{n}+1)$로 두고 위에서 만든 covering을 homeomorphism $x\mapsto\lambda x$로 옮기면, order $\leq n+1$이고 모든 원소의 diameter가 $\lambda(\sqrt{n}+1/2)<\delta$인 $\mathbb{R}^n$의 open covering $\mathcal{W}$를 얻는다. 그럼 $(W\cap A)_{W\in\mathcal{W}}$는 $A$의 open covering이고 그 order는 여전히 $n+1$ 이하이며, 각각의 원소가 diameter $<\delta$를 가지므로 첫 단계에서 찾은 Lebesgue number의 성질에 의해 어떤 $U_i$에 포함된다. 즉 이는 주어진 covering의 order $\leq n+1$짜리 open refinement이고, 따라서 $\dim A\leq n$이다.
:::

## Krull dimension

한편 우리는 algebraic geometry에서 사용하는 차원의 개념을 정의할 것인데, algebraic geometry에서 관심을 갖는 공간은 일반적으로 생각하는 위상구조와는 다른 위상구조가 주어져 있어서 이 정의는 다소 비직관적이다. 특히, 일상적인 위상구조가 주어진 $\mathbb{R}^n$은 항상 $0$차원이다. 그러나 어쨌든 이 정의를 위상수학의 언어로 할 수 있는 것은 사실이므로 이 페이지에 같이 적어두기로 한다.

::: 정의 6
위상공간 $X$가 *irreducible<sub>기약</sub>*이라는 것은 $X$가 공집합이 아니고, $X=A\cup B$이도록 하는 $X$의 진부분 닫힌집합 $A,B$가 존재하지 않는 것이다. 
:::

그럼 다음이 모두 동치이다.

::: 명제 7
공집합이 아닌 위상공간 $X$에 대하여 다음이 모두 동치이다.

1. $X$가 irreducible이다.
2. 공집합이 아닌 $X$의 임의의 열린집합 $U,V$에 대하여, $U\cap V\neq\emptyset$이다.
3. 공집합이 아닌 $X$의 임의의 열린집합 $U$에 대하여, $\cl U=X$이다.
4. $X$의 임의의 열린집합이 connected이다.
:::
::: 증명
첫째 조건과 둘째 조건은 여집합을 생각하면 동치인 것이 자명하며, 둘째 조건과 셋째 조건이 동치인 것은 $X\setminus \cl U$와 $U$를 생각하면 자명하다. 마지막으로 둘째 조건과 넷째 조건이 정의에 의해 동치이다. 
:::

특히 irreducible space는 Hausdorff가 아니다. 위의 명제의 마지막 동치 때문에 irreducible space는 *hyperconnected space*라 부르기도 한다. 비슷한 맥락에서 다음이 성립한다. (참고: [§연결공간, ⁋명제 3](/ko/math/topology/connected_spaces#prop3))

::: 명제 8
만일 공집합이 아닌 $X$가 irreducible open subset들의 합집합

$$X=\bigcup_{i\in I} U_i$$

이고 $U_i\cap U_j\neq \emptyset$이 모든 $i,j$에 대해 성립한다 하자. 그럼 $X$는 irreducible이다.
:::
::: 증명
임의의 두 열린집합 $V, W$가 주어졌다 하고, $V\cap W\neq\emptyset$임을 보이자. 그럼 주어진 가정으로부터 우선 $U_i\cap V\neq\emptyset$ 그리고 $U_j\cap W\neq\emptyset$을 만족하는 $i,j$가 존재한다. 이제 $U_i$가 irreducible이므로, $U_i$의 두 nonempty subset $U_i\cap V$와 $U_i\cap U_j$도 반드시 공집합이 아닌 교집합을 가져야 한다. 즉

$$(U_i\cap V)\cap (U_i\cap U_j)=U_i\cap U_j\cap V\neq\emptyset$$

이고, $U_i\cap U_j\cap V$를 $U_j$의 nonempty subset으로 보면 마찬가지로 $U_j$의 irreducibility로부터 다음의 식

$$(U_i\cap U_j\cap V)\cap (U_j\cap W)=U_i\cap U_j\cap V\cap W\neq\emptyset$$

을 얻고 특히 $V\cap W\neq\emptyset$이다. 
:::

Connected component와 비슷하게 다음을 정의할 수 있다.

::: 정의 9
위상공간 $X$의 부분집합 $A$에 대하여, $A$를 포함하는 *irreducible component<sub>기약성분</sub>*는 $A$를 포함하는 irreducible subset들 가운데 포함관계에 대하여 maximal인 것을 의미한다. 
:::

$A$를 포함하는 irreducible subset들의 공집합이 아닌 totally ordered subset이 주어졌다면 그 합집합 $Y$도 irreducible인데, $Y$의 공집합이 아닌 두 열린집합이 각각 그 모임의 원소 $Y_1, Y_2$와 만난다 하고 $Y_1\subseteq Y_2$라 하면, 두 열린집합과 $Y_2$의 교집합이 $Y_2$의 공집합이 아닌 열린집합이므로 [명제 7](#prop7)의 둘째 조건에 의하여 서로 만나기 때문이다. 따라서 $A$가 irreducible이라면 공집합인 totally ordered subset은 $A$ 자신을 upper bound로 가지므로, [\[집합론\] §선택공리, ⁋정리 4](/ko/math/set_theory/axiom_of_choice#thm4)에 의하여 $A$를 포함하는 irreducible component가 존재한다. 다만 connected component와 달리 maximal인 것이 유일할 이유가 없으므로, $A$를 포함하는 irreducible component는 여럿일 수 있다. 한편 [§연결공간, ⁋명제 2](/ko/math/topology/connected_spaces#prop2)과 비슷한 논증에 의하여, irreducible set의 closure는 irreducible인 것을 보일 수 있으므로 irreducible component는 반드시 closed subset이다. 

::: 정의 10
위상공간 $X$에 대하여, $X$의 irreducible closed subset들의 strictly descending chain

$$A_n\supsetneq\cdots\supsetneq A_0$$

의 *length<sub>길이</sub>*를 $n$으로 정의한다. 그럼 $X$의 *Krull dimension<sub>크룰 차원</sub>*을 다음의 식

$$\dim X=\sup\{\text{length of strictly descending chains of irreducible closed subsets}\}$$

으로 정의한다. 만일 무한한 길이의 strictly descending chain이 존재한다면 $\dim X=\infty$로 정의하고, $X=\emptyset$인 경우 $\dim X=-\infty$로 정의한다. 
:::

Hausdorff space에서는 오직 singleton만이 irreducible subset이므로, 공집합이 아닌 Hausdorff space의 Krull dimension은 항상 $0$이다. 한편 algebraic geometry에서 다루는 공간들은 다음의 유한성 조건을 만족하는 경우가 많다. 

::: 정의 11
위상공간 $X$가 *Noetherian<sub>뇌터 공간</sub>*이라는 것은 임의의 닫힌집합들의 chain

$$A_1\supseteq A_2\supseteq\cdots$$

이 주어질 때마다, 적당한 $n$이 존재하여 $A_n=A_{n+1}=\cdots$이도록 할 수 있는 것이다.
:::

이 조건이 Krull dimension의 유한성까지 주지는 않는다. 가령 $X=\mathbb{N}$에 $\emptyset$과 $X$, 그리고 유한한 initial segment $\{1,\ldots,n\}$들을 닫힌집합으로 하는 위상을 주면, 닫힌집합들의 strictly descending chain에서는 $n$이 감소해야 하므로 $X$는 Noetherian이다. 그러나 각각의 $\{1,\ldots,n\}$은 $\{n\}$의 closure이므로 irreducible이고, 따라서 $\{1\}\subsetneq\{1,2\}\subsetneq\cdots$가 임의로 긴 chain을 주어 $\dim X=\infty$이다.

또한 $X$가 Noetherian이라면, $X$의 닫힌집합들로 이루어진 공집합이 아닌 임의의 모임 $\mathcal{S}$는 포함관계에 대하여 minimal element를 갖는다. 그렇지 않다면 각각의 $A\in\mathcal{S}$마다 $A\supsetneq A'$인 $A'\in\mathcal{S}$를 택할 수 있고, 이를 반복하여 안정화하지 않는 닫힌집합들의 descending chain을 얻기 때문이다.

Noetherian 조건은 강력한 유한성의 조건을 준다. 가령 다음이 성립한다.

::: 명제 12
Noetherian space는 compact이다.
:::
::: 증명
Noetherian space $X$와 $X$의 open covering $\{U_i\}_{i\in I}$가 주어졌다 가정하자. 그럼

$$\mathcal{C}=\left\{\bigcup_{j\in J} U_j\mid\text{$J$ finite subset of $I$}\right\}$$

라 정의할 수 있다. 이제 $\mathcal{C}$의 임의의 totally ordered subset $\mathcal{D}$가 주어졌다 하자. $\mathcal{D}$가 공집합이라면 $J=\emptyset$에 대응하는 $\emptyset\in\mathcal{C}$가 $\mathcal{D}$의 upper bound이고, 그렇지 않다면 $\mathcal{D}$의 원소들의 여집합들이 $X$의 닫힌집합들로 이루어진 공집합이 아닌 모임이므로 위에서 본 것과 같이 minimal element를 가지며, $\mathcal{D}$가 totally ordered이므로 그 여집합은 $\mathcal{D}$에서 가장 큰 원소, 특히 $\mathcal{D}$의 upper bound이다. 즉 $\mathcal{C}$의 임의의 totally ordered subset이 upper bound를 가지므로, [\[집합론\] §선택공리, ⁋정리 4](/ko/math/set_theory/axiom_of_choice#thm4)에 의하여 $\mathcal{C}$는 maximal element $U\in \mathcal{C}$를 갖는다. 만일 $X\neq U$라면, $x\in X\setminus U$를 포함하는 $U_j$를 택할 수 있고 그럼 $U\cup U_j$는 $U$를 strict하게 포함하는 $\mathcal{C}$의 원소이므로 $U$의 maximality에 모순이다. 따라서 $U=X$이고 우리는 원하는 결과를 얻는다. 
:::

추가적으로 Noetherian space에 대해 다음이 성립한다.

::: 명제 13
Noetherian topological space $X$에 대하여, 다음이 성립한다.

1. $X$의 임의의 부분공간은 Noetherian이다.
2. $X$는 유한히 많은 irreducible component를 가진다. 
3. $X$의 각각의 irreducible component는 공집합이 아닌 $X$의 열린집합을 포함한다.
:::
::: 증명
1. $X$의 임의의 부분공간 $Y$가 주어졌다 하고 $Y$의 임의의 닫힌집합들의 descending chain 
    
    $$A_1\supseteq A_2\supseteq \cdots$$

    가 주어졌다 하자. 그럼 $A_i=A_i' \cap Y$를 만족하는 $X$의 닫힌집합 $A_i'$들이 존재한다. 이제 $B_i=A_1'\cap\cdots\cap A_i'$라 하면, $B_i\cap Y=A_i$이고 $B_i$는 $X$의 닫힌집합들의 descending chain이다. 
2. $\mathcal{C}$를 $X$의 닫힌집합 중, 유한히 많은 irreducible closed subset들의 합집합으로 나타낼 수 없는 집합들의 모임이라 하자. 그럼 $\mathcal{C}=\emptyset$임을 보이면 된다. 결론에 반하여 $\mathcal{C}$가 공집합이 아니라 하면, 위에서 본 minimal element의 존재로부터 $\mathcal{C}$는 minimal element $A$를 갖는다. 공집합은 공집합인 모임의 합집합이므로 $A\neq\emptyset$이고, $A$가 irreducible이라면 $A$ 자기 자신이 하나짜리 합집합이 되므로 $A$는 irreducible이 아니다. 따라서 [정의 6](#def6)에 의하여 $A=B_1\cup B_2$이도록 하는 $A$의 진부분 닫힌집합 $B_1,B_2$가 존재하고, $A$의 minimality로부터 $B_1,B_2\not\in\mathcal{C}$이므로 이들 각각은 유한히 많은 irreducible closed subset의 합집합이며, 이 둘을 합치면 $A$ 또한 그러한 합집합이 되어 모순이다. 즉 $\mathcal{C}=\emptyset$이고, 특히 $X=A_1\cup\cdots\cup A_n$이도록 하는 $X$의 irreducible closed subset들 $A_1,\ldots,A_n$이 존재한다. 어떤 $A_i$가 다른 $A_j$에 포함된다면 그것을 지워도 되므로 처음부터 $A_i$들 사이에 포함관계가 없다고 가정하면, $X$의 임의의 irreducible closed subset $B$에 대하여 $B=\bigcup_i (B\cap A_i)$는 $B$의 닫힌집합들의 유한한 합집합이므로 [정의 6](#def6)을 반복 적용하여 $B\subseteq A_i$인 $i$가 존재한다. 그럼 $X$의 irreducible component는 [정의 9](#def9)에 의하여 maximal인 irreducible subset이고 앞서 보았듯 닫힌집합이므로 어떤 $A_i$에 포함되며, $A_i$ 자신이 irreducible이므로 maximality로부터 $A_i$와 같다. 따라서 $X$의 irreducible component는 많아야 $n$개이다.
3. (2)에서 얻은 $X=A_1\cup\cdots\cup A_n$을 $A_i$들 사이에 포함관계가 없도록 택하자. 만일 $A_1\subseteq A_2\cup\cdots\cup A_n$이라면 $A_1=\bigcup_{j\geq 2}(A_1\cap A_j)$이므로 위와 같이 $A_1\subseteq A_j$인 $j\geq 2$가 존재하여 포함관계가 없다는 것에 모순이고, 따라서 $X\setminus (A_2\cup\cdots\cup A_n)$은 $A_1$에 포함되는 공집합이 아닌 $X$의 열린집합이다. 각각의 irreducible component가 어떤 $A_i$와 같으므로, 같은 논증을 모든 $i$에 적용하면 된다. 
:::

그럼 만일 $X$가 Noetherian이라면, $X$의 irreducible decomposition

$$X=\bigcup_{i=1}^r X_i$$

이 존재하며, $X_i$들은 모두 닫힌집합이다. 그러나 서로 다른 irreducible component들은 서로 만날 수 있어 $X\setminus X_i$가 $\bigcup_{j\neq i}X_j$보다 작을 수 있으므로, $X_i$가 열린집합일 이유는 없다. 실제로 $X_i$가 열린집합이면서 다른 component $X_j$와 만난다면 $X_i\cap X_j$는 $X_j$의 공집합이 아닌 열린집합이므로 [명제 7](#prop7)의 셋째 조건에 의하여 $X_j$에서 dense이고, $X_i$가 닫힌집합이므로 $X_j\subseteq X_i$가 되어 $X_j$의 maximality로부터 $X_i=X_j$이다. 즉 $X_i$가 열린집합인 것은 $X_i$가 다른 component와 만나지 않는 경우뿐이다. 

닫힌집합들의 공집합이 아닌 모임이 언제나 minimal element를 가진다는 위의 사실을 하나의 귀납 원리로 정리하면, Noetherian space 위에서 닫힌집합에 대한 성질을 증명하는 표준적인 도구를 얻는다.

::: 명제 14 (Noetherian induction)
Noetherian topological space $X$와, $X$의 닫힌집합에 대한 성질 $P$가 주어졌다 하자. 만일 임의의 닫힌집합 $Z\subseteq X$에 대하여, 모든 진부분 닫힌집합 $Z'\subsetneq Z$에서 $P(Z')$가 성립할 때마다 $P(Z)$ 또한 성립한다면, $P$는 $X$의 모든 닫힌집합에서 성립한다.
:::
::: 증명
$P$가 성립하지 않는 닫힌집합들의 모임을 $\mathcal{S}$라 하고, 결론에 반하여 $\mathcal{S}\neq\emptyset$이라 하자. 위에서 본 것과 같이 $\mathcal{S}$는 minimal element $Z_0$을 가진다. 그럼 $Z_0$이 minimal이므로 임의의 진부분 닫힌집합 $Z'\subsetneq Z_0$은 $\mathcal{S}$에 속하지 않아 $P(Z')$가 성립하고, 따라서 가정에 의하여 $P(Z_0)$이 성립한다. 이는 $Z_0\in\mathcal{S}$에 모순이므로 $\mathcal{S}=\emptyset$이며, 곧 $P$는 $X$의 모든 닫힌집합에서 성립한다.
:::

이는 자연수에 대한 강한 귀납법의 위상적 유비로, 닫힌집합들이 descending chain condition을 만족한다는 Noetherian 조건이 귀납을 가능하게 한다. 실제 사용에서는 임의의 닫힌집합 $Z$에 대해 그 진부분 닫힌집합들에서 성질이 성립한다고 가정하고 $Z$에서 성립함을 보이며, 특히 $Z=X$의 경우가 결론에 포함된다.

::: 명제 15
위상공간 $X$와 열린집합 $U$에 대하여, $U$와 만나는 $X$의 irreducible closed subset과, $U$의 irreducible closed subset 사이의 일대일대응이 존재한다.
:::
::: 증명
우선 $U\cap Z\neq\emptyset$을 만족하는 $X$의 irreducible subspace $Z$가 주어졌다 하고, $Z\cap U$의 공집합이 아닌 임의의 두 열린집합이 서로소가 아님을 보여야 한다. $Z\cap U$의 임의의 열린집합은 $Z$의 열린집합 $V_1, V_2$에 대하여 $V_1\cap U$, $V_2\cap U$의 꼴이므로, 다음의 식

$$(V_1\cap U)\cap (V_2\cap U)=(V_1\cap V_2)\cap U$$

으로부터 만일 $(V_1\cap U)\cap(V_2\cap U)\neq\emptyset$이라면 $V_1\cap V_2\neq\emptyset$이 되어 $Z$가 irreducible이라는 가정에 모순이다. 

거꾸로 $U$의 irreducible closed subset $Y\subseteq U$가 주어졌다 하면 $Y$의 closure 또한 irreducible이므로 $X$의 irreducible $\cl_X(Y)$가 $U$와 만나는 $X$의 irreducible subset이 된다. 즉 이로부터 두 함수

$$\{\text{irreducible closed subset of $X$ meeting $U$}\}\rightarrow \{\text{irreducible closed subset of $U$}\};\qquad Z\mapsto Z\cap U$$

그리고 

$$\{\text{irreducible closed subset of $U$}\} \rightarrow \{\text{irreducible closed subset of $X$ meeting $U$}\};\qquad Y\mapsto \cl_X(Y)$$

를 얻으며, 이들이 서로의 bijection임을 확인할 수 있다.
:::

뿐만 아니라, 위의 증명에서의 두 함수는 inclusion-preserving이므로, $U$와 만나는 $X$의 irreducible component와 $U$의 irreducible component 사이의 일대일대응이 존재한다.

이제 다음 명제를 보이자.

::: 명제 16
만일 위상공간 $X$의 두 유한차원 closed subspace $Y,Z$가 존재하여 $X=Y\cup Z$라면, 이들의 Krull dimension 또한 식 $\dim X=\max(\dim Y,\dim Z)$을 만족한다.
:::

---

**참고문헌**

**[Bou]** N. Bourbaki, <i>General Topology</i>. Elements of mathematics. Springer, 1995.
