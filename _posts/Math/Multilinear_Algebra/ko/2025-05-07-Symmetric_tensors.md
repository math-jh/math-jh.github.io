---

title: "대칭텐서"
excerpt: ""

categories: [Math / Multilinear Algebra]
permalink: /ko/math/multilinear_algebra/symmetric_tensors
header:
    overlay_image: /assets/images/Math/Multilinear_Algebra/Symmetric_tensors.png
    overlay_filter: 0.5
sidebar: 
    nav: "multilinear_algebra-ko"

date: 2025-05-07
last_modified_at: 2025-05-07
weight: 201

---


임의의 group $H$와 ring $A$가 주어졌을 때, 우리는 group ring $AH$를 정의하였다. ([\[대수적 구조\] §대수, ⁋정의 5](/ko/math/algebraic_structures/algebras#def5)) 이제 $AH$-module $M$을 고정하고, $M^H$를 다음의 집합

$$M^H=\left\{x\in M\mid \text{$hx=x$ for all $h\in H$}\right\}$$

으로 정의하자. 여기서 $hx$는 당연히, $h\mapsto \delta_h$를 통해 $h$를 $AH$의 원소로 본 후, $AH$-module 구조를 이용하여 정의된 것이다. 그럼 $M^H$는 $M$의 $A$-submodule이지만, group $H$가 commutative가 아니라면 일반적으로 $AH$-submodule이 되지는 않는다. 또, 만일 $H$의 subgroup $G$가  주어졌다면 $M^H\leq M^G$임이 자명하다. 

이제 $x\in M^G$와 $h\in H$가 주어졌다 하고, $H/G$의 원소 $\bar{h}=hG$가 주어졌다 하자. 그럼 

$$\bar{h}x=(hG)x=\left\{hx\right\}$$

인 것이 자명하므로, 약간의 abuse of notation을 통해 $hx$와 $\bar{h}x$를 같은 것으로 취급하여도 된다. 그럼 임의의 $h'\in H$에 대하여, 다음의 식

$$h'(\bar{h}x)=(h'\bar{h})x$$

이 성립한다. 

이제 $[H:G]$가 유한이라 가정하자. 그럼 $H/G$는 유한집합이며, 따라서 다음의 합

$$\sum_{\bar{h}\in H/G}\bar{h}x$$

이 잘 정의된다. 뿐만 아니라 이 합은 $M^H$의 원소인데, 임의의 $h'\in H$에 대하여 

$$h'\left( \sum_{\bar{h}\in H/G}\bar{h}x\right)=\sum_{\bar{h}\in H/G}(h'\bar{h})x=\sum_{\bar{z}\in H/G}\bar{z}x$$

이기 때문이다. 

<div class="definition" markdown="1">

<ins id="def1">**정의 1**</ins> 위와 같은 상황에서, $\tr_{H/G}:M^G \rightarrow M^H$를 다음의 식

$$\tr_{H/G}(x)=\sum_{\bar{h}\in H/G} \bar{h}x$$

으로 정의하고, 이를 *relative trace*라 부른다. 

</div>

그럼 다음이 성립한다. 

<div class="proposition" markdown="1">

<ins id="prop2">**명제 2**</ins> 다음이 성립한다.

1. 임의의 $x\in M^G$와 $h\in H$에 대하여, $hx\in M^{hGh^{-1}}$이고 식 $\tr_{H/hGh^{-1}}(hx)=\tr_{H/G}(x)$이 성립한다. 
2. Subgroup들 $F\leq G\leq H$에 대하여, $\tr_{H/G}\circ\tr_{G/F}=tr_{H/F}$가 성립한다. 
3. 임의의 $x\in M^H$에 대하여, $\tr_{H/G}(x)=[H:G].x$가 성립한다. 

</div>

## 대칭텐서

이제 본격적인 정의를 시작한다. 우선 임의의 $A$-module $M$에 대하여, $n$-th tensor power $\T^n(M)$ 위에 $S_n$-action을 다음의 식

$$\sigma(x_1\otimes x_2\otimes \cdots \otimes x_n)=x_{\sigma^{-1}(1)}\otimes \cdots \otimes x_{\sigma^{-1}(n)}$$

으로 정의할 수 있다. 

<div class="definition" markdown="1">

<ins id="def3">**정의 3**</ins> 위와 같은 상황에서, 

$$\sigma z=z\qquad\text{for all $\sigma\in S_n$}$$

을 만족하는 $z\in \T^nM$들을 $n$th *symmetric tensor<sub>대칭텐서</sub>*라 부르고, 이들의 모임 $\Sym^n(M)$을 $n$-th *symmetric power*라 부른다. 이들의 (graded) direct sum을

$$\Sym(M)=\bigoplus_{d=0}^\infty \Sym^d(M)$$

으로 적는다. 

</div>

$\Sym(M)$은 앞서 정의했던 symmetric algebra $\S(M)$과는 구별해야 하지만, 좋은 경우에는 이들 둘이 서로 isomorphic하다는 것을 보일 수 있다. 

우선 두 symmetric tensor의 곱을 정의하자. 일반적으로 임의의 두 symmetric tensor

$$x=x_1\otimes x_2\otimes \cdots \otimes x_p,\qquad y=y_1\otimes y_2\otimes \cdots \otimes y_q$$

를 가져왔을 떄, 이들의 텐서로서의 곱

$$x\otimes y=x_1\otimes x_2\otimes \cdots \otimes x_p\otimes y_1\otimes y_2\otimes \cdots \otimes y_q$$

이 symmetric tensor가 될 것이라는 보장은 없다. 간단히 위의 꼴에서 $x_i$와 $y_j$의 위치를 서로 바꾸는 원소를 생각하면 이것이 symmetric tensor의 조건을 만족하지 않을 수도 있기 대문이다. 

대신 위의 형태의 곱은 $S_{p+q}$의 subgroup $S_p\times S_q$의 action에 대해서는 invariant하다. 따라서 

$$xy=\tr_{S_{p+q}/S_p\times S_q}(x\otimes y)$$

으로 정의하면 $xy\in M^{S_{p+q}}$이고 그 값은 

$$\sum_{S_{p+q}/(S_p\times S_q)} \bar{\sigma}(x\otimes y)$$

이다. 한편, $S_{p,q}$를 다음의 식

$$\sigma(1)<\sigma(2)< \cdots < \sigma(p), \qquad \sigma(p+1)<\sigma(p+2)<\cdots< \sigma(p+q)$$

를 만족하는 $\sigma$들로 이루어진 $S_{p+q}$의 부분집합이라 하면 어렵지 않게 $S_{p+q}/S_p\times S_q$와 $S_{p,q}$ 사이의 bijection을 찾을 수 있다. 이는 꽤나 자연스러운 것이, $S_p\times S_q$의 원소들은 automorphism의 치역을 고정해놓은 후, 그 안에서의 permutation은 마음대로 움직여도 되는 원소들이고 $S_{p,q}$의 원소들은 반대로 automorphism의 치역은 마음대로 택하되 그 안에서의 permutation은 하나로 고정한 것들이기 때문이다. 따라서 위의 식은 다시

$$xy=\sum_{\sigma\in S_{p,q}}\sigma(x\otimes y)$$

으로 적을 수 있다. 

<div class="proposition" markdown="1">

<ins id="prop4">**명제 4**</ins> 임의의 $A$-module $M$에 대하여 다음이 성립한다.

1. $\Sym(M)$은 위에서 정의한 곱셈에 의해 associative, commutative unital $A$-algebra가 된다. 
2. 양의 정수 $p_1,\ldots, p_n$에 대하여, 다음의 식
    
    $$x_1x_2\cdots x_n=\tr_{S_{p_1+\cdots+p_n}/S_{p_1}\times\cdots\times S_{p_n}}(x_1\otimes \cdots\otimes x_n)$$

    이 성립한다.

</div>
<details class="proof" markdown="1">
<summary>증명</summary>

둘째 주장부터 보이자. 귀납법으로 진행한다. $n=2$일 때는 정의와 같으므로, 귀납적으로

$$x_2\cdots x_n=\tr_{S_{p_2+\dots+p_n}/(S_{p_2}\times\cdots\times S_{p_n})}(x_2 \otimes \dots \otimes x_n)$$

이 성립한다고 가정하자. 이제 $S_{p_1+\cdots+p_n}$의 subgroup들의 tower

$$S_{p_1+\cdots+p_n}\geq S_{p_1}\times S_{p_2+\cdots p_n}\geq \left\{\id_{p_1}\right\}\times S_{p_2+\cdots+p_n}$$

을 생각하면, [명제 2](#prop2)의 결과에 의하여

$$\tr_{S_{p_1+\cdots +p_n}/S_{p_2+\cdots +p_n}}(x_1\otimes\cdots\otimes x_n)=\tr_{S_{p_1+\cdots+p_n}/(S_{p_1}\times S_{p_2+\cdots+p_n})}\circ\tr_{(S_{p_1}\times S_{p_2+\cdots+p_n})/S_{p_2+\cdots+p_n}}(x_1\otimes\cdots\otimes x_n)$$

이 성립한다. 이제 우변을 계산하면, 위의 포함관계에 의해

$$\tr_{(S_{p_1}\times S_{p_2+\cdots+p_n})/S_{p_2+\cdots+p_n}}(x_1\otimes\cdots\otimes x_n)=x_1\otimes\tr_{S_{p_2+\cdots+p_n}/(S_{p_2}\times\cdots\times S_{p_n})}(x_2\otimes\cdots\otimes x_n)=x_1\otimes (x_2\cdots x_n)$$

이고 따라서

$$\tr_{S_{p_1+\cdots +p_n}/S_{p_2+\cdots +p_n}}(x_1\otimes\cdots\otimes x_n)=\tr_{S_{p_1+\cdots+p_n}/(S_{p_1}\times S_{p_2+\cdots+p_n})}(x_1\otimes (x_2\cdots x_n))=x_1(x_2\cdots x_n)$$

이 성립한다. 만일 처음 시작을 다음 subgroup들의 tower

$$S_{p_1+\cdots+p_n}\geq S_{p_1+\cdots p_{n-1}}\times S_{p_n}\geq S_{p_1+\cdots p_{n-1}}\times 1$$

로 시작했다면 

$$\tr_{S_{p_1+\cdots +p_n}/S_{p_2+\cdots +p_n}}(x_1\otimes\cdots\otimes x_n)=(x_1\cdots x_{n-1})x_n$$

을 얻을 것이며 특히 $n=3$인 경우에는 이로부터 $\Sym(M)$의 associativity가 보여진다. Commutativity의 경우, $\sigma$를 $p_1+p_2$개의 원소 중, 앞의 $p_1$개의 원소와 뒤의 $p_2$개의 원소를 다음의 꼴

$$\underbrace{p_2+1,\cdots p_2+p_1}_\text{\scriptsize$p_1$ elements},\qquad \underbrace{1,\ldots, p_2}_\text{\scriptsize$p_2$ elements}$$

로 배열하는 $\sigma\in S_{p_1+p_2}$를 사용하여 [명제 2](#prop2)의 첫째 결과를 사용하면 된다. Unit은 당연하게 $1\in \Sym^0(M)$이다.

</details>

임의의 $x\in M$과 $k\in \mathbb{N}$에 대하여, 

$$\gamma_k(x)=\underbrace{x\otimes\cdots\otimes x}_\text{\scriptsize $k$ times}$$

으로 정의하자. 그럼 위의 명제를 사용하여 계산하면 다음의 따름정리를 얻는다.

<div class="proposition" markdown="1">

<ins id="cor5">**따름정리 5**</ins> 다음이 성립한다. 

1. [명제 4](#prop4)에서 정의한 $x$의 곱 $x^k$는 $p!\gamma_k(x)$와 같다. 
2. 임의의 $x_1,\ldots, x_n\in M$에 대하여,
    
    $$\gamma_p(x_1+\cdots+x_n)=\sum_{p_1+\cdots+p_n=p}\gamma_{p_1}(x_1)\cdots\gamma_{p_n}(x_n)$$

    이 성립한다. 
3. 임의의 $x_1,\ldots, x_n\in M$에 대하여, $p=p_1+\cdots+p_n$이라 하자. 그럼 $\\{1,\ldots, p\\}=P_1\cup\cdots\cup P_n$이도록 하는 집합 $\\{1,\ldots, p\\}$의 분할들의 순서쌍들의 집합

    $$\mathscr{P}=\left\{(P_1,\ldots, P_n)\bigg| \bigcup_{k=1}^n P_k=\{1,\ldots, p\}, P_i\cap P_j=\emptyset\right\}$$

    과, 각각의 $P\in\mathscr{P}$마다 정의된 $i\in P_{\phi(i)}$이도록 하는 함수 $\phi:\\{1,\ldots, p\\} \rightarrow \\{1,\ldots, n\\}$에 대하여,

    $$\gamma_{p_1}(x_1)\cdots\gamma_{p_n}(x_n)=\sum_{P\in \mathscr{P}}x_{\phi(1)}\otimes \cdots x_{\phi(p)}$$

    이 성립한다. 
4. 임의의 $x\in M$과 자연수 $p,q$에 대하여, 식
    
    $$\gamma_p(x)\gamma_q(x)=\frac{(p+q)!}{p!q!}\gamma_{p+q}(x)$$

    이 성립한다.
5. 임의의 $x_1,\ldots, x_n\in M$이 주어졌다 하고, 임의의 부분집합 $H\subseteq \\{1,\ldots, n\\}$에 대하여 $x_H+\sum_{i\in H}x_i$라 하자. 그럼 다음의 식
    
    $$(-1)^nx_1x_2\cdots x_n=\sum_{H\subset\{1,\ldots, n\}}(-1)^{\lvert H\rvert}\gamma_n(x_H)$$

    이 성립한다. 

</div>

일반적인 텐서대수에서와 마찬가지로, 우리의 관심이 되는 것은 특별히 $M$이 free $A$-module일 때이다. 우선 다음의 보조정리를 보이자. 

<div class="proposition" markdown="1">

<ins id="lem6">**보조정리 6**</ins> Finite group $H$와 left $AH$-module $N$에 대하여, $N$의 $H$-invariant $A$-basis $B$가 주어졌다 하고, 이 action에 대한 quotient set $\Omega=B/H$를 생각하자. 그럼 다음이 성립한다. 

1. 각각의 $\omega\in \Omega$마다 $y_\omega=\sum_{b\in\omega}b$라 정의하면, $(y\_\omega)\_{\omega\in \Omega}$는 $N^H$의 $A$-basis이다. 
2. $N^H$의 $N$에서의 supplementary submodule의 basis는 각각의 $\omega\in\Omega$에서 원소 하나씩을 뺀 집합 $\omega'=\omega\setminus \\{z_\omega\\}$들의 합집합 $B'=\bigcup_{\omega\in\Omega} \omega'$로 이루어진다. 

</div>
<details class="proof" markdown="1">
<summary>증명</summary>

우선 $y\_\omega$들과 $B'$의 원소들을 모두 모으면, 이는 단지 $\omega$의 한 원소 $z\_\omega$를 $y\_\omega$로 교체한 것에 불과하므로, 간단한 선형대수에 의해 이것이 $N$의 $A$-basis임을 안다. 즉, 주어진 decomposition을 따라

$$N_1=\sum_{\omega\in\Omega} Ay_\omega,\qquad N_2=\sum_{b'\in B'}Ab$$

라 하면 $N=N_1\oplus N_2$이다. 

이제 보여야 할 것은 $N_1=N^H$이다. 가정에 의해 $N_1\subset N_H$는 자명하다. 한편 임의의 $y\in N^H$에 대하여, $y$를 $A$-basis $B$의 linear combination $y=\sum \alpha_b b$로 나타내면 모든 $b\in B$와 모든 $h\in H$에 대하여 $\alpha_{bh}=\alpha_b$가 성립해야 하는 것을 안다. 이로부터 $y\in N_1$이어야 한다. 

</details>

그럼 이를 이용하여 다음의 명제를 보일 수 있다. 

<div class="proposition" markdown="1">

<ins id="prop7">**명제 7**</ins> $M$이 free $A$-module이고, $(e_i)_{i \in I}$가 $M$의 basis라고 하자.

1. 각각의 $\nu\in\mathbb{N}^{(I)}$에 대하여, $e_\nu=\prod_{i\in I}\gamma_{\nu_i}(e_i)$들은 $\Sym(M)$의 $A$-basis를 이룬다.
2. 임의의 $k$에 대하여, $\Sym^k(M)$은 $\T^kM$의 $A$-direct factor이다. 

</div>
<details class="proof" markdown="1">
<summary>증명</summary>

1. [따름정리 5](#cor5)의 둘째 식을 사용하면 된다.
2. 각각의 $k$에 대하여, $H=S_k$, $N=\T^KM$으로 두고 [보조정리 6](#lem6)을 적용하면 된다. 

</details>

## Functoriality

$A$-module homomorphism $u: M \rightarrow N$에 대하여, 

$$\T(u)\vert_{\Sym(M)}:\Sym(M) \rightarrow \Sym(N)$$

이 잘 정의된다. 우리는 $\T(u)\vert_{\Sym(M)}$을 간단히 $\Sym(u)$로 적는다. 그러면 $\Sym$이 functor가 되는 것을 알고, 뿐만 아니라 [§텐서대수](/ko/math/multilinear_algebra/tensor_algebras)의 해당하는 성질들로부터 다음의 natural isomorphism 

$$\bigotimes_{i\in I}\Sym(M_i)\rightarrow \Sym\left(\bigoplus_{i\in I} M_i\right)$$

이 존재하는 것을 안다. 그럼 $u: M\oplus M \rightarrow M$를 $(x,y)\mapsto x+y$로 정의하면, 다음의 합성

$$\Sym(M)\otimes\Sym(M) \rightarrow \Sym(M\oplus M)\overset{\Sym(u)}{\longrightarrow} \Sym(M)$$

이 $x\otimes y$를 $xy$로 보낸다는 것을 안다. 

## 대칭대수와 대칭텐서

Canonical injection $i: M \rightarrow \T(M)$과 $j: M \rightarrow \Sym(M)$을 생각하자. 그럼 [§텐서대수, ⁋명제 2](/ko/math/multilinear_algebra/tensor_algebras#prop2)에 의하여, 유일한 $\mathbb{N}$-graded $A$-algebra homomorphism $s: \T(M)\mapsto \Sym(M)$이 존재하여 $j=s\circ i$이도록 할 수 있다. 그럼 이는 $\T^0(M)=\Sym^0(M)$에서는 identity이며, $\T(M)$과 $\Sym(M)$ 각각에서 곱셈이 어떻게 정의되었는지를 생각하면 $s:\T(M) \rightarrow \Sym(M)$은 정확히 *symmetrization* 

$$s:\T(M)\rightarrow \Sym(M);\qquad x\mapsto \sum_{\sigma\in S_n}\sigma x$$

임을 안다. 다소 주의할 것으로, 만일 $x\in\Sym^k(M)\subseteq \T^k(M)$이라 하더라도 $s(x)$는 $x$가 그대로 나오는 것이 아니라 $k!.x$가 나온다는 것이 있다.

<div class="remark" markdown="1">

<ins id="rmk1">**참고**</ins> 위와 같은 이유로, 몇몇 reference들에는 처음 symmetric product를 정의할 때부터

$$xy=\frac{1}{p!q!}\tr_{S_{p+q}/(S_p\times S_q)}(x\otimes y)$$

으로 정의하기도 한다. 이렇게 했을 때 유리한 점은 위와 같은 계수를 더 이상 신경쓸 필요가 없다는 것이나, 위의 표기가 말이 되기 위해서는 처음부터 $\T(M)$ 위에 $\mathbb{Q}$-vector space 구조가 있어야 한다. 

일반적으로 임의의 $A$-module 위에는 $\mathbb{Z}$-module 구조가 있지만 (따라서 $k!.x$ 등의 표현이 $A$에 관계없이 잘 정의되지만) 자연스러운 $\mathbb{Q}$-action은 존재하지 않으므로 우리는 원래의 정의를 그대로 사용하기로 한다. 

</div>

이와 같이 얻어낸 symmetrization map $s:\T(M) \rightarrow \Sym(M)$에 대하여, 우리는 [§텐서대수, ⁋명제 6](/ko/math/multilinear_algebra/tensor_algebras#prop6)에 의하여 다음의 식

$$s=\bar{s}\circ p$$

를 만족하는 $\bar{s}: \S(M) \rightarrow \Sym(M)$을 얻을 수 있으며, 어렵지 않게 이것이 실제로 graded homomorphism이 되는 것을 확인할 수 있다. 여기서 $p: \T(M) \rightarrow \S(M)$은 canonical projection이다. 

한편 $\bar{s}$는 반대방향의 함수

$$t: \Sym(M)\hookrightarrow \T(M)\overset{p}{\longrightarrow}\S(M)$$

또한 가지며, 우리의 주장은 많은 경우 이들 두 함수를 서로의 (거의) 역함수로 생각해도 된다는 것이다. 

<div class="proposition" markdown="1">

<ins id="prop8">**명제 8**</ins> 다음이 성립한다.

1. 만일 $x\in \S^n(M)$이라면, $(t\circ\bar{s})(x)=n!.x$이다.
2. 만일 $x\in \Sym^n(M)$이라면, $(\bar{s}\circ t)(x)=n!.x$이다. 

</div>

이에 대한 증명은 단순한 계산이다. 

위에서의 [참고](#rmk1)에서 살펴본 바와 비슷한 이유로, 만일 $A$가 ($\mathbb{Z}$-algebra일 뿐만 아니라) $\mathbb{Q}$-algebra라면 $x\mapsto n!.x$가 bijection이고 따라서 위에서 정의한 $\bar{s}: \S(M) \rightarrow \Sym(M)$이 isomorphism이 되는 것을 확인할 수 있다. 

## 다항식 사상

한편 symmetric algebra $\S(M)$은 symmetric $n$-linear map들의 representation으로 생각할 수 있었는데, 위의 [명제 8](#prop8)을 통해 $\Sym(M)$을 함께 생각하면 다음의 명제를 얻는다. 

<div class="proposition" markdown="1">

<ins id="prop9">**명제 9**</ins> 두 $A$-module $M,N$, 자연수 $n$과 $u: M \rightarrow N$이 주어졌다 하자. 만일 $M$이 free $A$-module이라면 다음이 모두 동치이다. 

1. 식 $u(x)=v(x,\ldots, x)$를 만족하는 $n$-linear map $v: M^n \rightarrow N$이 존재한다. 
2. 식 $u(x)=w(\gamma_n(x))$를 만족하는 linear map $w: \Sym(M) \rightarrow N$이 존재한다. 
3. $M$의 basis $(e\_i)\_{i\in I}$, $(\mathbb{N}^{(I)})_n$-indexed family $(y\_\nu)$가 존재하여 
    
    $$u\left(\sum_{i\in I}\lambda_i e_i\right)=\sum_{\nu\in\mathbb{N}^{(I)})_n}\lambda^\nu y_\nu$$

    이도록 할 수 있다. 
4. $M$의 basis $(e\_i)\_{i\in I}$마다 3번 조건의 식을 만족하는 family $(y_\nu)$를 찾을 수 있다.

</div>

그럼 이 동치조건들을 만족하는 map $u: M \rightarrow N$들을 degree $n$ *homogeneous polynomial mapping*이라 부르고 이들의 모임을 $\Poly^n(M,N)$으로 적는다. 위의 명제의 첫째 조건과 둘째 조건은 각각 $M$에서 $N$으로의 $n$-linear map들의 모임에서 $\Poly^n(M,N)$으로의 surjection, $\Hom_A(\Sym^n(M), N)$에서 $\Poly^n(M,N)$으로의 surjection을 각각 유도하며, 셋째 조건과 넷째 조건은 이 이름 *polynomial mapping*을 정당화한다. 

<div class="example" markdown="1">

<ins id="ex10">**예시 10**</ins> $A$-module $N$에 대하여, free $A$-module $A^{(I)}$이 주어졌다 하고 다항식 $u\in N[\x\_i]\_{i\in I}$를 하나 고정하자. 그럼 다음의 식

$$(x_i)_{i\in I} \mapsto u(x_i)\in N$$

은 $A$-module들 사이의 hoomgeneous polynomial mapping이며 그 degree는 $n$이다. 

</div>

어렵지 않게 두 polynomial mapping의 합성은 다시 homogeneous mapping이라는 것을 보일 수 있다. 

<div class="proposition" markdown="1">

<ins id="prop11">**명제 11**</ins> [명제 9](#prop9)의 조건을 모두 가정하고, 추가로 $y\mapsto n!.y$가 $N$의 automorphism이라 가정하자. 그럼 임의의 $u\in\Poly^n(M,N)$에 대하여, 식

$$u(x)=v(x,\ldots, x)$$

을 만족하는 <em_ko>유일한</em_ko> symmetric $n$-linear map $v:M^n \rightarrow N$이 존재한다. 뿐만 아니라, 임의의 $x_1,\ldots, x_n\in M$에 대하여, 명시적으로

$$v(x_1,\ldots, x_n)=\frac{1}{n!}\sum_{H\subseteq \{1,\ldots, n\}}(-1)^{\lvert H\rvert}u\left(\sum_{i\in I} x_i\right)$$

이 성립한다. 

</div>

이는 [따름정리 5](#cor5)로부터 따라나오는 결과이다. 이제 이것과 [참고](#rmk1)의 관찰을 종합하면 다음의 결과를 얻는다. 

<div class="proposition" markdown="1">

<ins id="prop12">**명제 12**</ins> [명제 9](#prop9)의 상황을 가정하고, canonical homomorphism $\Hom_A(\Sym^n(M), N) \rightarrow \Poly^n(M,N)$을 생각하자. 그럼 다음이 성립한다.

1. 만일 $A$가 무한집합인 integral domain이고 $N$이 torsion-free라면 이 homomorphism은 isomorphism이다. 
2. 만일 $y\mapsto n!.y$가 $N$에서 $N$으로의 injective endomorphism이라면 $u$는 isomorphism이다. 

</div>

## 대칭함수

한편, $M$이 fintely generated free $A$-module일 경우 $\S(M)$은 polynomial algebra $A[\x_1,\ldots, \x_n]$과 isomorphic하다는 것을 알고 있다. 이 상황을 조금 더 자세히 살펴보자. 

우선 자연수 $n$과 $\sigma\in S_n$에 대하여, 우리는 다음의 식

$$\x_i\mapsto \x_{\sigma(i)}$$

을 통해 polynomial ring $A[\x_1,\ldots, \x_n]$의 endomorphism을 정의할 수 있다. 그럼 이 action에 대한 invariant들의 모임

$$A[\x_1,\ldots, \x_n]^{S_n}=\{p\in A[x_1,\ldots, \x_n]\mid \sigma\cdot p=p\}$$

을 생각할 수 있다. 우선 우리는 이들이 $A$-algebra로서 다음의 원소들

$$s_k=\sum_{\substack{H\subset \{1,\ldots, n\}\\\lvert H\rvert=k}}\prod_{i\in H} x_i$$

로 생성된다는 것을 확인할 수 있다. 명시적으로

$$s_0=1,\quad s_1=\sum_{i=1}^n \x_i,\quad s_2=\sum_{1\leq i< j\leq n} \x_i\x_j,\quad \cdots \quad s_n=\x_1\cdots\x_n$$

으로 주어진다. 그럼 귀납법을 통해 $s_i$들이 $A$ 위에서 
algebraically independent인 것을 보일 수 있다. 즉, 다음의 식

$$u(s_0,\ldots, s_n)=0$$

을 만족하는 $u\in A[\x_0,\ldots, \x_n]$은 존재하지 않는다. 또, 다음의 식

$$\x^\nu=\x_1^{\nu(1)}\cdots\x_n^{\nu(n)},\qquad 0\leq\nu(i)< i$$

을 만족하는 monomial들 $\x^\nu$들이 $A[\x_1,\ldots, \x_n]^{S_n}$-module로서 $A[\x_1,\ldots, \x_n]$을 생성한다는 것 또한 확인할 수 있다. 이 과정에서 유용한 식은 polynomial ring $A[\x_1,\ldots, \x_n, T_1, T_2]$에서 성립하는 다음의 식

$$\prod_{i=1}^n(T_1+\x_iT_2)=\sum_{k=0}^n T_1^{n-k}T_2\x_k$$

으로, 이 식은 특히 다음의 두 식

$$\prod_{i=1}^n(1+\x_iT)=\sum_{k=0}^n s_kT^k,\qquad \prod_{i=1}(\x-\x_i)=\sum_{k=0}^n(-1)^{n-k}s_{n-k}\x^k$$

을 준다. 여기서 둘째 식을 근과 계수의 관계와 비슷한 성질 것으로 생각하면 임의의 다항식

$$f(\x)=\x^n+a_{n-1}\x^{n-1}+\cdots +a_1\x +a_0$$

에 대하여 다음의 $A$-algebra

$$E_f=A[\x_1,\ldots,\x_n]/\mathfrak{a},\qquad \mathfrak{a}=(s_k+(-1)^{k+1}a_k)$$

를 생각할 수 있으며, 이 때 $f$는, 계수를 $A$ 대신 $E_f$로 확장하면, 일차식들의 곱으로 완전히 인수분해된다. 뿐만 아니라 $E_f$는 이러한 성질을 갖는 $A$-algebra 중 universal한 대상인데, 이를 엄밀히 적으면 다음과 같다.

<div class="proposition" markdown="1">

<ins id="prop13">**명제 13**</ins> 임의의 commutative ring $A,B$가 주어졌다 하고, ring homomorphism $\rho: A \rightarrow B$와 $B$의 원소들 $\xi_1,\ldots, \xi_n$을 고정하자. 만일 $B[\x]$에서 다음의 식

$$\rho(f)(\x)=\prod_{i=1}^n (\x-\xi_i)$$

이 성립한다면, 유일한 ring homomorphism $u: E_f \rightarrow B$가 존재하여 $\rho(a)=u(a.1)$이고 $u(\x_i)=\xi_i$이도록 할 수 있다. 

</div>