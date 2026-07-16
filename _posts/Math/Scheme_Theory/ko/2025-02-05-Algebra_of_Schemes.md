---
title: "스킴의 대수구조"
description: "스킴의 대수적 구조를 다루며, 축소스킴과 정역스킴의 정의 및 성질을 살펴보고 reducedness가 stalk-local property임을 증명한다. 정역스킴은 불가분 축소스킴과 동치인 것을 보인다."
excerpt: "Reduced scheme과 integral scheme의 정의와 성질"

categories: [Math / Scheme Theory]
permalink: /ko/math/scheme_theory/algebra_of_schemes
sidebar: 
    nav: "scheme_theory-ko"

date: 2025-02-05
weight: 7
published: false
drift_needed: true
---

스킴은 기하적인 동시에 대수적인 대상이므로, 이를 잘 알기 위해서는 앞선 글에서 살펴본 스킴의 위상구조 뿐만 아니라 대수적인 구조도 동시에 고려할 필요가 있으며, 우리는 이전 글에서 이러한 철학이 어떻게 반영되는지를 간략하게 살펴보았다. 이번 글에서는 이 철학을 더욱 발전시킨다. 

## 축소스킴과 정역스킴

::: 정의 1
Scheme $X$가 *reduced scheme<sub>축소스킴</sub>*인 것은 임의의 열린집합 $U$에 대하여 $\mathcal{O}_X(U)$가 reduced인 것이다. ([\[대수적 구조\] §분수체, ⁋정의 11](/ko/math/algebraic_structures/field_of_fractions#def11)) 비슷하게, $X$가 *integral<sub>정역스킴</sub>*인 것은 임의의 열린집합 $U$에 대하여 $\mathcal{O}_X(U)$가 integral domain인 것이다. ([\[대수적 구조\] §분수체, ⁋정의 5](/ko/math/algebraic_structures/field_of_fractions#def5))
:::

그럼 다음이 성립한다.

::: 보조정리 2
Scheme $X$가 reduced scheme인 것은 임의의 $x\in X$에 대하여 $\mathcal{O}_{X, x}$가 reduced ring인 것과 동치이다.
:::
::: 증명
우선 reduced scheme $X$의 임의의 점 $x\in X$에 대하여, $x$를 포함하는 affine open subscheme $U=\Spec A$를 생각하자. $\Spec A$ 안에서 $x$에 대응되는 prime ideal을 $\mathfrak{p}$라 하면

$$\mathcal{O}_{X,x}=(\mathcal{O}_X\vert_U)_x\cong \mathcal{O}_{\Spec A, \mathfrak{p}}\cong A_\mathfrak{p}$$

이고, 가정에 의해 $\mathcal{O}_X(U)\cong A$가 reduced이므로 $A_\mathfrak{p}$ 또한 reduced이다. 

거꾸로 임의의 $x\in X$에 대하여 $\mathcal{O}_{X,x}$가 reduced라 하면, 임의의 열린집합 $U$에 대하여 다음 inclusion

$$\mathcal{O}_X(U)\hookrightarrow\prod_{x\in U} \mathcal{O}_{X,x}$$

을 생각하면 $\mathcal{O}_X(U)$가 reduced인 것을 확인할 수 있다. 
:::

이로부터 reducedness는 stalk-local property인 것을 안다. ([§스킴의 위상구조, ⁋명제 16](/ko/math/scheme_theory/topology_of_schemes#prop16)) 또, 만일 ring $A$가 reduced라면 그 localization도 reduced임을 쉽게 보일 수 있으므로, reduced ring의 spectrum은 reduced라는 것을 보일 수 있다. 

비슷하게 integral domain의 spectrum은 integral scheme이다. 이는 직접 보이는 것도 어렵지 않지만, [명제 4](#prop4)에서 우리는 scheme $X$가 integral인 것과, scheme $X$가 irreducible, reduced scheme인 것이 동치인 것을 증명한다. 그럼 integral domain $A$의 spectrum $\Spec A$는

1. $A$가 reduced ring이므로 reduced scheme이고,
2. $A$가 유일한 minimal prime ideal $\{0\}$을 가지므로 irreducible이다.

즉, 이를 받아들인다면 integral domain의 spectrum이 integral scheme이라는 것을 볼 수 있다. 

[명제 4](#prop4)의 증명을 위해서는 irreducibility를 다음과 같이 대수적인 언어로 풀어쓰는 것이 좋다.

::: 보조정리 3
Affine scheme $\Spec A$가 irreducible인 것은 nilradical $\mathfrak{N}(A)$가 prime ideal인 것과 동치이다.
:::
::: 증명
$\Spec A$가 irreducible인 것은 이 공간의 임의의 두 basis $D(f),D(g)\neq\emptyset$에 대하여 $D(fg)\neq\emptyset$인 것과 동치이다. 그런데 다음 동치관계

$$D(f)\neq\emptyset\iff f\not\in \mathfrak{p}\text{ for some $\mathfrak{p}$}\iff f\not\in \mathfrak{N}(A)$$

로부터, ([\[대수적 구조\] §분수체, ⁋명제 14](/ko/math/algebraic_structures/field_of_fractions#prop14)) 명제 $D(f),D(g)\neq\emptyset\implies D(fg)\neq\emptyset$은 다음 명제

$$f,g\not\in \mathfrak{N}(A)\implies fg\not\in \mathfrak{N}(A)$$

와 동치임을 안다. 
:::

이제 다음을 얻는다. 

::: 명제 4
$X$가 integral인 것과, $X$가 reduced, irreducible인 것이 동치이다.
:::
::: 증명
우선 $X$가 integral이라 하자. 임의의 integral domain은 항상 reduced이므로 $X$는 reduced scheme이다. 만일 $X$가 irreducible scheme이 아니라 하면, 서로소이고 공집합이 아닌 두 열린집합 $U_1,U_2\neq\emptyset$가 존재한다. 그럼 열린집합 $U_1\cup U_2$에 대하여

$$\mathcal{O}_X(U_1\cup U_2)=\mathcal{O}_X(U_1)\times \mathcal{O}_X(U_2)$$

이고, 우변은 integral domain이 아니므로 이는 $X$가 integral이라는 가정에 모순이다.

거꾸로 irreducible reduced scheme $X$가 주어졌다 하고, $X$가 integral scheme임을 보이자. 즉, $X$의 임의의 열린집합 $U$가 주어졌을 때, $\mathcal{O}_X(U)$가 integral domain임을 보여야 한다. 우선 다음 주장을 보이자.

> **주장.** 임의의 affine open subset $\Spec A\cong V\subseteq X$에 대하여, $\mathcal{O}_X(V)\cong A$는 항상 integral domain이다.  
> **증명.** $X$가 reduced라는 가정으로부터 $A$가 reduced ring이어야 하는 것을 안다. 한편, $X$는 $X$의 irreducible closed subset이므로 $V$도 irreducible이고 ([\[위상수학\] §차원, ⁋명제 14](/ko/math/topology/dimension#prop14)) 따라서 [보조정리 3](#lem3)으로부터 $\mathfrak{N}(A)=0$는 prime ideal이 되어 $A$가 integral domain이다. 

이제 일반적으로 $X$의 임의의 열린집합 $U$에 대하여 $\mathcal{O}_X(U)$가 integral domain임을 보인다. 이를 위해 두 원소 $f,g\in \mathcal{O}_X(U)$가 $fg=0$을 만족한다고 하자. 그럼 $U$의 두 열린집합

$$D_U(f)=\{x\in U\mid f_x\not\in \mathfrak{m}_x\},\qquad D_U(g)=\{x\in U\mid g_x\not\in \mathfrak{m}_x\}$$

와 이들의 여집합 $Z_U(f), Z_U(g)$에 대하여 $U=Z_U(f)\cup Z_U(g)$가 성립한다. 이제 $X$가 irreducible이므로, [\[위상수학\] §차원, ⁋명제 14](/ko/math/topology/dimension#prop14)으로부터 그 열린집합 $U$ 또한 마찬가지라는 것을 알고 따라서 $Z_U(f)=U$이거나 $Z_U(g)=U$여야 한다. 일반성을 잃지 않고 $Z_U(f)=U$라 하자. 그럼 $U$의 임의의 open affine subset $V$에 대하여, $V$에서

$$D_V(f)=\{x\in V\mid f_x\not\in \mathfrak{m}_x\}$$

로 정의하면 $D_V(f)=D_U(f)\cap V$이고, 이것이 공집합이기 위해서는 $f\vert_V$가 $\mathcal{O}_X(V)$의 nilpotent element이다. 그런데 $\mathcal{O}_X(V)$는 위의 주장에 의하여 integral domain이므로, 이로부터 $f\vert_V=0$이어야 함을 알고, 이것이 $U$의 임의의 open affine subset $V$에 대해 성립하므로 $f=0$이어야 한다. 
:::

한편 [§스킴의 위상구조, ⁋예시 6](/ko/math/scheme_theory/topology_of_schemes#ex6)을 보면, 임의의 scheme $X$의 irreducibility를 stalk만 보아서는 판단할 수 없다는 것을 안다. 가령 $Z(\x(\x-1))$는 두 개의 component로 쪼개지므로 각 component의 점은 다른 component의 점에 대한 정보를 알지 못한다. 따라서 integrality 또한 stalk만 보아서는 판단하지 못한다. 

그러나 만일 $X$가 *connected* scheme이었다면, irreducible component들은 반드시 어떠한 점에서는 만나야 하고, 이 점에서의 stalk을 보면 irreducibility를 판단할 수도 있을 것이다. 다음 명제는 이 아이디어를 엄밀하게 적은 것이다. 


::: 명제 5
Noetherian scheme $X$가 integral인 것과, $X$가 nonempty, connected이고 각각의 $\mathcal{O}_{X,x}$가 integral domain인 것이 동치이다. 
:::
::: 증명
우선 $X$가 integral이라면 $X$는 irreducible이므로 connected이고, 또 integral domain의 localization은 integral domain이므로 한쪽 방향은 자명하다.

반대쪽 방향의 경우, scheme $X$가 reduced인 것은 임의의 integral domain이 reduced이고, reducedness가 stalk-local property이기 때문에 자명하다. 따라서 주어진 조건을 사용하여 $X$가 irreducible이라는 것을 보이면 나머지는 [명제 4](#prop4)로부터 자명하다.

우선 $X$가 noetherian scheme이므로 적당한 noetherian ring들 $A_1,\ldots, A_r$이 존재하여 $X=\bigcup \Spec A_i$라 할 수 있다. 또, $X$는 위상공간으로서 noetherian이고, 따라서 [\[위상수학\] §차원, ⁋명제 13](/ko/math/topology/dimension#prop13)에 의하여 $X$는 유한히 많은 irreducible component를 갖는다. 이제

$$X=\bigcup_{j=1}^s X_j\tag{$\ast$}$$

가 $X$를 irreducible component들로 분해한 것이라 하면, 고정된 $i$에 대하여 다음 집합들

$$X_1\cap \Spec A_i,\quad X_2\cap \Spec A_i,\quad\ldots,\quad X_s\cap \Spec A_i$$

중 공집합이 아닌 것들은 $\Spec A_i$의 irreducible component들이 된다. 이제 [§스펙트럼, ⁋명제 16](/ko/math/scheme_theory/spectrums#prop16)에 의하여, 이들 각각은 minimal prime ideal $\mathfrak{q}_j=I(X_j)$를 정의하며 거꾸로 $A_i$의 임의의 minimal prime ideal은 irreducible component $X_j\cap \Spec A_i$를 유일하게 결정한다. 

한편, $X$는 connected이므로, irreducible decomposition ($\ast$)에서 다음의 교집합

$$X_1\cap \bigcup_{j=2}^s X_j$$

를 생각하면 이는 $X$의 공집합이 아닌 두 열린집합들의 교집합이고, $X$가 connected이므로 이들은 반드시 어떠한 점 $x$에서 만나야 한다. 즉, 적당한 $j$가 존재하여 $x\in X_1\cap X_j$이다. 이제 점 $x$를 포함하는 $X$의 affine cover를 $\Spec A_i$라 하고, 이 때 $x$가 prime ideal $\mathfrak{p}$에 대응된다 하자. 즉

$$x\in \Spec A_i\cap X_1\cap X_j=(\Spec A_i\cap X_1)\cap (\Spec A_i\cap X_j)$$

이다. 이제 앞선 논증으로부터 $\Spec A_i\cap X_1$은 generic point $\mathfrak{q}_1$을, $\Spec A_i\cap X_j$는 generic point $\mathfrak{q}_j$를 가지며, 이들은 $A_i$의 minimal prime ideal이다. 이제 $x$에서의 stalk $\mathcal{O}_{X,x}\cong (A_i)_\mathfrak{p}$를 생각하자. $x$가 $X_1$과 $X_j$ 모두에 속하므로 $\mathfrak{q}_1,\mathfrak{q}_j\subseteq \mathfrak{p}$이고, 따라서 [\[가환대수학\] §국소화, ⁋명제 8](/ko/math/commutative_algebra/localization#prop8)에 의하여 $\mathfrak{q}_1(A_i)_\mathfrak{p}$와 $\mathfrak{q}_j(A_i)_\mathfrak{p}$는 $(A_i)_\mathfrak{p}\cong\mathcal{O}_{X,x}$의 서로 다른 minimal prime ideal이 된다. 그런데 integral domain은 유일한 minimal prime ideal $(0)$을 가지므로 이는 $\mathcal{O}_{X,x}$가 integral domain이라는 가정에 모순이다.
:::

위의 증명에서 핵심적인 논리는 

1. $X$가 connected이므로, $X$를 irreducible component들로 분해하면 각각의 irreducible component는 다른 irreducible component와 반드시 만나야 하고[^1]
2. 두 irreducible component가 만나는 점을 $x$라 하고 $x$의 임의의 열린집합을 잡으면 이 열린집합은 각각의 irreducible component의 generic point를 포함할 것이며 ([§스펙트럼, ⁋명제 16](/ko/math/scheme_theory/spectrums#prop16)),
3. 따라서 이들 generic point들은 $x$에서의 stalk $\mathcal{O}_{X,x}$에서도 살아있지만, 이것은 $\mathcal{O}_{X,x}$가 integral domain이므로 불가능하다.

는 것으로 요약할 수 있다. 이 generic point에 대한 성질은 이 글의 마지막에서 살펴본다. 

## 정규스킴

Integral scheme과 비슷하게 다음을 정의할 수 있다.

::: 정의 6
Scheme $X$가 *normal<sub>정규스킴</sub>*인 것은 임의의 $x\in X$에 대하여 $\mathcal{O}_{X,x}$가 normal domain인 것이다. ([\[가환대수학\] §정수적 확장, ⁋정의 3](/ko/math/commutative_algebra/integral_extension#def3))
:::

일반적으로 normal domain의 localization은 항상 normal domain이다. ([\[가환대수학\] §정수적 확장, ⁋명제 12](/ko/math/commutative_algebra/integral_extension#prop12)) 이로부터 normal domain $A$의 스펙트럼 $\Spec A$는 normal scheme인 것을 안다. 

임의의 integral domain은 항상 reduced이고, [보조정리 2](#lem2)로부터 reducedness는 stalk에서 확인할 수 있으므로 임의의 normal scheme은 reduced이다. 반면 integral scheme이 되는 것은 stalk-local property가 아니므로 일반적으로 normal scheme이 항상 integral scheme이 되는 것은 아니다. 그러나 만일 $X$가 connected, nonempty Noetherian scheme이라면 [명제 5](#prop5)에 의해 normality가 integrality를 함의하는 것을 안다. 

한편, 우리는 unique factorization domain은 항상 normal domain인 것을 안다. ([\[가환대수학\] §정수적 확장, ⁋명제 9](/ko/math/commutative_algebra/integral_extension#prop9)) 이로부터 다음을 정의한다.

::: 정의 7
Scheme $X$가 *factorial<sub>인수분해스킴</sub>*인 것은 임의의 $x\in X$에 대하여 $\mathcal{O}_{X,x}$가 unique factorization domain인 것이다.
:::

따라서 임의의 factorial scheme은 normal scheme이다. 또, unique factorization domain의 localization은 unique factorization domain이므로 unique factorization domain $A$의 spectrum $\Spec A$는 factorial이다. 

## 동반소아이디얼

우리는 [§스펙트럼, ⁋따름정리 17](/ko/math/scheme_theory/spectrums#cor17)에 의해, scheme $X=\Spec A$의 irreducible component와 ring $A$의 minimal prime ideal 사이의 일대일대응이 존재하는 것을 안다. 이는 위의 [명제 5](#prop5)에서 중요하게 사용되었다.

한편 대수적으로 minimal prime ideal은 항상 associated prime ideal이 된다. 이는 ring $A$를 자기 자신 위의 module로 보면 $\ann A=\{0\}$이므로 [\[가환대수학\] §동반소아이디얼, ⁋정리 7](/ko/math/commutative_algebra/associated_primes#thm7)를 적용하면 확인할 수 있다.

그러나 associated prime ideal은 minimal prime보다 더 많은 것을 담고 있다. [\[가환대수학\] §동반소아이디얼, ⁋정리 7](/ko/math/commutative_algebra/associated_primes#thm7)의 둘째 결과에 의하면 $A$의 associated prime들의 합집합은 정확히 $0$과 $A$의 zero-divisor들의 모임과 같다. 가령 [§스킴의 위상구조, ⁋예시 6](/ko/math/scheme_theory/topology_of_schemes#ex6)에서 본 $Z(\x\y)$의 경우, zero-divisor $\x,\y$는 각각 서로 다른 irreducible component에서 $0$이 되는 함수였으며, 그 zero-divisor 관계는 두 component의 generic point인 minimal prime $(\x),(\y)$만으로 이미 완전히 설명된다. 그러나 뒤의 [예시 11](#ex11)에서 보듯 이것이 항상 그런 것은 아니며, minimal prime, 다시 말해 irreducible component의 generic point만으로는 놓치는 zero-divisor의 위치까지도 associated point는 전부 포착한다. 

::: 정의 8
Locally noetherian scheme $X$의 한 점 $x$와 $x$의 affine open neighborhood $U\cong \Spec A$에 대하여, $x$가 $X$의 *associated point<sub>동반점</sub>*이라는 것은 $x$에 대응되는 prime ideal $\mathfrak{p}_x\subset A$가 $A$의 associated prime ideal인 것이다. 
:::

그럼 이 정의는 $U$의 선택에 의존하지 않으며, 뿐만 아니라 stalk-local하게 쓸 수도 있다. 이는 우선 $x$를 포함하는 affine open neighborhood $\Spec A$에 대하여, $X$가 locally noetherian scheme이라는 조건으로부터 $A$가 noetherian ring이라 가정하면 [\[가환대수학\] §동반소아이디얼, ⁋정리 7](/ko/math/commutative_algebra/associated_primes#thm7)의 셋째 조건으로부터 $\mathfrak{p}_x$에 포함된 $A$의 associated prime ideal들의 모임과 $A_{\mathfrak{p}_x}$의 associated prime ideal들 사이의 일대일대응이 존재하는 것을 알고, 이 일대일대응으로부터 [정의 8](#def8)을

> Locally noetherian scheme $X$의 한 점 $x$에 대하여, $x$가 $X$의 *associated point<sub>동반점</sub>*이라는 것은 $\mathfrak{m}_x$가 $\mathcal{O}_{X,x}$의 associated prime ideal인 것이다.

으로 바꾸어 쓸 수 있기 때문이다. 

이제 [\[가환대수학\] §동반소아이디얼, ⁋정리 7](/ko/math/commutative_algebra/associated_primes#thm7)의 첫째 조건은 만일 $X$가 quasicompact locally noetherian scheme일 경우, 즉 $X$가 noetherian scheme일 경우 associated point들의 유한성 또한 보장해준다. 이제 [정의 8](#def8)이 앞서 본 것처럼 $U$의 선택과 무관하게 stalk만으로 재서술되므로, 우리는 우리의 관심사를 noetherian ring의 spectrum $\Spec A$로 한정할 수 있다. 

::: 정의 9
Noetherian ring의 스펙트럼 $\Spec A$의 associated point들 중, $\Spec A$의 irreducible component들의 generic point에 해당하지 않는 것들을 *embedded point*라 부른다. 
:::

Irreducible component의 generic point에 해당하는 associated point는 각 component마다 대표적으로 존재하는 zero-divisor 관계를 담당하는 반면, embedded point는 이미 다른 (더 큰) irreducible component에 속해 있는 점이면서도 그 자리에서 $A$가 국소적으로 추가적인 nilpotent 방향의 정보를 갖는다는 것을 기록한다. 즉 embedded point 근처에서 scheme은 그 component만으로 결정되는 reduced 구조보다 실제로 더 많은 정보를 담고 있으며, 이는 다음 예시에서 구체적으로 확인할 수 있다.

한편, 정의에 의해 다음이 성립한다.

::: 명제 10
Noetherian ring의 스펙트럼 $\Spec A$의 associated point들은 적당한 $f\in A$에 대하여, $\supp(f)$의 irreducible component의 generic point이며, 그 역 또한 성립한다.
:::
::: 증명
우선 임의의 $g\in A$와 prime ideal $\mathfrak{q}\in \Spec A$에 대하여

$$\mathfrak{q}\in \supp(g)\iff g_\mathfrak{q}\neq 0\text{ in $A_\mathfrak{q}$}\iff \ann(g_\mathfrak{q})\neq A_\mathfrak{q}$$

이 성립한다. 그런데 [\[가환대수학\] §국소화, ⁋명제 5](/ko/math/commutative_algebra/localization#prop5)에 의하여

$$\ann(g_\mathfrak{q})=\ann(g)A_\mathfrak{q}$$

이므로, 마지막 조건은 $\ann(g)\setminus \mathfrak{q}=\emptyset$, 즉 $\mathfrak{q}\in Z(\ann(g))$와 동치이다. 이로부터 임의의 $g\in A$에 대해

$$\supp(g)=Z(\ann(g))$$

이 성립하는 것을 안다. 따라서 $\supp(g)$의 irreducible component와 $\ann(g)$를 포함하는 minimal prime ideal 사이의 일대일 대응이 존재한다. 

이제 $\Spec A$의 임의의 associated point $\mathfrak{p}$가 주어졌다 하면, 정의에 의해 적당한 $f\in A$가 존재하여 $\mathfrak{p}=\ann(f)$이다. 이제

$$\supp(f)=Z(\ann(f))=Z(\mathfrak{p})$$

이고, $\mathfrak{p}$가 $\ann(f)=\mathfrak{p}$의 minimal prime인 것은 자명하므로 $\mathfrak{p}$는 $\supp f$의 generic point이다.

거꾸로 $\mathfrak{p}$가 적당한 $g\in A$에 대하여 $\supp(g)$의 generic point라 하자. 즉 $\mathfrak{p}$가 $\ann(g)$를 포함하는 minimal prime ideal이라 하자. 사상 $A \rightarrow Ag$, $a\mapsto ag$의 kernel이 정확히 $\ann(g)$이므로 $Ag\cong A/\ann(g)$이고, 특히 $\ann(A/\ann(g))=\ann(g)$이다. 이제 [\[가환대수학\] §동반소아이디얼, ⁋정리 7](/ko/math/commutative_algebra/associated_primes#thm7)의 첫째 결과를 $A$-module $A/\ann(g)$에 적용하면 $\mathfrak{p}\in \Ass(A/\ann(g))=\Ass(Ag)$를 얻는다. 그런데 $Ag$는 $A$의 submodule이므로 [\[가환대수학\] §동반소아이디얼, ⁋보조정리 5](/ko/math/commutative_algebra/associated_primes#lem5)의 첫 번째 포함관계에 의하여 $\Ass(Ag)\subseteq \Ass(A)$이고, 따라서 $\mathfrak{p}\in \Ass(A)$, 즉 $\mathfrak{p}$는 $\Spec A$의 associated point이다.
:::

위의 증명에서 사용한 식

$$\supp(f)=Z(\ann(f))$$

를 살펴보면, 만일 $A$가 integral domain이었다면 $\ann(f)$는 오직 $f=0$일 때만 $A$ 전체이고, 그렇지 않은 경우에는 $0$이 된다. 즉, 이 경우 $\supp(f)$는 $f$가 $0$인 경우만 공집합이고, 나머지 경우에는 $\Spec A$ 전체이며, 우리는 [명제 4](#prop4)에서 $\Spec A$가 irreducible임을 알고 있으므로 $\Spec A$의 유일한 associated point는 generic point $(0)$ 뿐임을 안다. 

더 일반적으로, $A$가 integral domain이 아니라면 $\ann(f)$가 $0$도, $A$도 아닌 경우가 존재하므로 embedded point가 존재할 가능성이 있다. 

::: 예시 11
Affine scheme $X=\Spec \mathbb{K}[\x_1,\x_2]/(\x_2^2, \x_1\x_2)$를 생각하자. 그럼 [§스펙트럼, ⁋명제 9](/ko/math/scheme_theory/spectrums#prop9)에 의하여 집합으로서 $X=Z(\x_2^2,\x_1\x_2)$이며, $\sqrt{(\x_2^2,\x_1\x_2)}=(\x_2)$이므로 이는 $Z(\x_2)$, 즉 $\x_1$-축($\Spec\mathbb{K}[\x_1]$)이다. 

그럼에도 불구하고 ring $A=\mathbb{K}[\x_1,\x_2]/(\x_2^2,\x_1\x_2)$는 primary 분해

$$(\x_2^2,\x_1\x_2)=(\x_2)\cap(\x_1,\x_2)^2$$

가 보여주듯 두 개의 associated prime $(\x_2)$와 $(\x_1,\x_2)$를 가진다. 전자는 $\x_1$-축의 generic point로 $X$의 유일한 irreducible component를 결정하고, 후자는 이 component의 generic point가 아니므로 embedded point가 되며 원점에 해당한다. 
:::

이 예시는 [§스킴의 위상구조, ⁋예시 6](/ko/math/scheme_theory/topology_of_schemes#ex6)의 $Z(\x\y)$와 대조적이다. $X$는 irreducible component를 $\x_1$-축 하나만 가지므로, $A$의 zero-divisor 관계 $\x_1\x_2=0$ ($\x_1,\x_2\neq 0$)은 서로 다른 component에서 각각 $0$이 되는 함수들의 곱으로는 설명할 수 없다. 실제로 $\x_2$는 nilpotent이므로 ($\x_2^2=0$) reduced ring $A/\mathfrak{N}(A)\cong \mathbb{K}[\x_1]$에서는 이미 $0$이 되어 사라지며, 그 zero-divisor로서의 정보는 오직 embedded point, 즉 원점에서의 associated prime $(\x_1,\x_2)$에만 남아있다. 이것이 바로 irreducible component의 generic point만으로는 놓치고, associated point 전체를 보아야만 포착할 수 있는 zero-divisor의 위치이다.

## 유리함수

이제 우리는 스킴 위에서 정의된 유리함수를 정의한다. 우선 [\[가환대수학\] §동반소아이디얼, ⁋따름정리 4](/ko/math/commutative_algebra/associated_primes#cor4)의 둘째 결과에 의하여 다음의 함수

$$A \rightarrow \prod_\text{\scriptsize $\mathfrak{p}$ associated prime} A_\mathfrak{p}$$

는 injective인 것을 안다. 따라서 locally noetherian scheme $X$의 임의의 열린집합 $U$에 대하여 다음의 함수

$$\Gamma(U, \mathcal{O}_X) \rightarrow \prod_\text{\scriptsize $x$ associated in $U$} \mathcal{O}_{X,x}\tag{$\ast$}$$

가 injective이다. 

::: 정의 12
Locally noetherian scheme $X$와, $X$의 associated point들을 모두 포함하는 열린집합 $U$에 대하여, $\Gamma(U, \mathcal{O}_X)$의 ($\ast$)에 의한 image를 $X$ 위에 정의된 *rational function<sub>유리함수</sub>*라 부른다. 
:::

따라서, 정의에 의해 $X$ 위에 정의된 rational function은 (1) $X$의 모든 associated point들을 포함하는 *정의역* $U$와, (2) 그 위의 함수 $f\in \Gamma(U, \mathcal{O}_X)$의 데이터로 이루어지며, 이러한 pair $(U, f)$와 $(U',f')$는 만일 $U\cap U'$에서 $f$와 $f'$가 같은 함수를 정의하면 같은 함수가 된다. 

이러한 정의역의 조건은 다음과 같이 이해할 수 있다. $X$가 integral scheme이라면, 유리함수는 그저 공집합이 아닌 열린집합 위에서 정의된 regular function이었다. $X$가 irreducible이므로 임의의 두 그러한 열린집합은 항상 만나고, 결국 이는 generic point에서의 stalk, 즉 $\Frac(A)$의 원소를 정의하는 것과 같았다. $X$가 integral이 아니라면 이 역할을 해 줄 단일한 generic point가 없으므로, 그 대신 위의 ($\ast$)의 injectivity가 보장하는 성질, 즉 이 점들에서의 stalk 값만으로 $\Gamma(U,\mathcal{O}_X)$의 원소가 완전히 결정된다는 성질을 만족하는 점들의 모임이 필요하며 associated point가 그 역할을 한다. 

이 때 $U$가 associated point 중 irreducible component의 generic point 뿐만 아니라 embedded point까지 전부 포함해야 하는 이유는, 그렇지 않으면 nilpotent 방향의 정보를 잃어버리기 때문이다. 가령 [예시 11](#ex11)의 $X=\Spec \mathbb{K}[\x_1,\x_2]/(\x_2^2,\x_1\x_2)$를 생각하면, embedded point는 원점 $(\x_1,\x_2)$이고 나머지 associated point는 $\x_1$-축의 generic point $(\x_2)$ 뿐이다. 만일 $U$가 원점을 포함하지 않아도 된다고 완화하여 $U=D(\x_1)$을 허용한다면, $\x_1$을 뒤집는 순간 $\x_2=\x_1^{-1}(\x_1\x_2)=0$이 되어 $\Gamma(U,\mathcal{O}_X)\cong \mathbb{K}[\x_1]_{\x_1}$, 즉 nilpotent $\x_2$가 완전히 사라진 reduced 구조만 남는다. 반면 $U$가 원점을 포함하도록 강제하면 $\x_2$는 (nilpotent이지만) $0$이 아닌 함수로 남아, $X$가 원점에서 실제로 갖는 두꺼움이 유리함수의 정의에도 반영된다. 

::: 예시 13
Affine scheme $X=\Spec \mathbb{K}[\x_1,\x_2]/(\x_2-\x_1^2)$을 생각하자. 그럼 $X$는 유일한 associated prime $(0)$을 가지며, $X$의 임의의 열린집합은 이 점을 포함하므로 $X$의 rational function은 공집합이 아닌 임의의 열린집합 $U$와 그 위에서의 함수 $f\in\Gamma(U, \mathcal{O}_X)$로 이루어진다. 

한편, 우리는 affine scheme $X=\Spec A$의 principal open subset $\Spec A_f$들이 위상의 basis를 이루며, 이 위에서의 함수는 $A_f$로 주어지는 것을 안다. 가령 이 예시에서 $f$를 $\x_1$(의 $A$에서의 image)로 택했다고 하면, isomorphism

$$\left(\frac{\mathbb{K}[\x_1,\x_2]}{(\x_2-\x_1^2)}\right)_{\x_1}\cong\frac{\mathbb{K}[\x_1,\x_2]_{\x_1}}{(\x_2-\x_1^2)_{\x_1}}$$

에 의하여, 열린집합 $\Spec A_{\x_1}$ 위에서 정의된 $1/\x_1$과 같은 함수들은 $X$ 위에서의 rational function이 된다. 이를 통해 분모에 $\x_2-\x_1^2$ 인자를 갖고 있지 않은 모든 유리식은 $X$ 위의 (적절한 열린집합에서의) 유리함수가 된다는 것을 안다. 
:::

Locally noetherian scheme $X$ 위에 정의된 rational function들의 모임은 *total quotient ring* $K(X)$를 정의한다. 만일, 위와 같이 $X$가 integral scheme이라 하자. 그럼 특히 $X$는 irreducible이므로 유일한 generic point $x$를 갖는다. 이 점은 임의의 affine open subset $U\cong\Spec A$에 대하여, integral domain $A$의 유일한 minimal prime ideal $(0)$에 대응되어야 한다. 이 점에서의 localization은 $A$의 nonzero element들을 모두 분모로 추가해 준 것, 즉 $\Frac(A)$와 같다. 따라서 $K(X)\cong \mathcal{O}_{X,x}\cong \Frac(A)$이며, 이는 $X$가 하나의 affine open $\Spec A$로 이루어진 경우 이미 알고 있던 $A$의 fraction field가 일반적인 integral scheme에서도 그대로 유리함수체의 역할을 한다는 것을 보여준다. 


---
**참고문헌**

**[Har]** R. Hartshorne, *Algebraic geometry*. Graduate texts in mathematics. Springer, 1977.  
**[Vak]** R. Vakil, *The rising sea: Foundation of algebraic geometry*. Available [online](https://math.stanford.edu/~vakil/216blog/).  

---
[^1]: 이 과정에서 $$X$$의 irreducible component들이 유한히 많기 때문에 각각의 component들이 열린집합임을 사용하였다. 