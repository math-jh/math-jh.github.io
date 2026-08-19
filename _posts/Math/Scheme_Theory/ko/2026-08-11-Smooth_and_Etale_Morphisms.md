---
title: "매끄러운 사상과 에탈 사상"
description: "스킴 사상의 매끄러움을 flat이면서 모든 기하적 올이 정칙인 finitely presented 사상으로 정의하고, cotangent sheaf가 relative dimension만큼의 locally free sheaf임과 동치임을 본다. 이 동치의 어려운 방향은 매끄러운 사상이 국소적으로 Jacobian이 최대 rank인 방정식들로 잘린다는 국소 구조 정리를 거쳐 증명한다. Unramified 사상을 대각선이 open immersion인 경우로 특징짓고, étale morphism을 매끄럽고 unramified한 relative dimension 0의 사상으로 도입하며 standard étale 모형과 Jacobian 판정, square-zero 확대에 대한 무한소 lifting 판정을 다룬다."
excerpt: "Smooth, unramified, and étale morphisms; the Jacobian and infinitesimal lifting criteria"

categories: [Math / Scheme Theory]
permalink: /ko/math/scheme_theory/smooth_and_etale_morphisms
sidebar: 
    nav: "scheme_theory-ko"

date: 2026-08-11
weight: 21

published: false
drift_needed: true
---

우리는 본질적으로 cotangent sheaf가 주는 exact sequence들은 *right* exact이기만 하다는 것을 살펴보았다. ([§Kähler differential과 여접층, ⁋명제 6](/ko/math/scheme_theory/sheaf_of_differentials#prop6) 이후의 exact sequence들) 이러한 정보의 손실을 막기 위해서는 morphism에 특수한 조건을 부여해야 하는데, 그것이 smooth morphism의 동기이다. 반대쪽 극단은 $\Omega_{X/S}$가 통째로 소멸하는 경우로, 우리는 이를 *unramified* morphism이라 부른다. 마지막으로 우리는 smooth unramified morphism인 *étale* morphism을 정의한다. 

우리는 이 글 전체에서 morphism이 *locally of finite presentation*임을 기본 가정으로 둔다. 이는 (대부분의 관심사인) locally Noetherian base 위에서는 이것이 locally of finite type과 일치하므로 직관적으로는 이렇게 생각해도 무방하다. 

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

한편, smooth morphism은 cotangent sheaf의 local freeness로 적어줄 수도 있으며, 이것이 가장 중요한 smooth morphism의 characterization이다. 이를 위해 우선 scheme $Y$와 그 점 $y\in Y$에 대하여, $y$에서의 *local dimension<sub>국소차원</sub>* $\dim_yY$를 $y$를 포함하는 irreducible component들의 차원의 supremum으로 정의하자. 그럼 정의에 의해 $Y$의 전체 차원은 이들의 supremum이며, 만일 $Y$가 irreducible이면 모든 점이 유일한 irreducible component 위에 놓이므로 $\dim_yY=\dim Y$가 성립한다. 더 일반적으로 모든 irreducible component의 차원이 같은 *equidimensional* scheme에서도 그러하다. 이것이 성립하며, 이 개념은 새로운 것이 아니라 평면과 직선의 합집합 $Y=V(\x\z,\y\z)\subseteq\mathbb{A}^3_\mathbb{K}$에서 서로 차원이 다른 두 성분을 다루기 위한 언어일 뿐이다. 만일 $Y$가 field 위에서 finite type이면 그 closed point $z$에서는 [\[가환대수학\] §뇌터 정규화, ⁋정리 4](/ko/math/commutative_algebra/noether_normalization#thm4)에 의하여 $\dim\mathcal{O}_{Y,z}=\dim_zY$가 성립한다.

Smooth 조건 가운데 flatness를 뺀 나머지는 geometric fiber 위에서 주어져 있으므로, 이를 $X$ 위의 조건으로 옮겨 적으려면 무엇을 옮길 수 있는지 먼저 확인하여야 한다. Local ring $(\mathcal{O}_{X_{\overline{s}}, \overline{x}}, \mathfrak{m}_{\overline{x}})$이 regular라는 것은 그 정의에 의해 다음의 등식

$$\dim_{\kappa(\overline{x})}\mathfrak{m}_{\overline{x}}/\mathfrak{m}_{\overline{x}}^2=\dim \mathcal{O}_{X_{\overline{s}},\overline{x}}\tag{$\ast$}$$

이 성립하는 것이다. ([\[가환대수학\] §차원, ⁋정의 12](/ko/math/commutative_algebra/Krull_dimension#def12)) 한편 [§Kähler differential과 여접층, ⁋정의 8](/ko/math/scheme_theory/sheaf_of_differentials#def8) 직후에 우리는 $\mathbb{K}$-point $\overline{x}$에 대해서는 좌변의 $\mathfrak{m}/\mathfrak{m}^2$이 $\Omega_{X_{\overline{s}}/\mathbb{K}}\otimes\kappa(\overline{x})$임을 살펴보았으며, 우리 상황에서는 $\mathbb{K}=\overline{\kappa(s)}$가 algebraically closed이므로 임의의 closed point가 $\mathbb{K}$-point가 되어 이 전제를 만족한다. 또, 위에서 우변은 $\dim_{\overline{x}} X_{\overline{s}}$과 같음을 이미 살펴보았으므로, 우리가 원하는 것은 다음과 같은 형태의 주장이다. 

::: 보조정리 2
Locally of finite presentation인 morphism $\varphi:X \rightarrow S$와 점 $x\in X$, $s=\varphi(x)$에 대하여 $\mathbb{K}=\overline{\kappa(s)}$라 하고 geometric fiber $X_{\overline{s}}$를 생각하자. 그럼 $x$ 위의 임의의 점 $\overline{x}\in X_{\overline{s}}$에 대하여

$$\dim_{\kappa(\overline{x})}\bigl(\Omega_{X_{\overline{s}}/\mathbb{K}}\otimes \kappa(\overline{x})\bigr)=\dim_{\kappa(x)}\bigl(\Omega_{X/S}\otimes \kappa(x)\bigr),\qquad \dim_{\overline{x}}X_{\overline{s}}=\dim_xX_s$$

가 성립한다.
:::
::: 증명
Cotangent sheaf는 base change와 commute하므로 ([§Kähler differential과 여접층, ⁋명제 5](/ko/math/scheme_theory/sheaf_of_differentials#prop5)) geometric fiber가 주는 pullback diagram

{% diagram Math/Scheme_Theory/Smooth_and_Etale_Morphisms-2.svg width="8.18em" alt="pullback" %}

에서 $\Omega_{X_{\overline{s}}/\mathbb{K}}$는 $\pi$를 따라 끌어온 pullback $\pi^\ast\Omega_{X/S}$이다. 한 점에서 fiber를 취하는 것은 그 점이 정의하는 canonical morphism을 따른 pullback이고, $\overline{x}:\Spec\kappa(\overline{x}) \rightarrow X_{\overline{s}}$와 $\pi$의 합성은 $x$와 field extension $\kappa(x)\hookrightarrow \kappa(\overline{x})$가 정의하는 canonical morphism $\Spec\kappa(\overline{x}) \rightarrow \Spec\kappa(x) \rightarrow X$이므로, pullback의 functoriality에 의하여

$$\Omega_{X_{\overline{s}}/\mathbb{K}}\otimes \kappa(\overline{x})=\overline{x}^\ast\pi^\ast\Omega_{X/S}=\bigl(\Omega_{X/S}\otimes \kappa(x)\bigr)\otimes_{\kappa(x)}\kappa(\overline{x})$$

이다. 한편 우변은 $\kappa(x)$-vector space $\Omega_{X/S}\otimes \kappa(x)$을 $\kappa(\overline{x})$로 스칼라를 바꾼 것에 지나지 않으므로 차원 또한 같고, 이것이 첫 번째 등식이다.

두 번째 등식을 보인다. 우선 algebraic extension이 주는 $\Spec\mathbb{K} \rightarrow \Spec\kappa(s)$가 integral morphism이고 이는 base change에 대해 보존되는 성질이므로, $X_{\overline{s}} \rightarrow X_s$는 integral, surjective morphism이다. 그럼 $\overline{x}$를 포함하는 $X_{\overline{s}}$의 component는 그 image의 closure 위로 가는 dominant integral morphism을 주므로, [§차원, ⁋명제 5](/ko/math/scheme_theory/dimension#prop5)에 의하여 그 closure와 차원이 같고, 이 closure는 $x$를 담는 어떤 component 안에 들어가므로 $\dim_{\overline{x}}X_{\overline{s}}\leq\dim_xX_s$임은 자명하다. 반대방향을 보이기 위해 $x$를 담는 $X_s$의 component $W$를 잡으면, $\overline{x}$는 base change $W\times_{\Spec\kappa(s)}\Spec\mathbb{K}$에 속하며 [\[가환대수학\] §정수적 확장과 아이디얼, ⁋따름정리 4](/ko/math/commutative_algebra/lying_over_and_going_up#cor4)에 의해 이 scheme의 각 component는 $W$의 generic point 위로 간다. 이로부터 우리는 원하는 등식 $\dim_{\overline{x}}X_{\overline{s}}=\dim_xX_s$을 얻는다.
:::

이로부터 등식 ($\ast$)는 같은 가정 하에서 $X$의 점 $x$에 대한 조건

$$\dim_{\kappa(x)}\bigl(\Omega_{X/S}\otimes \kappa(x)\bigr)=\dim_xX_s$$

으로 이해할 수 있다. 여기에서 $\Omega_{X/S}$가 locally free이면 위의 fiber dimension이 rank와 같으므로, 이 조건은 rank가 fiber의 local dimension과 일치한다는 것으로 바꾸어 쓸 수 있다. 이 보조정리를 통하여, cotangent sheaf의 local freeness로부터 smoothness를 읽어낼 수 있다.

::: 명제 3
Locally of finite presentation인 morphism $\varphi:X \rightarrow S$가 flat하고, $\Omega_{X/S}$가 locally free sheaf이며 각 $x\in X$에서 그 rank가 $s=\varphi(x)$ 위 fiber의 local dimension $\dim_xX_s$와 같다고 하자. 그럼 $\varphi$는 smooth하다.
:::
::: 증명
$\varphi$가 flat하므로 각 $s\in S$에 대하여 geometric fiber $X_{\overline{s}}$가 regular임을 보이면 충분하다. $\mathbb{K}=\overline{\kappa(s)}$라 하자.

먼저 주어진 주장을 $X_{\overline{s}}$의 closed point $z$에서 확인한다. $X_{\overline{s}}$는 algebraically closed field $\mathbb{K}$ 위에서 locally of finite presentation이므로 ([§올곱, ⁋명제 16](/ko/math/scheme_theory/fiber_products#prop16)) $z$를 담는 affine open subset $\Spec\bigl(\mathbb{K}[\x_1,\ldots, \x_n]/\mathfrak{a}\bigr)$을 택할 수 있고, $z$에 해당하는 ideal이 maximal이므로 [\[가환대수학\] §영점정리, ⁋보조정리 5](/ko/math/commutative_algebra/nullstellensatz#lem5)에 의하여 이는 어떤 $a\in \mathbb{K}^n$에 대한 $(\x_1-a_1,\ldots, \x_n-a_n)$의 image이고 따라서 $\kappa(z)=\mathbb{K}$이다. 즉 $z$는 $\mathbb{K}$-point이며, 우리는 [§Kähler differential과 여접층, ⁋정의 8](/ko/math/scheme_theory/sheaf_of_differentials#def8) 직후에 이러한 점에 대해서는

$$\Omega_{X_{\overline{s}}/\mathbb{K}}\otimes\kappa(z)\cong\mathfrak{m}_z/\mathfrak{m}_z^2$$

이 성립하는 것을 확인하였다.

이제 $z$의 $X_s$에서의 image를 $x$라 하자. $\Omega_{X/S}$가 locally free이므로 그 $x$에서의 fiber dimension은 rank와 같고, 가정에 의하여 이 값은 다시 $\dim_s X_s$와 같으므로, [보조정리 2](#lem2)는 좌변의 차원 또한 이 값과 같으며 따라서 $\dim_xX_s=\dim_zX_{\overline{s}}$임을 준다. 한편 $z$가 closed point이므로 $\dim_zX_{\overline{s}}=\dim\mathcal{O}_{X_{\overline{s}},z}$이며, 따라서

$$\dim_{\kappa(z)}\mathfrak{m}_z/\mathfrak{m}_z^2=\dim \mathcal{O}_{X_{\overline{s}},z}$$

를 얻는다. Regular local ring이기 위해서는 maximal ideal이 $\dim$개의 원소로 생성되는 Noetherian local ring이어야 하는데 ([\[가환대수학\] §차원, ⁋정의 12](/ko/math/commutative_algebra/Krull_dimension#def12)), [\[가환대수학\] §정수적 확장, ⁋보조정리 8](/ko/math/commutative_algebra/integral_extension#lem8)에 의하여 이는 위의 등식과 동치이므로 $\mathcal{O}_{X_{\overline{s}},z}$는 regular local ring이다.

이제 임의의 점 $\overline{x}\in X_{\overline{s}}$에 대하여 $\overline{\{\overline{x}\}}$ 안의 closed point $z$를 택하면 ([§차원, ⁋명제 11](/ko/math/scheme_theory/dimension#prop11)에 의하여 공집합이 아닌 locally closed subset은 언제나 closed point를 담는다), $z$의 열린근방은 모두 $\overline{x}$를 담으므로 $\mathcal{O}_{X_{\overline{s}},\overline{x}}$는 $\mathcal{O}_{X_{\overline{s}},z}$의 localization이다. Regular local ring의 localization은 regular이므로 ([\[가환대수학\] §정칙성의 호몰로지 판정, ⁋따름정리 4](/ko/math/commutative_algebra/homological_criterion_for_regularity#cor4)) $\mathcal{O}_{X_{\overline{s}},\overline{x}}$ 또한 regular local ring이고, 곧 $X_{\overline{s}}$는 regular scheme이다.
:::

[명제 3](#prop3)의 조건 아래에서 $\Omega_{X/S}$의 rank를 $\varphi$의 *relative dimension<sub>상대차원</sub>*이라 부른다. 직관적으로 이것이 보는 것은 $\varphi$의 fiber 방향 tangent space의 차원이다. 즉 relative tangent bundle $\Omega_{X/S}^\vee$의 $x$에서의 fiber가 곧 $X_s$의 $x$에서의 Zariski tangent space이므로 ([§Kähler differential과 여접층, ⁋정의 8](/ko/math/scheme_theory/sheaf_of_differentials#def8)), relative dimension이 $r$이라는 것은 각 점에서 이 tangent space가 $r$차원이라는 것이다.

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
[명제 3](#prop3)에 의하여 우리가 보여야 할 것은 $x$의 어떤 근방 위에서 $\varphi$가 flat하고 $\Omega_{X/S}$가 rank $n-r$의 locally free sheaf이며, 그 근방의 각 점에서 fiber의 local dimension이 $n-r$이라는 것이다. 먼저 $\Omega$를 기술하기 위해 

$$B=A[\x_1,\ldots, \x_n],\qquad \mathfrak{a}=(f_1,\ldots, f_r), \qquad C=B/\mathfrak{a}$$

이라 하자. 그럼 closed immersion $X\hookrightarrow \mathbb{A}^n_S$의 conormal exact sequence ([§Kähler differential과 여접층, ⁋명제 2](/ko/math/scheme_theory/sheaf_of_differentials#prop2))

$$\mathfrak{a}/\mathfrak{a}^2 \overset{\overline{d}}{\longrightarrow} \Omega_{B/A}\otimes_BC \longrightarrow \Omega_{C/A} \longrightarrow 0$$

에서 $\Omega_{B/A}\otimes_BC$는 $\dd{\x_1},\ldots, \dd{\x_n}$을 기저로 하는 rank $n$의 free $C$-module이다. ([§Kähler differential과 여접층, ⁋명제 9](/ko/math/scheme_theory/sheaf_of_differentials#prop9)) 이 때 첫째 morphism $\overline{d}$는 

$$\overline{d}: \mathfrak{a}/ \mathfrak{a}^2\rightarrow \Omega_{B/A}\otimes_BC;\qquad f_i+\mathfrak{a}^2\mapsto \dd{f_i}=\sum_j\frac{\partial f_i}{\partial \x_j}\dd{\x_j}$$

로 주어지는 것이다. 한편, 가정에 의해 

$$\pi: C^{\oplus r} \rightarrow \mathfrak{a}/\mathfrak{a}^2;\qquad e_i\mapsto f_i+\mathfrak{a}^2$$

은 surjective $C$-module homomorphism이며, 그럼 합성 

$$\overline{d}\circ\pi: C^{\oplus r}\rightarrow \mathfrak{a}/\mathfrak{a}^2\rightarrow \Omega_{B/A}\otimes_BC;\qquad e_i\mapsto \sum_j\frac{\partial f_i}{\partial \x_j}\dd{\x_j}$$

은 전사함수이며, 이를 $\overline{d}\circ\pi$를 $e_i$와 $\dd{\x_j}$ 기저에 대하여 표현한 행렬이 정확히 Jacobian $J$의 transpose로, 각각의 성분들은 $X$ 위의 함수를 정의한다.

이제 가정에 의해 $J$가 full rank이므로, 어떤 index $j_1,\ldots, j_r$이 존재하여 그 열들이 이루는 $r\times r$ minor $g$가 $x$에서 $0$이 아니도록 할 수 있다. 이제 $\Omega_{B/A}\otimes_BC$의 좌표들 $\dd{\x_{j_1}},\ldots, \dd{\x_{j_r}}$로의 projection $\pr_{j_1,\ldots,j_r}$을 생각하면, 이를 합성한

$$\pr_{j_1,\ldots,j_r}\circ\overline{d}\circ\pi: C^{\oplus r}\rightarrow\mathfrak{a}/\mathfrak{a}^2\rightarrow \Omega_{B/A}\otimes_BC\rightarrow C^{\oplus r}$$

을 생각할 수 있다. 그럼 이 사상은 $e_i$를 $\dd{f_i}$의 $j_1,\ldots, j_r$번째 좌표로 보내며, 이를 기저 $e_i$에 대하여 표현한 행렬이 정확히 $J$의 $j_1,\ldots, j_r$번째 열이 이루는 $r\times r$ 부분행렬의 transpose가 된다. 따라서 그 determinant $g$에서 localization을 취하면 $g$가 unit이 되므로

$$(\pr_{j_1,\ldots,j_r}\circ\overline{d}\circ\pi)_g: C_g^{\oplus r}\rightarrow C_g^{\oplus r}$$

은 automorphism이다. ([\[다중선형대수학\] §행렬식, ⁋따름정리 3](/ko/math/multilinear_algebra/determinants#cor3)) 이제 이 automorphism의 역과 $(\pr_{j_1,\ldots,j_r})_g$를 합성하면 $(\overline{d}\circ\pi)_g$의 retraction이 얻어지므로 $(\overline{d}\circ\pi)_g$는 split injection이고, 특히 $\pi_g$는 injective이다. $\pi_g$는 이미 $\pi$ 단계에서부터 surjective였으므로 isomorphism이 되며, 따라서 $(\mathfrak{a}/\mathfrak{a}^2)_g$는 rank $r$ free module이고 $\overline{d}_g$ 또한 free module 사이의 split injection이다. 

이제 $\overline{d}_g$의 cokernel은, $\pi_g$가 isomorphism이므로, $(\overline{d}\circ\pi)_g$의 cokernel과 같고 일반적으로 split injection의 cokernel은 그 retraction의 kernel과 isomorphic하며, 위에서 $(\overline{d}\circ\pi)_g$의 retraction이 $(\pr_{j_1,\ldots,j_r})_g$에 automorphism의 역을 합성한 것으로 주어지는 것을 살펴보았으므로 이는 $(\pr_{j_1,\ldots,j_r})_g$의 kernel, 즉 $j\notin\{j_1,\ldots, j_r\}$인 $\dd{\x_j}$들이 생성하는 rank $n-r$의 free submodule이다. 이제 tensor product는 cokernel을 보존하므로 이 cokernel이 곧 $\Omega_{C/A}\otimes_CC_g$이고, 따라서 $\Omega_{C/A}$는 $D(g)=\Spec C_g$ 위에서 rank $n-r$ locally free sheaf가 된다.

이제 $\varphi$가 $x$의 어떤 근방에서 flat하다는 것을 보인다. 이를 위해 우리가 사용할 결과는 [\[가환대수학\] §평탄성과 국소화, ⁋따름정리 4](/ko/math/commutative_algebra/local_criterion_for_flatness#cor4)으로, 이를 위해서 우리는 우선 $A$가 Noetherian인 경우로의 reduction을 한 차례 진행해야 한다. 

이는 기본적으로 우리가 필요로 하는 정보가 $A$ 전체가 아니라 $f_1,\ldots, f_r$의 계수들이 $A$ 안에서 생성하는 $\mathbb{Z}$-subalgebra $A_0$에 담겨있으므로 가능하다. 그럼 이 세팅에서 [\[가환대수학\] §기본 개념들, ⁋따름정리 13](/ko/math/commutative_algebra/basic_notions#cor13)에 의해 $A_0$은 Noetherian이고, $C_0=A_0[\x_1,\ldots, \x_n]/(f_1,\ldots, f_r)$로 두면 $C=C_0\otimes_{A_0}A$이다. 한편 $f_i$의 계수가 $A_0$에 있으므로 $\partial f_i/\partial \x_j$의 계수 또한 $A_0$에 있고, 따라서 앞에서 고른 minor $g$는 $A_0[\x_1,\ldots, \x_n]$의 원소이다. 그럼 $x$의 $\Spec C_0$에서의 image를 $x_0$이라 할 때 $x_0$에 대응하는 prime이 $x$에 대응하는 prime의 preimage이므로 $g$는 $x_0$에서도 $0$이 아니며, $J$가 행을 $r$개 가지므로 $x_0$에서 $J$의 rank 또한 정확히 $r$이다. 한편  flatness는 base change에 의해 보존되므로 ([§평탄사상, ⁋명제 3](/ko/math/scheme_theory/flat_morphisms#prop3)) $\Spec C_0 \rightarrow \Spec A_0$이 $x_0$의 근방에서 flat이면 $\varphi$도 $x$의 근방에서 flat이다. 이로부터 우리는 $A$가 Noetherian이라 가정할 수 있다.

이제 $s=\varphi(x)$라 하자. 위의 논증을 따라 $A$가 Noetherian이라 가정하면, 이 따름정리를 *Noetherian* local ring $(\mathcal{O}_{S,s},\mathfrak{m}_s)$와 그 위의 local *Noetherian* algebra $(\mathcal{O}_{\mathbb{A}^n_S,x},\mathfrak{m}_x)$, 그리고 그 자신을 module로 본 $M=\mathcal{O}_{\mathbb{A}^n_S,x}$와 $\mathfrak{m}_x$의 원소 $f_1,\ldots, f_r$에 적용할 수 있다. $M$은 polynomial ring $B=A[\x_1,\ldots, \x_n]$의 localization이며 $B$가 $A$ 위에서 free이므로 $\mathcal{O}_{S,s}$ 위에서 flat이고, 따라서 우리가 보여야 할 것은 $R=M/\mathfrak{m}_sM$, 즉 fiber $\mathbb{A}^n_{\kappa(s)}$의 $x$에서의 local ring에서 $f_1,\ldots, f_r$의 image가 regular sequence를 이룬다는 것뿐이다. $\mathfrak{m}_s$로 나누는 것은 $s$ 위의 fiber로 제한하는 것이고 $f_i$의 image는 그 fiber 위로 내려온 방정식이므로, 이 조건은 방정식들이 fiber 안에서 서로 겹치지 않고 차원을 하나씩 깎는다는 뜻이다. 자르기 전의 $\mathbb{A}^n_S \rightarrow S$는 이미 flat이므로 남는 문제는 자르는 방식뿐이고, 따름정리는 fiber 하나에서 확인한 이 조건을 base 방향으로 들어올려 준다. $R$의 maximal ideal을 $\mathfrak{m}$이라 적자.

우선 [\[가환대수학\] §정칙성의 호몰로지 판정, ⁋따름정리 6](/ko/math/commutative_algebra/homological_criterion_for_regularity#cor6)에 의하여 $\kappa(s)[\x_1,\ldots, \x_n]$이 regular ring이므로 $R$은 residue field $\kappa(x)$를 가지는 regular local ring이다. $f_i$의 $R$에서의 image를 $\overline{f}_i$라 하면 $\overline{f}_i\in\mathfrak{m}$이고, Leibniz 규칙에 의하여 $h\mapsto \sum_j(\partial h/\partial \x_j)(x)\dd{\x_j}$가 $\mathfrak{m}^2$을 소멸시키므로 $\kappa(x)$-linear map $\mathfrak{m}/\mathfrak{m}^2 \rightarrow \kappa(x)^{\oplus n}$이 유도된다. 이 map은 $\overline{f}_i$의 class를 $J$의 $i$번째 행으로 보내고 가정에 의하여 그 행들이 일차독립이므로, $\overline{f}_1,\ldots, \overline{f}_r$의 class들도 $\mathfrak{m}/\mathfrak{m}^2$ 안에서 일차독립이다. 이 class들을 $\mathfrak{m}/\mathfrak{m}^2$의 기저로 확장하고 [\[가환대수학\] §정수적 확장, ⁋보조정리 8](/ko/math/commutative_algebra/integral_extension#lem8)을 적용하면 $\mathfrak{m}$을 생성하는 $\dim R$개의 원소를 얻으므로, $\overline{f}_1,\ldots, \overline{f}_r$은 $R$의 regular system of parameters의 앞부분이다. [\[가환대수학\] §정칙국소환, ⁋따름정리 3](/ko/math/commutative_algebra/regular_local_rings#cor3)에 의하여 regular system of parameters 전체가 $R$-sequence이므로, 그 앞부분인 $\overline{f}_1,\ldots, \overline{f}_r$ 또한 $R$-regular sequence이다.

그럼 [\[가환대수학\] §평탄성과 국소화, ⁋따름정리 4](/ko/math/commutative_algebra/local_criterion_for_flatness#cor4)에 의하여 $f_1,\ldots, f_r$은 $\mathcal{O}_{\mathbb{A}^n_S,x}$의 regular sequence이고 quotient $\mathcal{O}_{X,x}$는 $\mathcal{O}_{S,s}$ 위에서 flat이다. [§평탄사상, ⁋정의 1](/ko/math/scheme_theory/flat_morphisms#def1)의 의미에서 $\varphi$는 $x$에서 flat이므로 [§평탄사상, ⁋정리 20](/ko/math/scheme_theory/flat_morphisms#thm20)에 의하여 $x$의 어떤 열린근방 위에서 flat하다.

마지막으로 남은 것은 fiber의 local dimension이다. 앞의 근방과 $D(g)$의 교집합을 $U$라 하면 $U$ 위에서 $\varphi$는 flat하고 $\Omega_{C/A}$는 rank $n-r$의 locally free이므로, [명제 3](#prop3)을 적용하기 위해 보여야 할 것은 $U$의 각 점에서 fiber의 local dimension이 $n-r$이라는 것이다. 이는 위의 fiber 논증을 $U$의 다른 점에서 반복하여 얻는다. $U$의 점 $y$와 $s'=\varphi(y)$에 대하여 fiber $X_{s'}$의 $y$를 지나는 component의 generic point를 $\eta$라 하면, $g$가 $\eta$에서도 가역이어서 $J$의 rank가 $r$이므로, 같은 논증에 의하여 $\overline{f}_1,\ldots, \overline{f}_r$의 class들은 regular local ring $\mathcal{O}_{\mathbb{A}^n_{\kappa(s')},\eta}$의 $\mathfrak{m}_\eta/\mathfrak{m}_\eta^2$ 안에서 일차독립이다. 곧 그 component의 codimension인 $\dim\mathcal{O}_{\mathbb{A}^n_{\kappa(s')},\eta}$는 $r$ 이상이고, $\eta$가 $(\overline{f}_1,\ldots, \overline{f}_r)$을 포함하는 minimal prime이므로 [\[가환대수학\] §차원, ⁋정리 7](/ko/math/commutative_algebra/Krull_dimension#thm7)이 반대 부등식을 주어 codimension은 정확히 $r$이며, 차원 공식에 의하여 ([\[가환대수학\] §뇌터 정규화, ⁋정리 4](/ko/math/commutative_algebra/noether_normalization#thm4)) component의 차원은 $n-r$이다. 따라서 $U$의 각 점에서 fiber의 local dimension이 rank와 일치하고, [명제 3](#prop3)에 의하여 $\varphi$는 relative dimension $n-r$의 smooth morphism이다.
:::

차원만 따라가면 이 증명이 하는 일은 짧게 적힌다. $n$은 fiber 방향 coordinate $\x_1,\ldots, \x_n$의 개수, 곧 $\mathbb{A}^n_S \rightarrow S$의 relative dimension이며 base의 차원은 여기에 기여하지 않는다. $r$은 각 fiber 안에서 방정식들이 깎아내는 차원의 수로, Jacobian의 rank가 $r$이라는 가정이 그 $r$개의 조건이 서로 겹치지 않음을 보장한다. 남는 $n-r$은 $\dd{\x_1},\ldots, \dd{\x_n}$이 생성하는 rank $n$의 free module을 일차독립인 $\dd{f_1},\ldots, \dd{f_r}$로 나눈 $\Omega_{X/S}$의 rank이자 codimension $r$로 잘린 fiber의 차원이고, [명제 3](#prop3)이 요구하는 두 수의 일치가 곧 이것이다.

증명의 fiber 단계에서 얻은 regular sequence는 한 점 $x$에서의 조건이지만 근방으로 퍼진다. 각 $i$에 대하여 $\overline{f}_{i+1}$의 곱셈이 $\kappa(s)[\x_1,\ldots, \x_n]/(\overline{f}_1,\ldots, \overline{f}_i)$에 만드는 kernel은 finitely generated이고 $x$에서의 stalk이 $0$이므로 $x$를 담는 어떤 principal open 위에서 소멸한다. 이 principal open들의 교집합을 $D(h)\subseteq \mathbb{A}^n_{\kappa(s)}$라 하면 그 위에서 $\overline{f}_1,\ldots, \overline{f}_r$은 regular sequence를 이루고, $X_s\cap D(h)\hookrightarrow D(h)$는 codimension $r$의 complete intersection이다. ([§완전교차, ⁋정의 1](/ko/math/scheme_theory/complete_intersections#def1)) 곧 Jacobian 조건 아래에서 $\varphi$의 fiber는 국소적으로 complete intersection이다.

Jacobian 판정은 smooth 여부를 미분 계산으로 환원하므로 실용적으로 가장 자주 쓰인다. 가령 $\Spec\mathbb{Z}[\x,\y]/(\y^2-\x^3-\x)$ 위에서 $f=\y^2-\x^3-\x$의 Jacobian은 $(\partial f/\partial\x, \partial f/\partial\y)=(-3\x^2-1, 2\y)$이며, 이 두 성분이 동시에 영이 되는 점이 base의 어떤 소수에서 나타나는지를 보면 곡선이 그 소수에서 smooth fiber를 가지는지를 판정할 수 있다.

## 매끄러운 사상의 국소 구조

[정리 4](#thm4)는 Jacobian 조건을 만족하는 방정식 표현이 주어졌을 때 smoothness를 준다. 그 역, 곧 임의의 smooth morphism이 국소적으로 그러한 표현을 가진다는 것이 이 절의 목표이며, 여기에서 [명제 3](#prop3)의 역방향이 따라나온다. 출발점은 base가 field인 경우이다. 이 경우 smooth 조건은 geometric fiber의 regularity 하나로 주어지므로, 남는 일은 그 regularity를 Jacobian의 rank로 번역하는 것뿐이다.

::: 보조정리 5
Field $\mathbb{K}$와 그 algebraic closure $\mathbb{L}=\overline{\mathbb{K}}$, 그리고 다항식 $g_1,\ldots, g_m\in \mathbb{K}[\x_1,\ldots, \x_n]$에 대하여

$$X=\Spec\bigl(\mathbb{K}[\x_1,\ldots, \x_n]/(g_1,\ldots, g_m)\bigr)$$

이라 하고, base change $X_\mathbb{L}=X\times_{\Spec\mathbb{K}}\Spec\mathbb{L}$이 regular scheme이라 하자. 그럼 임의의 $x\in X$에 대하여 $c=n-\dim_xX$개의 첨자 $i_1,\ldots, i_c$와 $h\in \mathbb{K}[\x_1,\ldots, \x_n]$이 존재하여, $x\in D(h)$이고 $D(h)$ 위에서 $X$는 $g_{i_1},\ldots, g_{i_c}$가 정의하는 $\mathbb{A}^n_\mathbb{K}$의 closed subscheme과 일치하며, Jacobian $(\partial g_{i_k}/\partial \x_j)$의 어떤 $c\times c$ minor가 $D(h)$ 위에서 가역이다.
:::
::: 증명
$\mathfrak{a}=(g_1,\ldots, g_m)$이라 하고, $X_\mathbb{L}$을 $\mathfrak{a}\mathbb{L}[\x_1,\ldots, \x_n]$이 정의하는 $\mathbb{A}^n_\mathbb{L}$의 closed subscheme으로 본다. $X_\mathbb{L} \rightarrow X$가 전사이므로 ([보조정리 2](#lem2)의 증명) $x$ 위의 점 $\overline{x}\in X_\mathbb{L}$을 택할 수 있다.

먼저 차원을 고정한다. $X_\mathbb{L}$의 local ring들은 regular이므로 특히 domain이고 ([\[가환대수학\] §정칙국소환, ⁋따름정리 1](/ko/math/commutative_algebra/regular_local_rings#cor1)), 따라서 각 점은 유일한 irreducible component 위에 놓인다. $X_\mathbb{L}$이 Noetherian이라 component가 유한개이므로 각 component는 나머지의 합집합의 여집합으로서 열려 있고, 곧 clopen이다. 그럼 $\overline{x}$를 담는 component를 $Z$라 할 때 $Z$의 모든 점에서 local dimension은 $d=\dim Z$이다. 이제 $\overline{\{\overline{x}\}}$ 안의 closed point $z$를 택하면 ([§차원, ⁋명제 11](/ko/math/scheme_theory/dimension#prop11)) $z\in Z$이므로 $\dim_zX_\mathbb{L}=d$이고, $z$가 closed point이므로 [\[가환대수학\] §뇌터 정규화, ⁋정리 4](/ko/math/commutative_algebra/noether_normalization#thm4)에 의하여 $\dim\mathcal{O}_{X_\mathbb{L},z}=d$이다. 또 $\mathbb{L}$이 algebraically closed이므로 [\[가환대수학\] §영점정리, ⁋보조정리 5](/ko/math/commutative_algebra/nullstellensatz#lem5)에 의하여 $z$에 해당하는 maximal ideal은 어떤 $a\in \mathbb{L}^n$에 대한 $(\x_1-a_1,\ldots, \x_n-a_n)$의 image이고, 특히 $\kappa(z)=\mathbb{L}$이다.

다음으로 $z$에서 Jacobian의 rank를 계산한다. Closed immersion $X_\mathbb{L}\hookrightarrow \mathbb{A}^n_\mathbb{L}$의 conormal exact sequence에서 ([§Kähler differential과 여접층, ⁋명제 2](/ko/math/scheme_theory/sheaf_of_differentials#prop2)) 가운데 항은 $\dd{\x_1},\ldots, \dd{\x_n}$을 기저로 하는 rank $n$의 free module이고 ([§Kähler differential과 여접층, ⁋명제 9](/ko/math/scheme_theory/sheaf_of_differentials#prop9)), defining ideal이 $g_1,\ldots, g_m$으로 생성되므로 왼쪽 morphism의 image는 $\dd{g_i}=\sum_j(\partial g_i/\partial \x_j)\dd{\x_j}$들이 생성한다. 이 sequence를 $\kappa(z)$로 내리면

$$\Omega_{X_\mathbb{L}/\mathbb{L}}\otimes\kappa(z)\cong\coker\bigl(\kappa(z)^{\oplus m} \longrightarrow \kappa(z)^{\oplus n}\bigr)$$

를 얻으며, 여기에서 오른쪽 morphism은 $z$에서 계산한 Jacobian $J=(\partial g_i/\partial \x_j)$의 transpose이다. 한편 $z$가 $\mathbb{L}$-point이므로 좌변은 $\mathfrak{m}_z/\mathfrak{m}_z^2$이고 ([§Kähler differential과 여접층, ⁋정의 8](/ko/math/scheme_theory/sheaf_of_differentials#def8) 직후), $\mathcal{O}_{X_\mathbb{L},z}$가 regular local ring이므로 그 차원은 $\dim\mathcal{O}_{X_\mathbb{L},z}=d$이다. ([\[가환대수학\] §차원, ⁋정의 12](/ko/math/commutative_algebra/Krull_dimension#def12)) 두 계산을 맞추면 $\rank J(z)=n-d$이며, 이 값을 $c$라 쓰자.

그럼 $J(z)$의 영이 아닌 $c\times c$ minor가 존재한다. 그것을 이루는 행에 대응하는 첨자를 $i_1,\ldots, i_c$라 하고 $f_k=g_{i_k}$, 그 minor를 $h_0\in \mathbb{K}[\x_1,\ldots, \x_n]$이라 하자. $X'=\Spec\bigl(\mathbb{K}[\x_1,\ldots, \x_n]/(f_1,\ldots, f_c)\bigr)$으로 두면 $(f_1,\ldots, f_c)\subseteq \mathfrak{a}$이므로 $X$는 $X'$의 closed subscheme이며, 우리는 이 포함이 $x$ 근방에서 등호임을 보인다.

$z$에서 확인한다. $R=\mathcal{O}_{\mathbb{A}^n_\mathbb{L},z}$은 residue field $\mathbb{L}$을 가지는 regular local ring이고 ([\[가환대수학\] §정칙성의 호몰로지 판정, ⁋따름정리 6](/ko/math/commutative_algebra/homological_criterion_for_regularity#cor6)) 그 차원은 $n$이다. $z$가 $\mathbb{L}$-point이므로 Leibniz 규칙에 의하여 $u\mapsto \sum_j(\partial u/\partial \x_j)(z)\dd{\x_j}$가 isomorphism $\mathfrak{m}_R/\mathfrak{m}_R^2\cong\mathbb{L}^{\oplus n}$을 주고, 이 아래에서 $f_1,\ldots, f_c$의 class들은 $h_0(z)\neq 0$에 의하여 일차독립이다. 이들을 기저로 확장하고 [\[가환대수학\] §정수적 확장, ⁋보조정리 8](/ko/math/commutative_algebra/integral_extension#lem8)을 적용하면 $\mathfrak{m}_R$은 $f_1,\ldots, f_c$와 다른 $n-c$개의 원소로 생성되므로, $\overline{R}=R/(f_1,\ldots, f_c)=\mathcal{O}_{X'_\mathbb{L},z}$의 maximal ideal은 $n-c$개의 원소로 생성되고 [\[가환대수학\] §차원, ⁋정리 7](/ko/math/commutative_algebra/Krull_dimension#thm7)에 의하여 $\dim\overline{R}\leq n-c=d$이다. 그런데 $\mathcal{O}_{X_\mathbb{L},z}$는 $\overline{R}$의 quotient이고 그 차원이 $d$이므로 $\dim\overline{R}\geq d$이며, 결국 $\dim\overline{R}=d$이다. 곧 $\overline{R}$의 maximal ideal이 $\dim\overline{R}$개의 원소로 생성되어 $\overline{R}$은 regular local ring이고 ([\[가환대수학\] §차원, ⁋정의 12](/ko/math/commutative_algebra/Krull_dimension#def12)), 특히 domain이다.

이제 surjection $\overline{R} \rightarrow \mathcal{O}_{X_\mathbb{L},z}$의 kernel $I$가 영이 아니라 하자. $\overline{R}/I$의 prime ideal들은 $I$를 포함하는 $\overline{R}$의 prime ideal들이고 그러한 chain은 모두 $I$ 위의 minimal prime에서 시작하므로, $\dim\overline{R}/I=\dim\overline{R}/\mathfrak{p}$를 실현하는 $I$ 위의 minimal prime $\mathfrak{p}$가 존재한다. $I\neq 0$이고 $\overline{R}$이 domain이므로 $\mathfrak{p}\neq 0$이며, 따라서 $\overline{R}/\mathfrak{p}$의 길이 $\dim\overline{R}/\mathfrak{p}$인 chain 앞에 $0\subsetneq\mathfrak{p}$를 이어 붙이면 $\dim\overline{R}\geq \dim\overline{R}/\mathfrak{p}+1$을 얻는다. 곧 $\dim\mathcal{O}_{X_\mathbb{L},z}<\dim\overline{R}=d$가 되어 모순이므로 $I=0$이다. $X_\mathbb{L}\subseteq X'_\mathbb{L}$의 ideal sheaf는 $g_1,\ldots, g_m$의 image로 생성되어 finite type이므로, 그 stalk이 $z$에서 소멸하면 $z$의 어떤 열린근방 위에서 소멸한다. $z\in \overline{\{\overline{x}\}}$이므로 이 근방은 $\overline{x}$를 담는다.

마지막으로 $\mathbb{K}$로 내려온다. $X\subseteq X'$의 ideal sheaf를 $\mathcal{J}$라 하면 $\mathbb{K} \rightarrow \mathbb{L}$이 flat이므로 $\mathcal{J}$의 $\mathbb{L}$로의 base change가 $X_\mathbb{L}\subseteq X'_\mathbb{L}$의 ideal sheaf이고, 따라서 $\mathcal{J}_x\otimes_{\mathcal{O}_{X',x}}\mathcal{O}_{X'_\mathbb{L},\overline{x}}=0$이다. 그런데 $\mathcal{O}_{X',x} \rightarrow \mathcal{O}_{X'_\mathbb{L},\overline{x}}$는 flat local homomorphism이므로 [§평탄사상, ⁋보조정리 15](/ko/math/scheme_theory/flat_morphisms#lem15)에 의하여 영이 아닌 module을 영으로 보내지 않으며, 곧 $\mathcal{J}_x=0$이다. $\mathcal{J}$ 또한 finite type이므로 $x$의 어떤 principal open 근방 위에서 소멸한다. 한편 $D(h_0)$은 $z$를 담는 열린집합이라 $\overline{x}$를 담고, $\kappa(x)\hookrightarrow\kappa(\overline{x})$이므로 $h_0(x)\neq 0$이다. 그럼 앞의 principal open과 $D(h_0)$의 교집합을 $D(h)$로 두면 원하는 성질이 모두 성립한다. 끝으로 [보조정리 2](#lem2)를 $S=\Spec\mathbb{K}$에 적용하면 $d=\dim_{\overline{x}}X_\mathbb{L}=\dim_xX$이므로 $c=n-\dim_xX$이다.
:::

Base가 일반의 scheme일 때에는 이 표현을 fiber 위에서 얻은 뒤 base 방향으로 들어올리게 되며, 그 들어올림을 정당화하는 것이 정의에 들어 있는 flatness이다.

::: 정리 6 (국소 구조)
Smooth morphism $\varphi:X \rightarrow S$와 점 $x\in X$, $s=\varphi(x)$에 대하여, $s$의 affine 열린근방 $\Spec A$와 그 위에 놓인 $x$의 열린근방으로서

$$\Spec\Bigl(\bigl(A[\x_1,\ldots, \x_n]/(f_1,\ldots, f_c)\bigr)_g\Bigr)$$

와 $S$-isomorphic한 것이 존재한다. 여기에서 Jacobian $(\partial f_i/\partial \x_j)$의 어떤 $c\times c$ minor는 이 ring에서 가역이며, $c=n-\dim_xX_s$이다.
:::
::: 증명
문제가 국소적이므로 $S=\Spec A$이고 $x$가 affine open $\Spec C$에 속한다 하여도 좋다. $\varphi$가 locally of finite presentation이므로 $C=A[\x_1,\ldots, \x_n]/\mathfrak{a}$, $\mathfrak{a}=(u_1,\ldots, u_m)$으로 적을 수 있다.

Fiber $X_s$는 $\kappa(s)[\x_1,\ldots, \x_n]$을 $u_i$의 image $\overline{u}_i$들로 나눈 것이고, $\varphi$가 smooth하므로 그 base change $X_{\overline{s}}$는 regular이다. ([정의 1](#def1)) 따라서 [보조정리 5](#lem5)를 $\mathbb{K}=\kappa(s)$와 $\overline{u}_1,\ldots, \overline{u}_m$에 적용할 수 있고, 이는 $c=n-\dim_xX_s$개의 첨자 $i_1,\ldots, i_c$를 주어 $x$의 어떤 열린근방 위에서 $X_s$가 $\overline{u}_{i_1},\ldots, \overline{u}_{i_c}$가 정의하는 closed subscheme과 일치하고 대응하는 $c\times c$ minor가 그 위에서 가역이 되도록 한다. $f_k=u_{i_k}$로 두고 $A[\x_1,\ldots, \x_n]$에서 계산한 그 minor를 $g_0$이라 하자. $g_0$을 $\kappa(s)$로 내린 것이 $x$에서 영이 아니므로 $g_0(x)\neq 0$이다.

이제 $X'=\Spec\bigl(A[\x_1,\ldots, \x_n]/(f_1,\ldots, f_c)\bigr)$이라 하면 $(f_1,\ldots, f_c)\subseteq \mathfrak{a}$이므로 $X$는 $X'$의 closed subscheme이고, 그 ideal $I$는 $u_1,\ldots, u_m$의 image로 생성되어 finite type이다. 우리는 $I_x=0$을 보인다.

$\mathcal{O}_{S,s}$-module의 exact sequence

$$0 \rightarrow I_x \rightarrow \mathcal{O}_{X',x} \rightarrow \mathcal{O}_{X,x} \rightarrow 0$$

을 생각하자. $\varphi$가 flat하므로 $\mathcal{O}_{X,x}$는 flat $\mathcal{O}_{S,s}$-module이고 ([§평탄사상, ⁋정의 1](/ko/math/scheme_theory/flat_morphisms#def1)), 특히 $\mathfrak{m}_s\otimes_{\mathcal{O}_{S,s}}\mathcal{O}_{X,x} \rightarrow \mathcal{O}_{X,x}$가 단사여서 [\[가환대수학\] §평탄성, ⁋명제 1](/ko/math/commutative_algebra/flatness#prop1)에 의하여 $\Tor_1^{\mathcal{O}_{S,s}}(\kappa(s), \mathcal{O}_{X,x})=0$이다. 따라서 위 sequence에 $-\otimes_{\mathcal{O}_{S,s}}\kappa(s)$를 적용한 것 또한 왼쪽에서 exact이며, 그 왼쪽 항 $I_x/\mathfrak{m}_sI_x$는 $\mathcal{O}_{X'_s,x} \rightarrow \mathcal{O}_{X_s,x}$의 kernel과 같다. 그런데 [보조정리 5](#lem5)가 $x$ 근방에서 $X_s=X'_s$를 주므로 이 kernel은 영이고, 곧 $I_x=\mathfrak{m}_sI_x$이다. $\varphi$가 morphism이라 $\mathfrak{m}_s\mathcal{O}_{X',x}\subseteq\mathfrak{m}_x$이고 $I_x$가 finitely generated이므로, [\[가환대수학\] §정수적 확장, ⁋보조정리 8](/ko/math/commutative_algebra/integral_extension#lem8)에 의하여 $I_x=0$이다.

$I$가 finite type이므로 $I$는 $x$의 어떤 열린근방 위에서 소멸하고, 그 근방 안의 principal open $D(g_1)$을 택하면 $X$와 $X'$은 $D(g_1)$ 위에서 일치한다. $g=g_0g_1$으로 두면 원하는 표현을 얻는다.
:::

이제 [명제 3](#prop3)의 역방향이 따라나오며, 이로써 cotangent sheaf에 의한 smooth morphism의 characterization이 완성된다.

::: 정리 7
Locally of finite presentation인 morphism $\varphi:X \rightarrow S$에 대하여 다음이 동치이다.

1. $\varphi$는 smooth하다.
2. $\varphi$는 flat하고, $\Omega_{X/S}$는 locally free sheaf이며, 각 $x\in X$에서 그 rank가 $s=\varphi(x)$ 위 fiber의 local dimension $\dim_xX_s$와 같다.
:::
::: 증명
두 번째 조건에서 첫 번째 조건이 따라나오는 것이 [명제 3](#prop3)이다.

역으로 $\varphi$가 smooth하다 하자. Flatness는 [정의 1](#def1)에 들어 있다. 점 $x\in X$와 $s=\varphi(x)$를 고정하면, [정리 6](#thm6)에 의하여 $x$의 어떤 열린근방 위에서 $X$는 $A[\x_1,\ldots, \x_n]/(f_1,\ldots, f_c)$의 localization이고 Jacobian의 어떤 $c\times c$ minor가 그 위에서 가역이며 $c=n-\dim_xX_s$이다. 그럼 [정리 4](#thm4)의 증명에서 conormal exact sequence로부터 locally free임을 얻은 논증이 그대로 적용되어, 그 근방 위에서 $\Omega_{X/S}$는 rank $n-c$의 locally free sheaf이다. 곧 그 rank는 $\dim_xX_s$이다.
:::

Jacobian 판정의 증명에서 실제로 쓰인 것은 conormal exact sequence의 왼쪽 morphism이 단사라는 것을 넘어 split injection이 된다는 사실이었다. 이 성질은 택한 방정식 표현에 딸린 우연이 아니라 smoothness 자체와 동치이다.

::: 명제 8
$S=\Spec A$ 위의 closed immersion $X\hookrightarrow \mathbb{A}^n_S$이 주어졌다 하고, $B=A[\x_1,\ldots, \x_n]$, 그 defining ideal을 $\mathfrak{a}\subseteq B$, $C=B/\mathfrak{a}$라 하자. 그럼 $\varphi:X \rightarrow S$가 smooth한 것은 conormal exact sequence가 ([§Kähler differential과 여접층, ⁋명제 2](/ko/math/scheme_theory/sheaf_of_differentials#prop2)) 왼쪽에서도 exact이며 split되는 것, 곧

$$0 \longrightarrow \mathfrak{a}/\mathfrak{a}^2 \overset{\overline{d}}{\longrightarrow} \Omega_{B/A}\otimes_BC \longrightarrow \Omega_{C/A} \longrightarrow 0$$

이 split short exact sequence인 것과 동치이다. 이 때 $\mathfrak{a}/\mathfrak{a}^2$과 $\Omega_{C/A}$는 모두 finitely generated projective $C$-module이다.
:::
::: 증명
먼저 $\varphi$가 smooth하다 하자. [정리 7](#thm7)에 의하여 $\Omega_{C/A}$는 locally free이고 finitely presented이므로 projective $C$-module이며, 따라서 오른쪽 surjection은 split된다. 남은 것은 $\overline{d}$가 단사라는 것, 곧 conormal sequence의 왼쪽 두 항이 이루는 naive cotangent complex의 ([\[가환대수학\] §미분, ⁋정의 10](/ko/math/commutative_algebra/differentials#def10)) $H_1=\ker\overline{d}$가 소멸한다는 것이다. 이를 위해 우선 위의 split으로부터 $\Omega_{B/A}\otimes_BC\cong \Omega_{C/A}\oplus \im\overline{d}$이므로 $\im\overline{d}$가 free module의 direct summand로서 projective이고, 따라서 surjection $\mathfrak{a}/\mathfrak{a}^2 \rightarrow \im\overline{d}$ 또한 split되어

$$\mathfrak{a}/\mathfrak{a}^2\cong\ker\overline{d}\oplus\im\overline{d}$$

가 성립함을 관찰한다. $\varphi$가 locally of finite presentation이라 $\mathfrak{a}$가 finitely generated이므로 $\ker\overline{d}$는 finitely generated $C$-module이고, 곧 임의의 prime $\mathfrak{q}\subseteq C$에 대하여 $(\ker\overline{d})_\mathfrak{q}=0$임을 보이면 충분하다.

$\mathfrak{q}$에 해당하는 점을 $x$, $s=\varphi(x)$, $\mathfrak{q}$의 $B$에서의 preimage를 $\mathfrak{p}$라 하고 $d=\dim_xX_s$라 하자. [정리 7](#thm7)에 의하여 $\Omega_{C/A}$의 $\mathfrak{q}$에서의 rank가 $d$이므로 $(\im\overline{d})_\mathfrak{q}$는 rank $n-d$의 free module이고, 위의 분해에 의하여 $(\mathfrak{a}/\mathfrak{a}^2)_\mathfrak{q}$를 생성하는 최소 원소 개수는 $n-d$ 이상이며 등호가 성립하는 것과 $(\ker\overline{d})_\mathfrak{q}=0$인 것이 동치이다. 한편 $\mathfrak{a}\subseteq\mathfrak{p}$이므로 $\mathfrak{a}^2\subseteq\mathfrak{p}\mathfrak{a}$이고, [\[가환대수학\] §정수적 확장, ⁋보조정리 8](/ko/math/commutative_algebra/integral_extension#lem8)에 의하여 이 최소 개수는 $\dim_{\kappa(x)}\mathfrak{a}_\mathfrak{p}\otimes\kappa(x)$와 같다.

이 값은 fiber에서 계산된다. $\varphi$가 flat하여 $C$가 flat $A$-module이므로 $\Tor_1^A(C, \kappa(s))=0$이고, 따라서 $0 \rightarrow \mathfrak{a} \rightarrow B \rightarrow C \rightarrow 0$에 $-\otimes_A\kappa(s)$를 적용한 것은 왼쪽에서도 exact이다. $B$가 $A$ 위에서 free라 $B\otimes_A\kappa(s)=\kappa(s)[\x_1,\ldots, \x_n]$이므로, 이는 $\mathfrak{a}\otimes_A\kappa(s)$가 그 안에서 fiber $X_s$를 정의하는 ideal $\overline{\mathfrak{a}}$와 같음을 뜻한다. 따라서 $\mathfrak{a}_\mathfrak{p}\otimes\kappa(x)=\overline{\mathfrak{a}}_{\overline{\mathfrak{p}}}\otimes\kappa(x)$이며, $\varphi$가 smooth하여 geometric fiber가 regular이므로 [보조정리 5](#lem5)에 의하여 $\overline{\mathfrak{a}}$는 $x$ 근방에서 $n-d$개의 원소로 생성된다. 곧 이 차원은 $n-d$ 이하이고, 위의 부등식과 합쳐 등호가 성립하여 $(\ker\overline{d})_\mathfrak{q}=0$이다. $\mathfrak{q}$가 임의였으므로 $\overline{d}$는 단사이다.

역으로 위의 sequence가 split short exact이라 하자. 그럼 $\mathfrak{a}/\mathfrak{a}^2$과 $\Omega_{C/A}$는 모두 rank $n$의 free module $\Omega_{B/A}\otimes_BC$의 direct summand이므로 finitely generated projective이다. 한 점 $x\in X$에 대응하는 prime을 $\mathfrak{q}\subseteq C$, 그 preimage를 $\mathfrak{p}\subseteq B$라 하고 free module $(\mathfrak{a}/\mathfrak{a}^2)_{\mathfrak{q}}$의 rank를 $c$라 하자. 그 기저를 $\mathfrak{a}$의 원소들 $f_1,\ldots, f_c$의 class로 택하면 $\mathfrak{a}_{\mathfrak{p}}=(f_1,\ldots, f_c)_{\mathfrak{p}}+\mathfrak{a}_{\mathfrak{p}}^2$이고, $\varphi$가 locally of finite presentation이라 $\mathfrak{a}$가 finitely generated이므로 [\[가환대수학\] §정수적 확장, ⁋보조정리 8](/ko/math/commutative_algebra/integral_extension#lem8)에 의하여 $\mathfrak{a}_{\mathfrak{p}}=(f_1,\ldots, f_c)_{\mathfrak{p}}$이다. 그럼 어떤 $g\notin\mathfrak{p}$에 대하여 $\mathfrak{a}_g=(f_1,\ldots, f_c)_g$이므로, $X$는 $x$의 근방에서 $X'=\Spec\bigl(B/(f_1,\ldots, f_c)\bigr)$과 open subscheme으로서 일치한다. 한편 split injection은 임의의 base change 뒤에도 단사이므로 $\overline{d}\otimes\kappa(x)$가 단사이고, 이를 기저 $\overline{f_1},\ldots, \overline{f_c}$와 $\dd{\x_1},\ldots, \dd{\x_n}$에 대하여 표현한 행렬이 $x$에서 계산한 Jacobian $(\partial f_i/\partial \x_j)$의 transpose이므로 그 rank는 $c$이다. 따라서 [정리 4](#thm4)에 의하여 $X' \rightarrow S$는 $x$의 어떤 근방에서 smooth하고, 그 근방에서 $X$와 $X'$이 일치하므로 $\varphi$는 $x$에서 smooth하다. $x$가 임의였으므로 $\varphi$는 smooth하다.
:::

Affine 위에서는 언제나 이러한 closed immersion을 택할 수 있고 smoothness는 국소적인 성질이므로, 위의 판정은 임의의 $\varphi$에 대하여 국소적으로 적용된다. 또한 $\overline{d}$의 kernel은 [\[가환대수학\] §미분, ⁋정리 14](/ko/math/commutative_algebra/differentials#thm14)에 의하여 표현의 선택에 무관한 불변량 $H_1(\operatorname{NL}_{C/A})$이므로, [명제 8](#prop8)는 smoothness를 이 $H_1$의 소멸과 $H_0(\operatorname{NL}_{C/A})\cong\Omega_{C/A}$의 projectivity로 옮겨 적은 것이기도 하다. 다만 단사성만으로는 smooth가 되지 않는다. 가령 $C=\mathbb{K}[\x,\y]/(\x\y)$에서 $\mathfrak{a}=(\x\y)$는 nonzerodivisor로 생성되어 $\mathfrak{a}/\mathfrak{a}^2$가 rank $1$의 free module이고 $\overline{d}(\overline{\x\y})=\y \dd{\x}+\x \dd{\y}$를 죽이는 원소는 $(\x)\cap(\y)=0$에 속하므로 $\overline{d}$는 단사이다. 그러나 원점에서 $\overline{d}$를 residue field로 내린 것은 영이 되어 그 image가 direct summand를 이루지 못하며, 실제로 $X$는 원점에서 singular하다.

이렇듯 conormal sequence의 왼쪽 끝에서의 exactness의 실패는 smoothness의 실패를 재는 양이고, naive cotangent complex는 그 sequence를 왼쪽으로 한 항 연장하여 이를 담은 것이다. 이 연장을 모든 degree로 밀고 나가 $\Omega$를 왼쪽으로 유도한 것이 Quillen과 André의 cotangent complex이며, 그 위에서는 [§Kähler differential과 여접층, ⁋명제 1](/ko/math/scheme_theory/sheaf_of_differentials#prop1)의 추이 sequence 또한 오른쪽에서만 exact한 sequence가 아니라 왼쪽으로 이어지는 long exact sequence로 연장된다.

## Unramified morphism

Smooth morphism이 $\Omega_{X/S}$를 fiber 차원만큼 남긴다면, 반대쪽 극단은 그것이 통째로 사라지는 경우이다. Cotangent sheaf $\Omega_{X/S}$는 base $S$ 방향을 상수로 본 $X$의 미분을 담으므로, 이것이 영이라는 것은 $X$가 $S$ 위에서 여분의 무한소 방향을 가지지 않음을 뜻하며, 미분기하의 immersion에 대응하는 것이 이 조건이다.

::: 정의 9
Locally of finite presentation인 scheme morphism $\varphi:X \rightarrow S$가 *unramified<sub>비분기</sub>*하다는 것은 cotangent sheaf가

$$\Omega_{X/S}=0$$

인 것이다.
:::

이 정의는 affine 위에서 곧바로 계산된다. $S=\Spec A$, $X=\Spec B$이면 $\Omega_{X/S}=\widetilde{\Omega_{B/A}}$이므로 ([§Kähler differential과 여접층, ⁋정의 4](/ko/math/scheme_theory/sheaf_of_differentials#def4)), $\varphi$가 unramified한 것은 Kähler differential module $\Omega_{B/A}$가 영인 것과 동치이다. 가령 field 확대 $\mathbb{K} \subseteq \mathbb{L}$이 separable algebraic이면 $\Omega_{\mathbb{L}/\mathbb{K}}=0$이고, 따라서 $\Spec \mathbb{L} \rightarrow \Spec \mathbb{K}$는 unramified하다. 반대로 characteristic $p$에서 $\mathbb{L}=\mathbb{K}(t^{1/p})$와 같은 inseparable 확대는 $\Omega_{\mathbb{L}/\mathbb{K}}\neq 0$을 주어 unramified하지 않다.

Unramified 조건은 diagonal morphism을 통해 좌표 독립적으로 표현된다. Cotangent sheaf 자체가 대각선의 conormal로 정의되므로, 그 소멸은 대각선이 open subscheme이 되는 것과 직접 연결된다.

::: 명제 10
Locally of finite presentation인 morphism $\varphi:X \rightarrow S$에 대하여 다음이 동치이다.

1. $\varphi$는 unramified하다.
2. diagonal morphism $\Delta_\varphi:X \rightarrow X\times_SX$이 ([§값매김환, ⁋정의 3](/ko/math/scheme_theory/valuative_criteria#def3)) open immersion이다.
:::
::: 증명
$\Delta_\varphi$는 항상 immersion, 즉 어떤 open subscheme 위로의 closed immersion이다. 따라서 $\Delta_\varphi$가 open immersion인 것은 그 closed immersion 성분이 isomorphic, 곧 그 image의 ideal sheaf $\mathcal{I}$가 영인 것과 동치이다.

문제는 affine 위에서 국소적이므로 $S=\Spec A$, $X=\Spec B$로 두자. 이 때 $X\times_SX=\Spec(B\otimes_AB)$이고 $\Delta_\varphi$는 곱사상 $\mu:B\otimes_AB \rightarrow B$로부터 온다. $\mathfrak{a}=\ker\mu$라 하면, [§Kähler differential과 여접층, ⁋명제 6](/ko/math/scheme_theory/sheaf_of_differentials#prop6)의 증명에서 보았듯 $\mathfrak{a}/\mathfrak{a}^2\cong \Omega_{B/A}$이다.

이제 $\Omega_{B/A}=0$, 곧 $\mathfrak{a}=\mathfrak{a}^2$임을 가정하자. $B$가 $A$ 위에서 finite presentation이므로 $B\otimes_AB$ 위에서 $\mathfrak{a}$는 finitely generated이고, Nakayama 보조정리의 행렬식 형태에 의하여 $\mathfrak{a}=\mathfrak{a}^2$이면 어떤 $e\in \mathfrak{a}$가 존재하여 $e^2=e$이고 $\mathfrak{a}=(e)$이다. 그럼 $1-e$가 $\mu$의 image를 trivialize하는 idempotent가 되어, $\Delta_\varphi$의 image는 $D(1-e)$ 위에서 열린 동시에 closed subscheme으로 실현된다. 따라서 $\Delta_\varphi$는 open immersion이다.

역으로 $\Delta_\varphi$가 open immersion이면 그 image의 ideal sheaf가 영이므로 $\mathfrak{a}/\mathfrak{a}^2=0$, 곧 $\Omega_{B/A}=0$이고 $\varphi$는 unramified하다.
:::

대각선이 open immersion이라는 조건은 미분기하에서 immersion의 그래프가 곱공간 안에서 국소적으로 닫힌 부분다양체를 이루는 상황의 대수적 그림자이다. 한 점 $x\in X$에서 unramified 조건을 fiber로 옮기면, $s=\varphi(x)$의 residue field $\kappa(s)$ 위의 fiber $X_s$에서 $x$가 $\kappa(s)$의 separable 확대를 residue field로 가지는 isolated point가 된다는 것으로 표현된다. 이렇듯 unramified morphism은 fiber 방향으로 infinitesimal deformation을 허용하지 않는 morphism이다.

## 에탈 사상

미분기하의 covering map은 fiber가 이산적인 submersion, 곧 relative dimension 0의 smooth morphism이다. 대수적 대응물인 étale morphism은 smooth와 unramified를 동시에 요구하여 얻어진다.

::: 정의 11
Locally of finite presentation인 morphism $\varphi:X \rightarrow S$가 *étale<sub>에탈</sub>*하다는 것은 $\varphi$가 smooth하면서 unramified한 것이다.
:::

Smooth morphism에서 $\Omega_{X/S}$는 relative dimension만큼의 rank를 가지는 locally free sheaf이고 ([정리 7](#thm7)), unramified morphism에서는 $\Omega_{X/S}=0$이므로 ([정의 9](#def9)), 두 조건이 함께 성립하면 relative dimension이 $0$이다. 따라서 étale morphism은 relative dimension $0$의 smooth morphism이며, 동치로 다음과 같이 특징지어진다.

::: 명제 12
Locally of finite presentation인 morphism $\varphi:X \rightarrow S$에 대하여 다음이 동치이다.

1. $\varphi$는 étale하다.
2. $\varphi$는 flat하고 unramified하다.
3. $\varphi$는 flat하고 $\Omega_{X/S}=0$이다.
:::
::: 증명
(1)과 (2)의 동치를 보이면 (3)은 unramified의 정의로부터 곧바로 따른다 ([정의 9](#def9)).

(1) $\Rightarrow$ (2)는 정의에 포함되어 있다. $\varphi$가 étale하면 smooth하므로 flat하고, unramified하다.

(2) $\Rightarrow$ (1)을 보이려면 $\varphi$가 flat하고 unramified할 때 geometric fiber가 regular임을 보이면 된다. Unramified 가정에 의하여 $\Omega_{X/S}=0$이고, 따라서 임의의 geometric fiber $X_{\overline{s}}$ 위에서도 base change와 commute하는 cotangent sheaf가 $\Omega_{X_{\overline{s}}/\mathbb{K}}=0$이다. $X_{\overline{s}}$는 algebraically closed field $\mathbb{K}=\overline{\kappa(s)}$ 위에서 locally of finite presentation이므로 그 closed point $z$는 $\mathbb{K}$-point이고, 따라서 $\mathfrak{m}_z/\mathfrak{m}_z^2\cong\Omega_{X_{\overline{s}}/\mathbb{K}}\otimes\kappa(z)=0$이다. [\[가환대수학\] §정수적 확장, ⁋보조정리 8](/ko/math/commutative_algebra/integral_extension#lem8)에 의하여 $\mathfrak{m}_z=0$이므로 $\mathcal{O}_{X_{\overline{s}},z}=\mathbb{K}$는 field이다. 그럼 $z$를 담는 irreducible component가 $\{z\}$뿐이고 나머지 component들의 합집합은 닫혀 있으므로, 그 여집합으로서 $\{z\}$는 열린집합이다. 이 열린집합들의 합집합의 여집합은 closed point를 담지 않는 닫힌집합이라 공집합이므로 ([명제 3](#prop3)의 증명에서 보았듯 공집합이 아닌 닫힌집합은 언제나 closed point를 담는다), $X_{\overline{s}}$는 $\Spec\mathbb{K}$들의 disjoint union이다. 특히 이는 local dimension이 $0$인 reduced scheme이라 regular이다. 그러므로 $\varphi$는 flat하고 geometric fiber가 regular이므로 smooth하며, $\Omega_{X/S}=0$이므로 unramified, 곧 étale하다.
:::

이 명제에 의하여 étale morphism은 "flat한 unramified morphism"이라는 가장 간결한 형태로 다룰 수 있으며, relative dimension $0$이라는 점에서 covering map의 대수적 대응물이다. Étale morphism은 국소적으로 표준적인 모형을 가진다. 이것이 미분기하에서 covering map이 국소적으로 trivial sheet들의 합집합으로 보이는 것에 대응한다.

::: 정의 13
Ring $A$에 대하여, $A$-대수 $B$가

$$B=\bigl(A[t]/(f)\bigr)_g$$

의 꼴이고 monic 다항식 $f\in A[t]$와 $g\in A[t]/(f)$에 대하여 도함수 $f'$의 image가 $B$에서 가역일 때, $\Spec B \rightarrow \Spec A$를 *standard étale<sub>표준 에탈</sub>* morphism이라 부른다.
:::

여기서 $A[t]/(f)$는 monic $f$로 인하여 $A$ 위에서 free module, 따라서 flat하고, localization $(\cdot)_g$ 역시 flat하므로 $B$는 $A$ 위에서 flat하다. 한편 conormal exact sequence에서 $\Omega_{(A[t]/(f))/A}\cong (A[t]/(f))/(f')$이고 $f'$를 가역으로 만드는 localization에서 이 module이 소멸하므로 $\Omega_{B/A}=0$이다. 따라서 standard étale morphism은 실제로 étale하며, 핵심 조건인 $f'$의 가역성은 정확히 $f=0$이 중근을 가지지 않는다는 분리가능성의 대수적 표현이다. Étale morphism은 국소적으로 항상 이 standard 형태를 가진다는 구조 정리가 성립하지만, 그 증명은 본 글의 범위를 넘는다.

::: 예시 14
Separable algebraic field 확대 $\mathbb{K} \subseteq \mathbb{L}$에 대하여 $\Spec \mathbb{L} \rightarrow \Spec \mathbb{K}$는 étale하다. 실제로 primitive element 정리에 의하여 $\mathbb{L}=\mathbb{K}[t]/(f)$이고 $f$가 separable이므로 $f'$가 $\mathbb{L}$에서 가역이다. 따라서 이는 standard étale morphism이며, fiber가 한 점인 covering의 가장 단순한 예이다. 반면 inseparable 확대 $\mathbb{F}_p(t^{1/p}) \supseteq \mathbb{F}_p(t)$는 $\Omega\neq 0$이므로 unramified하지 않고, étale하지도 않다.
:::

::: 예시 15
Field $\mathbb{K}$ 위의 multiplicative group $\mathbb{G}_m=\Spec \mathbb{K}[t, t^{-1}]$에서 자기 자신으로의 $n$제곱 morphism

$$[n]:\mathbb{G}_m \longrightarrow \mathbb{G}_m,\qquad t\longmapsto t^n$$

을 생각하자. 이는 ring homomorphism $\mathbb{K}[s, s^{-1}] \rightarrow \mathbb{K}[t, t^{-1}]$, $s\mapsto t^n$으로부터 온다. 상대미분은 $\dd{(t^n)}=n t^{n-1}\dd{t}$로 생성되므로

$$\Omega_{\mathbb{G}_m/\mathbb{G}_m}\cong \mathbb{K}[t, t^{-1}]/(nt^{n-1})$$

이다. $t$가 가역이므로 이 module은 $\mathbb{K}[t, t^{-1}]/(n)$과 같다. 따라서 $\operatorname{char}\mathbb{K}\nmid n$이면 $n$이 가역이어서 $\Omega=0$이고, $[n]$은 flat하므로 ($\mathbb{K}[t, t^{-1}]$이 $s\mapsto t^n$ 아래 free module이다) étale하다. 반면 $\operatorname{char}\mathbb{K}=p$가 $n$을 나누면 $\Omega\neq 0$이 되어 $[n]$은 unramified하지 않고, $p$에서 ramification이 일어난다. 이는 characteristic $p$에서 Frobenius가 분기를 일으키는 현상의 가장 단순한 사례이다.
:::

위 두 예시는 étale morphism이 "분기 없는 covering"이라는 직관을 구체화한다. Separable 확대와 characteristic을 나누지 않는 거듭제곱 morphism은 fiber가 분기 없이 균일하게 갈라지는 반면, inseparable 확대나 characteristic을 나누는 거듭제곱에서는 fiber가 무너지며 unramified 조건이 깨진다.

## 무한소 lifting 판정

세 개념 smooth, unramified, étale은 square-zero 확대에 대한 morphism의 lifting이라는 통일된 무한소 조건으로 동시에 특징지어진다. 이것이 미분기하에서 smooth morphism이 infinitesimal deformation을 항상 적분할 수 있다는 사실에 대응하며, 좌표나 fiber에 의존하지 않는 가장 개념적인 판정을 준다.

먼저 무대를 설정한다. $T_0\hookrightarrow T$가 affine scheme들의 closed immersion이고, 그 defining ideal $\mathcal{J}$가 $\mathcal{J}^2=0$을 만족할 때 이를 *square-zero extension<sub>제곱영 확대</sub>*이라 부른다. 대수적으로는 surjection $R \rightarrow R_0$의 kernel $\mathfrak{b}$가 $\mathfrak{b}^2=0$을 만족하는 상황이다.

::: 정리 16 (무한소 lifting 판정)
Locally of finite presentation인 morphism $\varphi:X \rightarrow S$가 주어졌다 하자. 임의의 affine $S$-scheme $T$와 그 안의 square-zero closed subscheme $T_0\hookrightarrow T$, 그리고 $S$-morphism $\psi_0:T_0 \rightarrow X$에 대하여, $\psi_0$을 $T$ 위로 확장하는 $S$-morphism $\psi:T \rightarrow X$의 존재·유일성을 다음과 같이 부른다.

{% diagram Math/Scheme_Theory/Smooth_and_Etale_Morphisms-3.svg width="6.05em" alt="lifting diagram" %}

그럼 다음이 성립한다.

1. $\varphi$가 smooth한 것은 모든 그러한 $(T_0, T, \psi_0)$에 대하여 lifting $\psi$가 존재하는 것과 동치이다.
2. $\varphi$가 unramified한 것은 모든 그러한 $(T_0, T, \psi_0)$에 대하여 lifting $\psi$가 많아야 하나인 것과 동치이다.
3. $\varphi$가 étale한 것은 모든 그러한 $(T_0, T, \psi_0)$에 대하여 lifting $\psi$가 정확히 하나 존재하는 것과 동치이다.
:::
::: 증명
(3)은 (1)과 (2)의 결합이고, étale이 smooth와 unramified의 교집합이므로 ([정의 11](#def11)) (1)과 (2)만 보이면 충분하다.

핵심은 두 lifting의 차이가 $\Omega_{X/S}$로 측정된다는 사실이다. $T=\Spec R$, $T_0=\Spec R_0$이고 $\mathfrak{b}=\ker(R \rightarrow R_0)$가 $\mathfrak{b}^2=0$을 만족한다 하자. 문제가 affine 위에서 국소적이므로 $X=\Spec C$라 하자. $\psi_0$의 두 lifting $\psi, \psi'$가 주어지면, 대응하는 ring homomorphism $C \rightarrow R$의 차이 $D=\psi^\sharp-\psi'^\sharp:C \rightarrow \mathfrak{b}$는 $\mathfrak{b}^2=0$에 의하여 $A$-derivation이 된다. 실제로 $\psi, \psi'$이 mod $\mathfrak{b}$로 일치하므로 임의의 $c, c'\in C$에 대하여

$$D(cc')=\psi(c)\psi(c')-\psi'(c)\psi'(c')=\psi(c)D(c')+D(c)\psi'(c')\equiv \psi_0(c)D(c')+D(c)\psi_0(c')\pmod{\mathfrak{b}^2}$$

이고, $\mathfrak{b}^2=0$이므로 이는 정확히 Leibniz rule이다. 따라서 두 lifting의 차이는 $\Der_A(C, \mathfrak{b})\cong \Hom_C(\Omega_{C/A}, \mathfrak{b})$의 원소들과 일대일 대응한다. ([§Kähler differential과 여접층, ⁋정의 4](/ko/math/scheme_theory/sheaf_of_differentials#def4)에서 $\Omega_{X/S}=\widetilde{\Omega_{C/A}}$이고, derivation의 표현성에 의한다.)

이로부터 (2)를 얻는다. $\varphi$가 unramified하면 $\Omega_{C/A}=0$이므로 $\Hom_C(\Omega_{C/A}, \mathfrak{b})=0$이고, 따라서 두 lifting의 차이가 항상 영, 곧 lifting은 많아야 하나이다. 역으로 lifting이 항상 많아야 하나이면, $T_0=X$, $T=X[\epsilon]$를 $\Omega_{X/S}$의 dual로 만든 표준 square-zero 확대로 택하여 두 자명한 lifting이 일치해야 함을 보이면 $\Der_A(C, \Omega_{C/A})$의 항등원이 영이 되어 $\Omega_{C/A}=0$이 강제된다. 따라서 $\varphi$는 unramified하다.

(1)을 보인다. $\varphi$가 smooth하다 하자. Lifting의 obstruction은 다음과 같이 분석된다. $\psi_0^\sharp:C \rightarrow R_0$이 주어졌을 때 이를 $C \rightarrow R$로 들어올리려면, $C$의 generator의 image를 $R$로 임의로 올린 뒤 그것이 $C$의 relation을 만족하도록 $\mathfrak{b}$ 안에서 수정해야 한다. 이 수정의 가능 여부가 $\Omega_{C/A}$가 locally free라는 사실로 통제된다. $C$를 $B=A[\x_i]$의 quotient $B/\mathfrak{a}$로 표시하면, $B \rightarrow R$로의 lifting은 free polynomial ring이므로 항상 존재하고, 그것이 $\mathfrak{a}$를 $0$으로 보내도록 $\Hom(\mathfrak{a}/\mathfrak{a}^2, \mathfrak{b})$ 안에서 수정 가능한지가 문제이다. Smooth 가정에서 conormal exact sequence

$$\mathfrak{a}/\mathfrak{a}^2 \rightarrow \Omega_{B/A}\otimes C \rightarrow \Omega_{C/A} \rightarrow 0$$

이 좌측에서도 split되므로 ([명제 8](#prop8)) short exact sequence로 분해되고, 이 split이 정확히 원하는 수정을 제공하여 lifting $\psi$가 존재한다.

역으로 모든 square-zero 확대에 대하여 lifting이 존재한다 하자. 이 lifting property를 $T_0=X$ 위의 conormal 확대 $\Spec(B/\mathfrak{a}^2)$에 항등사상 $\psi_0=\id_X$와 함께 적용하면 $B/\mathfrak{a}^2 \rightarrow C$의 $A$-대수 section을 얻고, 이로부터 conormal exact sequence $\mathfrak{a}/\mathfrak{a}^2 \rightarrow \Omega_{B/A}\otimes C \rightarrow \Omega_{C/A} \rightarrow 0$의 좌측 morphism이 split injection이 된다. 그러므로 [명제 8](#prop8)에 의하여 $\varphi$는 smooth하다.
:::

이 판정은 세 개념을 한 그림 안에 통합한다. infinitesimal deformation $T_0\hookrightarrow T$를 따라 $X$로의 morphism을 항상 적분할 수 있으면 smooth, 그 적분이 많아야 한 가지 방법으로만 가능하면 unramified, 정확히 한 가지로 가능하면 étale이다. 특히 étale morphism의 lifting이 유일하다는 것은 covering map 위에서 경로를 들어올리는 방법이 유일하다는 위상적 사실의 대수적 대응이며, 이것이 étale morphism이 대수기하에서 분기 없는 covering과 fundamental group 이론의 토대가 되는 이유이다.

세 조건은 모두 base change와 합성에 대해 안정적이다. Smooth morphism의 base change는 다시 smooth하고, smooth morphism들의 합성도 smooth하며, unramified와 étale에 대해서도 마찬가지이다. 이는 위 lifting 판정이 순수하게 morphism 도식의 성질로 표현되어 있어 base change와 합성 아래에서 그대로 보존되기 때문이다.

---

**참고문헌**

**[Har]** R. Hartshorne, *Algebraic geometry*. Graduate Texts in Mathematics. Springer, 1977.  
**[Vak]** R. Vakil, *The rising sea: Foundations of algebraic geometry*. Available [online](https://math.stanford.edu/~vakil/216blog/).
