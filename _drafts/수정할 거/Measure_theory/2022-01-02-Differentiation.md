---

title: "Differentiation"
excerpt: "Lebesgue integration"

categories: [Math / Measure Theory]
permalink: /ko/math/measure_theory/differentiation
header:
    overlay_image: /assets/images/Measure_theory/Differentiation.png
    overlay_filter: 0.5
sidebar: 
    nav: "analysis"

date: 2022-01-02
last_modified_at:
weight: 5

published: false

---
<div class="notice--warning" markdown="1">

이 글은 현재 수정중입니다.

이 글은 예전에 쓴 글로, 서술 방향이 마음에 들지 않거나 표기법이 마음에 들지 않아 전체적으로 수정이 진행중입니다. 읽으실 때 참고해주세요.

</div>


**[Rud]**의 경우, 부등식들을 소개한 후 $L^p$ space로 이어지는 functional analysis 초입부의 내용을 진행한다. 이 부분의 내용이 뒷부분의 몇몇 정리의 증명에서 중요하게 쓰이기 때문에 그 배치 자체는 합리적이지만, 다른 분야로 넘어가는 다리를 맨 마지막에 두었으면 하는 개인적인 바람도 있어서, 약간의 엄밀성을 포기하더라도  **[Rud]** 6, 7단원의 내용을 먼저 소개하고 싶었다.

## Complex measure

우리는 그 동안 positive real-valued measure에 집중하며, complex measure는 의도적으로 무시해왔다. 그리고 이건 임의의 complex-valued measure를 항상 positive measure로 바꿀 수 있다는 이유였다. 그런데 여기에는 약간의 선의의 거짓말이 섞여있다. 

Positive real-valued measure를 다룰 때 좋은 것은, 예를 들어 $E=\bigcup E_i$이고 $E_i$들이 모두 disjoint라면, 

$$\mu(E)=\sum_{i=1}^\infty \mu(E_i)$$

라는 식을 아무런 제한없이 쓸 수 있다는 것이다. 여기서 *제한없이*라는 말은, 설령 우변의 무한합이 수렴하지 않더라도, positive measure의 경우 이 값은 계속 커지기만 하므로 (즉 $\infty$에 가까워지기만 하므로) 이 합이 $\infty$라는 값으로 수렴한다고 생각할 수 있다는 뜻이다. 하지만 당장 positive 조건을 떼어낸 real-valued의 경우만 보더라도 우변의 식이, 예를 들어 $\mu(E_i)=(-1)^i$라면, 이 식의 발산은 $\infty$로 수렴하는 것으로 볼 수 없다. Complex-valued measure의 경우 이러한 문제가 더 심각한 것은 물론이다.

따라서, complex-valued measure를 다룰 때에는 다음과 같이 아주 작은 제한조건을 하나 추가한다.

<div class="definition" markdown="1">

<ins id="df1">**정의 1**</ins> Measurable space $(X,\mathfrak{M})$ 위에 정의된 함수 $\mu:\mathfrak{M}\rightarrow\mathbb{C}$가 *complex measure*라는 것은, 임의의 $E\in\mathfrak{M}$과, 각각이 $\mathfrak{M}$의 원소인 $E$의 partition $\\{E_i\\}_1^\infty$에 대하여, 다음의 식

$$\mu(E)=\sum_{i=1}^\infty \mu(E_i)$$

이 성립하는 것이다.

</div>

이렇게 정의하면, $\mu(E)$는 $\mathbb{C}$의 원소이므로, 우변의 무한합은 반드시 수렴해야 한다. 뿐만 아니라, $E=\bigcup E_i$라 할 때, 이 합집합은 index set $i$의 배열에 영향받지 않으므로, 위 무한합도 마찬가지로 $i$의 배열에 영향받지 않아야 한다. 그럼 기초적인 해석학으로부터 이 무한합은 반드시 절대수렴해야 한다는 것을 알 수 있다. 즉, 다음의 식

$$\sum_{i=1}^\infty \lvert\mu(E_i)\rvert$$

는 항상 수렴한다. 따라서, 어떤 집합 $E$ 위에 아예 위의 식으로 함숫값을 정의해버린다면 그 값이 어떻게 될지에 관심을 가질 수 있다. 물론 이 식 자체는 별 의미를 갖지 않는다. $E=\bigcup E_i$를 어떻게 나누느냐에 따라 이 무한합의 값은 달라질 수 있기 때문이다. 그럼 당연히 이러한 partition들에 대한 supremum 혹은 infimum을 취해야 할텐데, 우리는 supremum을 취한다.[^1]

<div class="definition" markdown="1">

<ins id="df2">**정의 2**</ins> Complex measure $\mu$가 주어진 measure space $(X,\mathfrak{M},\mu)$에 대하여, 함수 $\lvert\mu\rvert:\mathfrak{M}\rightarrow [-\infty,\infty]$를 다음의 식

$$\lvert \mu\rvert(E)=\sup_{\{E_i\}\text{ partites }E}\sum_{i=1}^\infty\lvert\mu(E_i)\rvert$$

으로 정의하고, 이를 $\mu$의 *total variation*이라 부른다.

</div>

그럼 $\lvert\mu\rvert$는 사실 $\mathfrak{M}$ 위에서 정의된 measure가 된다.

<div class="proposition" markdown="1">

<ins id="pp3">**명제 3**</ins> Complex measure $\mu$가 주어진 measure space $(X,\mathfrak{M},\mu)$에 대하여, $\mu$의 total variation $\lvert\mu\rvert$는 $\mathfrak{M}$ 위의 positive measure를 정의한다.

</div>
<details class="proof" markdown="1">
<summary>증명</summary>

$\lvert\mu\rvert$의 $\sigma$-additivity를 보여야 한다. 즉, $E\in\mathfrak{M}$와, $E$의 partition $\\{E\_i\\}\_1^\infty$가 주어졌다 하고, 

$$\lvert\mu\rvert(E)=\sum_{i=1}^\infty \lvert\mu\rvert(E_i)$$

가 성립함을 보이면 된다.

우선 각각의 $E_i$에 대하여, $t_i<\lvert\mu\rvert(E\_i)$를 만족하는 실수 $t_i$를 택하면, total variation의 정의에 의해 $E_i$의 partition $\\{F\_{ij}\\}\_{j=1}^\infty$가 존재하여 

$$\sum_j\lvert\mu(F_{ij})\rvert>t_i$$

가 항상 성립하도록 할 수 있다. 이들 $\\{F\_{ij}\\}\_{i,j}$는 $E$의 partition이기도 하므로, 다시 total variation의 정의에 의하여

$$\sum_i t_i\leq\sum_{i,j}\lvert\mu(F_{ij})\rvert\leq\lvert\mu\rvert(E)$$

가 성립하고, 이제 $t_i$들의 선택에 supremum을 걸면, $t_i$들의 정의로부터

$$\sum_i\lvert\mu\rvert(E_i)\leq\lvert\mu\rvert(E)$$

가 성립한다. 이제 반대방향 부등식을 보여야 한다. $E$의 임의의 partition $\\{A\_j\\}\_1^\infty$가 주어졌다 하자. 그럼 $\\{E\_i\cap A\_j\\}\_{i=1}^\infty$는 $A\_j$의 partition을, $\\{E\_i\cap A\_j\\}\_{j=1}^\infty$는 $E\_i$의 parition을 이루므로 

$$\sum_j\lvert\mu(A_j)\rvert=\sum_j\left\lvert\sum_i\mu(A_j\cap E_i)\right\rvert\leq\sum_j\sum_i\lvert\mu(A_j\cap E_i)\rvert=\sum_i\sum_j\lvert\mu(A_j\cap E_i)\rvert\leq\sum_i\lvert\mu\rvert(E_i)$$

가 성립한다. 이 식은 임의의 partition $\\{A_j\\}$에 대해 성립하므로, 

$$\lvert\mu(E)\rvert\leq\sum_i\lvert\mu\rvert(E_i)$$

가 성립한다. 

</details>

또, 우리는 positive measure를 정의한 후에 모든 measurable set의 크기가 무한대인 것을 방지하기 위해 적어도 하나의 measurable set에 대해서는 유한한 값을 갖는 measure만을 생각하기로 하였는데, 이 조건은 $\lvert\mu\rvert(\emptyset)=0$이므로 자연스럽게 만족된다는 것도 확인할 수 있다.

뿐만 아니라, $\lvert\mu\rvert$는 finite measure이다. 즉 $\lvert\mu\rvert<\infty$가 성립한다. 이를 보이기 위해서는 다음의 보조정리가 필요하다.

<div class="proposition" markdown="1">

<ins id="lem4">**보조정리 4**</ins> $N$개의 복소수 $z_1,\ldots,z_N$이 주어졌다 하자. 그럼 $\\{1,\ldots,N\\}$의 적당한 부분집합 $S$가 존재하여

$$\left\lvert\sum_{k\in S}z_k\right\rvert\geq\frac{1}{\pi}\sum_{k=1}^N\lvert z_k\rvert$$

가 성립하도록 할 수 있다.
 
</div>
<details class="proof" markdown="1">
<summary>증명</summary>

우선, $z_k=\lvert z_k\rvert e^{i\alpha_k}$으로 잡자. 그리고 $-\pi\leq\theta\leq\pi$에 대하여, 집합 $S(\theta)$를 $\cos(\alpha_k-\theta)>0$이도록 하는 $k$의 집합이라 하자. 그럼

$$\left\lvert\sum_{k\in S(\theta)}z_k\right\rvert=\left\lvert\sum_{k\in S(\theta)}e^{-i\theta}z_k\right\rvert=\left\lvert\sum_{k\in S(\theta)}\lvert z_k\rvert e^{i(\alpha_k-\theta)}\right\rvert\geq\sum_{k=1}^N\lvert z_k\rvert\cos^+(\alpha_k-\theta)$$

가 성립한다. 이제 이 식의 우변을 최대로 하는 $\theta_0$값을 택하고 $S=S(\theta_0)$으로 잡자. 그럼 이 값은 $\theta$가 취할 수 있는 범위의 평균, 즉

$$\frac{1}{2\pi}\int_{-\pi}^\pi \sum_{k=1}^N\lvert z_k\rvert\cos^+(\alpha_k-\theta)\mathop{d\theta}=\sum_{k=1}^N\lvert z_k\rvert\int_{-\pi}^\pi \cos^+(\alpha_k-\theta)\mathop{d\theta}$$

보다는 커야 하는데, 우변의 적분은 어렵지 않게 2임을 확인할 수 있으므로 원하는 결과를 얻는다. 

</details>
<div class="proposition" markdown="1">

<ins id="pp5">**명제 5**</ins> $X$ 위에 정의된 complex measure $\mu$에 대하여, $\lvert\mu\rvert(X)<\infty$.

</div>
<details class="proof" markdown="1">
<summary>증명</summary>

<#content#>

</details>

한편, 이렇게 total variation measure를 정의하고 나면, 우리는 자연스럽게 다음의 두 measure

$$\mu^+=\frac{1}{2}(\lvert\mu\rvert+\mu),\quad\mu^-=\frac{1}{2}(\lvert\mu\rvert-\mu)$$

를 생각할 수 있는데, 그럼 이들은 각각 positive measure가 되며

$$\mu=\mu^+-\mu^-,\quad\lvert\mu\rvert=\mu^++\mu^-$$

가 성립한다. 

## Radon-Nikodym 정리

<div class="definition" markdown="1">

<ins id="df6">**정의 6**</ins> $\mathfrak{M}$ 위에 정의된 positive measure $\mu$와 임의의 measure $\lambda$를 생각하자. 그럼

1. $\lambda$가 $\mu$에 대해 *absolutely continuous*하다는 것은 임의의 $E\in\mathfrak{M}$에 대하여, 만일 $\mu(E)=0$이면 $\lambda(E)=0$ 또한 성립하는 것이다. 이를 $\lambda\ll\mu$와 같이 표기한다.
2. 만일 $\lambda(E)=\lambda(A\cap E)$가 임의의 $E\in\mathfrak{M}$에 대해 성립하도록 하는 $A\in\mathfrak{M}$이 존재한다면, $\lambda$가 $A$ 위에서 *concentrate*되었다고 부른다.[^2] 
3. 두 임의의 measure $\lambda_1,\lambda_2$에 대해, 적당한 집합 $A_1,A_2$가 존재하여 $\lambda_1$은 $A_1$ 위에, $\lambda_2$는 $A_2$ 위에 concentrate되어있고 $A_1\cap A_2=\emptyset$이라면 $\lambda_1$과 $\lambda_2$가 *mutually singular*하다고 하고 $\lambda_1\perp\lambda_2$와 같이 적는다. 

</div>

그럼 이들에 대해 몇가지 성질들이 성립한다.

<div class="proposition" markdown="1">

<ins id="pp7">**명제 7**</ins> Measurable space $(X,\mathfrak{M})$ 위에, positive measure $\mu$와, 임의의 measure들 $\lambda,\lambda_1,\lambda_2$가 주어졌다 하자. 그럼 다음이 성립한다.

1. 만약 $\lambda$가 $A$에서 concentrate되어있다면 $\lvert\lambda\rvert$도 그러하다.
2. 만일 $\lambda_1\perp\lambda_2$라면 $\lvert\lambda_1\rvert\perp\lvert\lambda_2\rvert$.
3. 만일 $\lambda_1\perp\mu$, $\lambda_2\perp\mu$라면 $\lambda_1+\lambda_2\perp\mu$.
4. 만일 $\lambda_1\ll\mu$, $\lambda_2\ll\mu$라면 $\lambda_1+\lambda_2\ll\mu$.
5. 만일 $\lambda\ll\mu$라면 $\lvert\lambda\rvert\ll\mu$.
6. $\lambda_1\ll\mu$이고 $\lambda_2\perp\mu$라면 $\lambda_1\perp\lambda_2$.
7. $\lambda\ll\mu$인 동시에 $\lambda\perp\mu$라면 $\lambda=0$.

</div>

다른 책들에서는 보통 다음 정리를 두 개로 나누어 서술하는데, 특이하게 **[Rud]**의 경우에는 이를 하나로 합쳐서 설명하고 있다.

<div class="proposition" markdown="1">

<ins id="thm8">**정리 8 (Lebesgue-Radon-Nikodym)**</ins> Measurable space $(X,\mathfrak{M})$ 위에 $\sigma$-finite positive measure $\mu$가 주어졌다 하자. 그럼 이 measurable space 위에 정의된 임의의 complex measure $\lambda$에 대하여,

1. 이 measurable space 위에 정의된 complex measure들의 pair $(\lambda_a,\lambda_s)$가 유일하게 존재하여, 

    $$\lambda=\lambda_a+\lambda_s,\quad\lambda_a\ll\mu,\quad\lambda_s\perp\mu$$
    
    그리고, 만일 $\lambda$가 positive, finite이라면 $\lambda_a$와 $\lambda_s$도 그러하다.
2. 위와 같이 정의된 $\lambda_a$에 대하여, 유일한 $h\in L^1(\mu)$가 존재하여

    $$\lambda_a(E)=\int_E h\mathop{d\mu}$$
    
    가 임의의 $E\in\mathfrak{M}$에 대해 성립한다.

</div>

위 정리에서의 $h$를 흔히 $h=d\lambda_a/d\mu$와 같이 쓰기도 한다. 

## Differentiation



---
**Reference**

**[Rud]** W. Rudin, *Real and complex analysis*, Mathematics series. McGraw-Hill, 1987.  

---

[^1]: 이 이야기, 즉 *total variation*에 대한 이야기는 원래 처음 도입되었을 때는 함수에 대해 정의되었으므로, 이를 measure에 대한 이야기가 아니라 실수를 domain으로 갖는 함수를 생각하면 직관적으로 좀 더 명확하다. 함수의 언어에서 total variation이란, $\sin x$와 같이 진동하는 함수를 순증가/순감소하는 부분들로 나누어 증가폭과 감소폭을 모두 더한 것이다. 
[^2]: 따라서, 임의의 measure는 (별 의미는 없지만) 항상 $X$ 위에서 concentrate되어 있다. 
