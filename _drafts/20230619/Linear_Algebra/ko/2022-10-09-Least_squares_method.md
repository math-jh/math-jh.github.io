---

title: "최소제곱법 (작성중)"
excerpt: "정사영과 최소제곱법"

categories: [Math / Linear Algebra]
permalink: /ko/math/linear_algebra/least_squares_method
sidebar: 
    nav: "linear_algebra-ko"

header:
    overlay_image: /assets/images/Math/Linear_Algebra/Least_squares_method.png
    overlay_filter: 0.5

date: 2022-10-09
last_modified_at: 2022-10-09

weight: 18

---

## 최소제곱법

지금 소개할 최소제곱법은 우선 유클리드 공간 $\mathbb{R}^n$들과 이 위에 주어진 dot product에 대해서 생각한다. 그러나 [§쌍선형형식, §§비퇴화 쌍선형형식](/ko/math/linear_algebra/bilinear_form#비퇴화-쌍선형형식)에서 했던 것과 동일한 방식으로 이를 일반적인 $\mathbb{R}$-내적공간으로 일반화할 수 있다.

임의의 행렬 $A\in\Mat_{m\times n}(\mathbb{R})$과 연립일차방정식 $Ax=y$를 생각하자. 만일 $m=n$이고 $A$가 가역이라면 이 방정식은 유일한 해를 갖지만, 일반적인 경우는 그렇지 않다. 특별히 $m>n$인 경우를 생각하자. 그럼 $\rank(A)\leq n< m$이므로, $A$의 image에 해당하는 벡터들을 제외한 대부분의 $y$에 대해서는 이 방정식을 풀 수 없다. 

대표적인 예시는 다양한 데이터가 주어졌을 때, 이를 표현하는 적당한 함수를 찾는 것이다. 물론 라그랑주 보간법을 이용하면 적절한 basis를 잡아 주어진 $n+1$개의 데이터를 근사하는 $n$차 함수를 찾을 수 있지만, 가령 이 데이터를 표현하는 일차함수를 찾으려 한다면 주어진 $n+1$개의 점이 모두 일직선 상에 존재하지 않는 한 정확한 해를 찾을 수는 없을 것이다.

우리는 임의의 주어진 벡터 $y$를 $\im A$로 사영한 후, 이 벡터 $y'=\proj\_{\im(A)}y$에 대해 방정식 $Ax=y'$를 풀 것이다. 그런데 앞선 글에서 우리는 $y-y'\in (\im A)^\perp$임을 알고 있으므로

$$\langle y-y', v\rangle=0\qquad\text{for all $v\in \im A$}$$

임을 안다. 따라서 다음의 식

$$\langle y-y', Au\rangle=0\qquad\text{for all $u\in \mathbb{R}^n$}$$

을 얻는다. 이제 $A$를 왼쪽으로 넘겨주면

$$\langle A^t(y-y'), u\rangle=0\qquad\text{for all $u\in\mathbb{R}^n$}$$

이고, $\langle-,-\rangle$이 non-degenerate인 것으로부터 $A^t(y-y')=0$임을 안다. 이제 $y'=Ax$이므로, 우리는 방정식

$$A^tAx=A^ty$$

을 얻는다. 이 과정을 요약하면 다음과 같다.

<div class="proposition" markdown="1">

<ins id="pp1">**명제 1**</ins> 임의의 행렬 $A\in\Mat_{m\times n}(\mathbb{R})$과 $y\in\mathbb{R}^m$에 대하여, 벡터 $x\in\mathbb{R}^n$이 실수 $\lVert Au-y\rVert$의 값을 최소로 하는 것은 다음 방정식

$$A^tAx=A^ty$$

이 성립하는 것과 동치이다.

</div>

도입부에서 다룬 예시는 다음과 같은 방식으로 풀 수 있다.

<div class="example" markdown="1">

<ins id="ex2">**예시 2**</ins> 

</div>

더 일반적으로, 내적 $\langle-,-\rangle$을 dot product 대신 함수들의 공간에서의 $L^2$-내적 등으로 택하여도 이와 비슷한 예시를 반복할 수 있다. 

## 유사역행렬

이번에는 반대로 행렬 $A\in\Mat_{m\times n}(\mathbb{R})$에서 $m< n$인 경우를 생각한다. 

우선 임의의 $A\in\Mat_{m\times n}(\mathbb{R})$과 $y\in\im(A)$가 주어졌다 하고, $A$가 단사가 아니라 하자. 그럼 $Au=0$을 만족하는 영이 아닌 벡터 $u$들이 존재하며, 따라서 $Ax=y$를 만족하는 벡터 $x$가 하나 주어진다면, $x+u$들 또한 해가 된다는 것을 알 수 있다. 이제 이들 중 가장 작은 norm을 갖는 해를 찾아 이를 *minimum-norm solution*이라 부르자. 