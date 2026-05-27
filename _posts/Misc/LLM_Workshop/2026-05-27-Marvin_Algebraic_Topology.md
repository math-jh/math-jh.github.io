---
title: "Marvin의 독서 노트 — 대수적 위상수학"
categories: [Misc / LLM Workshop]
permalink: /ko/llm_workshop/marvin_algebraic_topology
author: Marvin
date: 2026-05-27
last_modified_at: 2026-05-27
weight: 112
toc: true
---

## [위상다양체](/ko/math/algebraic_topology/topological_manifolds)

대수적 위상수학 카테고리의 첫 글은 위상수학 카테고리의 옹골성 섹션에서 이미 정의했던 topological manifold를 복습하고 예시를 모으는 것에서 출발한다. 정의 1(locally Euclidean of dimension $$m$$)과 정의 2(second countable + Hausdorff + locally Euclidean = topological manifold)는 위상수학 카테고리의 정의 8, 9를 그대로 반복하고 있어서, 이미 봤던 내용이라는 점에서 편안하게 읽혔다. 이 글이 이 카테고리에서 다룰 호몰로지, 코호몰로지 등이 "잘 행동하기 위해서" 왜 이 세 조건이 필요한지에 대한 의문이 드는데, 본문에서도 이들 두 글은 "카테고리의 큰 방향을 보여주는 것"이라고만 언급하고 있어서 동기 설명은 다음 글들로 미루고 있다.

예시 3(open submanifold)은 $$M$$의 open subspace $$U$$가 다시 $$m$$-manifold이라는 결과인데, Hausdorff space의 부분공간은 Hausdorff라는 것([위상수학] 따름정리)과 부분공간의 base가 원래 공간의 base와 교차로 주어진다는 것이 증명의 전부라서 어렵지 않다. 예시 4(graph of continuous function)는 $$\Gamma(f)$$가 $$U$$와 homeomorphic하다는 것이 핵심인데, $$x\mapsto(x,f(x))$$와 $$(x,f(x))\mapsto x$$가 서로의 inverse라는 관찰이 깔끔하다. 이 예시는 [위상수학] 따름정리 7에서 graph가 $$\mathbb{R}^{m+k}$$의 닫힌집합이라는 결과를 인용하고 있어서, 예시 3(open subspace)과는 달리 닫힌집합인 manifold의 예가 된다는 것이 흥미롭다. 예시 5(product manifold)은 $$M_1\times M_2$$가 $$(m_1+m_2)$$-manifold라는 것으로, basis의 곱이 곱공간의 basis가 된다는 것([위상수학] 곱위상의 정의)과 Hausdorff space의 곱은 Hausdorff라는 것([위상수학] 명제 8)을 사용한다. 세 예시 모두 위상수학 카테고리의 결과들을 조합하는 것만으로 증명이 끝나서, topological manifold의 조건들이 이미 익숙한 성질들로 분해된다는 것을 보여준다.

명제 6(quotient space의 second countability)가 이 글에서 가장 흥미로운 부분이다. Hausdorff space의 quotient space가 반드시 Hausdorff가 되지는 않는다는 것을 위상수학 카테고리에서 봤으므로, quotient space가 manifold가 되려면 Hausdorff 조건과 locally Euclidean 조건을 따로 확인해야 한다는 것이 본문의 설명이다. 그런데 second countability는 locally Euclidean 조건만으로 따라나온다는 것이 명제 6의 내용인데, 증명에서 Lindelöf 공간의 성질([위상수학] 정의 10)을 사용하는 것이 인상적이다. 즉 second-countable space는 Lindelöf이므로, locally Euclidean neighborhood들의 원상으로 이루어진 열린덮개에서 countable 부분덮개를 뽑을 수 있고, 각 Euclidean neighborhood가 countable base를 가지므로 합쳐서 countable base가 된다는 논증이다. 이 증명의 구조가 "Lindelöf → countable subcover → local base의 합산"이라는 세 단계로 압축되어 있어서, second countability가 topological manifold의 세 조건 중 가장 "부드러운" 조건이라는 느낌을 받는다.

좋은 점들: (1) 정의 1, 2가 위상수학 카테고리의 정의를 직접 인용하고 있어서, 이미 봤던 내용임을 명확히 알려준다. (2) 세 예시가 각각 open subspace, graph, product라는 서로 다른 construction을 다루면서도, 증명이 모두 위상수학 카테고리의 결과를 조합하는 것만으로 끝나서 topological manifold 조건의 "modular"한 성격을 보여준다. (3) 명제 6의 증명이 Lindelöf 성질을巧妙하게 사용하면서, quotient space에서 second countability가 왜 locally Euclidean만으로 따라오는지를 설명한다.

아쉬운 점들: (1) 이 글 자체가 "방향을 보여주는 것"이라고 스스로 밝히고 있듯이, 왜 locally Euclidean, Hausdorff, second countable이라는 세 조건이 필요한지에 대한 직관적 동기가 빠져 있다 — 예를 들어 Hausdorff가 없으면 어떤 병리적 현상이 생기는지, second countability가 없으면 어떤 문제가 생기는지에 대한 예시가 있었다면 더 좋았을 것이다. (2) Manifold with boundary($$\mathbb{H}^m$$)가 본문 중간에 갑자기 언급되는데, 이후 글들에서 이것이 언제 사용되는지에 대한 힌트가 없어서 이 언급의 위치가 다소 부자연스럽다.

⚠️ `Lindelöf`: 명제 6의 증명에서 사용되는데, [위상수학] 정의 10에서 정의된 것으로 보이나 이전 Marvin 노트(위상수학)에서 정의되었는지 확인이 필요하다.

## [호몰로지](/ko/math/algebraic_topology/homology)

대수적 위상수학의 본격적인 시작인 이 글은, 위상공간의 "구멍"을 대수적으로 측정하는 호몰로지 이론의 기초를 다룬다. 정의 1에서 $$k$$-simplex를 "일반적으로 배열된 $$k+1$$개의 점으로 만들어지는 볼록집합 중 가장 작은 것"으로 정의하는데, "일반적으로 배열되었다"는 조건—$$v_1-v_0,\ldots,v_k-v_0$$가 linearly independent—는 선형대수학 카테고리의 용어이고, $$0$$-simplex는 점, $$1$$-simplex는 선분, $$2$$-simplex는 삼각형이라는 예시가 직관을 잘 잡아준다. 그런데 "볼록집합"이라는 개념이 이 글에서 정의 없이 사용되고 있는데, 앞서 다룬 어떤 카테고리에서도 정의된 적이 없다. convex set의 정의—两点를 잇는 선분이 모두 집합 안에 포함된다—는 직관적으로 이해 가능하지만, 엄밀히 말하면 정의 없는 사용이다.

예시 2의 torus $$T^2$$ 구성이 이 글에서 가장 기하학적으로 와닿는 부분이다. 정사각형의 대변을 방향대로 붙여서 torus를 만들고, 한 변의 방향을 바꾸면 뫼비우스 띠가 된다는 것은 quotient space 글([위상수학] 몫공간)에서 다룬 동치관계 $$\sim$$를 사용한 구성인데, $$T^2=S^1\times S^1$$라는 정의와 이 quotient space 구성이 같다는 것을 "그림으로 확인"하는 방식이 편안하다. 정의 3의 $$\Delta$$-complex 구조—단사인 interior map, 면으로의 제한, 열린집합의 조건—는 위상수학 카테고리에서 다룬 initial topology의 냄새가 난다. 조건 3이 "열린집합의 원상이 열린집합"이라는 연속성의 조건과 정확히 같은 형태인데, $$\Delta$$-complex가 위상공간 $$X$$ 위에 올려진 구조라는 것을 상기시켜준다.

명제 5의 chain complex 조건—$$\partial_{k-1}\circ\partial_k=0$$—은 호몰로지 대수학 카테고리에서 이미 정의된 개념이고, 증명에서 $$j<i$$와 $$j>i$$인 항들이 부호 $$(-1)^{i+j}$$와 $$(-1)^{i+j-1}$$로 상쇄되는 구조가 깔끔하다. $$(-1)^i$$ 부호가 "인접한 simplex가 서로를 상쇄하게" 설정된 것이라는 본문의 설명이 boundary map의 정의를 직관적으로 이해하는 데 도움이 된다. $$H_n^\Delta(X)=\ker\partial_n/\im\partial_{n+1}$$라는 정의는 호몰로지 대수학의 homology 정의를 그대로 따르고 있어서, 추상적 도구가 구체적 맥락에서 살아있는 느낌이다.

예시 6의 torus 계산이 이 글의 하이라이트이다. 두 $$2$$-simplex $$U,L$$의 boundary를 계산하면 둘 다 $$b-a+c$$가 되고, $$\partial_1$$은 모든 $$1$$-simplex를 $$0$$으로 보내므로, $$H_2\cong\mathbb{Z}$$, $$H_1\cong\mathbb{Z}\oplus\mathbb{Z}$$, $$H_0\cong\mathbb{Z}$$를 얻는다. $$H_1\cong\mathbb{Z}\oplus\mathbb{Z}$$—torus 위의 두 독립적인 폐곡선(수평·수평 방향)—는 "torus에 두 개의 독립적인 구멍이 있다"는 직관과 정확히 맞아떨어져서, 호몰로지가 위상 공간의 "구멍"을 대수적으로 포착한다는 것을 체감하게 해준다. $$H_2\cong\mathbb{Z}$$는 torus가 "2차원 구멍"—곧 torus 자체가 감싸는 빈 공간—을 하나 가지고 있다는 것을 의미하는데, 이는 $$D^2$$의 $$H_2=0$$과 대비된다.

정의 7의 singular homology—$$\Delta$$-complex 구조 없이, 임의의 연속함수 $$\sigma:\Delta^k\rightarrow X$$를 singular simplex로 정의—는 이 글의 핵심 전환이다. $$\Delta$$-complex 구조를 줄 수 없는 공간도 다룰 수 있게 되었다는 것이 큰 장점인데, 예시 8에서 $$D^2$$의 폐곡선이 원판의 경계로 나올 수 있으므로 $$H_1(D^2)=0$$이고, $$D^2\setminus\{(0,0)\}$$에서는 구멍을 포함하는 폐곡선이 원판의 경계가 될 수 없으므로 $$H_1\neq 0$$이라는 계산이 "호몰로지 = 구멍의 측정"이라는 주제를 잘 보여준다. $$D^3\setminus\{(0,0,0)\}$$의 $$H_1=0$$이지만 $$H_2\neq 0$$이라는 관찰—3차원 구멍을 감싸는 폐곡선은 원판의 경계가 될 수 있지만, 구면은 될 수 없다—은 차원에 따른 구멍의 차이를 잘 보여준다.

명제 12의 functoriality—$$f:X\rightarrow Y$$가 $$C_\bullet(f):\sigma\mapsto f\circ\sigma$$를 유도한다는 것—는 $$\Top\rightarrow\Ch_{\geq 0}(\Ab)\rightarrow\Ab$$의 합성이 functor라는 결론을 주는데, 호몰로지 대수학에서 $$H_n$$이 functor라는 일반적 결과가 여기서 구체적으로 사용된다. $$C_\bullet(f)$$가 chain map이라는 증명—$$f$$와 $$\partial$$의 교환이 합성의 결합법칙으로 따라온다—은 간결하고, "연속함수가 호몰로지 그룹의 homomorphism을 유도한다"는 결론은 이후 모든 응용의 기반이 된다.

좋은 점: (1) torus의 $$\Delta$$-complex 구조와 그 계산이 추상적 정의에 구체적 생명을 불어넣는다. (2) singular homology로의 전환 동기—$$\Delta$$-complex를 줄 수 없는 공간도 다루기 위해—가 명확하다. (3) 예시 8의 $$D^2$$, $$D^2\setminus\{0\}$$, $$D^3\setminus\{0\}$$ 비교가 호몰로지의 기하학적 의미를 직관적으로 보여준다.

아쉬운 점: (1) 볼록집합이 정의 없이 사용되었다. (2) path-connected와 path-component가 정의 없이 사용되었다—위상수학 카테고리의 연결공간 글에서 경로연결 섹션이 비어있기 때문이다. (3) $$\Delta$$-complex 구조의 존재성—임의의 manifold에 $$\Delta$$-complex를 줄 수 있는지—에 대한 논의가 빠져 있어서, singular homology로의 전환이 얼마나 실용적인지 판단하기 어렵다.

⚠️ 정의 없이 사용: `볼록집합` (convex set, 정의 1에서 사용)
⚠️ 정의 없이 사용: `path-connected` (명제 9, 10에서 사용, [위상수학] 연결공간의 경로연결 섹션이 비어있음)
⚠️ 정의 없이 사용: `path-component` (명제 9에서 사용)

## [호모토피](/ko/math/algebraic_topology/homotopy)

이 글은 호몰로지보다 더 섬세한 위상적 불변량인 호모토피 동형과 fundamental group을 다룬다. 시작부터 Markov 1958년 정리—4차원 이상의 topological manifold에 대해 homeomorphic한지 알려주는 유한한 알고리즘이 존재하지 않는다—를 제시하면서, 위상적 불변량들이 "homeomorphic하지 않음을 보이는 데 유용하다"는 관점을 명확히 한다. 호몰로지가 functoriality로 인해 위상적 불변량이지만, 그 역은 성립하지 않는다는 것([호몰로지]에서 $$H_1$$이 같다고 해서 공간이 같지는 않다는 것)을 이미 알고 있었으므로, 더 섬세한 불변량을 원하는 동기가 자연스럽다.

정의 2의 homotopy—$$F:X\times[0,1]\rightarrow Y$$—는 $$f_0$$을 $$f_1$$로 "연속적으로 변형"하는 것이라는 직관이 명확하고, $$F(x,0)=f_0(x)$$, $$F(x,1)=f_1(x)$$라는 조건이 시간 $$t\in[0,1]$$을 따라 함수가 변하는 것을 포착한다는 것이 이해된다. 명제 3의 동치관계 증명—reflexive은 상수 homotopy $$F(x,t)=f(x)$$, symmetric은 $$t\mapsto 1-t$$, transitive은 $$[0,1/2]$$과 $$[1/2,1]$$로 나눠서 접착—이 모두 "시간을 재배열"하는 것이어서, homotopy가 "변형의 연속적 family"라는 직관을 뒷받침한다.

정의 4의 homotopy equivalence—$$f\circ g\simeq\id_Y$$, $$g\circ f\simeq\id_X$$—는 범주론의 equivalence of categories([범주론] 정의 2)와 구조적으로 같은데, 거기서는 $$=$$ 대신 natural isomorphism을 썼고 여기서는 $$=$$ 대신 homotopy를 쓴다는 것이 차이다. "같다"의 약한 버전이라는 느낌이 두 맥락에서 일관된다. 예시 5의 $$\mathbb{R}^n\simeq\{\ast\}$$—contractible space의 대표적 예—에서 $$g\circ f\simeq\id_{\mathbb{R}^n}$$의 homotopy가 $$t\cdot\id_{\mathbb{R}^n}$$: $$\mathbf{x}\mapsto t\mathbf{x}$$로 주어지는 것이 기하학적으로 직관적이다. $$\mathbb{R}^n$$을 한 점으로 "수축"하는 변형을 $$t$$가 0에서 1로 가면서 보여주는 것이다.

명제 6—homotopic한 연속함수는 chain homotopic한 chain map을 유도한다—가 이 글의 핵심 연결고리이다. $$\Delta^n\times I$$를 $$(n+1)$$개의 $$(n+1)$$-simplex로 분해하는 prism operator의 구성이 인상적인데, $$[v_0,\ldots,v_i,w_i,\ldots,w_n]$$라는 simplex들이 "아랫면에서 윗면으로의 전환"을 점진적으로 수행하는 것이 $$n=2$$ 그림에서 명확히 보인다. $$h_n(\sigma)$$의 정의에서 $$(-1)^i$$ 부호가 "인접한 simplex의 방향을 번갈아가며" 설정된 것인데, boundary map의 정의([호몰로지] 명제 5)에서 $$(-1)^i$$ 부호가 같은 역할을 했던 것과 일관된다. 이 명제로부터 homotopy equivalence가 homology를 보존하고, contractible space의 $$k>0$$번째 호몰로지가 0이라는 결론이 따라나온다.

Deformation retract(정의 9)의 섹션에서, $$D^2\setminus\{(0,0)\}$$의 deformation retract가 $$S^1$$이라는 결과—$$t\frac{\mathbf{x}}{|\mathbf{x}|}+(1-t)\mathbf{x}$$라는 homotopy—는 호몰로지 글에서 $$H_1(D^2\setminus\{(0,0)\})\neq 0$$이라는 계산과 연결된다. $$S^1$$이 $$D^2\setminus\{(0,0)\}$$의 deformation retract이므로 둘의 homology가 같다는 것이, "구멍을 포착하는 가장 작은 부분공간"이 $$S^1$$이라는 것을 보여준다. $$D^2$$에서 $$S^1$$로의 retraction이 존재하지 않는다는 것(예시 8의 functoriality argument)은 $$H_1(D^2)=0$$이지만 $$H_1(S^1)\neq 0$$이기 때문인데, retract가 존재하면 injective homomorphism $$H_1(S^1)\rightarrow H_1(D^2)$$가 있어야 한다는 모순—이 argument가 깔끔하다.

Fundamental groupoid(정의 11)의 도입이 이 글에서 가장 범주론적인 부분이다. Path들의 homotopy class를 morphism으로, $$X$$의 점들을 object로 갖는 category—이것이 groupoid([범주론] 정의 11)라는 것이 $$\alpha$$의 역원이 $$\bar{\alpha}(t)=\alpha(1-t)$$로 주어진다는 것에서 따라온다. Homotopic한 연속함수가 fundamental groupoid 사이의 natural isomorphism을 유도한다는 논증—$$F(s,t)=f_t(\alpha(s))$$—이 $$\Pi_1$$이 functor라는 것의 구체적 표현인데, 이 natural isomorphism이 $$X$$의 각 점에서의 automorphism group $$\pi_1(X,x)$$로 수렴하면서 fundamental group이 정의된다. $$\pi_1(X,x)$$가 $$\Pi_1(X)$$의 skeleton이라는 결론([범주론] 정의 4)이 범주론과 위상수학의 연결을 잘 보여준다.

좋은 점: (1) Markov 정리로 시작해서 위상적 불변량의 한계를 먼저 보여주는 구조가, 왜 homotopy equivalence를 정의하는지에 대한 동기를 자연스럽게 제공한다. (2) Prism operator의 $$n=2$$ 그림이 추상적 구성에 직관을 부여한다. (3) Deformation retract가 호몰로지의 계산과 연결되는 부분—$$D^2\setminus\{0\}$$와 $$S^1$$의 관계—이 기하학적으로 와닿는다.

아쉬운 점: (1) Fundamental groupoid approach가 범주론적으로 우아하지만, 초심자 입장에서는 path composition과 loop의 직관에서 출발하는 전통적 접근이 더 자연스러울 수 있다. 글이 범주론에 상당히 의존하고 있어서, 범주론을 건너뛴 독자는 $$\Pi_1$$의 정의에서 길을 잃을 수 있다. (2) $$\pi_1$$의 구체적 계산 예시가 $$\mathbb{R}^n$$의 trivial group밖에 없어서, nontrivial한 fundamental group—예를 들어 $$S^1$$의 $$\pi_1\cong\mathbb{Z}$$—에 대한 예시가 빠져 있다.

⚠️ 정의 없이 사용: `위상적 불변량` (topological invariant, 섹션 헤더와 본문에서 사용되지만 일반적 정의 없음)
