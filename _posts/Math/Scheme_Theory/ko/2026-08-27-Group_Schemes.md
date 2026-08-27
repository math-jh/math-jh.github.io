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
Scheme $S$ 위의 *group scheme<sub>군 스킴</sub>*은 $\Sch_{/S}$의 group object이다. 즉 group scheme $G$는 structure morphism $\pi: G \rightarrow S$를 가진 $S$-scheme $G$으로서, 이 위에 정의된 세 $S$-morphism

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
:::

위의 예시에서 각 경우의 group scheme의 구조는 [명제 2](#prop2)를 사용하여 얻어진 것으로, 해당 명제의 유용성을 증명한다. 뿐만 아니라, 위의 예시는 $\Spec \mathbb{Z}$ 위에서 정의한 것이지만 본질적으로 이는 모든 base $S$에서 정의한 것이다. [§스킴 사이의 사상, ⁋예시 4](/ko/math/scheme_theory/morphism_of_schemes#ex4) 이후에서 보았듯 $\Spec \mathbb{Z}$는 $\Sch$의 terminal object로서, 임의의 scheme $S$마다 유일한 structure morphism $\varphi: S\rightarrow \Spec \mathbb{Z}$가 존재하며, 이것이 유도하는 base change morphism

$$\varphi^\ast: \Sch\rightarrow \Sch_{/S};\qquad X\mapsto X\times_\mathbb{Z}S$$

을 생각할 수 있으며, 이를 통해 $\mathbb{Z}$ 위에서 정의된 group scheme $G$를 $G_S=\varphi^\ast G$로 옮겨 $S$-scheme으로 볼 수 있기 때문이다. [명제 2](#prop2)의 관점에서 보자면, 이는  $\widetilde{h}_G: \Sch^\op\rightarrow \Grp$ 이전에 다음의 functor

$$\varphi_\ast: \Sch_{/S}\rightarrow \Sch;\qquad (T\rightarrow S)\mapsto (T\rightarrow S\rightarrow \Spec\mathbb{Z})$$

의 opposite functor $\varphi_\ast^\op$를 합성하여 $\widetilde{h}_{G_S}=\widetilde{h}_G\circ \varphi_\ast^\op$로 정의한 것과 같으며, 이 둘이 같다는 것이 adjunction

$$\Hom_S(T, \varphi^\ast G)\cong \Hom_\mathbb{Z}(\varphi_\ast T, G)$$

에 의해 보장되는 것이다. 이러한 방식으로 얻어지는 relative group schemes over $S$는 아래첨자를 사용하여 $\mathbb{G}_{a,S}, \mathbb{G}_{m,S},\mu_{n,S},\GL_{n,S},\SL_{n,S}$ 등으로 적고, 문맥상 base가 명확한 경우에는 첨자를 생략하고 $\mathbb{G}_a, \mathbb{G}_m$ 등으로 적기로 한다.

한편 위의 예시에서 주어진 것들은 모두 affine group scheme들이며, 이들이 정의된 방식 또한 명확하다. 뿐만 아니라, $\mu_n$을 제외한 예시들이 affine space 위에서 smooth인 것도 쉽게 보일 수 있다. 우선 $\mathbb{G}_a$는 affine line 그 자체이므로 별도의 논증이 필요없으며, $\GL_n$은 $\det$이 정의하는 $n^2$-dimensional affine space의 open subscheme $D(\det)$이며 그 특수한 경우 $n=1$이 $\mathbb{G}_m$이다. 마지막으로 $\SL_n$의 경우, [\[선형대수학\] §행렬식의 존재성과 유일성, ⁋정리 12](/ko/math/linear_algebra/existence_and_uniqueness_of_determinant#thm12)의 Laplace expansion으로부터 $f=\det-1$의 $\x_{ij}$에 대한 편미분이 $(i,j)$ 방향의 cofactor $C_{ij}$임을 확인할 수 있다. 따라서 [§매끄러운 사상과 에탈 사상, ⁋정리 4](/ko/math/scheme_theory/smooth_and_etale_morphisms#thm4)에 의해 그 Jacobian은 다음의 $1\times n^2$ 행렬

$$J_f=(\partial f/\partial\x_{ij})_{i,j}=(C_{ij})_{ij}$$

로 주어진다. 이 때, $\SL_n$에 속하는 임의의 행렬에 대하여, 이 행렬의 $i$번째 행을 고정하고 Laplace expansion을 생각하면 항등식 $\sum_j\x_{ij}C_{ij}=1$이 성립하며 따라서 위 Jacobian의 성분들 중 $C_{i1},\ldots, C_{in}$이 생성하는 ideal이 전체 ring이 되므로 이는 모든 점에서 full rank를 가지고, 따라서 $\SL_n$은 그 base 위에서 relative dimension $n^2-1$의 smooth morphism이 된다. 

한편 $\mu_n$은 $n$이 base에서 가역이면 finite étale이다. 반면 characteristic $p$인 field $\mathbb{K}$ 위에서는 $\mu_p$와 $\alpha_p=\ker(\Frob:\mathbb{G}_a\rightarrow\mathbb{G}_a)$가 underlying topological space로는 한 점이지만 nonreduced인 *infinitesimal* group scheme이 된다. 이는 [§매끄러운 사상과 에탈 사상, ⁋예시 14](/ko/math/scheme_theory/smooth_and_etale_morphisms#ex14)에서 inseparable extension의 geometric fiber에 nontrivial thickening이 남아 étale하지 않았던 것과 같은 현상으로, characteristic $p$ 특유의 성질을 보여주는 또 다른 예시이다.

## 부분군 스킴

일반적으로 $S$ 위의 group scheme $G$의 *subgroup scheme*은 group scheme $H$와 group scheme homomorphism인 monomorphism $\iota:H\rightarrow G$의 데이터이며, 특히 $\iota$가 closed embedding이면 이를 *closed subgroup scheme*이라 부른다. [\[리 이론\] §리 군, ⁋정리 5](/ko/math/lie_theory/Lie_groups#thm5)가 Lie group의 closed subgroup에 canonical Lie group structure를 주듯, group scheme에서도 주로 다루는 algebraic subgroup들은 closed subgroup scheme으로 나타난다. 예를 들어 group scheme homomorphism을 정의하고 나면 가장 먼저 살펴보는 것은 그 kernel이다. Group의 kernel은 항등원의 preimage이므로, scheme의 언어에서 이는 identity morphism을 따른 fiber product가 된다.

::: 정의 4
Group scheme homomorphism $\varphi:G\rightarrow H$에 대하여 그 *kernel*을 fiber product

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
먼저 closed embedding은 base change에 대해 보존된다. ([§닫힌 부분스킴, ⁋명제 3](/ko/math/scheme_theory/closed_subschemes#prop3)) 이제 $\pi:H\rightarrow S$를 structure morphism이라 하면 $\epsilon_H:S\rightarrow H$는 $\pi$의 절단이고, 따라서 diagonal morphism $\Delta_{H/S}:H\rightarrow H\times_S H$의 base change이다. $\pi$가 separated이므로 $\Delta_{H/S}$는 closed embedding이고, 따라서 $\epsilon_H$도 closed embedding이다. 다시 $\ker\varphi\rightarrow G$는 $\epsilon_H$를 $\varphi$를 따라 base change한 것이므로 closed embedding이다. 위에서 이미 $\ker\varphi$가 group scheme임을 확인하였으므로 이는 $G$의 closed subgroup scheme이다.
:::

Affine scheme 사이의 morphism은 항상 separated이므로 ([§값매김환, ⁋보조정리 5](/ko/math/scheme_theory/valuative_criteria#lem5)), affine base 위의 affine group scheme에 대해서는 [명제 5](#prop5)의 가정이 자동으로 성립한다. 가장 중요한 예는 $n$제곱 morphism $[n]:\mathbb{G}_m \rightarrow \mathbb{G}_m$, 곧 각각의 $T$에서 $a\mapsto a^n$인 homomorphism이다. 공역의 좌표를 $\y$로 적으면 이는 ring 수준에서 $\y\mapsto \x^n$에 대응하고, 항등원 morphism은 $\y\mapsto 1$인 counit에 대응하므로

$$\ker[n]=\Spec\left(\mathbb{Z}[\x,\x^{-1}]\otimes_{\mathbb{Z}[\y,\y^{-1}]}\mathbb{Z}\right)=\Spec \mathbb{Z}[\x,\x^{-1}]/(\x^n-1)=\Spec \mathbb{Z}[\x]/(\x^n-1)=\mu_n$$

이다. ([§올곱, ⁋보조정리 2](/ko/math/scheme_theory/fiber_products#lem2)) 여기에서 $\mathbb{Z}=\mathbb{Z}[\y,\y^{-1}]/(\y-1)$이므로 tensor product는 $\x^n-1$이 생성하는 ideal로 나눈 몫이 되고, 그 몫에서는 $\x$가 이미 가역이므로 localization을 떼어낼 수 있다. 곧 $\mu_n$은 $\mathbb{G}_m$의 closed subgroup scheme이다.

## Hopf algebra

이제 base와 group scheme 자신이 모두 affine인 경우를 보자. $G=\Spec A$라 하면 $\Spec$은 contravariant이므로 [정의 1](#def1)의 세 morphism $\mu_G,\epsilon_G,\iota_G$는 coordinate ring 위에서 방향이 뒤집힌 $\mathbb{K}$-algebra homomorphism

$$\Delta:A\rightarrow A\otimes_\mathbb{K}A,\qquad \epsilon:A\rightarrow\mathbb{K},\qquad \iota:A\rightarrow A$$

으로 나타난다. Group object의 결합법칙·항등원·역원 조건도 각각 coassociativity·counit·antipode 조건으로 뒤집히는데, 마침 이는 [\[범주론\] §모노이드 대상, ⁋정의 7](/ko/math/category_theory/monoid_objects#def7)의 Hopf monoid를 symmetric monoidal category $(\rMod{\mathbb{K}},\otimes_\mathbb{K},\mathbb{K})$에서 구현한 *Hopf algebra<sub>호프 대수</sub>*이다. ([\[범주론\] §모노이드 대상, ⁋예시 8](/ko/math/category_theory/monoid_objects#ex8)) 여기에서는 affine scheme의 coordinate ring만을 다루므로 $A$가 commutative인 경우로 제한하고, base scheme의 기호와 구별하기 위하여 antipode를 관례적인 $S$ 대신 $\iota$로 적는다.

그럼 다음을 기대하는 것이 자연스럽다.

::: 정리 6
Ring $\mathbb{K}$에 대하여, $\Spec$은 commutative Hopf $\mathbb{K}$-algebra들의 category와 $\Spec \mathbb{K}$ 위의 affine group scheme들의 category 사이의 anti-equivalence를 준다. 이 대응 아래에서 $\Delta,\epsilon,\iota$는 각각 $\mu_G,\epsilon_G,\iota_G$에 대응한다.
:::
::: 증명
[§아핀스킴, ⁋정리 13](/ko/math/scheme_theory/affine_schemes#thm13)에 의하여 commutative $\mathbb{K}$-algebra들과 $\Spec\mathbb{K}$ 위의 affine scheme들은 anti-equivalent이고, 이 대응은 tensor product와 $\mathbb{K}$를 각각 fiber product와 terminal object로 옮긴다. ([§올곱, ⁋보조정리 2](/ko/math/scheme_theory/fiber_products#lem2)) 따라서 [정의 1](#def1)의 데이터 $\mu_G,\epsilon_G,\iota_G$는 arrow를 뒤집으면 위의 데이터 $\Delta,\epsilon,\iota$가 된다. 이 동치가 합성과 항등사상을 보존하므로 group object의 세 공리는 각각 Hopf algebra의 세 공리로 옮겨지고, 같은 논리를 구조를 보존하는 morphism에 적용하면 주장한 anti-equivalence를 얻는다.
:::

[정리 6](#thm6)에 의하여 affine group scheme $G=\Spec A$의 $R$-point들의 group 구조는 $A$의 Hopf 구조로 명시된다. 곧 $G(R)=\Hom_{\mathbb{K}\text{-alg}}(A,R)$ 위에서 곱셈은 $g\ast h=\mu_R\circ(g\otimes h)\circ\Delta$, 항등원은 $\eta_R\circ\epsilon$, 역원은 $g\mapsto g\circ\iota$로 주어진다. 여기에서 $\mu_R:R\otimes_\mathbb{K}R\rightarrow R$은 곱셈이고 $\eta_R:\mathbb{K}\rightarrow R$은 구조사상이다. 이 공식들은 다음 절에서 representation을 comodule로 번역할 때 그대로 쓰인다.

## Comodule과 representation

[\[표현론\] §유한군의 표현론, ⁋명제 4](/ko/math/representation_theory/representations_of_finite_groups#prop4)에서 ordinary group $G$의 representation을 group algebra 위의 module, 곧 $G$-module로 해석하였다. Group scheme에서는 이 작용을 functorial하게 요구하여, 각 $R$-point가 $R$로 계수확장한 module 위에 작용하도록 한다.

::: 정의 7
Ring $\mathbb{K}$ 위의 affine group scheme $G$와 $\mathbb{K}$-module $V$에 대하여, $G$의 $V$ 위로의 *linear representation*이란 각각의 $\mathbb{K}$-algebra $R$마다 group homomorphism

$$r_R: G(R) \rightarrow \Aut_R(V\otimes_\mathbb{K}R)$$

이 주어지고 이것이 $R$에 대해 자연스러운 것이다. 곧 임의의 $\mathbb{K}$-algebra homomorphism $\phi: R \rightarrow R'$과 $g\in G(R)$에 대하여

$$r_{R'}(G(\phi)(g))\circ(\id_V\otimes\phi)=(\id_V\otimes\phi)\circ r_R(g)$$

이 성립하는 것이다. 두 representation $(V, r)$과 $(W, r')$ 사이의 *morphism*은 $\mathbb{K}$-linear map $u: V \rightarrow W$로서, 각각의 $R$과 $g\in G(R)$에 대하여 $r'_R(g)\circ(u\otimes\id_R)=(u\otimes\id_R)\circ r_R(g)$인 것이다.
:::

이 정의에서 $r_R(g)$는 $R$-선형 automorphism이므로, representation은 $V$의 $\mathbb{K}$-구조를 계수확장한 모든 층위에서 동시에 주어진 작용이다. 그런데 affine group scheme의 coordinate algebra는 contravariant functor $\Spec$을 통해 나타나므로, module의 작용 $A\otimes_\mathbb{K}V\rightarrow V$에 대응하는 map도 방향이 뒤집힌다. 이렇게 얻는 coaction $V\rightarrow V\otimes_\mathbb{K}A$가 comodule 구조이다.

::: 정의 8
Hopf $\mathbb{K}$-algebra $A$에 대하여, $A$-*comodule<sub>쌍대모듈</sub>*이란 $\mathbb{K}$-module $V$와 $\mathbb{K}$-linear map $\rho: V \rightarrow V\otimes_\mathbb{K}A$로서 다음 두 조건을 만족하는 것이다.

1. $(\rho\otimes\id_A)\circ\rho=(\id_V\otimes\Delta)\circ\rho$.
2. 동일시 $V\otimes_\mathbb{K}\mathbb{K}\cong V$ 아래에서 $(\id_V\otimes\epsilon)\circ\rho=\id_V$.

두 comodule 사이의 *morphism*은 $\mathbb{K}$-linear map $u: V \rightarrow W$로서 $\rho_W\circ u=(u\otimes\id_A)\circ\rho_V$인 것이다.
:::

두 조건은 Hopf algebra의 coassociativity와 counit 조건을 $V$가 받아들이는 형태로 옮긴 것이며, $V=A$이고 $\rho=\Delta$인 경우가 자명한 예이다. 다음 정리가 두 개념이 같은 데이터임을 말해준다.

::: 정리 9
Ring $\mathbb{K}$ 위의 affine group scheme $G=\Spec A$와 $\mathbb{K}$-module $V$에 대하여, $G$의 $V$ 위로의 linear representation과 $V$ 위의 $A$-comodule 구조는 서로 일대일대응한다. 이 대응은 morphism까지 보존하여 두 category의 동치를 준다.
:::
::: 증명
[§아핀스킴, ⁋정리 13](/ko/math/scheme_theory/affine_schemes#thm13)에 의하여 $G(R)=\Hom_{\mathbb{K}\text{-alg}}(A, R)$이고, [정리 6](#thm6) 직후에 적은 대로 그 group 구조는 $g\ast h=\mu_R\circ(g\otimes h)\circ\Delta$, 항등원 $\eta_R\circ\epsilon$, 역원 $g\circ\iota$로 주어진다.

Representation $\{r_R\}$이 주어졌다 하자. Universal element $\id_A\in G(A)$를 택하여 $\sigma=r_A(\id_A)$라 하고

$$\rho: V \rightarrow V\otimes_\mathbb{K}A;\qquad \rho(v)=\sigma(v\otimes 1)$$

로 정의한다. 임의의 $g\in G(R)$은 $\mathbb{K}$-algebra homomorphism $g:A\rightarrow R$이고 $G(g)(\id_A)=g$이므로, 자연스러움에 의하여

$$r_R(g)(v\otimes 1)=(\id_V\otimes g)(\rho(v))\tag{$\ast$}$$

를 얻으므로 representation 전체가 $\rho$ 하나로 복원된다. 이 식을 항등원 $\epsilon\in G(\mathbb{K})$과 두 universal element $a\mapsto a\otimes 1,1\otimes a$의 곱에 적용하면, group action의 항등원 조건과 결합법칙은 각각 $\rho$의 counit 조건과 coassociativity가 된다.

거꾸로 comodule 구조 $\rho$가 주어지면 $(\ast)$의 우변으로 $r_R(g)$를 정의하고 $R$-linear하게 확장한다. Coassociativity와 counit 조건은 각각 $r_R(g)\circ r_R(h)=r_R(g\ast h)$와 $r_R(\eta_R\circ\epsilon)=\id$을 주며, antipode 조건에 의하여 $r_R(g\circ\iota)$가 $r_R(g)$의 inverse가 된다. 자연스러움도 $(\ast)$에서 바로 따라오므로 $\{r_R\}$은 representation이고, 두 구성이 서로 역인 것과 morphism 조건의 대응도 같은 식에서 따라온다.
:::

[정리 9](#thm9)는 affine group scheme의 표현론이 순수하게 대수적인 comodule의 이론으로 번역됨을 말한다. 가장 기본적인 경우를 계산해두자.

::: 예시 10
$\mathbb{K}$ 위의 $\mathbb{G}_m=\Spec \mathbb{K}[\x,\x^{-1}]$에 대하여, $\mathbb{G}_m$의 $V$ 위로의 representation은 $V$의 $\mathbb{Z}$-grading

$$V=\bigoplus_{n\in \mathbb{Z}}V_n$$

과 일대일대응한다. 실제로 $\rho(v)=\sum_n\rho_n(v)\otimes\x^n$으로 적으면 ($\rho_n: V \rightarrow V$는 $\mathbb{K}$-linear이고 각 $v$에 대해 유한히 많은 $n$을 제외하면 $0$이다), $\epsilon(\x^n)=1$이므로 counit 조건은 $\sum_n\rho_n=\id_V$이 되고, $\Delta(\x^n)=\x^n\otimes\x^n$이므로 coassociativity는 $\rho_m\circ\rho_n=0$ ($m\neq n$)과 $\rho_n\circ\rho_n=\rho_n$이 된다. 곧 $\{\rho_n\}$은 합이 항등사상인 직교 idempotent들이고, $V_n=\rho_n(V)$로 두면 $V=\bigoplus_nV_n$이다. 거꾸로 grading이 주어지면 $\rho(v)=\sum_nv_n\otimes\x^n$이 comodule 구조를 준다. $(\ast)$를 통해 대응하는 representation은, $u\in \mathbb{G}_m(R)=R^\times$가 $V_n\otimes_\mathbb{K}R$ 위에 $u^n$배로 작용하는 것이다.
:::

[예시 10](#ex10)의 $V_n$을 weight $n$의 부분이라 부르며, 이 분해는 torus의 작용을 다룰 때 표준적인 도구가 된다. Torus $\mathbb{G}_m^r$의 경우 같은 계산을 반복하면 grading이 $\mathbb{Z}^r$에 의해 매겨지며, 그 각각의 성분이 torus의 한 character에 대응한다.

## Torsor

Group scheme이 등장하는 가장 중요한 기하학적 상황은, 어떤 대상 위에 group이 단순추이적으로 작용하지만 기준점이 정해져 있지 않은 경우이다. 위상수학의 principal bundle이 그러하듯, 이러한 대상은 국소적으로만 group 자신과 같아 보인다. 우선 작용을 정의한다.

::: 정의 11
$S$ 위의 group scheme $G$의 $S$-scheme $X$ 위로의 *left action*이란 $S$-scheme morphism $\sigma: G\times_SX \rightarrow X$로서, 각각의 $S$-scheme $T$에 대하여 유도되는 map

$$\sigma_T: G(T)\times X(T) \rightarrow X(T)$$

이 group $G(T)$의 집합 $X(T)$ 위로의 작용인 것이다.
:::

여기에서도 [§점함자, ⁋명제 7](/ko/math/scheme_theory/functor_of_points#prop7)과 [\[범주론\] §표현가능한 함자, ⁋정리 4](/ko/math/category_theory/representable_functors#thm4)에 의하여, 이 조건은 $\sigma\circ(\mu_G\times\id_X)=\sigma\circ(\id_G\times\sigma)$와 $\sigma\circ(\epsilon_G\circ\pi_X, \id_X)=\id_X$이라는 두 등식과 동치이다. 여기에서 $\pi_X: X \rightarrow S$는 structure morphism이다. 가장 기본적인 작용은 $G$ 자신 위로의 left translation, 곧 $\sigma=\mu_G$인 경우이다. Torsor는 이 자명한 예를 국소적으로만 닮은 대상이다.

::: 정의 12
$S$ 위의 group scheme $G$와 left action $\sigma: G\times_SP \rightarrow P$를 가진 $S$-scheme $P$에 대하여, $P$가 *$G$-torsor*라는 것은 다음 두 조건이 성립하는 것이다.

1. $P \rightarrow S$는 faithfully flat이고 ([§평탄사상, ⁋정의 1](/ko/math/scheme_theory/flat_morphisms#def1)) locally of finite presentation이다. ([§스킴 사상의 성질들, ⁋정의 18](/ko/math/scheme_theory/properties_of_scheme_morphisms#def18))
2. 작용과 사영이 유도하는 morphism

   $$(\sigma, \operatorname{pr}_2): G\times_SP \rightarrow P\times_SP$$

   이 isomorphism이다.

$G$-torsor $P$가 *trivial*하다는 것은, left translation 작용을 가진 $G$ 자신과 $G$-동변인 $S$-scheme isomorphism이 존재하는 것이다.
:::

둘째 조건을 functor의 언어로 읽으면 명확해진다. [§점함자, ⁋명제 7](/ko/math/scheme_theory/functor_of_points#prop7)에 의하여 각각의 $S$-scheme $T$에 대하여 이 조건은 map

$$G(T)\times P(T) \rightarrow P(T)\times P(T);\qquad (g, q)\mapsto (g\cdot q, q)$$

이 전단사인 것, 곧 임의의 두 점 $q, q'\in P(T)$에 대하여 $g\cdot q=q'$인 $g\in G(T)$가 유일하게 존재하는 것이다. 다시 말해 $P(T)$가 비어있지 않을 때마다 $G(T)$가 그 위에 단순추이적으로 작용한다. 첫째 조건은 $P$가 $S$ 위에서 충분히 고르게 퍼져 있어 그 자신이 covering의 역할을 할 수 있도록 요구하는 것이다. 이 둘을 합치면 다음을 얻는다.

::: 명제 13
$S$ 위의 $G$-torsor $P$에 대하여, $P$가 trivial한 것과 $P(S)\neq \emptyset$인 것, 곧 $P \rightarrow S$가 절단을 가지는 것은 동치이다.
:::
::: 증명
$P$가 trivial하면 $G$의 항등원 $\epsilon_G\in G(S)$에 대응하는 원소가 $P(S)$의 원소를 주므로 절단이 존재한다.

거꾸로 절단 $s\in P(S)$가 주어졌다 하자. 합성

$$\varphi: G\cong G\times_SS\xrightarrow{\ \id_G\times s\ }G\times_SP\xrightarrow{\ \sigma\ }P$$

를 생각하면, 각각의 $S$-scheme $T$에서 $\varphi_T(g)=g\cdot s_T$이다. 여기에서 $s_T\in P(T)$는 $s$를 $T \rightarrow S$를 따라 끌어당긴 것이다. [정의 12](#def12)의 둘째 조건이 주는 전단사 $G(T)\times P(T) \rightarrow P(T)\times P(T)$에서 둘째 좌표를 $s_T$로 고정하면, $g\mapsto g\cdot s_T$가 $G(T)$에서 $P(T)$로의 전단사임을 얻는다. 이 전단사는 $T$에 대해 자연스러우므로 [\[범주론\] §표현가능한 함자, ⁋정리 4](/ko/math/category_theory/representable_functors#thm4)에 의하여 $\varphi$는 isomorphism이다. 또 $\varphi_T(g'g)=(g'g)\cdot s_T=g'\cdot\varphi_T(g)$이므로 $\varphi$는 $G$-동변이며, 따라서 $P$는 trivial하다.
:::

[명제 13](#prop13)은 torsor가 자명한지의 여부가 오로지 대역적인 절단의 존재에 달려 있음을 말한다. 그런데 torsor는 정의상 자기 자신 위로 끌어올리면 언제나 절단을 가진다. 이것이 다음 명제의 내용이며, 여기에서 covering의 의미는 flat이고 locally of finite presentation이며 surjective morphism들의 모임, 곧 *fppf covering*이다. 이러한 covering에서 base의 각 affine open subset이 유한히 많은 affine open subset의 image로 덮이기까지 하면 [§충실평탄하강, ⁋정의 9](/ko/math/scheme_theory/faithfully_flat_descent#def9)의 fpqc covering이 되므로, 하강에 관한 그 글의 결과들을 그대로 쓸 수 있다.

::: 명제 14
$S$ 위의 $G$-torsor $P$에 대하여 다음이 성립한다.

1. 둘째 사영 $P\times_SP \rightarrow P$는 $P$ 위의 group scheme $G_P=G\times_SP$에 대한 torsor이며 trivial하다. 곧 $P$는 fppf covering $\{P \rightarrow S\}$ 위에서 자명해진다.
2. $G \rightarrow S$가 affine이고 $P \rightarrow S$가 quasi-compact이면 ([§스킴 사상의 성질들, ⁋정의 2](/ko/math/scheme_theory/properties_of_scheme_morphisms#def2)) $P \rightarrow S$ 또한 affine이다.
:::
::: 증명
1번을 보자. [정의 12](#def12)의 두 조건은 base change에 대해 보존된다. 실제로 flat은 base change에 대해 보존되고 ([§평탄사상, ⁋명제 3](/ko/math/scheme_theory/flat_morphisms#prop3)), surjective와 locally of finite presentation도 그러하며 ([§올곱, ⁋명제 16](/ko/math/scheme_theory/fiber_products#prop16)), 둘째 조건의 isomorphism은 base change하여도 isomorphism이기 때문이다. 따라서 둘째 사영 $P\times_SP \rightarrow P$는 $P$ 위의 $G_P$-torsor이다. 그런데 diagonal morphism $\Delta: P \rightarrow P\times_SP$가 이 사영의 절단이므로, [명제 13](#prop13)에 의하여 이 torsor는 trivial하다. 곧 $P$ 위에서 $P\times_SP\cong G\times_SP$이다. 한편 $P \rightarrow S$는 정의에 의하여 flat, locally of finite presentation, 전사이므로 $\{P \rightarrow S\}$는 fppf covering이다.

2번을 보이기 위해 먼저 $\{P \rightarrow S\}$가 fpqc covering임을 확인한다. $S$의 affine open subset $V$를 택하면 $V$는 quasi-compact이고 ([§스펙트럼, ⁋보조정리 12](/ko/math/scheme_theory/spectrums#lem12)), $P \rightarrow S$가 quasi-compact이므로 그 preimage 또한 quasi-compact이어서 유한히 많은 affine open subset들로 덮인다. $P \rightarrow S$가 전사이므로 이들의 image가 $V$를 덮으며, 나머지 조건은 1번에서 이미 확인하였으므로 [§충실평탄하강, ⁋정의 9](/ko/math/scheme_theory/faithfully_flat_descent#def9)의 조건이 모두 성립한다.

이제 affine은 base change에 대해 보존되므로 ([§올곱, ⁋명제 16](/ko/math/scheme_theory/fiber_products#prop16)) $G\times_SP \rightarrow P$는 affine이고, 1번에 의하여 이는 $P\times_SP \rightarrow P$, 곧 $P \rightarrow S$를 자기 자신을 따라 base change한 것과 isomorphic하다. 그런데 affine이라는 성질은 fpqc covering에 대해 base에서 국소적이므로 ([§충실평탄하강, ⁋명제 13](/ko/math/scheme_theory/faithfully_flat_descent#prop13)), $P \rightarrow S$ 자신이 affine이다.
:::

[명제 14](#prop14)의 둘째 항에 붙은 quasi-compact 가정은 fppf covering $\{P \rightarrow S\}$를 fpqc covering으로 올려 하강 결과를 쓸 수 있게 하기 위한 것이며, $P$가 Noetherian scheme인 경우에는 [§스킴 사상의 성질들, ⁋명제 4](/ko/math/scheme_theory/properties_of_scheme_morphisms#prop4)에 의하여 자동으로 성립한다.

[명제 14](#prop14)는 torsor를 $G$의 *form*으로 규정한다. 곧 torsor는 대역적으로는 $G$와 다를 수 있으나, 적당한 fppf covering으로 올라가면 언제나 $G$ 자신이 된다. 이 관점에서 torsor는 [§충실평탄하강, ⁋정의 4](/ko/math/scheme_theory/faithfully_flat_descent#def4)의 descent datum으로 기술되며, $G$가 affine인 경우 [§충실평탄하강, ⁋정리 12](/ko/math/scheme_theory/faithfully_flat_descent#thm12)에 의하여 그러한 데이터가 실제로 $S$ 위의 scheme을 산출한다. 자명하지 않은 torsor가 실제로 존재한다는 것은 다음 예시가 보여준다.

::: 예시 15
1. $S=\Spec \mathbb{R}$, $P=\Spec \mathbb{C}$이라 하고, $G$를 $\mathbb{Z}/2$의 constant group scheme, 곧 두 개의 $S$의 복사본의 disjoint union $\Spec(\mathbb{R}\times\mathbb{R})$이라 하자. 이는 $G(T)$가 locally constant function $\lvert T\rvert \rightarrow \mathbb{Z}/2$들이 이루는 group이 되도록 하는 group scheme이며, $T$의 connected component들이 열려 있는 경우에는 이것이 component마다 $\mathbb{Z}/2$의 원소를 고르는 것과 같다. 복소켤레가 $\mathbb{R}$-algebra automorphism이므로, 한 복사본 위에서는 $\id_P$로 다른 복사본 위에서는 켤레로 정의하여 작용 $\sigma: G\times_SP \rightarrow P$를 얻는다. $\mathbb{C}$가 $\mathbb{R}$ 위의 rank $2$ free module이므로 $P \rightarrow S$는 faithfully flat이고 locally of finite presentation이다. 또 $G\times_SP=\Spec(\mathbb{C}\times\mathbb{C})$이고 $P\times_SP=\Spec(\mathbb{C}\otimes_\mathbb{R}\mathbb{C})$인데, 위의 $\sigma$가 $\sigma^\sharp(z)=(z,\bar z)$를 주므로 $(\sigma, \operatorname{pr}_2)$의 dual은

   $$\mathbb{C}\otimes_\mathbb{R}\mathbb{C} \rightarrow \mathbb{C}\times\mathbb{C};\qquad z\otimes w\mapsto (zw, \bar zw)$$

   이다. 이것이 $\mathbb{R}$-algebra isomorphism이므로 [정의 12](#def12)의 둘째 조건도 성립한다. 그러나 $\mathbb{R}$-algebra homomorphism $\mathbb{C} \rightarrow \mathbb{R}$은 존재하지 않으므로 $P(S)=\emptyset$이고, [명제 13](#prop13)에 의하여 이 torsor는 자명하지 않다.

2. Scheme $S$ 위의 invertible sheaf $\mathcal{L}$에 대하여 ([§준연접층, ⁋정의 12](/ko/math/scheme_theory/quasicoherent_sheaves#def12)), $\mathcal{L}$을 trivialize하는 open cover $\{U_i\}$와 transition unit $g_{ij}\in \Gamma(U_i\cap U_j, \mathcal{O}_S^\times)$를 택하자. 이들은 $\mathcal{L}\vert_{U_i}\cong \mathcal{O}_{U_i}$인 trivialization들 사이의 좌표변환이므로 $U_i\cap U_j\cap U_k$ 위에서 $g_{ij}g_{jk}=g_{ik}$를 만족한다. 그럼 $\mathbb{G}_{m}\times_SU_i$들을 겹침 위에서 $(t, u)\mapsto (g_{ij}(u)t, u)$로 붙이면 이 등식이 [§스킴, ⁋보조정리 9](/ko/math/scheme_theory/schemes#lem9)의 cocycle condition을 그대로 주므로 $S$-scheme $P_\mathcal{L}$을 얻으며, 왼쪽 곱셈이 이 접합과 commute하므로 $P_\mathcal{L}$은 $\mathbb{G}_m$-torsor가 된다. Zariski open cover는 fppf covering이고 [정의 12](#def12)의 두 조건은 모두 국소적으로 확인되기 때문이다. 이 torsor의 절단은 $s_i\in \Gamma(U_i,\mathcal{O}_S^\times)$들로서 $s_i=g_{ij}s_j$를 만족하는 것, 곧 어디에서도 사라지지 않는 $\mathcal{L}$의 global section이므로, [명제 13](#prop13)에 의하여 $P_\mathcal{L}$이 자명한 것과 $\mathcal{L}\cong \mathcal{O}_S$인 것이 동치이다.
:::

[예시 15](#ex15)의 둘째 경우는 $\mathbb{G}_m$-torsor가 invertible sheaf와 같은 정보를 담고 있음을 시사한다. 그럼 자연스러운 다음 질문은 주어진 $S$와 $G$에 대하여 $G$-torsor 전체를 분류하는 것인데, [명제 13](#prop13)이 말해주듯 자명하지 않은 torsor의 존재는 대역적인 절단의 부재라는 형태의 장애이므로, 이 분류는 cohomology의 문제가 된다. 또 하나의 길은 torsor들을 개별적으로 세는 대신 그들이 이루는 groupoid를 그대로 하나의 기하학적 대상으로 삼는 것이며, field $\mathbb{K}$ 위에서 $\mathbb{G}_m$-torsor를 분류하는 $[\Spec \mathbb{K}/\mathbb{G}_m]$과 같은 quotient stack이 그렇게 얻어지는 대상으로서 stack 이론의 출발점이 된다.

---

**참고문헌**

**[Har]** R. Hartshorne, *Algebraic geometry*. Graduate texts in mathematics. Springer, 1977.  
**[Vak]** R. Vakil, *The rising sea: Foundation of algebraic geometry*. Available [online](https://math.stanford.edu/~vakil/216blog/).
