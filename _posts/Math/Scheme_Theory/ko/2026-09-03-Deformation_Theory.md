---
title: "변형이론과 여접 복합체"
description: "Square-zero 확대를 따른 변형과 obstruction을 통해 Kähler differential만으로는 부족한 이유를 밝히고, naive 여접 복합체의 H_0·H_1이 변형이론적으로 무엇을 재는지, 그리고 완전한 여접 복합체가 왜 필요한지를 동기화한다."
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

이 잘 정의된다. 뿐만 아니라, 이렇게 얻어진 $\delta$는 $C$-linear map이 된다. 여기서 $\mathfrak{a}/\mathfrak{a}^2$는 $\mathfrak{a}$를 $B$-module로 봤을 때, $B$의 부분집합 $\mathfrak{a}$가 이 위에 $0$으로 작용하므로 $C=B/\mathfrak{a}$-module structure가 주어진 것이고, $\mathfrak{b}$의 경우 $\mathfrak{b}^2=0$인 것으로부터 $\mathfrak{b}$의 $R$-module structure가 $R_0=R/\mathfrak{b}$-module structure를 주고, 이를 $\rho_0$를 따라 $C$-module로 본 것이다. 즉, 고정된 $\widetilde{\rho}$에 대하여 $\widetilde{\rho}(\mathfrak{a})=0$인 것은 정확히 이런 방식으로 정의한 $C$-linear map $\delta\in\Hom_C(\mathfrak{a}/\mathfrak{a}^2, \mathfrak{b})$가 $0$이 되는 것과 같다. 

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

이므로 모든 $n$에 대하여 $H_n(\ker p)=0$이다. 위의 short exact sequence에 [\[호몰로지 대수학\] §긴 완전열, ⁋정리 1](/ko/math/homological_algebra/long_exact_sequence#thm1)을 적용하면 모든 degree에서 $H_n(p)$가 isomorphism이 되어, $p$는 $\NL_{C/A}$에서 degree $0$의 projective module $\Omega_{C/A}$로의 quasi-isomorphism이 된다. 즉, 이 경우에는 $\Omega_{C/A}$만 보아도 lifting들의 차이 $T^0(C/A,M)=\Hom_C(\Omega_{C/A},M)$를 계산할 수 있고, lifting의 존재를 가로막는 obastruction space $T^1$은 항상 사라진다.

그러나 일반적인 $C$에 대해서는 conormal morphism의 kernel과 그 image가 direct summand인지 여부부터 살펴보아야 한다. $\Omega_{C/A}$는 이 morphism의 cokernel이므로, 이 두 조건을 직접 다루려면 그 앞의 항과 morphism까지 남긴 $\NL_{C/A}$가 본격적으로 필요하게 된다. 이 상황을 대표하는 것이 lci의 경우이다. ([§완전교차, ⁋정의 1](/ko/math/scheme_theory/complete_intersections#def1)) 일반적인 non-lci 상황에서는 비슷한 계산을 수행하기 위해 cotangent complex 전체를 살펴보아야 할 수 있지만, lci에서는 naive cotangent complex가 cotangent complex 전체와 quasi-isomorphic하다. 이러한 관점에서 lci는 필요한 cotangent data를 naive cotangent complex에서 직접 읽을 수 있는 대표적인 경우로 생각할 수 있다.

구체적인 상황을 보기 위하여 $B=A[\x_1,\ldots,\x_n]$, $C=B/\mathfrak{a}$로 놓고, $\mathfrak{a}=(f_1,\ldots,f_r)$가 $B$-regular sequence로 생성된다고 하자. 각 $f_j$의 class를 보내는 $C$-linear morphism

$$C^r\longrightarrow\mathfrak{a}/\mathfrak{a}^2,\qquad e_j\longmapsto\bar{f}_j$$

은 [§완전교차, ⁋명제 5](/ko/math/scheme_theory/complete_intersections#prop5)와 그 증명에 의하여 isomorphism이므로, 이 경우 naive cotangent complex는 Jacobian에 의해

$$\NL_{C/A}\cong\left[C^r\overset{\bar{d}}{\longrightarrow}C^n\right],\qquad\bar{d}(e_j)=\sum_i\overline{\frac{\partial f_j}{\partial\x_i}}\dd{\x_i}$$

로 주어지며 두 항은 모두 finitely generated free (따라서 finitely generated projective) $C$-module이다. 일반적인 lci 상황에서는 이들 두 free module 사이의 morphism이 남지만, 위에서 살펴본 smooth 상황에서는 여기에 $\bar{d}$가 split injection이라는 조건이 더해져 complex가 degree $0$의 projective module 하나로 줄어드는 것이다. 

## 일차 변형이론

앞에서 우리는 naive cotangent complex가 smoothness의 infinitesimal lifting property를 어떻게 기록하는지 살펴보았다. 이 complex는 deformation theory에서도 중심적인 역할을 한다. 

Deformation theory의 기하학적 출발점은 $A$-scheme $X_0$를 고정하고, section $t_0:\Spec A\rightarrow T$을 갖춘 pointed $A$-scheme $(T,t_0)$ 위의 family $\pi:X\rightarrow T$와 central fiber의 identification $X\times_T\Spec A\cong X_0$를 찾는 것이다. [§스킴 사이의 사상, ⁋예시 10](/ko/math/scheme_theory/morphism_of_schemes#ex10)에서와 같이 scheme morphism $\pi:X\rightarrow T$를 $T$로 매개화된 family로 보면, 이는 $T$ 위에서 변하는 scheme들 가운데 section $t_0$을 따라 얻는 fiber가 $X_0$으로 주어지는 family를 보는 것이다. 이러한 관점을 위해 $\pi$가 flat일 것을 요구하는 것이 합리적이며 ([§평탄사상](/ko/math/scheme_theory/flat_morphisms)) 이러한 가정 아래 이는 fiber들을 하나의 대상 $X_0$가 변해 가는 모습으로 보고 비교하는 것이다.

가장 단순한 예시로 두 직선이 원점에서 만나는 node $X_0=\Spec\bigl(A[\x,\y]/(\x\y)\bigr)$를 생각하자. 이를 deform하는 가장 간단한 방법은 방정식 $\x\y=0$을 $\x\y=t$로 바꾸어 다음의 family

$$\pi:X=\Spec\bigl(A[t,\x,\y]/(\x\y-t)\bigr)\longrightarrow\Spec A[t]$$

를 생각하는 것이다. 이는 $t=0$에서 $X_0$를 fiber로 갖고, $t$를 invert한 open set 위에서는 $\x$와 $\y$가 모두 invertible이 되어 smooth한 family를 이루며, [§평탄사상, ⁋명제 5](/ko/math/scheme_theory/flat_morphisms#prop5)을 통해 $\pi$의 flatness 또한 확인할 수 있다. 즉 이 family를 보면 $X_0$의 원점에 있던 singularity가 parameter $t$를 따라 어떻게 사라지는지를 살펴볼 수 있다.

일반적인 scheme $X_0$의 deformation을 찾는 첫 단계는 base의 central section $t_0$에서 infinitesimal direction들을 하나씩 살펴보는 것이다. $A[\epsilon]=A[t]/(t^2)$로 놓으면, $(T,t_0)$의 $A$-상대 tangent direction은 $t=0$에서 $t_0$로 제한되는 $A$-morphism $\Spec A[\epsilon]\rightarrow T$으로 표현된다 ([§매끄러운 사상과 에탈 사상, §§Infinitesimal lifting criterion](/ko/math/scheme_theory/smooth_and_etale_morphisms#infinitesimal-lifting-criterion)). 이를 따라 $\pi:X\rightarrow T$를 pullback하면 $\Spec A[\epsilon]$ 위의 family를 얻으며, 직관적으로 이는 그 tangent direction을 따라 $X_0$이 일차까지 변하는 모습을 기록한다.

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

특히 $A'=A[\epsilon]=A[t]/(t^2)$인 경우의 deformation을 $C$의 $A$ 위 *first-order deformation<sub>일차 변형</sub>*이라 부른다.
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

을 morphism으로 갖는 category $\Ext_{\Alg{A}}(C,M)$을 이루며, 이때 이들 morphism들은 [\[호몰로지 대수학\] §Diagram chasing, ⁋따름정리 3](/ko/math/homological_algebra/diagram_chasing#cor3)에 의해 모두 isomorphism이다. 즉 이 category는 groupoid이고, 그 대상들 사이에 morphism이 존재하는지에 따라 square-zero extension의 isomorphism class들이 나뉜다.실제로, 위의 category의 임의의 데이터

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

앞서 보았듯 scheme $X_0$의 deformation을 찾는 과정은 base $S=\Spec A$를 square-zero extension을 통해 infinitesimal thickening해 나가며 그 위의 fiber를 함께 정의하는 작업이며, 방금 살펴본 first-order deformation은 이 베이스의 확장이 가장 단순한 dual numbers $A[\epsilon]$으로 주어진 경우에 해당한다. 우리는 이제 그 위에 놓인 fiber $X_0=\Spec C$가 어떤 방향으로 두꺼워져 flat family $X=\Spec C'$을 이루는지를 보아야 한다.

이를 구체적인 방정식의 언어로 살펴보자. 우리 상황에서 $X$는 locally of finite presentation $S$-scheme이므로, 이 affine case에서 $C$는 finite polynomial ring $B=A[\x_1,\ldots,\x_n]$과 finitely generated ideal $\mathfrak{a}=(f_1,\ldots,f_m)$에 의한 quotient $C=B/\mathfrak{a}$로 나타낼 수 있다. 그럼 $B[\epsilon]=A[\epsilon][\x_1,\ldots,\x_n]$에서는 fiber 방향 좌표 $\x_i$와 $\epsilon$ 방향이 자연스레 분리되며, 이 때 fiber를 정의하던 각 방정식 $f_j\in B$을 central fiber 주변에서 확장할 수 있는 후보들은 $F_j=f_j+\epsilon g_j$의 꼴이고, 이들 후보에 의해 deform된 family는 $C'=B[\epsilon]/(F_1,\ldots,F_m)$으로 나타나게 될 것이다. 이 때, 유일한 조건은 이렇게 얻어지는 family가 실제로 flat family가 되어야 한다는 것이다. 

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

를 잘 정의하고, 거꾸로 임의의 $\varphi\in\Hom_C(\mathfrak{a}/\mathfrak{a}^2,C)$은 $g_j\in B$를 $\varphi(\bar{f}_j)=\bar{g}_j$이도록 택하여 first-order deformation을 준다. 즉 first-order deformation들의 집합은 $\Hom_C(\mathfrak{a}/\mathfrak{a}^2,C)$와 자연스럽게 대응하며, 이는 도입부에서 확대의 자료로부터 얻었던 $\delta\in\Hom_C(\mathfrak{a}/\mathfrak{a}^2,\mathfrak{b})$를 $\mathfrak{b}=C$인 경우에 방정식의 언어로 다시 본 것이다.

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
1. $\Hom_C(\mathfrak{a}/\mathfrak{a}^2,C)$는 $C$의 first-order deformation들을 분류한다.
2. 두 deformation이 isomorphic인 것은 그 차이가 trivial deformation들의 공간 $\im\bar{d}^\ast$에 속하는 것과 동치이므로, isomorphism class로 본 first-order deformation들의 집합은 quotient
$$\Hom_C(\mathfrak{a}/\mathfrak{a}^2,C)\big/\im\bar{d}^\ast=T^1(C/A,C)$$
과 자연스럽게 일대일 대응한다. 이 대응 아래에서 trivial deformation은 $0\in T^1$에 대응한다.
3. 임의의 deformation $C'$의 infinitesimal automorphism군은 좌표변환의 stabilizer인 $\ker\bar{d}^\ast$, 곧 $T^0(C/A,C)=\Der_A(C,C)$과 동형이다.
:::

::: 예시 6 (Nodal curve)
앞에서 살펴본 node $\x\y=0$을 살펴보자. $B=A[\x,\y]$, $f(\x,\y)=\x\y$, $\mathfrak{a}=(f)$라 하고, $C=B/\mathfrak{a}$, $X_0=\Spec C$라 하자. First-order deformaion $g\in B$를 택하자. 즉, 적당한 $g\in B$에 대하여

$$F=f+\epsilon g\in B[\epsilon],\qquad C'=B[\epsilon]/(F)$$

로 주어진다. 직관적으로 $\Spec C'$는 $\Spec A$를 무한소방향으로 늘리고, 이 방향을 따라 정의된 fat point $\Spec A'$를 따라 $X$를 늘려둔 것이다. 

 $C'/\epsilon C'\cong C$이므로 $X'=\Spec C'$의 structure morphism $X'\rightarrow\Spec A[\epsilon]$은 central fiber의 identification

$$X'\times_{\Spec A[\epsilon]}\Spec A\cong X_0$$

를 갖는다. 또 $C$는 $1,\x,\x^2,\ldots,\y,\y^2,\ldots$를 basis로 갖는 free $A$-module이고, $f=\x\y$는 $B$의 nonzerodivisor이므로 $a\in B$에 대하여 $af=0$인 relation은 $a=0$뿐이다. 따라서 [명제 4](#prop4)의 조건은 모든 $g\in B$에 대해 성립하며, $C'$은 $A[\epsilon]$ 위에서 flat하다.

이 deformation을 기록하는 $C$-linear map $\varphi$는

$$\varphi:\mathfrak{a}/\mathfrak{a}^2\longrightarrow C,\qquad \bar{f}\longmapsto\bar{g}$$

이다. 여기서 $\bar{f}$는 $f$의 $\mathfrak{a}/\mathfrak{a}^2$에서의 class이고, $\bar{g}$는 $g$의 $C=B/\mathfrak{a}$에서의 class이다. $\mathfrak{a}/\mathfrak{a}^2=C\bar{f}$이므로 $\varphi$는 $\bar{g}$ 하나로 결정된다. 즉, $g$로 방정식을 바꾸는 자료를 module의 언어로 기록한 것이 $\varphi$이다.

이제 [정리 5](#thm5)에 따라 좌표변환에서 오는 변화를 제외하자. $\theta(\x)=a$, $\theta(\y)=b$인 derivation $\theta\in\Der_A(B,C)$에 대하여

$$\theta(f)=\theta(\x\y)=a\y+b\x$$

이므로, $\Hom_C(\mathfrak{a}/\mathfrak{a}^2,C)\cong C$라는 identification 아래에서 $\im\bar{d}^\ast=(\x,\y)\subseteq C$이다. 따라서

$$T^1(C/A,C)\cong C/(\x,\y)\cong A$$

이며, $F=f+\epsilon g$의 isomorphism class는 $g$의 constant term으로 결정된다. 특히 $g=-1$을 택하면

$$F=\x\y-\epsilon,\qquad C'=A[\epsilon][\x,\y]/(\x\y-\epsilon)$$

을 얻고, 이는 $-1\in T^1(C/A,C)\cong A$에 대응하므로 $A\neq0$일 때 nontrivial하다. 반면 $g=\x$이면 $F=\x\y+\epsilon\x=\x(\y+\epsilon)$이므로 좌표변환 $\y\mapsto\y+\epsilon$으로 얻어지는 trivial deformation이다.

끝으로 $g=-1$인 first-order deformation은 앞에서 보았던 family

$$\pi:X=\Spec\bigl(A[t,\x,\y]/(\x\y-t)\bigr)\longrightarrow\Spec A[t]$$

의 일차 근사이다. 관계식 $\x\y=t$로 mixed monomial들을 정리하면 이 coordinate ring의 각 원소는 $A[t]$의 원소를 coefficient로 갖는 $1,\x,\x^2,\ldots,\y,\y^2,\ldots$의 유한한 linear combination으로 유일하게 표현된다. 따라서 이들은 $A[t]$-basis를 이루며, $\pi$는 flat하다. $A[t]\rightarrow A[\epsilon]$, $t\mapsto\epsilon$을 따라 pullback하면 위의 $X'$를 얻고, $A[t]\rightarrow A[t]/(t^{n+1})$을 따라 pullback하면 모든 $n\geq1$에 대하여 서로 호환되는 고차 deformation을 얻는다. 이 경우에는 방정식 $\x\y-t$에 고차 보정항을 더할 필요가 없다.
:::

## 변형의 장애와 고차 변형이론

지금까지 우리는 $A$-algebra $C$의 first-order deformation을 구성하고, 그 isomorphism class를 $T^1(C/A,C)$으로 분류하였다. [예시 6](#ex6)에서는 $\x\y-\epsilon$으로 주어진 first-order deformation을 $\x\y-t$라는 flat family로 연장할 수 있었다. 이제 우리의 관심사는 일반적인 presentation에서도 주어진 first-order deformation을 더 높은 차수의 deformation으로 높이는 것이다. 만일 one-parameter flat family가 이미 주어졌다면, 이를 각각 modulo $t^2,t^3,\ldots$으로 제한하여 각 차수를 차례로 보지만, 앞선 절의 도입부에서 살펴봤듯 우리는 이러한 family를 만들어내는 것이 목적이므로 상황은 더 복잡하다.

이를 직관적으로 살펴보기 위해 앞에서 고정한 presentation

$$C=B/\mathfrak{a},\qquad B=A[\x_1,\ldots,\x_n],\qquad \mathfrak{a}=(f_1,\ldots,f_m)$$

으로 돌아가자. First-order deformation의 방정식은

$$F_j=f_j+tg_j\in B[t]/(t^2)$$

이었다. 이를 이차까지 연장하려면 $h_j\in B$를 택하여

$$F_j^{(2)}=f_j+tg_j+t^2h_j\in B[t]/(t^3)$$

을 구성해야 한다. 여기서 $f_j,g_j,h_j$는 모두 $B$의 원소이며, 각각 원래의 방정식, 이미 주어진 일차 변화, 이제 선택할 이차 보정항이다. $F_j^{(2)}$는 이들을 매개변수 $t$로 조합한 확장된 환의 원소이다. 목표는 $t^2=0$으로 제한하면 주어진 first-order deformation으로 돌아오면서, algebra

$$C^{(2)}=\bigl(B[t]/(t^3)\bigr)/(F_1^{(2)},\ldots,F_m^{(2)})$$

가 $A[t]/(t^3)$ 위에서 flat하도록 $h_j$들을 고르는 것이다.

앞서 [명제 4](#prop4)에서 flatness는 원래 방정식들 사이의 relation을 함께 들어올리는 조건으로 나타났다. 일차에서는 $g_j$들이 이 조건을 만족하도록 택했지만, 이차에서는 relation의 일차 보정항과 방정식의 일차 보정항이 곱해져 새로운 잔여항이 나타난다. 이 잔여항을 $h_j$들과 relation의 이차 보정으로 소거할 수 있다면 deformation을 연장할 수 있다. 그러나 가능한 보정을 모두 허용해도 소거되지 않는 부분이 남을 수 있으며, 그 실패를 선택에 무관한 class로 기록한 것이 obstruction class이다. 따라서 특정한 보정이 실패했다는 사실만으로 연장이 불가능한 것은 아니며, 모든 보정의 자유도를 고려한 뒤에도 남는 잔여항을 살펴보아야 한다.

고차 deformation을 구성하는 과정은 이처럼 이미 얻은 근사를 유지하면서 다음 차수의 flatness 조건을 차례로 해결하는 과정이다. 모든 차수에서 호환되는 연장을 얻으면 이들의 체계가 formal deformation을 이룬다. 이를 실제 family로 실현하는 문제는 별도로 남는다. 이제 첫 단계인 일차에서 이차로의 연장을 살펴보고, relation에서 발생하는 잔여항을 기록할 수 있도록 complex를 확장하자.

Naive cotangent complex $\NL_{C/A}=[\mathfrak{a}/\mathfrak{a}^2\rightarrow\Omega_{B/A}\otimes_BC]$에서는 방정식들과 그 관계가 $\mathfrak{a}/\mathfrak{a}^2$라는 하나의 module에 묶여 있었다. Obstruction을 계산하려면 relation에 값을 부여하는 데이터를 별도의 항으로 기록해야 한다. 이를 위해 방정식들을 표시하는 free module $F=B^m$을 두고, $e_j\mapsto f_j$로 주어지는 사상 $F\rightarrow\mathfrak{a}$의 kernel을 $\operatorname{Rel}$이라 하자. 이때 $f_ie_j-f_je_i$ 꼴의 Koszul relation들은 방정식의 선택에 관계없이 성립하는 trivial relation들이며, 이들이 생성하는 submodule을 $\operatorname{TrivRel}$이라 적는다. 이들을 제외한 $\operatorname{Rel}/\operatorname{TrivRel}$이 obstruction을 기록하는 데 필요한 $C$-module이 된다. 따라서 $\NL_{C/A}$의 $\mathfrak{a}/\mathfrak{a}^2$를 $F\otimes_BC$로 풀고, 그 왼쪽에 $\operatorname{Rel}/\operatorname{TrivRel}$을 붙여 3개 항의 complex를 구성한다.

::: 정의 7
$C=B/\mathfrak{a}$의 presentation $B=A[\x_1,\ldots,\x_n]$, $\mathfrak{a}=(f_1,\ldots,f_m)$에 대하여, $F=B^m$의 basis를 $e_1,\ldots,e_m$이라 하고 전사사상 $F\rightarrow \mathfrak{a}$, $e_j\mapsto f_j$의 kernel을 $\operatorname{Rel}$이라 하자. 또 $\operatorname{TrivRel}\subseteq\operatorname{Rel}$을 $f_ie_j-f_je_i$ 꼴의 trivial relation들이 생성하는 submodule이라 하자. 이때 *Lichtenbaum–Schlessinger complex* $\operatorname{LS}_{C/A}$는

$$\operatorname{LS}_{C/A}=\Bigl[\at{2}{\operatorname{Rel}/\operatorname{TrivRel}}\overset{d_2}{\rightarrow}\at{1}{F\otimes_BC}\overset{d_1}{\rightarrow}\at{0}{\Omega_{B/A}\otimes_BC}\Bigr]$$

로 정의되며, 미분은

$$d_2\bigl(\overline{(a_1,\ldots,a_m)}\bigr)=\sum_j\overline{a_j}e_j,\qquad d_1(e_j)=\dd{f_j}\otimes1$$

이다. 각 $i=0,1,2$에 대하여 함자

$$T^i(C/A,M)=H^i\bigl(\Hom_C(\operatorname{LS}_{C/A},M)\bigr)$$

를 $C$의 *Lichtenbaum–Schlessinger functor<sub>리히텐바움-슐레진저 함자</sub>*라 부른다.
:::

이 정의는 $i=0,1$에서 [정의 1](#def1)과 어긋나지 않는다. 양쪽 모두 degree $0$ cocycle은 $\mathfrak{a}$를 죽여 $C=B/\mathfrak{a}$ 위로 내려오는 derivation $B\rightarrow M$, 곧 $\Der_A(C,M)$의 원소이고, quotient

$$\bigl(F\otimes_BC\bigr)/\im d_2\cong \mathfrak{a}/\mathfrak{a}^2$$

에 의하여 degree $1$ cocycle은 $\Hom_C(\mathfrak{a}/\mathfrak{a}^2,M)$의 원소와 같다. 따라서 위 정의의 $T^1$은 앞서 얻은 $\coker\bar{d}^\ast$, 곧 "flat deformation modulo trivial"과 정확히 일치한다. $T^2$에서 새로 등장한 $\operatorname{Rel}/\operatorname{TrivRel}$은 방정식들 사이의 관계식 가운데 tautological한 Koszul 관계를 넘어서는 부분을 기록한다. 이 점은 obstruction을 다룰 때 분명해진다.

이렇게 $T^0$과 $T^1$은 two-term complex $\NL_{C/A}$만으로 올바르게 계산되지만, $T^2$는 Lichtenbaum–Schlessinger complex의 degree $2$ 항을 추가로 요구한다. 더 정확히는, 뒤에서 다룰 완전한 여접 복합체 $\LL_{C/A}$에 대하여 $T^i(C/A,M)=\Ext^i_C(\LL_{C/A},M)$이며, $\NL_{C/A}$와 $\operatorname{LS}_{C/A}$는 각각 $\LL_{C/A}$의 degree $0,1$ 절단과 degree $0,1,2$ 절단이다. $T^2$가 naive complex의 범위를 벗어난다는 이 사실이, obstruction을 제대로 다루려면 적어도 한 항을 더 보아야 한다는 첫 신호이다.

이제 obstruction class를 실제로 만들어 보자. First-order deformation $\xi$를 [명제 4](#prop4)와 같이 $F_j=f_j+tg_j$로 실현하면, flatness에 의하여 relation $a=(a_1,\ldots,a_m)\in\operatorname{Rel}$마다 $\sum_ja_jg_j=\sum_jc_jf_j$이도록 하는 $c_j\in B$를 고를 수 있다. 이 선택으로

$$\eta(a)=\overline{\sum_jc_jg_j}\in C$$

를 정의한다. $c_j$의 다른 선택과의 차이는 다시 $\operatorname{Rel}$의 원소이고 $g_j$가 [명제 4](#prop4)의 flatness 조건을 만족하므로 그 차이는 $C$에서 $0$이 되며, trivial relation 위에서는 $\eta$가 소멸하므로 이는 $C$-linear map $\eta:\operatorname{Rel}/\operatorname{TrivRel}\rightarrow C$을 준다. 그 class를 $\operatorname{ob}(\xi)=[\eta]\in T^2(C/A,C)$라 적는다.

이 class가 연장 가능성을 정확히 판정한다. $A[t]/(t^3)$ 위의 연장을 $F_j^{(2)}=f_j+tg_j+t^2h_j$ 꼴로 찾고 relation $a$의 일차 lift를 $R_j=a_j-tc_j$로 두어 $t^3=0$ 아래에서 전개하면

$$\sum_jR_jF_j^{(2)}=t^2\left(\sum_ja_jh_j-\sum_jc_jg_j\right)$$

을 얻는다. 여기에 $R_j$를 $t^2s_j$만큼 보정하면 괄호 안에 $\sum_js_jf_j$를 더할 수 있으므로, relation을 이차까지 lift할 수 있는 조건은

$$\sum_jc_jg_j\equiv\sum_ja_jh_j\pmod{\mathfrak{a}}$$

이다. 오른쪽은 $h=(\bar{h}_1,\ldots,\bar{h}_m)\in\Hom_C(F\otimes_BC,C)$가 $d_2$를 따라 만드는 coboundary의 $a$에서의 값이므로, 모든 relation에 대하여 이 합동식을 만족시키는 $h_j$가 존재하는 것은 $[\eta]=0$인 것과 동치이고 바로 이때 이차 연장이 존재한다. $g_j$의 representative와 presentation을 바꾸어도 Lichtenbaum–Schlessinger complex 사이의 canonical homotopy equivalence 아래에서 같은 class를 얻으므로 $\operatorname{ob}(\xi)$는 $\xi$에만 의존한다.

::: 정리 8
$\xi\in T^1(C/A,C)$를 $A$ 위의 first-order deformation이라 하자. 그럼 $\xi$가 $A[t]/(t^3)$ 위의 flat deformation으로 연장되는 것을 막는 obstruction class

$$\operatorname{ob}(\xi)\in T^2(C/A,C)$$

가 자연스럽게 정의되며, $\xi$가 연장 가능한 것은 $\operatorname{ob}(\xi)=0$인 것과 동치이다. 더 일반적으로, $A$-algebra들의 square-zero extension $0\rightarrow \mathfrak{b}\rightarrow R'\rightarrow R\rightarrow0$과 $R$ 위의 deformation $C_R$에 대하여, $C_R$을 $R'$ 위로 연장하는 것에 대한 obstruction은 $T^2(C_R/R,C_R\otimes_R\mathfrak{b})$의 한 원소이고, 연장이 존재할 때 그 isomorphism class들은 $T^1(C_R/R,C_R\otimes_R\mathfrak{b})$ 위의 torsor를 이룬다.
:::
일반적인 square-zero extension $0\rightarrow \mathfrak{b}\rightarrow R'\rightarrow R\rightarrow0$에 대해서도 $t$의 거듭제곱 대신 $\mathfrak{b}$를 흔드는 방향으로 같은 계산을 반복하여 obstruction class를 얻으며, 연장이 존재할 때 두 연장의 차이에 [정리 5](#thm5)의 논증을 적용하면 그 isomorphism class들이 $T^1$ 위의 torsor를 이룬다.

Obstruction의 정체는 이렇게 명료하다. First-order deformation은 관계식을 일차까지 들어올린 뒤 남는 이차 잔여항 $-t^2\sum c_jg_j$를 만들고, 이 잔여항을 $h_j$의 선택으로 흡수할 수 있는지가 연장 가능성이며, 흡수의 실패를 $T^2$가 잰다. 여기서 잔여항이 관계식의 데이터로 표현되고, 그것이 trivial relation을 넘어서는 부분에서만 의미를 가지므로 $\operatorname{Rel}/\operatorname{TrivRel}$이 등장한 것이다. 이 obstruction을 반복적으로 소거하며 더 높은 차수로 deformation을 쌓아 올리면, 그 limit으로 complete local ring 위의 formal deformation을 얻는다 ([Ser]).

여기서부터는 이 계산을 full cotangent complex 전체로 옮긴다. $A$-algebra $C$를 한 번 polynomial algebra의 quotient로 나타내는 대신, 각 항이 polynomial $A$-algebra인 free simplicial resolution $P_\bullet\overset{\sim}{\rightarrow}C$를 택하고 각 degree에서 Kähler differential을 취한다. 그 결과인 simplicial $C$-module

$$\LL_{C/A}=\Omega_{P_\bullet/A}\otimes_{P_\bullet}C$$

을 chain complex로 본 것이 $C$의 $A$ 위 *cotangent complex<sub>여접 복합체</sub>*이다. Degree $0$에서는 generator의 differential이, degree $1$에서는 relation이, 그보다 높은 degree에서는 relation 사이의 relation과 그 higher coherence가 차례로 기록된다. 따라서 $\LL_{C/A}$는 일반적으로 모든 nonnegative degree에 항을 가지며, 앞에서 사용한 두 complex는 그 낮은 degree의 절단으로 되돌아온다.

$$\tau_{\leq1}\LL_{C/A}\simeq\NL_{C/A},\qquad \tau_{\leq2}\LL_{C/A}\simeq\operatorname{LS}_{C/A}$$

그러므로 지금까지 얻은 해석은 full cotangent complex에서도 그대로 유지된다. 모든 $C$-module $M$에 대하여

$$T^i(C/A,M)=\Ext^i_C(\LL_{C/A},M)$$

로 놓으면, $T^0$는 infinitesimal automorphism을, $T^1$은 first-order deformation과 연장이 존재할 때 그 선택들의 차이를, $T^2$는 연장의 obstruction을 통제한다. Naive cotangent complex와 Lichtenbaum–Schlessinger complex에서 계산한 $T^0,T^1,T^2$는 이 정의의 처음 세 항과 일치하므로, full cotangent complex는 앞의 이론을 폐기하지 않고 그 뒤에 higher degree를 이어 붙인다.

Taylor 차수를 올리는 과정에서도 매번 이 같은 세 항이 다시 나타난다. $A_n=A[t]/(t^{n+1})$로 놓으면 $A_{n+1}\rightarrow A_n$의 kernel $I_n=(t^{n+1})/(t^{n+2})$은 square-zero ideal이다. 따라서 $A_n$ 위의 deformation $C_n$을 $A_{n+1}$ 위로 연장하는 obstruction은

$$T^2(C_n/A_n,C_n\otimes_{A_n}I_n)$$

에 놓이고, 이것이 $0$일 때 연장들의 isomorphism class는 $T^1(C_n/A_n,C_n\otimes_{A_n}I_n)$ 위의 torsor를 이루며 infinitesimal automorphism은 $T^0(C_n/A_n,C_n\otimes_{A_n}I_n)$이 기록한다. 따라서 $n$차 연장에 $T^n$이 새로 대응하는 것이 아니라, base를 한 차수씩 두껍게 할 때마다 $T^0,T^1,T^2$의 deformation–obstruction 구조가 반복된다. 서로 호환되는 연장을 모든 $n$에 대하여 고르는 것이 formal deformation을 구성하는 일이다.

더 높은 $T^i$는 Taylor 전개의 $t^i$항을 직접 분류하는 공간이 아니라, $C$의 방정식 뒤에 놓인 higher relation과 coherence를 재는 André–Quillen cohomology이다. 이 항들까지 보존해야 ring morphism의 chain $A\rightarrow B\rightarrow C$에 대하여 distinguished triangle

$$\LL_{B/A}\otimes_B^{\mathbb{L}}C\longrightarrow\LL_{C/A}\longrightarrow\LL_{C/B}\longrightarrow\LL_{B/A}\otimes_B^{\mathbb{L}}C[1]$$

이 성립하고, 여기서 나오는 long exact sequence가 모든 $T^i$를 연결한다. Base change에서도 ordinary tensor를 derived tensor로 바꾸어야 같은 구조가 보존된다. 한 presentation에서 만든 유한 complex로는 relation의 처음 몇 층만 볼 수 있는 반면, full cotangent complex는 이 transitivity와 derived base change를 모든 degree에서 동시에 만족한다.

이제 [명제 2](#prop2)의 smoothness 판정을 full cotangent complex에 적용하면 deformation의 모든 degree에 대한 다음 결론을 얻는다.

::: 명제 9
$C$가 $A$ 위에서 smooth하면 모든 $C$-module $M$에 대하여

$$T^i(C/A,M)=0\qquad(i>0)$$

이다. 특히 $C$의 모든 first-order deformation은 trivial하고, 모든 square-zero lifting problem은 obstruction 없이 유일한 isomorphism class의 해를 가지며, 그 infinitesimal automorphism은 $T^0(C/A,C)=\Der_A(C,C)$가 분류한다.
:::
::: 증명
Smooth한 $C$의 cotangent complex $\LL_{C/A}$는 degree $0$의 $\Omega_{C/A}$에 quasi-isomorphic하고, 이 module이 projective이므로 모든 $i>0$에 대하여

$$T^i(C/A,M)=\Ext^i_C(\LL_{C/A},M)=\Ext^i_C(\Omega_{C/A},M)=0$$

이다. First-order deformation과 그 infinitesimal automorphism에 관한 주장은 [정리 5](#thm5)에 따르고, 일반적인 square-zero lifting에 관한 주장은 [정리 8](#thm8)에 따른다.
:::

$A$ 위의 affine lci algebra $C$에 대해서는 $\LL_{C/A}$가 두 projective module로 이루어진 naive cotangent complex와 quasi-isomorphic하므로 $T^i(C/A,M)=0$이 모든 $i\geq2$에서 성립한다. 따라서 각 단계의 obstruction은 사라지고 first-order deformation을 formal deformation으로 계속 연장할 수 있으며, 이러한 deformation 문제를 *unobstructed<sub>장애 없음</sub>*라 부른다. 일반적인 non-lci algebra에서는 $\LL_{C/A}$의 higher homology가 남을 수 있고, Lichtenbaum–Schlessinger complex는 그 가운데 고전적 deformation과 obstruction에 필요한 degree $2$까지를 보여 주며 full cotangent complex는 그 뒤의 higher relation까지 보존한다.

[예시 6](#ex6)의 $C=A[\x,\y]/(\x\y)$는 하나의 nonzerodivisor로 정의된 hypersurface이므로 이 경우에 해당한다. 따라서 $T^2(C/A,C)=0$이며, 그 예시에서 직접 구성한 고차 연장을 obstruction 이론으로도 설명할 수 있다.

## 예시

이제 $A=\mathbb{K}$가 field인 경우로 specialize하여, 구체적인 singular point들로 위 이론을 검증한다.

::: 예시 10 (세 좌표축)
$C=\mathbb{K}[\x,\y,\z]/\mathfrak{a}$, $\mathfrak{a}=(\x\y,\y\z,\z\x)$를 생각하자. 이는 $\mathbb{A}^3$의 세 좌표축의 합집합으로, 차원 $1$, codimension $2$이지만 ideal이 세 원소로 최소생성되므로 complete intersection이 아니며, 따라서 lci가 아니다. 이 singular point에서 $H_1(\NL_{C/\mathbb{K}})$이 $0$이 아님을 직접 확인한다.

$f_1=\x\y$, $f_2=\y\z$, $f_3=\z\x$라 하면, $\bar{d}:\mathfrak{a}/\mathfrak{a}^2\rightarrow C^3$는

$$\bar{d}(\bar{f}_1)=(\y,\x,0),\quad\bar{d}(\bar{f}_2)=(0,\z,\y),\quad\bar{d}(\bar{f}_3)=(\z,0,\x)$$

으로 주어진다 ($C^3=C \dd{\x}\oplus C \dd{\y}\oplus C \dd{\z}$). 이제 원소 $\x\cdot\bar{f}_2\in \mathfrak{a}/\mathfrak{a}^2$을 보자. $C$ 위에서 $\x\z=\x\y=0$이므로

$$\bar{d}(\x\cdot\bar{f}_2)=\x\cdot(0,\z,\y)=(0,\x\z,\x\y)=(0,0,0)$$

이어서 $\x\cdot\bar{f}_2\in\ker\bar{d}=H_1(\NL_{C/\mathbb{K}})$이다. 한편 $\x f_2=\x\y\z$는 degree $3$이고 $\mathfrak{a}^2$의 원소는 모두 degree $4$ 이상이므로 $\x\y\z\notin \mathfrak{a}^2$, 곧 $\x\cdot\bar{f}_2=\overline{\x\y\z}\neq0$이다. 따라서

$$H_1(\NL_{C/\mathbb{K}})\neq0,\qquad \overline{\x\y\z}\in H_1(\NL_{C/\mathbb{K}})$$

이다. 이 nonzero class는 conormal morphism $\bar{d}$의 왼쪽 끝 비단사성, 곧 conormal exact sequence를 왼쪽으로 연장했을 때 비로소 보이는 정보이며, $\Omega_{C/\mathbb{K}}$만으로는 결코 검출되지 않는다. ($\overline{\x\y\z}$는 세 generator 어느 쪽으로 보아도 같은 원소로서, $\z\cdot\bar{f}_1=\x\cdot\bar{f}_2=\y\cdot\bar{f}_3$이 모두 kernel에 속한다.) 이것이 naive 여접 복합체의 $H_1$이 smoothness의 실패 가운데 conormal morphism의 비단사성을 포착하는 가장 깨끗한 사례이다.
:::

::: 예시 11 (obstruction이 있는 deformation)
Obstruction이 실제로 $0$이 아닌 고전적 예는 rational normal quartic curve $C_4\subseteq\mathbb{P}^4$ 위의 affine cone

$$C=\mathbb{K}[\z_0,\z_1,\z_2,\z_3,\z_4]/\mathfrak{a},\qquad X=\Spec C,\qquad M=\begin{pmatrix}\z_0&\z_1&\z_2&\z_3\\\z_1&\z_2&\z_3&\z_4\end{pmatrix}$$

이다. 여기서 $\mathfrak{a}=I_2(M)$은 $M$의 $2\times2$ minor들로 생성되는 ideal이다. 이렇게 얻는 cone은 codimension $3$이고 그 vertex가 isolated singular point이다. Pinkham이 계산한 이 singular point의 semiuniversal deformation의 base는 한 점에서 만나는 두 component, 곧 차원 $3$인 성분과 차원 $1$인 성분으로 이루어져, base가 그 교점에서 singular하다. 이는 $T^1$의 어떤 접방향(한 component의 접방향에서 벗어난 방향)이 [정리 8](#thm8)의 의미에서 *obstructed*임을, 곧 그 first-order deformation을 이차로 연장할 때 $\operatorname{ob}(\xi)\neq0\in T^2(C/\mathbb{K},C)$임을 뜻한다.

Codimension $3$ 이상에서는 이러한 obstruction이 나타날 수 있는 반면, $\mathbb{P}^3$ 위 rational normal cubic의 cone과 같은 codimension $2$ Cohen–Macaulay singular point는 항상 unobstructed하여 base가 매끄럽다. 따라서 [예시 10](#ex10)처럼 lci가 아니어도 obstruction이 없을 수 있으며, "non-lci"와 "obstructed"는 서로 다른 현상이다. Obstruction의 유무는 $T^2$와 그 위에서 정의되는 이차 morphism $\operatorname{ob}$이 결정하는 것이지, $\Omega$나 $H_1(\NL)$만으로 읽히지 않는다. 이 예시의 명시적 계산은 ([Ser], [Har])를 참조하라.
:::

---

**참고문헌**

**[Ill]** L. Illusie, _Complexe cotangent et déformations I, II_, Lecture Notes in Mathematics 239, 283, Springer, 1971–1972.  
**[Har]** R. Hartshorne, _Deformation theory_, Graduate Texts in Mathematics 257, Springer, 2010.  
**[Ser]** E. Sernesi, _Deformations of algebraic schemes_, Grundlehren der mathematischen Wissenschaften 334, Springer, 2006.  
**[Stacks]** The Stacks project authors, _The Stacks project_, [stacks.math.columbia.edu](https://stacks.math.columbia.edu).
