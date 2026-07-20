---
title: "차원"
description: "스킴의 차원을 크룰 차원으로 정의하고, 가환대수학적 차원과의 관계를 살펴봅니다. 유한 사상과 적분 사상의 성질을 함께 다룹니다."
excerpt: "Scheme의 dimension 정의와 local ring의 Krull dimension과의 관계"

categories: [Math / Scheme Theory]
permalink: /ko/math/scheme_theory/dimension
sidebar: 
    nav: "scheme_theory-ko"

date: 2025-03-14
weight: 12
published: false
drift_needed: true

---

## 스킴의 차원

이제 우리는 scheme의 차원을 정의한다.

::: 정의 1
Scheme $X$의 *dimension<sub>차원</sub>*은 위상공간 $X$의 Krull dimension으로 정의한다. ([\[위상수학\] §차원, ⁋정의 10](/ko/math/topology/dimension#def10))
:::

그럼 [§스펙트럼, ⁋명제 16](/ko/math/scheme_theory/spectrums#prop16)의 Galois correspondence로부터 우리는 $\Spec A$의 scheme으로서의 차원과 $A$의 ring으로서의 차원이 같다는 것을 안다. ([\[가환대수학\] §차원, ⁋정의 1](/ko/math/commutative_algebra/Krull_dimension#def1)) 뿐만 아니라, 정의에 의하여 $\Spec A$와 $\Spec A/\mathfrak{N}(A)$가 homeomorphic하다는 것을 보일 수 있으므로 $\dim A=\dim A/\mathfrak{N}(A)$가 성립한다. 즉 reducedness는 차원에 영향을 주지 않는다. 

한편 [\[위상수학\] §차원, ⁋명제 14](/ko/math/topology/dimension#prop14)와 마찬가지 이유로 다음이 성립한다. 

::: 명제 2
임의의 scheme $X$에 대하여, $\dim X=n$인 것은 $X$의 affine open covering $(U_i)$가 존재하여, 모든 $U_i$에 대하여 $\dim U_i\leq n$이고, 적어도 하나의 $i$에 대해서는 등호가 성립하는 것과 동치이다. 
:::
::: 증명
$X$의 임의의 irreducible closed subset들의 chain

$$Y_0\subsetneq Y_1\subsetneq\cdots\subsetneq Y_r$$

에서 가장 작은 항 $Y_0$의 generic point $\eta_0$는 $X$의 점이므로 covering $(U_i)$에 의해 어떤 $U_i$에 속한다. 그러면 chain의 모든 항이 $U_i$와 만나므로, [\[위상수학\] §차원, ⁋명제 14](/ko/math/topology/dimension#prop14)의 inclusion-preserving bijection을 생각하면 $U_i$ 안의 같은 길이의 chain으로 대응된다. 거꾸로 $U_i$의 임의의 chain은 $X$ 안에서 closure를 취해 올려지므로 $\dim X\geq\dim U_i$이고, 따라서 $\dim X=\sup_i\dim U_i$이며 이는 명제의 조건과 동치이다.
:::

한편 우리는 [§스킴 사상의 성질들, ⁋명제 14](/ko/math/scheme_theory/properties_of_scheme_morphisms#prop14)에서 finite morphism은 integral morphism of finite type인 것을 살펴보았으며, [§올곱, ⁋명제 14](/ko/math/scheme_theory/fiber_products#prop14)에서 임의의 finite morphism은 quasi-finite인 것을 살펴보았다. 일반적으로 integral morphism이지만 finite type은 아닌 morphism이 존재하며, 따라서 아직까지는 integral morphism의 fiber에 대한 이야기를 할 수가 없다.

::: 예시 3
예를 들어 $\mathbb{Q}$의 algebraic closure $\overline{\mathbb{Q}}$를 생각하자. $\overline{\mathbb{Q}}$의 임의의 원소는 $\mathbb{Q}$ 위에서 algebraic하므로 integral이고, 따라서 $\mathbb{Q} \rightarrow \overline{\mathbb{Q}}$는 integral extension이며 이로부터 scheme morphism $\varphi:\Spec \overline{\mathbb{Q}} \rightarrow \Spec \mathbb{Q}$도 integral morphism이다.

이제 $\varphi$를 $\Spec\overline{\mathbb{Q}}\rightarrow\Spec\mathbb{Q}$로 base change하면, 다음의 pullback diagram

![pullback](/assets/images/Math/Scheme_Theory/Dimension_Schemes-1.svg){:style="width:13.60em" class="invert" .align-center}

을 얻으며, 이 때 좌측 수직방향의 map

$$\Spec(\overline{\mathbb{Q}}\otimes_\mathbb{Q}\overline{\mathbb{Q}})\rightarrow \Spec \overline{\mathbb{Q}}$$

또한 [§올곱, ⁋명제 15](/ko/math/scheme_theory/fiber_products#prop15)에 의하여 integral이다. 

이 map을 살펴보기 위해, 구체적으로 ring homomorphism $\overline{\mathbb{Q}}\rightarrow \overline{\mathbb{Q}}\otimes_\mathbb{Q}\overline{\mathbb{Q}}$를 살펴보자. 위의 scheme 사이의 map의 section을 보는 것은 이 함수의 retraction을 보는 것과 같으며 이는 다음의 surjective ring homomorphism

$$\overline{\mathbb{Q}}\otimes_\mathbb{Q}\overline{\mathbb{Q}}\rightarrow\overline{\mathbb{Q}},\qquad a\otimes b\mapsto a\sigma(b)$$

으로부터 온다. 구체적으로, 이 ring homomorphism의 kernel $\mathfrak{p}_\sigma$는 maximal ideal이므로 $\Spec(\overline{\mathbb{Q}}\otimes_\mathbb{Q}\overline{\mathbb{Q}})$의 한 점을 정의하며, $\sigma\neq\tau$이면 $\sigma(b)\neq\tau(b)$인 $b\in\overline{\mathbb{Q}}$를 택할 때 $1\otimes b-\sigma(b)\otimes 1\in\mathfrak{p}_\sigma$이지만 $\mathfrak{p}_\tau$에는 속하지 않으므로 $\mathfrak{p}_\sigma\neq\mathfrak{p}_\tau$이다. 따라서 $\Spec(\overline{\mathbb{Q}}\otimes_\mathbb{Q}\overline{\mathbb{Q}})$은 적어도 $\Gal(\overline{\mathbb{Q}}/\mathbb{Q})$만큼의, 곧 무한히 많은 점을 가지며, $\Spec(\overline{\mathbb{Q}}\otimes_\mathbb{Q}\overline{\mathbb{Q}})\rightarrow\Spec\overline{\mathbb{Q}}$는 quasi-finite morphism이 아니므로 finite morphism도 아니다.
:::

혹은 더 간단한 예로 $\Spec \mathbb{C}\rightarrow \Spec \mathbb{R}$을 보자. 여기서 $\mathbb{R}$와 $\mathbb{C}$가 모두 field이므로 $\Spec\mathbb{C}$와 $\Spec\mathbb{R}$는 각각 한 점이며, 따라서 이 map 자체는 한 점에서 한 점으로 가는 trivial한 map이다. 그러나 이를 $\Spec \mathbb{C}\rightarrow \Spec \mathbb{R}$로 pullback하여 위의 예시와 비슷한 함수

$$\Spec(\mathbb{C}\otimes_\mathbb{R} \mathbb{C}) \rightarrow \Spec \mathbb{C}$$

를 만들면 $\mathbb{C}\otimes_\mathbb{R}\mathbb{C}$는 더 이상 field가 아니다. 실제로 $\Spec\mathbb{C}=\Spec\mathbb{R}[\x]/(\x^2+1)$이므로, 

$$\mathbb{C}\otimes_\mathbb{R} \mathbb{C}\cong \mathbb{C}\otimes_\mathbb{R} \frac{\mathbb{R}[\x]}{(\x^2+1)}\cong \frac{\mathbb{C}[\x]}{(\x^2+1)}$$

이며, $\x^2+1$은 $\mathbb{C}$에서는 두 일차식의 곱 $\x^2+1=(\x-i)(\x+i)$로 인수분해되며, $(\x-i)$와 $(\x+i)$는 comaximal이므로 [\[환론\] §중국인의 나머지정리, ⁋명제 6](/ko/math/ring_theory/chinese_remainder_theorem#prop6)에 의하여 

$$\frac{\mathbb{C}[\x]}{((\x-i)(\x+i)}\cong\frac{\mathbb{C}[\x]}{(\x-i)}\times\frac{\mathbb{C}[\x]}{(\x+i)}\cong\mathbb{C}\times\mathbb{C}$$

가 된다. 위의 예시에서 살펴본 Galois group의 언어로 생각하면 이는 위 분해의 두 factor $\mathbb{C}[\x]/(\x-i)$와 $\mathbb{C}[\x]/(\x+i)$가 곧 $\mathbb{R}$을 고정하는 $\mathbb{C}\rightarrow \mathbb{C}$의 automorphism, 즉 $\Gal(\mathbb{C}/\mathbb{R})$의 두 원소에 해당하기 때문에 나타나는 것이며 같은 일이 [예시 3](#ex3)의 $\mathbb{Q}\rightarrow \overline{\mathbb{Q}}$에서도 나타난다. 유일한 차이는 $\Gal(\overline{\mathbb{Q}}/\mathbb{Q})$는 무한하므로 fiber가 두 개가 아닌 무한개가 된다는 것이다. 

그럼에도 이 예시는 integral morphism의 fiber에 대한 어떠한 종류의 finiteness를 암시하는데, 가령 $\Gal(\overline{\mathbb{Q}}/\mathbb{Q})$는 profinite group이므로 ([\[체론\] §갈루아 군의 성질들, ⁋명제 5](/ko/math/field_theory/properties_of_galois_extensions#prop5)) $0$차원이 된다. 이는 임의의 integral morphism에 대해서도 성립하는 사실이다. 

::: 명제 4
Integral morphism $\varphi: X \rightarrow Y$의 임의의 fiber는 항상 $0$차원이다. 
:::
::: 증명
정의에 의해 $Y$의 한 점 $y$에서의 fiber는 [§스킴, ⁋정의 5](/ko/math/scheme_theory/schemes#def5)의 residue field $\kappa(y)$에 대한 inclusion map $\Spec \kappa(y) \rightarrow Y$에 의한 $\varphi$의 base change

$$\varphi^{-1}(y)=X\times_Y\Spec \kappa(y)$$

으로 주어지며, integral morphism은 base change에 의해 보존되므로 ([§올곱, ⁋명제 15](/ko/math/scheme_theory/fiber_products#prop15))

$$\varphi^{-1}(y)=X\times_Y\Spec \kappa(y) \rightarrow \Spec \kappa(y)$$

는 integral morphism이며, integral morphism은 그 정의에 의해 affine morphism이므로 임의의 integral morphism $\Spec B \rightarrow \Spec \mathbb{K}$에 대하여 $\dim \Spec B=\dim B=0$임을 보이면 충분하다. 즉, 임의의 integral extension $\mathbb{K} \rightarrow B$에 대하여, $B$의 prime ideal들의 chain

$$\mathfrak{q}_1\subsetneq \mathfrak{q}_2$$

이 존재할 수 없음을 보여야 한다. 이는 [\[가환대수학\] §정수적 확장과 아이디얼, ⁋따름정리 4](/ko/math/commutative_algebra/lying_over_and_going_up#cor4)의 결과이다. 
:::

기하적으로, 이 명제는 integral morphism의 각 fiber가 양의 차원을 갖지 않는다는 것을 보여준다. 

위의 명제의 증명에서 사용한 [\[가환대수학\] §정수적 확장과 아이디얼, ⁋따름정리 4](/ko/math/commutative_algebra/lying_over_and_going_up#cor4)는 임의의 integral extension $A\hookrightarrow B$에 대해서도 성립한다. 이에 의해 $B$의 prime ideal chain을 $A$로 contraction하면 여전히 strict하므로 $\dim B\leq\dim A$이고, 거꾸로 [\[가환대수학\] §정수적 확장과 아이디얼, ⁋명제 1](/ko/math/commutative_algebra/lying_over_and_going_up#prop1)의 lying over와 going up에 의해 $A$의 prime ideal chain은 $B$로 올려지므로 $\dim A\leq\dim B$이다. 따라서 더 일반적으로 다음이 성립한다.

::: 명제 5
임의의 integral extension $\phi:A \rightarrow B$에 대하여 

$$\dim\Spec A=\dim\Spec B$$

가 항상 성립한다. 
:::

특히 임의의 integral domain $A$와 그 normalization $\tilde{A}$에 대하여, extension $A\hookrightarrow\tilde{A}$가 integral이므로 [명제 5](#prop5)에 의하여 $\dim\Spec\tilde{A}=\dim\Spec A$이다. 여기서 normalization $\tilde{A}$는 $A$를 그 field of fractions $\Frac(A)$ 안에서 integrally closed가 되도록 확장한 것, 곧 $\Frac(A)$의 원소 가운데 $A$ 위에서 integral인 것들을 모두 $A$에 붙여 얻는 확장이다. ([\[가환대수학\] §정수적 확장, ⁋정의 3](/ko/math/commutative_algebra/integral_extension#def3)) 정의에 의해 $A\subseteq\tilde{A}\subseteq\Frac(A)$이므로 $\Frac(\tilde{A})=\Frac(A)$, 즉 normalization은 $A$의 function field를 보존한다.

::: 예시 6
위의 논의에서 우리는 normalization이 function field를 보존한다는 것을 살펴보았다. 기하적으로 이는 normalization으로 얻어지는 두 공간이 birational하다는 것이다. ([\[대수다양체\] §유리사상, ⁋명제 10](/ko/math/algebraic_varieties/rational_maps#prop10)) 즉, normalization은 무시할만큼 작은 특정한 loci 바깥에서는 원래의 공간과 같다. 

Normalization은 여기에 더해 이 특정한 locus가 정확히 singular point들이 되도록 한다. 대표적인 예로 [\[대수다양체\] §접공간과 매끄러움, ⁋예시 7](/ko/math/algebraic_varieties/tangent_spaces_and_smoothness#ex7)의 cusp

$$A=\mathbb{K}[\x,\y]/(\y^2-\x^3)\cong\mathbb{K}[t^2,t^3]$$

를 보자. $A$의 field of fraction을 보기 위해 $t=\y/\x$임을 사용하면 $\Frac(A)=\mathbb{K}(t)$임을 확인할 수 있고, 이 때 원소 $t\in\Frac(A)$는 $t^2=\x\in A$를 만족하므로 $A$ 위에서 integral이다. 따라서 $t$를 붙여 얻은 extension 

$$A[t]=\mathbb{K}[t^2,t^3,t]=\mathbb{K}[t]$$

가 $A$의 integral extension이고, $\mathbb{K}[t]$는 UFD이므로 [\[가환대수학\] §정수적 확장, ⁋명제 9](/ko/math/commutative_algebra/integral_extension#prop9)에 의하여 integrally closed이므로 이것이 곧 normalization $\tilde{A}$이다. 

이제 기하적으로 이것이 무슨 의미인지 살펴보자. 우리는 우선 위의 integral extension $A\rightarrow A[t]$가 주는 공간들 사이의 map 

$$\Spec A[t]\rightarrow \Spec A$$

을 살펴보아야 한다. 우선 곡선 $\Spec A$의 singular point, 즉 원점 $\mathfrak m=(t^2,t^3)\in\Spec A$을 보면 이 점에서의 위의 map의 fiber는

$$\Spec(\mathbb{K}[t]\otimes_A A/\mathfrak m)=\Spec(\mathbb{K}[t]/(t^2,t^3))=\Spec(\mathbb{K}[t]/(t^2))$$

로 주어진다. 즉, fiber 자체는 한 점이 되지만 그 위에 주어진 scheme 구조는 non-reduced이다. 

원점에서 cusp의 local ring $A_{\mathfrak m}=\mathbb{K}[t^2,t^3]_{(t^2,t^3)}$는 maximal ideal $(t^2,t^3)$이 두 원소로 생성되어야 하여 singular한데, 이는 [\[대수다양체\] §접공간과 매끄러움, ⁋예시 7](/ko/math/algebraic_varieties/tangent_spaces_and_smoothness#ex7)에서 본 것처럼 tangent space $T_0=\mathbb{K}^2$가 너무 크기 때문이다. 반면 normalization의 원점에서 local ring $\mathbb{K}[t]_{(t)}$는 maximal ideal이 단일 원소 $t$로 생성되어 tangent space가 1차원, 곧 매끈하다. 즉 normalization이 singular한 국소 구조를 매끈한 것으로 바꾸어 주는 것이 cusp를 펴주는 일이다.

반면 원점을 뺀 열린집합 $D(\x)$에서는 $\x=t^2$를 가역시키면 $t=t^3\cdot(t^2)^{-1}$가 들어와

$$A[\x^{-1}]=\mathbb{K}[t,t^{-1}]=\tilde{A}[\x^{-1}]$$

이 되어 두 scheme은 원점을 뺀 매끈한 부분에서 완전히 같다. 즉 기하 사상 $\Spec\mathbb{K}[t]\to\Spec A$, $t\mapsto(t^2,t^3)$은 affine line $\mathbb{A}^1$을 cusp 위로 감싸 정확히 원점의 singular point만 펴주며, 두 scheme 모두 1차원 곡선이라 차원이 보존되는 것은 normalization이 integral 확장이라는 사실 그 자체이다.
:::

임의의 scheme에 대해서도 normalization을 같은 방식으로 정의할 수 있지만, 이는 이후 별도의 글에서 다룬다.

::: 정의 7
위상공간 $X$의 irreducible subset $Y$에 대하여, $Y$의 $X$에서의 *codimension<sub>여차원</sub>* $\codim_XY$를 $X$의 irreducible closed subset들의 strictly descending chain 

$$A_n\supsetneq A_{n-1}\supsetneq\cdots\supsetneq A_0=\cl_X(Y)$$

의 length의 supremum으로 정의한다. 
:::

그럼 ring $A$의 prime ideal $\mathfrak{p}$의 codimension은 ([\[가환대수학\] §차원, ⁋정의 2](/ko/math/commutative_algebra/Krull_dimension#def2)) $\Spec A$에서 점 $\mathfrak{p}$의 codimension과 같은 것을 확인할 수 있다. 

::: 명제 8
$X$의 irreducible closed subset $Y$와 $Y$의 generic point $y$에 대하여, $\codim_X Y=\dim \mathcal{O}_{X,y}$이 성립한다.
:::
::: 증명
$Y$가 generic point $y$를 가지므로, 정의에 의해 $\codim_XY$와 $\codim_X\{y\}$가 같다. 이제 $y$를 포함하는 임의의 affine open subset $U\cong\Spec A$를 택하고, 이 isomorphism에 의해 $y\in U$가 $\mathfrak{p}_y\in \Spec A$에 대응된다 하자. 그럼  [\[위상수학\] §차원, ⁋명제 14](/ko/math/topology/dimension#prop14)로부터 우리는 $U$와 만나는 $X$의 irreducible closed subset들과 $U$의 irreducible closed subset들 사이의 일대일 대응이 존재한다는 것을 안다. 즉, $\codim_X\{y\}=\codim_U \mathfrak{p}_y$이다. 이제 [§스펙트럼, ⁋명제 16](/ko/math/scheme_theory/spectrums#prop16)으로부터 원하는 결과를 얻는다. 
:::

더 일반적으로 우리는 [\[가환대수학\] §차원, ⁋정의 2](/ko/math/commutative_algebra/Krull_dimension#def2)에서 codimension을 정의한 후 다음의 부등식

$$\dim \mathfrak{a}+\codim \mathfrak{a}\leq \dim A$$

를 증명하였는데, 여기에서 사용한 [\[가환대수학\] §국소화, ⁋명제 8](/ko/math/commutative_algebra/localization#prop8) 대신 [\[위상수학\] §차원, ⁋명제 14](/ko/math/topology/dimension#prop14)를 사용하면 scheme $X$와 $X$의 irreducible closed subset $Y$에 대하여 다음의 부등식

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

이제 만일 $m=n$이라면, $y_i$들이 정확히 원하는 원소가 되므로 더 이상 증명할 것이 없다. 이제 주어진 주장을 보이기 위해 $m>n$이라 하고, $n\leq k< m$을 만족하는 임의의 $k$에 대하여 정리가 성립한다 하자. 그럼 $m>n$이라는 가정으로부터 $y_1,\ldots, y_m$들은 algebraically dependent이다. 즉, 다음의 식

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

과 $z_k$를 포함하는 그 외의 항들이 될 것이다. 이제 $r_1,\ldots, r_{m-1}$을 충분히 크게 잡으면, 이러한 형태의 항이 최고차항이 되도록 할 수 있고, 따라서 위의 등식 ($\ast\ast$)은 $y_m$이 $z_1,\ldots, z_{m-1}$에 대해 integrally dependent임을 보여준다. 한편 $z_1,\ldots, z_{m-1}$로 생성되는 $A$의 $\mathbb{K}$-subalgebra $A'$, 즉 ($\ast\ast$)를 $y_m$의 일변수 다항식으로 보았을 때 그 계수들이 존재하는 $A$의 $\mathbb{K}$-subalgebra $A'$에 대해서는 귀납적 가정에 의해 원하는 조건을 만족하는 $x_1,\ldots, x_n\in A$들이 존재한다. 이제 $A$는 위의 논증에 의해 finite $A'$-module이고, $A'$는 귀납적 가정에 의해 finite $\mathbb{K}[x_1,\ldots, x_n]$-module이므로 원하는 결과를 얻는다.
:::

기하적으로 $A=\mathbb{K}[y_1,\ldots, y_m]/\mathfrak{p}$라 두는 것은 $\Spec A$가 affine space $\mathbb{A}^m_\mathbb{K}$의 integral closed subscheme이라는 것과 같으므로, 위의 정리의 결과로 얻어지는 finite ring homomorphism $\mathbb{K}[x_1,\ldots, x_n] \rightarrow \mathbb{K}[y_1,\ldots, y_m]/\mathfrak{p}$는 기하적으로는 finite scheme morphism $\Spec A \rightarrow \Spec \mathbb{K}[x_1,\ldots, x_n]$을 찾는 것과 같다. 이제 finite extension $\mathbb{K}[x_1,\ldots, x_n] \rightarrow A$은 integral extension이므로 [명제 5](#prop5)에 의하여 $\dim A=\dim \mathbb{K}[x_1,\ldots, x_n]$이므로, [\[가환대수학\] §매개계, ⁋따름정리 11](/ko/math/commutative_algebra/system_of_parameters#cor11)에 의하여 다음 결과를 얻는다.

::: 명제 10
임의의 field $\mathbb{K}$와, finitely generated $\mathbb{K}$-algebra $A$가 주어졌다 하자. 만일 $A$가 integral domain이라면, $\dim\Spec A=\trdeg_\mathbb{K} \Frac(A)$이 성립한다. 
:::

위의 주장들에서 가장 중요하게 쓰인 결과는 당연히 [\[가환대수학\] §정수적 확장과 아이디얼](/ko/math/commutative_algebra/lying_over_and_going_up)의 결과들이다. 한편 차원 공식 [\[가환대수학\] §뇌터 정규화, ⁋정리 4](/ko/math/commutative_algebra/noether_normalization#thm4)를 사용하면 다음을 얻는다.

::: 명제 11
임의의 field $\mathbb{K}$와, finitely generated $\mathbb{K}$-algebra $A$가 주어졌다 하자. 만일 $A$가 integral domain이고, $f\in A$가 nonzero non-unit이라면 $\dim A/(f)=\dim A-1$이 성립한다.
:::
::: 증명
$(f)$를 포함하는 $A$의 minimal prime $\mathfrak{p}$를 택하자. [\[가환대수학\] §차원, ⁋정리 6](/ko/math/commutative_algebra/Krull_dimension#thm6)에 의하여 $\operatorname{ht}\mathfrak{p}\leq 1$이고, $A$가 domain이고 $f\neq 0$이므로 $(0)\subsetneq\mathfrak{p}$에서 $\operatorname{ht}\mathfrak{p}\geq 1$이다. 따라서 $\operatorname{ht}\mathfrak{p}=1$이며, 차원 공식 [\[가환대수학\] §뇌터 정규화, ⁋정리 4](/ko/math/commutative_algebra/noether_normalization#thm4)에 의하여 $\dim A/\mathfrak{p}=\dim A-1$이다. 이제 $\dim A/(f)$는 $(f)$의 minimal prime $\mathfrak{p}$들에 대한 $\dim A/\mathfrak{p}$의 최댓값으로 주어지는데, 위에서 모든 minimal prime이 height $1$이므로 이 값들은 모두 $\dim A-1$이고, 따라서 $\dim A/(f)=\dim A-1$이다.
:::

## Principal ideal theorem

앞서 우리는 임의의 affine integral $\mathbb{K}$-scheme $X=\Spec A$에 대하여, $A$의 nonzero non-unit $f$를 통해 정의된 closed subscheme $Z(f)$는 $A$보다 하나 적은 차원을 갖는다는 것을 살펴보았다. 이는 분명 유용한 결과이지만, 다음과 같이 더 일반적인 경우에도 그 결과를 살펴볼 수 있다.

::: 명제 12
Locally noetherian scheme $X$와 $X$ 위의 함수 $f$에 대하여, $Z(f)$의 irreducible component는 codimension $0$이거나 codimension $1$이다.
:::
::: 증명
[\[가환대수학\] §차원, ⁋정리 6](/ko/math/commutative_algebra/Krull_dimension#thm6)
:::

---

**참고문헌**

**[AM]** M. F. Atiyah and I. G. Macdonald, *Introduction to commutative algebra*, Addison-Wesley, 1969.

