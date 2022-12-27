---

title: "Algebraic extension"
excerpt: "Algebraic field extensions and algebraic closure of field"

categories: [Math / Galois Theory]
permalink: /ko/math/galois_theory/algebraic_extension
header:
    overlay_image: /assets/images/Galois_theory/Algebraic_extension.png
    overlay_filter: 0.5
sidebar: 
    nav: "algebraic_structures"

date: 2021-08-29
last_modified_at:
weight: 3

published: false

---
<div class="notice--warning" markdown="1">

이 글은 현재 수정중입니다.

이 글은 예전에 쓴 글로, 서술 방향이 마음에 들지 않거나 표기법이 마음에 들지 않아 전체적으로 수정이 진행중입니다. 읽으실 때 참고해주세요.

</div>

이제 드디어 algebraic extension을 정의한다. Galois extension은 보통 normal, separable extension으로 정의되므로 algebraic extension의 정의가 반드시 필요한 것은 아니지만, 거의 대부분의 경우 우리는 algebraic한 Galois extension에 관심을 가지므로 이를 먼저 소개한다. 

## Algebraic extensions

$K$의 extension field $E$에 대하여, $E$가 $K$에 대해 algebraic하다는 것은 $E$의 모든 원소가 $K$에 대하여 algebraic하다는 것이다. 따라서, algebraic extension을 정의하기 위해서는 어떤 원소 $\alpha\in E$가 $K$에 대해 algebraic하다는 것이 무엇인지를 먼저 정의해야 한다. 

<div class="definition" markdown="1">

<ins id="df1">**정의 1**</ins>  $K$-algebra $A$에 대하여, $A$의 원소 $\alpha$가 $K$에 대해 *algebraic*이라는 것은 어떤 nonzero polynomial $f\in K[X]$가 존재하여, $f(\alpha)=0$인 것이다. 그렇지 않다면, $\alpha$가 $K$에 대해 *transcendental*이라 한다.  

</div>

$\alpha\in A$가 algebraic element라 하자. 그럼 적어도 하나의 $f\in K[X]$가 존재하여 $f(\alpha)=0$이다. 이제 자연수의 well-orderedness에 의하여, $g(\alpha)=0$을 만족하는 다항식들 중 가장 차수가 작은 다항식이 존재한다. 이를 

$$f(X)=a_dX^d+\cdots+a_1X+a_0$$

이라 하자. 그럼 $a_d\neq 0$이고 $K$는 field이므로, $a_d^{-1}$이 존재하고 따라서

$$\bar{f}(X)=X^d+\cdots+\frac{a_1}{a_d}X+\frac{a_0}{a_d}$$

이라 정의하면, $\bar{f}$ 또한 $\bar{f}(\alpha)=0$을 만족하는 것을 쉽게 확인할 수 있다. 이렇게, $f(\alpha)=0$을 만족하는 다항식 $f(X)$들 가운데 최소 차수를 갖는 monic polynomial을 $\alpha$의 *minimal polynomial*이라 부른다. 

그럼 다음이 성립한다.

<div class="proposition" markdown="1">

<ins id="pp2">**명제 2**</ins> $K$-algebra $A$와, $K$에 대하여 algebraic한 원소 $\alpha\in A$를 생각하자. 그럼 $\alpha$의 minimal polynomial $f$와, $n=\deg f$에 대해 다음이 성립한다.

1. 임의의 다항식 $g\in K[X]$에 대하여, $g(\alpha)=0$인 것은 $g$가 $f$의 배수인 것과 동치이다.
2. $K[X]/(f)\cong K[\alpha]$가 성립하며, 특히 $K[\alpha]$는 basis $1$, $\alpha$, $\cdots$, $\alpha^{n-1}$을 갖는다.
3. 만일 $A$가 integral domain이라면, $K[\alpha]$는 역시 field이고, $f$는 $f(\alpha)=0$을 만족하는 유일한 monic irreducible polynomial이다.
4. $\alpha$가 invertible한 것은 $f(0)\neq 0$인 것과 동치이며, 이 경우 $\alpha^{-1}\in K[\alpha]$가 성립한다. 

</div>
<details class="proof" markdown="1">
<summary>증명</summary>

증명할 것이 많다보니 길긴 하지만, 하나하나가 어렵지는 않다.

1. 우선, $K[X]$는 $x$에 의해 generate되는 $K$-algebra이므로, $K[X]$를 domain으로 갖는 $K$-algebra homomorphism은 $X$의 값에 의해 유일하게 결정된다. $X\mapsto\alpha$인 $K$-algebra homomorphism을 $\varphi$라 하면, 임의의 polynomial $p\in K[X]$에 대하여 $\varphi(p)=p(\alpha)$가 되므로, $\varphi$의 image는 $K[\alpha]$와 동일하다. 이제 $\ker\varphi=\mathfrak{a}$라 하자. 정의에 의해, $f\in\mathfrak{a}$이고 $f$는 $\mathfrak{a}$의 원소들 중 가장 작은 degree를 갖는 monic polynomial이다. 이제 $K[X]$는 PID이므로 $\mathfrak{a}=(f)$가 성립하고, 따라서 임의의 $g\in K[X]$에 대하여, $g(\alpha)=0$은 $g\in\ker\varphi=\mathfrak{a}=(f)$와 동치이므로, $g$가 $f$로 나누어 떨어지는 것과 동치이다.
2. 따라서, 1st isomorphism theorem에 의해 $K[X]/(f)\cong K[\alpha]$이며, $K[X]/(f)$의 basis들의 image $1$, $\alpha$, $\ldots$, $\alpha^{n-1}$이 $K[\alpha]$의 basis가 된다. 
3. 만일 $A$가 integral domain이었다면, $A$의 부분집합 $K[\alpha]$ 또한 integral domain이며, 이는 2에 의해 finite degree를 가지므로 field가 된다. 그러므로 $(f)$는 $K[x]$의 maximal ideal이고, 따라서 $f$가 irreducible이 된다. $f$의 유일성은 1로부터 보장된다.
4. 우선, $f(x)$를 $f(x)=xg(x)+f(0)$이라 쓸 수 있다. 만일 $f(0)=0$이라면 $f(x)=xg(x)$이고, 따라서 $0=f(\alpha)=\alpha g(\alpha)$이므로 $\alpha$는 invertible하지 않다. 반대로 만일 $f(0)\neq 0$이라면, $f(0)^{-1}$이 존재하고, 이 때 $\alpha(-f(0)^{-1}g(\alpha))=1$이 성립한다. 따라서 $\alpha$는 $A$에서 invertible하고, $\alpha^{-1}=-(f(0)^{-1}) g(\alpha)\in K[\alpha]$가 성립한다. 

</details>

<div class="remark" markdown="1">

<ins id="rmk1">**참고**</ins> 위 명제에 의해, 임의의 $\alpha\in A$가 algebraic이라면 $K[\alpha]$의 extension degree가 유한하다.  
거꾸로, 만일 임의의 $K$-algebra $A$가 finite degree라면, $A$의 임의의 원소는 algebraic이다. 임의의 $\alpha\in A$가 주어졌다고 하자. 그럼 $A$가 finite degree이므로, 원소 $1$, $\alpha$, $\ldots$는 언젠가 linearly dependent할 수밖에 없고, 따라서 모두 0은 아닌 $K$의 원소들 $a_0$, $\ldots$, $a_d$에 대하여

$$a_d\alpha^d+a_{d-1}\alpha^{d-1}+\cdots+a_1\alpha+a_0=0$$

이 되어야 한다. 이제, 다항식 $f\in K[X]$를 

$$f(X)=a_dX^d+\cdots+a_1X+a_0$$

으로 정의하면, 앞선 식은 정확히 $f(\alpha)=0$이라는 것이고 따라서 $\alpha$는 algebraic이다. 
</div>

맨 처음에 말했듯, algebraic extension은 다음과 같이 정의된다. 

<div class="definition" markdown="1">

<ins id="df3">**정의 3**</ins> $K$의 extension $E$가 *algebraic extension*이라는 것은 $E$의 모든 원소가 $K$에 대해 algebraic인 것이다. 그렇지 않다면 $E$가 *transcendental extension*이라 부른다.

</div>

이제 algebraic extension의 몇 가지 성질을 살펴보자. 

<div class="proposition" markdown="1">

<ins id="pp4">**명제 4**</ins> $K$의 extension $E$가 algebraic인 것은, $E$의 임의의 sub-$K$-algebra $A$가 field인 것과 동치이다.

</div>
<details class="proof" markdown="1">
<summary>증명</summary>

우선 $E$가 algebraic이라 가정하고, $E$의 임의의 sub-$K$-algebra $A$가 주어졌다 하자. 임의의 nonzero element $\alpha\in A$에 대하여, $\alpha$는 algebraic이므로 [명제 2](#pp2)에 의하여 $\alpha^{-1}\in K[\alpha]\subset A$가 성립한다. $A$의 임의의 nonzero element가 invertible하므로, $A$는 field이다.  
거꾸로, $E$의 임의의 sub-$K$-algebra가 field라 하자. $E$의 임의의 nonzero element $\alpha\in E$에 대하여, $K[\alpha]$는 $E$의 sub-$K$-algebra이고, 따라서 가정에 의해 field이므로 $K[\alpha]$에서 $\alpha$는 invertible하다. 즉, 어떤 적당한 polynomial $p\in K[X]$에 대하여, $\alpha^{-1}=g(\alpha)$이므로, $f(X)=Xg(X)-1$이라 하면 $f(\alpha)=0$이고, 따라서 $\alpha$는 $E$에 대해 algebraic한 원소다. 따라서 $E$는 algebraic extension이 된다.  

</details>

앞선 [참고](#rmk1)에서, 우리는 finite degree를 갖는 $K$의 extension은 항상 algebraic extension이 됨을 보였다. 이 과정에서 중요하게 등장한 intermediate field는 $K[\alpha]=K(\alpha)$인데, 기본적인 extension degree의 성질에 의해 ([§Field extensions, 명제 13](/ko/math/galois_theory/field_extensions#pp13)) 

$$[E:K(\alpha)][K(\alpha):K]=[E:K]\tag{1}$$

이 성립하므로, $K(\alpha)$의 extension degree는 항상 $E$의 extension degree를 나눈다. 일반적으로 위의 식은 양변 중 하나가 무한대라면 효용가치가 많이 떨어지는데, 실제로 임의의 field $K$에 대하여 $K$의 algebraic extension field $E$가 항상 finite degree를 가질 필요는 없다. 즉, 우변이 무한대가 될 가능성이 충분히 존재한다. 그럼에도 불구하고, algebraic한 원소 *하나*를 추가하여 만든 extension은, 앞선 [명제 2](#pp2)에 의해, 항상 유한한 degree를 갖는다. 더 일반적으로, 다음이 성립한다.

<div class="proposition" markdown="1">

<ins id="pp5">**명제 5**</ins> $E$가 $K$의 finitely generated field extension이라 하고, $E$의 generator들을 $a\_1,\ldots, a\_m$이라 하자. 만일 이들 generator들이 모두 algebraic하고, 따라서 $K(a\_1,\ldots,a\_{i-1})$에 대해 원소 $a\_i$가 degree $n\_i$를 갖는다면 전체 degree 

$$[K(a_1,\ldots, a_m):K]=n_1n_2\cdots n_m$$

이고, 이 때 $n_1n_2\cdots n_m$개의 basis는 $\\{a\_1^{d\_1}a\_2^{d\_2}\cdots a\_m^{d\_m}\\}$들로 주어진다.

</div>

아무튼, 위의 식 (1)이 무한대가 되느냐, 유한하게 bound되느냐와는 별개로, 다음이 성립한다.  

<div class="proposition" markdown="1">

<ins id="pp6">**명제 6**</ins> $E$, $F$가 $K\subset E\subset F$를 만족하는 extension field들이라면, $E$가 $K$에 대해 algebraic한 것은 $E$가 $K$에 대해 algebraic하고, $F$가 $E$에 대해 algebraic한 것과 동치이다.

</div>

<details class="proof" markdown="1">
<summary>증명</summary>

만일 $F$가 $K$에 대해 algebraic하다면, 임의의 $\alpha\in F$의 minimal polynomial $f\in K[X]$는 $E[X]$의 원소이기도 하므로 $\alpha$는 $E$에 대해 algebraic하고, 따라서 $F$는 $E$에 대해 algebraic하다. 한편, $E$의 모든 원소는 $F$의 원소이고, 따라서 $K$에 대해 algebraic하므로 정의에 의해 $E$는 $K$에 대해 algebraic하다.

따라서 반대방향만 보이면 충분하다. $F$의 임의의 원소 $\alpha\in F$를 고정하자. 그럼 가정에 의해, 적당한 $g\in E[X]$가 존재하여 $g(\alpha)=0$이다. 그런데, $g$의 각 coefficient $(a_n)$들은 $E$의 원소들이므로, 가정에 의해 $K$에 대해서는 algebraic한 원소들이다. 따라서, 이들을 모두 $K$에 adjoin하여 얻어지는 field extension $L=K(a_0,\ldots, a_d)$은 finite degree를 가지므로 algebraic이다. 그럼 $g\in L[X]$이고, 따라서 $\alpha$는 $L$에 대해 algebraic이므로 $L[\alpha]$도 $L$에 대해 finite degree를 가지게 되어, 최종적으로 $L[\alpha]=L(\alpha)$도 $K$에 대해 finite degree를 가진다. 즉, $K(a_0,\ldots, a_d,\alpha)$가 finite extension이므로, 이 extension의 원소 $\alpha$는 $K$에 대해 algebraic하게 된다.  

</details>

## Algebraically closed field and splitting extensions

Algebraic extension을 정의했으니, 이제 algebraic closure를 정의할 수 있고, 그 전에 algebraically closed field를 정의할 수 있다. 대표적인 예시는 $\mathbb{C}$가 있는데, $\mathbb{C}$가 algebraically closed라는 말은

> 임의의 복소수 계수 다항식 $f(X)=a_nX^n+\cdots+a_1X+a_0$은 항상 $n$개의 근을 갖는다.

와 같은 말이다. 물론 아직은 이걸 증명할 도구가 없지만 (사실 가장 간단한 방법은 복소해석학에서 Liouville's theorem의 따름정리로 얻는 방법이다) 열심히 field extension을 공부하다보면 이를 위한 도구가 생기게 된다. 

<div class="proposition" markdown="1">

<ins id="pp7">**명제 7**</ins> Field $K$에 대하여, 다음이 모두 동치이다.

1. 상수가 아닌 $K[X]$의 임의의 원소가 일차식들의 곱으로 인수분해된다.
2. 상수가 아닌 $K[X]$의 임의의 원소가 적어도 하나의 근을 가진다.
3. $K[X]$의 irreducible polynomial은 반드시 degree 1이다.
4. $K$의 임의의 algebraic extension이 degree 1이다.

</div>
<details class="proof" markdown="1">
<summary>증명</summary>

우선, 만일 1이 성립한다면 3은 자명하다. 또, $K[X]$는 UFD이므로 모든 다항식은 irreducible polynomial들의 곱으로 나타낼 수 있는데, 3을 가정한다면 모든 다항식은 1차항들의 곱으로 인수분해 되어야 하므로 거꾸로 1번도 성립한다.

한편, 만일 1이 성립한다면, 임의로 주어진 $f(X)$에 대하여, 이를 나누는 일차항 $ax+b$가 존재하고, 그럼 $-b/a$가 $f(X)=0$의 해가 되므로 2번이 성립한다. 거꾸로 만일 2번이 성립한다면, [§Polynomials, 명제 11](/ko/math/galois_theory/polynomials#pp11)에 의하여 임의의 $f\in K[X]$가 주어졌을 때, $f$를 나누는 일차식 $X-\alpha$가 존재한다. 이제 degree에 대한 induction을 사용하면 1번을 얻는다.

마지막으로, 3번과 4번이 동치라는 것을 보이자. 우선 3번을 가정하고, $K$의 임의의 algebraic extension field $L$과, $L$의 임의의 원소 $\alpha\in L$에 대하여 $\alpha$의 minimal polynomial $f(X)$를 생각하자. $K[X]$는 integral domain이므로, $f$는 irreducible이고, 따라서 degree가 1이어야 한다. 이 말은 $K[\alpha]=K$라는 것과 같으므로, 4번이 성립한다. 거꾸로, 임의의 irreducible polynomial $f$에 대하여, $K[X]/(f)$는 degree $n$짜리 extension이 되므로 $K$에 대한 algebraic extension이고, 따라서 만일 4번이 성립한다면 이 extension이 degree 1이므로 $n=1$이어야 한다.

</details>

따라서, 이들 조건을 만족하는 field를 다음과 같이 이름붙일 수 있다.

<div class="definition" markdown="1">

<ins id="df8">**정의 8**</ins> Field $K$가 위의 동치조건을 만족한다면, $K$가 *algebraically closed*라 부른다.

</div>

[§Field extensions, 명제 16](/ko/math/galois_theory/field_extensions#pp16)를 임의의 $K$-homomorphism을 얻는 데에 쓸 수 있으므로, inclusion $K\hookrightarrow\Omega$와 $K$의 algebraic extension $E$에 해당 명제를 적용하면 우리는 $\Omega$의 extension $\Omega'$에 대해, $K\hookrightarrow\Omega$를 $E\rightarrow \Omega'$로 확장할 수 있다. 그런데, $E$가 algebraic extension이므로 임의의 $x\in E$는 $K$에 대해 algebraic하고, 따라서 $u(x)$ 또한 $u(K)$에서 algebraic하다. $\Omega$는 $K$의 algebraically closed extension이므로, $x$는 $\Omega$에 대해서도 algebraic이고, $u(x)\in\Omega$이므로 이번엔 $E$가 $\Omega$의 extension으로 갈 필요 없이 $\Omega$로 들어간다.

방금 전의 argument와 같이, $K$의 algebraically closed extension은 중요하다. 그런데 앞선 동치조건들에 의해, 이러한 extension을 찾기 위해 우리는 주어진 polynomial $f\in K[X]$에 대해, $f$가 일차식들로 인수분해되는 extension을 먼저 생각하는 것이 자연스러울 것이다. 이렇게 어떤 다항식이 일차식들로 쪼개지는 (split) extension을 splitting extension이라 하고, 더 일반적으로 다음을 정의한다.

<div class="definition" markdown="1">

<ins id="df9">**정의 9**</ins> Field $K$와 $K[X]$의 non-constant polynomial들의 family $(f_i)_{i\in I}$에 대하여, $(f_i)\_{i\in I}$의 *splitting extension*은 다음의 두 조건

- 임의의 $i\in I$에 대하여, $f_i$는 $E[X]$에서 일차식들의 곱으로 나타난다.
- $R_i$가 $f_i$의 $E$에서의 근들이라면, $E=K(\bigcup R_i)$가 성립한다.

을 만족하는 $K$의 extension $E$이다.

</div>

우리는 splitting field가 존재함을 증명해야겠지만, 이건 polynomial algebra에 대해 더 잘 이해하고 있어야 쉽게 증명할 수 있으니 fact로 받아들인다. 그 대신 짚고 넘어갈만한 것은 두 번째 조건이 splitting field에 일종의 minimality를 부여하므로, splitting field는 유일하다는 것이다. 이걸 받아들인다면 $K$의 *algebraic closure*가 (유일하게) 존재하는 것도 자명하다.

<div class="definition" markdown="1">

<ins id="df10">**정의 10**</ins> Field $K$에 대하여, $K$의 algebraic extension 중 그 자체로 algebraically closed field인 것을 $K$의 *algebraic closure*라 부른다.

</div>

왜냐하면, $(f_i)_{i\in I}$를 $K[X]$ 전체에 대해 돌려버리면 되기 때문이다. 



---
**Reference**

- [BCH13] N. Bourbaki, P.M. Cohn, and J. Howie. <i>Algebra II: Chapters 4 - 7</i>. Elements of mathematics. Springer Berlin-Heidelberg, 2013. 

---
