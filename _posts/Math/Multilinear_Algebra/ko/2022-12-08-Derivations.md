---

title: "미분 (작성중)"
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

우리는 이제 미분의 개념을 도입한다. 가장 일반적인 정의는 언제나와 같이 [Bou]에 있지만, 이는 약간 과도한 측면이 있어 더 간단한 형태로 줄이기로 한다.

Commutative ring $A$를 고정하고, unital associative $A$-algebra $E$를 고정하자. 

<div class="definition" markdown="1">

<ins id="def1">**정의 1**</ins> $E$-module $M$을 고정하자. 그럼 $E$에서 $M$으로의 *$E$-derivation<sub>$E$-미분</sub>*은 식

$$d(x+x')=dx+dx',\qquad d(xx')=xdx'+x'dx$$

를 만족하는 $E \rightarrow M$을 의미한다. 만일 추가로 다음의 식

$$d(a\cdot 1_E)=0\qquad\text{for all $a\in A$}$$

이 성립한다면 이를 *$A$-derivation*이라 부른다. 

</div>

