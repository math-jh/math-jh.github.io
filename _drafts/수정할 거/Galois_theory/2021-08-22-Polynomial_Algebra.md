---

title: "Polynomial algebra"
excerpt: "다항식의 성질들"

categories: [Math / Galois Theory]
permalink: /ko/math/galois_theory/polynomial_algebra
header:
    overlay_image: /assets/images/Galois_theory/Polynomial_algebra.png
    overlay_filter: 0.5
sidebar: 
    nav: "algebraic_structures"

date: 2021-08-22
last_modified_at:
weight: 1

published: false

---
<div class="notice--warning" markdown="1">

이 글은 현재 수정중입니다.

이 글은 예전에 쓴 글로, 서술 방향이 마음에 들지 않거나 표기법이 마음에 들지 않아 전체적으로 수정이 진행중입니다. 읽으실 때 참고해주세요.

</div>

모든 ring은 commutative ring with unity $1$이고, 모든 ring homomorphism은 unital이다.

Galois theory를 공부하기 전에, 우선 우리가 필요로 하는 도구들을 정리하자. (사실 이걸 쓰는 시점에 아직 부르바키의 3, 4단원을 안 봐서 공부 목적으로 쓰는 중)

## Review of polynomial Algebra

임의의 ring $R$에 대하여, 우리가 ring of polynomial이라 불렀던 집합 $R[X]$를 생각해보자. 이는 당연히 $R$-module structure를 가지며, 또 ring of polynomial이라는 이름답게 ring structure도 가진다. 따라서 이 집합은 사실 $R$-algebra로 보는 것이 타당하다.[^1] 그럼 $R[X]$의 모든 원소들은 다음의 식

$$f(X)=a_dX^d+a_{d-1}X^{d-1}+\cdots+a_1X+a_0$$

의 꼴이다. 혹은 더 일반적으로, finitely supported family $(a_n)_{n\in \mathbb{N}}$에 대해

$$f(X)=\sum_{n\in\mathbb{N}} a_nX^n$$

의 꼴이라 할 수도 있을 것이다. 그럼, 우리는 집합 $\supp(a\_n)\_{n\in\mathbb{N}}$의 maximal element $d$를 $f(X)$의 *degree*라 하고, $a\_dX^d$를 leading term, $a_d$를 leading coefficient라 부른다. Leading coefficient가 $1$이라면, 이 다항식 $f$를 monic polynomial이라 부른다. 우리는 $f(X)$를 이루는 각각의 $a\_nX^n$를 degree $n$짜리 *term*이라 부르고, 하나의 term만으로 이루어진 다항식들 $X^n$들은 각각 degree $n$의 *monomial*들이라 부른다. 

더 일반적으로, variable들의 family $(X\_i)\_{i\in I}$가 주어졌다 하고, 이들에 의해 generate된 free $R$-algebra $R[X]$를 생각히자. 이 $R$-algebra의 모든 원소들을 표현하려면 다음과 같은 multi-index notation을 먼저 도입하는 편이 좋다.  
$\mathbb{N}^{(I)}$를 $\supp(\alpha\_i)\_{i\in I}$가 finite인 자연수 수열들의 모임이라 하자. 수열 $\alpha=(\alpha_i)\_{i\in I}\in\mathbb{N}^{(I)}$에 대하여, 다음의 식

$$X^\alpha=\prod_{i\in I}X_i^{\alpha_i}$$

을 통해 먼저 monomial들을 정의할 수 있다. $\alpha$를 $X$의 degree처럼 본다면 임의의 다항식은 degree $\alpha$의 monomial들의 합으로 나타낼 수 있고, 더 편하게 표기하기 위해 $\lvert\alpha\rvert=\sum\_{i\in I}\alpha\_i$로 정의하면, $R[X]$의 모든 원소들은 

$$f(X)=\sum_{\lvert\alpha\rvert=0}^\infty a_\alpha X^\alpha$$

의 꼴로 나타낼 수 있다. 물론 single-variable polynomial때와 마찬가지로, $(a\_\alpha)\_{\lvert\alpha\rvert\in\mathbb{N}}$은 finitely supported이다. 우리는 $X^\alpha$를 degree $\alpha$의 monomial이라 부르기로 하였으므로,  $a\_\alpha X^\alpha$는 degree $\alpha$짜리 term이라 부르면 적절할 것이다. 또, $f(X)$의 degree $\deg f$는 $\supp(a\_\alpha)\_{\lvert\alpha\rvert\in\mathbb{N}}$의 원소들 중 최대의 degree로 정의된다. 

다음의 사실은 자명하다.

<div class="proposition" markdown="1">

<ins id="pp1">**명제 1**</ins> $f$, $g$가 $R[X]$의 원소들이라 하자. 그럼 다음의 식들이 성립한다. 

$$\deg(f+g)=\sup(\deg f, \deg g),\qquad \deg(fg)\leq\deg f+\deg g.$$

</div>

여기서, 후자에 부등호가 들어있는 이유는 zero divisor의 존재 때문이고, 따라서 만일 $f$와 $g$의 leading coefficient가 모두 zero divisor가 아니라면 등호가 성립한다. 그러므로, monic polynomial $f$, $g$에 대해서는 항상 $\deg(fg)=\deg f+\deg g$이고, 또 만일 coefficient ring $R$이 integral domain이라면 임의의 polynomial에 대하여 $\deg(fg)=\deg f+\deg g$가 성립한다. 특히, 이들 조건이 만족된다면 $f$와 $g$는 zero divisor가 아니다 ($fg$의 degree가 $0$보다 크므로)

사실 $R[X]$는 단순한 algebra도 아니고, 바로 위에서 정의한 degree를 통해 grading이 주어진 graded algebra이다.

<div class="definition" markdown="1">

<ins id="df2">**정의 2**</ins> Ring $R$이 다음과 같은 additive group $R_n$들의 direct sum

$$R=\bigoplus_{n=0}^\infty R_n$$

으로 나타내어진다고 하자. 만일 $R_mR_n\subset R_{m+n}$이라면 이 ring을 *$\mathbb{Z}^{\geq 0}$-graded ring*이라 부른다. 0이 아닌 $R_n$의 각각의 원소들은 *homogeneous element of degree $n$* 이라 부르고, 임의의 $x\in R$이

$$x=\sum_{n=0}^\infty x_n$$

으로 나타난다면 (당연히 $(x_n)_{n\geq 0}$은 finitely supported) nonzero인 각각의 $x_n$들을 $x$의 *homogeneous component*라 부른다. 
</div>

Grading을 주는 $\mathbb{Z}^{\geq 0}$을 일반적인 monoid $\Delta$로 일반화할 수도 있지만, 보통은 index set을 지금과 같이  $\mathbb{Z}^{\geq 0}$으로 잡으므로 $\mathbb{Z}^{\geq 0}$-graded ring을 그냥 간단히 graded ring이라고 부른다. 

<div class="example" markdown="1">

<ins id="ex3">**예시 3**</ins> 임의의 ring $R$과 ideal $I$에 대하여, 다음과 같이 graded ring을 대응시킬 수 있다.

$$\operatorname{gr}_IR=\bigoplus_{n=0}^\infty I^n/I^{n+1}$$

덧셈은 자명하게 주어지며, 곱셈은 우선 homogeneous element $a+I^{n+1}$, $b+I^{m+1}$를 곱한 것을 $ab+I^{m+n+1}$로 정의한 후 distributivity를 사용하면 된다.  
</div>

<div class="definition" markdown="1">

<ins id="df4">**정의 4**</ins> Graded ring $R$에 대하여, $R$-module $M$이 다음과 같은 additive group $M_n$들의 direct sum

$$M=\bigoplus_{n=0}^\infty M_n$$

으로 나타내어진다고 하자. 만일 $R_mM_n\subset M_{m+n}$이라면 이 ring을 *graded $R$-module*이라 부른다.
</div>

따라서 (당연하게도) 다음과 같이 *graded algebra* 또한 정의할 수 있다. 

<ins id="df5">**정의 5**</ins> Graded ring $R$에 대하여, $A$가 *graded $R$-algebra*라는 것은 $A$가 graded ring인 동시에 graded $R$-module이라는 것이다.
{: .definition}

많은 경우에, $R$은 다음과 같은 trivial grading

$$R=R\oplus 0\oplus 0\oplus\cdots$$

가 주어진 것으로 보기도 한다. 그럼 $R\subset A_0$이고, 각각의 $A_i$들은 $R$-module이 된다. Ring $R$의 grading이 명시되지 않았을 경우는 모두 이와 같이 trivial grading이 주어진 것으로 생각한다.

<div class="example" markdown="1">

<ins id="ex6">**예시 6**</ins> Polynomial algebra $A=R[X]$는 위에서 정의한 degree $\lvert\alpha\rvert$를 grading으로 갖는 graded $R$-algebra가 된다.  이 때, 각각의 homogeneous piece $A_d$들은 다음의 식

$$\sum_{\lvert \alpha\rvert=d} a_\alpha x^\alpha$$

을 만족하는 원소들의 모임이고, $A_d$는 따라서 degree $d$의 monomial들로 generate되는 $R$-module이다. 
</div>

많은 경우에 우리는 $X$가 singleton인 경우, 즉 $A=R[x]$인 경우에 관심을 가진다. 그리고 특히 앞으로 할 Galois theory에서 $R$은 종종 field $k$가 된다.  


<div class="proposition" markdown="1">

<ins id="pp7">**명제 7**</ins> Field $k$에 대하여, 다음이 성립한다.

1. $k[x]$의 임의의 ideal $\mathfrak{a}$에 대하여, 유일한 monic polynomial $f\in k[x]$가 존재하여 $\mathfrak{a}=(f)$이다.
2. $f_1,f_2\in k[x]$에 대하여, $(f_1)=(f_2)$는 어떠한 $r\neq 0$이 존재하여 $f_2=rf_1$인 것과 동치이다.

</div>

<details class="proof" markdown="1">
<summary>증명</summary>

Euclidean division을 사용하면 자명.

</details>

<ins id="df8">**정의 8**</ins> Field $k$에 대하여, $f,g\in k[x]$가 주어졌다고 하자. 만일 $f\in (g)$가 성립한다면, $g$가 $f$를 나눈다고 한다. 만일 $\deg f\geq 1$이고 $f$가 $0<\deg g<\deg f$를 만족하는 어떠한 $g$로도 나누어지지 않으면 $f$가 irreducible이라 한다.
{: .definition}

한편, $k[x]$는 위에서 증명했듯 principal ideal domain이므로, 다음도 성립한다. 

<div class="proposition" markdown="1">

<ins id="pp9">**명제 9**</ins> Field $k$와 $f,g\in k[x]$가 주어졌다고 하자. 임의의 $d\in k[x]$에 대하여, 다음 조건들이 모두 동치이다.

1. $d$가 $f$와 $g$를 나누며, $f,g$를 나누는 또 다른 polynomial $d'$에 대해 항상 $d$가 $d'$를 나눈다.
2. $d$가 $f$, $g$를 나누며, 어떠한 두 개의 polynomial $u$, $v$가 존재하여 $d=uf+vg$이다.
3. $(d)=(f)+(g)$가 성립한다.

</div>

이 동치조건을 만족하는 $d$를 $f$와 $g$의 greatest common divisor라고 부른다. 

## Zeros of polynomials

이제 우리는 다항식의 근들을 살펴본다. 임의의 ring $R$을 고정하자. 

<ins id="df10">**정의 10**</ins> 어떤 $R$-algebra $S$의 원소 $s$가 $f\in R[x]$의 근이라는 것은 $f(s)=0$인 것이다.
{: .definition}

정의에서, 어떤 $r\in R$ 대신 $s\in S$를 이용한 이유는, 예를 들어, $f(x)=x^2+1$은 $\mathbb{R}[x]$의 원소이지만 $\mathbb{R}$에서는 근을 갖지 않기 때문이다. 따라서 우리는 이 $R$-algebra $S$를 이용해서 $R$을 확장할 생각을 하게 된다.

그건 어쨌든 조금 먼 일이고, 우선 zero를 정의했으니 zero들의 multiplicity를 정의하는 게 당연하다. 먼저 간단한 명제 하나.

<ins id="pp11">**명제 11**</ins> $f\in R[x]$와 $\alpha\in R$에 대하여, $f$를 $x-\alpha$로 나눈 나머지는 $f(\alpha)$이다.
{: .proposition}

<details class="proof" markdown="1">
<summary>증명</summary>
유클리드 호제법에 의하여, $f(x)=(x-\alpha)g(x)+r(x)$이도록 하는 $g,r\in R[x]$가 존재하고, 이 때 $\deg r<\deg(x-\alpha)=1$이므로 $r$은 상수여야 한다. 이제 $x=\alpha$를 대입하면 $r(\alpha)=f(\alpha)$를 얻는다.
</details>

따라서, $\alpha$가 $f(x)=0$의 근이 되는 것은 $x-\alpha$가 $f\in R[x]$를 나누는 것과 동치이다.

<div class="proposition" markdown="1">

<ins id="pp12">**명제 12**</ins> $f\in R[x]$, $\alpha\in R$과 integer $d\geq 0$에 대하여, 다음이 동치이다.

1. $f$가 $(x-\alpha)^d$로는 나누어떨어지지만, $(x-\alpha)^{d+1}$로는 나누어떨어지지 않는다.
2. 어떤 $g\in R[x]$가 존재하여 $f(x)=(x-\alpha)^d g(x)$이고 $g(\alpha)\neq 0$이다.

</div>

<details class="proof" markdown="1">
<summary>증명</summary>

만일 1이 성립한다면 $f(x)=(x-\alpha)^d g(x)$라 할 수 있다. 만일 $g(\alpha)=0$이었다면, 이는 적당한 $h\in R[x]$에 대하여 $g(x)=(x-\alpha)h(x)$라는 것이므로 $f(x)$는 $(x-\alpha)^{d+1}$로도 나누어져야 하고 이는 모순이다.  
거꾸로 만일 $f(x)=(x-\alpha)^dg(x)$이고 $g(\alpha)\neq 0$이라 하자. 그럼 $f$가 $(x-\alpha)^d$로 나누어떨어지는 것은 자명하다. 만일 어떠한 $h\in R[x]$가 존재하여 $f(x)=(x-\alpha)^{d+1}h(x)$라 한다면, $(x-\alpha)^d$는 monic이므로 zero divisor가 아니고, 따라서 

$$0=f(x)-f(x)=(x-\alpha)^{d+1}h(x)-(x-\alpha)^dg(x)=(x-\alpha)^d\left((x-\alpha)h(x)-g(x)\right)$$

은 곧 $g(x)=(x-\alpha)h(x)$라는 것이다. 이는 $g(\alpha)\neq 0$이라는 원래 가정에 모순이므로 $f$는 $(x-\alpha)^{d+1}$로 나누어지지 않는다.

</details>

또한, 위의 동치관계 중 1로부터 반드시 이러한 $d$는 단 하나 존재함을 알 수 있으므로, 다음과 같이 정의한다.

<ins id="df13">**정의 13**</ins> 위의 명제에서 얻어지는 $d$를 근 $\alpha$의 *multiplicity*라 부른다.
{: .definition}

## Module of differentials
이제 근들의 multiplicity를 조금 더 깊게 살펴본다. 당연히 이를 파악하는 방법은 (고등학교 때부터 배웠듯) 미분이다. 그런데 지금 우리는 일반적인 $R[x]$에서 논리를 만들어 나가고 있으므로, 이는 완벽하게 타당한 방법은 아니다. 임의로 주어진 polynomial $f\in R[x]$에 대하여, 만일

$$f(x)=\sum_{n=0}^\infty a_nx^n$$

라면 $f$의 미분을 formal하게 다음의 식

$$f'(x)=\sum_{n=1}^\infty na_nx^{n-1}\tag{1}$$

으로 정의하고 넘어가는 방법도 있겠지만, 이미 $R$-algebra structure라는 걸 아는 상태에서 이렇게 넘어가는 건 자존심이 상한다. 따라서 대수적으로 미분 역할을 할 무언가를 만들 것이다. 자세한 내용은 algebra를 다루며 따로 정리해두었다.

아무튼 우리는 미분을 대수적으로 정의해야 하는데, 그러기 위해서는 미분이 갖는 특별한 성질을 먼저 characterize해야 한다. 우리의 조건이 되는 것은 Leibniz rule이다.

$$(fg)'=f'g+fg'.$$

<div class="definition" markdown="1">

<ins id="df14">**정의 14**</ins> Ring $R$과, $R$-module $M$에 대하여, $R$에서 $M$으로의 *derivation*은 다음의 두 조건

1. $D$는 $R$에서 $M$으로의 additive map이다 (즉, $R$, $M$의 underlying group structure들 간의 group homomorphism이다)
2. $D$는 Leibniz rule을 만족한다. 즉, $D(ab)=aD(b)+bD(a)$가 성립한다. 

을 만족하는 map $D$이다. $R$에서 $M$으로의 모든 derivation들을 모아둔 집합을 $\Der(R, M)$이라 적는다.

</div>

$\Der(R,M)$은 $\Hom(R, M)$에서 자연스럽게 물려받은 $R$-module structure를 갖는다.

한편, 임의의 derivation $D$에 대하여 $D^{-1}(0)$은 $R$의 subring이다. 만일 $a, b\in D^{-1}(0)$이라면  $D(a+b)=0$인 것은 $D$의 linearity로부터 자명하고, 또 $D(ab)=aD(b)+bD(a)=a0+b0=0$이기 때문이다. 특히, 

$$D(1)=D(1\cdot1)=1D(1)+1D(1)$$

이므로 $D(1)=0$이고 따라서 $1\in D^{-1}(0)$이 성립한다. 

방금 정의한 derivation은 상당히 불충분한데, 우리가 마음에 두고 있는 미분은 domain이 $R$이 아니라 $R[x]$이기 때문이다. 일반화가 필요하다.

지금부터 우리가 언급하는 임의의 $R$-algebra들은 $R[x]$ 등등을 마음 속에 두고 있다고 생각하면 이해가 빠르다.

<div class="definition" markdown="1">

<ins id="df15">**정의 15**</ins> $R$이 ring이고, $A$가 commutative associative unital algebra, 그리고 $M$이 $A$-module이라 하자. 그럼 $A$에서 $M$으로의 *$R$-derivation*은 다음의 세 조건

1. $D$는 $A$에서 $M$으로의 additive map이다.
2. $D$는 Leibniz rule을 만족한다. 즉, $D(ab)=aD(b)+bD(a)$가 성립한다.
3. 임의의 $r\in R$에 대하여, $D(r\cdot 1)=0$이 항상 성립한다.

을 만족하는 map $D$이다. 이러한 $R$-derivation들의 모임을 $\Der_R(A, M)$으로 쓰고, 만일 $M=A$라면 간단히 $\Der_R(A)$로 적는다. 
</div>

우선 지금까지의 construction만으로도 이 페이지에서의 내용은 충분히 커버할 수 있다. Leibniz rule에 의해, 

$$D((x-\alpha)g(x))=D(x-\alpha)g(x)+(x-\alpha)D(g(x))$$

이므로, 만일 $\alpha$를 근으로 갖는 $f(x)=(x-\alpha)g(x)$가 multiple root를 갖는다면, $g(\alpha)=0$이고, $(x-\alpha)$ 또한 $x=\alpha$에서 $0$이므로 $D((x-\alpha)g(x))$가 $\alpha$에서 $0$이 되므로, $f$의 *미분* $Df$ 또한 근 $\alpha$를 갖게 되기 때문이다. 그러나 앞으로 사용할 도구를 좀 더 마련하기 위해, 조금만 더 고생을 해 보자. 

우리는 derivation을 characterize하기 위해 Leibniz rule을 도입했고, 이를 통해 $R$-derivation이라는 걸 만들어냈다. 그럼 항상 그래왔듯 어떤 universal한 대상을 찾고싶다. 즉, 다음과 같은 universal mapping problem을 생각해보자. 

![elements]({{ site.url }}{{ site.baseurl }}/assets/images/<#name#>.png){:width="250px"  class="invert" .align-center}

> **(Universal mapping problem for derivations)**  
Commutative, associative unital $R$-algebra $A$가 주어졌을 때, 어떤 $A$-module $\Omega_R(A)$와 $R$-derivation $d$가 존재하여, 임의의 $A$-module $M$과 $R$-derivation $D:A\rightarrow M$이 주어질 때마다 $D=fd$이도록 하는 어떤 $A$-module homomorphism $f:\Omega_R(A)\rightarrow M$이 존재하도록 할 수 있는가?

당연히 이에 대한 대답은 그렇다는 것이고, $\Omega_R(A)$를 module of differentials, 혹은 module of Kähler differentials라 부른다. 우선 $\Omega_R(A)$를 만들어야 하는데, 크게 두 가지 방법이 있으며 둘 다 좋은 방법이다.

한 가지 방법은 각각의 $a\in A$마다 $da$를 하나씩 대응시켜, 이들 $\\{da:a\in A\\}$를 basis로 하여 free $A$-module을 만든 후 정의의 1번 ($d(a+b)-da-db$), 2번 ($d(ab)-adb-bda$), 3번 ($d(r\cdot 1)$) 조건들로 quotient를 시키는 것이다. 이 방법의 장점은 $\Omega_R(A)$의 generator가 explicit하게 주어진다는 것과, 또 differential 1-form들로 generate되는 space, 곧 cotangent space과의 유사성을 많이 보여준다는 것이다. 

그러나 이렇게 differential 1-form들을 생각하기 위해서는 tangent space를 먼저 정의해야 한다. 물론 미분기하 같은 곳에서는 tangent space가 조금 더 자연스러운 개념이겠지만, 대수적으로는 (특히 대수기하쪽에서는) cotangent가 훨씬 자연스러운 개념이다. 이건 보통 maximal ideal $\mathfrak{m}$에 대해 $\mathfrak{m}/\mathfrak{m}^2$과 같이 정의하는데... 

아무튼 이 두 번째 construction으로 바로 들어가보자. 우선 commutative, associative unital $R$-algebra $A$에 대해, $B=A\otimes_RA$로 두자. 그럼 $B$에서 $A$로 가는 자연스러운 map $\epsilon:B\rightarrow A$, 그리고 $A$에서 $B$로 가는 두 개의 자연스러운 map $\lambda_i:A\rightarrow B$를 다음의 식

$$\epsilon(a\otimes a')=aa',\qquad \lambda_1(a)=a\otimes 1,\qquad\lambda_2(a)=1\otimes a$$

으로 정의할 수 있다. 우선 $A$에서 $B$로 가는 map (편의상 $\lambda_1$로 고정하자)이 주어졌으므로, $B$는 자연스럽게 $A$-algebra structure를 갖는다. 즉 임의의 $a\in A$에 대해, $B$의 임의의 원소와의 scalar multiplication을 $a\cdot b=\lambda_1(a)b$으로 정의한다. 한편, $B$의 ideal $\ker\epsilon=I$라 하면, $I/I^2$이 잘 정의된다. 그런데 $I$와 $I^2$은 모두 $A$-module로 생각할 수도 있으므로, $I/I^2$ 또한 $A$-module이 된다. 이를 $\Omega_R(A)$로 적자.  
이제 $d:A\rightarrow \Omega_R(A)$를 정의해야 한다. 우선 $\epsilon\lambda_1=\epsilon\lambda_2=\id_A$이므로, $\epsilon(\lambda_2-\lambda_1):A\rightarrow A$는 zero map이고, 특히 $d^*=\lambda_2-\lambda_1$의 image가 $\ker\epsilon=I$에 포함된다. 따라서 canonical surjection $p:B\rightarrow B/I^2$에 대하여, $pd^\*$는 $A$에서 $\Omega_R(A)$로의 map이 된다. 물론 $d=pd^\*$가 derivation이 된다는 것은 보여야 한다. 이를 위해 임의의 $a,b\in A$가 주어졌다 하자. 우선 $d^\*(a)$, $d^\*(b)\in I$이므로, $d^\*(a)d^\*(b)=0\pmod I$이고, 따라서

$$\begin{aligned}
d^*(a)d^*(b)&=(1\otimes a-a\otimes 1)(1\otimes b-b\otimes 1)\\
&=1\otimes ab-b\otimes a-a\otimes b+ab\otimes1\\
&=1\otimes ab-(b\otimes a-ba\otimes 1)-(a\otimes b-ab\otimes 1)-ab\otimes 1\\
&=(1\otimes ab-ab\otimes 1)-(b\otimes 1)(1\otimes a-a\otimes 1)-(a\otimes 1)(1\otimes b-b\otimes 1)\\
&=d(ab)-b\cdot d(a)-a\cdot d(b)
\end{aligned}$$

에서 $d$가 derivation임을 알 수 있다. 

이렇게 정의된 $R$-module $\Omega_R(A)$와 $d:A\rightarrow\Omega_R(A)$는 위의 universal property를 만족한다.  

<ins id="pp16">**명제 16**</ins> Pair $(\Omega_R(A), d)$는 위의 (Universal mapping problem for derivations)의 해가 된다.
{: .proposition}

<details class="proof" markdown="1">
<summary>증명</summary>

우선 유일성을 보이자. 다음의 식

$$x\otimes y=(xy\otimes 1)(1\otimes 1)+(x\otimes 1)(1\otimes y-y\otimes 1)=\epsilon(x\otimes 1)\cdot 1+xd^*(y)$$

에서, 만일 $\sum x_i\otimes y_i\in\ker\epsilon$이라면 $\sum x\_i\otimes y\_i=\sum x\_i d^\*(y\_i)$이다. 정의에 의해 $d^*y=dy\pmod{I^2}$이 성립하므로, 임의의 $\Omega_R(A)$의 원소는 generator들 $dy$ ($y\in A$)를 갖는 $A$-module로 볼 수 있고 따라서 $D=fd$를 만족하는 $f$가 존재한다면 이는 유일하게 결정된다. 

이제 $f$의 존재성을 보여야 한다. $A$-module $M$에 trivial한 $A$-algebra structure를 주고 이 $A$-algebra에 unity를 adjoin해서 (§Basic definitions (algebra), [예시 8](/ko/math/algebras/basic_definitions#ex8)과 [예시 10](/ko/math/algebras/basic_definitions#ex10)) $\tilde{M}$을 만들자. 그럼 이제 map $\phi: B\rightarrow \tilde{M}$을 

$$\phi(x\otimes y)=(xy, xD(y)) $$

으로 정의하고, $I=\ker\epsilon$의 image를 생각하면 $xy=\epsilon(x\otimes y)=0$이므로 $\phi(I)\subset M$이게 된다. 그런데 $(0,m)(0,n)=0$이므로, $\phi(I^2)\subset M^2=0$이고 따라서 $I^2\subset\ker\phi$가 된다. 그러므로 $p:B\rightarrow B/I^2$을 canonical surjection이라 하면 어떠한 homomorphism $f:B/I^2\rightarrow\tilde{M}$이 존재하여, $\phi=fp$이다. 이 map은 $dy=1\otimes y-y\otimes 1+I^2$을 $(0,D(y))$로 보내므로, $D=fd$가 성립한다.   
</div>

지금까지 살펴본 내용에 의해 (위의 증명 혹은 첫 번째 construction에서), 만일 $R$-algebra $A$가 $(x_i)_{i\in I}$으로 generate된다면, $\Omega_R(A)$는 $(dx_i)\_{i\in I}$으로 generate되는 $A$-module이라는 것을 알 수 있다. 예를 들어 $A=R[x]$를 생각하면, $\Omega_R(A)$는 $dx$로 generate되는 $R[x]$-module이 된다. 이때 canonical한 map $d$는 derivation이므로, $d$는 덧셈을 보존하고 따라서 $d$를 묘사하기 위해서는 homogeneous polynomial만 신경쓰면 된다. 우선 임의의 $ax^n$에 대하여, 

$$d(ax^n)=d((a\cdot 1)(1\cdot x^n))=x^nd(a\cdot 1)+d(x^n)a$$

이므로 우리는 사실 monomial들에만 신경쓰면 되고, 다음의 식

$$d(x^n)=d(xx^{n-1})=x^{n-1}dx+d(x^{n-1})$$

으로부터, induction을 이용하여 $d(x^n)$의 값을 계산할 수 있다. 그런데

$$dx=1\cdot dx$$

이므로, $d(x^n)=nx^{n-1}dx$임을 알 수 있다. 그러므로 우리는 드디어 식 (1)을 얻게 되는 것이다.

<div class="proposition" markdown="1">

<ins id="pp17">**명제 17**</ins> $A=R[x]$라 하면, $\Omega_R(A)=R[x]dx$이며, canonical map $d:R[x]\rightarrow \Omega_R(A)$는 임의의 $f=\sum a_nx^n$에 대하여 다음의 식

$$d(f)=\sum_{n=1}^\infty na_nx^{n-1}dx$$

으로 주어진다.
</div>

만일 우리가 canonical하게 $\Omega_R(A)$와 $R[x]$를 identify한다면, 즉 $f(x)dx\in\Omega_R(A)$와 $f(x)\in R[x]$를 같게 취급한다면 $d$는 module $R[x]$ 위에 정의된 endomorphism으로 볼 수 있다. 따라서 앞으로 별 말 없이 $df$를 polynomial로 취급한다면, 이는 $dx$ 앞에 붙은 계수로 생각하면 된다. 이런 abuse of notation을 통하면 우리는 $d$를 몇번이고 합성할 수 있고, 이는 정확히 $f$를 여러 번 미분하는 것이 된다. 

한편, 우리가 module of differential을 정의한 이유는 polynomial의 근이 갖는 multiplicity를 정의하기 위해서였다. 

<ins id="pp18">**명제 18**</ins> $f\in R[x]$이고 $\alpha\in R$이 $f$의 근이 된다고 하자. 이 때, $\alpha$가 $f$의 simple root인 것은 $\alpha$가 $df$의 해는 아닌 것과 동치이다.
{: .proposition}

<details class="proof" markdown="1">
<summary>증명</summary>
우선 $\alpha$가 $f$의 근이므로, 적당한 $g\in R[x]$에 대하여 $f(x)=(x-\alpha)g(x)$라 할 수 있다. 이제, $\alpha$가 $x$의 simple root인 것은 $g(\alpha)\neq 0$인 것과 동치인데, $df$를 계산해보면

$$(df)(x)=d(x-\alpha)g(x)+(x-\alpha)(dg)(x)=g(x)+(x-\alpha)(dg)(x)$$

이므로, 이 상황에서 $\alpha$가 $df$의 해인 것은  $\alpha$가 $g(x)$의 해인 것과 동치이다. 따라서 주어진 정리가 성립한다.

</details>

 더 일반적으로, multiplicity $k$의 근에 대해서도 다음과 같은 명제가 성립한다.
 
 <ins id="pp19">**명제 19**</ins> $f\in R[x]$와 $\alpha\in R$에 대하여, $\alpha$가 $f$의 multiplicity $k$짜리 근이라 하자. 그럼 $\alpha$는 $df$의 multiplicity $k-1$ 이상의 근이고, 만일 $k\cdot 1\in R$ ($1$을 $R$ 안에서 $k$번 더한 것)이 cancellable이라면 등호가 성립한다.
{: .proposition}

<details class="proof" markdown="1">
<summary>증명</summary>

적당한 $g\in R[x]$에 대하여, $f(x)=(x-\alpha)^k g(x)$이고 $g(\alpha)\neq 0$이다. 따라서 

$$(df)(x)=k(x-\alpha)^{k-1}g(x)+(x-\alpha)^k (dg)(x)=(x-\alpha)^{k-1}(kg(x)+(x-\alpha)(dg)(x))$$

이므로 $df$에서 $\alpha$는 최소 multiplicity $k-1$의 근이다. 한편, 이제 $kg(x)+(x-\alpha)(dg)(x)$를 생각해보면, 이 다항식의 $x=\alpha$에서의 값은 $kg(\alpha)$이다. $g(\alpha)\neq 0$이므로, 만일 $k\cdot 1$이 cancellable하다면 $kg(\alpha)\neq 0$이다. 

</details>

나중을 위해, differential module에 대한 몇 가지 사실들을 증명하고 넘어가야 한다.

<div class="proposition" markdown="1">

<ins id="pp20">**명제 20**</ins> $A$, $L$이 $K$-algebra이고, $A_{(L)}$을 extension of scalar를 통해 얻어진 $L$-algebra $A\otimes_KL$이라 하자. 그럼

$$\Omega_K(A)\otimes_A A_{(L)}\cong \Omega_L(A_{(L)})$$

이 성립한다. 

</div>
<details class="proof" markdown="1">
<summary>증명</summary>

우선, $\Omega_K(A)\otimes_A A_{(L)}$을 간단히 살펴보면,

$$\Omega_K(A)\otimes_AA_{(L)}=\Omega_K(A)\otimes_A(A\otimes_KL)\cong\Omega_K(A)\otimes_KL$$

이 성립한다. 한편, $\Omega_L(A_{(L)})$을 살펴보기 위해 우선 $A_{(L)}\otimes_L A_{(L)}$를 살펴보면

$$A_{(L)}\otimes_L A_{(L)}=(A\otimes_KL)\otimes_L(A\otimes_KL)\cong A\otimes_K(A\otimes_KL)\cong(A\otimes_KA)\otimes_KL$$

이 성립한다. 더 concrete하게는, 위의 isomorphism은 

$$(a_1\otimes l_1)\otimes(a_2\otimes l_2)\mapsto (a_1\otimes a_2)\otimes(l_1l_2)$$

그리고 그 inverse는

$$(a_1\otimes a_2)\otimes l\mapsto (a_1\otimes l)\otimes(a_2\otimes 1)$$

으로 주어진다. 이제 $\epsilon_{(L)}:A_{(L)}\otimes_L A_{(L)}\rightarrow A_{(L)}$을 다음의 식

$$(a_1\otimes l_1)\otimes(a_2\otimes l_2)\mapsto (a_1\otimes l_1)(a_2\otimes l_2)=(a_1a_2)\otimes(l_1l_2)$$

으로 정의하면 임의의 $(a_1\otimes l_1), (a_2\otimes l_2)\in A_{(L)}\otimes_LA_{(L)}$에 대하여

$$(\epsilon\otimes\id_L)((a_1\otimes a_2)\otimes l_1l_2)=(a_1a_2)\otimes(l_1l_2)=\epsilon_{(L)}((a_1\otimes l_1)\otimes(a_2\otimes l_2))$$

이고, 또 임의의 $(a_1\otimes a_2)\otimes l\in (A\otimes_KA)\otimes_KL$에 대하여

$$\epsilon_{(L)}((a_1\otimes l)\otimes(a_2\otimes 1))=(a_1a_2)\otimes l=(\epsilon\otimes\id_L)((a_1\otimes a_2)\otimes l)$$

이 성립한다. 즉, 다음의 diagram이 commute한다.

![elements]({{ site.url }}{{ site.baseurl }}/assets/images/<#name#>.png){:width="250px"  class="invert" .align-center}

따라서 위의 isomorphism에 의하여, $\ker(\epsilon\otimes\id\_L)=I\otimes_KL$과 $I_{(L)}=\ker(\epsilon_{(L)})$을 identify할 수 있다. 

</details>

다음 두 개의 diagram은 Kähler differential의 두 개의 fundamental sequence라 불린다.

<div class="proposition" markdown="1">

<ins id="pp21">**명제 21 (The first fundamental sequence)**</ins> Field $K$와 commutative $K$-algebra $A$를 생각하자. $B$가 homomorphism $\psi:A\rightarrow B$를 통해 얻어지는 commutative $A$-algebra라면, $u:db\mapsto db$, $v:da\otimes b\mapsto bd\psi(a)$으로 정의되는 두 map $u$, $v$에 대하여 다음의 sequence

$$\Omega_K(A)\otimes_AB\overset{v}{\longrightarrow}\Omega_K(B)\overset{u}{\longrightarrow}\Omega_A(B)\longrightarrow 0$$

이 exact이다.
</div>
<details class="proof" markdown="1">
<summary>증명</summary>

우선, $\Omega_A(B)$의 임의의 원소는 $db$들의 $B$-linear combination으로 표현되므로 $u$가 surjective인 것은 자명하다. 또, $d\psi(a)=0$이므로, $uv=0$이다. 따라서 $\ker u\subset\imv$인 것만 보이면 된다. 주어진 sequence에 $\Hom_B(-, T)$를 적용하면

$$0\longrightarrow\Hom_B(\Omega_A(B),T)\longrightarrow\Hom_B(\Omega_K(B),T)\longrightarrow\Hom_B(\Omega_K(A)\otimes_A B,T)$$

를 얻는다. 그런데, 

$$\Hom_B(\Omega_K(A)\otimes_AB,T)\cong\Hom_A(\Omega_K(A),T)\cong\Der_K(A,T)$$

이고, 비슷하게 $\Hom_B(\Omega_K(B),T)\cong\Der_K(B,T)$ 그리고 $\Hom_B(\Omega_A(B), T)\cong\Der_A(B,T)$를 얻는다. 그런데 $\Der_A(B,T)\rightarrow\Der_K(B,T)$는 정의에 의해 $A$에서 vanish하고, 이는 또 정확히 $\Der_K(B,T)\rightarrow\Der_K(A,T)$의 kernel이다. 따라서 원래의 sequence가 exact가 된다.

</details>

<div class="proposition" markdown="1">

<ins id="pp22">**명제 22 (The second fundamental sequence)**</ins> Ring $K$, $K$-algebra $A$와 $A$의 ideal $\mathfrak{a}$에 대하여, 만일 $B=A/\mathfrak{a}$라면 다음 $B$-module들의 exact sequence

$$\mathfrak{a}/\mathfrak{a}^2\overset{\delta}{\longrightarrow}\Omega_K(A)\otimes_AB\overset{v}{\longrightarrow}\Omega_K(B)\longrightarrow 0$$

이 존재한다.

</div>

## Irreducibility criterions for single-variable polynomial

마지막으로


---
**References**

**[BCH]** N. Bourbaki, P.M. Cohn, and J. Howie. <i>Algebra II: Chapters 4 - 7</i>. Elements of mathematics. Springer Berlin-Heidelberg, 2013.  
**[Mat]** H. Matsumura. <i>Commutative Algebra</i>. W.A. Benjamin, 1970.

---

[^1]: 사실 이건 notation에서도 드러나는데, 이 집합을 단순히 $R$-module로만 볼 거였다면 $R[x]$와 같이 쓰지도 않았을 것이다. Module로서 $R[x]$는 $x$ 하나가 아니라, $x$, $x^2$, $\ldots$에 의해 generate되므로
