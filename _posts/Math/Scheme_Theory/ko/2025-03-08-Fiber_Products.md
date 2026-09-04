---
title: "올곱"
description: "스킴 사이의 올곱 정의와 보편 성질을 다루며, affine scheme들의 올곱 존재성을 증명한다."
excerpt: "Category of S-schemes에서의 fiber product 정의와 존재성"

categories: [Math / Scheme Theory]
permalink: /ko/math/scheme_theory/fiber_products
sidebar: 
    nav: "scheme_theory-ko"

date: 2025-03-08
weight: 12

---

우리가 scheme을 도입하며 약속한 것들 중 하나는 fiber product였으며, 이는 $\Sch_{/S}$ 위에서의 곱이므로 이를 위해서는 $S$-scheme들 (그리고 scheme morphism들)을 정의했어야 했다. 이제 우리는 준비를 마치고 fiber product를 정의한다. 

## 올곱의 정의와 존재성

우리는 [§스킴 사이의 사상, ⁋정의 3](/ko/math/scheme_theory/morphism_of_schemes#def3)에서 scheme morphism $X \rightarrow S$를 *$S$-scheme*이라 부르기로 하였다. 이번 글에서 우리는 category $\Sch_{/S}$에서의 product를 정의할 것이다. 

::: 정의 1
두 scheme morphism $\varphi_X:X \rightarrow S$, $\varphi_Y:Y \rightarrow S$의 fiber product를 $X\times_SY$로 적는다. ([\[범주론\] §극한, ⁋예시 8](/ko/math/category_theory/limits#ex8))
:::

즉, $X\times_SY$는 다음의 성질을 만족한다.

> 다음의 diagram
> 
> {% diagram Math/Scheme_Theory/Fiber_Products-1.svg width="9.32em" alt="fiber_diagram" %}
> 
> 이 commute한다. 뿐만 아니라, 식 $\varphi_Y\circ\psi_Y=\varphi_X\circ\psi_X$를 만족하는 임의의 $\psi_X:Z \rightarrow X$, $\psi_Y:Z \rightarrow Y$가 주어질 때마다 유일한 $\psi:Z \rightarrow X\times_SY$가 존재하여 $\psi_X=\rho_X\circ\psi$이고 $\psi_Y=\rho_Y\circ\psi$이다.
> 
> {% diagram Math/Scheme_Theory/Fiber_Products-2.svg width="13.72em" alt="universal_product" %}

따라서, $X\times_SY$에서 $S$로의 canonical morphism이 존재하며, 이로부터 우리는 $X\times_SY$를 $S$-scheme으로 볼 수 있다. 뿐만 아니라, 이 관점에서 $X\times_SY$는 $\Sch_{/S}$에서의 product이기도 하다는 것이 정의로부터 자명하다.

[§스킴 사이의 사상, ⁋예시 4](/ko/math/scheme_theory/morphism_of_schemes#ex4) 이후에 우리는 임의의 scheme $X$는 항상 유일한 방식으로 $\mathbb{Z}$-scheme으로 생각할 수 있다는 것을 보았다. 따라서 [정의 1](#def1)을 만족하는 fiber product $X\times_SY$가 항상 존재한다고 가정하면, 우리는 임의의 두 scheme $X, Y$에 대하여 $X\times_{\Spec \mathbb{Z}}Y$가 $X$와 $Y$의 product를 주는 것을 안다. 

[정의 1](#def1)은 fiber product $X\times_SY$의 존재성에 대해서는 어떠한 것도 보장해주지 않으므로, 이것이 진짜 정의가 되기 위해서는 $X\times_SY$의 존재성을 별도로 증명해주어야 한다. ([정리 8](#thm8)) 그러나 특별히 $\AffSch$에서 fiber product의 존재성은 거의 자명하며, 이것이 우리의 증명의 시작이 될 것이다.

::: 보조정리 2
Affine scheme들 사이의 morphism $\Spec A \rightarrow \Spec C$, $\Spec B \rightarrow\Spec C$가 주어졌다 하자. 그럼

$$\Spec A\times_{\Spec C}\Spec B\cong\Spec (A\otimes_C B)$$

가 성립한다.
:::
::: 증명
$\AffSch\cong\cRing^\op$를 통해 $\Spec A \rightarrow \Spec C$, $\Spec B \rightarrow \Spec C$를 $C \rightarrow A$, $C \rightarrow B$로 바꿔놓고 [\[대수적 구조\] §대수의 직접곱, 직합, 텐서곱, ⁋정리 8](/ko/math/algebraic_structures/operations_of_algebras#thm8)의 universal property와 fiber product의 universal property를 비교하면 된다. 이 비교가 affine scheme뿐 아니라 임의의 scheme $T$를 test object로 삼아도 성립하는 것은, [§아핀스킴, ⁋정리 13](/ko/math/scheme_theory/affine_schemes#thm13)에 의하여 임의의 ring $R$에 대하여 $\Hom_\Sch(T, \Spec R)\cong \Hom_\cRing(R, \Gamma(T))$이기 때문이다.
:::

이제 일반적인 scheme에 대해 fiber product가 존재한다는 사실은 [보조정리 2](#lem2)에서 살펴본 affine scheme에서의 결과를 바탕으로, 이들을 잘 붙일 수 있다는 것을 보이면 된다. 

우선, $Z$의 open subscheme $U$가 주어졌을 때, 이를 inclusion morphism을 이용하여 $\iota:U \rightarrow Z$와 같은 꼴로 쓰면 다음 보조정리는 거의 말장난이다. 

::: 보조정리 3
Scheme morphism $\varphi: Y \rightarrow Z$와 $Z$의 open subscheme $\iota: U \rightarrow Z$가 주어졌다 하자. 그럼 다음의 diagram

{% diagram Math/Scheme_Theory/Fiber_Products-3.svg width="8.22em" alt="open_subscheme" %}

은 fiber diagram이다.
:::
::: 증명
$\varphi^{-1}(U)$가 fiber product의 universal property를 만족한다. 
:::

이제 이를 약간 활용하면 다음의 보조정리를 보일 수 있다. 

::: 보조정리 4
Affine scheme들 $X, Y, Z$가 주어졌다 하고, $Y$의 open subscheme $Y'\hookrightarrow Y$가 주어졌다 하자. 그럼 $X\rightarrow Z$와 $Y'\hookrightarrow Y \rightarrow Z$의 fiber product $X\times_ZY'$가 존재한다.
:::
::: 증명
우선 [보조정리 2](#lem2)로부터 다음의 fiber diagram 

{% diagram frozen/635a8f80/Math/Scheme_Theory/Fiber_Products-4.svg width="9.32em" alt="open_fiber_product-1" %}

이 존재하는 것을 안다. 이제 다음의 데이터

{% diagram frozen/635a8f80/Math/Scheme_Theory/Fiber_Products-5.svg width="8.55em" alt="open_fiber_product-2" %}

를 생각하면, 우리는 [보조정리 3](#lem3)으로부터 $X\times_ZY$의 open subscheme $\rho_Y^{-1}(Y')$가 fiber product가 되는 것을 확인할 수 있다. 이제 일반적으로 다음의 diagram

{% diagram frozen/635a8f80/Math/Scheme_Theory/Fiber_Products-6.svg width="8.55em" alt="magic_square" %}

에서 작은 두 사각형이 fiber diagram이라면 외곽의 큰 사각형도 fiber diagram이므로 원하는 결과를 얻는다. 
:::

이제 이를 이용하면 affine scheme과 임의의 scheme의 fiber product가 존재한다는 것을 보일 수 있다.

::: 보조정리 5
Affine scheme들 $X, Z$ 그리고 임의의 scheme $Y$에 대하여, $X\rightarrow Z$와 $Y \rightarrow Z$의 fiber product $X\times_ZY$가 존재한다.
:::
::: 증명
이를 위해 $Y$를 affine open subset들 $Y_i$들로 덮자. 그럼 우리는 [보조정리 2](#lem2)으로부터 $X\times_ZY_i$들이 존재함을 안다. 또, $Y_{ij}=Y_i\cap Y_j$는 affine scheme $Y_i$의 open subscheme이므로 역시 $X\times_Z Y_{ij}$가 [보조정리 4](#lem4)에 의하여 존재한다. 

한편, [보조정리 4](#lem4)의 증명을 보면 $X\times_ZY_{ij}$는 각각 $X\times_ZY_i$와 $X\times_ZY_j$의 open subscheme인 것을 알 수 있다. 이들 데이터가 [§스킴, ⁋보조정리 9](/ko/math/scheme_theory/schemes#lem9)의 조건들을 만족하는 것을 쉽게 확인할 수 있으므로, 이들을 붙여 scheme $X\times_ZY$를 만들 수 있다. 이것이 fiber product의 universal property를 만족하는 것은 다음과 같이 확인한다. Scheme $W$와 morphism $\alpha: W \rightarrow X$, $\beta: W \rightarrow Y$가 $Z$ 위에서 일치한다 하고 $W_i=\beta^{-1}(Y_i)$라 두자. 그럼 $\beta$를 $W_i$로 제한한 것은 $W_i \rightarrow Y_i$를 정의하므로, $X\times_ZY_i$의 universal property로부터 유일한 morphism $\sigma_i: W_i \rightarrow X\times_ZY_i$를 얻는다. 이제 $W_i\cap W_j=\beta^{-1}(Y_{ij})$ 위에서 $\sigma_i$와 $\sigma_j$는 모두 $X\times_ZY_{ij}$의 universal property가 주는 유일한 morphism과 같으므로 서로 일치하며, 따라서 [§스킴 사이의 사상, ⁋명제 1](/ko/math/scheme_theory/morphism_of_schemes#prop1)에 의하여 이들은 유일한 morphism $\sigma: W \rightarrow X\times_ZY$로 붙는다. 여기에서 공역을 $Y_i$로 제한하는 것이 아니라 정의역을 $W_i$로 제한한다는 것에 주의해야 하는데, $\beta$의 image가 $Y_i$에 들어갈 이유가 없기 때문이다. 
:::

이 보조정리에서 $X$가 affine scheme이라는 가정은 오직 $X\times_ZY_i$가 존재한다는 것을 보이기 위해서만 사용되었다. 따라서, 임의의 두 scheme $X,Y$와 affine scheme $Z$, 그리고 scheme morphism $X \rightarrow Z$와 $Y \rightarrow Z$가 주어졌다 하면 우리는 $Y$의 affine open cover $\{Y_i\}$를 택한 후 [보조정리 5](#lem5)에서 두 인자의 역할을 바꾸어 적용할 수 있다. 즉 $Y_i$와 $Z$가 affine이므로 $Y_i\times_ZX$가 존재하고, fiber product는 두 인자의 순서에 대해 대칭이므로 $X\times_ZY_i$가 존재한다. 또 $Y_{ij}$는 $Y_i$의 open subscheme이므로 [보조정리 4](#lem4)의 증명과 같은 방식으로 $X\times_ZY_{ij}$가 존재하며 이는 $X\times_ZY_i$와 $X\times_ZY_j$의 open subscheme이다. 따라서 [보조정리 5](#lem5)의 증명에서의 접합 논증을 그대로 반복하면 다음을 얻는다.

::: 보조정리 6
Affine scheme $Z$, 임의의 scheme $X,Y$와 scheme morphism $X \rightarrow Z$, $Y \rightarrow Z$에 대하여, fiber product $X\times_ZY$가 존재한다. 
:::

이제 마지막으로 $Z$를 임의의 scheme으로 확장해야 한다. 우선 다음이 성립한다.

::: 보조정리 7
임의의 scheme $X,Y,Z$가 주어졌다 하고, scheme morphism $\varphi_X:X \rightarrow Z$, $\varphi_Y:Y \rightarrow Z$ 그리고 affine scheme $Z'$로의 monomorphism $\iota: Z \rightarrow Z'$가 주어졌다 하자. 가령 $\iota$가 open immersion이거나 closed embedding인 경우가 이에 해당한다. 후자의 경우, $\iota\circ \alpha=\iota\circ \beta$인 두 morphism $\alpha,\beta: T \rightarrow Z$가 주어졌다 하면 $\iota$가 단사이므로 연속함수로서 $\alpha=\beta$이고, 각각의 $t\in T$에서 $\iota^\sharp$이 stalk 사이의 surjection $\mathcal{O}_{Z',\iota(\alpha(t))} \rightarrow \mathcal{O}_{Z,\alpha(t)}$을 유도하므로 ([§닫힌 부분스킴, ⁋정의 2](/ko/math/scheme_theory/closed_subschemes#def2)) $\alpha^\sharp$와 $\beta^\sharp$는 그 합성에 의해 결정되어 서로 같다. 그럼 $\iota\circ\varphi_X$와 $\iota\circ\varphi_Y$의 fiber product $X\times_{Z'}Y$는 $X\times_ZY$의 universal property를 만족하고, 따라서 $X\times_ZY$가 존재한다.  
:::
::: 증명
$Z'$이 affine이므로 $X\times_{Z'}Y$는 존재한다. 이제 임의의 scheme $T$와 morphism $\alpha:T \rightarrow X$, $\beta:T \rightarrow Y$가 주어졌다 하자. $X\times_ZY$의 universal property에서 요구하는 조건은 $\varphi_X\circ \alpha=\varphi_Y\circ \beta$이고, $X\times_{Z'}Y$의 것은 $\iota\circ\varphi_X\circ \alpha=\iota\circ\varphi_Y\circ \beta$인데, $\iota$가 monomorphism이므로 이 두 조건은 서로 동치이다. 따라서 두 fiber product는 같은 universal property를 만족하고, 유일성에 의하여 $X\times_{Z'}Y$가 $X\times_ZY$의 역할을 한다.

한편 $\iota$에 대한 가정이 없으면 이는 성립하지 않는다. 가령 $k$-scheme의 structure morphism $\iota:Z \rightarrow \Spec k$를 택하고 $X=Y=Z=\mathbb{A}^1_k$에 identity morphism을 주면, $X\times_ZY=\mathbb{A}^1_k$이지만 $X\times_{\Spec k}Y=\mathbb{A}^2_k$이다.
:::

이제 위의 보조정리를 이용하여 우리는 임의의 $X,Y,Z$와 scheme morphism $\varphi_X:X \rightarrow Z$, $\varphi_Y: Y \rightarrow Z$에 대하여 $Z$를 affine open cover $\{Z_i\}$들로 덮으면 $\varphi_X\vert^{Z_i}:\varphi_X^{-1}(Z_i) \rightarrow Z_i$와 $\varphi_Y\vert^{Z_i}:\varphi_Y^{-1}(Z_i) \rightarrow Z_i$에 대해서는, $X_i=\varphi_X^{-1}(Z_i)$와 $Y_i=\varphi_Y^{-1}(Z_i)$로 쓰면 fiber product $X_i\times_{Z_i}Y_i$가 존재하는 것을 안다. 이제 교집합 $Z_{ij}=Z_i\cap Z_j$은 $Z_i$의 열린집합이므로 [보조정리 7](#lem7)에 의하여 $\varphi_X\vert^{Z_{ij}}$와 $\varphi_Y\vert^{Z_{ij}}$의 fiber product들도 존재하며 이는 $X_i\times_{Z_i}Y_i$와 $X_j\times_{Z_j}Y_j$의 open subscheme이다. 따라서 [보조정리 5](#lem5)의 증명과 마찬가지로, 이들 데이터가 [§스킴, ⁋보조정리 9](/ko/math/scheme_theory/schemes#lem9)의 조건을 만족한다는 것을 보이면 다음 정리를 얻는다.

::: 정리 8
임의의 scheme $X,Y,Z$와 scheme morphism $X \rightarrow Z$, $Y \rightarrow Z$에 대하여, fiber product $X\times_ZY$가 존재한다.
:::
::: 증명
Gluing에 필요한 것은 두 조각 $X_i\times_{Z_i}Y_i$와 $X_j\times_{Z_j}Y_j$ 안에서 $Z_{ij}$ 위의 fiber product에 해당하는 열린집합들이 canonical하게 identify되고, 이 identification들이 triple intersection 위에서 cocycle condition을 만족한다는 것이다. 그런데 두 열린집합은 모두 $\varphi_X\vert^{Z_{ij}}$와 $\varphi_Y\vert^{Z_{ij}}$의 fiber product의 universal property를 만족하므로 그 사이의 identification은 유일하게 결정되며, triple intersection 위에서 얻어지는 세 identification 또한 $Z_{ijk}=Z_i\cap Z_j\cap Z_k$ 위의 fiber product의 universal property가 주는 유일한 사상이므로, 그 가운데 두 개의 합성은 나머지 하나와 같아 cocycle condition이 성립한다. 따라서 [§스킴, ⁋보조정리 9](/ko/math/scheme_theory/schemes#lem9)에 의하여 이들은 하나의 scheme으로 붙는다.

이렇게 얻어진 scheme이 universal property를 만족하는 것은 [보조정리 5](#lem5)의 증명에서와 같다. 즉 morphism $\alpha: W \rightarrow X$, $\beta: W \rightarrow Y$가 $Z$ 위에서 일치한다 하면 $W_i=(\varphi_X\circ \alpha)^{-1}(Z_i)$로 두고 각 $W_i$에서 $X_i\times_{Z_i}Y_i$로의 유일한 morphism을 얻은 후, 겹침에서의 일치를 위와 같이 universal property의 유일성으로 확인하여 붙이면 된다.
:::

## Fiber product의 해석

Scheme morphism을 해석하는 방법이 여러가지가 존재하듯, fiber product도 이해하는 방법이 여러가지가 있다. 

앞서 우리는 scheme morphism $X \rightarrow S$를 $S$로 parametrize된 family로 생각하기로 하였으며 ([§스킴 사이의 사상, ⁋예시 10](/ko/math/scheme_theory/morphism_of_schemes#ex10)) 이 관점에서 $S$는 family $X$의 base로 생각할 수 있다. 이제 임의의 $S$-family $X \rightarrow S$가 주어졌다 하고, scheme morphism $S' \rightarrow S$가 주어졌다 하면 fiber product를 통해 우리는 새로운 $S'$-family $X\times_SS' \rightarrow S'$를 얻는다. 이러한 관점에서 우리는 종종 fiber product를 *base change*라 부르기도 한다. 

::: 예시 9
Affine scheme으로 우리의 관심범위를 좁혀보면, $\Spec B$가 $C$-scheme이라는 것은 scheme morphism $\Spec B \rightarrow \Spec C$가 주어졌다는 것이고 이는 다시 ring homomorphism $C \rightarrow B$가 주어진 것과 같고 이는 다시 $B$가 $C$-algebra라는 것과 같은 말이다. 

이제 여기에 더해 scheme morphism $\Spec A \rightarrow \Spec C$가 주어졌다 하고 위의 base change가 어떠한 것을 주는지를 살펴보면, [보조정리 2](#lem2)에 의해 우리는 이렇게 얻어지는 것이

$$\Spec A\times_{\Spec C}\Spec B=\Spec(A\otimes_CB) \rightarrow \Spec A$$

즉 ring homomorphism $A \rightarrow A\otimes_CB$임을 안다. 즉, base change는 (affine scheme의 경우에는) 별다른 것이 아니라 [\[대수적 구조\] §스칼라의 변환, ⁋정의 3](/ko/math/algebraic_structures/change_of_base_ring#def3)에 불과하다. 
:::

특별히 $B$-algebra $B[\x_1,\ldots,\x_n]$와 임의의 ring homomorphism $B \rightarrow A$에 대하여, 다음 식

$$A\otimes_BB[\x_1,\ldots,\x_n]\cong A[\x_1,\ldots, \x_n]$$

이 성립하는 것으로부터 다음의 diagram

{% diagram Math/Scheme_Theory/Fiber_Products-7.svg width="20.67em" alt="adding_extra_variables" %}

이 fiber diagram인 것을 안다. 

이 관점은 중요한 것이지만, 지금 당장은 여기에 있는 기하학적인 직관이 잘 보이지 않는다. 이를 위해 특별히 $S' \rightarrow S$가 embedding인 경우를 생각하자. 

우선 임의로 주어진 $S$-family $X \rightarrow S$와 open embedding $S' \rightarrow S$에 대하여, [보조정리 3](#lem3)은 $S'$-family $X\times_SS' \rightarrow S'$가 단순히 $X \rightarrow S$의 base를 $S'$로 제한하여 얻어진 것임을 보여준다. 여기에 더하여 $X \rightarrow S$ 또한 open embedding이라 가정하면, 우리는 $X\times_SS'$가 ($S$ 안에서의) $X$와 $S'$의 교집합임을 안다. 

위의 논증은 closed embedding인 경우에도 성립한다. 이를 위해서는 [보조정리 3](#lem3)에 해당하는 다음 보조정리를 보여야 한다.

::: 보조정리 10
Ring homomorphism $\phi: B \rightarrow A$와 $B$의 임의의 ideal $\mathfrak{b}$에 대하여, isomorphism 

$$A/\phi(\mathfrak{b})A\cong A \otimes_B(B/\mathfrak{b})$$

이 존재한다. 
:::
::: 증명
Ideal $\mathfrak{b}$로부터 얻어지는 다음의 exact sequence

$$\mathfrak{b} \rightarrow B \rightarrow B/\mathfrak{b} \rightarrow 0$$

에 $\otimes_BA$를 취하면 다음의 exact sequence

$$A\otimes_B \mathfrak{b} \rightarrow A\otimes_BB \rightarrow A\otimes_B (B/\mathfrak{b}) \rightarrow 0$$

을 얻고, 이 때 $A\otimes_B \mathfrak{b}$의 $A\otimes_BB\cong A$에서의 image가 $\phi(\mathfrak{b})A$이므로 원하는 결과를 얻는다.
:::

이제 임의의 closed embedding은 국소적으로는 항상 $B \rightarrow B/\mathfrak{b}$로부터 오는 것이므로 위의 논의를 closed embedding에 대해서도 동일하게 적용할 수 있다. 특히 두 closed embedding의 교집합이 잘 정의된다. 

::: 예시 11
$Z=\Spec\mathbb{K}[\x,\y]$의 두 closed subscheme 

$$X=\Spec \mathbb{K}[\x,\y]/(\y)=\Spec \mathbb{K}[\x],\qquad Y=\Spec \mathbb{K}[\x,\y]/(\x)=\Spec \mathbb{K}[\y]$$

을 생각하자. 그럼 $X$와 $Y$는 각각 $Z=\mathbb{A}^2_\mathbb{K}$의 $\x$축과 $\y$축에 해당하며, 그 closed embedding은 projection들

$$\mathbb{K}[\x,\y] \rightarrow \mathbb{K}[\x],\qquad \mathbb{K}[\x,\y] \rightarrow \mathbb{K}[\y]$$

로 주어진다. 이제 $X\times_ZY$는, [보조정리 2](#lem2)에 의하여, 

$$\Spec\left(\frac{\mathbb{K}[\x,\y]}{(\y)}\otimes_{\mathbb{K}[\x,\y]} \frac{\mathbb{K}[\x,\y]}{(\x)}\right)\cong \Spec \mathbb{K}[\x,\y]/(\x,\y)\cong\Spec \mathbb{K}$$

로 주어지는 것을 확인할 수 있으며 이는 정확히 $\x$축과 $\y$축의 교점인 원점에 해당한다.

이번에는 위의 계산에서 $Y$를 다음의 closed subscheme

$$Y=\Spec \mathbb{K}[\x,\y]/(\y-\x^2)$$

으로 바꿔보자. $\y=\x^2$과 $\x$축의 교점은 마찬가지로 원점이지만, 이번에는 중근이 존재하므로 scheme 구조는 위와 다르게 주어져야 할 것이다. 실제로 계산을 반복하면 $X\times_ZY$는

$$\Spec\left(\frac{\mathbb{K}[\x,\y]}{(\y)}\otimes_{\mathbb{K}[\x,\y]}\frac{\mathbb{K}[\x,\y]}{(\y-\x^2)}\right)\cong\Spec \mathbb{K}[\x,\y]/(\y,\y-\x^2)\cong\Spec \mathbb{K}[\x]/(\x^2)$$

이 된다. 
:::

이 관점에서 우리는 scheme morphism $\varphi:X \rightarrow Y$의 $y_0\in Y$에서의 fiber $\varphi^{-1}(y_0)$을 어떻게 정의해야 하는지도 알 수 있다. $y_0$ 하나만을 담는 scheme에서 $Y$로 가는 morphism을 만든 후, 이 morphism과 $\varphi$의 fiber product를 취하면 된다. 여기에서 한점집합 $\{y_0\}$을 $Y$의 부분공간으로 보아 embedding을 취할 수는 없다는 것에 주의해야 한다. $y_0$가 closed point가 아니면 $\{y_0\}$은 일반적으로 $Y$의 locally closed subset조차 아니기 때문이다. 가령 $\mathbb{A}^2$의 generic point가 그러하다. 

이제 $\Spec\kappa(y) \rightarrow Y$를 만들기 위해 $y$에서의 residue field $\kappa(y)$를 생각하자. 그럼 $\Spec\kappa(y)$는 항상 한점집합이다. 뿐만 아니라, $y$를 포함하는 $Y$의 affine open subset $V=\Spec B$를 생각하고, $y$가 prime ideal $\mathfrak{q}_y$에 대응된다 하면 canonical morphism

$$B \rightarrow B_{\mathfrak{q}_y} \rightarrow B_{\mathfrak{q}_y}/\mathfrak{q}_y B_{\mathfrak{q}_y} =\kappa(\mathfrak{q}_y)=\kappa(y)$$

을 통해 $\Spec\kappa(y)\rightarrow \Spec B$가 정의되며 $\Spec \kappa(y)$의 (유일한) 점 $(0)$은 위의 morphism을 통해 $\mathfrak{q}_y$로 옮겨진다. 따라서 다음을 정의한다.

::: 정의 12
Scheme morphism $\varphi: X \rightarrow Y$에 대하여, $Y$의 한 점 $y\in Y$에서의 *fiber<sub>올</sub>*를

$$\varphi^{-1}(y)=X\times_Y\Spec \kappa(y)$$

으로 정의한다. 만일 $Y$가 irreducible이라면, $Y$의 generic point에서의 fiber를 *generic fiber<sub>일반 올</sub>*라 부른다. 
:::

이 정의는 연속함수로서의 preimage와 같은 기호를 사용하고 있으며, 실제로 두 대상은 위상공간으로서 일치한다.

::: 보조정리 13
Scheme morphism $\varphi: X \rightarrow Y$와 $y\in Y$에 대하여, projection $X\times_Y\Spec\kappa(y) \rightarrow X$는 집합으로서의 preimage $\{x\in X\mid \varphi(x)=y\}$ 위로의 homeomorphism이다.
:::
::: 증명
[보조정리 4](#lem4)의 증명과 같은 방식으로 fiber product를 만드는 것은 $X$와 $Y$를 열린집합으로 제한하는 것과 호환되므로, $y\in V=\Spec B$인 affine open subset $V$를 택하고 $\varphi^{-1}(V)$를 affine open subset $\Spec A$들로 덮어 $X=\Spec A$, $Y=\Spec B$인 경우만 보이면 충분하다. 이 때 $y$에 대응되는 prime ideal을 $\mathfrak{q}$, $\phi: B \rightarrow A$를 $\varphi$에 대응되는 ring homomorphism이라 하자.

[보조정리 2](#lem2)에 의하여 $X\times_Y\Spec \kappa(\mathfrak{q})=\Spec (A\otimes_B\kappa(\mathfrak{q}))$이다. 한편 $\kappa(\mathfrak{q})=B_\mathfrak{q}/\mathfrak{q}B_\mathfrak{q}$이므로, $S=\phi(B\setminus \mathfrak{q})$라 두면

$$A\otimes_B\kappa(\mathfrak{q})\cong (S^{-1}A)/\mathfrak{q}(S^{-1}A)$$

이다. 그럼 [§스펙트럼, ⁋명제 9](/ko/math/scheme_theory/spectrums#prop9)를 두 번 적용하여, $\Spec (A\otimes_B\kappa(\mathfrak{q})) \rightarrow \Spec A$는 그 image 위로의 homeomorphism이며 그 image는 $S$와 만나지 않으면서 $\mathfrak{q}(S^{-1}A)$를 포함하는 prime ideal들, 곧 $\phi^{-1}(\mathfrak{p})\subseteq \mathfrak{q}$와 $\mathfrak{q}\subseteq \phi^{-1}(\mathfrak{p})$를 동시에 만족하는 $\mathfrak{p}\in \Spec A$들의 모임임을 안다. 이는 정확히 $(\Spec\phi)(\mathfrak{p})=\mathfrak{q}$인 점들의 모임이다.
:::

::: 예시 14
$\operatorname{char}\mathbb{K}\neq 2$인 algebraically closed field $\mathbb{K}$에 대하여, ring homomorphism $\mathbb{K}[\x] \rightarrow \mathbb{K}[\y]$을 식 $\x \mapsto \y^2$으로 정의하고, 이로부터 얻어지는 scheme morphism $\varphi: \Spec \mathbb{K}[\y] \rightarrow \Spec \mathbb{K}[\x]$를 생각하자. 그럼 $\Spec\mathbb{K}[\x]$의 임의의 점 $(\x-a)$에서의 residue field는 

$$\Frac(\mathbb{K}[\x]/(\x-a))=\mathbb{K}[\x]/(\x-a)$$

이다. 이제 임의의 $a\in \mathbb{K}$에 대하여,

$$\varphi^{-1}((\x-a))=\Spec \mathbb{K}[\y]\times_{\Spec \mathbb{K}[\x]}\Spec \mathbb{K}[\x]/(\x-a)\cong \Spec(\mathbb{K}[\y]\otimes_{\mathbb{K}[\x]}\mathbb{K}[\x]/(\x-a))=\Spec \mathbb{K}[\y]/(\y^2-a)$$

이며, 따라서 만일 $a=0$이라면 $\varphi^{-1}((\x))\cong\Spec \mathbb{K}[\y]/(\y^2)$이고, $a\neq 0$이라면 $\mathbb{K}$가 algebraically closed이고 $\operatorname{char}\mathbb{K}\neq 2$라는 가정으로부터 

$$\Spec \mathbb{K}[\y]/(\y^2-a)\cong \Spec \mathbb{K}[\y]/(\y-\sqrt{a})\coprod \Spec \mathbb{K}[\y]/(\y+\sqrt{a})$$

임을 안다. 한편 $\mathbb{K}[\x]$의 generic point $(0)$에 대해서는 $\kappa((0))=\mathbb{K}(\x)$이므로 

$$\varphi^{-1}((0))=\Spec \mathbb{K}[\y]\times_{\Spec \mathbb{K}[\x]}\Spec \mathbb{K}(\x)\cong \Spec\mathbb{K}(\y)$$

이 된다. 
:::

위의 예시는 이미 [§스킴 사상의 성질들, ⁋예시 16](/ko/math/scheme_theory/properties_of_scheme_morphisms#ex16)에서 살펴보았던 것이다. 해당 예시에서 우리는 finite morphism이 항상 quasi-finite라는 사실을 주장했는데, 이제 이를 증명할 수 있다. 

::: 명제 15
Finite morphism $\varphi: X \rightarrow Y$는 quasi-finite morphism이다. 
:::
::: 증명
우선 [§스킴 사상의 성질들, ⁋명제 15](/ko/math/scheme_theory/properties_of_scheme_morphisms#prop15)에 의하여 finite morphism은 integral이면서 locally of finite type이고, integral morphism은 affine이므로 quasi-compact이어서 $\varphi$는 morphism of finite type이다. 따라서 fiber들이 유한집합임만 보이면 되는데, [보조정리 13](#lem13)에 의하여 집합 $\varphi^{-1}(y)$의 점들은 scheme $X\times_Y\Spec\kappa(y)$의 점들과 일대일로 대응하므로, 후자의 점의 개수를 세면 된다. 그럼 affine인 경우만 보이면 충분하다. 즉, 임의의 finite ring homomorphism $\phi: B \rightarrow A$와 $B$의 prime ideal $\mathfrak{q}$에 대하여 $A\otimes_B\kappa(\mathfrak{q})$가 유한히 많은 prime ideal을 갖는다는 것을 보이면 충분하다. 그런데 $\phi$가 finite이므로 $A\otimes_B\kappa(\mathfrak{q})$는 finite $\kappa(\mathfrak{q})$-algebra이고 따라서 Artinian이며, [\[가환대수학\] §조르단-횔더 정리, ⁋따름정리 6](/ko/math/commutative_algebra/Jordan-Holder_theorem#cor6)에 의하여 $0$이 유한히 많은 maximal ideal들의 곱이므로 임의의 prime ideal은 그 가운데 하나와 같아 원하는 결과를 얻는다.
:::

위의 예시와 명제들에서 우리는 중요한 관찰을 할 수 있는데, $X \rightarrow S$가 만족하는 성질이 임의의 $S' \rightarrow S$로의 base change $X\times_SS' \rightarrow S'$에도 이어지는 경우가 많다는 것이다. 물론 모든 성질이 그런 것은 아니다. 가령 dominant는 보존되지 않는데, $\Spec \mathbb{K}(\t) \rightarrow \Spec \mathbb{K}[\t]$는 generic point로의 dominant morphism이지만 $\t=0$을 따라 base change하면 공집합에서 한 점으로 가는 morphism이 된다. 그러나 우리가 관심을 가지는 대부분의 성질은 base change에 대해 닫혀있다. 

::: 명제 16
만일 scheme morphism $\varphi:X \rightarrow Z$가 quasicompact (resp. quasiseparated, affine, finite, integral, locally of finite type, finite type, locally of finite presentation, finite presentation, quasi-finite, surjective) 라면, 임의의 scheme morphism $Y \rightarrow Z$를 통해 $\varphi$를 base change한 $X\times_ZY \rightarrow Y$ 또한 그러하다.
:::
::: 증명
모든 성질에 공통되는 환원을 먼저 해 두자. $Z$의 affine open covering을 이루는 $\Spec A$들을 택하고, 각각의 $\Spec A$에 대하여 $Y \rightarrow Z$에 의한 그 preimage를 affine open subset $\Spec C$들로 덮으면, 이렇게 얻어진 $\Spec C$들은 $Y$의 affine open covering을 이룬다. 이제 projection을 $\rho_Y: X\times_ZY \rightarrow Y$라 하면, [보조정리 3](#lem3)과 [보조정리 4](#lem4)의 증명에서 사용한 "작은 두 사각형이 fiber diagram이면 외곽의 큰 사각형도 fiber diagram"이라는 사실로부터

$$\rho_Y^{-1}(\Spec C)\cong X\times_Z\Spec C\cong \varphi^{-1}(\Spec A)\times_{\Spec A}\Spec C$$

를 얻는다. 따라서 $X_A=\varphi^{-1}(\Spec A)$, $W=X_A\times_{\Spec A}\Spec C$라 쓰면, base change $\rho_Y$를 $\Spec C$ 위에서 살펴보는 것은 $X_A \rightarrow \Spec A$의 $\Spec C \rightarrow \Spec A$를 따른 base change $W \rightarrow \Spec C$를 살펴보는 것과 같다. 뿐만 아니라 같은 이유로, $X_A$의 임의의 affine open subset $\Spec B$에 대하여 projection $\rho: W \rightarrow X_A$에 의한 그 preimage는 [보조정리 2](#lem2)에 의하여

$$\rho^{-1}(\Spec B)\cong \Spec B\times_{\Spec A}\Spec C\cong \Spec (B\otimes_AC)$$

이므로, $X_A$의 affine open covering $\{\Spec B_i\}$가 주어질 때마다 $\{\Spec (B_i\otimes_AC)\}$는 $W$의 affine open covering이 된다. 즉 모든 문제는 ring homomorphism $C \rightarrow B\otimes_AC$에 대한 문제로 환원된다. 이제 각각의 성질을 살펴본다.

우선 $\varphi$가 affine이라 하자. 그럼 $X_A$는 affine scheme $\Spec B$이고 따라서 $\rho_Y^{-1}(\Spec C)=W\cong\Spec (B\otimes_AC)$는 affine이므로, $Y$의 affine open covering $\{\Spec C\}$와 [§스킴 사상의 성질들, ⁋명제 9](/ko/math/scheme_theory/properties_of_scheme_morphisms#prop9)에 의하여 $\rho_Y$는 affine이다.

$\varphi$가 quasi-compact이라 하자. 그럼 $X_A$는 quasi-compact이므로 유한히 많은 affine open subset $\Spec B_1,\ldots, \Spec B_n$으로 덮이고, 따라서 $W$는 유한히 많은 affine open subset $\Spec (B_i\otimes_AC)$들로 덮여 quasi-compact이다. 이제 [§스킴 사상의 성질들, ⁋명제 7](/ko/math/scheme_theory/properties_of_scheme_morphisms#prop7)의 첫째 결과에 의하여 $\rho_Y$는 quasi-compact이다.

$\varphi$가 quasi-separated라 하자. 그럼 $X_A$는 quasi-separated scheme이다. $X_A$의 affine open covering $\{\Spec B_i\}$를 택하면 $\{W_i=\Spec (B_i\otimes_AC)\}$는 $W$의 affine open covering이고, $\Spec B_i\cap \Spec B_j$가 quasi-compact이므로 이를 $\Spec B_i$의 유한히 많은 principal open set $D(h_1),\ldots, D(h_s)$의 합집합으로 쓸 수 있어 ([§스펙트럼, ⁋보조정리 11](/ko/math/scheme_theory/spectrums#lem11))

$$W_i\cap W_j=\rho^{-1}(\Spec B_i\cap \Spec B_j)=\bigcup_{t=1}^s\Spec \bigl((B_i)_{h_t}\otimes_AC\bigr)$$

는 유한히 많은 affine open subset의 합집합, 곧 quasi-compact이다. 이제 일반적으로 scheme $W$가 $W_i\cap W_j$들이 모두 quasi-compact인 affine open covering $\{W_i\}$를 갖는다면 $W$가 quasi-separated임을 보이자. $W$의 임의의 quasi-compact open subset은 유한히 많은 affine open subset의 합집합이므로, $W$의 임의의 두 affine open subset $P,Q$에 대하여 $P\cap Q$가 quasi-compact임을 보이면 충분하다. [§스킴의 위상구조, ⁋보조정리 11](/ko/math/scheme_theory/topology_of_schemes#lem11)과 $P,Q$의 quasi-compactness에 의하여 $P$와 $Q$는 각각 유한히 많은, 자기 자신과 어떤 $W_i$ 모두에서 principal open set인 열린집합들로 덮이므로, 결국 $W_i$의 principal open set $D(f)$와 $W_j$의 principal open set $D(g)$에 대하여 $D(f)\cap D(g)$가 quasi-compact임을 보이면 된다. 그런데 $D(f)\cap D(g)\subseteq W_i\cap W_j$이고 $W_i\cap W_j$는 quasi-compact이므로 이를 $W_i$의 유한히 많은 principal open set $D(h_1),\ldots, D(h_s)$의 합집합으로 쓸 수 있고, 따라서

$$D(f)\cap D(g)=\bigcup_{t=1}^s\bigl(D(fh_t)\cap D(g)\bigr)$$

이다. 이 때 각각의 $D(fh_t)$는 $W_i\cap W_j$에 포함되는 affine open subset이므로 이를 $W_j$의 affine open subset으로 보면 $D(fh_t)\cap D(g)$는 $g$의 restriction이 affine scheme $D(fh_t)$ 위에서 정의하는 principal open set이고 ([§스펙트럼, ⁋명제 8](/ko/math/scheme_theory/spectrums#prop8)) 따라서 affine이다. 즉 $D(f)\cap D(g)$는 유한히 많은 affine open subset의 합집합이므로 quasi-compact이다. 이상에서 $W$는 quasi-separated이고, [§스킴 사상의 성질들, ⁋명제 7](/ko/math/scheme_theory/properties_of_scheme_morphisms#prop7)의 둘째 결과에 의하여 $\rho_Y$는 quasi-separated이다.

$\varphi$가 integral (resp. finite)이라 하자. 그럼 $\varphi$는 affine이므로 $X_A=\Spec B$이고 $A \rightarrow B$가 integral (resp. finite)이다. 따라서 $\rho_Y^{-1}(\Spec C)=\Spec (B\otimes_AC)$이고 [\[가환대수학\] §정수적 확장, ⁋명제 14](/ko/math/commutative_algebra/integral_extension#prop14)에 의하여 $C \rightarrow B\otimes_AC$ 또한 integral (resp. finite)이다. 이 두 성질이 affine-local on target이라는 것은 [§스킴 사상의 성질들, ⁋정의 11](/ko/math/scheme_theory/properties_of_scheme_morphisms#def11) 직후에 살펴보았으므로, $Y$의 affine open covering $\{\Spec C\}$ 위에서 확인한 것으로 충분하다.

$\varphi$가 locally of finite type이라 하자. $X_A$의 affine open covering $\{\Spec B_i\}$를 택하면 각각의 $A \rightarrow B_i$는 finite type이고, $B_i$를 $A$-algebra로서 생성하는 원소들을 $x_1,\ldots, x_n$이라 하면 $B_i\otimes_AC$는 $C$-algebra로서 $x_1\otimes 1,\ldots, x_n\otimes 1$에 의해 생성되므로 $C \rightarrow B_i\otimes_AC$ 또한 finite type이다. 이제 $W$의 <em-ko>모든</em-ko> affine open subset에 대하여 같은 결론을 얻어야 하는데, 이는 방금 만든 affine open covering $\{\Spec (B_i\otimes_AC)\}$에 [§스킴 사상의 성질들, ⁋보조정리 13](/ko/math/scheme_theory/properties_of_scheme_morphisms#lem13)을 적용하면 얻어진다. 즉 $\rho_Y$는 locally of finite type이다. 또 morphism of finite type은 quasi-compact이면서 locally of finite type인 morphism이므로, 위의 quasi-compact인 경우와 종합하면 finite type 또한 base change에 대해 보존된다.

$\varphi$가 locally of finite presentation이라 하자. [§스킴 사상의 성질들, ⁋정의 18](/ko/math/scheme_theory/properties_of_scheme_morphisms#def18)의 조건은 preimage의 <em-ko>어떤</em-ko> affine open covering에 대한 조건이므로 이 경우는 오히려 간단하다. 가정에 의하여 $X_A$의 affine open covering $\{\Spec B_i\}$가 존재하여 각각의 $B_i$가

$$B_i\cong A[\x_1,\ldots, \x_n]/(f_1,\ldots, f_m)$$

의 꼴이도록 할 수 있고, 그럼 [예시 9](#ex9) 이후에 살펴본 isomorphism $C\otimes_AA[\x_1,\ldots, \x_n]\cong C[\x_1,\ldots, \x_n]$과 [보조정리 10](#lem10)으로부터

$$B_i\otimes_AC\cong C[\x_1,\ldots, \x_n]/(\bar{f}_1,\ldots, \bar{f}_m)$$

이므로 ($\bar{f}_k$는 $f_k$의 계수를 $C$로 보낸 것) $C \rightarrow B_i\otimes_AC$ 또한 finitely presented이다. 즉 $W$의 affine open covering $\{\Spec (B_i\otimes_AC)\}$가 $\Spec C$ 위에서 요구되는 조건을 증언한다. 이 성질이 affine-local on target이라는 것은 [§스킴의 위상구조, ⁋보조정리 12](/ko/math/scheme_theory/topology_of_schemes#lem12)를 성질 "$\varphi^{-1}(\Spec B)$가, $B \rightarrow R_i$가 모두 finitely presented인 affine open covering $\{\Spec R_i\}$를 갖는다"에 적용하여 얻어진다. 실제로 [§스킴의 위상구조, ⁋정의 9](/ko/math/scheme_theory/topology_of_schemes#def9)의 첫째 조건은 $\varphi^{-1}(D(f))$가 $\Spec (R_i)_f$들로 덮이고 $(R_i)_f\cong R_i\otimes_BB_f$가 finitely presented homomorphism의 base change라는 것으로부터, 둘째 조건은 $B \rightarrow B_f\cong B[\y]/(f\y-1)$가 finitely presented이고 finitely presented homomorphism들의 합성이 다시 finitely presented라는 것으로부터 얻어진다. 마지막으로 morphism of finite presentation은 quasi-compact, quasi-separated이면서 locally of finite presentation인 morphism이므로, 앞의 결과들과 종합하면 이 성질 또한 base change에 대해 보존된다.

이제 남은 두 성질을 위해 fiber를 계산하자. $y\in Y$와 그 image $z\in Z$에 대하여, $\mathcal{O}_{Z,z} \rightarrow \mathcal{O}_{Y,y}$가 local homomorphism이므로 $\Spec \kappa(y) \rightarrow Y \rightarrow Z$는 $\Spec\kappa(z) \rightarrow Z$를 통해 인수분해되고, 따라서 위에서와 같이 fiber diagram들을 합성하면 [정의 12](#def12)에 의하여

$$\rho_Y^{-1}(y)=(X\times_ZY)\times_Y\Spec \kappa(y)\cong X\times_Z\Spec \kappa(y)\cong \varphi^{-1}(z)\times_{\Spec \kappa(z)}\Spec \kappa(y)$$

를 얻는다. 또 [보조정리 3](#lem3)에 의하여, $\varphi^{-1}(z)$의 affine open subset $\Spec R$에 대하여 $\Spec (R\otimes_{\kappa(z)}\kappa(y))$는 $\rho_Y^{-1}(y)$의 열린집합이며 이러한 것들이 $\rho_Y^{-1}(y)$를 덮는다.

$\varphi$가 surjective라 하자. 우선 $\varphi^{-1}(z)$가 공집합이 아님을 확인한다. $\varphi(x)=z$인 $x\in X$를 택하고, $x$를 포함하며 $\varphi$에 의해 $\Spec A$ 안으로 들어가는 affine open subset $\Spec B\subseteq X$와 이에 대응되는 ring homomorphism $\phi:A \rightarrow B$를 택하자. $x$와 $z$에 대응되는 prime ideal을 각각 $\mathfrak{q}\subseteq B$, $\mathfrak{p}\subseteq A$라 하면 $\phi^{-1}(\mathfrak{q})=\mathfrak{p}$이고, [보조정리 10](#lem10)과 localization의 성질로부터

$$B\otimes_A\kappa(\mathfrak{p})\cong (B/\mathfrak{p}B)_\mathfrak{p}$$

이므로 $\mathfrak{q}$는 이 ring의 prime ideal을 정의한다. 즉 $\varphi^{-1}(z)\neq\emptyset$이다. 이제 $\varphi^{-1}(z)$의 공집합이 아닌 affine open subset $\Spec R$을 택하면 $R$은 $0$이 아닌 $\kappa(z)$-algebra이고, $\kappa(y)$가 $0$이 아닌 $\kappa(z)$-벡터 space이므로 $R\otimes_{\kappa(z)}\kappa(y)\neq 0$이다. $0$이 아닌 ring은 항상 prime ideal을 가지므로 $\Spec (R\otimes_{\kappa(z)}\kappa(y))\neq\emptyset$이고, 따라서 $\rho_Y^{-1}(y)\neq\emptyset$이다. $y$는 임의였으므로 $\rho_Y$는 surjective이다.

마지막으로 $\varphi$가 quasi-finite라 하자. $\varphi$는 finite type이므로 위에서 본 대로 $\rho_Y$ 또한 finite type이고, 따라서 $\rho_Y$의 fiber들이 모두 유한집합임만 보이면 된다. $\varphi$가 quasi-compact이므로 base change에 대한 quasi-compactness의 보존을 $\Spec \kappa(z) \rightarrow Z$에 적용하면 $\varphi^{-1}(z)$가 quasi-compact임을 알고, 따라서 이를 유한히 많은 affine open subset $\Spec R_1,\ldots, \Spec R_n$으로 덮을 수 있다. 마찬가지로 $\varphi$가 locally of finite type이므로 각각의 $R_l$은 finite type $\kappa(z)$-algebra이며, 가정에 의하여 각각의 $\Spec R_l$은 유한집합이다.

이제 유한히 많은 prime ideal만을 갖는 finite type $\mathbb{K}$-algebra $R$은 항상 유한차원 $\mathbb{K}$-벡터 space임을 보이자. 우선 $R$의 임의의 prime ideal $\mathfrak{p}$가 maximal임을 보인다. 만일 $\mathfrak{p}$를 진부분집합으로 포함하는 prime ideal이 존재한다면 $d=\dim R/\mathfrak{p}\geq 1$이고, [\[가환대수학\] §뇌터 정규화, ⁋정리 1](/ko/math/commutative_algebra/noether_normalization#thm1)에 의하여 $R/\mathfrak{p}$는 polynomial ring $\mathbb{K}[\x_1,\ldots, \x_d]$를 subring으로 가지며 그 위에서 finitely generated module, 특히 integral extension이다. 그런데 $d\geq 1$이므로 $\mathbb{K}[\x_1,\ldots, \x_d]$는 $\mathbb{K}[\x_1]$의 서로 다른 irreducible polynomial들이 생성하는 무한히 많은 prime ideal을 갖고, [\[가환대수학\] §정수적 확장과 아이디얼, ⁋명제 1](/ko/math/commutative_algebra/lying_over_and_going_up#prop1)에 의하여 이들 각각 위에 $R/\mathfrak{p}$의 prime ideal이 놓이므로, $R$이 유한히 많은 prime ideal만을 갖는다는 가정에 모순이다. 따라서 $R$의 모든 prime ideal은 maximal이고, [\[가환대수학\] §기본 개념들, ⁋정리 12](/ko/math/commutative_algebra/basic_notions#thm12)에 의하여 $R$이 Noetherian이므로 [\[가환대수학\] §조르단-횔더 정리, ⁋정리 4](/ko/math/commutative_algebra/Jordan-Holder_theorem#thm4)에 의하여 $R$은 $R$-module로서 유한한 length를 갖는다. 이 때 composition factor들은 모두 $R/\mathfrak{m}$의 꼴인데, field는 Jacobson ring이므로 [\[가환대수학\] §영점정리, ⁋정리 4](/ko/math/commutative_algebra/nullstellensatz#thm4)에 의하여 $R/\mathfrak{m}$은 $\mathbb{K}$의 finite extension이다. 따라서 $R$은 유한차원 $\mathbb{K}$-벡터 space이다.

그럼 각각의 $R_l$은 유한차원 $\kappa(z)$-벡터 space이므로 $R_l\otimes_{\kappa(z)}\kappa(y)$ 또한 유한차원 $\kappa(y)$-벡터 space이고, 따라서 Artinian ring이 되어 위에서와 같은 이유로 유한히 많은 prime ideal만을 갖는다. ([\[가환대수학\] §조르단-횔더 정리, ⁋따름정리 6](/ko/math/commutative_algebra/Jordan-Holder_theorem#cor6)) 이제 $\rho_Y^{-1}(y)$는 유한히 많은 $\Spec (R_l\otimes_{\kappa(z)}\kappa(y))$들로 덮이므로 유한집합이고, 이로써 $\rho_Y$가 quasi-finite임을 안다. 
:::

---

**참고문헌**

**[Har]** R. Hartshorne, *Algebraic geometry*. Graduate texts in mathematics. Springer, 1977.  
**[Vak]** R. Vakil, *The rising sea: Foundation of algebraic geometry*. Available [online](https://math.stanford.edu/~vakil/216blog/).
