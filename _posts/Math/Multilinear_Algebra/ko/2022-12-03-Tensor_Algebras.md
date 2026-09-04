---
title: "텐서대수"
description: "행렬식 정의에 필요한 텐서대수의 개념과 보편 성질을 정리하고, 직접 합과 스칼라 확장에서의 연산 거동을 살펴본다."
excerpt: "텐서대수, 대칭대수, 외대수"

categories: [Math / Multilinear Algebra]
permalink: /ko/math/multilinear_algebra/tensor_algebras
sidebar: 
    nav: "multilinear_algebra-ko"

date: 2022-12-03
weight: 10

---

이제 우리는 행렬식을 정의할 것인데, 이를 위해 우선 tensor algebra와 symmetric algebra, exterior algebra를 정의한다. 이 과정에서 $A$는 항상 commutative ring인 것으로 생각한다. 그럼 특히 $A$는 IBN property를 갖는다. ([§기저, ⁋명제 6](/ko/math/multilinear_algebra/basis_of_free_modules#prop6))

## 텐서대수의 정의

우리는 임의의 $A$-module $M$에 대하여, $M$에 의해 정의되는 free algebra $F(M)$을 다음의 식

$$F(M)=\bigoplus_{n\geq 0} M^{\otimes n}$$

으로 정의했었다. ([\[대수적 구조\] §대수, ⁋명제 4](/ko/math/algebraic_structures/algebras#prop4)) 이는 단순한 algebra일 뿐 아니라, 자연스럽게 $\mathbb{N}_{\geq 0}$-graded associative unital algebra의 구조를 갖는다. 이를 다음과 같이 이름붙인다.

::: 정의 1
위에서 정의한 $F(M)$을 $M$의 *tensor algebra<sub>텐서대수</sub>*라 부르고, $\T(M)$으로 표기한다. 
:::

이들 각각의 성분 $M^{\otimes n}$을 $\T^n(M)$으로 표기하기로 한다. 그럼 $\T^1(M)=M$이므로, $M$에서 $\T(M)$으로의 canonical injection $\iota: M \rightarrow \T(M)$이 존재한다. 

이제 adjoint $T\dashv U$를 생각하면, $\iota$는 다음 adjunction

$$\Hom_{\Alg{A}}(\T(M), \T(M))\cong \Hom_{\rMod{A}}(M, U\T(M))$$

에 의한 $\id_{\T(M)}$의 image이고, $\T(M)$을 $\mathbb{N}$-graded associative unital algebra로 보면 좌변을 적절한 category로 바꿔주면 된다. 이 adjoint를 universal property로 풀어쓰면 다음과 같다.  

::: 명제 2
임의의 $A$-algebra $E$와 $A$-linear map $u:M \rightarrow E$가 주어졌다 하자. 그럼 유일한 $A$-algebra homomorphism $g: \T(M) \rightarrow E$가 존재하여 $u=g \circ\iota$이도록 할 수 있다. 

추가로, 만일 $E$가 $\mathbb{N}$-graded $A$-algebra이고, $u(M)\subseteq E_1$이 성립한다면 위에서 얻어지는 $A$-algebra homomorphism $g$는 $\mathbb{N}$-graded $A$-algebra homomorphism이 된다.
:::

만일 $A$-module $N$과 surjective $A$-linear map $u:M \rightarrow N$이 주어졌다면, $\T(N)$이 $\T^1(N)$으로 생성되는 것으로부터 $\T(u): \T(M) \rightarrow \T(N)$이 surjective가 되는 것을 안다. 

## 텐서대수의 성질들

이제 우리는 $\rMod{A}$에서의 연산들이 functor $T:\rMod{A} \rightarrow \Alg{A}$를 통해 옮겨졌을 때, 이들이 어떻게 행동하는지를 살펴본다. 특히 direct sum과 extension of scalar에 관심이 있다. 이 절의 논의는 [명제 2](#prop2)와 같이, $T$를 $\rMod{A}$에서 associative unital $\mathbb{N}$-graded $A$-algebra들의 category들로 가는 functor로 이해하여도 동일한 논증이 성립하지만, 표기상의 복잡함을 해소하기 위해 target category를 $\Alg{A}$로 적기로 한다. 

우선 direct sum의 경우를 살펴본다. $M=\bigoplus_{i\in I} M_i$가 $A$-module들 $M_i$들의 direct sum이라 하자. 그럼 $\otimes$가 $\Hom$의 left adjoint라는 사실과 약간의 귀납법을 통해 다음의 isomorphism

$$\bigoplus_{(i_1,\ldots, i_n)\in I^n}M_{i_1}\otimes\cdots\otimes M_{i_n}\cong \T^n(M)$$

을 얻고, 그럼 $\T(M)$은 이들의 direct sum

$$\T(M)\cong\bigoplus_{n\geq 0} \T^n(M)\cong\bigoplus_{n\geq 0}\bigoplus_{(i_1,\ldots, i_n)\in I^n}M_{i_1}\otimes\cdots\otimes M_{i_n}$$

으로 주어진다. 이는 식으로는 복잡해보이지만, 기본적으로는 $T$가 left adjoint이므로 

$$T\left(\bigoplus_{i\in I} M_i\right)\cong \coprod_{i\in I} \T(M_i)$$

로부터, 우변의 graded algebra들의 coproduct를 풀어쓴 것에 불과하다.[^1]

특별히 임의의 free $A$-module $M$에 대하여, $M$의 basis를 $\mathcal{B}=(e_i)_{i\in I}$라 하자. 그럼 

$$M=\bigoplus_{i\in I} Ae_i$$

이며, 위의 설명을 적용하면 다음 명제를 얻는다.

::: 명제 3
위와 같은 상황에서, $\T(M)$은 다음의 꼴

$$e_s=e_{i_1}\otimes\cdots\otimes e_{i_n},\qquad\text{$s$ a finite sequence $(i_1,i_2,\ldots,i_n)$ in $I$}$$

들의 원소 $e_s$를 basis로 갖는다.
:::

이는 $\T^n(M)$ 각각이 길이 $n$짜리 유한한 수열 $s$를 사용해 정의한 $e_s$들을 basis로 갖고, 이들의 direct sum이 $\T(M)$이기 때문이다. 한편 우리는 [§기저, ⁋정의 9](/ko/math/multilinear_algebra/basis_of_free_modules#def9)의 structure constant를 사용하면 $\T(M)$의 곱셈을 서술할 수 있다는 것을 알고 있는데, 위의 설명에 따르면 이는 다른 것이 아니라 단순히 수열을 이어쓰기하여 얻어지는 것이다. 즉 두 수열

$$s=(i_1,\ldots, i_m),\qquad t=(j_1,\ldots, j_n)$$

에 대하여, $st$를 다음의 수열

$$st=(i_1,\ldots, i_m,j_1,\ldots, j_n)$$

으로 정의하면 structure constant를 정의하는 식은 다음의 식

$$e_se_t=e_{st}$$

이 된다. 

Extension of scalar의 경우, ring homomorphism $\phi: A \rightarrow B$가 주어졌다 하고, $M$이 $A$-module이라 하자. 그럼 extension of scalar $\phi_!: \rMod{A} \rightarrow\rMod{B}$와 두 functor $\T_A: \rMod{A} \rightarrow \Alg{A}$, $\T_B:\rMod{B} \rightarrow \Alg{B}$가 존재하며, 자명한 방식으로 $\phi_!:\Alg{A} \rightarrow\Alg{B}$ 또한 정의된다. 이를 통해 다음의 (graded) $B$-linear map

{% diagram Math/Multilinear_Algebra/Tensor_Algebras-1.svg width="17.93em" alt="extension_of_scalars" %}

을 얻는다. 

::: 명제 4
위에서 얻어지는 $B$-linear map $\T_{B}(B\otimes_AM)\rightarrow B\otimes_A\T_A(M)$은 isomorphism이다.
:::
::: 증명
역함수를 만들면 충분하다. 이를 위해, 우선 adjoint

$$\Hom_\rMod{B}(\phi_!M,\phi_!M)\cong\Hom_\rMod{A}(M, \phi^\ast \phi_!M)$$

로부터 $\id_{\phi_!M}$에 해당하는 $A$-linear map $i: M \rightarrow \phi^\ast\phi_!M$을 얻자. ([\[대수적 구조\] §스칼라의 변환, ⁋명제 6](/ko/math/algebraic_structures/change_of_base_ring#prop6)) 그 후, $A$-module $\phi^\ast\phi_!M$을 $B$-module $\phi_!M$으로 본 후 

$$\iota_{\phi_!M}: \phi_!M \rightarrow \T_B(\phi_!M)$$

을 생각하면 이는 $A$-module $M$에서 $A$-module $\phi^\ast \T_B(\phi_!M)$ (더 정확히는 $U\phi^\ast \T_B(\phi_!M)$)으로의 $A$-linear map이다. 따라서 [명제 2](#prop2)에 의하여 다음의 diagram

{% diagram Math/Multilinear_Algebra/Tensor_Algebras-2.svg width="10.30em" alt="Extension_of_scalar_proof" %}

을 commute하도록 하는 $A$-algebra homomorphism $T_A(M)\rightarrow \phi^\ast T_{B}(\phi_!M)$이 유일하게 존재한다. 이제 다음의 adjoint

$$\Hom_{\Alg{A}}(\T_A(M), \phi^\ast \T_B(\phi_!M))\cong \Hom_\Alg{B}(\phi_! \T_A(M), \T_B(\phi_!M))$$

에 의하여 이를 $B$-linear map $\phi_!\T_A(M) \rightarrow \T_B(\phi_!M)$으로 보면 이것이 위의 $B$-linear map의 inverse가 되는 것을 확인할 수 있다. 
:::

## Mixed tensor

이제 $A$-module $M$과 그 dual module $M^\ast$, 그리고 이 둘 사이의 Kronecker pairing $\langle x,\xi\rangle$를 기억하자. ([§쌍대공간, ⁋정의 1](/ko/math/multilinear_algebra/dual_spaces#def1)) 선형대수에서 다루는 많은 대상들은 $M$과 $M^\ast$ 여러 개의 tensor product 안에서 찾을 수 있는데, 가령 $M$이 finitely generated projective라면 [§Hom과 텐서곱, ⁋따름정리 4](/ko/math/multilinear_algebra/hom_and_tensor#cor4)에 의하여 $M^\ast\otimes_AM\cong \End_\rMod{A}(M)$이다. 이러한 대상들을 한꺼번에 다루기 위해 tensor algebra $\T(M\oplus M^\ast)$를 생각하면, 앞 절에서 살펴본 direct sum 분해를 $M_1=M$, $M_2=M^\ast$에 적용하여 다음의 isomorphism

$$\T^n(M\oplus M^\ast)\cong\bigoplus_{(i_1,\ldots, i_n)\in\{1,2\}^n} M_{i_1}\otimes\cdots\otimes M_{i_n}$$

을 얻는다. 즉 $\T^n(M\oplus M^\ast)$의 각 summand는 $M$과 $M^\ast$를 재료로 하는 길이 $n$의 tensor product이며, 담고 있는 $M$과 $M^\ast$의 개수가 같더라도 그 배열 순서가 다르면 서로 다른 summand로 취급된다. 가령 $n=2$일 때 $M\otimes_AM^\ast$와 $M^\ast\otimes_AM$은 위의 분해에서 서로 다른 summand이다.

그러나 이 구별은 표기 이상의 정보를 담고 있지 않다. $(i_1,\ldots, i_n)$이 $p$개의 자리에서 $M$을, $q=n-p$개의 자리에서 $M^\ast$를 가리킨다 하고, $(z_1,\ldots, z_n)\in M_{i_1}\times\cdots\times M_{i_n}$에 대하여 $M$에 속하는 성분들을 원래 순서대로 $x_1,\ldots, x_p$로, $M^\ast$에 속하는 성분들을 원래 순서대로 $\xi_1,\ldots, \xi_q$로 적자. 그럼 다음의 식

$$(z_1,\ldots, z_n)\mapsto x_1\otimes\cdots\otimes x_p\otimes\xi_1\otimes\cdots\otimes\xi_q$$

으로 정의된 함수는 각 성분에 대해 $A$-linear이므로, tensor product의 universal property에 의하여 $A$-linear map $M_{i_1}\otimes\cdots\otimes M_{i_n}\rightarrow M^{\otimes p}\otimes_A(M^\ast)^{\otimes q}$이 유도된다. 반대방향의 map 또한 같은 방식으로 얻어지며, 이 둘은 decomposable tensor들 위에서 서로의 역함수이고 decomposable tensor들이 전체를 생성하므로 이 map은 isomorphism이다. 따라서 각 summand는 $M$의 성분들을 앞으로 모아둔

$$\T^p_q(M)=M^{\otimes p}\otimes_A (M^\ast)^{\otimes q}$$

와 canonical하게 isomorphic하며, 배열 순서의 구별은 잃는 정보 없이 지워도 된다. 우리는 $\T^p_q(M)$의 원소들을 *contravariant* order $p$, *covariant* order $q$의 tensor, 혹은 간단히 type $(p,q)$의 tensor라 부르고, 특히 $p,q\geq 1$인 경우 이들을 *mixed tensor*라 부른다. 이 이름들은 basis를 바꿀 때 각 성분의 좌표가 변환되는 방식에서 유래한 고전적인 용어이다. 정의로부터 $\T^p_0(M)=\T^p(M)$이고 $\T^0_q(M)=\T^q(M^\ast)$이며, $\T^0_0(M)=A$이다.

Mixed tensor가 순수한 tensor power와 다른 점은 $M$의 성분과 $M^\ast$의 성분이 한 tensor 안에 공존한다는 것이고, 따라서 이 둘을 Kronecker pairing으로 짝지어 소거하는 연산이 존재한다. $p,q\geq 1$과 $1\leq i\leq p$, $1\leq j\leq q$를 고정하고, 함수 $M^p\times (M^\ast)^q \rightarrow \T^{p-1}_{q-1}(M)$을 다음의 식

$$(x_1,\ldots, x_p,\xi_1,\ldots, \xi_q)\mapsto \langle x_i,\xi_j\rangle\cdot x_1\otimes\cdots\otimes x_{i-1}\otimes x_{i+1}\otimes\cdots\otimes x_p\otimes \xi_1\otimes\cdots\otimes \xi_{j-1}\otimes\xi_{j+1}\otimes\cdots\otimes \xi_q$$

으로 정의하자. $A$가 commutative이므로 Kronecker pairing은 $A$-bilinear이고, 나머지 성분들은 그대로 tensor product에 들어가므로 이 함수는 각 성분에 대해 $A$-linear이다. 따라서 위에서와 마찬가지로 유일한 $A$-linear map

$$c^i_j: \T^p_q(M)\rightarrow \T^{p-1}_{q-1}(M)$$

이 유도되며, 우리는 이를 $i$번째 contravariant 성분과 $j$번째 covariant 성분의 *contraction*이라 부른다. Contraction은 이름 그대로 tensor의 type을 $(p,q)$에서 $(p-1,q-1)$로 줄이는 연산이다.

가장 간단한 경우인 $p=q=1$에서 $c^1_1: M\otimes_AM^\ast\rightarrow A$는 $x\otimes\xi$를 $\langle x,\xi\rangle$로 보내는 map이며, 두 성분의 위치를 바꾸는 canonical isomorphism $M\otimes_AM^\ast\cong M^\ast\otimes_AM$을 통해 보면 이는 [§Hom과 텐서곱, §§Trace](/ko/math/multilinear_algebra/hom_and_tensor#trace)에서 정의한 $A$-linear map $\tau: M^\ast\otimes_AM \rightarrow A$와 일치한다. 특히 만일 $M$이 finitely generated projective라면 위에서 언급한 isomorphism $M^\ast\otimes_AM\cong\End_\rMod{A}(M)$ 아래에서 $c^1_1$은 정확히 [§Hom과 텐서곱, ⁋정의 6](/ko/math/multilinear_algebra/hom_and_tensor#def6)의 trace map이 된다. 이러한 의미에서 일반적인 contraction $c^i_j$는 $i$번째 contravariant 성분과 $j$번째 covariant 성분이 이루는 type $(1,1)$ 부분에 trace를 취하고 나머지 성분들은 그대로 두는 연산이라 생각할 수 있다.

이를 좌표로도 살펴보자. $M$이 finitely generated free $A$-module이라 하고, $M$의 basis $(e_k)_{1\leq k\leq r}$과 그 dual basis $(e_k^\ast)_{1\leq k\leq r}$를 고정하자. ([§쌍대공간, ⁋정의 6](/ko/math/multilinear_algebra/dual_spaces#def6)) 그럼 [명제 3](#prop3)에서와 같은 논증에 의하여 $\T^p_q(M)$은 다음의 꼴

$$e_{s_1}\otimes\cdots\otimes e_{s_p}\otimes e_{t_1}^\ast\otimes\cdots\otimes e_{t_q}^\ast$$

의 원소들을 basis로 갖는 free $A$-module이다. 가령 type $(1,1)$의 tensor $z\in M\otimes_AM^\ast$를 이 basis로 전개하여

$$z=\sum_{k,l=1}^r a^k_l (e_k\otimes e_l^\ast)$$

로 적으면, $\langle e_k, e_l^\ast\rangle=\delta_{kl}$이므로 다음의 식

$$c^1_1(z)=\sum_{k,l=1}^r a^k_l\langle e_k, e_l^\ast\rangle=\sum_{k=1}^r a^k_k$$

을 얻고, 이는 $z$에 대응되는 endomorphism의 trace를 계수들의 행렬 $(a^k_l)$의 대각성분의 합으로 계산한 것이다. 일반적인 $c^i_j$ 또한 마찬가지로 $i$번째 위첨자와 $j$번째 아래첨자를 같은 값으로 놓고 그 값에 대해 합을 취하는 연산이며, 이는 고전적인 tensor 표기법에서 위아래로 반복하여 나타나는 index끼리 짝지어 소거하는 관례에 해당한다. 마지막으로 $p=q$인 mixed tensor에 contraction을 $p$번 반복하여 적용하면 $\T^0_0(M)=A$의 원소, 즉 scalar를 얻는다.

## 대칭대수의 정의

::: 정의 5
임의의 $A$-module $M$에 대하여, tensor algebra $\T(M)$의 two-sided ideal

$$\mathfrak{I}=\langle x\otimes y-y\otimes x\mid x,y\in M\rangle$$

을 생각하자. 그럼 quotient algebra $\T(M)/\mathfrak{I}$를 $M$의 *symmetric algebra<sub>대칭대수</sub>*라 부르고 $\S(M)$으로 적는다. 
:::

정의로부터 $\mathfrak{I}$는 homogeneous ideal이므로 $\T(M)/\mathfrak{I}$가 $\mathbb{Z}_{\geq 0}$-graded algebra가 되는 것은 자명하다. 또, 각각의 generator들 $x\otimes y-y\otimes x$는 모두 degree $2$의 원소이므로, $\mathfrak{I}$로 quotient를 취하는 것은 $\T^0(M)$과 $\T^1(M)$에는 아무런 영향을 미치지 않는다. 즉, $\S^0(M)\cong A$이고 $\S^1(M)\cong M$이다. 

정의로부터 $\S(M)$이 commutative unital associative algebra인 것은 자명하다. 이는 $\S(M)$이 $\S^1(M)$의 원소들로 생성되는데, 임의의 $x,y\in \S^1(M)\cong M$에 대해서는

$$x\otimes y\equiv y\otimes x\pmod{\mathfrak{I}}$$

이기 때문이다. $\S(M)$의 두 원소의 곱은 곱셈처럼 $xy$ 등과 같이 쓰는 것이 관례이다.

한편 quotient algebra의 universal property와 [명제 2](#prop2)로부터 다음의 universal property 또한 자명하게 얻어진다. 

::: 명제 6
임의의 $A$-algebra $E$와 $A$-linear map $u:M \rightarrow E$가 다음 조건

$$u(x)u(y)=u(y)u(x)\qquad\text{for all $x,y\in M$}$$

주어졌다 하자. 그럼 유일한 $A$-algebra homomorphism $g: \S(M) \rightarrow E$가 존재하여 $u=g \circ\iota$이도록 할 수 있다. 
:::

더 일반적으로, 임의의 $A$-module $M,N$과 자연수 $n\geq 1$를 고정하자. $M^n$에서 $N$로의 *symmetric $n$-linear map*은 다음 조건

$$f(x_{\sigma(1)},x_{\sigma(2)},\ldots, x_{\sigma(n)})=f(x_1,x_2,\ldots, x_n),\qquad \sigma\in S_n$$

이 모든 $(x_i)\in M^n$과 $\sigma\in S_n$에 대해 성립하는 $n$-linear map $f$이다. 

::: 명제 7
두 $A$-module $M,N$에 대하여, 임의의 $A$-linear map $g:\S^n(M) \rightarrow N$에 대하여 다음의 식

$$(x_1,x_2,\ldots, x_n) \mapsto g(x_1x_2\cdots x_n)$$

으로 정의되는 함수는 $n$-linear이고, 이 대응을 통해 $\Hom_{\lMod{A}}(\S^n(M), N)$에서, symmetric $n$-linear map $M^n \rightarrow N$들의 $A$-module로의 bijective $A$-module homomorphism이 정의된다. 
:::

이 때, $A$-module $\S^n(M)$을 $M$의 *$n$번째 symmetric power<sub>$n$번째 대칭곱</sub>*이라 부른다. 그럼 임의의 $A$-linear map $u:M \rightarrow N$에 대하여, $\S^n(u): \S^n(M) \rightarrow \S^n(N)$이 유도되며 이들의 direct sum을 취하면 $\S(u)$를 복원할 수 있다.

## 대칭대수의 성질들

앞서 functor $T$와 $\rMod{A}$의 연산들이 어떻게 행동하는지를 살펴보았다. 이제 이러한 결과들이 $S$에 대해서도 성립하는 것을 증명한다.

우선 $M=\bigoplus_{i\in I} M_i$가 $A$-module들 $M_i$들의 direct sum이라 하자. 그럼 우리는 다음의 isomorphism

$$\S(M)\cong \bigotimes_{i\in I} \S(M_i)$$

를 얻는다. 이는 $S$가 forgetful functor $U:\cAlg{A}\rightarrow \rMod{A}$의 left adjoint이므로 colimit을 보존하고, $\cAlg{A}$에서의 coproduct는 ($\cRing$에서의 coproduct가 tensor product이듯) $\otimes_A$로 주어지기 때문이다. 특히 [명제 3](#prop3)과 같이 free $A$-module의 basis $(e_i)$를 고정해두고 나면 다음의 명제를 얻는다.

::: 명제 8
Free $A$-module $M$과 그 basis $(e_i)_{i\in I}$에 대하여, $\alpha:I \rightarrow \mathbb{N}$을 finitely supported function이라 하자. 

$$e^\alpha=\prod_{i\in I} e_i^{\alpha(i)}$$

라 하면, 이러한 원소들을 모두 모아둔 것이 $\S(M)$의 basis가 된다.
:::

이들의 multiplication은 $e^\alpha e^\beta=e^{\alpha+\beta}$로 주어진다. 즉 이 경우 $\S(M)$은 정확하게 polynomial algebra $A[\x_i]_{i\in I}$가 된다. 

[명제 4](#prop4)에 대응되는 결과는 다음의 명제이며, 그 증명 또한 동일하다. 

::: 명제 9
$\S_{B}(B\otimes_AM)\rightarrow B\otimes_A\S_A(M)$은 isomorphism이다. 
:::

## 외대수의 정의

::: 정의 10
임의의 $A$-module $M$에 대하여, tensor algebra $\T(M)$의 two-sided ideal 

$$\mathfrak{J}=\langle x\otimes x\mid x\in M\rangle$$

을 생각하자. 그럼 quotient algebra $\T(M)/\mathfrak{J}$를 $M$의 *exterior algebra<sub>외대수</sub>*라 부르고 $\bigwedge(M)$으로 적는다. 
:::

$\bigwedge(M)$에서의 원소들의 곱셈은 $\wedge$로 적는 것이 관례이다. 한편 [정의 5](#def5) 이후의 논의와 마찬가지로, $\mathfrak{J}$는 homogeneous ideal이고 canonical inclusion $\iota:M \hookrightarrow\bigwedge(M)$이 존재한다는 것이 자명하다. 또, [명제 6](#prop6)과 마찬가지 이유에서 다음의 universal property가 성립한다.

::: 명제 11
임의의 $A$-algebra $E$와 $A$-linear map $u:M \rightarrow E$가 다음 조건

$$u(x)^2=0\qquad\text{for all $x\in M$}$$

주어졌다 하자. 그럼 유일한 $A$-algebra homomorphism $g: \bigwedge(M) \rightarrow E$가 존재하여 $u=g \circ\iota$이도록 할 수 있다. 
:::

[명제 7](#prop7)과 비슷한 성질이 exterior algebra에서도 성립한다. 이하 $A$의 표수는 $2$가 아니라고 가정한다. 임의의 $A$-module $M,N$과 정수 $n\geq 1$에 대하여, $M^n$에서 $N$로의 $n$-linear map $f$가 *alternating $n$-linear map*이라는 것은 다음 조건

$$f(x_{\sigma(1)},x_{\sigma(2)},\ldots, x_{\sigma(n)})=\epsilon(\sigma)f(x_1,x_2,\ldots, x_n),\qquad \sigma\in S_n$$

이 모든 $(x_i)\in M^n$과 $\sigma\in S_n$에 대해 성립하는 것이다. 이는 임의의 $x_1,\ldots, x_{n-2}$와 $x$에 대하여

$$f(x_1,\ldots, x_i, x,x,x_{i+1},\ldots, x_{n-2})=0$$

이 성립하는 것과 동치이다. 

::: 명제 12
두 $A$-module $M,N$에 대하여, 임의의 $A$-linear map $g:\bigwedge^n(M) \rightarrow N$에 대하여 다음의 식

$$(x_1,x_2,\ldots, x_n) \mapsto g(x_1\wedge x_2\wedge\cdots\wedge x_n)$$

으로 정의되는 함수는 $n$-linear이고, 이 대응을 통해 $\Hom_{\lMod{A}}(\bigwedge^n(M), N)$에서, alternating $n$-linear map $M^n \rightarrow N$들의 $A$-module로의 bijective $A$-module homomorphism이 정의된다. 
:::

## 외대수의 성질들

마찬가지로 $M=\bigoplus_{i\in I} M_i$가 $A$-module들 $M_i$들의 direct sum이라 하였을 때, $\bigwedge$가 left adjoint인 것으로부터 $\bigwedge(M)$이 $\bigwedge(M_i)$들의 coproduct가 되어야 한다는 것을 안다. 이를 엄밀히 하기 위해서는 alternating algebra들의 category에서의 coproduct를 정의해야 한다. 이는 $\cAlg{A}$와 유사하게 tensor product로 나오지만, Koszul sign convention이 붙어있다. 이는 별다른 것은 아니고, 정의로부터 exterior algebra의 degree $m,n$의 원소를 곱하면 $(-1)^{mn}$의 부호가 생기게 되므로 이를 반영해주는 것이다. 당장은 이를 엄밀하게 쓸 이유는 없으니 다음 명제만 소개한다. 

::: 명제 13
Free $A$-module $M$과 그 basis $(e_i)_{i\in I}$에 대하여, $I$의 total ordering을 하나 고정하자. 임의의 유한한 부분집합 $J\subseteq I$에 대하여

$$e_J=e_{j_1}\wedge e_{j_2}\wedge\cdots\wedge e_{j_k},\qquad j_1<\cdots < j_k, \quad J=\{j_1,\ldots, j_k\}$$

라 하면, 이러한 $e_J$들을 모아둔 것이 $\bigwedge (M)$의 basis가 된다. 
:::

예를 들어, $e_1\wedge e_2\wedge e_3$과 $e_1\wedge e_3\wedge e_2$는 나중 두 원소의 위치를 서로 바꾸어 주기만 하면 부호의 차이만 제외하고는 같은 원소가 되므로 위와 같이 $I$에 아무렇게나 order를 준 후 이에 맞추어 배열하는 식으로 무의미한 중복을 피할 수 있다. 다음 명제는 더더욱 설명할 것이 없다. 

::: 명제 14
$\bigwedge_{B}(B\otimes_AM)\rightarrow B\otimes_A\bigwedge_A(M)$은 isomorphism이다. 
:::


---

**참고문헌**

**[Bou]** Bourbaki, N. Algebra I. *Elements of Mathematics*. Springer. 1998.  

---

[^1]: Category $\Ring$에서의 coproduct는 free product와 비슷한 식으로 정의되었던 것을 기억하자. ([§환의 곱, 쌍대곱, 텐서곱, ⁋명제 4](/ko/math/algebraic_structures/operations_of_rings#prop4)) 반면, 같은 글에서 우리는 category $\cRing$의 coproduct는 tensor product $\otimes$로 주어진다는 것 또한 확인하였다.