---

title: "향"
excerpt: "Manifold 위의 orientation"

categories: [Math / Manifold]
permalink: /ko/math/manifold/orientation
header:
    overlay_image: /assets/images/Math/Manifold/Orientation.png
    overlay_filter: 0.5
sidebar: 
    nav: "manifold-ko"

date: 2023-02-13
last_modified_at: 2023-02-13
weight: 19

---

## 유클리드 공간에서의 방향

3차원 공간에서 주어진 standard basis $(e_1,e_2,e_3)$를 생각하자. 우리는 미적분학을 배울 때부터 이 basis가 배열된 순서가 중요하다는 것을 알고 있다. 예를 들어, 위의 basis는 $e_1\times e_2=e_3$을 만족하지만, 순서가 바뀌어 $(e_2,e_1,e_3)$과 같은 식으로 배열되어 있다면 $e_2\times e_1=-e_3$이 되었을 것이다. 

이 관찰을 굳이 standard basis로 한정지을 필요는 없다. 일반적으로 $\mathbb{R}^3$의 모든 orthonormal basis $(x_1,x_2,x_3)$에 대하여도 $x_1\times x_2$의 값이 $x_3$인지 $-x_3$인지의 여부에 따라 이 basis가 올바른 순서로 배열되었는지 아닌지를 알 수 있다. 이를 식으로 나타내면

$$x_3\cdot(x_1\times x_2)$$

의 값이 $+1$인지, $-1$인지에 따라 순서가 결정되는 것이다. 그런데 위의 식은

$$x_3\cdot(x_1\times x_2)=\det[x_3\;x_1\;x_2]=\det[x_1\;x_2\;x_3]$$

과 같으므로, 우리는 orthonormal이 아닌 일반적인 basis에 대해서도 위의 행렬식의 값이 양수인지 음수인지를 읽어내어 순서를 정해줄 수 있다.

이렇게 $\mathbb{R}^3$의 경우에서 basis의 순서를 행렬식을 통해 정의하고 나면, $\mathbb{R}^m$에서도 자연스럽게 basis $(x_1,\ldots, x_m)$이 올바른 순서로 배열되었는지, 혹은 반대로 배열되었는지를 알 수 있다. 즉 다음의 행렬식

$$\det[x_1\;x_2\;\cdots\;x_m]$$

의 부호를 조사해보면 된다.

## 행렬식과 방향

$V,W$가 $n$차원 $\mathbb{R}$ 벡터공간이라 하고, linear map $L:V\rightarrow W$가 주어졌다 하자. 그럼 [\[다중선형대수\] §텐서대수, ⁋명제 11](/ko/math/multilinear_algebra/tensor_algebras#prop11)의 universal property에 의하여, 다음의 linear map

$$\bigwedge\nolimits^n(L):\bigwedge\nolimits^n(V)\rightarrow\bigwedge\nolimits^n(W)$$

이 잘 정의된다. 한편 $V,W$가 모두 $n$차원이므로 $\bigwedge\nolimits^n(V),\bigwedge\nolimits^n(W)$는 모두 1차원 벡터공간이 되고, 따라서 위의 linear map은 임의의 영이 아닌 벡터가 어디로 옮겨지는지에 의해 유일하게 결정된다. 특히 만일 $V=W$라면, $\bigwedge\nolimits^n(V)$의 영이 아닌 임의의 벡터는 항상 자기 자신의 상수배로 옮겨지게 되며, 이 때의 상수가 $L$의 행렬식과 같다. 이러한 관점에서 $\bigwedge\nolimits^n(L)$을 *determinant map*이라 부르기도 하고, $E$가 manifold $M$ 위에 정의된 $n$차원의 vector bundle이라면 $\bigwedge\nolimits^n(E)$를 $E$의 *determinant bundle*이라 부르기도 한다.

특별히 $E=T^\ast M$이라면 다음과 같이 정의한다.

<div class="definition" markdown="1">

<ins id="def1">**정의 1**</ins> $M$이 $m$차원의 connected manifold라 하자. 이 때, $M$이 *orientable*이라는 것은 $\bigwedge\nolimits^m(M)\setminus\\{0\\}$이 두 개의 component를 갖는 것이고, 이 때 두 component중 하나를 택하는 것을 $M$의 *orientation*이라 부른다. 

</div>

<div class="proposition" markdown="1">

<ins id="prop2">**명제 2**</ins> $M$이 $m$차원의 connected manifold라 하자. 다음이 모두 동치이다.

1. $M$이 orientable이다.
2. $M$을 덮는 적당한 coordinate system들의 모임이 존재하여, 이들이 겹치는 곳에서 Jacobian이 항상 0보다 크도록 할 수 있다.
3. $M$ 위에 정의된 non-vanishing $m$-form이 존재한다.

</div>
<details class="proof" markdown="1">
<summary>증명</summary>



</details>

<div class="example" markdown="1">

<ins id="ex3">**예시 3**</ins> 

임의의 Lie group은 orientable이다. 이는 $\Omega_\text{l.inv}^\ast(G)$에서의 임의의 basis $\omega_1,\ldots,\omega_n$을 택한 후, 이들의 wedge $\omega_1\wedge\cdots\wedge\omega_n$을 생각하면 이것이 $G$ 위에서 nonvanishing $n$-form을 정의하기 때문이다.

</div>

---

**참고문헌**

**[War]** Frank W. Warner. *Foundations of Differentiable Manifolds and Lie Groups*, Graduate texts in mathematics, Springer, 2013  
**[Lee]** John M. Lee. *Introduction to Smooth Manifolds*, Graduate texts in mathematics, Springer, 2012  

---