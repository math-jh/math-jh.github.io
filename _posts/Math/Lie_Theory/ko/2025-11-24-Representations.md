---

title: "리 군의 표현"
excerpt: ""

categories: [Math / Lie Theory]
permalink: /ko/math/Lie_theory/representations
header:
    overlay_image: /assets/images/Math/Lie_Theory/Representations.png
    overlay_filter: 0.5
sidebar: 
    nav: "Lie_theory-ko"

date: 2025-11-24
last_modified_at: 2025-11-24
weight: 2

---

일반적으로 그 구조가 복잡한 수학적인 대상을 다룰 때 좋은 전략 중 하나는 이 대상이 다른 단순한 대상 위에 어떻게 작용하는지를 보는 것이다. Lie group의 경우 이러한 철학은 더 각별한데, Lie group의 대표적인 예시인 $\GL(n;\mathbb{R})$이나 $\Diff(M)$ 등을 생각하면 이들은 그 본질부터가 다른 대상 위에 act하는 것이기 때문이다. 이번 글에서 우리는 Lie group의 finite-dimensional representation을 살펴본다.

{% comment %}
나중에 표현론 카테고리 만들면 빼기
{% endcomment %}

## 유한군의 표현론

우선 우리는 유한군의 표현론을 살펴본다. 임의의 finite group은 discrete topology와 자명한 미분구조가 주어진 Lie group이라 생각할 수 있으므로 이는 앞으로 살펴볼 일반적인 경우의 특수한 케이스로 생각할 수 있다. 그러나 이 일반화의 과정은 상당히 단순한 것이며, 이 일반화 하에서 모든 원하는 결과들이 성립하므로 사실상 이 섹션에 우리의 주장들이 모두 담겨있다고 생각하여도 된다. 우선 다음의 정의부터 시작하자. 

<div class="definition" markdown="1">

<ins id="def1">**정의 1**</ins> 임의의 finite group $G$에 대하여, $G$의 *representation<sub>표현</sub>*은 벡터공간 $V$와, group action의 조건을 만족하는 함수

$$\rho: G\times V \rightarrow V$$

가 주어져서 각각의 $\rho(g,-)$가 linear map인 것이다.

</div>

혹은, 더 간략하게 group homomorphism $G\rightarrow \Aut(V)$가 주어진 것으로 생각할 수도 있다. 우리는 편의를 위해 함수 $\rho$가 문맥에 따라 명확하다면 $V$를 $G$의 representation이라 부르기도 한다. 

일반적으로 ground field $\mathbb{K}$는 임의의 ring $A$로 대체해도 아무런 문제는 없지만, 우리의 논의에서는 $\mathbb{K}=\mathbb{C}$로 두어도 충분하므로 이렇게 고정하기로 한다. 

고정된 (finite) group $G$와 $G$의 두 representation 사이의 morphism은 $G$-equivariant map들, 즉 다음의 diagram

![G-equivariant_maps](/assets/images/Math/Lie_Theory/Representations-1.png){:style="width:10em" class="invert" .align-center}

으로 주어진다. 이들의 합성이 잘 행동하는 것은 자명하므로, 고정된 group $G$에 대하여 $G$의 representation들의 category $\Rep_\mathbb{C}(G)$가 존재한다. 

한편 $V$에 적용되는 선형대수학의 언어를 차용하면 다음을 정의할 수 있다. 

<div class="definition" markdown="1">

<ins id="def2">**정의 2**</ins> Group $G$의 representation $G\times V\rightarrow V$에 대하여 다음을 정의한다. 

1. $V$의 subspace $W$가 *$G$-invariant<sub>$G$-불변공간</sub>*라는 것은 임의의 $g\in G$와 임의의 $w\in W$에 대하여 $g\cdot w\in W$가 항상 성립하는 것이다.
2. 임의의 $G$-invariant subspace $W$에 대하여, representation $G\times W\rightarrow W$를 $V$의 *subrepresentation<sub>부분표현</sub>*이라 부른다. 
3. 만일 $V$가 zero representation이 아니고 $V$의 subrepresentation들이 trivial subrepresentation들, 즉 자기 자신과 $G\times\\{0\\}\rightarrow\\{0\\}$ 뿐이라면 $V$를 *irreducible representation<sub>기약표현</sub>*이라 부른다. 

</div>

임의의 representation $G\rightarrow \Aut(V)$가 주어졌을 때, 우리는 $G$-fixed point들의 집합

$$V^G=\{v\in V\mid g\cdot v=v\text{ for all $g\in G$}\}$$

이 $G$-invariant subspace임을 안다. 따라서 representation $G\rightarrow \Aut(V)$이 irreducible representation이기 위해서는 $V^G=V$이거나 $V^G=\\{0\\}$이어야 한다. 그런데 $V^G=V$이라면, $V$의 임의의 subspace가 $G$-invariant일 것이므로 $G\rightarrow \Aut(V)$가 irreducible representation이기 위해서는 $V^G=\\{0\\}$이거나 $V$가 $1$차원이어야 한다. 

이 $G$-fixed point set $V^G$은 주어진 $G$-representation $V$로부터 새로운 $G$-representation을 얻어내는 하나의 방법이다. 이 외에도 주어진 $G$-representation들로부터 새로운 $G$-representation을 구성하는 방법들이 여럿 존재한다. 가령 선형대수의 각종 construction들을 생각하고, 그 위에 $G$-action을 정의해주면 다음을 얻는다. 

<div class="definition" markdown="1">

<ins id="def3">**정의 3**</ins> $G$-representation $V, W$에 대하여, 다음의 $G$-action을 통해 새로운 $G$-representation들을 정의한다.

1. Direct sum $V\oplus W$; $G$-action $g\cdot(v,w)=(g\cdot v,g\cdot w)$
2. Tensor product $V\otimes W$; $G$-action $g\cdot(v\otimes w)=(g\cdot v)\otimes (g\cdot w)$
3. $\Hom_\mathbb{C}(V,W)$; $G$-action $(g\cdot f)(v)=g\cdot f(g^{-1}\cdot v)$
4. 3번에서 $W=\mathbb{C}$로 두어 얻어지는 *dual representation* $V^\ast$
5. 스칼라곱을 conjugate으로 바꾸어 얻어지는 *conjugate representation* $\overline{V}$
6. 그 외 exterior power $\bigwedge^k V$, symmetric power $\operatorname{Sym}^k V$ 등에도 자연스럽게 정의되는 $G$-action들.

</div>

이러한 construction들을 체계적으로 다루기 위해서는 group algebra의 언어가 유용하다. ([\[대수적 구조\] §대수, ⁋정의 5](/ko/math/algebraic_structures/algebras#def5)) 이를 간단히 리뷰하자면 집합으로서 $\mathbb{C}[G]$는 $G$에서 $\mathbb{C}$로의 함수들의 모임이었다. 각각의 $x\in G$에 대하여 $\delta_x:G\rightarrow \mathbb{C}$를

$$\delta_x(y)=\begin{cases}1&\text{if $y=x$}\\0&\text{otherwise}\end{cases}$$

으로 정의하면, 임의의 $f\in\mathbb{C}[G]$는 

$$f=\sum_{x\in G}f(x)\delta_x$$

로 나타낼 수 있으므로 $\delta_x$들이 $\mathbb{C}[G]$의 basis를 이룬다. 우리가 다룰 $\mathbb{C}[G]$가 단순히 $G$에서 $\mathbb{C}$로의 함수들이 이루는 ring과 같지 않은 부분은 이 위에 정의된 곱셈이다. 두 함수 $f,g$의 곱셈을

$$(fg)(x)=f(x)g(x), \qquad \text{for all $x\in G$}$$

으로 정의하는 대신 이 위에는 convolution product

$$(f\ast g)(x)=\sum_{y\in G}f(y)g(y^{-1}x)$$

가 곱셈을 정의한다. 만일 우리가 위의 delta function $\delta_x$와 $x\in G$를 identify한다면, 다음의 식

$$\left(\sum_{x\in G}f(x)\cdot x\right)\left(\sum_{y\in G} g(y)\cdot y\right)=\sum_{x,y\in G} f(x)g(y) \cdot(xy)=\sum_{z\in G}\left(\sum_{x\in G} f(x)g(x^{-1}z)\right)\cdot z$$

이 성립하므로 이러한 곱셈을 선택하는 것이 자연스럽다. 가령 $\delta_x$와 $\delta_y$의 곱은 $0$이지만, 이 둘의 convolution은 $\delta_{xy}$이므로, group action에 포함되는 다음의 식

$$(\delta_x\ast \delta_y)\cdot v=\delta_x\cdot(\delta_y\ast v)$$

와 같은 것들이 말이 되기 위해서는 이러한 선택이 필연적이다.

임의의 $G$-representation $\rho:G\rightarrow \Aut(V)$에 대하여, 다음의 식

$$\widetilde{\rho}\left(\sum_{x\in G} a_x x, v\right)= \sum_{x\in G} a_x\rho(x)v$$

은 $V$ 위에 $\mathbb{C}[G]$-module 구조를 준다. 거꾸로 임의의 $\mathbb{C}[G]$-module $V$가 주어졌다 하면, 각 $x\in G$에 대하여 $x$가 $V$에 작용하는 방식을 통해 $G$-representation을 얻을 수 있다.

<div class="proposition" markdown="1">

<ins id="prop4">**명제 4**</ins> 위의 대응들은 categorical equivalence

$$\Rep_\mathbb{C}(G)\cong \lMod{\mathbb{C}[G]}$$

을 준다.

</div>

약간의 abuse of language를 통해 우리는 $\mathbb{C}[G]$-module을 간단히 $G$-module이라 부르기도 한다. 근본적으로 임의의 $x\in G$가 임의의 $v\in V$를 어디로 옮기는지만 알면 위의 식을 통해 $\mathbb{C}[G]$-action이 결정된다는 점에서 이 명칭은 상당히 적절하다고 할 수 있다. 

실제로 위에서 논의한 대부분의 것들이 이 categorical equivalence로 설명될 수 있다. 가령 임의의 $G$-representation $V$에 대하여, $V$의 subrepresentation은 $V$의 $G$-submodule (정확히는 $\mathbb{C}[G]$-submodule)이다. 또, [정의 3](#def3)의 tensor product도 납득할만한데, 일반적으로 coproduct $\Delta:A\rightarrow A\otimes A$가 주어진 $\mathbb{K}$-algebra $A$와 두 $A$-module $M,N$에 대하여 이들의 텐서곱을 정의하기 위해서는 $\Delta$를 활용하여 

$$A\otimes (M\otimes N)\rightarrow (A\otimes A)\otimes (M\otimes N)\rightarrow (A\otimes M)\otimes (A\otimes N)\rightarrow M\otimes N$$

을 사용해야 하고, 이 때 사용하는 coproduct $A\rightarrow A\otimes A$이 $\mathbb{C}[G]$의 경우에는 

$$\mathbb{C}[G]\rightarrow \mathbb{C}[G]\otimes \mathbb{C}[G]$$

이기 때문이다. 

특별히 $G$의 subrepresentation과 $\mathbb{C}[G]$-submodule이 같은 것이라는 것을 생각하면, $V$가 irreducible representation인 것은 $V$가 *simple* $\mathbb{C}[G]$-module인 것과 같다. 


이제 우리는 $G$의 representation을 이루는 가장 기본 단위, 곧 irreducible representation이 



핵심은 임의의 inner product를 평균화하여 $G$-invariant한 inner product를 얻는 것이다.

<div class="definition" markdown="1">

<ins id="def5">**정의 5**</ins> $G$-representation $V$ 위의 Hermitian inner product $\langle-,-\rangle$이 *$G$-invariant*라는 것은 임의의 $g\in G$와 $u,v\in V$에 대하여

$$\langle g\cdot u,g\cdot v\rangle=\langle u,v\rangle$$

이 성립하는 것이다. $G$-invariant inner product를 갖는 representation을 *unitary representation*이라 부른다.

</div>

<div class="proposition" markdown="1">

<ins id="thm7">**정리 7 (Maschke)**</ins> Finite group $G$와 $G$-representation $V$가 주어졌다 하고, $V$의 $G$-invariant subspace $W$를 고정하자. 그럼 적당한 $G$-invariant subspace $W'$가 존재하여 $V = W \oplus W'$이도록 할 수 있다. 따라서 귀납적으로 임의의 $G$-representation은 irreducible representation들의 direct sum으로 분해된다.

</div>

<details class="proof" markdown="1">
<summary>증명</summary>

$V$ 위의 임의의 Hermitian inner product $\langle -,- \rangle$에 대하여, [정의 1](#def1)에서의 평균화 연산자와 유사하게 다음의 식

$$\langle\kern-1.5pt\langle u,v\rangle\kern-1.5pt\rangle = \frac{1}{|G|}\sum_{g \in G} \langle g\cdot u, g\cdot v \rangle$$

을 통해 새로운 inner product $\langle\kern-1.5pt\langle-,-\rangle\kern-1.5pt\rangle$를 정의하자. 그럼 임의의 $h\in G$에 대하여

$$\langle\kern-1.5pt\langle h\cdot u, h\cdot v\rangle\kern-1.5pt\rangle = \frac{1}{|G|}\sum_{g \in G} \langle gh\cdot u, gh\cdot v \rangle = \langle\kern-1.5pt\langle u, v\rangle\kern-1.5pt\rangle$$

이므로 이 inner product는 $G$-invariant이다. 이제 $W'$를 $W$의 orthogonal complement로 잡으면, $W'$ 또한 $G$-invariant subspace이며 $V = W \oplus W'$가 성립한다.

</details>



## 나중

이제 group algebra $\mathbb{C}[G]$를 생각하자. 이는 $G$에서 $\mathbb{C}$로의 함수들의 모임이며, 각각의 $g\in G$에 대하여 $\delta_x:G\rightarrow \mathbb{C}$를

$$\delta_x(y)=\begin{cases}1&\text{if $y=x$}\\0&\text{otherwise}\end{cases}$$

으로 정의하면 임의의 $f:G\rightarrow\mathbb{C}$는 다음의 꼴

$$f(y)=\sum_{x\in G} f(x)\delta_x(y)$$

로 나타낼 수 있으므로 $\delta_x$들이 $\mathbb{C}[G]$의 basis를 이룬다. 편의상 우리는 이러한 방식으로 $x\in G$와 $\delta_x\in \mathbb{C}[G]$를 identify한다. 그럼 이 표기 하에서,

$$\left(\sum_{x\in G}f(x)\cdot x\right)\left(\sum_{y\in G} g(y)\cdot y\right)=\sum_{x,y\in G} f(x)g(y) \cdot(xy)=\sum_{z\in G}\left(\sum_{x\in G} f(x)g(x^{-1}z)\right)\cdot z$$

이므로 두 함수 $f$와 $g$의 곱은 convolution으로 주어진다. 때문에 $\mathbb{C}[G]$를 *convolution algebra*라 부르기도 한다. 

그럼 임의의 finite group representation $\rho:G\rightarrow \Aut(V)$에 대하여, 다음의 식

$$\widetilde{\rho}: (\sum_{x\in G} a_x x, v)\mapsto \sum_{x\in G} a_x\rho(x)v$$

은 $V$ 위에 $\mathbb{C}[G]$-module 구조를 준다. 거꾸로 임의의 $\mathbb{C}[G]$-module $V$가 주어졌다 하면, 즉 다음의 함수

$$\mu: \mathbb{C}[G]\times V\rightarrow V$$

가 주어졌다 하면 우리는 다음의 식

$$g\mapsto \left( v\mapsto \mu(\delta_x, v)\right)$$

을 통해 이를 $G$의 representation $G\rightarrow \Aut(V)$로 볼 수 있다. 이들 두 대응은 categorical equivalence

$$\Rep_\mathbb{C}(G)\cong \lMod{\mathbb{C}[G]}$$

을 준다. 



## 리 군의 표현론

<div class="definition" markdown="1">

<ins id="def1">**정의 1**</ins> Lie group $G$의 *representation<sub>표현</sub>*은 continuous action

$$\rho:G\times V \rightarrow V$$

중, 각각의 $g\in G$를 고정했을 때 $\rho(g,-)$가 linear map인 것이다. 

</div>

즉 Lie group automorphism은 언제나와 같이 homomorphism $G\rightarrow \Aut(V)$를 의미한다. 우리는 이 글에서 $V$가 유한차원 벡터공간이며, 그 base field는 $\mathbb{K}=\mathbb{C}$로 고정하기로 한다. 그럼 $V$ 위에 basis를 택하면, $\Aut(V)\cong \GL(n;\mathbb{C})$이므로 이러한 representation을 *matrix representation*이라 부르기도 한다. 

가장 단순한 예시는 trivial representation $\rho(g)=I$ (항상 항등변환)와 standard representation (e.g., $S_n$의 permutation matrix)이다. 





우리가 표현론을 다룰 때는 크게 두 가지 맥락을 생각할 수 있다. 하나는 위에서 언급한 것처럼 Lie group의 표현을 다루는 것이고, 또 다른 하나는 finite group의 표현을 다루는 것이다. 이들은 서로 유사한 정리들을 공유하며, finite group에서 먼저 익힌 직관들이 compact Lie group의 경우로 자연스럽게 확장된다. 따라서 우리는 먼저 finite group의 경우를 살펴 본 후, 이를 compact Lie group으로 일반화할 것이다.

## Finite Group의 표현

우선 *finite* group $G$와 $\mathbb{C}$ 위의 finite-dimensional vector space $V$를 생각하자. $G$의 *representation*은 group homomorphism

$$\rho: G \longrightarrow \Aut(V) \cong \GL(n;\mathbb{C})$$

을 의미한다. 이는 각각의 $g \in G$가 $V$ 위의 invertible linear operator로 작용함을 의미하며, $G$의 group structure가 $\Aut(V)$의 곱셈과 호환됨을 요구한다.

<div class="proposition" markdown="1">

<ins id="thm-finite-maschke">**정리 (Maschke)**</ins> Finite group $G$와 $G$-module $V$가 주어졌다 하고, $V$의 $G$-submodule $W$를 고정하자. 그럼 적당한 $G$-submodule $W'$가 존재하여 $V = W \oplus W'$이도록 할 수 있다. 따라서 귀납적으로 임의의 $G$-module은 irreducible $G$-module들의 direct sum이다.

</div>

<details class="proof" markdown="1">
<summary>증명</summary>

$V$ 위의 임의의 Hermitian inner product $\langle -,- \rangle$에 대하여 다음의 식

$$\langle\kern-1.5pt\langle u,v\rangle\kern-1.5pt\rangle = \frac{1}{|G|}\sum_{g \in G} \langle gu, gv \rangle$$

을 통해 이를 평균내주면 $G$-invariant Hermitian inner product를 정의할 수 있다. 즉 모든 $g \in G$에 대하여 $\langle\kern-1.5pt\langle gu, gv\rangle\kern-1.5pt\rangle = \langle\kern-1.5pt\langle u, v\rangle\kern-1.5pt\rangle$이 성립한다. 이제 $W'$를 $W$의 orthogonal complement로 잡으면 된다.

</details>

Representation $\rho: G \rightarrow \Aut(V)$가 주어졌을 때, 이에 대응하는 *character* $\chi_\rho: G \rightarrow \mathbb{C}$는 다음과 같이 정의된다.

$$\chi_\rho(g) = \tr(\rho(g))$$

즉 각 $g \in G$가 $V$에 작용하는 linear operator의 trace를 대응시키는 함수이다. Character는 conjugacy class 위에서 상수값을 가지며, representation이 isomorphic할 때 같은 character를 갖는다.

<div class="definition" markdown="1">

<ins id="def-class-func">**정의**</ins> 함수 $f: G \rightarrow \mathbb{C}$가 *class function*이라는 것은 $G$의 각각의 conjugacy class 위에서 이 함수가 상수인 것이다.

</div>

Character function들의 가장 중요한 성질 중 하나는 *Schur orthogonality relation*이다. Finite group의 경우 이는 다음과 같이 표현된다. Irreducible representation들 $\rho_i$에 대응하는 character들 $\chi_i$가 주어졌을 때,

$$\frac{1}{|G|}\sum_{g \in G} \chi_i(g)\overline{\chi_j(g)} = \delta_{ij}$$

가 성립한다. 이는 서로 다른 irreducible representation의 character들이 평균내어진 내적에서 orthogonal함을 의미한다.

## Compact Lie Group의 표현

이제 $G$를 *compact* Lie group으로 바꾸어보자. Finite group에서 compact Lie group으로 넘어갈 때, 우리가 해야 할 유일한 수정은 *평균*을 취하는 방식을 바꾸는 것뿐이다. Finite group에서는 $\frac{1}{|G|}\sum_{g \in G}$로 평균을 내었지만, compact Lie group에서는 *Haar measure*를 사용한 적분으로 대체된다.

Compact topological group $G$ 위에는 left-invariant (또는 right-invariant) probability measure, 즉 Haar measure가 항상 존재하며 유일하다. 편의상 $G$ 위에 정의된 Haar measure에 대한 적분을

$$\int_G f(g)\mathop{dg}$$

와 같이 쓰기로 하자. 이는 Haar measure가 확률측도(total mass 1)로 정규화되었다는 것을 의미한다.

<div class="definition" markdown="1">

<ins id="def4">**정의 4**</ins> 임의의 $G$-module $V$에 대하여, $V$ 위에 정의된 Hermitian inner product $\langle-,-\rangle$이 *$G$-invariant*라는 것은 $\langle g\cdot u,g\cdot v\rangle=\langle u,v\rangle$이 모든 $u,v,g$에 대해 성립하는 것이다. 만일 $V$가 $G$-invariant Hermitian inner product를 갖는다면 이를 *unitary representation*이라 부른다. 

</div>

<div class="proposition" markdown="1">

<ins id="thm5">**정리 5**</ins> 임의의 compact group $G$와 $G$-module $V$에 대하여, $V$ 위의 임의의 Hermitian inner product $\langle-,-\rangle$에 대하여 다음의 식

$$\langle\kern-1.5pt\langle u,v\rangle\kern-1.5pt\rangle=\int_G \langle gu,gv\rangle \mathop{dg}$$

을 통해 이를 평균내주면 $G$-invariant Hermitian inner product를 정의할 수 있다. 즉, $V$는 항상 unitary representation이다. 

</div>

<div class="proposition" markdown="1">

<ins id="prop6">**명제 6**</ins> Compact group $G$와 $G$-module $U$가 주어졌다 하고, $U$의 $G$-submodule $V$를 고정하자. 그럼 적당한 $G$-submodule $W$가 존재하여 $U=V\oplus W$이도록 할 수 있으며, 따라서 귀납적으로 임의의 $G$-module은 irreducible $G$-module들의 direct sum이다. 

</div>

이에 대한 증명은 [정리 5](#thm5)에서 정의한 $G$-invariant inner product를 사용하여 $W$를 $V$의 orthogonal complement로 잡으면 된다. 이것이 바로 finite group에서의 [Maschke 정리](#thm-finite-maschke)와 완전히 동일한 구조임을 알 수 있다.

<div class="proposition" markdown="1">

<ins id="lem7">**보조정리 7**</ins> (Compact) group $G$와 irreducible $G$-module들 $V,W$가 주어졌다 하자. 그럼 다음이 성립한다. 

1. 임의의 $G$-map $V\rightarrow W$는 zero map이거나 isomorphism이다. 
2. 임의의 $G$-automorphism $f\in \Aut_G(V)$는 $f(v)=\lambda v$의 꼴이다. 
3. $G$-map들의 모임 $\Hom_G(V,W)$은 $\mathbb{C}$이거나 $0$이다. 

</div>
<details class="proof" markdown="1">
<summary>증명</summary>

1. 이는 kernel과 image를 각각 생각하면 자명하다. 
2. 주어진 $f$는 $G$-linear map이기 이전에 $\mathbb{C}$-linear map이므로, $f$의 eigenvalue $\lambda$가 존재한다. 이제 이 eigenvalue에 대응되는 eigenspace를 $W$라 하고, 이것이 실은 $G$-submodule이 됨을 보이면 된다. 
3. 위의 두 명제에 의해 자명하다. 

</details>

우리가 생각할 수 있는 가장 단순한 경우, 즉 $G$가 (compact) abelian Lie group인 경우, 임의의 $G$-module $V$의 임의의 subspace는 $G$-invariant이다. 따라서 abelian Lie group의 irreducible representation은 반드시 $1$차원이다.

**예시 (SU(2))**: Fundamental rep는 2차원, spin $j=1/2$. Character 계산으로 irrep 분해 가능.

이제 임의의 compact Lie group $G$에 대하여, irreducible $G$-module들의 isomorphism class들의 집합 $\Irr(G, \mathbb{C})$를 생각하자. 그럼 임의의 $W\in \Irr(G, \mathbb{C})$에 대하여, 다음의 함수

$$d_W:\Hom_G(W,V)\otimes_\mathbb{C}W\rightarrow V; \qquad \varphi\otimes w\mapsto \varphi(w)$$

는 잘 정의되며 $G$-map임을 보일 수 있다. 이 때 $\Hom_G(W,V)\otimes W$는 다음의 식

$$g\cdot(\varphi\otimes w)=\varphi\otimes(g\cdot w)$$

을 통해 $G$-action이 주어지는 $G$-module이다. 그럼 다음이 성립한다. 

<div class="proposition" markdown="1">

<ins id="prop8">**명제 8**</ins> 위와 같은 상황에서, 다음의 함수 

$$d=\bigoplus_{W\in\Irr(G, \mathbb{C})} d_W:\bigoplus_{W\in \Irr(G, \mathbb{C})}\Hom_G(W,V)\otimes_\mathbb{C}W\rightarrow V$$

는 isomorphism이다. 

</div>

이에 대한 증명은 만일 $V$가 "irreducible decomposition" $V=\bigoplus V_j$을 갖는다면, 다음의 식

$$\Hom_G(W, V)=\Hom_G\left(W, \bigoplus V_j\right)\cong \bigoplus \Hom_G(W, V_j) $$

과 [보조정리 7](#lem7)에 의해 자명하다. 즉 복잡하게 써 두기는 했지만, 위의 $d$는 각각의 irreducible $G$-module $W$(의 isomorphism class)들이 $V$ 안에 얼마나 들어있는지를 세는 것이며, 따라서 다음 정의가 자연스럽다. 

<div class="definition" markdown="1">

<ins id="def9">**정의 9**</ins> 위의 함수에 의한 $W\in\Irr(G, \mathbb{C})$의 image를 $V$의 *$W$-isotypical summand*라 부르고, $\Hom_G(W, V)$를 $W$의 *multiplicity*라 부른다. 

</div>

약간의 믿음을 가지면 이러한 표현이 유일하다는 것도 납득할 수 있다. 한편, 우리는 위의 $d_W$를 정의할 때 이미 $G$-action이 정의되어있는 $V.W$로부터 새로운 $G$-module 위에 $G$-action을 정의했는데, 이는 선형대수에서의 construction으로 만들어지는 벡터공간 위에 $G$-action만 추가한 것이다. 이들 action을 정의하는 것 또한 자연스럽겠지만, 혼란을 피하기 위해 적어둔다. 

<div class="definition" markdown="1">

<ins id="def10">**정의 10**</ins> $G$-module $V,W$에 대하여 다음의 action을 통해 새로운 $G$-module들을 정의한다. 

1. Direct sum $V\oplus W$; $G$-action $g\cdot(v,w)=(g\cdot v,g\cdot w)$
2. Tensor product $V\otimes W$; $G$-action $g\cdot(v\otimes w)=(g\cdot v)\otimes (g\cdot w)$
3. $\Hom_\mathbb{C}(V,W)$; $G$-action $g\cdot f=L_g\circ f\circ L_{g^{-1}}$[^1]
4. 3번에서 $W=\mathbb{C}$로 두어 얻어지는 dual representation
5. 스칼라곱을 conjugate으로 바꾸어 얻어지는 *conjugate representation*
6. 그 외 exterior power, symmetric power 등에 비슷하게 정의되는 $G$-action들.

</div>

## 표현의 지표

**Schur Orthogonality 예시 ($S_3$)**:

| irrep | dim | $\chi(id)$ | $\chi((12))$ | $\chi((123))$ |
|-------|-----|------------|--------------|---------------|
| Triv  | 1   | 1          | 1            | 1             |
| Sign  | 1   | 1          | -1           | 1             |
| Std   | 2   | 2          | 0            | -1            |

내적 $\langle \chi_i, \chi_j \rangle = \frac{1}{6} \sum \chi_i \bar{\chi_j} = \delta_{ij}$.

이제 우리는 표현의 지표<sub>character</sub>에 대해 살펴 보겠다. 간단히 말해서 이는 임의의 $G$-representation $\rho:G\rightarrow \Aut_\mathbb{C}(V)$가 주어졌을 때, $G$의 임의의 원소 $g\in G$가 $V$에 act하는 것 (즉 $\rho(g)$의 행렬표현)의 trace를 대응시켜주는 함수 $\chi_\rho:G\rightarrow \mathbb{C}$이다. 이는 그 이름이 시사하는 바와 같이, 임의의 $G$-representation을 characterize하는 대상이다. 즉, 서로 같은 character function을 갖는 representation은 isomorphic하다. 뿐만 아니라, character function은 conjugacy class 위에서 같은 값을 지정한다. 

임의의 character function이 class function인 것은 trace의 성질에 의해 자명하다. 뿐만 아니라 character function은 class function들의 vector space의 basis가 되는데, 이는 가령 다음의 식

$$\chi_{V\oplus W}=\chi_V+\chi_W, \quad \chi_{V\otimes W}=\chi_V \chi_W$$

에 의한 것이다. 그렇다면 class function들의 벡터공간에서의 projection 등이 어떻게 정의되는지를 탐구할 수 있을 것인데, 이러한 종류의 관계식을 *Schur orthogonality relation*이라 부른다. 

## 리 대수의 표현

우리는 Lie group의 infinitesimal한 정보가 모두 그 Lie algebra에 들어있는 것을 알고, 적당한 위상적인 조건들 하에서 Lie algebra의 정보는 Lie group을 복원해내는데에 충분하다는 것을 안다. 그렇다면, 적어도 철학적으로는 Lie group의 representation의 infinitisimal한 정보를 Lie algebra의 representation에 담아줄 수 있을 것이다. 그리고 이는 정당한 직관이다. 

임의의 $G$-module $V$가 주어졌다 하자. 그럼 $V$를 manifold로 본다면, 우리는 임의의 $X\in \mathfrak{g}$와 임의의 $v\in V$에 대하여, $v$에서 출발하여 $X$가 지정해주는 방향으로 움직이는 곡선 

$$t\mapsto\exp(tX)\cdot v$$

이 존재함을 안다. 그럼 이 action의 infinitesimal한 정보는 다음의 식

$$\mathcal{L}_X v:=\lim_{t \rightarrow 0}\frac{\exp(tX)\cdot v-v}{t}$$

에 담겨있는 것을 안다. 만일 우리가 $G$-module $V$를 $\rho:G\rightarrow \Aut(V)$로 해석한다면, 우변은 $\Aut(V)$의 Lie algebra에 해당하는 $\End(V)$의 원소이며, 더 나아가 $d\rho_e(X)$가 된다는 것을 안다. 즉 다음의 대응

$$\mathfrak{g}\times V \rightarrow V;\qquad (X,v)\mapsto \mathcal{L}_Xv$$

은 $G\times V \rightarrow V$의 infinitesimal한 버전으로 생각할 수 있으며, 이 대응은 그 자체로 *Lie algebra의 representation*을 준다. 여기서, 임의의 Lie algebra $L$과 벡터공간 $V$에 대하여 $L\times V \rightarrow V$가 Lie algebra representation이기 위해 우리가 요구하는 관계식은

$$X(Yv)-Y(Xv)=[X,Y]v$$

이다. 약간의 믿음을 가지면 simply connected Lie group $G$과 그 Lie algebra $\mathfrak{g}$에 대해서는 ([§리 군, ⁋정리 15](/ko/math/Lie_theory/Lie_groups#thm15)와 마찬가지 결과로) Lie algebra representation $\mathfrak{g}\times V \rightarrow V$이 Lie group의 representation $G\times V \rightarrow V$를 결정하는 것도 납득할 수 있다. 

이는 root systems나 Weyl group 등 후속 주제로 이어진다. 
