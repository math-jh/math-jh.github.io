---

title: "배유 인자"
excerpt: ""

categories: [Math / Algebraic Geometry]
permalink: /ko/math/algebraic_geometry/Weil_divisors
header:
    overlay_image: /assets/images/Math/Algebraic_Geometry/Weil_divisors.png
    overlay_filter: 0.5
sidebar: 
    nav: "algebraic_geometry-ko"

date: 2024-07-22
last_modified_at: 2024-07-22
weight: 12

---

이번 글과 다음 글에서는 divisor들을 정의한다. 기하적으로 이들은 scheme 위에서의 homology (혹은 cohomology)라고 할 수 있는데, 그 중 이번 글에서 정의할 Weil divisor는 $(n-1)$차원의 호몰로지라고 생각할 수 있다. 이들은 공통적으로 scheme 위에 정의된 rational function과 깊은 연관이 있다.

## Rational functions

임의의 integral scheme $X$가 주어졌다 하자. 일반적으로 irreducible scheme은 유일한 generic point를 갖는다는 것이 알려져 있으므로, $X$의 유일한 generic point $\xi$가 존재한다. 이제 $X$의 임의의 affine open subset $U=\Spec A$를 생각하자. 그럼 정의에 의해 $\xi\in U$여야 하고, $\xi$가 generic point인 것을 이용하면 이 집합에서 $\xi$는 $A$의 가장 작은 prime ideal, 즉 $(0)$에 대응되어야 한다는 사실은 안다. 즉 

$$\mathscr{O}_{X,\xi}\cong \mathscr{O}_{U,\xi}\cong A_{(0)}\cong\Frac(A)$$

이 성립한다. 

<div class="definition" markdown="1">

<ins id="def1">**정의 1**</ins> Integral scheme $X$와 generic point $\xi$에 대하여, local ring $\mathscr{O}_{X,\xi}$를 $X$의 *function field*라 부르고, $K(X)$로 표기한다. 

</div>

우리는 $A$를 열린집합 $U\subseteq X$ 위에서 정의된 함수들의 ring으로 생각한다. 그럼 위의 식이 말해주는 것은 $\mathscr{O}_{X,\xi}$를 affine open set $U$에서 보면 *rational function*들의 모임처럼 보인다는 뜻이고, 따라서 위와 같은 이름을 붙이는 것이 어색하지 않다. 이들은 진정한 의미에서의 함수는 아닌데, 전체 공간 $X$에서 정의되지는 않기 때문이다. 

<div class="example" markdown="1">

<ins id="ex2">**예시 2**</ins> 예를 들어 $X=\Spec \mathbb{C}[x,y]$를 생각하면, $X$는 generic point $(0)$을 갖는다. 이 점에서의 local ring은

$$\mathbb{C}[x,y]_{(0)}=\Frac(\mathbb{C}[x,y])$$

와 같다. 이 local ring의 각 원소들은 분모가 $0$이 아닌 affine open subset에서만 정의되는 것을 확인할 수 있다. 

</div>

## Weil divisors

<div class="definition" markdown="1">

<ins id="def3">**정의 3**</ins> Scheme $X$가 *regular in codimension $1$*이라는 것은 dimension 1짜리 local ring $\mathscr{O}_x$가 항상 regular인 것이다. 

</div>

우리는 이제 Weil divisor를 정의할 것인데, Weil divisor는 앞으로 설명할 조건 ($\ast$)를 만족하는 scheme에서만 잘 정의된다. 따라서, 이번 절에서 다루는 모든 scheme은 다음의 조건을 만족한다고 가정한다. 

> ($\ast$) $X$는 noetherian integral separated scheme이며, regular in codimension $1$이다. 

<div class="definition" markdown="1">

<ins id="def4">**정의 4**</ins> Scheme $X$의 closed integral subscheme을 $X$의 *prime divisor<sub>소인자</sub>*라 부른다. 그럼 $X$의 *Weil divisor<sub>베유 인자</sub>*는 prime ideal의 일차결합

$$D=\sum n_iY_i$$

을 의미하며, 이 때 $n_i$들은 유한개를 제외하고는 모두 $0$이라 가정한다. 특별히 $n_i\geq 0$이 모든 $i$에 대해 성립할 경우 $D$를 *effective*라 부른다. $X$의 Weil divisor들의 모임은 $\Div X$로 표기한다. 

</div>

$X$의 prime divisor $Y$를 고정하자. $\eta\in Y$를 $Y$의 generic point라 하면 $\mathscr{O}_{X,\eta}$는 regular local ring of dimension $1$, 즉 discrete valuation ring이 된다. 

한편 임의의 discrete valuation ring $(A,\mathfrak{m})$에 대해 생각해보면, $A$의 임의의 원소는 다음의 꼴

$$u\pi^k\qquad\text{where $u$ is a unit, $\pi$ is a uniformizer, $k\geq 0$}$$

로 쓰일 수 있으며, 이러한 원소에 $k$를 대응시키는 것이 정확히 discrete valuation $v$에 해당되었다. 한편 이러한 표현 하에서 discrete valuation ring의 field of fractions를 생각하는 것은 $k$를 모든 정수값을 가질 수 있도록 하는 것과 같으며, 여기에서의 discrete valuation 또한 같은 방식으로 주어진다. 

이제 $\eta$를 포함하는 affine open subset $\Spec A$를 생각하면, 이 local ring의 quotient field $\Frac(\mathscr{O}\_{X,\eta})$는

$$\Frac(\mathscr{O}_{X,\eta})=\Frac(A_\eta)=\Frac(A)$$

이므로 $X$의 function field $K(X)$와 같다. 즉, $\mathscr{O}_{X,\eta}$ 위에 주어진 discrete valuation $v_Y$가 위의 방식을 따라 $K(X)$ 위에 discrete valuation을 준다.

<div class="example" markdown="1">

<ins id="ex5">**예시 5**</ins> 앞의 예를 계속해서, $X=\Spec \mathbb{C}[x,y]$라 하자. 그럼 $K(X)$는 다음의 꼴

$$f(x,y)=\frac{g(x,y)}{h(x,y)},\qquad g,h\in \mathbb{C}[x,y],\quad h(x)\not\equiv 0$$

의 원소들을 모아둔 것임을 살펴보았다. 이제 $F(x,y)=0$에 의해 정의되는 closed subscheme $Y$, 즉

$$\Spec \mathbb{C}[x,y]/F(x,y)$$

을 생각하자. $\Spec \mathbb{C}[x,y]/F(x,y)$의 generic point $(0)$은 $\Spec \mathbb{C}[x,y]$에서는 $\eta=(F(x,y))$이므로, 여기에서의 local ring은

$$\mathscr{O}_{X,\eta}=\mathbb{C}[x,y]_{(F(x,y))}$$

즉 다음의 꼴

$$f(x,y)=\frac{g(x,y)}{h(x,y)},\qquad g,h\in \mathbb{C}[x,y],\quad F(x,y)\nmid h(x,y)$$

을 모아둔 것이다. 여기에서의 unit은 추가로 $F(x,y)\nmid g(x,y)$를 만족하는 $g(x,y)/h(x,y)$ 꼴의 원소들이며, 따라서 이 local ring의 원소들은 모두

$$f(x,y)=u(x,y) F(x,y)^k,\qquad\text{where $u(x,y)=\frac{g(x,y)}{h(x,y)}$ with $F(x,y)\nmid g(x,y),h(x,y)$ and $k\geq 0$}$$

의 꼴로 쓸 수 있으며, discrete valuation $v_Y$는 이 표현에서 지수 $k$를 읽어오는 것이다. 

한편 $\Frac(\mathscr{O}_{X,\eta})$는 [예시 2](#ex2)에서 살펴본 $X$의 function field $K(X)$와 동일한 것을 알 수 있으며, $v_Y$는 이를 통해 $K(X)$ 위에 valuation을 정의한다. 이는 $K(X)$의 원소를 다음의 꼴

$$f(x,y)=g(x,y)F(x,y)^k,\qquad k\in \mathbb{Z}$$

으로 나타내어 얻어진다. 

</div>

이로부터 다음 정의가 자연스럽다.

<div class="definition" markdown="1">

<ins id="def6">**정의 6**</ins> 위와 같은 상황에서, 만일 $f\in K^\ast$에 대해 $v_Y(f)>0$이라면 $f\in K(X)$가 $Y$ 위에서 order $v_Y(f)$의 zero를 갖는다 하고, 거꾸로 $v_Y(f)<0$이라면 $f$가 $Y$ 위에서 order $-v_Y(f)$의 pole을 갖는다고 말한다. 

</div>

그럼 다음이 성립한다. 

<div class="proposition" markdown="1">

<ins id="lem7">**보조정리 7**</ins> 임의의 $f\in K(X)^\ast$를 고정하자. 그럼 유한히 많은 prime divisor $Y$를 제외하면, $v_Y(f)=0$이 항상 성립한다. 

</div>

이는 위의 예시에서 보면, 대략적으로 분모와 분자에 등장하는 유한한 항들에 의해 정의되는 prime divisor들을 제외하면, 나머지 prime divisor는 $v_Y(f)=0$을 만족하기 때문이다. 따라서 다음이 잘 정의된다.

<div class="definition" markdown="1">

<ins id="def7">**정의 8**</ins> 임의의 rational function $f\in K^\ast$에 대하여, $f$의 *divisor*를 다음 식

$$(f)=\sum v_Y(f)Y$$

으로 정의한다. 이와 같은 형태의 divisor를 *principal divisor*라 부른다. 

</div>

이 표현에서 $(f)$는 rational function $f$가 zero와 pole을 갖는 위치 $Y$와, 그 차수 $v_Y(f)$에 대한 정보를 가지고 있게된다. 이제 다음을 정의한다.

<div class="definition" markdown="1">

<ins id="def9">**정의 9**</ins> $\Div X$의 동치관계

$$D\sim D'\iff D-D'\text{ is a principal divisor}$$

에 의한 quotient group을 *divisor class group*이라 부르고 $\Cl(X)$로 표기한다. 

</div>

## Weil divisor의 성질들

이제 Weil divisor의 성질들을 살펴본다. $X$가 $n$차원의 scheme이었다 하면, 지금까지 우리는 $(n-1)$차원 closed subscheme들을 모아 이들로 free abelian group $\Div (X)$를 만들고, 이 위에 특정한 종류의 동치관계를 주어 이에 대한 quotient group으로 $\Cl(X)$를 정의했다. 이는 다른 기하학에서 $(n-1)$번째 homology group을 만드는 과정과 거의 유사하며, 실제로 많은 비슷한 성질들이 성립한다. 가령 다음은 $\mathbb{P}^n$이 우리가 원하는대로 행동한다는 것을 보여준다. 

<div class="proposition" markdown="1">

<ins id="prop10">**명제 10 (Divisor class group of $\mathbb{P}^n$)**</ins> $X=\mathbb{P}_k^n$이라 하자. $\Cl(X)$ 위에 *degree map*을

$$\sum n_i Y_i\mapsto n_i\deg(Y_i)$$

으로 정의하자. 여기서 $\deg Y_i$는 hyperplane $Y_i$의 degree로 정의된다. 특별히 hypersurface $H$를 $x_0=0$이라 하자. 그럼 다음이 성립한다. 

1. Degree $d$ divisor $D$에 대하여, $D\sim dH$이다. 
2. 임의의 $f\in K^\ast$에 대하여 $\deg(f)=0$이 성립한다. 
3. Degree map에 의해 isomorphism $\Cl(X) \rightarrow \mathbb{Z}$가 정의된다. 

</div>

다음 명제는 excision sequence에 대한 analogue이다.

<div class="proposition" markdown="1">

<ins id="prop11">**명제 11**</ins> Scheme $X$의 proper closed subscheme $Z$, $U=X\setminus Z$를 생각하자. 

1. $\sum n_i Y_i \mapsto \sum n_i(Y_i\cap U)$는 surjective homomorphism $\Cl(X) \rightarrow \Cl(U)$를 정의한다.
2. $\codim(Z,X)\geq 2$라면 $\Cl(X) \rightarrow \Cl(U)$는 isomorphism이다.
3. $Z$가 irreducible subset of codimension $1$이라면, 다음의 exact sequence
    
    $$\mathbb{Z}\rightarrow \Cl(X) \rightarrow \Cl(U) \rightarrow 0$$

    이 존재한다. 여기서 첫째 map은 $1\mapsto 1\cdot Z$이다. 

</div>

<div class="proposition" markdown="1">

<ins id="prop12">**명제 12**</ins> Scheme $X$가 조건 ($\ast$)를 만족한다면 $X\times \mathbb{A}^1$ 또한 그러하며, 이 때 $\Cl(X)\cong\Cl(X\times \mathbb{A}^1)$이 성립한다.

</div>

Kunneth formula를 생각하면 된다. 