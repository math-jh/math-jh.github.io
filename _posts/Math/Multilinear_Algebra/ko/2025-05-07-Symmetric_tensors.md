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

이제 본격적인 정의를 시작한다. 우선 임의의 $A$-module $M$에 대하여, $n$-th tensor power $T^n(M)$ 위에 $S_n$-action을 다음의 식

$$\sigma(x_1\otimes x_2\otimes \cdots \otimes x_n)=x_{\sigma^{-1}(1)}\otimes \cdots \otimes x_{\sigma^{-1}(n)}$$

으로 정의할 수 있다. 

<div class="definition" markdown="1">

<ins id="def3">**정의 3**</ins> 위와 같은 상황에서, 

$$\sigma z=z\qquad\text{for all $\sigma\in S_n$}$$

을 만족하는 $z\in T^nM$들을 $n$th *symmetric tensor<sub>대칭텐서</sub>*라 부르고, 이들의 모임 $\Sym^n(M)$을 $n$-th *symmetric power*라 부른다. 이들의 (graded) direct sum을

$$\Sym(M)=\bigoplus_{d=0}^\infty \Sym^d(M)$$

으로 적는다. 

</div>

$\Sym(M)$은 앞서 정의했던 symmetric algebra $S(M)$과는 구별해야 하지만, 좋은 경우에는 이들 둘이 서로 isomorphic하다는 것을 보일 수 있다. 

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

를 만족하는 $\sigma$들로 이루어진 $S_{p+q}$의 subgroup이라 하면 어렵지 않게 $S_{p+q}/S_p\times S_q$와 $S_{p,q}$ 사이의 bijection을 찾을 수 있다. 따라서 위의 식은 다시

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
3. 임의의 $x_1,\ldots, x_n\in M$에 대하여, $p=p_1+\cdots+p_n$이라 하자. 그럼 $\\{1,\ldots, p\\}=P_1\cup\cdots\cup P_n$이도록 하는 집합 $\\{1,\ldots, p\\}$의 분할들의 순서쌍

    $$\mathscr{P}=\left\{(P_1,\ldots, P_n)\bigg\mid \bigcup_{k=1}^n P_k=\{1,\ldots, p\}, P_i\cap P_j=\emptyset\right\}$$

    에 대하여, 

</div>