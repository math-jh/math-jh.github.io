---

title: "사영가군, 단사가군, 평탄가군"
excerpt: ""

categories: [Math / Linear Algebra]
permalink: /ko/math/linear_algebra/various_modules
header:
    overlay_image: /assets/images/Math/Linear_Algebra/Various_modules.png
    overlay_filter: 0.5
sidebar: 
    nav: "linear_algebra-ko"

date: 2024-08-21
last_modified_at: 2024-09-23
weight: 2

---

[\[대수적 구조\]](/ko/algebraic_structures/)에서 우리는 임의의 ring $A$ 위에 정의된 $A$-module을 정의하고, 이에 대한 기본적인 성질들을 살펴보았다. 이제 우리는 (left) $A$-module들에 대한 성질을 더 살펴본다.

## 핵과 여핵

임의의 $A$-linear map $f:M \rightarrow N$에 대하여, $f$가 injective인 것은 $\ker f=0$인 것과 동치이고, $f$가 surjective인 것은 $\coker f=0$인 것과 동치이다. 한편, category $\lMod{A}$는 bicomplete category이며, 이 때 $A$-module들의 family의 product는 direct product로, coproduct는 direct sum으로 주어졌다. ([\[대수적 구조\] §가군의 직접곱과 직합, 텐서곱, ⁋정리 1](/ko/math/algebraic_structures/operations_of_modules#thm1)) 따라서 [\[범주론\] §극한, ⁋명제 10](/ko/math/category_theory/limits#prop10)에 의하여 다음 식

$$\ker \prod f_i=\prod \ker f_i,\qquad \coker \bigoplus f_i=\bigoplus \coker f_i $$

이 성립하며, 위의 논의를 통해  [\[대수적 구조\] §가군의 직접곱과 직합, 텐서곱, ⁋명제 2](/ko/math/algebraic_structures/operations_of_modules#prop2)를 다시 써보면 다음의 두 식

$$\ker \bigoplus f_i=\bigoplus \ker f_i,\qquad \coker \prod f_i=\prod \coker f_i$$

또한 얻게 된다. 

비슷한 맥락에서 $\Hom$ functor와 $\otimes$ functor에 대한 성질을 다시 살펴볼 수 있으며, 여기에서 $\Hom$과 $\otimes$의 adjoint를 사용하게 된다. ([\[대수적 구조\] §가군의 직접곱과 직합, 텐서곱, ⁋정리 6](/ko/math/algebraic_structures/operations_of_modules#thm6)과 [\[대수적 구조\] §가군의 직접곱과 직합, 텐서곱, ⁋정리 9](/ko/math/algebraic_structures/operations_of_modules#thm9))

## 직접곱과 직합

위의 adjunction을 사용하는 법을 살펴보기 위해 가장 기초적인 예시를 생각한다. 우선 $\Hom$과 $\bigoplus$, $\prod$의 관계를 살펴보자. 이를 위해 left $A$-module $M,N$과 left $A$-module들의 family $(M\_i)\_{i\in I}$, $(N\_j)\_{j\in J}$를 고정한다. 그럼 $\Hom$은 right adjoint이므로 limit을 보존한다. ([\[범주론\] §수반함자, ⁋정리 9](/ko/math/category_theory/adjoints#thm9)) 따라서 [\[범주론\] §극한, ⁋명제 10](/ko/math/category_theory/limits#prop10)에 의하여 abelian group들 사이의 isomorphism

$$\Hom_{\lMod{A}}\left(M, \prod_{j\in J} N_j \right)\cong\prod_{j\in J} \Hom_{\lMod{A}}(M, N_j),\qquad \Hom_{\lMod{A}}\left(\bigoplus_{i\in I} M_i, N\right)\cong\prod_{i\in I}\Hom_{\lMod{A}}(M_i, N)$$

를 얻는다. 다시 여기에 [\[범주론\] §극한, ⁋명제 10](/ko/math/category_theory/limits#prop10)을 적용하면 다음 식

$$\Hom_{\lMod{A}}\left(\bigoplus_{i\in I} M_i, \prod_{j\in J} N_j\right)\cong\prod_{(i,j)\in I\times J}\Hom_{\lMod{A}}(M_i, N_j)\tag{1}$$

을 얻는다. 

비슷하게 $\otimes$와 $\bigoplus$의 관계를 살펴보자. 이번에는 right $A$-module $M$, right $A$-module들의 family $(M\_i)\_{i\in I}$, left $A$-module $N$, left $A$-module들의 family $(N\_j)\_{j\in J}$를 생각한다. 그럼 $\otimes$는 colimit을 보존하므로 abelian group isomorphism

$$M\otimes_A \left(\bigoplus_{j\in J}N_j\right)\cong\bigoplus_{j\in J} (M\otimes_AN_j),\qquad \left(\bigoplus_{i\in I} M_i\right)\otimes_A N\cong \bigoplus_{i\in I} M_i\otimes_AN)$$

그리고 이들을 종합하여

$$\left(\bigoplus_{i\in I} M_i\right)\otimes_A\left(\bigoplus_{j\in J} N_j\right)\cong\bigoplus_{(i,j)\in I\times J}M_i\otimes_AN_j$$

을 얻는다. 만일 $A$가 commutative ring이었다면, [\[대수적 구조\] §가군의 직접곱과 직합, 텐서곱, ⁋정리 6](/ko/math/algebraic_structures/operations_of_modules#thm6) 대신 [\[대수적 구조\] §가군의 직접곱과 직합, 텐서곱, ⁋정리 9](/ko/math/algebraic_structures/operations_of_modules#thm9)을 사용하여 위의 isomorphism들이 $A$-module들 사이의 isomorphism이 되도록 할 수 있다.

## 사영가군과 단사가군

이번에는 임의의 $A$-linear map $f:M \rightarrow M'$와 $A$-module $N$이 주어졌다 하자. 그럼 다음의 abelian group homomorphism

$$\Hom_{\lMod{A}}(f,N):\Hom_{\lMod{A}}(M', N) \rightarrow \Hom_{\lMod{A}}(M,N)$$

에 대하여, 그런데 $\Hom$은 right adjoint이므로

$$\ker(\Hom_{\lMod{A}}(f,N))\cong\Hom_{\lMod{A}}(\coker f, N)\tag{2}$$

이 성립한다. 비슷하게 다음의 abelian group homomorphism

$$\Hom_{\lMod{A}}(N, f):\Hom_{\lMod{A}}(M, N) \rightarrow\Hom_{\lMod{A}}(M', N)$$

에 대해서는 

$$\ker(\Hom_{\lMod{A}}(N, f))\cong\Hom_{\lMod{A}}(N, \ker f)\tag{3}$$

이 성립한다. 따라서 다음이 성립한다. 

<div class="proposition" markdown="1">

<ins id="prop1">**명제 1**</ins> $A$-linear map $f:M \rightarrow M'$이 주어졌다 하자.

1. $f$가 injective인 것은 임의의 $A$-module $N$에 대하여 $\Hom(N, f)$가 injective인 것과 동치이다.
2. $f$가 surjective인 것은 임의의 $A$-module $N$에 대하여 $\Hom(f, N)$이 injective인 것과 동치이다.

</div>

그러나 일반적으로, $f$가 surjective이더라도 $\Hom(f, N)$이 surjective는 아닐 수도 있고, $f$가 injective이더라도 $\Hom(N, f)$가 surjective는 아닐 수도 있다. 

한편 $\lMod{A}$는 abelian category이므로, 식 (2)의 isomorphism은 본질적으로 다음의 short exact sequence

$$M_1 \rightarrow M_2 \rightarrow M_3 \rightarrow 0$$

가 주어졌을 때, 여기에 (contravariant) additive functor $\Hom_{\lMod{A}}(-, N):\lMod{A} \rightarrow\lMod{\mathbb{Z}}$를 취해 얻어지는 다음의 sequence

$$0 \rightarrow \Hom_\lMod{A}(M_3, N) \rightarrow \Hom_\lMod{A}(M_2, N)\rightarrow\Hom_\lMod{A}(M_1,A)$$

가 exact라는 것과 같은 말이다. 비슷하게 식 (3)의 isomorphism은 다음의 short exact sequence

$$0 \rightarrow M_1 \rightarrow M_2 \rightarrow M_3$$

가 주어졌을 때, 여기에 additive functor $\Hom_\lMod{A}(N,-):\lMod{A} \rightarrow \lMod{\mathbb{Z}}$를 취하여 얻어지는 다음의 sequence

$$0 \rightarrow \Hom_\lMod{A}(N, M_1)\rightarrow\Hom_\lMod{A}(N, M_2) \rightarrow\Hom_\lMod{A}(N, M_3)$$

가 exact라는 것과 같은 말이다. 즉 다음이 성립한다.

<div class="proposition" markdown="1">

<ins id="prop2">**명제 2**</ins> 임의의 $N\in\lMod{A}$에 대하여, $\Hom_\lMod{A}(-,N)$과 $\Hom_\lMod{A}(N,-)$은 left exact functor이다.

</div>

그러나 일반적으로 $\Hom_\lMod{A}(-,N)$과 $\Hom_{\lMod{A}}(N,-)$이 right exact가 될 필요는 없다. 이러한 조건을 만족하는 $A$-module들을 다음과 같이 정의한다.

<div class="definition" markdown="1">

<ins id="def3">**정의 3**</ins> 다음을 정의한다.

1. 만일 $\Hom(-, I)$가 right exact라면 $I$를 *injective module<sub>단사가군</sub>*이라 부른다. 
2. 만일 $\Hom(P, -)$가 right exact라면 $P$를 *projective module<sub>사영가군</sub>*이라 부른다. 

</div>

그럼 식 (1)로부터 module들의 direct product가 injective인 것과 각각의 성분이 injective인 것이 동치인 것을 알고, module들의 direct sum이 projective인 것은 각각의 direct summand가 projective인 것과 동치임을 안다. 특히 다음의 homomorphism

$$\Hom(A, f):\Hom_{\lMod{A}}(A, M) \rightarrow \Hom_{\lMod{A}}(A, M')$$

이 isomorphism이라는 사실로부터 $A$ 자기 자신은 projective임을 알고, 따라서 임의의 free module은 projective module이다. 

<div class="proposition" markdown="1">

<ins id="prop4">**명제 4**</ins> Left $A$-module가 projective인 것과 $P$가 free $A$-module의 direct summand인 것이 동치이다.

</div>
<details class="proof" markdown="1">
<summary>증명</summary>

임의의 free module의 direct summand가 projective라는 것은 위의 논증으로부터 자명하다. 따라서 $P$가 projective라 가정하자. [§기저, ⁋명제 2](/ko/math/linear_algebra/basis#prop2)에 의하여 적당한 free $A$-module $F$와 surjection $\pi:F \rightarrow P$를 택할 수 있다. 한편 $P$가 projective라는 것은 다음의 함수

$$\Hom_{\lMod{A}}(P, \pi):\Hom_{\lMod{A}}(P,F) \rightarrow \Hom_{\lMod{A}}(P,P)$$

가 surjective라는 것이므로, 적당한 $i\in \Hom_{\lMod{A}}(P,F)$가 존재하여 

$$\id_P=\Hom_{\lMod{A}}(P,\pi)(i)=\pi\circ i$$

이도록 할 수 있다. 이 식으로부터 $i$는 injective이므로 $P$와 $\im i$를 같은 것으로 볼 수 있고, 그럼 $F\cong\ker\pi\oplus\im i$인 것을 확인할 수 있다.

</details>

## 평탄가군

이번에는 right $A$-module $M$과 left $A$-module들 사이의 $A$-linear map $g:N \rightarrow N'$이 주어졌다 하자. 그럼 다음의 abelian group homomorphism

$$M\otimes_A g:M\otimes_AN \rightarrow M\otimes_AN'$$

이 존재한다. 그럼 $\otimes$는 left adjoint이므로 colimit을 보존하고, 따라서 다음 abelian group들 사이의 isomorphism

$$\coker(M\otimes_Ag)\cong M\otimes_A(\coker g)$$

이 존재한다. 비슷하게 right $A$-module들 사이의 $A$-linear map $f:M \rightarrow M'$과 고정된 left $A$-module $N$에 대하여 다음의 isomorphism

$$\coker(f\otimes_AN)\cong (\coker f)\otimes_A N$$

이 존재한다. 

<div class="proposition" markdown="1">

<ins id="prop5">**명제 5**</ins> 다음이 성립한다.

1. Right $A$-module들 사이의 linear map $f:M \rightarrow M'$이 surjective인 것은 임의의 left $A$-module $N$에 대하여, $f\otimes_A N$이 surjective인 것과 동치이다.
2. Left $A$-module들 사이의 linear map $g:N \rightarrow N'$이 surjective인 것은 임의의 right $A$-module $M$에 대하여, $M\otimes_A f$이 surjective인 것과 동치이다.

</div>

그럼 앞서 했던 것과 마찬가지로, 위의 성질은 right $A$-module들의 exact sequence

$$M_1 \rightarrow M_2 \rightarrow M_3 \rightarrow 0$$

가 주어졌을 때, 임의의 left $A$-module $N$에 대해

$$M_1\otimes_AN \rightarrow M_2\otimes_AN \rightarrow M_3\otimes_AN \rightarrow 0$$

도 exact라는 것으로 쓸 수 있다. 마찬가지로 left $A$-module들의 exact sequence

$$N_1 \rightarrow N_2 \rightarrow N_3 \rightarrow 0$$

가 주어졌을 때, 임의의 right $A$-module $M$에 대하여

$$M\otimes_AN_1 \rightarrow M\otimes_AN_2 \rightarrow M\otimes_AN_3 \rightarrow 0$$

또한 exact가 된다. 즉 다음이 성립한다.

<div class="proposition" markdown="1">

<ins id="prop6">**명제 6**</ins> 임의의 $M\in\rMod{A}$, $N\in \lMod{A}$에 대하여, $-\otimes_AN$과 $M\otimes_A-$는 각각 right exact functor이다.

</div>

그럼 [정의 3](#def3)과 비슷한 맥락에서 다음을 정의할 수 있다.


<div class="definition" markdown="1">

<ins id="def7">**정의 7**</ins> Left $A$-module $N$이 *flat module<sub>평탄가군</sub>*이라는 것은 임의의 right $A$-module들 사이의 injective $A$-linear map $f:M \rightarrow M'$에 대하여, $f\otimes_A N$이 injective인 것이다. 비슷하게 flat right $A$-module을 정의할 수 있다. 

</div>

임의의 free module은 flat이다. 또, module들의 direct sum이 flat인 것과 각각의 summand가 flat인 것이 동치임이 자명하다. 따라서 [명제 4](#prop4)에 의하여 projective module은 항상 flat이다. 그러나 그 역이 항상 성립하는 것은 아니다.