---

title: "실수집합의 정의"
excerpt: "기본정의"

categories: [Math / Analayis]
permalink: /ko/math/analysis/construction_of_R
header:
    overlay_image: /assets/images/Analysis/Construction_of_R.png
    overlay_filter: 0.5
sidebar: 
    nav: "analysis-ko"

date: 2022-03-13
last_modified_at: 2022-10-14
weight: 1

published: false

---

우리는 집합론에서 자연수를 정의했다. ([집합론, §서수와 정렬집합<sup>†</sup>](/ko/math/set_theory/ordinals)) 이로부터 정수를 정의하고, 그 후 유리수로 확장하는 것은 덧셈과 곱셈에 대한 역원을 추가해주는 것으로 생각할 수 있다. (<#ref#>) 그러나 유리수로부터 실수를 얻어내는 것은 이와는 결이 다르다. 이는 실수가 유리수에 비해 갖고 있는 성질이 *완비성*이라 부르는, 해석학에서 다루는 성질이기 때문이다. 이번 글에서는 완비성의 개념을 정의하고, 이로부터 실수를 정의한다.

## 코시 수열

유리수 집합 $\mathbb{Q}$는 totally ordered set이므로, 이 위에 정의된 order topology가 존재한다. ([위상수학, §거리위상 (1), 정의 1](/ko/math/topology/metric_topology_1#df1)) 따라서 $\mathbb{Q}$의 원소들로 이루어진 수열의 수렴을 [위상수학, §수열의 수렴, 정의 7](/ko/math/topology/basic_definition_3)과 같이 정의할 수 있다. $\mathbb{Q}$ 위에 다음의 식

$$d(x,y)=\lvert x-y\rvert$$

으로 정의된 metric[^1] $d$가 존재한다는 것을 알 수 있으므로, 이 경우 수열의 수렴은 임의의 $\epsilon>0$마다 적당한 자연수 $N$이 존재하여

$$n>N\implies \lvert x_n-x\rvert<\epsilon$$

이도록 하는 $x\in\mathbb{Q}$가 존재한다는 것으로 이해할 수 있다. 

<div class="definition" markdown="1">

<ins id="df1">**정의 1**</ins> 유리수열 $(x\_n)\_{n\in\mathbb{N}}$이 *Cauchy sequence<sub>코시수열</sub>*이라는 것은 임의의 양의 유리수 $\epsilon>0$마다 적당한 자연수 $N$이 존재하여, $m,n>N$일 때마다 $\lvert x_m-x_n\rvert<\epsilon$이 성립하도록 할 수 있는 것이다.

</div>

가령 다음의 유리수열

$$3,\quad 3.1,\quad 3.14,\quad 3.141,\quad\cdots$$

은 코시수열이다. 임의의 양의 유리수 $\epsilon>0$이 주어졌다 하면, $10^{-N}<\epsilon$을 만족하는 $N$을 사용하면 된다. 삼각부등식과 위의 정의들로부터, 임의의 수렴하는 수열은 Cauchy라는 것이 명확하다. 반면 위의 수열은 유리수에서는 수렴하지 않으므로 이 명제의 역은 성립하지 않는다. 그러나 수열을 $\mathbb{Q}$ 대신 $\mathbb{R}$에서 정의된 것으로 생각하면 위의 수열은 실수 $\pi$로 수렴하며, 이 성질이 정확하게 유리수와 실수를 구분하는 성질이 된다.

<div class="definition" markdown="1">

<ins id="df2">**정의 2**</ins> 

</div>



---

**Reference**

**[Rud]** W.Rudin, *Principles of mathematical analysis*, McGraw-Hill, 1976.    

---

[^1]: 정의에 의해 metric은 $\mathbb{R}$로의 함수이므로, 실수를 정의하지 않은 상황에서 metric을 논하는 것은 아주 사소한 선후관계 문제가 있긴 하다. 