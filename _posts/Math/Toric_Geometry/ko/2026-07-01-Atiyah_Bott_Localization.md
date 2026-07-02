---
title: "Atiyah–Bott 국소화 정리"
description: "Torus가 작용하는 콤팩트 다양체의 동변 코호몰로지가 고정점 자리의 것으로 국소화됨을 보이고, 동변 적분을 고정점에서의 기여의 합으로 주는 Atiyah–Bott–Berline–Vergne 공식을 다룬다."
excerpt: "The localization theorem and the ABBV integration formula via torus fixed points"

categories: [Math / Toric Geometry]
permalink: /ko/math/toric_geometry/atiyah_bott_localization
sidebar: 
    nav: "toric_geometry-ko"

date: 2026-07-01
last_modified_at: 2026-07-01
weight: 11

published: false

---

앞 글에서 torus $$T=(S^1)^n$$이 작용하는 공간의 equivariant cohomology $$H_T^\bullet(X)$$이 항상 $$H_T^\bullet(\mathrm{pt})=\mathbb{Q}[t_1,\ldots,t_n]$$ 위의 algebra이며, fixed point로의 restriction이 그 구조를 거의 결정한다는 현상을 보았다. ([§동변 코호몰로지, ⁋예시 6](/ko/math/toric_geometry/equivariant_cohomology#ex6)) 이 글의 목표는 그 "거의"를 정확한 정리로 바꾸는 것이다. 곧 $$H_T^\bullet(\mathrm{pt})$$의 $$0$$이 아닌 원소들을 모두 가역으로 만들면 (다항식환의 분수체로 넘어가면) $$H_T^\bullet(X)$$이 fixed locus $$X^T$$의 equivariant cohomology와 동형이 됨을 보인다. 이것이 Atiyah–Bott와 Berline–Vergne의 *localization theorem*이며, 그 즉각적 귀결로 콤팩트 다양체 위의 equivariant 적분이 fixed point 각각에서의 국소적 기여의 유한합으로 계산된다는 Atiyah–Bott–Berline–Vergne 공식을 얻는다.

이 글 전체에서 $$T=(S^1)^n$$은 $$n$$차원 torus, $$M$$은 $$T$$가 매끄럽게 작용하는 콤팩트 oriented 매끄러운 다양체이며, 계수는 $$\mathbb{Q}$$로 둔다. 그럼 $$T$$가 connected이므로 작용은 방향을 보존하고, base ring을

$$R:=H_T^\bullet(\mathrm{pt};\mathbb{Q})=\mathbb{Q}[t_1,\ldots,t_n],\qquad \lvert t_i\rvert=2$$

로 적는다. 이는 character lattice $$M_T=\mathrm{Hom}(T,S^1)$$의 symmetric algebra $$\mathrm{Sym}_{\mathbb{Q}}(M_T\otimes\mathbb{Q})$$이고, 각 character $$\chi\in M_T$$은 degree $$2$$ 원소로서 $$R$$ 안에 놓인다. ([§동변 코호몰로지, ⁋명제 4](/ko/math/toric_geometry/equivariant_cohomology#prop4)) $$R$$은 정역이므로 그 분수체 $$\mathrm{Frac}(R)=\mathbb{Q}(t_1,\ldots,t_n)$$가 존재한다. 임의의 $$R$$-가군 $$N$$에 대하여 그 *국소화*를

$$N_{\mathrm{loc}}:=N\otimes_R\mathrm{Frac}(R)$$

로 적기로 한다. $$\mathrm{Frac}(R)$$이 $$R$$ 위에서 flat이므로 $$N\mapsto N_{\mathrm{loc}}$$은 완전함수이고, $$N$$이 torsion $$R$$-가군 (모든 원소가 $$0$$이 아닌 $$R$$의 원소에 의해 소멸되는 가군) 이면 $$N_{\mathrm{loc}}=0$$이다.

## 고정점 성분과 그 normal bundle

국소화 정리의 무대는 fixed locus $$M^T=\{x\in M\mid g\cdot x=x\text{ for all }g\in T\}$$이다. Torus 작용의 fixed locus는 다양체로서 잘 행동하며, 각 성분 주위에서 작용이 normal 방향으로 어떻게 보이는지가 정리의 핵심 데이터가 된다.

<div class="proposition" markdown="1">

<ins id="prop1">**명제 1**</ins> $$T$$가 콤팩트 다양체 $$M$$ 위에 매끄럽게 작용할 때, fixed locus $$M^T$$은 닫힌 매끄러운 부분다양체이며 유한히 많은 connected 성분 $$F$$의 disjoint union이다. 각 성분 $$F$$는 $$T$$-불변이고 그 위에서 $$T$$가 자명하게 작용한다. 더 나아가 $$F$$의 normal bundle $$N_F=TM\vert_F/TF$$은 fiber마다 $$T$$-작용을 가지며, 이 작용의 weight들은 모두 $$0$$이 아니다.

</div>
<details class="proof" markdown="1">
<summary>증명</summary>

$$T$$는 콤팩트이므로 $$M$$ 위에 $$T$$-불변 Riemann metric을 평균화로 만들 수 있고, 그에 대한 exponential map은 $$T$$-동변이다. 한 fixed point $$x\in M^T$$에서 $$T$$는 tangent space $$T_xM$$ 위에 선형으로 (isotropy 표현으로) 작용하며, 이 선형표현의 weight $$0$$ 고유공간을 $$(T_xM)^T$$라 하면 $$T$$-동변 exponential map이 $$(T_xM)^T$$의 작은 근방을 $$M^T$$ 위로 보내는 chart를 준다. 따라서 $$M^T$$은 각 점 근방에서 $$(T_xM)^T$$로 모형화되는 매끄러운 부분다양체이고, $$M$$이 콤팩트이므로 성분의 수는 유한하다. 정의상 $$M^T$$의 모든 점이 고정되므로 각 성분 위에서 작용은 자명하다.

성분 $$F$$에서 $$T_xM=T_xF\oplus(N_F)_x$$로 분해할 때, $$T_xF=(T_xM)^T$$는 정확히 weight $$0$$ 부분이므로 그 보충 $$(N_F)_x$$ 위의 isotropy 표현에는 weight $$0$$이 나타나지 않는다. 만일 normal 방향에 weight $$0$$ 성분이 있었다면 그 방향이 fixed locus를 키워 $$F$$의 차원과 모순이다. 동변 tubular neighborhood 정리에 의해 $$F$$의 근방은 $$N_F$$의 disk bundle과 $$T$$-동변 미분동형이고, 그 위에서 $$T$$가 fiber에 선형으로 작용한다. 자세한 slice 정리와 동변 tubular neighborhood의 구성은 [BGV]의 §7을 따른다.

</details>

곧 fixed locus는 차원이 제각각일 수 있는 부분다양체들의 모임이며, 각 성분 $$F$$ 위에서는 $$T$$가 아무 일도 하지 않는 대신 그 normal 방향에 모든 비자명한 작용이 응축되어 있다. Isolated fixed point, 곧 $$F=\{p\}$$가 한 점인 경우에는 $$N_F=T_pM$$이 곧 tangent space 전체이고, 그 위의 isotropy 표현의 weight $$w_1(p),\ldots,w_m(p)\in M_T$$ (여기서 $$m=\dim_{\mathbb{C}}M$$, 단 $$M$$이 거의 복소다양체일 때) 들이 작용의 모든 국소 정보를 담는다. ([\[리 이론\] §원환면의 작용, ⁋정의 4](/ko/math/lie_theory/torus_action#def4)) 앞으로 이 weight들이 $$R$$의 일차식으로 분모에 등장한다.

## 동변 Euler class

명제 1의 normal bundle $$N_F$$은 $$T$$-동변 vector bundle이다. 우리는 그 *동변 Euler class*를 만들어, 국소화 정리에서 $$F$$로의 기여를 이 class로 나누는 형태로 기술할 것이다. 정의는 Borel 구성을 통해 보통의 Euler class를 동변 판본으로 들어올리는 것이다. 앞으로 다룰 normal bundle은 모두 복소 bundle이므로 (예시의 $$\mathbb{P}^n$$, Grassmannian, 매끄러운 toric variety는 모두 복소다양체이다), 우리는 복소 $$T$$-동변 bundle에 한정해 정의한다.

<div class="definition" markdown="1">

<ins id="def2">**정의 2**</ins> $$T$$-공간 $$Y$$ 위의 복소 $$T$$-동변 vector bundle $$E\rightarrow Y$$에 대하여, Borel 구성 $$E_T=ET\times_T E\rightarrow Y_T=ET\times_T Y$$은 $$Y_T$$ 위의 보통의 복소 vector bundle이다. ([§동변 코호몰로지, ⁋정의 1](/ko/math/toric_geometry/equivariant_cohomology#def1)) 그 보통의 Chern class와 top Chern class (= Euler class) 를 통해 $$E$$의 *equivariant Chern class<sub>동변 천 특성류</sub>*와 *equivariant Euler class<sub>동변 오일러 특성류</sub>*를

$$c_i^T(E):=c_i(E_T)\in H_T^{2i}(Y),\qquad e_T(E):=c_{\mathrm{rank}}^T(E)=e\big((E_T)_{\mathbb{R}}\big)\in H_T^{2\mathrm{rank}(E)}(Y)$$

로 정의한다. 여기서 우변의 보통 Chern class와 Euler class는 각각 [\[대수적 위상수학\] §벡터다발의 특성류, ⁋정의 6](/ko/math/algebraic_topology/characteristic_classes#def6)과 [\[대수적 위상수학\] §벡터다발의 특성류, ⁋정의 3](/ko/math/algebraic_topology/characteristic_classes#def3)의 것이다.

</div>

보통의 특성류가 만족하던 naturality와 Whitney 합 공식은 Borel 구성이 함자적이므로 그대로 동변 판본으로 이어진다. ([\[대수적 위상수학\] §벡터다발의 특성류, ⁋정리 8](/ko/math/algebraic_topology/characteristic_classes#thm8)) 특히 $$T$$-동변 bundle의 직합에 대해 $$e_T(E\oplus E')=e_T(E)e_T(E')$$이다.

이 정의가 명제 1의 fixed component $$F$$ 위에서 어떻게 구체화되는지를 살피자. $$F$$ 위에서 $$T$$가 자명하게 작용하므로 $$F_T=ET\times_T F=BT\times F$$이고, 따라서

$$H_T^\bullet(F)=H^\bullet(BT\times F)=R\otimes_{\mathbb{Q}}H^\bullet(F;\mathbb{Q})$$

이다 (Künneth). 자명한 작용을 갖는 $$T$$-동변 복소 bundle $$N_F$$은 weight에 따라 고유 subbundle들로 분해된다. 곧 $$N_F=\bigoplus_{\chi}(N_F)_\chi$$이고 여기서 $$T$$는 $$(N_F)_\chi$$ 위에 character $$\chi\in M_T$$로 작용한다. 명제 1에 의해 나타나는 $$\chi$$는 모두 $$0$$이 아니다. 한 weight bundle $$(N_F)_\chi$$의 Borel 구성은 $$BT\times F$$ 위에서 $$L_\chi\boxtimes(N_F)_\chi$$ 꼴로 풀려, 그 보통의 Chern root가 $$x_{\chi,j}+\chi$$ ($$x_{\chi,j}$$는 $$(N_F)_\chi$$의 $$H^\bullet(F)$$ 안에서의 Chern root, $$\chi\in R$$) 가 된다. 따라서

$$e_T(N_F)=\prod_{\chi}\prod_{j}\big(x_{\chi,j}+\chi\big)\in R\otimes_{\mathbb{Q}}H^\bullet(F)$$

이다. Isolated fixed point $$F=\{p\}$$에서는 $$H^\bullet(F)=\mathbb{Q}$$라 모든 $$x_{\chi,j}=0$$이고, weight를 $$w_1,\ldots,w_m$$으로 다시 적으면

$$e_T(N_p)=\prod_{j=1}^m w_j\in R$$

이라는 가장 단순한 형태가 된다. 곧 isolated fixed point에서 동변 Euler class는 isotropy weight들의 곱이다.

다음 명제가 국소화에서 결정적이다. $$e_T(N_F)$$은 $$F$$ 위에서 일반적으로 $$0$$이 아닌 nilpotent 보정항을 갖지만, 국소화하면 가역이 된다.

<div class="proposition" markdown="1">

<ins id="prop3">**명제 3**</ins> 명제 1의 fixed component $$F$$에 대하여, $$e_T(N_F)$$은 국소화된 환 $$H_T^\bullet(F)_{\mathrm{loc}}=H^\bullet(F)\otimes_{\mathbb{Q}}\mathrm{Frac}(R)$$ 안에서 가역이다.

</div>
<details class="proof" markdown="1">
<summary>증명</summary>

위 분해식에서 $$e_T(N_F)=\prod_\chi\prod_j(x_{\chi,j}+\chi)$$이다. $$x_{\chi,j}\in H^{>0}(F)$$이고 $$F$$가 콤팩트 다양체이므로 $$H^{>0}(F;\mathbb{Q})$$의 원소는 모두 nilpotent이다. 한 인수를 $$x_{\chi,j}+\chi=\chi(1+\chi^{-1}x_{\chi,j})$$로 쓰면, $$\chi\neq 0$$이라 $$\chi$$는 $$\mathrm{Frac}(R)$$에서 가역이고 $$\chi^{-1}x_{\chi,j}$$은 nilpotent이므로 $$1+\chi^{-1}x_{\chi,j}$$은 가역이다 (그 역은 유한 geometric series이다). 따라서 각 인수가 $$H^\bullet(F)\otimes\mathrm{Frac}(R)$$에서 가역이고 그 곱 $$e_T(N_F)$$도 가역이다. 동치로, $$e_T(N_F)$$을 차수에 따라 분해하면 그 최저차 항은 $$\prod_\chi\chi^{\mathrm{rank}(N_F)_\chi}\in R$$이라는 $$R$$의 $$0$$이 아닌 원소이고, 나머지는 $$H^{>0}(F)$$에서 온 nilpotent 보정이다.

</details>

Isolated fixed point에서는 $$e_T(N_p)=\prod_j w_j$$이 $$R$$의 $$0$$이 아닌 원소이므로, 보정항 없이 곧바로 $$\mathrm{Frac}(R)$$에서 가역이다. 일반적인 양의 차원 성분에서도 국소화 후에는 분모에 둘 수 있는 양이 된다는 것이 이 명제의 내용이다.

## 동변 적분

콤팩트 oriented 다양체 위에서는 cohomology class를 fundamental class 위에서 평가하는 적분이 있다. ([\[대수적 위상수학\] §푸앵카레 쌍대성, ⁋정의 10](/ko/math/algebraic_topology/Poincare_duality#def10)) 동변 판본에서는 이것이 $$R$$에 값을 갖는 $$R$$-선형 사상이 되며, fiber를 따라 적분하는 Gysin 사상으로 실현된다.

<div class="definition" markdown="1">

<ins id="def4">**정의 4**</ins> $$M$$이 $$\dim_{\mathbb{R}}M=d$$인 콤팩트 oriented $$T$$-다양체라 하자. Borel 구성 $$M_T\rightarrow BT$$은 fiber $$M$$을 갖는 oriented fiber bundle이므로 ([§동변 코호몰로지, ⁋명제 2](/ko/math/toric_geometry/equivariant_cohomology#prop2)), fiber를 따른 적분 (Gysin 사상)

$$\int_M:H_T^k(M)=H^k(M_T)\longrightarrow H^{k-d}(BT)=R^{k-d}$$

이 정의된다. 이를 $$M$$ 위의 *equivariant integration<sub>동변 적분</sub>* 또는 $$M\rightarrow\mathrm{pt}$$의 pushforward $$\pi_\ast$$라 부른다. 같은 방식으로 닫힌 $$T$$-부분다양체의 포함 $$j:F\hookrightarrow M$$ (normal bundle이 oriented) 에 대해 차수를 $$\mathrm{codim}F$$만큼 올리는 동변 Gysin pushforward $$j_\ast:H_T^\bullet(F)\rightarrow H_T^{\bullet+\mathrm{codim}F}(M)$$이 정의된다.

</div>

$$\int_M$$은 $$R$$-선형이며 차수를 $$d=\dim_{\mathbb{R}}M$$만큼 낮춘다. Borel 구성을 잊고 $$t_i=0$$으로 보내면 ([§동변 코호몰로지, ⁋정의 8](/ko/math/toric_geometry/equivariant_cohomology#def8)의 augmentation) 보통의 적분 $$H^\bullet(M)\rightarrow\mathbb{Q}$$, 곧 fundamental class 위에서의 평가로 환원된다. Fiber 적분과 동변 Gysin 사상의 구성은 [BT]의 §6과 [AF]의 §2를 따른다. 이 적분이 fixed component로 어떻게 분해되는지를 지배하는 것이 다음의 세 항등식이다.

<div class="proposition" markdown="1">

<ins id="prop5">**명제 5**</ins> $$j_F:F\hookrightarrow M$$을 fixed component의 포함, $$\pi_M:M\rightarrow\mathrm{pt}$$, $$\pi_F:F\rightarrow\mathrm{pt}$$을 상수사상이라 하자. 그럼 다음이 성립한다.

1. (자기교차 공식) 모든 $$\beta\in H_T^\bullet(F)$$에 대하여 $$j_F^\ast j_{F\ast}\beta=e_T(N_F)\smile\beta$$이다.
2. (직교성) 서로 다른 성분 $$F\neq G$$에 대하여 $$j_F^\ast j_{G\ast}=0$$이다.
3. (함자성) $$\pi_{M\ast}\circ j_{F\ast}=\pi_{F\ast}$$, 곧 $$\int_M j_{F\ast}\beta=\int_F\beta$$이다.

</div>
<details class="proof" markdown="1">
<summary>증명</summary>

(1) 동변 Thom class를 통한 자기교차 공식이다. 닫힌 부분다양체 $$F$$의 동변 tubular neighborhood는 $$N_F$$의 disk bundle과 동일시되고 (명제 1), 그 동변 Thom class $$u\in H_T^{\mathrm{codim}F}(N_F,N_F^\circ)$$의 zero section으로의 제한이 동변 Euler class $$e_T(N_F)$$이다. ([\[대수적 위상수학\] §벡터다발의 특성류, ⁋정리 2](/ko/math/algebraic_topology/characteristic_classes#thm2)의 동변 판본) Pushforward $$j_{F\ast}$$은 Thom class와의 곱 뒤 확장으로 정의되므로, 그 즉시 되돌려 제한하면 $$j_F^\ast j_{F\ast}\beta=e_T(N_F)\smile\beta$$를 얻는다.

(2) $$F$$와 $$G$$가 서로소이므로 $$j_{G\ast}\beta$$는 $$G$$의 한 근방에 support를 갖는 class로 표현되고, 그것을 $$F$$로 제한하면 $$0$$이다.

(3) 동변 Gysin 사상의 함자성으로, $$\pi_M\circ j_F=\pi_F$$이면 pushforward도 합성된다. 동변 Thom 동형과 fiber 적분의 함자성에서 따라온다. 자세한 내용은 [AF]의 §2, [BGV]의 §7을 따른다.

</details>

(1)은 보통의 위상수학에서 부분다양체의 자기교차가 그 normal bundle의 Euler class로 주어진다는 사실의 동변 판본이며, (3)은 "먼저 $$F$$에 밀어 넣고 $$M$$ 위에서 적분하나, $$F$$ 위에서 바로 적분하나 같다"는 명백한 사실이다. 세 항등식을 합치면, $$M$$ 전체에서의 적분을 fixed component들로 쪼개 읽는 길이 열린다.

## 국소화 정리

이제 핵심 보조정리로 넘어간다. Fixed locus를 제거한 자리 위에서는 작용이 어디서도 자명하지 않으므로, 그 equivariant cohomology가 $$R$$ 위에서 torsion이 된다. 이것이 국소화의 대수적 원천이다.

<div class="proposition" markdown="1">

<ins id="lem6">**보조정리 6**</ins> $$U=M\setminus M^T$$이라 하면 $$H_T^\bullet(U)$$은 torsion $$R$$-가군이다. 같은 결론이 pair의 상대 cohomology $$H_T^\bullet(M,M^T)$$에도 성립한다.

</div>
<details class="proof" markdown="1">
<summary>증명</summary>

$$U$$의 한 점 $$x$$를 보자. $$x$$는 고정점이 아니므로 그 stabilizer $$T_x=\{g\in T\mid g\cdot x=x\}$$은 $$T$$의 진부분 닫힌 부분군이다. Slice 정리에 의해 $$x$$는 $$T$$-불변 근방 $$T\times_{T_x}S_x$$ ($$S_x$$는 slice) 를 가지며, 이때

$$H_T^\bullet(T\times_{T_x}S_x)=H_{T_x}^\bullet(S_x)$$

이다. 이 가군 위의 $$R=H_T^\bullet(\mathrm{pt})$$-작용은 제한사상 $$R=H_T^\bullet(\mathrm{pt})\rightarrow H_{T_x}^\bullet(\mathrm{pt})$$을 거친다. $$T_x$$가 진부분군이므로 그 항등성분 $$T_x^0$$의 차원은 $$n$$보다 작거나, $$T_x$$가 유한군이다. $$\mathbb{Q}$$-계수에서 $$H_{T_x}^\bullet(\mathrm{pt};\mathbb{Q})=H^\bullet(BT_x^0;\mathbb{Q})=\mathrm{Sym}_{\mathbb{Q}}\big(\mathrm{Hom}(T_x^0,S^1)\otimes\mathbb{Q}\big)$$이고, 제한사상 $$M_T\otimes\mathbb{Q}\rightarrow\mathrm{Hom}(T_x^0,S^1)\otimes\mathbb{Q}$$은 차원이 떨어지므로 핵이 $$0$$이 아니다. 그 핵의 $$0$$이 아닌 원소 $$\chi\in R$$을 고르면, $$\chi$$는 $$H_{T_x}^\bullet(S_x)$$ 위에서 $$0$$으로 작용한다. 곧 $$\chi$$가 이 국소 가군을 소멸시킨다.

$$M^T$$이 콤팩트이고 그 보충 $$U$$를 위와 같은 유한 개의 $$T$$-불변 열린집합으로 덮을 수 있다. ($$M$$이 콤팩트이므로 임의의 콤팩트 부분집합이 유한 개로 덮이고, Mayer–Vietoris로 이어붙인다.) 각 조각을 소멸시키는 character들의 곱 $$\chi=\chi_1\cdots\chi_r\in R$$은 $$0$$이 아니며, Mayer–Vietoris 완전열을 따라 귀납하면 $$\chi$$가 $$H_T^\bullet(U)$$ 전체를 소멸시킨다. 따라서 $$H_T^\bullet(U)$$은 torsion이다. $$H_T^\bullet(M,M^T)$$의 torsion성은 pair $$(M,M^T)$$의 동변 tubular neighborhood를 통한 excision으로 $$U$$의 (compactly supported) equivariant cohomology와 같은 orbit-type 조각들로 환원되어 같은 방식으로 따라온다. 전면적인 Mayer–Vietoris 논증은 [AB]의 §3과 [AF]의 §7을 따른다.

</details>

이 torsion 현상이 의미하는 바는 직관적으로 명료하다. $$\mathrm{Spec}R$$을 좌표공간으로 볼 때, equivariant cohomology는 그 위의 가군으로서 작용의 stabilizer가 비자명한 자리에 support를 가지며, 작용이 거의 자유로운 $$U$$ 위에서는 support가 원점 주변의 진부분 자취로 밀려나 분수체로 넘어가면 사라진다. 이제 본 정리를 증명한다.

<div class="proposition" markdown="1">

<ins id="thm7">**정리 7 (Atiyah–Bott, Berline–Vergne 국소화 정리)**</ins> 포함 $$i:M^T\hookrightarrow M$$이 유도하는 제한사상은 국소화 후 동형

$$i^\ast:H_T^\bullet(M)_{\mathrm{loc}}\xrightarrow{\ \cong\ }H_T^\bullet(M^T)_{\mathrm{loc}}=\bigoplus_F H_T^\bullet(F)_{\mathrm{loc}}$$

이 된다. 그 역사상은 fixed component 별 pushforward를 동변 Euler class로 나눈 것으로 주어진다. 곧 $$\beta=(\beta_F)_F$$에 대하여

$$(i^\ast)^{-1}(\beta)=\sum_F j_{F\ast}\left(\frac{\beta_F}{e_T(N_F)}\right)$$

이다.

</div>
<details class="proof" markdown="1">
<summary>증명</summary>

Pair $$(M,M^T)$$의 동변 cohomology 긴 완전열

$$\cdots\rightarrow H_T^k(M,M^T)\rightarrow H_T^k(M)\xrightarrow{\ i^\ast\ }H_T^k(M^T)\rightarrow H_T^{k+1}(M,M^T)\rightarrow\cdots$$

에 완전함수인 국소화 $$-\otimes_R\mathrm{Frac}(R)$$을 적용한다. [보조정리 6](#lem6)에 의해 $$H_T^\bullet(M,M^T)$$이 torsion이므로 $$H_T^\bullet(M,M^T)_{\mathrm{loc}}=0$$이고, 따라서 완전열에서 양옆 항이 사라져

$$i^\ast:H_T^\bullet(M)_{\mathrm{loc}}\xrightarrow{\ \cong\ }H_T^\bullet(M^T)_{\mathrm{loc}}$$

이 동형이다.

역사상의 명시적 형태를 확인하기 위해 사상 $$J(\beta)=\sum_F j_{F\ast}\big(\beta_F/e_T(N_F)\big)$$을 생각한다 ([명제 3](#prop3)에 의해 $$e_T(N_F)$$이 국소화 후 가역이라 잘 정의된다). 임의의 성분 $$G$$에 대하여 $$J(\beta)$$를 $$G$$로 제한하면, [명제 5](#prop5)의 직교성으로 $$F\neq G$$ 항이 모두 사라지고 자기교차 공식으로

$$j_G^\ast J(\beta)=j_G^\ast j_{G\ast}\left(\frac{\beta_G}{e_T(N_G)}\right)=e_T(N_G)\smile\frac{\beta_G}{e_T(N_G)}=\beta_G$$

이다. 곧 $$i^\ast\circ J=\mathrm{id}$$이고, $$i^\ast$$이 이미 동형이므로 $$J=(i^\ast)^{-1}$$이다.

</details>

정리의 내용을 다시 읽으면, $$H_T^\bullet(M)_{\mathrm{loc}}$$의 임의의 원소 $$\alpha$$는 그 fixed point로의 제한 $$(i_F^\ast\alpha)_F$$만으로 완전히 복원된다. 곧

$$\alpha=\sum_F j_{F\ast}\left(\frac{i_F^\ast\alpha}{e_T(N_F)}\right)\quad\text{in }H_T^\bullet(M)_{\mathrm{loc}}$$

이 항상 성립한다. 이는 [§동변 코호몰로지, ⁋예시 6](/ko/math/toric_geometry/equivariant_cohomology#ex6)에서 관찰한 "fixed point로의 제한이 거의 단사"라는 현상의 정확한 형태이다. Equivariantly formal한 경우 ([§동변 코호몰로지, ⁋정의 8](/ko/math/toric_geometry/equivariant_cohomology#def8)) 에는 제한사상이 국소화 이전에도 단사이므로, 국소화는 단사성을 전사성까지 끌어올리는 역할만 한다.

## Atiyah–Bott–Berline–Vergne 적분 공식

국소화 정리에 동변 적분을 결합하면, $$M$$ 전체에서의 적분이 fixed component 각각에서의 국소 적분의 합으로 분해된다.

<div class="proposition" markdown="1">

<ins id="thm8">**정리 8 (ABBV 적분 공식)**</ins> $$\alpha\in H_T^\bullet(M)$$에 대하여

$$\int_M\alpha=\sum_F\int_F\frac{i_F^\ast\alpha}{e_T(N_F)}$$

이 $$\mathrm{Frac}(R)$$ 안에서 성립한다. 여기서 합은 fixed locus $$M^T$$의 connected 성분 $$F$$ 전체에 대한 것이다. 특히 좌변은 $$R$$의 원소이고 우변은 fixed point에서의 데이터만으로 계산된다.

</div>
<details class="proof" markdown="1">
<summary>증명</summary>

[정리 7](#thm7)의 등식 $$\alpha=\sum_F j_{F\ast}\big(i_F^\ast\alpha/e_T(N_F)\big)$$을 $$H_T^\bullet(M)_{\mathrm{loc}}$$ 안에서 잡고, $$\mathrm{Frac}(R)$$-선형으로 확장한 동변 적분 $$\int_M$$을 양변에 적용한다. [명제 5](#prop5)의 함자성 $$\int_M\circ j_{F\ast}=\int_F$$로부터

$$\int_M\alpha=\sum_F\int_M j_{F\ast}\left(\frac{i_F^\ast\alpha}{e_T(N_F)}\right)=\sum_F\int_F\frac{i_F^\ast\alpha}{e_T(N_F)}$$

를 얻는다. 좌변 $$\int_M\alpha$$은 정의상 $$R$$에 속하므로, 우변의 합도 $$R$$의 원소이다 (각 항은 $$\mathrm{Frac}(R)$$에 있으나 그 합은 분모가 약분되어 $$R$$로 떨어진다).

</details>

가장 자주 쓰는 경우는 fixed point가 모두 isolated일 때이다. 이때 각 $$F=\{p\}$$에서 $$\int_p$$은 단순히 $$p$$에서의 값을 읽는 것이고 $$e_T(N_p)=\prod_j w_j(p)$$이므로, 공식이 다음과 같이 단순해진다.

<div class="proposition" markdown="1">

<ins id="cor9">**따름정리 9**</ins> $$M^T$$이 유한 개의 isolated fixed point들로 이루어진 경우, 각 $$p\in M^T$$의 isotropy weight를 $$w_1(p),\ldots,w_m(p)$$ ($$m=\dim_{\mathbb{C}}M$$) 이라 하면

$$\int_M\alpha=\sum_{p\in M^T}\frac{i_p^\ast\alpha}{\prod_{j=1}^m w_j(p)}$$

이다. 더 나아가 동변 tangent bundle의 Euler class $$\alpha=e_T(TM)$$을 대입하면

$$\chi(M)=\#M^T$$

곧 Euler characteristic이 fixed point의 개수와 같다. 일반적으로 fixed locus가 양의 차원 성분을 가질 때는 $$\chi(M)=\sum_F\chi(F)$$이다.

</div>
<details class="proof" markdown="1">
<summary>증명</summary>

첫 식은 [정리 8](#thm8)에서 $$F=\{p\}$$, $$i_p^\ast\alpha\in R$$, $$e_T(N_p)=\prod_j w_j(p)$$을 대입한 것이다.

둘째 식을 보자. Isolated fixed point에서는 $$N_p=T_pM$$이므로 $$i_p^\ast e_T(TM)=e_T(T_pM)=e_T(N_p)$$이고, 따라서

$$\int_M e_T(TM)=\sum_{p}\frac{e_T(N_p)}{e_T(N_p)}=\sum_p 1=\#M^T$$

이다. 한편 $$\int_M e_T(TM)$$은 차수 $$2m-2m=0$$의 $$R$$-원소, 곧 상수이며, $$t_i=0$$으로 보내면 보통의 적분 $$\int_M e(TM)$$가 된다. 보통의 Euler class를 fundamental class 위에서 평가한 값이 Euler characteristic $$\chi(M)$$이므로 ([\[대수적 위상수학\] §벡터다발의 특성류, ⁋명제 4](/ko/math/algebraic_topology/characteristic_classes#prop4)의 tangent bundle에 대한 Poincaré–Hopf 해석) $$\int_M e_T(TM)=\chi(M)$$이고, 따라서 $$\chi(M)=\#M^T$$이다. 양의 차원 성분이 있는 일반적 경우에는 각 성분에서 $$i_F^\ast e_T(TM)=e_T(TF)\smile e_T(N_F)$$이므로 ($$TM\vert_F=TF\oplus N_F$$에 대한 Whitney 합 공식) ABBV의 피적분은 $$e_T(TF)\smile e_T(N_F)/e_T(N_F)=e_T(TF)$$이고, $$T$$가 $$F$$ 위에서 자명하게 작용하므로 $$\int_F e_T(TF)=\int_F e(TF)=\chi(F)$$가 되어 $$\chi(M)=\sum_F\chi(F)$$를 얻는다.

</details>

곧 Atiyah–Bott–Berline–Vergne 공식은 위상적 불변량인 Euler characteristic을 "fixed point를 세는" 조합적 양으로 바꾸어 주며, 이는 콤팩트 Lie group 작용에 대한 고전적인 결과를 동변 적분의 특수한 경우로 회수한다.

## 예시: 사영공간

[§동변 코호몰로지, ⁋정리 7](/ko/math/toric_geometry/equivariant_cohomology#thm7)에서 계산한 $$\mathbb{P}^n$$ 위의 표준 작용으로 돌아가, ABBV 공식이 무엇을 주는지를 본다. $$T=(S^1)^{n+1}$$이 좌표별로 작용하고, fixed point는 $$n+1$$개의 좌표점 $$p_i=[0:\cdots:1:\cdots:0]$$ ($$i$$번째 자리에 $$1$$) 이다.

<div class="example" markdown="1">

<ins id="ex10">**예시 10**</ins> $$\mathbb{P}^n$$의 fixed point $$p_i$$에서 tangent space는

$$T_{p_i}\mathbb{P}^n=\mathrm{Hom}\Big(\mathbb{C}_{t_i},\bigoplus_{j\neq i}\mathbb{C}_{t_j}\Big)=\bigoplus_{j\neq i}\mathbb{C}_{t_j-t_i}$$

이므로 isotropy weight는 $$\{t_j-t_i\mid j\neq i\}$$이고, 따라서

$$e_T(N_{p_i})=\prod_{j\neq i}(t_j-t_i)$$

이다. [§동변 코호몰로지, ⁋정리 7](/ko/math/toric_geometry/equivariant_cohomology#thm7)에서 $$h=c_1(\mathcal{O}(-1))$$의 fixed point 제한은 $$i_{p_i}^\ast h=t_i$$였다. [따름정리 9](#cor9)를 $$\alpha=h^k$$에 적용하면

$$\int_{\mathbb{P}^n}h^k=\sum_{i=0}^n\frac{t_i^k}{\prod_{j\neq i}(t_j-t_i)}$$

이다. 좌변은 차수 $$2k-2n$$의 상수 또는 $$0$$이므로 우변도 그러해야 하고, 실제로 이는 Lagrange 보간에서 나오는 고전적 항등식

$$\sum_{i=0}^n\frac{t_i^k}{\prod_{j\neq i}(t_i-t_j)}=h_{k-n}(t_0,\ldots,t_n)$$

($$h_{k-n}$$은 complete homogeneous symmetric polynomial, 음의 차수이면 $$0$$) 의 한 형태이다. 분모의 부호를 정리하면 $$\prod_{j\neq i}(t_j-t_i)=(-1)^n\prod_{j\neq i}(t_i-t_j)$$이므로

$$\int_{\mathbb{P}^n}h^k=(-1)^n h_{k-n}(t_0,\ldots,t_n)$$

이다. 두 가지 특수한 경우가 의미를 분명히 해 준다.

1. $$k=0$$, 곧 $$\alpha=1$$이고 $$n\geq 1$$이면 $$h_{-n}=0$$이므로

$$\sum_{i=0}^n\frac{1}{\prod_{j\neq i}(t_j-t_i)}=0$$

이다. 이것이 Bott 잔여 형태의 vanishing 항등식이며, 차수가 모자라 적분이 $$0$$이어야 한다는 사실의 화신이다.

2. $$k=n$$이면 $$h_0=1$$이므로 $$\int_{\mathbb{P}^n}h^n=(-1)^n$$이다. 동치로 ample hyperplane class $$\zeta=c_1(\mathcal{O}(1))=-h$$를 쓰면 $$i_{p_i}^\ast\zeta=-t_i$$이고

$$\int_{\mathbb{P}^n}\zeta^n=\sum_{i=0}^n\frac{(-t_i)^n}{\prod_{j\neq i}(t_j-t_i)}=\sum_{i=0}^n\frac{t_i^n}{\prod_{j\neq i}(t_i-t_j)}=1$$

이 되어, $$\mathbb{P}^n$$의 차수 $$\int_{\mathbb{P}^n}\zeta^n=1$$을 fixed point의 합으로 회복한다.

</div>

이 예시에서 주목할 점은, 우변의 각 항이 $$t_i$$의 유리함수로 분모를 가짐에도 그 합이 $$t$$에 무관한 정수가 된다는 것이다. ABBV 공식은 이 "기적적인 약분"이 사실은 $$M$$ 위의 적분이라는 위상적 양의 그림자임을 설명한다. 또한 [따름정리 9](#cor9)의 Euler characteristic 계산은 여기서 $$\chi(\mathbb{P}^n)=\#\{p_0,\ldots,p_n\}=n+1$$로 즉시 확인된다.

## 예시: Grassmannian

다음으로 Grassmannian $$\mathrm{Gr}(k,n)$$, 곧 $$\mathbb{C}^n$$의 $$k$$차원 부분공간들의 공간을 보자. $$T=(S^1)^n$$이 $$\mathbb{C}^n$$의 좌표에 작용하면 $$\mathrm{Gr}(k,n)$$ 위에 작용이 유도되고, 그 fixed point는 좌표 부분공간들이다. 이는 Schubert calculus의 동변 판본으로 가는 입구가 된다.

<div class="example" markdown="1">

<ins id="ex11">**예시 11**</ins> $$T=(S^1)^n$$이 좌표별로 작용하는 $$\mathrm{Gr}(k,n)$$에서, $$k$$-원소 부분집합 $$I\subseteq\{1,\ldots,n\}$$마다 좌표 부분공간 $$E_I=\mathrm{span}(e_i\mid i\in I)$$이 fixed point이고, fixed point는 정확히 이들 $$\binom{n}{k}$$개이다. $$E_I$$에서 tangent space는

$$T_{E_I}\mathrm{Gr}(k,n)=\mathrm{Hom}\big(E_I,\mathbb{C}^n/E_I\big)=\bigoplus_{i\in I,\ j\notin I}\mathbb{C}_{t_j-t_i}$$

이므로 isotropy weight는 $$\{t_j-t_i\mid i\in I,\ j\notin I\}$$이고

$$e_T(N_{E_I})=\prod_{i\in I,\ j\notin I}(t_j-t_i)$$

이다. [따름정리 9](#cor9)로부터 우선 $$\chi\big(\mathrm{Gr}(k,n)\big)=\binom{n}{k}$$를 얻는다. 일반적인 class $$\alpha$$에 대해서는

$$\int_{\mathrm{Gr}(k,n)}\alpha=\sum_{\lvert I\rvert=k}\frac{i_{E_I}^\ast\alpha}{\prod_{i\in I,\ j\notin I}(t_j-t_i)}$$

이다.

구체적인 Schubert calculus 계산으로 $$\mathrm{Gr}(2,4)$$의 Plücker 차수를 회복하자. Plücker 매장 $$\mathrm{Gr}(k,n)\hookrightarrow\mathbb{P}\big(\bigwedge^k\mathbb{C}^n\big)$$에서 hyperplane class $$\zeta=c_1(\mathcal{O}(1))$$의 fixed point 제한은 [예시 10](#ex10)의 $$\mathbb{P}^n$$ 컨벤션과 마찬가지로 tautological line $$\mathcal{O}(-1)$$의 fiber인 Plücker 좌표선 $$\bigwedge^k E_I=e_{i_1}\wedge\cdots\wedge e_{i_k}$$ ($$I=\{i_1<\cdots<i_k\}$$) 의 weight $$\sum_{i\in I}t_i$$에 부호를 뒤집은 것, 곧

$$i_{E_I}^\ast\zeta=-\sum_{i\in I}t_i$$

이다. $$\dim_{\mathbb{C}}\mathrm{Gr}(2,4)=4$$이므로 차수는 $$\int_{\mathrm{Gr}(2,4)}\zeta^4$$이고, ABBV로

$$\int_{\mathrm{Gr}(2,4)}\zeta^4=\sum_{\lvert I\rvert=2}\frac{\big(-\sum_{i\in I}t_i\big)^4}{\prod_{i\in I,\ j\notin I}(t_j-t_i)}=2$$

가 된다 (우변은 $$t$$에 무관한 상수이며 $$2$$로 계산된다). 이는 $$\mathrm{Gr}(2,4)\subset\mathbb{P}^5$$의 차수가 $$2$$, 곧 $$\mathbb{P}^3$$ 안에서 일반 위치의 네 직선과 모두 만나는 직선의 개수가 $$2$$라는 고전적 Schubert 계산과 일치한다.

</div>

이 예시가 보여 주듯, Schubert class의 fixed point 제한 $$i_{E_I}^\ast\sigma_\lambda$$만 알면 모든 교차수가 좌표 부분공간 위의 유한합으로 환원된다. 이 제한값들은 factorial Schur polynomial로 명시되며, equivariant Schubert calculus는 바로 이 국소화 데이터를 조직하는 이론이다.

## 매끄러운 toric variety로의 적용

마지막으로 이 글의 무대인 toric variety와의 연결을 본다. $$N$$을 rank $$n$$ lattice, $$\Sigma\subset N_{\mathbb{R}}$$를 fan, $$X_\Sigma$$를 그에 대응하는 toric variety라 하자. ([§토릭 다양체의 정의, ⁋정의 3](/ko/math/toric_geometry/toric_varieties#def3)) $$X_\Sigma$$ 위에는 algebraic torus $$T_N=N\otimes\mathbb{C}^\ast$$의 작용이 있고 ([§토릭 다양체의 정의, ⁋명제 5](/ko/math/toric_geometry/toric_varieties#prop5)), 그 콤팩트 부분군 $$T=(S^1)^n$$이 $$X_\Sigma$$ 위에 작용한다. $$X_\Sigma$$가 smooth complete이면 ([§토릭 다양체의 정의, ⁋명제 11](/ko/math/toric_geometry/toric_varieties#prop11)) 콤팩트 oriented 다양체로서 ABBV 공식의 가정을 만족한다.

이때 $$T$$-fixed point는 fan의 maximal cone, 곧 $$n$$차원 cone $$\sigma\in\Sigma(n)$$과 일대일 대응한다. 실제로 cone $$\sigma$$에 대응하는 orbit closure $$V(\sigma)$$는 ([§토릭 다양체의 교차 이론, ⁋정의 1](/ko/math/toric_geometry/toric_intersection_theory#def1)) $$\sigma$$가 maximal일 때 한 점으로 줄어들며, 이것이 affine chart $$U_\sigma\cong\mathbb{C}^n$$의 원점인 fixed point $$x_\sigma$$이다. $$X_\Sigma$$가 사영적이면 maximal cone들은 그 fan을 normal fan으로 갖는 polytope $$P$$의 꼭짓점들과 대응하므로 ([§토릭 다양체의 정의, ⁋명제 8](/ko/math/toric_geometry/toric_varieties#prop8)), fixed point는 곧 $$P$$의 꼭짓점이다.

각 fixed point $$x_\sigma$$에서 isotropy weight를 읽는 것도 조합적이다. Smooth maximal cone $$\sigma$$는 $$N$$의 기저를 이루는 primitive ray generator $$v_1,\ldots,v_n$$으로 생성되며, tangent space $$T_{x_\sigma}X_\Sigma$$의 weight는 정확히 이 기저의 dual basis $$u_1,\ldots,u_n\in M$$ (곧 $$\langle u_i,v_j\rangle=\delta_{ij}$$) 이다. 따라서

$$e_T(N_{x_\sigma})=\prod_{i=1}^n u_i\in R$$

이고, [따름정리 9](#cor9)는 임의의 $$\alpha\in H_T^\bullet(X_\Sigma)$$에 대하여

$$\int_{X_\Sigma}\alpha=\sum_{\sigma\in\Sigma(n)}\frac{i_{x_\sigma}^\ast\alpha}{\prod_{i=1}^n u_i^\sigma}$$

을 준다. 곧 ABBV 공식은 $$X_\Sigma$$ 위의 동변 교차수를 fan의 꼭짓점 (maximal cone) 들에 대한 유한합으로 바꾸며, 각 꼭짓점의 기여는 그 cone의 dual basis로 명시된다.

이 합의 항들은 [§토릭 다양체의 교차 이론, ⁋정리 5](/ko/math/toric_geometry/toric_intersection_theory#thm5)에서 본, smooth complete toric variety의 cohomology ring을 fan으로부터 조합적으로 기술하는 표현과 정확히 호응한다. 거기서 cohomology class는 ray에 대응하는 divisor class들의 다항식으로 주어졌고, fixed point로의 제한은 그 다항식을 각 maximal cone의 좌표로 평가하는 것에 해당한다. 따라서 toric variety의 교차 이론 전체가 두 가지 조합적 데이터, 곧 cohomology ring의 fan 표현과 ABBV의 꼭짓점별 국소화 사이의 변환으로 정리된다. Fixed point가 모두 isolated이고 꼭짓점으로 명시되는 toric 세팅은 국소화 정리가 가장 투명하게 작동하는 본보기이다.

---

**참고문헌**

**[AB]** M. F. Atiyah and R. Bott, *The moment map and equivariant cohomology*, Topology **23** (1984), 1–28.

**[BGV]** N. Berline, E. Getzler, and M. Vergne, *Heat Kernels and Dirac Operators*, Grundlehren der mathematischen Wissenschaften 298, Springer, 1992.

**[GS]** V. W. Guillemin and S. Sternberg, *Supersymmetry and Equivariant de Rham Theory*, Springer, 1999.

**[AF]** D. Anderson and W. Fulton, *Equivariant Cohomology in Algebraic Geometry*, Cambridge Studies in Advanced Mathematics 210, Cambridge University Press, 2023.

**[BT]** R. Bott and L. W. Tu, *Differential Forms in Algebraic Topology*, Springer, 1982.
