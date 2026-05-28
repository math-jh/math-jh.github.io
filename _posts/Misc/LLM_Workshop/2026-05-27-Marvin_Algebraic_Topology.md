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

좋은 점들: (1) 정의 1, 2가 위상수학 카테고리의 정의를 직접 인용하고 있어서, 이미 봤던 내용임을 명확히 알려준다. (2) 세 예시가 각각 open subspace, graph, product라는 서로 다른 construction을 다루면서도, 증명이 모두 위상수학 카테고리의 결과를 조합하는 것만으로 끝나서 topological manifold 조건의 "modular"한 성격을 보여준다. (3) 명제 6의 증명이 Lindelöf 성질을 묘하게 사용하면서, quotient space에서 second countability가 왜 locally Euclidean만으로 따라오는지를 설명한다.

아쉬운 점들: (1) 이 글 자체가 "방향을 보여주는 것"이라고 스스로 밝히고 있듯이, 왜 locally Euclidean, Hausdorff, second countable이라는 세 조건이 필요한지에 대한 직관적 동기가 빠져 있다 — 예를 들어 Hausdorff가 없으면 어떤 병리적 현상이 생기는지, second countability가 없으면 어떤 문제가 생기는지에 대한 예시가 있었다면 더 좋았을 것이다. (2) Manifold with boundary($$\mathbb{H}^m$$)가 본문 중간에 갑자기 언급되는데, 이후 글들에서 이것이 언제 사용되는지에 대한 힌트가 없어서 이 언급의 위치가 다소 부자연스럽다.

⚠️ `Lindelöf`: 명제 6의 증명에서 사용되는데, [위상수학] 정의 10에서 정의된 것으로 보이나 이전 Marvin 노트(위상수학)에서 정의되었는지 확인이 필요하다.

## [호몰로지](/ko/math/algebraic_topology/homology)

대수적 위상수학의 본격적인 시작인 이 글은, 위상공간의 "구멍"을 대수적으로 측정하는 호몰로지 이론의 기초를 다룬다. 정의 1에서 $$k$$-simplex를 "일반적으로 배열된 $$k+1$$개의 점으로 만들어지는 볼록집합 중 가장 작은 것"으로 정의하는데, "일반적으로 배열되었다"는 조건—$$v_1-v_0,\ldots,v_k-v_0$$가 linearly independent—는 선형대수학 카테고리의 용어이고, $$0$$-simplex는 점, $$1$$-simplex는 선분, $$2$$-simplex는 삼각형이라는 예시가 직관을 잘 잡아준다. 그런데 "볼록집합"이라는 개념이 이 글에서 정의 없이 사용되고 있는데, 앞서 다룬 어떤 카테고리에서도 정의된 적이 없다. convex set의 정의—두 점을 잇는 선분이 모두 집합 안에 포함된다—는 직관적으로 이해 가능하지만, 엄밀히 말하면 정의 없는 사용이다.

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

Deformation retract(정의 9)의 섹션에서, $$D^2\setminus\{(0,0)\}$$의 deformation retract가 $$S^1$$이라는 결과—$$t\frac{\mathbf{x}}{\lvert\mathbf{x}\rvert}+(1-t)\mathbf{x}$$라는 homotopy—는 호몰로지 글에서 $$H_1(D^2\setminus\{(0,0)\})\neq 0$$이라는 계산과 연결된다. $$S^1$$이 $$D^2\setminus\{(0,0)\}$$의 deformation retract이므로 둘의 homology가 같다는 것이, "구멍을 포착하는 가장 작은 부분공간"이 $$S^1$$이라는 것을 보여준다. $$D^2$$에서 $$S^1$$로의 retraction이 존재하지 않는다는 것(예시 8의 functoriality argument)은 $$H_1(D^2)=0$$이지만 $$H_1(S^1)\neq 0$$이기 때문인데, retract가 존재하면 injective homomorphism $$H_1(S^1)\rightarrow H_1(D^2)$$가 있어야 한다는 모순—이 argument가 깔끔하다.

Fundamental groupoid(정의 11)의 도입이 이 글에서 가장 범주론적인 부분이다. Path들의 homotopy class를 morphism으로, $$X$$의 점들을 object로 갖는 category—이것이 groupoid([범주론] 정의 11)라는 것이 $$\alpha$$의 역원이 $$\bar{\alpha}(t)=\alpha(1-t)$$로 주어진다는 것에서 따라온다. Homotopic한 연속함수가 fundamental groupoid 사이의 natural isomorphism을 유도한다는 논증—$$F(s,t)=f_t(\alpha(s))$$—이 $$\Pi_1$$이 functor라는 것의 구체적 표현인데, 이 natural isomorphism이 $$X$$의 각 점에서의 automorphism group $$\pi_1(X,x)$$로 수렴하면서 fundamental group이 정의된다. $$\pi_1(X,x)$$가 $$\Pi_1(X)$$의 skeleton이라는 결론([범주론] 정의 4)이 범주론과 위상수학의 연결을 잘 보여준다.

좋은 점: (1) Markov 정리로 시작해서 위상적 불변량의 한계를 먼저 보여주는 구조가, 왜 homotopy equivalence를 정의하는지에 대한 동기를 자연스럽게 제공한다. (2) Prism operator의 $$n=2$$ 그림이 추상적 구성에 직관을 부여한다. (3) Deformation retract가 호몰로지의 계산과 연결되는 부분—$$D^2\setminus\{0\}$$와 $$S^1$$의 관계—이 기하학적으로 와닿는다.

아쉬운 점: (1) Fundamental groupoid approach가 범주론적으로 우아하지만, 초심자 입장에서는 path composition과 loop의 직관에서 출발하는 전통적 접근이 더 자연스러울 수 있다. 글이 범주론에 상당히 의존하고 있어서, 범주론을 건너뛴 독자는 $$\Pi_1$$의 정의에서 길을 잃을 수 있다. (2) $$\pi_1$$의 구체적 계산 예시가 $$\mathbb{R}^n$$의 trivial group밖에 없어서, nontrivial한 fundamental group—예를 들어 $$S^1$$의 $$\pi_1\cong\mathbb{Z}$$—에 대한 예시가 빠져 있다.

⚠️ 정의 없이 사용: `위상적 불변량` (topological invariant, 섹션 헤더와 본문에서 사용되지만 일반적 정의 없음)

## [피복공간](/ko/math/algebraic_topology/covering_spaces)

이 글은 호모토피에서 정의한 fundamental group $$\pi_1(X)$$를 실제로 계산하기 위한 핵심 도구인 covering space를 다룬다. 보조정리 1에서 simply connected space를 $$\pi_1(X)=0$$인 path-connected space로 정의하는데, 이 동치조건들—임의의 loop이 null-homotopic, 임의의 loop이 $$D^2$$로 확장 가능—은 호모토피 글의 deformation retract 섹션과 자연스럽게 연결된다. $$\mathbb{R}^n$$이 simply connected하지만 $$S^1$$은 아니라는 사실이, 왜 covering space가 필요한지를 보여준다: simply connected가 아닌 공간의 $$\pi_1$$을 계산하려면 "더 단순한" 공간으로의 lifting이 필요하다.

정의 3의 covering map—continuous surjection $$p:E\rightarrow B$$가 모든 점에서 evenly covered—는 본질적으로 $$B$$의 각 점 위에 $$p^{-1}(x)$$가 discrete fiber로 놓여있다는 것이고, $$p:\mathbb{R}\rightarrow S^1; t\mapsto(\cos 2\pi t,\sin 2\pi t)$$가 대표적 예시이다. 이 그림에서 $$S^1$$의 작은 열린호 위에 $$\mathbb{R}$$의 countably many open interval들이 각각 homeomorphic하게 놓여있는 것이 "고르게 덮임"의 직관인데, $$\mathbb{Z}$$의 작용으로 $$\mathbb{R}$$을 $$n\mapsto t+n$$으로 옮기면 각 fiber가 정확히 한 겹씩 덮인다는 것이 명확하다.

보조정리 6의 path lifting—임의의 path $$\alpha:I\rightarrow B$$가 주어지면 시작점 $$y_0\in p^{-1}(x_0)$$으로부터 유일한 lifting $$\widetilde{\alpha}$$가 존재한다—가 이 글의 첫 번째 핵심 결과이다. 증명의 구조가 깔끔하다: $$I$$를 Lebesgue number lemma로 유한 개의 구간으로 분할하여 각 구간이 evenly covered인 열린집합 안에 들어가게 하고, 귀납적으로 $$\widetilde{\alpha}$$를 정의한다. 각 단계에서 $$\widetilde{\alpha}(s_i)$$가 속하는 component가 연결성에 의해 유일하게 결정된다는 것이 lifting의 유일성의 핵심인데, "evenly covered + connected = 유일한 선택"이라는 패턴이 이후 보조정리 7(homotopy lifting)에서도 반복된다.

Transport map $$T_{[\alpha]}:p^{-1}(x_0)\rightarrow p^{-1}(x_1)$$과 monodromy functor $$M_p:\Pi_1(B)\rightarrow\Set$$의 정의가 글의 방향을 추상적으로 전환시킨다. $$[\alpha]$$가 fiber 위의 bijection을 정의한다는 것은, path class가 "fiber 위에서의 이동"을 지시한다는 것인데, $$\mathbb{R}\rightarrow S^1$$의 경우 $$S^1$$ 위의 loop이 $$\mathbb{Z}$$만큼 fiber를 이동시키는 것이 $$\pi_1(S^1)\cong\mathbb{Z}$$와 연결된다. $$M_p$$가 functor라는 것은 path concatenation이 fiber 위의 bijection의 합성에 대응된다는 것이고, 이것이 "topological 정보를 대수적 정보로 변환"하는 첫 단계이다.

정리 11—$$M:\Cov(B)\simeq\Fun(\Pi_1(B),\Set)$$—가 이 글의 중심 정리인데, 증명의 핵심은 "거꾸로 가는" 것이다: 임의의 functor $$F:\Pi_1(B)\rightarrow\Set$$이 주어지면 $$E=\coprod_{x\in B}F(x)$$로 집합을 만들고, transport map을 이용하여 위상구조를 부여한다. 이 위상구조를 정의하기 위해 필요한 조건—$$U$$가 path-connected(locally path-connected)이고, $$U$$ 안의 path class가 $$B$$에서 유일하게 결정됨(semi-locally simply connected)—이 정리의 가정으로 등장하는 것이 자연스럽다. 이 두 조건이 "fiber 위의 이동을 정의하기 위해 base 공간이 얼마나 잘 행동해야 하는가"를 묻는 것이라는 해석이 가능하다.

따름정리 12의 Galois correspondence—connected covering space의 isomorphism class와 $$\pi_1(B)$$의 subgroup의 conjugacy class 사이의 대응—는 범주론적 equivalence가 구체적으로 무엇을 의미하는지를 보여주는 예시이다. $$\Fun(\Pi_1(B),\Set)$$이 $$\pi_1(B)$$-set임을 관찰하고, transitive $$G$$-set의 분류($$G/H$$의 분류)를 사용하여 최종적으로 subgroup의 conjugacy class로 수렴하는 논증이, 범주론→groupoid→group→subgroup으로 가는 "추상에서 구체로의 하강"을 잘 보여준다. $$E_H$$의 Deck transformation group이 $$N_G(H)/H$$라는 결과는, covering space의 대칭성이 base 공간의 $$\pi_1$$의 구조로 읽힌다는 것을 의미하는데, universal cover $$\widetilde{B}$$의 경우 $$H=\{e\}$$이므로 Deck transformation group이 $$\pi_1(B)$$ 전체가 된다는 것이 인상적이다.

Seifert-van Kampen 정리(정리 13)는 $$X=U\cup V$$일 때 $$\pi_1(X)$$를 $$\pi_1(U)$$, $$\pi_1(V)$$, $$\pi_1(U\cap V)$$로부터 계산하는 도구인데, groupoid 버전의 증명—$$\mathcal{O}$$-shaped diagram의 colimit으로서 $$\Pi_1(X)$$를 표현—이 범주론적이다. $$\Grpd$$의 colimit을 $$\Grp$$로 내리면 free product $$\pi_1(U)\ast_{\pi_1(U\cap V)}\pi_1(V)$$가 된다는 것이 따름정리 14인데, $$S^1\vee S^1$$의 $$\pi_1$$이 free group $$F_2$$가 된다는 응용—두 원의 교집합이 한 점이므로 amalgamation이 없음—이 이 정리의 힘을 보여준다.

Hurewicz 정리(정리 15)는 $$\pi_1$$과 $$H_1$$의 관계를 $$H_1(X)\cong\pi_1(X)^{\mathrm{ab}}$$로 명시하는데, 호몰로지 글에서 $$H_1$$이 abelian group이라는 관찰과 호모토피 글에서 $$\pi_1$$이 일반적으로 non-abelian이라는 것이 여기서 만나 $$H_1$$은 정확히 $$\pi_1$$의 abelianization이라는 결론이 된다. $$h_n:\pi_n(X)\rightarrow H_n(X)$$의 일반적 정의에서 $$\pi_n$$이 사용되는데, 이 글에서는 $$\pi_n$$의 정의가 없어서 $$n\geq 2$$인 경우의 의미를 따라가기 어렵다.

좋은 점: (1) Simply connected→covering space→monodromy→Galois correspondence로 이어지는 흐름이, "fundamental group을 계산한다"는 목표를 향해 일관되게 전진한다. (2) $$\mathbb{R}\rightarrow S^1$$ 예시가 처음 등장한 이후 fiber, transport, monodromy의 모든 추상적 개념에 대해 이 구체적 예시를 참조할 수 있게 해서, 추상적 정의의 직관적 이해를 돕는다. (3) Seifert-van Kampen의 groupoid 버전과 classical 버전을 모두 제시하면서, 추상적 형태가 더 강력하지만 classical 형태가 더 계산에 유용하다는 것을 보여주는 구조가 좋다.

아쉬운 점: (1) Locally path-connected가 정의 없이 사용되고 있다—이 글의 핵심 정리(정리 11)의 가정인데, 열린집합의 기저와의 관계 등이 설명되었다면 더 좋았을 것이다. (2) $$\pi_n$$($$n\geq 2$$)의 정의가 없어서 Hurewicz 정리의 일반적 형태를 이해하기 어렵다. (3) 구체적 계산 예시—예를 들어 $$S^1$$의 covering space들을 분류하거나, torus의 $$\pi_1$$을 Seifert-van Kampen으로 계산하는 것—이 부족해서, Galois correspondence가 실제로 어떻게 작동하는지를 체감하기 어렵다.

⚠️ 정의 없이 사용: `Lebesgue number lemma` (보조정리 6 증명에서 사용, 위상수학 카테고리에서 정의되지 않음)
⚠️ 정의 없이 사용: `locally path-connected` (정리 11, 따름정리 12에서 사용)
⚠️ 정의 없이 사용: `conjugate subgroup` (따름정리 12에서 사용, 군론 카테고리에서 정의되지 않음)
⚠️ 정의 없이 사용: `pushout` (따름정리 14에서 사용, 범주론 카테고리에서 정의되지 않음)
⚠️ 정의 없이 사용: `$$\pi_n$$` ($$n\geq 2$$, Hurewicz 정리에서 사용, 호모토피 글에서 $$\pi_1$$만 정의됨)

## [호몰로지의 계산](/ko/math/algebraic_topology/computation_of_homology)

이 글은 호몰로지를 실제로 계산할 수 있는 도구들을 개발한다. 서두에서 Seifert-van Kampen 정리([피복공간] 정리 13)의 상황을 abelianization functor $$\ab:\Grp\rightarrow\Ab$$로 옮기면서, left adjoint functor는 colimit을 보존한다는 범주론적 사실([수반함자] 정리 9)로부터 $$H_1$$이 colimit을 보존해야 한다는 것을 보여주는 도입부가 인상적이다. 즉 식 (1)의 $$H_1(U\cup V)$$에 대한 pushout 공식이 단지 추측이 아니라, adjunction 구조로부터 필연적으로 따라오는 것이라는 것이 이 글의 출발점이다. 범주론의 추상적 결과가 구체적 계산 공식으로 환원되는 이 과정이, 지금까지 읽은 카테고리들의 "수확"을 느끼게 해준다.

정의 1의 relative homology—$$C_k(X,A):=C_k(X)/C_k(A)$$—는 chain group의 quotient로 정의되는데, 호몰로지 대수학의 cokernel 개념([긴 완전열])이 여기서 살아있다. $$0\rightarrow C_\bullet(A)\rightarrow C_\bullet(X)\rightarrow C_\bullet(X,A)\rightarrow 0$$이 short exact sequence이고, long exact sequence 정리([긴 완전열] 정리 1)로부터 $$\cdots\rightarrow H_k(A)\rightarrow H_k(X)\rightarrow H_k(X,A)\rightarrow H_{k-1}(A)\rightarrow\cdots$$가 따라나오는 것이 깔끔하다. Connecting map $$H_k(X,A)\rightarrow H_{k-1}(A)$$가 "relative cycle의 boundary를 취하는 것"이라는 설명이, 호몰로지 대수학에서 추상적으로 정의된 connecting homomorphism이 topology 맥락에서 어떤 의미를 가지는지를 보여준다.

정리 2의 excision theorem—$$\cl Z\subseteq\interior A$$일 때 $$H_k(X\setminus Z,A\setminus Z)\rightarrow H_k(X,A)$$가 isomorphism—은 증명이 생략되었지만, "A 안의 정보는 relative homology에서 무시된다"는 직관이 명확하다. 이 정리의 진짜 힘은 정의 3의 good pair 조건과 결합될 때 드러나는데, $$A$$가 $$U$$의 strong deformation retract([호모토피] 정의 9)라는 가정 하에서 $$H_k(X,A)\cong\widetilde{H}_k(X/A)$$라는 명제 4를 얻는 과정—3x3 diagram chasing과 excision을 조합하는 것—이 이 글에서 가장 기술적인 부분이다. $$H_k(X/A,[A])\cong H_k(X/A, U/A)$$에서 $$U/A$$가 한 점 $$[A]$$로 strong deformation retract한다는 관찰이 핵심인데, good pair의 조건이 정확히 이 deformation retract를 보장하기 위해 존재한다는 것을 느낀다.

정리 5의 simplicial homology와 singular homology의 일치—$$H_\bullet^\Delta(X)\rightarrow H_\bullet(X)$$가 isomorphism—는 $$\Delta$$-complex의 filtration $$X_0\subset X_1\subset\cdots\subset X_l=X$$에 대한 귀납법으로 증명된다. $$H_n(\Delta^k,\partial\Delta^k)$$가 $$n=k$$일 때만 nontrivial이라는 핵심 관찰—$$\Lambda$$를 하나 뺀 face로 정의하고 deformation retract를 사용하는 것—이 호모토피의 도구가 계산에 직접 쓰이는 예시이다. 이 증명이 본질적으로 Eilenberg-Steenrod 공리들을 사용하고 있다는 것이 정의 6에서 밝혀지는데, homology theory의 "공리적 성격"이 추상과 계산 사이의 다리 역할을 한다.

명제 7의 Mayer-Vietoris sequence가 이 글의 하이라이트이다. $$X=U\cup V$$일 때 long exact sequence $$\cdots\rightarrow H_{n+1}(U)\oplus H_{n+1}(V)\rightarrow H_{n+1}(X)\rightarrow H_n(U\cap V)\rightarrow H_n(U)\oplus H_n(V)\rightarrow\cdots$$를 유도하는 증명에서, mapping cone exact sequence([긴 완전열] 정의 8)를 사용하는 것이 호몰로지 대수학의 도구가 topology에서 어떻게 작동하는지를 잘 보여준다. $$\Psi(u,v)=u+v$$, $$\Phi(x)=(x,-x)$$라는 명시적 공식이 추상적 construction의 구체적 얼굴인데, Seifert-van Kampen 정리의 abelianization 버전으로서 식 (1)을 복원한다는 결론이 서두의 동기와 완벽하게 닫힌다.

좋은 점: (1) 서두의 adjunction 논증이 "왜 relative homology를 정의하는가"에 대한 동기를 범주론적으로 제공한다. (2) Excision theorem과 good pair의 조합이 quotient space와의 연결을 통해 relative homology의 기하학적 의미를 보여준다. (3) Mayer-Vietoris의 mapping cone 증명이 호몰로지 대수학의 도구가 실제로 계산에 쓰이는 것을 입증한다.

아쉬운 점: (1) Excision theorem의 증명이 생략되어서, 이 정리가 실제로 왜 성립하는지에 대한 직관이 부족하다—증명의 핵심 아이디어만이라도 있었으면 좋았을 것이다. (2) Cellular homology와 CW complex가 마지막에 한 줄로 언급되지만, 이후 글들에서 이것이 언제 도입되는지에 대한 힌트가 없다. (3) 구체적 계산 예시—예를 들어 $$S^n$$의 homology를 Mayer-Vietoris로 계산하는 것—이 없어서, 도구의 실전 활용을 체감하기 어렵다.

## [코호몰로지](/ko/math/algebraic_topology/cohomology)

이 글은 호몰로지의 dual인 코호몰로지를 정의하고, 그 위에 자연스럽게 존재하는 곱셈 구조가 호몰로지만으로는 포착할 수 없는 위상적 정보를 담고 있음을 보여준다. 서두에서 "단순히 $$H^k(X)\cong H_k(X)^\ast$$가 성립하는 것은 아니다"라고 못을 박으면서, 코호몰로지를 별도로 다뤄야 하는 동기를 명확히 한다. $$\Hom_\mathbb{Z}(-,A)$$를 chain complex에 취해 cochain complex를 만들고 그 호몰로지를 취한다는 정의 자체는 호몰로지 대수학의 Hom functor([호몰로지 대수학] 유도함자)와 자연스럽게 연결되는데, contravariant functor라는 특성—long exact sequence의 화살표 방향이 호몰로지와 반대—이름의 "co"가 붙은 이유를 실감하게 해준다.

명제 1의 universal coefficient theorem for homology—$$H_k(X;A)\cong(H_k(X)\otimes_\mathbb{Z}A)\oplus\Tor_1^\mathbb{Z}(H_{k-1}(X),A)$$—의 증명 구조가 인상적이다. $$0\rightarrow Z_\bullet\rightarrow C_\bullet\rightarrow B_{\bullet-1}\rightarrow 0$$이 split exact sequence([다중선형대수학] 완전열 명제 10)라는 관찰에서 출발하여, $$\Tor$$가 정확히 "텐서곱이 잃어버린 정보"를 측정한다는 것을 보여주는 논증이 깔끔하다. $$\delta_k$$가 inclusion $$B_k\rightarrow Z_k$$에 $$-\otimes\id_A$$를 취한 것과 같다는 관찰로부터 $$\Tor$$ 항이 자연스럽게 등장하는 과정—free resolution의 관점에서 connecting map을 해석하는 것—은 호몰로지 대수학의 도구가 계산에 직접 쓰이는 또 다른 예시이다. 명제 3의 cohomology 버전—$$H^k(X;A)\cong\Hom_\mathbb{Z}(H_k(X),A)\oplus\Ext^1_\mathbb{Z}(H_{k-1}(X),A)$$—에서 $$\Tor$$ 대신 $$\Ext$$가 등장하는 것이, "Hom은 왼쪽 정확하지만 오른쪽 정확하지 않다"는 것([호몰로지 대수학] Ext와 Tor)의 직접적 반영이라는 것을 느낀다.

de Rham cohomology 섹션은 이 글에서 가장 새로운 내용이다. $$\Omega^k(\mathbb{R}^n)$$과 exterior derivative로 cochain complex를 구성하고, $$H^k_\dR(\mathbb{R}^n)=0$$($$k>0$$)이라는 Poincaré lemma의 결론—closed form은 항상 exact—를 사용하는데, Poincaré lemma 자체가 이 글에서 정의 없이 인용되고 있다. 미분형식과 exterior derivative는 미분다양체 카테고리에서 정의될텐데, 현재 카테고리 순서상 아직 읽지 않았으므로 이 섹션의 전제를 따라가기 어렵다. $$dx\wedge dy$$의 적분 계산 예시—$$S$$ 위의 값이 1, $$\Sigma$$ 위의 값이 $$\pi$$—는 differential form을 "부분집합에 숫자를 대응시키는 함수"로 해석하는 관점을 보여주려는 의도인 것 같지만, $$\wedge$$의 정의와 pullback 없이는 이 계산의 의미를 완전히 이해하기 어렵다. coefficient group이 $$\mathbb{R}$$이면 $$\Tor$$와 $$\Ext$$ 둘 다 사라져서 $$H_k(X;\mathbb{R})\cong H_k(X)\otimes\mathbb{R}$$, $$H^k(X;\mathbb{R})\cong\Hom(H_k(X),\mathbb{R})$$라는 깔끔한 식이 된다는 관찰—$$\mathbb{R}$$이 torsion-free이자 injective $$\mathbb{Z}$$-module이라는 것—은 coefficient를 바꾸는 것만으로 계산이 얼마나 단순해지는지를 보여준다.

정리 4, 5의 일반화—$$\mathbb{Z}$$ 대신 임의의 principal ideal domain $$A$$에 대해 성립—는 $$A$$가 PID이면 free $$A$$-module의 submodule이 다시 free라는 사실([환론] 정역 정의 8)이 핵심 가정이라는 것을 본문에서 명시하고 있어서, ring theory 카테고리와의 연결이 자연스럽다. 이 일반화가 이후 Künneth 공식에서 계수환을 $$\mathbb{Z}$$가 아닌 것으로 확장할 때 직접 쓰인다는 것이, universal coefficient theorem이 "단순한 복습"이 아니라 이후 전개의 기반임을 보여준다.

Eilenberg-Zilber 정리(정리 9)—$$C_\bullet(X\times Y)\simeq(C(X)\otimes C(Y))_\bullet$$—와 Künneth 공식(따름정리 10)의 조합이 이 글의 하이라이트이다. Alexander-Whitney map이 $$C(X)$$를 coalgebra로 만든다는 관찰—$$X=Y$$일 때 $$C(X)\rightarrow C(X)\otimes C(X)$$—은 다음 글(합곱)에서 다시 등장할 것이라는 예고인데, 호몰로지의 곱 구조가 코호몰로지의 곱 구조와 어떤 관계인지에 대한 힌트를 준다. Künneth 공식의 형태—$$\bigoplus_{p+q=k}H_p\otimes H_q$$와 $$\Tor$$ 항—가 universal coefficient theorem의 구조와 정확히 parallel이라는 것이, 이 글 전체가 "텐서곱 vs Hom, $$\Tor$$ vs $$\Ext$$"라는 대수적 도구들의 체계적 전시라는 느낌을 준다.

좋은 점: (1) 서두에서 "코호몰로지는 단순한 dual이 아니다"라고 명확히 선언하면서, 왜 별도로 다뤄야 하는지에 대한 동기가 확실하다. (2) Universal coefficient theorem의 증명이 $$\Tor$$와 $$\Ext$$를 자연스럽게 유도하는 구조로 되어 있어서, 호몰로지 대수학의 도구가 실제로 어떻게 계산에 쓰이는지를 보여준다. (3) coefficient를 $$\mathbb{R}$$로 바꿨을 때 $$\Tor$$와 $$\Ext$$가 사라지는 관찰이, coefficient의 선택이 계산 복잡도에 미치는 영향을 직관적으로 보여준다.

아쉬운 점: (1) de Rham cohomology 섹션의 전제—미분형식, exterior derivative, Poincaré lemma—가 미분다양체 카테고리에서 정의될텐데, 현재 카테고리 순서상 아직 읽지 않았으므로 이 섹션을 따라가기 어렵다. (2) Mayer-Vietoris sequence(명제 6)가 제시되지만 구체적 계산 예시—예를 들어 $$S^n$$의 cohomology를 계산하는 것—이 없어서, 이 도구의 실전 활용을 체감하기 어렵다. (3) Acyclic models theorem이 별도 글로 미루어졌는데, Eilenberg-Zilber 정리의 증명 없이 결과만 사용하는 것이 다소 불만족스럽다.

⚠️ 정의 없이 사용: `differential form` (de Rham cohomology 섹션에서 사용, 미분다양체 카테고리에서 정의됨)
⚠️ 정의 없이 사용: `exterior derivative` (de Rham cohomology 섹션에서 사용, 미분다양체 카테고리에서 정의됨)
⚠️ 정의 없이 사용: `Poincaré lemma` (de Rham cohomology 섹션에서 인용, 이 카테고리에서 정의되지 않음)
⚠️ 정의 없이 사용: `wedge product` (de Rham cohomology 계산 예시에서 사용, 미분다양체 카테고리에서 정의됨)

## [Acyclic models theorem](/ko/math/algebraic_topology/acyclic_models_theorem)

이 글은 코호몰로지 글에서 언급한 Eilenberg-Zilber 정리의 원래 증명을 일반화하는 acyclic models theorem을 다룬다. 코호몰로지 노트에서 "Eilenberg-Zilber 정리의 증명 없이 결과만 사용하는 것이 다소 불만족스럽다"고 적었는데, 이 글이 그 빈자리를 정확히 채워주는 구성이다. 정의 1의 category with models—category $$\mathcal{A}$$와 object들의 모임 $$\mathcal{M}$$의 pair—는 그 자체로는 아무 내용도 없는 프레임에 불과하지만, 정의 2의 "acyclic on $$\mathcal{M}$$"과 "free on $$\mathcal{M}$$"이라는 조건이 이 프레임에 살을 붙인다. $$F_\bullet$$이 acyclic on $$\mathcal{M}$$이라는 것은 각 model $$M$$에 대해 $$H_i(F(M))=0$$ ($$i>0$$)이라는 것이고, free on $$\mathcal{M}$$이라는 것은 $$F_n(-)\cong\bigoplus_{M\in\mathcal{M}}\mathbb{Z}\Hom_\mathcal{A}(M,-)$$라는 자연동형이 성립한다는 것인데, singular chain complex $$C_\bullet$$가 standard simplex $$\Delta^n$$들을 model로 잡으면 둘 다 만족한다는 관찰이 이 정리의 동기를 잘 보여준다.

정리 3의 acyclic models theorem—$$F_\bullet$$이 free, $$G_\bullet$$이 acyclic일 때 $$H_0$$ 수준의 자연변환 $$f_0$$를 chain map $$f_\bullet$$로 lifting할 수 있고, 이 lifting은 natural chain homotopy에 대해 유일하다—의 증명 구조가 깔끔하다. $$n=0$$에서는 $$F_0(X)$$가 free이므로 generator $$u:M\to X$$의 상을 정의하면 되고, $$p_G$$의 surjectivity로 lifting이 가능하다. 귀납 단계에서는 $$f_{n-1}$$까지 정의되었다고 가정하고 $$f_n$$을 구성해야 하는데, 여기서 "model로 reduction"하는 것이 핵심이다. $$F_n$$이 free이므로 model $$M$$ 위에서만 정의하면 되고, $$\id_M$$에 해당하는 $$F_n(M)$$의 원소를 $$G_n(u)\circ f_n(M)$$으로 옮기는 것이 naturality를 보장한다. 그리고 model 위에서 $$f_{n-1}\circ d_n^{F(M)}$$의 image가 $$\ker d_{n-1}^{G(M)}$$ 안에 있다는 것은 $$F_\bullet$$의 $$d^2=0$$과 귀납 가정으로부터 따라오고, $$G$$가 acyclic이므로 $$\ker d_{n-1}^{G(M)}=\im d_n^{G(M)}$$가 되어 lifting $$y_n$$의 존재성이 보장된다. 이 귀납의 두 축—"free 조건이 reduction을 가능하게 하고, acyclic 조건이 lifting을 가능하게 한다"—이 서로 맞물리는 구조가 인상적이다.

활용 섹션에서 Eilenberg-Zilber map과 Alexander-Whitney map을 이 정리의 따름정리로 유도하는 것이, 코호몰로지 글에서 결과만 사용했던 것을 정당화해준다. $$\Top^2$$에서 $$C_\bullet(-\times -;A)$$와 $$C_\bullet(-;A)\otimes_A C_\bullet(-;A)$$를 두 functor로 잡고, model을 $$(\Delta^p,\Delta^q)$$로 잡으면 둘 다 free이자 acyclic이므로, $$H_0$$ 수준의 isomorphism $$C_p(X;A)\times C_q(Y;A)\to C_{p+q}(X\times Y;A)$$의 lifting으로 Eilenberg-Zilber map을 얻는다는 논증이 직접적이다. 비슷하게 flip map의 존재성도 같은 방식으로 따르는데, $$X\times Y$$와 $$Y\times X$$의 chain complex 사이의 교환을 보이는 것이 acyclic models theorem의 힘이라는 것을 보여준다.

좋은 점: (1) 증명의 구조—$$n=0$$에서의 lifting, 귀납 단계에서의 model reduction과 acyclic 조건의 사용—가 두 단계로 명확히 분리되어 있어서, 각 조건이 왜 필요한지가 증명 안에서 자연스럽게 드러난다. (2) 활용 섹션에서 Eilenberg-Zilber를 비롯한 기존 결과들을 이 정리의 따름정리로 한꺼번에 처리하는 것이, 이 정리의 일반성을 잘 보여준다. (3) "acyclic = homology가 trivial하다", "free = generator가 있다"는 두 조건이 "존재성"과 "유일성"을 각각 보장한다는 해석이 가능하다는 것이 흥미롭다.

아쉬운 점: (1) $$G_\bullet$$이 acyclic on $$\mathcal{M}$$이라는 조건에서 $$H_0(G(M))$$는 0이 아니어도 된다는 것이 본문에서 "주의하자"고만 언급되고 있는데, 이 점이 왜 중요한지—$$H_0$$ 수준의 자연변환 $$f_0$$를 정의하기 위해 $$H_0(G(M))$$가 nontrivial해야 한다는 것—이 더 설명되었다면 좋았을 것이다. (2) $$y_n$$의 선택이 유일하지 않다는 것이 "서로 다른 lift의 차이가 chain homotopy를 정의한다"고만 되어 있는데, 이 chain homotopy가 구체적으로 어떻게 정의되는지에 대한 명시적 공식이 없다. (3) 활용이 Eilenberg-Zilber와 flip map 두 가지만 있어서, 다른 응용—예를 들어 singular homology의 functoriality나 homotopy invariance의 증명—이 이 정리로 가능한지에 대한 힌트가 없었다.

⚠️ 정의 없이 사용: `natural chain homotopy` (정리 3에서 사용, 호몰로지 대수학에서 chain homotopy는 정의했지만 natural chain homotopy의 정의는 없음)

## [합곱](/ko/math/algebraic_topology/cup_products)

이 글은 코호몰로지 위에 자연스럽게 존재하는 곱셈 구조—cup product—를 정의하고, 이것이 graded-commutative ring을 이루며, 나아가 homology와 cohomology 사이의 duality를 포착하는 cap product까지 다룬다. 코호몰로지 글에서 "코호몰로지의 가장 큰 장점 중 하나가 이 위에 자연스럽게 정의된 곱셈구조"라고 했던 선언이 이 글에서 구체적으로 실현되는 것이다. 서두에서 "왜 homology에서는 명시적으로 보이지 않았는지"를 contravariant functor의 성격으로 설명하는 것이 동기를 잘 잡아주는데, diagonal map $$\Delta:X\rightarrow X\times X$$에 homology functor를 취하면 covariant이므로 방향이 맞지 않는다는 관찰—homology의 한계를 정확히 짚어주는 부분이다.

정의 1의 cup product—$$H^\bullet(X;A)\otimes_A H^\bullet(X;A)\overset{\Delta^\ast\circ(\AW^\ast\circ\bar{\times})}{\longrightarrow} H^\bullet(X;A)$$—는 세 단계의 합성으로 구성된다: 먼저 cross product $$\bar{\times}$$로 두 cohomology class를 $$H^\bullet(X\times X)$$로 보내고, Alexander-Whitney map의 pullback $$\AW^\ast$$로 chain 수준에서의 cross product를 얻고, 마지막으로 diagonal map의 pullback $$\Delta^\ast$$로 $$H^\bullet(X)$$로 가져온다. 명시적 계산—$$(\alpha\smile\beta)(\sigma)=(-1)^{pq}\alpha(\text{front face})\beta(\text{back face})$$—이 이 합성의 chain 수준 얼굴을 보여주는데, $$(-1)^{pq}$$ 부호가 "graded-commutativity를 위해 정확히 필요한 부호"라는 것을 이후 명제 2에서 확인하게 된다.

명제 2의 grade-commutativity—$$\alpha\smile\beta=(-1)^{pq}\beta\smile\alpha$$—는 cup product가 일반적인 commutative ring의 곱셈과 다른 점을 보여준다. $$p$$, $$q$$가 둘 다 홀수이면 부호가 $$-1$$이 되는데, 이는 코호몰로지의 contravariant 성격이 만들어내는 "부호의 비용"이다. 증명에서 acyclic models theorem([acyclic models theorem] 정리 3)을 사용한다는 것이, 이 정리가 얼마나 보편적인지를 다시 한번 보여준다. $$H^\bullet(X;A)$$가 $$\mathbb{N}$$-graded $$A$$-algebra를 이룬다는 결론은, 코호몰로지가 단순한 abelian group들의 sequence가 아니라 ring 구조를 가진다는 것을 의미하는데, homology에서는 이 구조를 직접 정의할 수 없다는 것이 대비된다.

명제 3, 4의 functoriality—$$\times: H^*(X;A)\otimes_A H^*(Y;A)\to H^*(X\times Y;A)$$가 graded algebra homomorphism이고, $$f^\ast$$가 cup product를 보존한다는 것—은 cup product가 "자연스러운" 구조임을 보여준다. 증명에서 diagonal map과 연속함수 $$f$$의 관계—$$(f\times f)\circ\Delta_{X}=\Delta_{Y}\circ f$$—가 핵심인데, 범주론 카테고리에서 배운 diagonal morphism의 naturality가 여기서 직접 쓰인다.

Cap product(정의 5)—$$\frown:H^p(X;A)\otimes H_{p+q}(X;A)\rightarrow H_q(X;A)$$—는 이 글의 후반부에서 homology와 cohomology 사이의 duality를 포착하기 위해 도입된다. 정의의 동기—adjunction formula $$\langle\alpha\smile\beta,\sigma\rangle=\langle\alpha,\beta\frown\sigma\rangle$$—가 깔끔한데, Kronecker pairing $$\langle-,-\rangle$$을 통해 cohomology가 homology 위의 "측정 장치"로서 작동하는 것을 보여준다. 명시적 공식—$$\beta\frown\sigma=\sum_i(-1)^{\lvert\beta\rvert\lvert\sigma_i\rvert}\beta(\tau_i)\sigma_i$$—이 Alexander-Whitney map의 분해 $$\AW(\sigma)=\sum\sigma_i\otimes\tau_i$$를 사용하는 것이, 코호몰로지 글에서 도입한 이 도구가 다시 살아있는 느낌이다. cap product가 "interior product에 해당하는 연산"이라는 본문의 언급은 미분형식의 interior product—벡터 장을 differential form에 대응시키는 것—과의 유추인데, 이 유추의 정확한 의미는 미분다양체 카테고리를 읽은 후에야 완전히 이해할 수 있을 것 같다.

명제 6의 projection formula—$$f_\ast(f^\ast\beta\frown\sigma)=\beta\frown f_\ast\sigma$$—는 cap product와 연속함수의 관계를 정리하는 공식인데, $$f^\ast$$와 $$f_\ast$$가 "서로 다른 방향으로 가는" 두 functor가 cap product 안에서 만나면 방향이 상쇄된다는 것이 핵심이다. 이 공식이 이후 Poincaré duality에서 사용될 것이라는 예감이 든다.

좋은 점: (1) cup product의 정의를 cross product → Alexander-Whitney → diagonal pullback의 세 단계로 분해한 구조가, "왜 homology에서는 안 되고 cohomology에서는 되는가"에 대한 답을 정의 안에 포함하고 있다. (2) 명시적 계산—$$(\alpha\smile\beta)(\sigma)=(-1)^{pq}\alpha(\text{front face})\beta(\text{back face})$$—이 추상적 합성의 chain 수준 얼굴을 보여줘서, cup product가 실제로 무엇을 하는지 직관을 잡을 수 있게 해준다. (3) Cap product의 adjunction formula가 $$\langle-,-\rangle$$이라는 하나의 pairing으로 cup과 cap을 동시에 묶는 것이, 두 연산의 관계를 명확히 한다.

아쉬운 점: (1) 구체적 계산 예시—예를 들어 $$S^n$$의 cohomology ring $$H^\bullet(S^n;A)$$를 계산하거나, torus의 cup product를 구하는 것—이 없어서, 이 도구의 실전 활용을 체감하기 어렵다. 코호몰로지 글에서도 Mayer-Vietoris 계산 예시가 없었는데, 이 글에서도 같은 문제가 반복된다. (2) Cap product의 "interior product에 해당한다"는 언급이 한 줄만 있고, interior product가 무엇인지에 대한 설명이 없어서, 이 유추의 의미를 따라가기 어렵다. (3) Grade-commutativity의 증명이 acyclic models theorem에 의존하고 있는데, 이 정리의 어떤 부분이 정확히 사용되는지에 대한 힌트가 없어서, 독자 입장에서는 "왜 acyclic models가 필요한가"를 판단하기 어렵다.

⚠️ 정의 없이 사용: `interior product` (정의 5 cap product의 본문에서 "interior product에 해당하는 연산"이라고 언급되나, 미분다양체 카테고리에서 정의될 개념으로 이 카테고리에서 정의되지 않음)

## [푸앵카레 쌍대성](/ko/math/algebraic_topology/Poincare_duality)

이 글은 호몰로지와 코호몰로지 사이의 가장 깊은 연결인 Poincaré duality를 다룬다. 핵심은 $$A$$-orientable compact $$m$$-manifold $$M$$에 대해 cap product with the fundamental class $$-\frown [M]: H^p(M;A)\rightarrow H_{m-p}(M;A)$$가 isomorphism이라는 것이다. 코호몰로지 글에서 universal coefficient theorem이 $$H^k(X;A)$$와 $$H_k(X;A)$$를 $$\Tor$$, $$\Ext$$ 항으로 연결했던 것과 달리, 이 정리는 coefficient나 대수적 도구 없이 직접적인 기하학적 isomorphism을 제공한다는 것이 인상적이다.

Orientation sheaf $$\or_M$$의 구성이 이 글의 첫 번째 핵심이다. $$U\mapsto H_m(M,M\setminus U;\mathbb{Z})$$라는 presheaf를 sheafification해서 얻는 $$\or_M$$의 stalk가 $$H_m(M,M\setminus\{x\};\mathbb{Z})\cong\mathbb{Z}$$라는 관찰—이것이 각 점에서의 "국소 방향"을 포착한다는 것—은 호몰로지가 기하학적 정보를 담고 있다는 것을 다시 한번 확인시켜준다. 특히 $$\mathbb{R}^m\setminus\{0\}$$이 $$S^{m-1}$$으로 deformation retract한다는 것([호모토피] deformation retract)과 relative homology long exact sequence를 조합해서 이 stalk가 $$\mathbb{Z}$$라는 것을 보이는 논증이 깔끔하다.

Orientation double cover $$\Spe(\omega_M)\rightarrow M$$의 예시—$$S^1$$의 경우 두 개의 component를 갖는 trivial cover, 뫼비우스 띠의 경우 원기둥과 homeomorphic한 하나의 component를 갖는 non-trivial cover—가 orientability의 차이를 시각적으로 잘 보여준다. 뫼비우스 띠를 한 바퀴 돌아왔을 때 $$(x,+)$$와 $$(x,-)$$가 뒤바뀐다는 것이 non-orientable의 본질인데, $$\pi_1(M)$$의 monodromy action이 trivial한지로 orientability를 판별할 수 있다는 명제 6(7)—$$M$$이 $$A$$-orientable iff monodromy $$\pi_1(M)\rightarrow A^\times$$가 trivial—이 [피복공간]의 Galois correspondence를 직접 사용한다. 특히 $$A=\mathbb{Z}/2$$일 때는 $$A^\times=\{1\}$$이므로 모든 manifold가 $$\mathbb{Z}/2$$-orientable이라는 결론이, $$\mathbb{Z}/2$$ coefficient가 "방향을 무시한다"는 것을 대수적으로 확인시켜준다.

보조정리 8의 증명 구조—compact set $$C$$에 대해 section $$s$$를 $$\alpha_C\in H_m(M,M\setminus C;A)$$로 lifting하는 것—이 Mayer-Vietoris sequence와 귀납법의 조합으로 진행되는 것이 이 글에서 가장 기술적인 부분이다. $$C_1\cup C_2$$에서 $$(\alpha_{C_1},-\alpha_{C_2})$$를 Mayer-Vietoris의 kernel에서 picking하는 것이 핵심인데, $$H_{m+1}(M,M\setminus(C_1\cap C_2);A)=0$$이라는 가정이 이 lifting의 유일성을 보장한다. 귀납의 base step—$$M=\mathbb{R}^m$$이고 $$C$$가 convex compact인 경우—에서 $$\mathbb{R}^m\setminus C$$와 $$\mathbb{R}^m\setminus\{x\}$$가 둘 다 $$S^{m-1}$$으로 deformation retract한다는 것이 사용되는데, convexity 조건이 정확히 이 deformation retract를 보장하기 위해 필요하다는 것을 느낀다.

Compactly supported cohomology $$H_c^p(M;A)$$의 도입—non-compact manifold에서 duality를 다루기 위해—이 이 글의 후반부 전개를 지배한다. $$H_c^p(M;A)\cong\varinjlim_K H^p(M,M\setminus K;A)$$라는 정의가 직관적이고, compact manifold에서는 $$H_c^p\cong H^p$$가 되어 원래의 Poincaré duality를 복원한다는 것이 깔끔하다. 보조정리 13의 증명—$$\mathbb{R}^m$$에서 ball의 반지름을 키워가며 directed system을 만들고, 이후 nested open subset의 union으로 일반화하는 것—이 "compact에서 non-compact로의 확장"이라는 분석학적 사고방식이 topology에서도 작동하는 예시이다.

뒤틀린 Poincaré duality—$$H^k(M;\mathscr{L})\cong H_{m-k}(M;\or_M^A\otimes\mathscr{L})$$—의 도입이 글의 마지막 부분이다. Local coefficient system $$\mathscr{L}$$를 $$\underline{A}$$로 놓고 $$\or_M^A$$가 constant sheaf인 경우를 classical Poincaré duality로 복원하는 논증이 명쾌하지만, sheaf cohomology를 정의하기 위해 도입된 Godement resolution—$$\mathscr{G}_0(U)=\prod_{x\in U}\mathscr{F}_x$$로 시작해서 flabby sheaf들의 resolution을 만드는 것—은 다소 갑작스럽다. Flabby(flasque) sheaf가 무엇인지, 왜 이것이 derived functor를 계산할 수 있는지에 대한 설명이 없어서, 이 resolution이 왜 작동하는지를 따라가기 어렵다.

좋은 점: (1) $$S^1$$과 뫼비우스 띠의 orientation double cover 예시가 orientability와 non-orientability의 차이를 시각적으로 명확히 보여준다. (2) 보조정리 8의 증명이 Mayer-Vietoris + 귀납법이라는 패턴을 반복 사용하면서, compactness의 역할을 증명 안에서 자연스럽게 드러낸다. (3) $$A=\mathbb{Z}/2$$일 때 모든 manifold가 orientable이라는 결론이 coefficient의 선택이 orientation 개념에 미치는 영향을 보여주는 것이 흥미롭다.

아쉬운 점: (1) Godement resolution과 flabby sheaf가 정의 없이 사용되어서, sheaf cohomology 섹션의 전제를 따라가기 어렵다. (2) 보조정리 8의 귀납 단계에서 $$H_{m+1}(M,M\setminus(C_1\cap C_2);A)=0$$이라는 가정이 어디서 오는지—보조정리의 둘째 주장이 이것을 보장하지만, 귀납이 시작되기 전에 이 사실을 알고 있어야 한다는 점—이 약간 순환적이다. (3) 마지막의 "Cup product는 교집합의 Poincaré dual이다"라는 선언이 매우 흥미롭지만, 예시 15의 torus 계산 외에는 이 해석을 더 발전시키지 않아서, cup product의 기하학적 의미가 여전히 흐릿하다.

⚠️ 정의 없이 사용: `flabby (flasque) sheaf` (Godement resolution에서 사용, 위상수학 카테고리에서 정의되지 않음)
⚠️ 정의 없이 사용: `general position` (예시 15에서 사용, 수학 전반에 걸친 개념이지만 이 카테고리에서 정의되지 않음)
⚠️ 정의 없이 사용: `locally constant sheaf` (정의 14 local coefficient system에서 사용, 위상수학 카테고리에서 constant sheaf는 정의했으나 locally constant의 명시적 정의는 없음)

## [특성류](/ko/math/algebraic_topology/characteristic_classes)

이 글은 covering space를 일반화한 fiber bundle과 vector bundle을 정의하고, vector bundle 위에 존재하는 cohomological invariant인 특성류를 다룬다. 정의 1의 fiber bundle—continuous surjection $$p:E\rightarrow B$$가 각 점에서 locally trivial—은 covering space의 조건에서 fiber가 discrete set이 아닌 일반 위상공간 $$F$$로 확장된 것인데, 피복공간 글에서 다룬 evenly covered 조건이 "각 점 위에 fiber가 고르게 놓여있다"는 것의 일반화라는 것이 명확하다. 정의 2의 vector bundle—fiber가 $$\mathbb{R}$$-벡터공간이고 local trivialization이 linear isomorphism을 preserve하는 것—은 이 중에서 가장 구체적인 예시인데, 각 fiber $$p^{-1}(x)$$에 vector space 구조가 부여된다는 것이 핵심이다.

예시 3의 tautological line bundle $$\gamma_1^1\rightarrow\RP^1$$이 non-trivial이라는 증명이 이 글에서 가장 기하학적으로 와닿는 부분이다. Section $$s:\RP^n\rightarrow E(\gamma_n^1)$$를 $$S^n$$ 위로 pullback하면 $$t(-\mathbf{x})=-t(\mathbf{x})$$를 만족하는 연속함수 $$t:S^n\rightarrow\mathbb{R}$$가 나오고, 중간값정리에 의해 $$t(\mathbf{x}_0)=0$$이 되어 section이 somewhere vanishing한다는 논증—이것이 Borsuk-Ulam 정리의 한 형태인데, 이 정리가 이 카테고리 어디서도 정의된 적이 없어서 증명의 전제를 따라가기 어렵다. 그럼에도 "non-trivial section은 반드시 somewhere vanishing한다"는 결론이 vector bundle의 non-triviality를 직관적으로 이해하는 데 좋은 예시라는 것은 느낀다.

Čech cohomology 섹션은 다소 갑작스럽다. Sheaf cohomology([푸앵카레 쌍대성] 정의 14)를 이미 다루었는데, 왜 또 다른 cohomology theory가 필요한지에 대한 동기가 본문에서 "local section들을 이어붙여 global section을 만드는 과정에서 살펴본다는 점에서 차이가 있다"라고만 설명되어 있다. 정의 자체—$$\check{C}^p(\mathcal{U},\mathscr{F})=\prod_{i_0,\ldots,i_p}\mathscr{F}(U_{i_0}\cap\cdots\cap U_{i_p})$$, differential $$\delta$$의 alternating sum 공식—는 호몰로지 대수학의 cochain complex 패턴과 일관되는데, "intersection 위의 section"이라는 해석이 singular cohomology의 "simplex 위의 함수"와 구조적으로 비슷하다는 것을 느낀다. 핵심 결론—$$\check{H}^1(\mathcal{U},\GL(n,\mathbb{R}))$$가 rank $$n$$ vector bundle의 isomorphism class를 분류한다는 것—은 transition function $$g_{ij}$$가 cochain이고 cocycle 조건 $$g_{ij}\cdot g_{jk}\cdot g_{ki}=\id$$이 정확히 $$\delta g=0$$이라는 관찰에서 오는데, 이 연결이 깔끔하다.

Stiefel-Whitney class의 공리적 정의(정의 5)—rank, naturality, Whitney product formula, normalization—가 이 글의 중심축이다. 공리 자체는 간결하지만, 이 공리들을 만족하는 class가 실제로 존재한다는 것이 다음 섹션에서 증명된다. $$w_i(E)\neq 0$$이면 $$n-i+1$$개의 linearly independent section이 존재할 수 없다는 해석—obstruction class로서의 역할—이 특성류의 기하학적 의미를 잘 보여준다. $$S^1$$의 line bundle이 정확히 두 종류—trivial과 tautological—밖에 없다는 관찰($$H^1(S^1;\mathbb{Z}/2)\cong\mathbb{Z}/2$$)이 Stiefel-Whitney class가 얼마나 섬세한지를 보여주는 좋은 예시이다.

그라스만 다양체 섹션이 이 글에서 가장 내용이 풍부한 부분이다. $$\Gr_k(\mathbb{R}^n)$$이 $$k(n-k)$$차원 compact manifold라는 것, Schubert cell $$\Omega_\lambda(F_\bullet)$$가 flag와 partition으로 정의되는 것, 이들의 Poincaré dual인 Schubert class $$\sigma_\lambda$$가 $$H^\bullet(\Gr_k(\mathbb{R}^n);\mathbb{Z}/2)$$를 생성한다는 것이 핵심인데, 예시 7의 $$\Gr_2(\mathbb{R}^4)$$에서 $$\sigma_{(1,0)}^2=\sigma_{(1,1)}+\sigma_{(2,0)}$$ 계산이 구체적이다. 두 flag $$F_\bullet$$과 $$F_\bullet'$$의 general position에서의 교차를 partition으로 읽는 과정—$$V$$가 $$F_2$$와 $$F_2'$$를 각각 1차원으로 만날 때, $$V$$가 $$G_3$$에 포함되는지 아닌지로 $$(1,1)$$과 $$(2,0)$$이 분리된다는 것—이 기하학적으로 와닿지만, "general position"이라는 개념이 이 카테고리에서 정의 없이 사용되고 있어서 이 계산의 전제가 불명확하다.

분류 정리—모든 rank $$k$$ vector bundle이 infinite Grassmannian $$\Gr_k(\mathbb{R}^\infty)$$의 universal bundle $$\gamma_\infty^k$$의 pullback이라는 것—이 이 글의 가장 강력한 결론이다. 증명은 생략되었지만, 이 결과가 의미하는 바는 명확하다: vector bundle의 분류 문제가 Grassmannian의 위상으로 환원된다는 것이다. $$H^\bullet(\Gr_k(\mathbb{R}^\infty);\mathbb{Z}/2)$$가 polynomial algebra이고, $$w_1,\ldots,w_k$$가 generator라는 결론—$$w_i$$가 $$\lambda_i=(i,0,\ldots,0)$$에 해당하는 Schubert class라는 것—은 특성류가 "Grassmannian의 cohomology ring에서 읽히는 정보"라는 것을 보여준다. Littlewood-Richardson rule이 Schubert class의 cup product를 계산한다는 언급이 있는데, 이 규칙이 무엇인지에 대한 정의가 없어서 이 부분의 의미를 따라가기 어렵다.

좋은 점: (1) Covering space→fiber bundle→vector bundle으로의 일반화 흐름이 자연스럽고, 각 단계에서 이전 글의 개념이 어떻게 확장되는지가 명확하다. (2) Tautological line bundle의 non-triviality 증명이 Borsuk-Ulam 정리를 사용하면서도 기하학적으로 직관적이다. (3) Čech cohomology의 transition function 해석이 vector bundle 분류와 자연스럽게 연결되는 구조가 좋다. (4) Schubert cell의 구체적 계산(예시 7)이 추상적 정의에 생명을 불어넣는다.

아쉬운 점: (1) "오일러 특성류" 섹션이 제목만 있고 본문이 없어서, 이 글이 incomplete한 상태이다. (2) Čech cohomology가 왜 필요한지에 대한 동기가 부족하다—sheaf cohomology와의 관계가 "좋은 경우에 같다"고만 되어 있어서, 어떤 상황에서 Čech가 더 유용한지 판단하기 어렵다. (3) 분류 정리의 증명이 생략되어서, universal bundle의 존재성을 어떻게 보이는지에 대한 직관이 없다. (4) 구체적 계산 예시—예를 들어 $$\RP^2$$의 Stiefel-Whitney class를 계산하거나, 어떤 vector bundle이 non-trivial인지 판별하는 것—이 부족해서, 공리와 분류 정리가 실전에서 어떻게 쓰이는지를 체감하기 어렵다.

⚠️ 정의 없이 사용: `Borsuk-Ulam 정리` (예시 3의 non-triviality 증명에서 사용, 이 카테고리에서 정의되지 않음)
⚠️ 정의 없이 사용: `general position` (예시 7의 Schubert class 계산에서 사용, 푸앵카레 쌍대성에서도 이미 지적됨)
⚠️ 정의 없이 사용: `Young diagram` (그라스만 다양체 섹션에서 사용, 이 카테고리에서 정의되지 않음)
⚠️ 정의 없이 사용: `Littlewood-Richardson rule` (그라스만 다양체 섹션에서 사용, 이 카테고리에서 정의되지 않음)
⚠️ 정의 없이 사용: `local trivialization` (Čech cohomology 섹션에서 사용, 정의 1의 homeomorphism $$\phi$$와 본질적으로 같으나 명시적 정의 없음)

### 카테고리 회고

대수적 위상수학 카테고리는 호몰로지에서 시작하여 코호몰로지, cup product, Poincaré duality를 거쳐 특성류까지—위상 공간의 "구멍"을 대수적으로 측정하는 것에서 출발하여, vector bundle의 분류 문제까지 도달하는 큰 그림을 보여주었다. 호몰로지 대수학의 도구—exact sequence, derived functor, acyclic models theorem—가 매 글마다 계산에 직접 쓰이면서, 추상적 도구가 구체적 맥락에서 살아있다는 것을 체감할 수 있었다. 가장 막혔던 지점은 de Rham cohomology와 미분형식 관련 섹션인데, 미분다양체 카테고리를 아직 읽지 않았기 때문에 이 부분의 전제를 따라가지 못했고, 특성류 글의 "오일러 특성류" 섹션이 incomplete한 것도 이와 관련이 있을 수 있다는 느낌이 든다.
