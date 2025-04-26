---

title: "스킴 사이의 사상"
excerpt: ""

categories: [Math / Algebraic Geometry]
permalink: /ko/math/algebraic_geometry/morphism_of_schemes
header:
    overlay_image: /assets/images/Math/Algebraic_Geometry/Morphism_of_schemes.png
    overlay_filter: 0.5
sidebar: 
    nav: "algebraic_geometry-ko"

date: 2025-02-19
last_modified_at: 2025-02-19
weight: 7

---

정의에 의해 $\Sch$는 $\LRS$의 full subcategory이다. ([§스킴, ⁋정의 1](/ko/math/algebraic_geometry/schemes#def1)) 즉 두 scheme $X,Y$가 주어졌을 떄, $X$에서 $Y$로의 scheme morphism은 연속함수 $\varphi: X \rightarrow Y$와 structure sheaf 사이의 morphism $\varphi^\sharp: \mathscr{O}\_Y \rightarrow \varphi_\ast \mathscr{O}\_X$으로 주어지며, 이 때 $\varphi^\sharp$는 각각의 stalk으로 제한하였을 때 local homomorphism이 되어야 한다. ([§아핀스킴, ⁋정의 2](/ko/math/algebraic_geometry/affine_schemes#def2)) 

위와 같이 scheme morphism $f:X \rightarrow Y$은 기본적으로 이미 우리가 정의했던 대상이다. 다음 글에서 우리는 scheme morphism의 성질들에 대해 살펴볼 것인데, 그 전에 우리는 scheme morphism을 이해하는 네 가지 방법을 제시한다. 

## 환 준동형사상의 gluing

가장 첫 번째 관점은 꽤나 자연스러운 것이다. Scheme은 본질적으로 affine scheme들을 붙여서 만드는 것이고, categorical equivalence $\AffSch\cong\cRing^\op$에 의하여 affine scheme 사이의 morphism은 본질적으로 ring homomorphism이다. 따라서 scheme morphism 또한 affine scheme들 사이의 morphism을 붙여서 만드는 것으로 이해할 수 있어야 할 것이다. 즉 다음 명제를 기대하는 것이 합당하다.

<div class="proposition" markdown="1">

<ins id="prop1">**명제 1**</ins> Scheme morphism $\varphi: X \rightarrow Y$가 주어졌다 하자. 그럼 $X$의 affine open subset $U\cong\Spec A$와 $Y$의 affine open subset $V\cong\Spec B$가 $\varphi(U)\subseteq V$를 만족한다면, $\varphi\vert_U: U \rightarrow V$는 affine scheme들 사이의 morphism이다. 

거꾸로 $X,Y$의 두 affine open covering $\\{U_i\\}$와 $\\{V_j\\}$가 주어졌다 하고, affine scheme들 사이의 morphism $\varphi_{ij}: U_i \rightarrow V_j$가 주어졌다 하자. 만일 이들이 각각의 교집합 위에서 gluing condition을 만족하여 잘 정의된다면 $\varphi_{ij}$들은 scheme morphism $\varphi: X \rightarrow Y$를 만든다. 

</div>

한쪽 방향은 [§아핀스킴, ⁋명제 11](/ko/math/algebraic_geometry/affine_schemes#prop11)에 의해 $\AffSch$이 $\LRS$의 full subcategory라는 주장의 새로운 버전일 뿐이며, 그 역을 위한 gluing 또한 자명한 방식으로 얻어진다. 

<div class="example" markdown="1">

<ins id="ex2">**예시 2**</ins> Affine scheme들 사이의 morphism이 아닌 scheme morphism의 예시로, [§사영스킴, §§사영공간](/ko/math/algebraic_geometry/projective_schemes#사영공간)에서 motivation을 위해 처음 등장했던 map

$$\varphi:\mathbb{A}_\mathbb{K}^{n+1}\setminus \{0\} \rightarrow \mathbb{P}^n_\mathbb{K}$$

이 있다. 이 식은 전통적으로 projective space를 만들 때 사용하는 식이었으나, [§사영스킴, ⁋예시 12](/ko/math/algebraic_geometry/projective_schemes)에서 전통적인 projective space를 대수기하의 언어로 옮길 때는 등장하지 않았었다. 이 morphism은 물론 식 $(x_0,\ldots, x_n)\mapsto [x_0:\cdots:x_n]$을 만족하지만, $\mathbb{A}^{n+1}_\mathbb{K}$의 점들이 이러한 꼴만 있는 것은 아니고, 또 이 식은 structure sheaf에 대한 정보를 하나도 담고 있지 않으므로 scheme morphism이라 칭하기는 부적절할 것이다.

이제 scheme morphism으로서 $\varphi$를 정의하기 위해 $\mathbb{P}^n_{\mathbb{K}}$의 affine open subscheme 

$$D_+(\x_i)\cong \Spec \mathbb{K}[\x_0,\ldots, \x_n]_{(\x_i)}\cong \Spec \mathbb{K}[\x_{0/i},\ldots, \x_{n/i}]/(\x_{i/i}-1)$$

을 생각하자. ([§사영스킴, ⁋예시 12](/ko/math/algebraic_geometry/projective_schemes#ex12)) 또, affine space 

$$\mathbb{A}^{n+1}_\mathbb{K}=\Spec \mathbb{K}[\x_0,\ldots, \x_n]$$

을 생각하자. 그럼 

$$\mathbb{A}^{n+1}_\mathbb{K}\setminus \{0\}=\bigcup_{i=0}^n D(\x_i)$$

이고, $D(\x\_i)\cong \Spec \mathbb{K}[\x\_0,\ldots, \x\_n]\_{\x\_i}$이다. 이제 각각의 $i$에 대하여, $\varphi\_i: D(\x\_i) \rightarrow D\_+(\x\_i)$는 affine scheme들 사이의 morphism이므로 ring homomorphism과 동일하다. 그럼 다음 식

$$\phi_i:\mathbb{K}[\x_{0/i},\ldots, \x_{n/i}]\rightarrow\mathbb{K}[\x_0,\ldots, \x_n]_{\x_i};\qquad \x_{k/i}\mapsto  \frac{\x_k}{\x_i}$$

에 first isomorphism theorem을 적용하여 정의된 affine scheme 사이의 morphism $\varphi_i$가 원하는 morphism이 된다. 이들이 [명제 1](#prop1)의 조건을 만족하는 것도 약간의 계산을 통해 확인할 수 있다. 이제 [§사영스킴, §§사영공간](/ko/math/algebraic_geometry/projective_schemes#사영공간)에서의 표기를 다시 빌려오면, 이들은 각각의 $D(\x_i)$ 위에서 다음 식

$$(x_0,\ldots, x_n) \rightarrow \left[\frac{x_0}{x_i}:\cdots:\frac{x_{i-1}}{x_i}:1:\frac{x_{i+1}}{x_i}:\cdots:\frac{x_n}{x_i} \right]$$

으로 주어지므로, 이를

$$(x_0,\ldots, x_n)\rightarrow [x_0:\cdots:x_n]$$

으로 표기하면 적절할 것이다. 

</div>

우리는 이 관점을 거의 정의로 받아들일 것이며, 남은 부분에서 소개할 세 가지 관점은 이를 해석하는 방법에 가깝다. 

## 스킴 위의 스킴

우선 우리는 다음을 정의한다. 

<div class="definition" markdown="1">

<ins id="def3">**정의 3**</ins> 임의의 scheme $S$에 대하여, slice category $\Sch_{/S}$ over $S$를 *$S$-scheme*들의 category라 부른다. ([\[범주론\] §범주, ⁋예시 13](/ko/math/category_theory/categories#ex13)) 

</div>

즉 $S$-scheme은 $S$로의 scheme morphism $X \rightarrow S$를 부르는 다른 이름이며, 이를 *structure morphism*이라 부르기도 한다. 

이는 다음 예시를 살펴보면 조금 더 직관적이다.

<div class="example" markdown="1">

<ins id="ex4">**예시 4**</ins> Affine $n$-space $\mathbb{A}^n_\mathbb{K}=\Spec \mathbb{K}[\x_1,\ldots, \x_n]$을 생각하자. 그럼 $\mathbb{K}[\x_1,\ldots, \x_n]$은 $\mathbb{K}$-algebra이며, 이는 structure morphism

$$\mathbb{K}\hookrightarrow \mathbb{K}[\x_1,\ldots, \x_n]$$

을 통해 $\mathbb{K}$-algebra가 주어진 것이다. ([\[대수적 구조\] §대수, ⁋정의 1](/ko/math/algebraic_structures/algebras#def1) 이후의 논증)

그럼 이 structure morphism을 통해 우리는 $\mathbb{A}^n_\mathbb{K}$를 $\Spec\mathbb{K}$-scheme

$$\mathbb{A}^n_\mathbb{K}=\Spec \mathbb{K}[\x_1,\ldots, \x_n] \rightarrow \Spec \mathbb{K}$$

으로 볼 수 있다. 

</div>

위와 같이 $S$가 affine scheme $S=\Spec A$인 경우, $S$-scheme $X$를 약간의 abuse of language를 통해 $A$-scheme이라 부르는 것이 일반적이다. 그럼 [§아핀스킴, ⁋정리 13](/ko/math/algebraic_geometry/affine_schemes#thm13)에 의하여, 임의의 ring $A$를 고정하고, scheme $X$에 $A$-scheme의 구조를 주는 것은 정확하게

$$\Hom_\Sch(X, \Spec A)=\Hom_\LRS(X, \Spec A)\cong \Hom_\cRing(A, \Gamma(X, \mathscr{O}_X))$$

와 같다. 즉, scheme $X$에 $A$-scheme 구조를 주는 것은 대수적으로는 $\Gamma(X, \mathscr{O}_X)$에 $A$-algebra 구조를 주는 것과 동등하다. 특히 $A=\mathbb{Z}$인 경우, $\mathbb{Z}$는 $\cRing$의 initial object이므로 모든 scheme은 유일한 방식으로 $\mathbb{Z}$-scheme으로 생각할 수 있다. 

이제 [예시 2](#ex2)를 더욱 일반화하는 다음의 예시를 보자.

<div class="example" markdown="1">

<ins id="ex5">**예시 5**</ins> Ring $A$와 $A$-scheme $X$를 생각하고, $X$ 위에 정의된 함수들 $f_0,\ldots, f_n\in \Gamma(X, \mathscr{O}\_X)$이 주어졌다 하고, $X$의 affine open covering $X=\bigcup U_j$를 생각하자. 그럼

$$U_{ij}:=D(f_i)\cap U_j=D(f_i\vert_{U_j})\subseteq U_j$$

이 $X$의 affine open covering이 된다. 한편 $A$ 위에 정의된 projective space

$$\mathbb{P}^n_A=\Proj A[\x_0,\ldots, \x_n]$$

을 생각하고, 이 공간의 open covering $D_+(\x_i)$를 생각하자. 이제 $i,j$ 쌍이 주어질 때마다, 함수 $\varphi_{ij}: U_{ij} \rightarrow D_+(\x_i)$를 ring homomorphism

$$A[\x_{0/i},\ldots, \x_{n/i}]\rightarrow \Gamma(U_{ij});\qquad \x_{k/i}\mapsto \frac{f_k\vert_{U_{ij}}}{f_i\vert_{U_{ij}}}$$

을 통해 정의하자. 그럼 정의에 의해 이 morphism이 [명제 1](#prop1)의 gluing condition을 만족하는 것이 자명하고, 따라서 이들이 scheme morphism

$$X \rightarrow \mathbb{P}^n_A$$

을 정의한다. 명시적으로 이 scheme morphism은, [예시 2](#ex2)와 마찬가지 방식으로, 

$$x\mapsto [f_0(x):\cdots: f_n(x)]$$

으로 주어진다. 

</div>

## 점

또, 다음을 정의한다.

<div class="definition" markdown="1">

<ins id="def6">**정의 6**</ins> Scheme morphism $f: X \rightarrow Y$를 $Y$의 *$X$-point*라 부른다. 

</div>

마찬가지로 $X$가 affine scheme인 경우를 살펴보는 것이 직관적으로 도움이 된다. 

<div class="example" markdown="1">

<ins id="ex7">**예시 7**</ins> Algebraically closed field $\mathbb{K}$와 그 위에 정의된 affine $n$-space $Y=\mathbb{A}^n_\mathbb{K}=\Spec \mathbb{K}[\x_1,\ldots, \x_n]$과 $X=\Spec \mathbb{K}$를 생각하자. 그럼 scheme morphism $X \rightarrow Y$는 affine scheme 사이의 morphism 

$$\Spec \mathbb{K} \rightarrow \Spec \mathbb{K}[\x_1,\ldots, \x_n]$$

이므로, ring homomorphism

$$\phi:\mathbb{K}[\x_1,\ldots, \x_n] \rightarrow \mathbb{K}$$

에 대응된다. 그럼 이 ring homomorphism은 반드시 surjective이다. Ring homomorphism의 정의로부터 $\phi(1)=1$이고 따라서 임의의 $x\in \mathbb{K}$에 대하여 $\phi(x)=x$이기 때문이다. 따라서 first isomorphism theorem에 의하여

$$\mathbb{K}[\x_1,\ldots, \x_n]/\ker\phi\cong \mathbb{K}$$

이다. 그럼 [\[대수적 구조\] §몫환, 환 동형사상, ⁋정리 3](/ko/math/algebraic_structures/quotient_rings#thm3)의 넷째 결과에 의하여 $\ker\phi$는 $\mathbb{K}[\x_1,\ldots, \x_n]$의 maximal ideal이어야 하고, 따라서 [\[가환대수학\] §영점정리, ⁋보조정리 5](/ko/math/commutative_algebra/nullstellensatz#lem5)로부터

$$\ker\phi=(\x_1-x_1,\ldots, \x_n-x_n)$$

의 꼴이며 $\phi$는 점 $x=(x_1,\ldots, x_n)$에서의 evaluation homomorphism $\ev_x$가 된다. 뿐만 아니라 해당 보조정리의 증명을 생각하면 $x_i=\phi(\x_i)$인 것 또한 알 수 있다. 즉, 역함수 관계에 있는 다음의 두 일대일대응

$$\begin{aligned}\{\text{$\mathbb{K}$-point $\Spec \phi:\Spec\mathbb{K}\rightarrow \mathbb{A}^n_\mathbb{K}$}\}&\rightarrow \{\text{points $(x_1,\ldots, x_n)\in \mathbb{A}^n_\mathbb{K}$}\}\\\Spec\phi&\mapsto (\phi(\x_1),\ldots,\phi(\x_n))\end{aligned}$$

그리고

$$\begin{aligned}\{\text{points $(x_1,\ldots, x_n)\in \mathbb{A}^n_\mathbb{K}$}\}&\rightarrow \{\text{$\mathbb{K}$-point $\Spec \phi:\Spec\mathbb{K}\rightarrow \mathbb{A}^n_\mathbb{K}$}\}\\a=(a_1,\ldots, a_n)&\mapsto \Spec \ev_a\end{aligned}$$

이 존재한다. 

</div>

위에서와 마찬가지로, $X$가 $\Spec A$ 꼴이라면 이를 간단히 $A$-point라 부른다. 이 개념의 유용성은 다음 예시에서도 확인할 수 있다.

<div class="example" markdown="1">

<ins id="ex8">**예시 8**</ins> $\mathbb{C}$-scheme $X=\Spec\frac{\mathbb{C}[\x_1,\ldots, \x_n]}{(f_1,\ldots, f_r)}$이 주어졌다 하고, 이 scheme의 $\mathbb{Q}$-point를 생각하자. 그럼 [\[가환대수학\] §영점정리, ⁋보조정리 5](/ko/math/commutative_algebra/nullstellensatz#lem5)와 [예시 6](#ex6)의 계산으로부터 우리는 $X$의 $\mathbb{Q}$-point $\Spec\phi: \Spec \mathbb{Q}\rightarrow X$와, 

$$f_1(x_1,\ldots, x_n)=\cdots=f_r(x_1,\ldots, x_n)=0$$

의 유리수해 사이의 일대일대응이 존재함을 안다. 비슷하게 위의 방정식의 정수해는 정확히 $X$의 $\mathbb{Z}$-point에 대응된다. 

</div>

이러한 관점을 바탕으로 다음을 정의한다.

<div class="definition" markdown="1">

<ins id="def9">**정의 9**</ins> Functor $\Hom_\Sch(-,X): \Sch^\op \rightarrow \Set$을 *functor of points of $X$*라 부른다. 

</div>

그럼 $\Hom_\Sch(-,X)$는 scheme $S$를 받아서, $X$의 $S$-valued point들의 집합을 내놓는 functor이다. 

## 스킴의 족

마지막 관점은 아직 엄밀하게 정의하기에는 우리가 가진 언어가 부족하므로, 기하학적인 직관만 설명하기로 한다. 우리는 scheme morphism $f:X \rightarrow S$를 *family parametrized by $S$* 혹은 간단히 $S$-family라 부른다. 따라서 정의에 의하여 $\Sch_{/S}$는 $S$로 parametrize된 family들의 category로 생각할 수 있다. 

기하학적인 직관을 위해서는 기본적으로 다음과 같은 (scheme이 아닌) 상황을 생각하면 된다.

<div class="example" markdown="1">

<ins id="ex10">**예시 10**</ins> 좌표공간 $\mathbb{R}^3$에서 정의된 구 $S:x^2+y^2+z^2=1$과, $x$축으로의 projection $\pi: S \rightarrow \mathbb{R}_x$를 생각하자. 그럼 임의의 $x_0\in \mathbb{R}_x$에 대하여, 

$$\pi^{-1}(x_0)=\{(x_0,y,z)\in \mathbb{R}: y^2+z^2=1-x_0^2\}$$

이다. 이를 기하학적으로 표현하면, 각각의 $x_0\in \mathbb{R}_x$마다 원 $y^2+z^2=1-x_0^2$가 대응된 상황으로 볼 수 있으며, 따라서 $\pi$를 <em_ko>$x$축으로 parametrize된 원들의 family</em_ko>로 생각할 수 있다. 

</div>

이 예시를 스킴으로 바로 나타낼 수 없는 이유 중 덜 본질적인 것은 $S$가 $\mathbb{R}^3$의 닫힌집합이고, 우리는 닫힌집합 위에 scheme structure를 주는 방법은 모른다는 것이다. 이는 [§닫힌 부분스킴](/ko/math/algebraic_geometry/closed_subschemes)에서 해결하게 된다. 더 미묘하고 본질적인 부분은 함수 $\pi$의 점 $x_0$에서의 fiber $\pi^{-1}(x_0)$을 나타낼 방법이 없는 것이다. 물론 scheme morphism은 기본적으로 연속함수이므로 이를 연속함수의 fiber로 볼 수 있겠지만, 그렇게 하였을 경우 $\pi^{-1}(x_0)$에 scheme structure를 주는 방법이 ([§닫힌 부분스킴](/ko/math/algebraic_geometry/closed_subschemes)의 내용을 가정하더라도) 존재하지 않는다. 이를 설명하기 위해서 우리는 조금 더 기다려야 한다. 

---
**참고문헌**

**[Har]** R. Hartshorne, *Algebraic geometry*. Graduate texts in mathematics. Springer, 1977.  
**[Vak]** R. Vakil, *The rising sea: Foundation of algebraic geometry*. Available [online](https://math.stanford.edu/~vakil/216blog/).  

---