---

title: "Basic definitions"
excerpt: "Algebra의 정의"

categories: [Math / Algebras]
permalink: /ko/math/algebras/basic_definitions
header:
    overlay_image: /assets/images/Algebras/Basic_definitions.png
    overlay_filter: 0.5
sidebar: 
    nav: "algebraic_structures"

date: 2021-08-24
last_modified_at: 
weight: 1

published: false

---
<div class="notice--warning" markdown="1">

이 글은 현재 수정중입니다.

이 글은 예전에 쓴 글로, 서술 방향이 마음에 들지 않거나 표기법이 마음에 들지 않아 전체적으로 수정이 진행중입니다. 읽으실 때 참고해주세요.

</div>

Algebra는 보통 학부 때에는 잘 다루지 않는 구조인데, 대학원에서는 온갖군데에 다 나오기 때문에 넘어갈 수가 없다. Algebra를 다루는 동안, 별 말이 없으면 모든 ring은 commutative ring with unity 1이라 가정하고, 모든 ring homomorphism은 unital (i.e. $1$을 $1$로 보내는)이라 가정한다.

## Basic definition

<div class="definition" markdown="1">
<ins id="df1">**정의 1**</ins> Commutative ring $R$에 대하여, $A$가 $R$-algebra라는 것은 다음의 두 구조

1. $A$ 위에서의 $R$-module structure
2. $A\times A$에서 $A$로의 $R$-bilinear map

이 주어진 구조이다. $R$-bilinear map $A\times A\rightarrow A$를 간단히 $(x,y)\mapsto xy$로 적는다. 
</div>

위의 정의에서의 $R$-bilinear map을 algebra $A$에서의 곱셈으로 정의한다. $R$이 bilinear라는 사실로부터, algebra의 곱셈이 $R$-module의 덧셈과의 분배법칙을 갖는다는 사실을 확인할 수 있다. 따라서 $R$-algebra라는 구조는 $R$-module인 동시에 스스로가 ring처럼 행동하는 구조다. 그러나 $R$-algebra의 곱셈은 1을 가질 필요도, commutative할 필요도 없으며 심지어는 associative할 필요도 없다.  
어쨌든, $A$는 기본적으로 $R$-module이므로 $A$의 원소들의 linear combination $\sum \alpha_ix_i$를 생각할 수 있다. (물론, 지금까지 그래왔듯 $\supp(\alpha_i)_{i\in I}$가 finite라는 것은 언급할 필요도 없이 당연하게 붙어있는 조건이다.) 그럼 임의의 두 linear combination

$$\sum_{i\in I}\alpha_ix_i,\qquad \sum_{j\in J}\beta_jy_j$$

에 대하여 분배법칙을 적용하면

$$\left(\sum_{i\in I}\alpha_ix_i\right)\left(\sum_{j\in J}\beta_jy_j\right)=\sum_{(i,j)\in I\times J}(\alpha_i\beta_j)\cdot (x_iy_j)\tag{1}$$

를 얻는다. 특히, $I$, $J$가 모두 singleton이고, $\beta=1$로 잡으면 다음의 식

$$(\alpha x)y=(\alpha 1)\cdot (xy)=\alpha\cdot(xy)=(1\alpha)\cdot(xy)=x(\alpha y)$$

을 얻는다. Ring에서와 같이, 곱셈 $(x,y)\mapsto xy$를 거꾸로 $(x,y)\mapsto yx$로 주어도 algebra structure를 얻으며, 이렇게 얻어진 구조를 *opposite algebra*라고 부르고 $A^\op$으로 적고, $A$에서 $A^\op$으로 가는 isomorphism은 *anti-automorphism*이라 부른다. 또, 만일 $A=A^\op$라면 (즉 algebra의 곱셈이 commutative하다면) $A$가 commutative하다고 부르고, algebra의 곱셈이 associative하다면 $A$가 associative하다고 한다. 마지막으로 만일 $A$가 곱셈에 대한 항등원을 가진다면 이 원소를 *unit element*라 부르고, algebra를 *unital algebra*라 부른다. 

<div class="example" markdown="1">
<ins id="ex2">**예시 2**</ins> 일반적으로 algebra는 associative할 필요도, commutative할 필요도, unital일 필요도 없다. 간단한 예시로, 실수 $\mathbb{R}$ 위에서 정의된 general linear group $\GL_n(\mathbb{R})$을 생각하자. 여기에서 $\mathbb{R}$-module ($\mathbb{R}$은 field이므로, 사실은 $\mathbb{R}$-vector space) 구조는 그냥 자연스럽게 $n^2$-dimensional $\mathbb{R}$-vector space 구조로 주어진다. 만일 여기에 자연스러운 행렬의 곱셈을 준다면, $\GL_n(\mathbb{R})$은 associative unital $\mathbb{R}$-algebra가 된다.  그런데 일반적인 곱셈 대신, 다음의 *bracket*

$$[X,Y]=XY-YX$$

을 준다면 associativity도 깨지게 되며, unity도 존재하지 않는다. (즉, $[X,Y]=X$ for all $X$인 $Y$는 존재하지 않는다.) 
</div>

위의 예시에서의 bracket은 나중에 또 나오게 된다.

아무튼, algebra를 정의했으니 algebra간의 homomorphism을 정의해야 하는데, 다른 대수적 구조들에서 그랬듯 그 정의야 뻔하다.

<div class="definition" markdown="1">

<ins id="df3">**정의 3**</ins> 두 $R$-algebra $A$, $A'$에 대하여 $f:A\rightarrow A'$가 *algebra homomorphism*인 것은 $f$가 $R$-module homomorphism이고, 임의의 $x,y\in A$에 대해 $f(xy)=f(x)f(y)$ 또한 성립하는 것이다. 만일 $A$, $A'$가 모두 unital algebra라면, $A$의 unit element를 $A'$의 unit element로 보내는 $R$-algebra homomorphism을 *unital homomorphism*이라 부른다.

</div>

그리고 역시 다른 대수적 구조와 마찬가지로, homomorphism을 정의하고 나면 체크해봐야 할 것이 있다.

<div class="proposition" markdown="1">

<ins id="pp4">**명제 4**</ins> 두 $R$-algebra homomorphism의 합성은 다시 $R$-algebra homomorphism이다. 

</div>

또한, 어렵지 않게 bijective한 algebra homomorphism이 algebra isomorphism이 된다는 것을 증명할 수 있다. 

한편, $R$-algebra $A$가 주어졌다고 하자. 그럼 우리는 $A$의 submodule $B$가 *subalgebra*라는 것을 $B$가 algebra의 곱셈에 대해 닫혀있다는 조건을 추가하여 정의한다. 또, $A$의 원소들의 family $(x_i)_{i\in I}$에 대하여, $(x_i)\_{i\in I}$들을 포함하는 $A$의 subalgebraa들 가운데 가장 작은 것을 이들 원소에 의해 generate되는 algebra라고 부른다. 

<div class="example" markdown="1">

<ins id="ex5">**예시 5**</ins> Polynomial ring $R[x]$를 생각하자. 그럼 $R[x]$는 자명한 $R$-module structure를 갖는다. 그런데 사실 우리는 $R[x]$에서의 곱셈도 어떻게 정의할 지 알고 있다. 즉, 임의의 polynomial $\sum\alpha_ix^i$, $\sum\beta_jx^j$에 대하여,

$$\left(\sum_{i\in I}\alpha_ix^i\right)\left(\sum_{j\in J}\beta_ x^j\right)=\sum_{d=0}^\infty\left(\sum_{i+j=d}\alpha_i\beta_j\right)x^d$$

이다. 사실 이는 notation에서도 어느정도 예견될 일이었는데, $R[x]$는 $x$에 의해 generate되는 $R$-module이 아니라, 무한히 많은 원소들 $x$, $x^2$, $\ldots$에 의해 generate되는 free $R$-module이기 때문이다. 이 집합을 module로만 취급할 거였다면 정확한 notation은 $R[x,x^2,\ldots]$여야 했을 것이다.

</div>

아주 대략 생각하자면, $R$-algebra는 $R$-module 위에 그 자체가 ring structure 비슷한 (물론 곱셈이 있단 것만 비슷하지만...) 구조가 정의된 것이므로 ideal 비슷한 것 또한 정의할 수 있다.

<div class="definition" markdown="1">

<ins id="df6">**정의 6**</ins> $R$-algebra $A$에 대하여, $A$의 부분집합 $\mathfrak{a}$가 $A$의 *left ideal*이라는 것은 $\mathfrak{a}$가 $A$의 submodule이고, 임의의 $a\in\mathfrak{a}$, $r\in A$에 대하여 $ra\in\mathfrak{a}$가 성립하는 것이다. 이와 비슷하게, *right ideal*  또한 정의하며, $\mathfrak{a}$가 left ideal인 동시에 right ideal이라면 이를 *ideal*이라 부른다.

</div>

Algebra의 곱셈은 ring의 곱셈과 이름만 같지 얼마든지 다르게 정의할 수 있으므로, 일반적으로 ring의 ideal이 algebra의 ideal과 같을 필요는 전혀 없다.

<div class="example" markdown="1">

<ins id="ex7">**예시 7**</ins> 임의의 field $F$에 대하여, ring $F$의 ideal은 $0$과 자기 자신 뿐이다. 한편, $F$는 자명하게 $F$-module (vector space)이기도 하다. 그러나 algebra의 곱셈을 "$ab=0$ for all $a,b\in F$"으로 정의하면, $F$의 임의의 additive subgroup은 0을 포함하므로 항상 $F$의 임의의 원소와의 (algebra) 곱에 닫혀있으므로 algebra ideal이다. 

</div>

사실 이 예시는 어떻게 보면 자연스럽기도 하다. 왜냐하면, 임의의 $R$-module $M$ 위에 algebra structure를 주는 가장 자명한 방법이 다음과 같기 때문이다.

<div class="example" markdown="1">

<ins id="ex8">**예시 8**</ins> 임의의 $R$-module $M$에 대하여, $xy=0$ for all $x,y\in M$으로 정의하면, 이 module은 trivial한 algebra structure를 갖는다. 이 algebra는 associative하고, commutative하지만 unital은 아니다.

</div>

그러나 충분히 좋은 algebra에서 이런 일은 일어나지 않는다.
<div class="proposition" markdown="1">

<ins id="pp9">**명제 9**</ins> Associative unital $R$-algebra $A$는 자연스러운 ring structure를 갖는다.

</div>
<details class="proof" markdown="1">
<summary>증명</summary>

*증명.* $A$가 associative unital $R$-algebra라는 조건은 $A$의 algebra의 곱셈이 associative하고, 이 곱셈에 대한 항등원도 존재한다는 뜻이므로 $A$를 noncommutative ring으로 취급할 수 있다.

</details>

이 명제 하에서, (noncommutative) ring $A$를 정의하는 곱셈과 algebra $A$를 정의하는 곱셈이 정확히 같고, ideal의 정의 또한 완벽하게 동일하므로 ring으로서의 ideal과 algebra로서의 ideal이 동일하다.

어찌되었건, algebra ideal은 ring에서 ideal이 하는 역할을 그대로 할 수 있다. 즉, algebra $A$에 대하여, ideal $\mathfrak{a}$가 주어진다면 이 때의 quotient algebra $A/\mathfrak{a}$가 잘 정의된다. 이에 대한 증명은 ring에서와 마찬가지로 할 수 있다. 그럼 이제 마찬가지로 isomorphism theorem들도 정의할 수 있고...

## Associativity and commutativity, unital algebras

임의의 $R$-algebra $A$는 $R$-module structure 위에, $A\times A$에서 $A$로 가는 $R$-bilinear map이 정의된 구조다. 그런데, 우리는 $A\times A$에서 $R$-module $B$로 가는 $R$-bilinear map이 주어진 것과 $A\otimes_RA$에서 $B$로 가는 $R$-linear map이 주어진 것이 같은 것임을 알고 있으므로, 사실 $A$에 $R$-algebra structure를 주는 것은 $A\otimes_RA$에서 $A$로의 linear map을 하나 주는 것과 동일하다. 

그럼 이제 linear map $m:A\otimes_RA\rightarrow A$가 $R$-algebra $A$의 곱셈을 나타낸다고 하고, 다른 $R$-algebra $A'$와 그 곱셈 $m':A'\otimes_RA'\rightarrow A$가 주어졌다고 하자. 그럼 어떤 map $f:A\rightarrow A'$가 algebra homomorphism이라는 것은 다음의 diagram

![diagram_representing_algebra_homomorphism]({{ site.url }}{{ site.baseurl }}/assets/images/Algebras/Basic_definitions-1.png){: width="250px"  class="invert" .align-center}

이 commutative diagram이라는 것과 동치이다. 한편, canonical하게 $R$-module들 $A\otimes_RA\otimes_RA\cong (A\otimes_RA)\otimes_RA\cong A\otimes_R(A\otimes_RA)$을 identify하고, 두 개의 map

$$m\otimes\id_A: (A\otimes_RA)\otimes_RA\rightarrow A\otimes_RA,\qquad \id_A\otimes_RA: A\otimes_R(A\otimes_RA)\rightarrow A\otimes_RA$$

을 생각한다면, $R$-algebra $A$가 associative하다는 것은 다음의 diagram

![diagram_representing_associativity]({{ site.url }}{{ site.baseurl }}/assets/images/Algebras/Basic_definitions-2.png){: width="250px"  class="invert" .align-center}

이 commute한다는 것과 동치이다. 이와 비슷하게, $R$-algebra $A$가 commutative하다는 것은 다음의 diagram

![diagram_representing_commutativity]({{ site.url }}{{ site.baseurl }}/assets/images/Algebras/Basic_definitions-3.png){: width="250px"  class="invert" .align-center}

이 commute한다는 것과 동치이다. 여기서 $\sigma$는 $x\otimes y\mapsto y\otimes x$로 정의되는 linear map이다. 

마지막으로 우리는 unital algebra를 살펴볼 것이다. 이를 commutative diagram의 언어로 표현하는 것은 잠시 뒤로 미뤄두기로 하고, 우선은 임의의 $R$-algebra가 주어졌을 때 여기에 unity를 만드는 방법을 소개한다.

<div class="example" markdown="1">

<ins id="ex10">**예시 10**</ins> 임의의 $R$-algebra $A$가 주어졌다고 하자. 집합 $\tilde{A}=R\times A$ 위에 다음의 식

$$\begin{aligned}(r,x)+(s,y)&=(r+s,x+y)\\ (r,x)(s,y)&=(rs,xy+sx+ry)\\ r(s, x)&=(rs, rx)\end{aligned}$$

을 통해 곱셈과 덧셈, 그리고 스칼라곱을 정의하면 $\tilde{A}$는 $R$-algebra structure를 가지며, $(1,0)$이 multiplicative unity가 된다. 이 때, $0\times A$는 $\tilde{A}$의 ideal이 되며, $x\mapsto (0,x)$는 $A$에서 $\tilde{A}$로의 injection이 되어 $A$를 어떤 unital algebra $\tilde{A}$의 subalgebra로 취급할 수 있다. 또, 만일 $A$가 associative, 혹은 commutative하다면 $\tilde{A}$도 각각 그렇다. 

</div>


## Algebra and Ring homomorphism

Algebra의 곱셈이 가질 수 있는 성질은 commutativity, associativity, 그리고 1을 갖는지의 여부다. 앞선 두 가지는 위에서 commutative diagram을 이용해서 표현했었다. 이제 algebra의 multiplicative identity를 어떻게 표현하면 좋을지를 한 번 살펴보자. 

우선 ring $R$을 자명한 연산이 주어진 $R$-module로 이해하자. 임의의 $R$-algebra $A$는 정의에 의해 $R$-module이기도 하므로, 우리는 $R$에서 $A$로의 $R$-module homomorphism에 우선 관심이 있다. 그런데 dual module을 정의할 때 살펴봤듯이, $R$에서 $A$로의 $R$-linear map은 $1$의 값만 정해지면 다음의 식

$$f(r)=r f(1)\qquad\text{for all $r\in R$}$$

을 통해 완벽하게 결정된다. 편의상 $1\mapsto a$로 정의되는 $R$-linear map $R\rightarrow A$를 $\eta_a$로 표현하자. 

한편, 임의의 $R$-module $A$에 대하여, $R\otimes_RA$와 $A\otimes_RR$은 map $r\otimes x\mapsto rx$ ($x\otimes r\mapsto rx$)을 통해 canonical하게 $A$와 identify할 수 있다. 이 두 map을 각각 $i$, $j$로 적자. 그럼 이제 임의의 $a\in A$가 algebra의 multiplicative identity가 된다는 것은 다음의 두 diagram

![diagram_representing_identity-1](/assets/images/Algebras/Basic_definitions-4.png){: width="250px"  class="invert" .align-center}

와

![diagram_representing_identity-2](/assets/images/Algebras/Basic_definitions-5.png){: width="250px"  class="invert" .align-center}

이 commute한다는 것과 동치가 된다. 

위에서 소개한 map $\eta_a$는 $R$-algebra와 ring homomorphism 사이의 어떤 관계를 보여준다. Unital $R$-algebra $A$가 주어졌다고 하고, $e\in A$가 $A$의 (algebra로서의) unit element라 하자. 그럼 $R$-module 사이의 homomorphism $\eta:R\rightarrow A$를 다음의 식

$$\eta(r)=r\cdot e$$

을 통해 정의할 수 있다. 한편, $R$은 자명한 $R$-algebra structure (즉 algebra의 곱셈이 ring의 곱셈으로 정의된) 를 가지며, 이 때 $\eta(r_1r_2)$의 값을 계산해보면, 위쪽의 식 (1)에서 $I=\\{i\\}$, $J=\\{j\\}$, $x_i=y_j=e$로 두어

$$\eta(r_1r_2)=(r_1r_2)\cdot e=(r_1r_2)\cdot(ee)=(r_1\cdot e)(r_2\cdot e)=\eta(r_1)\eta(r_2)$$

를 얻는다. 즉, $\eta$는 $R$-module homomorphism일 뿐만 아니라 $R$-algebra homomorphism이기도 하다. 한편 임의의 $r\in R$에 대하여

$$r\cdot x=(r1)\cdot(ex)=(r\cdot e)(1\cdot x)=\eta(r)x\tag{2}$$

이므로, $\eta$라는 함수의 값만 정확히 알고 있다면 우리는 $A$ 위에서의 module structure를 거꾸로 복원해낼 수도 있다. 이 이야기는 잠시 뒤에 하기로 하고... 아무튼 $\eta$는 앞서 말한 것과 같이 $R$-algebra homomorphism이므로 $\eta$의 image는 $A$의 subalgebra가 되고, 또 임의의 $a\in A$와, $\eta(r)\in \im\eta$에 대하여

$$\eta(r)a=(r\cdot e)(1\cdot a)=(r1)\cdot(ea)=(1r)\cdot(ae)=(1\cdot a)(r\cdot e)=a\eta(r)$$

이 성립하므로 $\im\eta$는 $A$의 모든 원소와 commute한다. 이제 $\ker\eta$를 생각해보자. 정의에 의해 $r\in\ker\eta\iff\eta(r)=0\iff r\cdot e=0$이므로, $\ker\eta$는 정확히 $e\in A$의 annihilator ideal이 되며, 앞서 $\eta$가 식 (2)와 같이 $A$ 위에 $R$-module structure를 주는 것을 확인하였으므로 사실 $\ker\eta$는 $A$의 annihilator ideal이기도 하다. 

아까 미뤄뒀던 이야기를 마저 해 보자. 만일 $A$가 associative unital $R$-algebra라면, $A$의 덧셈과 곱셈 구조는 정확하게 ring structure를 주고, 이 때 위에서 정의한 $\eta$가 ring homomorphism이 되는 것은 자명하다. 그런데 이 과정은 거꾸로 할 수도 있다. 즉, 임의의 ring homomorphism $\rho: R\rightarrow S$가 주어졌다고 하자. ($S$는 commutative ring with unity일 필요가 없다.) 만일 $\im\rho$의 모든 원소가 $S$의 원소들과 commute한다면, 즉 $\im\rho$가 $S$의 center에 포함된다면 $\rho$는 다음의 식

$$r\cdot x=\rho(r)x$$

을 통해 $S$ 위에 $R$-module structure를 정의하게 된다. 그럼 $S$는 (i) ring으로써 갖고 있던 덧셈, (ii) ring으로써 갖고 있던 곱셈, (iii) 방금 정의한 $R$-module structure를 통해 associative인 $R$-algebra structure를 갖게 된다. 만약 $S$가 (ring으로써) multiplicative identity $1$을 갖고 있었고, $\rho:R\rightarrow S$가 unital ring homomorphism이었다면 $S$는 associative unital algebra structure를 갖게 됐을 것이다. 물론 associative하지 않은 algebra도 굉장히 중요하지만 (대표적으로 Lie algebra만 해도 associative하지 않다.) 또 많은 경우에 associative한 algebra만 신경쓰기도 하므로, 저자에 따라서는 $R$-algebra의 정의를 ring homomorphism $R\rightarrow S$으로 정의하는 경우도 종종 있다.

## Construction of algebras

이제 우리가 이미 갖고 있는 algebra structure로부터 새로운 algebra를 만드는 법을 살펴본다. 맨 처음은 예상했듯 product다. 

---

**Reference**

**[Bou]** N. Bourbaki, <i>Theory of Sets</i>. Elements of mathematics. Springer Berlin-Heidelberg, 2013.

---
