---

title: "특성다항식"
excerpt: "행렬의 특성다항식"

categories: [Math / Linear Algebra]
permalink: /ko/math/linear_algebra/characteristic_polynomial
sidebar: 
    nav: "linear_algebra-ko"

header:
    overlay_image: /assets/images/Linear_algebra/Characteristic_polynomial.png
    overlay_filter: 0.5

date: 2022-08-28
last_modified_at: 2022-08-29

weight: 19

---

이제 우리는 행렬과 선형사상의 특성다항식을 살펴보고, 이를 통해 고유값을 정의한다. 

<div class="definition" markdown="1">

<ins id="df1">**정의 1**</ins> 임의의 $n$차 정사각행렬 $A$에 대하여, $A$의 *특성다항식<sub>characteristic polynomial</sub>*을 $\mathrm{x}$에 대한 다항식 $\det(\mathrm{x}I-A)$으로 정의한다.

</div>

다음의 식

$$\det(\mathrm{x}I-A)=\sum_{\sigma\in S_n}\operatorname{sgn}(\sigma)(\mathrm{x}I-A)_{\sigma(1),1}\cdots(\mathrm{x}I-A)_{\sigma(n),n}\tag{1}$$

으로부터, $A$의 특성다항식의 차수는 많아봐야 $n$차라는 것을 알 수 있다. 우변에서 더해지는 다항식은 $n$개 항들의 곱인데, 이 때 각 $(\mathrm{x}I-A)\_{\sigma(k),k}$는 $\sigma(k)=k$일 때에만 $x$에 대한 일차식이고, 그렇지 않으면 상수이기 때문이다. 이로부터 만일 특성다항식이 실제로 $n$차식이라면, 차수 $n$의 항은 <em_ko>반드시</em_ko> 모든 $k$에 대해 $\sigma(k)=k$를 만족하는 $\sigma$, 즉 $\sigma=\operatorname{id}\_{S\_n}$일 때에만 나타난다는 것을 안다. 이 때, 해당하는 항은

$$(\mathrm{x}I-A)_{1,1}\cdots(\mathrm{x}I-A)_{n,n}=(\mathrm{x}-A_{11})\cdots(\mathrm{x}-A_{nn})\tag{2}$$

이 되며, 이를 전개하면 $\mathrm{x}$의 계수는 $1$이므로 특성다항식의 차수는 항상 $n$이라는 것을 알 수 있다. 

만일 $\sigma(i)\neq i$인 $i$가 하나 존재한다면, 비둘기집 원리에 의해 반드시 또 다른 $j$에 대하여 $\sigma(j)\neq j$가 성립한다. 이로부터 식 (1)의 우변에서 더해지는 항들에는 $n-1$차식이 존재하지 않음을 안다. 즉, 특성다항식의 $n-1$차 항은 반드시 식 (2)에 의해서만 생기고, 이 때의 계수는 

$$-(A_{1,1}+\cdots+A_{n,n})$$

임을 알 수 있다.

마지막으로 특성다항식의 상수항을 구해보자. 이를 위해서는 특성다항식에 $\mathrm{x}=0$을 대입하면 된다. 그럼 그 결과는

$$\det(0I-A)=\det(-A)=(-1)^n\det(A)$$

이 된다. 

따라서 다음 명제를 증명하였다.

<div class="proposition" markdown="1">

<ins id="pp2">**명제 2**</ins> $n$차 정사각행렬의 특성다항식은 반드시 $n$차다항식이며, 특성다항식의 $n-1$차항의 계수는 $-\operatorname{tr}A$와 같고, 상수항은 $(-1)^n\det A$와 같다.

</div>

특성다항식의 해는 행렬을 살펴볼 때 중요한 정보가 된다.

<div class="definition" markdown="1">

<ins id="df3">**정의 3**</ins> $n\times n$ 행렬 $A$에 대하여, $A$의 특성다항식 $\det(\mathrm{x}I-A)=0$의 해를 $A$의 *고유값<sub>eigenvalue</sub>*이라 부른다.

</div>

