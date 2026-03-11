---

title: "제한합"
excerpt: "Group들의 restricted sum"

categories: [Math / Algebraic Structures]
permalink: /ko/math/algebraic_structures/restricted_sum
header:
    overlay_image: /assets/images/Math/Algebraic_Structures/Restricted_sum.png
    overlay_filter: 0.5
sidebar: 
    nav: "algebraic_structures-ko"

date: 2023-01-09
last_modified_at: 2023-01-09
weight: 8

---

앞서 우리는 [§군의 직접곱](/ko/math/algebraic_structures/direct_product)에서 universal property를 통해 $\prod G_i$를 정의했다. 이는 [\[집합론\], §집합의 곱, ⁋정리 3](/ko/math/set_theory/product_of_sets#thm3)에서와 동일한 과정이었는데, 그렇다면 [\[집합론\], §집합의 합, ⁋정리 8](/ko/math/set_theory/sum_of_sets#thm8)과 동일한 성질을 만족하는 group이 존재하는지가 자연스러운 질문이 된다. 그러나 [\[집합론\], §집합의 합, ⁋명제 5](/ko/math/set_theory/sum_of_sets#pp5)에서 만든 $\bigsqcup A_i$의 경우, 이 집합에 group 구조를 주는 것부터가 자명하지 않으므로, 이 질문에 대한 답을 찾는 것이 쉽지 않다. 

우리는 우선 abelian group들의 경우에 대해 [\[집합론\], §집합의 합, ⁋정리 8](/ko/math/set_theory/sum_of_sets#thm8)의 universal property를 만족하는 abelian group이 존재함을 보인다. 다음 글에서는 이번 글과는 다른 방식을 통해 <em_ko>임의의</em_ko> group들에 대하여도 이러한 universal property를 만족하는 group이 존재함을 보인다.

## Restricted sum

Group들의 family $(G_i)$와, 이들의 product가 주어졌다 하자. 그럼 $G_i$들 각각은 $\iota_i$를 통해 $\prod G_i$의 subgroup으로 볼 수 있다. 자연스럽게 다음의 식

$$\prod_{i\in I} G_i=\left\langle\bigcup \iota_i(G_i)\right\rangle$$

이 성립하는지를 생각할 수 있다. 이 식은 $I$가 무한집합이라면 거의 대부분 성립하지 않는다. 가장 간단한 예시로, $I=\mathbb{N}$이라 잡고 $G_i=\mathbb{Z}/2\mathbb{Z}=\\{\bar{0}, \bar{1}\\}이$라 하자. 그럼, 예를 들어 좌변은 원소

$$(\bar{1},\bar{1},\cdots)$$

를 포함하지만, 우변은 $\iota_i(\bar{1})$들의 *유한한* 연산을 통해 얻어지는 원소만을 포함하므로 위의 원소를 포함할 수 없다.

<div class="definition" markdown="1">

<ins id="df1">**정의 1**</ins> Group들의 family $(G_i)$가 주어졌다 하고, $G_i$들의 subgroup $H_i$들을 고정하자. 그럼 유한개를 제외한 모든 $i$에 대해 $\pr\_ix\in H\_i$를 만족하는 $x$들로 이루어진 subgroup을 $H_i$에 대한 $G_i$들의 *restricted sum*이라 부르고 $\prod^H G_i$라 표현한다.

특별히 모든 $i$에 대해 $H_i=\\{e\\}$인 경우 $G\_i$들의 *weak direct product*라 부르고, 간단히

$${\prod_{i\in I}}^w G_i$$

으로 표기한다.

</div>

표기법 $\prod^H$는 그렇게까지 좋은 표기법은 아니지만, 다행히 우리는 weak direct product에만 관심이 있으므로 이 표기를 다시 쓸 일은 없다. 

정의에 의해

$$\left\langle\bigcup \iota_i(G_i)\right\rangle={\prod_{i\in I}}^w G_i$$

이 성립한다. 또, 만일 $I$가 유한집합이라면 weak direct product는 보통의 direct product와 동일하다.

그럼 $\prod^wG_i$는 다음과 같은 universal property를 갖는다.

<div class="proposition" markdown="1">

<ins id="thm2">**정리 2**</ins> Group들의 family $(G_i)$와 이들의 weak direct product $\prod^w G_i$가 주어졌다 하자. 또 다른 group $H$에 대하여, group homomorphism들 $f_i:G_i\rightarrow H$가 다음의 조건

> 임의의 $i\neq j$에 대하여 $x\in G_i$이고 $y\in G_j$라면, $f_i(x)f_j(y)=f_j(y)f_i(x)$
 
을 만족한다면, 유일한 group homomorphism $f:\prod^w G_i\rightarrow H$가 존재하여 $f_i=f\circ\iota_i$가 임의의 $i$에 대해 성립한다. 

</div>
<details class="proof" markdown="1">
<summary>증명</summary>

우선 유일성부터 보이자. 만일 $f, f'$가 위의 식을 만족한다면, 이들은 $\bigcup\iota_i(G_i)$에서 같은 값을 가져야 하므로 $\prod^w G_i$에서도 같은 값을 가져야 하고 따라서 $f=f'$여야 한다.

이제 $f$의 존재성을 보여야 한다. 임의의 $x\in \prod^w G_i$에 대하여, $f(x)$를 다음의 식

$$f(x)=\prod_{i\in I} f_i(\pr_ix)$$

으로 정의하자. 이 때 $\prod$는 일반적인 원소들의 곱을 의미한다. $x$는 $\prod^w G_i$의 원소이므로, 우번의 $f_i(\pr_ix)$는 유한개의 $i$를 제외하면 모두 항등원이고, 따라서 이 곱은 잘 정의된다. 

식 $f_i=f\circ\iota_i$가 성립하는 것은 자명하고, $f$가 group homomorphism인 것은 임의의 $x,y\in\prod^wG_i$에 대해

$$f(xy)=\prod_{i\in I}f_i(\pr_i(xy))=\prod_{i\in I}f_i(\pr_ix)f_i(\pr_iy)$$

가 성립하므로, $\pr_i(xy)$가 $e_i$가 아니도록 하는 유한개의 값만 골라 이 index들을 $1,\ldots, n$이라 하면

$$f_1(\pr_1x)f_1(\pr_1y)f_2(\pr_2x)f_2(\pr_2y)\cdots f_n(\pr_nx)f_n(\pr_ny)$$

가 되고, 이 때 $f_i(\pr_ix)$와 $f_j(\pr_jy)$는 $i\neq j$라면 항상 commute하므로 이 식을

$$f_1(\pr_1x)f_2(\pr_2x)\cdots f_n(\pr_nx)f_1(\pr_1y)f_2(\pr_2y)\cdots f_n(\pr_ny)$$

으로 바꾸어 쓸 수 있다. 따라서 $f(xy)=f(x)f(y)$이고 $f$는 group homomorphism이 된다. $f_i=f\circ\iota_i$인 것은 자명하다.

</details>

$f_i$들에 걸려있는 조건

> 임의의 $i\neq j$에 대하여 $x\in G_i$이고 $y\in G_j$라면, $f_i(x)f_j(y)=f_j(y)f_i(x)$

은 필연적으로 나와야 할 조건인데, 이 조건들이 정확히 $\iota_i$들이 만족하는 조건이기 때문이다. 이로 인해 [정리 6](#thm6)이 abelian group들에 대해서만 우리의 물음에 대한 답이 된다.

Weak direct product의 universal property를 이용하면 direct product때와 유사한 몇몇 성질들을 보일 수 있다. 예컨대 다음이 성립한다.

<div class="proposition" markdown="1">

<ins id="pp3">**명제 3**</ins> $G_i$들이 group이고, $H_i$들이 $G_i$들의 normal subgroup이라 하면 $\prod^w H_i$들 또한 $\prod^w G_i$들의 normal subgroup이고 그 quotient group은 $\prod^w (G_i/H_i)$와 같다.

</div>

## Internal weak product

$G$가 group이고, $(H_i)$들이 $G$의 subgroup들의 family라 하자. 만일 $i\neq j$일 때마다 $H_i$의 원소들이 $H_j$의 원소들과 commute한다면, inclusion homomorphism들 $\iota_i:H_i\rightarrow G$에 의해 유도되는 $\prod^w H_i$에서 $G$로의 homomorphism $\iota$가 존재한다.

또, 다음을 정의한다.

<div class="definition" markdown="1">

<ins id="df4">**정의 4**</ins>  위와 같은 상황에서, 만일 $\iota$가 isomorphism이라면 $G$가 $H_i$들의 *internal weak direct product*라고 부른다. 

</div>

[정리 2](#thm2)에서 만들어낸 homomorphism $f$의 모양을 생각하면, $G$가 $H_i$들의 internal weak direct product인 것은 다음 조건

> 임의의 $x\in G$가 $y_i\in H_i$를 만족하는 finitely supported family $(y\_i)\_{i\in I}$들의 곱 $\prod y_i$로 나타날 수 있다.

과 동치임을 확인할 수 있다. 

만일 subgroup들 $H_i$가 모두 $G$의 normal subgroup이라면, 추가적으로 다음의 조건이 갖춰지면 $G$가 $H_i$들의 internal weak direct product가 된다.

<div class="proposition" markdown="1">

<ins id="pp5">**명제 5**</ins> Group $G$의 normal subgroup들 $(H_i)$가 다음의 두 조건

1. $G=\bigl\langle\bigcup_{i\in I} H_i\bigr\rangle$,
2. $H_k\cap \bigl\langle\bigcup_{i\neq k} H_i\bigr\rangle=\\{e\\}$

을 만족한다면 $G$가 $H_i$들의 internal weak direct product이다.

</div>
<details class="proof" markdown="1">
<summary>증명</summary>

우선 2번 조건은 특히 $H_i\cap H_j=\\{e\\}$가 모든 pair $i\neq j$에 대해 성립한다는 것을 보여준다. 이제 $x_i\in H_i,x_j\in H_j$를 임의로 택하면, 

$$x_ix_jx_i^{-1}x_j^{-1}=x_i\bigl(x_jx_i^{-1}x_j^{-1}\bigr)=\bigl(x_ix_jx_i^{-1}\bigr)x_j^{-1}\in H_i\cap H_j=\{e\}$$

으로부터 $H_i$와 $H_j$의 원소들이 commute한다는 것을 안다. 따라서 inclusion homomorphism $\iota_i$들이 [정리 2](#thm2)에서와 같이 $\iota$를 잘 유도한다.

$G$가 $H_i$들의 internal weak direct product임을 보이기 위해서는 이렇게 유도된 $\iota$가 isomorphism인 것을 보여야 한다. 우선 1번 조건에 의해, 임의의 $a\in G$는 $\bigcup H_i$들의 *finite*한 operation들을 통해 얻어진다. 또 $H_i$들이 서로 commute하므로, $a$를 

$$a=\prod_{i\in I} h_i=\prod_{i\in I}\iota_i(h_i),\qquad\text{$\supp(h_i)$ finite and $h_i\in H_i$}$$

로 적을 수 있다. $h=\prod_{i\in I} \iota_i(h_i)\in\prod^w H_i$라 하면, 

$$a=\prod_{i\in I}\iota_i(h_i)=\iota_i\left(\prod_{i\in I}h_i\right)=\iota_i(h)$$

이므로 $\iota$는 surjective이다.

이제 $\iota(a)=e$라 하자. 그럼 각 항들이 $H_i$에 속하는 finitely supported family $(a_i)$에 대하여 $a=(a_i)_{i\in I}$로 쓸 수 있다. 다음의 식  

$$\iota(a)=\prod_{i\in I}\iota_i(a_i)=\prod_{i\in I} a_i=e$$
  
으로부터, 만일 $\supp(a_i)$가 하나 이상의 원소를 갖고, $i\in\supp(a_i)$라 하면

$$a_i^{-1}=\prod_{j\in I\setminus\{i\}}a_j\in H_i\cap \left\langle\bigcup_{j\neq i} H_i\right\rangle=\{e\}$$

가 되어 $i\in\supp(a_i)$라는 가정에 모순이다. 따라서 $\supp(a_i)$는 공집합이고 $a$는 항등원이다. 

</details>


## Direct sum of abelian groups

[정리 2](#thm2)에서 보인 weak direct product의 universal property는 특히 group $H$가 abelian group일 경우 잘 적용된다. 즉 다음이 성립한다.

<div class="proposition" markdown="1">

<ins id="thm6">**정리 6**</ins> Abelian group들의 family $(G_i)$가 주어졌다 하고, $\prod^w G_i$와 inclusion map들 $\iota_i$를 생각하자. 그럼 임의의 abelian group $H$와 group homomorphism들 $f_i:G_i\rightarrow H$에 대하여, $f_i=f\circ\iota_i$이도록 하는 유일한 group homomorphism $f:\prod^wG_i\rightarrow H$가 존재한다.

</div>

따라서, 적어도 abelian group들 사이에서는 weak direct product $\prod^w G_i$가 우리가 찾던 [\[집합론\], §집합의 합, ⁋정리 8](/ko/math/set_theory/sum_of_sets#thm8)의 universal property에 대한 답이 된다. 

<div class="definition" markdown="1">

<ins id="df7">**정의 7**</ins> Abelian group들의 family $(G_i)$와, 이들의 weak direct product $\prod^w G_i$, 그리고 inclusion map들 $\iota_i$가 주어졌다 하자. 그럼 $\prod^w G_i$와 $\iota_i$들을 묶어 $G_i$들의 *direct sum<sub>직합</sub>*이라 부르고 이를 $\sum G_i$로 표현한다.  

</div>


---

**참고문헌**

**[Hun]** Thomas W. Hungerford, *Algebra*, Graduate texts in mathematics, Springer, 2003.

---