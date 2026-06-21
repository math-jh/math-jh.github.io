---
title: "Division ring"
description: "Division ring을 모든 nonzero 원소가 unit인 환으로 정의하고 그 안에 zero divisor가 없음을 보인다. Quaternion ℍ가 noncommutative division ring임을 직접 확인하고, 모든 유한 division ring이 field라는 Wedderburn의 little theorem을 class equation과 cyclotomic polynomial로 증명한다. Schur의 보조정리를 통해 simple module의 endomorphism ring으로 division ring이 등장함을 본다."
excerpt: "Division ring과 quaternion, Wedderburn의 little theorem, 그리고 Schur의 보조정리"

categories: [Math / Ring Theory]
permalink: /ko/math/ring_theory/division_rings
sidebar: 
    nav: "ring_theory-ko"

date: 2026-06-20

weight: 1.8

published: false

---

이 글에서 우리는 모든 nonzero 원소가 곱셈에 대한 역원을 갖는 환, 즉 *division ring*을 본격적으로 다룬다. Field는 가환인 division ring으로 이미 등장하였고 ([\[대수적 구조\] §분수체, ⁋정의 3](/ko/math/algebraic_structures/field_of_fractions#def3)), unit과 zero divisor의 언어로도 한 차례 정리하였다 ([§Unit과 zero divisor, ⁋참고 10](/ko/math/ring_theory/units_and_zero_divisors#rmk10)). 여기서는 division ring을 그 자체로 연구한다. 먼저 division ring에 zero divisor가 없음을 확인하고, 가환이 아닌 가장 기본적인 예인 quaternion $$\mathbb{H}$$를 직접 구성하여 그것이 division ring임을 검증한다. 이어서 모든 유한 division ring이 자동으로 field가 된다는 Wedderburn의 little theorem을 class equation과 cyclotomic polynomial을 이용해 증명한다. 마지막으로 Schur의 보조정리를 통해 simple module의 endomorphism ring으로서 division ring이 자연스럽게 출현함을 본다.

별도의 언급이 없는 한 환은 항등원 $$1\neq 0$$을 갖는 것으로 하며, division ring은 가환일 필요가 없다.

## Division ring과 zero divisor

Division ring의 정의는 이미 주어졌으나, 이후 논의의 기준점으로 삼기 위해 다시 적는다.

<div class="definition" markdown="1">

<ins id="def1">**정의 1**</ins> ([\[대수적 구조\] §분수체, ⁋정의 3](/ko/math/algebraic_structures/field_of_fractions#def3)) 환 $$D\neq 0$$이 *division ring<sub>나눗셈환</sub>* 혹은 *skew field*라는 것은 $$D$$의 모든 nonzero 원소가 곱셈에 대한 양쪽 역원을 갖는 것이다. 즉 $$D^\times=D\setminus\{0\}$$이다. 가환인 division ring을 *field<sub>체</sub>*라 부른다.

</div>

Unit의 모임 $$D^\times$$가 군을 이룸은 일반적인 환에서 이미 확인하였으므로 ([§Unit과 zero divisor, ⁋정의 1](/ko/math/ring_theory/units_and_zero_divisors#def1)), division ring에서는 $$D\setminus\{0\}$$ 자체가 곱셈에 대한 군이 된다. 이 군을 $$D$$의 *multiplicative group*이라 부르며, $$D$$가 field일 때 이 군은 가환이다. "Skew field"라는 이름은 가환성("field")이 빠질 수도 있음("skew")을 강조한 것으로, division ring과 같은 뜻이다.

Division ring의 정의는 곱셈 구조에만 관한 조건이지만, 그로부터 덧셈과 곱셈이 얽힌 zero divisor에 대한 정보가 곧바로 나온다.

<div class="proposition" markdown="1">

<ins id="prop2">**명제 2**</ins> Division ring $$D$$는 zero divisor를 갖지 않는다. 즉 $$ab=0$$이면 $$a=0$$ 또는 $$b=0$$이다. 특히 모든 field는 integral domain이다.

</div>
<details class="proof" markdown="1">
<summary>증명</summary>

$$a,b\in D$$가 $$ab=0$$이고 $$a\neq 0$$이라 하자. $$D$$가 division ring이므로 $$a$$는 역원 $$a^{-1}$$을 가지며, 양변의 왼쪽에 $$a^{-1}$$을 곱하면

$$b=1\cdot b=(a^{-1}a)b=a^{-1}(ab)=a^{-1}\cdot 0=0$$

이다. 따라서 $$a\neq 0$$이면 $$b=0$$이고, 이는 $$ab=0$$에서 $$a=0$$ 또는 $$b=0$$임을 뜻한다. 따라서 $$D$$에는 nonzero zero divisor가 없다. $$D$$가 field이면 추가로 가환이고 $$0\neq 1$$이므로 integral domain이다 ([\[대수적 구조\] §분수체, ⁋정의 5](/ko/math/algebraic_structures/field_of_fractions#def5)).

</details>

이는 unit이 결코 zero divisor가 아니라는 일반적 사실 ([§Unit과 zero divisor, ⁋명제 4](/ko/math/ring_theory/units_and_zero_divisors#prop4))의 직접적 귀결이기도 하다. Division ring에서는 모든 nonzero 원소가 unit이므로, nonzero zero divisor가 존재할 여지가 없다. 명제 2의 역, 곧 zero divisor가 없는 환이 항상 division ring이 되는 것은 일반적으로 거짓이다. $$\mathbb{Z}$$는 zero divisor가 없지만 $$2$$가 unit이 아니므로 division ring이 아니다. 이 간극이 유한환에서 사라진다는 사실은 [정리 8](#thm8)에서 다시 다룬다.

## Quaternion

지금까지 등장한 division ring은 모두 가환, 즉 field였다. 가환이 아닌 division ring이 실제로 존재함을 보이기 위해, 우리는 Hamilton의 *quaternion*을 구성한다. 이는 실수체 $$\mathbb{R}$$ 위의 $$4$$차원 vector space에 곱셈을 부여한 것이다.

<div class="definition" markdown="1">

<ins id="def3">**정의 3**</ins> *quaternion algebra<sub>사원수 대수</sub>* $$\mathbb{H}$$는 기저 $$1,i,j,k$$를 갖는 $$\mathbb{R}$$ 위의 $$4$$차원 vector space로서, 그 원소는

$$q=a+bi+cj+dk\qquad(a,b,c,d\in\mathbb{R})$$

의 꼴이며, 곱셈은 $$1$$을 항등원으로 하고 기저원소들에 대해 관계식

$$i^2=j^2=k^2=-1,\qquad ij=k,\quad jk=i,\quad ki=j,\qquad ji=-k,\quad kj=-i,\quad ik=-j$$

를 $$\mathbb{R}$$-쌍선형으로 확장하여 정의한 것이다.

</div>

위의 관계식들은 $$ij=k$$, $$jk=i$$, $$ki=j$$와 $$i^2=j^2=k^2=-1$$만으로 결정된다. 가령 $$ji$$는 $$i^2=j^2=k^2=ijk=-1$$로부터도 유도되는데, $$ijk=-1$$의 양변 왼쪽에 $$i$$를, 오른쪽에 $$k$$를 곱하는 식의 계산으로 $$ji=-k$$ 등을 얻는다. 이 곱셈이 결합적임은 기저원소들에 대해 $$(xy)z=x(yz)$$를 확인하면 충분하며, 이는 위 관계식을 이용한 유한한 경우 점검으로 이루어진다. 곱셈이 가환이 아님은 $$ij=k\neq -k=ji$$에서 즉시 드러난다.

Quaternion이 division ring임을 보이는 핵심 도구는 conjugate와 norm이다.

<div class="definition" markdown="1">

<ins id="def4">**정의 4**</ins> Quaternion $$q=a+bi+cj+dk$$에 대하여, 그 *conjugate<sub>켤레</sub>*를

$$\bar q=a-bi-cj-dk$$

로, *norm<sub>노름</sub>*을

$$N(q)=q\bar q$$

로 정의한다.

</div>

직접 계산하면 norm이 실수임을 알 수 있다. $$q=a+bi+cj+dk$$에 대해 $$\bar q$$를 곱하면, 관계식 $$i^2=j^2=k^2=-1$$과 $$ij=-ji$$ 등에 의해 $$i,j,k$$ 항의 계수가 모두 상쇄되어

$$N(q)=q\bar q=a^2+b^2+c^2+d^2\in\mathbb{R}$$

이 된다. 같은 계산으로 $$\bar q q=a^2+b^2+c^2+d^2$$이므로 $$q\bar q=\bar q q=N(q)$$이고, $$N(q)$$는 $$\mathbb{H}$$의 center에 속하는 실수이다. 특히 $$N(q)=0$$인 것은 $$a=b=c=d=0$$, 즉 $$q=0$$인 것과 동치이다.

<div class="proposition" markdown="1">

<ins id="prop5">**명제 5**</ins> Quaternion algebra $$\mathbb{H}$$는 noncommutative division ring이다.

</div>
<details class="proof" markdown="1">
<summary>증명</summary>

$$\mathbb{H}$$가 $$1\neq 0$$인 결합적 환임은 정의에서 확인하였고, 가환이 아님은 $$ij=k\neq -k=ji$$에서 보았다. 남은 것은 임의의 nonzero $$q\in\mathbb{H}$$가 곱셈에 대한 양쪽 역원을 가짐을 보이는 것이다.

$$q=a+bi+cj+dk\neq 0$$이라 하면 $$N(q)=a^2+b^2+c^2+d^2$$은 양의 실수이다. 실수 $$N(q)$$는 $$\mathbb{H}$$의 center에 속하므로 $$\mathbb{R}\setminus\{0\}$$ 안에서 역수 $$N(q)^{-1}$$을 갖고, 이를 $$\mathbb{H}$$의 원소로 볼 수 있다. 이제

$$q\cdot\bigl(N(q)^{-1}\bar q\bigr)=N(q)^{-1}(q\bar q)=N(q)^{-1}N(q)=1$$

이고, 같은 방식으로

$$\bigl(N(q)^{-1}\bar q\bigr)\cdot q=N(q)^{-1}(\bar q q)=N(q)^{-1}N(q)=1$$

이다. 따라서 $$q^{-1}=N(q)^{-1}\bar q$$가 $$q$$의 양쪽 역원이다. 즉 $$\mathbb{H}$$의 모든 nonzero 원소가 unit이므로 $$\mathbb{H}$$는 division ring이며, 가환이 아니다.

</details>

증명에서 norm이 실수이고 곱셈적이라는 점이 본질적이었다. 실제로 conjugate가 $$\overline{q_1q_2}=\bar q_2\bar q_1$$을 만족함을 확인하면

$$N(q_1q_2)=q_1q_2\overline{q_1q_2}=q_1q_2\bar q_2\bar q_1=q_1N(q_2)\bar q_1=N(q_2)q_1\bar q_1=N(q_1)N(q_2)$$

가 성립하는데, 여기서 $$N(q_2)$$가 center의 원소라는 사실을 썼다. 이 곱셈성

$$(a_1^2+b_1^2+c_1^2+d_1^2)(a_2^2+b_2^2+c_2^2+d_2^2)=(\cdots)^2+(\cdots)^2+(\cdots)^2+(\cdots)^2$$

은 두 개의 네 제곱수 합의 곱이 다시 네 제곱수의 합이라는 Euler의 four-square identity이며, quaternion 곱셈은 이 항등식의 대수적 출처이다. $$\mathbb{H}$$는 가환이 아닌 division ring의 가장 작은 차원의 예 중 하나로, 무한히 많은 nonzero 원소를 가지므로 다음 절의 Wedderburn 정리가 보장하는 유한성의 제약을 받지 않는다.

## Wedderburn의 little theorem

$$\mathbb{H}$$는 무한 division ring이었다. 유한한 경우에는 사정이 근본적으로 달라져서, 가환이 아닌 division ring은 아예 존재하지 않는다. 이것이 Wedderburn의 little theorem이다. 증명은 division ring의 center가 field임을 관찰한 뒤, 그 위의 vector space 구조를 통해 multiplicative group의 class equation을 세우고, cyclotomic polynomial의 정수론적 성질로 모순을 끌어내는 방식으로 진행된다.

먼저 center에 관한 두 관찰을 정리한다. Division ring $$D$$의 *center*를

$$Z=Z(D)=\{z\in D: zx=xz\text{ for all }x\in D\}$$

로 정의하면, $$Z$$는 $$D$$의 가환 부분환이다. 나아가 $$z\in Z$$가 nonzero이면 $$D$$ 안에서 역원 $$z^{-1}$$을 갖는데, 임의의 $$x$$에 대해 $$z^{-1}x=z^{-1}x zz^{-1}=z^{-1}zxz^{-1}=xz^{-1}$$이므로 $$z^{-1}\in Z$$이다. 즉 $$Z$$의 모든 nonzero 원소가 $$Z$$ 안에서 역원을 가지므로, $$Z$$는 field이다. $$D$$가 유한하면 $$Z$$도 유한 field이고, 그 원소의 개수를 $$q$$라 하면 $$q\geq 2$$이다.

이제 $$D$$를 $$Z$$ 위의 vector space로 본다. $$Z$$가 $$q$$개의 원소를 갖는 유한 field이고 $$D$$가 그 위의 $$n$$차원 vector space이면 $$\lvert D\rvert=q^n$$이다. 더 일반적으로, $$D$$의 임의의 부분 division ring $$D'$$이 $$Z$$를 포함하면 $$D'$$ 또한 $$Z$$ 위의 vector space이므로 그 원소 개수는 $$q^d$$ 꼴이며, $$D$$가 $$D'$$ 위의 vector space이기도 하므로 $$q^n=(q^d)^m$$에서 $$d\mid n$$이다. 이 정수론적 제약이 증명의 출발점이다.

증명에는 cyclotomic polynomial이 필요하다.

<div class="definition" markdown="1">

<ins id="def6">**정의 6**</ins> 양의 정수 $$n$$에 대하여 *$$n$$번째 cyclotomic polynomial<sub>원분다항식</sub>* $$\Phi_n(\x)$$를

$$\Phi_n(\x)=\prod_{\substack{1\leq m\leq n\\ \gcd(m,n)=1}}\bigl(\x-\zeta^m\bigr),\qquad \zeta=e^{2\pi i/n}$$

으로 정의한다. 즉 $$\Phi_n(\x)$$는 $$n$$번째 primitive root of unity들을 근으로 갖는 monic polynomial이다.

</div>

Cyclotomic polynomial의 기본 성질로 우리는 두 가지를 사용한다. 첫째, $$\x^n-1$$의 모든 근은 어떤 $$d\mid n$$에 대한 primitive $$d$$번째 root of unity이므로

$$\x^n-1=\prod_{d\mid n}\Phi_d(\x)$$

이 성립하고, 귀납적으로 각 $$\Phi_d(\x)$$가 정수 계수를 가짐을 안다 (monic 다항식의 나눗셈에서 계수가 정수로 유지된다). 둘째, $$d\mid n$$이고 $$d<n$$이면

$$\x^n-1=(\x^d-1)\cdot\!\!\prod_{\substack{e\mid n\\ e\nmid d}}\!\!\Phi_e(\x)$$

의 우변에 인수 $$\Phi_n(\x)$$가 들어 있으므로, $$\Phi_n(\x)$$는 $$\mathbb{Z}[\x]$$ 안에서 $$\dfrac{\x^n-1}{\x^d-1}$$을 나눈다. 이 정수 다항식들에 정수 $$q$$를 대입하면, $$\Phi_n(q)$$가 $$q^n-1$$과 $$\dfrac{q^n-1}{q^d-1}$$ (각 $$d\mid n$$, $$d<n$$)을 모두 정수로서 나눈다.

마지막으로 필요한 해석적 부등식 하나를 따로 떼어 둔다.

<div class="proposition" markdown="1">

<ins id="prop7">**명제 7**</ins> 정수 $$q\geq 2$$와 $$n\geq 2$$에 대하여 $$\lvert\Phi_n(q)\rvert>q-1$$이다.

</div>
<details class="proof" markdown="1">
<summary>증명</summary>

$$\Phi_n(q)=\prod_\zeta(q-\zeta)$$의 곱은 $$n$$번째 primitive root of unity $$\zeta$$들에 대한 것이다. $$n\geq 2$$이면 $$\zeta\neq 1$$이므로, 각 인수의 절댓값을 아래에서 평가한다. $$\zeta=\cos\theta+i\sin\theta$$ ($$\theta\neq 0$$)이라 하면

$$\lvert q-\zeta\rvert^2=(q-\cos\theta)^2+\sin^2\theta=q^2-2q\cos\theta+1$$

이고, $$\cos\theta<1$$이므로

$$\lvert q-\zeta\rvert^2-(q-1)^2=q^2-2q\cos\theta+1-(q^2-2q+1)=2q(1-\cos\theta)>0$$

이다. 따라서 모든 primitive root $$\zeta$$에 대해 $$\lvert q-\zeta\rvert>q-1\geq 1$$이고, primitive root가 적어도 하나 존재하므로

$$\lvert\Phi_n(q)\rvert=\prod_\zeta\lvert q-\zeta\rvert\geq\lvert q-\zeta_0\rvert>q-1$$

을 얻는다.

</details>

이제 정리를 증명한다.

<div class="proposition" markdown="1">

<ins id="thm8">**정리 8 (Wedderburn)**</ins> 모든 유한 division ring은 field이다. 즉 유한 division ring은 가환이다.

</div>
<details class="proof" markdown="1">
<summary>증명</summary>

$$D$$를 유한 division ring, $$Z=Z(D)$$를 그 center라 하자. 앞서 보았듯 $$Z$$는 유한 field이고, 그 원소의 개수를 $$q\geq 2$$라 하면 $$D$$는 $$Z$$ 위의 유한차원 vector space로서 $$\lvert D\rvert=q^n$$의 꼴이다. 보일 것은 $$n=1$$, 즉 $$D=Z$$가 가환이라는 것이다.

이를 위해 multiplicative group $$D^\times=D\setminus\{0\}$$의 class equation을 세운다. $$D^\times$$의 켤레작용에 대한 class equation은

$$\lvert D^\times\rvert=\lvert Z(D^\times)\rvert+\sum_{x}\bigl[D^\times:C_{D^\times}(x)\bigr]$$

이며, 합은 center에 속하지 않는 원소들의 켤레류 대표 $$x$$에 대한 것이다. 여기서 $$Z(D^\times)=Z^\times=Z\setminus\{0\}$$이므로 $$\lvert Z(D^\times)\rvert=q-1$$이다.

각 $$x\in D^\times$$에 대하여 $$C_D(x)=\{y\in D: xy=yx\}$$는 $$D$$의 부분 division ring이고 $$Z$$를 포함한다. 따라서 $$\lvert C_D(x)\rvert=q^{d(x)}$$ 꼴이며, $$D$$가 $$C_D(x)$$ 위의 vector space이므로 $$d(x)\mid n$$이다. $$C_{D^\times}(x)=C_D(x)\setminus\{0\}$$이므로

$$\bigl[D^\times:C_{D^\times}(x)\bigr]=\frac{q^n-1}{q^{d(x)}-1}$$

이고, 이 수가 정수이려면 (그리고 실제로 정수이다) $$d(x)\mid n$$이어야 한다. $$x$$가 center에 속하지 않으면 $$C_D(x)\neq D$$이므로 $$d(x)<n$$이다. 따라서 class equation은

$$q^n-1=(q-1)+\sum_{x}\frac{q^n-1}{q^{d(x)}-1}\tag{$\ast$}$$

의 형태가 되며, 합의 각 $$d(x)$$는 $$n$$의 진약수이다.

이제 $$n\geq 2$$라 가정하고 모순을 끌어낸다. Cyclotomic polynomial $$\Phi_n(\x)$$는 $$q^n-1$$을 나누며, 각 진약수 $$d=d(x)<n$$에 대해 $$\dfrac{q^n-1}{q^d-1}$$도 나눈다. 따라서 $$(\ast)$$에서 $$\Phi_n(q)$$는 좌변 $$q^n-1$$과 우변의 합 부분을 모두 나누므로, 그 차인 $$q-1$$도 나눈다. 즉 $$\Phi_n(q)\mid q-1$$이고 $$q-1\geq 1$$이므로 $$\lvert\Phi_n(q)\rvert\leq q-1$$이다. 그러나 [명제 7](#prop7)에 의해 $$n\geq 2$$이면 $$\lvert\Phi_n(q)\rvert>q-1$$이므로 모순이다.

따라서 $$n=1$$이고 $$D=Z$$이다. $$Z$$는 가환이므로 $$D$$는 field이다.

</details>

증명에서 유한성은 두 곳에서 결정적으로 쓰였다. 하나는 $$D$$가 center $$Z$$ 위의 유한차원 vector space가 되어 위수가 $$q^n$$ 꼴로 표현된 것이고, 다른 하나는 class equation의 항들이 cyclotomic polynomial이라는 강한 정수론적 정보를 갖게 된 것이다. $$\mathbb{H}$$가 무한 noncommutative division ring으로 존재하는 것은 이 두 메커니즘이 무한 차원·무한 위수에서 작동하지 않기 때문이다. Cyclotomic polynomial의 약수 관계와 [명제 7](#prop7)의 부등식만이 본질이며, 그 둘은 위 증명에서 자체적으로 확립하였다. Cyclotomic polynomial의 더 깊은 이론은 별도의 표준 문헌에 미룬다.

이 정리의 첫 번째 귀결은 유한 integral domain에 대한 결과를 다시 준다. 유한 division ring과 유한 integral domain은 가환이라는 결론을 공유하는데, 후자는 곱셈의 단사성에서 직접 따라온 결과였고 ([§Unit과 zero divisor, ⁋따름정리 6](/ko/math/ring_theory/units_and_zero_divisors#cor6)), 전자는 그보다 강한 주장이다.

<div class="proposition" markdown="1">

<ins id="cor9">**따름정리 9**</ins> $$0\neq 1$$인 유한환 $$A$$가 nonzero zero divisor를 갖지 않으면 $$A$$는 field이다.

</div>
<details class="proof" markdown="1">
<summary>증명</summary>

$$A$$가 유한환이고 $$0$$ 이외의 zero divisor가 없다고 하자. 임의의 nonzero $$a\in A$$에 대해 left multiplication 사상 $$\lambda_a:A\to A$$, $$\lambda_a(x)=ax$$를 생각하면, $$ax=ay$$일 때 $$a(x-y)=0$$이고 $$a$$가 zero divisor가 아니므로 $$x=y$$, 즉 $$\lambda_a$$가 단사이다. $$A$$가 유한집합이므로 $$\lambda_a$$는 전사이고, $$av=1$$인 $$v$$가 존재한다. 같은 논법을 right multiplication에 적용하면 $$wa=1$$인 $$w$$가 존재하며, $$w=w(av)=(wa)v=v$$이므로 $$v$$는 $$a$$의 양쪽 역원이다. 따라서 모든 nonzero 원소가 unit이고 $$A$$는 division ring이다. 유한 division ring은 [정리 8](#thm8)에 의해 field이다.

</details>

여기서는 가환성을 가정하지 않고 출발하여 division ring임을 먼저 얻은 뒤 Wedderburn 정리로 가환성을 결론지었다. 가환을 처음부터 가정하면 [정리 8](#thm8) 없이도 곱셈사상의 단사성만으로 field임을 얻으며, 이것이 "유한 integral domain은 field"라는 앞선 결과였다 ([§Unit과 zero divisor, ⁋따름정리 6](/ko/math/ring_theory/units_and_zero_divisors#cor6)). Wedderburn 정리의 힘은 가환 가정 없이 zero divisor의 부재만으로 같은 결론에 이른다는 데에 있다.

## Simple module의 endomorphism ring

Division ring이 자연스럽게 등장하는 또 하나의 맥락은 module 이론이다. 환 $$R$$ 위의 *simple module*은 nonzero이며 $$0$$과 자기 자신 외의 submodule을 갖지 않는 left $$R$$-module이다 ([\[가환대수학\] §조르단-횔더 정리, ⁋정의 1](/ko/math/commutative_algebra/Jordan-Holder_theorem#def1)). Simple module 사이의 homomorphism은 매우 제한되어 있으며, 이를 기술하는 것이 Schur의 보조정리이다.

<div class="proposition" markdown="1">

<ins id="lem10">**보조정리 10 (Schur)**</ins> 환 $$R$$ 위의 simple module $$M,N$$에 대하여 다음이 성립한다.

1. 임의의 $$R$$-module homomorphism $$f:M\to N$$은 zero map이거나 isomorphism이다.
2. 특히 simple module $$M$$의 endomorphism ring $$\End_R(M)$$은 division ring이다.

</div>
<details class="proof" markdown="1">
<summary>증명</summary>

$$f:M\to N$$을 nonzero $$R$$-module homomorphism이라 하자. $$\ker f$$는 $$M$$의 submodule이고 $$f\neq 0$$이므로 $$\ker f\neq M$$이다. $$M$$이 simple이므로 $$\ker f=0$$, 즉 $$f$$는 단사이다. 또 $$\im f$$는 $$N$$의 nonzero submodule이고 $$N$$이 simple이므로 $$\im f=N$$, 즉 $$f$$는 전사이다. 따라서 $$f$$는 isomorphism이다. 이로써 1이 성립한다.

이제 $$M=N$$인 경우를 보면, $$\End_R(M)$$은 사상의 합성을 곱셈으로, 항등사상 $$\id_M$$을 항등원으로 하는 환이다. $$M$$이 nonzero이므로 $$\id_M\neq 0$$, 즉 이 환은 $$0$$이 아니다. 1에 의해 nonzero $$f\in\End_R(M)$$은 isomorphism이고, 그 역사상 $$f^{-1}$$ 또한 $$R$$-module homomorphism이므로 $$\End_R(M)$$의 원소이다. $$f\circ f^{-1}=f^{-1}\circ f=\id_M$$이므로 $$f$$는 unit이다. 따라서 모든 nonzero 원소가 unit이고, $$\End_R(M)$$은 division ring이다.

</details>

이 보조정리는 simple module의 endomorphism ring이라는 형태로 division ring을 대량으로 공급한다. 표현론에서는 이 division ring이 흔히 작은 field로 판명되는데, 가령 algebraically closed field $$\mathbb{C}$$ 위의 유한군 $$G$$의 irreducible representation에 대해 $$\End_{\mathbb{C}[G]}(M)\cong\mathbb{C}$$가 됨이 알려져 있다 ([\[표현론\] §유한군의 표현론, ⁋보조정리 8](/ko/math/representation_theory/representations_of_finite_groups#lem8)). 그러나 base field가 algebraically closed가 아니면 이 division ring이 진정으로 noncommutative하거나 base field보다 큰 field가 될 수 있으며, 이때 보조정리 10이 주는 division ring 구조가 본질적인 정보를 담는다. 이것이 Artin–Wedderburn 이론에서 semisimple ring을 division ring 위의 행렬환들의 곱으로 분해할 때 등장하는 division ring의 출처이다.

Quaternion $$\mathbb{H}$$ 또한 이 관점에 들어맞는다. $$\mathbb{H}$$를 자기 자신 위의 left module로 보면 이는 simple $$\mathbb{H}$$-module이고, 그 endomorphism ring은 right multiplication들로 이루어져 다시 $$\mathbb{H}$$와 동형이 된다. 즉 [명제 5](#prop5)에서 직접 구성한 noncommutative division ring $$\mathbb{H}$$는 simple module의 endomorphism ring으로도 실현되며, 보조정리 10의 결론이 비가환의 경우에도 비어 있지 않음을 보여 준다.

---

**참고문헌**

**[DF]** D. S. Dummit and R. M. Foote, *Abstract algebra*, 3rd ed., Wiley, 2004.

**[Her]** I. N. Herstein, *Noncommutative rings*, Carus Mathematical Monographs 15, Mathematical Association of America, 1968.

**[Lam]** T. Y. Lam, *A first course in noncommutative rings*, 2nd ed., Graduate Texts in Mathematics 131, Springer, 2001.
