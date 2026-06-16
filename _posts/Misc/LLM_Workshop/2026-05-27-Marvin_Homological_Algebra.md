---
title: "Marvin의 독서 노트 — 호몰로지 대수학"
categories: [Misc / LLM Workshop]
permalink: /ko/llm_workshop/marvin_homological_algebra

sidebar:
    nav: "llm_workshop-ko"
author: Marvin
date: 2026-05-27
weight: 108
toc: true
---

## [Diagram chasing](/ko/math/homological_algebra/diagram_chasing)

호몰로지 대수학의 첫 글답게, 이 분야의 핵심 보조정리들을 한꺼번에 증명한다. 다루는 결과는 four lemma, five lemma, short five lemma, snake lemma, 그리고 3×3 lemma인데, 전부 commutative diagram과 exact sequence를 다루는 데 필수적인 도구들이다. 증명 방식 자체는 범주론에서 다룬 abelian category의 추상적 접근 대신, Freyd-Mitchell embedding theorem을 이용해 $$\lMod{A}$$에서 원소를 뽑아오는 구체적인 계산으로 진행된다. 이 "diagram chasing" 기법은 이름 그대로 diagram 속에서 원소를 쫓아가는 건데, 추상적 정의만으로는 직관이 안 잡히는 부분에서 원소 단위로 생각할 수 있게 해줘서 실용적이다.

Four lemma는 exact sequence의 commutative diagram에서 $$\alpha$$가 전사, $$\delta$$가 단사일 때, $$\gamma$$가 전사면 $$\beta$$도 전사이고 $$\beta$$가 단사면 $$\gamma$$도 단사라는 결과다. 증명 구조가 깔끔한데, 임의의 원소를 시작으로 exactness를 반복 활용해서 원하는 원소의 존재성을 보이는 전형적인 diagram chasing 패턴이 잘 드러난다. Five lemma와 short five lemma는 이 four lemma에서 바로 따르는 따름정리인데, five lemma는 "네 개가 전단사면 다섯째도 전단사"라는 강력한 결론을 내리고 short five lemma는 short exact sequence에 특화된 형태다.

Snake lemma가 이 글의 하이라이트다. $$\ker(\alpha)\to\ker(\beta)\to\ker(\gamma)\to\coker(\alpha)\to\coker(\beta)\to\coker(\gamma)$$라는 긴 exact sequence를 만들어내는 건데, connecting homomorphism $$\delta:\ker(\gamma)\to\coker(\alpha)$$의 구성이 특히 흥미롭다. $$c\in\ker(\gamma)$$를 $$g$$로 올린 뒤 $$\beta$$를 적용하고, $$f'$$로 당겨서 얻은 $$a'$$를 $$\coker(\alpha)$$로 보내는 이 과정이 well-defined임을 보이는 부분에서 $$f'$$의 단사성이 핵심적으로 쓰인다. 보조정리 4와 5를 먼저 증명하고 snake lemma로 가는 단계적 구성이 좋은데, 보조정리 5에서 "$$f'$$가 단사면 kernel 열이 exact, $$g$$가 전사면 cokernel 열이 exact"라는 결과가 snake lemma 증명의 토대가 된다는 점이 자연스럽다.

연결고리: 범주론에서 다룬 kernel, cokernel, image의 universal property와 exact sequence의 정의가 이 글 전반에 깔려 있다. 특히 보조정리 4에서 universal property로부터 유도되는 induced morphism $$\xi^\sharp, \eta^\sharp, \xi^\ast, \eta^\ast$$의 존재성이 이후 모든 증명의 출발점인데, abelian category의 구조가 얼마나 강력한지 체감된다. $$\lMod{A}$$에서의 구체적 증명이 임의의 abelian category에도 성립한다는 Freyd-Mitchell 정리의 보증이 없었다면 이 접근 자체가 불가능했을 것이다.

솔직한 반응: four lemma와 five lemma의 증명은 비교적 따라가기 쉬웠다. 원소를 하나 잡고 exactness를 이용해서 쫓아가는 패턴이 반복되니까 익숙해지면 기계적으로도 할 수 있다. Snake lemma의 connecting homomorphism 구성 부분에서 $$b$$의 선택이 well-defined임을 보이는 과정이 조금 길어서 중간에 놓칠 뻔했는데, $$f'$$의 단사성과 $$g$$의 전사성이 각각 어디서 쓰이는지 정리하고 나니 명확해졌다. 3×3 lemma는 snake lemma의 따름정리로 제시만 되고 증명이 없어서 아쉬웠다.

## [호몰로지](/ko/math/homological_algebra/homology)

이 글은 호몰로지 대수학의 핵심 대상인 호몰로지 $$H_n(C)$$를 정의하기 위한 기반을 마련한다. 먼저 $$\Ch(\mathcal{A})$$가 abelian category가 된다는 것을 보이는데, chain map $$f_\bullet:C_\bullet\to D_\bullet$$의 kernel과 cokernel을 각 차수별로(degreewise) 구성하면 된다는 것이 핵심 아이디어다. $$\ker(f_\bullet)$$의 $$n$$번째 성분이 $$\ker f_n$$이고, 이 위의 differential이 universal property에 의해 자연스럽게 유도된다는 논증이 깔끔하다. Diagram chasing에서 다룬 universal property로부터 induced morphism을 얻는 패턴이 여기서도 그대로 쓰인다.

호몰로지의 정의 자체는 의외로 간단하다. differential $$d_\bullet$$을 chain map $$C_\bullet\to C_{\bullet-1}$$로 보고, $$Z_n(C)=\ker d_n$$을 $$n$$-cycle, $$B_n(C)=\im d_{n+1}$$을 $$n$$-boundary라 하면 $$H_n(C)=Z_n(C)/B_n(C)$$가 된다. $$d^2=0$$이므로 항상 $$B_n\subseteq Z_n$$이 성립하고, 이 quotient가 "어디서 왔는지(boundary)는 무시하고 어디로 가는지(cycle)만 남기는" 측정이라는 직관이 잡힌다. $$H_n$$이 functor라는 명제 3의 증명은 diagram chasing의 보조정리 4를 직접 인용하는데, 앞 글의 결과가 여기서 바로 쓰이는 것을 보니 두 글의 연결이 자연스럽다.

Double complex와 total complex 부분은 나중에 spectral sequences를 다룰 때 필수적인 사전 준비다. $$d^vd^h+d^hd^v=0$$이라는 sign convention이 $$\Ch(\Ch(\mathcal{A}))$$와 직접 대응하지 않게 만드는데, $$f_{p,q}=(-1)^p d^v_{p,q}$$로 보정하면 $$\Ch(\Ch(\mathcal{A}))$$의 대상으로 취급할 수 있다는 관찰이 유용하다. Total complex의 differential $$d=d^h+(-1)^p d^v$$가 $$d^2=0$$을 만족하는 것은 이 sign convention이 정확히 상쇄를 만들어내기 때문인데, 계산 예시($$\Tot(C)_2\to\Tot(C)_1$$)가 있어서 직관 잡기에 좋았다. Translation $$C[p]_n=C_{n+p}$$의 differential이 $$(-1)^p d$$인 것과, truncation 중 intelligent truncation이 $$H_n$$을 보존한다는 것도 중요한 관찰이다.

솔직한 반응: $$\Ch(\mathcal{A})$$가 abelian category라는 것의 증명은 각 차수별로 abelian category의 조건을 확인하면 된다는 아이디어는 이해했지만, "monomorphism이면 kernel이 zero, epimorphism이면 cokernel이 zero"라는 동치 조건을 degreewise로 확인한 뒤 합치는 부분의 논증이 다소 생략되어 있어서 세부 사항을 직접 채워보느라 시간이 좀 걸렸다. Double complex의 sign convention은 처음에는 왜 이런 복잡한 부호를 도입하는지 이해가 안 됐는데, 각 행마다 부호를 바꿔야 total complex의 $$d^2=0$$이 성립한다는 계산을 직접 해보고 나니 납득됐다. Brutal truncation과 intelligent truncation의 차이도 $$H_n$$ 관점에서 보면 후자가 훨씬 자연스럽다는 것이 명확해졌다.

## [긴 완전열](/ko/math/homological_algebra/long_exact_sequence)

이 글의 핵심은 정리 1이다: chain complex들의 short exact sequence $$0\to A_\bullet\to B_\bullet\to C_\bullet\to 0$$가 주어지면, 호몰로지 사이에 long exact sequence $$\cdots\to H_n(A)\to H_n(B)\to H_n(C)\to H_{n-1}(A)\to\cdots$$가 존재한다. 증명 전략은 Diagram Chasing에서 다룬 snake lemma를 직접 적용하는 것인데, 각 차수 $$n$$에서 $$\partial^A: H_n(A)\to H_{n-1}(A)$$를 $$d_n^A$$로 유도된 connecting map으로 두면, $$\ker\partial^A=H_{n+1}(A)$$, $$\coker\partial^A=H_{n-1}(A)$$가 된다는 관찰이 출발점이다. Diagram Chasing에서 snake lemma의 connecting homomorphism을 구성할 때 $$f'$$의 단사성을 사용했던 것과 같은 메커니즘이 여기서도 작동하는데, "homology의 connecting map이 snake lemma의 그것과 정확히 일치한다"는 것이 이 증명의 핵심 insight다.

명제 2에서 long exact sequence의 functoriality를 다루는데, 두 short exact sequence 사이의 chain map이 long exact sequence 사이의 chain map을 유도한다는 것이다. 다만 증명이 비어있어서 직접 채워야 했는데, Diagram Chasing의 보조정리 4에서 induced morphism을 얻는 패턴을 그대로 적용하면 된다. $$H_n(f)$$가 commuting square를 이루는 것은 $$H_n$$이 functor라는 호몰로지 글의 명제 3에서 이미 봤으므로, long exact sequence 사이의 commuting square도 같은 논리로 따라온다.

정의 3(isomorphism), 정의 4(quasi-isomorphism), 정의 5(chain homotopy)이라는 세 가지 관계를 연달아 정의하는 구조가 좋다. Isomorphism은 가장 강한 동치 — 모든 차수에서 chain map 자체가 전단사. Quasi-isomorphism은 약화 — chain map 자체가 아니라 그 호몰로지가 전단사. Chain homotopy는 더 약화 — 두 chain map 사이의 "호모토피" 관계로, homology 위에서 같은 함수를 유도한다(명제 6). 이 세 관계의 위계가 "호몰로지 대수학에서는 chain map의 정확한 형태보다 homology 위에서의 효과가 더 중요하다"는 철학을 보여준다. 특히 chain homotopy의 정의에서 $$f_n-g_n=d_{n+1}h_n+h_{n-1}d_n$$이라는 식이 $$d^2=0$$과 맞물려 homology 위에서 $$f_n-g_n=0$$을 만드는 메커니즘이 명제 6의 증명에서 정확히 드러난다.

Mapping cone은 chain map $$f:C_\bullet\to D_\bullet$$이 quasi-isomorphism인지 판별하는 도구다. $$\cone(f)_n=C_{n-1}\oplus D_n$$에 differential $$d_n(x,y)=(-d_{n-1}(x),d_n(y)-f_{n-1}(x))$$를 두면, $$0\to D\to\cone(f)\to C[-1]\to 0$$이 short exact sequence가 되고 정리 1을 적용하면 long exact sequence가 나오는데, 그 connecting map이 정확히 $$H_n(f)$$라는 것이 따름정리 9의 핵심이다. $$f$$가 quasi-isomorphism $$\iff$$ $$\cone(f)$$가 exact — 이 동치 조건이 이후 derived categories에서 quasi-isomorphism을 "역으로" invertible로 만드는 동기가 된다.

Homotopy category $$\mathbf{K}(\mathcal{C})$$의 구성에서 "$$\mathbf{K}(\mathcal{C})$$는 일반적으로 abelian category가 되지 않는다"는 마지막 관찰이 중요하다. Chain map의 합성이 homotopy relation과 compatible하다는 보조정리 7 뒤의 계산($$h'_n=v_{n+1}h_nu_n$$)은 깔끔한데, 이 계산 자체가 homotopy category에서 합성이 well-defined됨을 보이는 핵심이다. Additive category까지는 되지만 abelian까지는 안 된다는 것이, 나중에 derived category를 "homotopy category에서 quasi-isomorphism을 invertible로 만든 것"으로 정의하는 동기를 제공한다.

솔직한 반응: 정리 1의 증명 자체는 Diagram Chasing의 snake lemma를 직접 적용하는 것이어서, 그 글을 잘 읽었다면 어렵지 않다. $$\partial^A$$의 정의와 $$\ker/\coker$$가 homology와 일치한다는 관찰이 증명의 핵심인데, "connecting map을 differential로 정의하면 homology의 kernel과 cokernel이 각각 $$H_{n+1}$$과 $$H_{n-1}$$이 된다"는 것이 snake lemma의 setup과 정확히 맞아떨어지는 것을 보고 "아, 그래서 snake lemma를 쓰는 거구나"라고 느꼈다. Quasi-isomorphism과 chain homotopy의 관계는 명제 6의 증명이 3줄로 끝나는 것이 인상적이다 — $$a\in\ker d_n^C$$이므로 $$h_{n-1}d_n^C(a)=0$$이 되어 $$f_n(a)-g_n(a)=d_{n+1}^D(h_n(a))$$가 바로 나온다. Mapping cone의 differential 정의에서 부호 $$(-d_{n-1}(x))$$가 처음에는 왜 음수인지 이해가 안 됐는데, $$d^2=0$$을 확인하기 위해 $$d_n\circ d_{n+1}$$을 직접 계산해보니 $$f$$ 항과 $$d^2$$ 항이 각각 상쇄되는 구조가 명확해졌다. 다만 따름정리 9에서 "connecting map이 $$H_n(f)$$가 된다"는 주장을 증명 없이 인용하고 있는데, 이 확인이 직접 하기에 꽤 계산이 필요해서 아쉬웠다.

## [분해](/ko/math/homological_algebra/resolutions)

이 글은 호몰로지 대수학의 실질적 출발점이다. Diagram chasing, homology, long exact sequence까지가 "도구"를 마련하는 과정이었다면, 분해(resolution)부터가 실제로 그 도구를 써서 무언가를 만들어내는 단계다. 핵심 아이디어는 단순하다: 임의의 대상 $$M$$을 projective object(또는 injective object)들의 exact sequence로 "근사"하면, homology를 계산하는 대신 이 근사를 통해 $$M$$의 정보를 추출할 수 있다는 것이다.

Projective object와 injective object의 정의는 [\[다중선형대수학\] §사영가군, 단사가군, 평탄가군](/ko/math/multilinear_algebra/various_modules)에서 module 언어로 이미 봤지만, 이 글에서는 abelian category의 diagram 언어로 다시 쓴다. Projective object $$P$$는 임의의 전사 $$A\twoheadrightarrow B$$에 대해 $$P\to B$$가 주어지면 $$P\to A$$로 올려보낼 수 있는 대상이고, injective object $$I$$는 임의의 단사 $$A\hookrightarrow B$$에 대해 $$A\to I$$가 주어지면 $$B\to I$$로 확장할 수 있는 대상이다. 이 "lifting property"가 resolution의 존재성 증명에서 반복적으로 사용되는 메커니즘이다.

Left resolution $$P_\bullet\overset{\epsilon}{\to} M$$과 right resolution $$M\overset{\eta}{\to} I^\bullet$$의 정의에서 augmentation map $$\epsilon$$, $$\eta$$가 등장하는데, 이 map이 없으면 $$P_\bullet$$ 자체는 $$M$$과 무관한 exact sequence에 불과하다. $$\epsilon$$이 $$P_\bullet$$을 $$M$$에 "연결"하는 역할을 하는 것이고, $$\im(d_1)=\ker\epsilon$$이라는 exactness 조건이 $$P_\bullet$$이 $$M$$을 정확히 근사하고 있다는 것을 보장한다. $$\mathcal{A}^\op$$에서의 duality 관찰 — projective object가 injective object로, left resolution이 right resolution으로 바뀐다는 것 — 은 형식적이지만 이후 injective resolution을 다룰 때 projective 경우의 논증을 그대로 베껴 쓸 수 있게 해줘서 실용적이다.

명제 3의 증명은 "enough projective $$\implies$$ 모든 대상이 projective resolution을 가진다"는 것인데, 구성 방식이 induction의 전형이다. $$\epsilon_0:P_0\twoheadrightarrow M$$을 잡고, $$M_0=\ker\epsilon_0$$에 다시 $$\epsilon_1:P_1\twoheadrightarrow M_0$$을 잡는 걸 반복하면 $$d_n=\iota_{n-1}\circ\epsilon_n$$으로 differential이 만들어진다. $$\im(d_n)=\ker(d_{n-1}$$이라는 exactness 확인이 $$\epsilon_n$$의 전사성과 $$\iota_{n-2}$$의 단사성에서 각각 나온다는 것이 깔끔한데, Diagram Chasing에서 봤던 "전사 $$\implies$$ image가 전체" "단사 $$\implies$$ kernel이 영"이라는 동치 조건이 여기서 직접 쓰인다.

$$\lMod{A}$$가 enough projective를 갖는다는 것은 자명하다 — free module은 projective이므로 임의의 $$A$$-module $$M$$에 대해 $$A^{\oplus I}\twoheadrightarrow M$$을 잡으면 된다. 반면 enough injective는 자명하지 않다. 증명 전략이 흥미로운데, $$\mathbb{Z}\to A$$로부터 얻어지는 coextension of scalar $$\Ab\to\lMod{A}$$가 restriction of scalar의 right adjoint이므로, right adjoint는 injective object를 보존한다는 일반적 사실로 $$\Ab$$의 injective object를 $$\lMod{A}$$로 옮길 수 있다. $$\Ab$$에서 $$\mathbb{Q}/\mathbb{Z}$$가 injective cogenerator라는 것도 중요한 관찰인데, $$I(A)=\prod_{f\in\Hom(A,\mathbb{Q}/\mathbb{Z})}\mathbb{Q}/\mathbb{Z}$$라는 구성이 "충분히 많은 map을 모아서 injective envelope을 만든다"는 아이디어를 보여준다.

정리 6(comparison theorem)은 "projective resolution $$P_\bullet\to M$$과 임의의 $$u:M\to N$$이 주어지면, 임의의 left resolution $$Q_\bullet\to N$$에 대해 $$u$$를 lifting하는 chain map $$f:P_\bullet\to Q_\bullet$$이 up to homotopy로 유일하게 존재한다"는 결과다. 이것이 resolution의 유일성을 보장하는 핵심 정리인데, $$P_i$$의 projectivity가 $$f_i$$의 존재성을 보장하고, $$f$$의 유일성(up to homotopy)은 Long Exact Sequence에서 정의한 chain homotopy 관계로 포착된다. "유일성이 up to homotopy"라는 것 — 정확히 같은 chain map이 아니라 homotopy class로 유일하다는 것 — 이 "호몰로지 대수학에서는 정확한 형태보다 homology 위에서의 효과가 더 중요하다"는 철학과 정확히 맞아떨어진다.

보조정리 7(horseshoe lemma)은 $$0\to A'\to A\to A''\to 0$$이 short exact sequence일 때, $$A'$$와 $$A''$$의 projective resolution으로부터 $$A$$의 projective resolution을 직접 짜는 구성이다. $$P_n=P_n'\oplus P_n''$$으로 두면 $$0\to P'\to P\to P''\to 0$$이 exact sequence가 되는데, $$P_n''$$의 projectivity가 $$P_n''\to A$$를 lifting하는 데 사용된다는 것이 핵심이다. Diagram Chasing의 보조정리 5("$$f'$$가 단사면 kernel 열이 exact")를 직접 인용해서 induction을 진행하는 구조가 깔끔하다. 이 구성이 이후 derived functor에서 short exact sequence의 resolution을 다룰 때 필수적인데, $$A$$의 resolution을 $$A'$$와 $$A''$$의 resolution으로 "조립"할 수 있다는 것이 long exact sequence와 호환됨을 보장한다.

솔직한 반응: $$\lMod{A}$$가 enough projective라는 것은 free module이 projective라는 사실로부터 바로 와서 쉬웠다. Enough injective의 증명은 "right adjoint는 injective를 보존한다"는 범주론적 사실을 $$\Ab\to\lMod{A}$$에 적용하는 구조가 예상치 못했는데, $$\mathbb{Q}/\mathbb{Z}$$가 injective cogenerator라는 것을 알고 나면 논증이 간결해져서 인상적이었다. 보조정리 7의 구성은 induction 단계를 하나하나 따라가면 이해할 수 있었지만, $$P_0''$$의 projectivity로 $$P_0''\to A$$를 정의하는 부분에서 "왜 $$A''$$의 resolution을 쓰면서 $$A$$로 가는 map을 잡을 수 있지?"라고 순간 헷갈렸다 — $$P_0''\twoheadrightarrow A''$$의 surjection과 $$A\twoheadrightarrow A''$$의 surjection을 합성해서 $$P_0''\twoheadrightarrow A''$$를 얻고, $$P_0''$$의 projectivity로 이를 $$P_0''\to A$$로 올린다는 것을 이해하고 나니 명확해졌다. 다만 정리 6의 증명이 비어있는 것이 아쉬웠다 — comparison theorem은 이후 유도함자를 정의할 때 핵심적으로 쓰이는 결과인데, 증명 없이는 "up to homotopy로 유일"이라는 주장의 근거를 스스로 확인할 수 없었다.

## [유도함자](/ko/math/homological_algebra/derived_functors)

유도함자는 호몰로지 대수학이 실제로 "동작"하는 지점이다. 분해에서 마련한 projective/injective resolution이라는 도구를 가지고, exact functor가 아닌 함자의 "잃어버린 exactness"를 복구하는 것이 이 글의 목표다. 핵심 아이디어는 단순하다: right exact functor $$F$$에 대해 $$A$$의 projective resolution $$P_\bullet$$을 적용한 뒤 호몰로지를 취하면, $$F$$가 왼쪽에서 잃어버린 정보를 $$L_iF(A)=H_i(F(P_\bullet))$$로 복원할 수 있다는 것이다.

$$\delta$$-functor의 정의가 이 글의 출발점이다. $$T_0=F$$로 시작해서 short exact sequence마다 connecting map $$\delta_n:T_n(C)\to T_{n-1}(A)$$를 붙여 long exact sequence를 만드는 구조인데, 이게 자연변환으로서의 naturality 조건까지 포함한다는 것이 중요하다. "$$\delta$$가 short exact sequence들의 모임에서 자연변환"이라는 관찰이 $$\delta$$-functor의 정의를 이해하는 데 핵심인데, 같은 exact sequence를 다른 exact sequence로 보내는 morphism 사이에서 $$\delta$$가 commute해야 한다는 것이 diagram chasing의 naturality와 같은 맥락이다. Universal $$\delta$$-functor의 정의는 $$S_0\to T_0$$ 하나가 주어지면 $$\delta$$와의 호환에 의해 유일하게 확장된다는 것인데, 이것이 이후 left derived functor가 universal이라는 명제 8의 동기가 된다.

Left derived functor의 well-definedness(보조정리 5)는 비교정리(분해의 정리 6)의 직접적인 적용이다. 두 projective resolution이 주어지면 identity map $$A\to A$$를 lifting하는 chain map이 up to homotopy로 유일하므로, 호몰로지 위에서 같은 함수를 유도한다는 것이 핵심이다. $$L_0F(A)\cong F(A)$$라는 계산이 $$F$$의 right exactness에서 $$F(P_1)\to F(P_0)\to F(A)\to 0$$이 exact임을 이용하는 것도 깔끔하다 — $$L_0$$은 $$F$$ 자체를 복원하고, $$L_i$$ ($$i>0$$)는 $$F$$의 exactness 결함을 측정한다는 해석이 자연스럽다.

보조정리 7의 증명이 이 글에서 가장 기술적인 부분이다. Horseshoe lemma로 $$B$$의 resolution $$Q_\bullet$$을 $$P_\bullet\oplus R_\bullet$$로 구성하면, 각 차수에서 $$0\to P_n\to Q_n\to R_n\to 0$$이 $$R_n$$의 projectivity에 의해 split exact가 된다. 이 split exactness가 $$F$$를 적용해도 깨지지 않는다는 것이 핵심인데, [\[다중선형대수학\] §Hom과 텐서곱](/ko/math/multilinear_algebra/hom_and_tensor)에서 다룬 "split exact sequence는 임의의 additive functor를 적용해도 exact sequence가 된다"는 사실이 여기서 직접 쓰인다. 이로부터 $$0\to F(P_\bullet)\to F(Q_\bullet)\to F(R_\bullet)\to 0$$이 short exact sequence가 되고, 호몰로지의 long exact sequence가 $$L_iF$$의 connecting map을 제공하는 구조가 분해의 보조정리 7과 정확히 대응된다.

Right derived functor는 이 모든 것의 $$\mathcal{A}^\op$$에서의 dual이다. Left exact functor $$F$$에 대해 injective resolution으로 $$R^iF(A)=H^i(F(I^\bullet))$$를 정의하면, cohomological $$\delta$$-functor를 얻는다. 위첨자를 쓰는 이유가 "cohomology 관련에서 나온다"는 설명은 다소 형식적이지만, $$R^i$$의 $$i$$가 cohomological degree라는 것과 homological $$L_i$$의 $$i$$가 homological degree라는 구분은 이후 spectral sequences에서 indexing을 맞출 때 실제로 중요해진다.

솔직한 반응: $$\delta$$-functor의 정의 자체는 "long exact sequence를 만드는 functor의 모임"이라는 아이디어가 자연스러워서 비교적 빨리 이해했다. Universal $$\delta$$-functor의 정의에서 "$$S_0\to T_0$$가 주어지면 유일하게 확장"이라는 조건이 $$\delta$$의 naturality로부터 나온다는 것도 명제 8의 증명을 읽기 전에 이미 직감할 수 있었다. 보조정리 7의 증명에서 split exact sequence에 $$F$$를 적용해도 exact가 된다는 부분이 가장 핵심적인데, 이 사실을 다중선형대수학에서 이미 봤기 때문에 "아, 그래서 horseshoe lemma를 쓰는 거구나"라고 연결됐다 — $$Q_n$$을 직접 구성하면 $$F$$를 적용해도 exactness가 유지된다는 것이 horseshoe lemma의 존재 이유다. 다만 $$L_iF$$들이 universal이라는 명제 8의 증명이 생략된 것이 아쉬운데, 보조정리 5의 well-definedness와 보조정리 7의 $$\delta$$-functor 구성을 합치면 될 것 같긴 하나 "유일하게 확장"이라는 universality의 핵심 논증을 직접 채우기는 꽤 까다로워 보인다.

## [Ext와 Tor](/ko/math/homological_algebra/ext_and_tor)

유도함자의 일반 이론을 실제로 적용하는 첫 번째 글이다. $$\Hom$$과 $$\otimes$$라는 $$\lMod{A}$$에서 가장 기본적인 두 bifunctor의 derived functor인 $$\Ext$$와 $$\Tor$$를 정의하고, 그 성질을 살펴본다. $$\Ext_A^i(M,N)=R^i\Hom(M,-)(N)$$, $$\Tor_i^A(M,N)=L_i(-\otimes N)(M)$$ — 정의 자체는 유도함자 글의 형식을 그대로 따르지만, 이 두 함자가 왜 특별한지는 이후 계산과 응용에서 드러난다. $$\Hom(M,-)$$이 exact functor인 것이 $$N$$이 injective인 것과 동치라는 관찰(명제 1 근처)을 derived functor의 언어로 재해석하면, $$\Ext_A^1(M,N)=0$$이 모든 $$M$$에 대해 성립하는 것이 $$N$$의 injectivity를 characterise한다는 것이고, 이는 $$\Tor$$의 경우에도 projectivity에 대해 같은 논리가 적용된다.

이 글에서 가장 기술적인 부분은 balancing 증명(명제 3)이다. $$\Ext_A^i(M,N)$$을 $$M$$의 projective resolution으로 계산하든 $$N$$의 injective resolution으로 계산하든 결과가 같다는 것인데, 증명 전략이 호몰로지 글에서 정의한 double complex와 filtration을 직접 사용한다. $$K^{p,q}=\Hom(P_q,I^p)$$로 double complex를 잡고, total complex의 cohomology를 두 가지 filtration으로 각각 계산해서 같음을 보이는 구조인데, 호몰로지 글에서 total complex의 cohomology 계산이 "주의가 필요하다"고 했던 것이 여기서 구체적으로 실현된다. $$H^q(K^{p,\bullet})$$와 $$H^p(K^{\bullet,q})$$가 각각 $$q>0$$, $$p>0$$에서 사라진다는 것이 projective/injective의 정의에서 직접 나오고, 이 소멸이 filtration의 short exact sequence에서 long exact sequence를 단순화하는 핵심이다. $$\Tor$$의 경우(명제 4)도 같은 전략인데, projective module이 flat이라는 사실로 처리한다는 것이 차이점이다.

계산 예시가 직관 잡기에 좋다. $$\Tor_1^\mathbb{Z}(\mathbb{Z}/n,\mathbb{Z}/m)\cong\mathbb{Z}/(n,m)$$이라는 결과는 $$\Tor$$라는 이름이 "torsion"에서 왔다는 것을 보여주고, $$\Ext^1_\mathbb{Z}(\mathbb{Z}/n,A)\cong A/nA$$라는 결과는 $$\Ext$$가 extension의 equivalence class와 연결된다는 힌트를 준다. $$\mathbb{Z}$$ 위의 resolution $$0\to\mathbb{Z}\xrightarrow{\cdot n}\mathbb{Z}\to\mathbb{Z}/n\to 0$$이 이 모든 계산의 출발점인데, 이 resolution의 길이가 1이라는 것이 $$\Tor_i$$, $$\Ext^i$$가 $$i\geq 2$$에서 모두 0인 이유다.

Koszul complex(정의 7)는 이 글의 마지막 부분에서 갑자기 등장하는데, $$\Ext$$/$$\Tor$$의 정의와 직접 연결되기보다는 "resolution의 구체적인 예시"로 제시된다. $$\bigwedge F$$에 graded derivation $$d(f)=\varphi(f)$$로 differential을 부여하는 구성은 exterior algebra의 구조를 적극 활용하는 것인데, regular sequence 조건하에서 이 complex가 exact하다는 증명(귀납법)의 핵심이 $$K(\x_1,\ldots,\x_n)_i\cong K'_i\oplus K'_{i-1}\cdot e_n$$이라는 분해와 induction hypothesis의정교한 결합이다. 마지막에 polynomial ring의 $$\Tor$$를 계산해서 $$\Tor_i^A(\mathbb{K},\mathbb{K})\cong\bigwedge^i_\mathbb{K}(\mathbb{K}^n)$$을 얻는 부분은 인상적인데, 이 결과가 global dimension과 연결된다고 하지만 그 정의가 없어서 맥락을 따라가기 어려웠다.

솔직한 반응: $$\Ext$$와 $$\Tor$$의 정의 자체는 유도함자 글의 형식적 적용이라 쉽게 이해했다. Balancing 증명의 구조 — double complex를 잡고 filtration으로 양쪽을 계산 — 은 호몰로지 글의 double complex/filtration이 왜 필요한지 보여줘서 "아, 그래서 그때 그런 도구를 정의했구나"라고 느꼈다. 다만 증명의 세부 계산, 특히 $$\delta_n$$이 정확히 $$\Hom(M,I^n)\to\Hom(M,I^{n+1}$$로부터 온다는 주장("실제로 계산을 해 보면")을 직접 확인하지는 않았다. Koszul complex 부분은 갑자기 분위기가 바뀌는데, exterior algebra와 graded derivation을 다중선형대수학에서 봤지만 regular sequence는 가환대수학에서 정의된 개념이라 이 글 안에서는 정의 없이 쓰이고 있다. Yoneda Ext도 Wikipedia 링크만 있고 정의가 없어서, $$\Ext^1$$이 extension의 equivalence class라는 주장의 근거를 이 글만으로는 확인할 수 없다.

⚠️ 정의 없이 사용: `regular sequence` (가환대수학 §정칙국소환에서 정의, 이 카테고리/이전 노트에서 미정의)
⚠️ 정의 없이 사용: `graded derivation` (검색해도 정의를 찾지 못함)
⚠️ 정의 없이 사용: `Yoneda Ext` (정의 없이 Wikipedia 링크만 인용)
⚠️ 정의 없이 사용: `global dimension` (정의 없이 이후 결과로만 언급)

## [유도카테고리](/ko/math/homological_algebra/derived_categories)

이 글은 호몰로지 대수학 카테고리의 마지막 글이자, 앞서 쌓아온 모든 것의 개념적 완성이다. 유도함자에서 projective/injective resolution의 선택이 homology 레벨에서는 영향을 주지 않지만 chain complex 레벨에서는 자연스럽지 않았던 문제를, quasi-isomorphic한 complex들을 처음부터 같은 것으로 취급하여 해결한다. 핵심 구성은 세 단계다: $$\Ch(\mathcal{A})$$에서 chain homotopic한 map들을 동일시하여 homotopy category $$K(\mathcal{A})$$를 만들고, 여기서 quasi-isomorphism을 Verdier quotient로 invertible하게 만들어 $$D(\mathcal{A})$$를 얻는다. 분수체의 구성과 유사한 localization이라는 관찰이 $$D(\mathcal{A})$$의 morphism을 roof diagram $$X\overset{s}{\leftarrow} X'\overset{f}{\rightarrow} Y$$로 이해할 수 있게 해주는데, $$s$$가 quasi-isomorphism이라는 것이 핵심이다.

$$D(\mathcal{A})$$에서 $$A$$의 injective resolution과 projective resolution이 모두 $$A[0]$$과 quasi-isomorphic하므로, resolution의 선택 문제가 자연스럽게 사라진다. $$D^+(\mathcal{A})$$는 injective resolution에, $$D^-(\mathcal{A})$$는 projective resolution에, $$D^b(\mathcal{A})$$는 대부분의 응용에 적합한 무대인데, amplitude라는 개념으로 boundedness를 설명하는 것이 깔끔하다. Shift functor $$[n]$$의 정의에서 differential의 sign convention $$(-1)^n$$은 호몰로지 글에서 이미 봤던 것인데, $$H^i(A[n])=H^{i+n}(A)$$라는 결과가 sign이 cohomology에 영향을 주지 않는다는 것을 확인시켜준다.

Derived functor의 새로운 정의가 이 글의 핵심이다. $$K$$-projective와 $$K$$-injective라는 개념을 도입해서, 기존의 "대상의 resolution에 functor를 적용"하는 방식을 "complex 전체에 대해 resolution을 취한 뒤 functor를 적용"하는 것으로 일반화한다. $$R F(A^\bullet)=F(I^\bullet)$$, $$L F(A^\bullet)=F(P_\bullet)$$라는 정의가 $$A[0]$$에 적용되면 $$H^i(RF(A[0]))=(R^iF)(A)$$가 되어 기존 유도함자를 복원한다는 것이 명제 9와 그 뒤의 관찰에서 드러나는데, "모든 $$R^iF$$의 정보가 $$RF$$라는 단일 functor에 들어있다"는 관점이 인상적이다. $$R\Hom(A,B)$$의 cohomology가 $$\Ext^i(A,B)$$라는 명제 10의 증명이 projective resolution을 $$K$$-projective complex로 사용하는 것을 보면서, $$K$$-projective가 기존 projective object의 "complex 수준의 일반화"라는 것이 체감됐다.

Triangulated category 부분은 이 글에서 가장 추상적인 부분이다. Distinguished triangle이 abelian category의 short exact sequence를 대체한다는 직관은 mapping cone과의 연결($$0\to A\to B\to C(f)\to 0$$의 derived version)을 통해 이해할 수 있었지만, octahedral axiom(TR4)은 "합성 $$B\to C\to D$$에 연관된 octahedron을 이루는 세 개의 distinguished triangle이 존재한다"는 설명만으로는 왜 이것이 필요한지, 어떤 역할을 하는지 체감이 되지 않았다. $$RF$$가 triangulated functor라는 명제 12의 증명에서 $$K$$-injective complex들의 mapping cone도 $$K$$-injective가 된다는 관찰이 핵심인데, bounded below $$K$$-injective complex들이 triangulated subcategory를 이룬다는 것이 이 증명의 토대다.

Derived adjunction(명제 13)은 이 글의 마지막 하이라이트다. $$F\dashv G$$가 원래 adjunction이면 $$LF\dashv RG$$가 derived category에서 성립한다는 것인데, 증명이 의외로 간결하다 — $$K$$-projective resolution과 $$K$$-injective resolution을 각각 선택하면, complex 수준의 adjunction이 $$D(\mathcal{A})$$에서의 Hom으로 바로 환원된다. Tensor-Hom adjunction의 예시에서 $$\mathbb{Z}/n\mathbb{Z}$$가 flat이 아니어서 naive adjunction이 깨진다는 구체적 계산($$\Tor_1^\mathbb{Z}(\mathbb{Z}/n,\mathbb{Z}/n)\cong\mathbb{Z}/n$$)이 derived adjunction의 동기를 잘 보여준다. $$A\otimes^L B$$와 $$R\Hom(B,C)$$의 adjunction $$\Hom(A\otimes^L B,C)\cong\Hom(A,R\Hom(B,C))$$는 호몰로지 대수학 전체를 관통하는 결과로서, 앞서 쌓아온 모든 도구가 이 하나의 식으로 수렴한다는 느낌을 준다.

솔직한 반응: $$D(\mathcal{A})$$의 구성 자체는 localization의 추상적 패턴을 따르니까, 분수체의 구성과 비교하면 큰 그림이 잡힌다. Roof diagram으로 morphism을 설명하는 부분도 $$s^{-1}$$을 "존재하지 않을 수도 있는 map"으로 보는 관점이 localization의 일반적 직관과 맞아떨어져서 이해할 수 있었다. $$K$$-projective와 $$K$$-injective의 정의는 "Hom functor를 quasi-isomorphism에 대해 invariant하게 만드는 complex"라는 것이 기존 projective/injective의 lifting property와 정확히 대응된다는 것을 인식하면 자연스럽다. 하지만 octahedral axiom은 정말로 이해가 안 됐다. Geometric intuition이라는 설명 외에 이 공리가 실제로 보장하는 것이 무엇인지, 어떤 상황에서 이것이 필요한지에 대한 설명이 없어서 이 글만으로는 "왜 triangulated category에 이 공리가 필요한지"를 판단할 수 없었다. $$K$$-injective resolution의 존재성도 "충분히 injective를 갖는 임의의 abelian category의 homotopy category는 enough $$K$$-injective resolution을 가진다"고만 언급되고 증명이 없는데, 이 사실이 $$R F$$의 well-definedness에 필수적이므로 아쉬웠다.

⚠️ 정의 없이 사용: `Verdier quotient` (정의 2에서 사용, 분수체의 구성과 유사하다고만 설명 — 정확한 정의는 이 글/이전 노트에서 미정의)
⚠️ 정의 없이 사용: `octahedral axiom` (TR4에서 사용, 이름만 언급 — 정의 없이 공리로 나열)

### 카테고리 회고

호몰로지 대수학은 "exact하지 않은 functor를 고치는 것"이라는 하나의 목표를 향해 diagram chasing부터 derived categories까지 일관된 흐름으로 전개된다. 앞서 범주론에서 다룬 abelian category의 구조와 대수적 구조/다중선형대수학에서 봤던 module의 구체적 계산이 이 카테고리 전반의 토대가 됐는데, 특히 snake lemma와 horseshoe lemma가 반복적으로 등장하는 패턴이 인상적이었다. 가장 막혔던 지점은 spectral sequence의 $$d_r$$ well-definedness와 triangulated category의 octahedral axiom — 둘 다 이 카테고리 안에서 충분히 설명되지 못한 채 넘어간 부분이었다.

## [스펙트럼 열](/ko/math/homological_algebra/spectral_sequences)

이 글은 호몰로지 대수학의 계산 도구 중 가장 강력하면서도 가장 추상적인 spectral sequence를 다룬다. 동기는 Ext와 Tor의 balancing 증명에서 이미 봤다: double complex의 total complex에 horizontal/vertical filtration을 걸고, 각 filtration에서 나온 spectral sequence가 같은 대상에 수렴한다는 것이 그 증명의 핵심 아이디어였다. 이 글은 그 아이디어를 일반화해서, 임의의 filtered complex로부터 spectral sequence를 구성하고 그것이 원래 complex의 cohomology를 page 단위로 근사한다는 것을 보인다.

정의 자체는 비교적 직관적이다. Spectral sequence는 bigraded object $$E_r^{p,q}$$와 bidegree $$(r,1-r)$$의 differential $$d_r$$로 구성되며, 각 page의 cohomology가 다음 page를 준다: $$E_{r+1}^{p,q}\cong\ker d_r/\im d_r$$. $$r$$이 커질수록 $$d_r$$의 bidegree가 점점 "대각선 방향"으로 틀어지기 때문에, first quadrant spectral sequence에서는 충분히 큰 $$r$$에서 $$d_r$$이 영역 밖으로 나가버려 자동으로 안정화된다(regularity). 이 안정화된 값 $$E_\infty^{p,q}$$가 최종적으로 $$\gr^p H^{p+q}$$에 동형이면 spectral sequence가 수렴한다고 말한다.

Filtered complex로부터 spectral sequence를 구성하는 부분이 이 글의 핵심이다. $$E_0^{p,q}=\gr^p A^{p+q}$$로 시작해서, $$d_r$$은 원래의 differential $$d$$를 quotient로 factor through 한 것이다. $$d_r$$의 정의에서 "filtration을 $$r$$단계 건너뛴다"는 것이 $$r$$번째 page의 differential이 측정하는 것인데, $$r=0$$이면 $$d$$의 가장 가까운 성분, $$r$$이 커지면 더 먼 성분을 잡아내는 구조다. 다만 $$d_r$$이 well-defined임을 보이는 계산이 Stacks Project로 링크되어 있고 이 글에서는 생략되어 있는데, 이 확인이 없으면 $$E_{r+1}\cong H(E_r,d_r)$$라는 명제 7의 핵심 주장을 직접 검증할 수 없다는 것이 아쉽다.

명제 10은 bounded filtered complex의 spectral sequence가 항상 수렴한다는 것을 보장하는데, 이 수렴의 의미는 $$E_\infty^{p,q}\cong\gr^p H^{p+q}$$이다. "수렴"의 두 가지 수준 — weak convergence( $$E_\infty$$만 존재)와 strong convergence(Hausdorff + exhaustive 조건으로 $$H^n$$을 유일하게 재구성 가능) — 을 구분하는 것이 중요하다. First quadrant의 경우 strong convergence까지 보장된다는 것이 이후 응용에서 핵심적인데, 이 글에서는 이 점을 명시적으로 다루지 않고 넘어간다. 예시 11에서 double complex의 vertical/horizontal filtration에서 나온 두 spectral sequence가 같은 $$H^\bullet(\Tot(K))$$에 수렴한다는 관찰이 Ext/Tor balancing의 "더 fancy한 언어로의 복원"이라는 결론이 깔끔하다.

솔직한 반응: spectral sequence의 정의와 수렴의 큰 그림은 이해했다. "filtration으로 complex를 쪼개고, page를 거치면서 점진적으로 정제한다"는 철학 자체는 자연스럽고, Ext/Tor balancing에서 이미 proto-version을 봤으니까 동기도 명확하다. First quadrant regularity의 증명 아이디어 — $$d_r$$이 영역 밖으로 나가면 0이 된다 — 도 직관적이다. 하지만 $$d_r$$의 일반적인 구성($$\ast$$)에서 "다소 복잡한 계산"이라는 한 줄로 넘어간 부분이 걸린다. $$E_0$$와 $$E_1$$의 경우는 이해할 수 있지만, 임의의 $$r$$에 대해 $$d_r$$이 well-defined이고 $$d_r^2=0$$을 만족한다는 것은 이 글만으로는 확인할 수 없다. Weak vs strong convergence의 차이도 정의는 읽었지만, 실제로 어떤 spectral sequence가 strong convergence를 못 하는지 예시가 없어서 체감이 안 된다. 그럼에도 불구하고 이 글이 호몰로지 대수학 카테고리의 마지막 계산 도구로서, 앞서 쌓아온 double complex/filtration/derived functor의 모든 것을 하나로 엮어내는 역할을 한다는 점에서 큰 그림이 인상적이다.
