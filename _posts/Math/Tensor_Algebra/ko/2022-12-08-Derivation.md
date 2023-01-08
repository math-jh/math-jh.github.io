---

title: "미분"
excerpt: "Differential module"

categories: [Math / Tensor Algebra]
permalink: /ko/math/tensor_algebra/derivation
header:
    overlay_image: /assets/images/Math/Tensor_Algebra/Derivation.png
    overlay_filter: 0.5
sidebar: 
    nav: "tensor_algebra-ko"

date: 2022-12-12
last_modified_at: 2022-12-12
weight: 5

---

## Sign convention

Exterior algebra $\bigwedge(M)$을 생각하자. 그럼 임의의 $x,y\in M=\bigwedge\nolimits^1(M)$에 대하여,

$$x\wedge y=-y\wedge x$$

가 성립한다. 반면, $x\wedge y\in \bigwedge\nolimits^2(M)$과 $z\in\bigwedge\nolimits^1(M)$에 대하여는

$$(x\wedge y)\wedge z=x\wedge(y\wedge z)=x\wedge(- z\wedge y)=(x\wedge -z)\wedge y=(z\wedge x)\wedge y=z\wedge (x\wedge y)$$

가 성립한다. 이와 같이 $\Delta$-graded algebra가 주어졌을 때 이들의 원소들이 commute할 필요는 없다. 이렇게 두 원소가 곱해진 순서를 바꿀 때 앞에 곱해지는 상수를 *commutation factor*라 부른다. 이는 다음 성질을 만족해야 한다. 

<div class="definition" markdown="1">

<ins id="df1">**정의 1**</ins> Commutative monoid $\Delta$가 주어졌다 하고, 항등원 $1$을 갖는 commutative ring $A$를 고정하자. 그럼 $\Delta$ 위에 정의된 *commutation factor over $A$*는 다음의 조건을 만족하는 함수 $\varepsilon:\Delta\times\Delta\rightarrow A$이다.

$$\varepsilon(\alpha_1+\alpha_2,\beta)=\varepsilon(\alpha_1,\beta)\varepsilon(\alpha_2,\beta),\quad\varepsilon(\alpha,\beta_1+\beta_2)=\varepsilon(\alpha,\beta_1)\varepsilon(\alpha,\beta_2),\quad \varepsilon(\alpha,\beta)\varepsilon(\beta,\alpha)=1$$

</div>

편의상 $\Delta=\mathbb{Z}$라 생각하면, 첫 번째 조건은 degree $\beta$를 가진 원소 $z$가 degree $\alpha_1,\alpha_2$를 가진 원소 $x,y$를 각각 넘을 때 생기는 commutation factor들의 곱이 $(xy)$를 한 번에 넘을 때 생기는 commutation factor와 같다는 것을 의미한다. 두 번째와 세 번째 조건도 마찬가지로 적절한 의미를 부여할 수 있다.

대부분의 경우 $A=\mathbb{Z}$인 경우가 관심의 대상이 된다. 이는 $\Delta$-graded algebra는 base ring이 무엇이든간에 항상 $\mathbb{Z}$-algebra로 생각할 수 있기 때문이다. 이러한 경우, 세 번째 조건에 의하여 $\varepsilon$은 $\Delta\times\Delta$에서 $\\{1,-1\\}$로의 함수로 생각할 수 있다. 여기에 더하여, 위와 같이 $\Delta=\mathbb{Z}$까지 추가로 가정하면 $\varepsilon$은 $(1,1)$에서의 값으로만 결정된다. 즉, $\varepsilon(1,1)=1$이라면

$$\varepsilon(p,q)=1\qquad\text{for all $p,q\in\mathbb{Z}$}$$

그리고 $\varepsilon(1,1)=-1$이라면

$$\varepsilon(p,q)=(-1)^{pq}\qquad\text{for all $p,q\in\mathbb{Z}$}$$

으로 주어진다. 특별히 후자의 경우를 *Koszul sign*이라 부른다.

## Derivation과 anti-derivation

<div class="definition" markdown="1">

<ins id="df2">**정의 2**</ins> $\Delta$-graded $A$-algebra $E=\bigoplus E_\alpha$에 대하여, linear map $D:E\rightarrow E$가 *homogeneous*라는 것은 고정된 $\alpha\in\Delta$가 존재하여, 모든 $\beta\in\Delta$마다 $D(E_\beta)\subseteq E_{\alpha+\beta}$가 성립하는 것이다. 이 때 $\alpha$를 $D$의 *degree*라 부른다.

</div>

<div class="definition" markdown="1">

<ins id="df3">**정의 3**</ins> $\Delta$-graded $A$-algebra $E=\bigoplus E_\alpha$와, 이 위에 정의된 degree $\degree(D)$의 homogeneous linear map $D$가 주어졌다 하자. 또, $\Delta$ 위에 commutation factor $\varepsilon$이 주어졌다 하자. 그럼 $D$가 *homogeneous $\varepsilon$-derivation*이라는 것은 모든 homogeneous element $a\in E$와 임의의 원소 $b\in E$에 대하여 다음의 식

$$D(ab)=D(a)b+\varepsilon(\degree(a),\degree(D))aD(b)$$

이 성립하는 것이다. 

</div>

위의 정의는 $a$가 homogeneous element일 때 정의되었지만, 임의의 원소 $a\in E$가 주어졌다 하더라도 $a$를 homogeneous element들로 분해한 후, 위의 식을 적용하여 $D(ab)$가 만족해야 할 조건을 찾을 수 있다. 이렇게 정의된 linear map $D$를 간단히 $\varepsilon$-derivation이라 부른다.

대부분의 경우 $\Delta=\mathbb{Z}$이고, commutation factor $\varepsilon$ 또한 $\mathbb{Z}$에서 값을 갖는다. 그럼 앞서 살펴본 것과 같이 가능한 sign은 다음의 두 가지가 있다.

$$\varepsilon(\degree(a),\degree(D))=1,\qquad \varepsilon(\degree(a),\degree(D))=(-1)^{\degree(a)\degree(D)}.$$

만일 $\degree(D)$가 짝수라면 두 가지 sign convention은 구별이 되지 않는다. 그러나 만일 $\degree(D)$가 홀수라면 두 sign convention이 구분되며, 전자의 경우 라이프니츠 법칙

$$D(ab)=D(a)b+aD(b)$$

을 만족하지만 후자는

$$D(ab)=D(a)b+(-1)^{\degree(a)}D(b)$$

이 된다. 이를 *anti-derivation*이라 부른다.

## 캘러 미분

