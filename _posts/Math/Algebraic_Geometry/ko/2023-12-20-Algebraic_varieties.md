---

title: "대수다양체"
excerpt: "대수다양체와 스킴"

categories: [Math / Algebraic Geometry]
permalink: /ko/math/algebraic_geometry/algebraic_varieties
header:
    overlay_image: /assets/images/Math/Algebraic_Geometry/Algebraic_varieties.png
    overlay_filter: 0.5
sidebar: 
    nav: "algebraic_geometry-ko"

date: 2023-12-20
last_modified_at: 2023-12-20
weight: 1
toc: false

---

이 글에서는 scheme theory를 시작하기 전에, 간략하게 큰 흐름을 살펴본다.

대수기하에서 생각하는 공간들은 대략적으로 다항식의 해집합으로 나타나는 공간들이고, 대충 이야기하면 이런 공간들을 대수다양체라 부른다. 가령 유클리드 공간 $\mathbb{R}^2$에서 방정식 $y=x^2$이 나타내는 해집합은 포물선이 될텐데, 이러한 해집합들의 성질을 대수적인 방식으로 살펴보는 것이 우리의 목적이라 할 수 있다. 표기의 편의를 위해, 다항함수 $f$에 대하여 $f$의 해집합을 $V(f)$라 하자. 그럼 위에서 정의한 포물선의 경우는 $V(y-x^2)$이라 적을 수 있다.

더 일반적으로, 임의의 field $k$와, 이를 사용해 만든 $n$차원 공간 $k^n$을 생각하자. 그럼 $n$변수 다항함수들의 집합 $I$에 대하여, $V(I)$를 다음 식

$$V(I)=\{(x_1,\ldots, x_n): f(x_1,\ldots, x_n)=0\text{ for all $f\in I$}\}$$

으로 정의한다. 즉 $V(I)$는 <em_ko>모든</em_ko> $f\in I$에 대하여, $f(x_1,\ldots, x_n)=0$이 성립하는 점들의 집합이고, 바꿔말하면 $I$에 속하는 다항함수들의 해집합의 교집합이다. 즉

$$V(I)=\bigcap_{f\in I} V(f)$$

이다. 

<div class="example" markdown="1">

<ins id="ex1">**예시 1**</ins> $\mathbb{R}^2$에서, $V(x,y)$는 두 직선 $x=0$과 $y=0$의 교집합이므로 원점 $(0,0)$을 의미한다. 마찬가지로 $V(y-x^2, y)$를 생각하면, 이는 포물선 $y=x^2$과 직선 $y=0$의 교집합이므로 원점 $(0,0)$을 의미한다. 

![reduced_scheme](/assets/images/Math/Algebraic_Geometry/Algebraic_varieties-1.png){:width="666px" class="invert" .align-center}

위의 그림에서 첫 번째 경우와 두 번째 경우 사이에는 multiplicity로부터 오는 차이가 있지만, 단순히 $V(I)$만 생각해서는 이 둘을 구별할 수 없다.

</div>

[예시 1](#ex1)의 두 상황을 구별하기 위해 우리는 공간을 생각할 때, 공간 뿐만 아니라 그 위에 정의된 함수들도 같이 생각하게 된다. 예를 들어 $k^n$을 생각할 때 우리는 이 위에 정의된 다항함수들의 모임, 즉 polynomial ring $k[x_1,\ldots, x_n]$을 함께 생각한다. 이렇게 다항함수들의 모임을 생각했을 때 좋은 점은 $V(I)$ 위에 정의된 함수들의 모임이 이 다항함수들의 모임으로부터 자연스럽게 얻어진다는 것이다. 

가령 위의 예시에서 $V(y-x^2)$을 생각해보면, 이 집합 위에서는 두 함수 $g_1(x,y)=x$와 $g_2(x,y)=x-x^2+y$는 같은 함수이다. 어차피 $V(y-x^2)$ 위에서는 $y-x^2=0$이므로 이 두 함수를 구별할 수 없기 때문이다. 즉 $V(y-x^2)$에 정의된 함수들은 다음 ring $\mathbb{R}[x,y]/(y-x^2)$의 원소로 생각할 수 있다. 이를 $V(y-x^2)$의 *coordinate ring*이라 부르며, 같은 방식으로 임의의 집합 $I$에 대하여 $V(I)$의 coordinate ring를 정의할 수 있다. 

<div class="example" markdown="1">

<ins id="ex2">**예시 2**</ins> [예시 1](#ex1)에서의 두 집합 $V(x,y)$와 $V(y-x^2,y)$를 생각해보면, $V(x,y)$의 coordinate ring은

$$\mathbb{R}[x,y]/(x,y)\cong \mathbb{R}[x]/(x)\cong\mathbb{R}$$

과 같다. 한편 $V(y-x^2,y)$의 coordinate ring은

$$\mathbb{R}[x,y]/(y-x^2,y)\cong\mathbb{R}[x]/(x^2)$$

와 같다. 이 두 ring 사이에는 큰 차이가 있는데, 첫 번째 ring에는 $\alpha^2=0$을 만족하는 $\alpha\neq 0$이 존재하지 않지만, 두 번째 ring에서는 $x$가 그러한 원소가 된다는 것이다. 즉 이 상황에서 ring의 nilpotent인 원소가 중근에 해당하는 개념을 나타내고 있는 것을 확인할 수 있다.

</div>

이렇게 정의를 하면 약간 미묘한 부분이 있다.

<div class="example" markdown="1">

<ins id="ex3">**예시 3**</ins> $\mathbb{R}^2$에서 정의된 원 $V(x^2+y^2-1)$을 생각하자. 그럼 이 집합 위에서 정의된 두 함수

$$g_1(x,y)=\frac{x^2}{1-y},\quad g_2(x,y)=1+y$$

는 본질적으로는 같은 함수여야 한다. 물론 $g_1$은 점 $(0,1)$에서 정의가 되지 않는 함수이긴 하지만, 그 점만 제외하면 식

$$\frac{x^2}{1-y}=1+y$$

이 $V(x^2+y^2-1)$에서 항상 성립하며, 뿐만 아니라 $(0,1)$에서의 값을 적당히 잘 정의해서 $g_1$을 확장할 수도 있으므로 이 경우에는 $g_1$의 정의역은 사실 그렇게 큰 문제가 되지 않는다.

</div>

이런 차원에서 우리는 $V$ 위에 정의된 함수들의 모임을 생각할 때 *regular function*들을 생각하게 되고, 이는 각각의 $p\in V$마다 적당한 근방 $U\subseteq V$가 존재하여 여기에서는 $g/h$ 꼴로 쓸 수 있는 함수들을 말한다. (물론, $g,h$는 다항식이고 $h$는 $U$에서는 $0$이 되지 않는다.)

앞으로 몇 개의 글에서 우리는 우선 공간 위에 정의된 함수들을 다루는 방법을 살펴본다. 그 후에는 위에서 했던 예시들을 마음에 두고 scheme을 정의하고, scheme의 성질들을 살펴본다. 