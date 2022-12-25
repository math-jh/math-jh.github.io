---

title: "타원곡선"
excerpt: "Basic notions"

categories: [Math / Algebraic Number Theory]
permalink: ko/math/algebraic_number_theory/elliptic_curves
header:
    overlay_image: /assets/images/Algebraic_number_theory/Elliptic_curves.png
    overlay_filter: 0.5
sidebar: 
    nav: "further_topics"

date: 2021-09-10
last_modified_at: 2022-06-06
weight: 1

published: false

---

<div class="notice--warning" markdown="1">

이 글은 현재 수정중입니다.

이 글은 예전에 쓴 글로, 서술 방향이 마음에 들지 않거나 표기법이 마음에 들지 않아 전체적으로 수정이 진행중입니다. 읽으실 때 참고해주세요.

</div>

## Elliptic curves

우리는 복소해석학의 마지막 부분에서 elliptic curve를 정의했었는데, 이 elliptic curve들은 정수론과 밀접한 관련이 있다. 예를 들어, 수론에서 가장 유명한 문제들 중 하나인 페르마의 마지막 정리 또한 타원곡선에 대한 정리인 시무라-타니야마 추론을 사용해 증명되었다. 

예를 들어, elliptic curve $y^2=x^3-2$를 생각하자. 페르마는 이 식의 정수해는 $(3,\pm 5)$ 뿐이라는 것을 증명하였다. 그의 아이디어는 이 식을 *algebraic number field* $\mathbb{Q}[\sqrt{-2}]$에서 생각하는 것이었다. 위의 식은 $x^3=y^2+2$이므로, $\mathbb{Q}[\sqrt{-2}]$에서의 $\mathbb{Z}$의 integral closure $\mathbb{Z}[\sqrt{-2}]$에서는 다음과 같이 인수분해될 수 있다.

$$x^3=(y+\sqrt{-2})(y-\sqrt{-2})$$

다행히도 $\mathbb{Z}[\sqrt{-2}]$는 UFD이므로 (사실 Euclidean domain이기도 하다), 만일 우리가 $y\pm\sqrt{-2}$가 서로소라는 것만 보인다면, $y\pm\sqrt{-2}$는 각각 

$$u p_1^{3n_1}p_2^{3n_2}\cdots p_k^{3n_k},\qquad vq_1^{3m_1}q_2^{3m_2}\cdots q_l^{3m_l}$$

의 꼴들로 나타나야 하고, irreducible들 $p_i$와 $q_j$들은 서로 겹치지 않아야 한다. 그런데 $\mathbb{Z}[\sqrt{-2}]$에서의 norm을 생각하면, $\mathbb{Z}[\sqrt{-2}]$의 unit은 $\pm 1$ 뿐이므로 (그리고 $\pm1$은 각각 세제곱수이므로) $y\pm \sqrt{-2}$들은 모두 cubic이다. 이제

$$y+\sqrt{-2}=(a+b\sqrt{-2})^3=a(a^2-6b^2)+b(3a^2-2b^2)\sqrt{-2}$$

이므로, $1=b(3a^2-2b^2)$으로부터 $b=\pm 1$이고, 이를 다시 대입하면 $\pm 1=3a^2-2$를 얻는다. 따라서 $3a^2=3$, 그리고 $b=1$일 수밖에 없으므로 $y$는 $a=1$이면 $-5$, $a=-1$이면 $5$가 되어야 한다. 이 경우 모두에 $x=3$이므로, 우리는 원하는 대로 이 식의 정수해가 $(3,\pm 5)$라는 것을 증명하였다.

그러나, 우리는 이 argument가 굉장히 한정적이라는 것 또한 알고 있다. 예를 들어, $\mathbb{Z}[\sqrt{-5}]$에서, 

$$6=2\cdot 3=(1+\sqrt{-5})(1-\sqrt{-5})$$

이고, 이들 두 factorization은 서로 다르다는 것을 쉽게 증명할 수 있다. 즉, $\mathbb{Z}[\sqrt{-5}]$는 UFD가 아니고, 따라서 우리가 위에서 한 argument를 사용할 수 없다.

이런 문제를 해결하기 위한 데데킨트와 쿰머의 아이디어는, 이들 $2$, $3$이나 $1\pm \sqrt{-5}$ 등이 모두 충분히 나누어지지 않았기 때문이라는 것이고, 이를 위해 *이상적인* 숫자들, 즉 *ideal*의 개념을 도입하게 된다. 예를 들어, ring $\mathbb{Z}[\sqrt{-5}]$에서의 ideal $(2)$은 다음의 ideal product 

$$(2)=(2, 1+\sqrt{-5})(2, 1+\sqrt{-5})$$

를 통해 한 번 더 분해되며, $(3)$은 

$$(3)=(3, 1+\sqrt{-5})(3, 1-\sqrt{-5})$$

을 통해 한 번 더 분해된다는 것을 알 수 있다. 약간의 계산을 통해, 예를 들어 

$$(2, 1+\sqrt{-5})(3, 1-\sqrt{-5})=(1-\sqrt{-5})$$

임을 체크할 수 있다. 즉, 우리는 이렇게 숫자들 대신 ideal들로 인수분해를 진행함으로써 UFD와 비슷한 성질을 얻을 수 있게 된다.  

## Localization

이렇게 ideal들을 도입하면, 우리는 prime ideal이 실제로 prime element와 비슷한 역할을 할 것임을 이름으로부터 추측할 수 있다. 그리고, prime ideal을 다룰 때 좋은 도구는 localization이었다. 

Integral domain $R$과, $R$의 multiplicative subset $S$에 대하여, $R$을 $S$에서 localize한 것을 $R_S$로 표기하자. 특히, prime ideal $\mathfrak{p}$에 대하여, $R\setminus\mathfrak{p}$는 multiplicative subset이 되는데, 이 경우를 특히 자주 마주할 예정이므로 이 또한 ($R\_{R\setminus\mathfrak{p}}$ 대신) $R\_\mathfrak{p}$로 적는다. 

한편, 일반적인 대수 시간에 우리가 배운 correspondence에 따르면, <span class="border-highlight">$R_S$의 prime ideal들</span>과, <span class="border-highlight">$R$의 prime ideal들 중 $S$와 만나지 않는 것들</span> 사이의 inclusion-preserving bijection이 존재하며, 이 bijection은 explicit하게

$$\mathfrak{p}\mapsto \mathfrak{p}R_S, \qquad \mathfrak{q}\mapsto \mathfrak{q}\cap R$$

로 주어진다. 따라서, 만일 $S=R\setminus\mathfrak{p}$일 경우, 이 성질은 정확히 <span class="border-highlight">$R_\mathfrak{p}$의 prime ideal들</span>과 <span class="border-highlight">$\mathfrak{p}$에 속한 $R$의 prime ideal들</span> 사이의 inclusion-preserving bijection을 준다. 그러므로

<div class="proposition" markdown="1">

<ins id="pp1">**명제 1**</ins> Integral domain $R$과, $R$의 prime ideal $\mathfrak{p}$에 대하여, $R\_\mathfrak{p}$는 유일한 maximal ideal $\mathfrak{p}R\_\mathfrak{p}$를 갖는다. 

</div>

이렇게 유일한 maximal ideal을 갖는 ring을 *local ring*이라 부른다. 

## Algebraic integers

우리는 이 글의 맨 도입부분에서 $\mathbb{Q}[\sqrt{-2}]$를 *algebraic number field*라고 지칭했었는데, 이제 이를 엄밀하게 정의한다. *Algebraic number field*란, 다른 것이 아니고 그냥 $\mathbb{Q}$의 finite extension을 뜻한다. 그러니 사실 이 정의 자체는 별로 흥미로울 것이 없다. 우리가 흥미있게 바라보는 것은, 이 algebraic number field에서 정수의 역할을 하는 ($\mathbb{Q}$에서 $\mathbb{Z}$가 그러하듯이) 원소들에 대한 것이다. 

<div class="definition" markdown="1">

<ins id="df2">**정의 2**</ins> 주어진 ring $R$과, $R$을 subring으로 갖는 또 다른 ring $R'$에 대하여 $b\in R'$이 $R$에 대해 *integral*이라는 것은 $f(b)=0$을 만족하는 *monic* polynomial $f\in R[x]$가 존재하는 것이다.  

</div>

즉, integral element라는 것은 algebraic number와 거의 같은데, 다만 polynomial이 monic이라는 조건이 추가된 것이다. 만약 $R$이 field였다면, algebraic number $\alpha$의 minimal polynomial을 항상 monic으로 만들 수 있겠지만, 일반적으로 $R$이 field가 아닌 경우는 두 개념은 서로 다르다. 그럼에도 불구하고 integral element는 algebraic number와 거의 비슷한 느낌의 개념이다. 

<div class="proposition" markdown="1">

<ins id="pp3">**명제 3**</ins> [정의 2](#df2)의 상황에서, 다음이 모두 동치이다.

1. $b$가 $R$에 대해 integral이다.
2. $R[b]$가 finitely generated $R$-module이다.
3. $R[b]$는 $R'$의 subring 중, 그 자체로 finitely generated $R$-module인 어떤 subring $B$에 포함되어있다.
4. $R$-module로써 finitely generated인 $R[b]$-module $M$이 존재하여, $yM=0$을 만족하는 유일한 $y\in R[b]$는 $y=0$ 뿐이다. 

</div>
<details class="proof" markdown="1">
<summary>증명</summary>

우선 1이 성립하면 2가 성립하는 것은 field extension에서와 마찬가지로 자명하다. 또, 2가 성립한다고 하면 $R[b]$ 자체가 3의 조건을 만족하는 finitely generated $R$-module이자 subring이 되며, 만일 3번이 성립한다고 하면 $M=R[b]$로 두면 $R[b]$ 자기 자신은 $R[b]$-module이며, $1\in R[b]$이므로 $yM=0$이려면 $y1=0$이고 따라서 이를 만족하는 $y$는 $0$ 뿐이다.

따라서 가장 덜 자명한 파트는 4번에서 1번으로 가는 파트다. 4번을 가정하고, $M=\sum_1^n m_iR$ ($m_i\in R$)이라 하자. 그럼 $b\in R[b]$이므로, $M$의 원소 $m_i$들에 대한 각각의 scalar multiplication $bm_i$들이 잘 정의되며, $(m_i)$들이 $R$-module $M$을 generate하므로 적당한 $R$의 원소들 $r_{ij}$가 존재하여 다음의 식

$$bm_i=\sum_j r_{ij}m_j$$

이 모든 pair $i,j$에 대해 성립하도록 할 수 있다. 이를 행렬로 적으면 다음의 식

$$\begin{pmatrix}bm_1\\bm_2\\ \vdots\\ bm_n\end{pmatrix}=\begin{pmatrix}r_{11}&r_{12}&\cdots&r_{1n}\\r_{21}&r_{22}&\cdots& r_{2n}\\\vdots&\vdots&\ddots&\vdots\\ r_{n1}&r_{n2}&\cdots&r_{nn}\end{pmatrix}\begin{pmatrix}m_1\\ m_2\\ \vdots\\ m_n\end{pmatrix}$$

이 된다. 편의상 우변의 $n\times n$ 행렬을 $B$라 적자. 우변의 식을 좌변으로 이항하면

$$\begin{pmatrix}b-r_{11}&-r_{12}&\cdots&-r_{1n}\\ -r_{21}&b-r_{22}&\cdots&-r_{2n}\\ \vdots&\vdots&\ddots&\vdots\\ -r_{n1}&-r_{n2}&\cdots&-r_{nn}\end{pmatrix}\begin{pmatrix}m_1\\ m_2\\ \vdots\\ m_n\end{pmatrix}=0$$

이다. 위에서 구한 $n\times n$ 행렬을 $A$라 하고, $\det A$를 $d$라 하자. 만일 $d\neq 0$이라면, $A$의 adjoint matrix를 곱해주면

$$A^\text{adj}A\begin{pmatrix}m_1\\m_2\\ \vdots\\ m_n\end{pmatrix}=d\begin{pmatrix}m_1\\m_2\\ \vdots\\ m_n\end{pmatrix}=0$$

이 되므로 모순이다. 따라서 $d=0$이어야 한다. 이제 다항식 $f(\x)$를 다음의 식

$$f(\x)=\det(\xI-B)$$

이라 하면, $f$는 모든 계수가 $R$의 원소인 monic polynomial이 되고, $f(b)=0$임을 앞서 보였으므로 $b$는 원하던 것과 같이 $R$에 대해 integral이다.

</details>

Integral element들의 중요한 성질 중 하나는, 이러한 상황에서 $R$에 대해 integral인 원소들을 모아둔 것이 $R'$의 subring이 된다는 것이다.

<div class="proposition" markdown="1">

<ins id="pp4">**명제 4**</ins> [정의 2](#df2)의 상황에서, $R$에 대해 integral인 원소들을 모두 모아둔 집합은 $R'$의 subring이다.

</div>
<details class="proof" markdown="1">
<summary>증명</summary>

사실 이보다 더 강한 명제를 보일 수 있다. 즉, 

> 만일 $b_1,\ldots, b_n\in R'$이 $R$에 대해 integral이라면, $R[b_1, \ldots, b_n]$은 finitely generated $R$-module이다. 

이 명제는 $n$에 대한 귀납법으로 쉽게 보일 수 있다. 우선 $n=1$인 경우는 앞선 명제의 2번 동치조건에 의해 성립한다. 이제 $n>1$에 대해, $R\'\'=R[b_1,\ldots, b_{n-1}]$이 finitely generated $R$-module이라 가정하고, 이 때의 $R$-generator를 $a_1,\ldots, a_s$라 하자. $b_n$은 $R$에 대해 integral이고, $R''$은 $R$을 포함하므로 $b_n$은 $R''$에 대해서도 integral이다. 따라서 $R\'\'[b_n]$은 다시 2번 동치조건 (그리고 algebraic element의 경우와 동일해서 생략한 증명과정)에 의하여 $1,b_n, b_n^2,\ldots, b_n^k$에 의해 generate된다. 이제, $R\'\'[b_n]$의 임의의 원소 $x$는 우선 다음의 식

$$x=\sum_{i=1}^k t_ib_n^i,\qquad t_i\in R''$$

으로 적을 수 있고, 각각의 $t_i$들은 $R\'\'$의 원소로서 다음의 식

$$t_i=\sum_{j=1}^s r_{ij}a_j$$

으로 적을 수 있으므로, 

$$x=\sum_{i,j} r_{ij}a_jb_n^i$$

가 성립한다. 즉, $R\'\'[b_n]=R[b_1, \ldots, b_n]$의 임의의 원소 $x$는 $a_jb_n^i$들의 $R$-linear combination으로 나타낼 수 있으므로 finitely generated $R$-module이 된다. 

이제 원래의 명제는 자명하다. $R$에 대해 integral인 두 원소 $x,y$에 대하여 $B=R[x,y]$가 finitely generated $R$-module이고, 따라서 $x\pm y, xy\in B$이다. 그럼 [명제 3](#pp3)의 3번 동치조건에 의하여 $x\pm y$와 $xy$는 모두 integral element가 된다.  

</details>

우리는 이렇게 얻어진 subring을 $R$의 $R'$에서의 *integral closure*라고 부른다. 그럼 만약 $R$의 $R'$에서의 integral closure가 자기 자신이라면, $R$을 $R'$에서 *integrally closed*라 부르는 것이 타당할 것이다. 우리는 또, $R\subset R'$이고 $R'$의 모든 원소가 $R$에 대해 integral이라면 $R'$이 $R$에 대해 integral이라 부르는데, 그럼 $R$의 $R'$에서의 integral closure는 언제나와 같이, $R'$에 대해 integrally closed인 $R$의 extension 중 가장 작은 것임을 쉽게 확인할 수 있다. 많은 경우, 우리가 마주하게 되는 상황은 $R$이 integral domain이고, $R'$이 $R$의 field of fraction이 되는 경우이다. 이런 경우 우리는 $R'$을 특별히 명시하는 대신, *$R$이 integrally closed이다*, 혹은 *$R$의 integral closure*등과 같이 생략해서 말하기도 한다.

예컨대 $R=\mathbb{Z}$와 $R'=\mathbb{Q}$가 이런 상황인데, 우리는 $\mathbb{Q}$ 안에서 $\mathbb{Z}$에 대해 integral인 원소는 오직 $\mathbb{Z}$의 원소들 뿐이라는 것을 알고 있다. 즉, $\mathbb{Z}$는 integrally closed이다. 하지만 만약 $\mathbb{Q}$ 대신 조금 더 큰 $\mathbb{Q}[\sqrt{-2}]$를 생각하면 이 field에서 $\mathbb{Z}$는 integrally closed가 아니다. 예를 들어, $\sqrt{-2}$는 monic polynomial $x^2+2$의 근이 되지만 $\mathbb{Z}$의 원소가 아니다. 일반적으로 다음이 성립한다.

<div class="example" markdown="1">

<ins id="ex5">**예시 5**</ins> $\mathbb{Q}[\sqrt{d}]$에서, $\mathbb{Z}$의 integral closure는

$$\mathbb{Z}[\sqrt{d}]=\mathbb{Z}+\mathbb{Z}\sqrt{d}\qquad\text{if $d\equiv 2,3\mod 4$},$$

그리고

$$\mathbb{Z}\left[\frac{1+\sqrt{d}}{2}\right]=\mathbb{Z}+\mathbb{Z}\frac{1+\sqrt{d}}{2}\qquad\text{ if $d\equiv 1\mod 4$}$$

으로 주어진다. 

</div>

Integrality는 다음과 같이 transitive하게 잘 작동한다.

<div class="proposition" markdown="1">

<ins id="pp6">**명제 6**</ins> $R\subset R'\subset R\'\'$이고, $R'$이 $R$에 대해 integral이고, $R\'\'$이 $R'$에 대해 integral이라 하자. 그럼 $R\'\'$은 $R$에 대해 integral이다.

</div>
<details class="proof" markdown="1">
<summary>증명</summary>

임의의 $b\in R\'\'$을 골라오자. 그럼 $b$는 $R'$에 대해 integral이므로, $R'$의 원소들 $t_i$가 존재하여

$$f(\x)=\x^n+t_{n-1}\x^{n-1}+\cdots+t_1\x+t_0$$

이 $f(b)=0$을 만족한다. 그런데 $B=R[t_1,\ldots, t_{n-1}]$에 [명제 4](#pp4)에서 증명했던 claim을 적용하면, 이는 $R$-module로서 finitely generated이고, 따라서 $B[b]$도 finitely generated $R$-module이므로 [명제 3](#pp3)의 세 번째 동치조건에 의해 $b$는 $R$에 대해 integral이다.

</details>

마지막으로 몇 개의 예시만 살펴보고 이야기를 마무리하자.

<div class="example" markdown="1">

<ins id="ex7">**예시 7**</ins> 임의의 unique factorization domain은 integrally closed이다. $R$이 unique factorization domain이라 하고, $K=\FracR$이라 하자. $R$이 integrally closed임을 보이는 것은, 임의의 $x/y\in K$가 integral이라면, 사실 $x/y\in R$도 성립함을 보이는 것이다. $R$에서의 unique factorization을 이용하여, $x$와 $y$가 non-unit인 common factor를 갖지 않도록 할 수 있다. 이제 $x/y$가 다음의 식

$$\left(\frac{x}{y}\right)^n+s_{n-1}\left(\frac{x}{y}\right)^{n-1}+\cdots+s_0=0,\qquad s_i\in R$$

을 만족한다 가정하자. 그럼

$$\left(\frac{x}{y}\right)^n=\sum_{i=0}^{n-1} r_i\left(\frac{x}{y}\right)^i$$

이라 할 수 있고, 양 변에 $y^n$을 곱하면

$$x^n=\sum_{i=0}^{n-1}r_ix^iy^{n-i}=y\sum_{i=0}^{n-1}r_ix^iy^{n-1-i}$$

이라 할 수 있다. 따라서 $y$는 $x^n$을 나눈다. 만약 $y$가 $R$에서 unit이 아니라면, $y$를 나누는 어떤 prime factor $p$가 $x^n$을 나눠야 하고, 그러한 $p$는 $x$ 또한 나누므로 이는 $x,y$가 서로소라는 원래의 가정에 모순이다. 따라서 $y$는 unit이고, $x/y=xy^{-1}\in R$이 성립한다.

특히, 임의의 principal ideal domain은 항상 unique factorization domain이므로 모든 PID는 integrally closed이다.
 
</div>

<div class="example" markdown="1">

<ins id="ex8">**예시 8**</ins> $R$이 integrally closed라 가정하자. $S$를 $R$의 multiplicative subset이라 하면, $R_S$ 또한 integrally closed이다.

</div>

---

**References**

[Jan] Gerald J. Janusz. *Algebraic Number Fields*, American  Mathematical Soc., 1995
