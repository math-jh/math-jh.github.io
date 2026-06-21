---
title: "매끄러운 사상과 étale 사상"
description: "스킴 사상의 매끄러움을 flat이면서 모든 기하적 올이 정칙인 유한표시 사상으로 정의하고, cotangent sheaf가 상대차원만큼의 국소자유층임과 동치임을 본다. unramified 사상을 대각선이 열린 immersion인 경우로 특징짓고, étale 사상을 매끄럽고 unramified한 상대차원 0의 사상으로 도입하며 standard étale 모형과 Jacobian 판정, square-zero 확대에 대한 무한소 lifting 판정을 다룬다."
excerpt: "Smooth, unramified, and étale morphisms; the Jacobian and infinitesimal lifting criteria"

categories: [Math / Scheme Theory]
permalink: /ko/math/scheme_theory/smooth_and_etale_morphisms
sidebar: 
    nav: "scheme_theory-ko"

date: 2026-06-21
weight: 20

published: false
---

미분기하에서 submersion과 covering map은 매끄러운 사상 가운데 각각 fiber가 양의 차원을 가지는 경우와 이산적인 경우에 해당한다. 대수기하에서 이 두 개념의 유사물이 *smooth* 사상과 *étale* 사상이며, 둘을 함께 묶는 약한 조건이 *unramified* 사상이다. 이들은 모두 fiber가 base 위에서 균일하게 정칙임을 요구하므로, 평탄성 ([§평탄사상, ⁋정의 2](/ko/math/scheme_theory/flat_morphisms#def2))과 cotangent sheaf ([§Kähler 미분과 여접층, ⁋정의 3](/ko/math/scheme_theory/sheaf_of_differentials#def3))의 국소자유성을 조합하여 정의된다. 이 글에서는 먼저 unramified 사상을 cotangent sheaf의 소멸로 정의하고 대각선 사상을 통한 특징을 제시한 뒤, smooth 사상을 flat이면서 기하적 올이 정칙인 사상으로 정의하고 그 Jacobian 판정을 본다. 이어서 étale 사상을 두 개념의 교집합으로 도입하고 standard étale 모형과 예시를 살펴본 다음, 세 개념을 통일적으로 다루는 square-zero 확대에 대한 무한소 lifting 판정으로 마무리한다.

우리는 이 글 전체에서 사상이 *locally of finite presentation*임을 기본 가정으로 둔다. Locally Noetherian base 위에서는 이것이 locally of finite type과 일치하므로, 독자는 Noetherian 맥락에서 후자로 읽어도 무방하다.

## Unramified 사상

미분기하의 immersion에 대응하는 가장 약한 조건은 상대미분이 소멸하는 것이다. Cotangent sheaf $$\Omega_{X/S}$$는 base $$S$$ 방향을 상수로 본 $$X$$의 미분을 담으므로, 이것이 영이라는 것은 $$X$$가 $$S$$ 위에서 여분의 무한소 방향을 가지지 않음을 뜻한다.

<div class="definition" markdown="1">

<ins id="def1">**정의 1**</ins> Locally of finite presentation인 scheme 사상 $$f:X \rightarrow S$$가 *unramified<sub>비분기</sub>*하다는 것은 cotangent sheaf가

$$\Omega_{X/S}=0$$

인 것이다.

</div>

이 정의는 affine 위에서 곧바로 계산된다. $$S=\Spec A$$, $$X=\Spec B$$이면 $$\Omega_{X/S}=\widetilde{\Omega_{B/A}}$$이므로 ([§Kähler 미분과 여접층, ⁋명제 4](/ko/math/scheme_theory/sheaf_of_differentials#prop4)), $$f$$가 unramified한 것은 Kähler 미분 가군 $$\Omega_{B/A}$$가 영인 것과 동치이다. 가령 field 확대 $$K \subseteq L$$이 separable algebraic이면 $$\Omega_{L/K}=0$$이고, 따라서 $$\Spec L \rightarrow \Spec K$$는 unramified하다. 반대로 특성 $$p$$에서 $$L=K(t^{1/p})$$와 같은 inseparable 확대는 $$\Omega_{L/K}\neq 0$$을 주어 unramified하지 않다.

Unramified 조건은 대각선 사상을 통해 좌표 독립적으로 표현된다. Cotangent sheaf 자체가 대각선의 conormal로 정의되므로, 그 소멸은 대각선이 열린 부분scheme이 되는 것과 직접 연결된다.

<div class="proposition" markdown="1">

<ins id="prop2">**명제 2**</ins> Locally of finite presentation인 사상 $$f:X \rightarrow S$$에 대하여 다음이 동치이다.

1. $$f$$는 unramified하다.
2. 대각선 사상 $$\Delta_f:X \rightarrow X\times_SX$$ ([§값매김환, ⁋정의 3](/ko/math/scheme_theory/valuative_criteria#def3))이 열린 immersion이다.

</div>
<details class="proof" markdown="1">
<summary>증명</summary>

$$\Delta_f$$는 항상 immersion, 즉 어떤 열린 부분scheme 위로의 닫힌 immersion이다. 따라서 $$\Delta_f$$가 열린 immersion인 것은 그 닫힌 immersion 성분이 동형, 곧 그 image의 ideal sheaf $$\mathcal{I}$$가 영인 것과 동치이다.

문제는 affine 위에서 국소적이므로 $$S=\Spec A$$, $$X=\Spec B$$로 두자. 이 때 $$X\times_SX=\Spec(B\otimes_AB)$$이고 $$\Delta_f$$는 곱사상 $$\mu:B\otimes_AB \rightarrow B$$로부터 온다. $$I=\ker\mu$$라 하면, [§Kähler 미분과 여접층, ⁋명제 4](/ko/math/scheme_theory/sheaf_of_differentials#prop4)의 증명에서 보았듯 $$I/I^2\cong \Omega_{B/A}$$이다.

이제 $$\Omega_{B/A}=0$$, 곧 $$I=I^2$$임을 가정하자. $$B$$가 $$A$$ 위에서 finite presentation이므로 $$B\otimes_AB$$ 위에서 $$I$$는 finitely generated이고, Nakayama 보조정리의 행렬식 형태에 의하여 $$I=I^2$$이면 어떤 $$e\in I$$가 존재하여 $$e^2=e$$이고 $$I=(e)$$이다. 그럼 $$1-e$$가 $$\mu$$의 image를 trivialize하는 idempotent가 되어, $$\Delta_f$$의 image는 $$D(1-e)$$ 위에서 열린 동시에 닫힌 부분scheme으로 실현된다. 따라서 $$\Delta_f$$는 열린 immersion이다.

역으로 $$\Delta_f$$가 열린 immersion이면 그 image의 ideal sheaf가 영이므로 $$I/I^2=0$$, 곧 $$\Omega_{B/A}=0$$이고 $$f$$는 unramified하다.

</details>

대각선이 열린 immersion이라는 조건은 미분기하에서 immersion의 그래프가 곱공간 안에서 국소적으로 닫힌 부분다양체를 이루는 상황의 대수적 그림자이다. 한 점 $$x\in X$$에서 unramified 조건을 fiber로 옮기면, $$s=f(x)$$의 잉여류체 $$\kappa(s)$$ 위의 fiber $$X_s$$에서 $$x$$가 $$\kappa(s)$$의 separable 확대를 잉여류체로 가지는 고립점이 된다는 것으로 표현된다. 이렇듯 unramified 사상은 fiber 방향으로 무한소 변형을 허용하지 않는 사상이다.

## Smooth 사상

Unramified 사상이 fiber의 무한소 방향을 모두 죽인다면, smooth 사상은 fiber가 base 위에서 균일하게 정칙인 family를 이루도록 한다. 정칙성 ([\[가환대수학\] §정칙국소환](/ko/math/commutative_algebra/regular_local_rings))은 국소환에 대한 절대적 조건이므로, 이를 상대적 상황으로 옮기려면 base의 각 점 위 fiber를 그 잉여류체의 대수적 폐포 위로 끌어올린 *geometric fiber*에서 정칙성을 요구해야 한다.

<div class="definition" markdown="1">

<ins id="def3">**정의 3**</ins> Locally of finite presentation인 scheme 사상 $$f:X \rightarrow S$$가 *smooth<sub>매끄러운</sub>*하다는 것은 다음 두 조건이 성립하는 것이다.

1. $$f$$는 flat하다. ([§평탄사상, ⁋정의 2](/ko/math/scheme_theory/flat_morphisms#def2))
2. 임의의 $$s\in S$$에 대하여, 잉여류체 $$\kappa(s)$$의 대수적 폐포 $$\overline{\kappa(s)}$$ 위의 geometric fiber

   $$X_{\bar s}=X\times_S\Spec\overline{\kappa(s)}$$

   는 정칙 scheme이다. 즉 그 모든 국소환이 regular local ring이다.

</div>

이 정의에서 두 조건은 서로 다른 방향을 통제한다. 평탄성은 fiber들이 base를 따라 차원 도약 없이 연속적으로 변함을 보장하고 ([§평탄사상, ⁋명제 3](/ko/math/scheme_theory/flat_morphisms#prop3)), geometric fiber의 정칙성은 각 fiber 자체가 특이점을 가지지 않음을 보장한다. 잉여류체가 완전하지 않을 때 fiber $$X_s$$가 정칙이더라도 base change 후 특이점이 생길 수 있으므로, 대수적 폐포 위의 geometric fiber에서 정칙성을 요구하는 것이 본질적이다.

Smooth 사상은 cotangent sheaf의 국소자유성으로 동치적으로 특징지어진다. 이것이 미분기하의 submersion과의 직접적 연결을 준다.

<div class="proposition" markdown="1">

<ins id="thm4">**정리 4**</ins> Locally of finite presentation인 사상 $$f:X \rightarrow S$$에 대하여 다음이 동치이다.

1. $$f$$는 smooth하다.
2. $$f$$는 flat하고, $$\Omega_{X/S}$$는 국소자유층 ([§준연접층, ⁋정의 15](/ko/math/scheme_theory/quasicoherent_sheaves#def15))이며, 각 $$x\in X$$에서 그 rank가 $$s=f(x)$$ 위 fiber의 국소차원 $$\dim_x X_s$$와 같다.

이 때 $$\Omega_{X/S}$$의 rank를 $$f$$의 *상대차원<sub>relative dimension</sub>*이라 부른다.

</div>
<details class="proof" markdown="1">
<summary>증명</summary>

문제가 국소적이므로 $$S=\Spec A$$, $$X=\Spec B$$이고 한 점 $$x$$에 해당하는 prime $$\mathfrak{p}\subseteq B$$ 근방에서 작업한다. $$s=f(x)$$에 해당하는 prime을 $$\mathfrak{q}\subseteq A$$라 하자.

먼저 $$f$$가 smooth하다고 가정한다. Geometric fiber $$X_{\bar s}$$가 정칙이고 flat하므로, fiber 위에서 cotangent sheaf의 거동을 본다. Field $$k=\overline{\kappa(s)}$$ 위의 정칙 scheme $$X_{\bar s}$$의 점 $$\bar x$$에서, Zariski 접공간 ([§Kähler 미분과 여접층, ⁋정의 6](/ko/math/scheme_theory/sheaf_of_differentials#def6))의 차원은 국소차원과 같다. 즉

$$\dim_{\kappa(\bar x)}\bigl(\Omega_{X_{\bar s}/k}\otimes \kappa(\bar x)\bigr)=\dim \mathcal{O}_{X_{\bar s},\bar x}=\dim_{\bar x}X_{\bar s}$$

이다. 이는 정확히 정칙국소환의 cotangent space $$\mathfrak{m}/\mathfrak{m}^2$$이 차원만큼의 dimension을 가진다는 사실이다. ([\[가환대수학\] §정칙국소환, ⁋따름정리 1](/ko/math/commutative_algebra/regular_local_rings#cor1)의 정칙국소환은 그 정의상 $$\mathfrak{m}$$이 $$\dim$$개의 원소로 생성되며, 이는 $$\dim\mathfrak{m}/\mathfrak{m}^2=\dim$$과 동치이다.) Cotangent sheaf는 base change와 commute하므로 $$\Omega_{X_{\bar s}/k}=\Omega_{X/S}\otimes_S k$$이고, 따라서 $$\Omega_{X/S}\otimes \kappa(\bar x)$$의 차원이 fiber 차원과 같다.

이제 평탄성과 결합한다. $$f$$가 flat이고 fiber 위에서 $$\Omega$$의 fiber 차원이 일정하므로, 유한표시 가군에 대한 국소자유성 판정에 의하여 $$\Omega_{X/S}$$는 $$\mathfrak{p}$$ 근방에서 그 차원만큼의 rank를 가지는 국소자유층이다. 구체적으로 $$\Omega_{B/A}$$는 finitely presented $$B$$-가군이고, $$f$$가 flat이고 모든 fiber에서 $$\dim_{\kappa(x)}\Omega_{B/A}\otimes\kappa(x)$$가 일정하므로 $$\Omega_{B/A}$$는 사영가군, 곧 국소자유이다 (유한표시·평탄 가군의 fiber rank가 국소상수이면 국소자유, Stacks 00NX). 그 rank가 fiber 차원과 같음은 위 계산에서 따른다.

역으로 두 번째 조건을 가정하자. $$\Omega_{X/S}$$가 국소자유이고 그 rank가 fiber 차원과 같으면, 각 geometric fiber $$X_{\bar s}$$ 위에서 $$\Omega_{X_{\bar s}/k}$$도 국소자유이며 그 rank가 fiber의 차원과 일치한다. 이는 $$X_{\bar s}$$의 모든 점에서 Zariski 접공간 차원이 국소차원과 같다는 것이고, $$X_{\bar s}$$가 finite type over a field이므로 그 점은 정칙이다. (대수적으로 닫힌 체 위에서 접공간 차원과 국소차원이 일치하면 그 국소환은 regular이다.) 따라서 geometric fiber가 정칙이고, 가정에 의해 $$f$$가 flat이므로 $$f$$는 smooth하다.

</details>

이 동치성에 의하여 smooth 사상은 fiber다발처럼 다룰 수 있다. $$\Omega_{X/S}$$가 rank $$r$$의 국소자유층이라는 것은 $$X$$가 국소적으로 $$S$$ 위의 $$r$$차원 affine space처럼 보인다는 직관을 정확히 표현한다. 실제로 가장 기본적인 예는 affine space로의 사영이며, $$\mathbb{A}^r_S \rightarrow S$$는 flat하고 $$\Omega_{\mathbb{A}^r_S/S}\cong \mathcal{O}^{\oplus r}$$이므로 ([§Kähler 미분과 여접층, ⁋명제 7](/ko/math/scheme_theory/sheaf_of_differentials#prop7)) 상대차원 $$r$$의 smooth 사상이다.

일반적인 smooth 사상은 국소적으로 affine space 안에서 Jacobian이 최대 rank를 가지는 방정식들로 잘린 것으로 기술된다. 이것이 미분기하의 implicit function theorem에 대응하는 대수적 판정이며, smooth 여부를 좌표 계산으로 확인하게 해 준다.

<div class="proposition" markdown="1">

<ins id="thm5">**정리 5 (Jacobian 판정)**</ins> $$S=\Spec A$$ 위에서

$$X=\Spec\bigl(A[\x_1,\ldots, \x_{n}]/(f_1,\ldots, f_r)\bigr)$$

이라 하고, $$x\in X$$를 한 점이라 하자. $$x$$에서 Jacobian 행렬

$$J=\Bigl(\frac{\partial f_i}{\partial \x_j}\Bigr)_{\substack{1\leq i\leq r\\ 1\leq j\leq n}}$$

의 $$\kappa(x)$$ 위에서의 rank가 $$r$$이면, $$f:X \rightarrow S$$는 $$x$$의 어떤 열린 근방에서 상대차원 $$n-r$$의 smooth 사상이다.

</div>
<details class="proof" markdown="1">
<summary>증명</summary>

$$B=A[\x_1,\ldots, \x_n]/(f_1,\ldots, f_r)$$, $$P=A[\x_1,\ldots, \x_n]$$이라 하고 $$I=(f_1,\ldots, f_r)$$라 하자. 닫힌 immersion $$X\hookrightarrow \mathbb{A}^n_S$$의 conormal 완전열 ([§Kähler 미분과 여접층, ⁋명제 2](/ko/math/scheme_theory/sheaf_of_differentials#prop2))은

$$I/I^2 \overset{\bar d}{\longrightarrow} \Omega_{P/A}\otimes_PB \longrightarrow \Omega_{B/A} \longrightarrow 0$$

이며, $$\Omega_{P/A}\otimes_PB$$는 $$d\x_1,\ldots, d\x_n$$을 기저로 하는 rank $$n$$의 자유 $$B$$-가군이다. ([§Kähler 미분과 여접층, ⁋명제 7](/ko/math/scheme_theory/sheaf_of_differentials#prop7)) 사상 $$\bar d$$는 $$f_i+I^2\mapsto df_i=\sum_j(\partial f_i/\partial \x_j)\,d\x_j$$로 주어지므로, $$\bar d$$를 $$d\x_j$$ 기저에 대하여 표현한 행렬이 정확히 Jacobian $$J$$의 transpose이다.

$$x$$에서 $$J$$의 rank가 $$r$$이면, $$\kappa(x)$$ 위에서 $$\bar d\otimes\kappa(x)$$가 단사이고 그 image가 $$n$$차원 공간의 $$r$$차원 부분공간이다. 따라서 conormal 완전열을 $$\kappa(x)$$로 텐서한

$$I/I^2\otimes\kappa(x) \overset{\bar d\otimes\kappa(x)}{\longrightarrow} \kappa(x)^{\oplus n} \longrightarrow \Omega_{B/A}\otimes\kappa(x) \longrightarrow 0$$

에서 $$\dim_{\kappa(x)}\Omega_{B/A}\otimes\kappa(x)=n-r$$이다. 한편 $$\bar d$$의 행렬 $$J$$의 어떤 $$r\times r$$ 소행렬식 $$g$$가 $$x$$에서 영이 아니므로, $$D(g)$$ 위에서 $$\bar d$$는 자유 가군 사이의 split injection이 되고 그 cokernel $$\Omega_{B/A}$$는 rank $$n-r$$의 국소자유층이 된다. 이로부터 $$\Omega_{B/A}$$는 $$D(g)$$ 위에서 rank $$n-r$$의 국소자유이다.

남은 것은 $$D(g)$$ 위에서 $$f$$가 flat이라는 사실이다. $$\bar d$$가 split injection이면 conormal 가군 $$I/I^2$$이 rank $$r$$의 국소자유이며, Jacobian이 $$x$$에서 rank $$r$$이라는 조건은 $$f_1,\ldots, f_r$$이 $$x$$ 근방에서 regular sequence를 이룸($$P$$ 안의 codimension $$r$$ regular immersion)과 동치이다. Affine space $$\mathbb{A}^n_S$$가 $$S$$ 위에서 flat이고 $$f_1,\ldots, f_r$$이 각 fiber에서도 regular sequence를 이루므로, $$B=P/(f_1,\ldots, f_r)$$은 $$S$$ 위에서 flat하다. 따라서 $$D(g)$$ 위에서 $$f$$는 flat하고 $$\Omega$$가 rank $$n-r$$의 국소자유이므로, [정리 4](#thm4)에 의하여 $$f$$는 상대차원 $$n-r$$의 smooth 사상이다.

</details>

Jacobian 판정은 smooth 여부를 미분 계산으로 환원하므로 실용적으로 가장 자주 쓰인다. 가령 $$\Spec\mathbb{Z}[\x,\y]/(\y^2-\x^3-\x)$$ 위에서 $$f=\y^2-\x^3-\x$$의 Jacobian은 $$(\partial f/\partial\x, \partial f/\partial\y)=(-3\x^2-1, 2\y)$$이며, 이 두 성분이 동시에 영이 되는 점이 base의 어떤 소수에서 나타나는지를 보면 곡선이 그 소수에서 smooth fiber를 가지는지를 판정할 수 있다.

## Étale 사상

미분기하의 covering map은 fiber가 이산적인 submersion, 곧 상대차원 0의 매끄러운 사상이다. 대수적 대응물인 étale 사상은 smooth와 unramified를 동시에 요구하여 얻어진다.

<div class="definition" markdown="1">

<ins id="def6">**정의 6**</ins> Locally of finite presentation인 사상 $$f:X \rightarrow S$$가 *étale<sub>에탈</sub>*하다는 것은 $$f$$가 smooth하면서 unramified한 것이다.

</div>

Smooth 사상에서 $$\Omega_{X/S}$$는 상대차원만큼의 rank를 가지는 국소자유층이고 ([정리 4](#thm4)), unramified 사상에서는 $$\Omega_{X/S}=0$$이므로 ([정의 1](#def1)), 두 조건이 함께 성립하면 상대차원이 $$0$$이다. 따라서 étale 사상은 상대차원 $$0$$의 smooth 사상이며, 동치로 다음과 같이 특징지어진다.

<div class="proposition" markdown="1">

<ins id="prop7">**명제 7**</ins> Locally of finite presentation인 사상 $$f:X \rightarrow S$$에 대하여 다음이 동치이다.

1. $$f$$는 étale하다.
2. $$f$$는 flat하고 unramified하다.
3. $$f$$는 flat하고 $$\Omega_{X/S}=0$$이다.

</div>
<details class="proof" markdown="1">
<summary>증명</summary>

(1)과 (2)의 동치를 보이면 (3)은 unramified의 정의 ([정의 1](#def1))로부터 곧바로 따른다.

(1) $$\Rightarrow$$ (2)는 정의에 포함되어 있다. $$f$$가 étale하면 smooth하므로 flat하고, unramified하다.

(2) $$\Rightarrow$$ (1)을 보이려면 $$f$$가 flat하고 unramified할 때 geometric fiber가 정칙임을 보이면 된다. Unramified 가정에 의하여 $$\Omega_{X/S}=0$$이고, 따라서 임의의 geometric fiber $$X_{\bar s}$$ 위에서도 base change와 commute하는 cotangent sheaf가 $$\Omega_{X_{\bar s}/k}=0$$이다. $$X_{\bar s}$$는 대수적으로 닫힌 체 $$k=\overline{\kappa(s)}$$ 위의 finite type scheme이고, 그 위에서 $$\Omega=0$$이라는 것은 모든 점에서 Zariski 접공간이 영, 곧 국소차원이 $$0$$이라는 뜻이다. 따라서 $$X_{\bar s}$$는 $$k$$의 유한 분리가능 확대들의 곱의 spectrum, 곧 reduced $$0$$차원 scheme이며 특히 정칙이다. 그러므로 $$f$$는 flat하고 geometric fiber가 정칙이므로 smooth하며, $$\Omega_{X/S}=0$$이므로 unramified, 곧 étale하다.

</details>

이 명제에 의하여 étale 사상은 "flat한 unramified 사상"이라는 가장 간결한 형태로 다룰 수 있으며, 상대차원 $$0$$이라는 점에서 covering map의 대수적 대응물이다. Étale 사상은 국소적으로 표준적인 모형을 가진다. 이것이 미분기하에서 covering map이 국소적으로 trivial sheet들의 합집합으로 보이는 것에 대응한다.

<div class="definition" markdown="1">

<ins id="def8">**정의 8**</ins> Ring $$A$$에 대하여, $$A$$-대수 $$B$$가

$$B=\bigl(A[t]/(f)\bigr)_g$$

의 꼴이고 monic 다항식 $$f\in A[t]$$와 $$g\in A[t]/(f)$$에 대하여 도함수 $$f'$$의 image가 $$B$$에서 가역일 때, $$\Spec B \rightarrow \Spec A$$를 *standard étale* 사상이라 부른다.

</div>

여기서 $$A[t]/(f)$$는 monic $$f$$로 인하여 $$A$$ 위에서 자유 가군, 따라서 flat하고, localization $$(\cdot)_g$$ 역시 flat하므로 $$B$$는 $$A$$ 위에서 flat하다. 한편 conormal 완전열에서 $$\Omega_{(A[t]/(f))/A}\cong (A[t]/(f))/(f')$$이고 $$f'$$를 가역으로 만드는 localization에서 이 가군이 소멸하므로 $$\Omega_{B/A}=0$$이다. 따라서 standard étale 사상은 실제로 étale하며, 핵심 조건인 $$f'$$의 가역성은 정확히 $$f=0$$이 중근을 가지지 않는다는 분리가능성의 대수적 표현이다. Étale 사상은 국소적으로 항상 이 standard 형태를 가진다는 구조 정리가 성립하지만, 그 증명은 본 글의 범위를 넘는다.

<div class="example" markdown="1">

<ins id="ex9">**예시 9**</ins> Separable algebraic field 확대 $$K \subseteq L$$에 대하여 $$\Spec L \rightarrow \Spec K$$는 étale하다. 실제로 primitive element 정리에 의하여 $$L=K[t]/(f)$$이고 $$f$$가 separable이므로 $$f'$$가 $$L$$에서 가역이다. 따라서 이는 standard étale 사상이며, fiber가 한 점인 covering의 가장 단순한 예이다. 반면 inseparable 확대 $$\mathbb{F}_p(t^{1/p}) \supseteq \mathbb{F}_p(t)$$는 $$\Omega\neq 0$$이므로 unramified하지 않고, étale하지도 않다.

</div>

<div class="example" markdown="1">

<ins id="ex10">**예시 10**</ins> Field $$k$$ 위의 곱셈군 $$\mathbb{G}_m=\Spec k[t, t^{-1}]$$에서 자기 자신으로의 $$n$$제곱 사상

$$[n]:\mathbb{G}_m \longrightarrow \mathbb{G}_m,\qquad t\longmapsto t^n$$

을 생각하자. 이는 ring homomorphism $$k[s, s^{-1}] \rightarrow k[t, t^{-1}]$$, $$s\mapsto t^n$$으로부터 온다. 상대미분은 $$d(t^n)=n t^{n-1}\,dt$$로 생성되므로

$$\Omega_{\mathbb{G}_m/\mathbb{G}_m}\cong k[t, t^{-1}]/(nt^{n-1})$$

이다. $$t$$가 가역이므로 이 가군은 $$k[t, t^{-1}]/(n)$$과 같다. 따라서 $$\operatorname{char}k\nmid n$$이면 $$n$$이 가역이어서 $$\Omega=0$$이고, $$[n]$$은 flat하므로 ($$k[t,t^{-1}]$$이 $$s\mapsto t^n$$ 아래 자유 가군이다) étale하다. 반면 $$\operatorname{char}k=p$$가 $$n$$을 나누면 $$\Omega\neq 0$$이 되어 $$[n]$$은 unramified하지 않고, $$p$$에서 ramification이 일어난다. 이는 표수 $$p$$에서 Frobenius가 분기를 일으키는 현상의 가장 단순한 사례이다.

</div>

위 두 예시는 étale 사상이 "분기 없는 덮개"라는 직관을 구체화한다. Separable 확대와 표수를 나누지 않는 거듭제곱 사상은 fiber가 분기 없이 균일하게 갈라지는 반면, inseparable 확대나 표수를 나누는 거듭제곱에서는 fiber가 무너지며 unramified 조건이 깨진다.

## 무한소 lifting 판정

세 개념 smooth, unramified, étale은 square-zero 확대에 대한 사상의 lifting이라는 통일된 무한소 조건으로 동시에 특징지어진다. 이것이 미분기하에서 매끄러운 사상이 무한소 변형을 항상 적분할 수 있다는 사실에 대응하며, 좌표나 fiber에 의존하지 않는 가장 개념적인 판정을 준다.

먼저 무대를 설정한다. $$T_0\hookrightarrow T$$가 affine scheme들의 닫힌 immersion이고, 그 정의 ideal $$\mathcal{J}$$가 $$\mathcal{J}^2=0$$을 만족할 때 이를 *square-zero extension<sub>제곱영 확대</sub>*이라 부른다. 대수적으로는 surjection $$R \rightarrow R_0$$의 kernel $$J$$가 $$J^2=0$$을 만족하는 상황이다.

<div class="proposition" markdown="1">

<ins id="thm11">**정리 11 (무한소 lifting 판정)**</ins> Locally of finite presentation인 사상 $$f:X \rightarrow S$$가 주어졌다 하자. 임의의 affine $$S$$-scheme $$T$$와 그 안의 square-zero 닫힌 부분scheme $$T_0\hookrightarrow T$$, 그리고 $$S$$-사상 $$g_0:T_0 \rightarrow X$$에 대하여, $$g_0$$을 $$T$$ 위로 확장하는 $$S$$-사상 $$g:T \rightarrow X$$의 존재·유일성을 다음과 같이 부른다.

![lifting diagram](/assets/images/Math/Scheme_Theory/Smooth_and_Etale_Morphisms-1.svg){:style="width:5.99em" class="invert" .align-center}

그럼 다음이 성립한다.

1. $$f$$가 smooth한 것은 모든 그러한 $$(T_0, T, g_0)$$에 대하여 lifting $$g$$가 존재하는 것과 동치이다.
2. $$f$$가 unramified한 것은 모든 그러한 $$(T_0, T, g_0)$$에 대하여 lifting $$g$$가 많아야 하나인 것과 동치이다.
3. $$f$$가 étale한 것은 모든 그러한 $$(T_0, T, g_0)$$에 대하여 lifting $$g$$가 정확히 하나 존재하는 것과 동치이다.

</div>
<details class="proof" markdown="1">
<summary>증명</summary>

(3)은 (1)과 (2)의 결합이고, étale이 smooth와 unramified의 교집합 ([정의 6](#def6))이므로 (1)과 (2)만 보이면 충분하다.

핵심은 두 lifting의 차이가 $$\Omega_{X/S}$$로 측정된다는 사실이다. $$T=\Spec R$$, $$T_0=\Spec R_0$$이고 $$J=\ker(R \rightarrow R_0)$$가 $$J^2=0$$을 만족한다 하자. $$g_0$$의 두 lifting $$g, g'$$가 주어지면, 대응하는 ring homomorphism $$B \rightarrow R$$의 차이 $$D=g^\sharp-g'^\sharp:B \rightarrow J$$는 $$J^2=0$$에 의하여 $$A$$-derivation이 된다. 실제로 $$g, g'$$이 mod $$J$$로 일치하므로 임의의 $$b, b'\in B$$에 대하여

$$D(bb')=g(b)g(b')-g'(b)g'(b')=g(b)D(b')+D(b)g'(b')\equiv g_0(b)D(b')+D(b)g_0(b')\pmod{J^2}$$

이고, $$J^2=0$$이므로 이는 정확히 Leibniz rule이다. 따라서 두 lifting의 차이는 $$\Der_A(B, J)\cong \Hom_B(\Omega_{B/A}, J)$$의 원소들과 일대일 대응한다. ([§Kähler 미분과 여접층, ⁋명제 4](/ko/math/scheme_theory/sheaf_of_differentials#prop4)에서 $$\Omega_{X/S}=\widetilde{\Omega_{B/A}}$$이고, derivation의 표현성에 의한다.)

이로부터 (2)를 얻는다. $$f$$가 unramified하면 $$\Omega_{B/A}=0$$이므로 $$\Hom_B(\Omega_{B/A}, J)=0$$이고, 따라서 두 lifting의 차이가 항상 영, 곧 lifting은 많아야 하나이다. 역으로 lifting이 항상 많아야 하나이면, $$T_0=X$$, $$T=X[\epsilon]$$를 $$\Omega_{X/S}$$의 dual로 만든 표준 square-zero 확대로 택하여 두 자명한 lifting이 일치해야 함을 보이면 $$\Der_A(B, \Omega_{B/A})$$의 항등원이 영이 되어 $$\Omega_{B/A}=0$$이 강제된다. 따라서 $$f$$는 unramified하다.

(1)을 보인다. $$f$$가 smooth하다 하자. lifting의 obstruction은 다음과 같이 분석된다. $$g_0^\sharp:B \rightarrow R_0$$이 주어졌을 때 이를 $$B \rightarrow R$$로 들어올리려면, $$B$$의 생성원의 상을 $$R$$로 임의로 올린 뒤 그것이 $$B$$의 relation을 만족하도록 $$J$$ 안에서 수정해야 한다. 이 수정의 가능 여부가 $$\Omega_{B/A}$$의 국소자유성으로 통제된다. $$B$$를 $$P=A[\x_i]$$의 quotient $$P/I$$로 표시하면, $$P \rightarrow R$$로의 lifting은 자유 다항식환이므로 항상 존재하고, 그것이 $$I$$를 $$0$$으로 보내도록 $$\Hom(I/I^2, J)$$ 안에서 수정 가능한지가 문제이다. Smooth 가정에서 conormal 완전열

$$I/I^2 \rightarrow \Omega_{P/A}\otimes B \rightarrow \Omega_{B/A} \rightarrow 0$$

이 좌측에서도 split되어 ($$\Omega_{B/A}$$가 국소자유이므로 [정리 4](#thm4)) 짧은 완전열로 분해되고, 이 split이 정확히 원하는 수정을 제공하여 lifting $$g$$가 존재한다.

역으로 모든 square-zero 확대에 대하여 lifting이 존재한다 하자. 이 lifting property를 $$T_0=X$$ 위의 conormal 확대에 적용하면, conormal 완전열 $$I/I^2 \rightarrow \Omega_{P/A}\otimes B \rightarrow \Omega_{B/A} \rightarrow 0$$의 좌측 사상이 split됨을 얻고, 따라서 $$\Omega_{B/A}$$가 국소자유이다. 또한 formal smoothness(모든 square-zero 확대에 대한 lifting의 존재)와 locally of finite presentation으로부터 local criterion of flatness를 거쳐 $$f$$가 flat임이 따른다 (표준 결과, EGA IV 17.5.1). 그러므로 [정리 4](#thm4)에 의하여 $$f$$는 smooth하다.

</details>

이 판정은 세 개념을 한 그림 안에 통합한다. 무한소 변형 $$T_0\hookrightarrow T$$를 따라 $$X$$로의 사상을 항상 적분할 수 있으면 smooth, 그 적분이 많아야 한 가지 방법으로만 가능하면 unramified, 정확히 한 가지로 가능하면 étale이다. 특히 étale 사상의 lifting이 유일하다는 것은 covering map 위에서 경로를 들어올리는 방법이 유일하다는 위상적 사실의 대수적 대응이며, 이것이 étale 사상이 대수기하에서 분기 없는 덮개와 기본군 이론의 토대가 되는 이유이다.

세 조건은 모두 base change와 합성에 대해 안정적이다. Smooth 사상의 base change는 다시 smooth하고, smooth 사상들의 합성도 smooth하며, unramified와 étale에 대해서도 마찬가지이다. 이는 위 lifting 판정이 순수하게 사상 도식의 성질로 표현되어 있어 base change와 합성 아래에서 그대로 보존되기 때문이다.

---

**참고문헌**

**[Har]** R. Hartshorne, *Algebraic geometry*. Graduate Texts in Mathematics. Springer, 1977.  
**[Vak]** R. Vakil, *The rising sea: Foundations of algebraic geometry*. Available [online](https://math.stanford.edu/~vakil/216blog/).  
**[EGA IV]** A. Grothendieck, *Éléments de géométrie algébrique IV*. Publ. Math. IHÉS, 1964–1967.  
**[Stacks]** The Stacks Project Authors, *The Stacks Project*. Available [online](https://stacks.math.columbia.edu/).
