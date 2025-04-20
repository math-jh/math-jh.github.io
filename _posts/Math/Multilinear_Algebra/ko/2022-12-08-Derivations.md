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

을 만족하는 degree $\delta$ graded $A$-module homomorphism들의 triple $d: E \rightarrow F$, $d': E' \rightarrow F'$, $d'': E'' \rightarrow F''$이다. 만일 $\varepsilon$이 항상 $1$이 되어, 위의 식에서 $\varepsilon$을 없앨 수 있다면 $(d,d',d'')$를 간단히 *derivation*이라 부른다. 

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

지금까지의 논의가 어떻게 적용될 수 있는지를 알기 위해, 잠시 간단한 예시를 살펴보자. 여기에서 $\mathbb{k}$는 field이고 polynomial algebra $E=\mathbb{k}[\x_1,\ldots, \x_n]$이다. 

우선 degree $0$ derivation은 항상 commutation factor를 무시할 수 있으므로, $E$를 non-graded $\mathbb{k}$-algebra로 본 후 $E$에서 $E$로의 derivation을 생각하면 $\varepsilon$은 등장하지 않는다. 이제 각각의 $i$에 대하여, $\partial_i:E \rightarrow E$를 편미분 $\partial/\partial \x_i$로 정의하면 Leibniz rule에 의해 [정의 2](#def2)의 등식이 만족된다. 

이번에는 graded algebra의 예시를 보자. 위와 같이 정의된 polynomial algebra $E$에 대하여, free $A$-module $M$을 다음의 원소들 

$$d\x_1,d\x_2,\ldots, d\x_n$$

로 생성되도록 잡고 exterior algebra $\bigwedge(M)$을 생각하면 이 exterior algebra는 $\mathbb{Z}$-graded $E$-algebra

$$\bigwedge(M)=\bigoplus_{d=0}^n{\bigwedge}^d(M)$$

으로 주어지며, 이 때 $\bigwedge^0(M)=A$이고 각각의 $k$에 대하여 $\bigwedge^k(M)$은 

$$d\x_J=d\x_{j_1}\wedge d\x_{j_2}\wedge\cdots\wedge d\x_{j_k},\qquad j_1<\cdots< j_k$$

의 꼴로 생성되는 free $E$-module이다. ([\[다중선형대수학\] §텐서대수, ⁋명제 13](/ko/math/multilinear_algebra/tensor_algebras#prop13)) 이제 각각의 basis

$$f\; d\x_{j_1}\wedge d\x_{j_2}\wedge\cdots\wedge d\x_{j_d}\in {\bigwedge}^k(M)$$

에 대하여 다음의 식

$$d(f\; d\x_{j_1}\wedge d\x_{j_2}\wedge\cdots\wedge d\x_{j_k})=\sum_{i=1}^n\frac{\partial f}{\partial \x_i}d\x_i\wedge d\x_{j_1}\wedge d\x_{j_2}\wedge\cdots\wedge d\x_{j_k}\in{\bigwedge}^{k+1}(M)$$

으로 정의하면 이를 확장하여 $d: \bigwedge M \rightarrow \bigwedge M$을 정의할 수 있다. 그럼 $d$는 degree $1$을 갖는 $\bigwedge(M)$의 antiderivation이 된다. 

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

<ins id="prop4">**따름정리 4**</ins> $\Delta = \mathbb{Z}$라 하자. 이때 다음이 성립한다.

1. Antiderivation의 제곱은 derivation이다.  
2. 두 derivation의 bracket은 derivation이다.  
3. antiderivation과 짝수 차수 derivation의 bracket은 antiderivation이다.  
4. $d_1$, $d_2$가 antiderivation이면, $d_1 d_2 + d_2 d_1$은 derivation이다.

</div>

한편, polynomial algebra 위에 정의된 편미분을 보면 이들은 임의의 $i,j$에 대하여 $\partial_i\partial_j=\partial_j\partial_i$를 만족한다. 이제 일반적인 미분연산자처럼 $D=\partial_i+\partial_j$를 적고, $D^2$를 생각하면 이는

$$D^2=(\partial_i+\partial_j)^2=\partial_i^2+\partial_i\partial_j+\partial_j\partial_i+\partial_j^2$$

와 같이 전개할 수 있으며, $\partial_i$와 $\partial_j$가 commute하므로 이를 더 간단히 

$$D^2=\partial_i^2+2\partial_i\partial_j+\partial_j^2$$

와 같이 적을 수도 있다. 다음 명제는 이를 더욱 일반화한 것이다. 

<div class="proposition" markdown="1">

<ins id="prop5">**명제 5**</ins> 위 가정과 표기 아래에서, 미지수 $T_1, \dots, T_n, T_1', \dots, T_n'$에 대한 다항식 
$F \in A[\x_1, \dots, \x_k]$가 주어졌다고 하자. 즉 $F(T)$, $F(T')$는 각각

$$F(T) = F(T_1, \dots, T_n), \qquad F(T') = F(T_1', \dots, T_n')$$

를 뜻한다. 비슷하게 

$$F(T + T') = F(T_1 + T_1', \dots, T_n + T_n')$$

라고 정의하자. 

이제 만일 다항식 $P$가 다음의 식

$$P(T + T') = \sum_i Q_i(T) R_i(T')$$

을 만족한다면, 임의의 $x\in E$, $x\'\in E'$에 대하여 다음의 식

$$P(D)(x x') = \sum_i (Q_i(D) x)(R_i(D) x')$$

이 성립한다. 

</div>

## $A$-대수의 미분

이제 우리는 [정의 2](#def2) 이후 다뤘던 두 가지 특별한 경우 중 두 번째 경우를 살펴본다. 즉 $\Delta$-graded $A$-algebra $E$와 graded $A$-module $F$, 그리고 두 개의 곱셈 $E\otimes_AF \rightarrow F$와 $F\otimes_AE \rightarrow F$가 주어졌다 하자. 

<div class="proposition" markdown="1">

<ins id="prop6">**명제 6**</ins> Degree $\delta$의 $\varepsilon$-derivation $d:E \to F$에 대하여, $\ker(d)$는 $E$의 graded subalgebra이며, 만약 $E$가 $1$을 갖는다면 $1 \in \ker(d)$이다.

</div>
<details class="proof" markdown="1">
<summary>증명</summary>

우선 $\ker(d)$가 $E$의 $A$-submodule인 것은 자명하므로, $\ker(d)$가 곱셈에 대해 닫혀있다는 것만 보이면 된다. 임의의 homogeneous $x, y \in \ker(d)$에 대하여,

$$d(xy) = (dx)y + \varepsilon(\delta, \deg(x))x(dy) = 0$$

이므로 $xy \in \ker(d)$이다. 따라서 $\ker(d)$는 graded subalgebra이다.

이제 만일 $E$가 $1$을 갖는다면 $1$은 degree $0$이므로,

$$d(1) = d(1 \cdot 1) = (d1) \cdot 1 + \varepsilon_{\delta, 0} \cdot 1 \cdot (d1) = d1 + d1 = 2d1$$

이 되어, $d(1) = 0$임을 알 수 있다.

</details>

따라서 만일 $d_1,d_2$가 $E$에서 $F$로의 degree $\delta$ $\varepsilon$-derivation이고 이들이 $A$의 algebra로서의 generator에서 그 값이 모두 같다면 $d_1=d_2$여야 한다. 한편 역원에 대해서는 다음이 성립한다.

<div class="proposition" markdown="1">

<ins id="prop7">**명제 7**</ins> $E$가 $1$을 갖는 $\Delta$-graded $A$-algebra라 하고, degree $\delta$의 $\varepsilon$-derivation $d:E \to F$를 생각하자. 만일 $x$가 $E$의 invertible homogeneous element라면, 그 역원 $x^{-1}$에 대하여 다음의 식

$$d(x^{-1}) = -\varepsilon_{\delta, \deg(x)} x^{-1}(d(x))x^{-1}
= -\varepsilon_{\delta, \deg(x)} (d(x)) x^{-2}$$

이 성립한다. 

</div>
<details class="proof" markdown="1">
<summary>증명</summary>

[명제 5](#prop5)에 의해 $d(1) = 0$이므로,

$$0 = d(xx^{-1}) = d(x))x^{-1} + \varepsilon_{\delta, \deg(x)}x(d(x^{-1})$$

이다. 양변의 왼쪽에 $x^{-1}$를 곱하면

$$0 = x^{-1}(d(x))x^{-1} + \varepsilon_{\delta, \deg(x)} d(x^{-1})$$

이고, 정리하면

$$d(x^{-1}) = -\varepsilon_{\delta, \deg(x)} x^{-1}(d(x))x^{-1}.
$$

을 얻는다. 또한 $x^{-1}$의 차수는 $-\deg(x)$인 것을 이용하여 $d(x^{-1}x)$를 계산하면 둘째 등식을 얻는다. 

</details>

<div class="proposition" markdown="1">

<ins id="prop8">**명제 8**</ins> 어떤 $A$-algebra $E$가 integral domain이라 하고, 그 field of fraction $K=\Frac E$를 생각하자. 임의의 $K$-vector space $F$를 $E$-module로 보아 $A$-derivation $d:E \rightarrow F$를 생각하면, $d$는 유일한 방식으로 $K$에서 $F$로의 $A$-derivation으로 확장된다. 

</div>

<details class="proof" markdown="1">
<summary>증명</summary>

임의의 derivation $d:E \rightarrow f$가 주어졌다 하고, $d$를 $K$ 위로 확장한 $\bar{d}$가 존재한다면, [명제 7](#prop7)을 적용하여 다음의 식

$$\bar{d}(u/v) = v^{-1} d(u) - v^{-2} u\, d(v)$$

이 성립해야 한다는 것을 알고, 따라서 $\bar{d}$가 만일 존재한다면 그 표현은 유일하다.

이 정의가 $B$의 원소 표기 $u/v$의 선택에 의존하지 않음을 보이자. 즉, $u/v = u'/v'$일 때도

$$v^{-1} d(u) - v^{-2} u\, d(v) = v'^{-1} d(u') - v'^{-2} u'\, d(v')$$

이어야 한다.

$uv' = u'v$라고 두자. 양변에 $d$를 취하면

$$v' d(u) + u\, d(v') = v\, d(u') + u'\, d(v)$$

이므로 양변에 $vv'$를 곱하면

$$v v' d(u) - u\, v\, d(v') = v v' d(u') - u'\, v'\, d(v)$$

이고, 이를 정리하면

$$v' d(u) - v^{-1} u\, d(v) = v' d(u') - v'^{-1} u'\, d(v')$$

이다. 따라서 정의는 $F$의 원소 $u/v$의 표현에 무관하게 잘 정의되어 있다. 이제 $\bar{d}$가 실제로 $K$에서 $F$로의 $A$-derivation의 조건을 ㅁ낮곻나다는 것은 단순한 계산이다. 

</details>

다음 명제에서, 표기의 편의를 위해 임의의 degree $\delta$ $\varepsilon$-derivation $d:A \rightarrow E$에 대하여 

$$Z_\varepsilon=\{a\in A\mid \text{$xa_d=\varepsilon(\deg(a),\deg(x))a_dx$ for all homogeneous component $a_d$ of $a$ and for all homogeneous $x\in E$.}\}$$

으로 정의하자. 

<div class="proposition" markdown="1">

<ins id="prop9">**명제 9**</ins>  $A$가 unital graded associative $A$-algebra이고 $E$가 graded $(A, A)$-bimodule이라 하자. 이제 $d: A \to E$가 degree $\delta$의 $\varepsilon$-derivation이고, $a$가 degree $\alpha$의 $Z_\varepsilon$의 homogeneous element라 하자. 그러면 morphism

$$x \mapsto a (d x)$$

는 degree $\delta + \alpha$의 $\varepsilon$-derivation이다.

</div>
<details class="proof" markdown="1">
<summary>증명</summary>

주어진 morphism을 $d'$로 적으면 이 morphism은 자명하게 $A$-linear이다. 이제 $d'$가 $\varepsilon$-derivation임을 보이기 위해 임의의 degree $\delta'$ homogeneous element $x$와 임의의 $y\in A$에 대하여 

$$\begin{aligned}d'(xy)&=a(dx)y+\varepsilon(\delta, \delta')a(x(dy))\\&=a(dx)y+\varepsilon(\delta, \delta')\varepsilon(\alpha,\delta')xa(dy)\\&=(d'x)y+\varepsilon(\delta+\alpha,\delta')x(d'y)\end{aligned}$$

이므로 $d'$는 degree $\delta + \alpha$ $\varepsilon$-derivation이 된다.

</details>

한편 $E$가 $\varepsilon$-bracket이 주어진 $\Delta$-graded (associative) $A$-algebra라면 이 위에는 자연스러운 $\varepsilon$-derivation이 존재한다. 

<div class="definition" markdown="1">

<ins id="def10">**정의 10**</ins> Graded $A$-algebra $E$의 homogeneous element $z\in E$에 대하여, 다음의 morphism 

$$x\mapsto [z,x]_\varepsilon$$

을 $\ad_\varepsilon(z)$으로 적는다. 

</div>

그럼 다음이 성립한다.

<div class="proposition" markdown="1">

<ins id="prop11">**명제 11**</ins>  $E$가 graded $A$-algebra라 하자. 

1. 임의의 $\varepsilon$-derivation $d : E \rightarrow E$와 $E$의 모든 homogeneous 원소 $z$에 대하여 ${[d, \ad(a)]_\varepsilon = \ad(dz)}$이 성립한다. 
2. 만일 $A$가 associative라면, $\ad(z)$는 $A$의 $\varepsilon$-derivation이며, 그 degree는 $\deg(z)$이다.
</div>

<details class="proof" markdown="1">
<summary>증명</summary>

1. $d$가 degree $\delta$ $\varepsilon$-derivation이라 하고, $\zeta = \deg(z)$라고 하자. 이제 $f = [d, \ad(z)]_\varepsilon$라 하면, 모든 degree $\xi$ homogeneous element $x \in A$에 대해, 

    $$\begin{aligned}f(x)&=d(z x - \varepsilon(\zeta, \xi) x z) - \varepsilon(\delta, \zeta) (z (dx) - \varepsilon(\zeta, \delta+\xi) (dx) z) \\&= d(z x) - \varepsilon(\zeta, \xi) d(x z) - \varepsilon(\delta, \zeta) z (dx) + \varepsilon(\zeta,2.\delta+\xi) d(x) z \\&=(dz)x+\varepsilon(\delta, \zeta)z(dx)-\varepsilon(\zeta,\xi)((dx)z+\varepsilon(\delta, \xi)x(dz))- \varepsilon(\delta, \zeta) z (dx) + \varepsilon(\zeta,2.\delta+\xi) (dx) z\\&=(dz)x+\varepsilon(\delta,\zeta)z(dx)-\varepsilon(\zeta,\xi)(dx)z-\varepsilon(\delta+\zeta,\xi)x(dz)-\varepsilon(\delta,\zeta)z (dx)+\varepsilon(\zeta,\xi)(dx)z\\&=(dz)x-\varepsilon(\delta+\zeta,\xi)x(dz)=[dz,x]_\varepsilon=\ad_\varepsilon(dz)(x)\end{aligned}$$

    이므로 원하는 결과를 얻는다. 
2. 모든 degree $\xi$ homogeneous element $x \in A$와 degree $\eta$ homogeneous element $y \in A$에 대해,  
    
    $$\begin{aligned}\ad(z)(x y) &= z(x y) - \varepsilon(\zeta, \xi + \eta)(x y) z \\&= (z x) y - \varepsilon(\zeta, \xi) x z y + \varepsilon(\zeta, \xi) x z y - \varepsilon(\zeta, \xi + \eta) x y z \\&= (ax-\varepsilon(\zeta,\xi xz)y+\varepsilon(zeta,\xi)x(ay-\varepsilon(\zeta,\eta)ya)\\&=\ad(z)(x) \cdot y + \varepsilon(\zeta, \xi) x \cdot \ad(z)(y)\end{aligned}$$

    이다.

</details>

따라서, $E$가 associative graded $A$-algebra라면 [정의 10](#def10)을 통해 $E$의 임의의 homogeneous가 $E$에서 자기 자신으로의 $\varepsilon$-derivation을 정의하며, 우리는 이를 *inner $\varepsilon$-derivation*이라 부른다. 

이것이 성립할 경우, 위의 식에서 $d$를 inner $\varepsilon$-derivation으로 대체해주면 다음 따름정리를 얻는다. 

<div class="proposition" markdown="1">

<ins id="cor12">**따름정리 12**</ins> Associative graded algebra $E$의 두 homogeneous 원소 $x,y$에 대해 다음의 식

$${[\ad_\varepsilon(x), \ad_\varepsilon(y)]_\varepsilon = \ad_\varepsilon([x,y]_\varepsilon)}$$

이 항상 성립한다. 

</div>

또한, 위의 따름정리의 등식은 임의의 homogeneous $z\in E$에 대해 확인함으로써 얻을 수 있으므로, $x,y,z$가 각각 degree $\xi,\eta,\zeta$의 homogeneous element라 하면 다음의 식

$${\varepsilon}_{\xi, \zeta} [[x, [y,z]_{\varepsilon}]_{\varepsilon} + \varepsilon_{\eta,\xi} [y, [z,x]_{\varepsilon}]_{\varepsilon} + \varepsilon_{\zeta,\eta} [z, [x,y]_{\varepsilon}]_{\varepsilon} = 0$$

이 성립하며, 우리는 이를 *Jacobi identity*라 부른다. 

