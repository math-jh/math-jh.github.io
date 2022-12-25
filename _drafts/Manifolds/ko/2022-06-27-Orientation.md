---

title: "Orientation"
excerpt: "Differential form"

categories: [Math / Manifold]
permalink: /ko/math/manifold/Orientation
header:
    overlay_image: /assets/images/Manifold/Orientation.png
    overlay_filter: 0.5
sidebar: 
    nav: "manifold-ko"

date: 2022-06-27
last_modified_at: 2022-06-27
weight: 18

---

우리는 마지막으로 다양체 위에서의 적분을 정의한다. 이를 위해서는 방향의 개념이 필수적이다. 

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

## Manifold에서의 방향

그런데 잘 생각해보면, 행렬식이란 별다른 것이 아닌 $m$-form에 불과하다. $V$가 $m$차원 $\mathbb{R}$-벡터공간일 때, $\bigwedge\nolimits^m(V^\ast)$는 1차원 $\mathbb{R}$-벡터공간이 된다. 우리는 이 공간에서 크기가 1인 두 벡터 가운데 중 하나를 택하여 그것을 determinant라 부르기로 약속한 것이다. 따라서 일반적으로 다음을 정의한다.

<div class="definition" markdown="1">

<ins id="df1">**정의 1**</ins> $m$차원 $\mathbb{R}$-벡터공간 $V$가 주어졌다 하자. $V$ 위에 정의된 *orientation<sub>향</sub>*은 $\bigwedge\nolimits^m(V^\ast)\setminus\\{0\\}$의 두 component 중 하나를 택하는 것이다.

</div>

그러나 벡터공간과 다르게, 일반적인 manifold에서는 방향을 잡기가 쉽지 않다. 대표적으로 뫼비우스 띠의 경우는 잘 정의된 방향이 존재하지 않는다. 따라서 우선 방향을 줄 수 있는 manifold를 정의한다.

<div class="definition" markdown="1">

<ins id="df2">**정의 2**</ins> $M$이 $m$차원의 connected manifold라 하자. 이 때, $M$이 *orientable*이라는 것은 $\bigwedge\nolimits^m(M)\setminus\\{0\\}$이 두 개의 component를 갖는 것이고, 이 때 두 component중 하나를 택하는 것을 $M$의 *orientation*이라 부른다. 

</div>

<div class="proposition" markdown="1">

<ins id="pp3">**명제 3**</ins> $M$이 $m$차원의 connected manifold라 하자. 다음이 모두 동치이다.

1. $M$이 orientable이다.
2. $M$을 덮는 적당한 coordinate system들의 모임이 존재하여, 이들이 겹치는 곳에서 Jacobian이 항상 0보다 크도록 할 수 있다.
3. $M$ 위에 정의된 non-vanishing $m$-form이 존재한다.

</div>
<details class="proof" markdown="1">
<summary>증명</summary>



</details>

예를 들어, 임의의 Lie group은 orientable이다. 이는 $G$ 위에 정의된 left invariant 1-form들, 즉 $T_e^\ast G$의 원소들을 left translation을 통해 임의의 $g\in G$로 보내어 nonvanishing $n$-form을 만들 수 있기 때문이다. 

---

**참고문헌**

**[War]** Frank W. Warner. *Foundations of Differentiable Manifolds and Lie Groups*, Graduate texts in mathematics, Springer, 2013  
**[Lee]** John M. Lee. *Introduction to Smooth Manifolds*, Graduate texts in mathematics, Springer, 2012  

---