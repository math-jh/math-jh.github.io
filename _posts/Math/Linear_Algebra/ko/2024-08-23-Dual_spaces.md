---

title: "쌍대공간"
excerpt: ""

categories: [Math / Linear Algebra]
permalink: /ko/math/linear_algebra/dual_spaces
header:
    overlay_image: /assets/images/Math/Linear_Algebra/Dual_spaces.png
    overlay_filter: 0.5
sidebar: 
    nav: "linear_algebra-ko"

date: 2024-08-23
last_modified_at: 2024-08-23
weight: 103

---

## 쌍대공간의 정의

임의의 left $A$-module $M$을 고정하고, $A$를 자기 자신 위의 left $A$-module로 본 것을 $A_l$이라 하자. 임의의 $\alpha\in A$, $f\in\Hom_{\lMod{A}}(M, A_l)$에 대하여, 다음 식

$$(f\cdot\alpha)(x)=f(x)\alpha\qquad\text{for all $x\in M$}$$

을 통해 $\Hom_{\lMod{A}}(M, A_l)$을 right $A$-module로 생각할 수 있다. 

<div class="definition" markdown="1">

<ins id="def1">**정의 1**</ins> 위에서 정의한 right $A$-module $\Hom_{\lMod{A}}(M, A_l)$를 $M$의 *dual module<sub>쌍대가군</sub>*이라 부르고 $M^\ast$로 적는다.

</div>

비슷하게 right $A$-module $M$이 주어졌다면 $\Hom_{\rMod{A}}(M,A_r)$를 left $A$-module로 볼 수 있으며 우리는 이를 $M$의 dual module이라 부른다. 특별히 $M=A$인 경우, $A_l^\ast=A_r$이고 $A_r^\ast=A_l$인 것을 확인할 수 있다. 

정의에 의해, 임의의 $x\in M$과 임의의 $\xi\in M^\ast$가 주어졌다면 이들 쌍은 $\xi(x)\in A$를 지정한다. 이를 $\langle x, \xi\rangle$로 적으며, 이러한 표기를 *Kronecker pairing<sub>크로네커 쌍</sub>*이라 부른다. 

<div class="definition" markdown="1">

<ins id="def2">**정의 2**</ins> 임의의 $A$-module $M$과 그 dual $M^\ast$에 대하여, $x\in M$과 $\xi\in M^\ast$가 *orthogonal<sub>작교</sub>*한다는 것은 $\langle x,\xi\rangle=0$인 것이다.

</div>

$M$과 $M^\ast$의 두 부분집합의 임의의 원소들의 쌍이 orthogonal이라면 이들 둘이 orthogonal하다 말한다. 한편, $x\in M$를 임의로 고정하고 $\xi,\xi_1,\xi_2\in M^\ast$와 $\alpha\in A$가 주어졌다 하자. 그럼

$$\langle x, \xi_1+\xi_2\rangle=\langle x, \xi_1\rangle,+\langle x,\xi_2\rangle=0,\qquad \langle x,\xi\cdot\alpha\rangle=\langle x,\xi\rangle\alpha=0$$

이므로, $M$의 고정된 부분집합 $S$에 대해, $S$의 원소들과 orthogonal한 $M^\ast$의 원소들을 모아두면 이는 $M^\ast$의 submodule이 된다.

<div class="definition" markdown="1">

<ins id="def3">**정의 3**</ins> 위와 같이 정의한 $M^\ast$의 submodule을 $M$에 orthogonal한 submodule이라 부르고, $S^\perp$라 적는다.

</div>

임의의 부분집합 $T\subseteq M^\ast$에 대해서도 비슷하게 $T^\perp$를 정의할 수 있는데, 여기서 주의할 것은 $T^\perp$를 $M^{\ast\ast}$의 submodule이 아니라 $M$의 submodule로 정의한다는 것이다. 

## 선형사상의 전치

임의의 $A$-linear map $f:M \rightarrow N$이 주어졌다 하자. 그럼 [\[대수적 구조\] §가군, ⁋명제 8](/ko/math/algebraic_structures/modules#prop8)의 abelian group homomorphism

$$\Hom(f,A_l):\Hom_{\lMod{A}}(N,A_l)\rightarrow\Hom_{\lMod{A}}(M,A_l)$$

이 $A$의 right action과 compatible함을 알 수 있다. 즉 $\Hom(f,A_l)$는 right $A$-module homomorphism이다.

<div class="definition" markdown="1">

<ins id="def4">**정의 4**</ins> Left $A$-module들 사이의 $A$-linear map $f:M \rightarrow N$에 대하여, 위에서 정의한 right $A$-module homomorphism을 $f$의 *transpose<sub>전치</sub>*라 하고 $f^\ast$로 적는다.

</div>

$f^\ast$는 임의의 $\xi\in N^\ast$에서의 값 $f^\ast(\xi)\in M^\ast$로 주어지며, 다시 $f^\ast(\xi)\in M^\ast$는 임의의 $x\in M$에서의 값 

$$f^\ast(\xi)(x)=\langle x, f^\ast(\xi)\rangle$$

에 의해 결정된다. 한편 $f^\ast=\Hom(f,A_l)$의 정의에 의해 $f^\ast(\xi)=\xi\circ f$이다. 즉, 위의 식은

$$\langle f(x),\xi\rangle=\langle x, f^\ast\xi\rangle$$

으로 쓸 수 있으며, 거꾸로 이 식이 모든 $x\in M$과 모든 $\xi\in N^\ast$에 대해 성립한다면 $f^\ast$가 유일하게 결정된다. 

또, $\Hom(-,A_l)$의 functoriality와 [\[대수적 구조\] §가군, ⁋명제 8](/ko/math/algebraic_structures/modules#prop8)에 의해 다음 명제를 얻는다. 

<div class="proposition" markdown="1">

<ins id="prop5">**명제 5**</ins> 다음이 성립한다.

1. 두 $A$-linear map $f,g:M \rightarrow N$에 대하여, $(f+g)^\ast=f^\ast+g^\ast$이다.
2. 두 $A$-linear map $f:M \rightarrow N$, $g:N \rightarrow L$에 대하여, $(g\circ f)^\ast=f^\ast\circ g^\ast$이다.
3. 임의의 $M$에 대하여, $(\id_M)^\ast=\id_{M^\ast}$이다.

</div>

## 쌍대기저

$A$-module $M$이 basis $(x\_i)\_{i\in I}$를 갖는다 하자. () 즉 다음의 isomorphism

$$\varepsilon: A_l^{\oplus I} \rightarrow M$$

이 존재한다. 그럼 이 isomorphism의 dual을 생각하면 right $A$-module들 사이의 isomorphism

$$\varepsilon^\ast: M^\ast \rightarrow (A_l^{\oplus I})^\ast=\Hom_{\lMod{A}}(A_l^{\oplus I}, A_l)\cong \prod_{i\in I}\left(\Hom_\lMod{A}(A_l,A_l)\right)\cong \prod_{i\in I} A_r$$

을 얻는다. 이제 우변의 원소들 중, $i$번째 성분만 $1$이고, 나머지 성분은 $0$인 원소들을 생각하고, 이 원소의 $\varepsilon^\ast$에 대한 preimage를 $e_i^\ast$로 적자. 그럼 다음 식

$$\langle e_i, e_j^\ast\rangle=\delta_{ij}$$

이 성립한다는 것을 안다. 이들의 모임은 linearly independent이지만, $I$가 무한집합이라면 이것이 $M^\ast$의 basis가 되지는 않는다. 그러나 $I$가 유한집합이라면 $\prod_{i\in I} A\cong \bigoplus_{i\in I}A$이므로 이들이 정확히 basis가 된다. 

<div class="definition" markdown="1">

<ins id="def6">**정의 6**</ins> 만일 $M$이 finitely generated free module이고, basis $(e\_i)\_{i\in I}$를 갖는다면 위에서 정의한 $M^\ast$의 basis $(e_i^\ast)\_{i\in I}$를 $(e\_i)$의 *dual basis<sub>쌍대기저</sub>*라 부른다.

</div>


## 이중쌍대공간

임의의 left $A$-module $M$에 대하여, $M$의 dual $M^\ast$는 right $A$-module이고 $M^\ast$의 dual $M^{\ast\ast}$는 다시 left $A$-module이 된다. 한편 임의의 $x\in M$에 대하여, 다음 식

$$\langle x,-\rangle: M^\ast \rightarrow A$$

을 통해 정의된 함수가 right $A$-module homomorphism인 것을 확인할 수 있다. 즉 위의 식이 $M$에서 $M^{\ast\ast}$로의 함수를 정의하며, 이 함수 또한 linear map인 것을 확인할 수 있다. 일반적으로 이 함수는 injective도, surjective도 되지 않는다.

<div class="definition" markdown="1">

<ins id="def7">**정의 7**</ins> 만일 위의 함수 $M \rightarrow M^{\ast\ast}$이 bijective라면 $M$을 *reflexive*라 부른다.

</div>

그럼 다음이 성립한다.

<div class="proposition" markdown="1">

<ins id="prop8">**명제 8**</ins> 임의의 free module $M$에 대하여, 위에서 정의한 $M \rightarrow M^{\ast\ast}$는 injective이다. 만일 여기에 더하여, $M$이 finitely generated라면 이 함수는 bijectivedㅣ다.

</div>

