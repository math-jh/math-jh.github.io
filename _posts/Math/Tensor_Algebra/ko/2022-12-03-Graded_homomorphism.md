---

title: "등급대수"
excerpt: "등급대수의 부분대수와 아이디얼, 극한"

categories: [Math / Tensor Algebra]
permalink: /ko/math/tensor_algebra/graded_homomorphism
header:
    overlay_image: /assets/images/Math/Tensor_Algebra/Graded_homomorphism.png
    overlay_filter: 0.5
sidebar: 
    nav: "tensor_algebra-ko"

date: 2022-12-03
last_modified_at: 2022-12-03
weight: 2

---

## 등급대수 사이의 준동형사상

이제 우리는 graded algebra에 집중한다. 앞으로 별다른 말이 없을 경우 $A$는 commutative graded ring인 것으로 생각한다. 

<div class="definition" markdown="1">

<ins id="df1">**정의 1**</ins> 두 $\Delta$-graded $A$-algebra $E,E'$에 대하여, $A$-algebra homomorphism $u:E\rightarrow E'$이 *graded algebra homomorphism*이라는 것은 임의의 $\alpha\in\Delta$에 대하여 $u(E_\alpha)\subseteq E_\alpha'$이 성립하는 것이다.

</div>

Graded algebra homomorphism $u:E\rightarrow E'$가 주어졌다 하자. 그럼 $\im u$는 $E'$의 graded subalgebra가 되고, $\ker u$는 $E$의 graded subalgebra가 될 뿐 아니라 $E$의 graded ideal이 된다. 

## 등급대수의 부분대수, 아이디얼과 몫대수

$\Delta$-graded algebra $A$의 graded subalgebra는 $A$의 algebra 가운데, graded submodule인 것을 의미하므로 우선 다음의 보조정리를 보여야 한다.

<div class="proposition" markdown="1">

<ins id="lem2">**보조정리 2**</ins> $M$이 $\Delta$-graded $A$-module이고, $N$이 $M$의 submodule이라 하자. 그럼 다음이 모두 동치이다.

1. $N=\bigoplus_{\alpha\in\Delta}(N\cap M_\alpha)$이 성립한다.
2. 임의의 $x=\sum\_{\alpha\in\Delta} x_\alpha\in N$에 대하여, $x_\alpha\in N$가 항상 성립한다.
3. $N$을 homogeneous element들로 생성할 수 있다.

</div>
<details class="proof" markdown="1">
<summary>증명</summary>

우선 첫 번째 조건과 두 번째 조건이 서로 동치임은 자명하다. 이제 둘째 조건이 성립한다고 가정하면, 

$$N=\left\langle x_\alpha\biggm\vert x=\sum_{\alpha\in\Delta} x_\alpha, x\in N\right\rangle$$

이므로 셋째 조건이 성립하는 것은 자명하다. 

따라서 셋째 조건을 가정하고 둘째 조건을 보이자. $N$이 homogeneous element들 $(y_\alpha)\_{\alpha\in\Delta}$에 의해 생성된다고 가정하고, $N$의 임의의 원소

$$x=\sum_{\alpha\in\Delta}x_\alpha$$

가 주어졌다 가정하자. 한편 $(y\_\alpha)$가 $N$을 생성하므로, 다음의 식

$$x=\sum_{\beta\in\Delta}a_\beta y_\beta$$

을 만족하는 $a_\beta\in A$들이 존재한다. 각각의 $a_\beta$에 대하여 $a_{\beta,\gamma}\in A\_\gamma$를

$$a_\beta=\sum_{\gamma\in\Delta}a_{\beta,\gamma}$$

를 만족하는 homogeneous element들로 잡으면, 위의 식을

$$x=\sum_{\beta\in\Delta}\sum_{\gamma\in\Delta}a_{\beta,\gamma}y_\beta=\sum_{\alpha\in\Delta}\left(\sum_{\beta+\gamma=\alpha}\alpha_{\beta,\gamma}y_\beta\right)$$

으로 쓸 수 있고, 이를 $x=\sum x_\alpha$와 각 성분별로 비교하면 원하는 결과를 얻는다.

</details>

이 조건들이 성립하면, $N$을 $M$의 *graded submodule<sub>부분등급가군</sub>*이라 부른다. 만일 $M$의 graded submodule $N$이 그 자체로 곱셈에 대해 닫혀있기도 하다면, 이 곱셈은 graduation을 보존하므로 다음 정의를 할 수 있다.

<div class="definition" markdown="1">

<ins id="df3">**정의 3**</ins> $\Delta$-graded $A$-algebra $E$가 주어졌다 하자. $E$의 subalgebra $F$가 *graded subalgebra<sub>부분등급대수</sub>*라는 것은 $F$가 $E$의 graded submodule인 것이다.

</div>

한편 $E$는 단순한 $A$-module이 아니라 $A$-algebra이므로, $E$의 left ideal $\mathfrak{a}$가 정의된다. 위와 마찬가지로 $\mathfrak{a}$가 $E$의 graded submodule이라면 $\mathfrak{a}$를 $E$의 *left graded ideal*이라 부른다. 

<div class="proposition" markdown="1">

<ins id="pp4">**명제 4**</ins> 임의의 graded algebra homomorphism $u:E\rightarrow E'$에 대하여, $\ker u$는 $E$의 two-sided graded ideal이며 $\im u$는 $E'$의 graded subalgebra이다.

</div>
<details class="proof" markdown="1">
<summary>증명</summary>

$\ker u$가 $E$의 two-sided ideal이고, $\im u$가 $E'$의 subalgebra인 것이 자명하므로 이 명제를 보이기 위해서는 $\ker u$와 $\im u$가 각각 graded submodule임만 보이면 충분하다.

우선 임의의 $x\in \ker u$를 택하고, $x=\sum_{\alpha\in\Delta} x_\alpha$라 하자. 그럼

$$0=u(x)=u\left(\sum_{\alpha\in\Delta}x_\alpha\right)=\sum_{\alpha\in\Delta} u(x_\alpha)$$

이며, 이 때 $u(x\_\alpha)\in E'\_\alpha$이므로 모든 $\alpha$에 대하여 $u(x\_\alpha)=0$이다. 따라서 [보조정리 2](#lem2)의 둘째 조건으로부터 $\ker u$가 $E$의 graded submodule임을 안다.

비슷하게 임의의 $y\in\im u$가 주어졌다 하자. 그럼 $y=u(x)$이도록 하는 $x\in E$가 존재하며, $x=\sum_{\alpha\in\Delta} x_\alpha$라 하면

$$y=u(x)=u\left(\sum_{\alpha\in\Delta}x_\alpha\right)=\sum_{\alpha\in\Delta}u(x_\alpha)$$

이고, 따라서 $y$의 $\alpha$번째 성분이 $u(x_\alpha)$와 같다는 것을 안다. 자명하게 $u(x_\alpha)\in\im u$이므로, 다시 [보조정리 2](#lem2)의 둘째 조건으로부터 $\im u$가 graded submodule임을 안다.

</details>

일반적으로 $A$-algebra $E$의 two-sided ideal $\mathfrak{a}$가 주어진다면 quotient algebra $E/\mathfrak{a}$를 정의할 수 있었다. 만일 $E$가 graded algebra이고, $\mathfrak{a}$가 graded ideal이라면 $E/\mathfrak{a}$는 $A$-algebra 구조 뿐만 아니라 graduation 또한 물려받는다.

<div class="proposition" markdown="1">

<ins id="pp5">**명제 5**</ins> Graded ring $A=\bigoplus_{\alpha\in\Delta} A_\alpha$와 $\Delta$-graded $A$-algebra $E$가 주어졌다 하자. 그럼 $E$의 two-sided graded ideal $\mathfrak{a}$에 대하여, $E/\mathfrak{a}$ 또한 $\Delta$-graded $A$-algebra이고 이 때 canonical projection map $E\rightarrow E/\mathfrak{a}$는 graded algebra homomorphism이다.

</div>
<details class="proof" markdown="1">
<summary>증명</summary>

다음 식

$$E/\mathfrak{a}=\left(\bigoplus_{\alpha\in\Delta}E_\alpha\right)\bigg/\left(\bigoplus_{\alpha\in\Delta}\mathfrak{a}\cap E_\alpha\right)\cong \bigoplus_{\alpha\in\Delta} E_\alpha/(\mathfrak{a}\cap E_\alpha)$$

으로부터 $E/\mathfrak{a}$에 $\Delta$-graduation을 줄 수 있으며, 이 때 스칼라곱과 $E$의 곱셈이 모두 graduation을 보인다는 것 또한 자명하다. 또, 위의 isomorphism으로부터 임의의 $x_\alpha\in E_\alpha$에 대해 $x_\alpha+\mathfrak{a}\in E_\alpha/(\mathfrak{a}\cap E_\alpha)$임을 안다.

</details>

## 등급대수의 극한

마지막으로 우리는 등급대수의 극한, 특히 direct limit을 정의한다. 

Right directed set $I$와 commutative monoid $\Delta$가 주어졌다 하고, $\Delta$-graded ring들의 directed system $\big((A\_i)\_{i\in I}, (\phi\_{ij})\_{i\leq j}\bigr)$이 주어졌다 하자. 이제 $\Delta$-graded $A\_i$-algebra들의 directed system $\bigl((E\_i)\_{i\in I}, (f\_{ij})\_{i\leq j}\bigr)$에 대하여, 

$$A=\varinjlim_{i\in I} A_i,\qquad E=\varinjlim_{i\in I} E_i$$

이라 하면 $E$는 $A$-algebra이며, 뿐만 아니라 $E$ 위에 정의된 곱셈이 graduation을 잘 따르므로 이는 $\Delta$-graded $A$-algebra가 된다. 

---

**참고문헌**

**[Bou]** Bourbaki, N. Algebra I. *Elements of Mathematics*. Springer. 1998.  

---