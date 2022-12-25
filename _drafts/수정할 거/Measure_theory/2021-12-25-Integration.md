---

title: "Integration"
excerpt: "Lebesgue integration"

categories: [Math / Measure Theory]
permalink: /ko/math/measure_theory/integration
header:
    overlay_image: /assets/images/Measure_theory/Integration.png
    overlay_filter: 0.5
sidebar: 
    nav: "analysis"

date: 2021-12-25
last_modified_at:
weight: 2

published: false

---
<div class="notice--warning" markdown="1">

이 글은 현재 수정중입니다.

이 글은 예전에 쓴 글로, 서술 방향이 마음에 들지 않거나 표기법이 마음에 들지 않아 전체적으로 수정이 진행중입니다. 읽으실 때 참고해주세요.

</div>


## Simple function and approximation

우리는 지난 글에서 measurable set, measurable function 등의 개념을 정의했고, measurable set들 위에 measure를 정의했다. 이제 우리는 드디어 함수의 적분을 정의할 수 있다. 이를 위해서는 우선 다음과 같은 특별한 종류의 함수를 정의해야 한다.

<div class="definition" markdown="1">

<ins id="df1">**정의 1**</ins> Complex function $s$가 *simple function*이라는 것은 $\ims$가 유한집합인 것이다.

</div>

따라서, 어떤 집합 $X$ 위에 정의된 simple function $s$가 주어진다면, 우리는 $\ims$의 각 원소의 preimage를 생각하여 $X$를 (유한한) partition으로 나눌 수 있다. 즉, $s$는 항상 다음과 같은 표현

$$s=\sum_{i=1}^n\alpha_i 1_{A_i}$$

을 갖는다. 만일 $X$가 measurable space였고, $A_i$들이 모두 measurable이라면, $s$도 measurable이고 그 역 또한 성립한다는 것은 자명하다.

우리는 이 simple function들을 이용해서 measurable function들을 항상 approximate할 수 있다는 것을 보일 것이다. 앞서 complex-valued measurable function을 살펴보기 위해서는 항상 positive measurable function만 고려하면 된다는 이야기를 했었는데, 따라서 이 approximation 또한 positive measurable function에 대해서만 고려하면 충분하다.

<div class="proposition" markdown="1">

<ins id="pp2">**명제 2**</ins> Positive measurable function $f$에 대하여, 다음의 조건을 만족하는 simple measurable function들의 sequence $(s_n)$이 존재한다.

1. $0\leq s_1\leq s_2\leq\cdots\leq f$,
2. 임의의 $x\in X$에 대하여, $s_n(x)\rightarrow f(x)$.

</div>
<details class="proof" markdown="1">
<summary>증명</summary>

집합 $E_n^k=f^{-1}((k2^{-n}, (k+1)2^{-n}))$, $F_n=f^{-1}((2^n,\infty])$라 하고 

$$s_n=\sum_{k=0}^{2^{2n}-1}k2^{-n}1_{E_n^k}+2^n1_{F_n}$$

이라 하면 된다. 식으로는 난해해 보이지만 **[Fol]**의 47페이지에 아주 좋은 그림이 그려져 있다.[^1]

</details>

## Integration

본격적으로 적분을 정의하기 시작한다. 우선 앞서 정의한 simple function

$$s=\sum_{i=1}^n\alpha_i 1_{A_i}$$

에 대해 적분을 어떻게 정의할지는 아주 명백하다.

<div class="definition" markdown="1">

<ins id="df3">**정의 3**</ins> Measure space $(X,\mathfrak{M},\mu)$ 위에 정의된 positive simple function

$$s=\sum_{i=1}^n\alpha_i 1_{A_i}$$

와, measurable set $E$에 대하여, $s$의 $E$ 위에서의 *적분*은 다음의 식

$$\int_E s\mathop{d\mu}=\sum_{i=1}^n\alpha_i \mu(A_i\cap E)$$

으로 정의되는 값이다. 

</div>

많은 경우에 함수는 단순히 $s$가 아니라, $s(x)$ 혹은 $s(x,y)$등으로 표현된다. 만일 이런 경우, $\mu$가 어떠한 공간에서 정의된 measure인지가 불명확하다면 

$$\int_E s(x)\mathop{d\mu(x)}$$

등과 같이 적분해주는 문자를 명시적으로 표현해주기도 한다. 하지만 혼동의 여지가 없는 대부분의 경우에는 이러한 notation을 잘 사용하지 않는다.

적분의 정의에 의해, 임의의 measurable set $E\subset X$에 대하여

$$\mu(E)=\int_X 1_E\mathop{d\mu}$$

임은 자명하다. 더 일반적으로 다음을 정의한다.

<div class="definition" markdown="1">

<ins id="df4">**정의 4**</ins> Measure space $(X,\mathfrak{M},\mu)$ 위에 정의된 positive measurable function $f$, 그리고 measurable set $E$에 대하여, $f$의 $E$ 위에서의 *적분*은 다음의 식

$$\int_Ef\mathop{d\mu}=\sup_{0\leq s\leq f}\int_E s\mathop{d\mu}$$

으로 정의된다.
</div>

마지막으로 짚고 넘어가자. 만일 $f$가 complex-valued measurable function이었다면, $f$를 실수부와 허수부로 분리한 뒤, 이들 각각을 다시 양수부분과 음수부분으로 나누면, 위의 정의는 바로 complex-valued measurable function에 대해서도 확장될 수 있다.

몇 가지 성질들을 살펴보자. 

<div class="proposition" markdown="1">

<ins id="pp5">**명제 5**</ins> 

1. 만일 $0\leq f\leq g$라면 $\int_E f\mathop{d\mu}\leq\int_Eg\mathop{d\mu}$가 성립한다.
2. $A\subset B$이고 $f\geq 0$이라면 $\int_Af\mathop{d\mu}\leq\int_Bf\mathop{d\mu}$가 성립한다.
3. 만일 $f\geq 0$이고, $0\leq c<\infty$라면 다음의 식 $\int_E cf\mathop{d\mu}=c\int_Ef\mathop{d\mu}$이 성립한다.
4. 만일 $f(x)=0$이 모든 $x\in E$에 대해 성립한다면 $\int_E f\mathop{d\mu}=0$이다.
5. 만일 $\mu(E)=0$이라면, $\int_E f\mathop{d\mu}=0$이다. 
6. $\int_E f\mathop{d\mu}=\int_X f1_E\mathop{d\mu}$.

</div>

이 명제의 4번과 5번 조건이 성립하기 위해서는 $0\cdot\infty=0$이라는 식이 성립해야 한다. 일반적으로 이러한 종류의 식은 잘 정의하지 않지만, 적어도 measure sense에서는 이렇게 정의하기로 한다. 

## Monotone convergence theorem

이제 우리는 이렇게 새롭게 정의한 적분의 여러 성질들을 살펴본다. 리만적분에서, 예를 들어 다음과 같은 극한

$$\lim_{n\rightarrow\infty}\int f_n\mathop{dx}$$

을 계산하기 위해서는 특정한 성질이 만족되어야 한다. 예를 들면 $f_n$이 uniformly convergent라던지... 하지만 Lebesgue 센스에서는 상대적으로 약한 조건만 갖추어져도 적분과 극한의 순서를 교환할 수 있다. 우선 다음 보조정리를 먼저 살펴보자.

<div class="proposition" markdown="1">

<ins id="lem6">**보조정리 6**</ins> Measure space $X$에 measurable simple function $s$가 주어졌다 하자. 그럼 다음의 식

$$\mu_s(E)=\int_E s\mathop{d\mu}$$

으로 주어진 $\mu_s$는 $\mathfrak{M}$ 위에서의 measure가 된다. 

또 다른 measurable simple function $t$가 주어졌다면, 다음의 식

$$\int_X(s+t)\mathop{d\mu}=\int_Xs\mathop{d\mu}+\int_Xt\mathop{d\mu}$$

이 성립한다. 

</div>

둘 중 첫 번째 명제는 리만-스틸체스 적분에서 monotone function $g$를 이용해 $\int f \mathop{dg(x)}$를 정의한 것을 떠올리게 한다.

<details class="proof" markdown="1">
<summary>증명</summary>

우선 $\mu_s$가 $\sigma$-additivity를 만족한다는 것을 보여야 한다. 언제나처럼 

$$s=\sum_{i=1}^n\alpha_i 1_{A_i}$$

으로 잡고, $E$의 countable partition $(E\_j)\_1^\infty$를 생각하자. 그럼

$$\mu_s(E)=\sum_{i=1}^n\alpha_i\mu(A_i\cap E)=\sum_{i=1}^n\alpha_i\sum_{j=1}^\infty\mu(A_i\cap E_j)$$

이다. 그런데

$$\sum_{i=1}^n\alpha_i\sum_{j=1}^\infty\mu(A_i\cap E_j)=\sum_{i=1}^n\alpha_i\lim_{k\rightarrow\infty}\sum_{j=1}^k\mu(A_i\cap E_j)$$

이고, limit은 finite summation과 commute하고, finite summation끼리는 항상 commute하므로

$$\mu_s(E)=\lim_{k\rightarrow\infty}\sum_{i=1}^n\sum_{j=1}^k\alpha_i\mu(A_i\cap E_j)=\lim_{k\rightarrow\infty}\sum_{j=1}^k\sum_{i=1}^n\alpha_i\mu(A_i\cap E_j)=\sum_{j=1}^\infty\mu_s(E_j)$$

가 되어 첫 번째 주장이 성립한다. 두 번째는 만약

$$t=\sum_{j=1}^m\beta_j1_{B_j}$$

라면 

$$s+t=\sum_{i=1}^n\sum_{j=1}^m(\alpha_i+\beta_j)1_{A_i\cap B_j}$$

이 성립하고, $A_i\cap B_j$는 각각 $A_i$들과 $B_j$들의 partition이 되므로 자명하다.

</details>

<div class="proposition" markdown="1">

<ins id="thm7">**정리 7 (Monotone convergence theorem)**</ins> $(f_n)_1^\infty$가 다음의 두 조건

1. $0\leq f_1(x)\leq f_2(x)\leq\cdots\leq\infty$가 모든 $x$에 대해 성립하고,
2. $f_n(x)\rightarrow f(x)$.

을 만족한다면, $f$도 measurable이고 그 적분값은

$$\int_Xf_n\mathop{d\mu}\rightarrow\int_Xf\mathop{d\mu}$$

를 만족한다.

</div>
<details class="proof" markdown="1">
<summary>증명</summary>

우선, $\int f_n\leq\int f_{n+1}$이므로, ($\infty$를 포함해서) 수열 $\int_X f_n\mathop{d\mu}$가 수렴하는 것은 자명하다. 이 수렴값을 $\alpha$라 하면, 모든 $n$에 대해 $\int f_n\leq \int f$가 성립하므로 $\alpha\leq\int f$인 것은 자명하다. 이 정리의 핵심은 반대방향 부등식이다.

$c\in (0,1)$을 하나 고정하자. $0\leq s\leq f$를 만족하는 임의의 simple measurable function $s$에 대하여, 다음의 집합

$$E_n=\{x:f_n(x)\geq cs(x)\}$$

은 두 measurable function의 크기비교로 나타나는 집합이므로 measurable하다. 또, $f_n\leq f_{n+1}$이므로, 이 집합들은 $E_1\subset E_2\subset\cdots$이다. 또, $s\leq f$이므로, 임의의 $x\in X$에 대해 $f_n(x)\geq s(x)\geq cs(x)$인 $n$이 각각 존재할 것이다. 즉, $X=\bigcup E_n$이다. 그럼

$$\int_X f_n\mathop{d\mu}\geq\int_{E_n}f_n\mathop{d\mu}\geq c\int_{E_n}s\mathop{d\mu}$$ 

가 성립하므로, $n\rightarrow\infty$이면 좌변은 $\alpha$로 가며, 우변은 $s$를 구성하는 각각의 measurable set에 measure의 continuity from below ([§Measurable sets, 명제 11의 4](/ko/math/measure_theory/measurable_sets#pp11))를 적용하면 $c\int_X s\mathop{d\mu}$가 된다. 즉,

$$\alpha\geq c\int_X s\mathop{d\mu}$$

가 임의의 $c<1$에 대해 성립하므로, $c=1$일 때에도 성립하며, $s$는 $0\leq s\leq f$를 만족하는 임의의 simple measurable function이므로 원하는 대로 반대쪽 부등식이 완성되었다.
</details>


다음 따름정리는 우리가 어떤 measurable function에 대한 명제를 증명할 때 사용하는 standard한 테크닉을 사용한다는 점에서 그 증명을 살펴볼 가치가 있다. 

<div class="proposition" markdown="1">

<ins id="crl8">**따름정리 8**</ins> Positive measurable function들의 sequence $(f_n)_1^\infty$에 대하여, 

$$f(x)=\sum_{n=1}^\infty f_n(x)$$

는 measurable이며, 또

$$\int_Xf\mathop{d\mu}=\sum_{i=1}^\infty\int_Xf_n\mathop{d\mu}$$

가 성립한다.

</div>
<details class="proof" markdown="1">
<summary>증명</summary>

우선 유한한 경우를 먼저 살펴보자. 즉 우리는 먼저 

$$\int_X (f_1+f_2)\mathop{d\mu}=\int_X f_1\mathop{d\mu}+\int_X f_2\mathop{d\mu}$$

를 보이려 한다. 이 식은 우리가 [보조정리 6](#lem6)에서 이미 simple function에 대해 보인 식이므로, 이에 착안하여 두 개의 simple function들의 sequence $(s_n),(t_n)$을 $s_n\nearrow f_1$, $t_n\nearrow f_2$이도록 잡자. (이는 [명제 2](#pp2)에 의해 가능하다.) 그럼 $(s_n+t_n)\nearrow (f_1+f_2)$이며, 따라서 MCT에 의하여 위의 식을 얻는다.

이제 남은 것은 이를 무한한 경우로 확장하는 것인데, 다시 ($x$에 대한) 함수 $s_n(f)$를

$$s_n(f)(x)=f_1(x)+\cdots+f_n(x)$$

로 정의하면 $s_n(f)\nearrow f$이고 따라서 MCT에 의해 원하는 명제가 성립한다.

</details>

만일 $\mu$가 countable set $\\{1,2,\ldots\\}$에 대한 counting measure라면, 위 정리는 그냥 간단하게

$$\sum_{i=1}^\infty\sum_{j=1}^\infty a_{ij}=\sum_{j=1}^\infty\sum_{i=1}^\infty a_{ij},\qquad\text{$a_{ij}\geq 0$ for each $i,j$}$$

가 된다. 

<div class="proposition" markdown="1">

<ins id="crl9">**따름정리 9**</ins> 만일 $f$가 positive measurable function이라면 다음의 식

$$\mu_f(E)=\int_Ef\mathop{d\mu}$$

으로 정의된 $\mu_E$는 $\mathfrak{M}$ 위에서 정의된 measure다. 또, 임의의 positive measurable function $g$에 대해 다음의 식

$$\int_Xg\mathop{d\mu_f}=\int_Xgf\mathop{d\mu}$$

가 성립한다.

</div>

우리는 simple function에 대해 이와 유사한 명제 ([보조정리 6](#lem6))를 소개하며, 이걸 스틸체스 적분에서의 change of variable 비슷한 느낌이라 언급했었는데, 따름정리의 두 번째 주장이 이를 정당화한다. 

<details class="proof" markdown="1">
<summary>증명</summary>

우선 $\mu_f$가 $\sigma$-additivity를 만족함을 보여야 한다. 이를 위해 $E=\bigcup E_i$이고 $E_i$들이 mutually disjoint라 하자. 그럼 $1_E=\sum 1_{E_i}$이고, 따라서

$$\mu_f(E)=\int_Ef\mathop{d\mu}=\int_X 1_Ef\mathop{d\mu}=\int_X\sum_{i=1}^\infty 1_{E_i}f\mathop{d\mu}$$

이고, 앞선 따름정리를 적용하면 $\mu_f$가 $\sigma$-additivity를 만족함을 안다. 즉 $\mu_f$는 실제로 measure가 된다. 

이제 두 번째 식을 보여야 한다. 그런데 이 식이 어떤 measurable set $F$의 characteristic function $g=1_F$에 대해 성립한다는 것은 다음의 식

$$\int_X 1_F\mathop{d\mu_f}=\mu_f(F)=\int_F f\mathop{d\mu}=\int_X 1_Ff\mathop{d\mu}$$

에 의해 자명하고, 또 우리가 보였던 simple function에 대한 적분의 linearity에 의해 ([보조정리 6](#lem6)의 두 번째) 이들 characteristic function들에 대해 성립하는 명제는 임의의 simple, measurable function에 대해서도 성립한다. 이제 마지막으로 임의의 measurable function $g$에 대해, $s_n\nearrow g$인 simple measurable function들을 잡은 후 MCT를 적용하면 원하는 결과를 얻는다. 

</details>
마지막으로 Fatou's lemma라 불리는 보조정리를 하나 살펴보자. 이 보조정리의 결과는 앞선 MCT나, 앞으로 소개할 DCT보다는 약하지만, 이들과는 달리 조건이 아무것도 필요하지 않다는 점에서 강력하다.

<div class="proposition" markdown="1">

<ins id="lem10">**보조정리 10 (Fatou)**</ins> Positive measurable function들의 sequence $(f_n)_1^\infty$에 대하여,

$$\int_X\liminf f_n\mathop{d\mu}\leq\liminf\int_X f_n\mathop{d\mu}.$$

</div>
<details class="proof" markdown="1">
<summary>증명</summary>

함수 $g_k$를 다음의 식 $g_k(x)=\inf_{i\geq k}f_i(x)$으로 정의하자. 그럼 정의에 의해 $g_k\leq f_k$임은 자명하므로 다음의 부등식

$$\int_X g_k\mathop{d\mu}\leq\int_X f_k\mathop{d\mu}$$

이 성립한다. 뿐만 아니라, $k$가 증가함에 따라 $\inf$를 취하는 범위는 줄어들게 되므로, $g_1\leq g_2\leq\cdots$가 성립한다. 이 때 $g_k$들의 극한값은 $g=\liminf f_n(x)$이므로, MCT에 의해 

$$\lim_{k\rightarrow\infty}\int_X g_k\mathop{d\mu}=\int_X\lim_{k\rightarrow\infty}g_k\mathop{d\mu}=\int_X\liminf_{n\rightarrow\infty} f_n\mathop{d\mu}$$

가 되고, 따라서 원하는 결론을 얻는다.

</details>

Dominated convergence theorem이 우리가 마지막으로 소개할 convergence theorem인데, 이를 위해서는 먼저 다음을 정의해야 한다.

<div class="definition" markdown="1">

<ins id="df11">**정의 11**</ins> $L^1(\mu)$는 다음의 식

$$\int_X\lvert f\rvert\mathop{d\mu}<\infty$$

를 만족하는 모든 complex measurable function $f$들의 모임이다.

</div>

$f\in L^1(\mu)$를 $f=u+iv$와 같이 표현하자. 그럼 언제나와 같이,

$$\int_E f\mathop{d\mu}=\int_E u\mathop{d\mu}+i\int_Ev\mathop{d\mu}$$

으로 쓸 수 있고, 각각의 real-valued measurable function들을 positive와 negative part로 분리하면

$$\int_E f\mathop{d\mu}=\int_E u^+\mathop{d\mu}-\int_E u^-\mathop{d\mu}+i\int_Ev^+\mathop{d\mu}-i\int_E v^-\mathop{d\mu}$$

으로 쓸 수 있다. 어렵지 않게 이들 각각이 유한하다는 것을 보일 수 있다. 예를 들어, $u^+\leq\lvert u\rvert\leq\lvert f\rvert$이다. 한편 $L^1(\mu)$는 (더 일반적으로 $L^p(\mu)$는) normed vector space의 구조를 가지는데, vector space의 구조는 우리가 쉽게 체크해볼 수 있다. 

<div class="proposition" markdown="1">

<ins id="pp12">**명제 12**</ins> $f,g\in L^1(\mu)$이고 $\alpha,\beta\in\mathbb{C}$라 하자. 그럼 $\alpha f+\beta g\in L^1(\mu)$이고, 적분값은

$$\int_X(\alpha f+\beta g)\mathop{d\mu}=\alpha\int_X f\mathop{d\mu}+\beta\int_X g\mathop{d\mu}$$

으로 주어진다.

</div>
<details class="proof" markdown="1">
<summary>증명</summary>

우선 $\alpha f+\beta g\in L^1(\mu)$인 것부터 보여야 한다. Triangle inequality로부터,

$$\int_X \lvert\alpha f+\beta g\rvert\mathop{d\mu}\leq\int_X\lvert\alpha\rvert\lvert f\rvert+\lvert\beta\rvert\lvert g\rvert\mathop{d\mu}$$

이고, 우리는 positive measurable function들에 대해서는 linearity를 증명했으므로 좌변을 $\lvert\alpha\rvert\int\lvert f\rvert\mathop{d\mu}+\lvert\beta\rvert\int\lvert g\rvert\mathop{d\mu}$으로 bound시킬 수 있고, $f,g\in L^1(\mu)$이므로 원하던 대로 $\alpha f+\beta g\in L^1(\mu)$이다. (따라서 $L^1(\mu)$는 vector addition과 scalar multiplication에 대해 닫혀있다.)

이제 이 값들이 실제로 주어진 식을 만족한다는 것을 보여야 하는데, 이 식은 우리가 이미 positive measurable function에 대해서는 보였으므로 자명하다. 더 자세히 이야기하자면, 우선 $f,g$를 real, imaginary part로 나누면 $f,g$가 real measurable인 경우만 증명하면 충분한데, $h=f+g$라 두고

$$h^+-h^-=f^+-f^-+g^+-g^-$$

라 한 후 양 변을 적당히 이항하여

$$h^++f^-+g^-=f^++g^++h^-$$

으로 두면, 이들 양 변의 적분은 positive measurable function들의 적분이므로 linearity를 적용해서

$$\int h^++\int f^-+\int g^-=\int f^++\int g^++\int h^-$$

로 적은 후, 원래대로 자리를 찾아 돌려주면 원하는 결과를 얻는다. Scalar multiplication의 경우에도 이와 유사하다. 

</details>

또, 이 명제를 이용하면 다음과 같이 "당연히" 성립해야 할 부등식 또한 얻을 수 있다.

<div class="proposition" markdown="1">

<ins id="crl13">**따름정리 13**</ins> $f\in L^1(\mu)$에 대하여 항상

$$\left\lvert\int_Xf\mathop{d\mu}\right\rvert\leq\int_X\lvert f\rvert\mathop{d\mu}$$

가 성립한다.

</div>
<details class="proof" markdown="1">
<summary>증명</summary>

$z=\int_Xf\mathop{d\mu}$라 하자. $f\in L^1(\mu)$이므로, $z$는 유한한 complex number가 된다. 이제 $\alpha=\frac{\lvert z\rvert}{z}$라 하자. 함수 $\alpha f$의 real part를 $u$라 하면, 

$$u\leq\lvert\alpha f\rvert=\lvert f\rvert$$

으로부터

$$\left\lvert\int_X f\mathop{d\mu}\right\rvert=\alpha\int_Xf\mathop{d\mu}=\int_X\alpha f\mathop{d\mu}$$

를 얻고, $\alpha f$의 적분값은 *실수* $\lvert z\rvert$이므로 $\alpha f$를 적분한 것은 그 real part $u$만 적분한 것과 같은 값을 가진다. 따라서

$$\left\lvert\int_Xf\mathop{d\mu}\right\rvert=\int_X u\mathop{d\mu}\leq \lvert f\rvert\mathop{d\mu}$$

이므로 원하는 결과를 얻는다. 

</details>

## The space $L^1(\mu)$

우리는 앞서 $L^1(\mu)$가 normed vector space의 구조를 갖는다고 주장했고, 이 중 $L^1$이 vector space라는 것은 이미 증명까지 마쳤다. 남은 부분은 $L^1(\mu)$에 norm을 주는 부분이다. $L^1(\mu)$에는 자명하게 원점 $0$ (즉 모든 $x\in X$에 대해 함숫값이 0인 함수)이 존재하므로, 여기에 normed space 구조를 주는 것은 metric을 주는 것과 동일하다. 임의의 $f,g\in L^1(\mu)$에 대하여, $f$와 $g$ 사이의 거리 $d(f,g)$는 다음과 같이 주어진다.

$$d(f,g)=\int_X\lvert f-g\rvert\mathop{d\mu}$$

Metric의 성질 중, $d\geq 0$인 것은 자명하다. 또, $d(f,g)=d(g,f)$도 마찬가지로 자명하며, triangle inequality의 경우도

$$d(f,h)=\int_X\lvert f-h\rvert\mathop{d\mu}\leq\int_X \lvert f-g\rvert+\lvert g-f\rvert\mathop{d\mu}=d(f,g)+d(g,h)$$

이므로 자명하다. 문제는 $d(f,g)=0$이라 해서 $f=g$가 성립하지는 않을 수도 있다는 것이다.[^2]

<div class="example" markdown="1">

<ins id="ex14">**예시 14**</ins> 예를 들어, measure space $(X,\mathcal{P}(X), \delta_a)$를 생각하자. Simple function $1_y$를

$$1_y(x)=\begin{cases}0&\text{if $x\neq y$}\\ 1&\text{if $x=y$}\end{cases}$$

으로 정의하면, 집합 $\\{y\\}$가 measurable이므로 $1_y(x)$는 simple measurable function이고, 그 적분은 다음의 식

$$\int_X 1_y\mathop{d\delta_a}=\delta_a(\{y\})=\begin{cases} 1&\text{y=a}\\ 0&\text{otherwise}\end{cases}$$

으로 잘 정의되므로 (그리고 $1_y$는 positive이므로) $1_y\in L^1(\delta_a)$이다. 

이제 $X$가 서로 다른 세 개 이상의 원소를 갖는다 가정하고, $a$가 아닌 서로 다른 두 원소 $b,c$를 택하자. 그럼 $1_b$, $1_c$는 모두 simple measurable function이며, 

$$\lvert 1_b(x)-1_c(x)\rvert=\begin{cases}1&\text{$x=b$ or $c$}\\ 0&\text{otherwise}\end{cases}$$

이 된다. 역시 집합 $\\{b,c\\}$가 measurable이므로 이 함수 또한 simple measurable function이며, 적분은 다음의 식

$$\int_X\lvert 1_b-1_c\rvert\mathop{d\delta_a}=\delta_a(\{b,c\})=0$$

으로 주어진다. 즉, $d(1_b,1_c)=0$이다. 하지만 $b\neq c$이므로, 당연히 함수로서 $1_b\neq 1_c$이다.
</div>

이러한 문제가 생기는 이유는, 간단히 말해서 우리의 $d$는 적분을 통해 정의되었는데, measure가 0인 집합 위에서의 함숫값은 적분값에 어떠한 영향도 미치지 않기 때문이다. 따라서, 우리 문제는 measure zero set 위에서만 다른 두 함수를 같게 본다면 해결될 것이다. 더 일반적으로 다음을 정의한다.

<div class="definition" markdown="1">

<ins id="df15">**정의 15**</ins> Measure space $(X,\mathfrak{M},\mu)$ 위에 어떤 성질 $P$가 주어졌다 하자. 만일 어떠한 measurable set $N$이 존재하여, $\mu(N)=0$이고, $P(x)$가 $X\setminus N$에서는 항상 참이라면 이 성질이 *$\mu$-almost everywhere* 성립한다고 한다. 더 일반적으로, 어떤 measurable set $E\subset X$에 대해 성질 $P$가 $\mu$-a.e. 성립한다는 것은 어떤 measure zero set $N\subset E$가 존재하여 $E\setminus X$에서는 항상 $P$가 참인 것이다.

</div>

그럼 *measure zero set 위에서만 다른 두 함수를 같게 보는 것*은 

> $f\sim g$ iff $f=g$ almost everywhere

인 relation을 생각하는 것과 같다. 

<div class="proposition" markdown="1">

<ins id="lem16">**보조정리 16**</ins> 위의 relation $\sim$은 $L^1(\mu)$ 위에 정의된 equivalence relation이다.

</div>

이 보조정리는 증명하기가 어렵지는 않지만, 약간의 comment를 하고 나서 증명을 하자. 

이 보조정리를 증명하고 나면, $L^1(\mu)$가 가지고 있는 vector space 구조가 $\sim$으로 quotient했을 때 잘 작동하는지가 궁금할 것이다. 예를 들어, 

> 만일 $f_1\sim f_2$이고 $g_1\sim g_2$라면 $(f_1+g_1)\sim (f_2+g_2)$일까? 만일 $f\sim g$라면, 임의의 상수 $\alpha\in\mathbb{C}$에 대해 $\alpha f\sim \alpha g$일까? 

이 질문들에 대한 대답 또한 본질적으로 어렵지는 않지만 앞선 보조정리의 증명과 비슷한 주의가 필요하다. (둘째 주장은 별로 주의할 필요 없이 자명하다.)

아무튼 결과적으로 $L^1(\mu)$ 위에 정의된 equivalence relation $\sim$은 vector addition과 scalar multiplication을 잘 보존해주며, 따라서 quotient space 또한 $\mathbb{C}$-vector space가 된다. 약간의 abuse of language를 통해, 이 quotient space를 마찬가지로 $L^1(\mu)$으로 생각하면 $L^1(\mu)$가 normed vector space라는 우리의 생각이 증명된다.

## Complete measure space

이제 미뤄뒀던 [보조정리 16](#lem16)의 증명을 두 단계로 나누어 설명한다. 아이디어는 직관적으로 자명하지만, 주의해야 할 부분이 있다.

<details class="proof--alone" markdown="1">
<summary>보조정리 16의 증명</summary>

우선 임의의 $f\in L^1(\mu)$에 대하여 $f\sim f$인 것은 자명하다. Symmetry 또한 말장난. 따라서 transitivity만 보이면 된다. $f\sim g$이고 $g\sim h$라 하자. 즉 다음의 두 집합

$$E_1=\{x\in X:f(x)\neq g(x)\},\qquad E_2=\{x\in X:g(x)\neq h(x)\}$$

이 모두 measure zero set이다. 그럼 다음의 집합

$$E_3=\{x\in X:f(x)\neq h(x)\}$$

은 $E_1\cup E_2$에 포함된 집합이므로, $\mu$의 monotonicity에 의해 $\mu(E_3)=0$이고 따라서 증명 끝.

</details>

이 증명의 문제점은 $E_3$이 measurable이라는 보장이 없다는 것이다. 따라서, 위와 같이 증명을 완료하려면 사실 다음을 보여야 한다.

> 집합 $E_3$은 measurable이다.

<details class="proof" markdown="1">
<summary>증명</summary>

두 함수 $f,h$는 모두 measurable function들이므로, 

$$E_3^{+\infty}=\{x\in X:f(x)=h(x)=\infty\},\qquad E_3^{-\infty}=\{f(x)=h(x)=-\infty\}$$

는 모두 measurable set이다. 예를 들어,

$$E_3^{+\infty}=f^{-1}(\{+\infty\})\cap h^{-1}(\{+\infty\})$$

이고 $\{+\infty\}$는 closed set이므로 $E_3^{+\infty}$는 두 measurable set의 교집합이므로 measurable이다. 한편 $E_3$의 남은 부분 

$$E_3^\fin=X\setminus(E_3^{+\infty}\cup E_3^{-\infty})$$

은 $f,h$의 값이 finite이고 $f(x)=h(x)$인 부분인데, 이 부분에서 $f-h$는 잘 정의되므로, $E_3^\fin=(f-h)^{-1}(\\{0\\})$이고 따라서 measurable이다.

</details>

방금 전의 argument를 약간 수정하면, 앞선 section에서 우리가 남겨둔 질문, 즉

> $f_1\sim f_2$, $g_1\sim g_2$라면 $(f_1+g_1)\sim(f_2+g_2)$?

에 대한 대답도 쉽게 증명할 수 있다. 물론 이 경우에는, 예를 들어 $f_1+g_1$이 $\infty$인 곳에서는 $f_1$이 무한대이거나, $g_1$이 무한대이거나, 혹은 둘 다 이므로 조금 더 경우를 나눠야 하긴 하지만 본질적으로 증명이 어렵지는 않다.

그런데, 사실 어떤 집합의 부분집합이 (어떻게 생겼든 간에) 크기가 작아야 한다는 것은 좀 당연한 사실같아 보인다. 

<div class="definition" markdown="1">

<ins id="df17">**정의 17**</ins> 어떤 measure space $(X,\mathfrak{M},\mu)$에 대해, 

> 만일 $\mu(E)=0$이라면, 임의의 $N\subset E$에 대해 $N\in\mathfrak{M}$이고 $\mu(N)=0$

이 성립한다면, 이 공간이 *complete*하다고 부른다.

</div>

Complete이 아닌 measure space $(X,\mathfrak{M},\mu)$가 주어졌다 하자. 그럼 $\mathfrak{M}$에, measure zero set들의 임의의 부분집합을 모두 추가하면 complete measure space를 얻을 수 있지 않을까? 그런데 이렇게 새로운 집합 $N$을 추가하고 나면, 예를 들어 measure가 0이 아니었던 집합 $A$에 대해 $A\cup N$도 $\mathfrak{M}$에 추가해 주어야 할 것이고...

물론 $\mathfrak{M}$에 이러한 집합들 $N$을 모두 추가한 후, 이 합집합에 의해 generate된 $\sigma$-algebra를 생각해도 되겠지만, **[Rud]**와 같이 처음부터 이런 집합들을 모두 추가해버리는 것이 아무래도 좀 더 깔끔하다. 

<div class="proposition" markdown="1">

<ins id="pp18">**명제 18**</ins> 임의의 measure space $(X,\mathfrak{M},\mu)$에 대하여, $\mathfrak{M}^*$을 

> 어떤 $A,B\in\mathfrak{M}$이 존재하여, $A\subset E\subset B$이고 $\mu(B\setminus A)$인 집합 $E$들의 모임

으로 정의하자. 또, $\mu(E)=\mu(A)$라 정의하자. 그럼 $\mathfrak{M}^\*$은 $\sigma$-algebra이고, 새롭게 정의한 $\mu$는 $\mathfrak{M}^\*$ 위에서의 measure가 된다.

</div>
<details class="proof" markdown="1">
<summary>증명</summary>

우선, $\mu(E)$의 값이 임의의 $E\in\mathfrak{M}^*$에 대해 잘 정의되었다는 것을 보이자. 즉, 만일 $A_1\subset E\subset B_1$, $A_2\subset E\subset B_2$이고, $\mu(B_2\setminus A_2)=\mu(B_1\setminus A_1)=0$이라면 $\mu(E)$는 $\mu(A_1)$으로 정의하든, $\mu(A_2)$으로 정의하든 같은 값이 나와야 한다.

다음의 포함관계

$$A_2\setminus A_1\subset E\setminus A_1\subset B_1\setminus A_1$$

로부터, $\mu(A_2\setminus A_1)\leq\mu(B_1\setminus A_1)=0$이고 따라서

$$\mu(A_2)=\mu(A_1\cap A_2)+\mu(A_2\setminus A_1)$$

으로부터 $\mu(A_2)=\mu(A_1\cap A_2)$가 성립한다. 마찬가지로 $\mu(A_1)=\mu(A_1\cap A_2)$이므로, 원하는 대로 $\mu(A_1)=\mu(A_2)$가 성립한다.

이제 $\mathfrak{M}^\*$이 $\sigma$-algebra임을 보여야 한다. 우선, $X\in\mathfrak{M}^\*$임은 자명하다.  
$E\in\mathfrak{M}^\*$이라 하자. 그럼 어떤 $A,B\in \mathfrak{M}$이 존재하여 $A\subset E\subset B$이고 $\mu(B\setminus A)=0$이다. 그런데, 이제 $B^c\subset E^c\subset A^c$이고, $A^c\setminus B^c=B\setminus A$이므로 $E^c\in\mathfrak{M}^\*$이다.  
마지막으로 $E_i$들이 $\mathfrak{M}^\*$의 원소들이라 하자. 그럼 $A_i\subset E_i\subset B_i$를 만족하는 $\mathfrak{M}$의 원소들 $A_i$, $B_i$가 존재하며, 또 이들은 $\mu(B_i\setminus A_i)=0$을 만족한다. 이제 $A=\bigcup A_i$, $B=\bigcup B_i$, $E=\bigcup E_i$라 하면 $A\subset E\subset B$이고

$$B\setminus A=\bigcup_{i=1}^\infty(B_i\setminus A)\subset\bigcup_{i=1}^\infty(B_i\setminus A_i)$$

가 된다. 이제 $\mu(\bigcup (B_i\setminus A_i))=0$이므로 ($C_n=\bigcup_1^n(B_i\setminus A_i)$으로 두고 continuity from below), $\mu(B\setminus A)=0$이다. 

이제 마지막으로 우리가 새로 정의한 $\mu$가 measure라는 것을 보여야 하는데, 다행히 이 부분은 쉽다. 만일 $E_i$들이 disjoint한 $\mathfrak{M}^\*$의 원소들이라면, $A_i\subset E_i\subset B_i$를 만족하는 $A_i\in\mathfrak{M}$들도 disjoint할 것이므로 (원래) $\mu$의 $\sigma$-additivity에 의하여

$$\mu(E)=\mu(A)=\sum_{i=1}^\infty\mu(A_i)=\sum_{i=1}^\infty\mu(E_i).$$

</details>

마지막으로, 우리가 적분에 대해 증명하는 모든 결과들은 $\mu$-a.e. 센스에서도 참이 된다는 것을 언급하고 다음 섹션으로 넘어가자.

## Dominated convergence theorem

원래의 궤도로 돌아와 dominated convergence theorem을 보인다.

<div class="proposition" markdown="1">

<ins id="thm19">**정리 19 (Dominated convergence theorem)**</ins> Complex measurable function들의 sequence $(f_n)_1^\infty$와, 그 극한 $f(x)=\lim f_n(x)$가 주어졌다 하자. 만약 어떤 $g\in L^1(\mu)$가 존재하여, 모든 $n$과 모든 $x$에 대해

$$\lvert f_n(x)\rvert\leq g(x)$$

를 만족한다면, $f\in L^1(\mu)$이며, 그 적분값은

$$\int_X f\mathop{d\mu}=\lim_{n\rightarrow\infty}\int_X f_n\mathop{d\mu}$$

으로 주어진다. 뿐만 아니라, 다음의 식

$$\lim_{n\rightarrow\infty}\int_X\lvert f_n-f\rvert\mathop{d\mu}=0$$

도 성립한다.

</div>
<details class="proof" markdown="1">
<summary>증명</summary>

<#content#>

</details>

DCT의 마지막 결론은 $L^1(\mu)$에서 정의된 metric 상에서 $f_n$이 $f$로 수렴한다는 것을 의미한다.

## Construction of Lebesgue measure

마지막으로 우리의 숙원사업인 Lebesgue measure를 정의할 수 있다. 이는 매우 강력한 다음의 정리에 의해 가능하다.

<div class="proposition" markdown="1">

<ins id="thm20">**정리 20 (Riesz)**</ins> Locally compact, Hausdorff space $X$가 주어졌다 하자. 만일 $\Lambda$가 compactly supported continuous function들의 (complex) vector space $C_c(X)$ 위에서 정의된 positive linear functional[^3]이라면, $X$의 Borel $\sigma$-algebra를 포함하는 적당한 $\sigma$-algebra $\mathfrak{M}$과, $\mathfrak{M}$ 위에 정의된 유일한 positive measure $\mu$가 존재하여 다음의 식

$$\Lambda f=\int_X f\mathop{d\mu}\qquad\text{ for all $f\in C_c(X)$}$$

을 만족한다. 또, 이들은 다음을 만족한다.
  
1. 임의의 compact set $K$에 대하여, $\mu(K)<\infty$.
2. (Outer regularity) 임의의 $E\in\mathfrak{M}$에 대하여, $\mu(E)=\inf\\{\mu(V): E\subset V, \text{$V$ is open in $X$}\\}$.
3. (Inner regularity) 임의의 open set $E$, 혹은 $\mu(E)<\infty$를 만족하는 임의의 $E\in\mathfrak{M}$에 대하여, $\mu(E)=\sup\\{\mu(K): K\subset E, \text{$K$ is compact in $X$}\\}$.
4. (Completeness) 만일 $\mu(E)=0$이라면 임의의 $A\subset E$에 대해 $A\in\mathfrak{M}$.

</div>

하지만, Riesz representation theorem의 증명과, 이 construction은 증명이 굉장히 길어서 이야기의 흐름을 끊어놓으므로 이 내용은 다음 글에 증명을 따로 분리해두기로 하고, 이를 이용해 Lebesgue measure를 만들기만 하자.

우선 약간의 약속이 필요하다. $\mathbb{R}^d$의 부분집합 $W$가 *$d$-cell*이라는 것은 $W$가 다음의 식

$$W=\{x=(x_1,\ldots, x_d):x_i\in I_i,\text{ $I_i$ interval}\}$$

꼴로 표현되는 것이다. 여기서 $I_i$는 open일 수도, closed일수도, half-open half-closed일 수도 있다. 이들 중 각 $I_i$들이 모두 $[a_i,a_i+\delta)$꼴인 $d$-cell들을 *$a=(a_1,\ldots, a_n)$을 꼭짓점으로 갖는 $\delta$-box*라 부르자. 

이제, $P_n$을 $\mathbb{R}^d$의 점 중 각 좌표들이 $2^{-n}$의 배수인 점들의 모임이라 하고 (즉, $P_n$은 길이 $2^{-n}$짜리 격자점들이다.) $\Omega_n$을 $P_n$의 각 원소들을 꼭짓점으로 갖는 $2^{-n}$-box라 하자. 다음 사실들은 자명하다.

1. 각각의 $n$에 대하여, 임의의 $x\in\mathbb{R}^d$를 포함하는 $\Omega_n$의 유일한 원소가 존재한다.
2. $m<n$이고 $Q\in\Omega_m$, $Q'\in\Omega_n$이라 하자. 그럼 $Q'\subset Q$이거나, $Q'\cap Q=\emptyset$이다.
3. $m<n$이라 하자. 임의의 $Q\in\Omega_n$에 대하여, $Q$에 포함된 $P_n$의 원소는 $2^{(n-r)d}$개이다.
4. $\mathbb{R}^d$의 임의의 open set은 $\Omega=\bigcup\Omega_n$의 disjoint한 원소들의 합집합으로 나타낼 수 있다.

그리고, 우리는 $2^{-r}$-box들은 모두 부피 

$$\volQ=2^{-rd},\qquad Q\in\Omega_r$$

를 갖는다고 생각할 것이다. 더 일반적으로, 임의의 $d$-cell

$$W=\{x=(x_1,\ldots, x_d):x_i\in I_i,\text{ $I_i$ interval}\}$$

은, 만일 $I_i$의 양 끝점이 $a_i\leq b_i$라면, 부피

$$\volW=\prod_{i=1}^d (b_i-a_i)$$

를 갖는다고 생각할 수 있다.

<div class="proposition" markdown="1">

<ins id="thm21">**정리 21**</ins> $\mathbb{R}^d$ 위에 $\sigma$-algebra $\mathfrak{M}$과 complete measure $m$을 다음의 성질

1. 임의의 $d$-cell $W$에 대하여, $m(W)$는 정확히 $W$의 부피와 같다.
2. $\mathfrak{M}$은 임의의 Borel set을 모두 포함하며, regularity (앞선 정리의 2번과 3번)가 임의의 measurable set에 대해 성립한다.
3. $m$은 translation invariant다. 즉, 임의의 measurable set을 평행이동한 집합은 마찬가지로 measurable이고 이는 원래의 집합의 measure와 동일하다.
4. 임의의 linear transformation $T$에 대하여[^4], measurable set $E$의 image $T(E)$는 measurable set이며, 그 measure는 $\lvert\det(T)\rvert m(E)$.   

을 만족하도록 정의할 수 있다. 
</div>
<details class="proof" markdown="1">
<summary>증명</summary>

아이디어 자체는 꽤나 간단하다. 어떻게 생겼을지 모르는 집합에 대해서는 적분을 정의하기 까다로워도, 우리는 어떤 box 위에서는 리만적분을 어떻게 정의하는지 알고 있고, 리만적분은 결국에는 positive linear functional이므로 Riesz representation theorem을 적용한다면 원하는 measure $m$과 $\sigma$-algebra $\mathfrak{M}$을 얻을 것이다. 우리가 앞서 $\delta$-box니, 어쩌니 하는 것을 정의한 것은 이 리만적분을 엄밀하게 정의하기 위해서다.

아무튼 시작하자. 임의의 $f\in C_c(\mathbb{R}^d)$에 대해, 

$$\Lambda_n f=2^{-nd}\sum_{x\in P_n} f(x)$$

으로 정의하자. $f$가 continuous이므로 이 값은 domain을 한 변의 길이가 $2^{-n}$인 $d$-cube들로 나눈 일반적인 리만적분으로 생각할 수 있다.

우리는 우선 $C_c(\mathbb{R}^d)$는 이와 같은 센스에서 리만적분이 가능하다는 것을 보인다. $f$가 real-valued, compactly supported라 하고, $W$가 $\suppf$를 포함하는 $d$-cell이라 하자. $f$는 compactly supported continuous이므로 uniformly continuous이고, 따라서 충분히 큰 $N$에 대하여, (i) $\Omega_N$의 각 원소들에 restrict했을 때는 constant function이고, (ii) $g\leq f\leq h$, (iii) $h-g<\epsilon$ 이도록 하는 두 함수 $g,h$가 존재한다. 예컨대 $d=1$이었다면 이는 구분구적법에서 얻어지는 상적분/하적분의 모양과 동일할 것이다. 따라서, 임의의 $n>N$에 대해 넓이를 직접 대입하여 계산하면

$$\Lambda_Ng=\Lambda_ng\leq\Lambda_nf\leq\Lambda_nh=\Lambda_Nh$$

가 성립한다. 그리고 (iii) 조건에 의하여 $\Lambda_nf$의 상적분과 하적분 값의 차이는 커봐야 $\epsilon\volW$이고, 따라서 $\Lambda f=\lim_{n\rightarrow}\Lambda_nf$가 존재한다.

이 때, $\Lambda$가 positive linear functional이 된다는 것은 자명하므로, Riesz representation theorem을 $\Lambda$에 사용하면 measure $m$, $\sigma$-algebra $\mathfrak{M}$이 얻어진다. 그럼 $m$이 complete이라는 것은 Riesz theorem의 직접적인 결과이다. 또, 아직 증명하진 않았지만 2번의 경우, Riesz representation을 증명하며 $\mathbb{R}^d$가 갖는 특정한 성질 때문에 성립한다는 것을 알게 될 것이다. 따라서, 이를 제외하면 1, 3, 4번만 보이면 충분하다.

우선 1번을 보이자. $W$를 다음의 open $d$-cell 

$$W=\{x=(x_1,\ldots, x_d):x_i\in (a_i,b_i)\}$$

이라 하자. 그럼 각각의 $r$마다, $\Omega_r$의 어떤 원소의 closure가 $W$ 안에 속하도록 하는 원소들이 존재한다. (안할 수도 있고, 하지만 $r$이 충분히 크다면 존재해야 한다.) 이들의 합집합을 $E_r$이라 하자. Urysohn's lemma를 이용해서, $\overline{E_r}\prec f_r\prec W$인 continuous function $f_r$을 찾을 수 있다. $g_r=\max(f_1,\ldots, f_r)$이라 하자. 그럼 $f_r$은 $E_r$ 위에서는 identically 1이므로, $\vol(E_r)\leq\Lambda f_r$이고, 따라서

$$\vol(E_r)\leq \Lambda f_r\leq\Lambda g_r\leq\volW$$

가 성립한다. 이제 $r\rightarrow\infty$일 때, $\vol(E_r)$은 $\volW$로 가므로 $\Lambda g_r$ 또한 $\vol(W)$로 가야 한다. 한편, $\Lambda g_r=\int g_r\mathop{dm}$의 값은, $g_r\nearrow 1_W$이므로 MCT에 의해

$$\Lambda g_r=\int g_r\mathop{dm}\rightarrow\int 1_W\mathop{dm}=m(W)$$

이기도 하므로, 이 경우 $m(W)=\vol(W)$가 성립한다. 한편 임의의 (open일 필요는 없는) $d$-cell은 이러한 open $d$-cell들의 교집합으로 나타낼 수 있으므로 1번 성질은 모든 $d$-cell들에 대해 성립한다.

한편, $\sigma$-algebra $\mathfrak{M}$ 위에 새로운 measure $\lambda$를 다음의 식

$$\lambda(E)=m(E+x)$$

으로 정의하자. 그럼 1번에 의하여 $\lambda(E)=m(E)$가 임의의 box $E$ 들에 대해 성립할 것이며, 따라서 임의의 Borel set들에 대해서도 성립할 것이고, regularity에 의해 임의의 measurable set들에 대해서도 성립해야 한다.    

4번 성질을 보이기 위해, **[Rud]**에는 다음의 claim

> $\mathbb{R}^d$ 위에 정의된 translation-invariant positive Borel measure $\mu$가 주어졌고, $\mu(K)<\infty$가 임의의 compact $K$에 대해 성립한다면, 적당한 $c$가 존재하여 $\mu(E)=cm(E)$가 임의의 Borel set에 대해 성립한다.

이 있다. 이 claim은 사실 claim이라기보다는 간단한 관찰의 결과인 게, 임의의 box는 그보다 작은 box들의 $2^{(n-r)d}$개의 합집합으로 나타날 수 있으며, 이들 모두는 ($\mu$가 translation-inavariant이므로) 크기가 같다. 따라서 만일 measure가 translation-invariant라면 이 box는 이보다 작은 box들의 크기를 결정하고, 그럼 임의의 measurable set의 크기도 결정된다. 즉, 예를 들어 어떤 $1$-box $Q_0$의 넓이를 $c$로 잡으면 다른 모든 measurable set의 크기 또한 $c$배가 된다. 

이 관찰과 함께라면 4번은 거의 자명한 결과로, 상수 $c$가 사실은 $\lvert \det(T)\rvert$가 된다는 것만 보이면 된다. 그런데 이 $Q_0$의 꼭짓점을 원점으로 고정하면, determinant의 기하학적인 정의에서 $c=\lvert \det(T)\rvert$여야 함이 자명하다.

</details>

이제 우리가 앞으로 가끔 사용하게 될 명제를 소개하고 마친다.

<div class="proposition" markdown="1">

<ins id="thm16">**정리 16 (Lusin)**</ins> 앞선 정리 15의 성질을 만족하는 measure space가 주어졌다 하자. $f$가 complex-valued measurable function이고, $f$의 support가 어떤 유한한 measure $\mu(A)<\infty$를 갖는 집합 $A$에 포함된다 하면 임의의 $\epsilon>0$에 대하여 적당한 $g\in C_c(X)$가 존재하여 

$$\mu(\{x:f(x)\neq g(x)\})<\epsilon$$

이도록 할 수 있다.

</div>
<details class="proof" markdown="1">
<summary>증명</summary>



</details>

---
**Reference**

**[Rud]** W. Rudin, *Real and complex analysis* Mathematics series. McGraw-Hill, 1987.  
**[SS]** E.M. Stein and R. Shakarchi. *Real Analysis: Measure theory, Integration, and Hilbert spaces*. Princeton University Press, 2009.  
**[Fol]** G.B. Folland, *Real Analysis: Modern Techniques and Their Applications*. Pure and Applied Mathematics: A Wiley Series of Texts, Monographs and Tracts. Wiley, 2013.

---

[^1]: Folland는 "This formula is messy in print but easily understood graphically" 라고 적고 있다.
[^2]: 이러한 함수 $d$를 종종 *pseudo-metric*이라 부른다. 그리고 우리가 이를 해결할 방법 또한 pseudo-metric을 metric으로 만드는 standard한 방법이다.
[^3]: 만약 $f\in C_c(X)$가 positive라면 (즉 $f(x)\geq 0$ for all $x\in X$라면) $\Lambda f\geq 0$.
[^4]: Linear transformation과 translation의 합성으로 얻어지는 변환을 *affine transformation*이라 한다.
