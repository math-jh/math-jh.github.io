---

title: "올곱"
excerpt: ""

categories: [Math / Algebraic Geometry]
permalink: /ko/math/algebraic_geometry/fiber_products
header:
    overlay_image: /assets/images/Math/Algebraic_Geometry/Fiber_products.png
    overlay_filter: 0.5
sidebar: 
    nav: "algebraic_geometry-ko"

date: 2024-11-28
last_modified_at: 2024-11-28
weight: 7

---

우리는 [§스킴 사상의 성질들](/ko/math/algebraic_geometry/properties_of_scheme_morphisms)에서 스킴들 사이의 morphism이 가질 수 있는 다양한 성질들을 살펴보았다. 그 중 몇몇 성질을 기하학적으로 설명하기 위해서는 scheme morphism의 fiber의 개념을 정의했어야 했는데, 이는 더 일반적으로 fiber product의 개념을 통해 설명된다. 

## 올곱의 정의

두 scheme morphism $X \rightarrow S$, $Y \rightarrow S$에 대하여, 이들의 fiber product $X\times_SY$는 category $\Sch_{/S}$에서의 product이다. 우리가 $\Sch_{/S}$를 생각하는 이유는 본질적으로는 이것이 Yoneda functor $h^S\in[\Sch^\op,\Set]$의 image이기 때문이므로, 이러한 철학을 바탕으로 $[\Sch^\op,\Set]$을 조금 더 자세히 살펴보자. 

Scheme들의 fiber product를 정의하기 위해 category $[\Sch^\op,\Set]$를 살펴보는 이유 중 하나는 $\Set$의 fiber product로부터 functor category $[\Sch^\op,\Set]$의 fiber product가 주어진다는 것이다. 즉 임의의 $f, g, h\in [\Sch^\op,\Set]$이 주어졌을 때, 다음의 식

$$(f\times_hg)(X)=f(X)\times_{h(X)}g(X)\qquad\text{for all $X\in\Sch$}$$

으로 정의하면 이것이 $[\Sch^\op,\Set]$에서의 fiber product가 된다. 이제 이로부터 $\Sch$에서의 fiber product를 정의할 수 있는데, 두 $S$-scheme들 $X \rightarrow S$, $Y \rightarrow S$에 대하여 이들의 Yoneda functor $h^X, h^Y, h^S$를 생각한 후, 이들 functor들의 fiber product $h^X\times_{h^S}h^Y$를 생각하면 된다. <em_ko>만일</em_ko> 이 functor가 representable이고 scheme $X\times_SY$가 그 representation이라면, 

$$\Hom_\Sch(Z, X\times_SY)\cong h^X\times_{h^S} h^Y=h^X(Z)\times_{h^S(Z)}h^Y(Z)\cong \Hom_\Sch(Z, X)\times_{\Hom_\Sch(Z,S)}\Hom_\Sch(Y,S)$$

을 통해 $X\times_SY$가 이들의 fiber product임을 보일 수 있기 때문이다.

위의 논증을 보면 functor들 $h\in[\Sch^\op, \Set]$을 (일종의) 기하학적 대상으로 생각하고 있는 것을 알 수 있는데, 여기에서 좀 더 나아가 이들 functor들 사이의 기하학을 할 수 있다. 즉, (representable일 필요는 없는) 두 functor들 사이의 morphism $h' \rightarrow h$에 대하여 이들이 갖는 성질을 scheme morphism의 성질로부터 정의할 것이다. 이는 다음과 같은 꼴로 이루어진다.

<div class="definition" markdown="1">

<ins id="def1">**정의 1**</ins> 두 functor $h',h\in[\Sch^\op,\Set]$에 대하여, $h'\rightarrow h$가 (Zariski) *open embedding*이라는 것은 임의의 representable functor $h^X$와 morphism $h^X \rightarrow h$마다 fiber product $h^X\times_hh'\simeq h^U$가 representable이고, 이로부터 얻어지는 morphism $h^U \rightarrow h^X$가 scheme들 사이의 open embedding $U\rightarrow X$로부터 나오는 것이다. 

</div>

이 때, $h'$를 $h$의 open subfunctor라 부른다. 그럼 이들이 open subscheme의 성질들을 그대로 물려받는 것을 확인할 수 있다. 가령 두 open subfunctor의 합성은 open subfunctor가 된다. 

<div class="definition" markdown="1">

<ins id="def2">**정의 2**</ins> Functor $h\in [\Sch^\op,\Set]$의 open subfunctor들 $(h_i)$이 $h$의 (Zariski) *open covering*이라는 것은 임의의 morphism $h^X \rightarrow h$마다, 이들 $h_i$들이 정의하는 $X$의 open subscheme $U_i$들이 $X$의 open covering이 되는 것이다.

</div>

이와 같은 방식으로 category $\Sch$ 위에 위상구조와 비슷한 구조를 정의할 수 있으며 이를 만들 때 Zariski topology를 사용했으므로 이를 *(big) Zariski site*라 부르고 $\Sch_\text{Zar}$와 같이 적는다. 엄밀히 말하자면 Zariski site를 정확하게 정의하기 위해서는 $\Sch$의 fiber product가 존재한다는 것을 먼저 보여야 하지만, 우리에게 중요한 것은 [정의 2](#def2)에서 open covering이 무엇인지 정의하였으므로, 이를 바탕으로 sheaf가 무엇인지를 정의할 수 있다는 것이고 $\Sch_\text{Zar}$이 정의된다는 것 자체는 중요하지 않다.

<div class="definition" markdown="1">

<ins id="def3">**정의 3**</ins> $\Sch$ 위에 정의된 *Zariski sheaf*는 다음 두 조건을 만족하는 presheaf $F:\Sch^\op \rightarrow \Set$을 의미한다. 

1. 임의의 $X\in\Sch$와 $f,g\in F(X)$, 그리고 $X$의 임의의 open covering $h^{U_i} \rightarrow h^X$가 주어졌다 하자. 만일 임의의 $i$마다 $f\vert_{U_i}=g\vert_{U_i}$가 성립한다면 $f=g$이다.
2. 만일 $X$의 임의의 open covering $h^{U_i} \rightarrow h^X$와 $f_i\in F(U_i)$들이 조건 $f_i\vert_{U_i\cap U_j}=f_j\vert_{U_i\cap U_j}$를 만족한다면, $f\vert_{U_i}=f_i$가 항상 성립하도록 하는 $f\in F(X)$가 존재한다.

</div>

물론 scheme $X$와 open embedding $U\rightarrow X$에 대하여, $f\in F(X)$의 restriction $f\vert_U\in F(U)$는 $F(X) \rightarrow F(U)$를 통해 얻어진다. 

그럼 다음이 성립한다.

<div class="proposition" markdown="1">

<ins id="prop4">**명제 4**</ins> Functor $h\in [\Sch^\op,\Set]$이 Zariski sheaf라 하자. 만일 $h$가 representable open subfunctor들로 이루어진 covering을 갖는다면, $h$는 representable이다.

</div>

이는 정의에 의해 거의 자명한데, open subfunctor들을 represent하는 scheme들 $U_i$를 이어붙여 scheme $X$를 만들 수 있고, 이것이 $h$를 represent하는 것을 확인할 수 있기 때문이다. 따라서 fiber product의 존재성은 다음 두 보조정리로부터 나온다. 

<div class="proposition" markdown="1">

<ins id="lem5">**보조정리 5**</ins> 두 $S$-scheme $X \rightarrow S$, $Y \rightarrow S$가 주어졌다 하자. $S$의 affine open covering $(S_i)$에 대하여, $S_i$의 $X$에서의 preimage를 덮는 affine open covering을 $X_{ij}$, $S_i$의 $Y$에서의 preimage를 덮는 affine open covering을 $Y_{ik}$라 하면, functor들

$$h^{X_{ij}}\times_{h^{S_i}}h^{Y_{ik}}$$

이 $h^X\times_{h^S}h^Y$의 open covering이 된다.

</div>

위의 보조정리에 대한 증명 또한 거의 자명하다. 따라서 affine scheme들의 fiber product만 정의하고 나면, 임의의 scheme들의 Yoneda functor들의 fiber product는 [보조정리 5](#lem5)를 사용하여 affine scheme들로 쪼갤 수 있고, 이들은 fiber product를 가지므로 [명제 4](#prop4)를 적용하면 이들 Yoneda functor들의 fiber product가 representable인 것을 확인할 수 있기 때문이다. 

그런데 $\cRing^\op=\AffSch$이고 fiber product의 universal property는 정확히 tensor product의 universal property의 dual이다. 즉,

<div class="proposition" markdown="1">

<ins id="lem6">**보조정리 6**</ins> $\Spec A\times_{\Spec C}\Spec B\cong \Spec (A\times_CB)$.

</div>

이를 정리하면 다음을 얻는다.

<div class="proposition" markdown="1">

<ins id="thm7">**정리 7**</ins> 임의의 scheme $S$와 scheme morphism $X \rightarrow S$, $Y \rightarrow S$에 대하여, 이들의 fiber product $X\times_SY$가 존재한다. 

</div>

지금까지의 과정을 간단하게 요약하자면, 적어도 affine scheme에서는 fiber product가 어떻게 생겨야 하는지 알고 ([정리 7](#thm7)) 따라서 $X, Y, S$들 각각을 affine subscheme들로 분해한 후 [보조정리 5](#lem5)와 같은 방식으로 이들을 이어붙여 하나의 scheme $X\times_SY$를 만들 수 있다는 것이다. 

Fiber product는 임의의 scheme morphism $T \rightarrow S$가 주어졌을 때, 임의의 $S$-scheme $X \rightarrow S$를 $T$-scheme $X\times_ST \rightarrow T$로 바꾸어준다. 이러한 관점에서 $X\times_ST$를 $X \rightarrow S$의 $T$에 의한 *base change*라 부르기도 한다.

## 올곱의 예시들

다음은 올곱의 예시들이다. 

<div class="example" markdown="1">

<ins id="ex8">**예시 8**</ins> 임의의 scheme morphism $f:X \rightarrow Y$와, open embedding $U \rightarrow Y$가 주어졌다 하자. 그럼 fiber product $X\times_YU$는 더 간단한 설명이 있는데, 바로 $f^{-1}(U)$이다. 이는 집합에서의 fiber product가 어떻게 생겼는지를 살펴보면 직관적으로도 자명하고, 엄밀한 증명은 universal property를 사용하면 된다.

</div>

이제 임의의 scheme morphism $f:X \rightarrow Y$가 주어졌다 하고, $Y$의 한 점 $y$를 생각하자. 즉 점 $y$를 다음의 scheme morphism

$$\Spec \kappa(y)\hookrightarrow Y$$

으로 생각할 수 있으며, $\mathscr{O}_Y$로 이를 표현하자면

$$\kappa(y)=\mathscr{O}_{Y,y}/\mathfrak{m}_y$$

이다. 그럼 이제 $y$의 $f$에 의한 fiber는 fiber product

$$X_y=X\times_Y\Spec\kappa (y)$$

로 주는 것이 자연스럽다. 어렵지 않게 이 scheme $X_y$를 위상공간으로 보면 $f^{-1}(y)$와 homeomorphic하다는 것을 보일 수 있다. 

<div class="example" markdown="1">

<ins id="ex9">**예시 9**</ins> 가령 다음의 scheme morphism

$$f:\Spec \frac{\mathbb{k}[\x,\y]}{(\y^2-\x)} \rightarrow \Spec \mathbb{k}[\x]$$

를 살펴보자. $\Spec \mathbb{k}[\x]$의 (closed) point $(\x-x)$는 $x\in \mathbb{k}$에 대응되며, 이 때의 residue field $\kappa(x)$는 $\mathbb{k}$이고 inclusion $\Spec\kappa(x)\hookrightarrow\Spec \mathbb{k}[\x]$는 ring homomorphism 

$$\mathbb{k}[\x]\rightarrow \kappa(x)=\mathbb{k};\qquad \x\mapsto x$$

으로 주어진다.

한편

$$\frac{\mathbb{k}[\x,\y]}{(\y^2-\x)}\cong \mathbb{k}[\y]$$

이며, 그럼 이 isomorphism 상에서 $f$는 ring homomorphism

$$\mathbb{k}[\x]\rightarrow \mathbb{k}[\y];\qquad \x\mapsto \y^2$$

으로 주어진다. 이제 점 $y$의 $f$에 대한 fiber를 생각하면, 이는

$$\Spec \mathbb{k}[\y]\times_{\Spec \mathbb{k}[\x]} \Spec \kappa(y)=\Spec(\mathbb{k}[\y]\otimes_{\mathbb{k}[\x]}\mathbb{k})\cong\Spec(\mathbb{k}[\y]/(\y^2-x))$$

임을 확인할 수 있다. 만일 방정식 $\y^2-x=0$이 $\mathbb{k}$에서 해를 가졌다면 우변은 

$$\Spec \mathbb{k}[\y]/(\y-\sqrt{x})\amalg\Spec \mathbb{k}[\y]/(\y+\sqrt{x})$$

으로 쪼개졌을 것이다. $x=0$인 경우 또한 재미있는데, 이 경우 우변은

$$\Spec \mathbb{k}[\y]/(\y^2)$$

이 되어 non-reduced point가 된다. 이는 포물선 $\y^2-\x$와 직선 $\x=0$이 중근을 갖는다는 것을 보여준다. 

</div>

위의 예시를 통해 scheme morphism $f:X \rightarrow Y$를 더 직관적으로 표현할 수 있는데, 이는 fiber $X_y$들이 각각의 $y\in Y$마다 붙어있는 것으로 생각할 수 있다. 만일 fiber들 $X_y$가 특정한 기하적인 대상이었다면, 가령 $X_y$들이 모두 curve였다면 $f:X \rightarrow Y$는 $Y$로 parametrize된 curve로 생각할 수 있을 것이다. 물론 $X_y$들이 curve라는 것을 정의하기 위해서는 $X_y$의 차원을 먼저 정의하는 것이 순서일 것이다. 

## 올곱에 의해 보존되는 성질들

대부분의 scheme morphism의 성질은 합성에 대해 잘 유지된다. 마찬가지로 대부분의 scheme morphism에 대한 성질은 base change에 대해서도 잘 보존된다.

<div class="proposition" markdown="1">

<ins id="prop8">**명제 8**</ins> 임의의 scheme morphism $T \rightarrow S$가 주어졌다 하고, $S$-scheme $X \rightarrow S$가 주어졌다 하자. 만일 $X \rightarrow S$가 quasi-compact (resp. quasiseparated, affine, finite, integral, locally of finite type, finite type)라면, $X\times_ST \rightarrow T$ 또한 uasicompact (resp. quasiseparated, affine, finite, integral, locally of finite type, finite type)이다.

</div>