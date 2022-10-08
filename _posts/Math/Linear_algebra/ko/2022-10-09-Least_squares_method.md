---

title: "최소제곱법"
excerpt: "정사영과 최소제곱법"

categories: [Math / Linear Algebra]
permalink: /ko/math/linear_algebra/least_squares_method
sidebar: 
    nav: "linear_algebra-ko"

header:
    overlay_image: /assets/images/Linear_algebra/Least_squares_method.png
    overlay_filter: 0.5

date: 2022-10-09
last_modified_at: 2022-10-09

weight: 18

---

임의의 행렬 $A\in\operatorname{Mat}_{m\times n}(\mathbb{R})$에 대하여, 방정식 $Ax=y$를 생각하자. 만일 $m=n$이고 $A$가 가역이라면 이 방정식은 유일한 해를 갖지만, 일반적인 경우는 그렇지 않다. 특별히 $m>n$인 경우를 생각하자. 그럼 $\operatorname{rank}(A)\leq n< m$이므로, $A$의 image에 해당하는 벡터들을 제외한 대부분의 $y$에 대해서는 이 방정식을 풀 수 없다. 

그러나 