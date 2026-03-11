---

title: "준사영다양체 위의 함수들"
excerpt: ""

categories: [Math / Algebraic Geometry]
permalink: /ko/math/algebraic_geometry/functions_on_quasiprojective_varieties
header:
    overlay_image: /assets/images/Math/Algebraic_Geometry/Functions_on_quasiprojective_varieties.png
    overlay_filter: 0.5
sidebar: 
    nav: "algebraic_geometry-ko"

date: 2024-11-07
last_modified_at: 2024-11-07
weight: 4

---

## 준사영다양체 위의 정칙함수들

이제 우리는 quasiprojective variety 위의 함수들에 대해 살펴본다. 특히 quasiprojective variety 위에서 rational function을 다루는 것이 문제가 될 수 있는데, 이는 아주 간단한 예시인 $\mathbb{P}^n$에서조차 rational function을 임의의 두 homogeneous polynomial들 $F,G\in \mathbb{k}[\X_0,\ldots, \X_n]$에 대하여

$$f(\X_0,\ldots,\X_n)=\frac{F(\X_0,\ldots,\X_n)}{G(\X_0,\ldots,\X_n)}$$

으로 정의하더라도, 만일 $F$와 $G$의 차수가 다르다면 다음 식

$$f(\lambda\X_0,\ldots,\lambda\X_n)=\frac{F(\lambda\X_0,\ldots,\lambda\X_n)}{G(\lambda\X_0,\ldots,\lambda\X_n)}=\frac{\lambda^{\deg F}F(\X_0,\ldots,\X_n)}{\lambda^{\deg G}G(\X_0,\ldots,\X_n)}$$

으로 인해 $f$가 homogeneous가 아닐 수 있기 때문이다. 이러한 이유로 우리는 $F,G$가 같은 degree에 있을 것을 요구하게 된다. $\deg f=\deg F-\deg G$라 한다면 이는 $\deg f=0$일 것을 요구하는 것과 같다. 

<div class="definition" markdown="1">

<ins id="def1">**정의 1**</ins> Quasiprojective variety $X\subseteq \mathbb{P}^n$이 주어졌다 하자. Degree $0$의 homogeneous function $f=F/G$가 주어졌다 하자. 만일 $G(x)\neq 0$이라면, 이 함수가 $x\in X$에서 *regular*라 말하고, $X$의 모든 점에서 regular인 함수를 *regular function*이라 부른다. 모든 regular function들의 모임을 $\mathbb{k}[X]$로 적는다.

</div>

특별히 $X$가 irreducible affine algebraic set일 경우 이 개념은 원래 정의한 regular function과 일치한다. ([§유리함수, ⁋명제 5](/ko/math/algebraic_geometry/rational_functions#prop5)) 이를 조금 더 확장하면 임의의 affine algebraic set일 경우에도 $\mathbb{k}[X]$는 원래 정의한 센스에서의 regular function과 같다는 것을 보일 수 있다. 

이제 더 일반적으로 quasiprojective variety에서 정의된 regular map을 정의한다. 공역이 affine set일 경우에는 어려울 것이 없다.

<div class="definition" markdown="1">

<ins id="def2">**정의 2**</ins> Quasiprojective variety $X$에서 affine space $\mathbb{A}^m$으로 가는 함수 $f=(f_1,\ldots, f_m)$이 *regular map*인 것은 각각의 $f_i$들이 모두 regular인 것이다. 

</div>

이제 일반적으로 quasiprojective variety 사이의 함수 $f:X \rightarrow Y$가 regular라는 것이 어떤 것인지를 정의해야 한다. 이를 위해서는 공역을 projective space $\mathbb{P}^m$에 넣은 후, $f(x)$를 포함하는 $\mathbb{P}^m$의 affine chart $V_i$를 잡고 $f$를 여기로 제한한 것이 regular일 것을 요구하면 된다.

<div class="definition" markdown="1">

<ins id="def3">**정의 3**</ins> Quasiprojective variety 사이의 함수 $f:X \rightarrow Y$가 주어졌다 하고, $Y\subseteq \mathbb{P}^m$이라 하자. 그럼 $f$가 *regular map*이라는 것은 임의의 $x\in X$와, $f(x)$를 포함하는 affine piece $V_i$에 대하여, $x$의 적당한 neighborhood $U$를 잡아 $f(U) \subseteq V_i$이고, $f\vert_U:U \rightarrow V_i$가 quasiprojective variety에서 affine space로의 map으로서 regular인 것이다. 

</div>

물론 이를 위해서는 위에서 정의한 regularity가 affine piece $V_i$의 선택에 의존하지 않음을 보여야 하지만, 이는 거의 자명하다. 이를 살펴보는 대신, [정의 3](#def3)을 조금 더 명시적인 형태로 바꿔보자. 주어진 regular map $f:X \rightarrow Y$와 $x\in X$, 그리고 $f(x)$를 포함하는 $\mathbb{P}^m$의 affine piece $V_i$와, $f(U)\subseteq V_i$이도록 하는 $x$의 neighborhood $U$를 고정하자. 그럼 정의에 의하여, $f$는 regular function들

$$f=(f_1,\ldots, f_m)=\left(\frac{F_0}{G_0},\ldots, \widehat{\frac{F_i}{G_i}},\ldots,\frac{F_m}{G_m}\right)=\left(\frac{P_0}{P_i},\ldots, \widehat{\frac{P_i}{P_i}},\ldots,\frac{P_m}{P_i}\right)$$

로 나타낼 수 있다. 여기서 가장 오른쪽 항은 두 번째 표현의 분모를 모두 통분하여 같은 분모들을 갖도록 맞춰준 형태이다. 이제 이를 다시 $\mathbb{P}^m$으로 돌려놓으면 $f$가 다음의 꼴

$$f(x)=(P_0(x):\cdots P_m(x))$$

으로 주어지는 것을 알 수 있다. 그럼 이 때, $P_j$들은 모두 같은 차수여야 하고, $P_j(x)\neq 0$이도록 하는 $j$가 적어도 하나는 존재해야 한다. 또 앞선 식에서 통분을 하는 방법은 유일하지 않으므로 또 다른 함수 $(Q_0:\cdots:Q_m)$이 주어졌다 할 때, $F_iQ_j=F_jQ_i$가 모든 $i,j$에 대해 성립하면 이를 같은 것으로 취급해야 한다. 

이렇게 quasiprojective variety와 이들 사이의 함수를 정의하였으므로, quasiprojective variety들의 카테고리가 존재한다. 이제 이 카테고리 안에서, affine space의 닫힌집합과 isomorphic한 quasiprojective variety를 *affine variety*, projective space의 닫힌집합과 isomorphic한 quasiprojective variety를 *projective variety*라 부른다. 지금까지 살펴본 예시와 정의들은 affine variety 혹은 projective variety에 대한 것이 대부분이고, 우리가 실제로 관심을 가지는 것들도 주로 이들 둘이기는 하지만, affine variety도, projective variety도 아닌 quasiprojective variety 또한 존재한다.

## 국소적인 성질들

기하학에서, 어떠한 성질 $P$가 *local property*라는 것은 대상 $X$의 각 점 $x\in X$의 적당한 열린집합에 대해서 $P$가 성립한다는 것을 보이면 $X$ 전체에서도 $P$가 성립하는 것을 의미한다. 완전히 동일한 상황은 아니지만, [정의 3](#def3) 또한 비슷한 맥락에서 이해할 수 있다. 우리는 조만간 이러한 성질들을 살펴보게 될 것인데, 이번 글에서는 아주 간단한 몇 가지의 경우만 살펴본다. 

<div class="proposition" markdown="1">

<ins id="lem4">**보조정리 4**</ins> Quasiprojective variety $Y\subseteq X$가 닫힌집합인 것은 local property이다. 

</div>

즉, $X=\bigcup U_\alpha$라 했을 때, $Y\cap U_\alpha$들이 $U_\alpha$ 각각에서 닫힌집합임을 보여야 한다. 이는 단순한 위상수학의 계산이므로 생략한다. 이를 이용하면 다음 보조정리 또한 자명하다. 

<div class="proposition" markdown="1">

<ins id="lem5">**보조정리 5**</ins> Quasiprojective variety의 임의의 점 $x\in X$는 항상 affine variety와 isomorphic한 neighborhood를 갖는다. 

</div>

이에 대한 증명은, 당연히 $X\subseteq \mathbb{P}^n$으로 두고 $\mathbb{P}^n$의 affine chart를 이용하면 된다. 이 과정에서는 필연적으로 projective variety (의 closed subset)의 open subset을 생각해야만 하고, 이들은 그 여집합을 정의하는 다항식이 $0$이 아니도록 하는 집합이므로 다음을 정의하는 것이 자연스럽다.

<div class="definition" markdown="1">

<ins id="def6">**정의 6**</ins> Affine variety $X$에 대하여, $D(f)=X\setminus Z(f)$를 *principal open set*이라 부른다. 

</div>

위에서 간략하게 언급한 증명을 조금 더 자세히 서술한다. 

<details class="proof--alone" markdown="1">
<summary>보조정리 5의 증명</summary>

$X\subseteq \mathbb{P}^n$으로 두고, 편의상 $x\in U_0$이라 하자. 그럼 $x\in X_0=X\cap U_0$이고, $X$가 quasiprojective라는 것으로부터 $U_0$의 두 closed subset $Y$과 $Y_1\subseteq Y$을 잡아 $X_0=Y\setminus Y_1$이라 할 수 있다. 한편 $Y_1$은 $U_0$의 closed subset이고, $x\not\in Y_1$이므로 $Y_1$에서는 $0$이지만 $x$에서의 함숫값은 $0$이 아닌 다항식 $F$를 찾을 수 있고, 이 다항식 $F$에 대하여 $D(F)$가 원하는 affine variety가 된다. 

</details>

뿐만 아니라 $D(f)$ 위에서는 $f\neq 0$이므로, $F/f$ 꼴의 함수는 $D(f)$에서는 모든 점에서 regular이므로 $D(f)$의 regular function을 정의한다. 이로부터 $\mathbb{k}[D(f)]=\mathbb{k}[X][f^{-1}]$임을 유도할 수 있다. 

<div class="example" markdown="1">

<ins id="ex7">**예시 7**</ins> $\mathbb{P}^n$ 위에 정의된 $n-d$개의 일차식으로 정의된 linear subspace $E$를 생각하자. 즉

$$E=\{L_1=\cdots=L_{n-d}=0\}$$

이다. $E$는 $d$차원 공간이므로, $\mathbb{P}^{n}$의 $(n-d-1)$차원 linear subspace 중 $E$와 만나지 않는 것이 존재한다. 이를 $H$라 하자. 그럼 함수 $\pi:\mathbb{P}^n\setminus E \rightarrow \mathbb{P}^{n-d-1}$을 다음의 식

$$\pi(x)=(L_1(x):\cdots:L_{n-d}(x))$$

으로 정의할 수 있으며, 이 함수는 regular map이 된다. 이 함수의 기하적인 의미를 보기 위해 적당한 변수변환을 통해 $\mathbb{P}^n$에서 $E$와 $H$의 방정식을

$$E=\{x_0=\cdots=x_{n-d-1}=0\},\quad H=\{x_{n-d}=\cdots=x_n=0\}$$

으로 적자. 그럼 임의의 $\xi\in \mathbb{P}^n\setminus E$는 

$$\xi=(\xi_0:\cdots:\xi_{n-d-1}:\xi_{n-d}:\cdots:\xi_n),\qquad\text{$\xi_i\neq 0$ for some $0\leq i\leq n-d-1$}$$

의 꼴로 적을 수 있으며, 따라서 $\xi$와 $E$의 한 점 $\zeta=(0:\cdots:0:\zeta_{n-d}:\cdots:\zeta_n)$를 지나는 직선은

$$(\lambda\xi_0:\cdots:\lambda\xi_{n-d-1}:\eta\zeta_{n-d}+\lambda\xi_{n-d}:\cdots:\eta\zeta_n+\lambda\xi_n)$$

의 꼴로 쓸 수 있으며, 이 직선이 $H$와 만나기 위해서는 $(\zeta_{n-d}:\cdots:\zeta_n)$과 $(\xi_{n-d}:\cdots\xi_n)$이 같을 때, 한 점 $(\xi_0:\cdots:\xi_{n-d-1}:0:\cdots:0)$에서 만나며 이것이 정확히 위에서 정의한 $\pi(x)$와 같다는 것을 안다. 

</div>

<div class="example" markdown="1">

<ins id="ex8">**예시 8**</ins> $\X_0,\ldots, \X_n$을 변수로 갖는 차수 $m$의 다항식들의 $\mathbb{k}$-벡터공간을 생각하자. 이 벡터공간은 차수 $m$의 monomial들을 basis로 가지며, 따라서 $\binom{n+m}{m}$ 차원이 된다. 

한편, 차수 $m$의 다항식은 $\mathbb{k}[\X_0,\ldots, \X_n]$이 만드는 $\mathbb{P}^n$ 안에서의 hypersurface를 정의한다. 다항식의 zero set은 다항식을 상수배 하는 것에 영향을 받지 않으므로, 이들 hypersurface를 모아둔 것은 $N=\binom{n+m}{m}-1$이라 할 때 $\mathbb{P}^N$의 한 점에 대응되는 것이라 생각할 수 있다. 이제 $\mathbb{P}^N$의 homogeneous coordinate을 $i_0+\cdots+i_n=m$을 만족하는 $i_0,\ldots,i_n$들을 이용하여 

$$v_{i_0,\ldots, i_n},\qquad i_0+\cdots+i_n=m,\quad i_k\geq 0$$

으로 주고 $v:\mathbb{P}^n \rightarrow \mathbb{P}^N$을

$$v=(v_{i_0,\ldots, i_n})_{i_0+\cdots+i_n=m}=(u_0^{i_0}\cdots u_n^{i_n})_{i_0+\cdots+i_n=m}$$

으로 정의할 수 있다. 그럼 $u_0^m,\]ldots, u_n^m$을 보면 $v$들이 모두 동시에 $0$이 될 수 없다는 것을 알고 따라서 $v$는 $\mathbb{P}^N$으로의 regular map을 정의한다. 이를 *Veronese embedding*이라 부른다. 


</div>

## 유리함수들

Quasiprojective variety $X$ 위에서의 rational function을 정의하기 위해서는 $X$가 $\mathbb{P}^n$ 안에 있는 것으로 두고 앞서 살펴본 $\mathbb{P}^n$의 rational function을 사용하면 된다. 몇가지 표기를 고정하자. 우선 $X$ 위에 정의된 rational function들 $f=P/Q$의 모임을 $\mathcal{O}_X$라 적는다. 여기에서, $Q$는 $X$ 위에서 항등적으로 $0$은 아니어야 한다. 그럼 $\mathcal{O}_X$가 ring인 것을 쉽게 보일 수 있으며, 이 때 $P$가 $X$ 위에서 항등적으로 $0$이 되는 함수들을 생각하면 이 모임은 $\mathcal{O}_X$의 maximal ideal $\mathfrak{m}_X$를 이룬다. 이로부터 다음을 정의한다.

<div class="definition" markdown="1">

<ins id="def9">**정의 9**</ins> Irreducible quasiprojective variety $X\subseteq \mathbb{P}^n$에 대하여, $\mathbb{k}(X)=\mathcal{O}_X/\mathfrak{m}_X$로 정의한다. 

</div>

## 세그레 매장

