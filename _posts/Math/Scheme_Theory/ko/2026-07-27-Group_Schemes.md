---
title: "군 스킴"
description: "Functor of points의 언어로 group scheme을 정의하고 곱셈·역원·항등원 morphism에 의한 고전적 정의와의 동치를 확인한 뒤, affine group scheme과 commutative Hopf algebra의 반대동치, 그리고 representation과 comodule의 대응을 확립한다. 이어 characteristic p에서 non-reduced가 되는 mu_p와 그곳에서만 정의되는 alpha_p를 살펴보고, 마지막으로 torsor를 정의하여 그 자명성 판정과 fppf-국소 자명성을 다룬다."
excerpt: "Group schemes, Hopf algebras, comodules, infinitesimal examples, and torsors"

categories: [Math / Scheme Theory]
permalink: /ko/math/scheme_theory/group_schemes
sidebar: 
    nav: "scheme_theory-ko"

date: 2026-07-27
weight: 24

published: false

---

Group은 대상 위의 대칭을 기술하는 가장 기본적인 장치이며, algebraic geometry에서도 사정은 다르지 않다. 다만 scheme의 세계에서 group을 다루려면 group의 공리를 원소가 아니라 morphism과 diagram으로 옮겨 적어야 하는데, [§점함자](/ko/math/scheme_theory/functor_of_points)의 관점을 취하면 이 번역이 거의 자동으로 이루어진다. 곧 scheme $G$의 각 test scheme $T$ 위의 점들의 집합 $G(T)$에 group 구조를 주고 그것이 $T$에 대해 자연스럽기만 요구하면, Yoneda 보조정리가 나머지를 처리한다. 이번 글에서 우리는 이 정의에서 출발하여, affine group scheme이 commutative Hopf algebra와 반대동치를 이룬다는 것과 그 representation이 comodule로 기술된다는 것을 확인한다. 이어 characteristic $p$에서 non-reduced가 되는 $\mu_p$와 그곳에서만 정의되는 $\alpha_p$를 살펴보는데, 이들은 고전적인 variety의 언어로는 보이지 않고 오직 scheme의 언어에서만 포착되는 대상이다. 마지막으로 group scheme이 단순추이적으로 작용하는 대상인 torsor를 정의하고, 그것이 [§충실평탄 하강](/ko/math/scheme_theory/faithfully_flat_descent)의 covering을 따라 국소적으로 자명해진다는 것을 확인한다.

## 군 스킴

고전적으로 algebraic group은 group 구조를 가진 variety로서, 곱셈과 역원이 morphism인 것으로 정의된다. ([\[대수다양체\] §대수적 군, ⁋정의 1](/ko/math/algebraic_varieties/algebraic_groups#def1)) 이를 scheme의 세계로 옮기는 가장 깔끔한 방법은, 각각의 test scheme 위에서 그 점들이 group을 이루도록 요구하는 것이다.

::: 정의 1
Scheme $S$ 위의 *group scheme<sub>군 스킴</sub>*은, $S$-scheme $G$로서 그 functor of points가 group으로 값을 갖는 functor로 lift되는 것이다. 곧 functor

$$h_G:(\Sch_{/S})^\op \rightarrow \Grp$$

이 존재하여, forgetful functor $\Grp \rightarrow \Set$과 합성하면 $\Hom_{\Sch_{/S}}(-, G)$가 되는 것이다. 풀어 말하면, 각각의 $S$-scheme $T$에 대하여 $G(T)$에 group 구조가 주어지고, 임의의 $S$-scheme morphism $T' \rightarrow T$가 유도하는 $G(T) \rightarrow G(T')$이 group homomorphism인 것이다. 두 group scheme $G, H$ 사이의 *homomorphism*은 $S$-scheme morphism $\varphi: G \rightarrow H$로서, 각각의 $T$에 대하여 $\varphi_T: G(T) \rightarrow H(T)$가 group homomorphism인 것이다.
:::

[정의 1](#def1)은 group scheme을 "functor로서 group인 scheme"으로 규정한다. 범주론의 언어로는 $\Sch_{/S}$가 categorical product를 가지는 cartesian monoidal category이므로 그 안의 group object를 생각할 수 있으며 ([\[범주론\] §모노이드 대상, ⁋정의 3](/ko/math/category_theory/monoid_objects#def3)), group scheme이란 정확히 이 group object이다. ([\[범주론\] §모노이드 대상, ⁋예시 4](/ko/math/category_theory/monoid_objects#ex4)) 다음 명제가 이 두 서술이 일치함을 확인해준다.

::: 명제 2
$S$-scheme $G$와 그 structure morphism $\pi: G \rightarrow S$에 대하여, 다음 두 데이터는 서로 일대일대응한다. 아래에서 $S$-scheme morphism $\alpha, \beta: X \rightarrow G$가 유도하는 morphism $X \rightarrow G\times_SG$를 $(\alpha,\beta)$로 적는다.

1. [정의 1](#def1)의 의미에서 $G$ 위의 group scheme 구조.
2. $S$-scheme morphism $\mu_G: G\times_SG \rightarrow G$, $\iota_G: G \rightarrow G$, $\epsilon_G: S \rightarrow G$로서

   $$\mu_G\circ(\mu_G\times \id_G)=\mu_G\circ(\id_G\times \mu_G),\qquad \mu_G\circ(\epsilon_G\circ\pi, \id_G)=\id_G=\mu_G\circ(\id_G, \epsilon_G\circ\pi)$$

   과

   $$\mu_G\circ(\iota_G, \id_G)=\epsilon_G\circ\pi=\mu_G\circ(\id_G, \iota_G)$$

   을 만족하는 것.
:::
::: 증명
Yoneda 보조정리는 임의의 locally small category에 대하여 성립하므로, [§점함자, ⁋따름정리 2](/ko/math/scheme_theory/functor_of_points#cor2)를 $\Sch_{/S}$에 적용하면 $S$-scheme 사이의 morphism과 그 functor of points 사이의 natural transformation이 정확히 대응한다. 또 $S$는 $\Sch_{/S}$의 terminal object이므로 $S(T)$는 한 점이고, 따라서 [§점함자, ⁋명제 11](/ko/math/scheme_theory/functor_of_points#prop11)에 의하여 임의의 $S$-scheme $T$에 대하여

$$(G\times_SG)(T)=G(T)\times_{S(T)}G(T)=G(T)\times G(T)$$

이 성립한다.

1번을 가정하자. 각각의 $T$마다 곱셈 $G(T)\times G(T) \rightarrow G(T)$, 역원 $G(T) \rightarrow G(T)$, 그리고 항등원을 고르는 map $S(T) \rightarrow G(T)$가 주어지고, 이들은 group 구조가 $T$에 대해 자연스럽다는 가정으로부터 $T$에 대해 자연스럽다. 위의 동일시 아래에서 이들은 각각 natural transformation $h_{G\times_SG} \rightarrow h_G$, $h_G \rightarrow h_G$, $h_S \rightarrow h_G$이므로, 유일한 morphism $\mu_G, \iota_G, \epsilon_G$를 준다. 이제 group의 공리는 각각의 $T$에서 성립하는 등식이고, 위의 대응은 합성을 합성으로 옮기므로, 결합법칙·항등원·역원의 조건은 그대로 2번의 세 등식이 된다.

거꾸로 2번을 가정하고 $h_G$를 적용하면, 각각의 $T$에 대하여 $\mu_{G,T}: G(T)\times G(T) \rightarrow G(T)$, $\iota_{G,T}: G(T) \rightarrow G(T)$와 원소 $\epsilon_{G,T}\in G(T)$를 얻고, 주어진 세 등식은 이들이 group의 공리를 만족한다는 것 그대로이다. 이 구조가 $T$에 대해 자연스러운 것은 $\mu_G, \iota_G, \epsilon_G$가 하나의 morphism이어서 그 유도 map이 functoriality와 commute하기 때문이다. 두 대응이 서로 역임은 [§점함자, ⁋따름정리 2](/ko/math/scheme_theory/functor_of_points#cor2)의 일대일대응의 유일성에서 따라온다.
:::

[명제 2](#prop2)에 의하여 우리는 group scheme을 다룰 때 필요에 따라 두 언어를 자유롭게 오갈 수 있다. Functorial한 정의의 장점은 group의 공리를 직접 commutative diagram으로 적는 대신 각 $G(T)$가 통상적인 의미에서 group이라는 것만 확인하면 된다는 데 있고, morphism에 의한 서술의 장점은 $\mu_G, \iota_G, \epsilon_G$를 대수적으로 명시할 수 있어 좌표 계산이 가능하다는 데 있다. 이후 $\epsilon_G\circ\pi: G \rightarrow G$를 간단히 $\epsilon_G$로 적고, $G(T)$의 항등원 또한 $\epsilon_G$로 적는다.

::: 예시 3
다음은 모두 $\Spec \mathbb{Z}$ 위의 group scheme이다.

1. *Additive group<sub>덧셈군</sub>* $\mathbb{G}_a=\Spec \mathbb{Z}[\x]=\mathbb{A}^1$. [§점함자, ⁋명제 5](/ko/math/scheme_theory/functor_of_points#prop5)에 의하여 $\mathbb{G}_a(T)\cong \Gamma(T, \mathcal{O}_T)$이며, 여기에 ring $\Gamma(T, \mathcal{O}_T)$의 덧셈을 주면 group이 된다. 임의의 morphism이 유도하는 사상은 ring homomorphism이므로 덧셈을 보존하고, 따라서 functoriality가 성립한다.

2. *Multiplicative group<sub>곱셈군</sub>* $\mathbb{G}_m=\Spec \mathbb{Z}[\x, \x^{-1}]$. [§점함자, ⁋명제 7](/ko/math/scheme_theory/functor_of_points#prop7)에 의하여 $\mathbb{G}_m(T)\cong \Gamma(T, \mathcal{O}_T)^\times$이며, 여기에 가역원들의 곱셈을 준다.

3. *$n$-th roots of unity* $\mu_n=\Spec \mathbb{Z}[\x]/(\x^n-1)$. [§아핀스킴, ⁋정리 13](/ko/math/scheme_theory/affine_schemes#thm13)의 adjunction에 의하여 $\mu_n(T)\cong \{a\in \Gamma(T, \mathcal{O}_T)\mid a^n=1\}$이며, $a^n=1$이면 $a$가 가역이므로 이는 $\mathbb{G}_m(T)$의 subgroup이다.

4. *General linear group* $\GL_n=\Spec \mathbb{Z}[\x_{11},\ldots, \x_{nn}, \det{}^{-1}]$. 여기에서 $\det$은 행렬 $(\x_{ij})$의 determinant이며, 이를 가역으로 만든 localization을 취한 것이다. 행렬이 가역인 것과 그 determinant가 가역인 것이 동치이므로 $\GL_n(T)$는 $\Gamma(T, \mathcal{O}_T)$ 성분의 가역행렬들의 group이다.

5. *Special linear group* $\SL_n=\Spec \mathbb{Z}[\x_{11},\ldots, \x_{nn}]/(\det-1)$. 각각의 $T$에 대하여 $\SL_n(T)$는 determinant가 $1$인 행렬들의 group이다.
:::

[예시 3](#ex3)의 각 경우에서 group 구조는 test scheme $T$에 대해 점별로 통상적인 대수 구조를 주는 것만으로 정의되었으며, 별도의 commutative diagram을 그릴 필요가 없었다. 또, 위의 구성은 모두 $\Spec \mathbb{Z}$ 위에서 주어졌으므로 임의의 base $S$ 위로 base change하여 상대적인 버전 $\mathbb{G}_{a,S}, \mathbb{G}_{m,S},\mu_{n,S},\GL_{n,S},\SL_{n,S}$를 얻는다. ([§올곱, ⁋예시 9](/ko/math/scheme_theory/fiber_products#ex9)) Fiber product가 functor of points 수준에서 점별 fiber product이므로 ([§점함자, ⁋명제 11](/ko/math/scheme_theory/functor_of_points#prop11)), base change한 대상의 group 구조는 원래의 것을 그대로 물려받는다. 이후 base가 문맥에서 분명한 경우에는 첨자를 생략하고 $\mathbb{G}_a, \mathbb{G}_m$ 등으로 적는다.

위의 다섯은 모두 affine group scheme이며, 그 가운데 $\mu_n$을 제외한 넷은 base 위에서 smooth하다. 실제로 $\mathbb{G}_a=\mathbb{A}^1$은 affine space로의 사영이고, $\GL_n$은 좌표를 하나 더 붙여

$$\GL_n=\Spec \mathbb{Z}[\x_{11},\ldots,\x_{nn},\z]/(\z\det-1)$$

로 적을 수 있는데 $\z\det-1$의 $\z$에 대한 편미분이 $\det$이고 이 ring에서 $\det$은 가역이므로, [§매끄러운 사상과 étale 사상, ⁋정리 5](/ko/math/scheme_theory/smooth_and_etale_morphisms#thm5)에 의하여 $\GL_n \rightarrow \Spec \mathbb{Z}$는 상대차원 $n^2$의 smooth morphism이다. $n=1$인 경우가 곧 $\mathbb{G}_m$이다. $\SL_n$의 경우 $\det-1$의 $\x_{ij}$에 대한 편미분은 $(i,j)$ 성분의 cofactor $C_{ij}$이고 $\sum_j\x_{ij}C_{ij}=\det=1$이므로 어느 점의 residue field에서도 이들이 모두 소멸할 수 없어, 같은 판정에 의하여 상대차원 $n^2-1$의 smooth morphism이다. 반면 $\mu_n$은 $n$이 가역이 아닌 점 위에서 smooth하지 않다. Characteristic $p$가 $n$을 나누는 field $\mathbb{K}$ 위에서 $n=p^am$이라 적으면 $\x^n-1=(\x^m-1)^{p^a}$이므로 fiber $\Spec \mathbb{K}[\x]/(\x^n-1)$가 $0$이 아닌 nilpotent $\x^m-1$을 가지며 이는 $\mathbb{K}$의 algebraic closure로 base change한 뒤에도 그러하다. 그런데 [\[가환대수학\] §정칙국소환, ⁋따름정리 1](/ko/math/commutative_algebra/regular_local_rings#cor1)에 의하여 regular local ring은 integral domain이므로, 이 nilpotent가 살아남는 점에서의 local ring은 regular일 수 없다. ([§매끄러운 사상과 étale 사상, ⁋정의 3](/ko/math/scheme_theory/smooth_and_etale_morphisms#def3))

## Subgroup scheme과 kernel

Group scheme 사이의 homomorphism이 주어지면 그 kernel을 만들고 싶다. Group의 kernel은 항등원의 preimage이므로, scheme의 언어에서 이는 항등원 morphism을 따른 fiber product가 된다.

::: 정의 4
$S$ 위의 group scheme $G$의 *closed subgroup scheme*이란, group scheme $H$와 group scheme homomorphism $\iota: H \rightarrow G$로서 $\iota$가 closed embedding인 것이다. ([§닫힌 부분스킴, ⁋정의 2](/ko/math/scheme_theory/closed_subschemes#def2)) 또, group scheme homomorphism $\varphi: G \rightarrow H$에 대하여 그 *kernel*을 fiber product

$$\ker \varphi=G\times_{\varphi, H, \epsilon_H}S$$

으로 정의한다. 여기에서 $\epsilon_H: S \rightarrow H$는 [명제 2](#prop2)의 항등원 morphism이다.
:::

[§점함자, ⁋명제 11](/ko/math/scheme_theory/functor_of_points#prop11)로 계산하면 각각의 $S$-scheme $T$에 대하여

$$(\ker \varphi)(T)=G(T)\times_{H(T)}S(T)=\{g\in G(T)\mid \varphi_T(g)=\epsilon_{H,T}\}$$

이므로, 이 정의는 통상적인 kernel의 정의를 그대로 옮긴 것이다. 우변이 $G(T)$의 subgroup이고 그 대응이 $T$에 대해 자연스러우므로, $\ker \varphi$는 [정의 1](#def1)의 의미에서 group scheme이다. 남는 것은 $\ker \varphi \rightarrow G$가 closed embedding인지의 여부인데, 이는 $\epsilon_H$가 closed embedding인 것에 달려 있고 그 조건이 곧 separatedness이다.

::: 명제 5
$S$ 위의 group scheme homomorphism $\varphi: G \rightarrow H$에 대하여, $H \rightarrow S$가 separated이면 ([§값매김환, ⁋정의 3](/ko/math/scheme_theory/valuative_criteria#def3)) $\ker \varphi$는 $G$의 closed subgroup scheme이다.
:::
::: 증명
먼저 $H$의 항등원 morphism $\epsilon_H: S \rightarrow H$가 closed embedding임을 본다. $\pi: H \rightarrow S$를 structure morphism이라 하면 $\epsilon_H$는 $\pi$의 절단, 곧 $\pi\circ \epsilon_H=\id_S$이다. 이제 두 morphism $\id_H$와 $\epsilon_H\circ\pi$가 유도하는 $(\id_H, \epsilon_H\circ\pi): H \rightarrow H\times_SH$를 따라 diagonal morphism $\Delta: H \rightarrow H\times_SH$를 base change하자. 임의의 $S$-scheme $T$에 대하여 [§점함자, ⁋명제 11](/ko/math/scheme_theory/functor_of_points#prop11)로 계산하면, 이 fiber product의 $T$-point들은 $(h', h')=(h, \epsilon_{H,T}(\pi_T(h)))$를 만족하는 순서쌍 $(h', h)\in H(T)\times H(T)$들, 곧 $h'=h$이면서 $h=\epsilon_{H,T}(\pi_T(h))$인 $h\in H(T)$들이다. 그런데 대응 $s\mapsto \epsilon_{H,T}\circ s$와 $h\mapsto \pi_T\circ h$가 서로 역이므로 이 집합은 $S(T)$와 자연스럽게 일대일대응하며, [§점함자, ⁋따름정리 2](/ko/math/scheme_theory/functor_of_points#cor2)에 의하여 fiber product는 $S$이고 $H$로의 사영은 $\epsilon_H$이다. $\pi$가 separated이므로 $\Delta$는 closed embedding이다.

다음으로 closed embedding이 base change에 대해 보존됨을 확인한다. Closed embedding $\iota: Z \rightarrow X$와 임의의 morphism $\psi: X' \rightarrow X$가 주어졌다 하고 $W=Z\times_XX'$이라 하자. Closed embedding은 affine morphism이고 affine은 base change에 대해 보존되므로 ([§닫힌 부분스킴, ⁋명제 3](/ko/math/scheme_theory/closed_subschemes#prop3), [§올곱, ⁋명제 16](/ko/math/scheme_theory/fiber_products#prop16)) $W \rightarrow X'$ 또한 affine이다. 따라서 남은 것은 [§닫힌 부분스킴, ⁋명제 3](/ko/math/scheme_theory/closed_subschemes#prop3)의 둘째 조건, 곧 $X'$의 <em-ko>임의의</em-ko> affine open subset $V=\Spec C$에 대하여 그 preimage $\Spec D$를 주는 $C \rightarrow D$가 surjective인 것을 확인하는 일이다.

$X$를 affine open subset들로 덮고 그 preimage들을 $V$에서 잘라내면 $V$의 열린 덮개를 얻으며, principal open set들이 $\Spec C$의 base를 이루므로 ([§스펙트럼, ⁋보조정리 11](/ko/math/scheme_theory/spectrums#lem11)) 이를 세분하여 $V=\bigcup_\alpha D(c_\alpha)$이면서 각 $D(c_\alpha)$가 $X$의 어떤 affine open subset $\Spec B_\alpha$ 안으로 사상되도록 할 수 있다. 그럼 $\iota^{-1}(\Spec B_\alpha)\cong \Spec A_\alpha$에 대하여 $B_\alpha \rightarrow A_\alpha$가 surjective이고 ([§닫힌 부분스킴, ⁋명제 3](/ko/math/scheme_theory/closed_subschemes#prop3)), $D(c_\alpha)=\Spec C_{c_\alpha}$ 위에서 $W$는 $\Spec (A_\alpha\otimes_{B_\alpha}C_{c_\alpha})$인 동시에 $\Spec D_{c_\alpha}$이므로 ([§올곱, ⁋보조정리 2](/ko/math/scheme_theory/fiber_products#lem2)), $C_{c_\alpha} \rightarrow D_{c_\alpha}$는 $B_\alpha \rightarrow A_\alpha$의 base change로서 surjective이다.

이제 $C$의 임의의 maximal ideal $\mathfrak{m}$을 택하면 그에 대응하는 점이 어떤 $D(c_\alpha)$에 속하므로 $C_\mathfrak{m}$과 $D_\mathfrak{m}$은 각각 $C_{c_\alpha}$와 $D_{c_\alpha}$를 $C_{c_\alpha}\setminus\mathfrak{m}C_{c_\alpha}$에서 다시 localize한 것이다. 따라서 $D_\mathfrak{m}$의 임의의 원소는 $d\in D_{c_\alpha}$와 $t\in C_{c_\alpha}\setminus\mathfrak{m}C_{c_\alpha}$로 $d/t$ 꼴로 적히는데 위에서 $d$가 $C_{c_\alpha}$의 어떤 원소의 image이므로, $C_\mathfrak{m} \rightarrow D_\mathfrak{m}$ 또한 surjective이다. 따라서 [\[가환대수학\] §국소화의 성질들, ⁋명제 4](/ko/math/commutative_algebra/properties_of_localization#prop4)에 의하여 $C \rightarrow D$는 surjective이고, $V$가 임의의 affine open subset이었으므로 $W \rightarrow X'$는 closed embedding이다.

위의 두 문단을 합치면 $\epsilon_H$는 closed embedding $\Delta$를 $(\id_H, \epsilon_H\circ\pi)$를 따라 base change한 것이므로 closed embedding이고, 다시 $\ker \varphi \rightarrow G$는 $\epsilon_H$를 $\varphi$를 따라 base change한 것이므로 closed embedding이다. 위에서 확인한 대로 $(\ker \varphi)(T)$가 $G(T)$의 subgroup이므로 $\ker \varphi$는 $G$의 closed subgroup scheme이다.
:::

Affine scheme 사이의 morphism은 항상 separated이므로 ([§값매김환, ⁋보조정리 5](/ko/math/scheme_theory/valuative_criteria#lem5)), affine base 위의 affine group scheme에 대해서는 [명제 5](#prop5)의 가정이 자동으로 성립한다. 가장 중요한 예는 $n$제곱 morphism $[n]:\mathbb{G}_m \rightarrow \mathbb{G}_m$, 곧 각각의 $T$에서 $a\mapsto a^n$인 homomorphism이다. 공역의 좌표를 $\y$로 적으면 이는 ring 수준에서 $\y\mapsto \x^n$에 대응하고, 항등원 morphism은 $\y\mapsto 1$인 counit에 대응하므로

$$\ker[n]=\Spec\left(\mathbb{Z}[\x,\x^{-1}]\otimes_{\mathbb{Z}[\y,\y^{-1}]}\mathbb{Z}\right)=\Spec \mathbb{Z}[\x,\x^{-1}]/(\x^n-1)=\Spec \mathbb{Z}[\x]/(\x^n-1)=\mu_n$$

이다. ([§올곱, ⁋보조정리 2](/ko/math/scheme_theory/fiber_products#lem2)) 여기에서 $\mathbb{Z}=\mathbb{Z}[\y,\y^{-1}]/(\y-1)$이므로 tensor product는 $\x^n-1$이 생성하는 ideal로 나눈 몫이 되고, 그 몫에서는 $\x$가 이미 가역이므로 localization을 떼어낼 수 있다. 곧 $\mu_n$은 $\mathbb{G}_m$의 closed subgroup scheme이다.

## Hopf algebra

이제 base가 affine이고 group scheme 자신도 affine인 경우를 본다. 이 경우 $\Spec$이 ring과 affine scheme 사이의 반대동치를 주므로, [명제 2](#prop2)의 세 morphism $\mu_G, \iota_G, \epsilon_G$는 coordinate ring 위의 세 사상으로 뒤집혀 나타나고 group의 공리는 그 dual 조건이 된다. 이렇게 얻어지는 대수적 구조가 Hopf algebra이다.

::: 정의 6
Ring $\mathbb{K}$에 대하여, commutative $\mathbb{K}$-algebra $A$와 $\mathbb{K}$-algebra homomorphism

$$\Delta: A \rightarrow A\otimes_\mathbb{K}A,\qquad \epsilon: A \rightarrow \mathbb{K},\qquad \iota: A \rightarrow A$$

의 데이터 $(A, \Delta, \epsilon, \iota)$가 *Hopf algebra<sub>호프 대수</sub>*라는 것은 다음 세 조건이 성립하는 것이다. 아래에서 $\mu: A\otimes_\mathbb{K}A \rightarrow A$는 곱셈이고 $\eta: \mathbb{K} \rightarrow A$는 구조사상이다.

1. (Coassociativity) $(\Delta\otimes\id_A)\circ\Delta=(\id_A\otimes\Delta)\circ\Delta$.
2. (Counit) 동일시 $\mathbb{K}\otimes_\mathbb{K}A\cong A\cong A\otimes_\mathbb{K}\mathbb{K}$ 아래에서 $(\epsilon\otimes\id_A)\circ\Delta=\id_A=(\id_A\otimes\epsilon)\circ\Delta$.
3. (Antipode) $\mu\circ(\iota\otimes\id_A)\circ\Delta=\eta\circ\epsilon=\mu\circ(\id_A\otimes\iota)\circ\Delta$.

이 때 $\Delta$를 *comultiplication*, $\epsilon$을 *counit*, $\iota$를 *antipode*라 부른다. 두 Hopf $\mathbb{K}$-algebra 사이의 *homomorphism*은 $\mathbb{K}$-algebra homomorphism $\phi: A \rightarrow B$로서 $\Delta_B\circ \phi=(\phi\otimes \phi)\circ\Delta_A$, $\epsilon_B\circ \phi=\epsilon_A$, $\phi\circ\iota_A=\iota_B\circ \phi$를 만족하는 것이다.
:::

세 조건은 각각 결합법칙·항등원·역원의 dual이며, 이는 [\[범주론\] §모노이드 대상, ⁋정의 7](/ko/math/category_theory/monoid_objects#def7)의 Hopf monoid를 monoidal category $(\rMod{\mathbb{K}},\otimes_\mathbb{K}, \mathbb{K})$에서 구현한 것이다. ([\[범주론\] §모노이드 대상, ⁋예시 8](/ko/math/category_theory/monoid_objects#ex8)) 문헌의 일반적인 정의는 $A$의 commutativity를 요구하지 않으며, 그 경우 antipode는 algebra homomorphism이 아니라 anti-homomorphism이 된다. 우리는 affine group scheme의 coordinate ring만을 다루므로 처음부터 commutative인 경우로 제한하였고, 이 제한 아래에서 antipode가 $\mathbb{K}$-algebra homomorphism이 되는 것이다. 또 문헌에서는 antipode를 $S$로 적는 것이 관례이나, 여기에서는 base scheme의 기호와 겹치지 않도록 $\iota$를 쓴다.

::: 정리 7
Ring $\mathbb{K}$에 대하여, $\Spec$은 [정의 6](#def6)의 Hopf $\mathbb{K}$-algebra들의 category와 $\Spec \mathbb{K}$ 위의 affine group scheme들의 category 사이의 anti-equivalence를 준다. 이 대응 아래에서 $\Delta, \epsilon, \iota$는 각각 $\mu_G, \epsilon_G, \iota_G$에 대응한다.
:::
::: 증명
[§아핀스킴, ⁋정리 13](/ko/math/scheme_theory/affine_schemes#thm13)의 adjunction을 affine scheme으로 제한하면 동치 $\AffSch\simeq \cRing^\op$를 얻으며, $\Spec \mathbb{K}$ 위의 affine scheme들과 $\mathbb{K}$-algebra들 사이에서도 마찬가지이다. 이 동치는 $\Spec \mathbb{K}$ 위의 fiber product를 tensor product로 옮기고 ([§올곱, ⁋보조정리 2](/ko/math/scheme_theory/fiber_products#lem2)), terminal object $\Spec \mathbb{K}$를 $\mathbb{K}$로 옮긴다. 곧 $A$를 commutative $\mathbb{K}$-algebra라 할 때

$$\Spec A\times_{\Spec \mathbb{K}}\Spec A=\Spec(A\otimes_\mathbb{K}A),\qquad \Spec A\times_{\Spec \mathbb{K}}\Spec A\times_{\Spec \mathbb{K}}\Spec A=\Spec (A\otimes_\mathbb{K}A\otimes_\mathbb{K}A)$$

이다.

따라서 [명제 2](#prop2)의 데이터 $\mu_G: \Spec A\times_{\Spec \mathbb{K}}\Spec A \rightarrow \Spec A$, $\epsilon_G:\Spec \mathbb{K} \rightarrow \Spec A$, $\iota_G:\Spec A \rightarrow \Spec A$를 주는 것은 $\mathbb{K}$-algebra homomorphism $\Delta: A \rightarrow A\otimes_\mathbb{K}A$, $\epsilon: A \rightarrow \mathbb{K}$, $\iota: A \rightarrow A$를 주는 것과 정확히 같다. 남은 것은 세 조건의 대응인데, 동치가 합성과 항등사상을 보존하므로 등식이 등식으로 옮겨간다. 결합법칙 $\mu_G\circ(\mu_G\times\id)=\mu_G\circ(\id\times \mu_G)$은 $(\Delta\otimes\id_A)\circ\Delta=(\id_A\otimes\Delta)\circ\Delta$이 되고, 항등원 조건은 counit 조건이 되며, 역원 조건에서는 $(\iota_G,\id_G)$가 $a\otimes b\mapsto \iota(a)b$, 곧 $\mu\circ(\iota\otimes\id_A)$에 대응하고 $\epsilon_G\circ\pi$가 $\eta\circ\epsilon$에 대응하여 antipode 조건이 된다.

마지막으로 morphism의 대응을 본다. Group scheme homomorphism은 각각의 $T$에서 $G(T) \rightarrow H(T)$가 group homomorphism이 되는 morphism이고, group homomorphism은 항등원과 역원을 자동으로 보존하므로 이는 $\mu_G$, $\epsilon_G$, $\iota_G$ 모두와 commute하는 $\Spec \mathbb{K}$ 위의 morphism과 같다. 위의 동치가 이 세 조건을 뒤집으면 $\Delta$, $\epsilon$, $\iota$ 모두와 commute하는 $\mathbb{K}$-algebra homomorphism, 곧 [정의 6](#def6)의 Hopf algebra homomorphism이 된다.
:::

[정리 7](#thm7)에 의하여 affine group scheme $G=\Spec A$의 $R$-point들의 group 구조는 $A$의 Hopf 구조로 명시된다. 곧 $G(R)=\Hom_{\mathbb{K}\text{-alg}}(A, R)$ 위에서 곱셈은 $g\ast h=\mu_R\circ(g\otimes h)\circ\Delta$, 항등원은 $\eta_R\circ\epsilon$, 역원은 $g\mapsto g\circ\iota$로 주어진다. 이 공식들은 다음 절에서 representation을 comodule로 번역할 때 그대로 쓰인다.

::: 예시 8
[예시 3](#ex3)의 group scheme들의 Hopf 구조는 다음과 같다. 각 경우 $\Delta$와 $\epsilon$은 generator에서의 값으로 결정된다.

1. $\mathbb{G}_a=\Spec \mathbb{Z}[\x]$에 대하여 $\Delta(\x)=\x\otimes 1+1\otimes \x$, $\epsilon(\x)=0$, $\iota(\x)=-\x$이다. 실제로 $\mathbb{G}_a(R)=R$ 위의 덧셈은 $(a,b)\mapsto a+b$이고, 이를 $\x$에 대해 dual하게 읽으면 위의 $\Delta$가 된다.

2. $\mathbb{G}_m=\Spec \mathbb{Z}[\x,\x^{-1}]$에 대하여 $\Delta(\x)=\x\otimes\x$, $\epsilon(\x)=1$, $\iota(\x)=\x^{-1}$이다.

3. $\mu_n=\Spec \mathbb{Z}[\x]/(\x^n-1)$의 구조는 $\mathbb{G}_m$의 것에서 유도된다. $A=\mathbb{Z}[\x,\x^{-1}]$이라 하고 $\bar A=A/(\x^n-1)$이라 하면, $\x^n\otimes\x^n-1\otimes 1=\x^n\otimes(\x^n-1)+(\x^n-1)\otimes 1$이므로 $\Delta$가 $\x^n-1$을 두 원소 $(\x^n-1)\otimes 1$과 $1\otimes(\x^n-1)$이 생성하는 ideal로 보내고, 이 ideal이 $A\otimes_\mathbb{Z}A \rightarrow \bar A\otimes_\mathbb{Z}\bar A$의 kernel이므로 몫에서 잘 정의되기 때문이다.

4. $\GL_n=\Spec \mathbb{Z}[\x_{11},\ldots,\x_{nn},\det{}^{-1}]$에 대하여

   $$\Delta(\x_{ij})=\sum_{l=1}^n\x_{il}\otimes\x_{lj},\qquad \epsilon(\x_{ij})=\delta_{ij}$$

   이며, $\iota(\x_{ij})$는 역행렬 $(\x_{ab})^{-1}$의 $(i,j)$ 성분, 곧 Cramer 공식이 주는 adjugate 행렬의 해당 성분을 $\det$으로 나눈 것이다. $\Delta$의 식은 행렬 곱셈 $(MN)_{ij}=\sum_lM_{il}N_{lj}$를 좌표함수 $\x_{ij}$에 대해 dual하게 읽은 것이다.
:::

[예시 8](#ex8)에서 반복적으로 나타나는 두 형태의 원소가 있다. $\Delta(u)=u\otimes u$이고 $\epsilon(u)=1$인 원소를 *group-like*라 부르고, $\Delta(u)=u\otimes 1+1\otimes u$이고 $\epsilon(u)=0$인 원소를 *primitive*라 부른다. Group-like 원소는 antipode 조건을 적용하면 $\iota(u)u=1$이므로 자동으로 가역이고, 따라서 [정리 7](#thm7)에 의하여 affine group scheme $G=\Spec A$의 coordinate ring의 group-like 원소는 $\mathbb{K}[\y,\y^{-1}] \rightarrow A$ 꼴의 Hopf algebra homomorphism, 곧 group scheme homomorphism $G \rightarrow \mathbb{G}_m$과 일대일대응하고, primitive 원소는 같은 이유로 $G \rightarrow \mathbb{G}_a$와 일대일대응한다. 곧 $\mathbb{G}_m$과 $\mathbb{G}_a$로 가는 homomorphism을 찾는 일이 coordinate ring 안에서 이 두 종류의 원소를 찾는 순수하게 대수적인 문제로 바뀌며, 이 계산이 [명제 14](#prop14)에서 두 무한소 group scheme을 구별하는 데 쓰인다.

## Comodule과 representation

Group의 representation은 벡터공간 위의 선형작용이다. Group scheme의 경우 이를 functorial하게 요구하면, 곧 각 $R$-point가 $R$-계수로 확장된 module 위에 작용하도록 요구하면, affine group scheme의 coordinate ring이 가진 Hopf 구조 덕분에 이 데이터가 하나의 $\mathbb{K}$-linear map으로 압축된다.

::: 정의 9
Ring $\mathbb{K}$ 위의 affine group scheme $G$와 $\mathbb{K}$-module $V$에 대하여, $G$의 $V$ 위로의 *linear representation*이란 각각의 $\mathbb{K}$-algebra $R$마다 group homomorphism

$$r_R: G(R) \rightarrow \Aut_R(V\otimes_\mathbb{K}R)$$

이 주어지고 이것이 $R$에 대해 자연스러운 것이다. 곧 임의의 $\mathbb{K}$-algebra homomorphism $\phi: R \rightarrow R'$과 $g\in G(R)$에 대하여

$$r_{R'}(G(\phi)(g))\circ(\id_V\otimes\phi)=(\id_V\otimes\phi)\circ r_R(g)$$

이 성립하는 것이다. 두 representation $(V, r)$과 $(W, r')$ 사이의 *morphism*은 $\mathbb{K}$-linear map $u: V \rightarrow W$로서, 각각의 $R$과 $g\in G(R)$에 대하여 $r'_R(g)\circ(u\otimes\id_R)=(u\otimes\id_R)\circ r_R(g)$인 것이다.
:::

이 정의에서 $r_R(g)$는 $R$-선형 automorphism이므로, representation은 $V$의 $\mathbb{K}$-구조를 계수확장한 모든 층위에서 동시에 주어진 작용이다. 이를 하나의 대수적 데이터로 압축한 것이 comodule이다.

::: 정의 10
Hopf $\mathbb{K}$-algebra $A$에 대하여, $A$-*comodule<sub>쌍대모듈</sub>*이란 $\mathbb{K}$-module $V$와 $\mathbb{K}$-linear map $\rho: V \rightarrow V\otimes_\mathbb{K}A$로서 다음 두 조건을 만족하는 것이다.

1. $(\rho\otimes\id_A)\circ\rho=(\id_V\otimes\Delta)\circ\rho$.
2. 동일시 $V\otimes_\mathbb{K}\mathbb{K}\cong V$ 아래에서 $(\id_V\otimes\epsilon)\circ\rho=\id_V$.

두 comodule 사이의 *morphism*은 $\mathbb{K}$-linear map $u: V \rightarrow W$로서 $\rho_W\circ u=(u\otimes\id_A)\circ\rho_V$인 것이다.
:::

두 조건은 [정의 6](#def6)의 coassociativity와 counit 조건을 $V$가 받아들이는 형태로 옮긴 것이며, $V=A$이고 $\rho=\Delta$인 경우가 자명한 예이다. 다음 정리가 두 개념이 같은 데이터임을 말해준다.

::: 정리 11
Ring $\mathbb{K}$ 위의 affine group scheme $G=\Spec A$와 $\mathbb{K}$-module $V$에 대하여, $G$의 $V$ 위로의 linear representation과 $V$ 위의 $A$-comodule 구조는 서로 일대일대응한다. 이 대응은 morphism까지 보존하여 두 category의 동치를 준다.
:::
::: 증명
[§아핀스킴, ⁋정리 13](/ko/math/scheme_theory/affine_schemes#thm13)에 의하여 $G(R)=\Hom_{\mathbb{K}\text{-alg}}(A, R)$이고, [정리 7](#thm7) 직후에 적은 대로 그 group 구조는 $g\ast h=\mu_R\circ(g\otimes h)\circ\Delta$, 항등원 $\eta_R\circ\epsilon$, 역원 $g\circ\iota$로 주어진다.

Representation $\{r_R\}$이 주어졌다 하자. $R=A$로 두고 universal element $\id_A\in G(A)$를 택하여 $\sigma=r_A(\id_A)\in \Aut_A(V\otimes_\mathbb{K}A)$라 하고,

$$\rho: V \rightarrow V\otimes_\mathbb{K}A;\qquad \rho(v)=\sigma(v\otimes 1)$$

로 정의한다. 임의의 $g\in G(R)$은 $\mathbb{K}$-algebra homomorphism $g: A \rightarrow R$이고 $G(g)(\id_A)=g$이므로, [정의 9](#def9)의 자연스러움을 $\phi=g$에 적용하여

$$r_R(g)(v\otimes 1)=r_R(g)\left((\id_V\otimes g)(v\otimes 1)\right)=(\id_V\otimes g)(\sigma(v\otimes 1))=(\id_V\otimes g)(\rho(v))\tag{$\ast$}$$

를 얻는다. 곧 representation 전체가 $\rho$ 하나로 복원된다. 이제 $(\ast)$에 $R=\mathbb{K}$, $g=\epsilon$을 대입하면 좌변은 $G(\mathbb{K})$의 항등원에서의 값이므로 $v$이고, 따라서 $(\id_V\otimes\epsilon)\circ\rho=\id_V$이다. 또 $R=A\otimes_\mathbb{K}A$로 두고 $p_1(a)=a\otimes 1$, $p_2(a)=1\otimes a$라 하면 $p_1\ast p_2=\mu_{A\otimes A}\circ(p_1\otimes p_2)\circ\Delta=\Delta$이므로 $r(p_1\ast p_2)=r(p_1)\circ r(p_2)$이고, 양변을 $v\otimes 1$에 적용하여 $(\ast)$로 계산하면 좌변은 $(\id_V\otimes\Delta)(\rho(v))$이며 우변은 $(\rho\otimes\id_A)(\rho(v))$이다. 여기에서 우변의 계산에는 $r(p_1)$이 $A\otimes_\mathbb{K}A$-선형이라는 것과 $r(p_1)(w\otimes 1)=(\id_V\otimes p_1)(\rho(w))$이라는 것을 함께 썼다. 따라서 $\rho$는 comodule 구조이다.

거꾸로 comodule 구조 $\rho$가 주어졌다 하면, $(\ast)$의 우변으로 $r_R(g)$를 정의하고 $R$-선형으로 확장한다. $\rho(v)=\sum_iv_i\otimes a_i$로 적고 $\tau=\id_V\otimes(\mu_R\circ(g\otimes h))$라 두자. 그럼 $g, h\in G(R)$에 대하여

$$\begin{aligned}
r_R(g)\left(r_R(h)(v\otimes 1)\right)&=\sum_ir_R(g)(v_i\otimes 1)h(a_i)=\sum_i(\id_V\otimes g)(\rho(v_i))h(a_i)\\
&=\tau\left((\rho\otimes\id_A)(\rho(v))\right)
\end{aligned}$$

이고, 한편 같은 $\tau$를 $(\id_V\otimes\Delta)(\rho(v))=\sum_iv_i\otimes\Delta(a_i)$에 적용하면

$$\tau\left((\id_V\otimes\Delta)(\rho(v))\right)=\sum_iv_i\otimes(g\ast h)(a_i)=(\id_V\otimes(g\ast h))(\rho(v))=r_R(g\ast h)(v\otimes 1)$$

을 얻는다. 따라서 coassociativity $(\rho\otimes\id_A)\circ\rho=(\id_V\otimes\Delta)\circ\rho$에 의하여 $r_R(g)\circ r_R(h)=r_R(g\ast h)$이다. 또 counit 조건에서 $r_R(\eta_R\circ\epsilon)=\id$인데, $G(R)$이 group이고 그 역원이 $g\circ\iota$이므로 $g\ast(g\circ\iota)$와 $(g\circ\iota)\ast g$가 모두 항등원 $\eta_R\circ\epsilon$이다. 따라서 $r_R(g)\circ r_R(g\circ\iota)$와 $r_R(g\circ\iota)\circ r_R(g)$가 모두 $\id$이 되어 $r_R(g)$는 가역이다. 자연스러움은 $\mathbb{K}$-algebra homomorphism $\phi: R \rightarrow R'$에 대하여

$$r_{R'}(\phi\circ g)(v\otimes 1)=(\id_V\otimes(\phi\circ g))(\rho(v))=(\id_V\otimes\phi)\left((\id_V\otimes g)(\rho(v))\right)=(\id_V\otimes\phi)\left(r_R(g)(v\otimes 1)\right)$$

이 성립하고, 양변을 $x\in V\otimes_\mathbb{K}R$의 함수 $F$로 볼 때 둘 모두 가법적이며 임의의 $c\in R$에 대하여 $F(cx)=\phi(c)F(x)$를 만족하는데 $V\otimes_\mathbb{K}R$가 $R$-module로서 $v\otimes 1$ 꼴의 원소들로 생성되므로, 그러한 원소들에서의 일치가 $V\otimes_\mathbb{K}R$ 전체에서의 일치를 주기 때문이다.

두 구성이 서로 역인 것은 $(\ast)$가 양방향에서 같은 식이기 때문이다. 마지막으로 $u: V \rightarrow W$가 각 $r_R$과 commute하는 것은 $(\ast)$에 의해 $\rho_W\circ u=(u\otimes\id_A)\circ\rho_V$와 동치이므로, 대응은 morphism까지 보존한다.
:::

[정리 11](#thm11)은 affine group scheme의 표현론이 순수하게 대수적인 comodule의 이론으로 번역됨을 말한다. 가장 기본적인 경우를 계산해두자.

::: 예시 12
$\mathbb{K}$ 위의 $\mathbb{G}_m=\Spec \mathbb{K}[\x,\x^{-1}]$에 대하여, $\mathbb{G}_m$의 $V$ 위로의 representation은 $V$의 $\mathbb{Z}$-grading

$$V=\bigoplus_{n\in \mathbb{Z}}V_n$$

과 일대일대응한다. 실제로 $\rho(v)=\sum_n\rho_n(v)\otimes\x^n$으로 적으면 ($\rho_n: V \rightarrow V$는 $\mathbb{K}$-linear이고 각 $v$에 대해 유한히 많은 $n$을 제외하면 $0$이다), $\epsilon(\x^n)=1$이므로 counit 조건은 $\sum_n\rho_n=\id_V$이 되고, $\Delta(\x^n)=\x^n\otimes\x^n$이므로 coassociativity는 $\rho_m\circ\rho_n=0$ ($m\neq n$)과 $\rho_n\circ\rho_n=\rho_n$이 된다. 곧 $\{\rho_n\}$은 합이 항등사상인 직교 idempotent들이고, $V_n=\rho_n(V)$로 두면 $V=\bigoplus_nV_n$이다. 거꾸로 grading이 주어지면 $\rho(v)=\sum_nv_n\otimes\x^n$이 comodule 구조를 준다. $(\ast)$를 통해 대응하는 representation은, $u\in \mathbb{G}_m(R)=R^\times$가 $V_n\otimes_\mathbb{K}R$ 위에 $u^n$배로 작용하는 것이다.
:::

[예시 12](#ex12)의 $V_n$을 weight $n$의 부분이라 부르며, 이 분해는 torus의 작용을 다룰 때 표준적인 도구가 된다. Torus $\mathbb{G}_m^r$의 경우 같은 계산을 반복하면 grading이 $\mathbb{Z}^r$에 의해 매겨지며, 그 각각의 성분이 torus의 한 character에 대응한다.

## Characteristic $p$에서의 예시

지금까지의 예시는 모두 고전적인 algebraic group의 scheme 판본이었다. 그러나 scheme의 언어는 그보다 넓어서, 위상공간으로는 한 점이지만 자명하지 않은 group scheme을 허용한다. 이러한 대상은 characteristic $p$에서 자연스럽게 나타나며, variety의 언어로는 전혀 포착되지 않는다.

::: 예시 13
$\mathbb{K}$를 characteristic $p>0$의 field라 하자.

1. $\mu_p=\Spec \mathbb{K}[\x]/(\x^p-1)$을 생각하자. Characteristic $p$에서 $\x^p-1=(\x-1)^p$이므로 이 ring은 nilpotent를 가지며, 따라서 $\mu_p$는 reduced scheme이 아니다. ([§스킴의 대수구조, ⁋정의 1](/ko/math/scheme_theory/algebra_of_schemes#def1)) 위상공간으로서 $\mu_p$는 한 점 $(\x-1)$뿐이고, $\mu_p(\mathbb{K})=\{a\in \mathbb{K}\mid a^p=1\}=\{1\}$이므로 $\mathbb{K}$-point로는 항등원 하나밖에 보이지 않는다.

2. Characteristic $p$에서 $\Frob: \mathbb{G}_a \rightarrow \mathbb{G}_a$를 각각의 $\mathbb{K}$-algebra $R$에서 $a\mapsto a^p$로 정의하면, $(a+b)^p=a^p+b^p$이므로 이는 group scheme homomorphism이다. 그 kernel

   $$\alpha_p=\ker \Frob=\Spec \mathbb{K}[\x]/(\x^p)$$

   은 $\alpha_p(R)=\{a\in R\mid a^p=0\}$을 만족하는 group scheme이며 ([명제 5](#prop5)), 역시 위상공간으로는 한 점이고 reduced가 아니다. 그 Hopf 구조는 $\mathbb{G}_a$에서 유도되어 $\Delta(\x)=\x\otimes 1+1\otimes\x$, $\epsilon(\x)=0$, $\iota(\x)=-\x$이다. Characteristic $p$에서 $(\x\otimes 1+1\otimes\x)^p=\x^p\otimes 1+1\otimes\x^p$이므로 이 $\Delta$가 $\mathbb{K}[\x]/(\x^p)$에서 잘 정의된다.
:::

두 group scheme은 각각 $\mathbb{G}_m$과 $\mathbb{G}_a$ 안에 무한소로 들어앉아 있으며, 밑에 깔린 scheme으로는 서로 구별되지 않는다. 실제로 $\t=\x-1$로 치환하면 $\mathbb{K}[\x]/(\x^p-1)=\mathbb{K}[\t]/(\t^p)$이므로 $\mu_p$와 $\alpha_p$는 $\mathbb{K}$-scheme으로서 isomorphic하다. 그럼에도 group 구조는 다르다.

::: 명제 14
$\mathbb{K}$가 characteristic $p>0$의 field이면 $\mathbb{K}$ 위의 group scheme homomorphism $\alpha_p \rightarrow \mathbb{G}_m$은 자명한 것 하나뿐이다. 따라서 $\mu_p$와 $\alpha_p$는 group scheme으로서 isomorphic하지 않다.
:::
::: 증명
$\mathbb{G}_m=\Spec \mathbb{K}[\y,\y^{-1}]$으로 적자. [정리 7](#thm7)에 의하여 group scheme homomorphism $\alpha_p \rightarrow \mathbb{G}_m$은 Hopf algebra homomorphism $\mathbb{K}[\y,\y^{-1}] \rightarrow \mathbb{K}[\x]/(\x^p)$와 대응하고, 이러한 사상은 $\y$의 image $u$에 의해 결정된다. $\mathbb{G}_m$의 Hopf 구조가 $\Delta(\y)=\y\otimes\y$, $\epsilon(\y)=1$이므로 ([예시 8](#ex8)), 조건은 $u$가 가역이고

$$\Delta(u)=u\otimes u,\qquad \epsilon(u)=1$$

인 것이다. $u=\sum_{i=0}^{p-1}a_i\x^i$로 적으면 $\epsilon(u)=a_0=1$이며, 이로부터 $u$는 자동으로 가역이다. 이제 $\Delta(\x)=\x\otimes 1+1\otimes\x$이므로

$$\Delta(u)=\sum_{i=0}^{p-1}a_i\sum_{j=0}^i\binom{i}{j}\x^j\otimes \x^{i-j}$$

이고, $\{\x^j\otimes\x^l\}_{0\leq j,l\leq p-1}$이 $\mathbb{K}[\x]/(\x^p)\otimes_\mathbb{K}\mathbb{K}[\x]/(\x^p)$의 기저이므로 $\Delta(u)=u\otimes u$는 다음 두 조건과 동치이다. 첫째로 $j+l\leq p-1$인 경우

$$\binom{j+l}{j}a_{j+l}=a_ja_l$$

이고, 둘째로 $j+l\geq p$이면서 $j, l\leq p-1$인 경우 $a_ja_l=0$이다. 첫째 조건에서 $j=1$, $l=i-1$로 두면 $1\leq i\leq p-1$마다 $ia_i=a_1a_{i-1}$인데, 이 범위에서 $i$는 $\mathbb{K}$에서 가역이므로 귀납적으로 $a_i=a_1^i/i!$을 얻는다. 한편 $p\geq 2$이므로 $2(p-1)\geq p$이고, 둘째 조건에 $j=l=p-1$을 대입하면 $a_{p-1}^2=0$, 곧 $a_{p-1}=0$이다. 따라서 $a_1^{p-1}/(p-1)!=0$이므로 $a_1=0$이고, 다시 $a_i=a_1^i/i!$에 의해 $i\geq 1$인 모든 $a_i$가 $0$이다. 곧 $u=1$이며 이는 자명한 homomorphism이다.

한편 $\mu_p$는 $\mathbb{G}_m$의 closed subgroup scheme이므로 그 포함사상은 $\mu_p \rightarrow \mathbb{G}_m$의 homomorphism이고, 이는 $\y\mapsto \x$에 대응하는데 $\mathbb{K}[\x]/(\x^p-1)$에서 $\x\neq 1$이므로 자명하지 않다. 만일 $\mu_p\cong \alpha_p$이었다면 $\mathbb{G}_m$으로 가는 homomorphism들의 두 집합이 일대일대응하였을 것이므로 모순이다.
:::

[명제 14](#prop14)는 group scheme의 정보가 밑에 깔린 scheme에 담기지 않는다는 것을 분명히 보여준다. Characteristic $0$의 field 위에서는 finite type group scheme이 항상 smooth라는 Cartier의 정리가 있어 이러한 현상이 일어나지 않지만, characteristic $p$에서는 $\mu_p$나 $\alpha_p$ 같은 무한소 대상이 필연적으로 나타나며 이들을 다룰 수 있다는 것이 scheme 언어의 실질적인 이득이다.

## Torsor

Group scheme이 등장하는 가장 중요한 기하학적 상황은, 어떤 대상 위에 group이 단순추이적으로 작용하지만 기준점이 정해져 있지 않은 경우이다. 위상수학의 principal bundle이 그러하듯, 이러한 대상은 국소적으로만 group 자신과 같아 보인다. 우선 작용을 정의한다.

::: 정의 15
$S$ 위의 group scheme $G$의 $S$-scheme $X$ 위로의 *left action*이란 $S$-scheme morphism $\sigma: G\times_SX \rightarrow X$로서, 각각의 $S$-scheme $T$에 대하여 유도되는 map

$$\sigma_T: G(T)\times X(T) \rightarrow X(T)$$

이 group $G(T)$의 집합 $X(T)$ 위로의 작용인 것이다.
:::

여기에서도 [§점함자, ⁋명제 11](/ko/math/scheme_theory/functor_of_points#prop11)과 [§점함자, ⁋따름정리 2](/ko/math/scheme_theory/functor_of_points#cor2)에 의하여, 이 조건은 $\sigma\circ(\mu_G\times\id_X)=\sigma\circ(\id_G\times\sigma)$와 $\sigma\circ(\epsilon_G\circ\pi_X, \id_X)=\id_X$이라는 두 등식과 동치이다. 여기에서 $\pi_X: X \rightarrow S$는 structure morphism이다. 가장 기본적인 작용은 $G$ 자신 위로의 left translation, 곧 $\sigma=\mu_G$인 경우이다. Torsor는 이 자명한 예를 국소적으로만 닮은 대상이다.

::: 정의 16
$S$ 위의 group scheme $G$와 left action $\sigma: G\times_SP \rightarrow P$를 가진 $S$-scheme $P$에 대하여, $P$가 *$G$-torsor*라는 것은 다음 두 조건이 성립하는 것이다.

1. $P \rightarrow S$는 faithfully flat이고 ([§평탄사상, ⁋정의 1](/ko/math/scheme_theory/flat_morphisms#def1)) locally of finite presentation이다. ([§스킴 사상의 성질들, ⁋정의 18](/ko/math/scheme_theory/properties_of_scheme_morphisms#def18))
2. 작용과 사영이 유도하는 morphism

   $$(\sigma, \operatorname{pr}_2): G\times_SP \rightarrow P\times_SP$$

   이 isomorphism이다.

$G$-torsor $P$가 *trivial*하다는 것은, left translation 작용을 가진 $G$ 자신과 $G$-동변인 $S$-scheme isomorphism이 존재하는 것이다.
:::

둘째 조건을 functor의 언어로 읽으면 명확해진다. [§점함자, ⁋명제 11](/ko/math/scheme_theory/functor_of_points#prop11)에 의하여 각각의 $S$-scheme $T$에 대하여 이 조건은 map

$$G(T)\times P(T) \rightarrow P(T)\times P(T);\qquad (g, q)\mapsto (g\cdot q, q)$$

이 전단사인 것, 곧 임의의 두 점 $q, q'\in P(T)$에 대하여 $g\cdot q=q'$인 $g\in G(T)$가 유일하게 존재하는 것이다. 다시 말해 $P(T)$가 비어있지 않을 때마다 $G(T)$가 그 위에 단순추이적으로 작용한다. 첫째 조건은 $P$가 $S$ 위에서 충분히 고르게 퍼져 있어 그 자신이 covering의 역할을 할 수 있도록 요구하는 것이다. 이 둘을 합치면 다음을 얻는다.

::: 명제 17
$S$ 위의 $G$-torsor $P$에 대하여, $P$가 trivial한 것과 $P(S)\neq \emptyset$인 것, 곧 $P \rightarrow S$가 절단을 가지는 것은 동치이다.
:::
::: 증명
$P$가 trivial하면 $G$의 항등원 $\epsilon_G\in G(S)$에 대응하는 원소가 $P(S)$의 원소를 주므로 절단이 존재한다.

거꾸로 절단 $s\in P(S)$가 주어졌다 하자. 합성

$$\varphi: G\cong G\times_SS\xrightarrow{\ \id_G\times s\ }G\times_SP\xrightarrow{\ \sigma\ }P$$

를 생각하면, 각각의 $S$-scheme $T$에서 $\varphi_T(g)=g\cdot s_T$이다. 여기에서 $s_T\in P(T)$는 $s$를 $T \rightarrow S$를 따라 끌어당긴 것이다. [정의 16](#def16)의 둘째 조건이 주는 전단사 $G(T)\times P(T) \rightarrow P(T)\times P(T)$에서 둘째 좌표를 $s_T$로 고정하면, $g\mapsto g\cdot s_T$가 $G(T)$에서 $P(T)$로의 전단사임을 얻는다. 이 전단사는 $T$에 대해 자연스러우므로 [§점함자, ⁋따름정리 2](/ko/math/scheme_theory/functor_of_points#cor2)에 의하여 $\varphi$는 isomorphism이다. 또 $\varphi_T(g'g)=(g'g)\cdot s_T=g'\cdot\varphi_T(g)$이므로 $\varphi$는 $G$-동변이며, 따라서 $P$는 trivial하다.
:::

[명제 17](#prop17)은 torsor가 자명한지의 여부가 오로지 대역적인 절단의 존재에 달려 있음을 말한다. 그런데 torsor는 정의상 자기 자신 위로 끌어올리면 언제나 절단을 가진다. 이것이 다음 명제의 내용이며, 여기에서 covering의 의미는 flat이고 locally of finite presentation이며 전사인 morphism들의 모임, 곧 *fppf covering*이다. 이러한 covering에서 base의 각 affine open subset이 유한히 많은 affine open subset의 image로 덮이기까지 하면 [§충실평탄 하강, ⁋정의 8](/ko/math/scheme_theory/faithfully_flat_descent#def8)의 fpqc covering이 되므로, 하강에 관한 그 글의 결과들을 그대로 쓸 수 있다.

::: 명제 18
$S$ 위의 $G$-torsor $P$에 대하여 다음이 성립한다.

1. 둘째 사영 $P\times_SP \rightarrow P$는 $P$ 위의 group scheme $G_P=G\times_SP$에 대한 torsor이며 trivial하다. 곧 $P$는 fppf covering $\{P \rightarrow S\}$ 위에서 자명해진다.
2. $G \rightarrow S$가 affine이고 $P \rightarrow S$가 quasi-compact이면 ([§스킴 사상의 성질들, ⁋정의 2](/ko/math/scheme_theory/properties_of_scheme_morphisms#def2)) $P \rightarrow S$ 또한 affine이다.
:::
::: 증명
1번을 보자. [정의 16](#def16)의 두 조건은 base change에 대해 보존된다. 실제로 flat은 base change에 대해 보존되고 ([§평탄사상, ⁋명제 3](/ko/math/scheme_theory/flat_morphisms#prop3)), surjective와 locally of finite presentation도 그러하며 ([§올곱, ⁋명제 16](/ko/math/scheme_theory/fiber_products#prop16)), 둘째 조건의 isomorphism은 base change하여도 isomorphism이기 때문이다. 따라서 둘째 사영 $P\times_SP \rightarrow P$는 $P$ 위의 $G_P$-torsor이다. 그런데 diagonal morphism $\Delta: P \rightarrow P\times_SP$가 이 사영의 절단이므로, [명제 17](#prop17)에 의하여 이 torsor는 trivial하다. 곧 $P$ 위에서 $P\times_SP\cong G\times_SP$이다. 한편 $P \rightarrow S$는 정의에 의하여 flat, locally of finite presentation, 전사이므로 $\{P \rightarrow S\}$는 fppf covering이다.

2번을 보이기 위해 먼저 $\{P \rightarrow S\}$가 fpqc covering임을 확인한다. $S$의 affine open subset $V$를 택하면 $V$는 quasi-compact이고 ([§스펙트럼, ⁋보조정리 12](/ko/math/scheme_theory/spectrums#lem12)), $P \rightarrow S$가 quasi-compact이므로 그 preimage 또한 quasi-compact이어서 유한히 많은 affine open subset들로 덮인다. $P \rightarrow S$가 전사이므로 이들의 image가 $V$를 덮으며, 나머지 조건은 1번에서 이미 확인하였으므로 [§충실평탄 하강, ⁋정의 8](/ko/math/scheme_theory/faithfully_flat_descent#def8)의 조건이 모두 성립한다.

이제 affine은 base change에 대해 보존되므로 ([§올곱, ⁋명제 16](/ko/math/scheme_theory/fiber_products#prop16)) $G\times_SP \rightarrow P$는 affine이고, 1번에 의하여 이는 $P\times_SP \rightarrow P$, 곧 $P \rightarrow S$를 자기 자신을 따라 base change한 것과 isomorphic하다. 그런데 affine이라는 성질은 fpqc covering에 대해 base에서 국소적이므로 ([§충실평탄 하강, ⁋명제 12](/ko/math/scheme_theory/faithfully_flat_descent#prop12)), $P \rightarrow S$ 자신이 affine이다.
:::

[명제 18](#prop18)의 둘째 항에 붙은 quasi-compact 가정은 fppf covering $\{P \rightarrow S\}$를 fpqc covering으로 올려 하강 결과를 쓸 수 있게 하기 위한 것이며, $P$가 Noetherian scheme인 경우에는 [§스킴 사상의 성질들, ⁋명제 4](/ko/math/scheme_theory/properties_of_scheme_morphisms#prop4)에 의하여 자동으로 성립한다.

[명제 18](#prop18)은 torsor를 $G$의 *form*으로 규정한다. 곧 torsor는 대역적으로는 $G$와 다를 수 있으나, 적당한 fppf covering으로 올라가면 언제나 $G$ 자신이 된다. 이 관점에서 torsor는 [§충실평탄 하강, ⁋정의 4](/ko/math/scheme_theory/faithfully_flat_descent#def4)의 descent datum으로 기술되며, $G$가 affine인 경우 [§충실평탄 하강, ⁋정리 11](/ko/math/scheme_theory/faithfully_flat_descent#thm11)에 의하여 그러한 데이터가 실제로 $S$ 위의 scheme을 산출한다. 자명하지 않은 torsor가 실제로 존재한다는 것은 다음 예시가 보여준다.

::: 예시 19
1. $S=\Spec \mathbb{R}$, $P=\Spec \mathbb{C}$이라 하고, $G$를 $\mathbb{Z}/2$의 constant group scheme, 곧 두 개의 $S$의 복사본의 disjoint union $\Spec(\mathbb{R}\times\mathbb{R})$이라 하자. 이는 $G(T)$가 locally constant function $\lvert T\rvert \rightarrow \mathbb{Z}/2$들이 이루는 group이 되도록 하는 group scheme이며, $T$의 connected component들이 열려 있는 경우에는 이것이 component마다 $\mathbb{Z}/2$의 원소를 고르는 것과 같다. 복소켤레가 $\mathbb{R}$-algebra automorphism이므로, 한 복사본 위에서는 $\id_P$로 다른 복사본 위에서는 켤레로 정의하여 작용 $\sigma: G\times_SP \rightarrow P$를 얻는다. $\mathbb{C}$가 $\mathbb{R}$ 위의 rank $2$ free module이므로 $P \rightarrow S$는 faithfully flat이고 locally of finite presentation이다. 또 $G\times_SP=\Spec(\mathbb{C}\times\mathbb{C})$이고 $P\times_SP=\Spec(\mathbb{C}\otimes_\mathbb{R}\mathbb{C})$인데, 위의 $\sigma$가 $\sigma^\sharp(z)=(z,\bar z)$를 주므로 $(\sigma, \operatorname{pr}_2)$의 dual은

   $$\mathbb{C}\otimes_\mathbb{R}\mathbb{C} \rightarrow \mathbb{C}\times\mathbb{C};\qquad z\otimes w\mapsto (zw, \bar zw)$$

   이다. 이것이 $\mathbb{R}$-algebra isomorphism이므로 [정의 16](#def16)의 둘째 조건도 성립한다. 그러나 $\mathbb{R}$-algebra homomorphism $\mathbb{C} \rightarrow \mathbb{R}$은 존재하지 않으므로 $P(S)=\emptyset$이고, [명제 17](#prop17)에 의하여 이 torsor는 자명하지 않다.

2. Scheme $S$ 위의 invertible sheaf $\mathcal{L}$에 대하여 ([§준연접층, ⁋정의 12](/ko/math/scheme_theory/quasicoherent_sheaves#def12)), $\mathcal{L}$을 trivialize하는 open cover $\{U_i\}$와 transition unit $g_{ij}\in \Gamma(U_i\cap U_j, \mathcal{O}_S^\times)$를 택하자. 이들은 $\mathcal{L}\vert_{U_i}\cong \mathcal{O}_{U_i}$인 자명화들 사이의 좌표변환이므로 $U_i\cap U_j\cap U_k$ 위에서 $g_{ij}g_{jk}=g_{ik}$를 만족한다. 그럼 $\mathbb{G}_{m}\times_SU_i$들을 겹침 위에서 $(t, u)\mapsto (g_{ij}(u)t, u)$로 붙이면 이 등식이 [§스킴, ⁋보조정리 9](/ko/math/scheme_theory/schemes#lem9)의 cocycle condition을 그대로 주므로 $S$-scheme $P_\mathcal{L}$을 얻으며, 왼쪽 곱셈이 이 접합과 commute하므로 $P_\mathcal{L}$은 $\mathbb{G}_m$-torsor가 된다. Zariski open cover는 fppf covering이고 [정의 16](#def16)의 두 조건은 모두 국소적으로 확인되기 때문이다. 이 torsor의 절단은 $s_i\in \Gamma(U_i,\mathcal{O}_S^\times)$들로서 $s_i=g_{ij}s_j$를 만족하는 것, 곧 어디에서도 사라지지 않는 $\mathcal{L}$의 global section이므로, [명제 17](#prop17)에 의하여 $P_\mathcal{L}$이 자명한 것과 $\mathcal{L}\cong \mathcal{O}_S$인 것이 동치이다.
:::

[예시 19](#ex19)의 둘째 경우는 $\mathbb{G}_m$-torsor가 invertible sheaf와 같은 정보를 담고 있음을 시사한다. 그럼 자연스러운 다음 질문은 주어진 $S$와 $G$에 대하여 $G$-torsor 전체를 분류하는 것인데, [명제 17](#prop17)이 말해주듯 자명하지 않은 torsor의 존재는 대역적인 절단의 부재라는 형태의 장애이므로, 이 분류는 cohomology의 문제가 된다. 또 하나의 길은 torsor들을 개별적으로 세는 대신 그들이 이루는 groupoid를 그대로 하나의 기하학적 대상으로 삼는 것이며, field $\mathbb{K}$ 위에서 $\mathbb{G}_m$-torsor를 분류하는 $[\Spec \mathbb{K}/\mathbb{G}_m]$과 같은 quotient stack이 그렇게 얻어지는 대상으로서 stack 이론의 출발점이 된다.

---

**참고문헌**

**[Har]** R. Hartshorne, *Algebraic geometry*. Graduate texts in mathematics. Springer, 1977.  
**[Vak]** R. Vakil, *The rising sea: Foundation of algebraic geometry*. Available [online](https://math.stanford.edu/~vakil/216blog/).
