---
title: "인자와 선형계"
description: "국소적으로 하나의 방정식으로 잘리는 closed subscheme으로부터 Cartier divisor를 정의하고, normal integral scheme 위에서 codimension 1 점의 valuation으로 Weil divisor와 divisor class group을 정의하여 두 인자 이론을 비교한다. 이어 Cartier divisor가 정의하는 invertible sheaf를 통해 Picard group과의 동형을 얻고, 선형계와 ample invertible sheaf를 다룬다."
excerpt: "Cartier and Weil divisors, the sheaf O_X(D), linear systems, and ampleness"

categories: [Math / Scheme Theory]
permalink: /ko/math/scheme_theory/divisors_and_linear_systems
sidebar: 
    nav: "scheme_theory-ko"

date: 2026-07-27
weight: 17

---

[§준연접층](/ko/math/scheme_theory/quasicoherent_sheaves)에서 quasi-coherent sheaf와 invertible sheaf를 정의하였으므로, 우리는 variety 위에서 하던 divisor와 line bundle의 계산을 이제 scheme 위에서 시작할 수 있다. 이 글의 목적은 [\[대수다양체\] §인자](/ko/math/algebraic_varieties/divisors), [\[대수다양체\] §선다발과 벡터다발](/ko/math/algebraic_varieties/line_bundles)와 [\[대수다양체\] §선형계](/ko/math/algebraic_varieties/linear_systems)에서 다루었던 내용들을 scheme의 언어로 올려주는 것이다. 

## 카르티에 인자

[\[대수다양체\] §인자](/ko/math/algebraic_varieties/divisors)에서는 Weil divisor를 먼저 정의하고 Cartier divisor를 그 후에 살펴보았다. 이는 Cartier divisor가 국소적으로 하나의 방정식으로 잘린다는 조건을 더함으로써 그 대상이 정의되는 공간을 일반화한 것이기 때문이었는데, 덕분에 우리는 singular variety에서 작동하는 divisor theory를 사용할 수 있었다. Scheme은 variety보다 여러 방면으로 일반적인 무대이므로, 우리는 처음부터 Weil divisor를 다루기보다 우리가 주로 사용할 Cartier divisor를 사용하기로 한다. 

::: 정의 1
Closed embedding $\iota: Z \hookrightarrow X$가 *effective Cartier divisor<sub>유효 카르티에 인자</sub>*라는 것은 $X$의 affine open cover $\{U_i=\Spec A_i\}$가 존재하여, 각각의 closed embedding들

$$\iota\vert^{U_i}:\iota^{-1}(U_i) \rightarrow U_i$$

마다 적당한 non-zerodivisor $s_i\in A_i=\Gamma(U_i, \mathcal{O}_X)$가 존재하여 두 closed embedding $\iota\vert^{U_i}$와 $s_i$의 vanishing scheme $Z(s_i)\hookrightarrow U_i$가 isomorphic한 것이다. ([§닫힌 부분스킴, ⁋정의 7](/ko/math/scheme_theory/closed_subschemes#def7))
:::

정의가 $s_i$에 요구하는 것은 non-zerodivisor라는 것뿐이므로 $Z$는 non-reduced일 수 있다. Algebraic variety에서는 closed subvariety가 언제나 reduced이므로, multiplicity를 담기 위해서는 [\[대수다양체\] §인자, ⁋정의 1](/ko/math/algebraic_varieties/divisors#def1)과 같이 formal sum을 사용하여 형식적으로 정수계수를 붙여주었어야 했다. 이제 $Z$ 자체가 multiplicity를 가지므로 effective인 경우에는 그러한 계수가 필요하지 않다. 가령 $X=\Spec \mathbb{K}[\x]$와 $s=\x^2$에 대하여 $\x^2$이 non-zerodivisor이므로 $Z(s)=\Spec \mathbb{K}[\x]/(\x^2)$은 effective Cartier divisor이며, 이는 원점 하나에 얹힌 non-reduced scheme으로서 multiplicity $2$를 갖는다.

위의 정의는 본질적으로 열린집합마다 정의되는 조건으로, cover에 의존하지만 이를 간단히 closed subscheme을 정의하는 ideal sheaf의 성질로 바꿔줄 수 있다. ([§닫힌 부분스킴, ⁋정의 5](/ko/math/scheme_theory/closed_subschemes#def5))

::: 명제 2
Closed embedding $\iota: Z\hookrightarrow X$가 effective Cartier divisor인 것은, 그 ideal sheaf $\mathcal{I}_{Z/X}$가 invertible sheaf인 것과 동치이다. ([§준연접층, ⁋정의 12](/ko/math/scheme_theory/quasicoherent_sheaves#def12))
:::
::: 증명
Affine open subset $U=\Spec A$ 위에서 $\iota$를 공역에 대해 제한한 것은 ideal $\mathfrak{a}=\mathcal{I}_{Z/X}(U)$가 정의하는 closed embedding $Z(\mathfrak{a})\hookrightarrow U$이며, 서로 다른 두 ideal은 서로 다른 closed subscheme을 정의한다. ([§닫힌 부분스킴, ⁋명제 3](/ko/math/scheme_theory/closed_subschemes#prop3)) 따라서 $\iota\vert^U$가 $Z(s)\hookrightarrow U$와 isomorphic한 것은 $\mathfrak{a}=(s)$인 것과 같다.

이제 $s\in A$에 대하여 $A \rightarrow (s)$, $a\mapsto as$를 생각하자. 이는 언제나 surjective이고 그 kernel이 $\ann(s)$이므로, 이것이 isomorphism인 것과 $s$가 non-zerodivisor인 것은 동치이다. 이제 $\iota$가 effective Cartier divisor라 하고 [정의 1](#def1)의 affine open cover $\{U_i=\Spec A_i\}$를 택하자. 그럼 $\mathcal{I}_{Z/X}(U_i)=(s_i)\cong A_i$이다. 한편 $\mathcal{I}_{Z/X}$는 quasi-coherent sheaf이고 ([§준연접층, ⁋명제 18](/ko/math/scheme_theory/quasicoherent_sheaves#prop18)) quasi-coherence는 affine-local이므로, [§준연접층, ⁋정리 10](/ko/math/scheme_theory/quasicoherent_sheaves#thm10)에 의하여 $\mathcal{I}_{Z/X}\vert_{U_i}\cong \widetilde{\mathcal{I}_{Z/X}(U_i)}$이다. 따라서 위의 동형은

$$\mathcal{I}_{Z/X}\vert_{U_i}\cong \widetilde{(s_i)}\cong \widetilde{A_i}=\mathcal{O}_{U_i}$$

를 준다. 즉 $\mathcal{I}_{Z/X}$는 rank $1$의 locally free sheaf이다.

거꾸로 $\mathcal{I}_{Z/X}$가 invertible sheaf라 하자. 임의의 점 $x$에 대하여 $\mathcal{I}_{Z/X}\vert_V\cong \mathcal{O}_V$인 열린근방 $V$를 택하고, $V$ 안에서 $x$를 담는 affine open subset $U=\Spec A$를 택하면 $\mathcal{I}_{Z/X}(U)\cong A$이다. 이 동형에서 $1\in A$의 image를 $s$라 하면 $\mathcal{I}_{Z/X}(U)=(s)$이고 $\ann(s)=0$이므로 $s$는 non-zerodivisor이다. 이러한 $U$들이 $X$를 덮으므로 [정의 1](#def1)의 조건이 충족된다.
:::

증명에서 사용한 사상 $A\rightarrow \mathcal{I}_{Z/X}(U)$가 [정의 1](#def1)의 두 요구를 명확하게 나눠준다. 이 사상이 surjective라는 것은 ideal $\mathcal{I}_{Z/X}(U)$가 $s$ 하나로 생성된다는 것, 곧 $Z$가 $U$ 위에서 방정식 하나로 잘린다는 것을 요구한다. 이 때, 위의 non-zerodivisor 조건은 $\ann(s)=0$가 되며, 이 때 이 사상이 injective가 되어 $\mathcal{I}_{Z/X}\vert_U\cong \mathcal{O}_U$를 얻는다. 만일 이 non-zerodivisor 조건을 뺀다면 각각의 $s_i$는 $A_i$의 임의의 원소로 택할 수 있으며, 이렇게 얻어지는 조건을 *locally principal*이라 부른다. 곧 effective Cartier divisor란 locally principal인 것 가운데 그 국소적인 방정식을 non-zerodivisor로 잡을 수 있는 것이다.

Effective Cartier divisor의 가장 기본적인 성질은 그 codimension이 언제나 $1$이라는 것이다.

::: 명제 3
Locally Noetherian scheme $X$ 위의 effective Cartier divisor $\iota:Z\hookrightarrow X$에 대하여, $Z$의 모든 irreducible component는 $X$에서 codimension $1$을 갖는다.
:::
::: 증명
Codimension은 국소적으로 계산되므로, [정의 1](#def1)의 affine open cover $\{U_i=\Spec A_i\}$ 가운데 하나를 택하여 $Z\cap U_i=Z(s_i)$이고 $s_i\in A_i$가 non-zerodivisor인 경우만 보면 충분하다. $Z$의 irreducible component $W$가 $U_i$와 만난다면 $W\cap U_i$는 $Z(s_i)$의 irreducible component이다. [§차원, ⁋명제 13](/ko/math/scheme_theory/dimension#prop13)에 의하여 $Z(s_i)$의 component는 $U_i$에서 codimension $0$이거나 $1$인데, codimension $0$인 component는 $U_i$ 자신의 irreducible component, 즉 $A_i$의 minimal prime ideal $\mathfrak{p}$에 대응된다. 만일 $W\cap U_i$가 그러한 component라면 $s_i$가 그 위에서 소멸하므로 $s_i\in \mathfrak{p}$이다. 그런데 Noetherian ring에서 non-zerodivisor는 어떠한 minimal prime ideal에도 속하지 않으므로 ([\[가환대수학\] §동반소아이디얼, ⁋정리 7](/ko/math/commutative_algebra/associated_primes#thm7)) 이는 $s_i$가 non-zerodivisor라는 가정에 모순이다. 따라서 $W\cap U_i$의 codimension은 $1$이고, [§차원, ⁋명제 8](/ko/math/scheme_theory/dimension#prop8)에 의하여 $W$의 $X$에서의 codimension 또한 $1$이다.
:::

증명에서 $s_i$가 non-zerodivisor라는 요구가 쓰인 곳은 $s_i$가 $A_i$의 어떠한 minimal prime ideal에도 속하지 않는다는 것뿐이었다. 기하적으로 이는 $s_i$가 $X$의 irreducible component 위에서 통째로 소멸하지 않는다는 것이다. [정의 1](#def1)에서 이 요구를 덜어내면 방정식 $s_i$가 component 하나를 자르는 대신 그것을 통째로 삼킬 수 있고, 그러면 $Z$는 codimension $1$이 아니라 $X$의 component 자체가 된다. 다음 예시에서 이러한 상황을 확인하자.

::: 예시 4
$X=\Spec \mathbb{K}[\x,\y]/(\x\y)$를 평면의 두 좌표축의 합집합이라 하고, $Z=Z(\x)$라 하자. 이는 global section $\x$ 하나의 vanishing scheme이므로, $X$ 자신을 cover로 택하면 $Z\hookrightarrow X$가 locally principal임을 안다.

그러나 이는 effective Cartier divisor가 아니다. $\mathbb{K}[\x,\y]/(\x\y,\x)\cong\mathbb{K}[\y]$이므로 $Z$는 $\y$-축이고, 이는 $X$의 두 irreducible component 가운데 하나이므로 $X$에서 codimension $0$을 갖는다. 그런데 [명제 3](#prop3)에 의하여 effective Cartier divisor의 irreducible component는 codimension $1$이어야 한다.

대수적으로는 [명제 2](#prop2)가 같은 것을 말해준다. 원점을 담는 affine open subset $U=\Spec A$를 어떻게 택하더라도 $U$는 두 좌표축과 모두 만나므로 $A$ 안에서 $\y$는 $0$이 아니고, $\mathcal{I}_{Z/X}(U)$를 생성하는 $\x$는 이를 죽이는 zerodivisor이다. 곧 이 ideal은 결코 free module이 될 수 없다.
:::

위의 예시에서 codimension이 예상대로 행동하지 않은 것은 $\x$가 minimal prime ideal에 포함되어 있었기 때문이다. 원소가 non-zerodivisor임을 요구함으로써 우리는 이와 같은 minimal prime ideal 뿐만 아니라 associated prime ideal 전체를 피할 수 있도록 해 주며, 예를 들어 다음의 scheme

$$A=\mathbb{K}[\x,\y]/(\x^2,\x\y)$$

에서 $(\x^2,\x\y)=(\x)\cap(\x^2,\y)$이므로 $\Ass(A)=\{(\x),(\x,\y)\}$인데, 이는 $\y$-축에 원점이 embedded point로 얹혀 있는 scheme이다. 여기에서 $\y$는 유일한 minimal prime ideal $(\x)$에 속하지 않으므로 $Z(\y)$는 어떠한 component도 삼키지 않고 codimension $1$을 가지지만, $\x\y=0$이고 $\x\neq 0$이므로 $\y$는 zerodivisor이고 $\ann(\y)=(\x)$이다. 따라서 $Z(\y)\hookrightarrow \Spec A$는 codimension $1$이면서도 effective Cartier divisor가 아니며, 이는 [명제 3](#prop3)의 역이 일반적으로 성립하지 않는다는 뜻이기도 하다.

두 예시 모두에서 문제가 된 것은 해당하는 점에서의 local ring이 domain조차 아니었다는 것이다. 이러한 상황을 배제하면 [명제 3](#prop3)의 역이 성립한다.

::: 명제 5
Locally Noetherian integral scheme $X$가 factorial이라 하자. ([§스킴의 대수구조, ⁋정의 7](/ko/math/scheme_theory/algebra_of_schemes#def7)) 그럼 codimension $1$인 임의의 integral closed subscheme $\iota:Z\hookrightarrow X$는 effective Cartier divisor이다.
:::
::: 증명
$X$가 integral이므로 임의의 affine open subset $U=\Spec A$에 대하여 $A$는 Noetherian domain이고, 특히 $A$의 $0$이 아닌 원소는 모두 non-zerodivisor이다.

$Z$와 만나지 않는 점에 대해서는 볼 것이 없다. $Z$가 닫힌집합이므로 그러한 점은 $Z$와 만나지 않는 affine open neighborhood를 가지며, 그 위에서 $Z$는 $Z(1)=\emptyset$이어서 [정의 1](#def1)의 조건이 $s=1$로 충족되기 때문이다.

이제 $z\in Z$를 택하고 $z$를 담는 affine open subset $U=\Spec A$를 잡자. $Z$가 integral이므로 $\mathfrak{p}=\mathcal{I}_{Z/X}(U)$는 prime ideal이며, [§차원, ⁋명제 8](/ko/math/scheme_theory/dimension#prop8)에 의하여 $Z$가 codimension $1$이라는 것은 $\mathfrak{p}$가 codimension $1$이라는 것이다. $z$에 대응하는 prime ideal을 $\mathfrak{q}\supseteq \mathfrak{p}$라 하면 $X$가 factorial이라는 가정에 의하여 $A_\mathfrak{q}=\mathcal{O}_{X,z}$는 Noetherian local UFD이고, $\mathfrak{p}A_\mathfrak{q}$는 codimension $1$인 prime ideal이다. 그럼 [\[가환대수학\] §정칙성의 호몰로지 판정, ⁋보조정리 8](/ko/math/commutative_algebra/homological_criterion_for_regularity#lem8)의 1번에 의하여 $\mathfrak{p}A_\mathfrak{q}$는 principal이다.

$\mathfrak{p}A_\mathfrak{q}=(t)$라 하고, $\mathfrak{q}$ 바깥의 원소는 $A_\mathfrak{q}$에서 unit이므로 $t=f/1$이 되도록 $f\in A$를 택하자. $\mathfrak{p}A_\mathfrak{q}\cap A=\mathfrak{p}$이므로 $f\in \mathfrak{p}$이다. 한편 $A$가 Noetherian이므로 $\mathfrak{p}$는 유한개의 원소 $p_1,\ldots, p_n$이 생성하고, 각각의 $p_i/1$이 $(f)A_\mathfrak{q}$에 속하므로 $g_i\notin \mathfrak{q}$가 존재하여 $g_ip_i\in (f)$이다. $g=g_1\cdots g_n$으로 두면 $\mathfrak{q}$가 prime이므로 $g\notin\mathfrak{q}$이고, $A_g$에서 $\mathfrak{p}A_g=(f)$이다.

그럼 $D(g)$는 $z$의 affine open neighborhood로서 그 위에서 $Z$는 $Z(f)$이며, $A_g$가 domain이고 $f\neq 0$이므로 $f$는 non-zerodivisor이다. 이렇게 얻은 열린집합들이 $X$를 덮으므로 [정의 1](#def1)에 의하여 $\iota$는 effective Cartier divisor이다.
:::

즉, 위의 가정에 대해서는 codimension $1$이라는 위상적인 조건만으로 방정식 하나를 되찾을 수 있으며, 일반적으로 모든 local ring이 regular local ring인 scheme은 factorial이라는 것이 알려져 있으므로 특히 regular한 대상에서 이러한 결과가 성립한다. 일반적으로는 그러한 회복을 기대할 수 없으므로, 우리는 국소적인 방정식 자료 자체를 대상으로 삼아 이들을 한데 모은다. 이 때 각각의 방정식은 $U_i$ 위의 함수일 필요가 없고 겹침 위에서 그 비율만이 통제되며, 아래에서 $K(U)$는 [§스킴의 대수구조, ⁋정의 12](/ko/math/scheme_theory/algebra_of_schemes#def12)의 total quotient ring이다.

::: 정의 6
Locally Noetherian scheme $X$ 위의 *Cartier divisor<sub>카르티에 인자</sub>*란 $X$의 affine open cover $\{U_i\}$와 각각의 $f_i\in K(U_i)^\times$가 이루는 데이터 $\{(U_i,f_i)\}$로, 임의의 $i,j$에 대하여 $f_i/f_j$가 $U_i\cap U_j$ 위에서 $\mathcal{O}_X^\times$의 section인 것이다. 이 때, 두 데이터 $\{(U_i,f_i)\}$와 $\{(V_j,g_j)\}$는 임의의 $i,j$에 대하여 $f_i/g_j$가 $U_i\cap V_j$ 위에서 $\mathcal{O}_X^\times$의 section일 때 같은 Cartier divisor로 본다. 이들은 덧셈

$$\{(U_i,f_i)\}+\{(V_j,g_j)\}=\{(W, (f_ig_j)\vert_W)\}$$

을 연산으로 하여 group을 이루며, 여기에서 $W$는 각각의 $U_i\cap V_j$에 포함되는 affine open subset들을 훑는다. 이 group을 $\CaDiv(X)$로 적는다.
:::

이는 [\[대수다양체\] §인자, ⁋정의 12](/ko/math/algebraic_varieties/divisors#def12)에서 살펴본 것과 같은 정의로, 각각의 $f_i$가 하나의 function field가 아니라 $U_i$마다의 $K(U_i)^\times$에서 온다는 것만이 다르다. 열린집합 $W\subseteq U$의 associated point들은 $U$의 associated point들 가운데 $W$에 속하는 것들이므로 ([§스킴의 대수구조, ⁋정의 8](/ko/math/scheme_theory/algebra_of_schemes#def8)) restriction $K(U)^\times\rightarrow K(W)^\times$가 있으며, 이를 통해 자료를 세분할 수 있으므로 아래에서는 affine이 아닌 cover 위에 적은 자료도 같은 방식으로 읽는다.

각각의 $f_i$가 모두 $\Gamma(U_i,\mathcal{O}_X)$에 속하는 Cartier divisor를 *effective*라 부르며, 이것이 위의 동치관계와 호환되는 것을 쉽게 확인할 수 있다. $f_i$가 $\Gamma(U_i,\mathcal{O}_X)$에 속하고 $f_i/g_j$가 $U_i\cap V_j$ 위에서 invertible section이라면 $g_j=f_i\cdot(f_i/g_j)^{-1}$ 또한 그 위에서 $\mathcal{O}_X$의 section이고, 이러한 $U_i\cap V_j$들이 $V_j$를 덮으므로 $g_j$ 역시 $\Gamma(V_j,\mathcal{O}_X)$에 속하기 때문이다. 이렇게 대수적으로 정의한 개념이 [정의 1](#def1)의 것과 일치한다는 것이 $\CaDiv(X)$에 관한 첫 번째 결과이다. 

::: 명제 7
Locally Noetherian scheme $X$에 대하여, effective Cartier divisor $\iota:Z\hookrightarrow X$들과 $\CaDiv(X)$의 effective한 원소들은 서로 일대일로 대응한다.
:::
::: 증명
Effective한 $D=\{(U_i,f_i)\}$가 주어졌다 하자. $f_i\in \Gamma(U_i,\mathcal{O}_X)$가 $K(U_i)^\times$의 원소라는 것은 $f_i$가 non-zerodivisor라는 것이다. 각 $U_i$ 위에서 ideal $(f_i)$를 생각하면, $f_i/f_j$가 겹침 위에서 unit이므로 이들은 겹침 위에서 같은 ideal sheaf를 정의하고, 따라서 [§닫힌 부분스킴, ⁋명제 6](/ko/math/scheme_theory/closed_subschemes#prop6)에 의하여 $X$의 closed subscheme $Z$ 하나로 붙는다. 이 $Z$는 구성에 의하여 [정의 1](#def1)의 조건을 만족한다.

거꾸로 effective Cartier divisor $\iota:Z\hookrightarrow X$와 [정의 1](#def1)의 자료 $\{(U_i,s_i)\}$가 주어졌다 하자. $s_i$가 non-zerodivisor이므로 $s_i\in K(U_i)^\times$이다. 겹침 위에서는 $\mathcal{I}_{Z/X}$가 $s_i$로도 $s_j$로도 생성되므로 각 점에서 $s_i=us_j$인 local unit $u$가 존재하며, 이러한 $u$는 $s_i$와 $s_j$가 non-zerodivisor라는 것에서 유일하게 결정되어 겹침 전체의 section으로 붙는다. 곧 $\{(U_i,s_i)\}$는 effective한 Cartier divisor이다. 두 구성이 서로 역이라는 것은 어느 쪽이든 $\mathcal{I}_{Z/X}$를 국소적으로 생성하는 원소를 주고받는 것이므로 곧바로 확인된다.
:::

이로부터 우리는 effective Cartier divisor와 $\CaDiv(X)$의 effective한 원소를 구별하지 않는다. 일반적인 Cartier divisor는 각각의 $U_i$ 위에서 $f_i$를 두 non-zerodivisor의 비로 적을 수 있으므로 국소적으로는 두 effective Cartier divisor의 차이며, 이런 뜻에서 $\CaDiv(X)$는 국소적으로 [정의 1](#def1)의 closed subscheme들로 생성된다.

우리는 $f\in K(X)^\times$ 하나가 정의하는 $\{(X,f)\}$ 꼴의 Cartier divisor를 $\divisor(f)$로 적고 *principal divisor<sub>주인자</sub>*라 부른다. Cartier divisor는 정의에 의해 언제나 국소적으로 함수 하나로 주어지므로, 여기에서 문제가 되는 것은 그 국소적인 자료를 하나의 전역적인 함수로 묶을 수 있는지의 여부이다. 이들이 이루는 subgroup을 $\Prin(X)$라 하면, quotient group

$$\CaCl(X)=\CaDiv(X)/\Prin(X)$$

가 정의되며, 두 Cartier divisor의 차가 principal일 때 이 둘을 *linearly equivalent*라 부른다. 

## $\mathcal{O}_X(D)$와 Picard group

Cartier divisor의 데이터 $\{(U_i,f_i)\}$는 각 조각 위에서 하나의 함수를 지정하고 겹침 위에서 그 비율만을 통제한다. 이는 정확히 invertible sheaf를 local trivialization과 transition function으로 기술하는 방식이므로, 인자에 invertible sheaf를 대응시킬 수 있다. 이 절에서 $X$는 *integral* Noetherian scheme으로 두자. 그럼 generic point에서의 local ring인 $K(X)$가 field이고 임의의 공집합이 아닌 열린집합에 대하여 $\Gamma(V,\mathcal{O}_X)$가 그 subring이므로, 아래에서 우리는 rational function들을 하나의 $K(X)$ 안에서 다룰 수 있다.

::: 정의 8
Integral Noetherian scheme $X$와 Cartier divisor $D=\{(U_i,f_i)\}$에 대하여, $X$ 위의 $\mathcal{O}_X$-module $\mathcal{O}_X(D)$를 각각의 공집합이 아닌 열린집합 $V$마다

$$\Gamma(V,\mathcal{O}_X(D))=\{g\in K(X)\mid gf_i\in \Gamma(V\cap U_i,\mathcal{O}_X)\text{ for all $i$}\}$$

로 정의하고, $\Gamma(\emptyset,\mathcal{O}_X(D))=0$으로 둔다. 여기에서 공집합이 아닌 열린집합들 사이의 restriction map은 $K(X)$의 원소를 그대로 보내는 것이다.
:::

이는 우리가 이미 [\[대수다양체\] §선다발과 벡터다발, ⁋정의 17](/ko/math/algebraic_varieties/line_bundles#def17)에서 다룬 것으로, 우리는 $f_i/f_j$를 transition function으로 삼아 line bundle을 만들고, 그 section들이 $\divisor(g)+D\geq 0$을 만족하는 rational function들임을 뒤이어 확인하였다. [정의 8](#def8)도 이 정의와 마찬가지로 sheaf $\mathcal{O}_X(D)$를 정의하는 것으로, 이 때 $\Gamma(V,\mathcal{O}_X(D))$는 $D$가 지정하는 만큼의 pole만을 허용하는 rational function들의 모임이다.

정의의 조건은 각 점의 근방에서 확인되는 조건이므로 $\mathcal{O}_X(D)$는 실제로 $\mathcal{O}_X$의 곱셈에 대해 닫힌 sheaf이다. 또 이 sheaf는 $D$를 나타내는 데이터의 선택에 무관하다. 다른 자료 $\{(V_j,g_j)\}$가 같은 Cartier divisor를 준다면 겹침 위에서 $f_i/g_j$가 invertible section이므로, $gf_i$가 $\mathcal{O}_X$의 section인 것과 $gg_j$가 그러한 것이 각각의 $V\cap U_i\cap V_j$ 위에서 같은 조건이기 때문이다. $D$가 effective이면 $\mathcal{O}_X\subseteq \mathcal{O}_X(D)$이고 $-D$에 대해서는 거꾸로 $D$ 위에서 소멸하는 함수들의 sheaf, 곧 [명제 7](#prop7)이 주는 closed subscheme의 ideal sheaf가 된다.

::: 명제 9
Integral Noetherian scheme $X$와 Cartier divisor $D,D'$에 대하여 다음이 성립한다.

1. $\mathcal{O}_X(D)$는 invertible sheaf이며, $\mathcal{O}_X(D)\vert_{U_i}$는 $f_i^{-1}$이 생성한다.
2. $K(X)$ 안에서의 곱셈이 isomorphism $\mathcal{O}_X(D)\otimes_{\mathcal{O}_X}\mathcal{O}_X(D')\cong \mathcal{O}_X(D+D')$를 준다.
3. $\mathcal{O}_X(D)\cong \mathcal{O}_X$인 것은 $D$가 principal인 것과 동치이다.
:::
::: 증명
1번의 경우, $V\subseteq U_i$인 열린집합에 대하여 $f_j=f_i\cdot(f_j/f_i)$이고 $f_j/f_i$가 $U_i\cap U_j$ 위의 invertible section이므로, $gf_i\in \Gamma(V,\mathcal{O}_X)$이면 자동으로 $gf_j\in\Gamma(V\cap U_j,\mathcal{O}_X)$이다. 따라서

$$\Gamma(V,\mathcal{O}_X(D))=f_i^{-1}\Gamma(V,\mathcal{O}_X)$$

이고, $f_i\in K(X)^\times$이므로 $g\mapsto gf_i$는 $\mathcal{O}_X(D)\vert_{U_i} \rightarrow \mathcal{O}_{U_i}$의 isomorphism이다. 즉 $\mathcal{O}_X(D)$는 rank $1$의 locally free sheaf이다.

2번의 경우, $D'=\{(V_j,g_j)\}$라 하고 $D+D'$을 $\{(U_i\cap V_j, f_ig_j)\}$로 계산하면 1번에 의하여 세 sheaf는 $U_i\cap V_j$ 위에서 각각 $f_i^{-1}$, $g_j^{-1}$, $(f_ig_j)^{-1}$이 생성하는 free module이다. 곱셈 $\mathcal{O}_X(D)\otimes \mathcal{O}_X(D') \rightarrow \mathcal{O}_X(D+D')$은 generator를 generator로 보내므로 각 조각 위에서 isomorphism이고, 따라서 전체에서 isomorphism이다.

3번의 경우, $D=\divisor(h)$라면 $\mathcal{O}_X(D)=h^{-1}\mathcal{O}_X\cong \mathcal{O}_X$이다. 거꾸로 isomorphism $\psi:\mathcal{O}_X \rightarrow \mathcal{O}_X(D)$가 주어졌다 하고 $h=\psi(1)\in \Gamma(X,\mathcal{O}_X(D))\subseteq K(X)$라 하자. 그럼 $h$는 각각의 $U_i$ 위에서 $\mathcal{O}_X(D)$를 생성하므로 1번과 비교하면 $h$와 $f_i^{-1}$은 $\mathcal{O}_X^\times$의 section만큼 차이나며, 곧 $f_i/h^{-1}=hf_i$가 $U_i$ 위의 invertible section이다. 따라서 [정의 6](#def6)의 동치관계에 의하여 $\{(U_i,f_i)\}$와 $\{(X,h^{-1})\}$은 같은 Cartier divisor를 정의하여 $D=\divisor(h^{-1})$이다.
:::

위 명제에 의해 대응 $D\mapsto \mathcal{O}_X(D)$는 group homomorphism $\CaDiv(X)\rightarrow\Pic(X)$를 주며, 그 kernel이 곧 $\Prin(X)$가 된다. 따라서 우리는 이 대응의 image가 $\CaCl(X)=\CaDiv(X)/\Prin(X)$와 isomorphic하다는 것을 안다. 다음 정리는 이 결과를 매듭짓는 것으로, 이 대응이 전사이고 따라서 canonical isomorphism $\CaCl(X)\cong \Pic(X)$를 준다는 것을 보여준다.

::: 정리 10
Integral Noetherian scheme $X$에 대하여, $D\mapsto \mathcal{O}_X(D)$는 isomorphism $\CaCl(X)\cong\Pic(X)$를 유도한다.
:::
::: 증명
[명제 9](#prop9)에 의하여 유도된 homomorphism이 injective이므로 surjectivity만 보이면 된다. Invertible sheaf $\mathcal{L}$과 그 trivialization $\psi_i:\mathcal{O}_{U_i} \rightarrow \mathcal{L}\vert_{U_i}$가 주어졌다 하자. Trivialization은 열린부분집합으로의 제한에서 유지되므로 각각의 $U_i$를 affine open subset들로 덮어 세분하면, 처음부터 $\{U_i\}$가 affine open cover라 가정하여도 된다. 이제 $t_i=\psi_i(1)$을 $\mathcal{L}$의 $U_i$ 위의 generating section이라 하자. 그럼 겹침 위에서 $t_j=g_{ij}t_i$인 $g_{ij}\in \Gamma(U_i\cap U_j,\mathcal{O}_X)^\times$가 유일하게 결정되고, 이들은 $g_{ij}g_{jk}=g_{ik}$를 만족한다.

우선 $g_{ii}=1$이고 $g_{ji}=g_{ij}^{-1}$임을 관찰하고, 공집합이 아닌 $U_{i_0}$ 하나를 고정하여 $f_i=g_{ii_0}\in \Gamma(U_i\cap U_{i_0},\mathcal{O}_X)^\times$로 두자. $X$가 integral이므로 이는 $K(X)^\times$의 원소이고, cocycle 조건에서 $U_i\cap U_j\cap U_{i_0}$ 위에서 $f_i/f_j=g_{ii_0}g_{i_0j}=g_{ij}$이다. 그런데 $X$가 irreducible이므로 이 열린집합은 $U_i\cap U_j$의 조밀한 열린부분집합이고, $\Gamma(U_i\cap U_j,\mathcal{O}_X)$가 $K(X)$에 embed되므로 이 등식은 $U_i\cap U_j$ 전체에서 성립한다. 특히 $f_i/f_j$는 겹침 위에서 invertible section이므로 $D=\{(U_i,f_i)\}$는 Cartier divisor이다.

이제 $\mathcal{O}_X(D)\cong \mathcal{L}$임을 보인다. [명제 9](#prop9)에 의하여 $\mathcal{O}_X(D)\vert_{U_i}$는 $f_i^{-1}$이 생성하므로, $V\subseteq U_i$ 위에서 $gf_i\in \Gamma(V,\mathcal{O}_X)$이고

$$\varphi_i:\mathcal{O}_X(D)\vert_{U_i} \rightarrow \mathcal{L}\vert_{U_i};\qquad g\mapsto (gf_i)\cdot t_i$$

는 isomorphism이다. 겹침 위에서 $t_i=g_{ji}t_j$이고 $g_{ji}=f_j/f_i$이므로

$$\varphi_i(g)=(gf_i)\cdot\frac{f_j}{f_i}t_j=(gf_j)\cdot t_j=\varphi_j(g)$$

가 되어 이들은 하나의 isomorphism $\mathcal{O}_X(D)\cong\mathcal{L}$로 붙는다.
:::

따라서 integral Noetherian scheme 위에서 invertible sheaf를 다루는 것은 Cartier divisor를 linear equivalence까지만 기억하며 다루는 것과 같으며, variety 수준에서의 같은 대응이 [\[대수다양체\] §선다발과 벡터다발, ⁋명제 19](/ko/math/algebraic_varieties/line_bundles#prop19)이다.

## 베유 인자

이제 우리는 linear system을 살펴보기 전에 Weil divisor를 간략하게 살펴본다. 위에서 간략하게 언급했듯, Weil divisor는 Cartier divisor보다 좋은 공간에서만 정의되었었는데, 이를 scheme의 언어에서 어떻게 가져올지가 우리의 첫 번째 논의의 대상이다. 우선 Weil divisor가 정의되기 위해서는 rational function이 각각의 codimension $1$ 부분에서 갖는 zero와 pole의 order를 정의할 수 있어야 하고, 그러려면 그 점에서의 local ring이 discrete valuation ring이어야 한다. 그러나 이 조건이 실제로 어떤 조건인지는 다소 불명확하므로, 우리는 normality를 가정한다. ([§스킴의 대수구조, ⁋정의 6](/ko/math/scheme_theory/algebra_of_schemes#def6)) 그럼 [보조정리 11](#lem11)에서 이 가정이 codimension $1$ 부분에서 local ring을 DVR로 만들어준다는 것을 확인할 것이다.

따라서 normal, integral Noetherian scheme $X$를 생각하자. $X$가 integral이므로 임의의 affine open subset은 domain의 spectrum이고, 따라서 $X$의 유일한 associated point는 generic point $\xi$이다. 그럼 [§스킴의 대수구조, ⁋정의 12](/ko/math/scheme_theory/algebra_of_schemes#def12)의 total quotient ring은 [§스킴 사상의 성질들, §§유리사상](/ko/math/scheme_theory/properties_of_scheme_morphisms#유리사상)에서 정의한 function field

$$K(X)=\mathcal{O}_{X,\xi}$$

가 되며, 임의의 공집합이 아닌 열린집합 $V$에 대하여 $\Gamma(V,\mathcal{O}_X)$는 $K(X)$의 subring으로 볼 수 있다. 특히 임의의 점 $x$에서의 local ring $\mathcal{O}_{X,x}$ 또한 $K(X)$의 subring이며 그 fraction field는 $K(X)$이다. 또한 이 embedding들이 restriction 및 germ을 취하는 것과 맞아떨어지므로, 등식

$$\Gamma(V,\mathcal{O}_X)=\bigcap_{x\in V}\mathcal{O}_{X,x}$$

이 $K(X)$ 안에서 성립함을 쉽게 확인할 수 있다. 즉, rational function이 열린집합 위에서 regular인지를 각 점의 local ring으로 판정할 수 있다.

::: 보조정리 11
Normal integral Noetherian scheme $X$에 대하여 다음이 성립한다.

1. $X$의 codimension $1$ irreducible closed subset $Y$와 그 generic point $\eta$에 대하여, $\mathcal{O}_{X,\eta}$는 discrete valuation ring이다.
2. 임의의 $f\in K(X)^\times$에 대하여, $f$의 $\mathcal{O}_{X,\eta}$에서의 valuation이 $0$이 아닌 codimension $1$ irreducible closed subset $Y$는 유한히 많다.
:::
::: 증명
1번의 경우, $X$가 normal이므로 $R=\mathcal{O}_{X,\eta}$는 normal domain이고 $X$가 locally Noetherian이므로 Noetherian이다. 또한 [§차원, ⁋명제 8](/ko/math/scheme_theory/dimension#prop8)에 의하여 $\dim R=\codim_X Y=1$이므로 $R$의 maximal ideal은 codimension $1$의 prime ideal이다. 한편 [\[가환대수학\] §정칙국소환, ⁋정리 10](/ko/math/commutative_algebra/regular_local_rings#thm10)을 normal domain $R$ 자신에 적용하면 (R1) 조건, 곧 codimension $1$ prime ideal에서의 localization이 discrete valuation ring이라는 것이 성립한다. 이를 $R$의 maximal ideal에 적용하고 $R$이 local ring이라는 것을 쓰면 $R$ 자신이 discrete valuation ring이다.

2번을 보이기 위해, $X$의 Noetherian 가정을 사용해 유한히 많은 affine open subset $U_1,\ldots, U_r$이 $X$를 덮는다 하자. 각각의 $Y$는 어떤 $U_k$와 만나며, 그럼 $Y\cap U_k$는 $U_k$의 codimension $1$ irreducible closed subset으로서 같은 generic point $\eta$를 가지므로, 하나의 $U=\Spec A$를 고정하고 그 위에서 유한성을 보이면 충분하다. 여기에서 $A$는 Noetherian domain이고 $\Frac(A)=K(X)$이므로 $f=a/b$인 $a,b\in A\setminus\{0\}$를 택할 수 있다. $Y\cap U$에 대응하는 codimension $1$ prime ideal을 $\mathfrak{p}$라 하면 $\mathcal{O}_{X,\eta}=A_\mathfrak{p}$이고, 만일 $a,b\notin \mathfrak{p}$라면 $a$와 $b$가 모두 $A_\mathfrak{p}$의 unit이므로 $f$의 valuation은 $0$이다. 따라서 valuation이 $0$이 아닌 $\mathfrak{p}$는 $(a)$ 또는 $(b)$를 포함하며, codimension $1$이라는 조건에서 이들은 $(a)$ 또는 $(b)$를 포함하는 minimal prime ideal이다. 그런데 Noetherian ring $A$의 ideal $\mathfrak{a}$에 대하여 $\mathfrak{a}=\ann(A/\mathfrak{a})$이므로, $\mathfrak{a}$를 포함하는 minimal prime ideal은 모두 $\Ass(A/\mathfrak{a})$에 속하고 이 집합은 유한하다. ([\[가환대수학\] §동반소아이디얼, ⁋정리 7](/ko/math/commutative_algebra/associated_primes#thm7)의 1번) 따라서 그러한 $\mathfrak{p}$ 또한 유한히 많다.
:::

[보조정리 11](#lem11)의 1번을 만족하는 $Y$와 그 generic point $\eta$에 대하여, DVR $\mathcal{O}_{X, \eta}$의 uniformizer $\pi$를 택하면 임의의 $f\in K(X)^\times$는 

$$f=\pi^nu,\qquad u\in \mathcal{O}_{X,\eta}^\times$$

꼴로 유일하게 적히며, 이 정수 $n$은 $\pi$의 선택에 무관하다. 이를 $\ord_Y(f)$로 적는다. 두 원소의 곱에서 지수가 더해지므로 $\ord_Y:K(X)^\times \rightarrow \mathbb{Z}$는 group homomorphism이며, 이는 정확히 $\mathcal{O}_{X,\eta}$의 discrete valuation이다.

::: 정의 12
Normal integral Noetherian scheme $X$의 codimension $1$ irreducible closed subset을 *prime divisor*라 부르고, prime divisor들로 생성되는 free abelian group $\Div(X)$의 원소를 $X$의 *Weil divisor<sub>베유 인자</sub>*라 부른다. Weil divisor $D=\sum_Y n_YY$가 *effective*라는 것은 모든 $n_Y$가 음이 아닌 것이며, 이를 $D\geq 0$으로 적는다.
:::

곧 Weil divisor는 codimension $1$짜리 닫힌집합들의 정수계수의 formal sum이며, 각각의 계수는 해당 prime divisor에서 함수가 갖는 zero 또는 pole의 order를 기록한다. 이는 [\[대수다양체\] §인자, ⁋정의 1](/ko/math/algebraic_varieties/divisors#def1)의 Weil divisor를 scheme의 언어로 옮긴 것이며, 이 기록을 실제로 수행하는 것이 다음의 정의이다.

::: 정의 13
Normal integral Noetherian scheme $X$와 $f\in K(X)^\times$에 대하여,

$$\divisor(f)=\sum_Y \ord_Y(f)\cdot Y\in \Div(X)$$

를 다시 $f$의 principal divisor라 부른다. 두 Weil divisor $D_1,D_2$가 linearly equivalent라는 것은 적당한 $f\in K(X)^\times$에 대하여 $D_1-D_2=\divisor(f)$인 것이며, quotient group

$$\Cl(X)=\Div(X)/\{\divisor(f)\mid f\in K(X)^\times\}$$

를 $X$의 *divisor class group<sub>인자류군</sub>*이라 부른다.
:::

[보조정리 11](#lem11)의 둘째 결과가 이 합의 유한성을 보장한다. 또, 각각의 $\ord_Y$가 group homomorphism이므로 $\divisor:K(X)^\times \rightarrow \Div(X)$ 또한 group homomorphism이며, 따라서 principal divisor들은 $\Div(X)$의 subgroup을 이루고 $\Cl(X)$가 잘 정의된다. 

이 글의 서두에서 언급하였듯, [\[대수다양체\] §인자](/ko/math/algebraic_varieties/divisors)에서 우리는 Weil divisor와 Cartier divisor가 기본적으로는 같은 것이며, Cartier divisor가 Weil divisor보다 조금 더 강한 조건으로 정의되었고, 따라서 더 나쁜 공간에서 정의된다는 점에서만 달랐다. 이 때 이 두 개념이 <em-ko>기본적으로 같다</em-ko>는 것은 [\[대수다양체\] §인자, ⁋명제 14](/ko/math/algebraic_varieties/divisors#prop14)의 결과로, 이 명제의 scheme 버전은 다음과 같다. 

::: 명제 14
Normal integral Noetherian scheme $X$가 주어졌다 하고, Cartier divisor $\{(U_i, f_i)\}$와 prime divisor $Y$가 주어질 때마다 $Y\cap U_i\neq\emptyset$이도록 하는 $i$를 택하자. 그럼 다음의 식

$$\{(U_i,f_i)\}\mapsto \sum_Y \ord_Y(f_i)\cdot Y$$

은 injective group homomorphism $\CaDiv(X) \rightarrow \Div(X)$를 정의하며, principal divisor를 principal divisor로 보낸다. 만일 $X$가 factorial이라면 이는 isomorphism이고, 따라서 $\CaCl(X)\cong \Cl(X)$이다.
:::
::: 증명
우선 위의 식이 $i$의 선택에 무관하다. $Y$가 $U_i$와 $U_j$를 모두 만난다면 $Y\cap U_i$와 $Y\cap U_j$는 irreducible space $Y$의 공집합이 아닌 두 열린부분집합이므로 서로 만나며, generic point $\eta$는 $Y$의 공집합이 아닌 모든 열린부분집합에 속하므로 $\eta\in U_i\cap U_j$이다. 그 위에서 $f_i/f_j$가 $\mathcal{O}_X^\times$의 section이므로 $f_i/f_j$는 $\mathcal{O}_{X,\eta}$의 unit이 되어 $\ord_Y(f_i)=\ord_Y(f_j)$이기 때문이다. 또 이 합이 유한합인 것은 [보조정리 11](#lem11)의 2번과 $X$가 유한히 많은 $U_i$로 덮인다는 것에서 따라온다. Cartier divisor의 덧셈이 $f_i$들의 곱이고 각각의 $\ord_Y$가 group homomorphism이므로 이 대응은 group homomorphism이며, $\divisor(f)=\{(X,f)\}$의 image가 [정의 13](#def13)의 $\divisor(f)$인 것은 정의 그대로이다.

Injectivity를 보이자. $D=\{(U_i,f_i)\}$의 image가 $0$이라 하면, 각각의 $i$에 대하여 $U_i$와 만나는 모든 prime divisor $Y$에서 $\ord_Y(f_i)=0$이다. 우리는 $f_i$가 $U_i$ 위의 invertible section임을 보인다. 이 절의 처음에서 본 등식 $\Gamma(V,\mathcal{O}_X)=\bigcap_{x\in V}\mathcal{O}_{X,x}$를 $f_i$와 $f_i^{-1}$에 적용하면, 각각의 $x\in U_i$에 대하여 $f_i\in \mathcal{O}_{X,x}^\times$임을 보이면 충분하다.

$R=\mathcal{O}_{X,x}$는 Noetherian normal local domain이고, $R$의 codimension $1$ prime ideal $\mathfrak{p}$는 $x$를 지나면서 $U_i$와 만나는 prime divisor $Y$에 대응하며 $R_\mathfrak{p}=\mathcal{O}_{X,\eta_Y}$이다. 그럼 [\[가환대수학\] §정칙국소환, ⁋정리 10](/ko/math/commutative_algebra/regular_local_rings#thm10)의 (S2) 조건에 의하여 $R$의 non-zerodivisor가 생성하는 principal ideal의 associated prime은 모두 codimension $1$이므로, [\[가환대수학\] §정칙국소환, ⁋명제 7](/ko/math/commutative_algebra/regular_local_rings#prop7)이 주는 등식

$$R=\bigcap_{\text{\scriptsize $\mathfrak{p}$ associated to a non-zerodivisor}}R_\mathfrak{p}$$

의 우변은 codimension $1$인 $\mathfrak{p}$들에 대한 교집합을 포함한다. 가정에 의하여 $\ord_Y(f_i)=0$이므로 $f_i$와 $f_i^{-1}$은 모든 codimension $1$ prime ideal에서의 localization에 속하고, 따라서 둘 다 $R$의 원소이므로 $f_i\in R^\times$이다. 곧 모든 $f_i$가 $U_i$ 위의 invertible section이므로, [정의 6](#def6)의 동치관계에 의하여 $D$는 $\{(U_i,1)\}$과 같은 Cartier divisor, 즉 $\CaDiv(X)$의 항등원이다.

이제 $X$가 factorial이라 하고 surjectivity를 보인다. Weil divisor $D=\sum_Y n_YY$가 주어졌다 하고 점 $x\in X$를 고정하자. $D$가 유한합이므로 $x$를 지나는 $Y$ 가운데 $n_Y\neq0$인 것은 유한히 많으며, 각각에 대하여 $\mathcal{O}_{X,x}$의 codimension $1$ prime ideal $\mathfrak{p}_Y$가 대응된다. $X$가 factorial이므로 $\mathcal{O}_{X,x}$는 UFD이고, [\[가환대수학\] §정칙성의 호몰로지 판정, ⁋보조정리 8](/ko/math/commutative_algebra/homological_criterion_for_regularity#lem8)의 1번에 의하여 $\mathfrak{p}_Y=(g_Y)$는 principal이다.

$f_x=\prod_Y g_Y^{n_Y}\in K(X)^\times$로 두자. 곱은 $x$를 지나는 유한히 많은 $Y$에 대한 것이다. 그럼 $E=\divisor(f_x)-D$는 유한히 많은 prime divisor들의 합이고, 구성에 의하여 $x$를 지나는 어떤 prime divisor도 $E$에 나타나지 않는다. 실제로 $x$를 지나는 prime divisor $Y'$에 대하여 $\ord_{Y'}(g_Y)$는 $Y'=Y$일 때 $1$이고 그렇지 않으면 $0$인데, 이는 $g_Y$가 $\mathcal{O}_{X,x}$의 prime element로서 $\mathfrak{p}_{Y'}$에 속하는 것이 $\mathfrak{p}_{Y'}=\mathfrak{p}_Y$인 것과 동치이기 때문이다. 따라서 $E$에 나타나는 prime divisor들의 합집합은 $x$를 담지 않는 닫힌집합이며, 그 여집합 $U_x$ 위에서 $\divisor(f_x)$와 $D$는 일치한다.

이렇게 얻은 열린집합들을 affine으로 줄여 $X$의 affine open cover $\{U_x\}$를 얻자. 그럼 $\divisor(f_x)$와 $\divisor(f_{x'})$이 모두 $U_x\cap U_{x'}$ 위에서 $D$와 일치하므로 $f_x/f_{x'}$는 겹침과 만나는 모든 prime divisor에서 $\ord$가 $0$이며, 위의 injectivity 논증을 열린집합 $U_x\cap U_{x'}$에 적용하면 이는 $\mathcal{O}_X^\times$의 section이다. 곧 $\{(U_x,f_x)\}$는 Cartier divisor이고 그 image가 $D$이다. 마지막으로 principal divisor들이 서로 대응되므로 quotient 사이의 동형 $\CaCl(X)\cong\Cl(X)$이 유도된다.
:::

[명제 14](#prop14)의 마지막 주장은 factorial scheme 위에서 두 인자 이론이 일치한다는 것이며, 이는 effective인 경우에 적용되던 [명제 5](#prop5)를 임의의 계수로 확장한 것이다. 여기에 [정리 10](#thm10)을 합치면 factorial인 경우 $\Cl(X)\cong\CaCl(X)\cong\Pic(X)$를 얻는다. 일반적인 normal scheme 위에서는 $\CaDiv(X)$의 image가 $\Div(X)$의 proper subgroup일 수 있고, 그 차이는 $X$의 singularity가 codimension $1$ 부분을 국소적으로 하나의 방정식으로 자르지 못하는 정도를 잰다.

## 선형계

이제 우리는 [\[대수다양체\] §선형계](/ko/math/algebraic_varieties/linear_systems)의 내용을 빠르게 되짚는다. Divisor $D$가 주어졌을 때 자연스러운 물음은 그 linear equivalence class 안에 어떠한 effective divisor가 들어 있는지이며, [정의 8](#def8)은 이 물음을 $\mathcal{O}_X(D)$의 global section에 대한 물음으로 바꾸어 준다.

::: 명제 15
Integral Noetherian scheme $X$와 Cartier divisor $D$에 대하여, $0\neq s\in \Gamma(X,\mathcal{O}_X(D))$마다 $D+\divisor(s)$는 effective Cartier divisor이며, 이 대응은 $D$와 linearly equivalent한 effective Cartier divisor 전체로의 surjection이다. 또, 두 section $s,s'$이 같은 divisor를 주는 것은 $s'/s\in \Gamma(X,\mathcal{O}_X)^\times$인 것과 동치이다.
:::
::: 증명
$D=\{(U_i,f_i)\}$라 하자. $s\in\Gamma(X,\mathcal{O}_X(D))$라는 것은 모든 $i$에 대하여 $sf_i\in \Gamma(U_i,\mathcal{O}_X)$라는 것이고, $D+\divisor(s)=\{(U_i,sf_i)\}$이므로 이는 정확히 $D+\divisor(s)$가 effective라는 것이다. 거꾸로 $D'$이 effective이고 $D'-D=\divisor(h)$라면 $D'=\{(U_i,hf_i)\}$이므로 $hf_i\in\Gamma(U_i,\mathcal{O}_X)$이고, 곧 $h\in \Gamma(X,\mathcal{O}_X(D))$이며 그 image가 $D'$이다.

마지막으로 $D+\divisor(s)=D+\divisor(s')$은 $\divisor(s'/s)=0$과 같고, [정의 6](#def6)의 동치관계에 의하여 이는 $s'/s$가 각각의 $U_i$ 위에서 $\mathcal{O}_X^\times$의 section인 것, 곧 $s'/s\in \Gamma(X,\mathcal{O}_X)^\times$인 것이다.
:::

따라서 $D$와 linearly equivalent한 effective divisor들은 $\Gamma(X,\mathcal{O}_X(D))$의 $0$이 아닌 section들을 $\Gamma(X,\mathcal{O}_X)^\times$의 작용으로 나눈 것과 일대일로 대응한다. $X$가 field $\mathbb{K}$ 위의 scheme이고 $\Gamma(X,\mathcal{O}_X)=\mathbb{K}$인 경우 이 quotient는 벡터공간의 projectivization이 되므로, [\[대수다양체\] §선형계, ⁋정의 2](/ko/math/algebraic_varieties/linear_systems#def2)를 복원한다.

::: 정의 16
Field $\mathbb{K}$ 위의 integral scheme $X$가 $\Gamma(X,\mathcal{O}_X)=\mathbb{K}$를 만족한다 하자. Invertible sheaf $\mathcal{L}$에 대하여 그 *complete linear system<sub>완비 선형계</sub>*은

$$\lvert \mathcal{L}\rvert=\mathbb{P}(\Gamma(X,\mathcal{L}))$$

이고, $\mathcal{L}$의 *linear system<sub>선형계</sub>*이란 부분공간 $V\subseteq \Gamma(X,\mathcal{L})$이 정의하는 $\mathbb{P}(V)\subseteq \lvert\mathcal{L}\rvert$이다.
:::

[명제 15](#prop15)에 의하여 $\mathcal{L}=\mathcal{O}_X(D)$인 경우 $\lvert\mathcal{L}\rvert$은 $D$와 linearly equivalent한 effective divisor들의 집합과 동일시되며, 이 때 이를 $\lvert D\rvert$로도 적는다. Linear system $\mathbb{P}(V)$에 대하여 $V$의 모든 section이 소멸하는 점들의 집합을 그 *base locus*라 부르며, base locus가 공집합인 linear system은 projective space로의 morphism을 주었다. ([\[대수다양체\] §선형계, ⁋정의 5](/ko/math/algebraic_varieties/linear_systems#def5)) 우리의 마지막 섹션은 이에 대한 것이다. 

## Ample invertible sheaf

$\mathcal{O}_X$-module $\mathcal{F}$가 *globally generated*라는 것은 각 점 $x$에서 stalk $\mathcal{F}_x$가 global section들의 germ으로 $\mathcal{O}_{X,x}$-module로서 생성되는 것이다. 이는 [\[대수다양체\] §사영공간의 코호몰로지, ⁋정의 4](/ko/math/algebraic_varieties/cohomology_of_projective_spaces#def4)의 evaluation map이 surjective라는 조건을 scheme 위로 옮긴 것이며, invertible sheaf $\mathcal{L}$의 경우 linear system $\mathbb{P}(V)$의 base locus가 공집합인 것과 $V$의 section들이 $\mathcal{L}$을 globally generate하는 것이 같은 조건이다.

Generating section들은 projective space로의 morphism을 결정한다. Ring $A$ 위의 scheme $X$와 invertible sheaf $\mathcal{L}$, 그리고 이를 globally generate하는 section $s_0,\ldots, s_n\in \Gamma(X,\mathcal{L})$이 주어졌다 하자. 각각의 $i$에 대하여

$$X_{s_i}=\{x\in X\mid \text{$(s_i)_x$ generates $\mathcal{L}_x$}\}$$

는 열린집합이다. 이는 $\mathcal{L}$의 trivializing open set 위에서 $s_i$는 하나의 함수에 대응되고, 그 함수가 unit이 되는 점들의 모임은 열린집합이기 때문이다. 또 $s_i$들이 $\mathcal{L}$을 globally generate하므로 $\{X_{s_i}\}$는 $X$의 open cover이며, $X_{s_i}$ 위에서는 $s_i$가 $\mathcal{L}$의 trivialization을 주므로 각각의 $j$에 대하여 $s_j/s_i\in \Gamma(X_{s_i},\mathcal{O}_X)$가 잘 정의된다. 이제 $D_+(\x_i)$는 $\Spec A[\x_0,\ldots,\x_n]_{(\x_i)}$와 isomorphic하므로 ([§사영공간과 Proj 구성, ⁋정리 10](/ko/math/scheme_theory/projective_schemes#thm10)), ring homomorphism

$$A[\x_0,\ldots, \x_n]_{(\x_i)} \rightarrow \Gamma(X_{s_i},\mathcal{O}_X);\qquad \frac{\x_j}{\x_i}\mapsto \frac{s_j}{s_i}$$

는 [§아핀스킴, ⁋정리 13](/ko/math/scheme_theory/affine_schemes#thm13)에 의하여 morphism $X_{s_i} \rightarrow D_+(\x_i)$를 준다. 교집합 위에서 이 morphism들은 $s_k/s_i=(s_k/s_j)(s_j/s_i)$에 의해 서로 일치하므로, 각각의 $X_{s_i}$를 affine open subset들로 덮어 얻은 $X$의 affine open cover에 [§스킴 사이의 사상, ⁋명제 1](/ko/math/scheme_theory/morphism_of_schemes#prop1)을 적용하면 이들은 하나의 morphism

$$\varphi:X \rightarrow \mathbb{P}^n_A$$

을 정의한다. 즉, $\mathcal{L}$의 generating section을 택하는 것은 $X$를 projective space 안에서 나타내는 방법을 택하는 것이다.

이 때 $\mathcal{L}$ 자신은 $\varphi$로부터 되찾아진다. 곧 $\mathcal{L}\cong \varphi^\ast\mathcal{O}(1)$이며 이 isomorphism이 $s_i$를 $\varphi^\ast\x_i$로 보낸다. 실제로 $\x_i$는 $D_+(\x_i)$ 위에서 $\mathcal{O}(1)$을 생성하고 $\varphi$는 $X_{s_i}$를 $D_+(\x_i)$ 안으로 보내므로 $\varphi^\ast\x_i$는 $X_{s_i}$ 위에서 $\varphi^\ast\mathcal{O}(1)$을 trivialize하며, $s_i$는 같은 열린집합 위에서 $\mathcal{L}$을 trivialize한다. overlap $X_{s_i}\cap X_{s_j}$ 위에서 두 trivialization의 transition function은 각각 $s_j/s_i$와 $\varphi^\ast(\x_j/\x_i)$인데 $\varphi$의 구성이 이 둘을 같게 두었으므로, $s_i\mapsto \varphi^\ast\x_i$가 주는 각 $X_{s_i}$ 위의 isomorphism들이 overlap 위에서 일치하여 $X$ 전체의 isomorphism으로 붙는다.

::: 정의 17
Noetherian ring $A$와 finite type $A$-scheme $X$ 위의 invertible sheaf $\mathcal{L}$이 *very ample*이라는 것은, $\mathcal{L}$을 globally generate하는 유한 개의 section $s_0,\ldots, s_n\in \Gamma(X,\mathcal{L})$이 존재하여 이들이 정의하는 morphism $\varphi:X \rightarrow \mathbb{P}^n_A$가 locally closed embedding인 것이다. ([§닫힌 부분스킴, ⁋정의 8](/ko/math/scheme_theory/closed_subschemes#def8))
:::

따라서, very ample invertible sheaf는 $X$를 projective space의 subspace로 실현하는 정보로, $X$가 그 자체로 projective space 안에 놓여 있지 않더라도 이를 통해 좌표를 부여할 수 있다. 

그러나 일반적으로 $\mathcal{L}$이 globally generated인 것은 강한 조건이다. 예를 들어 section들이 $\mathcal{L}$을 globally generate하지 못하면 $\varphi$ 자체가 정의되지 않는다. 이러한 문제를 해결하기 위해 우리가 사용하던 것은 $\mathcal{L}$을 여러 번 tensor하는 것이다. 곱셈 $\Gamma(X,\mathcal{L})^{\otimes m} \rightarrow \Gamma(X,\mathcal{L}^{\otimes m})$이 $\mathcal{L}$의 section들로부터 $\mathcal{L}^{\otimes m}$의 section을 만들어 주며, 일반적으로 그 image 바깥에도 section이 존재하므로 $m$이 커질수록 다룰 수 있는 section이 많아진다. 가령 $\mathbb{P}^n$ 위에서 $\Gamma(\mathcal{O}(1))$은 일차식들이 이루는 $n+1$차원 공간인 반면 $\Gamma(\mathcal{O}(m))$은 degree $m$ homogeneous polynomial들이 이루는 $\binom{n+m}{n}$차원 공간이다.

그렇다면 $\mathcal{L}^{\otimes m}$이 very ample이 되는 $m>0$이 존재하는지를 물을 수 있고, [\[대수다양체\] §선형계, ⁋정의 10](/ko/math/algebraic_varieties/linear_systems#def10)은 실제로 이를 ample의 정의로 삼았다. 그러나 이 서술은 ambient projective space를 경유하므로 $X$가 Noetherian ring 위의 finite type scheme이라는 가정 없이는 쓸 수 없다. 우리는 대신 twist가 sheaf를 얼마나 잘 펴는지만을 조건으로 삼아 임의의 Noetherian scheme에서 통하는 정의를 택한다.

::: 정의 18
Noetherian scheme $X$ 위의 invertible sheaf $\mathcal{L}$이 *ample*이라는 것은, 임의의 coherent sheaf $\mathcal{F}$에 대하여 ([§준연접층, ⁋정의 11](/ko/math/scheme_theory/quasicoherent_sheaves#def11)) 적당한 $n_0$가 존재하여 모든 $n\geq n_0$에 대해 $\mathcal{F}\otimes_{\mathcal{O}_X}\mathcal{L}^{\otimes n}$이 globally generated인 것이다.
:::

이 정의는 section의 존재만을 요구하며 projective space로의 morphism을 직접 언급하지 않는다. 여기에서 조건을 모든 coherent sheaf에 대하여 요구하는 것이 본질적으로, 만일 $\mathcal{F}=\mathcal{O}_X$만 요구한다면, 즉 $\mathcal{L}^{\otimes n}$이 globally generated라는 조건을 요구한다면 이는 $X$에 대한 정보를 전혀 담지 못한다. 반면 임의의 $\mathcal{F}$들에 대해 이 조건을 요구하면 $\mathcal{L}$의 twist가 $X$ 위의 모든 국소적인 자료를 global section으로 끌어올리는지를 묻게 되며, 이것이 embedding의 존재를 대신할 만큼 강한 조건이 된다. 다음은 이 정의로부터 곧바로 얻어지는 성질들이다.

::: 명제 19
Noetherian scheme $X$ 위의 invertible sheaf $\mathcal{L}$에 대하여 다음이 성립한다.

1. $X$가 affine이면 $\mathcal{L}$은 언제나 ample이다.
2. $m\geq 1$에 대하여, $\mathcal{L}$이 ample인 것과 $\mathcal{L}^{\otimes m}$이 ample인 것은 동치이다.
3. $\mathcal{L}$이 ample이고 invertible sheaf $\mathcal{M}$이 globally generated이면 $\mathcal{L}\otimes_{\mathcal{O}_X}\mathcal{M}$ 또한 ample이다.
:::
::: 증명
1번의 경우, $X=\Spec A$라 하고 coherent sheaf $\mathcal{F}$를 택하자. $\mathcal{L}$이 invertible sheaf이므로 $\mathcal{L}^{\otimes n}$은 각 점의 열린근방 위에서 $\mathcal{O}_X$와 동형이고, 따라서 $\mathcal{F}\otimes\mathcal{L}^{\otimes n}$은 그 근방 위에서 $\mathcal{F}$와 동형이다. quasi-coherence는 국소적인 조건이므로 이로부터 $\mathcal{F}\otimes\mathcal{L}^{\otimes n}$은 quasi-coherent sheaf이고, 곧 적당한 $A$-module $M$의 associated sheaf $\widetilde M$이다. ([§준연접층, ⁋정리 10](/ko/math/scheme_theory/quasicoherent_sheaves#thm10)) 그런데 $\widetilde M$의 stalk은 $M_\mathfrak{p}$이고 ([§준연접층, ⁋명제 5](/ko/math/scheme_theory/quasicoherent_sheaves#prop5)) 이는 global section module $M$의 image로 생성되므로 $\widetilde M$은 globally generated이다. 따라서 $n_0=0$으로 두면 된다.

2번에서 $\mathcal{L}$이 ample이면, coherent sheaf $\mathcal{F}$에 대해 $n_0$를 택하여 $n\geq n_0$마다 $\mathcal{F}\otimes\mathcal{L}^{\otimes n}$이 globally generated이도록 하자. 그럼 $k\geq n_0$에 대하여 $mk\geq n_0$이므로 $\mathcal{F}\otimes(\mathcal{L}^{\otimes m})^{\otimes k}$은 globally generated이다. 거꾸로 $\mathcal{L}^{\otimes m}$이 ample이라 하자. 각각의 $j=0,1,\ldots, m-1$에 대하여 $\mathcal{F}\otimes\mathcal{L}^{\otimes j}$ 또한 coherent sheaf이므로 $k_j$가 존재하여 $k\geq k_j$마다 $\mathcal{F}\otimes\mathcal{L}^{\otimes j}\otimes(\mathcal{L}^{\otimes m})^{\otimes k}$이 globally generated이다. $k_\ast=\max_jk_j$로 두면 $n\geq mk_\ast$인 임의의 $n$은 $n=mk+j$ ($k\geq k_\ast$, $0\leq j<m$)로 적히므로 $\mathcal{F}\otimes\mathcal{L}^{\otimes n}$은 globally generated이다.

3번을 위해 우선 두 globally generated $\mathcal{O}_X$-module $\mathcal{F},\mathcal{G}$의 tensor product가 다시 globally generated임을 관찰한다. Stalk $(\mathcal{F}\otimes\mathcal{G})_x\cong \mathcal{F}_x\otimes_{\mathcal{O}_{X,x}}\mathcal{G}_x$는 $\mathcal{F}_x$와 $\mathcal{G}_x$의 generator들의 tensor로 생성되고, 이들은 global section들의 germ의 tensor이기 때문이다. 이제 coherent sheaf $\mathcal{F}$에 대하여 $\mathcal{L}$의 ampleness가 주는 $n_0$를 택하면, $n\geq n_0$에 대하여

$$\mathcal{F}\otimes(\mathcal{L}\otimes\mathcal{M})^{\otimes n}\cong(\mathcal{F}\otimes\mathcal{L}^{\otimes n})\otimes\mathcal{M}^{\otimes n}$$

에서 첫째 인자는 globally generated이고 둘째 인자는 globally generated인 sheaf의 tensor power이므로 globally generated이다. 따라서 좌변 또한 globally generated이다.
:::

[명제 19](#prop19)의 1번에 의하면 affine scheme 위에서는 어떠한 invertible sheaf도 ample이므로, 이 조건은 $X$가 affine일 때 아무런 대상도 걸러내지 못한다. Ampleness가 실제로 대상을 구별하는 것은 $X$가 affine이 아닐 때이며, 특히 $X$가 Noetherian ring $A$ 위에서 projective인 경우 $\mathcal{L}$이 ample인 것과 적당한 $m>0$에 대하여 $\mathcal{L}^{\otimes m}$이 very ample인 것이 동치가 된다. 

---

**참고문헌**

**[Vak]** R. Vakil, *The rising sea: Foundations of algebraic geometry*. Available [online](https://math.stanford.edu/~vakil/216blog/).
