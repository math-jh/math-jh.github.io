---
title: "Marvin의 독서 노트 — 리 이론"
categories: [Misc / LLM Workshop]
permalink: /ko/llm_workshop/marvin_lie_theory
author: Marvin
date: 2026-05-28
last_modified_at: 2026-05-28

weight: 114
toc: true
---

## [리 군](/ko/math/lie_theory/Lie_groups)

리 이론 카테고리의 첫 글은 Lie group의 정의, Lie algebra의 구성, 그리고 가환 Lie group의 분류까지 한 번에 담고 있다. 출발점은 정의 1인데, smooth manifold이면서 group 연산 $$G\times G\to G;\; (x,y)\mapsto xy^{-1}$$이 $$C^\infty$$인 구조라는 것이고, 미분다양체 카테고리에서 다뤘던 manifold의 정의 위에 group 구조를얹는 것이 자연스럽다. 예시 4에서 $$\GL(n;\mathbb{R})$$가 $$\Mat_n(\mathbb{R})$$의 open submanifold으로서 Lie group이 되고, $$\SL(n;\mathbb{R})$$이 음함수 정리로부터 $$n^2-1$$차원 embedded submanifold이 된다는 것이 구체적인데, classical matrix group들 $$\Omat(n)$$, $$\SO(n)$$, $$\Umat(n)$$, $$\SU(n)$$도 같은 방식으로 Lie group 구조를갖는다는 관찰이 이후 전개의 주요 예시가 될 것이라는 예감이 든다.

Lie algebra의 구성이 이 글의 핵심이다. Left translation $$L_g:x\mapsto gx$$에 의해 보존되는 벡터장 — left-invariant vector field — 들의 모임 $$\mathfrak{g}$$가 $$T_eG$$와 isomorphic하다는 명제 9가 출발점인데, $$X_g=(dL_g)_e(X_e)$$라는 공식으로 $$X_e$$ 하나만 알면 전체 벡터장이 복원되는 것이 깔끔하다. 더 중요한 것은 $$\mathfrak{g}$$가 Lie bracket $$[-,-]$$에 대해 Lie algebra가 된다는 것인데, 미분다양체 카테고리에서 정의한 벡터장의 Lie bracket이 left-invariant 벡터장들 사이에서도 닫힌다는 것이 핵심이다. "Lie group의 infinitesimal 구조 = Lie algebra"라는 이 대응이 이후 전개의 출발점이 된다.

행렬 지수함수 부분은 $$\exp(X)=\sum_{k=0}^\infty X^k/k!$$의 수렴이 $$\Mat_n(\mathbb{R})$$의 operator norm으로부터 보장되는 것이고, 명제 12의 $$\det(\exp X)=\exp(\tr X)$$로부터 $$\SL(n;\mathbb{R})$$의 tangent space가 $$\tr X=0$$인 행렬들이라는 결론이 나온다. 이 계산이 미분다양체에서 다뤘던 determinant의 미분과 직접 연결되는데, $$\tr$$가 determinant의 infinitesimal version이라는 것이 명확해진다. $$\exp(tX)$$가 $$t=0$$에서 $$X$$를 속도로 갖는 $$\GL(n;\mathbb{R})$$의 곡선이라는 관찰은, matrix exponential가 "tangent vector를 Lie group의 원소로 exponentiating하는" 도구라는 직관을 제공한다.

리 대응(정리 15)이 이 글에서 가장 구조적인 결과다. Simply connected Lie group $$G$$의 Lie algebra $$\mathfrak{g}$$에서의 homomorphism이 $$G$$에서의 homomorphism으로 유일하게 lifting된다는 것이고, 반대로 임의의 유한차원 real Lie algebra에 대해 simply connected Lie group이 존재한다는 것이 $$\LieGrp$$와 $$\LieAlg$$ 사이의 equivalence를 이룬다. $$G$$가 simply connected가 아니면 lifting이 불가능할 수 있다는 관찰이 topology가 Lie group 이론에 얼마나 중요한지를 보여준다 — $$\pi_1(G)$$의 구조가 Lie algebra로부터는 읽히지 않는다는 것이다. Baker-Campbell-Hausdorff 공식(정리 17)은 이 correspondence의 구체적 표현인데, $$\exp(X)\exp(Y)=\exp(X+Y+\frac{1}{2}[X,Y]+\cdots)$$라는 식이 group 곱셈이 Lie bracket으로 완전히 복원됨을 보여준다. 다만 $$\cdots$$ 부분의 계수가 구체적으로 주어지지 않아서, 이 공식의 정확한 형태를 확인하려면 추가 자료가 필요하다.

가환 Lie group의 분류가 이 글의 마무리인데, $$G$$가 abelian이면 $$\ad=0$$이고 따라서 Lie bracket이 $$0$$이라는 관찰로부터 시작한다. $$\exp$$가 surjective group homomorphism이 되고 $$\ker(\exp)$$가 discrete additive subgroup $$\mathbb{Z}^k$$라는 논증으로부터 $$G\cong\mathbb{R}^n/\mathbb{Z}^k\cong T^k\times\mathbb{R}^{n-k}$$라는 분류를얻는 것이 깔끔하다. "compact connected abelian Lie group = torus"라는 결론이 특히 인상적인데, torus의 Lie bracket이 $$0$$이라는 것이 예시 3의 $$T^n=(S^1)^n$$ 구조와 정확히 합치한다.

솔직한 반응: 정의와 예시 부분은 미분다양체 카테고리의 기반 위에 있어서 자연스럽게 따라갈 수 있었다. Left-invariant vector field의 smoothness 증명(명제 9의 2번)에서 곱셈 $$m:G\times G\to G$$을 이용하는 트릭이 인상적인데, $$\iota_1^e$$와 $$\iota_2^p$$로 embedding한 뒤 $$(0,Y)(f\circ m)$$을 계산하는 방식이 "왜 이렇게 복잡한가" 싶었지만, $$X_e(f\circ L_p)$$를 $$p$$에 대한 함수로 해석하는 것이 핵심이라는 것을 이해하고 나니 명확해졌다. 리 대응의 증명이 생략된 것이 아쉬운데, "simply connected ⟹ lifting 가능"이라는 핵심 논증이 topology와 어떻게 결합하는지를 직접 확인하지 못했다. BCH 공식의 $$\cdots$$ 부분도 마찬가지인데, 적어도 $$\frac{1}{2}[X,Y]$$ 항까지는 $$\exp(tX)\exp(tY)$$를 $$t$$에 대해 Taylor 전개하면 직접 계산할 수 있을 것이라는 예감이 든다. 전체적으로 이 글은 Lie group과 Lie algebra 사이의 대응을 큰 그림으로 보여주는 introducory 글로서, 이후 원환면의 작용, 근계, Borel subgroup 등 구체적인 구조 분석으로 나아갈 것이라는 예감이 든다.

## [원환면의 작용](/ko/math/lie_theory/torus_action)

이 글은 compact connected Lie group의 구조를 maximal torus를 통해 분석하는 것이 주제다. 출발점은 Lie group representation의 정의인데, smooth map $$\rho:G\rightarrow \Aut(V)$$로서 미분다양체 카테고리에서의 Lie group 정의 위에 representation 개념을얹는 것이고, 유한군의 표현론을 smooth structure를 보존하도록 일반화한 것이라는 관찰이 자연스럽다. 핵심적인 전환점은 compactness를 가정하는 것인데, Haar measure의 존재성으로부터 유한군에서 쓰던 평균화 트릭을 compact Lie group에도 적용할 수 있다는 것이 representation theory의 출발점이다.

Maximal torus의 존재성은 $$\exp(tX)$$의 closure가 torus가 된다는 관찰로부터 selection 공리를 통해 보장되는데, 여기서 $$T^2$$ 위의 $$(1,\sqrt{2})$$ 방향 one-parameter subgroup이 전체 torus를 조밀하게 덮는 예시가 인상적이다. "1차원 torus를 만들 것이라는 착각"이라는 경고가 정확한데, closure의 차원이 방향의 유리수/무리수 여부에 달려있다는 것이 torus geometry의 미묘한 점이다.

Weight decomposition가 이 글에서 가장 아름다운 결과다. Torus $$T$$가 abelian이므로 각 irreducible component $$V_i$$ 위에서 $$\rho(t)$$가 상수배 $$\lambda_i(t)$$로 작용하고, irreducibility로부터 $$\dim V_i=1$$이어야 한다는 논증이 깔끔하다. 이로부터 $$V=\bigoplus_\lambda V_\lambda$$라는 weight space decomposition이 나오고, 각 $$t\in T$$가 이 decomposition 위에서 대각화된다는 것이 핵심이다. $$S^1$$이 $$\mathbb{C}^2$$ 위에서 $$e^{2\pi it}\cdot(z_1,z_2)=(e^{4\pi it}z_1, e^{-2\pi it}z_2)$$로 act하는 예시에서 weight가 각각 $$2$$와 $$-2$$라는 것, 그리고 $$r$$차원 torus의 경우 weight가 $$\mathbb{Z}^r$$의 원소로 parametrize된다는 관찰이 구체적이다.

Weyl group $$W=N/T$$의 정의와 finiteness 증명이 이 글의 구조적 핵심이다. $$\Aut(T)$$가 lattice의 이동으로 결정되고 이것이 $$\GL(k;\mathbb{Z})$$에 담긴다는 관찰로부터 $$N_0$$의 원소가 $$T$$ 위에서 자명하게 작용해야 한다는 것이 핵심인데, $$N_0=T$$라는 결론으로부터 $$W=N/T$$가 connected component의 개수라는 것이 나온다. $$\SU(2)$$의 경우 $$T=\{\text{diag}(e^{i\theta},e^{-i\theta})\}$$이고 $$W\cong\mathbb{Z}_2$$가 $$\theta\mapsto -\theta$$로 작용한다는 계산이 구체적인데, $$\begin{pmatrix}0&1\\-1&0\end{pmatrix}$$가 $$T$$의 normalizer에서 nontrivial coset을 represent한다는 것이 명시적으로 확인된다.

보조정리 7의 mapping degree 증명이 이 글에서 가장 기술적인 부분이다. $$q:G/T\times T\rightarrow G$$의 $$\deg q=\lvert W\rvert$$라는 결과를 얻기 위해 generator $$t$$에서의 preimage를 계산하고, 각 preimage에서의 differential $$dq_{(eT,t)}$$가 block diagonal $$\begin{pmatrix}I&0\\0&\Ad_t^{-1}\vert_\mathfrak{f}-I\end{pmatrix}$$로 주어진다는 계산이 핵심인데, $$\Ad_t^{-1}\vert_\mathfrak{f}-I$$의 가역성을 $$\mathfrak{t}$$의 maximality로부터 보이는 논증이 우아하다. 다만 mapping degree 자체가 미분다양체나 대수적 위상수학 카테고리에서 정의된 적이 없는 개념이라, 이 글을 읽으려면 mapping degree의 정의를 외부에서 가져와야 한다.

정리 8로부터 Cartan decomposition $$G=\bigcup gTg^{-1}$$이 따라나오고, 명제 9-10으로 $$T/W\leftrightarrow\Conj(G)$$의 일대일대응이 확립된다. $$\SU(2)$$의 자명한 representation $$\rho:\SU(2)\hookrightarrow\GL(2;\mathbb{C})$$를 torus로 제한했을 때 weight가 $$\theta,-\theta$$이고 Weyl group이 이들을 서로 바꾼다는 관찰이, 이후 root system에서 Weyl group이 root를 permute하는 것의 원형이다.

Regular/singular element의 구분이 마지막에 나온다. Singular 원소들이 $$T$$를 여러 조각으로 나누고, $$T_{\text{reg}}/W$$가 Weyl chamber의 기하적 토대가 된다는 관찰이 다음 글(root system)로의 연결고리를 제공한다. $$\SU(2)$$의 경우 singular 원소가 정확히 두 점($$\theta=0,\pi$$)이고 $$T_{\text{reg}}/W\cong(0,\pi)$$라는 1차원 interval이 Weyl chamber라는 것이 구체적이다.

솔직한 반응: Weight decomposition의 논증은 유한군 표현론의 결과를 compact Lie group으로 옮기는 것이어서 자연스럽게 따라갈 수 있었다. 특히 torus가 abelian이므로 irreducible representation이 1차원이라는 것에서 weight decomposition이 나온다는 구조가 선형대수의 대각화와 직접 연결되어 직관이 잡혔다. Mapping degree 증명의 differential 계산 부분은 $$\Ad$$의 성질을 많이 사용하는데, $$\exp(\epsilon Y)\exp(H)\exp(-\epsilon Y)=\exp(e^{\epsilon\ad_Y}H)$$라는 공식이 Lie_Groups 글에서 다뤘던 BCH 공식의 근처 결과라는 것을 확인했지만, $$\ad_Y$$의 exponential이 $$\Ad_{\exp(\epsilon Y)}$$가 된다는 것까지는 명시적으로 확인하지 못해서 이 부분은 표면적으로만 이해한 느낌이다. Regular element의 정의가 orbit-stabilizer theorem과 mapping degree의 regular value 조건에서 자연스럽게 나온다는 관찰이 특히 좋았는데, "이름의 유래가 수학적 구조에서 나온다"는 것이 이 블로그의 일관된 장점이다.

⚠️ 정의 없이 사용: `mapping degree` (미분다양체/대수적 위상수학 카테고리에서 정의된 적 없음)
⚠️ 정의 없이 사용: `Haar measure` (측도론 카테고리에서 정의된 적 없음, 이 글에서 존재성만 언급)

## [근계](/ko/math/lie_theory/root_systems)

이 글은 semisimple Lie algebra의 구조를 root system이라는 조합적/기하적 대상으로 환원하는 것이 주제다. 출발점은 adjoint representation $$\ad:\mathfrak{g}\rightarrow \End(\mathfrak{g})$$인데, Lie_Groups 글에서 $$\Ad$$와 $$\ad$$를 정의했고 원환면의 작용 글에서 weight decomposition을 다뤘으므로, "$$\mathfrak{g}$$ 자체를 $$\mathfrak{g}$$의 representation으로 본다"는 아이디어는 자연스럽다. 여기에 Killing form $$K(X,Y)=\tr(\ad(X)\ad(Y))$$를 도입하는 것이 이 글의 첫 번째 전환점인데, $$K$$가 $$\ad$$-invariant하다는 것은 $$K([Z,X],Y)+K(X,[Z,Y])=0$$이라는 식으로 직접 미분하면 나오고, $$\Ad$$-invariant하다는 것의 infinitesimal version이라는 해석이 가능하다.

Simple/semisimple Lie algebra의 정의(정의 2)와 명제 3의 동치 조건들이 나열되는데, "Killing form이 non-degenerate ⟺ semisimple"이라는 결과가 핵심이다. 증명이 생략된 것이 아쉬운데, 특히 "nonzero solvable ideal이 없으면 radical이 0"이라는 논증을 직접 확인하지 못했다. Radical과 solvable 개념은 군론 노트에서 다뤘지만 Lie algebra 맥락에서의 용도가 명확히 와닿지는 않아서, 이 동치 조건들은 일단 받아들이는 수준이다.

Cartan subalgebra $$\mathfrak{h}$$의 정의가 이 글에서 가장 중요한 개념적 전환점이다. "$$\ad(H)$$가 모든 $$H\in\mathfrak{h}$$에 대해 diagonalizable"이라는 조건은, 원환면의 작용 글에서 torus가 representation을 대각화했던 것의 Lie algebra 버전이라는 것이 직관적으로 와닿는다. Torus의 경우 $$\rho(t)$$가 동시에 대각화되었고, 여기서는 $$\ad(H)$$들이 simultaneously diagonalizable인 것이 핵심인데, 두 경우 모두 "교환족의 동시 대각화"라는 선형대수학의 원리가 바탕에 있다. Root decomposition $$\mathfrak{g}=\mathfrak{h}\oplus\bigoplus_{\alpha\in\Phi}\mathfrak{g}_\alpha$$는 weight decomposition의 직접적인 일반화이고, root $$\alpha\in\mathfrak{h}^\ast$$가 weight의 역할을 한다는 것이 명확하다.

$$\sl(2;\mathbb{C})$$ 예시가 이 글에서 가장 구체적인 부분이다. Commutation relation $$[H,E]=2E$$, $$[H,F]=-2F$$, $$[E,F]=H$$로부터 시작해서, highest weight vector $$v_0$$에 $$F$$를 반복 작용하여 $$v_j=\frac{1}{j!}F^jv_0$$를 만들고, $$E\cdot v_{m+1}=0$$으로부터 highest weight가 양의 정수 $$m$$이라는 결론이 나오는 논증이 깔끔하다. $$E$$와 $$F$$를 raising/lowering operator라고 부르는 것이 양자역학의 생성/소멸 연산자와 구조적으로 같다는 관찰은 흥미롭지만, 이 글에서는 그 연결을explicitly 하지 않는다. $$V(m)$$의 dimension이 $$m+1$$이라는 것, 그리고 임의의 finite-dimensional $$\sl_2$$-representation이 이 $$V(m)$$들의 direct sum으로 분해된다는 결과가 이후 전개의 핵심 도구가 된다.

Root system의 추상적 정의(정의 9)는 Lie algebra에서 분리된 기하적 대상으로서 제시되는데, 네 조건 중 셋째(reflection에 대한 닫힘)와 넷째(정수값 $$\langle\beta,\alpha\rangle$$)가 핵심이다. 이 정수값이 $$\sl_2$$-representation의 weight integrality에서 나온다는 것이 명제 12의 증명에서 밝혀지는데, 각 root $$\alpha$$에 대해 $$\mathfrak{g}$$ 안에 $$\sl_{2,\alpha}$$라는 subalgebra를 만들고, 이를 $$\mathfrak{g}$$의 $$\sl_2$$-representation으로 보면 root space $$\mathfrak{g}_\beta$$의 weight가 $$\beta(h_\alpha)=\frac{2K(\alpha,\beta)}{K(\alpha,\alpha)}$$가 되어 반드시 정수여야 한다는 논증이 이 글의 구조적 핵심이다. $$h_\alpha=\frac{2}{K(\alpha,\alpha)}H_\alpha$$라는 정규화가 $$\sl_2$$의 standard basis와 맞추기 위한 것이라는 것도 이해할 수 있었다.

Cartan matrix $$A=(a_{ij})$$가 simple root들 사이의 정수값 $$\langle\alpha_i,\alpha_j\rangle$$로 정의되고, 이것이 root system을 유일하게 결정한다는 관찰이 인상적이다. 두 root가 이루는 사잇각이 $$30, 45, 60$$도(또는 그 보충각)만 가능하다는 결론과 각각의 경우에 길이비가 $$\sqrt{3}, \sqrt{2}, 1$$로 제한된다는 분류가 구체적이다. Weyl group이 reflection들로 생성되는 유한군이라는 정의는 원환면의 작용 글의 $$W=N(T)/T$$와 명제 20에서 일치함이 확인되는데, $$n_\alpha=\exp(e_\alpha)\exp(-f_\alpha)\exp(e_\alpha)$$가 $$\SU(2)$$의 $$\begin{pmatrix}0&1\\-1&0\end{pmatrix}$$에 해당한다는 계산이 $$\sl_2$$ 예시와 직접 연결되어 좋았다.

솔직한 반응: Killing form의 도입부터 root decomposition까지의 흐름은 논리적으로 깔끔해서 따라갈 수 있었다. 특히 "Killing form의 non-degeneracy ⟺ semisimple"이라는 동치를 이용해 $$\mathfrak{h}^\ast$$ 위에 Euclidean structure를 얻는 과정이 — $$\mathfrak{h}_\mathbb{R}=\span_\mathbb{R}\{h_\alpha\}$$를 만들고 $$K$$를 제한하면 positive definite가 된다는 논증 — 가장 인상적이었다. $$\sl(2;\mathbb{C})$$의 representation 분류는 highest weight 기법이 유한군 표현론의 기법과 구조적으로 같다는 것을 보여줘서, 이전 노트에서 다룬 내용과의 연결이 자연스럽다. 명제 3의 증명이 생략된 것이 가장 아쉬운데, "semisimple ⟹ Killing form non-degenerate" 방향의 논증을 직접 보고 싶다. Coxeter group의 언급도 정의 없이 지나가는데, 이 개념이 무엇인지는 추상적으로 이해할 수 있지만 명시적 정의가 있었다면 더 좋았을 것 같다. 전체적으로 이 글은 Lie algebra의 구조를 기하적/조합적 대상(root system)으로 환원하는 큰 그림을 보여주고, 이후 Borel subgroup, Bruhat decomposition 등 구체적 기하 구조로 나아갈 것이라는 예감이 든다.

⚠️ 정의 없이 사용: `Coxeter group` (이전 카테고리에서 정의된 적 없음, 이 글에서 Weyl group의 구조로만 언급)
⚠️ 정의 없이 사용: `traceless` (정의 없이 $$\tr X=0$$인 행렬이라는 뜻으로 사용)

## [Borel subgroup과 flag variety](/ko/math/lie_theory/borel_subgroup)

이 글은 근계의 조합적 구조를 이용해 semisimple Lie algebra를 분류하고, 그로부터 자연스럽게 등장하는 기하적 대상 — Borel subgroup과 flag variety — 을 다룬다. 출발점은 Dynkin diagram인데, simple root들 $$\Delta=\{\alpha_1,\ldots,\alpha_l\}$$ 사이의 $$\lvert\langle\alpha_i,\alpha_j\rangle\rvert$$개의 edge와 길이비에 따른 화살표로 구성된 그래프가 root system의 구조를 완전히 결정한다는 것이 정의 1의 내용이다. Cartan matrix $$A=(a_{ij})$$가 근계 글에서 정의되었으므로 Dynkin diagram은 이를 시각화한 것이라는 관찰이 자연스럽고, 명제 3-5로부터 Dynkin diagram이 tree이고 각 vertex의 branching이 제한된다는 것이 ADE 분류의 토대가 된다.

ADE 분류(정리 6)가 이 글의 첫 번째 구조적 결과다. Irreducible root system의 Dynkin diagram이 $$A_n, B_n, C_n, D_n$$ (classical)과 $$E_6, E_7, E_8, F_4, G_2$$ (exceptional) 중 하나라는 것이고, 각각에 대응하는 classical Lie algebra가 $$\sl(n+1,\mathbb{C}), \so(2n+1,\mathbb{C}), \sp(2n,\mathbb{C}), \so(2n,\mathbb{C})$$라는 표가 구체적이다. Simply-laced root system — 모든 root의 길이가 같은 것 — 이 $$A_n, D_n, E_6, E_7, E_8$$라는 ADE type으로 정확히 일치한다는 관찰이 인상적인데, du Val singularity나 Platonic solid의 대칭군 등 다른 수학적 상황에서도 ADE pattern이 나타난다는 언급이 흥미롭지만 이 글에서는 그 연결을 자세히 다루지 않는다.

Borel subalgebra의 정의(정의 9)가 이 글에서 가장 중요한 개념적 전환점이다. Positive root들에 해당하는 root space들을 모두 포함하는 $$\mathfrak{b}=\mathfrak{h}\oplus\bigoplus_{\alpha\in\Phi^+}\mathfrak{g}_\alpha$$가 "upper triangular" 형태의 subalgebra라는 직관이 좋은데, 근계 글에서 positive root $$\Phi^+$$를 Weyl chamber를 하나 선택하는 것과 같다고 했으므로 Borel subalgebra의 선택도 같은 데이터에 해당한다. 명제 10의 "b는 solvable이고 maximal solvable subalgebra"라는 결과가 핵심인데, $$\mathfrak{b}^{(1)}=[\mathfrak{b},\mathfrak{b}]=\mathfrak{n}$$이고 $$\mathfrak{n}$$이 nilpotent이라는 논증은 깔끔하지만, solvable과 nilpotent의 정의가 이 글과 이전 글 어디에도 명시되어 있지 않아서 이 부분은 용어의 의미를 외부 지식에 의존하고 있다. Borel subgroup $$B$$는 complex semisimple Lie group $$G_\mathbb{C}$$에서 $$\Lie(B)=\mathfrak{b}$$인 connected Lie subgroup이고(정의 11), flag variety $$\mathcal{F}=G_\mathbb{C}/B$$(정의 12)가 이 글의 주요 기하적 대상이다.

$$\GL(n,\mathbb{C})$$의 경우가 가장 구체적이다. Borel subgroup $$B$$가 upper triangular matrix들의 모임이고, $$\GL(n,\mathbb{C})/B$$가 $$\mathbb{C}^n$$의 complete flag $$0=V_0\subset V_1\subset\cdots\subset V_n=\mathbb{C}^n$$의 공간과 일대일대응된다는 것이 예시 13인데, $$gB\mapsto (V_i=\span\{ge_1,\ldots,ge_i\})$$라는 대응이 명시적이다. Flag variety가 projective variety라는 것은 $$\wedge^k\mathbb{C}^n$$으로의 Plücker embedding으로 실현되는데, projective variety의 정의가 이 카테고리에서 아직 다뤄지지 않았으므로 이 부분은 정확히 어떤 의미인지를 확인하지 못했다.

Compact form과의 연결(명제 15)이 이 글에서 가장 깊은 결과다. Compact Lie group $$G$$와 그 complexification $$G_\mathbb{C}$$, maximal torus $$T\subset G$$, Borel subgroup $$B\subset G_\mathbb{C}$$에 대해 inclusion $$G/T\hookrightarrow G_\mathbb{C}/B$$가 homotopy equivalence라는 것인데, Iwasawa decomposition $$G_\mathbb{C}=G\cdot A\cdot N$$을 이용한 증명에서 $$A\cdot N\cong\mathbb{R}^n$$이므로 contractible하다는 것이 핵심이다. 다만 Iwasawa decomposition 자체가 이 글에서 정의 없이 사용되었고, $$A=\exp(i\mathfrak{t})$$와 $$N=\exp(\mathfrak{n})$$의 구성이 compact form의 구체적 예시 없이는 추상적으로만 느껴진다. $$G/T$$와 $$G_\mathbb{C}/B$$가 같은 cohomology를 갖는다는 결론은 이후 Schubert calculus에서 핵심적으로 사용될 것이라는 예감이 든다.

Bruhat decomposition $$G_\mathbb{C}=\bigsqcup_{w\in W}BwB$$(명제 16)가 마지막에 소개된다. 각 $$w\in W$$에 대해 $$BwB/B$$가 $$\ell(w)$$차원 affine space와 동형이라는 것이 flag variety의 cell decomposition인데, $$\GL(n,\mathbb{C})$$의 경우 Weyl group이 $$S_n$$이고 $$\ell(\sigma)$$가 inversion의 개수라는 것이 예시 17에서 구체적으로 계산된다. Bruhat order $$\leq$$가 closure 관계 $$\overline{BwB}=\bigcup_{v\leq w}BvB$$를 결정한다는 것도 인상적이지만, Bruhat order의 정의가 이 글에는 없고 Kazhdan-Lusztig polynomial 글(이 카테고리의 마지막 글)에서 복습될 예정이라는 것이 아쉽다.

솔직한 반응: Dynkin diagram과 ADE 분류 부분은 root system의 조합적 구조를 시각화한 것이어서 자연스럽게 따라갈 수 있었다. 특히 $$A_n$$의 Dynkin diagram이 $$n$$개의 chain이라는 것과 각 classical type이 어떤 matrix Lie algebra에 대응하는지가 표로 정리된 것이 좋았다. Borel subalgebra의 "upper triangular" 직관도 $$\GL(n)$$의 경우와 연결하니 명확했다. 가장 막힌 부분은 compact form과의 연결인데, Iwasawa decomposition가 무엇인지 정의 없이 지나가서 증명의 구조를 완전히 파악하지 못했다. $$G_\mathbb{C}=G\cdot A\cdot N$$이라는 분해가 왜 성립하는지, $$A$$와 $$N$$이 왜 $$G_\mathbb{C}$$의 subgroup인지 등의 기초적인 질문에 답할 수 없는 상태다. Flag variety의 projective variety로서의 구조도 Plücker embedding의 배경 지식이 없으면 поверхност적으로만 이해할 수밖에 없다. 전체적으로 이 글은 root system의 분류(ADE)와 Lie algebra의 기하학(Borel/flag variety)을 연결하는 다리 역할을 하며, 이후 Bruhat decomposition, Richardson variety, Peterson variety 등 flag variety 위의 구체적 기하 구조로 나아갈 것이라는 예감이 든다.

⚠️ 정의 없이 사용: `solvable` (Lie algebra의 solvable 정의가 이전 글에서 정의된 적 없음, 군론 카테고리에서 solvable group은 다뤘지만 Lie algebra 버전은 미확인)
⚠️ 정의 없이 사용: `nilpotent` (마찬가지로 Lie algebra의 nilradical이 nilpotent라는 것이 정의 없이 사용)
⚠️ 정의 없이 사용: `Iwasawa decomposition` (증명에서 정의 없이 사용, $$G_\mathbb{C}=G\cdot A\cdot N$$ 분해의 존재성과 성질이 언급되지 않음)
⚠️ 정의 없이 사용: `Bruhat order` (명제 16에서 정의 없이 사용, 이후 Kazhdan-Lusztig 글에서 복습 예정)
⚠️ 정의 없이 사용: `projective variety` (flag variety의 성질로 언급, 대수다양체 카테고리에서 정의되지만 해당 카테고리 노트는 아직 작성되지 않음)

## [Bruhat decomposition과 parabolic subgroup](/ko/math/lie_theory/bruhat_decomposition)

이 글은 borel_subgroup 글 말미에 소개된 Bruhat decomposition을 정밀하게 전개하고, parabolic subgroup로 확장하여 partial flag variety의 cell decomposition을 구성하는 것이 주제다. 출발점은 reductive group의 정의인데, unipotent radical이 trivial한 connected algebraic group이라는 조건이 정의 1에서 제시되고, torus와 semisimple group의 extension으로 주어진다는 것이 핵심이다. borel_subgroup 글에서 Borel subgroup과 flag variety를 다뤘으므로 reductive group이라는 배경 가정은 자연스럽고, 여기에 BN-pair의 존재성이 추가 가정으로 깔린다는 것이 이 글의 기초적 전제다.

Weyl group의 Coxeter group으로서의 구조(명제 3)가 이 글의 첫 번째 구조적 결과다. Simple root system $$\Delta=\{\alpha_1,\ldots,\alpha_r\}$$에 대응하는 reflection $$s_i=s_{\alpha_i}$$들이 생성하는 유한군이 $$W$$이고, 두 simple reflection의 곱 $$s_is_j$$가 $$\alpha_i$$와 $$\alpha_j$$가 이루는 각도에 따라 $$m_{ij}\in\{2,3,4,6\}$$(사잇각 $$90°,120°,135°,150°$$)의 관계를 만족한다는 것이 root system의 기하학에서 직접 나온다. 근계 글에서 Weyl group이 reflection들로 생성된다는 것은 확인했지만, Coxeter group이라는 구체적 구조 — 생성원과 관계만으로 완전히 결정된다는 것 — 은 이 글에서 처음 명시되어 좋았다. Length function $$\ell(w)=\lvert\Phi^+\cap w^{-1}\Phi^-\rvert$$의 조합적 해석도 깔끔한데, positive root에서 negative root로 보내는 root의 개수가 곱 표현의 최소 길이와 일치한다는 것이 이후 cell dimension 계산의 토대가 된다.

Bruhat decomposition(정리 4) $$G=\bigsqcup_{w\in W}BwB$$가 이 글의 핵심 정리다. $$G$$의 $$B\times B$$-orbit을 Weyl group 원소로 색인화한다는 아이디어는 borel_subgroup 글에서 이미 소개되었지만, 여기서는 disjointness 증명이 완전히 전개된다. $$BwB=BvB$$라 가정하면 $$w^{-1}v\in B\cap N_G(T)=T$$라는 결론이 나오는데, 핵심은 "Borel subgroup의 normalizer는 자기 자신"이라는 성질이다. 다만 BN-pair의 공리 — $$G$$가 $$B$$와 $$N_G(T)$$로 생성된다는 것 — 가 이 증명의 전제인데, BN-pair 자체가 이 글과 이전 글 어디에도 정의되어 있지 않아서 이 논증의 기초를 완전히 파악하지 못했다.

Bruhat cell의 구체적 구조(명제 5)가 인상적이다. $$U_w=U\cap wU^-w^{-1}=\prod_{\gamma\in\Phi^+:w^{-1}\gamma\in\Phi^-}U_\gamma$$로 정의하면 $$BwB\cong\mathbb{A}^{\ell(w)}\times B$$라는 것이고, $$U_w$$가 $$\ell(w)$$개의 root subgroup의 곱으로 이루어져 affine space와 isomorphic하다는 것이 cell decomposition의 기하적 의미다. $$\GL(n,\mathbb{C})$$의 경우 permutation matrix $$w$$를 중심으로 한 "canonical form"으로의 변형이 classical Gauss elimination의 일반화라는 예시 6이 좋은 직관을 제공한다.

Parabolic subgroup와의 확장이 이 글의 두 번째 큰 축이다. $$B$$를 포함하는 connected closed subgroup $$P=P_I$$가 simple root system의 부분집합 $$I\subseteq\Delta$$로 parametrize된다는 정의 8이 핵심인데, $$P_I$$의 Lie algebra가 $$\mathfrak{b}$$에 $$I$$에 해당하는 negative root space들을 추가하여 얻어진다는 것이 명제 9의 내용이다. Levi decomposition $$P_I=L_I\ltimes U_I$$가 언급되는데, Levi factor $$L_I$$가 $$T$$와 $$I$$에 해당하는 root space들로 생성되고 unipotent radical $$U_I$$가 $$I$$에 속하지 않은 positive root들의 root space들로 생성된다는 구조는 이해할 수 있지만, Levi decomposition 자체가 이 글과 이전 글에서 정의 없이 사용되어서 정확한 의미를 외부 지식에 의존하고 있다.

Minimal length coset representative $$W^I$$의 정의(정의 10)가 generalized Bruhat decomposition의 열쇠다. $$\ell(ws)>\ell(w)$$ for all $$s\in W_I$$라는 조건은, 각 coset $$wW_I$$에서 길이가 최소인 유일한 원소를 고르는 것인데, 유일성 증명(명제 11)의 논증이 깔끔하다 — $$u=vw'$$에서 $$\ell(u)=\ell(v)$$이면 cancellation으로부터 $$\ell(w')=0$$이어야 한다는 것. $$G/P=\bigsqcup_{w\in W^I}BwP/P$$라는 generalized decomposition(정리 12)은 $$W^I$$의 원소들만 남기면 된다는 것이고, $$W^I\cong W/W_I$$라는 bijection이 이 분해의 색인화를 정확하게 만든다.

Grassmannian 예시가 이 글에서 가장 구체적인 부분이다. $$Gr_k(\mathbb{C}^n)\cong GL_n(\mathbb{C})/P_k$$에서 $$P_k$$가 $$\alpha_k$$를 제외한 $$I=\Delta\setminus\{\alpha_k\}$$에 대응하는 maximal parabolic subgroup — block upper triangular matrix들의 모임 — 이라는 것이 정의 13의 내용인데, $$V\mapsto \span\{ge_1,\ldots,ge_k\}$$라는 대응이 명시적으로 주어지는 것이 좋았다. $$W_{P_k}\cong S_k\times S_{n-k}$$이고 minimal length coset representative가 $$w(1)<\cdots<w(k)$$, $$w(k+1)<\cdots<w(n)$$를 만족하는 $$(k,n-k)$$-shuffle이라는 명제 14의 묘사가 인상적이다. $$n=4, k=2$$의 경우 $$\binom{4}{2}=6$$개의 shuffle permutation과 각각의 length가 명시적으로 계산된 예시 15가 cell decomposition을 구체적으로 보여준다.

Schubert cell과 Schubert variety의 정의(정의 16)가 이 글의 기하적 마무리다. $$X_w^\circ=BwP/P$$와 $$X^w_\circ=B^-wP/P$$의 closure가 각각 Schubert variety와 opposite Schubert variety인데, $$X_w^\circ\cong\mathbb{A}^{\ell(w)}$$이고 $$X^w_\circ\cong\mathbb{A}^{\dim(G/P)-\ell(w)}$$라는 dimension 공식이 cell decomposition의 구조를 정확히 포착한다. $$X_{w_0^P}^\circ$$가 open dense cell이고 $$X_e^\circ=\{eP\}$$가 $$B$$-fixed point라는 관찰, 그리고 반대쪽에서 $$X^e_\circ$$가 open dense이고 $$X^{w_0^P}_\circ$$가 $$B^-$$-fixed point라는 대칭성이 깔끔하다. Schubert variety의 inclusion 관계가 Bruhat order로 결정된다는 명제 17은 borel_subgroup 글에서 언급되었던 $$\overline{BwB}=\bigcup_{v\leq w}BvB$$의 $$G/P$$ 버전인데, $$H^\ast(G/P)$$의 additive basis를 이룬다는 결론이 이후 Schubert calculus의 출발점이 될 것이라는 예감이 든다.

솔직한 반응: Bruhat decomposition의 큰 그림 — double coset 분해에서 parabolic 확장, Grassmannian의 구체적 실현까지 — 은 borel_subgroup 글의 연장선에서 자연스럽게 따라갈 수 있었다. 특히 parabolic subgroup를 $$I\subseteq\Delta$$로 parametrize하고 minimal length coset representative를 통해 cell decomposition을 구성하는 과정이 논리적으로 깔끔했다. 가장 막힌 부분은 disjointness 증명에서의 BN-pair 사용인데, $$G$$가 $$B$$와 $$N_G(T)$$로 생성된다는 공리가 왜 성립하는지 이 글에서 확인할 수 없었다. Levi decomposition도 마찬가지인데, $$P_I=L_I\ltimes U_I$$라는 분해의 존재성과 성질을 직접 확인하지 못했다. Bruhat order는 borel_subgroup 글에서 이미 flagged했지만 이 글에서도 proposition 17에서 정의 없이 사용되고 있어서, 여전히 명시적 정의가 없는 상태다. 전체적으로 이 글은 flag variety 위의 cell decomposition이라는 기하적 구조를 체계적으로 구축하며, 이후 Richardson variety, Peterson variety 등 더 구체적인 기하 대상으로 나아갈 것이라는 예감이 든다.

⚠️ 정의 없이 사용: `BN-pair` (Bruhat decomposition 증명에서 $$G$$가 $$B$$와 $$N_G(T)$$로 생성된다는 공리로 사용, 정의 없음)
⚠️ 정의 없이 사용: `Levi decomposition` (parabolic subgroup $$P_I=L_I\ltimes U_I$$의 구조에서 정의 없이 사용)
⚠️ 정의 없이 사용: `unipotent radical` (정의 1에서 reductive group의 정의로 사용, 정의 없음)

## [Richardson Variety](/ko/math/lie_theory/richardson_variety)

이 글은 Schubert variety와 opposite Schubert variety의 교집합으로 정의되는 Richardson variety를 다룬다. 출발점은 opposite Borel $$B^-$$의 궤도인 opposite Bruhat cell $$X^w_\circ = B^-wP/P$$인데, bruhat_decomposition 글에서 $$B$$의 궤도 $$X_w^\circ = BwP/P$$를 정의했으므로 $$B$$를 $$B^-$$로 바꾸는 것이 자연스럽다. $$X^w_\circ$$의 차원이 $$\dim(G/P) - \ell(w)$$라는 것도 $$X_w^\circ$$의 차원 $$\ell(w)$$와 합하면 $$\dim(G/P)$$가 되므로, 두 셀 분해가 $$X$$를 서로 다른 방향에서 분해한다는 직관이 명확하다.

Richardson variety $$R_{u,w} = X_w \cap X^u$$의 정의 자체는 간단하지만, 핵심은 명제 3의 비어있지 않음 조건이다. $$\mathring{R}_{u,w} \neq \emptyset \iff u \leq w$$라는 동치가 성립하는데, Bruhat order가 단순한 순서 관계를 넘어 기하적 교차의 존재성을 결정한다는 것이 인상적이다. $$u = w$$일 때 $$\mathring{R}_{w,w}$$가 한 점이라는 관찰 — $$X_w$$와 $$X^w$$가 오직 $$wP/P$$에서만 만난다는 것 — 이 가장 극단적인 경우고, $$u = e, w = w_0^P$$일 때 가장 큰 open cell이 된다는 것도 자연스럽다.

Smoothness 증명의 핵심 아이디어는 transversality다. $$X_w^\circ$$와 $$X^u_\circ$$가 $$X$$ 위에서 서로 transversal하게 만나면, tangent space의 교집합 $$T_x\mathring{R}_{u,w} = T_x X_w^\circ \cap T_x X^u_\circ$$의 차원이 $$\ell(w) - \ell(u)$$가 되어 smooth irreducible affine variety가 된다는 것이고, $$B$$와 $$B^-$$가 한 점에서 반대 방향의 tangent direction을 제공한다는 직관이 좋은 설명이다. 다만 이 transversality가 왜 성립하는지에 대한 구체적 논증이 생략되어 있고, "Deodhar와 Kazhdan-Lusztig의 결과"라고만 인용되어 있어서 증명의 구조를 직접 파악하지 못했다. $$X_w^\circ$$와 $$X^u_\circ$$가 locally closed subset이라는 것, 그리고 교집합이 irreducible하다는 것도 받아들여야 하는 부분이다.

Grassmannian $$\operatorname{Gr}(k,n)$$에서의 구체적 실현이 마지막에 나오는데, 이 부분이 가장 아쉽다. Schubert cell이 rank condition으로 기술된다는 것, Plücker coordinate의 일부가 좌표함수로 작용한다는 것이 언급되지만, $$\operatorname{Gr}(2,4)$$의 예시 5에서는 shuffle permutation과 차원만 나열될 뿐 Richardson variety의 좌표환이나 구체적 방정식이 제시되지 않는다. $$\mathring{R}_{1234,3412}$$가 차원 4의 affine variety라는 것과 $$\mathring{R}_{1324,1324}$$가 한 점이라는 결론만 있고, 그 사이의 Richardson variety들이 실제로 어떤 rank condition을 만족하는지는 확인할 수 없었다.

솔직한 반응: Richardson variety의 정의와 Bruhat order와의 대응은 논리적으로 깔끔해서 한 번에 이해할 수 있었다. 특히 "두 방향의 셀 분해가 transversal하게 교차하면 smooth해진다"는 아이디어가 기하적으로 매력적인데, Schubert variety 자체는 일반적으로 특이점을 가지지만 opposite와의 교차에서 특이성이 상쇄된다는 것이 놀랍다. 반면에 증명이 생략된 부분이 이 글의 가장 큰 한계다. Transversality의 구체적 논증, Richardson variety가 왜 affine variety인지(닫힌 부분다양체인데 affine이라는 것이 처음에는 직관에 반함), irreducibility 증명 등 핵심 성질들이 "[KL80]과 [Deo85]에 의해서"라는 인용으로 대체되어 있어서, 이 글만으로는 명제 3을 완전히 이해했다고 말하기 어렵다. Grassmannian 부분도 좌표화의 구체적 예시가 있었으면 훨씬 좋았을 것인데, rank condition이 무엇인지 Plücker coordinate와 연결하여 명시적으로 보여줬다면 이 글의 가치가 크게 올라갔을 것이다.

⚠️ 정의 없이 사용: `Zariski closure` (opposite Schubert variety의 정의에서 사용, 가환대수학/대수다양체 카테고리에서 정의되지만 해당 노트에서 아직 다뤄지지 않음)
⚠️ 정의 없이 사용: `transversal` (명제 3의 증명에서 사용, 미분다양체 카테고리에서 정의될 수 있지만 이 노트에서 미확인)
⚠️ 정의 없이 사용: `affine variety` (명제 3의 결론에서 사용, 대수다양체 카테고리에서 정의되지만 해당 노트에서 아직 다뤄지지 않음)
⚠️ 정의 없이 사용: `Plücker coordinate` (Grassmannian 절에서 사용, 정의 없음)

## [Peterson Variety](/ko/math/lie_theory/peterson_variety)

이 글은 regular nilpotent element가 결정하는 flag variety의 특수한 부분다양체인 Peterson variety를 다룬다. 출발점은 regular nilpotent element의 정의(정의 1)인데, centralizer의 차원이 $$\operatorname{rank}(\mathfrak{g}$$와 같은 nilpotent element라는 조건이고, 각 simple root $$\alpha_i$$에서 nonzero $$e_i\in\mathfrak{g}_{\alpha_i}$$를 골라 $$e=\sum_i e_i$$로 만들면 regular nilpotent이 된다는 것이 구체적이다. 근계 글에서 root space decomposition $$\mathfrak{g}=\mathfrak{h}\oplus\bigoplus_\alpha\mathfrak{g}_\alpha$$를 다뤘으므로 각 $$\mathfrak{g}_{\alpha_i}$$에서 원소를 꺼내 합하는 구성은 자연스럽고, 모든 regular nilpotent이 $$G$$의 adjoint action 아래 서로 conjugate하다는 Kostant의 정리가 이 원소의 유일성을 보장한다는 것이 핵심이다.

Peterson variety의 정의(정의 2)가 이 글에서 가장 중요한 전환점이다. $$Y_P^\circ=\{gB_-\in G/B_- \mid \operatorname{Ad}^\ast(g^{-1})\cdot F\in[\mathfrak{n}_-,\mathfrak{n}_-]^\perp\}$$라는 공식에서 $$F=e_1^\ast+\cdots+e_{n-1}^\ast$$가 dualized positive Chevalley generator의 합이고, $$\operatorname{Ad}^\ast$$가 coadjoint action이라는 것인데, 정의 자체는 간결하지만 사용된 개념들 — coadjoint action, Chevalley generator, derived subalgebra의 annihilator — 이 이전 글에서 정의된 적이 없어서 이 부분은 용어의 의미를 외부 지식에 의존하고 있다. $$P=B$$일 때가 Kostant-Peterson의 원래 정의이고 일반 $$P$$에 대한 형태는 Rietsch의 후속 연구에서 표준적이라는 언급이 역사적 맥락을 제공한다.

명제 3의 차원 결과 — $$\dim Y_B^\circ=\operatorname{rank}(\mathfrak{g})$$ — 가 이 글의 구조적 핵심이다. Kostant의 정리에 의해 regular nilpotent $$F$$의 coadjoint stabilizer가 abelian이고 차원이 rank라는 것에서 출발하여, $$G/B_-$$ 위의 조건이 codimension $$\dim[\mathfrak{n}_-,\mathfrak{n}_-]$$의 affine subspace를 자른다는 dimension count로 결론이 나온다. 다만 증명의 핵심인 dimension count가 "[Pet], [Rie]를 참조"로 생략되어 있어서, 정확히 어떤 차원 계산이 이루어지는지 직접 확인하지 못했다. Rank가 simple root의 개수와 같다는 사실과 잘 맞는다는 관찰은 인상적이지만, "차원이 rank"라는 결론이 왜 자연스러운지에 대한 직적적 설명이 부족하다.

Hessenberg variety로서의 기술(정의 4)이 이 글의 두 번째 관점이다. $$\mathfrak{b}$$를 포함하는 ad-stable subspace $$H$$에 대해 $$\mathcal{B}(X,H)=\{gB\in G/B \mid \operatorname{Ad}(g^{-1})X\in H\}$$로 정의되는 Hessenberg variety의 특수한 경우가 Peterson variety라는 것인데, $$X$$가 regular nilpotent이고 $$H=\mathfrak{b}\oplus\bigoplus_i\mathbb{C}f_i$$일 때가 Peterson variety의 affine chart에 해당한다는 것이 핵심이다. Hessenberg variety 자체가 이 글에서 처음 정의되므로 "더 일반적인 부분다양체 집합의 특수한 예시"라는 설명은 적절하지만, $$H$$의 구체적 조건 — simple negative root vector들을 추가하는 것 — 이 왜 Peterson variety를 복원하는지에 대한 직관적 설명이 부족하다. Insko-Tymoczko의 후속 연구에서 활용된다는 언급이 있지만, 어떤 맥락에서 활용되는지는 알 수 없다.

Stratification 부분이 이 글의 마지막 축이다. $$Y_P^\circ=\bigsqcup_{w\in W^P}Y_{P,w}^\ast$$로 분해되고 각 stratum이 $$Y_P^\circ\cap(BwB_-)/B_-$$로 정의된다는 것은, bruhat_decomposition 글의 Bruhat cell과 Peterson variety의 교집합으로 stratum을 구성하는 것이어서 자연스럽다. Open stratum $$Y_{P,e}^\ast$$가 Big Bruhat cell과의 교집합으로 주어진다는 것도 flag variety의 cell decomposition과 직접 연결된다. $$T$$-fixed point set이 $$W^P$$와 일대일대응된다는 관찰이 인상적인데, torus의 고정점이 Weyl group 원소로 색인된다는 것이 torus_action 글의 $$T$$-fixed point와 구조적으로 같다는 것을 시사한다.

솔직한 반응: Regular nilpotent element의 구성 — 각 simple root space에서 하나씩 꺼내 합하는 것 — 은 근계 글의 root space decomposition을 직접 사용하므로 자연스럽게 따라갈 수 있었다. 특히 $$e=\sum_i e_i$$가 정확히 $$\operatorname{rank}(\mathfrak{g})$$차원의 centralizer를 갖는다는 것이 놀라운데, $$\mathfrak{h}$$의 원소들이 $$e$$와 commute하지 않는 방향으로만 centralizer가 줄어든다는 것이 Kostant 정리의 핵심이라는 예감이 든다. 반면에 coadjoint action이 무엇인지 정의 없이 지나가는 것이 이 글의 가장 큰 한계다. $$\operatorname{Ad}^\ast(g)$$가 $$\mathfrak{g}^\ast$$ 위에서 어떻게 작용하는지, $$[\mathfrak{n}_-,\mathfrak{n}_-]^\perp$$가 구체적으로 어떤 부분공간인지 등을 확인하지 못하면 Peterson variety의 정의 자체를 정확히 이해하기 어렵다. $$G/B_-$$와 $$G/B$$의 차이도 명확하지 않은데, borel_subgroup 글에서는 flag variety를 $$G/B$$로 정의했고 여기서는 $$G/B_-$$를 쓰고 있으므로 두 정의 사이의 관계를 확인해야 한다. Chevalley generator도 마찬가지인데, $$\mathfrak{g}_{\alpha_i}$$의 nonzero 원소를 하나씩 고르는 것과 Chevalley generator의 관계가 무엇인지 명시되어 있지 않다. 전체적으로 이 글은 nilpotent cone과 flag variety의 교차점에 있는 Peterson variety를 소개하는 글로서, 이후 Kazhdan-Lusztig polynomial에서 Bruhat order와의 연결이 더 깊어질 것이라는 예감이 든다.

⚠️ 정의 없이 사용: `coadjoint action` (정의 2에서 $$\operatorname{Ad}^\ast$$로 사용, $$G$$의 $$\mathfrak{g}^\ast$$ 위의 작용인데 이전 글에서 정의된 적 없음)
⚠️ 정의 없이 사용: `Chevalley generator` (정의 2에서 "dualized positive Chevalley generator"로 사용, 정의 없음)
⚠️ 정의 없이 사용: `nilpotent cone` (서론에서 사용, $$\mathfrak{g}$$의 모든 nilpotent element들의 집합이라는 의미이나 정의 없음)
⚠️ 정의 없이 사용: `Springer fiber` (서론에서 언급, 정의 없음)

## [Kazhdan-Lusztig polynomial](/ko/math/lie_theory/kazhdan_lusztig)

이 글은 Hecke algebra 위에서 정의되는 Kazhdan-Lusztig polynomial을 다루며, Bruhat decomposition과 parabolic subgroup 글에서 구축한 조합적 구조 위에 순수하게 조합적인 정의를 내린 뒤 이것이 Schubert variety의 intersection cohomology를 인코딩한다는 기하학적 결과를 statement 수준에서 정리한다. 출발점은 Iwahori-Hecke algebra $$H_q(W)$$의 정의인데, group algebra $$\mathbb{Z}[W]$$의 $$q$$-deformation으로서 generator $$T_s$$가 quadratic relation $$T_s^2=(q-1)T_s+q$$를 만족한다는 것이 정의 1의 내용이다. $$q=1$$일 때 $$T_s^2=1$$로 환원되어 group algebra가 된다는 관찰이 좋은데, "1-parameter deformation"이라는 관점이 이후 KL basis의 bar invariance 조건에서 핵심적으로 사용된다는 것이 이 글의 구조적 출발점이다.

Bar involution $$\overline{\,\cdot\,}:H\to H$$가 $$\overline{q^{1/2}}=q^{-1/2}$$, $$\overline{T_s}=T_s^{-1}$$로 정의되는 것이 정의 3인데, $$T_s^{-1}=q^{-1}T_s+(q^{-1}-1)$$라는 공식으로부터 bar involution이 well-defined임을 확인하는 계산이 깔끔하다. $$T_s^{-1}$$이 동일한 quadratic relation을 $$q$$를 $$q^{-1}$$로 치환한 버전으로 만족한다는 것이 핵심인데, 이 검증이 직접 전개되어 있어서 따라갈 수 있었다. Bar involution의 역할은 KL basis의 self-duality 조건 $$\overline{C_w}=C_w$$를 통해 드러나는데, $$q$$와 $$q^{-1}$$ 사이의 대칭성을 $$C_w$$에 부여하는 것이 이 involution의 존재 이유라는 직관이 잡힌다.

정리 4가 이 글의 핵심 정리다. 각 $$w\in W$$에 대해 bar-invariant하면서 triangularity 조건 $$C_w=q^{-\ell(w)/2}\sum_{v\leq w}P_{v,w}(q)T_v$$를 만족하는 유일한 원소 $$C_w$$가 존재한다는 것인데, $$P_{w,w}=1$$이고 $$\deg P_{v,w}\leq\frac{1}{2}(\ell(w)-\ell(v)-1)$$라는 degree bound가 추가 조건이다. 증명이 $$\ell(w)$$에 대한 induction으로 전개되는 것이 인상적인데, 기저 $$C_e=1$$에서 출발하여 $$C_s=q^{-1/2}(T_s-q)$$를 정규화 generator로 도입하고, $$C_s\cdot C_{sw}$$의 산물에서 degree bound를 위반하는 보정 항 $$\sum_{z<w,\,sz<z}\mu(z,sw)C_z$$를 빼서 $$C_w$$를 구성하는 방식이 깔끔하다. 유일성 증명에서 bar-invariance가 계수를 $$q^{1/2}$$의 양의 거듭제곱과 음의 거듭제곱 모두로 표현되도록 강제한다는 논증이 특히 우아한데, 이로부터 계수가 $$0$$이 되어 유일성이 follows한다는 것이 이 증명의 핵심 아이디어다.

R-polynomial의 도입이 KL polynomial과 짝을 이루는 두 번째 축이다. $$\overline{T_{w^{-1}}^{-1}}=q^{-\ell(w)}\sum_{v\leq w}R_{v,w}(q)T_v$$로 정의되는 $$R_{v,w}(q)$$는 bar involution이 standard basis 위에서 어떻게 작용하는지를 기술하는데, recursion 공식 $$R_{v,w}(q)=R_{sv,sw}(q)$$ (if $$sv<v$$) 또는 $$(q-1)R_{v,sw}(q)+qR_{sv,sw}(q)$$ (if $$sv>v$$)로 효율적으로 계산된다. Inversion formula $$q^{\ell(w)-\ell(v)}\overline{P_{v,w}(q)}-P_{v,w}(q)=\sum_{v<z\leq w}(-1)^{\ell(z)-\ell(v)}R_{v,z}(q)P_{z,w}(q)$$가 KL polynomial과 R-polynomial을 서로 결정한다는 것이 명제 7의 내용인데, 증명의 개략에서 $$\overline{C_w}=C_w$$를 standard basis 표현에 대입하고 계수를 비교하는 방식이 제시되어 있지만 전체 계산은 [BB, Theorem 5.1.4]를 참조하라고만 되어 있어서 inversion formula의 구체적 유도를 직접 확인하지 못했다.

정리 8이 이 글에서 가장 깊은 결과다. Schubert variety $$X_w\subseteq G/B$$의 intersection cohomology sheaf $$\operatorname{IC}_{X_w}$$의 stalk cohomology의 Poincaré 다항식이 KL polynomial로 주어진다는 것 — $$\sum_{i\geq 0}\dim\mathcal{H}^i(\operatorname{IC}_{X_w})_{vB/B}\cdot q^{i/2}=P_{v,w}(q)$$ — 인데, 이 "Kazhdan-Lusztig 추측"이 Beilinson-Bernstein과 Brylinski-Kashiwara에 의해 독립적으로 증명되었다는 것이 언급된다. 증명의 개략이 세 단계로 요약되어 있는데, Beilinson-Bernstein localization으로 flag variety 위의 $$D$$-module category와 category $$\mathcal{O}$$의 동치를 보이고, Riemann-Hilbert correspondence로 $$D$$-module과 perverse sheaf를 연결하고, KL basis $$C_w$$가 $$[\operatorname{IC}_{X_w}]$$의 Grothendieck class로 실현됨을 보이는 구조가 큰 그림으로는 이해할 수 있었다. 다만 이 세 단계 각각이 상당히 깊은 결과를 전제로 하기 때문에, 이 글만으로는 증명의 구체적 내용을 파악할 수 없었다.

$$S_3$$과 $$S_4$$의 예시가 감을 잡기 좋다. $$S_3$$의 경우 모든 $$P_{v,w}(q)=1$$이므로 $$GL_3/B$$의 모든 Schubert variety가 매끄럽다는 결론이 나오고, $$S_4$$에서 처음으로 $$P_{e,3412}(q)=1+q$$라는 비자명한 polynomial이 등장한다는 것이 예시 11의 내용이다. $$3412$$와 $$4231$$이라는 두 permutation이 type $$A_3$$에서 매끄러움이 깨지는 유일한 reduced situation이라는 것이 Lakshmibai-Sandhya의 pattern avoidance 정리와 직접 연결된다는 관찰이 인상적이다. KL positivity conjecture가 Elias-Williamson의 Soergel bimodule 이론으로 일반적으로 증명되었다는 언급도 좋은데, finite type을 벗어난 경우까지 확장되는 이 결과의 깊이를 이 글만으로는 따라갈 수 없다.

솔직한 반응: Hecke algebra와 bar involution까지의 전개는 논리적으로 깔끔해서 따라갈 수 있었다. 특히 bar-invariant 원소의 존재성과 유일성을 induction으로 보이는 증명이 — 보정 항 $$\mu(z,sw)$$를 명시적으로 구성하는 방식 — 이 글에서 가장 우아한 부분이다. 반면에 정리 8의 기하학적 해석은 이 글의 가장 큰 한계다. Intersection cohomology sheaf가 무엇인지, $$D$$-module이 무엇인지, Riemann-Hilbert correspondence가 무엇인지 등의 배경 지식이 없으면 "KL polynomial이 Schubert variety의 특이점을 인코딩한다"는 statement를 받아들일 수밖에 없고, 그 의미를 실제로 이해하기 어렵다. Inversion formula의 전체 유도도 생략되어 있어서 $$P_{v,w}$$와 $$R_{v,w}$$ 사이의 관계를 직접 확인하지 못했다. 전체적으로 이 글은 조합적 정의(Hecke algebra, KL basis)와 기하학적 해석(IC sheaf)을 statement 수준에서 연결하는 다리 역할을 하며, 리 이론 카테고리의 마지막 글로서 Bruhat decomposition, Schubert variety 등 이전 글들의 조합적/기하적 구조가 집약된 결과를 보여준다.

⚠️ 정의 없이 사용: `intersection cohomology` (정리 8에서 사용, 대수적 위상수학/호몰로지 대수학 카테고리에서 정의된 적 없음)
⚠️ 정의 없이 사용: `perverse sheaf` (정리 8에서 사용, 정의 없음)
⚠️ 정의 없이 사용: `D-module` (증명 개략에서 사용, 정의 없음)
⚠️ 정의 없이 사용: `Riemann-Hilbert correspondence` (증명 개략에서 사용, 정의 없음)
⚠️ 정의 없이 사용: `Grothendieck group` (증명 개략에서 사용, 대수적 구조 카테고리에서 정의될 수 있으나 이 노트에서 미확인)
⚠️ 정의 없이 사용: `category $$\mathcal{O}$$` (증명 개략에서 사용, 정의 없음)
⚠️ 정의 없이 사용: `Soergel bimodule` (KL positivity conjecture 증명에서 언급, 정의 없음)

## 카테고리 회고

리 이론 카테고리는 Lie group의 정의에서 출발하여 Lie algebra, 원환면의 작용, 근계, Borel subgroup, Bruhat decomposition, Richardson variety, Peterson variety, Kazhdan-Lusztig polynomial까지 일관된 흐름으로 전개되었다. 큰 그림은 "Lie group의 대칭을 infinitesimal 구조(Lie algebra)로 환원하고, 그 조합적/기하적 구조(root system, Weyl group)를 이용해 flag variety 위의 세포 분해를 구성한 뒤, 그 위에 정의되는 특수한 부분다양체(Richardson, Peterson)와 조합적 불변량(KL polynomial)을 연구한다"는 것이다. 가장 막혔던 부분은 intersection cohomology, $$D$$-module, Riemann-Hilbert correspondence 등 homological algebra와 대수적 위상수학의 깊은 결과를 전제로 하는 Kazhdan-Lusztig polynomial의 기하학적 해석이었는데, 이 배경 지식 없이는 "KL polynomial이 Schubert variety의 특이점을 인코딩한다"는 statement의 의미를 완전히 파악하기 어려웠다.
