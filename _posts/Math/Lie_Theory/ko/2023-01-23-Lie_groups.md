---

title: "리 군"
excerpt: "Lie group의 정의와 성질"

categories: [Math / Lie Theory]
permalink: /ko/math/Lie_theory/Lie_groups
header:
    overlay_image: /assets/images/Math/Lie_theory/Lie_groups.png
    overlay_filter: 0.5
sidebar: 
    nav: "Lie_theory-ko"

date: 2023-01-23
last_modified_at: 2025-11-06
weight: 1

---

이 카테고리의 글들에서 우리는 Lie group과 Lie algebra에 대한 내용을 담는다. Lie group의 정의는 아주 간단한 것이다. 

<div class="definition" markdown="1">

<ins id="def1">**정의 1**</ins> Group $G$가 *Lie group<sub>리 군</sub>*이라는 것은 $G$가 그 자체로 manifold 구조를 가지고 있으며, 이 manifold 구조에 대하여 다음의 함수

$$G\times G\rightarrow G;\qquad (x,y)\mapsto xy^{-1}$$

가 $C^\infty$인 것이다. 

</div>

즉, Lie group은 그 자체로 group이며, 동시에 이 group을 정의하는 두 연산, multiplication과 inverse를 smooth이도록 하는 미분구조가 주어진 smooth manifold이다. 더 일반적으로 우리는 group의 연산들이 연속이도록 하는 위상공간을 *topological group*이라 부르지만, 이러한 일반화가 당장 필요한 것은 아니다. 

그럼 두 Lie group $G, H$ 사이의 morphism은 smooth map $f:G \rightarrow H$가 동시에 group homomorphism인 것을 의미한다. 이들 데이터는 category $\LieGrp$을 정의하며 여기에서의 isomorphism의 개념 또한 자명하다.

다음은 Lie group의 예시들이다. 

<div class="example" markdown="1">

<ins id="ex2">**예시 2**</ins> 임의의 유한차원 $\mathbb{R}$-벡터공간 $\mathbb{R}^n$은 덧셈을 연산으로 갖는 Lie group이 된다. 이는 다음의 함수 

$$\mathbb{R}^n \times \mathbb{R}^n\rightarrow \mathbb{R}^n;\quad (\mathbf{x},\mathbf{y})\mapsto \mathbf{x}-\mathbf{y}$$

이 smooth이므로 자명하다. 

</div>

<div class="example" markdown="1">

<ins id="ex3">**예시 3**</ins> $1$-torus $S^1$은 이를 $\mathbb{C}$의 multiplicative subgroup

$$S^1=\left\{z\in \mathbb{C}\mid \lvert z\rvert=1\right\}$$

으로 보면 Lie group이 된다. 더 일반적으로 임의의 Lie group $G, H$에 대하여 $G\times H$ 또한 Lie group이 되는 것을 쉽게 보일 수 있으므로, 임의의 $n$-torus

$$T^n=(S^1)^n$$

는 Lie group이다. 예를 들어, $T^2$는 항등원 역할을 할 한 점과 그 점을 지나는 적도방향 대원, 이와 수직인 방향의 대원을 <em_ko>축</em_ko>으로 갖는 벡터공간처럼 행동하며, 이는 다음의 isomorphism

$$\mathbb{R}/\mathbb{Z}\rightarrow S^1;\quad t\mapsto e^{2\pi i t}$$

으로부터 얻어지는 것이다. 

</div>

위의 두 예시보다 조금 더 복잡하고 많이 쓰이는 예시는 다음의 예시이다.

<div class="example" markdown="1">

<ins id="ex4">**예시 4**</ins> 임의의 $n\times k$ 행렬들의 공간 $\Mat_{n\times k}(\mathbb{R})$는 $nk$차원 벡터공간이며, 동시에 smooth manifold이다. 이제 특별히 $n\times n$ 행렬들의 공간을 생각하면, 이 행렬 위에 정의된 smooth function $\det:\Mat_{n\times n}(\mathbb{R})\rightarrow \mathbb{R}$은 다음의 open submanifold

$$\GL(n; \mathbb{R}) =\left\{A\in \Mat_{n\times n}(\mathbb{R})\mid \det(A)\neq 0\right\}$$

를 정의한다. 이제 이 위에는 행렬들의 곱셈과 역원이 잘 정의되며 이 때 행렬곱은 다항함수에 불과하고, 역원은 분모가 $0$이 되지 않는 유리함수에 불과하다. 즉, $\GL(n; \mathbb{R})$은 곱셈을 연산으로 갖는 Lie group이며, 원래의 manifold $\Mat_{n\times n}(\mathbb{R})$이 $n^2$차원이므로 $\GL(n; \mathbb{R})$의 차원 또한 그러하다.

이제 다시 $\det:\GL(n; \mathbb{R})\rightarrow \mathbb{R}^\times$를 생각하면, 우리는 다음의 식

$$\SL(n;\mathbb{R})=\left\{A\in \GL(n; \mathbb{R})\mid \det(A)=1\right\}$$

을 통해 $\GL(n;\mathbb{R})$의 부분집합 $\SL(n; \mathbb{R})$을 정의할 수 있다. 이 함수는 행렬의 각 성분들에 대한 다항함수이므로 smooth이고, 약간의 계산을 통해 모든 점에서 regular임을 알 수 있다. [\[미분다양체\] §음함수 정리, ⁋따름정리 4](/ko/math/manifold/implicit_function_theorem#cor4)로부터 $\SL(n;\mathbb{R})$은 $n^2-1$차원 manifold가 된다. 이 때 $\GL(n;\mathbb{R})$의 곱셈과 역원 또한 $\SL(n;\mathbb{R})$로 잘 제한되며 따라서 $\SL(n; \mathbb{R})$ 또한 Lie group이다. 

비슷한 방식으로, classical matrix group들 $\Omat(n)$, $\SO(n)$, $\Umat(n)$, $\SU(n)$ 등의 matrix group들 또한 Lie group 구조를 갖는 것을 확인할 수 있다. 

</div>

한편, 비록 determinant가 어떻게 생겼는지는 알지 못하더라도, $\SL(n;\mathbb{R})$이 group으로서 어떻게 생겼는지에 대한 정보는 선형대수학으로부터 나오는 것이다. 임의의 Lie group $G$에 대한 다음의 정리는 더 일반적으로 임의의 *closed* subgroup은 항상 embedded submanifold라는 것을 보여준다.

<div class="proposition" markdown="1">

<ins id="thm5">**정리 5**</ins> Lie group $G,H$가 주어졌다 하고, 이들의 Lie algebra $\mathfrak{g},\mathfrak{h}$ 사이의 homomorphism $L:\mathfrak{g} \rightarrow \mathfrak{h}$이 주어졌다 하자. 만일 $G$가 simply connected라면, $dF=L$을 만족하는 homomorphism $F:G \rightarrow H$가 유일하게 존재한다.

</div>

## 리 대수

위에서 언급한 것과 같이, Lie group의 개념 자체는 꽤나 단순한 것이다. 그렇다면 Lie group이 가지는 흥미로운 성질들은 이들이 어떻게 상호작용하는지에 대한 것이다. 가장 단순한 결과 중 하나는 Lie group의 경우, 자기 자신으로의 nontrivial한 diffeomorphism을 찾는 것이 쉽다는 것이다. 

<div class="definition" markdown="1">

<ins id="def6">**정의 6**</ins> Lie group $G$와, $G$의 임의의 원소 $g\in G$에 대하여, $g$에 의한 *left translation* $L_g$는

$$L_g:G\rightarrow G;\qquad x\mapsto gx$$

으로 정의된 $C^\infty$ 함수이다. 비슷하게, right translation $R_g$는

$$R_g:G\rightarrow G;\qquad x\mapsto xg$$

으로 정의된다.

</div>

이들은 Lie group homomorphism은 아니지만 정의에 의하여 smooth map이고, 그 inverse는 각각 $L_{g^{-1}}$과 $R_{g^{-1}}$로 주어지므로 diffeomorphism이다. 

우리는 Lie group과 그 위에 정의된 벡터장을 다룰 때 이러한 left translation들에 의해 보존되는 벡터장들에만 관심이 있다. 즉 다음을 정의한다.

<div class="definition" markdown="1">

<ins id="def7">**정의 7**</ins> Lie group $G$ 위에 정의된 벡터장 $X$에 대하여, $X$가 *left invariant*라는 것은 $X$가 자기 자신과 $L_g$-related인 것이다.

</div>

즉, 다음의 식

$$d(L_g)\circ X=X\circ L_g$$

이 성립하는 것이며, 더 명시적으로는 임의의 $p\in G$에 대하여

$$\left(d(L_g)\right)(X_p)=X_{gp}$$

이 항상 성립하는 것이다. 위의 식으로부터, $G$ 위에 정의된 left invariant인 벡터장 $X$를 명시하기 위해서는 <em_ko>오직 하나의 점</em_ko> $p\in G$에서의 값 $X_p$만 알면 충분하다는 것을 알 수 있으며, 당연하게도 가장 평범한 $p$의 선택은 $G$의 항등원 $e$이다. 또, 각 점에서의 $X$의 값이 이러한 방식으로 정의되었기 때문에, $X$가 left-invariant라는 사실이 $X$의 smoothness를 줄 것이라는 것도 추측할 수 있다. 

바꿔말하면, $G$ 위에서 정의된 left-invariant vector field는 정확하게 $G$의 identity에서의 tangent space $T_eG$와 같은 것이다. 한편 [\[미분다양체\] §리 미분, ⁋정의 5](/ko/math/manifold/Lie_derivative#def5)에서 우리는 $\mathfrak{X}(G)$를 $C^\infty(G)$-algebra가 되도록 하는 연산 $[-,-]$를 정의했는데, 그렇다면 left-invariant vector field들의 모임이 이 연산에 대한 subalgebra가 되는지 또한 우리의 의문 중 하나이다. 우선 $[-,-]$를 일반화하는 다음의 정의부터 생각하자. 

<div class="definition" markdown="1">

<ins id="def8">**정의 8**</ins> $\mathbb{R}$-벡터공간 $\mathfrak{g}$가 $\mathbb{R}$ 위에 정의된 *Lie algebra<sub>리 대수</sub>*라는 것은 이 위에 다음의 두 조건

1. (anticommutativity) $[x,y]=-[y,x]$,
2. (Jacobi identity) $[[x,y],z]+[[y,z],x]+[[z,x],y]=0$

을 만족하는 *Lie bracket<sub>리 브라켓</sub>* $[-,-]:\mathfrak{g}\times\mathfrak{g}\rightarrow\mathfrak{g}$가 정의된 것이다.

</div>

그럼 다음 명제가 성립한다. 

<div class="proposition" markdown="1">

<ins id="prop9">**명제 9**</ins> Lie group $G$가 주어졌다 하고, $\mathfrak{g}$를 $G$ 위에서 정의된 모든 left invariant vector field들의 모임이라 하자. 

1. $\mathfrak{g}$는 $\mathbb{R}$-벡터공간이며, $\alpha:\mathfrak{g} \rightarrow T_eG$ 를 다음의 식
     
    $$\alpha(X)=X_e$$
    
    으로 정의하면 $\alpha$는 isomorphism이 된다.
2. 임의의 $X\in\mathfrak{g}$는 $C^\infty$이다.
3. 임의의 $X,Y\in\mathfrak{g}$에 대하여, $X$와 $Y$의 Lie bracket$[X,Y]$ 또한 left-invariant이고, 따라서 $\mathfrak{g}$는 $\mathbb{R}$ 위에서 정의된 Lie algebra가 된다.

</div>
<details class="proof" markdown="1">
<summary>증명</summary>

1. 벡터장들의 덧셈과 스칼라곱에 대하여 $\mathfrak{g}$가 $\mathbb{R}$-벡터공간이 된다는 것은 자명하고, 또 $\alpha$가 linear map이라는 것 또한 자명하다. 이제 $\alpha$가 isomorphism임을 보여야 하는데, $T_eG$는 유한차원 벡터공간이므로 $\alpha$가 전단사임을 보이면 충분하다. 우선 $\alpha(X)=\alpha(Y)$를 만족하는 두 $X,Y\in\mathfrak{g}$가 존재한다 가정하면, 임의의 $g\in G$에 대하여
  
    $$X_g=(dL_g)_e(X_e)=(dL_g)_e(Y_e)=Y_g$$

    이므로 $X=Y$이다. 거꾸로 임의의 $v\in T_eG$에 대하여 $X_g$를 $(dL_g)_e(v)$으로 정의하면 $X$가 left invariant인 벡터장이고, $\alpha(X)=v$를 만족함이 자명하다. 
2. $X\in\mathfrak{g}$가 $C^\infty$임을 보이기 위해서는 임의의 함수 $f$에 대하여 $Xf$가 $C^\infty$임을 보이면 충분하다. ([\[미분다양체\] §벡터장, ⁋명제 2](/ko/math/manifold/vector_fields#prop2)) 한편 임의의 $p\in G$에 대하여, 
    
    $$(Xf)(p)=X_pf=(dL_p)_e(X_e)f=X_e(f\circ L_p)$$
    
    이므로 이는 다시 함수 $p\mapsto X_e(f\circ L_p)$가 $C^\infty$를 보이는 문제와 같다. $G$의 곱셈을 $m:G\times G\rightarrow G$로 쓰고, $G$에서 $G\times G$로의 자연스러운 두 embedding을

    $$\iota_1^p: x\mapsto (x,p),\qquad \iota_2^p:x\mapsto (p,x)$$

    으로 적고, $Y_e=X_e$를 만족하는 $C^\infty$ 벡터장을 택하여 $G\times G$ 위에 정의된 새로운 벡터장 $(0,Y)$을 생각하자. 그럼 $f\circ m$은 $C^\infty$ 함수이고 $(0,Y)$는 $C^\infty$ 벡터장이므로 $(0,Y)(f\circ m)$은 $C^\infty$ 함수가 되고, 따라서 합성 $\bigl((0,Y)(f\circ m)\bigr)\circ\iota_1^e$ 또한 $C^\infty$이다. 그런데 임의의 $p\in G$에 대하여, isomorphism

    $$T_{(x,y)}(M\times N)\cong T_xM\oplus T_yN$$

    을 통하면

    $$\begin{aligned}\bigl((0,Y)(f\circ m)\bigr)(\iota_1^e(p))&=(0,Y)_{(p,e)}(f\circ m)=0_p(f\circ m\circ\iota_1^e)+Y_e(f\circ m\circ\iota_2^p)\\&=X_e(f\circ m\circ\iota_2^p)=X_e(f\circ L_p)\end{aligned}$$

    이므로 원하는 결과를 얻는다.
3. [\[미분다양체\] §리 미분, ⁋명제 9](/ko/math/manifold/Lie_derivative#prop9)에 의하여 자명하다.

</details>

위의 과정을 통해 얻어진 Lie algebra $\mathfrak{g}$를 *$G$의 Lie algebra*라 부른다. 일반적으로 Lie group을 $G$라 적으면, 이에 해당하는 프락투어 소문자 $\mathfrak{g}$를 통해 $G$의 Lie algebra를 적는 것이 보통이다. 

특별한 예시로, 임의의 manifold $M$에서 자기자신으로의 diffeomorphism들의 group $\Diff(M)$을 생각하면, 이는 무한차원 Lie group으로 생각할 수 있다. 이 Lie group의 identity $\id_M$에서의 tangent space는 $\id_M$을 지나는 $\Diff(M)$의 curve들의 적당한 equivalence class이며, 이 때 [\[미분다양체\] §벡터장, ⁋정리 6](/ko/math/manifold/vector_fields#thm6)을 생각하면 이 정보는 정확하게 $\mathfrak{X}(M)$에 담겨있다. 이러한 방식으로 Lie group $G$의 Lie algebra $\mathfrak{g}$는 $G$가 자기 자신 위에 act할 때의 infinitisimal action을 정의한다.

<div class="example" markdown="1">

<ins id="ex10">**예시 10**</ins> 앞선 [예시 2](#ex2), [예시 3](#ex3), 그리고 [예시 4](#ex4)의 $\GL(n;\mathbb{R})$의 경우는 모두 벡터공간으로부터 오므로, 이들의 tangent space는 각각 원래의 벡터공간과 isomorphic하다. 즉 $\mathbb{R}^n$의 경우 그 tangent space는 $\mathbb{R}^n$ 자기자신이며, 비슷하게 $n$-torus $S^n\cong \mathbb{R}^n/\mathbb{Z}^n$의 경우 각 점에서의 tangent space는 quotient topology를 취하기 전인 $\mathbb{R}^n$과 같다. $\GL(n;\mathbb{R})$의 경우, 벡터공간 $\Mat_n(\mathbb{R})$의 open submanifold이므로 마찬가지로 각 점에서의 tangent space는 $\Mat_n(\mathbb{R})$과 같다.

</div>

그러나 $\SL(n;\mathbb{R})$의 Lie algebra를 알기 위해서는 조금 더 복잡한 계산이 필요하다. 구체적으로 우리는 determinant map $\GL(n; \mathbb{R})\rightarrow \mathbb{R}$의 미분을 알아야 한다. 

## 행렬 지수함수

$\mathbb{R}$ 위에 정의된 임의의 유한차원 벡터공간에 norm을 정의하는 방법은 위상적으로는 유일하며, 이렇게 정의된 norm은 $\mathbb{R}$의 completeness에 의하여 complete metric을 정의한다. 특히 $\Mat_n(\mathbb{R})$에 operator norm을 줄 경우 다음의 식

$$\lVert XY\rVert\leq\lVert X\rVert\lVert Y\rVert$$

이 성립하므로, 이 사실들을 종합하면 임의의 $X\in\Mat_n(\mathbb{R})$에 대하여 다음의 *matrix exponential*

$$\exp(X)=\sum_{i=0}^\infty\frac{X^k}{k!}$$

이 잘 정의된다는 것을 알 수 있다. 

다음 명제는 기본적으로 선형대수학과 미적분학의 결과이다.

<div class="proposition" markdown="1">

<ins id="prop11">**명제 11**</ins> 임의의 $X\in\Mat_n(\mathbb{R})$에 대하여 

$$\frac{d}{dt}\exp(tX)=X\exp(tX)=\exp(tX)X$$

이 성립한다.

</div>

일반적으로, 행렬의 곱은 commutative가 아니므로 다음의 식

$$\exp(A)\exp(B)=\exp(A+B)$$

은 성립하지 <em_ko>않는다</em_ko>. 그러나 만일 두 행렬 $A,B$가 commute한다면 이 식은 성립하고, 특히 다음의 계산

$$\exp(tX)\exp(-tX)=\exp(tX-tX)=\exp(O)=I$$

으로부터 $\exp(tX)$는 항상 역행렬을 갖는다는 것을 안다. 즉, 다음의 곡선

$$t\mapsto \exp(tX)$$

은 $\GL(n; \mathbb{R})$에서의 곡선이며, $t=0$에서의 이 곡선의 미분은

$$\frac{d}{dt}\exp(tX)\bigg\vert_{t=0}=X$$

임이 앞선 명제에 의해 자명하다. 이를 기하적으로 설명하자면, 위의 곡선은 $I=\exp(O)$에서의 임의의 tangent vector

$$X\in T_I\GL(n;\mathbb{R})=\Mat_n(\mathbb{R})$$

이 주어졌을 때, $t\mapsto \exp(tX)$이 점 $I$에서 그 속도가 $X$이도록 하는 곡선임을 의미한다. 

이제 $\SL(n;\mathbb{R})$의 tangent vector를 찾는 것은, 이 곡선이 (적어도 짧은 시간동안은) $\SL(n;\mathbb{R})$에 머물도록 하는 행렬들 $X$을 추려내는 것과 같다. 이를 위해서는 다음의 명제를 사용할 수 있다.

<div class="proposition" markdown="1">

<ins id="prop12">**명제 12**</ins> 임의의 $X\in\Mat_n(\mathbb{R})$에 대하여 $\det(\exp X)=\exp(\tr X)$이 성립한다. 

</div>

이 또한 기초적인 선형대수를 이용하여 해결할 수 있다. 그럼 

$$\det(\exp tX)=\exp(\tr(tX))=\exp(t\cdot\tr X)$$

로부터, 이를 만족하는 $X$는 정확히 $\tr X=0$을 만족해야 함을 안다. 즉 $\SL(n;\mathbb{R})$의 tangent space는 $\tr X=0$을 만족하는 행렬들이며 이 조건은 $n^2-1$차원 벡터공간을 정의한다. 

다음은 앞서 살펴본 left-invariant vector field의 일반화이다. 

<div class="definition" markdown="1">

<ins id="def13">**정의 13**</ins> Lie group $G$ 위에 정의된 form $\omega$가 *left invariant*라는 것은 임의의 $g\in G$에 대하여 $(dL_g)\omega=\omega$가 성립하는 것이다. $G$ 위에 정의된 left invariant $k$-form들의 모임은 $\Omega_\text{l.inv}^k(G)$로 적고, $G$ 위에 정의된 모든 left invariant form들의 모임은 $\Omega_\text{l.inv}^\ast(G)$으로 적는다.

</div>

특별히 $\Omega_\text{l.inv}^1(G)$의 원소들은 *Maurer-Cartan form*이라 부른다.

[명제 9](#prop9)과 마찬가지 방식으로 다음 명제를 증명할 수 있다.
    
<div class="proposition" markdown="1">

<ins id="prop14">**명제 14**</ins> Lie group $G$와 $\Omega_\text{l.inv}^\ast(G)$에 대하여 다음이 성립한다.

1. $\Omega_\text{l.inv}^\ast(G)$의 임의의 원소는 $C^\infty$이다. 
2. $\Omega_\text{l.inv}^\ast(G)$는 $\Omega^\ast(G)$의 $C^\infty(G)$-subalgebra이며, 함수 $\omega\mapsto\omega_e$는 $\Omega_\text{l.inv}^\ast(G)$에서 $\bigwedge(T_e^\ast G)$로의 $C^\infty(G)$-algebra isomorphism이다.
3. 임의의 $\omega\in\Omega_\text{l.inv}^1(G)$와 left invariant인 벡터장 $X$에 대하여, $\omega(X)$는 $G$ 위에서 정의된 상수함수이다.
4. 임의의 $\omega\in\Omega_\text{l.inv}^1(G)$와 $X,Y\in\mathfrak{g}$에 대하여 
    
    $$d\omega(X,Y)=-\omega[X,Y]$$

    이 성립한다.
5. $\mathfrak{g}$의 basis $X_1,\ldots, X_d$와 그 dual basis $\omega_1,\ldots,\omega_d$에 대하여, 다음의 식
    
    $$[X_i,X_j]=\sum_{k=1}^d c_{ij}^kX_k$$

    을 만족하는 $d^3$개의 상수들 $c_{ij}^k$이 존재한다. 이들은 다음 두 조건

    $$c_{ij}^k+c_{ji}^k=0,\qquad\sum_r (c_{ij}^rc_{rk}^s+c_{jk}^rc_{ri}^s+c_{ki}^rc_{rj}^s)=0\quad\text{for all $s$}$$

    을 만족하며, 따라서 다음의 식

    $$d\omega_i=\sum_{j < k} c_{jk}^i\omega_k\wedge\omega_j$$

    이 성립한다.

</div>

## 리 대응

임의의 manifold에 대하여, 그 tangent space를 위와 같이 곡선의 germ으로 생각할 수 있다. 따라서 우리는 임의의 Lie group $G$와 그 Lie algebra $\mathfrak{g}$에 대하여, $\mathfrak{g}$의 원소가 주어질 때마다 $G$의 곡선을 대응시켜줄 수 있다. 이러한 방식으로 Lie algebra는 Lie group에 대한 모든 정보를 보여줄 수 있다. 더 정확히 말하자면, 이렇게 곡선을 통해 $G$의 정보를 읽어오기 위해서는 곡선을 대응시키는 방법이 (up to homotopy) 유일해야하고, 존재해야 할 것이므로 Lie algebra는 simply connected Lie group에 대한 모든 정보를 가지고 있다. 이 섹션에서 우리는 이 대응관계를 조금 더 자세히, 그러나 증명은 생략하고 실펴보기로 한다.

리 대응은 다음과 같은 종류의 Lie group-Lie algebra 사이의 관계에 대한 결과들의 모임이다. 

<div class="proposition" markdown="1">

<ins id="thm15">**정리 15**</ins> 다음이 성립한다.

1. Lie group $G,H$가 주어졌다 하고, 이들의 Lie algebra $\mathfrak{g},\mathfrak{h}$ 사이의 homomorphism $L:\mathfrak{g} \rightarrow \mathfrak{h}$이 주어졌다 하자. 만일 $G$가 simply connected라면, $dF=L$을 만족하는 homomorphism $F:G \rightarrow H$가 유일하게 존재한다.
2. 임의의 유한차원 real Lie algebra $\mathfrak{g}$에 대하여, $\mathfrak{g}$를 Lie algebra로 갖는 simply connected Lie group $G$가 존재한다. 

</div>

즉, 바꾸어 말하자면 $\LieGrp$에서 $\LieAlg$로의 functor $\Lie:\LieGrp \rightarrow \LieAlg$는, simply connected Lie group들로 이루어진 $\LieGrp$의 full subcategory로 제한했을 때 두 category의 equivalence를 준다. 

Category-theoretic한 결과 외에도 이 정리는, 가령, 임의의 Lie group $G$와 그 Lie algebra $\mathfrak{g}$에 대하여 matrix exponential과 비슷한 exponential map을 정의할 수 있도록 해 준다. 이는 $(\mathbb{R},+)$이 1차원 simply connected Lie group이므로 그 Lie algebra 또한 1차원이고, 따라서 여기에서 다른 Lie algebra로의 Lie algebra homomorphism은 basis $d/dt$가 어디로 가는지에 의해 유일하게 결정되미 이 때 $d/dt$가 $X\in \mathfrak{g}$로 옮겨진다면 이 Lie algebra homomorphism에 [정리 15](#thm15)을 적용하여 얻어지는 Lie group homomorphism $\gamma: \mathbb{R}\rightarrow G$이 원하는 곡선을 정의하기 때문이다. 

<div class="definition" markdown="1">

<ins id="def16">**정의 16**</ins> 임의의 Lie group $G$와 그 Lie algebra $\mathfrak{g}$, 그리고 원소 $X\in \mathfrak{g}$에 대하여, 위의 과정을 통해 얻어지는 곡선을 $\gamma_X$로 표기하자. 그럼 $\exp:\mathfrak{g}\rightarrow G$를 $X\mapsto \gamma_X(1)$로 정의한다.

</div>

특별히 $G$가 위에서 살펴본 것과 같이 matrix Lie group일 경우 우리는 이 정의가 matrix exponential을 준다는 것을 확인할 수 있다. 

직관적으로 Lie algebra는 Lie group에 대한 정보를 exponential을 사용하여 읽어온다. 이것이 Lie group에 대한 정보를 알고 있다고 하기 위해서는 우리는 Lie group의 group operation에 대한 정보를 적어도 국소적으로는 복원해낼 수 있어야 한다. 이는 다음의 결과로부터 얻어진다.

<div class="proposition" markdown="1">

<ins id="thm17">**정리 17 (Baker-Campbell-Hausdorff)**</ins> Lie group $G$와 그 Lie algebra $\mathfrak{g}$, $X,Y\in \mathfrak{g}$에 대하여, 다음의 식

$$\exp(X)\exp(Y)=\exp\left(X+Y+\frac{1}{2}[X,Y]+\frac{1}{12}[X,[X,Y]]+\frac{1}{12}[Y,[Y,X]]+\cdots\right)$$

이 성립한다.

</div>

엄밀히 말하자면 위의 "정리"는 $\cdots$에 해당하는 항의 계수에 대한 정보가 없기는 하지만 이 계수들이 구체적으로 필요할 일은 드물다. 중요한 것은 Lie algebra의 원소 $X,Y$가 지정하는 방향의 두 (Lie group의) 원소를 각각 곱하였을 때 이들의 곱이 $X,Y$의 일차결합과 그 Lie bracket들의 합에 해당하는 방향이며, 만일 $X,Y$가 충분히 작은 벡터들이라면 이 급수 또한 수렴한다는 것이다. 한편 Lie group $G$에서, identity $e$와 가까운 임의의 원소는 $g=\exp(X)$의 꼴로 쓸 수 있으므로 이 정리는 (identity 근처에서) $G$의 group operation에 대한 정보를 정확하게 모두 담고 있다. 더 구체적으로, 우리는 Lie algebra $\mathfrak{g}$를 manifold로 보고, $\exp: \mathfrak{g}\rightarrow G$를 manifold 사이에서의 smooth map이라 생각할 수 있고 이 때 $0\in \mathfrak{g}$에서의 differential이 정확히 $\id_\mathfrak{g}$가 된다. 따라서 $\mathfrak{g}$에서 $0$의 적당한 neighborhood $U$가 존재하여 $\exp$가 $U$와 $\exp(U)$ 사이의 diffeomorphism을 정의하도록 할 수 있겠으나 (특히 local diffeomorphism의 inverse $\log$가 존재하겠지만), 이 $U$ 바깥에서 exponential map이 어떻게 행동할지는 단언할 수 없다. 

위의 [정리 15](#thm15)를 알게 되었을 때, 자연스러운 질문 중 하나는 Lie group $G$와 그 Lie algebra $\mathfrak{g}$, 그리고 $\mathfrak{g}$의 Lie subalgebra $\mathfrak{h}$가 주어졌을 때, $\mathfrak{h}$를 identity에서의 tangent space로 갖는 $G$의 Lie subgroup $H$가 존재하는지의 여부일 것이다. 그런데 정의에 의해 Lie subalgebra는 Lie bracket에 의해 닫혀있으므로 [\[미분다양체\] §Distribution, ⁋정리 3](/ko/math/manifold/distribution#thm3)에 의해 이는 $G$의 submanifold를 정의한다. 이들은 위의 [정리 17](#thm17)에 의해 group operation도 가질 것이지만, 문제는 이 정리는 앞서 지적했듯 오직 국소적인 영역에서만 효과가 있다는 것이다. 그러나, 만일 $G$가 simply connected였다면 이를 $G$ 전체로 확장하는 데에 위상적인 문제가 없어지므로 다음 정리가 성립한다. 

<div class="proposition" markdown="1">

<ins id="thm18">**정리 18**</ins> Simply connected Lie group $G$와 그 Lie algebra $\mathfrak{g}$, 그리고 $\mathfrak{g}$의 Lie subalgebra $\mathfrak{h}$가 주어졌을 때, $\mathfrak{h}$를 Lie algebra로 갖는 $G$의 Lie subgroup $H$가 존재한다. 

</div>

## 가환 리 군의 분류

이제 우리는 마지막으로 abelian Lie group의 classification을 한다. 정의에 의해 abelian Lie group은 그 group operation이 commutative인 것들을 뜻한다. 이제 우리는 inner automorphism

$$\rho_g: G \rightarrow G; \quad h\mapsto \rho_g(h)=ghg^{-1}$$

을 생각하자. ([\[대수적 구조\] §군의 작용, ⁋명제 9](/ko/math/algebraic_structures/group_actions#prop9)) 이는 Lie group automorphism이며, 따라서 identity $h=e$에서 이를 미분하면 $d\rho_g: \mathfrak{g}\rightarrow \mathfrak{g}$를 얻으며 이는 Lie albebra automorphism이 된다. 

<div class="definition" markdown="1">

<ins id="def19">**정의 19**</ins> Lie group $G$에 대하여, 다음의 대응

$$\Ad:G\rightarrow \Aut(\mathfrak{g});\quad g\mapsto d\rho_g$$

을 $G$의 *adjoint representation*이라 부른다. 이를 미분하여 얻어지는 

$$\ad: \mathfrak{g}\rightarrow \Lie(\Aut(\mathfrak{g})$$

을 $\mathfrak{g}$의 *adjoint representation*이라 부른다. 

</div>

그럼 정의에 의해 충분히 작은 범위 내에서 $G$의 adjoint representation은 정확하게 Lie derivative를 보는 것과 같고, 따라서 [\[미분다양체\] §리 미분, ⁋명제 4](/ko/math/manifold/Lie_derivative#prop4)에 의하여 다음의 식

$$\ad(X)Y =[X,Y]$$

이 성립한다. 뿐만 아니라 다음이 성립한다.

<div class="proposition" markdown="1">

<ins id="thm20">**정리 20**</ins> Connected compact Lie group $G$에 대하여 다음이 성립한다.

1. $d(\exp(e))=\id_\mathfrak{g}$
2. $\Ad\circ\exp=\exp_{\GL(\mathfrak{g})}\circ \ad$
3. $\rho_x\circ\exp=\exp\circ\Ad(x)$

</div>

만일 $G$가 abelian group이었다면 $\rho_g$는 그냥 identity map이고 따라서 $\Ad_g(X)=X$가 임의의 $g\in G$와 임의의 $X\in \mathfrak{g}$에 대해 성립하고, 따라서 그 미분인 $\mathfrak{g}$의 adjoint representation은 $0$이다. 즉, 임의의 abelian Lie group에 대하여, 그 Lie algebra의 Lie bracket은 항상 $0$이고 우리는 이를 *abelian* Lie algebra라 부른다. 이는 [정의 8](#def8)에 의해 anticommutative인 Lie bracket이 commutative이기도 하기 위한 유일한 방법이므로 그 이름이 어색하지 않다. 

그럼, $G$가 abelian일 경우 특히 [정리 17](#thm17)에 의하여 $\exp(X+Y)=\exp(X)\exp(Y)$이 성립한다. 즉 $\exp$는 group homomorphism이다. 뿐만 아니라 이 경우 [정리 17](#thm17)의 우변 $\exp$ 안의 식은 반드시 수렴하며 이는 ($G$가 conencted일 경우) $\exp$가 *surjective* group homomorphism이라는 결과로 나타난다. 따라서, first isomorphism theorem에 의하여

$$G\cong \mathfrak{g}/\ker(\exp)$$

이다. 이제 $\mathfrak{g}$는 $n$차원 $\mathbb{R}$-벡터공간이고, $\exp$가 local diffeomorphism이므로 $\ker(\exp)$는 *discrete* additive subgroup이 된다. 이는 $\mathbb{Z}^k$라는 사실이 잘 알려져있으며 따라서 

$$G\cong \mathfrak{g}/\ker(\exp)\cong \mathbb{R}^n/\mathbb{Z}^k\cong T^k\times \mathbb{R}^{n-k}$$

이다. 즉, connected abelian Lie group은 반드시 torus와 $\mathbb{R}^k$의 곱이며, 특히 compact connected abelian Lie group은 반드시 torus이다.

---

**참고문헌**

**[War]** Frank W. Warner. *Foundations of Differentiable Manifolds and Lie Groups*, Graduate texts in mathematics, Springer, 2013  

---