---
title: "매끄러운 사상과 étale 사상"
description: "스킴 사상의 매끄러움을 flat이면서 모든 기하적 올이 정칙인 유한표시 사상으로 정의하고, cotangent sheaf가 상대차원만큼의 국소자유층임과 동치임을 본다. Unramified 사상을 대각선이 열린 immersion인 경우로 특징짓고, étale 사상을 매끄럽고 unramified한 상대차원 0의 사상으로 도입하며 standard étale 모형과 Jacobian 판정, square-zero 확대에 대한 무한소 lifting 판정을 다룬다."
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

우리는 본질적으로 cotangent sheaf가 주는 exact sequence들은 *right* exact이기만 하다는 것을 살펴보았다. ([§Kähler 미분과 여접층, ⁋명제 6](/ko/math/scheme_theory/sheaf_of_differentials#prop6) 이후의 exact sequence들) 이러한 정보의 손실을 막기 위해서는 morphism에 특수한 조건을 부여해야 하는데, 그것이 smooth morphism의 동기이다. 반대쪽 극단은 $\Omega_{X/S}$가 통째로 소멸하는 경우로, 우리는 이를 *unramified* morphism이라 부른다. 마지막으로 우리는 smooth unramified morphism인 *étale* morphism을 정의한다. 

우리는 이 글 전체에서 morphism이 *locally of finite presentation*임을 기본 가정으로 둔다. 이는 (대부분의 관심사인) locally Noetherian base 위에서는 이것이 locally of finite type과 일치하므로 직관적으로는 이렇게 생각해도 무방하다. 

## 매끄러운 사상

Smooth morphism은 fiber가 base 위에서 균일하게 regular family를 이루는 morphism이다. 이를 가장 간단하게 정의할 방법은 각 점 $s\in S$ 위의 fiber $X_s=X\times_S\Spec\kappa(s)$가 singular point를 가지지 않는다는 조건을 부여하는 것이다. 즉, 임의의 점에서 접방향이 fiber 차원을 넘어가서는 안되며, 이를 해당 점에서의 대수적인 언어로 풀어쓰면 Noetherian local ring $(A, \mathfrak{m})$에서의 부등식 $\dim A\leq \dim_{A/\mathfrak{m}}\mathfrak{m}/\mathfrak{m}^2$의 등호가 성립해야 한다는 조건, 즉  $A$가 regular local ring이라는 것으로 해석할 수 있다. ([\[가환대수학\] §차원, ⁋정의 12](/ko/math/commutative_algebra/Krull_dimension#def12)) 

문제는 이것이 family의 성질이 되기 위해서는 이것이 base change에 대해 잘 행동해야 하는데, 일반적으로 그렇지 않다는 것이다. 즉, 위와 같이 명시적으로 fiber $X_s$의 각 점에서의 regularity를 요구하는 것은 base change에 대해 취약하며, 이를 위해서는 field $\kappa(s)$의 algebraic closure $\overline{\kappa(s)}$로 계수를 올려준 *geometric fiber* $X\times_S\Spec\overline{\kappa(s)}$를 생각하면 된다는 사실이 알려져 있다. 그러나 이 사실에 대한 증명은 그렇게 가볍지는 않으므로, 우리는 이를 motivation으로만 활용하고 바로 다음의 정의를 도입하기로 한다. 

::: 정의 1
Locally of finite presentation인 scheme morphism $\varphi:X \rightarrow S$가 *smooth<sub>매끄러운</sub>*하다는 것은 다음 두 조건이 성립하는 것이다.

1. $\varphi$는 flat하다. ([§평탄사상, ⁋정의 1](/ko/math/scheme_theory/flat_morphisms#def1))
2. 임의의 $s\in S$에 대하여, residue field $\kappa(s)$의 algebraic closure $\overline{\kappa(s)}$ 위의 geometric fiber

   $$X_{\bar s}=X\times_S\Spec\overline{\kappa(s)}$$

   는 regular scheme이다. 즉 그 모든 local ring이 regular local ring이다.
:::

이 정의에서 두 조건은 서로 다른 방향을 통제한다. Flatness는 fiber들이 base를 따라 차원 도약 없이 연속적으로 변함을 보장하고 ([§평탄사상, ⁋명제 17](/ko/math/scheme_theory/flat_morphisms#prop17)), geometric fiber의 regularity는 각 fiber 자체가 singular point를 가지지 않음을 보장한다.

Smooth morphism은 cotangent sheaf의 local freeness로 적어줄 수도 있으며, 이것이 가장 중요한 smooth morphism의 characterization이다. 이를 위해 우선 scheme $Y$와 그 점 $y\in Y$에 대하여, $y$에서의 *국소차원<sub>local dimension</sub>* $\dim_yY$를 $y$를 포함하는 irreducible component들의 차원의 supremum으로 정의하자. 그럼 정의에 의해 $Y$의 전체 차원은 이들의 supremum $\dim Y=\sup_{y\in Y}\dim_yY$이며, 만일 $Y$가 irreducible이면 모든 점이 유일한 irreducible component 위에 놓이므로 $\dim_yY=\dim Y$가 성립한다. 더 일반적으로 모든 irreducible component의 차원이 같은 *equidimensional* scheme에서도 그러하다. 이것이 성립하며, 이 개념은 새로운 것이 아니라 평면과 직선의 합집합 $Y=V(\x\z,\y\z)\subseteq\mathbb{A}^3_\mathbb{K}$에서 서로 차원이 다른 두 성분을 다루기 위한 언어일 뿐이다. 

한편 $Y$가 field 위에서 finite type이면 그 closed point $z$에서는 [\[가환대수학\] §뇌터 정규화, ⁋정리 4](/ko/math/commutative_algebra/noether_normalization#thm4)의 차원 공식에 의하여 $\dim\mathcal{O}_{Y,z}=\dim_zY$가 성립한다.

::: 정리 2
Locally of finite presentation인 morphism $\varphi:X \rightarrow S$에 대하여 다음이 동치이다.

1. $\varphi$는 smooth하다.
2. $\varphi$는 flat하고, $\Omega_{X/S}$는 locally free sheaf이며, 각 $x\in X$에서 그 rank가 $s=\varphi(x)$ 위 fiber의 국소차원 $\dim_x X_s$와 같다.

이 때 $\Omega_{X/S}$의 rank를 $\varphi$의 *상대차원<sub>relative dimension</sub>*이라 부른다.
:::
::: 증명
문제가 국소적이므로 $S=\Spec A$, $X=\Spec B$이고 한 점 $x$에 해당하는 prime $\mathfrak{p}\subseteq B$ 근방에서 작업한다. $s=\varphi(x)$에 해당하는 prime을 $\mathfrak{q}\subseteq A$라 하자.

먼저 $\varphi$가 smooth하다고 가정하고 $\Omega_{X/S}$의 $x$에서의 fiber 차원을 계산한다. Cotangent sheaf는 base change와 commute하므로 $\mathbb{K}=\overline{\kappa(s)}$ 위의 geometric fiber에서 $\Omega_{X_{\bar s}/\mathbb{K}}$는 $\Omega_{X/S}$의 pullback이고, $X_{\bar s} \rightarrow X_s$가 전사이므로 $x$ 위의 점 $\bar x$를 택하면

$$\dim_{\kappa(x)}\bigl(\Omega_{X/S}\otimes \kappa(x)\bigr)=\dim_{\kappa(\bar x)}\bigl(\Omega_{X_{\bar s}/\mathbb{K}}\otimes \kappa(\bar x)\bigr)$$

이 성립한다. 곧 우변을 regular scheme $X_{\bar s}$ 위에서 계산하면 된다.

우선 closed point에서 본다. $X_{\bar s}$가 algebraically closed field $\mathbb{K}$ 위에서 locally of finite presentation이므로 그 closed point $z$의 residue field는 $\mathbb{K}$의 유한확대, 곧 $\kappa(z)=\mathbb{K}$이다. ([\[가환대수학\] §영점정리, ⁋정리 4](/ko/math/commutative_algebra/nullstellensatz#thm4)) 이러한 $\mathbb{K}$-rational point에서는 $\Omega_{X_{\bar s}/\mathbb{K}}\otimes\kappa(z)\cong\mathfrak{m}_z/\mathfrak{m}_z^2$이 성립하므로 ([§Kähler 미분과 여접층, ⁋정의 8](/ko/math/scheme_theory/sheaf_of_differentials#def8) 직후의 관찰), $\mathcal{O}_{X_{\bar s},z}$가 regular local ring이라는 것은 정확히

$$\dim_{\kappa(z)}\bigl(\Omega_{X_{\bar s}/\mathbb{K}}\otimes \kappa(z)\bigr)=\dim \mathcal{O}_{X_{\bar s},z}$$

를 뜻한다. ([\[가환대수학\] §정칙국소환](/ko/math/commutative_algebra/regular_local_rings)의 regular local ring은 그 정의상 $\mathfrak{m}$이 $\dim$개의 원소로 생성되며, 이는 $\dim\mathfrak{m}/\mathfrak{m}^2=\dim$과 동치이다.) 게다가 $z$가 closed point이므로 차원 공식에 의하여 우변은 국소차원 $\dim_zX_{\bar s}$와 같다. 반면 non-closed point $\bar x$에서는 $\dim\mathcal{O}_{X_{\bar s},\bar x}$가 codimension이라 국소차원보다 작을 수 있으므로 이 계산을 그대로 옮길 수 없고, 남은 점들은 반연속성으로 처리해야 한다.

$X_{\bar s}$의 local ring들은 regular, 특히 domain이므로 ([\[가환대수학\] §정칙국소환, ⁋따름정리 1](/ko/math/commutative_algebra/regular_local_rings#cor1)) 서로 다른 irreducible component는 만나지 않는다. 곧 각 component는 열린 동시에 닫힌집합이고 그 위에서 국소차원은 일정하므로, $\bar x$를 담는 component를 $Z$, $d=\dim Z$라 하자. 이제

$$\mu(v)=\dim_{\kappa(v)}\bigl(\Omega_{X_{\bar s}/\mathbb{K}}\otimes \kappa(v)\bigr)$$

로 두면 $\mu$는 upper semicontinuous이다. ([§평탄사상, ⁋명제 22](/ko/math/scheme_theory/flat_morphisms#prop22)) 한편 $X_{\bar s}$의 공집합이 아닌 열린집합이나 닫힌집합은 언제나 $X_{\bar s}$의 closed point를 담는다. 그러한 부분집합에 reduced 구조를 주면 이 또한 $\mathbb{K}$ 위에서 locally of finite type이라 그 affine open의 maximal ideal이 한 점을 주고, 그 점의 residue field가 $\mathbb{K}$의 유한확대이므로 $X_{\bar s}$ 안에서의 closure가 $0$차원, 곧 그 점 자신이기 때문이다. ([\[가환대수학\] §뇌터 정규화, ⁋정리 3](/ko/math/commutative_algebra/noether_normalization#thm3)) 그럼 $\overline{\{\bar x\}}$ 안의 closed point $z$를 택하면 closed point에서의 계산이 $\mu(z)=\dim_zX_{\bar s}=d$를 주고, 열린집합 $\{\mu\leq d\}$가 $z$를 담으므로 $\bar x$도 담아 $\mu(\bar x)\leq d$이다. 거꾸로 열린집합 $\{\mu\leq\mu(\bar x)\}$와 $Z$의 교집합 안의 closed point $z'$을 택하면 $d=\mu(z')\leq\mu(\bar x)$이므로, 결국 $\mu(\bar x)=d=\dim_{\bar x}X_{\bar s}$이다.

마지막으로 이를 $X_s$로 내린다. Algebraic 확대가 주는 $\Spec\mathbb{K} \rightarrow \Spec\kappa(s)$가 integral이고 integral morphism은 base change로 보존되므로 ([§올곱, ⁋명제 16](/ko/math/scheme_theory/fiber_products#prop16)) $X_{\bar s} \rightarrow X_s$는 integral 전사이다. 그럼 $\bar x$를 담는 $X_{\bar s}$의 component는 그 image의 closure 위로 가는 dominant한 integral morphism을 주어 [§차원, ⁋명제 5](/ko/math/scheme_theory/dimension#prop5)에 의하여 그 closure와 차원이 같고, 이 closure는 $x$를 담는 어떤 component 안에 들어가므로 $\dim_{\bar x}X_{\bar s}\leq\dim_xX_s$이다. 거꾸로 $x$를 담는 $X_s$의 component $W$를 잡으면 $\bar x$는 base change $W\times_{\Spec\kappa(s)}\Spec\mathbb{K}$에 속하고, 이 scheme의 각 component는 $W$의 generic point 위로 간다. ($W$가 integral이라 그 위로의 integral extension이 단사이므로 minimal prime이 minimal prime 위로 간다. [\[가환대수학\] §정수적 확장과 아이디얼, ⁋따름정리 4](/ko/math/commutative_algebra/lying_over_and_going_up#cor4)) 따라서 다시 [§차원, ⁋명제 5](/ko/math/scheme_theory/dimension#prop5)에 의하여 이들의 차원은 $\dim W$이며, $\bar x$를 담는 것 하나를 택하면 그것을 담는 $X_{\bar s}$의 component가 $\bar x$를 지나 $\dim_{\bar x}X_{\bar s}\geq\dim W$이다. $W$가 임의였으므로 $\dim_{\bar x}X_{\bar s}=\dim_xX_s$이고, 따라서 $\Omega_{X/S}$의 $x$에서의 fiber 차원은 $\dim_xX_s$이다.

이제 flatness와 결합한다. $\varphi$가 flat이고 $\Omega$의 fiber 차원이 국소상수이므로, 유한표시 module에 대한 국소자유성 판정에 의하여 $\Omega_{X/S}$는 $\mathfrak{p}$ 근방에서 그 차원만큼의 rank를 가지는 locally free sheaf이다. 구체적으로 $\Omega_{B/A}$는 finitely presented $B$-module이고, $\varphi$가 flat이고 $\dim_{\kappa(x)}\Omega_{B/A}\otimes\kappa(x)$가 국소상수이므로 $\Omega_{B/A}$는 projective module, 곧 국소자유이다 (유한표시·flat module의 fiber rank가 국소상수이면 국소자유, Stacks 00NX). 그 rank가 fiber 차원과 같음은 위 계산에서 따른다.

역으로 두 번째 조건을 가정하자. $\Omega_{X/S}$가 국소자유이고 그 rank가 fiber의 국소차원과 같으면, 앞의 base change 계산에 의하여 각 geometric fiber $X_{\bar s}$ 위에서도 $\Omega_{X_{\bar s}/\mathbb{K}}$의 fiber 차원이 국소차원과 일치한다. 여기서도 closed point에서 출발한다. $X_{\bar s}$의 closed point $z$는 $\mathbb{K}$-rational이라 $\Omega_{X_{\bar s}/\mathbb{K}}\otimes\kappa(z)\cong\mathfrak{m}_z/\mathfrak{m}_z^2$이고 차원 공식이 $\dim_zX_{\bar s}=\dim\mathcal{O}_{X_{\bar s},z}$를 주므로

$$\dim_{\kappa(z)}\mathfrak{m}_z/\mathfrak{m}_z^2=\dim_zX_{\bar s}=\dim\mathcal{O}_{X_{\bar s},z}$$

이 되어 $\mathcal{O}_{X_{\bar s},z}$는 regular local ring이다. 이제 임의의 점 $\bar x\in X_{\bar s}$에 대하여 $\overline{\{\bar x\}}$ 안의 closed point $z$를 택하면, $z$의 열린근방은 모두 $\bar x$를 담으므로 $\mathcal{O}_{X_{\bar s},\bar x}$는 $\mathcal{O}_{X_{\bar s},z}$의 localization이다. Regular local ring의 localization은 regular이므로 ([\[가환대수학\] §정칙성의 호몰로지 판정, ⁋따름정리 4](/ko/math/commutative_algebra/homological_criterion_for_regularity#cor4)) $\mathcal{O}_{X_{\bar s},\bar x}$ 또한 regular local ring이다. 따라서 geometric fiber가 regular이고, 가정에 의해 $\varphi$가 flat이므로 $\varphi$는 smooth하다.
:::

이 동치성에 의하여 smooth morphism은 fiber다발처럼 다룰 수 있다. $\Omega_{X/S}$가 rank $r$의 locally free sheaf라는 것은 $X$가 국소적으로 $S$ 위의 $r$차원 affine space처럼 보인다는 직관을 정확히 표현한다. 실제로 가장 기본적인 예는 affine space로의 projection이며, $\mathbb{A}^r_S \rightarrow S$는 flat하고 $\Omega_{\mathbb{A}^r_S/S}\cong \mathcal{O}^{\oplus r}$이므로 ([§Kähler 미분과 여접층, ⁋명제 9](/ko/math/scheme_theory/sheaf_of_differentials#prop9)) 상대차원 $r$의 smooth morphism이다.

일반적인 smooth morphism은 국소적으로 affine space 안에서 Jacobian이 최대 rank를 가지는 방정식들로 잘린 것으로 기술된다. 이것이 미분기하의 implicit function theorem에 대응하는 대수적 판정이며, smooth 여부를 좌표 계산으로 확인하게 해 준다.

::: 정리 3 (Jacobian 판정)
$S=\Spec A$ 위에서

$$X=\Spec\bigl(A[\x_1,\ldots, \x_{n}]/(f_1,\ldots, f_r)\bigr)$$

이라 하고, $x\in X$를 한 점이라 하자. $x$에서 Jacobian 행렬

$$J=\Bigl(\frac{\partial f_i}{\partial \x_j}\Bigr)_{\substack{1\leq i\leq r\\ 1\leq j\leq n}}$$

의 $\kappa(x)$ 위에서의 rank가 $r$이면, $\varphi:X \rightarrow S$는 $x$의 어떤 열린 근방에서 상대차원 $n-r$의 smooth morphism이다.
:::
::: 증명
[정리 2](#thm2)에 의하여 우리가 보여야 할 것은 $x$의 어떤 근방 위에서 $\varphi$가 flat하고 $\Omega_{X/S}$가 rank $n-r$의 locally free sheaf이며, 그 근방의 각 점에서 fiber의 국소차원이 $n-r$이라는 것이다. 먼저 $\Omega$를 기술하기 위해 $B=A[\x_1,\ldots, \x_n]/(f_1,\ldots, f_r)$, $P=A[\x_1,\ldots, \x_n]$이라 하고 $\mathfrak{a}=(f_1,\ldots, f_r)$라 하자. Closed immersion $X\hookrightarrow \mathbb{A}^n_S$의 conormal exact sequence는 ([§Kähler 미분과 여접층, ⁋명제 2](/ko/math/scheme_theory/sheaf_of_differentials#prop2))

$$\mathfrak{a}/\mathfrak{a}^2 \overset{\bar d}{\longrightarrow} \Omega_{P/A}\otimes_PB \longrightarrow \Omega_{B/A} \longrightarrow 0$$

이며, $\Omega_{P/A}\otimes_PB$는 $\dd{\x_1},\ldots, \dd{\x_n}$을 기저로 하는 rank $n$의 자유 $B$-module이다. ([§Kähler 미분과 여접층, ⁋명제 9](/ko/math/scheme_theory/sheaf_of_differentials#prop9)) Morphism $\bar d$는 $f_i+\mathfrak{a}^2\mapsto \dd{f_i}=\sum_j(\partial f_i/\partial \x_j)\dd{\x_j}$로 주어진다. 한편 $\mathfrak{a}$가 $f_1,\ldots, f_r$로 생성되므로 $e_i\mapsto f_i+\mathfrak{a}^2$은 전사사상 $\pi:B^{\oplus r} \rightarrow \mathfrak{a}/\mathfrak{a}^2$을 정의하며, 합성 $\bar d\circ\pi$를 $e_i$와 $\dd{\x_j}$ 기저에 대하여 표현한 행렬이 정확히 Jacobian $J$의 transpose이다.

이 행렬 표현으로부터 첫 번째 목표인 국소자유성이 얻어진다. 가정에 의하여 $J$의 어떤 $r\times r$ 소행렬식 $g$가 $x$에서 영이 아니다. $D(g)=\Spec B_g$ 위에서는 해당 부분행렬이 가역이므로, 그 $r$개 좌표로의 projection과 $(\bar d\circ\pi)_g$의 합성이 $B_g^{\oplus r}$의 가역 endomorphism이 되어 $(\bar d\circ\pi)_g$는 split injection이다. 특히 $\pi_g$는 단사이고 이미 전사였으므로 동형이며, 따라서 $(\mathfrak{a}/\mathfrak{a}^2)_g$는 rank $r$의 자유 module이고 $\bar d_g$는 자유 module 사이의 split injection이다. 그럼 그 cokernel $\Omega_{B/A}\otimes_BB_g$는 $B_g^{\oplus n}$의 direct summand이므로, $\Omega_{B/A}$는 $D(g)$ 위에서 rank $n-r$의 국소자유이다.

다음 목표는 $\varphi$가 $x$의 어떤 근방에서 flat하다는 것이다. 이하의 논증이 Noetherian 가정을 요구하므로 먼저 일반의 $A$를 그 경우로 줄인다. $f_1,\ldots, f_r$의 계수들이 $A$ 안에서 생성하는 $\mathbb{Z}$-subalgebra를 $A_0$이라 하면 $A_0$은 Noetherian이고 ([\[가환대수학\] §기본 개념들, ⁋정리 12](/ko/math/commutative_algebra/basic_notions#thm12)), $B_0=A_0[\x_1,\ldots, \x_n]/(f_1,\ldots, f_r)$로 두면 $B=B_0\otimes_{A_0}A$이다. $\Spec B \rightarrow \Spec B_0$에 의한 $x$의 image를 $x_0$이라 하면 $J$의 $x$에서의 성분들은 $x_0$에서의 성분들의 image이고 행렬의 rank는 field 확대로 변하지 않으므로, $x_0$에서도 $J$의 rank는 $r$이다. Flatness가 base change로 보존되므로 ([§평탄사상, ⁋명제 3](/ko/math/scheme_theory/flat_morphisms#prop3)), $\Spec B_0 \rightarrow \Spec A_0$이 $x_0$의 근방에서 flat이면 $\varphi$도 $x$의 근방에서 flat이다. 따라서 $A$가 Noetherian이라 가정한다.

Flatness는 local criterion of flatness로 보일 것인데, 이 판정이 요구하는 것은 $f_i$들을 fiber로 내린 것들이 regular sequence를 이룬다는 사실이다. 이를 위해 $s=\varphi(x)$라 하고, $x$를 fiber $\mathbb{A}^n_{\kappa(s)}$의 점으로 볼 때의 local ring을 $R$, 그 maximal ideal을 $\mathfrak{m}$이라 하자. Polynomial ring $\kappa(s)[\x_1,\ldots, \x_n]$이 regular ring이므로 ([\[가환대수학\] §정칙성의 호몰로지 판정, ⁋따름정리 6](/ko/math/commutative_algebra/homological_criterion_for_regularity#cor6)) $R$은 residue field $\kappa(x)$를 가지는 regular local ring이다. $x\in X$이므로 $f_i$를 fiber로 내린 $\bar f_i$는 $\mathfrak{m}$에 속하며, Leibniz 규칙에 의하여 $h\mapsto \sum_j(\partial h/\partial \x_j)(x)\dd{\x_j}$가 $\mathfrak{m}^2$을 소멸시키므로 $\kappa(x)$-linear map $\mathfrak{m}/\mathfrak{m}^2 \rightarrow \kappa(x)^{\oplus n}$이 유도된다. 이 map은 $\bar f_i$의 class를 $J$의 $i$번째 행으로 보내고 가정에 의하여 그 행들이 일차독립이므로, $\bar f_1,\ldots, \bar f_r$의 class들도 $\mathfrak{m}/\mathfrak{m}^2$ 안에서 일차독립이다. 이 class들을 $\mathfrak{m}/\mathfrak{m}^2$의 기저로 확장하고 Nakayama 보조정리를 적용하면 ([\[가환대수학\] §정수적 확장, ⁋보조정리 8](/ko/math/commutative_algebra/integral_extension#lem8)) $\mathfrak{m}$을 생성하는 $\dim R$개의 원소를 얻으므로, $\bar f_1,\ldots, \bar f_r$은 $R$의 regular system of parameters의 앞부분이다. [\[가환대수학\] §정칙국소환, ⁋따름정리 3](/ko/math/commutative_algebra/regular_local_rings#cor3)에 의하여 regular system of parameters 전체가 $R$-sequence이므로, 그 앞부분인 $\bar f_1,\ldots, \bar f_r$ 또한 $R$-regular sequence이다.

이제 이 fiber 조건을 base 방향으로 들어올린다. $P$가 $A$ 위에서 free이므로 $\mathbb{A}^n_S \rightarrow S$는 flat이고 ([§평탄사상, ⁋보조정리 2](/ko/math/scheme_theory/flat_morphisms#lem2)), $A$가 Noetherian이므로 $\mathcal{O}_{S,s} \rightarrow \mathcal{O}_{\mathbb{A}^n_S,x}$는 Noetherian local ring 사이의 flat local homomorphism이며, 이를 $\mathcal{O}_{S,s}$의 maximal ideal로 나눈 것이 $R$이다. 그럼 $\bar f_1,\ldots, \bar f_r$이 $R$-regular sequence라는 것으로부터, local criterion of flatness에 의하여 $f_1,\ldots, f_r$은 $\mathcal{O}_{\mathbb{A}^n_S,x}$의 regular sequence이고 quotient $\mathcal{O}_{X,x}$는 $\mathcal{O}_{S,s}$ 위에서 flat이다. (Stacks 00MG) [§평탄사상, ⁋정의 1](/ko/math/scheme_theory/flat_morphisms#def1)의 의미에서 $\varphi$는 $x$에서 flat이므로 [§평탄사상, ⁋정리 20](/ko/math/scheme_theory/flat_morphisms#thm20)에 의하여 $x$의 어떤 열린근방 위에서 flat하다.

마지막으로 남은 것은 fiber의 국소차원이다. 앞의 근방과 $D(g)$의 교집합을 $U$라 하면 $U$ 위에서 $\varphi$는 flat하고 $\Omega_{B/A}$는 rank $n-r$의 국소자유이므로, [정리 2](#thm2)를 적용하기 위해 보여야 할 것은 $U$의 각 점에서 fiber의 국소차원이 $n-r$이라는 것이다. 이는 위의 fiber 논증을 $U$의 다른 점에서 반복하여 얻는다. $U$의 점 $y$와 $s'=\varphi(y)$에 대하여 fiber $X_{s'}$의 $y$를 지나는 component의 generic point를 $\eta$라 하면, $g$가 $\eta$에서도 가역이어서 $J$의 rank가 $r$이므로, 같은 논증에 의하여 $\bar f_1,\ldots, \bar f_r$의 class들은 regular local ring $\mathcal{O}_{\mathbb{A}^n_{\kappa(s')},\eta}$의 $\mathfrak{m}_\eta/\mathfrak{m}_\eta^2$ 안에서 일차독립이다. 곧 그 component의 codimension인 $\dim\mathcal{O}_{\mathbb{A}^n_{\kappa(s')},\eta}$는 $r$ 이상이고, $\eta$가 $(\bar f_1,\ldots, \bar f_r)$을 포함하는 minimal prime이므로 [\[가환대수학\] §차원, ⁋정리 7](/ko/math/commutative_algebra/Krull_dimension#thm7)이 반대 부등식을 주어 codimension은 정확히 $r$이며, 차원 공식에 의하여 ([\[가환대수학\] §뇌터 정규화, ⁋정리 4](/ko/math/commutative_algebra/noether_normalization#thm4)) component의 차원은 $n-r$이다. 따라서 $U$의 각 점에서 fiber의 국소차원이 rank와 일치하고, [정리 2](#thm2)에 의하여 $\varphi$는 상대차원 $n-r$의 smooth morphism이다.
:::

증명의 fiber 단계에서 얻은 regular sequence는 한 점 $x$에서의 조건이지만 근방으로 퍼진다. 각 $i$에 대하여 $\bar f_{i+1}$의 곱셈이 $\kappa(s)[\x_1,\ldots, \x_n]/(\bar f_1,\ldots, \bar f_i)$에 만드는 kernel은 finitely generated이고 $x$에서의 stalk이 $0$이므로 $x$를 담는 어떤 principal open 위에서 소멸한다. 이 principal open들의 교집합을 $D(h)\subseteq \mathbb{A}^n_{\kappa(s)}$라 하면 그 위에서 $\bar f_1,\ldots, \bar f_r$은 regular sequence를 이루고, $X_s\cap D(h)\hookrightarrow D(h)$는 codimension $r$의 complete intersection이다. ([§완전교차, ⁋정의 1](/ko/math/scheme_theory/complete_intersections#def1)) 곧 Jacobian 조건 아래에서 $\varphi$의 fiber는 국소적으로 complete intersection이다.

Jacobian 판정은 smooth 여부를 미분 계산으로 환원하므로 실용적으로 가장 자주 쓰인다. 가령 $\Spec\mathbb{Z}[\x,\y]/(\y^2-\x^3-\x)$ 위에서 $f=\y^2-\x^3-\x$의 Jacobian은 $(\partial f/\partial\x, \partial f/\partial\y)=(-3\x^2-1, 2\y)$이며, 이 두 성분이 동시에 영이 되는 점이 base의 어떤 소수에서 나타나는지를 보면 곡선이 그 소수에서 smooth fiber를 가지는지를 판정할 수 있다.

Jacobian 판정의 증명에서 실제로 쓰인 것은 conormal exact sequence의 왼쪽 morphism이 단사라는 것을 넘어 split injection이 된다는 사실이었다. 이 성질은 택한 방정식 표현에 딸린 우연이 아니라 smoothness 자체와 동치이다.

::: 명제 4
$S=\Spec A$ 위의 closed immersion $X\hookrightarrow \mathbb{A}^n_S$이 주어졌다 하고, $P=A[\x_1,\ldots, \x_n]$, 그 정의 ideal을 $\mathfrak{a}\subseteq P$, $B=P/\mathfrak{a}$라 하자. 그럼 $\varphi:X \rightarrow S$가 smooth한 것은 conormal exact sequence가 ([§Kähler 미분과 여접층, ⁋명제 2](/ko/math/scheme_theory/sheaf_of_differentials#prop2)) 왼쪽에서도 exact이며 split되는 것, 곧

$$0 \longrightarrow \mathfrak{a}/\mathfrak{a}^2 \overset{\bar d}{\longrightarrow} \Omega_{P/A}\otimes_PB \longrightarrow \Omega_{B/A} \longrightarrow 0$$

이 split short exact sequence인 것과 동치이다. 이 때 $\mathfrak{a}/\mathfrak{a}^2$과 $\Omega_{B/A}$는 모두 finitely generated projective $B$-module이다.
:::
::: 증명
먼저 $\varphi$가 smooth하다 하자. [정리 2](#thm2)에 의하여 $\Omega_{B/A}$는 국소자유이고 유한표시이므로 projective $B$-module이며, 따라서 오른쪽 surjection은 split된다. 남은 것은 $\bar d$가 단사라는 것, 곧 conormal sequence의 왼쪽 두 항이 이루는 naive cotangent complex의 ([\[가환대수학\] §미분, ⁋정의 10](/ko/math/commutative_algebra/differentials#def10)) $H_1=\ker\bar d$가 소멸한다는 것이다. 이 소멸은 국소적인 성질이고 naive cotangent complex는 localization과 commute하므로 (Stacks 08JZ), $X$의 어떤 open covering 위에서 확인하면 충분하다. 한편 smooth morphism은 국소적으로 Jacobian이 최대 rank인 방정식들로 잘린 표현을 가진다. 이는 [정리 3](#thm3)의 역에 해당하는 구조 정리로 그 증명은 본 글의 범위를 넘으며 (Stacks 00TA), 이로부터 $X$를 덮는 standard open $D(g)$들을 잡아, 각각의 $B_g$가 적당한 개수 $c$의 방정식으로 표현되고 그에 대응하는 $c\times c$ Jacobian 소행렬식이 $B_g$에서 가역이도록 할 수 있다. 그럼 [정리 3](#thm3)의 증명에서 본 논증에 의하여 그 표현의 conormal morphism은 split injection이고, 특히 그 $H_1$은 영이다. Naive cotangent complex의 homology는 표현의 선택에 무관하므로 ([\[가환대수학\] §미분, ⁋정리 14](/ko/math/commutative_algebra/differentials#thm14)) $\ker\bar d$는 이 open covering 위에서 소멸하고, 따라서 $\bar d$는 단사이다.

역으로 위의 sequence가 split short exact이라 하자. 그럼 $\mathfrak{a}/\mathfrak{a}^2$과 $\Omega_{B/A}$는 모두 rank $n$의 자유 module $\Omega_{P/A}\otimes_PB$의 direct summand이므로 finitely generated projective이다. 한 점 $x\in X$에 대응하는 prime을 $\mathfrak{q}\subseteq B$, 그 preimage를 $\mathfrak{p}\subseteq P$라 하고 자유 module $(\mathfrak{a}/\mathfrak{a}^2)_{\mathfrak{q}}$의 rank를 $c$라 하자. 그 기저를 $\mathfrak{a}$의 원소들 $f_1,\ldots, f_c$의 class로 택하면 $\mathfrak{a}_{\mathfrak{p}}=(f_1,\ldots, f_c)_{\mathfrak{p}}+\mathfrak{a}_{\mathfrak{p}}^2$이고, $\varphi$가 유한표시라 $\mathfrak{a}$가 finitely generated이므로 Nakayama 보조정리에 의하여 ([\[가환대수학\] §정수적 확장, ⁋보조정리 8](/ko/math/commutative_algebra/integral_extension#lem8)) $\mathfrak{a}_{\mathfrak{p}}=(f_1,\ldots, f_c)_{\mathfrak{p}}$이다. 그럼 어떤 $g\notin\mathfrak{p}$에 대하여 $\mathfrak{a}_g=(f_1,\ldots, f_c)_g$이므로, $X$는 $x$의 근방에서 $X'=\Spec\bigl(P/(f_1,\ldots, f_c)\bigr)$과 열린 부분scheme으로서 일치한다. 한편 split injection은 임의의 base change 뒤에도 단사이므로 $\bar d\otimes\kappa(x)$가 단사이고, 이를 기저 $\overline{f_1},\ldots, \overline{f_c}$와 $\dd{\x_1},\ldots, \dd{\x_n}$에 대하여 표현한 행렬이 $x$에서 계산한 Jacobian $(\partial f_i/\partial \x_j)$의 transpose이므로 그 rank는 $c$이다. 따라서 [정리 3](#thm3)에 의하여 $X' \rightarrow S$는 $x$의 어떤 근방에서 smooth하고, 그 근방에서 $X$와 $X'$이 일치하므로 $\varphi$는 $x$에서 smooth하다. $x$가 임의였으므로 $\varphi$는 smooth하다.
:::

Affine 위에서는 언제나 이러한 closed immersion을 택할 수 있고 smoothness는 국소적인 성질이므로, 위의 판정은 임의의 $\varphi$에 대하여 국소적으로 적용된다. 또한 $\bar d$의 kernel은 표현의 선택에 무관한 불변량 $H_1(\operatorname{NL}_{B/A})$이므로, [명제 4](#prop4)는 smoothness를 이 $H_1$의 소멸과 $H_0(\operatorname{NL}_{B/A})\cong\Omega_{B/A}$의 projectivity로 옮겨 적은 것이기도 하다. 다만 단사성만으로는 smooth가 되지 않는다. 가령 $B=\mathbb{K}[\x,\y]/(\x\y)$에서 $\mathfrak{a}=(\x\y)$는 nonzerodivisor로 생성되어 $\mathfrak{a}/\mathfrak{a}^2$가 rank $1$의 자유 module이고 $\bar d(\overline{\x\y})=\y \dd{\x}+\x \dd{\y}$를 죽이는 원소는 $(\x)\cap(\y)=0$에 속하므로 $\bar d$는 단사이다. 그러나 원점에서 $\bar d$를 residue field로 내린 것은 영이 되어 그 image가 direct summand를 이루지 못하며, 실제로 $X$는 원점에서 singular하다.

이렇듯 conormal sequence의 왼쪽 끝에서의 exactness의 실패는 smoothness의 실패를 재는 양이고, naive cotangent complex는 그 sequence를 왼쪽으로 한 항 연장하여 이를 담은 것이다. 이 연장을 모든 degree로 밀고 나가 $\Omega$를 왼쪽으로 유도한 것이 Quillen과 André의 cotangent complex이며, 그 위에서는 [§Kähler 미분과 여접층, ⁋명제 1](/ko/math/scheme_theory/sheaf_of_differentials#prop1)의 추이 sequence 또한 오른쪽에서만 exact한 sequence가 아니라 왼쪽으로 이어지는 long exact sequence로 연장된다.

## Unramified 사상

Smooth morphism이 $\Omega_{X/S}$를 fiber 차원만큼 남긴다면, 반대쪽 극단은 그것이 통째로 사라지는 경우이다. Cotangent sheaf $\Omega_{X/S}$는 base $S$ 방향을 상수로 본 $X$의 미분을 담으므로, 이것이 영이라는 것은 $X$가 $S$ 위에서 여분의 무한소 방향을 가지지 않음을 뜻하며, 미분기하의 immersion에 대응하는 것이 이 조건이다.

::: 정의 5
Locally of finite presentation인 scheme morphism $\varphi:X \rightarrow S$가 *unramified<sub>비분기</sub>*하다는 것은 cotangent sheaf가

$$\Omega_{X/S}=0$$

인 것이다.
:::

이 정의는 affine 위에서 곧바로 계산된다. $S=\Spec A$, $X=\Spec B$이면 $\Omega_{X/S}=\widetilde{\Omega_{B/A}}$이므로 ([§Kähler 미분과 여접층, ⁋정의 4](/ko/math/scheme_theory/sheaf_of_differentials#def4)), $\varphi$가 unramified한 것은 Kähler 미분 module $\Omega_{B/A}$가 영인 것과 동치이다. 가령 field 확대 $\mathbb{K} \subseteq \mathbb{L}$이 separable algebraic이면 $\Omega_{\mathbb{L}/\mathbb{K}}=0$이고, 따라서 $\Spec \mathbb{L} \rightarrow \Spec \mathbb{K}$는 unramified하다. 반대로 characteristic $p$에서 $\mathbb{L}=\mathbb{K}(t^{1/p})$와 같은 inseparable 확대는 $\Omega_{\mathbb{L}/\mathbb{K}}\neq 0$을 주어 unramified하지 않다.

Unramified 조건은 대각선 morphism을 통해 좌표 독립적으로 표현된다. Cotangent sheaf 자체가 대각선의 conormal로 정의되므로, 그 소멸은 대각선이 열린 부분scheme이 되는 것과 직접 연결된다.

::: 명제 6
Locally of finite presentation인 morphism $\varphi:X \rightarrow S$에 대하여 다음이 동치이다.

1. $\varphi$는 unramified하다.
2. 대각선 morphism $\Delta_\varphi:X \rightarrow X\times_SX$이 ([§값매김환, ⁋정의 3](/ko/math/scheme_theory/valuative_criteria#def3)) open immersion이다.
:::
::: 증명
$\Delta_\varphi$는 항상 immersion, 즉 어떤 열린 부분scheme 위로의 closed immersion이다. 따라서 $\Delta_\varphi$가 open immersion인 것은 그 closed immersion 성분이 isomorphic, 곧 그 image의 ideal sheaf $\mathcal{I}$가 영인 것과 동치이다.

문제는 affine 위에서 국소적이므로 $S=\Spec A$, $X=\Spec B$로 두자. 이 때 $X\times_SX=\Spec(B\otimes_AB)$이고 $\Delta_\varphi$는 곱사상 $\mu:B\otimes_AB \rightarrow B$로부터 온다. $\mathfrak{a}=\ker\mu$라 하면, [§Kähler 미분과 여접층, ⁋명제 6](/ko/math/scheme_theory/sheaf_of_differentials#prop6)의 증명에서 보았듯 $\mathfrak{a}/\mathfrak{a}^2\cong \Omega_{B/A}$이다.

이제 $\Omega_{B/A}=0$, 곧 $\mathfrak{a}=\mathfrak{a}^2$임을 가정하자. $B$가 $A$ 위에서 finite presentation이므로 $B\otimes_AB$ 위에서 $\mathfrak{a}$는 finitely generated이고, Nakayama 보조정리의 행렬식 형태에 의하여 $\mathfrak{a}=\mathfrak{a}^2$이면 어떤 $e\in \mathfrak{a}$가 존재하여 $e^2=e$이고 $\mathfrak{a}=(e)$이다. 그럼 $1-e$가 $\mu$의 image를 trivialize하는 idempotent가 되어, $\Delta_\varphi$의 image는 $D(1-e)$ 위에서 열린 동시에 닫힌 부분scheme으로 실현된다. 따라서 $\Delta_\varphi$는 open immersion이다.

역으로 $\Delta_\varphi$가 open immersion이면 그 image의 ideal sheaf가 영이므로 $\mathfrak{a}/\mathfrak{a}^2=0$, 곧 $\Omega_{B/A}=0$이고 $\varphi$는 unramified하다.
:::

대각선이 open immersion이라는 조건은 미분기하에서 immersion의 그래프가 곱공간 안에서 국소적으로 닫힌 부분다양체를 이루는 상황의 대수적 그림자이다. 한 점 $x\in X$에서 unramified 조건을 fiber로 옮기면, $s=\varphi(x)$의 residue field $\kappa(s)$ 위의 fiber $X_s$에서 $x$가 $\kappa(s)$의 separable 확대를 residue field로 가지는 isolated point가 된다는 것으로 표현된다. 이렇듯 unramified morphism은 fiber 방향으로 무한소 변형을 허용하지 않는 morphism이다.

## Étale 사상

미분기하의 covering map은 fiber가 이산적인 submersion, 곧 상대차원 0의 smooth morphism이다. 대수적 대응물인 étale morphism은 smooth와 unramified를 동시에 요구하여 얻어진다.

::: 정의 7
Locally of finite presentation인 morphism $\varphi:X \rightarrow S$가 *étale<sub>에탈</sub>*하다는 것은 $\varphi$가 smooth하면서 unramified한 것이다.
:::

Smooth morphism에서 $\Omega_{X/S}$는 상대차원만큼의 rank를 가지는 locally free sheaf이고 ([정리 2](#thm2)), unramified morphism에서는 $\Omega_{X/S}=0$이므로 ([정의 5](#def5)), 두 조건이 함께 성립하면 상대차원이 $0$이다. 따라서 étale morphism은 상대차원 $0$의 smooth morphism이며, 동치로 다음과 같이 특징지어진다.

::: 명제 8
Locally of finite presentation인 morphism $\varphi:X \rightarrow S$에 대하여 다음이 동치이다.

1. $\varphi$는 étale하다.
2. $\varphi$는 flat하고 unramified하다.
3. $\varphi$는 flat하고 $\Omega_{X/S}=0$이다.
:::
::: 증명
(1)과 (2)의 동치를 보이면 (3)은 unramified의 정의로부터 곧바로 따른다 ([정의 5](#def5)).

(1) $\Rightarrow$ (2)는 정의에 포함되어 있다. $\varphi$가 étale하면 smooth하므로 flat하고, unramified하다.

(2) $\Rightarrow$ (1)을 보이려면 $\varphi$가 flat하고 unramified할 때 geometric fiber가 regular임을 보이면 된다. Unramified 가정에 의하여 $\Omega_{X/S}=0$이고, 따라서 임의의 geometric fiber $X_{\bar s}$ 위에서도 base change와 commute하는 cotangent sheaf가 $\Omega_{X_{\bar s}/\mathbb{K}}=0$이다. $X_{\bar s}$는 algebraically closed field $\mathbb{K}=\overline{\kappa(s)}$ 위에서 locally of finite presentation이므로 그 closed point $z$는 $\mathbb{K}$-rational이고, 따라서 $\mathfrak{m}_z/\mathfrak{m}_z^2\cong\Omega_{X_{\bar s}/\mathbb{K}}\otimes\kappa(z)=0$이다. Nakayama 보조정리에 의하여 ([\[가환대수학\] §정수적 확장, ⁋보조정리 8](/ko/math/commutative_algebra/integral_extension#lem8)) $\mathfrak{m}_z=0$이므로 $\mathcal{O}_{X_{\bar s},z}=\mathbb{K}$는 field이다. 그럼 $z$를 담는 irreducible component가 $\{z\}$뿐이고 나머지 component들의 합집합은 닫혀 있으므로, 그 여집합으로서 $\{z\}$는 열린집합이다. 이 열린집합들의 합집합의 여집합은 closed point를 담지 않는 닫힌집합이라 공집합이므로 ([정리 2](#thm2)의 증명에서 보았듯 공집합이 아닌 닫힌집합은 언제나 closed point를 담는다), $X_{\bar s}$는 $\Spec\mathbb{K}$들의 disjoint union이다. 특히 이는 국소차원이 $0$인 reduced scheme이라 regular이다. 그러므로 $\varphi$는 flat하고 geometric fiber가 regular이므로 smooth하며, $\Omega_{X/S}=0$이므로 unramified, 곧 étale하다.
:::

이 명제에 의하여 étale morphism은 "flat한 unramified morphism"이라는 가장 간결한 형태로 다룰 수 있으며, 상대차원 $0$이라는 점에서 covering map의 대수적 대응물이다. Étale morphism은 국소적으로 표준적인 모형을 가진다. 이것이 미분기하에서 covering map이 국소적으로 trivial sheet들의 합집합으로 보이는 것에 대응한다.

::: 정의 9
Ring $A$에 대하여, $A$-대수 $B$가

$$B=\bigl(A[t]/(f)\bigr)_g$$

의 꼴이고 monic 다항식 $f\in A[t]$와 $g\in A[t]/(f)$에 대하여 도함수 $f'$의 image가 $B$에서 가역일 때, $\Spec B \rightarrow \Spec A$를 *standard étale<sub>표준 에탈</sub>* morphism이라 부른다.
:::

여기서 $A[t]/(f)$는 monic $f$로 인하여 $A$ 위에서 자유 module, 따라서 flat하고, localization $(\cdot)_g$ 역시 flat하므로 $B$는 $A$ 위에서 flat하다. 한편 conormal exact sequence에서 $\Omega_{(A[t]/(f))/A}\cong (A[t]/(f))/(f')$이고 $f'$를 가역으로 만드는 localization에서 이 module이 소멸하므로 $\Omega_{B/A}=0$이다. 따라서 standard étale morphism은 실제로 étale하며, 핵심 조건인 $f'$의 가역성은 정확히 $f=0$이 중근을 가지지 않는다는 분리가능성의 대수적 표현이다. Étale morphism은 국소적으로 항상 이 standard 형태를 가진다는 구조 정리가 성립하지만, 그 증명은 본 글의 범위를 넘는다.

::: 예시 10
Separable algebraic field 확대 $\mathbb{K} \subseteq \mathbb{L}$에 대하여 $\Spec \mathbb{L} \rightarrow \Spec \mathbb{K}$는 étale하다. 실제로 primitive element 정리에 의하여 $\mathbb{L}=\mathbb{K}[t]/(f)$이고 $f$가 separable이므로 $f'$가 $\mathbb{L}$에서 가역이다. 따라서 이는 standard étale morphism이며, fiber가 한 점인 covering의 가장 단순한 예이다. 반면 inseparable 확대 $\mathbb{F}_p(t^{1/p}) \supseteq \mathbb{F}_p(t)$는 $\Omega\neq 0$이므로 unramified하지 않고, étale하지도 않다.
:::

::: 예시 11
Field $\mathbb{K}$ 위의 multiplicative group $\mathbb{G}_m=\Spec \mathbb{K}[t, t^{-1}]$에서 자기 자신으로의 $n$제곱 morphism

$$[n]:\mathbb{G}_m \longrightarrow \mathbb{G}_m,\qquad t\longmapsto t^n$$

을 생각하자. 이는 ring homomorphism $\mathbb{K}[s, s^{-1}] \rightarrow \mathbb{K}[t, t^{-1}]$, $s\mapsto t^n$으로부터 온다. 상대미분은 $\dd{(t^n)}=n t^{n-1}\dd{t}$로 생성되므로

$$\Omega_{\mathbb{G}_m/\mathbb{G}_m}\cong \mathbb{K}[t, t^{-1}]/(nt^{n-1})$$

이다. $t$가 가역이므로 이 module은 $\mathbb{K}[t, t^{-1}]/(n)$과 같다. 따라서 $\operatorname{char}\mathbb{K}\nmid n$이면 $n$이 가역이어서 $\Omega=0$이고, $[n]$은 flat하므로 ($\mathbb{K}[t, t^{-1}]$이 $s\mapsto t^n$ 아래 자유 module이다) étale하다. 반면 $\operatorname{char}\mathbb{K}=p$가 $n$을 나누면 $\Omega\neq 0$이 되어 $[n]$은 unramified하지 않고, $p$에서 ramification이 일어난다. 이는 characteristic $p$에서 Frobenius가 분기를 일으키는 현상의 가장 단순한 사례이다.
:::

위 두 예시는 étale morphism이 "분기 없는 covering"이라는 직관을 구체화한다. Separable 확대와 characteristic을 나누지 않는 거듭제곱 morphism은 fiber가 분기 없이 균일하게 갈라지는 반면, inseparable 확대나 characteristic을 나누는 거듭제곱에서는 fiber가 무너지며 unramified 조건이 깨진다.

## 무한소 lifting 판정

세 개념 smooth, unramified, étale은 square-zero 확대에 대한 morphism의 lifting이라는 통일된 무한소 조건으로 동시에 특징지어진다. 이것이 미분기하에서 smooth morphism이 무한소 변형을 항상 적분할 수 있다는 사실에 대응하며, 좌표나 fiber에 의존하지 않는 가장 개념적인 판정을 준다.

먼저 무대를 설정한다. $T_0\hookrightarrow T$가 affine scheme들의 closed immersion이고, 그 정의 ideal $\mathcal{J}$가 $\mathcal{J}^2=0$을 만족할 때 이를 *square-zero extension<sub>제곱영 확대</sub>*이라 부른다. 대수적으로는 surjection $R \rightarrow R_0$의 kernel $\mathfrak{b}$가 $\mathfrak{b}^2=0$을 만족하는 상황이다.

::: 정리 12 (무한소 lifting 판정)
Locally of finite presentation인 morphism $\varphi:X \rightarrow S$가 주어졌다 하자. 임의의 affine $S$-scheme $T$와 그 안의 square-zero 닫힌 부분scheme $T_0\hookrightarrow T$, 그리고 $S$-morphism $\psi_0:T_0 \rightarrow X$에 대하여, $\psi_0$을 $T$ 위로 확장하는 $S$-morphism $\psi:T \rightarrow X$의 존재·유일성을 다음과 같이 부른다.

{% diagram Math/Scheme_Theory/Smooth_and_Etale_Morphisms-1.svg width="6.05em" alt="lifting diagram" %}

그럼 다음이 성립한다.

1. $\varphi$가 smooth한 것은 모든 그러한 $(T_0, T, \psi_0)$에 대하여 lifting $\psi$가 존재하는 것과 동치이다.
2. $\varphi$가 unramified한 것은 모든 그러한 $(T_0, T, \psi_0)$에 대하여 lifting $\psi$가 많아야 하나인 것과 동치이다.
3. $\varphi$가 étale한 것은 모든 그러한 $(T_0, T, \psi_0)$에 대하여 lifting $\psi$가 정확히 하나 존재하는 것과 동치이다.
:::
::: 증명
(3)은 (1)과 (2)의 결합이고, étale이 smooth와 unramified의 교집합이므로 ([정의 7](#def7)) (1)과 (2)만 보이면 충분하다.

핵심은 두 lifting의 차이가 $\Omega_{X/S}$로 측정된다는 사실이다. $T=\Spec R$, $T_0=\Spec R_0$이고 $\mathfrak{b}=\ker(R \rightarrow R_0)$가 $\mathfrak{b}^2=0$을 만족한다 하자. $\psi_0$의 두 lifting $\psi, \psi'$가 주어지면, 대응하는 ring homomorphism $B \rightarrow R$의 차이 $D=\psi^\sharp-\psi'^\sharp:B \rightarrow \mathfrak{b}$는 $\mathfrak{b}^2=0$에 의하여 $A$-derivation이 된다. 실제로 $\psi, \psi'$이 mod $\mathfrak{b}$로 일치하므로 임의의 $b, b'\in B$에 대하여

$$D(bb')=\psi(b)\psi(b')-\psi'(b)\psi'(b')=\psi(b)D(b')+D(b)\psi'(b')\equiv \psi_0(b)D(b')+D(b)\psi_0(b')\pmod{\mathfrak{b}^2}$$

이고, $\mathfrak{b}^2=0$이므로 이는 정확히 Leibniz rule이다. 따라서 두 lifting의 차이는 $\Der_A(B, \mathfrak{b})\cong \Hom_B(\Omega_{B/A}, \mathfrak{b})$의 원소들과 일대일 대응한다. ([§Kähler 미분과 여접층, ⁋정의 4](/ko/math/scheme_theory/sheaf_of_differentials#def4)에서 $\Omega_{X/S}=\widetilde{\Omega_{B/A}}$이고, derivation의 표현성에 의한다.)

이로부터 (2)를 얻는다. $\varphi$가 unramified하면 $\Omega_{B/A}=0$이므로 $\Hom_B(\Omega_{B/A}, \mathfrak{b})=0$이고, 따라서 두 lifting의 차이가 항상 영, 곧 lifting은 많아야 하나이다. 역으로 lifting이 항상 많아야 하나이면, $T_0=X$, $T=X[\epsilon]$를 $\Omega_{X/S}$의 dual로 만든 표준 square-zero 확대로 택하여 두 자명한 lifting이 일치해야 함을 보이면 $\Der_A(B, \Omega_{B/A})$의 항등원이 영이 되어 $\Omega_{B/A}=0$이 강제된다. 따라서 $\varphi$는 unramified하다.

(1)을 보인다. $\varphi$가 smooth하다 하자. Lifting의 obstruction은 다음과 같이 분석된다. $\psi_0^\sharp:B \rightarrow R_0$이 주어졌을 때 이를 $B \rightarrow R$로 들어올리려면, $B$의 generator의 image를 $R$로 임의로 올린 뒤 그것이 $B$의 relation을 만족하도록 $\mathfrak{b}$ 안에서 수정해야 한다. 이 수정의 가능 여부가 $\Omega_{B/A}$의 국소자유성으로 통제된다. $B$를 $P=A[\x_i]$의 quotient $P/\mathfrak{a}$로 표시하면, $P \rightarrow R$로의 lifting은 자유 polynomial ring이므로 항상 존재하고, 그것이 $\mathfrak{a}$를 $0$으로 보내도록 $\Hom(\mathfrak{a}/\mathfrak{a}^2, \mathfrak{b})$ 안에서 수정 가능한지가 문제이다. Smooth 가정에서 conormal exact sequence

$$\mathfrak{a}/\mathfrak{a}^2 \rightarrow \Omega_{P/A}\otimes B \rightarrow \Omega_{B/A} \rightarrow 0$$

이 좌측에서도 split되므로 ([명제 4](#prop4)) short exact sequence로 분해되고, 이 split이 정확히 원하는 수정을 제공하여 lifting $\psi$가 존재한다.

역으로 모든 square-zero 확대에 대하여 lifting이 존재한다 하자. 이 lifting property를 $T_0=X$ 위의 conormal 확대 $\Spec(P/\mathfrak{a}^2)$에 항등사상 $\psi_0=\id_X$와 함께 적용하면 $P/\mathfrak{a}^2 \rightarrow B$의 $A$-대수 section을 얻고, 이로부터 conormal exact sequence $\mathfrak{a}/\mathfrak{a}^2 \rightarrow \Omega_{P/A}\otimes B \rightarrow \Omega_{B/A} \rightarrow 0$의 좌측 morphism이 split injection이 된다. 그러므로 [명제 4](#prop4)에 의하여 $\varphi$는 smooth하다.
:::

이 판정은 세 개념을 한 그림 안에 통합한다. 무한소 변형 $T_0\hookrightarrow T$를 따라 $X$로의 morphism을 항상 적분할 수 있으면 smooth, 그 적분이 많아야 한 가지 방법으로만 가능하면 unramified, 정확히 한 가지로 가능하면 étale이다. 특히 étale morphism의 lifting이 유일하다는 것은 covering map 위에서 경로를 들어올리는 방법이 유일하다는 위상적 사실의 대수적 대응이며, 이것이 étale morphism이 대수기하에서 분기 없는 covering과 fundamental group 이론의 토대가 되는 이유이다.

세 조건은 모두 base change와 합성에 대해 안정적이다. Smooth morphism의 base change는 다시 smooth하고, smooth morphism들의 합성도 smooth하며, unramified와 étale에 대해서도 마찬가지이다. 이는 위 lifting 판정이 순수하게 morphism 도식의 성질로 표현되어 있어 base change와 합성 아래에서 그대로 보존되기 때문이다.

---

**참고문헌**

**[Har]** R. Hartshorne, *Algebraic geometry*. Graduate Texts in Mathematics. Springer, 1977.  
**[Vak]** R. Vakil, *The rising sea: Foundations of algebraic geometry*. Available [online](https://math.stanford.edu/~vakil/216blog/).  
**[EGA IV]** A. Grothendieck, *Éléments de géométrie algébrique IV*. Publ. Math. IHÉS, 1964–1967.  
**[Stacks]** The Stacks Project Authors, *The Stacks Project*. Available [online](https://stacks.math.columbia.edu/).
