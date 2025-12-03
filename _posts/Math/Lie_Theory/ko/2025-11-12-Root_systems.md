---

title: "근계"
excerpt: ""

categories: [Math / Lie Theory]
permalink: /ko/math/Lie_theory/root_systems
header:
    overlay_image: /assets/images/Math/Lie_Theory/Root_systems.png
    overlay_filter: 0.5
sidebar: 
    nav: "Lie_theory-ko"

date: 2025-11-12
last_modified_at: 2025-11-12
weight: 2

---

## Maximal torus

이전 글에서 우리는 abelian Lie group의 classification을 살펴보았다. 이번 글에서 우리는 이를 활용하여 임의의 compact connected Lie group $G$의 구조를 살펴본다. 

우선 임의의 torus $T^k\cong \mathbb{R}^k/\mathbb{Z}^k$를 생각하자. 그럼 $\mathbb{Q}$-linearly independent인 실수들 $t_1,\ldots, t_k$에 대하여, 벡터 $(t_1,\ldots t_k)$가 torus $T^k$를 *generate*한다 말한다. 이는 간단히 $k=2$인 경우를 생각해보면 직관적인데, 가령 $\mathbb{R}^2$의 한 벡터 $(1,\sqrt{2})$ 방향의 직선을 그은 뒤 $T^2\cong\mathbb{R}^2/\mathbb{Z}^2$에서의 image를 보면 이 직선은 시작했던 점으로는 돌아오지 않으며 $T^2$를 거의 덮을 것이기 때문이다. 엄밀한 정의는 다음과 같다. 

<div class="definition" markdown="1">

<ins id="def1">**정의 1**</ins> Torus $T$의 원소 $t\in T$가 $T$의 *generator*라는 것은 $\langle t\rangle$이 $T$에서 dense subgroup인 것이다. 

</div>

이제 다음을 정의한다. 

<div class="definition" markdown="1">

<ins id="def2">**정의 2**</ins> Compact connected Lie group $G$에 대하여, $G$의 subgroup $T$가 *maximal torus*라는 것은 $T$가 torus이고, $T\subsetneq T' \subset G$를 만족하는 torus $T'$가 존재하지 않는 것이다. Maximal torus $T$와 그 normalizer

$$N=N(T)=\{g\in G\mid gTg^{-1}=T\}$$

에 대하여, $W=N/T$를 $G$의 *Weyl group*이라 부른다. 

</div>

정의에 의해 Weyl group은 $T$의 선택에 의존하지만 우리는 곧 maximal torus들이 서로 conjugate임을 보일 것이므로 서로 다른 $T$의 선택 또한 isomorphic한 Weyl group을 준다. 한편 torus $T$의 generator $t$를 생각하고 다음의 연속함수

$$G\rightarrow G;\qquad g\mapsto gtg^{-1}$$

를 생각하면, $N$은 정확하게 이 map에 대한 $T$의 preimage이며 따라서 compact이다. 한편, 그 정의에 의해 $N$은 torus $T$ 위에 다음의 action

$$N\times T \rightarrow T;\qquad (n,t)\mapsto ntn^{-1}$$

을 준다. 그런데 $T$는 abelian이므로, 이 action은 결과적으로 다음의 Weyl group action 

$$W\times T \rightarrow T; \qquad (nT, t)\mapsto ntn^{-1}$$

을 주게 된다. 한편 torus의 automorphism은 각 lattice point가 어디로 가는지에 의해 결정되므로, 이를 고려하면 $N$의 action은 다음의 homomorphism

$$N\rightarrow\Aut(T)\cong \GL(k;\mathbb{Z})$$

을 주게 된다. 이제 $N$의 identity component $N_0$을 생각하자. 그럼 $\GL(k;\mathbb{Z})$은 
discrete group이므로 $N_0$는 통째로 $\id\in \GL(k;\mathbb{Z})$로 옮겨져야 한다. 즉 $N_0$은 $T$ 위에 trivial action을 정의한다. 그럼 임의의 one-parameter subgroup $\gamma: \mathbb{R}\rightarrow N_0$에 대하여, $T$의 maximality로부터 $\gamma(\mathbb{R})T=T$이므로 특히 $\gamma(\mathbb{R})\subset T$이다. 이제 $N_0$의 원점에서의 Lie algebra들의 exponential map들 (즉 one-parameter subgroup들)은 $N_0$를 생성하므로 반드시 $T=N_0$이어야 한다. 즉, $W=N/N_0$이다. 그런데 $N$이 compact이므로 $W$도 compact이고, 따라서 $W$는 유한집합이다. 

이제 Fubini-type 정리

$$\int_G f(g)\mathop{dg}=\int_{G/H}\left(\int_H f(gh)\mathop{dh}\right)\mathop{d(gH)}$$

를 다음 함수

$$\psi:G/T \times T \rightarrow G; \qquad (gT, t)\mapsto gtg^{-1}$$

에 적용하면, $\psi$의 mapping degree를 계산할 수 있고, mapping degree는 일반적으로 regular value의 preimage의 (sign을 포함한) counting으로 주어지므로 이를 활용하면 다음을 얻는다. 

<div class="proposition" markdown="1">

<ins id="lem3">**보조정리 3 (Weyl)**</ins> Compact connected Lie group $G$와 maximal torus $T$, 그리고 위의 함수

$$\psi: G/T\times T \rightarrow G\qquad (gT, t)\mapsto gtg^{-1}$$

에 대하여 $\deg(\psi)=\lvert W\rvert$이 성립한다. 

</div>

특히 $\psi$는 surjective이며, 따라서 다음을 얻는다. 

<div class="proposition" markdown="1">

<ins id="thm4">**정리 4**</ins> 임의의 compact connected Lie group $G$의 두 maximal torus $T,T'$는 항상 conjugate이며, 임의의 $G$의 원소는 어떤 maximal torus에 포함되어 있다. 

</div>

바꾸어 말하자면, 임의의 $G$의 element는, 고정된 maximal torus $T$에 대하여, 적당한 $t\in T$의 conjugate으로 쓸 수 있다. 뿐만 아니라 [보조정리 3](#lem3)에서 $\psi$를 적당히 대각화하면 다음의 따름정리 또한 얻어진다. 

<div class="proposition" markdown="1">

<ins id="cor5">**따름정리 5 (Weyl integration formula)**</ins> 다음의 식

$$\lvert W\rvert\int_G f(g)\mathop{dg}=\int_T\left(\det(1_{G/T}-\Ad_{G/T}(t^{-1}))\int_G f(gtg^{-1})\mathop{dg}\right)\mathop{dt}$$

이 성립한다. 

</div>

위의 따름정리 또한 중요한 결과지만, 어쨌든 이 글의 흐름에서 중요한 것은 [정리 4](#thm4)이므로 자세한 설명은 생략하기로 한다. 

Compact connected Lie group $G$에 대하여, 임의의 abelian Lie subgroup은 torus인 것을 알고 있다. 이에 우리는 대략적으로 maximal torus를 $G$의 maximal abelian subgroup과 같은 것으로 생각하지만, 이 둘이 정확히 같은 것은 아니다. 더 구체적으로 임의의 maximal torus는 maximal abelian subgroup이지만, 모든 maximal abelian subgroup이 torus인 것은 아니다. 그 대신, Weyl group action $W\times T \rightarrow T$를 생각하면 $T$가 abelian이므로 이 action은 *effective* action이 된다. 만일 어떠한 $gT\in W$가 모든 $t\in T$에 대하여 

$$t=(gT)\cdot t=gtg^{-1}$$

을 만족한다면, $g\in Z(T)$여야 하고 $T$의 maximality에 의하여 $Z(T)=T$이기 때문이다. 다음 보조정리는 orbit space $T/W$를 구체적으로 묘사한다. 

<div class="proposition" markdown="1">

<ins id="lem6">**보조정리 6**</ins> Maximal torus의 두 원소가 $G$에서 conjugate인 것과 이들이 Weyl group action의 같은 orbit에 속하는 것이 동치이다. 

</div>
<details class="proof" markdown="1">
<summary>증명</summary>

Maximal torus $T$를 고정하고, $T$의 두 원소 $x,y$가 서로 conjugate이라 하자. 즉 적당한 $g\in G$에 대하여 $gxg^{-1}=y$이다. 이제 $T$와 $gTg^{-1}$을 비교하면 이들은 $y$의 centralizer $Z(y)$의 maximal torus이다. 따라서 $T=h(gTg^{-1})h^{-1}$이도록 하는 $h\in Z(y)$가 존재하며, 이로부터 $(hg)x(hg)^{-1}-hyh^{-1}=y$이므로 $(hgT)\cdot x=y$이다. 

</details>

이제 임의의 $G$의 임의의 원소는 적당한 maximal torus에 포함되어 있고, 임의의 maximal torus는 다른 maximal torus와 conjugate이므로, 임의의 $x\in G$는 항상 고정된 maximal torus $T$와 적당한 $g\in G$에 대하여 $x=gtg^{-1}$으로 쓸 수 있다. 바꾸어 말하자면, $G$의 임의의 conjugacy class $[x]\in\Conj(G)$가 주어질 때마다 여기에 속한 $t\in T$를 대응시켜줄 수 있다. 이 대응을 사용하여, 임의의 conjugacy class $[x]$를 받아 $tW\in T/W$를 대응시키는 함수를 생각하자. 

<div class="proposition" markdown="1">

<ins id="prop7">**명제 7**</ins> 위의 함수는 잘 정의되며, $T/W$와 $\Conj(G)$ 사이의 일대일대응을 정의한다. 

</div>
<details class="proof" markdown="1">
<summary>증명</summary>

이 함수가 잘 정의된다는 것은 위의 명제에 의하여 자명하다. 이제 이 함수가 단사임을 보이자. 즉 두 class $[x_1]$, $[x_2]$가 같은 $W$-orbit $t_1W=t_2W$으로 옮겨진다 하자. 즉 $t_1, t_2$는 $G$에서 conjugate하며, 이들 각각은 $x_1, x_2$와 conjugate이므로 원래의 class $[x_1], [x_2]$도 서로 같아야 한다. 이 함수가 전사라는 것은 그냥 임의의 $t\in T$에 대하여 $t$의 conjugacy class가 $tW$으로 옯겨지므로 자명하다. 

</details>

조금 더 fancy한 언어를 사용하면 이는 다음과 같다. Lie group $G$ 위에 conjugate action을 생각하고 이를 통해 quotient topology를 주어 $G$의 conjugacy class들의 공간 $\Conj(G)$를 생각하자. 그럼 $G$ 위의 class function은 단순히 $\Conj(G)$ 위에서의 연속함수이다. 이제 이를 $T$로 제한하면 다음의 isomorphism

$$C^0(\Conj(G))\cong C^0(T)^W$$

이 주어지게 된다. 

## Torus action

우리는 $G$에 대한 정보가 $G$의 representation에 담겨있다는 것을 알고, 이것은 다시 그 representation의 character로부터 결정된다는 것을 안다. 임의의 representation $\rho:G\rightarrow \Aut(V)$에 대하여, 그 character $\chi_\rho$는 $G$의 conjugacy class 위에서 상수함수이며, 즉 class function이며, 위의 논의에서 우리는 $G$ 위에 정의된 class function들을 보는 것이 정확하게 $T$ 위에 정의된 $W$-invariant function을 보는 것과 같다는 것을 안다. 따라서 우리의 주된 관심사는 위와 같이 $W$-action이 주어진 manifold $T$를 살펴보는 것이 된다. 

이를 위해 우리는 우선 $T$의 representation에 대해 살펴본다. 임의의 torus $T$에 대하여, $T$는 abelian이고 따라서 $T$의 임의의 irreducible representation은 $1$차원이다. 바꾸어 말하자면, 임의의 representation $T\rightarrow\Aut(V)$가 주어졌다 하면, 이를 irreducible subrepresentation으로 분해하여 다음의 식

$$V=\bigoplus_{i}V_i$$

을 얻고, 각각의 $V_i$는 $1$차원이다. 이 때 각각의 $V_i$ 위에서는 $T$의 action이 훨씬 명시적인데, 이는 $V_i$가 $1$차원인 것으로부터 $\Aut(V_i)\cong \mathbb{C}^\times$이므로, torus action은 continuous homomorphism $\lambda_i:T \rightarrow \Aut(V_i)\cong \mathbb{C}^\times$로 주어지기 때문이다. 뿐만 아니라 이것이 irreducible이므로 $\lvert\lambda_i\rvert=1$이고 따라서 각각의 $V_i$ 위에서 torus action은 

$$t\cdot v=\lambda_i(t)v,\qquad \lambda_i(t)\in S^1\subset\mathbb{C}^\times$$

으로 주어지며, 이제 서로 같은 representation $\lambda$들을 갖는 성분들을 한데 모아 이를 $V_\lambda$라 하면, 우리는 *weight space decomposition* $V=\bigoplus V_\lambda$를 얻는다. 지금까지의 논의를 엄밀하게 정의로 적으면 다음과 같다. 

<div class="definition" markdown="1">

<ins id="def8">**정의 8**</ins> Torus $T$와 complex $T$-module $V$가 주어졌다 하자. Irreducible character $\lambda: T \rightarrow S^1$이 $V$의 *weight*이라는 것은 다음 집합

$$V_\lambda=\left\{v\in V\mid t\cdot v=\lambda(t)v\text{ for all $t\in T$}\right\}$$

이 nontrivial인 것이다. 이 때, $V_\lambda$를 $\lambda$의 *weight space*라 하며, decomposition

$$V=\bigoplus_\lambda V_\lambda$$

을 $V$의 *weight decomposition*이라 부른다. 

</div>

임의의 