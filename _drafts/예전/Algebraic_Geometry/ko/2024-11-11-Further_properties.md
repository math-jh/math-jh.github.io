---

title: "함수와 다양체의 성질들"
excerpt: ""

categories: [Math / Algebraic Geometry]
permalink: /ko/math/algebraic_geometry/further_properties
header:
    overlay_image: /assets/images/Math/Algebraic_Geometry/Further_properties.png
    overlay_filter: 0.5
sidebar: 
    nav: "algebraic_geometry-ko"

date: 2024-11-11
last_modified_at: 2024-11-11
weight: 5

---

## 유한사상

두 affine variety $f:X \rightarrow Y$가 주어졌다 하고 $f(X)$가 $Y$에서 dense라 하자. 그럼 이로부터 유도되는 pullback $f^\ast: \mathbb{k}[Y] \rightarrow \mathbb{k}[X]$가 injective이다. 이를 통해 $\mathbb{k}[Y]$를 $\mathbb{k}[X]$의 subring으로 생각할 수 있다. 

<div class="definition" markdown="1">

<ins id="def1">**정의 1**</ins> $\mathbb{k}[X]$가 $\mathbb{k}[Y]$에 대해 integral이라면 $f$를 *finite map<sub>유한사상</sub>*이라 부른다. 

</div>

용어를 정당화하기 위해, $X\subseteq \mathbb{A}^n$이라 하고 $\mathbb{A}^n$ 위에서 정의된 함수들 $\x_1,\ldots, \x_n$을 생각하자. 만일 $f$가 finite map이라면 각각의 $i$에 대하여, 다음의 식

$$\x_i^k+a_1\x_i^{k-1}+\cdots+a_k=0,\qquad a_i\in \mathbb{k}[Y]$$

가 성립한다. $\mathbb{k}[Y]$를 $\mathbb{k}[X]$의 subring으로 본 과정을 거꾸로 뒤집어보면, 이는 임의의 $y\in Y$와 $x\in f^{-1}(y)$에 대하여, 다음의 방정식

$$\x_i(x)^k+a_1(y)\x_i(x)^{k-1}+\cdots+a_k(y)=0$$

이 성립한다는 뜻이고, 이 방정식은 오직 유한히 많은 근만 가진다. 즉, 각각의 $y\in Y$가 주어졌을 때, $f^{-1}(y)$는 반드시 유한집합이어야 한다. 

Regular map $f:X \rightarrow Y$가 finite인 것은 local property다. 즉 다음이 성립한다.

<div class="proposition" markdown="1">

<ins id="thm2">**정리 2**</ins> Regular map $f:X \rightarrow Y$에 대하여, 임의의 $y\in Y$마다 적당한 affine neighborhood $V$가 존재하여 $U=f^{-1}(V)$가 affine이고 $f:U \rightarrow V$가 finite morphism이도록 할 수 있다 하자. 그럼 $f$는 finite morphism이다.

</div>
<details class="proof" markdown="1">
<summary>증명</summary>



</details>

따라서, 이를 바탕으로 quasiprojective variety들 사이의 finite morphism을 정의할 수 있다. 

<div class="definition" markdown="1">

<ins id="def3">**정의 3**</ins> 

</div>

