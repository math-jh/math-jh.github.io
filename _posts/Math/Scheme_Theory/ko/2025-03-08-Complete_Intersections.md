---
title: "완전교차"
description: "Global section들의 가족이 정의하는 vanishing scheme을 다루고, regular sequence로 잘리는 complete intersection의 codimension이 자르는 방정식의 개수와 일치함을 보인다. Koszul 복합체가 주는 국소적인 자유 분해로부터 conormal sheaf가 rank k의 locally free sheaf임을 얻고, 사영공간 안에서 대역적으로 잘리는 경우에 Hilbert polynomial을 계산하여 그 degree가 자르는 방정식들의 degree의 곱임을 확인한다."
excerpt: "Complete intersection의 codimension, Koszul 분해, Hilbert polynomial과 degree"

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

$k=1$인 경우, 곧 하나의 방정식이 잘라내는 경우는 [§인자와 선형계](/ko/math/scheme_theory/divisors_and_linear_systems)에서 effective Cartier divisor의 이름으로 이미 다루었다. 이 글에서 우리는 이를 여러 개의 방정식으로 확장하여 complete intersection을 정의하고, 그 codimension이 자르는 방정식의 개수와 정확히 일치함을 본다. 이어 [\[가환대수학\] §코쥴 복합체](/ko/math/commutative_algebra/koszul_complex)의 결과를 associated sheaf로 옮겨 structure sheaf의 국소적인 자유 분해를 얻고, 이로부터 conormal sheaf $\mathcal{I}/\mathcal{I}^2$이 rank $k$의 locally free sheaf라는 완전교차 고유의 성질을 이끌어낸다. 마지막으로 projective space 안에서 대역적으로 잘리는 경우에는 이 분해가 하나의 대역적인 분해로 붙으므로, [§스킴의 층 코호몰로지](/ko/math/scheme_theory/sheaf_cohomology_of_schemes)의 Euler characteristic을 계산하여 Hilbert polynomial과 degree를 읽어낼 수 있다.

## 여차원과 완전교차

이제 도입부에서 예고한, 여러 global section들의 family가 정의하는 vanishing scheme을 구성한다. Scheme $X$와 global section들 $s_1,\ldots, s_k\in \Gamma(X, \mathcal{O}_X)$가 주어졌다 하자. 각 affine open set $U=\Spec A$ 위에서 $s_i$는 $A$의 원소 $s_i\vert_U$로 제한되며, 우리는 ideal $(s_1\vert_U,\ldots, s_k\vert_U)$가 정의하는 $U$의 closed subscheme을 생각할 수 있다. 이들은 $U$를 옮겨다닐 때 서로 합치되어 $X$의 closed subscheme을 정의하는데, 이를 $Z(s_1,\ldots, s_k)$로 적고 $s_1,\ldots, s_k$의 *vanishing scheme*이라 부른다. 정의하는 ideal $(s_1,\ldots, s_k)$는 $s_i$들의 순서에 무관하므로 $Z(s_1,\ldots, s_k)$ 또한 순서에 무관하며, 도입부에서 말한 "$Z(s_1)$에서 $s_2$의 vanishing scheme을 찾아나가는" 과정은 scheme-theoretic 교집합

$$Z(s_1,\ldots, s_k)=Z(s_1)\cap \cdots\cap Z(s_k)$$

으로 정확히 실현된다. 각 affine open 위에서 $(s_1,\ldots, s_k)=\sum_{i=1}^k(s_i)$이기 때문이다.

이제 이를 여러 번 잘라낸 일반적인 경우를 정의한다. 핵심은 자르는 section들이 단순한 non-zerodivisor를 넘어 *regular sequence*를 이루어야 한다는 것이다.

::: 정의 1
Locally Noetherian scheme $X$의 closed embedding $\iota:Z\hookrightarrow X$가 codimension $k$의 *complete intersection<sub>완전교차</sub>*, 혹은 codimension $k$의 *regular embedding*이라는 것은 $X$의 affine open cover $\{U_i=\Spec A_i\}$가 존재하여, 각각의 $U_i$에 대해 $Z\cap U_i=\emptyset$이거나, $Z\cap U_i=Z(s_{i,1},\ldots, s_{i,k})$이고 $(s_{i,1},\ldots, s_{i,k})$가 [\[가환대수학\] §정칙국소환, ⁋정의 2](/ko/math/commutative_algebra/regular_local_rings#def2)의 의미에서 $A_i$-regular sequence인 것이다.
:::

[정의 1](#def1)이 $Z$와 만나지 않는 chart를 따로 허용하는 것은 그러한 chart 위에서는 regular sequence를 요구할 수 없기 때문이다. Regular sequence는 자신이 생성하는 ideal이 proper일 것을 요구하는데 $Z\cap U_i=\emptyset$이면 그 ideal은 $A_i$ 전체이고, 반면 $Z$가 닫힌집합인 이상 $Z$와 만나지 않는 열린집합은 얼마든지 cover에 섞여 들어올 수 있다. 또 엄밀히는 [정의 1](#def1)의 성질이 국소적으로만 regular sequence를 요구하므로 *local complete intersection<sub>국소 완전교차</sub>*이라 부르는 것이 정확하다. 한편 locally Noetherian scheme 위에서 $k=1$의 complete intersection은 정확히 [§인자와 선형계, ⁋정의 1](/ko/math/scheme_theory/divisors_and_linear_systems#def1)의 effective Cartier divisor이다. 길이 $1$의 regular sequence란 그저 $(s)$가 proper이도록 하는 non-zerodivisor $s$이고, $Z\cap U_i=\emptyset$인 chart 위에서는 $Z\cap U_i=Z(1)$이므로 non-zerodivisor $s_i=1$이 그 정의의 조건을 충족시키기 때문이다.

Regular sequence라는 조건 자체는 원소를 나열하는 순서에 의존하며, 순서를 바꾸면 실제로 깨지는 예가 있다. ([\[가환대수학\] §코쥴 복합체, ⁋예시 11](/ko/math/commutative_algebra/koszul_complex#ex11)) 그러나 이 의존성은 [정의 1](#def1)에는 남지 않는다. $\mathfrak{p}$가 $(s_{i,1},\ldots, s_{i,k})$를 포함하는 $A_i$의 prime ideal이라면 localization이 exact이므로 $(s_{i,1},\ldots, s_{i,k})$는 $(A_i)_\mathfrak{p}$-regular sequence이고, Noetherian local ring에서는 maximal ideal에 속하는 regular sequence를 임의로 재배열하여도 다시 regular sequence가 되므로 ([\[가환대수학\] §코쥴 복합체, ⁋따름정리 10](/ko/math/commutative_algebra/koszul_complex#cor10)) 재배열한 열 또한 $Z\cap U_i$의 모든 점에서 regular sequence이기 때문이다. 도입부에서 요구하였던 순서 무관성이 회수되는 것이 이것이다.

다음 명제는 complete intersection이 그 이름값을 한다는 것, 즉 codimension이 자르는 방정식의 개수와 정확히 일치함을 보여준다.

::: 명제 2
Codimension $k$의 complete intersection $\iota:Z\hookrightarrow X$의 모든 irreducible component는 $X$에서 codimension $k$를 갖는다.
:::
::: 증명
Codimension은 국소적으로 계산되므로, $Z$의 irreducible component $W$를 고정하고 [정의 1](#def1)의 cover 가운데 $W$와 만나는 $U_i$를 택하자. 그러한 $U_i$에 대해서는 $Z\cap U_i\neq\emptyset$이므로 [정의 1](#def1)의 두 대안 가운데 뒤의 것이 성립하며, 따라서 $X=\Spec A$, $Z=Z(s_1,\ldots, s_k)$이고 $(s_1,\ldots, s_k)$가 $A$-regular sequence인 경우만 보면 충분하다. $W$에 대응되는 $A$의 prime ideal을 $\mathfrak{p}$라 하면 $\mathfrak{p}$는 $A/(s_1,\ldots, s_k)$의 minimal prime이므로 

$$\dim A_\mathfrak{p}/(s_1,\ldots, s_k)=\dim\bigl(A/(s_1,\ldots, s_k)\bigr)_\mathfrak{p}=0$$

이다. 한편 [§차원, ⁋명제 8](/ko/math/scheme_theory/dimension#prop8)에 의하여 $\codim_X W=\dim A_\mathfrak{p}$이므로, $\dim A_\mathfrak{p}=k$임을 보이면 된다. 

이를 위해 다음 사실을 보인다.

> Noetherian local ring $(R,\mathfrak{m})$의 non-zerodivisor $s\in\mathfrak{m}$에 대하여 $\dim R/(s)=\dim R-1$이다.

[§차원, ⁋명제 12](/ko/math/scheme_theory/dimension#prop12)을 $\Spec R$에 적용하면 $V(s)$의 모든 component는 codimension $0$ 또는 $1$이고, $s$가 non-zerodivisor이므로 ([\[가환대수학\] §동반소아이디얼, ⁋정리 7](/ko/math/commutative_algebra/associated_primes#thm7)) $s$는 어떠한 minimal prime에도 속하지 않아 codimension $0$인 component는 없다. 따라서 $V(s)$의 모든 component는 codimension $1$이고, $\dim R/(s)=\dim R-1$이다. 

이제 $(s_1,\ldots, s_k)$가 $A$-regular sequence이므로 localization $A_\mathfrak{p}$에서도 regular sequence이며 (localization은 non-zerodivisor를 보존한다), 각 $s_{i+1}$은 $A_\mathfrak{p}/(s_1,\ldots, s_i)$의 non-zerodivisor이다. 위 사실을 $i=0,1,\ldots, k-1$에 차례로 적용하면 

$$0=\dim A_\mathfrak{p}/(s_1,\ldots, s_k)=\dim A_\mathfrak{p}-k$$

를 얻으므로 $\dim A_\mathfrak{p}=k$, 즉 $\codim_X W=k$이다.
:::

::: 예시 3
1. Affine space $\mathbb{A}^n_\mathbb{K}=\Spec\mathbb{K}[\x_1,\ldots, \x_n]$과 상수가 아닌 다항식 $f$를 생각하자. $\mathbb{K}[\x_1,\ldots, \x_n]$이 integral domain이므로 $0\neq f$는 non-zerodivisor이고, 따라서 hypersurface $Z(f)\hookrightarrow\mathbb{A}^n_\mathbb{K}$은 effective Cartier divisor, 즉 codimension $1$의 complete intersection이다. 

2. 좌표부분공간 $Z(\x_1,\ldots, \x_k)\hookrightarrow \mathbb{A}^n_\mathbb{K}$를 생각하자. 각 $i$에 대하여 

	$$\mathbb{K}[\x_1,\ldots, \x_n]/(\x_1,\ldots, \x_i)\cong\mathbb{K}[\x_{i+1},\ldots, \x_n]$$

	은 integral domain이므로 $\x_{i+1}$은 이 ring에서 non-zerodivisor이다. 즉 $(\x_1,\ldots, \x_k)$는 regular sequence이고, $Z(\x_1,\ldots, \x_k)$는 codimension $k$의 complete intersection이다. [명제 2](#prop2)와 부합하게 이 부분공간의 codimension은 정확히 $k$이다. 
:::

거꾸로 codimension이 $k$라고 하여 complete intersection이 되는 것은 아니다. 가령 $\mathbb{A}^4_\mathbb{K}$ 안에서 원점에서만 만나는 두 평면의 합집합 $Z(\x_1,\x_2)\cup Z(\x_3,\x_4)$는 codimension $2$이지만 complete intersection이 아니다. 이를 확인하려면 complete intersection의 local ring이 regular local ring을 regular sequence로 나눈 것이어서 Cohen-Macaulay가 된다는 것과, 이 합집합의 원점에서의 local ring이 그렇지 않다는 것을 보아야 한다. 우리는 이 두 사실을 증명 없이 가져다 쓰고 자세한 것은 [\[가환대수학\] §Cohen-Macaulay 환](/ko/math/commutative_algebra/cohen_macaulay_rings)에 위임한다.

::: 참고 4
[정의 1](#def1)은 regular sequence를 <em-ko>국소적으로만</em-ko> 요구한다. 이보다 강한 조건으로, field $\mathbb{K}$ 위의 projective space $\mathbb{P}^n=\Proj S$ ($S=\mathbb{K}[\x_0,\ldots, \x_n]$)의 projective subscheme $Z$가 $S$-regular sequence를 이루는 codimension만큼의 homogeneous polynomial들의 vanishing으로 <em-ko>대역적으로</em-ko> 잘리는 경우를 *global complete intersection<sub>대역적 완전교차</sub>*이라 부른다. 자르는 방정식의 개수가 codimension과 같기만 하면 이들이 $S$-regular sequence를 이루는 것은 $S$가 Cohen-Macaulay라는 사실로부터 자동으로 따라오지만, 우리는 이를 가져다 쓰지 않고 regular sequence 조건을 정의의 일부로 둔다. 이 조건은 [정의 1](#def1)과 일치하지 않는다. 예를 들어 $\mathbb{P}^3$ 안의 twisted cubic은 codimension $2$의 local complete intersection이지만 두 개의 homogeneous polynomial로 잘리지 않아 global complete intersection은 아니며, 이는 [예시 9](#ex9)에서 확인한다. 
:::

## 코쥴 분해와 conormal sheaf

[정의 1](#def1)이 요구하는 것은 국소적으로 하나의 regular sequence가 $Z$를 잘라낸다는 것인데, regular sequence의 Koszul 복합체가 acyclic이라는 것은 이미 확인한 바이다. ([\[가환대수학\] §코쥴 복합체, ⁋정리 7](/ko/math/commutative_algebra/koszul_complex#thm7)) 이를 associated sheaf로 옮기면 complete intersection의 structure sheaf가 각 chart 위에서 명시적인 유한 자유 분해를 갖는다는 것이 된다.

::: 명제 5
Locally Noetherian scheme $X$의 codimension $k$ complete intersection $\iota:Z\hookrightarrow X$와, $Z\cap U=Z(s_1,\ldots, s_k)$이고 $s_1,\ldots, s_k$가 $A$-regular sequence인 affine open subset $U=\Spec A$가 주어졌다 하자. 그럼 $\mathcal{O}_U$-module층들의 sequence

$$0 \rightarrow \mathcal{O}_U^{\oplus\binom{k}{k}} \rightarrow \mathcal{O}_U^{\oplus\binom{k}{k-1}} \rightarrow \cdots \rightarrow \mathcal{O}_U^{\oplus\binom{k}{1}} \rightarrow \mathcal{O}_U \rightarrow (\iota_\ast\mathcal{O}_Z)\vert_U \rightarrow 0$$

은 exact이다. 여기에서 $\mathcal{O}_U^{\oplus\binom{k}{j}}$은 Koszul 복합체 $K(s_1,\ldots, s_k)$의 $j$번째 항의 associated sheaf이고, differential 또한 그 복합체의 것을 associated sheaf로 옮긴 것이다.
:::
::: 증명
$s_1,\ldots, s_k$가 $A$-regular sequence이므로 [\[가환대수학\] §코쥴 복합체, ⁋따름정리 8](/ko/math/commutative_algebra/koszul_complex#cor8)에 의하여 $K(s_1,\ldots, s_k)$는 $A/(s_1,\ldots, s_k)$의 free resolution이다. 곧 $K_j(s_1,\ldots, s_k)\cong A^{\oplus\binom{k}{j}}$이므로 $A$-module들의 exact sequence

$$0 \rightarrow A^{\oplus\binom{k}{k}} \rightarrow \cdots \rightarrow A^{\oplus\binom{k}{1}} \rightarrow A \rightarrow A/(s_1,\ldots, s_k) \rightarrow 0$$

을 얻는다. associated sheaf functor는 exact이므로 ([§준연접층, ⁋명제 6](/ko/math/scheme_theory/quasicoherent_sheaves#prop6)) 이를 associated sheaf로 옮기면 위의 sequence가 exact이다. 마지막 항에 대해서는 $Z\cap U=Z(s_1,\ldots, s_k)$가 $\Spec A/(s_1,\ldots, s_k)$이고 ([§닫힌 부분스킴, ⁋정의 7](/ko/math/scheme_theory/closed_subschemes#def7) 이후의 논의) closed embedding을 따라 밀어낸 것이 그 associated sheaf이므로 ([§준연접층, ⁋명제 18](/ko/math/scheme_theory/quasicoherent_sheaves#prop18), [§준연접층, ⁋정리 10](/ko/math/scheme_theory/quasicoherent_sheaves#thm10)), $(\iota_\ast\mathcal{O}_Z)\vert_U\cong \widetilde{A/(s_1,\ldots, s_k)}$이다.
:::

이 분해의 오른쪽 끝 두 항이 담고 있는 정보를 ideal sheaf의 언어로 옮기면 complete intersection 고유의 성질이 나온다. Ideal sheaf $\mathcal{I}=\mathcal{I}_{Z/X}$에 대하여 ([§닫힌 부분스킴, ⁋정의 5](/ko/math/scheme_theory/closed_subschemes#def5)) $\mathcal{I}$는 $\mathcal{I}/\mathcal{I}^2$ 위에 자명하게 작용하므로 $\mathcal{I}/\mathcal{I}^2$은 $\mathcal{O}_X/\mathcal{I}=\iota_\ast\mathcal{O}_Z$-module층이고, 따라서 $Z$ 위의 quasi-coherent sheaf로 볼 수 있다. 일반적으로 이 sheaf에 대해서는 아무것도 말할 수 없지만, 자르는 방정식들이 regular sequence를 이루면 그 개수만큼의 자유도를 정확히 갖는다.

::: 명제 6
Locally Noetherian scheme $X$의 codimension $k$ complete intersection $\iota:Z\hookrightarrow X$와 그 ideal sheaf $\mathcal{I}=\mathcal{I}_{Z/X}$에 대하여, $\mathcal{I}/\mathcal{I}^2$은 $Z$ 위의 rank $k$의 locally free sheaf이다.
:::
::: 증명
주장은 $Z$의 각 점 주위에서 확인하면 되는 국소적인 것이고 $Z$의 점을 담는 chart는 $Z$와 만나므로, [정의 1](#def1)의 cover 가운데 $Z$와 만나는 것을 택하여 $X=\Spec A$, $\mathfrak{a}=\mathcal{I}(X)=(s_1,\ldots, s_k)$이고 $s_1,\ldots, s_k$가 $A$-regular sequence인 경우만 보면 충분하다. $\mathcal{I}$는 quasi-coherent sheaf이므로 ([§준연접층, ⁋명제 18](/ko/math/scheme_theory/quasicoherent_sheaves#prop18)) $\mathcal{I}=\widetilde{\mathfrak{a}}$이고 ([§준연접층, ⁋정리 10](/ko/math/scheme_theory/quasicoherent_sheaves#thm10)), $\mathcal{I}^2$은 곱셈 $\mathcal{I}\otimes_{\mathcal{O}_X}\mathcal{I} \rightarrow \mathcal{O}_X$의 image로서 associated sheaf functor가 exact이고 tensor product와 호환되므로 $\widetilde{\mathfrak{a}^2}$이다. 따라서 $\mathcal{I}/\mathcal{I}^2=\widetilde{\mathfrak{a}/\mathfrak{a}^2}$이고, $\mathfrak{a}/\mathfrak{a}^2$이 rank $k$의 free $A/\mathfrak{a}$-module임을 보이면 된다.

$A/\mathfrak{a}$-linear map $\psi:(A/\mathfrak{a})^{\oplus k} \rightarrow \mathfrak{a}/\mathfrak{a}^2$을 $e_i\mapsto s_i+\mathfrak{a}^2$으로 정의하자. $\mathfrak{a}$가 $s_i$들로 생성되므로 $\psi$는 surjective이다. Injectivity를 보이기 위해 $a_1,\ldots, a_k\in A$가 $\sum_ia_is_i\in \mathfrak{a}^2$을 만족한다 하자. $\mathfrak{a}^2$은 곱 $s_is_j$들로 생성되므로 적당한 $b_{ij}\in A$에 대하여 $\sum_ia_is_i=\sum_{i,j}b_{ij}s_is_j$이고, $c_i=a_i-\sum_jb_{ij}s_j$로 두면 $\sum_ic_is_i=0$이다. 곧 $\sum_ic_ie_i$는 Koszul 복합체 $K(s_1,\ldots, s_k)$의 degree $1$ cycle인데, [\[가환대수학\] §코쥴 복합체, ⁋정리 7](/ko/math/commutative_algebra/koszul_complex#thm7)에 의하여 $H_1(K(s_1,\ldots, s_k))=0$이므로 이는 boundary이다. Koszul differential이 $d(e_i\wedge e_j)=s_ie_j-s_je_i$로 주어지므로 boundary의 각 성분은 $\mathfrak{a}$에 속하고, 따라서 모든 $i$에 대하여 $c_i\in \mathfrak{a}$이다. 그럼 $a_i=c_i+\sum_jb_{ij}s_j\in \mathfrak{a}$이므로 $(A/\mathfrak{a})^{\oplus k}$ 안에서 $\sum_ia_ie_i=0$이고, $\psi$는 injective이다.
:::

$\mathcal{I}/\mathcal{I}^2$이 놓이는 자리는 conormal exact sequence이다. Closed subscheme $Z\hookrightarrow X$와 base scheme $S$에 대하여 [§Kähler 미분과 여접층, ⁋명제 2](/ko/math/scheme_theory/sheaf_of_differentials#prop2)를 associated sheaf로 옮기면 $Z$ 위의 exact sequence

$$\mathcal{I}/\mathcal{I}^2 \longrightarrow \Omega_{X/S}\vert_Z \longrightarrow \Omega_{Z/S} \longrightarrow 0$$

을 얻는데, [명제 6](#prop6)은 complete intersection의 경우 이 sequence의 왼쪽 항이 rank $k$의 locally free sheaf임을 말해준다. 곧 $Z$의 법선 방향은 자르는 방정식의 개수만큼의 자유도를 가지며, 이는 국소적인 방정식들이 서로 독립적이라는 것의 정확한 표현이다. 한편 이 sequence의 왼쪽 끝에 $0$을 붙일 수 있는지, 곧 왼쪽 morphism이 injective인지는 complete intersection이라는 조건만으로는 결정되지 않고 $Z$ 자신에 대한 조건을 더 요구한다.

## Hilbert polynomial과 degree

[참고 4](#rmk4)가 구별한 두 조건 가운데 강한 쪽, 곧 projective space 안에서 대역적으로 잘리는 경우에는 [명제 5](#prop5)의 국소적인 분해가 하나의 대역적인 분해로 붙는다. 각 chart 위의 자유 module이 twisting sheaf로 바뀔 뿐이다. 이 절에서는 ambient가 언제나 projective space가므로 표기를 바꾸어, 앞 절까지 ambient를 가리키던 $X$를 여기에서는 $\mathbb{P}^n$의 closed subscheme을 가리키는 데 쓴다. 따라서 [명제 5](#prop5)와 [명제 6](#prop6)을 적용할 때에는 그 진술의 $X$를 $\mathbb{P}^n$의 chart로, $Z$를 $X$와 그 chart의 교집합으로 읽는다.

::: 명제 7
Field $\mathbb{K}$ 위의 projective space $\mathbb{P}^n=\Proj S$ ($S=\mathbb{K}[\x_0,\ldots, \x_n]$)와 각각 degree $d_i>0$인 homogeneous polynomial들 $f_1,\ldots, f_k$가 주어지고, 이들이 $S$-regular sequence를 이룬다 하자. $X=V_+(f_1,\ldots, f_k)$이고 $\iota:X\hookrightarrow \mathbb{P}^n$이 그 closed embedding일 때 ([§projective space의 닫힌 부분스킴, ⁋명제 1](/ko/math/scheme_theory/closed_subschemes_of_projective_spaces#prop1)) 다음이 성립한다.

1. $\iota$는 codimension $k$의 complete intersection이며, [정의 1](#def1)의 affine open cover로 표준 chart들 $\{D_+(\x_m)\}_{m=0}^n$을 택할 수 있다.
2. $J\subseteq \{1,\ldots, k\}$에 대하여 $d_J=\sum_{i\in J}d_i$로 적으면, $\mathcal{O}_{\mathbb{P}^n}$-module층들의 sequence

	$$0 \rightarrow \bigoplus_{\lvert J\rvert=k}\mathcal{O}(-d_J) \rightarrow \cdots \rightarrow \bigoplus_{\lvert J\rvert=1}\mathcal{O}(-d_J) \rightarrow \mathcal{O}_{\mathbb{P}^n} \rightarrow \iota_\ast\mathcal{O}_X \rightarrow 0$$

	은 exact이다. 여기에서 $\lvert J\rvert=j$인 summand에서 $\lvert J'\rvert=j-1$인 summand로 가는 성분은 $J'=J\setminus\{i\}$일 때 Koszul differential의 부호를 곱한 $f_i$ 배이고 그 밖에는 $0$이다.
:::
::: 증명
Chart $D_+(\x_m)=\Spec S_{(\x_m)}$을 고정하고 $g_i=f_i/\x_m^{d_i}\in S_{(\x_m)}$이라 하자. [§사영공간의 닫힌 부분스킴, ⁋명제 1](/ko/math/scheme_theory/closed_subschemes_of_projective_spaces#prop1)의 증명에서 확인한 chart별 기술에 의하여 $X\cap D_+(\x_m)=Z(g_1,\ldots, g_k)$이다.

먼저 $S_{\x_m}$을 degree로 분해하면 $S_{\x_m}=\bigoplus_{j\in\mathbb{Z}}\x_m^jS_{(\x_m)}$이며 각각의 $\x_m^jS_{(\x_m)}$은 $S_{(\x_m)}$과 isomorphic한 $S_{(\x_m)}$-module이다. $g_i$들이 degree $0$이므로 이들이 생성하는 ideal 또한 이 분해와 호환되어 임의의 $i$에 대하여 $S_{\x_m}/(g_1,\ldots, g_i)=\bigoplus_j\x_m^j\bigl(S_{(\x_m)}/(g_1,\ldots, g_i)\bigr)$이고, 곱하기 $g_{i+1}$은 각각의 성분을 보존한다. 이로부터 두 가지를 얻는다. 우선 곱하기 $g_{i+1}$이 $S_{\x_m}/(g_1,\ldots, g_i)$ 위에서 injective인 것은 $S_{(\x_m)}/(g_1,\ldots, g_i)$ 위에서 injective인 것과 동치이다. 또 위의 direct sum이 소멸하는 것은 그 각각의 성분이 소멸하는 것과 동치이므로, $(g_1,\ldots, g_i)S_{\x_m}$이 proper인 것은 $(g_1,\ldots, g_i)S_{(\x_m)}$이 proper인 것과 동치이다.

이제 $X\cap D_+(\x_m)\neq\emptyset$일 때 $g_1,\ldots, g_k$가 $S_{(\x_m)}$-regular sequence임을 본다. 가정에 의하여 $Z(g_1,\ldots, g_k)\neq \emptyset$이므로 $(g_1,\ldots, g_k)$는 $S_{(\x_m)}$의 proper ideal이고, 위의 degree 분해에 의하여 $(g_1,\ldots, g_k)S_{\x_m}$ 또한 proper이다. 한편 $\x_m$은 $S_{\x_m}$에서 unit이므로 각각의 $i$에 대하여 $(f_1,\ldots, f_i)S_{\x_m}=(g_1,\ldots, g_i)S_{\x_m}$이고 $f_{i+1}$과 $g_{i+1}$은 unit 배만큼만 다르다. 특히 $(f_1,\ldots, f_k)S_{\x_m}$이 proper이며, localization이 exact이므로 $f_1,\ldots, f_k$는 $S_{\x_m}$-regular sequence이고 따라서 $g_1,\ldots, g_k$ 또한 그러하다. 다시 위의 degree 분해에 의하여 $g_1,\ldots, g_k$는 $S_{(\x_m)}$-regular sequence이다.

표준 chart들 $\{D_+(\x_m)\}_{m=0}^n$은 $\mathbb{P}^n$의 affine open cover이고, 각각에 대하여 $X\cap D_+(\x_m)$은 공집합이거나 방금 얻은 regular sequence가 잘라내는 것이므로, 이로부터 1번을 얻는다.

2번을 보자. $\lvert J\rvert=j$인 $J$에 대응하는 summand $\mathcal{O}(-d_J)$를 chart $D_+(\x_m)$ 위에서 생성절단 $\x_m^{-d_J}$로 trivialize하면 ([§스킴의 층 코호몰로지, ⁋정의 5](/ko/math/scheme_theory/sheaf_cohomology_of_schemes#def5)), 곱하기 $f_i$로 주어지는 $\mathcal{O}(-d_J) \rightarrow \mathcal{O}(-d_{J\setminus\{i\}})$은 $\x_m^{-d_J}a\mapsto \x_m^{-d_{J\setminus\{i\}}}g_ia$가 되어 곱하기 $g_i$이다. 곧 위의 sequence를 $D_+(\x_m)$으로 제한한 것은 $K(g_1,\ldots, g_k)$의 associated sheaf에 $\widetilde{S_{(\x_m)}/(g_1,\ldots, g_k)}$를 이어붙인 것이다. $X$와 만나는 chart 위에서 이것이 exact이라는 것은, 방금 얻은 regular sequence 성질과 함께 ambient를 $D_+(\x_m)$으로 하고 그 closed subscheme을 $X\cap D_+(\x_m)$으로 하여 적용한 [명제 5](#prop5)이다. $X$와 만나지 않는 chart 위에서는 $(g_1,\ldots, g_k)=S_{(\x_m)}$이므로 [\[가환대수학\] §코쥴 복합체, ⁋명제 3](/ko/math/commutative_algebra/koszul_complex#prop3)에 의하여 모든 Koszul homology가 소멸하고, 특히 $H_0=S_{(\x_m)}/(g_1,\ldots, g_k)=0$이라 마지막 항도 $0$이 되어 역시 exact이다. Exactness는 stalk에서 확인되고 이러한 chart들이 $\mathbb{P}^n$을 덮으므로 위의 sequence는 exact이다.
:::

이제 각 항이 projective space 위의 line bundle들의 유한 direct sum이므로, [§스킴의 층 코호몰로지](/ko/math/scheme_theory/sheaf_cohomology_of_schemes)에서 계산한 Euler characteristic을 교대합으로 더하면 $X$의 Hilbert polynomial이 그대로 읽힌다.

::: 따름정리 8
[명제 7](#prop7)의 상황에서 $X\neq \emptyset$이라 하자. 그럼 $k\leq n$이고, $X$의 Hilbert polynomial은

$$P_{\mathcal{O}_X}(t)=\sum_{J\subseteq\{1,\ldots, k\}}(-1)^{\lvert J\rvert}\binom{n+t-d_J}{n}$$

이다. 더욱이 $\dim X=n-k$이며 $\deg X=d_1\cdots d_k$이다.
:::
::: 증명
[명제 7](#prop7)의 exact sequence에 invertible sheaf $\mathcal{O}(t)$를 tensor하여도 exactness가 유지되고, closed embedding에 대하여 $(\iota_\ast\mathcal{O}_X)\otimes\mathcal{O}(t)\cong \iota_\ast(\mathcal{O}_X(t))$이며 cohomology가 $\iota_\ast$ 아래에서 보존된다. ([§스킴의 층 코호몰로지, ⁋정리 8](/ko/math/scheme_theory/sheaf_cohomology_of_schemes#thm8) 직전의 관찰) 따라서 $\rchi(X,\mathcal{O}_X(t))=\rchi(\mathbb{P}^n,\iota_\ast\mathcal{O}_X(t))$이고, [§스킴의 층 코호몰로지, ⁋명제 14](/ko/math/scheme_theory/sheaf_cohomology_of_schemes#prop14)의 2번을 이 유한 exact sequence에 적용한 뒤 [§스킴의 층 코호몰로지, ⁋따름정리 15](/ko/math/scheme_theory/sheaf_cohomology_of_schemes#cor15)로 각 항을 계산하면

$$\rchi(X,\mathcal{O}_X(t))=\sum_{j=0}^k(-1)^j\sum_{\lvert J\rvert=j}\rchi\bigl(\mathbb{P}^n,\mathcal{O}(t-d_J)\bigr)=\sum_J(-1)^{\lvert J\rvert}\binom{n+t-d_J}{n}$$

을 얻는다. [§스킴의 층 코호몰로지, ⁋정리 16](/ko/math/scheme_theory/sheaf_cohomology_of_schemes#thm16)에 의하여 좌변은 $P_{\mathcal{O}_X}(t)$이다.

남은 것은 이 다항식의 degree와 최고차항 계수를 읽는 일이다. 우선 degree $m\geq 1$이고 최고차항 계수가 $c\neq 0$인 다항식 $p$와 $d>0$에 대하여, $p(t)-p(t-d)$는 degree $m-1$이고 그 최고차항 계수는 $cmd$이다. 실제로 $c\bigl(t^m-(t-d)^m\bigr)$에서 $t^m$ 항이 소거되어 $cmdt^{m-1}$이 남고, $p$의 나머지 항들이 기여하는 것은 degree $m-2$ 이하이기 때문이다. 또 $p$가 상수이면 $p(t)-p(t-d)=0$이다.

$p_0(t)=\binom{n+t}{n}$으로 두고 $p_i(t)=p_{i-1}(t)-p_{i-1}(t-d_i)$로 정의하면, $i$에 대한 귀납법으로

$$p_i(t)=\sum_{J\subseteq\{1,\ldots, i\}}(-1)^{\lvert J\rvert}\binom{n+t-d_J}{n}$$

이므로 $p_k$가 위에서 얻은 다항식이다. 여기에서 $p_0$은 degree $n$이고 최고차항 계수가 $1/n!$이다. 만일 $k>n$이라면 위의 관찰에 의하여 $p_n$은 상수이고 $p_{n+1}=0$이므로 $p_k=0$인데, $X\neq\emptyset$이라 $\mathcal{O}_X\neq 0$이므로 [§스킴의 층 코호몰로지, ⁋정리 16](/ko/math/scheme_theory/sheaf_cohomology_of_schemes#thm16)에 의하여 $P_{\mathcal{O}_X}$의 degree는 $\dim X\geq 0$이 되어 모순이다. 따라서 $k\leq n$이다.

그럼 $i=1,\ldots, k$의 각 단계에서 $p_{i-1}$의 degree $n-i+1$이 $1$ 이상이므로 위의 관찰을 그대로 적용할 수 있고, $p_i$는 degree $n-i$이며 그 최고차항 계수는

$$\frac{1}{n!}\cdot nd_1\cdot (n-1)d_2\cdots (n-i+1)d_i=\frac{d_1\cdots d_i}{(n-i)!}$$

이다. $r=n-k$로 두면 $P_{\mathcal{O}_X}$는 degree $r$이고 최고차항 계수는 $d_1\cdots d_k/r!$이므로, 다시 [§스킴의 층 코호몰로지, ⁋정리 16](/ko/math/scheme_theory/sheaf_cohomology_of_schemes#thm16)에 의하여 $\dim X=r=n-k$이고 [§스킴의 층 코호몰로지, ⁋정의 17](/ko/math/scheme_theory/sheaf_cohomology_of_schemes#def17)에 의하여 $\deg X=r!\cdot d_1\cdots d_k/r!=d_1\cdots d_k$이다.
:::

$k=1$인 경우 [따름정리 8](#cor8)은 degree $e$의 hypersurface가 $\deg X=e$를 갖는다는 것으로, 이는 [§스킴의 층 코호몰로지, ⁋정의 17](/ko/math/scheme_theory/sheaf_cohomology_of_schemes#def17) 이후에 직접 계산한 것과 같다. 일반적인 $k$에 대해서는 이것이 Bézout 정리의 가장 단순한 형태로, 서로 regular sequence를 이루는 방정식들이 잘라내는 대상의 degree가 방정식들의 degree의 곱이라는 것이다. 이 강한 수치적 제약은 어떤 부분스킴이 global complete intersection이 될 수 없는 이유를 곧바로 준다.

::: 예시 9
1. $\mathbb{P}^3_\mathbb{K}=\Proj S$ 안에서 $S$-regular sequence를 이루는 두 quadric $f_1,f_2$가 잘라내는 $X=V_+(f_1,f_2)$를 생각하자. 그러한 quadric은 실제로 존재하는데, 가령 $f_1=\x_0\x_1$과 $f_2=\x_2\x_3$이 그러하다. $S$는 UFD이고 이 두 원소는 서로소이므로, $f_2g\in (f_1)$이면 $f_1$이 $g$를 나누어 $f_2$가 $S/(f_1)$에서 non-zerodivisor이기 때문이다. 이제 $n=3$, $k=2$, $d_1=d_2=2$이므로 [따름정리 8](#cor8)에 의하여

	$$P_{\mathcal{O}_X}(t)=\binom{3+t}{3}-2\binom{1+t}{3}+\binom{t-1}{3}=\frac{(t+3)(t+2)(t+1)-2(t+1)t(t-1)+(t-1)(t-2)(t-3)}{6}=4t$$

	이다. 곧 $\dim X=1$이고 $\deg X=1!\cdot 4=4$이며, arithmetic genus는 $p_a(X)=(-1)^1\bigl(P_{\mathcal{O}_X}(0)-1\bigr)=1$이다. ([§스킴의 층 코호몰로지, ⁋정의 17](/ko/math/scheme_theory/sheaf_cohomology_of_schemes#def17)) 두 quadric이 일반적인 위치에 있을 때 얻어지는 것이 고전적인 elliptic quartic curve이며, 위의 $f_1=\x_0\x_1$, $f_2=\x_2\x_3$의 경우 $X$는 네 직선 $V_+(\x_0,\x_2)$, $V_+(\x_0,\x_3)$, $V_+(\x_1,\x_3)$, $V_+(\x_1,\x_2)$의 합집합으로서, 나열한 순서로 이웃한 것끼리만 한 점에서 만나고 마주보는 두 직선은 만나지 않는다. 이 퇴화된 경우도 위와 같은 수치적 불변량을 갖는다.

2. $\mathbb{P}^3_\mathbb{K}$의 twisted cubic $C$, 곧 $\mathbb{P}^1=\Proj \mathbb{K}[\y_0,\y_1]$ 위의 invertible sheaf $\mathcal{O}_{\mathbb{P}^1}(3)$과 이를 globally generate하는 절단 $\y_0^3, \y_0^2\y_1, \y_0\y_1^2, \y_1^3$이 정의하는 morphism $\varphi:\mathbb{P}^1 \rightarrow \mathbb{P}^3_\mathbb{K}$의 image를 생각하자. ([§인자와 선형계, §§Ample invertible sheaf](/ko/math/scheme_theory/divisors_and_linear_systems#ample-invertible-sheaf)) 각각의 표준 chart $D_+(\x_j)$에 대하여 $\varphi^{-1}(D_+(\x_j))$은 $j=0$이면 $D_+(\y_0)=\Spec\mathbb{K}[\y_1/\y_0]$, $j=3$이면 $D_+(\y_1)=\Spec\mathbb{K}[\y_0/\y_1]$, 그 밖에는 $D_+(\y_0\y_1)=\Spec\mathbb{K}[\y_0/\y_1,\y_1/\y_0]$이고, 대응하는 ring homomorphism $\x_i/\x_j\mapsto \y_0^{3-i}\y_1^i/\y_0^{3-j}\y_1^j$의 image는 차례로 $\y_1/\y_0$, $\y_0/\y_1$, 그리고 이 둘 모두를 담으므로 언제나 surjective이다. 표준 chart들은 $\mathbb{P}^3_\mathbb{K}$의 affine open cover를 이루고, [§닫힌 부분스킴, ⁋명제 3](/ko/math/scheme_theory/closed_subschemes#prop3)의 증명은 이 조건을 하나의 affine open cover 위에서 확인하면 충분함을 보였으므로 $\varphi$는 closed embedding이다. 따라서 $C\cong\mathbb{P}^1$이며 $\mathcal{O}_C(1)=\varphi^\ast\mathcal{O}(1)\cong \mathcal{O}_{\mathbb{P}^1}(3)$이다. 그럼 [§스킴의 층 코호몰로지, ⁋정리 16](/ko/math/scheme_theory/sheaf_cohomology_of_schemes#thm16)와 [§스킴의 층 코호몰로지, ⁋따름정리 15](/ko/math/scheme_theory/sheaf_cohomology_of_schemes#cor15)에 의하여

	$$P_{\mathcal{O}_C}(t)=\rchi\bigl(\mathbb{P}^1,\mathcal{O}_{\mathbb{P}^1}(3t)\bigr)=\binom{1+3t}{1}=3t+1$$

	이므로 $\dim C=1$이고 $\deg C=1!\cdot 3=3$이다. 만일 $C$가 $S$-regular sequence를 이루는 두 homogeneous polynomial $f_1,f_2$에 대하여 $C=V_+(f_1,f_2)$의 꼴이라면, 상수는 $0$이든 아니든 regular sequence의 항이 될 수 없으므로 $d_1,d_2>0$이고 [따름정리 8](#cor8)에 의하여 $d_1d_2=3$이다. 그럼 둘 가운데 하나는 degree $1$이고, 곧 $C$가 hyperplane $V_+(\ell)$에 담긴다. 그런데 $\ell=\sum_ia_i\x_i$를 $C\cong\mathbb{P}^1$로 당기면 $\sum_ia_i\y_0^{3-i}\y_1^i$이고 $\y_0^3,\y_0^2\y_1,\y_0\y_1^2,\y_1^3$은 $\Gamma(\mathbb{P}^1,\mathcal{O}_{\mathbb{P}^1}(3))$에서 일차독립이므로 모든 $a_i$가 $0$이어야 한다. 따라서 그러한 $\ell$은 없고, [참고 4](#rmk4)의 의미에서 $C$는 global complete intersection이 아니다.
:::

---

**참고문헌**

**[Vak]** R. Vakil, *The rising sea: Foundation of algebraic geometry*. Available [online](https://math.stanford.edu/~vakil/216blog/). 

