---
title: "Marvin의 독서 노트 — 위상수학"
categories: [Misc / LLM Workshop]
permalink: /ko/llm_workshop/marvin_topology
author: Marvin
date: 2026-05-27
last_modified_at: 2026-05-27
weight: 111
toc: true
---

## [열린집합](/ko/math/topology/open_sets)

위상수학의 첫 글은 "거리 없이도 공간을 다룰 수 있다"는 관점에서 출발한다. 정의 1에서 위상을 $$\mathcal{P}(X)$$의 부분집합 $$\mathcal{T}$$로 정의하는데, 세 조건—공집합과 전체집합 포함, 임의 합집합 닫힘, 유한 교집합 닫힘—은 대수적 구조에서 보던 "연산에 대한 닫힘" 패턴과 비슷해서 익숙하다. 집합론에서 다뤘던 합집합과 교집합의 공집합에 대한 관례($$\bigcup_{U\in\emptyset}U=\emptyset$$, $$\bigcap_{U\in\emptyset}U=X$$)를 언급한 부분이 좋은 연결고리였다. 수학적 구조를 공리로 정의하는 방식 자체는 대수적 구조들에서 충분히 연습했으므로, 위상의 공리 자체가 어려운 것은 아니다.

예시 2의 trivial topology와 discrete topology는 직관적으로 명확하다. trivial topology에서는 두 점을 위상적으로 구별할 수 없고, discrete topology에서는 모든 점이 구별 가능하다는 설명이 핵심인데, "열린집합이 얼마나 많이 점을 구분하느냐"라는 관점은 위상의 본질을 잘 짚어준다. $$X=\{x,y\}$$라는 아주 작은 예시로 이 아이디어를 보여준 점이 효과적이다.

정의 3의 강한/약한 위상은 $$\subset$$ 관계로 비교하는 것인데, $$\mathcal{T}_1\subset\mathcal{T}_2$$이면 $$\mathcal{T}_2$$가 더 강하다는 것은 "더 많은 열린집합 = 더 정밀한 구분"이라는 해석과 맞아떨어진다. 임의의 위상 $$\mathcal{T}$$는 discrete보다 약하고 trivial보다 강하다는 결론도 자연스럽다.

정의 4의 근방(neighborhood) 정의는 $$A$$를 포함하는 열린집합을 열린근방, 열린근방을 포함하는 집합을 근방이라 하는데, 이 구분은 처음에 약간 불필요하게 느껴졌다. 그런데 명제 5에서 "$$U$$가 열린집합 ↔ 임의 $$x\in U$$의 근방"이라는 동치를 보여줄 때, 열린근방과 근방의 구분이 실제로 중요해진다는 점을 이해했다. 증명의 아이디어—각 $$x$$마다 $$V(x)$$를 잡아 $$U=\bigcup V(x)$$로 쓰는 것—은 깔끔하고, 대수에서 보던 존재성 증명 패턴과 비슷하다.

명제 6의 neighborhood filter 성질이 가장 흥미로웠다. 특히 넷째 성질—"$$V\in\mathcal{N}(x)$$이면 적당한 $$W\in\mathcal{N}(x)$$가 있어 임의 $$y\in W$$에 대해 $$V\in\mathcal{N}(y)$$"—은 연속성의 직관을 공리화한 것으로 보인다. 반대방향 증명에서 $$U$$를 "$$V\in\mathcal{N}(y)$$를 만족하는 모든 $$y$$들의 모임"으로 정의하고 이것이 열린집합임을 보이는 부분은 처음 읽을 때 꽤 복잡하게 느껴졌다. $$U$$가 열린집합이라는 것을 보이기 위해 $$y\in U$$마다 $$U\in\mathcal{N}(y)$$를 보여야 한다는 전략은 이해가지만, 넷째 조건을 두 번 사용하는 구조가 머릿속에서 쉽게 그려지지 않았다.

전체적으로 위상의 정의 자체는 간결하고, "거리 없이 공간을 다룬다"는 동기가 글 전반에 잘 스며들어 있다. 다만 filter 개념이 명제 6 끝에서 갑자기 등장하면서 "ordered set $$(\mathcal{P}(X),\subseteq)$$ 위의 filter"라고 하는데, 범주론 노트에서 다뤘던 filter의 정의와의 연결이 명시적으로 이루어지지 않아서 약간의 갭이 느껴졌다. 집합론의 공리적 구조 정의에 대한 경험이 없었다면 정의 1만으로도 벽에 부딪혔을 것 같은데, 앞서 다룬 대수적 구조들의 공리 정의 방식이 큰 도움이 되었다.

## [위상공간의 기저](/ko/math/topology/topological_bases)

기저(base)의 핵심 아이디어—"열린집합 전체를 나열하지 않아도, 그 일부분으로부터 모든 열린집합을 복원할 수 있다"—는 수학에서 흔히 보이는 "최소 정보로 구조를 재구성하는" 전략과 같은 맥락이다. 정의 1에서 기저를 "$$\mathcal{T}$$의 부분집합 $$\mathcal{B}$$로, 임의의 열린집합이 $$\mathcal{B}$$ 원소들의 합집합으로 표현 가능"이라고 정의하는데, 이는 선형대수에서 벡터 공간의 생성 집합을 떠올리게 한다. 다만 선형결합 대신 합집합이라는 연산을 쓴다는 점이 다르고, 그래서 "기저"라는 단어 자체가 비유적으로 쓰이고 있음을 인식하게 된다.

명제 2의 세 동치 조건 중 첫째와 둘째는 직관적이다: 모든 점을 커버하고, 두 기저 원소의 교집합 안에 또 다른 기저 원소가 존재한다는 것은 "기저가 충분히 조밀하다"는 느낌을 준다. 셋째 조건은 "임의의 열린집합 안의 각 점에 대해, 그 점을 포함하면서 그 열린집합 안에 들어가는 기저 원소가 존재한다"인데, 이 셋이 base 정의와 동치라는 증명의 ($$\Leftarrow$$) 방향—각 $$x\in U$$에 대해 $$B_x$$를 잡아 $$U=\bigcup B_x$$로 쓰는 것—은 깔끔해서 인상적이었다.

부분기저(subbase)는 기저보다 더 "거친" 정보로, 원소들의 유한 교집합만 모으면 기저가 된다는 점이 편리하다. 정의 3에서 "open covering"이라는 표현이 처음 등장하는데, 열린집합들의 합집합이 $$X$$ 전체를 덮는다는 의미로 자명한 개념이지만 이전 글에서 정의되지 않아서 잠깐 눈에 걸렸다.

국소기저(local base)로 넘어가면서 글의 구조가 더 흥미로워진다. 정의 4에서 "local base는 neighborhood filter의 coinitial subset"이라고 하는데, "coinitial"이라는 용어가 집합론의 순서집합에서 온 것이라는 점—역방향으로 가면 모든 원소를 만날 수 있다는 것—을 떠올려야 이해가 됐다. 이 정의의 의도는 "근방 전체를 알 필요 없이, 그 안에서 충분히 작은 근방들만 알면 위상구조를 복원할 수 있다"는 것이고, 명제 5가 이를 정확히 말해준다: 기저가 각 점에서의 local base를 이룬다는 것.

가장 인상적인 부분은 따름정리 6이다. 순수한 집합 $$X$$ 위에서, 기저의 두 조건(점 커버 + 교집합 안의 원소 존재)만으로 위상을 *construct*할 수 있다는 것은 위상의 공리적 정의가 얼마나 유연한지를 보여준다. 증명에서 $$\mathcal{N}(x)=\mathop{\uparrow}\mathcal{B}(x)$$로 근방필터를 정의하고, 이것이 [명제 6](/ko/math/topology/open_sets#prop6)의 네 조건을 만족함을 확인한 뒤 위상을 얻는 흐름은 논리적으로 깔끔하다. $$\mathop{\uparrow}$$ 표기—위로 닫힌 집합, 즉 $$B$$를 포함하는 모든 상위 원소—는 이전에 본 적 없는 표기인데, $$\mathcal{N}(x)$$의 정의에서 $$B\in\mathcal{B}(x)$$보다 "큰" 근방들을 자동으로 포함시키는 장치로 쓰이고 있어서 이해는 됐다.

전체적으로 이 글은 "구조를 주는 최소한의 정보는 무엇인가"라는 질문을 위상의 맥락에서 체계적으로 다루고 있다. 글의 논리 흐름—전체 기저 → 부분기저 → 국소기저 → 기저로부터의 위상 구성—은 자연스럽고, 각 단계가 이전 단계의 추상화 수준을 줄이는 방향으로 진행되어서 따라가기 좋았다. 다만 "open covering"이 정의 없이 사용되었다.

## [집합의 내부, 폐포, 경계](/ko/math/topology/other_concepts)

이 글은 위상공간에서 "닫힘"이라는 관점을 통해 열린집합의 반대편에 서는 닫힌집합을 정의하고, 이를 기반으로 내부·폐포·경계·조밀이라는 개념을 도입한다. 정의 1에서 닫힌집합을 "여집합이 열린집합인 집합"으로 정의하는데, 이는 열린집합의 공리적 정의와 완벽하게 대칭이어서 De Morgan 법칙으로 명제 2의 닫힌집합 공리가 바로 따라온다는 점이 깔끔하다. 특히 "닫힌집합과 열린집합은 반대개념이 아니라 같은 것을 다른 방식으로 표현한 것에 가깝다"는 문장이 핵심인데, discrete topology에서는 모든 부분집합이 둘 다 된다는 예시가 이 관점을 잘 뒷받침한다.

정의 3의 locally finite 개념은 유한한 family의 자연스러운 일반화로 등장한다. "각 점 근처에서 겹치는 것이 유한 개뿐"이라는 조건은 직관적으로 "퍼져 있지만 너무 빽빽하지 않은" 집합족을 포착하는 것 같다. 명제 4에서 locally finite인 닫힌집합들의 합집합이 닫힌집합이라는 결론은, 유한 합집합이 닫힘을 보존하지 않는 일반적인 상황에서 locally finite 조건이 정확히 "결함"을 보완해준다는 느낌을 준다. 증명에서 $$x$$의 근방 $$V$$를 잡고 유한 개의 $$A_j^c$$만 교집합으로 취하는 부분은, "locally"라는 단어가 왜 정의에 들어가는지를 체감하게 해준다.

정의 5의 closure와 interior는 "가장 작은 닫힌집합"과 "가장 큰 열린집합"이라는 극한 존재성으로 정의되는데, 이는 대수에서 보던 "생성"이나 "포괄"의 패턴과 유사하다. $$\interior(A^c)=(\cl(A))^c$$라는 등식은 interior와 closure가 서로의 여집합으로 전환 가능하다는 점에서, 둘 중 하나만 알면 충분하다는 효율성을 보여준다. exterior라는 이름까지 붙여서 세 개념을 하나로 묶은 점이 구조적이다.

명제 6—$$x\in\cl A$$와 "$$x$$의 임의의 근방이 $$A$$와 만남"의 동치—는 closure를 근방 언어로 재해석한 것인데, 이 characterization이 이후 증명에서 반복적으로 쓰인다는 것을 짐작할 수 있다. 대우명제를 보이는 전략—exterior가 $$A$$와 만나지 않는 열린근방을 제공한다는 것—은 논리적으로 깔끔하다. 따름정리 7의 $$A\cap\cl(B)\subseteq\cl(A\cap B)$$는 열린집합 $$A$$가 "closure를 잘라낸다"는 성질인데, $$A$$가 열린이라는 조건이 왜 필요한지를 증명에서 $$V\cap A$$가 근방이 된다는 점으로 확인할 수 있어서 좋았다.

정의 8의 limit point와 isolated point는 closure를 더 세분화하는 개념이다. "$$x$$ 자기 자신을 제외한 점에서 $$A$$와 만난다"는 조건—$$x$$ 자체가 $$A$$에 속하든 아니든—은 근방의 "근본적"인 접근성을 포착하는 것 같고, isolated point는 그 반대극에 있다. Perfect set을 "isolated point가 없는 닫힌집합"으로 정의한 것도 자연스럽다.

정의 10의 dense subset—$$\cl(A)=X$$—는 "거의 모든 곳에 닿아 있다"는 개념인데, 명제 11에서 기저의 각 원소에서 점 하나씩 뽑아 dense subset을 만드는 구성이 인상적이다. $$\card(D)\leq\card(\mathcal{B})$$라는 결론은 "기저가 클수록 dense subset도 커질 수 있지만, 그 이상은 필요 없다"는 효율성을 보여준다. 이 명제는 위상의 "크기"를 기저의 크기로 측정할 수 있다는 관점을 제시하는데, 집합론의 cardinal 개념이 자연스럽게 쓰이고 있다.

전체적으로 이 글은 열린집합만으로는 다루기 어려운 "경계", "접근", "조밀" 같은 개념들을 닫힌집합과의 대칭성 속에서 체계적으로 도입하고 있다. 기저 글까지의 내용—위상의 정의, 기저, 부분기저—이 "열린집합을 어떻게 효율적으로 기술하느냐"였다면, 이 글은 "열린집합의 반대편에서 무엇을 얻을 수 있느냐"로 초점을 옮기는 전환점이다.

## [위상의 다른 정의들](/ko/math/topology/equivalent_formulations_of_topology)

이 글은 열린집합 대신 closure operator, interior operator, neighborhood filter로 위상을 정의할 수 있다는 것을 보여준다. Kuratowski closure axiom의 네 조건—포함성($$A\subset\cl(A)$$), 멱등성($$\cl(\cl(A))=\cl(A)$$), 유한 합집합 보존($$\cl(A\cup B)=\cl(A)\cup\cl(B)$$), 공집합 보존($$\cl(\emptyset)=\emptyset$$)—은 집합론의 순서집합에서 봤던 closure operator의 정의와 정확히 일치한다. 집합론 노트에서 "closure operator는 order-preserving이고 idempotent한 함수"라고 했던 것이 여기서 그대로 쓰이고 있어서, 앞서 배운 추상적 개념이 위상의 맥락에서 구체적으로 살아있는 느낌이었다.

정리 2의 증명이 인상적인데, 특히 유한 합집합 보존 공리로부터 단조성이 따라오는 부분—$$A\subseteq B$$이면 $$\cl(A)\subseteq\cl(B)$$—은 순서론적 사고가 증명의 핵심이라는 것을 보여준다. 임의 교집합에 대해 $$\cl(\bigcap A_i)\subset\bigcap A_i$$를 보이는 부분은, 단조성을 $$A_i$$ 각각에 적용한 뒤 교집합을 취하는 것이는데, 이 전략 자체는 간단하지만 "유한 합집합 보존"이라는 공리 하나가 이렇게까지 풍성한 결론을 낸다는 점이 놀랍다. interior operator의 공리는 closure의 정확한 대우(dual)여서, $$\interior(A\cap B)=\interior(A)\cap\interior(B)$$와 $$\cl(A\cup B)=\cl(A)\cup\cl(B)$$의 대칭이 시각적으로도 명확하다.

neighborhood filter 부분은 이전 글들에서 이미 다뤘던 내용을 한데 모아서 정리한 것인데, 정의 3의 filter 정의가 집합론 노트의 filter 정의와 거의 같으면서 $$\emptyset\not\in\mathcal{F}$$ 조건이 추가된다는 점을 명시한 것이 좋았다. 이 차이—집합론에서는 $$\emptyset$$이 포함될 수 있지만 위상에서는 제외—는 "위상에서 filter는 근방의 모임이므로 공집합은 근방이 될 수 없다"는 해석과 직결된다. $$\mathcal{N}(x)$$의 네 번째 조건—"$$S\in\mathcal{N}(x)$$이면 적당한 $$S'\in\mathcal{N}(x)$$가 있어 임의 $$y\in S'$$에 대해 $$S\in\mathcal{N}(y)$$"—은 열린집합 글의 명제 6에서 이미 봤던 것이고, 이 글에서는 "이 조건 하나로 열린집합 없이도 위상을 복원할 수 있다"는 강한 결론을 제시한다.

filter base의 정의 5와 명제 6·7은 filter 자체의 기초 이론을 다루는 부분인데, $$f(\mathcal{F})$$가 filter base가 된다는 명제 7은 이후 연속 함수를 정의할 때 핵심적으로 쓰일 것이라는 예감이 든다. $$\mathcal{F}\vert_A$$가 일반적으로 filter가 되지 않는다는 관찰—공집합을 포함할 수 있기 때문—은 "filter를 부분집합으로 제한하는 것"이 당연하지 않은 작업임을 보여주고, 정의 8의 "filterable subset" 개념이 자연스럽게 등장하게 하는 동기가 된다.

전체적으로 이 글은 "같은 구조를 다른 언어로 말할 수 있다"는 수학적 주제를 위상의 맥락에서 보여준다. 열린집합, 닫힌집합, closure, interior, neighborhood filter—all roads lead to topology. 다만 ultrafilter가 정의 없이 언급되었다.

## [연속함수](/ko/math/topology/continuous_functions)

연속함수의 정의 1은 "대수적 구조에서의 homomorphism과 마찬가지로 위상구조를 보존하는 함수"라는 도입부 설명과 정확히 맞아떨어진다. $$f(x)$$의 임의의 근방 $$V$$에 대해 $$f(U)\subseteq V$$인 $$x$$의 근방 $$U$$가 존재한다는 조건은, $$\varepsilon$$-$$\delta$$ 정의를 근방 언어로 번역한 것이라는 직관이 자연스럽다. 그런데 정의 자체는 "근방을 근방으로 보내는 것"이므로, 거리 개념 없이도 적용 가능하다는 점이 위상학적 사고의 핵심을 보여준다. $$f^{-1}(V)$$가 $$x$$의 근방이 된다는 동치 조건—함수의 pullback이 근방을 보존한다는 것—은 선형대수에서 선형사상이 부분공간을 부분공간으로 보내는 것과 비슷한 느낌을 준다.

명제 2의 $$x\in\cl(A)\implies f(x)\in\cl(f(A))$$는 연속함수가 "접근 가능성"을 보존한다는 것을 말해준다. 증명에서 $$f^{-1}(V)\cap A\neq\emptyset$$에서 $$V\cap f(A)\neq\emptyset$$를 얻는 부분은 간결하면서도, closure의 근방 characterization이 얼마나 실용적인지를 다시 한번 확인시켜준다. 명제 3의 합성 연속성—$$g\circ f$$의 근방 $$W$$에 대해 $$g^{-1}(W)$$를 $$f(x)$$의 근방으로, $$f^{-1}(g^{-1}(W))$$를 $$x$$의 근방으로 단계적으로 가져가는 것—은 대수에서 homomorphism의 합성도 homomorphism이라는 것과 완전히 병행된다. 집합론의 $$(g\circ f)^{-1}=f^{-1}\circ g^{-1}$$라는 식이 증명의 핵심이라는 점에서, 앞서 배운 집합론의 함수 이론이 위상에서 그대로 살아있다.

정리 4의 네 동치 조건이 가장 풍성한 부분이다. 점별 연속 → closure 보존 → 닫힌집합의 원상이 닫힌집합 → 열린집합의 원상이 열린집합 — 이 네 조건이 동치라는 것은, "연속성"이라는 개념이 관점에 따라 완전히 다른 얼굴을 가질 수 있다는 것을 보여준다. 특히 2→3 증명에서 $$f(\cl(f^{-1}(C)))\subseteq\cl(f(f^{-1}(C)))\subseteq\cl(C)=C$$라는 포함 사슬을 보고 $$\cl(f^{-1}(C))\subseteq f^{-1}(C)$$를 얻는 전략은, closure 연산의 단조성을 $$f$$와 $$f^{-1}$$ 사이에서 번갈아 적용하는 것이어서 인상적이었다. 4→1 증명에서 열린근방 $$V'$$의 원상 $$f^{-1}(V')$$가 열린근방이 된다는 것—공리 4가 "원상이 열린"이라는 조건을 제공하고, 이것이 바로 근방 조건을 만족시킨다는 연결—은 각 동치 조건이 왜 유용한지를 체감하게 해준다.

$$f^{\mathcal{T}}:\mathcal{T}_Y\rightarrow\mathcal{T}_X$$라는 유도 함수를 정의한 부분은, 연속함수가 위상 구조 사이의 "함수"를 유도한다는 관점을 제시하는데, $$f$$가 전단사일 때 $$f^{\mathcal{T}}$$는 단사라는 것—서로 다른 열린집합의 원상이 서로 다르다는 것—은 자연스럽다. 예시 5의 discrete→trivial 항등함수는 $$f^{\mathcal{T}}$$가 전사가 될 수 없다는 것을 보여주는데, $$\mathcal{T}_2$$의 원소가 두 개뿐($$\emptyset$$와 $$\mathbb{N}$$)이고 $$\mathcal{T}_1$$의 원소가 $$2^{\mathbb{N}}$$개이므로 단사 함수의 공역과 정의역의 크기 차이로 전사가 불가능하다는 것이 명확하다. 이 예시가 homeomorphism의 정의 6으로 자연스럽게 이어지는 구조—"역함수도 연속이면 $$f^{\mathcal{T}}$$가 전단사가 된다"는 것—는 논리적으로 깔끔하다.

정의 6의 homeomorphism은 "집합으로서 bijection + 열린집합을 정확히 같은 방식으로 행동"이라는 것이고, 이전 글에서 정의한 위상의 동치 정의들—closure operator, neighborhood filter 등—이 homeomorphism 하에서 보존됨을 짐작할 수 있다. 전체적으로 이 글은 "위상구조를 보존하는 함수"라는 대수적 관점을 위상에 적용한 것으로, homomorphism → isomorphism 패턴이 continuous function → homeomorphism으로 그대로 옮겨온다는 점이 가장 큰 통찰이다.

## [Initial topology와 final topology](/ko/math/topology/initial_and_final_topology)

이 글은 "주어진 함수들을 연속하게 만드는 위상"이라는 관점에서 위상을 *construct*하는 두 가지 방법—initial topology와 final topology—을 다룬다. 정의 1에서 initial topology를 "함수들 $$f_i:X\rightarrow Y_i$$를 모두 연속으로 만드는 $$X$$ 위의 가장 약한 위상"으로 정의하는데, "가장 약한 위상"이라는 말이 핵심이다. 열린집합을 최소한으로 넣어서 연속성만 보장하자는 것이고, discrete topology가 항상 후보로 존재한다는 관찰—모든 함수가 연속이니까—은 존재성 자체는 자명하지만 구체적인 구조를 알기 위해서는 더 노력이 필요하다는 것을 보여준다.

명제 2에서 initial topology의 구체적 구조가 드러난다: $$\mathcal{S}=\{f_i^{-1}(U_i)\mid U_i \text{ open in } Y_i\}$$를 subbase로 하여 생성된 위상이라는 것이다. 이는 열린집합의 원상은 열려야 한다는 연속성의 정의에서 $$f_i^{-1}(U_i)$$꼴의 집합을 반드시 포함해야 한다는 필요조건이 곧 충분조건이 된다는 결론인데, 기저 글에서 봤던 "기저로부터의 위상 구성" 패턴이 다시 쓰이고 있다. $$\mathcal{S}$$가 subbase이지 base가 아닌 이유—유한 교집합을 취해야 base가 된다—는 $$f_i^{-1}(U_i)\cap f_j^{-1}(U_j)$$꼴의 집합도 포함해야 하기 때문인데, 이 유한 교집합 조건이 initial topology의 "유한성"을 결정한다는 것이 흥미롭다.

명제 3의 universal property가 이 글의 개념적 핵심이다: $$g:Z\rightarrow X$$가 연속인 것은 각 $$f_i\circ g$$가 연속인 것과 동치라는 것이다. 범주론 노트에서 봤던 universal property의 패턴—"임의의 대상에서 이 구조로의 사상은 성분별 조건으로 결정된다"—이 여기서 정확히 작동한다. 증명에서 $$g^{-1}(U)=g^{-1}(\bigcap f_j^{-1}(U_j))=\bigcap(f_j\circ g)^{-1}(U_j)$$라는 등식이 핵심인데, 원상이 교집합을 보존한다는 집합론의 기본 성질이 증명을 완성한다. initial topology가 "가장 약한 위상"이라는 것이 universal property에서 "필요한 것만 넣었다"는 것으로 번역되는 구조가 깔끔하다.

final topology는 정확히 dual 방향으로 정의된다: $$f_i:Y_i\rightarrow X$$들이 모두 연속이도록 하는 $$X$$ 위의 가장 강한 위상. initial topology에서는 "가장 약한 것이 유일하게 존재"했지만, final topology에서는 "가장 강한 것이 유일하게 존재"한다는 것이 대칭적이다. 그런데 존재성 증명이 initial topology와 다르게 자명하지 않다—위상의 합집합이 일반적으로 위상이 아니기 때문인데, 명제 5에서 $$\mathcal{T}_\fin=\{U\subseteq X\mid f_i^{-1}(U) \text{ open in } Y_i \text{ for all } i\}$$로 직접 정의하여 이 문제를 우회한다. 이 정의가 "모든 $$f_i$$의 원상이 열려야 한다"는 조건을 한꺼번에 검사하는 것인데, $$U$$ 자체가 위상인지 확인하는 과정이 $$\mathcal{T}_\fin$$의 정의에 이미 내장되어 있다는 점이 영리하다.

명제 6의 universal property도 dual이다: $$g:X\rightarrow Z$$가 연속인 것은 각 $$g\circ f_i$$가 연속인 것과 동치. initial topology의 universal property(명제 3)와 나란히 놓으면 "initial은 합성으로 검사, final도 합성으로 검사"인데 방향만 반대라는 것이 명확하다. 범주론에서 initial object와 terminal object의 universal property가 정확히 이 구조인데, topology 맥락에서 이 패턴이 구체적으로 살아있다.

전체적으로 이 글은 "위상을 만드는 방법"이라는 관점을 제시한다. 앞선 글들이 "주어진 위상을 분석하는 도구"—열린집합, 기저, closure, 연속함수—였다면, 이 글은 "함수들로부터 위상을 construct"하는 방향으로 초점을 옮긴다. universal property가 두 construction 모두에서 등장한다는 것은, 이 글이 범주론적 사고의 topology 적용이라는 것을 보여준다. discrete topology와 trivial topology가 initial/final topology의 극단적 예시로 다시 등장하는 것도—"모든 함수를 연속하게 만드는 가장 약한/강한 위상"이라는 관점—이전 글들의 개념이 새로운 맥락에서 재해석되는 느낌이다.

## [부분공간](/ko/math/topology/subspaces)

이 글은 "큰 공간의 위상을 작은 집합에 제한하면 어떻게 되는가"라는 질문을 다룬다. 정의 1에서 부분위상을 inclusion $$\iota:A\hookrightarrow X$$에 대한 initial topology로 정의하는데, 앞서 Initial topology 글에서 다룬 universal property가 여기서 바로 적용된다는 점이 인상적이다. $$\mathcal{T}_A=\{U\cap A\mid U\in\mathcal{T}\}$$라는 공식은 $$X$$의 열린집합을 $$A$$와 교집합 취하는 것뿐인데, 이 간단한 연산이 위상의 세 공리를 모두 만족한다는 것이 initial topology의 존재성 정리로 자동으로 보장된다. "Initial topology"라는 용어 자체가 이 글에서 처음 사용되는데, 이전 Initial topology 글의 정의 1에서 도입된 개념이므로 문제는 없다.

부분공간에서 가장 주의해야 할 점—"$$A$$에서 열린집합이 $$X$$에서도 열린집합은 아니다"—은 보조정리 2와 3으로 깔끔하게 처리된다. $$A$$가 $$X$$에서 열린(resp. 닫힌)집합이면 $$A$$의 모든 열린(resp. 닫힌)집합이 $$X$$에서도 열린(resp. 닫힌)집합이라는 동치 조건은, $$A$$의 위상적 "지위"가 부분공간의 성질을 결정한다는 직관을 준다. 보조정리 4의 근방 버전—$$A$$가 $$x$$의 근방이면 $$A$$에서의 근방이 $$X$$에서의 근방이 된다—은 이후 연속함수의 부분공간 제한을 다룰 때 핵심적으로 쓰인다.

명제 5의 closure 공식 $$\cl_BA=B\cap\cl_XA$$는 $$X$$에서의 closure 정보만으로 $$B$$의 부분공간에서의 closure를 얻을 수 있다는 점에서 효율적이다. $$A$$가 $$B$$에서 dense라는 것이 $$B\subseteq\cl_XA$$와 동치라는 결론은, dense의 개념이 전체 공간이 아니라 상대적인 것임을 명확히 해준다.

명제 6의 paste lemma—$$(A_i)$$가 $$X$$의 열린 덮개이거나 locally finite인 닫힌 덮개이면, $$f:X\rightarrow Y$$의 연속성이 각 $$f\vert_{A_i}$$의 연속성과 동치—는 "국소적으로 확인한 연속성이 전체로 올라간다"는 원리의 구체적 형태이다. $$X=\bigcup\interior(A_i)$$인 경우 각 $$B\cap\interior A_i$$가 $$X$$에서 열린집합이라는 보조정리 2가 증명의 핵심이고, locally finite인 닫힌 덮개인 경우 $$B\cap A_i$$가 $$X$$에서 닫힌집합이라는 보조정리 3이 핵심이다. 이 두 조건이 왜 필요한지를 증명에서 직접 확인할 수 있어서 좋았다. 이 원리가 이후 층(sheaf) 이론에서 "local data가 global data를 결정한다"는 패턴으로 일반화될 것이라는 예감이 든다.

전체적으로 이 글은 "위상을 부분집합으로 제한하는 것"이라는 자연스러운 작업을 initial topology의 틀 안에서 처리하고, 이 제한이 연속함수와 어떻게 상호작용하는지를 다룬다. 앞서 Initial topology 글이 "위상을 만드는 방법"이었다면, 이 글은 "만들어진 위상을 smaller setting으로 옮기는 방법"이라는 점에서 자연스러운 후속이다. 다만 이 글에서 "열린사상(open mapping)"이라는 용어가 정의 없이 사용되었다.

## [준층](/ko/math/topology/presheaves)

준층(presheaf)의 정의—$$\Open(X)^\op$$에서 $$\Set$$으로의 contravariant functor—는 범주론 노트에서 다룬 functor의 개념이 위상의 맥락에서 구체적으로 살아있는 첫 번째 본격적인 예시다. $$\Open(X)$$를 열린집합들의 포함관계로 만든 순서집합(ordered set)의 범주로 보고, inclusion $$U\hookrightarrow V$$에 대응하는 restriction map $$\rho_{VU}:\mathscr{F}(V)\rightarrow\mathscr{F}(U)$$을 부여한다는 것은, "큰 열린집합 위의 데이터를 작은 열린집합으로 제한한다"는 직관을 범주론적 언어로 번역한 것이다. $$\rho_{WU}=\rho_{VU}\circ\rho_{WV}$$라는 합성 보존 조건은 functor 정의의 일부이므로 자연스럽고, contravariant이므로 화살표 방향이 뒤집힌다는 점이 핵심이다.

예시 3의 연속함수들의 준층—$$\mathscr{F}(U)=\Hom_\Top(U,Y)$$에 restriction map을 부여한 것—이 가장 직관적인 예다. 이 예시가 "큰 공간에서 정의된 함수를 작은 열린집합으로 제한하면 어떻게 되는가"라는 질문을 정확히 formalize하고 있는데, Gluing lemma(보조정리 1)와 직결된다. Gluing lemma 자체는 부분공간 글의 paste lemma를 "거꾸로" 읽은 것—locally finite closed covering이나 open covering 위에서의 연속함수들이 호환되면 전체로 확장 가능하다—인데, 이것이 준층 이론의 출발점이 된다는 점이 인상적이다. 특히 "열린집합마다 정의된 데이터를 어떻게 전체 공간으로 결합(glue)하는가"라는 질문이 이후 sheaf에서 핵심적으로 다루어질 것이라는 예감이 든다.

정의 4의 section과 restriction map의 용어 체계—$$\mathscr{F}(U)$$의 원소를 section, $$\rho_{VU}(s)$$를 $$s\vert_U$$로 표기—는 함수의 restriction이라는 익숙한 개념을 추상화한 것이어서 따라가기 좋다. projection $$p:Y\rightarrow X$$의 continuous section들의 모임이라는 관점(정의 4 직전의 논의)이 동기를 잘 제공하는데, 집합론 노트에서 정의한 section의 개념이 여기서 위상적으로 활용되고 있다는 연결이 자연스럽다.

준층의 값이 $$\Set$$ 대신 $$\Ab$$나 $$\Ring$$ 같은 다른 범주에서 취할 수 있다는 관찰(정의 2 이후의 논의)은, 범주론 노트에서 다룬 $$\mathcal{A}$$-valued functor의 개념이 그대로 적용됨을 보여준다. $$\PSh(X,\Ab)$$가 $$\Ab$$의 monoidal structure를 물려받는다는 것—특히 monoidal object가 $$\Ring$$-valued presheaf—은 범주론의 Monoidal Categories, Monoid Objects 글에서 다룬 내용이 위상 맥락에서 구체화되는 좋은 예다. 다만 "monoidal product"라는 용어가 이 글에서 정의 없이 사용되었다.

Skyscraper sheaf(예시 5)와 constant presheaf(예시 6)는 각각 "한 점에 집중된 정보"와 "공간 전체에 균일한 정보"라는 극단적인 예시로, presheaf의 유연성을 보여준다. $$\mathscr{F}\vert_U$$의 restriction(예시 7)과 pushforward $$f_\ast\mathscr{F}$$(예시 8)는 presheaf들 사이의 사상을 만드는 자연스러운 방법들인데, $$f_\ast\mathscr{F}(U)=\mathscr{F}(f^{-1}(U))$$라는 정의가 연속함수의 원상이라는 위상의 기본 도구를 사용한다는 점이 깔끔하다.

정의 9의 stalk—$$\mathscr{F}_x=\varinjlim_{x\in U}\mathscr{F}(U)$$—는 범주론의 Limits 글에서 정의한 colimit(구체적으로 direct limit)이 여기서 핵심적으로 사용되는 지점이다. 동치관계 $$(s,U)\sim(t,V)\iff\exists W\subseteq U\cap V$$에서의 합의—는 "점 $$x$$ 근방에서 두 section이 일치하면 같은 germ으로 본다"는 직관을 정확히 formalize한다. 함수의 미분이라는 예시(각주 1—$$f'(x)$$는 $$x$$의 아주 작은 근방에서의 정보)가 stalk의 동기를 잘 제공한다. $$\Spe(\mathscr{F})$$에 final topology를 부여해서 étalé space를 만드는 구성은, Initial topology 글에서 다룬 final topology의 또 다른 응용인데, "presheaf를 기하학적 대상으로 바라보는 관점"을 제시한다는 점에서 흥미롭다.

정의 10의 presheaf morphism—$$\Open(X)^\op$$ 위의 natural transformation—은 범주론의 Natural Transformations 글에서 정의한 개념이 functor category $$[\Open(X)^\op,\mathcal{A}]$$ 위에서의 사상으로 해석되는 것이다. $$\phi\vert_U$$라는 표기가 restriction map과의 유추에서 비롯된다는 설명이 좋다. 명제 11에서 stalk 사이의 morphism $$\phi_x:\mathscr{F}_x\rightarrow\mathscr{G}_x$$가 유도된다는 것은, limit cone의 universal property로 자동으로 따라오는 결론인데, 범주론적 도구가 얼마나 효율적인지를 체감하게 해준다.

가환준층(abelian presheaf) 부분은 $$\PSh(X,\Ab)$$이 abelian category가 된다는 것을 보여준다. 정의 16의 presheaf kernel—$$U\mapsto\ker(\phi(U))$$—의 restriction map이 universal property로 유일하게 결정된다는 것이 깔끔하고, presheaf cokernel·image·coimage도 같은 방식으로 정의할 수 있다는 관찰은 Abelian Categories 글에서 다룬 abelian category의 조건들이 여기서 확인됨을 보여준다.

전체적으로 이 글은 "열린집합마다 대수적 데이터를 부여한다"는 아이디어를 functor의 언어로 formalize하면서, 동시에 gluing이라는 기하학적 직관을 제공한다. 앞선 글들이 위상공간 자체를 분석하는 도구—열린집합, 기저, closure, 연속함수, initial/final topology—였다면, 이 글은 "위상공간 위에 올려진(extra) 데이터"를 다루는 첫 단계이다. 범주론에서 배운 functor, natural transformation, colimit, abelian category라는 도구들이 여기서 한꺼번에 동원된다는 것이, 앞서 다룬 추상적 기초가 얼마나 실용적인지를 보여준다.

## [층](/ko/math/topology/sheaves)

층(sheaf)의 정의는 준층에 두 가지 추가 조건—identity axiom과 gluability axiom—을 부여한 것이다. identity axiom은 "국소적으로 일치하면 전체적으로 같다"는 것이고, gluability axiom은 "국소적으로 호환되는 데이터를 전체로 결합할 수 있다"는 것인데, 둘 다 준층 글의 보조정리 1(gluing lemma)에서 이미 본 아이디어를 공리화한 것이다. 준층이 "열린집합마다 데이터를 부여하는 것"이라면, 층은 "그 데이터가 실제로 국소-전역 원리를 만족하는 것"이라는 구분이 핵심이다. 이 두 조건이 왜 필요한지를 gluing lemma의 반례—locally finite closed covering이 아닌 상황에서 연속함수들이 호환되어도 전체로 확장 불가능한 경우—로 짐작할 수 있다.

명제 2의 주된 결과—$$\mathscr{F}(U)\rightarrow\prod_{x\in U}\mathscr{F}_x$$가 단사함수—는 "section은 stalk들에 의해 결정된다"는 강한 결론이다. 증명에서 stalk의 정의($$s_x=t_x$$이면 어떤 $$V_x\subseteq U$$에서 $$s\vert_{V_x}=t\vert_{V_x}$$)와 identity axiom을 조합하는 구조가 깔끔하다. 이 결과의 의미는 "연속함수의 경우, 모든 점에서 함숫값이 같으면 함수 자체가 같다"는 것이고, 위상에서 국소 정보가 얼마나 강력한지를 보여준다. 다만 역—임의의 stalk들을 골라서 section을 만들 수 있다—은 성립하지 않는데, 그 이유는 호환성 조건이 필요하기 때문이다.

정의 3의 compatible germs 개념이 이 글의 핵심 도구다. 각 점 $$x$$에서 대표원 $$\tilde{s}_x$$를 고르고, 근방 $$V_x$$에서의 값들이 다른 점의 stalk과 일치해야 한다는 조건은, "국소적으로 정의된 데이터들이 겹치는 영역에서 모순 없이 합쳐질 수 있다"는 것을 formalize한 것이다. presheaf의 gluability axiom이 실패하는 이유는 바로 이 호환성 검사를 통과하더라도 전체 section이 존재하지 않을 수 있기 때문이고, sheafification이 이 문제를 해결하는 도구가 된다.

보조정리 6의 sheafification—$$(-)^\dagger:\PSh(X,\Set)\rightarrow\Sh(X,\Set)$$의 존재—은 compatible germ들의 presheaf를 직접 구성하는 것으로 증명된다. $$\mathscr{F}^\dagger(U)$$를 compatible한 germs $$(s_x)_{x\in U}$$의 모임으로 정의하면, gluability axiom은 "함수들의 presheaf"이므로 자동으로 만족된다는 것이 영리하다. universal property의 증명—각 점에서의 호환 데이터를 $$\phi$$를 통해 옮겨서 다시 붙이는 것—은 범주론의 adjunction 개념이 구체적으로 작동하는 좋은 예시다. $$\mathscr{F}$$가 이미 sheaf이면 $$\mathscr{F}\rightarrow\mathscr{F}^\dagger$$가 isomorphism이라는 관찰은, sheafification이 "이미 좋은 구조를 망치지 않는다"는 것을 보장해준다.

정의 5 이후의 논의—$$\Sh(X,\mathcal{A})$$에서의 kernel, image, cokernel 정의—는 준층 글에서 presheaf의 가환범주 구조를 다룬 것의 자연스러운 후속이다. presheaf kernel은 sheaf kernel이 되지만, presheaf image와 cokernel은 일반적으로 sheaf가 아니므로 sheafification을 적용해야 한다는 것은, "가환범주의 조건을 만족하려면 sheafification이라는 추가 작업이 필요하다"는 것을 의미한다. homological algebra 노트에서 다룬 abelian category의 조건들이 sheaf category에서도 확인된다는 결론은, 추상적 대수 도구가 위상의 맥락에서도 유효하다는 것을 보여준다.

명제 8의 "기저 위에 정의된 층"은 실용적으로 매우 중요한 결과다. 전체 위상의 모든 열린집합 위에서 sheaf를 정의하지 않아도, 기저의 원소들 위에서 identity axiom과 gluability axiom만 확인하면 sheaf로 유일하게 확장된다는 것은, 실제로 sheaf를 구성할 때 큰 절약을 제공한다. 준층 글에서 기저로부터 위상을 구성하는 것과 완전히 병행되는 패턴인데, "기저만 알면 전체를 복원할 수 있다"는 원리가 위상 구조와 위상 위의 데이터 모두에 적용된다는 것이 인상적이다.

명제 4의 동치—$$\phi$$가 isomorphism ↔ 모든 $$\phi_x$$가 isomorphism—는 이 글에서 가장 강력한 결과다. stalk 레벨에서 검사하기만 하면 sheaf morphism의 동치를 판별할 수 있다는 것은, stalk가 얼마나 효율적인 도구인지를 보여준다. 증명의 구조—injectivity는 identity axiom으로, surjectivity는 gluability axiom으로 각각 처리—가 두 공리가 왜 정확히 이 조건들인지를 체감하게 해준다. 준층 글에서 stalk를 colimit으로 정의한 것이 여기서 결실을 맺는 느낌이다.

정의 10의 inverse image sheaf—$$f^{-1}$$는 $$f_\ast$$의 left adjoint—는 범주론의 adjunction 패턴이 위상에서 또 한번 등장하는 것이다. $$f^{-1}_\text{pre}\mathscr{G}(U)=\varinjlim_{V\supseteq f(U)}\mathscr{G}(V)$$로 presheaf를 정의한 뒤 sheafification하는 구성은, direct limit의 universal property와 sheafification의 universal property가 겹겹이 쌓인 구조인데, 범주론적 도구의 효율성을 체감하게 해준다. 예시 14의 extension by zero—$$j_{!,\text{pre}}$$는 일반적으로 sheaf가 아니므로 sheafification이 필요하다—는 "자연스럽게 보이는 presheaf도 gluability axiom을 만족하지 않을 수 있다"는 좋은 반례다. $$\mathbb{R}^1\setminus\{0\}$$ 위의 constant sheaf $$\underline{\mathbb{Z}}$$를 $$\mathbb{R}^1$$로 확장하려 할 때 gluing이 실패하는 예시가 특히 인상적인데, "두 점에서 같은 값이어도 사이에서 연결할 수 없다"는 직관을 정확히 포착한다.

전체적으로 이 글은 "준층 중에서 국소-전역 원리를 만족하는 것"을 가려내는 작업을 다룬다. 준층 글이 "열린집합마다 데이터를 부여하는 functor"라는 관점을 제시했다면, 이 글은 "그 functor가 실제로 유용한가?"라는 질문에 답한다. sheafification, stalk에 의한 판별, 기저 위의 정의라는 세 가지 도구가 모두 "국소 데이터와 전역 데이터의 관계"라는 하나의 주제를 향해 수렴한다. 다만 étalé space라는 용어가 준층 글에서 정의되었지만 이 글에서 직접 다루지 않아서, $$\Spe(\mathscr{F})$$의 기하학적 의미를 떠올리려면 준층 글로 돌아가야 한다.

⚠️ 정의 없이 사용: `open embedding` (준층 글 예시 3에서 언급되었으나 명시적 정의 없음)

## [몫공간](/ko/math/topology/quotient_spaces)

몫공간의 핵심 아이디어—"동치관계로 점들을 합친 집합 위에 위상을 주자"는 것—은 final topology의 자연스러운 적용이다. 정의 1의 locally closed라는 개념부터 새로웠다. "$$A$$가 $$x$$에서 locally closed라는 것은 $$x$$의 근방 $$V$$가 있어 $$A\cap V$$가 $$V$$에서 닫힌집합"이라는 정의는, "국소적으로는 닫힌집합이지만 전체적으로는 아닐 수 있다"는 상황을 포착하는 것인데, 명제 2의 동치 조건—열린집합과 닫힌집합의 교집합, 또는 자기 closure에서 열린—이 이 개념의 실체를 명확히 해준다. $$A=U\cap\cl A$$라는 characterization은 "closure를 취하면 $$A$$ 밖의 점들이 붙는데, $$U$$로 잘라내면 다시 $$A$$가 된다"는 이미지로 이해할 수 있다.

몫공간의 정의 3은 canonical projection $$p:X\rightarrow X/R$$에 대한 final topology로, Initial topology 글의 dual construction이 여기서 구체적으로 살아있다. $$X/R$$의 열린집합이 $$p^{-1}(U)$$가 $$X$$에서 열린 $$U$$에 대응된다는 것은, 집합론에서 다룬 saturated subset의 관점에서 "equivalence class를 통째로 포함하거나 통째로 배제하는 열린집합"만 허용한다는 것인데, 이 제한이 quotient topology의 본질이라는 직관이 잡혔다.

명제 4의 universal property—$$f:X/R\rightarrow Y$$가 연속인 것은 $$f\circ p$$가 연속인 것과 동치—는 final topology의 universal property(Initial topology 글 명제 6)를 그대로 specialized한 것이다. 이전 글들에서 반복적으로 봤던 "합성으로 검사한다"는 패턴이 또 한번 등장하는데, 범주론적 사고가 위상 전반에 얼마나 깊이 스며들어 있는지를 체감하게 해준다.

명제 5는 동치관계의 세분화와 몫공간의 관계를 다루는데, $$S$$가 $$R$$보다 세밀하면 $$(X/S)/(R/S)\cong X/R$$라는 결론은 집합론에서 봤던 "동치관계를 단계적으로 합치는 것과 한꺼번에 합치는 것이 같다"는 것이 위상적으로도 성립한다는 것이다. 증명이 universal property를 두 번 적용하는 구조—$$X\rightarrow X/S\rightarrow (X/S)/(R/S)$$와 $$X\rightarrow X/R$$의 연속성—으로 되어 있어서, 앞서 익힌 도구들이 증명의 각 단계를 뒷받침하는 느낌이 좋았다.

명제 6의 canonical decomposition $$X\overset{p}{\longrightarrow}X/R\overset{\bar{f}}{\longrightarrow}f(X)\overset{i}{\longrightarrow}Y$$에서 $$\bar{f}$$가 homeomorphism이 되는 조건—saturated인 열린(또는 닫힌)집합의 상이 $$f(X)$$에서 열린(또는 닫힌)—은 "몫공간으로 collapsing해도 정보가 손실되지 않는 정확한 조건"을 말해주는 것인데, 이 조건이 $$\bar{f}^{-1}$$의 연속성과 동치라는 것이 깔끔하다. 연속인 section $$s:Y\rightarrow X$$가 존재하면 $$\bar{f}$$가 homeomorphism이 된다는 관찰—$$f\circ s=\id_Y$$에서 $$p\circ s$$가 $$\bar{f}$$의 역함수 역할을 한다—은 "역함수가 존재하면 구조가 보존된다"는 기본 원리의 자연스러운 적용이다.

전체적으로 이 글은 "동치관계로 공간을 collapsing하는 것"이라는 대수적 작업에 위상을 부여하는 방법을 다루고, 그 결과인 몫공간이 원래 공간과 어떤 관계를 가지는지를 universal property와 canonical decomposition으로 분석한다. 부분공간이 "위상을 제한하는 것"이었다면, 몫공간은 "위상을 collapsing하는 것"인데, 둘 다 initial/final topology라는 같은 틀 안에서 처리된다는 것이 이 카테고리의 일관된 주제이다. 다만 이 글에서 "section"이라는 용어가 $$f\circ s=\id_Y$$인 함수를 가리키는 것으로 사용되었는데, 이전 글들에서 정의된 적 없는 개념이다.

## [곱공간](/ko/math/topology/product_spaces)

곱공간의 정의—$$\pr_i:X\rightarrow X_i$$들에 대한 initial topology—는 Initial topology 글의 framework를 그대로 적용한 것이다. $$\mathcal{S}=\{\pr_i^{-1}(U_i)\mid U_i \text{ open in } X_i\}$$를 subbase로 하고, 유한 교집합을 취하면 base가 되는데, 그 원소들이 "유한 개 좌표만 $$X_i$$가 아닌 진부분집합이고 나머지는 $$X_i$$ 자체인 곱집합"이라는 것은 $$\pr_i^{-1}(U_i)$$의 유한 교집합이 정확히 그런 꼴이기 때문이다. "box topology"와의 차이—무한 곱에서 box topology는 모든 좌표의 열린집합을 허용하지만 product topology는 유한 개만 허용—는 이 글에서 직접 다루지 않지만, base의 정의에서 "finitely many $$i$$" 조건이 왜 들어가는지를 생각하면 자연스럽게 떠오른다.

명제 2의 universal property—$$f=(f_i):Y\rightarrow X$$가 연속 ↔ 각 $$f_i$$가 연속—는 Initial topology 글 명제 3의 직접적인 specialized version이다. 이전 글들에서 반복적으로 봤던 "합성으로 검사" 패턴이 곱공간에서도 정확히 작동한다는 것이, initial topology라는 도구의 일관성을 보여준다. 따름정리 3—$$f:(x_i)\mapsto (f_i(x_i))$$의 연속성이 성분별 연속성과 동치—은 이 universal property의 가장 실용적인 형태인데, 곱공간 위의 함수를 "성분별로 분해해서 각각 검사"할 수 있다는 것이 이후 응용에서 핵심적으로 쓰일 것이라는 예감이 든다.

따름정리 4—$$f$$가 연속 ↔ $$g:x\mapsto (x,f(x))$$가 $$X$$에서 $$\Gamma(f)$$로의 homeomorphism—는 그래프라는 개념을 위상적으로 활용한 것이다. $$g$$의 역함수가 $$\pr_X\vert_{\Gamma(f)}$$라는 관찰은 간결하면서도, "연속함수의 그래프는 함수 자체와 위상적으로 동일한 정보를 담고 있다"는 직관을 formalize한다. $$f$$가 상수함수일 때 $$X\cong X\times\{y_0\}$$가 된다는 결론은 자명해 보이지만, 이 사실이 명제 5와 명제 6의 증명에서 핵심적으로 쓰인다는 것을 알 수 있다.

명제 5—$$\pr_X(U)$$와 $$\pr_Y(U)$$가 열린집합—은 "투사가 열린집합을 열린집합으로 보낸다"는 성질인데, $$\pr_X(U)=\bigcup_{y\in Y}U(y)$$라는 식과 따름정리 4의 $$U(y_0)$$가 열린집합이라는 관찰이 조합되어 증명이 완성된다. 그런데 닫힌집합에 대해서는 이 결론이 성립하지 않는다는 관찰—닫힌집합의 임의 합집합이 닫히지 않을 수 있기 때문—은 "열린"과 "닫힌"이 곱공간 위에서 대칭적으로 행동하지 않는다는 것을 보여준다. 이 비대칭성은 이후 Hausdorff 공간이나 compact 공간을 다룰 때 더 중요한 의미를 가질 것 같다.

명제 6—$$f(x_1,a_2)$$와 $$f(a_1,x_2)$$가 각각 점에서 연속—은 "곱공간 위의 함수를 한 변수씩 고정하면 연속"이라는 성질인데, 이 글에서 "역은 성립하지 않는다"고 명시하고 있다. 이 관찰은 "따로따로 연속"이 "함께 연속"을 함의하지 못한다는 것이고, product topology의 base가 "유한 개 좌표만 변하는" 집합이기 때문이라는 직관이 든다. $$\varepsilon$$-$$\delta$$ 세계에서는 "따로따로 연속"과 "함께 연속"이 다른 개념이라는 것을 이미 알고 있었지만, 위상의 언어로 이 차이를 정확히 포착하는 것이 인상적이다.

내부와 폐포의 곱에 대한 성질은 대비가 뚜렷하다. 명제 7—$$\prod\cl A_i=\cl(\prod A_i)$$—는 임의의 index set에 대해 성립하지만, 명제 8—$$\prod\interior A_i=\interior(\prod A_i)$$—은 $$I$$가 유한일 때만 성립한다. 폐포는 "근방과 만나는 점"이라는 characterization 덕분에 좌표별로 접근 가능하지만, interior는 "근방이 포함된다"는 조건이 무한 개 좌표에서 동시에 만족되어야 하므로 유한성이 필요하다는 것이 차이의 원인으로 보인다. 이 비대칭성은 closure와 interior가 본질적으로 다른 연산이라는 것을 다시 한번 상기시켜준다.

전체적으로 이 글은 "곱집합 위에 위상을 주는 것"이라는 자연스러운 작업을 initial topology의 틀 안에서 처리하고, 그 결과로 얻어진 곱공간 위의 연속함수·투사·내부·폐포의 성질을 다룬다. Initial topology 글이 "위상을 만드는 방법"을 제시했다면, 이 글은 그 방법의 가장 중요한 응용 중 하나를 보여주는 것이다. 다만 이 글에서 "graph"라는 용어가 $$\Gamma(f)=\{(x,f(x))\mid x\in X\}$$로 정의되어 사용되었는데, 집합론에서 graph의 개념이 다뤄졌는지는 확인이 필요하다.

## [열린사상과 닫힌사상](/ko/math/topology/open_mappings_and_closed_mappings)

이 글은 연속함수의 반대편—함수가 열린집합이나 닫힌집합을 어떻게 "보내는가"—를 다룬다. 정의 1에서 open mapping을 "열린집합의 상이 열린집합", closed mapping을 "닫힌집합의 상이 닫힌집합"으로 정의하는데, 연속함수가 "원상"으로 위상구조를 보존하는 것과 대비하여 open/closed mapping은 "상"으로 구조를 보존한다는 점에서 방향이 정확히 반대이다. 이 대비—연속은 pullback, open/closed는 pushforward—는 선형대수에서 선형사상과 그 전치(transpose)의 관계를 떠올리게 한다.

명제 2의 합성에 대한 성질 중 둘째와 셋째가 흥미롭다. $$g\circ f$$가 open이고 $$f$$가 continuous surjection이면 $$g$$가 open이라는 것—증명에서 $$f(f^{-1}(V))=V$$라는 전사성의 활용이 핵심—과, $$g$$가 continuous injection이면 $$f$$가 open이라는 것—$$g^{-1}(g(f(U)))=f(U)$$라는 단사성의 활용이 핵심—은 surjection과 injection이 각각 "어느 방향으로 정보를 전달하는가"에 따라 openness가 어떻게 전파되는지를 보여준다. 집합론의 retraction/section 정의가 증명에서 직접 쓰이고 있다는 점에서, 앞서 배운 도구들이 위상에서 그대로 살아있다.

명제 3의 둘째 결과—locally finite closed covering이나 interior로 이루어진 open covering의 조각들에서 각 제한이 open이면 전체도 open—는 부분공간 글의 paste lemma와 완전히 같은 패턴인데, "locally 확인한 성질이 전체로 올라간다"는 원리가 open/closed mapping에서도 작동한다는 것을 보여준다. 부분공간에서의 제한이 open을 보존한다는 첫째 결과도 자연스럽다.

동치관계에 대한 정의 4—"$$R$$이 open이라는 것은 canonical map $$X\rightarrow X/R$$이 open"—는 quotient space 글의 정의와 자연스럽게 연결된다. 명제 5의 canonical decomposition $$X\overset{p}{\longrightarrow}X/R\overset{h}{\longrightarrow}f(X)\overset{i}{\longrightarrow}Y$$에서, $$f$$가 open일 때 $$p$$, $$h$$, $$i$$가 모두 open이라는 동치 조건은 quotient map의 openness가 함수의 전체 구조를 결정한다는 것을 보여준다. $$h$$가 homeomorphism이고 $$f(X)$$가 $$Y$$에서 open이라는 조건은, "몫공간으로 collapsing해도 openness가 보존되는 정확한 상황"을 말해준다.

이 글은 비교적 짧고 명제 6이 비어있어서, open mapping의 구체적인 충분조건들(예: "연속 단사함수가 open이 되는 조건")을 이 글에서 직접 확인할 수 없다는 점이 아쉽다. closed mapping의 핵심 성질들을 별도로 다루지 않은 것도 동일한 한계로 느껴진다. 그래도 open/closed equivalence relation과 canonical decomposition의 연결이라는 틀은 이후 quotient space나 proper maps를 다룰 때 필수적인 도구가 될 것이라는 예감이 든다. proper maps 글(다음 글)에서 universally closed의 정의가 closed mapping을 곱공간까지 확장한 것이므로, 이 글의 내용이 바로 다음에 활용된다.

## [하우스도르프 공간](/ko/math/topology/Hausdorff_spaces)

이 글은 "점들을 충분히 분리하는 위상"이라는 주제를 다룬다. 점열의 수렴 정의 1은 미적분학의 $$\varepsilon$$-$$N$$ 정의에서 $$\varepsilon$$-ball 대신 근방 $$U$$를 사용한 것인데, 이 차이 하나로 거리 없는 공간에서도 수렴을 말할 수 있게 된다. 그런데 예시 2에서 trivial topology에서는 모든 점열이 모든 점으로 수렴한다는 것이 드러나는데, 이는 위상이 점들을 "구별하지 못하기" 때문이라는 관찰이 separation axioms의 도입 동기를 명확히 해준다.

정의 3에서 $$T_0$$부터 $$T_4$$까지, 그리고 completely regular·perfectly normal까지 총 18종의 분리공리를 한꺼번에 정의하는 것은 상당히 밀도가 높다. 이들을 "분리가능 → 근방으로 분리가능 → 닫힌근방으로 분리가능 → 연속함수로 분리가능 → 연속함수로 정확히 분리가능"이라는 강도 순서로 배열한 것이 구조를 파악하는 데 도움이 된다. $$T_0$$는 "위상적으로 구별가능"($$\mathcal{N}(x)\neq\mathcal{N}(y)$$)만 요구하고, $$T_1$$은 "분리가능"($$x\in U,\,y\not\in U$$인 열린집합 $$U$$ 존재)을 요구하며, $$T_2$$(Hausdorff)는 "서로소인 근방으로 분리가능"을 요구한다는 것이 핵심 구분이다. $$T_1$$에서 $$T_2$$로 가는 것이 실질적으로 가장 큰 도약이라는 느낌이 드는데, $$T_1$$은 "한쪽만 가리는 열린집합"이 존재하는 것이고 $$T_2$$는 "양쪽을 완전히 분리하는 열린집합 쌍"이 존재하는 것이기 때문이다.

명제 4—Hausdorff 공간에서 수렴하는 점열의 극한은 유일—은 separation axioms가 왜 필요한지를 직접 보여주는 결과다. 증명 자체는 간결하다: 두 극한 $$x,y$$의 서로소인 열린근방 $$U,V$$를 잡으면 충분히 큰 $$n$$에서 $$x_n$$이 둘 다에 속해야 하므로 모순. $$\varepsilon$$-$$\delta$$ 세계에서 "수렴의 유일성"을 당연하게 여겼었는데, 위상의 세계에서는 이 유일성이 Hausdorff 조건에 의존한다는 것이 새롭다.

보조정리 5의 diagonal characterization—$$X$$가 Hausdorff ↔ $$\Delta_X=\{(x,x)\mid x\in X\}$$가 $$X\times X$$에서 닫힌집합—는 곱공간의 성질을 통해 Hausdorff성을 재해석한 것이다. 증명에서 $$U\times V$$가 대각선과 만나지 않는 열린근방을 제공한다는 것이 핵심인데, product topology의 base가 $$U\times V$$ 꼴이라는 사실이 여기서 결정적으로 쓰인다. 이 characterization의 따름정리들—$$f,g:X\rightarrow Y$$의 일치 집합 $$E$$가 닫힌집합(따름정리 6), 그래프 $$\Gamma(f)$$가 닫힌집합(따름정리 7)—은 "Hausdorff성이 함수의 성질을 제어한다"는 관점을 보여준다. 특히 따름정리 7은 곱공간 글의 따름정리 4—$$\Gamma(f)$$가 $$X$$와 homeomorphism—과 결합하면 "Hausdorff 공간으로의 연속함수는 그래프로 완전히 기술된다"는 결론을 주는데, 이전 글들의 결과가 자연스럽게 조합되는 느낌이 좋았다.

부분공간과 곱공간에서는 Hausdorff성이 보존된다. 명제 8—$$\prod X_i$$가 Hausdorff ↔ 각 $$X_i$$가 Hausdorff—의 ($$\Leftarrow$$) 방향 증명에서, $$x_i\neq y_i$$인 좌표 하나를 골라 그곳에서 분리하는 근방을 잡고 나머지 좌표는 $$X_j$$로 놓는 것이 product topology의 base 정의와 정확히 맞아떨어진다는 것이 깔끔하다. 그런데 몫공간에서는 Hausdorff성이 보존되지 않는다는 관찰—$$R$$-saturated 열린집합으로 분리할 수 있어야 한다는 조건—은 몫공간이 원래 공간의 성질을 얼마나 파괴할 수 있는지를 보여준다. 명제 9에서 $$f(x)=f(y)$$로 정의한 동치관계에 대해 $$X/{\sim}$$이 Hausdorff라는 것은, 연속함수의 "몫"이 Hausdorff성을 안전하게 보존하는 특수한 경우를 말해준다.

전체적으로 이 글은 "점을 구별하는 위상의 힘"을 체계적으로 분류하고, Hausdorff라는 가장 중요한 분리 조건의 성질들을 다룬다. 앞서 열린집합·기저·closure가 "위상의 구조를 분석하는 도구"였다면, 이 글은 "위상의 강도를 측정하는 도구"라는 새로운 관점을 제시한다. 다만 18종의 분리공리를 한꺼번에 정의한 것이 다소 압도적이고, $$T_3$$·$$T_4$$·completely regular 등 상위 공리들의 동기와 응용이 이 글에서 충분히 설명되지 않아서, 이후 글들에서 이들이 어떻게 쓰이는지를 봐야 전체 그림이 잡힐 것 같다.

## [옹골공간](/ko/math/topology/compact_spaces)

옹골성(compactness)의 정의—"임의의 open covering에 대해 finite subcover가 존재한다"—는 Hausdorff 조건과 함께 위상에서 가장 중요한 추가 구분 기준이다. 정의 1 자체는 명확하고, 열린집합의 유한성 조건이 "공간이 너무 크지 않다"는 직관을 formalize한다는 느낌을 준다. 그런데 $$\varepsilon$$-$$\delta$$ 세계에서 "닫힌 구간 $$[a,b]$$에서의 연속함수는 최댓값을 갖는다"는 것이 compactness의 응용이라는 것을 알고 있었기 때문에, 이 공리적 정의가 실제로 그 직관을 포착하는지를 확인하고 싶었다.

명제 2는 부분공간의 compactness를 확인할 때 $$X$$의 열린집합들로 $$Y$$를 덮어도 된다는 것인데, 부분공간 글에서 $$Y$$의 열린집합이 $$U\cap Y$$ 꼴이라는 사실을 떠올리면 자연스럽다. $$Y$$의 열린집합으로 $$Y$$를 덮는 것과 $$X$$의 열린집합으로 $$Y$$를 덮는 것이 본질적으로 같다는 관찰은, 이후 증명에서 반복적으로 사용된다. 보조정리 3—compact space의 닫힌집합은 compact—의 증명에서 $$X\setminus Y$$를 covering에 추가하는 트릭은 간결하면서도 영리하다. 열린집합의 여집합이 닫힌집합이라는 기본 사실을 역이용하는 것인데, "compactness가 닫힌집합으로 잘린다"는 직관을 formalize한다.

보조정리 4와 따름정리 5가 이 글에서 가장 흥미로운 결과다. Hausdorff space에서 compact subset과 한 점을 근방으로 분리할 수 있다는 것—각 $$y\in Y$$마다 Hausdorff 조건으로 분리하는 근방 쌍을 잡고, compactness로 유한 개를 뽑아 교집합을 취하는 전략—은 Hausdorff와 compact가 "함께 작동하면 강해진다"는 것을 보여준다. 특히 따름정리 5—Hausdorff space의 compact subset은 닫힌집합—은 $$\varepsilon$$-$$\delta$$ 세계에서 "닫힌 유계 집합은 compact"라는 것과는 다른 방향의 결론인데, 위상에서는 유계성 대신 Hausdorff성이 compactness와 결합되어 닫힌집합을 만들어낸다는 것이 새롭다.

보조정리 6과 명제 7—compact Hausdorff space는 regular, normal—은 separation axioms의 계층에서 compactness가 상위 공리들을 자동으로 만족시킨다는 것을 보여준다. 하우스도르프 공간 글에서 $$T_3$$·$$T_4$$의 동기가 충분하지 않다고 느꼈었는데, 이 글에서 "compact Hausdorff가 곧 normal이다"라는 결론이 나오면서 그 공리들이 실제로 자연스러운 상황에서 등장한다는 것을 이해하게 되었다. 증명의 구조—보조정리 4를 반복 적용하는 것—"compact Hausdorff → regular → normal"이라는 사슬이 하나의 기법으로 증명되는 것이 깔끔하다.

명제 8—연속함수가 compactness를 보존—은 예상 가능한 결과인데, 원상이 covering을 covering으로 보내는 것이 핵심이다. 명제 9—compact에서 Hausdorff로의 전단사 연속함수는 homeomorphism—은 이 글에서 가장 실용적인 결과로 보인다. $$f^{-1}$$의 연속성을 보이기 위해 $$f$$가 closed map임을 compactness + Hausdorff로 증명하는 전략은, 따름정리 5와 보조정리 3이 조합되는 구조로서 앞서 다룬 결과들의 자연스러운 수확이다.

정의 10의 finite intersection property와 명제 11의 동치—compact ↔ FIP를 만족하는 닫힌집합 family의 교집합이 비어있지 않다—는 compactness의 "대우" 형태로, open covering 대신 닫힌집합의 교집합으로 compactness를 표현한다. 여집합을 취하면 바로 open covering 정의로 돌아간다는 증명의 한 줄이 이 동치의 본질을 보여준다. filter base의 subbase라는 언급은 위상의 다른 정의들 글의 terminology를 사용하고 있어서 연결이 자연스럽다.

전체적으로 이 글은 compactness를 정의하고, Hausdorff 조건과 결합했을 때 얻어지는 강력한 분리 성질들을 다룬다. Hausdorff 글이 "점을 구별하는 위상의 강도"를 분류했다면, 이 글은 "공간의 크기를 제한하는 조건"이 그 분리 성질과 어떻게 상호작용하는지를 보여준다. 다만 locally compact라는 개념이 보조정리 4에서 implicit하게 사용되고 있지만 이 글에서 명시적으로 정의되지 않았고, one-point compactification은 이후 Compactness 글에서야 등장한다.

## [옹골성과 필터의 수렴](/ko/math/topology/filter_convergence)

이 글은 compactness와 관련된 세 가지 개념—compact, limit point compact, sequentially compact—의 관계를 다루고, 점열의 수렴이 위상에서 부적절한 이유를 보여준 뒤 filter의 수렴으로 이를 대체한다. 정의 1의 limit point compact—"모든 무한집합이 limit point를 갖는다"—는 집합론 노트에서 다룬 Bolzano-Weierstrass 성질의 공리적 버전인데, compact ⇒ limit point compact라는 명제 2의 증명에서 compact subset $$A$$의 open covering $$(U_a)_{a\in A}$$이 finite subcover를 갖지 않는다는 모순을 유도하는 전략이 간결하다. 그런데 예시 3—trivial topology의 two-point space와 discrete topology의 무한집합의 곱—에서 compact가 아닌 limit point compact 공간이 존재한다는 것은, 두 개념이 실제로 다르다는 것을 보여준다.

정의 4의 sequentially compact—"모든 점열이 수렴하는 부분점열을 갖는다"—는 미적분학의 Bolzano-Weierstrass 정리와 가장 가까운 개념인데, 명제 5에서 sequentially compact ⇒ limit point compact를 보이는 증명은 자연스럽다. 그런데 예시 6이 이 글에서 가장 충격적인 부분이다. $$\mathbb{R}$$ 위에 $$\mathcal{B}=\{(a,\infty)\mid a\in\mathbb{R}\}$$를 기저로 하는 위상을 주면, 점열 $$x_n=-n$$은 수렴하는 부분점열이 없지만 $$A=\{x_n\}$$는 limit point $$-2$$를 갖는다. $$-2$$를 포함하는 임의의 열린집합이 $$-1\in A$$를 포함해야 한다는 이유인데, "limit point는 존재하지만 거기로 수렴하는 점열은 없다"는 이 반례는 $$\varepsilon$$-$$\delta$$ 직관으로는 예상하기 어려운 것이다.

보조정리 7—$$x$$로 수렴하는 $$A$$의 점열이 존재하면 $$x\in\cl(A)$$—은 자연스럽지만, 예시 8에서 $$\mathbb{R}^J$$의 uncountable product에 대해 $$\scl(A)\subsetneq\cl(A)$$가 된다는 것은 점열의 수렴이 closure를 완전히 포착하지 못한다는 것을 의미한다. $$A$$의 임의의 점열에 대해 모든 항의 $$j$$번째 성분이 $$1$$인 $$j\in J$$가 존재한다는 것은 uncountability가 점열의 "정보 전달 능력"을 제한한다는 직관을 준다. $$\scl(A)=\cl(A)$$인 공간을 sequential space라 부른다는 정의는 이후 위상에서 점열이 유효한 도구인지를 판별하는 기준이 될 것 같다.

명제 11—"first countable $$T_1$$이고 limit point compact이면 sequentially compact"—의 증명이 가장 기술적으로 흥미로운 부분이다. $$x$$의 countable local base $$B_1\supseteq B_2\supseteq\cdots$$를 잡고, $$T_1$$ 조건으로 이전 항들을 제거하는 열린집합 $$U_n$$을 만들어 $$x_{n_k}\in U_k\cap B_k$$를 선택하는 전략은, "점진적으로 근방을 좁혀가면서 부분점열을 추출한다"는 이미지가 명확하다. $$T_1$$ 조건이 "유한 개 점을 피하는 열린집합"을 제공한다는 것이 증명의 핵심인데, Hausdorff 글에서 $$T_1$$을 "분리가능"으로 정의한 것이 여기서 구체적으로 활용된다.

정의 12의 filter 수렴—$$\mathcal{N}(x)\subseteq\mathcal{F}$$—은 "filter가 $$x$$의 모든 근방을 포함한다"는 것이고, 명제 14에서 점열의 수렴이 Fréchet filter의 image로 생성되는 filter의 수렴과 동치라는 것은 filter가 점열의 일반화임을 정확히 보여준다. $$\mathbb{N}$$ 위의 Fréchet filter—유한 집합의 여집합들로 구성된 filter—가 "충분히 큰 $$n$$"이라는 직관을 formalize한다는 것이 인상적이다. 명제 15—$$x\in\cl(A)$$와 $$x$$로 수렴하는 $$A$$의 filter 존재의 동치—는 closure를 filter 언어로 재해석한 것으로, 명제 16—$$f$$의 연속성과 filter 수렴 보존의 동치—와 합치면 "연속함수는 filter의 수렴을 보존한다"는 깔끔한 결론이 된다.

전체적으로 이 글은 "점열이라는 도구가 위상에서 불충분한 이유"를 체계적으로 보여주고, filter라는 더 강력한 도구로 대체하는 과정을 다룬다. 앞서 Compact Spaces 글이 compactness를 정의하고 Hausdorff 조건과의 상호작용을 다뤘다면, 이 글은 compactness의 변형(limit point compact, sequentially compact)들과 그 차이를 분석한다. 다만 명제 11의 증명에서 "first countable $$T_1$$"이라는 가정이 정확히 어디에 쓰이는지를 따라가는 데 약간의 노력이 필요했다—$$T_1$$은 유한 집합을 피하는 열린집합을, first countability는 decreasing local base를 각각 제공한다는 것이 핵심이다.

## [옹골성](/ko/math/topology/compactness)

이 글은 compactness의 핵심 정리들—Tychonoff 정리, one-point compactification, paracompactness—을 다룬다. 보조정리 1의 ultrafilter characterization—compact ↔ 임의의 ultrafilter가 수렴—은 필터 수렴 글의 명제 5를 ultrafilter로 강화한 것인데, 증명에서 ultrafilter의 primality($$A\in\mathcal{F}$$ 또는 $$X\setminus A\in\mathcal{F}$$ 중 정확히 하나)를 사용하는 부분이 핵심이다. 유한 subcover가 없다고 가정하면 각 $$U_{x_i}\not\in\mathcal{F}$$이므로 $$X\setminus U_{x_i}\in\mathcal{F}$$이고, 이들의 유한 교집합도 $$\mathcal{F}$$에 속해야 하는데 이것이 $$X\setminus A\in\mathcal{F}$$와 모순된다는 구조가 깔끔하다. ultrafilter가 "더 이상 확장할 수 없는 filter"라는 maximality가 primality를 자동으로 제공한다는 것이, 집합론 필터 노트에서 봤던 결과가 여기서 결정적으로 쓰인다.

정리 2의 Tychonoff 정리—compact space들의 임의의 product는 compact—는 이 글에서 가장 강력한 결과다. 증명 전략이 영리한데, $$\pr_i(\mathcal{F})$$가 ultrafilter base를 이루고, 각 $$X_i$$의 compactness로 limit point $$x_i$$를 얻은 뒤, $$x=(x_i)$$가 전체 product의 ultrafilter의 limit point임을 보이는 것이다. 유한 product의 경우 induction으로 더 간단히 보일 수 있지만, 무한 product에서 ultrafilter가 필요한 이유—점열로는 uncountable product의 구조를 포착할 수 없기 때문—는 필터 수렴 글의 예시 8과 연결되는 통찰이다. Tychonoff 정리가 "compactness는 곱에 대해 보존된다"는 것인데, Hausdorff성도 곱에 대해 보존된다는 것(하우스도르프 공간 글 명제 8)과 나란히 놓으면 "곱공간이 원래 공간들의 좋은 성질을 물려받는다"는 큰 그림이 보인다.

정의 3의 locally compact—각 점에서 compact neighborhood가 존재—는 compactness를 "국소적으로" 완화한 것이다. Compact Spaces 글에서 implicitly 사용되었던 개념이 여기서 명시적으로 정의되는 셈인데, 보조정리 4에서 locally compact Hausdorff space가 regular라는 것도 Compact Spaces 글의 보조정리 6(compact Hausdorff → regular)과 병행된다. 정리 4의 Alexandroff one-point compactification—locally compact Hausdorff space에 한 점을 추가하여 compact Hausdorff space를 얻는 것—은 "compact하지 않은 공간을 compact하게 만드는 가장 자연스러운 방법"이다. 열린집합의 두 종류—$$X$$의 열린집합과, $$X$$의 compact subset의 여집합—가 정의 1의 세 공리를 만족한다는 것이 영리하고, 유일성은 universal property로 증명되는 구조가 범주론적 사고와 맞아떨어진다. proper maps 글 따름정리 9에서 $$\overline{f}$$의 연속성이 one-point compactification으로 재해석된다는 것을 이미 봤는데, 이 글에서 그 구성의 존재성과 유일성이 증명되는 것이 좋았다.

정의 5의 paracompact—임의의 open covering이 locally finite open refinement를 갖는 것—는 compactness의 또 다른 완화다. "locally finite subcover"는 compactness와 동치이지만, "locally finite refinement"를 허용하면 훨씬 넓은 클래스의 공간이 포함된다. 정리 7의 partition of unity 존재 동치—paracompact Hausdorff ↔ 임의의 open cover에 subordinate한 partition of unity 존재—는 이 글에서 가장 실용적인 결과로 보인다. partition of unity가 "국소적으로 정의된 함수들을 전역적으로 합치는 도구"라는 것은, 층 이론의 gluing 문제와 정확히 같은 주제인데, paracompactness가 이 gluing을 가능하게 해주는 위상적 조건이라는 것이 인상적이다.

정의 8·9의 topological manifold—second countable + Hausdorff + locally Euclidean—와 정리 10의 동치—Hausdorff locally Euclidean에서 second countable ↔ paracompact + countable many connected components—는 "실용적인 공간(manifold)이 paracompactness를 자동으로 만족한다"는 좋은 결론이다. connected component가 아직 정의되지 않았지만, 정리 10의 결론—manifold는 paracompact Hausdorff이고 따라서 partition of unity를 갖는다—은 이후 미분기하에서 국소적 구조를 전역적으로 결합하는 데 필수적인 도구가 될 것이라는 예감을 준다. $$f=\sum\phi_i f_i$$라는 식으로 전역 함수를 구성하는 것은 선형대수에서 벡터를 기저로 분해하는 것과 비슷한 느낌을 준다.

전체적으로 이 글은 compactness의 "활용"—Tychonoff 정리, one-point compactification, paracompactness, manifold—을 다루면서, compactness가 위상 전반에서 어떤 역할을 하는지를 보여준다. Compact Spaces 글이 compactness를 정의하고 Hausdorff 조건과의 상호작용을 다뤘다면, 이 글은 compactness의 일반화와 응용으로 초점을 옮긴다. 다만 ultrafilter의 primality 증명이 집합론 노트에서 이미 다뤄졌다는 것을 전제하고 있어서, 그 부분의 이해가 이 글의 증명을 따라가는 데 필수적이다.

⚠️ 정의 없이 사용: `supp` (support, 정의 6에서 $$\supp\phi_i\subseteq U_i$$로 사용)

## [고유함수](/ko/math/topology/proper_maps)

보편닫힌사상(universally closed map)의 정의—임의의 위상공간 $$Z$$에 대해 $$f\times\id_Z$$가 closed인 연속함수—는 "닫힌사상"이라는 개념을 곱공간까지 확장한 것이다. $$Z=\{\ast\}$$로 놓으면 universally closed가 closed를 함의하지만 역은 성립하지 않는다는 관찰에서, 이 정의가 얼마나 강한 조건인지를 짐작할 수 있다. 그런데 명제 2에서 연속 단사함수의 경우 세 조건—universally closed, closed, homeomorphism onto image—이 동치라는 것은, 단사성이라는 추가 가정이 universally closed의 힘을 크게 줄여준다는 것을 보여준다. 이 동치 조건의 증명이 비교적 간단한 편이라서, universally closed가 어려운 것은 "일반적인 함수"에서지 "단사 함수"에서는 아니라는 인상을 받았다.

명제 3의 두 결과는 universally closed를 국소적으로 검사할 수 있는 도구를 제공한다. 첫째—부분집합으로 제한해도 universally closed가 보존됨—는 자연스럽고, 둘째—locally finite closed covering이나 interior로 이루어진 open covering에서 각 조각이 universally closed이면 전체도 그러하다—는 "열린사상과 닫힌사상" 글의 명제 3을 그대로 사용하는 것이어서, 이전 글의 결과가 얼마나 실용적인지를 체감하게 해준다. 명제 4의 합성에 대한 성질들 중 처음 세 개는 열린사상과 닫힌사상 글의 명제 2로부터 바로 오는데, 마지막—$$Y$$가 Hausdorff이면 $$g\circ f$$가 universally closed일 때 $$f$$도 그러하다—는 그래프 $$\Gamma_f$$를 이용하는 증명이 가장 흥미롭다. $$Y$$가 Hausdorff라는 가정이 그래프가 닫힌집합이 되도록 만들어주고, 이것이 universally closed와 연결되는 구조가 $$\varepsilon$$-$$\delta$$ 직관과는 전혀 다른 방식의 사고라는 것을 느꼈다.

보조정리 5—$$f:X\rightarrow\{\ast\}$$가 universally closed이면 $$X$$는 compact—의 증명이 이 글에서 가장 도전적인 부분이다. $$X$$ 위의 filter $$\mathcal{F}$$에 대해 $$X'=X\cup\{\ast_X\}$$를 만들고 적절한 위상을 부여한 뒤, $$X\times X'$$의 대각선 $$\Delta$$의 closure를 $$f\times\id_{X'}$$로 보내는 전략은 상당히 영리하지만, $$\ast_X$$가 $$\mathcal{F}$$의 "극한점" 역할을 한다는 것—$$\mathcal{N}(\ast_X)=\mathcal{F}'$$로 정의하는 것—이 직관적으로 잘 잡히지 않았다. "filter의 극한점을 직접 만들어서 compactness를 증명한다"는 아이디어 자체는 이해하지만, 왜 $$\cl\Delta$$의 image가 닫힌집합이라는 것에서 $$x$$의 존재가 나오는지를 단계별로 따라가는 데 어려움이 있었다.

정리 6의 동치—universally closed ↔ closed + compact fibers—는 이 글의 핵심 결과이다. 특히 practical한 의미가 큰데, "모든 $$Z$$에 대해 $$f\times\id_Z$$를 검사해야 한다"는 정의 대신 "각 fiber $$f^{-1}(y)$$가 compact인지만 확인하면 된다"는 것이므로, 실제로 universally closed를 판별할 수 있는 도구가 된다. $$Z=\{\ast\}$$인 특수한 경우가 compactness를 주고, 일반적인 경우가 fiberwise compactness를 준다는 구조—보조정리 5와 정리 6이 각각 한 방향을 담당—는 논리적으로 깔끔하다. 따름정리 7—universally closed이면 compact subset의 역상도 compact—는 정리 6의 직접적인 응용인데, 이것이 곧 proper map의 정의가 된다.

명제 8에서 Hausdorff + locally compact 가정 하에 proper ↔ universally closed가 되는 것은, 이 가정들이 "fiberwise compactness에서 전체 universally closed로 올라갈 수 있는 통로"를 제공한다는 느낌을 준다. locally compact이므로 적당한 compact set으로 감싸는 open covering을 만들 수 있고, 각 조각에서 universally closed를 확인한 뒤 명제 3으로 합치는 전략은 "국소에서 전체로"라는 위상학적 사고의 전형적인 패턴이다. 따름정리 9의 one-point compactification을 통한 characterization—$$\overline{f}$$가 연속인 것과 동치—은 앞서 Compactness 글에서 살펴본 one-point compactification이 여기서 자연스럽게 응용되는 좋은 예시이다.

전체적으로 이 글은 "닫힌사상"이라는 개념을 곱공간까지 확장한 universally closed를 정의하고, 이것이 compactness와 본질적으로 연결되어 있음을 보여준다. $$f:X\rightarrow\{\ast\}$$가 universally closed ↔ $$X$$ compact라는 관찰은, compactness가 "한 점으로의 사상"이라는 특수한 proper map으로 해석될 수 있다는 것을 의미하고, 일반적인 proper map은 이를 fiberwise로 확장한 것이다. 다만 보조정리 5의 증명에서 $$X'$$를 구성하는 기법—filter의 극한점을 위상적으로 만들어내는 것—은 아직 완전히 소화하지 못한 느낌이다.

## [연결공간](/ko/math/topology/connected_spaces)

연결성의 정의—두 개의 서로소인 비어있지 않은 열린집합으로 분리할 수 없다는 것—는 위상의 "분리 불가능성"을 포착하는 개념이다. $$\varepsilon$$-$$\delta$$ 세계에서 구간 $$[a,b]$$가 "끊어지지 않는다"는 직관을 공리화한 것인데, discrete topology에서는 모든 두 점 이상의 집합이 disconnected이고, trivial topology에서는 모든 부분집합이 connected라는 예시가 정의의 양극단을 잘 보여준다. 명제 2의 closure 보존—$$A\subseteq B\subseteq\cl(A)$$이면 $$B$$도 connected—는 "연결된 집합에 경계점만 붙여도 연결성이 깨지지 않는다"는 것이고, $$\cl_B(A)=B$$라는 부분공간 closure 공식이 증명의 핵심이다. 명제 3의 pairwise intersecting union—서로 만나는 연결집합들의 합집합은 연결—은 직관적으로 명확하면서도, connected component의 정의(정의 7)에서 "가장 큰 connected set"의 존재성을 보장하는 데 필수적인 결과다.

명제 4의 연속함수 보존—$$f(A)$$가 connected—은 compactness 보존(옹골공간 글 명제 8)과 완전히 병행되는 패턴인데, "좋은 성질은 연속함수에 의해 보존된다"는 위상학의 기본 원리를 다시 한번 확인시켜준다. 따름정리 5—몫공간도 connected—는 명제 4의 직접적인 응용이고, 명제 6의 곱공간 connectedness는 Tychonoff 정리의 connected 버전이라는 느낌을 준다. 증명에서 $$f:X\rightarrow\{0,1\}$$이라는 상수함수를 discrete topology로 정의하고, $$f\circ\iota_i$$가 상수임을 $$X_i$$의 connectedness로부터 추론하는 전략은 영리하다. "유한 개를 제외한 성분이 $$a$$와 같은 점들의 모임이 dense"라는 관찰이 핵심인데, product topology의 base 정의—"유한 개 좌표만 변하는" 집합—과 정확히 맞아떨어진다.

정의 7의 connected component—$$x$$를 포함하는 가장 큰 connected set—는 명제 3의 pairwise intersecting 조건이 자동으로 만족되므로 well-defined가 된다. totally disconnected의 정의—"모든 component가 singleton"—는 예시로 $$\mathbb{Q}$$가 떠오르는데, 이 글에서 직접 다루지 않았지만 이후 위상에서 분리 공리와 연결되어 다시 등장할 것 같다. 명제 8의 $$X/{\sim}$$이 totally disconnected라는 것은, "component를 점으로 collapsing하면 더 이상 분리할 수 없다"는 직관을 formalize한다.

정의 9의 locally connected—각 점에서 connected neighborhood가 존재—는 compactness의 국소화(locally compact)와 유사한 패턴인데, 명제 10의 동치—"열린집합의 component가 항상 open"—가 이 개념의 실용적 characterization을 제공한다. locally connected space에서는 connected component가 clopen이므로, component decomposition이 열린집합들의 partition이 된다는 것이 인상적이다. 다만 이 글에서 "clopen set"이라는 용어가 정의 없이 사용되었다. 경로연결(path-connected) 섹션이 시작만 되어 있고 내용이 비어있는 점이 아쉽다.

⚠️ 정의 없이 사용: `clopen set` (열린집합이면서 닫힌집합인 집합, 정의 없이 사용됨)

## [차원](/ko/math/topology/dimension)

차원의 정의—"임의의 open covering을 order $$m+1$$짜리 refinement로 교체할 수 있는 최소의 $$m$$"—는 직관적으로 "점이 동시에 속하는 열린집합의 최대 개수"를 제한하는 것인데, $$\varepsilon$$-$$\delta$$ 세계에서 $$\mathbb{R}^n$$의 차원을 $$n$$으로 인식했던 것과는 전혀 다른 방식의 접근이다. 정의 1의 order 개념—"아무 점도 $$m+1$$개 이상의 $$U_i$$에 속하지 않고, 어떤 점은 정확히 $$m+1$$개에 속한다"—는 "겹침의 정도"를 정량화하는 것인데, 이 수치가 open refinement를 통해 제어 가능하다는 것이 covering dimension의 핵심이다. compact space만 다루겠다는 제한이 명시되어 있는데, 일반적인 위상공간에서는 이 정의가 잘 작동하지 않을 수 있다는 점을 짐작할 수 있다.

명제 3—closed subspace의 차원이 전체 공간의 차원 이하—는 예상 가능한 결과인데, 증명에서 $$X\setminus Y$$를 covering에 추가하는 트릭이 compactness 글의 보조정리 3과 같은 패턴이다. $$Y$$의 open covering을 $$X$$의 open covering으로 확장한 뒤 refinement를 취하고 다시 $$Y$$로 제한하는 전략은 "부분공간의 문제를 전체 공간으로 끌어올렸다가 다시 내리는" 위상학적 사고의 전형이다. 명제 4—$$X=Y\cup Z$$일 때 $$\dim X=\max(\dim Y,\dim Z)$$—는 "차원은 합집합에서 가장 큰 성분으로 결정된다"는 직관을 formalize하는데, connected spaces 글의 pairwise intersecting union과는 다른 맥락에서 "합집합의 성질"을 다루고 있다.

명제 5—$$\mathbb{R}^n$$의 compact subspace는 $$n$$차원 이하—는 "차원이 $$n$$인 공간의 compact 부분은 $$n$$을 초과할 수 없다"는 결론인데, $$\mathbb{R}^n$$과 $$\mathbb{R}^m$$이 homeomorphic하지 않다는 것 자체가 증명하기 어렵다는 언급이 인상적이다. 이 사실은 이후 대수적 위상수학에서 homology나 homotopy로 증명할 수 있는 것인데, 현재까지 다룬 도구로는 부족하다는 것이 솔직한 상황 인식이다. "차원이 보존되는가"라는 질문이 이렇게 어려운 것이라는 점이, 차원이라는 개념의 깊이를 느끼게 해준다.

Krull dimension 섹션은 대수기하학에서 사용하는 차원의 개념인데, "irreducible closed subset들의 strictly descending chain의 길이"로 정의하는 것은 covering dimension과 완전히 다른 접근이다. 정의 6의 irreducible—"두 비자명한 닫힌집합의 합으로 분해 불가능"—는 connected와 비슷해 보이지만 훨씬 강한 조건인데, 명제 7의 동치 조건들—특히 "임의의 두 비어있지 않은 열린집합이 만난다"는 것—이 이 강도를 보여준다. connected는 "두 열린집합으로 분리 불가능"이지만, irreducible은 "어떤 두 열린집합도 서로소가 될 수 없다"는 것이므로, irreducible은 connected를 함의하지만 역은 성립하지 않는다.

Hausdorff space에서는 singleton만이 irreducible이므로 Krull dimension이 항상 $$0$$이라는 관찰은, "Hausdorff성은 irreducibility를 완전히 파괴한다"는 강한 결론이다. 대수기하학에서 관심 있는 공간—Zariski topology—은 Hausdorff가 아니므로 irreducible 구조가 풍성해질 수 있다는 것이, 왜 대수기하학에서 이 정의가 자연스러운지를 보여준다.

정의 11의 noetherian 조건—"닫힌집합들의 descending chain이 항상 안정화된다"—는 환론 노트에서 봤던 noetherian ring의 정의와 정확히 병행된다. 명제 12—noetherian space는 compact—의 증명에서 Zorn의 lemma를 사용하는 구조가 인상적인데, 유한 조합들의 부분순서집합의 totally ordered subset이 descending chain과 동치라는 관찰이 핵심이다. 환론에서 noetherian ring의 ideal들이 유한 생성이라는 것과, 여기서 noetherian space의 irreducible component가 유한하다는 것(명제 13)이 같은 패턴이라는 것이 "noetherian = 유한성 조건"이라는 주제를 다시 확인시켜준다.

명제 14—$$U$$와 만나는 $$X$$의 irreducible closed subset과 $$U$$의 irreducible closed subset의 일대일대응—은 "irreducible 구조가 열린집합 제한에 대해 잘 행동한다"는 것을 보여주는데, $$Z\mapsto Z\cap U$$와 $$Y\mapsto\cl_X(Y)$$가 서로의 역이라는 증명이 깔끔하다. connected component와 달리 irreducible component는 closure를 취해도 irreducible이 유지된다는 사실(정의 9 이후의 언급)이 이 bijection의 기반이 된다.

전체적으로 이 글은 "차원"이라는 기하학적 직관을 두 가지 전혀 다른 방식—covering dimension과 Krull dimension—으로 formalize한다. covering dimension은 "겹침의 정도"라는 위상적 관점이고, Krull dimension은 "분해의 깊이"라는 대수적 관점인데, 둘 다 "공간의 복잡성을 수치로 측정한다"는 공통 목표를 가진다. 다만 $$\mathbb{R}^n$$의 차원이 $$n$$이라는 기본적인 사실도 현재 도구로는 보이지 못한다는 한계가 명시되어 있어서, 이 글이 "차원의 정의"만 다루고 "차원의 계산"은 이후 글들에 맡기고 있다는 느낌을 받았다.
