---

title: "리 군의 표현"
excerpt: ""

categories: [Math / Lie Theory]
permalink: /ko/math/lie_theory/representations
header:
    overlay_image: /assets/images/Math/Lie_Theory/Representations.png
    overlay_filter: 0.5
sidebar: 
    nav: "Lie_theory-ko"

date: 2025-11-24
last_modified_at: 2025-11-24
weight: 2

---

## 표현론의 철학

일반적으로 그 구조가 복잡한 수학적인 대상을 다룰 때 좋은 전략 중 하나는 이 대상이 다른 단순한 대상 위에 어떻게 act하는지를 보는 것이다. Lie group의 경우 이러한 철학은 더 각별한데, Lie group의 대표적인 예시인 $\GL(n;\mathbb{R})$이나 $\Diff(M)$ 등을 생각하면 이들은 그 본질부터가 다른 대상 위에 act하는 것이기 때문이다. 이번 글에서 우리는 Lie group의 finite-dimensional representation을 살펴본다. 

<div class="definition" markdown="1">

<ins id="def1">**정의 1**</ins> Lie group $G$의 *representation<sub>표현</sub>*은 continuous action

$$\rho:G\times V \rightarrow V$$

중, 각각의 $g\in G$를 고정했을 때 $\rho(g,-)$가 linear map인 것이다. 

</div>

즉 Lie group automorphism은 언제나와 같이 homomorphism $G\rightarrow \Aut(V)$를 의미한다. 우리는 이 글에서 $V$가 유한차원 벡터공간이며, 그 base field는 $\mathbb{K}=\mathbb{C}$로 고정하기로 한다. 

그럼 $V$ 위에 basis를 택하면, $\Aut(V)\cong \GL(n;\mathbb{C})$이므로 이러한 representation을 *matrix representation*이라 부르기도 한다. 

기본적으로 representation theory는 적절한 algebra 위에서의 module theory로 생각할 수 있다. 우리의 경우 이 역할을 해 줄 것은 group ring $\mathbb{C}[G]$이다. ([\[대수적 구조\] §대수, ⁋정의 5](/ko/math/algebraic_structures/algebras#def5))

충분한 motivation을 주기 위해, 위의 링크에서 정의한 group ring 가운데 특별히 *finite* group $G$와 commutative ring $A$으로 정의된 group ring $A[G]$를 생각하자. 정의에 의해 $A[G]$는 $G$에서 $A$로 가는 모든 함수들의 모임이며, 이 함수들의 덧셈과 곱셈은 자명한 방식으로 정의된다. 한편 우리는 임의의 함수 $f\in A[G]$에 대하여, 이를 다음의 식

$$f=\sum_{x\in G} f(x)\delta_x$$

으로 쓸 수 있다. 여기서 $f(x)$는 $A$의 원소이고 $\delta_x$는 Kronecker delta이다. 편의상 이를 더 간략하게

$$f=\sum_{x\in G}f(x)\cdot x$$

으로 쓰기도 한다. 이 표기 하에서 함수들의 곱셈을 나타내면 다음의 합성곱

$$\left(\sum_{x\in G}f(x)\cdot x\right)\left(\sum_{y\in G} g(y)\cdot y\right)=\sum_{x,y\in G} f(x)g(y) \cdot(xy)=\sum_{z\in G}\left(\sum_{x\in G} f(x)g(x^{-1}z)\right)\cdot z$$

을 얻는다. 

여전히 $G$가 finite group임을 가정한 상태로, representation $G \rightarrow \Aut(V)$가 주어졌다 하자. 그럼 우리는 다음의 식

$$v\mapsto \left(\sum_{x\in G}a_xx\right)\cdot v=\sum_{x\in G}a_x(x\cdot v)$$

을 통해 이 representation을 확장할 수 있다. 즉, $V$는 위의 식을 통해 $\mathbb{C}[G]$-module로 볼 수 있다. 

이제 $G$의 유한 조건을 없애야 한다. [\[대수적 구조\] §대수, ⁋정의 5](/ko/math/algebraic_structures/algebras#def5)에서는 이를 위해 finitely supported function들만 생각했지만, 우리 경우에는 $G$의 위상구조를 사용하면 이를 다루는데에 문제가 없다. 즉, 우리의 기본적인 철학은 위에서, 

- $G$를 (compact) Lie group으로 바꾸고, 
- 모든 함수들 $G\rightarrow \mathbb{C}$ 대신 연속함수들 $G\rightarrow \mathbb{C}$을 생각하고,
- 무한합은 적분으로 바꾸는 것이다. 

이 때 적분을 위해서는 $G$ 위에 정의된 measure가 필요한데, 이는 $G$가 compact topological group이기만 해도 Haar measure의 존재성이 보장되므로 문제가 없다. 약간의 abuse of language를 통해 이러한 $V$를 더 간단히 $G$-module이라 부르자. 또, 편의상 $G$ 위에 정의된 Haar measure에 대한 적분을

$$\int_G f(g)\mathop{dm(g)}$$

와 같은 표기 대신 간단히 

$$\int_G f(g)\mathop{dg}$$

처럼 쓰기로 한다. 

## 표현론의 기본적인 결과들

위와 같은 철학을 받아들인 후, 두 $G$-module $V,W$를 생각하자. 그럼 우리는 $G$-module들의 category에서의 morphism이 무엇인지 정의할 수 있다. 

<div class="definition" markdown="1">

<ins id="def3">**정의 3**</ins> 두 $G$-module $V,W$ 사이의 linear map $f:V \rightarrow W$이 *$G$-linear*라는 것은 $f$가 $G$-equivariant인 것이다. 즉 다음의 식

$$f(g\cdot v)=g\cdot f(v)$$

이 모든 $g\in G$와 모든 $v\in V$에 대해 성립하는 것이다. 

</div>

이러한 방식을 통해 $G$-action을 모두 선형대수로 취급하려 한다면, 좋은 도구 중 하나는 이 위에 정의된 inner product일 것이다.

<div class="definition" markdown="1">

<ins id="def4">**정의 4**</ins> 임의의 $G$-module $V$에 대하여, $V$ 위에 정의된 Hermitian inner product $\langle-,-\rangle$이 *$G$-invariant*라는 것은 $\langle g\cdot u,g\cdot v\rangle=\langle u,v\rangle$이 모든 $u,v,g$에 대해 성립하는 것이다. 만일 $V$가 $G$-invariant Hermitian inner product를 갖는다면 이를 *unitary representation*이라 부른다. 

</div>

만일 $G$가 compact group이라면, $V$ 위의 임의의 Hermitian inner product $\langle-,-\rangle$에 대하여 다음의 식

$$\langle\kern-1.5pt\langle u,v\rangle\kern-1.5pt\rangle=\int_G \langle gu,gv\rangle \mathop{dg}$$

을 통해 이를 평균내주면 $G$-invariant Hermitian inner product를 정의할 수 있다. 즉 다음이 성립한다. 

<div class="proposition" markdown="1">

<ins id="thm5">**정리 5**</ins> 임의의 compact group $G$와 $G$-module $V$에 대하여, $V$는 항상 unitary representation이다. 

</div>

임의의 $G$-module이 주어졌을 때, 그 $G$-submodule, 혹은 더 정확하게 $G$-subrepresentation은 자명한 방식으로 정의할 수 있다. 만일 $V$가 nontrivial한 $G$-submodule을 갖지 않는다면 이를 *irreducible*이라 부른다. 그럼 다음 명제는 앞선 정리로부터 자명한 것이다. 

<div class="proposition" markdown="1">

<ins id="prop6">**명제 6**</ins> Compact group $G$와 $G$-module $U$가 주어졌다 하고, $U$의 $G$-submodule $V$를 고정하자. 그럼 적당한 $G$-submodule $W$가 존재하여 $U=V\oplus W$이도록 할 수 있으며, 따라서 귀납적으로 임의의 $G$-module은 irreducible $G$-module들의 direct sum이다. 

</div>

이에 대한 증명은 $U$ 위에 $G$-invariant inner product를 하나 잡은 후, $W$를 $V$의 orthogonal complement로 잡으면 된다. 이것이 단순한 analogue가 아니라 실제로 잘 행동하는 것임은 직접 보여야 하는 것이기는 하지만, 선형대수학에서의 증명과 정확히 똑같으므로 생략하기로 한다. 

다음 보조정리는 irreducible representation을 분류해준다는 점에서 그 유용함이 자명하다. 

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

이제 우리는 표현의 지표<sub>character</sub>에 대해 살펴본다. 간단히 말해서 이는 임의의 $G$-representation $\rho:G\rightarrow \Aut_\mathbb{C}(V)$가 주어졌을 때, $G$의 임의의 원소 $g\in G$가 $V$에 act하는 것 (즉 $\rho(g)$의 행렬표현)의 trace를 대응시켜주는 함수 $\chi_\rho:G\rightarrow \mathbb{C}$이다. 이는 그 이름이 시사하는 바와 같이, 임의의 $G$-representation을 characterize하는 대상이다. 즉, 서로 같은 character function을 갖는 representation은 isomorphic하다. 뿐만 아니라, character function은 conjugacy class 위에서 같은 값을 지정한다. 

<div class="definition" markdown="1">

<ins id="def11">**정의 11**</ins> 함수 $G\rightarrow \mathbb{C}$가 *class function*이라는 것은 $G$의 각각의 conjugacy class들 위에서 이 함수가 상수인 것이다. 

</div>

임의의 character function이 class function인 것은 trace의 성질에 의해 자명하다. 뿐만 아니라 character function은 class function들의 vector space의 basis가 되는데, 이는 가령 다음의 식

$$\chi_{V\oplus W}=\chi_V+\chi_W$$

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