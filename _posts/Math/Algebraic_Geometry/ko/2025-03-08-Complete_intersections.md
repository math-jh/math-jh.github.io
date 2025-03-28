---

title: "완전교차"
excerpt: ""

categories: [Math / Algebraic Geometry]
permalink: /ko/math/algebraic_geometry/complete_intersections
header:
    overlay_image: /assets/images/Math/Algebraic_Geometry/Complete_intersections.png
    overlay_filter: 0.5
sidebar: 
    nav: "algebraic_geometry-ko"

date: 2025-03-08
last_modified_at: 2025-03-08
weight: 110

---

차원부터

닫힌 부분스킴의 중요한 예시 중 하나는 [§닫힌 부분스킴, ⁋정의 7](/ko/math/algebraic_geometry/closed_subschemes)에서 정의한 vanishing scheme이며, 이에 대한 motivation은 당연히 유클리드 공간 $\mathbb{R}^n$과 그 위에서 정의되는 함수 $f: \mathbb{R}^n \rightarrow \mathbb{R}$에 대하여 $f^{-1}(0)$으로 정의되는 $\mathbb{R}^n$의 초곡면 $f=0$이다. 

한편 우리는 더 일반적으로 global section들의 (유한한) family $s_1,\ldots, s_k\in \Gamma(X, \mathscr{O}_X)$가 주어졌을 때 이들이 정의하는 vanishing scheme $Z(s_1,\ldots, s_k)$에도 관심이 있다. 직관적으로 이는 우선 $X$에서 global section $s_1$을 사용하여 만든 vanishing scheme $\iota_1:Z(s_1)\hookrightarrow X$을 생각한 후, $Z(s_1)$의 global section 

$$s_2\vert_{Z(s_1)}=\iota^\sharp(X)(s_2)\in(\iota_1)_\ast \mathscr{O}_{Z(s_1)}(X)=\Gamma(Z(s_1), \mathscr{O}_{Z(s_1)})$$

을 통해 $Z(s_1)$에서 $s_2\vert_{Z(s_1)}$의 vanishing scheme을 찾아나가는 것을 반복하여 얻어질 것이며, 물론 이를 위해서는 이 과정이 $s_1, \ldots, s_k$의 순서에 무관하게 같은 scheme을 주어야 할 것이다. 


## Locally principal embedding

<div class="definition" markdown="1">

<ins id="def1">**정의 1**</ins> Closed embedding $\iota: Z \hookrightarrow X$가 *locally principal*이라는 것은 $X$의 적당한 open cover $\\{U\_i\\}$가 존재하여, $\iota$의 공역을 각각의 $U_i$로 제한하여 얻어지는 closed embedding들

$$\iota\vert^{U_i}: \iota^{-1}(U_i) \rightarrow U_i$$

마다 적당한 $s_i\in \Gamma(U_i, \mathscr{O}_X)$가 존재하여 두 closed embedding $\iota\vert^{U_i}$와 $Z(s_i)\hookrightarrow U_i$가 isomorphic한 것이다. 

</div>

그럼 만일 $\iota: Z\hookrightarrow X$가 locally principal이라면, 정의의 $U_i$들 각각을 affine open set들로 덮고 $s_i$들을 이들로 제한시키면 $\\{U_i\\}$들이 affine open covering이라 가정하여도 된다. 

<div class="definition" markdown="1">

<ins id="def2">**정의 2**</ins> Closed embedding $\iota: Z \hookrightarrow X$가 *effective Cartier divisor*라는 것은 $X$의 affine open cover $\\{U_i=\Spec A_i\\}$가 존재하여, 각각의 closed embedding들

$$\iota\vert^{U_i}:\iota^{-1}(U_i) \rightarrow U_i$$

마다 적당한 non-zerodivisor $s_i\in A_i=\Gamma(U_i, \mathscr{O}_X)$가 존재하여 두 closed embedding $\iota^{U_i}$와 $Z(s_i)\hookrightarrow U_i$가 isomorphic한 것이다.

</div>

정의에 의해 locally principal embedding은 대략적으로 ideal sheaf가 (국소적으로는) 하나의 원소로 생성되는 것, 즉 principal ideal인 것이고 effecetive Cartier divisor는 적절한 affine cover를 잡으면 이 하나의 원소가 non-zerodivisor이도록 할 수 있는 것이다. 따라서 임의의 effective Cartier divisor는 locally principal이지만 그 역은 성립하지 않는다.

