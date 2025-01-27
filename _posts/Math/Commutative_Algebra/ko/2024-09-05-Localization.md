---

title: "국소화"
excerpt: ""

categories: [Math / Commutative Algebra]
permalink: /ko/math/commutative_algebra/localization
header:
    overlay_image: /assets/images/Math/Commutative_Algebra/Localization.png
    overlay_filter: 0.5
sidebar: 
    nav: "commutative_algebra-ko"

date: 2024-09-05
last_modified_at: 2024-10-16
weight: 2

---

## 국소환

이번 글에서 우리는 localization을 정의한다. 간단히 이야기해서 localization은 ring $A$를 local ring으로 만드는 과정이라 생각할 수 있다.

<div class="definition" markdown="1">

<ins id="def1">**정의 1**</ins> Ring $A$가 *local ring<sub>국소환</sub>*이라는 것은 $A$가 유일한 maximal ideal을 갖는 것이다.

</div>

그럼 다음 동치관계를 보일 수 있다.

<div class="proposition" markdown="1">

<ins id="prop2">**명제 2**</ins> Ring $A$에 대하여, 다음이 동치이다.

1. $A$가 local ring이다. 
2. $A$의 임의의 non-unit은 모두 $A$의 어떠한 ideal $\mathfrak{m}\subsetneq A$에 속한다.
3. $A$의 모든 non-unit을 모아둔 것이 ideal을 이룬다.

</div>
<details class="proof" markdown="1">
<summary>증명</summary>

우선 1번을 가정하고, $A$의 임의의 non-unit $a\in A$가 주어졌다 하자. 그럼 $(a)$는 $A$의 ideal이므로 [\[대수적 구조\] §환의 정의, ⁋정리 9](/ko/math/algebraic_structures/rings#thm9)에 의하여 어떠한 maximal ideal에 포함된다. 그런데 $A$는 유일한 maximal ideal $\mathfrak{m}$을 가지므로, $(a)\subseteq \mathfrak{m}$일 수밖에 없고, 따라서 $a\in \mathfrak{m}$이다.

이제 2번을 가정하고 3번을 보이자. 이를 위해서는 $A$의 non-unit들을 모아둔 것이 덧셈에 대해 닫혀있음만 보이면 충분하다. 우선 $\mathfrak{m}\neq A$인 것으로부터 $\mathfrak{m}$은 $A$의 unit을 포함하지 않음을 안다. 이로부터 $A$의 non-unit을 모두 모아두면 반드시 이것이 $\mathfrak{m}$과 같아야 함을 안다. 

마지막으로 3번 조건을 가정하고 1번 조건을 보여야 한다. 임의의 ideal $\mathfrak{a}\subsetneq A$에 대하여, 앞선 관찰로부터 $\mathfrak{a}$는 non-unit들로만 이루어져 있다는 것을 알고, 따라서 $\mathfrak{a}$는 $A$의 모든 non-unit들을 모아둔 ideal $\mathfrak{m}$에 속한다. 한편 $\mathfrak{m}$은 maximal ideal인데, 이는 $A\setminus \mathfrak{m}$의 임의의 원소는 $A$의 unit이므로, $\mathfrak{m}$을 포함하는 ideal은 $A$ 뿐이기 때문이다.

</details>

## 가군의 국소화

앞선 글에서 설명한 것과 마찬가지로, ring의 localization을 보기 위해 우리는 더 일반적으로 module의 localization을 정의한다. 

<div class="definition" markdown="1">

<ins id="def3">**정의 3**</ins> Ring $A$의 부분집합 $S$가 *multiplicatively closed<sub>곱셈에 대하여 닫혀있다</sub>*인 것은 $U$의 원소들의 임의의 곱이 다시 $S$에 속하는 것이다. 

</div>

특히 $1$은 공집합으로 index가 주어진 family의 곱으로 생각할 수 있으므로 정의에 의해 $1\in S$이다. 

<div class="definition" markdown="1">

<ins id="def4">**정의 4**</ins> Ring $A$와 $A$-module $M$, 그리고 $A$의 multiplicative subset $S$에 대하여, $S$에서의 $M$의 *localization<sub>국소화</sub>*는 다음과 같이 정의되는 $A$-module $S^{-1}M$이다. 

1. 집합으로서 $S^{-1}M$은 $M\times S$ 위에 다음과 같은 equivalence relation
    
    $$(x,s)\sim (x',s')\iff \text{there exists $t\in S$ such that $t(s'x-sx')=0$}$$
  
    을 정의하여 얻어지는 quotient set이다. 이 때 $(x,s)$의 representative를 $x/s$로 표기한다.
2. $S^{-1}M$의 $A$-module 구조는 다음과 같이 정의된다.
  
  $$\frac{x}{s}+\frac{x'}{s'}=\frac{s'x+sx'}{ss'},\qquad a\cdot \frac{x}{s}=\frac{ax}{s}.$$

</div>

2번 조건에서 정의한 연산들이 실제로 $A$-module 구조를 준다는 것을 확인해야 하지만 이는 어렵지 않다. 대신 몇 가지 관찰을 추가한다. 우선 임의의 $t\in S$와 $x/s\in S^{-1}M$에 대하여, 

$$\frac{tx}{ts}=\frac{x}{s}$$

가 성립한다. 이는 그냥 $1(txs-tsx)=0$이기 때문이다. 또, $S^{-1}M$에서의 덧셈에 대한 항등원과 역원 또한 살펴볼 수 있는데, 우선 임의의 $s,s'\in S$에 대하여

$$\frac{0}{s}=\frac{0}{s'}$$

임을 확인할 수 있으며, 다음 식

$$\frac{0}{s'}+\frac{x}{s}=\frac{x}{s}+\frac{0}{s'}=\frac{0s+s'x}{ss'}=\frac{s'x}{s's}=\frac{x}{s}$$

으로부터 이것이 $S^{-1}M$에서의 덧셈에 대한 항등원임을 알 수 있다. 비슷한 계산으로 임의의 $x/s$의 역원은 $(-x)/s$임을 확인할 수 있다. 

위의 계산들은 중학교 때부터 해오던 분수의 덧셈 및 곱셈과 다른 것이 없다. 이를 직관삼아 $M$에서 $S^{-1}M$으로의 canonical map $\epsilon: M \rightarrow S^{-1}M$을 $x\mapsto x/1$으로 정의할 수 있다. 아쉽게도 $\epsilon$은 일반적인 경우에는 inclusion이 되지 않을 수 있는데, 그 이유는 생각해보면 자명하며, 다음 명제에 녹아있다.

<div class="proposition" markdown="1">

<ins id="prop5">**명제 5**</ins> 위와 같은 상황에서, $\epsilon(x)=0$인 것과, 적당한 $s\in S$가 존재하여 $sx=0$인 것이 동치이다. 특히 만일 $M$이 finitely generated이면 $S^{-1}M=0$인 것과 $M$이 $S$에 의해 annihilate되는 것이 동치이다.

</div>
<details class="proof" markdown="1">
<summary>증명</summary>

만일 

$$\epsilon(x)=x/1=0=0/1$$

이라면, 적당한 $s\in S$가 존재하여 

$$s(1x-0\cdot1)=sx=0$$

이 성립한다. 위의 논리는 반대방향으로도 성립한다.

</details>

## 환의 국소화

Localization의 가장 단순한 예시는 [\[대수적 구조\] §분수체, ⁋정의 2](/ko/math/algebraic_structures/field_of_fractions#def2)에서 살펴본 ring of fraction이다. 여기에서는 $M=A$로 잡았다. 특별히 우리는 $A$가 integral domain이라면 그 ring of fraction $\Frac(A)$가 field가 되는 것 또한 살펴보았다. ([\[대수적 구조\] §분수체, ⁋명제 6](/ko/math/algebraic_structures/field_of_fractions#prop6))

또 다른 예시로, 마찬가지로 $M=A$로 두고, $A$의 prime ideal $S=A\setminus \mathfrak{p}$로 두어 $A_\mathfrak{p}=S^{-1}A$을 생각할 수 있었다. [정의 1](#def1)을 이용하여 이를 임의의 $A$-module $M$에도 적용할 수 있는데, 그렇게 하여 얻어지는 $A$-module을 $M_\mathfrak{p}$로 적는다. 

위의 두 예시 모두 [정의 4](#def4)에서 정의한 덧셈구조 및 $A$의 스칼라곱 외에도 곱셈구조를 가지고 있다. 명시적으로 이 구조는

$$\frac{x}{s}\frac{x'}{s'}=\frac{xx'}{ss'}$$

으로 주어지므로 $S^{-1}A$를 $A$-algebra로 생각할 수 있다. 

Ring의 localization은 다음과 같은 universal property를 갖는다.

<div class="proposition" markdown="1">

<ins id="prop6">**명제 6**</ins> Ring $A,B$와 $A$의 multiplicative subset $S$를 고정하자. 만일 ring homomorphism $f:A \rightarrow B$에 의한 $S$의 image $f(S)\subseteq B$가 $f(S)\subseteq B^\times$를 만족한다면, 유일한 ring homomorphism $\tilde{f}: S^{-1}A \rightarrow B$가 존재하여 $\tilde{f}\circ\epsilon=f$가 성립한다. 

</div>
<details class="proof" markdown="1">
<summary>증명</summary>

주어진 조건을 만족하는 $f$가 주어졌다 하자. 만일 주어진 조건을 만족하는 $\tilde{f}: S^{-1}A \rightarrow B$가 존재한다면, 임의의 $a/s\in S^{-1}A$에 대하여

$$\tilde{f}\left(\frac{a}{s}\right)=\tilde{f}\left(\frac{a}{1}\frac{1}{s}\right)=\tilde{f}(\epsilon(a)\epsilon(s)^{-1})=\tilde{f}(\epsilon(a))\tilde{f}(\epsilon(s)^{-1})=f(a)f(s)^{-1}$$

이어야 하므로 $\tilde{f}$가 존재한다면 위의 식에 의해 유일하게 결정된다. 이제 위의 식 $\tilde{f}(a/s)=f(a)f(s)^{-1}$으로 정의한 $\tilde{f}: S^{-1} \rightarrow B$가 ring homomorphism임을 보이면 되고, 이는 단순한 계산에 불과하다.

</details>

이로부터 localization의 functoriality 또한 보일 수 있다. 

## 국소화와 아이디얼

한편, localization과 ideal 사이에는 특정한 관계가 있다. 우선 다음을 정의하자.

<div class="definition" markdown="1">

<ins id="def7">**정의 7**</ins> Ring homomorphism $f:A \rightarrow B$와 $A$의 ideal $\mathfrak{a}$, $B$의 ideal $\mathfrak{b}$에 대하여 다음을 정의한다.

1. $f$에 의한 $\mathfrak{b}$의 *contraction*은 $A$의 ideal $f^{-1}(\mathfrak{b})$으로 정의하고, $\mathfrak{b}^c$로 적는다.
2. $f$에 의한 $\mathfrak{a}$의 *extension*은 image $f(\mathfrak{a})$로 생성된 $B$의 ideal로 정의하고, $\mathfrak{a}^e$로 적는다.

</div>

첫 번째 정의를 하기 위해서는 $f^{-1}(\mathfrak{b})$가 ideal이 된다는 것을 증명해야 하지만, 이 증명은 쉽다. 위의 표기법들은 유용한 것이지만 비교적 덜 직관적이므로 이번 글이 지나면 위의 표기 대신 $f^{-1}(\mathfrak{b})$와 $f(\mathfrak{a})B$로 적을 것이다. 

<div class="proposition" markdown="1">

<ins id="prop8">**명제 8**</ins> 임의의 ring $A$, multiplicative subset $S$와 localization $S^{-1}A$, 그리고 canonical map $\epsilon:A \rightarrow S^{-1}A$에 대하여 다음이 성립한다. 

1. 임의의 ideal $\mathfrak{b}\subset S^{-1}A$에 대하여, $\mathfrak{b}=\mathfrak{b}^{ce}$이 성립한다.
2. 임의의 ideal $\mathfrak{a}\subset A$에 대하여, 
  
    $$\mathfrak{a}^{ec}=\{a\in A:\text{there exists $s\in S$ satisfying $sa\in \mathfrak{a}$}\}$$
  
    이 성립한다. 특히 $\mathfrak{a}^e=S^{-1}A$인 것과 $\mathfrak{a}\cap S\neq\emptyset$인 것이 동치이다.

따라서, $S^{-1}A$의 prime ideal들과, $A$의 prime ideal들 중 $S$와 만나지 않는 것들 사이의 inclusion-preserving bijection이 존재한다. 

</div>
<details class="proof" markdown="1">
<summary>증명</summary>

1. 우선 $\mathfrak{b}^{ce}\subseteq \mathfrak{b}$는 일반적으로 항상 성립한다. 반대 방향을 보이기 위해 $a/s\in \mathfrak{b}$라 하자. 그럼 $s(a/s)=a/1$이 $\mathfrak{b}$에 속해야 하므로, $a\in \mathfrak{b}^c$가 성립한다. 따라서 $a/1\in \mathfrak{b}^{ce}$이고 이로부터 $a/s=(1/s)(a/1)\in \mathfrak{b}^{ce}$임을 안다. 
2. 주어진 식의 우변을 편의상 $\mathfrak{a}'$라 적자. 그럼 우선 임의의 $a'\in \mathfrak{a}'$에 대하여, $sa'\in \mathfrak{a}$이도록 하는 $s$가 존재한다. 이제 $a'/1=sa'/s\in \mathfrak{a}^e$인 것으로부터 $a'\in \mathfrak{a}^{ec}$인 것을 안다. 반대로 임의의 $a\in \mathfrak{a}^{ec}$에 대하여, $a/1=a'/s$를 만족하는 $a\in \mathfrak{a}$와 $s\in S$를 찾을 수 있다. 그럼 적당한 $t\in S$가 존재하여 $tsa=ta'\in \mathfrak{a}$가 되며, 이제 $ts\in S$이므로 정의에 의해 $a\in \mathfrak{a}'$이 성립한다. 또 
  
  $$\mathfrak{a}^e=S^{-1}A\iff 1/1\in \mathfrak{a}^e\iff 1\in \mathfrak{a}^{ec}\iff \text{there exists $s\in S$ s.t. $s1\in \mathfrak{a}$}\iff \mathfrak{a}\cap S\neq \emptyset$$

  이다.

이제 2번 결과로부터 임의의 $\mathfrak{b}\subseteq S^{-1}A$가 주어졌을 때 $\mathfrak{b}^c$는 $S$와 만나지 않는 $A$의 prime ideal임을 안다. ([\[대수적 구조\] §분수체, ⁋명제 9](/ko/math/algebraic_structures/field_of_fractions#prop9)) 반대로 $\mathfrak{a}\subseteq A$가 $S$와 만나지 않는 $A$의 prime ideal이라 하자. 그럼 $\mathfrak{a}^e$는 $S^{-1}A$의 prime ideal이다. 임의의 $b/t,b'/t'$에 대하여 $(b/t)(b'/t')\in \mathfrak{a}^e$라 하자. 그럼 적당한 $a\in \mathfrak{a}$와 $s\in S$가 존재하여 $(bb')/(tt')=a/s$라 할 수 있고, 따라서 적당한 $u\in S$가 존재하여 $utt'a=usbb'\in \mathfrak{a}$이다. 이제 $\mathfrak{a}\cap S=\emptyset$인 것으로부터 $us\not\in \mathfrak{a}$인 것을 알고, $\mathfrak{a}$는 prime ideal이므로 $bb'\in \mathfrak{a}$가 성립한다. 따라서 $b\in \mathfrak{a}$이거나 $b'\in \mathfrak{a}$이고 $\mathfrak{a}^e$는 prime ideal이다. 이들 대응이 서로간의 inverse가 된다는 것은 2번 결과에서 자연스레 따라나오는 것이다. 

</details>

위의 명제로부터 다음이 자명하다.

<div class="proposition" markdown="1">

<ins id="cor9">**따름정리 9**</ins> Noetherian ring의 localization은 noetherian이다. 

</div>
<details class="proof" markdown="1">
<summary>증명</summary>

$S^{-1}A$의 ideal들의 ascending chain

$$\mathfrak{b}_0\subseteq \mathfrak{b}_1\subseteq\cdots$$

가 주어졌다 하면,

$$\mathfrak{b}_0^c\subseteq \mathfrak{b}_1^c\subseteq\cdots$$

는 noetherian ring $A$의 ideal들의 ascending chain이므로 적당한 $N$이 존재하여, $n>N$일 때마다 $\mathfrak{b}\_n^c=\mathfrak{b}\_{n+1}^c$이다. 이제 그러한 $n$에 대하여

$$\mathfrak{b}_n=\mathfrak{b}_n^{ce}=\mathfrak{b}_{n+1}^{ce}=\mathfrak{b}_{n+1}$$

이다. 

</details>

한편 [명제 7](#prop7)로부터, $A$의 임의의 prime ideal $\mathfrak{p}$에 대하여 $\mathfrak{p}^e=\mathfrak{p}A_\mathfrak{p}$는 $A_\mathfrak{p}$의 유일한 *maximal* ideal이라는 것이 자명하다. 즉 $A_\mathfrak{p}$는 local ring이며, 그 quotient field $A_\mathfrak{p}/\mathfrak{p}A_\mathfrak{p}$가 잘 정의된다. 

<div class="definition" markdown="1">

<ins id="def10">**정의 10**</ins> Ring $A$와 prime ideal $\mathfrak{p}$에 대하여, field $A_\mathfrak{p}/\mathfrak{p}A_\mathfrak{p}$를 $A$의 $\mathfrak{p}$에서의 *residue field*라 부르고 $\kappa(\mathfrak{p})$로 적는다. 

</div>

---

**참고문헌**

**[Eis]** David Eisenbud. *Commutative Algebra: with a view toward algebraic geometry*. Springer, 1995.

---