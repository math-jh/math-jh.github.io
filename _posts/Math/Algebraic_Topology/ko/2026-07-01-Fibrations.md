---
title: "호모토피의 계산"
description: "고차 호모토피 군을 정의하고, Hurewicz 정리와 fibration에 딸린 장거리 완전열을 통해 이를 계산하는 도구를 마련한다."
excerpt: "Higher homotopy groups, the Hurewicz theorem, and the long exact sequence of a fibration"

categories: [Math / Algebraic Topology]
permalink: /ko/math/algebraic_topology/fibrations
sidebar: 
    nav: "algebraic_topology-ko"

date: 2026-07-01
last_modified_at: 2026-07-01
weight: 5.3

published: false

---

## 고차 호모토피 군

앞선 글에서 우리는 fundamental group $\pi_1(X,x_0)$을 정의하고, 이것이 base point $x_0$을 시작점과 끝점으로 갖는 loop들의 homotopy type들이 이루는 group임을 보았다. ([§호모토피, ⁋정의 11](/ko/math/algebraic_topology/homotopy#def11)) Loop란 본질적으로 $1$차원 구 $S^1$에서 $X$로의 함수이므로, 이를 자연스럽게 고차원으로 일반화하여 $n$차원 구에서 $X$로의 함수들을 생각할 수 있다. 이렇게 얻어지는 불변량이 fundamental group보다 훨씬 섬세한 정보를 담고 있으리라 기대하는 것은 자연스럽다. 다만 이들 고차 불변량은 아직 정의된 바 없으므로, 우리는 우선 이를 엄밀하게 도입한다.

편의를 위해 $n$-cube $I^n=[0,1]^n$과 그 boundary $\partial I^n$을 생각하자. $\partial I^n$은 적어도 하나의 좌표가 $0$ 또는 $1$인 점들의 집합이다. 그럼 $\partial I^n$을 한 점으로 붕괴시킨 quotient space $I^n/\partial I^n$은 $n$차원 구 $S^n$과 homeomorphic하며, 따라서 $\partial I^n$ 전체를 base point $x_0$으로 보내는 연속함수 $(I^n,\partial I^n)\rightarrow(X,x_0)$은 $(S^n,s_0)\rightarrow(X,x_0)$과 같은 정보를 담는다.

::: 정의 1
Base point $x_0\in X$을 고정하자. 각각의 $n\geq 1$에 대하여, $\partial I^n$을 $x_0$으로 보내는 연속함수 $f:(I^n,\partial I^n)\rightarrow(X,x_0)$들의 homotopy 관계에 대한 equivalence class들의 집합을 $X$의 *$n$-th homotopy group<sub>$n$번째 호모토피 군</sub>* $\pi_n(X,x_0)$이라 부른다. 여기에서 homotopy는 $\partial I^n$을 항상 $x_0$으로 유지하는 것들만 생각한다.
:::

집합 $\pi_n(X,x_0)$에는 group 구조가 주어진다. 두 함수 $f,g:(I^n,\partial I^n)\rightarrow(X,x_0)$에 대하여, 첫째 좌표를 이등분하여 곱을 다음의 식

$$(f\ast g)(t_1,\ldots,t_n)=\begin{cases}f(2t_1,t_2,\ldots,t_n)&0\leq t_1\leq 1/2\\ g(2t_1-1,t_2,\ldots,t_n)&1/2\leq t_1\leq 1\end{cases}$$

으로 정의하면, $\partial I^n$ 위에서 두 함수가 모두 $x_0$의 값을 가지므로 이 곱이 잘 정의된 연속함수가 된다. 이 연산이 homotopy 관계에서 well-defined이고 결합법칙과 역원을 가짐은 $n=1$인 경우, 곧 [§호모토피, ⁋정의 11](/ko/math/algebraic_topology/homotopy#def11)의 fundamental group에서와 같은 방식으로 확인된다. 뿐만 아니라 $n\geq 2$인 경우 곱을 정의하는 데 쓸 수 있는 좌표가 둘 이상이므로, 이른바 Eckmann-Hilton 논법에 의하여 $\pi_n(X,x_0)$은 abelian group이 된다. 즉 fundamental group과 달리 고차 homotopy group은 항상 commutative하다.

이렇게 정의된 $\pi_n$은 fundamental group과 마찬가지로 base point를 갖는 공간들과 그 사이의 연속함수들에 대한 functor이며, path-connected space에서는 $x_0$의 선택에 의존하지 않는다. 이후 우리는 base point가 문맥에서 분명할 때 이를 생략하고 $\pi_n(X)$로 적기도 한다.

그런데 이러한 고차 homotopy group은 fundamental group과 달리 Seifert-van Kampen 정리와 같은 계산 도구를 갖지 않으며, 정의로부터 직접 계산하는 것은 거의 불가능하다. 실제로 구 $S^n$의 고차 homotopy group들조차 완전히 알려져 있지 않다. 이 글의 목표는 이러한 계산을 가능하게 하는 가장 근본적인 도구, 곧 fibration에 딸린 장거리 exact sequence를 마련하는 것이다.

## Hurewicz theorem

Homology group은 fundamental group보다 더 단순한 구조를 가지고 있다. 가령 $\pi_1(X)$는 일반적으로 abelian group일 필요가 없지만, $H_1(X)$는 그 정의에 의해 abelian group이다. 그러나 [§호몰로지, ⁋예시 8](/ko/math/algebraic_topology/homology#ex8)에서 살펴본 것처럼 $H_1(X)$의 원소들도 일단은 일종의 loop들처럼 생각할 수 있으므로 이들 사이의 관계를 기대하는 것이 자연스럽다.

::: 정리 2 (Hurewicz)
Path-connected space $X$를 고정하자. 그럼 각각의 $n$에 대하여, group homomorphism

$$h_n:\pi_n(X) \rightarrow H_n(X)$$

이 존재한다. 특별히 $n=1$인 경우, $h_1$은 surjective이고 $\ker h_1$은 $\pi_1(X)$의 commutator subgroup $[\pi_1(X),\pi_1(X)]$이 되어 first isomorphism theorem에 의해

$$H_1(X)\cong \pi_1(X)/\ker h_1=\pi_1(X)/[\pi_1(X),\pi_1(X)]=\pi_1(X)^\ab$$

이 성립한다. 더 일반적으로, 만일 모든 $i< n$에 대하여 $\pi_i(X)=0$이라면 $h_n$은 isomorphism이고 $h_{n+1}$은 surjective이다.
:::

Hurewicz homomorphism $h_n$은 임의의 $f:S^n \rightarrow X$가 주어졌을 때 $f_\ast([S^n])$으로 주어진다. 여기에서 $[S^n]$은 $H_n(S^n)\cong\mathbb{Z}$의 generator이다.

## 호모토피 올림 성질과 fibration

Covering space에 대한 우리의 논의에서 가장 핵심적인 성질은 path와 그 homotopy를 위로 들어올릴 수 있다는 것이었다. ([§피복공간, ⁋보조정리 6](/ko/math/algebraic_topology/covering_spaces#lem6), [§피복공간, ⁋보조정리 7](/ko/math/algebraic_topology/covering_spaces#lem7)) 이 lifting property를 임의의 공간에 대한 homotopy로 일반화한 것이 fibration의 정의이며, 피복사상은 그 특수한 경우에 해당한다.

::: 정의 3
연속함수 $p:E\rightarrow B$가 공간 $X$에 대하여 *homotopy lifting property<sub>호모토피 올림 성질</sub>* (줄여서 HLP) 를 갖는다는 것은, 다음의 조건이 성립하는 것이다. 임의의 homotopy $g:X\times I\rightarrow B$와, $g_0=g\vert_{X\times\{0\}}$의 lifting $\widetilde{g}_0:X\rightarrow E$ (즉 $p\circ\widetilde{g}_0=g_0$) 가 주어질 때마다, $g$ 전체의 lifting $\widetilde{G}:X\times I\rightarrow E$가 존재하여 $p\circ\widetilde{G}=g$이고 $\widetilde{G}\vert_{X\times\{0\}}=\widetilde{g}_0$이도록 할 수 있다.
:::

정의의 조건은 다음의 diagram에서 아래 삼각형을 채우는 점선 화살표 $\widetilde{G}$의 존재로 요약된다. 위쪽 삼각형은 초기 조건 $\widetilde{G}\vert_{X\times\{0\}}=\widetilde{g}_0$을, 아래쪽 삼각형은 lifting 조건 $p\circ\widetilde{G}=g$을 나타낸다.

![lifting_square](/assets/images/Math/Algebraic_Topology/Fibrations-1.svg){:style="width:8.72em" class="invert" .align-center}

이 성질을 어떤 공간들에 대하여 요구하느냐에 따라 서로 다른 fibration의 개념이 얻어진다.

::: 정의 4
연속함수 $p:E\rightarrow B$에 대하여 다음과 같이 정의한다.

1. $p$가 *Hurewicz fibration<sub>후레비치 올뭉치</sub>*이라는 것은 $p$가 모든 위상공간 $X$에 대하여 HLP를 갖는 것이다.
2. $p$가 *Serre fibration<sub>세르 올뭉치</sub>*이라는 것은 $p$가 모든 $n\geq 0$에 대한 cube $I^n$에 대하여 HLP를 갖는 것이다.

이 때 $E$를 *total space<sub>전공간</sub>*, $B$를 *base space<sub>밑공간</sub>*라 부르며, base point $b_0\in B$을 고정했을 때 그 preimage $F=p^{-1}(b_0)$을 $b_0$ 위의 *fiber<sub>올</sub>*라 부른다. 문맥에 따라 $p$ 자체 또는 자료 $F\rightarrow E\rightarrow B$를 *fibration<sub>올림</sub>*이라 부른다.
:::

Hurewicz fibration은 정의상 임의의 공간 $X$에 대하여 HLP를 가지므로, 특히 $X=I^n$인 경우에도 HLP를 만족하여 Serre fibration의 조건을 자동으로 충족한다. 그 역은 성립하지 않지만, 뒤에서 구성할 장거리 exact sequence는 Serre fibration에 대해서도 성립하므로 우리의 목적에는 더 약한 Serre fibration의 개념으로 충분하다. 한편 CW complex는 cube들을 붙여 얻어지는 공간이므로, Serre fibration의 조건은 모든 CW complex에 대한 HLP와 동치임이 알려져 있다.

::: 참고 5
Fibration의 가장 풍부한 공급원은 locally trivial fiber bundle, 곧 밑공간이 열린집합들로 덮여 각 열린집합 $U$ 위에서 $p^{-1}(U)$가 $U\times F$와 자연스럽게 homeomorphic한 경우이다. 이러한 fiber bundle은 항상 Serre fibration이며, 밑공간이 paracompact이면 Hurewicz fibration이기도 하다. 이는 [Hat]의 §4.2에 상세히 다루어져 있다.
:::

이제 피복사상이 fibration의 특수한 경우임을 확인한다.

::: 명제 6
임의의 covering map $p:E\rightarrow B$ ([§피복공간, ⁋정의 3](/ko/math/algebraic_topology/covering_spaces#def3)) 는 Hurewicz fibration이며, 그 각각의 fiber $p^{-1}(b)$는 discrete space이다.
:::
::: 증명
Fiber가 discrete라는 것은 covering map의 정의에서 즉시 따라온다. $b\in B$의 evenly covered인 열린근방 $U$에 대하여 $p^{-1}(U)$는 $U$와 homeomorphic한 disjoint open set들의 합집합이므로, $p^{-1}(b)$는 이들 각각의 slice에서 정확히 한 점씩을 가지며 따라서 $E$의 부분공간으로서 discrete이다.

HLP를 확인하자. Homotopy $g:X\times I\rightarrow B$와 초기 lifting $\widetilde{g}_0:X\rightarrow E$가 주어졌다 하자. 각각의 $x\in X$에 대하여, $t\mapsto g(x,t)$는 $g(x,0)=p(\widetilde{g}_0(x))$에서 시작하는 $B$의 path이다. [§피복공간, ⁋보조정리 6](/ko/math/algebraic_topology/covering_spaces#lem6)에 의하여 이 path는 $\widetilde{g}_0(x)$에서 시작하는 유일한 lifting을 가지므로, 이를 $t\mapsto\widetilde{G}(x,t)$로 정의하면 집합 사이의 함수로서 $\widetilde{G}:X\times I\rightarrow E$가 유일하게 결정되고 $p\circ\widetilde{G}=g$, $\widetilde{G}\vert_{X\times\{0\}}=\widetilde{g}_0$을 만족한다.

남은 것은 $\widetilde{G}$의 연속성이다. 한 점 $(x_0,t_0)$ 근방에서 이를 보이자. $g(x_0,t_0)$의 evenly covered인 열린근방 $U$를 택하고, $p^{-1}(U)$의 slice들 중 $\widetilde{G}(x_0,t_0)$을 포함하는 것을 $V$라 하자. Path lifting의 유일성에 의하여 $t$가 속하는 slice는 연속적으로 변하므로, $g$의 연속성으로부터 $(x_0,t_0)$의 적당한 근방이 $\widetilde{G}$에 의해 $V$로 보내지며, 이 근방 위에서 $\widetilde{G}=(p\vert_V)^{-1}\circ g$가 성립하여 연속이다. Cube의 콤팩트성을 이용해 이 국소적 논의를 이어 붙이면 $\widetilde{G}$ 전체의 연속성을 얻는다.
:::

즉 covering map이란 fiber가 discrete인 fibration에 다름 아니다. 우리가 이 글에서 얻을 장거리 exact sequence는 이 관점에서 covering space 이론의 정확한 일반화가 되며, discrete fiber라는 조건을 벗겨냈을 때 어떠한 exact sequence가 남는지를 알려줄 것이다.

## 상대 호모토피 군과 연결 사상

Fibration의 exact sequence를 얻기 위한 다리로서, 우리는 공간의 쌍 $(X,A)$에 대한 relative homotopy group을 도입한다. 이는 [§호몰로지의 계산, ⁋정의 1](/ko/math/algebraic_topology/computation_of_homology#def1)의 relative homology에 대응하는 homotopy 쪽의 개념이다.

$I^{n-1}=I^{n-1}\times\{0\}\subseteq I^n$을 $I^n$의 한 face로 보고, $J^{n-1}$을 $\partial I^n$에서 이 face를 뺀 나머지 face들의 합집합의 closure라 하자. 즉 $\partial I^n=I^{n-1}\cup J^{n-1}$이며 이 둘은 $\partial I^{n-1}$을 따라 만난다.

::: 정의 7
부분공간 $A\subseteq X$와 base point $x_0\in A$가 주어졌다 하자. 각각의 $n\geq 1$에 대하여, 세 쌍 사이의 연속함수

$$f:(I^n,\partial I^n,J^{n-1})\rightarrow(X,A,x_0),$$

곧 $\partial I^n$을 $A$로, $J^{n-1}$을 $x_0$으로 보내는 연속함수들의 (같은 형태의 조건을 유지하는) homotopy equivalence class들의 집합을 쌍 $(X,A)$의 *relative homotopy group<sub>상대 호모토피 군</sub>* $\pi_n(X,A,x_0)$이라 부른다.
:::

정의에서 $f$는 남은 face $I^{n-1}$을 $A$로 보내지만 반드시 $x_0$으로 보내지는 않는다. $\pi_n(X,A,x_0)$은 $n\geq 2$에 대하여 [정의 1](#def1)에서와 같은 방식의 곱으로 group이 되며, $n\geq 3$이면 abelian group이다. $n=1$인 경우에는 일반적으로 base point를 가진 집합일 뿐이다. 특별히 $A=\{x_0\}$인 경우, 조건 "$\partial I^n$을 $A=\{x_0\}$으로 보낸다"는 [정의 1](#def1)의 조건과 같아지므로

$$\pi_n(X,\{x_0\},x_0)=\pi_n(X,x_0)$$

이 성립한다. 즉 절대 homotopy group은 상대 homotopy group의 특수한 경우이다.

상대 homotopy group에는 자연스러운 *connecting homomorphism<sub>연결 준동형</sub>* 이 딸려 있다. 함수 $f:(I^n,\partial I^n,J^{n-1})\rightarrow(X,A,x_0)$을 남은 face $I^{n-1}=I^{n-1}\times\{0\}$으로 제한하면, 이 face 위에서 $f$는 $A$로 가는 값을 가지며 그 boundary $\partial I^{n-1}$에서는 $x_0$의 값을 가지므로, $f\vert_{I^{n-1}}$은 $(I^{n-1},\partial I^{n-1})\rightarrow(A,x_0)$의 원소, 곧 $\pi_{n-1}(A,x_0)$의 원소를 정의한다. 이 대응은 homotopy를 보존하므로 다음의 준동형

$$\partial:\pi_n(X,A,x_0)\rightarrow\pi_{n-1}(A,x_0)$$

을 정의하며, 우리는 이를 connecting homomorphism이라 부른다.

이제 inclusion $i:A\hookrightarrow X$가 유도하는 $i_\ast:\pi_n(A)\rightarrow\pi_n(X)$과, 절대 homotopy group을 상대 homotopy group으로 보는 자연스러운 morphism $j_\ast:\pi_n(X)\rightarrow\pi_n(X,A)$을 함께 생각하면, 이들이 relative homology의 장거리 exact sequence에 정확히 대응하는 exact sequence를 이룸을 보일 수 있다.

::: 명제 8 (쌍의 장거리 exact sequence)
Base point $x_0\in A\subseteq X$에 대하여, 다음의 수열

$$\cdots\rightarrow\pi_n(A,x_0)\overset{i_\ast}{\longrightarrow}\pi_n(X,x_0)\overset{j_\ast}{\longrightarrow}\pi_n(X,A,x_0)\overset{\partial}{\longrightarrow}\pi_{n-1}(A,x_0)\rightarrow\cdots$$

은 $\pi_1(X,A,x_0)$ 항까지 완전하다. (group 구조가 없는 낮은 항에서는 base point를 가진 집합들의 exact sequence로 이해한다.)
:::
::: 증명
핵심 관찰은 $\pi_n(X,A,x_0)$의 한 원소가 $0$이라는 것, 곧 그것이 $J^{n-1}$을 넘어 $\partial I^n$ 전체를 $x_0$으로 보내는 함수로 (쌍의 조건을 유지하며) 변형된다는 것이, 그 원소가 $A$ 안에 완전히 담긴 함수로 변형됨과 동치라는 것이다. 이를 이용해 각 마디의 완전성을 확인한다.

$\pi_n(X)$에서의 완전성, 곧 $\im i_\ast=\ker j_\ast$를 보자. $f:(I^n,\partial I^n)\rightarrow(X,x_0)$에 대하여 $j_\ast[f]=0$이라는 것은 $f$가 쌍 $(X,A)$의 원소로서 자명하다는 것, 곧 $f$가 image 전체를 $A$ 안에 갖는 함수 $f'$과 homotopic하다는 것이다. 이는 정확히 $[f]$가 $i_\ast[f']$의 꼴이라는 것이므로 $\im i_\ast=\ker j_\ast$이다.

$\pi_n(X,A)$에서의 완전성, 곧 $\im j_\ast=\ker\partial$을 보자. $f:(I^n,\partial I^n)\rightarrow(X,x_0)$에 대하여 $\partial(j_\ast[f])$는 $f\vert_{I^{n-1}}$인데, $f$가 절대 homotopy group에서 오므로 이 restriction은 상수함수 $x_0$이고 따라서 $0$이다. 역으로 $\partial[f]=0$인 $f:(I^n,\partial I^n,J^{n-1})\rightarrow(X,A,x_0)$가 주어지면, $f\vert_{I^{n-1}}$이 $A$ 안에서 $x_0$으로 향하는 null-homotopy를 가지므로, 이를 이용해 $f$를 $\partial I^n$ 전체를 $x_0$으로 보내는 함수로 변형할 수 있고 이는 $j_\ast$의 image에 속한다.

$\pi_{n-1}(A)$에서의 완전성, 곧 $\im\partial=\ker i_\ast$을 보자. $[f]\in\pi_n(X,A)$에 대하여 $i_\ast(\partial[f])$는 $f\vert_{I^{n-1}}$을 $X$ 안의 함수로 본 것인데, $f$ 자체가 이 restriction을 $X$ 안에서 $x_0$으로 향하게 하는 homotopy ($t_1$-좌표를 따라 $I^{n-1}$을 $J^{n-1}$ 쪽으로 미는 것) 를 제공하므로 $i_\ast\partial=0$이다. 역으로 $g:(I^{n-1},\partial I^{n-1})\rightarrow(A,x_0)$이 $i_\ast[g]=0$을 만족하면, $g$를 $X$ 안에서 $x_0$으로 보내는 homotopy $H:I^{n-1}\times I\rightarrow X$가 존재한다. $H$를 $I^n$ 위의 함수로 보면 이는 쌍 $(X,A)$의 원소 $[H]$를 정의하고 $\partial[H]=[g]$가 성립한다.

각 단계에서 사용한 변형이 쌍의 조건과 base point를 유지함을 확인하는 것은 기술적이지만 직접적이며, 자세한 내용은 [Hat]의 정리 4.3에 있다.
:::

이 exact sequence는 [§호몰로지의 계산, ⁋정의 1](/ko/math/algebraic_topology/computation_of_homology#def1)에서 relative homology가 이루는 장거리 exact sequence의 homotopy 판본이다. 우리의 전략은 fibration $p:E\rightarrow B$에 대하여 쌍 $(E,F)$의 이 exact sequence를 취한 뒤, 상대항 $\pi_n(E,F)$를 밑공간의 절대 homotopy group $\pi_n(B)$으로 바꾸는 것이다. 이 교체를 가능하게 하는 것이 다음의 보조정리이며, HLP가 결정적으로 쓰이는 곳이다.

::: 보조정리 9
$p:E\rightarrow B$가 Serre fibration이고, $b_0\in B$, $F=p^{-1}(b_0)$, $e_0\in F$라 하자. 그럼 $p$가 유도하는 준동형

$$p_\ast:\pi_n(E,F,e_0)\rightarrow\pi_n(B,b_0)$$

은 모든 $n\geq 1$에 대하여 isomorphism이다.
:::
::: 증명
$p_\ast$가 잘 정의됨은 $p$가 $F=p^{-1}(b_0)$을 $b_0$으로, $e_0$을 $b_0$으로 보내므로 세 쌍의 함수를 세 쌍의 함수로 보내기 때문이다. 목표는 이 morphism이 전단사임을 보이는 것이며, 두 방향 모두 HLP를 통한 lifting으로 처리된다.

*전사성.* $\alpha:(I^n,\partial I^n)\rightarrow(B,b_0)$이 $\pi_n(B,b_0)$의 한 원소를 나타낸다 하자. $I^n=I^{n-1}\times I$로 보고, face $I^{n-1}\times\{0\}$ 위에서는 $\alpha$가 $b_0$의 값을 가지므로 이 face의 lifting을 상수함수 $e_0$으로 택한다. $\alpha$를 $I^{n-1}$을 매개변수로 하고 마지막 좌표를 시간으로 하는 homotopy로 간주하면, $I^{n-1}$에 대한 HLP에 의하여 lifting $\widetilde{\alpha}:I^n\rightarrow E$가 존재하여 $p\circ\widetilde{\alpha}=\alpha$이고 $\widetilde{\alpha}\vert_{I^{n-1}\times\{0\}}=e_0$이도록 할 수 있다. 그럼 $\widetilde{\alpha}$는 $\partial I^n$을 $p^{-1}(b_0)=F$로 보내므로 쌍 $(E,F)$의 원소를 정의하고, 필요한 경우 $J^{n-1}$ 위의 값을 $F$ 안에서 $e_0$으로 미는 추가 변형을 거쳐 $\pi_n(E,F,e_0)$의 원소 $[\widetilde{\alpha}]$를 얻으며 $p_\ast[\widetilde{\alpha}]=[\alpha]$이다.

*단사성.* $p_\ast[\widetilde{\alpha}]=0$이라 하자. 그럼 $p\circ\widetilde{\alpha}$가 $\pi_n(B,b_0)$에서 상수 $b_0$으로 향하는 homotopy를 가지며, 이 homotopy를 초기 lifting $\widetilde{\alpha}$ 위에서 HLP로 들어올리면 $\widetilde{\alpha}$가 $F$ 안으로 향하는 쌍의 homotopy를 얻는다. 이는 $[\widetilde{\alpha}]=0$을 뜻한다.

두 논법 모두 요점은 밑공간에서의 함수와 그 homotopy를 HLP로 전공간으로 들어올릴 수 있다는 것이며, lifting의 face들이 정확히 fiber로 떨어진다는 사실이다. 세부적인 매개변수 조정은 [Hat]의 정리 4.41에 상세하다.
:::

## Fibration의 장거리 완전열

이제 준비된 두 결과를 결합하면 이 글의 핵심 정리가 얻어진다.

::: 정리 10 (Fibration의 장거리 exact sequence)
$p:E\rightarrow B$가 Serre fibration이고 $B$가 path-connected라 하자. Base point $b_0\in B$과 $e_0\in F=p^{-1}(b_0)$을 고정하면, 다음의 장거리 exact sequence

$$\cdots\rightarrow\pi_n(F,e_0)\overset{i_\ast}{\longrightarrow}\pi_n(E,e_0)\overset{p_\ast}{\longrightarrow}\pi_n(B,b_0)\overset{\partial}{\longrightarrow}\pi_{n-1}(F,e_0)\rightarrow\cdots$$

이 존재하며, 이는

$$\cdots\rightarrow\pi_1(B,b_0)\overset{\partial}{\longrightarrow}\pi_0(F)\rightarrow\pi_0(E)$$

으로 끝난다. 여기에서 $i:F\hookrightarrow E$는 inclusion이고, 낮은 항에서는 base point를 가진 집합들의 exact sequence로 이해한다.
:::
::: 증명
쌍 $(E,F)$에 [명제 8](#prop8)을 적용하면 exact sequence

$$\cdots\rightarrow\pi_n(F,e_0)\overset{i_\ast}{\longrightarrow}\pi_n(E,e_0)\overset{j_\ast}{\longrightarrow}\pi_n(E,F,e_0)\overset{\partial}{\longrightarrow}\pi_{n-1}(F,e_0)\rightarrow\cdots$$

을 얻는다. 이제 [보조정리 9](#lem9)의 isomorphism $p_\ast:\pi_n(E,F,e_0)\overset{\cong}{\rightarrow}\pi_n(B,b_0)$을 이용하여 각 상대항 $\pi_n(E,F,e_0)$을 $\pi_n(B,b_0)$으로 대체한다. Exact sequence의 한 항을 그것과 isomorphic한 항으로, morphism들과 가환하도록 바꾸면 완전성은 보존되므로, 남은 것은 두 morphism이 어떻게 바뀌는지를 확인하는 것뿐이다.

우선 $\pi_n(E)\rightarrow\pi_n(E,F)\overset{p_\ast}{\rightarrow}\pi_n(B)$의 합성을 보면, $f:(I^n,\partial I^n)\rightarrow(E,e_0)$에 대하여 $j_\ast[f]$는 $f$를 쌍의 원소로 본 것이고 여기에 $p_\ast$를 취하면 $[p\circ f]$이다. 이는 곧 $p:E\rightarrow B$가 유도하는 절대 준동형 $p_\ast:\pi_n(E)\rightarrow\pi_n(B)$과 같다. 즉 $j_\ast$ 자리에는 $p_\ast$가 온다. 다음으로 상대항의 connecting homomorphism $\partial:\pi_n(E,F)\rightarrow\pi_{n-1}(F)$은 대체 후 $\partial\circ(p_\ast)^{-1}:\pi_n(B)\rightarrow\pi_{n-1}(F)$이 되며, 이것이 정리에서 말하는 $\partial$이다. 이로써 원하는 exact sequence를 얻는다.

수열이 $\pi_0(F)\rightarrow\pi_0(E)$에서 끝나는 것은 [명제 8](#prop8)의 쌍의 exact sequence가 그 지점에서 끝나기 때문이다. $B$가 path-connected라는 가정은 $\pi_0(B)$가 자명하여 마지막 $\pi_0$ 항들의 완전성이 올바르게 해석됨을 보장한다.
:::

정리의 exact sequence에서 세 종류의 morphism이 등장한다. $i_\ast$는 fiber의 loop를 전공간의 loop로 포함시키는 것이고, $p_\ast$는 전공간의 함수를 밑공간으로 밀어내리는 것이며, connecting homomorphism $\partial$은 밑공간의 $n$차원 원소를 fiber의 $(n-1)$차원 원소로 떨어뜨리는 것이다. 특히 $\partial$은 [보조정리 9](#lem9)에 의해 밑공간의 원소를 전공간으로 들어올린 뒤 그 경계면이 fiber에 남긴 흔적을 취하는 것으로 이해할 수 있으며, 이것이 이 exact sequence가 계산에서 위력을 발휘하는 근본적인 이유이다. 예컨대 전공간의 homotopy가 모두 자명하다면 $\partial$이 isomorphism이 되어 밑공간과 fiber의 homotopy group이 한 차원 차이로 맞물리게 된다.

## 예시

::: 예시 11 (경로-고리 fibration)
Base point $b_0$을 가진 path-connected 공간 $B$에 대하여, $b_0$에서 출발하는 path들의 공간

$$PB=\{\gamma:I\rightarrow B\mid \gamma(0)=b_0\}$$

을 compact-open topology로 생각하자. 그럼 끝점 계산 함수 $p:PB\rightarrow B$, $\gamma\mapsto\gamma(1)$은 Hurewicz fibration임이 알려져 있으며, 그 fiber $p^{-1}(b_0)$은 $b_0$을 base point로 하는 loop들의 공간, 곧 loop space $\Omega B$이다.

전공간 $PB$는 contractible이다. 실제로 각 path를 시간에 따라 시작점 쪽으로 되감는

$$H(\gamma,s)(t)=\gamma\bigl((1-s)t\bigr)$$

이 항등함수에서 상수 path $c_{b_0}$으로의 homotopy를 준다. 따라서 모든 $n$에 대하여 $\pi_n(PB)=0$이다. 이제 [정리 10](#thm10)의 exact sequence

$$\pi_n(PB)\overset{p_\ast}{\longrightarrow}\pi_n(B)\overset{\partial}{\longrightarrow}\pi_{n-1}(\Omega B)\longrightarrow\pi_{n-1}(PB)$$

에서 양 끝 항이 $0$이므로 connecting homomorphism $\partial:\pi_n(B)\rightarrow\pi_{n-1}(\Omega B)$이 isomorphism이다. 곧 모든 $n\geq 1$에 대하여

$$\pi_n(\Omega B)\cong\pi_{n+1}(B)$$

이 성립한다. 이는 loop space가 homotopy group의 degree를 하나 낮춘다는 기본적인 사실이며, 고차 homotopy group을 loop space의 낮은 homotopy group으로 환원하는 통로가 된다.
:::

::: 예시 12 (피복사상)
[명제 6](#prop6)에 의하여 covering map $p:E\rightarrow B$는 fibration이고 그 fiber $F$는 discrete space이다. Discrete space의 각 성분은 한 점이므로 $\pi_n(F)=0$이 모든 $n\geq 1$에 대하여 성립하고, $\pi_0(F)$는 fiber의 점들의 집합이다. 이를 [정리 10](#thm10)의 exact sequence에 대입하면, $n\geq 2$인 부분에서

$$0=\pi_n(F)\rightarrow\pi_n(E)\overset{p_\ast}{\longrightarrow}\pi_n(B)\rightarrow\pi_{n-1}(F)=0$$

이 되어 $p_\ast:\pi_n(E)\rightarrow\pi_n(B)$이 모든 $n\geq 2$에 대하여 isomorphism이다. 즉 covering space는 밑공간의 고차 homotopy group을 그대로 물려받는다. 한편 exact sequence의 꼬리 부분

$$0=\pi_1(F)\rightarrow\pi_1(E)\overset{p_\ast}{\longrightarrow}\pi_1(B)\overset{\partial}{\longrightarrow}\pi_0(F)\rightarrow\pi_0(E)$$

은 $p_\ast:\pi_1(E)\rightarrow\pi_1(B)$이 injective임을 주며, $\partial:\pi_1(B)\rightarrow\pi_0(F)$은 $\pi_1(B,b_0)$이 fiber $F=p^{-1}(b_0)$에 작용하는 monodromy를 나타낸다. 이는 covering space 이론에서 알려진 $\pi_1$의 단사성과 fiber 위의 $\pi_1$-monodromy action([§피복공간, ⁋따름정리 12](/ko/math/algebraic_topology/covering_spaces#cor12) 부근에서 논의되는 Galois 대응의 밑바탕이 되는 사실들)에 대응하는 exact sequence 판본이다.

특히 universal cover $\mathbb{R}\rightarrow S^1$을 생각하면, $\mathbb{R}$이 contractible이므로 $\pi_n(\mathbb{R})=0$이고 따라서

$$\pi_n(S^1)\cong\pi_n(\mathbb{R})=0\qquad(n\geq 2)$$

임을 안다. 곧 $S^1$은 $\pi_1(S^1)\cong\mathbb{Z}$ 외의 모든 homotopy group이 자명하다.
:::

다음 예시를 위해 구의 낮은 homotopy group에 대한 기본적인 사실이 필요하다.

::: 명제 13
$n\geq 1$에 대하여, 구 $S^n$은 $(n-1)$-connected이다. 곧 모든 $0<i<n$에 대하여 $\pi_i(S^n)=0$이다.
:::
::: 증명
임의의 연속함수 $f:S^i\rightarrow S^n$이 $i<n$일 때 null-homotopic임을 보이면 된다. 핵심은 $f$가 전사가 아니도록 변형할 수 있다는 것이다. 연속함수는 항상 smooth (혹은 simplicial) 함수와 homotopic하며, $i<n$일 때 $S^i$에서 $S^n$으로의 smooth 함수의 image는 measure zero이므로 (Sard의 정리 또는 차원 비교에 의하여) 전사일 수 없다. 따라서 $f$는 어떤 점 $q\in S^n$을 image로 갖지 않는 함수와 homotopic하고, 그 함수는

$$S^n\setminus\{q\}\cong\mathbb{R}^n$$

을 통과하는데 $\mathbb{R}^n$이 contractible이므로 null-homotopic이다. 자세한 논의는 [Hat]의 따름정리 4.9에 있다.
:::

::: 예시 14 (Hopf fibration)
$S^3$을 $\mathbb{C}^2$의 단위구

$$S^3=\{(z_0,z_1)\in\mathbb{C}^2\mid \lvert z_0\rvert^2+\lvert z_1\rvert^2=1\}$$

로 보고, 각 점을 그것이 정하는 복소 직선으로 보내는 함수

$$p:S^3\rightarrow\mathbb{CP}^1\cong S^2;\qquad (z_0,z_1)\mapsto[z_0:z_1]$$

를 생각하자. 이를 *Hopf fibration*이라 부른다. 한 점 $[z_0:z_1]$ 위의 fiber는 $\{(\lambda z_0,\lambda z_1)\mid \lambda\in\mathbb{C}, \lvert\lambda\rvert=1\}$이며 이는 $S^1$과 homeomorphic하다. $p$는 locally trivial fiber bundle이므로 Serre fibration이고 ([참고 5](#rmk5)), 따라서 우리는 fibration $S^1\rightarrow S^3\rightarrow S^2$을 얻는다.

[정리 10](#thm10)의 exact sequence에서 $n=3$ 주변을 보면

$$\pi_3(S^1)\rightarrow\pi_3(S^3)\overset{p_\ast}{\longrightarrow}\pi_3(S^2)\overset{\partial}{\longrightarrow}\pi_2(S^1)$$

이다. [예시 12](#ex12)에 의하여 $\pi_3(S^1)=\pi_2(S^1)=0$이므로, $p_\ast:\pi_3(S^3)\rightarrow\pi_3(S^2)$은 isomorphism이다. 즉

$$\pi_3(S^2)\cong\pi_3(S^3)$$

이다. 이제 오른쪽 항을 계산하자. [명제 13](#prop13)에 의하여 $\pi_1(S^3)=\pi_2(S^3)=0$이므로, [정리 2](#thm2)에 의하여 Hurewicz 준동형

$$h_3:\pi_3(S^3)\rightarrow H_3(S^3)$$

이 isomorphism이다. 한편 [§호몰로지의 계산, ⁋명제 7](/ko/math/algebraic_topology/computation_of_homology#prop7)의 Mayer-Vietoris exact sequence를 $S^3$을 두 반구로 덮어 적용하는 표준적 계산으로 $H_3(S^3)\cong\mathbb{Z}$를 얻는다. 따라서

$$\pi_3(S^2)\cong\pi_3(S^3)\cong H_3(S^3)\cong\mathbb{Z}$$

이다. 이는 대단히 비자명한 결과인데, 정의역 $S^3$의 차원이 공역 $S^2$보다 높음에도 $\pi_3(S^2)$이 자명하지 않으며, 더구나 무한군임을 말해주기 때문이다. 그 generator는 Hopf fibration $p$ 자신의 homotopy equivalence class로 주어진다.
:::

이 예시는 [명제 13](#prop13)가 주는 $\pi_i(S^n)=0$ ($i<n$) 이라는 소극적 정보 너머에서 구의 homotopy group이 얼마나 복잡할 수 있는지를 보여준다. 실제로 이러한 fibration을 겹겹이 쌓아 얻는 계산을 체계화하면, 밑공간과 fiber의 homology로부터 전공간의 homology (그리고 homotopy) 를 근사하는 강력한 장치인 Serre spectral sequence에 이르게 되며, 이것이 고차 homotopy group에 대한 현대적 계산의 출발점이 된다.

## Serre 스펙트럼 열

이 계산을 체계화하는 장치가 Serre spectrum 열로, 밑공간과 fiber의 cohomology에서 출발하여 전공간의 cohomology를 근사해 나가는 [\[호몰로지 대수학\] §스펙트럼 열, ⁋정의 1](/ko/math/homological_algebra/spectral_sequences#def1)의 spectrum 열이다. 우리는 이 글에서 이를 증명 없이 서술하고 그 구성의 출처만 밝힌다.

::: 정리 15 (Serre spectral sequence)
Serre fibration $F\rightarrow E\overset{\pi}{\rightarrow}B$에서 $B$가 path-connected이고 $\pi_1(B)$이 $H^\bullet(F;\mathbb{Z})$에 자명하게 작용한다 하자. (가령 $B$가 simply connected이면 그러하다.) 그럼 first-quadrant cohomological spectrum 열 $\{E_r^{p,q}, d_r\}$이 존재하여

$$E_2^{p,q}=H^p\bigl(B;H^q(F;\mathbb{Z})\bigr)$$

이고, 미분은 $d_r:E_r^{p,q}\rightarrow E_r^{p+r,q-r+1}$의 형태이며, 이 spectrum 열은 전공간의 cohomology에 수렴한다. 곧 $E_2^{p,q}\Rightarrow H^{p+q}(E;\mathbb{Z})$이다.
:::

$E_2$-page는 밑공간의 cohomology를 fiber의 cohomology를 계수로 삼아 적은 것이다. 만일 모든 미분 $d_r$이 소멸한다면 $E_2=E_\infty$가 되어 전공간의 cohomology가 $H^\bullet(B)$와 $H^\bullet(F)$의 tensor product처럼 나타나는데, 이는 [§코호몰로지, ⁋따름정리 10](/ko/math/algebraic_topology/cohomology#cor10)이 곱공간 $B\times F$에 대해 주던 결론의 뒤틀린 fibration 판본이다. 일반적으로는 미분들이 이 곱을 보정하며, 그 보정을 누적한 것이 전공간의 cohomology를 준다. [정리 15](#thm15)에서 수렴이 뜻하는 바는 [\[호몰로지 대수학\] §스펙트럼 열, ⁋정의 5](/ko/math/homological_algebra/spectral_sequences#def5)에서와 같이 $H^n(E)$ 위의 filtration의 associated graded가 $\bigoplus_{p+q=n}E_\infty^{p,q}$이라는 것이다.

이 spectrum 열은 전공간의 singular cochain complex를 밑공간의 skeleton들의 preimage로 여과하여 얻은 filtered complex에 [\[호몰로지 대수학\] §스펙트럼 열, ⁋명제 10](/ko/math/homological_algebra/spectral_sequences#prop10)을 적용하여 얻어지며, 비자명한 부분은 그 $E_2$-page가 위와 같이 밑공간의 cohomology로 식별된다는 데 있다. 밑공간이 단순연결이 아닐 때에는 $\pi_1(B)$의 action을 담는 국소계수계로 $E_2$를 적어야 한다. 자세한 구성은 [May]와 [tD]에 있다.

--- 

**참고문헌**

[Hat] A. Hatcher, *Algebraic Topology*. Cambridge University Press, 2022.  
[May] J. P. May, *A concise course in algebraic topology*. University of Chicago Press, 1999.  
[tD] T. tom Dieck, *Algebraic Topology*. European Mathematical Society, 2008.

---
