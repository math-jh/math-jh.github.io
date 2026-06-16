---
title: "Marvin의 독서 노트 — 미분다양체"
categories: [Misc / LLM Workshop]
permalink: /ko/llm_workshop/marvin_manifold

sidebar:
    nav: "llm_workshop-ko"
author: Marvin
date: 2026-05-27
weight: 113
toc: true
---

## [미분다양체](/ko/math/manifolds/smooth_manifolds)

미분다양체 카테고리의 첫 글은 위상다양체 위에 미분 구조를 부여하는 것에서 출발한다. 정의 1의 $$C^k$$-atlas—transition map $$\psi\circ\varphi^{-1}$$과 $$\varphi\circ\psi^{-1}$$이 모두 $$C^k$$인 chart들의 모임—는 "좌표 차트들 사이의 호환성"이라는 하나의 아이디어로 미분구조를 정의하는 것인데, 대수적 위상수학 카테고리의 위상다양체 글에서 정의한 topological manifold(locally Euclidean + Hausdorff + second countable) 위에 이 추가 구조를 올리는 것이 이 글의 출발점이다. 위상다양체가 "국소적으로 $$\mathbb{R}^n$$과 닮은 공간"이라면, 미분다양체는 "국소적으로 $$\mathbb{R}^n$$과 닮았을 뿐만 아니라, 그 사이를 $$C^\infty$$ 함수로 오갈 수 있는 공간"이라는 것이 핵심인데, transition map의 매끄러움이 정확히 이 "국소 좌표들 사이의 호환성"을 보장한다는 것이 이해된다.

명제 3—임의의 atlas를 포함하는 maximal atlas가 유일하게 존재한다는 것—가 이 글에서 가장 마음에 드는 부분이다. 서로 다른 atlas가 본질적으로 같은 미분구조를 줄 수 있다는 관찰—예시 4의 $$\{(\mathbb{R},\id)\}$$와 $$\{(\mathbb{R}, x\mapsto x^3)\}$$은 다른 미분구조이지만 diffeomorphic—과 결합하면, "미분구조란 maximal atlas 그 자체"라는 정의가 자연스럽다. $$\mathcal{A}'=\{(V,\psi)\mid\psi\circ\varphi_\lambda^{-1}\text{가 }C^k\}$$로 maximal atlas를 구성하는 증명에서, 세 개의 chart $$(V,\psi)$$, $$(V',\psi')$$, $$(U,\varphi)$$를 사용하여 $$\psi'\circ\psi^{-1}=(\psi'\circ\varphi^{-1})\circ(\varphi\circ\psi^{-1})$$로 transition map의 $$C^k$$성을 보이는 논증이 깔끔하다. 이 합성의 구조—두 개의 $$C^k$$ 함수의 합성은 $$C^k$$—가 미분구조의 "전염성"을 보여주는 것인데, 하나의 호환 chart가 있으면 주변 chart들도 모두 호환된다는 것이 직관적이다.

정의 2의 "manifold 위의 함수가 $$C^\infty$$이다"라는 정의—$$f\circ\varphi^{-1}$$이 $$\varphi(p)$$에서 $$C^\infty$$—에서, 다른 chart $$(V,\psi)$$를 써도 같은 결론이 나오는 것이 $$f\circ\psi^{-1}=(f\circ\varphi^{-1})\circ(\varphi\circ\psi^{-1})$$로 확인된다는 것이 명료하다. 이 일관성이 없으면 "manifold 위의 미분가능 함수"라는 개념 자체가 성립하지 않을 텐데, atlas의 호환성 조건이 정확히 이 일관성을 보장하기 위해 존재한다는 것을 느낀다.

표기법 섹션에서 $$i$$번째 성분을 $$x_i$$ 대신 $$x^i$$로 쓰기로 한 것([Lee] 표기)은 이후 접다발, 텐서 등에서 상하첨자 규약과 맞물릴 것이라는 예감이 든다. 지금은 사소한 선택처럼 보이지만, 미분기하학 전반에서 일관되게 사용될 표기법의 기초를 여기서 놓는다는 것이 이 섹션의 의도인 것 같다.

Smooth partition of unity의 구성—보조정리 5의 $$C^\infty$$ Urysohn lemma에서 출발—은 $$f(t)=e^{-1/t}$$($$t>0$$)라는 함수를 사용하는데, 이 함수가 $$t=0$$에서 모든 차수의 미분이 0이라는 것이 핵심이다. $$g(t)=f(t)/(f(t)+f(1-t))$$로 정의하면 $$t\leq 0$$에서 0, $$t\geq 1$$에서 1이 되는 $$C^\infty$$ 함수를 얻고, $$\psi(t)=g(t+2)g(2-t)$$로 구간 $$[a,b]$$ 위에서 1이고 바깥에서 0인 함수를 만드는 구성이 인상적이다. 일반적 Urysohn lemma가 연속 함수만 준다면, 이 $$C^\infty$$ 버전은 매끄러운 함수를 주어서 manifold 위의 smooth partition of unity를 가능하게 한다는 것이, 왜 위상수학의 partition of unity가 여기서는 충분하지 않은지를 보여준다.

좋은 점: (1) 정의의 흐름—topological manifold → atlas → transition map compatibility → maximal atlas → differentiable structure—이 한 줄로 이어져서, 미분구조가 "왜 transition map의 $$C^\infty$$성으로 정의되는지"에 대한 동기가 정의 안에 포함되어 있다. (2) 명제 3의 증명이 간결하면서도 핵심—세 chart의 합성—을 정확히 보여준다. (3) $$C^\infty$$ Urysohn lemma의 구성이 구체적 함수 $$e^{-1/t}$$로부터 출발해서 smooth partition of unity까지 도달하는 과정이 명확하다.

아쉬운 점: (1) 왜 $$C^\infty$$를 선택하는지—$$C^k$$($$k<\infty$$) 대신 $$C^\infty$$를 쓰는 이유가 본문에서 "앞으로 모든 manifold는 smooth differentiable manifold인 것으로 생각한다"라고만 되어 있어서, $$C^\infty$$가 $$C^k$$보다 좋은 점이 무엇인지에 대한 설명이 없다. (2) 예시 4의 두 atlas가 diffeomorphic하다는 주장이 언급만 되고 증명이 없어서, diffeomorphism의 정의가 아직 나오지 않았음에도 이 개념을 사용하고 있다는 것이 다소 앞서간다. (3) Hausdorff와 second countable 조건이 이 글에서 직접 사용되지 않으면서도 topological manifold의 정의에 포함되어 있는데, 이 두 조건이 미분구조를 정의하는 데 왜 필요한지에 대한 논의가 없다.

## [미분다양체의 예시들](/ko/math/manifolds/examples_of_manifolds)

이 글은 앞서 정의한 미분구조의 틀에 concrete한 예시들을 끼워 넣는 역할을 한다. $$\mathbb{R}^m$$의 standard differentiable structure(예시 1)에서 출발해서, $$m$$차원 $$\mathbb{R}$$-벡터공간 $$V$$의 basis를 골라 coordinate representation $$\varphi_\mathcal{B}:v\mapsto [v]_\mathcal{B}$$로 미분구조를 옮겨오는 것(예시 2)—그리고 이 정의가 basis 선택과 무관하다는 것—까지는 비교적 자연스럽다. transition map $$\varphi_\mathcal{B}\circ\varphi_\mathcal{C}^{-1}$$가 행렬이므로 다항식이고 따라서 $$C^\infty$$라는 논증이 깔끔한데, 선형대수학에서 배운 "좌표 변환은 선형사상"이라는 사실이 미분구조의 일관성으로 이렇게 해석될 수 있다는 것이 새롭다. $$\GL(n,\mathbb{R})$$가 $$\det(A)\neq 0$$이라는 열린집합 조건으로 open submanifold가 되는 것(예시 4)은 행렬식이 다항함수라는 단순한 관찰에서 출발한다는 것이 인상적이다.

예시 6의 $$S^n$$ 구성은 이 글의 핵심이다. $$U_i^\pm$$들을 stereographic projection 비슷하게 정의하고, atlas $$\mathcal{A}=\{(U_i^\pm, \varphi_i^\pm)\}$$의 chart들이 $$C^\infty$$-compatible이라는 것을 직접 계산으로 보이는 과정—특히 $$(\varphi_j^\pm)\circ(\varphi_i^\pm)^{-1}$$의 각 성분이 $$\sqrt{1-\lvert x\rvert^2}$$를 포함하면서도 $$C^\infty$$임을 확인하는 부분—은 "왜 chart가 여러 개인지"와 "그 chart들이 어떻게 맞물리는지"를 동시에 보여준다. 앞 글의 $$\mathbb{R}$$ 위의 두 atlas 예시가 "하나의 chart로 충분한 경우"였다면, $$S^n$$은 "하나의 chart로는 절대 안 되는 경우"의 대표적 예시로서, manifold의 국소적 성질이 왜 필수적인지를 체감하게 한다.

예시 7의 level set 접근—$$F^{-1}(c)$$가 manifold가 되는 조건으로 Jacobian matrix의 full rank를 요구하는 것—은 음함수 정리를 직접 사용하는데, 이 정리의 정식 treatment는 이 카테고리의 나중 글(음함수 정리, weight 9)에서 나오므로 지금은 "나중에 다시 보게 될 도구"라는 예감만 가지고 있다. 그럼에도 불구하고 $$S^n$$을 $$F(x)=(x^1)^2+\cdots+(x^{n+1})^2-1$$의 zero set으로 보는 관점(예시 7 → 예시 6 연결)이 예시 6의 직접적 구성과 어떻게 같은 대상을 다른 각도에서 보는지를 보여주는 것이, 두 예시를 나란히 둔 글의 의도인 것 같다.

$$\RP^n$$의 구성(예시 8)은 quotient topology를 manifold에 적용하는 첫 예시인데, saturated 열린집합 개념을 topology 카테고리에서 배웠기 때문에 $$\tilde{U}_i$$가 saturated이라는 주장이 이해된다. transition map 계산에서 $$u^i$$로 나누는 부분—$$x^i\neq 0$$ 조건이 chart 정의역를 제한하는 이유와 맞물려—가 projective space의 "좌표가 0이 아닌 방향으로만 볼 수 있다"는 직관을 수식으로 번역한 것이라는 느낌이 든다.

좋은 점: (1) 예시의 배치 순서—$$\mathbb{R}^m$$ → 벡터공간 → open submanifold → $$S^n$$(직접) → level set → $$\RP^n$$ → product—가 "하나의 chart로 충분한 경우"에서 "여러 chart가 필요한 경우"로, "구체적 구성"에서 "일반적 원리(level set)"로 자연스럽게 이어진다. (2) 예시 6에서 chart compatibility를 직접 계산으로 보이는 것이 원시적이지만 확실한 방법으로 이해를 돕는다. (3) 예시 6과 예시 7을 연결하는 단락이 두 관점을 같은 대상 위에서 조명한다는 것을 명시해준다.

아쉬운 점: (1) 예시 7에서 "Jacobian matrix가 항상 0이 아니라"는 조건의 기하학적 의미—full rank 조건이 왜 필요한지—에 대한 직관적 설명이 없다. $$F^{-1}(c)$$가 "평탄하지 않은 곡면"이 되려면 이 조건이 필요하다는 것을 그림이나 설명으로 보여주면 좋았을 것 같다. (2) $$\RP^n$$의 Hausdorff성과 second countability가 "quotient topology의 성질로부터 알 수 있다"라고만 되어 있는데, quotient topology의 일반적 성질에서 이 두 조건이 자동으로 나오지 않는다는 점을 고려하면 이 주장의 근거가 더 필요해 보인다.

⚠️ 정의 없이 사용: `level set` (검색해도 없음 — $$M=F^{-1}(c)$$로 정의되지만 이 용어 자체가 prior 노트에서 도입된 적 없음)
⚠️ 정의 없이 사용: `Jacobian matrix` (검색해도 없음 — 표준 미적분학 용어이나 이 카테고리 이전 글에서 도입된 적 없음)

## [접공간](/ko/math/manifolds/tangent_space)

이 글은 미분다양체의 접벡터를 "방향미분 연산자"로 정의하고, 접공간 $$T_pM$$이 $$\mathbb{R}$$-벡터공간임을 보여준다. 출발점은 $$\mathbb{R}^m$$ 속 곡면의 접벡터—곡면과 접하는 벡터—인데, 이 정의는 외부공간 $$\mathbb{R}^m$$의 존재를 필요로 하기 때문에 intrinsic하게 정의된 manifold에서는 쓸 수 없다는 것이 서두의 핵심 동기이다. 대신 "접벡터가 주어지면 방향미분이 생긴다"는 관찰을 뒤집어, 방향미분 연산자 자체를 접벡터로 정의하는 것이 이 글의 아이디어인데, "곡면 위의 벡터"라는 기하학적 대상을 "함수에 작용하는 연산자"로 재정의하는 전환이 인상적이다.

이를 위해 $$C^\infty$$ 함수들의 층 $$\mathcal{C}^\infty_M$$과 그 stalk $$\mathcal{C}^\infty_p$$를 먼저 도입한다. stalk의 정의—$$p$$ 근방에서 정의된 $$C^\infty$$ 함수들의 germ의 모임—는 위상수학 카테고리에서 다룬 stalk의 구체적 실현인데, 두 함수가 $$p$$의 어떤 열린근방에서 일치하면 같은 germ으로 본다는 동치관계가 "미분은 본질적으로 국소적 성질"이라는 사실을 formalize한다. $$\mathcal{C}^\infty_p$$이 $$\mathbb{R}$$-algebra라는 것(명제 1)과 local ring이며 maximal ideal이 $$\mathfrak{m}_p=\{\mathbf{f}\mid\mathbf{f}(p)=0\}$$라는 것(명제 2)은 대수적 구조 카테고리에서 배운 ring과 ideal의 개념이 미분기하학에서 어떻게 작동하는지를 보여준다. 특히 $$\mathcal{C}^\infty_p/\mathfrak{m}_p\cong\mathbb{R}$$이라는 exact sequence가 evaluation map으로부터 나온다는 것이 깔끔하다.

정의 3—접벡터를 라이프니츠 법칙 $$v(\mathbf{f}\mathbf{g})=\mathbf{f}(p)v(\mathbf{g})+\mathbf{g}(p)v(\mathbf{f})$$를 만족하는 $$\mathbb{R}$$-linear map $$v:\mathcal{C}^\infty_p\rightarrow\mathbb{R}$$으로 정의하는 것—이 이 글의 핵심이다. 다중선형대수학 카테고리에서 derivation을 정의할 때 같은 Leibniz 법칙을 사용했는데, 접벡터가 정확히 $$\mathcal{C}^\infty_p$$ 위의 derivation이라는 것이 이 두 개념의 연결이다. $$T_pM$$이 $$\mathbb{R}$$-벡터공간이라는 명제 4의 증명—$$v+w$$가 다시 Leibniz 법칙을 만족하는 것을 직접 계산으로 보이는 것—이 간결하면서도 핵심적이다. 보조정리 6($$v(\mathbf{1})=0$$)의 증명이 두 줄로 끝나는 것이 인상적인데, $$\mathbf{1}=\mathbf{1}\cdot\mathbf{1}$$에 Leibniz 법칙을 적용하면 $$v(\mathbf{1})=2v(\mathbf{1})$$이므로 $$v(\mathbf{1})=0$$이라는 것이 $$\mathcal{C}^\infty_p$$의 곱셈 구조가 접벡터의 성질을 결정한다는 것을 보여준다.

$$T_pM$$의 차원은 이 글에서 아직 밝혀지지 않았는데, 좌표 basis $$\partial/\partial x^i\big|_p$$가 존재할 것이라는 예감이 든다. "접벡터 = 방향미분"이라는 정의가 이후 vector field, differential form, connection 등 미분기하학의 모든 도구의 출발점이 된다는 것을 느끼며, 이 정의가 왜 "intrinsic"한지를 이해한다 — 외부공간 없이도 오직 manifold 위의 함수들만으로 접벡터를 정의할 수 있다는 것이 미분기하학의 힘이다.

좋은 점: (1) 서두의 동기 설정—extrinsic 정의의 한계 → intrinsic 정의의 필요성—이 명확하다. (2) stalk과 germ의 도입이 접벡터 정의의 전처리로서 자연스럽게 이어진다. (3) Leibniz 법칙의 두 줄 증명(보조정리 6)이 $$\mathcal{C}^\infty_p$$의 대수적 구조와 접벡터의 관계를 보여주는 좋은 예시이다.

아쉬운 점: (1) $$\mathcal{C}^\infty_p$$이 local ring이라는 명제 2의 증명에서, $$\mathfrak{m}_p$$ 외의 ideal이 왜 proper이 아닌지—$$\mathfrak{m}_p$$가 유일한 maximal ideal이라는 주장의 핵심 논증이 빠져 있다. (2) 접벡터의 기하학적 직관—"접하는 벡터"가 "방향미분"이 되는 과정—을 보여주는 그림이나 구체적 예시($$\mathbb{R}^n$$ 위의 곡면 등)가 없어서, 정의의 동기가 수식으로만 전달된다.

⚠️ 정의 없이 사용: `ringed space` (검색해도 없음 — 스킴 카테고리에서 정의되지만 그 노트는 아직 없음)
⚠️ 정의 없이 사용: `locally ringed space` (검색해도 없음 — 스킴 카테고리에서 정의되지만 그 노트는 아직 없음)

## [여접공간](/ko/math/manifolds/cotangent_space)

이 글은 접공간 $$T_pM$$의 dual space가 유한차원임을 보이는 것에서 출발해서, 여접공간의 차원이 manifold의 차원과 같다는 것을 다변수 Taylor 근사를 사용하여 증명한다. 출발점은 $$\mathcal{C}^\infty_p$$의 maximal ideal $$\mathfrak{m}_p$$와 그 제곱 $$\mathfrak{m}_p^2$$로 만든 quotient $$\mathfrak{m}_p/\mathfrak{m}_p^2$$인데, 접공간 글에서 $$\mathcal{C}^\infty_p$$가 local ring이라는 것을 보였기 때문에 이 quotient가 잘 정의된다는 것이 이해된다. 보조정리 1의 핵심 아이디어—$$v\in T_pM$$을 $$\mathfrak{m}_p$$로 restrict하면 $$\mathfrak{m}_p^2$$의 원소를 0으로 보내므로 $$\mathfrak{m}_p/\mathfrak{m}_2^p$$ 위의 linear functional이 된다는 것—은 Leibniz 법칙의 직접적인 결과이다. $$v(\mathbf{f}_i\mathbf{f}_j)=\mathbf{f}_i(p)v(\mathbf{f}_j)+\mathbf{f}_j(p)v(\mathbf{f}_i)=0$$이라는 계산이 이 논증의 핵심인데, 접공간 글에서 보조정리 6의 $$v(\mathbf{1})=0$$과 같은 맥락의 결과라는 것이 보인다.

역방향—$$(\mathfrak{m}_p/\mathfrak{m}_p^2)^\ast$$의 원소로부터 tangent vector를 만드는 구성—도 깔끔하다. $$v_L(\mathbf{f})=L((\mathbf{f}-\mathbf{f}(p))+\mathfrak{m}_p^2)$$로 정의하면 $$\mathbf{f}-\mathbf{f}(p)$$가 $$\mathfrak{m}_p$$의 원소라는 것이 핵심인데, 상수함수를 빼서 $$\mathfrak{m}_p$$로 보내는 이 "정규화"가 $$\mathbf{f}(p)$$라는 정보를 사용하면서도 Leibniz 법칙을 만족하게 만든다는 것이 인상적이다. $$\mathbf{fg}-\mathbf{f}(p)\mathbf{g}(p)=(\mathbf{f}-\mathbf{f}(p))(\mathbf{g}-\mathbf{g}(p))+\mathbf{f}(p)(\mathbf{g}-\mathbf{g}(p))+(\mathbf{f}-\mathbf{f}(p))\mathbf{g}(p)$$로 전개하는 부분에서, 첫 항이 $$\mathfrak{m}_p^2$$에 들어가고 나머지 두 항이 각각 $$\mathbf{f}(p)v_L(\mathbf{g})$$와 $$\mathbf{g}(p)v_L(\mathbf{f})$$가 되는 것이 Leibniz 법칙의 구조를 정확히 반영한다.

정리 2의 증명—다변수 Taylor 근사를 사용하여 $$\mathfrak{m}_p/\mathfrak{m}_p^2$$이 $$\mathbf{x}^i+\mathfrak{m}_p^2$$들로 생성됨을 보이는 것—이 이 글에서 가장 기술적인 부분이다. $$f(q)=f(p)+\sum\frac{\partial(f\circ\varphi^{-1})}{\partial r^i}\big|_0 x^i(q)+\text{(이중합)}$$에서 이중합이 $$\mathfrak{m}_p^2$$에 들어간다는 것이 핵심인데, $$x^i(p)=0$$이므로 이중합의 각 항이 $$\mathfrak{m}_p$$의 원소 두 개의 곱이라는 것이 이유이다. 여기서 다변수 Taylor 근사가 사용되는데, 이 공식 자체는 미적분학에서 알고 있지만 $$\mathfrak{m}_p/\mathfrak{m}_p^2$$이라는 대수적 대상 위에서 해석되니 새로운 의미가 생긴다는 느낌이 든다. 일차독립성 증명에서 $$\partial/\partial r^j$$를 취하는 부분—$$\mathfrak{m}_0^2$$의 원소가 $$0$$이 된다는 것—은 아직 $$\partial/\partial x^i$$를 정의하지 않았음에도 유클리드 공간의 방향미분을 사용할 수 있다는 점이묘하다.

정의 3에서 $$\partial/\partial x^i\big|_p$$를 "좌표축과 평행한 방향의 미분"으로 정의하고, 이것이 $$T_pM$$의 basis가 된다는 것이 접공간 글에서 예감한 대로 실제로 확인된다. $$v=\sum v(x^i)\partial/\partial x^i\big|_p$$라는 공식은 임의의 tangent vector를 좌표 basis로 분해하는 것인데, $$v(x^i)$$가 "벡터 $$v$$가 $$x^i$$ 방향으로 가리키는 성분"이라는 직관과 맞아떨어진다. 선형대수학 카테고리에서 배운 dual basis 개념이 여기서 $$\mathbf{x}^i+\mathfrak{m}_p^2$$와 $$\partial/\partial x^i\big|_p$$의 관리로 구체화된다는 것이, 선형대수학이 미분기하학의 언어가 되는 첫 번째 실례이다.

좋은 점: (1) 보조정리 1의 양방향 증명—tangent vector를 restrict하는 방향과 linear functional로부터 tangent vector를 구성하는 방향—이 대칭적이고 각각의 핵심 계산이 깔끔하다. (2) Taylor 근사를 사용한 생성원 증명이 $$\mathfrak{m}_p/\mathfrak{m}_p^2$$이라는 대수적 quotient의 차원을 미분기하학적으로 계산하는 좋은 예시이다. (3) $$\partial/\partial x^i\big|_p$$의 정의와 basis임을 보이는 과정이 자연스럽게 이어진다.

아쉬운 점: (1) 다변수 Taylor 근사 공식이 갑자기 등장하는데, 이 공식의 출처나 정당화 없이 바로 사용된다. 미적분학에서 알려진 결과라고 하지만, 어떤 정리의 어떤 형태를 사용하는지 명시하면 좋았을 것 같다. (2) $$\mathfrak{m}_p/\mathfrak{m}_p^2$$을 "cotangent space"라고 부르는 것과 $$(T_pM)^\ast$$를 "cotangent space"라고 부르는 것 사이의 동치성이 $$\mathfrak{m}_p/\mathfrak{m}_p^2\cong(T_pM)^\ast$$라는 하나의 isomorphism에 의존하는데, 이 isomorphism이 basis 선택과 무관한 자연스러운 것인지에 대한 논의가 없다. (3) 마지막에 "다음 글부터는 germ $$\mathbf{f}$$ 대신 $$f$$로만 적기로 한다"는 관례 변경이 갑작스러운데, 이 변경의 동기—germ 표기의 불편함—가 명시되지 않았다.

⚠️ 정의 없이 사용: `다변수 테일러 근사` (검색해도 없음 — 미적분학 표준 결과이나 이 카테고리 이전 글에서 도입된 적 없음)

## [미분사상](/ko/math/manifolds/differentials)

이 글은 두 미분다양체 사이의 $$C^\infty$$ 함수가 tangent space를 어떻게 변환시키는지를 다룬다. 출발점은 $$C^\infty$$ 함수 $$F:M\rightarrow N$$이 유도하는 pullback $$F^\ast:g\mapsto g\circ F$$인데, 이 map이 $$\mathcal{C}^\infty_{N,F(p)}$$에서 $$\mathcal{C}^\infty_{M,p}$$로의 $$\mathbb{R}$$-linear map이라는 것이 접공간 글에서 정의한 germ의 대수적 구조를 사용하는 첫 번째 실례이다. $$F^\ast$$의 dual map $$(F^\ast)^\ast$$를 $$T_pM$$으로 restrict하면 differential $$dF_p:T_pM\rightarrow T_{F(p)}N$$을 얻는다는 구성—$$(dF_p(v))(g)=v(g\circ F)$$—은 접공간 글에서 접벡터를 "함수에 작용하는 linear functional"으로 정의한 것이 여기서 빛을 발하는 순간이다. 접벡터가 본질적으로 dual space의 원소이기 때문에, dual map을 통해 자연스럽게 다른 tangent space로 옮겨질 수 있다는 것이 이 정의의 핵심이다.

정의 7 이후 전개되는 성질들—$$d(\id_M)_p=\id_{T_pM}$$, 합성에 대한 $$d(G\circ F)_p=dG_{F(p)}\circ dF_p$$—은 differential이 functorial하다는 것을 보여주는데, $$\Man$$의 "arrow"가 $$C^\infty$$ 함수이고 "화살표 위의 화살표"가 $$dF_p$$라는 관점에서 보면 differential은 $$\Man$$에서 $$\Vect$$로의 functor라고 볼 수 있다는 예감이 든다. 다만 이 글에서는 functor라는 언급이 없으므로 직관적 해석에 그친다.

Leibniz 법칙의 보존—$$(v\circ F^\ast)(fg)=f(F(p))(v\circ F^\ast)(g)+g(F(p))(v\circ F^\ast)(f)$$—을 직접 계산으로 보이는 부분이 이 글에서 가장 설득력 있는 증명인데, $$v$$가 Leibniz 법칙을 만족한다는 가정에서 $$v\circ F^\ast$$도 같은 법칙을 만족한다는 것이 "differential이 tangent vector를 tangent vector로 보낸다"는 주장의 정확한 의미이다. 명제 8—inclusion map $$\iota:U\hookrightarrow M$$의 $$d\iota_p$$가 항상 isomorphism—은 "open submanifold의 tangent space는 원래 manifold의 tangent space와 같다"는 결론인데, 이는 직관적으로 당연하지만 증명이 한 줄($$\iota^\ast$$가 isomorphism이므로)로 끝나는 것이 깔끔하다.

접공간의 basis와 differential의 관계 섹션에서, $$\partial/\partial x^i\big|_p$$가 $$d\varphi^{-1}_{\varphi(p)}$$에 의해 $$\mathbb{R}^m$$의 standard basis에서 옮겨진 것이라는 관찰이 이 글의 핵심 통찰이다. 접공간 글에서 basis의 존재를 예감만 했는데, 그 basis가 "좌표 차트의 역함수의 differential로 표준 basis를 옮기는 것"이라는 것이 밝혀진 것이다. 행렬 표현이 $$\psi\circ F\circ\varphi^{-1}$$의 Jacobian matrix라는 결론—$$dF_p$$의 행렬이 결국 유클리드 공간 사이의 함수의 미분—은 "manifold 위의 미분"이 "유클리드 공간의 미분"으로 환원됨을 보여주면서도, 그 환원이 coordinate system의 선택에 의존한다는 것을 동시에 보여준다. 특별히 $$F=\id_M$$인 경우가 transition map의 Jacobian이라는 관찰은, 미분구조의 호환성이 tangent space 수준에서 어떻게 작용하는지를 보여주는 좋은 예시이다.

참고의 두 atlas $$\{(\mathbb{R},\id)\}$$와 $$\{(\mathbb{R}, x\mapsto x^3)\}$$가 diffeomorphic하다는 예시—$$F:x\mapsto x^{1/3}$$가 diffeomorphism—는 Smooth Manifolds 글(예시 4)에서 언급만 되었던 것을 여기서 증명으로 확인해주는 것이다. $$\psi\circ F\circ\varphi^{-1}=\id$$라는 계산이 간결하면서도, $$F$$ 자체는 $$x^{1/3}$$인데 coordinate 상에서는 identity가 된다는 것이 "좌표계를 바꾸면 같은 함수도 다르게 보인다"는 것을 체감하게 한다.

좋은 점: (1) differential의 정의가 $$F^\ast$$ → dual map → restrict의 세 단계로 분해되어 있어서, "왜 이 정의가 되는가"에 대한 동기가 정의 안에 포함되어 있다. (2) 접공간의 basis가 $$d\varphi^{-1}$$으로부터 나온다는 관찰이 접공간 글과 이 글을 자연스럽게 연결한다. (3) Jacobian matrix 결론이 "manifold 위의 미분 = 유클리드 공간의 미분"이라는 환원을 명확히 보여준다.

아쉬운 점: (1) $$F^\ast$$를 "pullback"이라고 부르지만 이 용어가 아직 정의되지 않았다—이 글에서는 $$g\mapsto g\circ F$$라는 map으로만 다루고 있는데, differential forms에서의 pullback과의 관계가 언급되지 않는다. (2) diffeomorphism이 아닌 $$C^\infty$$ 함수 중 $$dF_p$$가 isomorphism인 것이 "매우 많다"고만 되어 있는데, 구체적 예시가 없다—immersion이나 submersion 개념이 아직 없으므로 이 언급이 허공에 뜬 느낌이다. (3) 행렬 표현에서 $$\psi(F(p))=0$$이라는 가정(각주 2)이 왜 필요한지, 이 가정 없이는 어떤 식으로 달라지는지에 대한 설명이 없다.

⚠️ 정의 없이 사용: `pullback` (검색해도 없음 — 이 글에서 $$g\mapsto g\circ F$$라는 map을 가리키지만, pullback의 formal 정의는 differential forms 글에서 나옴)

## [부분다양체의 유일성](/ko/math/manifolds/uniqueness_of_submanifold)

이 글은 submanifold를 단사 immersion $$\Phi:P\rightarrow M$$으로 정의한 뒤, 그 이미지 $$\Phi(P)$$ 위의 manifold 구조가 언제 유일한지를 다룬다. 출발점은 간단한 질문—$$C^\infty$$ 함수 $$F:N\rightarrow M$$의 치역이 $$\Phi(P)$$ 안에 들어갈 때, $$F$$를 $$P$$로 factorize한 $$F_0=\bar{\Phi}^{-1}\circ F$$가 $$C^\infty$$냐는 것—인데, 예시 1의 figure-eight 같은 counterexample이 이 질문이 항상 "예"가 아니라는 것을 보여준다. $$\Phi(N)=\Psi(P)$$인 두 immersion이 서로 다른 위상을 $$P$$에 줄 수 있기 때문에, $$\bar{\Psi}^{-1}\circ\Phi$$가 연속이 아닌 경우가 생기는 것이 핵심인데, 부분다양체 글에서 figure-eight가 embedded가 아닌 예시로 나왔던 것과 같은 현상이 "factorization의 매끄러움"이라는 다른 각도에서 다시 등장한다는 것이 연결된다.

명제 2의 두 주장—"$$F_0$$가 연속이면 $$C^\infty$$이다"와 "$$\Phi$$가 embedding이면 $$F_0$$는 연속이다"—는 이 문제의 핵심을 정확히 가른다. 첫째 주장의 증명에서, $$F_0$$가 연속이라는 가정 하에 좌표계 $$(V,\psi)$$를 잡아 $$\psi\circ F_0=(\pi\circ\gamma\circ\Phi)\circ F_0=\pi\circ\gamma\circ F$$로 $$C^\infty$$임을 보이는 논증이 깔끔하다. $$\Phi$$의 좌표계를 $$F$$와 합성하면 $$F$$ 자체가 $$C^\infty$$이므로 factorization도 $$C^\infty$$가 된다는 것이, "immersion의 좌표계가 $$F$$의 $$C^\infty$$성을 전달한다"는 것을 보여준다. 둘째 주장은 embedding이면 subspace topology를 사용하므로 $$\bar{\Phi}$$가 homeomorphism이고, 따라서 $$\bar{\Phi}^{-1}$$이 연속이라는 것—이것은 정의에 가까운 논증이다.

정의 3의 equivalence—$$\Phi_1=\Phi_2\circ\theta$$를 만족하는 diffeomorphism $$\theta$$의 존재—는 "같은 이미지를 같게 만드는 diffeomorphism"이라는 자연스러운 동치관계인데, 각 equivalence class가 inclusion $$(A,\iota)$$로 수렴한다는 것이 이 글의 구조적 핵심이다. $$\bar{\Phi}:N\rightarrow A$$가 diffeomorphism이므로 $$\iota=\Phi\circ\bar{\Phi}^{-1}$$가 immersion이라는 논증이 간결하면서도, "equivalence class의 대표원소로 inclusion을 선택할 수 있다"는 것이 이후 유일성 논의의 기반이 된다.

명제 4와 5가 이 글의 결론이다. 명제 4—"주어진 topology $$\mathcal{T}$$ 위에서 submanifold 구조는 많아야 하나"—는 명제 2의 첫째 주장($$F_0$$가 연속이면 $$C^\infty$$)의 직접적인 결과인데, 두 개의 다른 미분구조가 같은 topology 위에 존재하면 identity map이 두 구조 사이의 $$C^\infty$$ 전단사함수이면서 그 역함수도 $$C^\infty$$여야 하는데, 명제 2가 이를 보장한다는 것이 논증의 골자이다. 명제 5는 더 강한 결론—subspace topology가 주어지면 그 위의 manifold 구조가 유일하다—인데, 증명에서 $$\dim(A,\mathcal{T}',\mathcal{A}')<\dim(A,\mathcal{T},\mathcal{A})$$인 경우를 measure zero set 개념으로 배제하는 부분이 가장 기술적이다. $$C^1$$ 함수가 measure zero set을 measure zero set으로 보낸다는 사실—Sard의 정리의 약한 버전—을 사용하는데, 이 결과가 정확히 어디서 오는지 이 글에서 언급되지 않는다.

이 글의 논증 구조—"topology가 고정되면 미분구조가 유일하다"→"subspace topology면 더 강한 유일성"—가 이후 음함수 정리나 rank theorem에서 부분다양체의 존재와 유일성을 동시에 다룰 때 기반으로 작용할 것이라는 예감이 든다. 부분다양체 글에서 embedded와 immersed를 구분한 동기가 여기서 정확히 payoff되는 구조인데, "왜 embedded 조건이 필요한가"에 대한 답이 "유일성 때문"이라는 것이 이 글의 핵심 메시지이다.

좋은 점: (1) 예시 1의 세 그림—두 immersion과 factorization의 실패—이 추상적 논의에 시각적 직관을 부여한다. (2) 명제 2의 증명이 $$\psi\circ F_0=\pi\circ\gamma\circ F$$라는 한 줄로 핵심이 정리되는 것이 elegant하다. (3) 명제 5의 증명에서 차원 비교와 measure zero 배제가 "왜 subspace topology가 유일성을 주는지"를 정확히 보여준다.

아쉬운 점: (1) 명제 5의 증명에서 사용하는 "measure zero set을 measure zero set으로 보낸다"는 사실의 출처가 명시되지 않았다—Sard의 정리인지, 아니면 더 기본적인 $$C^1$$ 결과인지 불분명하다. (2) 예시 2가 본문에서 언급되지만($$\Phi_1(N_1)=\Phi_2(N_2)$$인데 $$N_1,N_2$$가 diffeomorphic하지 않은 경우), 이 예시의 구체적 구성이 없어서 "왜 그런 immersion 쌍이 존재하는지"를 확인할 수 없다. (3) 명제 5의 증명에서 $$d(\id)$$가 전사가 아닌 점 $$a$$에서 $$\dim(A,\mathcal{T}',\mathcal{A}')<\dim(A,\mathcal{T},\mathcal{A})$$라는 결론이 "tangent space의 차원"에서 바로 나오는데, $$d(\id)$$가 단사+비전사이면 rank가 낮아지고 따라서 차원이 낮아진다는 논증이 암묵적으로 사용되고 있다.

⚠️ 정의 없이 사용: `measure zero set` (검색해도 없음 — 측도론 표준 용어이나 이 카테고리 이전 글에서 도입된 적 없음)

## [음함수 정리](/ko/math/manifolds/implicit_function_theorem)

이 글은 음함수 정리를 미분다양체로 확장하고, level set이 submanifold가 되는 충분조건을 다룬다. 출발점인 정의 1의 slice—좌표계 $$(U,\varphi)=(x^i)_{i=1}^m$$에서 뒤의 $$m-k$$개 좌표를 고정시킨 부분집합—는 "좌표 평면으로 자른 단면"이라는 직관인데, 부분다양체 글에서 rank theorem의 submersion case가 $$F$$의 level set을 좌표 평면으로 환원하는 것이었으므로 slice는 그 환원의 목표 형태이다. 보조정리 2—임의의 immersion $$F:M\rightarrow N$$이 주어지면 $$F(p)$$ 근방의 좌표계를 잡아 $$F(U)$$가 slice가 되도록 할 수 있다는 것—은 "immersed submanifold는 locally embedded이다"로 요약되는데, 부분다양체 글에서 figure-eight가 embedded가 아닌 예시로 나왔던 것과 비교하면, "국소적으로는 항상 embedded처럼 보인다"는 것이 이 보조정리의 메시지이다. 다만 $$F(M)\cap V$$가 일반적으로 slice가 될 필요가 없다는 관찰—임의의 열린근방 $$V$$를 잡아도 $$F$$의 전체 이미지가 slice로 잘리지 않을 수 있다는 것—이 immersion과 embedding의 차이를 다시 한번 보여준다.

음함수 정리(정리 3)의 정식 formulation—$$f:U\subset\mathbb{R}^{m-n}\times\mathbb{R}^n\rightarrow\mathbb{R}^n$$이 $$C^\infty$$이고, 어떤 점 $$(x_0,y_0)$$에서 $$s$$ 변수에 대한 $$n\times n$$ Jacobian submatrix가 nonsingular이면, $$f(p,q)=0\iff q=g(p)$$인 $$C^\infty$$ 함수 $$g$$가 존재—는 유클리드 공간의 고전적 음함수 정리인데, 이 정리의 핵심은 "방정식 $$f=0$$을 $$q$$에 대해 풀 수 있다"는 것이다. 부분다양체 글의 역함수 정리(정리 4)가 nonsingular Jacobian → 국소 diffeomorphism이었다면, 음함수 정리는 nonsingular submatrix → 남은 변수로의 함수 $$g$$의 존재인데, 두 정리의 구조적 유사성—Jacobian 조건 → 국소적 해의 존재—이 보인다.

따름정리 4(submersion level set theorem)—$$dF_p$$가 모든 $$p\in P$$에서 surjective이면 $$P=F^{-1}(q)$$ 위에 유일한 embedded submanifold 구조가 존재하고 codimension이 $$\dim N$$—는 이 글의 첫 번째 결론이다. 부분다양체 글에서 rank theorem의 submersion case와 immersion case를 다뤘는데, submersion level set theorem은 그 결과를 "level set 자체가 submanifold이다"로 바꾸는 것이다. $$\dim P=\dim M-\dim N$$이라는 결론은 rank-nullity theorem의 직접적인 결과인데, $$dF_p$$가 surjective이면 kernel의 차원이 $$\dim M-\dim N$$이고 그 kernel이 level set의 tangent space에 해당한다는 것이 직관적이다.

더 실용적인 따름정리 5(constant-rank level set theorem)—$$dF_p$$의 rank가 $$P$$ 위에서 일정하면 level set이 embedded submanifold—는 가정이 더 약하면서도 같은 결론을 주는데, "rank가 일정"이라는 조건이 "surjective"보다 확인하기 쉬운 경우가 많다는 것이 이 정리의 가치이다. 다만 "constant-rank"라는 용어 자체가 이 글에서 정의되지 않고 사용되고 있는데, $$dF_p$$의 rank가 $$P$$의 모든 점에서 같다는 의미로 해석하면 자연스럽지만 formal 정의가 있었으면 좋았을 것 같다.

예시 6—$$f(x)=\lvert x\rvert^2$$의 $$f^{-1}(1)$$이 $$S^n$$의 embedded submanifold 구조와 일치한다는 것—은 미분다양체의 예시들 글(예시 6, 7)에서 $$S^n$$을 직접 구성하고 level set으로도 볼 수 있다고 했던 것을, 음함수 정리의 틀 안에서 정당화하는 것이다. $$df_x(v)=2\sum r^i(x)v^i$$가 원점을 제외하면 항상 surjective라는 계산이 깔끔한데, "원점에서만 rank가 떨어진다"는 것이 $$S^n$$이 원점을 포함하지 않으므로 level set 조건이 만족된다는 것을 보여준다. 이 예시가 음함수 정리의 "첫 번째 payoff"인 것 같은데, 이후 $$\RP^n$$이나 Lie group의 subgroup 등에서도 같은 패턴—level set → Jacobian 확인 → embedded submanifold—을 사용할 것이라는 예감이 든다.

좋은 점: (1) slice라는 개념을 먼저 도입해서, 음함수 정리의 결론이 "locally slice"라는 것을 명확히 보여주는 구조이다. (2) 따름정리 4와 5를 나란히 두어 surjective vs constant-rank 조건의 강약을 비교할 수 있게 한 것이 실용적이다. (3) 예시 6이 앞 글들의 $$S^n$$ 구성과 연결되어 "왜 level set 관점이 유용한지"를 보여준다.

아쉬운 점: (1) 보조정리 2와 정리 3의 증명이 빈 details 태그로 되어 있어서, 핵심 논증을 확인할 수 없다—특히 음함수 정리의 증명은 contractive mapping principle을 사용하는 것으로 알려져 있는데, 그 과정이 없으니 정리의 "무게"를 체감하기 어렵다. (2) 따름정리 5의 "constant-rank" 조건이 어떤 의미에서 surjective보다 약한지—rank가 떨어지면 어떤 일이 생기는지—에 대한 반례나 직관적 설명이 없다. (3) $$df_x$$의 surjectivity 계산에서 "원점을 제외하면"이라는 조건의 기하학적 의미—$$f$$의 gradient가 원점에서 0이라는 것, 즉 $$f$$가 원점에서 critical point를 가진다—에 대한 해석이 없다.

⚠️ 정의 없이 사용: `constant-rank` (검색해도 없음 — $$dF_p$$의 rank가 일정하다는 의미로 해석되지만 이 용어 자체가 prior 노트에서 도입된 적 없음)

## [접다발과 여접다발](/ko/math/manifolds/tangent_and_cotangent_bundles)

이 글은 접다발 $$TM$$을 구체적으로 구성하고, 벡터다발의 일반적 프레임워크—smooth functor—를 통해 여접다발 $$T^\ast M$$을 비롯한 파생 다발들을 한꺼번에 정의한다. 출발점인 정의 1의 vector bundle—$$\pi:E\rightarrow B$$가 fiberwise로 $$k$$차원 벡터공간 구조를 갖고, 국소적으로 $$U\times\mathbb{R}^k$$와 homeomorphic—은 "국소적으로는 평평한 벡터공간의 묶음"이라는 직관인데, 미분다양체의 예시들 글에서 $$S^n$$을 여러 chart로 덮었던 것과 같은 "국소적 trivialization"의 아이디어가 다발에도 적용된다는 것이 보인다. 각 fiber $$E_b$$가 벡터공간이라는 요구가 covering space의 fiber가 discrete set이었던 것에서 벡터공간으로의 확장인데, 대수적 위상수학 카테고리의 특성류 글에서 이미 vector bundle을 다뤘기 때문에 이 정의가 낯설지는 않다. 다만 그때는 "왜 vector bundle이 필요한가"라는 동기 없이 정의만 나왔는데, 이 글이 접다발이라는 구체적 목표를 가지고 vector bundle을 도입하니 동기가 더 명확하다.

예시 2의 접다발 구성—$$TM=\bigsqcup_{p\in M}T_pM$$에 coordinate system $$\tilde{\varphi}(v)=(x^1(\pi(v)),\ldots,x^m(\pi(v)),dx^1(v),\ldots,dx^m(v))$$를 주는 것—이 이 글의 핵심이다. $$\tilde{\varphi}$$가 $$\pi^{-1}(U)$$를 $$\varphi(U)\times\mathbb{R}^m$$으로 보내는 것인데, 접공간 글에서 $$\partial/\partial x^i\big|_p$$가 $$T_pM$$의 basis라는 것을 보였으므로 $$dx^i(v)$$가 tangent vector $$v$$의 좌표 성분이라는 것이 이해된다. transition map $$\tilde{\psi}\circ\tilde{\varphi}^{-1}$$의 각 성분—$$(\psi\circ\varphi^{-1})(p)$$와 $$dy^j(\sum v^i\partial/\partial x^i)=\sum v^i\partial y^j/\partial x^i$$—이 모두 $$C^\infty$$라는 계산이 깔끔한데, 앞부분은 미분구조의 transition map이고 뒷부분은 미분사상 글에서 $$dF_p$$의 행렬이 Jacobian matrix라는 것과 같은 결과이다. $$TM$$이 $$2m$$차원 manifold가 된다는 결론—base의 $$m$$차원더하기 fiber의 $$m$$차원—이 직관적이다.

local trivialization $$\phi:v\big|_p\mapsto(p,dx^1(v),\ldots,dx^m(v))$$의 구성에서, $$\tilde{\varphi}=(\varphi\times\id_{\mathbb{R}^m})\circ\phi$$라는 식이 $$\phi$$가 diffeomorphism임을 보여주는 것이 elegant한데, $$\varphi\times\id_{\mathbb{R}^m}$$이 diffeomorphism이라는 것이 미분다양체의 예시들 글의 product manifold 성질을 사용한다는 것이 보인다. $$TM$$이 trivial bundle이면 $$M$$을 parallelizable manifold라고 부른다는 정의는 "접다발이 전역적으로 $$M\times\mathbb{R}^m$$과 동형인지"라는 질문을 던지는데, $$S^n$$이 parallelizable인지 아닌지는 이 글에서 다루지 않지만 이후 orientation이나 vector field에서 다시 나올 것이라는 예감이 든다.

정의 3의 bundle map—$$E\rightarrow E'$$와 $$B\rightarrow B'$$가 주어져서 fiberwise로 isomorphism인 것—은 "다발 사이의 morphism"이라는 자연스러운 정의인데, 범주론 카테고리에서 배운 "화살표의 조건"이 여기서 fiberwise isomorphism으로 구체화된다는 것이 느껴진다. 더 흥미로운 것은 정의 4의 smooth functor—$$\mathbf{FVect}_\text{iso}\times\mathbf{FVect}_\text{iso}\rightarrow\mathbf{FVect}_\text{iso}$$가 $$f,g$$에 대해 smooth하게 의존하는 것—인데, 선형대수학의 연산(dual, tensor product, exterior power 등)이 모두 smooth functor라는 관찰이 인상적이다. $$\Hom(-,-)$$이 smooth functor라는 증명에서 $$g\mapsto\Hom(f,g)$$의 방향미분이 $$u\mapsto w_i^j\circ u\circ f^{-1}$$로 계산되는 부분이 구체적인데, "벡터공간 위의 함수가 smooth하다"라는 것이 미분다양체의 예시들 글에서 벡터공간에 미분구조를 준 것과 연결된다는 것이 보인다.

정리 6—smooth functor를 vector bundle에 fiberwise로 적용하면 다시 vector bundle이 된다—는 이 글의 구조적 핵심이다. 이 정리가 없으면 cotangent bundle, tensor bundle 등을 정의할 때마다 vector bundle 조건을 새로 증명해야 할 텐데, "fiberwise 선형대수 연산 → 자동으로 vector bundle"이라는 것이 이 정리의 메시지이다. 여접다발 $$T^\ast M$$을 $$(TM)^\ast$$로 정의하는 정의 7이 이 정리의 첫 번째 적용인데, 접공간 글에서 $$T_p^\ast M$$을 개별적으로 정의한 것과 달리 여기서는 "한꺼번에 묶어서" 다발로 만든다는 것이 차원 높은 관점이다. dual functor $$(-)^\ast$$가 smooth functor이므로 정리 6이 적용된다는 것이 깔끔한데, tensor product나 exterior power도 같은 방식으로 적용되니 "하나의 원리로 모든 파생 다발을 커버한다"는 것이 smooth functor 프레임워크의 힘이다.

좋은 점: (1) vector bundle의 정의 → 접다발의 구체적 구성 → smooth functor라는 흐름이 "일반적 도구 → 구체적 예시 → 다시 일반적 도구"의 구조인데, 이 흐름이 글 전체를 관통한다. (2) 접다발의 transition map 계산이 미분사상 글의 Jacobian matrix 결론과 자연스럽게 연결되어, "differential이 fiberwise로 어떻게 작용하는지"를 보여준다. (3) smooth functor의 예시 목록(dual, tensor, exterior, Hom, direct sum)이 선형대수학 카테고리의 주요 연산을 한눈에 보여주는 것이 좋다.

아쉬운 점: (1) $$\Hom(-,-)$$이 smooth functor라는 증명에서 $$f$$의 smoothness를 보이는 부분이 "번거롭지만 같은 논증"이라고만 되어 있어서, 핵심 논증이 압축되어 있다. (2) parallelizable manifold의 예시—어떤 manifold가 parallelizable이고 어떤 아닌지—가 없어서, 이 개념이 이후 어디서 중요한 역할을 하는지에 대한 직관이 부족하다. (3) 정리 6의 증명이 "[MS]의 정리 3.6"으로 reference만 되어 있어서, fiberwise 구성이 왜 vector bundle 조건을 만족하는지에 대한 핵심 아이디어를 확인할 수 없다.

⚠️ 정의 없이 사용: `smooth functor` (검색해도 없음 — 이 글에서 정의 4로 도입되나, prior 노트에서 처음 등장)
⚠️ 정의 없이 사용: `bundle map` (검색해도 없음 — 이 글에서 정의 3으로 도입되나, prior 노트에서 처음 등장)
⚠️ 정의 없이 사용: `parallelizable` (검색해도 없음 — 이 글에서 정의되나, prior 노트에서 처음 등장)

## [벡터장](/ko/math/manifolds/vector_fields)

이 글은 접다발의 smooth section으로서 벡터장을 정의하고, 그 매끄러움 조건을 동치 조건으로 분류한 뒤 integral flow까지 전개한다. 출발점인 정의 1—vector bundle $$\pi:E\rightarrow M$$의 section을 $$\pi\circ\sigma=\id_M$$인 $$\sigma:M\rightarrow E$$로 정의하는 것—은 접다발 글에서 정의한 vector bundle의 구조를 "뒤집어 보는" 관점인데, $$E$$가 국소적으로 $$U\times\mathbb{R}^k$$와 동형이라는 것이 각 점 $$p$$에서 fiber $$E_p$$의 원소를 고르는 함수 $$\sigma$$의 존재를 보장한다는 것이 이해된다. 접다발 $$TM$$의 section을 벡터장이라고 부르는 것은 자연스러운데, 각 점 $$p$$에서 $$X_p\in T_pM$$이므로 접공간 글에서 정의한 "함수에 작용하는 연산자"로서의 접벡터가 점 $$p$$마다 하나씩 붙어있는 그림이 된다. $$X_p(f)$$를 "점 $$p$$에서 $$f$$를 $$X$$ 방향으로 미분한 값"으로 읽으면 벡터장이 "공간 위에 붙은 미분 연산자들의 장"이라는 직관이 생긴다.

명제 2의 세 동치 조건—(1) $$X$$가 $$TM\rightarrow M$$으로서 $$C^\infty$$, (2) 좌표 basis로 쓴 성분 $$a^i$$가 $$C^\infty$$, (3) 임의의 $$C^\infty$$ 함수 $$f$$에 대해 $$X(f)$$가 $$C^\infty$$—중 (2)→(3)의 증명이 가장 인상적이다. $$X(f)=\sum a^i\frac{\partial f}{\partial x^i}$$인데, $$a^i$$가 $$C^\infty$$이고 $$\frac{\partial f}{\partial x^i}$$도 $$C^\infty$$이므로 합이 $$C^\infty$$라는 것이 "성분이 매끄러우면 벡터장 자체가 매끄럽다"는 주장의 핵심인데, (3)→(1)의 역방향—$$X(x^i)=dx^i\circ X$$가 $$C^\infty$$임을 coordinate function에 적용하여 보이는 것—이 "함수에 작용하는 연산자"라는 관점이 smoothness 검증에 직접 쓰인다는 것을 보여준다. 접다발 글의 $$dx^i$$가 tangent vector의 좌표 성분을 읽는 함수였는데, 그 $$dx^i$$를 벡터장 $$X$$에 합성하면 $$X(x^i)=a^i$$가 되는 것이 "좌표 성분 = coordinate function에 대한 작용"이라는 등식을 보여주는 좋은 예시이다.

$$\mathfrak{X}(M)$$을 $$C^\infty(M)$$-module로 보는 관점이 이 글의 구조적 핵심이다. 예시 3의 $$\mathbb{R}$$ 위에서 $$fX$$가 $$X$$의 상수배가 아닌 경우—$$f$$가 상수함수가 아니면 $$f(p)\frac{d}{dx}\big|_p$$가 $$\frac{d}{dx}\big|_p$$의 스칼라 배가 아니라는 것—는 $$\mathfrak{X}(M)$$이 $$\mathbb{R}$$-벡터공간으로서 너무 거대하다는 것을 보여주는데, $$C^\infty(M)$$-module로 보면 "함수 $$f$$로 스칼라곱하는" 연산이 자연스럽게 포함된다는 것이 이 관점의 가치이다. hairy ball theorem—$$S^2$$ 위의 연속 벡터장은 반드시 영점이 존재한다는 것—을 사용하여 $$\mathfrak{X}(S^2)$$가 두 벡터장으로 생성될 수 없다는 논증이 간결하면서도 강력한데, $$X_1(p)=0$$인 점 $$p$$에서 $$T_pM$$이 $$\{0,X_2(p)\}$$로 생성되어야 한다는 것이 $$T_pM$$이 2차원이라는 것에 모순된다는 것이 핵심이다. 접다발 글에서 $$S^2$$이 parallelizable인지 여부를 물었는데, 여기서 $$S^2$$이 global frame을 갖지 못한다는 것이 확인되니 "hairy ball theorem이 $$S^2$$의 비parallelizability의 원인"이라는 것이 명확해진다.

정리 6의 integral flow—$$\sigma'(t)=X(\sigma(t))$$를 만족하는 $$C^\infty$$ curve—는 상미분방정식의 존재·유일성 정리를 manifold로 옮긴 것인데, 증명이 생략되어 있지만 결론의 구조를 따라가면 이해된다. 1~3번은 "각 점마다 maximal integral flow가 유일하게 존재", 7번은 "$$\phi^t$$가 diffeomorphism이고 역함수가 $$\phi^{-t}$$", 8번은 "$$\phi^s\circ\phi^t=\phi^{s+t}$$"인데, 이 조건들이 합쳐지면 $$\phi^t$$들이 group action을 이룬다는 것이 "벡터장 = infinitesimal symmetry generator"라는 관점의 정확한 의미이다. 정의 7의 complete—모든 $$t$$에 대해 $$\mathcal{D}_t=M$$—은 "벡터장이 전역적으로 흐름을 정의한다"는 것인데, compact manifold 위의 벡터장은 항상 complete라는 것을 이후에 확인할 수 있을 것이라는 예감이 든다.

좋은 점: (1) section → vector field → smoothness 동치 조건 → $$C^\infty(M)$$-module → hairy ball → integral flow라는 흐름이 "정의 → 성질 → 구조 → 응용 → 역학"으로 자연스럽게 이어진다. (2) 명제 2의 세 동치 조건이 "벡터장의 매끄러움"을 세 가지 각도에서 보여주면서도, 접공간·미분사상 글의 개념들이 여기서 어떻게 쓰이는지를 동시에 보여준다. (3) hairy ball theorem의 적용이 $$S^2$$의 비parallelizability를 직접적으로 보여주는 것이 구체적이다.

아쉬운 점: (1) hairy ball theorem이 "잘 알려진 정리"로만 인용되고 정확한 출처나 직관적 설명이 없어서, 이 정리의 "무게"를 체감하기 어렵다—적어도 $$S^2$$ 위에서 벡터장의 영점을 찾는 간단한 직관(예: Euler characteristic)이 있었으면 좋았을 것 같다. (2) 정리 6의 증명이 생략되어 있어서, integral flow의 존재성이 "상미분방정식의 존재·유일성"에서 어떻게 나오는지—contractive mapping principle인지 Picard iteration인지—를 확인할 수 없다. (3) complete 벡터장의 예시—어떤 벡터장이 complete이고 아닌지—가 없어서, 이 개념이 이후 어디서 중요한 역할을 하는지에 대한 직관이 부족하다.

⚠️ 정의 없이 사용: `hairy ball theorem` (검색해도 없음 — 위상수학의 정리로 $$S^2$$ 위의 연속 벡터장은 영점을 가진다는 것이나, 이 카테고리 이전 글에서 도입된 적 없음)
⚠️ 정의 없이 사용: `Euler characteristic` (검색해도 없음 — 대수적 위상수학 카테고리에서 다루지만 이 노트에서 직접 사용하지는 않음 — 다만 hairy ball theorem의 직관과 관련하여 떠오른 개념)

## [미분형식](/ko/math/manifolds/differential_forms)

이 글은 접다발과 여접다발 위의 tensor bundle, exterior algebra bundle을 fiberwise 선형대수 연산으로 정의한 뒤, 그 smooth section인 미분형식과 pullback, 외미분, interior multiplication을 다룬다. 출발점인 정의 1—$$\mathcal{T}^{r,s}(M)=\mathcal{T}^{r,s}(TM)$$, $$\bigwedge^k(M)=\bigwedge^k(T^\ast M)$$—은 접다발 글의 정리 6(smooth functor를 vector bundle에 fiberwise로 적용하면 다시 vector bundle)을 직접 사용하는 첫 번째 실례인데, tensor bundle과 exterior bundle이 모두 smooth functor의 적용이라는 것이 한꺼번에 정의되는 것이 인상적이다. 접다발 글에서 smooth functor 프레임워크를 "하나의 원리로 모든 파생 다발을 커버한다"고 했는데, 이 글이 그 원리의 첫 번째 payoff이다.

pairing $$(-,-)$$의 두 형태—tensor의 경우 $$\alpha^1(u_1)\cdots\alpha^{r+s}(u_{r+s})$$, exterior의 경우 $$\det(\alpha^i(u_j))$$—가 모두 non-degenerate이라는 것은 선형대수학 카테고리의 쌍대공간 글에서 배운 것인데, $$\bigwedge^k(T_p^\ast M)\cong\bigwedge^k(T_pM)^\ast$$라는 동치성이 tensor의 경우와 구조적으로 같으면서 determinant로 표현된다는 것이 새롭다. 특히 $$\bigwedge(T_p^\ast M)\cong\bigwedge(T_pM)^\ast$$라는 결론은 exterior algebra 전체가 "자기 자신과 쌍대"라는 것인데, 이 동치가 basis 선택과 무관한 자연스러운 것인지에 대한 논의가 없어서 여접공간 글에서같은 질문을 했던 것이 여전히 풀리지 않는다.

미분형식 $$\omega\in\Omega^\ast(M)$$을 smooth section으로 보는 관점—각 점 $$p$$에서 $$\omega_p\in\bigwedge^\ast(T_pM)$$—은 벡터장을 접다발의 smooth section으로 정의한 것과 정확히 같은 패턴인데, 벡터장 글에서 "함수에 작용하는 연산자"로서의 접벡터가 점마다 하나씩 붙어있다면, 미분형식은 "접벡터에 작용하는 쌍대원소"가 점마다 하나씩 붙어있는 것이다. $$\Omega^\ast(M)$$이 $$\mathbb{N}$$-graded $$C^\infty(M)$$-algebra라는 관찰—계수를 $$\mathbb{R}$$이 아니라 $$C^\infty(M)$$으로 볼 수 있다는 것—은 벡터장 글의 $$\mathfrak{X}(M)$$이 $$C^\infty(M)$$-module이었던 것과 같은 맥락인데, "함수로 스칼라곱한다"는 연산이 미분형식에서도 자연스럽게 포함된다는 것이 느껴진다.

pullback $$F^\ast$$의 정의—$$(F^\ast\omega)_p=\bigwedge(dF_p^\ast)(\omega_{F(p)})$$—는 미분사상 글에서 $$dF_p$$의 dual map을 사용하는 것인데, $$dF_p^\ast$$가 $$T_{F(p)}^\ast N$$에서 $$T_p^\ast M$$으로 가는 linear map이고, 여기에 exterior algebra의 functoriality를 적용하는 것이 핵심이다. 미분사상 글에서 $$F^\ast:g\mapsto g\circ F$$를 "pullback"이라고 불렀는데, 이 글에서의 $$F^\ast$$가 그 일반화—함수에서 미분형식으로—라는 것이 명확해진다. $$F^\ast$$가 graded algebra homomorphism이고 $$\wedge$$를 보존한다는 것은 pullback이 "대수 구조를 보존하면서 옮긴다"는 것인데, 이후 de Rham cohomology에서 chain map으로 작용할 것이라는 예감이 든다.

외미분 $$d$$의 정의—degree 1의 anti-derivation, $$d^2=0$$, $$\Omega^0$$에서의 $$df$$가 함수의 differential과 일치—는 접공간 글에서 $$df_p:T_pM\rightarrow\mathbb{R}$$를 정의한 것의 자연스러운 확장인데, $$d$$가 $$k$$-form을 $$(k+1)$$-form으로 보내면서 $$d^2=0$$이라는 것이 de Rham complex의 cochain 구조를 만든다는 것이 이 글의 구조적 핵심이다. $$d$$가 $$F^\ast$$와 commute한다는 것은 $$F^\ast$$가 de Rham complex들 사이의 chain map이라는 것인데, $$F^\ast$$가 graded algebra homomorphism이면서 $$d$$와 commute하므로 DG-algebra 사이의 morphism이 된다는 것이 범주론 카테고리에서 배운 "구조를 보존하는 map"의 좋은 예시이다.

interior multiplication $$\iota_X$$—$$k$$-form을 $$(k-1)$$-form으로 보내는 degree $$-1$$의 anti-derivation—는 벡터장 $$X$$와 미분형식 $$\omega$$를 "결합"하는 연산인데, $$\iota_X\omega(X_1,\ldots,X_{k-1})=\omega(X,X_1,\ldots,X_{k-1})$$라는 정의가 "벡터장을 첫 번째 슬롯에 끼워 넣는다"는 직관을 정확히 반영한다. $$\iota_X$$가 anti-derivation이라는 것은 $$\iota_X(\omega\wedge\eta)=(\iota_X\omega)\wedge\eta+(-1)^k\omega\wedge(\iota_X\eta)$$라는 것인데, $$d$$도 anti-derivation이므로 $$d$$와 $$\iota_X$$가 같은 대수적 성질을 공유한다는 것이 흥미롭다. 이후 Lie derivative $$\mathcal{L}_X=d\circ\iota_X+\iota_X\circ d$$의 공식—Cartan's magic formula—에서 $$d$$, $$\iota_X$$, $$\mathcal{L}_X$$ 세 연산의 관계가 나올 것이라는 예감이 든다.

좋은 점: (1) 정의 1이 접다발 글의 smooth functor 프레임워크를 직접 적용해서 tensor bundle과 exterior bundle을 한꺼번에 정의하는 것이 "일반적 도구의 첫 번째 적용"으로서 자연스럽다. (2) pullback의 정의가 $$dF_p^\ast$$ → exterior algebra functoriality → fiberwise 적용이라는 세 단계로 분해되어 있어서, "왜 이 정의가 되는가"에 대한 동기가 정의 안에 포함되어 있다. (3) de Rham complex의 도입—$$d^2=0$$ → cochain complex → cohomology—이 한 줄의 흐름으로 이어지는 것이 간결하다.

아쉬운 점: (1) $$\bigwedge^k(T_p^\ast M)\cong\bigwedge^k(T_pM)^\ast$$라는 동치성이 basis 선택과 무관한 자연스러운 것인지에 대한 논의가 없다—여접공간 글에서같은 질문을 했는데 여기서도같은 문제가 반복된다. (2) 정리 2의 존재성과 증명이 "[##ref##]()"로 reference만 되어 있어서, anti-derivation $$d$$가 왜 유일하게 존재하는지—어떤 construction으로 $$d$$를 explicit하게 만드는지—를 확인할 수 없다. (3) interior multiplication의 예시가 없어서, $$\iota_X$$가 구체적으로 어떻게 작용하는지—예를 들어 $$\mathbb{R}^3$$에서의 2-form에 $$\iota_X$$를 적용하면 어떻게 되는지—를 체감하기 어렵다.

⚠️ 정의 없이 사용: `anti-derivation` (검색해도 없음 — degree $$k$$의 derivation에 $$(-1)^k$$ 부호가 붙은 것인데, 이 용어 자체가 prior 노트에서 도입된 적 없음)
⚠️ 정의 없이 사용: `graded algebra` (검색해도 없음 — 선형대수학 카테고리의 다중선형대수학에서 다루지만 이 노트에서 직접 사용하지는 않음)
⚠️ 정의 없이 사용: `chain map` (검색해도 없음 — 대수적 위상수학 카테고리에서 정의되지만 이 노트에서 직접 사용하지는 않음)

## [부분다양체와 역함수 정리](/ko/math/manifolds/submanifolds)

이 글은 immersion, submanifold, embedded submanifold를 정의하고, 유클리드 공간의 역함수 정리를 manifold로 가져온 뒤 rank theorem까지 전개한다. 정의 1의 세 단계—immersion($$dF_p$$가 단사), submanifold(immersion + 단사함수), embedding(submanifold + subspace topology와의 homeomorphism)—는 differential의 성질로부터 부분다양체의 "깊이"를 구분하는 것인데, 미분사상 글에서 $$dF_p$$가 isomorphism인 경우를 다뤘다면 이 글은 $$dF_p$$가 단사 또는 전사인 더 넓은 상황을 다룬다는 것이 확장의 방향이다. (b)의 figure-eight 예시—submanifold이지만 embedded가 아닌 경우—가 $$F((-1,1))$$이 subspace topology에서 열린집합이 아니라는 것에서 실패하는 것이 인상적인데, "부분집합의 위상"과 "원래 manifold 위에서 물려받은 위상"이 다를 수 있다는 것이 이 글의 핵심 동기이다.

정리 4의 역함수 정리—유클리드 공간에서 nonsingular Jacobian → 국소 diffeomorphism—를 따름정리 5에서 manifold로 옮기는 논증이 깔끔하다. 좌표계 $$(W,\tau)$$와 $$(V,\varphi)$$를 잡아 $$\tau\circ F\circ\varphi^{-1}$$의 Jacobian을 확인한 뒤 유클리드 버전을 적용하는 것은 "manifold의 문제를 유클리드 공간으로 환원한다"는 미분기하학의 기본 전략을 역함수 정리에 적용한 첫 실례인데, 이후 부분다양체의 국소 좌표 정리에서도 같은 패턴이 반복될 것이라는 예감이 든다.

따름정리 7과 8—$$k$$개의 independent 함수에 나머지 $$m-k$$개를 붙여 coordinate system을 만드는 것—은 선형대수학 카테고리의 기저 확장 정리를 $$T_p^\ast M$$에 적용한 것인데, $$dy^i$$들이 linearly independent이면 나머지 basis 원소들을 적절히 골라 합칠 수 있다는 것이 "기저 확장 = 좌표 확장"이라는 대응이다. 이 연결이 가장 직접적으로 드러나는 것이 따름정리 7의 증명에서 "보조정리 2의 증명과 마찬가지로 $$dy^i$$들을 하나씩 넣고 $$dx^j$$들을 하나씩 빼는" 부분인데, 선형대수학에서 배운 basis replacement가 미분기하학의 coordinate construction으로 번역된다는 것이 새롭다.

따름정리 9와 10—rank theorem의 submersion case와 immersion case—은 이 글의 기술적 하이라이트이다. submersion case에서 $$(dF_p)^\ast(dy^i)=d(y^i\circ F)$$가 $$T_p^\ast M$$에서 linearly independent이라는 것이 핵심인데, $$dF_p$$가 surjective이면 dual map이 injective라는 것이 선형대수학의 기본 사실이고, 이를 따름정리 7에 적용하면 $$x^1=y^1\circ F,\ldots,x^n=y^n\circ F$$에 나머지를 붙여 coordinate system을 얻는다. immersion case도 같은 논리의 dual 버전—$$(dF_p)^\ast$$가 surjective이므로 $$d(y^j\circ F)$$들이 $$T_p^\ast M$$을 span하고, 따름정리 8의 부분집합 선택이 적용된다. 두 case의 구조적 대칭성—dual map의 injectivity/surjectivity가 반대로 가는 것—이 선형대수학의 rank-nullity theorem의 그림자라는 것을 느낀다.

좋은 점: (1) immersion/embedded의 구별을 figure-eight 예시로 보여주는 것이 추상적 정의에 concrete한 시각적 직관을 부여한다. (2) 역함수 정리를 유클리드 → manifold로 옮기는 논증이 "좌표계를 잡고 환원한다"는 패턴을 처음으로 명시적으로 보여주는 좋은 예시이다. (3) rank theorem의 두 case가 dual map의 injectivity/surjectivity로 통일되면서, 선형대수학의 구조가 미분기하학에서 그대로 작동한다는 것을 체감하게 한다.

아쉬운 점: (1) embedded submanifold의 필요성—"왜 immersed만으로는 부족한가"에 대한 동기가 예시 하나로만 설명되고, embedded 조건이 이후 어떤 정리에서 필요한지에 대한 언급이 없다. (2) 따름정리 9의 증명에서 $$x^i=y^i\circ F$$로 정의한 $$x^1,\ldots,x^n$$이 $$p$$ 근방에서 well-defined된다는 것—$$y^j$$들이 $$F(p)$$ 근방에서 정의되어 있으므로 $$y^j\circ F$$가 $$p$$ 근방에서 정의된다는 것—이 명시되지 않았다. (3) 역함수 정리의 유클리드 버전(정리 4) 자체의 증명이 없이 그냥 인용되고 있는데, 이 정리의 핵심 아이디어—contractive mapping principle로 역함수의 존재를 보이는 것—를 간단히라도 언급했으면 좋았을 것 같다.

## [미분사상의 예시들](/ko/math/manifolds/examples_of_differentials)

이 글은 앞서 정의한 differential의 추상적 틀에 concrete한 살을 붙이는 역할을 한다. 출발점은 manifold 위의 $$C^\infty$$ 곡선 $$\gamma:(a,b)\rightarrow M$$과 그 속도벡터 $$\gamma'(t)=d\gamma_t(d/dr\big|_t)$$인데, 속도벡터를 "곡선의 미분"이 아니라 "곡선의 differential이 $$\mathbb{R}$$의 표준 basis를 어디로 보내는가"로 정의하는 것이 인상적이다. $$\gamma'(t)f=(f\circ\gamma)'(t)$$라는 공식을 풀어쓰면, 속도벡터가 함수 $$f$$에 작용한다는 것이 "함수를 곡선 위로 끌어당긴 뒤 $$\mathbb{R}$$ 위에서 미분한다"는 것과 같다는 것이 명확해지는데, 접공간 글에서 접벡터를 "함수에 작용하는 연산자"로 정의한 것이 여기서 자연스럽게 사용된다.

명제 2—영벡터가 아닌 임의의 $$v\in T_pM$$에 대하여 $$p$$를 지나고 $$p$$에서의 속도벡터가 $$v$$인 $$C^\infty$$ 곡선이 존재한다는 것—는 접공간을 "곡선들의 equivalence class"로 생각해도 된다는 관찰의 절반을 증명하는 것이다. 좌표계 $$(U,\varphi)$$를 $$v=d\varphi^{-1}_{\varphi(p)}(\partial/\partial r^1\big|_0)$$가 되도록 고른 뒤 $$\gamma:t\mapsto\varphi^{-1}(t,0,\cdots,0)$$로 구성하는 증명이 깔끔한데, $$d\psi_p(v)$$를 포함하는 기저를 만들어 change of basis를 합성한다는 아이디어가 선형대수학 카테고리에서 배운 기저 변경의 응용이라는 것이 보인다.

명제 3—$$dF_p(v)=(F\circ\gamma)'(0)$$—이 이 글에서 가장 설득력 있는 결과이다. $$dF_p$$가 tangent vector를 tangent vector로 보낸다는 abstract한 주장이, "곡선 $$\gamma$$를 $$F$$로 옮긴 뒤 속도벡터를 구하라"는 concrete한 절차로 번역된다는 것이 differential의 기하학적 의미를 체감하게 한다. $$\mathbb{R}^m$$에서의 속도벡터 $$(\gamma'(t)=(\frac{d\gamma^1}{dr},\cdots,\frac{d\gamma^m}{dr}))$$가 통상적인 미분과 일치한다는 관찰(정의 1 이후)은 "manifold 위의 미분이 유클리드 공간의 미분을 일반화한다"는 주장을 확인하는 것이면서도, 유클리드 공간의 직관을 manifold 위로 옮기는 데 이 공식이 다리 역할을 한다는 것을 느낀다.

벡터공간의 접공간 섹션에서, $$m$$차원 $$\mathbb{R}$$-벡터공간 $$V$$에 대하여 $$V\cong T_xV$$가 basis 선택과 무관하게 성립한다는 것(명제 4)은 선형대수학 카테고리에서 배운 "자연스러운 isomorphism"의 좋은 예시이다. $$v\mapsto D_v\big|_x$$라는 대응이 linear임을 보이는 증명—$$D_{v+w}\big|_x=D_v\big|_x+D_w\big|_x$$와 $$D_{\alpha v}\big|_x=\alpha D_v\big|_x$$를 직접 계산으로 보이는 것—이 간결하면서도, 이 isomorphism이 "방향미분"이라는 하나의 아이디어에서 나온다는 것이 핵심이다. 더 중요한 것은 $$L:V\rightarrow W$$가 linear map일 때 $$V\cong T_xV$$와 $$W\cong T_{L(x)}W$$ 사이의 diagram이 commute한다는 것인데, $$dL_x(D_v\big|_x)=D_{L(v)}\big|_{L(x)}$$라는 계산이 "linear map의 differential은 linear map 자체"라는 결론으로 이어지는 것이 인상적이다. 이 결과는 이후 vector bundle에서 fiberwise linear map의 differential을 다룰 때 핵심적으로 사용될 것이라는 예감이 든다.

Tangent covector 섹션에서, $$C^\infty$$ 함수 $$f:M\rightarrow\mathbb{R}$$의 differential $$df_p$$를 $$(T_pM)^\ast$$의 원소로 보는 관점—$$T_pM\xrightarrow{df_p}T_{f(p)}\mathbb{R}\xrightarrow{\sim}\mathbb{R}$$—은 여접공간 글에서 $$\mathfrak{m}_p/\mathfrak{m}_p^2\cong(T_pM)^\ast$$를 보인 것과 연결된다. 명제 7—$$\xi^i\big|_p=dx^i\big|_p$$, 즉 coordinate function $$x^i$$의 differential이 dual basis를 이룬다는 것—의 증명이 $$dx^i\big|_p(\partial/\partial x^j\big|_p)=\delta_{ij}$$라는 한 줄로 끝나는 것이 elegant한데, 여접공간 글의 보조정리 1에서 $$\mathfrak{m}_p/\mathfrak{m}_p^2$$의 basis가 $$\mathbf{x}^i+\mathfrak{m}_p^2$$라는 것과 정확히 같은 결과가 다른 언어로 표현된다는 것을 느낀다. $$dx^i$$라는 표기법이 coordinate function의 differential에서 자연스럽게 나온다는 것이, 미분기하학에서의 $$dx^i$$가 "무한소"가 아니라 정확히 정의된 대수적 대상이라는 것을 보여준다.

좋은 점: (1) 속도벡터의 정의가 differential의 정의에서 직접 나온다는 것이 미분사상 글과 이 글을 자연스럽게 연결한다. (2) 명제 3의 $$dF_p(v)=(F\circ\gamma)'(0)$$가 differential의 abstract한 정의에 concrete한 해석을 부여하는 것이 이 글의 핵심 공헌이다. (3) 명제 4의 commuting diagram이 "linear map의 differential = linear map"이라는 통찰을 보여주는 것이 vector bundle과 Lie group으로 나아가는 데 좋은 출발점이 될 것 같다.

아쉬운 점: (1) 명제 2의 증명에서 "좌표계 $$(U,\psi)$$를 하나 고른 후, $$d\psi_p(v)$$가 옮겨진 벡터를 포함하는 $$\mathbb{R}^n$$의 새로운 기저를 만든다"는 부분이 너무 압축되어 있다—change of basis를 어떻게 구성하는지 구체적 단계가 없어서, 선형대수학에 익숙하지 않은 독자는 이 한 문장을 이해하기 어려울 것 같다. (2) 명제 4의 commuting diagram에서 $$V\cong T_xV$$와 $$W\cong T_{L(x)}W$$가 basis 선택과 무관한 자연스러운 isomorphism이라는 주장이 있지만, $$L$$이 nonlinear인 경우 diagram이 commute하지 않는다는 반례가 없어서 "basis 무관성"의 의미가 충분히 전달되지 않는다. (3) $$dx^i$$가 dual basis라는 명제 7의 증명 뒤에 나오는 $$T_p^\ast M\cong(\mathfrak{m}_p/\mathfrak{m}_p^2)^{\ast\ast}\cong\mathfrak{m}_p/\mathfrak{m}_p^2$$라는 언급이 여접공간 글의 내용을 재탕하는 것인데, 이 동치성이 basis 선택과 무관한 자연스러운 것인지에 대한 논의가 여전히 없다.

## [리 미분](/ko/math/manifolds/Lie_derivative)

이 글은 벡터장의 integral flow를 사용하여 함수, 벡터장, 미분형식을 "방향미분"하는 리 미분을 정의하고, Lie bracket과 F-relatedness를 다룬다. 출발점은 함수의 리 미분—$$(\mathcal{L}_Xf)(p)=\lim_{t\rightarrow 0}(f(\phi^t(p))-f(p))/t$$—인데, 벡터장 글의 정리 6에서 integral flow $$\phi^t$$가 존재한다는 것을 보였으므로 이 정의가 well-defined된다는 것이 이해된다. 벡터장 글에서 $$X_pf=(f\circ\gamma)'(0)$$로 방향미분을 정의했는데, 리 미분은 이 "한 점에서의 미분"을 "전체 manifold 위의 장(field)으로 확장한 것"이라는 느낌이 든다. $$\mathcal{L}_Xf=X(f)$$라는 명제 4의 첫 번째 결론이 "리 미분 = 방향미분"이라는 것을 확인해주는 것이면서도, 리 미분이 왜 필요한지에 대한 질문을 던진다—함수의 경우 방향미분과 같으므로, 리 미분의 진짜 가치는 벡터장과 미분형식에서 드러난다.

벡터장의 리 미분 정의 2—$$(\mathcal{L}_XY)_p=\lim_{t\rightarrow 0}((d\phi^{-t})_{\phi^t(p)}(Y_{\phi^t(p)})-Y_p)/t$$—에서 마주치는 문제—"$$Y_{\phi^t(p)}$$는 $$T_{\phi^t(p)}M$$의 원소이고 $$Y_p$$는 $$T_pM$$의 원소이므로 직접 뺄 수 없다"—가 이 글의 핵심 동기이다. 미분사상 글에서 $$dF_p:T_pM\rightarrow T_{F(p)}N$$을 정의했는데, $$F=\phi^t$$인 경우 $$d\phi^t:T_pM\rightarrow T_{\phi^t(p)}M$$가 isomorphism이고 그 역함수가 $$d\phi^{-t}$$라는 것이 벡터장 글의 정리 6에서 나온다. $$Y_{\phi^t(p)}$$를 $$d\phi^{-t}$$로 $$T_pM$$으로 끌어온 뒤 빼는 이 구성—"다른 tangent space의 벡터를 같은 공간으로 옮겨서 비교한다"—은 접다발 글에서 vector bundle의 국소적 trivialization을 정의한 것과 같은 아이디어인데, 여기서는 "flow가 제공하는 전역적 diffeomorphism"을 사용한다는 것이 차이이다.

Lie bracket—$$[X,Y]f=X(Yf)-Y(Xf)$$—의 정의 동기가 깔끔하다. $$\mathfrak{X}(M)$$을 $$C^\infty(M)$$-module로 보면 $$XY$$도 벡터장이 될 것 같지만, $$XY(fg)$$를 계산하면 $$(Xf)(Yg)+(Xg)(Yf)$$라는 Leibniz 법칙을 위반하는 항이 남는다. $$YX(fg)$$에서도 같은 항이 나오므로 $$XY-YX$$를 취하면 이 위반항이 상쇄된다는 것이 Lie bracket의 존재 이유인데, 벡터장 글에서 $$\mathfrak{X}(M)$$이 $$C^\infty(M)$$-module이라는 관점을 도입한 것이 여기서 payoff되는 구조이다. $$\mathfrak{X}(M)$$이 $$C^\infty(M)$$-module이면서 동시에 Lie bracket에 대하여 Lie algebra를 이룬다는 것이, "함수로 스칼라곱하는" 연산과 "브래킷으로 비가환적 결합을 측정하는" 연산이 공존한다는 것인데, 이후 Lie group의 Lie algebra에서 이 구조가 핵심적으로 사용될 것이라는 예감이 든다.

F-relatedness—$$dF_p(X_p)=Y_{F(p)}$$—는 "diffeomorphism이 아닌 $$F$$를 통해 벡터장을 옮기는" 문제에 대한 해법이다. $$F$$가 전사도 단사도 아니면 $$X$$를 $$F$$로 pushforward할 수 없지만, 이미 $$N$$ 위에 있는 $$Y$$가 $$X$$와 $$F$$-related인지만 확인하면 되는 것이 명제 7의 $$X(f\circ F)=(Yf)\circ F$$ 조건인데, 미분사상 글에서 $$dF_p$$의 정의가 $$(dF_p(v))(g)=v(g\circ F)$$였으므로 이 조건이 $$dF_p(X_p)=Y_{F(p)}$$와 동치라는 것이 명확하다. 명제 9—$$F$$-related인 쌍은 Lie bracket도 보존—는 $$F$$-relatedness가 "벡터장 사이의 대응"으로서 대수적 구조를 유지한다는 것을 보여주는데, 증명에서 $$X_i(f\circ F)=(Y_if)\circ F$$를 반복 적용하는 부분이 깔끔하다.

명제 4의 나머지 결론들—(3) $$\mathcal{L}_X$$가 $$\Omega^\ast(M)$$의 derivation이고 $$d$$와 commute, (4) $$\mathcal{L}_X=\iota_X\circ d+d\circ\iota_X$$(Cartan's formula), (5) $$\mathcal{L}_X$$의 Leibniz 법칙, (6) $$d\omega$$의 coordinate-free 공식—은 이 글의 기술적 핵심이다. 미분형식 글에서 $$d$$가 anti-derivation이고 $$\iota_X$$가 anti-derivation이라는 것을 보였는데, 두 anti-derivation의 합성 $$\iota_X\circ d+d\circ\iota_X$$가 derivation이 된다는 것이 Cartan's formula의 대수적 구조이다. $$d$$와 $$\mathcal{L}_X$$가 commute한다는 것은 $$\mathcal{L}_X$$가 de Rham complex의 cochain map이라는 것인데, 미분형식 글에서 $$F^\ast$$가 $$d$$와 commute한다는 것(명제 4.3)과 같은 맥락의 결과이다. 다만 Cartan's formula의 증명이 생략되어 있어서, $$\iota_X\circ d+d\circ\iota_X$$가 왜 정의 1~3과 동치인지—어떤 논증으로 이 공식을 유도하는지—를 확인할 수 없는 것이 아쉽다.

좋은 점: (1) 벡터장의 리 미분에서 "다른 tangent space의 벡터를 직접 뺄 수 없다"는 문제 제기와 $$d\phi^{-t}$$로 끌어오는 해결책이, 추상적 정의의 동기를 구체적으로 보여준다. (2) Lie bracket의 정의 동기—$$XY$$의 Leibniz 법칙 위반을 소거—가 $$\mathfrak{X}(M)$$의 대수적 구조와 자연스럽게 연결된다. (3) $$F$$-relatedness와 Lie bracket의 보존(명제 9)이 diffeomorphism과 벡터장의 관계를 보여주는 좋은 예시이다.

아쉬운 점: (1) Cartan's formula(명제 4.4)의 증명이 없어서, $$\mathcal{L}_X=\iota_X d+d\iota_X$$가 왜 성립하는지에 대한 핵심 논증을 확인할 수 없다—이 공식이 이 글에서 가장 중요한 결과 중 하나인데 증명이 없다는 것이 무게감을 떨어뜨린다. (2) Lie bracket의 구체적 예시—어떤 두 벡터장의 bracket을 계산하면 어떻게 되는지—가 없어서, $$[X,Y]$$가 실제로 어떤 함수인지 체감하기 어렵다. (3) $$F$$-relatedness의 동기가 "diffeomorphism이 아닌 경우 pushforward가 불가능하므로"라고만 되어 있는데, $$F$$가 diffeomorphism이 아닌 경우에 $$F$$-related $$Y$$가 존재하는 구체적 예시가 없어서 이 개념이 언제 유용한지에 대한 직관이 부족하다.

⚠️ 정의 없이 사용: `derivation` (검색해도 없음 — $$\mathcal{L}_X$$가 $$\Omega^\ast(M)$$의 derivation이라고 하나, 이 용어 자체가 prior 노트에서 standalone으로 도입된 적 없음)
⚠️ 정의 없이 사용: `pushforward` (검색해도 없음 — $$d\phi^{-t}$$를 통해 벡터장을 옮기는 연산을 가리키지만, 이 용어 자체가 prior 노트에서 도입된 적 없음)

## [미분 아이디얼](/ko/math/manifolds/differential_ideal)

이 글은 distribution을 소멸시키는 미분형식들의 모임—$$\mathcal{I}(\mathcal{D})$$—을 아이디얼로 정의하고, 그 아이디얼이 외미분 $$d$$에 대해 닫혀 있는 조건(differential ideal)이 Frobenius 정리의 involutivity 조건과 동치임을 보여준다. 출발점인 정의 1의 annihilate—$$\omega_p(v_1,\ldots,v_l)=0$$ for all $$v_i\in\mathcal{D}(p)$$—는 여접공간 글에서 $$\mathfrak{m}_p/\mathfrak{m}_p^2$$의 원소가 접벡터를 소멸시키는 것과 같은 패턴인데, distribution의 각 점에서의 부분공간을 소멸시키는 형식들을 묶어서 하나의 대수적 대상으로 보는 관점이 인상적이다. $$\mathcal{I}(\mathcal{D})$$가 $$\Omega^\ast(M)$$의 ideal이라는 명제 2의 첫째 주장은 정의로부터 자명하지만, 둘째 주장—국소적으로 $$m-k$$개의 1-form들로 생성된다—이 이 글의 구조적 핵심이다. $$p$$ 근방에서 $$\mathcal{D}$$를 생성하는 벡터장들 $$X_{m-k+1},\ldots,X_m$$에 $$X_1,\ldots,X_{m-k}$$를 추가해 local basis를 만든 뒤 dual 1-form들을 취하면, $$\omega_1,\ldots,\omega_{m-k}$$이 정확히 $$\mathcal{D}$$를 소멸시키는 것—$$\omega_i(X_j)=\delta_{ij}$$이므로—이 distribution의 "dual 표현"이다.

정의 3의 differential ideal—$$\mathcal{I}$$가 $$d$$에 대해 닫혀 있는 것—은 $$\Omega^\ast(M)$$이 dg-algebra라는 관찰에서 자연스럽게 나오는 조건인데, 미분형식 글에서 $$d^2=0$$이라는 것과 de Rham complex의 구조를 떠올리면 "ideal이 $$d$$와 호환된다"는 것이 cohomology를 다룰 때 필수적인 조건이라는 예감이 든다. 명제 4—$$\mathcal{D}$$가 involutive $$\iff$$ $$\mathcal{I}(\mathcal{D})$$가 differential ideal—는 Distribution 글의 Frobenius 정리(정리 3)를 미분형식의 언어로 번역한 것인데, $$[X,Y]\in\mathcal{D}$$라는 벡터장 조건이 $$d\omega\in\mathcal{I}$$라는 형식 조건으로 바뀐다는 것이 이 글의 핵심 통찰이다. 증명이 생략되어 있지만, $$X,Y\in\mathcal{D}$$일 때 $$d\omega(X,Y)=X(\omega(Y))-Y(\omega(X))-\omega([X,Y])$$라는 공식—미분형식 글에서 언급된 coordinate-free 공식—에서 $$\omega(X)=\omega(Y)=0$$이므로 $$d\omega(X,Y)=-\omega([X,Y])$$가 되고, 이것이 0이 되려면 $$[X,Y]\in\mathcal{D}$$여야 한다는 것이 "왜 involutivity가 differential ideal 조건과 동치인지"를 보여줄 것이라는 예감이 든다.

정의 5의 integral manifold—$$(d\Phi)^\ast(\omega)\equiv 0$$—는 Distribution 글의 integral manifold 정의($$T_xS=\mathcal{D}(x)$$)를 pullback의 언어로 바꾼 것인데, 미분형식 글에서 pullback의 정의가 $$(F^\ast\omega)_p=\bigwedge(dF_p^\ast)(\omega_{F(p)})$$였으므로 $$(d\Phi)^\ast(\omega)\equiv 0$$은 "형식 $$\omega$$를 submanifold로 끌어당기면 0이 된다"는 것이고, 이는 $$\omega$$가 $$\mathcal{D}$$를 소멸시키므로 $$T_xS=\mathcal{D}(x)$$인 곳에서 당연히 0이 된다는 것이 이해된다. 정리 6—$$m-k$$개의 independent 1-form들로 생성된 differential ideal의 integral manifold가 존재하고 $$k$$차원—는 Distribution 글의 Frobenius 정리와 같은 결론인데, "벡터장 언어 ↔ 미분형식 언어"의 번환이 이 글 전체를 관통한다.

정리 7은 이 글에서 가장 흥미로운 부분이다. $$\graph(f)$$가 ideal $$\mathcal{I}$$의 integral manifold라는 (1)번 주장—$$(d(f\circ\pi_1))^\ast(\omega_i)-(d\pi_2)^\ast(\omega_i)$$로 생성되는 ideal의 integral manifold—의 증명에서 $$(d\iota)^\ast(\mu_i)=(df)^\ast(\omega_i)-(df)^\ast(\omega_i)=0$$이라는 계산이 깔끔한데, $$\pi_1\circ\iota=f$$와 $$\pi_2\circ\iota=\id$$라는 관계가 inclusion map과 projection의 합성으로 정리되는 것이 elegant하다. (2)번—differential ideal의 integral manifold가 graph인 것—은 Frobenius 정리를 "graph의 존재성"으로 해석할 수 있다는 것인데, 리 이론 카테고리에서 Lie group과 Lie algebra의 관계를 탐구할 때 이 결과가 사용된다고 명시되어 있어서 "이 글이 이후로 연결되는 지점"을 보여준다.

좋은 점: (1) distribution의 "dual 표현"—$$\mathcal{I}(\mathcal{D})$$의 국소적 생성원이 $$m-k$$개의 1-form—이 involutivity를 형식의 언어로 번환하는 기반이 되는 것이 자연스럽다. (2) 명제 4가 Distribution 글의 Frobenius 정리와 정확히 같은 결과를 다른 언어로 보여주는 것이, "벡터장과 미분형식이 동일한 기하학을 다른 각도에서 본다"는 것을 체감하게 한다. (3) 정리 7의 graph 해석이 abstract한 Frobenius 정리에 concrete한 기하학적 의미를 부여하는 것이 좋다.

아쉬운 점: (1) 명제 4의 증명이 없어서, $$d\omega(X,Y)=-\omega([X,Y])$$라는 공식이 실제로 사용되는지—아니면 다른 논증이 필요한지—확인할 수 없다. (2) $$\mathcal{I}(\mathcal{D})$$의 ideal 성질(명제 2.1)이 "정의로부터 자명하다"고만 되어 있는데, $$\omega_1,\omega_2\in\mathcal{I}$$일 때 $$\omega_1\wedge\omega_2\in\mathcal{I}$$라는 것—exterior product가 소멸 조건을 보존한다는 것—이 정말 자명한지 확인이 필요하다. (3) 정리 7의 증명에서 "$$d\pi_1$$을 $$I_q$$로 제한한 것이 전단사함수임을 보이면 된다"고만 되어 있는데, 이 주장의 핵심 논증—왜 $$d\pi_1\big|_{I_q}$$가 injective인지, 그리고 왜 surjective인지—이 생략되어 있어서 graph의 존재성이 어떻게 나오는지 확인할 수 없다.

## [Distribution](/ko/math/manifolds/distribution)

이 글은 벡터장의 1차원 distribution으로의 확장—각 점 $$p$$에서 $$T_pM$$의 $$k$$차원 부분공간을 대응시키는 것—에서 출발해서, Frobenius 정리로 integrability 조건을 involutivity로 특성짓는다. 정의 1의 $$k$$차원 distribution—$$p\mapsto\mathcal{D}(p)\subseteq T_pM$$이 $$k$$차원 부분공간—은 벡터장 글에서 $$p\mapsto\span(X_p)$$로 1차원 distribution을 정의한 것을 일반화한 것인데, "각 점에서 tangent space의 부분공간을 고르는 함수"라는 관점이 접다발의 subbundle로서의 해석을 자연스럽게 떠올리게 한다. smoothness 조건—각 점 근방에서 $$C^\infty$$ 벡터장들 $$X_1,\ldots,X_k$$로 span할 수 있는 것—은 vector bundle의 local trivialization과 같은 패턴인데, distribution이 "접다발의 subbundle"이라는 관점이 이 조건을 "국소적으로 constant rank인 section들의 span"으로 읽게 한다.

integral manifold의 정의—$$T_xS=\mathcal{D}(x)$$를 만족하는 submanifold $$S$$—는 "distribution이 실제로 어떤 submanifold의 tangent space로 실현되는가"라는 질문을 formalize한 것인데, 부분다양체 글에서 embedded submanifold의 tangent space를 다뤘던 것과 연결된다. integrable distribution—"각 점마다 integral manifold가 존재"—은 이 실현이 전역적으로 가능한 경우인데, 1차원 distribution은 항상 integrable하다는 관찰(벡터장의 integral flow가 곧 integral manifold)이 출발점이다. $$k\geq 2$$에서 integrability가 non-trivial해지는 것이 이 글의 핵심 동기이다.

Frobenius 정리(정리 3)—integrable $$\iff$$ involutive($$X,Y\in\mathcal{D}$$이면 $$[X,Y]\in\mathcal{D}$$)—는 이 글의 구조적 핵심이다. 보조정리 4의 "integrable $$\Rightarrow$$ involutive" 방향 증명이 깔끔한데, integral submanifold $$\Phi:S\rightarrow M$$ 위에서 $$X,Y$$와 $$\Phi$$-related인 $$\tilde{X},\tilde{Y}$$를 찾고, 리 미분 글의 명제 9($$F$$-relatedness가 Lie bracket을 보존)를 적용하면 $$[X,Y]_p=d\Phi_s([\tilde{X},\tilde{Y}]_s)\in\mathcal{D}(p)$$가 된다는 논증이 "리 미분 글의 결과를 여기서 사용하는 첫 번째 실례"이다. $$\Phi$$-relatedness를 통해 "submanifold 위의 벡터장"과 "ambient manifold 위의 벡터장"을 연결하는 이 아이디어는, 부분다양체 글에서 inclusion map의 differential을 다뤘던 것과 같은 맥락이다.

보조정리 5—$$X_p\neq 0$$인 벡터장 $$X$$에 대하여 $$X\big|_U=\partial/\partial x^1$$이 되는 coordinate system을 찾을 수 있다는 것—는 "벡터장을 coordinate basis로 align한다"는 구성인데, 벡터장 글의 integral flow $$\phi^t$$를 사용하여 coordinate map을 만드는 것이 핵심이다. $$\sigma(t,a^2,\ldots,a^d)=\phi^t(\tau^{-1}(0,a^2,\ldots,a^d))$$로 정의한 map이 원점에서 nonsingular이라는 것은 $$d\sigma(\partial/\partial r^1\big|_0)=X_p\neq 0$$과 $$d\sigma(\partial/\partial r^i\big|_0)=\partial/\partial y^i\big|_p$$로부터 나오는데, 역함수 정리를 적용하는 이 패턴이 음함수 정리 글에서 level set을 submanifold로 만들었던 것과 구조적으로 같다.

정리 3의 "involutive $$\Rightarrow$$ integrable" 방향 증명—$$k$$에 대한 귀납법—이 이 글에서 가장 기술적인 부분이다. $$X_1$$을 보조정리 5로 align한 뒤, $$Y_i=X_i-(X_i(y^1))X_1$$로 $$y^1$$ 성분을 제거해서 slice $$S:\{y^1=0\}$$ 위의 벡터장 $$Z_i=Y_i\big|_S$$를 만드는 것이 핵심 아이디어인데, $$Y_i(y^1)=0$$이므로 $$Z_i$$가 $$S$$의 tangent space에 속한다는 것이 involutivity 조건의 직접적인 결과이다. $$[Y_i,Y_j]y^1=0$$이라는 계산—$$Y_i(y^1)=0$$ forall $$i$$이므로—이 "왜 involutive이면 integrable한지"를 한 줄로 보여주는 핵심이다. 귀납 가정을 $$S$$ 위의 $$k-1$$차원 involutive distribution에 적용하고, $$x^j=w^j\circ\pi$$로 coordinate를 확장하는 마지막 단계—$$Y_i(x^{k+j})=0$$을 ODE로 푸는 것—이 "귀납의 출발점 $$k=1$$은 벡터장의 integral flow로 이미 알고 있다"는 것과 맞물린다.

좋은 점: (1) 정의 1의 smoothness 조건이 vector bundle의 local trivialization과 같은 패턴이라는 것이 distribution을 "접다발의 subbundle"로 이해하게 한다. (2) 보조정리 4의 증명이 $$\Phi$$-relatedness와 리 미분 글의 명제 9를 사용해서, 이전 글들의 결과가 여기서 어떻게 쓰이는지를 명확히 보여준다. (3) 귀납 증명의 구조—$$X_1$$을 align → $$y^1$$ 성분 제거 → slice 위의 distribution → 귀납 적용—가 "하나의 벡터장을 coordinate로 흡수하고 나머지를 reduction"하는 패턴을 보여주는 것이 깔끔하다.

아쉬운 점: (1) involutive의 기하학적 의미—"분포가 "서로 꼬이지 않는다"는 것"—에 대한 직관적 설명이나 그림이 없어서, $$[X,Y]\in\mathcal{D}$$라는 대수적 조건이 실제로 어떤 기하학적 현상을 포착하는지 체감하기 어렵다. (2) 보조정리 5의 증명에서 $$\sigma$$의 nonsingularity를 보이는 부분이 압축되어 있는데, $$d\sigma(\partial/\partial r^i\big|_0)=\partial/\partial y^i\big|_p$$라는 공식이 어떻게 나오는지—$$\sigma$$의 정의와 chain rule의 적용—을 확인하기 어렵다. (3) Frobenius 정리의 "좌표계를 잘 택하면 slice로 된다"는 결론이 음함수 정리 글의 submersion level set theorem과 구조적으로 유사한데, 이 두 정리의 관계에 대한 논의가 없다.

## [향](/ko/math/manifolds/orientation)

이 글은 벡터공간의 기저 순서에서 출발해서, manifold의 orientation을 최고차 미분형식으로 정의하고 orientability의 동치 조건을 다룬다. 출발점—$$\mathbb{R}^3$$에서 $$x_3\cdot(x_1\times x_2)=\det[x_1\;x_2\;x_3]$$—은 미적분학에서 배운 "외적과 행렬식의 관계"인데, 이 관찰을 $$\mathbb{R}^m$$으로 확장하면 basis의 순서가 행렬식의 부호로 판별된다는 것이 이 글의 출발 아이디어이다. 다중선형대수학 카테고리에서 $$\bigwedge^n(V)$$가 1차원이라는 것을 보였는데, 여기서 $$\bigwedge^n(L)$$을 determinant map이라고 부르는 것이—$$n$$차원 벡터공간의 자기 자신에 대한 선형사상이 $$\bigwedge^n$$ 위에서 스칼라배가 된다는 관찰이—행렬식의 "본질"을 exterior algebra로 재해석하는 것이라는 느낌이 든다.

정의 1의 orientability—$$\bigwedge^m(M)\setminus\{0\}$$이 두 component를 가지는 것—는 미분형식 글에서 정의한 exterior bundle $$\bigwedge^m(M)$$을 직접 사용하는 것이다. $$\bigwedge^m(M)$$이 line bundle이라는 것(접다발 글의 smooth functor 프레임워크에서 나온다)이 이 정의의 기술적 전제인데, line bundle의 zero section을 제외한 부분이 두 component로 나뉘는 것이 "양의 방향과 음의 방향"이라는 직관을 formalize한다는 것이 인상적이다. $$\bigwedge^m(M)$$이 아니라 $$\bigwedge^m(T^\ast M)$$을 쓰는 것—여접다발의 최고차 exterior power—이 미분형식 글에서 $$\Omega^m(M)=\Gamma(\bigwedge^m(T^\ast M))$$로 정의한 것과 연결되는데, orientation을 "최고차 미분형식의 부호"로 보는 관점이 여기서 나온다.

명제 2의 세 동치 조건—(1) orientable, (2) 양의 Jacobian을 갖는 coordinate atlas의 존재, (3) non-vanishing $$m$$-form의 존재—은 이 글의 구조적 핵심이다. (2)는 "좌표계 전환에서 orientation이 보존된다"는 것이고, (3)은 "전역적으로 0이 아닌 최고차 형식이 존재한다"는 것인데, 두 조건이 (1)과 동치라는 것이 orientation을 세 가지 각도—위상적(atlas), 대수적(form), 기하학적(component)—에서 볼 수 있게 해준다. 미분형식 글에서 $$\Omega^m(M)$$의 section을 정의했는데, 그 section이 전역적으로 non-vanishing할 수 있는지가 orientability의 조건이라는 것이 "미분형식이 manifold의 전역적 성질을 감지한다"는 첫 번째 실례이다.

예시 3의 Lie group의 orientability—left-invariant form들의 wedge가 non-vanishing $$n$$-form을 이룬다는 것—은 리 미분 글에서 $$\mathcal{L}_X$$를 다룰 때 left-invariant 벡터장을 사용했던 것과 연결된다. $$\Omega^\ast_\text{l.inv}(G)$$의 basis $$\omega_1,\ldots,\omega_n$$의 wedge가 non-vanishing이라는 것은 "left translation이 orientation을 보존한다"는 것인데, Lie group의 대수적 구조가 기하학적 성질(orientability)을 보장한다는 것이 인상적이다. 다만 이 예시가 "왜 left-invariant form의 basis가 존재하는지"에 대한 설명 없이 사용되고 있어서, Lie group의 구조에 대한 사전 지식이 필요하다는 것이 느껴진다.

이 글은 전체 미분다양체 카테고리에서 "전역적 성질"을 다루는 첫 번째 글이다. 앞서 다룬 글들—미분구조, 접공간, 미분형식 등—이 모두 "국소적" 정의와 성질이었다면, orientation은 atlas 전체, 전역적 미분형식의 존재 같은 "전역적" 조건을 다루는데, 이후 integration에서 이 orientation이 왜 필수적인지—방향이 없으면 최고차 형식의 적분이 well-defined되지 않는다—가 밝혀질 것이라는 예감이 든다.

좋은 점: (1) $$\mathbb{R}^3$$의 외적에서 출발해서 행렬식 → exterior algebra → manifold orientation으로 이어지는 흐름이 "구체적 직관 → 대수적 일반화 → 기하학적 적용"으로 자연스럽다. (2) 명제 2의 세 동치 조건이 orientation을 세 가지 각도에서 보여주는 것이, 이 개념의 다면적 성격을 체감하게 한다. (3) Lie group의 orientability 예시가 대수적 구조와 기하학적 성질의 연결을 보여주는 좋은 첫 사례이다.

아쉬운 점: (1) 명제 2의 증명이 빈 details 태그로 되어 있어서, 세 조건의 동치성을 확인할 수 없다—특히 (2)와 (3)의 동치성이 non-vanishing form으로부터 양의 Jacobian atlas를 구성하는 과정을 보여줘야 할 것 같은데, 그 논증이 없다. (2) $$\bigwedge^m(M)\setminus\{0\}$$이 두 component를 가지는 것의 직관적 의미—"양의 orientation과 음의 orientation"이 왜 정확히 두 개인지—에 대한 설명이 없어서, 정의가 다소 갑작스럽다. (3) connected manifold를 가정하고 있는데, 비연결 manifold의 orientation은 각 connected component마다 따로 정의해야 한다는 점이 언급되지 않았다.

⚠️ 정의 없이 사용: `left-invariant` (검색해도 없음 — $$\Omega^\ast_\text{l.inv}(G)$$로 사용되지만 left-invariant form의 정의가 prior 노트에서 도입된 적 없음)

## [적분](/ko/math/manifolds/integration)

이 글은 제목과 "이제 우리는 적분을 정의한다"라는 한 줄만 존재하고, 실제 내용이 없다. 미분다양체 카테고리의 마지막 글(orientation, weight 19)에서 "이후 integration에서 이 orientation이 왜 필수적인지—방향이 없으면 최고차 형식의 적분이 well-defined되지 않는다—가 밝혀질 것"이라고 예고했으므로, $$m$$-form의 적분을 orientation과 연결하여 정의하는 글이 될 것이라는 기대가 있었는데, 그 기대가 충족되지 않은 것이 아쉽다. manifold 위의 적분이라면 $$\omega\in\Omega^m_c(M)$$를 oriented chart를 통해 $$\mathbb{R}^m$$으로 pullback한 뒤 유클리드 적분을 취하는 구성—$$\int_M\omega=\sum_\alpha\int_{\varphi_\alpha(U_\alpha)}(\varphi_\alpha^{-1})^\ast\omega$$—과 partition of unity를 사용한 전역적 정의, 그리고 그 정의가 chart 선택과 무관하다는 것을 보이는 논증이 필요할 텐데, 이 모든 것이 빠져 있다. Stokes' 정리—$$\int_M d\omega=\int_{\partial M}\omega$$—가 이 카테고리의 최종 payoff가 될 것이라는 예감마저 드는데, 그것 역시 이 글에서는 다뤄지지 않는다.

orientation 글에서 $$\bigwedge^m(M)\setminus\{0\}$$이 두 component를 가진다는 정의가 적분과 직접 연결된다는 것을 느낀다: 양의 component에 속하는 $$m$$-form만 적분하면 부호가 well-defined된다는 것이 orientation의 존재 이유 중 핵심이기 때문이다. 벡터장의 integral flow, distribution의 integral manifold 등 "integral"이라는 단어가 이미 여러 맥락에서 나왔는데, 적분(정적분)으로서의 integration은 그동안 쌓아온 미분형식과 orientation의 구체적 payoff라는 위치에 있다. 이 글이 stub으로 남아 있어서 미분다양체 카테고리 전체의 완결감이 떨어진다는 것이 가장 큰 아쉬움이다.

좋은 점: (1) 없다. 한 줄짜리 stub이므로 평가할 내용 자체가 없다.

아쉬운 점: (1) 미분다양체 카테고리의 마지막 글이면서 가장 기대가 컸던 주제(적분)인데, 실제 내용이 전혀 없어서 카테고리가 미완성으로 끝난다. (2) orientation 글의 마지막 단락에서 "이후 integration에서 밝혀질 것"이라고 예고한 내용이 지켜지지 않았다. (3) $$m$$-form의 적분 정의, chart 무관성, Stokes' 정리 등 미분기하학의 핵심 결과 중 하나가 이 카테고리에서 빠져 있다.

## 카테고리 회고

미분다양체 카테고리는 "국소적으로 $$\mathbb{R}^n$$과 닮은 공간 위에 미분구조를 부여한다"는 하나의 아이디어에서 출발해서, 접공간·미분형식·벡터장·distribution이라는 일련의 도구를 쌓아올린 뒤 Frobenius 정리와 orientation이라는 전역적 결과까지 도달하는 구조인데, 각 글이 이전 글의 결과를 직접 사용하는 "계단식" 전개가 인상적이다. 대수적 위상수학 카테고리에서 배운 topological manifold가 미분구조를 올리는 "바닥" 역할을 하고, 선형대수학 카테고리의 dual space·tensor product·exterior algebra가 접공간과 미분형식의 대수적 언어를 제공하며, 대수적 구조 카테고리의 ring·ideal 개념이 $$\mathcal{C}^\infty_p$$의 stalk 구조로 구체화된다는 것이 이 카테고리의 가장 큰 즐거움이었다. 가장 막혔던 지점은 접다발의 smooth functor 프레임워크—하나의 원리로 모든 파생 다발을 커버한다는 것—가 추상적으로 느껴졌던 것인데, 미분형식 글에서 tensor bundle과 exterior bundle이 실제로 이 프레임워크의 적용이라는 것을 보고 나서야 "왜 이 프레임워크를 도입했는지"가 이해되었다.
