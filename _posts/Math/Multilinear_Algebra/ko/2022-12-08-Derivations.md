---

title: "미분"
excerpt: "Differential module"

categories: [Math / Multilinear Algebra]
permalink: /ko/math/multilinear_algebra/derivations
header:
    overlay_image: /assets/images/Math/Multilinear_Algebra/Derivations.png
    overlay_filter: 0.5
sidebar: 
    nav: "multilinear_algebra-ko"

date: 2022-12-12
last_modified_at: 2024-10-16
weight: 120

---

## 미분의 정의

우리는 이제 미분의 개념을 도입한다. 더 정확히 말하자면 우리가 생각할 것은 미분형식의 개념으로, 이를 다루기 위해서는 graded algebra가 필요하다. 앞으로 graded algebra의 구조를 주는 abelian group을 $\Delta$로 표기하기로 한다. 

<div class="definition" markdown="1">

<ins id="def1">**정의 1**</ins> Abelian group $(\Delta, +, 0)$에 대하여, 함수 $\varepsilon : \Delta \times \Delta \to \\{ \pm 1 \\}$가 다음의 세 조건을 만족한다 하자. 

- $\varepsilon(\alpha + \alpha', \beta) = \varepsilon(\alpha, \beta)\varepsilon(\alpha', \beta)$  
- $\varepsilon(\alpha, \beta + \beta') = \varepsilon(\alpha, \beta)\varepsilon(\alpha, \beta')$  
- $\varepsilon(\beta, \alpha) = \varepsilon(\alpha, \beta)$

이 때, $\varepsilon$을 *commutation factor*라 부른다. 

</div>

그럼 특히 $\varepsilon(2.\alpha, \beta) = \varepsilon(\alpha, 2.\beta) = 1$이다.

우리가 가장 관심있는 예시는 $\Delta=\mathbb{Z}$인 경우이다. 이 경우, [정의 1](#def1)에 의하여 $\varepsilon$은 $\varepsilon(1,1)$에서의 값에 의해 완전하게 결정되며, 따라서 $\Delta=\mathbb{Z}$에 정의되는 commutation factor는 오직

$$\varepsilon(p,q)=1,\qquad \varepsilon(p,q)=(-1)^{pq}$$

뿐이다. Commutation factor는 degree $p$와 degree $q$의 원소의 곱을 생각할 때, 이들이 서로 순서를 바꿀 때 생겨나는 부호로써 등장할 것이다. 

이제 commutative ring $A$, $\Delta$-graded $A$-module $E$, $E'$, $E''$, $F$, $F'$, $F''$$A$-bilinear map들

$$\mu: E \times E' \to E'', \qquad \lambda_1: F \times E' \to F', \qquad \lambda_2: E \times F' \to F''$$

그리고 이들이 유도하는 $A$-linear map들

$$E \otimes_A E' \to E'', \qquad F \otimes_A E' \to F'', \qquad E \otimes_A F' \to F''$$

을 생각하고, 이 세 $A$-linear map들이 모두 degree $0$ graded homomorphism이라 하자. 이들은 각각 곱셈에 해당하는 연산들로, 우리는 가령 $x\otimes x'$의 $E''$에서의 image를 간단히 $xx'$로 적을 것이다. $E\otimes_A E'$에서 원소 $x\otimes x'$는 degree $\degree(x)+\degree(x')$에 있으므로, 위와 같은 가정에서 $xx'$는 $E''$의 degree $\degree(x)+\degree(x')$ 성분에 있게 된다. 

이제 다음을 정의한다. 

<div class="definition" markdown="1">

<ins id="def2">**정의 2**</ins> 위의 상황에 더해 commutation factor $\varepsilon: \Delta \times \Delta \to \\{ \pm 1 \\}$이 주어졌다 하자. 그럼 $(E, E', E'')$에서 $(F, F', F'')$로 가는 degree $\delta$의 *$(A, \varepsilon)$-derivation<sub>$(A,\varepsilon)$-미분</sub>* 혹은 간단히 *$\varepsilon$-derivation*은 다음의 조건 

$$d''(xx') = (dx)x' + \varepsilon(\delta, \deg(x))x(d'x')$$

을 만족하는 graded $A$-module homomorphism들의 triple $d: E \rightarrow F$, $d': E' \rightarrow F'$, $d'': E'' \rightarrow F''$이다. 만일 $\varepsilon$이 항상 $1$이 되어, 위의 식에서 $\varepsilon$을 없앨 수 있다면 $(d,d',d'')$를 간단히 *derivation*이라 부른다. 

</div>

위의 정의에서 혼동을 피하기 위해서는 각 항들이 어디에 속하는지, 가령 우변의 $(dx)x'$는 $dx\in F$와 $x'\in E'$를 $\lambda_1$에 의해 곱하여 얻은 $F''$의 원소라는 것 등을 살펴보는 것도 좋다. 그러나 실제로는 우리는 다음과 같은 특별한 두 경우에 관심이 있다.

1. $E=F$, $E'=F'$, $E''=F''$, 그리고 세 개의 bilinear map $ \mu, \lambda_1, \lambda_2 $가 모두 동일한 경우
2. $E=E'=E''$, $F=F'=F''$이고, 따라서 $\mu:E\otimes_A E \rightarrow E$에 의해 $E$가 *graded* algebra가 되며, 

    $$\lambda_1: F \otimes_A E \to F, \qquad \lambda_2: E \otimes_A F \to F$$

    인 경우. 이 경우, 임의의 $x,y\in E$에 대하여 다음의 식

    $$d(xy)=(dx)y+\varepsilon(\delta, \deg(x))x(dy)$$

    을 만족하는 <em_ko>단일한</em_ko> $d:E \rightarrow F$를 $E$에서 $F$로의 $\varepsilon$-derivation이라 부른다. 

두 번째 경우를 motivation 삼아 우리는 표기의 편의상 $d, d', d''$를 모두 같은 문자 $d$로 통일하여 쓰기도 하며, 그럼 [정의 2](#def2)의 식은

$$d(xx')=(dx)x'+\varepsilon(\delta,\deg(x))x (dx)$$

로 쓸 수 있으며, 우리가 다루는 대부분의 경우에서는 이 정도 표기법의 남용은 혼동을 주지 않을 것이다. 

만일 위의 두 경우가 모두 성립하여 $E=E'=E''=F=F'=F''$이고 $\lambda_1, \lambda_2$가 $E$에서의 곱셈이며, derivation이 단일한 graded endomorphism $d: E \rightarrow E$인 경우가 가장 많이 등장한다. 그럼 $\varepsilon$-derivation은 $A$에서 $A$로 가는 함수로 생각할 수 있으므로 이 경우 우리는 $\varepsilon$-derivation을 간단히 $A$의 $\varepsilon$-derivation이라 부른다. 

한편 우리는 앞에서 $\Delta=\mathbb{Z}$인 경우가 우리의 주된 관심사라 하였는데, 이 경우 non-trivial한 commutation factor $\varepsilon(p,q)=(-1)^{pq}$를 생각하면, 이 $\varepsilon$에 대하여 임의의 짝수 차수 $\varepsilon$-derivation은 항상 $\varepsilon$의 영향을 무시할 수 있다는 것을 안다. 홀수 차수의 경우, 임의의 homogeneous element $x\in E$에 대하여 다음의 식

$$d(xx')=(dx)x'+(-1)^{\deg x}x(dx')$$

이 성립한다. 이 경우 $d$를 *anti-derivation*이라 부른다. 

## 미분형식

지금까지의 논의가 어떻게 적용될 수 있는지를 알기 위해, 잠시 간단하면서 핵심적인 예시를 살펴보자. $\mathbb{k}$를 field라 하고, polynomial algebra $A=\mathbb{k}[\x_1,\ldots, \x_n]$을 생각하자. 이제 free $A$-module $M$을 다음의 원소들 

$$d\x_1,d\x_2,\ldots, d\x_n$$

로 생성되도록 잡고 exterior algebra $\bigwedge(M)$을 생각하면 이 exterior algebra는

$$\bigwedge(M)=\bigoplus_{d=0}^n{\bigwedge}^d(M)$$

으로 주어지며, 이 때 $\bigwedge^0(M)=A$이고 각각의 $d$에 대하여 $\bigwedge^d(M)$은 

$$e_J=e_{j_1}\wedge e_{j_2}\wedge\cdots\wedge e_{j_d},\qquad j_1<\cdots< j_d$$

의 꼴로 생성되는 free $A$-module이다. 

## Bracket

한편, 위의 두 경우 중 첫째 조건이 성립한다 가정하자. 그럼 $d=(d,d',d'')$은 $(E,E',E'')$에서 자기자신으로의 함수로 생각할 수 있으므로, $\varepsilon$-derivation들의 합성 또한 생각할 수 있다. 그러나 일반적으로 [정의 2](#def2)의 식을 보면, 임의로 주어진 두 degree $\delta_1$, $\delta_2$의 $\varepsilon$-derivation $d_1,d_2$와 임의의 $x\in E$, $x'\in E'$에 대하여

$$\begin{aligned}(d_2\circ d_1)(xx')&=d_2((d_1x)x'+\varepsilon(\delta_1, \deg(x))x(d_1'x'))\\&=(d_2d_1x)x'+\varepsilon(\delta_2,\deg(d_1x))(d_1x)(d_2'x')+\varepsilon(\delta_1, \deg(x))(d_2x)(d_1'x')+\varepsilon(\delta_1, \deg(x))\varepsilon(\delta_2, \deg(x))x(d_2' d_1'x')\end{aligned}$$

이므로 일반적인 상황에서 $\varepsilon$-derivation들의 합성은 $\varepsilon$-derivation이 아니다. 즉, 일반적으로 $\Delta$-graded $A$-module들의 triple들로 이루어진 category를 생각하고, 고정된 triple $(E,E',E'')$의 endomorphism algebra

$$\End_{\bgr_\Delta \Alg{A}^3}(E, E', E'')$$

를 생각하면, $\varepsilon$-derivation들의 모임은 이 endomorphism algebra의 subalgebra를 정의하지 않는다. 그러나 위의 계산을 살펴본다면, 이 위에 어떠한 종류의 곱셈을 정의해야 $\varepsilon$-derivation들의 모임을 정의할 수 있는지도 명확하다. 즉 우변의 네 항 중, 가운데의 두 항을 없애주면 $d_2d_1$이 degree $\delta_1+\delta_2$의 $\varepsilon$-derivation이 될 것이다. 

이를 위해 우선 가장 일반적으로 임의의 $\Delta$-graded algebra $G$와 고정된 commutation factor $\varepsilon$에 대하여, $G$의 두 homogeneous element $x,y$에 대하여 이들의 *$\varepsilon$-bracket*을 다음의 식

$$[x,y]_\varepsilon=xy-\varepsilon(\deg(x),\deg(y))yx$$

으로 정의하자. 그럼 이를 통해 $G=\End_{\bgr_\Delta \Alg{A}^3}(E, E', E'')$에서의 $\varepsilon$-bracket을 정의할 수 있다. 

<div class="proposition" markdown="1">

<ins id="prop3">**명제 3**</ins> $d_1, d_2$를 $(E, E', E'')$ 위의 $\varepsilon$-derivation들이라 하자. 각각의 degree를 $\delta_1$, $\delta_2$라 하면, 이들의 $\varepsilon$-bracket

$$[d_1, d_2]_\varepsilon = d_1 \circ d_2 - \varepsilon_{\delta_1, \delta_2} \, d_2 \circ d_1$$

은 degree $\delta_1 + \delta_2$를 갖는 또 다른 $\varepsilon$-derivation이 된다. 특히, 만일 $d$가 degree $\delta$를 갖는 $\varepsilon$-derivation이고, $\varepsilon_{\delta, \delta} = -1$이라면, $d^2 = d \circ d$는 derivation이다.

</div>

이에 대한 증명은 앞에서 계산한 $(d_2\circ d_1)(xx')$의 전개식을 사용하면 자명하다. 

그럼 특히 $\Delta=\mathbb{Z}$인 경우로 한정지으면, 위의 명제는 다음의 따름정리를 갖는다. 

<div class="proposition" markdown="1">

<ins id="prop4">**따름정리 4**</ins> $\Delta = \mathbb{Z}$라 하자. 이때 다음이 성립한다:

1. Antiderivation의 제곱은 derivation이다.  
2. 두 derivation의 bracket은 derivation이다.  
3. antiderivation과 짝수 차수 derivation의 bracket은 antiderivation이다.  
4. $d_1$, $d_2$가 antiderivation이면, $d_1 d_2 + d_2 d_1$은 derivation이다.

</div>

