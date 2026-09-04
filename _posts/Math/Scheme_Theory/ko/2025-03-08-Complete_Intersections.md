---
title: "완전교차"
description: "Global section들의 가족이 정의하는 vanishing scheme을 다루고, regular sequence로 잘리는 local complete intersection의 codimension이 자르는 방정식의 개수와 일치함을 보인다. Koszul 복합체가 주는 국소적인 자유 분해로부터 conormal sheaf가 rank k의 locally free sheaf임을 얻고, 사영공간 안에서 대역적으로 잘리는 경우에 Hilbert polynomial을 계산하여 그 degree가 자르는 방정식들의 degree의 곱임을 확인한다."
excerpt: "Local complete intersection의 codimension, Koszul 분해, Hilbert polynomial과 degree"

categories: [Math / Scheme Theory]
permalink: /ko/math/scheme_theory/complete_intersections
sidebar: 
    nav: "scheme_theory-ko"

date: 2025-03-08
weight: 20


---

Closed subscheme의 중요한 예시 중 하나는 [§닫힌 부분스킴, ⁋정의 7](/ko/math/scheme_theory/closed_subschemes#def7)에서 정의한 vanishing scheme이며, 이에 대한 motivation은 당연히 유클리드 공간 $\mathbb{R}^n$과 그 위에서 정의되는 함수 $f: \mathbb{R}^n \rightarrow \mathbb{R}$에 대하여 $f^{-1}(0)$으로 정의되는 $\mathbb{R}^n$의 hypersurface $f=0$이다. 

한편 우리는 더 일반적으로 global section들의 (유한한) family $s_1,\ldots, s_k\in \Gamma(X, \mathcal{O}_X)$가 주어졌을 때 이들이 정의하는 vanishing scheme $Z(s_1,\ldots, s_k)$에도 관심이 있다. 직관적으로 이는 우선 $X$에서 global section $s_1$을 사용하여 만든 vanishing scheme $\iota_1:Z(s_1)\hookrightarrow X$을 생각한 후, $Z(s_1)$의 global section 

$$s_2\vert_{Z(s_1)}=\iota_1^\sharp(X)(s_2)\in\bigl((\iota_1)_\ast \mathcal{O}_{Z(s_1)}\bigr)(X)=\Gamma(Z(s_1), \mathcal{O}_{Z(s_1)})$$

을 통해 $Z(s_1)$에서 $s_2\vert_{Z(s_1)}$의 vanishing scheme을 찾아나가는 것을 반복하여 얻어질 것이며, 물론 이를 위해서는 이 과정이 $s_1, \ldots, s_k$의 순서에 무관하게 같은 scheme을 주어야 할 것이다. 

$k=1$인 경우, 즉 하나의 방정식이 잘라내는 경우는 [§인자와 선형계](/ko/math/scheme_theory/divisors_and_linear_systems)에서 effective Cartier divisor라는 이름으로 이미 다루었다. 이 글에서 우리는 이를 여러 개의 방정식으로 확장하여 local complete intersection을 정의하고, 그 codimension이 자르는 방정식의 개수와 정확히 일치함을 본다. 이어 [\[가환대수학\] §코쥴 복합체](/ko/math/commutative_algebra/koszul_complex)의 결과를 associated sheaf로 옮겨 structure sheaf의 local free resolution을 얻고, 이로부터 conormal sheaf $\mathcal{I}/\mathcal{I}^2$이 rank $k$의 locally free sheaf라는 local complete intersection 고유의 성질을 이끌어낸다. 마지막으로 projective space 안에서 대역적으로 잘리는 경우에는 이 분해가 하나의 대역적인 분해로 붙으므로, [§스킴의 층 코호몰로지](/ko/math/scheme_theory/sheaf_cohomology_of_schemes)의 Euler characteristic을 계산하여 Hilbert polynomial과 degree를 읽어낼 수 있다.

## 여차원과 완전교차

Scheme $X$와 global section들 $s_1,\ldots, s_k\in \Gamma(X, \mathcal{O}_X)$가 주어졌다 하자. 각 affine open set $U=\Spec A$ 위에서 $s_i$는 $A$의 원소 $s_i\vert_U$로 제한되며, 우리는 ideal $(s_1\vert_U,\ldots, s_k\vert_U)$가 정의하는 $U$의 closed subscheme을 생각할 수 있다. 이들은 $U$를 옮겨다닐 때 서로 합치되어 $X$의 closed subscheme을 정의하는데, 이를 $Z(s_1,\ldots, s_k)$로 적고 $s_1,\ldots, s_k$의 *vanishing scheme*이라 부른다. 정의하는 ideal $(s_1,\ldots, s_k)$는 $s_i$들의 순서에 무관하므로 $Z(s_1,\ldots, s_k)$ 또한 순서에 무관하며, 그럼 $Z(s_1)$에서 $s_2$의 vanishing scheme을 찾아나가는 과정은 scheme-theoretic intersection

$$Z(s_1,\ldots, s_k)=Z(s_1)\cap \cdots\cap Z(s_k)$$

으로 정확히 실현된다. 각 affine open 위에서 $(s_1,\ldots, s_k)=\sum_{i=1}^k(s_i)$이기 때문이다.

우리가 이러한 방식으로 잘리는 closed subscheme에 대해 기대하는 것 중 하나는 codimension이다. 즉 만일 주어진 vanishing scheme이 $k$개의 방정식으로 잘린다면 그 codimension이 $k$가 될 것이라 기대하는 것이 자연스럽다. 그러나 이는 일반적으로 성립하지 않는다. 가령 $\mathbb{A}^3_\mathbb{K}=\Spec\mathbb{K}[\x,\y,\z]$에서 $Z(\x\y, \x\z)$는 두 개의 방정식으로 잘리는 closed subscheme이므로 그 codimension이 $2$임을 기대하겠지만, 실제로 이 scheme을 분석해보면 이 scheme은 두 irreducible component $Z(\x)$와 $Z(\y,\z)$를 갖고, 이들 각각의 codimension은 $1$과 $2$이다. 

직관적으로 이는 $\mathbb{K}[\x,\y,\z]$에서 첫 번째 방정식 $\x\y=0$을 이용해 잘라낸 closed subscheme $Z(\x\y)$를 생각하면 이 subscheme은 두 개의 component $Z(\x)$, $Z(\y)$를 갖는데, 이 중 $Z(\x)$ 위에서는 두 번째 방정식 $\x\z$가 이미 항등적으로 소멸하므로 $Z(\x,\x\z)$를 생각해봐야 이미 더 잘라낼 것이 없어 $Z(\x)$이고, 둘째 성분 $Z(\y)$에서만 $Z(\y,\x\z)$가 의미가 생기며, 실제로 이 성분에서의 값을 계산하면

$$Z(\y,\x\z)=Z(\y)\cap (Z(\x)\cup Z(\z))=Z(\x,\y)\cup Z(\y,\z)$$

이며 이들 중 $Z(\x,\y)$는 이미 첫째 성분 $Z(\x)$에 담겨있으므로 유효하게 남는 것은 $Z(\y,\z)$ 뿐이라 위의 묘사를 얻는다. 이에 해당하는 대수적인 설명은 첫째 방정식이 잘라낸 closed subscheme의 coordinate ring $\mathbb{K}[\x,\y,\z]/(\x\y)$ 안에서 $\y\neq 0$이면서 $\x\z\cdot\y=0$이라는 것, 곧 $\x\z$가 zerodivisor라는 것이다. 따라서 이를 해결하기 위해서는 각각의 방정식이 앞선 방정식들을 지난 후에도 여전히 non-zerodivisor일 것을 요구하면 된다. ([\[가환대수학\] §정칙국소환, ⁋정의 2](/ko/math/commutative_algebra/regular_local_rings#def2))

::: 정의 1
Locally Noetherian scheme $X$의 closed embedding $\iota:Z\hookrightarrow X$가 codimension $k$의 *local complete intersection<sub>국소 완전교차</sub>*, 혹은 codimension $k$의 *regular embedding*이라는 것은 $X$의 affine open cover $\{U_i=\Spec A_i\}$가 존재하여, $Z\cap U_i\neq\emptyset$일 때마다 $Z\cap U_i=Z(s_{i,1},\ldots, s_{i,k})$이고 $(s_{i,1},\ldots, s_{i,k})$가 $A_i$-regular sequence인 것이다.
:::

일반적으로 regular sequence의 조건은 원소를 나열하는 순서에 의존했던 것을 기억하자. ([\[가환대수학\] §정칙국소환, ⁋정의 2](/ko/math/commutative_algebra/regular_local_rings#def2)) 그러나 이 의존성은 [정의 1](#def1)에는 남지 않는데, $\mathfrak{p}$가 $(s_{i,1},\ldots, s_{i,k})$를 포함하는 $A_i$의 prime ideal이라면 localization이 exact이므로 $(s_{i,1},\ldots, s_{i,k})$는 $(A_i)_\mathfrak{p}$-regular sequence이고, Noetherian local ring에서는 maximal ideal에 속하는 regular sequence를 임의로 재배열하여도 다시 regular sequence가 되기 때문이다. ([\[가환대수학\] §코쥴 복합체, ⁋따름정리 10](/ko/math/commutative_algebra/koszul_complex#cor10)) 재배열한 sequence가 $A_i$ 전체에서 다시 regular sequence가 되지는 않을 수 있지만, 각 단계에 나타나는 module의 associated prime이 유한개이므로 $\mathfrak{p}$에 담기지 않는 것들을 $(A_i)_f$가 한꺼번에 피하도록 하는 $f\notin \mathfrak{p}$를 택하면 $(A_i)_f$ 위에서는 그러하고, [정의 1](#def1)은 cover를 고를 자유를 주므로 이렇게 세분한 cover가 조건을 만족한다. 

이제 이를 도입하기 전 우리의 직관을 정당화하자. 한쪽 방향은 조건 없이 성립하는데, $k$개의 원소가 생성하는 ideal을 포함하는 minimal prime의 codimension은 언제나 $k$ 이하이기 때문이다. ([\[가환대수학\] §차원, ⁋정리 7](/ko/math/commutative_algebra/Krull_dimension#thm7)) 따라서 실제로 보여야 할 것은 codimension이 $k$보다 작아지지 않는다는 것이다.

::: 명제 2
Codimension $k$의 local complete intersection $\iota:Z\hookrightarrow X$의 모든 irreducible component는 $X$에서 codimension $k$를 갖는다.
:::
::: 증명
$Z$의 irreducible component $W$를 고정하고 [정의 1](#def1)의 cover 가운데 $W$와 만나는 $U=\Spec A$를 택하자. 그럼 적당한 $A$-regular sequence $s_1,\ldots, s_k$가 $Z\cap U=Z(s_1,\ldots, s_k)$를 만족하며, $X$가 locally Noetherian이므로 $A$는 Noetherian ring이다. ([§스킴의 위상구조, ⁋보조정리 13](/ko/math/scheme_theory/topology_of_schemes#lem13)) 한편 [\[위상수학\] §차원, ⁋명제 15](/ko/math/topology/dimension#prop15)의 대응에 의하여 $W\cap U$는 $Z\cap U$의 irreducible component이며, $W$의 generic point는 $W$에서 dense이므로 공집합이 아닌 열린집합 $W\cap U$에 속하고 그 안에서도 dense이다. 즉, 이는 $W\cap U$의 generic point이기도 하며, 이 점에 대응되는 $A$의 prime ideal을 $\mathfrak{p}$라 하면 $\mathfrak{p}$는 $A/(s_1,\ldots, s_k)$의 minimal prime이므로 

$$\dim A_\mathfrak{p}/(s_1,\ldots, s_k)=\dim\bigl(A/(s_1,\ldots, s_k)\bigr)_\mathfrak{p}=0$$

이다. ([\[가환대수학\] §국소화, ⁋명제 8](/ko/math/commutative_algebra/localization#prop8)) 

한편, [§차원, ⁋명제 8](/ko/math/scheme_theory/dimension#prop8)에 의하여 $\codim_X W=\dim A_\mathfrak{p}$이므로 우리가 증명해야 할 것은 $\dim A_\mathfrak{p}$가 $k$가 된다는 사실이다. 위의 식에서 우리는 $\dim A_\mathfrak{p}/(s_1,\ldots, s_k)=0$임을 보았으므로, 이를 위해서는 $s_i$들로 자르는 과정이 정확히 차원을 $1$씩 깎는다는 것을 보이면 충분하다. 우선 $\mathfrak{p}$가 $(s_1,\ldots, s_k)$를 포함하므로 $(s_1,\ldots, s_k)A_\mathfrak{p}$는 proper ideal이고, localization이 exact이라 non-zerodivisor를 보존하므로 $(s_1,\ldots, s_k)$는 $A_\mathfrak{p}$-regular sequence이다. 즉, $R_i=A_\mathfrak{p}/(s_1,\ldots, s_i)$로 두면 각각의 $R_i$는 $0$이 아닌 Noetherian local ring이고, $s_{i+1}$의 image는 $R_i$의 maximal ideal에 속하는 non-zerodivisor이며 $R_i/s_{i+1}R_i=R_{i+1}$이다.

이제 한쪽 방향의 부등식 $\dim R_{i+1}\geq \dim R_i-1$은 [\[가환대수학\] §매개계, ⁋따름정리 7](/ko/math/commutative_algebra/system_of_parameters#cor7)로부터 바로 따라나온다. 반대 방향 부등식이 $s_{i+1}$이 non-zerodivisor임을 사용하는 방향으로, 우선 $s_{i+1}$은 $R_i$의 어떠한 associated prime에도 속하지 않으므로 $s_{i+1}$을 포함하는 $R_i$의 prime ideal은 minimal이 아니다. ([\[가환대수학\] §동반소아이디얼, ⁋정리 7](/ko/math/commutative_algebra/associated_primes#thm7)) 그럼 $R_{i+1}$의 prime ideal들의 임의의 chain에 대하여, 그 각 항의 quotient map $R_i \rightarrow R_{i+1}$에 의한 preimage를 취하면 $s_{i+1}$을 포함하는 $R_i$의 prime ideal들의 같은 길이의 chain을 얻는다. ([\[가환대수학\] §기본 개념들, ⁋명제 11](/ko/math/commutative_algebra/basic_notions#prop11)) 이 chain의 가장 작은 항 $\mathfrak{q}$는 $s_{i+1}$을 포함하므로 minimal이 아니고, 따라서 $\mathfrak{q}'\subsetneq \mathfrak{q}$인 $R_i$의 prime ideal $\mathfrak{q}'$을 chain 아래에 덧붙여 길이가 하나 더 긴 $R_i$의 chain을 얻는다. 곧 $\dim R_{i+1}+1\leq \dim R_i$이다.

이상에서 $\dim R_{i+1}=\dim R_i-1$이고, 이를 $i=0,1,\ldots, k-1$에 차례로 적용하면 

$$0=\dim A_\mathfrak{p}/(s_1,\ldots, s_k)=\dim A_\mathfrak{p}-k$$

를 얻으므로 $\dim A_\mathfrak{p}=k$, 즉 $\codim_X W=k$이다.
:::

이제 간단한 예시들을 살펴보자.

::: 예시 3
1. Affine space $\mathbb{A}^n_\mathbb{K}=\Spec\mathbb{K}[\x_1,\ldots, \x_n]$과 상수가 아닌 다항식 $f$를 생각하자. $\mathbb{K}[\x_1,\ldots, \x_n]$이 integral domain이므로 $0\neq f$는 non-zerodivisor이고, 따라서 hypersurface $Z(f)\hookrightarrow\mathbb{A}^n_\mathbb{K}$은 effective Cartier divisor, 즉 codimension $1$의 local complete intersection이다. 

2. Closed embedding $Z(\x_{n-k+1},\ldots, \x_n)\hookrightarrow \mathbb{A}^n_\mathbb{K}$을 생각하자. 각 $i$에 대하여 

	$$\mathbb{K}[\x_1,\ldots, \x_n]/(\x_{n-k+1},\ldots, \x_{n-k+i})\cong\mathbb{K}[\x_1,\ldots, \x_{n-k},\x_{n-k+i+1},\ldots, \x_n]$$

	은 integral domain이므로 $\x_{n-k+i+1}$은 이 ring에서 non-zerodivisor이다. 즉 $(\x_{n-k+1},\ldots, \x_n)$은 regular sequence이고, $Z(\x_{n-k+1},\ldots, \x_n)$은 codimension $k$의 local complete intersection이다. [명제 2](#prop2)와 부합하게 이 closed subscheme의 codimension은 정확히 $k$이다. 
:::

거꾸로 codimension이 $k$라고 하여 local complete intersection이 되는 것은 아니다. 가령 $\mathbb{A}^4_\mathbb{K}$ 안에서 원점에서만 만나는 두 평면의 합집합 $Z(\x_1,\x_2)\cup Z(\x_3,\x_4)$는 codimension $2$이지만 local complete intersection이 아니다. 두 평면 각각은 두 개의 방정식으로 잘리지만 이들이 만나는 원점 근방에서는 두 개로 부족하기 때문이며, 이는 [명제 5](#prop5) 이후의 논의에서 확인한다.

## 코쥴 복합체와 여법다발

[정의 1](#def1)이 요구하는 것은 국소적으로 하나의 regular sequence가 $Z$를 잘라낸다는 것이고, 이 조건을 다루는 데 쓰이는 것이 Koszul complex이다. Ring $A$의 원소들 $x_1,\ldots, x_n$에 대하여, 그 *Koszul complex* $K(x_1,\ldots, x_n)$은 $j$번째 항이 $A^{\oplus\binom{n}{j}}$인 complex

$$0 \rightarrow A^{\oplus\binom{n}{n}} \rightarrow A^{\oplus\binom{n}{n-1}} \rightarrow \cdots \rightarrow A^{\oplus\binom{n}{1}} \rightarrow A \rightarrow 0$$

이다. 여기에서 $j$번째 항은 $i_1<\cdots<i_j$를 만족하는 index들에 대응되는 원소 $e_{i_1}\wedge\cdots\wedge e_{i_j}$들을 basis로 갖고, differential은 각 basis 원소에서 $e_{i_k}$를 하나씩 지우며 $x_{i_k}$를 곱한 alternating sum

$$\dd{(e_{i_1}\wedge\cdots\wedge e_{i_j})}=\sum_{k=1}^j(-1)^{k-1}x_{i_k}e_{i_1}\wedge\cdots\wedge\widehat{e_{i_k}}\wedge\cdots\wedge e_{i_j}$$

으로 주어진다. 이 complex의 homology는 우리에게 필요한 것을 모두 담고 있으므로, [\[가환대수학\] §코쥴 복합체](/ko/math/commutative_algebra/koszul_complex)의 기본적인 결과들을 소개한다. 

우선 이 complex의 양 끝의 homology는 익숙한 대상으로, $H_0$는 quotient $A/(x_1,\ldots, x_n)$이고 $H_n$은 $x_i$들 모두에 의해 annihilate되는 원소들의 모임이다. 또, Koszul homology는 언제나 $(x_1,\ldots, x_n)$에 의해 annihilate되므로, 자르는 방정식들이 unit ideal을 생성하는 극단적인 경우에는 모든 homology가 소멸한다. 가장 중요한 것은 $x_1,\ldots, x_n$이 regular sequence이면 모든 $i\geq 1$에 대하여 $H_i$가 소멸하고, 그 결과 $K(x_1,\ldots, x_n)$은 $A/(x_1,\ldots, x_n)$의 유한한 free resolution이 된다는 것이다. 직관적으로 가장 단순한 $n=1$의 경우를 보면, 다음의 complex

$$0 \rightarrow A\overset{x_1}{\longrightarrow}A \rightarrow 0$$

에서 

$$H_1=\ker(A\overset{x_1}{\longrightarrow}A)=\{a\in A\mid x_1a=0\}$$

이므로 $H_1$의 소멸이 곧 $x_1$이 non-zerodivisor라는 조건이 되는데, 이를 모든 degree와 임의의 길이의 sequence로 올린 것이 Koszul complex이다. 이를 associated sheaf로 옮기면 local complete intersection의 structure sheaf가 각 chart 위에서 명시적인 finite free resolution을 갖는다는 것이 된다.

::: 명제 4
Locally Noetherian scheme $X$의 codimension $k$ local complete intersection $\iota:Z\hookrightarrow X$와, $Z$와 nontrivial하게 만나는 affine open subset $U=\Spec A$에 대하여, $Z\cap U=Z(s_1,\ldots, s_k)$라 하자. 여기서 $s_1,\ldots, s_k$는 $A$-regular sequence이다. 그럼 $\mathcal{O}_U$-module들의 sequence

$$0 \rightarrow \mathcal{O}_U^{\oplus\binom{k}{k}} \rightarrow \mathcal{O}_U^{\oplus\binom{k}{k-1}} \rightarrow \cdots \rightarrow \mathcal{O}_U^{\oplus\binom{k}{1}} \rightarrow \mathcal{O}_U \rightarrow (\iota_\ast\mathcal{O}_Z)\vert_U \rightarrow 0$$

은 exact이다. 여기에서 $\mathcal{O}_U^{\oplus\binom{k}{j}}$은 Koszul complex $K(s_1,\ldots, s_k)$의 $j$번째 항의 associated sheaf이고, differential 또한 그 complex의 differential을 associated sheaf로 옮긴 것이다.
:::
::: 증명
우리는 앞서 $s_1,\ldots, s_k$가 $A$-regular sequence라면 $K(s_1,\ldots, s_k)$가 $A/(s_1,\ldots, s_k)$의 free resolution이 된다는 것을 살펴보았다. 이제 associated sheaf functor는 exact이므로 ([§준연접층, ⁋명제 6](/ko/math/scheme_theory/quasicoherent_sheaves#prop6)), 이를 associated sheaf로 옮겨도 그 exactness가 보존되며, 이것이 명제의 첫 부분을 준다. 마지막 항에 대해서는 $Z\cap U=Z(s_1,\ldots, s_k)$가 $\Spec A/(s_1,\ldots, s_k)$이고 closed embedding을 따라 그 structure sheaf를 밀어낸 것이 associated sheaf이므로 $(\iota_\ast\mathcal{O}_Z)\vert_U\cong \widetilde{A/(s_1,\ldots, s_k)}$이다.
:::

$Z$의 ideal sheaf $\mathcal{I}=\mathcal{I}_{Z/X}$에 대하여 $\mathcal{I}$는 $\mathcal{I}/\mathcal{I}^2$ 위에 자명하게 작용하므로, 그 $\mathcal{O}_X$-module 구조는 $\mathcal{O}_X/\mathcal{I}\cong\iota_\ast\mathcal{O}_Z$를 거쳐 주어지고 따라서 $\mathcal{I}/\mathcal{I}^2$은 $Z$ 위의 quasi-coherent sheaf로 생각할 수 있다. 이는 기하적으로 $Z$의 conormal sheaf로, 우리는 local complete intersection에 대해서는 이 sheaf가 rank $k$의 locally free sheaf가 되어 conormal *bundle*이 된다는 것을 보인다.

우선 이 sheaf의 각 점에서의 fiber를 보자. 임의의 점 $z\in Z$를 포함하는 affine open subset $\Spec A$를 잡고, 여기서 $\mathcal{I}$에 대응하는 ideal을 $\mathfrak{a}$, $z$에 대응하는 prime을 $\mathfrak{p}$라 하면, $\mathcal{I}$의 stalk은 $\mathfrak{a}_\mathfrak{p}$이고 $\mathcal{O}_{Z,z}=A_\mathfrak{p}/\mathfrak{a}_\mathfrak{p}$의 maximal ideal은 $\mathfrak{p}A_\mathfrak{p}/\mathfrak{a}_\mathfrak{p}$이므로, $z$에서의 fiber는

$$(\mathcal{I}/\mathcal{I}^2)\otimes\kappa(z)=\mathfrak{a}_\mathfrak{p}/(\mathfrak{a}_\mathfrak{p}^2+\mathfrak{p}\mathfrak{a}_\mathfrak{p})=\mathfrak{a}_\mathfrak{p}/\mathfrak{p}\mathfrak{a}_\mathfrak{p}$$

이다. 여기서 마지막 등식은 대수적인 것으로, 만일 $z\in Z$이면 $\mathfrak{a}\subseteq \mathfrak{p}$이고 따라서 $\mathfrak{a}_\mathfrak{p}^2\subseteq \mathfrak{p}\mathfrak{a}_\mathfrak{p}$인 데서 온다. 그럼 [\[가환대수학\] §정수적 확장, ⁋보조정리 8](/ko/math/commutative_algebra/integral_extension#lem8)의 둘째 결과에 의해, $\mathfrak{a}_\mathfrak{p}$의 원소들이 이 ideal을 생성하는 것과 그 image가 $\kappa(z)$-vector space $\mathfrak{a}_\mathfrak{p}/\mathfrak{p}\mathfrak{a}_\mathfrak{p}$를 span하는 것이 동치이므로, fiber의 차원은 $\mathcal{I}_z$를 생성하는 데 필요한 원소의 최소 개수와 같다. 이 보조정리가 요구하는 Jacobson radical 조건은 $J(A_\mathfrak{p})=\mathfrak{p}A_\mathfrak{p}$인 local ring $A_\mathfrak{p}$에서 자동으로 만족된다.

이 개수는 지금 상태에서는 한 점 $z$에서 잰 것이지만, 그 값은 $z$의 근방에서 잰 것으로 생각할 수 있다. $X$가 locally Noetherian이라 $A$가 Noetherian이고 따라서 $\mathfrak{a}$가 finitely generated이므로 $\mathcal{I}$는 finite type이며, 이로부터 [§준연접층](/ko/math/scheme_theory/quasicoherent_sheaves)에서 본 대로 stalk을 생성하는 section들은 그 점의 어떤 근방에서 sheaf 전체를 생성하기 때문이다. 즉, fiber의 차원은 $z$의 근방에서 $Z$를 잘라내는 데 필요한 방정식의 최소 개수이다.

Local complete intersection에서는 이 개수가 정확히 하나로 통제되는 것이 우리의 요지이다. 우선 한쪽 부등식의 경우, [정의 1](#def1)이 요구하는 것은 $Z$가 국소적으로 $k$개의 방정식으로 잘린다는 것이므로 fiber의 차원은 $Z$의 모든 점에서 $k$ 이하이다. 반대쪽 부등식의 경우 이 개수는 codimension 아래로 내려갈 수 없는데, $z$를 지나는 $Z$의 irreducible component $W$를 잡고 그 generic point에 대응하는 $A$의 prime을 $\mathfrak{q}$라 하면 $\mathfrak{q}A_\mathfrak{p}$는 $\mathfrak{a}_\mathfrak{p}$를 포함하는 minimal prime이고 [명제 2](#prop2)와 [§차원, ⁋명제 8](/ko/math/scheme_theory/dimension#prop8)에 의하여 그 codimension이 $\codim_XW=k$이므로, [\[가환대수학\] §차원, ⁋정리 7](/ko/math/commutative_algebra/Krull_dimension#thm7)이 $\mathfrak{a}_\mathfrak{p}$를 생성하는 원소의 개수가 $k$ 이상임을 주기 때문이다. 곧 local complete intersection의 conormal sheaf는 모든 점에서 정확히 $k$차원의 fiber를 갖는다. 단 fiber의 차원이 일정하다는 것만으로 sheaf가 locally free가 되지는 않는데, 가령 $A=\mathbb{K}[\x]/(\x^2)$ 위의 module $A/(\x)$는 $\Spec A$의 유일한 점에서 $1$차원의 fiber를 갖지만 free $A$-module이 아니다. 이를 해소하는 것이 regular sequence 조건으로, [명제 4](#prop4)가 사용한 $H_1(K(s_1,\ldots, s_k))$의 소멸은 $\sum_ia_is_i=0$인 관계가 모두 trivial한 관계 $s_ie_j-s_je_i$들의 조합이라는 뜻이고 그러한 관계에 나타나는 $a_i$는 모두 $\mathfrak{a}$에 속하므로, $\mathfrak{a}/\mathfrak{a}^2$ 위에서는 $s_i$들 사이의 관계가 남지 않아 freeness가 보장된다.

이 관찰을 각 chart 위에서 정확히 적으면 다음을 얻는다.

::: 명제 5
Locally Noetherian scheme $X$의 codimension $k$ local complete intersection $\iota:Z\hookrightarrow X$와 그 ideal sheaf $\mathcal{I}=\mathcal{I}_{Z/X}$에 대하여, $\mathcal{I}/\mathcal{I}^2$은 $Z$ 위의 rank $k$의 locally free sheaf이다.
:::
::: 증명
국소적인 주장이므로 $X=\Spec A$, $\mathfrak{a}=\mathcal{I}(X)=(s_1,\ldots, s_k)$이고 $s_1,\ldots, s_k$가 $A$-regular sequence인 경우만 보면 충분하다. 이 경우 $\mathcal{I}=\widetilde{\mathfrak{a}}$이고 $\mathcal{I}^2=\widetilde{\mathfrak{a}^2}$이므로 우리는 결국 $\mathfrak{a}/\mathfrak{a}^2$이 rank $k$의 free $A/\mathfrak{a}$-module임을 보이면 된다.

$A/\mathfrak{a}$-linear map $\psi:(A/\mathfrak{a})^{\oplus k} \rightarrow \mathfrak{a}/\mathfrak{a}^2$을 $e_i\mapsto s_i+\mathfrak{a}^2$으로 정의하자. $\mathfrak{a}$가 $s_i$들로 생성되므로 $\psi$는 surjective이다. Injectivity를 보이기 위해 $a_1,\ldots, a_k\in A$가 $\sum_ia_is_i\in \mathfrak{a}^2$을 만족한다 하자. $\mathfrak{a}^2$은 곱 $s_is_j$들로 생성되므로 적당한 $b_{ij}\in A$에 대하여 $\sum_ia_is_i=\sum_{i,j}b_{ij}s_is_j$이고, $c_i=a_i-\sum_jb_{ij}s_j$로 두면 $\sum_ic_is_i=0$이다. 그럼 위에서 본 대로 $H_1(K(s_1,\ldots, s_k))$의 소멸이 모든 $i$에 대하여 $c_i\in \mathfrak{a}$를 주므로 $a_i=c_i+\sum_jb_{ij}s_j\in \mathfrak{a}$이고, 곧 $(A/\mathfrak{a})^{\oplus k}$ 안에서 $\sum_ia_ie_i=0$이라 $\psi$는 injective이다.
:::

곧 $Z$를 국소적으로 잘라내는 $k$개의 방정식은 conormal sheaf의 기저를 이루며, $Z$의 법선 방향은 자르는 방정식의 개수만큼의 자유도를 정확히 갖는다.

[예시 3](#ex3) 직후에 미뤄둔 주장 또한 이제 확인할 수 있다. $A=\mathbb{K}[\x_1,\ldots, \x_4]$에 대하여 $\mathbb{A}^4_\mathbb{K}=\Spec A$ 안에서 원점에서만 만나는 두 평면의 합집합 $Z=Z(\x_1,\x_2)\cup Z(\x_3,\x_4)$를 생각하자. 만일 $Z$가 codimension $k$의 local complete intersection이라면 [명제 2](#prop2)에 의하여 두 irreducible component가 모두 codimension $k$를 가져야 하므로 $k=2$이고, [명제 5](#prop5)에 의하여 conormal sheaf의 fiber는 $Z$의 모든 점에서 $2$차원이어야 한다. 따라서 이 차원이 뛰는 점을 하나 찾으면 이것이 local complete intersection이 아니라는 것을 보일 수 있다. 우선 $Z$를 정의하는 ideal은

$$\mathfrak{a}=(\x_1,\x_2)\cap(\x_3,\x_4)=(\x_1\x_3, \x_1\x_4, \x_2\x_3, \x_2\x_4)$$

이다. 원점이 아닌 $Z$의 점은 모두 네 chart $D(\x_i)$ 가운데 하나에 놓이는데, 가령 $A_{\x_1}$ 안에서는 $\x_3=\x_1^{-1}(\x_1\x_3)$과 $\x_4=\x_1^{-1}(\x_1\x_4)$가 모두 $\mathfrak{a}A_{\x_1}$에 속하고 남은 두 generator $\x_2\x_3, \x_2\x_4$는 이 둘이 생성하는 ideal에 담기므로 $\mathfrak{a}A_{\x_1}=(\x_3,\x_4)A_{\x_1}$이다. 여기에서 $A_{\x_1}$과 $A_{\x_1}/(\x_3)$이 모두 integral domain이라 $\x_3,\x_4$는 regular sequence이고, 나머지 세 좌표에 대해서도 같은 계산이 성립하므로, 원점을 제외하면 $Z$는 codimension $2$의 local complete intersection이며 [명제 5](#prop5)에 의하여 그 위에서 fiber의 차원은 $2$이다.

문제가 되는 곳은 원점이다. 이에 대응하는 maximal ideal을 $\mathfrak{m}=(\x_1,\x_2,\x_3,\x_4)$라 하면 $\mathfrak{m}\mathfrak{a}$의 homogeneous 원소는 모두 degree $3$ 이상인 데 반해 $\mathfrak{a}$의 네 generator는 모두 degree $2$이므로, 이들의 $\mathbb{K}$-linear combination 가운데 $\mathfrak{m}\mathfrak{a}$에 속하는 것은 $0$뿐이고 따라서 $\mathfrak{a}/\mathfrak{m}\mathfrak{a}$는 $4$차원이다. 이 vector space는 이미 $\mathfrak{m}$에 의해 소멸되고 $A\setminus \mathfrak{m}$의 원소는 그 위에서 $\mathbb{K}^\times$의 원소로 작용하므로 $\mathfrak{m}$에서 localize하여도 바뀌지 않으며, 곧 원점에서의 fiber $\mathfrak{a}_\mathfrak{m}/\mathfrak{m}\mathfrak{a}_\mathfrak{m}$ 또한 $4$차원이다. 따라서 $Z$는 local complete intersection이 아니며, 이는 동시에 $\mathcal{I}/\mathcal{I}^2$이 locally free가 아닌 예이기도 하다.

## Hilbert polynomial과 degree

[정의 1](#def1)이 요구하는 것은 local한 조건이지만, projective space 안에서 하나의 regular sequence를 이루는 homogeneous polynomial들이 global하게 잘라내는 경우에는 [명제 4](#prop4)의 local한 $\mathcal{O}_X$-module들의 resolution이 하나의 global한 resolution으로 붙게 된다. 이 절에서는 ambient가 언제나 projective space이므로 표기를 바꾸어, 앞 절까지 ambient를 가리키던 $X$를 여기에서는 $\mathbb{P}^n$의 closed subscheme을 가리키는 데 쓴다.

::: 명제 6
Field $\mathbb{K}$ 위의 projective space $\mathbb{P}^n=\Proj S_\bullet$ ($S_\bullet=\mathbb{K}[\x_0,\ldots, \x_n]$)와 각각 degree $d_i>0$인 homogeneous polynomial들 $f_1,\ldots, f_k$가 주어지고, 이들이 $S_\bullet$-regular sequence를 이룬다 하자. $X=V_+(f_1,\ldots, f_k)$이고 $\iota:X\hookrightarrow \mathbb{P}^n$이 그 closed embedding일 때 ([§사영공간의 닫힌 부분스킴, ⁋명제 1](/ko/math/scheme_theory/closed_subschemes_of_projective_spaces#prop1)) 다음이 성립한다.

1. $\iota$는 codimension $k$의 local complete intersection이며, [정의 1](#def1)의 affine open cover로 표준 chart들 $\{D_+(\x_m)\}_{m=0}^n$을 택할 수 있다.
2. $J\subseteq \{1,\ldots, k\}$에 대하여 $d_J=\sum_{i\in J}d_i$로 적으면, $\mathcal{O}_{\mathbb{P}^n}$-module들의 sequence

	$$0 \rightarrow \bigoplus_{\lvert J\rvert=k}\mathcal{O}(-d_J) \rightarrow \cdots \rightarrow \bigoplus_{\lvert J\rvert=1}\mathcal{O}(-d_J) \rightarrow \mathcal{O}_{\mathbb{P}^n} \rightarrow \iota_\ast\mathcal{O}_X \rightarrow 0$$

	은 exact이다. 여기에서 $\lvert J\rvert=j$인 summand에서 $\lvert J'\rvert=j-1$인 summand로 가는 성분은 $J'=J\setminus\{i\}$일 때 Koszul differential의 부호를 곱한 $f_i$ 배이고 그 밖에는 $0$이다.
:::
::: 증명
Chart $D_+(\x_m)=\Spec S_{(\x_m)}$을 고정하고 $g_i=f_i/\x_m^{d_i}\in S_{(\x_m)}$이라 하면 $X\cap D_+(\x_m)=Z(g_1,\ldots, g_k)$임을 안다. 

먼저 $S_{\x_m}$을 degree로 분해하면 

$$S_{\x_m}=\bigoplus_{j\in\mathbb{Z}}\x_m^jS_{(\x_m)}$$

이며 각각의 $\x_m^jS_{(\x_m)}$은 $S_{(\x_m)}$과 isomorphic한 $S_{(\x_m)}$-module이다. $g_i$들이 degree $0$이므로 이들이 생성하는 ideal 또한 이 분해와 호환되어 임의의 $i$에 대하여 

$$S_{\x_m}/(g_1,\ldots, g_i)=\bigoplus_j\x_m^j\bigl(S_{(\x_m)}/(g_1,\ldots, g_i)\bigr)$$

이고, 이 때 $g_{i+1}$은 degree $0$이므로 $g_{i+1}$를 곱하는 것은 각각의 성분을 보존한다. 따라서 $g_{i+1}$을 곱하는 것이 $S_{\x_m}/(g_1,\ldots, g_i)$ 위에서 injective인지 확인하기 위해서는 이것이 $S_{(\x_m)}/(g_1,\ldots, g_i)$ 위에서 injective인지 확인하면 충분하며, 또 위의 direct sum이 소멸하는 것은 그 각각의 성분이 소멸하는 것과 동치이므로, $(g_1,\ldots, g_i)S_{\x_m}$이 proper ideal인 것은 $(g_1,\ldots, g_i)S_{(\x_m)}$이 proper ideal인 것과 동치이다.

이제 $X\cap D_+(\x_m)\neq\emptyset$이라 하고, $g_1,\ldots, g_k$가 $S_{(\x_m)}$-regular sequence임을 보이자. ([\[가환대수학\] §정칙국소환, ⁋정의 2](/ko/math/commutative_algebra/regular_local_rings#def2)) 그럼 $Z(g_1,\ldots, g_k)\neq \emptyset$이므로 $(g_1,\ldots, g_k)$는 $S_{(\x_m)}$의 proper ideal이고, 위의 degree 분해에 의하여 $(g_1,\ldots, g_k)S_{\x_m}$ 또한 proper이다. 한편 $\x_m$은 $S_{\x_m}$에서 unit이므로 각각의 $i$에 대하여 $(f_1,\ldots, f_i)S_{\x_m}=(g_1,\ldots, g_i)S_{\x_m}$이고 $f_{i+1}$과 $g_{i+1}$은 unit만큼만 차이난다. 특히 $(f_1,\ldots, f_k)S_{\x_m}$이 proper ideal이며, localization이 exact이므로 가정에 의해 $f_1,\ldots, f_k$는 $S_{\x_m}$-regular sequence이기도 하고, 따라서 $g_1,\ldots, g_k$ 또한 그러하다. 그럼 위의 degree 분해에서 살펴본 것과 같이 $g_1,\ldots, g_k$는 $S_{(\x_m)}$-regular sequence이다. 이제 standard affine chart들 $\{D_+(\x_m)\}_{m=0}^n$은 $\mathbb{P}^n$의 affine open cover이고, 각각에 대하여 $X\cap D_+(\x_m)$은 공집합이거나 방금 얻은 regular sequence가 잘라내는 것이므로, 이로부터 첫째 결과를 얻는다.

둘째 결과의 경우, $\lvert J\rvert=j$인 $J$에 대응하는 summand $\mathcal{O}(-d_J)$를 chart $D_+(\x_m)$ 위에서 generating section $\x_m^{-d_J}$로 trivialize하면, $f_i$를 곱하는 것으로 주어지는 $\mathcal{O}(-d_J) \rightarrow \mathcal{O}(-d_{J\setminus\{i\}})$은 $\x_m^{-d_J}a\mapsto \x_m^{-d_{J\setminus\{i\}}}g_ia$가 되어 이 위에서는 $g_i$를 곱하는 것과 같다. 즉, 위의 sequence를 $D_+(\x_m)$으로 제한한 것은 $K(g_1,\ldots, g_k)$의 associated sheaf에 $\widetilde{S_{(\x_m)}/(g_1,\ldots, g_k)}$를 이어붙인 것이며, $X$와 만나는 chart 위에서 이것이 exact이라는 것은, 방금 얻은 regular sequence 성질과 함께 ambient를 $D_+(\x_m)$으로 하고 그 closed subscheme을 $X\cap D_+(\x_m)$으로 하여 [명제 4](#prop4)를 적용하면 된다. $X$와 만나지 않는 chart 위에서는 $(g_1,\ldots, g_k)=S_{(\x_m)}$이 unit ideal이므로 모든 Koszul homology가 소멸하고, 특히 $H_0=S_{(\x_m)}/(g_1,\ldots, g_k)=0$이라 마지막 항도 $0$이 되어 역시 exact이다. Exactness는 stalk에서 확인되고 이러한 chart들이 $\mathbb{P}^n$을 덮으므로 위의 sequence는 exact이다.
:::

그럼 이러한 경우, Koszul complex의 각 항이 projective space 위의 line bundle들의 finite direct sum이다. Finite exact sequence 위에서 Euler characteristic의 alternating sum은 소멸하며, projective space 위의 twisting sheaf의 Euler characteristic은 이미 명시적으로 계산되어 있으므로, 이 분해 하나로부터 $X$의 Hilbert polynomial이 자르는 방정식들의 degree만으로 결정되고 그로부터 dimension과 degree가 따라 나온다. ([§스킴의 층 코호몰로지, ⁋정리 16](/ko/math/scheme_theory/sheaf_cohomology_of_schemes#thm16))

::: 따름정리 7
[명제 6](#prop6)의 상황에서 $X\neq \emptyset$이라 하자. 그럼 $k\leq n$이고, $X$의 Hilbert polynomial은

$$P_{\mathcal{O}_X}(t)=\sum_{J\subseteq\{1,\ldots, k\}}(-1)^{\lvert J\rvert}\binom{n+t-d_J}{n}$$

이다. 더욱이 $\dim X=n-k$이며 $\deg X=d_1\cdots d_k$이다.
:::
::: 증명
[명제 6](#prop6)의 exact sequence에 invertible sheaf $\mathcal{O}(t)$를 tensor하여도 exactness가 유지되고, closed embedding에 대하여 $(\iota_\ast\mathcal{O}_X)\otimes\mathcal{O}(t)\cong \iota_\ast(\mathcal{O}_X(t))$이며 cohomology가 $\iota_\ast$ 아래에서 보존된다. ([§스킴의 층 코호몰로지, ⁋정리 8](/ko/math/scheme_theory/sheaf_cohomology_of_schemes#thm8) 직전의 관찰) 따라서 $\rchi(X,\mathcal{O}_X(t))=\rchi(\mathbb{P}^n,\iota_\ast\mathcal{O}_X(t))$이고, [§스킴의 층 코호몰로지, ⁋명제 14](/ko/math/scheme_theory/sheaf_cohomology_of_schemes#prop14)의 2번을 이 finite exact sequence에 적용한 뒤 [§스킴의 층 코호몰로지, ⁋따름정리 15](/ko/math/scheme_theory/sheaf_cohomology_of_schemes#cor15)로 각 항을 계산하면

$$\rchi(X,\mathcal{O}_X(t))=\sum_{j=0}^k(-1)^j\sum_{\lvert J\rvert=j}\rchi\bigl(\mathbb{P}^n,\mathcal{O}(t-d_J)\bigr)=\sum_J(-1)^{\lvert J\rvert}\binom{n+t-d_J}{n}$$

을 얻는다. [§스킴의 층 코호몰로지, ⁋정리 16](/ko/math/scheme_theory/sheaf_cohomology_of_schemes#thm16)에 의하여 좌변은 $P_{\mathcal{O}_X}(t)$이다.

남은 것은 이 다항식의 degree와 최고차항 계수를 읽는 것 뿐이다. 우선 degree $m\geq 1$이고 최고차항 계수가 $c\neq 0$인 다항식 $p$와 $d>0$에 대하여, $p(t)-p(t-d)$는 degree $m-1$이고 그 최고차항 계수는 $cmd$임을 계산할 수 있다. 또 $p$가 상수이면 $p(t)-p(t-d)=0$이다.

이제 $p_0(t)=\binom{n+t}{n}$으로 두고 $p_i(t)=p_{i-1}(t)-p_{i-1}(t-d_i)$로 정의하면, $i$에 대한 귀납법으로

$$p_i(t)=\sum_{J\subseteq\{1,\ldots, i\}}(-1)^{\lvert J\rvert}\binom{n+t-d_J}{n}$$

임을 보일 수 있고, 이로부터 $p_k$가 위에서 얻은 다항식임을 알 수 있다. 여기에서 $p_0$은 degree $n$이고 최고차항 계수가 $1/n!$이다. 만일 $k>n$이라면 위의 관찰에 의하여 $p_n$은 상수이고 $p_{n+1}=0$이므로 $p_k=0$가 되어 이 다항식의 degree는 $-\infty$인데, $X\neq\emptyset$이라 $\mathcal{O}_X\neq 0$이므로 [§스킴의 층 코호몰로지, ⁋정리 16](/ko/math/scheme_theory/sheaf_cohomology_of_schemes#thm16)에 의하여 $P_{\mathcal{O}_X}$의 degree는 $\dim X\geq 0$이 되어 모순이다. 따라서 $k\leq n$이어야 한다.

그럼 $i=1,\ldots, k$의 각 단계에서 $p_{i-1}$의 degree $n-i+1$이 $1$ 이상이므로 위의 관찰을 그대로 적용할 수 있고, $p_i$는 degree $n-i$이며 그 최고차항 계수는

$$\frac{1}{n!}\cdot nd_1\cdot (n-1)d_2\cdots (n-i+1)d_i=\frac{d_1\cdots d_i}{(n-i)!}$$

이다. $r=n-k$로 두면 $P_{\mathcal{O}_X}$는 degree $r$이고 최고차항 계수는 $d_1\cdots d_k/r!$이므로, 다시 [§스킴의 층 코호몰로지, ⁋정리 16](/ko/math/scheme_theory/sheaf_cohomology_of_schemes#thm16)에 의하여 $\dim X=r=n-k$이고 [§스킴의 층 코호몰로지, ⁋정의 17](/ko/math/scheme_theory/sheaf_cohomology_of_schemes#def17)에 의하여 $\deg X=r!\cdot d_1\cdots d_k/r!=d_1\cdots d_k$이다.
:::

$k=1$인 경우 [따름정리 7](#cor7)은 degree $e$의 hypersurface가 $\deg X=e$를 갖는다는 것으로, 이는 [§스킴의 층 코호몰로지, ⁋정의 17](/ko/math/scheme_theory/sheaf_cohomology_of_schemes#def17) 이후에 직접 계산한 것과 같다. 일반적인 $k$에 대해서는 이것이 Bézout 정리의 가장 단순한 형태로, 서로 regular sequence를 이루는 방정식들이 잘라내는 대상의 degree가 방정식들의 degree의 곱이라는 것이다. 

::: 예시 8
1. $\mathbb{P}^3_\mathbb{K}=\Proj S_\bullet$ 안에서 $S_\bullet$-regular sequence를 이루는 두 quadric $f_1,f_2$가 잘라내는 $X=V_+(f_1,f_2)$를 생각하자. 이제 $n=3$, $k=2$, $d_1=d_2=2$이므로 [따름정리 7](#cor7)에 의하여

	$$P_{\mathcal{O}_X}(t)=\binom{3+t}{3}-2\binom{1+t}{3}+\binom{t-1}{3}=\frac{(t+3)(t+2)(t+1)-2(t+1)t(t-1)+(t-1)(t-2)(t-3)}{6}=4t$$

	이다. 곧 $\dim X=1$이고 $\deg X=1!\cdot 4=4$이며, arithmetic genus는 $p_a(X)=(-1)^1\bigl(P_{\mathcal{O}_X}(0)-1\bigr)=1$이다. ([§스킴의 층 코호몰로지, ⁋정의 17](/ko/math/scheme_theory/sheaf_cohomology_of_schemes#def17)) 

2. $\mathbb{P}^3_\mathbb{K}=\Proj \mathbb{K}[\x_0,\x_1,\x_2,\x_3]$의 twisted cubic $C$를 보자. 이는 $\mathbb{P}^1=\Proj \mathbb{K}[\y_0,\y_1]$ 위의 invertible sheaf $\mathcal{O}_{\mathbb{P}^1}(3)$과 그 globally generating section $\y_0^3, \y_0^2\y_1, \y_0\y_1^2, \y_1^3$이 정의하는 morphism $\varphi:\mathbb{P}^1 \rightarrow \mathbb{P}^3_\mathbb{K}$으로 주어진 것이다. Standard affine chart $D_+(\x_j)$ 위에서 $\varphi$에 대응하는 ring homomorphism은 $\x_i/\x_j\mapsto \y_0^{3-i}\y_1^i/\y_0^{3-j}\y_1^j$이며, 우리는 $\varphi$가 closed embedding이라는 것을 보이기 위해 우선 이 ring homomorphism이 surjective임을 보인다. 표기의 편의를 위해 $\t=\y_1/\y_0$으로 적자.
  
	우선 $\varphi^{-1}(D_+(\x_0))=D_+(\y_0)=\Spec\mathbb{K}[\t]$이고 $D_+(\x_0)$의 좌표 $\s_1=\x_1/\x_0$, $\s_2=\x_2/\x_0$, $\s_3=\x_3/\x_0$은 각각 $\t$, $\t^2$, $\t^3$으로 가므로, 대응하는 ring homomorphism은 surjective이고 이렇게 주어지는 $\s_1\mapsto \t$이 정의하는 isomorphism
	
	$$\mathbb{K}[\s_1,\s_2,\s_3]/(\s_2-\s_1^2, \s_3-\s_1^3)\cong\mathbb{K}[\s_1]\cong \mathbb{K}[\t]$$
	
	으로부터 그 kernel이 정확히 $(\s_2-\s_1^2, \s_3-\s_1^3)$이다. 마찬가지로 
	
	$$\varphi^{-1}(D_+(\x_1))=D_+(\y_0\y_1)=\Spec\mathbb{K}[\t,\t^{-1}]$$
	
	위에서는 $D_+(\x_1)$의 좌표 $\s_1'=\x_0/\x_1$, $\s_2'=\x_2/\x_1$, $\s_3'=\x_3/\x_1$가 각각 $\t^{-1}$, $\t$, $\t^2$으로 가 surjective이며, $\s_2'\mapsto \t$이 정의하는 isomorphism
	
	$$\mathbb{K}[\s_1',\s_2',\s_3']/(\s_3'-{\s_2'}^2, \s_1'\s_2'-1)\cong\mathbb{K}[\s_2',{\s_2'}^{-1}]\cong \mathbb{K}[\t,\t^{-1}]$$
	
	으로부터 이 ring homomorphism의 kernel이 $(\s_3'-{\s_2'}^2, \s_1'\s_2'-1)$임을 안다. 남은 두 chart에 대해서는 $\x_i'=\x_{3-i}$와 $\y_0'=\y_1$, $\y_1'=\y_0$, $\t'=\t^{-1}$로 이름을 바꾸어 적으면 $\varphi$가 $\x_i'\mapsto {\y_0'}^{3-i}{\y_1'}^i$라는 같은 꼴로 주어지고 $D_+(\x_0')=D_+(\x_3)$, $D_+(\x_1')=D_+(\x_2)$이므로, 위의 두 계산이 그대로 옮겨진다. 이제 standard affine chart들은 $\mathbb{P}^3_\mathbb{K}$의 affine open cover를 이루고 [§닫힌 부분스킴, ⁋명제 3](/ko/math/scheme_theory/closed_subschemes#prop3)의 증명은 이 조건을 하나의 affine open cover 위에서 확인하면 충분함을 보였으므로, $\varphi$는 closed embedding이고 따라서 $C\cong\mathbb{P}^1$이며 $\mathcal{O}_C(1)=\varphi^\ast\mathcal{O}(1)\cong \mathcal{O}_{\mathbb{P}^1}(3)$이다.

	뿐만 아니라, 위의 계산에서 두 경우 모두 ambient가 integral domain이고 첫 generator로 나눈 quotient $\mathbb{K}[\s_1,\s_3]$와 $\mathbb{K}[\s_1',\s_2']$ 또한 integral domain이므로, 각 kernel의 두 generator는 regular sequence를 이룬다. 즉, $C$는 codimension $2$의 local complete intersection이며, 이로부터 

	$$P_{\mathcal{O}_C}(t)=\rchi\bigl(\mathbb{P}^1,\mathcal{O}_{\mathbb{P}^1}(3t)\bigr)=\binom{1+3t}{1}=3t+1$$

	이므로 $\dim C=1$이고 $\deg C=1!\cdot 3=3$이다. 
	
	우리 주장은 $C$가 $S_\bullet$-regular sequence를 이루는 두 homogeneous polynomial $f_1,f_2$에 대하여 $C=V_+(f_1,f_2)$의 꼴이 아니라는 것이다. 만일 $C$가 이러한 꼴이라면, [따름정리 7](#cor7)에 의하여 $d_1d_2=3$이다. 그럼 둘 가운데 하나는 degree $1$이고, 이는 $C$가 hyperplane $V_+(H)$에 담긴다는 뜻이다. 그런데 $H=\sum_ia_i\x_i$를 $C\cong\mathbb{P}^1$로 당기면 $\sum_ia_i\y_0^{3-i}\y_1^i$이고, 이 때 $\y_0^3,\y_0^2\y_1,\y_0\y_1^2,\y_1^3$은 $\Gamma(\mathbb{P}^1,\mathcal{O}_{\mathbb{P}^1}(3))$에서 일차독립이므로 모든 $a_i$가 $0$이어야 한다. 따라서 그러한 $H$는 존재할 수 없다. 한편 $C=V_+(f_1,f_2)$이기만 하면 위의 regular sequence 가정은 저절로 따라오는데, $\dim C=1$이라 $f_1,f_2$는 모두 positive degree를 갖고, 공통인수가 상수가 아니라면 그것이 정의하는 hypersurface가 $C$에 담겨 차원이 맞지 않으므로 둘은 서로소이며, $S_\bullet$이 UFD라 $f_1\mid f_2g$에서 $f_1\mid g$가 따라나와 $f_2$가 $S_\bullet/(f_1)$의 non-zerodivisor이기 때문이다. 즉, $C$는 codimension $2$의 local complete intersection임에도 global하게는 두 homogeneous polynomial의 vanishing으로 잘리지는 않는 예시이다.
:::

---

**참고문헌**

**[Vak]** R. Vakil, *The rising sea: Foundation of algebraic geometry*. Available [online](https://math.stanford.edu/~vakil/216blog/). 

