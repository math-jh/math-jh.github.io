---

title: "분수체"
excerpt: "Localization, ring of fraction, prime ideal"

categories: [Math / Algebraic Structures]
permalink: /ko/math/algebraic_structures/field_of_fractions
header:
    overlay_image: /assets/images/Math/Algebraic_Structures/Field_of_fractions.png
    overlay_filter: 0.5
sidebar: 
    nav: "algebraic_structures-ko"

date: 2024-05-08
last_modified_at: 2024-05-08
weight: 105

---

## 분수환

[\[집합론\] §자연수와 무한집합](/ko/math/set_theory/natural_numbers)에서 정의한 자연수들의 monoid $\mathbb{N}$은 (약간의 기술적인 문제를 제외하면) 집합론의 언어로 쓰여질 수 있었다. 그리고 $\mathbb{Z}$는 commutative monoid $\mathbb{N}$의 Grothendieck group으로 정의되었다. 중학교 때 배우는 수체계를 생각해보면 이 다음 정의해야 할 대상은 유리수 집합 $\mathbb{Q}$이다. 

$\mathbb{Z}$의 덧셈구조를 잊어버리고, 곱셈구조만 기억한다면 $(\mathbb{Z},\cdot,1)$은 commutative monoid이다. 우리가 해야 할 일은 역수들을 추가하는 것이고, $1/0$은 정의되지 않으므로 $S=\mathbb{Z}\setminus\\{0\\}$으로 두고 ([§Grothendieck 군, ⁋정의 7](/ko/math/algebraic_structures/Grothendieck_groups#def7))의 monoid of fractions을 생각하면 multiplicative group $\mathbb{Q}$를 얻게 된다. 

일반적으로 이 과정은 다음 정리를 통해 가능하다.

<div class="proposition" markdown="1">

<ins id="thm1">**정리 1**</ins> Commutative ring $A$와 $A$의 부분집합 $S$를 생각하자. $A$를 multiplicative monoid로 보고, monoid of fractions $A_S$를 생각하자. 그럼 canonical morphism $\epsilon:A \rightarrow A_S$에 대하여, 다음 두 조건을 만족하는 유일한 덧셈구조가 존재한다.

1. $A_S$ 위의 곱셈구조와, 이 덧셈구조는 $A_S$를 commutative ring으로 만든다.
2. $\epsilon$이 ring homomorphism이다.

</div>
<details class="proof" markdown="1">
<summary>증명</summary>

증명을 시작하기에 앞서 [§Grothendieck 군, ⁋정의 7](/ko/math/algebraic_structures/Grothendieck_groups#def7)의 construction을 잠깐 리뷰하자. 우리는 $S$에 의해 생성된 $A$의 submonoid $S'$를 생각하고, monoid $A\times S'$에 동치관계 $R$을

$$(\alpha,\gamma)\equiv (\beta,\delta)\pmod{R}\iff \alpha\delta\zeta=\beta\gamma\zeta\text{ for some $\zeta\in S'$}$$

로 정의하여, quotient monoid $(A\times S')/R$을 $A_S$로 정의하였다. 이 때 $(\alpha,\gamma)\in A\times S'$를 representative로 갖는 $A_S$의 원소를 $\alpha/\gamma$로 표기하였으며, 그럼 $A_S$는 여전히 다음 연산

$$\frac{\alpha}{\gamma}\frac{\beta}{\delta}=\frac{\alpha\beta}{\gamma\delta}$$

을 통해 multiplicative monoid 구조가 된다. 두 multiplicative monoid 사이의 canonical morphism $\epsilon:A \rightarrow A_S$은 $\alpha\mapsto \alpha/1$로 정의되었었는데, 이것이 monoid homomorphism이라는 것은 $\epsilon$이 ($A_S$가 ring이라는 것을 보이고 나면) $A$에서 $A_S$로 가는, 곱셈구조를 보존하는 함수라는 뜻이다.

즉, 우리가 해야 할 것은 $A_S$ 위에 정리의 두 조건을 만족하는 덧셈구조를 부여하고, 이렇게 정의된 덧셈 구조가 $A_S$를 ring으로 만드는 것, 그리고 $\epsilon$이 실제로 이 덧셈구조까지 보존한다는 것이다.

우선 이러한 덧셈구조가 존재한다 가정하고 유일성을 보이자. 임의의 $x,y\in A_S$는 적당한 $\alpha,\beta\in A$와 $\gamma,\delta\in S'$에 대하여 $x=\alpha/\gamma,y=\beta/\delta$라 적을 수 있다. 그럼

$$x=\epsilon(\alpha)\epsilon(\gamma)^{-1}=\epsilon(\alpha\delta)\epsilon(\gamma\delta)^{-1},\qquad y=\epsilon(\beta)\epsilon(\delta)^{-1}=\epsilon(\beta\gamma)\epsilon(\gamma\delta)^{-1}$$

으로 적을 수 있고 따라서

$$x+y=(\epsilon(\alpha\delta)+\epsilon(\beta\gamma))\epsilon(\gamma\delta)^{-1}=\frac{\alpha\delta+\beta\gamma}{\gamma\delta}$$

여야만 한다. 

이제 유일성 증명에서 힌트를 얻어 $A_S$의 덧셈구조를 위의 식으로 정의한다. 그럼 보여야 할 것들은 다음과 같다.


1. 이 정의는 $\alpha,\beta,\gamma,\delta$의 선택에 무관하다. 즉 $x=\alpha'/\gamma',y=\beta'/\delta'$의 꼴로 쓰였다 하자. 다음 식

    $$(\alpha\delta+\beta\gamma)/\delta\gamma=(\alpha'\delta'+\beta'\gamma')/\gamma'\delta'$$

    이 $A_S$에서 성립하는 것을 보여야 한다. 그런데 $\alpha/\gamma=\alpha'/\gamma',\beta/\delta=\beta'/\delta'$이므로, 정의에 의해 $ap's=a'ps,bq't=b'qt$를 만족하는 $\zeta,\xi\in S'$가 존재한다. 이로부터 

    $$(\alpha\delta+\beta\gamma)(\gamma'\delta')(\zeta\xi)=(\alpha'\delta'+\beta'\gamma')(\gamma\delta)(\zeta\xi)$$

    을 확인할 수 있으므로 원하는 식이 성립한다.

2. 이렇게 정의한 $+$는 결합법칙을 만족한다. 임의의 $x_1=\alpha_1/\gamma_1,x_2=\alpha_2/\gamma_2,x_3=\alpha_3/\gamma_3$에 대하여,

    $$(x_1+x_2)+x_3=\frac{\alpha_1\gamma_2+\alpha_2\gamma_1}{\gamma_1\gamma_2}+\frac{\alpha_3}{\gamma_3}=\frac{(\alpha_1\gamma_2+\alpha_2\gamma_1)\gamma_3+\alpha_3(\gamma_1\gamma_2)}{\gamma_1\gamma_2\gamma_3}=\frac{\alpha_1\gamma_2\gamma_3+\gamma_1\alpha_2\gamma_3+\gamma_1\gamma_2\alpha_3}{\gamma_1\gamma_2\gamma_3}$$

    이고 비슷하게 $x_1+(x_2+x_3)$도 우변의 값을 갖는다는 것을 확인할 수 있다.
3. $+$의 교환법칙은 $A$의 덧셈과 곱셈이 commutative하기 때문에 자명하다.
4. $+$는 덧셈에 대한 항등원 $0/1$을 갖는다. 이는 임의의 $x=\alpha/\gamma\in A_S$에 대하여,

    $$\frac{0}{1}+\frac{\alpha}{\gamma}=\frac{\alpha}{\gamma}$$

    이 성립하기 때문이다.
5. $+$에 대한 역원이 항상 존재한다. 임의의 $x\in \alpha/\gamma\in A_S$에 대하여, $(-\alpha)/\gamma$가 다음 식

    $$\frac{-\alpha}{\gamma}+\frac{\alpha}{\gamma}=\frac{(-\alpha)\gamma+\alpha\gamma}{\gamma^2}=0$$

    을 만족하기 때문이다.
6. $+$는 곱셈에 대해 분배법칙을 만족한다. 임의의 $x=\alpha/\gamma,y_1=\beta_1/\delta_1,y_2=\beta_2/\delta_2$에 대하여,

    $$x(y_1+y_2)=\frac{\alpha}{\gamma}\left(\frac{\beta_1}{\delta_1}+\frac{\beta_2}{\delta_2}\right)=\frac{\alpha}{\gamma}\frac{\beta_1\delta_2+\delta_1\beta_2}{\delta_1\delta_2}=\frac{\alpha\beta_1\delta_2+\alpha\delta_1\beta_2}{\gamma\delta_1\delta_2}$$

    이고

    $$xy_1+xy_2=\frac{\alpha\beta_1}{\gamma\delta_1}+\frac{\alpha\beta_2}{\gamma\delta_2}=\frac{\alpha\beta_1\gamma\delta_2+\alpha\beta_2\gamma\delta_1}{\gamma^2\delta_1\delta_2}$$

    이며, $1,\gamma\in S'$를 사용해 이 두 식이 같은 값임을 확인할 수 있다. 비슷하게 등식$(x_1+x_2)y=x_1y+x_2y$도 보일 수 있다.

이상에서 $A_S$가 commutative ring 구조를 갖는다는 것을 안다. 마지막으로 $\epsilon$이 ring homomorphism이라는 것은 $\epsilon$이 덧셈을 보존한다는 것만 보이면 충분하고, 이는

$$\epsilon(\alpha+\beta)=(\alpha+\beta)/1=\alpha/1+\beta/1=\epsilon(\alpha)+\epsilon(\beta)$$

으로부터 알 수 있다.  

</details>

<div class="definition" markdown="1">

<ins id="def2">**정의 2**</ins> 위와 같이 얻어진 ring을 $S$에 의해 정의되는 $A$의 *ring of fractions<sub>분수환</sub>*이라 부르고, 이를 $S^{-1}A$로 표기한다.

</div>

만일 $S$가 $A$의 cancellable element들의 모임이었다 하면 $\epsilon$이 injection이 되는 것이 자명하고, 따라서 $A$를 $S^{-1}A$의 subring으로 생각할 수 있다. 이 때 $S^{-1}A$를 $A$의 *total ring of fractions*라 부른다.

## 체

유리수 $\mathbb{Q}$는 일반적인 ring과 구분되는 다음과 같은 특징을 갖는다.

<div class="definition" markdown="1">

<ins id="def3">**정의 3**</ins> Ring $A$가 *division ring<sub>나눗셈환</sub>*이라는 것은 $A\neq0$이고, $A$의 임의의 영이 아닌 원소가 모두 곱셈에 대한 역원을 갖는 것이다. Commutative division ring을 *field<sub>체</sub>*라 부른다.

</div>

<div class="proposition" markdown="1">

<ins id="prop4">**명제 4**</ins> Ring $A\neq 0$이 division ring인 것과, $A$의 left ideal이 $0$과 $A$ 뿐인 것이 동치이다.

</div>
<details class="proof" markdown="1">
<summary>증명</summary>

우선 $A$가 division ring이라 하자. 만일 left ideal $\mathfrak{a}\neq 0$가 주어졌다면 $0\neq x\in \mathfrak{a}$가 존재한다. 그런데 $A$에서는 $x$의 역원 $x^{-1}$이 존재하므로, 

$$1=x^{-1}x\in A\mathfrak{a}=\mathfrak{a}$$

이고 따라서 $\mathfrak{a}=A$이다. 거꾸로 $A$의 left ideal이 $0$과 $A$ 뿐이라 하자. 임의의 $0\neq x\in A$에 대하여, $A$의 left ideal $Ax$를 생각하면 $0\neq x\in Ax$이므로 $Ax\neq 0$이다. 이제 $A$의 left ideal은 $0$ 혹은 $A$ 뿐이므로 반드시 $Ax=A$이고, 따라서 $1\in Ax$이다. 즉, 적당한 $\alpha\in A$가 존재하여 $\alpha x=1$이도록 할 수 있다. 그럼 $\alpha\neq 0$이고, 마찬가지 논리에 의하여 적당한 $\beta\in A$가 존재하여 $\beta\alpha=1$이도록 할 수 있다. 이제

$$\beta=\beta1=\beta\alpha x=x$$

로부터 $\beta=x$임을 알 수 있고, 따라서 $\alpha$는 $x$의 곱셈에 대한 역원이다. 

</details>

## 정역

$\mathbb{Q}$는 그 정의에 의하여 $\mathbb{Z}$의 total ring of fraction이다. 이것이 field가 되는 것은 졍의에 의해 자명하며, 이는 다음과 같이 확장할 수 있다. 

<div class="definition" markdown="1">

<ins id="def5">**정의 5**</ins> Ring $A$의 원소 $\alpha,\beta$가 $\alpha\beta=0$이지만 $\alpha\neq 0$이고 $\beta\neq 0$일 경우, $\alpha,\beta$를 *zerodivisor<sub>영인자</sub>*라 부른다. Ring $A$가 *integral domain<sub>정역</sub>*이라는 것은 $A$가 commutative이고, $0\neq 1$이며, $A$가 zerodivisor를 갖지 않는 것이다.

</div>

정의에 의해 integral domain의 subring은 integral domain임이 자명하다. 임의의 nonzero ring $A,B$에 대하여, $A\times B$는 다음 식

$$(1,0)(0,1)=(0,0)$$

으로부터 항상 integral domain이 될 수 없다. 

<div class="proposition" markdown="1">

<ins id="prop6">**명제 6**</ins> Integral domain $A$의 total ring of fraction는 field이다.

</div>
<details class="proof" markdown="1">
<summary>증명</summary>

$A$가 integral domain이라는 가정으로부터, $S=A\setminus\\{0\\}$임을 안다. 즉, $S^{-1}A$의 임의의 원소는 $\alpha\in A$, $\beta\in A\setminus\\{0\\}$에 대하여 $\alpha/\beta$의 꼴로 나타낼 수 있다. 여기에서 $\alpha/\beta\neq 0$이기 위해서는 $\alpha\neq 0$이므로, $\beta/\alpha\in K$도 잘 정의되고 그럼 $\beta/\alpha$가 $\alpha/\beta$의 역원이 된다.

</details>

<div class="definition" markdown="1">

<ins id="def7">**정의 7**</ins> 위의 [명제 6](#prop6)으로부터 얻어지는 field $S^{-1}A$를 $A$의 *field of fractions<sub>분수체</sub>*이라 부르고, $\Frac(A)$로 나타낸다.

</div>

## 소아이디얼

Ring homomorphism의 fourth isomorphism theorem으로부터, 임의의 ring $A\neq 0$과 maximal left ideal $\mathfrak{m}$에 대하여 $A/\mathfrak{m}$의 유일한 left ideal은 $0$과 $A/\mathfrak{m}$ 자기 자신 뿐임을 안다. 따라서 [명제 4](#prop4)에 의하여 $A/\mathfrak{m}$은 division ring이다. Integral domain 또한 비슷한 식으로 특징지을 수 있다.

<div class="proposition" markdown="1">

<ins id="prop8">**명제 8**</ins> Commutative ring $A$와 ideal $\mathfrak{p}\neq A$에 대하여 다음이 모두 동치이다.

1. $A/\mathfrak{p}$가 integral domain이다.
2. 만일 $\alpha,\beta\in A\setminus \mathfrak{p}$라면 $\alpha\beta\in A\setminus \mathfrak{p}$이다.
3. 만일 $\alpha\beta\in \mathfrak{p}$라면, $\alpha\in \mathfrak{p}$이거나 $\beta\in \mathfrak{p}$이다.

</div>
<details class="proof" markdown="1">
<summary>증명</summary>

2번과 3번 조건은 서로 대우명제이므로, 1번과의 동치만 보이면 충분하다. 우선 $A/\mathfrak{p}$가 integral domain이라 가정하자. 즉

$$(\alpha+\mathfrak{p})(\beta+\mathfrak{p})=0+\mathfrak{p}$$

라면, 반드시 $\alpha+\mathfrak{p}=0+\mathfrak{p}$이거나 $\beta+\mathfrak{p}=0+\mathfrak{p}$이다. 이로부터 1번 조건이 성립하면 3번 조건이 성립하는 것을 안다. 이 논증은 반대방향으로도 성립한다.

</details>

위의 동치조건을 만족하는 ideal $\mathfrak{p}$를 *prime ideal<sub>소아이디얼</sub>*이라 부른다. 모든 field는 integral domain이므로, 모든 maximal ideal은 prime ideal이다. 그 역은 성립하지 않는데, 가령 $\mathbb{Z}$의 prime ideal은 $(0)$과, 소수 $p$에 대해 $p\mathbb{Z}$ 꼴 뿐이라는 것을 쉽게 확인할 수 있다. 그럼 $(0)$은 prime ideal이지만 maximal ideal은 아니다.

한편 다음이 성립한다.

<div class="proposition" markdown="1">

<ins id="prop9">**명제 9**</ins> Commutative ring $A,B$ 사이의 ring homomorphism $\phi:A \rightarrow B$와 $B$의 prime ideal $\mathfrak{p}$에 대하여, $\phi^{-1}(\mathfrak{p})$는 $A$의 prime ideal이다.

</div>
<details class="proof" markdown="1">
<summary>증명</summary>

결론에 반하여 $\alpha\beta\in\phi^{-1}(\mathfrak{p})$이지만 $\alpha,\beta\not\in\phi^{-1}(\mathfrak{p})$인 $\alpha,\beta\in A$가 존재한다 하면, $\phi(\alpha)\phi(\beta)=\phi(\alpha\beta)\in \mathfrak{p}$이지만 $\phi(\alpha),\phi(\beta)\not\in \mathfrak{p}$가 되어 [명제 8](#prop8)의 동치에 모순이다. 

</details>

한편, [명제 8](#prop8)의 2번 동치에 의하여, commutative ring $A$를 $A$를 multiplicative monoid로 본다면, 그 prime ideal $\mathfrak{p}$에 대해 $A\setminus\mathfrak{p}$는 $A$의 submonoid로 볼 수 있다. 따라서 ring of fractions $(A\setminus \mathfrak{p})^{-1}A$가 잘 정의되며, 이 ring의 분모에 들어가는 것은 오직 $A\setminus \mathfrak{p}$의 원소들 뿐이다. 이를 다음과 같이 정의한다.

<div class="definition" markdown="1">

<ins id="def10">**정의 10**</ins> Commutative ring $A$와 prime ideal $\mathfrak{p}$에 대하여, $A$의 $\mathfrak{p}$에서의 *localization<sub>국소화</sub>*을 $(A\setminus \mathfrak{p})^{-1}A$로 정의하고, 이를 간단히 $A_\mathfrak{p}$로 적는다.

</div>

## 멱영원

<div class="definition" markdown="1">

<ins id="def11">**정의 11**</ins> Ring $A$의 원소 $\alpha$가 *nilpotent<sub>멱영</sub>*이라는 것은 적당한 $n>0$이 존재하여 $\alpha^n=0$이 성립하는 것이다. 만일 $A$가 영이 아닌 nilpotent element를 갖지 않으면 $A$를 *reduced<sub>기약</sub>*라 부른다.

</div>

정의에 의하여, 영이 아닌 nilpotent element는 zero-divisor이다. 따라서 모든 integral domain은 (commutative) reduced ring이다. 뿐만 아니라, commutative ring으로 한정하면 다음을 얻는다.

<div class="proposition" markdown="1">

<ins id="prop12">**명제 12**</ins> Commutative ring $A$에 대하여, nilpotent element들의 모임 $\mathfrak{N}$은 ideal이 된다.

</div>
<details class="proof" markdown="1">
<summary>증명</summary>

만일 $x\in \mathfrak{N}$이라면 $x^n=0$이도록 하는 $n>0$이 존재할 것이고, 임의의 $\alpha\in A$에 대하여 $(\alphax)^n=\alpha^nx^n=0$이 되어 $\alpha x\in \mathfrak{N}$임을 보일 수 있다. 

이제 $\mathfrak{N}$이 덧셈에 대해 닫혀있다는 것을 보여야 한다. 임의의 $x,y\in \mathfrak{N}$이 주어졌다 하고, 적당한 $m,n>0$에 대하여 $x^m=0$이고 $y^n=0$이라 하자. 그럼

$$(x+y)^{m+n}=x^{m+n}+\binom{m+n}{1}x^{m+n-1}y+\cdots+\binom{m+n}{n}x^my^n+\binom{m+n}{n+1}x^{m-1}y^{n+1}+\cdots+y^n$$

이고, 우변의 모든 항들이 $0$임을 알 수 있다. 이상에서 $x+y\in \mathfrak{N}$이다.

</details>

<div class="definition" markdown="1">

<ins id="def13">**정의 13**</ins> [명제 12](#prop12)의 ideal $\mathfrak{N}$을 $A$의 *nilradical*이라 부른다.

</div>

정의에 의하여 $A$가 reduced인 것은 $A$의 nilradical이 $0$인 것과 동치이다. 한편, 만일 $x\in \mathfrak{N}$이라면, 식 $x^n=0$과 prime ideal의 정의로부터 $x\in \mathfrak{p}$이 모든 prime ideal $\mathfrak{p}$에 대해 성립하는 것을 안다. 즉 다음 포함관계

$$\mathfrak{N}\subseteq\bigcap_\text{\scriptsize$\mathfrak{p}$: prime} \mathfrak{p}$$

이 성립한다.

<div class="proposition" markdown="1">

<ins id="prop14">**명제 14**</ins> Commutative ring $A$와 nilradical $\mathfrak{N}$에 대하여, 

$$\mathfrak{N}=\bigcap_\text{\scriptsize$\mathfrak{p}$: prime} \mathfrak{p}$$

이 성립한다. 

</div>
<details class="proof" markdown="1">
<summary>증명</summary>

만일 $x\not\in \mathfrak{N}$이라면, 적당한 $\mathfrak{p}$에 대해 $x\not\in \mathfrak{p}$임을 보이면 충분하다. 우선 multiplicative subset $S=\\{1,x,x^2,\ldots\\}$으로 만들어진 ring of fractions $A_x=S^{-1}A$를 생각하자. 그럼 $A_x$의 곱셈에 대한 항등원 $x/x$이 반드시 $0/1$과 다르다는 것을 확인할 수 있고, 특히 $A_x\neq 0$이다. 이제 [§환의 정의, ⁋정리 9](/ko/math/algebraic_structures/rings#thm9)로부터 $A_x$의 maximal ideal $\mathfrak{m}$이 반드시 존재하고, 모든 maximal ideal은 prime ideal이므로 $A_x$는 prime ideal을 갖는다. 이제 [명제 9](#prop9)를 $\epsilon:A \rightarrow A_x$에 적용하면 $\epsilon^{-1}(\mathfrak{p})$는 $A$의 prime ideal이며, 만일 $x\in\epsilon^{-1}(\mathfrak{p})$라면 $x/1\in \mathfrak{p}$이고 $x/1$은 $A_x$에서 invertible이므로 $\mathfrak{p}=A_x$가 되어 모순이다. 

</details>


---

**참고문헌**

**[Bou]** Bourbaki, N. Algebra I. *Elements of Mathematics*. Springer. 1998.  

---