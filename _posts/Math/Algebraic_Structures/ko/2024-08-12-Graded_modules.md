---

title: "등급가군"
excerpt: ""

categories: [Math / Algebraic Structures]
permalink: /ko/math/algebraic_structures/graded_modules
header:
    overlay_image: /assets/images/Math/Algebraic_Structures/Graded_modules.png
    overlay_filter: 0.5
sidebar: 
    nav: "algebraic_structures-ko"

date: 2024-08-12
last_modified_at: 2024-08-12
weight: 204

---

이제 우리는 graded module의 개념을 정의한다.

## 등급가군

<div class="definition" markdown="1">

<ins id="def1">**정의 1**</ins> Commutative monoid $I$에 대해, $A=\bigoplus_{i\in I}A_i$가 $I$-graded ring이라 하고, $M$이 left $A$-module이라 하자. 그럼 $M$이 *$I$-graded left $A$-module<sub>$I$-등급 왼쪽가군</sub>*이라는 것은 임의의 $i,j\in I$에 대하여 

$$A_iM_j\subseteq M_{i+j}$$

이 성립하는 것이다. 

</div>

비슷하게 $I$-graded right $A4-module 도한 정의한다. 특별히 $A$를 $A$ 자기 자신에 대한 left $A$-module로 본다면, [정의 1](#def1)에 의해 모든 graded ring은 자기 자신에 대한 graded (left) $A$-module이다. 만일 $I$의 덧셈에 대하여, 모든 원소가 cancellable이라면 [§등급환, ⁋명제 2](/ko/math/algebraic_structures/graded_rings#prop2)에 의하여 $A_0$은 ring이다. 그럼 위의 식으로부터 각각의 $M_j$들이 $A_0$-module이 되는 것이 자명하다. 

<div class="definition" markdown="1">

<ins id="def2">**정의 2**</ins> 두 $I$-graded left $A$-module $M,M'$에 대하여, $A$-linear map $f:M \rightarrow M'$이 *graded homomorphism*이라는 것은 $f(M_i)\subseteq M_i'$이 항상 성립하는 것이다.

</div>

이를 통해 $I$-graded left $A$-module들의 category $\gr_I\lMod{A}$를 정의할 수 있다. 더 일반적으로 다음을 정의한다. 

<div class="definition" markdown="1">

<ins id="def3">**정의 3**</ins>  두 $I$-graded left $A$-module $M,M'$에 대하여, $A$-linear map $f:M \rightarrow M'$이 *graded homomorphism of degree $i$*이라는 것은 $f(M_j)\subseteq M_{i+j}'$이 항상 성립하는 것이다.

</div>

그럼 [정의 2](#def2)의 graded homomorphism들은 모두 graded homomorphism of degree $0$에 불과하다. 만일 $I$의 모든 원소들이 cancellable이라면, 우리는 *graded homomorphism of degree $-i$*를 다음 조건

$$f(M_{i+j})\subseteq M_j',\qquad f(M_j)=0\text{ if $j-i\not\in I$}$$

으로 정의할 수도 있다. 다만 이러한 방식으로 정의할 때 주의할 점은 bijective graded homomorphism of degree $i$는 $i\neq 0$일 경우, 일반적으로 $I$-graded left $A$-module들 사이의 isomorphism으로 생각하지 않는다는 것이다. 

이러한 방식의 일반화는 호몰로지 대수학에서 더 자세히 다룬다.

## 등급부분가군

<div class="proposition" markdown="1">

<ins id="prop4">**명제 4**</ins> $I$-graded left $A$-module $M=\bigoplus_{i\in I} M_i$가 주어졌다 하자. 그럼 $M$의 submodule $N$에 대하여, 다음이 모두 동치이다.

1. $N$은 $N\cap M_i$들의 합이다.
2. $N$의 임의의 원소를 homogeneous element들로 분해하면, 각각의 원소들도 모두 $N$에 속한다. 
3. $N$은 homogeneous element들로 생성된다.

</div>

이 명제는 [§등급환, §명제 6](/ko/math/algebraic_structures/graded_rings#prop6)의 일반화이며, 그 증명 또한 동일하다. 이 동치조건을 만족하는 submodule들을 *graded submodule<sub>등급부분가군</sub>*이라 부른다. 다음 명제 또한 [§등급환, §명제 7](/ko/math/algebraic_structures/graded_rings#prop7)의 일반화이다.

<div class="proposition" markdown="1">

<ins id="prop5">**명제 5**</ins> Degree $d$의 graded $A$-homomorphism $f:M \rightarrow N$에 대하여, 다음이 성립한다.

1. $\im(f)$는 $N$의 graded submodule이다.
2. 만일 $d$가 cancellable이라면, $\ker(f)$는 $M$의 graded submodule이다.
3. $d=0$이라면 canonical bijection $M/\ker(f)\cong\im(f)$는 graded module들 사이의 isomorphism을 정의한다. 

</div>