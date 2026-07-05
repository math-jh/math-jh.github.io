---
title: "분류공간"
description: "임의의 topological group을 구조군으로 갖는 principal bundle을 정의하고, universal bundle과 classifying space를 통해 이들을 homotopy 이론으로 분류한다."
excerpt: "Principal G-bundle의 분류와 classifying space BG의 구성"

categories: [Math / Algebraic Topology]
permalink: /ko/math/algebraic_topology/classifying_spaces
sidebar: 
    nav: "algebraic_topology-ko"

date: 2026-07-01
last_modified_at: 2026-07-01
weight: 12

published: false

---

앞선 글에서 우리는 vector bundle의 분류 문제를 다루었다. 임의의 위상공간 $$B$$ 위의 rank $$k$$ 실 vector bundle은 infinite Grassmannian $$\Gr_k(\mathbb{R}^\infty)$$ 위의 universal bundle을 pullback하여 얻어지며, 따라서 그 isomorphism class는 homotopy class $$[B, \Gr_k(\mathbb{R}^\infty)]$$와 일대일 대응하였다. 한편 이 분류는 또 다른 모습으로도 나타났는데, rank $$k$$ vector bundle은 open cover $$\{U_i\}$$ 위에서 transition function

$$g_{ij}:U_i\cap U_j \rightarrow \mathrm{GL}(k,\mathbb{R})$$

들이 cocycle 조건을 만족하도록 주어지는 데이터와 같았고, 따라서 그 isomorphism class들은 $$\mathrm{GL}(k,\mathbb{R})$$에 값을 갖는 Čech cohomology $$\check{H}^1(B;\mathrm{GL}(k,\mathbb{R}))$$가 분류하였다. ([§슈티펠-휘트니 특성류, ⁋정의 2](/ko/math/algebraic_topology/stiefel_whitney_classes#def2))

이 두 그림은 본질적으로 같은 현상을 말한다. 즉 transition function이 어떤 위상군 $$G$$에 값을 가지면, 그 bundle은 $$G$$를 구조군으로 갖는 것이고, 이러한 bundle은 $$G$$에만 의존하는 하나의 공간으로 분류된다. Vector bundle의 경우 $$G=\mathrm{GL}(k,\mathbb{R})$$이었고 그 공간이 $$\Gr_k(\mathbb{R}^\infty)$$이었던 것이다. 이번 글의 목표는 임의의 topological group $$G$$에 대하여 이 분류를 통일적으로 수행하는 것이다. 이를 위해 우리는 우선 구조군 $$G$$만을 데이터로 갖는 *principal $$G$$-bundle*을 정의하고, 모든 principal $$G$$-bundle을 분류하는 단 하나의 공간 *classifying space* $$BG$$를 구성한다. 앞으로 $$G$$는 항상 topological group을 의미하며, 별다른 언급이 없는 한 base space는 paracompact인 것으로 가정한다.

## Principal bundle의 정의

Vector bundle의 fiber에는 벡터공간 구조가 있었고, 그 transition function은 이 구조를 보존하는 선형동형, 곧 $$\mathrm{GL}(k,\mathbb{R})$$의 원소들이었다. 일반적인 구조군 $$G$$를 다룰 때는 fiber 자체를 $$G$$로 두고, transition을 $$G$$의 left translation으로 주는 것이 자연스럽다. 다만 fiber $$G$$ 위에는 어느 점도 특별하지 않으므로, 이 데이터를 좌표에 의존하지 않고 기술하기 위해 우리는 total space 위의 $$G$$-작용을 사용한다.

::: 정의 1
Topological group $$G$$에 대하여, fiber bundle $$p:P\rightarrow X$$와 그 위의 연속적인 right action $$P\times G\rightarrow P$$가 주어졌다 하자. 이 데이터가 *principal $$G$$-bundle<sub>주다발</sub>*이라는 것은 다음 세 조건이 성립하는 것이다.

1. $$G$$-작용은 fiber를 보존한다. 즉 모든 $$y\in P$$와 $$g\in G$$에 대하여 $$p(y\cdot g)=p(y)$$이다.
2. 각 fiber 위에서 $$G$$-작용은 free이고 transitive하다. 즉 임의의 $$x\in X$$에 대하여, 한 점 $$y\in p^{-1}(x)$$를 고정하면 $$g\mapsto y\cdot g$$가 $$G$$에서 $$p^{-1}(x)$$로의 전단사이다.
3. ($$G$$-equivariant local triviality) 각 $$x\in X$$마다 열린 이웃 $$U$$와, $$U$$ 위에서 $$p$$와 호환되는 homeomorphism $$\varphi:p^{-1}(U)\rightarrow U\times G$$가 존재하여, $$G$$-equivariant이다. 여기서 $$U\times G$$ 위의 $$G$$-작용은 $$(u,h)\cdot g=(u,hg)$$로 둔다.
:::

조건 (3)은 국소적으로 $$P$$가 $$U\times G$$와 같고, 그 위의 $$G$$-작용은 두 번째 좌표의 right translation임을 말한다. 조건 (2)에서 $$G$$-작용이 각 fiber 위에서 simply transitive하므로, fiber $$p^{-1}(x)$$는 $$G$$와 위상동형이지만 항등원에 해당하는 표준적인 점을 갖지 않는 *torsor*이다. 가장 단순한 예는 $$X\times G$$에 $$(x,h)\cdot g=(x,hg)$$로 작용을 준 *trivial bundle*이며, 이는 항등원으로 이루어진 표준적인 section $$x\mapsto(x,e)$$를 갖는다.

두 principal $$G$$-bundle $$P,P'\rightarrow X$$ 사이의 *morphism over $$X$$*는 $$p'\circ f=p$$를 만족하고 $$G$$-작용과 호환되는 ($$f(y\cdot g)=f(y)\cdot g$$) 연속함수 $$f:P\rightarrow P'$$를 뜻하며, 이것이 homeomorphism이면 *isomorphism*이라 부른다. 국소 trivialization $$\varphi_i:p^{-1}(U_i)\rightarrow U_i\times G$$들을 고정하면, $$U_i\cap U_j$$ 위에서 $$\varphi_i\circ\varphi_j^{-1}(u,h)=(u,g_{ij}(u)h)$$를 만족하는 연속함수 $$g_{ij}:U_i\cap U_j\rightarrow G$$가 결정된다. 이 transition function들은 vector bundle에서와 같은 cocycle 조건

$$g_{ij}(x)g_{jk}(x)=g_{ik}(x),\qquad g_{ii}(x)=e$$

를 만족하며, 두 cocycle $$(g_{ij})$$와 $$(g_{ij}')$$이 같은 bundle을 주는 것은 연속함수 $$\lambda_i:U_i\rightarrow G$$들이 존재하여 $$g_{ij}'=\lambda_i g_{ij}\lambda_j^{-1}$$인 것과 동치이다. 따라서 open cover $$\{U_i\}$$ 위에서 trivialize되는 principal $$G$$-bundle의 isomorphism class들은 nonabelian Čech cohomology $$\check{H}^1(X;G)$$로 분류되며, $$G=\mathrm{GL}(k,\mathbb{R})$$인 경우 이는 앞 글의 vector bundle 분류와 정확히 일치한다.

Vector bundle은 언제나 zero section을 가졌으나, principal bundle은 그렇지 않다. 실제로 section의 존재 여부가 principal bundle의 자명성을 완전히 결정한다.

::: 명제 2
Principal $$G$$-bundle $$p:P\rightarrow X$$가 trivial bundle과 isomorphic한 것은 연속적인 global section $$s:X\rightarrow P$$가 존재하는 것과 동치이다.
:::
::: 증명
Trivial bundle $$X\times G$$는 $$x\mapsto(x,e)$$라는 section을 가지므로, $$P$$가 trivial이면 isomorphism을 통해 section을 얻는다. 역으로 section $$s:X\rightarrow P$$가 존재한다 하자. 그럼 다음의 함수

$$\Phi:X\times G\rightarrow P,\qquad (x,g)\mapsto s(x)\cdot g$$

를 생각한다. 각 fiber 위에서 $$G$$-작용이 simply transitive ([정의 1](#def1)의 조건 (2)) 하므로 $$\Phi$$를 fiber $$\{x\}\times G\rightarrow p^{-1}(x)$$로 제한한 것은 전단사이고, 따라서 $$\Phi$$는 전단사이다. $$\Phi$$는 정의에 의해 $$p\circ\Phi=\mathrm{pr}_1$$을 만족하고 $$G$$-작용과 호환되므로 morphism over $$X$$이다. 마지막으로 $$\Phi$$가 homeomorphism임은 국소적으로 확인하면 되는데, trivialization $$\varphi:p^{-1}(U)\rightarrow U\times G$$ 위에서 $$s$$가 $$x\mapsto(x,\sigma(x))$$의 꼴로 쓰이면 ($$\sigma:U\rightarrow G$$ 연속) $$\Phi$$는 $$(x,g)\mapsto(x,\sigma(x)g)$$가 되어 그 역 $$(x,h)\mapsto(x,\sigma(x)^{-1}h)$$이 연속이기 때문이다.
:::

이 명제는 principal bundle과 vector bundle의 결정적인 차이를 드러낸다. Section의 존재가 곧 자명성이므로, nontrivial principal bundle은 어떠한 연속 section도 갖지 않는다. 가령 quotient map $$S^n\rightarrow \RP^n$$은 $$\mathbb{Z}/2$$의 free action에 대한 principal $$\mathbb{Z}/2$$-bundle인데, $$S^n$$이 connected이므로 ($$n\geq 1$$) 두 장의 sheet를 연속적으로 고르는 section은 존재할 수 없고, 따라서 이 bundle은 nontrivial이다.

## 수반다발

Principal $$G$$-bundle은 그 자체로는 fiber가 $$G$$이지만, 여기에 $$G$$가 작용하는 임의의 공간을 fiber로 갖는 bundle을 만들어 붙일 수 있다. 이 구성이 principal bundle을 모든 종류의 bundle의 공통 원천으로 만들어 준다.

::: 정의 3
Principal $$G$$-bundle $$p:P\rightarrow X$$와, $$G$$가 왼쪽에서 연속적으로 작용하는 위상공간 $$F$$ (이를 *$$G$$-space*라 한다) 가 주어졌다 하자. 곱공간 $$P\times F$$ 위에 $$G$$-작용을

$$(y,f)\cdot g=(y\cdot g,\ g^{-1}\cdot f)$$

로 정의하고, 그 orbit space를 $$P\times_G F=(P\times F)/G$$로 적는다. 그럼 $$(y,f)\mapsto p(y)$$가 유도하는 사상 $$P\times_G F\rightarrow X$$는 fiber $$F$$를 갖는 fiber bundle이며, 이를 $$P$$의 *associated bundle<sub>수반다발</sub>*이라 부른다.
:::

$$P$$가 $$\{U_i\}$$ 위에서 transition function $$g_{ij}$$로 주어지면, $$P\times_G F$$는 같은 $$U_i$$ 위에서 $$F$$를 fiber로 하고 transition이 $$g_{ij}$$의 $$F$$ 위에서의 작용으로 주어지는 bundle이 된다. 특히 $$F$$가 벡터공간이고 $$G$$가 선형으로 작용하면 associated bundle은 vector bundle이다. 가장 중요한 경우는 $$G=\mathrm{GL}(n,\mathbb{R})$$이 $$F=\mathbb{R}^n$$에 표준적으로 작용하는 경우로, 이때 $$P\times_G \mathbb{R}^n$$은 rank $$n$$ vector bundle이다. 역방향의 구성도 가능하다. Rank $$n$$ vector bundle $$E\rightarrow X$$가 주어지면, 각 $$x$$ 위의 fiber $$E_x$$의 순서기저(frame) 전체로 이루어진 공간

$$\mathrm{Fr}(E)=\{(x,b)\mid x\in X,\ b\ \text{는}\ E_x\ \text{의 순서기저}\}$$

는 기저를 행렬로 보내는 $$\mathrm{GL}(n,\mathbb{R})$$의 작용에 대하여 principal $$\mathrm{GL}(n,\mathbb{R})$$-bundle이 되며, 이를 $$E$$의 *frame bundle*이라 한다. 이 두 구성은 서로 역이다.

::: 명제 4
위상공간 $$X$$ 위에서, principal $$\mathrm{GL}(n,\mathbb{R})$$-bundle들의 isomorphism class와 rank $$n$$ 실 vector bundle들의 isomorphism class 사이에는 자연스러운 일대일 대응이 존재한다. 이 대응은 principal bundle $$P$$에 associated bundle $$P\times_{\mathrm{GL}(n,\mathbb{R})}\mathbb{R}^n$$을, vector bundle $$E$$에 frame bundle $$\mathrm{Fr}(E)$$를 대응시킨다.
:::
::: 증명
두 대응이 서로 역임을 확인하면 된다. Frame bundle $$\mathrm{Fr}(E)$$의 한 점은 fiber $$E_x$$의 기저, 곧 선형동형 $$b:\mathbb{R}^n\xrightarrow{\cong}E_x$$이다. 그럼 사상

$$\mathrm{Fr}(E)\times_{\mathrm{GL}(n,\mathbb{R})}\mathbb{R}^n\rightarrow E,\qquad [(b,v)]\mapsto b(v)$$

는 잘 정의된다. $$(b,v)$$를 $$(b\circ A, A^{-1}v)$$로 바꾸어도 $$b(Av\cdot A^{-1})$$ 꼴이 아니라 $$(b\circ A)(A^{-1}v)=b(v)$$로 같은 값을 주기 때문이다. 이 사상은 각 fiber 위에서 선형동형이므로 vector bundle의 isomorphism이다. 거꾸로 principal bundle $$P$$에서 출발하면, $$P\times_G\mathbb{R}^n$$의 frame bundle이 다시 $$P$$와 동형임을 국소 trivialization 위에서 transition function $$g_{ij}$$가 양쪽에서 일치함을 통해 확인한다. 두 구성 모두 transition function을 보존하므로 isomorphism class를 보존하고, 사상의 자연성은 pullback과의 호환에서 따라온다.
:::

이 동치 덕분에 vector bundle에 대한 모든 분류 문제는 principal $$\mathrm{GL}(n,\mathbb{R})$$-bundle에 대한 문제로 번역된다. 같은 방식으로 복소 vector bundle은 principal $$\mathrm{GL}(n,\mathbb{C})$$-bundle에, oriented 실 vector bundle은 principal $$\mathrm{GL}^+(n,\mathbb{R})$$-bundle에 대응한다. 따라서 임의의 구조군 $$G$$에 대하여 principal $$G$$-bundle을 분류할 수 있다면, 이 모든 경우가 한꺼번에 해결된다.

## Pullback과 호모토피 불변성

Vector bundle에서와 마찬가지로, 연속함수 $$f:X'\rightarrow X$$와 principal $$G$$-bundle $$p:P\rightarrow X$$가 주어지면 *pullback bundle*

$$f^\ast P=\{(x',y)\in X'\times P\mid f(x')=p(y)\}$$

이 정의된다. 여기에 $$(x',y)\cdot g=(x',y\cdot g)$$로 작용을 주면 $$f^\ast P\rightarrow X'$$은 다시 principal $$G$$-bundle이 되고, transition function의 관점에서는 $$g_{ij}$$를 $$g_{ij}\circ f$$로 끌어당기는 것에 해당한다. 분류 이론의 핵심은 이 pullback이 $$f$$의 homotopy class에만 의존한다는 사실이다.

::: 정리 5 (Pullback의 homotopy 불변성)
$$X$$가 paracompact 공간이고 $$f_0,f_1:X\rightarrow Y$$가 homotopic하다고 하자. ([§호모토피, ⁋정의 2](/ko/math/algebraic_topology/homotopy#def2)) 그럼 임의의 principal $$G$$-bundle $$p:P\rightarrow Y$$에 대하여 $$f_0^\ast P$$와 $$f_1^\ast P$$는 $$X$$ 위에서 isomorphic하다.
:::
::: 증명
핵심은 다음 보조사실이다. *$$X$$가 paracompact일 때, $$X\times[0,1]$$ 위의 principal $$G$$-bundle $$Q$$는 $$X\times\{0\}$$으로의 제한을 projection $$X\times[0,1]\rightarrow X\times\{0\}$$으로 pullback한 것과 isomorphic하다.* 이는 bundle의 covering homotopy property로, paracompact base 위의 trivializing cover가 numerable(국소유한한 partition of unity를 허락)하다는 사실에 기댄다. 증명의 골자는 $$[0,1]$$을 작은 구간들로 나누어 각 구간 위에서 trivialization을 잇고, partition of unity로 이 국소적 동형들을 하나의 대역적 동형으로 붙이는 것이다. 자세한 내용은 [Hus]의 §4와 [tD]의 §14를 따른다.

이제 homotopy $$H:X\times[0,1]\rightarrow Y$$가 $$f_0,f_1$$을 잇는다 하고 $$Q=H^\ast P$$를 두자. 위 보조사실에 의해 $$Q$$는 $$Q\vert_{X\times\{0\}}=f_0^\ast P$$를 projection으로 끌어당긴 것과 동형이고, 같은 논증을 $$X\times\{1\}$$ 끝에서 반복하면 $$Q\vert_{X\times\{1\}}=f_1^\ast P$$ 역시 같은 bundle과 동형이다. $$[0,1]$$이 connected이므로 두 끝의 제한이 모두 같은 $$X$$ 위의 bundle과 동형이 되어 $$f_0^\ast P\cong f_1^\ast P$$를 얻는다.
:::

특히 $$X$$가 contractible이면 항등사상이 상수사상과 homotopic하므로 $$X$$ 위의 모든 principal $$G$$-bundle은 trivial이다. Paracompactness 가정은 빠뜨릴 수 없는데, partition of unity가 없으면 국소 동형들을 이어붙이는 단계가 무너지기 때문이다. CW complex는 항상 paracompact이므로 우리가 다루려는 base들에 대해서는 이 가정이 자동으로 성립한다.

## Universal bundle과 classifying space

정리 5는 분류사상 $$f\mapsto f^\ast P$$가 homotopy class에 의존함을 말해 준다. 만일 어떤 고정된 principal $$G$$-bundle 하나를 모든 다른 bundle이 pullback으로 얻을 수 있는 *원천*으로 삼을 수 있다면, principal $$G$$-bundle의 분류는 그 원천 공간으로의 homotopy class를 세는 일로 환원될 것이다. Vector bundle에서 $$\Gr_k(\mathbb{R}^\infty)$$ 위의 universal bundle이 그러한 원천이었던 것을 일반화한다.

::: 정의 6
Topological group $$G$$에 대하여, principal $$G$$-bundle $$p:EG\rightarrow BG$$가 *universal bundle*이라는 것은 total space $$EG$$가 contractible인 것, 곧 $$EG$$가 한 점과 homotopy equivalent인 것이다. ([§호모토피, ⁋정의 4](/ko/math/algebraic_topology/homotopy#def4)) 이때 base space $$BG$$를 $$G$$의 *classifying space<sub>분류공간</sub>*라 부른다.
:::

곧 universal bundle이란 contractible한 공간 위의 free $$G$$-작용이며, $$BG$$는 그 orbit space $$EG/G$$이다. 이러한 공간의 존재는 자명하지 않으나, Milnor가 임의의 topological group에 대하여 그 구성을 주었다.

::: 정리 7 (Milnor)
임의의 topological group $$G$$에 대하여 universal bundle $$EG\rightarrow BG$$가 존재한다.
:::
::: 증명
$$G$$의 무한 join

$$EG=G\ast G\ast G\ast\cdots=\varinjlim_n G^{\ast(n+1)}$$

을 사용한다. $$(n{+}1)$$-fold join $$G^{\ast(n+1)}$$의 점은 형식적인 합 $$t_0 y_0+\cdots+t_n y_n$$으로, $$y_i\in G$$이고 $$t_i\geq 0$$, $$\sum_i t_i=1$$이며, $$t_i=0$$인 좌표의 $$y_i$$는 무시한다. 여기에 $$G$$가 대각으로 right translation

$$(t_0 y_0+\cdots+t_n y_n)\cdot g=t_0(y_0 g)+\cdots+t_n(y_n g)$$

함으로써 작용한다. 어떤 점에서도 적어도 하나의 $$t_i$$가 양수이고 그 좌표에서 $$y_i g=y_i$$는 $$g=e$$를 강제하므로 이 작용은 free이며, 따라서 $$EG\rightarrow EG/G=BG$$는 principal $$G$$-bundle이 된다 (numerability는 join의 좌표함수 $$t_i$$가 주는 partition of unity로부터 나온다).

남은 것은 $$EG$$가 contractible임을 보이는 것이다. 두 공간 $$A,B$$의 join에 대하여 connectivity가 $$\mathrm{conn}(A\ast B)\geq \mathrm{conn}(A)+\mathrm{conn}(B)+2$$로 올라가는데, $$G$$가 공집합이 아니므로 $$(-1)$$-connected이고, 따라서 $$(n{+}1)$$개의 copy의 join $$G^{\ast(n+1)}$$은 $$(n-1)$$-connected이다. $$n\rightarrow\infty$$로 보내면 colimit $$EG$$는 모든 차원에서 connected, 곧 weakly contractible이고, CW 구조 하에서는 contractible이다. 자세한 내용은 [Mil]과 [tD]의 §14를 따른다.
:::

Universal bundle은 본질적으로 유일하다. 두 universal bundle $$EG\rightarrow BG$$와 $$EG'\rightarrow BG'$$이 주어지면, $$EG'$$이 contractible이므로 정리 5에 의해 $$BG$$로 끌어내린 분류사상이 존재하고, 이 논증을 양방향으로 적용하면 $$BG$$와 $$BG'$$이 서로 homotopy inverse인 사상으로 연결됨을 얻는다. 따라서 $$BG$$는 homotopy equivalence를 넘어서는 모호함 없이 결정되며, 우리는 $$BG$$를 *the* classifying space라 부른다.

## 분류정리

이제 분류 이론의 중심 결과를 진술한다. Classifying space의 이름이 정당화되는 지점이다.

::: 정리 8 (분류정리)
$$X$$를 paracompact 공간(가령 CW complex)이라 하고 $$[X,BG]$$를 $$X$$에서 $$BG$$로의 free homotopy class들의 집합이라 하자. 그럼 universal bundle $$EG\rightarrow BG$$를 pullback하는 사상

$$[X,BG]\xrightarrow{\ \cong\ }\{X\text{ 위의 principal }G\text{-bundle}\}/\cong,\qquad [f]\mapsto f^\ast EG$$

은 잘 정의된 전단사이며, 사상 $$X'\rightarrow X$$에 대한 pullback과 호환된다는 의미에서 자연스럽다.
:::
::: 증명
$$[f]\mapsto f^\ast EG$$가 $$[f]$$의 대표 선택에 의존하지 않는 것은 [정리 5](#thm5)에 의한 것이다. 전사성과 단사성을 차례로 본다.

**전사성.** $$X$$ 위의 principal $$G$$-bundle $$P$$가 주어졌다 하자. $$X$$가 paracompact이므로 $$P$$가 trivialize되는 numerable open cover $$\{U_i\}$$와 그에 종속된 partition of unity $$\{\rho_i\}$$를 잡을 수 있다. 각 $$U_i$$ 위의 trivialization은 $$G$$-equivariant 사상 $$\psi_i:p^{-1}(U_i)\rightarrow G$$를 주므로,

$$\widetilde{f}:P\rightarrow EG,\qquad y\mapsto \sum_i \rho_i(p(y))\psi_i(y)$$

는 잘 정의된 $$G$$-equivariant 연속함수이다 (각 점에서 유한합이고, $$\psi_i$$가 $$\rho_i>0$$인 곳에서만 등장한다). $$G$$-equivariant 사상은 base space 사이의 사상 $$f:X\rightarrow BG$$로 내려가고, $$\widetilde{f}$$가 fiber마다 동형이므로 $$P\cong f^\ast EG$$를 얻는다.

**단사성.** $$f_0,f_1:X\rightarrow BG$$에 대하여 $$f_0^\ast EG\cong f_1^\ast EG=:P$$라 하자. 각 분류사상 $$f_i$$는 bundle 사상 $$P\cong f_i^\ast EG\rightarrow EG$$, 곧 $$P$$에서 universal bundle로 가는 $$G$$-equivariant 연속함수 $$\Phi_i:P\rightarrow EG$$를 덮개로 가지며 base에서 $$f_i$$를 유도한다. 그런데 $$EG$$가 contractible이므로, numerable principal bundle $$P$$에서 $$EG$$로 가는 임의의 두 $$G$$-equivariant 사상은 서로 $$G$$-equivariant homotopic하다. 따라서 $$\Phi_0$$과 $$\Phi_1$$을 잇는 $$G$$-equivariant homotopy $$P\times[0,1]\rightarrow EG$$가 존재하고, 이것이 base로 내려가 $$f_0$$과 $$f_1$$ 사이의 homotopy를 주므로 $$[f_0]=[f_1]$$이다. 여기서 두 $$G$$-equivariant 사상이 $$G$$-homotopic하다는 사실 자체는 $$EG$$의 contractibility와 $$P$$의 numerability에 기댄다.

두 단계의 세부는 [Mil], [tD]의 §14, [Hus]의 §4를 따른다.
:::

![분류사상의 pullback 사각형](/assets/images/Math/Algebraic_Topology/Classifying_Spaces-1.svg){:style="width:8.21em" class="invert" .align-center}

분류정리는 principal $$G$$-bundle의 기하학적 분류를 순수하게 homotopy 이론적인 데이터 $$[X,BG]$$로 옮긴다. [명제 4](#prop4)와 결합하면 rank $$n$$ 실 vector bundle의 분류가 $$[X,B\mathrm{GL}(n,\mathbb{R})]$$로, 복소의 경우 $$[X,B\mathrm{GL}(n,\mathbb{C})]$$로 환원되며, 이것이 앞 글의 Grassmannian을 통한 분류와 같은 내용임을 곧 보게 된다.

::: 참고 9
Classifying space의 구성은 $$G$$에 대해 functorial이다. 연속적인 group homomorphism $$\phi:G\rightarrow H$$가 주어지면, $$EG$$ 위의 $$G$$-작용을 $$\phi$$를 통해 $$H$$-작용으로 바꾸어 얻는 associated bundle $$EG\times_G H$$를 분류하는 사상이 $$B\phi:BG\rightarrow BH$$를 유도한다. 이는 $$B(\psi\circ\phi)\simeq B\psi\circ B\phi$$를 만족하여, $$G\mapsto BG$$가 homotopy category 위의 functor가 되게 한다. 가령 inclusion $$\mathrm{U}(n)\hookrightarrow\mathrm{GL}(n,\mathbb{C})$$이 유도하는 $$B\mathrm{U}(n)\rightarrow B\mathrm{GL}(n,\mathbb{C})$$이 아래에서 쓰인다.
:::

## 분류공간의 예

가장 단순하면서도 시사적인 경우는 $$G$$가 discrete group일 때이다. 이때 principal $$G$$-bundle은 fiber가 discrete set인 fiber bundle, 곧 $$G$$를 deck transformation group으로 갖는 regular covering space와 같다.

::: 예시 10
$$G$$가 discrete group이라 하자. Universal bundle $$EG\rightarrow BG$$에서 $$EG$$는 contractible이고 $$G$$가 free하게, 그리고 discrete하게 작용하므로, $$EG\rightarrow BG$$는 $$BG$$의 universal cover이며 그 deck transformation group은 $$G$$이다. ([§피복공간, ⁋정리 11](/ko/math/algebraic_topology/covering_spaces#thm11)) 따라서 $$\pi_1(BG)\cong G$$이고, $$EG$$가 contractible이라 $$BG$$의 universal cover 또한 contractible이므로 $$\pi_n(BG)=0$$ ($$n\geq 2$$) 이다. 곧 $$BG$$는 Eilenberg–MacLane 공간 $$K(G,1)$$이다.

이로부터 구체적인 분류공간이 covering space 이론으로부터 직접 읽힌다. $$G=\mathbb{Z}/2$$일 때 $$S^\infty$$는 contractible이고 antipodal 작용이 free하므로 $$E(\mathbb{Z}/2)=S^\infty$$, $$B(\mathbb{Z}/2)=S^\infty/(\mathbb{Z}/2)=\RP^\infty$$이다. $$G=\mathbb{Z}$$일 때는 $$\mathbb{R}$$ 위의 평행이동 작용으로부터 $$B\mathbb{Z}=\mathbb{R}/\mathbb{Z}=S^1$$을 얻으며, 이는 $$S^1$$의 universal cover $$\mathbb{R}\rightarrow S^1$$이 deck group $$\mathbb{Z}$$를 갖는다는 사실과 정확히 일치한다. ([§피복공간, ⁋따름정리 12](/ko/math/algebraic_topology/covering_spaces#cor12))
:::

연속군의 경우 가장 기본적인 예는 원군 $$G=S^1$$이다. $$S^1$$은 $$\mathbb{C}^\infty\setminus\{0\}$$ 위에 스칼라곱으로 free하게 작용하고 이 공간은 단위구면 $$S^\infty=\varinjlim_n S^{2n-1}$$으로 deformation retract되어 contractible이므로, $$ES^1=\mathbb{C}^\infty\setminus\{0\}$$이고 그 orbit space는 복소 직선들의 공간

$$BS^1=(\mathbb{C}^\infty\setminus\{0\})/S^1=\CP^\infty$$

이다. 한편 $$\CP^\infty=\Gr_1(\mathbb{C}^\infty)$$은 $$\mathrm{U}(1)=S^1$$의 분류공간으로 앞 글에서 $$B\mathrm{U}(1)$$이라 적은 바로 그 공간이며, 따라서 $$BS^1=B\mathrm{U}(1)=\CP^\infty$$이다. 더 일반적으로 $$n$$차원 torus $$T=(S^1)^n$$에 대해서는 곱이 분류공간의 곱으로 가므로

$$BT=B(S^1)^n=(\CP^\infty)^n$$

이다. 같은 방식으로 임의의 $$n$$에 대하여 unitary group과 orthogonal group의 분류공간은 앞 글의 infinite Grassmannian으로 실현된다. 즉 $$B\mathrm{U}(n)=\Gr_n(\mathbb{C}^\infty)$$이고 $$B\mathrm{O}(n)=\Gr_n(\mathbb{R}^\infty)$$인데, 이는 $$\Gr_n(\mathbb{C}^\infty)$$ 위의 universal vector bundle의 frame bundle이 universal principal $$\mathrm{U}(n)$$-bundle을 주고 그 total space (Stiefel 공간의 colimit) 가 contractible이기 때문이다.

마지막으로 일반선형군과 그 maximal compact subgroup의 분류공간이 같은 homotopy type을 갖는다는 사실은 분류 이론에서 자주 쓰인다.

::: 예시 11
Inclusion $$\mathrm{U}(n)\hookrightarrow\mathrm{GL}(n,\mathbb{C})$$은 homotopy equivalence

$$B\mathrm{U}(n)\xrightarrow{\ \simeq\ }B\mathrm{GL}(n,\mathbb{C})$$

를 유도한다. 이는 Gram–Schmidt 직교화가 $$\mathrm{GL}(n,\mathbb{C})$$을 $$\mathrm{U}(n)$$ 위로 deformation retract시키는 데서 나온다. 구체적으로 $$\mathrm{GL}(n,\mathbb{C})$$의 임의의 행렬은 unitary 행렬과 양의 정부호 upper-triangular 행렬의 곱으로 유일하게 분해되고($$QR$$ 분해), upper-triangular 인자를 항등원 쪽으로 연속적으로 수축시키면 $$\mathrm{GL}(n,\mathbb{C})$$이 $$\mathrm{U}(n)$$으로 deformation retract됨을 얻는다. Group 수준의 이 homotopy equivalence가 $$B$$를 거쳐 분류공간 수준의 homotopy equivalence를 준다. 따라서 복소 rank $$n$$ vector bundle은 그 구조군을 $$\mathrm{GL}(n,\mathbb{C})$$에서 $$\mathrm{U}(n)$$으로 줄여도 분류에 손실이 없으며, 이것이 모든 복소 bundle에 Hermitian metric을 줄 수 있다는 사실의 분류공간 판본이다.
:::

## 분류공간의 코호몰로지

분류정리에 따르면 구조군 $$G$$를 갖는 bundle의 특성류란 $$BG$$의 cohomology class를 분류사상으로 pullback한 것이다. 따라서 특성류 이론은 $$BG$$의 cohomology ring을 계산하는 일과 같으며, 우리는 가장 기본적인 군들에 대해 이를 정리한다.

출발점은 복소 projective space의 cohomology ring이다. 앞 글에서 우리는

$$H^\bullet(\CP^\infty;\mathbb{Z})=\mathbb{Z}[x],\qquad \lvert x\rvert=2$$

임을 보았으며, 생성원 $$x$$는 tautological line bundle의 first Chern class였다. ([§벡터다발의 특성류, ⁋예시 8](/ko/math/algebraic_topology/characteristic_classes#ex8)) $$BS^1=\CP^\infty$$이므로 이는 곧

$$H^\bullet(BS^1;\mathbb{Z})=\mathbb{Z}[t],\qquad \lvert t\rvert=2$$

를 뜻한다. Torus의 경우는 곱공간의 cohomology로부터 따라온다.

::: 따름정리 12
$$n$$차원 torus $$T=(S^1)^n$$에 대하여

$$H^\bullet(BT;\mathbb{Z})=\mathbb{Z}[t_1,\ldots,t_n],\qquad \lvert t_i\rvert=2$$

는 $$n$$개의 degree $$2$$ 생성원으로 이루어진 polynomial ring이다. 더 나아가 degree $$2$$ 부분 $$H^2(BT;\mathbb{Z})$$은 character lattice $$\mathrm{Hom}(T,S^1)$$과 표준적으로 동형이며, $$H^\bullet(BT;\mathbb{Z})$$은 이 lattice 위의 symmetric algebra이다.
:::
::: 증명
$$BT=(\CP^\infty)^n$$이고, 앞 절의 $$BS^1=\CP^\infty$$ 계산으로부터 각 인자의 cohomology $$H^\bullet(\CP^\infty;\mathbb{Z})=\mathbb{Z}[t_i]$$는 각 차수에서 free abelian group이므로 Künneth 정리에 Tor 항이 나타나지 않는다. 따라서 cross product가 cohomology ring의 동형

$$H^\bullet(BT;\mathbb{Z})\cong\bigotimes_{i=1}^n \mathbb{Z}[t_i]=\mathbb{Z}[t_1,\ldots,t_n]$$

을 준다. ([§합곱](/ko/math/algebraic_topology/cup_products)) Character $$\chi:T\rightarrow S^1$$은 $$B\chi:BT\rightarrow BS^1=\CP^\infty$$을 유도하고 ([참고 9](#rmk9)) $$B\chi^\ast(t)\in H^2(BT;\mathbb{Z})$$를 대응시키는데, $$i$$번째 좌표 projection $$T\rightarrow S^1$$이 $$t_i$$로 가므로 이 대응은 $$\mathrm{Hom}(T,S^1)\cong\mathbb{Z}^n$$을 $$H^2(BT;\mathbb{Z})=\bigoplus_i\mathbb{Z}t_i$$로 보내는 동형이다. Polynomial ring은 그 degree $$2$$ 부분 위의 symmetric algebra이므로 마지막 주장이 따라온다.
:::

이 동형은 character lattice 위의 다항식을 $$BT$$의 cohomology class로 읽게 해 주며, torus가 작용하는 공간의 불변량을 다룰 때 핵심이 된다. Unitary group의 경우는 한 단계 더 나아간 계산이 필요하지만, 앞 글에서 이미 그 결과를 보았다.

::: 명제 13
Unitary group $$\mathrm{U}(n)$$에 대하여

$$H^\bullet(B\mathrm{U}(n);\mathbb{Z})=\mathbb{Z}[c_1,\ldots,c_n],\qquad \lvert c_i\rvert=2i$$

는 universal complex bundle의 Chern class $$c_i$$들로 생성되는 polynomial ring이다.
:::
::: 증명
$$B\mathrm{U}(n)=\Gr_n(\mathbb{C}^\infty)$$이고, 그 cohomology ring이 universal bundle의 Chern class들로 생성되는 polynomial ring

$$H^\bullet(\Gr_n(\mathbb{C}^\infty);\mathbb{Z})=\mathbb{Z}[c_1,\ldots,c_n]$$

임은 앞 글에서 진술하였다. ([§벡터다발의 특성류](/ko/math/algebraic_topology/characteristic_classes)) 그 증명의 골자는 maximal torus $$T\subset\mathrm{U}(n)$$이 유도하는 사상 $$BT\rightarrow B\mathrm{U}(n)$$이 cohomology 위에서 Weyl group $$S_n$$의 작용에 대한 불변량으로의 단사를 주고, [따름정리 12](#cor12)의 $$\mathbb{Z}[t_1,\ldots,t_n]$$ 안에서 $$S_n$$-불변 부분이 elementary symmetric polynomial들이 생성하는 $$\mathbb{Z}[c_1,\ldots,c_n]$$이라는 데 있다. 이때 $$c_i$$는 $$t_1,\ldots,t_n$$의 $$i$$번째 elementary symmetric polynomial로 표현되며, 이것이 splitting principle에서 Chern class를 Chern root로 분해하던 식과 같다. 완전한 계산은 [MS]의 §14를 따른다.
:::

이렇게 $$B\mathrm{U}(n)$$의 cohomology가 Chern class들의 다항식 전부로 이루어지므로, 복소 vector bundle의 모든 특성류는 Chern class의 다항식이다. 같은 방식으로 $$H^\bullet(B\mathrm{O}(n);\mathbb{Z}/2)=\mathbb{Z}/2[w_1,\ldots,w_n]$$이 Stiefel–Whitney class를 분류하며, oriented bundle에 대해서는 $$B\mathrm{SO}(n)$$의 cohomology에서 Euler class가 나타난다. 한 공간 $$X$$ 대신 $$G$$-작용을 갖는 공간을 다룰 때, $$BG$$와 그 위에서의 homotopy quotient는 이 cohomology를 base로 삼는 equivariant cohomology의 토대가 된다.

---

**참고문헌**

**[Mil]** J. W. Milnor, *Construction of universal bundles, II*, Annals of Mathematics **63** (1956), 430–436.

**[MS]** J. W. Milnor and J. D. Stasheff, *Characteristic Classes*, Annals of Mathematics Studies 76, Princeton University Press, 1974.

**[Hat]** A. Hatcher, *Algebraic Topology*, Cambridge University Press, 2002.

**[tD]** T. tom Dieck, *Algebraic Topology*, EMS Textbooks in Mathematics, European Mathematical Society, 2008.

**[Hus]** D. Husemoller, *Fibre Bundles*, 3rd ed., Graduate Texts in Mathematics 20, Springer, 1994.
