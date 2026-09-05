---
title: "차원"
description: "스킴의 차원을 Krull dimension으로 정의하고, 가환대수학적 차원과의 관계를 살펴본다. Finite morphism과 integral morphism의 성질을 함께 다룬다."
excerpt: "Scheme의 dimension 정의와 local ring의 Krull dimension과의 관계"

categories: [Math / Scheme Theory]
permalink: /ko/math/scheme_theory/dimension
sidebar: 
    nav: "scheme_theory-ko"

date: 2025-03-14
weight: 13

drift_needed: true



---

## 스킴의 차원

이제 우리는 scheme의 차원을 정의한다.

::: 정의 1
Scheme $X$의 *dimension<sub>차원</sub>*은 위상공간 $X$의 Krull dimension으로 정의한다. ([\[위상수학\] §차원, ⁋정의 10](/ko/math/topology/dimension#def10))
:::

그럼 [§스펙트럼, ⁋명제 16](/ko/math/scheme_theory/spectrums#prop16)의 Galois correspondence로부터 우리는 $\Spec A$의 scheme으로서의 차원과 $A$의 ring으로서의 차원이 같다는 것을 안다. ([\[가환대수학\] §차원, ⁋정의 1](/ko/math/commutative_algebra/Krull_dimension#def1)) 뿐만 아니라, 정의에 의하여 $\Spec A$와 $\Spec A/\mathfrak{N}(A)$가 homeomorphic하다는 것을 보일 수 있으므로 $\dim A=\dim A/\mathfrak{N}(A)$가 성립한다. 즉 reducedness는 차원에 영향을 주지 않는다. 

한편 [\[위상수학\] §차원, ⁋명제 15](/ko/math/topology/dimension#prop15)와 마찬가지 이유로 다음이 성립한다. 

::: 명제 2
임의의 scheme $X$와 정수 $n\geq 0$에 대하여, $\dim X=n$인 것은 $X$의 affine open covering $(U_i)$가 존재하여, 모든 $U_i$에 대하여 $\dim U_i\leq n$이고, 적어도 하나의 $i$에 대해서는 등호가 성립하는 것과 동치이다. 
:::
::: 증명
$X$의 임의의 irreducible closed subset들의 chain

$$Y_0\subsetneq Y_1\subsetneq\cdots\subsetneq Y_r$$

에서 가장 작은 항 $Y_0$의 generic point $\eta_0$는 $X$의 점이므로 covering $(U_i)$에 의해 어떤 $U_i$에 속한다. 그러면 chain의 모든 항이 $U_i$와 만나므로, [\[위상수학\] §차원, ⁋명제 15](/ko/math/topology/dimension#prop15)의 inclusion-preserving bijection을 생각하면 $U_i$ 안의 같은 길이의 chain으로 대응된다. 거꾸로 $U_i$의 임의의 chain은 $X$ 안에서 closure를 취해 올려지므로 $\dim X\geq\dim U_i$이고, 따라서 $\dim X=\sup_i\dim U_i$이며 이는 명제의 조건과 동치이다.
:::

증명이 실제로 준 것은 $\dim X=\sup_i\dim U_i$이며, $\dim X$가 유한하다는 가정이 없으면 등호가 성립하는 $i$가 존재하지 않을 수도 있다. 가령 $X=\coprod_{d\geq 0}\mathbb{A}^d_\mathbb{K}$는 무한차원이지만 각각의 affine open subset은 유한히 많은 성분만 만나므로 모두 유한차원이다.

한편 우리는 [§스킴 사상의 성질들, ⁋명제 15](/ko/math/scheme_theory/properties_of_scheme_morphisms#prop15)에서 finite morphism은 integral morphism of finite type인 것을 살펴보았으며, [§올곱, ⁋명제 15](/ko/math/scheme_theory/fiber_products#prop15)에서 임의의 finite morphism은 quasi-finite인 것을 살펴보았다. 일반적으로 integral morphism이지만 finite type은 아닌 morphism이 존재하며, 따라서 아직까지는 integral morphism의 fiber에 대한 이야기를 할 수가 없다.

::: 예시 3
예를 들어 $\mathbb{Q}$의 algebraic closure $\overline{\mathbb{Q}}$를 생각하자. $\overline{\mathbb{Q}}$의 임의의 원소는 $\mathbb{Q}$ 위에서 algebraic하므로 integral이고, 따라서 $\mathbb{Q} \rightarrow \overline{\mathbb{Q}}$는 integral extension이며 이로부터 scheme morphism $\varphi:\Spec \overline{\mathbb{Q}} \rightarrow \Spec \mathbb{Q}$도 integral morphism이다.

이제 $\varphi$를 $\Spec\overline{\mathbb{Q}}\rightarrow\Spec\mathbb{Q}$로 base change하면, 다음의 pullback diagram

{% diagram Math/Scheme_Theory/Dimension_Schemes-1.svg width="13.60em" alt="pullback" %}

을 얻으며, 이 때 좌측 수직방향의 map

$$\Spec(\overline{\mathbb{Q}}\otimes_\mathbb{Q}\overline{\mathbb{Q}})\rightarrow \Spec \overline{\mathbb{Q}}$$

또한 [§올곱, ⁋명제 16](/ko/math/scheme_theory/fiber_products#prop16)에 의하여 integral이다. 

이 map을 살펴보기 위해, 구체적으로 ring homomorphism $\overline{\mathbb{Q}}\rightarrow \overline{\mathbb{Q}}\otimes_\mathbb{Q}\overline{\mathbb{Q}}$를 살펴보자. 위의 scheme 사이의 map의 section을 보는 것은 이 함수의 retraction을 보는 것과 같으며 이는 임의의 $\sigma\in\Gal(\overline{\mathbb{Q}}/\mathbb{Q})$에 대하여 다음의 surjective ring homomorphism

$$\overline{\mathbb{Q}}\otimes_\mathbb{Q}\overline{\mathbb{Q}}\rightarrow\overline{\mathbb{Q}},\qquad a\otimes b\mapsto a\sigma(b)$$

으로부터 온다. 구체적으로, 이 ring homomorphism의 kernel $\mathfrak{p}_\sigma$는 maximal ideal이므로 $\Spec(\overline{\mathbb{Q}}\otimes_\mathbb{Q}\overline{\mathbb{Q}})$의 한 점을 정의하며, $\sigma\neq\tau$이면 $\sigma(b)\neq\tau(b)$인 $b\in\overline{\mathbb{Q}}$를 택할 때 $1\otimes b-\sigma(b)\otimes 1\in\mathfrak{p}_\sigma$이지만 $\mathfrak{p}_\tau$에는 속하지 않으므로 $\mathfrak{p}_\sigma\neq\mathfrak{p}_\tau$이다. 따라서 $\Spec(\overline{\mathbb{Q}}\otimes_\mathbb{Q}\overline{\mathbb{Q}})$은 적어도 $\Gal(\overline{\mathbb{Q}}/\mathbb{Q})$만큼의, 곧 무한히 많은 점을 가지며, $\Spec(\overline{\mathbb{Q}}\otimes_\mathbb{Q}\overline{\mathbb{Q}})\rightarrow\Spec\overline{\mathbb{Q}}$는 quasi-finite morphism이 아니므로 finite morphism도 아니다.
:::

혹은 더 간단한 예로 $\Spec \mathbb{C}\rightarrow \Spec \mathbb{R}$을 보자. 여기서 $\mathbb{R}$와 $\mathbb{C}$가 모두 field이므로 $\Spec\mathbb{C}$와 $\Spec\mathbb{R}$는 각각 한 점이며, 따라서 이 map 자체는 한 점에서 한 점으로 가는 trivial한 map이다. 그러나 이를 $\Spec \mathbb{C}\rightarrow \Spec \mathbb{R}$로 pullback하여 위의 예시와 비슷한 함수

$$\Spec(\mathbb{C}\otimes_\mathbb{R} \mathbb{C}) \rightarrow \Spec \mathbb{C}$$

를 만들면 $\mathbb{C}\otimes_\mathbb{R}\mathbb{C}$는 더 이상 field가 아니다. 실제로 $\Spec\mathbb{C}=\Spec\mathbb{R}[\x]/(\x^2+1)$이므로, 

$$\mathbb{C}\otimes_\mathbb{R} \mathbb{C}\cong \mathbb{C}\otimes_\mathbb{R} \frac{\mathbb{R}[\x]}{(\x^2+1)}\cong \frac{\mathbb{C}[\x]}{(\x^2+1)}$$

이며, $\x^2+1$은 $\mathbb{C}$에서는 두 일차식의 곱 $\x^2+1=(\x-i)(\x+i)$로 인수분해되며, $(\x-i)$와 $(\x+i)$는 comaximal이므로 [\[환론\] §중국인의 나머지정리, ⁋명제 6](/ko/math/ring_theory/chinese_remainder_theorem#prop6)에 의하여 

$$\frac{\mathbb{C}[\x]}{((\x-i)(\x+i))}\cong\frac{\mathbb{C}[\x]}{(\x-i)}\times\frac{\mathbb{C}[\x]}{(\x+i)}\cong\mathbb{C}\times\mathbb{C}$$

가 된다. 위의 예시에서 살펴본 Galois group의 언어로 생각하면 이는 위 분해의 두 factor $\mathbb{C}[\x]/(\x-i)$와 $\mathbb{C}[\x]/(\x+i)$가 곧 $\mathbb{R}$을 고정하는 $\mathbb{C}\rightarrow \mathbb{C}$의 automorphism, 즉 $\Gal(\mathbb{C}/\mathbb{R})$의 두 원소에 해당하기 때문에 나타나는 것이며 같은 일이 [예시 3](#ex3)의 $\mathbb{Q}\rightarrow \overline{\mathbb{Q}}$에서도 나타난다. 유일한 차이는 $\Gal(\overline{\mathbb{Q}}/\mathbb{Q})$는 무한하므로 fiber가 두 개가 아닌 무한개가 된다는 것이다. 

그럼에도 이 예시는 integral morphism의 fiber에 대한 어떠한 종류의 finiteness를 암시하는데, 가령 $\Gal(\overline{\mathbb{Q}}/\mathbb{Q})$는 profinite group이므로 ([\[체론\] §갈루아 군의 성질들, ⁋명제 5](/ko/math/field_theory/properties_of_galois_extensions#prop5)) $0$차원이 된다. 이는 임의의 integral morphism에 대해서도 성립하는 사실이다. 

::: 명제 4
Integral morphism $\varphi: X \rightarrow Y$의 공집합이 아닌 임의의 fiber는 항상 $0$차원이다. 
:::
::: 증명
정의에 의해 $Y$의 한 점 $y$에서의 fiber는 [§스킴, ⁋정의 5](/ko/math/scheme_theory/schemes#def5)의 residue field $\kappa(y)$에 대한 inclusion map $\Spec \kappa(y) \rightarrow Y$에 의한 $\varphi$의 base change

$$\varphi^{-1}(y)=X\times_Y\Spec \kappa(y)$$

으로 주어지며, integral morphism은 base change에 의해 보존되므로 ([§올곱, ⁋명제 16](/ko/math/scheme_theory/fiber_products#prop16))

$$\varphi^{-1}(y)=X\times_Y\Spec \kappa(y) \rightarrow \Spec \kappa(y)$$

는 integral morphism이며, integral morphism은 그 정의에 의해 affine morphism이므로 integral morphism $\Spec B \rightarrow \Spec \kappa(y)$에 대하여 $\dim \Spec B=\dim B=0$임을 보이면 충분하다. 즉, 임의의 integral extension $\kappa(y) \rightarrow B$에 대하여, $B$의 prime ideal들의 chain

$$\mathfrak{q}_1\subsetneq \mathfrak{q}_2$$

이 존재할 수 없음을 보여야 한다. 이는 [\[가환대수학\] §정수적 확장과 아이디얼, ⁋따름정리 4](/ko/math/commutative_algebra/lying_over_and_going_up#cor4)의 결과이다. 
:::

기하적으로, 이 명제는 integral morphism의 각 fiber가 양의 차원을 갖지 않는다는 것을 보여준다. 

위의 명제의 증명에서 사용한 [\[가환대수학\] §정수적 확장과 아이디얼, ⁋따름정리 4](/ko/math/commutative_algebra/lying_over_and_going_up#cor4)는 임의의 integral extension $A\hookrightarrow B$에 대해서도 성립한다. 이에 의해 $B$의 prime ideal chain을 $A$로 contraction하면 여전히 strict하므로 $\dim B\leq\dim A$이고, 거꾸로 [\[가환대수학\] §정수적 확장과 아이디얼, ⁋명제 1](/ko/math/commutative_algebra/lying_over_and_going_up#prop1)의 lying over와 going up에 의해 $A$의 prime ideal chain은 $B$로 올려지므로 $\dim A\leq\dim B$이다. 따라서 더 일반적으로 다음이 성립한다.

::: 명제 5
임의의 integral extension $\phi:A \hookrightarrow B$에 대하여 

$$\dim\Spec A=\dim\Spec B$$

가 항상 성립한다. 
:::

특히 임의의 integral domain $A$와 그 normalization $\tilde{A}$에 대하여, extension $A\hookrightarrow\tilde{A}$가 integral이므로 [명제 5](#prop5)에 의하여 $\dim\Spec\tilde{A}=\dim\Spec A$이다. 여기서 normalization $\tilde{A}$는 $A$를 그 field of fractions $\Frac(A)$ 안에서 integrally closed가 되도록 확장한 것, 곧 $\Frac(A)$의 원소 가운데 $A$ 위에서 integral인 것들을 모두 $A$에 붙여 얻는 확장이다. ([\[가환대수학\] §정수적 확장, ⁋정의 3](/ko/math/commutative_algebra/integral_extension#def3)) 정의에 의해 $A\subseteq\tilde{A}\subseteq\Frac(A)$이므로 $\Frac(\tilde{A})=\Frac(A)$, 즉 normalization은 $A$의 function field를 보존한다.

::: 예시 6
위의 논의에서 우리는 normalization이 function field를 보존한다는 것을 살펴보았다. 기하적으로, $A$가 $\mathbb{K}$ 위의 affine variety의 coordinate ring인 경우 이는 normalization으로 얻어지는 두 공간이 birational하다는 것이다. ([\[대수다양체\] §유리사상, ⁋명제 10](/ko/math/algebraic_varieties/rational_maps#prop10)) 즉, normalization은 무시할만큼 작은 특정한 loci 바깥에서는 원래의 공간과 같다. 

Normalization이 실제로 달라지는 곳은 $A$가 integrally closed가 아닌 locus, 곧 non-normal locus이다. 이는 singular locus에 포함되지만 일반적으로 그와 같지는 않다. 가령 quadric cone $\mathbb{K}[\x,\y,\z]/(\x\y-\z^2)$는 원점에서 singular인 $2$차원 domain이지만 normal이므로 normalization이 항등사상이 되어 singular point가 그대로 남는다. 그러나 곡선의 경우, 곧 $1$차원에서는 normal인 local ring이 정확히 regular local ring이므로 non-normal locus가 singular locus와 일치한다. 대표적인 예로 [\[대수다양체\] §접공간과 매끄러움, ⁋예시 7](/ko/math/algebraic_varieties/tangent_spaces_and_smoothness#ex7)의 cusp

$$A=\mathbb{K}[\x,\y]/(\y^2-\x^3)\cong\mathbb{K}[t^2,t^3]$$

를 보자. $A$의 field of fractions를 보기 위해 $t=\y/\x$임을 사용하면 $\Frac(A)=\mathbb{K}(t)$임을 확인할 수 있고, 이 때 원소 $t\in\Frac(A)$는 $t^2=\x\in A$를 만족하므로 $A$ 위에서 integral이다. 따라서 $t$를 붙여 얻은 extension 

$$A[t]=\mathbb{K}[t^2,t^3,t]=\mathbb{K}[t]$$

가 $A$의 integral extension이고, $A[t]$는 UFD이므로 [\[가환대수학\] §정수적 확장, ⁋명제 9](/ko/math/commutative_algebra/integral_extension#prop9)에 의하여 integrally closed이므로 이것이 곧 normalization $\tilde{A}$이다. 

이제 기하적으로 이것이 무슨 의미인지 살펴보자. 우리는 우선 위의 integral extension $A\rightarrow A[t]$가 주는 공간들 사이의 map 

$$\Spec A[t]\rightarrow \Spec A$$

을 살펴보아야 한다. 우선 곡선 $\Spec A$의 singular point인 원점 $\mathfrak{m}=(t^2,t^3)\in\Spec A$을 보면, 이 점에서의 위의 map의 fiber는 다음의 pullback diagram

{% diagram Math/Scheme_Theory/Dimension_Schemes-2.svg width="17.35em" alt="cusp-fiber" %}

즉 다음의 scheme

$$\Spec(A[t]\otimes_A A/\mathfrak{m})=\Spec(A[t]/(t^2,t^3))=\Spec(A[t]/(t^2))$$

로 주어진다. 즉, fiber 자체는 한 점이 되지만 그 위에 주어진 scheme 구조는 non-reduced이며, 반면 $\Spec A$의 원점 $\Spec A/\mathfrak{m}$은 field의 spectrum으로서 reduced인 한 점이므로 위의 fiber는 이 점과 같아질 수 없다. 반면 원점을 뺀 열린집합 $D(\x)$에서는 $\x=t^2$가 invertible해지므로, $t=t^3\cdot(t^2)^{-1}$가 들어와

$$A[\x^{-1}]=\tilde{A}[\x^{-1}]$$

이 되어 두 scheme은 원점을 뺀 부분에서 완전히 같다. 

원점에서 일어나는 일을 조금 더 대수적으로 살펴보기 위해 local ring을 보자. 우선 $\Spec A$의 원점 $\mathfrak{m}$의 preimage는 그 정의에 의해 $\mathfrak{m}$을 포함하는 $A[t]$의 prime ideal이며, $\mathfrak{m}A[t]=(t^2)$을 포함하는 prime ideal은 이 ideal의 radical $(t)$이다. 그럼 $A[t]$의 원점 $(t)$에서의 local ring은

$$A[t]_{(t)}=\mathbb{K}[t]_{(t)}$$

인 반면, 원래의 curve $\Spec A$의 원점에서의 local ring은

$$A_{\mathfrak{m}}=\mathbb{K}[t^2,t^3]_{(t^2, t^3)}$$

임을 확인할 수 있다. 이들을 비교하면 normalization이 원점에서 무엇을 하는지가 대수적으로 드러난다. $A_{\mathfrak{m}}$은 $1$차원 local ring임에도 maximal ideal을 하나의 원소로 생성할 수 없고 $t^2$과 $t^3$ 두 원소를 필요로 하므로 regular local ring이 아니다. ([\[가환대수학\] §차원, ⁋정의 12](/ko/math/commutative_algebra/Krull_dimension#def12)) 실제로 $\mathfrak{m}/\mathfrak{m}^2$은 $t^2$과 $t^3$의 image로 생성되는 $2$차원 벡터공간이며, 이는 [\[대수다양체\] §접공간과 매끄러움, ⁋예시 7](/ko/math/algebraic_varieties/tangent_spaces_and_smoothness#ex7)에서 cusp의 원점에서의 tangent space가 curve의 차원보다 큰 $2$차원으로 계산되었던 것과 같은 현상이다. 반면 normalization의 local ring $A[t]_{(t)}=\mathbb{K}[t]_{(t)}$는 maximal ideal이 단 하나의 원소 $t$로 생성되는 regular local ring이다. 즉 normalization은 singular한 local ring $A_{\mathfrak{m}}$을 regular local ring $A[t]_{(t)}$로 바꾸어 cusp를 펴는 것이다.
:::

임의의 integral scheme $X$에 대해서도 normalization을 같은 방식으로 정의할 수 있다. $X$를 affine open $\Spec A_i$들로 덮자. $X$가 integral이므로 유일한 generic point $\xi$를 가지며, 이 점은 각 $\Spec A_i$에서 domain $A_i$의 minimal prime $(0)$에 대응하여 그 stalk이 $\Frac(A_i)$가 된다. Stalk $\mathcal{O}_{X,\xi}$는 어느 affine open에서 계산하든 같으므로 모든 $\Frac(A_i)$가 하나의 공통 function field $K(X)$로 일치하며 ([§스킴 사상의 성질들, §§유리사상](/ko/math/scheme_theory/properties_of_scheme_morphisms#유리사상)), 우리는 각 조각에서 $A_i$의 $K(X)$ 안에서의 normalization $\tilde{A}_i$를 취할 수 있다. 이 때 normalization은 localization과 commute하므로 ([\[가환대수학\] §정수적 확장, ⁋명제 12](/ko/math/commutative_algebra/integral_extension#prop12)) 각 $\Spec\tilde{A}_i$의 겹침 $\Spec A_i\cap\Spec A_j$로의 restriction들이 서로 일치하고, 따라서 이들은 하나의 scheme $\tilde{X}$로 붙어 normalization morphism $\tilde{X}\rightarrow X$를 정의한다. 이 morphism은 affine-locally $A_i\hookrightarrow\tilde{A}_i$가 integral extension이므로 integral morphism이며, [명제 5](#prop5)에 의하여 각 조각에서 $\dim\Spec\tilde{A}_i=\dim\Spec A_i$이므로 [명제 2](#prop2)의 증명으로부터 $\dim\tilde{X}=\dim X$를 얻는다. 

이제 우리는 codimension을 정의한다. 

::: 정의 7
위상공간 $X$의 irreducible subset $Y$에 대하여, $Y$의 $X$에서의 *codimension<sub>여차원</sub>* $\codim_XY$를 $X$의 irreducible closed subset들의 strictly descending chain 

$$Z_n\supsetneq Z_{n-1}\supsetneq\cdots\supsetneq Z_0=\cl_X(Y)$$

의 length의 supremum으로 정의한다. 
:::

그럼 ring $A$의 prime ideal $\mathfrak{p}$의 codimension은 $\Spec A$에서 점 $\mathfrak{p}$의 codimension과 같은 것을 확인할 수 있다. ([\[가환대수학\] §차원, ⁋정의 2](/ko/math/commutative_algebra/Krull_dimension#def2))

::: 명제 8
$X$의 irreducible closed subset $Y$와 $Y$의 generic point $\eta$에 대하여, $\codim_X Y=\dim \mathcal{O}_{X,\eta}$이 성립한다.
:::
::: 증명
$Y$가 generic point $\eta$를 가지므로, 정의에 의해 $\codim_XY$와 $\codim_X\{\eta\}$가 같다. 이제 $\eta$를 포함하는 임의의 affine open subset $U\cong\Spec A$를 택하고, 이 isomorphism에 의해 $\eta\in U$가 $\mathfrak{p}_\eta\in \Spec A$에 대응된다 하자. 그럼 [\[위상수학\] §차원, ⁋명제 15](/ko/math/topology/dimension#prop15)로부터 우리는 $U$와 만나는 $X$의 irreducible closed subset들과 $U$의 irreducible closed subset들 사이의 일대일 대응이 존재한다는 것을 안다. 즉, $\codim_X\{\eta\}=\codim_U \mathfrak{p}_\eta$이다. 이제 [§스펙트럼, ⁋명제 16](/ko/math/scheme_theory/spectrums#prop16)으로부터 원하는 결과를 얻는다. 
:::

더 일반적으로 우리는 [\[가환대수학\] §차원, ⁋정의 2](/ko/math/commutative_algebra/Krull_dimension#def2)에서 codimension을 정의한 후 다음의 부등식

$$\dim \mathfrak{a}+\codim \mathfrak{a}\leq \dim A$$

를 증명하였는데, 여기에서 사용한 [\[가환대수학\] §국소화, ⁋명제 8](/ko/math/commutative_algebra/localization#prop8) 대신 [\[위상수학\] §차원, ⁋명제 15](/ko/math/topology/dimension#prop15)를 사용하면 scheme $X$와 $X$의 irreducible closed subset $Y$에 대하여 다음의 부등식

$$\dim Y+\codim_XY\leq \dim X$$

이 성립하는 것을 확인할 수 있다. 그러나 마찬가지로 일반적인 경우에는 등호가 성립하지 않는다. 

## 뇌터 정규화

이제 우리는 중요한 다음 결과를 보인다.

::: 정리 9 (Noether normalization lemma)
임의의 field $\mathbb{K}$와, finitely generated $\mathbb{K}$-algebra $A$가 주어졌다 하자. 만일 $A$가 integral domain이고 

$$\trdeg_\mathbb{K}\Frac(A)=n$$

이라면 $A$의 적당한 원소들 $x_1,\ldots, x_n$이 존재하여 이들이 algebraically independent이고 $A$가 finite $\mathbb{K}[x_1,\ldots, x_n]$-module이도록 할 수 있다. 
:::
::: 증명
$A$가 finitely generated $\mathbb{K}$-algebra라는 가정으로부터

$$A=\mathbb{K}[y_1,\ldots, y_m]/\mathfrak{p}$$

로 적을 수 있다. 그럼 이들 $y_1,\ldots, y_m$의 $\Frac(A)$에서의 image가 $\mathbb{K}$의 field extension으로서 $\Frac(A)$를 생성하므로 반드시 $m\geq n$이어야 한다. 

이제 만일 $m=n$이라면, $y_i$들의 image가 $\Frac(A)$의 transcendence basis를 이루므로 특히 algebraically independent이고, 따라서 $\mathfrak{p}=0$, 곧 $A=\mathbb{K}[y_1,\ldots, y_n]$이다. 실제로 $\mathfrak{p}$의 nonzero element는 $y_i$들 사이의 nontrivial algebraic relation을 주므로 transcendence degree가 $n$보다 작아지게 된다. 즉 이 경우 $y_i$들이 정확히 원하는 원소가 되므로 더 이상 증명할 것이 없다. 이제 주어진 주장을 보이기 위해 $m>n$이라 하고, $n\leq k< m$을 만족하는 임의의 $k$에 대하여 정리가 성립한다 하자. 그럼 $m>n$이라는 가정으로부터 $y_1,\ldots, y_m$들은 algebraically dependent이다. 즉, 다음의 식

$$f(y_1,\ldots, y_m)=0$$

을 만족하는 $\mathbb{K}$-계수 $m$변수 다항식 

$$f(\x_1,\ldots, \x_m)=\sum \alpha_{d_1d_2\cdots d_m}\x_1^{d_1}\cdots\x_m^{d_m}\in \mathbb{K}[\x_1,\ldots, \x_m]\tag{$\ast$}$$

이 존재한다. 이제 정수 $r_1,\ldots, r_{m-1}$에 대하여 다음의 식

$$z_1=y_1-y_m^{r_1},\quad z_2=y_2-y_m^{r_2},\quad\ldots\quad,\quad z_{m-1}=y_{m-1}-y_m^{r_{m-1}}$$

으로 원소들 $z_1,\ldots, z_{m-1}$을 정의하자. 그럼 정의에 의해 

$$f(z_1+y_m^{r_1},\ldots, z_{m-1}+y_m^{r_{m-1}}, y_m)=0\tag{$\ast\ast$}$$

이 성립한다. 이제 식 ($\ast$)에서 $f$를 이루는 각각의 monomial $\alpha_{d_1d_2\cdots d_m}\x_1^{d_1}\cdots\x_m^{d_m}$에 

$$\x_1=z_1+y_m^{r_1},\quad \ldots\quad,\quad \x_{m-1}=z_{m-1}+y_m^{r_{m-1}},\quad \x_m=y_m$$

을 대입하여 전개하면, 그 결과는 계수가 상수항인 $y_m$의 거듭제곱

$$\alpha_{d_1d_2\cdots d_m}y_m^{r_1d_1+\cdots+r_{m-1}d_{m-1}+d_m}$$

과 $z_k$를 포함하는 그 외의 항들이 될 것이다. 이제 $f$에 실제로 나타나는 지수 $d_j$들의 최댓값보다 큰 정수 $r$을 택하여 $r_i=r^i$로 두면, $f$의 서로 다른 monomial마다 지수

$$r_1d_1+\cdots+r_{m-1}d_{m-1}+d_m=d_m+d_1r+\cdots+d_{m-1}r^{m-1}$$

이 $r$진법 전개의 유일성에 의해 서로 다른 값을 가지므로, 이러한 형태의 항 가운데 정확히 하나가 최고차항으로 남는다. 그 계수는 $\mathbb{K}$의 $0$이 아닌 원소이므로 양변을 그것으로 나눌 수 있고, 따라서 위의 등식 ($\ast\ast$)은 $y_m$이 $z_1,\ldots, z_{m-1}$에 대해 integrally dependent임을 보여준다.

한편 $z_1,\ldots, z_{m-1}$로 생성되는 $A$의 $\mathbb{K}$-subalgebra $A'$, 즉 ($\ast\ast$)를 $y_m$의 일변수 다항식으로 보았을 때 그 계수들이 존재하는 $A$의 $\mathbb{K}$-subalgebra $A'$를 생각하자. 위의 논증에 의해 $A$는 finite $A'$-module이고, 따라서 $\Frac(A)$는 $\Frac(A')$의 algebraic extension이므로 $\trdeg_\mathbb{K}\Frac(A')=n$이다. 그럼 $A'$는 $m-1$개의 원소로 생성되는 integral domain이므로 귀납적 가정에 의해 원하는 조건을 만족하는 $x_1,\ldots, x_n\in A'$들이 존재하며, $A'$가 finite $\mathbb{K}[x_1,\ldots, x_n]$-module이므로 $A$ 또한 finite $\mathbb{K}[x_1,\ldots, x_n]$-module이다.
:::

기하적으로 $A=\mathbb{K}[y_1,\ldots, y_m]/\mathfrak{p}$라 두는 것은 $\Spec A$가 affine space $\mathbb{A}^m_\mathbb{K}$의 integral closed subscheme이라는 것과 같으므로, 위의 정리의 결과로 얻어지는 finite ring homomorphism $\mathbb{K}[x_1,\ldots, x_n] \rightarrow \mathbb{K}[y_1,\ldots, y_m]/\mathfrak{p}$는 기하적으로는 finite scheme morphism $\Spec A \rightarrow \Spec \mathbb{K}[x_1,\ldots, x_n]$을 찾는 것과 같다. 이제 finite extension $\mathbb{K}[x_1,\ldots, x_n] \rightarrow A$은 integral extension이므로 [명제 5](#prop5)에 의하여 $\dim A=\dim \mathbb{K}[x_1,\ldots, x_n]$이므로, [\[가환대수학\] §매개계, ⁋따름정리 11](/ko/math/commutative_algebra/system_of_parameters#cor11)에 의하여 다음 결과를 얻는다.

::: 명제 10
임의의 field $\mathbb{K}$와, finitely generated $\mathbb{K}$-algebra $A$가 주어졌다 하자. 만일 $A$가 integral domain이라면, $\dim\Spec A=\trdeg_\mathbb{K} \Frac(A)$이 성립한다. 
:::

[명제 10](#prop10)을 점의 언어로 옮기면 $\mathbb{K}$ 위에서 locally of finite type인 scheme의 closed point가 어떤 점인지, 그리고 그러한 점이 얼마나 많은지를 알 수 있다.

::: 명제 11
Field $\mathbb{K}$ 위에서 locally of finite type인 scheme $X$에 대하여 다음이 성립한다.

1. 점 $x\in X$가 closed point인 것과 $\kappa(x)$가 $\mathbb{K}$의 유한확대인 것은 동치이다.
2. $X$의 공집합이 아닌 임의의 locally closed subset은 $X$의 closed point를 포함하며, 따라서 closed point들은 그 안에서 조밀하다.
:::
::: 증명
우선 $X$의 임의의 affine open subset $\Spec S$에 대하여 $S$가 finitely generated $\mathbb{K}$-algebra라는 것을 관찰한다. ([§스킴 사상의 성질들, ⁋보조정리 13](/ko/math/scheme_theory/properties_of_scheme_morphisms#lem13))

첫째 주장의 한 방향을 위해 $\kappa(x)$가 $\mathbb{K}$의 유한확대라 하고, $x$를 담는 affine open subset $\Spec S$와 $x$에 대응하는 prime ideal $\mathfrak{q}$를 택하자. 그럼 $S/\mathfrak{q}$는 fraction field가 $\kappa(x)$인 finitely generated $\mathbb{K}$-algebra domain이므로 [명제 10](#prop10)에 의하여 $\dim S/\mathfrak{q}=\trdeg_\mathbb{K}\kappa(x)=0$이고, 차원이 $0$인 domain은 field이므로 $\mathfrak{q}$는 maximal ideal, 곧 $x$는 $\Spec S$의 closed point이다. 이제 $y\in\cl(\{x\})$를 택하면 $y$를 담는 affine open subset은 모두 $x$ 또한 담으므로 그러한 subset 하나에 위의 논증을 적용하여 $y=x$를 얻고, 따라서 $x$는 $X$의 closed point이다. 거꾸로 $x$가 $X$의 closed point이면 $x$를 담는 affine open subset $\Spec S$ 안에서도 $\{x\}$가 닫힌집합이라 대응하는 prime ideal이 maximal ideal이고, field는 유일한 prime ideal $(0)$이 maximal ideal이라 Jacobson ring이므로 [\[가환대수학\] §영점정리, ⁋정리 4](/ko/math/commutative_algebra/nullstellensatz#thm4)에 의하여 $\kappa(x)$는 $\mathbb{K}$의 유한확대이다.

둘째 주장을 위해 공집합이 아닌 locally closed subset을 $U\cap C$로 쓰자. 이 집합의 한 점을 담으면서 $U$에 포함되는 affine open subset $\Spec S$를 택하면 $C$는 그 안에서 여전히 닫힌집합이므로 $(U\cap C)\cap \Spec S$는 어떤 ideal $I$에 대한 $V(I)$이고, 이것이 공집합이 아니므로 $I$를 포함하는 maximal ideal $\mathfrak{m}$이 존재한다. 그럼 $\mathfrak{m}$이 주는 점은 $U\cap C$에 속하며 그 residue field가 $\mathbb{K}$의 유한확대이므로 ([\[가환대수학\] §영점정리, ⁋정리 4](/ko/math/commutative_algebra/nullstellensatz#thm4)) 첫째 주장에 의하여 $X$의 closed point이다. 마지막으로 $U\cap C$의 공집합이 아닌 상대열린 부분집합은 다시 $X$의 locally closed subset이므로 같은 논증이 그 안의 closed point를 주고, 따라서 closed point들은 $U\cap C$에서 조밀하다.
:::

위의 주장들에서 가장 중요하게 쓰인 결과는 당연히 [\[가환대수학\] §정수적 확장과 아이디얼](/ko/math/commutative_algebra/lying_over_and_going_up)의 결과들이다. 한편 차원 공식 [\[가환대수학\] §뇌터 정규화, ⁋정리 4](/ko/math/commutative_algebra/noether_normalization#thm4)를 사용하면 다음을 얻는다.

::: 명제 12
임의의 field $\mathbb{K}$와, finitely generated $\mathbb{K}$-algebra $A$가 주어졌다 하자. 만일 $A$가 integral domain이고, $f\in A$가 nonzero non-unit이라면 $\dim A/(f)=\dim A-1$이 성립한다.
:::
::: 증명
$(f)$를 포함하는 $A$의 minimal prime $\mathfrak{p}$를 택하자. [\[가환대수학\] §차원, ⁋정리 6](/ko/math/commutative_algebra/Krull_dimension#thm6)에 의하여 $\operatorname{ht}\mathfrak{p}\leq 1$이고, $A$가 domain이고 $f\neq 0$이므로 $(0)\subsetneq\mathfrak{p}$에서 $\operatorname{ht}\mathfrak{p}\geq 1$이다. 따라서 $\operatorname{ht}\mathfrak{p}=1$이며, 차원 공식 [\[가환대수학\] §뇌터 정규화, ⁋정리 4](/ko/math/commutative_algebra/noether_normalization#thm4)에 의하여 $\dim A/\mathfrak{p}=\dim A-1$이다. 이제 $\dim A/(f)$는 $(f)$의 minimal prime $\mathfrak{p}$들에 대한 $\dim A/\mathfrak{p}$의 최댓값으로 주어지는데, 위에서 모든 minimal prime이 height $1$이므로 이 값들은 모두 $\dim A-1$이고, 따라서 $\dim A/(f)=\dim A-1$이다.
:::

## Principal ideal theorem

앞서 우리는 finite type인 affine integral $\mathbb{K}$-scheme $X=\Spec A$에 대하여, $A$의 nonzero non-unit $f$를 통해 정의된 closed subscheme $Z(f)$는 $X$보다 하나 적은 차원을 갖는다는 것을 살펴보았다. 이는 분명 유용한 결과이지만, 다음과 같이 더 일반적인 경우에도 그 결과를 살펴볼 수 있다.

::: 명제 13
Locally Noetherian scheme $X$와 $X$ 위의 함수 $f$에 대하여, $Z(f)$의 irreducible component는 codimension $0$이거나 codimension $1$이다.
:::
::: 증명
$W$를 $Z(f)$의 irreducible component라 하고 $w$를 $W$의 generic point라 하자. 이제 $w$를 포함하는 affine open subset $U\cong\Spec A$를 택하면, $X$가 locally Noetherian이므로 $A$를 Noetherian ring으로 잡을 수 있으며, 이 isomorphism에 의해 $w$가 $\mathfrak{p}\in\Spec A$에 대응된다 하자. [\[위상수학\] §차원, ⁋명제 15](/ko/math/topology/dimension#prop15)의 대응에 의하여 $W\cap U$는 $Z(f\vert_U)$의 irreducible component이므로, $\mathfrak{p}$는 $f\vert_U\in A$가 생성하는 principal ideal을 포함하는 minimal prime ideal이다. 따라서 [\[가환대수학\] §차원, ⁋정리 6](/ko/math/commutative_algebra/Krull_dimension#thm6)에 의하여 $\codim\mathfrak{p}\leq 1$이다.

한편 stalk은 $w$의 열린근방에만 의존하므로 $\mathcal{O}_{U,w}=\mathcal{O}_{X,w}$이고, $W$와 $W\cap U$는 각각 $X$와 $U$의 irreducible closed subset으로서 모두 $w$를 generic point로 가지므로 [명제 8](#prop8)을 두 번 적용하면

$$\codim_XW=\dim\mathcal{O}_{X,w}=\dim\mathcal{O}_{U,w}=\codim_U(W\cap U)$$

를 얻는다. 이제 $\Spec A$에서 점 $\mathfrak{p}$의 codimension이 ring $A$에서의 $\codim\mathfrak{p}$와 같으므로 ([\[가환대수학\] §차원, ⁋정의 2](/ko/math/commutative_algebra/Krull_dimension#def2)) 결국 $\codim_XW=\codim\mathfrak{p}\leq 1$이다.
:::

$\codim_XW=0$인 것은 $W$가 $X$ 자신의 irreducible component라는 것, 곧 $f$가 그 component 위에서 항등적으로 소멸한다는 것과 같다. 따라서 $f$가 $X$의 어떤 irreducible component 위에서도 항등적으로 소멸하지 않는다면 $Z(f)$의 모든 component는 codimension이 정확히 $1$이 되며, 이것이 [명제 12](#prop12)에서 $A$가 integral domain이고 $f$가 nonzero라는 가정이 하던 역할이다.

---

**참고문헌**

**[AM]** M. F. Atiyah and I. G. Macdonald, *Introduction to commutative algebra*, Addison-Wesley, 1969.  
**[Vak]** R. Vakil, *The rising sea: Foundation of algebraic geometry*. Available [online](https://math.stanford.edu/~vakil/216blog/).

