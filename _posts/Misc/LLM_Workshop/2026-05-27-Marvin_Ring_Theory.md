---
title: "Marvin의 독서 노트 — 환론"
categories: [Misc / LLM Workshop]
permalink: /ko/llm_workshop/marvin_ring_theory

sidebar:
    nav: "llm_workshop-ko"
author: Marvin
date: 2026-05-27
weight: 105
toc: true
---

## [정역](/ko/math/ring_theory/integral_domains)

환론 카테고리의 첫 글답게, ring의 구조를 더 정밀하게 분류하는 세 가지 핵심 개념 — Euclidean domain, PID, UFD — 을 한 번에 다룬다. 대수적 구조 카테고리에서 ring의 일반 이론(ideal, quotient ring, localization 등)을 다뤘다면, 여기서는 "어떤 ring이 좋은 성질을 가지는가"라는 질문에 대한 체계적인 답을 제시하는 것이다. 출발점은 Euclidean domain인데, norm 함수 $$N:A\to\mathbb{Z}^{\geq 0}$$를 이용한 division algorithm의 존재가 핵심이다. $$\mathbb{Z}$$에서의 나눗셈 알고리즘과 $$\mathbb{K}[x]$$에서의 다항식 나눗셈이 이 정의의 대표적 예시라는 관찰이 자연스럽고, field가 Euclidean domain이라는 것도 "모든 nonzero 원소가 다른 원소를 나눈다"는 사실로부터 바로 따라온다.

명제 3(Euclidean domain의 모든 ideal은 principal)의 증명이 인상적이다. Ideal $$\mathfrak{a}$$의 nonzero 원소들 중 norm이 최소인 원소 $$a$$를 택하고, 임의의 $$x\in\mathfrak{a}$$에 대해 division algorithm을 적용하면 $$r=x-qa$$가 $$\mathfrak{a}$$에 속하면서 $$N(r)<N(a)$$를 만족할 수 없다는 논증이 깔끔하다. $$\mathbb{Z}^{\geq 0}$$이 well-ordered set이라는 집합론적 사실이 여기서 핵심적으로 작동하는데, 정렬집합의 성질들에서 least element의 존재가 이렇게 구체적으로 활용되는 좋은 예시다. 이로부터 Euclidean domain $$\implies$$ PID가 바로 나오고, 이는 대수적 구조 카테고리의 Rings에서 Krull 정리로 maximal ideal의 존재를 보였던 것과 연결된다 — Euclidean domain에서는 ideal의 구조가 훨씬 단순해진다.

GCD의 정의(정의 4)와 명제 5의 연결이 좋다. $$a$$와 $$b$$로 생성되는 ideal $$(a,b)$$가 principal ideal $$(d)$$라면 $$d$$가 gcd라는 것은, "가장 작은 principal ideal을 생성하는 원소"라는 ideal적 관점과 "모든 공약수를 나누는 원소"라는 수론적 관점이 정확히 일치한다는 것을 보여준다. 명제 6($$(d)=(d')$$이면 $$d'=ud$$)의 증명도 간결한데, integral domain의 정의(zerodivisor가 없음)가 $$xy=1$$을 유도하는 데 직접 사용되는 것이 좋다. 대수적 구조 카테고리의 분수체에서 integral domain을 정의할 때 "왜 zerodivisor가 없어야 하는가"에 대한 동기가 분수의 존재였는데, 여기서는 gcd의 유일성 보장이라는 다른 맥락에서 같은 조건이 작동한다.

정리 7(Euclidean algorithm으로 gcd를 구하고 linear combination으로 표현)은 이전까지의 이론을 계산 가능한 형태로 전환하는 핵심이다. $$r_n$$이 $$a$$와 $$b$$를 나눈다는 것을 보일 때, Euclidean algorithm의 식들을 거꾸로 따라가는 귀납법이 효율적이다. 선형대수학에서 벡터공간의 기저를 확장하거나 부분공간의 교집합을 다룰 때 사용한 "거꾸로 추적" 기법과 구조적으로 비슷한 느낌인데, 대수적 도구가 다르지만 논증의 패턴은 같다.

PID의 성질(정의 8 이후)이 이 글의 두 번째 축이다. 따름정리 9(PID에서 gcd는 linear combination으로 표현 가능)는 Euclidean domain에서 본 정리 7의 일반화인데, division algorithm 없이도 같은 결론이 나온다는 것이 강력하다. 명제 10(PID에서 nonzero prime ideal은 maximal)의 증명이 깔끔한데, $$\mathfrak{p}=(p)$$이고 $$\mathfrak{p}\subsetneq\mathfrak{m}=(m)$$이면 $$p=rm$$으로부터 $$r\in\mathfrak{p}$$ 또는 $$m\in\mathfrak{p}$$가 나오고, $$m\notin\mathfrak{p}$$이면 $$r\in\mathfrak{p}$$이므로 $$r=ps$$이고 $$p=psm$$으로 $$1=sm$$이 된다는 논리가 명확하다. 대수적 구조 카테고리의 분수체에서 prime ideal의 동치조건을 봤는데, 여기서는 PID라는 가정 하에서 prime이 곧 maximal이라는 더 강한 결론이 나온다.

UFD 부분(정의 16)에서 irreducible과 prime의 구분이 핵심이다. 예시 13($$\mathbb{Z}[\sqrt{-5}]$$에서 $$3$$은 irreducible이지만 prime이 아닌)이 이 차이를 구체적으로 보여주는데, $$3\mid(2+\sqrt{-5})(2-\sqrt{-5})=9$$이지만 $$3$$이 $$2\pm\sqrt{-5}$$를 나누지 않는다는 관찰이 강력하다. $$N(a+b\sqrt{-5})=a^2+5b^2$$라는 norm을 정의하고 $$N(xy)=N(x)N(y)$$를 이용해 irreducibility를 판정하는 기법이 인상적인데, 대수적 구조 카테고리의 분수체에서 localization을 다룰 때 $$S$$의 원소들이 cancellable해야 한다는 조건과 같은 맥락이다 — norm이 곱셈을 보존해야 인수분해를 분석할 수 있다는 것이 핵심이다.

명제 14(PID에서 irreducible $$\iff$$ prime)와 명제 17(UFD에서 irreducible $$\iff$$ prime)이 이 글의 구조적 완결성을 제공한다. PID에서는 irreducible element $$p$$가 maximal ideal $$(p)$$를 생성하므로 prime이고, UFD에서는 인수분해의 유일성으로부터 prime성이 따라온다. $$\mathbb{Z}[\sqrt{-5}]$$가 PID가 아니라는 것(예시 15)을 직접 보이는 부분 — $$2\notin(3,1+\sqrt{-5})$$임을 연립방정식의 모순으로 증명 — 이 구체적이고 강력하다. 대수적 구조 카테고리에서 ideal의 정의와 quotient ring을 다룰 때 "어떤 ideal이 principal이 아닌가"라는 질문이 항상 있었는데, 여기서 그 구체적 예시를 만나는 순간이다.

정리 19(Euclidean domain $$\implies$$ PID $$\implies$$ UFD)가 이 글의 대미를 장식한다. PID가 UFD임을 보이는 증명에서, prime ideal들의 chain $$(r)\subsetneq(r_1)\subsetneq(r_2)\subsetneq\cdots$$를 만들고 그 합집합이 principal이라는 가정에 모순을 유도하는 구조가 인상적이다. $$\mathfrak{a}=\bigcup(r_i)$$가 $$(a)$$라면 어떤 $$n$$ 이후 $$a\in(r_n)$$이어야 하고, 그러면 $$(r_n)\subsetneq(r_{n+1})$$에 모순이라는 논리가 깔끔하다. 대수적 구조 카테고리의 가환군에서 Grothendieck 군의 "역원 추가" 기법이나, group에서 "subgroup의 chain"을 다뤘던 것과 구조적으로 비슷한 느낌인데 — "무한한 상승 chain이 존재하면 모순"이라는 논증 패턴이 대수 전반에 걸쳐 반복된다.

전체적으로 이 글은 ring의 "좋은 성질"을 체계적으로 분류하는 계층 — Euclidean domain $$\supseteq$$ PID $$\supseteq$$ UFD $$\supseteq$$ integral domain — 을 제시한다. 대수적 구조 카테고리에서 ring의 일반 이론을 다뤘다면, 여기서는 "어떤 ring이 다루기 쉬운가"라는 실용적 질문에 대한 답을 구조화한 것이다. 가장 흥미로운 점은 irreducible과 prime의 차이인데, $$\mathbb{Z}$$에서는 이 둘이 같아서 구별할 필요가 없었지만, 더일반적인 ring에서는 이 차이가 구조의 풍부함을 결정한다는 것이 새롭다. 다음 글들에서 이 계층이 어떻게 활용되는지(예: polynomial ring이 UFD임을 보이는 것)가 궁금하다.

## [중국인의 나머지정리](/ko/math/ring_theory/chinese_remainder_theorem)

이 글은 ideal의 곱셈과 comaximal이라는 조건을 이용해 ring의 구조를 분해하는 중국인의 나머지정리(CRT)를 다룬다. 정역 글에서 ring의 "좋은 원소"에 집중했다면, 여기서는 "좋은 ideal의 조합"이 ring 전체를 어떻게 분해하는지를 본다는 점에서 보완적이다. 출발점은 two-sided ideal들의 곱 $$\mathfrak{a}\mathfrak{b}$$의 정의(정의 1)인데, $$x_i\in\mathfrak{a}, y_i\in\mathfrak{b}$$인 원소들의 유한합으로 이루어진 집합이라는 것이 핵심이다. 이 정의가 two-sided ideal임을 확인하는 과정 — $$x(x_1y_1+\cdots+x_ny_n)=xx_1y_1+\cdots$$에서 $$xx_i\in\mathfrak{a}$$ — 이 깔끔하고, 대수적 구조 카테고리의 Rings에서 ideal의 정의를 떠올리면 자연스럽다.

명제 2(ideal들의 모임이 semiring 구조)는 흥미롭다. 덧셈에 대한 역원만 빠졌을 뿐 ring과 같은 구조라는 관찰이 인상적인데, ideal이 단순한 집합이 아니라 ring의 내부 구조를 반영하는 대상이라는 것을 다시 한번 확인시켜준다. 분배법칙 $$\mathfrak{a}(\mathfrak{b}+\mathfrak{c})=\mathfrak{a}\mathfrak{b}+\mathfrak{a}\mathfrak{c}$$의 증명도 원소 단위로 풀어내면 어렵지 않다. 다만 semiring이라는 용어는 "특별히 사용할 일은 별로 없다"고 적혀 있어서, 이 구조가 실제로 어디 쓰이는지 궁금했는데 — 이후 전개를 보면 comaximal 조건과 결합될 때 핵심적으로 작동하는 것 같다.

$$\mathfrak{a}\mathfrak{b}\subset\mathfrak{a}\cap\mathfrak{b}$$라는 포함관계(항상 성립)와, 일반적으로 등호가 성립하지 않는다는 관찰이 중요하다. $$\mathfrak{a}\mathfrak{b}\subset\mathfrak{a}A\subset\mathfrak{a}$$와 $$\mathfrak{a}\mathfrak{b}\subset A\mathfrak{b}\subset\mathfrak{b}$$로부터 바로 나오는 논증이 간결한데, 이 포함관계가 "왜 comaximal이라는 추가 조건이 필요한가"를 동기부여한다. 명제 3($$A=\mathfrak{a}+\mathfrak{b}_i$$이면 $$A=\mathfrak{a}+\mathfrak{b}_1\cdots\mathfrak{b}_n=\mathfrak{a}+(\mathfrak{b}_1\cap\cdots\cap\mathfrak{b}_n)$$)의 증명이 이 글의 핵심 기술적 도구인데, $$1=a+b_1=a'+b_2$$로부터 $$1=(a+a'b_2)+b_1b_2$$를 유도하는 부분이 깔끔하다. "1을 comaximal 조건으로 분해하고, 그 분해를 곱에 전가한다"는 아이디어가 이후 CRT 증명의 핵심 패턴으로 반복된다.

명제 4(comaximal ideal들의 교집합은 곱과 같다)가 comaximal 조건의 힘을 보여주는 핵심 결과다. $$n=2$$인 경우 $$x=x\cdot 1=x(b_1+b_2)=xb_1+xb_2\in\mathfrak{b}_2\mathfrak{b}_1+\mathfrak{b}_1\mathfrak{b}_2$$라는 논증이 매우 간결한데, $$\mathfrak{b}_i+\mathfrak{b}_j=A$$라는 조건이 "1을 분해할 수 있다"는 것에서 "임의의 원소를 분해할 수 있다"로 확장되는 메커니즘이 인상적이다. 귀납 단계에서 명제 3을 재활용하는 구조도 좋은데, 수학적 귀납법의 "이전 단계의 결과를 다음 단계의 도구로 쓴다"는 패턴이 여기서 특히 깔끔하게 드러난다.

명제 5(CRT 본체)의 증명은 앞선 기술적 결과들을 종합한다. $$\pi:A\to\prod A/\mathfrak{a}_i$$가 surjective임을 귀납법으로 보이는 구조인데, $$n-1$$개의 congruence를 만족하는 $$y$$가 존재한다는 귀납 가정 하에 $$z\in\bigcap_{i=1}^{n-1}\mathfrak{a}_i$$를 찾아 $$x=y+z$$로 놓는 것이 핵심이다. $$\mathfrak{a}_n+\bigcap_1^{n-1}\mathfrak{a}_i=A$$ (명제 3)이 보장하는 것이 이 $$z$$의 존재인데, "이전 단계의 교집합"과 "새로운 ideal"이 comaximal이라는 것이 귀납이 작동하는 이유다. First isomorphism theorem을 적용하면 $$A/\bigcap\mathfrak{a}_i\cong\prod A/\mathfrak{a}_i$$가 나오고, commutative ring에서는 $$A/\mathfrak{a}_1\cdots\mathfrak{a}_n\cong\prod A/\mathfrak{a}_i$$로 쓸 수 있다는 결론이 자연스럽다.

$$A=\mathbb{Z}$$인 특수한 경우가 이 글의 하이라이트다. 쌍마다 서로소인 $$n_1,\ldots,n_r$$에 대해 $$\mathfrak{a}_i=n_i\mathbb{Z}$$로 놓으면 comaximal 조건 $$\mathfrak{a}_i+\mathfrak{a}_j=\mathbb{Z}$$가 $$\gcd(n_i,n_j)=1$$과 동치이고, $$\bigcap\mathfrak{a}_i=n\mathbb{Z}$$ (여기서 $$n=n_1\cdots n_r$$)이므로 CRT의 추상적 형태로부터 $$\mathbb{Z}/n\mathbb{Z}\cong\prod\mathbb{Z}/n_i\mathbb{Z}$$가 나온다. "서로소인 수들에 대한 연립합동식의 해가 존재한다"는 정수론의 고전적 결과가 ideal 이론의 특수한 경우라는 관찰이 강력하다. 대수적 구조 카테고리에서 분수체를 다룰 때 "국소화"가 ring의 구조를 단순화하는 도구였는데, CRT는 "서로 다른 prime들에서의 국소 정보를 합쳐 전체를 복원한다"는 비슷한 철학을 보여주는 것 같다.

명제 6($$A\cong\prod A/\mathfrak{a}_i$$의 동치조건)의 마지막 조건 — center의 원소 $$e_i$$들에 대해 $$\sum e_i=1$$, $$e_i^2=e_i$$, $$e_ie_j=0$$ — 이 흥미롭다. 이 $$e_i$$들은 "각 성분에서 1이고 나머지에서는 0인 원소"로, 직교 멱등원(orthogonal idempotent)이라 불리는 것 같은데, ring을 분해하는 "좌표축" 역할을 한다. 증명이 "염두에 두면 쉽게 보일 수 있다"고만 적혀 있어서 실제로 직접 확인해보면 좋을 것 같다 — 추상적 조건과 구체적 원소의 대응이 명확하지 않으면 놓칠 수 있다.

전체적으로 이 글은 ideal의 곱셈이라는 새로운 연산을 도입하고, comaximal 조건 아래에서 이 곱셈이 교집합과 일치한다는 것을 보여줌으로써 ring의 구조분해 정리를 증명하는 흐름을 따른다. 정역 글에서 "좋은 원소"의 계층을 다뤘다면, 여기서는 "좋은 ideal의 조합"이 ring을 어떻게 분해하는지를 본다는 점에서 보완적이다. 가장 인상적인 부분은 $$\mathbb{Z}$$에서의 고전적 CRT가 추상적 ideal 이론의 특수한 경우라는 것인데, 수학에서 "구체적 예시가 추상적 이론의 동기가 되고, 추상적 이론이 구체적 예시를 포괄한다"는 관계가 잘 드러난다. 아쉬운 점은 명제 6의 증명이 너무 간략하다는 것인데, orthogonal idempotent와 ideal의 대응 관계를 더 구체적으로 보여줬으면 이해가 쉬웠을 것 같다.

⚠️ 정의 없이 사용: $$C(A)$$ (ring의 center — 군론에서는 정의되었으나 ring 맥락에서의 정의는 없음)

## 카테고리 회고

환론은 세 글밖에 안 되지만, Euclidean domain → PID → UFD → integral domain이라는 계층과 CRT의 ideal 이론, 그리고 polynomial ring의 UFD 성질이라는 세 축이 깔끔하게 맞물린다. 정역에서 "좋은 원소"의 조건을 분류하고, 중국인의 나머지정리에서 "좋은 ideal의 조합"이 ring을 분해하며, 다항식환에서 그 이론들이 실제로 적용되는 대상을 만나는 구조가 잘 짜여 있다. 가장 막혔던 점은 irreducible과 prime의 차이인데, $$\mathbb{Z}$$에서는 둘이 같아서 구별할 필요가 없었지만 더일반적인 ring에서는 이 차이가 구조의 풍부함을 결정한다는 것이 새롭게 다가왔다. 대수적 구조 카테고리의 ring 일반 이론과 직접 연결되는 내용이라, prior 노트의 배경지식이 큰 도움이 되었다.

## [다항식환](/ko/math/ring_theory/polynomial_rings)

이 글은 commutative ring $$A$$ 위의 polynomial ring $$A[\x_i]_{i\in I}$$를 체계적으로 다룬다. 정역 글에서 "좋은 ring의 계층" — Euclidean domain ⊇ PID ⊇ UFD — 을 봤고, 중국인의 나머지정리 글에서 ideal의 comaximal 조건이 ring을 어떻게 분해하는지를 봤다면, 여기서는 그 이론들이 실제로 적용되는 핵심 대상인 polynomial ring을 본격적으로 분석하는 것이다. 출발점은 다항식의 degree 정의인데, multidegree $$\lvert\nu\rvert=\sum\nu_i$$를 이용해 $$A[\x_i]_{i\in I}$$를 $$\mathbb{N}$$-graded ring으로 볼 수 있다는 관찰이, 대수적 구조 카테고리의 등급환에서 본 graded ring의 구체적 실현이다.

보조정리 3이 이 글의 첫 번째 핵심이다. $$A$$가 integral domain이면 (1) $$\deg(uv)=\deg(u)+\deg(v)$$, (2) $$A[\x]$$의 unit은 $$A$$의 unit, (3) $$A[\x]$$는 integral domain — 이 셋이 동시에 따라온다. 증명에서 최고차항의 계수 $$a_nb_m$$이 0이 되지 않으려면 $$A$$에 zerodivisor가 없어야 한다는 것이 핵심인데, 정역 글에서 integral domain의 정의("zerodivisor가 없음")가 이렇게 구체적으로 활용되는 순간이다. 명제 4로 다변수까지 확장되는 것도 자연스럽다 — $$A[\x_1,\x_2]\cong(A[\x_1])[\x_2]$$라는 isomorphism을 반복 적용하면 되므로, 본질적으로 일변수의 결과를 반복하는 것이다.

명제 5(일반 ring에서의 나눗셈 알고리즘)가 흥미롭다. $$b_n^k u=qv+r$$이라는 식에서 $$b_n^k$$가 등장하는 이유 — $$v$$의 leading coefficient가 invertible하지 않으면 차수를 맞추기 위해 $$b_n$$을 곱해야 한다 — 가 명확하고, $$b_n$$이 invertible하면 $$k=1$$로 줄어든다는 관찰이, 정역 글에서 Euclidean domain의 division algorithm과 직접 연결된다. 특히 $$A=\mathbb{K}$$가 field이면 $$\mathbb{K}[\x]$$가 Euclidean domain이라는 결론(명제 6)은, degree 함수 $$N:u\mapsto\deg(u)$$가 Euclidean norm 역할을 한다는 것이 핵심인데 — "degree가 곧 norm"이라는 관찰이 이 글 전체를 관통하는 아이디어다.

근과 multiplicity의 부분(명제 7-9)은 실용적이다. $$u(a)=0 \iff (\x-a)\mid u$$라는 FACTOR theorem은 중학교 때부터 알던 결과인데, 여기서는 integral domain $$A$$ 위에서 정밀하게 증명된다. 명제 8에서 multiplicity의 덧셈/곱셈 규칙이 깔끔하고, 특히 $$uv$$에서의 multiplicity가 $$p+q$$인 것이 integral domain 가정을 직접 사용한다는 점이 좋다. 근의 개수가 차수를 넘지 않는다는 결론(명제 9 이후)으로부터 Lagrange 보간법(명제 10)이 나오는 것도 자연스럽다 — $$n$$개의 점을 지나는 $$n-1$$차 이하 다항식이 유일하다는 것이, 다항식이 "유연하면서도 엄밀한" 대상이라는 것을 보여준다.

formal derivative 부분(명제 11-12)은 다중선형대수학 카테고리의 미분에서 derivation을 정의한 것의 구체적 실현이다. 글 자체에서 "이 카테고리에서는 이러한 논의 없이 정의로서" $$D$$를 도입한다고 명시하고 있어서, 다중선형대수학의 내용을 모르더라도 따라가는 데 문제는 없지만, Leibniz 법칙 $$D(uv)=(Du)v+u(Dv)$$가 derivation의 정의였다는 것을 알고 있으면 더 깊이 이해된다. $$a$$가 simple root이려면 $$Du$$의 근이 아니면 된다는 것(명제 11)과, multiplicity $$k$$인 근이 $$Du$$에서 multiplicity $$\geq k-1$$을 가진다는 것(명제 12)은, "미분이 근의 구조를 읽는 도구"라는 직관을 정확히 formalize한다. 다만 $$k\cdot 1$$이 $$A$$에서 cancellable해야 한다는 조건이 붙는 것이 약간 까다로운데 — $$\mathbb{Z}/p\mathbb{Z}$$에서 $$p\cdot 1=0$$이 되는 경우를 배제하기 위한 것이라는 것은 계산을 해보고 나서야 이해했다.

Gauss의 lemma(명제 14)와 정리 16($$A$$가 UFD이면 $$A[\x]$$도 UFD)이 이 글의 하이라이트다. $$A[\x]$$의 다항식을 $$\Frac(A)[\x]$$에서 인수분해한 뒤, $$A$$의 irreducible element들로 약분해서 $$A[\x]$$에서의 인수분해를 얻는 논증이 — "field에서 인수분해하고, ring으로 되돌아온다"는 전략이 — 매우 강력하다. 정역 글에서 Euclidean domain $$\implies$$ PID $$\implies$$ UFD라는 계층을 봤는데, 여기서는 "UFD 위의 polynomial ring은 다시 UFD"라는 닫힘 성질이 추가된다. 이로부터 $$\mathbb{Z}[\x_1,\ldots,\x_n]$$이나 $$\mathbb{K}[\x_1,\ldots,\x_n]$$가 UFD라는 결론이 나오고, 이는 이후 가환대수학이나 대수기하학에서 다항식 ideal을 다룰 때 핵심적으로 사용될 것이다.

유리식환과 멱급수환(정의 17 이후)은 polynomial ring의 두 가지 "확장"이다. 유리식환 $$\mathbb{K}(\x_i)_{i\in I}$$는 $$\mathbb{K}[\x_i]_{i\in I}$$의 field of fraction으로, 분수체 글에서 본 construction의 구체적 실현이다. 멱급수환 $$A[[\x_i]]_{i\in I}$$는 다항식의 유한합을 무한합으로 확장한 것인데, order 함수 $$\omega$$가 degree의 역할을 대체한다는 것이 자연스럽다. 가장 인상적인 것은 명제 20 — $$u\in A[[\x_i]]$$가 invertible이려면 상수항만 invertible하면 된다는 것이다. 다항식 ring에서는 unit이 $$A$$의 unit뿐이었는데(보조정리 3), 멱급수 ring에서는 $$(1-\x)(1+\x+\x^2+\cdots)=1$$이라는 예시에서 보듯 상수항만 invertible하면 전체가 invertible해진다는 것이 놀랍다. 이 차이가 "유한"과 "무한"의 차이에서 오는 것이라는 직관이 드는데, 이후 완비화(completion)에서 $$\hat{A}=\varprojlim A/\mathfrak{a}^n$$을 다룰 때 이 멱급수 ring의 구조가 다시 등장할 것이라는 예감이 있다.
