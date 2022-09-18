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

이제 우리는 행렬과 선형사상의 특성다항식을 살펴보고, 이를 통해 고윳값을 정의한다. 

## 특성다항식과 고윳값

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

<ins id="df3">**정의 3**</ins> $n\times n$ 행렬 $A$에 대하여, $A$의 특성다항식 $\det(\mathrm{x}I-A)=0$의 해를 $A$의 *고윳값<sub>eigenvalue</sub>*이라 부른다.

</div>

두 닮은 $n\times n$ 행렬 $A,B$를 생각하자. 그럼 $A=PBP^{-1}$로부터, 

$$\det(\mathrm{x}I-A)=\det(\mathrm{x}I-PBP^{-1})=\det(P(\mathrm{x}I-B)P^{-1})=\det P\det(\mathrm{x}I-B)\det P^{-1}=\det(\mathrm{x}I-B)$$

를 얻는다. 따라서 $A$와 $B$의 특성다항식은 서로 같다. 이로부터 다음의 따름정리들을 얻는다.

<div class="proposition" markdown="1">

<ins id="crl4">**따름정리 4**</ins> 임의의 linear map $L:V\rightarrow V$에 대하여, $L$의 특성다항식을 <phrase>행렬 $[L]_\mathcal{B}^\mathcal{B}$의 특성다항식</phrase>으로 정의한 것이 잘 정의된다.

</div>
<details class="proof" markdown="1">
<summary>증명</summary>

즉, $V$의 basis $\mathcal{B}$ 대신 $\mathcal{C}$를 택하여도 $L$의 특성다항식에는 변화가 없다는 것을 보여야 한다. 앞선 논증에 의하여, 이는 [§기저변환, 정의 2]로부터 두 행렬표현 $[L]\_\mathcal{B}^\mathcal{B}$와 $[L]\_\mathcal{C}^\mathcal{C}$가 서로 닮은 행렬이라는 것을 관찰하는 것으로 충분하다.

</details>

편의상 앞으로의 논의는 모두 행렬에 대한 것으로 통일하지만, 위의 따름정리를 통해 우리는 똑같은 내용을 임의의 linear map $L$에 대하여도 증명할 수 있다.

<div class="proposition" markdown="1">

<ins id="crl5">**따름정리 5**</ins> 서로 닮은 행렬의 trace와 행렬식은 같다. 

</div>
<details class="proof" markdown="1">
<summary>증명</summary>

앞선 논증으로부터 $A$와 $B$는 같은 특성다항식을 갖는다는 것을 알고, [명제 2](#pp2)로부터 행렬의 trace와 행렬식은 특성다항식으로부터 결정된다. 

</details>

## 대수적 중복도

고윳값들은 모두 특성다항식의 해지만, 어떤 고윳값들은 다른 고윳값보다 더 큰 중복도를 가질 수 있다. 이는 다음과 같이 정의된다.

<div class="definition" markdown="1">

<ins id="df6">**정의 6**</ins> $F[\mathrm{x}]$의 임의의 다항식 $p(\mathrm{x})$이 주어졌다 하고, $a\in F$가 $p(\mathrm{x})=0$의 해라 하자. 만일 $(\mathrm{x}-a)^k$가 $p(\mathrm{x})$를 나누지만, $(\mathrm{x}-a)^{k+1}$은 $p(\mathrm{x})$를 나누지 않는다면 $a$의 *중복도<sub>multiplicity</sub>*를 $k$로 정의한다. 

</div>

$n\times n$ 행렬 $A$의 특성다항식을 $p_A(\mathrm{x})$라 하고, $\lambda$가 $A$의 한 고윳값이라 하자. 그럼 $p_A$의 해로서의 $\lambda$의 중복도를 $\lambda$의 *대수적 중복도<sub>algebraic multiplicity</sub>*라 부른다. 이는 곧 정의할 *기하적 중복도*와 구분하기 위한 용어이다. 

$F[\mathrm{x}]$의 임의의 원소 $p(\mathrm{x})$가 주어졌다 하자. $p$가 $n$차식이라 하면, $p$는 많아야 $n$개의 해를 가진다. 그러나 $p$가 정확히 $n$개의 해를 가져야만 하는 것은 아니다.

<div class="example" markdown="1">

<ins id="ex7">**예시 7**</ins> 예를 들어, $F=\mathbb{R}$이라 하고, $2\times 2$ 정사각행렬

$$J=\begin{pmatrix}0&-1\\1&0\end{pmatrix}$$

을 생각하자. 그럼 $J$의 특성다항식은 $\mathrm{x}^2+1$이며, 이 다항식은 $\mathbb{R}$에서 해를 갖지 않는다. 

</div>

이와 같은 일이 일어나지 않는 field를 *algebraically closed field<sub>대수적으로 닫힌 체</sub>*라 부른다. 다음 *대수학의 기본정리*는 대수적으로 증명할 수도 있고, 해석학을 통해 증명할 수도 있지만 어떠한 방식도 우리의 현재 수준에선 어렵기 때문에 사실로 받아들이고 넘어간다.

<div class="proposition" markdown="1">

<ins id="thm8">**정리 8 (대수학의 기본정리)**</ins> 복소수 집합 $\mathbb{C}$는 algebraically closed field이다.

</div>

따라서 위의 [예시 7](#ex7)의 행렬 $J$는 $\mathbb{R}$에서는 해를 갖지 않지만, $\mathbb{C}$에서는 두 개의 해를 갖는다. 앞으로도 이와 같이 다항식의 해가 어떠한 field 위에서 정의되었는지를 구분하는 것이 중요하다. 

## 고유벡터와 기하적 중복도

$n\times n$ 행렬 $A$와 그 고윳값 $\lambda$를 생각하자. 그럼 정의에 의해 행렬 $\lambda I-A$가 singular이고, 따라서 

$$(\lambda I-A)v=0$$

을 만족하는 영이 아닌 벡터 $v$가 존재한다.

<div class="definition" markdown="1">

<ins id="df9">**정의 9**</ins> $n\times n$ 행렬 $A$와 고윳값 $\lambda$에 대하여, $Av=\lambda v$를 만족하는 벡터 $v$를 $\lambda$에 해당하는 $A$의 *고유벡터<sub>eigenvector</sub>*라 부른다. 

</div>

행렬 $A$에 대하여, $\lambda$에 해당하는 고유벡터들을 모두 모아 그 집합을 $E_\lambda$라 하자. 그럼 $E_\lambda$가 벡터공간을 이룬다는 것을 쉽게 확인할 수 있다. 이를 $\lambda$에 해당하는 *고유공간<sub>eigenspace</sub>*이라 부른다. $E_\lambda$는 항상 영이 아닌 벡터를 적어도 하나 포함하므로, $\dim E\_\lambda$는 항상 $0$보다 크다. 

<div class="definition" markdown="1">

<ins id="df10">**정의 10**</ins> $n\times n$ 행렬 $A$와 고윳값 $\lambda$에 대하여, $E\_\lambda$의 차원 $\dim E\_\lambda$를 $\lambda$의 *기하적 중복도<sub>geometric multiplicity</sub>*라 부른다. 

</div>



---

**참고문헌**

**[Goc]** M.S. Gockenbach, *Finite-dimensional linear algebra*, Discrete Mathematics and its applications, Taylor&Francis, 2011.

---
