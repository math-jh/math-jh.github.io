---
title: "가역원과 영인자"
description: "환의 unit, zero divisor와 regular element를 정의하고, unit이 결코 zero divisor가 아님을 보인다. 유한가환환에서는 모든 regular element가 unit임을 곱셈사상의 단사성으로 증명하여, 유한 integral domain이 field임을 따름정리로 얻는다."
excerpt: "Unit, regular element, 그리고 유한가환환에서 regular element가 unit이 되는 현상"

categories: [Math / Ring Theory]
permalink: /ko/math/ring_theory/units_and_zero_divisors
sidebar: 
    nav: "ring_theory-ko"

date: 2026-06-20


weight: 1

---

이 글에서 우리는 ring의 곱셈 구조에서 가장 기본적인 두 부류의 원소, 즉 곱셈에 대한 역원을 갖는 *unit*과, 곱하여 $0$을 만드는 짝을 갖는 *zero divisor*를 정리한다. 이 두 개념은 이미 여러 곳에서 암묵적으로 쓰였다. Integral domain은 zero divisor가 없는 commutative ring으로 정의되었고 ([\[대수적 구조\] §분수체, ⁋정의 5](/ko/math/algebraic_structures/field_of_fractions#def5)), field는 모든 nonzero 원소가 unit인 commutative ring이었다 ([\[대수적 구조\] §분수체, ⁋정의 3](/ko/math/algebraic_structures/field_of_fractions#def3)). 여기서는 unit을 본격적으로 정의하여 그 모임이 group을 이룸을 확인하고, unit과 zero divisor가 서로 배타적임을 보인 뒤, finite ring에서는 zero divisor가 아닌 모든 원소가 자동으로 unit이 된다는 사실을 증명한다. 그 직접적 귀결로 finite integral domain이 field임을 얻는다.

별도의 언급이 없는 한 $A$는 항등원 $1\neq 0$을 갖는 ring이며, commutativity는 필요한 곳에서 그때그때 명시한다.

## 가역원

::: 정의 1
Ring $A$의 원소 $u\in A$가 *unit<sub>가역원</sub>*이라는 것은 $A$ 안에 $uv=vu=1$을 만족하는 원소 $v$가 존재하는 것이다. 이러한 $v$는 존재한다면 유일하며, 이를 $u$의 *역원<sub>inverse</sub>* $u^{-1}$이라 적는다. $A$의 unit 전체의 모임을 $A^\times$로 표기한다.
:::

역원의 유일성은 곱셈의 결합법칙에서 곧바로 따라온다. 가령 만일 $vu=1$이고 $uw=1$이면

$$v=v\cdot 1=v(uw)=(vu)w=1\cdot w=w$$

이므로 left inverse와 right inverse가 일치하고, 따라서 양쪽에서 역원을 갖는 원소의 역원은 하나뿐이다. 

뿐만 아니라, $A^\times$는 곱셈에 대해 닫혀 있다. 우선 empty product에 대해 닫혀있는 것, 즉 $1\in A^\times$임은 $1\cdot 1=1$에서 자명하고, $u,u'\in A^\times$이면

$$(uu')(u'^{-1}u^{-1})=u(u'u'^{-1})u^{-1}=uu^{-1}=1$$

이며 같은 방식으로 $(u'^{-1}u^{-1})(uu')=1$이므로 $uu'\in A^\times$이고 그 역원은 $u'^{-1}u^{-1}$이다. 또 $u\in A^\times$이면 $u^{-1}$도 $u$를 역원으로 가지므로 $u^{-1}\in A^\times$이다. 따라서 $A^\times$는 $A$의 곱셈을 연산으로 갖는 group이며, 이를 $A$의 *unit group<sub>가역원군</sub>*이라 부른다.

::: 예시 2
Ring $\mathbb{Z}$에서 $uv=1$을 만족하는 정수 $u,v$는 $u=v=1$ 또는 $u=v=-1$뿐이므로 $\mathbb{Z}^\times=\{1,-1\}$이다.

임의의 division ring $A$에서는 $0$을 제외한 모든 원소가 정의상 역원을 가지므로 $A^\times=A\setminus\{0\}$이다 ([\[대수적 구조\] §분수체, ⁋정의 3](/ko/math/algebraic_structures/field_of_fractions#def3)). 특히 field $\mathbb{K}$에 대해 $\mathbb{K}^\times=\mathbb{K}\setminus\{0\}$은 곱셈에 대한 abelian group이다.

주의할 것 중 하나는 한 ring의 unit이 그 특정 subring에서는 unit이 아닐 수 있다는 것이다. 가령 $2\in\mathbb{Q}$는 $\mathbb{Q}^\times$의 원소이지만, $\mathbb{Z}$ 안에서는 $2v=1$을 만족하는 정수 $v$가 없으므로 $2\not\in\mathbb{Z}^\times$이다. 
:::

## Zero divisor와 regular element

곱셈 구조에서, unit의 반대편 극단은 $0$이라 할 수 있다. 이를 확장하여 우리는 서로 곱하면 $0$이 되는 원소들, 즉 zero divisor들을 살펴본다. ([\[대수적 구조\] §분수체, ⁋정의 5](/ko/math/algebraic_structures/field_of_fractions#def5)) 우선 정의를 조금 더 세밀하게 다듬자. 

::: 정의 3
 Ring $A$의 원소 $a\in A$에 대하여, 다음을 정의한다. 
 
 1. $a$가 *left zero divisor<sub>왼쪽 영인자</sub>*라는 것은 적당한 nonzero 원소 $b\neq 0$이 존재하여 $ab=0$인 것이다. 
 2. 마찬가지로 적당한 $b\neq 0$에 대해 $ba=0$이면 $a$를 *right zero divisor<sub>오른쪽 영인자</sub>*라 한다. 
 3. Zero divisor가 아닌 원소를 *regular element<sub>정칙원</sub>* 혹은 non-zero-divisor라 부른다.
:::

[\[대수적 구조\] §분수체, ⁋정의 5](/ko/math/algebraic_structures/field_of_fractions#def5)는 left zero divisor와 right zero divisor를 구별하지 않고 서술한 것으로, 이들 두 개념을 모두 포함하는 것이다. 특별히 commutative ring에 대해서는 이들의 구별이 사라지므로 방향을 명시하지 않아도 혼동의 여지가 없다. 

정의에 의해, $0$ 자신은 $A\neq 0$인 한 nonzero 원소 (가령 $1$)와 곱했을 때 항상 $0$이므로 zero divisor이며, 그 대우명제를 생각하면 regular element는 항상 nonzero여야 한다. 

우리의 관심사는 regular element와 unit 사이의 관계이다. 먼저 한 방향은 일반적인 ring에서 항상 성립한다.

::: 명제 4
Ring $A$의 임의의 unit은 regular element이다.
:::
::: 증명
$u\in A^\times$이라 하고, 결론에 반하여 적당한 $b\neq 0$에 대해 $ub=0$이라 하자. 양변의 왼쪽에 $u^{-1}$을 곱하면

$$b=1\cdot b=(u^{-1}u)b=u^{-1}(ub)=u^{-1}\cdot 0=0$$

이므로 $b=0$이고, 이는 $b\neq 0$에 모순이다. 비슷한 논증이 $bu=0$이라 가정해도 성립하며 따라서 $u$는 regular element이다.
:::

위의 [명제 4](#prop4)는 임의의 unit이 regular임을 보여주지만, 일반적으로 그 역은 성립하지 않는다. 가령 $\mathbb{Z}$에서 $2$는 regular element인 것을 쉽게 확인할 수 있지만 $2$는 $\mathbb{Z}$의 unit이 아니다. ([예시 2](#ex2))

그러나 만일 ring이 *finite* ring이라면 그 역이 성립하는데, 이는 기본적으로 유한집합의 정의 ([\[집합론\] §자연수와 무한집합, ⁋정의 1](/ko/math/set_theory/natural_numbers#def1))에 의하여, 유한집합에서 자기자신으로 가는 함수는 전사이거나 단사이기만 해도 자동으로 전단사가 보장되기 때문이다. 

::: 정리 5
Finite ring $A$와 임의의 원소 $a$에 대하여, $a$가 regular element인 것과 unit인 것이 동치이다.
:::
::: 증명
[명제 4](#prop4)에 의해 unit은 항상 regular element이므로, regular element가 unit임만 보이면 된다. $a\in A$를 regular element라 하고, 곱셈사상

$$\lambda_a:A\rightarrow A;\qquad x\mapsto ax$$

를 생각하자. 그럼 $\lambda_a(x)=\lambda_a(y)$이면 $a(x-y)=0$인데, $a$가 regular element이므로 $x-y=0$, 즉 $x=y$이다. 따라서 $\lambda_a$는 단사이다. 그런데 $A$는 유한집합이고, 유한집합에서 자기 자신으로 가는 단사함수는 전사이므로 $\lambda_a$는 전사이다. 따라서 $\lambda_a(v)=1$을 만족하는 $v\in A$가 존재하고, 이는 $av=1$을 뜻한다. 비슷한 방식으로 우리는 right multiplication map이 전사임을 이용하여 $a$의 left inverse를 구성해줄 수 있으며, 앞서 [정의 1](#def1) 직후의 논증에서 이렇게 만든 두 inverse가 서로 반드시 일치해야 하는 것을 안다. 
:::

그럼 이 정리의 가장 중요한 귀결은 integral domain에 관한 것이다.

::: 따름정리 6
모든 finite integral domain은 field이다.
:::
::: 증명
정의상 임의의 finite integral domain $A$는 commutative이고 $0\neq 1$이다. ([\[대수적 구조\] §분수체, ⁋정의 5](/ko/math/algebraic_structures/field_of_fractions#def5)) 이제 추가로 $A$가 field임을 보이려면 모든 nonzero 원소가 unit임을 보이면 되는데, integral domain에는 $0$ 이외의 zero divisor가 없으므로 임의의 nonzero 원소 $a$는 regular element이고 따라서 [정리 5](#thm5)에 의해 $a$는 unit이다. 
:::

## 예시

이제 위 결과들에 대한 예시를 살펴보자. 

::: 예시 7
$n\geq 1$에 대해 정의된 ring $\mathbb{Z}/n\mathbb{Z}$를 보자. 이 ring의 원소 $a+n\mathbb{Z}$가 unit이라는 것은 어떠한 $x+n\mathbb{Z}$가 존재하여 

$$(a+n\mathbb{Z})(x+n\mathbb{Z})=1+n\mathbb{Z}$$

인 것, 즉 적당한 정수 $x,k$에 대해 $ax-kn=1$이 성립하는 것이다. [\[정수론\] §유클리드 호제법과 Bézout 항등식, ⁋명제 5](/ko/math/number_theory/euclidean_algorithm#prop5)에 의해 이러한 $x,k$가 존재하는 것은 $\gcd(a,n)=1$, 즉 $a$가 $n$과 서로소인 것과 동치이므로,

$$(\mathbb{Z}/n\mathbb{Z})^\times=\{a+n\mathbb{Z}\mid\gcd(a,n)=1\}$$

이고, 이 group의 크기는 $n$과 서로소인 $1$ 이상 $n$ 이하 정수의 개수 $\varphi(n)$이다 ([\[정수론\] §오일러 정리와 phi 함수, ⁋정의 1](/ko/math/number_theory/euler_theorem#def1)).

반면 $\gcd(a,n)=d>1$이고 $a+n\mathbb{Z}\neq 0+n\mathbb{Z}$이면 $a+n\mathbb{Z}$는 zero divisor이다. 이는 $n/d+n\mathbb{Z}\neq 0+n\mathbb{Z}$이고,

$$(a+n\mathbb{Z})(n/d+n\mathbb{Z})=a\cdot(n/d)+n\mathbb{Z}=(a/d)n+n\mathbb{Z}=0+n\mathbb{Z}$$

이기 때문이다. 따라서 $\mathbb{Z}/n\mathbb{Z}$의 모든 nonzero 원소는 unit이거나 zero divisor이며, 이 분류가 다시 [정리 5](#thm5)를 잘 보여준다. 

특히 $n=p$가 소수이면 $1,\ldots,p-1$이 모두 $p$와 서로소이므로 $(\mathbb{Z}/p\mathbb{Z})^\times=\mathbb{Z}/p\mathbb{Z}\setminus\{0+p\mathbb{Z}\}$이고, $\mathbb{Z}/p\mathbb{Z}$는 $0$ 이외의 zero divisor를 갖지 않는 finite integral domain이다. [따름정리 6](#cor6)에 의해 이는 field이며, 이것이 $p$개의 원소를 갖는 *prime field<sub>소체</sub>* $\mathbb{F}_p$이다 ([\[체론\] §체, §§소체](/ko/math/field_theory/fields#소체)).
:::

한편, product ring의 unit group은 성분별로 결정된다. 이는 product ring에서 곱셈이 성분별로 계산되기 때문이다.

::: 명제 8
Ring들 $A_1,\ldots,A_n$의 product $A=A_1\times\cdots\times A_n$에 대하여, 원소 $(a_1,\ldots,a_n)$이 $A$의 unit인 것과 각 $a_i$가 $A_i$의 unit인 것이 동치이다. 즉, group으로서

$$A^\times=A_1^\times\times\cdots\times A_n^\times$$

이 성립한다.
:::
::: 증명
$A$의 곱셈은 성분별로 이루어지고 항등원은 $(1,\ldots,1)$이다. 원소 $a=(a_1,\ldots,a_n)$이 unit이면 $ab=ba=(1,\ldots,1)$을 만족하는 $b=(b_1,\ldots,b_n)$이 존재하는데, 이는 각 성분에서 $a_ib_i=b_ia_i=1$임을 뜻하므로 각 $a_i$가 unit이고 $b_i=a_i^{-1}$이다. 

거꾸로 각 $a_i$가 unit이면 $b=(a_1^{-1},\ldots,a_n^{-1})$이 $ab=ba=(1,\ldots,1)$을 만족하므로 $a$가 unit이다. 따라서 $a\in A^\times$인 것과 각 $a_i\in A_i^\times$인 것이 동치이며, morphism

$$A^\times\rightarrow A_1^\times\times\cdots\times A_n^\times;\quad (a_1,\ldots,a_n)\mapsto(a_1,\ldots,a_n)$$

은 위의 동치에 의해 잘 정의된 전단사이고, 곱셈이 성분별이므로 group homomorphism이 되어 isomorphism을 정의한다.
:::

한편 matrix ring의 경우 unit group은 general linear group이 된다.

::: 예시 9
Ring $R$의 원소를 각 성분으로 갖는 $n\times n$ 행렬들의 ring $\Mat_n(R)$을 생각하자. 정의상 $\Mat_n(R)$의 unit은 곱셈에 대한 양쪽 역원을 갖는 행렬, 즉 invertible matrix이다. 이러한 행렬 전체의 모임을 *general linear group<sub>일반선형군</sub>*이라 부르고 $\GL(n;R)$으로 쓴다. 즉

$$\Mat_n(R)^\times=\GL(n;R)$$

이다 ([\[다중선형대수학\] §기저변환, ⁋정의 3](/ko/math/multilinear_algebra/change_of_basis#def3)). $R$가 commutative ring이면 행렬 $M\in \Mat_n(R)$이 invertible인 것과 그 행렬식 $\det M$이 $R^\times$의 원소인 것이 동치라는 것이 알려져 있다. ([\[다중선형대수학\] §행렬식, ⁋따름정리 3](/ko/math/multilinear_algebra/determinants#cor3)) 즉 이 경우

$$\GL(n;R)=\{M\in \Mat_n(R)\mid\det M\in R^\times\}$$

이다. 예를 들어 $R=\mathbb{Z}$이면 $\mathbb{Z}^\times=\{1,-1\}$이므로 $\GL(n;\mathbb{Z})$는 행렬식이 $\pm 1$인 정수행렬들로 이루어진다.

$\Mat_n(R)$은 $n\geq 2$이면 nontrivial zero divisor를 가지므로 unit과 zero divisor의 구별이 의미를 갖는다. 가령 $n=2$에서 matrix unit 

$$E_{11}=\begin{pmatrix}1&0\\0&0\end{pmatrix},\qquad E_{12}=\begin{pmatrix}0&1\\0&0\end{pmatrix}$$

는 $E_{12}E_{11}=0$이지만 $E_{12}\neq 0$, $E_{11}\neq 0$이므로 둘 다 zero divisor이고, 따라서 [명제 4](#prop4)에 의해 invertible하지 않다.
:::

---

**참고문헌**

**[AM]** M. F. Atiyah and I. G. Macdonald, *Introduction to commutative algebra*, Addison–Wesley, 1969.  
**[DF]** D. S. Dummit and R. M. Foote, *Abstract algebra*, 3rd ed., Wiley, 2004.  
**[Lam]** T. Y. Lam, *A first course in noncommutative rings*, 2nd ed., Graduate Texts in Mathematics 131, Springer, 2001.
