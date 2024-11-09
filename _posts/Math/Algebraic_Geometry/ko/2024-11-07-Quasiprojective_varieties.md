---

title: "준사영다양체"
excerpt: ""

categories: [Math / Algebraic Geometry]
permalink: /ko/math/algebraic_geometry/quasiprojective_varieties
header:
    overlay_image: /assets/images/Math/Algebraic_Geometry/Quasiprojective_varieties.png
    overlay_filter: 0.5
sidebar: 
    nav: "algebraic_geometry-ko"

date: 2024-11-07
last_modified_at: 2024-11-07
weight: 3

---

## 사영공간의 정의

임의의 $(n+1)$차원 $\mathbb{k}$-벡터공간 $V$에 대하여, $V$의 projectivization $\mathbb{P}(V)$를 생각하자. 그럼 $V$의 좌표 $\xi_0,\ldots, \xi_n$은 $\mathbb{P}(V)$에서의 homogeneous coordinate $(\xi_0:\cdots:\xi_n)$을 주며, 정의에 의해 임의의 $\lambda\in \mathbb{k}^\times$에 대하여 $(\xi_0:\cdots:\xi_n)$과 $(\lambda\xi_0:\cdots:\lambda\xi_n)$는 같은 점을 나타낸다. 

편의상 $V$의 좌표 $\xi_0,\ldots,\xi_n$을 고정하여 $\mathbb{P}(V)$를 $\mathbb{P}^n$으로 취급하자. 우리가 이번 글에서 처음으로 할 일은 $\mathbb{P}^n$에서 [§대수적 집합](/ko/math/algebraic_geometry/algebraic_sets)에서와 유사한 이론을 전개하는 것이다. 이를 위해서는 다항식 $f\in \mathbb{k}[\X_0,\ldots, \X_n]$에 대하여 $Z(f)$를 정의하는 것으로 시작해야 하는데, 이를 위해서는 다소 주의해야 할 것이, $\mathbb{P}^n$의 한 점에는 대응되는 여러 개의 표현이 존재하므로 $Z(f)$는 이러한 표현의 선택에 의존하지 않고 $0$이 되어야 한다는 것이다. 즉 다음과 같이 정의한다.

<div class="definition" markdown="1">

<ins id="def1">**정의 1**</ins> 다항식 $f\in \mathbb{k}[\X_0,\ldots, \X_n]$가 $\xi\in \mathbb{P}^n$에서 죽는다는 것은 $\xi$의 임의의 homogeneous coordinate $(\xi_0:\cdots:\xi_n)$에 대하여 $f(\xi_0,\ldots,\xi_n)=0$이 성립하는 것이다.

</div>

그럼 특히 임의의 $\lambda\in \mathbb{k}^\times$에 대하여 $f(\lambda\xi_0,\ldots,\lambda\xi_n)=0$이 성립해야 한다. 한편, $f$가 $\xi$에서 죽는다 하고 $f$를 degree별로 쪼개어 $f=f_0+f_1+\cdots+ f_r$이라 하자. 그럼

$$0=f(\lambda\xi_0,\ldots,\lambda\xi_n)=f_0(\xi_0,\ldots, \xi_n)+\lambda f_1(\xi_0,\ldots,\xi_n)+\cdots+\lambda^r f_r(\xi_0,\ldots,\xi_n)$$

이 성립한다. 그럼 $\mathbb{k}$는 algebraically closed이므로 무한집합이고, 따라서 각각의 $f_i$들이 모두 $\xi$에서 죽어야 한다는 것을 안다.

<div class="definition" markdown="1">

<ins id="def2">**정의 2**</ins> $\mathbb{P}^n$의 부분집합 $X$가 닫혀있다는 것은 $X$의 점들이 정확히 유한히 많은 다항식들 $f_1,\ldots, f_m$들이 죽는 점들로 이루어진 것이다. 

</div>

그럼 $X$는 $\mathbb{k}[\X_0,\ldots, \X_n]$의 ideal $I(X)$를 정의하며, 위의 논의로부터 $I(X)$는 *homogeneous* ideal인 것을 안다. 물론, 반대로 $\mathbb{k}[\X_0,\ldots, \X_n]$의 임의의 homogeneous ideal은 $\mathbb{P}^n$의 closed subset $X$를 정의한다. 

## 아핀공간과 사영공간

[정의 2](#def2)를 따라 $\mathbb{P}^n$의 closed subset을 정의할 때에는 다소 주의해야 할 점이 있다. [§대수적 집합, ⁋따름정리 6](/ko/math/algebraic_geometry/algebraic_sets#cor6)에서 살펴본 대응을 따르면, 우리는 $\mathbb{P}^n$의 closed subset과 homogeneous radical ideal들 사이에 일대일대응이 있기를 바라지만 이는 일반적으로 참이 아니라는 것이다. 

<div class="definition" markdown="1">

<ins id="def3">**정의 3**</ins> 임의의 graded ring $A=\bigoplus_{i=0}^\infty A_i$에 대하여, $A$의 *irrelevant ideal* $A_+$를 $A_+=\bigoplus_{i=1}^\infty A_i$으로 정의한다. 

</div>

가령 $A=\mathbb{k}[\X_0,\ldots, \X_n]$라면 $A_+=(\X_0,\ldots,\X_n)$이다. 만일 다항식들 $f_1,\ldots, f_m$들로 만들어진 ideal이 $A_+$를 포함한다면, $Z(A_+)=\emptyset$이 된다. 즉 $\mathbb{P}^n$의 닫힌집합 $\emptyset$에 대응되는 ideal이 $(1)$을 제외하고도 존재한다. 따라서, 그 radical이 irrelevant ideal을 포함하는 ideal들을 우리의 논의대상에서 제외시킬 필요가 있다. 

<div class="proposition" markdown="1">

<ins id="lem4">**보조정리 4**</ins> $A=\mathbb{k}[\X_0,\ldots, \X_n]$의 homogeneous ideal $\mathfrak{a}$가 공집합에 대응되는 것은 $\mathfrak{a}$가 ideal $\bigoplus_{i=s}^\infty A_i$를 포함하는 것과 동치이다.

</div>

$\mathbb{P}^n$ 위에 정의된 다항식 $\X_i=0$으로 주어지는 닫힌집합을 생각하자. 그럼 이 닫힌집합의 여집합은 $\mathbb{P}^n$의 점들 $(\xi_0:\cdots:\xi_n)$ 가운데 $\xi_i\neq 0$을 만족하는 점들의 집합이며, 이는 다음의 대응

$$\xi=(\xi_0:\cdots:\xi_n)\mapsto \left(\frac{\xi_0}{\xi_i},\ldots, \widehat{\frac{\xi_i}{\xi_i}},\ldots, \frac{\xi_n}{\xi_0}\right)\in U_i=\mathbb{A}^n$$

을 통해 $U_i=\mathbb{A}^n$과 일대일대응에 있다. 또, 이러한 $U_i$들이 $\mathbb{P}^n$의 cover가 됨도 자명하다. 

이제 $\mathbb{P}^n$ 위에 있는 임의의 닫힌집합 $X$에 대하여, $X$는 다음 교집합

$$X_i=X\cap U_i$$

을 통해 정의된 $U_i$의 부분집합들 $X_i$들을 모은 것으로 생각할 수 있다. 만일 $X$가 degree $d$짜리 homogeneous equation $F=0$ 하나로 정의된다면, $\xi_i\neq 0$을 만족하는 $X$의 점들에 대해서는 다음 식

$$F(\xi_0,\ldots, \xi_n)=\xi_i^dF\left(\frac{\xi_0}{\xi_i},\ldots, \frac{\xi_{i-1}}{\xi_i}, 1,\frac{\xi_{i+1}}{\xi_i}\ldots, \frac{\xi_n}{\xi_0}\right)$$

으로부터 $X_i$는 $U_i$ 위에서 다음 식

$$F(\x_0, \ldots, \x_{i-1}, 1, \x_{i+1}, \ldots, \x_n)=0$$

으로 정의된 $\mathbb{k}[\x_0, \ldots, \hat{\x}_i, \ldots, \x_n]$의 함수의 zero set으로 볼 수 있다. 즉 $X_i$는 $U_i$의 닫힌집합이며 그 방정식 또한 어렵지 않게 구할 수 있다. 이를 $X$의 $U_i$에서의 *affine piece*라 부른다. 

한편 affine space $\mathbb{A}^n$ 안의 closed set $U$가 주어졌다 하자. 그럼 $\mathbb{A}^n$을 $\mathbb{P}^n$ 안에 $U_0$으로 들어가 있는 것처럼 생각한 후, $U$의 $\mathbb{P}^n$에서의 closure를 취하여 $\overline{U}\subseteq \mathbb{P}^n$을 얻을 수 있으며, 이 때

$$U=\overline{U}\cap \mathbb{A}_0^n$$

이 성립한다. 

<div class="definition" markdown="1">

<ins id="def5">**정의 5**</ins> Closed projective set의 open subset을 *quasiprojective variety<sub>준사영다양체</sub>*라 부른다. 

</div>

그럼 위의 논의로부터, 임의의 closed affine set은 quasiprojective variety임을 알고, closed projective set은 자명한 이유로 quasiprojective variety임을 안다. 따라서 앞으로는 quasiprojective variety에 대한 이론을 전개하기로 한다. 

## 그라스만 다양체

위에서의 맥락과는 별개로 projective variety의 중요한 예시 하나를 소개하며 이 글을 마친다. 

<div class="example" markdown="1">

<ins id="ex6">**예시 6 (Grassmannian)**</ins> 위에서 정의한 projective space $\mathbb{P}(V)$는 $V$의 1차원 subspace들을 parametrize하는 기하적인 대상으로 생각할 수 있다. 즉, vector space $V$의 1차원 부분공간들을 받아 $\mathbb{P}(V)$의 한 점에 대응시키는 자연스러운 방법이 존재한다.  

이를 일반화하여 다음과 같이 Grassmannian을 정의한다. 이는 앞으로도 많이 쓰이는 예시이므로, 혼동을 방지하기 위해 $V$가 $n$차원 $\mathbb{k}$-벡터공간이고, $e_1,\ldots, e_n$이 $V$의 basis라고 고정하자. 그럼 $\Gr(r, V)$는 $V$의 $r$차원 부분공간을 parametrize하는 기하적인 대상이며, 이번 예시의 목적은 이것이 $\mathbb{P}(\bigwedge^r V)$의 적당한 closed subset이 된다는 것을 보이는 것이다. 

$\mathbb{k}$-벡터공간 $V$의 $r$차원 부분공간 $W$가 주어질 때마다, $W$의 아무 basis $w_1,\ldots, w_r$을 받아온 후 이들의 wedge product

$$w_1\wedge\cdots\wedge w_r\in \bigwedge^r V$$

를 생각하자. 이 대응은 물론 $W$의 basis의 선택에 의존하지만, $W$의 basis를 다르게 잡더라도 결과적으로 나오는 $\bigwedge^r V$의 원소는 오직 상수배 만큼의 차이밖에 나지 않는다. 즉, 이 과정을 통해 $W$를 받아 $w_1\wedge\cdots\wedge w_r$을 내놓는 대응은, 그 공역을 $\mathbb{P}(\bigwedge^r V)$로 잡아주면 잘 정의된 대응이 된다. 

한편, $V$의 basis $e_1,\ldots, e_n$을 고정하면  $\bigwedge^r V$의 basis는 

$$e_{i_1}\wedge\cdots\wedge e_{i_r},\qquad i_1\lt i_2\lt \cdots\lt i_r$$

들로 주어지는 것을 알고 있다. ([\[다중선형대수학\] §텐서대수, ⁋명제 13](/ko/math/multilinear_algebra/tensor_algebras#prop13)) 이로부터 위의 $w_1\wedge w_r$을 

$$w_1\wedge\cdots\wedge w_r=\sum_{i_1\lt\cdots\lt i_r} p_{i_1\cdots i_r} e_{i_1}\wedge\cdots\wedge e_{i_r}$$

으로 적을 수 있다. 이렇게 얻어지는 $p_{i_1\cdots i_r}$들을 $W$의 *Plücker coordinate*라고 부르며, 이는 $W$를 나타내는 $\mathbb{P}(\bigwedge^r V)$의 점의 homogeneous coordinate로 생각할 수 있다. 이렇게 $\Gr(r, V)$를 $\mathbb{P}(\bigwedge^r V)$의 subset으로 보는 embedding $P$를 *Plücker embedding*이라고 한다. 

이제 $P$의 image가 closed set임을 보여야 한다. 이를 위해서는 $P$를 나타내는 식을 유도해야 한다. 즉, 임의의 $x\in \bigwedge^r V$가 주어졌을 때, 적당한 $f_1,\ldots, f_r\in V$에 대하여 $x=f_1\wedge\cdots \wedge f_r$로 쓸 수 있는지의 여부를 판별하는 (동차)식이 필요하며, 이 식의 zero set이 $\Gr(r,V)$를 정의하는 식이 될 것이다. 이는 *Plücker relation*이라고 부르는 다음의 식들

$$\sum_{k=1}^{r+1}(-1)^k p_{i_1\cdots i_{r-1}j_k}p_{j_1\cdots\hat{j}_k\cdots j_{r+1}}=0,\qquad i_1\lt\cdots\lt i_{r-1},\quad j_1\lt\cdots\lt j_{r+1}$$

으로 주어진다는 사실이 잘 알려져 있다. 

특별히 $\dim V=4$이고 $r=2$인 경우를 생각하자. 그럼 $\bigwedge^2V$의 basis는

$$e_1\wedge e_2,\quad e_1\wedge e_3,\quad e_1\wedge e_4, \quad e_2\wedge e_3, \quad e_2\wedge e_4,\quad e_3\wedge e_4$$

이며, 이 basis에 대한 임의의 $x\in \mathbb{P}(\bigwedge^2V)$의 좌표가 $p_{ij}$들이라 한다면 위의 Plücker relation은 하나의 식

$$-p_{12}p_{34}+p_{13}p_{24}-p_{14}p_{23}=0$$

을 준다. 

</div>
