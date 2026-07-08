---
title: "분류공간"
description: "임의의 topological group을 구조군으로 갖는 principal bundle을 정의하고, universal bundle과 classifying space를 통해 이들을 homotopy 이론으로 분류한다."
excerpt: "Principal G-bundle의 분류와 classifying space BG의 구성"

categories: [Math / Algebraic Topology]
permalink: /ko/math/algebraic_topology/classifying_spaces
sidebar: 
    nav: "algebraic_topology-ko"

date: 2026-07-07
weight: 12
published: false

---

앞선 글들에서 우리는 vector bundle을 분류하기 위해 특성류를 도입하였다. 흥미로운 것 중 하나는 이들의 존재성을 보이는 방식으로, 우리는 큰 공간 위에 정의된 어떤 *universal* bundle이 존재하여, 임의의 bundle이 이것의 pullback으로 나타날 수 있다는 것을 살펴보았다. 가령 real vector bundle의 경우, infinite real Grassmannian 위의 tautological line bundle

$$E(\gamma_n^k)\rightarrow \Gr(k, \mathbb{C}^\infty)$$

이 그러한 역할을 하였으며 ([§슈티펠-휘트니 특성류, §§그라스만 다양체](/ko/math/algebraic_topology/stiefel_whitney_classes#그라스만-다양체)) complex vector bundle에서도 비슷한 construction이 존재했다. ([§벡터다발의 특성류, ⁋예시 8](/ko/math/algebraic_topology/characteristic_classes#ex8)) 한편 vector bundle의 pullback은 오직 map의 homotopy class에만 의존하므로, 고정된 공간 $$B$$ 위의 rank $$k$$ vector bundle의 isomorphism class는 이들 공간으로의 함수들의 homotopy class들의 모임 $$[B, \Gr(k, \mathbb{R}^\infty)]$$ (혹은 $$[B, \Gr(k, \mathbb{C}^\infty)]$$)이 된다. 

한편, vector bundle을 살펴보는 또 다른 관점은 이를 transition function들의 모임으로 생각하는 것이었다. 가령 임의의 vector bundle은 두 개의 trivializing open cover가 겹치는 곳에서

$$g_{ij}: U_i\cap U_j\rightarrow \GL(k;;\mathbb{R})$$

를 명시해주면 되었으며, 이 관점은 예를 들어, $$\GL(k;;\mathbb{R})$$을 $$\GL^+(k;\mathbb{R})$$로 바꿔주면 *oriented* vector bundle 또한 설명할 수 있다는 점에서 강력했다. 

이번 글의 목적은 이 두 관점을 이어주는 것이다. 즉 우리는 더 일반적으로, structure group이 (topological) group $$G$$인 경우 나타나는 *principal $$G$$-budnle*을 정의하고, 이러한 것들을 분류하는 공간인 *classifying space* $$BG$$를 정의할 것이다. 이번 글에서 $$G$$는 항상 topological group을 의미하며, 별다른 언급이 없는 한 base space는 paracompact인 것으로 가정한다.

## Principal bundle의 정의

Vector bundle의 fiber에는 벡터공간 구조가 있었고, 그 transition function은 이 구조를 보존하는 linear automorphism, 곧 $$\GL(k;,\mathbb{R})$$의 원소들이었다. 일반적인 구조군 $$G$$를 다룰 때는 fiber 자체를 $$G$$로 두고, transition을 $$G$$의 left translation으로 주는 것이 자연스럽다. 약간의 차이는 이러한 관점에서 특별한 점이 존재하지 않는다는 것으로, 하나의 chart 상에서 항등원인 fiber의 원소도 left translation을 통해 다른 chart에서는 fiber의 다른 원소로 이해된다. 즉, 이들 원소는 *$$G$$-torsor*들로 생각해야 하며, 이를 좌표에 의존하지 않고 기술하기 위해 우리는 total space 위의 $$G$$-action을 사용한다.

::: 정의 1
Topological group $$G$$에 대하여, fiber bundle $$p:P\rightarrow X$$와 그 위의 연속적인 right action $$P\times G\rightarrow P$$가 주어졌다 하자. 이 데이터가 *principal $$G$$-bundle<sub>주다발</sub>*이라는 것은 다음 세 조건이 성립하는 것이다.

1. $$G$$-action은 fiber를 보존한다. 즉 모든 $$y\in P$$와 $$g\in G$$에 대하여 $$p(y\cdot g)=p(y)$$이다.
2. 각 fiber 위에서 $$G$$-action은 free이고 transitive하다. 즉 임의의 $$x\in X$$에 대하여, 한 점 $$y\in p^{-1}(x)$$를 고정하면 $$g\mapsto y\cdot g$$가 $$G$$에서 $$p^{-1}(x)$$로의 전단사이다.
3. ($$G$$-equivariant local triviality) 각 $$x\in X$$마다 열린근방 $$U$$와, $$U$$ 위에서 $$p$$와 호환되는 $$G$$-equivariant homeomorphism $$\varphi:p^{-1}(U)\rightarrow U\times G$$가 존재한다. 여기서 $$U\times G$$ 위의 $$G$$-작용은 $$(u,h)\cdot g=(u,hg)$$로 둔다.
:::

즉, 국소적으로는 base space 위에 fiber 방향으로 $$G$$들을 달아주고, 그 각각의 fiber 위에 $$G$$가 right translation으로 작용하는 것이다. 

그럼 두 principal $$G$$-bundle $$P,P'\rightarrow X$$ 사이의 *morphism*는 $$p'\circ f=p$$를 만족하고 $$G$$-작용과 호환되는 연속함수 $$f:P\rightarrow P'$$를 뜻하며, 이것이 homeomorphism이면 이를 두 principal bundle 사이의 *isomorphism*이라 부른다. Local trivialization $$\varphi_i:p^{-1}(U_i)\rightarrow U_i\times G$$들을 고정하면, $$U_i\cap U_j$$ 위에서 $$\varphi_i\circ\varphi_j^{-1}(u,h)=(u,g_{ij}(u)h)$$를 만족하는 연속함수 $$g_{ij}:U_i\cap U_j\rightarrow G$$가 결정된다. 이 transition function들은 vector bundle에서와 같은 cocycle 조건

$$g_{ij}(x)g_{jk}(x)=g_{ik}(x),\qquad g_{ii}(x)=e$$

를 만족하며, 두 cocycle $$(g_{ij})$$와 $$(g_{ij}')$$이 같은 bundle을 주는 것은 연속함수 $$\lambda_i:U_i\rightarrow G$$들이 존재하여 $$g_{ij}'=\lambda_i g_{ij}\lambda_j^{-1}$$인 것과 동치이다. 따라서 open cover $$\{U_i\}$$ 위에서 trivialize되는 principal $$G$$-bundle의 isomorphism class들은 nonabelian Čech cohomology $$\check{H}^1(X;G)$$로 분류되며, $$G=\GL(k;,\mathbb{R})$$인 경우 이는 앞 글의 vector bundle 분류와 정확히 일치한다.

Vector bundle은 언제나 zero section을 가졌으나, principal bundle은 fiber가 $$G$$가 아니라 $$G$$-torsor이므로 이러한 역할을 하는 section을 잡는 것이 자명하지 않다. 실제로 다음 명제는 section의 존재 여부가 principal bundle의 자명성을 완전히 결정한다는 것을 보여준단.

::: 명제 2
Principal $$G$$-bundle $$p:P\rightarrow X$$가 trivial bundle과 isomorphic한 것은 연속적인 global section $$s:X\rightarrow P$$가 존재하는 것과 동치이다.
:::
::: 증명
Trivial bundle $$X\times G$$는 $$x\mapsto(x,e)$$라는 section을 가지므로, $$P$$가 trivial이면 isomorphism을 통해 section을 얻는다. 역으로 section $$s:X\rightarrow P$$가 존재한다 하고, 다음의 함수

$$\Phi:X\times G\rightarrow P,\qquad (x,g)\mapsto s(x)\cdot g$$

를 생각한다. 각 fiber 위에서 $$G$$-action이 simply transitive ([정의 1](#def1)의 조건 (2)) 하므로 $$\Phi$$를 fiber $$\{x\}\times G\rightarrow p^{-1}(x)$$로 제한한 것은 전단사이고, 따라서 $$\Phi$$는 전단사이다. $$\Phi$$는 정의에 의해 $$p\circ\Phi=\pr_1$$을 만족하고 $$G$$-action과 호환되므로 morphism over $$X$$이다. 마지막으로 $$\Phi$$가 homeomorphism임은 국소적으로 확인하면 되는데, trivialization $$\varphi:p^{-1}(U)\rightarrow U\times G$$ 위에서 $$s$$가 $$x\mapsto(x,\sigma(x))$$의 꼴로 쓰이면 ($$\sigma:U\rightarrow G$$ 연속) $$\Phi$$는 $$(x,g)\mapsto(x,\sigma(x)g)$$가 되어 그 역 $$(x,h)\mapsto(x,\sigma(x)^{-1}h)$$이 연속이기 때문이다.
:::

이 명제는 principal bundle과 vector bundle의 결정적인 차이를 드러낸다. 따라서 principal bundle과 vector bundle을 관계짓기 위해서는 이들 둘을 이어주는 대상이 필요하다.

Principal $$G$$-bundle이 vector bundle이 될 수 없는 이유 중 가장 단순한 것은 vector bundle의 fiber는 vector space지 group이 아니라는 데에 있다. 우리는 이를 해결하기 위해 다음을 정의한다. 

::: 정의 3
Principal $$G$$-bundle $$p:P\rightarrow X$$와, $$G$$가 왼쪽에서 연속적으로 작용하는 위상공간 $$F$$가 주어졌다 하자. 그럼 $$P\times F$$ 위에 $$G$$-action을

$$(y,f)\cdot g=(y\cdot g,\ g^{-1}\cdot f)$$

로 정의하고, 그 orbit space를 $$P\times_G F=(P\times F)/G$$로 적는다. 그럼 $$(y,f)\mapsto p(y)$$가 유도하는 사상 $$P\times_G F\rightarrow X$$는 fiber $$F$$를 갖는 fiber bundle이며, 이를 $$P$$의 *associated bundle<sub>수반다발</sub>*이라 부른다.
:::

직관적으로 이는 principal $$G$$-bundle이 <em-ko>비틀려있는</em-ko> 구조를 따라 fiber $$F$$를 이어붙여주는 것으로, 가령 trivial $$G$$-bundle $$X\times G$$와 fiber $$F$$에 이를 적용하면 trivial fiber bundle $$X\times F$$가 나오고, 비슷하게 약간 비틀려있는 (즉 non-trivial한) principal $$G$$-bundle $$P$$와 fiber $$F$$에 이를 적용하면 그로부터 얻어지는 fiber bundle은 fiber가 $$F$$이고, $$P$$에서 비틀림 데이터를 받아오는 bundle이 된다. 

가장 투명한 예시는 vector bundle이므로, 여기에서 정의를 차례차례 따라가보자. Topological group $$G=\GL(k;, \mathbb{R})$$은 dimension $$k$$ real vector space $$F=V$$ 위에 왼쪽에서 작용한다. 또, 편의를 위해 trivial $$G$$-bundle $$P=X\times G$$가 주어졌다 하자. 그럼 우선 곱공간 $$P\times F=(X\times G)\times V$$ 위에 정의된 $$G$$-action은

$$\bigl((x,g),v\bigr)\cdot h=\bigl((x, gh),h^{-1}v\bigr)$$

이 되며, 그 orbit space는 $$X\times V$$에 불과하다. 이는 임의의 원소 $$((x,g),v)$$에 $$h=g^{-1}$$로의 action을 취하면

$$((x,g),v)\cdot g^{-1}=\bigl((x,e),gv\bigr)$$

이 되기 때문으로, 이 과정에서 우리는 $$X\times G$$의 $$(x,e)$$를 $$X$$의 원소 $$x$$와 identify하여, 다음의 식

$$[((x,g),v)]\mapsto(x,gv)$$

가 well-defined인 homeomorphism인 것을 사용하였다. 즉 trivial $$G$$-bundle에서 출발하면 associated bundle도 trivial하다.

더 일반적으로 만일 $$P$$가 $$\{U_i\}$$ 위에서 transition function $$g_{ij}$$로 주어지면, $$P\times_G F$$는 같은 $$U_i$$ 위에서 $$F$$를 fiber로 하고 transition이 $$g_{ij}$$의 $$F$$ 위에서의 작용으로 주어지는 bundle이 된다. 

이 역방향의 구성도 가능하다. Rank $$n$$ vector bundle $$E\rightarrow X$$가 주어지면, 각 $$x$$ 위의 fiber $$E_x$$의 ordered basis들, 즉 *frame* 전체로 이루어진 공간

$$\Fr(E)=\{(x,b)\mid x\in X,b\text{ an ordered basis of $E_x$}\}$$

는 기저를 행렬로 보내는 $$\GL(n;\mathbb{R})$$의 작용에 대하여 principal $$\GL(n;\mathbb{R})$$-bundle이 되며, 이를 $$E$$의 *frame bundle*이라 한다. 다음 명제는 이 두 구성이 서로 역과정임을 보여준다. 

::: 명제 4
위상공간 $$X$$ 위에서, principal $$\GL(n;\mathbb{R})$$-bundle들의 isomorphism class와 rank $$n$$ real vector bundle들의 isomorphism class 사이에는 자연스러운 일대일 대응이 존재한다. 이 대응은 principal bundle $$P$$에 associated bundle $$P\times_{\GL(n;\mathbb{R})}\mathbb{R}^n$$을, vector bundle $$E$$에 frame bundle $$\Fr(E)$$를 대응시킨다.
:::
::: 증명
두 대응이 서로 역임을 확인하면 된다. 

우선 정의에 의해 frame bundle $$\Fr(E)$$의 한 점은 fiber $$E_x$$의 한 ordered basis와 같으며, 이는 정확히 standard Euclidean space $$\mathbb{R}^n$$의 각 standard basis가 어디로 가는지를 보면 되므로 linear isomorphism $$b:\mathbb{R}^n\rightarrow E_x$$와 정확히 같은 정보량을 가진다. 이렇게 정의된 사상

$$\Fr(E)\times_{\GL(n;\mathbb{R})}\mathbb{R}^n\rightarrow E,\qquad [(b,v)]\mapsto b(v)$$

는 잘 정의되는데, $$(b,v)$$를 $$(b\circ A, A^{-1}v)$$로 바꾸어도 $$(b\circ A)(A^{-1}v)=b(v)$$로 같은 값을 주기 때문이다. 이 사상은 각 fiber 위에서 선형동형이므로 vector bundle의 isomorphism이다. 

거꾸로 principal bundle $$P$$에서 출발하면, $$P\times_G\mathbb{R}^n$$의 frame bundle이 다시 $$P$$와 동형임을 local trivialization 위에서 transition function $$g_{ij}$$가 양쪽에서 일치함을 통해 확인할 수 있다. 

두 구성 모두 transition function을 보존하므로 isomorphism class를 보존하고, 사상의 naturality는 pullback과의 호환에서 따라온다.
:::

이 동치 덕분에 vector bundle에 대한 모든 분류 문제는 principal $$\GL(n;\mathbb{R})$$-bundle에 대한 문제로 번역된다. 같은 방식으로 complex vector bundle은 principal $$\GL(n;\mathbb{C})$$-bundle에, oriented real vector bundle은 principal $$\GL^+(n,\mathbb{R})$$-bundle에 대응한다. 따라서 임의의 구조군 $$G$$에 대하여 principal $$G$$-bundle을 분류할 수 있다면, 이 모든 경우가 한꺼번에 해결된다.

Vector bundle에서와 마찬가지로, 연속함수 $$f:X'\rightarrow X$$와 principal $$G$$-bundle $$p:P\rightarrow X$$가 주어지면 *pullback bundle*

$$f^\ast P=\{(x',y)\in X'\times P\mid f(x')=p(y)\}$$

이 정의된다. 여기에 $$(x',y)\cdot g=(x',y\cdot g)$$로 작용을 주면 $$f^\ast P\rightarrow X'$$은 다시 principal $$G$$-bundle이 되며, 이는 transition function의 관점에서는 $$g_{ij}$$를 $$g_{ij}\circ f$$로 끌어당기는 것에 해당한다. 핵심적인 사실은 이 pullback이 $$f$$의 homotopy class에만 의존한다는 사실이다.

::: 정리 5 (Pullback의 homotopy 불변성)
$$X$$가 paracompact이고 $$f_0,f_1:X\rightarrow Y$$가 homotopic이라 하자. ([§호모토피, ⁋정의 2](/ko/math/algebraic_topology/homotopy#def2)) 그럼 임의의 principal $$G$$-bundle $$p:P\rightarrow Y$$에 대하여 $$f_0^\ast P$$와 $$f_1^\ast P$$는 $$X$$ 위에서 isomorphic하다.
:::
::: 증명
핵심은 다음의 사실이다. 

> $$X$$가 paracompact일 때, $$X\times[0,1]$$ 위의 principal $$G$$-bundle $$Q$$는 $$X\times\{0\}$$으로의 제한을 projection $$X\times[0,1]\rightarrow X\times\{0\}$$으로 pullback한 것과 isomorphic하다.

이는 bundle의 covering homotopy property로, paracompact base 위의 trivializing cover가 locally finite partition of unity를 갖는다는 사실에 따른 것이다. 증명의 골자는 $$[0,1]$$을 작은 구간들로 나누어 각 구간 위에서 trivialization을 잇고, partition of unity로 이 local isomorphism들을 붙이는 것이다. 

이제 homotopy $$H:X\times[0,1]\rightarrow Y$$가 $$f_0,f_1$$을 잇는다 하고 $$Q=H^\ast P$$로 정의하자. 위 사실에 의해 $$Q$$는 $$Q\vert_{X\times\{0\}}=f_0^\ast P$$를 projection으로 끌어당긴 것과 isomorphic하고, 같은 논증을 $$X\times\{1\}$$ 끝에서 반복하면 $$Q\vert_{X\times\{1\}}=f_1^\ast P$$ 역시 같은 bundle과 isomorphic이다. 
:::

특히 $$X$$가 contractible이면 항등사상이 상수사상과 homotopic하므로 $$X$$ 위의 모든 principal $$G$$-bundle은 trivial이다. 일반적으로 CW complex는 항상 paracompact이므로 우리가 다루려는 base들에 대해서는 위 정리의 가정이 자동으로 성립한다.

## Universal bundle과 classifying space

[정리 5](#thm5)는 함수 $$f$$를 $$f^\ast P$$로 대응시키는 것이 $$f$$의 homotopy class에만 의존함을 말해 준다. 따라서, 만일 어떤 고정된 principal $$G$$-bundle 하나를 모든 다른 bundle이 pullback으로 얻을 수 있는 원천으로 삼을 수 있다면, principal $$G$$-bundle의 분류는 그 원천 공간으로의 homotopy class를 세는 일로 환원될 것이며, 이는 vector bundle에서 $$\Gr(k,\mathbb{R}^\infty)$$ 위의 universal bundle이 그러한 원천이었던 것을 일반화한다.

::: 정의 6
Topological group $$G$$에 대하여, principal $$G$$-bundle $$p:EG\rightarrow BG$$가 *universal bundle*이라는 것은 total space $$EG$$가 contractible인 것, 곧 $$EG$$가 한 점과 homotopy equivalent인 것이다. ([§호모토피, ⁋정의 4](/ko/math/algebraic_topology/homotopy#def4)) 이때 base space $$BG$$를 $$G$$의 *classifying space<sub>분류공간</sub>*라 부른다.
:::

즉, universal $$G$$-bundle은 contractible space 위의 free $$G$$-action이며, 그 orbit space $$BG=EG/G$$가 base space이며, 여기로의 projection map이 bundle map이다. $$EG$$가 contractible이라는 조건은 [정리 8](#thm8)에서 중요하게 사용될 것이다. 그 전에, 우선 다음이 성립한다. 

::: 정리 7 (Milnor)
임의의 topological group $$G$$에 대하여 universal bundle $$EG\rightarrow BG$$가 존재한다.
:::
이에 대한 증명은 $$G$$의 무한 join 

$$EG=G\ast G\ast G\ast\cdots$$

를 사용하며, 이 공간은 임의의 $$n$$에 대해 $$n$$-connected이고, 따라서 weakly contractible이 되며 CW 구조 하에서 contractible이라는 것이 요지이다. 자세한 내용은 [Mil]에 맡겨둔다.

한편, universal bundle은 본질적으로 유일하다. 두 universal bundle $$EG\rightarrow BG$$와 $$EG'\rightarrow BG'$$이 주어지면, $$EG'$$이 contractible이므로 [정리 5](#thm5)에 의해 $$BG$$로 끌어내린 분류사상이 존재하고, 이 논증을 양방향으로 적용하면 $$BG$$와 $$BG'$$이 서로 homotopy inverse인 사상으로 연결되기 때문이다. 따라서 $$BG$$는 homotopy equivalence를 넘어서는 모호함 없이 결정되며, 우리는 $$BG$$를 *the* classifying space라 부른다.

그럼 이 글의 가장 핵심적인 결과는, 당연히 다음의 정리이다.

::: 정리 8 (분류정리)
Paracompact space $$X$$와 topological group $$G$$에 대하여, $$[X,BG]$$를 $$X$$에서 $$BG$$로의 free homotopy class들의 집합이라 하자. 그럼 universal bundle $$EG\rightarrow BG$$를 pullback하는 사상

$$[X,BG]\rightarrow\{\text{principal $G$-bundles over $X$}\}/{\cong};\qquad [f]\mapsto f^\ast EG$$

은 잘 정의된 전단사이며, 사상 $$X'\rightarrow X$$에 대한 pullback과 호환된다는 의미에서 자연스럽다.

![분류사상의 pullback 사각형](/assets/images/Math/Algebraic_Topology/Classifying_Spaces-1.svg){:style="width:8.21em" class="invert" .align-center}

:::
::: 증명
$$[f]\mapsto f^\ast EG$$가 $$[f]$$의 대표 선택에 의존하지 않는 것은 [정리 5](#thm5)에 의한 것이다. 우리는 이것이 전단사임을 간략히 살펴본다.

우선 $$X$$ 위의 principal $$G$$-bundle $$P$$가 주어졌다 하자. $$X$$가 paracompact이므로, [\[위상수학\] §옹골성, ⁋정리 27](/ko/math/topology/compactness#thm27)에 의하여 $$P$$를 trivialize하는 open cover $$\{U_i\}$$와 이에 종속된 locally finite partition of unity $$\{\rho_i\}$$를 함께 잡을 수 있다. 각 $$U_i$$ 위의 trivialization은 $$G$$-equivariant map $$\psi_i:p^{-1}(U_i)\rightarrow G$$를 주므로,

$$\widetilde{f}:P\rightarrow EG,\qquad y\mapsto \sum_i \rho_i(p(y))\psi_i(y)$$

는 잘 정의된 $$G$$-equivariant map이다. 이 때 $$G$$-equivariant map은 base space 사이의 사상 $$f:X\rightarrow BG$$로 내려가고, $$\widetilde{f}$$가 fiber마다 동형이므로 $$P\cong f^\ast EG$$를 얻는다.

이제 injectivity를 보이기 위해 $$f_0,f_1:X\rightarrow BG$$에 대하여 $$f_0^\ast EG\cong f_1^\ast EG=:P$$라 하자. 우리는 $$f_0$$과 $$f_1$$이 homotopic한 것을 보여야 한다. 각 $$f_i$$는 bundle map $$P\cong f_i^\ast EG\rightarrow EG$$, 곧 $$P$$에서 universal bundle로 가는 $$G$$-equivariant bundle map $$\Phi_i:P\rightarrow EG$$을 가진다. 그런데 $$EG$$가 contractible이므로, paracompact 공간 위의 principal bundle $$P$$에서 $$EG$$로 가는 임의의 두 $$G$$-equivariant map은 서로 $$G$$-equivariant homotopic하며, 따라서 $$\Phi_0$$과 $$\Phi_1$$을 잇는 $$G$$-equivariant homotopy $$P\times[0,1]\rightarrow EG$$가 존재하고, 이것이 base로 내려가 $$f_0$$과 $$f_1$$ 사이의 homotopy를 주므로 $$[f_0]=[f_1]$$이다. 
:::

이 정리는 principal $$G$$-bundle의 기하학적 분류를 순수하게 homotopy의 데이터 $$[X,BG]$$로 옮긴다. [명제 4](#prop4)와 결합하면 rank $$n$$ real vector bundle의 분류가 $$[X,B\GL(n;\mathbb{R})]$$로, complex의 경우 $$[X,B\GL(n;\mathbb{C})]$$로 옮겨지게 되며, 실제로 이들 $$B\GL(n; \mathbb{R})$$과 $$B\GL(n; \mathbb{C})$$이 실은 (real/complex) Grassmannian인 것을 곧 살펴보게 될 것이다. 

::: 보조정리 9
Classifying space의 구성은 $$G$$에 대해 functorial이다. 연속적인 group homomorphism $$\phi:G\rightarrow H$$가 주어지면, $$EG$$ 위의 $$G$$-작용을 $$\phi$$를 통해 $$H$$-작용으로 바꾸어 얻는 associated bundle $$EG\times_G H$$를 분류하는 사상이 $$B\phi:BG\rightarrow BH$$를 유도한다. 이는 $$B(\psi\circ\phi)\simeq B\psi\circ B\phi$$를 만족하여, $$G\mapsto BG$$가 homotopy category 위의 functor가 되게 한다. 가령 inclusion $$\Umat(n)\hookrightarrow\GL(n;\mathbb{C})$$이 유도하는 $$B\Umat(n)\rightarrow B\GL(n;\mathbb{C})$$이 아래에서 쓰인다.
:::

## 분류공간의 예

현실적으로, 이 글에서 가장 유용한 부분은 존재성보다도 이 분류공간들이 어떻게 주어지는지에 대한 것이다. 가장 단순한 경우는 다음과 같다. 

::: 예시 10
$$G$$가 discrete group이라 하자. 그럼 임의의 base $$B$$ 위에 정의된 principal $$G$$-bundle은 그 fiber가 discrete이므로 $$B$$ 위의 covering space가 된다. 그럼 이 이해에서 $$G$$의 right action은 Deck transformation이 되며, fiber 위에서 Deck group이 transitive하게 작용하므로 이 covering space는 *regular* covering space이다. 

이제 이를 universal bundle $$EG \rightarrow BG$$에 적용하자. 그럼 [§피복공간, ⁋따름정리 12](/ko/math/algebraic_topology/covering_spaces#cor12)에 의해 이 covering space의 Deck transformation group은 $$\pi_1(BG)$$와 isomorphic한데, 우리는 앞서 이 Deck group이 곧 $$G$$가 되어야 하는 것을 살펴보았으므로 $$\pi_1(BG)\cong G$$이고, $$EG$$가 contractible이라 $$BG$$의 universal cover 또한 contractible이므로 $$\pi_n(BG)=0$$ ($$n\geq 2$$) 이다. 곧 $$BG$$는 Eilenberg–MacLane 공간 $$K(G,1)$$이다.

더 구체적인 예시로 $$G=\mathbb{Z}/2$$인 경우와 $$G=\mathbb{Z}$$인 경우를 각각 보자. 우선 $$\mathbb{Z}/2$$의 경우 우리는 $$\mathbb{Z}/2$$이 free하게 작용하는 contractible space를 찾아야 하는데, $$S^\infty$$에 antipodal action을 준 게 정확히 이 두 조건을 모두 만족한다. 그럼 이 action의 orbit space는 $$\RP^\infty$$가 된다. $$\mathbb{Z}$$의 경우도 이미 우리와 친숙한 예시에서 찾아올 수 있는데, 바로 [§피복공간, ⁋정의 3](/ko/math/algebraic_topology/covering_spaces#def3) 직후에 covering space의 표준적인 예시로 소개한 $$\mathbb{R}\rightarrow S^1$$이 그러하다. 
:::

이제 실제로 우리가 관심있는 group들의 covering space들을 살펴보자. Discrete이 아닌 group 중 가장 기본적인 예는 $$G=S^1$$이며 이는 보편적으로 $$\mathbb{C}^\times$$에 들어있는 길이 $$1$$짜리 복소수들 $$e^{2\pi it}$$들의 모임으로 생각한다. 그럼 $$S^1$$은 $$\mathbb{C}^\infty\setminus\{0\}$$ 위에 스칼라곱으로 free하게 작용한다. 각 $$\mathbb{C}^n\setminus\{0\}$$은 radial deformation retract로 단위구면 $$S^{2n-1}\subseteq\mathbb{C}^n\cong\mathbb{R}^{2n}$$과 같은 호모토피형이며, 표준 inclusion $$\mathbb{C}^n\hookrightarrow\mathbb{C}^{n+1}$$이 equator inclusion $$S^{2n-1}\hookrightarrow S^{2n+1}$$을 유도하므로 $$\mathbb{C}^\infty\setminus\{0\}$$는 그 colimit $$S^\infty=\varinjlim_n S^{2n-1}$$로 deformation retract된다. 유한 차원 구면과 달리 이 colimit은 shift 사상 $$(x_1,x_2,\ldots)\mapsto(0,x_1,x_2,\ldots)$$이 항등사상과 homotopic이라 한 점으로 수축하므로 contractible이고, 따라서 $$ES^1=\mathbb{C}^\infty\setminus\{0\}$$이며 그 orbit space는 복소 직선들의 공간

$$BS^1=(\mathbb{C}^\infty\setminus\{0\})/S^1=\CP^\infty$$

이다. 한편 $$\CP^\infty=\Gr_1(\mathbb{C}^\infty)$$은 $$\Umat(1)=S^1$$의 분류공간으로 앞 글에서 $$B\Umat(1)$$이라 적은 바로 그 공간이며, 따라서 $$BS^1=B\Umat(1)=\CP^\infty$$이다. 더 일반적으로 $$n$$차원 torus $$T=(S^1)^n$$에 대해서는 곱이 분류공간의 곱으로 가므로

$$BT=B(S^1)^n=(\CP^\infty)^n$$

이다. 같은 방식으로 임의의 $$n$$에 대하여 unitary group과 orthogonal group의 분류공간은 앞 글의 infinite Grassmannian으로 실현된다. 즉 $$B\Umat(n)=\Gr(n,\mathbb{C}^\infty)$$이고 $$B\Omat(n)=\Gr(n,\mathbb{R}^\infty)$$인데, 이는 $$\Gr(n,\mathbb{C}^\infty)$$ 위의 universal vector bundle의 frame bundle이 universal principal $$\Umat(n)$$-bundle을 주고 그 total space (Stiefel 공간의 colimit) 가 contractible이기 때문이다.

마지막으로 일반선형군과 그 maximal compact subgroup의 분류공간이 같은 homotopy type을 갖는다는 사실은 분류 이론에서 자주 쓰인다.

::: 예시 11
Inclusion $$\Umat(n)\hookrightarrow\GL(n;\mathbb{C})$$은 homotopy equivalence

$$B\Umat(n)\xrightarrow{\ \simeq\ }B\GL(n;\mathbb{C})$$

를 유도한다. 이는 Gram–Schmidt 직교화가 $$\GL(n;\mathbb{C})$$을 $$\Umat(n)$$ 위로 deformation retract시키는 데서 나온다. 구체적으로 $$\GL(n;\mathbb{C})$$의 임의의 행렬은 unitary 행렬과 양의 정부호 upper-triangular 행렬의 곱으로 유일하게 분해되고($$QR$$ 분해), upper-triangular 인자를 항등원 쪽으로 연속적으로 수축시키면 $$\GL(n;\mathbb{C})$$이 $$\Umat(n)$$으로 deformation retract됨을 얻는다. Group 수준의 이 homotopy equivalence가 $$B$$를 거쳐 분류공간 수준의 homotopy equivalence를 준다. 따라서 rank $$n$$ complex vector bundle은 그 구조군을 $$\GL(n;\mathbb{C})$$에서 $$\Umat(n)$$으로 줄여도 분류에 손실이 없으며, 이것이 모든 complex bundle에 Hermitian metric을 줄 수 있다는 사실의 분류공간 판본이다.
:::

## 분류공간의 코호몰로지

분류정리에 따르면 구조군 $$G$$를 갖는 bundle의 특성류란 $$BG$$의 cohomology class를 분류사상으로 pullback한 것이다. 따라서 특성류 이론은 $$BG$$의 cohomology ring을 계산하는 일과 같으며, 우리는 가장 기본적인 군들에 대해 이를 정리한다.

출발점은 complex projective space의 cohomology ring이다. 앞 글에서 우리는

$$H^\bullet(\CP^\infty;\mathbb{Z})=\mathbb{Z}[x],\qquad \lvert x\rvert=2$$

임을 보았으며, 생성원 $$x$$는 tautological line bundle의 first Chern class였다. ([§벡터다발의 특성류, ⁋예시 8](/ko/math/algebraic_topology/characteristic_classes#ex8)) $$BS^1=\CP^\infty$$이므로 이는 곧

$$H^\bullet(BS^1;\mathbb{Z})=\mathbb{Z}[t],\qquad \lvert t\rvert=2$$

를 뜻한다. Torus의 경우는 곱공간의 cohomology로부터 따라온다.

::: 따름정리 12
$$n$$차원 torus $$T=(S^1)^n$$에 대하여

$$H^\bullet(BT;\mathbb{Z})=\mathbb{Z}[t_1,\ldots,t_n],\qquad \lvert t_i\rvert=2$$

는 $$n$$개의 degree $$2$$ 생성원으로 이루어진 polynomial ring이다. 더 나아가 degree $$2$$ 부분 $$H^2(BT;\mathbb{Z})$$은 character lattice $$\Hom(T,S^1)$$과 표준적으로 동형이며, $$H^\bullet(BT;\mathbb{Z})$$은 이 lattice 위의 symmetric algebra이다.
:::
::: 증명
$$BT=(\CP^\infty)^n$$이고, 앞 절의 $$BS^1=\CP^\infty$$ 계산으로부터 각 인자의 cohomology $$H^\bullet(\CP^\infty;\mathbb{Z})=\mathbb{Z}[t_i]$$는 각 차수에서 free abelian group이므로 Künneth 정리에 Tor 항이 나타나지 않는다. 따라서 cross product가 cohomology ring의 동형

$$H^\bullet(BT;\mathbb{Z})\cong\bigotimes_{i=1}^n \mathbb{Z}[t_i]=\mathbb{Z}[t_1,\ldots,t_n]$$

을 준다. ([§합곱](/ko/math/algebraic_topology/cup_products)) Character $$\chi:T\rightarrow S^1$$은 $$B\chi:BT\rightarrow BS^1=\CP^\infty$$을 유도하고 ([보조정리 9](#lem9)) $$B\chi^\ast(t)\in H^2(BT;\mathbb{Z})$$를 대응시키는데, $$i$$번째 좌표 projection $$T\rightarrow S^1$$이 $$t_i$$로 가므로 이 대응은 $$\Hom(T,S^1)\cong\mathbb{Z}^n$$을 $$H^2(BT;\mathbb{Z})=\bigoplus_i\mathbb{Z}t_i$$로 보내는 동형이다. Polynomial ring은 그 degree $$2$$ 부분 위의 symmetric algebra이므로 마지막 주장이 따라온다.
:::

이 동형은 character lattice 위의 다항식을 $$BT$$의 cohomology class로 읽게 해 주며, torus가 작용하는 공간의 불변량을 다룰 때 핵심이 된다. Unitary group의 경우는 한 단계 더 나아간 계산이 필요하지만, 앞 글에서 이미 그 결과를 보았다.

::: 명제 13
Unitary group $$\Umat(n)$$에 대하여

$$H^\bullet(B\Umat(n);\mathbb{Z})=\mathbb{Z}[c_1,\ldots,c_n],\qquad \lvert c_i\rvert=2i$$

는 universal complex bundle의 Chern class $$c_i$$들로 생성되는 polynomial ring이다.
:::
::: 증명
$$B\Umat(n)=\Gr_n(\mathbb{C}^\infty)$$이고, 그 cohomology ring이 universal bundle의 Chern class들로 생성되는 polynomial ring

$$H^\bullet(\Gr_n(\mathbb{C}^\infty);\mathbb{Z})=\mathbb{Z}[c_1,\ldots,c_n]$$

임은 앞 글에서 진술하였다. ([§벡터다발의 특성류](/ko/math/algebraic_topology/characteristic_classes)) 그 증명의 골자는 maximal torus $$T\subset\Umat(n)$$이 유도하는 사상 $$BT\rightarrow B\Umat(n)$$이 cohomology 위에서 Weyl group $$S_n$$의 작용에 대한 불변량으로의 단사를 주고, [따름정리 12](#cor12)의 $$\mathbb{Z}[t_1,\ldots,t_n]$$ 안에서 $$S_n$$-불변 부분이 elementary symmetric polynomial들이 생성하는 $$\mathbb{Z}[c_1,\ldots,c_n]$$이라는 데 있다. 이때 $$c_i$$는 $$t_1,\ldots,t_n$$의 $$i$$번째 elementary symmetric polynomial로 표현되며, 이것이 splitting principle에서 Chern class를 Chern root로 분해하던 식과 같다. 완전한 계산은 [MS]의 §14를 따른다.
:::

이렇게 $$B\Umat(n)$$의 cohomology가 Chern class들의 다항식 전부로 이루어지므로, complex vector bundle의 모든 특성류는 Chern class의 다항식이다. 같은 방식으로 $$H^\bullet(B\Omat(n);\mathbb{Z}/2)=\mathbb{Z}/2[w_1,\ldots,w_n]$$이 Stiefel–Whitney class를 분류하며, oriented bundle에 대해서는 $$B\SO(n)$$의 cohomology에서 Euler class가 나타난다. 한 공간 $$X$$ 대신 $$G$$-작용을 갖는 공간을 다룰 때, $$BG$$와 그 위에서의 homotopy quotient는 이 cohomology를 base로 삼는 equivariant cohomology의 토대가 된다.

---

**참고문헌**

**[Mil]** J. W. Milnor, *Construction of universal bundles, II*, Annals of Mathematics **63** (1956), 430–436.

**[MS]** J. W. Milnor and J. D. Stasheff, *Characteristic Classes*, Annals of Mathematics Studies 76, Princeton University Press, 1974.

**[Hat]** A. Hatcher, *Algebraic Topology*, Cambridge University Press, 2002.

**[tD]** T. tom Dieck, *Algebraic Topology*, EMS Textbooks in Mathematics, European Mathematical Society, 2008.

**[Hus]** D. Husemoller, *Fibre Bundles*, 3rd ed., Graduate Texts in Mathematics 20, Springer, 1994.
