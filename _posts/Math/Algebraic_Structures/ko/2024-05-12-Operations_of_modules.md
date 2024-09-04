---

title: "가군의 곱과 합, 텐서곱"
excerpt: ""

categories: [Math / Algebraic Structures]
permalink: /ko/math/algebraic_structures/operations_of_modules
header:
    overlay_image: /assets/images/Math/Algebraic_Structures/Operations_of_modules.png
    overlay_filter: 0.5
sidebar: 
    nav: "algebraic_structures-ko"

date: 2024-05-12
last_modified_at: 2024-05-12
weight: 202

---

## 가군의 곱과 합

Category $\lMod{A}$는 bicomplete category이다. 이를 보이기 위해서는 $\lMod{A}$에서의 임의의 product와 coproduct를 만들어야 하는데, 이를 보이기 위해서는 $\Ab$에서의 product와 coproduct 위에 자연스러운 $A$-action이 존재한다는 것을 보이면 된다.

$A$-module들의 family $(M\_i)\_{i\in I}$이 주어졌다 하자. 그럼 $\prod M\_i$ 위에서의 action은 다음의 식

$$A\otimes\left(\prod_{i\in I}M_i\right)\overset{\id_A\otimes\pr_i}{\longrightarrow} A\otimes M_i \overset{\rho_i}{\longrightarrow} M_i $$

을 통해 $A\otimes\left(\prod M\_i\right) \rightarrow M\_i$를 정의한 후, $\Ab$에서의 product의 universal property를 이용해 $A\otimes\left(\prod M\_i\right) \rightarrow \prod M\_i$를 만들고 이것이 action의 조건을 만족함을 보이면 된다. 

Coproduct의 경우, $A\otimes-$은 $\Ab$에서 $\Ab$로의 left adjoint이므로 colimit을 보존하고, 따라서 

$$A\otimes\left(\bigoplus_{i\in I} M_i\right)\cong\bigoplus_{i\in I}(A\otimes M_i)\overset{\bigoplus \rho_i}{\longrightarrow} \bigoplus_{i\in I}M_i$$

를 통해 $\bigoplus M\_i$ 위에서의 action이 정의된다. Equalizer와 coequalizer의 경우, 두 module homomorphism $f,g:M \rightarrow N$에 대하여

$$\Eq(f,g)=\{x\in M: f(x)=g(x)\}$$

그리고

$$\CoEq(f,g)=N/N',\qquad N'=\langle f(x)-g(x)\rangle\rangle$$

을 통해 정의할 수 있다. 즉 다음이 성립한다. 

<div class="proposition" markdown="1">

<ins id="thm1">**정리 1**</ins> $\lMod{A}$는 bicomplete category이며, 특히 $A$-module들의 family $(M_i)$의 product는 이들의 direct product, coproduct는 이들의 direct sum으로 주어진다.

</div>

그럼 direct product는 kernel을, direct sum은 cokernel을 각각 보존한다. ([\[범주론\] §극한, ⁋명제 10](/ko/math/category_theory/limits#prop10)) 추가로 이들은 다음의 명제 또한 만족한다. 

<div class="proposition" markdown="1">

<ins id="prop2">**명제 2**</ins> 두 $A$-module들의 family $(M\_i)\_{i\in I},(N\_i)\_{i\in I}$와 이들 사이의 linear map들 $f\_i: M\_i \rightarrow N\_i$가 주어졌다 하고, 이들이 유도하는 함수 $\bigoplus f\_i:\bigoplus M\_i \rightarrow \bigoplus N\_i$와 $\prod f\_i: \prod M\_i \rightarrow \prod N\_i$를 생각하자. 그럼 다음이 성립한다.

1. 만일 $f\_i$들 각각이 surjective라면 $\prod f\_i$도 surjective이고, 그 역도 성립한다.
2. 만일 $f\_i$들 각각이 injective라면 $\bigoplus f\_i$도 injective이고, 그 역도 성립한다.

</div>

이에 대한 증명은 $\prod f\_i$와 $\bigoplus f\_i$를 직접 좌표별로 써서 얻어진다. 특히 이 명제에 의해 direct product는 cokernel 또한 보존하고, direct sum은 kernel 또한 보존한다는 것을 알 수 있다. 

앞서 우리는 임의의 $M,N\in\lMod{A}$에 대하여 $\Hom_{\lMod{A}}(M,N)$이 abelian group이 된다는 것을 살펴보았다. 어렵지 않게 이 덧셈이 합성에 대해 잘 행동하고, category $\lMod{A}$는 zero module $0$을 zero object로 갖는 additive category가 된다는 것을 확인할 수 있다. ([\[범주론\] §아벨 카테고리, ⁋정의 1](/ko/math/category_theory/abelian_categories#def1))

뿐만 아니라 $\lMod{A}$는 abelian category가 된다. ([\[범주론\] §아벨 카테고리, ⁋정의 7](/ko/math/category_theory/abelian_categories#def7)) 이를 확인하기 위해서는 임의의 monomorphism $f:M \rightarrow N$은 그 cokernel $N \rightarrow N/M$의 kernel과 같고, 임의의 epimorphism $g:M \rightarrow N$은 그 kernel $\ker g$의 cokernel $M \rightarrow M/\ker g$과 같다는 것을 확인하면 된다. 

## 자유가군

[§가군, ⁋예시 5](/ko/math/algebraic_structures/modules#ex5)에서 우리는 ring $A$가 $A$-module의 구조를 가진다는 것을 살펴보았다. 그럼 임의의 $A$-module homomorphism $f:A \rightarrow M$는 $f(1)$에 의해 유일하게 결정된다. 임의의 $\alpha\in A$에 대하여, 

$$f(\alpha)=f(\alpha\cdot 1)=\alpha\cdot f(1)$$

이기 때문이다. 바꾸어 말하면 다음의 isomorphism

$$\Hom_A(A, M)\cong\Hom_\Set(\ast, U(M))$$

이 성립한다. 여기서 $U:\lMod{A} \rightarrow \Set$은 forgetful functor이다. 즉 $A$는 forgetful functor $U$의 representation이라 할 수 있다. 

한편 앞서 $\lMod{R}$이 coproduct $\bigoplus$를 갖는다는 것을 확인하였으므로, $U$의 left adjoint $F: \Set \rightarrow \lMod{A}$가 존재한다면 다음의 식

$$F(X)=F\left(\coprod_{x\in X} \{x\}\right)\cong\bigoplus_{x\in X} F(\{x\})$$

이 성립해야 하고, 위의 representation을 이용하면 $F(X)=\bigoplus_{x\in X}Ax$로 정의해야 한다는 것을 안다. 즉 다음이 성립한다. 

<div class="proposition" markdown="1">

<ins id="prop3">**명제 3**</ins> Forgetful functor $U:\lMod{A} \rightarrow\Set$과 위에서 정의한 free functor $F:\Set \rightarrow\lMod{A}$에 대하여, adjunction $F\dashv U$가 존재한다.

</div>

임의의 집합 $X$에 대하여, $F(X)$와 isomorphic한 $A$-module들을 *free $A$-module<sub>자유 $A$-가군</sub>*이라 부른다.

## 가군의 텐서곱

한편 우리는 $A$-module들의 텐서곱 또한 정의할 수 있다. 우선 다음 정의부터 시작한다. 

<div class="definition" markdown="1">

<ins id="def4">**정의 4**</ins> Ring $A$와 right $A$-module $M$, left $A$-module $N$이 주어졌다 하자. 그럼 임의의 abelian group $L$에 대하여, 함수 $f:M\times N \rightarrow L$이 *$A$-balanced*라는 것은 $f$가 abelian group들 사이의 함수로서 bilinear이고, 추가로 다음 식

$$f(x\alpha, y)=f(x,\alpha y)$$

이 성립하는 것이다. 

</div>

고정된 $M\in\obj(\rMod{A}),N\in\obj(\lMod{A})$에 대하여, 집합 $\Balan_A(M,N;L)$를 다음 식

$$\Balan_A(M,N;L)=\{\text{$A$-balanced maps from $M\times N$ to $L$}\}$$

으로 정의하자. 그럼 다음 정리가 성립한다.

<div class="proposition" markdown="1">

<ins id="thm5">**정리 5**</ins> Functor $\Balan_A(M,N;-):\lMod{\mathbb{Z}}=\Ab\rightarrow\Set$은 representable functor이다.

</div>
<details class="proof" markdown="1">
<summary>증명</summary>

Free abelian group $F(M\times N)$의 subgroup $M'$를

$$M'=\left\langle (x, y_1+y_2)-(x,y_1)-(x,y_2), (x_1+x_2,y)-(x_1,y)-(x_2,y), (\alpha x,y)-(x,\alpha y)\right\rangle$$

으로 정의하자. 그럼 free group의 universal property에 의하여, 임의의 함수 $f:M\times N \rightarrow L$이 주어질 때마다 group homomorphism $\hat{f}:F(M\times N)\rightarrow L$이 존재하고, $f$가 $A$-balanced라면 이 $\hat{f}$의 kernel이 $M'$를 포함하므로 $\hat{f}$가 $F(M\times N)/M'$에서 $L$로의 group homomorphism을 정의한다. 

Isomorphism $\Balan_A(M,N;L)\cong\Hom_\Ab(F(M\times N)/M',L)$의 naturality는 추가적으로 보여야 하긴 하지만, 단순한 계산이므로 생략한다. 

</details>

이렇게 얻어진 representation을 $M\otimes_AN$으로 적는다. 그럼 다음이 성립한다.

<div class="proposition" markdown="1">

<ins id="thm6">**정리 6 ($\otimes\dashv\Hom$)**</ins> Adjunction 

$$\Hom_\mathbb{Z}(M\otimes_A N, L)\cong\Hom_{\rMod{A}}(M,\Hom_\mathbb{Z}(N, L))\cong\Hom_{\lMod{A}}(N,\Hom_\mathbb{Z}(M, L))$$

이 존재한다. 

</div>

따라서 $\otimes$는 colimit과 commute하고, $\Hom$은 limit과 commute한다. 특히 abelian group들 사이의 다음의 isomorphism들

$$M\otimes_A\left(\bigoplus_{i\in I} N_i\right)\cong \bigoplus_{i\in I} M\otimes_AN_i,\qquad \left(\bigoplus_{i\in I} M_i\right)\otimes_A N\cong\bigoplus_{i\in I} M_i\otimes_AN\tag{1}$$

그리고

$$\Hom_{\lMod{A}}\left(M,\prod_{i\in I} N_i\right)\cong\prod_{i\in I}\Hom_{\lMod{A}}(M, N_i),\qquad \Hom_{\lMod{A}}\left(\bigoplus_{i\in I} M_i, N\right)\cong \prod_{i\in I}\Hom_{\lMod{A}}(M_i,N)\tag{2}$$

을 얻는다. 특별히 $A=\mathbb{Z}$인 경우 [§가환군, §§텐서곱](/ko/math/algebraic_structures/abelian_groups#텐서곱)의 내용들을 복구하게 되는데, 위의 isomorphism들은 해당 글에서는 분량의 문제로 적지 않았던 것들이다.

## 가환환 위에서 정의된 가군의 텐서곱

앞서 정의한 $M\otimes_A N$이 $A$-module 구조를 갖지 않는다. 이는 $M\otimes_A N$ 위에 $A$의 action을 정의한다 생각해보면, 다음 원소

$$(x\alpha)\otimes_A y=x\otimes_A(\alpha y)$$

를 $\alpha(x\otimes_Ay)$로 정의하는 것이 자연스럽겠지만, $(\alpha\beta)(x\otimes_Ay)$를 계산해서 나온

$$(x\alpha\beta)\otimes_A y,\qquad x\otimes_A(\alpha\beta y)$$

가 서로 다른 원소가 될 것이기 때문이다. Tensor product의 정의에서, $M$은 right module로, $N$은 left module로 두는 것도 이와 비슷한 이유에서이다.

만일 $M$이 right $A$-module의 구조 뿐만 아니라, 이와 호환되는 left $B$-module 구조를 갖고 있다면 $M$을 $(B,A)$-bimodule이라 부른다. 즉, 임의의 $\alpha\in A$, $\beta\in B$, $x\in M$에 대하여 다음 식

$$(\alpha\cdot_A x)\cdot_B\beta=\alpha\cdot_A(x\cdot_B\beta)$$

아 성립해야 하는 것이다. 그럼 다음 식

$$\beta(x\otimes_A y)=(\beta x)\otimes_Ay$$

이 $M\otimes_AN$ 위에 left $B$-module 구조를 준다는 것을 확인할 수 있다. 

우리는 대부분 $A$가 commutative ring인 경우에 관심이 있다. 그럼 임의의 left $A$-module은 right $A$-module이기도 하고, 그 반대도 성립한다. 뿐만 아니라, 이를 통해 임의의 left $A$-module을 right $A$-module로 보면 이 두 구조는 $(A,A)$-bimodule의 구조를 이룬다. 따라서 $M\otimes_AN$에 자연스러운 $A$-action

$$\alpha(x\otimes_Ay)=(\alpha x)\otimes_Ay=x\otimes_A(\alpha y)$$

이 존재한다. 이 또한 적절한 functor의 representation이 된다.

<div class="definition" markdown="1">

<ins id="def7">**정의 7**</ins> Commutative ring $A$와 세 $A$-module $M,N,L$이 주어졌다 하자. 그럼 함수 $f:M\times N \rightarrow L$이 *$A$-bilinear*라는 것은 $f$가 abelian group들 사이의 함수로서 bilinear이고, 추가로 다음 식

$$\alpha f(x,y)=f(\alpha x,y)=f(x,\alpha y)$$

이 성립하는 것이다. 

</div>

집합 $\Bilin_A(M,N;L)$을 다음 식

$$\Bilin_A(M,N;L)=\{\text{$A$-bilinear maps from $M\times N$ to $L$}\}$$

으로 정의하자.

<div class="proposition" markdown="1">

<ins id="prop8">**명제 8**</ins> Functor $\Bilin_A(M,N;-):\lMod{A}\rightarrow\Set$은 representable functor이며, 그 representation은 위에서 정의한 *$A$-module* $M\otimes_AN$이다. 

</div>

한편 $A$가 일반적인 ring이라면 $\Hom_{\lMod{A}}(M,M')$은 $A$-module 구조를 갖지 않았지만, $A$가 commutative ring이라면 $\Hom_{\lMod{A}}(M,M')$ 위에도 $A$-module 구조가 존재한다. 즉, $\Hom_A$는 internal $\Hom$이며,  따라서 [정리 6](#thm6)의 adjunction을 더 다듬어 다음을 증명할 수 있다.

<div class="proposition" markdown="1">

<ins id="thm9">**정리 9**</ins> Adjunction

$$\Hom_A(M\otimes_AN, L)\cong\Hom_A(M,\Hom_A(N,L))\cong\Hom_A(N,\Hom_A(M,L))$$

이 존재한다. 

</div>

특히 위의 식들 (1), (2)가 모두 $A$-module들 사이의 isomorphism이 된다. 또, $(\lMod{A},\otimes_A,A)$이 symmetric monoidal category가 된다는 것을 확인할 수 있다. 