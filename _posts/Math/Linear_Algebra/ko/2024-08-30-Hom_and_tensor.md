---

title: "Hom과 텐서곱"
excerpt: ""

categories: [Math / Linear Algebra]
permalink: /ko/math/linear_algebra/hom_and_tensor
header:
    overlay_image: /assets/images/Math/Linear_Algebra/Hom_and_tensor.png
    overlay_filter: 0.5
sidebar: 
    nav: "linear_algebra-ko"

date: 2024-08-30
last_modified_at: 2024-08-30
weight: 104

---

이번 글에서 우리는 $\Hom$과 텐곱 사이의 관계를 살펴본다. 

## Homomorphism $M^\ast\otimes_AN \rightarrow \Hom_{\lMod{A}}(M,N)$

편의상 $A$가 commutative ring이라 가정하고, 세 $A$-module $M,N,L$이 주어졌다 하자. 그럼 다음의 $A$-module homomorphism

$$\nu:\Hom_{\lMod{A}}(M,L)\otimes_A N \rightarrow\Hom_{\lMod{A}}(M,L\otimes_AN)$$

을 만들 수 있다. 더 일반적으로 $A,B$가 (commutative일 필요는 없는) ring이고, left $A$-module $M$, left $B$-module $N$, $(A,B)$-bimodule $L$가 주어졌다 하면 다음의 $\mathbb{Z}$-module homomorphism

$$\Hom_{\lMod{A}}(M,L)\otimes_AN \rightarrow \Hom_{\lMod{A}}(M, L\otimes_BN)$$

을 만들 수 있다. ([\[Bou\] II.4.2]()) 

이는 우선 임의의 $f\in\Hom_{\lMod{A}}(M,L)$와 임의의 $y\in N$에 대하여, 다음 식

$$x\mapsto f(x)\otimes_Ay$$

으로 $M$에서 $L\otimes_AN$으로의 $A$-linear map을 정의하고, 그럼 $(f,y)\in\Hom_{\lMod{A}}(M,L)\times N$의 원소를 받아 $\Hom_{\lMod{A}}(M, L\otimes_AB)$의 원소를 대응시키는 위의 함수가 $A$-balanced인 것을 알 수 있다. 따라서 이로부터 위의 $A$-linear map $\nu$가 유도된다. 

<div class="proposition" markdown="1">

<ins id="prop1">**명제 1**</ins> 위와 같이 정의된 $\nu$에 대하여, 다음이 성립한다.

1. 만일 $N$이 projective $A$-module이라면 $\nu$는 injective이다. 또, $N$이 finitely generated projective라면 $\nu$는 bijective이다.
2. 만일 $M$이 fintiely generated projective $A$-module이라면, $\nu$는 bijective이다.

</div>

특히 만일 $L=A$인 경우 다음의 따름정리를 얻는다.

<div class="proposition" markdown="1">

<ins id="cor2">**따름정리 2**</ins> 임의의 두 $A$-module $M,N$이 주어졌다 하자. 만일 $M$ 또는 $N$이 finitely generated projective $A$-module이라면, 다음의 isomorphism

$$M^\ast \otimes_AN\cong \Hom_{\lMod{A}}(M,N)$$

이 존재한다.

</div>

또, $N=\Hom_{\lMod{A}}(M', L')$로 두면 다음의 따름정리를 얻는다.

<div class="proposition" markdown="1">

<ins id="cor3">**따름정리 3**</ins> 다음의 $A$-linear map

$$\Hom_\lMod{A}(M,L)\otimes_A\Hom_\lMod{A}(M',L') \rightarrow \Hom_\lMod{A}(M\otimes M', L\otimes L')$$

이 존재하며, 이는 만일 다음의 쌍

$$(M,M'),\quad (M,L),\quad (M',L')$$

중 하나가 finitely generated projective $A$-module이라면 isomorphism이다.

</div>

## Trace

여전히 $A$가 commutative ring이라 가정한다. 그럼 임의의 $A$-module $M$에 대하여, 

$$M^\ast\times M \rightarrow A;\qquad (\xi,x) \mapsto \langle x, \xi\rangle$$

이 $A$-balanced인 것을 안다. 따라서 이 함수는 다음의 $A$-linear map

$$\tau: M^\ast\otimes_A M \rightarrow A$$

을 만족한다. 이제 만일 $M$이 finitely generated projective $A$-module이라면 [따름정리 2](#cor2)에 의하여 좌변을 $\End_\lMod{A}(M)=\Hom_\lMod{A}(M,M)$과 identify할 수 있고, 따라서 $\End_\lMod{A}(M)$에서 $A$로 가는 유일한 $A$-linear map이 정의된다.

<div class="definition" markdown="1">

<ins id="def4">**정의 4**</ins> 위와 같이 정의된 map을 *trace map*이라 하고, $\tr$로 표기한다.

</div>

임의의 $u\in\End_\lMod{A}(M)$이 주어졌다 가정하자. $\End_\lMod{A}(M)$과 $M^\ast\otimes_AM$을 identify하고 나면 유한히 많은 $\xi_i\in M^\ast, x_i\in M$을 택하여 이를 다음의 합

$$\sum_i \xi_i\otimes_A x_i$$

으로 쓸 수 있으며, 이 때 이 isomorphism이 어떻게 정의되었는지를 생각하면, 위의 합으로부터 $u$를 다음의 식

$$u(x)=\sum_i\langle x,\xi\rangle x_i\qquad\text{for all $x\in M$}$$

으로 쓸 수 있다. 그럼 이 표현 하에서

$$\tr(u)=\sum_i\langle x_i,\xi_i\rangle$$

이다. 그럼 $\tr$이 $A$-linear map인 것을 확인할 수 있다. 또, 다음이 성립한다.

<div class="proposition" markdown="1">

<ins id="prop5">**명제 5**</ins> 임의의 두 finitely generated projective $A$-module $M,N$과 이들 사이의 $A$-linear map $f:M \rightarrow N$, $g:N \rightarrow M$에 대하여

$$\tr(f\circ g)=\tr(g\circ f)$$

이 성립한다.

</div>

