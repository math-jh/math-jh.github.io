---
title: "완전교차"
description: "Global section들의 가족이 정의하는 vanishing scheme, locally principal embedding과 effective Cartier divisor를 다루고, regular sequence로 잘리는 complete intersection의 codimension이 자르는 방정식의 개수와 일치함을 보인다."
excerpt: "Vanishing scheme의 codimension과 complete intersection"

categories: [Math / Scheme Theory]
permalink: /ko/math/scheme_theory/complete_intersections
sidebar: 
    nav: "scheme_theory-ko"

date: 2025-03-08
weight: 20

published: false

drift_needed: true

---

Closed subscheme의 중요한 예시 중 하나는 [§닫힌 부분스킴, ⁋정의 7](/ko/math/scheme_theory/closed_subschemes#def7)에서 정의한 vanishing scheme이며, 이에 대한 motivation은 당연히 유클리드 공간 $\mathbb{R}^n$과 그 위에서 정의되는 함수 $f: \mathbb{R}^n \rightarrow \mathbb{R}$에 대하여 $f^{-1}(0)$으로 정의되는 $\mathbb{R}^n$의 hypersurface $f=0$이다. 

한편 우리는 더 일반적으로 global section들의 (유한한) family $s_1,\ldots, s_k\in \Gamma(X, \mathcal{O}_X)$가 주어졌을 때 이들이 정의하는 vanishing scheme $Z(s_1,\ldots, s_k)$에도 관심이 있다. 직관적으로 이는 우선 $X$에서 global section $s_1$을 사용하여 만든 vanishing scheme $\iota_1:Z(s_1)\hookrightarrow X$을 생각한 후, $Z(s_1)$의 global section 

$$s_2\vert_{Z(s_1)}=\iota_1^\sharp(X)(s_2)\in(\iota_1)_\ast \mathcal{O}_{Z(s_1)}(X)=\Gamma(Z(s_1), \mathcal{O}_{Z(s_1)})$$

을 통해 $Z(s_1)$에서 $s_2\vert_{Z(s_1)}$의 vanishing scheme을 찾아나가는 것을 반복하여 얻어질 것이며, 물론 이를 위해서는 이 과정이 $s_1, \ldots, s_k$의 순서에 무관하게 같은 scheme을 주어야 할 것이다. 


## Locally principal embedding

::: 정의 1
Closed embedding $\iota: Z \hookrightarrow X$가 *locally principal*이라는 것은 $X$의 적당한 open cover $\{U_i\}$가 존재하여, $\iota$의 공역을 각각의 $U_i$로 제한하여 얻어지는 closed embedding들

$$\iota\vert^{U_i}: \iota^{-1}(U_i) \rightarrow U_i$$

마다 적당한 $s_i\in \Gamma(U_i, \mathcal{O}_X)$가 존재하여 두 closed embedding $\iota\vert^{U_i}$와 $Z(s_i)\hookrightarrow U_i$가 isomorphic한 것이다. 
:::

그럼 만일 $\iota: Z\hookrightarrow X$가 locally principal이라면, 정의의 $U_i$들 각각을 affine open set들로 덮고 $s_i$들을 이들로 제한시키면 $\{U_i\}$들이 affine open covering이라 가정하여도 된다. 

::: 정의 2
Closed embedding $\iota: Z \hookrightarrow X$가 *effective Cartier divisor<sub>유효 카르티에 인자</sub>*라는 것은 $X$의 affine open cover $\{U_i=\Spec A_i\}$가 존재하여, 각각의 closed embedding들

$$\iota\vert^{U_i}:\iota^{-1}(U_i) \rightarrow U_i$$

마다 적당한 non-zerodivisor $s_i\in A_i=\Gamma(U_i, \mathcal{O}_X)$가 존재하여 두 closed embedding $\iota\vert^{U_i}$와 $Z(s_i)\hookrightarrow U_i$가 isomorphic한 것이다.
:::

정의에 의해 locally principal embedding은 대략적으로 ideal sheaf가 (국소적으로는) 하나의 원소로 생성되는 것, 즉 principal ideal인 것이고 effective Cartier divisor는 적절한 affine cover를 잡으면 이 하나의 원소가 non-zerodivisor이도록 할 수 있는 것이다. 특히 임의의 effective Cartier divisor는 locally principal이다. 이 대략적인 서술을 ideal sheaf의 언어로 정확히 적어두자. ([§닫힌 부분스킴, ⁋정의 5](/ko/math/scheme_theory/closed_subschemes#def5))

::: 명제 3
Closed embedding $\iota: Z\hookrightarrow X$와 그 ideal sheaf $\mathcal{I}_{Z/X}$에 대하여 다음이 성립한다.

1. $\iota$가 locally principal인 것은, $X$의 임의의 점이 affine open neighborhood $U=\Spec A$를 가져 $A$의 ideal $\mathcal{I}_{Z/X}(U)$가 하나의 원소로 생성되는 것과 동치이다.
2. $\iota$가 effective Cartier divisor인 것은, $X$의 임의의 점이 affine open neighborhood $U=\Spec A$를 가져 $\mathcal{I}_{Z/X}(U)$가 $A$-module로서 rank $1$의 free module, 곧 $A$ 자신과 isomorphic한 것과 동치이다.
:::
::: 증명
Affine open subset $U=\Spec A$ 위에서 $\iota$를 공역에 대해 제한한 것은 ideal $\mathfrak{a}=\mathcal{I}_{Z/X}(U)$가 정의하는 closed embedding $Z(\mathfrak{a})\hookrightarrow U$이며, 서로 다른 두 ideal은 서로 다른 closed subscheme을 정의한다. ([§닫힌 부분스킴, ⁋명제 3](/ko/math/scheme_theory/closed_subschemes#prop3)) 따라서 $\iota\vert^U$가 $Z(s)\hookrightarrow U$와 isomorphic한 것은 $\mathfrak{a}=(s)$인 것과 같다.

그럼 1번은 [정의 1](#def1) 직후에 관찰한 대로 locally principal embedding의 cover를 affine으로 잡아도 되는 것에서 곧바로 따라온다.

2번을 보기 위해 $s\in A$에 대하여 $A \rightarrow (s)$, $a\mapsto as$를 생각하자. 이는 언제나 surjective이고 그 kernel이 $\ann(s)$이므로, 이것이 isomorphism인 것과 $s$가 non-zerodivisor인 것은 동치이다. 따라서 $\mathfrak{a}=(s)$이고 $s$가 non-zerodivisor라면 $\mathfrak{a}\cong A$이다. 거꾸로 $\mathfrak{a}$가 rank $1$의 free $A$-module이라면 그 기저를 이루는 원소 $s$에 대하여 $\mathfrak{a}=(s)$이고 $\ann(s)=0$이므로, $s$는 non-zerodivisor이다.
:::

곧 effective Cartier divisor란 ideal sheaf가 국소적으로 structure sheaf 자신과 구별되지 않는 closed subscheme이고, locally principal이라는 조건은 여기에서 generator가 하나라는 것만 남기고 그 generator가 관계식을 갖지 않는다는 요구를 덜어낸 것이다. 두 조건이 실제로 다르다는 것은 [예시 5](#ex5)에서 확인한다.

## Cartier 인자

우선 하나의 non-zerodivisor가 잘라내는 경우, 곧 effective Cartier divisor의 이론을 끝까지 살펴본다. 출발점은 그 codimension이 언제나 $1$이라는 것이다.

::: 명제 4
Locally Noetherian scheme $X$ 위의 effective Cartier divisor $\iota:Z\hookrightarrow X$에 대하여, $Z$의 모든 irreducible component는 $X$에서 codimension $1$을 갖는다.
:::
::: 증명
Codimension은 국소적으로 계산되므로, [정의 2](#def2)의 affine open cover $\{U_i=\Spec A_i\}$ 가운데 하나를 택하여 $Z\cap U_i=Z(s_i)$이고 $s_i\in A_i$가 non-zerodivisor인 경우만 보면 충분하다. $Z$의 irreducible component $W$가 $U_i$와 만난다면 $W\cap U_i$는 $Z(s_i)$의 irreducible component이다. [§차원, ⁋명제 12](/ko/math/scheme_theory/dimension#prop12)에 의하여 $Z(s_i)$의 component는 $U_i$에서 codimension $0$이거나 $1$인데, codimension $0$인 component는 $U_i$ 자신의 irreducible component, 즉 $A_i$의 minimal prime ideal $\mathfrak{p}$에 대응된다. 만일 $W\cap U_i$가 그러한 component라면 $s_i$가 그 위에서 소멸하므로 $s_i\in \mathfrak{p}$이다. 그런데 Noetherian ring에서 non-zerodivisor는 어떠한 minimal prime ideal에도 속하지 않으므로 ([\[가환대수학\] §동반소아이디얼, ⁋정리 7](/ko/math/commutative_algebra/associated_primes#thm7)) 이는 $s_i$가 non-zerodivisor라는 가정에 모순이다. 따라서 $W\cap U_i$의 codimension은 $1$이고, [§차원, ⁋명제 8](/ko/math/scheme_theory/dimension#prop8)에 의하여 $W$의 $X$에서의 codimension 또한 $1$이다.
:::

이로부터 앞에서 미룬 것, 곧 locally principal이지만 effective Cartier divisor는 아닌 closed embedding이 실제로 존재한다는 것을 확인할 수 있다.

::: 예시 5
$X=\Spec \mathbb{K}[\x,\y]/(\x\y)$를 평면의 두 좌표축의 합집합이라 하고, $Z=Z(\x)$라 하자. 이는 global section $\x$ 하나의 vanishing scheme이므로, [정의 1](#def1)에서 $X$ 자신을 cover로 택하면 $Z\hookrightarrow X$가 locally principal임을 안다.

그러나 이는 effective Cartier divisor가 아니다. $\mathbb{K}[\x,\y]/(\x\y,\x)\cong\mathbb{K}[\y]$이므로 $Z$는 $\y$-축이고, 이는 $X$의 두 irreducible component 가운데 하나이므로 $X$에서 codimension $0$을 갖는다. 그런데 [명제 4](#prop4)에 의하여 effective Cartier divisor의 irreducible component는 codimension $1$이어야 한다.

대수적으로는 [명제 3](#prop3)의 2번이 같은 것을 말해준다. 원점을 담는 affine open subset $U=\Spec A$를 어떻게 택하더라도 $U$는 두 좌표축과 모두 만나므로 $A$ 안에서 $\y$는 $0$이 아니고, $\mathcal{I}_{Z/X}(U)$를 생성하는 $\x$는 이를 죽이는 zerodivisor이다. 곧 이 ideal은 결코 free module이 될 수 없다.
:::

[예시 5](#ex5)에서 문제가 된 것은 원점에서의 local ring이 domain조차 아니었다는 것이다. 이러한 병리를 배제하면 [명제 4](#prop4)의 역이 성립한다.

::: 명제 6
Locally Noetherian integral scheme $X$의 모든 local ring $\mathcal{O}_{X,x}$가 UFD라 하자. 그럼 codimension $1$인 임의의 integral closed subscheme $\iota:Z\hookrightarrow X$는 effective Cartier divisor이다.
:::
::: 증명
$X$가 integral이므로 임의의 affine open subset $U=\Spec A$에 대하여 $A$는 Noetherian domain이고, 특히 $A$의 $0$이 아닌 원소는 모두 non-zerodivisor이다.

$Z$와 만나지 않는 점에 대해서는 볼 것이 없다. $Z$가 닫힌집합이므로 그러한 점은 $Z$와 만나지 않는 affine open neighborhood를 가지며, 그 위에서 $Z$는 $Z(1)=\emptyset$이어서 [정의 2](#def2)의 조건이 $s=1$로 충족되기 때문이다.

이제 $z\in Z$를 택하고 $z$를 담는 affine open subset $U=\Spec A$를 잡자. $Z$가 integral이므로 $\mathfrak{p}=\mathcal{I}_{Z/X}(U)$는 prime ideal이며, [§차원, ⁋명제 8](/ko/math/scheme_theory/dimension#prop8)에 의하여 $Z$가 codimension $1$이라는 것은 $\mathfrak{p}$가 codimension $1$이라는 것이다. $z$에 대응하는 prime ideal을 $\mathfrak{q}\supseteq \mathfrak{p}$라 하면 가정에 의하여 $A_\mathfrak{q}=\mathcal{O}_{X,z}$는 Noetherian local UFD이고, $\mathfrak{p}A_\mathfrak{q}$는 codimension $1$인 prime ideal이다. 그럼 [\[가환대수학\] §정칙성의 호몰로지 판정, ⁋보조정리 8](/ko/math/commutative_algebra/homological_criterion_for_regularity#lem8)의 1번에 의하여 $\mathfrak{p}A_\mathfrak{q}$는 principal이다.

$\mathfrak{p}A_\mathfrak{q}=(t)$라 하고, $\mathfrak{q}$ 바깥의 원소는 $A_\mathfrak{q}$에서 unit이므로 $t=f/1$이 되도록 $f\in A$를 택하자. $\mathfrak{p}A_\mathfrak{q}\cap A=\mathfrak{p}$이므로 $f\in \mathfrak{p}$이다. 한편 $A$가 Noetherian이므로 $\mathfrak{p}$는 유한개의 원소 $p_1,\ldots, p_n$이 생성하고, 각각의 $p_i/1$이 $(f)A_\mathfrak{q}$에 속하므로 $g_i\notin \mathfrak{q}$가 존재하여 $g_ip_i\in (f)$이다. $g=g_1\cdots g_n$으로 두면 $\mathfrak{q}$가 prime이므로 $g\notin\mathfrak{q}$이고, $A_g$에서 $\mathfrak{p}A_g=(f)$이다.

그럼 $D(g)$는 $z$의 affine open neighborhood로서 그 위에서 $Z$는 $Z(f)$이며, $A_g$가 domain이고 $f\neq 0$이므로 $f$는 non-zerodivisor이다. 이렇게 얻은 열린집합들이 $X$를 덮으므로 [정의 2](#def2)에 의하여 $\iota$는 effective Cartier divisor이다.
:::

이 가정은 공허하지 않다. 모든 local ring이 regular local ring인 scheme이 그러한데, regular local ring이 UFD라는 것은 Auslander-Buchsbaum의 정리로 이 글에서 증명하지 않고 [\[가환대수학\] §정칙성의 호몰로지 판정](/ko/math/commutative_algebra/homological_criterion_for_regularity)에 위임한다. 곧 smooth한 대상 위에서는 codimension $1$이라는 위상적인 조건만으로 방정식 하나를 되찾을 수 있다.

이제 effective Cartier divisor들을 한데 모으면 group이 얻어진다. 이는 [\[대수다양체\] §인자](/ko/math/algebraic_varieties/divisors)에서 variety에 대하여 살펴본 것의 scheme 판본으로, 국소적인 방정식 자료만으로 서술된다. 아래에서 $K(U)$는 [§스킴의 대수구조, ⁋정의 12](/ko/math/scheme_theory/algebra_of_schemes#def12)의 total quotient ring이다.

::: 정의 7
Locally Noetherian scheme $X$ 위의 *Cartier divisor<sub>카르티에 인자</sub>*란 $X$의 affine open cover $\{U_i\}$와 각각의 $f_i\in K(U_i)^\times$가 이루는 자료 $\{(U_i,f_i)\}$로서, 임의의 $i,j$에 대하여 $f_i/f_j$가 $U_i\cap U_j$ 위에서 $\mathcal{O}_X^\times$의 section인 것이다. 두 자료가 공통의 세분 위에서 이 조건을 만족하며 일치하면 같은 Cartier divisor로 본다. 이들은 $\{(U_i,f_i)\}+\{(V_j,g_j)\}=\{(U_i\cap V_j, f_ig_j)\}$를 연산으로 하여 group을 이루며, 이를 $\CaDiv(X)$로 적는다.
:::

$f_i$들이 모두 $\Gamma(U_i,\mathcal{O}_X)$에 속하는 Cartier divisor를 *effective*라 부른다. 이 이름이 [정의 2](#def2)와 충돌하지 않는다는 것이 다음의 내용이다.

::: 명제 8
Locally Noetherian scheme $X$에 대하여, effective Cartier divisor $\iota:Z\hookrightarrow X$들과 $\CaDiv(X)$의 effective한 원소들은 서로 일대일로 대응한다.
:::
::: 증명
Effective한 $D=\{(U_i,f_i)\}$가 주어졌다 하자. $f_i\in \Gamma(U_i,\mathcal{O}_X)$가 $K(U_i)^\times$의 원소라는 것은 $f_i$가 non-zerodivisor라는 것이다. 각 $U_i$ 위에서 ideal $(f_i)$를 생각하면, $f_i/f_j$가 겹침 위에서 unit이므로 이들은 겹침 위에서 같은 ideal sheaf를 정의하고, 따라서 [§닫힌 부분스킴, ⁋명제 6](/ko/math/scheme_theory/closed_subschemes#prop6)에 의하여 $X$의 closed subscheme $Z$ 하나로 붙는다. 이 $Z$는 구성에 의하여 [정의 2](#def2)의 조건을 만족한다.

거꾸로 effective Cartier divisor $\iota:Z\hookrightarrow X$와 [정의 2](#def2)의 자료 $\{(U_i,s_i)\}$가 주어졌다 하자. $s_i$가 non-zerodivisor이므로 $s_i\in K(U_i)^\times$이다. 겹침 위에서는 $\mathcal{I}_{Z/X}$가 $s_i$로도 $s_j$로도 생성되므로 각 점에서 $s_i=us_j$인 local unit $u$가 존재하며, 이러한 $u$는 $s_i$와 $s_j$가 non-zerodivisor라는 것에서 유일하게 결정되어 겹침 전체의 section으로 붙는다. 곧 $\{(U_i,s_i)\}$는 effective한 Cartier divisor이다. 두 구성이 서로 역이라는 것은 어느 쪽이든 $\mathcal{I}_{Z/X}$를 국소적으로 생성하는 원소를 주고받는 것이므로 곧바로 확인된다.
:::

$f\in K(X)^\times$ 하나가 정의하는 $\{(X,f)\}$ 꼴의 Cartier divisor를 *principal divisor*라 부르며, 이들이 이루는 subgroup으로 $\CaDiv(X)$를 나눈 것이 $\Pic(X)$와 일치한다. 다만 이 동형을 적으려면 각 divisor에 invertible sheaf를 대응시켜야 하고 invertible sheaf는 이 글의 범위를 벗어나므로, 여기에서는 대응의 존재만 밝히고 넘어간다. Variety 수준에서의 같은 그림은 [\[대수다양체\] §선다발과 벡터다발](/ko/math/algebraic_varieties/line_bundles)에 있다.

## 여차원과 완전교차

이제 도입부에서 예고한, 여러 global section들의 family가 정의하는 vanishing scheme을 구성한다. Scheme $X$와 global section들 $s_1,\ldots, s_k\in \Gamma(X, \mathcal{O}_X)$가 주어졌다 하자. 각 affine open set $U=\Spec A$ 위에서 $s_i$는 $A$의 원소 $s_i\vert_U$로 제한되며, 우리는 ideal $(s_1\vert_U,\ldots, s_k\vert_U)$가 정의하는 $U$의 closed subscheme을 생각할 수 있다. 이들은 $U$를 옮겨다닐 때 서로 합치되어 $X$의 closed subscheme을 정의하는데, 이를 $Z(s_1,\ldots, s_k)$로 적고 $s_1,\ldots, s_k$의 *vanishing scheme*이라 부른다. 정의하는 ideal $(s_1,\ldots, s_k)$는 $s_i$들의 순서에 무관하므로 $Z(s_1,\ldots, s_k)$ 또한 순서에 무관하며, 도입부에서 말한 "$Z(s_1)$에서 $s_2$의 vanishing scheme을 찾아나가는" 과정은 scheme-theoretic 교집합

$$Z(s_1,\ldots, s_k)=Z(s_1)\cap \cdots\cap Z(s_k)$$

으로 정확히 실현된다. 각 affine open 위에서 $(s_1,\ldots, s_k)=\sum_{i=1}^k(s_i)$이기 때문이다.

이제 이를 여러 번 잘라낸 일반적인 경우를 정의한다. 핵심은 자르는 section들이 단순한 non-zerodivisor를 넘어 *regular sequence*를 이루어야 한다는 것이다.

::: 정의 9
Locally Noetherian scheme $X$의 closed embedding $\iota:Z\hookrightarrow X$가 codimension $k$의 *complete intersection<sub>완전교차</sub>*, 혹은 codimension $k$의 *regular embedding*이라는 것은 $X$의 affine open cover $\{U_i=\Spec A_i\}$가 존재하여, 각각의 $U_i$에 대해 $Z\cap U_i=Z(s_{i,1},\ldots, s_{i,k})$이고 $(s_{i,1},\ldots, s_{i,k})$가 [\[가환대수학\] §정칙국소환, ⁋정의 2](/ko/math/commutative_algebra/regular_local_rings#def2)의 의미에서 $A_i$-regular sequence인 것이다.
:::

엄밀히는 [정의 9](#def9)의 성질은 국소적으로만 regular sequence를 요구하므로 *local complete intersection<sub>국소 완전교차</sub>*이라 부르는 것이 정확하다. 한편 $k=1$의 complete intersection은 정확히 effective Cartier divisor인데, regular sequence의 첫 원소는 그저 $(s)$가 proper이도록 하는 non-zerodivisor이기 때문이다.

Regular sequence라는 조건 자체는 원소를 나열하는 순서에 의존하며, 순서를 바꾸면 실제로 깨지는 예가 있다. ([\[가환대수학\] §코쥴 복합체, ⁋예시 11](/ko/math/commutative_algebra/koszul_complex#ex11)) 그러나 이 의존성은 [정의 9](#def9)에는 남지 않는다. $\mathfrak{p}$가 $(s_{i,1},\ldots, s_{i,k})$를 포함하는 $A_i$의 prime ideal이라면 localization이 exact이므로 $(s_{i,1},\ldots, s_{i,k})$는 $(A_i)_\mathfrak{p}$-regular sequence이고, Noetherian local ring에서는 maximal ideal에 속하는 regular sequence를 임의로 재배열하여도 다시 regular sequence가 되므로 ([\[가환대수학\] §코쥴 복합체, ⁋따름정리 10](/ko/math/commutative_algebra/koszul_complex#cor10)) 재배열한 열 또한 $Z\cap U_i$의 모든 점에서 regular sequence이기 때문이다. 도입부에서 요구하였던 순서 무관성이 회수되는 것이 이것이다.

다음 명제는 complete intersection이 그 이름값을 한다는 것, 즉 codimension이 자르는 방정식의 개수와 정확히 일치함을 보여준다.

::: 명제 10
Codimension $k$의 complete intersection $\iota:Z\hookrightarrow X$의 모든 irreducible component는 $X$에서 codimension $k$를 갖는다.
:::
::: 증명
다시 국소적이므로 [정의 9](#def9)의 cover 가운데 하나에 대해 $X=\Spec A$, $Z=Z(s_1,\ldots, s_k)$이고 $(s_1,\ldots, s_k)$가 $A$-regular sequence인 경우만 보면 충분하다. $Z$의 irreducible component $W$에 대응되는 $A$의 prime ideal을 $\mathfrak{p}$라 하면 $\mathfrak{p}$는 $A/(s_1,\ldots, s_k)$의 minimal prime이므로 

$$\dim A_\mathfrak{p}/(s_1,\ldots, s_k)=\dim\bigl(A/(s_1,\ldots, s_k)\bigr)_\mathfrak{p}=0$$

이다. 한편 [§차원, ⁋명제 8](/ko/math/scheme_theory/dimension#prop8)에 의하여 $\codim_X W=\dim A_\mathfrak{p}$이므로, $\dim A_\mathfrak{p}=k$임을 보이면 된다. 

이를 위해 다음 사실을 보인다.

> Noetherian local ring $(R,\mathfrak{m})$의 non-zerodivisor $s\in\mathfrak{m}$에 대하여 $\dim R/(s)=\dim R-1$이다.

[§차원, ⁋명제 12](/ko/math/scheme_theory/dimension#prop12)을 $\Spec R$에 적용하면 $V(s)$의 모든 component는 codimension $0$ 또는 $1$이고, $s$가 non-zerodivisor이므로 ([\[가환대수학\] §동반소아이디얼, ⁋정리 7](/ko/math/commutative_algebra/associated_primes#thm7)) $s$는 어떠한 minimal prime에도 속하지 않아 codimension $0$인 component는 없다. 따라서 $V(s)$의 모든 component는 codimension $1$이고, $\dim R/(s)=\dim R-1$이다. 

이제 $(s_1,\ldots, s_k)$가 $A$-regular sequence이므로 localization $A_\mathfrak{p}$에서도 regular sequence이며 (localization은 non-zerodivisor를 보존한다), 각 $s_{i+1}$은 $A_\mathfrak{p}/(s_1,\ldots, s_i)$의 non-zerodivisor이다. 위 사실을 $i=0,1,\ldots, k-1$에 차례로 적용하면 

$$0=\dim A_\mathfrak{p}/(s_1,\ldots, s_k)=\dim A_\mathfrak{p}-k$$

를 얻으므로 $\dim A_\mathfrak{p}=k$, 즉 $\codim_X W=k$이다.
:::

::: 예시 11
1. Affine space $\mathbb{A}^n_\mathbb{K}=\Spec\mathbb{K}[\x_1,\ldots, \x_n]$과 상수가 아닌 다항식 $f$를 생각하자. $\mathbb{K}[\x_1,\ldots, \x_n]$이 integral domain이므로 $0\neq f$는 non-zerodivisor이고, 따라서 hypersurface $Z(f)\hookrightarrow\mathbb{A}^n_\mathbb{K}$은 effective Cartier divisor, 즉 codimension $1$의 complete intersection이다. 

2. 좌표부분공간 $Z(\x_1,\ldots, \x_k)\hookrightarrow \mathbb{A}^n_\mathbb{K}$를 생각하자. 각 $i$에 대하여 

	$$\mathbb{K}[\x_1,\ldots, \x_n]/(\x_1,\ldots, \x_i)\cong\mathbb{K}[\x_{i+1},\ldots, \x_n]$$

	은 integral domain이므로 $\x_{i+1}$은 이 ring에서 non-zerodivisor이다. 즉 $(\x_1,\ldots, \x_k)$는 regular sequence이고, $Z(\x_1,\ldots, \x_k)$는 codimension $k$의 complete intersection이다. [명제 10](#prop10)과 부합하게 이 부분공간의 codimension은 정확히 $k$이다. 
:::

거꾸로 codimension이 $k$라고 하여 complete intersection이 되는 것은 아니다. 가령 $\mathbb{A}^4_\mathbb{K}$ 안에서 원점에서만 만나는 두 평면의 합집합 $Z(\x_1,\x_2)\cup Z(\x_3,\x_4)$는 codimension $2$이지만 complete intersection이 아니다. 이를 확인하려면 complete intersection의 local ring이 regular local ring을 regular sequence로 나눈 것이어서 Cohen-Macaulay가 된다는 것과, 이 합집합의 원점에서의 local ring이 그렇지 않다는 것을 보아야 한다. 우리는 이 두 사실을 증명 없이 가져다 쓰고 자세한 것은 [\[가환대수학\] §Cohen-Macaulay 환](/ko/math/commutative_algebra/cohen_macaulay_rings)에 위임한다.

::: 참고 12
[정의 9](#def9)는 regular sequence를 <em-ko>국소적으로만</em-ko> 요구한다. 이보다 강한 조건으로, projective scheme $Z\subseteq \mathbb{P}^n$이 codimension만큼의 homogeneous polynomial들의 vanishing으로 <em-ko>대역적으로</em-ko> 잘리는 경우를 *global complete intersection<sub>대역적 완전교차</sub>*이라 부른다. 이 둘은 일치하지 않는다. 예를 들어 $\mathbb{P}^3$ 안의 twisted cubic은 codimension $2$의 local complete intersection이지만, 두 개의 homogeneous polynomial만으로는 잘리지 않아 global complete intersection은 아니다. 
:::

---

**참고문헌**

**[Vak]** R. Vakil, *The rising sea: Foundation of algebraic geometry*. Available [online](https://math.stanford.edu/~vakil/216blog/). 

