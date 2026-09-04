---
title: "실로우 정리"
description: "유한군의 소수 거듭제곱 부분군인 p군의 성질을 다루며, 고정점 보조정리와 중심의 비자명성을 통해 p군의 항등성과 실로우 정리를 전개한다."
excerpt: "유한군의 p-부분군과 Sylow의 세 정리"

categories: [Math / Group Theory]
permalink: /ko/math/group_theory/Sylow_theorems
sidebar: 
    nav: "group_theory-ko"

date: 2025-04-07
weight: 4

---

## $p$-군

이번 글에서 $p$는 항상 소수를 나타낸다. 

::: 정의 1
Finite group $G$가 *$p$-group*이라는 것은 $G$의 크기가 $p$의 거듭제곱인 것이다. 
:::

그럼 $p$-group의 subgroup과 quotient group이 다시 $p$-group임은 자명하다. 또, 다음이 성립한다.

::: 보조정리 2
$p$-group $G$가 유한집합 $E$ 위에 act한다 하고, 이 action의 fixed point들의 모임

$$E^G=\{x\in E\mid g\cdot x=x\text{ for all $g\in G$}\}$$

을 생각하자. 그럼

$$\lvert E^G\rvert\equiv\lvert E\rvert\pmod{p}$$

이 성립한다.
:::
::: 증명
즉, 집합 $E\setminus E^G$의 크기가 $p$의 배수임을 보여야 한다. 그런데 $E\setminus E^G$는 그 크기가 $1$보다 큰 (disjoint한) $G$-orbit들의 합집합이고, 이들 각각의 orbit은 [\[대수적 구조\] §군의 작용, ⁋정리 14](/ko/math/algebraic_structures/group_actions#thm14)에 의하여 그 크기가 $p$의 거듭제곱이므로 이것이 성립한다. 
:::

특별히 $E=G$ 위에 $G$가 inner automorphism으로 act하는 경우를 생각하면 $E^G$는 정확하게 $G$의 center이므로, [보조정리 2](#lem2)에 의하여 $p$-group $G$의 center $Z(G)$는 trivial group이 아님을 알 수 있다. 

::: 정리 3
크기 $p^r$의 $p$-group $G$에 대하여, $G$의 subgroup들의 series 

$$G=G_1\supset G_2\supset\cdots\supset G_{n+1}=\{e\}$$

가 존재하여, $[G, G_k]\subseteq G_{k+1}$이 모든 $k$에 대해 성립하고, $G_k/G_{k+1}$이 order $p$의 cyclic group이도록 할 수 있다. 
:::
::: 증명
$G$의 크기에 대한 귀납법으로 증명한다. 우선 $G=\{e\}$인 경우는 증명할 것이 없다. 이제 $\lvert G\rvert=p^r$보다 작은 모든 $p$-group에서 주어진 주장이 성립한다 하고, $\lvert G\rvert=p^r$인 경우를 증명하자. 앞선 논증으로부터 $Z(G)\neq\{e\}$이므로, 적당한 $x\in Z(G)$가 존재하여 그 order가 $p^s$ ($1\leq s\leq r$)이도록 할 수 있다. 

이제 원소 $x^{p^{s-1}}$로 생성되는 $Z(G)$의 subgroup $H$를 생각하면, $G'=G/H$는 그 크기가 $p^{r-1}$인 $p$-group이므로 귀납적 가정에 의하여 주어진 조건을 만족하는 subgroup들의 series가 존재하며, 이제 이를 canonical projection $\pi: G \rightarrow G'$의 inverse image로 보낸 것이 원하는 조건을 만족한다. 다만 이렇게 얻어진 series의 마지막 항은 $\pi^{-1}(\{e\})=H$이므로 여기에 $G_{n+2}=\{e\}$를 한 항 더 이어붙이며, $H\subseteq Z(G)$로부터 $[G, H]=\{e\}$이고 $H/\{e\}\cong H$가 order $p$의 cyclic group이므로 이 마지막 단계에서도 두 조건이 성립한다. 
:::

따라서 [§군의 열, ⁋명제 7](/ko/math/group_theory/series_of_groups#prop7)의 첫째 조건과 둘째 조건의 동치에 의하여 임의의 $p$-group은 항상 nilpotent임을 안다.

한편 [§군의 열, ⁋명제 8](/ko/math/group_theory/series_of_groups#prop8)에 의해 다음을 얻는다. 

::: 명제 4
$p$-group $G$와, subgroup $H\subsetneq G$를 고정하자. 

1. $H$의 $G$에서의 normalizer $N_G(H)$는 $H\subsetneq N_G(H)$를 만족한다. 
2. $G$의 적당한 index $p$짜리 normal subgroup $N$이 존재하여 $H$를 포함한다. 
:::

따라서 $p$-group $G$의 임의의 index $p$ subgroup은 항상 normal이다. 

## 실로우 정리

우리는 이제 일반적인 group의 $p$-subgroup을 살펴본다. 그 중 특별한 관심의 대상이 되는 것은 다음과 같다.

::: 정의 5
Finite group $G$의 *Sylow $p$-subgroup<sub>실로우 $p$-부분군</sub>*은 다음의 두 조건을 만족하는 $G$의 subgroup $P$를 뜻한다.

1. $P$는 $p$-group이다. 
2. $[G:P]$는 $p$의 배수가 아니다. 

$G$의 Sylow $p$-subgroup들의 모임을 $\Syl_p(G)$로 적는다. 
:::

즉, $G$의 크기가 $p^r m$ ($p\nmid m$)으로 주어질 때, Sylow $p$-group $P$는 정확히 order $p^r$를 갖는 $G$의 subgroup이다. 앞으로 남은 글에서 $G$의 크기 $n=p^rm$은 항상 $p\nmid m$을 만족하는 것으로 가정하자. 

실로우 정리는 임의의 finite group의 Sylow $p$-subgroup에 대한 정리들로서, finite group을 분류하는 데에 도움을 준다. 첫 번째 결과는 Sylow $p$-subgroup의 존재성에 대한 것으로, 이를 위해서는 우선 다음의 보조정리가 필요하다.

::: 보조정리 6
$n=p^rm$이라 하고 $p\nmid m$이라 하자. 그럼

$$\binom{n}{p^r}\not\equiv 0\pmod{p}$$

이 성립한다. 
:::
::: 증명
크기 $p^r$의 group $G$와 크기 $m$의 집합 $S$를 생각하자. 그럼 집합 $G\times S$는 크기 $n$의 집합이며, 집합 $E$를 $G\times S$의 크기 $p^r$짜리 부분집합들의 집합으로 정의하면

$$\lvert E\rvert=\binom{n}{p^r}$$

이 성립한다. $G$가 $G\times S$ 위에서 다음의 식

$$g \cdot (x, s) = (g x, s) \quad (g, x \in G,\; s \in S)$$

으로 act한다 하면, $E$의 각 원소들 (즉 $G\times S$의 크기 $p^r$짜리 부분집합들)의 각 원소들에 이 action을 적용함으로써 $G$의 $E$ 위에서의 action이 주어진다. 이 action에 대한 fixed point의 모임 $E^G$는 모두 다음의 꼴

$$G \times \{s\},\qquad s\in S$$

이므로, $\lvert E^G\rvert=m$이고 이제 [보조정리 2](#lem2)에 의하여 

$$\binom{n}{p^r} = \lvert E\rvert \equiv \lvert E^G\rvert = m \not\equiv 0 \pmod{p}$$

가 성립한다. 
:::

그럼 실로우 정리의 첫 번째 결과는 Sylow $p$-subgroup의 존재성에 대한 것이다. 

::: 정리 7
$G$는 Sylow $p$-subgroup을 가진다. 
:::
::: 증명
$G$의 부분집합 중 원소 개수가 $p^r$인 것들의 집합을 $E$라 하자. 그러면 [보조정리 6](#lem6)에 의하여

$$\lvert E\rvert = \binom{n}{p^r}\not\equiv 0\pmod{p}$$

이다. 이제 group $G$의 자기 자신 위에서의 left translation action 

$$L_g:G \rightarrow G;\qquad x\mapsto gx$$

을 생각하고 [보조정리 6](#lem6)의 증명과 같은 방식으로 이 action을 $E$ 위에서 정의된 action으로 보자. 그럼 $\lvert E\rvert\not\equiv 0\pmod{p}$라는 가정으로부터, $p$의 배수가 아닌 orbit $O$가 존재한다. 이제 $O$의 한 원소를 $X$라 하고, $X$의 stabilizer를 $\Stab(\{X\})=\Stab(X)$라 하자. 그럼 $\Stab(X)$는 $G$의 subgroup이며 ([\[대수적 구조\] §군의 작용, ⁋따름정리 8](/ko/math/algebraic_structures/group_actions#cor8)) 이것이 우리가 원하는 subgroup이 된다. 

이를 보이기 위해 우선 [\[대수적 구조\] §군의 작용, ⁋정리 14](/ko/math/algebraic_structures/group_actions#thm14)로부터

$$\lvert O\rvert=\lvert G\cdot X\rvert=[G:\Stab(X)]=\frac{\lvert G\rvert}{\lvert\Stab(X)\rvert}\not\equiv 0\pmod{p}$$

이므로, $p^r$이 $\lvert \Stab(X)\rvert$를 나눈다.

한편, $\Stab(X)$는 $g\in G$ 중 $gX = X$를 만족하는 원소들의 모임이며, 따라서 임의의 원소 $x \in X$에 대해

$$\Stab(X) \subseteq X x^{-1}$$

이므로 

$$\lvert \Stab(X)\rvert\leq\lvert Xx^{-1}\rvert=\lvert X\rvert=p^r$$

이어야 한다. 이로부터 $\lvert\Stab(X)\rvert=p^r$임을 안다. 
:::

이로부터 우리는 임의의 finite group $G$의 크기가 $p$로 나누어떨어진다면 $G$는 order $p$의 원소를 갖는다는 사실을 안다. 

우리는 $G$의 두 subgroup $H_1, H_2$에 대하여, $\rho(H_1)=H_2$이도록 하는 $\rho\in\Inn(G)$가 존재하면 $H_1$과 $H_2$이 서로 *conjugate*하다고 말한다. 

::: 정리 8
다음이 성립한다. 

1. $G$의 Sylow $p$-subgroup들은 서로 conjugate하며, 그 개수는 $1$ mod $p$이다.
2. $G$의 모든 $p$-subgroup은 어떤 Sylow $p$-subgroup에 포함된다.
:::
::: 증명
$P$를 $G$의 Sylow $p$-subgroup이라 하고, $H$를 $G$의 $p$-subgroup이라 하자. 집합 $E = G/P$위의 $H$의 left translation action을 생각하면, $\lvert E\rvert=[G:P]$가 $p$의 배수가 아니므로 [보조정리 2](#lem2)에 의해 $\lvert E^H\rvert\neq 0$이고, 따라서 $Hx=x$인 $x\in G/P$가 존재한다. 이제 $G/P$의 원소 $x$의 representative를 $g\in G$를 택하자. 그러면 임의의 $h \in H$에 대해 $h(gP) = gP$이므로 $g^{-1} h g \in P$이다. 따라서 $H \subseteq gPg^{-1}$이고, 이로써 둘째 주장이 증명된다.

이제 $H$가 Sylow $p$-subgroup이라 하자. 그러면

$$\lvert H \rvert = \lvert P \rvert = \lvert gPg^{-1} \rvert$$

이므로, 위의 포함관계가 $H = gPg^{-1}$가 되어 첫째 주장의 앞부분이 증명된다.

이제 첫째 주장의 뒷부분을 증명하기 위해, $P$가 $\Syl_p(G)$ 위에 conjugation으로 작용하게 하자. 그럼 앞선 논증으로부터 $P$ 자신은 이 action의 fixed point이며, 우리는 이것이 *유일한* fixed point임을 보인다. 

결론에 반하여 다른 fixed point $Q \in \Syl_p(G)$가 있다고 가정하자. $Q$는 $G$의 Sylow $p$-subgroup이며, $P$에 의해 normalize된다. 즉 $P\subseteq N_G(Q)$이다. 이제 $P$와 $Q$는 모두 $N_G(Q)$의 Sylow $p$-subgroup들이고, 따라서 앞선 논증에 의해 적당한 $n \in N_G(Q)$가 존재하여

$$P = nQn^{-1} = Q$$

가 성립한다. 따라서 [보조정리 2](#lem2)로부터 $\lvert \Syl_p(G) \rvert \equiv \lvert \Syl_p(G)^P \rvert = 1 \pmod{p}$임을 안다. 
:::

::: 따름정리 9
$P\in\Syl_p(G)$와 normalizer $N_G(P)$를 생각하자. $N_G(P)$을 포함하는 $G$의 subgroup $M$에 대하여, $M$의 $G$에서의 normalizer $N_G(M)$은 $M$과 같다.
:::

::: 증명
$M=gMg^{-1}$을 만족하는 $g\in G$를 택하자. 그럼 $gPg^{-1}$는 $M$의 Sylow $p$-subgroup이다. 따라서 적당한 $h \in M$가 존재하여 $gPg^{-1} = hPh^{-1}$가 된다. 이제 $h^{-1}g \in N_G(P)$이고, 따라서 $g \in hN_G(P) \subseteq M$이다.
:::

::: 따름정리 10
 Finite group 사이의 group homomorphism $f: G_1 \rightarrow G_2$을 고정하자.  $G_1$의 Sylow $p$-subgroup $P_1$에 대해, $f(P_1)$를 포함하는 $G_2$의 Sylow $p$-subgroup $P_2$가 존재한다.
:::

::: 증명
$G_2$의 subgroup $f(P_1)$에 대해 [정리 8](#thm8)의 둘째 결과를 적용하면 된다.
:::

::: 따름정리 11
1. $H$를 $G$의 subgroup이라 하자. $H$의 Sylow $p$-subgroup $P$에 대해, $G$의 Sylow $p$-subgroup $Q$가 존재하여 $P = Q \cap H$가 된다.
2. 반대로, $Q$를 $G$의 Sylow $p$-subgroup이라 하고 $H$를 $G$의 normal subgroup이라 하자. 그러면 $Q \cap H$는 $H$의 Sylow $p$-subgroup이다.
:::

::: 증명
1. $p$-group $P$는 $G$의 Sylow $p$-subgroup $Q$에 포함된다. 한편 $Q \cap H$는 $P$를 포함하는 $H$의 $p$-subgroup이므로, 결국 $P = Q \cap H$이다.
2. $P'$를 $H$의 Sylow $p$-subgroup이라 하자. 그러면 적당한 $g \in G$가 존재하여 $gP'g^{-1} \subseteq Q$가 된다. $H$가 normal subgroup이므로, $P = gP'g^{-1}$는 다시 $H$에 포함되고 따라서 $P$는 $Q\cap H$에 포함된다. 이제 $Q \cap H$는 $H$의 $p$-subgroup이고, $P$는 Sylow $p$-subgroup이므로 $P = Q \cap H$이다.
:::

::: 따름정리 12
$N$을 $G$의 normal subgroup이라 하자. 그럼 $G$의 Sylow $p$-subgroup의 $G/N$에서의 이미지는 $G/N$의 Sylow $p$-subgroup이 되고, 뿐만 아니라 모든 $G/N$의 Sylow $p$-subgroup은 이런 식으로 얻어진다.
:::

::: 증명
$P\in \Syl_p(G)$를 고정하고, $G' = G/N$, $P$의 $G'$에서의 image를 $P'$라고 하자. 

$G$의 $G'/P'$ 위에서의 left translation action을 생각하면 이는 transitive action이므로, $G$의 orbit은 $G'/P'$ 자기 자신 뿐이다. 이제 [\[대수적 구조\] §군의 작용, ⁋정리 14](/ko/math/algebraic_structures/group_actions#thm14)에 의하여

$$\lvert G'/P'\rvert=[G:\Stab(eP')]$$

이다. 그런데 정의에 의하여 $\Stab(eP')$는 $P$를 포함하므로, $[G:\Stab(eP')]$는 $p$의 배수가 아니고 따라서 $[G':P']$도 $p$의 배수가 아니다. 한편 $P'$는 $p$-group이므로, 정의에 의해 $P'$는 $G'$의 Sylow $p$-subgroup이다.

반대방향의 경우, $G'$의 다른 Sylow $p$-subgroup $Q'$를 생각하면 적당한 $g' \in G'$에 대해 $Q' = g'P'g'^{-1}$이고, $g'$의 representative $g \in G$를 잡으면 $gPg^{-1}$의 이미지가 $Q'$가 된다.
:::

## 실로우 정리의 활용

앞서 언급한 것과 같이, Sylow theorem은 finite group의 classification에 유용하게 사용된다. 이를 위해 [정리 8](#thm8)을 조금 더 뜯어보자. $\Syl_p(G)$의 크기를 $n_p$라 하면, [정리 8](#thm8)의 첫 번째 결과의 뒷부분에 의하여 $n_p\equiv 1\pmod{p}$이다. 한편, [정리 8](#thm8)의 첫째 결과의 앞부분은 $G$가 $\Syl_p(G)$ 위에 transitive하게 act한다는 것을 보여주므로 [\[대수적 구조\] §군의 작용, ⁋정리 14](/ko/math/algebraic_structures/group_actions#thm14)에 의하여

$$n_p=\lvert \Syl_p(G)\rvert=[G:\Stab(P)],\qquad P\in\Syl_p(G)$$

를 얻으며, 특히 $n_p$는 $\lvert G\rvert$를 나눠야 하고, $n_p\equiv 1\pmod{p}$로부터 $p$가 $n_p$를 나누지 않으므로 $n_p$는 반드시 $m$을 나눠야 한다. 

::: 예시 13
크기가 $15$인 finite group $G$를 분류해 보자.

$$\lvert G\rvert = 15 = 3\times 5$$

이다. Sylow 3-subgroup을 먼저 생각하자. 그럼 [정리 8](#thm8)에 의하여 Sylow 3-subgroup의 개수 $n_3$는 다음 두 조건

- $n_3\equiv 1\pmod{3}$,
- $n_3$는 $5$를 나눈다.

을 만족한다. 이 두 조건을 만족하는 $n_3$은 오직 $1$ 뿐이며, 이는 [정리 8](#thm8)의 결과에 의하여 $G$의 (유일한) Sylow $3$-subgroup $P_3$이 normal subgroup이라는 것이다. 

비슷하게 Sylow 5-subgroup에 대해서도 생각하자. Sylow 정리에 의해, Sylow 5-subgroup의 개수 $n_5$는 다음 조건을 만족한다:

- $n_5\equiv 1\pmod{5}$,
- $n_5$는 $3$을 나누어야 한다.

마찬가지로 이 두 조건을 만족하는 $n_5$ 또한 $1$ 뿐이므로 Sylow 5-subgroup도 유일하게 존재하며 normal subgroup이다. 이를 $P_5$라 적자. 

이제 $P_3\cap P_5$는 $P_3$과 $P_5$의 subgroup이므로, 그 크기가 $1$이어야 하고 따라서 $P_3\cap P_5=\{e\}$이다. 이제 $G$의 subgroup $P_3P_5$를 생각하면, [\[대수적 구조\] §군 동형사상, ⁋정리 5](/ko/math/algebraic_structures/isomorphism_theorems#thm5)로부터

$$\frac{P_3P_5}{P_3}\cong P_5/\{e\}\implies \lvert P_3P_5\rvert=\lvert P_3\rvert\lvert P_5\rvert=15=\lvert G\rvert$$

이므로 $G=P_3P_5$이고, $P_3$과 $P_5$가 모두 normal subgroup이면서 $P_3\cap P_5=\{e\}$이므로 결국 $G\cong \mathbb{Z}/3\mathbb{Z}\times \mathbb{Z}/5\mathbb{Z}$여야 한다. 
:::

Sylow 정리의 또 다른 강력한 응용으로, alternating group $A_5$가 simple group이라는 사실을 보이자. 이는 [§대칭군, ⁋예시 13](/ko/math/group_theory/symmetric_groups#ex13)에서 이미 conjugacy class의 구조를 직접 조사하여 증명하였다. 거기서는 $A_5$가 그다지 큰 group이 아니라는 점을 이용하여 원소의 종류를 일일이 분류하였는데, 여기서는 동일한 결론을 normal subgroup이 반드시 포함해야 하는 Sylow subgroup들을 세는 방식으로 다시 도출한다.

::: 명제 14
Alternating group $A_5$는 simple group이다.
:::

::: 증명
Alternating group의 크기는

$$\lvert A_5\rvert=\frac{5!}{2}=60=2^2\cdot 3\cdot 5$$

이다. 또 [§대칭군, ⁋예시 13](/ko/math/group_theory/symmetric_groups#ex13)에서 살펴본 바와 같이, $A_5$의 원소들은 항등원 1개, order 3의 원소(3-cycle) 20개, order 2의 원소(double transposition) 15개, order 5의 원소(5-cycle) 24개로 이루어진다.

이제 $N\triangleleft A_5$가 $N\neq\{e\}$을 만족한다 하고, $N=A_5$임을 보이자. $\lvert N\rvert$은 $60$의 약수이며, $60$의 약수 중 소수 $3$이나 $5$로 나누어떨어지지 않는 것은 $1,2,4$뿐이다. 따라서 $3$ 또는 $5$가 $\lvert N\rvert$을 나누거나, 그렇지 않으면 $\lvert N\rvert\in\{2,4\}$이다.

우선 $5\mid\lvert N\rvert$이라 하자. 그럼 $N$은 order $5$의 원소를 가지며, 이 원소가 생성하는 subgroup $P$는 곧 $A_5$의 Sylow 5-subgroup이다. $N$이 normal subgroup이므로 임의의 $g\in A_5$에 대하여 $gPg^{-1}\subseteq gNg^{-1}=N$이 성립하고, [정리 8](#thm8)에 의하여 $A_5$의 모든 Sylow 5-subgroup은 $P$와 conjugate이므로 결국 $N$은 이들 모두를 포함한다. 한편 $A_5$의 5-cycle은 24개이고, 각 Sylow 5-subgroup은 정확히 4개의 5-cycle을 원소로 가지며 서로 다른 Sylow 5-subgroup들은 order가 5인 subgroup이므로 항등원만을 공유한다. 따라서 Sylow 5-subgroup의 개수는 $n_5=24/4=6$이며, 이는 $n_5\equiv 1\pmod{5}$, $n_5\mid 12$라는 Sylow 정리의 결과와 일치한다. 그러므로 $N$은 24개의 order 5 원소를 포함하여 $\lvert N\rvert\geq 25$이고, $5\mid\lvert N\rvert$이며 $\lvert N\rvert\mid 60$이므로 $\lvert N\rvert\in\{30,60\}$이어야 한다.

비슷하게 $3\mid\lvert N\rvert$인 경우에도 같은 논증으로 $N$이 $A_5$의 모든 Sylow 3-subgroup을 포함함을 안다. 3-cycle이 20개이고 각 Sylow 3-subgroup은 2개의 3-cycle을 가지며 서로 다른 것들은 항등원만 공유하므로 $n_3=20/2=10$이고, $N$은 20개의 order 3 원소를 포함하여 $\lvert N\rvert\geq 21$이다. 마찬가지로 $\lvert N\rvert\in\{30,60\}$이다.

이제 $\lvert N\rvert\in\{2,4\}$인 경우를 배제하자. 만일 $\lvert N\rvert=4$라면 $N$은 $A_5$의 Sylow 2-subgroup이며, normal subgroup이므로 $A_5$의 유일한 Sylow 2-subgroup이다. 모든 order 2 원소는 자신이 생성하는 subgroup을 통해 어떤 Sylow 2-subgroup에 속하므로, 그러한 subgroup이 유일하다면 15개의 order 2 원소가 모두 그 안에 들어가야 한다. 그러나 $A_5$는 order $4$의 원소를 갖지 않으므로(가능한 order는 $1,2,3,5$뿐이다) 각 Sylow 2-subgroup은 Klein four-group $\mathbb{Z}/2\mathbb{Z}\times\mathbb{Z}/2\mathbb{Z}$이고, 따라서 order 2 원소를 정확히 3개만 가진다. 이는 모순이다. 한편 $\lvert N\rvert=2$라면 $N=\langle x\rangle$이고 $x$는 double transposition인데, $N$이 normal subgroup이려면 임의의 $g\in A_5$에 대하여 $gxg^{-1}=x$, 즉 $x$가 central이어야 한다. 그러나 임의의 double transposition $(ab)(cd)$를 3-cycle $(abc)$로 conjugate하면 $(abc)(ab)(cd)(abc)^{-1}=(ad)(bc)$가 되어 원래 원소와 다르므로, double transposition은 central일 수 없다. 이 또한 모순이다. 따라서 $\lvert N\rvert\notin\{2,4\}$이며, 앞선 논증에 의하여 $\lvert N\rvert\in\{30,60\}$이다.

마지막으로 $\lvert N\rvert=30$인 경우를 배제하자. $3\mid 30$이고 $5\mid 30$이므로, 앞선 두 논증에 의하여 $N$은 20개의 order 3 원소와 24개의 order 5 원소를 모두 포함해야 한다. 이들은 order가 서로 다르므로 겹치지 않으며, 항등원까지 합치면 $N$은 적어도 $20+24+1=45$개의 원소를 갖는다. 이는 $\lvert N\rvert=30$에 모순이다.

결론적으로 남는 가능성은 $\lvert N\rvert=60$뿐이며, 즉 $N=A_5$이다. 따라서 $A_5$는 simple group이다.
:::

---

**참고문헌**

**[DF]** D. S. Dummit and R. M. Foote, *Abstract algebra*, 3rd ed., Wiley, 2004.
