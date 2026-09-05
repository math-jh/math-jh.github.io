---
title: "매끄러운 사상과 에탈 사상"
description: "스킴 사상의 매끄러움을 flat이면서 모든 기하적 올이 정칙인 finitely presented 사상으로 정의하고, cotangent sheaf가 relative dimension만큼의 locally free sheaf임과 동치임을 본다. 이 동치의 어려운 방향은 매끄러운 사상이 국소적으로 Jacobian이 최대 rank인 방정식들로 잘린다는 국소 구조 정리를 거쳐 증명한다. Unramified 사상을 대각선이 open embedding인 경우로 특징짓고, étale morphism을 매끄럽고 unramified한 relative dimension 0의 사상으로 도입하며 standard étale 모형과 Jacobian 판정, square-zero 확대에 대한 무한소 lifting 판정을 다룬다."
excerpt: "Smooth, unramified, and étale morphisms; the Jacobian and infinitesimal lifting criteria"

categories: [Math / Scheme Theory]
permalink: /ko/math/scheme_theory/smooth_and_etale_morphisms
sidebar: 
    nav: "scheme_theory-ko"

date: 2026-08-11
weight: 21

---

우리는 본질적으로 cotangent sheaf가 주는 exact sequence들은 *right* exact이기만 하다는 것을 살펴보았다. ([§미분과 여접층, ⁋명제 6](/ko/math/scheme_theory/sheaf_of_differentials#prop6) 이후의 exact sequence들) 이러한 정보의 손실을 막기 위해서는 morphism에 특수한 조건을 부여해야 하는데, 그것이 smooth morphism의 동기이다. 반대쪽 극단은 $\Omega_{X/S}$가 통째로 소멸하는 경우로, 우리는 이를 *unramified* morphism이라 부른다. 마지막으로 우리는 smooth unramified morphism인 *étale* morphism을 정의한다.

우리는 이 글 전체에서 morphism이 *locally of finite presentation*임을 기본 가정으로 둔다. (대부분의 관심사인) locally Noetherian base 위에서는 이것이 locally of finite type과 일치하므로, 직관적으로는 이렇게 생각해도 무방하다.

## 매끄러운 사상

Smooth morphism은 fiber가 base 위에서 균일하게 regular family를 이루는 morphism이다. 이를 가장 간단하게 정의할 방법은 각 점 $s\in S$ 위의 fiber $X_s=X\times_S\Spec\kappa(s)$가 singular point를 가지지 않는다는 조건을 부여하는 것이다. 즉, 임의의 점에서 접방향이 fiber 차원을 넘어가서는 안되며, 이를 해당 점에서의 대수적인 언어로 풀어쓰면 Noetherian local ring $(A, \mathfrak{m})$에서의 부등식 $\dim A\leq \dim_{A/\mathfrak{m}}\mathfrak{m}/\mathfrak{m}^2$의 등호가 성립해야 한다는 조건, 즉  $A$가 regular local ring이라는 것으로 해석할 수 있다. ([\[가환대수학\] §차원, ⁋정의 12](/ko/math/commutative_algebra/Krull_dimension#def12)) 

문제는 이것이 family의 성질이 되기 위해서는 이것이 base change에 대해 잘 행동해야 하는데, 일반적으로 그렇지 않다는 것이다. 즉, 위와 같이 명시적으로 fiber $X_s$의 각 점에서의 regularity를 요구하는 것은 base change에 대해 취약하며, 이를 위해서는 field $\kappa(s)$의 algebraic closure $\overline{\kappa(s)}$로 계수를 올려준 *geometric fiber* $X\times_S\Spec\overline{\kappa(s)}$를 생각하면 된다는 사실이 알려져 있다. 그러나 이 사실에 대한 증명은 그렇게 가볍지는 않으므로, 우리는 이를 motivation으로만 활용하고 바로 다음의 정의를 도입하기로 한다. 

::: 정의 1
Locally of finite presentation인 scheme morphism $\varphi:X \rightarrow S$가 *smooth<sub>매끄러운</sub>*하다는 것은 다음 두 조건이 성립하는 것이다.

1. $\varphi$는 flat하다. ([§평탄사상, ⁋정의 1](/ko/math/scheme_theory/flat_morphisms#def1))
2. 임의의 $s\in S$에 대하여, residue field $\kappa(s)$의 algebraic closure $\overline{\kappa(s)}$와 그것이 주는 canonical morphism $\overline{s}:\Spec\overline{\kappa(s)} \rightarrow S$에 대한 geometric fiber

   $$X_{\overline{s}}=X\times_S\Spec\overline{\kappa(s)}$$

   는 *regular scheme<sub>정칙스킴</sub>*이다. 즉 그 모든 local ring이 regular local ring이다. ([\[가환대수학\] §차원, ⁋정의 12](/ko/math/commutative_algebra/Krull_dimension#def12))
:::

위의 정의에서 두 조건은 서로 다른 방향을 통제하는데, flatness는 fiber들이 base를 따라 차원 도약 없이 연속적으로 변함을 보장하고 ([§평탄사상, ⁋명제 17](/ko/math/scheme_theory/flat_morphisms#prop17)), geometric fiber의 regularity는 각 fiber 자체가 singular point를 가지지 않음을 보장한다.

정의의 canonical morphism은 다음의 합성

$$\Spec \overline{\kappa(s)}\rightarrow \Spec \kappa(s)\rightarrow S$$

로 주어지는 것으로, 위의 조건은 $X_s$ 자체에 대한 조건보다 강한 것이다. 구체적으로 $X_{\overline{s}} \rightarrow X_s$는 cartesian square

{% diagram Math/Scheme_Theory/Smooth_and_Etale_Morphisms-1.svg width="12.38em" alt="base change" %}

에서 $X_s$를 $\Spec\overline{\kappa(s)} \rightarrow \Spec\kappa(s)$를 따라 base change하여 얻어지는 projection으로, 이 morphism의 $x\in X_s$ 위의 fiber가

$$\Spec\kappa(x)\times_{\Spec \kappa(s)}\Spec \overline{\kappa(s)}=\Spec\bigl(\kappa(x)\otimes_{\kappa(s)}\overline{\kappa(s)}\bigr)$$

이고, $\kappa(x)$와 $\overline{\kappa(s)}$가 모두 $\kappa(s)$ 위의 nonzero vector space이므로 그 tensor product 또한 nonzero가 되어 이 fiber는 공집합이 아니다. 그럼 fiber가 집합으로서의 preimage와 일치하므로 ([§올곱, ⁋보조정리 13](/ko/math/scheme_theory/fiber_products#lem13)) $X_{\overline{s}}\rightarrow X_s$가 전사가 된다. 즉, geometric fiber는 $X_s$의 점을 하나도 잃지 않고 계수만 키운 것으로, 이 위에서 regularity를 요구하는 것이 $X_s$의 모든 점에 대한 요구를 포함한다. 

한편, smooth morphism은 cotangent sheaf의 local freeness로 적어줄 수도 있으며, 이것이 가장 중요한 smooth morphism의 characterization이다. 이를 위해 우선 scheme $Y$와 그 점 $y\in Y$에 대하여, $y$에서의 *local dimension<sub>국소차원</sub>* $\dim_yY$를 $y$를 포함하는 irreducible component들의 차원의 supremum으로 정의하자. 그럼 정의에 의해 $Y$의 전체 차원은 이들의 supremum이며, 만일 $Y$가 irreducible이면 모든 점이 유일한 irreducible component에 속하므로 $\dim_yY=\dim Y$가 성립한다. 더 일반적으로 모든 irreducible component의 차원이 같은 *equidimensional* scheme에서도 그러하다. 이 개념은 새로운 것이 아니라 평면과 직선의 합집합 $Y=V(\x\z,\y\z)\subseteq\mathbb{A}^3_\mathbb{K}$에서 서로 차원이 다른 두 성분을 다루기 위한 언어일 뿐이다. 만일 $Y$가 field 위에서 finite type이면 그 closed point $z$에서는 [\[가환대수학\] §뇌터 정규화, ⁋정리 4](/ko/math/commutative_algebra/noether_normalization#thm4)에 의하여 $\dim\mathcal{O}_{Y,z}=\dim_zY$가 성립한다.

Smooth 조건 가운데 flatness를 뺀 나머지는 geometric fiber 위에서 주어져 있으므로, 이를 $X$ 위의 조건으로 옮겨 적으려면 무엇을 옮길 수 있는지 먼저 확인하여야 한다. Local ring $(\mathcal{O}_{X_{\overline{s}}, \overline{x}}, \mathfrak{m}_{\overline{x}})$이 regular라는 것은 그 정의에 의해 다음의 등식

$$\dim_{\kappa(\overline{x})}\mathfrak{m}_{\overline{x}}/\mathfrak{m}_{\overline{x}}^2=\dim \mathcal{O}_{X_{\overline{s}},\overline{x}}\tag{$\ast$}$$

이 성립하는 것이다. ([\[가환대수학\] §차원, ⁋정의 12](/ko/math/commutative_algebra/Krull_dimension#def12)) 한편 [§미분과 여접층, ⁋정의 8](/ko/math/scheme_theory/sheaf_of_differentials#def8) 직후에 우리는 $\mathbb{K}$-point $\overline{x}$에 대해서는 좌변의 $\mathfrak{m}/\mathfrak{m}^2$이 $\Omega_{X_{\overline{s}}/\mathbb{K}}\otimes\kappa(\overline{x})$임을 살펴보았으며, 우리 상황에서는 $\mathbb{K}=\overline{\kappa(s)}$가 algebraically closed이므로 임의의 closed point가 $\mathbb{K}$-point가 되어 이 전제를 만족한다. 또, 위에서 우변은 $\dim_{\overline{x}} X_{\overline{s}}$과 같음을 이미 살펴보았으므로, 우리가 원하는 것은 다음과 같은 형태의 주장이다.

::: 보조정리 2
Locally of finite presentation인 morphism $\varphi:X \rightarrow S$와 점 $x\in X$, $s=\varphi(x)$에 대하여 $\mathbb{K}=\overline{\kappa(s)}$라 하고 geometric fiber $X_{\overline{s}}$를 생각하자. 그럼 $x$ 위의 임의의 점 $\overline{x}\in X_{\overline{s}}$에 대하여

$$\dim_{\kappa(\overline{x})}\bigl(\Omega_{X_{\overline{s}}/\mathbb{K}}\otimes \kappa(\overline{x})\bigr)=\dim_{\kappa(x)}\bigl(\Omega_{X/S}\otimes \kappa(x)\bigr),\qquad \dim_{\overline{x}}X_{\overline{s}}=\dim_xX_s$$

가 성립한다.
:::
::: 증명
Cotangent sheaf는 base change와 commute하므로 ([§미분과 여접층, ⁋명제 5](/ko/math/scheme_theory/sheaf_of_differentials#prop5)) geometric fiber가 주는 pullback diagram

{% diagram Math/Scheme_Theory/Smooth_and_Etale_Morphisms-2.svg width="8.18em" alt="pullback" %}

에서 $\Omega_{X_{\overline{s}}/\mathbb{K}}$는 $\pi$를 따라 끌어온 pullback $\pi^\ast\Omega_{X/S}$이다. 한 점에서 fiber를 취하는 것은 그 점이 정의하는 canonical morphism을 따른 pullback이고, $\overline{x}:\Spec\kappa(\overline{x}) \rightarrow X_{\overline{s}}$와 $\pi$의 합성은 $x$와 field extension $\kappa(x)\hookrightarrow \kappa(\overline{x})$가 정의하는 canonical morphism $\Spec\kappa(\overline{x}) \rightarrow \Spec\kappa(x) \rightarrow X$이므로, pullback의 functoriality에 의하여

$$\Omega_{X_{\overline{s}}/\mathbb{K}}\otimes \kappa(\overline{x})=\overline{x}^\ast\pi^\ast\Omega_{X/S}=\bigl(\Omega_{X/S}\otimes \kappa(x)\bigr)\otimes_{\kappa(x)}\kappa(\overline{x})$$

이다. 한편 우변은 $\kappa(x)$-vector space $\Omega_{X/S}\otimes \kappa(x)$을 $\kappa(\overline{x})$로 스칼라를 바꾼 것에 지나지 않으므로 차원 또한 같고, 이것이 첫 번째 등식이다.

두 번째 등식을 보인다. 우선 algebraic extension이 주는 $\Spec\mathbb{K} \rightarrow \Spec\kappa(s)$가 integral morphism이고 이는 base change에 대해 보존되는 성질이므로, $X_{\overline{s}} \rightarrow X_s$는 integral, surjective morphism이다. 그럼 $\overline{x}$를 포함하는 $X_{\overline{s}}$의 component는 그 image의 closure 위로 가는 dominant integral morphism을 주므로, [§차원, ⁋명제 5](/ko/math/scheme_theory/dimension#prop5)에 의하여 그 closure와 차원이 같고, 이 closure는 $x$를 담는 어떤 component 안에 들어가므로 $\dim_{\overline{x}}X_{\overline{s}}\leq\dim_xX_s$임은 자명하다. 반대방향을 보이기 위해 $x$를 담는 $X_s$의 component $W$를 reduced structure로 잡으면, $\overline{x}$는 base change $W_\mathbb{K}=W\times_{\Spec\kappa(s)}\Spec\mathbb{K}$에 속한다. $W=\Spec A$라 하면 $A$는 domain이고 $A\otimes_{\kappa(s)}\mathbb{K}$는 free $A$-module이므로, 만일 그 minimal prime $\mathfrak{q}$가 $\mathfrak{q}\cap A\neq 0$을 만족한다면 [\[가환대수학\] §매개계, ⁋보조정리 8](/ko/math/commutative_algebra/system_of_parameters#lem8)에 의하여 $0$ 위로 가는 prime을 $\mathfrak{q}$ 안에서 찾을 수 있어 minimality에 모순이다. 즉 $W_\mathbb{K}$의 각 component는 $W$의 generic point 위로 가며, 그럼 이는 dominant integral morphism을 주므로 [§차원, ⁋명제 5](/ko/math/scheme_theory/dimension#prop5)에 의하여 $W$와 차원이 같다. 한편 $\overline{x}$를 담는 $W_\mathbb{K}$의 component는 $\overline{x}$를 담는 $X_{\overline{s}}$의 어떤 component 안에 들어가므로 $\dim_{\overline{x}}X_{\overline{s}}\geq \dim W$이고, $x$를 담는 $X_s$의 모든 component에 대하여 supremum을 취하면 $\dim_{\overline{x}}X_{\overline{s}}\geq\dim_xX_s$을 얻는다. 이로부터 우리는 원하는 등식 $\dim_{\overline{x}}X_{\overline{s}}=\dim_xX_s$을 얻는다.
:::

이로부터 등식 ($\ast$)는 같은 가정 하에서 $X$의 점 $x$에 대한 조건

$$\dim_{\kappa(x)}\bigl(\Omega_{X/S}\otimes \kappa(x)\bigr)=\dim_xX_s$$

으로 이해할 수 있다. 여기에서 $\Omega_{X/S}$가 locally free이면 위의 fiber dimension이 rank와 같으므로, 이 조건은 rank가 fiber의 local dimension과 일치한다는 것으로 바꾸어 쓸 수 있다. 이 보조정리를 통하여, cotangent sheaf의 local freeness로부터 smoothness를 읽어낼 수 있다.

::: 명제 3
Locally of finite presentation인 morphism $\varphi:X \rightarrow S$가 flat하고, $\Omega_{X/S}$가 locally free sheaf이며 각 $x\in X$에서 그 rank가 $s=\varphi(x)$ 위 fiber의 local dimension $\dim_xX_s$와 같다고 하자. 그럼 $\varphi$는 smooth하다.
:::
::: 증명
$\varphi$가 flat하므로 각 $s\in S$에 대하여 geometric fiber $X_{\overline{s}}$가 regular임을 보이면 충분하다. $\mathbb{K}=\overline{\kappa(s)}$라 하자.

먼저 주어진 주장을 $X_{\overline{s}}$의 closed point $z$에서 확인한다. $X_{\overline{s}}$는 algebraically closed field $\mathbb{K}$ 위에서 locally of finite presentation이므로 ([§올곱, ⁋명제 16](/ko/math/scheme_theory/fiber_products#prop16)) $z$를 담는 affine open subset $\Spec\bigl(\mathbb{K}[\x_1,\ldots, \x_n]/\mathfrak{a}\bigr)$을 택할 수 있고, $z$에 해당하는 ideal이 maximal이므로 [\[가환대수학\] §영점정리, ⁋보조정리 5](/ko/math/commutative_algebra/nullstellensatz#lem5)에 의하여 이는 어떤 $a\in \mathbb{K}^n$에 대한 $(\x_1-a_1,\ldots, \x_n-a_n)$의 image이고 따라서 $\kappa(z)=\mathbb{K}$이다. 즉 $z$는 $\mathbb{K}$-point이며, 우리는 [§미분과 여접층, ⁋정의 8](/ko/math/scheme_theory/sheaf_of_differentials#def8) 직후에 이러한 점에 대해서는

$$\Omega_{X_{\overline{s}}/\mathbb{K}}\otimes\kappa(z)\cong\mathfrak{m}_z/\mathfrak{m}_z^2$$

이 성립하는 것을 확인하였다.

이제 $z$의 $X_s$에서의 image를 $x$라 하자. $\Omega_{X/S}$가 locally free이므로 그 $x$에서의 fiber dimension은 rank와 같고, 가정에 의하여 이 값은 다시 $\dim_x X_s$와 같으므로, [보조정리 2](#lem2)는 좌변의 차원 또한 이 값과 같으며 따라서 $\dim_xX_s=\dim_zX_{\overline{s}}$임을 준다. 한편 $z$가 closed point이므로 $\dim_zX_{\overline{s}}=\dim\mathcal{O}_{X_{\overline{s}},z}$이며, 따라서

$$\dim_{\kappa(z)}\mathfrak{m}_z/\mathfrak{m}_z^2=\dim \mathcal{O}_{X_{\overline{s}},z}$$

를 얻는다. Regular local ring이기 위해서는 maximal ideal이 $\dim$개의 원소로 생성되는 Noetherian local ring이어야 하는데 ([\[가환대수학\] §차원, ⁋정의 12](/ko/math/commutative_algebra/Krull_dimension#def12)), [\[가환대수학\] §정수적 확장, ⁋보조정리 8](/ko/math/commutative_algebra/integral_extension#lem8)에 의하여 이는 위의 등식과 동치이므로 $\mathcal{O}_{X_{\overline{s}},z}$는 regular local ring이다.

이제 임의의 점 $\overline{x}\in X_{\overline{s}}$에 대하여 $\cl(\overline{x})$ 안의 closed point $z$를 택하면 ([§차원, ⁋명제 11](/ko/math/scheme_theory/dimension#prop11)에 의하여 공집합이 아닌 locally closed subset은 언제나 closed point를 담는다), $z$의 열린근방은 모두 $\overline{x}$를 담으므로 $\mathcal{O}_{X_{\overline{s}},\overline{x}}$는 $\mathcal{O}_{X_{\overline{s}},z}$의 localization이다. Regular local ring의 localization은 regular이므로 ([\[가환대수학\] §정칙성의 호몰로지 판정, ⁋따름정리 4](/ko/math/commutative_algebra/homological_criterion_for_regularity#cor4)) $\mathcal{O}_{X_{\overline{s}},\overline{x}}$ 또한 regular local ring이고, 곧 $X_{\overline{s}}$는 regular scheme이다.
:::

[명제 3](#prop3)의 조건 아래에서 $\Omega_{X/S}$의 rank를 $\varphi$의 *relative dimension<sub>상대차원</sub>*이라 부른다. 직관적으로 이것이 보는 것은 $\varphi$의 fiber 방향 tangent space의 차원이다. 즉 relative tangent bundle $\Omega_{X/S}^\vee$의 $x$에서의 fiber가 곧 $X_s$의 $x$에서의 Zariski tangent space이므로 ([§미분과 여접층, ⁋정의 8](/ko/math/scheme_theory/sheaf_of_differentials#def8)), relative dimension이 $r$이라는 것은 각 점에서 이 tangent space가 $r$차원이라는 것이다.

이제 임의의 locally of finite presentation인 scheme morphism $\varphi: X \rightarrow S$에 대하여, 우리는 국소적으로는 이 morphism을

$$\Spec\bigl(A[\x_1,\ldots, \x_n]/(f_1,\ldots, f_r)\bigr)\rightarrow \Spec A$$

의 형태로 바꾸어 쓸 수 있는 것을 안다. 그럼 다음 정리는 이와 같은 상황에서, 만일 $x\in X$에서의 Jacobian matrix의 rank가 $X$를 정의하는 방정식의 개수 $r$과 맞아떨어진다면 $\varphi$는 $x$의 어떤 근방에서 relative dimension $n-r$의 smooth morphism임을 보여준다. 

::: 정리 4 (Jacobian criterion)
$S=\Spec A$ 위에서

$$X=\Spec\bigl(A[\x_1,\ldots, \x_n]/(f_1,\ldots, f_r)\bigr)$$

이라 하고, $x\in X$를 한 점이라 하자. $x$에서 Jacobian matrix

$$J=\Bigl(\frac{\partial f_i}{\partial \x_j}\Bigr)_{\substack{1\leq i\leq r\\ 1\leq j\leq n}}$$

의 $\kappa(x)$ 위에서의 rank가 $r$이면, $\varphi:X \rightarrow S$는 $x$의 어떤 열린 근방에서 relative dimension $n-r$의 smooth morphism이다.
:::
::: 증명
[명제 3](#prop3)에 의하여 우리가 보여야 할 것은 $x$의 어떤 근방 위에서 $\varphi$가 flat하고 $\Omega_{X/S}$가 rank $n-r$의 locally free sheaf이며, 그 근방의 각 점에서 fiber의 local dimension이 $n-r$이라는 것이다. 우선 우리는 $\varphi$를 다음의 식

{% diagram Math/Scheme_Theory/Smooth_and_Etale_Morphisms-3.svg width="5.94em" alt="factorization" %}

와 같이 분해한다. 여기서 $\mathbb{A}_S^n \rightarrow S$는 canonical한 structure map이고, 수평 방향의 $X\hookrightarrow \mathbb{A}_S^n$은 $X$를 $(f_1,\ldots, f_r)$이 정의하는 closed subscheme으로 넣어주는 closed embedding이다. 이제

$$B=A[\x_1,\ldots, \x_n],\qquad \mathfrak{a}=(f_1,\ldots, f_r), \qquad C=B/\mathfrak{a}$$

이라 하면 $\mathbb{A}^n_S=\Spec B$이고 $X=\Spec C$이라 할 수 있다. 그럼 [§미분과 여접층, ⁋명제 2](/ko/math/scheme_theory/sheaf_of_differentials#prop2)에서 다음의 exact sequence

$$\mathfrak{a}/\mathfrak{a}^2 \overset{\bar{d}}{\longrightarrow} \Omega_{B/A}\otimes_BC \longrightarrow \Omega_{C/A} \longrightarrow 0$$

이 존재하며, 여기서 $\Omega_{B/A}$는 [§미분과 여접층, ⁋명제 9](/ko/math/scheme_theory/sheaf_of_differentials#prop9)에 의하여 $\dd{\x_1},\ldots, \dd{\x_n}$을 기저로 하는 rank $n$의 free $B$-module이므로, $\Omega_{B/A}\otimes_BC$는 이들을 basis로 하는 rank $n$ free $C$-module이다. 그럼 이 canonical base 하에서, $\bar{d}$는

$$\bar{d}: \mathfrak{a}/ \mathfrak{a}^2\rightarrow \Omega_{B/A}\otimes_BC;\qquad f_i+\mathfrak{a}^2\mapsto \dd{f_i}=\sum_j\frac{\partial f_i}{\partial \x_j}\dd{\x_j}$$

로 쓸 수 있다. 그럼 주장에서 주어진 Jacobian matrix는 다음의 surjective $C$-module homomorphism

$$\pi: C^{\oplus r} \rightarrow \mathfrak{a}/\mathfrak{a}^2;\qquad e_i\mapsto f_i+\mathfrak{a}^2$$

을 $\bar{d}$와 합성하여 얻어진 다음 함수

$$\bar{d}\circ\pi: C^{\oplus r}\rightarrow \mathfrak{a}/\mathfrak{a}^2\rightarrow \Omega_{B/A}\otimes_BC;\qquad e_i\mapsto \sum_j\frac{\partial f_i}{\partial \x_j}\dd{\x_j}$$

을 $e_i$와 $\dd{\x_j}$ basis에 대해 표현한 행렬을 transpose한 것이며, 그 각각의 성분들은 $X$ 위의 함수이다. 

이제 가정에 의해 $J$가 full rank이므로, 어떤 index $j_1,\ldots, j_r$이 존재하여 그 열들이 이루는 $r\times r$ minor $\Delta_{j_1,\ldots,j_r}$가 $x$에서 $0$이 아니도록 할 수 있다. 그럼 이제 $\Omega_{B/A}\otimes_BC$의 basis들 중, 이들 $\dd{\x_{j_k}}$들이 생성하는 부분공간으로의 projection을 $\pr_{j_1,\ldots,j_r}$이라 하면 위의 행렬 표현에 의하여

$$\pr_{j_1,\ldots,j_r}\circ\bar{d}\circ\pi: C^{\oplus r}\rightarrow\mathfrak{a}/\mathfrak{a}^2\rightarrow \Omega_{B/A}\otimes_BC\rightarrow C^{\oplus r}$$

을 $e_i$들에 대해 표현한 행렬이 $\Delta_{j_1,\ldots,j_r}$를 정의하는 $r\times r$ 행렬의 transpose로 주어진다. 따라서 이 minor $\Delta=\Delta_{j_1,\ldots,j_r}$를 역수로 추가해주면 다음의 함수

$$(\pr_{j_1,\ldots,j_r}\circ\bar{d}\circ\pi)_\Delta: C_\Delta^{\oplus r}\rightarrow C_\Delta^{\oplus r}$$

은 automorphism이 된다. ([\[다중선형대수학\] §행렬식, ⁋따름정리 3](/ko/math/multilinear_algebra/determinants#cor3)) 따라서 $\pi_\Delta$가 injective $C_\Delta$-module homomorphism이어야 하는데, $\pi$는 원래부터 surjection이었으므로 $\pi_\Delta$는 $C_\Delta$-module isomorphism이고 이로부터 $(\mathfrak{a}/\mathfrak{a}^2)_\Delta$가 rank $r$ free $C_\Delta$-module인 것을 안다. 한편

$$\bigl((\pr_{j_1,\ldots,j_r}\circ\bar{d}\circ\pi)_\Delta^{-1}\circ \pr_{j_1,\ldots, j_r}\bigr)\circ(\bar{d}\circ\pi)_\Delta=\id_{C_\Delta^{\oplus r}}$$

이므로, $\pi_\Delta$와 $\pi_\Delta^{-1}$을 앞뒤로 합성해주면

$$\left(\pi_\Delta\circ (\pr_{j_1,\ldots,j_r}\circ\bar{d}\circ\pi)_\Delta^{-1}\circ \pr_{j_1,\ldots, j_r}\right)\circ\bar{d}_\Delta=\id_{(\mathfrak{a}/\mathfrak{a}^2)_\Delta}$$

가 되어 $\bar{d}_\Delta$는 split injection이다. 일반적으로 [\[다중선형대수학\] §완전열, ⁋명제 10](/ko/math/multilinear_algebra/exact_sequences#prop10)에 의하여 split injection $\bar{d}_\Delta$의 cokernel은 그 retraction의 kernel로 주어지며, 여기에서 $\pi_\Delta$와 $(\pr_{j_1,\ldots,j_r}\circ\bar{d}\circ\pi)_\Delta^{-1}$는 모두 isomorphism이므로 이는 정확히 $(\pr_{j_1,\ldots,j_r})_\Delta$의 kernel, 즉 $j\notin\{j_1,\ldots, j_r\}$인 $\dd{\x_j}$들이 생성하는 rank $n-r$의 free submodule로 주어진다. 그럼 tensor product는 cokernel을 보존하므로 이것이 곧 $\Omega_{C/A}\otimes_CC_\Delta$여야 하고, 따라서 $\Omega_{C/A}$는 $D(\Delta)=\Spec C_\Delta$ 위에서 rank $n-r$ locally free sheaf가 된다.

이제 [명제 3](#prop3)을 사용하기 위해서는 $\varphi$가 $x$의 어떤 열린 근방에서 flat이고, 이 근방의 각 점에서 fiber의 local dimension이 $n-r$임을 보여야 한다. 우선 $\varphi$의 flatness부터 보인다. 이를 위해 우리는 우선 $A$가 Noetherian인 경우로의 reduction을 한 차례 진행해야 한다. 기본적으로 이는 우리가 필요로 하는 정보가 $A$ 전체가 아니라 $f_1,\ldots, f_r$의 계수들이 $A$ 안에서 생성하는 $\mathbb{Z}$-subalgebra $A_0$에 담겨있으므로 가능하다. 그럼 [\[가환대수학\] §기본 개념들, ⁋따름정리 13](/ko/math/commutative_algebra/basic_notions#cor13)에 의해 $A_0$은 Noetherian이고, $C_0=A_0[\x_1,\ldots, \x_n]/(f_1,\ldots, f_r)$로 두면 $C=C_0\otimes_{A_0}A$이다. $A_0$의 정의에 의하여, $J$ 또한 $C_0$에서의 행렬로 볼 수 있고, 따라서 그 minor $\Delta$ 또한 마찬가지이다. 문제의 점 $x$의 $\Spec C_0$에서의 image를 $x_0$이라 하면, 이에 대응되는 prime ideal은 $x$에 대응되는 prime ideal의 preimage이므로, $\Delta$는 $x_0$에서도 $0$이 아니며, 따라서 $J$ 또한 $x_0$에서 여전히 full rank $r$을 가진다. 즉, 우리는 문제의 조건을 모두 $X_0$, $S_0$ 위로 가져올 수 있으며, 만일 이 가정 하에서 $\varphi_0: X_0\rightarrow S_0$의 flatness를 보일 수 있다면 flatness가 base change에 의해 보존되므로 $\varphi$의 flatness를 복원할 수 있다.

따라서 $A$가 처음부터 Noetherian이었다고 가정하자. $X$의 임의의 점 $x$와 그 image $s=\varphi(x)$에 대하여, $x$를 $\mathbb{A}_S^n=\Spec B$의 점으로 보아 대응되는 $B$의 prime ideal을 $\mathfrak{p}$, $s$에 대응되는 $A$의 prime ideal을 $\mathfrak{q}$라 하면 structure map의 정의에 의하여 $\mathfrak{q}=\mathfrak{p}\cap A$이다. 우리 목적은 [\[가환대수학\] §평탄성과 국소화, ⁋따름정리 4](/ko/math/commutative_algebra/local_criterion_for_flatness#cor4)를 *Noetherian* local ring $(A_\mathfrak{q}, \mathfrak{q}A_\mathfrak{q})$, 그 위의 local *Noetherian* algebra $(B_\mathfrak{p}, \mathfrak{p}B_\mathfrak{p})$, 그리고 그 자신을 module로 본 $B_\mathfrak{p}$와 $\mathfrak{p}B_\mathfrak{p}$의 원소 $f_1,\ldots, f_r$에 적용하는 것이다. 이를 기하적으로 살펴보면 다음과 같다. 우선 $A_\mathfrak{q}$는 $s=\varphi(x)$에서의 local ring $\mathcal{O}_{S, s}$이며, 마찬가지로 $B_\mathfrak{p}$는 $x\in X\subset \mathbb{A}_S^n$에서의 local ring $\mathcal{O}_{\mathbb{A}_S^n, x}$이고, 그 maximal ideal $\mathfrak{p}B_\mathfrak{p}$는 $x$에서 소멸하는 함수들로 이루어진다. 한편 $\mathfrak{q}B_\mathfrak{p}$는 $s$에서 소멸하는 $S$ 위의 함수들을 $\varphi$를 따라 당겨온 것이 생성하는 ideal이며, 이것으로 나눈 $B_\mathfrak{p}/\mathfrak{q}B_\mathfrak{p}$는 $s$ 위 fiber의 $x$에서의 local ring이다. 이 그림에서 $x$는 $f_1,\ldots, f_r$들이 깎아낸 zero set $X$의 점이므로 $f_i$는 모두 $\mathfrak{p}B_\mathfrak{p}$에 속하며, 그럼 따름정리의 주장은 만일 $B_\mathfrak{p}$가 flat $A_\mathfrak{q}$-module이고 이들 $f_i$가 $B_\mathfrak{p}/\mathfrak{q}B_\mathfrak{p}$에서 regular sequence라면, 원래의 $B_\mathfrak{p}$에서도 이들은 regular sequence이며 이들이 잘라내는 zero set의 $x$에서의 local ring이 $A_\mathfrak{q}$ 위에서 flat이라는 것이다. 

우선 $B$가 free $A$-module이므로 $B_\mathfrak{p}$가 flat $A_\mathfrak{q}$-module임은 당연하다. 따라서 우리가 보여야 할 것은 $f_1,\ldots, f_r$의 image가 $R=B_\mathfrak{p}/\mathfrak{q}B_\mathfrak{p}$에서 regular sequence를 이룬다는 것 뿐이다. 편의상 $R$의 maximal ideal을 $\mathfrak{m}$이라 적기로 하자. 

우선 $B/\mathfrak{q}B=(A/\mathfrak{q})[\x_1,\ldots, \x_n]$에서 $A/\mathfrak{q}$의 영이 아닌 원소들은 모두 $\mathfrak{p}$ 바깥에 있으므로 $R$은 $\kappa(\mathfrak{q})[\x_1,\ldots, \x_n]$을 $\mathfrak{p}$가 유도하는 prime ideal에서 localize한 것이고, [\[가환대수학\] §정칙성의 호몰로지 판정, ⁋따름정리 6](/ko/math/commutative_algebra/homological_criterion_for_regularity#cor6)에 의하여 이 polynomial ring이 regular ring이므로 $R$은 residue field $\kappa(\mathfrak{p})=\kappa(x)$를 가지는 regular local ring이다. ([\[가환대수학\] §차원, ⁋정의 12](/ko/math/commutative_algebra/Krull_dimension#def12)) 이제 $f_i$의 $R$에서의 image를 $\bar{f}_i$라 하면 $\bar{f}_i\in\mathfrak{m}$가 성립하고, $R$이 regular local ring이므로 $\mathfrak{m}$은 $\dim R$개의 원소로 생성되며, 우리는 [\[가환대수학\] §정칙국소환, ⁋따름정리 3](/ko/math/commutative_algebra/regular_local_rings#cor3)에 의하여 이러한 generator들이 regular sequence를 준다는 것을 안다. 따라서 우리는 $\bar{f}_1,\ldots, \bar{f}_r$을 포함하는 regular system of parameters를 만든 후, regular sequence의 앞부분이 다시 regular sequence라는 사실을 사용하여 결론을 낼 것이다. 

이제 $\mathfrak{m}$의 $\dim R$개의 generator를 만들어야 하며, 이 대신 $\mathfrak{m}/\mathfrak{m}^2$을 $\kappa(\mathfrak{p})$-벡터공간으로서 생성하는 원소들을 찾으면 충분하다. ([\[가환대수학\] §정수적 확장, ⁋보조정리 8](/ko/math/commutative_algebra/integral_extension#lem8)) 이제 [§미분과 여접층, ⁋명제 2](/ko/math/scheme_theory/sheaf_of_differentials#prop2)를 $\kappa(\mathfrak{q})$-algebra $R$과 그 ideal $\mathfrak{m}$에 적용하면 conormal exact sequence

$$\mathfrak{m}/\mathfrak{m}^2\longrightarrow\Omega_{R/\kappa(\mathfrak{q})}\otimes_R\kappa(\mathfrak{p})\longrightarrow \Omega_{\kappa(\mathfrak{p})/\kappa(\mathfrak{q})}\longrightarrow 0$$

을 얻으며, 그 첫째 morphism은 $u+\mathfrak{m}^2\mapsto\dd{u}$로 주어진다. 한편 $R$이 $\kappa(\mathfrak{q})[\x_1,\ldots, \x_n]$의 localization이므로 [\[가환대수학\] §미분, ⁋명제 7](/ko/math/commutative_algebra/differentials#prop7)과 [§미분과 여접층, ⁋명제 9](/ko/math/scheme_theory/sheaf_of_differentials#prop9)에 의하여 $\Omega_{R/\kappa(\mathfrak{q})}$는 $\dd{\x_1},\ldots, \dd{\x_n}$을 기저로 하는 free $R$-module이고, 따라서 $u\in R$의 $\kappa(\mathfrak{p})$에서의 image를 $u(\mathfrak{p})$로 적으면 이 morphism은 $\kappa(\mathfrak{p})$-linear map

$$\mathfrak{m}/\mathfrak{m}^2 \longrightarrow \kappa(\mathfrak{p})^{\oplus n};\qquad u\mapsto \sum_j\frac{\partial u}{\partial \x_j}(\mathfrak{p})\dd{\x_j}$$

이다. 특히 이 map은 $\bar{f}_i$의 class를 $J$의 $i$번째 행으로 보내며, Jacobian의 가정에 의하여 이들의 image들이 일차독립인 벡터들이므로 $\bar{f}_i$의 class들 또한 일차독립이다. 따라서 이 class들에서 basis를 완성하여 $\mathfrak{m}/\mathfrak{m}^2$의 basis를 만들면 원하는 $\mathfrak{m}$의 basis를 얻으며, 앞선 논증들에 의해 $f_1,\ldots, f_r$은 $B_\mathfrak{p}$의 regular sequence이고 quotient $C_\mathfrak{p}=B_\mathfrak{p}/\mathfrak{a}B_\mathfrak{p}$는 $A_\mathfrak{q}$ 위에서 flat이다. 즉 $\varphi$는 $x$에서 flat이고 ([§평탄사상, ⁋정의 1](/ko/math/scheme_theory/flat_morphisms#def1)), 따라서 [§평탄사상, ⁋정리 20](/ko/math/scheme_theory/flat_morphisms#thm20)에 의하여 $\varphi$는 $x$의 어떤 열린근방 위에서 flat하다.

이 열린근방과 앞서 얻은 $D(\Delta)$의 교집합을 $U$라 하면, 이 위에서 $\varphi$가 flat하고 $\Omega_{C/A}$는 rank $n-r$의 locally free이다. 따라서 [명제 3](#prop3)을 적용하기 위해 보여야 할 마지막 조각은 $U$의 각 점에서 fiber의 local dimension이 $n-r$이라는 것이다. 이는 위의 fiber 논증을 $U$의 다른 점에서 반복하여 얻는다. $U$의 점 $y$와 $s'=\varphi(y)$에 대하여 fiber $X_{s'}$의 $y$를 지나는 component의 generic point를 $\eta$라 하면, $\Delta$가 $\eta$에서도 가역이어서 $J$의 rank가 $r$이므로, 같은 논증에 의하여 $\bar{f}_1,\ldots, \bar{f}_r$의 class들은 regular local ring $\mathcal{O}_{\mathbb{A}^n_{\kappa(s')},\eta}$의 $\mathfrak{m}_\eta/\mathfrak{m}_\eta^2$ 안에서 일차독립이다. 곧 그 component의 codimension인 $\dim\mathcal{O}_{\mathbb{A}^n_{\kappa(s')},\eta}$는 $r$ 이상이고, $\eta$가 $(\bar{f}_1,\ldots, \bar{f}_r)$을 포함하는 minimal prime이므로 [\[가환대수학\] §차원, ⁋정리 7](/ko/math/commutative_algebra/Krull_dimension#thm7)이 반대 부등식을 주어 codimension은 정확히 $r$이며, 차원 공식에 의하여 ([\[가환대수학\] §뇌터 정규화, ⁋정리 4](/ko/math/commutative_algebra/noether_normalization#thm4)) component의 차원은 $n-r$이다. 따라서 $U$의 각 점에서 fiber의 local dimension이 rank와 일치하고, [명제 3](#prop3)에 의하여 $\varphi$는 relative dimension $n-r$의 smooth morphism이다.
:::

이 증명의 핵심적인 내용은 diagram

{% diagram Math/Scheme_Theory/Smooth_and_Etale_Morphisms-3.svg width="5.94em" alt="factorization" %}

에 모두 담겨있으며, 이를 따라 차원을 세어 보면 각각의 역할이 더 명확하다. 즉 우리는 $X\rightarrow S$를 relative affine space $\mathbb{A}^n_S \rightarrow S$의 방정식들 $f_1,\ldots, f_r$이 잘라내는 closed subscheme으로 보며, 이 때 Jacobian의 rank가 $r$이라는 가정이 그 $r$개의 조건이 서로 겹치지 않음을 보장한다. 그럼 남는 $n-r$차원은 $\dd{\x_1},\ldots, \dd{\x_n}$이 생성하는 rank $n$의 free module을 일차독립인 $\dd{f_1},\ldots, \dd{f_r}$로 나눈 $\Omega_{X/S}$의 rank이자, codimension $r$로 잘린 fiber의 차원이 되며, [명제 3](#prop3)이 요구하는 조건이 바로 이 두 값이 같다는 것이다. 

한편 증명은 $f_1,\ldots, f_r$이 $\mathcal{O}_{\mathbb{A}^n_S,x}$의 regular sequence라는 것도 함께 주었는데, 이는 $X\hookrightarrow \mathbb{A}^n_S$가 $x$ 근방에서 codimension $r$의 complete intersection이라는 뜻이다. ([§완전교차, ⁋정의 1](/ko/math/scheme_theory/complete_intersections#def1)) 다음 절에서 우리는 임의의 smooth morphism이 국소적으로 [정리 4](#thm4)의 꼴로 적힌다는 것을 보이므로 ([정리 6](#thm6)), 이로부터 smooth morphism은 언제나 국소적으로 이러한 complete intersection의 모양을 가진다는 것이 따라나온다.

## 매끄러운 사상의 국소 구조

[정리 4](#thm4)는 Jacobian 조건을 만족하는 방정식 표현이 주어졌을 때 smoothness를 주는데, 거꾸로 우리는 임의의 smooth morphism이 항상 국소적으로는 이러한 꼴임을 보일 수 있다. 우리는 우선 base가 field인 다음의 상황부터 시작한다. 이 경우 smooth 조건은 geometric fiber의 regularity 하나로 주어지므로, 남는 일은 그 regularity를 Jacobian의 rank로 번역하는 것뿐이다.

::: 보조정리 5
Field $\mathbb{K}$와 그 algebraic closure $\overline{\mathbb{K}}$, 그리고 다항식 $g_1,\ldots, g_m\in \mathbb{K}[\x_1,\ldots, \x_n]$에 대하여

$$X=\Spec\bigl(\mathbb{K}[\x_1,\ldots, \x_n]/(g_1,\ldots, g_m)\bigr)$$

이라 하고, base change $X_{\overline{\mathbb{K}}}=X\times_{\Spec\mathbb{K}}\Spec\overline{\mathbb{K}}$가 regular scheme이라 하자. 그럼 임의의 $x\in X$에 대하여 $c=n-\dim_xX$개의 첨자 $i_1,\ldots, i_c$와 $h\in \mathbb{K}[\x_1,\ldots, \x_n]$이 존재하여, $x\in D(h)$이고 $D(h)$ 위에서 $X$는 $g_{i_1},\ldots, g_{i_c}$가 정의하는 $\mathbb{A}^n_\mathbb{K}$의 closed subscheme과 일치하며, Jacobian $(\partial g_{i_k}/\partial \x_j)$의 어떤 $c\times c$ minor $\Delta$가 $D(h)$ 위에서 가역이다.
:::
::: 증명
앞서 [정리 4](#thm4)의 증명에서의 표기와 같이 $\mathfrak{a}=(g_1,\ldots, g_m)$이라 하고, $X_{\overline{\mathbb{K}}}$를 $\mathfrak{a}\overline{\mathbb{K}}[\x_1,\ldots, \x_n]$이 정의하는 $\mathbb{A}^n_{\overline{\mathbb{K}}}$의 closed subscheme으로 보자. [보조정리 2](#lem2)의 증명에서 우리는 $X_{\overline{\mathbb{K}}} \rightarrow X$가 surjective인 것을 알고 있으므로, 우리는 임의로 주어진 $x$에 대하여, 그 위의 점 $\overline{x}\in X_{\overline{\mathbb{K}}}$를 택할 수 있다.

가정에 의해 $X_{\overline{\mathbb{K}}}$의 local ring들은 regular이므로 특히 domain이고 ([\[가환대수학\] §정칙국소환, ⁋따름정리 1](/ko/math/commutative_algebra/regular_local_rings#cor1)), 따라서 각 점은 유일한 irreducible component에 속하며 local dimension은 곧 그 점이 포함된 component의 차원과 같다. $\overline{x}$가 포함된 component를 $Z$, 그 차원을 $d=\dim Z$라 하자. 그럼 $\overline{x}$의 $X_{\overline{\mathbb{K}}}$에서의 closure $\cl(\overline{x})$를 생각하면, 이는 $Z$에 포함된 닫힌집합이며 [§차원, ⁋명제 11](/ko/math/scheme_theory/dimension#prop11)의 둘째 결과에 의해 $X_{\overline{\mathbb{K}}}$의 closed point $z$를 포함한다. 그럼 [\[가환대수학\] §뇌터 정규화, ⁋정리 4](/ko/math/commutative_algebra/noether_normalization#thm4)에 의하여 $\dim\mathcal{O}_{X_{\overline{\mathbb{K}}},z}=d$이고, 또 $\overline{\mathbb{K}}$가 algebraically closed이므로 [\[가환대수학\] §영점정리, ⁋보조정리 5](/ko/math/commutative_algebra/nullstellensatz#lem5)에 의하여 $z$에 해당하는 maximal ideal은 어떤 $a\in \overline{\mathbb{K}}^n$에 대한 $(\x_1-a_1,\ldots, \x_n-a_n)$의 image이고, 특히 $\kappa(z)=\overline{\mathbb{K}}$이다.

이제 $z$에서 Jacobian의 rank를 계산하자. Closed embedding $X_{\overline{\mathbb{K}}}\hookrightarrow \mathbb{A}^n_{\overline{\mathbb{K}}}$의 conormal exact sequence를 생각하면, 가운데 항은 $\dd{\x_1},\ldots, \dd{\x_n}$을 기저로 하는 rank $n$의 free module이고, defining ideal이 $g_1,\ldots, g_m$으로 생성되므로 첫 morphism $\bar{d}$의 image는 $\dd{g_i}=\sum_j(\partial g_i/\partial \x_j)\dd{\x_j}$들이 생성한다. 이 sequence를 $\kappa(z)$로 내리면

$$\Omega_{X_{\overline{\mathbb{K}}}/\overline{\mathbb{K}}}\otimes\kappa(z)\cong\coker\bigl(\kappa(z)^{\oplus m} \longrightarrow \kappa(z)^{\oplus n}\bigr)$$

를 얻으며, 여기에서 오른쪽 morphism은 $z$에서 계산한 Jacobian $J=(\partial g_i/\partial \x_j)$의 transpose이다. 한편 $z$가 $\overline{\mathbb{K}}$-point이므로 좌변은 $\mathfrak{m}_z/\mathfrak{m}_z^2$이고 ([§미분과 여접층, ⁋정의 8](/ko/math/scheme_theory/sheaf_of_differentials#def8) 직후), $\mathcal{O}_{X_{\overline{\mathbb{K}}},z}$가 regular local ring이므로 그 차원은 $\dim\mathcal{O}_{X_{\overline{\mathbb{K}}},z}=d$이다. ([\[가환대수학\] §차원, ⁋정의 12](/ko/math/commutative_algebra/Krull_dimension#def12)) 따라서 $\rank J(z)=n-d$이며, 이 값을 $c$라 쓰면 $J(z)$의 영이 아닌 $c\times c$ minor $\Delta\in \mathbb{K}[\x_1,\ldots, \x_n]$가 존재한다. 이를 정의하는 index를 $i_1,\ldots, i_c$라 하고 $f_k=g_{i_k}$라 하자. $\mathfrak{a}'=(f_1,\ldots, f_c)$라 하고 $X'=\Spec\bigl(\mathbb{K}[\x_1,\ldots, \x_n]/\mathfrak{a}'\bigr)$으로 두면 $\mathfrak{a}'\subseteq \mathfrak{a}$이므로 $X$는 $X'$의 closed subscheme이며, 우리의 주장은 이 포함관계가 $x$ 근방에서는 등호라는 것이다.

우선 주장을 $z$에서의 local ring에서 확인한다. $\overline{\mathbb{K}}[\x_1,\ldots, \x_n]$을 $z$에 대응하는 maximal ideal에서 localize한 것을 $R=\mathcal{O}_{\mathbb{A}^n_{\overline{\mathbb{K}}},z}$이라 하면, 이는 residue field $\overline{\mathbb{K}}$를 가지는 차원 $n$의 regular local ring이다. 그럼 $X_{\overline{\mathbb{K}}}$와 $X'_{\overline{\mathbb{K}}}$는 $\mathbb{A}^n_{\overline{\mathbb{K}}}$ 안에서 각각 $\mathfrak{a}$와 $\mathfrak{a}'$이 잘라낸 closed subscheme이므로, $z$에서의 local ring은 $R$을 이 두 ideal로 나눈

$$\mathcal{O}_{X_{\overline{\mathbb{K}}},z}=R/\mathfrak{a}R,\qquad R'=\mathcal{O}_{X'_{\overline{\mathbb{K}}},z}=R/\mathfrak{a}'R$$

이며, 우리가 $z$에서 보일 것은 이 두 ideal이 일치한다는 것, 곧 $\mathfrak{a}R=\mathfrak{a}'R$이다. [정리 4](#thm4)의 증명과 마찬가지로, 조건 $\Delta(z)\neq 0$에 의하여 $f_1,\ldots, f_c$의 class들은 $\mathfrak{m}_R/\mathfrak{m}_R^2$에서 일차독립이고, 따라서 $\mathfrak{m}_R$은 이들과 다른 $n-c$개의 원소로 생성된다. 그럼 $R'$의 maximal ideal은 $n-c$개의 원소로 생성되고 [\[가환대수학\] §차원, ⁋정리 7](/ko/math/commutative_algebra/Krull_dimension#thm7)에 의하여 $\dim R'\leq n-c=d$이다. 그런데 $\mathcal{O}_{X_{\overline{\mathbb{K}}},z}$는 $R'$의 quotient이고 그 차원이 $d$이므로 $\dim R'\geq d$이며, 결국 $\dim R'=d$이다. 곧 $R'$의 maximal ideal이 $\dim R'$개의 원소로 생성되어 $R'$은 regular local ring이고 ([\[가환대수학\] §차원, ⁋정의 12](/ko/math/commutative_algebra/Krull_dimension#def12)), 특히 domain이다. 이제 결론에 반하여 surjection $R' \rightarrow \mathcal{O}_{X_{\overline{\mathbb{K}}},z}$의 kernel $\mathfrak{b}=\mathfrak{a}R/\mathfrak{a}'R$이 영이 아니라 하자. $R'/\mathfrak{b}$의 prime ideal들은 $\mathfrak{b}$를 포함하는 $R'$의 prime ideal들이고 그러한 chain은 모두 $\mathfrak{b}$ 위의 minimal prime에서 시작하므로, $\dim R'/\mathfrak{b}=\dim R'/\mathfrak{p}$이도록 하는 $\mathfrak{b}$ 위의 minimal prime $\mathfrak{p}$가 존재한다. 그런데 $\mathfrak{b}\subseteq\mathfrak{p}$이고 가정에 의해 $\mathfrak{b}\neq 0$이므로 $\mathfrak{p}\neq 0$이다. 한편 $R'$이 domain이므로 $0$ 또한 $R'$의 prime ideal이고, 따라서 $R'/\mathfrak{p}$의 길이 $\dim R'/\mathfrak{p}$인 chain 앞에 $0\subsetneq\mathfrak{p}$를 이어 붙일 수 있어 $\dim R'\geq \dim R'/\mathfrak{p}+1$을 얻는다. 즉, $\dim\mathcal{O}_{X_{\overline{\mathbb{K}}},z}<\dim R'=d$가 되어 모순이므로 $\mathfrak{b}=0$이어야 하고, 이로부터 $z$에서의 주장이 얻어진다. 한편 $\mathfrak{b}$는 $X_{\overline{\mathbb{K}}}\subseteq X'_{\overline{\mathbb{K}}}$의 ideal sheaf에 $z$에서의 stalk을 취한 것이고, 이 sheaf는 $g_1,\ldots, g_m$의 image로 생성되어 finite type이므로, $\mathfrak{b}=0$으로부터 이 sheaf가 실제로 $z$의 어떤 열린근방 위에서 소멸함을 얻는다. 가정에 의해 $z\in \cl(\overline{x})$이므로 이 근방은 $\overline{x}$를 포함한다.

마지막으로 $\mathbb{K}$로 내려온다. $X\subseteq X'$의 ideal sheaf를 $\mathcal{J}$라 하면 $\mathbb{K} \rightarrow \overline{\mathbb{K}}$가 flat이므로 $\mathcal{J}$의 $\overline{\mathbb{K}}$로의 base change가 $X_{\overline{\mathbb{K}}}\subseteq X'_{\overline{\mathbb{K}}}$의 ideal sheaf이고, 따라서 $\mathcal{J}_x\otimes_{\mathcal{O}_{X',x}}\mathcal{O}_{X'_{\overline{\mathbb{K}}},\overline{x}}=0$이다. 그런데 $\mathcal{O}_{X',x} \rightarrow \mathcal{O}_{X'_{\overline{\mathbb{K}}},\overline{x}}$는 flat local homomorphism이므로 [§평탄사상, ⁋보조정리 15](/ko/math/scheme_theory/flat_morphisms#lem15)에 의하여 영이 아닌 module을 영으로 보내지 않으며, 곧 $\mathcal{J}_x=0$이다. $\mathcal{J}$ 또한 finite type이므로 $x$의 어떤 principal open 근방 위에서 소멸한다. 한편 $D(\Delta)$은 $z$를 담는 열린집합이라 $\overline{x}$를 담고, $\kappa(x)\hookrightarrow\kappa(\overline{x})$이므로 $\Delta(x)\neq 0$이다. 그럼 앞의 principal open과 $D(\Delta)$의 교집합을 $D(h)$로 두면 원하는 성질이 모두 성립한다. 끝으로 [보조정리 2](#lem2)를 $S=\Spec\mathbb{K}$에 적용하면 $d=\dim_{\overline{x}}X_{\overline{\mathbb{K}}}=\dim_xX$이므로 $c=n-\dim_xX$이다.
:::

Base가 일반의 scheme일 때에는 이 표현을 fiber 위에서 얻은 뒤 base 방향으로 들어올리게 되며, 이 과정에서 필요한 것이 flatness 가정이다.

::: 정리 6 (국소 구조)
Smooth morphism $\varphi:X \rightarrow S$와 점 $x\in X$, $s=\varphi(x)$에 대하여, $s$의 affine 열린근방 $\Spec A$와 그 위에 놓인 $x$의 열린근방으로서

$$\Spec\Bigl(\bigl(A[\x_1,\ldots, \x_n]/(f_1,\ldots, f_c)\bigr)_g\Bigr)$$

와 $S$-scheme으로서 isomorphic한 것이 존재한다. 여기에서 Jacobian $(\partial f_i/\partial \x_j)$의 어떤 $c\times c$ minor는 이 ring에서 가역이며, $c=n-\dim_xX_s$이다.
:::
::: 증명
문제가 국소적이므로 $S=\Spec A$이고 $x$가 affine open $\Spec C$에 속한다고 가정할 수 있다. 또, $\varphi$가 locally of finite presentation이므로 $C=A[\x_1,\ldots, \x_n]/(u_1,\ldots, u_m)$으로 적을 수 있다. 이 때의 ideal을 $\mathfrak{a}=(u_1,\ldots, u_m)$이라 하자.

Fiber $X_s$는 $\kappa(s)[\x_1,\ldots, \x_n]$을 $u_i$의 image $\overline{u}_i$들로 나눈 것이고, $\varphi$가 smooth하므로 그 base change $X_{\overline{s}}$는 regular이다. 따라서 [보조정리 5](#lem5)를 $\mathbb{K}=\kappa(s)$와 $\overline{u}_1,\ldots, \overline{u}_m$에 적용할 수 있으며, 그 결과로 $c=n-\dim_xX_s$개의 index $i_1,\ldots, i_c$가 존재하여 $x$의 어떤 열린근방 위에서 $X_s$가 $\overline{u}_{i_1},\ldots, \overline{u}_{i_c}$가 정의하는 closed subscheme과 일치하며 이 index들이 주는 $c\times c$ minor가 그 위에서 가역이 되도록 할 수 있다. [보조정리 5](#lem5)에서의 construction과 마찬가지로, $f_k=u_{i_k}$로 두고 $A[\x_1,\ldots, \x_n]$에서 계산한 그 minor를 $\Delta$라 하자. 그럼 $\Delta$를 $\kappa(s)$로 내린 것이 $x$에서 영이 아니므로 $\Delta(x)\neq 0$이다. 이제 $X'=\Spec\bigl(A[\x_1,\ldots, \x_n]/(f_1,\ldots, f_c)\bigr)$이라 하면 $(f_1,\ldots, f_c)\subseteq \mathfrak{a}$이므로 $X$는 $X'$의 closed subscheme이고, 그 ideal sheaf $\mathcal{I}$는 $u_1,\ldots, u_m$의 image로 생성되어 finite type이다. 우리는 $\mathcal{I}_x=0$을 보인다.

$\mathcal{O}_{S,s}$-module의 exact sequence

$$0 \rightarrow \mathcal{I}_x \rightarrow \mathcal{O}_{X',x} \rightarrow \mathcal{O}_{X,x} \rightarrow 0$$

을 생각하자. $\varphi$가 flat하므로 $\mathcal{O}_{X,x}$는 flat $\mathcal{O}_{S,s}$-module이고 ([§평탄사상, ⁋정의 1](/ko/math/scheme_theory/flat_morphisms#def1)), 특히 $\mathfrak{m}_s\otimes_{\mathcal{O}_{S,s}}\mathcal{O}_{X,x} \rightarrow \mathcal{O}_{X,x}$가 단사여서 [\[가환대수학\] §평탄성, ⁋명제 1](/ko/math/commutative_algebra/flatness#prop1)에 의하여 $\Tor_1^{\mathcal{O}_{S,s}}(\kappa(s), \mathcal{O}_{X,x})=0$이다. 따라서 위 sequence에 $-\otimes_{\mathcal{O}_{S,s}}\kappa(s)$를 적용한 것 또한 왼쪽에서 exact이며, 특히 $\mathcal{I}_x/\mathfrak{m}_s\mathcal{I}_x$는 $\mathcal{O}_{X'_s,x} \rightarrow \mathcal{O}_{X_s,x}$의 kernel과 같다. 그런데 [보조정리 5](#lem5)에 의해 $x$ 근방에서는 $X_s=X'_s$이므로 이 kernel은 영이고, 따라서 $\mathcal{I}_x=\mathfrak{m}_s\mathcal{I}_x$이다. 이제 $\mathfrak{m}_s\mathcal{O}_{X',x}\subseteq\mathfrak{m}_x$이고 $\mathcal{I}_x$가 finitely generated이므로, [\[가환대수학\] §정수적 확장, ⁋보조정리 8](/ko/math/commutative_algebra/integral_extension#lem8)에 의하여 $\mathcal{I}_x=0$이다. 그럼 $\mathcal{I}$가 finite type이므로 $\mathcal{I}$는 $x$의 어떤 열린근방 위에서 소멸하고, 그 근방 안의 principal open $D(g_1)$을 택하면 $X$와 $X'$은 $D(g_1)$ 위에서 일치한다. $g=\Delta g_1$으로 두면 원하는 표현을 얻는다.
:::

이제 [명제 3](#prop3)의 역방향이 따라나오며, 이로써 cotangent sheaf에 의한 smooth morphism의 characterization이 완성된다.

::: 정리 7
Locally of finite presentation인 morphism $\varphi:X \rightarrow S$에 대하여 다음이 동치이다.

1. $\varphi$는 smooth하다.
2. $\varphi$는 flat하고, $\Omega_{X/S}$는 locally free sheaf이며, 각 $x\in X$에서 그 rank가 $s=\varphi(x)$ 위 fiber의 local dimension $\dim_xX_s$와 같다.
:::
::: 증명
두 번째 조건에서 첫 번째 조건이 따라나오는 것이 [명제 3](#prop3)이다.

역으로 $\varphi$가 smooth하다 하자. Flatness는 이미 [정의 1](#def1)에 들어 있다. 점 $x\in X$와 $s=\varphi(x)$를 고정하면, [정리 6](#thm6)에 의하여 $x$의 어떤 열린근방 위에서 $X$는 $A[\x_1,\ldots, \x_n]/(f_1,\ldots, f_c)$의 localization이고 Jacobian의 어떤 $c\times c$ minor가 그 위에서 가역이며 $c=n-\dim_xX_s$이다. 그럼 [정리 4](#thm4)의 증명에서 conormal exact sequence로부터 locally free임을 얻은 논증이 그대로 적용되어, 그 근방 위에서 $\Omega_{X/S}$는 rank $n-c$의 locally free sheaf이다. 곧 그 rank는 $\dim_xX_s$이다.
:::

한편, [정리 4](#thm4)의 증명에서 실제로 쓰인 것은 conormal exact sequence의 왼쪽 morphism이 단사라는 것을 넘어 split injection이 된다는 사실이었다. 이 성질은 택한 방정식 표현에 딸린 우연이 아니라 smoothness 자체와 동치이다.

::: 명제 8
$S=\Spec A$ 위의 closed embedding $X\hookrightarrow \mathbb{A}^n_S$이 주어졌다 하고, $B=A[\x_1,\ldots, \x_n]$, 그 defining ideal을 $\mathfrak{a}\subseteq B$, $C=B/\mathfrak{a}$라 하자. 그럼 $\varphi:X \rightarrow S$가 smooth한 것은 conormal exact sequence가 ([§미분과 여접층, ⁋명제 2](/ko/math/scheme_theory/sheaf_of_differentials#prop2)) 왼쪽에서도 exact이며 split되는 것, 곧

$$0 \longrightarrow \mathfrak{a}/\mathfrak{a}^2 \overset{\bar{d}}{\longrightarrow} \Omega_{B/A}\otimes_BC \longrightarrow \Omega_{C/A} \longrightarrow 0$$

이 split short exact sequence인 것과 동치이다. 이 때 $\mathfrak{a}/\mathfrak{a}^2$과 $\Omega_{C/A}$는 모두 finitely generated projective $C$-module이다.
:::
::: 증명
먼저 $\varphi$가 smooth하다 하자. [정리 7](#thm7)에 의하여 $\Omega_{C/A}$는 locally free이고 finitely presented이므로 projective $C$-module이며, 따라서 오른쪽 surjection은 split된다. 남은 것은 $\bar{d}$가 단사라는 것이다. 이를 위해 우선 위의 split으로부터 $\Omega_{B/A}\otimes_BC\cong \Omega_{C/A}\oplus \im\bar{d}$이므로 $\im\bar{d}$가 free module의 direct summand로서 projective이고, 따라서 surjection $\mathfrak{a}/\mathfrak{a}^2 \rightarrow \im\bar{d}$ 또한 split되어

$$\mathfrak{a}/\mathfrak{a}^2\cong\ker\bar{d}\oplus\im\bar{d}$$

가 성립함을 관찰한다. 이제 한 점 $x\in X$와 $s=\varphi(x)$, $d=\dim_xX_s$를 고정하고, $x$에 대응하는 prime을 $\mathfrak{q}\subseteq C$, 그 $B$에서의 preimage를 $\mathfrak{p}$라 하자. [정리 7](#thm7)에 의하여 $\Omega_{C/A}$의 $x$에서의 rank가 $d$이므로 $\im\bar{d}\otimes_C\kappa(x)$의 차원은 $n-d$이고, 한편 $\mathfrak{a}\subseteq\mathfrak{p}$에서 $\mathfrak{a}^2\subseteq\mathfrak{p}\mathfrak{a}$이므로 $(\mathfrak{a}/\mathfrak{a}^2)\otimes_C\kappa(x)=\mathfrak{a}\otimes_B\kappa(x)$이다. 따라서 위의 분해를 $\kappa(x)$로 내리면

$$\dim_{\kappa(x)}\mathfrak{a}\otimes_B\kappa(x)=\dim_{\kappa(x)}\ker\bar{d}\otimes_C\kappa(x)+(n-d)$$

를 얻는다. 좌변은 fiber에서 계산된다. $\varphi$가 flat하여 $C$가 flat $A$-module이므로 $\Tor_1^A(C, \kappa(s))=0$이고, 따라서 $0 \rightarrow \mathfrak{a} \rightarrow B \rightarrow C \rightarrow 0$에 $-\otimes_A\kappa(s)$를 적용한 것은 왼쪽에서도 exact이다. $B$가 $A$ 위에서 free라 $B\otimes_A\kappa(s)=\kappa(s)[\x_1,\ldots, \x_n]$이므로, 이는 $\mathfrak{a}\otimes_A\kappa(s)$가 그 안에서 fiber $X_s$를 정의하는 ideal $\overline{\mathfrak{a}}$와 같음을 뜻한다. 따라서 $\mathfrak{a}\otimes_B\kappa(x)=\overline{\mathfrak{a}}\otimes\kappa(x)$이며, $\varphi$가 smooth하여 geometric fiber가 regular이므로 [보조정리 5](#lem5)에 의하여 $\overline{\mathfrak{a}}$는 $x$ 근방에서 $n-d$개의 원소로 생성된다. 곧 좌변은 $n-d$ 이하이고, 위의 등식에 의하여 $\ker\bar{d}\otimes_C\kappa(x)=0$이다. $\varphi$가 locally of finite presentation이라 $\mathfrak{a}$가 finitely generated이므로 $\ker\bar{d}$ 또한 finitely generated이고, [\[가환대수학\] §정수적 확장, ⁋보조정리 8](/ko/math/commutative_algebra/integral_extension#lem8)에 의하여 $(\ker\bar{d})_\mathfrak{q}=0$이다. $x$가 임의였으므로 $\bar{d}$는 단사이다.

역으로 위의 sequence가 split short exact이라 하자. 그럼 $\mathfrak{a}/\mathfrak{a}^2$과 $\Omega_{C/A}$는 모두 rank $n$의 free module $\Omega_{B/A}\otimes_BC$의 direct summand이므로 finitely generated projective이다. 한 점 $x\in X$에 대응하는 prime을 $\mathfrak{q}\subseteq C$, 그 preimage를 $\mathfrak{p}\subseteq B$라 하고 free module $(\mathfrak{a}/\mathfrak{a}^2)_{\mathfrak{q}}$의 rank를 $c$라 하자. 그 기저를 $\mathfrak{a}$의 원소들 $f_1,\ldots, f_c$의 class로 택하면 $\mathfrak{a}_{\mathfrak{p}}=(f_1,\ldots, f_c)_{\mathfrak{p}}+\mathfrak{a}_{\mathfrak{p}}^2$이고, $\varphi$가 locally of finite presentation이라 $\mathfrak{a}$가 finitely generated이므로 [\[가환대수학\] §정수적 확장, ⁋보조정리 8](/ko/math/commutative_algebra/integral_extension#lem8)에 의하여 $\mathfrak{a}_{\mathfrak{p}}=(f_1,\ldots, f_c)_{\mathfrak{p}}$이다. 그럼 어떤 $g\notin\mathfrak{p}$에 대하여 $\mathfrak{a}_g=(f_1,\ldots, f_c)_g$이므로, $X$는 $x$의 근방에서 $X'=\Spec\bigl(B/(f_1,\ldots, f_c)\bigr)$과 open subscheme으로서 일치한다. 한편 split injection은 임의의 base change 뒤에도 단사이므로 $\bar{d}\otimes\kappa(x)$가 단사이고, 이를 기저 $\bar{f}_1,\ldots, \bar{f}_c$와 $\dd{\x_1},\ldots, \dd{\x_n}$에 대하여 표현한 행렬이 $x$에서 계산한 Jacobian $(\partial f_i/\partial \x_j)$의 transpose이므로 그 rank는 $c$이다. 따라서 [정리 4](#thm4)에 의하여 $X' \rightarrow S$는 $x$의 어떤 근방에서 smooth하고, 그 근방에서 $X$와 $X'$이 일치하므로 $\varphi$는 $x$에서 smooth하다. $x$가 임의였으므로 $\varphi$는 smooth하다.
:::

Affine 위에서는 언제나 이러한 closed embedding을 택할 수 있고 smoothness는 국소적인 성질이므로, 위의 판정은 임의의 $\varphi$에 대하여 국소적으로 적용된다. 한편 $\bar{d}$의 단사성만으로는 smooth가 되지 않는다. 가령 $C=\mathbb{K}[\x,\y]/(\x\y)$에서 $\mathfrak{a}=(\x\y)$는 nonzerodivisor로 생성되어 $\mathfrak{a}/\mathfrak{a}^2$가 rank $1$의 free module이고 $\bar{d}(\overline{\x\y})=\y \dd{\x}+\x \dd{\y}$를 죽이는 원소는 $(\x)\cap(\y)=0$에 속하므로 $\bar{d}$는 단사이다. 그러나 원점에서 $\bar{d}$를 residue field로 내린 것은 영이 되어 그 image가 direct summand를 이루지 못하며, 실제로 $X$는 원점에서 singular하다.

이렇듯 smoothness의 실패는 $\bar{d}$가 단사이지 않은 경우와, 단사이더라도 그 image가 direct summand가 되지 않는 경우로 나뉜다. 전자는 $H_1(\operatorname{NL}_{C/A})=\ker\bar{d}$가 기록하고, 후자는 $\Omega_{C/A}$의 projectivity가 실패하는 것으로 나타난다. 두 조건을 함께 담도록 $\Omega$를 왼쪽으로 연장한 것이 naive cotangent complex이며, 이를 모든 degree로 확장한 것이 cotangent complex이다.

## 비분기 사상

[정리 4](#thm4)에서 Jacobian의 rank가 full rank라는 조건은 $f_1,\ldots, f_r$이 정의하는 morphism $\mathbb{A}^n_S \rightarrow \mathbb{A}^r_S$의 미분이 fiber 방향에서 surjective라는 것으로, [\[미분다양체\] §음함수 정리, ⁋따름정리 4](/ko/math/manifolds/implicit_function_theorem#cor4)에서는 어떠한 함수의 level set이 이러한 점들로 이루어져 있다면 그것이 codimension $r$의 embedded submanifold를 이뤘던 것을 생각하면 [정리 4](#thm4)는 이 사실을 base 방향으로 parametrize한 것으로 생각할 수 있다. 따라서 직관적으로 smooth morphism은 submersion의 대수적인 대응물이라 생각할 수 있다. 이와 유사하게 immersion의 대수적 대응물을 생각할 수 있으며, 이는 *unramified morphism*이라 부른다. 미분기하학에서 immersion은 그 differential이 injective인 smooth map으로 주어지므로, 대수적 언어에서 이는 $\Omega_{X/S}$가 $0$이 된다는 것으로 번역된다. 따라서 unramified morphism은 fiber 방향으로 움직일 수 있는 무한소 방향이 없는 morphism으로 생각할 수 있다.

::: 정의 9
Locally of finite presentation인 scheme morphism $\varphi:X \rightarrow S$가 *unramified<sub>비분기</sub>*하다는 것은 $\Omega_{X/S}=0$인 것이다.
:::

정의에 의해 이 조건은 affine chart 위에서 곧바로 계산할 수 있다. ([§미분과 여접층, ⁋정의 4](/ko/math/scheme_theory/sheaf_of_differentials#def4)) 특히 $S=\Spec A$, $X=\Spec B$이면 $\Omega_{X/S}=\widetilde{\Omega_{B/A}}$이므로, $\varphi$가 unramified한 것은 Kähler differential module $\Omega_{B/A}$가 영인 것과 동치이다. 표준적인 예시는 finite degree separable field extension ([\[체론\] §분리가능확대체, ⁋정의 8](/ko/math/field_theory/separable_extensions#def8)) $\mathbb{K} \subseteq \mathbb{L}$으로, 정의에 의해 $\Omega_{\mathbb{L}/\mathbb{K}}=0$이므로 $\Spec \mathbb{L} \rightarrow \Spec \mathbb{K}$는 unramified하다. 같은 맥락에서 표준적인 반례 또한 나오는데, characteristic $p$ field 위에서 정의된 inseparable extension $\mathbb{L}=\mathbb{K}(\t^{1/p})$을 생각하면 $\Omega_{\mathbb{L}/\mathbb{K}}\neq 0$을 주어 unramified하지 않다. ([\[체론\] §분리가능확대체, ⁋예시 4](/ko/math/field_theory/separable_extensions#ex4)) 이 예시를 보면 위에서 설명한 unramified morphism의 직관이 더 잘 드러나는데, 이 inseparable extension에서 $\Spec\mathbb{L}$는 위상적으로 한 점이지만, geometric base change 뒤에는 nontrivial thickening이 남아 있으므로 무한소 방향이 사라지지 않아 unramified하지 않게 되는 것이다.

이 조건은 diagonal morphism을 통해 좌표에 의존하지 않고 표현할 수 있는데, cotangent sheaf 자체가 diagonal의 conormal로 정의되므로, 그 소멸은 diagonal이 open subscheme이 되는 것과 직접 연결된다.

::: 명제 10
Locally of finite presentation인 morphism $\varphi:X \rightarrow S$에 대하여 다음이 동치이다.

1. $\varphi$는 unramified하다.
2. Diagonal morphism $\Delta_\varphi:X \rightarrow X\times_SX$이 open embedding이다.
:::
::: 증명

우선 $\varphi$가 unramified morphism이라 가정하자. 일반적으로 $\Delta_\varphi$는 항상 어떤 open subscheme 위로의 closed embedding이므로, 따라서 $\Delta_\varphi$가 open embedding인 것은 그 closed embedding 성분이 isomorphism이 되어 그 image의 ideal sheaf $\mathcal{I}$가 영인 것과 동치이다. 문제가 affine 위에서 국소적이므로 $S=\Spec A$, $X=\Spec B$로 두자. 그럼 $X\times_SX=\Spec(B\otimes_AB)$이고 $\Delta_\varphi$는 multiplication $\mu:B\otimes_AB \rightarrow B$로부터 온다. $\mathfrak{a}=\ker\mu$라 하면 $\mathfrak{a}/\mathfrak{a}^2\cong \Omega_{B/A}$이므로 ([§미분과 여접층, ⁋명제 6](/ko/math/scheme_theory/sheaf_of_differentials#prop6)의 증명), unramified 가정 하에서 $\mathfrak{a}=\mathfrak{a}^2$이 성립한다. 한편 $B$가 $A$ 위에서 finite presentation이므로 $B\otimes_AB$ 위에서 $\mathfrak{a}$는 finitely generated이고, 이제 [\[가환대수학\] §정수적 확장, ⁋보조정리 8](/ko/math/commutative_algebra/integral_extension#lem8)에 의하여 $\mathfrak{a}=\mathfrak{a}^2$이면 어떤 $e\in \mathfrak{a}$가 존재하여 $e^2=e$이고 $\mathfrak{a}=(e)$이도록 할 수 있다. 그럼 $1-e$가 $\mu$의 image를 trivialize하는 idempotent가 되어, $\Delta_\varphi$의 image는 $D(1-e)$ 위에 clopen인 subscheme으로 실현된다. 따라서 $\Delta_\varphi$는 open embedding이다.

역으로 $\Delta_\varphi$가 open embedding이라 하자. 같은 affine 상황에서 $\mathfrak{a}$를 포함하는 prime $\mathfrak{P}$를 잡으면, closed embedding이 주는 surjection $(B\otimes_AB)_\mathfrak{P} \rightarrow \bigl((B\otimes_AB)/\mathfrak{a}\bigr)_\mathfrak{P}$이 동시에 open embedding이 주는 isomorphism이므로 $\mathfrak{a}_\mathfrak{P}=0$이고, $\mathfrak{a}$를 포함하지 않는 prime에서는 $\mathfrak{a}_\mathfrak{P}$가 전체가 되어 어느 쪽이든 $(\mathfrak{a}/\mathfrak{a}^2)_\mathfrak{P}=0$이다. 따라서 $\mathfrak{a}/\mathfrak{a}^2=0$, 곧 $\Omega_{B/A}=0$이고 $\varphi$는 unramified하다.
:::

한 점 $x\in X$와 $s=\varphi(x)$에 대하여 fiber $X_s=X\times_S\Spec\kappa(s)$를 생각하자. Cotangent sheaf는 base change와 commute하므로 $\Omega_{X_s/\kappa(s)}$는 $\Omega_{X/S}$의 $X_s$ 위 pullback이며, unramified 가정에 의해 영이다. 따라서 fiber morphism $X_s\rightarrow\Spec\kappa(s)$ 또한 unramified하다. Field 위에서 locally of finite presentation인 unramified morphism의 점들은 finite separable residue field extension을 가지는 isolated point들이므로, $x$는 $\kappa(s)$의 finite separable extension $\kappa(x)$를 residue field로 가지는 isolated point가 된다.

## 에탈 사상

미분기하에서 fiber가 이산적인 submersion, 곧 relative dimension $0$의 submersion은 local diffeomorphism을 정의했었다. ([\[미분다양체\] §부분다양체와 역함수 정리, ⁋정리 4](/ko/math/manifolds/submanifolds#thm4)) 그럼 이 대수적 대응물은 smoothness와 unramified 조건을 동시에 요구하여 얻어지는 것이다.

::: 정의 11
Locally of finite presentation인 morphism $\varphi:X \rightarrow S$가 *étale<sub>에탈</sub>*하다는 것은 $\varphi$가 smooth하면서 unramified한 것이다.
:::

Smooth morphism에서 $\Omega_{X/S}$는 relative dimension만큼의 rank를 가지는 locally free sheaf이고 ([정리 7](#thm7)), unramified morphism에서는 $\Omega_{X/S}=0$이므로 ([정의 9](#def9)), 두 조건이 함께 성립하면 relative dimension이 $0$이다. 따라서 étale morphism은 relative dimension $0$의 smooth morphism이며, 동치로 다음과 같이 특징지어진다.

::: 명제 12
Locally of finite presentation인 morphism $\varphi:X \rightarrow S$에 대하여 다음이 동치이다.

1. $\varphi$는 étale하다.
2. $\varphi$는 flat하고 unramified하다.
:::
::: 증명
첫째 조건이 둘째 조건을 함의하는 것은 자명하므로 그 역만 보이면 충분하다. 즉 $\varphi$가 flat하고 unramified하다 가정하고, 그 geometric fiber가 regular임을 보이자.

우선 unramified 가정에 의하여 $\Omega_{X/S}=0$이고, 따라서 위에서 살펴봤듯 임의의 geometric fiber $X_{\overline{s}}$ 위에서도 $\Omega_{X_{\overline{s}}/\mathbb{K}}=0$이 성립한다. 이제 $X_{\overline{s}}$는 algebraically closed field $\mathbb{K}=\overline{\kappa(s)}$ 위에서 locally of finite presentation이므로 그 closed point $z$는 $\mathbb{K}$-point이고, 따라서 $\mathfrak{m}_z/\mathfrak{m}_z^2\cong\Omega_{X_{\overline{s}}/\mathbb{K}}\otimes\kappa(z)=0$이다. 그럼 [\[가환대수학\] §정수적 확장, ⁋보조정리 8](/ko/math/commutative_algebra/integral_extension#lem8)에 의하여 $\mathfrak{m}_z=0$이므로 $\mathcal{O}_{X_{\overline{s}},z}=\mathbb{K}$는 field이다. 한편 $z$를 담는 $X_{\overline{s}}$의 affine open neighborhood $U$를 택하면 $U$는 Noetherian이고, $\mathcal{O}_{U,z}$ 역시 field이므로 $z$를 담는 irreducible component는 $\{z\}$ 하나뿐이다. $U$의 다른 irreducible component들은 유한히 많으므로 $\{z\}$는 $U$에서, 따라서 $X_{\overline{s}}$에서 열린집합이다. 한편 [명제 3](#prop3)의 증명에서 우리는 공집합이 아닌 닫힌집합은 언제나 closed point를 담는다는 것을 확인했으므로, fiber의 모든 점이 closed point여야 한다. 즉 $X_{\overline{s}}$는 $\Spec\mathbb{K}$들의 disjoint union이며, 이는 local dimension이 $0$인 reduced scheme이라 regular이다. 그러므로 $\varphi$는 flat하고 geometric fiber가 regular이므로 smooth하며, $\Omega_{X/S}=0$이므로 unramified, 곧 étale하다.
:::

우리는 이전 절에서 unramified morphism이 $0$차원의 fiber방향을 갖는다고 주장했는데, 위의 증명에서의 계산이 이를 뒷받침한다. 한편 [정리 6](#thm6)과 같이, étale morphism 또한 다음과 같은 표준형을 갖는다.

::: 정리 13
Locally of finite presentation인 morphism $\varphi:X\rightarrow S$에 대하여, $\varphi$가 étale한 것은 임의의 $x\in X$에 대하여 $x$를 포함하는 $X$의 affine open set과 $\varphi(x)$를 포함하는 $S$의 affine open set 위에서 $\varphi$를 다음 꼴의 *standard étale* morphism의 형태로 쓸 수 있는 것과 동치이다.

$$\Spec\bigl((A[\t]/(f))_g\bigr)\longrightarrow\Spec A$$

여기서 $f\in A[\t]$는 monic이고 $g\in A[\t]/(f)$이며, $f'$의 image는 $(A[\t]/(f))_g$에서 가역이다.
:::

하지만 [정리 6](#thm6)의 증명과 달리 이 명제의 증명은 다소 기술적이므로 우리는 생략하기로 한다. 또 다른 중요한 것은, 여기의 도함수 조건이 $f=0$이 중근을 가지지 않는다는 분리가능성의 대수적 표현이라는 것으로, 이로부터 위의 inseparable 예시가 étale morphism이 아니라는 것을 알 수 있다.

::: 예시 14
위에서 살펴봤듯, finite separable field extension $\mathbb{K}\subseteq\mathbb{L}$에 대하여 $\Spec\mathbb{L}\rightarrow\Spec\mathbb{K}$는 étale이다. Primitive element theorem에 의하여 $\mathbb{L}=\mathbb{K}[\t]/(f)$로 쓸 수 있고, $f$가 separable이므로 $f'$는 $\mathbb{L}$에서 가역이기 때문이다. ([\[체론\] §분리가능확대체, ⁋정의 8](/ko/math/field_theory/separable_extensions#def8)) 반면 $\mathbb{K}=\mathbb{F}_p(\t)$와 $\mathbb{L}=\mathbb{F}_p(\t^{1/p})$의 inseparable extension은 étale morphism이 아니다. 여기서 추가되는 원소 $u=\t^{1/p}$의 minimal polynomial은 $\x^p-\t$인데, 이를 미분하면 $0$이 되어 가역이 될 수 없기 때문이다.

두 상황 모두 $\Spec \mathbb{L}\rightarrow \Spec \mathbb{K}$는 한 점에서 한 점으로 가는 morphism이지만, 이를 geometric fiber로 옮겨오면 사정이 전혀 다르다. 첫째 경우에는 $f$가 서로 다른 일차식들의 곱으로 완전히 분리되어 geometric fiber가 이들 근들로 분해되는 반면, 둘째 경우는 $\mathbb{K}$의 algebraic closure에서 $f$가 $(\x-u)^p$로 인수분해되어 근들이 중근으로 뭉쳐있기 때문이다. 이를 통해 우리는 앞서 nontrivial thickening 때문에 unramified 조건이 실패한다는 직관을 다시 확인할 수 있다.
:::

## Infinitesimal lifting criterion

이제 우리는 이들 개념의 *infinitesimal lifting criterion*을 살펴본다. 개념적으로 이는 [§값매김환](/ko/math/scheme_theory/valuative_criteria)에서 다룬 separatedness와 properness의 valuative criterion과 같은 구조이다. 어떠한 morphism의 separatedness와 properness를 보기 위해 우리는 우선 discrete valuation ring $A$와 fraction field $K$가 만드는 $\Spec K\rightarrow\Spec A$를 test diagram으로 삼았다. 직관적으로 $\Spec K$는 중심점을 잃은 곡선의 germ이고, $\Spec A$는 이 중심점과 germ 데이터를 모두 갖고 있는 대상으로 $\Spec K\rightarrow X$를 $\Spec A\rightarrow X$로 연장하는 것은 곧 그 빠진 중심을 채우는 것과 같았다.

비슷하게 smoothness와 unramifiedness의 경우 (그리고 따라서 étaleness의 경우)에도 이와 같은 식의 characterization이 존재한다. 이에 대한 기하적 직관은 [\[미분다양체\] §음함수 정리, ⁋정리 3](/ko/math/manifolds/implicit_function_theorem#thm3)로부터 오는 것으로, 이 정리의 주장은 $F:\mathbb{R}^{m-n}_s\times\mathbb{R}^n_r\rightarrow\mathbb{R}^n$의 zero set은 $r$ 방향 Jacobian이 invertible인 점 근방에서 $r=g(s)$의 graph와 locally diffeomorphic하다는 것이다. 만일 $S=\mathbb{R}^{m-n}$와 $X=F^{-1}(0)$로 두면 $X\rightarrow S$는 이 graph에서 첫째 인자로 가는 projection이며, $X$ 자체가 국소적으로 $S$ 위의 graph가 된다.

직관적으로 음함수 정리는 $F(s_0,r_0)=0$인 해에서 $s_0$를 조금 움직여 $s=s_0+\epsilon$으로 바꾸더라도 $F(s,r)=0$을 유지하도록 $r$를 유일하게 보정할 수 있다는 주장으로, 이 보정 규칙이 곧 함수 $r=g(s)$을 정의하는 것이다. 이를 작동하게 하는 두 가지 가정을 분리해서 보는 것이 도움이 되는데, 우선 임의의 가까운 $s$에 대하여 보정된 $r$가 <em-ko>존재한다</em-ko>는 것은 graph에서 첫째 인자로 가는 projection이 submersion이라는 것이고, 그 $r$가 <em-ko>유일하다</em-ko>는 것은 이 projection이 immersion이라는 것이다. 우리 상황에서는 smoothness가 submersion에, unramified morphism이 immersion에 대응되는 개념이므로 이 characterization은 적당한 test scheme을 이용하여 정의되는 lifting의 존재성과 유일성을 각각 줄 것이다.

이제 이에 대응하는 test scheme은 이러한 first-order deformation을 담는 대상이어야 한다. Closed embedding $T_0\hookrightarrow T$의 defining ideal $\mathcal{J}$가 $\mathcal{J}^2=0$을 만족할 때 이를 *square-zero extension<sub>제곱영 확대</sub>*이라 부른다. 가장 기본적인 예는 field $\mathbb{K}$에 대한

$$\Spec\mathbb{K}\hookrightarrow\Spec\mathbb{K}[\epsilon]/(\epsilon^2)$$

이다. Ring 단계에서 이는 $a+b\epsilon\mapsto a$로 정의되는 ring homomorphism으로부터 오는 것이다. 두 scheme은 underlying topological space로는 모두 한 점이지만, 오른쪽에는 $\mathbb{K}$에 $\varepsilon$ 방향의 first-order infinitesimal thickening이 추가된 대상이며, 이것이 일차항의 정보만을 담고 있는 것은 $\epsilon^2=0$이기 때문이다. 비슷하게, 위의 일반적인 정의에서 대수적으로 $T=\Spec R$, $T_0=\Spec R_0$라 하면 이는 surjection $R\rightarrow R_0$의 kernel $\mathfrak{b}$가 $\mathfrak{b}^2=0$을 만족하는 상황으로 번역되며, 특히 이 조건 때문에 $\mathfrak{b}$ 안의 두 보정항을 곱한 second-order term은 모두 사라진다.

예를 들어 $\ch \mathbb{K}\neq 2$라 하고, 위의 $\Spec \mathbb{K}\hookrightarrow \Spec \mathbb{K}[\epsilon]/(\epsilon^2)$을 test scheme $T_0\rightarrow T$로 삼고,
$S=\Spec \mathbb{K}[\y]$-scheme $X=\mathbb{A}^2_\mathbb{K}$가 주어졌다 하자. 우리가 도입할 criterion은 다음의 diagram

{% diagram Math/Scheme_Theory/Smooth_and_Etale_Morphisms-4.svg width="14.67em" alt="concrete lifting" %}

의 꼴이다. 여기서 등장하는 scheme이 모두 affine이므로 이 diagram은 arrow를 뒤집어 $\mathbb{K}$-algebra homomorphism들의 diagram

{% diagram Math/Scheme_Theory/Smooth_and_Etale_Morphisms-5.svg width="11.90em" alt="ring level lifting" %}

에서 오는 것이며, 이들 사이의 ring homomorphism을 통해 scheme morphism들을 정의할 수 있다. $\mathbb{K}[\epsilon]/(\epsilon^2)\rightarrow \mathbb{K}$는 위에서 살펴본 것과 같은 것이며, 나머지는

$$\mathbb{K}[\y]\rightarrow \mathbb{K}[\x_1,\x_2];\quad \y\mapsto \x_1^2+\x_2^2,\qquad \mathbb{K}[\x_1,\x_2]\rightarrow \mathbb{K};\quad \x_i\mapsto a_i,\qquad \mathbb{K}[\y]\rightarrow \mathbb{K}[\epsilon]/(\epsilon^2); \quad \y\mapsto y_0+c\epsilon$$

으로 정의되는 것이다. 이 때 diagram의 commutativity를 위하여 상수 $y_0, a_1, a_2$는 식 $y_0=a_1^2+a_2^2$을 만족하여야 한다.

이제 위의 $\varphi:\mathbb{A}^2_\mathbb{K}\rightarrow\mathbb{A}^1_\mathbb{K}$에 대하여,

$$F(\y,\x_1,\x_2)=\x_1^2+\x_2^2-\y$$

로 두면 $(\id_X,\varphi)$가 주는 graph는 $X$를 $\mathbb{A}^2_S=S\times_\mathbb{K} \mathbb{A}_\mathbb{K}^2$ 안의 zero set $Z(F)$와 identify하고, 이 identification 아래에서 $\varphi$는 첫째 factor로의 projection $Z(F)\rightarrow S$이 된다. 그럼 우리가 원하는 형태의 음함수 정리는 $Z(F)$의 한 점 $\varrho_0:\Spec \mathbb{K}\rightarrow Z(F)$, 즉 $(y_0, a_1, a_2)$에서 $y_0+c\epsilon$으로 first-order deformation을 줬을 때 여전히 $Z(F)$에 머물도록 하는 규칙을 찾는 것이 된다. 이것이 바로 lifting $\varrho:T\rightarrow X$의 문제이며, ring 단계에서는 $\x_i$를

$$\x_i\mapsto a_i+b_i\epsilon$$

으로 보내는 map을 찾는 일이다. 앞에서 정한 $\y\mapsto y_0+c\epsilon$와 함께 이는 우선 $S$ 위의 ambient space $\mathbb{A}^2_S$로 가는 $T$-point를 정의한다. 이것이 lifting이 된다는 조건이 바로 음함수정리가 요구하던, closed subscheme $Z(F)\cong X$를 통해 factor한다는 조건으로, 이를 위해서는 다음의 식

$$F(y_0+c\epsilon,a_1+b_1\epsilon,a_2+b_2\epsilon)=0$$

이 성립해야 한다. 우리 가정에서 $\epsilon^2=0$이고 $y_0=a_1^2+a_2^2$이므로, 이는

$$2a_1b_1+2a_2b_2=c$$

와 동치이며, $a_1\neq 0$이거나 $a_2\neq 0$인 곳에서는 실제로 이를 풀어 그 lifting을 구할 수 있다. 반면 $(a_1,a_2)=(0,0)$에서는 위 linear equation이 $0=c$가 되어 $c\neq0$인 base 변화는 lift할 수 없으며, 이것이 이 점에서 fiber $\x_1^2+\x_2^2=0$가 singular하다는 사실을 반영하는 것이다.

지금까지의 논의를 일반적인 세팅에서 적으면 다음의 criterion을 얻는다.

::: 정리 15 (Infinitesimal lifting criterion)
Locally of finite presentation인 morphism $\varphi:X \rightarrow S$가 주어졌다 하자. 임의의 affine $S$-scheme $T$와 그 안의 square-zero closed subscheme $T_0\hookrightarrow T$, 그리고 $S$-morphism $\varrho_0:T_0 \rightarrow X$에 대하여, 다음 diagram

{% diagram Math/Scheme_Theory/Smooth_and_Etale_Morphisms-6.svg width="6.05em" alt="lifting diagram" %}

을 생각하자.

1. $\varphi$가 smooth한 것은 모든 그러한 $(T_0, T, \varrho_0)$에 대하여 lifting $\varrho$가 존재하는 것과 동치이다.
2. $\varphi$가 unramified한 것은 모든 그러한 $(T_0, T, \varrho_0)$에 대하여 lifting $\varrho$가 많아야 하나인 것과 동치이다.
3. $\varphi$가 étale한 것은 모든 그러한 $(T_0, T, \varrho_0)$에 대하여 lifting $\varrho$가 정확히 하나 존재하는 것과 동치이다.
:::
::: 증명
우선 $T=\Spec R$, $T_0=\Spec R_0$이고, quotient map을 $q:R\rightarrow R_0$, 그 kernel을 $\mathfrak{b}$라 하자. 그러면 $T_0$가 square-zero extension이라는 것으로부터 $\mathfrak{b}^2=0$이다. 한편 문제가 affine-local하므로 우리는 $S=\Spec A$, $X=\Spec C$라 할 수 있으며, 그럼 $\varrho_0$은 $A$-algebra homomorphism $\rho_0: C \rightarrow R_0$에 대응된다. 이제 만일 $\varrho$가 $\varrho_0$의 lifting이라면, 이 조건은 ring homomorphism에서는 $\rho_0=q\circ\rho$로 번역된다. 따라서 만일 $\varrho$와 $\varrho'$가 $\varrho_0$의 두 lifting이라면 다음 식

$$q\circ\rho=\rho_0=q\circ\rho'$$

이 성립해야 하고, 따라서 $D=\rho-\rho'$의 image는 $\ker q=\mathfrak{b}$에 들어간다. $\mathfrak{b}^2=0$에 의하여 $D:C\rightarrow\mathfrak{b}$는 $A$-derivation이 된다. 임의의 $c, c'\in C$에 대하여

$$D(cc')=\rho(c)\rho(c')-\rho'(c)\rho'(c')=\rho(c)D(c')+D(c)\rho'(c')\equiv \rho_0(c)D(c')+D(c)\rho_0(c')\pmod{\mathfrak{b}^2}$$

이고, $\mathfrak{b}^2=0$이므로 이는 정확히 Leibniz rule이 되기 때문이다. 따라서 두 lifting의 차이는 $\Der_A(C, \mathfrak{b})\cong \Hom_C(\Omega_{C/A}, \mathfrak{b})$의 원소들과 일대일로 대응된다.

이제 만일 $\varphi$가 unramified하면 $\Omega_{C/A}=0$이므로 $\Hom_C(\Omega_{C/A}, \mathfrak{b})=0$이고, 따라서 두 lifting의 차이가 항상 영이되어 lifting의 유일성이 얻어진다. 거꾸로 lifting이 항상 많아야 하나라면, $\Omega_{C/A}$를 square-zero ideal로 하는 trivial extension $C\oplus\Omega_{C/A}$를 정의해줄 수 있다. 이 위에서의 곱은

$$(c,\omega)(c',\omega')=(cc',c\omega'+c'\omega)$$

로 주어지며, 그럼 $T_0=\Spec C\hookrightarrow T=\Spec(C\oplus\Omega_{C/A})$가 실제로 square-zero extension이 되는 것을 확인할 수 있다. 이 때, ring map $c\mapsto(c,0)$과 $c\mapsto(c,\dd{c})$은 모두 $\id_X$의 lifting을 주며, 가정에 의해 이들이 일치하므로 universal derivation이 영이 되어야 하고 따라서 $\Omega_{C/A}=0$이 되어 unramified임을 보일 수 있다.

이제 smoothness를 보이자. 앞선 증명들에서 했던 것처럼 $C=B/\mathfrak{a}$, $B=A[\x_1,\ldots,\x_n]$로 쓰면, [\[대수적 구조\] §대수, ⁋명제 8](/ko/math/algebraic_structures/algebras#prop8)의 universal property에 의하여 $B\twoheadrightarrow C\overset{\rho_0}{\longrightarrow}R_0$를 $q$를 따라 올리는 $A$-algebra homomorphism $\widetilde{\rho}:B\rightarrow R$를 잡을 수 있다. 그럼 $(q\circ\widetilde{\rho})(\mathfrak{a})=0$이므로 그 image는 $\mathfrak{b}$에 들어가며, 더 나아가

$$\widetilde{\rho}(\mathfrak{a}^2)=\widetilde{\rho}(\mathfrak{a})^2\subseteq \mathfrak{b}^2=0$$

이므로 이는 $C$-linear map

$$\delta:\mathfrak{a}/\mathfrak{a}^2\rightarrow\mathfrak{b}$$

을 유도한다. 이 때, $\widetilde{\rho}$가 $C=B/\mathfrak{a}$를 거쳐 factor하는 것은 $\widetilde{\rho}(\mathfrak{a})=0$, 즉 $\delta=0$인 것과 동치이며, $\delta$는 이 lift가 $X$의 defining equation을 만족하지 못하는 obstruction을 기록하는 것이다. 따라서 원하는 lifting을 얻는 문제는 $\widetilde{\rho}$를 $\mathfrak{b}$-valued derivation만큼 보정하여 $\delta$를 없애는 문제로 바뀐다. Smoothness와 [명제 8](#prop8)에 의하여 conormal sequence

$$0\longrightarrow\mathfrak{a}/\mathfrak{a}^2\overset{\bar{d}}{\longrightarrow}\Omega_{B/A}\otimes_BC\longrightarrow\Omega_{C/A}\longrightarrow0$$

는 split short exact sequence이다. 따라서 $r\circ\bar{d}=\id$를 만족하는 $C$-linear retraction $r:\Omega_{B/A}\otimes_BC\rightarrow\mathfrak{a}/\mathfrak{a}^2$가 존재하며, 이를 사용하여 $h=-\delta\circ r$로 두면 $h:\Omega_{B/A}\otimes_BC\rightarrow\mathfrak{b}$는 $h\circ\bar{d}=-\delta$를 만족한다. 이제 [\[가환대수학\] §미분, ⁋보조정리 2](/ko/math/commutative_algebra/differentials#lem2)에 의하여 $h$는 $A$-derivation $d:B\rightarrow\mathfrak{b}$에 대응하고, $\widetilde{\rho}+d:B\rightarrow R$는 다시 $A$-algebra homomorphism이다. 이 map은 $\mathfrak{a}$ 위에서 $\delta+h\circ\bar{d}=0$이므로 $C$를 factor through하며, 얻어지는 $\rho:C\rightarrow R$는 $\rho_0$의 lifting이다.

역으로 모든 square-zero extension에 대하여 lifting이 존재한다고 하자. Quotient $\pi:B/\mathfrak{a}^2\twoheadrightarrow C$의 kernel은 $\mathfrak{a}/\mathfrak{a}^2$이고 그 제곱은 영이므로, $T_0=X=\Spec C\hookrightarrow T=\Spec(B/\mathfrak{a}^2)$는 square-zero extension이다. 이를 $\varrho_0=\id_X$에 적용하면, 반대방향으로 $\pi$의 $A$-algebra section $\sigma:C\rightarrow B/\mathfrak{a}^2$를 얻는다. 이제 $B\twoheadrightarrow B/\mathfrak{a}^2$와 $B\twoheadrightarrow C\overset{\sigma}{\longrightarrow}B/\mathfrak{a}^2$의 차이는 $\mathfrak{a}/\mathfrak{a}^2$-valued $A$-derivation이고 따라서 이는 $C$-linear map

$$r:\Omega_{B/A}\otimes_BC\longrightarrow\mathfrak{a}/\mathfrak{a}^2$$

을 유도한다. $f\in\mathfrak{a}$에 대하여 이 derivation의 값은 $f$의 $\mathfrak{a}/\mathfrak{a}^2$에서의 class이므로 $r\circ\bar{d}=\id_{\mathfrak{a}/\mathfrak{a}^2}$이다. 즉 conormal sequence의 왼쪽 morphism은 split injection이고, [명제 8](#prop8)에 의하여 $\varphi$는 smooth하다.
:::

세 조건은 모두 base change와 합성에 대해 안정적이다. Smooth morphism의 base change는 다시 smooth하고, smooth morphism들의 합성도 smooth하며, unramified와 étale에 대해서도 마찬가지이다. 이는 위 lifting 판정이 순수하게 morphism diagram의 성질로 표현되어 있어 base change와 합성 아래에서 그대로 보존되기 때문이다.

한편, 위 증명에서 보았듯 cotangent sheaf는 두 lift의 차이, 곧 유일성을 직접 측정하지만, 반면 lifting의 존재에는 conormal sequence의 splitting이 필요하며, 이렇게 더 일반적인 obstruction을 체계적으로 기록하는 대상이 cotangent complex의 개념이 된다.

---

**참고문헌**

**[Har]** R. Hartshorne, *Algebraic geometry*. Graduate Texts in Mathematics. Springer, 1977.  
**[Vak]** R. Vakil, *The rising sea: Foundations of algebraic geometry*. Available [online](https://math.stanford.edu/~vakil/216blog/).
