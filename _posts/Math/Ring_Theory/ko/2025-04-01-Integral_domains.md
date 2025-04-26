---

title: "정역"
excerpt: ""

categories: [Math / Ring Theory]
permalink: /ko/math/ring_theory/integral_domains
header:
    overlay_image: /assets/images/Math/Ring_Theory/Integral_domains.png
    overlay_filter: 0.5
sidebar: 
    nav: "ring_theory-ko"

date: 2025-04-01
last_modified_at: 2025-04-01
weight: 1

---

이 카테고리의 글들에서 우리는 ring에 대한 성질들을 조금 더 자세하게 살펴본다. 처음으로 다룰 것은 integral domain이다. ([\[대수적 구조\] §분수체, ⁋정의 5](/ko/math/algebraic_structures/field_of_fractions#def5)) 

## 유클리드 정역

<div class="definition" markdown="1">

<ins id="def1">**정의 1**</ins> Integral domain $A$를 고정하자. 함수 $N : A \to \mathbb{Z}^{\geq0}$가 조건 $N(0) = 0$를 만족하면, 이를 $R$ 위의 *norm<sub>노름</sub>*이라고 한다. 만약 $N(a) > 0$이 모든 $a \neq 0$에 대해 성립하면, 이 norm을 *positive norm*이라 한다. 

</div>

Norm의 조건은 매우 약한 것으로, 가령 동일한 integral domain이 주어졌을 때 이 위에 norm을 정의하는 방법은 매우 많다. 

<div class="definition" markdown="1">

<ins id="def2">**정의 2**</ins> Integral domain $A$가 *Euclidean domain<sub>유클리드 정역</sub>*이라는 것은 $A$ 위에 어떤 norm $N$이 존재하여, 임의의 $a, b \in A$ (단, $$b \neq 0$$)에 대해 $A$ 안의 원소 $q, r$가 존재하여

$$a = qb + r \qquad\text{with $r = 0$ or $N(r) < N(b)$}$$

를 만족하는 것이다. 여기서 $q$를 *몫<sub>quotient</sub>*, $r$을 *나머지<sub>remainder</sub>*라고 부른다.

</div>

이는 $A$를 정수 $\mathbb{Z}$로 대체하고, $N$을 절댓값 함수 $\lvert-\rvert:\mathbb{Z} \rightarrow \mathbb{Z}^{\geq0}$으로 보면 우리가 잘 알고 있는 정수에서의 나눗셈 알고리즘과 동일하다. 또 다른 예로, polynomial ring $\mathbb{K}[\x]$ 위에 $N$을 다항식의 차수를 주는 함수로 정의하면 다항식의 나눗셈 알고리즘을 얻게 될 것이다. 마지막으로, 임의의 field $\mathbb{K}$는 Euclidean domain이며, 이는 모든 $x\in\mathbb{K}$를 $0$으로 보내는 함수 $N$에 의해 얻어진다. 이것이 위의 조건을 만족하는 이유는 field의 모든 (nonzero) 원소는 항상 다른 원소를 나누기 때문이다. 

<div class="proposition" markdown="1">

<ins id="prop3">**명제 3**</ins> Euclidean Domain의 모든 ideal은 principal이다. 좀 더 정확히 말하면, Euclidean Domain $A$의 임의의 영이 아닌 ideal $\mathfrak{a}$에 대하여, $\mathfrak{a}$의 minimal norm을 갖는 원소를 $a$라 하면 $\mathfrak{a}=a$이다. 

</div>
<details class="proof" markdown="1">
<summary>증명</summary>

$\mathfrak{a}$가 zero ideal이라면 증명할 것이 없으므로, $\mathfrak{a}\neq 0$이라 가정하자. 

$\mathfrak{a}\setminus \\{0\\}$의 $N$에 의한 ㅑmage를 보면, $\mathbb{Z}^{\geq 0}$은 well-ordered set이므로 norm이 최소인 $\mathfrak{a}$의 nonzero element $a$를 택할 수 있다. 

$(a)\subseteq \mathfrak{a}$인 것은 자명하므로, $(a)=\mathfrak{a}$임을 보이기 위해서는 반대방향 포함관계만 보이면 충분하다. $\mathfrak{a}$의 임의의 원소 $x$에 대하여 division algorithm을 적용하면

$$x=qa+r,\qquad\text{with $r = 0$ or $N(r) < N(a)$}$$


이다. 그럼 $r = x - qa$이고, $x$와 $qa$ 모두 $\mathfrak{a}$에 속하므로 $r$ 또한 $\mathfrak{a}$에 속한다. 이제 $a$의 norm이 최소라는 가정으로부터 $N(r) < N(a)$는 불가능하므로, $r$은 반드시 $0$이어야 한다. 즉, $x=qa$이고 이로부터  $\mathfrak{a} = (a)$임을 안다.

</details>

이제 다음을 정의하자.

<div class="definition" markdown="1">

<ins id="def4">**정의 4**</ins> Commutative ring $A$와 그 안의 원소 $a, b \in A$ ($b \neq 0$)에 대하여 다음을 정의한다.

1. $a$가 $b$의 *배수*라는 것은 어떤 $x \in A$가 존재하여 $a = bx$인 것을 말한다. 이 경우 $b$가 $a$를 *나눈다*고 하며, 기호로 $b \mid a$라고 쓴다. 
2. $a$와 $b$의 *최대공약수<sub>greatest common divisor</sub>*는 다음 조건을 만족하는 nonzero element $d$를 말한다.
   - $d \mid a$이고 $d \mid b$, 그리고
   - $d'$가 $a \mid d'$이고 $b \mid d'$를 만족하면 항상 $d \mid d'$

$a$와 $b$의 greatest common divisor는 $\gcd(a, b)$ 또는 간단히 $(a, b)$로 쓴다.

</div>

정의에 의해, $b \mid a$가 $A$의 ring에서 성립함은 $(a) \subset (b)$와 동치이다. 특히, $d$가 $a$, $b$의 모든 공약수이면 $(d)$는 $(a, b)$를 포함해야 한다. 따라서 위의 두 조건은 ideal의 언어로 다음과 같이 번역할 수 있다:

- $\mathfrak{a} \subseteq (d)$
- $(d) \subseteq (d')$ for any principal ideal $(d')$ such that $a, b \in (d')$

즉, $a$, $b$의 greatest common divisor는 (존재한다면) $a$, $b$를 포함하는 가장 작은 principal ideal을 생성하는 원소가 된다. 이것이 가능한 integral domain을 *GCD domain*이라 부르지만, 우리의 논의에서 이 정의가 별도로 등장할 일은 없다. 

위의 논의를 통해 다음이 성립한다. 

<div class="proposition" markdown="1">

<ins id="prop5">**명제 5**</ins> Commutative ring $A$ 안의 $a, b \in A$가 $0$이 아니라고 하자. 만약 $a$와 $b$로 생성되는 ideal $(a, b)$가 어떤 원소 $d \in A$로 생성되는 principal ideal $(d)$라면, $d$는 $a$와 $b$의 greatest common divisor이다.

</div>

그럼 최대공약수는 유일하게 결정된다. 이 유일성을 말할 때는 다소 주의해야 하는데, 가령 정수에서 $(2)$와 $(-2)$는 같은 ideal이 되기 때문이다. 

<div class="proposition" markdown="1">

<ins id="prop6">**명제 6**</ins> $A$를 integral domain이라 하자. $A$의 두 원소 $d, d' \in A$가 같은 principal ideal, 즉 $(d) = (d')$를 생성한다고 하자. 그러면 $d' = ud$인 어떤 unit $u \in A$가 존재한다.

</div>

<details class="proof" markdown="1">
<summary>증명</summary>

$d = 0$이거나 $d' = 0$이면 자명하므로, $d, d'$가 모두 $0$이 아니라고 가정하자. 즉, $(d) = (d')$이므로 적당한 $x, y \in A$가 존재하여

$$d = xd',\qquad d' = yd$$

를 만족한다. 그러면 $d = xyd$로부터 $(1-xy)d=0$이다. 이제 $A$가 integral domain이라는 가정과 $d \neq 0$으로부터 $xy = 1$이라는 것을 알고, 따라서 $xy$는 각각이 서로의 역원이 되는 unit이다. 

</details>

그럼 정수에서의 Bézout lemma와 마찬가지로, Euclidean domain에 대해서 다음이 성립한다. 

<div class="proposition" markdown="1">

<ins id="thm7">**정리 7**</ins> $A$를 Euclidean domain이라 하자. $a, b \in A$가 $0$이 아닌 원소들이고, $r_n$을 $a, b$에 대하여 [정의 2](#def2)의 과정을 반복하였을 때 더 진행이 불가능한 마지막 nonzero remainder라 하자. 그러면 다음이 성립한다:

1. $r_n$은 $a, b$의 greatest common divisor이다. 
2. $(r_n)$은 $(a, b)$와 같은 ideal이다. 특히 $r_n$은 $a, b$의 $A$-linear combination으로 쓸 수 있으며, 즉 어떤 $x, y \in A$가 존재하여 $r_n=ax+by$를 만족한다.

</div>

<details class="proof" markdown="1">
<summary>증명</summary>

$r_n$이 $a$와 $b$를 나눈다는 것을 보이자. Euclidean algorithm의 마지막 단계는 다음의 식
    
$$r_{n-1} = q_n r_n$$

으로 주어졌을 것이며, 일반적으로는

$$r_{k-2}=q_{k}r_{k-1}+r_{k}$$

의 형태가 된다. 여기서 $r_{-2}=a$, $r_{-1}=b$로 잡는다. 우리의 주장은 모든 나머지 $r_k$들이 $r_n$으로 나누어진다는 것이다. 이를 위해 위의 식을 거꾸로 따라가며 귀납법을 사용하자.

우선 $r_n\mid r_{n-1}$은 자명하다. 따라서 $r_n \mid r_k$와 $r_n \mid r_{k-1}$을 가정하면, 위의 식을 통해 $r_n$이 $r_{k-2}$ 또한 나눈다는 것을 알 수 있고 이로부터 귀납적으로 $r_n$이 $a$와 $b$ 각각을 나누는 것을 안다. 즉, $(a), (b)\subset (r_n)$이므로 이로부터 $(a,b)\subset (r_n)$임을 안다. 한편 $r_n$이 $a$와 $b$의 최대공약수이기 위해서는 $(a,b)=(r_n)$이 성립해야 하며, 이는 마찬가지로 위의 식들을 통해 $r_n$을 $a$와 $b$의 $A$-linear combination으로 나타낼 수 있기 때문에 자명하다. 

</details>


## 주아이디얼정역

이제 우리는 다음을 정의한다. 

<div class="definition" markdown="1">

<ins id="def8">**정의 8**</ins> Ring $A$가 *principal ideal domain<sub>주아이디얼정역</sub>*이라는 것은 모든 ideal이 principal인 integral domain을 말한다.

</div>

그럼 [명제 3](#prop3)으로부터 우리는 임의의 Euclidean domain은 항상 PID임을 안다. 그러나 그 역은 성립하지 않는다. Division algorithm은 두 원소 $a,b$가 주어졌을 때 이들의 최대공약수를 얻는 방법을 구체적으로 주지만, [명제 5](#prop5)에 의하여 다음이 성립한다. 

<div class="proposition" markdown="1">

<ins id="cor9">**따름정리 9**</ins> $A$를 Principal Ideal Domain이라 하고, $a, b \in A$가 $0$이 아닌 원소들이라 하자. $a, b$로 생성된 principal ideal $(a, b)$의 generator를 $d$라 하면 다음이 성립한다:

1. $d$는 $a$와 $b$의 greatest common divisor이다.
2. $d$는 $a$와 $b$의 $A$-linear combination으로 쓸 수 있다. 즉, $x, y \in A$가 존재하여

   $$d = ax + by$$

   를 만족한다.
3. $d$는 [명제 6](#prop6)의 센스에서 유일하다. 

</div>
<details class="proof" markdown="1">
<summary>증명</summary>

[명제 5](#prop5), [명제 6](#prop6)의 결과이며, 둘째 결과는 $(a,b)=(d)$라는 가정으로부터 자명하다. 

</details>

Principal ideal domain의 유용한 성질 중 하나는 임의의 prime ideal이 항상 maximal이라는 것이다. 

<div class="proposition" markdown="1">

<ins id="prop10">**명제 10**</ins> Principal Ideal Domain $A$의 모든 $0$이 아닌 prime ideal은 maximal ideal이다.

</div>

<details class="proof" markdown="1">
<summary>증명</summary>

결론에 반하여 $A$의 nonzero prime idea$\mathfrak{p} = (p)$에 대하여 $\mathfrak{p} \subsetneq \mathfrak{m} = (m)$인 ideal $\mathfrak{m}$이 있다고 하자. 그럼 우선 $p \in \mathfrak{m} = (m)$이므로, 적당한 $r\in A$에 대하여 $p = rm$이고, $\mathfrak{p}$가 prime ideal이라는 가정으로부터 $r\in \mathfrak{p}$이거나 $m\in\mathfrak{p}$이고, 가정 $\mathfrak{p} \subsetneq \mathfrak{m}$로부터 $m\not\in \mathfrak{p}$여야 한다. 그런데 만약 $r \in \mathfrak{p} = (p)$라면 적당한 $s\in A$에 대하여 $r = ps$이고, 따라서 $p = rm = psm$이므로 $1 = sm$이이다. 즉, $m$은 unit이고 이는 $\mathfrak{m}$이 maximal ideal이라는 가정에 모순이다. (정의에 의해, $A$ 자기자신은 maximal ideal이 아니다.)

</details>

## 단일인수분해정역

이제 우리는 마지막으로 단일인수분해정역을 정의한다. 이를 위해 우선 용어를 정리하자. 

<div class="definition" markdown="1">

<ins id="def11">**정의 11**</ins> $A$를 integral domain이라 하자. 

1. Nonzero, non-unit $r\in A$를 고정하자. 만일 $r = ab$를 만족하는 어떤 $a,b$가 주어질 때마다 $a$ 혹은 $b$ 중 적어도 하나가 반드시 unit이라면 $r$을 *irreducible<sub>기약</sub>*이라고 한다. 그렇지 않으면 $r$은 *reducible*이라 부른다.
2. Nonzero, non-unit $p \in A$를 고정하자. 만일 $p \mid ab$를 만족하는 어떤 $a,b$가 주어질 때마다 항상 $p \mid a$ 또는 $p \mid b$를 만족하면 $p$를 *prime*이라고 한다. 
3. 두 원소 $a,b$에 대하여, 만일 $A$의 적당한 unit $u$가 존재하여 $a=ub$라면 이들이 *associate in $R$*이라 부른다. 

</div>

가령 $\mathbb{Z}$를 보자. 우리는 $\mathbb{Z}$의 임의의 원소, 예를 들어 $10$이 주어졌을 떄 이를 유일하게 $2\times 5$의 꼴로 인수분해할 수 있다고 주장하고 싶다. 그러나 $\mathbb{Z}$의 $1$이 아닌 unit, 즉 $-1$ 때문에 다음의 식

$$10=2\times 5=(-2)\times (-5)=(-1)^2\times 2\times 5=\cdots$$

과 같은 형태의 곱으로 $10$을 나타낼 수도 있으며, 우리는 이러한 식은 서로 다르지 않은 것으로 취급하고 싶다. 이 때문에 위의 정의에서 unit만큼 차이나는 두 원소는 (사실상) 같은 것으로 보는 것이다. 

한편, irreducible과 prime의 차이는 다소 미묘한데, 단일인수분해정역을 제대로 정의하기 위해서는 이들을 확실하게 구별해야 한다. 우선 다음 명제는 자명하다. 

<div class="proposition" markdown="1">

<ins id="prop12">**명제 12**</ins> Integral domain $A$에서 prime element는 항상 irreducible이다.

</div>

<details class="proof" markdown="1">
<summary>증명</summary>

원소 $p \in A$가 prime element라 가정하고, 적당한 $a,b$에 대하여 $p = ab$라 하자. 그럼 $p\mid a$이거나 $p\mid b$이므로, 일반성을 잃지 않고 $p\mid a$라 하자. 즉 적당한 $r\in A$가 존재하여 $a=pr$이다. 이제 $p=ab=prb$로부터, $p(1-rb)=0$이고 $A$는 integral domain이며, $p$가 nonzero이므로 $1-rb=0$이다. 즉 $b$가 unit이다. 

</details>

그러나 그 역이 항상 성립하는 것은 아니다. 

<div class="example" markdown="1">

<ins id="ex13">**예시 13**</ins> 우선 $A=\mathbb{Z}[\sqrt{-5}]$ 위에 다음과 같은 norm

$$N(a + b\sqrt{-5}) := a^2 + 5b^2$$

을 정의하면, 다음의 식

$$N(xy) = N(x)N(y)$$

이 모든 $x,y\in A$에 대해 성립하는 것을 안다. 이로부터, 만일 $x$가 $A$의 unit이라면 반드시 $N(x)=1$이어야 하고, 그 역도 성립함을 안다. 

이제 $A$의 원소 $3$을 생각하자. 그럼 $xy=3$이고 $x$와 $y$가 동시에 non-unit이기 위해서는 

$$N(x) N(y)=N(3) = 9$$

로부터 $N(x)=N(y)=3$이어야만 하는 것을 안다. 그런데 $N$의 정의로부터 이를 만족하는 원소는 존재하지 않으므로, $3$은 irreducible이다.

하지만 $3$은 prime이 아니다. 이는

$$3 \mid (2 + \sqrt{-5})(2 - \sqrt{-5}) = 4 + 5 = 9$$

이지만 $3$은 $2 + \sqrt{-5}$도, $2 - \sqrt{-5}$도 나누지 않기 때문이다. 

</div>

그러나 PID에서는 이것이 항상 성립한다. 

<div class="proposition" markdown="1">

<ins id="prop14">**명제 14**</ins> PID $A$에서 nonzero element가 irreducible인 것과 prime인 것이 동치이다. 

</div>
<details class="proof" markdown="1">
<summary>증명</summary>

$A$의 irreducible element $p \in A$를 고정하자. 보일 것은 $p$가 prime이라는 것, 즉 $(p)$가 prime ideal이라는 것이다. $A$가 P.I.D.이므로 임의의 ideal은 $(m)$의 꼴로 쓰인다. 이제 $(p) \subseteq (m)$이라고 하면 $p = rm$ for some $r \in A$이다. 그런데 $p$는 irreducible이므로 $r$이나 $m$ 중 하나는 unit이어야 한다.

- 만약 $r$이 unit이면 $p$와 $m$은 associate이고, $(p) = (m)$이다.
- 만약 $m$이 unit이면 $(m) = A$이다.

따라서 $(p)$를 포함하는 ideal은 $(p)$ 자신이거나 $A$뿐이므로, $(p)$는 maximal이고, P.I.D.에서는 maximal ideal은 항상 prime이므로 $(p)$는 prime ideal이다. 따라서 $p$는 prime element이다.

</details>

따라서 [예시 13](#ex13)의 $A=\mathbb{Z}[\sqrt{-5}]$는 PID가 아니다.

<div class="example" markdown="1">

<ins id="ex15">**예시 15**</ins> 정의를 사용하여 $A=\mathbb{Z}[\sqrt{-5}]$가 실제로 PID가 아님을 보이자. 우리 주장은 다음의 ideal

$$\mathfrak{a}=(3, 1+\sqrt{-5})$$

이 non-principal이라는 것이다. 앞서 [예시 13](#ex13)에서 정의한 norm을 계속 사용하자. 그럼 

$$N(3)=9,\qquad N(1+\sqrt{-5})=6$$

이므로 만일 적당한 $x\in A$가 존재하여 $\mathfrak{a}=(a)$라면 $N(x)$는 $3$의 약수여야 한다. 그러나 [예시 13](#ex13)에서 살펴본 것과 같이 $N(x)=3$을 만족하는 $x\in A$는 존재하지 않으므로, 유일한 가능성은 $N(x)=1$이고 따라서 $(3, 1+\sqrt{-5})$가 unit ideal인 것이다. 

그러나 $2\not\in \mathfrak{a}$이다. 이를 보이기 위해, 적당한 $x,y\in A$에 대하여

$$2=3x+(1+\sqrt{-5})y$$

라 하자. $x = a_1 + a_2\sqrt{-5}$, $y = b_1 + b_2\sqrt{-5}$라 하고 우변을 전개하면

$$3x + (1+\sqrt{-5})y = (3a_1 + b_1 - 5b_2) + (3a_2 + b_1 + b_2)\sqrt{-5}$$

이므로, 이것이 $2$가 되려면 다음의 두 연립방정식

$$\begin{cases}3a_1 + b_1 - 5b_2 = 2 \\3a_2 + b_1 + b_2 = 0\end{cases}$$

이 성립해야 한다. 그런데 두 번째 식에서 $b_1 = -3a_2 - b_2$를 첫 번째 식에 대입하면

$$3a_1 - 3a_2 - 6b_2 = 2$$

를 얻는데, 좌변은 $3$의 배수인 반면 우변은 그렇지 않으므로 모순이다. 즉, $(3, 1+\sqrt{-5}) \neq (1)$이다.

</div>

이제 다음을 정의하자.

<div class="definition" markdown="1">

<ins id="def16">**정의 16**</ins> Integral domain $A$가 *unique factorization domain<sub>단일인수분해정역</sub>*인 것은 모든 non-zero, non-unit $a\in A$에 대하여 다음 두 조건이 성립하는 것이다. 

1. $a$는 $A$의 irreducible element들의 유한곱으로 표현될 수 있다. 즉, 적당한 irreducible $p_1, \dots, p_n \in A$가 존재하여
    
    $$a = p_1 p_2 \cdots p_n$$

   으로 쓸 수 있다.
2. 위의 표현은 *associate* 관계를 제외하고 유일하다. 즉, $a = q_1 q_2 \cdots q_m$이 또 다른 표현이라면 $m = n$이고, 적당한 재배열 후 각 $p_i$와 $q_i$가 서로 associate이도록 할 수 있다. 

</div>

그럼 다음이 성립한다. 

<div class="proposition" markdown="1">

<ins id="prop17">**명제 17**</ins> UFD $A$에서 nonzero element가 irreducible인 것과 prime인 것이 동치이다. 

</div>

<details class="proof" markdown="1">
<summary>증명</summary>

Irreducible element가 항상 prime임을 보이면 충분하다.

Irreducible element $p \in A$를 택하고, $p \mid ab$ for some $a, b \in A$라 하자. 그럼 $p \mid a$ 또는 $p \mid b$임을 보여야 한다. 우선 $A$는 UFD이므로 $a$, $b$, $ab$를 irreducible들의 곱으로 쓸 수 있다. 이를 이용해

$$a = p_1 \cdots p_k,\quad b = q_1 \cdots q_l$$

이라 하면 $ab = p_1 \cdots p_k q_1 \cdots q_l$이다. 여기에서 $p \mid ab$라 함은 어떤 $c \in A$가 존재하여 $ab = pc$인 것이다. 이제 $p$도 irreducible이고 $ab$도 irreducible들의 곱으로 표현되므로, UFD의 정의에 따라 $p$는 $ab$의 성분 $p_i$ 혹은 $q_j$ 중 어떤 하나와 associate 관계에 있고, 이에 따라 $p$는 $a$를 나누거나 $b$를 나눈다. 

</details>

UFD는 그 정의에 의해 임의의 원소를 인수분해할 수 있는 integral domain이다. 두 정수를 소인수분해 하였을 때의 좋은점은, 이로부터 이들의 최대공약수가 바로 나온다는 것이다. 

<div class="proposition" markdown="1">

<ins id="prop18">**명제 18**</ins> $A$를 Unique Factorization Domain이라 하자. $a, b \in A$가 $0$이 아닌 원소들이고 다음과 같은 prime factorization을 갖는다고 하자:

$$a = u \cdot p_1^{e_1} p_2^{e_2} \cdots p_n^{e_n}, \qquad b = v \cdot p_1^{f_1} p_2^{f_2} \cdots p_n^{f_n}$$

여기서 $u, v \in A^\times$는 unit들이고, $p_1, \dots, p_n$은 서로 다른 irreducible (또는 prime)들이며, $e_i, f_i \geq 0$이다. 그러면 다음과 같이 정의된 원소

$$d = p_1^{\min(e_1, f_1)} p_2^{\min(e_2, f_2)} \cdots p_n^{\min(e_n, f_n)}$$

는 $a$와 $b$의 greatest common divisor이다. (단, 모든 지수가 $0$이면 $d = 1$이다.)

</div>

<details class="proof" markdown="1">
<summary>증명</summary>

먼저 $d$의 각 prime 인수 $p_i$의 지수 $\min(e_i, f_i)$는 $a$와 $b$ 양쪽의 factorization에서 $p_i$가 등장하는 최소 횟수이므로, $d \mid a$이고 $d \mid b$임이 자명하다. 즉, $d$는 공약수이다.

이제 $c$를 $a$와 $b$의 임의의 공약수라고 하자. 그러면 $c$의 prime factorization은 다음과 같다:

$$c = q_1^{g_1} \cdots q_m^{g_m}$$

그런데 $c \mid a, b$이므로 각 $q_j$는 $a$ 또는 $b$의 어떤 prime factor와 associate해야 한다. 즉, $\\{q_1, \dots, q_m\} \subseteq \{p_1, \dots, p_n\\}$이다.

또한 각 지수 $g_j$는 $a$와 $b$에서 $q_j$의 지수 이상일 수 없으므로, $g_j \leq \min(e_j, f_j)$이다.  따라서 $c \mid d$이고, $d$는 $a$, $b$의 greatest common divisor이다.

</details>

그럼 다음 정리는 지금까지 다룬 세 정의를 한데 묶어준다. 

<div class="proposition" markdown="1">

<ins id="thm19">**정리 19**</ins> 모든 Euclidean domain은 Principal Ideal Domain이고, 모든 Principal Ideal Domain은 Unique Factorization Domain이다. 특히, 모든 Euclidean domain은 Unique Factorization Domain이다.

</div>

<details class="proof" markdown="1">
<summary>증명</summary>

보여야 할 것은 오직 임의의 PID가 UFD라는 사실 뿐이다. PID $A$를 고정하고, non-zero, non-unit $r\in A$를 고정하자. 우선 우리는 prime ideal들의 chain

$$(r)=(r_0) \subsetneq (r_1) \subsetneq (r_2) \subsetneq \cdots$$

를 귀납적으로 만들어낼 것이다. 만일 $r$가 irreducible이라면 여기서 과정을 끝내고, 그렇지 않다면 non-unit인 $r_1, r_2$가 존재하여 $r = r_1 r_2$와 같이 쓸 수 있다. 다시 이들 둘 모두가 irreducible이라면 여기에서 과정을 종료하고, 그렇지 않다면 이 과정을 반복하는 식으로 위의 ideal들의 chain을 잡을 수 있다. 

이제 $\mathfrak{a}=\bigcup_{i=0}^\infty (r_i)$라 하자. 그럼 $\mathfrak{a}$가 ideal인 것은 자명하며, $A$가 PID라는 가정으로부터 $\mathfrak{a}=(a)$이도록 하는 $a\in A$가 존재한다. 그럼 어떠한 $n$에 대해서는 $a\in (r_n)$이어야 하고, 그럼 이 $n$ 이후부터는 $(r_n)$이 항상 $a$를 포함하므로 $(r_n)\subsetneq (r_{n+1})$에 모순이다. 

유일성의 경우는 [명제 18](#prop18)과 비슷한 방법으로 

$$r = p_1 \cdots p_m = q_1 \cdots q_n$$

와 같이 두 개의 표현이 주어졌다 가정하고, $p_1$부터 순서대로 associate관계에 있는 $q_j$들을 찾아가면 된다. 

</details>
