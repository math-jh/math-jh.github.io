---

title: "다항식환"
excerpt: ""

categories: [Math / Ring Theory]
permalink: /ko/math/ring_theory/polynomial_rings
header:
    overlay_image: /assets/images/Math/Ring_Theory/Polynomial_rings.png
    overlay_filter: 0.5
sidebar: 
    nav: "ring_theory-ko"

date: 2025-05-06
last_modified_at: 2025-05-06
weight: 3

---

<div class="remark" markdown="1">

<ins id="rmk">**주의**</ins> 이번 글에서 $A$는 항상 commutative ring이다.

</div>

우리는 [\[대수적 구조\] §대수, ⁋정의 7](/ko/math/algebraic_structures/algebras#def7)에서 임의의 (commutative) ring $A$에 대하여 polynomial algebra $A[\x\_i]\_{i\in I}$를 정의하였다. 이는 $A$-algebra 구조를 갖지만, 어차피 $A[\x\_i]\_{i\in I}$ 위에 정의된 $A$의 스칼라곱은 $A[\x\_i]\_{i\in I}$를 ring으로 보았을 때, inclusion $A\hookrightarrow A[\x\_i]\_{i\in I}$으로부터 오는 것이므로 $A[\x\_i]\_{i\in I}$의 성질을 살펴보기 위해서는 $A[\x\_i]\_{i\in I}$를 ring으로 생각하는 것만으로 충분하다. 

## 다항식의 차수

다항식들을 본격적으로 다루기 전에, 이들을 다루기 위한 도구들을 먼저 정의하자. 우선 $A$ 위에서 정의된 *다항식*들은 polynomial ring $P=A[\x\_i]\_{i\in I}$의 원소들을 의미한다. 이 때, $\mathbb{N}^{(I)}$를 $I$에서 $\mathbb{N}$으로 가는 finitely supported function들의 모임

$$\mathbb{N}^{(I)}=\{\nu:I \rightarrow \mathbb{N}\mid\text{$f(i)=0$ for all but finitely many $i\in I$}\}$$

으로 정의하자. 그럼 임의의 $\nu\in \mathbb{N}^{(I)}$에 대하여, 

$$\x^\nu=\prod_{i\in I} \x_i^{\nu_i}$$

으로 두면 $\x^\nu$는 $P$의 원소이다. 우리는 

$$a\x^\nu$$

꼴의 원소들을 *단항식*이라 부른다. 그럼 임의의 다항식 $u$는 단항식들의 유한합

$$u(\x)=\sum_{\nu\in \mathbb{N}^{(I)}} a_\nu \x^\nu,\qquad\text{$\alpha_\nu=0$ for all but finitely many $\nu$}$$

으로 나타낼 수 있다. 

한편 임의의 $\nu\in \mathbb{N}^{(I)}$에 대하여 

$$\lvert\nu\rvert=\sum_{i\in I} \nu_i$$

으로 정의하면, $P=A[\x_i]\_{i\in I}$를 $\mathbb{N}$-graded ring

$$P=\bigoplus_{n\in \mathbb{N}}\bigoplus_{\lvert\nu\rvert=n}(A[\x_i]_{i\in I})_\nu=\bigoplus_{n\in \mathbb{N}} P_n$$

으로 생각할 수 있다. 이 때, 각각의 $n$에 대하여, $P_n$의 원소들을 degree $n$의  *homogeneous polynomial<sub>동차다항식</sub>*이라 부른다. 또, 임의의 다항식 $u\in P$에 대하여, 이 homogeneous decomposition에서 degree $n$에 해당하는 $u$의 성분을 $u_n$으로 적기도 한다. 

<div class="definition" markdown="1">

<ins id="def1">**정의 1**</ins> Polynomial ring $P=A[\x]_{i\in I}$의 임의의 원소 

$$u(\x)=\sum_{\nu\in \mathbb{N}^{(I)}} a_\nu \x^\nu,\qquad\text{$\alpha_\nu=0$ for all but finitely many $\nu$}$$

가 주어졌다 하자. 그럼 $u_n\neq 0$을 만족하는 가장 큰 $n$을 $u$의 *degree*라 부르고 $\deg(u)$와 같이 표기한다. 정의에 의하여 상수항만을 가지는 다항식의 차수는 $0$이지만, 특별히 $P$의 덧셈에 대한 항등원 $0$에 대하여는 $\deg(0)=-\infty$로 정의한다.  

</div>

그럼 다음 명제가 성립하는 것이 당연하다. 

<div class="proposition" markdown="1">

<ins id="prop2">**명제 2**</ins> 두 다항식 $u,v$에 대하여 다음이 성립한다.

1. 만일 $\deg (u)\neq\deg(v)$라면 $p+q\neq 0$이고 등식
     
    $$\deg(u+v)=\sup(\deg(u), \deg(v))$$

    이 성립한다. 만일 $\deg(u)=\deg(v)$라면 부등식 $\deg(u+v)\leq\deg(u)$이 성립한다.
2. 부등식 $\deg(uv)\leq\deg(u)+\deg(v)$이 성립한다. 

</div>

이 명제의 둘째 조건이 등식이 아닌 이유는 $A$에 있다. 이를 더 자세하게 살펴보기 위해 하나의 변수로만 이루어진 polynomial ring $A[\x]$를 생각하자. 그럼 $A[\x]$의 임의의 다항식은 

$$u(\x)=\sum_{i=0}^n a_i\x^i\qquad\text{($a_n\neq 0$)}$$

의 꼴로 적을 수 있으며, 이 때 $a_n\x^n$을 다항식 $p$의 *leading term*, 그 계수 $a_n$을 다항식 $p$의 *leading coefficient*라 부른다. 만일 $p$의 leading coefficient가 $1$이라면 $p$를 *monic polynomial*이라 부른다. 

이제 임의의 두 (일변수)다항식

$$u(\x)=\sum_{i=0}^n a_i\x^i,\qquad v(\x)=\sum_{j=0}^m b_j \x^j$$

에 대하여 이들의 곱은 명시적으로 다음의 식

$$u(\x)v(\x)=\sum_{k=0}^{n+m}\left(\sum_{i=0}^k a_ib_{k-i}\right)\x^k$$

으로 주어지며, 따라서 최고차항의 계수는 $a_nb_m$이다. 그러나 만일 $A$가 integral domain이 아니라면, 두 개의 nonzero element $a_n$, $b_m$을 곱한 것이 $0$이 될 수 있으므로 $uv$가 $m+n$차 다항식이 되지 않을 수 있다. 이 논의를 이용하면 다음을 얻는다. 

<div class="proposition" markdown="1">

<ins id="lem3">**보조정리 3**</ins> Integral domain $A$에 대하여, 다음이 성립한다.

1. 임의의 $u,v\in A[\x]$에 대하여, $\deg(uv)=\deg(u)+\deg(v)$이다. 
2. $A[\x]$의 unit은 정확히 $A$의 unit과 같다.
3. $A[\x]$는 integral domain이다. 

</div>

이제 다시 일반적인 경우를 생각하자. 임의의 두 다항식 $u,v\in A[\x\_i]\_{i\in I}$가 주어졌다 하면, 이들 다항식에서 등장하는 미지수는 어차피 유한하므로 $uv$를 계산할 때에는 $A[\x\_i]\_{i\in I}$ 대신, 유한집합 $J\subset I$를 택하여 이를 $A[\x\_j]\_{j\in J}$를 보아도 충분하다. 그럼 이 때 $A[\x\_j]_{j\in J}$가 integral domain인 것은 [보조정리 3](#lem3)과 다음의 isomorphism

$$A[\x_1,\x_2]\cong (A[\x_1])[\x_2]$$

에 의해 따라온다. 즉 다음이 성립한다. 

<div class="proposition" markdown="1">

<ins id="prop4">**명제 4**</ins> Integral domain $A$와 polynomial ring $P=A[\x\_i]\_{i\in I}$에 대하여 다음이 성립한다. 

1. 임의의 $u,v\in P$에 대해 $\deg(uv)=\deg(u)+\deg(v)$이다. 
2. $P$의 unit은 정확히 $A$의 unit과 같다.
3. $P$는 integral domain이다. 

</div>

## 일변수다항식

우리는 이제 일변수다항식에 대해 조금 더 자세히 살펴본다. 

<div class="proposition" markdown="1">

<ins id="prop5">**명제 5**</ins> $A[\x]$의 $m$차 다항식 $u(\x)$, $n$차 다항식 $v(\x)$이 주어졌다 하고, $v$의 leading coefficient를 $b_n$이라 하자. $k=\sup(m-n+1,0)$이라 하면, 다음의 식

$$b_n^k u=qv+r,\qquad \deg r < n$$

을 만족하는 $q,r\in A[\x]$가 존재한다. 

</div>

<details class="proof" markdown="1">
<summary>증명</summary>

만일 $n>m$이라면 $k=0$이고, 이 때 주어진 식은 $q=0$, $r=u$로 두면 성립하므로 이 경우에는 보일 것이 없다. 따라서 $n\leq m$이라 가정하자.  

$m$에 대한 귀납법을 사용한다. $u$의 leading coefficient를 $a_m$이라 하자. 만일

$$v(\x)=\sum_{j=0}^n b_j\x^j$$

라면, 적당한 $m$차 미만의 다항식 $u_1\in A[\x]$이 존재하여 

$$b_n^k u(\x)=b_n^{k-1}a_m\x^{m-n}v(\x)+b_n^{k-1}v_1(\x)$$

이라 쓸 수 있다. 이 식은 $v(\x)$에 $a_m\x^{m-n}$을 곱하여 leading term을 $b_n u$의 leading term과 같게 맞춰주어

$$b_nu(\x)=a_m\x^{m-n}v(\x)+u_1(\x)$$

을 얻은 후, 양 변에 $b_n^{k-1}$을 곱한 것에 불과하다. 이제 귀납적 가정에 의하여, 우리는 적당한 다항식 $q_1,r\in A[\x]$이 존재하여 다음 식

$$b_n^{k-1}u_1(\x)=q_1(\x)v(\x)+r(\x),\qquad \deg(r) < n$$

이 성립하도록 할 수 있다. 이제 이를 다시 앞선 식에 대입하면

$$b_n^k u(\x)=(b_n^{k-1}a_m\x^{m-n}+q_1(\x))v(\x)+r(\x)$$

을 얻는다. 

</details>

여기서 등장하는 계수 $b_n^k$는 $v$에서 차수를 하나씩 올려가며 $u$와 최고차항을 맞춰줄 때 생기는 것으로, 가령 $b_n$이 invertible하다면 위의 식을 만족하는 $q$와 $r$은 유일하게 결정됨을 확인할 수 있다. 특히 만일 $A$의 임의의 nonzero element가 invertible이라면, 즉 $A=\mathbb{K}$라면 우리는 위와 같은 상황에서

$$u=qv+r,\qquad \deg r < n$$

을 만족하는 $q,r$을 유일하게 결정할 수 있다. 뿐만 아니라, 이 경우 polynomial ring $\mathbb{K}[\x]$는 [보조정리 3](#lem3)에 의하여 integral domain이고, 따라서 $N:\mathbb{K}[\x] \rightarrow \mathbb{Z}^{\geq0}$를 

$$N: u\mapsto \deg(u)\qquad \text{단, $N(0)=0$}$$

으로 주면 $\mathbb{K}[\x]$가 Euclidean domain임을 안다. 

<div class="proposition" markdown="1">

<ins id="prop6">**명제 6**</ins> 임의의 field $\mathbb{K}$에 대하여, $\mathbb{K}[\x]$는 Euclidean domain이다. 

</div>

특히 Euclidean domain 위에서는 최대공약수의 개념이 잘 정의되며, 이와 관련하여 Bézout lemma 또한 성립한다. ([§정역, ⁋정리 7](/ko/math/ring_theory/integral_domains#thm7))

앞서 $\mathbb{K}[\x]$에서 $\mathbb{K}$의 임의의 (non-zero) 원소들의 image가 $\mathbb{K}[\x]$의 unit인 것을 살펴보았다. ([보조정리 3](#lem3)) 한편 Euclidean domain에서 어떠한 원소가 다른 한 원소를 나누는지의 여부는 Euclidean algorithm을 돌려서 알아낼 수 있으므로, 상수가 아닌 임의의 $u\in \mathbb{K}[\x]$가 irreducible인 것은 $u$가 $\deg(v)<\deg(u)$를 만족하는 임의의 $v\in \mathbb{K}[\x]$에 의해 나누어떨어지지 않는 것과 동치이다. 

한편 $\mathbb{K}[\x]$는 UFD이며, 따라서 $\mathbb{K}[\x]$의 irreducible element 등을 정의할 수 있다. 한편 $\mathbb{K}[\x]$의 unit은 정확히 $\mathbb{K}$의 unit과 동일하므로, 임의의 irreducible polynomial $u$는 (정의에 의해) $\deg(u)\geq 1$을 만족하며, $u$가 irreducible이므로 만일 $v\mid u$라면 $v$는 상수 다항식이거나 $u$의 상수배이다. 특히, 임의의 두 irreducible polynomial은 서로의 상수배여야만 하므로, 서로 다른 두 *monic* irreducible polynomial은 서로소이다. 이와 같이 $A[\x]$의 임의의 다항식은, leading coefficient와 monic irreducible polynomial의 곱으로 유일하게 나타낼 수 있다. 

<div class="proposition" markdown="1">

<ins id="prop7">**명제 7**</ins> 임의의 다항식 $u\in A[\x]$와 $a\in A$에 대하여, $u(\x)$를 $\x-a$로 나눈 나머지는 $u(a)$이다. 따라서, $u$가 근 $a$를 갖는 것과 $\x-a$가 $A[\x]$ 안에서 $u$의 약수인 것이 동치이다. 

</div>

이에 대한 증명은 당연히 Euclidean algorithm을 돌리면 되며, 이는 사실 중학교 때부터 익숙한 결과이다. 또 다른 결과로, 만일 $u$가 근 $a$를 갖는다면 $u$는 반드시 다음의 꼴

$$u(\x)=(\x-a)^p v(\x),\qquad v(a)\neq 0$$

로 쓰여져야 하는 것을 안다. 이 때 우리는 $p$를 근 $a$의 *multiplicity*라 부른다. 그럼 다음이 성립한다. 

<div class="proposition" markdown="1">

<ins id="prop8">**명제 8**</ins> 임의의 두 다항식 $u,v\in A[\x]$이 공통근 $a$를 갖는다 하고, $u$와 $v$ 각각에서 $a$의 multiplicity가 $p,q$라 하자. 그럼 다음이 성립한다.

1. 다항식 $u+v$에서 $a$의 multiplicity는 최소 $\inf(p,q)$이며, 등호는 $p\neq q$일 때 성립한다.
2. 다항식 $uv$에서 $a$의 multiplicity는 최소 $p+q$이며, 등호는 $A$가 integral domain일 때 성립한다.

</div>
<details class="proof" markdown="1">
<summary>증명</summary>

$u(\x) = (\x-a)^p u_1(\x)$, $v(\x) = (\x-a)^q v_1(\x)$이고 $u_1(a) \neq 0$, $v_1(a) \neq 0$라고 하자. 일반성을 잃지 않고 $p \leq q$라고 가정하면, 다음의 식

$$u(\x) + v(\x) = (\x-a)^p (u_1(\x) + (\x-a)^{q-p}v_1(\x))$$

을 얻으므로 원하는 부등식을 얻는다. 만일 여기에서 $p < q$였다면 $a$는 $u_1(\x) + (\x-a)^{q-p}v_1(\x)$의 근이 아니므로 원하는 결과를 얻는다. 

둘째 결과의 경우, 동일한 가정 하에서

$$u(\x)v(\x) = (\x-a)^{p+q}u_1(\x)v_1(\x)$$

이다. 만일 $A$가 integral domain이라면 $u_1(a)v_1(a) \neq 0$이므로 이로부터 둘째 결과를 얻는다. 

</details>

더 나아가 만일 $A$가 integral domain이라면 귀납적으로 다음을 보일 수 있다.

<div class="proposition" markdown="1">

<ins id="prop9">**명제 9**</ins> Integral domain $A$를 고정하자. $A[\x]$의 nonzero element $u$가 근 $a_1,\ldots, a_r$을 가지며, 이들의 multiplicity가 각각 $p_1,\ldots, p_r$이라 하자. 그럼 

$$u(\x)=(\x-a_1)^{p_1}\cdots(\x-a_r)^{p_r}v(\x),\qquad v(a_1),\ldots, v(a_r)\neq0$$

이도록 하는 $v\in A[\x]$가 존재한다. 

</div>
<details class="proof" markdown="1">
<summary>증명</summary>

$r$에 대한 귀납법으로 진행한다. $p=1$인 경우는 자명하므로, $u$의 $r$개의 근 $a_1,\ldots, a_r$이 주어졌다 하고, 앞의 $r-1$개의 근에 귀납적 가정을 적용하여 

$$u(\x)=u_1(\x)u_2(\x)=(\x-a_1)^{p_1}\cdots(\x-a_{r-1})^{p_{r-1}}u_2(\x)$$

이라 적자. 그럼 $A$가 integral domain이라는 가정으로부터 $u_1(a_r)\neq 0$임을 알고 있으므로, 반드시 $u_2(a_r)=0$이어야 하고 $u_2$에서 $a_r$의 multiplicity가 $p_r$이어야 한다. 이로부터 원하는 주장을 얻는다. 

</details>

특히, 임의의 integral domain $A$에 대하여, $A[\x]$의 임의의 $n$차 다항식은 (중복을 허용하여 셌을 때) 많아야 $n$개의 근을 갖는다는 것을 안다. 따라서 만일 $n$차 이하의 두 다항식 $f,g\in A[\x]$가 주어졌다 하고, 서로 다른 $n+1$개의 원소 $a_1,\ldots, a_{n+1}$에 대해 $f(a_i)=g(a_i)$가 성립한다 가정하면 $f=g$여야만 한다. 이로부터 다음의 결과를 얻는다. 

<div class="proposition" markdown="1">

<ins id="prop10">**명제 10**</ins> Field $\mathbb{K}$의 서로 다른 $n$개의 원소들 $a_1,\ldots, a_n$을 고정하자. $\mathbb{K}$의 임의의 원소들 $b_1,\ldots, b_n$에 대하여, 각각의 $i$마다

$$u_i(\x)=\prod_{j\neq i}\frac{\x-a_j}{a_i-a_j}$$

로 정의하자. 그럼 

$$u=b_1 u_1 + \cdots + b_n u_n$$

는 각각의 $i$에 대해 $u(a_i)=b_i$를 만족하는 유일한 $n$차 미만의 다항식이다. 

</div>
<details class="proof" markdown="1">
<summary>증명</summary>

유일성은 위의 논증에 의해 자명하고, 남는 것은 $u$에 각각의 $a_i$를 대입하여 그 값이 $b_i$가 나오는 것을 확인하는 것 뿐이다. 

</details>

한편, 중근을 찾아내는 방법 중 유용한 것은 주어진 다항식을 미분하는 것이다. 우리는 대수적으로 미분이 무엇인지를 정의할 수 있으나 ([\[다중선형대수학\] §미분](/ko/math/multilinear_algebra/derivations)) 이 카테고리에서는 이러한 논의 없이 정의로서 $D: A[\x] \rightarrow A[\x]$를 다음의 식

$$D:\left(u(\x)=\sum_{i=0}^n a_i\x^i\right)\mapsto \left((Du)(\x)=i.a_i\x^{i-1}\right)\tag{$\ast$}$$

로 정하기로 한다. 여기서 $i.a_i$는 

$$i.a_i=\underbrace{a_i+\cdots+a_i}_\text{\scriptsize$i$ times}$$

으로 정의되는 $A$의 원소이다. 남은 논의에서 우리가 유일하게 사용할 성질은 라이프니츠 법칙

$$D(uv)=(Du)v+u(Dv)$$

이며, 이는 [\[다중선형대수학\] §미분](/ko/math/multilinear_algebra/derivations)에서는 미분의 정의이지만 위의 식 ($\ast$)를 정의로 받아들인다면 직접 계산을 통해 확인할 수 있다. 

<div class="proposition" markdown="1">

<ins id="prop11">**명제 11**</ins> 임의의 다항식 $u \in A[\x]$에 대하여, $u$의 근 $a \in A$가 simple root이기 위한 필요충분조건은 $a$가 $Du$의 근이 아닌 것이다. 

</div>
<details class="proof" markdown="1">
<summary>증명</summary>

$a$가 $u$의 근이라는 가정에 의해 $u = (\x - a)v$이도록 하는 $v \in A[\x]$가 존재하며, 이 때 $a$가 $u$의 simple root일 필요충분조건은 $v(a) \neq 0$인 것이다. 이제 $Du = v + (\x - a)Dv$이므로, $(Du)(a) = v(a)$이다.

</details>

더 일반적으로, 귀납법을 사용하면 다음을 보일 수 있다.

<div class="proposition" markdown="1">

<ins id="prop12">**명제 12**</ins> 임의의 다항식 $u \in A[\x]$에 대하여, $u$의 근 $a \in A$가 multiplicity $k$를 가진다면, $a$는 $Du$의 multiplicity $\geq k-1$의 근이다. 만일 $k \cdot 1$이 $A$에서 cancellable하다면, $a$는 $Du$에 대해 order $k-1$을 가진다.

</div>
<details class="proof" markdown="1">
<summary>증명</summary>

위의 명제와 비슷하게 $u=(\x-a)^k v$로 두고 $v(a)\neq 0$이므로, 

$$Du=k(\x-a)^{k-1}v+(\x-a)^k Dv=(\x - a)^{k-1}(kv + (\x - a)Dv)$$

로부터 첫 번째 주장을 얻는다. 만일 $k\cdot 1$이 $A$에서 cancellable하다면, $kv+(\x-a)Dv$에 $\x=a$를 대입한 값 $k.v(a)$가 $0$이 아니게 되어 나중의 주장이 성립한다. 

</details>

<div class="proposition" markdown="1">

<ins id="prop13">**명제 13**</ins> Integral domain $A$와 집합 $I$가 주어졌다 하고, $(H\_i)\_{i\in I}$를 $I$로 index된 $A$의 무한한 부분집합들의 family라 하자. 또, $H=\prod_{i\in I} H_i\subseteq A^I$라 하자. 그럼 만일 $u$가 $A[\x\_i]\_{i\in I}$의 non-zero element이라 하면, $H$와 다음의 집합

$$H_u=\{(\x_i)\in H\mid u(\x_i)\neq 0\}$$

이 같은 cardinality를 갖는다. 

</div>
<details class="proof" markdown="1">
<summary>증명</summary>

$I$가 유한집합인 경우는 귀납법으로 보일 수 있다. $\lvert I\rvert=n$이라 하고, $n$에 대한 귀납법으로 증명하자. 우선 $n=0$인 경우는 증명할 것이 없다. 귀납법을 사용하기 위해 표기를 단순화하여 $I=\\{1,\ldots, n\\}$이라 하고, $J=\\{1,\ldots, n-1\\}$ 그리고 $B=A[\x\_i]\_{i\in J}$라 하자. 그럼 $u\neq 0$이므로

$$u=\sum_{k=0}^m v_k\x_n^k$$

이도록 하는 $v_k\in B$들이 존재한다. 여기서 $v_m\neq 0$이다. 이제 귀납적 가정에 의하여, 집합

$$H_{v_m}=\{(\x_i)\in H\mid v_m(\x_i)\neq 0\}$$

은 $\prod\_{i\in J} H_i$와 같은 cardinality를 가진다. 이제 $\prod\_{i\in J} H_i$의 임의의 원소 $(x\_i)\_{i\in J}$에 대하여, 

$$w(\x)=\sum_{k=0}^mv_k(x_1,\ldots, x_{n-1})\x_n^k$$

는 $0$이 아닌 다항식이다. 한편, 집합

$$\{a\in H_n\mid w(a)\neq 0\}$$

은, $H_n$이 무한집합이라는 사실과 [명제 9](#prop9) 이후의 논증, 그리고 [\[집합론\] §자연수와 무한집합, ⁋명제 12](/ko/math/set_theory/natural_numbers#prop12)로부터

$$\lvert H\rvert\geq \lvert H_u\rvert\geq \lvert H_{v_m}\rvert\lvert H_n\rvert=\lvert H\rvert$$

이 성립한다. $I$가 무한집합인 경우에는 $u$에 등장하는 미지수들만을 포함하는 polynomial ring을 생각하여 유한집합인 케이스로 줄일 수 있다.

</details>

특히, 만일 $I$가 공집합이 아니라면  $H_u$는 무한집합이 된다. 

## 인수분해

임의의 ring homomorphism $\phi:A \rightarrow B$가 주어졌다 하면, 임의의 $u\in A[\x\_i]\_{i\in I}$는 $\phi$를 통해 $B[\x\_i]\_{i\in I}$의 원소로 볼 수 있다.

특별히 $A$가 integral domain이고 $\phi$가 canonical inclusion $A \hookrightarrow \Frac(A)$인 경우를 생각하자. 그럼 $\Frac(A)$는 field이므로 [명제 6](#prop6)에 의하여 $(\Frac A)[\x]$는 Euclidean domain이고, 따라서 임의의 $u\in A[\x]$를 $(\Frac A)[\x]$로 본다면 $u$는 적어도 $(\Frac A)[\x]$에서는 인수분해가 가능하다. 그렇다면 여기에서 실행한 인수분해가 $A[\x]$에서는 어떻게 반영되는지를 살펴보는 것이 당연한 순서일 것이다. 

<div class="proposition" markdown="1">

<ins id="prop14">**명제 14 (Gauss)**</ins> UFD $A$와 그 field of fraction $\Frac(A)$, 그리고 $A[\x]$의 원소 $u$를 생각하자. 만일 $u$가 $(\Frac A)[\x]$에서 reducible이라면, $u$는 $A[\x]$에서도 reducible이다.

</div>
<details class="proof" markdown="1">
<summary>증명</summary>

$(\Frac A)[\x]$의 다항식 $u$가 두 다항식의 곱

$$u(\x)=\tilde{v}_1(\x)\tilde{v}_2(\x),\qquad \tilde{v}_i\in (\Frac A)[\x]$$

으로 나타난다 하자. 그럼 $\tilde{v}_1$과 $\tilde{v}_2$의 계수들의 최대공배수들을 양변에 곱하여, 적절한 $a\in A$에 대하여

$$a u(\x)=v_1(\x)v_2(\x)$$

이도록 하는 $v_i\in A[\x]$들이 존재한다. 만일 $a$가 unit이라면 더 중명할 것이 없으므로, $a$가 unit이 아니라 가정하자. 그럼 $a=p_1\cdots p_r$이도록 하는 irreducible element $p_i\in A$들이 존재한다. 이 때, [§정역, ⁋명제 17](/ko/math/ring_theory/integral_domains#prop17)에 의하여 $(p_i)$는 $A$의 prime ideal이며, 따라서 

$$(A/p_iA)[\x]\cong A[\x]/P_i$$

는 [명제 4](#prop4)에 의해 integral domain이다. 따라서 등식 $au=v_1v_2$를 $P_i$로 mod out 하고 나면, $v_1$ 혹은 $v_2$가 $(A/p_iA)[x]$에서 $0$이 되어야 하는 것을 안다. 즉, $v_1$ 혹은 $v_2$ 중 하나의 계수들은 모두 $p_i$의 배수이며, 따라서 이 $p_i$를 약분하여 $A[\x]$의 또 다른 polynomial을 얻을 수 있다. 이제 이를 모든 $p_i$에 대해 적용하면 원하는 결과를 얻는다.

</details>

이로부터 다음을 얻는다. 

<div class="proposition" markdown="1">

<ins id="cor15">**따름정리 15**</ins> UFD $A$와 그 field of fraction $\Frac A$, 다항식 $u(\x) \in A[\x]$를 생각하고 $u(\x)$의 계수들의 최대공약수를 $1$이라 하자. 만약 $u(\x)$가 $A[\x]$에서 irreducible이면, $u(\x)$는 $(\Frac A)[\x]$에서도 irreducible이다.

</div>
<details class="proof" markdown="1">
<summary>증명</summary>

[명제 14](#prop14)에 의하여, $u(\x)$가 $(\Frac A)[\x]$에서 reducible이면, $A[\x]$에서도 reducible하다. 

반대로, $u(\x)$의 계수들의 최대공약수가 1이라고 하고, $u(\x)$가 $A[\x]$에서 reducible이라 하자. 즉 

$$u(\x) = v_1(\x) v_2(\x)$$

이라 할 수 있으며, 이 때 $v_1(\x)$와 $v_2(\x)$의 계수들의 최대공약수 역시 1이어야 하므로 특히 $v_1,v_2$는 둘 다 상수가 아니다. 이로부터  $u=v_1v_2$는 $(\Frac A)[\x]$에서 보았을 때에도 $u$가 reducible이라는 것을 의미한다. 

</details>

그럼 인수분해와 관련된 핵심적인 결과 중 하나는 다음의 정리이다.

<div class="proposition" markdown="1">

<ins id="thm16">**정리 16**</ins> $A$가 UFD일 필요충분조건은 $A[\x]$가 UFD인 것이다.

</div>
<details class="proof" markdown="1">
<summary>증명</summary>

$A[\x]$가 UFD이면 $A$도 UFD임은 자명하므로, 반대방향만 보이면 충분하다.

UFD $A$에 대하여, $A[\x]$의 $0$이 아닌 원소를 $u(\x)$라 하고, $u(\x)$의 계수들의 최대공약수를 $d$라 하면 $u(\x)=du_0(\x)$로 두어 계수들의 최대공약수가 $1$인 다항식 $u_0\in A[\x]$를 얻어낼 수 있으므로 우리는 일반성을 잃지 않고 $u$의 계수들의 최대공약수가 $1$이라 가정할 수 있다. 

[명제 6](#prop6)에 의해 $u$는 $(\Frac A)[\x]$에서 유일한 방식으로 인수분해를 할 수 있으며, [명제 14](#prop14)를 이 인수분해에 적용하면 우리는 $u$를 $A[\x]$에서 인수분해할 수 있다. 한편, $u$의 계수들의 최대공약수는 $1$이므로, 이렇게 얻어진 $u$의 factor들의 계수들의 최대공약수 또한 $1$이고 따라서 [따름정리 15](#cor15)에 의해 이들은 $A[\x]$에서 irreducible이다. 이로부터 $u$의 $A[\x]$에서의 인수분해를 얻으며, 유일성은 이들 각각의 성분이 $(\Frac A)[\x]$에서 해당하는 인수들의 $\Frac A$-multiple이라는 사실을 이용하면 자명하다. 

</details>