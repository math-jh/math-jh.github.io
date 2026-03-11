---

title: "다양체 사이의 사상"
excerpt: "두 다양체 사이의 정칙사상"

categories: [Math / Algebraic Geometry]
permalink: /ko/math/algebraic_geometry/morphisms
header:
    overlay_image: /assets/images/Math/Algebraic_Geometry/Morphisms.png
    overlay_filter: 0.5
sidebar: 
    nav: "algebraic_geometry-ko"

date: 2024-12-17
last_modified_at: 2024-12-17
weight: 2

---

이제 우리는 다양체들 사이의 사상에 대해 살펴본다. 앞으로 별다른 혼동의 여지가 없을 때에는 $\mathbb{A}^n_\mathbb{k}$와 $\mathbb{P}^n_\mathbb{k}$를 각각 $\mathbb{A}^n$과 $\mathbb{P}^n$으로 줄여쓰기로 한다. 

## 정칙사상

<div class="definition" markdown="1">

<ins id="def1">**정의 1**</ins> Quasi-affine variety $X\subseteq \mathbb{A}^n$에 대하여, 함수 $f:X \rightarrow \mathbb{k}$가 점 $x$에서 *regular<sub>정칙</sub>*라는 것은 $x$의 적당한 열린근방 $U$와 다항식 $g,h\in A=\mathbb{k}[\x_1,\ldots, x_n]$이 존재하여 $U$ 위에서는 $h$가 $0$이 되는 점이 존재하지 않고, $U$ 위에서는 $f=g/h$로 적을 수 있는 것이다. 만일 $f$가 $X$의 모든 점에서 regular라면 이를 간단히 *regular function*이라 부른다. 

</div>

그럼 다음이 성립한다.

<div class="proposition" markdown="1">

<ins id="lem2">**보조정리 2**</ins> Regular function $f:X \rightarrow \mathbb{k}$에 대하여, $\mathbb{k}$를 affine line $\mathbb{A}^1$로 위상구조를 부여하면 $f$는 연속함수이다. 

</div>

Quasi-projective variety 위의 regular function 또한 정의할 수 있는데, 이를 위해서는 우선 $S=\mathbb{k}[\x_0,\ldots, \x_n]$이 $\mathbb{P}^n$ 위의 함수를 정의하지 못했던 것을 기억하자. 설령 $Z(f)$를 정의하기 위해 $S$의 동차다항식들로만 우리의 관심을 한정지어도 다음 식

$$f(\lambda x_0,\ldots, \lambda x_n)=\lambda^d f(x_0,\ldots, x_n)\qquad\text{for any $\lambda\neq 0$ and any $x\in \mathbb{A}^{n+1}$}$$

에 의해 $f$의 해집합만이 잘 정의되며, $f$의 함숫값 자체는 잘 정의되지 않았다. 반면, regular function을 [정의 1](#def1)과 유사하게 정의하면 이번에는 그 함숫값까지도 잘 정의된다.

<div class="definition" markdown="1">

<ins id="def3">**정의 3**</ins> Quasi-projective variety $X\subseteq \mathbb{P}^n$에 대하여, 함수 $f:X \rightarrow \mathbb{k}$가 점 $x$에서 *regular<sub>정칙</sub>*라는 것은 $x$의 적당한 열린근방 $U$와, <em_ko>같은 차수의</em_ko> 동차다항식 $g,h\in S=\mathbb{k}[\x_0,\ldots, x_n]$이 존재하여 $U$ 위에서는 $h$가 $0$이 되는 점이 존재하지 않고, $U$ 위에서는 $f=g/h$로 적을 수 있는 것이다. 만일 $f$가 $X$의 모든 점에서 regular라면 이를 간단히 *regular function*이라 부른다. 

</div>

그럼 [보조정리 2](#lem2)는 quasi-affine variety 뿐만이 아니라, quasi-projective variety에 대해서도 성립한다. 정의에 의해 지금까지 정의한 모든 종류의 variety들 (affine variety, quasi-affine variety, projective variety, quasi-projective variety)는 모두 quasi-projective variety이다. 때문에 quasi-projective variety를 그냥 *variety*라 부르기로 하자.

<div class="definition" markdown="1">

<ins id="def4">**정의 4**</ins> 임의의 두 variety $X,Y$에 대하여, $X$에서 $Y$로의 *morphism* $\varphi:X \rightarrow Y$는 임의의 열린집합 $V\subseteq Y$와 임의의 regular function $f:V \rightarrow \mathbb{k}$에 대하여 함수 $f\circ\varphi:\varphi^{-1}(V) \rightarrow \mathbb{k}$가 regular이도록 하는 연속함수를 의미한다.

</div>

예를 들어 이전 글의 말미에서 정의한 $\varphi_i:U_i \rightarrow \mathbb{A}^n$은 

## 함수환

이제 다음을 정의하자.

<div class="definition" markdown="1">

<ins id="def5">**정의 5**</ins> Variety $X$에 대하여, $\mathscr{O}(X)$를 $X$ 위에 정의된 모든 regular function들의 ring으로 정의한다. 또, 임의의 $x\in X$에 대하여 $\mathscr{O}_{X,x}$를 $x$에서의 $X$의 *local ring<sub>국소환</sub>*이라 부르고, 이를 $x$ 근방의 regular function들의 germ들의 모임으로 정의한다. ([\[위상수학\] §준층, ⁋정의 9](/ko/math/topology/presheaves#def9))

</div>

즉 $\mathscr{O}_{X,x}$의 원소들은 다음 순서쌍들의 집합

$$\{(U, f):\text{$U$ is an open neighborhood of $x$, $f$ is a regular function on $U$}\}$$

들의 모임 위에, 다음의 동치관계

$$(U, f)\sim (V,g)\iff\text{$f=g$ on $U\cap V$}$$

를 주어 정의되는 동치류들이다.

그럼 특히 $\mathscr{O}_{X,x}$는 그 이름답게 local ring이 된다.

<div class="proposition" markdown="1">

<ins id="lem6">**보조정리 6**</ins> 임의의 variety $X$와 $x\in X$에 대하여, $\mathscr{O}_{X,x}$는 local ring이다. 

</div>

이는 $\mathscr{O}\_{X,x}$의 유일한 maximal ideal $\mathfrak{m}\_x$가 non-unit들의 모임, 즉 $f(x)=0$을 만족하는 regular function들의 모임으로 이루어져있기 때문에 자명하다. 그럼 evaluation map에 의하여 $\mathscr{O}\_{X,x}/\mathfrak{m}\_x\cong \mathbb{k}$임이 자명하다. 

<div class="definition" markdown="1">

<ins id="def7">**정의 7**</ins> 임의의 variety $X$에 대하여, $X$의 *function field<sub>함수체</sub>* $K(X)$를 다음 집합

$$\{(U, f):\text{$U$ open, $f$ is a regular function on $U$}\}$$

들의 모임 위에, 다음의 동치관계

$$(U, f)\sim (V,g)\iff\text{$f=g$ on $U\cap V$}$$

를 통해 정의된 quotient field이다. 

</div>

직관적으로 $[(U,f)]$를 $K(X)$의 원소로 볼 때는 $X\setminus U$를 $f$가 정의되지 않는 (더 엄밀하게는, 정의되지 않을 수도 있는) 집합으로 보면 된다. 그러나 정의에 의해 $X$는 irreducible이므로, $U$는 반드시 $X$의 dense subset이다. ([\[위상수학\] §차원, ⁋명제 7](/ko/math/topology/dimension#prop7)) 즉, 이러한 상황에서 이렇게 $f$가 정의되지 않는 점들의 집합은 매우 작다. 뿐만 아니라 이들 원소들의 곱과 합이 잘 정의되는데, 이는 $K(X)$의 두 원소 $[(U,f)]$와 $[(V, g)]$에 대하여 $U\cap V$가 [\[위상수학\] §차원, ⁋명제 7](/ko/math/topology/dimension#prop7)에 의하여 공집합이 아닌 열린집합이 되므로, 

$$[(U, f)]+[(V, g)]=[(U\cap V, f+g)],\qquad [(U,f)]\cdot[(V,g)]=[(U\cap V,fg)]$$

으로 정의하면 되기 때문이다. 한편 임의의 원소 $[(U,f)]$에 대하여 $Z(f)$는 닫힌집합이므로 $V=U\setminus U\cap Z(f)$는 열린집합이고 따라서 $[(V, 1/f)]$가 $[(U,f)]$의 곱셈에 대한 역원이 된다. 

이제 임의의 variety $X$에 대하여, $\mathscr{O}(X)$의 임의의 원소 $f$는 다음 함수

$$\mathscr{O}(X) \rightarrow \mathscr{O}_{X,x};\qquad f\mapsto (X,f)$$

를 통해 $\mathscr{O}\_{X,x}$의 원소로 볼 수 있고, $\mathscr{O}\_{X,x}$의 임의의 원소 $[(U,f)]$는 다음 함수

$$\mathscr{O}_{X,x} \rightarrow K(X);\qquad [(U,f)]\mapsto [(U,f)]$$

를 통해 $K(X)$임을 안다. 이들은 모두 injective이므로, $\mathscr{O}(X)$와 $\mathscr{O}_{X,x}$를 모두 $K(X)$의 subring으로 생각해도 큰 문제가 없다. 

한편 우리는 variety로부터 그 위에 정의된 함수들의 ring을 얻어내는 방법을 이미 하나 알고 있는데, coordinate ring이 그것이다. 방금 정의한 $\mathscr{O}(X)$와 이들 사이에도 관계가 있다.

<div class="proposition" markdown="1">

<ins id="thm8">**정리 8**</ins> Affine variety $X\subseteq \mathbb{A}^n$과 $X$의 coordinate ring $A(X)$에 대하여 다음이 성립한다.

1. $\mathscr{O}(X)\cong A(X)$이다.
2. 각각의 $x\in X$와, 점 $x$에서 함숫값이 $0$이 되는 $\mathscr{O}(X)$의 원소들로 이루어진 ideal $\mathfrak{m}_x$를 생각하자. 그럼 $x\mapsto \mathfrak{m}_x$는 $X$의 점들과 $A(X)$의 maximal ideal들 사이의 일대일대응을 준다.
3. 각각의 $x\in X$에 대하여, $\mathscr{O}\_{X,x}\cong A(X)_{\mathfrak{m}_x}$이 성립하고, 따라서 $\dim \mathscr{O}\_{X,x}=\dim X$이다.
4. $K(X)\cong \Frac A(X)$가 성립한다.

</div>

한편 위의 정리는 projective variety에 대해서는 조금 다르게 작동한다. 

<div class="proposition" markdown="1">

<ins id="thm9">**정리 9**</ins> Projective variety $X\subseteq \mathbb{P}^n$과 $X$의 coordinate ring $S(X)$에 대하여 다음이 성립한다.

1. $\mathscr{O}(X)\cong \mathbb{k}$이다.
2. 각각의 $x\in X$와, 점 $x$에서 함숫값이 $0$이 되는 homogeneous한 $S(X)$의 원소들로 이루어진 ideal $\mathfrak{m}_x$를 생각하자. 그럼 $\mathscr{O}\_{X,x}=S(Y)\_{\mathfrak{m}_x}$이 성립한다.
3. $K(X)\cong S(X)\_{((0))}$이다.

</div>

여기에서 사용된 homogeneous localization은 [\[가환대수학\] §등급환의 국소화, ⁋정의 4](/ko/math/commutative_algebra/localization_of_graded_rings#def4)에서 정의하였다.

그럼 다음이 성립한다.

<div class="proposition" markdown="1">

<ins id="thm10">**정리 10**</ins> Variety $X$와 affine variety $Y$가 주어졌다 하자. 그럼 다음의 natural isomorphism

$$\Hom_\Var(X,Y)\cong \Hom_{\Alg{k}}(A(Y), \mathscr{O}(X))$$

이 존재한다. 

</div>