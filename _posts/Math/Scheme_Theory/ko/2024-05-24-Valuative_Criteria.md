---
title: "값매김환"
description: "분리사상과 proper 사상을 정의하고, 이들이 위상수학의 Hausdorff 조건과 compact 조건을 대수기하학적으로 어떻게 일반화하는지 살펴본다. 이산값매김환의 구조도 함께 다룬다."
excerpt: "Valuative criteria for separated, properness"

categories: [Math / Scheme Theory]
permalink: /ko/math/scheme_theory/valuative_criteria
sidebar: 
    nav: "scheme_theory-ko"

date: 2024-05-24
weight: 15

---

이번 글에서 우리는 separated morphism과 proper morphism을 정의한다. 우리는 앞선 글들에서 open subscheme을 정의하였고 ([§스킴, ⁋정의 4](/ko/math/scheme_theory/schemes#def4)), closed embedding과 그로부터 얻어지는 closed subscheme, 그리고 ideal sheaf를 살펴보았다. ([§닫힌 부분스킴, ⁋정의 2](/ko/math/scheme_theory/closed_subschemes#def2), [닫힌 부분스킴, ⁋정의 5](/ko/math/scheme_theory/closed_subschemes#def5)) 여기에 다음의 개념들을 더한다.

::: 정의 1
Scheme morphism $\varphi: X \rightarrow Y$가 주어졌다 하자.

1. $\varphi$가 $X$와 $Y$의 open subscheme 사이의 isomorphism을 유도하면 $\varphi$를 *open embedding<sub>열린 매장</sub>*이라 부른다.
2. $\varphi$가 *projective<sub>사영사상</sub>*라는 것은 적당한 $n$에 대하여, $\varphi$를 closed embedding과 projection의 합성 $X\hookrightarrow \mathbb{P}^n_Y \rightarrow Y$의 꼴로 분해할 수 있는 것이다. ([§사영공간과 Proj 구성](/ko/math/scheme_theory/projective_schemes))
3. $\varphi$가 *quasi-projective<sub>준사영사상</sub>*라는 것은 이를 적당한 open embedding $X \rightarrow X'$와 projective morphism $X' \rightarrow Y$의 합성으로 분해할 수 있는 것이다.
:::

첫째 정의는 자명한 것이며, 둘째와 셋째 정의 또한 [\[대수다양체\] §사영다양체, ⁋정의 3](/ko/math/algebraic_varieties/projective_varieties#def3)과 [\[대수다양체\] §준사영다양체, ⁋정의 1](/ko/math/algebraic_varieties/quasi_projective_varieties#def1)을 relative 버전, 즉 $\Sch_{/Y}$에서 다룬 것이다. 

본격적인 이야기를 시작하기 전에 다음 예시를 살펴보는 것이 좋다. 

::: 예시 2
Ring $A$가 field $K$의 subring으로서 discrete valuation ring이라 하자. 즉 임의의 $x\in K^\times$에 대해 $x\in A$이거나 $x^{-1}\in A$이며, $A$는 Noetherian이고 그 maximal ideal $\mathfrak{m}$은 principal이다. ([\[가환대수학\] §인자, ⁋정의 5](/ko/math/commutative_algebra/divisors#def5)) 임의의 $x\in K^\times$가 $x$ 또는 $x^{-1}$을 통해 $A$의 원소들의 비로 표현되므로 $K=\Frac(A)$이다. 또 $A$는 $\mathfrak{m}$을 유일한 maximal ideal로 갖는 local ring이고 ([\[가환대수학\] §인자, ⁋명제 6](/ko/math/commutative_algebra/divisors#prop6)), uniformizer $\pi$를 하나 잡으면 임의의 $f\in K^\times$가 정수 $n$과 unit $u$에 대해 $f=\pi^nu$로 유일하게 표현되므로 ([\[가환대수학\] §인자, ⁋명제 8](/ko/math/commutative_algebra/divisors#prop8)) $A$의 nonzero ideal은 모두 $(\pi^n)$ 꼴이다. 특히 $A$는 principal ideal domain이며 그 prime ideal은 $(0)$과 $\mathfrak{m}=(\pi)$ 둘 뿐이다.

이로부터 $\Spec A$는 두 개의 점 $(0)$, $\mathfrak{m}$으로 이루어져 있으며,

$$Z((0))=\{(0),\mathfrak{m}\},\quad Z(\mathfrak{m})=\{\mathfrak{m}\}$$

이므로 $\Spec A$의 자명하지 않은 열린집합은

$$D(\pi)=\Spec A\setminus Z(\mathfrak{m})=\{(0)\}$$

뿐이다. 그럼 [§아핀스킴, ⁋보조정리 6](/ko/math/scheme_theory/affine_schemes#lem6)에 의하여

$$\mathcal{O}(D(\pi))\cong A_\pi\cong K$$

이다. 물론 $\mathcal{O}(\Spec A)\cong A$이다. 

한편 $\Spec A$의 두 점은 각각의 residue field를 통해 기하적으로 살펴볼 수 있다. [§아핀스킴, ⁋보조정리 8](/ko/math/scheme_theory/affine_schemes#lem8)를 사용하면

$$\mathcal{O}_{(0)}\cong A_{(0)}\cong K,\qquad \mathcal{O}_\mathfrak{m}\cong A_\mathfrak{m}$$

으로부터 

$$\kappa((0))=K, \qquad \kappa(\mathfrak{m})=A_\mathfrak{m}/\mathfrak{m}A_\mathfrak{m}\cong A/\mathfrak{m}$$

을 얻는다. 
:::

예시를 조금 더 기하적으로 살펴보자. $Z((0))=\Spec A$이므로 $(0)$의 closure는 $\Spec A$ 전체가 되고, 곧 $(0)$은 이 공간의 generic point가 된다. 이와 같은 상황은 곡선 $C$와 그 위의 점 $p$에 대해 $\mathcal{O}_{C,p}$가 discrete valuation ring일 때 특히 직관적으로 보여진다. 구체적으로 stalk

$$\mathcal{O}_{C,p}=\varinjlim_{U\ni p} \mathcal{O}(U)$$

은 점 $p$에서의 germ으로 볼 수 있으며, $\Spec \mathcal{O}_{C,p}$의 generic point $(0)$은 바로 이 데이터를 담고 있는 것이다. 그럼 남아있는 (유일한) 점 $\mathfrak{m}$은 정확하게 점 $p$에 해당하는 것으로, 이것이 $(0)$의 specialization이라는 사실이 바로 germ을 정의할 때 $p$에 한없이 가까운 근방을 살펴본다는 것을 반영한다. 

이 그림에서 $\Spec K$의 역할은 함수 쪽을 살펴보면 드러난다. $\Spec A$ 위의 함수들은 $A$ 자신, 곧 $p$에서 regular한 germ들이고, 자명하지 않은 유일한 열린집합 $D(\pi)=\{(0)\}$ 위의 함수들인 $K\cong A_\pi$의 원소는 $f=\pi^nu$의 꼴을 음의 order $n$까지 허용한 것이다. ([\[가환대수학\] §인자, ⁋명제 8](/ko/math/commutative_algebra/divisors#prop8)의 2번) 즉, 이는 $p$에서 pole을 갖되 그 order가 유한한 함수, 곧 $p$ 하나만 빼면 근방 전체에서 regular한 함수를 뜻하며, 따라서 $\Spec K$는 이 germ에서 중심 $p$를 빼내어, $p$의 정보는 잃어버린 채 $p$의 근방에 대한 정보만 가지고 있는 공간이며, canonical morphism $\Spec K \rightarrow \Spec A$는 정확히 이 그림이 정의하는 포함사상이다. 

그럼 morphism $\Spec K \rightarrow X$는 $X$ 안으로 들어가는, 점이 빠진 곡선의 germ이고, 이를 $\Spec A \rightarrow X$로 확장하는 것은 빠져 있던 그 점을 $X$ 안에서 되찾아 곡선을 이어 붙이는 것, 곧 곡선의 극한을 찾는 것이 된다. 이 extension이 많아야 하나 존재한다는 것이 separatedness이고 정확히 하나 존재한다는 것이 properness이며, 이것이 앞으로 볼 두 판정법의 내용이다. 이는 위상적으로는 Hausdorff 공간에서 극한이 유일하고 ([\[위상수학\] §하우스도르프 공간, ⁋명제 4](/ko/math/topology/Hausdorff_spaces#prop4)), compact 공간에서 극한이 항상 존재한다는 사실에 대한 대수기하 analogue이다. ([\[위상수학\] §Compactness와 paracompactness, ⁋보조정리 1](/ko/math/topology/compactness#lem1))

## 분리사상

위에서 살펴본 것과 같이, 주어진 곡선의 germ이 주어졌을 때, 그 중심 점 $p$를 채우는 방법이 많아야 하나 존재한다는 것이 separated morphism의 아이디어이다. 이를 서술하기 위해서는 다음 정의가 필요하다. 

::: 정의 3
Scheme morphism $\varphi:X \rightarrow Y$에 대하여, 두 개의 $\id_X$가 fiber product의 universal property에 의해 유도하는 유일한 morphism, 곧 다음 diagram

{% diagram Math/Scheme_Theory/Valuative_Criteria-1.svg width="13.58em" alt="diagonal_morphism" %}

의 점선 arrow $\Delta: X \rightarrow X \times_Y X$를 $\varphi$의 *diagonal morphism<sub>대각사상</sub>*이라 부른다. ([§올곱, ⁋정의 1](/ko/math/scheme_theory/fiber_products#def1)) 만일 $\Delta$가 closed embedding이라면 $\varphi$를 *separated<sub>분리사상</sub>*라 부르고, $X$가 $Y$에 대해 *separated*라 부른다. 만일 $X$가 $\Spec \mathbb{Z}$에 대해 separated이면, $X$를 간단히 *separated* scheme이라 부른다.
:::

어느 morphism의 diagonal인지를 밝혀야 할 때에는 $\Delta$ 대신 $\Delta_{X/Y}$로 적는다. 정의로부터 두 projection $\pi_1,\pi_2: X\times_YX \rightarrow X$에 대해 $\pi_1\circ\Delta=\pi_2\circ\Delta=\id_X$인 것은 자명하다. 또, $\Delta$는 단사이고 $\pi_1$을 $\Delta(X)$로 제한한 것이 $\Delta$의 연속인 역함수를 주므로, $\Delta$는 언제나 $\Delta(X)$ 위로의 homeomorphism이다. 따라서 $\Delta$가 closed embedding인지를 묻는 것은, $\Delta(X)$가 닫혀 있는지와 $X$의 함수들이 모두 $X\times_YX$의 함수를 제한하여 얻어지는지를 묻는 것이 된다. ([§닫힌 부분스킴, ⁋정의 2](/ko/math/scheme_theory/closed_subschemes#def2))

위에서 설명한 것과 같이 algebraic geometry에서는 separatedness가 Hausdorff를 대체하는 성질이라 생각한다. 위상공간 $T$가 Hausdorff인 것이 $T\times T$ 안에서 대각선이 닫혀 있는 것과 동치였음을 떠올리면 ([\[위상수학\] §하우스도르프 공간, ⁋보조정리 5](/ko/math/topology/Hausdorff_spaces#lem5)) 다음 명제를 기대하는 것이 자연스럽다. 

::: 명제 4
$\varphi:X \rightarrow Y$가 separated인 것과, diagonal morphism $\Delta: X \rightarrow X\times_YX$에 의한 $X$의 image가 닫힌집합인 것이 동치이다.
:::
::: 증명
정의에 의하여 $\varphi$가 separated라면 $\Delta(X)$가 닫혀있음은 자명하다. 따라서 $\Delta(X)$가 closed임을 가정하고, $\Delta$가 closed embedding임을 보여야 한다. 앞에서 보았듯 $\Delta$는 언제나 $\Delta(X)$ 위로의 homeomorphism이므로, 가정과 함께 위상적인 조건은 이미 확보되었고 $\mathcal{O}_{X\times_YX} \rightarrow \Delta_\ast \mathcal{O}_X$가 surjective임만 보이면 된다. 이는 stalk 위에서 체크할 수 있다.

우선 $q\notin \Delta(X)$인 점에서는 볼 것이 없다. $\Delta(X)$가 닫혀 있다는 가정으로부터 $q$의 열린근방 $W$가 존재하여 $W\cap\Delta(X)=\emptyset$이고, 그럼 $\Delta^{-1}(W)=\emptyset$이므로

$$(\Delta_\ast\mathcal{O}_X)(W)=\mathcal{O}_X(\emptyset)=0$$

이 되어 $(\Delta_\ast\mathcal{O}_X)_q=0$이기 때문이다. 아래에서 택할 열린근방들은 $\Delta(X)$ 바깥의 점을 덮지 못하므로, 가정이 실제로 쓰이는 곳은 정확히 여기이다.

이제 $\Delta(p)$ 꼴의 점을 보자. 임의의 $p\in X$에 대하여 $p$의 open affine subset $U$를 택할 수 있으며, 필요하다면 $U$를 제한하여 $\varphi(U)$가 $Y$의 어떠한 open affine subset $V$에 속하도록 할 수 있다. 그럼 $U\times_VU$는 $X\times_YX$의 열린집합으로서 $\Delta(p)$의 open neighborhood이고, $\pi_1\circ\Delta=\pi_2\circ\Delta=\id_X$이므로 $\Delta^{-1}(U\times_VU)=U$이다. 이 위에서 $\Delta: U \rightarrow U\times_VU$는 다음의 [보조정리 5](#lem5)에 의하여 closed embedding이므로 $\mathcal{O}_{U\times_VU} \rightarrow \Delta_\ast\mathcal{O}_U$가 surjective이고, 특히 $\Delta(p)$에서의 stalk 사이의 morphism이 surjective이다.
:::

그럼 이로부터 다음을 얻는다.

::: 보조정리 5
Affine scheme 사이의 임의의 morphism $\varphi:X \rightarrow Y$는 항상 separated이다.
:::
::: 증명
$X=\Spec A$, $Y=\Spec B$라 하면 $X\times_YX=\Spec(A\otimes_BA)$이고 ([§올곱, ⁋보조정리 2](/ko/math/scheme_theory/fiber_products#lem2)), $\Delta$는 ring homomorphism 

$$A\otimes_BA \rightarrow A;\quad a\otimes a'\mapsto aa'$$

으로부터 유도된다. 이 ring homomorphism은 $a\otimes 1$을 $a$로 보내므로 surjective이고, 따라서 $\Delta$는 closed embedding이다. ([§닫힌 부분스킴, ⁋명제 3](/ko/math/scheme_theory/closed_subschemes#prop3))
:::

Separated가 아닌 scheme의 예시는 [§스킴, ⁋예시 10](/ko/math/scheme_theory/schemes#ex10)에서 만든 line with double origin이 있다. 편의상 이 scheme을 $X$라 하고 이를 이루는 두 chart를 $X_1=\Spec\mathbb{K}[\x_1]$, $X_2=\Spec\mathbb{K}[\x_2]$라 하자. 이들은 $\x_1$과 $\x_2$를 동일시하여 $D(\x_1)$과 $D(\x_2)$를 따라 붙여진 것이므로, 두 chart의 교집합은 원점 두 개를 뺀

$$X_1\cap X_2=X\setminus \{0_1,0_2\}=\Spec\mathbb{K}[t,1/t]$$

이다. 여기에서 $t$는 이 gluing 아래에서 $\x_1$과 $\x_2$가 공통적으로 대응되는 좌표이다. $X$는 $\mathbb{K}$ 위의 scheme이므로 우리가 볼 것은 $X\times_\mathbb{K}X$이며, fiber product는 각 인자를 열린집합으로 제한하여 계산할 수 있으므로 ([§올곱, ⁋보조정리 4](/ko/math/scheme_theory/fiber_products#lem4)) 이는 네 개의 chart

$$X_a\times_\mathbb{K}X_b=\Spec\bigl(\mathbb{K}[\x_a]\otimes_\mathbb{K}\mathbb{K}[\x_b]\bigr)=\Spec\mathbb{K}[\x_a,\x_b]\cong \mathbb{A}^2_\mathbb{K}\qquad (a,b\in \{1,2\})$$

를 붙여 얻어진다. 이 과정에서 두 좌표가 모두 $0$이 아닌 점은 네 chart에서 모두 같은 점이 되어 한 번씩 나오며, 한 좌표만 $0$인 점은 두 번, 두 좌표가 모두 $0$인 원점은 네 번 나타난다.

이제 $\pi_1\circ\Delta=\pi_2\circ\Delta=\id_X$이므로 $\Delta^{-1}(X_a\times_\mathbb{K}X_b)=X_a\cap X_b$이다. 곧 $a=b$이면 이는 $X_a$ 전체이고 [보조정리 5](#lem5)에 의하여 그 위에서 $\Delta$는 closed embedding이며, 특히 $X$의 두 원점은 네 개의 원점 가운데 $(0_1,0_1)$과 $(0_2,0_2)$로 간다. 반면 $a\neq b$이면 $\Delta$는 $X_1\cap X_2=\Spec\mathbb{K}[t,1/t]$ 위에서 ring homomorphism

$$\mathbb{K}[\x_1,\x_2] \longrightarrow \mathbb{K}[t,1/t];\qquad \x_1,\x_2\mapsto t$$

가 유도하는 morphism이므로, chart $X_1\times_\mathbb{K}X_2\cong \mathbb{A}^2_\mathbb{K}$ 안에서 $\Delta(X)$는 대각선에서 원점을 뺀 것 $Z(\x_1-\x_2)\cap D(\x_1)$이다. 이 집합의 closure는 대각선 $Z(\x_1-\x_2)$ 전체이고 그 원점이 정확히 $(0_1,0_2)$이므로, $(0_1,0_2)$는 $\Delta(X)$에 속하지 않으면서 그 closure에는 속한다. 따라서 $\Delta(X)$는 닫혀 있지 않고 [명제 4](#prop4)에 의하여 $X$는 separated가 아니다. 이 공간은 위상적으로도 Hausdorff가 아닌 공간의 표준적인 예이다. 

이제 separatedness의 판정법을 보자. [예시 2](#ex2)에서와 달리 판정법은 discrete일 필요가 없는 valuation ring 전체, 곧 임의의 $x\in K^\times$에 대해 $x\in A$이거나 $x^{-1}\in A$라는 조건만을 만족하는 field $K$의 subring $A$ 전부에 대해 요구된다. ([\[가환대수학\] §인자, ⁋정의 5](/ko/math/commutative_algebra/divisors#def5)) 또 아래에서 $\iota:\Spec K \rightarrow \Spec A$는 언제나 inclusion $A\hookrightarrow K$가 유도하는 morphism을 가리킨다.

::: 정리 6
Noetherian scheme $X$와 scheme morphism $\varphi:X \rightarrow Y$에 대하여, $\varphi$가 separated인 것은 임의의 valuation ring $A$와 그 quotient field $K=\Frac(A)$에 대하여, 임의의 scheme morphism $\Spec A \rightarrow Y$, $\Spec K \rightarrow X$와 다음 commutative diagram

{% diagram Math/Scheme_Theory/Valuative_Criteria-2.svg width="8.34em" alt="valuative_criterion" %}

의 바깥쪽 square가 주어질 때마다, 많아야 하나의 $\Spec A \rightarrow X$가 전체 diagram이 commute하도록 하는 것이 동치이다.
:::
::: 증명
바깥쪽 square가 주어졌다는 것은 morphism $\alpha:\Spec K \rightarrow X$와 $\beta: \Spec A \rightarrow Y$가 주어져 $\varphi\circ \alpha=\beta\circ \iota$가 성립하는 것이며, 이 square의 lifting이란 $\gamma\circ \iota=\alpha$와 $\varphi\circ \gamma=\beta$를 만족하는 $\gamma:\Spec A \rightarrow X$를 말한다.

증명 전체에서 두 개의 표준적인 사실을 사용한다. 첫째는 valuation ring의 존재정리로, field $K$와 그 안의 local subring $\mathcal{O}$가 주어질 때마다 $\Frac(A)=K$이고 $\mathcal{O}\subseteq A$이며 $\mathfrak{m}_A\cap \mathcal{O}=\mathfrak{m}_\mathcal{O}$인 valuation ring $A$가 존재한다는 것이다. 이 때 $A$가 $\mathcal{O}$를 *dominate*한다고 하며, 이러한 $A$의 존재는 $\mathcal{O}$를 dominate하는 $K$의 local subring들의 모임에 Zorn's lemma를 적용하여 얻어진다. 둘째는 field $K$에 대하여 morphism $\Spec K \rightarrow X$가 점 $x\in X$와 field homomorphism $\kappa(x) \rightarrow K$의 쌍에 일대일로 대응한다는 것이다. 이는 $X=\Spec B$인 경우 ring homomorphism $B \rightarrow K$가 그 kernel인 prime ideal $\mathfrak{p}$와 $\kappa(\mathfrak{p}) \rightarrow K$의 쌍을 주는 것에서 따르고, 일반적인 경우는 $x$의 affine open neighborhood를 택하면 된다.

먼저 $\varphi$가 separated라 가정하고, 위 square의 두 lifting $\gamma_1, \gamma_2$가 주어졌다 하자. $\varphi\circ \gamma_1=\varphi\circ \gamma_2=\beta$이므로 fiber product의 universal property에 의하여 유일한 $\theta:\Spec A \rightarrow X\times_YX$가 존재하여 $\pi_1\circ \theta=\gamma_1$, $\pi_2\circ \theta=\gamma_2$이다. 여기에서 $\pi_1,\pi_2$는 두 projection이다. 이제 $\Delta$가 closed embedding이므로 base change

$$Z=\Spec A\times_{X\times_YX}X \longrightarrow \Spec A$$

또한 closed embedding이다. Closed embedding이 base change에 대해 안정적인 것은 affine-local하게 $B \rightarrow B/\mathfrak{b}$의 base change가 $C \rightarrow C\otimes_B(B/\mathfrak{b})\cong C/\mathfrak{b}C$로서 여전히 surjective인 것으로부터 얻어진다. ([§닫힌 부분스킴, ⁋명제 3](/ko/math/scheme_theory/closed_subschemes#prop3))

한편 $\pi_1\circ \theta\circ \iota=\gamma_1\circ \iota=\alpha$이고 $\pi_2\circ \theta\circ \iota=\gamma_2\circ \iota=\alpha$이며, $\pi_1\circ \Delta\circ \alpha=\alpha$이고 $\pi_2\circ\Delta\circ \alpha=\alpha$이므로 universal property의 유일성으로부터 $\theta\circ \iota=\Delta\circ \alpha$이다. 따라서 $\iota$는 pullback $Z$를 경유하고, 특히 $Z \rightarrow \Spec A$의 image는 $\iota$의 image, 곧 $A$의 zero ideal $(0)$을 포함하는 닫힌집합이다. $A$는 domain이므로 $(0)$은 $\Spec A$의 generic point이고 ([§스킴의 위상구조, ⁋예시 5](/ko/math/scheme_theory/topology_of_schemes#ex5)), 따라서 $(0)$을 포함하는 $\Spec A$의 닫힌집합은 $\Spec A$ 자신뿐이다. 그럼 $Z$는 $\Spec A$의 closed subscheme으로서 적당한 ideal $\mathfrak{a}\subseteq A$에 대해 $\Spec(A/\mathfrak{a})$의 꼴이며 ([§닫힌 부분스킴, ⁋명제 3](/ko/math/scheme_theory/closed_subschemes#prop3)), 그 image가 $\Spec A$ 전체라는 것은 $\mathfrak{a}$가 $A$의 모든 prime ideal에 포함된다는 것, 곧

$$\mathfrak{a}\subseteq \mathfrak{N}(A)=(0)$$

임을 뜻한다. 마지막 등호는 $A$가 domain이라는 사실에서 온다. 따라서 $Z \rightarrow \Spec A$는 isomorphism이고, 이는 $\theta$가 $\Delta$를 경유한다는 것, 곧 적당한 $\gamma:\Spec A \rightarrow X$에 대하여 $\theta=\Delta\circ \gamma$임을 뜻한다. 그럼

$$\gamma_1=\pi_1\circ \theta=\pi_1\circ \Delta\circ \gamma=\gamma,\qquad \gamma_2=\pi_2\circ \theta=\pi_2\circ\Delta\circ \gamma=\gamma$$

이므로 $\gamma_1=\gamma_2$이다. 이 방향에서는 $X$가 Noetherian이라는 가정이 쓰이지 않는다.

거꾸로 임의의 square에 대하여 lifting이 많아야 하나 존재한다고 가정하자. [명제 4](#prop4)에 의하여 $\Delta(X)$가 $X\times_YX$의 닫힌집합임을 보이면 충분하다.

우선 $\cl(\Delta(X))$의 모든 점이 $\Delta(X)$의 어떤 점의 specialization임을 관찰한다. $X$가 Noetherian scheme이므로 위상공간으로서도 Noetherian이고 ([§스킴의 위상구조, ⁋정의 14](/ko/math/scheme_theory/topology_of_schemes#def14)), 따라서 유한히 많은 irreducible component $X_1,\ldots, X_r$를 갖는다. ([\[위상수학\] §차원, ⁋명제 13](/ko/math/topology/dimension#prop13)) 각 $X_i$는 irreducible closed subset이므로, $X_i$와 만나는 affine open subset $U=\Spec C\subseteq X$를 택하면 $X_i\cap U$는 $U$의 irreducible closed subset으로서 generic point $\eta_i$를 가지며 ([§스펙트럼, ⁋명제 16](/ko/math/scheme_theory/spectrums#prop16)), $X_i\cap U$가 $X_i$에서 dense이므로 $\cl(\{\eta_i\})=X_i$, 곧 $X=\bigcup_{i=1}^r\cl(\{\eta_i\})$이다. 이제 $\Delta$가 연속이므로 $\Delta(X)\subseteq \bigcup_{i=1}^r \cl(\{\Delta(\eta_i)\})$이고 우변은 유한합집합이라 닫혀 있으며, 거꾸로 각 $\Delta(\eta_i)$가 $\Delta(X)$에 속하므로

$$\cl(\Delta(X))=\bigcup_{i=1}^r\cl(\{\Delta(\eta_i)\})$$

를 얻는다. 곧 $\cl(\Delta(X))$의 임의의 점은 적당한 $\Delta(\eta_i)\in \Delta(X)$의 specialization이다. ([§스킴의 위상구조, ⁋정의 2](/ko/math/scheme_theory/topology_of_schemes#def2)) 그러므로 $\Delta(X)$가 specialization에 대해 닫혀 있음을 보이면 $\Delta(X)=\cl(\Delta(X))$가 되어 증명이 끝난다.

$\xi=\Delta(x)\in \Delta(X)$이고 $\eta\in\cl(\{\xi\})$라 하자. 닫힌집합 $T=\cl(\{\xi\})$에 reduced scheme structure를 주면 ([§닫힌 부분스킴, ⁋정의 14](/ko/math/scheme_theory/closed_subschemes#def14)) $T$는 generic point $\xi$를 갖는 integral scheme이다. $\eta$를 포함하는 affine open subset $\Spec B\subseteq T$를 택하자. Generic point는 공집합이 아닌 모든 열린집합에 속하므로 $\Spec B$는 $\xi$ 또한 포함하며, $B$는 domain이고 $\xi$는 $B$의 zero ideal에 대응하므로

$$K:=\kappa(\xi)=\mathcal{O}_{T,\xi}=\Frac(B), \qquad \mathcal{O}:=\mathcal{O}_{T,\eta}=B_\mathfrak{q}\subseteq K$$

이며, 여기에서 $\mathfrak{q}$는 $\eta$에 대응하는 prime ideal이다. 특히 $\mathcal{O}$는 $\Frac(\mathcal{O})=K$인 local domain이다. 위에서 인용한 존재정리로 $\mathcal{O}$를 dominate하는 $K$의 valuation ring $A$를 택하면, local homomorphism $\mathcal{O} \rightarrow A$가 유도하는 morphism

$$\chi:\Spec A \longrightarrow \Spec \mathcal{O} \longrightarrow T \hookrightarrow X\times_YX$$

는 $\Spec A$의 generic point $(0)$을 $\xi$로, closed point $\mathfrak{m}_A$를 $\eta$로 보낸다.

이제 $\gamma_1=\pi_1\circ \chi$, $\gamma_2=\pi_2\circ \chi$라 하고, $\varphi\circ \pi_1=\varphi\circ \pi_2$이므로 잘 정의되는 $\omega=\varphi\circ \gamma_1=\varphi\circ \gamma_2:\Spec A \rightarrow Y$를 생각하자. [명제 4](#prop4)의 증명에서 보았듯 $x$의 affine open neighborhood $U$와 $\varphi(U)$를 포함하는 $Y$의 affine open subset $V$를 택하면 $U\times_VU$는 $X\times_YX$에서 $\xi$의 open neighborhood이고 그 위에서 $\Delta$는 closed embedding이므로 ([보조정리 5](#lem5)), stalk 사이의 morphism $\mathcal{O}_{X\times_YX,\xi} \rightarrow \mathcal{O}_{X,x}$는 surjective이고 따라서 $\kappa(\xi) \rightarrow \kappa(x)$ 또한 surjective이다. 한편 $\pi_1\circ\Delta=\id_X$이므로 합성 $\kappa(x) \rightarrow \kappa(\xi) \rightarrow \kappa(x)$는 항등사상이고, 그러므로 두 morphism은 서로의 역이 되는 isomorphism이다. 곧 $K=\kappa(\xi)\cong\kappa(x)$이다. 이 동일시 아래에서 점 $x$와 $\kappa(x)\cong K$가 정의하는 canonical morphism을 $\alpha:\Spec K \rightarrow X$라 하면, $\Delta\circ \alpha$는 점 $\xi$와 $\kappa(\xi)\cong K$가 정의하는 canonical morphism이고 이는 $\chi\circ \iota$와 같다. 실제로 $\chi\circ \iota$는 $\xi$를 image로 갖고 residue field 위에서 $\kappa(\xi)=\Frac(\mathcal{O})=K$의 항등사상을 유도하기 때문이다. 따라서

$$\gamma_1\circ \iota=\pi_1\circ \chi\circ \iota=\pi_1\circ \Delta\circ \alpha=\alpha,\qquad \gamma_2\circ \iota=\pi_2\circ \chi\circ \iota=\pi_2\circ\Delta\circ \alpha=\alpha$$

이고 $\varphi\circ \gamma_1=\varphi\circ \gamma_2=\omega$이므로, $\gamma_1$과 $\gamma_2$는 $\alpha$와 $\omega$가 주는 square의 두 lifting이다. 가정에 의하여 $\gamma_1=\gamma_2$이고, 그럼 $\Delta\circ \gamma_1$과 $\chi$는 $\pi_1$, $\pi_2$와 합성했을 때 각각 $\gamma_1$과 $\gamma_2=\gamma_1$을 주므로 fiber product의 universal property에 의해 $\chi=\Delta\circ \gamma_1$이다. 그러므로

$$\eta=\chi(\mathfrak{m}_A)=\Delta(\gamma_1(\mathfrak{m}_A))\in \Delta(X)$$

이고, $\Delta(X)$는 specialization에 대해 닫혀 있다. 앞의 관찰과 결합하면 $\Delta(X)=\cl(\Delta(X))$이므로 $\Delta(X)$는 닫힌집합이고, [명제 4](#prop4)에 의하여 $\varphi$는 separated이다.
:::

직관적으로 $\Spec A$는 generic point $(0)$과 그것이 specialize되는 closed point $\mathfrak{m}_A$로 이루어져 있으며, 그 중 generic point는 조건 $\gamma\circ \iota=\alpha$에 의해 $\alpha$의 image $\xi$로 가야 하므로, lifting $\gamma:\Spec A \rightarrow X$를 준다는 것은 $\eta\in \cl(\{\xi\})$인 점 $\eta=\gamma(\mathfrak{m}_A)$를 하나 지정하는 것, 곧 주어진 germ의 극한을 $X$ 안에서 고르는 것이다. 그러므로 lifting이 많아야 하나라는 것은 하나의 germ이 서로 다른 두 극한으로 갈라지지 않는다는 뜻이며, 증명이 보여주듯 이것이 정확히 $\Delta(X)$가 specialization에 대해 닫혀 있다는 위상적 조건이 된다. 거꾸로 $X$ 안의 임의의 specialization을 이러한 germ으로 실현해 주는 것이 증명에서 쓴 valuation ring의 존재정리이고, 판정법이 discrete인 것뿐 아니라 임의의 valuation ring에 대하여 요구되는 것도 이 때문이다. 다만 일반적인 valuation ring의 $\Spec$은 prime ideal들이 더 긴 사슬을 이루어 [예시 2](#ex2)의 두 점짜리 그림에서 벗어나는데, $Y$가 Noetherian이고 $\varphi$가 finite type morphism이라면 위의 정리를 임의의 discrete valuation ring에 대한 것으로 대체해도 되므로 그 그림이 그대로 살아난다. 이 사실에 대한 증명은 현재 우리 상태에서는 할 수 없으므로 넘기기로 한다. 

이 그림을 실제로 확인해 보자.

::: 예시 7
앞에서 우리는 line with double origin $X$가 separated가 아님을 [명제 4](#prop4)로 확인했지만, [정리 6](#thm6)을 쓰면 같은 사실이 곡선의 극한이라는 말로 그대로 드러난다. $A=\mathbb{K}[t]_{(t)}$는 uniformizer $t$를 갖는 discrete valuation ring이고 $K=\Frac(A)=\mathbb{K}(t)$이며, $Y=\Spec\mathbb{K}$로 둔다. 이제 ring homomorphism $\mathbb{K}[\x_1] \rightarrow K$, $\x_1\mapsto t$가 정의하는 morphism $\alpha:\Spec K \rightarrow X$를 생각하자. $t$는 $K$의 unit이므로 $\alpha$의 image는 두 chart가 겹치는 열린집합에 들어간다. 모든 것이 $\mathbb{K}$ 위에 있으므로 $\alpha$와 구조사상 $\Spec A \rightarrow \Spec\mathbb{K}$는 바깥쪽 square를 이룬다.

이제 앞에서와 같이 두 chart를 $X_1=\Spec\mathbb{K}[\x_1]$, $X_2=\Spec\mathbb{K}[\x_2]$라 하고, 이들로 들어가는 두 morphism

$$\gamma_1:\Spec A \longrightarrow X_1\subseteq X,\qquad \gamma_2:\Spec A \longrightarrow X_2\subseteq X$$

를 각각 $\x_1\mapsto t$와 $\x_2\mapsto t$로 정의하면 둘 다 $t\in A$이므로 잘 정의된다. 두 chart는 원점 바깥에서 $\x_1$과 $\x_2$를 동일시하여 붙여졌으므로 $\gamma_1\circ \iota=\gamma_2\circ \iota=\alpha$이고, 따라서 둘 다 이 square의 lifting이다. 그러나 $\gamma_1$은 $\mathfrak{m}_A=(t)$를 첫 번째 chart의 원점 $0_1$로, $\gamma_2$는 두 번째 chart의 원점 $0_2$로 보내므로 $\gamma_1\neq \gamma_2$이다. 곧 점이 빠진 곡선의 germ이 두 개의 극한을 가지며, 이것이 $X$가 separated가 아닌 이유이다.
:::

한편 [정리 6](#thm6)으로부터 다음을 얻는다.

::: 따름정리 8
Noetherian scheme들에 대하여, 

1. Open embedding과 closed embedding은 모두 separated이다.
2. 두 separated morphism의 합성은 separated이다.
3. Separated morphism은 base change에 의해 보존된다.
4. Separated morphism은 fiber product에 의해 보존된다.
5. 만일 $\varphi:X \rightarrow Y$, $\psi:Y \rightarrow Z$가 scheme morphism들이고 $\psi\circ \varphi$가 separated morphism이라면 $\varphi$ 또한 separated morphism이다.
:::
::: 증명
1번은 정의에서 직접 확인한다. $\varphi$가 closed embedding이라면 $Y$의 affine open subset $V=\Spec B$마다 $\varphi^{-1}(V)=\Spec A$이고 $B \rightarrow A$가 surjective이며 ([§닫힌 부분스킴, ⁋명제 3](/ko/math/scheme_theory/closed_subschemes#prop3)), 이러한 $V$를 모두 모으면 $\varphi^{-1}(V)\times_V\varphi^{-1}(V)$들이 $X\times_YX$를 덮는다. 각각의 위에서 $\Delta$는 [보조정리 5](#lem5)의 계산에 의하여 closed embedding이고, closed embedding은 target에 대해 affine-local하므로 $\Delta$ 자체가 closed embedding이다. $\varphi$가 open embedding이라면 $X$를 $Y$의 open subscheme으로 보고 $Y$의 affine open subset $V=\Spec B$들과 그 안에 들어가는 $X$의 basic open subset $\Spec B_b$들을 생각하자. 그럼 $\Spec B_b\times_V\Spec B_{b'}$들이 $X\times_YX$를 덮으며,

$$B_b\otimes_BB_{b'}\cong B_{bb'}=\mathcal{O}(\Spec B_b\cap \Spec B_{b'})$$

이므로 $\Delta$는 각각의 위에서 isomorphism이고 특히 closed embedding이다.

나머지는 [정리 6](#thm6)의 판정법으로 얻어진다. 곧 lifting의 유일성이 물려받아진다는 것만 확인하면 된다.

2번의 경우 $\psi\circ \varphi$에 대한 바깥쪽 square $\alpha:\Spec K \rightarrow X$, $\beta:\Spec A \rightarrow Z$와 두 lifting $\gamma_1,\gamma_2:\Spec A \rightarrow X$가 주어졌다 하자. 그럼 $\varphi\circ \gamma_1$과 $\varphi\circ \gamma_2$는 $\alpha' = \varphi\circ \alpha$와 $\beta$가 주는 $\psi$에 대한 square의 두 lifting이므로 $\varphi\circ \gamma_1=\varphi\circ \gamma_2$이고, 그럼 $\gamma_1,\gamma_2$는 $\alpha$와 $\varphi\circ \gamma_1$이 주는 $\varphi$에 대한 square의 두 lifting이므로 $\gamma_1=\gamma_2$이다.

3번의 경우 $Y' \rightarrow Y$와 $X'=X\times_YY'$, $\varphi':X' \rightarrow Y'$에 대하여 $\varphi'$에 대한 square와 그 두 lifting $\gamma_1',\gamma_2':\Spec A \rightarrow X'$가 주어졌다 하자. 이들을 $X' \rightarrow X$와 합성한 것은 $\varphi$에 대한 square의 두 lifting이므로 서로 같고, $Y'$로 가는 두 합성 또한 square가 주는 같은 morphism이므로, fiber product의 universal property의 유일성에서 $\gamma_1'=\gamma_2'$이다.

5번의 경우 $\varphi$에 대한 square와 두 lifting $\gamma_1,\gamma_2$가 주어지면, $\Spec A \rightarrow Y$를 $\psi$와 합성하여 $\psi\circ \varphi$에 대한 square를 얻고 $\gamma_1,\gamma_2$는 그 두 lifting이므로 $\gamma_1=\gamma_2$이다.

끝으로 4번은 $S$-scheme들 사이의 separated morphism $\varphi:X \rightarrow Y$, $\varphi':X' \rightarrow Y'$에 대하여 $\varphi\times \varphi'$가 합성

$$X\times_SX' \longrightarrow Y\times_SX' \longrightarrow Y\times_SY'$$

으로 분해되고 두 morphism이 각각 $\varphi$와 $\varphi'$의 base change이므로, 3번과 2번에서 따라온다. 
:::

특히 2번과 5번을 함께 쓰면, $Y$가 separated scheme일 때 $Y$-scheme $X$가 separated scheme인 것과 그 구조사상 $X \rightarrow Y$가 separated인 것이 동치임을 안다. Affine scheme은 [보조정리 5](#lem5)에 의하여 언제나 separated scheme이므로, 가령 affine scheme 위의 scheme에 대해서는 separatedness를 구조사상만 보고 판정할 수 있다.

Separatedness는 두 morphism이 언제 같은지를 판정하는 데에도 쓰인다. Reduced scheme $X$와 separated scheme $Y$, 그리고 $X$의 dense open subset $W$ 위에서 일치하는 두 morphism $\varphi,\psi: X \rightarrow Y$가 주어졌다 하자. 그럼 $\varphi$와 $\psi$가 유도하는 morphism $\theta: X \rightarrow Y\times_{\Spec \mathbb{Z}}Y$에 대하여 $\varphi$와 $\psi$가 일치하는 부분은 $\Delta$를 $\theta$를 따라 base change한 것으로 주어지고, closed embedding의 base change는 다시 closed embedding이므로 ([정리 6](#thm6)의 증명) 이는 $X$의 closed subscheme이다. 이 closed subscheme이 $W$를 포함하여 위상적으로 $X$ 전체이므로, 이를 정의하는 ideal sheaf는 $X$의 각 affine open subset $\Spec A$ 위에서 $\mathfrak{N}(A)=0$에 포함되고 ([§닫힌 부분스킴, ⁋명제 3](/ko/math/scheme_theory/closed_subschemes#prop3)), 따라서 $\varphi=\psi$이다. 이를 [§스킴 사상의 성질들, ⁋정의 22](/ko/math/scheme_theory/properties_of_scheme_morphisms#def22)에 적용하면, $Y$가 separated이고 $X$가 reduced일 때 rational map의 동치관계는 두 representative가 $U\cap V$ 전체에서 일치한다는 조건과 같아진다. 그 글에서는 $Y$가 affine인 경우로 이를 확인하였으며, affine scheme이 언제나 separated인 만큼 이는 위 논증의 특수한 경우이다.

## 고유사상

이제 compact 조건에 대응하는 성질로 넘어간다. 위상수학에서 우리는 compactness를 universally closed라는 조건으로 바꾸어 쓸 수 있음을 보았고 ([\[위상수학\] §고유함수, ⁋정리 6](/ko/math/topology/proper_maps#thm6)), 대수기하에서는 곱을 fiber product로 바꾼 이 조건이 그대로 정의가 된다.

::: 정의 9
$\varphi:X \rightarrow Y$가 *universally closed<sub>보편닫힌사상</sub>*라는 것은 $\varphi$가 closed map이고, 임의의 $Y' \rightarrow Y$에 대해서도 $X\times_Y Y' \rightarrow Y'$가 closed인 것이다. Separated, universally closed인 finite type morphism을 *proper morphism<sub>고유사상</sub>*이라 부른다. 
:::

$Y'=Y$로 두면 두 번째 조건이 첫 번째 조건을 포함하므로, 실질적인 조건은 모든 base change가 closed map이라는 것 하나이다. 한편 우리는 이 절에서 Noetherian scheme들의 범주 안에서 작업하므로, 앞으로 universally closed를 확인할 때 base change $Y' \rightarrow Y$는 Noetherian scheme에 대한 것만 생각한다. 임의의 $Y'$에 대한 조건이 이로부터 따라온다는 것은 $Y'$를 affine으로 제한한 뒤 그 coordinate ring을 finitely generated subalgebra들의 filtered colimit으로 쓰는 극한 논법에서 얻어지며, 이는 이 글의 범위를 벗어나므로 생략하기로 한다.

Proper morphism은 separated 조건과 universally closed 조건을 함께 요구하므로, 판정법 또한 두 조각으로 나뉜다. [정리 6](#thm6)이 lifting의 유일성으로 separatedness를 판정했으니, 남은 것은 lifting의 존재성이 universal closedness를 판정한다는 것이다.

::: 명제 10
Noetherian scheme들 사이의 finite type scheme morphism $\varphi:X \rightarrow Y$에 대하여, $\varphi$가 universally closed인 것은 임의의 valuation ring $A$와 그 quotient field $K=\Frac(A)$에 대하여, 임의의 scheme morphism $\Spec A \rightarrow Y$, $\Spec K \rightarrow X$와 다음 commutative diagram

{% diagram Math/Scheme_Theory/Valuative_Criteria-2.svg width="8.34em" alt="valuative_criterion" %}

의 바깥쪽 square가 주어질 때마다, 적어도 하나의 $\Spec A \rightarrow X$가 존재하여 전체 diagram이 commute하는 것과 동치이다.
:::
::: 증명
[정리 6](#thm6)의 증명에서와 같이 바깥쪽 square를 $\alpha:\Spec K \rightarrow X$, $\beta:\Spec A \rightarrow Y$, $\iota:\Spec K \rightarrow \Spec A$로 적고, 그 증명에서 인용한 두 표준적인 사실을 계속 사용한다. 곧 field $K$ 안의 local subring은 항상 $\Frac(A)=K$인 valuation ring $A$에 의해 dominate되며, morphism $\Spec K \rightarrow X$는 점 $x\in X$와 field homomorphism $\kappa(x) \rightarrow K$의 쌍과 같은 것이다. 여기에 valuation ring의 다음 극대성을 덧붙인다. 만일 $K$의 valuation ring $A$를 dominate하는 local subring $\mathcal{O}\subseteq K$가 주어졌다면 $\mathcal{O}=A$이다. 실제로 $c\in\mathcal{O}$가 $0$이 아니고 $c\notin A$라면 valuation ring의 정의에 의해 $c^{-1}\in A$이며, $c\notin A$이므로 $c^{-1}$은 $A$의 unit이 아니다. 곧 $c^{-1}\in\mathfrak{m}_A\subseteq \mathfrak{m}_\mathcal{O}$인데 $c\in\mathcal{O}$이므로 $c^{-1}$은 $\mathcal{O}$의 unit이 되어 모순이다. 따라서 $\mathcal{O}\subseteq A$이고, dominate의 정의에서 $A\subseteq\mathcal{O}$이므로 $\mathcal{O}=A$이다.

먼저 $\varphi$가 universally closed라 하고 lifting을 만들자. $\beta$를 따라 base change하여 $X_A=X\times_Y\Spec A$와 projection $\pi:X_A \rightarrow \Spec A$를 얻으면 $\pi$는 closed map이다. ([정의 9](#def9)) 한편 $\alpha$와 $\iota$는 fiber product의 universal property에 의해 $\Spec A$ 위의 morphism $\tilde{\alpha}:\Spec K \rightarrow X_A$를 유도하며, $\Spec A \rightarrow X_A$ 꼴의 $\pi$의 section으로서 $\tilde{\alpha}$를 extend하는 것을 찾으면 이를 $X$로 project하여 원하는 lifting을 얻는다.

$\xi\in X_A$를 $\tilde{\alpha}$의 image가 되는 점이라 하고 $Z=\cl(\{\xi\})$에 reduced scheme structure를 주자. ([§닫힌 부분스킴, ⁋정의 14](/ko/math/scheme_theory/closed_subschemes#def14)) $\pi\circ\tilde{\alpha}=\iota$이므로 $\pi(\xi)$는 $\Spec A$의 generic point $(0)$이고, $\pi$가 closed map이므로 $\pi(Z)$는 $(0)$을 포함하는 닫힌집합, 곧 $\Spec A$ 전체이다. 따라서 $\pi(z)=\mathfrak{m}_A$인 $z\in Z$가 존재한다.

Residue field들을 살펴보자. $\pi\circ \tilde{\alpha}=\iota$가 $(0)$에서 유도하는 morphism $\kappa((0))=K \rightarrow K$는 항등사상이고, 이것은 $\pi$가 유도하는 $K\rightarrow\kappa(\xi)$와 $\tilde{\alpha}$가 유도하는 $\kappa(\xi) \rightarrow K$의 합성이므로 두 morphism은 서로의 역이 되는 isomorphism이다. 곧 $\kappa(\xi)\cong K$이다. 그럼 $Z$는 generic point $\xi$를 갖는 integral scheme이므로, [정리 6](#thm6)의 증명에서와 같이 $z$를 포함하는 affine open subset을 택하여

$$\mathcal{O}:=\mathcal{O}_{Z,z}\subseteq \kappa(\xi)=K,\qquad \Frac(\mathcal{O})=K$$

임을 안다. 또 $\pi\vert_Z$가 유도하는 morphism $A=\mathcal{O}_{\Spec A,\mathfrak{m}_A} \rightarrow \mathcal{O}_{Z,z}$는 local homomorphism이며, generic point에서 이것이 유도하는 $K \rightarrow \kappa(\xi)=K$가 항등사상이므로 이 morphism은 $K$의 subring 사이의 포함사상이다. 곧 $\mathcal{O}$는 $A$를 dominate하는 $K$의 local subring이고, 위의 극대성에 의하여 $\mathcal{O}_{Z,z}=A$이다.

그럼 canonical morphism $\Spec A=\Spec\mathcal{O}_{Z,z} \rightarrow Z \hookrightarrow X_A$를 얻고, 이것과 $\pi$의 합성은 ring 수준에서 $A$의 항등사상에 대응하므로 $\pi$의 section이다. 이 section을 $\Spec K$로 제한한 것은 $\xi$를 image로 갖고 residue field 위에서 $\kappa(\xi)=K$의 항등사상을 유도하므로 $\tilde{\alpha}$와 같다. 따라서 이 section을 $X$로 project하면 $\gamma\circ \iota=\alpha$이고 $\varphi\circ \gamma=\beta$인 $\gamma:\Spec A \rightarrow X$를 얻는다.

거꾸로 존재성 부분이 성립한다고 가정하자. [정의 9](#def9) 이후에 밝힌 규약대로 base change $Y' \rightarrow Y$는 Noetherian scheme에 대한 것만 생각한다.

우선 존재성 부분이 base change에 대해 안정적이다. $Y' \rightarrow Y$와 $X'=X\times_YY'$, $\varphi':X' \rightarrow Y'$가 주어졌다 하고, $\Spec K \rightarrow X'$와 $\Spec A \rightarrow Y'$가 $\varphi'$에 대한 바깥쪽 square를 이룬다 하자. 이들을 $X' \rightarrow X$, $Y' \rightarrow Y$와 합성하면 $\varphi$에 대한 바깥쪽 square를 얻으므로 lifting $\gamma:\Spec A \rightarrow X$가 존재하고, $\gamma$와 $\Spec A \rightarrow Y'$는 universal property에 의해 유일한 $\gamma':\Spec A \rightarrow X'$를 준다. $\gamma'\circ \iota$와 주어진 $\Spec K \rightarrow X'$는 $X' \rightarrow X$, $X' \rightarrow Y'$와 합성한 결과가 각각 같으므로 서로 같고, 따라서 $\gamma'$는 $\varphi'$에 대한 lifting이다. 한편 finite type morphism은 base change에 대해 안정적이고 Noetherian scheme 위의 finite type scheme은 다시 Noetherian이므로, $X'$는 Noetherian이고 $\varphi'$는 finite type이다. 따라서 Noetherian scheme $X$와 finite type morphism $\varphi:X \rightarrow Y$가 판정법의 존재성 부분을 만족할 때 $\varphi$가 closed map임을 보이면, 이를 모든 base change에 적용하여 증명이 끝난다.

이를 보이기 위해 $X$의 닫힌집합 $T$를 택하고 reduced scheme structure를 주자. Closed embedding $T\hookrightarrow X$는 finite morphism이므로 ([§닫힌 부분스킴, ⁋명제 4](/ko/math/scheme_theory/closed_subschemes#prop4)) finite type이고, 따라서 $T$는 Noetherian scheme이며 $\varphi\vert_T:T \rightarrow Y$ 또한 finite type이다. 또 $\varphi\vert_T$는 판정법의 존재성 부분을 물려받는다. 실제로 $\Spec K \rightarrow T$와 $\Spec A \rightarrow Y$가 $\varphi\vert_T$에 대한 square를 이루면, $\Spec K \rightarrow T\hookrightarrow X$에 판정법을 적용하여 lifting $\gamma_0:\Spec A \rightarrow X$를 얻는다. $\Spec A$의 모든 점은 generic point $(0)$의 specialization이고 morphism은 specialization을 보존하므로 $\gamma_0(\Spec A)\subseteq \cl(\{\gamma_0((0))\})\subseteq T$이며, $\Spec A$는 reduced이므로 $\gamma_0$는 $T$를 경유한다. 여기에서 마지막 사실은 다음과 같이 얻어진다. Reduced scheme $S$에서의 morphism $\psi:S \rightarrow X$의 image가 닫힌집합 $T$에 들어간다 하고, $X$의 affine open subset $\Spec B$와 $\psi^{-1}(\Spec B)$의 affine open subset $\Spec R$을 택하자. $T\cap \Spec B=Z(\mathfrak{b})$ ($\mathfrak{b}$는 radical ideal)라 하면 $T$의 reduced structure는 그 위에서 $\Spec (B/\mathfrak{b})$이고, 대응하는 ring homomorphism $\phi:B \rightarrow R$는 임의의 prime ideal $\mathfrak{p}\subseteq R$에 대해 $\mathfrak{b}\subseteq \phi^{-1}(\mathfrak{p})$를 만족하므로

$$\phi(\mathfrak{b})\subseteq \bigcap_{\mathfrak{p}\in\Spec R}\mathfrak{p}=\mathfrak{N}(R)=(0)$$

이다. 곧 $\phi$는 $B/\mathfrak{b}$를 유일하게 경유하고, 이렇게 얻어진 local factorization들은 유일성에 의해 붙는다.

따라서 $\varphi(T)=\varphi\vert_T(T)$가 닫힌집합임을 보이면 되고, 결국 판정법의 존재성 부분을 만족하는 finite type morphism $\varphi:X \rightarrow Y$ (단 $X$는 Noetherian)의 image $\varphi(X)$가 닫혀 있음을 보이면 충분하다.

$\varphi(X)$가 specialization에 대해 닫혀 있음을 먼저 본다. $y_1=\varphi(x_1)\in \varphi(X)$이고 $y_0\in\cl(\{y_1\})$이라 하자. $W=\cl(\{y_1\})$에 reduced scheme structure를 주면 $W$는 generic point $y_1$을 갖는 integral scheme이고, 앞에서와 같이 $\mathcal{O}=\mathcal{O}_{W,y_0}$는 $\Frac(\mathcal{O})=\kappa(y_1)$인 local domain이다. 이제 $K=\kappa(x_1)$이라 하고 $\varphi$가 유도하는 field homomorphism $\kappa(y_1)\hookrightarrow K$를 통해 $\mathcal{O}$를 $K$의 local subring으로 보자. 그럼 $\mathcal{O}$를 dominate하는 $K$의 valuation ring $A$가 존재하고, 이로부터 두 morphism

$$\Spec A \longrightarrow \Spec\mathcal{O} \longrightarrow W\hookrightarrow Y,\qquad \alpha:\Spec K \longrightarrow X$$

를 얻는다. 여기에서 $\alpha$는 점 $x_1$과 $\kappa(x_1)=K$가 정의하는 canonical morphism이다. 이 둘은 바깥쪽 square를 이루는데, $\Spec K \rightarrow Y$로 가는 두 합성이 모두 점 $y_1$과 field homomorphism $\kappa(y_1)\hookrightarrow K$가 정의하는 canonical morphism이기 때문이다. 판정법의 존재성에 의하여 lifting $\gamma_0:\Spec A \rightarrow X$가 존재하고, $\Spec A \rightarrow \Spec\mathcal{O}$가 local homomorphism에서 오므로 $\mathfrak{m}_A$는 $\mathfrak{m}_\mathcal{O}$, 곧 $y_0$으로 간다. 따라서 $\varphi(\gamma_0(\mathfrak{m}_A))=y_0$이고 $y_0\in \varphi(X)$이다.

끝으로 [정리 6](#thm6)의 증명에서의 위상적인 관찰을 그대로 반복한다. $X$의 irreducible component들 $X_1,\ldots,X_r$의 generic point를 $\eta_1,\ldots,\eta_r$이라 하면 $X=\bigcup_{i=1}^r\cl(\{\eta_i\})$이므로

$$\cl(\varphi(X))=\bigcup_{i=1}^r\cl(\{\varphi(\eta_i)\})$$

이고, 따라서 $\cl(\varphi(X))$의 모든 점은 $\varphi(X)$의 점의 specialization이다. 앞에서 $\varphi(X)$가 specialization에 대해 닫혀 있음을 보였으므로 $\varphi(X)=\cl(\varphi(X))$이다. 
:::

그럼 두 조각을 합치면 properness의 판정법을 얻는다.

::: 정리 11
Noetherian scheme들 사이의 finite type scheme morphism $\varphi:X \rightarrow Y$에 대하여, $\varphi$가 proper인 것은 임의의 valuation ring $A$와 그 quotient field $K=\Frac(A)$에 대하여, 임의의 scheme morphism $\Spec A \rightarrow Y$, $\Spec K \rightarrow X$와 다음 commutative diagram

{% diagram Math/Scheme_Theory/Valuative_Criteria-2.svg width="8.34em" alt="valuative_criterion" %}

의 바깥쪽 square가 주어질 때마다, 정확히 하나의 $\Spec A \rightarrow X$가 존재하여 전체 diagram이 commute하는 것이 동치이다.
:::
::: 증명
$\varphi$는 finite type이라 가정되어 있으므로, [정의 9](#def9)에 의하여 $\varphi$가 proper인 것은 $\varphi$가 separated이고 universally closed인 것이다. [정리 6](#thm6)에 의하여 $\varphi$가 separated인 것은 임의의 바깥쪽 square가 많아야 하나의 lifting을 갖는 것이고, [명제 10](#prop10)에 의하여 $\varphi$가 universally closed인 것은 임의의 바깥쪽 square가 적어도 하나의 lifting을 갖는 것이다. 두 조건이 함께 성립하는 것이 곧 모든 square가 정확히 하나의 lifting을 갖는 것이다.
:::

판정법이 실패하는 모습을 보아 두는 것이 좋다. [예시 7](#ex7)이 유일성이 깨지는 경우였다면, 다음은 존재성이 깨지는 경우이다.

::: 예시 12
$\mathbb{A}^1_\mathbb{K}=\Spec\mathbb{K}[\x]$는 $\Spec\mathbb{K}$ 위에서 proper가 아니다. $A=\mathbb{K}[t]_{(t)}$와 $K=\Frac(A)=\mathbb{K}(t)$를 택하고, ring homomorphism

$$\mathbb{K}[\x] \longrightarrow K;\qquad \x\mapsto 1/t$$

가 정의하는 morphism $\alpha:\Spec K \rightarrow \mathbb{A}^1_\mathbb{K}$를 생각하자. 모든 것이 $\mathbb{K}$ 위에 있으므로 $\alpha$와 구조사상 $\Spec A \rightarrow \Spec\mathbb{K}$는 바깥쪽 square를 이룬다. 만일 lifting $\gamma:\Spec A \rightarrow \mathbb{A}^1_\mathbb{K}$가 존재한다면 이는 ring homomorphism $\mathbb{K}[\x] \rightarrow A$에 대응하고, $\gamma\circ \iota=\alpha$라는 조건은 이 homomorphism과 $A\hookrightarrow K$의 합성이 $\x$를 $1/t$로 보낸다는 것이다. 곧 $1/t\in A$여야 하는데 $t$는 $A$의 uniformizer이므로 이는 불가능하다. 따라서 lifting이 존재하지 않고, [정리 11](#thm11)에 의하여 $\mathbb{A}^1_\mathbb{K} \rightarrow \Spec\mathbb{K}$는 proper가 아니다.

기하적으로 이 $\alpha$는 원점에서 무한대로 달아나는 곡선의 germ이며, 판정법은 $\mathbb{A}^1_\mathbb{K}$ 안에 그 극한이 없다는 것을 그대로 읽어낸 것이다. 같은 계산을 $\mathbb{P}^1_\mathbb{K}$에서 하면 $1/t$는 무한대에 대응하는 chart에서 $t$가 되어 lifting이 존재하며, 이것이 [정리 15](#thm15)에서 일반화된다.
:::

마찬가지로 다음 따름정리가 성립한다.

::: 따름정리 13
Noetherian scheme들에 대하여,

1. Closed embedding은 proper이다.
2. Proper morphism들의 합성은 proper이다. 
3. Proper morphism은 base change에 의해 보존된다.
4. Proper morphism은 fiber product에 의해 보존된다.
5. 만일 $\varphi:X \rightarrow Y$, $\psi:Y \rightarrow Z$가 scheme morphism들이고 $\psi$가 separated이며 $\psi\circ \varphi$가 proper morphism이라면 $\varphi$ 또한 proper morphism이다.
:::
::: 증명
1번의 경우 closed embedding은 [따름정리 8](#cor8)의 1번에 의하여 separated이고, finite morphism이므로 ([§닫힌 부분스킴, ⁋명제 4](/ko/math/scheme_theory/closed_subschemes#prop4)) finite type이다. 또 closed embedding은 closed map이며 base change에 대해 안정적이므로 ([정리 6](#thm6)의 증명) universally closed이다.

2번의 경우 separated는 [따름정리 8](#cor8)의 2번이고 finite type morphism의 합성은 finite type이므로, universally closed만 보이면 된다. $Z' \rightarrow Z$가 주어졌다 하면 $X\times_ZZ'=X\times_Y(Y\times_ZZ')$이므로

$$X\times_ZZ' \longrightarrow Y\times_ZZ' \longrightarrow Z'$$

의 두 morphism은 각각 $\varphi$와 $\psi$의 base change이고, 따라서 둘 다 closed map이다. Closed map의 합성은 closed map이므로 $X\times_ZZ' \rightarrow Z'$ 또한 closed이다.

3번의 경우 separated는 [따름정리 8](#cor8)의 3번, finite type은 base change에 대한 안정성이고, universally closed는 base change의 base change가 다시 base change라는 것에서 정의상 바로 얻어진다. 이어서 4번은 [따름정리 8](#cor8)의 4번에서와 같은 분해를 2번과 3번에 적용하면 된다.

끝으로 5번을 보자. $\id_X$와 $\varphi$가 유도하는 graph morphism $\Gamma_\varphi:X \rightarrow X\times_ZY$를 생각하면 $\varphi=\pi_2\circ\Gamma_\varphi$이다. 이 때 $\Gamma_\varphi$와 $\varphi\times\id_Y: X\times_ZY \rightarrow Y\times_ZY$가 이루는 square는 $\Delta_{Y/Z}:Y \rightarrow Y\times_ZY$를 밑변으로 하는 cartesian square이다. 실제로 임의의 $T$에 대하여 $Y\times_ZY$로 가는 두 morphism을 맞추는 것은 $\alpha:T \rightarrow X$와 $\beta:T \rightarrow Y$의 쌍 가운데 $\varphi\circ \alpha=\beta$인 것을 고르는 일이고, 이러한 쌍은 $\alpha$ 하나가 결정하기 때문이다. 그럼 $\psi$가 separated라는 가정에서 $\Delta_{Y/Z}$가 closed embedding이므로 $\Gamma_\varphi$ 또한 closed embedding이고, 1번에 의하여 proper이다. 한편 $\pi_2:X\times_ZY \rightarrow Y$는 $\psi\circ \varphi$를 $\psi$를 따라 base change한 것이므로 3번에 의하여 proper이다. 따라서 2번에 의하여 $\varphi=\pi_2\circ\Gamma_\varphi$는 proper이다.
:::

5번에서 $\psi$가 separated라는 가정이 붙는 것은, 증명에서 $\Gamma_\varphi$가 closed embedding이 되는 근거가 정확히 $\Delta_{Y/Z}$가 closed embedding이라는 것이기 때문이다. 이 가정이 없으면 $\Gamma_\varphi$가 closed embedding이라는 보장이 사라지고 논증이 작동하지 않는다. [따름정리 8](#cor8)의 5번에는 이러한 가정이 필요하지 않았으므로, 두 항목의 모양이 서로 다르다는 점에 주의해야 한다.

한편 [따름정리 13](#cor13)의 1번은 다음의 특수한 경우이다. 이는 판정법이 실제로 어떻게 쓰이는지를 보여주는 가장 전형적인 예로, valuation ring이 integrally closed라는 사실 하나로 존재성이 나온다.

::: 따름정리 14
Noetherian scheme들 사이의 finite morphism은 proper이다.
:::
::: 증명
Finite morphism $\varphi:X \rightarrow Y$는 affine morphism이므로 임의의 affine open subset $V\subseteq Y$에 대하여 $\varphi^{-1}(V)$가 affine이고, 따라서 [보조정리 5](#lem5)와 closed embedding의 affine-local 판정에 의하여 ([§닫힌 부분스킴, ⁋명제 3](/ko/math/scheme_theory/closed_subschemes#prop3)) $\varphi$는 separated이다. 또 finite morphism은 finite type이다. ([§스킴 사상의 성질들, ⁋명제 15](/ko/math/scheme_theory/properties_of_scheme_morphisms#prop15)) 그러므로 [정리 11](#thm11)에 의하여 lifting의 존재성만 확인하면 된다.

바깥쪽 square $\alpha:\Spec K \rightarrow X$, $\beta:\Spec A \rightarrow Y$가 주어졌다 하자. $\Spec A$의 모든 점은 generic point $(0)$의 specialization이고 morphism은 specialization을 보존하므로, $\beta(\mathfrak{m}_A)$를 포함하는 $Y$의 affine open subset $V=\Spec B$를 택하면 $V$는 $\beta((0))$ 또한 포함하고 따라서 $\beta$는 $V$를 경유한다. 그럼 $\alpha$의 image는 $\varphi^{-1}(V)=\Spec C$에 들어가며, $C$는 $B$-module로서 finitely generated이다. 이제 문제는 다음의 ring homomorphism들

$$B \longrightarrow A,\qquad C \longrightarrow K$$

가 주어졌을 때 이들과 양립하는 $C \rightarrow A$를 만드는 것이 된다.

임의의 $c\in C$는 $B$ 위에서 integral이므로 적당한 $b_i\in B$에 대하여

$$c^n+b_{n-1}c^{n-1}+\cdots+b_0=0$$

을 만족한다. 이 식을 $C \rightarrow K$로 옮기면 $c$의 image는 $B$의 image 위에서 integral이고, $B$의 image는 $A$ 안에 들어가므로 $c$의 image는 $A$ 위에서 integral이다. 그런데 valuation ring은 언제나 integrally closed이므로 ([\[가환대수학\] §인자, ⁋명제 6](/ko/math/commutative_algebra/divisors#prop6)의 2번) $c$의 image는 $A$에 속한다. 곧 $C \rightarrow K$는 $A$를 경유하고, 이것이 원하는 lifting을 준다.
:::

같은 판정법이 훨씬 큰 결과를 준다. Projective morphism은 정의상 closed embedding과 projection $\mathbb{P}^n_Y \rightarrow Y$의 합성이고 ([정의 1](#def1)) closed embedding 쪽은 이미 [따름정리 13](#cor13)의 1번으로 처리되었으므로, 결국 확인할 것은 projective space가 base 위에서 proper라는 것 하나이다. 그리고 이는 base change를 따라 $\mathbb{P}^n_\mathbb{Z} \rightarrow \Spec\mathbb{Z}$ 하나로 환원된다.

::: 정리 15
Noetherian scheme들 사이의 projective morphism은 proper morphism이고, quasi-projective morphism은 separated, finite type morphism이다. 
:::
::: 증명
증명의 핵심은 $\pi:\mathbb{P}^n_\mathbb{Z} \rightarrow \Spec\mathbb{Z}$가 proper라는 것이며, 이는 [정리 11](#thm11)의 판정법을 직접 확인하여 얻어진다. 우선 $\mathbb{P}^n_\mathbb{Z}$는 $n+1$개의 affine chart

$$U_i=\Spec \mathbb{Z}[\x_0/\x_i,\ldots,\x_n/\x_i]\qquad (i=0,\ldots,n)$$

을 $U_i\cap U_j=D(\x_j/\x_i)\subseteq U_i$를 따라 붙여 얻어진다. 여기에서 $\x_i/\x_i=1$이므로 각 $U_i$는 $\mathbb{Z}$ 위의 $n$변수 polynomial ring의 spectrum이다. 특히 각 $U_i$는 Noetherian ring의 spectrum이고 chart의 개수가 유한하므로 $\mathbb{P}^n_\mathbb{Z}$는 Noetherian scheme이며, $\pi$는 finite type이다. ([§스킴 사상의 성질들, ⁋정의 14](/ko/math/scheme_theory/properties_of_scheme_morphisms#def14))

$\pi$가 separated인 것은 chart 위에서 직접 확인된다. $\mathbb{P}^n_\mathbb{Z}\times_\mathbb{Z}\mathbb{P}^n_\mathbb{Z}$는 affine open subset들 $U_i\times_\mathbb{Z}U_j$로 덮이고 $\pi_1\circ\Delta=\pi_2\circ\Delta=\id$이므로 $\Delta^{-1}(U_i\times_\mathbb{Z}U_j)=U_i\cap U_j$이다. 이제 $\Delta$가 이 위에서 유도하는 ring homomorphism

$$\mathbb{Z}[\x_0/\x_i,\ldots,\x_n/\x_i]\otimes_\mathbb{Z}\mathbb{Z}[\x_0/\x_j,\ldots,\x_n/\x_j] \longrightarrow \mathcal{O}(U_i\cap U_j)=\mathbb{Z}[\x_0/\x_i,\ldots,\x_n/\x_i]_{\x_j/\x_i}$$

를 보면, 우변은 $\mathbb{Z}$ 위에서 $\x_l/\x_i$들과 $(\x_j/\x_i)^{-1}=\x_i/\x_j$로 생성되는데 앞의 것들은 첫째 인자에서, 뒤의 것은 둘째 인자에서 오므로 이 morphism은 surjective이다. 따라서 $\Delta$는 각 $U_i\times_\mathbb{Z}U_j$ 위에서 closed embedding이고, closed embedding은 target에 대해 affine-local이므로 ([§닫힌 부분스킴, ⁋명제 3](/ko/math/scheme_theory/closed_subschemes#prop3)) $\Delta$ 자체가 closed embedding이다.

$\Spec \mathbb{Z}$는 scheme들의 category에서 terminal object이므로, valuation ring $A$와 $K=\Frac(A)$에 대한 바깥쪽 square를 주는 것은 morphism $\Spec K \rightarrow \mathbb{P}^n_\mathbb{Z}$를 주는 것과 같다. Lifting의 유일성은 $\pi$가 separated인 것과 [정리 6](#thm6)에서 따르므로 존재성만 보이면 된다. $\Spec K$는 한 점이므로 주어진 morphism의 image는 적당한 chart $U_i$에 들어가고, 따라서 이 morphism은 ring homomorphism

$$\mathbb{Z}[\x_0/\x_i,\ldots,\x_n/\x_i] \longrightarrow K$$

에 대응한다. $\x_j/\x_i$의 image를 $a_j\in K$라 하면 $a_i=1$이다. 이제 $K^\times$ 위에서 $s\preceq t$를 $t/s\in A$로 정의하면, valuation ring의 정의에 의하여 임의의 $s,t$에 대해 $s\preceq t$이거나 $t\preceq s$이고, $t/s\in A$이고 $r/t\in A$일 때 $r/s=(r/t)(t/s)\in A$이므로 $\preceq$는 $K^\times$ 위의 total preorder이다. $a_i=1\neq 0$이므로 유한집합 $\{a_j \mid a_j\neq 0\}$은 공집합이 아니고, 따라서 이 집합의 최소원 $a_k$를 택할 수 있다. 곧 모든 $j$에 대하여

$$b_j:=a_j/a_k\in A$$

이다. ($a_j=0$인 경우 $b_j=0\in A$이다.) 특별히 $b_k=1$이므로 ring homomorphism

$$\mathbb{Z}[\x_0/\x_k,\ldots,\x_n/\x_k] \longrightarrow A;\qquad \x_j/\x_k\mapsto b_j$$

가 정의되고, 이는 morphism $\Spec A \rightarrow U_k\subseteq\mathbb{P}^n_\mathbb{Z}$를 준다. 이것이 lifting임을 보이려면 $A\hookrightarrow K$와의 합성이 처음 주어진 morphism과 같음을 확인하면 된다. $a_k\neq 0$이므로 처음의 ring homomorphism은 $\x_k/\x_i$를 $K$의 unit $a_k$로 보내고, 따라서 처음 morphism의 image는 $D(\x_k/\x_i)=U_i\cap U_k$에 들어간다. 그럼 $U_k$ 위에서 이 morphism은 transition 관계

$$\x_j/\x_k=(\x_j/\x_i)\cdot(\x_k/\x_i)^{-1}$$

에 의하여 $\x_j/\x_k\mapsto a_j/a_k=b_j$로 주어지므로, 위에서 만든 $\Spec A \rightarrow U_k$를 $\Spec K$로 제한한 것과 정확히 같다. 곧 판정법의 존재성이 성립하고, [정리 11](#thm11)에 의하여 $\pi$는 proper이다.

임의의 Noetherian scheme $Y$에 대하여 $\mathbb{P}^n_Y=\mathbb{P}^n_\mathbb{Z}\times_{\Spec\mathbb{Z}}Y$이다. $Y=\Spec B$인 경우 $\mathbb{P}^n_B$의 chart $\Spec B[\x_0/\x_i,\ldots,\x_n/\x_i]$가 $U_i\times_{\Spec\mathbb{Z}}\Spec B$와 일치하기 때문이며, 일반적인 $Y$에 대해서는 이들을 붙이면 된다. 따라서 [따름정리 13](#cor13)에 의하여 $\mathbb{P}^n_Y \rightarrow Y$는 proper이고, 특히 finite type이므로 $\mathbb{P}^n_Y$는 Noetherian scheme이다.

이제 $\varphi:X \rightarrow Y$가 projective라 하면 $\varphi$는 closed embedding $X\hookrightarrow \mathbb{P}^n_Y$와 projection $\mathbb{P}^n_Y \rightarrow Y$의 합성이다. ([정의 1](#def1)) Closed embedding은 proper이고 두 proper morphism의 합성은 proper이므로 ([따름정리 13](#cor13)), $\varphi$는 proper이다.

마지막으로 $\varphi:X \rightarrow Y$가 quasi-projective라 하고, 이를 open embedding $\lambda: X \rightarrow X'$와 projective morphism $\psi:X' \rightarrow Y$의 합성 $\varphi=\psi\circ\lambda$로 분해하자. ([정의 1](#def1)) 방금 보인 것에 의해 $\psi$는 proper이고, 따라서 separated이며 finite type이다. 한편 open embedding은 separated이고 두 separated morphism의 합성은 separated이므로 ([따름정리 8](#cor8)), $\varphi$는 separated이다. 또 open embedding은 locally of finite type이며, $X$가 Noetherian이므로 $X'$의 임의의 affine open subset의 $\lambda$에 의한 preimage는 Noetherian space의 열린집합으로서 quasi-compact이다. 곧 $\lambda$는 finite type이고 ([§스킴 사상의 성질들, ⁋정의 14](/ko/math/scheme_theory/properties_of_scheme_morphisms#def14)), 두 finite type morphism의 합성은 finite type이므로 $\varphi$ 또한 finite type이다.
:::

이로써 우리는 판정법의 고전적인 귀결을 얻는다. Proper morphism은 정의상 closed map이므로, projective scheme에서 나가는 morphism의 image는 언제나 닫혀 있다.

::: 따름정리 16
$\mathbb{K}$ 위의 projective scheme $X$와 separated finite type $\mathbb{K}$-scheme $Z$, 그리고 $\mathbb{K}$-morphism $\varphi:X \rightarrow Z$에 대하여 $\varphi(X)$는 $Z$의 닫힌집합이다.
:::
::: 증명
Structure morphism $X \rightarrow \Spec\mathbb{K}$가 projective이므로 [정리 15](#thm15)에 의하여 proper이고, $Z \rightarrow \Spec\mathbb{K}$는 가정에 의하여 separated이다. 그럼 [따름정리 13](#cor13)의 5번을 $\varphi$와 $Z \rightarrow \Spec\mathbb{K}$에 적용하여 $\varphi$가 proper임을 얻고, 특히 $\varphi$는 closed map이므로 $X$ 자신이 $X$의 닫힌집합이라는 것으로부터 $\varphi(X)$가 닫혀 있다.
:::

---

**참고문헌**

**[Har]** R. Hartshorne, *Algebraic geometry*. Graduate texts in mathematics. Springer, 1977.  
**[Vak]** R. Vakil, *The rising sea: Foundation of algebraic geometry*. Available [online](https://math.stanford.edu/~vakil/216blog/).