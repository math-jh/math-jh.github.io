---

title: "유리함수"
excerpt: "두 다양체 사이의 유리사상"

categories: [Math / Algebraic Geometry]
permalink: /ko/math/algebraic_geometry/rational_functions
header:
    overlay_image: /assets/images/Math/Algebraic_Geometry/Rational_functions.png
    overlay_filter: 0.5
sidebar: 
    nav: "algebraic_geometry-ko"

date: 2024-12-04
last_modified_at: 2024-12-04
weight: 3

---

앞서 우리는 [§다양체 사이의 사상, ⁋정의 7](/ko/math/algebraic_geometry/morphisms#def7)을 정의하며 variety의 open subset에서 정의된 함수는 이미 충분히 많은 정보를 가지고 있다는 것을 확인했다. 따라서 우리는 $K(X)$의 원소들에도 다음과 같이 이름을 붙여주고, 이들이 주는 정보를 더 살펴볼 수 있다.

<div class="definition" markdown="1">

<ins id="def1">**정의 1**</ins> 임의의 variety $X$에 대하여, function field $K(X)$의 원소들을 *rational function<sub>유리함수</sub>*이라 부른다. 

</div>

이제 regular function ([§다양체 사이의 사상, ⁋정의 1](/ko/math/algebraic_geometry/morphisms#def1))으로부터 regular map ([§다양체 사이의 사상, ⁋정의 3](/ko/math/algebraic_geometry/morphisms#def3))을 정의했듯, rational function으로부터 rational map을 정의할 수 있다. 그 전에 다음 보조정리를 보이자.

<div class="proposition" markdown="1">

<ins id="lem2">**보조정리 2**</ins> 두 variety $X,Y$와 이들 사이의 morphism $\varphi, \psi: X \rightarrow Y$에 대하여, $\varphi\vert_U=\psi\vert_U$를 만족하는 공집합이 아닌 열린집합 $U$가 존재한다 하자. 그럼 $\phi=\psi$가 성립한다. 

</div>

그럼 다음을 정의하는 것이 말이 된다.

<div class="definition" markdown="1">

<ins id="def3">**정의 3**</ins> 두 variety $X,Y$에 대하여, *rational map<sub>유리사상</sub>* $\varphi:X \rightarrow Y$는 다음 순서쌍

$$(U, \varphi\vert_U),\qquad\text{$U$ nonempty open, $\varphi\vert_U$ a morphism of $U$ to $Y$}$$

들의 모임에, 동치관계

$$(U,\varphi\vert_U)\sim (V,\varphi\vert_V)\iff\text{$\varphi\vert_U$ and $\varphi\vert_V$ agree on $U\cap V$}$$

를 주어 정의되는 동치류이다. 만일 $\varphi$의 어떤 representative $(U,\varphi)$에 대하여 $\varphi\vert_U$의 image가 $Y$에서 dense라면, $\varphi$를 *dominant*라 말한다.

</div>

위의 정의에서의 표기 $\varphi\vert_U$는 다소 오해를 불러일으킬 수 있는데, 이는 $X$ 전체에서 정의된 함수 $\varphi:X \rightarrow Y$를 $U$로 제한시켜 얻어지는 것이 <em_ko>아니다</em_ko>. Rational map이 정의되는 곳들을 모두 합하여도 $X$ 전체가 되지는 않을 수도 있다. 이 때문에 rational map $\varphi$를 표현할 때는 $\varphi:X \dashrightarrow Y$와 같이 쓴다. 

한편 두 dominant rational map은 합성이 가능하며, 따라서 variety들을 object로, dominant rational map을 morphism으로 갖는 category가 존재한다. 이 category에서의 isomorphism을 *birational map*이라 부른다. 

이제 다음이 성립한다.

<div class="proposition" markdown="1">

<ins id="thm4">**정리 4**</ins> 두 variety $X,Y$에 대하여, 다음의 bijection

$$\{\text{dominant rational maps from $X$ to $Y$}\}\leftrightarrow\{\text{$\mathbb{k}$-algebra homomorphisms from $K(Y)$ to $K(X)$}\}$$

이 존재하며, 이 대응을 통해 위에서 정의한 birational category와, finitely generated field extension들 사이의 (contravariant) categorical equivalence가 존재한다.

</div>

이 때, 임의의 dominant rational map $\varphi: X\dashrightarrow Y$에 대하여, 여기에 대응되는 $K(Y) \rightarrow K(X)$는 임의의 $f\in K(Y)$를 받아 $f^{-1}\circ\varphi\in K(X)$를 주는 함수이다. 반대방향을 보이기 위해서는 우선, 임의의 variety $Y$가 open affine subset들로 덮일 수 있다는 것을 보여 $Y$가 affine인 경우로 한정지어 생각할 수 있다. 만일 $A(Y)$의 generator를 $\y_1,\ldots, \y_n$이라 적는다면, 주어진 $\mathbb{k}$-algebra homomorphism $K(Y) \rightarrow K(X)$을 통해 이들 $\y_1,\ldots, \y_n$들을 $K(X)$에서의 rational map으로 보고, 이들의 정의역을 모두 포함하는 단일한 $X$의 열린집합 $U$를 받아 이 $\mathbb{k}$-algebra homomorphism $A(Y) \rightarrow \mathscr{O}(U)$를 정의할 수 있으며, [§다양체 사이의 사상, ⁋정리 10](/ko/math/algebraic_geometry/morphisms)에 의해 이것이 $U$에서 $Y$로의 map을 정의하는 것을 안다. 이것이 dominant rational map을 주며, [정리 4](#thm4)에서 언급된 모든 결과를 만족하는 것을 쉽게 보일 수 있다. 

특히 다음이 성립한다.

<div class="proposition" markdown="1">

<ins id="cor5">**따름정리 5**</ins> 두 variety $X,Y$에 대하여, $X$와 $Y$가 birationally equivalent한 것과 $K(X)\cong K(Y)$인 것이 동치이다. 

</div>

<div class="example" markdown="1">

<ins id="ex6">**예시 6**</ins> Variety $\mathbb{A}^n\times \mathbb{P}^{n-1}$에 대하여, $\mathbb{A}^n$의 좌표를 $\x_1,\ldots, \x_n$, $\mathbb{P}^{n-1}$의 좌표를 $\y_1,\ldots, \y_n$이라 쓰자. 그럼 $\mathbb{A}^n\times \mathbb{P}^{n-1}$의 닫힌집합들은 $\x_i$들과 $\y_j$로 이루어진 polynomial 중, $\y$ 변수들은 모두 동차인 것들의 해집합으로 나타나는 것들이다. 특히 다음의 집합

$$\{\x_i\y_j=\y_i\x_j: i,j=1,\ldots,n\}$$

은 $\mathbb{A}^n\times \mathbb{P}^{n-1}$의 닫힌집합 $X$를 정의한다. 이제 합성

$$\varphi: X \hookrightarrow \mathbb{A}^n\times \mathbb{P}^{n-1} \rightarrow \mathbb{A}^n$$

를 원점에서의 $X$의 *blowup<sub>확대</sub>*이라 부른다. 이제 $\varphi$와 $X$의 성질을 살펴보자. 

우선 원점이 아닌 $x=(x_1,\ldots, x_n)\in \mathbb{A}^n$에 대하여, 일반성을 잃지 않고 $x_1\neq 0$이라 하면 다음 식

$$y_j=(x_j/x_1)y_1$$

이므로, 가령 $y_1=x_1$로 잡는다면 위의 식이 $\mathbb{P}^{n-1}$의 점

$$[x_1:x_2:\cdots:x_n]\in \mathbb{P}^{n-1}$$

을 지정할 것이다. 즉 $\varphi^{-1}(x)$는 정확히 한 점이다. 뿐만 아니라 $\varphi$가 $X\setminus \varphi^{-1}(0)$에서 $\mathbb{A}^n\setminus 0$으로의 isomorphism을 유도하는 것을 안다. 한편 원점에 대해서는 $\varphi^{-1}(0)=\mathbb{P}^{n-1}$임이 자명하다. 

이제 원점을 지나는 $\mathbb{A}^n$의 직선 $L$이 다음 식

$$\x_i=a_it, \qquad\text{$(a_1,\ldots, a_n)\neq (0,\ldots,0)$, $t\in \mathbb{A}^1$}$$

으로 주어졌다 하자. 그럼 $L$의 $\varphi$에 의한 preimage는 우선 원점을 제외한 점, 즉 $t\neq 0$일 때의 $(x_1,\ldots, x_n)$의 점은 하나의 점

$$(a_1t,\ldots, a_nt, a_1,\ldots, a_n)\in X\subseteq \mathbb{A}^n\times \mathbb{P}^{n-1}$$

으로 정해지며, $t=0$일 때에는 방금 구한 $L\setminus 0$의 preimage에 closure를 취하면

$$(0,\ldots, 0, a_1,\ldots, a_n)\in X\subseteq \mathbb{A}^n\times \mathbb{P}^{n-1}$$

이 되어야 한다는 것을 안다. 뿐만 아니라 $X$는 irreducible인데, 이는 $X\setminus \varphi^{-1}(0)$의 경우는 $\mathbb{A}^n\setminus 0$과 isomorphic하므로 irreducible이고, 여기에 추가되는 점들인 $\varphi^{-1}(0)$은 위의 결과에서 알 수 있듯 $X\setminus\varphi^{-1}(0)$의 적절한 부분집합의 closure에 속하기 때문이다. 

</div>

위의 [예시 6](#ex6)을 바탕으로 다음을 정의한다.

<div class="definition" markdown="1">

<ins id="def7">**정의 7**</ins> 원점을 지나는 $\mathbb{A}^n$의 closed subvariety $X$에 대하여, $0$에서의 $X$의 *blowup<sub>확대</sub>*을 $\tilde{X}=\cl(\varphi^{-1}(X\setminus 0))$으로 정의하고, $\Bl_0X$와 같이 적는다. 

</div>