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
published: false
drift_needed: true
---

우리는 scheme morphism $f: X \rightarrow S$를 $S$로 parametrize된 family로 읽기로 하였으며 ([§스킴 사이의 사상, ⁋예시 10](/ko/math/scheme_theory/morphism_of_schemes#ex10)), 이 family의 $s\in S$에서의 member를 fiber $X_s=X\times_S\Spec \kappa(s)$로 정의하였다. ([§올곱, ⁋정의 12](/ko/math/scheme_theory/fiber_products#def12)) 그러나 이 family가 얼마나 좋게 행동할지는 현재로서 우리가 확인할 수 없는 정보이다. 

실제로 이와 같은 family는 나쁘게 행동할 수 있는데, 가령

$$\Spec \mathbb{K}[t,\x]/(t\x) \longrightarrow \mathbb{A}^1_\mathbb{K}=\Spec \mathbb{K}[t]$$

을 보자. 이를 변수 $t$로 parametrize된 family로 생각하면, 고정된 점 $t_0\neq 0$ 위에서는 방정식 $t_0\x=0$이 강제하는 점 $\x=0$ 하나만이 fiber가 되지만, $t=0$ 위에서는 이 조건이 공허해져 fiber가 $\x$ 방향 직선 $\mathbb{A}^1_\mathbb{K}$ 전체가 된다. Fiber의 차원이 $0$에서 $1$로 뛰는 것이다. 

대수적으로 무엇이 잘못되었는지는 이 fiber를 직접 계산해 보면 드러난다. $A=\mathbb{K}[t]$와 $B=\mathbb{K}[t,\x]/(t\x)$라 두면 점 $t_0$에 대응하는 것은 $A$의 maximal ideal $(t-t_0)$이며, 이 때 이 점 $t_0$의 $\Spec A$로의 embedding은 residue field $\kappa(t_0)=A/(t-t_0)$으로의 projection $A\rightarrow \kappa(t_0)$이 유도하는

$$\Spec \kappa(t_0)\rightarrow \Spec A$$

로 주어진다. 즉, 점 $t_0$ 위의 fiber $X_{t_0}$는 이 점을 $f$를 따라 끌어올린 것, 곧 다음의 diagram

![fiber_as_pullback](/assets/images/Math/Scheme_Theory/Flat_Morphisms-1.svg){:style="width:11.64em" class="invert" .align-center}

으로 주어지며 이 경우 [§올곱, ⁋보조정리 2](/ko/math/scheme_theory/fiber_products#lem2)로부터 $X_{t_0}$은 다음의 tensor product

$$B\otimes_A\kappa(t_0)=\mathbb{K}[t,\x]/(t\x, t-t_0)=\mathbb{K}[\x]/(t_0\x)$$

의 spectrum으로 주어진다는 것을 안다. 그럼 여기에서 만일 $t_0\neq 0$이면 $t_0$가 unit이므로 이는 $\mathbb{K}[\x]/(\x)=\mathbb{K}$가 되어 한 점이고, $t_0=0$이면 나누는 것이 없어 $\mathbb{K}[\x]$ 자신이 되어 직선 전체가 되는 것이다.

이제 차원이 뛴 $t_0=0$에서 일어난 일을 더 자세히 살펴보자. Residue field $\kappa(0)$을 얻기 위해 우리는 이를 $\times t: A\rightarrow A$의 cokernel로 생각하며, 실제로 $A$가 integral domain이므로 우리는 다음의 exact sequence

$$0 \longrightarrow A \xrightarrow{\ \times t\ } A \longrightarrow \kappa(0) \longrightarrow 0$$

가 존재하는 것을 안다. 이제 fiber를 얻기 위해 여기에 $-\otimes_AB$를 적용하면 다음의 diagram

![tensoring_kills_injectivity](/assets/images/Math/Scheme_Theory/Flat_Morphisms-2.svg){:style="width:19.88em" class="invert" .align-center}

을 얻는데, tensor product는 right exact이므로 아랫줄에는 왼쪽 끝의 $0$이 남지 않는다. 이 때 $B$에서의 $\times t$의 단사성이 깨지는 부분이 정확하게 $\x\neq 0$이 $\times t$를 통해 $t\x=0$으로 가는 현상이며, 기하적으로는 정확히 이 현상이 $t_0=0$에서 모든 affine line이 살아있는 현상으로 나타났던 것이다. 

Fiber를 취하는 것은 base change이고 affine에서 base change는 tensor product이므로, 일반적인 $X=\Spec B$와 $S=\Spec A$에 대해서도 $s\in S$에서의 fiber는 $\Spec (B\otimes_A\kappa(s))$이다. 더 일반적으로 family를 base를 따라 옮기는 연산은 언제나 functor $-\otimes_AB$이며, 위에서 본 대로 이 functor는 exact일 필요가 없으므로 이 때도 비슷한 문제가 일어난다. 즉, 우리가 family에 우선적으로 바라는 조건은 정확히 $-\otimes_AB$가 exact functor인 것, 즉 flatness이다. 

Flat module의 정의와 그 기본 판정법들은 본질적으로 [\[다중선형대수학\] §사영가군, 단사가군, 평탄가군, ⁋정의 7](/ko/math/multilinear_algebra/various_modules#def7)과 [\[가환대수학\] §평탄성](/ko/math/commutative_algebra/flatness)에서 살펴본 기계들이다. 대수기하학의 많은 부분들이 그러하듯 flatness 또한 이 기계가 어떻게 만들어졌는지보다는, scheme의 언어에서 이것이 어떠한 방식으로 돌아가는지가 중요하다.

> The concept of flatness is a riddle that comes out of algebra, but which technically is the answer to many prayers. - Mumford

## 평탄 사상의 정의

위에서 지적했듯, 우리가 원하는 조건은 가환대수학에서의 flat module을 기하적으로 가져오는 것이다. 

::: 정의 1
Morphism $f: X \rightarrow Y$가 *flat<sub>평탄</sub>*이라는 것은 임의의 $x \in X$에 대하여 local ring $\mathcal{O}_{X,x}$가 $\mathcal{O}_{Y,f(x)}$-module로서 flat한 것이다. 추가로 $f$가 대응하는 위상공간의 사상이 전사이면 *faithfully flat<sub>충실평탄</sub>*이라 부른다.
:::

위의 정의에서 flatness는 각 점에서의 국소적인 조건으로 정의되었지만, affine에서는 이를 대역적인 조건으로 바꿔 쓸 수 있다. 

::: 보조정리 2
Ring homomorphism $\varphi: A \rightarrow B$가 유도하는 morphism $f: \Spec B \rightarrow \Spec A$에 대하여, $f$가 flat인 것과 $B$가 $A$-module로서 flat한 것은 서로 동치이다.
:::
::: 증명
표기의 편의상 $\mathfrak{q}\in \Spec B$가 주어질 때마다 $\mathfrak{p}=\varphi^{-1}(\mathfrak{q})$로 적기로 한다.

우선 $B$가 $A$-flat이라 가정하자. Localization $B \rightarrow B_\mathfrak{q}$는 flat이므로 ([\[가환대수학\] §국소화의 성질들, ⁋명제 2](/ko/math/commutative_algebra/properties_of_localization#prop2)), functor $-\otimes_AB_\mathfrak{q}$는 $-\otimes_AB$와 $-\otimes_BB_\mathfrak{q}$의 합성이 되어 exact이다. 즉 $B_\mathfrak{q}$는 $A$-flat이다. 한편 $B_\mathfrak{q}$는 $A_\mathfrak{p}$-algebra이므로 $A_\mathfrak{p}\otimes_AB_\mathfrak{q}\cong B_\mathfrak{q}$이고, 따라서 임의의 $A_\mathfrak{p}$-module $M$에 대하여

$$M\otimes_AB_\mathfrak{q}\cong M\otimes_{A_\mathfrak{p}}(A_\mathfrak{p}\otimes_AB_\mathfrak{q})\cong M\otimes_{A_\mathfrak{p}}B_\mathfrak{q}$$

가 성립한다. 이제 $A_\mathfrak{p}$-module의 단사사상 $M'\hookrightarrow M$은 $A$-module의 단사사상이기도 하므로 $M'\otimes_AB_\mathfrak{q} \rightarrow M\otimes_AB_\mathfrak{q}$가 단사이고, 위의 isomorphism에 의하여 $M'\otimes_{A_\mathfrak{p}}B_\mathfrak{q} \rightarrow M\otimes_{A_\mathfrak{p}}B_\mathfrak{q}$ 또한 단사이다. 즉 $\mathcal{O}_{\Spec B,\mathfrak{q}}=B_\mathfrak{q}$는 $\mathcal{O}_{\Spec A,\mathfrak{p}}=A_\mathfrak{p}$-flat이며, $\mathfrak{q}$가 임의였으므로 $f$는 flat이다.

역으로 $f$가 flat이라 하자. 각 $\mathfrak{q}$에 대하여 $B_\mathfrak{q}$는 $A_\mathfrak{p}$-flat이고 $A \rightarrow A_\mathfrak{p}$는 flat이므로, 위와 같은 논증에 의하여 $B_\mathfrak{q}$는 $A$-flat이다. 이제 $A$-module의 단사사상 $M'\hookrightarrow M$을 택하고

$$K=\ker(M'\otimes_AB \longrightarrow M\otimes_AB)$$

라 두자. Localization이 exact functor이므로 $B$의 임의의 maximal ideal $\mathfrak{q}$에 대하여 $K_\mathfrak{q}=\ker(M'\otimes_AB_\mathfrak{q} \rightarrow M\otimes_AB_\mathfrak{q})=0$이다. 그런데 $0\neq \xi\in K$가 존재한다면 $\ann(\xi)$는 $B$의 proper ideal이므로 어떤 maximal ideal $\mathfrak{q}$에 포함되고, $K_\mathfrak{q}=0$으로부터 $s\xi=0$인 $s\in B\setminus \mathfrak{q}$가 존재하여 $\ann(\xi)\not\subseteq \mathfrak{q}$가 되어 모순이다. 따라서 $K=0$이고 $B$는 $A$-flat이다.
:::

이 보조정리에 의해 flatness를 확인할 때는 거의 언제나 가환대수학의 도구를 사용할 수 있다. 가령 flatness가 base change와 합성에 대해 안정적이라는 것은 이제 순수하게 대수적인 계산이다.

::: 명제 3
Flat morphism은 base change와 합성에 대하여 닫혀 있다. 즉 다음이 성립한다.

1. $f: X \rightarrow Y$가 flat이고 $Z \rightarrow Y$가 임의의 사상이면, base change $X \times_Y Z \rightarrow Z$는 flat이다. ([§올곱](/ko/math/scheme_theory/fiber_products))
2. $f: X \rightarrow Y$와 $g: Y \rightarrow Z$가 모두 flat이면, 합성 $g \circ f: X \rightarrow Z$도 flat이다.
:::
::: 증명
[보조정리 2](#lem2)에 의하여 둘 다 affine case로 환원된다.

(1) $A \rightarrow B$가 flat일 때 임의의 $A$-algebra $C$에 대하여 $C \rightarrow B\otimes_AC$가 flat임을 보이면 된다. 임의의 $C$-module $M$에 대하여

$$(B \otimes_A C) \otimes_C M \cong B \otimes_A (C \otimes_C M) \cong B \otimes_A M$$

이므로, $C$-module의 injection $M' \hookrightarrow M$에 $-\otimes_C (B \otimes_A C)$를 적용한 것은 $B \otimes_A M' \rightarrow B \otimes_A M$과 같다. $B$가 $A$-flat이므로 이 사상은 단사이고, 따라서 $B \otimes_A C$는 $C$-flat이다.

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

이를 정확히 적기 위해 용어를 하나 마련해둔다. Morphism $g: Z \rightarrow Y$가 *dominant*라는 것은 그 상이 $Y$에서 조밀한 것, 곧 $\overline{g(Z)}=Y$인 것이다. Variety 사이의 rational map에 대하여 같은 조건을 이미 다룬 바 있다. ([\[대수다양체\] §유리사상, ⁋정의 8](/ko/math/algebraic_varieties/rational_maps#def8)) 아래에서 $X$의 irreducible component $Z$가 base를 dominate한다는 것은, $Z$에 reduced closed subscheme 구조를 준 뒤 포함사상과 $f$를 합성한 것이 dominant라는 뜻이다.

::: 따름정리 6
Noetherian $\mathbb{K}[t]$-algebra $B$에 대하여 $X=\Spec B$가 reduced라 하자. 그럼 $X \rightarrow \mathbb{A}^1_\mathbb{K}$가 flat인 것과, $X$의 모든 irreducible component가 $\mathbb{A}^1_\mathbb{K}$를 dominate하는 것은 서로 동치이다.
:::
::: 증명
[명제 5](#prop5)에 의하여 flatness는 $\mathbb{K}[t]$의 $0$이 아닌 모든 원소가 $B$에서 zerodivisor가 아닌 것과 동치이다.

$B$가 noetherian이므로 $B$의 zerodivisor 전체는 $\Ass B$의 원소들의 합집합이다. ([\[가환대수학\] §동반소아이디얼, ⁋정리 7](/ko/math/commutative_algebra/associated_primes#thm7)) 여기에 $B$가 reduced라는 가정을 더하면 이 합집합은 정확히 $B$의 minimal prime ideal $\mathfrak{p}_1,\ldots, \mathfrak{p}_k$들의 합집합이 된다. 실제로 minimal prime들이 언제나 $\Ass B$에 속한다는 것이 이 정리의 첫째 결과이고, 역으로 $B$가 reduced이면

$$(0)=\mathfrak{N}(B)=\bigcap_{i=1}^k \mathfrak{p}_i$$

이므로, $ab=0$이고 $b\neq 0$인 zerodivisor $a$에 대하여 $b\not\in \mathfrak{p}_i$인 $i$를 택하면 $ab=0\in \mathfrak{p}_i$로부터 $a\in \mathfrak{p}_i$를 얻기 때문이다.

한편 $\mathfrak{p}_i$들은 정확히 $X$의 irreducible component $Z_i=V(\mathfrak{p}_i)$들의 generic point에 대응한다. 이제 $0\neq f\in \mathbb{K}[t]$가 $B$에서 zerodivisor인 것은 어떤 $i$에 대하여 $f\in \mathfrak{p}_i$인 것, 즉 $f$가 $Z_i$ 위에서 항등적으로 소멸하는 것과 같다. 그런데 $f$가 $Z_i$ 위에서 소멸한다는 것은 $Z_i$의 상이 진부분 닫힌집합 $Z(f)\subsetneq \mathbb{A}^1_\mathbb{K}$에 포함된다는 것, 즉 $Z_i$가 $\mathbb{A}^1_\mathbb{K}$를 dominate하지 않는다는 것과 같다. 역으로 $Z_i$가 dominate하지 않으면 그 상의 closure가 진부분 닫힌집합이므로 그 위에서 소멸하는 $0$이 아닌 $f\in \mathbb{K}[t]$가 존재하고, 이 $f$는 $\mathfrak{p}_i$에 속하여 zerodivisor가 된다. 이상에서 결론을 얻는다.
:::

도입에서 본 $X=\Spec \mathbb{K}[t,\x]/(t\x)$는 reduced이고 그 성분 $\{t=0\}$이 base를 dominate하지 않으므로, [따름정리 6](#cor6)이 곧바로 non-flatness를 준다. 

다만 주의할 것은, flatness가 family의 변화 자체를 막는 것이 아니라, 그 family가 무너지는 것만 막는다는 것이다. 가령, flat family의 어떠한 fiber는 singular할 수 있다. 

::: 예시 7
이번 예시에서 우리는 curve들의 family 가운데 특정한 fiber가 singular해지는 경우를 살펴본다. Curve의 singularity 중 특별한 위치를 차지하고 있던 두 예시가 cusp singularity와 nodal singularity였음을 기억하자. ([\[대수다양체\] §접공간과 매끄러움, ⁋예시 7](/ko/math/algebraic_varieties/tangent_spaces_and_smoothness#ex7))

우선 curve들의 family

$$\Spec \mathbb{K}[t, \x, \y]/(\y^2 - \x^3 - t) \longrightarrow \mathbb{A}^1_\mathbb{K}$$

를 생각하자. 관계식이 $t = \y^2 - \x^3$을 주므로 coordinate ring은 $\mathbb{K}[\x,\y]$와 isomorphic이며, 이 isomorphism 아래에서 $\mathbb{K}[t]$의 action은 $t \mapsto \y^2-\x^3$으로 주어진다. Coordinate ring이 integral domain이므로 $\mathbb{K}[t]$의 $0$이 아닌 원소는 zerodivisor일 수 없고, [명제 5](#prop5)에 의하여 이 사상은 flat이다. 그럼에도 $t=0$ 위의 fiber는 cusp singularity를 갖는 $\y^2=\x^3$이다.

또 다른 curve들의 family

$$\Spec \mathbb{K}[t, \x, \y]/(\x\y - t) \longrightarrow \mathbb{A}^1_\mathbb{K}$$

도 마찬가지이다. $t=\x\y$로 두면 coordinate ring은 integral domain $\mathbb{K}[\x,\y]$와 isomorphic하므로 flat이며, $t\neq 0$ 위의 fiber는 smooth한 쌍곡선 $\x\y=t$이지만 $t=0$ 위의 fiber는 두 직선이 만나 nodal singularity를 갖는 $\x\y=0$이다.

요컨대 flatness가 통제하는 것은 fiber가 특이해지는지의 여부가 아니라, fiber들이 같은 크기로 남는지의 여부이다.
:::

지금까지 본 family에서 fiber는 모두 $\mathbb{A}^2$ 안의 곡선이었고, 따라서 무한대에 놓인 점들이 빠져 있었다. 이들까지 함께 보려면 곡선을 $\mathbb{P}^2$ 안에서 자르는 것이 자연스럽다. ([§사영스킴](/ko/math/scheme_theory/projective_schemes)) 이 때 $X$는 더 이상 affine이 아니므로 flatness는 affine chart마다 확인하게 된다.

::: 예시 8
$\x,\y,\z$의 차수로 grading을 준 graded ring $R=\mathbb{K}[t][\x,\y,\z]$를 생각하자. 여기에서 $t$는 차수 $0$이며, 따라서 base ring은 $R_0=\mathbb{K}[t]$이다. Chart를 계산하면 $R_{(\x)}=\mathbb{K}[t][\y/\x,\z/\x]$이므로 $D_+(\x)$는 $\mathbb{A}^2_{\mathbb{K}[t]}$이고, $t$가 차수 $0$이라 localization에서 살아남는다. 세 chart를 붙이면 $\Proj R$은 $\mathbb{P}^2\times_\mathbb{K}\mathbb{A}^1_\mathbb{K}$가 되며, 모든 $f$에 대하여 $R_0\subseteq R_{(f)}$이므로 이들이 붙어 structure morphism $\Proj R \rightarrow \mathbb{A}^1_\mathbb{K}$를 준다.

이제 $\x\z-t\y^2$을 보면 $\x\z$와 $t\y^2$이 모두 $\x,\y,\z$에 대하여 차수 $2$이므로 이는 homogeneous element이다. 여기에서도 $t$의 차수가 $0$인 것이 쓰인다. 따라서 $(\x\z-t\y^2)$는 homogeneous ideal이고, [§사영공간의 닫힌 부분스킴, ⁋명제 1](/ko/math/scheme_theory/closed_subschemes_of_projective_spaces#prop1)에 의하여

$$X=\Proj R/(\x\z-t\y^2)$$

은 $\mathbb{P}^2\times_\mathbb{K}\mathbb{A}^1_\mathbb{K}$의 닫힌 부분스킴으로서 $Z_+(\x\z-t\y^2)$이다. 즉 $X$는 $\mathbb{P}^2$ 안에서 방정식 $\x\z=t\y^2$이 자르는 곡선들의 family이며, 위의 structure morphism이 이를 $\mathbb{A}^1_\mathbb{K}$ 위의 family로 만든다.

이 사상이 flat인 것은 세 개의 affine chart에서 확인된다. $D_+(\y)$ 위에서 $u=\x/\y$, $v=\z/\y$로 두면 관계식을 $\y^2$으로 나누어 $uv=t$를 얻으므로 coordinate ring은 $\mathbb{K}[t][u,v]/(uv-t)$이며, 이는 $t=uv$를 통해 integral domain $\mathbb{K}[u,v]$와 isomorphic이다. 따라서 [명제 5](#prop5)에 의하여 flat이다. $D_+(\x)$ 위에서 $w=\y/\x$, $s=\z/\x$로 두면 관계식을 $\x^2$으로 나누어 $s=tw^2$을 얻으므로 coordinate ring은 $\mathbb{K}[t][w]$이고, 이는 free $\mathbb{K}[t]$-module이므로 flat이다. $D_+(\z)$의 경우도 symmetric이다. 이 셋이 $X$를 덮으므로 $X \rightarrow \mathbb{A}^1_\mathbb{K}$는 flat이다.

Fiber를 보면, $t=a\neq 0$ 위에서는 $\mathbb{P}^2$의 원뿔곡선 $\x\z=a\y^2$이 되어 smooth하고 $\mathbb{P}^1$과 isomorphic이다. 반면 $t=0$ 위에서는 $\x\z=0$, 즉 두 직선 $\{\x=0\}$과 $\{\z=0\}$이 점 $[0:1:0]$에서 만나는 곡선이 된다. 즉 이것은 smooth한 원뿔곡선이 두 직선으로 퇴화하는 상수 아닌 곡선들의 family이며, 그럼에도 모든 fiber가 $1$차원으로 남는다.
:::

## 제네릭 평탄성

이제부터 flat morphism의 기하학적 성질들을 살펴볼 것인데, 그 증명들은 예외 없이 두 가지 준비물 위에 놓인다. 하나는 flatness가 base의 조밀한 열린집합 위에서는 언제나 성립한다는 사실이고, 다른 하나는 finite type 사상의 상이 언제나 constructible이라는 Chevalley의 정리이다. 그런데 이 둘은 모두 다음의 대수적 정리 하나에서 나오므로, 기하로 넘어가기 전에 이를 먼저 마련해둔다.

::: 정리 9 (Grothendieck의 generic freeness)
Noetherian integral domain $A$와 finite type $A$-algebra $B$, 그리고 finitely generated $B$-module $M$이 주어졌다 하자. 그럼 $0$이 아닌 $a\in A$가 존재하여 $M_a$가 free $A_a$-module이 된다.
:::
::: 증명
$B$는 Noetherian integral domain $A$ 위의 finite type 대수이므로 [\[가환대수학\] §기본 개념들, ⁋정리 12](/ko/math/commutative_algebra/basic_notions#thm12)에 의하여 Noetherian ring이다.

**Dévissage.** [\[가환대수학\] §동반소아이디얼, ⁋보조정리 6](/ko/math/commutative_algebra/associated_primes#lem6)을 $B$와 $M$에 적용하면 filtration

$$0=M_0\subseteq M_1\subseteq\cdots\subseteq M_n=M,\qquad M_i/M_{i-1}\cong B/\mathfrak{q}_i$$

를 얻는다. 각 $B/\mathfrak{q}_i$에 대하여 결론이 성립한다 하고 그 원소들의 곱을 $a$라 하면, exact sequence

$$0 \longrightarrow (M_{i-1})_a \longrightarrow (M_i)_a \longrightarrow (B/\mathfrak{q}_i)_a \longrightarrow 0$$

의 오른쪽 항이 free module이므로 이 exact sequence는 split하고, $i$에 대한 귀납법으로 $(M_i)_a$가 모두 free $A_a$-module이 된다. 따라서 $M=B/\mathfrak{q}$인 경우, 즉 $B$를 $B/\mathfrak{q}$로 바꾸어 $B$가 integral domain이고 $M=B$인 경우만 보이면 충분하다.

**환원.** $\varphi: A \rightarrow B$의 kernel이 $0$이 아니라면 $0\neq a\in \ker \varphi$를 택하자. $B_a=B\otimes_AA_a$에서 $\varphi(a)=0$이면서 $a$가 unit이므로 $B_a=0$이고, 이는 rank $0$의 free module이다. 따라서 $A\subseteq B$라 가정해도 좋다.

**귀납.** $K=\Frac(A)$라 하자. $B\otimes_AK$는 $A\setminus\{0\}$에서의 $B$의 localization이므로 $0$이 아닌 integral domain이며, $K$ 위의 finite type 대수이다. $d=\dim (B\otimes_AK)$에 대한 귀납법을 쓴다.

[§차원, ⁋정리 9](/ko/math/scheme_theory/dimension#thm9)에 의하여 algebraically independent한 원소들 $y_1,\ldots, y_d\in B\otimes_AK$가 존재하여 $B\otimes_AK$가 $K[y_1,\ldots,y_d]$ 위의 finite module이다. 각 $y_i$에 $A$의 $0$이 아닌 원소를 곱해도 대수적 독립성과 유한성은 유지되므로, 처음부터 $y_i\in B$라 가정해도 좋다.

$B$를 $A$-algebra로서 생성하는 원소를 $b_1,\ldots, b_m$이라 하면 각 $b_j$는 $K[y_1,\ldots,y_d]$ 위에서 integral하다. 이 정수 방정식들에 등장하는 계수는 유한개이므로, 그 분모를 모두 없애는 $0\neq a_0\in A$를 택할 수 있다. 그럼 각 $b_j$는

$$C=A_{a_0}[y_1,\ldots, y_d]$$

위에서 integral하고, 따라서 $B_{a_0}$는 finite $C$-module이다. 여기에서 $y_i$들이 $K$ 위에서 대수적으로 독립이므로 $C$는 $A_{a_0}$ 위의 polynomial ring이며, 특히 free $A_{a_0}$-module이다.

이제 dévissage를 Noetherian ring $C$와 finite $C$-module $B_{a_0}$에 다시 적용하면, quotient가 $C/\mathfrak{p}$ 꼴인 finite filtration을 얻는다. 따라서 각 $C/\mathfrak{p}$에 대하여 결론을 보이면 충분하다.

$\mathfrak{p}=0$이면 $C$ 자신이 free $A_{a_0}$-module이므로 볼 것이 없다. $\mathfrak{p}\neq 0$이라 하자. 만일 $\mathfrak{p}\cap A_{a_0}\neq 0$이면 그 안의 $0$이 아닌 원소 $a_1$을 택했을 때 $(C/\mathfrak{p})_{a_1}=0$이므로 결론이 성립한다. 그렇지 않다면 $S=A_{a_0}\setminus\{0\}$에 대하여 $S^{-1}C=K[y_1,\ldots,y_d]$이고 $\mathfrak{p}\cap S=\emptyset$이므로, $\mathfrak{p}K[y_1,\ldots,y_d]$는 $K[y_1,\ldots,y_d]$의 $0$이 아닌 prime ideal이다. 이제

$$(C/\mathfrak{p})\otimes_{A_{a_0}}K=K[y_1,\ldots,y_d]/\mathfrak{p}K[y_1,\ldots,y_d]$$

인데, $0\neq g\in \mathfrak{p}K[y_1,\ldots,y_d]$를 택하면 이 quotient ring에서 $y_1,\ldots,y_d$의 image들은 $g=0$이라는 대수적 관계를 만족하므로 대수적으로 독립일 수 없다. 그런데 이 quotient ring은 이들 image로 생성되는 $K$-algebra이므로 그 field of fractions의 초월차수는 $d$보다 작고, [§차원, ⁋명제 10](/ko/math/scheme_theory/dimension#prop10)에 의하여

$$\dim\big((C/\mathfrak{p})\otimes_{A_{a_0}}K\big)<d$$

이다. $A_{a_0}$ 또한 $K$를 field of fractions로 갖는 Noetherian integral domain이고 $C/\mathfrak{p}$는 그 위의 finite type integral domain이므로, 귀납가정을 적용하면 $0\neq a_\mathfrak{p}\in A_{a_0}$가 존재하여 $(C/\mathfrak{p})_{a_\mathfrak{p}}$가 free $(A_{a_0})_{a_\mathfrak{p}}$-module이다. 필요하다면 $a_0$의 거듭제곱을 곱하여 $a_\mathfrak{p}\in A$로 볼 수 있다.

$d=0$인 경우에는 $C=A_{a_0}$이므로 위의 dévissage가 주는 quotient는 $A_{a_0}/\mathfrak{p}$ 꼴이고, $\mathfrak{p}=0$이면 free module, $\mathfrak{p}\neq 0$이면 $\mathfrak{p}$의 $0$이 아닌 원소를 뒤집어 $0$으로 만들 수 있으므로 귀납의 기저가 된다.

Filtration에 등장하는 유한개의 $\mathfrak{p}$들에 대한 $a_\mathfrak{p}$와 $a_0$의 곱을 $a$로 두면 $B_a=(B_{a_0})_a$는 free $A_a$-module이다.
:::

::: 명제 10 (Generic flatness)
Noetherian integral scheme $Y$와 finite type morphism $f: X \rightarrow Y$가 주어졌다 하자. 그럼 $Y$의 조밀한 열린집합 $U$가 존재하여 $f\rvert_{f^{-1}(U)}: f^{-1}(U) \rightarrow U$가 flat이다.
:::
::: 증명
$Y$가 irreducible이므로 $Y$의 공집합이 아닌 열린집합은 모두 조밀하다. 따라서 $Y$의 affine open $V=\Spec A$를 하나 고정하고 그 안에서 $U$를 찾으면 충분하다. $Y$가 Noetherian integral이므로 $A$는 Noetherian integral domain이다.

$f$가 finite type이므로 $f^{-1}(V)$는 유한개의 affine open $\Spec B_1,\ldots, \Spec B_k$로 덮이고, 각 $B_i$는 finite type $A$-algebra이다. [정리 9](#thm9)를 $M=B_i$에 적용하면 $0\neq a_i\in A$가 존재하여 $(B_i)_{a_i}$가 free $A_{a_i}$-module이다. $a=a_1\cdots a_k$로 두면 각 $(B_i)_a$는 free module $(B_i)_{a_i}$의 localization이므로 여전히 free $A_a$-module이고, free module은 flat하므로 [보조정리 2](#lem2)에 의하여

$$\Spec (B_i)_a \longrightarrow \Spec A_a=D(a)$$

는 flat이다. flatness는 $X$ 위에서 국소적인 조건이고 $\Spec (B_i)_a$들이 $f^{-1}(D(a))$를 덮으므로 $f^{-1}(D(a)) \rightarrow D(a)$는 flat이다. $A$가 integral domain이고 $a\neq 0$이므로 $D(a)$는 공집합이 아니며, 따라서 $U=D(a)$가 원하는 열린집합이다.
:::

## Chevalley 정리

두 번째 준비물은 상의 모양에 대한 것이다. 일반적인 사상의 상은 열린집합도 닫힌집합도 아니지만, finite type 사상의 상은 언제나 다음의 의미에서 좋은 집합이다.

::: 정의 11
위상공간 $T$의 부분집합이 *constructible<sub>구성가능</sub>*이라는 것은 그것이 유한개의 locally closed subset들의 합집합으로 쓰일 수 있는 것이다. ([\[위상수학\] §몫공간, ⁋정의 1](/ko/math/topology/quotient_spaces#def1))
:::

Locally closed subset은 열린집합과 닫힌집합의 교집합 $U\cap Z$로 쓸 수 있으므로 ([\[위상수학\] §몫공간, ⁋명제 2](/ko/math/topology/quotient_spaces#prop2)), constructible subset들의 모임은 유한합집합, 유한교집합, 여집합에 대하여 닫혀 있다. 유한합집합은 정의에 의하여 자명하고, 두 locally closed subset의 교집합 $(U_1\cap Z_1)\cap (U_2\cap Z_2)=(U_1\cap U_2)\cap (Z_1\cap Z_2)$이 다시 locally closed이므로 교집합에 대한 닫힘은 분배법칙으로부터 나오며, locally closed subset $U\cap Z$의 여집합은 $(T\setminus U)\cup (T\setminus Z)$로 두 locally closed subset의 합집합이므로 여집합에 대해서도 닫혀 있다.

::: 정리 12 (Chevalley)
Noetherian scheme $Y$와 finite type morphism $f: X \rightarrow Y$에 대하여, $f(X)$는 $Y$의 constructible subset이다.
:::
::: 증명
**Affine으로의 환원.** $Y$가 Noetherian이므로 유한개의 affine open $V_j$로 덮이고, $f$가 finite type이므로 각 $f^{-1}(V_j)$ 또한 유한개의 affine open으로 덮인다. 따라서 $f(X)$는 유한개의 $\Spec B \rightarrow \Spec A$ 꼴 사상의 상들의 합집합이다. 열린집합 $V_j$의 constructible subset은 $Y$의 constructible subset이고 constructible subset들의 유한합집합은 constructible이므로, 처음부터 $Y=\Spec A$, $X=\Spec B$이고 $B$가 finite type $A$-algebra인 경우만 보이면 충분하다.

**Noetherian 귀납법.** 이제 $Y=\Spec A$의 닫힌 부분집합 $Z$에 대하여, "$Z$ 위의 임의의 finite type morphism의 상은 $Z$의 constructible subset이다"라는 명제를 $P(Z)$라 하자. $A$가 Noetherian이므로 $Y$의 닫힌 부분집합들의 모임은 descending chain condition을 만족하고, 따라서 Noetherian 귀납법을 쓸 수 있다. 즉 $Y$의 모든 진부분 닫힌집합 $Z\subsetneq Y$에 대하여 $P(Z)$가 성립한다고 가정하고 $P(Y)$를 보이면 된다. 또 $Z$의 constructible subset은 $Z$가 닫힌집합이므로 $Y$의 constructible subset이기도 하여, 결론을 $Y$ 안에서 읽어도 좋다.

**Reduced로의 환원.** $\mathfrak{N}=\mathfrak{N}(A)$를 $A$의 nilradical이라 하면 $\mathfrak{N}B$는 $B$의 nilpotent ideal이므로 $\Spec B/\mathfrak{N}B$와 $\Spec B$는 같은 위상공간이고, $\Spec A/\mathfrak{N}$과 $\Spec A$도 그러하다. 따라서 $A$를 $A/\mathfrak{N}$으로, $B$를 $B/\mathfrak{N}B$로 바꾸어도 $f(X)$는 바뀌지 않으므로 $A$가 reduced라 가정해도 좋다.

**integral domain으로의 환원.** $A$의 minimal prime을 $\mathfrak{p}_1,\ldots, \mathfrak{p}_k$라 하면 $A$가 reduced이므로 $Y=\bigcup_j V(\mathfrak{p}_j)$이다. 만일 $k\geq 2$라면 각 $V(\mathfrak{p}_j)$는 $Y$의 진부분 닫힌집합이고

$$f(X)=\bigcup_{j=1}^k f\big(X\times_Y V(\mathfrak{p}_j)\big)$$

인데, 각 base change $X\times_YV(\mathfrak{p}_j) \rightarrow V(\mathfrak{p}_j)$는 여전히 finite type이므로 귀납가정 $P(V(\mathfrak{p}_j))$에 의하여 각 항이 constructible이고 따라서 $f(X)$도 constructible이다. 그러므로 $k=1$, 즉 $A$가 integral domain인 경우만 남는다.

**integral domain인 경우.** $B=0$이면 $f(X)=\emptyset$이므로 자명하다. $B\neq 0$이라 하고 [정리 9](#thm9)를 $M=B$에 적용하면 $0\neq a\in A$가 존재하여 $B_a$가 free $A_a$-module이다. $a$가 unit이면 $D(a)=Y$이므로 $a$를 unit이 아닌 것으로 택했다고 가정해도 좋고 (unit이라면 아래 논증에서 $V(a)=\emptyset$이 되어 결론이 더 간단해진다), 이 경우 $A$가 integral domain이므로 $V(a)$는 $Y$의 진부분 닫힌집합이다.

$B_a=0$인 경우, 이는 $\varphi(a)$가 $B$에서 nilpotent라는 뜻이므로 $\varphi(a)$는 $B$의 모든 prime ideal에 속한다. 따라서 $f(X)\subseteq V(a)$이고, $f(X)$는 base change $X\times_YV(a) \rightarrow V(a)$의 상과 같으므로 귀납가정 $P(V(a))$에 의하여 constructible이다.

$B_a\neq 0$인 경우, $B_a$는 $0$이 아닌 free $A_a$-module이다. 임의의 $\mathfrak{p}\in D(a)$에 대하여

$$B_a\otimes_{A_a}\kappa(\mathfrak{p})\cong \kappa(\mathfrak{p})^{(r)}\neq 0$$

이므로 ($r\geq 1$은 $B_a$의 rank이다) $\mathfrak{p}$ 위의 fiber는 공집합이 아니고, 따라서 $D(a)\subseteq f(X)$이다. 그럼

$$f(X)=D(a)\cup \big(f(X)\cap V(a)\big)$$

이고, $f(X)\cap V(a)$는 base change $X\times_YV(a) \rightarrow V(a)$의 상이므로 귀납가정 $P(V(a))$에 의하여 constructible이다. $D(a)$는 열린집합이므로 constructible이고, 따라서 $f(X)$는 constructible이다.
:::

Constructible한 집합이 언제 열린집합이 되는지도 함께 정리해둔다. 이것이 flatness와 만나는 지점은 다음 절에서 드러난다.

::: 보조정리 13
Noetherian scheme $Y$의 constructible subset $E$가 generization에 대하여 닫혀 있다면, 즉 $y\in E$이고 $y\in \overline{\{y'\}}$일 때마다 $y'\in E$라면, $E$는 $Y$의 열린집합이다.
:::
::: 증명
여집합 $F=Y\setminus E$는 constructible이며 specialization에 대하여 닫혀 있다. $F$가 닫힌집합임을 보이면 된다. $F=\emptyset$인 경우는 자명하므로 $F\neq \emptyset$이라 하고, $Z=\overline{F}$의 irreducible component들을 $Z_1,\ldots, Z_k$라 하자. $Y$가 Noetherian이므로 이들은 유한개이다.

먼저 각 $j$에 대하여 $\overline{F\cap Z_j}=Z_j$임을 보인다. 만일 $W=\overline{F\cap Z_j}\subsetneq Z_j$라면 $F\subseteq W\cup \bigcup_{i\neq j}Z_i$이고 우변이 닫힌집합이므로 $Z=\overline{F}\subseteq W\cup \bigcup_{i\neq j}Z_i$인데, 이는 $Z_j$가 $Z$의 irreducible component라는 것에 모순이다.

이제 $F$를 locally closed subset들의 유한합집합 $F=\bigcup_{i=1}^n (U_i\cap C_i)$로 쓰자. $Z_j$가 irreducible이고

$$Z_j=\overline{F\cap Z_j}=\bigcup_{i=1}^n \overline{U_i\cap C_i\cap Z_j}$$

이므로, 적당한 $i$에 대하여 $\overline{U_i\cap C_i\cap Z_j}=Z_j$이다. 그럼 $U_i\cap C_i\cap Z_j\subseteq C_i$이고 $C_i$가 닫힌집합이므로 $Z_j\subseteq C_i$이며, 따라서

$$U_i\cap Z_j\subseteq U_i\cap C_i\subseteq F$$

이다. 한편 $U_i\cap Z_j$는 $Z_j$의 열린 부분집합이며 그 closure가 $Z_j$이므로 공집합이 아니다. $Z_j$는 $Y$의 irreducible closed subset이므로 generic point $z_j$를 가지며, $Z_j$의 공집합이 아닌 열린 부분집합은 언제나 $z_j$를 포함하므로 $z_j\in F$이다.

$F$가 specialization에 대하여 닫혀 있으므로 $Z_j=\overline{\{z_j\}}\subseteq F$이고, 이것이 모든 $j$에 대하여 성립하므로 $Z=\bigcup_j Z_j\subseteq F$이다. $F\subseteq Z$는 자명하므로 $F=Z$는 닫힌집합이다.
:::

## 평탄 사상의 기하학적 성질

준비를 마쳤으므로 이제 flatness가 기하학적으로 무엇을 뜻하는지를 본다. flatness의 내용은 fiber들이 서로 이어지는 방식을 통제한다는 데에 있으며, 그 출발점은 flat한 국소사상이 자동으로 faithfully flat이 된다는 다음 관찰이다.

::: 보조정리 14
local ring 사이의 국소사상 $\varphi: (A,\mathfrak{m}) \rightarrow (B,\mathfrak{n})$이 $B$를 flat $A$-module로 만든다 하자. 그럼 $0$이 아닌 임의의 $A$-module $M$에 대하여 $M\otimes_AB\neq 0$이며, 특히 $\Spec B \rightarrow \Spec A$는 전사이다.
:::
::: 증명
$0\neq \xi\in M$을 택하자. $\ann(\xi)$는 $A$의 진 ideal이므로 $\ann(\xi)\subseteq \mathfrak{m}$이고, $A/\ann(\xi)\cong A\xi$는 $M$의 submodule이다. 여기에 flat한 functor $-\otimes_AB$를 적용하면 단사사상

$$B/\ann(\xi)B\cong (A/\ann(\xi))\otimes_AB\hookrightarrow M\otimes_AB$$

를 얻는다. 그런데 $\varphi$가 국소사상이므로 $\ann(\xi)B\subseteq \mathfrak{m}B\subseteq \mathfrak{n}\subsetneq B$이고, 따라서 $B/\ann(\xi)B\neq 0$이다. 즉 $M\otimes_AB\neq 0$이다.

이제 임의의 $\mathfrak{p}\in \Spec A$에 대하여 $M=\kappa(\mathfrak{p})$로 두면 $\kappa(\mathfrak{p})\neq 0$이므로 fiber ring

$$B\otimes_A\kappa(\mathfrak{p})$$

은 $0$이 아닌 ring이고, 따라서 prime ideal을 갖는다. 그러한 prime ideal에 대응하는 $\Spec B$의 점은 $\mathfrak{p}$ 위에 놓이므로 $\Spec B \rightarrow \Spec A$는 전사이다.
:::

이로부터 flat morphism이 generization을 들어올린다는 것, 곧 going-down 성질을 얻는다. 같은 결과가 가환대수학의 언어로 이미 서술된 바 있다. ([\[가환대수학\] §매개계, ⁋보조정리 8](/ko/math/commutative_algebra/system_of_parameters#lem8))

::: 명제 15
Flat morphism $f: X \rightarrow Y$와 점 $x \in X$가 주어졌다 하고, $y=f(x)$의 generization $y'$, 즉 $y \in \overline{\{y'\}}$인 점 $y'$가 주어졌다 하자. 그럼 $x$의 generization $x'$가 존재하여 $f(x')=y'$이다.
:::
::: 증명
$y$의 affine open neighborhood $V=\Spec A$를 택하고, 그 다음 $f^{-1}(V)$ 안에서 $x$의 affine open neighborhood $U=\Spec B$를 택하자. $y'$이 $y$의 generization이므로 $y'\in V$이다. 따라서 $X=\Spec B$, $Y=\Spec A$이고 $x=\mathfrak{q}$, $y=\mathfrak{p}=\varphi^{-1}(\mathfrak{q})$, $y'=\mathfrak{p}'\subseteq \mathfrak{p}$인 경우만 보이면 충분하다.

[보조정리 2](#lem2)에 의하여 $A_\mathfrak{p} \rightarrow B_\mathfrak{q}$는 flat한 국소사상이므로, [보조정리 14](#lem14)에 의하여 $\Spec B_\mathfrak{q} \rightarrow \Spec A_\mathfrak{p}$는 전사이다. 특히 $\mathfrak{p}'A_\mathfrak{p}\in \Spec A_\mathfrak{p}$ 위에 놓인 $\Spec B_\mathfrak{q}$의 점이 존재하며, 이를 $B$의 prime ideal로 되돌리면 $\mathfrak{q}'\subseteq \mathfrak{q}$이면서 $\varphi^{-1}(\mathfrak{q}')=\mathfrak{p}'$인 $\mathfrak{q}'$를 얻는다. $\mathfrak{q}'\subseteq \mathfrak{q}$는 곧 $x\in \overline{\{x'\}}$을 뜻하므로 $x'=\mathfrak{q}'$가 원하는 점이다.
:::

즉 flat morphism은 base에서의 generization을 언제나 위로 들어올린다. 특히 $Y$가 irreducible이고 그 generic point가 $y$라면 $X$의 임의의 점은 generic fiber $X_y$의 어떤 점의 specialization이며, 따라서 $X$의 어떤 성분도 fiber 하나에 갇혀 있을 수 없다. [따름정리 6](#cor6)에서 곡선 위의 family에 대하여 관찰한 것이 일반적으로도 성립하는 것이다.

Going-down의 첫 번째 대가는 차원에 대한 정확한 등식이다. Flat morphism에서 $X$의 국소차원은 base의 국소차원과 fiber의 국소차원으로 정확히 분해된다.

::: 명제 16
Locally Noetherian scheme 사이의 flat morphism $f: X \rightarrow Y$와 점 $x\in X$, $y=f(x)$에 대하여

$$\dim \mathcal{O}_{X,x}=\dim \mathcal{O}_{Y,y}+\dim \mathcal{O}_{X_y,x}$$

가 성립한다. 여기에서 $X_y=f^{-1}(y)$는 $y$에서의 fiber이다.
:::
::: 증명
먼저 fiber의 local ring이 무엇인지를 확인한다. $X=\Spec B$, $Y=\Spec A$인 affine 상황으로 localize하고 $x=\mathfrak{q}$, $y=\mathfrak{p}=\varphi^{-1}(\mathfrak{q})$라 두자. 정의에 의하여 $X_y=\Spec (B\otimes_A\kappa(\mathfrak{p}))$이고, $x$에 대응하는 점에서의 local ring은

$$\mathcal{O}_{X_y,x}=(B\otimes_A\kappa(\mathfrak{p}))_\mathfrak{q}\cong B_\mathfrak{q}\otimes_{A_\mathfrak{p}}\kappa(\mathfrak{p})\cong B_\mathfrak{q}/\mathfrak{p}B_\mathfrak{q}=\mathcal{O}_{X,x}/\mathfrak{m}_y\mathcal{O}_{X,x}$$

이다. 즉 fiber의 local ring은 $\mathcal{O}_{X,x}$를 $\mathcal{O}_{Y,y}$의 maximal ideal로 나눈 것이다.

한편 $X$와 $Y$가 locally Noetherian이므로 $\mathcal{O}_{X,x}$와 $\mathcal{O}_{Y,y}$는 Noetherian local ring이고, [보조정리 2](#lem2)에 의하여 $\mathcal{O}_{Y,y} \rightarrow \mathcal{O}_{X,x}$는 flat한 국소사상이다. 따라서 [\[가환대수학\] §매개계, ⁋정리 9](/ko/math/commutative_algebra/system_of_parameters#thm9)를 적용하면 원하는 등식을 얻는다.
:::

이 등식이 도입에서 본 family의 non-flatness를 다시 한 번 설명해준다. 거기에서 $X=\Spec \mathbb{K}[t,\x]/(t\x)$의 원점 $x$를 생각하면 $X$의 두 성분이 모두 원점을 지나고 각각 $1$차원이므로 $\dim \mathcal{O}_{X,x}=1$이다. 또 $y=f(x)$는 $\mathbb{A}^1_\mathbb{K}$의 원점이므로 $\dim \mathcal{O}_{Y,y}=1$이고, fiber $X_y=\mathbb{A}^1_\mathbb{K}$의 원점에서의 local ring도 $1$차원이다. 등식이 요구하는 것은 $1=1+1$이므로 이 사상은 flat일 수 없다. 반대로 [예시 8](#ex8)의 $X$는 $2$차원이고 base는 $1$차원이므로, flatness로부터 모든 fiber가 $1$차원이어야 한다는 것이 자동으로 따라 나온다.

$X$와 $Y$가 field $\mathbb{K}$ 위의 finite type integral scheme인 경우에는 closed point에서 $\dim \mathcal{O}_{X,x}=\dim X$가 성립하므로 ([\[Har\] I.1.8A](https://link.springer.com/book/10.1007/978-1-4757-3849-0)의 등차원성), [명제 16](#prop16)은 익숙한 형태

$$\dim X_y=\dim X-\dim Y$$

가 된다. 이 등차원성 자체는 우리가 확립한 결과가 아니므로 여기에서는 인용에 그친다.

Flat morphism의 또 다른 기하학적 성질은 열린집합을 열린집합으로 본다는 것이다. 앞서 마련해둔 Chevalley의 정리와 going-down이 여기에서 정확히 맞물린다.

::: 명제 17
Noetherian scheme 사이의 flat하고 finite type인 사상 $f: X \rightarrow Y$는 열린 사상이다. 즉 임의의 열린집합 $U\subseteq X$에 대하여 $f(U)$는 $Y$의 열린집합이다.
:::
::: 증명
$Y$가 Noetherian이고 $f$가 finite type이므로 $X$ 또한 Noetherian scheme이다. 따라서 열린집합 $U\subseteq X$는 quasi-compact이며, open subscheme의 포함사상은 flat이므로 ([예시 4](#ex4)) [명제 3](#prop3)에 의하여 합성 $f\vert_U: U \rightarrow Y$ 또한 flat하고 finite type이다. 그러므로 처음부터 $U=X$인 경우, 즉 $f(X)$가 열린집합임을 보이면 충분하다.

[정리 12](#thm12)에 의하여 $f(X)$는 constructible이다. 또 $y\in f(X)$와 그 generization $y'$이 주어지면, $f(x)=y$인 $x$를 택하고 [명제 15](#prop15)를 적용하여 $f(x')=y'$인 $x'$를 얻으므로 $y'\in f(X)$이다. 즉 $f(X)$는 generization에 대하여 닫혀 있다. 이제 [보조정리 13](#lem13)으로부터 $f(X)$가 열린집합임을 얻는다.
:::

## 평탄성의 국소 판정법

마지막으로 flatness를 각 점에서 검사하는 기준을 정리한다. [명제 5](#prop5)의 torsion-free 판정법은 base가 PID일 때만 쓸 수 있었지만, 다음은 임의의 locally Noetherian base에서 성립한다.

::: 명제 18
Locally Noetherian scheme 사이의 locally of finite type인 사상 $f: X \rightarrow Y$와 점 $x\in X$, $y=f(x)$에 대하여, $\mathcal{O}_{X,x}$가 $\mathcal{O}_{Y,y}$-flat인 것과

$$\Tor_1^{\mathcal{O}_{Y,y}}(\kappa(y), \mathcal{O}_{X,x})=0$$

인 것은 서로 동치이다.
:::
::: 증명
$Y$가 locally Noetherian이므로 $A=\mathcal{O}_{Y,y}$는 Noetherian local ring이고, $f$가 locally of finite type이므로 $X$ 또한 locally Noetherian이어서 $E=\mathcal{O}_{X,x}$도 Noetherian local ring이다. $f$가 유도하는 $A \rightarrow E$는 국소사상이므로 $\mathfrak{m}_yE\subseteq \mathfrak{m}_x$를 만족한다. 이제 $M=E$로 두면 $M$은 finitely generated $E$-module이므로 [\[가환대수학\] §평탄성과 국소화, ⁋정리 1](/ko/math/commutative_algebra/local_criterion_for_flatness#thm1)의 가정이 모두 충족되며, 그 결론이 정확히 주장하는 동치이다.
:::

Flat한 점들의 집합이 $X$의 열린집합을 이룬다는 사실 또한 성립한다. 곧 $f$가 locally of finite presentation이면 $\mathcal{O}_{X,x}$가 $\mathcal{O}_{Y,f(x)}$-flat인 $x$들의 모임은 $X$에서 열려 있다. ([\[Stacks\] Tag 00RC](https://stacks.math.columbia.edu/tag/00RC)) [명제 10](#prop10)이 base에서 좋은 열린집합을 하나 찾아준 것이라면 이쪽은 $X$ 위에서의 열림을 주장하는 것이며, 그 증명에 필요한 도구는 우리가 갖춘 것과 다르므로 논증의 얼개만 적어두고 인용에 그친다. 먼저 Noetherian 근사로 $A$와 $B$가 $\mathbb{Z}$ 위의 finite type인 경우로 환원하고, $B$를 다항식환으로 바꾸어 모든 fiber ring이 유한한 global dimension을 갖도록 만든다. 그럼 문제의 module이 finite free module들의 유한 복합체 $F_\bullet$로 분해되어, flatness는 $F_\bullet$이 각 fiber 위에서 exact인지의 문제가 된다. 마지막 단계는 Buchsbaum과 Eisenbud의 exactness 판정법으로, 각 사상 $\varphi_i$의 rank와 그 행렬의 $r_i\times r_i$ minor들이 생성하는 ideal $I(\varphi_i)$의 depth 조건으로 exactness를 읽어내는 것이다. 이 $I(\varphi_i)$는 $\coker \varphi_i$의 Fitting ideal이며, minor라는 명시적인 $B$의 원소들로 주어지므로 그것이 정의하는 집합이 열려 있음을 직접 확인할 수 있다.

---

**참고문헌**

**[Har]** R. Hartshorne, *Algebraic geometry*, Springer, 1977.

**[Stacks]** The Stacks Project Authors, *Stacks Project*, https://stacks.math.columbia.edu.

**[EGA]** A. Grothendieck, *Éléments de géométrie algébrique*, IHES, 1960–1967.
