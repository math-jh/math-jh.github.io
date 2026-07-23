---
title: "스킴의 위상구조"
description: "스킴의 위상 구조에서 닫힌점, 일반점, 특수화 개념을 정의하고, 아핀 스킴의 점들이 아이디얼과 어떤 관계를 맺으며 위상적 성질을 나타내는지 살펴본다."
excerpt: "Generic point와 Zariski topology, irreducible component"

categories: [Math / Scheme Theory]
permalink: /ko/math/scheme_theory/topology_of_schemes
sidebar: 
    nav: "scheme_theory-ko"

date: 2025-02-03
weight: 6
---

## 일반점

이제 우리는 scheme이 갖는 위상적인 구조를 살펴볼 것이다. 가장 특이한 것 중 하나는 한점집합이 닫힌집합이 아닐 수도 있다는 것이다. 


::: 정의 1
위상공간 $X$의 한 점 $x$가 *closed point<sub>닫힌점</sub>*이라는 것은 $\{x\}$가 $X$의 닫힌집합이라는 것이다.
:::

따라서 공간 $X$가 $T_1$-space인 것과 $X$의 모든 점이 closed point인 것이 동치임을 안다. ([\[위상수학\] §하우스도르프 공간, ⁋정의 3](/ko/math/topology/Hausdorff_spaces#def3)) [§스킴, ⁋예시 7](/ko/math/scheme_theory/schemes#ex7)에서 보았듯 classical algebraic geometry에서는 maximal ideal들만 생각하였으므로, 이러한 maximal ideal $\mathfrak{m}$에 대해서는 $Z(\mathfrak{m})=\{\mathfrak{m}\}$이고, 따라서 [§스펙트럼, ⁋명제 14](/ko/math/scheme_theory/spectrums#prop14)과 [\[집합론\] §필터와 아이디얼, 갈루아 대응, ⁋명제 7](/ko/math/set_theory/filter_and_ideal#prop7)을 적용하면

$$\cl(\{\mathfrak{m}\})=ZI(\{\mathfrak{m}\})=ZIZ(\mathfrak{m})=Z(\mathfrak{m})=\{\mathfrak{m}\}$$

이 되어, 모든 점이 closed point가 되었다. 그러나 field가 아닌 integral domain의 spectrum을 생각하면 이는 maximal ideal $\mathfrak{m}\neq 0$을 가지는 동시에 integral domain의 정의에 의하여 $0$이 prime ideal이 되므로, 이러한 scheme은 closed point가 아닌 점을 갖는다. 

우리의 첫째 목표는 이러한 점을 직관적으로 이해하는 것이다. 

::: 정의 2
위상공간 $X$의 두 점 $x,y$가 $x\in\cl(\{y\})$를 만족한다 하자. 그럼 $x$를 $y$의 *specialization<sub>특수화</sub>*이라 하고, $y$는 $x$의 *generization<sub>일반화</sub>*이라 한다. 만일 위상공간 $X$의 닫힌집합 $C$에 대하여, $C=\cl(\{x\})$가 성립한다면 $x$를 $C$의 *generic point<sub>일반점</sub>*라 부른다. 
:::

그럼 정의에 의하여, $x$가 $C$의 generic point라면 임의의 점 $y\in C$와 그 열린근방 $U$에 대하여 $U$는 항상 $x$를 포함한다. 따라서 generic point는 $C$의 모든 점에 가까운 점으로 생각할 수 있다.

이를 더욱 기하적으로 설명하면 다음과 같다. 예를 들어 $\mathbb{A}^n=\Spec\mathbb{K}[\x_1,\ldots, \x_n]$을 보자. 그럼 classical한 대수기하학에서 우리는 적당한 함수 $f$의 zero locus $Z(f)$가 $\mathbb{A}^n_\text{classical}$의 subscheme을 이룬다는 것을 안다. 

논리 전개의 편의상 $f$가 prime element여서, $f$가 생성하는 ideal $\mathfrak{p}_f=(f)$가 prime ideal이라 하자. 그럼 $\mathfrak{p}_f$는 우선 정의에 의해 $\mathbb{A}^n$의 (closed일 필요는 없는) 점이며, 바로 이 점이 $f$가 정의하는 closed subscheme의 generic point이다. 이 점은 $Z(f)$의 대부분의 정보를 담고 있는데, 가령 $Z(f)$에 포함된 (classical한) 점들을 얻기 위해서는 $\mathfrak{p}_f$에 closure를 취하여 $Z(f)$를 얻은 후 maximal ideal들만 택하면 되고, 대수적으로는 $\mathfrak{p}_f$를 포함하는 maximal ideal들을 모두 가져오면 된다. 

이 논증은 일반적인 $A$의 ideal $\mathfrak{a}$에 대해서도 확장된다. 즉, $Z(\mathfrak{a})$의 irreducible component들은 $\mathfrak{a}$를 포함하는 minimal prime ideal들에 일대일로 대응한다. ([\[가환대수학\] §으뜸분해, ⁋정리 3](/ko/math/commutative_algebra/primary_decomposition#thm3)) 이 때 각각의 minimal prime ideal들이 해당 component의 generic point에 대응되며 따라서 일반적인 경우도 component별로 위에서의 직관을 그대로 가져온 것이라 생각할 수 있다. 

## 스킴의 위상적 성질들

한편 scheme은 structure sheaf를 빼고 보면 그냥 위상공간이므로, 위상공간의 성질들을 가질 수 있다.

::: 정의 3
Scheme $(X,\mathcal{O}_X)$가 주어졌다 하자. 만일 $X$가 위상공간으로서 quasi-compact (resp. irreducible, connected)라면, $X$를 quasi-compact (resp. irreducible, connected) scheme이라 부른다. 
:::

위 정의에 해당하는 위상수학의 정의들은 각각 [\[위상수학\] §옹골공간, ⁋정의 1](/ko/math/topology/compact_spaces#def1), [\[위상수학\] §차원, ⁋정의 6](/ko/math/topology/dimension#def6)과 [\[위상수학\] §연결공간, ⁋정의 1](/ko/math/topology/connected_spaces#def1)에서 각각 찾아볼 수 있다.[^1] 다음은 이 정의에 대한 예시와 반례들이다. 

::: 예시 4
우리는 [§스펙트럼, ⁋보조정리 12](/ko/math/scheme_theory/spectrums#lem12)에 의해 임의의 affine scheme은 quasi-compact임을 안다. Quasi-compact가 아닌 scheme의 예시로는, 당연히 무한히 많은 scheme들의 disjoint union이 있다. 
:::

Irreducibility의 경우 다음 예시들을 보자. 

::: 예시 5
임의의 integral domain $A$에 대하여, $\Spec A$는 항상 irreducible이다. Generic point $\{0\}$을 생각하면, $\{0\}$를 포함하는 닫힌집합은 오직 $\Spec A$ 자신뿐이어야 하므로, $\Spec A$를 두 개의 proper closed subset의 합집합으로 나타내는 것이 불가능하기 때문이다. 따라서 $A=\mathbb{K}[\x_0,\ldots, \x_n]$으로 두면 affine $n$-space $\mathbb{A}_\mathbb{K}^n$은 irreducible인 것을 안다. 그럼 projective space $\mathbb{P}^n_\mathbb{K}$는 irreducible open subset들 $D_+(\x_i)$을 가지므로 [\[위상수학\] §차원, ⁋명제 8](/ko/math/topology/dimension#prop8)에 의해 $\mathbb{P}^n_\mathbb{K}$ 또한 irreducible이다. 

거꾸로 affine scheme $\Spec A$의 임의의 irreducible closed set $Z$는 항상 generic point $I(Z)$를 갖는다. ([§스펙트럼, ⁋명제 16](/ko/math/scheme_theory/spectrums#prop16)) 
:::

Irreducible space는 항상 connected이므로, 위의 예시들은 connected space의 예시이기도 하다. 다음 예시는 connected가 아닌 scheme과, connected이지만 irreducible이 아닌 scheme들의 예시를 위한 것으로, affine plane $\mathbb{A}^2_\mathbb{K}$의 특정한 *closed subscheme*들이 주어져 있다. 

우리는 아직 closed subscheme을 정의하지 않았으나, 적어도 [§스펙트럼, ⁋명제 9](/ko/math/scheme_theory/spectrums#prop9)에서 우리는 affine scheme $\Spec A$와 $A$의 임의의 ideal $\mathfrak{a}$에 대하여 canonical morphism $A \rightarrow A/\mathfrak{a}$을 통해 $\Spec A/\mathfrak{a}$와 $Z(\mathfrak{a})\subseteq \Spec A$가 위상공간으로서 homeomorphic한 것은 이미 살펴보았다. Connectedness와 irreducibility는 모두 위상공간의 성질이므로, $\Spec A/\mathfrak{a}$의 위상적인 성질은 $\Spec A$의 닫힌집합 $Z(\mathfrak{a})$의 위상구조를 살펴보아 확인할 수 있다. 이들을 closed subscheme이라 부를 때, 부족한 것은 오직 $\Spec A/\mathfrak{a}$의 structure sheaf와 $\Spec A$의 structure sheaf(를 $Z(\mathfrak{a})$로 제한한 것)이 어떤 관계에 있는지 뿐이며, 이는 [§닫힌 부분스킴](/ko/math/scheme_theory/closed_subschemes)에서 다시 살펴보게 된다. 

::: 예시 6
우선 connected가 아닌 scheme의 예시는 $\mathbb{A}^2_\mathbb{K}$의 closed subscheme 

$$\Spec \frac{\mathbb{K}[\x,\y]}{(\x(\x-1))}$$

이 있다. 이것이 connected가 아님을 보기 위해서는 이를 두 개의 subscheme $\Spec \mathbb{K}[\x,\y]/(\x)$와 $\Spec \mathbb{K}[\x,\y]/(\x-1)$의 disjoint union으로 쓸 수 있다는 것을 확인하면 된다. 

한편 connected이지만 irreducible하지 않은 scheme의 예시로는 

$$Z(\x\y)=\Spec \frac{\mathbb{K}[\x,\y]}{(\x\y)}$$

이 있으며, 이 scheme의 irreducible component는 $\Spec\mathbb{K}[\x,\y]/(\x)$와 $\Spec \mathbb{K}[\x,\y]/(\y)$이다. 

![counterexamples](/assets/images/Math/Scheme_Theory/Topology_of_Schemes-1.svg){:style="width:21.87em" class="invert" .align-center}

이들은 generic point의 관점에서도 설명할 수 있다. 앞서 우리는 함수 $f$가 정의하는 generic point는 $f$가 정의하는 ideal 그 자체라고 하였으며, 따라서, 예를 들어 $y$축을 나타내는 ideal $(\x)$가 바로 $y$축의 generic point이며, 비슷하게 $(\y)$는 $x$축을 나타내는 generic point이다. 문제는 위에서 살펴본 $Z(\x\y)$를 나타내는 ideal이 없다는 것으로, 두 축을 합집합하여 얻어지는 대상에 해당하는 ideal은 이들 두 ideal의 교집합에 포함되어야 할테지만 이 두 ideal의 교집합은 $(0)$ 뿐이며, 이는 전체 ring $\mathbb{K}[\x,\y]/(\x\y)$의 prime ideal이 <em-ko>아니다</em-ko>, 즉, $\mathbb{K}[\x,\y]/(\x\y)$는 integral domain이 아니며, 이는 $\x\y=0$임에도 $\x,\y\neq 0$이기 때문이다. 이 때 zero-divisor의 역할을 해 주는 $\x,\y$들은 각각 서로 다른 component에서 $0$이 되는 함수들로, 더 복잡한 scheme의 경우에서도 약간의 계산은 추가되지만 그 정신은 같은 원리로 나타나게 된다. 
:::

우리는 [\[위상수학\] §차원, ⁋정의 11](/ko/math/topology/dimension#def11)에서 위상공간이 noetherian이라는 개념을 정의하였다. 이를 scheme의 언어로 옮겨올 때에는 약간의 주의가 필요한데, 우선 affine scheme에 대해서는 다음 명제가 성립한다.

::: 명제 7
Noetherian ring $A$에 대하여, $\Spec A$는 항상 noetherian topological space이다. 
:::
::: 증명
$\Spec A$의 닫힌집합들의 chain

$$Z(\mathfrak{a}_1)\supseteq Z(\mathfrak{a}_2)\supseteq\cdots$$

이 주어졌다 하면, $A$의 ideal들의 chain

$$IZ(\mathfrak{a}_1)\subseteq IZ(\mathfrak{a}_2)\subseteq\cdots$$

을 얻고 이것은

$$\sqrt{\mathfrak{a}_1}\subseteq \sqrt{\mathfrak{a}_2}\subseteq\cdots$$

와 같다. 이제 $A$가 noetherian ring이라는 가정으로부터 적당한 $k$가 존재하여

$$\sqrt{\mathfrak{a}_k}=\sqrt{\mathfrak{a}_{k+1}}=\cdots$$

이 성립하고 따라서

$$Z(\sqrt{\mathfrak{a}_k})=Z(\sqrt{\mathfrak{a}_{k+1}})=\cdots$$

이다. 이제 [§스펙트럼, ⁋명제 5](/ko/math/scheme_theory/spectrums#prop5)로부터 원하는 결과를 얻는다.
:::

그러나 일반적으로 그 역은 성립하지 않는다. 즉 어떠한 affine scheme이 주어졌을 때, 이 scheme이 위상공간으로서 noetherian이더라도 이를 정의하는 ring은 noetherian이 아닐 수 있다. 

## 국소성

Scheme은 정의상 affine scheme들을 붙여서 얻어지는 대상이므로, 그 성질을 탐구하기 위해 선택하는 전략 중 하나는 어떠한 성질들을 local하게 탐구하는 것이다. 실제로 위에서 다룬 많은 예시가 affine scheme이었듯, 일반적인 scheme의 성질도 affine 조각을 이어붙여 다루는 것이 이 전략의 핵심이다. 뿐만 아니라, 이 접근방식의 장점은 우리의 affine scheme에 대한 이해가 위상적인 영역에만 국한되지는 <em-ko>않는다</em-ko>는 점에 있다. 즉, 이번 글에서 도입한 위상적인 데이터 뿐만 아니라, affine scheme $\Spec A$는 $A$가 ring으로서 가지는 대수적인 성질도 가지고 있으며, 이 국소성은 이러한 대수적인 성질들도 global하게 이어붙이는 데에 도움을 줄 것이다. 

이러한 상황에서 흥미롭게 동작하는 개념 중 하나는 noetherian property로, 이는 noetherian이라는 조건이 위상수학에서도, 대수학에서도 각각 정의되기 때문이며, 이것이 [명제 7](#prop7)을 도입하기 전에 지적한 ambiguity의 정체이다.

우리는 이번 글에서 local property를 정의하고, 이를 noetherian property에 적용하며 글을 마친다. 우선 ring의 성질이 local하다는 것이 어떤 의미인지 살펴보자.

::: 정의 8
Ring의 성질 $P_\alg$가 *local<sub>국소적</sub>*이라는 것은 다음의 두 조건이 성립하는 것이다.

1. 임의의 ring $A$와 $f\in A$에 대하여, 만일 $A$가 $P_\alg$를 만족한다면 $A_f$도 $P_\alg$를 만족한다.
2. 임의의 ring $A$와, $f_1,\ldots, f_n\in A$가 $A=(f_1,\ldots, f_n)$을 만족한다 하자. 그럼 만일 모든 $A_{f_i}$가 $P_\alg$를 만족한다면 $A$도 $P_\alg$를 만족한다. 
:::

이를 affine scheme의 언어로 바꾸어보자. Ring의 성질 $P_\alg$에 대하여, affine scheme $X=\Spec A$의 global section ring $\mathcal{O}_X(X)=A$가 $P_\alg$를 만족할 때 $X$가 성질 $P_\geo$를 갖는다고 하자. 그럼 $D(f)\cong\Spec A_f$이고, 또 $A=(f_1,\ldots, f_r)$이면

$$\Spec A=\Spec A\setminus Z(f_1,\ldots, f_r)=\Spec A\setminus\bigcap_{i=1}^r Z(f_i)=\bigcup_{i=1}^r D(f_i)$$

으로부터 $D(f_i)$들이 $\Spec A$를 덮는다는 것을 안다. 이를 사용하여 [정의 8](#def8)의 두 조건은 다음과 같이 번역된다.

1. $\Spec A$가 $P_\geo$를 만족한다면, 임의의 principal open set $D(f)$ 또한 $P_\geo$를 만족한다.
2. $\Spec A$를 덮는 open covering $D(f_1),\ldots, D(f_r)$가 각각 $P_\geo$를 만족한다면, $\Spec A$도 $P_\geo$를 만족한다. 

한편 $\Spec A$의 일반적인 open set은 principal open set들의 합집합으로 나타낼 수 있고 ([§스펙트럼, ⁋보조정리 11](/ko/math/scheme_theory/spectrums#lem11)), 따라서 $\Spec A$가 $P_\geo$를 만족하면 $\Spec A$의 임의의 *affine* open subset 또한 $P_\geo$를 만족한다. 이처럼 principal open set들로 검사하여 결정되는 성질을 *affine-local property*라 부르며, 이를 임의의 scheme의 affine subscheme들에 대한 성질로 일반화한 것이 다음 정의이다. 

::: 정의 9
Scheme $X$의 적당한 affine subscheme들에 대해 정의된 성질 $P$가 *affine-local property<sub>아핀-국소 성질</sub>*라는 것은 다음 두 조건이 성립하는 것이다. 

1. 만일 $\Spec A\subseteq X$가 $P$를 만족한다면, 임의의 $f\in A$에 대해 $\Spec A_f\subseteq X$ 또한 $P$를 만족한다.
2. 만일 $A=(f_1,\ldots, f_r)$이고 $\Spec A_{f_i}\subseteq X$가 모두 $P$를 만족한다면 $\Spec A \subseteq X$ 또한 $P$를 만족한다. 
:::

반면 우리는 [§스킴, ⁋예시 8](/ko/math/scheme_theory/schemes#ex8)에서 affine scheme의 open subscheme이 affine이 되지 않을 수 있다는 것을 이미 살펴보았으므로 $P$가 ring의 local property라고 하여도 이러한 식으로 정의한 성질 $P$는 진정한 의미에서 local한 성질이 아니다. 정말로 local한 성질을 살펴보기 위해서는 다음과 같이 정의하면 된다. 

::: 정의 10
Scheme의 affine-local property $P$에 대하여, scheme $(X, \mathcal{O}_X)$가 *locally $P$*라는 것은 임의의 $x\in X$마다 적절한 open affine neighborhood $U$가 존재하여 $X$의 affine open subscheme $U$가 $P$를 만족하는 것이다. 
:::

그럼 [보조정리 12](#lem12)에서 우리는 scheme $X$가 locally $P$라면, $X$의 임의의 open subscheme이 locally $P$라는 것을 보인다. 우선 다음 보조정리를 보이자.

::: 보조정리 11 (Nike)
Scheme $X$와 임의의 affine open subset $U,V$가 주어졌다 하자. 그럼 임의의 $x\in U\cap V$에 대하여, 적당한 $x\in W\subseteq U\cap V$가 존재하여 $W$가 $U$와 $V$ 모두에서 principal open subset이도록 할 수 있다. 
:::
::: 증명
표기를 위해 $U=\Spec A$, $V=\Spec B$라 하고, $x$가 이들 각각에서 prime ideal들 $\mathfrak{p}\subset A$, $\mathfrak{q}\subset B$에 대응된다 하자. 그럼 우선 $U\cap V$를 $U$의 열린집합으로 보아 [§스펙트럼, ⁋보조정리 11](/ko/math/scheme_theory/spectrums#lem11)를 적용하면 $U$의 principal open set $D(f)$를 택하여

$$\mathfrak{p}\in D(f)\subseteq U\cap V$$

이도록 할 수 있다. 이 때, $D(f)\cong \Spec A_f$이므로 inclusion $D(f)\hookrightarrow V$는 ring homomorphism $i:B \rightarrow A_f$로부터 얻어진다. 

한편, 이제 $D(f)\cong\Spec A_f$를 $V$의 열린집합으로 보면 다시 $V$의 principal open set $D(g)$가 존재하여

$$\mathfrak{q}\in D(g)\subseteq D(f)\cap V$$

이도록 할 수 있다. 이제 $\Spec B$의 open subscheme $D(g)$와, $\Spec A$의 open subscheme $D(i(g))$이 서로 같다는 것을 확인하면 된다. 
:::

::: 보조정리 12
Scheme $X$와 scheme의 affine-local property $P$에 대하여 다음이 모두 동치이다.

1. $X$가 locally $P$이다.
2. $X$의 임의의 affine open subset $U\subseteq X$에 대하여, $X$의 open subscheme $U$가 $P$를 만족한다.
3. $X$의 적당한 affine open covering $\{U_i\}$가 존재하여 $X$의 open subscheme $U_i$가 모두 $P$를 만족한다.
4. $X$의 적당한 open covering $\{U_i\}$가 존재하여, 각각의 open subscheme $(U_i, \mathcal{O}_X\vert_{U_i})$가 locally $P$이다.

특히, 만일 $X$가 locally $P$라면 $X$의 임의의 open subscheme이 locally $P$이다. 
:::
::: 증명
첫째 조건이 성립한다면 각각의 $x$마다 open affine neighborhood $U_x$가 존재한다. 따라서 $\{U_x\}_{x\in X}$가 셋째 조건에서 요구하는 $X$의 affine open covering이 된다. 거꾸로 셋째 조건에 의해 주어지는 affine open covering $\{U_i\}$가 주어진다면, $X$의 임의의 점 $x$가 주어질 때마다 $x\in U_i$를 만족하는 $U_i$를 택할 수 있고, 이렇게 얻어지는 $U_i$가 [정의 9](#def9)에서 요구하는 $x$의 open affine neighborhood가 된다. 따라서 첫째 조건과 셋째 조건은 동치이다. 또, 둘째 조건이 첫째 조건을 함의하는 것은 자명하다. 

이제 셋째 조건이 성립한다 가정하고 둘째 조건이 성립함을 보인다. 셋째 조건을 만족하는 $X$의 affine open covering $\{U_i=\Spec A_i\}$가 주어졌다 하자. 그럼 $X$의 임의의 affine open subset $V=\Spec A$에 대하여, 각각의 $V\cap U_i$들은 $V$의 열린집합이기도 하므로 [보조정리 11](#lem11)로부터 

$$V=\bigcup_{i\in I} V\cap U_i=\bigcup_{i\in I} \bigcup_{j\in J_i} \Spec (A_i)_{f_j}$$

를 만족하는 $f_j\in A_i$들을 찾을 수 있고, $\Spec (A_i)_{f_j}$들 각각은 $\Spec A$의 적당한 localization $\Spec A_{g_j}$들로 둘 수 있다는 것을 알고 [§스펙트럼, ⁋보조정리 12](/ko/math/scheme_theory/spectrums#lem12)를 사용하면 $g_j$들이 유한하게 주어졌다 가정할 수 있다. 이제 [정의 9](#def9) 이전의 논의로부터 $P$가 local이라는 가정으로부터 각각의 $\Spec (A_i)_{f_j}=\Spec A_{g_j}$가 $P$를 만족하는 것을 알고, 이로부터 $\Spec A$가 $P$를 만족하는 것을 안다.

이상에서 첫째 조건부터 셋째 조건이 모두 동치임을 안다. 

이제 $X$가 locally $P$라 하고, $U$가 $X$의 임의의 open subscheme이라 하자. 그럼 임의의 $x\in U$에 대하여, [§스펙트럼, ⁋보조정리 11](/ko/math/scheme_theory/spectrums#lem11)로부터 $x\in D(f)\subseteq U$를 만족하는 $X$의 affine open subset $D(f)$를 잡을 수 있고 이제 둘째 조건으로부터 $D(f)$가 $P$를 만족하는 affine scheme인 것을 안다. 따라서 scheme $U$ 또한 locally $P$가 되어 마지막 주장을 얻는다. 마지막으로 넷째 조건과 나머지 조건이 동치인 것은 이 주장을 사용하여 둘째 조건과 셋째 조건에서 affine이라는 가정만 빼면 얻어진다. 
:::

한편 우리는 [명제 7](#prop7)에서 noetherian ring $A$에 대하여 $\Spec A$가 noetherian space임을 보았다. 이제 임의의 scheme $X$에 대하여 $X$가 noetherian인 것이 무엇인지를 정의하자.

::: 보조정리 13
Ring $A$가 noetherian인 것은 local property이고, 따라서 affine-local property $P$를 정의한다. 
:::
::: 증명
[정의 8](#def8)의 두 조건을 증명해야 한다. 

첫째 조건은 [\[가환대수학\] §국소화, ⁋따름정리 9](/ko/math/commutative_algebra/localization#cor9)로부터 얻어지며, 혹은 [\[위상수학\] §차원, ⁋명제 13](/ko/math/topology/dimension#prop13)의 첫째 결과를 사용해도 충분하다.

둘째 조건을 보자. $A=(f_1,\ldots, f_r)$이고 각 $A_{f_i}$가 noetherian이라 가정한 뒤, $A$의 임의의 ideal $\mathfrak{a}$가 finitely generated임을 보이면 된다. 각 $i$에 대하여 $A_{f_i}$가 noetherian이므로 ideal $\mathfrak{a}A_{f_i}$는 finitely generated이며, generator들의 분모를 없애면 $\mathfrak{a}$의 원소 $a_{i1},\ldots, a_{in_i}$이 존재하여 이들의 상이 $\mathfrak{a}A_{f_i}$를 생성하게 할 수 있다. 이제 이 유한개의 원소들 전체가 생성하는 ideal을 $\mathfrak{b}\subseteq \mathfrak{a}$라 하면, 구성에 의하여 모든 $i$에 대해 $\mathfrak{b}A_{f_i}=\mathfrak{a}A_{f_i}$이다.

이제 $\mathfrak{a}=\mathfrak{b}$임을 보이면 된다. Localization이 완전함수이므로 $M=\mathfrak{a}/\mathfrak{b}$는 모든 $i$에 대하여 $M_{f_i}=0$을 만족한다. 임의의 $m\in M$을 잡으면 각 $i$마다 $f_i^{n}m=0$이 되는 $n$이 존재하고, $i$가 유한개이므로 충분히 큰 $n$ 하나를 공통으로 잡을 수 있다. 한편 $D(f_i)=D(f_i^n)$이므로 $D(f_i^n)$들 또한 $\Spec A$를 덮고, 따라서 $f_1^n,\ldots, f_r^n$은 unit ideal을 생성하여 $1=\sum_{i=1}^r g_if_i^n$인 $g_i\in A$가 존재한다. 그럼

$$m=\sum_{i=1}^r g_if_i^nm=0$$

이므로 $M=0$, 곧 $\mathfrak{a}=\mathfrak{b}$가 finitely generated이다.
:::

::: 정의 14
Scheme $X$가 *locally noetherian scheme<sub>국소뇌터스킴</sub>*인 것은 $A_i$가 모두 noetherian인 $X$의 affine open covering $\{U_i=\Spec A_i\}$가 존재하는 것이다. 만일 $X$가 quasi-compact locally noetherian scheme이라면 이를 *noetherian scheme<sub>뇌터스킴</sub>*이라 부른다. 
:::

그럼 만일 $A$가 noetherian이라면 $\Spec A$가 noetherian scheme인 것은 정의와 [§스펙트럼, ⁋보조정리 12](/ko/math/scheme_theory/spectrums#lem12)로부터 자명하다. 또, [명제 7](#prop7)과 마찬가지로 임의의 noetherian scheme은 위상공간으로서 noetherian이다. 그러나 [명제 7](#prop7) 이후에 지적했듯, scheme $X$가 위상공간으로서 noetherian이라 해서 위의 조건이 성립하는 것은 아니라는 것에 주의해야 한다.

마지막으로 우리는 [정의 9](#def9)와는 조금 다른 국소성의 개념을 정의하는데, *stalk-local*의 개념이 그것이다. 

::: 정의 15
Scheme $X$의 성질 $P$가 *stalk-local<sub>줄기-국소</sub>*이라는 것은 각각의 $x\in X$에 대하여 ring $\mathcal{O}_{X,x}$가 ring의 성질 $Q$를 만족하는 것이다. 
:::

그럼 다음이 성립한다.

::: 명제 16
Scheme $X$의 stalk-local property $P$에 대하여, 다음이 모두 동치이다.

1. $X$가 $P$를 만족한다.
2. $X$의 임의의 open subscheme이 $P$를 만족한다.
3. $X$의 임의의 affine open subscheme이 $P$를 만족한다. 
4. $X$의 affine open cover $\{U_i\}$를 택하여 각각의 open subscheme들 $U_i$가 $P$를 만족하도록 할 수 있다. 
5. $X$의 open cover $\{U_i\}$를 택하여 각각의 open subscheme들 $U_i$가 $P$를 만족하도록 할 수 있다.  
:::
::: 증명
우선 $2\implies 3\implies 4\implies 5$임은 자명하므로, $5\implies 1$ 그리고 $1\implies 2$만 보이면 충분하며, 이들은 다음의 isomorphism

$$\mathcal{O}_{X,x}= \varinjlim_{V\ni x} \mathcal{O}_X(V)\cong \varinjlim_{V\ni x, V\subseteq U}\mathcal{O}_X(V)=\mathcal{O}_{U, x}$$

으로부터 자명하다. 
:::

특히 임의의 stalk-local property는 affine-local property이기도 하다. 그러나 이는 다소 주의할 필요가 있는 명제인데, 이는 가령 $X$ 위의 stalk-local property가

$$\text{$X$ is $P$}\iff \text{$\mathcal{O}_{X,x}$ satisfies $Q$}$$

로 주어졌을 때, 임의의 affine open subset $U$에 대하여 $\mathcal{O}_X(U)$가 $Q$를 만족한다는 것이 <em-ko>아니라</em-ko>, 임의의 affine open subset $U$와 원소 $x\in U$에 대하여 $\mathcal{O}_{U,x}$가 성질 $Q$를 만족하고 따라서 affine open subscheme $U$가 성질 $P$를 만족한다는 것이다. 

가령 다음의 affine scheme

$$X=\Spec A=\Spec\left(\prod_{i=1}^\infty \mathbb{Z}/2\mathbb{Z}\right)$$

을 생각하면 $A$의 임의의 원소 $x$는 $x^2=x$를 만족하고, 따라서 임의의 localization $A_\mathfrak{p}$의 원소도 그러하다. 이제 $A_{\mathfrak{p}}$에서 성립하는 $x(1-x)=0$으로부터 우리는 $x\in \mathfrak{p}A_\mathfrak{p}$이거나 $1-x\in \mathfrak{p}A_\mathfrak{p}$임을 알고, $\mathfrak{p}A_\mathfrak{p}$에 속하지 않는 원소는 unit임을 안다. ([\[가환대수학\] §국소화, ⁋명제 2](/ko/math/commutative_algebra/localization#prop2)) 따라서 $x=0$ 혹은 $x=1$이므로 $A_\mathfrak{p}$의 ideal의 chain은 $(0)\subseteq (1)=A_\mathfrak{p}$ 뿐이다. 이로부터 $A_\mathfrak{p}$ 각각은 noetherian이지만, 

$$\mathbb{Z}/2\mathbb{Z}\times \{0\}\times\{0\}\times\cdots\subseteq \mathbb{Z}/2\mathbb{Z}\times \mathbb{Z}/2\mathbb{Z}\times\{0\}\subseteq\cdots$$

을 생각하면 $A$는 noetherian이 아니라는 것을 알 수 있다. 

---
**참고문헌**

**[Har]** R. Hartshorne, *Algebraic geometry*. Graduate texts in mathematics. Springer, 1977.  
**[Vak]** R. Vakil, *The rising sea: Foundation of algebraic geometry*. Available [online](https://math.stanford.edu/~vakil/216blog/).  

---

[^1]: 우리는 [§스펙트럼, ⁋보조정리 11](/ko/math/scheme_theory/spectrums#lem11) 이후에 (Hausdorff가 아닐 수 있는) compact한 위상공간을 *quasi-compact*라 부르기로 하였다. 