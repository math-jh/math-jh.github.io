---
title: "정칙성의 호몰로지 판정"
description: "Noetherian local ring이 regular인 것이 residue field의 projective dimension이 유한한 것과 동치라는 Auslander-Buchsbaum-Serre 정리를 증명하고, 그 귀결로 regular local ring의 국소화가 다시 regular임과 다항식환의 정칙성을 얻은 뒤, regular local ring이 UFD라는 Auslander-Buchsbaum 정리를 증명한다."
excerpt: "Auslander-Buchsbaum-Serre 정리와 regular local ring의 UFD 정리"

categories: [Math / Commutative Algebra]
permalink: /ko/math/commutative_algebra/homological_criterion_for_regularity
sidebar: 
    nav: "commutative_algebra-ko"

date: 2026-07-24
weight: 28
published: false
drift_needed: true

---

[§호몰로지 차원, ⁋명제 13](/ko/math/commutative_algebra/homological_dimension#prop13)에서 우리는 $d$차원 regular local ring의 global dimension이 정확히 $d$라는 것을 보였고, [§Auslander-Buchsbaum 공식](/ko/math/commutative_algebra/auslander_buchsbaum_formula)의 말미에서는 이 명제의 역이 성립한다는 것을 예고하였다. 이 글은 그 약속을 이행한다. 곧 Noetherian local ring $(A,\mathfrak{m},\kappa)$에 대하여 $\operatorname{gldim}A<\infty$이기만 하면 $A$는 regular local ring이며, 사실은 module 하나, 즉 residue field $\kappa$의 projective dimension이 유한하다는 조건만으로도 충분하다. 이것이 Auslander--Buchsbaum--Serre 정리이다.

Regular local ring이라는 개념은 본래 $\mathfrak{m}$의 generator 개수를 세는 조건으로 정의되었지만 ([§차원, ⁋정의 12](/ko/math/commutative_algebra/Krull_dimension#def12)), 이 정리는 그 조건을 free resolution의 언어로 완전히 다시 적는다. 이러한 관점 전환의 위력은 정의만으로는 접근하기 어려웠던 성질들이 형식적인 논증으로 얻어진다는 데에 있다. 우리는 그 대표적인 예로 regular local ring의 localization이 다시 regular local ring이라는 사실과 다항식환이 모든 prime ideal에서 regular라는 사실을 증명하고, 글의 후반부에서는 이 관점의 더 깊은 귀결인 Auslander--Buchsbaum 정리, 곧 임의의 regular local ring이 unique factorization domain이라는 정리를 증명한다.

## Auslander-Buchsbaum-Serre 정리

이 절 전체에서 $(A,\mathfrak{m},\kappa)$는 Noetherian local ring이다. 목표는 $\pd_A\kappa<\infty$로부터 $A$가 regular local ring이라는 것을 끌어내는 것이고, 논증은 $\kappa$-벡터공간 $\mathfrak{m}/\mathfrak{m}^2$의 차원에 대한 귀납법으로 진행된다. 귀납 단계에서는 $x\in\mathfrak{m}\setminus\mathfrak{m}^2$인 non-zerodivisor를 골라 $\overline{A}=A/xA$로 내려가는데, 이 환원이 작동하려면 가정 $\pd_A\kappa<\infty$가 quotient에서도 유지된다는 것, 곧 $\pd_{\overline{A}}\kappa<\infty$를 알아야 한다. [§Auslander-Buchsbaum 공식, ⁋보조정리 2](/ko/math/commutative_algebra/auslander_buchsbaum_formula#lem2)는 $x$가 regular인 module의 projective dimension이 quotient에서 보존된다는 것을 말해주지만, $x\in\mathfrak{m}$은 $\kappa$를 annihilate하므로 $\kappa$ 자체에는 적용할 수 없다. 대신 우리는 $\mathfrak{m}$에 이를 적용한 뒤, $\overline{A}$-module $\mathfrak{m}/x\mathfrak{m}$이 $\kappa$를 direct summand로 가진다는 다음의 관찰로 $\kappa$를 회수한다.

::: 보조정리 1
Noetherian local ring $(A,\mathfrak{m},\kappa)$가 field가 아니라 하고, $x\in\mathfrak{m}\setminus\mathfrak{m}^2$이 $A$-regular라 하자. $\overline{A}=A/xA$로 적으면, $\overline{A}$-module isomorphism

$$\mathfrak{m}/x\mathfrak{m}\cong (\mathfrak{m}/xA)\oplus\kappa$$

가 존재한다.
:::
::: 증명
우선 등장하는 세 module $\mathfrak{m}/x\mathfrak{m}$, $\mathfrak{m}/xA$, $\kappa$는 모두 $x$에 의해 annihilate되는 $A$-module이므로 (각각 $x\cdot\mathfrak{m}\subseteq x\mathfrak{m}$, $x\cdot\mathfrak{m}\subseteq xA$, $x\in\mathfrak{m}$이기 때문이다) 자연스럽게 $\overline{A}$-module이고, 이들 사이의 $A$-linear map은 곧 $\overline{A}$-linear map이다. 따라서 $A$-module로서 위의 분해를 얻으면 충분하다.

$n=\dim_\kappa(\mathfrak{m}/\mathfrak{m}^2)$이라 하자. $x\not\in\mathfrak{m}^2$이므로 $x$의 $\mathfrak{m}/\mathfrak{m}^2$에서의 image는 $0$이 아니고, 이를 $\kappa$-basis로 확장한 뒤 [§정수적 확장, ⁋보조정리 8](/ko/math/commutative_algebra/integral_extension#lem8)을 적용하면 $x,y_2,\ldots, y_n$이 $\mathfrak{m}$을 생성하며 그 image들이 $\mathfrak{m}/\mathfrak{m}^2$의 basis가 되도록 할 수 있다. $N=(y_2,\ldots, y_n)$으로 두면 (단 $n=1$인 경우는 $N=0$) $\mathfrak{m}=xA+N$이다.

첫째로 $xA\cap N\subseteq x\mathfrak{m}$임을 보인다. $h=xb\in N$이라 하고 $b\not\in\mathfrak{m}$이라 가정하면 $b$는 unit이고 ([§국소화, ⁋명제 2](/ko/math/commutative_algebra/localization#prop2)) $x=hb^{-1}\in N$이 되어 $\mathfrak{m}=xA+N=N$이 $n-1$개의 원소 $y_2,\ldots, y_n$으로 생성된다. 그럼 이들의 image가 $n$차원 $\kappa$-벡터공간 $\mathfrak{m}/\mathfrak{m}^2$을 생성해야 하므로 모순이다. 따라서 $b\in\mathfrak{m}$이고 $h=xb\in x\mathfrak{m}$이다.

둘째로 $xA\cap(N+x\mathfrak{m})=x\mathfrak{m}$임을 보인다. $x\mathfrak{m}$이 좌변에 포함되는 것은 자명하다. 거꾸로 $ax=h+xs$ ($h\in N$, $s\in\mathfrak{m}$)라 하면 $h=x(a-s)\in xA\cap N\subseteq x\mathfrak{m}$이므로 $h=xt$이도록 하는 $t\in\mathfrak{m}$이 존재하고, 따라서 $ax=x(t+s)\in x\mathfrak{m}$이다.

이제 $\mathfrak{m}/x\mathfrak{m}$의 두 submodule $xA/x\mathfrak{m}$과 $(N+x\mathfrak{m})/x\mathfrak{m}$을 생각하자. $\mathfrak{m}=xA+N$이므로 이 둘의 합은 $\mathfrak{m}/x\mathfrak{m}$ 전체이고, 이 둘의 교집합은 $(xA\cap(N+x\mathfrak{m}))/x\mathfrak{m}=x\mathfrak{m}/x\mathfrak{m}=0$이다. 즉

$$\mathfrak{m}/x\mathfrak{m}=(xA/x\mathfrak{m})\oplus((N+x\mathfrak{m})/x\mathfrak{m})$$

이다.

첫째 성분을 계산하자. $a\mapsto ax+x\mathfrak{m}$으로 정의된 $A$-linear map $A \rightarrow xA/x\mathfrak{m}$은 surjective이고, 그 kernel은 $ax\in x\mathfrak{m}$이도록 하는 $a$들의 모임인데, $ax=xt$ ($t\in\mathfrak{m}$)라면 $x$가 $A$-regular이므로 $a=t\in\mathfrak{m}$이고 거꾸로 $a\in\mathfrak{m}$이면 $ax\in x\mathfrak{m}$이다. 따라서 kernel은 $\mathfrak{m}$이고 $xA/x\mathfrak{m}\cong A/\mathfrak{m}=\kappa$이다.

둘째 성분을 계산하자. 합성 $N+x\mathfrak{m}\hookrightarrow \mathfrak{m}\twoheadrightarrow \mathfrak{m}/xA$은 $\mathfrak{m}=xA+N$이므로 surjective이고, 그 kernel은 $(N+x\mathfrak{m})\cap xA=x\mathfrak{m}$이다. 따라서 first isomorphism theorem에 의하여 $(N+x\mathfrak{m})/x\mathfrak{m}\cong\mathfrak{m}/xA$이고, 원하는 분해를 얻는다.
:::

이 보조정리에서 $\mathfrak{m}/xA$는 다른 것이 아니라 $\overline{A}$의 maximal ideal $\overline{\mathfrak{m}}$이다. 즉 $\mathfrak{m}/x\mathfrak{m}\cong\overline{\mathfrak{m}}\oplus\kappa$이고, 좌변의 projective dimension은 [§Auslander-Buchsbaum 공식, ⁋보조정리 2](/ko/math/commutative_algebra/auslander_buchsbaum_formula#lem2)로 통제되므로 direct summand인 $\kappa$의 projective dimension도 따라서 통제된다.

조건 $x\not\in\mathfrak{m}^2$은 생략할 수 없다. 가령 $A=\mathbb{K}[[\x]]$에서 $x=\x^2$을 택하면 $\mathfrak{m}/x\mathfrak{m}=(\x)/(\x^3)$은 $\x$의 class로 생성되는 cyclic module로서 그 annihilator가 $(\x^2)$인 반면, $(\mathfrak{m}/xA)\oplus\kappa=(\x)/(\x^2)\oplus\kappa$는 $\mathfrak{m}$ 전체에 의해 annihilate되므로 두 module은 isomorphic하지 않다. 증명에서 $x$의 image를 $\mathfrak{m}/\mathfrak{m}^2$의 basis로 확장하는 첫 단계가 정확히 이 조건을 사용하는 자리이다. 위의 관찰을 정확히 적으면 다음과 같다.

::: 보조정리 2
[보조정리 1](#lem1)의 상황에서, $\pd_A\kappa<\infty$이면 $\pd_{\overline{A}}\kappa<\infty$이다.
:::
::: 증명
우선 $\pd_A\kappa\geq 1$임을 확인한다. 만일 $\pd_A\kappa=0$이라면 [§호몰로지 차원, ⁋명제 11](/ko/math/commutative_algebra/homological_dimension#prop11)에 의하여 $\kappa$의 minimal free resolution이 $F_0$에서 끝나므로 $\kappa\cong F_0$은 $0$이 아닌 free module인데, 그럼 $\ann(\kappa)=\ann(F_0)=0$이고 한편 $\ann(\kappa)=\mathfrak{m}$이므로 $\mathfrak{m}=0$이 되어 $A$가 field라는 모순을 얻는다.

이제 canonical surjection $\epsilon:A \rightarrow \kappa$는 $\ker\epsilon=\mathfrak{m}\subseteq\mathfrak{m}A$를 만족하므로, [§호몰로지 차원, ⁋명제 9](/ko/math/commutative_algebra/homological_dimension#prop9)가 주는 $\mathfrak{m}$의 minimal free resolution을 $\mathfrak{m}\hookrightarrow A$에 이어 붙이면 $F_0=A$인 $\kappa$의 minimal free resolution을 얻는다. 이 resolution의 길이는 $\mathfrak{m}$의 minimal free resolution의 길이보다 정확히 $1$ 크므로, [§호몰로지 차원, ⁋명제 11](/ko/math/commutative_algebra/homological_dimension#prop11)에 의하여

$$\pd_A\mathfrak{m}=\pd_A\kappa-1<\infty$$

이다.

한편 $x$는 $A$-regular이고 $\mathfrak{m}\subseteq A$이므로 곱하기 $x$는 $\mathfrak{m}$ 위에서도 injective, 곧 $x$는 $\mathfrak{m}$-regular이다. $A$가 field가 아니므로 $\mathfrak{m}\neq 0$이고, $\mathfrak{m}$은 finitely generated이므로 ([§기본 개념들, ⁋정리 3](/ko/math/commutative_algebra/basic_notions#thm3)) [§Auslander-Buchsbaum 공식, ⁋보조정리 2](/ko/math/commutative_algebra/auslander_buchsbaum_formula#lem2)의 둘째 결과를 $M=\mathfrak{m}$에 적용하면

$$\pd_{\overline{A}}(\mathfrak{m}/x\mathfrak{m})=\pd_A\mathfrak{m}<\infty$$

이다.

마지막으로 [보조정리 1](#lem1)의 분해 $\mathfrak{m}/x\mathfrak{m}\cong\overline{\mathfrak{m}}\oplus\kappa$를 사용한다. 일반적으로 두 module의 direct sum의 projective resolution은 각각의 projective resolution의 direct sum으로 택할 수 있고 $\Hom_{\overline{A}}(-,L)$은 유한한 direct sum을 direct product로 옮기므로, 임의의 $\overline{A}$-module $L$에 대하여

$$\Ext^i_{\overline{A}}(\mathfrak{m}/x\mathfrak{m},L)\cong \Ext^i_{\overline{A}}(\overline{\mathfrak{m}},L)\oplus\Ext^i_{\overline{A}}(\kappa,L)$$

이다. $t=\pd_{\overline{A}}(\mathfrak{m}/x\mathfrak{m})$으로 두면 [§호몰로지 차원, ⁋명제 2](/ko/math/commutative_algebra/homological_dimension#prop2)에 의하여 좌변이 $i=t+1$에서 모든 $L$에 대해 소멸하므로 $\Ext^{t+1}_{\overline{A}}(\kappa,L)=0$이 모든 $L$에 대해 성립하고, 다시 같은 명제에 의하여 $\pd_{\overline{A}}\kappa\leq t<\infty$이다.
:::

앞으로 $n=\dim_\kappa(\mathfrak{m}/\mathfrak{m}^2)$을 $A$의 *embedding dimension*이라 부르기로 한다. [§정수적 확장, ⁋보조정리 8](/ko/math/commutative_algebra/integral_extension#lem8)에 의하여 이는 $\mathfrak{m}$의 minimal generating set의 크기와 같고, [§매개계, ⁋명제 2](/ko/math/commutative_algebra/system_of_parameters#prop2)에 의하여 언제나 $n\geq\dim A$이며, 정의에 의하여 $A$가 regular local ring인 것은 등호가 성립하는 것이다. 이제 이 절의 주된 정리를 증명한다.

::: 정리 3 (Auslander--Buchsbaum--Serre)
Noetherian local ring $(A,\mathfrak{m},\kappa)$에 대하여 다음이 모두 동치이다.

1. $A$는 regular local ring이다.
2. $\operatorname{gldim}A<\infty$이다.
3. $\pd_A\kappa<\infty$이다.
:::
::: 증명
(1)$\Rightarrow$(2)는 [§호몰로지 차원, ⁋명제 13](/ko/math/commutative_algebra/homological_dimension#prop13)이 $\operatorname{gldim}A=\dim A<\infty$를 주므로 성립하고, (2)$\Rightarrow$(3)은 global dimension의 정의에 의해 자명하다. ([§호몰로지 차원, ⁋정의 6](/ko/math/commutative_algebra/homological_dimension#def6))

(3)$\Rightarrow$(1)을 embedding dimension $n=\dim_\kappa(\mathfrak{m}/\mathfrak{m}^2)$에 대한 귀납법으로 보인다.

$n=0$인 경우 $\mathfrak{m}=\mathfrak{m}^2$이므로 [§정수적 확장, ⁋보조정리 8](/ko/math/commutative_algebra/integral_extension#lem8)에 의하여 $\mathfrak{m}=0$이고, $A$는 field이다. 그럼 $\dim A=0$이고 $\mathfrak{m}$은 $0$개의 원소로 생성되므로 $A$는 regular local ring이다. ([§차원, ⁋정의 12](/ko/math/commutative_algebra/Krull_dimension#def12))

이제 $n\geq 1$이라 하고, embedding dimension이 $n-1$인 모든 Noetherian local ring에 대하여 주장이 성립한다고 가정하자. $\mathfrak{m}/\mathfrak{m}^2\neq 0$이므로 $\mathfrak{m}\neq 0$이고 $A$는 field가 아니다.

먼저 $\operatorname{depth}A\geq 1$임을 보인다. 만일 $\operatorname{depth}A=0$이라면, $\kappa$는 $\pd_A\kappa<\infty$를 만족하는 $0$이 아닌 finitely generated module이므로 [§Auslander-Buchsbaum 공식, ⁋따름정리 4](/ko/math/commutative_algebra/auslander_buchsbaum_formula#cor4)의 둘째 결과에 의하여 free여야 한다. 그런데 $0$이 아닌 free module의 annihilator는 $0$이고 $\ann(\kappa)=\mathfrak{m}$이므로 $\mathfrak{m}=0$이 되어 $n\geq 1$에 모순이다.

다음으로 $\mathfrak{m}^2$과 $A$의 associated prime들을 동시에 피하는 원소를 찾는다. [§동반소아이디얼, ⁋정리 7](/ko/math/commutative_algebra/associated_primes#thm7)에 의하여 $A$의 zerodivisor들의 모임은 유한집합 $\Ass A$의 원소들의 합집합이다. 만일

$$\mathfrak{m}\subseteq \mathfrak{m}^2\cup\bigcup_{\mathfrak{p}\in\Ass A}\mathfrak{p}$$

라면, 이 합집합에서 prime이 아닌 ideal은 $\mathfrak{m}^2$ 하나뿐이므로 [§동반소아이디얼, ⁋보조정리 2](/ko/math/commutative_algebra/associated_primes#lem2)에 의하여 $\mathfrak{m}$은 $\mathfrak{m}^2$ 또는 어떤 $\mathfrak{p}\in\Ass A$에 포함되어야 한다. 전자는 위에서 본 것처럼 $\mathfrak{m}=0$을 강제하여 모순이고, 후자의 경우 $A$가 local이므로 $\mathfrak{p}\subseteq\mathfrak{m}$과 종합하면 $\mathfrak{m}=\mathfrak{p}\in\Ass A$가 되어 [§Depth, ⁋따름정리 4](/ko/math/commutative_algebra/depth#cor4)의 첫째 결과로부터 $\operatorname{depth}A=0$이라는 모순을 얻는다. 이 avoidance 논증은 [§정칙국소환, ⁋따름정리 1](/ko/math/commutative_algebra/regular_local_rings#cor1)의 증명에서 사용한 것과 동일한 패턴이다. 따라서 $\mathfrak{m}^2$에도, 어떠한 associated prime에도 속하지 않는 $x\in\mathfrak{m}$이 존재하며, 특히 $x$는 $A$-regular이고 $x\not\in\mathfrak{m}^2$이다.

$\overline{A}=A/xA$로 두자. [§Auslander-Buchsbaum 공식, ⁋보조정리 2](/ko/math/commutative_algebra/auslander_buchsbaum_formula#lem2)에서 살펴본 것처럼 $\overline{A}$는 maximal ideal $\overline{\mathfrak{m}}=\mathfrak{m}/xA$와 residue field $\kappa$를 갖는 Noetherian local ring이다. $\overline{A}$의 embedding dimension을 계산하면, $\overline{\mathfrak{m}}^2=(\mathfrak{m}^2+xA)/xA$이므로

$$\overline{\mathfrak{m}}/\overline{\mathfrak{m}}^2\cong\mathfrak{m}/(\mathfrak{m}^2+xA)$$

인데, $x\not\in\mathfrak{m}^2$이므로 $(\mathfrak{m}^2+xA)/\mathfrak{m}^2$은 $x$의 image로 생성되는 $\mathfrak{m}/\mathfrak{m}^2$의 $1$차원 부분공간이고, 따라서

$$\dim_\kappa(\overline{\mathfrak{m}}/\overline{\mathfrak{m}}^2)=\dim_\kappa(\mathfrak{m}/\mathfrak{m}^2)-1=n-1$$

이다.

[보조정리 2](#lem2)에 의하여 $\pd_{\overline{A}}\kappa<\infty$이므로, 귀납 가정에 의하여 $\overline{A}$는 regular local ring이다. 그럼 $\overline{\mathfrak{m}}$은 $\dim\overline{A}$개의 원소로 생성되고, 그 image들이 $\overline{\mathfrak{m}}/\overline{\mathfrak{m}}^2$을 생성하므로 $n-1\leq \dim\overline{A}$이며, 반대 부등식은 [§매개계, ⁋명제 2](/ko/math/commutative_algebra/system_of_parameters#prop2)가 주므로 $\dim\overline{A}=n-1$이다. 한편 $x$가 $A$-regular이므로 [§Depth, ⁋명제 9](/ko/math/commutative_algebra/depth#prop9)를 $M=A$에 적용하면 $\dim\overline{A}=\dim A-1$이고, 종합하면 $\dim A=n$이다. 그런데 $\mathfrak{m}$은 $n$개의 원소로 생성되므로 ($\mathfrak{m}/\mathfrak{m}^2$의 basis의 lift, [§정수적 확장, ⁋보조정리 8](/ko/math/commutative_algebra/integral_extension#lem8)), $A$는 regular local ring이다. ([§차원, ⁋정의 12](/ko/math/commutative_algebra/Krull_dimension#def12))
:::

정리의 셋째 조건이 실전에서 가장 유용하다. 어떤 local ring이 regular인지를 판정하는 데에 module 하나의 유한한 free resolution만 제시하면 되기 때문이다. 또, 정리와 [§호몰로지 차원, ⁋명제 13](/ko/math/commutative_algebra/homological_dimension#prop13)을 종합하면 Noetherian local ring의 global dimension은 무한하거나, 유한한 경우 정확히 $\dim A$와 같다는 것도 알 수 있다.

Regular local ring의 정의는 $\mathfrak{m}$이라는 특정한 ideal에 대한 조건이므로, regular local ring $A$의 prime ideal $\mathfrak{p}$에서의 localization이 다시 regular인지는 정의로부터 전혀 자명하지 않다. $\mathfrak{m}$의 generator들이 $\mathfrak{p}A_\mathfrak{p}$의 generator와 직접적인 관계가 없기 때문이다. 그러나 [정리 3](#thm3)의 셋째 조건은 localization과 잘 어울린다.

::: 따름정리 4
Regular local ring $A$와 임의의 prime ideal $\mathfrak{p}$에 대하여, $A_\mathfrak{p}$는 regular local ring이다.
:::
::: 증명
[§국소화, ⁋따름정리 9](/ko/math/commutative_algebra/localization#cor9)와 [§국소화, ⁋명제 8](/ko/math/commutative_algebra/localization#prop8)에 의하여 $A_\mathfrak{p}$는 $\mathfrak{p}A_\mathfrak{p}$를 유일한 maximal ideal로 갖는 Noetherian local ring이고, 그 residue field는 $\kappa(\mathfrak{p})=A_\mathfrak{p}/\mathfrak{p}A_\mathfrak{p}$이다. ([§국소화, ⁋정의 10](/ko/math/commutative_algebra/localization#def10))

Short exact sequence $0 \rightarrow \mathfrak{p} \rightarrow A \rightarrow A/\mathfrak{p} \rightarrow 0$을 $\mathfrak{p}$에서 localize하면 [§국소화의 성질들, ⁋명제 2](/ko/math/commutative_algebra/properties_of_localization#prop2)에 의하여 exactness가 보존되므로 $(A/\mathfrak{p})_\mathfrak{p}\cong A_\mathfrak{p}/\mathfrak{p}A_\mathfrak{p}=\kappa(\mathfrak{p})$이다. 같은 명제에 의하여 $A_\mathfrak{p}$는 flat $A$-module이고, [§국소화의 성질들, ⁋보조정리 1](/ko/math/commutative_algebra/properties_of_localization#lem1)에 의하여 $A_\mathfrak{p}\otimes_A(A/\mathfrak{p})\cong(A/\mathfrak{p})_\mathfrak{p}$이므로, [§호몰로지 차원, ⁋보조정리 15](/ko/math/commutative_algebra/homological_dimension#lem15)의 첫째 결과에 의하여

$$\pd_{A_\mathfrak{p}}\kappa(\mathfrak{p})=\pd_{A_\mathfrak{p}}\big(A_\mathfrak{p}\otimes_A(A/\mathfrak{p})\big)\leq \pd_A(A/\mathfrak{p})\leq\operatorname{gldim}A=\dim A<\infty$$

이다. 마지막 두 부등식은 각각 [§호몰로지 차원, ⁋정의 6](/ko/math/commutative_algebra/homological_dimension#def6)과 [§호몰로지 차원, ⁋명제 13](/ko/math/commutative_algebra/homological_dimension#prop13)에 의한 것이다. 따라서 [정리 3](#thm3)에 의하여 $A_\mathfrak{p}$는 regular local ring이다.
:::

이 따름정리 덕분에 regular라는 성질을 국소적 조건으로 놓는 다음의 정의가 의미를 가진다.

::: 정의 5
Noetherian ring $A$가 *regular ring<sub>정칙환</sub>*이라는 것은 $A$의 임의의 prime ideal $\mathfrak{p}$에 대하여 $A_\mathfrak{p}$가 regular local ring인 것이다.
:::

[따름정리 4](#cor4)에 의하여 regular local ring은 regular ring이며, 특히 field는 regular ring이다. 이 정의의 조건은 실은 maximal ideal에서만 확인해도 충분하다. 이를 살펴보기 위해 localization의 합성에 대한 일반적인 관찰 하나를 짚고 넘어간다. Multiplicative subset $S\subseteq A$와 $S\cap\mathfrak{q}=\emptyset$을 만족하는 prime ideal $\mathfrak{q}$에 대하여, canonical isomorphism

$$(S^{-1}A)_{\mathfrak{q}S^{-1}A}\cong A_\mathfrak{q}$$

가 존재한다. 실제로 canonical map $A \rightarrow A_\mathfrak{q}$는 $S\subseteq A\setminus\mathfrak{q}$의 원소를 unit으로 보내므로 [§국소화, ⁋명제 6](/ko/math/commutative_algebra/localization#prop6)에 의하여 ring homomorphism $S^{-1}A \rightarrow A_\mathfrak{q}$가 유도되고, [§국소화, ⁋명제 8](/ko/math/commutative_algebra/localization#prop8)에 의하여 $a/s\not\in\mathfrak{q}S^{-1}A$인 것이 $a\not\in\mathfrak{q}$인 것과 동치이므로 이 map은 $S^{-1}A\setminus\mathfrak{q}S^{-1}A$의 원소를 $A_\mathfrak{q}$의 unit으로 보내며, 다시 [§국소화, ⁋명제 6](/ko/math/commutative_algebra/localization#prop6)에 의하여 ring homomorphism $(S^{-1}A)_{\mathfrak{q}S^{-1}A} \rightarrow A_\mathfrak{q}$를 얻는다. 반대방향으로는 합성 $A \rightarrow S^{-1}A \rightarrow (S^{-1}A)_{\mathfrak{q}S^{-1}A}$가 $A\setminus\mathfrak{q}$의 원소를 unit으로 보내므로 (그 image가 maximal ideal $\mathfrak{q}(S^{-1}A)_{\mathfrak{q}S^{-1}A}$ 바깥에 있으므로) ring homomorphism $A_\mathfrak{q} \rightarrow (S^{-1}A)_{\mathfrak{q}S^{-1}A}$를 얻고, 두 합성이 각각 identity라는 것은 [§국소화, ⁋명제 6](/ko/math/commutative_algebra/localization#prop6)의 유일성으로부터 따라나온다.

이제 $A$의 prime ideal $\mathfrak{p}$가 주어지면 $\mathfrak{p}$를 포함하는 maximal ideal $\mathfrak{m}$이 존재하고 ([\[대수적 구조\] §환의 정의, ⁋정리 10](/ko/math/algebraic_structures/rings#thm10)), 위의 관찰을 $S=A\setminus\mathfrak{m}$에 적용하면 $A_\mathfrak{p}\cong(A_\mathfrak{m})_{\mathfrak{p}A_\mathfrak{m}}$이다. 따라서 $A_\mathfrak{m}$이 regular local ring이기만 하면 [따름정리 4](#cor4)에 의하여 $A_\mathfrak{p}$도 regular local ring이다.

::: 따름정리 6
Field $\mathbb{K}$에 대하여 $\mathbb{K}[\x_1,\ldots,\x_n]$은 regular ring이다.
:::
::: 증명
$A=\mathbb{K}[\x_1,\ldots,\x_n]$으로 두자. 방금의 논의에 의하여 임의의 maximal ideal $\mathfrak{m}$에 대해 $A_\mathfrak{m}$이 regular local ring임을 보이면 충분하다. [§호몰로지 차원, ⁋정리 17](/ko/math/commutative_algebra/homological_dimension#thm17)에 의하여 $\operatorname{gldim}A=n<\infty$이므로, [따름정리 4](#cor4)의 증명에서와 동일한 계산으로

$$\pd_{A_\mathfrak{m}}\kappa(\mathfrak{m})\leq\pd_A(A/\mathfrak{m})\leq\operatorname{gldim}A=n<\infty$$

이고, [정리 3](#thm3)에 의하여 $A_\mathfrak{m}$은 regular local ring이다.
:::

기하적으로 이 따름정리는 affine space가 모든 점에서, 나아가 모든 subvariety를 따라 매끄럽다는 사실의 대수적 표현이다. Regular라는 성질이 이제 finitely generated algebra의 세계에서도 안정적으로 확인되는 성질이 된 셈이다.

## 정칙국소환은 UFD

이 절에서는 한 걸음 더 나아가 Auslander--Buchsbaum 정리, 곧 regular local ring이 unique factorization domain이라는 것을 증명한다. UFD의 정의와 기본 성질들은 [\[환론\] §정역, ⁋정의 16](/ko/math/ring_theory/integral_domains#def16)에서 다루었다. Integral domain $A$의 $0$이 아닌 non-unit $p$가 *prime element*라는 것은 $p\mid ab$일 때마다 $p\mid a$ 또는 $p\mid b$가 성립하는 것이고 ([\[환론\] §정역, ⁋정의 11](/ko/math/ring_theory/integral_domains#def11)), 이는 principal ideal $(p)$가 $0$이 아닌 prime ideal인 것과 동치이다 ($p\mid ab$가 $ab\in(p)$와 같은 뜻이기 때문이다). Prime element는 언제나 irreducible이며 ([\[환론\] §정역, ⁋명제 12](/ko/math/ring_theory/integral_domains#prop12)), UFD에서는 그 역도 성립한다. ([\[환론\] §정역, ⁋명제 17](/ko/math/ring_theory/integral_domains#prop17))

한편 우리는 [§으뜸분해, ⁋정리 7](/ko/math/commutative_algebra/primary_decomposition#thm7)에서 Noetherian domain이 UFD인 것과 principal ideal에 대한 minimal prime들이 모두 principal인 것이 동치임을 이미 보인 바 있다. 이 절에서 사용할 판정은 이와 비슷한 정신의 것으로, prime ideal이 prime element를 하나라도 포함하는지를 묻는다.

::: 보조정리 7 (Kaplansky)
Noetherian integral domain $A$에 대하여, $A$가 UFD인 것과 $A$의 $0$이 아닌 임의의 prime ideal이 prime element를 포함하는 것이 동치이다.
:::
::: 증명
우선 $A$가 UFD라 하고 $0$이 아닌 prime ideal $\mathfrak{p}$가 주어졌다 하자. $0$이 아닌 $a\in\mathfrak{p}$를 택하면 $\mathfrak{p}\neq A$이므로 $a$는 non-unit이고, UFD의 정의에 의하여 $a=p_1\cdots p_r$로 irreducible element들의 곱으로 분해된다. 각 $p_i$는 [\[환론\] §정역, ⁋명제 17](/ko/math/ring_theory/integral_domains#prop17)에 의하여 prime element이고, $a\in\mathfrak{p}$와 $\mathfrak{p}$가 prime이라는 것으로부터 어떤 $p_i$가 $\mathfrak{p}$에 속한다.

거꾸로 $0$이 아닌 임의의 prime ideal이 prime element를 포함한다고 가정하자.

$$S=\{u\in A\mid \text{$u$ unit}\}\cup\{up_1\cdots p_r\mid \text{$u$ unit, $p_i$ prime element, $r\geq 1$}\}$$

로 두면 $S$는 $1$을 포함하고 곱셈에 대해 닫혀있는 multiplicative subset이며, $A$가 domain이므로 $0\not\in S$이다.

먼저 $S$가 saturated임을, 곧 $ab\in S$이면 $a\in S$이고 $b\in S$임을 곱해지는 prime element의 개수 $r$에 대한 귀납법으로 보인다. $ab$가 unit이면 $a,b$ 모두 unit이므로 $S$에 속한다. $ab=up_1\cdots p_r$ ($r\geq 1$)라 하면 $p_r\mid ab$이므로 일반성을 잃지 않고 $p_r\mid a$, 곧 $a=p_ra'$라 할 수 있다. 그럼 $p_ra'b=up_1\cdots p_r$에서 $A$가 domain이므로 $p_r$을 소거하여 $a'b=up_1\cdots p_{r-1}$을 얻고, 귀납 가정에 의하여 $a'\in S$, $b\in S$이다. $a'$가 unit이든 prime element들의 곱에 unit을 곱한 것이든, $a=p_ra'$는 다시 $S$의 원소이다.

이제 $0$도 unit도 아닌 $a\in A$가 $S$에 속하지 않는다고 가정하자. $S$가 saturated이므로 $(a)\cap S=\emptyset$이다. $(a)$를 포함하고 $S$와 만나지 않는 ideal들의 모임을 포함관계로 순서를 주어 생각하면, 이 모임은 $(a)$를 원소로 가져 공집합이 아니고, totally ordered subset의 합집합이 다시 $(a)$를 포함하며 $S$와 만나지 않는 ideal이 되므로 inductive하다. 따라서 [\[집합론\] §선택공리, ⁋정리 4](/ko/math/set_theory/axiom_of_choice#thm4)에 의하여 maximal element $\mathfrak{p}$가 존재한다. 만일 $\mathfrak{b}\supsetneq\mathfrak{p}$가 $S$와 만나지 않는 ideal이라면 $\mathfrak{b}$는 $(a)$도 포함하므로 $\mathfrak{p}$의 maximality에 모순이고, 따라서 $\mathfrak{p}$는 $S$와 만나지 않는 ideal 전체 가운데에서도 maximal하다. 그럼 [§국소화의 성질들, ⁋명제 7](/ko/math/commutative_algebra/properties_of_localization#prop7)에 의하여 $\mathfrak{p}$는 prime ideal이고, $1\in S$이므로 proper이며, $0\neq a\in\mathfrak{p}$이므로 $0$이 아니다. 가정에 의하여 $\mathfrak{p}$는 prime element $p$를 포함하는데, $p\in S$이므로 $\mathfrak{p}\cap S=\emptyset$에 모순이다.

그러므로 $0$이 아닌 임의의 non-unit은 $S$에 속하고, 곧 unit 곱하기 prime element들의 곱으로 적힌다. Prime element는 irreducible이고 ([\[환론\] §정역, ⁋명제 12](/ko/math/ring_theory/integral_domains#prop12)) prime element의 unit배도 prime element이므로, $a=up_1\cdots p_r$를 $(up_1)p_2\cdots p_r$로 읽으면 임의의 $0$이 아닌 non-unit이 irreducible element들의 곱으로 분해된다. 분해의 유일성을 위해 $p_1\cdots p_r=q_1\cdots q_m$이 성립한다 하자. 여기서 $p_i$들은 prime element, $q_j$들은 irreducible element들이다. $r$에 대한 귀납법을 쓰면, $p_r\mid q_1\cdots q_m$이므로 어떤 $j$에 대하여 $p_r\mid q_j$이고, $q_j$가 irreducible이고 $p_r$이 non-unit이므로 $q_j=wp_r$이도록 하는 unit $w$가 존재한다. $A$가 domain이므로 양변에서 $p_r$을 소거하고 귀납 가정을 적용하면, 적절한 재배열 후에 $r=m$이고 각 $p_i$와 $q_i$가 associate임을 얻는다. 임의의 irreducible 분해의 한쪽을 prime element 분해로 택할 수 있으므로 이는 임의의 두 irreducible 분해 사이의 유일성을 주고, 따라서 $A$는 UFD이다. ([\[환론\] §정역, ⁋정의 16](/ko/math/ring_theory/integral_domains#def16))
:::

증명을 살펴보면 역방향에서는 Noetherian 가정이 전혀 사용되지 않았다. 즉 이 판정은 임의의 integral domain에서 유효하지만, 우리의 용례는 모두 Noetherian이므로 위와 같이 적었다. 다음 보조정리는 Kaplansky 판정을 실제로 적용할 때 확인해야 하는 prime ideal의 범위를 codimension $1$짜리로 좁혀준다. 여기서 prime ideal의 codimension은 [§차원, ⁋정의 2](/ko/math/commutative_algebra/Krull_dimension#def2)에서 정의한 것으로, 문헌에 따라 *height*라고도 부른다.

::: 보조정리 8
Noetherian integral domain $A$에 대하여 다음이 성립한다.

1. $A$가 UFD라면, codimension $1$인 $A$의 임의의 prime ideal은 principal이다.
2. $0$이 아닌 $A$의 임의의 prime ideal은 codimension $1$인 prime ideal을 포함한다.
:::
::: 증명
첫째 결과를 보자. $\mathfrak{p}$가 codimension $1$인 prime ideal이라 하면 특히 $\mathfrak{p}\neq 0$이므로, [보조정리 7](#lem7)의 첫 문단에서와 같이 prime element $\pi\in\mathfrak{p}$가 존재한다. 그럼 $(\pi)$는 $0$이 아닌 prime ideal이고 $(\pi)\subseteq\mathfrak{p}$인데, 만일 $(\pi)\subsetneq\mathfrak{p}$라면 $A$가 domain이므로 prime ideal들의 chain $\mathfrak{p}\supsetneq(\pi)\supsetneq(0)$이 $\codim\mathfrak{p}\geq 2$를 주어 모순이다. 따라서 $\mathfrak{p}=(\pi)$는 principal이다.

둘째 결과를 보자. $0$이 아닌 prime ideal $\mathfrak{p}$와 $0$이 아닌 원소 $a\in\mathfrak{p}$를 택하고, $(a)$를 포함하며 $\mathfrak{p}$에 포함되는 prime ideal들의 모임을 역포함관계로 순서를 주어 생각하자. 이 모임은 $\mathfrak{p}$를 원소로 가지므로 공집합이 아니다. Totally ordered subset, 곧 포함관계에 대한 prime ideal들의 감소하는 chain이 주어지면 그 교집합 $\mathfrak{q}_0$도 $(a)$를 포함하는 prime ideal이다. 실제로 $bc\in\mathfrak{q}_0$이고 $b\not\in\mathfrak{q}_0$이면 chain의 어떤 원소 $\mathfrak{q}'$에 대해 $b\not\in\mathfrak{q}'$인데, chain의 임의의 원소 $\mathfrak{q}''$에 대하여 $\mathfrak{q}''\subseteq\mathfrak{q}'$이면 $b\not\in\mathfrak{q}''$이므로 $c\in\mathfrak{q}''$이고, $\mathfrak{q}''\supseteq\mathfrak{q}'$이면 $c\in\mathfrak{q}'\subseteq\mathfrak{q}''$이기 때문이다. 따라서 이 모임은 inductive하고, [\[집합론\] §선택공리, ⁋정리 4](/ko/math/set_theory/axiom_of_choice#thm4)에 의하여 역포함관계에 대한 maximal element, 곧 $(a)$를 포함하고 $\mathfrak{p}$에 포함되는 prime ideal 중 minimal한 $\mathfrak{q}$가 존재한다.

이러한 $\mathfrak{q}$는 실은 $(a)$를 포함하는 $A$의 prime ideal 전체 가운데에서 minimal하다. $(a)$를 포함하는 prime ideal $\mathfrak{q}'\subseteq\mathfrak{q}$는 자동으로 $\mathfrak{p}$에 포함되기 때문이다. 따라서 [§차원, ⁋정리 7](/ko/math/commutative_algebra/Krull_dimension#thm7)에 의하여 $\codim\mathfrak{q}\leq 1$이고, $A$가 domain이며 $\mathfrak{q}\supseteq(a)\neq 0$이므로 chain $\mathfrak{q}\supsetneq(0)$으로부터 $\codim\mathfrak{q}\geq 1$이다. 곧 $\mathfrak{q}\subseteq\mathfrak{p}$는 codimension $1$인 prime ideal이다.
:::

이 두 판정을 종합하면, Noetherian domain $A$가 UFD임을 보이는 문제는 codimension $1$인 prime ideal마다 prime element를 찾는 문제로 환원된다. Regular local ring에서 이를 수행할 때의 핵심 전략은 잘 고른 prime element $x$를 invert하여 더 작은 ring으로 옮겨가는 것인데, 그 과정에서 prime element를 다시 원래 ring으로 가져오는 다리가 필요하다.

::: 보조정리 9
Integral domain $A$의 prime element $x$를 고정하고, multiplicative subset $\{x^k\mid k\geq 0\}$에 대한 $A$의 localization을 $A_x$로 적자. 원소 $\pi\in A$가 $x\nmid\pi$를 만족하고 $\pi/1$이 $A_x$의 prime element라면, $\pi$는 $A$의 prime element이다.
:::
::: 증명
$A$가 domain이고 $x\neq 0$이므로 canonical map $A \rightarrow A_x$는 injective이다. $\pi/1$이 $0$이 아니고 unit이 아니므로 $\pi\neq 0$이고, $\pi$가 $A$의 unit이라면 $\pi/1$이 $A_x$의 unit이 되므로 $\pi$는 $A$의 non-unit이다.

이제 $\pi\mid ab$가 $A$에서 성립한다 하자. 그럼 $A_x$에서도 $\pi/1$이 $ab/1$을 나누므로, $\pi/1$이 prime element라는 가정에 의하여 일반성을 잃지 않고 $\pi/1\mid a/1$이라 할 수 있다. 곧 적당한 $c\in A$와 $m\geq 0$에 대하여 $a/1=(\pi/1)(c/x^m)$이고, $A$가 domain이므로 이는 $A$에서의 등식

$$x^ma=\pi c$$

와 같은 뜻이다. $m$에 대한 귀납법으로 $\pi\mid a$를 보인다. $m=0$이면 그 자체로 $\pi\mid a$이다. $m\geq 1$이면 $x\mid \pi c$인데 $x$가 prime element이고 $x\nmid\pi$이므로 $x\mid c$이고, $c=xc_1$으로 적은 뒤 domain에서 $x$를 소거하면 $x^{m-1}a=\pi c_1$이 되어 귀납 가정을 적용할 수 있다. 따라서 $\pi\mid a$이고, $\pi$는 $A$의 prime element이다.
:::

이 보조정리의 조건 $x\nmid\pi$는 생략할 수 없다. 가령 $\pi=x^2$이라면 $\pi/1$은 $A_x$의 unit이라 아예 조건이 성립하지 않지만, 조건을 성립시키더라도 $x$의 거듭제곱이 섞인 원소는 $A_x$에서의 소성으로부터 $A$에서의 소성을 복원할 수 없다. 증명의 귀납 단계가 정확히 이 거듭제곱을 벗겨내는 과정이다.

다음 두 보조정리는 성격이 다르다. 최종 증명에서 우리는 어떤 ideal이 free module임을 보여야 하는데, 처음에 손에 들어오는 정보는 그 ideal이 stably free라는 것, 곧 free module을 direct sum하면 free가 된다는 것뿐이다. 일반적으로 stably free module은 free가 아닐 수 있지만, rank $1$에서는 exterior algebra를 통해 자유성을 복원할 수 있다.

::: 보조정리 10
Ring $A$와 $A$-module $P,Q$가 주어졌다 하고, $\bigwedge^2P=0$이라 하자. 그럼 각각의 $k\geq 1$에 대하여 다음의 $A$-module isomorphism

$$\bigwedge\nolimits^k(P\oplus Q)\cong\Big(\bigwedge\nolimits^kQ\Big)\oplus\Big(P\otimes_A\bigwedge\nolimits^{k-1}Q\Big)$$

이 존재한다.
:::
::: 증명
$M=P\oplus Q$로 적고, canonical inclusion과 projection들을 $\iota_P,\iota_Q,\pi_P,\pi_Q$로 적자. Exterior algebra는 [\[다중선형대수학\] §텐서대수, ⁋정의 10](/ko/math/multilinear_algebra/tensor_algebras#def10)의 quotient 구성에서 $\mathfrak{J}$가 degree $2$ 이상의 원소들로 생성되는 homogeneous ideal이므로 $\bigwedge^0(N)\cong A$, $\bigwedge^1(N)\cong N$을 만족하고, 특히 $\bigwedge^0Q=A$로 이해한다. 또 임의의 $A$-linear map $f:N \rightarrow N'$에 대하여 합성 $N \rightarrow N' \hookrightarrow \bigwedge(N')$은 각 원소의 wedge 제곱이 $0$이므로 [\[다중선형대수학\] §텐서대수, ⁋명제 11](/ko/math/multilinear_algebra/tensor_algebras#prop11)에 의하여 유일한 algebra homomorphism $\bigwedge(f):\bigwedge(N) \rightarrow \bigwedge(N')$을 유도하며, 이는 grading을 보존하고, 유일성에 의하여 $\bigwedge(g\circ f)=\bigwedge(g)\circ\bigwedge(f)$와 $\bigwedge(\id)=\id$가 성립한다. 그 degree $k$ 성분을 $\bigwedge^k(f)$로 적는다. 마지막으로 degree $1$의 두 원소 $u,v\in M\subseteq\bigwedge(M)$는 $(u+v)\wedge(u+v)=0$을 전개하여 $u\wedge v=-v\wedge u$를 만족하고, 따라서 같은 degree $1$ 원소가 두 번 등장하는 wedge는 두 원소를 부호를 감수하고 인접하게 재배열하면 $0$이 됨을 안다.

이제 $A$-linear map

$$\varphi:\Big(\bigwedge\nolimits^kQ\Big)\oplus\Big(P\otimes_A\bigwedge\nolimits^{k-1}Q\Big)\rightarrow \bigwedge\nolimits^k(M);\qquad (\beta,\ p\otimes\gamma)\mapsto \big(\bigwedge\nolimits^k\iota_Q\big)(\beta)+\iota_P(p)\wedge\big(\bigwedge\nolimits^{k-1}\iota_Q\big)(\gamma)$$

를 정의하자. 둘째 성분은 $(p,\gamma)\mapsto \iota_P(p)\wedge(\bigwedge^{k-1}\iota_Q)(\gamma)$가 $A$-bilinear이므로 tensor product의 universal property로부터 잘 정의된다. ([\[대수적 구조\] §가군의 직접곱과 직합, 텐서곱, ⁋정리 5](/ko/math/algebraic_structures/operations_of_modules#thm5))

$\varphi$가 surjective임을 보인다. $\bigwedge^k(M)$은 $z_1\wedge\cdots\wedge z_k$ ($z_i=(p_i,q_i)\in M$) 꼴의 원소들로 생성되고, $z_i=\iota_P(p_i)+\iota_Q(q_i)$를 대입하여 multilinear하게 전개하면 각 항은 $\iota_P(p_i)$들과 $\iota_Q(q_j)$들의 wedge이다. $P$-성분이 두 개 이상인 항은 재배열하면 $\iota_P(p_i)\wedge\iota_P(p_j)$ 꼴의 인수를 가지는데, 이는 functorial map $\bigwedge^2(\iota_P):\bigwedge^2P \rightarrow \bigwedge^2M$에 의한 $p_i\wedge p_j$의 image이고 $\bigwedge^2P=0$이므로 그러한 항은 모두 $0$이다. $P$-성분이 정확히 하나인 항은 재배열하면 $\pm\iota_P(p_i)\wedge(\bigwedge^{k-1}\iota_Q)(q_{j_1}\wedge\cdots\wedge q_{j_{k-1}})$의 꼴이 되어 $\varphi$의 image에 속하고, $P$-성분이 없는 항은 $(\bigwedge^k\iota_Q)(q_1\wedge\cdots\wedge q_k)$이므로 역시 image에 속한다.

$\varphi$가 injective임을 보이기 위해 왼쪽 역사상을 만든다. 첫째 성분은 $\bigwedge^k(\pi_Q):\bigwedge^kM \rightarrow \bigwedge^kQ$로 둔다. 둘째 성분을 위해 함수 $\theta_0: M^k \rightarrow P\otimes_A\bigwedge^{k-1}Q$를 다음의 식

$$\theta_0(z_1,\ldots, z_k)=\sum_{i=1}^k(-1)^{i-1}\pi_P(z_i)\otimes\big(\pi_Q(z_1)\wedge\cdots\wedge\widehat{\pi_Q(z_i)}\wedge\cdots\wedge\pi_Q(z_k)\big)$$

으로 정의하자. 여기서 hat은 해당 인수를 생략한다는 뜻이다. $\theta_0$이 각 변수에 대해 $A$-linear인 것은 자명하다. 이제 $z_i=z_j=z$ ($i<j$)로 두 인수가 같다고 하고 $p=\pi_P(z)$, $q=\pi_Q(z)$라 하자. $l\not\in\{i,j\}$인 항의 wedge에는 $\pi_Q(z_i)=q$와 $\pi_Q(z_j)=q$가 모두 남아 있으므로 그 항은 $0$이다. 남는 것은 $i$번째와 $j$번째 항인데, 두 항의 wedge는 같은 원소들을 담되 $q$ 하나가 각각 원래의 $j$번째 자리와 $i$번째 자리에 놓인 것이므로, $q$를 $j-i-1$개의 인수를 가로질러 옮기면 부호 $(-1)^{j-i-1}$만큼 차이난다. 따라서 두 항의 합은

$$\big((-1)^{i-1}(-1)^{j-i-1}+(-1)^{j-1}\big)p\otimes\big(\cdots\big)=\big((-1)^{j-2}+(-1)^{j-1}\big)p\otimes\big(\cdots\big)=0$$

이다. 곧 $\theta_0$은 두 인수가 같을 때마다 소멸하는 multilinear map이다. 따라서 $\theta_0$은 $\T^k(M)$에서의 linear map을 유도하고 ([\[대수적 구조\] §가군의 직접곱과 직합, 텐서곱, ⁋정리 5](/ko/math/algebraic_structures/operations_of_modules#thm5)), 인접한 두 인수가 같을 때 소멸하므로 이 linear map은 ideal $\mathfrak{J}$의 degree $k$ 성분을 $0$으로 보내어 quotient $\bigwedge^k(M)$에서의 linear map $\theta:\bigwedge^kM \rightarrow P\otimes_A\bigwedge^{k-1}Q$를 유도한다. 이는 [\[다중선형대수학\] §텐서대수, ⁋명제 12](/ko/math/multilinear_algebra/tensor_algebras#prop12)의 대응에서 alternating map에 linear map을 대응시키는 방향이며, 두 인수가 같으면 소멸한다는 조건만으로 유도되므로 별도의 표수 제한이 필요 없다.

이제 $\psi=(\bigwedge^k\pi_Q, \theta)$로 두고 $\psi\circ\varphi=\id$를 각 generator에서 확인한다. 우선 $\beta=q_1\wedge\cdots\wedge q_k$에 대하여 $\varphi(\beta,0)=\iota_Q(q_1)\wedge\cdots\wedge\iota_Q(q_k)$이고, $\pi_Q\circ\iota_Q=\id$와 functoriality로부터 $\bigwedge^k(\pi_Q)$는 이를 $\beta$로 보내며, $\theta$는 모든 항에 $\pi_P(\iota_Q(q_i))=0$이 등장하므로 이를 $0$으로 보낸다. 다음으로 $p\otimes\gamma$ ($\gamma=q_1\wedge\cdots\wedge q_{k-1}$)에 대하여 $\varphi(0,p\otimes\gamma)=\iota_P(p)\wedge\iota_Q(q_1)\wedge\cdots\wedge\iota_Q(q_{k-1})$인데, $\pi_Q(\iota_P(p))=0$이므로 $\bigwedge^k(\pi_Q)$는 이를 $0$으로 보내고, $\theta$의 전개에서 둘째 항부터는 $\pi_P(\iota_Q(q_i))=0$을 담아 소멸하므로 첫째 항만 남아

$$\theta\big(\varphi(0,p\otimes\gamma)\big)=\pi_P(\iota_P(p))\otimes\big(\pi_Q(\iota_Q(q_1))\wedge\cdots\wedge\pi_Q(\iota_Q(q_{k-1}))\big)=p\otimes\gamma$$

이다. 따라서 $\psi\circ\varphi=\id$이고, $\varphi$는 injective이면서 surjective이므로 isomorphism이다.
:::

가령 $Q$가 free module이라면 [\[다중선형대수학\] §텐서대수, ⁋명제 13](/ko/math/multilinear_algebra/tensor_algebras#prop13)이 $\bigwedge^kQ$의 basis를 원소 개수 $k$짜리 부분집합들로 색인하므로, 위의 분해는 $\bigwedge^2P=0$인 $P$를 하나 섞은 direct sum의 exterior power를 완전히 계산해준다. 바로 이 형태로 아래에서 사용된다.

다음으로 stably free성을 뽑아낼 보조정리들을 준비한다. 먼저 [§분수아이디얼, ⁋정의 1](/ko/math/commutative_algebra/fractional_ideals#def1)의 invertible module이 projective라는 것을 확인한다. [§분수아이디얼, ⁋정리 3](/ko/math/commutative_algebra/fractional_ideals#thm3)은 invertible module의 trace map이 isomorphism이라는 것까지 주었으므로, 남은 것은 표준적인 dual basis 논증이다.

::: 보조정리 11
Noetherian ring $A$의 invertible $A$-module $M$은 finitely generated projective module이다.
:::
::: 증명
$M$은 정의에 의하여 finitely generated이다. [§분수아이디얼, ⁋정리 3](/ko/math/commutative_algebra/fractional_ideals#thm3)의 첫째 결과에 의하여 trace map $M^\ast\otimes_AM \rightarrow A$는 isomorphism이고, 특히 surjective이므로 $\sum_{i=1}^r\xi_i(s_i)=1$이 성립하도록 하는 $\xi_1,\ldots,\xi_r\in M^\ast=\Hom_A(M,A)$와 $s_1,\ldots,s_r\in M$이 존재한다.

$A$-linear map들을 $\varphi:M \rightarrow A^{\oplus r}$, $m\mapsto(\xi_1(m),\ldots,\xi_r(m))$과 $\psi:A^{\oplus r} \rightarrow M$, $e_i\mapsto s_i$로 정의하고 $\psi\circ\varphi=\id_M$임을 보인다. 임의의 maximal ideal $\mathfrak{m}$을 고정하면 invertible의 정의에 의하여 $M_\mathfrak{m}\cong A_\mathfrak{m}$은 한 원소 $t$로 생성되는 free module이다. 등식 $\sum\xi_i(s_i)=1$을 localize하면 $\sum(\xi_i)_\mathfrak{m}\big((s_i)_\mathfrak{m}\big)=1$이고, $(s_i)_\mathfrak{m}=c_it$로 적으면 임의의 $m=ut\in M_\mathfrak{m}$에 대하여

$$(\psi\circ\varphi)_\mathfrak{m}(m)=\sum_{i=1}^r(\xi_i)_\mathfrak{m}(ut)\cdot(s_i)_\mathfrak{m}=u\sum_{i=1}^rc_i(\xi_i)_\mathfrak{m}(t)\cdot t=u\sum_{i=1}^r(\xi_i)_\mathfrak{m}(c_it)\cdot t=u\cdot 1\cdot t=m$$

이다. 곧 $(\psi\circ\varphi)_\mathfrak{m}=\id$이므로, 임의의 $m\in M$에 대하여 원소 $\psi(\varphi(m))-m$은 모든 maximal ideal에서의 localization이 $0$이고, [§국소화의 성질들, ⁋보조정리 3](/ko/math/commutative_algebra/properties_of_localization#lem3)에 의하여 $\psi(\varphi(m))=m$이다.

따라서 $\varphi$는 injective이고 $A^{\oplus r}=\varphi(M)\oplus\ker\psi$이다. 실제로 임의의 $v\in A^{\oplus r}$에 대하여 $v=\varphi(\psi(v))+(v-\varphi(\psi(v)))$인데 $\psi(v-\varphi(\psi(v)))=\psi(v)-\psi(v)=0$이고, $\varphi(m)\in\ker\psi$라면 $m=\psi(\varphi(m))=0$이기 때문이다. 곧 $M\cong\varphi(M)$은 free module의 direct summand이고, [\[다중선형대수학\] §사영가군, 단사가군, 평탄가군, ⁋명제 4](/ko/math/multilinear_algebra/various_modules#prop4)에 의하여 projective이다.
:::

이 증명은 trace map의 surjectivity만 사용하며, 위에서 정의한 $\xi_i$들과 $s_i$들이 표준적인 dual basis의 역할을 한다. 이제 유한한 free resolution으로부터 stably free성을 뽑아내는 마지막 준비를 마친다.

::: 보조정리 12
Ring $A$와 finitely generated projective $A$-module $Q$가 finitely generated free module들로 이루어진 유한한 길이의 free resolution

$$0 \rightarrow F_n \rightarrow \cdots \rightarrow F_1 \rightarrow F_0 \rightarrow Q \rightarrow 0$$

을 갖는다 하자. 그럼 적당한 finitely generated free module $F,F'$에 대하여 $Q\oplus F\cong F'$이다.
:::
::: 증명
$n$에 대한 귀납법을 쓴다. $n=0$이면 $Q\cong F_0$이므로 $F=0$으로 두면 된다.

$n\geq 1$이라 하고 $K=\ker(F_0 \rightarrow Q)$로 두자. $Q$가 projective이므로 $\Hom_A(Q,-)$는 right exact이고 ([\[다중선형대수학\] §사영가군, 단사가군, 평탄가군, ⁋정의 3](/ko/math/multilinear_algebra/various_modules#def3)), surjection $F_0 \rightarrow Q$에 적용하면 $\Hom_A(Q,F_0) \rightarrow \Hom_A(Q,Q)$가 surjective이므로 $\id_Q$의 preimage $s:Q \rightarrow F_0$이 존재한다. 그럼 short exact sequence $0 \rightarrow K \rightarrow F_0 \rightarrow Q \rightarrow 0$이 split하여 $F_0\cong K\oplus Q$이다. 따라서 $K$는 finitely generated free module의 direct summand이므로 finitely generated projective이고 ([\[다중선형대수학\] §사영가군, 단사가군, 평탄가군, ⁋명제 4](/ko/math/multilinear_algebra/various_modules#prop4)), 주어진 resolution의 exactness로부터 $K=\operatorname{im}(F_1 \rightarrow F_0)$이므로

$$0 \rightarrow F_n \rightarrow \cdots \rightarrow F_1 \rightarrow K \rightarrow 0$$

은 길이 $n-1$의 free resolution이다. 귀납 가정에 의하여 $K\oplus A^{\oplus a}\cong A^{\oplus b}$이도록 하는 $a,b\geq 0$이 존재하고, 그럼

$$Q\oplus A^{\oplus b}\cong Q\oplus K\oplus A^{\oplus a}\cong F_0\oplus A^{\oplus a}$$

는 finitely generated free module이다.
:::

이 보조정리의 결론을 만족하는 module을 *stably free*라 부른다. 일반적으로 stably free module이 free일 이유는 없으나, 아래 정리의 증명에서 보듯 rank $1$의 경우에는 [보조정리 10](#lem10)이 free성을 강제한다. 이제 모든 준비가 끝났다.

::: 정리 13 (Auslander--Buchsbaum)
Regular local ring은 UFD이다.
:::
::: 증명
$d$차원 regular local ring $(A,\mathfrak{m},\kappa)$에 대하여, $d$에 대한 귀납법으로 증명한다.

$d=0$인 경우 $\mathfrak{m}$은 $0$개의 원소로 생성되므로 ([§차원, ⁋정의 12](/ko/math/commutative_algebra/Krull_dimension#def12)) $\mathfrak{m}=0$이고 $A$는 field이다. Field는 $0$이 아닌 non-unit을 갖지 않으므로 UFD의 두 조건이 공허하게 성립한다. ([\[환론\] §정역, ⁋정의 16](/ko/math/ring_theory/integral_domains#def16))

이제 $d\geq 1$이라 하고, 차원이 $d$ 미만인 모든 regular local ring이 UFD라 가정하자. [§정칙국소환, ⁋따름정리 1](/ko/math/commutative_algebra/regular_local_rings#cor1)에 의하여 $A$는 integral domain이므로 [보조정리 7](#lem7)을 적용할 수 있고, $0$이 아닌 임의의 prime ideal $\mathfrak{p}_0$는 [보조정리 8](#lem8)의 둘째 결과에 의하여 codimension $1$인 prime ideal $\mathfrak{p}\subseteq\mathfrak{p}_0$를 포함하므로, codimension $1$인 임의의 prime ideal $\mathfrak{p}$가 prime element를 포함한다는 것만 보이면 충분하다.

$d\geq 1$이므로 $\mathfrak{m}\neq 0$이고, [§정수적 확장, ⁋보조정리 8](/ko/math/commutative_algebra/integral_extension#lem8)에 의하여 $\mathfrak{m}\neq\mathfrak{m}^2$이므로 $x\in\mathfrak{m}\setminus\mathfrak{m}^2$을 택할 수 있다. $A$가 domain이고 $x\neq 0$이므로 $x$는 $A$-regular이다. 우선 $x$가 prime element임을 확인한다. $A$가 regular이므로 embedding dimension은 $\dim_\kappa(\mathfrak{m}/\mathfrak{m}^2)=d$이고 ([§차원, ⁋정의 12](/ko/math/commutative_algebra/Krull_dimension#def12)의 generating set과 [§매개계, ⁋명제 2](/ko/math/commutative_algebra/system_of_parameters#prop2)), [정리 3](#thm3)의 증명에서와 동일한 계산으로 $\overline{A}=A/xA$는 embedding dimension이 $d-1$인 Noetherian local ring이며 [§Depth, ⁋명제 9](/ko/math/commutative_algebra/depth#prop9)에 의하여 $\dim\overline{A}=d-1$이다. 따라서 $\overline{A}$의 maximal ideal은 $\dim\overline{A}$개의 원소로 생성되어 $\overline{A}$는 regular local ring이고, [§정칙국소환, ⁋따름정리 1](/ko/math/commutative_algebra/regular_local_rings#cor1)에 의하여 integral domain이다. 곧 $xA$는 $0$이 아닌 prime ideal이고 $x$는 non-unit이므로 $x$는 prime element이다.

Codimension $1$인 prime ideal $\mathfrak{p}$를 고정하고 두 경우로 나눈다.

먼저 $x\in\mathfrak{p}$인 경우, $(x)\subseteq\mathfrak{p}$는 둘 다 $0$이 아닌 prime ideal이고 $\codim\mathfrak{p}=1$이므로 [보조정리 8](#lem8)의 첫째 결과의 증명에서와 같이 $(x)\subsetneq\mathfrak{p}$라면 chain $\mathfrak{p}\supsetneq(x)\supsetneq(0)$이 모순을 주어 $\mathfrak{p}=(x)$이다. 곧 $\mathfrak{p}$는 prime element $x$를 포함한다.

이제 $x\not\in\mathfrak{p}$인 경우를 다룬다. [보조정리 9](#lem9)에서와 같이 multiplicative subset $S=\{x^k\mid k\geq 0\}$에 대한 localization $A_x$를 생각하자. $A$가 domain이므로 $A_x$도 domain이고, $A$가 Noetherian이므로 $A_x$도 Noetherian이다. ([§국소화, ⁋따름정리 9](/ko/math/commutative_algebra/localization#cor9)) $\mathfrak{p}$는 prime이고 $x\not\in\mathfrak{p}$이므로 $S$와 만나지 않고, 따라서 [§국소화, ⁋명제 8](/ko/math/commutative_algebra/localization#prop8)에 의하여 $\mathfrak{p}A_x$는 $A_x$의 prime ideal이며 그 contraction은 $\mathfrak{p}$이다. 또 $\mathfrak{p}\neq 0$이고 $A \rightarrow A_x$가 injective이므로 $\mathfrak{p}A_x\neq 0$이고, 같은 명제에 의하여 $\mathfrak{p}A_x$는 proper ideal이다. 우리의 계획은 $A_x$-module $\mathfrak{p}A_x$가 $A_x$와 isomorphic함을 보이는 것이다.

첫째로 $\mathfrak{p}A_x$가 invertible $A_x$-module임을 보인다. $\mathfrak{p}$는 finitely generated이므로 ([§기본 개념들, ⁋정리 3](/ko/math/commutative_algebra/basic_notions#thm3)) $\mathfrak{p}A_x$는 그 generator들의 image로 생성되는 finitely generated $A_x$-module이다. [§국소화, ⁋명제 8](/ko/math/commutative_algebra/localization#prop8)에 의하여 $A_x$의 임의의 prime ideal은 $x\not\in\mathfrak{q}$인 $A$의 prime ideal $\mathfrak{q}$에 대하여 $\mathfrak{q}A_x$의 꼴이고, [정의 5](#def5) 직후에 살펴본 localization의 합성에 의하여 $(A_x)_{\mathfrak{q}A_x}\cong A_\mathfrak{q}$이며, 이 identification 아래에서 $(\mathfrak{p}A_x)_{\mathfrak{q}A_x}$는 양변 모두 $\mathfrak{p}$의 image로 생성되는 ideal이므로 $\mathfrak{p}A_\mathfrak{q}$와 대응된다. $x\in\mathfrak{m}\setminus\mathfrak{q}$이므로 $\mathfrak{q}\subsetneq\mathfrak{m}$이고, $\mathfrak{q}$에서 시작하는 임의의 prime chain 위에 $\mathfrak{m}$을 얹으면 $\codim\mathfrak{q}\leq d-1$을 얻으므로 [따름정리 4](#cor4)에 의하여 $A_\mathfrak{q}$는 차원이 $d-1$ 이하인 regular local ring이고, 귀납 가정에 의하여 UFD이다. 만일 $\mathfrak{p}\not\subseteq\mathfrak{q}$라면 $\mathfrak{p}\setminus\mathfrak{q}$의 원소가 $A_\mathfrak{q}$에서 unit이 되어 $\mathfrak{p}A_\mathfrak{q}=A_\mathfrak{q}$이다. 만일 $\mathfrak{p}\subseteq\mathfrak{q}$라면 [§국소화, ⁋명제 8](/ko/math/commutative_algebra/localization#prop8)의 inclusion-preserving bijection에 의하여 $\mathfrak{p}A_\mathfrak{q}$는 $A_\mathfrak{q}$의 $0$이 아닌 prime ideal이고, $\mathfrak{p}$에 포함되는 prime들과 $\mathfrak{p}A_\mathfrak{q}$에 포함되는 prime들이 대응되므로 codimension이 $1$로 유지되어, [보조정리 8](#lem8)의 첫째 결과에 의하여 $\mathfrak{p}A_\mathfrak{q}=tA_\mathfrak{q}$는 $0$이 아닌 principal ideal이다. 그럼 $A_\mathfrak{q}$가 domain이므로 $c\mapsto tc$는 $A_\mathfrak{q}$에서 $\mathfrak{p}A_\mathfrak{q}$로의 isomorphism이다. 어느 경우든 $(\mathfrak{p}A_x)_{\mathfrak{q}A_x}\cong(A_x)_{\mathfrak{q}A_x}$이므로, $\mathfrak{p}A_x$는 invertible $A_x$-module이다. ([§분수아이디얼, ⁋정의 1](/ko/math/commutative_algebra/fractional_ideals#def1)) 특히 [보조정리 11](#lem11)에 의하여 finitely generated projective $A_x$-module이다.

둘째로 $\mathfrak{p}A_x$가 유한한 길이의 free resolution을 가짐을 본다. $\pd_A\mathfrak{p}\leq\operatorname{gldim}A=d<\infty$이므로 ([§호몰로지 차원, ⁋명제 13](/ko/math/commutative_algebra/homological_dimension#prop13)) [§호몰로지 차원, ⁋명제 9](/ko/math/commutative_algebra/homological_dimension#prop9)와 [§호몰로지 차원, ⁋명제 11](/ko/math/commutative_algebra/homological_dimension#prop11)에 의하여 $\mathfrak{p}$는 finitely generated free $A$-module들로 이루어진 유한한 길이의 free resolution $0 \rightarrow F_t \rightarrow \cdots \rightarrow F_0 \rightarrow \mathfrak{p} \rightarrow 0$을 갖는다. 여기에 localization을 취하면 [§국소화의 성질들, ⁋명제 2](/ko/math/commutative_algebra/properties_of_localization#prop2)에 의하여 exactness가 보존되고, 각 $(F_i)_x$는 finitely generated free $A_x$-module이며, inclusion $\mathfrak{p}\hookrightarrow A$의 localization의 image가 정확히 $\mathfrak{p}A_x$이므로 $\mathfrak{p}_x\cong\mathfrak{p}A_x$이다. 곧 $\mathfrak{p}A_x$는 유한한 길이의 free resolution을 갖고, [보조정리 12](#lem12)에 의하여 적당한 $a,b\geq 0$에 대해

$$\mathfrak{p}A_x\oplus A_x^{\oplus a}\cong A_x^{\oplus b}$$

이다. $A_x$의 quotient field를 $F$라 하고 양변에 $F$를 tensor하면, [§국소화의 성질들, ⁋보조정리 1](/ko/math/commutative_algebra/properties_of_localization#lem1)에 의하여 $F\otimes_{A_x}\mathfrak{p}A_x$는 inclusion $\mathfrak{p}A_x\hookrightarrow A_x$를 localize하여 얻어지는 injective map을 통해 ([§국소화의 성질들, ⁋명제 2](/ko/math/commutative_algebra/properties_of_localization#prop2)) $F$의 $0$이 아닌 ideal과 identify되고, field의 $0$이 아닌 ideal은 전체뿐이므로 $F\otimes_{A_x}\mathfrak{p}A_x\cong F$이다. 따라서 $F$-벡터공간의 차원을 비교하면 $1+a=b$이다.

셋째로 $\bigwedge^2(\mathfrak{p}A_x)=0$임을 본다. $A_x$의 임의의 maximal ideal $\mathfrak{q}A_x$에 대하여 $B=(A_x)_{\mathfrak{q}A_x}$로 두면, [\[다중선형대수학\] §텐서대수, ⁋명제 14](/ko/math/multilinear_algebra/tensor_algebras#prop14)의 base change를 degree별로 읽고 [§국소화의 성질들, ⁋보조정리 1](/ko/math/commutative_algebra/properties_of_localization#lem1)을 적용하면

$$\Big(\bigwedge\nolimits^2(\mathfrak{p}A_x)\Big)_{\mathfrak{q}A_x}\cong \bigwedge\nolimits^2_B\big((\mathfrak{p}A_x)_{\mathfrak{q}A_x}\big)\cong\bigwedge\nolimits^2_B(B)=0$$

이다. 가운데 isomorphism에서는 앞서 첫째 단계에서 확인한 $(\mathfrak{p}A_x)_{\mathfrak{q}A_x}\cong B$를 사용하였고, 마지막 등식은 rank $1$의 free module의 $2$차 exterior power가 [\[다중선형대수학\] §텐서대수, ⁋명제 13](/ko/math/multilinear_algebra/tensor_algebras#prop13)에 의하여 $0$이기 때문이다. 모든 maximal ideal에서의 localization이 $0$이므로 [§국소화의 성질들, ⁋보조정리 3](/ko/math/commutative_algebra/properties_of_localization#lem3)에 의하여 $\bigwedge^2(\mathfrak{p}A_x)=0$이다.

이제 [보조정리 10](#lem10)을 $P=\mathfrak{p}A_x$, $Q=A_x^{\oplus a}$, $k=a+1$에 적용하면

$$A_x\cong\bigwedge\nolimits^{a+1}\big(A_x^{\oplus(a+1)}\big)\cong\bigwedge\nolimits^{a+1}\big(\mathfrak{p}A_x\oplus A_x^{\oplus a}\big)\cong\bigwedge\nolimits^{a+1}\big(A_x^{\oplus a}\big)\oplus\Big(\mathfrak{p}A_x\otimes_{A_x}\bigwedge\nolimits^a\big(A_x^{\oplus a}\big)\Big)\cong 0\oplus\big(\mathfrak{p}A_x\otimes_{A_x}A_x\big)\cong\mathfrak{p}A_x$$

이다. 처음과 마지막의 계산 $\bigwedge^{a+1}(A_x^{\oplus(a+1)})\cong A_x$, $\bigwedge^{a+1}(A_x^{\oplus a})=0$, $\bigwedge^a(A_x^{\oplus a})\cong A_x$는 모두 [\[다중선형대수학\] §텐서대수, ⁋명제 13](/ko/math/multilinear_algebra/tensor_algebras#prop13)의 basis 묘사에 의한 것이다. Isomorphism $A_x \rightarrow \mathfrak{p}A_x$에 의한 $1$의 image를 $t$라 하면 $\mathfrak{p}A_x=tA_x$는 principal ideal이다.

마지막으로 prime element를 $A$로 가져온다. $\mathfrak{p}A_x$의 원소는 공통분모를 잡으면 $p/x^k$ ($p\in\mathfrak{p}$)의 꼴이므로 $t=p/x^k$로 적을 수 있고, $x$가 unit이므로 $\mathfrak{p}A_x=(p/1)A_x$이다. $p\neq 0$이고, [§부풀림 대수, ⁋따름정리 8](/ko/math/commutative_algebra/blowup_algebra#cor8)에 의하여 $\bigcap_{l\geq 1}(x)^l=0$이므로 $x^l\mid p$이도록 하는 $l$은 유한히 많고, 가장 큰 $l$을 택해 $p=x^l\pi$로 적으면 $x\nmid\pi$이다. 다시 $x$가 $A_x$에서 unit이므로

$$\mathfrak{p}A_x=(p/1)A_x=(\pi/1)A_x$$

이다. 그럼 $(\pi/1)A_x=\mathfrak{p}A_x$는 $0$이 아닌 proper prime ideal이므로 $\pi/1$은 $A_x$의 prime element이고, $x\nmid\pi$이므로 [보조정리 9](#lem9)에 의하여 $\pi$는 $A$의 prime element이다. 한편 $\pi/1\in\mathfrak{p}A_x$이므로 적당한 $k$에 대하여 $x^k\pi\in\mathfrak{p}$이고 ([§국소화, ⁋명제 8](/ko/math/commutative_algebra/localization#prop8)), $x\not\in\mathfrak{p}$이므로 $\pi\in\mathfrak{p}$이다. 곧 $\mathfrak{p}$는 prime element $\pi$를 포함한다.

두 경우 모두에서 codimension $1$인 prime ideal이 prime element를 포함하므로, [보조정리 7](#lem7)에 의하여 $A$는 UFD이다.
:::

증명의 뼈대를 되짚어보면, $x\in\mathfrak{m}\setminus\mathfrak{m}^2$이 prime element라는 사실은 $A$가 regular라는 것에서 나오고, $x$를 invert한 ring $A_x$는 국소적으로 더 작은 차원의 regular local ring들로 이루어져 귀납이 작동하며, $\mathfrak{p}A_x$의 유한 free resolution은 locally principal ideal을 진짜 principal ideal로 승격시키는 지점에서 개입한다. 유한한 free resolution 없이는 invertible module이 free일 이유가 전혀 없다는 점에서, 이 정리는 [정리 3](#thm3)과 마찬가지로 free resolution의 언어가 실질적인 계산력을 갖는다는 것을 보여준다.

기하적으로 Auslander--Buchsbaum 정리는 smooth point의 local ring에서는 언제나 유일한 소인수분해가 가능하다는 선언이다. Algebraic variety의 smooth point에서의 local ring은 regular local ring이므로, 그 점 근방의 함수는 unit과 순서를 무시하면 유일한 방식으로 기약 인수들의 곱으로 분해되고, 특히 codimension $1$의 부분다양체는 국소적으로 방정식 하나로 잘려 나온다. ([보조정리 8](#lem8)의 첫째 결과) 이것이 smooth variety 위에서 divisor 이론이 특히 투명해지는 대수적 이유이다. 지금까지 우리는 free resolution의 길이라는 정보만으로 어떤 ring이 regular인지를 판정하고 나아가 UFD라는 것까지 끌어냈는데, free resolution이 담고 있는 정보는 길이에 그치지 않으며, 이후의 글에서는 Fitting ideal과 determinantal 방법 등 free resolution의 행렬 표현을 더 정밀하게 읽어내는 도구들을 다룬다.

---

**참고문헌**

**[Eis]** David Eisenbud. *Commutative Algebra: with a view toward algebraic geometry*. Springer, 1995.

**[Mat]** Hideyuki Matsumura. *Commutative Ring Theory*. Cambridge University Press, 1986.

**[Stacks]** The Stacks Project Authors. *The Stacks Project*. [https://stacks.math.columbia.edu](https://stacks.math.columbia.edu).

---
