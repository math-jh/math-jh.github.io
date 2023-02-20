---

title: "고전군"
excerpt: "Lie group과 Lie algebra의 예시들"

categories: [Math / Manifold]
permalink: /ko/math/manifold/classical_groups
header:
    overlay_image: /assets/images/Math/Manifold/Classical_groups.png
    overlay_filter: 0.5
sidebar: 
    nav: "manifold-ko"

date: 2023-02-04
last_modified_at: 2023-02-04
weight: 18

---

다음 글에서 우리는 Lie group $G$와, 그 Lie algebra $\mathfrak{g}$ 사이에 밀접한 관련이 있다는 것을 살펴본다. 그 전에 우리는 다양한 matrix Lie group들의 예시를 살펴본다.

우선 임의의 벡터공간 $V$의 basis $e_1,\ldots,e_n$과 그 dual basis $r^1,\ldots, r^n$에 대하여, 우리는 $V$와 $T_p V$ 사이의 isomorphism

$$\sum a_ie_i\leftrightarrow \sum a_i\frac{\partial}{\partial r^i}\tag{1}$$

이 존재한다는 것을 알고 있다. ([§미분사상의 예시들, ⁋명제 4](/ko/math/manifold/examples_of_differentials#pp4)) 이를 바탕으로 우리는 다양한 matrix group들의 구조를 파악할 수 있다. 가령 임의의 $A\in\Mat_n(\mathbb{R})$에 대하여

$$T_A\Mat_n(\mathbb{R})\cong\Mat_n(\mathbb{R})$$

이 성립하며, 이를 이용하여 [§미분사상의 예시들, ⁋예시 5](/ko/math/manifold/examples_of_differentials#ex5)에서 우리는 $T_I\GL(n,\mathbb{R})\cong\Mat_n(\mathbb{R})$인 것을 살펴보았다. 이 절에서는 다른 다양한 matrix group들의 구조를 살펴본다.

## General linear group

<div class="example" markdown="1">

<ins id="ex1">**예시 1 (General linear group)**</ins> 위에서 살펴보았듯 $T_I\GL(n,\mathbb{R})\cong\Mat_n(\mathbb{R})$이고 따라서 $\GL(n,\mathbb{R})$의 Lie algebra $\gl(n,\mathbb{R})$은 $\mathbb{R}$-벡터공간으로서 $\Mat_n(\mathbb{R})$과 같다. 명시적으로, 이 isomorphism $\beta$는

$$\gl(n,\mathbb{R})\cong T_I\GL(n,\mathbb{R})\cong T_I\Mat_n(\mathbb{R})\cong\Mat_n(\mathbb{R})$$

을 통해 얻어지며, $\Mat_n(\mathbb{R})$의 자연스러운 basis $(e\_{ij})\_{1\leq i,j\leq n}$에 식 (1)을 적용하면 임의의 

$$X=\sum_{i,j} X^{ij}\frac{\partial}{\partial r^{ij}}\mapsto \alpha(X)=X_I=\sum_{i,j} X^{ij}(I)\frac{\partial}{\partial r^{ij}}\bigg|_I\in T_I\GL(n,\mathbb{R})$$

에 대하여 $\beta(X)\in\Mat_n(\mathbb{R})$는 $(i,j)$ 성분이 다음의 식

$$\beta(X)_{ij}=r^{ij}(\beta(X))=r^{ij}\bigl(\sum X^{ij}(I)e_{ij}\bigr)=X^{ij}(I)$$

으로 주어진 행렬은 $\sum X^{ij}(I)e_{ij}$와 같다. 

한편 $\Mat_n(\mathbb{R})$ 위에는 자연스러운 bracket $[A,B]=AB-BA$가 존재하며, 이를 통해 $\Mat_n(\mathbb{R})$은 Lie algebra 구조를 갖는다. 우리는 $\beta$가 $\mathbb{R}$-벡터공간 사이의 linear map일 뿐만 아니라, bracket을 보존하는 *Lie algebra homomorphism*이기도 하다는 것을 보인다. 즉, 임의의 $X,Y\in\mathfrak{gl}(n,\mathbb{R})$에 대하여 $\beta([X,Y])=[\beta(X),\beta(Y)]$가 성립한다.

이를 보이기 위해 우선 임의의 $A,B\in\Mat_n(\mathbb{R})$에 대하여 

$$(r^{ij}\circ L_A)(B)=r^{ij}(AB)=\sum_{k=1}^n r^{ik}(A)r^{kj}(B)$$

임을 기억하자. 그럼 $Y$가 left invariant인 벡터장이므로, 

$$\begin{aligned}(Yr^{ij})(A)&=Y_A(r^{ij})=Y_{AI}(r^{ij})=[(dL_A)_I(Y_I)](r^{ij})\\&=Y_I(r^{ij}\circ L_A)=Y_I\left(\sum_{k=1}^nr^{ik}(A)r^{kj}\right)\\&=\sum_{k=1}^nr^{ik}(A) Y_Ir^{kj}=\sum_{k=1}^n r^{ik}(A)Y^{kj}(I)\\&=\sum_{k=1}^n r^{ik}(A)\beta(Y)_{kj}\end{aligned}$$

을 얻는다. 이제 

$$\beta([X,Y])_{ij}=[X,Y]_I(r^{ij})=X_I(Yr^{ij})-Y_I(Xr^{ij})$$

에 방금 전의 결과 

$$Yr^{ij}=\sum_k\beta(Y)_{kj}r^{ik},\qquad Xr^{ij}=\sum_k\beta(X)_{kj}r^{ik}$$

를 대입하여 정리하면 원하는 식 $\beta([X,Y])\_{ij}=[\beta(X),\beta(Y)]\_{ij}$를 얻는다. 

</div>

이와 동일한 계산을 통해 $\mathbb{C}$ 위에서의 general linear group $\GL(n,\mathbb{C})$에 대해서도 $\gl(n,\mathbb{C})\cong\Mat_n(\mathbb{C})$임을 확인할 수 있다. 여기에서 $\GL(n,\mathbb{C})$는 $z=x+iy$를 통하여 $2n^2$차원 manifold로 생각할 수 있다. 다만 주의할 것은 $\GL(n,\mathbb{C})$와 $\GL(2n,\mathbb{R})$은 서로 다른 manifold라는 것이다. 예를 들어 $\GL(2n,\mathbb{R})$은 connected가 아니지만 $\GL(n,\mathbb{C})$는 connected이다.

## Matrix exponential

$\mathbb{R}$ 위에 정의된 임의의 유한차원 벡터공간에 norm을 정의하는 방법은 위상적으로는 유일하며, 이렇게 정의된 norm은 $\mathbb{R}$의 completeness에 의하여 complete metric을 정의한다. (<#ref#>) 특히 $\Mat_n(\mathbb{R})$에 operator norm을 줄 경우 다음의 식

$$\lVert XY\rVert\leq\lVert X\rVert\lVert Y\rVert$$

이 성립하므로, 이 사실들을 종합하면 임의의 $X\in\Mat_n(\mathbb{R})$에 대하여 다음의 *matrix exponential*

$$\exp(X)=\sum_{i=0}^\infty\frac{X^k}{k!}$$

이 잘 정의된다는 것을 알 수 있다. 

다음 두 명제는 기본적으로 선형대수학과 미적분학의 결과이다.

<div class="proposition" markdown="1">

<ins id="pp2">**명제 2**</ins> 임의의 $X\in\Mat_n(\mathbb{R})$에 대하여 

$$\frac{d}{dt}\exp(tX)=X\exp(tX)=\exp(tX)X$$

이 성립한다.

</div>

<div class="proposition" markdown="1">

<ins id="pp3">**명제 3**</ins> 임의의 $X\in\Mat_n(\mathbb{R})$에 대하여 $\det(\exp X)=\exp(\tr X)$이 성립한다. 

</div>

## Special linear group

$\SL(n,\mathbb{R})$이 $n^2-1$차원의 Lie group이라는 것은 자명하지만, 그 Lie algebra를 구하기 위해서는 약간의 노력이 더 필요하다. 특히 determinant map $\det:\GL(n,\mathbb{R})\rightarrow \mathbb{R}$에 대해 조금 더 자세히 살펴볼 필요가 있다. 

<div class="proposition" markdown="1">

<ins id="lem4">**보조정리 4**</ins> 임의의 $X\in\gl(n,\mathbb{R})=T_I\Mat_n(\mathbb{R})$과, [예시 1](#ex1)의 함수 $\beta$에 대하여 $(d(\det))_I(X_I)=\tr\beta(X)$가 성립한다. 

</div>
<details class="proof" markdown="1">
<summary>증명</summary>

우선 [§미분사상의 예시들, ⁋명제 2](/ko/math/manifold/examples_of_differentials#pp2)로부터 우리는 다음 두 조건

$$\gamma(0)=I,\qquad (d\gamma)_0\left(\frac{d}{dt}\bigg|_0\right)=X_I$$

을 만족하는 곡선 $\gamma:(-\epsilon,\epsilon)\rightarrow\Mat_n(\mathbb{R})$을 찾을 수 있다. 특히, $\gamma(t)=\exp(tX)$으로 정의하면 이 조건이 만족된다. 이제

$$\begin{aligned}(d(\det))_I(X_I)&=\frac{d}{dt}\bigg|_{t=0}\det(\exp(tX))=\frac{d}{dt}\bigg|_{t=0}\exp(t\tr X))\\
&=(\tr X)\frac{d}{dt}\bigg|_{t=0}(\exp(t\tr X))=\tr X\end{aligned}$$

이므로 원하는 결과를 얻는다.

</details>

<div class="example" markdown="1">

<ins id="ex5">**예시 5 (Special linear group)**</ins> $\sl(n,\mathbb{R})$을 구하기 위해서는 임의의 tangent vector $X_I\in T_I\SL(n,\mathbb{R})$이 만족해야 할 조건만 찾으면 충분하다. 

다시 [§미분사상의 예시들, ⁋명제 2](/ko/math/manifold/examples_of_differentials#pp2)을 통해 다음 두 조건

$$\gamma(0)=I,\qquad (d\gamma)_0\left(\frac{d}{dt}\bigg|_0\right)=X_I$$

을 만족하는 곡선 $\gamma:(-\epsilon,\epsilon)\rightarrow\SL(n,\mathbb{R})$을 찾자. 그럼

$$\det(\gamma(t))=1$$

이 모든 $t$에 대해 성립하고 따라서 이를 미분하면

$$0=\frac{d}{dt}\bigg|_{t=0}\det(\gamma(t))=(d(\det))_I(X_I)=\tr(X_I)$$

가 성립한다. 즉 $\sl(n,\mathbb{R})$은 식 $\tr X=0$으로 정의된 $\gl(n,\mathbb{R})$의 $n^2-1$차원 부분공간에 속해야 한다. 그런데 $\sl(n,\mathbb{R})$ 또한 $n^2-1$차원이므로 이 두 공간은 동일하다. 즉

$$\sl(n,\mathbb{R})=\{X\in\Mat_n(\mathbb{R})\mid \tr X=0\}.$$

어렵지 않게 $\sl(n,\mathbb{R})$은 Lie bracket $[-,-]$에 대하여 닫혀있다는 것을 보일 수 있으며, [예시 2](#ex2)와 마찬가지 방식을 통해 $\beta$가 Lie algebra homomorphism이 되는 것을 확인할 수 있다. 

</div>

## Orthogonal group

이번에는 orthogonal group

$$\Omat(n)=\{A\in\Mat_n(\mathbb{R})\mid A^TA=I\}$$

을 생각하자. 그럼 $\Omat(n)$은 다음의 식

$$f(A)=A^TA$$

으로 정의된 함수 $f:\GL(n,\mathbb{R})\rightarrow\GL(n,\mathbb{R})$에 대한 $I$의 level set임을 확인할 수 있다. [예시 5](#ex5)와 마찬가지로 이번엔 $X_I\in T_I\Omat(n)$이 만족해야 할 조건을 구해보면, 

$$\gamma'(t)^T\gamma(t)+\gamma(t)^T\gamma'(t)=0$$

이 되므로, $t=0$을 대입하면 $X^T+X=0$을 얻는다. 앞선 예시와 마찬가지로 이들의 차원을 생각하면 $\Omat(n)$의 Lie algebra $\omat(n)$은 실제로 

$$\omat(n)=\{X\in\Mat_n(\mathbb{R})\mid X+X^T=0\}$$

으로 주어진다는 것을 알 수 있다. 

Orthogonal group의 원소들 중 행렬식이 1인 것들을 모아둔 *special orthogonal group* $\SO(n)$의 경우, 새로 추가되는 조건 $\det(A)=1$은 [예시 5](#ex5)의 논증을 거쳐 $\tr X=0$으로 바뀌는데, skew-symmetric인 행렬은 이미 이 조건을 만족하므로 $\so(n)=\omat(n)$이 된다.

## Unitary group

앞서 살펴본 orthogonal matrix들의 경우, 별 말이 없으면 실수 위에서 정의된 행렬들만을 생각하는 것이 일반적이다. $\GL(n,\mathbb{R})$에서 $\GL(n,\mathbb{C})$를 생각하듯 이를 $\Omat(n,\mathbb{C})$로 확장하는 것 또한 가능하지만, 보편적으로 $\mathbb{C}$ 위의 행렬들을 생각할 때는 다음의 *unitary group*

$$\Umat(n)=\{A\in\Mat_n(\mathbb{C})\mid A^\ast A=I\}$$

의 원소들을 생각하게 된다. 마찬가지로 위의 논증을 반복하면 $\Umat(n)$의 Lie algebra $\umat(n)$은 다음의 식

$$\umat(n)=\{X\in\Mat_n(\mathbb{C})\mid X^\ast+X=0\}$$

이 경우, $\umat(n)$의 원소들은 $\tr X=0$을 만족할 필요가 없기 때문에 *special unitary group* $\SU(n)$의 Lie algebra $\su(n)$은

$$\su(n)=\{X\in\Mat_n(\mathbb{C})\mid X^\ast+X=0,\tr X=0\}$$

으로 주어지게 되며, 일반적으로 $\umat(n)$의 proper subalgebra가 된다.

## Symplectic group

마지막으로 살펴볼 *symplectic group*은 다음의 식

$$\Sp(2n)=\{A\in\Mat_{2n}(\mathbb{R})\mid A^TJA=J\},\qquad J=\begin{pmatrix}0&I\\-I&0\end{pmatrix}$$

으로 정의된다. 그럼 $\Sp(2n)$의 Lie algebra $\sp(2n)$은 다음의 식

$$\sp(2n)=\{X\in\Mat_{2n}(\mathbb{R})\mid X^TJ+JX=0\}$$

으로 주어진다.

---

**참고문헌**

**[War]** Frank W. Warner. *Foundations of Differentiable Manifolds and Lie Groups*, Graduate texts in mathematics, Springer, 2013  

---