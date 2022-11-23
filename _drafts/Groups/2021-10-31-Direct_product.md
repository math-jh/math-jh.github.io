---

title: "Direct product와 direct sum"
excerpt: "Direct product and direct sum of groups"

categories: [Math / Groups]
permalink: /ko/math/groups/direct_product
header:
    overlay_image: /assets/images/Groups/Direct_product.png
    overlay_filter: 0.5
sidebar: 
    nav: "algebraic_structures"

date: 2021-10-31
last_modified_at:
weight: 5

published: false

---
<div class="notice--warning" markdown="1">

이 글은 현재 수정중입니다.

이 글은 예전에 쓴 글로, 서술 방향이 마음에 들지 않거나 표기법이 마음에 들지 않아 전체적으로 수정이 진행중입니다. 읽으실 때 참고해주세요.

</div>


지난 글에서 우리는 특정한 group의 예시들을 살펴봤는데, 이제 우리는 이미 알고 있던 group들로부터 새로운 group을 얻어내는 방법을 살펴본다. 이 때 사용할 도구는 세 가지, direct product, direct sum, 그리고 free product다. 

## Review of set theory

우리가 product set을 정의한 방법은 크게 두 가지다.

우선 explicit하게 집합들의 product를 정의할 수 있었다. ([Set Theory, §집합의 연산, 정의 18](/ko/math/set_theory/set_operations#df18))  다른 방법은 universal property를 이용한 방법이다. 즉, 

> 집합들의 모임 $(S_i)$들에 대하여, 집합 $S$, 그리고 $i$마다 정의된 함수들 $\operatorname{pr}_i:S\rightarrow S_i$가 *product*라는 것은, 또 다른 집합 $R$과 함수들 $f_i:R\rightarrow S_i$들이 주어졌을 때, $f_i=\operatorname{pr}_i\circ f$이도록 하는 유일한 함수 $f$가 존재하는 것이다.

를 만족하는 집합 $S$와, $\operatorname{pr}\_i$들의 pair를 *product set*이라 불렀다. (같은 글의 [정리 20](/ko/math/set_theory/set_operations#thm20)) 마찬가지로 set들의 sum을 정의하는 방법도 두 가지가 있었다. (마찬가지로 같은 글의 [정의 14](/ko/math/set_theory/set_operations#df14)와 [정리 16](/ko/math/set_theory/set_operations#thm16))

Group들 사이에 product와 sum을 정의할 때에도 이와 비슷한 방법을 사용할 것이다.

## Direct product of groups

우선 concrete한 construction을 생각해보자.

Group들의 family $(G_i)\_{i\in I}$가 주어졌고, $\*\_i$들이 각각 $G_i$에서의 연산, $e\_i$들이 각각 $G\_i$에서 ($\*\_i$에 대한) 항등원이라 하자. 집합에서의 경우와 마찬가지로, $G_i$들의 product는 

> $f(i)\in G_i$를 만족하는 함수 $f:I\rightarrow \bigcup G_i$들의 group

으로 정의할 수 있다.[^1] 물론 이 구조에는 아직 어떠한 항등원도, 연산도 없으므로 이를 group이라 부르는 것에는 어폐가 있다. 논의의 편의를 위해, 위에서 정의한 product set을 $G$로 적자. 우리가 해야 할 첫 번째 일은 두 함수 $f,g$ 사이의 연산 $f\*g$를 정의하는 것이다. 이 연산은 우선 $G$에 대해 닫혀있어야 하므로, $f\*g\in G$여야 하고, 따라서 이 함수 $f\*g$는 임의의 $i\in I$에 대해 $(f\*g)(i)\in G_i$를 만족해야 한다. 그리고 이들 함수값 $(f\*g)(i)$은 함수 $f\*g$를 유일하게 결정해주므로, 우리는 $i$를 임의로 고정하고 $(f\*g)(i)$의 값만 결정해주면 된다. 이제 $f(i), g(i)\in G_i$에 대해, $(f\*g)(i)$로 정의할 만한 것은 $f(i)\*_ig(i)$ 뿐이다. 즉,

> 임의의 $f,g\in G$에 대해, $f\*g:I\rightarrow \bigcup G_i$는 임의의 $i\in I$에 대해 $(f\*g)(i)=f(i)\*\_ig(i)$으로 정의된다.

이렇게 정의된 $\*$이 $G$ 위에서 group structure를 이룬다는 것을 보여야 한다.

<div class="proposition" markdown="1">

<ins id="lem1">**보조정리 1**</ins> 위와 같은 상황에서, product set $G$는 $\*$에 대해 group을 이룬다.

</div>
<details class="proof" markdown="1">
<summary>증명</summary>

우선 $\*$가 잘 정의되었고, 그 결과가 $G$의 원소가 된다는 것은 위에서 보였다. 즉 $(f\*g)(i)$는 $I$에서 $\bigcup G_i$로의 함수이며, 각각의 $i$에 대해 $(f\*g)(i)\in G_i$이다. 이제 $\*$이 group의 연산 조건을 모두 만족한다는 것을 보여야 한다.

- $f,g,h\in G$라 하자. 그럼 $(f\*g)\*h$는 임의의 $i\in I$를 $(f\*g)(i)\*_ih(i)$로 보내는 함수이다. 그런데 다시 $f\*g$는 $i$를 $f(i)\*_ig(i)$로 보내는 함수이며, 따라서 임의의 $i\in I$에 대해 $((f\*g)\*h)(i)$의 값은 $(f(i)\*_ig(i))\*_ih(i)$와 같다. 이와 비슷하게 임의의 $i\in I$에 대해 $(f\*(g\*h))(i)$의 값은 $f(i)\*_i(g(i)\*_ih(i))$와 같다는 것을 보일 수 있고, $\*_i$는 group $G_i$의 연산으로써 associative하므로 이 두 값은 같다. $i$는 임의의 원소였으므로, 이는 곧 $(f\*g)\*h=f\*(g\*h)$라는 뜻이고 따라서 $\*$는 associative하다.

- 항등원을 결정해 줘야 한다. 함수 $e:I\rightarrow \bigcup G_i$를 임의의 $i\in I$에 대해 $e(i)=e_i$로 정의된 함수라 하자. 임의의 $f\in G$와 임의의 $i\in I$에 대하여, 

    $$(e*f)(i)=e(i)*_if(i)=e_i*_if(i)=f(i),\quad (f*e)(i)=f(i)*_ie(i)=f(i)*_ie_i=f(i)$$

    이므로 $e$는 $G$에서의 항등원이 된다.
    
- 또, 역원을 결정해줘야 한다. 임의의 $f\in G$에 대하여, 함수 $\bar{f}:I\rightarrow\bigcup G_i$를 $\bar{f}(i)=f(i)^{-1}$으로 정의하자. 즉, 임의의 $i\in I$에 대하여, $\bar{f}(i)$는 $f(i)\in G_i$의 ($G_i$에서의) 역원 $f(i)^{-1}$이다. 어렵지 않게 $\bar{f}$가 실제로 $G$의 원소임을 확인할 수 있으며, 또

    $$(\bar{f}*f)(i)=\bar{f}(i)*_if(i)=f(i)^{-1}*_if(i)=e_i=e(i)$$
    
    그리고 마찬가지로 $(f\*\bar{f})(i)=e(i)$이므로 $\bar{f}$는 $f$의 역원이 된다. 
</details>

각각의 $i\in I$에 대하여, $p_i:G\rightarrow G_i$를 $f\mapsto f(i)$로 정의하자. 즉 $p_i$는 $G$의 원소(순서쌍) $f$를 받아서, $i$에서의 함숫값 ($f$의 $i$번째 좌표)을 내놓는 함수이다. $p_i$들 각각은 그럼 group homomorphism이 되는데, 이는 다음의 계산들

$$(\cdots, x_i,\cdots)+(\cdots, y_i, \cdots)=(\cdots, x_i+y_i, \cdots)$$

그리고

$$p_i(\cdots, x_i,\cdots)=x_i,\qquad p_i(\cdots, y_i,\cdots)=x_i,\qquad p_i(\cdots, x_i+y_i,\cdots)=x_i+y_i$$

에 의해 자명하다.

물론 우리는 universal property를 이용해 product group을 정의할 수도 있다.

<div class="definition" markdown="1">

<ins id="df2">**정의 2**</ins> Group들의 family $(G_i)$가 주어졌다고 하자. 그럼 어떤 group $G$와, group homomorphism들 $\operatorname{pr}_i:G\rightarrow G_i$가 이들 family의 *product*라는 것은, 다음의 universal property

> 임의의 group $H$와 group homomorphism들 $f_i:H\rightarrow G_i$들이 주어졌을 때, $f\_i=\operatorname{pr}\_i\circ f$이도록 하는 유일한 group homomorphism $f:H\rightarrow \prod\_{i\in I} G\_i $가 존재한다.

![universal_property_of_direct_product](/assets/images/Groups/Direct_product-1.png){:width="240px" class="invert" .align-center}

를 만족하는 것이다. 

</div>

이 정의는 우리가 앞서 잠깐 되새겼던 product set의 universal property와 거의 완벽하게 동일하다. 달라진 점은 set이라는 단어가 group으로, 그리고 집합들 사이의 함수가 group들 사이의 homomorphism으로 바뀐 것 뿐이다. 다만 group에는 다양한 종류의 product가 있으므로, 이들과 구별해주기 위해 이를 *direct product*라고 부르기도 한다. 

물론, 집합론 때와 마찬가지로 이 자체만으로는 정의라기보다는 선언에 가깝다. 아직까지는 이러한 성질을 만족하는 group $G$와 homomorphism들이 존재하는지, 존재한다면 유일하게 결정되는지도 확인하지 않았다. 

유일성은 universal property에 의해 얻어지는 formal한 성질이다.

<div class="proposition" markdown="1">

<ins id="pp3">**명제 3**</ins> Group들의 family $(G_i)$에 대하여, 이들 family의 product는 isomorphism에 대해 유일하다.  

</div>
<details class="proof" markdown="1">
<summary>증명</summary>

Universal property를 만족시키는 두 개의 pair $\bigl(G,(\operatorname{pr}\_i)\_{i\in I}\bigr)$, $\bigl(G',(\operatorname{pr}\_i')\_{i\in I}\bigr)$가 주어졌다 하자. 우선, $G$와 $\operatorname{pr}_i$들은 unversal property를 만족하므로, 또 다른 group $G'$와 group homomorphism들 $\operatorname{pr}_i':G'\rightarrow G_i$에 대해, $\operatorname{pr}_i'={\operatorname{pr}_i}\circ p'$이도록 하는 $p':G'\rightarrow G$가 존재한다.  
한편, 이번에는 $G'$의 universal property를 활용하면, 마찬가지로 group $G$와 $\operatorname{pr}_i:G\rightarrow G_i$들에 대해 $\operatorname{pr}_i={\operatorname{pr}_i}'\circ p$이도록 하는 $p:G\rightarrow G'$가 존재한다는 것을 안다.

즉 지금까지 우리는 다음의 두 diagram

![uniqueness_1](/assets/images/Groups/Direct_product-2.png){:width="500px"  class="invert" .align-center}

을 얻었다. 그런데 $p$와 $p'$가 만족하는 식들로부터,  

$${\operatorname{pr}_i}\circ(p'\circ p)=({\operatorname{pr}_i}\circ p')\circ p={\operatorname{pr}_i}'\circ p=\operatorname{pr}_i,\qquad {\operatorname{pr}_i'}\circ(p'\circ p)=({\operatorname{pr}_i}'\circ p')\circ p={\operatorname{pr}_i}\circ p=\operatorname{pr}_i'$$

를 만족한다는 것을 알 수 있다. 그런데 이 식은 $p'\circ p$와 $p\circ p'$ 이전에, identity homomorphism $\operatorname{id}\_G$와 $\operatorname{id}\_{G'}$가 만족하는 식이다. 

![uniqueness_2](/assets/images/Groups/Direct_product-3.png){:width="500px" class="invert" .align-center}

따라서 universal property의 *유일한 group homomorphism* 조건에 의하여, 이들은 사실 각각 같은 homomorphism이어야 한다. 즉, $p'\circ p=\operatorname{id}\_G$이고 $p\circ p'=\operatorname{id}\_{G'}$이다. 따라서 $p$와 $p'$는 서로를 inverse로 갖는 isomorphism들이고, $G$와 $G'$ 또한 isomorphic하다.
</details>

이러한 universal property를 만족하는 pair가 실제로 존재함을 보여야 한다. 이를 위해서는 앞서 정의한 direct product가 universal property를 만족함을 보이면 충분하다.

<div class="proposition" markdown="1">

<ins id="pp4">**명제 4**</ins> [보조정리 1](#lem1)의 group $G$와, group homomorphism들의 family $(p_i)$가 universal property를 만족한다.

</div>
<details class="proof" markdown="1">
<summary>증명</summary>

[Set Theory, §집합의 연산, 정리 20](/ko/math/set_theory/set_operations#thm20)의 universal property와 완벽하게 동일하다. 하지만 product set으로서 얻어지는 $f:H\rightarrow G$는 함수라는 것만 보장되므로 $f$가 사실은 group homomorphism이라는 것은 별도로 보여야 한다. 

이는 단순 계산으로부터 자명하다. $f$는 다음의 식

$$x\mapsto (f_i(x))_{i\in I}$$

으로 정의되는 함수였는데, 그럼

$$f(xy)=(f_i(xy))_{i\in I}=(f_i(x)*_if_i(y))_{i\in I}=(f_i(x))_{i\in I}*(f_i(y))_{i\in I}=f(x)*f(y)$$

이므로 $f$는 group homomorphism이다.

</details>

Direct product의 대부분의 성질들은 universal property만을 이용해서 유도해낼 수 있다. 우선 유용한 보조정리를 하나 증명하자.

<div class="proposition" markdown="1">

<ins id="lem5">**보조정리 5**</ins> Product group $\prod_{i\in I}G_i$에 대하여, $x\in \prod_{i\in I}G_i$가 identity element인 것은 모든 $i\in I$에 대하여 $\operatorname{pr}_ix=e_i$인 것과 동치이다.

</div>

앞서 explicit하게 만들었던 product group에서 이 보조정리는 당연한 말이지만, 우리는 universal property에 의해 얻어지는 (unique up to isomorphism인) group을 product group이라 정의하고 있으므로 추가적인 증명이 필요하다.  

<details class="proof--alone" markdown="1">
<summary>보조정리 5의 증명</summary>

우선, 만일 $x$가 항등원이라면 group homomorphism들 $\operatorname{pr}_i$들은 항등원을 항등원으로 보내므로 $\operatorname{pr}_ix=e_i$가 되어야 한다는 것은 자명하다.

반대 방향을 보이자. Trivial group $\\{e\\}$을 생각하고, 각각의 함수들 $\iota_i:\\{e\\}\rightarrow G_i$를 $e\mapsto e_i$로 정의하자. Group이기 이전에, 집합으로서 $\prod G_i$는 product set이므로 Set Theory, §집합의 연산, 정리 20 직후의 [remark](/ko/math/set_theory/set_operations#rmk2)가 그대로 적용이 된다. 

![projection_determines_element](/assets/images/Groups/Direct_product-4.png){:width="250px" class="invert" .align-center}

즉 $\operatorname{pr}_ix=e_i$를 모든 $i$에 대해 만족하는 원소 $x=\iota(e)$는 유일하다. 물론 $\iota$는 group homomorphism이므로 항등원을 항등원으로 보내고, 따라서 $x$는 $\prod G_i$의 항등원이 되어야 한다. 

</details>

<div class="proposition" markdown="1">

<ins id="pp6">**명제 6**</ins> $(G_i)$, $(H_i)$가 동일한 집합 $I$를 index set으로 갖는 group들의 family이고, 각각의 $i$마다 group homomorphism $f_i:G_i\rightarrow H_i$가 주어졌다 하자. 그럼 유일한 group homomorphism $f:\prod G_i\rightarrow\prod H_i$가 존재하여, 모든 $i\in I$마다 $\operatorname{pr}_i\circ f=f_i\circ\operatorname{pr}_i$가 성립[^2]하도록 할 수 있다. 특히, 이 때 $\ker f=\prod\ker f_i$이고, $\operatorname{im}f=\prod\operatorname{im}f_i$이다.
    
</div>
<details class="proof" markdown="1">
<summary>증명</summary>

$f$를 만들기 위해서는 group homomorphism들 $f_i\circ\operatorname{pr}_i$에 $H$의 universal property를 적용하면 된다.

![mapping_induced_to_product](/assets/images/Groups/Direct_product-5.png){:width="240px" class="invert" .align-center}

이 때, 

$$x\in\ker f\iff f(x)=e\iff \forall i(\operatorname{pr}_i(f(x))=e_i)\iff \forall i((f_i\circ{\operatorname{pr}_i})(x)=e_i)\iff \forall i({\operatorname{pr}_i}(x)\in\ker f_i)$$

이므로 $\ker f=\prod\ker f_i$가 성립한다.

이와 유사하게, $y\in\prod H_i$에 대해 $y\in\operatorname{im}f$인 것은 $y=f(x)$인 $x\in H_i$가 존재하는 것과 동치이고, 이러한 $x$에 대하여

$$\operatorname{pr}_i(y)=\operatorname{pr}_i(f(x))=f_i(\operatorname{pr}_i(x))\in\operatorname{im}f_i$$

이므로 $\operatorname{im}f=\prod\operatorname{im} f_i$ 또한 성립한다.

</details>

<div class="proposition" markdown="1">

<ins id="crl7">**따름정리 7**</ins> Group들의 family $(G\_i)\_{i\in I}$가 주어졌다 하자. 각각의 $i\in I$에 대하여 $H_i\trianglelefteq G_i$라면, $\prod H_i$도 $\prod G_i$의 normal subgroup이고 그 quotient group은 $\prod (G_i/H_i)$와 같다.

</div>
<details class="proof" markdown="1">
<summary>증명</summary>

이번에는 canonical homomorphism들 $p_i:G_i\rightarrow G_i/H_i$들에 [명제 6](#pp6)를 적용하면 된다.

![product_of_normal_subgroups](/assets/images/Groups/Direct_product-6.png){:width="280px" class="invert" .align-center}

$p_i\circ\operatorname{pr}_i$들 각각은 surjective homomorphism들의 합성이므로 surjective하고 따라서 $\operatorname{im}p$는 $\prod(G_i/H_i)$와 같다. 또, 이들 각각의 kernel은 (partial product로써) $H_i$와 같다. 따라서 first isomorphism theorem에 의하여

$$\biggl(\prod_{i\in I} G_i\biggr)\bigg/\biggl(\prod_{i\in I}H_i\biggr)\cong\prod_{i\in I} (G_i/H_i)$$

가 성립한다.

</details>

물론, $H_i$들이 $G_i$들의 normal이 아닌 subgroup이더라도 $\prod H_i$는 $\prod G_i$의 subgroup이 된다.

<div class="proposition" markdown="1">

<ins id="crl8">**따름정리 8**</ins> Group들의 family $(G\_i)\_{i\in I}$가 주어졌다 하자. 만일 각각의 $i\in I$에 대하여 $H_i\leq G_i$라면, $\prod H_i$는 $\prod G_i$의 subgroup이다.

</div>
<details class="proof" markdown="1">
<summary>증명</summary>

Inclusion homomorphism들 $\iota_i:H_i\hookrightarrow G_i$에 앞선 명제를 적용하면, $\prod H_i$는 정확히 $\iota$의 image이고 따라서 $\prod G_i$의 subgroup이다.

![product_of_subgroups](/assets/images/Groups/Direct_product-7.png){:width="240px" class="invert" .align-center}

</details>

## Partial products 

위의 따름정리들은 다음의 상황에서 특히 유용하다. 

$(G\_i)\_{i\in I}$가 group들의 family라 하고, $I$의 부분집합 $J$를 생각하자. 그럼 product $\prod_{j\in J}G_j$가 잘 정의된다. 혼동을 피하기 위해, $\prod_{i\in I}G_i$들에 대한 projection map들을 $\operatorname{pr}\_i$들로 적고, $\prod\_{j\in J}G\_j$들에 대한 projection map들은 $\operatorname{pr}\_j^J$와 같이 적자. 

Group homomorphism들 $\iota^J_i:\prod_{j\in J}G_j\rightarrow G_i$를 다음의 식

$$\iota^J_i(x)=\begin{cases}\operatorname{pr}_i^J(x)&\text{$i\in J$}\\e_i&\text{otherwise}\end{cases}$$

으로 정의하면, 다시 $\iota^J:\prod_{j\in J}G_j\rightarrow\prod_{i\in I} G_i$가 존재하여 다음의 diagram을 commute하게 할 수 있다.

![partial_product](/assets/images/Groups/Direct_product-8.png){:width="240px" class="invert" .align-center}

이 때 $\iota^J$의 kernel과 image를 살펴보자.

우선 $x\in\ker\iota^J$라 하자. 그럼 $\iota^J(x)$는 $\prod_{i\in I}G_i$의 항등원이고, 따라서 다음의 식

$$\operatorname{pr}_i\bigl(\iota^J(x)\bigr)=e_i$$

이 모든 $i\in I$에 대해 성립한다. 그런데 ${\operatorname{pr}_i}\circ\iota^J=\iota_i^J$이므로, 위 식은

$$\iota_i^J(x)=e_i$$

와 같고, 특히 $j\in J$인 경우에만 한정하여 보면 이 식은

$$\operatorname{pr}_j^J(x)=e_j$$

와 같다. 따라서 [보조정리 5](#lem5)에 의하여 $x$는 $\prod_{j\in J}G_j$의 항등원이어야만 하고, $\iota^J$는 injective이다.

한편, $x\in\prod_{i\in I} G_i$라 하자. 만일 $\operatorname{pr}_ix\neq e_i$가 $i\in I\setminus J$에 대해 성립한다면, 위의 diagram의 commutativity로부터 $x\not\in\operatorname{im}\iota^J$인 것을 알 수 있다. 따라서, $G_i$들의 subgroup들의 family $(H_i)$를 다음의 식

$$H_i=\begin{cases} G_i&i\in J\\ \{e\}&i\in I\setminus J\end{cases}$$

으로 정의한다면, 

$$\operatorname{im}\iota^J\subset\prod_{i\in I}H_i$$

가 성립한다. 어렵지 않게 위의 포함관계가 사실은 $=$인 것을 알 수 있다. $x\in\prod H_i$라 하자. 그럼 $\operatorname{pr}\_ix=e_i$가 임의의 $i\in I\setminus J$에 대해 성립한다. 우선 다음의 diagram

![partial_product_surjection](/assets/images/Groups/Direct_product-9.png){:width="250px" class="invert" .align-center}

을 통해 $p:\prod_{i\in I}G_i\rightarrow\prod_{j\in J}G_j$를 얻자. 이 때 $p$는 *모든 $j\in J$에 대하여*

$${\operatorname{pr}_j^J}\circ p=\operatorname{pr}_j$$

를 만족하는 group homomorphism이다. 이제 $p(x)\in \prod_{j\in J}G_j$이다. 한편, $\iota^J(p(x))$의 값을 생각해보면 $\operatorname{im}\iota^J\subset\prod H_i$로부터 $\operatorname{pr}_i(\iota^J(p(x)))=e_i$가 임의의 $i\in I\setminus J$에 대해 성립하는 것을 알 수 있고, $j\in J$에 대해서는

$$\operatorname{pr}_j\bigl(\iota^J(p(x))\bigr)=\iota_j^J(p(x))=\operatorname{pr}_j^J(p(x))=\operatorname{pr}_jx$$

임을 알 수 있다. 다시 [보조정리 5](#lem5)에 의하여, 이 식들은 $\iota^J(p(x))$의 값을 유일하게 정의한다. 그런데 마찬가지 식들이 $x$에 대해서도 성립하므로, $\iota^J(p(x))=x$이고 따라서 $x\in\operatorname{im}\iota^J$이 성립한다.

그러므로, 위에서 정의한 $(H_i)$들에 대해

$$\prod_{j\in J}G_j\cong\operatorname{im}\iota^J=\prod_{i\in I}H_i$$

가 성립한다. 즉 $\prod_{j\in J}G_j$를 canonical하게 $\prod_{i\in I}G_i$의 subgroup으로 취급할 수 있고, 우리는 이를 *partial product*라 부른다. 

그런데 $H_i$들은 모두 $G_i$들의 *normal* subgroup이기도 하므로, partial product는 항상 $\prod G_i$의 normal subgroup이 된다. 이 때, $\prod\_{i\in I}H_i$에 의한 quotient는 [따름정리 7](#crl7)에 의하여

$$\biggl(\prod_{i\in I} G_i\biggr)\bigg/\biggl(\prod_{i\in I}H_i\biggr)\cong\prod_{i\in I} (G_i/H_i)\tag{1}$$

라고 쓸 수 있다. 이 때, 

$$G_i/H_i=\begin{cases} \{e\}&i\in J\\ G_i&i\in I\setminus J\end{cases}$$

이므로 우변의 식은 $\prod_{i\in I\setminus J} G_i$로도 볼 수 있고, 그럼 식 (1)은 약간의 abuse of notation을 통해

$$\biggl(\prod_{i\in I} G_i\biggr)\bigg/\biggl(\prod_{j\in J}G_j\biggr)\cong\prod_{i\in I\setminus J} G_i$$

와 같이 쓸 수도 있다.

특히 $J=\\{i\\}$인 경우, 우리는 다음의 commutative diagram

![inclusion_map_in_product](/assets/images/Groups/Direct_product-10.png){:width="240px" class="invert" .align-center}

을 얻고, 이 때 $\iota^i$는 injection이다. 이 때 $\iota^i$들을 $G_i$의 *canonical inclusion*이라 부른다.

$\iota^i(G_i)$들의 원소는 모두 $\operatorname{pr}_j$에 의해 $e_j$로 옮겨지므로 $\iota^i(G_i)$와 $\iota^j(G_j)$는 $\prod G_i$의 항등원 $e=\iota^i(e_i)=\iota^j(e_j)$를 제외하면 교집합이 없다. 뿐만 아니라, 만일 $x\in G_i$이고 $y\in G_j$라면 $\iota^i(x)\iota^j(y)=\iota^j(y)\iota^i(x)$임을 확인할 수 있다. 이는 임의의 $i\in I$에 대해 $\operatorname{pr}_i(xy)$의 값과 $\operatorname{pr}_i(yx)$의 값이 같기 때문이다.

이번 절에서는 inclusion map이나 partial product 등의 개념을 완벽하게 universal property만을 이용해 설명했고, 앞으로 이야기할 내용들도 모두 이와 같은 방법으로, 즉 특정한 construction에 의존하지 않도록 논리를 전개해나갈 수 있다. 하지만 $\prod_{i\in I} G_i$가 concrete하게 주어졌었다면, 가령 inclusion map을 

$$x_j\mapsto (\cdots, e_i, x_j, e_k, \cdots )$$

등과 같이 직관적으로 정의할 수 있었음도 부정하기는 어렵다. 따라서 남은 부분들에서는 universal property를 이용한 argument들과 concrete한 construction을 바탕으로 한 argument를 적절히 섞어서 사용한다. 하지만 언제라도 이 concrete construction은 모두 universal property만을 이용한 argument들로 바꾸어 쓸 수 있다.

## Restricted sum

Group들의 family $(G_i)$와, 이들의 product가 주어졌다 하자. 그럼 $G_i$들 각각은 $\iota^i$를 통해 $\prod G_i$의 subgroup으로 볼 수 있다. 자연스럽게 다음의 식

$$\prod_{i\in I} G_i=\left\langle\bigcup \iota^i(G_i)\right\rangle$$

이 성립하는지를 생각할 수 있다. 이 식은 $I$가 무한집합이라면 거의 대부분 성립하지 않는다. 가장 간단한 예시로, $I=\mathbb{N}$이라 잡고 $G_i=\mathbb{Z}/2\mathbb{Z}=\\{\bar{0}, \bar{1}\\}이$라 하자. 그럼, 예를 들어 좌변은 원소

$$(\bar{1},\bar{1},\cdots)$$

를 포함하지만, 우변은 $\iota^i(\bar{1})$들의 *유한한* 연산을 통해 얻어지는 원소만을 포함하므로 위의 원소를 포함할 수 없다.

<div class="definition" markdown="1">

<ins id="df9">**정의 9**</ins> Group들의 family $(G_i)$에 대하여, $\operatorname{pr}\_i x=e\_i$가 유한개를 제외한 모든 $i$에 대해 성립하는 $x$들로 이루어진 subgroup을 $G\_i$들의 *weak direct product*라 부르고,

$${\prod_{i\in I}}^w G_i$$

으로 표기한다.

더 일반적으로, $G_i$들의 subgroup $H_i$들에 대하여 $\operatorname{pr}\_ix\in H\_i$가 유한개를 제외한 모든 $i$에 대해 성립하는 $x$들로 이루어진 subgroup을 $H_i$에 대한 $G_i$들의 *restricted sum*이라 부르고 $\coprod G_i$라 표현한다.

</div>

$\coprod G_i$는 그렇게까지 나쁜 표기법은 아니지만 별로 좋은 표기법도 아니다. 다행히도 이 표기법은 이번 절이 끝나면 사용할 일은 없을 것이다. 

정의에 의해 weak direct product는 위에서 언급했던 subgroup과 동일하다. 즉

$$\left\langle\bigcup \iota^i(G_i)\right\rangle={\prod_{i\in I}}^w G_i$$

이 성립한다. 또, 만일 $I$가 유한집합이라면 weak direct product는 보통의 direct product와 동일하다.

그럼 $\prod^wG_i$는 다음과 같은 universal property를 갖는다.

<div class="proposition" markdown="1">

<ins id="thm10">**정리 10**</ins> Group들의 family $(G_i)$와 이들의 weak direct product $\prod^w G_i$가 주어졌다 하자. 또 다른 group $H$에 대하여, group homomorphism들 $f_i:G_i\rightarrow H$가 다음의 조건

> 임의의 $i\neq j$에 대하여 $x\in G_i$이고 $y\in G_j$라면, $f_i(x)f_j(y)=f_j(y)f_i(x)$
 
을 만족한다면, 유일한 group homomorphism $f:\prod^w G_i\rightarrow H$가 존재하여 $f_i=f\circ\iota^i$가 임의의 $i$에 대해 성립한다. 

</div>
<details class="proof" markdown="1">
<summary>증명</summary>

우선 유일성부터 보이자. 만일 $f, f'$가 위의 식을 만족한다면, 이들은 $\bigcup\iota^i(G_i)$에서 같은 값을 가져야 하므로 $\prod^w G_i$에서도 같은 값을 가져야 하고 따라서 $f=f'$여야 한다.

이제 $f$의 존재성을 보여야 한다. 임의의 $x\in \prod^w G_i$에 대하여, $f(x)$를 다음의 식

$$f(x)=\prod_{i\in I} f_i(\operatorname{pr}_ix)$$

으로 정의하자. 이 때 $\prod$는 일반적인 원소들의 곱을 의미한다. $x$는 $\prod^w G_i$의 원소이므로, 우번의 $f_i(\operatorname{pr}_ix)$는 유한개의 $i$를 제외하면 모두 항등원이고, 따라서 이 곱은 잘 정의된다. 

식 $f_i=f\circ\iota^i$가 성립하는 것은 자명하고, $f$가 group homomorphism인 것은 임의의 $x,y\in\prod^wG_i$에 대해

$$f(xy)=\prod_{i\in I}f_i(\operatorname{pr}_i(xy))=\prod_{i\in I}f_i(\operatorname{pr}_ix)f_i(\operatorname{pr}_iy)$$

가 성립하므로, $\operatorname{pr}_i(xy)$가 $e_i$가 아니도록 하는 유한개의 값만 골라 이 index들을 $1,\ldots, n$이라 하면

$$f_1(\operatorname{pr}_1x)f_1(\operatorname{pr}_1y)f_2(\operatorname{pr}_2x)f_2(\operatorname{pr}_2y)\cdots f_n(\operatorname{pr}_nx)f_n(\operatorname{pr}_ny)$$

가 되고, 이 때 $f_i(\operatorname{pr}_ix)$와 $f_j(\operatorname{pr}_jy)$는 $i\neq j$라면 항상 commute하므로 이 식을

$$f_1(\operatorname{pr}_1x)f_2(\operatorname{pr}_2x)\cdots f_n(\operatorname{pr}_nx)f_1(\operatorname{pr}_1y)f_2(\operatorname{pr}_2y)\cdots f_n(\operatorname{pr}_ny)$$

으로 바꾸어 쓸 수 있다. 따라서 $f(xy)=f(x)f(y)$이고 $f$는 group homomorphism이 된다. $f_i=f\circ\iota^i$인 것은 자명하다.

</details>

$f_i$들에 걸려있는 조건

> 임의의 $i\neq j$에 대하여 $x\in G_i$이고 $y\in G_j$라면, $f_i(x)f_j(y)=f_j(y)f_i(x)$

은 필연적으로 나와야 할 조건인데, 이 조건들이 정확히 $\iota^i$들이 만족하는 조건이기 때문이다.

Direct sum의 universal property를 이용하면 direct product때와 유사한 몇몇 성질들을 보일 수 있다. 예컨대 다음이 성립한다.

<div class="proposition" markdown="1">

<ins id="pp11">**명제 11**</ins> $G_i$들이 group이고, $H_i$들이 $G_i$들의 normal subgroup이라 하면 $\prod^w H_i$들 또한 $\prod^w G_i$들의 normal subgroup이고 그 quotient group은 $\prod^w (G_i/H_i)$와 같다.

</div>

Weak direct product의 universal property에 대해서는 조금 더 할 말이 있지만, 이는 다음 절로 미뤄두고 우선 다음을 정의하자.

<div class="definition" markdown="1">

<ins id="df12">**정의 12**</ins> $G$가 group이고, $(H_i)$들이 $G$의 subgroup들의 family라 하자. 만일 $i\neq j$일 때마다 $H_i$의 원소들이 $H_j$의 원소들과 commute한다면, inclusion homomorphism들 $\iota_i:H_i\rightarrow G$에 의해 유도되는 $\prod^w H_i$에서 $G$로의 homomorphism $\iota$가 존재한다. 만일 $\iota$가 isomorphism이라면 $G$가 $H_i$들의 *internal weak direct product*라고 부른다. 

</div>

[정리 10](#thm10)에서 만들어낸 homomorphism $f$의 모양을 생각하면, $G$가 $H_i$들의 internal weak direct product인 것은 임의의 $x\in G$가 $y_i\in H_i$를 만족하는 finitely supported family $(y\_i)\_{i\in I}$들의 곱 $\prod y_i$로 나타날 수 있다는 것과 동치임을 확인할 수 있다. 

만일 subgroup들 $H_i$가 모두 $G$의 normal subgroup이라면, 추가적으로 다음의 조건이 갖춰지면 $G$가 $H_i$들의 internal weak direct product가 된다.

<div class="proposition" markdown="1">

<ins id="pp13">**명제 13**</ins> Group $G$의 normal subgroup들 $(H_i)$가 다음의 두 조건

1. $G=\bigl\langle\bigcup_{i\in I} H_i\bigr\rangle$,
2. $H_k\cap \bigl\langle\bigcup_{i\neq k} H_i\bigr\rangle=\\{e\\}$

을 만족한다면 $G$가 $H_i$들의 internal weak direct product이다.

</div>
<details class="proof" markdown="1">
<summary>증명</summary>

우선 2번 조건은 특히 $H_i\cap H_j=\\{e\\}$가 모든 pair $i\neq j$에 대해 성립한다는 것을 보여주므로, [§Subgroups and quotient groups, 명제 16](/ko/math/groups/subgroups#pp16)의 마지막 결과

> 만일 $N$, $K$가 group $G$의 normal subgroup이고 $N\cap K=\\{e\\}$라면 임의의 $n\in N$, $k\in K$에 대해 $nk=kn$이 성립한다.

에 의하여 $H_i$의 임의의 원소와 $H_j$의 임의의 원소가 commute하고, 따라서 inclusion homomorphism $\iota_i$들이 [정의 11](#df11)에서와 같이 $\iota$를 잘 유도한다.

$G$가 $H_i$들의 internal weak direct product임을 보이기 위해서는 이렇게 유도된 $\iota$가 isomorphism인 것을 보여야 한다. 우선 1번 조건에 의해, 임의의 $a\in G$는 $\bigcup H_i$들의 *finite*한 operation들을 통해 얻어진다. 또 $H_i$들이 서로 commute하므로, $a$를 

$$a=\prod_{i\in I} h_i=\prod_{i\in I}\iota^i(h_i),\qquad\text{$\operatorname{supp}(h_i)$ finite and $h_i\in H_i$}$$

로 적을 수 있다. $h=\prod_{i\in I} \iota^i(h_i)\in\prod^w H_i$라 하면, 

$$a=\prod_{i\in I}\iota^i(h_i)=\iota^i\left(\prod_{i\in I}h_i\right)=\iota^i(h)$$

이므로 $\iota$는 surjective이다.

이제 $\iota(a)=e$라 하자. 그럼 각 항들이 $H_i$에 속하는 finitely supported family $(a_i)$에 대하여 $a=(a_i)_{i\in I}$로 쓸 수 있다. 다음의 식  

$$\iota(a)=\prod_{i\in I}\iota^i(a_i)=\prod_{i\in I} a_i=e$$
  
으로부터, 만일 $\operatorname{supp}(a_i)$가 하나 이상의 원소를 갖고, $i\in\operatorname{supp}(a_i)$라 하면

$$a_i^{-1}=\prod_{j\in I\setminus\{i\}}a_j\in H_i\cap \left\langle\bigcup_{j\neq i} H_i\right\rangle=\{e\}$$

가 되어 $i\in\operatorname{supp}(a_i)$라는 가정에 모순이다. 따라서 $\operatorname{supp}(a_i)$는 공집합이고 $a$는 항등원이다. 

</details>


## Direct sum of abelian groups

[정의 10](#thm10)에서 보인 weak direct product의 universal property는 특히 group $H$가 abelian group일 경우 잘 적용된다. 따라서 다음이 성립한다.

<div class="proposition" markdown="1">

<ins id="thm14">**정리 14**</ins> Abelian group들의 family $(G_i)$가 주어졌다 하고, $\prod^w G_i$와 inclusion map들 $\iota^i$를 생각하자. 그럼 임의의 abelian group $H$와 group homomorphism들 $f_i:G_i\rightarrow H$에 대하여, $f_i=f\circ\iota^i$이도록 하는 유일한 group homomorphism $f:\prod^wG_i\rightarrow H$가 존재한다.

</div>

따라서, 적어도 abelian group들 사이에서는 weak direct product $\prod^w G_i$가 product $\prod G_i$의 dual notion이 된다. 때문에 abelian인 경우는 다음과 같이 별도로 이름을 붙여준다. $\iota^i$의 경우 지금까지는 direct product때 정해준 그대로 index를 위첨자로 표기했었는데, 이제 이 정의를 기점으로 하여 $\iota^i$ 또한 독립적으로 사용되는 homomorphism이므로 index를 아래첨자에 적기로 하자.

<div class="definition" markdown="1">

<ins id="df15">**정의 15**</ins> Abelian group들의 family $(G_i)$와, 이들의 weak direct product $\prod^w G_i$, 그리고 inclusion map들 $\iota^i$가 주어졌다 하자. 그럼 $\prod^w G_i$와 $\iota^i$들을 묶어 $G_i$들의 *direct sum*이라 부르고 이를 $\sum G_i$와 $\iota_i$들로 표현한다.  

</div>





## Free groups and free products

그러나 abelian group에서와는 다르게, weak direct product는 일반적인 group에서 universal property를 만족하지 않는다.

<div class="example" markdown="1">

<ins id="ex16">**예시 16**</ins> 임의의 nonabelian group $G$를 생각하고, $a,b\in G$에 대해 $ab\neq ba$가 성립한다 하자. Group homomorphism $f_1, f_2: (\mathbb{Z},+)\rightarrow (G,\cdot)$을

$$f_1(1)=a, \qquad f_2(1)=b$$

을 통해 정의하면, 우리는 다음의 diagram

![counterexample](/assets/images/Groups/Direct_product-11.png){:width="240px" class="invert" .align-center}

을 commute하게 만드는 $f:\mathbb{Z}\times\mathbb{Z}$는 존재하지 않음을 알 수 있다. 만일 그러한 $f$가 존재한다면 

$$\begin{aligned}ab&=f_1(1)f_2(1)=f(\iota_1(1))f(\iota_2(1))=f(\iota_1(1)+\iota_2(1))\\
&=f(\iota_2(1)+\iota_1(1))=f(\iota_2(1))f(\iota_1(1))=f_2(1)f_1(1)\\
&=ba\end{aligned}$$

가 되어 $a,b$의 선택에 모순이기 때문이다.

</div>

그러므로 일반적인 group들 사이에서 direct sum과 같이, universal property를 만족하는 대상을 찾는 것이 중요한 문제가 된다. 

우선 다음 정의를 먼저 살펴보자.

<div class="definition" markdown="1">

<ins id="df17">**정의 17**</ins> 공집합이 아닌 집합 $X$에 대하여, $X$에 의해 정의된 *free group*은 다음과 같은 universal mapping problem의 solution $(F,\iota)$으로 정해진다.

> 임의의 group $G$에 대하여, 만일 어떤 함수 $f:X\rightarrow G$가 주어졌다면 유일한 group homomorphism $\bar{f}:F\rightarrow G$가 존재하여 $\bar{f}\circ\iota=f$를 만족한다.

</div>

위의 정의를 만족하는 pair들은 모두 unique up to bijection임이 분명하다. 문제는 이러한 pair가 적어도 하나는 존재한다는 것을 보이는 부분이다.

대략적인 흐름을 소개한다. 우선 $X$와 disjoint하며 같은 cardinality를 갖는 집합 $X^{-1}$을 생각하자. $X^{-1}$은 어떤 특별한 집합이 될 이유는 없지만, 우리는 bijection $X\rightarrow X^{-1}$ 하나를 골라 $x\in X$의 $X^{-1}$에서의 image를 $x^{-1}$으로 표기할 것이다. 또, $X\cup X^{-1}$과 disjoint한 singleton을 하나 골라 이 집합의 원소를 $e$라 하자. 

그럼 group $F$의 원소는 집합 $X\cup X^{-1}\cup \\{e\\}$에 의해 정의되는 *reduced word*들의 모임이다. 여기서 *word*라는 것은 그저 집합 $X\cup X^{-1}\cup \\{e\\}$의 원소들의 나열이다. 만일 같은 원소가 $xx$와 같이 두 번 연달아 나열되거나, $xx^{-1}$과 같이 $x$ 직후에 $x^{-1}$이 나열되거나, $xey$와 같이 두 개의 term 사이에 $e$가 있을 경우 이들을 각각 $x^2$, $e$, $xy$으로 줄여 쓸 수 있다. 하지만, 예를 들어 $y\neq x^{-1}$이라면 $xyx$를 줄여 쓸 방법은 없다. 이렇게 줄여 쓴 word를 *reduced word*라 부른다. 

우리는 모든 word를 reduced word로 줄여 쓸 수 있다. Word들 사이의 연산을 정의해주기 위해 reduced word를 꼭 도입해줘야 하는 것은 아니지만 표현상의 uniqueness를 적용해주기 위해 필요하다. 어쨌든 이들 사이의 연산과 항등원을 정의해야 한다. 항등원은 당연히 reduced word $e$이다. 연산은 그냥 두 개의 word를 이어쓰는 것으로 정의된다. 예를 들어 word $x_1x_2$와 $x_3x_4$의 연산은 $x_1x_2x_3x_4$로 주어진다. 그럼 $e$는 이 연산 하에서의 *empty word*로 볼 수도 있다. 물론 두 reduced word를 이어붙여 만들어진 word가 reduced일 필요는 없지만, 다시 위의 규칙을 적용하여 reduced word로 만들 수 있다. 이 연산은 자명하게 associative하다. 역원은 원래 주어진 원소의 각 term들에 inverse를 취한 후, 이를 거꾸로 나열한 것이다. 예를 들어 다음의 word

$$x_1x_2^{-1}x_3^2$$

의 역원은

$$x_3^{-2}x_2x_1^{-1}$$

이 되며, 실제로 이들 둘을 연산해보면 $e$가 됨을 확인할 수 있다. 

이제 우리는 group $F$를 만들었으며, 여기서 $X$의 원소로 이루어진 길이 1짜리 원소들을 $X$의 원소와 동일시하면 $\iota:X\rightarrow F$ 또한 얻는다. 그럼 이들이 [정의 17](#df17)의 universal property를 만족한다는 것을 쉽게 보일 수 있다. 이를 위해서는 $\bar{f}$를 $F$에 등장하는 원소들 $x\in X$들을 모두 $g(x)$로 바꿔주는 함수로 정의한 후, 이것이 group homomorphism이 된다는 것을 확인하면 된다.

<div class="proposition" markdown="1">

<ins id="crl18">**따름정리 18**</ins> 임의의 group $G$는 free group의 homomorphic image이다.

</div>
<details class="proof" markdown="1">
<summary>증명</summary>

$G$의 generator들의 모임 $X$를 생각한 후, $X$에 대한 free group $F$를 생각하자. 함수 $X\hookrightarrow G$에 의해 정의되는 $F$에서 $G$로의 group homomorphism이 존재하며, 이 homomorphism의 image는 $G$의 generator들을 모두 포함하므로 surjective하다.

</details>

비슷하게 free product 또한 정의할 수 있으며, 이는 우리가 찾아헤매던 [정리 14](#thm14)와 같은 universal property를 갖는 group이 된다.

마찬가지로 construction은 간략하게만 소개한다. 

Group들의 family $(G_i)$가 주어졌다 하자. 편의를 위해 이들이 모두 서로 disjoint하다고 하고, $X=\bigcup G_i$라 하자. 즉, 임의의 원소 $x\in X$에 대하여 $x\in G_i$인 $i$를 유일하게 찾을 수 있다. $G_i$들은 이미 역원을 포함하고 있으므로, generator들의 모임으로는 $X\cup\\{e\\}$만 생각하면 충분하다. 

$(G_i)$들의 *free product* $\prod^\* G_i$는 이 집합 $X\cup\\{e\\}$에서 만들어지는 reduced word들의 모임이다. 큰 흐름은 free group을 정의할 때와 같지만, 이번에는 $G_i$의 원소들이 자신들끼리 연산이 가능하므로 reduced word를 정의할 때 조금 더 신경을 써 주어야 한다. Free product를 정의할 때 사용하는 reduced word라는 말은 집합 $X\cup\\{e\\}$의 원소들로 만들어진 word

$$x_1x_2\cdots x_n$$

가 다음의 세 조건을 만족한다는 것을 의미한다.

1. 만일 $n>1$이라면 $x_k$들 가운데 어떤 것도 $e$와 같지 않다. 
2. 만일 $x_k\in X$라면 $x_k$는 이 원소가 포함된 group $G_i$에서 non-identity element다. 
3. 인접한 두 원소 $x\_i, x\_{i+1}$은 반드시 서로 다른 group에 속한다.

임의의 word가 주어졌을 때, 이를 reduced word로 만드는 법은 간단하다. 인접한 원소들이 서로 같은 group에 속하는 원소인지를 모두 체크해본 후, 같은 group에 속하는 원소들은 이 group에서의 연산을 통해 하나의 원소로 합쳐준다. 이 과정에서 (혹은 원래부터) 어떤 group에서의 항등원이 나왔다면, 그 원소는 지워버리면 된다. 

그럼 $\prod^\*G_i$ 위의 연산은 free group을 정의할 때와 동일한 concatenation이며[^3], 어렵지 않게 이 모임이 group structure를 갖는다는 것을 확인할 수 있다. 또, [예시 16](#ex16)과 같은 상황은 더 이상 일어나지 않는데, 이는 두 group $G\_1,G\_2$가 abelian이라 하더라도 그 free product $G\_1\*G\_2$는 더 이상 abelian group이 아니기 때문이다.

<div class="example" markdown="1">

<ins id="ex19">**예시 19**</ins> [예시 16](#ex16)과 동일한 상황을 생각하자. 대신 notation상의 편의를 위해 $G_1=\langle a\rangle$, $G_2=\langle b\rangle$이라 하자. 그럼 $G\_1\*G\_2$의 원소는 다음과 같은 원소들

$$ab, a^2b, a^{-1}ba^3, bab^2, \cdots$$

의 모임이다. 예를 들어, 두 개의 원소 $a^2b$와 $bab^2$를 연산하면 우리는

$$(a^2b)(bab^2)=a^2bbab^2=a^2b^2ab^2$$

을 얻는다. 

이 때 $\langle a\rangle$과 $\langle b\rangle$은 $G\_1\*G\_2$의 cyclic subgroup이고, 따라서 $G_1$과 $G_2$에서 $G\_1\*G\_2$으로의 homomorphism을 $a\mapsto a$, $b\mapsto b$로 정의하면 자연스러운 inclusion map $\iota_1$과 $\iota_2$를 얻는다. 

물론 [예시 16](#ex16)과 같은 문제 또한 일어나지 않는다. $\iota_1(a)\iota_2(b)=ab$이고 $\iota_2(b)\iota_1(a)=ba$인데, 이 두 원소는 $\prod^\*G_i$의 서로 다른 원소이기 때문이다.

</div>

---
**Reference**

**[Bou]** Bourbaki, N. Algebra. I. Chapters 1-3. Translated from the French. Reprint of the 1989 English translation. *Elements of Mathematics. Springer-Verlag, Berlin,* 1998.  
**[Hun]** Thomas W. Hungerford, *Algebra*, Graduate texts in mathematics, Springer, 2003.

---

[^1]: 이 정의가 낯설다면 [Set Theory, §집합의 연산, Remark 1](/ko/math/set_theory/set_operations#rmk1)과, 같은 글에서 product set을 정의할 때의 [motivation](/ko/math/set_theory/set_operations#product-of-sets)을 다시 살펴볼 필요가 있다. 
[^2]: 물론 좌변의 $\operatorname{pr}_i$는 $H\rightarrow H_i$, 우변의 $\operatorname{pr}_i$는 $G\rightarrow G_i$를 의미한다.
[^3]: 이후 이렇게 이어붙여진 word를 reduced word로 만드는 것 포함.
