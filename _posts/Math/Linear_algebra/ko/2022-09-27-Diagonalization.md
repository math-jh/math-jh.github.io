---

title: "대각화"
excerpt: "행렬의 대각화"

categories: [Math / Linear Algebra]
permalink: /ko/math/linear_algebra/diagonalization
sidebar: 
    nav: "linear_algebra-ko"

header:
    overlay_image: /assets/images/Linear_algebra/Diagonalization.png
    overlay_filter: 0.5

date: 2022-09-27
last_modified_at: 2022-09-27

weight: 21

---

## 행렬의 대각화

우리는 앞서 임의의 $n\times n$ 행렬 $A$가 주어졌을 때, $A$의 고윳값과 고유공간을 통해 $\mathbb{R}^n$을 분해하는 방법을 살펴보았고, 해당 글의 [명제 5](/ko/math/linear_algebra/eigenspace_decomposition#pp5)으로부터 이러한 분해가 언제 가능한지 또한 알게 되었다. 

이를 증명하기 위해 사용했던 [명제 4](/ko/math/linear_algebra/eigenspace_decomposition#pp4)의 증명을 다시 한 번 살펴보자. 우리는 $E_\lambda$의 basis $x_1,\ldots, x_k$에 $n-k$개의 임의의 벡터를 추가한 후, 이를 통해 행렬 $X=(x\_1\|\cdots\|x\_n)$을 정의한 후 계산을 통해

$$XAX^{-1}=\begin{pmatrix}\lambda I_k&B\\0&C\end{pmatrix}$$

의 왼쪽 위 $k\times k$ block matrix가 대각행렬 $\lambda I_k$가 된다는 것을 보았다. 그런데 만일 $A$가 [명제 5](/ko/math/linear_algebra/eigenspace_decomposition#pp5)의 조건을 모두 만족한다면, $n-k$개의 벡터들 $x\_{k+1},\ldots, x_n$을 마구잡이로 추가할 것이 아니라, $n$개의 벡터들 $x_1,\ldots, x_n$이 모두 $A$의 고유공간의 basis가 되도록 잡을 수 있다. 그럼 [명제 4](/ko/math/linear_algebra/eigenspace_decomposition#pp4)의 증명 중

$$y_i\cdot x_j=\begin{cases}1&i=j\\0&i\neq j\end{cases}$$

으로부터 $C$도 대각행렬이 되고, $B$는 영행렬이 된다는 것을 알 수 있다. 따라서 다음이 성립한다.

<div class="proposition" markdown="1">

<ins id="pp1">**명제 1**</ins> 이전 글의 [명제 5](/ko/math/linear_algebra/eigenspace_decomposition#pp5)의 조건을 모두 만족하는 $n\times n$ 행렬 $A$를 생각하고, 고유공간들의 basis로 이루어진 $\mathbb{R}^n$의 basis를 잡아 이를 $x_1,\ldots, x_n$이라 하자. $Ax_i=\lambda_ix_i$라 하고, $X=(x\_1\|\cdots\|x\_n)$이라 하면, 대각행렬

$$D=\begin{pmatrix}\lambda_1&0&\cdots&0\\ 0&\lambda_2&\cdots&0\\ \vdots&\vdots&\ddots&\vdots\\0&0&\cdots&\lambda_n\end{pmatrix}$$

에 대하여 $A=XDX^{-1}$이 성립한다. 

</div>

따라서 이 조건을 만족하는 행렬 $A$에 그럴듯한 이름을 붙여줄 수 있다.

<div class="definition" markdown="1">

<ins id="df2">**정의 2**</ins> 이전 글의 [명제 5](/ko/math/linear_algebra/eigenspace_decomposition#pp5)의 조건을 모두 만족하는 $n\times n$ 행렬 $A$를 *diagonalizable<sub>대각화가능</sub>*이라 한다.

</div>

혹은, [명제 5](/ko/math/linear_algebra/eigenspace_decomposition#pp5)는 필요충분조건이었으므로, 대각행렬과 닮은 행렬을 diagonalizable matrix라 불러도 아무런 문제가 없다. 

<div class="notice--warning" markdown="1">
Primary decomposition theorem, Cayley-Hamilton, Jordan canonical form  
내적  
QR, LU, SVD  

분해정리끼리 묶기는 순서 애매; 일단 내적부터
아예 pairing 다음에 내적을 넣을 걸 그랬나? 생각해보니 괜찮은듯

</div>

