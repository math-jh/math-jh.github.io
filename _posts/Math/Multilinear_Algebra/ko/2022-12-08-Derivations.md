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

이제 commutative ring $A$, $\Delta$-graded $A$-module $E$, $E'$, $E''$, $F$, $F'$, $F''$와 $A$-bilinear map들

$$\mu: E \times E' \to E'', \qquad \lambda_1: F \times E' \to F', \qquad \lambda_2: E \times F' \to F''$$

그리고 이들이 유도하는 $A$-linear map들

$$E \otimes_A E' \to E'', \qquad F \otimes_A E' \to F', \qquad E \otimes_A F' \to F''$$

을 생각하고, 이 세 $A$-linear map들이 모두 degree $0$ graded homomorphism이라 하자. 이들은 각각 곱셈에 해당하는 연산들로, 우리는 가령 $\alpha\otimes\alpha'$의 $E''$에서의 image를 간단히 $\alpha\alpha'$로 적을 것이다. $E\otimes_A E'$에서 원소 $\alpha\otimes\alpha'$는 degree $\degree(\alpha)+\degree(\alpha')$에 있으므로, 위와 같은 가정에서 $\alpha\alpha'$는 $E''$의 degree $\degree(\alpha)+\degree(\alpha')$ 성분에 있게 된다. 

이제 다음을 정의한다. 

<div class="definition" markdown="1">

<ins id="def2">**정의 2**</ins> 위의 상황에 더해 commutation factor $\varepsilon: \Delta \times \Delta \to \{ \pm 1 \}$이 주어졌다 하자. 그럼 $(E, E', E'')$에서 $(F, F', F'')$로 가는 *$(A, \varepsilon)$-derivation<sub>$(A,\varepsilon)$-미분</sub>* 혹은 간단히 *$\varepsilon$-derivation*은 다음의 조건 

$$d''(\alpha\alpha') = (d\alpha) \cdot \alpha' + \varepsilon(\delta, \deg(\alpha))a \cdot (d'\alpha')$$

을 만족하는 graded $A$-module homomorphism $d: E \rightarrow F$, $d': E' \rightarrow F'$, $d'': E'' \rightarrow F''$이다. 

</div>


Commutative ring $A$를 고정하고, unital associative $A$-algebra $E$를 고정하자. 

<div class="definition" markdown="1">

<ins id="def1">**정의 1**</ins> $E$-module $M$을 고정하자. 그럼 $E$에서 $M$으로의 *$E$-derivation<sub>$E$-미분</sub>*은 식

$$d(x+x')=dx+dx',\qquad d(xx')=xdx'+x'dx$$

를 만족하는 $E \rightarrow M$을 의미한다. 만일 추가로 다음의 식

$$d(a\cdot 1_E)=0\qquad\text{for all $a\in A$}$$

이 성립한다면 이를 *$A$-derivation*이라 부른다. 

</div>

