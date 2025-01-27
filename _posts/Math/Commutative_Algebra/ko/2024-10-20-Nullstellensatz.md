---

title: "영점정리"
excerpt: ""

categories: [Math / Commutative Algebra]
permalink: /ko/math/commutative_algebra/nullstellensatz
header:
    overlay_image: /assets/images/Math/Commutative_Algebra/Nullstellensatz.png
    overlay_filter: 0.5
sidebar: 
    nav: "commutative_algebra-ko"

date: 2024-10-20
last_modified_at: 2024-10-20
weight: 10

---

## 제이콥슨 환

우리는 ring $A$와 임의의 ideal $\mathfrak{a}$에 대하여, 다음 식

$$\sqrt{\mathfrak{a}}=\bigcap_\text{\scriptsize$\mathfrak{p}$ prime containing $\mathfrak{a}$} \mathfrak{p}$$

이 성립하는 것을 살펴보았다. ([§국소화의 성질들, ⁋따름정리 8](/ko/math/commutative_algebra/properties_of_localization#cor8)) 특히, 만일 $\mathfrak{a}$가 prime ideal이라면 $\mathfrak{p}=\sqrt{\mathfrak{p}}$가 성립해야 하는 것이 당연하다. 더 일반적으로 다음을 정의한다.

<div class="definition" markdown="1">

<ins id="def1">**정의 1**</ins> Ring $A$의 임의의 ideal $\mathfrak{a}$가 *radical ideal<sub>근기아이디얼</sub>*이라는 것은 $\mathfrak{a}=\sqrt{\mathfrak{a}}$가 성립하는 것이다. 

</div>

따라서, 위의 관찰은 한마디로 임의의 prime ideal은 radical이라는 것이다. 이 관찰에 대한 증명은 다소 자명한 부분이 있는데, 만일 우리가 $\mathfrak{p}$를 포함하는 prime ideal들의 교집합 대신, [§정수적 확장, §§나카야마 보조정리](/ko/math/commutative_algebra/integral_extension#나카야마-보조정리)에서와 비슷한 방식으로 $\mathfrak{p}$를 포함하는 *maximal* ideal들의 교집합을 생각했다면 이 관찰이 그리 자명하지 않았을 것이며, 실제로 이것이 성립하지도 않는다. 예컨대 $\mathbb{Z}\_{(2)}$와 같이 maximal ideal이 아닌 prime ideal을 포함하는 임의의 local ring이 모두 반례가 될 것이다. 

<div class="definition" markdown="1">

<ins id="def2">**정의 2**</ins> Ring $A$가 *Jacobson ring<sub>제이콥슨 환</sub>*이라는 것은 임의의 prime ideal이 maximal ideal들의 교집합으로 나타나는 것이다.

</div>

그럼 다음이 성립한다.

<div class="proposition" markdown="1">

<ins id="lem3">**보조정리 3 (Rabinowitch)**</ins> Ring $A$에 대하여, 다음이 동치이다.

1. $A$가 Jacobson ring이다.
2. $A$의 prime ideal $\mathfrak{p}$에 대하여, $(A/\mathfrak{p})[a^{-1}]$이 field이도록 하는 $a\in A/\mathfrak{p}$가 존재한다면, $A/\mathfrak{p}$는 field이다.

</div>
<details class="proof" markdown="1">
<summary>증명</summary>

우선 $A$가 Jacobson이라 가정하자. 그럼 그 quotient $A/ \mathfrak{p}$가 Jacobson이 되는 것도 정의에 의해 자명하다. 한편 [\[대수적 구조\] §분수체, ⁋명제 8](/ko/math/algebraic_structures/field_of_fractions#prop8)에 의해 $A/\mathfrak{p}$는 integral domain이고, integral domain에서 $(0)$은 prime ideal이므로 $(0)$을 maximal ideal들의 교집합으로 나타낼 수 있다. 그런데 [§국소화, ⁋명제 8](/ko/math/commutative_algebra/localization#prop8)에 의하여 $(A/\mathfrak{p})[a^{-1}]$의 prime ideal과, $A/\mathfrak{p}$의 prime ideal 중 $a$를 포함하지 않는 것 사이의 일대일대응이 존재하며, 가정에 의해 $(A/\mathfrak{p})[a^{-1}]$의 prime ideal은 $0$뿐이므로, $A/\mathfrak{p}$의 prime ideal 중 $a$를 포함하지 않는 prime ideal 또한 $0$ 뿐이다. 즉, $A/\mathfrak{p}$의 임의의 nonzero prime ideal에는 항상 $a$가 들어가야 한다. 그런데 만일 이러한 prime ideal이 존재한다면, $A/\mathfrak{p}$는 integral domain이므로 

$$(0)=\sqrt{(0)}=\bigcap_\text{\scriptsize$\mathfrak{p}$ a prime} \mathfrak{p}$$

이고, 따라서 $a=0$이 되어 모순이다. 

거꾸로 둘째 조건을 가정하고 첫째 조건을 보이자. 즉 $A$의 prime ideal $\mathfrak{p}$를 고정하고, $\mathfrak{p}$를 포함하는 모든 maximal ideal들의 교집합을 $\mathfrak{P}$라 했을 때 $\mathfrak{p}=\mathfrak{P}$임을 보여야 한다. 결론에 반하여 어떠한 원소 $a\in \mathfrak{P}\setminus \mathfrak{p}$가 존재한다 가정하자. 그럼 [\[집합론\] §선택공리, ⁋정리 4](/ko/math/set_theory/axiom_of_choice#thm4)에 의하여, $\mathfrak{p}$를 포함하지만 $a$를 포함하지 않는 prime ideal 중 maximal한 prime ideal $\mathfrak{q}$가 존재한다. 정의에 의해 $a\not\in \mathfrak{q}$이므로 $\mathfrak{q}$는 maximal ideal이 아니고, 따라서 $A/\mathfrak{q}$는 field가 아니다. 그러나 $A[a^{-1}]$에서는 $\mathfrak{q}$가 정의에 의해 maximal ideal이어야 하고, 이는 둘째 조건에 모순이므로 $\mathfrak{p}=\mathfrak{P}$여야 한다. 

</details>

## 영점정리

이제 영점정리는 다음과 같이 서술할 수 있다.

<div class="proposition" markdown="1">

<ins id="thm4">**정리 4**</ins> Jacobson ring $A$와, finitely generated $A$-algebra $E$가 주어졌다 하자. 그럼 $E$도 Jacobson ring이다. 또, 만일 $\mathfrak{n}$이 $E$의 maximal ideal이라면 $\mathfrak{m}=\mathfrak{n}\cap A$는 $A$의 maximal ideal이며, $E/\mathfrak{n}$은 $A/\mathfrak{m}$의 finite field extension이다.

</div>
<details class="proof" markdown="1">
<summary>증명</summary>

세 단계로 나누어 증명한다.

1. 우선 $A=\mathbb{k}$이고 $E=\mathbb{k}[\x]$인 경우를 보자. 그럼 $E$는 principal ideal domain이고, 특히 $E$의 임의의 prime ideal은 irreducible monic polynomial로 생성된다. 이로부터 임의의 prime ideal은 다른 prime ideal에 포함될 수 없다는 것을 알 수 있으므로, $E$의 임의의 prime ideal이 maximal인 것을 알고, 이러한 ideal은 $1\in \mathbb{k}$를 포함할 수 없으므로 $A=\mathbb{k}$와 교집합하였을 때 반드시 $(0)$이 되어야 한다. 이 때, $E/\mathfrak{n}$은 $\mathfrak{n}$을 정의하는 irreducible polynomial의 차수만큼의 차원을 갖는 $\mathbb{k}$-벡터공간이 된다. 마지막으로 $(0)$이 maximal ideal들의 곱이라는 것을 보이기 위해서는, $E=\mathbb{k}[\x]$가 무한히 많은 irreducible polynomial들을 가지고 있고, 다항식의 차수는 반드시 유한이므로 이들 모두를 인수로 갖는 다항식은 $0$뿐이라는 논증을 사용하면 된다. 이 때 $E$에서의 irreducible polynomial의 무한성은 유클리드의 소수의 무한성 증명을 그대로 따라하면 된다.
2. 다음 단계로, 임의의 Jacobson ring $A$와, 하나의 원소로 생성되는 $A$-algebra $E$를 생각하고 $E$가 Jacobson임을 보이기 위해 [보조정리 3](#lem3)의 둘째 조건이 성립함을 보이자. 즉 이번 단계에서 우리의 목표는 다음 명제를 증명하는 것이다.
    > Jacobson ring $A$가 주어졌다 하고, 하나의 원소로 생성되는 $A$-algebra $E$가 주어졌다 하자. 만일 고정된 prime ideal $\mathfrak{q}\subseteq E$에 대하여, $E/\mathfrak{q}$가 영이 아닌 $x\in E/\mathfrak{q}$를 포함하여 $(E/\mathfrak{q})[x^{-1}]$이 field이도록 할 수 있다면, $E/\mathfrak{q}$ 또한 field이다.

    그런데 $E'=E/\mathfrak{q}$ 또한 하나의 원소로 생성되는 $A$-algebra이므로, 위의 명제는 다음 명제를 보이는 것과 동일한 것이다.
    > Jacobson ring $A$가 주어졌다 하고, 하나의 원소로 생성되는 $A$-algebra $E'$가 integral domain이라 하자. 만일 $E'$가 영이 아닌 $x\in E'$를 포함하여 $E'[x^{-1}]$이 field이도록 할 수 있다면, $E'$ 또한 field이다.

    이렇게 quotient를 취하는 과정에서, $A$는 $A'=A/(A\cap \mathfrak{q})$로 바뀌게 되며 이 또한 Jacobson ring이므로, 결과적으로 우리가 보여야 하는 것은 다음 명제이다.
    > Integral domain $A'$가 Jacobson이라 하고, 하나의 원소로 생성되는 $A'$-algebra $E'$가 integral domain이며 $A'$를 포함한다 하자. 만일 $E'$가 영이 아닌 $x\in E'$를 포함하여 $E'[x^{-1}]$이 field이도록 할 수 있다면, $E'$ 또한 field이다.

    이를 위해 우리는 위의 가정 하에서 $A'$가 field가 되어야 하고, $E'$는 $A$의 유한한 extension이 됨을 보인다. 위의 명제에서 $E'$는 하나의 원소로 생성되는 $A'$-algebra이므로, $E'=A'[\x]/\mathfrak{q}$라 쓸 수 있다. 우선 $\mathfrak{q}\neq 0$임을 보이자. 결론에 반하여 $\mathfrak{q}=0$이라 하고, 적당한 $x\in E'/(0)=A'[\x]$가 존재하여 $E'[x^{-1}]=A'[\x][x^{-1}]$이 field라 가정하자. $K'=\Frac(A')$라 하면, 이 가정에 의해 $K'[\x][x^{-1}]$ 또한 field이다. 그런데 $K'[\x]$는 첫째 결과에 의해 Jacobson이므로 $K'[\x]$가 field가 되어야 하고 이는 모순이다. 따라서 $\mathfrak{q}\neq 0$이어야 하고, $E'[x^{-1}]=K'[\x]/\mathfrak{q}K'[\x]$는 $K'$의 finite dimensional extension이다.  
    이제 $p(x)\in \mathfrak{q}$가 $E'$에서 다음의 식

    $$p(\alpha)=p_n\alpha^n+\cdots+p_0=0$$

    을 만족한다 하자. 여기에서 $\alpha$는 $E'$의 $A'$-algebra로서의 generator이다. 그럼 위의 식으로부터 $E'[p_n^{-1}]$은 integral $A'[p_n^{-1}]$-algebra이다. 한편, 위에서 정의한 $x$ 또한 적당한 다항식

    $$q(x)=q_mx^m+\cdots+q_0=0$$

    을 만족해야 하며, $E'$가 integral domain이므로 우리는 일반성을 잃지 않고 $q_0\neq 0$이라 가정할 수 있다. 그럼 이제 monic polynomial

    $$\left(\frac{1}{x}\right)^m+\frac{q_1}{1_0}\left(\frac{1}{x}\right)^{m-1}+\cdots+\frac{q_m}{q_0}=0$$

    으로부터 $E'[x^{-1}]$이 integral $A'[(p_nq_0)^{-1}]$-algebra임을 안다. 이제 [§정수적 확장과 아이디얼, ⁋따름정리 3](/ko/math/commutative_algebra/lying_over_and_going_up#cor3)으로부터 $A'[(p_nq_0)^{-1}]$는 field이고, 가정에 의해 $A'$는 Jacobson이므로 [보조정리 3](#lem3)에 의해 $A'$는 field이다. 따라서 $E'$는 integral $A'$-algebra이고 다시 [§정수적 확장과 아이디얼, ⁋따름정리 3](/ko/math/commutative_algebra/lying_over_and_going_up#cor3)으로부터 $E'$가 field임을 안다. 
3. 이제 마지막 경우는 둘째 결과를 사용해 induction을 진행하면 된다. 

</details>

특별히 $A=\mathbb{k}$이고 $E=\mathbb{k}[\x_1,\ldots, \x_n]$인 경우를 생각하자. 그럼 임의의 

$$a=(a_1,\ldots, a_n)\in \mathbb{k}^n$$

에 대하여, ideal $\mathfrak{m}_a$를 다음의 식

$$\mathfrak{m}_a=(\x_1-a_1,\ldots, \x_n-a_n)$$

으로 정의하면 evaluation으로 주어지는 isomorphism

$$\ev_a:\mathbb{k}[\x_1,\ldots, \x_n]/\mathfrak{m}_a\rightarrow \mathbb{k}$$

로부터 $\mathfrak{m}_a$가 maximal ideal인 것을 안다. 

뿐만 아니라, 만일 $\mathbb{k}$가 algebraically closed field라면 $E$의 모든 maximal ideal은 이러한 꼴이다. 우선 $E$의 임의의 maximal ideal $\mathfrak{n}$에 대하여, $E/\mathfrak{n}$은 $\mathbb{k}/(\mathfrak{n}\cap \mathbb{k})=\mathbb{k}$에 대해 algebraic extension인데, $\mathbb{k}$가 algebraically closed라면 이러한 extension은 자기자신밖에 없고, 따라서 $E/\mathfrak{n}\cong \mathbb{k}$여야 한다. 한편 canonical surjection $E \rightarrow E/\mathfrak{n}\cong \mathbb{k}$을 통해 각각의 $\x_i$가 옮겨지는 $\mathbb{k}$의 원소를 $a_i$라 하면, $\mathfrak{m}_a\subseteq \mathfrak{n}$이고 이제 $\mathfrak{m}_a$의 maximality로부터 원하는 결과를 얻는다. 

따라서 [§기본 개념들, ⁋명제 11](/ko/math/commutative_algebra/basic_notions#prop11)로부터 다음을 얻는다.

<div class="proposition" markdown="1">

<ins id="lem5">**보조정리 5**</ins> Field $\mathbb{k}$가 주어졌다 하자. 그럼 $\mathfrak{m}_a=(\x_1-a_1,\ldots, \x_n-a_n)$은 $\mathbb{k}[\x_1,\ldots, \x_n]$의 maximal ideal이다. 또, 만일 $\mathbb{k}$가 algebraically closed라면 $\mathbb{k}[\x_1,\ldots,\x_n]/(f_1,\ldots, f_r)$의 maximal ideal들과, 다음 식

$$f_1(x_1,\ldots, x_n)=\cdots=f_r(x_1,\ldots, x_n)=0$$

을 만족하는 $(x_1,\ldots, x_n)$들 사이의 일대일 대응이 존재한다. 

</div>

조금 더 전통적인 버전의 영점정리 또한 이로부터 얻어진다. 이를 서술하기 위해, $\mathbb{k}[\x_1,\ldots, \x_n]$의 ideal $\mathfrak{a}$을 받아 $\mathbb{k}^n$의 부분집합 $Z(\mathfrak{a})$를 내놓는 함수

$$Z(\mathfrak{a})=\{(a_1,\ldots, a_n)\in \mathbb{k}^n: \text{$f(a_1,\ldots, a_n)=0$ for all $f\in \mathfrak{a}$}\}$$

그리고 $\mathbb{k}^n$의 부분집합 $S$를 받아 $\mathbb{k}[\x_1,\ldots, \x_n]$의 부분집합

$$I(S)=\{f\in \mathbb{k}[\x_1,\ldots, \x_n]:\text{$f(a_1,\ldots, a_n)=0$ for all $(a_1,\ldots, a_n)\in S$}\}$$

을 내놓는 함수 $I$를 생각하자. 

<div class="proposition" markdown="1">

<ins id="prop6">**명제 6**</ins> Algebraically closed field $\mathbb{k}$와 ideal $\mathfrak{a}\subseteq \mathbb{k}[\x_1,\ldots, \x_n]$이 주어졌다 하자. 그럼 

$$I(Z(\mathfrak{a}))=\sqrt{\mathfrak{a}}$$

이 성립한다.

</div>
<details class="proof" markdown="1">
<summary>증명</summary>

[보조정리 5](#lem5)로부터, $Z(\mathfrak{a})$의 원소들이 $\mathbb{k}[\x_1,\ldots, \x_n]$의 maximal ideal들 중 $\mathfrak{a}$를 포함하는 것들에 일대일로 대응됨을 안다. 따라서 $I(Z(\mathfrak{a}))$는 $\mathfrak{a}$를 포함하는 $\mathbb{k}[\x_1,\ldots, \x_n]$의 maximal ideal들의 교집합이며, [정리 4](#thm4)에 의해 $\mathbb{k}[\x_1,\ldots, \x_n]$은 Jacobson이므로 이는 $\mathfrak{a}$를 포함하는 $\mathbb{k}[\x_1,\ldots, \x_n]$의 prime ideal들의 교집합과 같고 이것이 정확히 우변이다. 

</details>

---

**참고문헌**

**[Eis]** David Eisenbud. *Commutative Algebra: with a view toward algebraic geometry*. Springer, 1995.

---