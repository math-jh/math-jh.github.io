---

title: "Hom과 텐서곱"
excerpt: ""

categories: [Math / Multilinear Algebra]
permalink: /ko/math/multilinear_algebra/hom_and_tensor
header:
    overlay_image: /assets/images/Math/Multilinear_Algebra/Hom_and_tensor.png
    overlay_filter: 0.5
sidebar: 
    nav: "multilinear_algebra-ko"

date: 2024-08-30
last_modified_at: 2024-09-23
weight: 5

---

이번 글에서 우리는 $\Hom$과 텐서곱 사이의 관계를 살펴본다. 

## Homomorphism $M^\ast\otimes_AN \rightarrow \Hom_{\rMod{A}}(M,N)$

편의상 $A$가 commutative ring이라 가정하자. 그럼 $\lMod{A}=\rMod{A}$이므로 임의의 $A$-module이 left $A$-module인지 right $A$-module인지 구별할 필요가 없다. 이러한 경우에는 아래첨자로 썼을 때의 미관상의 이유로 $\rMod{A}$를 표기법으로 고정하기로 한다. 이제 세 $A$-module $M,N,L$이 주어졌다 하자. 그럼 다음의 $A$-module homomorphism

$$\nu:\Hom_{\rMod{A}}(M,L)\otimes_A N \rightarrow\Hom_{\rMod{A}}(M,L\otimes_AN)$$

을 만들 수 있다. 더 일반적으로 $A,B$가 (commutative일 필요는 없는) ring이고, left $A$-module $M$, left $B$-module $N$, $(A,B)$-bimodule $L$가 주어졌다 하면 다음의 $\mathbb{Z}$-module homomorphism

$$\Hom_{\lMod{A}}(M,L)\otimes_AN \rightarrow \Hom_{\lMod{A}}(M, L\otimes_BN)$$

을 만들 수 있다. ([\[Bou\] II.4.2]()) 

이는 우선 임의의 $u\in\Hom_{\rMod{A}}(M,L)$와 임의의 $y\in N$에 대하여, 다음 식

$$x\mapsto u(x)\otimes_Ay$$

으로 $M$에서 $L\otimes_AN$으로의 $A$-linear map을 정의하고, 그럼 $(u,y)\in\Hom_{\rMod{A}}(M,L)\times N$의 원소를 받아 $\Hom_{\rMod{A}}(M, L\otimes_AB)$의 원소를 대응시키는 위의 함수가 $A$-balanced인 것을 알 수 있다. 따라서 이로부터 위의 $A$-linear map $\nu$가 유도된다. 

<div class="proposition" markdown="1">

<ins id="prop1">**명제 1**</ins> 위와 같이 정의된 $\nu$에 대하여, 다음이 성립한다.

1. 만일 $N$이 projective $A$-module이라면 $\nu$는 injective이다. 또, $N$이 finitely generated projective라면 $\nu$는 bijective이다.
2. 만일 $M$이 fintiely generated projective $A$-module이라면, $\nu$는 bijective이다.

</div>

특히 만일 $L=A$인 경우 다음의 따름정리를 얻는다.

<div class="proposition" markdown="1">

<ins id="cor2">**따름정리 2**</ins> 임의의 두 $A$-module $M,N$이 주어졌다 하자. 만일 $M$ 또는 $N$이 finitely generated projective $A$-module이라면, 다음의 isomorphism

$$M^\ast \otimes_AN\cong \Hom_{\rMod{A}}(M,N)$$

이 존재한다.

</div>

또, $N=\Hom_{\rMod{A}}(M', L')$로 두면 다음의 따름정리를 얻는다.

<div class="proposition" markdown="1">

<ins id="cor3">**따름정리 3**</ins> 다음의 $A$-linear map

$$\Hom_\rMod{A}(M,L)\otimes_A\Hom_\rMod{A}(M',L') \rightarrow \Hom_\rMod{A}(M\otimes M', L\otimes L')$$

이 존재하며, 이는 만일 다음의 쌍

$$(M,M'),\quad (M,L),\quad (M',L')$$

중 하나가 finitely generated projective $A$-module이라면 isomorphism이다.

</div>

## Trace

여전히 $A$가 commutative ring이라 가정한다. 그럼 임의의 $A$-module $M$에 대하여, 

$$M^\ast\times M \rightarrow A;\qquad (\xi,x) \mapsto \langle x, \xi\rangle$$

이 $A$-balanced인 것을 안다. 따라서 이 함수는 다음의 $A$-linear map

$$\tau: M^\ast\otimes_A M \rightarrow A$$

을 만족한다. 이제 만일 $M$이 finitely generated projective $A$-module이라면 [따름정리 2](#cor2)에 의하여 좌변을 $\End_\rMod{A}(M)=\Hom_\rMod{A}(M,M)$과 identify할 수 있고, 따라서 $\End_\rMod{A}(M)$에서 $A$로 가는 유일한 $A$-linear map이 정의된다.

<div class="definition" markdown="1">

<ins id="def4">**정의 4**</ins> 위와 같이 정의된 map을 *trace map*이라 하고, $\tr$로 표기한다.

</div>

임의의 $u\in\End_\rMod{A}(M)$이 주어졌다 가정하자. $\End_\rMod{A}(M)$과 $M^\ast\otimes_AM$을 identify하고 나면 유한히 많은 $\xi_i\in M^\ast, x_i\in M$을 택하여 이를 다음의 합

$$\sum_i \xi_i\otimes_A x_i\tag{1}$$

으로 쓸 수 있으며, 이 원소가 [따름정리 2](#cor2)에 의해 $u$에 대응된다는 것은 다음의 식

$$u(x)=\sum_i\langle x,\xi_i\rangle x_i\qquad\text{for all $x\in M$}\tag{2}$$

이 성립하는 것이다. 그럼 trace map의 정의에 의하여

$$\tr(u)=\sum_i\langle x_i,\xi_i\rangle$$

이 된다. 일반적으로 식 (2)를 만족하는 $\xi_i\in M^\ast, x_i\in M$의 쌍은 무수히 많을 수 있지만, 이는 $M^\ast\otimes_AM$의 원소를 식 (1)과 같이 나타내는 방법이 무수히 많기 때문이며, 어쨌든 $\tau:M^\ast\otimes_AM \rightarrow A$는 잘 정의되었으므로 $\tr$은 이러한 선택에 의존하지 않는다.

뿐만 아니라, $\tr$이 $A$-linear map인 것을 확인할 수 있으며 더 나아가 다음이 성립한다. 

<div class="proposition" markdown="1">

<ins id="prop5">**명제 5**</ins> 임의의 두 finitely generated projective $A$-module $M,N$과 이들 사이의 $A$-linear map $u:M \rightarrow N$, $v:N \rightarrow M$에 대하여

$$\tr(u\circ v)=\tr(v\circ u)$$

이 성립한다.

</div>

