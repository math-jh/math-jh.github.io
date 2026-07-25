---
title: "Gorenstein 환"
description: "정칙성이 projective dimension의 유한성으로 특징지어지는 것과 쌍대로, injective dimension이 유한한 local ring인 Gorenstein ring을 Bass 정리로 다루어 depth와의 일치, Cohen-Macaulay 성질, regular sequence 몫과의 관계, 그리고 Artinian인 경우의 socle 특징화를 확립한다."
excerpt: "Gorenstein local ring과 Bass 정리, socle 특징화"

categories: [Math / Commutative Algebra]
permalink: /ko/math/commutative_algebra/gorenstein_rings
sidebar: 
    nav: "commutative_algebra-ko"

date: 2026-07-24
weight: 32
published: false
drift_needed: true

---

[§정칙성의 호몰로지 판정, ⁋정리 3](/ko/math/commutative_algebra/homological_criterion_for_regularity#thm3)에서 우리는 Noetherian local ring이 regular인 것과 global dimension이 유한한 것, 곧 residue field의 projective dimension이 유한한 것이 서로 동치임을 보았다. Projective 쪽의 이 유한성이 regular라는 강한 조건을 정확히 골라냈다면, 그 쌍대에 해당하는 injective 쪽의 유한성 조건이 어떤 local ring을 특징짓는지가 이 글의 출발점이다. 우리는 $\operatorname{injdim}_AA<\infty$인 Noetherian local ring, 곧 Gorenstein ring을 다룬다. Bass의 정리로 이 injective dimension이 depth와 같음을 보이고, 그로부터 Gorenstein ring이 Cohen--Macaulay임을 유도하며, regular sequence에 대한 quotient와의 관계를 세운 뒤, Artinian인 경우 이 조건이 socle의 $1$차원성으로 정확히 특징지어짐을 확인한다.

## Injective dimension이 유한한 local ring

[§단사가군과 Matlis 쌍대성, ⁋명제 7](/ko/math/commutative_algebra/matlis_duality#prop7)은 Noetherian local ring $(A,\mathfrak{m},\kappa)$ 위의 finitely generated module의 injective dimension을 오직 residue field와의 $\Ext$의 소멸 차수로 읽어낸다. 이 판정과 [§코쥴 복합체](/ko/math/commutative_algebra/koszul_complex)의 도구를 결합하면, injective dimension이 유한할 때 그 값이 정확히 무엇인지가 결정된다.

::: 정리 1 (Bass)
Noetherian local ring $(A,\mathfrak{m},\kappa)$ 위의 $0$이 아닌 finitely generated $A$-module $M$이 $\operatorname{injdim}_AM<\infty$를 만족하면
$$\operatorname{injdim}_AM=\operatorname{depth}A$$
가 성립한다.
:::
::: 증명
$t=\operatorname{depth}A$로 두고, $\mathfrak{m}$ 안의 maximal $A$-sequence $x_1,\ldots,x_t$를 택하자. ([§Depth, ⁋정리 2](/ko/math/commutative_algebra/depth#thm2)) $x=(x_1,\ldots,x_t)$로 적으면 이는 $A$-regular sequence이므로 [§코쥴 복합체, ⁋따름정리 8](/ko/math/commutative_algebra/koszul_complex#cor8)에 의하여 각 $j$에서
$$\Ext_A^j(A/(x),M)\cong H^j(x;M)$$
이다.

먼저 $\operatorname{injdim}_AM\geq t$를 보인다. $x$가 $t$개의 원소이므로 [§코쥴 복합체, ⁋명제 4](/ko/math/commutative_algebra/koszul_complex#prop4)의 self-duality와 [§코쥴 복합체, ⁋명제 2](/ko/math/commutative_algebra/koszul_complex#prop2)의 $H_0$ 계산에 의하여
$$H^t(x;M)\cong H_0(x;M)=M/xM$$
이다. $M\neq 0$이 finitely generated이고 $x_i\in\mathfrak{m}$이므로 [§정수적 확장, ⁋보조정리 8](/ko/math/commutative_algebra/integral_extension#lem8)에 의하여 $M/xM\neq 0$이고, 따라서 $\Ext_A^t(A/(x),M)\neq 0$이다. [§호몰로지 차원, ⁋명제 3](/ko/math/commutative_algebra/homological_dimension#prop3)에 의하여 이는 $\operatorname{injdim}_AM\geq t$를 준다.

이제 $s=\operatorname{injdim}_AM$으로 두면 가정에 의하여 $s<\infty$이고 방금 보인 것에서 $s\geq t$이다. 반대 부등식 $s\leq t$를 보이자. [§Depth, ⁋따름정리 4](/ko/math/commutative_algebra/depth#cor4)의 둘째 결과를 $I=\mathfrak{m}$에 대하여 반복 적용하면 각 $i$에서 $\operatorname{depth}(A/(x_1,\ldots,x_i))=\operatorname{depth}A-i$이므로 $\operatorname{depth}(A/(x))=t-t=0$이고, 다시 [§Depth, ⁋따름정리 4](/ko/math/commutative_algebra/depth#cor4)의 첫째 결과에 의하여 $\mathfrak{m}\in\Ass(A/(x))$이다. 곧 annihilator가 $\mathfrak{m}$인 원소가 있어 embedding $\kappa\hookrightarrow A/(x)$를 얻는다. 그 cokernel을 $C$라 하면 short exact sequence
$$0\rightarrow\kappa\rightarrow A/(x)\rightarrow C\rightarrow 0$$
을 얻고, 여기에 $\Hom_A(-,M)$의 long exact sequence를 적용한
$$\Ext_A^s(A/(x),M)\rightarrow\Ext_A^s(\kappa,M)\rightarrow\Ext_A^{s+1}(C,M)$$
에서 $s+1>\operatorname{injdim}_AM$이므로 [§호몰로지 차원, ⁋명제 3](/ko/math/commutative_algebra/homological_dimension#prop3)에 의하여 $\Ext_A^{s+1}(C,M)=0$이고, 따라서 첫째 map은 surjective이다. 한편 [§단사가군과 Matlis 쌍대성, ⁋명제 7](/ko/math/commutative_algebra/matlis_duality#prop7)에 의하여 $s=\sup\{i\mid\Ext_A^i(\kappa,M)\neq 0\}$이므로 $\Ext_A^s(\kappa,M)\neq 0$이고, surjectivity로부터 $\Ext_A^s(A/(x),M)\neq 0$이다. 그런데 $\Ext_A^s(A/(x),M)\cong H^s(x;M)$이고 Koszul cochain complex $K^\bullet(x;M)$은 $0\leq\bullet\leq t$에서만 $0$이 아닐 수 있으므로 $H^s(x;M)\neq 0$은 $s\leq t$를 강제한다. 종합하면 $s=t=\operatorname{depth}A$이다.
:::

이 정리에서 injective dimension이 유한하다는 가정은 결론을 위해 필수적이다. 값이 유한하기만 하면 그것이 무엇인지는 module의 세부 구조와 무관하게 오직 base ring의 depth로 결정된다. 특히 $M=A$인 경우가 이 글의 주인공이다.

::: 정의 2
Noetherian local ring $A$가 *Gorenstein*이라는 것은 $\operatorname{injdim}_AA<\infty$인 것이다.
:::

[정리 1](#thm1)을 $M=A$에 적용하면, Gorenstein local ring은 언제나 $\operatorname{injdim}_AA=\operatorname{depth}A$를 만족한다. 곧 Gorenstein 조건은 $A$를 자기 자신 위의 module로 보았을 때의 injective resolution이 유한한 길이에서 끝난다는 것이며, 이 때 그 길이는 depth와 일치한다. 앞으로 우리는 이 유한성이 localization과 regular sequence에 대한 quotient에 대해 어떻게 행동하는지를 추적한다. 그 첫걸음으로 $\Ext$가 localization과 교환한다는 사실을 정리해 둔다.

::: 보조정리 3
Noetherian ring $A$와 finitely generated $A$-module $N$, 임의의 $A$-module $M$, 그리고 multiplicative subset $S\subseteq A$에 대하여, 각 $i$에서
$$S^{-1}\Ext_A^i(N,M)\cong\Ext_{S^{-1}A}^i(S^{-1}N,S^{-1}M)$$
이 성립한다.
:::
::: 증명
$A$가 Noetherian이므로 $N$은 finitely generated free module들로 이루어진 resolution $F_\bullet\rightarrow N$을 갖는다. ([§기본 개념들, ⁋정리 3](/ko/math/commutative_algebra/basic_notions#thm3)) Localization은 exact이므로 ([§국소화의 성질들, ⁋명제 2](/ko/math/commutative_algebra/properties_of_localization#prop2)) $S^{-1}F_\bullet$은 $S^{-1}N$의 free resolution이다. 각 $F_j$는 finitely presented이고 $S^{-1}A$는 flat $A$-module이므로 ([§국소화의 성질들, ⁋명제 2](/ko/math/commutative_algebra/properties_of_localization#prop2)), [§국소화의 성질들, ⁋보조정리 1](/ko/math/commutative_algebra/properties_of_localization#lem1)의 $S^{-1}A\otimes_A(-)\cong S^{-1}(-)$와 [§국소화의 성질들, ⁋명제 5](/ko/math/commutative_algebra/properties_of_localization#prop5)를 종합하여
$$S^{-1}\Hom_A(F_j,M)\cong S^{-1}A\otimes_A\Hom_A(F_j,M)\cong\Hom_{S^{-1}A}(S^{-1}F_j,S^{-1}M)$$
을 얻는다. 이 isomorphism이 $j$에 대하여 자연스러우므로 cochain complex들의 isomorphism $S^{-1}\Hom_A(F_\bullet,M)\cong\Hom_{S^{-1}A}(S^{-1}F_\bullet,S^{-1}M)$을 이룬다. Localization이 cohomology와 교환하므로 (다시 [§국소화의 성질들, ⁋명제 2](/ko/math/commutative_algebra/properties_of_localization#prop2))
$$S^{-1}\Ext_A^i(N,M)=S^{-1}H^i(\Hom_A(F_\bullet,M))\cong H^i(\Hom_{S^{-1}A}(S^{-1}F_\bullet,S^{-1}M))=\Ext_{S^{-1}A}^i(S^{-1}N,S^{-1}M)$$
이다.
:::

이 보조정리는 injective dimension의 유한성이 localization으로 내려간다는 것을 보여준다.

::: 따름정리 4
Noetherian ring $A$와 finitely generated $A$-module $M$, 그리고 prime ideal $\mathfrak{p}$에 대하여 $\operatorname{injdim}_{A_\mathfrak{p}}(M_\mathfrak{p})\leq\operatorname{injdim}_A(M)$이 성립한다. 특히 $A$가 Gorenstein local ring이면 임의의 prime ideal $\mathfrak{p}$에 대하여 $A_\mathfrak{p}$도 Gorenstein local ring이다.
:::
::: 증명
$\operatorname{injdim}_AM=n<\infty$이라 하자 (아니면 부등식은 자명하다). [§호몰로지 차원, ⁋따름정리 5](/ko/math/commutative_algebra/homological_dimension#cor5)에 의하여 $A$의 모든 ideal $I$에 대하여 $\Ext_A^{n+1}(A/I,M)=0$이다. $A_\mathfrak{p}$의 임의의 ideal은 [§국소화, ⁋명제 8](/ko/math/commutative_algebra/localization#prop8)에 의하여 어떤 $A$의 ideal $J$의 extension $JA_\mathfrak{p}$이고, $(A/J)_\mathfrak{p}=A_\mathfrak{p}/JA_\mathfrak{p}$이므로 [보조정리 3](#lem3)에 의하여
$$\Ext_{A_\mathfrak{p}}^{n+1}(A_\mathfrak{p}/JA_\mathfrak{p},M_\mathfrak{p})\cong\Ext_A^{n+1}(A/J,M)_\mathfrak{p}=0$$
이다. 따라서 다시 [§호몰로지 차원, ⁋따름정리 5](/ko/math/commutative_algebra/homological_dimension#cor5)에 의하여 $\operatorname{injdim}_{A_\mathfrak{p}}(M_\mathfrak{p})\leq n$이다. $A$가 Gorenstein이면 $M=A$에 대하여 $\operatorname{injdim}_{A_\mathfrak{p}}A_\mathfrak{p}\leq\operatorname{injdim}_AA<\infty$이고, $A_\mathfrak{p}$는 Noetherian local ring이므로 ([§국소화, ⁋따름정리 9](/ko/math/commutative_algebra/localization#cor9)) Gorenstein이다.
:::

반대로, injective dimension은 prime ideal의 chain을 따라 올라갈 때 한 단계마다 적어도 $1$씩 커진다. 이 강하 성질이 다음 절에서 Gorenstein ring의 차원과 depth를 잇는 열쇠가 된다.

::: 보조정리 5
Noetherian local ring $(A,\mathfrak{m})$ 위의 $0$이 아닌 finitely generated $A$-module $M$과 prime ideal $\mathfrak{p}\subsetneq\mathfrak{m}$, 그리고 정수 $i$에 대하여, $\Ext_{A_\mathfrak{p}}^i(\kappa(\mathfrak{p}),M_\mathfrak{p})\neq 0$이면 $\operatorname{injdim}_AM\geq i+1$이다. 여기서 $\kappa(\mathfrak{p})=A_\mathfrak{p}/\mathfrak{p}A_\mathfrak{p}$이다.
:::
::: 증명
$(A/\mathfrak{p})_\mathfrak{p}$가 [§국소화, ⁋정의 10](/ko/math/commutative_algebra/localization#def10)의 residue field $\kappa(\mathfrak{p})$이므로, [보조정리 3](#lem3)에 의하여
$$\Ext_A^i(A/\mathfrak{p},M)_\mathfrak{p}\cong\Ext_{A_\mathfrak{p}}^i((A/\mathfrak{p})_\mathfrak{p},M_\mathfrak{p})=\Ext_{A_\mathfrak{p}}^i(\kappa(\mathfrak{p}),M_\mathfrak{p})\neq 0$$
이므로 $\Ext_A^i(A/\mathfrak{p},M)\neq 0$이다. 이제 $x\in\mathfrak{m}\setminus\mathfrak{p}$를 택하자. $A/\mathfrak{p}$가 integral domain이고 $x$의 image가 $0$이 아니므로 곱하기 $x$는 $A/\mathfrak{p}$ 위에서 injective이고, short exact sequence
$$0\rightarrow A/\mathfrak{p}\overset{x}{\longrightarrow}A/\mathfrak{p}\rightarrow A/(\mathfrak{p}+(x))\rightarrow 0$$
을 얻는다. 여기에 $\Hom_A(-,M)$의 long exact sequence를 적용한
$$\Ext_A^i(A/\mathfrak{p},M)\overset{x}{\longrightarrow}\Ext_A^i(A/\mathfrak{p},M)\overset{\delta}{\longrightarrow}\Ext_A^{i+1}(A/(\mathfrak{p}+(x)),M)$$
에서 가운데 map은 곱하기 $x$가 유도하는 스칼라 곱 $x$이고, 완전성에 의하여 그 cokernel은 $\Ext_A^{i+1}(A/(\mathfrak{p}+(x)),M)$의 submodule $\operatorname{im}\delta$와 isomorphic하다. 만일 $\Ext_A^{i+1}(A/(\mathfrak{p}+(x)),M)=0$이라면 곱하기 $x$가 $\Ext_A^i(A/\mathfrak{p},M)$ 위에서 surjective가 된다. $A$가 Noetherian이므로 $A/\mathfrak{p}$는 finitely generated free resolution을 갖고, 따라서 $\Ext_A^i(A/\mathfrak{p},M)$은 finitely generated $A$-module이다. ([§Depth, ⁋정리 7](/ko/math/commutative_algebra/depth#thm7)의 증명에서와 같은 논증이다.) $x\in\mathfrak{m}$이 이 module 위에서 surjective하게 작용하므로 [§정수적 확장, ⁋보조정리 8](/ko/math/commutative_algebra/integral_extension#lem8)에 의하여 $\Ext_A^i(A/\mathfrak{p},M)=0$이 되어 앞의 결과에 모순이다. 따라서 $\Ext_A^{i+1}(A/(\mathfrak{p}+(x)),M)\neq 0$이고, [§호몰로지 차원, ⁋명제 3](/ko/math/commutative_algebra/homological_dimension#prop3)에 의하여 $\operatorname{injdim}_AM\geq i+1$이다.
:::

두 보조정리를 종합하면 Gorenstein ring이 언제나 Cohen--Macaulay라는 것이 따라온다.

::: 정리 6
Gorenstein local ring $(A,\mathfrak{m})$은 Cohen--Macaulay local ring이다.
:::
::: 증명
$d=\dim A$로 두고 $\operatorname{injdim}_AA\geq d$를 보이면, [정리 1](#thm1)에 의하여 $\operatorname{depth}A=\operatorname{injdim}_AA\geq d$이고 [§Depth, ⁋따름정리 8](/ko/math/commutative_algebra/depth#cor8)의 $\operatorname{depth}A\leq\dim A=d$와 종합하여 $\operatorname{depth}A=\dim A$, 곧 [§Cohen-Macaulay 환, ⁋정의 1](/ko/math/commutative_algebra/cohen_macaulay_rings#def1)의 의미에서 $A$가 Cohen--Macaulay라는 결론을 얻는다.

길이 $d$의 prime ideal chain $\mathfrak{p}_0\subsetneq\mathfrak{p}_1\subsetneq\cdots\subsetneq\mathfrak{p}_d=\mathfrak{m}$을 택하자. ($\dim A=\codim\mathfrak{m}=d$이므로 $\mathfrak{m}$에서 끝나는 이러한 chain이 존재한다.) 각 $j$에 대하여 [따름정리 4](#cor4)에 의하여 $A_{\mathfrak{p}_j}$는 Gorenstein이므로 $d_j:=\operatorname{injdim}_{A_{\mathfrak{p}_j}}A_{\mathfrak{p}_j}$는 유한하고, [§단사가군과 Matlis 쌍대성, ⁋명제 7](/ko/math/commutative_algebra/matlis_duality#prop7)을 $A_{\mathfrak{p}_j}$에 적용하면
$$d_j=\sup\{i\mid\Ext_{A_{\mathfrak{p}_j}}^i(\kappa(\mathfrak{p}_j),A_{\mathfrak{p}_j})\neq 0\}$$
이므로 $\Ext_{A_{\mathfrak{p}_j}}^{d_j}(\kappa(\mathfrak{p}_j),A_{\mathfrak{p}_j})\neq 0$이다.

이제 $0\leq j<d$를 고정하고 Noetherian local ring $B=A_{\mathfrak{p}_{j+1}}$에 [보조정리 5](#lem5)를 적용한다. $B$의 prime ideal $\mathfrak{q}=\mathfrak{p}_jB$는 $B$의 maximal ideal $\mathfrak{p}_{j+1}B$에 진성으로 포함되며, localization의 합성에 대한 [§정칙성의 호몰로지 판정, ⁋정의 5](/ko/math/commutative_algebra/homological_criterion_for_regularity#def5) 직후의 관찰에 의하여 $B_\mathfrak{q}=(A_{\mathfrak{p}_{j+1}})_{\mathfrak{p}_jA_{\mathfrak{p}_{j+1}}}\cong A_{\mathfrak{p}_j}$이고 그 residue field는 $\kappa(\mathfrak{p}_j)$이다. 따라서
$$\Ext_{B_\mathfrak{q}}^{d_j}(\kappa(\mathfrak{q}),B_\mathfrak{q})\cong\Ext_{A_{\mathfrak{p}_j}}^{d_j}(\kappa(\mathfrak{p}_j),A_{\mathfrak{p}_j})\neq 0$$
이므로 [보조정리 5](#lem5)에 의하여 $d_{j+1}=\operatorname{injdim}_BB\geq d_j+1$이다.

이를 $j=0,\ldots,d-1$에 대하여 종합하면 $d_d\geq d_0+d\geq d$이고, $A_{\mathfrak{p}_d}=A_\mathfrak{m}=A$이므로 $\operatorname{injdim}_AA=d_d\geq d$이다.
:::

## Regular sequence와 Gorenstein

앞 절이 Gorenstein 조건을 depth와 차원에 이었다면, 이 절에서는 non-zerodivisor에 대한 quotient가 이 조건을 정확히 보존한다는 것을 본다. 그 바탕에는 non-zerodivisor로 나눌 때 $\Ext$의 차수가 한 칸 이동한다는 Rees의 change of rings isomorphism이 있다.

::: 보조정리 7
Noetherian local ring $(A,\mathfrak{m})$과 $A$-regular 원소 $x\in\mathfrak{m}$, 그리고 $\overline{A}=A/xA$가 주어졌다 하자. $\overline{A}$-module로 볼 수 있는 (곧 $xN=0$인) $0$이 아닌 finitely generated $A$-module $N$에 대하여, 각 $i\geq 0$에서
$$\Ext_A^{i+1}(N,A)\cong\Ext_{\overline{A}}^i(N,\overline{A})$$
가 성립한다.
:::
::: 증명
먼저 $\Ext_A^\bullet(\overline{A},A)$를 계산한다. $x$가 $A$-regular이므로 [§코쥴 복합체, ⁋따름정리 8](/ko/math/commutative_algebra/koszul_complex#cor8)을 $n=1$에 적용하면 $K(x)=[0\rightarrow A\overset{x}{\rightarrow}A\rightarrow 0]$이 $\overline{A}$의 free resolution이고, $\Hom_A(K(x),A)$가 $A\overset{x}{\rightarrow}A$이므로
$$\Ext_A^0(\overline{A},A)=(0:_Ax)=0,\qquad\Ext_A^1(\overline{A},A)\cong A/xA=\overline{A},\qquad\Ext_A^{\geq 2}(\overline{A},A)=0$$
을 얻는다. 여기서 $\Ext_A^0$이 $0$인 것은 $x$가 $A$-regular이기 때문이다. 또한 $N$이 $\overline{A}$-module이고 $A$가 $x$-torsion을 갖지 않으므로 $\Hom_A(N,A)=0$인데, 임의의 $f:N\rightarrow A$와 $n\in N$에 대하여 $xf(n)=f(xn)=0$이라 $f(n)\in(0:_Ax)=0$이기 때문이다. 같은 이유로 임의의 finitely generated $\overline{A}$-module $N$에 대하여 $\Hom_A(N,A)=0$이다.

이제 주장을 $i$에 대한 귀납법으로 보인다. $\overline{A}$-module 사이의 $A$-linear map은 자동으로 $\overline{A}$-linear이므로 언제나 $\Hom_A(N,\overline{A})=\Hom_{\overline{A}}(N,\overline{A})$이다.

기저 단계 $i=0$을 보자. $\Hom_A(N,-)$을 short exact sequence $0\rightarrow A\overset{x}{\rightarrow}A\rightarrow\overline{A}\rightarrow 0$에 적용한 long exact sequence
$$\Hom_A(N,A)\overset{x}{\longrightarrow}\Hom_A(N,A)\rightarrow\Hom_A(N,\overline{A})\overset{\partial}{\longrightarrow}\Ext_A^1(N,A)\overset{x}{\longrightarrow}\Ext_A^1(N,A)$$
을 생각한다. $xN=0$이므로 곱하기 $x$는 $N$ 위에서 $0$이고, 함자성에 의하여 $\Ext_A^\bullet(N,A)$ 위의 스칼라 곱 $x$ 또한 $0$이다. 그럼 $\Hom_A(N,A)=0$과 종합하여 이 long exact sequence는 $\partial$이 $\Hom_A(N,\overline{A})$과 $\Ext_A^1(N,A)$ 사이의 isomorphism임을 주며, 이는 $N$에 대하여 자연스럽다. 곧
$$\Ext_A^1(N,A)\cong\Hom_A(N,\overline{A})=\Hom_{\overline{A}}(N,\overline{A})$$
이다.

이제 $i\geq 1$이라 하고 주장이 $i-1$에 대하여 모든 finitely generated $\overline{A}$-module에 대해 성립한다고 가정하자. $\overline{A}$가 Noetherian이므로 finitely generated free $\overline{A}$-module $\overline{A}^k$로부터의 surjection과 그 kernel $N'$으로 이루어진 $\overline{A}$-module들의 short exact sequence $0\rightarrow N'\rightarrow\overline{A}^k\rightarrow N\rightarrow 0$을 택한다. 여기에 $\Hom_A(-,A)$의 long exact sequence를 적용하고 앞서 계산한 $\Ext_A^j(\overline{A}^k,A)$의 소멸을 사용하면, $i\geq 2$일 때 $\Ext_A^i(\overline{A}^k,A)=\Ext_A^{i+1}(\overline{A}^k,A)=0$이므로
$$\Ext_A^{i+1}(N,A)\cong\Ext_A^i(N',A)$$
이고, $\Hom_{\overline{A}}(-,\overline{A})$의 long exact sequence에서 $\Ext_{\overline{A}}^{\geq 1}(\overline{A}^k,\overline{A})=0$이므로 $\Ext_{\overline{A}}^i(N,\overline{A})\cong\Ext_{\overline{A}}^{i-1}(N',\overline{A})$이다. 귀납적 가정을 $N'$에 적용하면 $\Ext_A^i(N',A)\cong\Ext_{\overline{A}}^{i-1}(N',\overline{A})$이므로 $i\geq 2$에서 원하는 isomorphism을 얻는다. $i=1$인 경우에는 위의 두 long exact sequence가 각각
$$\overline{A}^k\overset{\varphi}{\longrightarrow}\Ext_A^1(N',A)\rightarrow\Ext_A^2(N,A)\rightarrow 0,\qquad\overline{A}^k\overset{\psi}{\longrightarrow}\Hom_{\overline{A}}(N',\overline{A})\rightarrow\Ext_{\overline{A}}^1(N,\overline{A})\rightarrow 0$$
을 주는데, 기저 단계의 isomorphism $\Ext_A^1(-,A)\cong\Hom_{\overline{A}}(-,\overline{A})$가 자연스러우므로 $\varphi$와 $\psi$가 이 isomorphism 아래에서 대응하고, 따라서 그 cokernel인 $\Ext_A^2(N,A)$와 $\Ext_{\overline{A}}^1(N,\overline{A})$도 isomorphic하다.
:::

이 isomorphism을 residue field에 적용하면 Gorenstein 조건이 non-zerodivisor로 나누는 조작에 대해 정확히 한 차원씩 이동한다는 것이 드러난다.

::: 정리 8
Noetherian local ring $(A,\mathfrak{m})$과 $A$-regular 원소 $x\in\mathfrak{m}$에 대하여, $A$가 Gorenstein인 것과 $A/xA$가 Gorenstein인 것이 동치이며, 이 때
$$\operatorname{injdim}_{A/xA}(A/xA)=\operatorname{injdim}_A(A)-1$$
이 성립한다.
:::
::: 증명
$\overline{A}=A/xA$, $\kappa=A/\mathfrak{m}$으로 두자. $x\in\mathfrak{m}$이므로 $\kappa$는 $\overline{A}$-module이고, [보조정리 7](#lem7)을 $N=\kappa$에 적용하면 각 $j\geq 0$에서 $\Ext_{\overline{A}}^j(\kappa,\overline{A})\cong\Ext_A^{j+1}(\kappa,A)$이다. 한편 $x\in\mathfrak{m}$이 $A$-regular이므로 $\Hom_A(\kappa,A)=(0:_A\mathfrak{m})=0$이고, 곧 $\Ext_A^0(\kappa,A)=0$이다.

[§단사가군과 Matlis 쌍대성, ⁋명제 7](/ko/math/commutative_algebra/matlis_duality#prop7)을 $A$에 적용하면 $\operatorname{injdim}_AA=\sup\{i\mid\Ext_A^i(\kappa,A)\neq 0\}$인데, 방금 본 $\Ext_A^0(\kappa,A)=0$에 의하여 이 supremum은 $i\geq 1$에서 취해진다. 그럼 Rees isomorphism $\Ext_A^{j+1}(\kappa,A)\cong\Ext_{\overline{A}}^j(\kappa,\overline{A})$와 다시 같은 명제를 $\overline{A}$에 적용한 결과로부터
$$\operatorname{injdim}_AA=1+\sup\{j\geq 0\mid\Ext_{\overline{A}}^j(\kappa,\overline{A})\neq 0\}=1+\operatorname{injdim}_{\overline{A}}\overline{A}$$
이다. 이 등식의 양변은 함께 유한하거나 함께 무한하므로 두 Gorenstein 조건이 동치이고, 유한한 경우 $\operatorname{injdim}_{\overline{A}}\overline{A}=\operatorname{injdim}_AA-1$이다.
:::

Regular local ring 자신부터 이 조작의 출발점에 놓이며, 여기에서 Gorenstein ring들의 넓은 위계가 자란다.

::: 따름정리 9
다음이 성립한다.

1. Regular local ring은 Gorenstein이다.
2. Regular local ring $R$와 그 $R$-regular sequence $y_1,\ldots,y_c$에 대하여 $R/(y_1,\ldots,y_c)$는 Gorenstein이다.
:::
::: 증명
첫째 결과의 경우, [§호몰로지 차원, ⁋명제 7](/ko/math/commutative_algebra/homological_dimension#prop7)에 의하여 $\operatorname{injdim}_AA\leq\sup_M\operatorname{injdim}_AM=\operatorname{gldim}A$이고, $A$가 regular local ring이므로 [§호몰로지 차원, ⁋명제 13](/ko/math/commutative_algebra/homological_dimension#prop13)에 의하여 $\operatorname{gldim}A=\dim A<\infty$이다. 따라서 $\operatorname{injdim}_AA<\infty$, 곧 $A$는 Gorenstein이다.

둘째 결과를 $c$에 대한 귀납법으로 보인다. $c=0$이면 $R/(y_1,\ldots,y_c)=R$은 regular local ring이므로 첫째 결과에 의하여 Gorenstein이다. $c\geq 1$이면 $\overline{R}=R/(y_1,\ldots,y_{c-1})$은 귀납적 가정에 의하여 Gorenstein이다. Regular sequence의 원소는 모두 non-unit이므로 $y_c$의 image $\overline{y}_c$는 $\overline{R}$의 maximal ideal에 속하고, regular sequence의 정의에 의하여 $\overline{R}$-regular이므로 ([§정칙국소환, ⁋정의 2](/ko/math/commutative_algebra/regular_local_rings#def2)) [정리 8](#thm8)에 의하여 $R/(y_1,\ldots,y_c)=\overline{R}/\overline{y}_c\overline{R}$도 Gorenstein이다.
:::

둘째 결과에서 다룬, 어떤 regular local ring $R$와 그 $R$-regular sequence $y_1,\ldots,y_c$에 대하여 $R/(y_1,\ldots,y_c)$와 isomorphic한 local ring을 *complete intersection*이라 부른다. [정리 6](#thm6)과 종합하면 local ring의 성질들 사이의 위계
$$\text{regular}\implies\text{complete intersection}\implies\text{Gorenstein}\implies\text{Cohen--Macaulay}$$
를 얻는다. 첫째 함의는 $c=0$인 경우이고 마지막은 [정리 6](#thm6)이다. 이 위계에서 적어도 두 포함이 진성일 수 있다는 것은 [예시 11](#ex11)이 보여주는데, 거기서 $\mathbb{K}[[\x,\y]]/(\x^2,\y^2)$은 regular가 아닌 complete intersection이고 $\mathbb{K}[[t^3,t^4,t^5]]$은 Gorenstein이 아닌 Cohen--Macaulay이다.

## 0차원 특징화와 예시

Artinian local ring $(A,\mathfrak{m},\kappa)$에서는 $\dim A=0$이므로 depth 또한 $0$이고, [정리 1](#thm1)에 의하여 Gorenstein 조건은 $A$가 injective module이라는 것으로 단순해진다. 이 조건을 residue field로 직접 읽어내기 위해, $\mathfrak{m}$에 의해 소멸되는 원소들의 module
$$(0:_A\mathfrak{m})=\{a\in A\mid\mathfrak{m}a=0\}$$
을 $A$의 *socle*이라 부른다. 이는 $\mathfrak{m}$이 자명하게 작용하는 $\kappa$-벡터공간 구조를 갖는 submodule이다.

::: 정리 10
Artinian local ring $(A,\mathfrak{m},\kappa)$에 대하여 다음이 모두 동치이다.

1. $A$는 Gorenstein이다.
2. $A$는 injective $A$-module이다.
3. $\dim_\kappa(0:_A\mathfrak{m})=1$이다.
4. $A\cong E(\kappa)$이다. 여기서 $E(\kappa)$는 $\kappa$의 injective hull이다.
:::
::: 증명
$A$가 Artinian이므로 [§조르단-횔더 정리, ⁋정리 4](/ko/math/commutative_algebra/Jordan-Holder_theorem#thm4)에 의하여 $\dim A=0$이다.

(1)과 (2)의 동치를 보자. $A$가 Gorenstein이면 [정리 1](#thm1)에 의하여 $\operatorname{injdim}_AA=\operatorname{depth}A$인데, [§Depth, ⁋따름정리 8](/ko/math/commutative_algebra/depth#cor8)에 의하여 $\operatorname{depth}A\leq\dim A=0$이므로 $\operatorname{injdim}_AA=0$, 곧 $A$는 injective이다. 거꾸로 $A$가 injective이면 $\operatorname{injdim}_AA=0<\infty$이므로 Gorenstein이다.

(2)가 (4)를 함의함을 보자. $A$가 $0$이 아닌 injective module이므로 [§단사가군과 Matlis 쌍대성, ⁋정리 6](/ko/math/commutative_algebra/matlis_duality#thm6)에 의하여 prime ideal들의 족 $(\mathfrak{p}_\lambda)$에 대하여 $A\cong\bigoplus_\lambda E(A/\mathfrak{p}_\lambda)$이다. $A$가 Artinian local이라 그 유일한 prime ideal은 $\mathfrak{m}$이므로 ([§조르단-횔더 정리, ⁋정리 4](/ko/math/commutative_algebra/Jordan-Holder_theorem#thm4)) 각 $\mathfrak{p}_\lambda=\mathfrak{m}$이고, 따라서 $A\cong E(\kappa)^{\oplus k}$이다. 한편 $A$는 $A$-module로서 indecomposable인데, direct summand로의 분해는 $\Hom_A(A,A)\cong A$의 idempotent에 대응하고 local ring $A$의 idempotent는 $0$과 $1$ 뿐이기 때문이다 ($e^2=e$이면 $e(1-e)=0$이고 $e$와 $1-e$ 중 하나는 unit이므로 $e\in\{0,1\}$이다). 그러므로 $k=1$이고 $A\cong E(\kappa)$이다.

(4)가 (3)을 함의함을 보자. $A\cong E(\kappa)$이면 [§단사가군과 Matlis 쌍대성, ⁋보조정리 8](/ko/math/commutative_algebra/matlis_duality#lem8)에 의하여 $(0:_A\mathfrak{m})=\Hom_A(\kappa,A)\cong\Hom_A(\kappa,E(\kappa))\cong\kappa$이므로 $\dim_\kappa(0:_A\mathfrak{m})=1$이다.

(3)이 (2)를 함의함을 보자. $\dim_\kappa(0:_A\mathfrak{m})=1$이라 하자. $A$의 $0$이 아닌 임의의 submodule $N$은 Artinian이므로 minimal한 $0$이 아닌 submodule, 곧 simple submodule $S$를 포함하며 ([§조르단-횔더 정리, ⁋정의 2](/ko/math/commutative_algebra/Jordan-Holder_theorem#def2)), $S$의 annihilator는 maximal ideal이라 $\mathfrak{m}$이므로 $S\subseteq(0:_A\mathfrak{m})$이다. $(0:_A\mathfrak{m})$이 $1$차원이라 그 안의 simple submodule은 $(0:_A\mathfrak{m})$ 자신뿐이므로 $S=(0:_A\mathfrak{m})$이고, 곧 $A$의 모든 $0$이 아닌 submodule이 $(0:_A\mathfrak{m})$을 포함한다. 이는 $(0:_A\mathfrak{m})\cong\kappa$가 $A$의 essential submodule이라는 뜻이므로 ([§단사가군과 Matlis 쌍대성, ⁋정의 1](/ko/math/commutative_algebra/matlis_duality#def1)), [§단사가군과 Matlis 쌍대성, ⁋정리 3](/ko/math/commutative_algebra/matlis_duality#thm3)의 injective hull 유일성에 의하여 $E(A)\cong E(\kappa)$이다.

이제 길이를 비교한다. $A$가 Artinian이라 유한한 길이를 가지므로 [§단사가군과 Matlis 쌍대성, ⁋명제 9](/ko/math/commutative_algebra/matlis_duality#prop9)를 $M=A$에 적용하면, Matlis dual $\Hom_A(A,E(\kappa))\cong E(\kappa)$가 $\length E(\kappa)=\length A$인 유한한 길이의 module이다. 그럼 essential embedding $A\hookrightarrow E(A)\cong E(\kappa)$의 양변이 같은 유한한 길이를 가지므로 $A=E(\kappa)$이고, 따라서 $A$는 injective이다.
:::

Socle이 $1$차원이라는 조건은 $A$가 유일한 minimal한 $0$이 아닌 submodule을 갖는다는 것이다. Local ring $A$는 언제나 유일한 maximal submodule $\mathfrak{m}$을 가지므로, socle 조건은 이 극대성을 뒤집은 최소성의 형태이며, Matlis dual $D(-)=\Hom_A(-,E(\kappa))$가 유한한 길이 module 위에서 정확히 이 둘을 맞바꾼다. 다음 예시들은 이 판정을 구체적인 local ring에서 적용한다.

::: 예시 11
1. $A=\mathbb{K}[[\x,\y]]/(\x^2,\y^2)$을 생각하자. $\x^2,\y^2$은 $\mathbb{K}[[\x,\y]]$의 regular sequence이다. $\mathbb{K}[[\x,\y]]$가 integral domain이므로 $\x^2$은 non-zerodivisor이고, $\mathbb{K}[[\x,\y]]/(\x^2)$은 $\{1,\x\}$를 basis로 갖는 free $\mathbb{K}[[\y]]$-module이라 곱하기 $\y^2$이 그 위에서 injective이므로 $\y^2$은 $\mathbb{K}[[\x,\y]]/(\x^2)$의 non-zerodivisor이다. 따라서 $A$는 complete intersection이고 [따름정리 9](#cor9)에 의하여 Gorenstein이다. 직접 확인하면 $A$는 $\{1,\x,\y,\x\y\}$를 $\mathbb{K}$-basis로 가지며, $\mathfrak{m}=(\x,\y)$에 의해 소멸되는 원소는 $\x\y$의 배수뿐이므로 $(0:_A\mathfrak{m})=(\x\y)$는 $1$차원이다. 그러나 $\mathfrak{m}/\mathfrak{m}^2$은 $\{\x,\y\}$의 상으로 생성되어 $2$차원인 반면 $\dim A=0$이므로 $A$는 regular local ring이 아니다.

2. $A=\mathbb{K}[[\x,\y]]/(\x^2,\x\y,\y^2)=\mathbb{K}[[\x,\y]]/\mathfrak{m}^2$을 생각하자. 이는 $\{1,\x,\y\}$를 $\mathbb{K}$-basis로 갖는 Artinian local ring이고 $\mathfrak{m}^2=0$이므로, socle $(0:_A\mathfrak{m})$은 $\mathfrak{m}$ 전체, 곧 $\{\x,\y\}$의 상으로 생성되는 $2$차원 벡터공간이다. 따라서 [정리 10](#thm10)에 의하여 $A$는 Gorenstein이 아니다. 그럼에도 $A$는 $0$차원이라 Cohen--Macaulay이므로 ([§Cohen-Macaulay 환, ⁋예시 7](/ko/math/commutative_algebra/cohen_macaulay_rings#ex7)의 셋째 판정), 이는 Gorenstein이 Cohen--Macaulay보다 진성으로 강한 조건임을 보여준다.

3. $\mathbb{K}[[t]]$의 subring $A_1=\mathbb{K}[[t^3,t^4]]$와 $A_2=\mathbb{K}[[t^3,t^4,t^5]]$을 생각하자. 두 ring 모두 $1$차원 Noetherian local domain이다. $t^3$이 domain의 $0$이 아닌 원소라 $A_i$-regular이고, 아래에서 보듯 $A_i/(t^3)$이 유한한 $\mathbb{K}$-차원을 가지므로 $(t^3)$은 $\mathfrak{m}$-primary, 곧 $\dim A_i=1$이다. Domain이라 $\operatorname{depth}A_i\geq 1$이므로 [§Cohen-Macaulay 환, ⁋예시 7](/ko/math/commutative_algebra/cohen_macaulay_rings#ex7)의 넷째 판정에 의하여 $A_i$는 Cohen--Macaulay이다. [정리 8](#thm8)에 의하여 $A_i$가 Gorenstein인 것은 Artinian local ring $A_i/(t^3)$이 Gorenstein인 것과 동치이므로, 후자에 [정리 10](#thm10)의 socle 판정을 적용한다.

  $A_1$은 semigroup $\langle 3,4\rangle=\{0,3,4,6,7,8,\ldots\}$의 원소 $s$에 대한 $t^s$들을 $\mathbb{K}$-basis로 가지며, $t^3A_1=\{t^{3+s}\mid s\in\langle 3,4\rangle\}$을 법으로 하면 $\langle 3,4\rangle$에서 $3+\langle 3,4\rangle$을 뺀 나머지가 $\{0,4,8\}$이므로 $A_1/(t^3)$은 $\{1,t^4,t^8\}$을 basis로 갖는다. 그 maximal ideal은 $t^3=0$이라 $t^4$의 상으로 생성되고, $t^4\cdot t^4=t^8\neq 0$이지만 $t^4\cdot t^8=t^{12}=0$이므로 socle은 $t^8$의 상으로 이루어진 $1$차원이다. 따라서 $A_1/(t^3)$은 Gorenstein이고 $A_1$도 Gorenstein이다.

  $A_2$는 semigroup $\langle 3,4,5\rangle=\{0,3,4,5,6,\ldots\}$로부터 같은 방식으로 $A_2/(t^3)=\{1,t^4,t^5\}$을 얻는다. 이번에는 $t^4\cdot t^4=t^8=t^3t^5\in(t^3)$이라 $0$이고 마찬가지로 $t^4\cdot t^5=t^9=0$, $t^5\cdot t^5=t^{10}=0$이므로 $t^4$과 $t^5$의 상이 모두 maximal ideal에 의해 소멸된다. 곧 socle은 $2$차원이고, [정리 10](#thm10)에 의하여 $A_2/(t^3)$은 Gorenstein이 아니므로 $A_2$도 Gorenstein이 아니다. 두 monomial curve $A_1$과 $A_2$는 모두 $1$차원 Cohen--Macaulay local domain이면서 Gorenstein 여부에서 갈린다.
:::

Local ring의 depth와 차원, 그리고 이 글의 duality를 하나의 언어로 엮는 local cohomology가 이 여정의 다음 장을 이룬다.

---

**참고문헌**

**[BH]** W. Bruns, J. Herzog. *Cohen-Macaulay Rings*. Cambridge University Press, 1993.

**[Eis]** David Eisenbud. *Commutative Algebra: with a view toward algebraic geometry*. Springer, 1995.

**[Mat]** Hideyuki Matsumura. *Commutative Ring Theory*. Cambridge University Press, 1986.

**[Stacks]** The Stacks Project Authors. *The Stacks Project*. [https://stacks.math.columbia.edu](https://stacks.math.columbia.edu).

---
