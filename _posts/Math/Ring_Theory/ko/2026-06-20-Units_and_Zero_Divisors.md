---
title: "Unit과 zero divisor"
description: "환의 unit과 그 모임 R^×, zero divisor와 regular element를 정의하고, unit이 결코 zero divisor가 아님을 보인다. 유한가환환에서는 모든 regular element가 unit임을 곱셈사상의 단사성으로 증명하여, 유한 integral domain이 field임을 따름정리로 얻는다."
excerpt: "Unit의 모임 R^×, regular element, 그리고 유한가환환에서 regular element가 unit이 되는 현상"

categories: [Math / Ring Theory]
permalink: /ko/math/ring_theory/units_and_zero_divisors
sidebar: 
    nav: "ring_theory-ko"

date: 2026-06-20

weight: 1.5

published: false

---

이 글에서 우리는 환의 곱셈 구조에서 가장 기본적인 두 부류의 원소, 즉 곱셈에 대한 역원을 갖는 *unit*과, 곱하여 $$0$$을 만드는 짝을 갖는 *zero divisor*를 정리한다. 이 두 개념은 이미 여러 곳에서 암묵적으로 쓰였다. Integral domain은 zero divisor가 없는 가환환으로 정의되었고 ([\[대수적 구조\] §분수체, ⁋정의 5](/ko/math/algebraic_structures/field_of_fractions#def5)), field는 모든 nonzero 원소가 unit인 division ring이었다 ([\[대수적 구조\] §분수체, ⁋정의 3](/ko/math/algebraic_structures/field_of_fractions#def3)). 여기서는 unit을 본격적으로 정의하여 그 모임이 군을 이룸을 확인하고, unit과 zero divisor가 서로 배타적임을 보인 뒤, 유한가환환에서는 zero divisor가 아닌 모든 원소가 자동으로 unit이 된다는 사실을 증명한다. 그 직접적 귀결로 유한 integral domain이 field임을 얻는다.

별도의 언급이 없는 한 $$A$$는 항등원 $$1\neq 0$$을 갖는 환이며, commutativity는 필요한 곳에서 그때그때 명시한다.

## Unit

<div class="definition" markdown="1">

<ins id="def1">**정의 1**</ins> 환 $$A$$의 원소 $$u\in A$$가 *unit<sub>가역원</sub>*이라는 것은 $$A$$ 안에 $$uv=vu=1$$을 만족하는 원소 $$v$$가 존재하는 것이다. 이러한 $$v$$는 존재한다면 유일하며, 이를 $$u$$의 *역원<sub>inverse</sub>* $$u^{-1}$$이라 적는다. $$A$$의 unit 전체의 모임을 $$A^\times$$로 표기한다.

</div>

역원의 유일성은 곱셈의 결합법칙에서 곧바로 따라온다. 만일 $$vu=1$$이고 $$uw=1$$이면

$$v=v\cdot 1=v(uw)=(vu)w=1\cdot w=w$$

이므로 좌역원과 우역원이 일치하고, 따라서 양쪽 역원을 갖는 원소의 역원은 하나뿐이다. 이제 $$A^\times$$가 곱셈에 대해 닫혀 있음을 확인하자. $$1\in A^\times$$임은 $$1\cdot 1=1$$에서 자명하고, $$u,u'\in A^\times$$이면

$$(uu')(u'^{-1}u^{-1})=u(u'u'^{-1})u^{-1}=uu^{-1}=1$$

이며 같은 방식으로 $$(u'^{-1}u^{-1})(uu')=1$$이므로 $$uu'\in A^\times$$이고 그 역원은 $$u'^{-1}u^{-1}$$이다. 또 $$u\in A^\times$$이면 $$u^{-1}$$도 $$u$$를 역원으로 가지므로 $$u^{-1}\in A^\times$$이다. 따라서 $$A^\times$$는 $$A$$의 곱셈을 연산으로 갖는 군이며, 이를 $$A$$의 *unit group<sub>가역원군</sub>* 혹은 group of units라 부른다.

<div class="example" markdown="1">

<ins id="ex2">**예시 2**</ins> 정수환 $$\mathbb{Z}$$에서 $$uv=1$$을 만족하는 정수 $$u,v$$는 $$u=v=1$$ 또는 $$u=v=-1$$뿐이므로 $$\mathbb{Z}^\times=\{1,-1\}$$이다.

Division ring $$A$$에서는 $$0$$을 제외한 모든 원소가 정의상 역원을 가지므로 $$A^\times=A\setminus\{0\}$$이다 ([\[대수적 구조\] §분수체, ⁋정의 3](/ko/math/algebraic_structures/field_of_fractions#def3)). 특히 field $$\mathbb{K}$$에 대해 $$\mathbb{K}^\times=\mathbb{K}\setminus\{0\}$$은 곱셈에 대한 가환군이다.

한 환의 unit이 다른 부분환에서는 unit이 아닐 수 있다. 가령 $$2\in\mathbb{Q}$$는 $$\mathbb{Q}^\times$$의 원소이지만, $$\mathbb{Z}$$ 안에서는 $$2v=1$$을 만족하는 정수 $$v$$가 없으므로 $$2\notin\mathbb{Z}^\times$$이다. 즉 unit인지의 여부는 어느 환 안에서 보는지에 달려 있다.

</div>

Unit의 개념은 앞선 글들에서 이미 쓰였다. Integral domain에서 두 원소가 같은 principal ideal을 생성하는 것이 unit배만큼 차이나는 것과 동치라는 사실 ([§정역, ⁋명제 6](/ko/math/ring_theory/integral_domains#prop6))과, irreducible · prime · associate의 정의 ([§정역, ⁋정의 11](/ko/math/ring_theory/integral_domains#def11))가 모두 unit에 기대고 있다. 정의 1은 이 용어를 명시적으로 고정한 것이다.

## Zero divisor와 regular element

이제 곱셈 구조의 반대편 극단, 즉 곱하여 $$0$$을 만드는 원소들을 본다. Zero divisor와 integral domain은 이미 정의되었다.

<div class="definition" markdown="1">

<ins id="def3">**정의 3**</ins> ([\[대수적 구조\] §분수체, ⁋정의 5](/ko/math/algebraic_structures/field_of_fractions#def5)) 환 $$A$$의 원소 $$a\in A$$가 *left zero divisor<sub>왼쪽 영인자</sub>*라는 것은 적당한 nonzero 원소 $$b\neq 0$$이 존재하여 $$ab=0$$인 것이다. 마찬가지로 적당한 $$b\neq 0$$에 대해 $$ba=0$$이면 $$a$$를 *right zero divisor<sub>오른쪽 영인자</sub>*라 한다. 어느 쪽도 아닌 원소, 즉 nonzero 원소 $$b$$에 대해 $$ab=0$$이나 $$ba=0$$이 결코 성립하지 않는 원소를 *regular element<sub>정칙원</sub>* 혹은 non-zero-divisor라 부른다.

</div>

가환환에서는 left zero divisor와 right zero divisor의 구별이 사라지므로 이들을 통틀어 *zero divisor<sub>영인자</sub>*라 부른다. 정의에서 $$0$$ 자신은 $$A\neq 0$$인 한 nonzero 원소 $$1$$과 $$0\cdot 1=0$$을 이루므로 zero divisor이며, regular element는 항상 nonzero이다. Integral domain은 가환환 $$A\neq 0$$ 중에서 $$0$$ 이외의 zero divisor가 없는 것, 즉 모든 nonzero 원소가 regular element인 것으로 특징지어진다. 우리의 관심사는 regular element와 unit 사이의 관계이다.

먼저 한 방향은 일반적인 환에서 항상 성립한다.

<div class="proposition" markdown="1">

<ins id="prop4">**명제 4**</ins> 환 $$A$$의 unit은 left zero divisor도 right zero divisor도 아니다. 즉 모든 unit은 regular element이다.

</div>
<details class="proof" markdown="1">
<summary>증명</summary>

$$u\in A^\times$$이라 하고 적당한 $$b\in A$$에 대해 $$ub=0$$이라 하자. 양변의 왼쪽에 $$u^{-1}$$을 곱하면

$$b=1\cdot b=(u^{-1}u)b=u^{-1}(ub)=u^{-1}\cdot 0=0$$

이므로 $$b=0$$이다. 따라서 $$ub=0$$이 nonzero $$b$$에서 성립할 수 없고, $$u$$는 left zero divisor가 아니다. 마찬가지로 $$bu=0$$이라 하면 오른쪽에 $$u^{-1}$$을 곱하여 $$b=0$$을 얻으므로 $$u$$는 right zero divisor도 아니다. 따라서 $$u$$는 regular element이다.

</details>

명제의 대우를 취하면, zero divisor는 결코 unit이 될 수 없다. 이는 곱셈에 대한 역원을 갖는 원소를 다룰 때 자주 쓰는 사실이다. 가령 [예시 2](#ex2)에서 $$2\in\mathbb{Z}$$가 unit이 아닌 것은 별도의 계산 없이도 다음 절의 관점에서 다시 설명되는데, $$\mathbb{Z}$$ 같은 무한환에서는 regular element가 반드시 unit이 되지는 않는다. 실제로 $$2$$는 $$\mathbb{Z}$$에서 regular element이지만 unit이 아니다. 즉 명제 4의 역은 일반적으로 거짓이다.

그러나 환이 유한하면 사정이 달라진다.

## 유한가환환에서의 regular element

명제 4의 역, 곧 "regular element는 unit이다"가 무한환에서 거짓임을 보았다. 핵심은 곱셈사상의 단사성과 전사성 사이의 간극에 있다. 환 $$A$$의 원소 $$a$$에 대해 left multiplication 사상

$$\lambda_a:A\longrightarrow A,\qquad \lambda_a(x)=ax$$

를 생각하면, $$a$$가 left zero divisor가 아니라는 것은 $$\lambda_a$$가 단사라는 것과 같다. 실제로 $$\lambda_a(x)=\lambda_a(y)$$이면 $$a(x-y)=0$$이고, $$a$$가 left zero divisor가 아니면 $$x-y=0$$이다. 반대로 $$a$$가 unit이라는 것은 (가환환에서) $$\lambda_a$$가 전단사이며 그 역사상이 $$\lambda_{a^{-1}}$$이라는 것에 대응한다. 유한집합에서는 단사사상이 자동으로 전사이므로, 유한환에서는 이 간극이 사라진다.

<div class="proposition" markdown="1">

<ins id="thm5">**정리 5**</ins> $$A$$가 유한가환환이라 하자. 그럼 $$A$$의 원소 $$a$$가 regular element인 것과 unit인 것이 동치이다.

</div>
<details class="proof" markdown="1">
<summary>증명</summary>

[명제 4](#prop4)에 의해 unit은 항상 regular element이므로, regular element가 unit임만 보이면 된다. $$a\in A$$를 regular element라 하고, 곱셈사상

$$\lambda_a:A\longrightarrow A,\qquad \lambda_a(x)=ax$$

를 생각하자. $$\lambda_a(x)=\lambda_a(y)$$이면 $$a(x-y)=0$$인데, $$a$$가 regular element이므로 $$x-y=0$$, 즉 $$x=y$$이다. 따라서 $$\lambda_a$$는 단사이다. 그런데 $$A$$는 유한집합이고, 유한집합에서 자기 자신으로 가는 단사함수는 전사이므로 $$\lambda_a$$는 전사이다. 따라서 $$\lambda_a(v)=1$$을 만족하는 $$v\in A$$가 존재하고, 이는 $$av=1$$을 뜻한다. $$A$$가 가환이므로 $$va=av=1$$이고, 따라서 $$v$$는 $$a$$의 양쪽 역원이다. 즉 $$a\in A^\times$$이다.

</details>

증명에서 가환성은 $$av=1$$로부터 $$va=1$$을 얻는 마지막 단계에만 쓰였다. 비가환환에서도 $$\lambda_a$$의 전사성은 우역원 $$av=1$$을 주지만, 좌역원의 존재까지 보장하려면 right multiplication 사상의 단사성을 따로 써야 한다. Regular element는 양쪽 zero divisor가 아니므로 이 두 사상이 모두 단사이고, 따라서 유한환에서는 가환성 없이도 같은 결론이 성립한다. 우리는 가환의 경우만 필요하므로 위의 진술로 충분하다.

이 정리의 가장 중요한 귀결은 integral domain에 관한 것이다.

<div class="proposition" markdown="1">

<ins id="cor6">**따름정리 6**</ins> 모든 유한 integral domain은 field이다.

</div>
<details class="proof" markdown="1">
<summary>증명</summary>

$$A$$를 유한 integral domain이라 하자. 정의상 $$A$$는 가환이고 $$0\neq 1$$이다 ([\[대수적 구조\] §분수체, ⁋정의 5](/ko/math/algebraic_structures/field_of_fractions#def5)). Field임을 보이려면 모든 nonzero 원소가 unit임을 보이면 된다. Integral domain에는 $$0$$ 이외의 zero divisor가 없으므로 임의의 nonzero 원소 $$a$$는 regular element이다. $$A$$가 유한가환환이므로 [정리 5](#thm5)에 의해 $$a$$는 unit이다. 따라서 모든 nonzero 원소가 unit이고, $$A$$는 field이다.

</details>

이 결과는 유한성이 정수론적 상황에서 갖는 힘을 잘 보여준다. 다음 절에서 보듯 $$\mathbb{Z}/p\mathbb{Z}$$가 소수 $$p$$에 대해 field가 되는 것이 그 전형적인 예이며, 더 일반적으로 임의의 유한 integral domain은 자동으로 그 nonzero 원소들이 곱셈군을 이루는 field가 된다.

## 정수의 잉여류환과 unit group

위의 결과들을 가장 친숙한 유한가환환인 $$\mathbb{Z}/n\mathbb{Z}$$에 적용하면, unit과 zero divisor의 분포가 정수론의 언어로 정확히 기술된다.

<div class="example" markdown="1">

<ins id="ex7">**예시 7**</ins> $$n\geq 1$$에 대해 환 $$\mathbb{Z}/n\mathbb{Z}$$를 보자. 잉여류 $$\bar a$$가 unit이라는 것은 $$\bar a\bar x=\bar 1$$을 만족하는 $$\bar x$$가 존재하는 것, 즉 적당한 정수 $$x,k$$에 대해 $$ax-kn=1$$이 성립하는 것이다. Bézout의 정리에 의해 이러한 $$x,k$$가 존재하는 것은 $$\gcd(a,n)=1$$, 즉 $$a$$가 $$n$$과 서로소인 것과 동치이다. 따라서

$$(\mathbb{Z}/n\mathbb{Z})^\times=\{\bar a:\gcd(a,n)=1\}$$

이고, 이 군의 위수는 $$n$$과 서로소인 $$1$$ 이상 $$n$$ 이하 정수의 개수, 즉 Euler totient $$\varphi(n)$$이다.

반면 $$\gcd(a,n)=d>1$$이고 $$\bar a\neq\bar 0$$이면 $$\bar a$$는 zero divisor이다. 이는 $$\bar a\cdot\overline{n/d}=\overline{a\cdot n/d}=\overline{(a/d)n}=\bar 0$$이고 $$1\le n/d<n$$이라 $$\overline{n/d}\neq\bar 0$$이기 때문이다. 따라서 $$\mathbb{Z}/n\mathbb{Z}$$의 모든 nonzero 원소는 unit이거나 zero divisor이며, 이 분류는 [정리 5](#thm5)의 유한환 판정 ("regular element $$\Leftrightarrow$$ unit")과 정확히 일치한다. 가령 $$n=6$$이면 unit은 $$\bar 1,\bar 5$$의 둘($$\varphi(6)=2$$)이고, $$\bar 2,\bar 3,\bar 4$$는 zero divisor이다. 실제로 $$\bar 2\cdot\bar 3=\bar 0$$이다.

특히 $$n=p$$가 소수이면 $$1,\ldots,p-1$$이 모두 $$p$$와 서로소이므로 $$(\mathbb{Z}/p\mathbb{Z})^\times=\mathbb{Z}/p\mathbb{Z}\setminus\{\bar 0\}$$이고, $$\mathbb{Z}/p\mathbb{Z}$$는 zero divisor를 갖지 않는 유한 integral domain이다. [따름정리 6](#cor6)에 의해 이는 field이며, 이것이 $$p$$개의 원소를 갖는 소체 $$\mathbb{F}_p$$이다.

</div>

위 예시에서 $$\mathbb{Z}/n\mathbb{Z}$$가 소수의 거듭제곱들의 곱으로 분해되는 모습은 중국인의 나머지정리로 정리되며 ([§중국인의 나머지정리, ⁋명제 5](/ko/math/ring_theory/chinese_remainder_theorem#prop5)), 그 곱분해를 떠받치는 idempotent들은 별도의 글에서 다룬다 ([§Idempotent과 곱분해, ⁋예시 8](/ko/math/ring_theory/idempotents#ex8)). 여기서는 unit group이 곱분해와 어떻게 어울리는지를 본다.

## 곱환과 행렬환의 unit group

곱환의 unit group은 성분별로 결정된다. 이는 곱환에서 곱셈이 성분별로 이루어진다는 사실의 직접적 귀결이다.

<div class="proposition" markdown="1">

<ins id="prop8">**명제 8**</ins> 환들 $$A_1,\ldots,A_n$$의 곱환 $$A=A_1\times\cdots\times A_n$$에 대하여, 원소 $$(a_1,\ldots,a_n)$$이 $$A$$의 unit인 것과 각 $$a_i$$가 $$A_i$$의 unit인 것이 동치이다. 따라서 군으로서

$$A^\times=A_1^\times\times\cdots\times A_n^\times$$

이 성립한다.

</div>
<details class="proof" markdown="1">
<summary>증명</summary>

$$A$$의 곱셈은 성분별로 이루어지고 항등원은 $$(1,\ldots,1)$$이다. 원소 $$a=(a_1,\ldots,a_n)$$이 unit이면 $$ab=ba=(1,\ldots,1)$$을 만족하는 $$b=(b_1,\ldots,b_n)$$이 존재하는데, 이는 각 성분에서 $$a_ib_i=b_ia_i=1$$임을 뜻하므로 각 $$a_i$$가 unit이고 $$b_i=a_i^{-1}$$이다. 거꾸로 각 $$a_i$$가 unit이면 $$b=(a_1^{-1},\ldots,a_n^{-1})$$이 $$ab=ba=(1,\ldots,1)$$을 만족하므로 $$a$$가 unit이다. 따라서 $$a\in A^\times$$인 것과 각 $$a_i\in A_i^\times$$인 것이 동치이며, 사상

$$A^\times\longrightarrow A_1^\times\times\cdots\times A_n^\times,\qquad (a_1,\ldots,a_n)\longmapsto(a_1,\ldots,a_n)$$

은 위의 동치에 의해 잘 정의된 전단사이고, 곱셈이 성분별이므로 군준동형사상이다. 즉 군동형사상이다.

</details>

가령 $$\mathbb{Z}/6\mathbb{Z}\cong\mathbb{Z}/2\mathbb{Z}\times\mathbb{Z}/3\mathbb{Z}$$ ([§중국인의 나머지정리, ⁋명제 5](/ko/math/ring_theory/chinese_remainder_theorem#prop5))에 명제 8을 적용하면

$$(\mathbb{Z}/6\mathbb{Z})^\times\cong(\mathbb{Z}/2\mathbb{Z})^\times\times(\mathbb{Z}/3\mathbb{Z})^\times$$

이고, 위수를 비교하면 $$\varphi(6)=\varphi(2)\varphi(3)=1\cdot 2=2$$를 얻는다. 이것이 Euler totient의 곱셈성 $$\varphi(mn)=\varphi(m)\varphi(n)$$ ($$\gcd(m,n)=1$$)의 환론적 출처이다.

행렬환의 경우 unit group은 일반선형군이 된다.

<div class="example" markdown="1">

<ins id="ex9">**예시 9**</ins> 환 $$R$$에 대해 $$n\times n$$ 행렬환 $$M_n(R)$$을 생각하자. 정의상 $$M_n(R)$$의 unit은 곱셈에 대한 양쪽 역원을 갖는 행렬, 즉 invertible matrix이다. 이러한 행렬 전체의 모임을 *general linear group<sub>일반선형군</sub>* $$\GL_n(R)$$이라 적으므로

$$M_n(R)^\times=\GL_n(R)$$

이다. $$R$$가 가환환이면 행렬 $$M\in M_n(R)$$이 invertible인 것과 그 행렬식 $$\det M$$이 $$R^\times$$의 원소인 것이 동치인데, 이는 adjugate 공식 $$M\cdot\operatorname{adj}(M)=\operatorname{adj}(M)\cdot M=(\det M)I$$가 임의의 가환환 위에서 성립하기 때문이다. 실제로 $$\det M\in R^\times$$이면 $$(\det M)^{-1}\operatorname{adj}(M)$$이 $$M$$의 역행렬이고, 거꾸로 $$MN=I$$이면 $$\det M\cdot\det N=\det I=1$$이라 $$\det M\in R^\times$$이다. 따라서

$$\GL_n(R)=\{M\in M_n(R):\det M\in R^\times\}$$

이다. 예를 들어 $$R=\mathbb{Z}$$이면 $$\mathbb{Z}^\times=\{1,-1\}$$이므로 $$\GL_n(\mathbb{Z})$$는 행렬식이 $$\pm 1$$인 정수행렬들로 이루어진다.

$$M_n(R)$$은 $$n\geq 2$$이면 nontrivial한 zero divisor를 가지므로 unit과 zero divisor의 구별이 의미를 갖는다. 가령 $$n=2$$에서 matrix unit $$E_{11},E_{12}$$는 $$E_{12}E_{11}=0$$이지만 $$E_{12}\neq 0$$, $$E_{11}\neq 0$$이므로 둘 다 zero divisor이고, 따라서 [명제 4](#prop4)에 의해 invertible하지 않다.

</div>

## Field와 division ring의 관점

마지막으로, unit의 언어로 division ring과 field를 다시 본다.

<div class="remark" markdown="1">

<ins id="rmk10">**참고 10**</ins> 환 $$A\neq 0$$이 division ring이라는 것은 $$A^\times=A\setminus\{0\}$$인 것, 즉 모든 nonzero 원소가 unit인 것이다 ([\[대수적 구조\] §분수체, ⁋정의 3](/ko/math/algebraic_structures/field_of_fractions#def3)). 가환인 경우가 field이다. 이 관점에서 [명제 4](#prop4)는 division ring에 zero divisor가 없음을 곧바로 함의한다. 모든 nonzero 원소가 unit이고 unit은 zero divisor가 아니므로, division ring (특히 field)에는 $$0$$ 이외의 zero divisor가 없다. 따라서 모든 field는 integral domain이다.

[따름정리 6](#cor6)은 이 함의가 유한한 경우 부분적으로 역전됨을 말한다. 일반적으로 integral domain이 field가 될 필요는 없지만 ($$\mathbb{Z}$$가 반례이다), 유한한 integral domain은 반드시 field이다. 무한한 경우 regular element와 unit의 간극을 메우는 것은 division ring 구조 자체이지 유한성이 아니므로, integral domain을 field로 만드는 표준적 방법은 [정리 5](#thm5)의 유한성 논증 대신 field of fractions를 취하는 것이다 ([\[대수적 구조\] §분수체, ⁋정의 7](/ko/math/algebraic_structures/field_of_fractions#def7)).

</div>

---

**참고문헌**

**[AM]** M. F. Atiyah and I. G. Macdonald, *Introduction to commutative algebra*, Addison–Wesley, 1969.

**[DF]** D. S. Dummit and R. M. Foote, *Abstract algebra*, 3rd ed., Wiley, 2004.

**[Lam]** T. Y. Lam, *A first course in noncommutative rings*, 2nd ed., Graduate Texts in Mathematics 131, Springer, 2001.
