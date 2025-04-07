---

title: "실로우 정리"
excerpt: ""

categories: [Math / Group Theory]
permalink: /ko/math/group_theory/sylow_theorems
header:
    overlay_image: /assets/images/Math/Group_Theory/Sylow_theorems.png
    overlay_filter: 0.5
sidebar: 
    nav: "group_theory-ko"

date: 2025-04-07
last_modified_at: 2025-04-07
weight: 4

---

## Orbit-stabilizer theorem



이번 글에서 $p$는 항상 소수를 나타낸다. 

<div class="definition" markdown="1">

<ins id="def1">**정의 1**</ins> Finite group $G$가 *$p$-group*이라는 것은 $G$의 크기가 $p$의 거듭제곱인 것이다. 

</div>

그럼 $p$-group의 subgroup과 quotient group이 다시 $p$-group임은 자명하다. 또, 다음이 성립한다.

<div class="proposition" markdown="1">

<ins id="lem2">**보조정리 2**</ins> $p$-group $G$가 유한집합 $E$ 위에 act한다 하고, 이 action의 fixed point들의 모임

$$E^G=\{x\in E\mid g\cdot x=x\text{ for all $g\in G$}\}$$

을 생각하자. 그럼

$$\lvert E^G\rvert\equiv\lvert E\rvert\pmod{p}$$

이 성립한다.

</div>
<details class="proof" markdown="1">
<summary>증명</summary>

즉, 집합 $E\setminus E^G$의 크기가 $p$의 배수임을 보여야 한다. 그런데 $E\setminus E^G$는 그 크기가 $1$보다 큰 (disjoint한) $G$-orbit들의 합집합이고, 이들 각각의 orbit은 [\[대수적 구조\] §군의 작용, ⁋정리 14](/ko/math/algebraic_structures/group_actions#thm14)에 의하여 그 크기가 $p$의 거듭제곱이므로 이것이 성립한다. 

</details>

특별히 $E=G$ 위에 $G$가 inner automorphism으로 act하는 경우를 생각하면 $E^G$는 정확하게 $G$의 center이므로, [보조정리 2](#lem2)에 의하여 $p$-group $G$의 center $C(G)$는 trivial group이 아님을 알 수 있다. 

<div class="proposition" markdown="1">

<ins id="thm3">**정리 3**</ins> 크기 $p^r$의 $p$-group $G$에 대하여, $G$의 subgroup들의 series 

$$G=G_1\supset G_2\supset\cdots G_{n+1}=\{e\}$$

가 존재하여, $[G, G_k]\subseteq G_{k+1}$이 모든 $k$에 대해 성립하고, $G_k/G_{k+1}$이 order $p$의 cyclic group이도록 할 수 있다. 

</div>
<details class="proof" markdown="1">
<summary>증명</summary>

$G$의 크기에 대한 귀납법으로 증명한다. 우선 $G=\\{e\\}$인 경우는 증명할 것이 없다. 이제 $\lvert G\rvert=p^r$보다 작은 모든 $p$-group에서 주어진 주장이 성립한다 하고, $\lvert G\rvert=p^r$인 경우를 증명하자. 앞선 논증으로부터 $C(G)\neq\\{e\\}$이므로, 적당한 $x\in C(G)$가 존재하여 그 order가 $p^s$ ($1\leq s\leq r$)이도록 할 수 있다. 

이제 원소 $x^{p^{s-1}}$로 생성되는 $C(G)$의 subgroup $H$를 생각하면, $G'=G/H$는 그 크기가 $p^{r-1}$인 $p$-group이므로 귀납적 가정에 의하여 주어진 조건을 만족하는 subgroup들의 series가 존재하며, 이제 이를 canonical projection $p: G \rightarrow G'$의 inverse image로 보낸 것이 원하는 조건을 만족한다. 

</details>