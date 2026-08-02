---
title: "매끄러운 사상과 étale 사상"
description: "스킴 사상의 매끄러움을 flat이면서 모든 기하적 올이 정칙인 유한표시 사상으로 정의하고, cotangent sheaf가 상대차원만큼의 국소자유층임과 동치임을 본다. Unramified 사상을 대각선이 열린 immersion인 경우로 특징짓고, étale 사상을 매끄럽고 unramified한 상대차원 0의 사상으로 도입하며 standard étale 모형과 Jacobian 판정, square-zero 확대에 대한 무한소 lifting 판정을 다룬다."
excerpt: "Smooth, unramified, and étale morphisms; the Jacobian and infinitesimal lifting criteria"

categories: [Math / Scheme Theory]
permalink: /ko/math/scheme_theory/smooth_and_etale_morphisms
sidebar: 
    nav: "scheme_theory-ko"

date: 2026-06-21
weight: 21

published: false
drift_needed: true
---

미분기하에서 submersion과 covering map은 smooth morphism 가운데 각각 fiber가 양의 차원을 가지는 경우와 이산적인 경우에 해당한다. 대수기하에서 이 두 개념의 유사물이 *smooth* morphism과 *étale* morphism이며, 둘을 함께 묶는 약한 조건이 *unramified* morphism이다. 이들은 모두 fiber가 base 위에서 균일하게 regular임을 요구하므로, flatness와 ([§평탄사상, ⁋정의 1](/ko/math/scheme_theory/flat_morphisms#def1)) cotangent sheaf의 ([§Kähler 미분과 여접층, ⁋정의 4](/ko/math/scheme_theory/sheaf_of_differentials#def4)) 국소자유성을 조합하여 정의된다. 이 글에서는 먼저 unramified morphism을 cotangent sheaf의 소멸로 정의하고 대각선 morphism을 통한 특징을 제시한 뒤, smooth morphism을 flat이면서 geometric fiber가 regular인 morphism으로 정의하고 그 Jacobian 판정을 본다. 이어서 étale morphism을 두 개념의 교집합으로 도입하고 standard étale 모형과 예시를 살펴본 다음, 세 개념을 통일적으로 다루는 square-zero 확대에 대한 무한소 lifting 판정으로 마무리한다.

우리는 이 글 전체에서 morphism이 *locally of finite presentation*임을 기본 가정으로 둔다. Locally Noetherian base 위에서는 이것이 locally of finite type과 일치하므로, 독자는 Noetherian 맥락에서 후자로 읽어도 무방하다.

## Unramified 사상

미분기하의 immersion에 대응하는 가장 약한 조건은 상대미분이 소멸하는 것이다. Cotangent sheaf $\Omega_{X/S}$는 base $S$ 방향을 상수로 본 $X$의 미분을 담으므로, 이것이 영이라는 것은 $X$가 $S$ 위에서 여분의 무한소 방향을 가지지 않음을 뜻한다.

::: 정의 1
Locally of finite presentation인 scheme morphism $f:X \rightarrow S$가 *unramified<sub>비분기</sub>*하다는 것은 cotangent sheaf가

$$\Omega_{X/S}=0$$

인 것이다.
:::

이 정의는 affine 위에서 곧바로 계산된다. $S=\Spec A$, $X=\Spec B$이면 $\Omega_{X/S}=\widetilde{\Omega_{B/A}}$이므로 ([§Kähler 미분과 여접층, ⁋정의 4](/ko/math/scheme_theory/sheaf_of_differentials#def4)), $f$가 unramified한 것은 Kähler 미분 module $\Omega_{B/A}$가 영인 것과 동치이다. 가령 field 확대 $K \subseteq L$이 separable algebraic이면 $\Omega_{L/K}=0$이고, 따라서 $\Spec L \rightarrow \Spec K$는 unramified하다. 반대로 characteristic $p$에서 $L=K(t^{1/p})$와 같은 inseparable 확대는 $\Omega_{L/K}\neq 0$을 주어 unramified하지 않다.

Unramified 조건은 대각선 morphism을 통해 좌표 독립적으로 표현된다. Cotangent sheaf 자체가 대각선의 conormal로 정의되므로, 그 소멸은 대각선이 열린 부분scheme이 되는 것과 직접 연결된다.

::: 명제 2
Locally of finite presentation인 morphism $f:X \rightarrow S$에 대하여 다음이 동치이다.

1. $f$는 unramified하다.
2. 대각선 morphism $\Delta_f:X \rightarrow X\times_SX$이 ([§값매김환, ⁋정의 3](/ko/math/scheme_theory/valuative_criteria#def3)) open immersion이다.
:::
::: 증명
$\Delta_f$는 항상 immersion, 즉 어떤 열린 부분scheme 위로의 closed immersion이다. 따라서 $\Delta_f$가 open immersion인 것은 그 closed immersion 성분이 isomorphic, 곧 그 image의 ideal sheaf $\mathcal{I}$가 영인 것과 동치이다.

문제는 affine 위에서 국소적이므로 $S=\Spec A$, $X=\Spec B$로 두자. 이 때 $X\times_SX=\Spec(B\otimes_AB)$이고 $\Delta_f$는 곱사상 $\mu:B\otimes_AB \rightarrow B$로부터 온다. $\mathfrak{a}=\ker\mu$라 하면, [§Kähler 미분과 여접층, ⁋명제 5](/ko/math/scheme_theory/sheaf_of_differentials#prop5)의 증명에서 보았듯 $\mathfrak{a}/\mathfrak{a}^2\cong \Omega_{B/A}$이다.

이제 $\Omega_{B/A}=0$, 곧 $\mathfrak{a}=\mathfrak{a}^2$임을 가정하자. $B$가 $A$ 위에서 finite presentation이므로 $B\otimes_AB$ 위에서 $\mathfrak{a}$는 finitely generated이고, Nakayama 보조정리의 행렬식 형태에 의하여 $\mathfrak{a}=\mathfrak{a}^2$이면 어떤 $e\in \mathfrak{a}$가 존재하여 $e^2=e$이고 $\mathfrak{a}=(e)$이다. 그럼 $1-e$가 $\mu$의 image를 trivialize하는 idempotent가 되어, $\Delta_f$의 image는 $D(1-e)$ 위에서 열린 동시에 닫힌 부분scheme으로 실현된다. 따라서 $\Delta_f$는 open immersion이다.

역으로 $\Delta_f$가 open immersion이면 그 image의 ideal sheaf가 영이므로 $\mathfrak{a}/\mathfrak{a}^2=0$, 곧 $\Omega_{B/A}=0$이고 $f$는 unramified하다.
:::

대각선이 open immersion이라는 조건은 미분기하에서 immersion의 그래프가 곱공간 안에서 국소적으로 닫힌 부분다양체를 이루는 상황의 대수적 그림자이다. 한 점 $x\in X$에서 unramified 조건을 fiber로 옮기면, $s=f(x)$의 residue field $\kappa(s)$ 위의 fiber $X_s$에서 $x$가 $\kappa(s)$의 separable 확대를 residue field로 가지는 isolated point가 된다는 것으로 표현된다. 이렇듯 unramified morphism은 fiber 방향으로 무한소 변형을 허용하지 않는 morphism이다.

## Smooth 사상

Unramified morphism이 fiber의 무한소 방향을 모두 죽인다면, smooth morphism은 fiber가 base 위에서 균일하게 regular family를 이루도록 한다. Regularity는 ([\[가환대수학\] §정칙국소환](/ko/math/commutative_algebra/regular_local_rings)) local ring에 대한 절대적 조건이므로, 이를 상대적 상황으로 옮기려면 base의 각 점 위 fiber를 그 residue field의 algebraic closure 위로 끌어올린 *geometric fiber*에서 regularity를 요구해야 한다.

::: 정의 3
Locally of finite presentation인 scheme morphism $f:X \rightarrow S$가 *smooth<sub>매끄러운</sub>*하다는 것은 다음 두 조건이 성립하는 것이다.

1. $f$는 flat하다. ([§평탄사상, ⁋정의 1](/ko/math/scheme_theory/flat_morphisms#def1))
2. 임의의 $s\in S$에 대하여, residue field $\kappa(s)$의 algebraic closure $\overline{\kappa(s)}$ 위의 geometric fiber

   $$X_{\bar s}=X\times_S\Spec\overline{\kappa(s)}$$

   는 regular scheme이다. 즉 그 모든 local ring이 regular local ring이다.
:::

이 정의에서 두 조건은 서로 다른 방향을 통제한다. Flatness는 fiber들이 base를 따라 차원 도약 없이 연속적으로 변함을 보장하고 ([§평탄사상, ⁋명제 17](/ko/math/scheme_theory/flat_morphisms#prop17)), geometric fiber의 regularity는 각 fiber 자체가 singular point를 가지지 않음을 보장한다. Residue field가 완전하지 않을 때 fiber $X_s$가 regular이더라도 base change 후 singular point가 생길 수 있으므로, algebraic closure 위의 geometric fiber에서 regularity를 요구하는 것이 본질적이다.

Smooth morphism은 cotangent sheaf의 국소자유성으로 동치적으로 특징지어진다. 이것이 미분기하의 submersion과의 직접적 연결을 준다.

::: 정리 4
Locally of finite presentation인 morphism $f:X \rightarrow S$에 대하여 다음이 동치이다.

1. $f$는 smooth하다.
2. $f$는 flat하고, $\Omega_{X/S}$는 locally free sheaf이며 ([§준연접층, ⁋정의 12](/ko/math/scheme_theory/quasicoherent_sheaves#def12)), 각 $x\in X$에서 그 rank가 $s=f(x)$ 위 fiber의 국소차원 $\dim_x X_s$와 같다.

이 때 $\Omega_{X/S}$의 rank를 $f$의 *상대차원<sub>relative dimension</sub>*이라 부른다.
:::
::: 증명
문제가 국소적이므로 $S=\Spec A$, $X=\Spec B$이고 한 점 $x$에 해당하는 prime $\mathfrak{p}\subseteq B$ 근방에서 작업한다. $s=f(x)$에 해당하는 prime을 $\mathfrak{q}\subseteq A$라 하자.

먼저 $f$가 smooth하다고 가정한다. Geometric fiber $X_{\bar s}$가 regular이고 flat하므로, fiber 위에서 cotangent sheaf의 거동을 본다. Field $k=\overline{\kappa(s)}$ 위의 regular scheme $X_{\bar s}$의 점 $\bar x$에서, Zariski tangent space의 ([§Kähler 미분과 여접층, ⁋정의 7](/ko/math/scheme_theory/sheaf_of_differentials#def7)) 차원은 국소차원과 같다. 즉

$$\dim_{\kappa(\bar x)}\bigl(\Omega_{X_{\bar s}/k}\otimes \kappa(\bar x)\bigr)=\dim \mathcal{O}_{X_{\bar s},\bar x}=\dim_{\bar x}X_{\bar s}$$

이다. 이는 정확히 regular local ring의 cotangent space $\mathfrak{m}/\mathfrak{m}^2$이 차원만큼의 dimension을 가진다는 사실이다. ([\[가환대수학\] §정칙국소환](/ko/math/commutative_algebra/regular_local_rings)의 regular local ring은 그 정의상 $\mathfrak{m}$이 $\dim$개의 원소로 생성되며, 이는 $\dim\mathfrak{m}/\mathfrak{m}^2=\dim$과 동치이다.) Cotangent sheaf는 base change와 commute하므로 $\Omega_{X_{\bar s}/k}=\Omega_{X/S}\otimes_S k$이고, 따라서 $\Omega_{X/S}\otimes \kappa(\bar x)$의 차원이 fiber 차원과 같다.

이제 flatness와 결합한다. $f$가 flat이고 fiber 위에서 $\Omega$의 fiber 차원이 일정하므로, 유한표시 module에 대한 국소자유성 판정에 의하여 $\Omega_{X/S}$는 $\mathfrak{p}$ 근방에서 그 차원만큼의 rank를 가지는 locally free sheaf이다. 구체적으로 $\Omega_{B/A}$는 finitely presented $B$-module이고, $f$가 flat이고 모든 fiber에서 $\dim_{\kappa(x)}\Omega_{B/A}\otimes\kappa(x)$가 일정하므로 $\Omega_{B/A}$는 projective module, 곧 국소자유이다 (유한표시·flat module의 fiber rank가 국소상수이면 국소자유, Stacks 00NX). 그 rank가 fiber 차원과 같음은 위 계산에서 따른다.

역으로 두 번째 조건을 가정하자. $\Omega_{X/S}$가 국소자유이고 그 rank가 fiber 차원과 같으면, 각 geometric fiber $X_{\bar s}$ 위에서 $\Omega_{X_{\bar s}/k}$도 국소자유이며 그 rank가 fiber의 차원과 일치한다. 이는 $X_{\bar s}$의 모든 점에서 Zariski tangent space 차원이 국소차원과 같다는 것이고, $X_{\bar s}$가 finite type over a field이므로 그 점은 regular이다. (algebraically closed field 위에서 tangent space 차원과 국소차원이 일치하면 그 local ring은 regular이다.) 따라서 geometric fiber가 regular이고, 가정에 의해 $f$가 flat이므로 $f$는 smooth하다.
:::

이 동치성에 의하여 smooth morphism은 fiber다발처럼 다룰 수 있다. $\Omega_{X/S}$가 rank $r$의 locally free sheaf라는 것은 $X$가 국소적으로 $S$ 위의 $r$차원 affine space처럼 보인다는 직관을 정확히 표현한다. 실제로 가장 기본적인 예는 affine space로의 projection이며, $\mathbb{A}^r_S \rightarrow S$는 flat하고 $\Omega_{\mathbb{A}^r_S/S}\cong \mathcal{O}^{\oplus r}$이므로 ([§Kähler 미분과 여접층, ⁋명제 8](/ko/math/scheme_theory/sheaf_of_differentials#prop8)) 상대차원 $r$의 smooth morphism이다.

일반적인 smooth morphism은 국소적으로 affine space 안에서 Jacobian이 최대 rank를 가지는 방정식들로 잘린 것으로 기술된다. 이것이 미분기하의 implicit function theorem에 대응하는 대수적 판정이며, smooth 여부를 좌표 계산으로 확인하게 해 준다.

::: 정리 5 (Jacobian 판정)
$S=\Spec A$ 위에서

$$X=\Spec\bigl(A[\x_1,\ldots, \x_{n}]/(f_1,\ldots, f_r)\bigr)$$

이라 하고, $x\in X$를 한 점이라 하자. $x$에서 Jacobian 행렬

$$J=\Bigl(\frac{\partial f_i}{\partial \x_j}\Bigr)_{\substack{1\leq i\leq r\\ 1\leq j\leq n}}$$

의 $\kappa(x)$ 위에서의 rank가 $r$이면, $f:X \rightarrow S$는 $x$의 어떤 열린 근방에서 상대차원 $n-r$의 smooth morphism이다.
:::
::: 증명
[정리 4](#thm4)에 의하여 우리가 보여야 할 것은 $x$의 어떤 근방 위에서 $f$가 flat하고 $\Omega_{X/S}$가 rank $n-r$의 locally free sheaf이며, 그 근방의 각 점에서 fiber의 국소차원이 $n-r$이라는 것이다. 먼저 $\Omega$를 기술하기 위해 $B=A[\x_1,\ldots, \x_n]/(f_1,\ldots, f_r)$, $P=A[\x_1,\ldots, \x_n]$이라 하고 $\mathfrak{a}=(f_1,\ldots, f_r)$라 하자. Closed immersion $X\hookrightarrow \mathbb{A}^n_S$의 conormal exact sequence는 ([§Kähler 미분과 여접층, ⁋명제 2](/ko/math/scheme_theory/sheaf_of_differentials#prop2))

$$\mathfrak{a}/\mathfrak{a}^2 \overset{\bar d}{\longrightarrow} \Omega_{P/A}\otimes_PB \longrightarrow \Omega_{B/A} \longrightarrow 0$$

이며, $\Omega_{P/A}\otimes_PB$는 $d\x_1,\ldots, d\x_n$을 기저로 하는 rank $n$의 자유 $B$-module이다. ([§Kähler 미분과 여접층, ⁋명제 8](/ko/math/scheme_theory/sheaf_of_differentials#prop8)) Morphism $\bar d$는 $f_i+\mathfrak{a}^2\mapsto df_i=\sum_j(\partial f_i/\partial \x_j)d\x_j$로 주어진다. 한편 $\mathfrak{a}$가 $f_1,\ldots, f_r$로 생성되므로 $e_i\mapsto f_i+\mathfrak{a}^2$은 전사사상 $\varphi:B^{\oplus r} \rightarrow \mathfrak{a}/\mathfrak{a}^2$을 정의하며, 합성 $\bar d\circ\varphi$를 $e_i$와 $d\x_j$ 기저에 대하여 표현한 행렬이 정확히 Jacobian $J$의 transpose이다.

이 행렬 표현으로부터 첫 번째 목표인 국소자유성이 얻어진다. 가정에 의하여 $J$의 어떤 $r\times r$ 소행렬식 $g$가 $x$에서 영이 아니다. $D(g)=\Spec B_g$ 위에서는 해당 부분행렬이 가역이므로, 그 $r$개 좌표로의 projection과 $(\bar d\circ\varphi)_g$의 합성이 $B_g^{\oplus r}$의 가역 endomorphism이 되어 $(\bar d\circ\varphi)_g$는 split injection이다. 특히 $\varphi_g$는 단사이고 이미 전사였으므로 동형이며, 따라서 $(\mathfrak{a}/\mathfrak{a}^2)_g$는 rank $r$의 자유 module이고 $\bar d_g$는 자유 module 사이의 split injection이다. 그럼 그 cokernel $\Omega_{B/A}\otimes_BB_g$는 $B_g^{\oplus n}$의 direct summand이므로, $\Omega_{B/A}$는 $D(g)$ 위에서 rank $n-r$의 국소자유이다.

다음 목표는 $f$가 $x$의 어떤 근방에서 flat하다는 것이다. 이하의 논증이 Noetherian 가정을 요구하므로 먼저 일반의 $A$를 그 경우로 줄인다. $f_1,\ldots, f_r$의 계수들이 $A$ 안에서 생성하는 $\mathbb{Z}$-subalgebra를 $A_0$이라 하면 $A_0$은 Noetherian이고 ([\[가환대수학\] §기본 개념들, ⁋정리 12](/ko/math/commutative_algebra/basic_notions#thm12)), $B_0=A_0[\x_1,\ldots, \x_n]/(f_1,\ldots, f_r)$로 두면 $B=B_0\otimes_{A_0}A$이다. $\Spec B \rightarrow \Spec B_0$에 의한 $x$의 image를 $x_0$이라 하면 $J$의 $x$에서의 성분들은 $x_0$에서의 성분들의 image이고 행렬의 rank는 field 확대로 변하지 않으므로, $x_0$에서도 $J$의 rank는 $r$이다. Flatness가 base change로 보존되므로 ([§평탄사상, ⁋명제 3](/ko/math/scheme_theory/flat_morphisms#prop3)), $\Spec B_0 \rightarrow \Spec A_0$이 $x_0$의 근방에서 flat이면 $f$도 $x$의 근방에서 flat이다. 따라서 $A$가 Noetherian이라 가정한다.

Flatness는 local criterion of flatness로 보일 것인데, 이 판정이 요구하는 것은 $f_i$들을 fiber로 내린 것들이 regular sequence를 이룬다는 사실이다. 이를 위해 $s=f(x)$라 하고, $x$를 fiber $\mathbb{A}^n_{\kappa(s)}$의 점으로 볼 때의 local ring을 $R$, 그 maximal ideal을 $\mathfrak{m}$이라 하자. Polynomial ring $\kappa(s)[\x_1,\ldots, \x_n]$이 regular ring이므로 ([\[가환대수학\] §정칙성의 호몰로지 판정, ⁋따름정리 6](/ko/math/commutative_algebra/homological_criterion_for_regularity#cor6)) $R$은 residue field $\kappa(x)$를 가지는 regular local ring이다. $x\in X$이므로 $f_i$를 fiber로 내린 $\bar f_i$는 $\mathfrak{m}$에 속하며, Leibniz 규칙에 의하여 $h\mapsto \sum_j(\partial h/\partial \x_j)(x)d\x_j$가 $\mathfrak{m}^2$을 소멸시키므로 $\kappa(x)$-linear map $\mathfrak{m}/\mathfrak{m}^2 \rightarrow \kappa(x)^{\oplus n}$이 유도된다. 이 map은 $\bar f_i$의 class를 $J$의 $i$번째 행으로 보내고 가정에 의하여 그 행들이 일차독립이므로, $\bar f_1,\ldots, \bar f_r$의 class들도 $\mathfrak{m}/\mathfrak{m}^2$ 안에서 일차독립이다. 이 class들을 $\mathfrak{m}/\mathfrak{m}^2$의 기저로 확장하고 Nakayama 보조정리를 적용하면 ([\[가환대수학\] §정수적 확장, ⁋보조정리 8](/ko/math/commutative_algebra/integral_extension#lem8)) $\mathfrak{m}$을 생성하는 $\dim R$개의 원소를 얻으므로, $\bar f_1,\ldots, \bar f_r$은 $R$의 regular system of parameters의 앞부분이다. [\[가환대수학\] §정칙국소환, ⁋따름정리 3](/ko/math/commutative_algebra/regular_local_rings#cor3)에 의하여 regular system of parameters 전체가 $R$-sequence이므로, 그 앞부분인 $\bar f_1,\ldots, \bar f_r$ 또한 $R$-regular sequence이다.

이제 이 fiber 조건을 base 방향으로 들어올린다. $P$가 $A$ 위에서 free이므로 $\mathbb{A}^n_S \rightarrow S$는 flat이고 ([§평탄사상, ⁋보조정리 2](/ko/math/scheme_theory/flat_morphisms#lem2)), $A$가 Noetherian이므로 $\mathcal{O}_{S,s} \rightarrow \mathcal{O}_{\mathbb{A}^n_S,x}$는 Noetherian local ring 사이의 flat local homomorphism이며, 이를 $\mathcal{O}_{S,s}$의 maximal ideal로 나눈 것이 $R$이다. 그럼 $\bar f_1,\ldots, \bar f_r$이 $R$-regular sequence라는 것으로부터, local criterion of flatness에 의하여 $f_1,\ldots, f_r$은 $\mathcal{O}_{\mathbb{A}^n_S,x}$의 regular sequence이고 quotient $\mathcal{O}_{X,x}$는 $\mathcal{O}_{S,s}$ 위에서 flat이다. (Stacks 00MG) [§평탄사상, ⁋정의 1](/ko/math/scheme_theory/flat_morphisms#def1)의 의미에서 $f$는 $x$에서 flat이므로 [§평탄사상, ⁋정리 20](/ko/math/scheme_theory/flat_morphisms#thm20)에 의하여 $x$의 어떤 열린근방 위에서 flat하다.

마지막으로 남은 것은 fiber의 국소차원이다. 앞의 근방과 $D(g)$의 교집합을 $U$라 하면 $U$ 위에서 $f$는 flat하고 $\Omega_{B/A}$는 rank $n-r$의 국소자유이므로, [정리 4](#thm4)를 적용하기 위해 보여야 할 것은 $U$의 각 점에서 fiber의 국소차원이 $n-r$이라는 것이다. 이는 위의 fiber 논증을 $U$의 다른 점에서 반복하여 얻는다. $U$의 점 $y$와 $s'=f(y)$에 대하여 fiber $X_{s'}$의 $y$를 지나는 component의 generic point를 $\eta$라 하면, $g$가 $\eta$에서도 가역이어서 $J$의 rank가 $r$이므로, 같은 논증에 의하여 $\bar f_1,\ldots, \bar f_r$의 class들은 regular local ring $\mathcal{O}_{\mathbb{A}^n_{\kappa(s')},\eta}$의 $\mathfrak{m}_\eta/\mathfrak{m}_\eta^2$ 안에서 일차독립이다. 곧 그 component의 codimension인 $\dim\mathcal{O}_{\mathbb{A}^n_{\kappa(s')},\eta}$는 $r$ 이상이고, $\eta$가 $(\bar f_1,\ldots, \bar f_r)$을 포함하는 minimal prime이므로 [\[가환대수학\] §차원, ⁋정리 7](/ko/math/commutative_algebra/Krull_dimension#thm7)이 반대 부등식을 주어 codimension은 정확히 $r$이며, 차원 공식에 의하여 ([\[가환대수학\] §뇌터 정규화, ⁋정리 4](/ko/math/commutative_algebra/noether_normalization#thm4)) component의 차원은 $n-r$이다. 따라서 $U$의 각 점에서 fiber의 국소차원이 rank와 일치하고, [정리 4](#thm4)에 의하여 $f$는 상대차원 $n-r$의 smooth morphism이다.
:::

증명의 fiber 단계에서 얻은 regular sequence는 한 점 $x$에서의 조건이지만 근방으로 퍼진다. 각 $i$에 대하여 $\bar f_{i+1}$의 곱셈이 $\kappa(s)[\x_1,\ldots, \x_n]/(\bar f_1,\ldots, \bar f_i)$에 만드는 kernel은 finitely generated이고 $x$에서의 stalk이 $0$이므로 $x$를 담는 어떤 principal open 위에서 소멸한다. 이 principal open들의 교집합을 $D(h)\subseteq \mathbb{A}^n_{\kappa(s)}$라 하면 그 위에서 $\bar f_1,\ldots, \bar f_r$은 regular sequence를 이루고, $X_s\cap D(h)\hookrightarrow D(h)$는 codimension $r$의 complete intersection이다. ([§완전교차, ⁋정의 1](/ko/math/scheme_theory/complete_intersections#def1)) 곧 Jacobian 조건 아래에서 $f$의 fiber는 국소적으로 complete intersection이다.

Jacobian 판정은 smooth 여부를 미분 계산으로 환원하므로 실용적으로 가장 자주 쓰인다. 가령 $\Spec\mathbb{Z}[\x,\y]/(\y^2-\x^3-\x)$ 위에서 $f=\y^2-\x^3-\x$의 Jacobian은 $(\partial f/\partial\x, \partial f/\partial\y)=(-3\x^2-1, 2\y)$이며, 이 두 성분이 동시에 영이 되는 점이 base의 어떤 소수에서 나타나는지를 보면 곡선이 그 소수에서 smooth fiber를 가지는지를 판정할 수 있다.

Jacobian 판정의 증명에서 실제로 쓰인 것은 conormal exact sequence의 왼쪽 morphism이 단사라는 것을 넘어 split injection이 된다는 사실이었다. 이 성질은 택한 방정식 표현에 딸린 우연이 아니라 smoothness 자체와 동치이다.

::: 명제 6
$S=\Spec A$ 위의 closed immersion $X\hookrightarrow \mathbb{A}^n_S$이 주어졌다 하고, $P=A[\x_1,\ldots, \x_n]$, 그 정의 ideal을 $\mathfrak{a}\subseteq P$, $B=P/\mathfrak{a}$라 하자. 그럼 $f:X \rightarrow S$가 smooth한 것은 conormal exact sequence가 ([§Kähler 미분과 여접층, ⁋명제 2](/ko/math/scheme_theory/sheaf_of_differentials#prop2)) 왼쪽에서도 exact이며 split되는 것, 곧

$$0 \longrightarrow \mathfrak{a}/\mathfrak{a}^2 \overset{\bar d}{\longrightarrow} \Omega_{P/A}\otimes_PB \longrightarrow \Omega_{B/A} \longrightarrow 0$$

이 split short exact sequence인 것과 동치이다. 이 때 $\mathfrak{a}/\mathfrak{a}^2$과 $\Omega_{B/A}$는 모두 finitely generated projective $B$-module이다.
:::
::: 증명
먼저 $f$가 smooth하다 하자. [정리 4](#thm4)에 의하여 $\Omega_{B/A}$는 국소자유이고 유한표시이므로 projective $B$-module이며, 따라서 오른쪽 surjection은 split된다. 남은 것은 $\bar d$가 단사라는 것, 곧 conormal sequence의 왼쪽 두 항이 이루는 naive cotangent complex의 ([\[가환대수학\] §미분, ⁋정의 10](/ko/math/commutative_algebra/differentials#def10)) $H_1=\ker\bar d$가 소멸한다는 것이다. 이 소멸은 국소적인 성질이고 naive cotangent complex는 localization과 commute하므로 (Stacks 08JZ), $X$의 어떤 open covering 위에서 확인하면 충분하다. 한편 smooth morphism은 국소적으로 Jacobian이 최대 rank인 방정식들로 잘린 표현을 가진다. 이는 [정리 5](#thm5)의 역에 해당하는 구조 정리로 그 증명은 본 글의 범위를 넘으며 (Stacks 00TA), 이로부터 $X$를 덮는 standard open $D(g)$들을 잡아, 각각의 $B_g$가 적당한 개수 $c$의 방정식으로 표현되고 그에 대응하는 $c\times c$ Jacobian 소행렬식이 $B_g$에서 가역이도록 할 수 있다. 그럼 [정리 5](#thm5)의 증명에서 본 논증에 의하여 그 표현의 conormal morphism은 split injection이고, 특히 그 $H_1$은 영이다. Naive cotangent complex의 homology는 표현의 선택에 무관하므로 ([\[가환대수학\] §미분, ⁋정리 14](/ko/math/commutative_algebra/differentials#thm14)) $\ker\bar d$는 이 open covering 위에서 소멸하고, 따라서 $\bar d$는 단사이다.

역으로 위의 sequence가 split short exact이라 하자. 그럼 $\mathfrak{a}/\mathfrak{a}^2$과 $\Omega_{B/A}$는 모두 rank $n$의 자유 module $\Omega_{P/A}\otimes_PB$의 direct summand이므로 finitely generated projective이다. 한 점 $x\in X$에 대응하는 prime을 $\mathfrak{q}\subseteq B$, 그 preimage를 $\mathfrak{p}\subseteq P$라 하고 자유 module $(\mathfrak{a}/\mathfrak{a}^2)_{\mathfrak{q}}$의 rank를 $c$라 하자. 그 기저를 $\mathfrak{a}$의 원소들 $f_1,\ldots, f_c$의 class로 택하면 $\mathfrak{a}_{\mathfrak{p}}=(f_1,\ldots, f_c)_{\mathfrak{p}}+\mathfrak{a}_{\mathfrak{p}}^2$이고, $f$가 유한표시라 $\mathfrak{a}$가 finitely generated이므로 Nakayama 보조정리에 의하여 ([\[가환대수학\] §정수적 확장, ⁋보조정리 8](/ko/math/commutative_algebra/integral_extension#lem8)) $\mathfrak{a}_{\mathfrak{p}}=(f_1,\ldots, f_c)_{\mathfrak{p}}$이다. 그럼 어떤 $g\notin\mathfrak{p}$에 대하여 $\mathfrak{a}_g=(f_1,\ldots, f_c)_g$이므로, $X$는 $x$의 근방에서 $X'=\Spec\bigl(P/(f_1,\ldots, f_c)\bigr)$과 열린 부분scheme으로서 일치한다. 한편 split injection은 임의의 base change 뒤에도 단사이므로 $\bar d\otimes\kappa(x)$가 단사이고, 이를 기저 $\overline{f_1},\ldots, \overline{f_c}$와 $d\x_1,\ldots, d\x_n$에 대하여 표현한 행렬이 $x$에서 계산한 Jacobian $(\partial f_i/\partial \x_j)$의 transpose이므로 그 rank는 $c$이다. 따라서 [정리 5](#thm5)에 의하여 $X' \rightarrow S$는 $x$의 어떤 근방에서 smooth하고, 그 근방에서 $X$와 $X'$이 일치하므로 $f$는 $x$에서 smooth하다. $x$가 임의였으므로 $f$는 smooth하다.
:::

Affine 위에서는 언제나 이러한 closed immersion을 택할 수 있고 smoothness는 국소적인 성질이므로, 위의 판정은 임의의 $f$에 대하여 국소적으로 적용된다. 또한 $\bar d$의 kernel은 표현의 선택에 무관한 불변량 $H_1(\operatorname{NL}_{B/A})$이므로, [명제 6](#prop6)은 smoothness를 이 $H_1$의 소멸과 $H_0(\operatorname{NL}_{B/A})\cong\Omega_{B/A}$의 projectivity로 옮겨 적은 것이기도 하다. 다만 단사성만으로는 smooth가 되지 않는다. 가령 $B=k[\x,\y]/(\x\y)$에서 $\mathfrak{a}=(\x\y)$는 nonzerodivisor로 생성되어 $\mathfrak{a}/\mathfrak{a}^2$가 rank $1$의 자유 module이고 $\bar d(\overline{\x\y})=\y d\x+\x d\y$를 죽이는 원소는 $(\x)\cap(\y)=0$에 속하므로 $\bar d$는 단사이다. 그러나 원점에서 $\bar d$를 residue field로 내린 것은 영이 되어 그 image가 direct summand를 이루지 못하며, 실제로 $X$는 원점에서 singular하다.

이렇듯 conormal sequence의 왼쪽 끝에서의 exactness의 실패는 smoothness의 실패를 재는 양이고, naive cotangent complex는 그 sequence를 왼쪽으로 한 항 연장하여 이를 담은 것이다. 이 연장을 모든 degree로 밀고 나가 $\Omega$를 왼쪽으로 유도한 것이 Quillen과 André의 cotangent complex이며, 그 위에서는 [§Kähler 미분과 여접층, ⁋명제 1](/ko/math/scheme_theory/sheaf_of_differentials#prop1)의 추이 sequence 또한 오른쪽에서만 exact한 sequence가 아니라 왼쪽으로 이어지는 long exact sequence로 연장된다.

## Étale 사상

미분기하의 covering map은 fiber가 이산적인 submersion, 곧 상대차원 0의 smooth morphism이다. 대수적 대응물인 étale morphism은 smooth와 unramified를 동시에 요구하여 얻어진다.

::: 정의 7
Locally of finite presentation인 morphism $f:X \rightarrow S$가 *étale<sub>에탈</sub>*하다는 것은 $f$가 smooth하면서 unramified한 것이다.
:::

Smooth morphism에서 $\Omega_{X/S}$는 상대차원만큼의 rank를 가지는 locally free sheaf이고 ([정리 4](#thm4)), unramified morphism에서는 $\Omega_{X/S}=0$이므로 ([정의 1](#def1)), 두 조건이 함께 성립하면 상대차원이 $0$이다. 따라서 étale morphism은 상대차원 $0$의 smooth morphism이며, 동치로 다음과 같이 특징지어진다.

::: 명제 8
Locally of finite presentation인 morphism $f:X \rightarrow S$에 대하여 다음이 동치이다.

1. $f$는 étale하다.
2. $f$는 flat하고 unramified하다.
3. $f$는 flat하고 $\Omega_{X/S}=0$이다.
:::
::: 증명
(1)과 (2)의 동치를 보이면 (3)은 unramified의 정의로부터 곧바로 따른다 ([정의 1](#def1)).

(1) $\Rightarrow$ (2)는 정의에 포함되어 있다. $f$가 étale하면 smooth하므로 flat하고, unramified하다.

(2) $\Rightarrow$ (1)을 보이려면 $f$가 flat하고 unramified할 때 geometric fiber가 regular임을 보이면 된다. Unramified 가정에 의하여 $\Omega_{X/S}=0$이고, 따라서 임의의 geometric fiber $X_{\bar s}$ 위에서도 base change와 commute하는 cotangent sheaf가 $\Omega_{X_{\bar s}/k}=0$이다. $X_{\bar s}$는 algebraically closed field $k=\overline{\kappa(s)}$ 위의 finite type scheme이고, 그 위에서 $\Omega=0$이라는 것은 모든 점에서 Zariski tangent space가 영, 곧 국소차원이 $0$이라는 뜻이다. 따라서 $X_{\bar s}$는 $k$의 유한 분리가능 확대들의 곱의 spectrum, 곧 reduced $0$차원 scheme이며 특히 regular이다. 그러므로 $f$는 flat하고 geometric fiber가 regular이므로 smooth하며, $\Omega_{X/S}=0$이므로 unramified, 곧 étale하다.
:::

이 명제에 의하여 étale morphism은 "flat한 unramified morphism"이라는 가장 간결한 형태로 다룰 수 있으며, 상대차원 $0$이라는 점에서 covering map의 대수적 대응물이다. Étale morphism은 국소적으로 표준적인 모형을 가진다. 이것이 미분기하에서 covering map이 국소적으로 trivial sheet들의 합집합으로 보이는 것에 대응한다.

::: 정의 9
Ring $A$에 대하여, $A$-대수 $B$가

$$B=\bigl(A[t]/(f)\bigr)_g$$

의 꼴이고 monic 다항식 $f\in A[t]$와 $g\in A[t]/(f)$에 대하여 도함수 $f'$의 image가 $B$에서 가역일 때, $\Spec B \rightarrow \Spec A$를 *standard étale<sub>표준 에탈</sub>* morphism이라 부른다.
:::

여기서 $A[t]/(f)$는 monic $f$로 인하여 $A$ 위에서 자유 module, 따라서 flat하고, localization $(\cdot)_g$ 역시 flat하므로 $B$는 $A$ 위에서 flat하다. 한편 conormal exact sequence에서 $\Omega_{(A[t]/(f))/A}\cong (A[t]/(f))/(f')$이고 $f'$를 가역으로 만드는 localization에서 이 module이 소멸하므로 $\Omega_{B/A}=0$이다. 따라서 standard étale morphism은 실제로 étale하며, 핵심 조건인 $f'$의 가역성은 정확히 $f=0$이 중근을 가지지 않는다는 분리가능성의 대수적 표현이다. Étale morphism은 국소적으로 항상 이 standard 형태를 가진다는 구조 정리가 성립하지만, 그 증명은 본 글의 범위를 넘는다.

::: 예시 10
Separable algebraic field 확대 $K \subseteq L$에 대하여 $\Spec L \rightarrow \Spec K$는 étale하다. 실제로 primitive element 정리에 의하여 $L=K[t]/(f)$이고 $f$가 separable이므로 $f'$가 $L$에서 가역이다. 따라서 이는 standard étale morphism이며, fiber가 한 점인 covering의 가장 단순한 예이다. 반면 inseparable 확대 $\mathbb{F}_p(t^{1/p}) \supseteq \mathbb{F}_p(t)$는 $\Omega\neq 0$이므로 unramified하지 않고, étale하지도 않다.
:::

::: 예시 11
Field $k$ 위의 곱셈군 $\mathbb{G}_m=\Spec k[t, t^{-1}]$에서 자기 자신으로의 $n$제곱 morphism

$$[n]:\mathbb{G}_m \longrightarrow \mathbb{G}_m,\qquad t\longmapsto t^n$$

을 생각하자. 이는 ring homomorphism $k[s, s^{-1}] \rightarrow k[t, t^{-1}]$, $s\mapsto t^n$으로부터 온다. 상대미분은 $d(t^n)=n t^{n-1}dt$로 생성되므로

$$\Omega_{\mathbb{G}_m/\mathbb{G}_m}\cong k[t, t^{-1}]/(nt^{n-1})$$

이다. $t$가 가역이므로 이 module은 $k[t, t^{-1}]/(n)$과 같다. 따라서 $\operatorname{char}k\nmid n$이면 $n$이 가역이어서 $\Omega=0$이고, $[n]$은 flat하므로 ($k[t,t^{-1}]$이 $s\mapsto t^n$ 아래 자유 module이다) étale하다. 반면 $\operatorname{char}k=p$가 $n$을 나누면 $\Omega\neq 0$이 되어 $[n]$은 unramified하지 않고, $p$에서 ramification이 일어난다. 이는 characteristic $p$에서 Frobenius가 분기를 일으키는 현상의 가장 단순한 사례이다.
:::

위 두 예시는 étale morphism이 "분기 없는 covering"이라는 직관을 구체화한다. Separable 확대와 characteristic을 나누지 않는 거듭제곱 morphism은 fiber가 분기 없이 균일하게 갈라지는 반면, inseparable 확대나 characteristic을 나누는 거듭제곱에서는 fiber가 무너지며 unramified 조건이 깨진다.

## 무한소 lifting 판정

세 개념 smooth, unramified, étale은 square-zero 확대에 대한 morphism의 lifting이라는 통일된 무한소 조건으로 동시에 특징지어진다. 이것이 미분기하에서 smooth morphism이 무한소 변형을 항상 적분할 수 있다는 사실에 대응하며, 좌표나 fiber에 의존하지 않는 가장 개념적인 판정을 준다.

먼저 무대를 설정한다. $T_0\hookrightarrow T$가 affine scheme들의 closed immersion이고, 그 정의 ideal $\mathcal{J}$가 $\mathcal{J}^2=0$을 만족할 때 이를 *square-zero extension<sub>제곱영 확대</sub>*이라 부른다. 대수적으로는 surjection $R \rightarrow R_0$의 kernel $\mathfrak{b}$가 $\mathfrak{b}^2=0$을 만족하는 상황이다.

::: 정리 12 (무한소 lifting 판정)
Locally of finite presentation인 morphism $f:X \rightarrow S$가 주어졌다 하자. 임의의 affine $S$-scheme $T$와 그 안의 square-zero 닫힌 부분scheme $T_0\hookrightarrow T$, 그리고 $S$-morphism $g_0:T_0 \rightarrow X$에 대하여, $g_0$을 $T$ 위로 확장하는 $S$-morphism $g:T \rightarrow X$의 존재·유일성을 다음과 같이 부른다.

{% diagram Math/Scheme_Theory/Smooth_and_Etale_Morphisms-1.svg width="5.99em" alt="lifting diagram" %}

그럼 다음이 성립한다.

1. $f$가 smooth한 것은 모든 그러한 $(T_0, T, g_0)$에 대하여 lifting $g$가 존재하는 것과 동치이다.
2. $f$가 unramified한 것은 모든 그러한 $(T_0, T, g_0)$에 대하여 lifting $g$가 많아야 하나인 것과 동치이다.
3. $f$가 étale한 것은 모든 그러한 $(T_0, T, g_0)$에 대하여 lifting $g$가 정확히 하나 존재하는 것과 동치이다.
:::
::: 증명
(3)은 (1)과 (2)의 결합이고, étale이 smooth와 unramified의 교집합이므로 ([정의 7](#def7)) (1)과 (2)만 보이면 충분하다.

핵심은 두 lifting의 차이가 $\Omega_{X/S}$로 측정된다는 사실이다. $T=\Spec R$, $T_0=\Spec R_0$이고 $\mathfrak{b}=\ker(R \rightarrow R_0)$가 $\mathfrak{b}^2=0$을 만족한다 하자. $g_0$의 두 lifting $g, g'$가 주어지면, 대응하는 ring homomorphism $B \rightarrow R$의 차이 $D=g^\sharp-g'^\sharp:B \rightarrow \mathfrak{b}$는 $\mathfrak{b}^2=0$에 의하여 $A$-derivation이 된다. 실제로 $g, g'$이 mod $\mathfrak{b}$로 일치하므로 임의의 $b, b'\in B$에 대하여

$$D(bb')=g(b)g(b')-g'(b)g'(b')=g(b)D(b')+D(b)g'(b')\equiv g_0(b)D(b')+D(b)g_0(b')\pmod{\mathfrak{b}^2}$$

이고, $\mathfrak{b}^2=0$이므로 이는 정확히 Leibniz rule이다. 따라서 두 lifting의 차이는 $\Der_A(B, \mathfrak{b})\cong \Hom_B(\Omega_{B/A}, \mathfrak{b})$의 원소들과 일대일 대응한다. ([§Kähler 미분과 여접층, ⁋정의 4](/ko/math/scheme_theory/sheaf_of_differentials#def4)에서 $\Omega_{X/S}=\widetilde{\Omega_{B/A}}$이고, derivation의 표현성에 의한다.)

이로부터 (2)를 얻는다. $f$가 unramified하면 $\Omega_{B/A}=0$이므로 $\Hom_B(\Omega_{B/A}, \mathfrak{b})=0$이고, 따라서 두 lifting의 차이가 항상 영, 곧 lifting은 많아야 하나이다. 역으로 lifting이 항상 많아야 하나이면, $T_0=X$, $T=X[\epsilon]$를 $\Omega_{X/S}$의 dual로 만든 표준 square-zero 확대로 택하여 두 자명한 lifting이 일치해야 함을 보이면 $\Der_A(B, \Omega_{B/A})$의 항등원이 영이 되어 $\Omega_{B/A}=0$이 강제된다. 따라서 $f$는 unramified하다.

(1)을 보인다. $f$가 smooth하다 하자. Lifting의 obstruction은 다음과 같이 분석된다. $g_0^\sharp:B \rightarrow R_0$이 주어졌을 때 이를 $B \rightarrow R$로 들어올리려면, $B$의 generator의 image를 $R$로 임의로 올린 뒤 그것이 $B$의 relation을 만족하도록 $\mathfrak{b}$ 안에서 수정해야 한다. 이 수정의 가능 여부가 $\Omega_{B/A}$의 국소자유성으로 통제된다. $B$를 $P=A[\x_i]$의 quotient $P/\mathfrak{a}$로 표시하면, $P \rightarrow R$로의 lifting은 자유 다항식환이므로 항상 존재하고, 그것이 $\mathfrak{a}$를 $0$으로 보내도록 $\Hom(\mathfrak{a}/\mathfrak{a}^2, \mathfrak{b})$ 안에서 수정 가능한지가 문제이다. Smooth 가정에서 conormal exact sequence

$$\mathfrak{a}/\mathfrak{a}^2 \rightarrow \Omega_{P/A}\otimes B \rightarrow \Omega_{B/A} \rightarrow 0$$

이 좌측에서도 split되므로 ([명제 6](#prop6)) short exact sequence로 분해되고, 이 split이 정확히 원하는 수정을 제공하여 lifting $g$가 존재한다.

역으로 모든 square-zero 확대에 대하여 lifting이 존재한다 하자. 이 lifting property를 $T_0=X$ 위의 conormal 확대 $\Spec(P/\mathfrak{a}^2)$에 항등사상 $g_0=\id_X$와 함께 적용하면 $P/\mathfrak{a}^2 \rightarrow B$의 $A$-대수 section을 얻고, 이로부터 conormal exact sequence $\mathfrak{a}/\mathfrak{a}^2 \rightarrow \Omega_{P/A}\otimes B \rightarrow \Omega_{B/A} \rightarrow 0$의 좌측 morphism이 split injection이 된다. 그러므로 [명제 6](#prop6)에 의하여 $f$는 smooth하다.
:::

이 판정은 세 개념을 한 그림 안에 통합한다. 무한소 변형 $T_0\hookrightarrow T$를 따라 $X$로의 morphism을 항상 적분할 수 있으면 smooth, 그 적분이 많아야 한 가지 방법으로만 가능하면 unramified, 정확히 한 가지로 가능하면 étale이다. 특히 étale morphism의 lifting이 유일하다는 것은 covering map 위에서 경로를 들어올리는 방법이 유일하다는 위상적 사실의 대수적 대응이며, 이것이 étale morphism이 대수기하에서 분기 없는 covering과 기본군 이론의 토대가 되는 이유이다.

세 조건은 모두 base change와 합성에 대해 안정적이다. Smooth morphism의 base change는 다시 smooth하고, smooth morphism들의 합성도 smooth하며, unramified와 étale에 대해서도 마찬가지이다. 이는 위 lifting 판정이 순수하게 morphism 도식의 성질로 표현되어 있어 base change와 합성 아래에서 그대로 보존되기 때문이다.

---

**참고문헌**

**[Har]** R. Hartshorne, *Algebraic geometry*. Graduate Texts in Mathematics. Springer, 1977.  
**[Vak]** R. Vakil, *The rising sea: Foundations of algebraic geometry*. Available [online](https://math.stanford.edu/~vakil/216blog/).  
**[EGA IV]** A. Grothendieck, *Éléments de géométrie algébrique IV*. Publ. Math. IHÉS, 1964–1967.  
**[Stacks]** The Stacks Project Authors, *The Stacks Project*. Available [online](https://stacks.math.columbia.edu/).
