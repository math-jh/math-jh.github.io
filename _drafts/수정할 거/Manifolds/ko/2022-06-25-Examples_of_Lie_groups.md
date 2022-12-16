---

title: "리 군의 예시들"
excerpt: "Examples of Lie group and Lie groups"

categories: [Math / Manifold]
permalink: /ko/math/manifold/examples_of_Lie_groups
header:
    overlay_image: /assets/images/Manifold/Example_of_Lie_groups.png
    overlay_filter: 0.5
sidebar: 
    nav: "manifold-ko"

date: 2022-06-25
last_modified_at: 2022-06-25
weight: 17

---

우리는 지난 글에서 리 군과 그에 대응되는 리 대수를 살펴봤다. 이번 글에서 살펴볼 리 군의 예시는 $\operatorname{GL}_n(\mathbb{R})$과 그 부분군들이다.

## Lie group $\operatorname{GL}_n(\mathbb{R})$

<div class="proposition" markdown="1">

<ins id="pp1">**명제 1**</ins> 역행렬을 갖는 $n\times n$ 행렬들의 모임 $\operatorname{GL}_n(\mathbb{R})$은 Lie group이다.

</div>
<details class="proof" markdown="1">
<summary>증명</summary>

$\operatorname{GL}_n(\mathbb{R})$은 $n\times n$차원 manifold $\operatorname{Mat}_n(\mathbb{R})$의 open submanifold로서 $n\times n$차원 manifold가 된다. ([§미분다양체의 예시들, 예시 4](/ko/math/manifold/examples_of_manifolds#ex4)) 뿐만 아니라, $\operatorname{GL}_n(\mathbb{R})$ 위에 정의된 곱셈 $AB$를 생각하면, $AB$의 각 성분들은 각 $n^2$개의 $a_i$들과 $b_j$들의 다항식으로 적을 수 있으므로 곱셈은 $C^\infty$이다. 비슷하게 역행렬 $A^{-1}$도 분모 $\det A$를 갖는 $n^2$개 항들의 유리식으로 나타나고, $\operatorname{GL}_n(\mathbb{R})$에서 이 분모는 항상 0이 아니므로 $\operatorname{GL}_n(\mathbb{R})$은 Lie group의 구조를 갖는다.

</details>

한편 우리는 일반적인 Lie group을 다룰 때 그에 대응되는 Lie algebra가 많은 성질들을 결정지어준다는 것을 알고 있다. $\mathbb{R}$-벡터공간으로서 $\operatorname{GL}_n(\mathbb{R})$을 결정지어주는 것은 쉽다. 다음 보조정리는 [§미분사상의 예시들, 명제 4](/ko/math/manifold/examples_of_differentials#pp4)과 정확하게 똑같은 명제지만, 증명하는 방식이 조금 다르다. 

<div class="proposition" markdown="1">

<ins id="lem2">**보조정리 2**</ins> 유한차원 $\mathbb{R}$-벡터공간 $V$와 임의의 $x\in V$에 대하여, $V\cong T_xV$가 성립한다.

</div>
<details class="proof" markdown="1">
<summary>증명</summary>

$V$가 유한차원 $\mathbb{R}$-벡터공간이라 하고, $V$의 basis $(e\_i)\_{i=1}^n$이 주어졌다 하자. 그럼 $V$ 위에서 정의된 단 하나의 coordinate system

$$v=\sum_{i=1}^n v^i e_i\mapsto (v^1,\ldots, v^n)\in\mathbb{R}^n$$

이 $V$를 manifold로 만든다. $(e\_i)$들의 dual basis $(\epsilon^i)$를 생각하자. 그럼 $\epsilon^i$들은 위 coordinate system들의 성분함수들이다. 따라서 임의의 점 $x\in V$에 대하여, tangent space $T_xV$의 basis를 다음의 tangent vector들

$$\frac{\partial}{\partial\epsilon^1}\bigg|_x,\cdots,\frac{\partial}{\partial\epsilon^n}\bigg|_x$$

으로 잡는 것이 자연스럽다.

</details>

위 증명에서는 basis를 하나 택해서 계산했지만, 이렇게 만들어진 isomorphism은 [§미분사상의 예시들, 명제 4](/ko/math/manifold/examples_of_differentials#pp4)의 그것과 같고, 따라서 (isomorphism의 정의에는 basis가 필요했지만) 이 isomorphism은 basis의 선택에 의존하지 않는다.

<div class="proposition" markdown="1">

<ins id="pp3">**명제 3**</ins> $\operatorname{GL}_n(\mathbb{R})$에 대응되는 Lie algebra를 $\mathfrak{gl}_n(\mathbb{R})$이라 하자. 그럼 $\mathbb{R}$-벡터공간 사이의 isomorphism $\alpha:\mathfrak{gl}_n(\mathbb{R})\rightarrow\operatorname{Mat}_n(\mathbb{R})$이 존재한다.

</div>
<details class="proof" markdown="1">
<summary>증명</summary>

[§리 군과 리 대수, 명제 3](/ko/math/manifold/Lie_group_and_Lie_algebra#pp3)에 의하여, $\operatorname{GL}_n(\mathbb{R})$의 Lie algebra $\mathfrak{gl}_n(\mathbb{R})$은 항등원 $I$에서의 tangent space $T_I\operatorname{GL}_n(\mathbb{R})$과 같고, $\operatorname{GL}_n(\mathbb{R})$은 $\operatorname{Mat}_n(\mathbb{R})$의 open submanifold이므로 이는 다시 $T_I\operatorname{Mat}_n(\mathbb{R})$과 동일하다. 따라서 [보조정리 2](#lem2)에 의해, $\mathfrak{gl}_n(\mathbb{R})$은 $\mathbb{R}$-벡터공간으로서 $\operatorname{Mat}_n(\mathbb{R})$과 동일하게 취급할 수 있다.  

</details>

우리는 [§리 군과 리 대수, 명제 3](/ko/math/manifold/Lie_group_and_Lie_algebra#pp3)을 증명한 후, $T_eG$와 $\mathfrak{g}$ 사이의 isomorphism을 통해 $\mathfrak{g}$에서 정의된 Lie bracket을 $T_eG$로 옮겨와 $T_eG$를 Lie algebra로 취급할 수 있다는 것을 언급했었다. 그런데 $\operatorname{Mat}_n(\mathbb{R})$의 경우, $\mathfrak{gl}_n(\mathbb{R})$에서 오는 Lie bracket과는 별도로 이미 충분히 그럴듯한 Lie bracket을 하나 갖고 있다.

<div class="proposition" markdown="1">

<ins id="pp4">**명제 4**</ins> $n\times n$ 행렬들의 모임 $\operatorname{Mat}_n(\mathbb{R})$위에 다음의 식

$$[A,B]=AB-BA$$

을 통해 정의된 bracket $[-,-]$은 [§리 군과 리 대수, 정의 2](/ko/math/manifold/Lie_group_and_Lie_algebra#df2)의 조건을 모두 만족하며, 따라서 $\operatorname{Mat}_n(\mathbb{R})$은 그 자체로 Lie algebra가 된다.

</div>

이에 대한 증명은 단순한 선형대수이므로 생략한다.

어쨌든 이제 [명제 3](#pp3)에서 정의한 $\mathbb{R}$-벡터공간 사이의 isomorphism $\alpha$는 두 Lie algebra 사이의 스칼라곱과 덧셈을 보존하는 bijection이 된다. 뿐만 아니라, $\alpha$는 Lie bracket 또한 보존하고 따라서 Lie algebra isomorphism이 된다.

<div class="proposition" markdown="1">

<ins id="pp5">**명제 5**</ins> [명제 3](#pp3)에서 정의한 isomorphism $\alpha$는 Lie algebra isomorphism이다.

</div>
<details class="proof" markdown="1">
<summary>증명</summary>

[명제 3](#pp3)의 isomorphism $\alpha$는 다음 isomorphism들의 합성으로 생각할 수 있다.

$$\mathfrak{gl}_n(\mathbb{R})\overset{\alpha'}{\longrightarrow}T_I\operatorname{GL}_n(\mathbb{R})\overset{\sim}{\longrightarrow}T_I\operatorname{Mat}_n(\mathbb{R})\overset{\sim}{\longrightarrow}\operatorname{Mat}_n(\mathbb{R})$$

즉 $\alpha$는 임의의 $X\in\mathfrak{gl}_n(\mathbb{R})$을 받은 후, $X\mapsto X_I$를 통해 $T_I\operatorname{GL}_n(\mathbb{R})\cong T_I\operatorname{Mat}_n(\mathbb{R})$의 원소를 얻은 후, 다시 [보조정리 2](#lem2)의 isomorphism을 통해 이를 $\operatorname{Mat}_n(\mathbb{R})$의 원소로 보내는 함수이다.

$\operatorname{Mat}_n(\mathbb{R})$의 $n^2$개의 basis

$$\begin{pmatrix}1&0&\cdots&0\\0&0&\cdots&0\\\vdots&\vdots&\ddots&\vdots\\0&0&\cdots&0\end{pmatrix},\quad\begin{pmatrix}0&1&\cdots&0\\0&0&\cdots&0\\\vdots&\vdots&\ddots&\vdots\\0&0&\cdots&0\end{pmatrix},\quad\cdots,\quad \begin{pmatrix}0&0&\cdots&0\\0&0&\cdots&0\\\vdots&\vdots&\ddots&\vdots\\0&0&\cdots&1\end{pmatrix}$$

을 생각하자. 이들의 dual basis는 행렬 $A\in\operatorname{Mat}\_n(\mathbb{R})$에 대하여, $A$의 $(i,j)$ 성분 $A\_{i,j}$을 주는 함수들 $\epsilon^{i,j}:\operatorname{Mat}\_n(\mathbb{R})\rightarrow\mathbb{R}$이다. 

위의 basis를 사용해 [보조정리 2](#lem2)의 증명을 적용하면, $\alpha(X)$의 $(i,j)$ 성분은 $X_I\in T_I\operatorname{GL}_n(\mathbb{R})\cong T_I\operatorname{Mat}_n(\mathbb{R})$를 

$$X_I=\sum a^{i,j}\frac{\partial}{\partial\epsilon^{i,j}}\bigg|_I$$

으로 적었을 때에 해당하는 계수 $a^{i,j}$, 곧 $X_I \epsilon^{i,j}$가 된다. 따라서 $\alpha$가 Lie algebra isomorphism인 것을 보이기 위해서는

$$[X,Y]_I \epsilon^{i,j}=[\alpha(X),\alpha(Y)]_{i,j}$$

가 성립함을 보여야 한다. 우선 좌변의 경우는 약간 더 계산을 하면

$$[X,Y]_I\epsilon^{i,j}=X_I(Y\epsilon^{i,j})-Y_I(X\epsilon^{i,j})\tag{1}$$

이 된다. 한편 다음의 식

$$(\epsilon^{i,j}\circ L_A)(B)=\epsilon^{i,j}(AB)=\sum_{k=1}^n\epsilon^{i,k}(A)\epsilon^{k,j}(B)$$

을 통해, $\operatorname{GL}_n(\mathbb{R})$ 위에서 정의된 함수들로서

$$\epsilon^{i,j}\circ L_A=\sum_{k=1}^n\epsilon^{i,k}(A)\epsilon^{k,j}$$

임을 알 수 있고, 이를 이용하면 임의의 left invariant vector field $X$와 임의의 $C\in\operatorname{GL}_n(\mathbb{R})$에 대하여

$$(X\epsilon^{i,j})(C)=(X\epsilon^{i,j})(L_CI)=(X(\epsilon^{i,j}\circ L_C))(I)=X_I\left(\sum_{k=1}^n\epsilon^{i,k}(C)\epsilon^{k,j}\right)=\sum_{k=1}^n\epsilon^{i,k}(C)X_I\epsilon^{k,j}=\sum_{k=1}^n\epsilon^{i,k}(C)\alpha(X)_{k,j}$$

이므로, 마찬가지로 함수 $X\epsilon^{i,j}$는 다음의 식

$$X\epsilon^{i,j}=\sum_{k=1}^n\alpha(X)_{k,j}\epsilon^{i,k}$$

으로 주어진다는 것을 알 수 있다. 이를 다시 (1)에 대입하면, 우변은

$$\begin{aligned}X_I\left(\sum_{k=1}^n\alpha(Y)_{k,j}\epsilon^{i,k}\right)-Y_I\left(\sum_{k=1}^n\alpha(X)_{k,j}\epsilon^{i,k}\right)&=\sum_{k=1}^n\alpha(Y)_{k,j}X_I(\epsilon^{i,k})-\alpha(X)_{k,j}Y_I(\epsilon^{i,k})\\&=\sum_{k=1}^n\alpha(Y)_{k,j}\alpha(X)_{i,k}-\alpha(X)_{k,j}\alpha(Y)_{i,k}\end{aligned}$$

을 얻는다. 최종적으로 나오는 식은 단순히 $\alpha(X)\alpha(Y)-\alpha(Y)\alpha(X)$의 $(i,j)$번째 성분에 불과하므로 원하는 증명이 완료되었다.

</details>

## Matrix Lie group

$\operatorname{GL}_n(\mathbb{R})$의 subgroup들 가운데 우리가 관심있는 것들은 닫힌집합들이다. 

<div class="definition" markdown="1">

<ins id="df6">**정의 6**</ins> $\operatorname{GL}_n(\mathbb{R})$의 subgroup 중 닫힌집합이 되는 것들을 *matrix Lie group*이라 부른다.

</div>

고전적인 결과인 closed subgroup theorem은 임의의 Lie group $G$의 closed subgroup은 항상 embedded Lie group으로 생각할 수 있다는 것을 보장해주지만, 이는 distribution을 정의해야 증명할 수 있기 때문에 지금 당장 사용할 수는 없다. 그러므로 다음 예시들에서 정의하는 group들은 (아직은) Lie group은 아니다.

<div class="example" markdown="1">

<ins id="ex7">**예시 7**</ins> $\operatorname{GL}_n(\mathbb{R})$의 부분집합 중 행렬식이 1인 원소들을 모두 모아 $\operatorname{SL}_n(\mathbb{R})$이라 하자. 이 모임이 $\operatorname{GL}_n(\mathbb{R})$의 subgroup이 된다는 것은 자명하다. 한편,  $\operatorname{SL}_n(\mathbb{R})$은 연속함수 $\det:\operatorname{GL}_n(\mathbb{R})\rightarrow\mathbb{R}$에 의한 닫힌집합 $\\{1\\}\subset\mathbb{R}$의 preimage이므로 $\operatorname{SL}_n(\mathbb{R})$은 $\operatorname{GL}_n(\mathbb{R})$의 closed subgroup이고, 따라서 matrix Lie group이다.

이번에는 $f:\operatorname{GL}_n(\mathbb{R})\rightarrow\operatorname{Mat}_n(\mathbb{R})$을 $A\mapsto A^tA$로 정의하자. 이제 $\operatorname{GL}_n(\mathbb{R})$의 부분집합 $f^{-1}(I)$를 생각하면 이 집합은 닫힌집합 $\\{I\\}\subset\operatorname{Mat}_n(\mathbb{R})$의 연속함수에 의한 preimage이므로 닫힌집합이고, 따라서 matrix Lie group이 된다. 명시적으로 이 집합은 $A^tA=I$를 만족하는 모든 $n\times n$ 행렬들의 모임이며, 우리는 이를 $\operatorname{O}(n)$으로 적는다.

마지막으로, $\operatorname{O}(n)$의 원소들 가운데 $\det A=1$을 만족하는 원소들을 모아 이를 $\operatorname{SO}(n)$으로 적자. 그럼 $\operatorname{SO}(n)=\operatorname{O}(n)\cap\operatorname{SL}(n)$이고, 따라서 $\operatorname{GL}_n(\mathbb{R})$의 subgroup인 동시에 두 닫힌집합의 교집합이므로 닫힌집합 또한 된다. 따라서 이 모임 또한 matrix Lie group이 된다.

</div>

이들 matrix Lie group들이 실제로 Lie group이 된다는 것을 보이기 위해서는 이들이 모두 manifold 구조를 가지고, 그 manifold 구조에 대해 연산이 $C^\infty$임을 보여야 한다. 얼핏 보면 manifold 구조를 가진다는 것을 보이는 것이 연산들이 $C^\infty$임을 보이는 것보다 쉬울 것 같지만 꼭 그런 것만은 아니다. 예를 들어 $\operatorname{SL}_n(\mathbb{R})$의 경우만 하더라도, $\operatorname{SL}_n(\mathbb{R})$의 연산은 단순히 $\operatorname{GL}_n(\mathbb{R})$의 연산을 제한한 것에 불과하지만 [§부분다양체의 유일성, Restriction of codomain](/ko/math/manifold/uniqueness_of_submanifold#restriction-of-codomain)에서 볼 수 있듯 $C^\infty$ 함수의 치역을 submanifold로 제한한 것은 $C^\infty$가 될 필요가 없기 때문이다. 

다행히 우리는 같은 글에서, embedded submanifold의 경우에는 이것이 성립한다는 것을 보였으며, 또 위에서 Lie group의 closed subgroup은 embedded라는 것을 슬쩍 언급했으므로 $\operatorname{SL}_n(\mathbb{R})$과 $\operatorname{O}(n)$이 embedded submanifold인 것만 직접 보이면 된다.

우선 함수 $\det:\operatorname{GL}_n(\mathbb{R})\rightarrow\mathbb{R}$을 생각하자. 그럼 cofactor expansion에서 $\det A$는

$$\det A=\sum (-1)^{i+j}a_{ij}\det(A^{(i,j)})$$

이므로, 이를 $\epsilon^{i,j}$로 미분하면 

$$\frac{\partial(\det)}{\partial\epsilon^{i,j}}\bigg|_A=(-1)^{i+j}\det(A^{(i,j)})$$

임을 알 수 있다. 즉, $\det$가 submersion이 아니기 위해서는 $\partial(\det)/\partial \epsilon^{i,j}$가 모두 0이어야 하는데, 이를 위해서는 $(n-1)\times(n-1)$ minor matrix들의 행렬식이 모두 0이어야 한다. 이러한 행렬은 어차피 $\operatorname{GL}_n(\mathbb{R})$ 바깥에 있으므로, submersion rank theorem에 의하여 $\operatorname{SL}_n(\mathbb{R})$은 $n^2-1$차원의 embedded submanifold가 된다. 

또, 우리는 $A\mapsto A^tA$가 constant rank를 갖는 differential을 유도하고, 따라서 $\operatorname{O}(n)$이 embedded submanifold가 된다는 것을 보일 수 있다. 임의의 $A,B$에 대하여, 

$$F(AB)=F(AB)=(AB)^t(AB)=B^t F(A)B=(L_{B^t}\circ R_B\circ F)(A)$$

가 성립하므로 $F\circ R_B=L_{B^t}\circ R_B\circ F$가 성립한다. 이제 chain rule을 적용하면 

$$dF_{AB}\circ d(R_B)_A=d(L_{B^t})_{A^tAB}\circ d(R_B)_{A^tA}\circ dF_A$$

가 성립하는데, 어차피 translation들은 모두 diffeomorphism들이므로 rank를 고려할 때는 전혀 영향을 주지 않는다. 따라서 $dF_{AB}=dF_A$가 성립하고, $A,B$는 임의로 택할 수 있으므로 $F$는 constant rank를 갖는다. 

## Exponential map

우리는 각각의 $X\in\mathfrak{g}$마다, $G$의 적당한 1-parameter subgroup $\exp_X:\mathbb{R}\rightarrow G$가 존재하여 

$$d\exp_X\left(\lambda\frac{d}{dr}\right)=\lambda X$$

라는 것을 알고 있으며, 이를 바탕으로 *exponential map* $\exp:\mathfrak{g}\rightarrow G$를 정의했다. 물론 다음의 성질들

$$\exp(tX)=\exp_X(t),\qquad \exp(t_1+t_2)X=(\exp t_1X)(\exp t_2X),\qquad \exp(-tX)=(\exp tX)^{-1}$$

등은 지수함수가 가져야 할 성질이 맞지만, 그렇더라도 이 이름을 완전히 납득할 수 있었던 것은 아니다. 이는 사실 $\operatorname{GL}_n(\mathbb{R})$의 경우에서 온 이름이다.

행렬 $A$에 대하여, 다음의 식

$$e^A=I+A+\frac{A^2}{2!}+\cdots$$

을 통해 *matrix exponential*을 정의하자. 이 식이 잘 정의된다는 것은 약간의 해석학 지식에서 자명하다. 뿐만 아니라, $\det e^A=e^{\operatorname{tr}A}$가 성립한다는 것 또한 어렵지 않게 확인할 수 있다.

이제 $\mathbb{R}$에서 $\operatorname{GL}_n(\mathbb{R})$로의 함수 $t\mapsto e^{tA}$를 생각하면, 이 함수가 정확히 $\exp_A$가 만족해야 할 조건을 만족하므로, 사실은 정확하게 $\exp(A)=e^A$임을 알 수 있다. 



---

**참고문헌**

**[Lee]** John M. Lee. *Introduction to Smooth Manifolds*, Graduate texts in mathematics, Springer, 2012  
**[War]** Frank W. Warner. *Foundations of Differentiable Manifolds and Lie Groups*, Graduate texts in mathematics, Springer, 2013  


---