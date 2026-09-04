---
title: "평탄사상"
description: "평탄 사상의 정의와 기하학적 의미, 판정법과 예시를 다룬다. 평탄성은 사상의 fiber가 기저 위에서 일정한 대수적·기하학적 성질을 유지하도록 보장하는 핵심적인 성질이다."
excerpt: "Flat morphisms in algebraic geometry"

categories: [Math / Scheme Theory]
permalink: /ko/math/scheme_theory/flat_morphisms
sidebar: 
    nav: "scheme_theory-ko"

date: 2025-02-21
weight: 14
---

우리는 scheme morphism $\varphi: X \rightarrow S$를 $S$로 parametrize된 family로 읽기로 하였으며 ([§스킴 사이의 사상, ⁋예시 10](/ko/math/scheme_theory/morphism_of_schemes#ex10)), 이 family의 $s\in S$에서의 member를 fiber $X_s=X\times_S\Spec \kappa(s)$로 정의하였다. ([§올곱, ⁋정의 12](/ko/math/scheme_theory/fiber_products#def12)) 그러나 이 family가 얼마나 좋게 행동할지는 현재로서 우리가 확인할 수 없는 정보이다. 

실제로 이와 같은 family는 나쁘게 행동할 수 있는데, 가령

$$\Spec \mathbb{K}[t,\x]/(t\x) \longrightarrow \mathbb{A}^1_\mathbb{K}=\Spec \mathbb{K}[t]$$

을 보자. 이를 변수 $t$로 parametrize된 family로 생각하면, 고정된 점 $t_0\neq 0$ 위에서는 방정식 $t_0\x=0$이 강제하는 점 $\x=0$ 하나만이 fiber가 되지만, $t=0$ 위에서는 이 조건이 공허해져 fiber가 $\x$ 방향 직선 $\mathbb{A}^1_\mathbb{K}$ 전체가 된다. Fiber의 차원이 $0$에서 $1$로 뛰는 것이다. 

대수적으로 무엇이 잘못되었는지는 이 fiber를 직접 계산해 보면 드러난다. $A=\mathbb{K}[t]$와 $B=\mathbb{K}[t,\x]/(t\x)$라 두면 점 $t_0$에 대응하는 것은 $A$의 maximal ideal $(t-t_0)$이며, 이 때 이 점 $t_0$의 $\Spec A$로의 embedding은 residue field $\kappa(t_0)=A/(t-t_0)$으로의 projection $A\rightarrow \kappa(t_0)$이 유도하는

$$\Spec \kappa(t_0)\rightarrow \Spec A$$

로 주어진다. 즉, 점 $t_0$ 위의 fiber $X_{t_0}$는 이 점을 $\varphi$를 따라 끌어올린 것, 곧 다음의 diagram

{% diagram Math/Scheme_Theory/Flat_Morphisms-1.svg width="11.64em" alt="fiber_as_pullback" %}

으로 주어지며 이 경우 [§올곱, ⁋보조정리 2](/ko/math/scheme_theory/fiber_products#lem2)로부터 $X_{t_0}$은 다음의 tensor product

$$B\otimes_A\kappa(t_0)=\mathbb{K}[t,\x]/(t\x, t-t_0)=\mathbb{K}[\x]/(t_0\x)$$

의 spectrum으로 주어진다는 것을 안다. 그럼 여기에서 만일 $t_0\neq 0$이면 $t_0$가 unit이므로 이는 $\mathbb{K}[\x]/(\x)=\mathbb{K}$가 되어 한 점이고, $t_0=0$이면 나누는 것이 없어 $\mathbb{K}[\x]$ 자신이 되어 직선 전체가 되는 것이다.

이제 차원이 뛴 $t_0=0$에서 일어난 일을 더 자세히 살펴보자. Residue field $\kappa(0)$을 얻기 위해 우리는 이를 $\times t: A\rightarrow A$의 cokernel로 생각하며, 실제로 $A$가 integral domain이므로 우리는 다음의 exact sequence

$$0 \longrightarrow A \xrightarrow{\ \times t\ } A \longrightarrow \kappa(0) \longrightarrow 0$$

가 존재하는 것을 안다. 이제 fiber를 얻기 위해 여기에 $-\otimes_AB$를 적용하면 다음의 diagram

{% diagram Math/Scheme_Theory/Flat_Morphisms-2.svg width="19.88em" alt="tensoring_kills_injectivity" %}

을 얻는데, tensor product는 right exact이므로 아랫줄에는 왼쪽 끝의 $0$이 남지 않는다. 이 때 $B$에서의 $\times t$의 단사성이 깨지는 부분이 정확하게 $\x\neq 0$이 $\times t$를 통해 $t\x=0$으로 가는 현상이며, 기하적으로는 정확히 이 현상이 $t_0=0$에서 모든 affine line이 살아있는 현상으로 나타났던 것이다. 

Fiber를 취하는 것은 base change이고 affine에서 base change는 tensor product이므로, 일반적인 $X=\Spec B$와 $S=\Spec A$에 대해서도 $s\in S$에서의 fiber는 $\Spec (B\otimes_A\kappa(s))$이다. 더 일반적으로 family를 base를 따라 옮기는 연산은 언제나 functor $-\otimes_AB$이며, 위에서 본 대로 이 functor는 exact일 필요가 없으므로 이 때도 비슷한 문제가 일어난다. 즉, 우리가 family에 우선적으로 바라는 조건은 정확히 $-\otimes_AB$가 exact functor인 것, 즉 flatness이다. 

Flat module의 정의와 그 기본 판정법들은 본질적으로 [\[다중선형대수학\] §사영가군, 단사가군, 평탄가군, ⁋정의 7](/ko/math/multilinear_algebra/various_modules#def7)과 [\[가환대수학\] §평탄성](/ko/math/commutative_algebra/flatness)에서 살펴본 기계들이다. Algebraic geometry의 많은 부분들이 그러하듯 flatness 또한 이 기계가 어떻게 만들어졌는지보다는, scheme의 언어에서 이것이 어떠한 방식으로 돌아가는지가 중요하다.

> The concept of flatness is a riddle that comes out of algebra, but which technically is the answer to many prayers. - Mumford

## 평탄 사상의 정의

위에서 지적했듯, 우리가 원하는 조건은 가환대수학에서의 flat module을 기하적으로 가져오는 것이다. 

::: 정의 1
Morphism $\varphi: X \rightarrow Y$가 *flat<sub>평탄</sub>*이라는 것은 임의의 $x \in X$에 대하여 local ring $\mathcal{O}_{X,x}$가 $\mathcal{O}_{Y,\varphi(x)}$-module로서 flat한 것이다. 추가로 $\varphi$가 대응하는 위상공간의 morphism이 전사이면 *faithfully flat<sub>충실평탄</sub>*이라 부른다.
:::

위의 정의에서 flatness는 각 점에서의 국소적인 조건으로 정의되었지만, affine에서는 이를 대역적인 조건으로 바꿔 쓸 수 있다. 

::: 보조정리 2
Ring homomorphism $\phi: A \rightarrow B$가 유도하는 morphism $\varphi: \Spec B \rightarrow \Spec A$에 대하여, $\varphi$가 flat인 것과 $B$가 $A$-module로서 flat한 것은 서로 동치이다.
:::
::: 증명
표기의 편의상 $\mathfrak{q}\in \Spec B$가 주어질 때마다 $\mathfrak{p}=\phi^{-1}(\mathfrak{q})$로 적기로 한다.

우선 $B$가 $A$-flat이라 가정하자. Localization $B \rightarrow B_\mathfrak{q}$는 flat이므로 ([\[가환대수학\] §국소화의 성질들, ⁋명제 2](/ko/math/commutative_algebra/properties_of_localization#prop2)), functor $-\otimes_AB_\mathfrak{q}$는 $-\otimes_AB$와 $-\otimes_BB_\mathfrak{q}$의 합성이 되어 exact이다. 즉 $B_\mathfrak{q}$는 $A$-flat이다. 한편 $B_\mathfrak{q}$는 $A_\mathfrak{p}$-algebra이므로 $A_\mathfrak{p}\otimes_AB_\mathfrak{q}\cong B_\mathfrak{q}$이고, 따라서 임의의 $A_\mathfrak{p}$-module $M$에 대하여

$$M\otimes_AB_\mathfrak{q}\cong M\otimes_{A_\mathfrak{p}}(A_\mathfrak{p}\otimes_AB_\mathfrak{q})\cong M\otimes_{A_\mathfrak{p}}B_\mathfrak{q}$$

가 성립한다. 이제 $A_\mathfrak{p}$-module의 단사사상 $M'\hookrightarrow M$은 $A$-module의 단사사상이기도 하므로 $M'\otimes_AB_\mathfrak{q} \rightarrow M\otimes_AB_\mathfrak{q}$가 단사이고, 위의 isomorphism에 의하여 $M'\otimes_{A_\mathfrak{p}}B_\mathfrak{q} \rightarrow M\otimes_{A_\mathfrak{p}}B_\mathfrak{q}$ 또한 단사이다. 즉 $\mathcal{O}_{\Spec B,\mathfrak{q}}=B_\mathfrak{q}$는 $\mathcal{O}_{\Spec A,\mathfrak{p}}=A_\mathfrak{p}$-flat이며, $\mathfrak{q}$가 임의였으므로 $\varphi$는 flat이다.

역으로 $\varphi$가 flat이라 하자. 각 $\mathfrak{q}$에 대하여 $B_\mathfrak{q}$는 $A_\mathfrak{p}$-flat이고 $A \rightarrow A_\mathfrak{p}$는 flat이므로, 위와 같은 논증에 의하여 $B_\mathfrak{q}$는 $A$-flat이다. 이제 $A$-module의 단사사상 $M'\hookrightarrow M$을 택하고

$$K=\ker(M'\otimes_AB \longrightarrow M\otimes_AB)$$

라 두자. Localization이 exact functor이므로 $B$의 임의의 maximal ideal $\mathfrak{q}$에 대하여 $K_\mathfrak{q}=\ker(M'\otimes_AB_\mathfrak{q} \rightarrow M\otimes_AB_\mathfrak{q})=0$이다. 그런데 $0\neq \xi\in K$가 존재한다면 $\ann(\xi)$는 $B$의 proper ideal이므로 어떤 maximal ideal $\mathfrak{q}$에 포함되고, $K_\mathfrak{q}=0$으로부터 $s\xi=0$인 $s\in B\setminus \mathfrak{q}$가 존재하여 $\ann(\xi)\not\subseteq \mathfrak{q}$가 되어 모순이다. 따라서 $K=0$이고 $B$는 $A$-flat이다.
:::

이 보조정리에 의해 flatness를 확인할 때는 거의 언제나 가환대수학의 도구를 사용할 수 있다. 가령 flatness가 base change와 합성에 대해 안정적이라는 것은 이제 순수하게 대수적인 계산이다.

::: 명제 3
Flat morphism은 base change와 합성에 대하여 닫혀 있다. 즉 다음이 성립한다.

1. $\varphi: X \rightarrow Y$가 flat이고 $Z \rightarrow Y$가 임의의 morphism이면, base change $X \times_Y Z \rightarrow Z$는 flat이다. ([§올곱](/ko/math/scheme_theory/fiber_products))
2. $\varphi: X \rightarrow Y$와 $\psi: Y \rightarrow Z$가 모두 flat이면, 합성 $\psi \circ \varphi: X \rightarrow Z$도 flat이다.
:::
::: 증명
[보조정리 2](#lem2)에 의하여 둘 다 affine case로 환원된다.

(1) $A \rightarrow B$가 flat일 때 임의의 $A$-algebra $C$에 대하여 $C \rightarrow B\otimes_AC$가 flat임을 보이면 된다. 임의의 $C$-module $M$에 대하여

$$(B \otimes_A C) \otimes_C M \cong B \otimes_A (C \otimes_C M) \cong B \otimes_A M$$

이므로, $C$-module의 injection $M' \hookrightarrow M$에 $-\otimes_C (B \otimes_A C)$를 적용한 것은 $B \otimes_A M' \rightarrow B \otimes_A M$과 같다. $B$가 $A$-flat이므로 이 morphism은 단사이고, 따라서 $B \otimes_A C$는 $C$-flat이다.

(2) $A \rightarrow B$와 $B \rightarrow C$가 모두 flat이라 하자. 임의의 $A$-module $N$에 대하여 $N \otimes_A C \cong (N \otimes_A B) \otimes_B C$이므로 functor $-\otimes_A C$는 $-\otimes_A B$와 $-\otimes_B C$의 합성이다. 두 functor가 모두 exact이므로 그 합성 또한 그러하고, 따라서 $C$는 $A$-flat이다.
:::

## Flat family

이제 우리는 몇몇 구체적인 상황들을 살펴보자. 

::: 예시 4
다음은 flat morphism의 가장 기본적인 예시들이다.

1. Open subscheme의 포함사상 $U \hookrightarrow X$는 flat이다. 이는 국소적으로 localization이며, localization은 언제나 flat하기 때문이다. ([\[가환대수학\] §국소화의 성질들, ⁋명제 2](/ko/math/commutative_algebra/properties_of_localization#prop2))
2. Affine space 사이의 projection $\mathbb{A}^{n+m}_\mathbb{K} \rightarrow \mathbb{A}^n_\mathbb{K}$는 flat이다. 이에 대응하는 ring homomorphism $\mathbb{K}[\x_1,\ldots,\x_n] \rightarrow \mathbb{K}[\x_1,\ldots,\x_n,\y_1,\ldots,\y_m]$은 free module 구조를 주고, free module은 flat하기 때문이다.
3. Constant family $C \times_\mathbb{K} S \rightarrow S$는 flat이다. Field 위의 모든 module은 free module이므로 $C \rightarrow \Spec \mathbb{K}$가 flat이고, [명제 3](#prop3)의 base change로부터 그 pullback인 $C\times_\mathbb{K}S \rightarrow S$도 flat이기 때문이다.

반대로 flat이 아닌 morphism의 대표적인 예시로는 도입에서 살펴본 

$$X=\Spec \mathbb{K}[t,\x]/(t\x) \rightarrow \mathbb{A}^1_\mathbb{K}$$

가 있다. 우리는 이미 $B=\mathbb{K}[t,\x]/(t\x)$ 위의 $\times t$가 단사가 아님을 보았으므로, 이것이 flat이 아니라는 것은 이제 [보조정리 2](#lem2)의 직접적인 결과이다. 직관적으로 $X$는 평면의 두 좌표축의 합집합인데, 이 가운데 $\{\x=0\}$은 base 위로 전사하지만 $\{t=0\}$은 base의 한 점으로만 간다. 즉 $X$에는 base를 따라 퍼지지 않고 fiber 하나에 통째로 얹혀 있는 성분이 있으며, 이것이 $t=0$의 fiber를 부풀린 원인이다.
:::

위의 반례를 대수적으로 다시 읽으면, $B$ 안에 parameter $t$를 죽이는 원소 $\x\neq 0$이 있다는 것, 곧 $t$가 $B$에서 zerodivisor라는 것이 flatness를 깨뜨렸다. Base가 PID의 spectrum인 경우에는 이 현상이 flatness의 실패와 정확히 같은 것이 된다.

::: 명제 5
$A$가 PID이고 $B$가 $A$-algebra라 하자. 그럼 $\Spec B \rightarrow \Spec A$가 flat인 것과, $A$의 $0$이 아닌 임의의 원소가 $B$에서 zerodivisor가 아닌 것은 서로 동치이다.
:::
::: 증명
[보조정리 2](#lem2)에 의하여 이는 $B$가 $A$-flat인 것과 동치이다. $A$가 PID이므로 특히 integral domain이고, 따라서 $A$의 $0$이 아닌 원소는 모두 $A$에서 zerodivisor가 아니다. 이제 [\[가환대수학\] §평탄성, ⁋따름정리 3](/ko/math/commutative_algebra/flatness#cor3)을 $M=B$에 적용하면 된다.
:::

즉, $\mathbb{K}[t]$ 위의 family가 flat인 것은 그 coordinate ring이 $\mathbb{K}[t]$-module로서 torsion을 갖지 않는 것과 같다. Torsion 원소란 base의 함수 하나에 의해 죽는 원소이며, 기하학적으로는 fiber 하나에 갇힌 성분이 그러한 원소를 낳는다.

이를 정확히 적기 위해서는 [§스킴 사상의 성질들, ⁋정의 19](/ko/math/scheme_theory/properties_of_scheme_morphisms#def19)의 dominant morphism이 필요하다. 아래에서 $X$의 irreducible component $Z$가 base를 dominate한다는 것은, $Z$에 reduced closed subscheme 구조를 준 뒤 포함사상과 $\varphi$를 합성한 것이 dominant라는 뜻이다.

::: 따름정리 6
Noetherian $\mathbb{K}[t]$-algebra $B$에 대하여 $X=\Spec B$가 reduced라 하자. 그럼 $X \rightarrow \mathbb{A}^1_\mathbb{K}$가 flat인 것과, $X$의 모든 irreducible component가 $\mathbb{A}^1_\mathbb{K}$를 dominate하는 것은 서로 동치이다.
:::
::: 증명
[명제 5](#prop5)에 의하여 flatness는 $\mathbb{K}[t]$의 $0$이 아닌 모든 원소가 $B$에서 zerodivisor가 아닌 것과 동치이다.

$B$가 Noetherian이므로 $B$의 zerodivisor 전체는 $\Ass B$의 원소들의 합집합이다. ([\[가환대수학\] §동반소아이디얼, ⁋정리 7](/ko/math/commutative_algebra/associated_primes#thm7)) 여기에 $B$가 reduced라는 가정을 더하면 이 합집합은 정확히 $B$의 minimal prime ideal $\mathfrak{p}_1,\ldots, \mathfrak{p}_k$들의 합집합이 된다. 실제로 minimal prime들이 언제나 $\Ass B$에 속한다는 것이 이 정리의 첫째 결과이고, 역으로 $B$가 reduced이면

$$(0)=\mathfrak{N}(B)=\bigcap_{i=1}^k \mathfrak{p}_i$$

이므로, $ab=0$이고 $b\neq 0$인 zerodivisor $a$에 대하여 $b\not\in \mathfrak{p}_i$인 $i$를 택하면 $ab=0\in \mathfrak{p}_i$로부터 $a\in \mathfrak{p}_i$를 얻기 때문이다.

한편 $\mathfrak{p}_i$들은 정확히 $X$의 irreducible component $Z_i=V(\mathfrak{p}_i)$들의 generic point에 대응한다. 이제 $0\neq f\in \mathbb{K}[t]$가 $B$에서 zerodivisor인 것은 어떤 $i$에 대하여 $f\in \mathfrak{p}_i$인 것, 즉 $f$가 $Z_i$ 위에서 항등적으로 소멸하는 것과 같다. 그런데 $f$가 $Z_i$ 위에서 소멸한다는 것은 $Z_i$의 image가 진부분 닫힌집합 $Z(f)\subsetneq \mathbb{A}^1_\mathbb{K}$에 포함된다는 것, 즉 $Z_i$가 $\mathbb{A}^1_\mathbb{K}$를 dominate하지 않는다는 것과 같다. 역으로 $Z_i$가 dominate하지 않으면 그 image의 closure가 진부분 닫힌집합이므로 그 위에서 소멸하는 $0$이 아닌 $f\in \mathbb{K}[t]$가 존재하고, 이 $f$는 $\mathfrak{p}_i$에 속하여 zerodivisor가 된다. 이상에서 결론을 얻는다.
:::

도입에서 본 $X=\Spec \mathbb{K}[t,\x]/(t\x)$는 reduced이고 그 성분 $\{t=0\}$이 base를 dominate하지 않으므로, [따름정리 6](#cor6)이 곧바로 non-flatness를 준다. 

다만 주의할 것은, flatness가 family의 변화 자체를 막는 것이 아니라, 그 family가 무너지는 것만 막는다는 것이다. 가령, flat family의 어떠한 fiber는 singular할 수 있다. 

::: 예시 7
이번 예시에서 우리는 curve들의 family 가운데 특정한 fiber가 singular해지는 경우를 살펴본다. Curve의 singularity 중 특별한 위치를 차지하고 있던 두 예시가 cusp singularity와 nodal singularity였음을 기억하자. ([\[대수다양체\] §접공간과 매끄러움, ⁋예시 7](/ko/math/algebraic_varieties/tangent_spaces_and_smoothness#ex7))

우선 curve들의 family

$$\Spec \mathbb{K}[t, \x, \y]/(\y^2 - \x^3 - t) \longrightarrow \mathbb{A}^1_\mathbb{K}$$

를 생각하자. 관계식이 $t = \y^2 - \x^3$을 주므로 coordinate ring은 $\mathbb{K}[\x,\y]$와 isomorphic이며, 이 isomorphism 아래에서 $\mathbb{K}[t]$의 action은 $t \mapsto \y^2-\x^3$으로 주어진다. $\y^2-\x^3$이 상수가 아니므로 $\mathbb{K}$ 위에서 초월적이고, 따라서 $\mathbb{K}[t] \rightarrow \mathbb{K}[\x,\y]$는 단사이다. 그럼 $\mathbb{K}[t]$의 $0$이 아닌 원소는 integral domain의 $0$이 아닌 원소로 옮겨져 zerodivisor일 수 없고, [명제 5](#prop5)에 의하여 이 morphism은 flat이다. 그럼에도 $t=0$ 위의 fiber는 cusp singularity를 갖는 $\y^2=\x^3$이다.

또 다른 curve들의 family

$$\Spec \mathbb{K}[t, \x, \y]/(\x\y - t) \longrightarrow \mathbb{A}^1_\mathbb{K}$$

도 마찬가지이다. $t=\x\y$로 두면 coordinate ring은 integral domain $\mathbb{K}[\x,\y]$와 isomorphic하고 $\x\y$ 또한 상수가 아니므로 같은 이유로 flat이며, $t\neq 0$ 위의 fiber는 smooth한 쌍곡선 $\x\y=t$이지만 $t=0$ 위의 fiber는 두 직선이 만나 nodal singularity를 갖는 $\x\y=0$이다.

요컨대 flatness가 통제하는 것은 fiber가 특이해지는지의 여부가 아니라, fiber가 크기를 유지한 채로 이어지는지의 여부이다.
:::

지금까지 본 family에서 fiber는 모두 $\mathbb{A}^2$ 안의 곡선이었고, 따라서 무한대에 놓인 점들이 빠져 있었다. 이들까지 함께 보려면 곡선을 $\mathbb{P}^2$ 안에서 자르는 것이 자연스럽다. ([§사영공간과 Proj 구성](/ko/math/scheme_theory/projective_schemes)) 이 때 $X$는 더 이상 affine이 아니므로 flatness는 affine chart마다 확인하게 된다.

::: 예시 8
$\x,\y,\z$의 degree로 grading을 준 graded ring $A_\bullet=\mathbb{K}[t][\x,\y,\z]$를 생각하자. 여기에서 $t$는 degree $0$이며, 따라서 base ring은 $A_0=\mathbb{K}[t]$이다. Chart를 계산하면 $A_{(\x)}=\mathbb{K}[t][\y/\x,\z/\x]$이므로 $D_+(\x)$는 $\mathbb{A}^2_{\mathbb{K}[t]}$이고, $t$가 degree $0$이라 localization에서 살아남는다. 세 chart를 붙이면 $\Proj A_\bullet$은 $\mathbb{P}^2\times_\mathbb{K}\mathbb{A}^1_\mathbb{K}$가 되며, 모든 $f$에 대하여 $A_0\subseteq A_{(f)}$이므로 이들이 붙어 structure morphism $\Proj A_\bullet \rightarrow \mathbb{A}^1_\mathbb{K}$를 준다.

이제 $\x\z-t\y^2$을 보면 $\x\z$와 $t\y^2$이 모두 $\x,\y,\z$에 대하여 degree $2$이므로 이는 homogeneous element이다. 여기에서도 $t$의 degree가 $0$인 것이 쓰인다. 따라서 $(\x\z-t\y^2)$는 homogeneous ideal이고, [§사영공간의 닫힌 부분스킴, ⁋명제 1](/ko/math/scheme_theory/closed_subschemes_of_projective_spaces#prop1)에 의하여

$$X=\Proj A_\bullet/(\x\z-t\y^2)$$

은 $\mathbb{P}^2\times_\mathbb{K}\mathbb{A}^1_\mathbb{K}$의 closed subscheme으로서 $V_+(\x\z-t\y^2)$이다. 즉 $X$는 $\mathbb{P}^2$ 안에서 방정식 $\x\z=t\y^2$이 자르는 곡선들의 family이며, 위의 structure morphism이 이를 $\mathbb{A}^1_\mathbb{K}$ 위의 family로 만든다.

이 morphism이 flat인 것은 세 개의 affine chart에서 확인된다. $D_+(\y)$ 위에서 $u=\x/\y$, $v=\z/\y$로 두면 관계식을 $\y^2$으로 나누어 $uv=t$를 얻으므로 coordinate ring은 $\mathbb{K}[t][u,v]/(uv-t)$이며, 이는 $t=uv$를 통해 integral domain $\mathbb{K}[u,v]$와 isomorphic이다. $uv$ 또한 상수가 아니므로 [예시 7](#ex7)에서와 같은 이유로 [명제 5](#prop5)에 의하여 flat이다. $D_+(\x)$ 위에서 $w=\y/\x$, $s=\z/\x$로 두면 관계식을 $\x^2$으로 나누어 $s=tw^2$을 얻으므로 coordinate ring은 $\mathbb{K}[t][w]$이고, 이는 free $\mathbb{K}[t]$-module이므로 flat이다. $D_+(\z)$의 경우도 symmetric이다. 이 셋이 $X$를 덮으므로 $X \rightarrow \mathbb{A}^1_\mathbb{K}$는 flat이다.

Fiber를 보면, $t=a\neq 0$ 위에서는 $\mathbb{P}^2$의 원뿔곡선 $\x\z=a\y^2$이 되어 smooth하고 $\mathbb{P}^1$과 isomorphic이다. 반면 $t=0$ 위에서는 $\x\z=0$, 즉 두 직선 $\{\x=0\}$과 $\{\z=0\}$이 점 $[0:1:0]$에서 만나는 곡선이 된다. 즉 이것은 smooth한 원뿔곡선이 두 직선으로 퇴화하는 상수 아닌 곡선들의 family이며, 그럼에도 모든 fiber가 $1$차원으로 남는다.
:::

## 평탄성의 실패

그렇다면 언제 morphism이 flat이 아니게 되는지를 살펴보자. 직관적으로 morphism이 flat이 아니게 되는 상황은 어떤 방식으로든 $X$의 어떤 부분이 base를 따라 퍼지지 못하고 fiber 하나에 통째로 얹혀 있는 것이다. [명제 5](#prop5)의 언어로는 이것이 base의 함수 하나에 죽는 원소, 곧 torsion으로 나타난다. 다만 갇히는 것이 무엇이냐에 따라 겉으로 드러나는 모습은 셋으로 갈린다.

첫째는 이 글의 도입에서 본 $\Spec \mathbb{K}[t,\x]/(t\x)$로, $\x$-축이 $t=0$ 위의 fiber에 통째로 들어앉아 fiber의 차원이 $0$에서 $1$로 뛰었다. 이는 [예시 4](#ex4)에서 이미 다룬 경우로, fiber 방향에 양의 차원 성분이 갇혀있는 경우에 해당한다.

둘째 예시는 갇히는 것이 $0$차원인 경우이다. 이 경우에는 차원은 아무 데에서도 변하지 않지만, fiber의 점의 개수만 달라진다.

::: 예시 9
$X$를 affine line에 원점 위의 isolated point 하나를 더한 것으로 두자. 이를 나타내는 coordinate ring은

$$B=\mathbb{K}[t]\times \mathbb{K}$$

으로, 실제로 $B$의 prime ideal을 직접 적으면 이 그림이 분명해진다. $e=(0,1)$은 $e(1-e)=0$을 만족하므로 $B$의 임의의 prime ideal은 $e$와 $1-e$ 가운데 정확히 하나를 포함한다는 것을 알 수 있으며, 이 때 $e$를 포함하는 것은 $B/(0\times \mathbb{K})=\mathbb{K}[t]$의 prime ideal에, $1-e$를 포함하는 것은 $B/(\mathbb{K}[t]\times 0)=\mathbb{K}$의 prime ideal에 각각 대응된다. 이는 $\mathbb{A}^2_\mathbb{K}$ 평면 안에서는 $X=Z(t\x, \x^2-\x)$로 나타낼 수 있다.

이제 $\phi:\mathbb{K}[t] \rightarrow B$를 $t\mapsto (t,0)$으로 정의하자. 그럼 $\phi(f)=(f, f(0))$이므로

$$\phi^{-1}(\mathfrak{p}\times \mathbb{K})=\mathfrak{p},\qquad \phi^{-1}(\mathbb{K}[t]\times 0)=(t)$$

이 된다. 즉, $\Spec\phi$의 target인 affine line의 원점을 제외한 모든 점은 정확히 $X$의 같은 점을 fiber의 유일한 점으로 가지지만, 원점에서의 fiber는 $X$의 원점과, 원점 위에 있는 한 점의 두 개의 점을 가진다. 즉, fiber의 차원은 어디에서나 $0$이지만, fiber를 이루는 점의 개수가 $1$에서 $2$로 뛴다.

이것이 flat이 아닌 것은 $(0,1)\neq 0$이면서 $t\cdot (0,1)=0$이므로 $t$가 $B$에서 zerodivisor이기 때문이다. ([명제 5](#prop5)) $X$가 reduced이므로 [따름정리 6](#cor6)으로도 같은 결론을 얻는데, 두 성분 가운데 isolated point가 $\mathbb{A}^1_\mathbb{K}$를 dominate하지 못하기 때문이다.
:::

마지막 예시는 갇히는 것이 embedded point인 경우로 ([§스킴의 대수구조, ⁋정의 9](/ko/math/scheme_theory/algebra_of_schemes#def9)), 이번에는 차원도 점의 개수도 변하지 않지만, fiber의 length가 달라진다. ([\[가환대수학\] §조르단-횔더 정리, ⁋정의 2](/ko/math/commutative_algebra/Jordan-Holder_theorem#def2))

::: 예시 10
Scheme morphism

$$X=\Spec \mathbb{K}[t,\x]/(\x^2, t\x) \longrightarrow \mathbb{A}^1_\mathbb{K}$$

를 생각하자. Ideal이 $(\x^2, t\x)=(\x)\cap (t,\x^2)$로 분해되므로 $X$는 $t$-축이며, 원점이 embedded point가 된다.

이 morphism의 fiber는 $t=a$ 위에서 $\mathbb{K}[\x]/(\x^2, a\x)$이다. 만일 $a\neq 0$이면 $a$가 unit이라 $\x=0$이 강제되므로 이 fiber는 $\mathbb{K}$가 되지만, $a=0$이면 $\mathbb{K}[\x]/(\x^2)$이 되어 길이 $2$의 한 점이 된다. 위상적으로는 $\Spec \mathbb{K}$도, $\Spec \mathbb{K}[\x]/(\x^2)$도 점 하나이므로 fiber의 차원도 개수도 그대로이지만, 여전히 length는 $1$에서 $2$로 뛴다.

이 morphism은 실제로 $\x\neq 0$이면서 $t\x=0$이므로 [명제 5](#prop5)에 의하여 flat이 아니다. 다소 주의할 것은 이로부터 따라나오는 판정법인 [따름정리 6](#cor6)은 이 상황에서 적용할 수 없다는 것으로, 이는 $X$가 reduced가 아니기 때문이다. 실제로 $X$의 reduced structure인 $t$-축은 base와 isomorphic하여 flat이므로, 이 실패는 scheme 구조를 보아야만 드러난다.
:::

이 세 경우를 보면 흥미로운 것이 두 가지 있다. 우선, 우리는 서로 다른 세 가지 예시를 살펴보았으나 본질적으로는 [예시 10](#ex10)의 length가 [예시 9](#ex9)의 실패까지 포함한다. 뿐만 아니라, 이를 Hilbert polynomial로 한 층 올리면 도입에서 본 예시까지 함께 포괄된다. ([\[대수다양체\] §베주 정리, ⁋명제 3](/ko/math/algebraic_varieties/bezout_theorem#prop3)) 즉, 세 실패는 모두 하나의 다항식이 뛴 것이며, 실제로 Noetherian integral scheme 위의 projective family에 대하여 flat인 것과 fiber의 Hilbert polynomial이 일정한 것은 서로 동치이다. 이 예시들이 알려주는 흥미로운 점 중 다른 하나는 뛰는 방향으로, 세 경우 모두에서 값은 일반적인 열린집합에서는 작다가, flatness가 깨지는 곳으로 가면서 커졌을 뿐, 그 반대로 움직인 적이 없다. 이 글의 말미에서 우리는 이것이 우연이 아니라는 것을 살펴보게 될 것이다. 

## Generic flatness와 Chevalley의 정리

이제 우리는 글의 남은 부분에서 flat morphism의 기하학적 성질들을 더 살펴본다. 이를 위해서는 두 가지의 준비가 필요하며, 이 섹션은 이들을 위한 것이다. 이 두 준비물은 모두 [\[가환대수학\] §뇌터 정규화, ⁋정리 6](/ko/math/commutative_algebra/noether_normalization#thm6)를 사용하여 증명할 수 있다.

::: 명제 11 (Generic flatness)
Noetherian integral scheme $Y$와 finite type morphism $\varphi: X \rightarrow Y$가 주어졌다 하자. 그럼 $Y$의 dense open subset $U$가 존재하여 $\varphi\rvert^U: \varphi^{-1}(U) \rightarrow U$가 flat이다.
:::
::: 증명
$Y$가 irreducible이므로 $Y$의 공집합이 아닌 열린집합은 모두 dense이다. 따라서 $Y$의 affine open $V=\Spec A$를 하나 고정하고 그 안에서 $U$를 찾으면 충분하다. $Y$가 integral scheme이므로 $A=\mathcal{O}_Y(V)$는 integral domain이고, Noetherian scheme의 affine open은 Noetherian ring의 spectrum이므로 $A$는 Noetherian ring이기도 하다. ([§스킴의 위상구조, ⁋보조정리 13](/ko/math/scheme_theory/topology_of_schemes#lem13))

한편, $\varphi$가 finite type이므로 $\varphi^{-1}(V)$는 유한개의 affine open $\Spec B_1,\ldots, \Spec B_k$로 덮이고 ([§스킴 사상의 성질들, ⁋정의 14](/ko/math/scheme_theory/properties_of_scheme_morphisms#def14)), 각 $B_i$는 finite type $A$-algebra이다. [\[가환대수학\] §뇌터 정규화, ⁋정리 6](/ko/math/commutative_algebra/noether_normalization#thm6)를 $M=B_i$에 적용하면 $0\neq a_i\in A$가 존재하여 $(B_i)_{a_i}$가 free $A_{a_i}$-module이다. $a=a_1\cdots a_k$로 두면 각 $(B_i)_a$는 free module $(B_i)_{a_i}$의 localization이므로 여전히 free $A_a$-module이고, free module은 flat하므로 [보조정리 2](#lem2)에 의하여

$$\Spec (B_i)_a \longrightarrow \Spec A_a=D(a)$$

는 flat이다. Flatness는 $X$ 위에서 국소적인 조건이고 $\Spec (B_i)_a$들이 $\varphi^{-1}(D(a))$를 덮으므로 $\varphi^{-1}(D(a)) \rightarrow D(a)$는 flat이다. $A$가 integral domain이고 $a\neq 0$이므로 $D(a)$는 공집합이 아니며, 따라서 $U=D(a)$를 열린집합으로 택하면 된다.
:::

두 번째 명제는 image의 모양에 대한 것이다. 일반적인 morphism의 image는 열린집합도 닫힌집합도 아니지만, finite type morphism의 image는 언제나 다음의 의미에서 좋은 집합이다.

::: 정의 12
위상공간 $T$의 부분집합이 *constructible<sub>구성가능</sub>*이라는 것은 그것이 유한개의 locally closed subset들의 합집합으로 쓰일 수 있는 것이다. ([\[위상수학\] §몫공간, ⁋정의 1](/ko/math/topology/quotient_spaces#def1))
:::

직관적으로 constructible subset은 유한개의 방정식의 zero locus와, 그 여집합으로 잘라낼 수 있는 집합으로, 우리가 생각하는 기하적인 대상들에 부합하는 조각들이다. 더 엄밀하게는 locally closed subset이 열린집합과 닫힌집합의 교집합 $U\cap Z$로 쓰이고 그 여집합이 다시 두 locally closed subset의 합집합 $(T\setminus U)\cup(T\setminus Z)$이므로 ([\[위상수학\] §몫공간, ⁋명제 2](/ko/math/topology/quotient_spaces#prop2)), constructible subset들의 모임은 유한한 합집합, 유한한 교집합, 여집합에 대하여 닫혀 있다는 것을 안다. 

::: 정리 13 (Chevalley)
Noetherian scheme $Y$와 finite type morphism $\varphi: X \rightarrow Y$에 대하여, $\varphi(X)$는 $Y$의 constructible subset이다.
:::
::: 증명
$Y$가 Noetherian이므로 유한개의 affine open $V_j$로 덮이고, $\varphi$가 finite type이므로 각 $\varphi^{-1}(V_j)$ 또한 유한개의 affine open으로 덮인다. 따라서 $\varphi(X)$는 유한개의 $\Spec B \rightarrow \Spec A$ 꼴 morphism의 image들의 합집합이다. 열린집합 $V_j$의 constructible subset은 $Y$의 constructible subset이고 constructible subset들의 유한합집합은 constructible이므로, 처음부터 $Y=\Spec A$, $X=\Spec B$이고 $B$가 ring homomorphism $\phi: A \rightarrow B$를 통한 finite type $A$-algebra인 경우만 보이면 충분하다.

이 affine case는 $Y$의 closed subset에 대한 Noetherian induction으로 해결한다. $Y=\Spec A$의 closed subset $Z$에 대하여, 명제 $P(Z)$를

> $\Spec C \rightarrow Z$ 꼴의 임의의 finite type morphism의 image는 $Y$의 constructible subset이다.

이라 하자. $A$가 Noetherian이므로 $Y=\Spec A$는 Noetherian space이고 ([§스킴의 위상구조, ⁋명제 7](/ko/math/scheme_theory/topology_of_schemes#prop7)), 그 위에서 Noetherian induction을 쓸 수 있다. ([\[위상수학\] §차원, ⁋명제 14](/ko/math/topology/dimension#prop14)) 즉 $Y$의 모든 진부분 닫힌집합 $Z\subsetneq Y$에 대하여 $P(Z)$가 성립한다고 가정하고 $P(Y)$를 보이면 된다.

먼저 $A$의 nilradical $\mathfrak{N}=\mathfrak{N}(A)$에 대하여 $\mathfrak{N}B$는 $B$의 nilpotent ideal이므로 $\Spec B/\mathfrak{N}B$와 $\Spec B$는 같은 위상공간이고, $\Spec A/\mathfrak{N}$과 $\Spec A$도 그러하다. ([§차원, §§스킴의 차원](/ko/math/scheme_theory/dimension#스킴의-차원)) 따라서, 필요하다면 $A$를 $A/\mathfrak{N}$으로, $B$를 $B/\mathfrak{N}B$로 바꾸어 $A$가 reduced라 가정해도 좋다.

이제 $A$의 minimal prime을 $\mathfrak{p}_1,\ldots, \mathfrak{p}_k$라 하자. 그럼 임의의 prime ideal은 항상 적당한 minimal prime을 포함하므로 $Y=\bigcup_j V(\mathfrak{p}_j)$이다. 만일 $k\geq 2$라면 각 $V(\mathfrak{p}_j)$는 $Y$의 진부분 닫힌집합이고

$$\varphi(X)=\bigcup_{j=1}^k \varphi\big(X\times_Y V(\mathfrak{p}_j)\big)$$

인데, 각 base change $X\times_YV(\mathfrak{p}_j)=\Spec (B\otimes_AA/\mathfrak{p}_j) \rightarrow V(\mathfrak{p}_j)$는 여전히 affine이고 finite type이므로 Noetherian induction의 귀납가정 $P(V(\mathfrak{p}_j))$에 의하여 각 항이 constructible이고 따라서 $\varphi(X)$도 constructible이다. 그러므로 $k=1$, 즉 $A$가 integral domain인 경우만 고려해도 충분하다.

$B=0$인 경우는 자명하므로 $B\neq 0$이라 하자. 그럼 [\[가환대수학\] §뇌터 정규화, ⁋정리 6](/ko/math/commutative_algebra/noether_normalization#thm6)에 의해 $0\neq a\in A$가 존재하여 $B_a$가 free $A_a$-module이다. $a$가 unit인 경우는 마찬가지로 자명하므로,  $a$가 non-unit이라 하자. 이 경우 $A$가 integral domain이므로 $V(a)$는 $Y$의 진부분 닫힌집합이다. 

우선 만일 $B_a=0$인 경우, 이는 $\phi(a)$가 $B$에서 nilpotent라는 뜻이므로 $\phi(a)$는 $B$의 모든 prime ideal에 속한다. 따라서 $\varphi(X)\subseteq V(a)$이고, $\varphi(X)$는 base change $X\times_YV(a) \rightarrow V(a)$의 image와 같으므로 귀납가정 $P(V(a))$에 의하여 constructible이다.

마지막으로 $B_a\neq 0$이어서 $B_a$가 $0$이 아닌 free $A_a$-module인 경우를 보자. 임의의 $\mathfrak{p}\in D(a)$에 대하여, $B_a$의 rank를 $r$이라 하면

$$B_a\otimes_{A_a}\kappa(\mathfrak{p})\cong \kappa(\mathfrak{p})^{\oplus r}\neq 0$$

이므로 $\mathfrak{p}$ 위의 fiber는 공집합이 아니고, 따라서 $D(a)\subseteq \varphi(X)$이다. 그럼

$$\varphi(X)=D(a)\cup \big(\varphi(X)\cap V(a)\big)$$

이고, $\varphi(X)\cap V(a)$는 base change $X\times_YV(a) \rightarrow V(a)$의 image이므로 귀납가정 $P(V(a))$에 의하여 constructible이다. $D(a)$는 열린집합이므로 constructible이고, 따라서 $\varphi(X)$는 constructible이다.
:::

마지막으로 우리는 constructible set이 언제 열린집합이 되는지도 함께 정리해둔다.

::: 보조정리 14
Noetherian scheme $Y$의 constructible subset $E$가 generization에 대하여 닫혀 있다면, 즉 $y\in E$이고 $y\in \overline{\{y'\}}$일 때마다 $y'\in E$라면, $E$는 $Y$의 열린집합이다.
:::
::: 증명
여집합 $F=Y\setminus E$는 constructible이며 specialization에 대하여 닫혀 있다. 이를 이용하여 $F$가 닫힌집합임을 보이자. $F=\emptyset$인 경우는 자명하므로 $F\neq \emptyset$이라 하고, $Z=\overline{F}$의 irreducible component들을 $Z_1,\ldots, Z_k$라 하자. $Y$가 Noetherian이므로 이들은 유한개이다.

먼저 각 $j$에 대하여 $\overline{F\cap Z_j}=Z_j$임을 보인다. 만일 $W=\overline{F\cap Z_j}\subsetneq Z_j$라면 $F\subseteq W\cup \bigcup_{i\neq j}Z_i$이고 우변이 닫힌집합이므로 $Z=\overline{F}\subseteq W\cup \bigcup_{i\neq j}Z_i$인데, 이는 $Z_j$가 $Z$의 irreducible component라는 것에 모순이다.

이제 $F$를 locally closed subset들의 유한합집합 $F=\bigcup_{i=1}^n (U_i\cap C_i)$로 쓰자. $Z_j$가 irreducible이고

$$Z_j=\overline{F\cap Z_j}=\bigcup_{i=1}^n \overline{U_i\cap C_i\cap Z_j}$$

이므로, 적당한 $i$에 대하여 $\overline{U_i\cap C_i\cap Z_j}=Z_j$이다. 그럼 $U_i\cap C_i\cap Z_j\subseteq C_i$이고 $C_i$가 닫힌집합이므로 $Z_j\subseteq C_i$이며, 따라서

$$U_i\cap Z_j\subseteq U_i\cap C_i\subseteq F$$

이다. 한편 $U_i\cap Z_j$는 $Z_j$의 열린 부분집합이며 그 closure가 $Z_j$이므로 공집합이 아니다. $Z_j$는 $Y$의 irreducible closed subset이므로 generic point $\zeta_j$를 가지며, $Z_j$의 공집합이 아닌 열린 부분집합은 언제나 $\zeta_j$를 포함하므로 $\zeta_j\in F$이다.

$F$가 specialization에 대하여 닫혀 있으므로 $Z_j=\overline{\{\zeta_j\}}\subseteq F$이고, 이것이 모든 $j$에 대하여 성립하므로 $Z=\bigcup_j Z_j\subseteq F$이다. $F\subseteq Z$는 자명하므로 $F=Z$는 닫힌집합이다.
:::

## 평탄 사상의 기하학적 성질

이제 모든 준비를 마쳤으므로 flatness의 기하학적 의미를 살펴보자. Flatness의 내용은 fiber들이 서로 이어지는 방식을 통제한다는 데에 있으며, 그 출발점은 flat local homomorphism이 자동으로 faithfully flat이 된다는 다음 관찰이다.

::: 보조정리 15
Local ring 사이의 local homomorphism $\phi: (A,\mathfrak{m}) \rightarrow (B,\mathfrak{n})$이 $B$를 flat $A$-module로 만든다 하자. 그럼 $0$이 아닌 임의의 $A$-module $M$에 대하여 $M\otimes_AB\neq 0$이며, 특히 $\Spec B \rightarrow \Spec A$는 전사이다.
:::
::: 증명
$0\neq \xi\in M$을 택하자. $\ann(\xi)$는 $A$의 proper ideal이므로 $\ann(\xi)\subseteq \mathfrak{m}$이고, $A/\ann(\xi)\cong A\xi$는 $M$의 submodule이다. 여기에 flat functor $-\otimes_AB$를 적용하면 단사사상

$$B/\ann(\xi)B\cong (A/\ann(\xi))\otimes_AB\hookrightarrow M\otimes_AB$$

를 얻는다. 그런데 $\phi$가 local homomorphism이므로 $\ann(\xi)B\subseteq \mathfrak{m}B\subseteq \mathfrak{n}\subsetneq B$이고, 따라서 $B/\ann(\xi)B\neq 0$이다. 즉 $M\otimes_AB\neq 0$이다.

이제 임의의 $\mathfrak{p}\in \Spec A$에 대하여 $M=\kappa(\mathfrak{p})$로 두면 $\kappa(\mathfrak{p})\neq 0$이므로 fiber를 나타내는 ring

$$B\otimes_A\kappa(\mathfrak{p})$$

은 $0$이 아니고, 따라서 prime ideal을 갖는다. 그러한 prime ideal에 대응하는 $\Spec B$의 점은 $\mathfrak{p}$ 위에 놓이므로 $\Spec B \rightarrow \Spec A$는 전사이다.
:::

이로부터 flat morphism이 generization을 들어올린다는 *going-down* 성질을 얻는다. ([\[가환대수학\] §매개계, ⁋보조정리 8](/ko/math/commutative_algebra/system_of_parameters#lem8))

::: 명제 16
Flat morphism $\varphi: X \rightarrow Y$와 점 $x \in X$가 주어졌다 하고, $y=\varphi(x)$의 generization $y'$, 즉 $y \in \overline{\{y'\}}$인 점 $y'$가 주어졌다 하자. 그럼 $x$의 generization $x'$가 존재하여 $\varphi(x')=y'$이다.
:::
::: 증명
$y$의 affine open neighborhood $V=\Spec A$를 택하고, 그 다음 $\varphi^{-1}(V)$ 안에서 $x$의 affine open neighborhood $U=\Spec B$를 택하자. $y'$이 $y$의 generization이므로 $y'\in V$이다. 따라서 $X=\Spec B$, $Y=\Spec A$이고, $\varphi$에 대응하는 ring homomorphism을 $\phi: A \rightarrow B$라 할 때 $x=\mathfrak{q}$, $y=\mathfrak{p}=\phi^{-1}(\mathfrak{q})$, $y'=\mathfrak{p}'\subseteq \mathfrak{p}$인 경우만 보이면 충분하다.

[보조정리 2](#lem2)에 의하여 $A_\mathfrak{p} \rightarrow B_\mathfrak{q}$는 flat한 local homomorphism이므로, [보조정리 15](#lem15)에 의하여 $\Spec B_\mathfrak{q} \rightarrow \Spec A_\mathfrak{p}$는 전사이다. 특히 $\mathfrak{p}'A_\mathfrak{p}\in \Spec A_\mathfrak{p}$ 위에 놓인 $\Spec B_\mathfrak{q}$의 점이 존재하며, 이를 $B$의 prime ideal로 되돌리면 $\mathfrak{q}'\subseteq \mathfrak{q}$이면서 $\phi^{-1}(\mathfrak{q}')=\mathfrak{p}'$인 $\mathfrak{q}'$를 얻는다. $\mathfrak{q}'\subseteq \mathfrak{q}$는 곧 $x\in \overline{\{x'\}}$을 뜻하므로 $x'=\mathfrak{q}'$가 원하는 점이다.
:::

즉 flat morphism은 base에서의 generization을 언제나 위로 들어올린다. 특히 $Y$가 irreducible이고 그 generic point가 $y$라면 $X$의 임의의 점은 generic fiber $X_y$의 어떤 점의 specialization이며, 따라서 $X$의 어떤 성분도 fiber 하나에 갇혀 있을 수 없다. [따름정리 6](#cor6)에서 곡선 위의 family에 대하여 관찰한 것이 일반적으로도 성립하는 것이다.

Going-down의 첫 번째 결과는 차원에 대한 정확한 등식이다. Flat morphism에서 $X$의 local dimension은 base의 local dimension과 fiber의 local dimension으로 정확히 분해된다.

::: 명제 17
Locally Noetherian scheme 사이의 flat morphism $\varphi: X \rightarrow Y$와 점 $x\in X$, $y=\varphi(x)$에 대하여

$$\dim \mathcal{O}_{X,x}=\dim \mathcal{O}_{Y,y}+\dim \mathcal{O}_{X_y,x}$$

가 성립한다. 여기에서 $X_y=\varphi^{-1}(y)$는 $y$에서의 fiber이다.
:::
::: 증명
먼저 fiber의 local ring이 무엇인지를 확인한다. $X=\Spec B$, $Y=\Spec A$인 affine 상황으로 localize하고, $\varphi$에 대응하는 ring homomorphism을 $\phi: A \rightarrow B$라 하여 $x=\mathfrak{q}$, $y=\mathfrak{p}=\phi^{-1}(\mathfrak{q})$라 두자. 정의에 의하여 $X_y=\Spec (B\otimes_A\kappa(\mathfrak{p}))$이고, $x$에 대응하는 점에서의 local ring은

$$\mathcal{O}_{X_y,x}=(B\otimes_A\kappa(\mathfrak{p}))_\mathfrak{q}\cong B_\mathfrak{q}\otimes_{A_\mathfrak{p}}\kappa(\mathfrak{p})\cong B_\mathfrak{q}/\mathfrak{p}B_\mathfrak{q}=\mathcal{O}_{X,x}/\mathfrak{m}_y\mathcal{O}_{X,x}$$

이다. 즉 fiber의 local ring은 $\mathcal{O}_{X,x}$를 $\mathcal{O}_{Y,y}$의 maximal ideal로 나눈 것이다.

한편 $X$와 $Y$가 locally Noetherian이므로 $\mathcal{O}_{X,x}$와 $\mathcal{O}_{Y,y}$는 Noetherian local ring이고, [보조정리 2](#lem2)에 의하여 $\mathcal{O}_{Y,y} \rightarrow \mathcal{O}_{X,x}$는 flat local homomorphism이다. 따라서 [\[가환대수학\] §매개계, ⁋정리 9](/ko/math/commutative_algebra/system_of_parameters#thm9)를 적용하면 원하는 등식을 얻는다.
:::

만일 $X$와 $Y$가 field $\mathbb{K}$ 위의 finite type integral scheme인 경우에는 closed point에서 $\dim \mathcal{O}_{X,x}=\dim X$가 성립하므로, $\varphi$의 image에 속하는 closed point $y$에 대하여 [명제 17](#prop17)는 익숙한 형태

$$\dim X_y=\dim X-\dim Y$$

가 된다. 

이 등식은 이 글의 도입에서 본 예시의 non-flatness를 다시 한 번 설명해준다. 해당 예시에서 $X=\Spec \mathbb{K}[t,\x]/(t\x)$의 원점 $x$를 생각하면, [§차원, ⁋명제 8](/ko/math/scheme_theory/dimension#prop8)에 의하여 local ring의 차원은 원점에서 위로 올라가는 irreducible closed subset들의 chain의 maximal length로 주어진다. 문제는 원점을 포함하는 두 irreducible closed subset들 (즉 $t$축과 $\x$축)으로 올라가는 순간, 그것을 포함하는 irreducible closed subset은 존재하지 않으므로 $\dim \mathcal{O}_{X,x}=1$이 된다는 것이다. 반면 $Y=\mathbb{A}_\mathbb{K}^1$의 원점 $y$를 생각하면, 이 점의 $Y$에서의 차원 또한 같은 이유로 $\dim \mathcal{O}_{Y,y}=1$이고, fiber $X_y=\mathbb{A}^1_\mathbb{K}$의 원점에서의 local ring 또한 그러하다. 따라서 $1\neq 1+1$이므로 이 morphism은 flat이 아니다. [명제 16](#prop16)의 언어로 하면 이는 $x$를 지나는 $\x$-축 성분이 $t=0$ 위의 fiber에 통째로 갇혀 base 방향으로 뻗지 못하는 것이 $\dim \mathcal{O}_{X,x}=1\neq 2$인 것으로 나타나는 것으로, 이렇게 한 fiber에 갇힌 성분은 fiber 방향 차원 $1$은 우변에 보태주지만 base 방향이 없어 등식을 깨뜨리게 된다. 

Flat morphism의 또 다른 기하학적 성질은 열린집합을 열린집합으로 보낸다는 것으로, 이는 [정리 13](#thm13)과 [보조정리 14](#lem14)의 결과이다. 

::: 명제 18
Noetherian scheme $Y$와 flat하고 finite type인 morphism $\varphi: X \rightarrow Y$에 대하여 $\varphi$는 open map이다. 즉 임의의 열린집합 $U\subseteq X$에 대하여 $\varphi(U)$는 $Y$의 열린집합이다.
:::
::: 증명
$Y$가 Noetherian이고 $\varphi$가 finite type이므로, $X$를 덮는 각 affine open은 Noetherian ring 위의 finite type algebra의 spectrum이 되어 [\[가환대수학\] §기본 개념들, ⁋정리 12](/ko/math/commutative_algebra/basic_notions#thm12)에 의하여 Noetherian이고, $\varphi$가 quasi-compact이므로 $X$ 또한 quasi-compact이다. 즉 $X$는 [§스킴의 위상구조, ⁋정의 14](/ko/math/scheme_theory/topology_of_schemes#def14)의 의미에서 Noetherian scheme이며, 특히 위상공간으로서 Noetherian이다. 그럼 열린집합 $U\subseteq X$는 [\[위상수학\] §차원, ⁋명제 13](/ko/math/topology/dimension#prop13)에 의하여 다시 Noetherian이므로 [\[위상수학\] §차원, ⁋명제 12](/ko/math/topology/dimension#prop12)에 의하여 quasi-compact이고, open subscheme의 포함사상은 flat이므로 ([예시 4](#ex4)) [명제 3](#prop3)에 의하여 합성 $\varphi\vert_U: U \rightarrow Y$ 또한 flat하고 finite type이다. 그러므로 처음부터 $U=X$인 경우, 즉 $\varphi(X)$가 열린집합임을 보이면 충분하다.

[정리 13](#thm13)에 의하여 $\varphi(X)$는 constructible이다. 또 $y\in \varphi(X)$와 그 generization $y'$이 주어지면, $\varphi(x)=y$인 $x$를 택하고 [명제 16](#prop16)를 적용하여 $\varphi(x')=y'$인 $x'$를 얻으므로 $y'\in \varphi(X)$이다. 즉 $\varphi(X)$는 generization에 대하여 닫혀 있다. 이제 [보조정리 14](#lem14)로부터 $\varphi(X)$가 열린집합임을 얻는다.
:::

## 평탄성의 국소 판정법

마지막으로 flatness를 각 점에서 검사하는 기준을 정리한다. 대수적으로 $\otimes$가 left-exact로부터 멀어지는 정도를 측정하는 도구는 $\otimes$의 left derived functor, 즉 $\Tor$였다. 특히 flatness는 모든 finitely generated ideal $\mathfrak{a}$에 대한 $\Tor_1^A(A/\mathfrak{a}, M)$의 vanishing으로 나타났으므로 ([\[가환대수학\] §평탄성, ⁋명제 1](/ko/math/commutative_algebra/flatness#prop1)), 이를 기하학의 언어로 옮기면 다음을 얻는다.

::: 명제 19
Locally Noetherian scheme $Y$와 locally of finite type인 morphism $\varphi: X \rightarrow Y$, 그리고 점 $x\in X$, $y=\varphi(x)$에 대하여, $\mathcal{O}_{X,x}$가 $\mathcal{O}_{Y,y}$-flat인 것과

$$\Tor_1^{\mathcal{O}_{Y,y}}(\kappa(y), \mathcal{O}_{X,x})=0$$

인 것은 서로 동치이다.
:::
::: 증명
$Y$가 locally Noetherian이므로 $A=\mathcal{O}_{Y,y}$는 Noetherian local ring이고, $\varphi$가 locally of finite type이므로 $X$ 또한 locally Noetherian이어서 $E=\mathcal{O}_{X,x}$도 Noetherian local ring이다. $\varphi$가 유도하는 $A \rightarrow E$는 local homomorphism이므로 $\mathfrak{m}_yE\subseteq \mathfrak{m}_x$를 만족한다. 이제 $M=E$로 두면 $M$은 finitely generated $E$-module이므로 [\[가환대수학\] §평탄성과 국소화, ⁋정리 1](/ko/math/commutative_algebra/local_criterion_for_flatness#thm1)의 가정이 모두 충족되며, 그 결론이 정확히 주장하는 동치이다.
:::

Flatness는 본질적으로 family가 어떻게 <em-ko>움직이는가</em-ko>에 대한 정의이므로, 한 점에서 morphism이 flat하다는 사실만 아는 것은 기하적으로는 큰 의미가 없다. 이를 해결해주는 것이 다음의 정리이다.

::: 정리 20 (Openness of the flat locus)
Locally Noetherian scheme $Y$와 locally of finite type인 morphism $\varphi: X \rightarrow Y$에 대하여, $\mathcal{O}_{X,x}$가 $\mathcal{O}_{Y,\varphi(x)}$-flat인 점 $x\in X$들의 집합은 $X$의 열린집합이다. 
:::

더 일반적으로, 위의 정리는 $Y$에 아무런 Noetherian 조건 없이 $\varphi$가 locally of finite presentation이기만 하여도 성립한다. 약간 무리하면 이 정리의 증명 또한 우리가 알고 있는 범위에서 어느정도 할 수는 있지만, 이 글 전체의 분량을 위해 생략하기로 한다. 

이제 [정리 20](#thm20)에 의하여 [명제 19](#prop19)로 한 점에서 $\Tor$의 소멸을 확인하면 그 점의 열린 근방 $U$ 위에서 $\varphi\vert_U$가 flat morphism이 되므로, [명제 3](#prop3)이나 [명제 18](#prop18)처럼 morphism 전체의 flatness를 요구하는 결과들을 적용할 수 있게 된다. 바꾸어 말하면 flatness가 깨지는 지점들은 닫힌집합을 이루며, 도입에서 살펴본 예시의 원점과 같이 성분들이 부딪히거나 fiber에 갇히는 특수한 곳에 한정된다. 

## 평탄성과 반연속성

앞에서 우리는 이 깨짐이 언제나 커지는 방향으로만 일어난다고 관찰하였는데, 이를 정확히 적으려면 정수값을 갖는 불변량이 공간 위에서 어떻게 변하는지를 재는 언어가 먼저 필요하다.

::: 정의 21
Topological space $X$ 위의 함수 $f: X \rightarrow \mathbb{Z}$가 *upper semicontinuous*라는 것은 임의의 $i\in \mathbb{Z}$에 대하여 집합

$$\{x\in X\mid f(x)\leq i\}$$

가 $X$의 열린집합인 것이다. 마찬가지로 $f$가 *lower semicontinuous<sub>하반연속</sub>*라는 것은 임의의 $i\in \mathbb{Z}$에 대하여 $\{x\in X\mid f(x)\geq i\}$가 $X$의 열린집합인 것이다.
:::

[예시 9](#ex9)와 [예시 10](#ex10), 그리고 도입부의 예시 모두에서 우리는 flatness의 실패를 측정하는 어떠한 양들이, flatness가 깨지는 점으로 가면서 커지기만 할 뿐 그 반대로는 움직이지 않는다는 것을 확인했는데, 이를 엄밀하게 정의한 것이 바로 이 upper semicontinuity이다. 이러한 양의 대표적인 예시로 다음의 명제를 보자.

::: 명제 22
Ring $A$와 finitely generated $A$-module $M$에 대하여 함수 $\mu:\Spec A \rightarrow \mathbb{Z}$를

$$\mu(\mathfrak{p})=\dim_{\kappa(\mathfrak{p})}M\otimes_A\kappa(\mathfrak{p})$$

로 두면 $\mu$는 upper semicontinuous이다.
:::
::: 증명
$M\otimes_A\kappa(\mathfrak{p})=M_\mathfrak{p}/\mathfrak{p}M_\mathfrak{p}$이고 $\mathfrak{p}A_\mathfrak{p}$가 $A_\mathfrak{p}$의 Jacobson radical이므로, [\[가환대수학\] §정수적 확장, ⁋보조정리 8](/ko/math/commutative_algebra/integral_extension#lem8)에 의하여 $\mu(\mathfrak{p})$는 $M_\mathfrak{p}$를 생성하는 원소의 최소 개수와 같다.

$\mathfrak{p}\in \Spec A$를 고정하고 $r=\mu(\mathfrak{p})$라 하자. $M_\mathfrak{p}$를 생성하는 $r$개의 원소에 분모를 곱하면 $M$의 원소 $m_1,\ldots, m_r$으로서 그 image가 $M_\mathfrak{p}$를 생성하는 것들을 얻는다. 이들이 정의하는 $\psi: A^r \rightarrow M$의 cokernel을 $N$이라 하면 $N$은 $M$의 quotient이므로 finitely generated이고, $\psi_\mathfrak{p}$가 surjective이므로 $N_\mathfrak{p}=0$이다.

$N$의 generator $n_1,\ldots, n_k$ 각각에 대하여 $s_jn_j=0$을 만족하는 $s_j\notin \mathfrak{p}$가 존재하며, $\mathfrak{p}$가 prime이므로 $f=s_1\cdots s_k$ 또한 $\mathfrak{p}$에 속하지 않는다. 그럼 $fN=0$이므로 임의의 $\mathfrak{q}\in D(f)$에 대하여 $N_\mathfrak{q}=0$이고, 곧 $m_1,\ldots, m_r$의 image가 $M_\mathfrak{q}$를 생성하여 $\mu(\mathfrak{q})\leq r$이다. 따라서 $\mu(\mathfrak{p})\leq i$인 임의의 $\mathfrak{p}$에 대하여 $\mathfrak{p}\in D(f)\subseteq \{\mu\leq r\}\subseteq \{\mu\leq i\}$이므로, $\{\mu\leq i\}$는 열린집합이다.
:::

$\mu$가 무엇을 재는지는 family의 언어로 옮기면 분명해진다. Morphism $\Spec B \rightarrow \Spec A$가 finite일 때 $M=B$로 두면 $\mu(\mathfrak{p})$는 fiber의 coordinate ring $B\otimes_A\kappa(\mathfrak{p})$를 $\kappa(\mathfrak{p})$ 위의 vector space로 보았을 때의 차원이다. 이 algebra는 Artinian이므로 local ring들의 곱으로 분해되고, 각 인자에서 composition series의 factor가 그 residue field이므로

$$\mu(\mathfrak{p})=\sum_{x\in X_\mathfrak{p}}\length(\mathcal{O}_{X_\mathfrak{p},x})\cdot[\kappa(x):\kappa(\mathfrak{p})]$$

가 성립한다. 곧 $\mu$는 fiber의 length에 residue field의 degree까지 실어서 잰 것이며, 만일 fiber의 점이 모두 $\kappa(\mathfrak{p})$-점이면 length 그 자체가 된다. 즉, [예시 9](#ex9)와 [예시 10](#ex10)에서 살펴본 flatness의 실패가 모두 [명제 22](#prop22)의 사례가 된다. 만일 이를 Hilbert polynomial까지 올리면 이 글의 도입에서 본 예시 또한 이 프레이밍을 통해 설명할 수 있으나, 우리는 아직 scheme 버전의 sheaf cohomology도 다루지 않았으므로 이는 우선 넘어가기로 한다. 

한편 [명제 22](#prop22)의 앞뒤를 뒤집으면 lower semicontinuity가 나온다. $A$가 Noetherian이면 $M$은 finite presentation 

$$A^m\overset{\psi}{\rightarrow}A^n \rightarrow M \rightarrow 0$$

을 가지고 tensor product가 right exact이므로 $\mu(\mathfrak{p})=n-\rank(\psi\otimes\kappa(\mathfrak{p}))$이며, 따라서 [명제 22](#prop22)는 행렬 $\psi$의 rank가 lower semicontinuous라는 것과 같은 내용이다. 곧 $\mu$가 튀어오르는 닫힌집합은 $\psi$의 minor가 소멸하는 자리로 명시되며, 이 minor들이 생성하는 ideal이 [\[가환대수학\] §Fitting 아이디얼, ⁋정의 2](/ko/math/commutative_algebra/fitting_ideals#def2)의 Fitting ideal이다.

---

**참고문헌**

**[Vak]** R. Vakil, *The rising sea: Foundation of algebraic geometry*. Available [online](https://math.stanford.edu/~vakil/216blog/).
