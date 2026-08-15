---
title: "분류공간"
description: "임의의 topological group을 구조군으로 갖는 principal bundle을 정의하고, universal bundle과 classifying space를 통해 이들을 homotopy 이론으로 분류한다."
excerpt: "Principal G-bundle의 분류와 classifying space BG의 구성"

categories: [Math / Algebraic Topology]
permalink: /ko/math/algebraic_topology/classifying_spaces
sidebar: 
    nav: "algebraic_topology-ko"

date: 2026-07-07
weight: 16

---

앞선 글들에서 우리는 vector bundle을 분류하기 위해 특성류를 도입하였다. 흥미로운 것 중 하나는 이들의 존재성을 보이는 방식으로, 우리는 큰 공간 위에 정의된 어떤 *universal* bundle이 존재하여, 임의의 bundle이 이것의 pullback으로 나타날 수 있다는 것을 살펴보았다. 가령 real vector bundle의 경우, infinite real Grassmannian 위의 tautological $k$-plane bundle

$$E(\gamma^k_\infty)\rightarrow \Gr(k, \mathbb{R}^\infty)$$

이 그러한 역할을 하였으며 ([§슈티펠-휘트니 특성류, §§그라스만 다양체](/ko/math/algebraic_topology/stiefel_whitney_classes#그라스만-다양체)) complex vector bundle에서도 비슷한 construction이 존재했다. ([§벡터다발의 특성류, ⁋예시 8](/ko/math/algebraic_topology/characteristic_classes#ex8)) 한편 vector bundle의 pullback은 오직 map의 homotopy class에만 의존하므로, 고정된 공간 $B$ 위의 rank $k$ vector bundle의 isomorphism class는 이들 공간으로의 함수들의 homotopy class들의 모임 $[B, \Gr(k, \mathbb{R}^\infty)]$ (혹은 $[B, \Gr(k, \mathbb{C}^\infty)]$)이 된다. 

한편, vector bundle을 살펴보는 또 다른 관점은 이를 transition function들의 모임으로 생각하는 것이었다. 가령 임의의 vector bundle은 두 개의 trivializing open cover가 겹치는 곳에서

$$g_{ij}: U_i\cap U_j\rightarrow \GL(k;\mathbb{R})$$

를 명시해주면 되었으며, 이 관점은 예를 들어, $\GL(k;\mathbb{R})$을 $\GL^+(k;\mathbb{R})$로 바꿔주면 *oriented* vector bundle 또한 설명할 수 있다는 점에서 강력했다. 

이번 글의 목적은 이 두 관점을 이어주는 것이다. 즉 우리는 더 일반적으로, structure group이 (topological) group $G$인 경우 나타나는 *principal $G$-bundle*을 정의하고, 이러한 것들을 분류하는 공간인 *classifying space* $\B G$를 정의할 것이다. 이번 글에서 $G$는 항상 topological group을 의미하며, 별다른 언급이 없는 한 base space는 paracompact Hausdorff인 것으로 가정한다.

## Principal bundle의 정의

Vector bundle의 fiber에는 벡터공간 구조가 있었고, 그 transition function은 이 구조를 보존하는 linear automorphism, 곧 $\GL(k;\mathbb{R})$의 원소들이었다. 일반적인 구조군 $G$를 다룰 때는 fiber 자체를 $G$로 두고, transition을 $G$의 left translation으로 주는 것이 자연스럽다. 약간의 차이는 이러한 관점에서 특별한 점이 존재하지 않는다는 것으로, 하나의 chart 상에서 항등원인 fiber의 원소도 left translation을 통해 다른 chart에서는 fiber의 다른 원소로 이해된다. 즉, 이들 원소는 *$G$-torsor*들로 생각해야 하며, 이를 좌표에 의존하지 않고 기술하기 위해 우리는 total space 위의 $G$-action을 사용한다.

::: 정의 1
Topological group $G$에 대하여, fiber bundle $p:P\rightarrow X$와 그 위의 연속적인 right action $P\times G\rightarrow P$가 주어졌다 하자. 이 데이터가 *principal $G$-bundle<sub>주다발</sub>*이라는 것은 다음 세 조건이 성립하는 것이다.

1. $G$-action은 fiber를 보존한다. 즉 모든 $y\in P$와 $g\in G$에 대하여 $p(y\cdot g)=p(y)$이다.
2. 각 fiber 위에서 $G$-action은 free이고 transitive하다. 즉 임의의 $x\in X$에 대하여, 한 점 $y\in p^{-1}(x)$를 고정하면 $g\mapsto y\cdot g$가 $G$에서 $p^{-1}(x)$로의 전단사이다.
3. ($G$-equivariant local triviality) 각 $x\in X$마다 열린근방 $U$와, $U$ 위에서 $p$와 호환되는 $G$-equivariant homeomorphism $\varphi:p^{-1}(U)\rightarrow U\times G$가 존재한다. 여기서 $U\times G$ 위의 $G$-작용은 $(u,h)\cdot g=(u,hg)$로 둔다.
:::

즉, 국소적으로는 base space 위에 fiber 방향으로 $G$들을 달아주고, 그 각각의 fiber 위에 $G$가 right translation으로 작용하는 것이다. 

그럼 두 principal $G$-bundle $P,P'\rightarrow X$ 사이의 *morphism*은 $p'\circ f=p$를 만족하고 $G$-작용과 호환되는 연속함수 $f:P\rightarrow P'$를 뜻하며, 이것이 homeomorphism이면 이를 두 principal bundle 사이의 *isomorphism*이라 부른다. Local trivialization $\varphi_i:p^{-1}(U_i)\rightarrow U_i\times G$들을 고정하면, $U_i\cap U_j$ 위에서 $\varphi_i\circ\varphi_j^{-1}(u,h)=(u,g_{ij}(u)h)$를 만족하는 연속함수 $g_{ij}:U_i\cap U_j\rightarrow G$가 결정된다. 이 transition function들은 vector bundle에서와 같은 cocycle 조건

$$g_{ij}(x)g_{jk}(x)=g_{ik}(x),\qquad g_{ii}(x)=e$$

를 만족하며, 두 cocycle $(g_{ij})$와 $(g_{ij}')$이 같은 bundle을 주는 것은 연속함수 $\lambda_i:U_i\rightarrow G$들이 존재하여 $g_{ij}'=\lambda_i g_{ij}\lambda_j^{-1}$인 것과 동치이다. 따라서 open cover $\mathcal{U}=\{U_i\}$ 위에서 trivialize되는 principal $G$-bundle의 isomorphism class들은 (nonabelian) Čech cohomology $\check{H}^1(\mathcal{U};G)$로 분류되며, $G=\GL(k;\mathbb{R})$인 경우 이는 앞 글의 vector bundle 분류와 정확히 일치한다.

Vector bundle은 언제나 zero section을 가졌으나, principal bundle은 fiber가 $G$가 아니라 $G$-torsor이므로 이러한 역할을 하는 section을 잡는 것이 자명하지 않다. 실제로 다음 명제는 section의 존재 여부가 principal bundle의 자명성을 완전히 결정한다는 것을 보여준다.

::: 명제 2
Principal $G$-bundle $p:P\rightarrow X$가 trivial bundle과 isomorphic한 것은 연속적인 global section $s:X\rightarrow P$가 존재하는 것과 동치이다.
:::
::: 증명
Trivial bundle $X\times G$는 $x\mapsto(x,e)$라는 section을 가지므로, $P$가 trivial이면 isomorphism을 통해 section을 얻는다. 역으로 section $s:X\rightarrow P$가 존재한다 하고, 다음의 함수

$$\Phi:X\times G\rightarrow P,\qquad (x,g)\mapsto s(x)\cdot g$$

를 생각한다. 각 fiber 위에서 $G$-action이 simply transitive ([정의 1](#def1)의 조건 (2)) 하므로 $\Phi$를 fiber $\{x\}\times G\rightarrow p^{-1}(x)$로 제한한 것은 전단사이고, 따라서 $\Phi$는 전단사이다. $\Phi$는 정의에 의해 $p\circ\Phi=\pr_1$을 만족하고 $G$-action과 호환되므로 morphism over $X$이다. 마지막으로 $\Phi$가 homeomorphism임은 국소적으로 확인하면 되는데, trivialization $\varphi:p^{-1}(U)\rightarrow U\times G$ 위에서 $s$가 $x\mapsto(x,\sigma(x))$의 꼴로 쓰이면 ($\sigma:U\rightarrow G$ 연속) $\Phi$는 $(x,g)\mapsto(x,\sigma(x)g)$가 되어 그 역 $(x,h)\mapsto(x,\sigma(x)^{-1}h)$이 연속이기 때문이다.
:::

이 명제는 principal bundle과 vector bundle의 결정적인 차이를 드러낸다. 따라서 principal bundle과 vector bundle을 관계짓기 위해서는 이들 둘을 이어주는 대상이 필요하다.

Principal $G$-bundle이 vector bundle이 될 수 없는 이유 중 가장 단순한 것은 vector bundle의 fiber는 vector space지 group이 아니라는 데에 있다. 우리는 이를 해결하기 위해 다음을 정의한다. 

::: 정의 3
Principal $G$-bundle $p:P\rightarrow X$와, $G$가 왼쪽에서 연속적으로 작용하는 위상공간 $F$가 주어졌다 하자. 그럼 $P\times F$ 위에 $G$-action을

$$(y,f)\cdot g=(y\cdot g,\ g^{-1}\cdot f)$$

로 정의하고, 그 orbit space를 $P\times_G F=(P\times F)/G$로 적는다. 그럼 $(y,f)\mapsto p(y)$가 유도하는 morphism $P\times_G F\rightarrow X$는 fiber $F$를 갖는 fiber bundle이며, 이를 $P$의 *associated bundle<sub>수반다발</sub>*이라 부른다.
:::

직관적으로 이는 principal $G$-bundle이 <em-ko>비틀려있는</em-ko> 구조를 따라 fiber $F$를 이어붙여주는 것으로, 가령 trivial $G$-bundle $X\times G$와 fiber $F$에 이를 적용하면 trivial fiber bundle $X\times F$가 나오고, 비슷하게 약간 비틀려있는 (즉 non-trivial한) principal $G$-bundle $P$와 fiber $F$에 이를 적용하면 그로부터 얻어지는 fiber bundle은 fiber가 $F$이고, $P$에서 비틀림 데이터를 받아오는 bundle이 된다. 

가장 투명한 예시는 vector bundle이므로, 여기에서 정의를 차례차례 따라가보자. Topological group $G=\GL(k;\mathbb{R})$은 dimension $k$ real vector space $F=V$ 위에 왼쪽에서 작용한다. 또, 편의를 위해 trivial $G$-bundle $P=X\times G$가 주어졌다 하자. 그럼 우선 곱공간 $P\times F=(X\times G)\times V$ 위에 정의된 $G$-action은

$$\bigl((x,g),v\bigr)\cdot h=\bigl((x, gh),h^{-1}v\bigr)$$

이 되며, 그 orbit space는 $X\times V$에 불과하다. 이는 임의의 원소 $((x,g),v)$에 $h=g^{-1}$로의 action을 취하면

$$((x,g),v)\cdot g^{-1}=\bigl((x,e),gv\bigr)$$

이 되기 때문으로, 이 과정에서 우리는 $X\times G$의 $(x,e)$를 $X$의 원소 $x$와 identify하여, 다음의 식

$$[((x,g),v)]\mapsto(x,gv)$$

가 well-defined인 homeomorphism인 것을 사용하였다. 즉 trivial $G$-bundle에서 출발하면 associated bundle도 trivial하다.

더 일반적으로 만일 $P$가 $\{U_i\}$ 위에서 transition function $g_{ij}$로 주어지면, $P\times_G F$는 같은 $U_i$ 위에서 $F$를 fiber로 하고 transition이 $g_{ij}$의 $F$ 위에서의 작용으로 주어지는 bundle이 된다. 

이 역방향의 구성도 가능하다. Rank $n$ vector bundle $E\rightarrow X$가 주어지면, 각 $x$ 위의 fiber $E_x$의 ordered basis들, 즉 *frame* 전체로 이루어진 공간

$$\Fr(E)=\{(x,b)\mid x\in X,b\text{ an ordered basis of $E_x$}\}$$

는 ordered basis에 행렬을 오른쪽에서 곱해 기저를 바꾸는 $\GL(n;\mathbb{R})$의 작용에 대하여 principal $\GL(n;\mathbb{R})$-bundle이 되며, 이를 $E$의 *frame bundle*이라 한다. 다음 명제는 이 두 구성이 서로 역과정임을 보여준다. 

::: 명제 4
위상공간 $X$ 위에서, principal $\GL(n;\mathbb{R})$-bundle들의 isomorphism class와 rank $n$ real vector bundle들의 isomorphism class 사이에는 자연스러운 일대일 대응이 존재한다. 이 대응은 principal bundle $P$에 associated bundle $P\times_{\GL(n;\mathbb{R})}\mathbb{R}^n$을, vector bundle $E$에 frame bundle $\Fr(E)$를 대응시킨다.
:::
::: 증명
두 대응이 서로 역임을 확인하면 된다. 

우선 정의에 의해 frame bundle $\Fr(E)$의 한 점은 fiber $E_x$의 한 ordered basis와 같으며, 이는 정확히 standard Euclidean space $\mathbb{R}^n$의 각 standard basis가 어디로 가는지를 보면 되므로 linear isomorphism $b:\mathbb{R}^n\rightarrow E_x$와 정확히 같은 정보량을 가진다. 이렇게 정의된 morphism

$$\Fr(E)\times_{\GL(n;\mathbb{R})}\mathbb{R}^n\rightarrow E,\qquad [(b,v)]\mapsto b(v)$$

는 잘 정의되는데, $(b,v)$를 $(b\circ A, A^{-1}v)$로 바꾸어도 $(b\circ A)(A^{-1}v)=b(v)$로 같은 값을 주기 때문이다. 이 morphism은 각 fiber 위에서 선형동형이므로 vector bundle의 isomorphism이다. 

거꾸로 principal bundle $P$에서 출발하면, $P\times_G\mathbb{R}^n$의 frame bundle이 다시 $P$와 동형임을 local trivialization 위에서 transition function $g_{ij}$가 양쪽에서 일치함을 통해 확인할 수 있다. 

두 구성 모두 transition function을 보존하므로 isomorphism class를 보존하고, morphism의 naturality는 pullback과의 호환에서 따라온다.
:::

이 동치 덕분에 vector bundle에 대한 모든 분류 문제는 principal $\GL(n;\mathbb{R})$-bundle에 대한 문제로 번역된다. 같은 방식으로 complex vector bundle은 principal $\GL(n;\mathbb{C})$-bundle에, oriented real vector bundle은 principal $\GL^+(n;\mathbb{R})$-bundle에 대응한다. 따라서 임의의 구조군 $G$에 대하여 principal $G$-bundle을 분류할 수 있다면, 이 모든 경우가 한꺼번에 해결된다.

Vector bundle에서와 마찬가지로, 연속함수 $f:X'\rightarrow X$와 principal $G$-bundle $p:P\rightarrow X$가 주어지면 *pullback bundle*

$$f^\ast P=\{(x',y)\in X'\times P\mid f(x')=p(y)\}$$

이 정의된다. 여기에 $(x',y)\cdot g=(x',y\cdot g)$로 작용을 주면 $f^\ast P\rightarrow X'$은 다시 principal $G$-bundle이 되며, 이는 transition function의 관점에서는 $g_{ij}$를 $g_{ij}\circ f$로 끌어당기는 것에 해당한다. 핵심적인 사실은 이 pullback이 $f$의 homotopy class에만 의존한다는 사실이다.

::: 정리 5 (Pullback의 homotopy invariance)
$X$가 paracompact Hausdorff이고 $f_0,f_1:X\rightarrow Y$가 homotopic이라 하자. ([§호모토피, ⁋정의 2](/ko/math/algebraic_topology/homotopy#def2)) 그럼 임의의 principal $G$-bundle $p:P\rightarrow Y$에 대하여 $f_0^\ast P$와 $f_1^\ast P$는 $X$ 위에서 isomorphic하다.
:::
::: 증명
핵심은 다음의 사실이다. 

> $X$가 paracompact Hausdorff일 때, $X\times[0,1]$ 위의 principal $G$-bundle $Q$는 $X\times\{0\}$으로의 restriction을 projection $X\times[0,1]\rightarrow X\times\{0\}$으로 pullback한 것과 isomorphic하다.

이는 bundle의 covering homotopy property로, paracompact Hausdorff base 위의 trivializing cover가 locally finite partition of unity를 갖는다는 사실에 따른 것이다. 증명의 골자는 $[0,1]$을 작은 구간들로 나누어 각 구간 위에서 trivialization을 잇고, partition of unity로 이 local isomorphism들을 붙이는 것이다. 

이제 homotopy $H:X\times[0,1]\rightarrow Y$가 $f_0,f_1$을 잇는다 하고 $Q=H^\ast P$로 정의하자. 위 사실에 의해 $Q$는 $Q\vert_{X\times\{0\}}=f_0^\ast P$를 projection으로 끌어당긴 것과 isomorphic하고, 같은 논증을 $X\times\{1\}$ 끝에서 반복하면 $Q\vert_{X\times\{1\}}=f_1^\ast P$ 역시 같은 bundle과 isomorphic이다. 
:::

특히 $X$가 contractible이면 항등사상이 상수사상과 homotopic하므로 $X$ 위의 모든 principal $G$-bundle은 trivial이다. 일반적으로 CW complex는 항상 paracompact Hausdorff이므로 우리가 다루려는 base들에 대해서는 위 정리의 가정이 자동으로 성립한다.

## Universal bundle과 classifying space

[정리 5](#thm5)는 함수 $f$를 $f^\ast P$로 대응시키는 것이 $f$의 homotopy class에만 의존함을 말해 준다. 따라서, 만일 어떤 고정된 principal $G$-bundle 하나를 모든 다른 bundle이 pullback으로 얻을 수 있는 원천으로 삼을 수 있다면, principal $G$-bundle의 분류는 그 원천 공간으로의 homotopy class를 세는 일로 환원될 것이며, 이는 vector bundle에서 $\Gr(k,\mathbb{R}^\infty)$ 위의 universal bundle이 그러한 원천이었던 것을 일반화한다.

::: 정의 6
Topological group $G$에 대하여, principal $G$-bundle $p:\E G\rightarrow \B G$가 *universal bundle<sub>보편다발</sub>*이라는 것은 total space $\E G$가 contractible인 것, 곧 $\E G$가 한 점과 homotopy equivalent인 것이다. ([§호모토피, ⁋정의 4](/ko/math/algebraic_topology/homotopy#def4)) 이때 base space $\B G$를 $G$의 *classifying space<sub>분류공간</sub>*라 부른다.
:::

즉, universal $G$-bundle은 contractible space 위의 free $G$-action이며, 그 orbit space $\B G=\E G/G$가 base space이며, 여기로의 projection map이 bundle map이다. $\E G$가 contractible이라는 조건은 [정리 8](#thm8)에서 중요하게 사용될 것이다. 그 전에, 우선 다음이 성립한다. 

::: 정리 7 (Milnor)
임의의 topological group $G$에 대하여 universal bundle $\E G\rightarrow \B G$가 존재한다.
:::

이에 대한 증명은 $G$의 infinite join 

$$\E G=G\ast G\ast G\ast\cdots$$

를 사용하며, 이 공간은 임의의 $n$에 대해 $n$-connected이고, 따라서 weakly contractible이 되며 CW 구조 하에서 contractible이라는 것이 요지이다.

한편, universal bundle은 본질적으로 유일하다. 두 universal bundle $\E G\rightarrow \B G$와 $\E G'\rightarrow \B G'$이 주어졌다 하자. $\E G'\rightarrow\B G'$이 universal이므로 아래에서 보일 [정리 8](#thm8)에 의하여 $\B G$ 위의 principal $G$-bundle $\E G$를 분류하는 morphism $u:\B G\rightarrow \B G'$이 존재하여 $\E G\cong u^\ast\E G'$이고, 두 bundle의 역할을 바꾸면 마찬가지로 $\E G'\cong v^\ast\E G$인 $v:\B G'\rightarrow \B G$가 존재한다. 그럼 $(v\circ u)^\ast\E G\cong u^\ast\E G'\cong\E G$인데 항등사상 또한 $\E G$를 분류하므로, 같은 정리의 단사성에 의하여 $v\circ u$는 $\B G$의 항등사상과 homotopic하고 같은 이유로 $u\circ v$는 $\B G'$의 항등사상과 homotopic하다. 따라서 $\B G$는 homotopy equivalence를 넘어서는 모호함 없이 결정되며, 우리는 $\B G$를 *the* classifying space라 부른다.

꼭 이 논증의 재료라서가 아니더라도, 이 글의 가장 핵심적인 결과는 당연히 다음의 정리이다.

::: 정리 8 (분류정리)
Paracompact Hausdorff space $X$와 topological group $G$에 대하여, $[X,\B G]$를 $X$에서 $\B G$로의 free homotopy class들의 집합이라 하자. 그럼 universal bundle $\E G\rightarrow \B G$를 pullback하는 morphism

$$[X,\B G]\rightarrow\{\text{principal $G$-bundles over $X$}\}/{\cong};\qquad [f]\mapsto f^\ast \E G$$

은 잘 정의된 전단사이며, morphism $X'\rightarrow X$에 대한 pullback과 호환된다는 의미에서 자연스럽다.

{% diagram Math/Algebraic_Topology/Classifying_Spaces-1.svg width="8.21em" alt="분류사상의 pullback 사각형" %}

:::
::: 증명
$[f]\mapsto f^\ast \E G$가 $[f]$의 대표 선택에 의존하지 않는 것은 [정리 5](#thm5)에 의한 것이다. 우리는 이것이 전단사임을 간략히 살펴본다.

우선 $X$ 위의 principal $G$-bundle $P$가 주어졌다 하자. $X$가 paracompact Hausdorff이므로, [\[위상수학\] §Compactness와 paracompactness, ⁋정리 27](/ko/math/topology/compactness#thm27)에 의하여 $P$를 trivialize하는 open cover $\{U_i\}$와 이에 종속된 locally finite partition of unity $\{\rho_i\}$를 함께 잡을 수 있다. 각 $U_i$ 위의 trivialization은 $G$-equivariant map $\psi_i:p^{-1}(U_i)\rightarrow G$를 주므로, $\E G$를 [정리 7](#thm7)의 join으로 두어 그 점을 $\sum_i t_ig_i$의 꼴로 적으면

$$\widetilde{f}:P\rightarrow \E G,\qquad y\mapsto \sum_i \rho_i(p(y))\psi_i(y)$$

는 잘 정의된 $G$-equivariant map이다. 이 때 $G$-equivariant map은 base space 사이의 morphism $f:X\rightarrow \B G$로 내려가고, $\widetilde{f}$가 fiber마다 동형이므로 $P\cong f^\ast\E G$를 얻는다.

이제 injectivity를 보이기 위해 $f_0,f_1:X\rightarrow \B G$에 대하여 $f_0^\ast \E G\cong f_1^\ast \E G=:P$라 하자. 우리는 $f_0$과 $f_1$이 homotopic한 것을 보여야 한다. 각 $f_i$는 bundle map $P\cong f_i^\ast \E G\rightarrow \E G$, 곧 $P$에서 universal bundle로 가는 $G$-equivariant bundle map $\Phi_i:P\rightarrow \E G$을 가진다. 그런데 $\E G$가 contractible이므로, paracompact 공간 위의 principal bundle $P$에서 $\E G$로 가는 임의의 두 $G$-equivariant map은 서로 $G$-equivariant homotopic하며, 따라서 $\Phi_0$과 $\Phi_1$을 잇는 $G$-equivariant homotopy $P\times[0,1]\rightarrow \E G$가 존재하고, 이것이 base로 내려가 $f_0$과 $f_1$ 사이의 homotopy를 주므로 $[f_0]=[f_1]$이다. 
:::

이 정리는 principal $G$-bundle의 기하학적 분류를 순수하게 homotopy의 데이터 $[X,\B G]$로 옮긴다. [명제 4](#prop4)와 결합하면 rank $n$ real vector bundle의 분류가 $[X,\B\GL(n;\mathbb{R})]$로, complex의 경우 $[X,\B\GL(n;\mathbb{C})]$로 옮겨지게 되며, 실제로 이들 $\B\GL(n; \mathbb{R})$과 $\B\GL(n; \mathbb{C})$이 실은 (real/complex) Grassmannian인 것을 곧 살펴보게 될 것이다. 

::: 보조정리 9
Classifying space의 구성은 $G$에 대해 functorial이다. Continuous group homomorphism $\phi:G\rightarrow H$가 주어지면, $\E G$ 위의 $G$-작용을 $\phi$를 통해 $H$-action으로 바꾸어 얻는 associated bundle $\E G\times_G H$를 분류하는 morphism이 $\B\phi:\B G\rightarrow \B H$를 유도한다. 이는 $\B(\psi\circ\phi)\simeq \B\psi\circ \B\phi$를 만족하여, $G\mapsto \B G$가 homotopy category 위의 functor가 되게 한다. 가령 inclusion $\Umat(n)\hookrightarrow\GL(n;\mathbb{C})$이 유도하는 $\B\Umat(n)\rightarrow \B\GL(n;\mathbb{C})$이 아래에서 쓰인다.
:::
::: 증명
[정리 7](#thm7)의 $\B G$는 CW complex이므로 paracompact Hausdorff이고, 따라서 $\B G$ 위의 principal bundle들에 대하여 [정리 8](#thm8)을 쓸 수 있다. 이제 $\B\phi$가 $\B\phi^\ast\E H\cong\E G\times_G H$로 정해진다는 것과, associated bundle을 만드는 것이 pullback과 교환한다는 것으로부터 continuous group homomorphism $\psi:H\rightarrow K$에 대하여

$$(\B\psi\circ\B\phi)^\ast\E K\cong\B\phi^\ast\left(\E H\times_H K\right)\cong\left(\B\phi^\ast\E H\right)\times_H K\cong\left(\E G\times_G H\right)\times_H K\cong \E G\times_G K$$

를 얻는다. 마지막 항에서 $G$가 $K$에 작용하는 방식은 $\psi\circ\phi$를 통한 것이므로 이는 정확히 $\B(\psi\circ\phi)$가 분류하는 bundle이고, 따라서 $\B\psi\circ\B\phi$와 $\B(\psi\circ\phi)$는 $\B G$ 위의 같은 principal $K$-bundle을 분류한다. 그럼 [정리 8](#thm8)의 단사성에 의하여 이들은 homotopic하다. 
:::

## 분류공간의 예

현실적으로, 이 글에서 가장 유용한 부분은 존재성보다도 이 classifying space들이 어떻게 주어지는지에 대한 것이다. 가장 단순한 경우는 다음과 같다. 

::: 예시 10
$G$가 discrete group이라 하자. 그럼 임의의 base $B$ 위에 정의된 principal $G$-bundle은 그 fiber가 discrete이므로 $B$ 위의 covering space가 된다. 그럼 이 이해에서 $G$의 right action은 Deck transformation이 되며, fiber 위에서 Deck group이 transitive하게 작용하므로 이 covering space는 *regular* covering space이다. 

이제 이를 universal bundle $\E G \rightarrow \B G$에 적용하자. $\E G$가 contractible이므로 이는 $\B G$의 universal cover이며, [정리 7](#thm7)의 $\B G$는 connected CW complex이므로 covering space 이론이 요구하는 path-connected, locally path-connected, semi-locally simply connected 조건이 모두 성립한다. 그럼 [§피복공간, §§피복공간의 기본정리](/ko/math/algebraic_topology/covering_spaces#피복공간의-기본정리)에서 살펴본 대로 이 covering space의 Deck transformation group은 $\pi_1(\B G)$와 isomorphic한데, 우리는 앞서 이 Deck group이 곧 $G$가 되어야 하는 것을 살펴보았으므로 $\pi_1(\B G)\cong G$이고, $\E G$가 contractible이라 $\B G$의 universal cover 또한 contractible이므로 $\pi_n(\B G)=0$ ($n\geq 2$) 이다. 곧 $\B G$는 Eilenberg–MacLane 공간 $K(G,1)$이다.

더 구체적인 예시로 $G=\mathbb{Z}/2$인 경우와 $G=\mathbb{Z}$인 경우를 각각 보자. 우선 $\mathbb{Z}/2$의 경우 우리는 $\mathbb{Z}/2$이 free하게 작용하는 contractible space를 찾아야 하는데, $S^\infty$에 antipodal action을 준 게 정확히 이 두 조건을 모두 만족한다. 그럼 이 action의 orbit space는 $\RP^\infty$가 된다. $\mathbb{Z}$의 경우도 이미 우리와 친숙한 예시에서 찾아올 수 있는데, 바로 [§피복공간, ⁋정의 3](/ko/math/algebraic_topology/covering_spaces#def3) 직후에 covering space의 표준적인 예시로 소개한 $\mathbb{R}\rightarrow S^1$이 그러하다. 
:::

이제 실제로 우리가 관심있는 group들의 classifying space들을 살펴보자. Discrete이 아닌 group 중 가장 기본적인 예는 $G=S^1$이며 이는 보편적으로 $\mathbb{C}^\times$에 들어있는 길이 $1$짜리 복소수들 $e^{2\pi it}$들의 모임으로 생각한다. 그럼 $S^1$은 $\mathbb{C}^\infty\setminus\{0\}$ 위에 스칼라곱으로 free하게 작용한다. 

이제 각각의 $\mathbb{C}^n\setminus 0$을 radial deformation retract를 통해 단위구면 

$$S^{2n-1}\subseteq\mathbb{C}^n\cong\mathbb{R}^{2n}$$

로 deformation retract할 수 있으며, canonical inclusion

$$\mathbb{C}^n\hookrightarrow\mathbb{C}^{n+1}\hookrightarrow \mathbb{C}^{n+2}\hookrightarrow \cdots$$

이 이전의 단위구면을 다음 단위구면의 적도에 넣어주는 inclusion $S^{2n-1}\hookrightarrow S^{2n+1}$을 유도하는 것을 보자. 따라서 $\mathbb{C}^\infty\setminus \{0\}$을 colimit $\varinjlim (\mathbb{C}^n\setminus \{0\})$으로 본다면, 이는 colimit $\varinjlim S^{2n-1}$로 deformation retract되며, 이는 $S^\infty$를 정의할 때 등장하는 inclusion

$$S^1\subseteq S^2\subseteq S^3\cdots $$

의 cofinal subsequence이므로 그 결과는 $S^\infty$와 같다. 한편 $S^1$의 스칼라곱은 norm을 보존하므로, 이 action은 단위구면 $S^\infty\subseteq\mathbb{C}^\infty\setminus\{0\}$ 위의 free action으로 제한된다. 즉 $\E S^1=S^\infty$로 잡으면 이는 $S^1$이 free하게 작용하는 contractible space이며, $\mathbb{C}^\infty$의 각 complex line이 $S^\infty$와 만나는 자취가 정확히 하나의 $S^1$-orbit, 곧 그 직선 안의 unit circle이므로 그 orbit space는 complex projective space

$$\B S^1=S^\infty/S^1=\CP^\infty$$

이 된다.

이것이 vector bundle의 언어로 갖는 의미를 살펴보기 위해 [정의 3](#def3)의 associated bundle로 돌아가자. $S^1$은 $\mathbb{C}$ 위에 스칼라곱으로 작용하므로, 임의의 principal $S^1$-bundle $P\rightarrow X$마다 associated bundle

$$P\times_{S^1}\mathbb{C}\rightarrow X$$

가 정의된다. 앞서 살펴보았듯 이는 $P$와 같은 open cover 위에서 fiber가 $\mathbb{C}$이고 transition이 $g_{ij}$의 $\mathbb{C}$ 위에서의 작용으로 주어지는 bundle인데, 스칼라곱은 $\mathbb{C}$-linear하므로 이 transition들은 $S^1\subseteq\mathbb{C}^\times=\GL(1;\mathbb{C})$의 원소들이 주는 linear automorphism들이고, 따라서 $P\times_{S^1}\mathbb{C}$는 complex line bundle이다. 즉 principal $S^1$-bundle은 $\mathbb{C}$를 붙이는 것만으로 자연스럽게 line bundle이 된다. 거꾸로 line bundle $L\rightarrow X$가 주어지면 paracompactness에 의해 Hermitian metric을 잡을 수 있고, 각 fiber의 unit vector들의 모임인 sphere bundle $S(L)\subseteq L$은 $S^1$의 스칼라곱에 대하여 principal $S^1$-bundle이 된다. [명제 4](#prop4)에서 ordered basis를 unit vector로 바꾼 것과 같은 논증으로 이 두 구성이 서로의 역임을 확인할 수 있으며, 이것이 line bundle의 구조군을 $\GL(1;\mathbb{C})$에서 $S^1=\Umat(1)$로 줄여 잡을 수 있는 이유이다. 

이를 명시적으로 universal bundle $\E S^1=S^\infty\rightarrow\CP^\infty$에 적용하면 line bundle

$$S^\infty\times_{S^1}\mathbb{C}\longrightarrow\CP^\infty$$

을 얻는다. 점 $[\ell]\in\CP^\infty$ 위의 fiber를 살피면 equivalence class $[e,z]$는 unit vector $e$가 결정하는 직선 $\ell=\mathbb{C}e$의 원소 $ze\in\ell$와 같으므로, 이는 각 직선을 그 자신을 fiber로 갖는 tautological line bundle $\gamma$이다. 즉 [§벡터다발의 특성류, ⁋예시 8](/ko/math/algebraic_topology/characteristic_classes#ex8)에서 $\gamma$가 complex line bundle의 universal family가 되었던 것은 universal principal $S^1$-bundle에 $\mathbb{C}$를 붙인 결과가 정확히 $\gamma$이기 때문이며, 거꾸로 그곳에서 $\gamma$의 sphere bundle로 등장했던 $S^\infty$가 바로 $\E S^1$이다.

::: 예시 11 (선형군의 분류공간)
위의 논의는 임의의 rank $n$ bundle로 일반화된다. 우선 일반적으로 topological group $G$의 continuous representation 

$$G\rightarrow\GL(n;\mathbb{C})$$

이 주어지면 임의의 principal $G$-bundle $P$에 대해 associated bundle $P\times_G\mathbb{C}^n$은 rank $n$ complex vector bundle이 된다는 것을 관찰하자. Line bundle이 principal $\Umat(1)=S^1$-bundle에 표준 representation $\mathbb{C}$를 붙인 것이었으므로, rank $n$ complex vector bundle은 principal $\Umat(n)$-bundle에 표준 representation $\mathbb{C}^n$을 붙여 얻어질 것을 기대하는 것이 자연스럽다. 

이를 위해 필요한 것은 universal principal $\Umat(n)$-bundle로, 이는 $\mathbb{C}^\infty$의 orthonormal $n$-frame 전체의 공간인 *complex Stiefel manifold*

$$V_n(\mathbb{C}^\infty)=\varinjlim_k V_n(\mathbb{C}^k)$$

위에 $\Umat(n)$이 오른쪽에서 행렬곱으로 작용하고 그 orbit space가 $\Gr(n,\mathbb{C}^\infty)$가 되는 것으로 주어진다. Orthonormal $1$-frame은 unit vector에 불과하므로 $n=1$인 경우 이는 정확히 본문의 $\E S^1=S^\infty\rightarrow\CP^\infty$이며, 일반적인 $n$에 대해서도 앞서 $S^\infty$에서 본 것과 같은 논증으로 $V_n(\mathbb{C}^\infty)$가 한 점으로 deformation retract되어 contractible이므로 이 principal bundle은 universal이다.

이제 여기에 canonical representation $\mathbb{C}^n$을 붙이면 associated bundle

$$V_n(\mathbb{C}^\infty)\times_{\Umat(n)}\mathbb{C}^n\longrightarrow\Gr(n,\mathbb{C}^\infty)$$

을 얻는다. 점 $[V]$ 위의 fiber를 살피면 $z=(z_1,\ldots,z_n)\in\mathbb{C}^n$에 대해 equivalence class $[(e_1,\ldots,e_n),z]$는 frame이 span하는 부분공간 $V$의 원소 $z_1e_1+\cdots+z_ne_n\in V$와 같으므로, line bundle에서와 마찬가지로 이는 각 부분공간을 그 자신을 fiber로 갖는 tautological $n$-plane bundle $\gamma^n$이며, 거꾸로 $\gamma^n$의 각 fiber의 orthonormal frame 전체를 모으면 $V_n(\mathbb{C}^\infty)$가 복원되는 것도 line bundle에서와 같다. 즉

$$\B\Umat(n)=\Gr(n,\mathbb{C}^\infty)$$

이고, 그 위의 universal bundle은 tautological $n$-plane bundle이다. 

한편 [명제 4](#prop4), 정확히는 해당 명제의 complex 버전이 rank $n$ complex vector bundle에 대응시키는 과정은 엄밀하게 말하면 principal $\GL(n;\mathbb{C})$-bundle을 이용한 associated bundle을 사용해야 한다. 즉, 위의 계산이 임의의 complex vector bundle의 분류로 이어지려면 $\B\GL(n;\mathbb{C})$와 $\B\Umat(n)$이 같아야 하며, 실제로 그러하다. 이는 [\[선형대수학\] §복소내적공간, ⁋명제 7](/ko/math/linear_algebra/complex_inner_product_spaces#prop7)에 의한 것으로, $\GL(n;\mathbb{C})$의 임의의 원소는 unitary 행렬과 대각성분이 양수인 upper-triangular 행렬의 곱으로 유일하게 분해되며, 이 분해가 연속임을 보일 수 있다. 이제 이 분해에서 upper-triangular 성분을 항등원 쪽으로 수축시키면 그것이 바로 $\GL(n;\mathbb{C})$의 $\Umat(n)$으로의 deformation retract이다. 즉 inclusion $\Umat(n)\hookrightarrow\GL(n;\mathbb{C})$은 homotopy equivalence이고, classifying space의 functoriality [보조정리 9](#lem9)에 의하여

$$\B\GL(n;\mathbb{C})\simeq \B\Umat(n)=\Gr(n,\mathbb{C}^\infty)$$

이다. 

같은 이야기 전체를 $\mathbb{R}^\infty$의 orthonormal $n$-frame 전체의 공간인 real Stiefel manifold $V_n(\mathbb{R}^\infty)$와 $\Omat(n)$, 그리고 Gram–Schmidt 직교화에 대해 반복하면

$$\B\GL(n;\mathbb{R})\simeq \B\Omat(n)=\Gr(n,\mathbb{R}^\infty)$$

을 얻는다.
:::

## 분류공간의 코호몰로지

[정리 8](#thm8)에 따르면 구조군 $G$를 갖는 bundle의 특성류란 $\B G$의 cohomology class를 분류사상으로 pullback한 것이다. 따라서 특성류 이론은 $\B G$의 cohomology ring을 계산하는 일과 같으며, 우리는 가장 기본적인 group들에 대해 이를 정리한다.

출발점은 complex projective space의 cohomology ring이다. [§벡터다발의 특성류, ⁋예시 8](/ko/math/algebraic_topology/characteristic_classes#ex8)에서 우리는

$$H^\bullet(\CP^\infty;\mathbb{Z})=\mathbb{Z}[t],\qquad \lvert t\rvert=2$$

임을 보았으며, generator $t$는 tautological line bundle의 first Chern class였다. 우리는 위에서 $\B S^1=\CP^\infty$인 것을 보았으므로, 이는 곧

$$H^\bullet(\B S^1;\mathbb{Z})=\mathbb{Z}[t],\qquad \lvert t\rvert=2$$

를 뜻한다. Torus의 경우는 곱공간의 cohomology로부터 따라온다.

::: 따름정리 12
$n$차원 torus $T=(S^1)^n$에 대하여

$$H^\bullet(\B T;\mathbb{Z})=\mathbb{Z}[t_1,\ldots,t_n],\qquad \lvert t_i\rvert=2$$

는 $n$개의 degree $2$ generator로 이루어진 polynomial ring이다. 더 나아가 degree $2$ 부분 $H^2(\B T;\mathbb{Z})$은 $\Hom(T,S^1)$과 표준적으로 isomorphic하다.
:::
::: 증명
$\B T=(\CP^\infty)^n$이므로 $i$번째 인자로의 projection을 $\pi_i:\B T\rightarrow\CP^\infty$라 하자. 앞 절의 $\B S^1=\CP^\infty$ 계산으로부터 각 인자의 cohomology $H^\bullet(\CP^\infty;\mathbb{Z})=\mathbb{Z}[t]$는 각 degree에서 finite rank의 free abelian group이므로, [§코호몰로지, ⁋따름정리 10](/ko/math/algebraic_topology/cohomology#cor10)과 [§코호몰로지, ⁋정리 5](/ko/math/algebraic_topology/cohomology#thm5)이 함께 주는 cohomology 판본의 Künneth 공식에서 $\Tor$ 항과 $\Ext$ 항이 모두 사라진다. 따라서 cross product가 각 degree에서 isomorphism이고 이는 [§합곱, ⁋명제 3](/ko/math/algebraic_topology/cup_products#prop3)에 의하여 graded algebra homomorphism이므로, 인자의 개수에 대한 귀납으로 ring isomorphism

$$H^\bullet(\B T;\mathbb{Z})\cong\bigotimes_{i=1}^n \mathbb{Z}[t_i]=\mathbb{Z}[t_1,\ldots,t_n]$$

을 얻으며, 여기서 generator $t_i$는 $i$번째 인자의 generator $t$를 $\pi_i$로 끌어당긴 것, 곧 $t_i=\pi_i^\ast t$이다.

이제 degree $2$ 부분을 보자. *Character* $\rchi:T\rightarrow S^1$는 functoriality에 의해

$$\B\rchi:\B T\rightarrow \B S^1=\CP^\infty$$

를 유도하므로, generator $t$를 끌어당긴 $(\B\rchi)^\ast t\in H^2(\B T;\mathbb{Z})$들이 결정된다. 이 대응 $\rchi\mapsto(\B\rchi)^\ast t$는 homomorphism $\Hom(T,S^1)\rightarrow H^2(\B T;\mathbb{Z})$을 준다는 것을 확인할 수 있으며, 특히 결정적인 것은 위에서 살펴봤듯 $i$번째 좌표 projection $\pr_i:T\rightarrow S^1$이 정확히 $t_i$로 간다는 사실이다. 즉, $\B\pr_i$는 정확히 $i$번째 projection $\pi_i$와 같고, 따라서

$$(\B\pr_i)^\ast t=\pi_i^\ast t=t_i$$

이다. 곧 $\Hom(T,S^1)\cong\mathbb{Z}^n$의 표준기저 $\{\pr_1,\ldots,\pr_n\}$이 $H^2(\B T;\mathbb{Z})=\bigoplus_i\mathbb{Z}t_i$의 기저 $\{t_1,\ldots,t_n\}$으로 가므로 이 대응은 isomorphism이다. 
:::

이 동형은 character lattice 위의 다항식을 $\B T$의 cohomology class로 읽게 해 주며, torus가 작용하는 공간의 불변량을 다룰 때 핵심이 된다. Unitary group의 경우는 한 단계 더 나아간 계산이 필요하지만, 앞 글에서 이미 그 결과를 보았다.

::: 명제 13
Unitary group $\Umat(n)$에 대하여

$$H^\bullet(\B\Umat(n);\mathbb{Z})=\mathbb{Z}[c_1,\ldots,c_n],\qquad \lvert c_i\rvert=2i$$

는 universal complex bundle의 Chern class $c_i$들로 생성되는 polynomial ring이다.
:::
::: 증명
$\B\Umat(n)=\Gr(n,\mathbb{C}^\infty)$이고, 그 cohomology ring이 universal bundle의 Chern class들로 생성되는 polynomial ring

$$H^\bullet(\Gr(n,\mathbb{C}^\infty);\mathbb{Z})=\mathbb{Z}[c_1,\ldots,c_n]$$

임은 이미 [§벡터다발의 특성류, ⁋예시 8](/ko/math/algebraic_topology/characteristic_classes#ex8) 이후에 살펴보았다. 따라서 generator가 Chern class이고 $\lvert c_i\rvert=2i$라는 것만 보이면 충분하다. 

이 계산은 [따름정리 12](#cor12)와 사실상 같은 것으로, 핵심은 앞에서와 똑같이 maximal torus $T=(S^1)^n\subseteq\Umat(n)$을 대각으로 넣어 얻는 $\B T\rightarrow\B\Umat(n)$이다. $\Umat(n)$의 canonical representation $\mathbb{C}^n$을 $T$로 제한하면 좌표축을 따라

$$\mathbb{C}^n=L_1\oplus\cdots\oplus L_n$$

으로 쪼개지고, $T$는 $i$번째 직선 $L_i$ 위에 정확히 character $\pr_i$로 작용한다. 따라서 universal bundle $E$를 $\B T$로 당긴 것은 각 character에 딸린 line bundle들의 합 $\bigoplus_i\mathcal{L}_i$이고, 그 $i$번째 성분은 [따름정리 12](#cor12)에서 $c_1(\mathcal{L}_i)=(\B\pr_i)^\ast t=t_i$로 이미 계산한 바로 그 line bundle이다. 여기에 Whitney 공식을 적용하면

$$c(E)\vert_{\B T}=\prod_{i=1}^n(1+t_i);\qquad c_i\vert_{\B T}=e_i(t_1,\ldots,t_n)$$

을 얻는다. 여기서 $e_i$는 $i$번째 elementary symmetric polynomial이며, $\lvert t_i\rvert=2$이므로 $\lvert c_i\rvert=2i$이다. 이제 남은 것은 $H^\bullet(\B\Umat(n);\mathbb{Z})\rightarrow H^\bullet(\B T;\mathbb{Z})=\mathbb{Z}[t_1,\ldots,t_n]$이 단사이고 그 image가 Weyl group $S_n$의 invariant ring $\mathbb{Z}[t_1,\ldots,t_n]^{S_n}$이라는 것으로, 정수계수 대칭다항식은 elementary symmetric polynomial들이 자유롭게 생성하므로 $\mathbb{Z}[t_1,\ldots,t_n]^{S_n}=\mathbb{Z}[e_1,\ldots,e_n]=\mathbb{Z}[c_1,\ldots,c_n]$이고, 결국 $\B\Umat(n)$의 cohomology는 따름정리 12의 polynomial ring에서 $S_n$-대칭인 부분만 남긴 것이다. 자세한 계산은 [MS]로 넘긴다.
:::

이렇게 $\B\Umat(n)$의 cohomology가 Chern class들의 다항식 전부로 이루어지므로, complex vector bundle의 모든 특성류는 Chern class의 다항식이다. 같은 방식으로 $H^\bullet(\B\Omat(n);\mathbb{Z}/2)=\mathbb{Z}/2[w_1,\ldots,w_n]$이 Stiefel–Whitney class를, oriented bundle에 대해서는 $\B\SO(n)$이 Euler class를 준다. 한 공간 $X$ 대신 $G$-작용을 갖는 공간을 다룰 때, $\B G$와 그 위에서의 homotopy quotient는 이 cohomology를 base로 삼는 equivariant cohomology의 토대가 된다.

---

**참고문헌**

**[Hat]** A. Hatcher, *Vector Bundles and K-Theory*, online notes, 2017.  
**[MS]** J. W. Milnor and J. D. Stasheff, *Characteristic Classes*, Annals of Mathematics Studies 76, Princeton University Press, 1974.
