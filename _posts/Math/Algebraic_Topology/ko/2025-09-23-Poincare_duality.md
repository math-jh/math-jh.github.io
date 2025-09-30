---

title: "푸앵카레 쌍대성"
excerpt: ""

categories: [Math / Algebraic Topology]
permalink: /ko/math/algebraic_topology/Poincare_duality
header:
    overlay_image: /assets/images/Math/Algebraic_Topology/Poincare_duality.png
    overlay_filter: 0.5
sidebar: 
    nav: "algebraic_topology-ko"

date: 2025-09-23
last_modified_at: 2025-09-23
weight: 9

---

이번 글에서 우리는 대수적 위상수학의 아름다운 정리인 푸앵카레 쌍대성에 대해 다룬다. 이전 글에서 언급한 것과 같이, 푸앵카레 쌍대성은 호몰로지와 코호몰로지 사이의 쌍대성을 보여준다. 우리가 이미 살펴본 universal coefficient theorem ([§코호몰로지, ⁋정리 5](/ko/math/algebraic_topology/cohomology#thm65))의 경우, $C^\bullet(X;A)$를 $C_\bullet(X;A)$의 dual로서 정의했을 때 어느정도 예상 가능한 결과였지만 푸앵카레 쌍대성은 보다 더 기하학적인 의미를 가지고 있다. 

## 방향

푸앵카레 쌍대성을 정의하기 위해서는 우선 방향의 개념을 정의해야 한다. 이는 topological manifold ([§위상다양체, ⁋정의 2](/ko/math/algebraic_topology/topological_manifolds#def2)) 위에서 정의되는 개념으로, 이번 글에서는 별다른 말이 없다면 임의의 manifold는 *connected*인 것으로 가정한다. 

임의의 topological manifold $M$ of dimension $m$과 한 점 $x\in M$에 대하여, $M$은 locally Euclidean이므로 $x$의 적당한 열린근방 $U$와 homeomorphism $\phi: U \rightarrow \mathbb{R}^m$이 존재한다. 이 때 쌍 $(U,\phi)$를 *Euclidean chart*라 부른다. 그럼 [§호몰로지의 계산, ⁋정리 2](/ko/math/algebraic_topology/computation_of_homology#thm2)에 의하여, 

$$H_n(M,M\setminus\{x\})\cong H_n(U,U\setminus\{\phi(x)\})\cong H_n(\mathbb{R}^m, \mathbb{R}^m\setminus\{0\})$$

이 성립한다. 한편 $\mathbb{R}^m\setminus\{0\}$은 $S^{m-1}$으로 deformation retract하고, 따라서 relative homology long exact sequence에 의하여 

$$H_k(M,M\setminus\{x\})$$

들은 (1) $k\neq m$인 경우 모두 trivial group이고, (2) $k=m$인 경우 모두 $\mathbb{Z}$와 isomorphic하다. 한편, $\mathbb{Z}$에서 $\mathbb{Z}$로의 isomorphism은 정의역의 generaor $1$이 치역의 $+1$로 가는지, 혹은 치역의 $-1$로 가는지에 따라 두 가지의 경우가 있다. 우리는 이 isomorphism의 선택을 $M$의 방향을 주는 것으로 생각할 것이다. 

이를 위해서는 우선 reference 역할을 할 $\mathbb{Z}$가 필요하다. 이를 위해 $M$ 위에 constant presheaf $\underline{\mathbb{Z}}$를 하나 고정하자. ([\[위상수학\] §준층, ⁋예시 6](/ko/math/topology/presheaves#ex6)) 그럼 각각의 $x\in M$에 대하여 그 stalk $\underline{\mathbb{Z}}_x$은 generator $1$이 consistent한 방식으로 선택되어 있는 것으로 생각할 수 있고, 따라서 각각의 $x$에 대하여 isomorphism

$$\Iso_\mathbb{Z}(H_m(M, M\setminus\{x\}), \underline{\mathbb{Z}}_x)$$

을 선택하는 것은 각각의 $x$에서 $M$이 양의 방향인지, 음의 방향인지를 택하는 것과 같다. 

<div class="definition" markdown="1">

<ins id="def1">**정의 1**</ins> Topological manifold $M$ of dimension $m$에 대하여, 점 $x$에서의 *local orientation*은 $\Iso_\mathbb{Z}(H_m(M,M\setminus\\{x\\}), \underline{\mathbb{Z}}_x)$의 원소를 택하는 것으로 주어진다.

</div>

이제 각각의 열린집합 $U$에 대하여 

$$\or_M(U)=\prod_{x\in U}\Iso_\mathbb{Z}(H_m(M,M\setminus\{x\}), \underline{\mathbb{Z}}_x)$$

으로 정의하고, $U\subseteq V$일 때마다 $\rho_{VU}:\or_M(V)\rightarrow \or_M(U)$를 canonical projection으로 정의하자. ([\[집합론\] §곱집합의 성질, ⁋정의 1](/ko/math/set_theory/property_of_products#def1)) 그럼 $\or_M$은 $M$ 위에 정의된 presheaf가 되며 ([\[위상수학\] §준층, ⁋정의 4](/ko/math/topology/presheaves#def4)), 각각의 $p\in M$에 대하여 $\or_M$의 점 $x$에서의 stalk $\or_{M,x}$는 $\\{\pm 1\\}$이 된다. ([\[위상수학\] §준층, ⁋정의 9](/ko/math/topology/presheaves#def9))

이제 $\or_M$의 sheafification $\Or_M$을 $M$의 *orientation sheaf*라 부른다. 그럼 [\[위상수학\] §준층, ⁋정의 9](/ko/math/topology/presheaves#def9) 이후에 정의한 étalé space $\Spe(\or_M)$을 생각하면, $\Or_M$은 canonical projection $p:\Spe(\or_M)\rightarrow M$의 section들의 sheaf이다. 

<div class="definition" markdown="1">

<ins id="def2">**정의 2**</ins> 위에서 정의한 étalé space $\Spe(\or_M)$을 $M$의 *orientation double cover*라 부르고, global section $M \rightarrow \Spe(\or_M)$을 *global orientation*이라 부른다. $M$이 *orientable*하다는 것은 global orientation이 존재하는 것이다.

</div>

그럼 그 이름과 같이 $\Spe(\or_M)$은 $M$의 covering space이며, 뿐만 아니라 임의의 $x\in M$에 대하여, $x$의 chart $U$를 생각하면 canonical projection $p:\Spe(\or_M)\rightarrow M$에 의한 $U$의 preimage $p^{-1}(U)$가 $U$와 homeomorphic한 두 개의 disjoint open subset으로 나타난다. 

그러나 이것이 orientation double cover $\Spe(\or_M)$이 위상공간으로서 $M\times\\{\pm 1\\}$과 homeomorphic하다는 것은 아니다. 이를 직관적으로 확인하기 위해서는 뫼비우스 띠를 생각하면 되는데, 뫼비우스 띠의 한 점 $x$에서 바깥쪽을 향하는 화살표를 그린 후, 뫼비우스 띠를 따라 한 바퀴 돌아오면 이 화살표가 반대방향을 가리키고 있을 것이다. 즉 뫼비우스 띠 $M$의 orientation double cover $\Spe(\or_M)$를 생각하면 점 $x$의 fiber에 해당하는 두 점을 잇는 path가 존재할 것이며, 이는 두 개의 component를 가질 $M\times\\{\pm 1\\}$로서는 불가능한 일이기 때문이다. 이와 정확히 같은 이유로 global section $M \rightarrow \Spe(\or_M)$이 존재할 수 없으며, 이를 일반화하면 다음의 명제를 얻는다. 

<div class="proposition" markdown="1">

<ins id="prop3">**명제 3**</ins> (Connected) topological manifold $M$에 대하여, 다음이 동치이다. 

1. $M$이 orientable이다.
2. $\Spe(\or_M)$이 두 개의 component를 갖는다. 
3. $\pi_1(M)$이 index 2 subgroup을 갖지 않는다. 

</div>

그런데 우리는 이미 호몰로지와 코호몰로지를 다룰 때 $\mathbb{Z}$-module뿐 아니라, 일반적인 $A$-module로 확장했으므로 위의 논증 또한 일반적인 $A$-module에 대해 확장할 수 있다. 이를 위해 우선 [\[대수적 위상수학\] §코호몰로지, ⁋명제 1](/ko/math/algebraic_topology/cohomology#prop1)의 relative homology 버전을 생각하면, 다음의 (non-canonical) isomorphism

$$H_k(M, M\setminus\{x\};A)\cong H_k(M,M\setminus\{x\})\otimes_\mathbb{Z}A\oplus\Tor_1^\mathbb{Z}(H_{k-1}(M, M\setminus\{x\}), A)$$

가 존재하는 것을 관찰하자. 그런데 $H_k(M,M\setminus \\{x\\})$는 $k\neq m$인 경우는 항상 trivial group이므로, 이 isomorphism으로부터 우리는

$$H_m(M,M\setminus \{x\};A)\cong H_m(M,M\setminus\{x\})\otimes_\mathbb{Z}A\cong A$$

임을 안다. 따라서 위의 논증에서 등장하는 $\mathbb{Z}$를 모두 $A$로 바꾸어도 말이 될 것이며, 특히 우리는 $A$-orientation들의 presheaf

$$\or_M^A(U)=\prod_{x\in U}\Iso_A(H_m(M,M\setminus\{x\};A), \underline{A}_x)$$

그리고 이로부터 정의되는 global $A$-orientation의 개념을 얻을 것이다. 

이 정의에서 [명제 3](#prop3)과 같은 결과를 도출하기 위해 [§피복공간, ⁋정리 11](/ko/math/algebraic_topology/covering_spaces#thm11)를 다시 살펴보자. 우리는 각각의 covering space $p:E \rightarrow M$에 대하여, fiber $p^{-1}(x)$ 위에 monodromy functor가 정의하는 $\pi_1(M,x)$-action을 생각하였고, 이는 곧 group homomorphism $\pi_1(M,x)\rightarrow \Aut(p^{-1}(x))$를 생각하는 것과 같았다. 그렇다면 covering space $p:\Spe(\or_M)\rightarrow M$에 대하여 $\pi_1(M,x)$-action은 어떻게 정의되는지를 살펴보아야 하는데, 이 때 fiber $p^{-1}(x)$는 stalk $\mathbb{Z}$의 automorphism 

$$\Iso_\mathbb{Z}(\mathbb{Z},\mathbb{Z})\cong \mathbb{Z}^\times\cong \{\pm 1\}$$

으로부터 정의되는 것이고 따라서 $\pi_1(M,x)$-action은 정확하게 group homomorphism $\pi_1(M,x)\rightarrow \mathbb{Z}^\times$로 생각할 수 있다. 그럼 $A$에서 $A$로의 $A$-module isomorphism은 정확히 $A$의 unit group $A^\times$의 원소와 대응되므로, 이는 결과적으로 group homomorphism $\pi_1(M,x)\rightarrow A^\times$를 살펴보는 것과 같다. 즉 [명제 3](#prop3)은 다음과 같이 일반화할 수 있다.

<div class="proposition" markdown="1">

<ins id="prop4">**명제 4**</ins>  (Connected) topological manifold $M$에 대하여, 다음이 동치이다. 

1. $M$이 $A$-orientable이다.
2. $\Spe(\or_M^A)$이 trivial covering $M\times \lvert A^\times\rvert$이다. 
3. Monodromy representation $\pi_1(M)\rightarrow A^\times$는 trivial이다. 

</div>

이러한 일반화에서 가장 특기할만한 경우는 $A=\mathbb{Z}/2$일 때이다. 이 경우, $A$의 unit은 $-1=1$ 뿐이므로 orientation을 지정하는 방법은 유일하고, 따라서 임의의 manifold는 항상 $\mathbb{Z}/2$-orientable이다.

## 기본류

이제 우리는 global ($A$-)orientation의 존재성에 대해 살펴본다. 즉, 모든 $x\in X$에 대하여 local orientation들 $s_x$이 주어졌을 때, 적당한 global section $s:M\rightarrow \Spe(\or_M^A)$이 존재하여 $s(x)=(x,s_x)$이도록 할 수 있는지를 살펴볼 것이다. 

한편 우리는 다음의 canonical homomorphism

$$H_m(M; A)\rightarrow H_m(M,M\setminus\{x\};A)\tag{1}$$

을 통해, 임의의 top homology class $\alpha\in H_m(M;A)$는 local homology group의 원소 $\alpha_x\in H_m(M,M\setminus\\{x\\};A)$를 정의하는 것을 안다. 그렇다면 자연스러운 질문 중 하나는 각각의 $x\in S_x$마다 주어진 local orientation $s_x$들을 $A^\times$의 원소로 보아 이를 $H_m(M,M\setminus\{x\};A)$의 원소로 취급했을 때, 모든 $x\in X$에 대하여 $\alpha\in H_m(M;A)$의 $H_m(M,M\setminus\\{x\\};A)$에서의 image가 $s_x$이도록 할 수 있는 $\alpha$가 존재하는지의 여부일 것이다. 

위의 두 문단은 푸앵카레 쌍대성이 어떠한 꼴인지를 보여준다. Global section $s:M \rightarrow \Spe(\or_M^A)$는 본질적으로 $M$ 전체 위에 정의된 함수로서, $0$번째 cohomology에 해당하는 개념이다. 반면 $\alpha\in H_m(M;A)$는 $m$번째 homology의 원소이다. 푸앵카레 쌍대성은 이들 두 개념이 동치라는 것과, 더 일반적으로, $k$번째 cohomology와 $n-k$번째 homology 사이의 duality를 보여준다.

이제 남은 글에서 우리가 해야 할 것은 크게 두 가지이다. 

1. Canonical homomorphism (1)의 lifting이 global orientation을 정의하고, 그 반대도 성립한다는 것을 보인다.
2. Global orientation $M \rightarrow \Spe(\or_M^A)$가 존재하는 *sheaf cohomology*를 정의한다.

푸앵카레 쌍대성의 핵심적인 내용은 모두 첫째 단계에 담겨있는 것이며, 둘째 단계는 이를 현명하게 표현할 수 있는 언어를 배우는 것에 가깝다. 따라서 우리는 우선 첫째 단계부터 시작한다. 이는 다음의 보조정리에 의해 얻어진다.

<div class="proposition" markdown="1">

<ins id="lem5">**보조정리 5**</ins> Topological manifold $M$ of dimension $m$을 고정하자. $M$의 임의의 compact subset $C$에 대하여 다음이 성립한다.

1. 임의의 section $s:M \rightarrow \Spe(\or_M^A)$가 주어질 때마다, 적당한 homology class 
    
    $$\alpha_C\in H_m(M,M\setminus C;A)$$

    이 유일하게 존재하여, 임의의 $x\in C$마다 canonical homomorphism

    $$H_m(M,M\setminus C;A)\rightarrow H_m(M,M\setminus\{x\};A)$$

    에 의한 $\alpha_C$의 image가 $s_x$이도록 할 수 있다. 
2. 모든 $i>n$에 대해 $H_i(M, M\setminus C;A)=0$이다.

</div>
<details class="proof" markdown="1">
<summary>증명</summary>

우선 임의의 compact set $C_1,C_2$, 그리고 이들의 교집합 $C_1\cap C_2$에 대해 이 명제가 성립한다면 $C_1\cup C_2$에 대해서도 명제가 성립함을 보이자. 이는 Mayer-Vietoris sequence

$$\cdots \rightarrow H_k(M,M\setminus (C_1\cup C_2); A)\rightarrow H_k(M,M\setminus C_1;A)\oplus H_k(M,M\setminus C_2;A)\rightarrow H_k(M, M\setminus (C_1\cap C_2);A)\rightarrow\cdots\tag{2}$$

에서, $k>m$에 대해서는 귀납적 가정에 의해 

$$H_k(M,M\setminus C_1;A)=H_k(M,M\setminus C_2;A)=H_k(M,M\setminus(C_1\cap C_2);A)=0$$

이므로 $H_k(M,M\setminus (C_1\cup C_2);A)$ 또한 $0$이어야 하고, 이로부터 둘째 주장이 성립한다. 

첫째 주장을 보이기 위해 section $s:M \rightarrow \Spe(\or_M^A)$이 주어졌다 하자. 귀납적 가정에 의해 이들은 $C_1,C_2,C_1\cap C_2$에 대해서는 lifting이 가능하므로, 이들을 이어붙여 $C_1\cup C_2$에 대하여 class $\alpha_{C_1\cup C_2}$를 만들어야 한다. 이들 $\alpha_{C_1},\alpha_{C_2},\alpha_{C_1\cap C_2}$의 유일성에 의하여 $\alpha_{C_1}$과 $\alpha_{C_2}$는 모두 $\alpha_{C_1\cap C_2}$에서 같은 원소가 되어야 하므로, (2)에서 원소 

$$(\alpha_{C_1},-\alpha_{C_2})\in H_m(M,M\setminus C_1;A)\oplus H_m(M,M\setminus C_2;A)$$

를 생각하면 이 원소는 $H_m(M,M\setminus C_1;A)\oplus H_m(M,M\setminus C_2;A)\rightarrow H_m(M, M\setminus (C_1\cap C_2);A)$의 kernel에 속하고, 따라서 $H_m(M,M\setminus (C_1\cup C_2);A)$의 원소를 택할 수 있고 유일성은

$$0=H_{m+1}(M,M\setminus (C_1\cap C_2);A)\rightarrow H_m(M,M\setminus (C_1\cup C_2))\rightarrow H_m(M,M\setminus C_1;A)\oplus H_m(M,M\setminus C_2;A)$$

의 injectivity로부터 나온다. 

이제 귀납법의 기초단계를 위해서는 $M=\mathbb{R}^m$이고 $A$가 convex compact subset인 경우를 생각하면 충분하다. 임의의 manifold $M$의 compact set을 Euclidean chart로 덮은 후, compactness를 사용하면 $M=\mathbb{R}^m$으로 가정해도 충분하며 $\mathbb{R}^m$의 open ball들의 basis를 사용하고 다시 compactness를 사용하면 $A$가 convex임을 추가로 가정해도 되기 때문이다. 그럼 이 단계에서 두 공간 $\mathbb{R}^m\setminus A$와 $\mathbb{R}^m\setminus \\{x\\}$가 모두 같은 공간 $S^{m-1}$로 deformation retract하므로 isomorphism이 되고, 이로부터 증명이 끝난다. 

</details>

이 증명에서 compactness는 Mayer-Vietoris sequence를 사용하여 귀납적인 방식으로 $\alpha$를 구성할 때, 이 귀납적인 과정이 유한한 단계에서 끝나도록 하려면 반드시 필요하다. 실제로 compactness가 빠질 경우 푸앵카레 쌍대성은 다소 다른 형태를 띄게 되는데, 이를 공통된 식으로 표현하기 위해 도입해야 하는 것이 sheaf cohomology의 언어이다. 

어쨌든 위의 [보조정리 5](#lem5)에 의하여, 만일 $M$이 compact topological manifold of dimension $M$이라면, $C=M$으로 두어 다음의 정리를 얻는다.

<div class="proposition" markdown="1">

<ins id="thm6">**정리 6**</ins> Compact connected topological manifold $M$ of dimension $m$이 주어졌다 하자. 그럼 orientation sheaf $\or_M^A$이 주어질 때마다 적당한 class $[M]\in H_m(M;A)$이 유일하게 존재하여 canonical homomorphism (1)에 의한 $[M]$의 image가 $s_x$와 일치하도록 할 수 있다. 

</div>

그럼 [보조정리 5](#lem5)에 의하여 $H_m(M;A)$는 $[M]$에 의해 생성되는 free $A$-module of rank 1이며, 서로 다른 global orientation의 선택은 서로 다른 $H_m(M;A)$의 generator의 선택에 대응된다. 

<div class="definition" markdown="1">

<ins id="def7">**정의 7**</ins> 위의 [정리 6](#thm6)에서 정의한 $[M]$을 global orientation $s$가 정의하는 $M$의 *fundamental class<sub>기본류</sub>*라 부른다. 

</div>

뿐만 아니라, 만일 [정리 6](#thm6)의 조건을 만족하는 homology class $[M]$이 존재한다면, 이로부터 global section $s:M \rightarrow \Spe(\or_M^A)$이 주어진다는 것을 안다. 

## 푸앵카레 쌍대성

이제 적어도 주어진 manifold가 $A$-orientable일 경우의 푸앵카레 정리를 증명할 수 있다. 

증명 적기

## 층 코호몰로지와 체흐 코호몰로지

fundamental class 존재성 중요한거 강조

한편, 위에서 지적했듯 [보조정리 5](#lem5)의 증명에서 compactness는 필수적이다. 실제로 non-compact manifold인 $\mathbb{R}^m$을 생각해보면 $m$번째 homology group이 $0$이므로 여기에서 fundamental class를 택할 여지가 없다. 유사하게 우리가 알고 있는 non-($\mathbb{Z}$-)orientable manifold인 뫼비우스 띠를 생각해보면, 어렵지 않게 top homology group이 $0$임을 알 수 있다. 이들 두 경우에 fundamental class가 존재하지 않는 이유는 다소 다른데, sheaf cohomology는 non-orientable인 경우를 다루는데에 특히 도움을 준다. 

기본적인 아이디어는 non-orientability는 $\Spe(\or_M^A)$의 nontrivial한 monodromy에 의해 생기게 된다는 것이다. 그런데 covering space의 lifting property를 생각하면, 충분히 local한 범위에서는 nontrivial monodromy가 별 영향을 주지 않으므로, global section $M \rightarrow \Spe(\or_M^A)$ 뿐만 아니라 local section들을 따로따로 보면 정보를 잃지 않을 수 있을 것이다. 그리고 이러한 방식으로 데이터를 기록하는 것이 바로 sheaf이므로, sheaf cohomology가 나오는 것이 자연스럽다.

임의의 위상공간 $X$와 그 위에 정의된 sheaf $\mathscr{F}$에 대하여, global section functor 

$$\Gamma(X,-):\Sh(X,\mathcal{A})\rightarrow \mathcal{A}$$

는 left exact functor이므로, 이 functor의 right derived functor가 존재한다. 이를 직접 계산하기 위해서는 Godement resolution을 사용하는데, 이는 다음과 같이 정의된다.

위상공간 $X$와 그 위에 정의된 sheaf $\mathscr{F}$를 생각하고, étalé space $\Spe(\mathscr{F})$를 생각하자. 우리는 $\mathscr{F}$가 정확하게 $\Spe(\mathscr{F})\rightarrow X$의 continuous section들의 sheaf임을 안다. 이제 임의의 열린집합 $U$에 대하여

$$\mathscr{G}_0(U)=\prod_{x\in U}\mathscr{F}_x$$

으로 정의하자. 즉 $\mathscr{G}_0$는 $\Spe(\mathscr{F})\rightarrow X$의 (연속일 필요가 없는) 집합론적인 section들의 sheaf이다. 우리의 아이디어는, 일반적으로 local하게 정의된 함수들이 이어붙였을 때 함수가 되지 않는 경우를 inclusion $\mathscr{F}\rightarrow \mathscr{G}_0$에 의해 유도되는 다음의 sequence

$$0 \rightarrow \mathscr{F}\rightarrow \mathscr{G}_0 \rightarrow \mathscr{Q}\rightarrow 0$$

을 통해 quotient sheaf $\mathscr{Q}$에 몰아넣어버리는 것이다. 그렇다면 sheaf $\mathscr{Q}$에 대해서도 마찬가지로 

$$\mathscr{G}_1(U)=\prod_{x\in U}\mathscr{Q}_x$$

으로 정의되는 sheaf를 만들 수 있고, 이것이 다음의 *Godement resolution*

$$0 \rightarrow \mathscr{F}\rightarrow \mathscr{G}_0 \rightarrow \mathscr{G}_1\rightarrow \cdots$$

을 정의한다. 직관적으로 이는 $\Spe(\mathscr{F})$의 global section이 존재하지 못하도록 하는 부분을 $\mathscr{Q}$에, 그리고 다시 $\mathscr{Q}$의 global section이 존재하지 못하도록 하는 부븐을 $\mathscr{Q}'$에 담는 식으로 계속해서 반복하는 것이다. 이 resolution $\mathscr{G}_\bullet$은 injective resolution은 아니지만, 각각의 sheaf가 flabby (flasque) sheaf이기 때문에 이를 통해 global section functor의 right derived functor $R^i\Gamma$들을 계산할 수 있다. 

<div class="definition" markdown="1">

<ins id="def8">**정의 8**</ins> 위상공간 $X$와 그 위에 정의된 sheaf $\mathscr{F}$에 대하여, Godement resolution의 global section들의 sequence

$$0 \rightarrow \mathscr{F}(X)\rightarrow \mathscr{G}_0(X)\rightarrow \mathscr{G}_1(X)\rightarrow \cdots$$

의 $k$번째 호몰로지를 

$$H^k(X; \mathscr{F})$$

으로 적고, 이를 *sheaf cohomology*라 부른다. 

</div>

어렵지 않게 $H^0(X, \mathscr{F})=\mathscr{F}(X)$임을 알 수 있다. 

직관적으로, Godement resolution은 local data를 global하게 붙일 때의 obstruction을 무한대로 보내는 것이라 생각할 수 있다. 
 
정의/증명/적분예시/왜 터지는지/compactly supported로 업그레이드/sheaf cohomology로 업그레이드/intersection