---

title: "가우스 소거법"
excerpt: "가우스 소거법과 역행렬"

categories: [Math / Linear Algebra]
permalink: /ko/math/linear_algebra/Gaussian_elimination
sidebar: 
    nav: "linear_algebra-ko"

header:
    overlay_image: /assets/images/Linear_algebra/Gaussian_elimination.png
    overlay_filter: 0.5

date: 2022-08-19
last_modified_at: 2022-08-19

weight: 9

---

다음의 일차연립방정식

$$\begin{aligned}a_{11}x_{1}+a_{12}x_2+\cdots+a_{1n}x_n&=c_1\\a_{21}x_1+a_{22}x_2+\cdots+a_{2n}x_n&=c_2\\\hspace{10pt}\vdots&\\a_{mn}x_1+a_{m2}x_2+\cdots+a_{mn}x_n&=c_m\end{aligned}$$

이 주어졌다 하자. 이전 글에서 정의한 행렬의 곱에 의하여 위의 식은 다음의 행렬들

$$A=\begin{pmatrix}a_{11}&a_{12}&\cdots&a_{1n}\\a_{21}&a_{22}&\cdots&a_{2n}\\\vdots&\vdots&\ddots&\vdots\\a_{m1}&a_{m2}&\cdots&a_{mn}\end{pmatrix},\quad x=\begin{pmatrix}x_1\\x_2\\\vdots\\x_n\end{pmatrix},\quad c=\begin{pmatrix}c_1\\c_2\\\vdots\\c_m\end{pmatrix}$$

에 대하여 $Ax=c$으로 쓸 수 있다. 만일 $m=n$이고, 행렬 $A$의 역행렬이 존재한다면 이 연립방정식의 해는 다음의 식

$$x=A^{-1}c$$

을 통해 유일하게 결정된다. 만일 $m\neq n$이거나 혹은 $A$의 역행렬이 존재하지 않으면 위의 일차연립방정식의 해는 존재하지 않을 수도 있고, 무한히 많을 수도 있다. 우리는 이 경우에도 유용하게 사용할 수 있는 *가우스 소거법*을 살펴본다.