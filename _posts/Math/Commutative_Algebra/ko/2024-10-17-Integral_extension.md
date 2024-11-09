---

title: "정수적 확장"
excerpt: ""

categories: [Math / Commutative Algebra]
permalink: /ko/math/commutative_algebra/integral_extension
header:
    overlay_image: /assets/images/Math/Commutative_Algebra/Integral_extension.png
    overlay_filter: 0.5
sidebar: 
    nav: "commutative_algebra-ko"

date: 2024-10-17
last_modified_at: 2024-10-17
weight: 8

---

## 케일리-해밀턴 정리

우선 일반화된 Cayley-Hamilton 정리를 먼저 언급하고 시작한다. 

<div class="proposition" markdown="1">

<ins id="thm1">**정리 1**</ins> Ring $A$와 ideal $\mathfrak{a}\subseteq A$를 고정하고, $M$이 $n$개의 원소들 $e\_1,\ldots,e\_n$으로 생성되는 $A$-module이라 하자. 그럼 임의의 $u\in\End_\rMod{A}(M)$에 대하여, 만일 $u(M)\subseteq \mathfrak{a}M$이 성립한다면 다음의 monic polynomial

$$p(\x)=\x^n+p_1\x^{n-1}+\cdots+p_n,\qquad p_k\in \mathfrak{a}^k$$

이 존재하여 $p(u)=0$인 것과 동치이다.

</div>
<details class="proof" markdown="1">
<summary>증명</summary>

[\[다중선형대수학\] §행렬식, ⁋명제 9](/ko/math/multilinear_algebra/determinants#prop9)에서 $M$은 free module일 필요가 없다.

</details>

그럼 다음이 성립한다.

<div class="proposition" markdown="1">

<ins id="prop2">**명제 2**</ins> Ring $A$에 대하여, ideal $\mathfrak{a}\subseteq A[\x]$이 주어졌다 하고, $B=A[\x]/\mathfrak{a}$, 그리고 $\x+\mathfrak{a}\in B$를 $b$로 표기하자. 그럼 다음이 성립한다.

1. $B$가 $A$-module로서 $n$개 이하의 원소로 생성되는 것과 $\mathfrak{a}$가 $n$차 이하의 monic polynomial을 포함하는 것이 동치이다. 이 때, $B$는 $1,b,\cdots,b^{n-1}$로 생성된다. 
2. $B$가 $A$-module로서 free module인 것은 $\mathfrak{a}$가 monic polynomial로 생성되는 것과 동치이다. 이 때 $1,b,\cdots,b^{n-1}$가 $B$의 basis가 된다.

</div>
<details class="proof" markdown="1">
<summary>증명</summary>

1. 한쪽 방향은 자명하다. 거꾸로 $B$가 $A$-module로서 $n$개의 원소로 생성된다 하자. 이제 $B$의 원소에 $b$를 곱하여 얻어지는 $A$-module endomorphism $b:B \rightarrow B$를 생각하자. Ideal $A$에 대해 [정리 1](#thm1)을 적용하면 이 endomorphism이 $n$차 monic polynomial $p(x)$를 만족한다는 것을 알고, 이것은 원소로서 $b$를 대입해도 $0$이 되어야 한다. 따라서 $b$의 정의에 의하여 $p(\x)\in \mathfrak{a}$임을 안다.
2. 우선 $\mathfrak{a}$가 차수 $n$의 monic polynomial로 생성된다 하자. 그럼 방금 전의 결과에 의해 $B$가 $1,b,\ldots, b^{n-1}$에 의해 생성된다는 것을 안다. 이제 이들이 일차독립임을 보이면 충분하다. $A$-module $B$에서 $\sum_{i=0}^{n-1} a_i b^i=0$이라 하면, $q(\x)=\sum_{i=0}^{n-1}a_i\x^i$가 $\mathfrak{a}$에 석해야 하고, 차수 때문에 $q=0$이어야 한다.  
반대로 $B$가 rank $n$의 free $A$-module이라 하면 $B$를 $n$개의 원소로 생성할 수 있으며, 다시 방금 전의 결과로부터 $\mathfrak{a}$가 $n$차 monic polynomial $p$를 포함하며, 이로부터 $1,b,\ldots, b^{n-1}$이 $B$의 basis가 되는 것까지 유도할 수 있다. 남은 것은 $p$가 $\mathfrak{a}$를 생성하는 것을 보이는 것인데, 이는 임의의 $f\in \mathfrak{a}$가 주어졌다 하고 이를 $p$로 나눈 나머지 $r$을 생각하면 된다. 두 다항식 $f$와 $p$가 모두 $\mathfrak{a}$에 속하므로, 이 나머지 또한 $B$로 보내면 $0$이 되어야 한다. 그런데 이는 다항식 $r(\x)$에 $\x=b$를 대입한 것과 같고, 이는 $B$의 basis $1,\ldots, b^{n-1}$의 일차결합이라 생각하면 $r$의 계수들이 모두 $0$이어야 한다는 것을 안다. 

</details>

이제 다음을 정의한다.

<div class="definition" markdown="1">

<ins id="def3">**정의 3**</ins> 임의의 ring $A$와 $A$-algebra $E$를 생각하자.

1. $E$의 원소 $x$가 $A$에 대해 *integral<sub>정수적</sub>*이라는 것은 적당한 monic polynomial $p\in A[\x]$가 존재하여 $p(x)=0$인 것이다. $E$의 모든 원소가 $A$에 대해 integral이라면 $E$가 $A$에 대하여 integral이라 부른다. 
2. $A$-algebra $E$ 중, injective map $a\mapsto a\cdot 1_E$를 통해 $A$를 포함하고 있는 $E$를 $A$의 extension이라 부르고, 특히 $E$의 모든 원소가 integral이라면 $E$를 $A$의 *integral extension<sub>정수적 확장</sub>*이라 부른다. 
3. 임의의 $A$-algebra $E$에 대하여, $E$의 원소들 중 $A$에 대해 integral인 것을 모두 모은 것을 $E$ 안에서의 $A$의 *normalization<sub>정규화</sub>*라 부른다. 특별히 임의의 integral domain $A$에 대하여, $\Frac(A)$ 안에서의 $A$의 normalization을 별다른 수식어 없이 $A$의 normalization이라 부르고, 자기 자신과 그 normalization이 같은 integral domain을 *normal domain<sub>정규정역</sub>*이라 부른다.
4. $A$-algebra $E$가 $A$-module로서 유한하게 생성된다면, $E$가 *finite over $A$<sub>$A$에 대하여 유한</sub>*이라 부른다.

</div>

그럼 $E$가 $A$에 대하여 integral인 것과, $E$의 각각의 원소들이 integral인 것이 서로 관계가 있기를 기대하는 것이 자연스럽다. 이를 위해 우선 다음 보조정리를 보인다.

<div class="proposition" markdown="1">

<ins id="lem4">**보조정리 4**</ins> $A$-algebra $E$와 $E$의 원소 $x$가 주어졌다 하자. 그럼 $x$가 $A$에 대해 integral인 것은, 적당한 $E$-module $N$과 $N$의 $R$-submodule $M$이 존재하여, $M$은 $E$의 어떠한 nonzero element에 대해서도 annihilate되지 않으며 포함관계 $xM\subseteq M$이 성립하는 것과 동치이다. 

</div>
<details class="proof" markdown="1">
<summary>증명</summary>

우선 $x$가 $A$에 대하여 integral이라 하자. 그럼 $N=E$로 잡으면 $M=A[x]$는 [명제 2](#prop2)에 의하여 finitely generated인 것을 안다. 반대방향은 [명제 2](#prop2)의 증명과 마찬가지로 $x$를 곱하는 것을 $M$의 endomorphism으로 본 후 [정리 1](#thm1)을 적용하면 된다.

</details>

이제 다음을 증명할 수 있다.

<div class="proposition" markdown="1">

<ins id="thm5">**정리 5**</ins> $A$-algebra $E$에 대하여, $E$ 안에서 $A$의 integral extension은 다시 $A$-algebra이다. 

</div>
<details class="proof" markdown="1">
<summary>증명</summary>

두 원소 $x,y\in E$가 $A$에 대하여 integral이라 하자. 그럼 $x+y$와 $xy$가 $A$에 대하여 integral임을 보여야 한다. 이제 $M=A[x]$, $M'=A[y]$이 $E$의 두 submodule이라 하고, 이들의 원소들의 곱 $xx'$들로 생성되는 $E$의 subalgebra를 $MM'$을 생각하면 $M,M'$ 각각이 finitely generated이므로 $MM'$ 또한 finitely generated이다. 이제

$$(xx')MM'=(xM)(x'M)\subseteq MM',\qquad (x+x')MM'\subseteq xMM'+M(x'M')\subseteq MM'$$

이므로 [보조정리 4](#lem4)를 이용하면 원하는 결과를 얻는다. 

</details>


## 나카야마 보조정리

이제 우리는 아주 유용한 보조정리를 증명한다. 우선 ring $A$의 임의의 ideal $\mathfrak{a}$에 대하여, $\mathfrak{a}$의 *nilradical<sub>영근기</sub>* $\sqrt{(0)}$은 다음 식

$$\sqrt{(0)}=\bigcap_\text{\scriptsize$\mathfrak{p}$ prime} \mathfrak{p}$$

으로 주어지는 것을 기억하자. ([§국소화, ⁋따름정리 10](/ko/math/commutative_algebra/localization#cor10)) 비슷한 식으로 $A$의 *Jacobson radical<sub>제이콥슨 근기</sub>*를 다음 식

$$J(R)=\bigcap_\text{\scriptsize$\mathfrak{m}$ maximal} \mathfrak{m}$$

으로 정의한다.

나카야마 보조정리를 증명하기 위해서는 우선 다음의 보조정리를 먼저 증명해야 한다.

<div class="proposition" markdown="1">

<ins id="lem6">**보조정리 6**</ins> Finitely generated $A$-module $M$과 $A$의 ideal $\mathfrak{a}$가 $\mathfrak{a}M=M$을 만족한다 하자. 그럼 적당한 $a\in \mathfrak{a}$가 존재하여 $(1-a)M=0$이다.

</div>
<details class="proof" markdown="1">
<summary>증명</summary>

주어진 조건으로부터 $M\subseteq \mathfrak{a}M$이므로 [정리 1](#thm1)로부터 적당한 monic polynomial

$$p(\x)=\x^n+p_1\x^{n-1}+\cdots+p_n,\qquad p_k\in \mathfrak{a}^k$$

이 존재하여 $p(\id_M)=0$이다. 즉, 

$$(1+p_1+\cdots_p_n)M=0$$

이고 $a=-(p_1+\cdots_p_n)$으로 두면 원하는 결과를 얻는다. 

</details>

이제 드디어 나카야마 보조정리를 말할 수 있다. 

<div class="proposition" markdown="1">

<ins id="lem7">**보조정리 7 (Nakayama)**</ins> $A$의 Jacobson radical $J(A)$에 속하는 ideal $\mathfrak{a}$가 주어졌다 하고, $M$이 finitely generated $A$-module이라 하자. 그럼 다음이 성립한다.

1. 만일 $\mathfrak{a}M=M$이라면 $M=0$이다.
2. 만일 $x_1,\ldots, x_n$의 $M/\mathfrak{a}M$에서의 image가 $M/\mathfrak{a}M$을 $A$-module로써 생성한다면, $x_1,\ldots, x_n$들은 $M$을 $A$-module로써 생성한다.

</div>
<details class="proof" markdown="1">
<summary>증명</summary>

1번 겷과의 경우 [보조정리 6](#lem6)으로부터 얻어지는 $a\in \mathfrak{a}$가 가정에 의하여 모든 maximal ideal에 속한다는 사실을 안다. 바꾸어 말하면 $1-a$는 어떠한 maximal ideal에도 속할 수 없으므로 $1-a$는 unit이다. 따라서 원하는 결과를 얻는다.

2번 결과의 경우, $N=M/\sum\_i Ax\_i$라 하자. 그럼 $N/IN=0$임을 보일 수 있고 1번 결과로부터 $N=0$임을 안다.

</details>

## 정규화

이제 우리는 normal domain과 normalization에 대해 살펴본다. 

<div class="proposition" markdown="1">

<ins id="prop8">**명제 8**</ins> Unique factorization domain은 normal domain이다.

</div>
<details class="proof" markdown="1">
<summary>증명</summary>

임의의 $a/b\in \Frac(A)$에 대하여, $a,b$가 coprime이고 $a/b$가 $A$의 normalization에 포함된다 하자. 그럼 적당한 monic polynomial이 존재하여

$$\left(\frac{a}{b}\right)^n+a_{n-1}\left(\frac{a}{b}\right)^{n-1}+\cdots+a_1\left(\frac{a}{b}\right)+a_0=0$$

이도록 할 수 있디. 이제 이로부터

$$\x^n+a_{n-1}b \x^{n-1}+\cdots+a_1b^{n-1}\x+a_0b^n\in A[\x]$$

은 $\x=a$를 넣었을 때 $0$이 되는 monic polynomial인 것을 안다. 즉 $a^n$은 $b$로 나누어떨어지며, 이것이 모순이 되지 않기 위해서는 $b=1$, 즉 $A$가 normal domain이어야 한다.

</details>

더 일반적으로 다음이 성립한다.

<div class="proposition" markdown="1">

<ins id="prop9">**명제 9**</ins> Ring $A\subseteq B$가 주어졌다 하고 monic polynomial $p\in A[\x]$가 주어졌다 하자. 만일 $B[\x]$ 안에서 $p=q_1q_2$이도록 하는 monic polynomial들 $q_1,q_2\in B[\x]$를 찾을 수 있다면 $q_1,q_2$의 계수들은 $A$에 대해 integral이다.

</div>
<details class="proof" markdown="1">
<summary>증명</summary>

방정식의 해를 넣어주는 방법으로 $B$를 포함하는 적당한 ring $C$에 대하여 $C[\x]$ 안에서는 $q_1,q_2$가 모두 $\prod (x-\alpha_i)$, $\prod(x-\beta_j)$의 꼴로 분해되도록 할 수 있다. 그럼 정의에 의해 $\alpha_i,\beta_j$들은 모두 $A$에 대해 integral이므로, 이들로 생성되는 $C$의 subring $C'$는 integral $A$-algebra이다. 한편 $p=q_1q_2$를 전개하여 그 계수를 보면 이들이 $C'$에 속한다는 것을 안다.

</details>

따라서 다음이 성립한다.

<div class="proposition" markdown="1">

<ins id="cor10">**따름정리 10**</ins> Normal domain $A$에 대하여, 임의의 monic irreducible polynomial은 prime이다. 

</div>

이제 