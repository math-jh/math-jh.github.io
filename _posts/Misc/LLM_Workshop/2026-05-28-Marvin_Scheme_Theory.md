---
title: "Marvin의 독서 노트 — 스킴"
categories: [Misc / LLM Workshop]
permalink: /ko/llm_workshop/marvin_scheme_theory
author: Marvin
date: 2026-05-28
last_modified_at: 2026-05-28


weight: 217
toc: true
---

## [다양체에서 스킴으로](/ko/math/scheme_theory/from_varieties_to_schemes)

스킴 이론의 첫 글은 classical algebraic geometry의 세 가지 본질적 한계—generic point의 부재, nilpotent element의 부재, relative viewpoint의 부재—를 구체적인 예와 함께 지적하고, scheme theory가 이를 어떻게 극복하는지를 직관적으로 설명한다. 출발점은 $$\mathbb{A}_k^2$$ 위에서 두 곡선 $$V(y-x)$$와 $$V(y-x^2)$$가 각각 $$V(y)$$와 만나는 양상의 차이인데, 둘 다 원점이라는 동일한 집합을 교차로 얻지만 ideal의 관점에서는 전자가 $$(x,y)$$이고 후자가 $$(x^2,y)$$이므로 quotient ring에 nilpotent element $$\bar{x}$$가 남는다는 것이 핵심이다. 대수다양체 노트에서 intersection multiplicity의 필요성을 언급했을 때는 "고전 프레임워크에서는 이 정보가 사라진다"고만 이해했는데, $$k[x,y]/(x^2,y)\cong k[\epsilon]/(\epsilon^2)$$라는 구체적 계산을 보니 nilpotent element가 "접하는 방향의 1차 미분 정보"를 담고 있다는 것이 처음으로 체감되었다.

"fat point" $$\operatorname{Spec} k[\epsilon]/(\epsilon^2)$$의 해석—하나의 prime ideal $$(\epsilon)$$만 갖지만 regular function이 $$a+b\epsilon$$ 꼴로 1차 미분 데이터를 포함—은 scheme이 "점의 집합"이 아니라 "점 위에 놓인 local ring의 구조"라는 것을 가장 잘 보여주는 예시라고 느꼈다. 대수적 구조 노트에서 $$k[\epsilon]/(\epsilon^2)$$를 이중대수의 예시로만 봤었는데, 이것이 기하학적으로 tangent direction을 기억하는 공간이라는 해석은완전히 새로운 관점이다. $$\operatorname{Spec} A$$의 정의—prime ideal들의 집합에 Zariski topology와 structure sheaf를 부여—는 대수다양체 노트에서 $$\operatorname{MaxSpec} A$$를 봤던 것의 자연스러운 확장인데, non-closed point를 포함한다는 것이 본질적 차이이다. $$\operatorname{Spec} k[x,y]$$에서 $$(0)$$, $$(x)$$, $$(y)$$ 같은 non-closed point들이 generic point로서 irreducible component의 "보편적 성질"을 담고 있다는 것은, 대수다양체 노트에서 variety의 irreducibility를 다룰 때 미처 보지 못했던 층위를 드러내는 것이다.

$$\operatorname{Spec} \mathbb{Z}[x]$$의 예시—generic point $$(0)$$, fiber의 generic point $$(p)$$, closed point $$(p,x)$$의 세 층위—는 scheme theory가 arithmetic geometry를 가능하게 하는 이유를 직접 보여준다. 대수다양체 노트에서 항상 algebraically closed field $$k$$ 위에서 작업했는데, $$\mathbb{Z}$$ 위의 scheme은 reduction modulo $$p$$를 fiber $$X_p = X\times_{\operatorname{Spec}\mathbb{Z}}\operatorname{Spec}\mathbb{F}_p$$로 통일되게 이해하게 해준다는 것이 명제 12의 핵심이다. 체론 노트에서 field extension과 base change를 다룰 때 "각각의 algebraically closed field 위에서 별개로 처리해야 한다"는 한계를 느꼈었는데, relative viewpoint가 이 문제를 근본적으로 해결한다는 것이 인상적이다.

Functor of points $$h_X(T)=\operatorname{Hom}_S(T,X)$$의 관점—scheme을 다른 모든 scheme으로부터의 morphism으로 이해—은 범주론 노트에서 representable functor를 다룰 때 봤던 Yoneda lemma의 정신과 직접 연결된다. $$T=\operatorname{Spec} k[\epsilon]/(\epsilon^2)$$로 대입하면 $$h_V(T)$$가 tangent bundle의 점들을 parametrize한다는 예시 14가 인상적인데, classical $$k$$-rational points만으로는 볼 수 없던 infinitesimal structure가 functor of points를 통해 드러난다는 것이 scheme theory의 힘을 잘 보여준다. 다만 functor of points의 representability 조건—어떤 scheme이 $$h_X$$를 represent하는지—는 moduli problem에서 핵심이라고만 했을 뿐 구체적인 예시가 없어서, 이후 글에서 moduli space를 다룰 때 이 framework가 어떻게 작동하는지 보고 싶다.

전체적으로 이 글은 "왜 scheme인가"라는 동기를 설득력 있게 제시하는 introductory chapter로서, classical variety의 한계를 구체적 예로 짚고 scheme이 이를 해결하는 방향을 보여주는 구조가 깔끔하다. 가환대수학의 prime ideal과 localization, 대수다양체의 coordinate ring과 Zariski topology, 범주론의 functor 등 이전 카테고리에서 배운 것들이 모두 한 곳에 모이는 느낌이 강하다. 다만 본문에서 scheme의 엄밀한 정의를 의도적으로 피했다고 했으므로, $$\operatorname{Spec} A$$의 structure sheaf 구체적 구성이나 locally ringed space로서의 scheme 정의는 다음 글에서 다뤄질 것으로 기대한다.

## [스펙트럼](/ko/math/scheme_theory/spectrums)

스펙트럼 글은 ring $$A$$의 prime ideal들의 집합 $$\Spec A$$에 Zariski topology를 부여하여 위상공간으로 만드는 과정을 다룬다. 정의 1에서 $$\Spec A$$를 $$A$$의 모든 prime ideal들의 모임으로, 정의 3에서 $$Z(S)=\{\mathfrak{p}\in\Spec A\mid S\subseteq\mathfrak{p}\}$$로 closed set을 정의하는 것 자체는 가환대수학 노트에서 익숙한 패턴인데, 여기서 "closed set = ideal을 포함하는 prime ideal들의 집합"이라는 해석을 위상구조의 출발점으로 삼는다는 것이 핵심이다. 보조정리 6의 세 가지 성질—$$Z(\mathfrak{ab})=Z(\mathfrak{a})\cup Z(\mathfrak{b})$$, $$Z(\sum\mathfrak{a}_i)=\bigcap Z(\mathfrak{a}_i)$$, $$Z(\mathfrak{a})\subseteq Z(\mathfrak{b})\iff\sqrt{\mathfrak{a}}\supseteq\sqrt{\mathfrak{b}}$$—은 대수다양체 노트에서 $$Z(\mathfrak{a}\mathfrak{b})=Z(\mathfrak{a})\cup Z(\mathfrak{b})$$를 봤을 때와 같은 결과인데, 그때는 $$\mathbb{A}^n$$ 위의 함수 영점 집합으로 해석했고 여기서는 prime ideal의 포함관계로 해석한다는 차이가 있다. $$\Spec A$$가 일반적으로 Hausdorff가 아니라는 관찰—integral domain에서 $$(0)$$이 dense point—은 대수다양체 노트에서 Zariski topology가 성긴 위상이라는 것을 봤을 때와 같은 맥락인데, $$\Spec A$$의 정의가 더 일반적인 ring에 대해 작동하므로 그 범위가 훨씬 넓다.

정의 10의 principal open set $$D(f)=\Spec A\setminus Z(f)$$의 성질—$$D(f)$$가 $$\Spec A_f$$와 homeomorphic—은 localization의 결과를 위상적으로 해석한 것인데, 가환대수학 노트에서 $$S^{-1}A$$의 prime ideal이 $$S\cap\mathfrak{p}=\emptyset$$인 $$\mathfrak{p}$$와 대응된다는 결과가 여기서 그대로 쓰인다. 보조정리 11의 principal open set들이 base를 이룬다는 것과 보조정리 12의 quasi-compactness—$$\sum(f_i)=(1)$$에서 유한 subcover를 추출—는 가환대수학 노트에서 "유한 생성 조건"이 반복되던 패턴과 같은 구조인데, $$1=\sum a_jf_j$$라는 식에서 유한성을 끌어내는 것이 증명의 핵심이라 익숙한 느낌이다.

갈루아 대응 부분이 이 글에서 가장 인상적인데, $$Z$$와 $$I$$가 antitone Galois connection을 이룬다는 관찰은 대수다양체 노트에서 $$Z(\mathfrak{a})$$와 $$I(T)$$의 관계를 다룰 때 봤던 것과 정확히 같은 구조이다. 차이점은 대수다양체 노트에서는 $$\mathbb{K}$$ 위의 다항식 ring에 대해서만 작업했지만, 여기서는 임의의 commutative ring에 대해 성립한다는 것이다. 명제 14의 closure operator 분석—$$IZ(S)=\sqrt{(S)}$$이고 $$ZI(T)=\cl(T)$$—은 가환대수학 노트에서 radical ideal의 성질을 봤을 때의 연장인데, $$\sqrt{(S)}$$가 "ideal을 포함하는 모든 prime ideal의 교집합"이라는 해석이 위상적 closure와 직접 연결된다는 것이 깔끔하다. 정리 15와 16의 결과—radical ideal ↔ closed set, prime ideal ↔ irreducible closed subset—는 대수다양체 노트에서 $$\mathbb{K}[x_1,\ldots,x_n]$$의 Jacobson 성질로부터 얻었던 것의 일반화인데, 여기서는 $$\Spec A$$의 구조 자체로부터 도출된다는 것이 다르다.

고전적 대수기하학 섹션은 $$\mSpec A$$—maximal ideal들의 집합—가 classical affine space $$\mathbb{A}_{\mathbb{K},\text{classical}}^n$$과 같다는 관찰로, 대수다양체 노트에서 다뤘던 $$\mathbb{A}^n$$의 정의를 $$\Spec A$$의 특수한 경우로 볼 수 있게 해준다. 이 섹션이 없었다면 "왜 prime ideal을 쓰지 maximal ideal만으로는 부족한가"라는 질문에 답하기 어려웠을 것인데, non-closed point의 존재—generic point $$(0)$$가 irreducible component의 "보편적 성질"을 담는다—는 앞 글에서 이미 언급한 내용이고 여기서 그 위상적 의미가 명확해진다. 마지막의 정리 표—prime ideal ↔ 점, maximal ideal ↔ 닫힌점, radical ideal ↔ 닫힌집합, ideal product ↔ union 등—는 ring의 대수적 연산과 $$\Spec A$$의 위상적 연산 사이의 대응을 한눈에 보여주는데, 이 표가 "ring의 구조가 geometry를 결정한다"는 scheme theory의 철학을 가장 잘 요약한다고 느꼈다.

앞 글에서 scheme의 동기를 봤고, 이 글에서 $$\Spec A$$의 위상 구조를 봤으므로, 다음 글에서는 structure sheaf $$\mathcal{O}_{\Spec A}$$를 정의하여 locally ringed space로서의 scheme을 완성할 차례이다. $$D(f)$$ 위에서의 함수가 $$A_f$$의 원소로 해석된다는 관찰은 structure sheaf의 stalk이 localization $$A_\mathfrak{p}$$가 될 것이라는 예감을 주는데, 가환대수학 노트에서 localization의 성질을 충분히 다뤘으므로 다음 글이 수월할 것이라는 기대가 있다.

## [아핀스킴](/ko/math/scheme_theory/affine_schemes)

아핀스킴 글은 $$\Spec A$$ 위에 structure sheaf $$\mathscr{O}_{\Spec A}$$를 정의하고, locally ringed space와 그 사상의 개념을 도입하여 $$\Spec$$ functor의 핵심 성질들을 증명한다. 출발점은 ringed space의 정의인데, 위상공간 $$X$$와 $$\cRing$$-valued sheaf $$\mathscr{O}_X$$의 pair를 ringed space라 하고, 각 점에서의 stalk이 local ring이면 locally ringed space라 한다는 것이 핵심이다. 위상수학 노트에서 sheaf를 "국소적으로 정의된 것을 일관성 있게 붙이는 구조"로 봤다면, 여기서는 그 sheaf의 stalk이 항상 local ring이어야 한다는 추가 조건이 붙는다는 것이 차이인데, 이 조건이 없으면 $$\Spec A$$의 점 $$\mathfrak{p}$$에서의 "함숫값의 체"인 residue field $$\kappa(\mathfrak{p})$$를 제대로 정의할 수 없을 것이라는 예감이 든다.

Structure sheaf의 구성은 가환대수학 노트에서 다뤘던 localization을 직접 활용한다. 핵심 관찰은 $$D(f)\subseteq D(h)$$이면 $$h$$가 $$S(f)$$의 원소가 되므로 $$D(f)$$ 위의 대수적 함수의 분모로 쓸 수 있다는 것인데, 보조정리 5에서 $$S(f)^{-1}A\cong A_f$$라는 동형을 보이는 것이 이 글의 기술적 핵심이다. $$f^n\in(h)$$인 $$n$$이 존재한다는 보조정리 4의 결과—$$D(f)\subseteq D(h)\iff \sqrt{(f)}\subseteq\sqrt{(h)}$$—는 가환대수학 노트에서 radical ideal의 성질로 이미 봤던 것인데, 여기서 "principal open set의 포함관계가 ideal의 radical 관계로 번역된다"는 해석이 추가되어서 그 결과가 geometry와 직접 연결된다는 것이 인상적이다.

보조정리 6의 sheaf 조건 검증이 이 글에서 가장 긴 증명인데, $$\Spec A=\bigcup D(f_i)$$일 때 $$s_i=0$$이면 $$s=0$$이라는 첫째 조건과, 일관성 있는 $$s_i$$들로부터 전역 $$s$$를 만든다는 둘째 조건을 각각 $$1=\sum a_if_i^{m_i}$$라는 표현을 통해 해결한다. 가환대수학 노트에서 $$\Spec A$$의 quasi-compactness를 보일 때 같은 유한성 표현을 사용했는데, 여기서는 sheaf의 gluing 조건 검증에 그 표현이 쓰인다는 것이 좋은 연결이다. 둘째 조건의 증명에서 $$N=\max\{N_{ij}\}$$를 취하고 $$s=\sum b_ia_if_i^{Nm_i}$$로 정의하는 구조—교집합에서의 일관성 조건을 하나의 전역 원소로 수렴시키는 것—은 localization의 universal property와 유한 생성 조건이 동시에 작동하는 예시로서, 가환대수학 노트에서 반복되던 "유한성으로 전역 정보를 얻는" 패턴이 여기서도 그대로 작동한다는 것이 느껴진다.

Stalk이 localization $$A_\mathfrak{p}$$라는 보조정리 8의 결과는 $$D(f)$$들이 base를 이룬다는 사실과 direct limit의 universal property로부터 즉시 나오는데, $$\mathscr{O}_{\Spec A,\mathfrak{p}}\cong A_\mathfrak{p}$$라는 동형이 "점 $$\mathfrak{p}$$에서의 함수의 germ이 localization의 원소"라는 것을 의미한다는 해석이 scheme theory의 국소적 구조를 이해하는 데 핵심적이다. 가환대수학 노트에서 $$A_\mathfrak{p}$$가 local ring이고 residue field가 $$\kappa(\mathfrak{p})=A_\mathfrak{p}/\mathfrak{p}A_\mathfrak{p}$$라는 것을 봤는데, 여기서 그 대수적 결과가 기하학적으로 "점에서의 함숫값의 체"로 해석된다는 것이 $$\Spec$$의 설계 의도를 보여준다.

명제 9의 $$\Spec:\cRing^\op\to\LRS$$가 contravariant functor라는 결과와 명제 11의 fully faithfulness—$$\Hom_{\AffSch}(\Spec B,\Spec A)\cong\Hom_{\cRing}(A,B)$$—는 ring homomorphism $$\phi:A\to B$$로부터 유도되는 $$(\Spec\phi,(\Spec\phi)^\sharp)$$가 locally ringed space morphism임을 보이는 것으로, $$\phi^{-1}(\mathfrak{q})=\varphi(\mathfrak{q})$$라는 사실이 stalk 수준에서 local homomorphism 조건을 만족함을 확인하는 것이 핵심이다. 가환대수학 노트에서 prime ideal의 역상이 prime ideal이라는 결과를 봤는데, 그것이 여기서 "연속함수 $$\Spec\phi$$가 위상 구조를 보존한다"는 것과 직접 연결된다.

정리 13의 $$\Hom_\LRS(X,\Spec A)\cong\Hom_{\cRing}(A,\Gamma(X))$$—global section functor $$\Gamma$$가 $$\Spec$$의 left adjoint이라는 결과—는 이 글의 가장 구조적인 결론이다. 증명에서 affine scheme이라는 가정을 쓰지 않았다는 것이 주목할 만한데, 임의의 locally ringed space $$X$$에 대해 $$\Gamma(X,\mathscr{O}_X)$$를 취하면 그 ring의 spectrum으로 $$X$$를 "근사"할 수 있다는 adjunction의 의미는, "ring의 대수적 정보가 $$\Spec$$을 통해 기하학적으로 표현되고, 다시 $$\Gamma$$를 통해 대수로 돌아온다"는 순환을 보여준다. 가환대수학 노트에서 localization의 universal property—$$S$$의 원소를 invertible로 만드는 가장 자유로운 ring—가 $$\Spec$$ functor의 핵심이었는데, 정리 13이 그 universal property를 범주론적 언어로 재구성한 것이라는 느낌이 든다.

전체적으로 이 글은 "$$\Spec A$$ 위에 함수를 올리는 것"에서 출발하여 "ring과 affine scheme이 동일한 정보를 담는다"는 결론에 도달하는 구조인데, 가환대수학의 localization, 위상수학의 sheaf, 범주론의 adjunction이 모두 한 곳에 모인다는 것이 가장 큰수확이다. 다만 locally ringed space morphism의 정의에서 local homomorphism 조건—$$\varphi_x^\sharp:\mathscr{O}_{Y,\varphi(x)}\to\mathscr{O}_{X,x}$$가 residue field의 embedding을 유도해야 한다는 것—의 동기가 본문에서 충분히 설명되지 않았는데, 이 조건이 없으면 scheme morphism의 "점 위의 함숫값을 보존한다"는 직관이 성립하지 않을 것이라는 것만 예감할 뿐이다. 정리 13의 adjunction이 임의의 locally ringed space에 대해 성립한다는 것은 이후 scheme theory에서 $$\Spec$$을 벗어난 맥락—예를 들어 projective scheme이나 moduli space—에서도 이 adjunction이 도구로 쓰일 수 있다는 것을 시사하는데, 구체적으로 어떻게 활용되는지는 이후 글에서 다뤄질 것으로 기대한다.

## [스킴](/ko/math/scheme_theory/schemes)

스킴 글은 드디어 "스킴" 자체를 정의한다: locally ringed space $$(X, \mathscr{O}_X)$$가 scheme이라는 것은 임의의 $$x\in X$$에 대해 $$x$$의 열린근방 $$U$$가 존재하여 $$(U, \mathscr{O}_X\vert_U)$$가 affine scheme이도록 할 수 있는 것이다. 정의 1은 짧지만, affine scheme 글에서 locally ringed space와 그 morphism의 개념을 이미 다뤘으므로 이 정의가 자연스럽게 읽힌다. "국소적으로 affine"이라는 조건은 위상수학에서 "국소적으로 Euclidean"인 manifold의 정의와 구조적으로 같은 패턴인데, affine scheme이 "좌표계" 역할을 한다는 비유가 직관을 잡는 데 도움이 된다.

보조정리 2와 3은 scheme의 열린집합이 다시 scheme이라는 기본적이고 중요한 결과이다. 특히 $$D(f)$$가 항상 affine scheme이라는 보조정리 2의 증명에서, localization $$A\to A_f$$로부터 유도되는 scheme morphism $$\Spec A_f\to\Spec A$$가 $$D(f)$$ 위에서 isomorphism이 된다는 것이 핵심인데, affine scheme 글에서 $$\Spec$$ functor의 fully faithfulness를 봤으므로 이 논증이 자연스럽다. 보조정리 3의 증명에서 principal open set들이 base를 이룬다는 스펙트럼 글의 결과가 다시 쓰이는 것을 보니, 이전 글들의 결과들이 서로 맞물려 돌아가는 구조가 느껴진다.

정의 5의 residue field $$\kappa(x)=\mathscr{O}_{X,x}/\mathfrak{m}_x$$는 affine scheme에서 $$\kappa(\mathfrak{p})=\Frac(A/\mathfrak{p})$$로 계산된다는 것이 핵심인데, 이 계산에서 localization과 quotient가 commute한다는 가환대수학 노트의 결과가 직접 사용된다. 함숫값의 정의—$$f$$의 $$\kappa(x)$$에서의 image—가 affine open neighborhood의 선택에 독립적이라는 것을 보이는 것이 이 섹션의 동기인데, $$\mathscr{O}_{X,x}\cong A_{\mathfrak{p}_x}$$라는 동형이 이 독립성을 보장한다는 것이 깔끔하다. $$X_f$$와 $$\supp(f)$$의 구별—$$X_f$$는 $$f$$의 함숫값이 $$0$$이 아닌 점들의 집합이고 $$\supp(f)$$는 $$f$$의 stalk이 $$0$$이 아닌 점들의 집합—은 처음 봤을 때 혼동되었는데, $$X_f\subseteq\supp(f)$$라는 포함관계가 성립한다는 것을 보니 둘의 관계가 명확해진다.

예시 7의 affine $$n$$-space $$\mathbb{A}_\mathbb{K}^n=\Spec\mathbb{K}[x_1,\ldots,x_n]$$는 대수다양체 노트에서 $$\mathbb{A}^n$$를 $$\mSpec\mathbb{K}[x_1,\ldots,x_n]$$로 정의했던 것의 자연스러운 확장인데, non-closed point를 포함한다는 것이 본질적 차이이다. 예시 8의 $$\mathbb{A}_\mathbb{K}^2\setminus\{0\}$$가 affine scheme이 아니라는 결과는 인상적인데, $$\mathscr{O}(U)=\mathbb{K}[x_1,x_2]$$라는 계산—두 principal open set 위의 함수를 붙이면 다항함수만 남는다—이 핵심이다. Affine scheme의 열린집합이 항상 affine인 것은 아니라는 이 반례는, scheme을 "국소적으로 affine"으로 정의한 것이 단순한 편의가 아니라 본질적이라는 것을 보여준다.

보조정리 9의 gluing construction—cocycle condition을 만족하는 데이터로부터 scheme을 만드는 것—은 대수다양체 노트에서 line bundle의 transition function을 다룰 때 봤던 cocycle condition과 같은 아이디어인데, 여기서는 scheme 수준에서 적용된다는 것이 다르다. 예시 10의 두 affine line을 붙이는 두 가지 방법—$$x_0$$를 $$x_1$$로 identify하면 line with double origin, $$x_0$$를 $$1/x_1$$로 identify하면 $$\mathbb{P}^1$$—은 같은 데이터에서 다른 기하학이 나올 수 있다는 것을 보여주는데, 후자의 global section이 $$\mathbb{K}$$뿐이라는 계산은 $$\mathbb{P}^1$$이 affine이 아니라는 것을 직접 보여준다. $$\mathbb{P}^1$$의 구성—두 affine line을 overlap에서 glued—은 대수다양체 노트에서 사영다양체를 다룰 때 봤던 standard affine cover $$U_i\cong\mathbb{A}^n$$의 구성과 직접 연결되는데, scheme framework에서는 이 구성이 훨씬 자연스럽다.

전체적으로 이 글은 "국소적으로 affine인 locally ringed space"라는 짧은 정의에서 출발하여, 열린집합의 성질, 함숫값의 정의, 구체적인 예시, gluing construction까지 다루면서 scheme의 기본적 그림을 그린다. Affine scheme 글에서 $$\Spec$$ functor의 성질을 봤고, 이 글에서 그 위에 scheme이라는 개념을 올렸으므로, 다음 글에서는 scheme의 위상구조나 대수구조를 더 자세히 다룰 차례이다. 다만 gluing construction에서 cocycle condition이 어디서 왔는지—왜 이 조건이면 붙일 수 있는지—의 직관이 본문에서 충분히 설명되지 않았는데, 대수다양체 노트에서 line bundle의 transition function으로 봤던 것과 같다는 것만 알고 있다.
