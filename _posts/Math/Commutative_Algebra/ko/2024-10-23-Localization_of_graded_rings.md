---

title: "등급환의 국소화"
excerpt: ""

categories: [Math / Commutative Algebra]
permalink: /ko/math/commutative_algebra/localization_of_graded_rings
header:
    overlay_image: /assets/images/Math/Commutative_Algebra/Localization_of_graded_rings.png
    overlay_filter: 0.5
sidebar: 
    nav: "commutative_algebra-ko"

date: 2024-10-23
last_modified_at: 2024-10-23
weight: 4

---

우리는 임의의 graded ring, 더 일반적으로는 임의의 graded module을 localize하는 방법을 살펴본다. 이번 글에서는 별다른 말이 없다면 모든 graded ring은 $\mathbb{N}_{\geq 0}$-graded인 것으로 생각하고, $A=\bigoplus A_i$, $M=\bigoplus M_i$를 고정하기로 한다. 그럼 임의의 $n$에 대하여,

$$M(n)_k=M_{n+k}\qquad\text{for all $k$}$$

으로 정의된 $M(n)$은 자연스럽게 graded $A$-module 구조를 갖는다.

## 몫아이디얼

우선 임의의 ring $A$와 $A$의 두 ideal $\mathfrak{a}, \mathfrak{b}$에 대하여, ideal quotient의 정의를 기억하자. ([§기본개념들, ⁋정의 1](/ko/math/commutative_algebra/basic_notions#def1))

<div class="definition" markdown="1">

<ins id="def1">**정의 1**</ins> Ring $A$와 $A$의 두 ideal $\mathfrak{a}, \mathfrak{b}$에 대하여, *ideal quotient<sub>몫아이디얼</sub>*을 다음의 식

$$(\mathfrak{a}:\mathfrak{b})=\{a\in A\mid a \mathfrak{b}\subseteq \mathfrak{a}\}$$

으로 정의한다.

</div>

그럼 $(\mathfrak{a}:\mathfrak{b})$는 자명하게 덧셈에 대하여 닫혀있고, 또 임의의 $x\in A$와 $a\in (\mathfrak{a}:\mathfrak{b})$에 대하여 다음 식

$$xa \mathfrak{b}\subseteq x \mathfrak{a}\subseteq \mathfrak{a}$$

이 성립하므로 $xa\in (\mathfrak{a}:\mathfrak{b})$이다. 즉 $(\mathfrak{a}:\mathfrak{b})$는 실제로 ideal이 된다. 

## 동차아이디얼의 성질들

우리는 [\[대수적 구조\] §등급환, ⁋명제 6](/ko/math/algebraic_structures/graded_rings#prop6)에서 임의의 homogeneous ideal은 항상 homogeneous element들로 생성됨을 보였는데, 이를 이용하면 다음의 [보조정리 1](#lem1)을 보일 수 있다. 

<div class="proposition" markdown="1">

<ins id="lem2">**보조정리 2**</ins> Graded ring $A$와 $A$의 homogeneous ideal들 $\mathfrak{a},\mathfrak{b}$에 대하여 다음이 성립한다. 다음이 성립한다.

1. $\sqrt{\mathfrak{a}}$는 homogeneous ideal이다. 
2. $(\mathfrak{a}:\mathfrak{b})$는 homogeneous ideal이다. 
3. 임의의 homogeneous element $a,b\in A$가 $ab\in \mathfrak{a}$를 만족할 때마다 $a\in \mathfrak{a}$ 혹은 $b\in \mathfrak{a}$가 성립한다 하자. 그럼 $\mathfrak{a}$는 prime ideal이다. 

</div>
<details class="proof" markdown="1">
<summary>증명</summary>

1. 우선 $\sqrt{\mathfrak{a}}$가 homogeneous ideal인 것을 보이자. 즉 임의의 $x\in \sqrt{\mathfrak{a}}$에 대하여, $x$를 homogeneous ideal들의 합
    
    $$x=x_{d_1}+\cdots+x_{d_l},\quad d_1 < \cdots < d_l\tag{$\ast$}$$
    
    으로 나타냈을 때, $x_i$들 각각이 $\sqrt{\mathfrak{a}}$에 속한다는 것을 보여야 한다. 우선 $x\in \mathfrak{a}$인 것으로부터, 적당한 $k$가 존재하여 $x^k\in \mathfrak{a}$이다. 한편, 일반성을 잃지 않고 위의 표현 ($\ast$)에서 $x_l$이 가장 큰 차수를 갖는다고 하면, $x^k$를 homogeneous element들의 합으로 나타냈을 때, $x_l^k$가 차수 $k\deg x_l$에 있는 유일한 원소이다. 이제 $x^k\in \mathfrak{a}$이고 $\mathfrak{a}$가 homogeneous ideal인 것으로부터 $x_l^k\in \mathfrak{a}$, 즉 $x_l\in \sqrt{\mathfrak{a}}$인 것을 안다. 이후에는 $x-x_l\in\sqrt{\mathfrak{a}}$이므로 같은 논증을 반복하면 된다.
2. $x\in (\mathfrak{a}:\mathfrak{b})$라 하자. 위와 마찬가지로 $x$를 homogeneous ideal들의 합 ($\ast$)으로 나타냈을 때, $x\_i$들 각각이 $(\mathfrak{a}:\mathfrak{b})$에 속함을 보여야 한다. 이제 $\mathfrak{b}$를 생성하는 임의의 homogeneous element $b$가 주어졌다 하자. 그럼 $x_ib$는 원소 $xb\in \mathfrak{a}$의 $\deg x_i+\deg b$에 해당하는 homogeneous element이며, $\mathfrak{a}$가 homogeneous ideal이므로 $x_ib\in \mathfrak{a}$이다. 
3. 마지막으로 주어진 조건을 가정한 후, 임의의 두 원소 $x,y\in A$를 homogeneous element들의 합
    
    $$x=x_{d_1}+\cdots+x_{d_m},\quad y=y_{e_1}+\cdots+y_{e_n},\qquad d_1<\cdots< d_m,\quad e_1<\cdots< e_n$$

    으로 표현하자. 결론에 반하여 $xy\in \mathfrak{a}$이지만 $x\not\in \mathfrak{a}$, $y\not\in \mathfrak{a}$라 가정하자. 그럼 가정에 의하여 어떤 $x\_{d\_i}$들 중 적어도 하나는 $x\_{d\_i}\not\in \mathfrak{a}$를 만족해야 한다. 그러한 $i$들 중 가장 큰 것을 $k$라 하고, 비슷하게 $y\_{e\_l}$을 정의하자. 이제 $A$의 원소 $xy$의 degree $d\_k+e\_l$에 해당하는 homogeneous component를 보자. 이 원소는 

    $$(xy)_{d_k+e_l}=\sum_{d_i+e_j=d_k+e_l}x_{d_i}y_{e_j}$$

    의 꼴로 쓰여질 수 있으며, 이 때 위의 식의 우변에서 $x\_{d\_k}y\_{e\_l}$ 이외의 모든 항은 $d\_i>d\_k$ 혹은 $e\_j>e\_l$을 반드시 만족해야 한다. $d\_k$와 $e\_l$의 정의에 의하여, 이러한 항들은 모두 $\mathfrak{a}$의 원소이다. 그런데 $xy\in \mathfrak{a}$이고 $\mathfrak{a}$는 homogeneous ideal이므로, $(xy)_{d_k+e_l}$ 또한 $\mathfrak{a}$의 원소이고 이로부터 모순을 얻는다. 

</details>

특히 임의의 ring의 prime ideal에서의 localization이 중요한 예시였던 것과 같이, $A$가 graded ring일 경우에도 *homogeneous* prime ideal $\mathfrak{p}$에서의 localization은 중요한 예시가 된다. 따라서 위 보조정리의 세 번째 결과는 특히 기억할만하다. 

어쨌든 우선 우리는 일반적인 경우부터 시작한다. 다음 명제는 원소들의 degree가 어떻게 행동하는지만 살펴보면 중명할 수 있으며 그 증명도 자명하다.

<div class="proposition" markdown="1">

<ins id="prop3">**명제 3**</ins> $A$의 multiplicative subset $S$의 모든 원소가 homogeneous라 하자. 그럼 임의의 homogeneous element $x\in M_n$과 $s\in S$에 대하여, $x/s\in S^{-1}M$를 degree $n-\deg s$에 있는 것으로 정의하면 $S^{-1}M$는 $\mathbb{Z}$-graded $A$-module의 구조를 갖는다. 만일 $M=A$인 경우, 이 grading은 $S^{-1}A$ 위에 정의된 곱셈에 대하여도 잘 작동하여 $S^{-1}A$를 $\mathbb{Z}$-graded ring으로 만든다.

</div>

우리는 inclusion $(S^{-1}A)_0 \rightarrow S^{-1}A$를 통해 $S^{-1}A$을 $(S^{-1}A)_0$-module로 생각할 수 있다. 그럼 $S^{-1}A$의 degree $0$ 부분 $(S^{-1}A)_0$은 곱셈에 대하여 닫혀있으므로 $(S^{-1}A)_0$은 $(S^{-1}A)_0$-algebra이다. 일반적으로 $S^{-1}M$은 곱셈이 정의되지는 않지만, 마찬가지로 $S^{-1}M$의 degree $0$ 부분 $(S^{-1}M)_0$을 생각하면 이는 $(S^{-1}A)_0$-module 구조를 갖는다.

특별히 중요한 예시 중 하나는 degree $1$의 homogeneous element $f\in A_1$에 대하여 $S=\\{1,f,f^2,\cdots\\}$인 경우인데, 이 경우는 $(S^{-1}A)_0$으로부터 $S^{-1}A$를 복원해낼 수 있다.

<div class="proposition" markdown="1">

<ins id="prop4">**명제 4**</ins> 위와 같은 상황에서 다음의 isomorphism

$$S^{-1}A\cong (S^{-1}A)_0[T, T^{-1}]$$

이 성립한다. 여기에서 $T$는 degree $1$을 주는 형식적인 변수이며, 우변의 $(S^{-1}A)_0[T, T^{-1}]$는

$$(S^{-1}A)_0[T_1, T_2]/(T_1T_2-1)$$

으로 정의된다.

</div>
<details class="proof" markdown="1">
<summary>증명</summary>

함수 $\\{T_1,T_2\\} \rightarrow S^{-1}A$를 $T_1\mapsto f, T_2\mapsto f^{-1}$으로 정의하면 [\[대수적 구조\] §대수, ⁋명제 8](/ko/math/algebraic_structures/algebras#prop8)에 의하여 $(S^{-1}A)_0$-algebra homomorphism

$$(S^{-1}A)_0[T_1,T_2] \rightarrow S^{-1}A$$

을 얻는다. 명시적으로 이 homomorphism은

$$\sum_{i,j\geq 0} a_{i,j}T_1^i T_2^j\mapsto \sum_{i,j\geq 0} a_{i,j}f^{i-j}=\sum_{d\in \mathbb{Z}}\left(\sum_{j\geq \max(-d,0)} a_{j+d,j}\right)f^d$$

으로 주어지며, 이 때 ideal $(T_1T_2-1)$이 위의 homomorphism의 kernel에 포함되는 것이 자명하다. 한편, $\deg a_{i,j}=0$이므로 위의 homomorphism의 kernel은 다음 식

$$\sum_{j\geq \max(-d,0)} a_{j+d,j}=0\qquad\text{for all $d\in\mathbb{Z}$}$$

을 만족하는 다항식들의 모임이다. 표기의 편의를 위하여 위의 합을 $d$의 부호에 따라 다음의 세 조건

$$\sum_{j\geq 0} a_{j,j}=0,\quad \sum_{j\geq 0} a_{j+d,j}=0,\quad \sum_{j\geq 0} a_{j,j+d}=0\qquad \text{for all $d>0$}$$

으로 바꾸어 쓸 수 있으며, 그럼 각각의 경우

$$a_{0,0}=-\sum_{j\geq 1} a_{j,j},\quad a_{d,0}=-\sum_{j\geq 1} a_{j+d,j},\quad a_{0,d}=-\sum_{j\geq 1} a_{j,j+d}\qquad \text{for all $d>0$}$$

를 얻는다. 이제 이를 다항식

$$\begin{aligned}\sum_{i,j\geq 0} a_{i,j} T_1^iT_2^j&=\sum_{j\geq 0} a_{j,j}T_1^jT_2^j+\sum_{d>0}\sum_{j\geq 0} a_{j+d,j}T_1^{j+d}T_2^j+\sum_{d>0}\sum_{j\geq 0} a_{j,j+d}T_1^jT_2^{j+d}\\&=\left(a_{0,0}+\sum_{j\geq 1} a_{j,j}T_1^jT_2^j\right)+\sum_{d>0} \left(a_{d,0}T_1^d+\sum_{j\geq 1}a_{j+d,j}T_1^{j+d}T_2^j\right)+\sum_{d>0} \left(a_{0,d}T_2^d+\sum_{j\geq 1}a_{j,j+d}T_1^{j}T_2^{j+d}\right)\end{aligned}$$

에 각각 대입하면 우변은

$$\left(\sum_{j\geq 1} a_{j,j}(T_1^jT_2^j-1)\right)+\sum_{d>0}\left(\sum_{j\geq 1}a_{j+d,j}T_1^d(T_1^jT_2^j-1)\right)+\sum_{d>0}\left(\sum_{j\geq 1}a_{j,j+d}T_2^d(T_1^jT_2^j-1)\right)$$

이 된다. 이 때 각각의 $T_1^jT_2^j-1$는 $(T_1T_2-1)$에 포함되므로 위의 식의 kernel은 <em_ko>정확히</em_ko> $(S^{-1}A)\_0[T\_1,T\_2]$의 ideal $(T_1T_2-1)$에 해당한다. 한편 이 homomorphism은 정의에 의해 surjective이므로 원하는 결과를 얻는다. 

</details>

## 동차국소화

<div class="definition" markdown="1">

<ins id="def5">**정의 5**</ins> 앞서 정의한 $(S^{-1}A)\_0$와 $(S^{-1}M)\_0$을 각각 $A$와 $M$의 *homogeneous localization<sub>동차국소화</sub>*이라 부르고, $A\_{(S)}$와 $M\_{(S)}$와 같이 표현한다.

</div>

일반적인 localization과 마찬가지로, homogeneous element $f\in A$에 대하여, $S=\\{1,f,f^2,\cdots\\}$으로 얻어지는 $M$의 homogeneous localization을 $M\_{(f)}$으로 적기로 하고, homogeneous prime ideal $\mathfrak{p}\subseteq A$에 대하여, $S=A\setminus \mathfrak{p}$으로 얻어지는 $M$의 homogeneous localization을 $M_{(\mathfrak{p})}$으로 적기로 한다. 

남은 글에서, 임의의 graded $A$-module $M$에 대하여 

$$M^{(d)}=\bigoplus_{k\geq 0} M_{kd}$$

으로 적기로 한다. 그럼 다음은 [명제 4](#prop4)의 일반화이다.

<div class="proposition" markdown="1">

<ins id="prop6">**명제 6**</ins> Degree $d$의 homogeneous element $f\in A$를 고정하자. 그럼 다음의 isomorphism

$$M_{(f)}\cong M^{(d)}/(f-1)M^{(d)}$$

이 성립한다.

</div>
<details class="proof" markdown="1">
<summary>증명</summary>

주어진 isomorphism은 적당한 $u:M^{(d)} \rightarrow M_{(f)}$에 first isomorphism theorem을 적용하여 얻어지며, $u$는 다음의 식

$$u_k:M_{kd} \rightarrow M_{(f)};\qquad x\mapsto x/f^k$$

을 통해 얻어진다. 그럼 $u$가 surjective인 것과 $\ker u=(f-1)M^{(d)}$인 것을 어렵지 않게 보일 수 있다. 

</details>

만일 $\deg f=1$이라면 위의 isomorphism은 $M_{(f)}\cong M/(f-1)M$으로 쓸 수 있다.

한편, $S$가 degree $1$의 원소를 하나 이상 포함한다 하면 [명제 4](#prop4)을 각각의 원소에 적용하여 다음을 얻는다. 

<div class="proposition" markdown="1">

<ins id="prop7">**명제 7**</ins> $S$가 degree $1$의 원소를 적어도 하나 포함하는 homogeneous multiplicative set이라면 $S^{-1}A\cong (S^{-1}A)_0[T,T^{-1}]$이 성립한다.

</div>
<details class="proof" markdown="1">
<summary>증명</summary>

이는 본질적으로 [명제 4](#prop4)과 동일한 증명으로, $S$에 속하는 degree $1$의 원소 $f$를 택하여 [명제 4](#prop4)의 증명과 동일한 방식으로 homomorphism $(S^{-1}A)_0[T_1,T_2] \rightarrow S^{-1}A$을 정의하면 된다. 그럼 이 homomorphism의 kernel이 $(T_1T_2-1)$이 되는 것은 동일한 증명으로 보일 수 있으며, 이 homomorphism이 surjective인 것은 임의의 degree $d$짜리 $S^{-1}A$의 원소 $a/s$를 다음의 꼴

$$\frac{a}{s}=\frac{af^d}{s}\frac{1}{f^d}$$

으로 쓸 수 있다는 것을 이용하면 쉽게 보일 수 있다.

</details>

특별히 homogeneous prime ideal $\mathfrak{p}$을 하나 고정하고, $A\_1\not\subset \mathfrak{p}$라 가정하자. $S$를 $\mathfrak{p}$에 속하지 않는 homogeneous element들로 이루어진 multiplicative subset이라 하면, 적어도 하나의 nonzero $f\in A\_1$이 존재하여 $f\in S$이므로, 위의 명제에 의해

$$S^{-1}A\cong A_{(\mathfrak{p})}[T,T^{-1}]$$

을 얻는다. 

<div class="proposition" markdown="1">

<ins id="prop8">**명제 8**</ins> 위와 같은 상황에서, homomorphism $p:A \rightarrow A/(f-1)$에 의한 $\mathfrak{p}$의 image를 $\mathfrak{q}$라 하자. 그럼 $\mathfrak{q}$는 prime ideal이며, 다음 식

$$A_{(\mathfrak{p})}\cong\left(A/(f-1)\right)_\mathfrak{q}$$

이 성립한다.

</div>
<details class="proof" markdown="1">
<summary>증명</summary>

Ring homomorphism $q:A \rightarrow A/\mathfrak{p}$를 생각하고, $q$에 의한 $f$의 image를 $\bar{f}$라 하자. 그럼 

$$\frac{A/(f-1)}{\mathfrak{q}}\cong \frac{A/\mathfrak{p}}{(\bar{f}-1)}$$

이며, [명제 6](#prop6)에 의하여 우변은 다시 $(A/\mathfrak{p})[f^{-1}]_0$과 isomorphic하다. 그런데 $\mathfrak{p}$가 prime ideal이므로, $A/\mathfrak{p}$는 integral domain이고 따라서 localization $(A/\mathfrak{p})[f^{-1}]$ 또한 integral domain이고, 따라서 $(A/\mathfrak{p})[f^{-1}]_0$도 integral domain이다. 이로부터 $\mathfrak{q}$가 $A/(f-1)$의 prime ideal인 것을 안다. 편의상 $\mathfrak{a}=(f-1)$라 적으면, 원하는 isomorphism은 다음의 homomorphism

$$A \overset{a\mapsto a/1}{\longrightarrow} S^{-1}A \overset{f\mapsto T}{\longrightarrow} A_{(\mathfrak{p})}[T, T^{-1}] \overset{T\mapsto 1}{\longrightarrow} A_{(\mathfrak{p})}$$

과

$$A\overset{a\mapsto a+\mathfrak{a}}{\longrightarrow}A/\mathfrak{a}\overset{a+\mathfrak{a}\mapsto\frac{a+\mathfrak{a}}{1}}{\longrightarrow}(A/\mathfrak{a})_\mathfrak{q}$$

을 비교하여 나온다.

</details>

---

**참고문헌**

**[Eis]** David Eisenbud. *Commutative Algebra: with a view toward algebraic geometry*. Springer, 1995.

---