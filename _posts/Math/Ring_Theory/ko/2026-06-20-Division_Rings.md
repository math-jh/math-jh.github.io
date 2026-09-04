---
title: "나눗셈환"
description: "Division ring을 모든 nonzero 원소가 unit인 환으로 정의하고 그 안에 zero divisor가 없음을 보인다. 모든 유한 division ring이 field라는 Wedderburn의 little theorem을 class equation과 cyclotomic polynomial로 증명한 뒤, 무한한 경우의 대표적 예시로 Quaternion ℍ가 noncommutative division ring임을 직접 확인한다. Schur의 보조정리를 통해 simple module의 endomorphism ring으로 division ring이 등장함을 본다."
excerpt: "Division ring과 quaternion, Wedderburn의 little theorem, 그리고 Schur의 보조정리"

categories: [Math / Ring Theory]
permalink: /ko/math/ring_theory/division_rings
sidebar: 
    nav: "ring_theory-ko"

date: 2026-06-20

weight: 5


---

이 글에서 우리는 모든 nonzero 원소가 곱셈에 대한 역원을 갖는 ring, 즉 *division ring*을 본격적으로 다룬다. 

별도의 언급이 없는 한 ring은 항등원 $1\neq 0$을 갖는 것으로 하며, division ring은 commutative임을 가정하지 <em-ko>않는다.</em-ko>

## 나눗셈환과 영인자

Division ring의 정의는 이미 주어졌으나, 이번 글의 시작을 위해 다시 state한다. ([\[대수적 구조\] §분수체, ⁋정의 3](/ko/math/algebraic_structures/field_of_fractions#def3)) 

::: 정의 1
Ring $D\neq 0$이 *division ring<sub>나눗셈환</sub>* 혹은 *skew field<sub>비가환체</sub>*라는 것은 $D$의 모든 nonzero 원소가 곱셈에 대한 양쪽 역원을 갖는 것이다. Commutative division ring을 *field<sub>체</sub>*라 부른다.
:::

우리는 [§가역원과 영인자, ⁋정의 1](/ko/math/ring_theory/units_and_zero_divisors#def1)에서 unit group $D^\times$가 곱셈에 대한 group임을 이미 확인하였으며, division ring에서는 정의에 의해 $D^\times=D\setminus\{0\}$이므로 이것이 곱셈에 대한 group이 된다. 이 group을 $D$의 *multiplicative group*이라 부른다. 

Division ring의 첫 번째 성질은 다음과 같다.

::: 명제 2
Division ring $D$는 nonzero zero divisor를 갖지 않는다. 즉 $ab=0$이면 $a=0$ 또는 $b=0$이다. 특히 모든 field는 integral domain이다.
:::
::: 증명
$a,b\in D$가 $ab=0$이고 $a\neq 0$이라 하자. $D$가 division ring이므로 $a$는 역원 $a^{-1}$을 가지며, 양변의 왼쪽에 $a^{-1}$을 곱하면

$$b=1\cdot b=(a^{-1}a)b=a^{-1}(ab)=a^{-1}\cdot 0=0$$

이다. 따라서 $a\neq 0$이면 $b=0$이고, 이는 $ab=0$에서 $a=0$ 또는 $b=0$임을 뜻한다. 따라서 $D$에는 nonzero zero divisor가 없다. $D$가 field이면 추가로 commutative하고 $0\neq 1$이므로 integral domain이다 ([\[대수적 구조\] §분수체, ⁋정의 5](/ko/math/algebraic_structures/field_of_fractions#def5)).
:::

## Wedderburn의 소정리

위의 [명제 2](#prop2)는 사실 [§가역원과 영인자, ⁋명제 4](/ko/math/ring_theory/units_and_zero_divisors#prop4)로부터도 바로 얻어지는 것으로, division ring에서는 모든 nonzero 원소가 unit이므로 nonzero zero divisor가 존재할 여지가 없다. 그러나 이 역은 일반적으로 사실이 아니며, 가령 $\mathbb{Z}$ 또한 그러하다는 것을 위의 명제 직후에서 이미 살펴보았다. 

뿐만 아니라, 해당 글에서 우리는 이미 위 [명제 2](#prop2)의 부분적인 역, 즉 *finite* ring에 대해서는 integral domain이 항상 field가 된다는 것을 살펴보았다. ([§가역원과 영인자, ⁋따름정리 6](/ko/math/ring_theory/units_and_zero_divisors#cor6)) 이 따름정리의 증명에는 ring의 commutativity가 본질적으로 사용되지 <em-ko>않는데</em-ko>, 그럼에도 불구하고 해당 따름정리에서 commutativity를 가정한 이유는 commutativity를 뺐을 때 다루게 되는 finite non-commutative zero-divisor-free ring이 존재하지 않기 때문이다. 

이 현상을 살펴보기 위해 우리는 우선 division ring $D$의 center $Z(D)$에 대한 성질을 정리한다. 이는 $D$의 commutative subring이며 ([\[대수적 구조\] §환의 정의, ⁋정의 8](/ko/math/algebraic_structures/rings#def8)), 나아가 field이다. 이는 임의의 nonzero $z\in Z(D)$가 $D$ 안에서 역원 $z^{-1}$을 갖고, 임의의 $x\in D$에 대하여 

$$z^{-1}x=z^{-1}xzz^{-1}=z^{-1}zxz^{-1}=xz^{-1}$$

이므로 $z^{-1}\in Z(D)$이기 때문이다. 따라서 $D$가 유한하면 $Z(D)$는 finite field이고, 그 원소의 개수를 $q$라 하면 $q\geq 2$이다.

여전히 위의 유한성을 가정한채로 $D$를 $Z(D)$ 위의 vector space로 보면 $n=\dim_{Z(D)} D$에 대하여 $\lvert D\rvert=q^n$이다. 더 일반적으로 $Z(D)$를 포함하는 $D$의 부분 division ring $D'$ 또한 $Z(D)$ 위의 vector space이므로 그 원소 개수는 $q^d$ 꼴이고, $D$가 $D'$ 위의 $m$차원 vector space이면 $q^n=(q^d)^m$에서 $d\mid n$을 얻는다. 비슷한 결에서, 우리는 이 절의 핵심 결과를 증명하기 위해 다음의 cyclotomic polynomial이 필요하다.

::: 정의 3
양의 정수 $n$에 대하여 *$n$번째 cyclotomic polynomial<sub>원분다항식</sub>* $\Phi_n(\x)$를

$$\Phi_n(\x)=\prod_{\substack{1\leq m\leq n\\ \gcd(m,n)=1}}\bigl(\x-\zeta^m\bigr),\qquad \zeta=e^{2\pi i/n}$$

으로 정의한다. 즉 $\Phi_n(\x)$는 $n$번째 primitive root of unity들을 해로 갖는 monic polynomial이다.
:::

Cyclotomic polynomial의 기본 성질로 우리는 두 가지를 사용한다. 첫째, $\x^n-1$의 모든 해는 어떤 $d\mid n$에 대한 primitive $d$번째 root of unity이므로

$$\x^n-1=\prod_{d\mid n}\Phi_d(\x)$$

이 성립하고, 따라서 여기에 [§다항식환, ⁋명제 5](/ko/math/ring_theory/polynomial_rings#prop5)의 나눗셈을 $\mathbb{Z}[\x]$ 안에서 수행하여 귀납적으로 각 $\Phi_d(\x)$가 정수 계수를 가짐을 안다. 둘째, $n$의 진약수 $d$에 대하여

$$\x^n-1=(\x^d-1)\cdot\prod_{e\mid n\text{ but }e\nmid d}\Phi_e(\x)$$

의 우변에 인수 $\Phi_n(\x)$가 들어 있으므로, $\Phi_n(\x)$는 $\mathbb{Z}[\x]$ 안에서 $(\x^n-1)/(\x^d-1)$을 나눈다. 특히 이 정수 다항식들에 정수 $q$를 대입하면, $\Phi_n(q)$가 $q^n-1$과 $(q^n-1)/(q^d-1)$를 모두 정수로서 나눈다는 것을 안다.

마지막으로 필요한 해석적인 부등식 하나를 따로 떼어 둔다.

::: 명제 4
정수 $q\geq 2$와 $n\geq 2$에 대하여 $\lvert\Phi_n(q)\rvert>q-1$이다.
:::
::: 증명
Cyclotomic polynomial에 $q$를 대입하면 [정의 3](#def3)에 의해

$$\Phi_n(q)=\prod_{\substack{1\leq m\leq n\\ \gcd(m,n)=1}}(q-\zeta^m)$$

이다. 각 인수의 절댓값을 아래에서 평가한다. $\zeta=\cos\theta+i\sin\theta$ ($\theta\neq 0$)이라 하면

$$\lvert q-\zeta^m\rvert^2=(q-\cos m\theta)^2+\sin^2 m\theta=q^2-2q\cos m\theta+1$$

이고, 따라서

$$\lvert q-\zeta^m\rvert^2-(q-1)^2=q^2-2q\cos m\theta+1-(q^2-2q+1)=2q(1-\cos m\theta)\geq 0$$

이다. 모든 primitive root $\zeta^m$에 대해 $\lvert q-\zeta^m\rvert\geq q-1\geq 1$이고, 특히

$$\lvert\Phi_n(q)\rvert=\prod_{\substack{1\leq m\leq n\\ \gcd(m,n)=1}}\lvert q-\zeta^m\rvert\geq\lvert q-\zeta\rvert\geq q-1$$

인데, 마지막 부등식의 경우 $\zeta\neq 1$, 즉 $\cos\theta\neq 1$임을 이용하면 이 부등식이 strict하므로 명제의 strict한 부등식을 얻는다.
:::

이제 정리를 증명한다.

::: 정리 5 (Wedderburn)
모든 finite division ring은 field이다. 즉 finite division ring은 commutative하다.
:::
::: 증명
$D$를 finite division ring, $Z=Z(D)$를 그 center라 하자. 앞서 보았듯 $Z$는 finite field이고, 그 원소의 개수를 $q\geq 2$라 하면 $D$는 $Z$ 위의 유한차원 vector space로서 그 원소의 개수는 $\lvert D\rvert=q^n$의 꼴이다. 우리 주장은 $n=1$이어서 $D=Z$가 commutative하다는 것이다.

이를 위해 multiplicative group $D^\times=D\setminus\{0\}$의 class equation을 만들자. ([\[대수적 구조\] §군의 작용, ⁋정리 14](/ko/math/algebraic_structures/group_actions#thm14)) [\[대수적 구조\] §군의 작용, ⁋명제 9](/ko/math/algebraic_structures/group_actions#prop9)의 conjugation action에 대한 $D^\times$의 class equation은

$$\lvert D^\times\rvert=\lvert Z(D^\times)\rvert+\sum_{x}\bigl[D^\times:C_{D^\times}(x)\bigr]$$

이며, 여기서 $C_{D^\times}(x)$는 [\[대수적 구조\] §군의 작용, ⁋정의 12](/ko/math/algebraic_structures/group_actions#def12) 직후에 정의한 $x$의 centralizer이고 합은 $Z(D^\times)$에 속하지 않는 모든 representative에 대한 것이다. 또, $Z(D^\times)=Z^\times=Z\setminus\{0\}$이므로 $\lvert Z(D^\times)\rvert=q-1$이다.

이제 각 $x\in D^\times$에 대하여 $C_D(x)=\{y\in D\mid xy=yx\}$는 $D$의 부분 division ring이고 $Z$를 포함한다. 이러한 경우 우리는 $C_D(x)$가 $Z$-vector space라는 것을 보았으며, $\lvert Z\rvert=q$이므로 $\lvert C_D(x)\rvert=q^{d(x)}$ 꼴이다. 또한 $D$가 $C_D(x)$ 위의 vector space이므로 $d(x)\mid n$이다. $C_{D^\times}(x)=C_D(x)\setminus\{0\}$이므로

$$\bigl[D^\times:C_{D^\times}(x)\bigr]=\frac{q^n-1}{q^{d(x)}-1}$$

이고, 이 수가 정수이려면 $d(x)\mid n$이어야 한다. 이제 $x$가 center에 속하지 않으면 $C_D(x)\neq D$이므로 $d(x)<n$이다. 따라서 class equation은

$$q^n-1=(q-1)+\sum_{x}\frac{q^n-1}{q^{d(x)}-1}\tag{$\ast$}$$

의 형태가 되며, 여기서 합의 각 $d(x)$는 $n$의 진약수이다.

이제 $n\geq 2$라 가정하고 모순을 얻자. Cyclotomic polynomial $\Phi_n(q)$는 $q^n-1$을 나누며, 각 진약수 $d=d(x)<n$에 대해 $\frac{q^n-1}{q^d-1}$도 나눈다. 따라서, 위의 $(\ast)$에서 $\Phi_n(q)$는 반드시 $q-1$도 나눠야 한다. 즉 $\Phi_n(q)\mid q-1$이고 $q-1\geq 1$이므로 $\lvert\Phi_n(q)\rvert\leq q-1$이다. 그러나 [명제 4](#prop4)에 의해 $n\geq 2$이면 $\lvert\Phi_n(q)\rvert>q-1$이므로 모순이다.
:::

이 정리의 첫 번째 결과는 finite integral domain에 대한 결과를 다시 확인하는 것이다.

::: 따름정리 6
$0\neq 1$인 finite ring $A$가 nonzero zero-divisor를 갖지 않으면 $A$는 field이다.
:::
::: 증명
$A$가 finite ring이고 $0$ 이외의 zero divisor가 없다고 하자. 임의의 nonzero $a\in A$에 대해 left multiplication morphism $\lambda_a:A\rightarrow A$, $\lambda_a(x)=ax$를 생각하면, $ax=ay$일 때 $a(x-y)=0$이고 $a$가 zero divisor가 아니므로 $x=y$, 즉 $\lambda_a$가 단사이다. $A$가 유한집합이므로 $\lambda_a$는 전사이고, $av=1$인 $v$가 존재한다. 같은 논법을 right multiplication에 적용하면 $wa=1$인 $w$가 존재하며, $w=w(av)=(wa)v=v$이므로 $v$는 $a$의 양쪽 역원이다. 따라서 모든 nonzero 원소가 unit이고 $A$는 division ring이다. 유한 division ring은 [정리 5](#thm5)에 의해 field이다.
:::

이것이 [§가역원과 영인자, ⁋따름정리 6](/ko/math/ring_theory/units_and_zero_divisors#cor6)과 본질적으로 다른 것은 $A$의 commutativity를 가정하지 않았다는 것이다. 만일 commutativity를 처음부터 가정했다면 이 따름정리를 증명하는 데에는 [정리 5](#thm5)가 필요하지 않았다. 이 정리의 힘은 commutativity 없이 유한성에 대한 가정만으로 같은 일을 수행했다는 것에 있다. 

## 사원수

[정리 5](#thm5)에 의해 non-commutative division ring은 필연적으로 무한하므로, 그 예시는 무한한 ring에서 찾아야 한다. 가장 고전적인 것은 Hamilton이 정의한 *quaternion*들의 공간으로, 이는 실수체 $\mathbb{R}$ 위의 $4$차원 vector space에 곱셈을 부여한 것이다.

::: 정의 7
*Quaternion algebra<sub>사원수 대수</sub>* $\mathbb{H}$는 기저 $1,i,j,k$를 갖는 $\mathbb{R}$ 위의 $4$차원 vector space로서, 그 원소는

$$q=a+bi+cj+dk\qquad(a,b,c,d\in\mathbb{R})$$

의 꼴이며, 곱셈은 $1$을 항등원으로 하고 기저원소들에 대해 관계식

$$i^2=j^2=k^2=-1,\qquad ij=k,\quad jk=i,\quad ki=j,\qquad ji=-k,\quad kj=-i,\quad ik=-j$$

를 $\mathbb{R}$-bilinear하게 확장하여 정의한 것이다.
:::

관계식을 bilinear하게 확장했다는 것만으로는 이 곱셈이 결합적이라는 것이 따라오지 않으므로, 이는 따로 확인해야 한다. 가장 간단한 방법은 $\mathbb{H}$를 $2\times 2$ complex matrix들의 ring $\Mat_2(\mathbb{C})$ 안에서 실현하는 것이다. 주어진 quaternion $q=a+bi+cj+dk$에 대해 $z=a+bi$, $w=c+di$로 두고 $\mathbb{R}$-linear map $\varphi:\mathbb{H}\rightarrow\Mat_2(\mathbb{C})$를

$$\varphi(q)=\begin{pmatrix}z&w\\ -\bar w&\bar z\end{pmatrix}$$

로 정의하면, 기저원소들의 상은

$$\varphi(1)=I,\qquad\varphi(i)=\begin{pmatrix}i&0\\ 0&-i\end{pmatrix},\qquad\varphi(j)=\begin{pmatrix}0&1\\ -1&0\end{pmatrix},\qquad\varphi(k)=\begin{pmatrix}0&i\\ i&0\end{pmatrix}$$

이고, 이 네 행렬이 [정의 7](#def7)의 관계식을 모두 만족하는 것은 직접 계산으로 확인된다. 양변이 $q,q'$에 대해 각각 bilinear하므로 이로부터 모든 quaternion에 대해 $\varphi(qq')=\varphi(q)\varphi(q')$이 성립하고, 위의 네 행렬이 $\mathbb{R}$ 위에서 linearly independent이므로 $\varphi$는 단사이다. 따라서 $\Mat_2(\mathbb{C})$의 곱셈이 결합적이라는 사실이 $\mathbb{H}$로 옮겨 오며, $\mathbb{H}$는 subring $\varphi(\mathbb{H})\subseteq\Mat_2(\mathbb{C})$와 isomorphic한 ring이 된다. 한편 이 행렬의 determinant 

$$\lvert z\rvert^2+\lvert w\rvert^2=a^2+b^2+c^2+d^2$$

이 곧 quaternion의 norm을 정의한다. 

::: 정의 8
Quaternion $q=a+bi+cj+dk$에 대하여, 그 *conjugate<sub>켤레</sub>*를

$$\bar q=a-bi-cj-dk$$

로, *norm<sub>노름</sub>*을

$$N(q)=q\bar q$$

로 정의한다.
:::

임의의 quaternion $q=a+bi+cj+dk$에 대해, conjugate $\bar q$를 곱하면 실제로 [정의 7](#def7)의 관계식들에 의해 $i,j,k$ 항의 계수가 모두 상쇄되어

$$N(q)=q\bar q=a^2+b^2+c^2+d^2\in\mathbb{R}$$

이 된다는 것을 확인할 수 있다. 특히 $N(q)=0$인 것은 $a=b=c=d=0$, 즉 $q=0$인 것과 동치이다. 또, $\bar q$의 conjugate가 다시 $q$이므로 $\bar qq=\bar q\bar{\bar q}=N(\bar q)=a^2+(-b)^2+(-c)^2+(-d)^2=N(q)$이며, 따라서 $q\bar q$와 $\bar qq$는 모두 $N(q)$와 같다. 

Norm의 또 다른 성질 중 하나는 이것이 곱셈을 보존한다는 것이다. 실제로, conjugate가 $\overline{q_1q_2}=\bar q_2\bar q_1$을 만족하는 것은 쉽게 확인할 수 있고, 이를 이용하면

$$N(q_1q_2)=q_1q_2\overline{q_1q_2}=q_1q_2\bar q_2\bar q_1=q_1N(q_2)\bar q_1=N(q_2)q_1\bar q_1=N(q_1)N(q_2)$$

이 성립한다. 이 곱셈성을 좌표로 풀어쓰면

$$(a_1^2+b_1^2+c_1^2+d_1^2)(a_2^2+b_2^2+c_2^2+d_2^2)=(\cdots)^2+(\cdots)^2+(\cdots)^2+(\cdots)^2$$

이 되며, 이는 두 개의 네 제곱수 합의 곱이 다시 네 제곱수의 합이라는 Euler의 [four-square identity](https://en.wikipedia.org/wiki/Euler%27s_four-square_identity)이다. 어쨌든 우리에게 중요한 것은 이를 사용하여 $\mathbb{H}$가 division ring이라는 사실을 증명할 수 있다는 것이다. 

::: 명제 9
Quaternion algebra $\mathbb{H}$는 noncommutative division ring이다.
:::
::: 증명
$\mathbb{H}$가 $1\neq 0$인 ring임은 위에서 확인하였고, commutative하지 않음은 $ij=k\neq -k=ji$에서 자명하다. 남은 것은 임의의 nonzero $q\in\mathbb{H}$가 곱셈에 대한 양쪽 역원을 가짐을 보이는 것이다.

$q=a+bi+cj+dk\neq 0$이라 하면, 우리는 위에서 $N(q)=a^2+b^2+c^2+d^2$이 양의 실수임을 보았다. 그럼 이는 $\mathbb{H}$의 원소로 볼 수 있으며, 뿐만 아니라 $\mathbb{H}$의 모든 원소와 commute한다. 이는 $N(q)$의 역수 $N(q)^{-1}$ 또한 마찬가지이며, 따라서

$$q\cdot\bigl(N(q)^{-1}\bar q\bigr)=N(q)^{-1}(q\bar q)=N(q)^{-1}N(q)=1$$

이고, 같은 방식으로

$$\bigl(N(q)^{-1}\bar q\bigr)\cdot q=N(q)^{-1}(\bar q q)=N(q)^{-1}N(q)=1$$

가 되는 것을 확인할 수 있다. 즉, $q^{-1}=N(q)^{-1}\bar q$가 $q$의 양쪽 역원이며 이로부터 원하는 주장을 얻는다. 
:::

## 단순 가군의 자기사상환

Division ring은 module의 endomorphism을 다룰 때 유용하게 사용된다. Ring $A$ 위에 정의된 nonzero module $M$이 *simple module<sub>단순가군</sub>*이라는 것은 $M$이 $0$과 자기 자신 외의 submodule을 갖지 않는 것이다. 논의의 편의상 $M$을 left module로 고정하자. 그럼 다음이 성립한다. 

::: 보조정리 10 (Schur)
Ring $A$ 위의 simple module $M,N$에 대하여 다음이 성립한다.

1. 임의의 $A$-module homomorphism $f:M\rightarrow N$은 zero map이거나 isomorphism이다.
2. 특히 simple module $M$의 endomorphism ring $\End_A(M)$은 division ring이다.
:::
::: 증명
$f:M\rightarrow N$을 nonzero $A$-module homomorphism이라 하자. $\ker f$는 $M$의 submodule이고 $f\neq 0$이므로 $\ker f\neq M$이다. $M$이 simple이므로 $\ker f=0$, 즉 $f$는 단사이다. 또 $\im f$는 $N$의 nonzero submodule이고 $N$이 simple이므로 $\im f=N$, 즉 $f$는 전사이다. 따라서 $f$는 isomorphism이다. 이로써 첫째 결과가 성립한다.

이제 $M=N$인 경우를 보면, $\End_A(M)$은 morphism의 합성을 곱셈으로, 항등사상 $\id_M$을 항등원으로 하는 ring이다. $M$이 nonzero이므로 $\id_M\neq 0$, 즉 이 ring은 $0$이 아니다. 첫째 결과에 의해 nonzero $f\in\End_A(M)$은 isomorphism이고, 그 inverse $f^{-1}$ 또한 $A$-module homomorphism이므로 $\End_A(M)$의 원소이다. 또, $f\circ f^{-1}=f^{-1}\circ f=\id_M$이므로 $f$는 unit이다. 즉 모든 nonzero 원소가 unit이고, $\End_A(M)$은 division ring이다.
:::

이 보조정리는 simple module의 endomorphism ring이라는 형태로 division ring을 대량으로 공급한다. 반대로 division ring 자신을 그보다 작은 field 위의 vector space로 보면 그 field 위의 linear endomorphism들로 이루어진 ring 안에서 행렬로 나타나며, [정의 7](#def7) 직후에 손으로 적은 quaternion $\mathbb{H}$의 행렬표현도 이렇게 얻어진다. $\mathbb{H}$의 subfield $\mathbb{C}=\mathbb{R}+\mathbb{R}i$를 왼쪽에서 곱하여 $\mathbb{H}$를 $\mathbb{C}$-vector space로 보면, quaternion $q=a+bi+cj+dk$는 $z=a+bi$, $w=c+di$에 대하여

$$q=z+wj$$

로 유일하게 적히므로 $\{1,j\}$가 이 vector space의 basis이며 $\dim_{\mathbb{C}}\mathbb{H}=2$이다. 이제 각 $q\in\mathbb{H}$에 대한 right multiplication $\rho_q(x)=xq$를 생각하면

$$\rho_q(ux)=uxq=u\rho_q(x)\qquad(u\in\mathbb{C})$$

이므로 $\rho_q$는 $\mathbb{C}$-linear map, 즉 $\End_{\mathbb{C}}(\mathbb{H})$의 원소이고, $\rho_q=0$이면 $q=\rho_q(1)=0$이므로 $q\mapsto\rho_q$는 단사이다. 결합법칙에 의해 $\rho_{qq'}=\rho_{q'}\circ\rho_q$이므로 이 대응은 곱의 순서를 뒤집지만, 좌표를 행벡터로 적어 $\mathbb{C}$-linear map을 오른쪽에서 곱하는 행렬 $M_q$로 나타내면 순서가 한 번 더 뒤집히므로

$$\mathbb{H}\rightarrow\Mat_2(\mathbb{C});\quad q\mapsto M_q$$

는 단사 ring homomorphism이다. 이때 $M_q$의 두 행은 각각 $\rho_q(1)$과 $\rho_q(j)$의 좌표이며, [정의 7](#def7)의 관계식에서 $ji=-ij$이므로 임의의 $u\in\mathbb{C}$에 대하여 $ju=\bar uj$가 성립함을 이용하면 $\rho_q(1)=q=z+wj$와

$$\rho_q(j)=jq=jz+jwj=\bar zj+\bar wj^2=-\bar w+\bar zj$$

로부터

$$M_q=\begin{pmatrix}z&w\\ -\bar w&\bar z\end{pmatrix}$$

를 얻는다. 이것이 앞서 적은 행렬표현이며, 그 determinant $\lvert z\rvert^2+\lvert w\rvert^2$는 곧 norm $N(q)$이므로, nonzero $q$에 대하여 $M_q$가 가역행렬이라는 사실은 [명제 9](#prop9)가 보인 것과 같은 내용이다.

---

**참고문헌**

**[DF]** D. S. Dummit and R. M. Foote, *Abstract algebra*, 3rd ed., Wiley, 2004.  
**[Her]** I. N. Herstein, *Noncommutative rings*, Carus Mathematical Monographs 15, Mathematical Association of America, 1968.  
**[Lam]** T. Y. Lam, *A first course in noncommutative rings*, 2nd ed., Graduate Texts in Mathematics 131, Springer, 2001.
