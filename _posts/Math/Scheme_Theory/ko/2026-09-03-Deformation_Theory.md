---
title: "변형이론과 여접 복합체"
description: "Square-zero 확대를 따른 변형과 obstruction을 통해 Kähler differential만으로는 부족한 이유를 밝히고, naive 여접 복합체와 완전한 여접 복합체가 affine algebra의 변형을 어떻게 재는지 계산한 뒤 스킴의 국소 변형과 접합 자료를 local-to-global spectral sequence로 조립한다."
excerpt: "Square-zero extensions, first-order deformations T^1, obstructions T^2, and why Ω is not enough"

categories: [Math / Scheme Theory]
permalink: /ko/math/scheme_theory/deformation_theory
sidebar:
  nav: "scheme_theory-ko"

date: 2026-09-03

weight: 22
published: false
---

## 소박한 여접 복합체

[§매끄러운 사상과 에탈 사상, ⁋정리 15](/ko/math/scheme_theory/smooth_and_etale_morphisms#thm15)에 따르면, locally of finite presentation인 morphism of schemes $\varphi:X\rightarrow S$가 smooth한 것은 임의의 affine $S$-scheme $T=\Spec R$와, square-zero subscheme $T_0=\Spec R_0$마다, 임의의 $S$-morphism $\varrho_0:T_0\rightarrow X$를 $T$로 연장하는 lifting $\varrho:T\rightarrow X$가 항상 존재하는 것과 동치이다. 여기서 $T_0$이 $T$의 *square-zero subscheme*이라는 것은, $T_0\hookrightarrow T$가 square-zero ideal sheaf $\mathcal{I}\subseteq\mathcal{O}_T$로 정의된다는 의미이며, 이를 affine space에서의 세팅 

$$S=\Spec A,\qquad X=\Spec C,\qquad\text{$C$ an $A$-algebra locally of finite presentation}$$

에서 보면, closed embedding $T_0\hookrightarrow T$는 square-zero ideal $\mathfrak{b}\subseteq R$에 의한 square-zero extension

$$0\longrightarrow\mathfrak{b}\longrightarrow R\overset{q}{\longrightarrow} R_0\longrightarrow0\tag{$\ast$}$$

에 대응하며, $S$-morphism $\varrho_0$는 $A$-algebra homomorphism $\rho_0:C\rightarrow R_0$에 대응한다. 즉, 이와 같은 상황에서 $\phi: A\rightarrow C$의 smoothness는 임의의 square-zero extension ($\ast$)와, 임의의 $\rho_0: C\rightarrow R_0$가 주어질 때마다, 그 lifting $\rho: C\rightarrow R$이 항상 존재하는 것과 동치였다. 
 
이제 $C$가 locally of finite presentation인 $A$-algebra이므로, 적당한 polynomial algebra $B=A[\x_1,\ldots,\x_n]$와 $B$의 finitely generated ideal $\mathfrak{a}$가 존재하여 $C=B/\mathfrak{a}$라 할 수 있다. 자연스러운 projection $\pi:B\twoheadrightarrow C$와 $\rho_0$의 합성

$$\overline{\rho}_0:B\longrightarrow C\overset{\rho_0}{\longrightarrow}R_0$$

을 생각하자. 그럼 $q$가 surjective이므로 각각의 변수 $\x_i$마다 $q(r_i)=\overline{\rho}_0(\x_i)$을 만족하는 $r_i\in R$들을 택할 수 있으며, [\[대수적 구조\] §대수, ⁋명제 8](/ko/math/algebraic_structures/algebras#prop8)에 의하여 대응 $\x_i\mapsto r_i$는 $A$-algebra homomorphism $\widetilde{\rho}: B\rightarrow R$을 유일하게 정의한다. 이는 $q\circ \widetilde{\rho}=\overline{\rho}_0$을 만족하며, 이 때 각 $r_i$의 선택에는 $\ker q=\mathfrak{b}$만큼의 자유도가 존재한다. 

우리가 본래 찾고자 하는 것은 $C$로부터의 lifting $\rho:C\rightarrow R$이다. 만약 택한 $\widetilde{\rho}$가 $\widetilde{\rho}(\mathfrak{a})=0$을 만족한다면, $\widetilde{\rho}$는 곧바로 $C=B/\mathfrak{a}$를 거쳐 원하는 lifting $\rho$를 유도할 것이지만, 그것만이 전부는 아니다. 위에서 살펴본 것과 같이 $\widetilde{\rho}$의 정의는 각 변수의 lift만큼의 차이가 있으므로, 다른 $\widetilde{\rho}$의 선택이 $\widetilde{\rho}(\mathfrak{a})=0$을 줄 수도 있기 때문이다. 따라서 이 lifting의 실패를 확인하기 위해서는 $\widetilde{\rho}$의 선택에 의존하지 않는 양을 계산해야 한다.

이를 위해 우선 고정된 $\widetilde{\rho}$에 대하여 $\widetilde{\rho}(\mathfrak{a})=0$이라는 것이 무엇을 의미하는지를 다시 써 보자. 우선 임의의 $f\in \mathfrak{a}$에 대하여

$$q(\widetilde{\rho}(f))=\overline{\rho}_0(f)=\rho_0(\pi(f))=\rho_0(0)=0$$

이므로, 포함관계 $\widetilde{\rho}(\mathfrak{a})\subset \ker q=\mathfrak{b}$는 자명하다. 뿐만 아니라, 임의의 $f,g\in \mathfrak{a}$에 대하여

$$\widetilde{\rho}(fg)=\widetilde{\rho}(f)\widetilde{\rho}(g)\in\mathfrak{b}^2=0$$

이므로 다음의 식

$$\delta: \mathfrak{a}/\mathfrak{a}^2\rightarrow \mathfrak{b};\qquad \bar{f}\mapsto \widetilde{\rho}(f)$$

이 잘 정의된다. 뿐만 아니라, 이렇게 얻어진 $\delta$는 $C$-linear map이 된다. 여기서 $\mathfrak{a}/\mathfrak{a}^2$는 $\mathfrak{a}$를 $B$-module로 봤을 때, $B$의 ideal $\mathfrak{a}$가 이 위에 $0$으로 작용하므로 $C=B/\mathfrak{a}$-module structure가 주어진 것이고, $\mathfrak{b}$의 경우 $\mathfrak{b}^2=0$인 것으로부터 $\mathfrak{b}$의 $R$-module structure가 $R_0=R/\mathfrak{b}$-module structure를 주고, 이를 $\rho_0$를 따라 $C$-module로 본 것이다. 즉, 고정된 $\widetilde{\rho}$에 대하여 $\widetilde{\rho}(\mathfrak{a})=0$인 것은 정확히 이런 방식으로 정의한 $C$-linear map $\delta\in\Hom_C(\mathfrak{a}/\mathfrak{a}^2, \mathfrak{b})$가 $0$이 되는 것과 같다. 

이를 바탕으로 우리는 $\widetilde{\rho}$의 선택을 바꿀 때의 변화량을 정량화할 수 있다. $\widetilde{\rho}$와 $\widetilde{\rho}'$이 $\overline{\rho}_0$의 두 lift라 하자. 그럼 등식 $q\circ\widetilde{\rho}=q\circ\widetilde{\rho}'$으로부터 그 차 $D=\widetilde{\rho}'-\widetilde{\rho}$는 $B$에서 $\ker q=\mathfrak{b}$로의 $A$-linear map이다. 그런데

$$D(fg)=\widetilde{\rho}'(f)\widetilde{\rho}'(g)-\widetilde{\rho}(f)\widetilde{\rho}(g)=\left(\widetilde{\rho}(f)+D(f)\right)\left(\widetilde{\rho}(g)+D(g)\right)-\widetilde{\rho}(f)\widetilde{\rho}(g)=\widetilde{\rho}(f)D(g)+D(f)\widetilde{\rho}(g)+D(f)D(g)$$

이고, $D(f),D(g)\in\mathfrak{b}$이며 $\mathfrak{b}^2=0$이므로 마지막 항 $D(f)D(g)$은 사라진다. 한편, $\mathfrak{b}$ 위의 $R$-module 구조는 $q: R\rightarrow R_0$을 통해 이루어진 것으로

$$\widetilde{\rho}(f)D(g)=q(\widetilde{\rho}(f))\cdot D(g)=\overline{\rho}_0(f)\cdot D(g)$$

이 성립하고, 따라서 위의 식에서 남은 두 항은 $\mathfrak{b}$를 $\overline{\rho}_0$를 따라 $B$-module로 볼 때의 action $f\cdot D(g)$와 $D(f)\cdot g$로 쓸 수 있다. 즉, $D$는 Leibniz rule

$$D(fg)=f\cdot D(g)+g\cdot D(f)$$

을 만족하고 따라서 $A$-derivation이다. 거꾸로 임의의 $D\in \Der_A(B, \mathfrak{b})$에 대하여, $\widetilde{\rho}+D$ 역시 $A$-algebra homomorphism이고 $q\circ(\widetilde{\rho}+D)=\overline{\rho}_0$을 만족하므로, $\overline{\rho}_0$의 lift를 고르는 자유도가 정확히 $\Der_A(B,\mathfrak{b})=\Hom_C(\Omega_{B/A}\otimes_BC,\mathfrak{b})$에 담기게 된다.

위의 $D=\widetilde{\rho}'-\widetilde{\rho}\in\Der_A(B,\mathfrak{b})$에 대응되는 $C$-linear map을 $h:\Omega_{B/A}\otimes_BC\rightarrow\mathfrak{b}$라 하면, 임의의 $f\in\mathfrak{a}$에 대하여

$$\delta'(\bar{f})-\delta(\bar{f})=D(f)=h(\dd{f}\otimes1)=h(\bar{d}(\bar{f}))$$

로 주어진다. 여기서 $\bar{d}: \mathfrak{a}/\mathfrak{a}^2\rightarrow\Omega_{B/A}\otimes_BC$는 [§미분과 여접층, ⁋명제 2](/ko/math/scheme_theory/sheaf_of_differentials#prop2)의 conormal morphism이고 $\delta'-\delta$는 $\bar{d}^\ast$의 image에 속한다는 것을 알 수 있다. 더 중요하게, 어떤 선택이 존재하여 $\mathfrak{a}$를 죽일 수 있는 것은 이제 적당한 $h:\Omega_{B/A}\otimes_BC\rightarrow \mathfrak{b}$가 존재하여 $\delta+\bar{d}^\ast(h)=0$인 것, 즉 $\delta$가 $\bar{d}^\ast$의 image에 속한다는 것과 동일하다. 즉, 이를 확인하기 위해서는 $\delta$를 다음의 class

$$[\delta]\in\coker\left(\Hom_C(\Omega_{B/A}\otimes_BC,\mathfrak{b})\overset{\bar{d}^{\ast}}{\longrightarrow}\Hom_C(\mathfrak{a}/\mathfrak{a}^2,\mathfrak{b})\right)$$

에서 살펴보면 되고, 이는 서로 다른 lift의 차이 $\delta'-\delta=\bar{d}^\ast(h)$가 $\im\bar{d}^\ast$에 속하므로 $\widetilde{\rho}$의 선택에 의존하지 않는다. 

더 일반적으로, 이는 다음의 complex

$$\NL_{C/A}=\left[\mathfrak{a}/\mathfrak{a}^2\overset{\bar{d}}{\longrightarrow}\Omega_{B/A}\otimes_BC\right]$$

를 $\mathfrak{b}$로 dualize하여 얻는 complex $\Hom_C(\NL_{C/A}, \mathfrak{b})$의 첫째 cohomology이며, 따라서 이 $\mathfrak{b}$를 kernel로 가지는 square-zero extension ($\ast$)에 대한 lifting problem을 재는 obstruction space가 $H^1(\Hom_C(\NL_{C/A}, \mathfrak{b}))$이고, 만일 이것이 임의의 $\mathfrak{b}$에 대해 $0$이 된다면 $A\rightarrow C$가 smooth이게 된다. 이 형식화를 바탕으로 [§매끄러운 사상과 에탈 사상, ⁋정리 15](/ko/math/scheme_theory/smooth_and_etale_morphisms#thm15)의 증명을 다시 보면, 해당 증명에서 한 것은 conormal sequence가 split exact임을 보여 naive cotangent complex 단계에서 이를 해결해버린 것이다. 

지금까지 등장한 대상들에 이름을 붙이면 다음과 같다.

::: 정의 1
$A$-algebra $C$와, $A$ 위의 polynomial algebra $B$에 의한 presentation $C=B/\mathfrak{a}$에 대하여, 위의 complex

$$\NL_{C/A}=\Bigl[\at{1}{\mathfrak{a}/\mathfrak{a}^2}\overset{\bar{d}}{\longrightarrow}\at{0}{\Omega_{B/A}\otimes_BC}\Bigr]$$

를 $C$의 *naive cotangent complex<sub>소박한 여접 복합체</sub>*라 부르고, 그 homology를 각각

$$H_1(\NL_{C/A})=\ker\bar{d},\qquad H_0(\NL_{C/A})=\coker\bar{d}$$

라 적는다. 또 $C$-module $M$에 대하여, 이를 $M$으로 dualize한 cochain complex

$$\Hom_C(\NL_{C/A},M):\quad \at{0}{\Hom_C(\Omega_{B/A}\otimes_BC,M)}\overset{\bar{d}^\ast}{\rightarrow}\at{1}{\Hom_C(\mathfrak{a}/\mathfrak{a}^2,M)}$$

의 cohomology를

$$T^0(C/A,M)=\ker\bar{d}^\ast,\qquad T^1(C/A,M)=\coker\bar{d}^\ast$$

라 적는다.
:::

이 대상들은 우리가 이미 알고 있는 것들이다. 우선 [§미분과 여접층, ⁋명제 2](/ko/math/scheme_theory/sheaf_of_differentials#prop2)의 conormal exact sequence를 degree $0$에서 읽으면

$$H_0(\NL_{C/A})\cong\Omega_{C/A}$$

를 얻는다. 또, 이 때 $H_0$과 $H_1$은 presentation $C=B/\mathfrak{a}$의 선택에 의존하지 않는다. $T^0$의 경우, degree $0$ cocycle은 $\mathfrak{a}$를 소멸시켜 $C=B/\mathfrak{a}$ 위로 내려오는 derivation $B\rightarrow M$이므로 곧바로 $T^0(C/A,M)\cong\Der_A(C,M)\cong\Hom_C(\Omega_{C/A},M)$이다. 마지막으로 $T^1$은 정의에 의하여 $[\delta]$가 놓인 cokernel이므로, 앞에서 얻은 obstruction space에서 $\mathfrak{b}$만 $M$으로 바꾼 것이다.  

## 소박한 여접 복합체와 매끄러움

[§매끄러운 사상과 에탈 사상, ⁋명제 8](/ko/math/scheme_theory/smooth_and_etale_morphisms#prop8)에서 smoothness는 conormal sequence의 splitting으로 나타났고, 이 글의 도입부에서는 lifting의 obstruction이 $T^1$에 놓인다는 것을 보았다. 이 두 설명은 다음과 같이 연결된다.

::: 명제 2
Finitely presented $A$-algebra $C$가 $A$ 위에서 smooth한 것은

$$H_1(\NL_{C/A})=0,\qquad \Omega_{C/A}\text{ is a finitely generated projective }C\text{-module}$$

인 것과 동치이다. 또한 이는 모든 $C$-module $M$에 대하여 $T^1(C/A,M)=0$인 것과 동치이다.
:::
::: 증명
$C$가 smooth하면 [§매끄러운 사상과 에탈 사상, ⁋명제 8](/ko/math/scheme_theory/smooth_and_etale_morphisms#prop8)에 의하여 conormal sequence

$$0\longrightarrow\mathfrak{a}/\mathfrak{a}^2\overset{\bar{d}}{\longrightarrow}\Omega_{B/A}\otimes_BC\longrightarrow\Omega_{C/A}\longrightarrow0$$

는 split short exact sequence이다. 따라서 $H_1(\NL_{C/A})=\ker\bar{d}=0$이고, $\Omega_{C/A}$는 finitely generated free module $\Omega_{B/A}\otimes_BC$의 direct summand이므로 finitely generated projective이다.

이제 $H_1(\NL_{C/A})=0$이고 $\Omega_{C/A}$가 projective라 하자. Presentation $C=B/\mathfrak{a}$에 대한 conormal sequence

$$\mathfrak{a}/\mathfrak{a}^2\overset{\bar{d}}{\longrightarrow}\Omega_{B/A}\otimes_BC\longrightarrow\Omega_{C/A}\longrightarrow0$$

는 항상 right exact이며 ([§미분과 여접층, ⁋명제 2](/ko/math/scheme_theory/sheaf_of_differentials#prop2)) 여기에 조건 $H_1(\NL_{C/A})=\ker\bar{d}=0$이 주어졌으므로 왼쪽에 $0$을 붙여 short exact sequence를 얻을 수 있다. 또, $\Omega_{C/A}$가 projective이므로 surjection $\Omega_{B/A}\otimes_BC\rightarrow\Omega_{C/A}$가 split한다. ([\[다중선형대수학\] §사영가군, 단사가군, 평탄가군, ⁋명제 4](/ko/math/multilinear_algebra/various_modules#prop4)) 따라서 [§매끄러운 사상과 에탈 사상, ⁋명제 8](/ko/math/scheme_theory/smooth_and_etale_morphisms#prop8)에 의하여 $C$는 $A$ 위에서 smooth하다.

마지막으로 smoothness와 모든 $C$-module $M$에 대한 $T^1(C/A,M)=0$인 것이 동치임을 보인다. 우선 $C$가 smooth라면 위에서 얻은 splitting에 의하여 $r\circ\bar{d}=\id$인 retraction $r:\Omega_{B/A}\otimes_BC\rightarrow\mathfrak{a}/\mathfrak{a}^2$가 존재한다. 이제 임의의 $C$-module $M$과 $\delta:\mathfrak{a}/\mathfrak{a}^2\rightarrow M$에 대하여 $h=\delta\circ r$로 두면 $h\circ\bar{d}=\delta$이므로 $\bar{d}^\ast$가 surjective이고 $T^1(C/A,M)=0$이다. 거꾸로 모든 $M$에 대하여 $T^1(C/A,M)=0$이라 하자. 그럼 도입부의 임의의 lifting problem에서 $[\delta]\in T^1(C/A,\mathfrak{b})$가 $0$이므로 lifting이 존재한다. $C$가 finitely presented이므로 [§매끄러운 사상과 에탈 사상, ⁋정리 15](/ko/math/scheme_theory/smooth_and_etale_morphisms#thm15)에 의하여 $C$는 $A$ 위에서 smooth하다.
:::

특히 $C$가 smooth라면, 위의 증명에서 얻은 splitting에 의하여 naive cotangent complex의 splitting

$$\NL_{C/A}\cong \Bigl[\at{1}{\mathfrak{a}/\mathfrak{a}^2}\overset{\id}{\longrightarrow}\at{0}{\mathfrak{a}/\mathfrak{a}^2}\Bigr]\oplus\Bigl[\at{1}{0}\longrightarrow\at{0}{\Omega_{C/A}}\Bigr]$$

이 존재한다. 즉, 둘째 summand로의 projection을 $p$라 하면 short exact sequence

$$0\longrightarrow\ker p\longrightarrow\NL_{C/A}\overset{p}{\longrightarrow}[0\longrightarrow\Omega_{C/A}]\longrightarrow0$$

가 존재하며, 이 때

$$\ker p\cong\Bigl[\mathfrak{a}/\mathfrak{a}^2\overset{\id}{\longrightarrow}\mathfrak{a}/\mathfrak{a}^2\Bigr]$$

이므로 모든 $n$에 대하여 $H_n(\ker p)=0$이다. 위의 short exact sequence에 [\[호몰로지 대수학\] §긴 완전열, ⁋정리 1](/ko/math/homological_algebra/long_exact_sequence#thm1)을 적용하면 모든 degree에서 $H_n(p)$가 isomorphism이 되어, $p$는 $\NL_{C/A}$에서 degree $0$의 projective module $\Omega_{C/A}$로의 quasi-isomorphism이 된다. 즉, 이 경우에는 $\Omega_{C/A}$만 보아도 lifting들의 차이 $T^0(C/A,M)=\Hom_C(\Omega_{C/A},M)$를 계산할 수 있고, lifting의 존재를 가로막는 obstruction space $T^1$은 항상 사라진다.

그러나 일반적인 $C$에 대해서는 conormal morphism의 kernel과 그 image가 direct summand인지 여부부터 살펴보아야 한다. $\Omega_{C/A}$는 이 morphism의 cokernel이므로, 이 두 조건을 직접 다루려면 그 앞의 항과 morphism까지 남긴 $\NL_{C/A}$가 본격적으로 필요하게 된다. 이 상황을 대표하는 것이 lci의 경우이다. ([§완전교차, ⁋정의 1](/ko/math/scheme_theory/complete_intersections#def1)) 일반적인 non-lci 상황에서는 비슷한 계산을 수행하기 위해 cotangent complex 전체를 살펴보아야 할 수 있지만, lci에서는 naive cotangent complex가 cotangent complex 전체와 quasi-isomorphic하다. 이러한 관점에서 lci는 필요한 cotangent data를 naive cotangent complex에서 직접 읽을 수 있는 대표적인 경우로 생각할 수 있다.

구체적인 상황을 보기 위하여 $B=A[\x_1,\ldots,\x_n]$, $C=B/\mathfrak{a}$로 놓고, $\mathfrak{a}=(f_1,\ldots,f_r)$가 $B$-regular sequence로 생성된다고 하자. 각 $f_j$의 class를 보내는 $C$-linear morphism

$$C^r\longrightarrow\mathfrak{a}/\mathfrak{a}^2,\qquad e_j\longmapsto\bar{f}_j$$

은 [§완전교차, ⁋명제 5](/ko/math/scheme_theory/complete_intersections#prop5)와 그 증명에 의하여 isomorphism이므로, 이 경우 naive cotangent complex는 Jacobian에 의해

$$\NL_{C/A}\cong\left[C^r\overset{\bar{d}}{\longrightarrow}C^n\right],\qquad\bar{d}(e_j)=\sum_i\overline{\frac{\partial f_j}{\partial\x_i}}\dd{\x_i}$$

로 주어지며 두 항은 모두 finitely generated free (따라서 finitely generated projective) $C$-module이다. 일반적인 lci 상황에서는 이들 두 free module 사이의 morphism이 남지만, 위에서 살펴본 smooth 상황에서는 여기에 $\bar{d}$가 split injection이라는 조건이 더해져 complex가 degree $0$의 projective module 하나로 줄어드는 것이다. 

## 일차 변형이론

앞에서 우리는 naive cotangent complex가 smoothness의 infinitesimal lifting property를 어떻게 기록하는지 살펴보았다. 이 complex는 deformation theory에서도 중심적인 역할을 한다. 

Deformation theory의 기하학적 출발점은 $A$-scheme $X_0$를 고정하고, section $\t_0:\Spec A\rightarrow T$을 갖춘 pointed $A$-scheme $(T,\t_0)$ 위의 family $\pi:X\rightarrow T$와 central fiber의 identification $X\times_T\Spec A\cong X_0$를 찾는 것이다. [§스킴 사이의 사상, ⁋예시 10](/ko/math/scheme_theory/morphism_of_schemes#ex10)에서와 같이 scheme morphism $\pi:X\rightarrow T$를 $T$로 매개화된 family로 보면, 이는 $T$ 위에서 변하는 scheme들 가운데 section $\t_0$을 따라 얻는 fiber가 $X_0$으로 주어지는 family를 보는 것이다. 이러한 관점을 위해 $\pi$가 flat일 것을 요구하는 것이 합리적이며 ([§평탄사상](/ko/math/scheme_theory/flat_morphisms)) 이러한 가정 아래 이는 fiber들을 하나의 대상 $X_0$가 변해 가는 모습으로 보고 비교하는 것이다.

가장 단순한 예시로 두 직선이 원점에서 만나는 node $X_0=\Spec\bigl(A[\x,\y]/(\x\y)\bigr)$를 생각하자. 이를 deform하는 가장 간단한 방법은 방정식 $\x\y=0$을 $\x\y=\t$로 바꾸어 다음의 family

$$\pi:X=\Spec\bigl(A[\t,\x,\y]/(\x\y-\t)\bigr)\longrightarrow\Spec A[\t]$$

를 생각하는 것이다. 이는 $\t=0$에서 $X_0$를 fiber로 갖고, $\t$를 invert한 open set 위에서는 $\x$와 $\y$가 모두 invertible이 되어 smooth한 family를 이루며, [§평탄사상, ⁋명제 5](/ko/math/scheme_theory/flat_morphisms#prop5)을 통해 $\pi$의 flatness 또한 확인할 수 있다. 즉 이 family를 보면 $X_0$의 원점에 있던 singularity가 parameter $\t$를 따라 어떻게 사라지는지를 살펴볼 수 있다.

일반적인 scheme $X_0$의 deformation을 찾는 첫 단계는 base의 central section $\t_0$에서 infinitesimal direction들을 하나씩 살펴보는 것이다. $A[\epsilon]=A[\t]/(\t^2)$로 놓으면, $(T,\t_0)$의 $A$-상대 tangent direction은 $\t=0$에서 $\t_0$로 제한되는 $A$-morphism $\Spec A[\epsilon]\rightarrow T$으로 표현된다 ([§매끄러운 사상과 에탈 사상, §§Infinitesimal lifting criterion](/ko/math/scheme_theory/smooth_and_etale_morphisms#infinitesimal-lifting-criterion)). 이를 따라 $\pi:X\rightarrow T$를 pullback하면 $\Spec A[\epsilon]$ 위의 family를 얻으며, 직관적으로 이는 그 tangent direction을 따라 $X_0$이 일차까지 변하는 모습을 기록한다.

그러나 실제로는 이 parameter scheme $T$와 그 위의 family $\pi:X\rightarrow T$ 자체가 미리 주어져 있지 않으며, 이를 찾아내는 것부터가 문제의 시작이다. 우리에게 처음 주어진 것은 $X_0$가 $S$-scheme인 것으로부터 주어지는 structure morphism $X_0\rightarrow S$ 뿐이며, 이를 위해 우리가 택하는 전략은 base $S$를 <em-ko>가능한 모든 방향</em-ko>으로 넓혀서 parameter scheme을 정의하는 것이다. 이때 base를 infinitesimal thickening해 나가는 과정이 바로 square-zero extension들이며, 우리는 parameter space와 동시에, 이 과정으로 두꺼워진 base $S$ 위에 놓인 fiber까지 함께 정의한다. 

::: 정의 3
Flat $A$-algebra $C$와, $A$의 임의의 square-zero extension

$$0\longrightarrow \mathfrak{b}\longrightarrow A'\longrightarrow A\longrightarrow0$$

에 대하여, 다음을 정의한다. 

1. $C$의 $A'$ 위로의 *deformation<sub>변형</sub>*이란, 다음 두 조건을 만족하는 pair $(C',\iota)$를 뜻한다.
   - $C'$은 $A'$ 위에서 flat한 $A'$-algebra이다.
   - $\iota:C'\otimes_{A'}A\xrightarrow{\sim} C$는 $A$-algebra isomorphism이다.

   {% diagram Math/Scheme_Theory/Deformation_Theory-1.svg width="5.60em" alt="deformation of algebra" %}

2. 두 deformation $(C',\iota)$와 $(C'',\iota')$이 *isomorphic*이라는 것은, 등식 $\iota'\circ(\psi\otimes\id_A)=\iota$를 만족하는 $A'$-algebra isomorphism $\psi:C'\rightarrow C''$이 존재하는 것이다.

   {% diagram Math/Scheme_Theory/Deformation_Theory-2.svg width="10.55em" alt="isomorphism of deformations" %}

특히 $A'=A[\epsilon]=A[\t]/(\t^2)$인 경우의 deformation을 $C$의 $A$ 위 *first-order deformation<sub>일차 변형</sub>*이라 부른다.
:::

일반적으로, 임의의 square-zero extension 

$$0\rightarrow \mathfrak{b}\rightarrow A'\rightarrow A\rightarrow0$$

과 $A$-algebra $C$의 deformation $(C',\iota)$가 주어졌다면, 여기에 $-\otimes_{A'}C'$를 취한 것이 exact sequence

$$0\longrightarrow \mathfrak{b}\otimes_A C\longrightarrow C'\overset{\iota}{\longrightarrow} C\longrightarrow0$$

을 준다. 여기서 $\mathfrak{b}\otimes_{A'} C'\cong \mathfrak{b}\otimes_A(A\otimes_{A'} C')\cong \mathfrak{b}\otimes_A C$이고, $\mathfrak{b}^2=0$이므로 $\mathfrak{b}\otimes_A C$는 $C'$의 square-zero ideal이고, 따라서 이 exact sequence는 $C$의 square-zero extension이다. 

더 일반적으로, 우리는 이 분류 문제를 임의의 $A$-algebra $C$와 $C$-module $M$에 대하여 다룰 수 있다. 다음 (square-zero) extension들

$$0\longrightarrow M\longrightarrow E\overset{p}{\longrightarrow} C\longrightarrow0$$

을 생각하면, 이들은 다음 commutative diagram

{% diagram Math/Scheme_Theory/Deformation_Theory-3.svg width="18.74em" alt="morphism of extensions" %}

을 morphism으로 갖는 category $\Ext_{\Alg{A}}(C,M)$을 이루며, 이때 이들 morphism들은 [\[호몰로지 대수학\] §Diagram chasing, ⁋따름정리 3](/ko/math/homological_algebra/diagram_chasing#cor3)에 의해 모두 isomorphism이다. 즉 이 category는 groupoid이고, 그 대상들 사이에 morphism이 존재하는지에 따라 square-zero extension의 isomorphism class들이 나뉜다. 실제로, 위의 category의 임의의 데이터

$$0\longrightarrow M\longrightarrow E\overset{p}{\longrightarrow} C\longrightarrow0$$

가 주어졌다 하고 $C$를 polynomial ring $B$에 의한 presentation $B/\mathfrak{a}$로 나타내어 lift $B\rightarrow E$를 택한다면 [정의 1](#def1) 직전의 lifting 계산과 정확히 같은 원리로 class $[\delta_E]\in T^1(C/A,M)$이 대응되며, 이는 우리가 택한 lift $B\rightarrow E$에 의존하지 않으므로 잘 정의된다.

뿐만 아니라 이 대응은 반대방향으로도 작동한다. 구체적으로, class $[\delta]\in T^1(C/A,M)$의 representative인 $C$-linear map $\delta:\mathfrak{a}/\mathfrak{a}^2\rightarrow M$이 주어졌을 때, trivial extension $B\oplus M$ 안에 ideal

$$\mathfrak{a}_\delta=\{(f,-\delta(\bar{f}))\in B\oplus M\mid f\in\mathfrak{a}\}$$

를 정의하면, quotient algebra $E_\delta=(B\oplus M)/\mathfrak{a}_\delta$는 자연스러운 morphism $m\mapsto\overline{(0,m)}$과 $\overline{(b,m)}\mapsto b+\mathfrak{a}$를 통해 $C$의 $M$에 의한 square-zero extension을 정의한다. 이 구성은 representative $\delta$의 선택에 무관하게 isomorphism class를 결정하며, 앞선 대응의 역을 준다는 것을 확인할 수 있다. 즉, 위의 대응은 $C$의 $M$에 의한 square-zero extension들의 isomorphism class들의 모임 $\pi_0(\Ext_{\Alg{A}}(C,M))$과 $T^1(C/A,M)$ 사이의 일대일 대응이며, 이 대응 하에서 split extension은 $0$에 대응한다. 즉, $T^1(C/A,M)$은 $C$의 $M$에 의한 square-zero extension들을 분류하는 공간이다.

이 관점에서 도입부의 lifting problem을 다시 바라보면, 우리는 우선 주어진 자료 $q:R\rightarrow R_0$와 $\rho_0:C\rightarrow R_0$의 pullback을 통해 다음의 extension

$$E=R\times_{R_0}C=\{(r,c)\in R\times C\mid q(r)=\rho_0(c)\}$$

을 정의할 수 있고, 이는 projection $p:E\rightarrow C$를 통해 $C$의 $\mathfrak{b}$에 의한 square-zero extension

$$0\longrightarrow\mathfrak{b}\longrightarrow E\overset{p}{\longrightarrow}C\longrightarrow0$$

을 정의한다. 이때 $\rho_0$의 lifting $\rho:C\rightarrow R$가 존재하는 것은 $s(c)=(\rho(c),c)$가 $p$의 $A$-algebra section을 주는 것, 곧 이 extension이 split되는 것과 동치이며, 이 때문에 $[\delta]$가 $0$으로 가는 것이 $\rho_0$의 lifting의 존재와 동치임을 안다.

앞서 보았듯 scheme $X_0$의 deformation을 찾는 과정은 base $S=\Spec A$를 square-zero extension을 통해 infinitesimal thickening해 나가며 그 위의 fiber를 함께 정의하는 작업이며, 방금 살펴본 first-order deformation은 이 base의 extension이 가장 단순한 dual numbers $A[\epsilon]$으로 주어진 경우에 해당한다. 우리는 이제 그 위에 놓인 fiber $X_0=\Spec C$가 어떤 방향으로 두꺼워져 flat family $X=\Spec C'$을 이루는지를 보아야 한다.

이를 구체적인 방정식의 언어로 살펴보자. 우리 상황에서 $X$는 locally of finite presentation $S$-scheme이므로, 이 affine case에서 $C$는 finite polynomial ring $B=A[\x_1,\ldots,\x_n]$과 finitely generated ideal $\mathfrak{a}=(f_1,\ldots,f_m)$에 의한 quotient $C=B/\mathfrak{a}$로 나타낼 수 있다. 그럼 $B[\epsilon]=A[\epsilon][\x_1,\ldots,\x_n]$에서는 fiber 방향의 coordinate $\x_i$와 $\epsilon$ 방향이 자연스레 분리되며, 이 때 fiber를 정의하던 각 방정식 $f_j\in B$을 central fiber 주변에서 확장할 수 있는 후보들은 $F_j=f_j+\epsilon g_j$의 꼴이고, 이들 후보에 의해 deform된 family는 $C'=B[\epsilon]/(F_1,\ldots,F_m)$으로 나타나게 될 것이다. 이 때, 유일한 조건은 이렇게 얻어지는 family가 실제로 flat family가 되어야 한다는 것이다. 

::: 명제 4
위와 같은 상황에서, $C'$이 $A[\epsilon]$ 위에서 flat한 것은 $(f_1,\ldots,f_m)$의 임의의 관계식 $(a_1,\ldots,a_m)$, 곧 $\sum_ja_jf_j=0$인 $(a_j)\in B^m$에 대하여

$$\sum_{j}a_jg_j\in \mathfrak{a}$$

이 성립하는 것과 동치이다. 이 조건이 성립할 때, 원래의 관계식 $(a_j)$는 $(F_1,\ldots,F_m)$의 관계식으로 들어올려진다.
:::
::: 증명
앞서 살펴본 것과 같이 $C'$이 flat한 것은 $C'$이 $C$의 $C$에 의한 square-zero extension인 것과 동치이다. $B[\epsilon]\cong B\oplus\epsilon B$에서 $F_j=f_j+\epsilon g_j$는 $(f_j,\bar{g}_j)\in B\oplus C$에 대응하므로, $B[\epsilon]/(F_j)$가 $C$의 square-zero extension을 정의하는 것은 대응 $\bar{f}_j\mapsto\bar{g}_j$가 $\mathfrak{a}/\mathfrak{a}^2$ 위의 $C$-linear map $\varphi:\mathfrak{a}/\mathfrak{a}^2\rightarrow C$를 잘 정의하는 것과 같다. 이는 임의의 관계식 $\sum_ja_jf_j=0$에 대하여 그 image $\sum_ja_j\bar{g}_j$가 $C$에서 $0$인 것, 곧 $\sum_ja_jg_j\in\mathfrak{a}$인 것과 동치이다. 이때 $\sum_ja_jg_j=\sum_jc_jf_j$ ($c_j\in B$)라 하면 $A_j=a_j-\epsilon c_j$에 대하여

$$\sum_jA_jF_j=\sum_ja_jf_j+\epsilon\Bigl(\sum_ja_jg_j-\sum_jc_jf_j\Bigr)=0$$

이므로 원래의 관계식 $(a_j)$가 들어올려진다.
:::

이 명제의 증명은 first-order deformation 상황에서 flat family가 얻어지는 과정을 보여주는데, 이는 즉 central fiber를 정의하던 관계식들, 즉

$$\sum a_jf_j=0$$

이 주어졌다면, $F_j=f_j+\epsilon g_j$를 통해 이를 흔들어 주었을 때, 그 결과

$$\sum a_j(f_j+\epsilon g_j)=\epsilon\sum a_j g_j$$

에서 $\sum a_jg_j$가 $\mathfrak{a}$로 흡수되어, 이를 다시 $f_j$들에 대한 식 $\sum a_jg_j=\sum c_jf_j$로 바꾸어줄 수 있고, 이를 다시 원래의 식에 대입해주면, $A_j=a_j-\epsilon c_j$에 대하여 다음 식

$$\sum_j A_j F_j=0$$

이 성립하므로, 이것이 바로 thickening에서의 방정식이 되는 것이다. 

만일 이 조건이 성립한다면 다음의 대응 $\bar{f}_j\mapsto\bar{g}_j$가 $C$-module homomorphism

$$\varphi:\mathfrak{a}/\mathfrak{a}^2\rightarrow C$$

를 잘 정의하고, 거꾸로 임의의 $\varphi\in\Hom_C(\mathfrak{a}/\mathfrak{a}^2,C)$은 $g_j\in B$를 $\varphi(\bar{f}_j)=\bar{g}_j$이도록 택하여 first-order deformation을 준다. 즉 first-order deformation과 presentation $B\twoheadrightarrow C$의 lift $B\rightarrow C'$를 함께 택한 자료들의 집합은 $\Hom_C(\mathfrak{a}/\mathfrak{a}^2,C)$와 자연스럽게 대응하며, 이는 도입부에서 확대의 자료로부터 얻었던 $\delta\in\Hom_C(\mathfrak{a}/\mathfrak{a}^2,\mathfrak{b})$를 $\mathfrak{b}=C$인 경우에 방정식의 언어로 다시 본 것이다.

이제 남은 일은 이 중 어떤 것들이 trivial deformation을 주는지 걸러내는 것이다. First-order deformation의 경우, $C'=C[\epsilon]$와 isomorphic한 deformation을 *trivial*하다 부른다. 이러한 것들 중 가장 단순한 형태는 모든 $g_j=0$이어서 $F_j=f_j$인 경우로, 이는 central fiber를 정의하던 방정식을 아무런 변형 없이 $\epsilon$ 방향으로 그대로 복사하여 늘려놓은 것에 불과하다.

그러나 $g_j\neq0$이어서 방정식이 변형된 것처럼 보이더라도, 실제로는 trivial deformation인 경우가 있다. Derivation $\theta\in\Der_A(B,C)$를 택하고, 각 $\theta(\x_i)\in C$의 representative $\widetilde{\theta}(\x_i)\in B$를 고르자. 이 선택은 $A$-derivation $\widetilde{\theta}:B\rightarrow B$를 유일하게 결정하며, $\pi\circ\widetilde{\theta}=\theta$를 만족한다. 이제 $B[\epsilon]$의 좌표변환 $\x_i\mapsto\x_i+\epsilon\widetilde{\theta}(\x_i)$를 원래의 식 $f_j$에 적용하면

$$f_j+\epsilon\sum_i\widetilde{\theta}(\x_i)\frac{\partial f_j}{\partial\x_i}=f_j+\epsilon\widetilde{\theta}(f_j)$$

로 옮겨진다. 따라서 $g_j=\widetilde{\theta}(f_j)\in B$로 택한 방정식 $F_j=f_j+\epsilon g_j$들은 ambient space의 좌표변환으로 얻어지며, 이들이 정의하는 family는 원래의 trivial family $C'=C[\epsilon]$과 isomorphic하다. 이때 $\bar{g}_j=\theta(f_j)\in C$이므로, 대응하는 $\varphi$는 $\bar{f}_j\mapsto\theta(f_j)$로 주어진다. 이를 일반화하면, trivial deformation들은 정확히 $\varphi$가 derivation에서 오는 경우, 곧 합성

$$\Der_A(B,C)=\Hom_C(\Omega_{B/A}\otimes_BC,C)\overset{\bar{d}^\ast}{\rightarrow}\Hom_C(\mathfrak{a}/\mathfrak{a}^2,C)$$

의 image에 속하는 경우 얻어지며, 이는 [정의 1](#def1) 직전의 계산에서 lift $\widetilde{\rho}$를 고르는 자유도가 $\Der_A(B,\mathfrak{b})$에 담겼던 것과 같은 현상이다. 

이제 이 절에서 얻은 것을 하나의 분류 정리로 묶는다.

::: 정리 5
Finitely presented $A$-algebra $C=B/\mathfrak{a}$에 대하여 다음의 exact sequence

$$0\longrightarrow T^0(C/A,C)\longrightarrow\Der_A(B,C)\overset{\bar{d}^\ast}{\longrightarrow}\Hom_C(\mathfrak{a}/\mathfrak{a}^2,C)\longrightarrow T^1(C/A,C)\longrightarrow0$$

가 성립하며, 각 항은 deformation theory에서 다음과 같은 의미를 가진다.
1. $\Hom_C(\mathfrak{a}/\mathfrak{a}^2,C)$는 $C$의 first-order deformation과 presentation $B\twoheadrightarrow C$의 lift $B\rightarrow C'$를 함께 택한 자료를 분류한다.
2. 두 deformation이 isomorphic인 것은 그 차이가 trivial deformation들의 공간 $\im\bar{d}^\ast$에 속하는 것과 동치이므로, isomorphism class로 본 first-order deformation들의 집합은 quotient
$$\Hom_C(\mathfrak{a}/\mathfrak{a}^2,C)\big/\im\bar{d}^\ast=T^1(C/A,C)$$
과 자연스럽게 일대일 대응한다. 이 대응 아래에서 trivial deformation은 $0\in T^1$에 대응한다.
3. 임의의 deformation $C'$의 infinitesimal automorphism group은 좌표변환의 stabilizer인 $\ker\bar{d}^\ast$, 곧 $T^0(C/A,C)=\Der_A(C,C)$과 isomorphic하다.
:::

::: 예시 6 (Nodal curve)
앞에서 살펴본 node $\x\y=0$을 엄밀하게 계산해보자. $B=A[\x,\y]$, $f(\x,\y)=\x\y$, $\mathfrak{a}=(f)$라 하고, $C=B/\mathfrak{a}$, $X_0=\Spec C$라 하자. First-order deformation $g\in B$를 택하자. 즉, 적당한 $g\in B$에 대하여

$$F=f+\epsilon g\in B[\epsilon],\qquad C'=B[\epsilon]/(F)$$

로 주어진다. 직관적으로 $\Spec C'$는 $\Spec A$를 무한소방향으로 늘리고, 이 방향을 따라 정의된 fat point $\Spec A'=\Spec A[\epsilon]$를 따라 $X$를 늘려둔 것이며 이를 어떻게 늘렸는지에 대한 정보가 $g$의 선택에 들어있으며, 더 구체적으로 우리는 [정리 5](#thm5)에서 이 선택이 주는 다음의 $C$-linear map

$$\varphi:\mathfrak{a}/\mathfrak{a}^2\longrightarrow C,\qquad \bar{f}\longmapsto\bar{g}$$

이 정확히 first-order deformation에 대한 정보를 모두 담고 있음을 보았다. 즉, $g$의 선택이 deformation을 결정한다. 

예를 들어 $g=\x$를 택하면

$$F=\x\y+\epsilon\x=\x(\y+\epsilon)$$

이므로, 이는 좌표변환 $\y\mapsto\y+\epsilon$으로 원래의 방정식 $f=\x\y$를 옮긴 것이다. 이 좌표변환은 $\epsilon=0$에서 identity로 제한되며 $C[\epsilon]\cong C'$을 유도하므로, $g=\x$는 trivial deformation을 정의한다.

{% diagram Math/Scheme_Theory/Deformation_Theory-4.svg width="12.56em" alt="trivial deformation of node" %}

더 일반적으로, [정리 5](#thm5)에 따르면 trivial deformation은 ambient space $B[\epsilon]$의 무한소 좌표변환에서 오는 경우, 곧 $\varphi\in\im\bar{d}^\ast$인 경우이다. [정리 5](#thm5) 직전에 살펴보았듯, 이러한 좌표변환은 derivation $\theta\in\Der_A(B,C)$이 결정하며, 구체적으로 각 방정식에 그 값 $\theta(f_j)$를 통해 deformation을 정의했다. 우리 예시에서 $B=A[\x,\y]$는 polynomial ring이므로, 임의의 derivation $\theta\in\Der_A(B,C)$는 두 변수의 값

$$\theta(\x)=a,\qquad \theta(\y)=b\qquad(a,b\in C)$$

에 의하여 유일하게 결정되며, 이것이 방정식 $f=\x\y$에 주는 변화량은

$$\theta(f)=\theta(\x\y)=\theta(\x)\y+\x\theta(\y)=a\y+b\x\tag{$\ast\ast$}$$

으로 주어진다. 그럼 $\bar{d}^\ast(\theta)$는 $\mathfrak{a}/\mathfrak{a}^2$의 (유일한) basis $\bar{f}$를 이 값 $\theta(f)\in C$로 보내는 것으로 정의되며, 따라서 $\varphi$가 $\im \bar{d}^\ast$에 속하는 것과, $\bar{g}$가 ($\ast\ast$)의 꼴로 나타나는 것이 동치임을 안다. 특히 앞에서 살펴본 $g=\x$의 경우는 $a=0$이고 $b=1$인 경우이다. 

이제 이로부터 nontrivial deformation의 예시를 쉽게 얻어낼 수 있다. 한편 이 image에 속하지 않는 $\bar{g}$를 택하면 nontrivial deformation을 얻으며, 위의 계산으로부터 우리는 nonzero constant term을 갖는 $g$가 이러한 것임을 안다. 예를 들어 $g=-1$로 택하면

$$F=\x\y-\epsilon,\qquad C'=A[\epsilon][\x,\y]/(\x\y-\epsilon),\qquad X'=\Spec C'$$

을 얻는다. 이는 $-1\in T^1(C/A,C)\cong A$에 대응하므로 $A\neq0$일 때 nontrivial하다.

{% diagram Math/Scheme_Theory/Deformation_Theory-5.svg width="12.56em" alt="smoothing of node" %}

후자의 경우가 nontrivial deformation이 되는 이유는 다음과 같이 직관적인 계산으로도 얻어질 수 있다. Nodal curve $X_0=\Spec C$의 원점은 $\x,\y$를 모두 $0$으로 보내는 ring homomorphism으로 주어진다. Trivial deformation에서는 이 ring homomorphism이 $C[\epsilon]\rightarrow A[\epsilon]$으로 확장되지만, 위의

$$C'=A[\epsilon][\x,\y]/(\x\y-\epsilon)$$

의 경우, $\x,\y\mapsto 0$을 확장하는 $A[\epsilon]$-algebra homomorphism $C'\rightarrow A[\epsilon]$이 존재한다면 반드시 $\x\mapsto \epsilon u$, $\y\mapsto \epsilon v$의 꼴이어야 하지만, 이러한 map의 경우

$$\x\y\mapsto (\epsilon u)(\epsilon v)=0$$

으로 주어지므로 $A[\epsilon,\x,\y]$의 ideal $\x\y-\epsilon$으로 factor through하지 않는다. 즉 $C'$에서 $A'=A[\epsilon]$으로의 $A[\epsilon]$-algebra homomorphism 가운데는 원점에 해당하는 homomorphism을 확장하는 것이 존재하지 않으며, 이는 위에서 살펴보았듯 쌍곡선들이 원점을 놓치는 현상의 대수적 설명이다. 
:::

## 변형의 장애와 고차 변형이론

지금까지 우리는 $A$-algebra $C$의 first-order deformation을 구성하고, 그 isomorphism class를 $T^1(C/A,C)$으로 분류하였다. 이제 우리의 관심사는 주어진 first-order deformation을 더 높은 차수의 deformation으로 높이는 것이다. 만일 one-parameter flat family가 이미 주어졌다면, 이는 단순히 $\t^2, \t^3, \ldots$ 항으로 잘라주어 각 차수를 차례로 보지만, 앞선 절의 도입부에서 살펴봤듯 우리는 이러한 family를 만들어내는 것이 목적이므로 상황이 단순하지 않다. 

이를 직관적으로 살펴보기 위해 앞에서 고정한 presentation

$$C=B/\mathfrak{a},\qquad B=A[\x_1,\ldots,\x_n],\qquad \mathfrak{a}=(f_1,\ldots,f_m)$$

으로 돌아가자. 그럼 first-order deformation의 방정식은, flatness 조건을 만족하는 $g_j$들에 대하여 다음의 꼴

$$F_j=f_j+\t g_j\in B[\t]/(\t^2)$$

로 나타나는 것들이었으며, 이를 한 차수 올려주기 위해서는 $h_j\in B$를 택하여

$$F_j^{(2)}=f_j+\t g_j+\t^2h_j\in B[\t]/(\t^3)$$

을 구성해야 한다. 여기서 필수적인 것은 이렇게 정의한 algebra

$$C^{(2)}=\bigl(B[\t]/(\t^3)\bigr)/(F_1^{(2)},\ldots,F_m^{(2)})$$

가 $A[\t]/(\t^3)$ 위에서 flat하도록 $h_j$들을 골라야 한다는 것으로, 이 조건은 다음과 같이 계산할 수 있다. 

[명제 4](#prop4)에서 flatness는 원래 방정식들 사이의 relation들을 함께 들어올리는 조건으로 나타났던 것을 기억하자. 구체적으로, $C$를 정의하던 방정식들 사이의 relation $\sum_j a_jf_j=0$이 주어졌다 하면, 이를

$$F_j=f_j+\epsilon g_j$$

로 올렸을 때의 방정식

$$\sum_j a_j(f_j+\epsilon g_j)=\epsilon\sum_j a_j g_j$$

에서, $\sum_j a_jg_j$를 $f_j$들에 대한 식 $\sum_j a_jg_j=\sum_j c_jf_j$로 바꾸어줄 수 있으면 이 오차를 $a_j$들로 옮겨 $A_j=a_j-\epsilon c_j$로 정의하면 $\sum_j A_j F_j=0$이 성립하도록 할 수 있었다. 

비슷한 논증을 통해 이를 이차까지 연장하려면 적당한 $d_j\in B$를 택하여 relation의 계수들

$$A_j^{(2)}=a_j-\t c_j+\t^2d_j\in B[\t]/(\t^3)$$

을 구성해야 하며, 이것이 만족할 조건을 구하려면 실제로 두 식의 곱을 $B[\t]/(\t^3)$에서 전개하여

$$\begin{aligned}\sum_j A_j^{(2)}F_j^{(2)}&=\sum_j(a_j-\t c_j+\t^2d_j)(f_j+\t g_j+\t^2h_j)\\
&=\sum_j a_jf_j+\t\Bigl(\sum_j a_jg_j-\sum_j c_jf_j\Bigr)+\t^2\Bigl(\sum_j a_jh_j-\sum_j c_jg_j+\sum_j d_jf_j\Bigr)\end{aligned}$$

을 보면 된다. 이 식에서, 우변의 $\t^0$ 항은 원래의 relation이므로 $0$이고, $\t^1$ 항은 일차에서 이미 flatness를 만족하도록 택했으므로 $0$이다. 이제 이것이 $B[\t]/(\t^3)$에서 $0$이 되도록 하려면 남은 것은 $\t^2$ 항으로, 여기서 $\sum_j d_jf_j\in\mathfrak{a}$이므로 이 조건은 다음의 식

$$\sum_j a_jh_j\equiv\sum_j c_jg_j\pmod{\mathfrak{a}}$$

으로 나타난다. 문제는 이 식의 우변이 이미 first-order deformation을 만족하기 위해 결정된, 일반적으로는 $0$이 아닐 수도 있는 값이라는 것으로, 이 때문에 $h_j$들을 잘 택하여 relation $(a_1, \ldots, a_m)$들이 <em-ko>주어질 때마다</em-ko> 위의 식이 만족되도록 하는 것이 일반적으로 불가능하다. 이것이 first-order deformation과는 다른 점으로, first-order deformation에서는 식

$$\sum_j a_j g_j\equiv 0\pmod{\mathfrak{a}}$$

의 우변이 $0$이었으므로, 하다못해 모든 $g_j$들을 $0$으로 두어 trivial deformation을 택하면 이 식을 만족하는 것 자체는 항상 가능했다. 그러나 이미 어떤 nontrivial한 1차 변형이 주어진 상황에서는 우변이 $0$이 아닌 고정된 잔여항을 이루므로 더 이상 $h_j=0$ 같은 선택으로 만족될 수 없으며, 이렇게 가능한 모든 보정 $h_j$를 허용해도 소거되지 않고 남는 이 실패를 대수적으로 기록한 것이 바로 *obstruction class<sub>장애류</sub>*이다. 

앞서 우리는 first-order deformation에 대한 정보가 naive cotangent complex의 cohomology들인 $T^0$과 $T^1$에 담겨있다는 것을 살펴보았다. 그럼 자연스러운 의문은 이 obstruction class가 사는 공간이 무엇인지에 대한 것이다. 그러나 naive cotangent complex에서 얻어낼 수 있는 정보는 본질적으로 $T^0$과 $T^1$ 뿐이므로, $2$차항의 정보를 얻기 위해서는 naive cotangent complex보다 더 많은 항을 가진 대상이 필요하다. 

이를 위해 앞선 계산에 나타난 relation들의 역할을 구체적으로 살펴보자. 우선 이미 여러 차례 사용한 $C$를 정의하는 방정식 $f_1, \ldots, f_m$ 사이의 *relation*이란, $\sum_j a_jf_j=0$을 만족하는 계수들의 $m$-tuple $(a_1, \ldots, a_m)\in B^m$이며, 이는 형식적으로 다음의 surjection

$$B^m\rightarrow\mathfrak{a};\qquad e_j\mapsto f_j$$

의 kernel $\Rel$의 원소들이다. 이들 방정식들 사이의 *trivial relation*이란 이들 방정식이 $B$의 commutativity에 의해 만족해야 하는 trivial relation들로, 가령 $f_if_j-f_jf_i=0$와 같은 식을 의미한다. 이는 $B^m$의 원소로서는 $j$번째 성분이 $f_i$이고 $i$번째 성분이 $-f_j$이며 나머지 성분이 $0$인 원소 $f_ie_j-f_je_i\in\Rel$에 대응하며, 이러한 원소들이 생성하는 submodule을 $\TrivRel\subseteq\Rel$이라 하자. 이러한 trivial relation들은 $B$의 commutativity에 의해 언제나 성립하므로 obstruction을 만드는 데 아무런 역할을 하지 않는다. 따라서 이들을 $\Rel$에서 지워낸 quotient module $\Rel/\TrivRel$을 생각하면 된다.

::: 정의 7
Finitely presented $A$-algebra $C=B/\mathfrak{a}$에 대하여, *Lichtenbaum–Schlessinger complex<sub>리히텐바움-슐레진저 복합체</sub>* $\operatorname{LS}_{C/A}$는

$$\operatorname{LS}_{C/A}=\Bigl[\at{2}{\Rel/\TrivRel}\overset{d_2}{\longrightarrow}\at{1}{B^m\otimes_BC}\overset{d_1}{\longrightarrow}\at{0}{\Omega_{B/A}\otimes_BC}\Bigr]$$

로 정의되며, 미분은

$$d_2\bigl(\overline{(a_1,\ldots,a_m)}\bigr)=\sum_j\overline{a_j}e_j,\qquad d_1(e_j)=\dd{f_j}\otimes1$$

이다. 각 $i=0,1,2$에 대하여 functor

$$T^i(C/A,M)=H^i\bigl(\Hom_C(\operatorname{LS}_{C/A},M)\bigr)$$

를 $C$의 *Lichtenbaum–Schlessinger functor<sub>리히텐바움-슐레진저 함자</sub>*라 부른다.
:::

어렵지 않게 이 정의의 $T^0$과 $T^1$이 [정의 1](#def1)에서 정의한 것과 정확히 같은 것을 알 수 있으며, 우리 주장은 obstruction class가 $T^2$에 사는 class라는 것이다. First-order deformation $\xi$에 대하여, 앞선 계산에서와 같이 relation $(a_1,\ldots,a_m)\in\Rel$마다 $\sum_ja_jg_j=\sum_jc_jf_j$를 만족하는 $c_j\in B$를 택하면

$$\eta(a_1,\ldots, a_m)=\overline{\sum_jc_jg_j}\in C$$

를 얻는다. 여기서 $c_j$의 다른 선택과의 차이는 다시 $\Rel$의 원소가 되고, $g_j$의 flatness 조건에 의해 그 차이는 $C$에서 $0$이 되며 $\TrivRel$ 위에서는 소멸하므로 이는 잘 정의된 $C$-linear map $\eta: \Rel/\TrivRel\rightarrow C$을 주며 따라서 그 class를 $\ob(\xi)=[\eta]\in T^2(C/A,C)$라 정의할 수 있다. 이는 representative와 presentation의 선택에 무관하게 $\ob(\xi)$는 $\xi$에만 의존하므로 well-defined이다.  

앞선 계산에서 살펴보았듯, $A[\t]/(\t^3)$ 위로의 second-order deformation이 존재할 조건은 모든 relation $a$에 대하여 합동식

$$\sum_jc_jg_j\equiv\sum_ja_jh_j\pmod{\mathfrak{a}}$$

를 만족시키는 $h_j\in B$가 존재하는 것이었다. 그런데 우변은 $h=(\bar{h}_1,\ldots,\bar{h}_m)\in\Hom_C(B^m\otimes_BC,C)$가 미분 $d_2$를 따라 만드는 coboundary의 $a$에서의 값이다. 따라서 이러한 $h_j$가 존재하는 것은 $\eta$가 coboundary인 것, 곧 $[\eta]=0\in T^2(C/A,C)$인 것과 정확히 동치이며 바로 이때 second-order deformation이 존재한다. 즉 다음이 성립한다. 

::: 정리 8
First-order deformation $\xi\in T^1(C/A,C)$가 $A[\t]/(\t^3)$ 위의 flat deformation으로 extend 가능한 것은 $\ob(\xi)=0$인 것과 동치이다.
:::

일반적인 square-zero extension $0\rightarrow \mathfrak{b}\rightarrow R'\rightarrow R\rightarrow0$에 대해서도 $\t$의 거듭제곱 대신 $\mathfrak{b}$를 흔드는 방향으로 같은 계산을 반복하여 obstruction class를 얻으며, extension이 존재할 때 두 extension의 차이에 [정리 5](#thm5)의 논증을 적용하면 그 isomorphism class들이 $T^1$ 위의 torsor를 이룬다.

지금까지의 계산은 더 일반적인 full cotangent complex로 일반화된다. 이를 위해 우리는 $A$-algebra $C$를 한 번 polynomial algebra의 quotient로 나타내는 대신, 각 항이 polynomial $A$-algebra인 free simplicial resolution 

$$P_\bullet\overset{\sim}{\rightarrow}C$$

를 택하고 각 degree에서 Kähler differential을 취한다. 그 결과인 simplicial $C$-module

$$\LL_{C/A}=\Omega_{P_\bullet/A}\otimes_{P_\bullet}C$$

을 chain complex로 본 것이 $C$의 $A$ 위 *cotangent complex<sub>여접 복합체</sub>*이다. 이렇게 정의한 $\LL_{C/A}$의 핵심적인 성질은 이것이 앞서 정의한 두 complex들을 일반화한다는 것으로, 이들은 $\LL_{C/A}$의 truncation

$$\tau_{\leq1}\LL_{C/A}\simeq\NL_{C/A},\qquad \tau_{\leq2}\LL_{C/A}\simeq\operatorname{LS}_{C/A}$$

으로 나타난다. 따라서 임의의 $C$-module $M$에 대하여

$$T^i(C/A,M)=\Ext^i_C(\LL_{C/A},M)$$

로 놓으면, $T^0$는 infinitesimal automorphism을, $T^1$은 first-order deformation과 extension이 존재할 때 그 선택들의 차이를 나타내며 ([정리 5](#thm5)), $T^2$는 extension의 obstruction을 통제한다. ([정리 8](#thm8)). 이제 [명제 2](#prop2)의 smoothness 판정을 full cotangent complex에 적용하면 deformation의 모든 degree에 대한 다음 결론을 얻는다.

::: 명제 9
$C$가 $A$ 위에서 smooth하면 모든 $C$-module $M$에 대하여

$$T^i(C/A,M)=0\qquad(i>0)$$

이다. 특히 $C$의 모든 first-order deformation은 trivial하고, 모든 square-zero lifting problem은 obstruction 없이 유일한 isomorphism class의 해를 가지며, 그 infinitesimal automorphism은 $T^0(C/A,C)=\Der_A(C,C)$가 분류한다.
:::
::: 증명
Smooth한 $C$의 cotangent complex $\LL_{C/A}$는 degree $0$의 $\Omega_{C/A}$에 quasi-isomorphic하고, 이 module이 projective이므로 모든 $i>0$에 대하여

$$T^i(C/A,M)=\Ext^i_C(\LL_{C/A},M)=\Ext^i_C(\Omega_{C/A},M)=0$$

이다. 
:::

앞서 살펴보았듯, $A$ 위의 affine lci algebra $C$에 대해서는 $\LL_{C/A}$가 두 projective module로 이루어진 naive cotangent complex와 quasi-isomorphic하므로 $T^i(C/A,M)=0$이 모든 $i\geq2$에서 성립한다. 따라서 각 단계의 obstruction은 사라지고 first-order deformation을 formal deformation으로 계속 연장할 수 있으며, 이러한 경우 obstruction class가 없다는 의미에서 *unobstructed*라 말한다. 일반적인 non-lci algebra에서는 $\LL_{C/A}$의 higher homology가 남을 수 있고, Lichtenbaum–Schlessinger complex는 그 가운데 고전적 deformation과 obstruction에 필요한 degree $2$까지를 보여 주며 full cotangent complex는 그 뒤의 higher relation까지 보존한다.

## 일반적인 변형이론

지금까지 우리는 affine scheme의 deformation을 다뤘으며, 이제 남은 일은 이 계산을 일반적인 scheme으로 올리는 것이다. Scheme morphism을 affine 조각에서 구성하는 일 자체는 익숙한 gluing이지만, deformation에서는 붙여야 할 자료가 늘어나므로 이 과정에서 필요한 것을 우선 상상해보자. 

먼저 base의 square-zero thickening을 정하고, 각 affine 조각 위에서 flat family를 만든 다음, 두 조각의 overlap에서 이 family들을 식별하는 isomorphism을 골라야 한다. 마지막으로 이 isomorphism들이 triple overlap에서 cocycle 조건을 만족해야 비로소 하나의 scheme deformation이 된다. 뿐만 아니라, cotangent complex도 affine 조각마다 계산한 뒤 restriction과 compatible하도록 붙여야 한다. 이 절에서는 이 과정을 모두 다시 수행하는 대신, 어느 층위에서 어떤 자료와 obstruction이 나타나는지 밝히고 이들이 하나의 대역적 $\Ext$로 조립되는 과정을 정리한다.

우선 처음에 주어지는 base space $S$를 affine scheme이 아닌 일반적인 scheme으로 확장하는 방향이 가장 단순하다.  $S$ 위의 quasi-coherent module $\mathcal{I}$에 대하여 $\mathcal{O}_S\oplus\mathcal{I}$에 곱셈

$$(a,u)(b,v)=(ab,av+bu)$$

을 주면, 이는 $\mathcal{I}^2=0$인 $\mathcal{O}_S$-algebra가 된다. 그럼 이에 대한 relative spectrum $S[\mathcal{I}]=\rSpec_S(\mathcal{O}_S\oplus\mathcal{I})$은 $S$의 split square-zero thickening이고, 특히 $\mathcal{I}=\mathcal{O}_S$인 경우 우리는 이를 $S[\epsilon]$이라 적는다. $S=\Spec A$이면 이는 앞에서 사용한 $\Spec(A[\epsilon])$과 같으며, 더 일반적으로는 square-zero ideal sheaf $\mathcal{I}=\ker(\mathcal{O}_{S'}\rightarrow\mathcal{O}_S)$로 정의된 closed immersion $S\hookrightarrow S'$을 base의 thickening으로 사용할 수 있다.

::: 정의 10
Flat morphism $f:X_0\rightarrow S$, square-zero ideal sheaf $\mathcal{I}$가 정의하는 closed embedding $i:S\hookrightarrow S'$에 대하여, $X_0$의 $S'$ 위로의 *deformation<sub>변형</sub>*이란 flat $S'$-scheme $X$와 $S$-isomorphism

$$\iota:X\times_{S'}S\xrightarrow{\sim}X_0$$

의 쌍 $(X,\iota)$이다. 두 deformation $(X,\iota)$와 $(X',\iota')$이 *isomorphic*이라는 것은 $\iota'\circ(\psi\times_{S'}S)=\iota$를 만족하는 $S'$-isomorphism $\psi:X\rightarrow X'$이 존재하는 것이다. 특히 $S'=S[\epsilon]$인 경우의 deformation을 $X_0$의 $S$ 위 *first-order deformation<sub>일차 변형</sub>*이라 부른다.
:::

이는 위에서 설명한 일반적인 scheme에 대한 infinitesimal thickening을 사용하여 [정의 3](#def3)을 다시 쓴 것에 불과하다. 실제로 square-zero thickening은 underlying topological space를 바꾸지 않으므로 $S$와 $S'$은 같은 열린집합을 가지며, 특히 affine open $V=\Spec A\subseteq S$에 대응하는 $V'\subseteq S'$ 역시 affine이며 이를 $V'=\Spec A'$이라 쓰면 $A'\twoheadrightarrow A$는 square-zero extension이 된다. 즉, 직관적으로 $S$의 infinitesimal thickening은 affine 조각들마다, compatible한 infinitesimal thickening을 한 후 붙여주는 것이라 생각할 수 있다. 마찬가지로 deformation $X$의 underlying space는 central fiber $X_0$와 같아서 $U\subseteq X_0$는 그대로 $X$의 열린집합을 정하며, 덕분에 deformation의 flatness와 central fiber 조건은 affine open들 위에서 확인할 수 있으며, 각 affine 조각에서는 [정의 3](#def3)의 경우로 환원된다. 특히 $V'=\Spec A'$ 위의 affine open을 $U'=\Spec B'\subseteq X$라 하고 $I=\ker(A'\rightarrow A)$라 하면, $B'$은 $A'$ 위에서 flat하므로 $0\rightarrow I\rightarrow A'\rightarrow A\rightarrow0$을 $B'$과 tensor하여 얻는 sequence

$$0\longrightarrow I\otimes_{A'}B'\longrightarrow B'\longrightarrow B'/IB'\longrightarrow0$$

는 exact이고, 또한 $I^2=0$이므로 $I\otimes_{A'}B'\cong I\otimes_A(B'/IB')$가 되어 $X_0\hookrightarrow X$의 ideal sheaf가 $\mathcal{G}=f^\ast\mathcal{I}$로 identify된다.

이제 $X_0$의 affine open cover $X_0=\bigcup_iU_i$를 택하자. 위의 논의에 의해 우리는 각 $U_i$ 위에서 deformation $U_i'$을 만들 수 있지만, 이들을 붙이는 문제가 여전히 남아있다. 우선 overlap $U_{ij}=U_i\cap U_j$ 위에서 central fiber의 항등사상으로 제한되는 isomorphism

$$\varphi_{ij}:U_i'\vert_{U_{ij}}\xrightarrow{\sim}U_j'\vert_{U_{ij}}$$

인 $S'$-isomorphism을 골라야 하고, triple overlap $U_{ijk}$에서 $\varphi_{jk}\circ\varphi_{ij}=\varphi_{ik}$가 성립해야 한다. 그럼 이 조건 하에서 $U_i'$들은 하나의 scheme $X$로 붙고, 각 structure morphism도 $X\rightarrow S'$으로 붙으며, flatness는 source와 base에 대하여 local한 조건이므로 이렇게 얻은 morphism은 flat하다. 즉 이 과정을 통해 deformation을 얻을 수 있다. 반대로 모든 deformation은 이와 같은 데이터를 주는 것이 자명하다.

이 과정에서 필요한 세 가지 자료, 곧 affine 조각 위의 local deformation, 두 조각의 overlap 위의 isomorphism, triple overlap 위의 cocycle 조건은 cotangent complex에 동시에 담긴다. 이를 위해 먼저 affine에서 정의한 complex를 scheme 위로 옮겨야 한다. $U=\Spec B\subseteq X_0$와 $V=\Spec A\subseteq S$가 affine open이고 $f(U)\subseteq V$이면, $\LL_{B/A}$의 각 항과 differential을 sheafify하여 quasi-coherent $\mathcal{O}_U$-module들과 그 사이의 morphism으로 이루어진 complex를 얻는다. Affine 조각마다 택한 presentation과 resolution은 다를 수 있으므로 이 complex들이 overlap에서 항별로 같을 필요는 없으며, 대신 canonical quasi-isomorphism

$$\widetilde{\LL_{B/A}}\xrightarrow{\sim}\LL_{X_0/S}\vert_U$$

이 존재한다. 이 quasi-isomorphism은 $U$와 $V$를 더 작은 affine open으로 줄이는 것과 compatible하므로, local complex들은 quasi-isomorphic complex를 같은 대상으로 보는 의미에서 하나의 cotangent complex $\LL_{X_0/S}$를 정한다.

따라서 affine에서 계산한 $T^0,T^1,T^2$는 $R\sHom_{\mathcal{O}_{X_0}}(\LL_{X_0/S},\mathcal{G})$의 cohomology sheaf로 붙는다. 앞의 affine correspondence에 의하여 각 $U_i$ 위의 local deformation과 그 obstruction은 각각 degree $1$과 $2$에서 읽힌다. 두 local deformation을 $U_{ij}$ 위에서 식별할 수 있는지는 그 restriction들의 차이가 degree $1$에서 $0$인지로 결정되고, 가능한 isomorphism들의 차이는 degree $0$이 잰다. 고른 isomorphism들에 대하여 $\varphi_{ik}^{-1}\circ\varphi_{jk}\circ\varphi_{ij}$는 $U_{ijk}$ 위의 infinitesimal automorphism이므로 degree $0$의 Čech $2$-cocycle를 이루며, 이것이 $0$일 때 정확히 cocycle 조건이 성립한다. Covering의 Čech degree와 local deformation complex의 degree를 함께 모으면

$$R\Gamma\bigl(X_0,R\sHom_{\mathcal{O}_{X_0}}(\LL_{X_0/S},\mathcal{G})\bigr)\simeq R\Hom_{\mathcal{O}_{X_0}}(\LL_{X_0/S},\mathcal{G})$$

을 얻고, 그 $0,1,2$차 cohomology는 각각 대역적 automorphism, deformation들의 차이, existence obstruction을 기록한다. 이에 따라

$$T^i(X_0/S,\mathcal{G})=\Ext^i_{\mathcal{O}_{X_0}}(\LL_{X_0/S},\mathcal{G}),\qquad T^i(X_0/S)=T^i(X_0/S,\mathcal{O}_{X_0})$$

라 적는다.

::: 정리 11 (Cotangent-complex deformation theorem)
$X_0$가 $S$ 위에서 flat하고 separated이며 locally of finite presentation인 scheme이면 $X_0$의 first-order deformation들의 isomorphism class는 $T^1(X_0/S)$와 자연스럽게 일대일 대응하며, trivial deformation은 $0$에 대응하고 그 infinitesimal automorphism은 $T^0(X_0/S)$가 분류한다.

더 일반적으로 $S\hookrightarrow S'$이 square-zero ideal sheaf $\mathcal{I}$로 정의되고 $\mathcal{G}=f^\ast\mathcal{I}$라 하면, $S'$ 위의 deformation의 existence obstruction은 $T^2(X_0/S,\mathcal{G})$에 놓인다. 이 obstruction이 $0$일 때 deformation들의 isomorphism class는 $T^1(X_0/S,\mathcal{G})$ 위의 torsor를 이루고, 각 deformation의 infinitesimal automorphism은 $T^0(X_0/S,\mathcal{G})$가 분류한다.
:::

정리의 대역적 $\Ext$ 하나에는 서로 다른 종류의 문제가 함께 들어 있다. 가령 degree $2$에는 각 affine 조각에서 lifting 자체가 존재하지 않는 local obstruction, overlap에서 local lifting들을 서로 identify하지 못하는 obstruction, 고른 identification들이 triple overlap에서 cocycle 조건을 만족하지 못하는 obstruction이 함께 기여한다. 이들은 각각 local deformation degree와 접합 degree가 $(0,2),(1,1),(2,0)$인 위치에 놓인다. 이들을 분리하려면 위 total complex를 두 degree 가운데 어느 방향으로 먼저 계산할지 정해야 한다. 이 filtration이 다음 local-to-global spectral sequence를 만든다.

이를 위해 대역적 $\Ext$와 대비되는 국소적 불변량인 *sheaf $\operatorname{Ext}$<sub>층 $\operatorname{Ext}$</sub>*

$$\mathcal{E}xt^q_{\mathcal{O}_{X_0}}(\mathcal{F},\mathcal{G})=R^q\sHom_{\mathcal{O}_{X_0}}(\mathcal{F},\mathcal{G})$$

를 생각하자. 이는 각 열린집합 $U$에 $\Ext^q_{\mathcal{O}_U}(\mathcal{F}\vert_U,\mathcal{G}\vert_U)$를 대응시키는 presheaf의 sheafification이다. 일반적으로 left exact functor $\Phi,\Psi$의 합성에 대하여, $\Psi$의 higher derived functor를 먼저 계산하고 여기에 $\Phi$의 higher derived functor를 적용한 값들을 $\Phi\Psi$의 higher derived functor로 모으는 spectral sequence를 Grothendieck spectral sequence라 부른다. Sheaf $\mathcal{F}$를 고정하면 지금의 두 functor는 $\Psi=\sHom_{\mathcal{O}_{X_0}}(\mathcal{F},-)$와 $\Phi=\Gamma(X_0,-)$이고,

$$\Gamma\bigl(X_0,\sHom_{\mathcal{O}_{X_0}}(\mathcal{F},-)\bigr)=\Hom_{\mathcal{O}_{X_0}}(\mathcal{F},-)$$

이다. Complex $\mathcal{K}$에 대해서는 이를 derived functor의 형태 $R\Gamma\circ R\sHom(\mathcal{K},-)\simeq R\Hom(\mathcal{K},-)$으로 적용한다. $R\sHom$의 cohomology sheaf를 먼저 취한 뒤 $R\Gamma$를 적용하는 filtration이 local-to-global $\Ext$ spectral sequence를 준다. 이는 double complex의 한 방향 cohomology를 먼저 계산하는 [\[호몰로지 대수학\] §스펙트럼 열, ⁋예시 11](/ko/math/homological_algebra/spectral_sequences#ex11)의 구성과 같은 원리이다.

::: 정리 12 (국소-대역 exact sequence)
$X_0$ 위의 quasi-coherent cohomology sheaf를 갖는 bounded above complex $\mathcal{K}$가 $q<0$에서 $\mathcal{E}xt^q_{\mathcal{O}_{X_0}}(\mathcal{K},\mathcal{O}_{X_0})=0$을 만족한다고 하자. 이때 local-to-global spectral sequence ([\[호몰로지 대수학\] §스펙트럼 열](/ko/math/homological_algebra/spectral_sequences))

$$E_2^{p,q}=H^p\bigl(X_0,\mathcal{E}xt^q_{\mathcal{O}_{X_0}}(\mathcal{K},\mathcal{O}_{X_0})\bigr)\Longrightarrow\Ext^{p+q}_{\mathcal{O}_{X_0}}(\mathcal{K},\mathcal{O}_{X_0})$$

가 존재한다. 특히 $\mathcal{K}=\LL_{X_0/S}$로 놓고 $\mathcal{T}_{X_0/S}^q=\mathcal{E}xt^q_{\mathcal{O}_{X_0}}(\LL_{X_0/S},\mathcal{O}_{X_0})$라 적으면 그 낮은 차수 부분은 exact sequence

$$0\longrightarrow H^1(X_0,\mathcal{T}_{X_0/S}^0)\longrightarrow T^1(X_0/S)\longrightarrow H^0(X_0,\mathcal{T}_{X_0/S}^1)\overset{d_2}{\longrightarrow}H^2(X_0,\mathcal{T}_{X_0/S}^0)\longrightarrow T^2(X_0/S)$$

를 이룬다.
:::
::: 증명
$R\sHom_{\mathcal{O}_{X_0}}(\mathcal{K},\mathcal{O}_{X_0})$의 대역적 cohomology를 injective resolution으로 계산하면, 한 방향에서는 cohomology sheaf $\mathcal{E}xt^q$를 계산하고 다른 방향에서는 그 sheaf cohomology $H^p$를 계산하는 double complex를 얻는다. 이를 $p$ 방향으로 filter하여 [\[호몰로지 대수학\] §스펙트럼 열, ⁋명제 10](/ko/math/homological_algebra/spectral_sequences#prop10)을 적용하면 $E_2$ page는 표시한 $H^p(X_0,\mathcal{E}xt^q)$이고 abutment는 total complex의 cohomology인 $\Ext^{p+q}$이다. 가정에 의해 이는 first quadrant spectral sequence를 이룬다. 전체 차수 $1$에 놓인 두 항 $(1,0)$과 $(0,1)$을 filtration으로 읽고, $(0,1)$에서 나가는 첫 비자명한 differential $d_2:E_2^{0,1}\rightarrow E_2^{2,0}$을 붙이면 표시한 five-term exact sequence를 얻는다.
:::

왼쪽의 $H^1(X_0,\mathcal{T}_{X_0/S}^0)$은 각 affine 조각에서는 trivial하지만 overlap isomorphism을 흔들어 얻는 locally trivial deformation이다. 가운데의 morphism $T^1(X_0/S)\rightarrow H^0(X_0,\mathcal{T}_{X_0/S}^1)$은 대역적 deformation에서 접합 자료를 잊고 그 local deformation class들만 남긴다. 따라서 $H^0(X_0,\mathcal{T}_{X_0/S}^1)$은 서로 restriction-compatible한 local deformation class들의 모임이고, differential $d_2$는 이 class들의 representatives와 overlap isomorphism을 골랐을 때 triple overlap에 남는 cocycle obstruction이다. 즉 $d_2$가 $0$인 local class들만 실제 scheme deformation으로 붙는다.

::: 따름정리 13
$X_0$가 $S$ 위에서 smooth하면 모든 $i$에 대하여

$$T^i(X_0/S)\cong H^i(X_0,\mathcal{T}_{X_0/S})$$

이다. 특히 first-order deformation들의 isomorphism class는 $H^1(X_0,\mathcal{T}_{X_0/S})$가 분류한다.
:::
::: 증명
Smooth한 경우 $\LL_{X_0/S}\simeq\Omega_{X_0/S}$이고 $\Omega_{X_0/S}$가 locally free이므로 $q>0$에서 $\mathcal{T}_{X_0/S}^q=0$이며 $\mathcal{T}_{X_0/S}^0=\sHom_{\mathcal{O}_{X_0}}(\Omega_{X_0/S},\mathcal{O}_{X_0})=\mathcal{T}_{X_0/S}$이다. 따라서 [정리 12](#thm12)의 spectral sequence가 $q=0$인 한 행으로 퇴화한다.
:::

---

**참고문헌**

**[Har]** R. Hartshorne, *Deformation theory*, Graduate Texts in Mathematics 257, Springer, 2010.  
**[Ill]** L. Illusie, *Complexe cotangent et déformations I, II*, Lecture Notes in Mathematics 239, 283, Springer, 1971--1972.  
**[Stacks]** The Stacks project authors, *The Stacks project*, [stacks.math.columbia.edu](https://stacks.math.columbia.edu).
