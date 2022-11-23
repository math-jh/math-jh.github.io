---

title: "리 군"
excerpt: "Differential form"

categories: [Math / Manifold]
permalink: /ko/math/manifold/Lie_groups
header:
    overlay_image: /assets/images/Manifold/Lie_groups.png
    overlay_filter: 0.5
sidebar: 
    nav: "manifold-ko"

date: 2022-06-22
last_modified_at: 2022-06-25
weight: 15

---

지금껏 우리는 수상쩍은 이름인 Lie[^1]를 외면해 왔었는데, 이제는 미룰 수가 없다.

## 리 군, 리 대수

<div class="definition" markdown="1">

<ins id="df1">**정의 1**</ins> $G$가 *Lie group<sub>리 군</sub>*이라는 것은 $G$가 manifold인 동시에, 이를 group으로 만드는 연산이 존재하여 다음의 함수

$$G\times G\rightarrow G;\qquad (g,h)\mapsto gh^{-1}$$

가 $C^\infty$인 것이다.

</div>

Lie group $G$가 주어졌다 하자. 그럼 임의의 $g\in G$에 대하여, 다음의 식

$$L_g:h\mapsto gh,\qquad R_g:h\mapsto hg$$

으로 정의된 두 함수 $G\rightarrow G$가 $C^\infty$인 것은 자명하다. 이를 각각 $g$에 의한 left, right translation이라 부른다. 뿐만 아니라, 역함수들 $L_{g^{-1}}$, $R_{g^{-1}}$도 마찬가지로 $C^\infty$이므로, $L_g$와 $R_g$는 각각 diffeomorphism이 된다. 

다음의 정의는 이미 조금은 친숙하다. ([§벡터장, 예시 4](/ko/math/manifold/vector_fields#ex4))

<div class="definition" markdown="1">

<ins id="df2">**정의 2**</ins> $\mathbb{R}$-벡터공간 $\mathfrak{g}$가 *Lie algebra<sub>리 대수</sub>*라는 것은 $\mathfrak{g}$ 위에 정의된 bilinear operator인 *Lie bracket* $[-,-]$이 존재하여, 다음의 두 조건

1. $[x,y]=-[y,x]$,
2. $\bigl[[x,y],z\bigr]+\bigl[[y,z],x\bigr]+\bigl[[z,x],y\bigr]=0$

을 만족하는 것이다. 두 번째 항등식을 *Jacobi identity<sub>야코비 항등식</sub>*이라 부른다.

</div>

Lie group $G$가 주어졌다 하자. Manifold로서, $G$ 위에 정의된 vector field들이 존재한다. Vector field $X$가 *left invariant*라는 것은 임의의 $g\in G$에 대하여 $X$가 자기 자신과 $L_g$-related라는 것이다. 즉, 다음의 식

$$dL_g\circ X=X\circ L_g$$

가 모든 $g\in G$에 대해 성립하는 것이다. 위의 정의는 $X$에 대한 $C^\infty$ 가정이 없어도 성립하지만, 모든 left invariant vector field는 반드시 $C^\infty$라는 것을 증명할 수 있다. 

<div class="proposition" markdown="1">

<ins id="pp3">**명제 3**</ins> Lie group $G$가 주어졌다 하고, 집합 $\mathfrak{g}$를 $G$ 위에서 정의된 left invariant vector field들의 모임이라 하자.

1. $\mathfrak{g}$의 모든 원소는 $C^\infty$이다.
2. $\mathfrak{g}$는 $\mathbb{R}$-벡터공간이며, 임의의 $X\in\mathfrak{g}$에 대해 $X\mapsto X_e$로 정의된 함수 $\alpha$는 두 벡터공간 $\mathfrak{g}$와 $T_eG$ 사이의 isomorphism을 정의한다.
3. $\mathfrak{g}$는 Lie algebra 구조를 갖는다.

</div>
<details class="proof" markdown="1">
<summary>증명</summary>



</details>

위의 명제의 2번에 의하여, $G$가 Lie group이라면 $T_eG$는 $\mathbb{R}$-벡터공간일 뿐만 아니라, $\mathfrak{g}$에서 정의된 Lie bracket $[-,-]$을 bijection $\alpha$를 통해 옮겨와서 Lie algebra로 취급할 수도 있다.

<div class="definition" markdown="1">

<ins id="df4">**정의 4**</ins> 임의의 Lie group $G$에 대하여, $G$ 위에 정의된 left invariant vector field들의 모임 $\mathfrak{g}$를 $G$의 Lie algebra라 부른다. 

</div>

이와 같이, 임의로 주어진 Lie group $G$에 해당하는 Lie group은 동일한 알파벳의 프락투어 소문자로 적는다. 

이번에는 Lie group $G$ 위에 differential form $\omega$가 정의되었다 하자. 그럼 $L_g$의 pullback $L_g^\ast$에 의해 $L_g^\ast$가 정의된다. Vector field의 경우와 마찬가지로, 모든 $g\in G$에 대하여 다음의 식

$$L_g^\ast \omega=\omega$$

가 성립할 경우, $\omega$가 *left invariant*라고 한다. 명시적으로, 만일 $\omega$가 $k$-form이었다면, 좌변은 $k$개의 vector field $X_i\in\mathfrak{X}(G)$, 그리고 임의의 점 $h\in G$에 대하여

$$(L_g^\ast\omega)(X_1,\ldots, X_k)(h)=\omega_{gh}((dL_g)_h(X_1)_h,\ldots, (dL_g)_h(X_k)_h)$$

으로 정의되는 $k$-form이 된다. 

다음은 위의 [명제 3](#pp3)의 form에서의 analogue이다.

<div class="proposition" markdown="1">

<ins id="pp5">**명제 5**</ins> Lie group $G$가 주어졌다 하고, $\Omega_\text{inv}^\ast(G)$를 $G$ 위에서 정의된 left invariant differential form들의 모임이라 하자.

1. $\Omega_\text{inv}^\ast(G)$의 모든 원소는 $C^\infty$이다.
2. $\Omega\_\text{inv}^\ast(G)$는 $\Omega^\ast(G)$의 subalgebra이며, 임의의 $\omega\in\Omega\_\text{inv}^\ast(G)$에 대해 $\omega\mapsto \omega\_e$으로 정의된 함수 $\beta$는 두 벡터공간 $\Omega\_\text{inv}^\ast(G)$와 $\bigwedge(T\_e^\ast G)$ 사이의 isomorphism을 정의한다.

</div>
<details class="proof" markdown="1">
<summary>증명</summary>



</details>

2번 결과에 의하여, $\Omega\_\text{inv}^1(G)$는 $T_e^\ast G$에 대응되고, 따라서 $\mathfrak{g}^\ast$으로 생각할 수도 있다.

$\mathfrak{g}$의 basis $(X\_i)\_{i=1}^m$이 주어졌다 하자. 그럼 이들의 dual basis $(\xi^i)\_{i=1}^m$은 $\Omega\_\text{inv}^1(G)$의 basis가 된다. 이제

$$[X_i,X_j]=\sum_k c_{ijk}X_k$$

라 하면, [정의 2](#df2)의 두 식으로부터 다음의 두 식

$$c_{ijk}+c_{jik}=0,\qquad\sum_m(c_{ijm}c_{mkn}+c_{jkm}c_{min}+c_{kim}c_{mjn})=0$$

이 성립한다는 것을 알 수 있다. 한편, [§미분형식, 명제 5](/ko/math/manifold/differential_forms#pp5)로부터 

$$d\omega(X,Y)=-\omega[X,Y]$$

가 항상 성립하므로, 

$$d\xi_k(X_i, X_j)=-\xi_k[X_i,X_j]=-c_{ijk}$$

으로부터

$$d\xi_k=\sum_{i < j}c_{ijk}\xi_j\wedge\xi_i$$

을 얻는다.


## 동형사상

모든 구조를 정의한 후에는 그들 사이의 homomorphism을 정의해야 한다. Lie group은 group인 동시에 manifold이기도 하므로 이들 사이의 homomorphism은 $C^\infty$인 group homomorphism으로 정의하는 것이 옳을 것이고, Lie algebra의 경우 단순히 곱셈이 bracket으로 주어진 algebra이므로 대수적인 정의를 그대로 사용하면 될 것이다.

<div class="definition" markdown="1">

<ins id="df6">**정의 6**</ins> 두 Lie group $G,H$에 대하여, $F:G\rightarrow H$가 *Lie group homomorphism*이라는 것은 $F$가 $C^\infty$이고, 동시에 group homomorphism인 것이다. 

비슷하게, 두 Lie algebra $\mathfrak{g},\mathfrak{h}$에 대하여, $F:\mathfrak{g}\rightarrow\mathfrak{h}$가 *Lie algebra homomorphism*이라는 것은 $F$가 linear map인 동시에, 모든 $X,Y$에 대해 $F([X,Y])=[F(X), F(Y)]$를 만족하는 것이다.

$F$가 Lie group homomorphism, 혹은 Lie algebra homomorphism이고, 그 역함수가 잘 정의되며 이 또한 Lie group homomorphism 혹은 Lie algebra homomorphism이라면, $F$를 Lie group isomorphism, 혹은 Lie algebra isomorphism이라 부른다.

</div>

Lie group $G,H$와 그들에 대응되는 Lie algebra들 $\mathfrak{g},\mathfrak{h}$가 주어졌다 하고, $C^\infty$ 함수 $F:M\rightarrow N$을 생각하자. [§벡터장, 정의 5](/ko/math/manifold/vector_fields#df5)를 정의하기 전에 우리는 $X\in\mathfrak{X}(G)$을 $F$를 통해 $H$으로 옮기는 방법이 완전하지 않다는 것을 살펴보았다. 하지만, $X$를 $\mathfrak{X}(G)$ 대신 $\mathfrak{g}$에서 고른다면 이것이 가능해진다.

<div class="proposition" markdown="1">

<ins id="pp7">**명제 7**</ins> 두 Lie group $G,H$ 사이의 homomorphism $F:G\rightarrow H$가 주어졌다 하고, 이들의 Lie algebra $\mathfrak{g},\mathfrak{h}$를 생각하자. 그럼 $dF(X)$는 $X$와 $F$-related인 $\mathfrak{h}$의 원소이며, 이러한 원소는 유일하다. 따라서 Lie algebra homomorphism $dF:\mathfrak{g}\rightarrow\mathfrak{h}$가 잘 정의된다.

</div>
<details class="proof" markdown="1">
<summary>증명</summary>



</details>

역으로 Lie algebra homomorphism $\phi:\mathfrak{g}\rightarrow\mathfrak{h}$가 주어졌을 때, $dF=\phi$이도록 하는 $F:G\rightarrow H$가 존재하는지의 여부도 자연스러운 질문일 것이다. 만일 $G$가 simply connected라면 이것이 참이며, 뿐만 아니라 이를 만족하는 $F$ 또한 유일하다.






---

**참고문헌**

**[War]** Frank W. Warner. *Foundations of Differentiable Manifolds and Lie Groups*, Graduate texts in mathematics, Springer, 2013  
**[Lee]** John M. Lee. *Introduction to Smooth Manifolds*, Graduate texts in mathematics, Springer, 2012  

---

[^1]: Sophus Lie, 노르웨이의 수학자 (1842-1899).