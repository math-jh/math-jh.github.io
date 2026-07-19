---
title: "값매김환"
description: "분리사상과 proper 사상을 정의하고, 이들이 위상수학의 Hausdorff 조건과 compact 조건을 대수기하학적으로 어떻게 일반화하는지 살펴본다. 이산값매김환의 구조도 함께 다룬다."
excerpt: "Valuative criteria for separated, properness"

categories: [Math / Scheme Theory]
permalink: /ko/math/scheme_theory/valuative_criteria
sidebar: 
    nav: "scheme_theory-ko"

date: 2024-05-24
weight: 14
published: false
drift_needed: true
---

이번 글에서 우리는 separated morphism과 proper morphism을 정의한다. 이들은 위상수학에서 Hausdorff 조건과 compact 조건을 대수기하로 옮겨온 것이라고 생각하면 편하다. 

우리는 앞선 글들에서 open subscheme을 ([§스킴, ⁋정의 4](/ko/math/scheme_theory/schemes#def4)) 정의하였고, closed embedding과 그로부터 얻어지는 closed subscheme, 그리고 ideal sheaf를 ([§닫힌 부분스킴, ⁋정의 2](/ko/math/scheme_theory/closed_subschemes#def2), [⁋정의 5](/ko/math/scheme_theory/closed_subschemes#def5)) 살펴보았다. 여기에 다음의 개념들을 더한다.

::: 정의 1
임의의 scheme $X$이 주어졌다 하자.

1. Scheme morphism $f:X \rightarrow Y$가 $X$와 $Y$의 open subscheme 사이의 isomorphism을 유도하면 $f$를 *open immersion<sub>열린 몰입</sub>*이라 부른다.
2. $f:X \rightarrow Y$가 *projective<sub>사영사상</sub>*라는 것은 적당한 $n$에 대하여, $f$를 closed embedding과 projection의 합성 $X\hookrightarrow \mathbb{P}^n_Y \rightarrow Y$의 꼴로 분해할 수 있는 것이다. ([§사영스킴](/ko/math/scheme_theory/projective_schemes))
3. $f:X \rightarrow Y$가 *quasi-projective<sub>준사영사상</sub>*라는 것은 이를 적당한 open immersion $X \rightarrow X'$와 projective morphism $X' \rightarrow Y$의 합성으로 분해할 수 있는 것이다. 
:::

본격적인 이야기를 시작하기 전에 다음 예시를 살펴보는 것이 좋다. 

::: 예시 2
Ring $A$가 discrete valuation ring이라 하자. 즉 $A$는 principal ideal domain이고 두 개의 prime ideal들 $(0)$, $\mathfrak{m}$을 가지며 이 중 $\mathfrak{m}$은 $A$의 유일한 maximal ideal로서 non-unit들의 모임이다. 

이로부터 $\Spec A$는 두 개의 점 $(0)$, $\mathfrak{m}$으로 이루어져 있으며,

$$Z((0))=\{(0),\mathfrak{m}\},\quad Z(\mathfrak{m})=\{\mathfrak{m}\}$$

이므로 $\Spec A$의 자명하지 않은 열린집합은

$$D(\mathfrak{m})=\{(0)\}$$

뿐이다. 한편 $\mathfrak{m}=(\pi)$라 하면 [§아핀스킴, ⁋보조정리 6](/ko/math/scheme_theory/affine_schemes#lem6)에 의하여

$$\mathcal{O}(D(\mathfrak{m}))=\mathcal{O}(D(\pi))\cong A_\pi\cong \Frac(A)$$

이다. 물론 $\mathcal{O}(\Spec A)\cong A$이다. 

한편 $\Spec A$의 두 점은 기하적으로 다음과 같이 살펴볼 수 있다: 각 점은 $A$에서 그 residue field로 가는 ring homomorphism에 의해 결정되는데, 즉 $\kappa((0))$와 $\kappa(\mathfrak{m})$이다. 다시 [§아핀스킴, ⁋보조정리 8](/ko/math/scheme_theory/affine_schemes#lem8)를 사용하면

$$\mathcal{O}_{(0)}\cong A_{(0)}\cong \Frac(A),\qquad \mathcal{O}_\mathfrak{m}\cong A_\mathfrak{m}$$

으로부터 

$$\kappa((0))=\Frac(A), \qquad \kappa(\mathfrak{m})=A_\mathfrak{m}/\mathfrak{m}A_\mathfrak{m}\cong \Frac(A/\mathfrak{m})\cong A/\mathfrak{m}$$

을 얻는다. 
:::

이 예시가 뜻하는 바를 짚어 두자. $Z((0))=\Spec A$이므로 $(0)$의 closure는 $\Spec A$ 전체이고, 곧 $(0)$은 generic point이며 유일한 closed point $\mathfrak{m}$은 $(0)$의 specialization이다. 여기에서 closed point를 빼낸 것이 자명하지 않은 유일한 열린집합 $D(\mathfrak{m})=\{(0)\}$이고 그 위의 함수들이 $K=\Frac(A)$였으므로, canonical morphism $\Spec K \rightarrow \Spec A$는 정확히 이 "점 하나를 빼는" 포함사상이다. 기하적으로는 $\Spec A$를 곡선의 한 점에서의 germ으로, $\Spec K$를 그 germ에서 점 하나를 빼낸 것으로 생각하면 된다.

그럼 morphism $\Spec K \rightarrow X$는 $X$ 안으로 들어가는, 점이 빠진 곡선의 germ이고, 이를 $\Spec A \rightarrow X$로 확장하는 것은 빠져 있던 그 점을 $X$ 안에서 되찾아 곡선을 이어 붙이는 것, 곧 곡선의 극한을 찾는 것이 된다. 이 extension이 많아야 하나 존재한다는 것이 separatedness이고 정확히 하나 존재한다는 것이 properness이며, 이것이 앞으로 볼 두 판정법의 내용이다. Hausdorff 공간에서 극한이 유일하고 compact 공간에서 극한이 항상 존재하는 것에 정확히 대응하는 구도이다.

## 분리사상

::: 정의 3
Scheme morphism $f:X \rightarrow Y$에 대하여, *diagonal morphism<sub>대각사상</sub>*을 $\Delta: X \rightarrow X \times_Y X$으로 정의한다. 

![diagonal_morphism](/assets/images/Math/Scheme_Theory/Valuative_Criteria-1.svg){:style="width:13.51em" class="invert" .align-center}

만일 $\Delta$가 closed embedding이라면 $f$를 *separated<sub>분리사상</sub>*라 부르고, $X$가 $Y$에 대해 *separated*라 부른다. 만일 $X$가 $\Spec \mathbb{Z}$에 대해 separated이면, $X$를 간단히 *separated* scheme이라 부른다.
:::

대수기하학에서는 separatedness가 Hausdorff를 대체하는 성질이라 생각하는데, 이는 다음 명제 때문이다.

::: 명제 4
$f:X \rightarrow Y$가 separated인 것과, diagonal morphism $\Delta: X \rightarrow X\times_YX$에 의한 $X$의 image가 닫힌집합인 것이 동치이다.
:::
::: 증명
정의에 의하여 $f$가 separated라면 $\Delta(X)$가 닫혀있음은 자명하다. 따라서 $\Delta(X)$가 closed임을 가정하고, $\Delta$가 closed embedding임을 보여야 한다. $\Delta(X)$가 $X\times_YX$의 닫힌집합이 되는 것은 자명하므로, $\mathcal{O}_{X\times_YX} \rightarrow \Delta_\ast \mathcal{O}_X$가 surjective임을 보이면 충분하다. 한편 sheaf morphism의 surjectivity는 stalk 위에서 체크할 수 있다. 임의의 $p\in X$를 택하자. 그럼 우선 $p$의 open affine subset $U$를 택할 수 있으며, 필요하다면 $U$를 제한하여 $f(U)$가 $Y$의 어떠한 open affine subset $V$에 속하도록 할 수 있다. 그럼 $U\times_VU$는 $\Delta(p)$의 open neighborhood이며, 이 위에서 $\Delta: U \rightarrow U\times_VU$는 다음의 [보조정리 5](#lem5)에 의하여 closed embedding이 되고, 증명이 완료된다.
:::

::: 보조정리 5
Affine scheme 사이의 임의의 morphism $f:X \rightarrow Y$는 항상 separated이다.
:::
::: 증명
$X=\Spec A, Y=\Spec B$라 하면 $\Delta$가 ring homomorphism 

$$A\otimes_BA \rightarrow A;\quad a\otimes a'\mapsto aa'$$

으로부터 유도되며, 이것이 surjective이므로 자명하다. 
:::

Separated가 아닌 scheme의 예시는 [§스킴, ⁋예시 10](/ko/math/scheme_theory/schemes#ex10)에서 만든 line with double origin이 있다. 편의상 이 scheme을 $X$라 하자. 그럼 $X\times X$는 축 바깥에서는 일반적인 좌표평면과 똑같을 것이지만 좌표축, 특히 원점을 보면 네 개의 원점이 들어가게 된다. 직관적으로는 $\Delta$가 
$X\times X$에 어떻게 들어갈지를 생각해보면 좌표축 바깥에서는 일반적인 대각선 모양이 될 것이지만, $X$의 두 원점이 $\Delta$를 통해 $X\times X$로 옮겨졌을 때, 이 네 원점 중 어느 두 개에 들어갈지를 알 수 없다. 실제로 이 네 원점은 모두 $\Delta(X)$의 closure에 들어가므로 separated가 아닌 것을 알 수 있다. 역시, 위상수학에서 이 공간은 Hausdorff가 아닌 공간의 예시였다. 

::: 정리 6
Noetherian scheme $X$와 scheme morphism $f:X \rightarrow Y$에 대하여, $f$가 separated인 것은 임의의 valuation ring $A$와 그 quotient field $K=\Frac(A)$에 대하여, 임의의 scheme morphism $\Spec A \rightarrow Y$, $\Spec K \rightarrow X$와 다음 commutative diagram

![valuative_criterion](/assets/images/Math/Scheme_Theory/Valuative_Criteria-2.svg){:style="width:8.27em" class="invert" .align-center}

의 바깥쪽 square가 주어질 때마다, 많아야 하나의 $\Spec A \rightarrow X$가 전체 diagram이 commute하도록 하는 것이 동치이다.
:::
::: 증명
바깥쪽 square가 주어졌다는 것은 morphism $u:\Spec K \rightarrow X$와 $v: \Spec A \rightarrow Y$가 주어져 inclusion $A\hookrightarrow K$가 유도하는 $j: \Spec K \rightarrow \Spec A$에 대해 $f\circ u=v\circ j$가 성립하는 것이며, 이 square의 lifting이란 $g\circ j=u$와 $f\circ g=v$를 만족하는 $g:\Spec A \rightarrow X$를 말한다.

증명 전체에서 두 개의 표준적인 사실을 사용한다. 첫째는 valuation ring의 존재정리로, field $K$와 그 안의 local subring $\mathcal{O}$가 주어질 때마다 $\Frac(A)=K$이고 $\mathcal{O}\subseteq A$이며 $\mathfrak{m}_A\cap \mathcal{O}=\mathfrak{m}_\mathcal{O}$인 valuation ring $A$가 존재한다는 것이다. 이 때 $A$가 $\mathcal{O}$를 *dominate*한다고 하며, 이러한 $A$의 존재는 Zorn's lemma로부터 얻어지는 가환대수학의 표준적인 결과이다. 둘째는 field $K$에 대하여 morphism $\Spec K \rightarrow X$가 점 $x\in X$와 field homomorphism $\kappa(x) \rightarrow K$의 쌍에 일대일로 대응한다는 것이다. 이는 $X=\Spec B$인 경우 ring homomorphism $B \rightarrow K$가 그 kernel인 prime ideal $\mathfrak{p}$와 $\kappa(\mathfrak{p}) \rightarrow K$의 쌍을 주는 것에서 따르고, 일반적인 경우는 $x$의 affine open neighborhood를 택하면 된다.

먼저 $f$가 separated라 가정하고, 위 square의 두 lifting $g_1, g_2$가 주어졌다 하자. $f\circ g_1=f\circ g_2=v$이므로 fiber product의 universal property에 의하여 유일한 $h:\Spec A \rightarrow X\times_YX$가 존재하여 $p_1\circ h=g_1$, $p_2\circ h=g_2$이다. 여기에서 $p_1,p_2$는 두 projection이다. 이제 $\Delta$가 closed embedding이므로 base change

$$Z=\Spec A\times_{X\times_YX}X \longrightarrow \Spec A$$

또한 closed embedding이다. Closed embedding이 base change에 대해 안정적인 것은 affine-local하게 $B \rightarrow B/\mathfrak{b}$의 base change가 $C \rightarrow C\otimes_B(B/\mathfrak{b})\cong C/\mathfrak{b}C$로서 여전히 surjective인 것으로부터 얻어진다. ([§닫힌 부분스킴, ⁋명제 3](/ko/math/scheme_theory/closed_subschemes#prop3))

한편 $p_1\circ h\circ j=g_1\circ j=u$이고 $p_2\circ h\circ j=g_2\circ j=u$이며, $p_1\circ \Delta\circ u=u$이고 $p_2\circ\Delta\circ u=u$이므로 universal property의 유일성으로부터 $h\circ j=\Delta\circ u$이다. 따라서 $j$는 pullback $Z$를 경유하고, 특히 $Z \rightarrow \Spec A$의 image는 $j$의 image, 곧 $A$의 zero ideal $(0)$을 포함하는 닫힌집합이다. $A$는 domain이므로 $(0)$은 $\Spec A$의 generic point이고 ([§스킴의 위상구조, ⁋예시 5](/ko/math/scheme_theory/topology_of_schemes#ex5)), 따라서 $(0)$을 포함하는 $\Spec A$의 닫힌집합은 $\Spec A$ 자신뿐이다. 그럼 $Z$는 $\Spec A$의 closed subscheme으로서 적당한 ideal $\mathfrak{a}\subseteq A$에 대해 $\Spec(A/\mathfrak{a})$의 꼴이며 ([§닫힌 부분스킴, ⁋명제 3](/ko/math/scheme_theory/closed_subschemes#prop3)), 그 image가 $\Spec A$ 전체라는 것은 $\mathfrak{a}$가 $A$의 모든 prime ideal에 포함된다는 것, 곧

$$\mathfrak{a}\subseteq \sqrt{(0)}=(0)$$

임을 뜻한다. 마지막 등호는 $A$가 domain이라는 사실에서 온다. 따라서 $Z \rightarrow \Spec A$는 isomorphism이고, 이는 $h$가 $\Delta$를 경유한다는 것, 곧 적당한 $g:\Spec A \rightarrow X$에 대하여 $h=\Delta\circ g$임을 뜻한다. 그럼

$$g_1=p_1\circ h=p_1\circ \Delta\circ g=g,\qquad g_2=p_2\circ h=p_2\circ\Delta\circ g=g$$

이므로 $g_1=g_2$이다. 이 방향에서는 $X$가 Noetherian이라는 가정이 쓰이지 않는다.

거꾸로 임의의 square에 대하여 lifting이 많아야 하나 존재한다고 가정하자. [명제 4](#prop4)에 의하여 $\Delta(X)$가 $X\times_YX$의 닫힌집합임을 보이면 충분하다.

우선 $\cl(\Delta(X))$의 모든 점이 $\Delta(X)$의 어떤 점의 specialization임을 관찰한다. $X$가 Noetherian scheme이므로 위상공간으로서도 Noetherian이고 ([§스킴의 위상구조, ⁋정의 14](/ko/math/scheme_theory/topology_of_schemes#def14)), 따라서 유한히 많은 irreducible component $X_1,\ldots, X_r$를 갖는다. ([\[위상수학\] §차원, ⁋명제 13](/ko/math/topology/dimension#prop13)) 각 $X_i$는 irreducible closed subset이므로 generic point $\eta_i$를 가지며 ([§스펙트럼, ⁋명제 16](/ko/math/scheme_theory/spectrums#prop16)), $X=\bigcup_{i=1}^r\cl(\{\eta_i\})$이다. 이제 $\Delta$가 연속이므로 $\Delta(X)\subseteq \bigcup_{i=1}^r \cl(\{\Delta(\eta_i)\})$이고 우변은 유한합집합이라 닫혀 있으며, 거꾸로 각 $\Delta(\eta_i)$가 $\Delta(X)$에 속하므로

$$\cl(\Delta(X))=\bigcup_{i=1}^r\cl(\{\Delta(\eta_i)\})$$

를 얻는다. 곧 $\cl(\Delta(X))$의 임의의 점은 적당한 $\Delta(\eta_i)\in \Delta(X)$의 specialization이다. ([§스킴의 위상구조, ⁋정의 2](/ko/math/scheme_theory/topology_of_schemes#def2)) 그러므로 $\Delta(X)$가 specialization에 대해 닫혀 있음을 보이면 $\Delta(X)=\cl(\Delta(X))$가 되어 증명이 끝난다.

$\xi=\Delta(x)\in \Delta(X)$이고 $\eta\in\cl(\{\xi\})$라 하자. 닫힌집합 $T=\cl(\{\xi\})$에 reduced scheme structure를 주면 ([§닫힌 부분스킴, ⁋정의 14](/ko/math/scheme_theory/closed_subschemes#def14)) $T$는 generic point $\xi$를 갖는 integral scheme이다. $\eta$를 포함하는 affine open subset $\Spec B\subseteq T$를 택하자. Generic point는 공집합이 아닌 모든 열린집합에 속하므로 $\Spec B$는 $\xi$ 또한 포함하며, $B$는 domain이고 $\xi$는 $B$의 zero ideal에 대응하므로

$$K:=\kappa(\xi)=\mathcal{O}_{T,\xi}=\Frac(B), \qquad \mathcal{O}:=\mathcal{O}_{T,\eta}=B_\mathfrak{q}\subseteq K$$

이며, 여기에서 $\mathfrak{q}$는 $\eta$에 대응하는 prime ideal이다. 특히 $\mathcal{O}$는 $\Frac(\mathcal{O})=K$인 local domain이다. 위에서 인용한 존재정리로 $\mathcal{O}$를 dominate하는 $K$의 valuation ring $A$를 택하면, local homomorphism $\mathcal{O} \rightarrow A$가 유도하는 morphism

$$q:\Spec A \longrightarrow \Spec \mathcal{O} \longrightarrow T \hookrightarrow X\times_YX$$

는 $\Spec A$의 generic point $(0)$을 $\xi$로, closed point $\mathfrak{m}_A$를 $\eta$로 보낸다.

이제 $g_1=p_1\circ q$, $g_2=p_2\circ q$라 하고, $f\circ p_1=f\circ p_2$이므로 잘 정의되는 $w=f\circ g_1=f\circ g_2:\Spec A \rightarrow Y$를 생각하자. [명제 4](#prop4)의 증명에서 보았듯 $x$의 affine open neighborhood $U$와 $f(U)$를 포함하는 $Y$의 affine open subset $V$를 택하면 $U\times_VU$는 $X\times_YX$에서 $\xi$의 open neighborhood이고 그 위에서 $\Delta$는 closed embedding이므로 ([보조정리 5](#lem5)), stalk 사이의 사상 $\mathcal{O}_{X\times_YX,\xi} \rightarrow \mathcal{O}_{X,x}$는 surjective이고 따라서 $\kappa(\xi) \rightarrow \kappa(x)$ 또한 surjective이다. 한편 $p_1\circ\Delta=\id_X$이므로 합성 $\kappa(x) \rightarrow \kappa(\xi) \rightarrow \kappa(x)$는 항등사상이고, 그러므로 두 사상은 서로의 역이 되는 isomorphism이다. 곧 $K=\kappa(\xi)\cong\kappa(x)$이다. 이 동일시 아래에서 점 $x$와 $\kappa(x)\cong K$가 정의하는 canonical morphism을 $u:\Spec K \rightarrow X$라 하면, $\Delta\circ u$는 점 $\xi$와 $\kappa(\xi)\cong K$가 정의하는 canonical morphism이고 이는 $q\circ j$와 같다. 실제로 $q\circ j$는 $\xi$를 상으로 갖고 residue field 위에서 $\kappa(\xi)=\Frac(\mathcal{O})=K$의 항등사상을 유도하기 때문이다. 따라서

$$g_1\circ j=p_1\circ q\circ j=p_1\circ \Delta\circ u=u,\qquad g_2\circ j=p_2\circ q\circ j=p_2\circ\Delta\circ u=u$$

이고 $f\circ g_1=f\circ g_2=w$이므로, $g_1$과 $g_2$는 $u$와 $w$가 주는 square의 두 lifting이다. 가정에 의하여 $g_1=g_2$이고, 그럼 $\Delta\circ g_1$과 $q$는 $p_1$, $p_2$와 합성했을 때 각각 $g_1$과 $g_2=g_1$을 주므로 fiber product의 universal property에 의해 $q=\Delta\circ g_1$이다. 그러므로

$$\eta=q(\mathfrak{m}_A)=\Delta(g_1(\mathfrak{m}_A))\in \Delta(X)$$

이고, $\Delta(X)$는 specialization에 대해 닫혀 있다. 앞의 관찰과 결합하면 $\Delta(X)=\cl(\Delta(X))$이므로 $\Delta(X)$는 닫힌집합이고, [명제 4](#prop4)에 의하여 $f$는 separated이다.
:::

한편 만일 $Y$가 noetherian이고 $f$가 finite type morphism이라면 위의 정리를 임의의 valuation ring이 아니라, 임의의 discrete valuation ring으로 대체해도 된다는 것이 알려져 있다. 이렇게 바꿔두고 나면 기하학적 직관을 이용해 정리를 설명하기가 쉬워지는데, $\Spec A$를 smooth curve의 germ을 나타내는 것으로 생각하고 $\Spec K$는 여기에서 한 점이 빠져있는 것으로 생각하면 위의 정리는 이러한 $\Spec K\hookrightarrow \Spec A$를 넣는 방법이 하나 뿐이라는 것을 말해준다. 

그럼 이로부터 다음을 얻는다.

::: 따름정리 7
Noetherian scheme들에 대하여, 

1. Open immersion과 closed embedding은 모두 separated이다. 
2. 두 separated morphism의 합성은 separated이다.
3. Separated morphism은 base change에 의해 보존된다.
4. Separated morphism은 fiber product에 의해 보존된다.
5. 만일 $f:X \rightarrow Y$, $g:Y \rightarrow Z$가 scheme morphism들이고 $g\circ f$가 separated morphism이라면 $f$ 또한 separated morphism이다.
:::

## 고유사상

::: 정의 8
$f:X \rightarrow Y$가 *universally closed*라는 것은 $f$가 closed map이고, 임의의 $Y' \rightarrow Y$에 대해서도 $X\times_Y Y' \rightarrow Y'$가 closed인 것이다. Separated, universally closed인 finite type morphism을 *proper morphism<sub>고유사상</sub>*이라 부른다. 
:::

[정리 6](#thm6)과 마찬가지로 proper morphism에 대해서도 valuative criterion이 존재한다.

::: 정리 9
Noetherian scheme $X$와 finite type scheme morphism $f:X \rightarrow Y$에 대하여, $f$가 proper인 것은 임의의 valuation ring $A$와 그 quotient field $K=\Frac(A)$에 대하여, 임의의 scheme morphism $\Spec A \rightarrow Y$, $\Spec K \rightarrow X$와 다음 commutative diagram

![valuative_criterion](/assets/images/Math/Scheme_Theory/Valuative_Criteria-2.svg){:style="width:8.27em" class="invert" .align-center}

의 바깥쪽 square가 주어질 때마다, 정확히 하나의 $\Spec A \rightarrow X$가 존재하여 전체 diagram이 commute하는 것이 동치이다.
:::
::: 증명
[정리 6](#thm6)의 증명에서와 같이 바깥쪽 square를 $u:\Spec K \rightarrow X$, $v:\Spec A \rightarrow Y$, $j:\Spec K \rightarrow \Spec A$로 적고, 그 증명에서 인용한 두 표준적인 사실을 계속 사용한다. 곧 field $K$ 안의 local subring은 항상 $\Frac(A)=K$인 valuation ring $A$에 의해 dominate되며, morphism $\Spec K \rightarrow X$는 점 $x\in X$와 field homomorphism $\kappa(x) \rightarrow K$의 쌍과 같은 것이다. 여기에 valuation ring의 다음 극대성을 덧붙인다. 만일 $K$의 valuation ring $A$를 dominate하는 local subring $\mathcal{O}\subseteq K$가 주어졌다면 $\mathcal{O}=A$이다. 실제로 $c\in\mathcal{O}$가 $0$이 아니고 $c\notin A$라면 valuation ring의 정의에 의해 $c^{-1}\in A$이며, $c\notin A$이므로 $c^{-1}$은 $A$의 unit이 아니다. 곧 $c^{-1}\in\mathfrak{m}_A\subseteq \mathfrak{m}_\mathcal{O}$인데 $c\in\mathcal{O}$이므로 $c^{-1}$은 $\mathcal{O}$의 unit이 되어 모순이다. 따라서 $\mathcal{O}\subseteq A$이고, dominate의 정의에서 $A\subseteq\mathcal{O}$이므로 $\mathcal{O}=A$이다.

먼저 $f$가 proper라 하자. Proper morphism은 separated이므로 [정리 6](#thm6)에 의하여 lifting은 많아야 하나이고, 따라서 존재성만 보이면 된다. $v$를 따라 base change하여 $X_A=X\times_Y\Spec A$와 projection $\pi:X_A \rightarrow \Spec A$를 얻자. $f$가 universally closed이므로 $\pi$는 closed map이다. ([정의 8](#def8)) 한편 $u$와 $j$는 fiber product의 universal property에 의해 $\Spec A$ 위의 morphism $\tilde{u}:\Spec K \rightarrow X_A$를 유도하며, $\Spec A \rightarrow X_A$ 꼴의 $\pi$의 section으로서 $\tilde{u}$를 연장하는 것을 찾으면 이를 $X$로 project하여 원하는 lifting을 얻는다.

$\xi\in X_A$를 $\tilde{u}$의 상이 되는 점이라 하고 $Z=\cl(\{\xi\})$에 reduced scheme structure를 주자. ([§닫힌 부분스킴, ⁋정의 14](/ko/math/scheme_theory/closed_subschemes#def14)) $\pi\circ\tilde{u}=j$이므로 $\pi(\xi)$는 $\Spec A$의 generic point $(0)$이고, $\pi$가 closed map이므로 $\pi(Z)$는 $(0)$을 포함하는 닫힌집합, 곧 $\Spec A$ 전체이다. 따라서 $\pi(z)=\mathfrak{m}_A$인 $z\in Z$가 존재한다.

Residue field들을 살펴보자. $\pi\circ \tilde{u}=j$가 $(0)$에서 유도하는 사상 $\kappa((0))=K \rightarrow K$는 항등사상이고, 이것은 $\pi$가 유도하는 $K\rightarrow\kappa(\xi)$와 $\tilde{u}$가 유도하는 $\kappa(\xi) \rightarrow K$의 합성이므로 두 사상은 서로의 역이 되는 isomorphism이다. 곧 $\kappa(\xi)\cong K$이다. 그럼 $Z$는 generic point $\xi$를 갖는 integral scheme이므로, [정리 6](#thm6)의 증명에서와 같이 $z$를 포함하는 affine open subset을 택하여

$$\mathcal{O}:=\mathcal{O}_{Z,z}\subseteq \kappa(\xi)=K,\qquad \Frac(\mathcal{O})=K$$

임을 안다. 또 $\pi\vert_Z$가 유도하는 사상 $A=\mathcal{O}_{\Spec A,\mathfrak{m}_A} \rightarrow \mathcal{O}_{Z,z}$는 local homomorphism이며, generic point에서 이것이 유도하는 $K \rightarrow \kappa(\xi)=K$가 항등사상이므로 이 사상은 $K$의 subring 사이의 포함사상이다. 곧 $\mathcal{O}$는 $A$를 dominate하는 $K$의 local subring이고, 위의 극대성에 의하여 $\mathcal{O}_{Z,z}=A$이다.

그럼 canonical morphism $\Spec A=\Spec\mathcal{O}_{Z,z} \rightarrow Z \hookrightarrow X_A$를 얻고, 이것과 $\pi$의 합성은 ring 수준에서 $A$의 항등사상에 대응하므로 $\pi$의 section이다. 이 section을 $\Spec K$로 제한한 것은 $\xi$를 상으로 갖고 residue field 위에서 $\kappa(\xi)=K$의 항등사상을 유도하므로 $\tilde{u}$와 같다. 따라서 이 section을 $X$로 project하면 $g\circ j=u$이고 $f\circ g=v$인 $g:\Spec A \rightarrow X$를 얻는다.

거꾸로 판정법이 성립한다고 가정하자. Lifting의 유일성과 [정리 6](#thm6)으로부터 $f$는 separated이고 finite type은 가정이므로, $f$가 universally closed임만 보이면 된다. 우리는 Noetherian scheme들의 범주 안에서 작업하고 있으므로 base change $Y' \rightarrow Y$ 또한 Noetherian scheme에 대한 것으로 제한한다.

우선 판정법이 base change에 대해 안정적이다. $Y' \rightarrow Y$와 $X'=X\times_YY'$, $f':X' \rightarrow Y'$가 주어졌다 하고, $\Spec K \rightarrow X'$와 $\Spec A \rightarrow Y'$가 $f'$에 대한 바깥쪽 square를 이룬다 하자. 이들을 $X' \rightarrow X$, $Y' \rightarrow Y$와 합성하면 $f$에 대한 바깥쪽 square를 얻으므로 유일한 lifting $g:\Spec A \rightarrow X$가 존재하고, $g$와 $\Spec A \rightarrow Y'$는 universal property에 의해 유일한 $g':\Spec A \rightarrow X'$를 준다. $g'\circ j$와 주어진 $\Spec K \rightarrow X'$는 $X' \rightarrow X$, $X' \rightarrow Y'$와 합성한 결과가 각각 같으므로 서로 같고, 따라서 $g'$는 $f'$에 대한 lifting이다. 유일성 또한 두 lifting을 $X' \rightarrow X$와 합성하여 $f$에 대한 lifting의 유일성을 쓰면 얻어진다. 한편 finite type morphism은 base change에 대해 안정적이고 Noetherian scheme 위의 finite type scheme은 다시 Noetherian이므로, $X'$는 Noetherian이고 $f'$는 finite type이다. 따라서 Noetherian scheme $X$와 finite type morphism $f:X \rightarrow Y$가 판정법의 존재성 부분을 만족할 때 $f$가 closed map임을 보이면, 이를 모든 base change에 적용하여 증명이 끝난다.

이를 보이기 위해 $X$의 닫힌집합 $T$를 택하고 reduced scheme structure를 주자. Closed embedding $T\hookrightarrow X$는 finite morphism이므로 ([§닫힌 부분스킴, ⁋명제 4](/ko/math/scheme_theory/closed_subschemes#prop4)) finite type이고, 따라서 $T$는 Noetherian scheme이며 $f\vert_T:T \rightarrow Y$ 또한 finite type이다. 또 $f\vert_T$는 판정법의 존재성 부분을 물려받는다. 실제로 $\Spec K \rightarrow T$와 $\Spec A \rightarrow Y$가 $f\vert_T$에 대한 square를 이루면, $\Spec K \rightarrow T\hookrightarrow X$에 판정법을 적용하여 lifting $g_0:\Spec A \rightarrow X$를 얻는다. $\Spec A$의 모든 점은 generic point $(0)$의 specialization이고 morphism은 specialization을 보존하므로 $g_0(\Spec A)\subseteq \cl(\{g_0((0))\})\subseteq T$이며, $\Spec A$는 reduced이므로 $g_0$는 $T$를 경유한다. 여기에서 마지막 사실은 다음과 같이 얻어진다. Reduced scheme $S$에서의 morphism $\varphi:S \rightarrow X$의 상이 닫힌집합 $T$에 들어간다 하고, $X$의 affine open subset $\Spec B$와 $\varphi^{-1}(\Spec B)$의 affine open subset $\Spec R$을 택하자. $T\cap \Spec B=Z(\mathfrak{b})$ ($\mathfrak{b}$는 radical ideal)라 하면 $T$의 reduced structure는 그 위에서 $\Spec (B/\mathfrak{b})$이고, 대응하는 ring homomorphism $\psi:B \rightarrow R$는 임의의 prime ideal $\mathfrak{p}\subseteq R$에 대해 $\mathfrak{b}\subseteq \psi^{-1}(\mathfrak{p})$를 만족하므로

$$\psi(\mathfrak{b})\subseteq \bigcap_{\mathfrak{p}\in\Spec R}\mathfrak{p}=\sqrt{(0)}=(0)$$

이다. 곧 $\psi$는 $B/\mathfrak{b}$를 유일하게 경유하고, 이렇게 얻어진 국소적인 factorization들은 유일성에 의해 붙는다.

따라서 $f(T)=f\vert_T(T)$가 닫힌집합임을 보이면 되고, 결국 판정법의 존재성 부분을 만족하는 finite type morphism $f:X \rightarrow Y$ (단 $X$는 Noetherian)의 상 $f(X)$가 닫혀 있음을 보이면 충분하다.

$f(X)$가 specialization에 대해 닫혀 있음을 먼저 본다. $y_1=f(x_1)\in f(X)$이고 $y_0\in\cl(\{y_1\})$이라 하자. $W=\cl(\{y_1\})$에 reduced scheme structure를 주면 $W$는 generic point $y_1$을 갖는 integral scheme이고, 앞에서와 같이 $\mathcal{O}=\mathcal{O}_{W,y_0}$는 $\Frac(\mathcal{O})=\kappa(y_1)$인 local domain이다. 이제 $K=\kappa(x_1)$이라 하고 $f$가 유도하는 field homomorphism $\kappa(y_1)\hookrightarrow K$를 통해 $\mathcal{O}$를 $K$의 local subring으로 보자. 그럼 $\mathcal{O}$를 dominate하는 $K$의 valuation ring $A$가 존재하고, 이로부터 두 morphism

$$\Spec A \longrightarrow \Spec\mathcal{O} \longrightarrow W\hookrightarrow Y,\qquad u:\Spec K \longrightarrow X$$

를 얻는다. 여기에서 $u$는 점 $x_1$과 $\kappa(x_1)=K$가 정의하는 canonical morphism이다. 이 둘은 바깥쪽 square를 이루는데, $\Spec K \rightarrow Y$로 가는 두 합성이 모두 점 $y_1$과 field homomorphism $\kappa(y_1)\hookrightarrow K$가 정의하는 canonical morphism이기 때문이다. 판정법의 존재성에 의하여 lifting $g_0:\Spec A \rightarrow X$가 존재하고, $\Spec A \rightarrow \Spec\mathcal{O}$가 local homomorphism에서 오므로 $\mathfrak{m}_A$는 $\mathfrak{m}_\mathcal{O}$, 곧 $y_0$으로 간다. 따라서 $f(g_0(\mathfrak{m}_A))=y_0$이고 $y_0\in f(X)$이다.

끝으로 [정리 6](#thm6)의 증명에서의 위상적인 관찰을 그대로 반복한다. $X$의 irreducible component들 $X_1,\ldots,X_r$의 generic point를 $\eta_1,\ldots,\eta_r$이라 하면 $X=\bigcup_{i=1}^r\cl(\{\eta_i\})$이므로

$$\cl(f(X))=\bigcup_{i=1}^r\cl(\{f(\eta_i)\})$$

이고, 따라서 $\cl(f(X))$의 모든 점은 $f(X)$의 점의 specialization이다. 앞에서 $f(X)$가 specialization에 대해 닫혀 있음을 보였으므로 $f(X)=\cl(f(X))$이다. 
:::

마찬가지로 다음 따름정리가 성립한다.

::: 따름정리 10
Noetherian scheme들에 대하여,

1. Closed embedding은 proper이다.
2. Proper morphism들의 합성은 proper이다. 
3. Proper morphism은 base change에 의해 보존된다.
4. Proper morphism은 fiber product에 의해 보존된다.
5. 만일 $f:X \rightarrow Y$, $g:Y \rightarrow Z$가 scheme morphism들이고 $g\circ f$가 proper morphism이라면 $f$ 또한 proper morphism이다.
:::

::: 정리 11
Noetherian scheme들 사이의 projective morphism은 proper morphism이고, quasi-projective morphism은 separated, finite type morphism이다. 
:::
::: 증명
증명의 핵심은 $\pi:\mathbb{P}^n_\mathbb{Z} \rightarrow \Spec\mathbb{Z}$가 proper라는 것이며, 이는 [정리 9](#thm9)의 판정법을 직접 확인하여 얻어진다. 우선 $\mathbb{P}^n_\mathbb{Z}$는 $n+1$개의 affine chart

$$U_i=\Spec \mathbb{Z}[\x_0/\x_i,\ldots,\x_n/\x_i]\qquad (i=0,\ldots,n)$$

을 $U_i\cap U_j=D(\x_j/\x_i)\subseteq U_i$를 따라 붙여 얻어진다. 여기에서 $\x_i/\x_i=1$이므로 각 $U_i$는 $\mathbb{Z}$ 위의 $n$변수 polynomial ring의 spectrum이다. 특히 각 $U_i$는 Noetherian ring의 spectrum이고 chart의 개수가 유한하므로 $\mathbb{P}^n_\mathbb{Z}$는 Noetherian scheme이며, $\pi$는 finite type이다. ([§스킴 사상의 성질들, ⁋정의 13](/ko/math/scheme_theory/properties_of_scheme_morphisms#def13))

$\pi$가 separated인 것은 chart 위에서 직접 확인된다. $\mathbb{P}^n_\mathbb{Z}\times_\mathbb{Z}\mathbb{P}^n_\mathbb{Z}$는 affine open subset들 $U_i\times_\mathbb{Z}U_j$로 덮이고 $p_1\circ\Delta=p_2\circ\Delta=\id$이므로 $\Delta^{-1}(U_i\times_\mathbb{Z}U_j)=U_i\cap U_j$이다. 이제 $\Delta$가 이 위에서 유도하는 ring homomorphism

$$\mathbb{Z}[\x_0/\x_i,\ldots,\x_n/\x_i]\otimes_\mathbb{Z}\mathbb{Z}[\x_0/\x_j,\ldots,\x_n/\x_j] \longrightarrow \mathcal{O}(U_i\cap U_j)=\mathbb{Z}[\x_0/\x_i,\ldots,\x_n/\x_i]_{\x_j/\x_i}$$

를 보면, 우변은 $\mathbb{Z}$ 위에서 $\x_l/\x_i$들과 $(\x_j/\x_i)^{-1}=\x_i/\x_j$로 생성되는데 앞의 것들은 첫째 인자에서, 뒤의 것은 둘째 인자에서 오므로 이 사상은 surjective이다. 따라서 $\Delta$는 각 $U_i\times_\mathbb{Z}U_j$ 위에서 closed embedding이고, closed embedding은 target에 대해 affine-local이므로 ([§닫힌 부분스킴, ⁋명제 3](/ko/math/scheme_theory/closed_subschemes#prop3)) $\Delta$ 자체가 closed embedding이다.

$\Spec \mathbb{Z}$는 scheme들의 category에서 terminal object이므로, valuation ring $A$와 $K=\Frac(A)$에 대한 바깥쪽 square를 주는 것은 morphism $\Spec K \rightarrow \mathbb{P}^n_\mathbb{Z}$를 주는 것과 같다. Lifting의 유일성은 $\pi$가 separated인 것과 [정리 6](#thm6)에서 따르므로 존재성만 보이면 된다. $\Spec K$는 한 점이므로 주어진 morphism의 상은 적당한 chart $U_i$에 들어가고, 따라서 이 morphism은 ring homomorphism

$$\mathbb{Z}[\x_0/\x_i,\ldots,\x_n/\x_i] \longrightarrow K$$

에 대응한다. $\x_j/\x_i$의 상을 $a_j\in K$라 하면 $a_i=1$이다. 이제 $K^\times$ 위에서 $s\preceq t$를 $t/s\in A$로 정의하면, valuation ring의 정의에 의하여 임의의 $s,t$에 대해 $s\preceq t$이거나 $t\preceq s$이고, $t/s\in A$이고 $r/t\in A$일 때 $r/s=(r/t)(t/s)\in A$이므로 $\preceq$는 $K^\times$ 위의 total preorder이다. $a_i=1\neq 0$이므로 유한집합 $\{a_j : a_j\neq 0\}$은 공집합이 아니고, 따라서 이 집합의 최소원 $a_k$를 택할 수 있다. 곧 모든 $j$에 대하여

$$b_j:=a_j/a_k\in A$$

이다. ($a_j=0$인 경우 $b_j=0\in A$이다.) 특별히 $b_k=1$이므로 ring homomorphism

$$\mathbb{Z}[\x_0/\x_k,\ldots,\x_n/\x_k] \longrightarrow A;\qquad \x_j/\x_k\mapsto b_j$$

가 정의되고, 이는 morphism $\Spec A \rightarrow U_k\subseteq\mathbb{P}^n_\mathbb{Z}$를 준다. 이것이 lifting임을 보이려면 $A\hookrightarrow K$와의 합성이 처음 주어진 morphism과 같음을 확인하면 된다. $a_k\neq 0$이므로 처음의 ring homomorphism은 $\x_k/\x_i$를 $K$의 unit $a_k$로 보내고, 따라서 처음 morphism의 상은 $D(\x_k/\x_i)=U_i\cap U_k$에 들어간다. 그럼 $U_k$ 위에서 이 morphism은 transition 관계

$$\x_j/\x_k=(\x_j/\x_i)\cdot(\x_k/\x_i)^{-1}$$

에 의하여 $\x_j/\x_k\mapsto a_j/a_k=b_j$로 주어지므로, 위에서 만든 $\Spec A \rightarrow U_k$를 $\Spec K$로 제한한 것과 정확히 같다. 곧 판정법의 존재성이 성립하고, [정리 9](#thm9)에 의하여 $\pi$는 proper이다.

임의의 Noetherian scheme $Y$에 대하여 $\mathbb{P}^n_Y=\mathbb{P}^n_\mathbb{Z}\times_{\Spec\mathbb{Z}}Y$이다. $Y=\Spec B$인 경우 $\mathbb{P}^n_B$의 chart $\Spec B[\x_0/\x_i,\ldots,\x_n/\x_i]$가 $U_i\times_{\Spec\mathbb{Z}}\Spec B$와 일치하기 때문이며, 일반적인 $Y$에 대해서는 이들을 붙이면 된다. 따라서 [따름정리 10](#cor10)에 의하여 $\mathbb{P}^n_Y \rightarrow Y$는 proper이고, 특히 finite type이므로 $\mathbb{P}^n_Y$는 Noetherian scheme이다.

이제 $f:X \rightarrow Y$가 projective라 하면 $f$는 closed embedding $X\hookrightarrow \mathbb{P}^n_Y$와 projection $\mathbb{P}^n_Y \rightarrow Y$의 합성이다. ([정의 1](#def1)) Closed embedding은 proper이고 두 proper morphism의 합성은 proper이므로 ([따름정리 10](#cor10)), $f$는 proper이다.

마지막으로 $f:X \rightarrow Y$가 quasi-projective라 하고, 이를 open immersion $\iota: X \rightarrow X'$와 projective morphism $g:X' \rightarrow Y$의 합성 $f=g\circ\iota$로 분해하자. ([정의 1](#def1)) 방금 보인 것에 의해 $g$는 proper이고, 따라서 separated이며 finite type이다. 한편 open immersion은 separated이고 두 separated morphism의 합성은 separated이므로 ([따름정리 7](#cor7)), $f$는 separated이다. 또 open immersion은 locally of finite type이며, $X$가 Noetherian이므로 $X'$의 임의의 affine open subset의 $\iota$에 의한 preimage는 Noetherian space의 열린집합으로서 quasi-compact이다. 곧 $\iota$는 finite type이고 ([§스킴 사상의 성질들, ⁋정의 13](/ko/math/scheme_theory/properties_of_scheme_morphisms#def13)), 두 finite type morphism의 합성은 finite type이므로 $f$ 또한 finite type이다.
:::