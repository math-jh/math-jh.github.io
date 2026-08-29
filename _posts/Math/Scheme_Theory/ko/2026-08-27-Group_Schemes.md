---
title: "군 스킴"
description: "$\\Sch_{/S}$의 group object로 group scheme을 정의하고 functor of points가 group으로 값을 갖는다는 점별 서술과의 동치를 확인한 뒤, affine group scheme과 commutative Hopf algebra의 반대동치, representation과 comodule의 대응, torsor의 자명성 판정과 fppf-국소 자명성을 다룬다."
excerpt: "Group schemes, Hopf algebras, comodules, and torsors"

categories: [Math / Scheme Theory]
permalink: /ko/math/scheme_theory/group_schemes
sidebar: 
    nav: "scheme_theory-ko"

date: 2026-08-27
weight: 24

published: false

---

이제 우리는 $\Sch_{/S}$의 group object, 즉 *group scheme*을 정의한다. 

## 군 스킴

고전적으로 algebraic group은 group 구조를 가진 variety로서, 곱셈과 역원이 morphism인 것으로 정의되었다. ([\[대수다양체\] §대수적 군, ⁋정의 1](/ko/math/algebraic_varieties/algebraic_groups#def1)) 이를 scheme의 세계로 옮기기 위하여 $\Sch_{/S}$의 categorical product와 terminal object를 사용한다. 곧 $\Sch_{/S}$를 cartesian monoidal category로 보고 그 안의 group object를 생각한다. 

::: 정의 1
Scheme $S$ 위의 *group scheme<sub>군 스킴</sub>*은 $\Sch_{/S}$의 group object이다. 즉 group scheme $G$는 structure morphism $\vartheta: G \rightarrow S$를 가진 $S$-scheme $G$으로서, 이 위에 정의된 세 $S$-morphism

$$\mu_G: G\times_SG \rightarrow G,\qquad \iota_G: G \rightarrow G,\qquad \epsilon_G: S \rightarrow G$$

이 함께 주어져서 [\[범주론\] §모노이드 대상, ⁋정의 3](/ko/math/category_theory/monoid_objects#def3)의 모든 조건들을 만족하는 것이다. 두 group scheme $G, H$ 사이의 *homomorphism*은 이 구조를 보존하는 $S$-morphism이다. 
:::

[정의 1](#def1)은 group scheme을 $\Sch_{/S}$ 내부의 구조로 규정한다. 한편, [§점함자](/ko/math/scheme_theory/functor_of_points)를 사용하면 이를 실제로 group으로 가져올 수 있는데, 임의의 test scheme $T$에 대해 정의된 $T$-point들의 집합 $G(T)$가 group이 되기 때문이다. 

::: 명제 2
$S$-scheme $G$가 group scheme이 되는 것은 적당한 functor $\widetilde{h}_G:(\Sch_{/S})^\op\rightarrow\Grp$가 주어져서 forgetful functor $U:\Grp\rightarrow\Set$과의 합성이 $G$의 functor of points $h_G$와 같아지는 것과 동치이다. 뿐만 아니라, 두 group scheme $G,H$ 사이의 $S$-morphism $\varphi:G\rightarrow H$가 group scheme homomorphism인 것과 각각의 $T$에 대하여 $\varphi_T:G(T)\rightarrow H(T)$가 group homomorphism인 것은 동치이다.
:::
::: 증명
[\[범주론\] §표현가능한 함자, ⁋정리 4](/ko/math/category_theory/representable_functors#thm4)에 의하여 Yoneda embedding $h_{(-)}:\Sch_{/S}\rightarrow\Fun((\Sch_{/S})^\op,\Set)$은 fully faithful하고, [§점함자, ⁋명제 7](/ko/math/scheme_theory/functor_of_points#prop7)에 의하여 finite product를 보존한다. 한편 functor category에서 group object의 구조는 pointwise하게 주어지므로, $h_G$ 위의 group object 구조는 $U\circ\widetilde{h}_G=h_G$인 functor $\widetilde{h}_G:(\Sch_{/S})^\op\rightarrow\Grp$와 같은 데이터이다. 따라서 Yoneda embedding의 fully faithfulness는 $G$ 위의 group object 구조와 이러한 functor $\widetilde{h}_G$를 일대일대응시키며, group object 사이의 morphism에도 같은 논의를 적용하면 마지막 주장도 따라온다.
:::

다음은 자주 등장하는 몇몇 예시들이다. 

::: 예시 3
다음은 모두 $\Spec \mathbb{Z}$ 위의 group scheme이다.

1. *Additive group<sub>덧셈군</sub>* $\mathbb{G}_a=\Spec \mathbb{Z}[\x]=\mathbb{A}^1$. [§점함자, ⁋명제 1](/ko/math/scheme_theory/functor_of_points#prop1)에 의하여 $\mathbb{G}_a(T)\cong \Gamma(T, \mathcal{O}_T)$이며, 여기에 ring $\Gamma(T, \mathcal{O}_T)$의 덧셈을 주면 group이 된다. 임의의 morphism이 유도하는 사상은 ring homomorphism이므로 덧셈을 보존하고, 따라서 functoriality가 성립한다.

2. *Multiplicative group<sub>곱셈군</sub>* $\mathbb{G}_m=\Spec \mathbb{Z}[\x, \x^{-1}]$. [§점함자, ⁋명제 3](/ko/math/scheme_theory/functor_of_points#prop3)에 의하여 $\mathbb{G}_m(T)\cong \Gamma(T, \mathcal{O}_T)^\times$이며, 여기에 가역원들의 곱셈을 준다.

3. *$n$-th roots of unity* $\mu_n=\Spec \mathbb{Z}[\x]/(\x^n-1)$. [§아핀스킴, ⁋정리 13](/ko/math/scheme_theory/affine_schemes#thm13)의 adjunction에 의하여 
    
    $$\mu_n(T)\cong \{a\in \Gamma(T, \mathcal{O}_T)\mid a^n=1\}$$
    
    이며, $a^n=1$이면 $a$가 가역이므로 이는 $\mathbb{G}_m(T)$의 subgroup이다.

4. *General linear group* $\GL_n=\Spec \mathbb{Z}[\x_{11},\ldots, \x_{nn}, \det{}^{-1}]$. 여기에서 $\det$은 행렬 $(\x_{ij})$의 determinant이며, 이를 가역으로 만든 localization을 취한 것이다. 행렬이 가역인 것과 그 determinant가 가역인 것이 동치이므로

   $$\GL_n(T)=\GL(n;\Gamma(T,\mathcal{O}_T))$$

   이다. ([\[환론\] §가역원과 영인자, ⁋예시 9](/ko/math/ring_theory/units_and_zero_divisors#ex9)) 특별히 $T=\Spec A$인 경우 $\GL_n(T)=\GL(n; A)$이다.

5. *Special linear group* $\SL_n=\Spec \mathbb{Z}[\x_{11},\ldots, \x_{nn}]/(\det-1)$. 각각의 $T$에 대하여

   $$\SL_n(T)=\SL(n;\Gamma(T,\mathcal{O}_T))$$

   이다. 위와 마찬가지로, 특별히 $T=\Spec A$인 경우 $\SL_n(T)=\SL(n; A)$이다.

6. *Constant group scheme*. 임의의 finite group $\Gamma$에 대하여, $\Gamma$의 원소들로 index된 $\Spec \mathbb{Z}$들의 disjoint union

   $$\underline{\Gamma}=\coprod_{\gamma\in\Gamma}\Spec\mathbb{Z}=\Spec\Bigl(\prod_{\gamma\in\Gamma}\mathbb{Z}\Bigr)$$

   을 생각하면, 임의의 scheme $T$에 대하여 $\underline{\Gamma}(T)$는 위상공간 $\lvert T\rvert$에서 discrete topology가 주어진 topological group $\Gamma$로 가는 locally constant function들의 군이다. 특히 $T$가 connected인 경우 $\underline{\Gamma}(T)\cong \Gamma$이다.
:::

위의 예시에서 각 경우의 group scheme의 구조는 [명제 2](#prop2)를 사용하여 얻어진 것으로, 해당 명제의 유용성을 증명한다. 뿐만 아니라, 위의 예시는 $\Spec \mathbb{Z}$ 위에서 정의한 것이지만 본질적으로 이는 모든 base $S$에서 정의한 것이다. [§스킴 사이의 사상, ⁋예시 4](/ko/math/scheme_theory/morphism_of_schemes#ex4) 이후에서 보았듯 $\Spec \mathbb{Z}$는 $\Sch$의 terminal object로서, 임의의 scheme $S$마다 유일한 structure morphism $p: S\rightarrow \Spec \mathbb{Z}$가 존재하며, 이것이 유도하는 base change morphism

$$p^\ast: \Sch\rightarrow \Sch_{/S};\qquad X\mapsto X\times_\mathbb{Z}S$$

을 생각할 수 있으며, 이를 통해 $\mathbb{Z}$ 위에서 정의된 group scheme $G$를 $G_S=p^\ast G$로 옮겨 $S$-scheme으로 볼 수 있기 때문이다. [명제 2](#prop2)의 관점에서 보자면, 이는  $\widetilde{h}_G: \Sch^\op\rightarrow \Grp$ 이전에 다음의 functor

$$p_\ast: \Sch_{/S}\rightarrow \Sch;\qquad (T\rightarrow S)\mapsto (T\rightarrow S\rightarrow \Spec\mathbb{Z})$$

의 opposite functor $p_\ast^\op$를 합성하여 $\widetilde{h}_{G_S}=\widetilde{h}_G\circ p_\ast^\op$로 정의한 것과 같으며, 이 둘이 같다는 것이 adjunction

$$\Hom_S(T, p^\ast G)\cong \Hom_\mathbb{Z}(p_\ast T, G)$$

에 의해 보장되는 것이다. 이러한 방식으로 얻어지는 relative group schemes over $S$는 아래첨자를 사용하여 $\mathbb{G}_{a,S}, \mathbb{G}_{m,S},\underline{\Gamma}_S,\mu_{n,S},\GL_{n,S},\SL_{n,S}$ 등으로 적고, 문맥상 base가 명확한 경우에는 첨자를 생략하고 $\mathbb{G}_a, \mathbb{G}_m, \underline{\Gamma}$ 등으로 적기로 한다.

한편 위의 예시에서 주어진 것들은 모두 affine group scheme들이며, 이들이 정의된 방식 또한 명확하다. 뿐만 아니라, $\mu_n$을 제외한 예시들이 affine space 위에서 smooth인 것도 쉽게 보일 수 있다. 우선 $\mathbb{G}_a$는 affine line 그 자체이므로 별도의 논증이 필요없으며, $\GL_n$은 $\det$이 정의하는 $n^2$-dimensional affine space의 open subscheme $D(\det)$이며 그 특수한 경우 $n=1$이 $\mathbb{G}_m$이다. 마지막으로 $\SL_n$의 경우, [\[선형대수학\] §행렬식의 존재성과 유일성, ⁋정리 12](/ko/math/linear_algebra/existence_and_uniqueness_of_determinant#thm12)의 Laplace expansion으로부터 $f=\det-1$의 $\x_{ij}$에 대한 편미분이 $(i,j)$ 방향의 cofactor $C_{ij}$임을 확인할 수 있다. 따라서 [§매끄러운 사상과 에탈 사상, ⁋정리 4](/ko/math/scheme_theory/smooth_and_etale_morphisms#thm4)에 의해 그 Jacobian은 다음의 $1\times n^2$ 행렬

$$J_f=(\partial f/\partial\x_{ij})_{i,j}=(C_{ij})_{ij}$$

로 주어진다. 이 때, $\SL_n$에 속하는 임의의 행렬에 대하여, 이 행렬의 $i$번째 행을 고정하고 Laplace expansion을 생각하면 항등식 $\sum_j\x_{ij}C_{ij}=1$이 성립하며 따라서 위 Jacobian의 성분들 중 $C_{i1},\ldots, C_{in}$이 생성하는 ideal이 전체 ring이 되므로 이는 모든 점에서 full rank를 가지고, 따라서 $\SL_n$은 그 base 위에서 relative dimension $n^2-1$의 smooth morphism이 된다. 

한편 $\mu_n$은 $n$이 base에서 가역이면 finite étale이다. 반면 characteristic $p$인 field $\mathbb{K}$ 위에서는 $\mu_p$와 $\alpha_p=\ker(\Frob:\mathbb{G}_a\rightarrow\mathbb{G}_a)$가 underlying topological space로는 한 점이지만 nonreduced인 *infinitesimal* group scheme이 된다. 이는 [§매끄러운 사상과 에탈 사상, ⁋예시 14](/ko/math/scheme_theory/smooth_and_etale_morphisms#ex14)에서 inseparable extension의 geometric fiber에 nontrivial thickening이 남아 étale하지 않았던 것과 같은 현상으로, characteristic $p$ 특유의 성질을 보여주는 또 다른 예시이다.

## 부분군 스킴

일반적으로 $S$ 위의 group scheme $G$의 *subgroup scheme*은 group scheme $H$와 group scheme homomorphism인 monomorphism $\iota:H\rightarrow G$의 데이터이며, 특히 $\iota$가 closed embedding이면 이를 *closed subgroup scheme*이라 부른다. [\[리 이론\] §리 군, ⁋정리 5](/ko/math/lie_theory/Lie_groups#thm5)가 Lie group의 closed subgroup에 canonical Lie group structure를 주듯, group scheme에서도 주로 다루는 algebraic subgroup들은 closed subgroup scheme으로 나타난다. 예를 들어 group scheme homomorphism을 정의하고 나면 가장 먼저 살펴보는 것은 그 kernel이다. Group의 kernel은 항등원의 preimage이므로, scheme의 언어에서 이는 identity morphism을 따른 fiber product가 된다.

::: 정의 4
$S$ 위의 group scheme homomorphism $\varphi:G\rightarrow H$에 대하여 그 *kernel*을 fiber product

$$\ker \varphi=G\times_{\varphi, H, \epsilon_H}S$$

으로 정의한다. 여기에서 $\epsilon_H:S\rightarrow H$는 [정의 1](#def1)의 identity morphism이다.
:::

[§점함자, ⁋명제 7](/ko/math/scheme_theory/functor_of_points#prop7)로 계산하면 각각의 $S$-scheme $T$에 대하여

$$(\ker \varphi)(T)=G(T)\times_{H(T)}S(T)=\{g\in G(T)\mid \varphi_T(g)=\epsilon_{H,T}\}$$

이므로, 이 정의는 통상적인 kernel의 정의를 그대로 옮긴 것이다. 우변이 $G(T)$의 subgroup이고 그 대응이 $T$에 대해 자연스러우므로, [명제 2](#prop2)에 의하여 $\ker \varphi$는 group scheme이다. 남는 것은 $\ker \varphi \rightarrow G$가 closed embedding인지의 여부인데, 이는 $\epsilon_H$가 closed embedding인 것에 달려 있고 그 조건이 곧 separatedness이다. ([§값매김환, ⁋정의 3](/ko/math/scheme_theory/valuative_criteria#def3))

::: 명제 5
$S$ 위의 group scheme homomorphism $\varphi: G \rightarrow H$에 대하여, $H \rightarrow S$가 separated이면 $\ker \varphi$는 $G$의 closed subgroup scheme이다.
:::
::: 증명
먼저 closed embedding은 base change에 대해 보존된다. ([§닫힌 부분스킴, ⁋명제 3](/ko/math/scheme_theory/closed_subschemes#prop3)) 이제 $\vartheta_H:H\rightarrow S$를 structure morphism이라 하고, 다음의 diagram을 생각하자.

{% diagram Math/Scheme_Theory/Group_Schemes-1.svg width="11.23em" alt="section_as_base_change" %}

여기서 $\epsilon_H$가 $\vartheta_H$의 section이므로 $\vartheta_H\circ\epsilon_H=\id_S$이고, 따라서

$$(\epsilon_H\circ \vartheta_H,\id_H)\circ\epsilon_H=(\epsilon_H\circ \vartheta_H\circ\epsilon_H,\epsilon_H)=(\epsilon_H,\epsilon_H)=\Delta_{H/S}\circ\epsilon_H$$

이므로 이 사각형은 commute한다. 뿐만 아니라, 임의의 scheme $T$와 morphism $a,b:T\rightarrow H$에 대하여

$$(\epsilon_H\circ \vartheta_H,\id_H)\circ a=\Delta_{H/S}\circ b \iff(\epsilon_H\circ \vartheta_H\circ a,a)=(b,b) \iff a=b=\epsilon_H\circ \vartheta_H\circ a$$

이므로 $a=b=\epsilon_H\circ t$이도록 하는 $t$는 $\vartheta_H\circ a$로 유일하게 결정된다. 즉, 위 diagram은 Cartesian이며, 왼쪽의 $\epsilon_H$는 $\Delta_{H/S}$의 base change이다. 이제 $\vartheta_H$가 separated이므로 $\Delta_{H/S}$는 closed embedding이고, 따라서 $\epsilon_H$도 closed embedding이다. 다시 $\ker\varphi\rightarrow G$는 $\epsilon_H$를 $\varphi$를 따라 base change한 것이므로 closed embedding이다. 위에서 이미 $\ker\varphi$가 group scheme임을 확인하였으므로 이는 $G$의 closed subgroup scheme이다.
:::

Affine scheme 사이의 morphism은 항상 separated이므로 ([§값매김환, ⁋보조정리 5](/ko/math/scheme_theory/valuative_criteria#lem5)), affine base 위의 affine group scheme에 대해서는 [명제 5](#prop5)의 가정이 자동으로 성립한다. 가장 중요한 예시 중 하나는 $n$제곱 morphism $(-)^n:\mathbb{G}_m \rightarrow \mathbb{G}_m$, 곧 각각의 $T$에서 $a\mapsto a^n$인 homomorphism이다. 공역의 좌표를 $\y$로 적으면 이는 ring 수준에서 $\y\mapsto \x^n$에 대응하고, 항등원 morphism은 $\y\mapsto 1$인 counit에 대응하므로

$$\ker(-)^n=\Spec\left(\mathbb{Z}[\x,\x^{-1}]\otimes_{\mathbb{Z}[\y,\y^{-1}]}\mathbb{Z}\right)=\Spec \mathbb{Z}[\x,\x^{-1}]/(\x^n-1)=\Spec \mathbb{Z}[\x]/(\x^n-1)=\mu_n$$

이다. ([§올곱, ⁋보조정리 2](/ko/math/scheme_theory/fiber_products#lem2)) 여기에서 $\mathbb{Z}=\mathbb{Z}[\y,\y^{-1}]/(\y-1)$이므로 tensor product는 $\x^n-1$이 생성하는 ideal로 나눈 quotient가 되고, 여기에서는 $\x$가 이미 가역이므로 localization을 떼어낼 수 있다. 즉 $\mu_n$은 $\mathbb{G}_m$의 closed subgroup scheme이다.

## 호프 대수

이제 base와 group scheme 자신이 모두 affine인 경우를 보자. $G=\Spec B$, $S=\Spec A$라 하면 $\Spec$은 contravariant이므로 [정의 1](#def1)의 세 morphism $\mu_G,\epsilon_G,\iota_G$는 coordinate ring 위에서 방향이 뒤집힌 $A$-algebra homomorphism

$$\Delta:B\rightarrow B\otimes_AB,\qquad \epsilon:B\rightarrow A,\qquad \iota:B\rightarrow B$$

으로 나타난다. Group object의 결합법칙·항등원·역원 조건도 각각 coassociativity·counit·antipode 조건으로 뒤집히는데, 우리는 마침 이러한 대상을 정의한 적이 있다. ([\[범주론\] §모노이드 대상, ⁋정의 7](/ko/math/category_theory/monoid_objects#def7)) 그럼 symmetric monoidal category $(\rMod{A},\otimes_A,A)$의 Hopf monoid object를 *Hopf algebra<sub>호프 대수</sub>*라고 부르며, 우리가 다루는 경우에서는 $B$가 commutative ring이라 가정하면 충분하다. 그럼 다음을 기대하는 것이 자연스럽다.

::: 정리 6
Ring $A$에 대하여, $\Spec$은 commutative Hopf $A$-algebra들의 category와 $\Spec A$ 위의 affine group scheme들의 category 사이의 anti-equivalence를 준다. 이 대응 아래에서 $\Delta,\epsilon,\iota$는 각각 $\mu_G,\epsilon_G,\iota_G$에 대응한다.
:::
::: 증명
[§아핀스킴, ⁋정리 13](/ko/math/scheme_theory/affine_schemes#thm13)에 의하여 commutative $A$-algebra들과 $\Spec A$ 위의 affine scheme들은 anti-equivalent이고, 이 대응은 tensor product와 $A$를 각각 fiber product와 terminal object로 옮긴다. ([§올곱, ⁋보조정리 2](/ko/math/scheme_theory/fiber_products#lem2)) 따라서 [정의 1](#def1)의 데이터 $\mu_G,\epsilon_G,\iota_G$는 arrow를 뒤집으면 위의 데이터 $\Delta,\epsilon,\iota$가 된다. 이 동치가 합성과 항등사상을 보존하므로 group object의 세 공리는 각각 Hopf algebra의 세 공리로 옮겨지고, 같은 논리를 구조를 보존하는 morphism에 적용하면 주장한 anti-equivalence를 얻는다.
:::

특히 affine group scheme $G=\Spec B$와 임의의 $A$-algebra $E$에 대하여, $G$의 $E$-point들의 group $G(E)=\Hom_{\cAlg{A}}(B,E)$의 구조는 $B$의 Hopf algebra structure로 완벽하게 설명할 수 있다. 즉, 곱셈은 $g\ast h=\mu_E\circ(g\otimes h)\circ\Delta$, 항등원은 $\eta_E\circ\epsilon$, 역원은 $g\mapsto g\circ\iota$로 정의하면 되고, 여기서 $\mu_E:E\otimes_AE\rightarrow E$는 곱셈이고 $\eta_E:A\rightarrow E$는 structure morphism이다.

## 군 스킴의 표현론

한편 group object를 다룰 때 유용한 도구는 표현론으로, 우리는 [\[표현론\] §유한군의 표현론, ⁋명제 4](/ko/math/representation_theory/representations_of_finite_groups#prop4)에서 ordinary group $G$의 representation을 group algebra 위의 module, 곧 $G$-module로 해석하였고, 이 관점은 Lie group의 representation에서도 유용하게 사용되었다. Group scheme에서도 이를 살펴보는 것이 타당한 일일 것이다.

이를 위해서는 [예시 3](#ex3)에서 그러했듯 임의의 $S$-scheme $p:T\rightarrow S$마다 어떤 $\mathcal{O}_T$-module $\mathcal{E}_T$ 위의 작용을 생각하고, 이것이 $S$-morphism $\varphi: T'\rightarrow T$를 통한 pullback과 compatible하도록 하면 된다. 이를 묶어주기 위해서는 $\mathcal{O}_S$-module $\mathcal{E}$를 하나 고정한 후, 모든 $p:T\rightarrow S$에 대하여 $\mathcal{E}_T=p^\ast \mathcal{E}$로 두면 된다.

그럼 이제 이렇게 정의된 $\mathcal{E}_T$가 $G(T)$-module이라는 것은 group homomorphism

$$\varrho_T:G(T)\rightarrow \Aut_{\mathcal{O}_T}(\mathcal{E}_T)$$

이 주어진 것이다. 이제 이것이 위와 같은 방식으로 pullback과 compatible하기 위해서는 이러한 homomorphism들이 $T$에 대해 natural해야 한다. 이 조건을 제대로 쓰기 위해서는 $S$의 group scheme $G$와, $S$ 위에 정의된 $\mathcal{O}_S$-module $\mathcal{E}$에 대하여 다음의 group-valued functor

$$\rAut(\mathcal{E}): (\Sch_{/S})^\op\rightarrow\Grp,\qquad T\mapsto\Aut_{\mathcal{O}_T}(\mathcal{E}_T)$$

를 생각한 후, 이들 사이의 morphism (즉 natural transformation) $\widetilde{\rho}: \widetilde{h}_G\Rightarrow\rAut(\mathcal{E})$을 주면 되며, 그럼 위에서 설명한 것과 마찬가지로 $\widetilde{\rho}$의 $T$-component가 바로 앞에서 요구한 group homomorphism $\varrho_T$이다.

이제 [\[범주론\] §표현가능한 함자](/ko/math/category_theory/representable_functors)의 결과들을 적용하기 위해, 이들 두 functor 각각에 forgetful functor $U: \Grp\rightarrow\Set$를 합성하고, 이를 통해 $\widetilde{\rho}:\widetilde{h}_G\Rightarrow \rAut(\mathcal{E})$를 두 $\Set$-valued functor $h_G = \Hom_S(-, G)$와 $F = U \circ \rAut(\mathcal{E})$ 사이의 natural transformation $\rho: h_G \Rightarrow F$로 보자. 즉 각각의 $S$-scheme $T$에 대하여, $\rho_T$는 group homomorphism $\widetilde{\rho}_T:G(T)\rightarrow \Aut_{\mathcal{O}_T}(\mathcal{E}_T)$를 underlying set들 사이의 함수로 생각한 것이다. 그럼 [\[범주론\] §표현가능한 함자, ⁋정리 4](/ko/math/category_theory/representable_functors#thm4)에 의하여 $\rho$는 universal element $\id_G\in h_G(G)$에서의 값

$$\lambda:=\rho_G(\id_G)\in F(G)=\Aut_{\mathcal{O}_G}(\mathcal{E}_G)$$

하나로 완전히 결정된다. 여기에서 $\vartheta:G\rightarrow S$에 대해 $\mathcal{E}_G=\vartheta^\ast\mathcal{E}$이다. 실제로 임의의 $S$-scheme $T$와 $T$-point $g\in G(T)=\Hom_S(T, G)$에 대하여, 다음의 diagram

{% diagram Math/Scheme_Theory/Group_Schemes-2.svg width="9.23em" alt="naturality" %}

을 생각하면

$$\varrho_T(g)=\rho_T(g)=\rho_T(g^\ast\id_G)=g^\ast(\rho_G(\id_G))=g^\ast\lambda$$

이므로 임의의 $g\in G(T)$의 작용 $\varrho_T(g)$는 이 하나의 automorphism $\lambda$의 pullback으로 복원된다.

문제는 [\[범주론\] §표현가능한 함자, ⁋정리 4](/ko/math/category_theory/representable_functors#thm4)는 $\Set$-valued functor들에 대한 결과이므로, <em-ko>임의의</em-ko> $\lambda\in\Aut_{\mathcal{O}_G}(\mathcal{E}_G)$에 대하여 위의 방식으로 정의된 함수 $\varrho_T: G(T)\rightarrow \Aut_{\mathcal{O}_T}(\mathcal{E}_T)$는 집합들 사이의 함수일 뿐, 자동으로 group homomorphism이 되지는 않는다는 것이다. 다행히 $\varrho_T$가 group homomorphism이도록 하는 조건은 명시적으로 쓸 수 있으며, 이는 다음과 같이 $\lambda$에 대한 두 조건으로 번역된다.

1. 우선 임의의 $g, h\in G(T)$에 대하여 $gh=\mu_G\circ(g, h)$이므로, 조건 $\varrho_T(gh)=\varrho_T(g)\circ\varrho_T(h)$은 다음의 조건 
    
    $$(g, h)^\ast(\mu_G^\ast\lambda)=(g, h)^\ast(\pr_1^\ast\lambda\circ\pr_2^\ast\lambda)$$
    
    와 같다. 이것이 모든 $T$와 $(g, h)$에 대해 성립해야 하므로, universal pair $(g, h)=\id_{G\times_S G}$를 대입하면 $G\times_SG$ 위에서 다음의 식
    
    $$\mu_G^\ast\lambda=\pr_1^\ast\lambda\circ\pr_2^\ast\lambda$$
    
    를 만족해야 한다.
2. 다음으로, $G(T)$의 항등원은 $e_T=\epsilon_G\circ \vartheta_T$이므로 조건 $\varrho_T(e_T)=\id_{\mathcal{E}_T}$은 다음의 조건 
    
    $$\vartheta_T^\ast(\epsilon_G^\ast\lambda)=\id_{\mathcal{E}_T}$$
    
    와 같다. 여기에 $T=S, \vartheta_T=\id_S$를 대입하면 $S$ 위에서 
    
    $$\epsilon_G^\ast\lambda=\id_\mathcal{E}$$
    
    를 만족해야 한다.

이러한 두 조건을 만족하는 $\mathcal{O}_G$-module automorphism

$$\lambda:\vartheta^\ast\mathcal{E}\xrightarrow{\sim}\vartheta^\ast\mathcal{E}$$

을 $\mathcal{E}$의 *$G$-linearization*이라 부른다. 이 때, 이 두 조건은 각각 universal pair $\id_{G\times_S G}$와 $\id_S$에서 얻어진 것이므로, 임의의 $S$-scheme $T$와 $g, h\in G(T)$에 대하여는 $(g, h)^\ast$ 및 $\vartheta_T^\ast$를 취해 pullback하면 원래의 group homomorphism의 조건들이 복원된다. 즉, $G$-linearization을 주는 것과 $G$의 representation을 주는 것은 정확히 같은 데이터이다. 특히 $\mathcal{E}$가 finite locally free이면 $\rAut(\mathcal{E})$는 general linear group scheme $\GL(\mathcal{E})$로 represent되므로, 이 데이터는 group scheme homomorphism $G\rightarrow\GL(\mathcal{E})$와 같으며, 이러한 이유에서 이를 *linearization*이라 부른다. 

이제 우리는 특별히 $S=\Spec A$인 상황을 본다. 그럼 특히 quasi-coherent $\mathcal{O}_S$-module $\mathcal{E}$는 어떤 $A$-module $V$에서 나오는 것이므로 $\mathcal{E}=\widetilde{V}$라 할 수 있다. 이 상황에서 위의 정의들을 다시 풀어보면, affine test scheme $\vartheta_T:T=\Spec E\rightarrow S$에 대해서는

$$\vartheta_T^\ast\mathcal{E}\cong\widetilde{V\otimes_AE},\qquad \Aut_{\mathcal{O}_T}(\vartheta_T^\ast\mathcal{E})\cong\Aut_E(V\otimes_AE)$$

가 된다. 이를 대수적으로 풀어쓰면 다음과 같다. 

::: 정의 7
Ring $A$와 $A$-module $V$가 주어졌다 하고, $\Spec A$ 위의 group scheme $G$가 주어졌다 하자. 그럼 $G$의 $V$ 위로의 *linear representation<sub>선형표현</sub>*이란 각각의 $A$-algebra $E$마다 group homomorphism

$$\varrho_E: G(E) \rightarrow \Aut_E(V\otimes_AE)$$

이 주어지고 이것이 $E$에 대해 자연스러운 것이다. 두 representation $(V, \varrho)$와 $(W, \varrho')$ 사이의 *morphism*은 $A$-linear map $u: V \rightarrow W$로서, 각각의 $E$와 $g\in G(E)$에 대하여 $\varrho'_E(g)\circ(u\otimes\id_E)=(u\otimes\id_E)\circ\varrho_E(g)$인 것이다.
:::

여기에서 $\varrho$의 naturality는 임의의 $A$-algebra homomorphism $\phi: E \rightarrow E'$에 대하여 다음의 diagram

{% diagram Math/Scheme_Theory/Group_Schemes-3.svg width="36.16em" alt="naturality of representation" %}

이 commute한다는 것이다. 

이제 $G=\Spec B$라 하면, 위의 정의에서 $G$-module 구조를 대수적인 언어, 즉 $B$의 언어로 표현할 수 있다. 물론 이 과정에서 $\Spec$의 contravariance에 의해, 우리는 *comodule* structure를 고려해야 한다. 

::: 정의 8
Hopf $A$-algebra $B$에 대하여, $B$-*comodule<sub>쌍대모듈</sub>*이란 $A$-module $V$와 $A$-linear map $\rho: V \rightarrow V\otimes_AB$로서, 다음 두 조건을 만족하는 것이다.

1. $(\rho\otimes\id_B)\circ\rho=(\id_V\otimes\Delta)\circ\rho$.
2. Identification $V\otimes_AA\cong V$ 아래에서 $(\id_V\otimes\epsilon)\circ\rho=\id_V$.

두 comodule 사이의 *morphism*은 $A$-linear map $u: V \rightarrow W$로서 $\rho_W\circ u=(u\otimes\id_B)\circ\rho_V$인 것이다.
:::

두 조건은 Hopf algebra의 coassociativity와 counit 조건을 $V$가 받아들이는 형태로 옮긴 것이며, $V=B$이고 $\rho=\Delta$인 경우가 자명한 예이다. 그럼 다음 정리도 기대함직하다. 

::: 정리 9
Ring $A$ 위의 affine group scheme $G=\Spec B$와 $A$-module $V$에 대하여, $G$의 $V$ 위로의 linear representation과 $V$ 위의 $B$-comodule 구조는 서로 일대일대응한다. 더 나아가, 이는 이들 category 사이의 equivalence를 준다.
:::
::: 증명
[§아핀스킴, ⁋정리 13](/ko/math/scheme_theory/affine_schemes#thm13)에 의하여 임의의 $A$-algebra $E$에 대해 $G(E)=\Hom_{\cAlg{A}}(B, E)$이고, [정리 6](#thm6) 직후에 적은 대로 그 group 구조는 $g\ast h=\mu_E\circ(g\otimes h)\circ\Delta$, 항등원 $\eta_E\circ\epsilon$, 역원 $g\circ\iota$로 주어진다.

Representation $\{\varrho_E\}_E$가 주어졌다 하자. Universal element $\id_B\in G(B)$를 택하여 $\sigma=\varrho_B(\id_B)$라 하고

$$\rho: V \rightarrow V\otimes_AB;\qquad \rho(v)=\sigma(v\otimes 1)$$

로 정의한다. 임의의 $g\in G(E)$는 $A$-algebra homomorphism $g:B\rightarrow E$이고 $G(g)(\id_B)=g$이므로, naturality에 의하여

$$\varrho_E(g)(v\otimes 1)=(\id_V\otimes g)(\rho(v))\tag{$\ast$}$$

를 얻으므로 representation 전체가 $\rho$ 하나로 복원된다. 이 식을 항등원 $\epsilon\in G(A)$과 두 universal element $b\mapsto b\otimes 1,1\otimes b$의 곱에 적용하면, group action의 항등원 조건과 결합법칙은 각각 $\rho$의 counit 조건과 coassociativity가 된다.

거꾸로 comodule structure $\rho$가 주어지면 $(\ast)$의 우변으로 $\varrho_E(g)$를 정의하고 $E$-linear map으로 확장할 수 있다. Coassociativity와 counit 조건은 각각 $\varrho_E(g)\circ\varrho_E(h)=\varrho_E(g\ast h)$와 $\varrho_E(\eta_E\circ\epsilon)=\id$을 주며, antipode 조건에 의하여 $\varrho_E(g\circ\iota)$가 $\varrho_E(g)$의 inverse가 된다. Naturality도 $(\ast)$에서 바로 따라오므로 $\{\varrho_E\}_E$는 representation이고, 두 구성이 서로 역인 것과 morphism 조건의 대응도 같은 식에서 따라온다.
:::

가장 기본적인 경우는 다음과 같다.

::: 예시 10
우리는 [정리 9](#thm9)를 이용해 torus $\mathbb{G}_m=\Spec A[\x,\x^{-1}]$의 linear representation을 분류한다. 우리 주장은 $\mathbb{G}_m$의 $V$ 위로의 representation은 $V$의 $\mathbb{Z}$-grading

$$V=\bigoplus_{n\in \mathbb{Z}}V_n$$

과 일대일대응한다는 것이다. 

우선 임의의 $A$-linear map $\rho: V \rightarrow V\otimes_AB$는 $B$의 기저 $\{\x^n\}_{n\in \mathbb{Z}}$에 대하여 유일하게

$$\rho(v)=\sum_{n\in\mathbb{Z}}\rho_n(v)\otimes\x^n$$

꼴로 전개된다. 여기서 각 $\rho_n: V \rightarrow V$는 $A$-linear map이고, 각 $v\in V$마다 $0$이 아닌 $\rho_n(v)$는 유한개뿐이다.

이제 $\rho$가 [정의 8](#def8)의 comodule 조건을 만족할 필요충분조건을 구해보자. 우선 counit 조건의 경우, identification $V\otimes_AA\cong V$ 아래에서 $(\id_V\otimes\epsilon)\circ\rho=\id_V$이어야 하므로

$$v=(\id_V\otimes\epsilon)(\rho(v))=(\id_V\otimes\epsilon)\left(\sum_{n\in\mathbb{Z}}\rho_n(v)\otimes\x^n\right)=\sum_{n\in\mathbb{Z}}\rho_n(v)\epsilon(\x^n)=\sum_{n\in\mathbb{Z}}\rho_n(v)$$

이어야 한다. 이것이 모든 $v\in V$에 대해 성립하므로 $\sum_{n\in\mathbb{Z}}\rho_n=\id_V$를 얻는다. Coassociativity 조건 $(\rho\otimes\id_B)\circ\rho=(\id_V\otimes\Delta)\circ\rho$의 경우, 좌변과 우변을 각각 계산하면

$$\begin{aligned}(\rho\otimes\id_B)(\rho(v))&=(\rho\otimes\id_B)\left(\sum_{n\in\mathbb{Z}}\rho_n(v)\otimes\x^n\right)=\sum_{m, n\in\mathbb{Z}}\rho_m(\rho_n(v))\otimes\x^m\otimes\x^n,\\ (\id_V\otimes\Delta)(\rho(v))&=(\id_V\otimes\Delta)\left(\sum_{k\in\mathbb{Z}}\rho_k(v)\otimes\x^k\right)=\sum_{k\in\mathbb{Z}}\rho_k(v)\otimes\x^k\otimes\x^k\end{aligned}$$

이다. $B\otimes_AB$의 basis $\{\x^m\otimes\x^n\}_{m, n\in\mathbb{Z}}$는 일차독립이므로, 양변의 계수를 비교하면 $m=n$인 곳에서 조건 $\rho_n\circ\rho_n=\rho_n$를, 나머지 $m\neq n$인 곳에서는 $\rho_m\circ\rho_n=0$임을 안다. 즉 $\{\rho_n\}_{n\in\mathbb{Z}}$는 합이 $\id_V$인 pairwise orthogonal idempotent들의 family이며, 이들을 이용하여 $n\in\mathbb{Z}$마다 $V_n:=\rho_n(V)=\{v\in V\mid \rho(v)=v\otimes\x^n\}$으로 정의하면, $V$는 direct sum decomposition

$$V=\bigoplus_{n\in\mathbb{Z}}V_n$$

을 가진다. 거꾸로 이러한 $\mathbb{Z}$-grading이 주어지면, 각 $v=\sum_n v_n$ ($v_n\in V_n$)에 대해 $\rho(v)=\sum_n v_n\otimes\x^n$으로 정의했을 때 위의 계산을 역으로 거쳐 $\rho$가 $B$-comodule 구조를 줌을 알 수 있다.

이제 이를 통해 $B$-comodule structure가 완전히 분류되었으므로, 남은 것은 이를 기하적인 언어 $\varrho$로 옮기는 것이다. 우리는 임의의 $A$-algebra $E$에 대하여 

$$\mathbb{G}_m(E)=\Hom_{\cAlg{A}}(A[\x,\x^{-1}], E)\cong E^\times$$

임을 이미 살펴보았으며, 이 때 unit $u\in E^\times$는 $\x\mapsto u$로 정의되는 $A$-algebra homomorphism $g_u: A[\x,\x^{-1}]\rightarrow E$에 대응한다. 이때 $g_u(\x^n)=u^n$이므로, $v\in V_n$에 대하여 $(\ast)$의 식은

$$\varrho_E(u)(v\otimes 1)=(\id_V\otimes g_u)(\rho(v))=(\id_V\otimes g_u)(v\otimes\x^n)=v\otimes g_u(\x^n)=u^n(v\otimes 1)$$

이 된다. 즉 $E$-linearity에 의하여, $u\in\mathbb{G}_m(E)=E^\times$는 $V_n\otimes_AE$의 원소 위에 정확히 $u^n$배로 작용한다.
:::

[예시 10](#ex10)의 $V_n$을 weight $n$의 부분이라 부르며, 이 분해는 torus의 작용을 다룰 때 표준적인 도구가 된다. Torus $\mathbb{G}_m^r$의 경우 같은 계산을 반복하면 grading이 $\mathbb{Z}^r$에 의해 매겨지며, 그 각각의 성분이 torus의 한 character에 대응한다.

## Torsor

우리가 group scheme을 생각하는 이유는 (당연히) scheme 위에 group action을 정의하기 위해서이다. 

::: 정의 11
$S$ 위에 정의된 group scheme $G$와, $S$-scheme $X$가 주어졌다 하자. 그럼 $G$의 $X$ 위로의 *left action*은 $S$-scheme morphism $\varrho: G\times_SX \rightarrow X$로서, 각각의 $S$-scheme $T$에 대하여 유도되는 map

$$\varrho_T: G(T)\times X(T) \rightarrow X(T)$$

이 $G(T)$의 집합 $X(T)$ 위로의 action인 것이다.
:::

그럼 다시 [명제 2](#prop2)의 정신에 의하여, 위의 조건은 정확히 group action이 가져야 할 다음의 두 조건

$$\varrho\circ(\mu_G\times\id_X)=\varrho\circ(\id_G\times\varrho),\qquad \varrho\circ(\epsilon_G\circ p, \id_X)=\id_X$$

이 성립하는 것과 동치이다. 여기에서 $p: X \rightarrow S$는 structure morphism이다. 

Scheme 위에 group action이 주어지면, 기하학적으로 자연스러운 다음 관심사는 orbit들의 공간, 곧 quotient $\overline{X}=X/G$와 quotient morphism $\varpi: X \rightarrow \overline{X}$를 구성하고 그 구조를 이해하는 것이다. 그러나 이는 위상공간에서조차 항상 기대되는 성질이 아니며, 우리는 적어도 이 action이 각 orbit 위에서 free, simply transitive하게 작동하기를 원한다. 이 경우 각 orbit의 점 $\overline{x}\in \overline{X}$ 위의 fiber $\varpi^{-1}(\overline{x})$는 $G$와 같은 모양을 가지게 되며, 이 경우 $X\rightarrow \overline{X}$를 $G$ 모양의 fiber들을 모아둔 것으로 해석할 수 있다. 이제 문제는 [\[대수적 위상수학\] §분류공간, ⁋정의 1](/ko/math/algebraic_topology/classifying_spaces#def1)에서와 비슷하게, 각각의 orbit마다 $G$의 항등원에 대응되는 기준점을 골라줄 수가 없다는 것으로, 이 때문에 각 fiber는 $G$ 자체가 아니라, $G$가 작용하는 방식만 기억하는 fiber가 된다. 

::: 정의 12
$S$ 위의 group scheme $G$와 left action $\varrho: G\times_SP \rightarrow P$를 가진 $S$-scheme $P$에 대하여, $P$가 *$G$-torsor*라는 것은 다음 두 조건이 성립하는 것이다.

1. $P \rightarrow S$는 faithfully flat, locally of finite presentation이다. ([§평탄사상, ⁋정의 1](/ko/math/scheme_theory/flat_morphisms#def1), [§스킴 사상의 성질들, ⁋정의 18](/ko/math/scheme_theory/properties_of_scheme_morphisms#def18))
2. Action과 projection이 유도하는 morphism

   $$(\varrho, \pr_2): G\times_SP \rightarrow P\times_SP$$

   이 isomorphism이다.

$G$-torsor $P$가 *trivial*하다는 것은, left translation action을 가진 $G$ 자신과 $G$-equivariant $S$-scheme isomorphism이 존재하는 것이다.
:::

둘째 조건은 각각의 test scheme마다

$$G(T)\times P(T) \rightarrow P(T)\times P(T);\qquad (g, q)\mapsto (g\cdot q, q)$$

이 bijection인 것, 즉 simply transitive 조건을 반영하는 것이다. 첫째 조건은 대략적으로는 local triviality를 잘 적기 위해 필요한 것인데, [§충실평탄하강](/ko/math/scheme_theory/faithfully_flat_descent)에서 보았듯 algebraic geometry에서는 Zariski open cover만으로는 충분한 정보를 담지 못하므로, $P \rightarrow S$ 자신이 *fppf covering*의 역할을 하도록 요구하는 것이다. 여기서 fppf는 *fidèlement plat de présentation finie*의 약자이다.

한편 [\[대수적 위상수학\] §분류공간, ⁋명제 2](/ko/math/algebraic_topology/classifying_spaces#prop2)에서와 마찬가지로, torsor의 (global한) triviality는 global section의 존재와 정확히 동치이다.

::: 명제 13
$S$ 위의 $G$-torsor $P$에 대하여, $P$가 trivial한 것과 $P(S)\neq \emptyset$인 것, 곧 $P \rightarrow S$가 section을 가지는 것은 동치이다.
:::
::: 증명
$P$가 trivial하면 $G$의 항등원 $\epsilon_G\in G(S)$에 대응하는 원소가 $P(S)$의 원소를 주므로 section이 존재한다.

거꾸로 section $s\in P(S)$가 주어졌다 하자. [\[대수적 위상수학\] §분류공간, ⁋명제 2](/ko/math/algebraic_topology/classifying_spaces#prop2)에서와 마찬가지로 합성

$$\varphi: G\cong G\times_SS\xrightarrow{\ \id_G\times s\ }G\times_SP\xrightarrow{\ \varrho\ }P$$

를 생각하면, 각각의 $S$-scheme $T$에서 $\varphi_T(g)=g\cdot s_T$이다. [정의 12](#def12)의 둘째 조건에 의하여 $g\mapsto g\cdot s_T$는 $G(T)$에서 $P(T)$로의 bijection이므로, [\[범주론\] §표현가능한 함자, ⁋정리 4](/ko/math/category_theory/representable_functors#thm4)에 의하여 $\varphi$는 isomorphism이다. 또 $\varphi_T(g'g)=(g'g)\cdot s_T=g'\cdot\varphi_T(g)$이므로 $\varphi$는 $G$-equivariant이며, 따라서 $P$는 trivial하다.
:::

[명제 13](#prop13)은 torsor가 원래의 base $S$ 위에서 trivial한지의 여부가 오로지 global section $S \rightarrow P$의 존재에 달려 있음을 말한다. 따라서 global section이 없는 torsor는 $S$ 위에서 결코 trivial하지 않다. 반면 torsor $P$를 사상 $P \rightarrow S$를 통해 자기 자신 위로 base change하면, diagonal morphism $\Delta: P \rightarrow P\times_SP$가 항상 section 역할을 해주므로 $P$ 위에서는 $P\times_SP \cong G\times_SP$로 언제나 trivial해진다. 이는 위상수학에서 principal bundle을 total space 위로 끌어올리면 항상 trivial해지는 것과 마찬가지 현상이다.

::: 명제 14
$S$ 위의 $G$-torsor $P$에 대하여 다음이 성립한다.

1. 둘째 projection $P\times_SP \rightarrow P$는 $P$ 위의 group scheme $G_P=G\times_SP$에 대한 torsor이며 trivial하다. 곧 $P$는 fppf covering $\{P \rightarrow S\}$ 위에서 자명해진다.
2. $G \rightarrow S$가 affine이고 $P \rightarrow S$가 quasi-compact이면 ([§스킴 사상의 성질들, ⁋정의 2](/ko/math/scheme_theory/properties_of_scheme_morphisms#def2)) $P \rightarrow S$ 또한 affine이다.
:::
::: 증명
1번을 보자. Flat, locally of finite presentation, surjective 성질과 fiber product의 isomorphism은 모두 base change에 대해 보존되므로 ([§평탄사상, ⁋명제 3](/ko/math/scheme_theory/flat_morphisms#prop3), [§올곱, ⁋명제 16](/ko/math/scheme_theory/fiber_products#prop16)), 둘째 projection $P\times_SP \rightarrow P$는 $P$ 위의 $G_P$-torsor이다. 그런데 diagonal morphism $\Delta: P \rightarrow P\times_SP$가 이 projection의 section이므로, [명제 13](#prop13)에 의하여 이 torsor는 trivial하다. 곧 $P$ 위에서 $P\times_SP\cong G\times_SP$이다. 한편 $P \rightarrow S$는 정의에 의하여 fppf covering이다.

2번을 보자. $S$의 affine open subset $V$를 택하면 $V$는 quasi-compact이고 ([§스펙트럼, ⁋보조정리 12](/ko/math/scheme_theory/spectrums#lem12)), $P \rightarrow S$가 quasi-compact이므로 그 preimage 또한 quasi-compact이다. 따라서 $\{P \rightarrow S\}$는 [§충실평탄하강, ⁋정의 9](/ko/math/scheme_theory/faithfully_flat_descent#def9)의 fpqc covering이 된다. 이제 affine은 base change에 대해 보존되므로 $G\times_SP \rightarrow P$는 affine이고, 1번에 의해 $P\times_SP \rightarrow P$ 역시 affine이다. Affine이라는 성질은 fpqc covering에 대해 base에서 국소적이므로 ([§충실평탄하강, ⁋명제 13](/ko/math/scheme_theory/faithfully_flat_descent#prop13)), $P \rightarrow S$ 자신이 affine이다.
:::

위의 증명에서 볼 수 있듯, [명제 14](#prop14)의 둘째 항에 붙은 quasi-compact 가정은 fppf covering $\{P \rightarrow S\}$를 fpqc covering으로 올리기 위한 것으로, 일반적으로 quasi-compact fppf covering은 항상 fpqc covering이다. 만일 $P$가 Noetherian scheme인 경우에는 [§스킴 사상의 성질들, ⁋명제 4](/ko/math/scheme_theory/properties_of_scheme_morphisms#prop4)에 의하여 fppf 사상이 자동으로 quasi-compact가 되어 이 가정이 언제나 성립한다.

직관적으로 [명제 14](#prop14)는 torsor $P$가 base $S$ 위에서는 $G$와 다를 수 있어도, fppf covering $\{P \rightarrow S\}$ 위로 올라가면 자명한 torsor $G\times_SP$가 된다는 것을 보여준다. 바꿔말하면, torsor는 [§충실평탄하강, ⁋정의 4](/ko/math/scheme_theory/faithfully_flat_descent#def4)의 descent datum을 통해 $G$를 fppf covering을 따라 붙여서 얻는 대상으로 이해할 수 있으며, $G$가 affine인 경우 [§충실평탄하강, ⁋정리 12](/ko/math/scheme_theory/faithfully_flat_descent#thm12)에 의하여 이러한 데이터가 실제로 $S$ 위의 scheme을 준다.

::: 예시 15
1. $S=\Spec\mathbb{R}$-scheme $p:P=\Spec \mathbb{C}\rightarrow S$를 생각하고, $\vartheta:G\rightarrow S$를 finite group $\mathbb{Z}/2$이 정의하는 constant group $S$-scheme 
    
    $$G=\underline{(\mathbb{Z}/2)}_S=S\amalg S=\Spec(\mathbb{R}\times\mathbb{R})$$
    
    을 생각하자. ([예시 3](#ex3)) 이는 두 점 집합이며 각각의 점들이 $\mathbb{R}$의 정보를 갖고 있는 group scheme이다. 이제 이것이 또 다른 한점집합인 $\Spec \mathbb{C}$ 위에 작용하는 상황을 본다. 이를 위해 complex conjugation을 $c$라 표기하면, 이 위의 group scheme action $\varrho: G\times_SP\rightarrow P$를 다음의 diagram

    {% diagram Math/Scheme_Theory/Group_Schemes-4.svg width="13.92em" alt="action_definition" %}

    으로 정의할 수 있다. 직관적으로 $\varrho$는 한 성분 $P$는 $\id_P$로 그대로 옮겨지되, 다른 성분 $P$는 $c$가 유도하는 사상으로 옮겨지는 것이다. 

    그럼 이는 $G$-torsor이다. 이를 위해 [정의 12](#def12)의 조건들을 확인해보면 우선  $\mathbb{C}$가 $\mathbb{R}$ 위의 rank $2$ free module이므로 $P \rightarrow S$는 faithfully flat이고 locally of finite presentation이다. 둘째 조건의 경우, $G\times_SP=\Spec(\mathbb{C}\times\mathbb{C})$이고 $P\times_SP=\Spec(\mathbb{C}\otimes_\mathbb{R}\mathbb{C})$인데, $\varrho$에 대응하는 algebra homomorphism을 대수적으로 써 보면 이는
    
    $$\rho:\mathbb{C}\rightarrow\mathbb{C}\times\mathbb{C};\qquad z\mapsto(z,\bar z)$$
    
    로 주어지는 것이다. 그럼 $(\varrho, \pr_2)$은 대수적으로

   $$\mathbb{C}\otimes_\mathbb{R}\mathbb{C} \rightarrow \mathbb{C}\times\mathbb{C};\qquad z\otimes w\mapsto (zw, \bar zw)$$

   이고, 이것이 $\mathbb{R}$-algebra isomorphism이므로 [정의 12](#def12)의 둘째 조건이 성립한다. 
   
   반면 $\mathbb{R}$-algebra homomorphism $\mathbb{C} \rightarrow \mathbb{R}$은 존재하지 않으므로 $P(S)=\emptyset$이고, [명제 13](#prop13)에 의하여 이 torsor는 trivial하지 않다.

2. Scheme $S$ 위의 invertible sheaf $\mathcal{L}$에 대하여, [\[대수적 위상수학\] §분류공간, ⁋명제 4](/ko/math/algebraic_topology/classifying_spaces#prop4)에서와 마찬가지로 우리는 $\mathcal{L}$을 trivialize하는 open cover $\{U_i\}$와 transition unit $g_{ij}\in \Gamma(U_i\cap U_j, \mathcal{O}_S^\times)$들을 통해 $\mathbb{G}_m$-torsor $P_\mathcal{L}$을 얻는다. Trivialization 사이의 좌표변환인 $g_{ij}$들은 $U_i\cap U_j\cap U_k$ 위에서 $g_{ij}g_{jk}=g_{ik}$를 만족하며, $\mathbb{G}_{m}\times_SU_i$들을 겹침 위에서 $(t, u)\mapsto (g_{ij}(u)t, u)$로 붙이면 [§스킴, ⁋보조정리 9](/ko/math/scheme_theory/schemes#lem9)에 의하여 $S$-scheme $P_\mathcal{L}$이 구성된다. $P_\mathcal{L}$의 section은 어디서도 소멸하지 않는 $\mathcal{L}$의 global section이므로, [명제 13](#prop13)에 의하여 $P_\mathcal{L}$이 trivial한 것과 $\mathcal{L}\cong \mathcal{O}_S$인 것은 동치이다.
:::

[예시 15](#ex15)의 둘째 경우에서 보듯, covering 위에서 $G$-torsor를 붙이는 transition data $g_{ij}$들은 정확히 cocycle condition $g_{ij}g_{jk}=g_{ik}$를 만족하며, trivialization의 선택에 따른 차이는 coboundary로 흡수된다. 따라서 주어진 base $S$ 위의 $G$-torsor의 isomorphism class 전체는 1차 cohomology set $H^1(S, G)$ (fppf topology에서는 $H^1_\fppf(S, G)$)에 의해 분류되며, $G=\mathbb{G}_m$인 경우가 바로 $\Pic(S)\cong H^1(S, \mathcal{O}_S^\times)$이다. 한편 torsor들을 집합으로 세는 대신 이들이 이루는 groupoid를 하나의 기하학적 대상으로 취급할 수도 있는데, field $\mathbb{K}$ 위에서 $\mathbb{G}_m$-torsor를 분류하는 $[\Spec \mathbb{K}/\mathbb{G}_m]$과 같은 quotient stack이 바로 그렇게 얻어지는 대상으로서 stack 이론의 출발점이 된다.

---

**참고문헌**

**[Har]** R. Hartshorne, *Algebraic geometry*. Graduate texts in mathematics. Springer, 1977.  
**[Vak]** R. Vakil, *The rising sea: Foundation of algebraic geometry*. Available [online](https://math.stanford.edu/~vakil/216blog/).
