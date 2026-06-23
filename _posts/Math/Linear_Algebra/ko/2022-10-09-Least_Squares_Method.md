---
title: "최소제곱법"
description: "유클리드 공간과 내적공간에서 최소제곱법을 정규방정식으로 유도하고, 평면 위 점들의 직선 적합 예시와 유사역행렬까지 다룬다."
excerpt: "정사영과 최소제곱법"

categories: [Math / Linear Algebra]
permalink: /ko/math/linear_algebra/least_squares_method
sidebar: 
    nav: "linear_algebra-ko"


date: 2022-10-09

weight: 119

published: false
drift_needed: true

---

## 최소제곱법

지금 소개할 최소제곱법은 우선 유클리드 공간 $$\mathbb{R}^n$$들과 이 위에 주어진 dot product에 대해서 생각한다. 그러나 [§쌍선형형식, §§비퇴화 쌍선형형식](/ko/math/linear_algebra/bilinear_form#비퇴화-쌍선형형식)에서 했던 것과 동일한 방식으로 이를 일반적인 $$\mathbb{R}$$-내적공간으로 일반화할 수 있다.

임의의 행렬 $$A\in\Mat_{m\times n}(\mathbb{R})$$과 연립일차방정식 $$Ax=y$$를 생각하자. 만일 $$m=n$$이고 $$A$$가 가역이라면 이 방정식은 유일한 해를 갖지만, 일반적인 경우는 그렇지 않다. 특별히 $$m>n$$인 경우를 생각하자. 그럼 $$\rank(A)\leq n< m$$이므로, $$A$$의 image에 해당하는 벡터들을 제외한 대부분의 $$y$$에 대해서는 이 방정식을 풀 수 없다. 

대표적인 예시는 다양한 데이터가 주어졌을 때, 이를 표현하는 적당한 함수를 찾는 것이다. 물론 라그랑주 보간법을 이용하면 적절한 basis를 잡아 주어진 $$n+1$$개의 데이터를 근사하는 $$n$$차 함수를 찾을 수 있지만, 가령 이 데이터를 표현하는 일차함수를 찾으려 한다면 주어진 $$n+1$$개의 점이 모두 일직선 상에 존재하지 않는 한 정확한 해를 찾을 수는 없을 것이다.

우리는 임의의 주어진 벡터 $$y$$를 $$\im A$$로 사영한 후, 이 벡터 $$\hat y=\proj_{\im(A)}y$$에 대해 방정식 $$Ax=\hat y$$를 풀 것이다. 그런데 앞선 글에서 우리는 $$y-\hat y\in (\im A)^\perp$$임을 알고 있으므로

$$\langle y-\hat y, v\rangle=0\qquad\text{for all $v\in \im A$}$$

임을 안다. 따라서 다음의 식

$$\langle y-\hat y, Au\rangle=0\qquad\text{for all $u\in \mathbb{R}^n$}$$

을 얻는다. 이제 $$A$$를 왼쪽으로 넘겨주면

$$\langle A^t(y-\hat y), u\rangle=0\qquad\text{for all $u\in\mathbb{R}^n$}$$

이고, $$\langle-,-\rangle$$이 non-degenerate인 것으로부터 $$A^t(y-\hat y)=0$$임을 안다. 이제 $$\hat y=Ax$$이므로, 우리는 방정식

$$A^tAx=A^ty$$

을 얻는다. 이 과정을 요약하면 다음과 같다.

<div class="proposition" markdown="1">

<ins id="prop1">**명제 1**</ins> 임의의 행렬 $$A\in\Mat_{m\times n}(\mathbb{R})$$과 $$y\in\mathbb{R}^m$$에 대하여, 벡터 $$x\in\mathbb{R}^n$$이 실수 $$\lVert Au-y\rVert$$의 값을 최소로 하는 것은 다음 방정식

$$A^tAx=A^ty$$

이 성립하는 것과 동치이다.

</div>

도입부에서 다룬 예시는 다음과 같은 방식으로 풀 수 있다.

<div class="example" markdown="1">

<ins id="ex2">**예시 2**</ins> 평면 위의 세 점 $$(0,1)$$, $$(1,3)$$, $$(2,4)$$가 주어졌다 하고, 이들을 가장 잘 적합하는 직선 $$y=ax+b$$를 찾는 문제를 생각하자. 세 점이 모두 한 직선 위에 있다면 미지수 $$a,b$$에 대한 연립방정식

$$\begin{aligned}a\cdot 0+b&=1\\ a\cdot 1+b&=3\\ a\cdot 2+b&=4\end{aligned}$$

가 해를 가져야 하지만, 세 점이 일직선 위에 있지 않으므로 정확한 해는 존재하지 않는다. 이 연립방정식을 $$Ax=y$$의 꼴로 적으면

$$A=\begin{pmatrix}0&1\\ 1&1\\ 2&1\end{pmatrix},\qquad x=\begin{pmatrix}a\\ b\end{pmatrix},\qquad y=\begin{pmatrix}1\\ 3\\ 4\end{pmatrix}$$

이며, $$A$$의 첫째 열은 각 점의 $$x$$좌표를, 둘째 열은 상수 $$1$$을 담는다. [명제 1](#prop1)에 따라, $$\lVert Ax-y\rVert$$을 최소로 하는 $$(a,b)$$는 normal equation

$$A^tAx=A^ty$$

의 해로 주어진다. 직접 계산하면

$$A^tA=\begin{pmatrix}5&3\\ 3&3\end{pmatrix},\qquad A^ty=\begin{pmatrix}11\\ 8\end{pmatrix}$$

이고, $$\det(A^tA)=5\cdot 3-3\cdot 3=6\neq 0$$이므로 $$A^tA$$는 가역이다. 따라서

$$\begin{pmatrix}a\\ b\end{pmatrix}=(A^tA)^{-1}A^ty=\frac{1}{6}\begin{pmatrix}3&-3\\ -3&5\end{pmatrix}\begin{pmatrix}11\\ 8\end{pmatrix}=\frac{1}{6}\begin{pmatrix}9\\ 7\end{pmatrix}=\begin{pmatrix}3/2\\ 7/6\end{pmatrix}$$

을 얻는다. 즉, 주어진 세 점을 최소제곱의 의미에서 가장 잘 표현하는 직선은 $$y=\frac{3}{2}x+\frac{7}{6}$$이다.

![linear least squares fit](/assets/images/Math/Linear_Algebra/Least_Squares_Method-1.svg){:style="width:11.95em" class="invert" .align-center}

</div>

더 일반적으로, 내적 $$\langle-,-\rangle$$을 dot product 대신 함수들의 공간에서의 $$L^2$$-내적 등으로 택하여도 이와 비슷한 예시를 반복할 수 있다. 

[예시 2](#ex2)에서 본질적으로 쓰인 것은 구하려는 함수가 미지의 계수들에 대해 일차라는 사실 뿐이다. 즉 사용하려는 모델이 미리 고른 함수들 $$f_1,\ldots, f_k$$의 일차결합 $$c_1f_1+\cdots+c_kf_k$$의 꼴이기만 하면, $$(i,j)$$ 성분이 $$i$$번째 데이터점에서의 $$f_j$$의 값인 행렬 $$A$$를 세우고 같은 normal equation을 풀어 계수 $$c_j$$를 얻을 수 있다. 특별히 [예시 2](#ex2)는 $$f_1(t)=t$$, $$f_2(t)=1$$인 경우였으며, 같은 방법이 일반적인 다항함수의 경우에도 그대로 적용된다. 

<div class="example" markdown="1">

<ins id="ex3">**예시 3**</ins> 평면 위의 네 점 $$(-2,5)$$, $$(-1,2)$$, $$(1,1)$$, $$(2,4)$$를 가장 잘 표현하는 이차함수 $$y=a\x^2+b\x+c$$를 찾는 문제를 생각하자. 각 점에서 $$(\x^2,\x,1)$$의 값을 행으로 쌓으면 

$$A=\begin{pmatrix}4&-2&1\\ 1&-1&1\\ 1&1&1\\ 4&2&1\end{pmatrix},\qquad x=\begin{pmatrix}a\\ b\\ c\end{pmatrix},\qquad y=\begin{pmatrix}5\\ 2\\ 1\\ 4\end{pmatrix}$$

이다. 직접 계산하면

$$A^tA=\begin{pmatrix}34&0&10\\ 0&10&0\\ 10&0&4\end{pmatrix},\qquad A^ty=\begin{pmatrix}39\\ -3\\ 12\end{pmatrix}$$

이다. 둘째 행은 분리되어 $$10b=-3$$, 즉 $$b=-\frac{3}{10}$$을 곧바로 주고, 나머지 두 미지수는 

$$\begin{pmatrix}34&10\\ 10&4\end{pmatrix}\begin{pmatrix}a\\ c\end{pmatrix}=\begin{pmatrix}39\\ 12\end{pmatrix}$$

을 푼다. 이 계수행렬의 행렬식은 $$34\cdot 4-10\cdot 10=36$$이므로 가역이고, 풀면 $$a=1$$, $$c=\frac{1}{2}$$을 얻는다. 따라서 최소제곱의 의미에서 이들 네 점을 가장 잘 표현하는 포물선은 $$y=\x^2-\frac{3}{10}\x+\frac{1}{2}$$이다.

![quadratic least squares fit](/assets/images/Math/Linear_Algebra/Least_Squares_Method-2.svg){:style="width:19.74em" class="invert" .align-center}

</div>

[명제 1](#prop1)의 유도과정을 돌이켜보면, least-squares solution $$x$$가 만드는 $$Ax$$는 $$y$$를 $$\im A$$로 정사영한 벡터 $$\proj_{\im A}y$$와 정확히 같았으며, 이것이 애초에 방정식 $$A^tAx=A^ty$$을 이끌어낸 출발점이었다. 즉 근사값 $$\hat y=Ax$$는 $$y$$에서 $$\im A$$로 내린 수선의 발이고, 오차 $$y-\hat y$$는 $$\im A$$에 수직이다. 특히 $$A$$가 full column rank여서 $$A^tA$$이 가역이라면 $$x=(A^tA)^{-1}A^ty$$이므로 근사값은 

$$\hat y=A(A^tA)^{-1}A^ty$$

로 주어진다. 여기서 등장한 행렬 $$P=A(A^tA)^{-1}A^t$$은 $$\im A$$로의 정사영을 나타낸다. 

<div class="example" markdown="1">

<ins id="ex4">**예시 4**</ins> [예시 2](#ex2)로 돌아가 근사함수와의 오차를 직접 구해보자. $$x=(\tfrac{3}{2},\tfrac{7}{6})$$이었으므로 

$$\hat y=Ax=\begin{pmatrix}0&1\\ 1&1\\ 2&1\end{pmatrix}\begin{pmatrix}3/2\\ 7/6\end{pmatrix}=\begin{pmatrix}7/6\\ 8/3\\ 25/6\end{pmatrix}$$

이고, 따라서 오차는 

$$y-\hat y=\begin{pmatrix}1\\ 3\\ 4\end{pmatrix}-\begin{pmatrix}7/6\\ 8/3\\ 25/6\end{pmatrix}=\begin{pmatrix}-1/6\\ 1/3\\ -1/6\end{pmatrix}$$

이다. 이 오차를 $$A$$의 두 열 $$(0,1,2)$$와 $$(1,1,1)$$ 각각과 내적하면 

$$0\cdot\left(-\tfrac{1}{6}\right)+1\cdot\tfrac{1}{3}+2\cdot\left(-\tfrac{1}{6}\right)=0,\qquad -\tfrac{1}{6}+\tfrac{1}{3}-\tfrac{1}{6}=0$$

이 되어 오차가 $$\im A$$에 수직임을 확인할 수 있다. 이 때, 오차는 $$\lVert y-\hat y\rVert^2=\frac{1}{36}(1+4+1)=\frac{1}{6}$$이며, 이는 주어진 세 점이 한 직선 위에 있지 않은 정도를 정량적으로 나타낸다. 

</div>

## 유사역행렬

이번에는 반대로 행렬 $$A\in\Mat_{m\times n}(\mathbb{R})$$에서 $$m< n$$인 경우를 생각한다. 

우선 임의의 $$A\in\Mat_{m\times n}(\mathbb{R})$$과 $$y\in\im(A)$$가 주어졌다 하고, $$A$$가 단사가 아니라 하자. 그럼 $$Au=0$$을 만족하는 영이 아닌 벡터 $$u$$들이 존재하며, 따라서 $$Ax=y$$를 만족하는 벡터 $$x$$가 하나 주어진다면, $$x+u$$들 또한 해가 된다는 것을 알 수 있다. 이제 이들 중 가장 작은 norm을 갖는 해를 찾아 이를 *최소노름해<sub>minimum-norm solution</sub>*라 부르자. 즉, $$Ax=y$$의 해 전체는 한 특수해 $$x_0$$에 대하여 $$x_0+\ker A$$의 꼴을 이루며, 우리는 이 affine 부분공간 위에서 norm을 최소로 만드는 점을 찾는다.

이는 [§내적공간, ⁋정리 9](/ko/math/linear_algebra/inner_product_spaces#thm9)의 projection theorem이 다루는 상황과 정확히 같다. 원점에서 affine 부분공간 $$x_0+\ker A$$까지의 거리를 최소로 만드는 점은 유일하며, 이 점에서 affine 부분공간으로 그은 벡터는 $$\ker A$$에 수직이다. 따라서 최소노름해는 $$(\ker A)^\perp$$에 놓인 유일한 해이다. 한편 [§쌍선형형식, ⁋명제 5](/ko/math/linear_algebra/bilinear_form#prop5)에 의하여 $$(\ker A)^\perp=\im A^t$$이 성립한다. 이를 정리하면 다음과 같다.

<div class="proposition" markdown="1">

<ins id="prop5">**명제 5**</ins> 임의의 행렬 $$A\in\Mat_{m\times n}(\mathbb{R})$$과 $$y\in\im A$$에 대하여, 방정식 $$Ax=y$$의 해들 중 norm을 최소로 하는 해는 유일하게 존재하며, 이는 $$\im A^t$$에 속하는 유일한 해이다.

</div>
<details class="proof" markdown="1">
<summary>증명</summary>

$$y\in\im A$$이므로 $$Ax_0=y$$를 만족하는 $$x_0$$이 존재하고, $$Ax=y$$의 해 전체는 $$x_0+\ker A$$와 같다. [§쌍선형형식, ⁋명제 5](/ko/math/linear_algebra/bilinear_form#prop5)에 의하여

$$\mathbb{R}^n=\ker A\oplus(\ker A)^\perp$$

이 성립하므로, $$x_0$$을 $$x_0=p+q$$로 분해할 수 있다. 여기서 $$p\in (\ker A)^\perp$$이고 $$q\in\ker A$$이다. 그럼 $$p=x_0-q$$ 또한 $$Ax=y$$의 해이고, 임의의 해 $$x=p+u$$ (단 $$u\in\ker A$$)에 대하여 $$p\perp u$$이므로 피타고라스 정리에 의해

$$\lVert x\rVert^2=\lVert p\rVert^2+\lVert u\rVert^2\geq \lVert p\rVert^2$$

이 성립한다. 등호는 $$u=0$$, 즉 $$x=p$$일 때만 성립하므로 norm을 최소로 하는 해는 $$p$$로 유일하다. 또한 같은 명제에 의하여 $$(\ker A)^\perp=\im A^t$$이므로 $$p\in\im A^t$$이다.

</details>

이제 이 최소노름해를 명시적으로 구할 수 있는 경우를 생각하자. $$A$$가 *full row rank*, 즉 $$\rank A=m$$인 경우에는 $$\im A=\mathbb{R}^m$$이므로 모든 $$y\in\mathbb{R}^m$$에 대하여 $$Ax=y$$가 해를 가지며, 위 명제에 따라 최소노름해는 $$\im A^t$$ 위에서 유일하게 결정된다.

<div class="proposition" markdown="1">

<ins id="prop6">**명제 6**</ins> 행렬 $$A\in\Mat_{m\times n}(\mathbb{R})$$이 $$\rank A=m$$을 만족한다면 $$AA^t\in\Mat_m(\mathbb{R})$$은 가역이며, 임의의 $$y\in\mathbb{R}^m$$에 대하여 방정식 $$Ax=y$$의 최소노름해는

$$x=A^t(AA^t)^{-1}y$$

로 주어진다.

</div>
<details class="proof" markdown="1">
<summary>증명</summary>

먼저 $$AA^t$$가 가역임을 보인다. $$AA^t$$는 $$m\times m$$ 정사각행렬이므로 $$AA^tz=0$$이 $$z=0$$만을 해로 가짐을 보이면 충분하다. $$AA^tz=0$$이라 하면

$$\lVert A^tz\rVert^2=\langle A^tz, A^tz\rangle=\langle z, AA^tz\rangle=0$$

이므로 $$A^tz=0$$, 즉 $$z\in\ker A^t$$이다. 그런데 $$\rank A^t=\rank A=m$$이므로 $$A^t$$은 단사이고, 따라서 $$z=0$$이다. 이로써 $$AA^t$$이 가역임을 안다.

이제 $$x=A^t(AA^t)^{-1}y$$로 놓으면

$$Ax=AA^t(AA^t)^{-1}y=y$$

이므로 $$x$$는 $$Ax=y$$의 해이다. 뿐만 아니라 $$x=A^t\big((AA^t)^{-1}y\big)\in\im A^t$$이므로, [명제 5](#prop5)에 의하여 $$x$$는 최소노름해이다.

</details>

증명에서 보았듯이, 최소노름해가 $$\im A^t$$ 위에 있다는 사실로부터 $$x=A^tz$$의 꼴을 가정하고 이를 $$Ax=y$$에 대입하여 $$AA^tz=y$$를 풀면 $$z=(AA^t)^{-1}y$$를 얻는다. 이때 $$A^t(AA^t)^{-1}$$은 $$A$$의 *오른쪽 역행렬*, 즉 $$A\cdot A^t(AA^t)^{-1}=I_m$$을 만족하는 행렬이 된다.

앞 절에서 다룬 최소제곱의 경우와 이 절에서 다룬 최소노름의 경우는 서로 쌍대적인 상황으로 볼 수 있다. $$A$$가 *full column rank*, 즉 $$\rank A=n$$인 경우 $$A^tA$$이 가역이 되어 [명제 1](#prop1)의 normal equation이 유일한 최소제곱해 $$x=(A^tA)^{-1}A^ty$$를 주며, 이때 $$(A^tA)^{-1}A^t$$은 $$A$$의 왼쪽 역행렬이 된다. 반면 $$A$$가 full row rank인 경우에는 위와 같이 오른쪽 역행렬 $$A^t(AA^t)^{-1}$$이 최소노름해를 준다. 이 두 행렬을 통합하는 것이 다음의 개념이다.

<div class="definition" markdown="1">

<ins id="def7">**정의 7**</ins> 행렬 $$A\in\Mat_{m\times n}(\mathbb{R})$$에 대하여, 만일 $$A$$가 full column rank라면

$$A^\dagger:=(A^tA)^{-1}A^t$$

으로, full row rank라면

$$A^\dagger:=A^t(AA^t)^{-1}$$

으로 정의되는 행렬 $$A^\dagger\in\Mat_{n\times m}(\mathbb{R})$$을 $$A$$의 *유사역행렬<sub>Moore-Penrose pseudoinverse</sub>*이라 부른다.

</div>

위 두 식은 $$A$$의 rank에 대한 가정이 없는 일반적인 상황에서는 그대로 쓸 수 없는데, $$A^tA$$이나 $$AA^t$$ 중 적어도 하나가 가역이 아니기 때문이다. 일반적인 행렬에 대한 유사역행렬은 singular value decomposition을 이용하여 정의되며, $$A$$가 위 두 경우에 해당할 때에는 그 정의가 위의 식과 일치한다. 이때 $$A^\dagger$$은 다음 네 조건

$$AA^\dagger A=A,\quad A^\dagger AA^\dagger=A^\dagger,\quad (AA^\dagger)^t=AA^\dagger,\quad (A^\dagger A)^t=A^\dagger A$$

으로 유일하게 특징지어진다는 것이 알려져 있으며, 이를 통해 $$A^\dagger$$이 $$A$$에 의해 잘 정의됨을 확인할 수 있다.

<div class="remark" markdown="1">

<ins id="rmk8">**참고 8**</ins> $$A$$가 가역인 정사각행렬이라면 $$A^\dagger=A^{-1}$$이 성립한다. 이는 $$A^tA$$과 $$AA^t$$이 모두 가역이어서 $$A^\dagger=(A^tA)^{-1}A^t=A^{-1}(A^t)^{-1}A^t=A^{-1}$$이 되기 때문이다. 이러한 의미에서 유사역행렬은 역행렬의 개념을 일반화한다.

</div>

유사역행렬을 도입하면 앞 절의 최소제곱과 이 절의 최소노름이 하나의 공식으로 통합된다. $$A$$가 full column rank인 경우 $$x=A^\dagger y=(A^tA)^{-1}A^ty$$는 $$\lVert Ax-y\rVert$$을 최소로 하는 유일한 최소제곱해이고, $$A$$가 full row rank인 경우 $$x=A^\dagger y=A^t(AA^t)^{-1}y$$는 $$Ax=y$$의 최소노름해이다. 일반적인 행렬에 대해서도 $$x=A^\dagger y$$는 $$\lVert Ax-y\rVert$$을 최소로 하는 해들 중 다시 norm이 최소인 유일한 해를 주며, 이로써 두 절에서 따로 다룬 문제가 유사역행렬이라는 하나의 대상으로 자연스럽게 통합된다.
