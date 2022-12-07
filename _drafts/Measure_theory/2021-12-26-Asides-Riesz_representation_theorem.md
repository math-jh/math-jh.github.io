---

title: "Riesz representation theorem<sup>†</sup>"
excerpt: "Lebesgue integration"

categories: [Math / Measure Theory]
permalink: /ko/math/measure_theory/riesz_representation_theorem
header:
    overlay_image: /assets/images/Measure_theory/Riesz_representation_theorem.png
    overlay_filter: 0.5
sidebar: 
    nav: "analysis"

date: 2021-12-26
last_modified_at:
weight: 3

published: false

---
<div class="notice--warning" markdown="1">

이 글은 현재 수정중입니다.

이 글은 예전에 쓴 글로, 서술 방향이 마음에 들지 않거나 표기법이 마음에 들지 않아 전체적으로 수정이 진행중입니다. 읽으실 때 참고해주세요.

</div>


앞선 글에서 생략한 Riesz 표현정리의 증명과, Lebesgue measure의 건설에 대한 내용이다. 이 글은 기본적으로 **[Rud]**의 chapter 2지만, 앞부분은 이미 위상수학 때 다룬 적이 있으므로 생략하기로 한다.  

## Notational conventions

우리의 목표는 앞서 소개한 다음 정리에 대한 증명이다.

<div class="proposition" markdown="1">

<ins id="thm1">**정리 1 (Riesz)**</ins> Locally compact, Hausdorff space $X$가 주어졌다 하자. 만일 $\Lambda$가 compactly supported continuous function들의 (complex) vector space $C_c(X)$ 위에서 정의된 positive linear functional이라면, $X$의 Borel $\sigma$-algebra를 포함하는 적당한 $\sigma$-algebra $\mathfrak{M}$과, $\mathfrak{M}$ 위에 정의된 유일한 positive measure $\mu$가 존재하여 다음의 식

$$\Lambda f=\int_X f\mathop{d\mu}\qquad\text{ for all $f\in C_c(X)$}$$

을 만족한다. 또, 이들은 다음 성질들을 만족한다.
  
1. 임의의 compact set $K$에 대하여, $\mu(K)<\infty$.
2. (Outer regularity) 임의의 $E\in\mathfrak{M}$에 대하여, $\mu(E)=\inf\\{\mu(V): E\subset V, \text{$V$ is open in $X$}\\}$.
3. (Inner regularity) 임의의 open set $E$, 혹은 $\mu(E)<\infty$를 만족하는 임의의 $E\in\mathfrak{M}$에 대하여, $\mu(E)=\sup\\{\mu(K): K\subset E, \text{$K$ is compact in $X$}\\}$.
4. (Completeness) 만일 $\mu(E)=0$이라면 임의의 $A\subset E$에 대해 $A\in\mathfrak{M}$.

</div>

우선, 증명이 좀 길기 때문에 (자잘한 걸 제외하고 10단계다) 몇 가지 notational convention을 좀 만들자. 언제나 그랬듯이, $V$는 항상 open set을 의미하고 $K$는 항상 compact set을 의미한다. 우리는 새로운 notation $\prec$을 도입할 것인데, 임의의 $f\in C_c(X)$에 대하여

1. $K\prec f$라는 것은, $0\leq f(x)\leq 1$이 모든 $x\in X$에 대해 성립하며, $f$의 값은 $K$ 위에서 identically 1이라는 것이다.
2. $f\prec V$라는 것은, $0\leq f(x)\leq 1$이 모든 $x\in X$에 대해 성립하며, $f$의 값은 $V$ 바깥에서는 identically 0이라는 것이다. (즉, $\operatorname{supp}f\subset V$라는 것이다.)

그럼 $K\prec f\prec V$라는 것은, $K\subset V$이며, $f$가 $K$ 위에서는 identically 1이고, $V$ 바깥에서는 identically zero, 그리고 $K$와 $V$ 사이에서는 0과 1 사이의 함숫값을 갖는다는 이야기이다. 즉, $f$는 일종의 bump function과 같은 역할을 한다. 이런 상황에서 우리가 잘 알고 있는 Urysohn's lemma는 다음과 같이 state될 수 있다.

<div class="proposition" markdown="1">

<ins id="lem-ury">**보조정리 (Urysohn)**</ins> Locally compact, Hausdorff space $X$에 대해, $K$는 compact, $V$는 $K$를 포함하는 open set이라 하자. 그럼 적당한 $f\in C_c(X)$가 존재하여 $K\prec f\prec V$이도록 할 수 있다.  

</div>

## Proof of the Riesz representation theorem

<details class="proof" id="pf0" markdown="1">
<summary>단계 0</summary>

우선, 우리가 주어진 조건을 만족하는 measure space $(X,\mathfrak{M},\mu)$를 만들었고, 이들이 1번부터 4번까지의 성질들도 모두 만족한다 가정한 다음 유일성을 먼저 보이자.  
Outer regularity에 의해, 임의의 measurable set의 measure는 open set의 measure들이 모두 결정된다면 자동으로 정해진다. 또, 다시 inner regularity에 의해 이 open set들의 measure는 compact set의 measure들이 모두 결정된다면 자동으로 정해진다. 따라서 유일성을 보이기 위해서는 위의 조건을 만족하는 두 measure $\mu_1$, $\mu_2$가 주어졌을 때 이들이 임의의 compact set $K$에 대해 같은 measure를 준다는 것을 보이면 된다.

임의의 compact set $K$를 택하자. 그럼 1번 성질에 의해 $K$는 measurable이고, 그 measure는 유한하다. 임의로 주어진 $\epsilon>0$에 대하여, measurable set $K$에 outer regularity를 적용하면 적당한 open set $V$가 존재하여 $K\subset V$이고 $\mu_2(V)<\mu_2(K)+\epsilon$이 성립한다. 이제 Urysohn's lemma에 의하여, 적당한 $f\in C_c(X)$가 존재하여 $K\prec f\prec V$이고 따라서

$$\mu_1(K)=\int_X 1_K\mathop{d\mu_1}\leq\int_X f\mathop{d\mu_1}=\Lambda f\tag{1}$$

가 성립한다. 한편, $\Lambda f$는 $\int_X f\mathop{d\mu_2}$이기도 하므로

$$\Lambda f=\int_X f\mathop{d\mu_2}\leq\int_X 1_V\mathop{d\mu_2}=\mu_2(V)<\mu_2(K)+\epsilon$$

이다. 즉, $\mu_1(K)<\mu_2(K)+\epsilon$가 임의의 $\epsilon$에 대해 성립하므로 $\mu_1(K)\leq\mu_2(K)$이다. $\mu_1$과 $\mu_2$의 역할을 바꾸면 $\mu_2(K)\leq\mu_1(K)$도 성립하므로, $\mu_1(K)=\mu_2(K)$ 또한 성립한다.

마지막으로 이 증명에서 주목할 것은, 우리는 $\mu_1(K)\leq\Lambda f$라는 것을 보였고 (1), $\Lambda$는 $\mathbb{C}$의 값만을 취하므로 $\Lambda f$는 반드시 유한하다는 것이다[^1]. 즉, 주어진 조건을 만족하는 measure $(X,\mathfrak{M},\mu)$는 *반드시* 첫 번째 성질 또한 만족해야 한다.

</details>

 
이제 정말 본격적으로 construction을 시작해야 한다. 그 전에 대략적인 흐름을 이해할 필요가 있다. 우리의 아이디어는 $(X,\mathfrak{M},\mu)$는 $\Lambda$를 represent하는 measure space이므로, 즉 다음의 식

$$\Lambda f=\int_X f\mathop{d\mu}$$

가 성립해야 하므로, 임의의 measurable set (아직 measurable set을 정의하지도 않았지만) $E$에 대해 $f=1_E$를 집어넣어보면

$$\Lambda(1_E)=\int_X 1_E\mathop{d\mu}=\mu(E)$$

가 나오므로 $\Lambda$의 값이 정확히 measure $\mu$를 정의해준다는 것이다. 이 아이디어에서 가장 큰 문제가 되는 것은, $\Lambda$는 $C_c(X)$ 위에서만 정의되었기 때문에 $\Lambda(1_E)$는 정의조차 되지 않았다는 것이다. 따라서 우리는 $1_E$를 $C_c(X)$의 원소들을 이용해 approximate할 필요가 있다.

$\mathfrak{M}$은 $X$의 Borel $\sigma$-algebra를 포함해야 하므로, 우선 $E$가 open set인 경우부터 해결하는 것이 여러모로 합리적이다. 임의의 open set $V$에 대하여, $\mu(V)$를 다음의 식

$$\mu(V)=\sup\{\Lambda f:f\prec V\}$$

으로 정의하자. 즉, 다음과 같은 그림으로 생각할 수 있다.

![open_set](/assets/images/Measure_theory/Lebesgue_measure-1.png){:width="360px"  class="invert" .align-center}

$f\prec V$인 함수들은 정의에 의해 $V$ 안에서 $0\leq f(x)\leq 1$이므로, $\mu(V)$를 위의 식과 같이 $\Lambda f$들의 supremum으로 정의한다는 것은 함수 $f$들이 결국은 $1_V$를 근사한다는 뜻이다. 물론 이 직관을 정당화하기 위해서는 $f$가 $1_V$에 가까우면 가까울수록 (즉 빨간 화살표를 따라갈수록) $\Lambda f$의 값이 커져야 하는데, 이는 $\Lambda$가 positive linear functional이라는 사실로부터 쉽게 알아낼 수 있다.

한편, 만일 $V_1\subset V_2$이고 $f\prec V_1$이라면 $f\prec V_2$인 것은 자명하다. 따라서, 만일 $V_1\subset V_2$라면 $\mu(V_1)\leq \mu(V_2)$여야 하고, 우리가 임의의 집합 $E\subset X$에 대해

$$\tilde{\mu}(E)=\inf\{\mu(V): E\subset V, \text{$V$ is open in $X$}\}$$

으로 정의한다면, $\tilde{\mu}$는 우리가 앞서 정의한 measure를 확장하는 함수가 될 것이다. 즉, 만일 $E$ 자기 자신이 open이라면, (i) $E$를 포함하는 임의의 open set $V$는 $\mu(E)\leq\mu(V)$를 만족하고, (ii) $E$ 자기 자신이 $E$를 포함하는 open set이므로 $\tilde{\mu}(E)=\mu(E)$여야 한다. 따라서, 약간의 abuse of notation을 통해 $\tilde{\mu}$를 그냥 $\mu$로 적자. 그럼 이제 $\mu$는 $X$의 임의의 부분집합에 대해 정의되었으며, 또 만일 $E_1\subset E_2$라면 $E_2$를 포함할 수 있는 open set은 $E_1$을 포함할 수 있는 open set들보다 적어지므로 $\mu$는 임의의 부분집합들에 대해서도 monotone이다.  

물론 우리는 앞선 글들에서 $\mathcal{P}(X)$에 measure structure를 주는 것이 힘든 일인 것을 알고 있고, 실제로 이건 우리의 관심사도 아니다. 우리는 단지 $\mathcal{P}(X)$에 포함되어 있는 $\sigma$-algebra를 적당히 찾아서 주어진 성질들이 만족되도록 하면 된다. 우선 $\mathfrak{M}_F$를 다음의 두 조건

1. $\mu(E)<\infty$,
2. $\mu(E)=\sup\\{\mu(K):K\subset E,\;K\text{ compact}\\}.$

을 만족하는 $E$들을 모은 집합이라 하고, 그 후 모든 compact set $K$에 대해 $E'\cap K\in\mathfrak{M}_F$이도록 하는 $E'$들을 모두 모아 이를 $\mathfrak{M}$으로 삼을 것이다. 

일단은 여기까지가 construction이고, 이렇게 만든 $\mu$, $\mathfrak{M}$이 주어진 성질들을 만족한다는 것을 보여야 한다. 우선 outer regularity는 $\mu$의 정의로부터 자명하게 성립한다. Completeness 또한 어렵지 않게 보일 수 있는데, 만일 $\mu(E)=0$이라면 $\mu$의 monotonicity에 의해 $\mu(A)=0$이 임의의 $A\subset E$에 대해 성립하며, 또 임의의 compact set $K$에 대하여

$$\mu(A\cap K)\leq \mu(A)=0$$

이므로 자명하게 $\mu(A)=\sup\\{\mu(K):K\subset A,\;K\text{ compact}\\}$가 성립하기 때문이다. 이제 날로 먹기 힘든 부분만 남아있다.

<details class="proof" id="pf1" markdown="1">
<summary>단계 1</summary>

첫 번째 단계는 다음의 $\sigma$-subadditivity를 보이는 것이다.

> 만일 $E_1,E_2,\ldots$가 $X$의 임의의 subset들이라면, 
> 
> $$\mu\left(\bigcup_{i=1}^\infty E_i\right)\leq\sum_{i=1}^\infty \mu(E_i).$$
>
> ($E_i$들이 mutually disjoint일 필요는 없다.)

이를 보이기 위해 우리는 우선 임의의 두 open set $V_1$, $V_2$에 대해

$$\mu(V_1\cup V_2)\leq\mu(V_1)+\mu(V_2)$$

인 것을 보인다. $g\prec V_1\cup V_2$인 $g\in C_c(X)$를 잡자. $K=\operatorname{supp}g$라 하면 우리는 다음의 두 조건

1. $h_1\prec V_1$, $h_2\prec V_2$,
2. $h_1(x)+h_2(x)=1$ for all $x\in K$.

을 만족하는 $h_1,h_2$, 즉 $V_1$, $V_2$에 대한 partition of unity를 잡을 수 있다. 그럼 $h_ig\prec V_i$이고 $g=h_1g+h_2g$가 성립한다. 따라서

$$\Lambda g=\Lambda(h_1g+h_2g)=\Lambda(h_1g)+\Lambda(h_2g)\leq\mu(V_1)+\mu(V_2)$$

이고, $g$는 $g\prec V_1\cup V_2$를 만족하는 $C_c(X)$의 임의의 원소를 택한 것이므로 supremum을 취하면 원하던 대로

$$\mu(V_1\cup V_2)\leq\mu(V_1)+\mu(V_2)$$

을 얻는다. Induction에 의해, 이 결과는 쉽게 유한히 많은 open set들로 일반화할 수 있다.

이제 이를 open set이 아닌 집합들의 countable한 union으로 일반화해야 한다. 만일 어떤 $i$에 대해, $\mu(E_i)=\infty$라면 $\mu$의 monotonicity에 의해 $\mu(\bigcup E_i)$ 또한 $\infty$가 될 것이므로, 우리는 일반성을 잃지 않고 $\mu(E_i)<\infty$라 가정해도 된다. 

임의의 $\epsilon>0$이 주어졌다 하자. 그럼 $\mu$의 정의에 의하여, $E_i$를 포함하는 open set $V_i$들이 존재하여 $\mu(V_i)<\mu(E_i)+2^{-i}\epsilon$이도록 할 수 있다. 이제 $V=\bigcup_1^\infty V_i$라 하고, $f\prec V$를 만족하는 임의의 $f\in C_c(X)$를 고르자. 그럼 $\operatorname{supp}f$는 compact이고 $V_i$들이 이를 덮으므로, 적당한 $N$이 존재하여 $V_1\cup\cdots\cup V_N$이 $\operatorname{supp}f$를 덮도록 할 수 있다. 그럼

$$\Lambda f\leq \mu(V_1\cup \cdots \cup V_N)\leq\mu(V_1)+\cdots+\mu(V_N)\leq\sum_{i=1}^\infty \mu(V_i)=\sum_{i=1}^\infty\mu(E_i)+\epsilon$$

이며, 또 $\bigcup_1^\infty E_i\subset \bigcup_1^\infty V_i=V$이므로 monotonicity에 의하여

$$\mu\left(\bigcup_{i=1}^\infty E_i\right)\leq\mu(V)\leq\sum_{i=1}^\infty\mu(E_i)+\epsilon$$ 

이 성립한다. $\epsilon$은 임의의 양수이므로 원하던 부등식을 얻는다.

</details>

두 번째 단계로, 우리는 임의의 compact set $K$가 $\mathfrak{M}_F$에 속하며, $\mu(K)=\inf\\{\Lambda f:K\prec f\\}$이 성립한다는 것을 증명할 것이다. 이 단계는 $K\in\mathfrak{M}_F$임을 보이므로, $\mathfrak{M}_F$의 정의에 의하여 $\mu(K)<\infty$임이 증명된다. 또, 나중의 식은 $\mu$의 값들을 살펴보는 데에 큰 도움이 될 것이다. 이 식 자체는 어떻게 보면 우리가 open set에 대해 정의한 $\mu$의 값과 대칭적이라 할 수 있다. 

![compact_set](/assets/images/Measure_theory/Lebesgue_measure-2.png){:width="360px"  class="invert" .align-center}

<details class="proof" id="pf2" markdown="1">
<summary>단계 2</summary>
$K\prec f$이고, 임의의 상수 $0<\alpha<1$이 주어졌다 하자. Open set $V_\alpha$를 다음의 식

$$V_\alpha=\{x:f(x)>\alpha\}$$

으로 정의하면, $f$는 $K$ 위에서 identically 1이므로 $K\subset V_\alpha$이다. 또, 만일 $g\prec V_\alpha$라면 함수 $\alpha g$는 $V_\alpha$ 위에서 커봐야 1이며 이 바깥에서는 0이므로, $\alpha g\leq f$이다. 따라서 $\Lambda g\leq\alpha^{-1}\Lambda f$이므로

$$\mu(K)\leq \mu(V_\alpha)=\sup\{\Lambda g:g\prec V_\alpha\}\leq \alpha^{-1}\Lambda f$$

가 성립한다. 이 식은 임의의 $0<\alpha<1$에 대해 성립하므로, $\alpha=1$에 대해서도 부등식

$$\mu(K)\leq\Lambda f$$

이 성립하고 따라서 $\mu(K)<\infty$이다. $K$ 자기 자신은 compact이므로 $\mathfrak{M}_F$의 두 번째 조건 또한 자명하다. 

이제 남은 건 $\mu(K)$에 대한 식인데, 언제나처럼 적당한 $\epsilon>0$이 주어졌다 하고, $\mu$의 정의를 이용하여 $\mu(V)<\mu(K)+\epsilon$을 만족하는 open set $V\supset K$를 찾자. 그럼 Urysohn's lemma에 의해 $K\prec f\prec V$를 만족하는 $f\in C_c(X)$가 존재하며 따라서

$$\mu(K)\leq \Lambda f\leq\mu(V)<\mu(K)+\epsilon$$

이고, $\epsilon$은 임의의 양수이므로 원하는 대로 $\mu(K)$에 대한 식을 얻는다. 

</details>

다음 단계로, 우리는 임의의 open set이 $\mathfrak{M}_F$의 두 번째 조건을 만족한다는 것을 증명할 것이다. 따라서, open set의 measure가 finite이기만 하다면 (두 번째 조건은 자동으로 만족될 것이므로) 이 집합은 $\mathfrak{M}_F$의 원소가 될 것이다.

<details class="proof" id="pf3" markdown="1">
<summary>단계 3</summary>
$\alpha<\mu(V)$를 만족하는 임의의 $\alpha$를 택하자. 그럼 $\mu$의 정의에 의해, $\alpha<\Lambda f$를 만족하는 $f\prec V$가 존재한다. 이제 $K=\operatorname{supp}f$라 하고, $W$가 $K$를 포함하는 open set이라 하자. 그럼 $\Lambda f\leq\mu(W)$이고, $\mu(K)$는 이러한 $\mu(W)$들의 infimum이므로 $\Lambda f\leq\mu(K)$이다. 따라서, $\alpha<\mu(K)$를 만족하는 compact set $K\subset V$가 항상 존재하며, $\alpha$ $\mu(V)$보다 작은 임의의 상수이므로 

$$\mu(V)=\sup\{\mu(K):K\subset V,\;K\text{ compact}\}$$

가 성립한다.

</details>

이제 우리는 $\mathfrak{M}_F$의 각 원소에 대해 $\sigma$-additivity가 성립한다는 것을 보인다.

<details class="proof" id="pf4" markdown="1">
<summary>단계 4</summary>

$\mu$는 $\mathfrak{M}_F$에 대해 $\sigma$-additivity를 만족한다. 즉,

> $\mathfrak{M}_F$의 임의의 원소들의 family $\\{E_i\\}_1^\infty$에 대하여, $E=\bigcup_1^\infty E_i$라면
> 
> $$\mu(E)=\sum_{i=1}^\infty\mu(E_i).$$

우선, disjoint compact set $K_1,K_2$에 대한 명제를 먼저 보이자. [*단계 1*](#pf1)에 의해 이건 한 쪽 방향 부등식 $\mu(K_1)+\mu(K_2)\leq\mu(K_1\cup K_2)$만 보이면 충분하다.
임의의 $\epsilon>0$이 주어졌다 하자. 그럼 Urysohn's lemma에 의하여, $K_1$에서는 1, $K_2$에서는 $0$이고 $0\leq f(x)\leq 1$이 항상 성립하는 $f\in C_c(X)$가 존재한다. 한편, 우리가 [*단계 1*](#pf2)에서 증명한 $\mu(K)$의 표현에 따르면, 적당한 $g\in C_c(X)$가 존재하여

$$K_1\cup K_2\prec g,\qquad \Lambda g<\mu(K_1\cup K_2)+\epsilon$$

이도록 할 수 있다. 그럼 정의에 의해 $K_1\prec fg$이고, $K_2\prec (1-f)g$인 것은 자명하다. 이제

$$\mu(K_1)+\mu(K_2)\leq\Lambda(fg)+\Lambda((1-f)g)=\Lambda g<\mu(K_1\cup K_2)+\epsilon$$

이고, $\epsilon$은 임의의 양수이므로 이 경우, 더 일반적으로 유한 개의 disjoint compact set에 대한 명제는 증명이 끝난다.

이제 남은 부분은 이를 임의의 $\mathfrak{M}\_F$의 원소들의 countable한 union으로 확장하는 일이다. 우선, 만일 $\mu(E)=\infty$라면 [*단계 1*](#pf1)에 의하여 원하는 식이 성립할 것이므로 $\mu(E)<\infty$라 가정할 수 있다. 임의의 $\epsilon>0$이 주어졌다 하자. 그럼 $E_i$들 각각은 $\mathfrak{M}_F$의 원소이므로, $\mathfrak{M}_F$의 두 번째 조건에 의해, 다음의 식

$$\mu(H_i)>\mu(E_i)-2^{-i}\epsilon$$

을 만족하는 compact set들 $H_i$가 존재한다. $K_n=\bigcup_1^n H_i$라 하면, 우리는

$$\mu(E)\geq\mu(K_n)=\sum_{i=1}^n\mu(H_i)>\sum_{i=1}^n\mu(E_i)-\epsilon$$

을 얻고, 이 식이 임의의 $n$과 임의의 $\epsilon$에 대해 성립하므로 $\mu(E)\geq\sum_1^n\mu(E_i)$가 성립한다. 반대 방향 부등식은 다시 [*단계 1*](#pf1)에 의해 자명하다.

여기에 더해, $\mu(E)<\infty$라 가정하자. 그럼 임의의 $\epsilon>0$에 대하여, 적당한 $N$이 존재하여

$$\mu(E)\leq\sum_{i=1}^N\mu(E_i)+\epsilon<\sum_{i=1}^N\mu(H_i)+2\epsilon=\mu(K_N)+2\epsilon$$

이도록 할 수 있다. 즉, $E$는 (만약 $\mu(E)<\infty$라면) $\mathfrak{M}_F$의 두 번째 조건도 만족하므로 $E\in\mathfrak{M}_F$가 성립한다.
  
</details>

이제 $\mathfrak{M}_F$에서의 regularity condition들을 보이자. 

<details class="proof" id="pf5" markdown="1">
<summary>단계 5</summary>

임의의 $E\in\mathfrak{M}_F$가 주어졌다 하자. 그럼 임의의 양수 $\epsilon$에 대하여, $\mu(V\setminus K)<\epsilon$이도록 하는 open set $V\supset E$와 compact set $K\subset E$가 존재한다.

$\mu$의 정의에 의하여, open set $V\supset E$가 존재하여 $\mu(V)<\mu(E)+\epsilon/2$이도록 할 수 있다. 또, $E\in\mathfrak{M}_F$이므로 compact set $K\subset E$가 존재하여 $\mu(E)<\mu(K)+\epsilon/2$이도록 할 수 있다. 이제 $V\setminus K$는 open이므로 [*단계 3*](#pf3)에 의하여 이는 $\mathfrak{M}_F$의 원소이고, 따라서 [*단계 4*](#pf4)의 유한한 버전을 $K$와 $V\setminus K$에 적용하면

$$\mu(K)+\mu(V\setminus K)=\mu(V)<\mu(K)+\epsilon$$

을 얻는다.

</details>

다음 단계는 $\mathfrak{M}_F$는 algebra 구조를 가진다는 것이다.

<details class="proof" id="pf6" markdown="1">
<summary>단계 6</summary>
임의의 $A,B\in\mathfrak{M}_F$를 고르자. 우선, 임의의 $\epsilon>0$에 대하여 다음의 두 식

$$\mu(V_1\setminus K_1)<\epsilon,\qquad\mu(V_2\setminus K_2)<\epsilon$$

을 만족하는 $K_1\subset A\subset V_1$과 $K_2\subset B\subset V_2$가 존재한다. 이제

$$A\setminus B\subset V_1\setminus K_2\subset(V_1\setminus K_1)\cup(K_1\setminus V_2)\cup(V_2\setminus K_2)$$

에 의하여, [*단계 1*](#pf1)의 $\sigma$-subadditivity를 적용하면

$$\mu(A\setminus B)\leq\mu(K_1\setminus V_2)+2\epsilon$$

을 얻는다. 이제, $K_1\setminus V_2$는 compact set이고, $\epsilon$은 임의의 양수이므로 위의 식은 $A\setminus B$가 $\mathfrak{M}_F$의 두 번째 조건을 만족한다는 것을 보여주고, 역시 $\mu(K_1\setminus V_2)<\infty$이므로 $A\setminus B\in\mathfrak{M}_F$이다. 한편, $A\cup B=(A\setminus B)\cup B$이므로, [*단계 4*](#pf4)에 의하여 $A\cup B\in\mathfrak{M}_F$이고, 또 $A\cap B=A\setminus(A\setminus B)$이므로 $A\cap B$ 또한 $\mathfrak{M}_F$의 원소가 된다.

</details>

이제 이렇게 정의한 $\mathfrak{M}_F$를 앞서 construct한 것과 같이 $\mathfrak{M}$으로 확장하자. 그럼 $\mathfrak{M}$은 Borel set들을 포함하는 $\sigma$-algebra가 된다.

<details class="proof" id="pf7" markdown="1">
<summary>단계 7</summary>
임의의 compact set $K\subset X$를 고정하자. 만약 $A\in\mathfrak{M}$이라면, 다음의 식

$$A^c\cap K=K\setminus(A\cap K)$$

에서, $K,A\cap K\in\mathfrak{M}\_F$이므로 앞선 [*단계 6*](#pf6)에 의하여 $A^c\in\mathfrak{M}\_F$이다. $K$는 임의의 compact set이므로, 이는 $A^c\in\mathfrak{M}$이라는 뜻이다. 

이제 $A=\bigcup_1^\infty A_i$이고 각각의 $A_i$들이 모두 $\mathfrak{M}$에 속한다고 하자. $B_1=A_1\cap K$라 하고, 귀납적으로 다음의 집합

$$B_n=(A_n\cap K)\setminus\bigcup_1^{n-1}B_i$$

이라 하면 $A\cap K=\bigcup_1^\infty B_n$이고, $\\{B_n\\}_1^\infty$는 $\mathfrak{M}_F$의 원소들이다. 한편, $\mu(A\cap K)\leq\mu(K)<\infty$이므로, [*단계 4*](#pf4)의 마지막 comment에 의하여 $A\cap K\in\mathfrak{M}_F$이다. 즉, $K$는 임의의 compact set이므로 $A\in\mathfrak{M}$이다. 

앞선 주장 둘은 $\mathfrak{M}$이 $\sigma$-algebra임을 보여준다. 마지막으로, 임의의 closed set $C$에 대하여 $C\cap K$는 compact이므로 $\mathfrak{M}_F$의 원소이고, 따라서 $C$는 $\mathfrak{M}$의 원소이다. 따라서 $\mathfrak{M}$은 Borel $\sigma$-algebra를 포함하는 $\sigma$-algebra이다.

</details>

우리는 $\mathfrak{M}_F$로부터 $\mathfrak{M}$을 만들어냈는데, 거꾸로 $\mathfrak{M}_F$은 $\mathfrak{M}$의 원소들 중 $\mu(E)<\infty$를 만족하는 $E$들만 모아둔 집합이다. 바꿔 말하자면, $E\in\mathfrak{M}$이 $\mu(E)<\infty$를 만족한다면 $E\in\mathfrak{M}_F$이고, 따라서 inner regularity가 성립한다. 따라서 이 단계는 세 번째 성질을 만족한다. 

<details class="proof" id="pf8" markdown="1">
<summary>단계 8</summary>
우선, 만일 $E\in\mathfrak{M}_F$라면, 임의의 compact set $K$는 $\mathfrak{M}_F$의 원소이기도 하고, $\mathfrak{M}_F$는 algebra이므로 $E\cap K\in\mathfrak{M}_F$이다. 따라서 $E\in\mathfrak{M}$이다. 

거꾸로 $\mu(E)<\infty$를 만족하는 $E\in\mathfrak{M}$을 골라오자. 우리는 $E\in\mathfrak{M}_F$임을 보여야 한다. 우선, $\mu(E)<\infty$이므로, $\mu$의 정의에 의해 $V\supset E$인 open set들 가운데 $\mu(V)<\infty$를 만족하는 것이 존재한다. 그럼 [*단계 3*](#pf3)에 의하여, $V$는 $\mathfrak{M}_F$의 원소이고, 따라서 [*단계 5*](#pf5)에 의하여 $\mu(V\setminus K)<\epsilon$이도록 하는 compact set $K$가 존재할 것이다. 가정에 의해 $E\in\mathfrak{M}$이므로, $E\cap K\in\mathfrak{M}_F$이고, 따라서 $\mathfrak{M}_F$의 두 번째 조건에 의하여 적당한 compact set $H$가 존재하여 $H\subset E\cap K$이고

$$\mu(E\cap K)<\mu(H)+\epsilon$$

이도록 할 수 있다. 이제, $E\subset (E\cap K)\cup(V\setminus K)$로부터

$$\mu(E)\leq\mu(E\cap K)+\mu(V\setminus K)<\mu(H)+2\epsilon$$

을 얻고, $\epsilon$은 임의의 양수이므로 $E\in\mathfrak{M}_F$이다. 

</details>

지금까지 우리는 $\mathfrak{M}$이 Borel $\sigma$-algebra를 포함한다는 것을 보였고, 또 $\mu$와 $\mathfrak{M}$이 만족해야 하는 성질들 1번부터 4번까지를 모두 보였다. 이제 남은 것은 $\mu$가 positive measure가 되며, 또 $\mu$가 $\Lambda$를 represent한다는 것이다.

<details class="proof" id="pf9" markdown="1">
<summary>단계 9</summary>

$\mu$는 $\mathfrak{M}$에서의 measure가 된다. $\mu$가 항상 0보다 크거나 같은 것은 자명하므로 $\sigma$-additivity만 보이면 되는데, $\mu(E)$가 무한대인 경우는 $\sigma$-subadditivity로부터 자명하며, 그렇지 않은 경우 [*단계 8*](#pf8)에 의하여 $E$는 $\mathfrak{M}\_F$의 원소이며, 여기에서는 [*단계 4*](#pf4)에 의하여 $\sigma$-additivity가 성립함이 알려져 있다. 어떤 경우에도 $\mu$는 $\sigma$-additivity를 만족한다.

</details>

드디어 마지막 단계로써, $\Lambda f=\int_Xf\mathop{d\mu}$임을 보인다. 우선 이는 $f$가 real인 경우만 보이면 충분하다. 또, $f$가 real인 경우에 대해서는 사실 다음의 *부등식*

$$\Lambda f\leq\int_X f\mathop{d\mu}$$

만 보이면 충분하다. 이것이 성립한다면

$$-\Lambda f=\Lambda (-f)\leq\int_X(-f)\mathop{d\mu}=-\int_Xf\mathop{d\mu}$$

로부터 반대쪽 부등식도 얻어지기 때문이다. 

<details class="proof" id="pf10" markdown="1">
<summary>단계 10</summary>
임의의 $f\in C_c(X)$를 택하고, $K=\operatorname{supp}f$라 하자. Extreme value theorem에 의하여, 적당한 interval $[a,b]$가 존재하여 $f(X)\subset [a,b]$가 성립한다. 이제 $\epsilon>0$을 임의로 택하고, $[a,b]$를 길이가 $\epsilon$보다 작은 partition들

$$a=y_0<y_1<\cdots<y_n=b$$

으로 나누고, 집합 $E_i$를 다음의 식

$$E_i=\{x:y_{i-1}<f(x)\leq y_i\}\cap K$$

으로 정의할 수 있다. $f$는 연속이므로, Borel mapping이기도 하고, 따라서 위의 집합들은 Borel set들이 된다. 또, 이들을 모두 합집합하면 $K$가 되며, 이들은 mutually disjoint이다. 이제, 각각의 $i$에 대하여 

$$\mu(V_i)<\mu(E_i)+\epsilon/n$$

을 만족하는 open set들 $\mu(V_i)$를 잡자. $V_i$를 충분히 작게 잡는다면 임의의 $x\in V_i$에 대해 $f(x)<y_i+\epsilon$이도록 할 수 있다. 이제 각각의 $V_i$들에 partition of unity $h_i$들을 대응시켜, $K$ 위에서는 $\sum h_i=1$이도록 하자. 그럼

$$\mu(K)\leq\Lambda\left(\sum h_i\right)=\sum\Lambda h_i$$

이고, 따라서

$$\begin{aligned}
        \Lambda f&=\sum_{i=1}^n\Lambda(h_i f)\leq\sum_{i=1}^\infty (y_i+\epsilon)\Lambda h_i\\
        &=\sum_{i=1}^n(\lvert a\rvert+y_i+\epsilon)\Lambda h_i-\lvert a\rvert\sum_{i=1}^n \Lambda h_i\\
        &\leq \sum_{i=1}^n(\lvert a\rvert+y_i+\epsilon)[\mu(E_i)+\epsilon/n]-\lvert a\rvert\mu(K)\\
        &=\sum_{i=1}^n (y_i-\epsilon)\mu(E_i)+2\epsilon\mu(K)+\frac{\epsilon}{n}\sum_{i=1}^n(\lvert a\rvert+y_i+\epsilon)\\
        &\leq \int_X f\mathop{d\mu}+\epsilon[2\mu(K)+\lvert a\rvert+b+\epsilon].
    \end{aligned}$$

이 성립하고, $\epsilon$은 임의의 양수이므로 드디어 증명이 끝난다.

</details>



---
**Reference**

**[Rud]** W. Rudin, *Real and complex analysis* Mathematics series. McGraw-Hill, 1987.

---

[^1]: 물론 $\Lambda f$는 $\mathbb{C}$의 원소일 뿐만 아니라 양의 실수다. 앞서 만든 $f$는 positive이고 $\Lambda$는 positive linear functional이기 때문.
