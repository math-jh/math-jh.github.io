---

title: "노름과 대각합"
excerpt: ""

categories: [Math / Linear Algebra]
permalink: /ko/math/linear_algebra/norm_and_trace
header:
    overlay_image: /assets/images/Math/Linear_Algebra/Norm_and_trace.png
    overlay_filter: 0.5
sidebar: 
    nav: "linear_algebra-ko"

date: 2024-10-13
last_modified_at: 2024-10-13
weight: 12

---

## 원소의 노름과 대각합

언제나처럼 commutative ring $A$가 주어졌다 하고, 이번에는 unital associative $A$-algebra $E$가 주어졌다 하자. 그럼 임의의 $E$-module은 항상 restriction of scalar를 통해 $A$-module로 생각할 수 있다.

<div class="definition" markdown="1">

<ins id="def1">**정의 1**</ins> $E$-module $M$이 주어졌다 하고, $M$이 $A$-module로서 유한한 basis를 갖는다 하자. 임의의 $\alpha\in E$에 대하여, 다음의 $E$-module endomorphism

$$\alpha_M: x\mapsto \alpha x$$

이 주어졌다 하자. 그럼 $\alpha_M$의 trace, determinant, characteristic polynomial을 각각 $\alpha$의 *trace*, *norm*, *characteristic polynomial*이라 부르고,

$$\tr_{M/A}(\alpha)=\tr(\alpha_M),\qquad N_{M/A}(\alpha)=\det(\alpha_M),\qquad \chi_{M/A,\alpha}(\x)=\chi_{\alpha_M}(\x)$$

으로 표기한다.

</div>

그럼 trace와 determinant의 성질로부터

$$\tr_{M/A}(\alpha+\beta)=\tr_{M/A}(\alpha)+\tr_{M/A}(\beta),\qquad \tr_{M/A}(\alpha\beta)=\tr_{M/A}(\beta\alpha),\qquad N_{M/A}(\alpha\beta)=N_{M/A}(\alpha)N_{M/A}(\beta)$$

를 얻는다. 또, 이들을 행렬의 trace, determinant, characteristic polynomial로 볼 수 있는 것도 앞선 글에서 살펴보았다. 