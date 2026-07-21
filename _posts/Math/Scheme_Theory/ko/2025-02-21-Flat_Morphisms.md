---
title: "평탄사상"
description: "평탄 사상의 정의와 기하학적 의미, 판정법과 예시를 다룬다. 평탄성은 사상의 fiber가 기저 위에서 일정한 대수적·기하학적 성질을 유지하도록 보장하는 핵심적인 성질이다."
excerpt: "Flat morphisms in algebraic geometry"

categories: [Math / Scheme Theory]
permalink: /ko/math/scheme_theory/flat_morphisms
sidebar: 
    nav: "scheme_theory-ko"

date: 2025-02-21
weight: 13
published: false
drift_needed: true
---

우리는 scheme morphism $f: X \rightarrow S$를 $S$로 parametrize된 family로 읽기로 하였으며 ([§스킴 사이의 사상, ⁋예시 10](/ko/math/scheme_theory/morphism_of_schemes#ex10)), 이 family의 $s\in S$에서의 멤버를 fiber $X_s=X\times_S\Spec \kappa(s)$로 정의하였다. ([§올곱, ⁋정의 12](/ko/math/scheme_theory/fiber_products#def12)) 이제 그 역을 물어야 한다. Morphism이기만 하면 언제나 좋은 family인가?

가장 자명한 family는 상수 family이다. $\mathbb{K}$-scheme $C$와 base $S$에 대하여 $C \rightarrow \Spec \mathbb{K}$를 $S \rightarrow \Spec \mathbb{K}$를 따라 pullback하면 $C\times_\mathbb{K} S \rightarrow S$를 얻고, 이 family의 fiber는 모든 $s$에서 $C_{\kappa(s)}$이다. 즉 이미 있는 scheme을 pullback하는 것만으로는 상수 family 이상을 만들어낼 수 없으며, 비자명한 family는 만들어지는 것이 아니라 방정식으로 주어진다. 예를 들어

$$\Spec \mathbb{K}[t, \x, \y]/(\y^2 - \x^3 - t) \longrightarrow \mathbb{A}^1_\mathbb{K}=\Spec \mathbb{K}[t]$$

는 매개변수 $t$가 움직임에 따라 평면곡선 $\y^2=\x^3+t$가 움직이는, 곡선들의 family이다.

문제는 이렇게 주어진 morphism이 family로서는 나쁘게 행동할 수 있다는 데에 있다. 가령

$$\Spec \mathbb{K}[t,\x]/(t\x) \longrightarrow \mathbb{A}^1_\mathbb{K}$$

에서 $t=a\neq 0$ 위의 fiber는 $a\x=0$이 강제하는 한 점이지만, $t=0$ 위의 fiber에서는 방정식 $t\x$가 통째로 사라져 직선 $\mathbb{A}^1_\mathbb{K}$ 전체가 남는다. Fiber의 차원이 $0$에서 $1$로 뛰는 것이다.

무엇이 잘못되었는지는 fiber를 꺼내는 연산이 대수적으로 무엇인지를 보면 드러난다. Fiber를 취하는 것은 base change이고, affine에서 base change는 tensor product이다. 즉 $X=\Spec B$와 $S=\Spec A$에 대하여 $s$에서의 fiber는 $\Spec (B\otimes_A\kappa(s))$이며, 더 일반적으로 family를 base를 따라 옮기는 연산은 functor $-\otimes_AB$이다. 그런데 tensor product는 완전하지 않다. 위의 예시에서 $A=\mathbb{K}[t]$의 단사사상 $A\xrightarrow{\ \times t\ }A$에 $-\otimes_AB$를 적용하면 $B\xrightarrow{\ \times t\ }B$가 되는데, $\x\neq 0$이면서 $t\x=0$이므로 이는 더 이상 단사가 아니다. 방정식이 사라진 것과 관계식이 무너진 것은 같은 사건이다.

따라서 family가 아무것도 부수지 않고 변하기를 요구하는 것은 정확히 $-\otimes_AB$가 완전하기를 요구하는 것이며, 이것이 flatness이다. 평탄 가군의 정의와 그 기본 판정법들은 [\[다중선형대수학\] §사영가군, 단사가군, 평탄가군, ⁋정의 7](/ko/math/multilinear_algebra/various_modules#def7)과 [\[가환대수학\] §평탄성](/ko/math/commutative_algebra/flatness)에서 이미 다루었으므로, 이 글에서는 이를 scheme의 언어로 옮기고 그것이 family에 대해 무엇을 말해주는지를 살펴본다.

## 평탄 사상의 정의

평탄 가군의 개념을 scheme으로 옮긴다. Morphism $f: X \rightarrow Y$가 평탄하다는 것은 대역적으로 말해 $X$의 구조층이 $Y$의 구조층 위에서 평탄한 가군 구조를 가진다는 의미이다.

::: 정의 1
Morphism $f: X \rightarrow Y$가 *flat<sub>평탄</sub>*이라는 것은 임의의 $x \in X$에 대하여 local ring $\mathcal{O}_{X,x}$가 $\mathcal{O}_{Y,f(x)}$-가군으로서 평탄한 것이다. 추가로 $f$가 대응하는 위상공간의 사상이 surjective이면 *faithfully flat<sub>충실히 평탄</sub>*이라 부른다.
:::

평탄성은 각 점에서의 국소적인 조건으로 정의되었지만, affine에서는 이를 대역적인 조건으로 바꿔 쓸 수 있다. 이 때문에 평탄성의 검사는 거의 언제나 가환대수학의 평탄 가군 검사로 환원된다.

::: 보조정리 2
Ring homomorphism $\varphi: A \rightarrow B$가 유도하는 morphism $f: \Spec B \rightarrow \Spec A$에 대하여, $f$가 평탄인 것과 $B$가 $A$-가군으로서 평탄한 것은 서로 동치이다.
:::
::: 증명
$\mathfrak{q}\in \Spec B$가 주어질 때마다 $\mathfrak{p}=\varphi^{-1}(\mathfrak{q})$로 적기로 한다.

우선 $B$가 $A$-평탄이라 가정하자. Localization $B \rightarrow B_\mathfrak{q}$는 평탄이므로 ([\[가환대수학\] §국소화의 성질들, ⁋명제 2](/ko/math/commutative_algebra/properties_of_localization#prop2)), functor $-\otimes_AB_\mathfrak{q}$는 $-\otimes_AB$와 $-\otimes_BB_\mathfrak{q}$의 합성이 되어 완전하다. 즉 $B_\mathfrak{q}$는 $A$-평탄이다. 한편 $B_\mathfrak{q}$는 $A_\mathfrak{p}$-대수이므로 $A_\mathfrak{p}\otimes_AB_\mathfrak{q}\cong B_\mathfrak{q}$이고, 따라서 임의의 $A_\mathfrak{p}$-가군 $M$에 대하여

$$M\otimes_AB_\mathfrak{q}\cong M\otimes_{A_\mathfrak{p}}(A_\mathfrak{p}\otimes_AB_\mathfrak{q})\cong M\otimes_{A_\mathfrak{p}}B_\mathfrak{q}$$

가 성립한다. 이제 $A_\mathfrak{p}$-가군의 단사사상 $M'\hookrightarrow M$은 $A$-가군의 단사사상이기도 하므로 $M'\otimes_AB_\mathfrak{q} \rightarrow M\otimes_AB_\mathfrak{q}$가 단사이고, 위의 동형에 의하여 $M'\otimes_{A_\mathfrak{p}}B_\mathfrak{q} \rightarrow M\otimes_{A_\mathfrak{p}}B_\mathfrak{q}$ 또한 단사이다. 즉 $\mathcal{O}_{\Spec B,\mathfrak{q}}=B_\mathfrak{q}$는 $\mathcal{O}_{\Spec A,\mathfrak{p}}=A_\mathfrak{p}$-평탄이며, $\mathfrak{q}$가 임의였으므로 $f$는 평탄이다.

역으로 $f$가 평탄이라 하자. 각 $\mathfrak{q}$에 대하여 $B_\mathfrak{q}$는 $A_\mathfrak{p}$-평탄이고 $A \rightarrow A_\mathfrak{p}$는 평탄이므로, 위와 같은 합성 논증에 의하여 $B_\mathfrak{q}$는 $A$-평탄이다. 이제 $A$-가군의 단사사상 $M'\hookrightarrow M$을 택하고

$$K=\ker(M'\otimes_AB \longrightarrow M\otimes_AB)$$

라 두자. Localization이 exact functor이므로 $B$의 임의의 maximal ideal $\mathfrak{q}$에 대하여 $K_\mathfrak{q}=\ker(M'\otimes_AB_\mathfrak{q} \rightarrow M\otimes_AB_\mathfrak{q})=0$이다. 그런데 $0\neq \xi\in K$가 존재한다면 $\ann(\xi)$는 $B$의 진 ideal이므로 어떤 maximal ideal $\mathfrak{q}$에 포함되고, $K_\mathfrak{q}=0$으로부터 $s\xi=0$인 $s\in B\setminus \mathfrak{q}$가 존재하여 $\ann(\xi)\not\subseteq \mathfrak{q}$가 되어 모순이다. 따라서 $K=0$이고 $B$는 $A$-평탄이다.
:::

평탄성이 base change와 합성에 대해 안정적이라는 것은 이제 순수하게 algebraic한 계산이다.

::: 명제 3
평탄 사상은 base change와 합성에 대하여 닫혀 있다. 즉 다음이 성립한다.

1. $f: X \rightarrow Y$가 평탄이고 $Z \rightarrow Y$가 임의의 사상이면, base change $X \times_Y Z \rightarrow Z$는 평탄이다. ([§올곱](/ko/math/scheme_theory/fiber_products))
2. $f: X \rightarrow Y$와 $g: Y \rightarrow Z$가 모두 평탄이면, 합성 $g \circ f: X \rightarrow Z$도 평탄이다.
:::
::: 증명
[보조정리 2](#lem2)에 의하여 둘 다 affine한 상황으로 환원된다.

(1) $A \rightarrow B$가 평탄일 때 임의의 $A$-대수 $C$에 대하여 $C \rightarrow B\otimes_AC$가 평탄임을 보이면 된다. 임의의 $C$-가군 $M$에 대하여

$$(B \otimes_A C) \otimes_C M \cong B \otimes_A (C \otimes_C M) \cong B \otimes_A M$$

이므로, $C$-가군의 단사사상 $M' \hookrightarrow M$에 $-\otimes_C (B \otimes_A C)$를 적용한 것은 $B \otimes_A M' \rightarrow B \otimes_A M$과 같다. $B$가 $A$-평탄이므로 이 사상은 단사이고, 따라서 $B \otimes_A C$는 $C$-평탄이다.

(2) $A \rightarrow B$와 $B \rightarrow C$가 모두 평탄이라 하자. 임의의 $A$-가군 $N$에 대하여 $N \otimes_A C \cong (N \otimes_A B) \otimes_B C$이므로 functor $-\otimes_A C$는 $-\otimes_A B$와 $-\otimes_B C$의 합성이다. 두 functor가 모두 완전하므로 그 합성 또한 완전하고, 따라서 $C$는 $A$-평탄이다.
:::

## Family와 평탄성

이제 도입에서 세운 관점으로 돌아가자. 우선 가장 기본적인 평탄 사상들을 모아둔다.

::: 예시 4
다음 사상들은 모두 평탄이다.

1. open subscheme의 포함사상 $U \hookrightarrow X$는 평탄이다. 이는 국소적으로 localization이며, localization은 언제나 평탄하기 때문이다. ([\[가환대수학\] §국소화의 성질들, ⁋명제 2](/ko/math/commutative_algebra/properties_of_localization#prop2))
2. 아핀공간 사이의 projection $\mathbb{A}^{n+m}_\mathbb{K} \rightarrow \mathbb{A}^n_\mathbb{K}$는 평탄이다. 이에 대응하는 ring homomorphism $\mathbb{K}[\x_1,\ldots,\x_n] \rightarrow \mathbb{K}[\x_1,\ldots,\x_n,\y_1,\ldots,\y_m]$은 자유가군 구조를 주고, 자유가군은 평탄하기 때문이다.
3. 상수 family $C \times_\mathbb{K} S \rightarrow S$는 평탄이다. Field 위의 모든 가군은 자유가군이므로 $C \rightarrow \Spec \mathbb{K}$가 평탄이고, [명제 3](#prop3)의 base change로부터 그 pullback인 $C\times_\mathbb{K}S \rightarrow S$도 평탄이기 때문이다.
:::

셋째 예시는 상수 family가 평탄임을 말해준다. 평탄성은 family가 변하는 것을 막는 조건이 아니라, 변하면서 무엇인가를 부수는 것을 막는 조건이다. 부수는 family의 전형은 도입에서 본 것이다.

::: 예시 5
$\mathbb{A}^1_\mathbb{K}=\Spec \mathbb{K}[t]$ 위의 family

$$X = \Spec \mathbb{K}[t, \x]/(t\x) \longrightarrow \mathbb{A}^1_\mathbb{K}$$

를 생각하자. $B=\mathbb{K}[t,\x]/(t\x)$가 $\mathbb{K}[t]$-평탄이라면 단사사상 $\mathbb{K}[t] \xrightarrow{\ \times t\ } \mathbb{K}[t]$에 $-\otimes_{\mathbb{K}[t]} B$를 적용하여 얻는 $B \xrightarrow{\ \times t\ } B$ 또한 단사여야 하지만, $\x \neq 0$이면서 $t\x = 0$이므로 그렇지 않다. 따라서 [보조정리 2](#lem2)에 의하여 이 사상은 평탄이 아니다.

기하학적으로 $X$는 평면의 두 좌표축의 합집합이며, $t = a \neq 0$ 위의 fiber는 $a\x = 0$이 강제하는 한 점인 반면 $t = 0$ 위의 fiber는 직선 $\mathbb{A}^1_\mathbb{K}$ 전체이다. 즉 fiber의 차원이 $0$에서 $1$로 뛴다.
:::

$X$를 이루는 두 성분 중 $\{\x=0\}$은 base 위로 전사하지만 $\{t=0\}$은 base의 한 점으로만 간다. 즉 $X$에는 base를 따라 퍼지지 않고 fiber 하나에 통째로 얹혀 있는 성분이 있으며, 이것이 $t=0$의 fiber를 부풀린 원인이다. Base가 곡선일 때 이 관찰은 평탄성의 완전한 판정법이 된다.

::: 명제 6
$A$가 PID이고 $B$가 $A$-대수라 하자. 그럼 $\Spec B \rightarrow \Spec A$가 평탄인 것과, $A$의 $0$이 아닌 임의의 원소가 $B$에서 zerodivisor가 아닌 것은 서로 동치이다.
:::
::: 증명
[보조정리 2](#lem2)에 의하여 이는 $B$가 $A$-평탄인 것과 동치이다. $A$가 PID이므로 특히 integral domain이고, 따라서 $A$의 $0$이 아닌 원소는 모두 $A$에서 zerodivisor가 아니다. 이제 [\[가환대수학\] §평탄성, ⁋따름정리 3](/ko/math/commutative_algebra/flatness#cor3)을 $M=B$에 적용하면 된다.
:::

즉 $\mathbb{K}[t]$ 위의 family가 평탄인 것은 그 coordinate ring이 $\mathbb{K}[t]$-가군으로서 torsion을 갖지 않는 것과 같다. Torsion 원소란 base의 함수 하나에 의해 죽는 원소이며, 기하학적으로는 fiber 하나에 갇힌 성분이 그러한 원소를 낳는다. 이를 정확히 적으면 다음과 같다.

::: 따름정리 7
Noetherian $\mathbb{K}[t]$-대수 $B$에 대하여 $X=\Spec B$가 reduced라 하자. 그럼 $X \rightarrow \mathbb{A}^1_\mathbb{K}$가 평탄인 것과, $X$의 모든 irreducible component가 $\mathbb{A}^1_\mathbb{K}$를 dominate하는 것은 서로 동치이다.
:::
::: 증명
[명제 6](#prop6)에 의하여 평탄성은 $\mathbb{K}[t]$의 $0$이 아닌 모든 원소가 $B$에서 zerodivisor가 아닌 것과 동치이다.

$B$가 Noetherian이므로 $B$의 zerodivisor 전체는 $\Ass B$의 원소들의 합집합이다. ([\[가환대수학\] §동반소아이디얼, ⁋정리 7](/ko/math/commutative_algebra/associated_primes#thm7)) 여기에 $B$가 reduced라는 가정을 더하면 이 합집합은 정확히 $B$의 minimal prime ideal $\mathfrak{p}_1,\ldots, \mathfrak{p}_k$들의 합집합이 된다. 실제로 minimal prime들이 언제나 $\Ass B$에 속한다는 것이 같은 정리의 첫째 결과이고, 역으로 $B$가 reduced이면

$$(0)=\mathfrak{N}(B)=\bigcap_{i=1}^k \mathfrak{p}_i$$

이므로, $ab=0$이고 $b\neq 0$인 zerodivisor $a$에 대하여 $b\not\in \mathfrak{p}_i$인 $i$를 택하면 $ab=0\in \mathfrak{p}_i$로부터 $a\in \mathfrak{p}_i$를 얻기 때문이다.

한편 $\mathfrak{p}_i$들은 정확히 $X$의 irreducible component $Z_i=V(\mathfrak{p}_i)$들의 generic point에 대응한다. 이제 $0\neq f\in \mathbb{K}[t]$가 $B$에서 zerodivisor인 것은 어떤 $i$에 대하여 $f\in \mathfrak{p}_i$인 것, 즉 $f$가 $Z_i$ 위에서 항등적으로 소멸하는 것과 같다. 그런데 $f$가 $Z_i$ 위에서 소멸한다는 것은 $Z_i$의 상이 진부분 닫힌집합 $Z(f)\subsetneq \mathbb{A}^1_\mathbb{K}$에 포함된다는 것, 즉 $Z_i$가 $\mathbb{A}^1_\mathbb{K}$를 dominate하지 않는다는 것과 같다. 역으로 $Z_i$가 dominate하지 않으면 그 상의 closure가 진부분 닫힌집합이므로 그 위에서 소멸하는 $0$이 아닌 $f\in \mathbb{K}[t]$가 존재하고, 이 $f$는 $\mathfrak{p}_i$에 속하여 zerodivisor가 된다. 이상에서 결론을 얻는다.
:::

[예시 5](#ex5)의 $X$는 reduced이고 그 성분 $\{t=0\}$이 base를 dominate하지 않으므로, [따름정리 7](#cor7)이 곧바로 비평탄성을 준다. 반면 같은 판정법은 fiber가 특이해지는 것과 평탄성이 깨지는 것이 서로 무관한 현상임을 보여준다.

::: 예시 8
cusp의 family

$$\Spec \mathbb{K}[t, \x, \y]/(\y^2 - \x^3 - t) \longrightarrow \mathbb{A}^1_\mathbb{K}$$

를 생각하자. 관계식이 $t = \y^2 - \x^3$을 주므로 coordinate ring은 $\mathbb{K}[\x,\y]$와 isomorphic이며, 이 동형 아래에서 $\mathbb{K}[t]$의 action은 $t \mapsto \y^2-\x^3$으로 주어진다. coordinate ring이 integral domain이므로 $\mathbb{K}[t]$의 $0$이 아닌 원소는 zerodivisor일 수 없고, [명제 6](#prop6)에 의하여 이 사상은 평탄이다. 그럼에도 $t=0$ 위의 fiber는 cusp $\y^2=\x^3$이 되어 singular point를 갖는다.

node의 family

$$\Spec \mathbb{K}[t, \x, \y]/(\x\y - t) \longrightarrow \mathbb{A}^1_\mathbb{K}$$

도 마찬가지이다. $t=\x\y$로 두면 coordinate ring은 integral domain $\mathbb{K}[\x,\y]$와 isomorphic이므로 평탄이며, $t\neq 0$ 위의 fiber는 smooth한 쌍곡선 $\x\y=t$이지만 $t=0$ 위의 fiber는 두 직선이 만나는 node $\x\y=0$이다.

요컨대 평탄성이 통제하는 것은 fiber가 특이해지는지의 여부가 아니라, fiber들이 같은 크기로 남는지의 여부이다.
:::

곡선들의 family를 제대로 다루려면 fiber가 아핀평면 밖으로 달아나지 않아야 하므로 projective space 안에서 보는 것이 자연스럽다. ([§사영스킴](/ko/math/scheme_theory/projective_schemes))

::: 예시 9
$\x,\y,\z$의 차수로 grading을 준 graded ring $\mathbb{K}[t][\x,\y,\z]$를 생각하자. 여기에서 $t$는 차수 $0$이며, 따라서 base ring은 $\mathbb{K}[t]$이다. 이제

$$X=\Proj \mathbb{K}[t][\x,\y,\z]/(\x\z-t\y^2)$$

라 두면 구조사상 $X \rightarrow \mathbb{A}^1_\mathbb{K}$를 얻으며, $X$는 $\mathbb{P}^2$ 안에서 방정식 $\x\z=t\y^2$이 자르는 곡선들의 family이다.

이 사상이 평탄인 것은 세 개의 affine chart에서 확인된다. $D_+(\y)$ 위에서 $u=\x/\y$, $v=\z/\y$로 두면 관계식을 $\y^2$으로 나누어 $uv=t$를 얻으므로 coordinate ring은 $\mathbb{K}[t][u,v]/(uv-t)$이며, 이는 $t=uv$를 통해 integral domain $\mathbb{K}[u,v]$와 isomorphic이다. 따라서 [명제 6](#prop6)에 의하여 평탄이다. $D_+(\x)$ 위에서 $w=\y/\x$, $s=\z/\x$로 두면 관계식을 $\x^2$으로 나누어 $s=tw^2$을 얻으므로 coordinate ring은 $\mathbb{K}[t][w]$이고, 이는 자유 $\mathbb{K}[t]$-가군이므로 평탄이다. $D_+(\z)$의 경우도 symmetric이다. 이 셋이 $X$를 덮으므로 $X \rightarrow \mathbb{A}^1_\mathbb{K}$는 평탄이다.

Fiber를 보면, $t=a\neq 0$ 위에서는 $\mathbb{P}^2$의 원뿔곡선 $\x\z=a\y^2$이 되어 smooth하고 $\mathbb{P}^1$과 isomorphic이다. 반면 $t=0$ 위에서는 $\x\z=0$, 즉 두 직선 $\{\x=0\}$과 $\{\z=0\}$이 점 $[0:1:0]$에서 만나는 곡선이 된다. 즉 이것은 smooth한 원뿔곡선이 두 직선으로 퇴화하는 상수 아닌 곡선들의 family이며, 그럼에도 모든 fiber가 $1$차원으로 남는다.
:::

## 제네릭 평탄성

이제부터 평탄 사상의 기하학적 성질들을 살펴볼 것인데, 그 증명들은 예외 없이 두 가지 준비물 위에 놓인다. 하나는 평탄성이 base의 조밀한 열린집합 위에서는 언제나 성립한다는 사실이고, 다른 하나는 finite type 사상의 상이 언제나 constructible이라는 Chevalley의 정리이다. 그런데 이 둘은 모두 다음의 대수적 정리 하나에서 나오므로, 기하로 넘어가기 전에 이를 먼저 마련해둔다.

::: 정리 10 (Grothendieck의 generic freeness)
Noetherian integral domain $A$와 finite type $A$-대수 $B$, 그리고 finitely generated $B$-가군 $M$이 주어졌다 하자. 그럼 $0$이 아닌 $a\in A$가 존재하여 $M_a$가 자유 $A_a$-가군이 된다.
:::
::: 증명
$B$는 Noetherian integral domain $A$ 위의 finite type 대수이므로 Hilbert 기저정리에 의하여 Noetherian ring이다.

**Dévissage.** [\[가환대수학\] §동반소아이디얼, ⁋보조정리 6](/ko/math/commutative_algebra/associated_primes#lem6)을 $B$와 $M$에 적용하면 filtration

$$0=M_0\subseteq M_1\subseteq\cdots\subseteq M_n=M,\qquad M_i/M_{i-1}\cong B/\mathfrak{q}_i$$

를 얻는다. 각 $B/\mathfrak{q}_i$에 대하여 결론이 성립한다 하고 그 원소들의 곱을 $a$라 하면, exact sequence

$$0 \longrightarrow (M_{i-1})_a \longrightarrow (M_i)_a \longrightarrow (B/\mathfrak{q}_i)_a \longrightarrow 0$$

의 오른쪽 항이 자유가군이므로 이 exact sequence는 split하고, $i$에 대한 귀납법으로 $(M_i)_a$가 모두 자유 $A_a$-가군이 된다. 따라서 $M=B/\mathfrak{q}$인 경우, 즉 $B$를 $B/\mathfrak{q}$로 바꾸어 $B$가 integral domain이고 $M=B$인 경우만 보이면 충분하다.

**환원.** $\varphi: A \rightarrow B$의 kernel이 $0$이 아니라면 $0\neq a\in \ker \varphi$를 택하자. $B_a=B\otimes_AA_a$에서 $\varphi(a)=0$이면서 $a$가 unit이므로 $B_a=0$이고, 이는 rank $0$의 자유가군이다. 따라서 $A\subseteq B$라 가정해도 좋다.

**귀납.** $K=\Frac(A)$라 하자. $B\otimes_AK$는 $A\setminus\{0\}$에서의 $B$의 localization이므로 $0$이 아닌 integral domain이며, $K$ 위의 finite type 대수이다. $d=\dim (B\otimes_AK)$에 대한 귀납법을 쓴다.

[§차원, ⁋정리 9](/ko/math/scheme_theory/dimension#thm9)에 의하여 algebraically independent한 원소들 $y_1,\ldots, y_d\in B\otimes_AK$가 존재하여 $B\otimes_AK$가 $K[y_1,\ldots,y_d]$ 위의 유한가군이다. 각 $y_i$에 $A$의 $0$이 아닌 원소를 곱해도 대수적 독립성과 유한성은 유지되므로, 처음부터 $y_i\in B$라 가정해도 좋다.

$B$를 $A$-대수로서 생성하는 원소를 $b_1,\ldots, b_m$이라 하면 각 $b_j$는 $K[y_1,\ldots,y_d]$ 위에서 integral하다. 이 정수 방정식들에 등장하는 계수는 유한개이므로, 그 분모를 모두 없애는 $0\neq a_0\in A$를 택할 수 있다. 그럼 각 $b_j$는

$$C=A_{a_0}[y_1,\ldots, y_d]$$

위에서 integral하고, 따라서 $B_{a_0}$는 유한 $C$-가군이다. 여기에서 $y_i$들이 $K$ 위에서 대수적으로 독립이므로 $C$는 $A_{a_0}$ 위의 polynomial ring이며, 특히 자유 $A_{a_0}$-가군이다.

이제 dévissage를 Noetherian ring $C$와 유한 $C$-가군 $B_{a_0}$에 다시 적용하면, quotient가 $C/\mathfrak{p}$ 꼴인 유한 filtration을 얻는다. 따라서 각 $C/\mathfrak{p}$에 대하여 결론을 보이면 충분하다.

$\mathfrak{p}=0$이면 $C$ 자신이 자유 $A_{a_0}$-가군이므로 볼 것이 없다. $\mathfrak{p}\neq 0$이라 하자. 만일 $\mathfrak{p}\cap A_{a_0}\neq 0$이면 그 안의 $0$이 아닌 원소 $a_1$을 택했을 때 $(C/\mathfrak{p})_{a_1}=0$이므로 결론이 성립한다. 그렇지 않다면 $S=A_{a_0}\setminus\{0\}$에 대하여 $S^{-1}C=K[y_1,\ldots,y_d]$이고 $\mathfrak{p}\cap S=\emptyset$이므로, $\mathfrak{p}K[y_1,\ldots,y_d]$는 $K[y_1,\ldots,y_d]$의 $0$이 아닌 prime ideal이다. 이제

$$(C/\mathfrak{p})\otimes_{A_{a_0}}K=K[y_1,\ldots,y_d]/\mathfrak{p}K[y_1,\ldots,y_d]$$

인데, $0\neq g\in \mathfrak{p}K[y_1,\ldots,y_d]$를 택하면 이 quotient ring에서 $y_1,\ldots,y_d$의 image들은 $g=0$이라는 대수적 관계를 만족하므로 대수적으로 독립일 수 없다. 그런데 이 quotient ring은 이들 image로 생성되는 $K$-대수이므로 그 field of fractions의 초월차수는 $d$보다 작고, [§차원, ⁋명제 10](/ko/math/scheme_theory/dimension#prop10)에 의하여

$$\dim\big((C/\mathfrak{p})\otimes_{A_{a_0}}K\big)<d$$

이다. $A_{a_0}$ 또한 $K$를 field of fractions로 갖는 Noetherian integral domain이고 $C/\mathfrak{p}$는 그 위의 finite type integral domain이므로, 귀납가정을 적용하면 $0\neq a_\mathfrak{p}\in A_{a_0}$가 존재하여 $(C/\mathfrak{p})_{a_\mathfrak{p}}$가 자유 $(A_{a_0})_{a_\mathfrak{p}}$-가군이다. 필요하다면 $a_0$의 거듭제곱을 곱하여 $a_\mathfrak{p}\in A$로 볼 수 있다.

$d=0$인 경우에는 $C=A_{a_0}$이므로 위의 dévissage가 주는 quotient는 $A_{a_0}/\mathfrak{p}$ 꼴이고, $\mathfrak{p}=0$이면 자유가군, $\mathfrak{p}\neq 0$이면 $\mathfrak{p}$의 $0$이 아닌 원소를 뒤집어 $0$으로 만들 수 있으므로 귀납의 기저가 된다.

Filtration에 등장하는 유한개의 $\mathfrak{p}$들에 대한 $a_\mathfrak{p}$와 $a_0$의 곱을 $a$로 두면 $B_a=(B_{a_0})_a$는 자유 $A_a$-가군이다.
:::

::: 명제 11 (제네릭 평탄성)
Noetherian integral scheme $Y$와 finite type morphism $f: X \rightarrow Y$가 주어졌다 하자. 그럼 $Y$의 조밀한 열린집합 $U$가 존재하여 $f\rvert_{f^{-1}(U)}: f^{-1}(U) \rightarrow U$가 평탄이다.
:::
::: 증명
$Y$가 irreducible이므로 $Y$의 공집합이 아닌 열린집합은 모두 조밀하다. 따라서 $Y$의 affine open $V=\Spec A$를 하나 고정하고 그 안에서 $U$를 찾으면 충분하다. $Y$가 Noetherian integral이므로 $A$는 Noetherian integral domain이다.

$f$가 finite type이므로 $f^{-1}(V)$는 유한개의 affine open $\Spec B_1,\ldots, \Spec B_k$로 덮이고, 각 $B_i$는 finite type $A$-대수이다. [정리 10](#thm10)을 $M=B_i$에 적용하면 $0\neq a_i\in A$가 존재하여 $(B_i)_{a_i}$가 자유 $A_{a_i}$-가군이다. $a=a_1\cdots a_k$로 두면 각 $(B_i)_a$는 자유가군 $(B_i)_{a_i}$의 localization이므로 여전히 자유 $A_a$-가군이고, 자유가군은 평탄하므로 [보조정리 2](#lem2)에 의하여

$$\Spec (B_i)_a \longrightarrow \Spec A_a=D(a)$$

는 평탄이다. 평탄성은 $X$ 위에서 국소적인 조건이고 $\Spec (B_i)_a$들이 $f^{-1}(D(a))$를 덮으므로 $f^{-1}(D(a)) \rightarrow D(a)$는 평탄이다. $A$가 integral domain이고 $a\neq 0$이므로 $D(a)$는 공집합이 아니며, 따라서 $U=D(a)$가 원하는 열린집합이다.
:::

## Chevalley 정리

두 번째 준비물은 상의 모양에 대한 것이다. 일반적인 사상의 상은 열린집합도 닫힌집합도 아니지만, finite type 사상의 상은 언제나 다음의 의미에서 좋은 집합이다.

::: 정의 12
위상공간 $T$의 부분집합이 *locally closed<sub>국소 닫힌</sub>*라는 것은 그것이 열린집합과 닫힌집합의 교집합으로 쓰일 수 있는 것이다. 또, $T$의 부분집합이 *constructible<sub>구성가능</sub>*이라는 것은 그것이 유한개의 locally closed subset들의 합집합으로 쓰일 수 있는 것이다.
:::

Constructible subset들의 모임은 유한합집합, 유한교집합, 여집합에 대하여 닫혀 있다. 유한합집합은 정의에 의하여 자명하고, 두 locally closed subset의 교집합 $(U_1\cap Z_1)\cap (U_2\cap Z_2)=(U_1\cap U_2)\cap (Z_1\cap Z_2)$이 다시 locally closed이므로 교집합에 대한 닫힘은 분배법칙으로부터 나오며, locally closed subset $U\cap Z$의 여집합은 $(T\setminus U)\cup (T\setminus Z)$로 두 locally closed subset의 합집합이므로 여집합에 대해서도 닫혀 있다.

::: 정리 13 (Chevalley)
Noetherian scheme $Y$와 finite type morphism $f: X \rightarrow Y$에 대하여, $f(X)$는 $Y$의 constructible subset이다.
:::
::: 증명
$Y$의 닫힌 부분집합 $Z$에 대하여, "$Z$ 위의 임의의 finite type morphism의 상은 $Z$의 constructible subset이다"라는 명제를 $P(Z)$라 하자. $Y$가 Noetherian이므로 닫힌 부분집합들의 모임은 descending chain condition을 만족하고, 따라서 Noetherian 귀납법을 쓸 수 있다. 즉 $Y$의 모든 진부분 닫힌집합 $Z\subsetneq Y$에 대하여 $P(Z)$가 성립한다고 가정하고 $P(Y)$를 보이면 된다. 또 $Z$의 constructible subset은 $Y$의 constructible subset이므로 ($Z$가 닫힌집합이기 때문이다) 결론을 $Y$ 안에서 읽어도 좋다.

**Affine으로의 환원.** $f$가 finite type이므로 $Y$를 유한개의 affine open $V_j$로 덮고 각 $f^{-1}(V_j)$를 유한개의 affine open으로 덮으면, $f(X)$는 유한개의 $\Spec B \rightarrow \Spec A$ 꼴 사상의 상들의 합집합이다. 열린집합 $V_j$의 constructible subset은 $Y$의 constructible subset이고 constructible subset들의 유한합집합은 constructible이므로, $Y=\Spec A$, $X=\Spec B$이고 $B$가 finite type $A$-대수인 경우만 보이면 충분하다.

**Reduced로의 환원.** $\mathfrak{N}=\mathfrak{N}(A)$를 $A$의 nilradical이라 하면 $\mathfrak{N}B$는 $B$의 nilpotent ideal이므로 $\Spec B/\mathfrak{N}B$와 $\Spec B$는 같은 위상공간이고, $\Spec A/\mathfrak{N}$과 $\Spec A$도 그러하다. 따라서 $A$를 $A/\mathfrak{N}$으로, $B$를 $B/\mathfrak{N}B$로 바꾸어도 $f(X)$는 바뀌지 않으므로 $A$가 reduced라 가정해도 좋다.

**integral domain으로의 환원.** $A$의 minimal prime을 $\mathfrak{p}_1,\ldots, \mathfrak{p}_k$라 하면 $A$가 reduced이므로 $Y=\bigcup_j V(\mathfrak{p}_j)$이다. 만일 $k\geq 2$라면 각 $V(\mathfrak{p}_j)$는 $Y$의 진부분 닫힌집합이고

$$f(X)=\bigcup_{j=1}^k f\big(X\times_Y V(\mathfrak{p}_j)\big)$$

인데, 각 base change $X\times_YV(\mathfrak{p}_j) \rightarrow V(\mathfrak{p}_j)$는 여전히 finite type이므로 귀납가정 $P(V(\mathfrak{p}_j))$에 의하여 각 항이 constructible이고 따라서 $f(X)$도 constructible이다. 그러므로 $k=1$, 즉 $A$가 integral domain인 경우만 남는다.

**integral domain인 경우.** $B=0$이면 $f(X)=\emptyset$이므로 자명하다. $B\neq 0$이라 하고 [정리 10](#thm10)을 $M=B$에 적용하면 $0\neq a\in A$가 존재하여 $B_a$가 자유 $A_a$-가군이다. $a$가 unit이면 $D(a)=Y$이므로 $a$를 unit이 아닌 것으로 택했다고 가정해도 좋고 (unit이라면 아래 논증에서 $V(a)=\emptyset$이 되어 결론이 더 간단해진다), 이 경우 $A$가 integral domain이므로 $V(a)$는 $Y$의 진부분 닫힌집합이다.

$B_a=0$인 경우, 이는 $\varphi(a)$가 $B$에서 nilpotent라는 뜻이므로 $\varphi(a)$는 $B$의 모든 prime ideal에 속한다. 따라서 $f(X)\subseteq V(a)$이고, $f(X)$는 base change $X\times_YV(a) \rightarrow V(a)$의 상과 같으므로 귀납가정 $P(V(a))$에 의하여 constructible이다.

$B_a\neq 0$인 경우, $B_a$는 $0$이 아닌 자유 $A_a$-가군이다. 임의의 $\mathfrak{p}\in D(a)$에 대하여

$$B_a\otimes_{A_a}\kappa(\mathfrak{p})\cong \kappa(\mathfrak{p})^{(r)}\neq 0$$

이므로 ($r\geq 1$은 $B_a$의 rank이다) $\mathfrak{p}$ 위의 fiber는 공집합이 아니고, 따라서 $D(a)\subseteq f(X)$이다. 그럼

$$f(X)=D(a)\cup \big(f(X)\cap V(a)\big)$$

이고, $f(X)\cap V(a)$는 base change $X\times_YV(a) \rightarrow V(a)$의 상이므로 귀납가정 $P(V(a))$에 의하여 constructible이다. $D(a)$는 열린집합이므로 constructible이고, 따라서 $f(X)$는 constructible이다.
:::

Constructible한 집합이 언제 열린집합이 되는지도 함께 정리해둔다. 이것이 평탄성과 만나는 지점은 다음 절에서 드러난다.

::: 보조정리 14
Noetherian scheme $Y$의 constructible subset $E$가 generization에 대하여 닫혀 있다면, 즉 $y\in E$이고 $y\in \overline{\{y'\}}$일 때마다 $y'\in E$라면, $E$는 $Y$의 열린집합이다.
:::
::: 증명
여집합 $F=Y\setminus E$는 constructible이며 specialization에 대하여 닫혀 있다. $F$가 닫힌집합임을 보이면 된다. $F=\emptyset$인 경우는 자명하므로 $F\neq \emptyset$이라 하고, $Z=\overline{F}$의 irreducible component들을 $Z_1,\ldots, Z_k$라 하자. $Y$가 Noetherian이므로 이들은 유한개이다.

먼저 각 $j$에 대하여 $\overline{F\cap Z_j}=Z_j$임을 보인다. 만일 $W=\overline{F\cap Z_j}\subsetneq Z_j$라면 $F\subseteq W\cup \bigcup_{i\neq j}Z_i$이고 우변이 닫힌집합이므로 $Z=\overline{F}\subseteq W\cup \bigcup_{i\neq j}Z_i$인데, 이는 $Z_j$가 $Z$의 irreducible component라는 것에 모순이다.

이제 $F$를 locally closed subset들의 유한합집합 $F=\bigcup_{i=1}^n (U_i\cap C_i)$로 쓰자. $Z_j$가 irreducible이고

$$Z_j=\overline{F\cap Z_j}=\bigcup_{i=1}^n \overline{U_i\cap C_i\cap Z_j}$$

이므로, 적당한 $i$에 대하여 $\overline{U_i\cap C_i\cap Z_j}=Z_j$이다. 그럼 $U_i\cap C_i\cap Z_j\subseteq C_i$이고 $C_i$가 닫힌집합이므로 $Z_j\subseteq C_i$이며, 따라서

$$U_i\cap Z_j\subseteq U_i\cap C_i\subseteq F$$

이다. 한편 $U_i\cap Z_j$는 $Z_j$의 열린 부분집합이며 그 closure가 $Z_j$이므로 공집합이 아니다. $Z_j$는 $Y$의 irreducible closed subset이므로 generic point $\eta_j$를 가지며, $Z_j$의 공집합이 아닌 열린 부분집합은 언제나 $\eta_j$를 포함하므로 $\eta_j\in F$이다.

$F$가 specialization에 대하여 닫혀 있으므로 $Z_j=\overline{\{\eta_j\}}\subseteq F$이고, 이것이 모든 $j$에 대하여 성립하므로 $Z=\bigcup_j Z_j\subseteq F$이다. $F\subseteq Z$는 자명하므로 $F=Z$는 닫힌집합이다.
:::

## 평탄 사상의 기하학적 성질

준비를 마쳤으므로 이제 평탄성이 기하학적으로 무엇을 뜻하는지를 본다. 평탄성의 내용은 fiber들이 서로 이어지는 방식을 통제한다는 데에 있으며, 그 출발점은 평탄한 국소사상이 자동으로 충실평탄이 된다는 다음 관찰이다.

::: 보조정리 15
local ring 사이의 국소사상 $\varphi: (A,\mathfrak{m}) \rightarrow (B,\mathfrak{n})$이 $B$를 평탄 $A$-가군으로 만든다 하자. 그럼 $0$이 아닌 임의의 $A$-가군 $M$에 대하여 $M\otimes_AB\neq 0$이며, 특히 $\Spec B \rightarrow \Spec A$는 전사이다.
:::
::: 증명
$0\neq \xi\in M$을 택하자. $\ann(\xi)$는 $A$의 진 ideal이므로 $\ann(\xi)\subseteq \mathfrak{m}$이고, $A/\ann(\xi)\cong A\xi$는 $M$의 submodule이다. 여기에 평탄한 functor $-\otimes_AB$를 적용하면 단사사상

$$B/\ann(\xi)B\cong (A/\ann(\xi))\otimes_AB\hookrightarrow M\otimes_AB$$

를 얻는다. 그런데 $\varphi$가 국소사상이므로 $\ann(\xi)B\subseteq \mathfrak{m}B\subseteq \mathfrak{n}\subsetneq B$이고, 따라서 $B/\ann(\xi)B\neq 0$이다. 즉 $M\otimes_AB\neq 0$이다.

이제 임의의 $\mathfrak{p}\in \Spec A$에 대하여 $M=\kappa(\mathfrak{p})$로 두면 $\kappa(\mathfrak{p})\neq 0$이므로 fiber ring

$$B\otimes_A\kappa(\mathfrak{p})$$

은 $0$이 아닌 ring이고, 따라서 prime ideal을 갖는다. 그러한 prime ideal에 대응하는 $\Spec B$의 점은 $\mathfrak{p}$ 위에 놓이므로 $\Spec B \rightarrow \Spec A$는 전사이다.
:::

이로부터 평탄 사상이 generization을 들어올린다는 것, 곧 going-down 성질을 얻는다. 같은 결과가 가환대수학의 언어로 이미 서술된 바 있다. ([\[가환대수학\] §매개계, ⁋보조정리 8](/ko/math/commutative_algebra/system_of_parameters#lem8))

::: 명제 16
평탄 사상 $f: X \rightarrow Y$와 점 $x \in X$가 주어졌다 하고, $y=f(x)$의 generization $y'$, 즉 $y \in \overline{\{y'\}}$인 점 $y'$가 주어졌다 하자. 그럼 $x$의 generization $x'$가 존재하여 $f(x')=y'$이다.
:::
::: 증명
$x$의 affine open neighborhood $U=\Spec B$와 $f(U)$를 포함하는 affine open $V=\Spec A$를 택하면, $y'$이 $y$의 generization이므로 $y'\in V$이다. 따라서 $X=\Spec B$, $Y=\Spec A$이고 $x=\mathfrak{q}$, $y=\mathfrak{p}=\varphi^{-1}(\mathfrak{q})$, $y'=\mathfrak{p}'\subseteq \mathfrak{p}$인 경우만 보이면 충분하다.

[보조정리 2](#lem2)에 의하여 $A_\mathfrak{p} \rightarrow B_\mathfrak{q}$는 평탄한 국소사상이므로, [보조정리 15](#lem15)에 의하여 $\Spec B_\mathfrak{q} \rightarrow \Spec A_\mathfrak{p}$는 전사이다. 특히 $\mathfrak{p}'A_\mathfrak{p}\in \Spec A_\mathfrak{p}$ 위에 놓인 $\Spec B_\mathfrak{q}$의 점이 존재하며, 이를 $B$의 prime ideal로 되돌리면 $\mathfrak{q}'\subseteq \mathfrak{q}$이면서 $\varphi^{-1}(\mathfrak{q}')=\mathfrak{p}'$인 $\mathfrak{q}'$를 얻는다. $\mathfrak{q}'\subseteq \mathfrak{q}$는 곧 $x\in \overline{\{x'\}}$을 뜻하므로 $x'=\mathfrak{q}'$가 원하는 점이다.
:::

즉 평탄 사상은 base에서의 generization을 언제나 위로 들어올린다. 특히 $Y$가 irreducible이고 그 generic point가 $\eta$라면 $X$의 임의의 점은 generic fiber $X_\eta$의 어떤 점의 specialization이며, 따라서 $X$의 어떤 성분도 fiber 하나에 갇혀 있을 수 없다. [따름정리 7](#cor7)에서 곡선 위의 family에 대하여 관찰한 것이 일반적으로도 성립하는 것이다.

Going-down의 첫 번째 대가는 차원에 대한 정확한 등식이다. 평탄 사상에서 $X$의 국소차원은 base의 국소차원과 fiber의 국소차원으로 정확히 분해된다.

::: 명제 17
Locally Noetherian scheme 사이의 평탄 사상 $f: X \rightarrow Y$와 점 $x\in X$, $y=f(x)$에 대하여

$$\dim \mathcal{O}_{X,x}=\dim \mathcal{O}_{Y,y}+\dim \mathcal{O}_{X_y,x}$$

가 성립한다. 여기에서 $X_y=f^{-1}(y)$는 $y$에서의 fiber이다.
:::
::: 증명
먼저 fiber의 local ring이 무엇인지를 확인한다. $X=\Spec B$, $Y=\Spec A$인 affine 상황으로 localize하고 $x=\mathfrak{q}$, $y=\mathfrak{p}=\varphi^{-1}(\mathfrak{q})$라 두자. 정의에 의하여 $X_y=\Spec (B\otimes_A\kappa(\mathfrak{p}))$이고, $x$에 대응하는 점에서의 local ring은

$$\mathcal{O}_{X_y,x}=(B\otimes_A\kappa(\mathfrak{p}))_\mathfrak{q}\cong B_\mathfrak{q}\otimes_{A_\mathfrak{p}}\kappa(\mathfrak{p})\cong B_\mathfrak{q}/\mathfrak{p}B_\mathfrak{q}=\mathcal{O}_{X,x}/\mathfrak{m}_y\mathcal{O}_{X,x}$$

이다. 즉 fiber의 local ring은 $\mathcal{O}_{X,x}$를 $\mathcal{O}_{Y,y}$의 maximal ideal로 나눈 것이다.

한편 $X$와 $Y$가 locally Noetherian이므로 $\mathcal{O}_{X,x}$와 $\mathcal{O}_{Y,y}$는 Noetherian local ring이고, [보조정리 2](#lem2)에 의하여 $\mathcal{O}_{Y,y} \rightarrow \mathcal{O}_{X,x}$는 평탄한 국소사상이다. 따라서 [\[가환대수학\] §매개계, ⁋정리 9](/ko/math/commutative_algebra/system_of_parameters#thm9)를 적용하면 원하는 등식을 얻는다.
:::

이 등식이 [예시 5](#ex5)의 비평탄성을 다시 한 번 설명해준다. 그 예시에서 $X=\Spec \mathbb{K}[t,\x]/(t\x)$의 원점 $x$를 생각하면 $X$의 두 성분이 모두 원점을 지나고 각각 $1$차원이므로 $\dim \mathcal{O}_{X,x}=1$이다. 또 $y=f(x)$는 $\mathbb{A}^1_\mathbb{K}$의 원점이므로 $\dim \mathcal{O}_{Y,y}=1$이고, fiber $X_y=\mathbb{A}^1_\mathbb{K}$의 원점에서의 local ring도 $1$차원이다. 등식이 요구하는 것은 $1=1+1$이므로 이 사상은 평탄일 수 없다. 반대로 [예시 9](#ex9)의 $X$는 $2$차원이고 base는 $1$차원이므로, 평탄성으로부터 모든 fiber가 $1$차원이어야 한다는 것이 자동으로 따라 나온다.

$X$와 $Y$가 field $\mathbb{K}$ 위의 finite type integral scheme인 경우에는 closed point에서 $\dim \mathcal{O}_{X,x}=\dim X$가 성립하므로 ([\[Har\] I.1.8A](https://link.springer.com/book/10.1007/978-1-4757-3849-0)의 등차원성), [명제 17](#prop17)은 익숙한 형태

$$\dim X_y=\dim X-\dim Y$$

가 된다. 이 등차원성 자체는 우리가 확립한 결과가 아니므로 여기에서는 인용에 그친다.

평탄 사상의 또 다른 기하학적 성질은 열린집합을 열린집합으로 본다는 것이다. 앞서 마련해둔 Chevalley의 정리와 going-down이 여기에서 정확히 맞물린다.

::: 명제 18
Noetherian scheme 사이의 평탄하고 finite type인 사상 $f: X \rightarrow Y$는 열린 사상이다. 즉 임의의 열린집합 $U\subseteq X$에 대하여 $f(U)$는 $Y$의 열린집합이다.
:::
::: 증명
$Y$가 Noetherian이고 $f$가 finite type이므로 $X$ 또한 Noetherian scheme이다. 따라서 열린집합 $U\subseteq X$는 quasi-compact이며, open subscheme의 포함사상은 평탄이므로 ([예시 4](#ex4)) [명제 3](#prop3)에 의하여 합성 $f\vert_U: U \rightarrow Y$ 또한 평탄하고 finite type이다. 그러므로 처음부터 $U=X$인 경우, 즉 $f(X)$가 열린집합임을 보이면 충분하다.

[정리 13](#thm13)에 의하여 $f(X)$는 constructible이다. 또 $y\in f(X)$와 그 generization $y'$이 주어지면, $f(x)=y$인 $x$를 택하고 [명제 16](#prop16)을 적용하여 $f(x')=y'$인 $x'$를 얻으므로 $y'\in f(X)$이다. 즉 $f(X)$는 generization에 대하여 닫혀 있다. 이제 [보조정리 14](#lem14)로부터 $f(X)$가 열린집합임을 얻는다.
:::

## 평탄성의 국소 판정법

마지막으로 평탄성을 각 점에서 검사하는 기준을 정리한다. [명제 6](#prop6)의 torsion-free 판정법은 base가 PID일 때만 쓸 수 있었지만, 다음은 임의의 locally Noetherian base에서 성립한다.

::: 명제 19
Locally Noetherian scheme 사이의 locally of finite type인 사상 $f: X \rightarrow Y$와 점 $x\in X$, $y=f(x)$에 대하여, $\mathcal{O}_{X,x}$가 $\mathcal{O}_{Y,y}$-평탄인 것과

$$\Tor_1^{\mathcal{O}_{Y,y}}(\kappa(y), \mathcal{O}_{X,x})=0$$

인 것은 서로 동치이다.
:::
::: 증명
$Y$가 locally Noetherian이므로 $A=\mathcal{O}_{Y,y}$는 Noetherian local ring이고, $f$가 locally of finite type이므로 $X$ 또한 locally Noetherian이어서 $E=\mathcal{O}_{X,x}$도 Noetherian local ring이다. $f$가 유도하는 $A \rightarrow E$는 국소사상이므로 $\mathfrak{m}_yE\subseteq \mathfrak{m}_x$를 만족한다. 이제 $M=E$로 두면 $M$은 finitely generated $E$-가군이므로 [\[가환대수학\] §평탄성과 국소화, ⁋정리 1](/ko/math/commutative_algebra/local_criterion_for_flatness#thm1)의 가정이 모두 충족되며, 그 결론이 정확히 주장하는 동치이다.
:::

평탄한 점들의 집합이 $X$의 열린집합을 이룬다는 사실 또한 성립한다. 즉 $f$가 locally of finite presentation이면 평탄 영역은 열린집합이며, 이는 [명제 11](#prop11)을 $X$ 쪽에서 본 형태에 해당한다. 그러나 그 증명은 Fitting ideal에 대한 별도의 이론을 필요로 하므로 여기에서는 다루지 않고 **[EGA]** IV.11.1.1과 [\[Stacks\] Tag 00RC](https://stacks.math.columbia.edu/tag/00RC)를 인용하는 데에 그친다.

또한 smooth한 사상은 그 정의에 평탄성을 직접 조건으로 포함하므로 언제나 평탄이다. ([§매끄러운 사상과 étale 사상](/ko/math/scheme_theory/smooth_and_etale_morphisms))

::: 예시 20
양수 특성 $p > 0$인 체 $\mathbb{K}$ 위의 scheme $X$에 대하여, *Frobenius 사상<sub>프로베니우스 사상</sub>*

$$F: X \longrightarrow X$$

은 구조층 위에서 $p$제곱사상 $a \mapsto a^p$을 유도한다. Kunz의 정리에 의하면 $X$가 regular인 것과 $F$가 평탄인 것은 서로 동치이다. 따라서 $X$가 singular point를 가지면 Frobenius 사상은 평탄이 아니며, 예를 들어 $X = \Spec \mathbb{K}[\x, \y]/(\x\y)$의 node에서 $F$는 평탄하지 않다. 이는 지금까지 본 판정법들과는 성격이 다른데, 여기에서는 평탄성이 family의 성질이 아니라 $X$ 자체의 regularity를 재고 있다.
:::

---

**참고문헌**

**[Har]** R. Hartshorne, *Algebraic geometry*, Springer, 1977.

**[Stacks]** The Stacks Project Authors, *Stacks Project*, https://stacks.math.columbia.edu.

**[EGA]** A. Grothendieck, *Éléments de géométrie algébrique*, IHES, 1960–1967.

**[Mats]** H. Matsumura, *Commutative ring theory*, Cambridge University Press, 1986.
