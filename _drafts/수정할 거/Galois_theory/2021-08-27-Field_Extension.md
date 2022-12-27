---

title: "Field Extension"
excerpt: "Field extension (확대체)의 정의"

categories: [Math / Galois Theory]
permalink: /ko/math/galois_theory/field_extension
header:
    overlay_image: /assets/images/Galois_theory/Field_extension.png
    overlay_filter: 0.5
sidebar: 
    nav: "algebraic_structures"

date: 2021-08-27
last_modified_at:
weight: 2

published: false

---
<div class="notice--warning" markdown="1">

이 글은 현재 수정중입니다.

이 글은 예전에 쓴 글로, 서술 방향이 마음에 들지 않거나 표기법이 마음에 들지 않아 전체적으로 수정이 진행중입니다. 읽으실 때 참고해주세요.

</div>

모든 ring은 unity 1을 가지고 있고, 모든 ring homomorphism은 unital homomorphism이다. (즉, $1$을 $1$로 보낸다.)

## Prime fields and characteristic

앞으로 해 나갈 우리의 이야기는 field $K$의 *characteristic*에 의해, 세세한 디테일이 두 갈래로 나뉘게 된다. 따라서, 우리는 먼저 field의 characteristic을 정의할 것이다. 우선 다음을 보자.

<ins id="df1">**정의 1**</ins> Field $F$가 *prime field*라는 것은 $F$가 $\mathbb{Q}$ 혹은 $F_p$ 중 하나와 isomorphic하다는 것이다.
{: .definition}

$\mathbb{Q}$의 subfield는 $1$을 포함하므로 $\mathbb{Z}$의 모든 원소를 포함하고, 따라서 $\mathbb{Z}$의 field of fraction인 $\mathbb{Q}$도 포함해야 한다. 즉, $\mathbb{Q}$의 subfield는 자기 자신 뿐이다. 또, $F_p$의 임의의 subring은 ($1$을 포함하므로) $F_p$ 자기 자신을 항상 포함하므로 $F_p$의 subfield 또한 자기 자신 뿐이다. 따라서 임의의 prime field에 대해, 이 field의 subfield는 자기 자신뿐이다. 

보통 많은 책에서 다음을 먼저 소개한 후 prime field를 정의하기도 한다.

<ins pp="pp2">**명제 2**</ins> Subfield를 갖는 임의의 (not necessarily commutative) ring $R$에 대하여, 정확히 하나의 subfield $P$가 prime subfield가 된다. 또, $P$는 $R$의 center, 그리고 $R$의 임의의 subfield에 포함된다.
{: .proposition}
<details class="proof" markdown="1">
<summary>증명</summary>

$R$의 임의의 subfield $K$가 주어졌다고 하자. $R$의 center $C$에 대하여, $K'=C\cap K$라 하면 $K'$는 $R$의 subfield이다. $K'$이 덧셈과 곱셈에 대해 닫혀있는 것은 자명하고, 만일 $c\in C\cap K$가 nonzero라면 $c^{-1}\in K$가 존재하는데, $cr=rc$가 모든 $r\in R$에 대해 성립하므로, 각 변 양쪽에 $c^{-1}$을 곱하면 $rc^{-1}=c^{-1}r$이 되기 때문이다.  
Ring homomorphism $f:\mathbb{Z}\rightarrow A$를 생각하자. 이 homomorphism은 $1$의 값에 의해 결정되는데, $f(1)=1$이므로 이 homomorphism은 유일하게 결정된다. 이 때의 $\ker f=\mathfrak{p}$라 하자. 한편, $A$의 임의의 subring은 $1$을 포함하므로, $f(\mathbb{Z})$를 모두 포함하고 따라서 $K'$ 또한 $f(\mathbb{Z})$를 포함한다. $K'$는 field이므로, zero ideal $(0)$은 prime ideal이고 따라서 이 ideal의 preimage $\mathfrak{p}=\ker f=f^{-1}(0)$ 또한 prime이다. 따라서, $\mathfrak{p}=(0)$이거나, 적당한 prime number $p$에 대하여 $\mathfrak{p}=(p)$이다.  
만일 $\mathfrak{p}=(0)$이라면 $f:\mathbb{Z}\rightarrow K'$가 injective라는 뜻이므로, localization의 universal property에 의해 또 다른 injective map $\bar{f}:\mathbb{Q}\rightarrow K'$로 확장될 수 있다. 이제 $\bar{f}(\mathbb{Q})=P\subset K'$는 $\mathbb{Q}$와 isomorphic하다.
한편 만일 $\mathfrak{p}=(p)$라면, first isomorphism theorem에 의해 우리는 $\mathbb{Z}/\mathfrak{p}=F_p$와 $f(\mathbb{Z})$ 사이의 isomorphism을 찾을 수 있으므로, 이 경우에도 역시 $K'$의 prime subfield $P=f(\mathbb{Z})\subset K'$가 존재한다.  
이렇게 얻어진 prime subfield $P$는 정의에 의해 $R$의 center $C$에 속해있으므로, 이제 $R$의 임의의 subfield $L$에 대하여 $P$가 $L$에도 속한다는 것을 보여야 한다. 이건 꽤 자명한데, $P\cap L$은 $P$의 subfield이기 때문이다. 그럼 prime field의 subfield는 자기 자신 뿐이므로, $P\cap L=P$이고 따라서 $P\subset L$이다. 마지막으로 유일성은 방금 전의 argument에서 subfield $L$을 또 다른 prime subfield $P'$로 바꾸면 된다. 그럼 $P\subset P'$일 것인데, $P'$는 prime field이므로 $P=P'$여야 한다. 
</details>

우리 이야기에서, 위의 정의는 특히 $R$이 field인 경우에 자주 쓰이게 된다. 아무튼 우리가 정의하기로 했던 characteristic을 정의할 차례다.

<ins id="df3">**정의 3**</ins> Subfield를 갖는 임의의 ring $R$에 대하여, $R$의 prime subfield가 $\mathbb{Q}$라면 $R$이 characteristic zero, 그렇지 않고 $F_p$라면 $R$의 characteristic이 $p$라고 한다. $R$의 characteristic을 $\chR$로 표기한다. 
{: .definition}

많은 저자들이 ring의 characteristic을 정의하는 방법과는 차이가 있는데, 대부분은 임의의 ring에 대해 characteristic을 정의하지만 부르바키는 그러지 않았다. 하지만 앞서 말했듯, 우리가 관심을 갖는 경우는 $R$이 field인 경우이므로 (따라서 subfield를 갖는 경우이므로) 우리가 다룰 경우들에서는 항상 두 정의가 동일하다.

<div class="proposition" markdown="1">

<ins id="pp4">**명제 4**</ins> $R$이 ring이라 하자. 그럼 다음이 성립한다.

1. $\chR=0$인 것은 임의의 $n\neq 0$에 대하여, mapping $x\mapsto n\cdot x$가 bijective인 것과 동치이다.
2. $\chR=p$인 것은 임의의 $x\in R$에 대하여 $p\cdot x=0$인 것과 동치이다.

</div>

<details class="proof" markdown="1">
<summary>증명</summary>

[명제 3](#pp3)의 증명과 마찬가지로, $f:\mathbb{Z}\rightarrow R$을 생각하자. 그럼 임의의 $n\in\mathbb{Z}$와 $x\in R$에 대하여, $n\cdot x=f(n)x$이므로, $\chR=0$인 것은 $f$가 $\bar{f}:\mathbb{Q}\rightarrow R$로 extend되는 것과 동치이고, 이는 다시 임의의 $f(n)\in R$이 invertible하다는 것과 동치이므로 1번이 성립한다. 비슷하게, $\chR=p$인 것은 $f(p\mathbb{Z})=0$인 것과 동치이고, 이는 다시 $f(p)=0$, 그리고 $p\cdot x=0$인 것과 동치가 된다.

</details>

Characteristic $p$를 갖는 ring의 중요한 특징은 다음 명제에서 나온다.

<div class="proposition" markdown="1">

<ins id="pp5">**명제 5 (Freshman's dream)**</ins> $R$이 characteristic $p$의 commutative ring이라 하자. 그럼 다음의 두 식

$$(a+b)^p=a^p+b^p,\qquad (ab)^p=a^pb^p$$

이 성립한다.
</div>

<details class="proof" markdown="1">
<summary>증명</summary>

둘째 식은 자명하고, 첫째 식도 $(a+b)^p$를 전개하면 $a^p$와 $b^p$를 제외한 모든 항들의 계수 (binomial coefficient)가 $p$로 나누어 떨어지므로 자명하다.

</details>

이 명제에 의해, 예를 들어, 다항식 $x^p-a^p$는 $\chK=p$인 field에서 $(x-a)^p$와 같이 인수분해된다. 이 부분이 나중에 Galois theory를 본격적으로 시작했을 때 이야기가 갈리는 부분이다. 

아무튼 위의 명제에 의해, $\chR=p$인 commutative ring $R$에는 자연스러운 endomorphism $a\mapsto a^p$가 존재한다. 이를 *Frobenius endomorphism*이라 부른다. 임의의 정수 $r$에 대하여, 이 Frobenius endomorphism을 $r$번 합성한 결과는 $x\mapsto x^{p^r}$이다. 임의의 부분집합 $S\subset R$에 대하여, 이 endomorphism에 의해 생기는 $S$의 image를 $S^{p^r}$로 표현하자. 만일 $S$가 subring이었다면, subring의 homomorphic image로써 $S^{p^r}$ 또한 subring이 된다. 

<ins id="rmk1">**참고**</ins> 위의 표기 $x\mapsto x^{p^r}$은 꽤나 그럴듯한게, 만일 $x\mapsto x^{p^r}$과 $x\mapsto x^{p^s}$를 합성한다면 $x\mapsto (x^{p^r})^{p^s}=x^{p^{r+s}}$가 된다. 즉, 지수법칙이 문제없이 적용되며, 나중에 이 endomorphism이 bijective하다면, inverse 또한 지수법칙을 잘 만족하게 할 수 있다.
{: .remark}


$R$의 임의의 subring $S$와 부분집합 $A$에 대하여, 앞으로 $S[A]$는 $S\cup A$로 generate된 $R$의 subring을 뜻한다. 또, 만일 $R$이 field일 경우, $S(A)$는 방금 정의한 $S[A]$의 field of fraction을 뜻한다. 

<div class="proposition" markdown="1">

<ins id="pp6">**명제 6**</ins> $R$이 commutative이고, $\chR=p$라 하자. $R$의 subring $K$와 부분집합 $S$에 대하여, 다음이 성립한다.

1. 임의의 정수 $r$에 대하여, $(K[S])^{p^r}=K^{p^r}[S^{p^r}]$이고, 만일 $R$이 field였다면 $K(S)^{p^r}=K^{p^r}(S^{p^r})$도 성립한다.
2. 만일 $K[S]$가 $K$-module로써 $R$의 원소들 $(x_i)_{i\in I}$들로 generate됐다면, $K[S^{p^r}]$은 $(x_i^{p^r})\_{i\in I}$에 의해 generate된다.

</div>

<details class="proof" markdown="1">
<summary>증명</summary>

우선 정의에 의해, $(K[S])^{p^r}$은 $K\cup S$에 의해 generate되는 subring을 endomorphism $x\mapsto x^{p^r}$을 통해 보내서 얻어진다. 따라서, 이 subring은 $K^{p^r}\cup S^{p^r}$을 generator로 가지므로 주어진 등식이 성립한다. $R$이 field라면 $K(S)$는 $K\cup S$들과, 그들의 inverse들에 의해 generate되므로 방금의 argument를 그대로 사용할 수 있다.  
위의 등식에서 $(K[S])^{p^r}=K^{p^r}[S^{p^r}]$이므로, 이 module이 ($K^{p^r}$-module로써) $(x_i^{p^r})_{i\in I}$에 의해 generate되는 것은 자명하다. 한편, $K$-module $K[S^{p^r}]$은 $S^{p^r}$의 원소들의 finite product $x_1^{p^r}x_2^{p^r}\cdots x_n^{p^r}$들로 generate되는데, 이들은 모두 $(K[S])^{p^r}$의 원소들이므로 $K[S^{p^r}]$은 $(K[S])^{p^r}$로도 generate된다. $(K[S])^{p^r}$은 다시 $K^{p^r}$-module로써 $(x_i^{p^r})\_{i\in I}$들로 generate되므로, 원하는 결론을 얻는다.

</details>

이제 마지막으로 perfect ring을 정의한 후, 메인 주제인 field extension으로 넘어간다. 

<ins id="df7">**정의 7**</ins> $\chR=p$인 ring $R$이 *perfect*라는 것은 $R$이 commutative하고, Frobenius endomorphism $x\mapsto x^p$가 bijective한 것이다.
{: .definition}

따라서, perfect ring에서는 Frobenius endomorphism, 혹은 더 일반적으로 이를 $r$번 합성한 $x\mapsto x^{p^r}$이 automorphism이 된다. 이 때의 inverse를 $x\mapsto x^{p^{-r}}$로 표기하면 앞선 [참고](#rmk1)에서 언급했듯 이 표기법 또한 지수법칙을 잘 유지해준다.

<ins id="pp8">**명제 8**</ins> 임의의 perfect ring은 reduced이다.
{: .proposition}

<details class="proof" markdown="1">
<summary>증명</summary>

임의의 자연수 $r$에 대하여, $x\mapsto x^{p^r}$의 kernel을 $\mathfrak{n}_r$로 적자. 그럼 이 ideal들은 increasing sequence를 이루고, 따라서 이들의 합집합 $\mathfrak{n}=\bigcup\_{r\geq 0}\mathfrak{n}_r$도 ideal이다. 한편, 만일 임의의 $x\in R$이 nilpotent였다면 어떤 $k$에 대해 $x^k=0$이었을 것이고, 따라서 적당한 $r$을 잡아 $x^{p^r}=0$이도록 할 수 있으므로, 모든 nilpotent element는 $\mathfrak{n}$의 원소가 되어야 한다. 그런데 $\mathfrak{n}_r$은 bijection $x\mapsto x^{p^r}$의 kernel로써 항상 $0$이므로 증명 끝.

</details>

<ins id="pp9">**명제 9**</ins> 만일 field $K$가 $\lvert K\rvert<\infty$를 만족한다면 $K$는 perfect이다. 
{: .proposition}

<details class="proof" markdown="1">
<summary>증명</summary>

$K$가 characteristic $p\neq 0$을 갖는다 하자. 만일 $K$가 유한하다면, $K$에서 $K^p$으로의 map $x\mapsto K^p$는 injective이고 따라서 surjective이기도 하다.  

</details>

마지막으로, 다음을 정의한다.

<div class="definition" markdown="1">

<ins id="df10">**정의 10**</ins> Characteristic $p$를 갖는 commutative ring $R$에 대하여, $R$의 *perfect closure* $\hat{R}$와 canonical map $u:R\rightarrow\hat{R}$은 characteristic $p$의 perfect ring이며, 다음의 universal property를 만족한다.

> Characteristic $p$를 갖는 임의의 perfect ring $S$와, homomorphism $v:R\rightarrow S$에 대하여, 유일한 homomorphism $\hat{v}:\hat{R}\rightarrow S$가 존재하여 $v=\hat{v}\circ u$가 성립한다.

</div>

물론, 이와 같이 universal property를 이용해 정의한다면, 이러한 대상이 실재로 존재해야 말이 된다. 이를 직접 construct하려면, direct system $\\{R_n\\}$을, 각각의 $n$에 대해 $R_n=R$로 두고, 각각의 map들은 $x\mapsto x^p$ 및 그들의 합성으로 준 다음 direct limit을 취하면 된다. 

특히, characteristic $p$를 갖는 perfect ring $R$과 그 subring $S$에 대하여, $S$를 포함하는 가장 작은 $R$의 perfect subring을 생각할 수 있다. 그럼 이는 정확히 $S^{p^{-\infty}}=\bigcup S^{p^{-f}}$이며, 이는 $A$의 perfect closure와 동일하다.

## Basic definition of field extension

앞으로 모든 algebra는 associative, unital이라 가정한다. (따라서 ring structure를 가진다.) 그러므로 정의에 의해 임의의 algebra의 subalgebra 또한 1을 가진다. 또, 모든 algebra homomorphism은 unital homomorphism인 것으로 한다. 

이제 드디어 갈루아 이론을 향한 첫 발을 내딛을 수 있다. 우선 field extension이 무엇인지부터 정의한다.

<div class="definition" markdown="1">

<ins id="df11">**정의 11**</ins> Field $K$에 대하여, $K$의 *extension*은 ring structure가 field가 되는 $K$-algebra $E$를 뜻한다. $E$의 subalgebra 중 field인 것을 *subextension*이라 부른다.

</div>

Field extension을 정의하는 방법은 여러가지가 있지만 이 정의도 아주 쓸만하다.   

우선, $E$ 위에 $K$-algebra structure가 주어졌다는 것은 ring homomorphism $u:K\rightarrow E$가 주어졌다는 것과 동일한 말이란 것을 기억하자. 이건 만일 $E$ 위에 $K$-algebra structure가 주어졌다면, $u:K\rightarrow E$를 $r\mapsto r\cdot 1$로 정의하면 $u$가 ring homomorphism이 되기 때문이고, 또 거꾸로 임의의 $u:K\rightarrow E$가 주어졌다면 임의의 $r\in K$와 $x\in E$에 대해 $r\cdot x=u(r)x$로 정의하면 $\cdot$이 scalar multiplication이 되기 때문이다.  
그럼 $E$가 $K$의 extension이라는 것은 어떤 ring homomorphism $u:K\rightarrow E$가 정의되는데, $u$는 field를 domain으로 갖는 ring homomorphism이고, zero map이 아니므로 injective여야 한다. 따라서, $u$는 $K$에서 $E$로의 inclusion map을 정의한다고 할 수 있으며[^1], 따라서 이 정의가 다음의 정의

> Field $K$에 대하여, $K$의 *extension*은 $K$를 subring으로 갖는 field $E$를 뜻한다.

를 imply한다는 것을 알 수 있다. 물론 위의 정의로부터 거꾸로 [정의 11](#df11)을 유도할 수도 있지만, 우리는 separable degree를 정의할 때 $K$-algebra structure를 아주 잘 사용하게 된다.

또, $K$의 두 extension $L$, $L'$이 주어졌다고 하자. 이들은 모두 $K$-algebra이므로, $L$과 $L'$ 사이의 자연스러운 map은 $K$-homomorphism들이다. 그런데, $K$-algebra homomorphism으로서 $\varphi:L\rightarrow L'$은 $1$을 $1$로 보내고, 따라서 임의의 $r\in K$에 대해 $r\cdot 1$을 $r\cdot 1$로 보내므로, 이 map들은 위에서 언급한 $K$의 isomorphic copy들을 보존한다. 이러한 이유로 우리는 Galois theory를 할 때, field $K$를 fix하는 homomorphism들을 $K$-homomorphism이라 부르는 것이다.

어쨌든, canonical한 inclusion $u:K\rightarrow E$에 대해, 만일 $u(K)=E$라면 이 extension이 trivial extension이라 부른다. 즉, trivial extension은 dimension $1$짜리 $K$-vector space이다. 더 일반적으로 다음을 정의한다.

<div class="definition" markdown="1">

<ins id="df12">**정의 12**</ins> $A$가 $K$-algebra라 하자. 그럼 ($K$-vector space로써의) $\dim A$를 이 algebra의 *degree*라 부르고, $[A:K]$로 적는다. 

</div>

그럼 $K$-vector space 레벨에서 다음이 성립한다.

<div class="proposition" markdown="1">

<ins id="pp13">**명제 13**</ins> $E$가 $K$의 extension이고, $A$가 $E$-algebra라면 $[A:K]=[A:E][E:K]$가 성립한다.   

</div>

하지만, 우리가 algebra structure를 리뷰하며 살펴봤듯, 일반적으로 algebra의 generator와 module의 generator는 서로 다르고, 이는 당연히 field extension에서도 마찬가지다. 예를 들어, 임의의 field $K$와, $K$를 포함하는 (충분히 큰) $K$의 extension $E$가 주어졌다고 하자. Algebra로써, $K[X]$는 그냥 polynomial ring이 된다. 한편, $K(X)$를 (항상 해왔던 대로) "$K$와 $X$를 포함하는 $E$의 subexension 가운데 가장 작은 것"으로 정의한다면$K(x)$와 $K[X]$가 같을 필요가 없다. 예를 들어, $K(X)$는 polynomial $X$의 역원을 포함해야 한다.[^2] 그러므로 notation상 "$K$와 집합 $S$를 포함하는 extension 중 가장 작은 것"은 항상 $K(S)$로 고정해서 적기로 한다.

어찌되었건 간에, 만일 $E$가 finite degree를 갖는 $K$의 extension이라면, $E$의 $K$-basis가 algebra로써 $E$를 generate하므로, $E$는 finitely generated $K$-algebra이기도 하다. 

<div class="proposition" markdown="1">

<ins id="pp14">**명제 14**</ins> $A$가 finite degree를 갖는 $K$-algebra라 하자. 만일 $a\in A$가 $a$의 left (resp. right) zero divisor가 아니라면, $a$는 invertible하다.

</div>
<details class="proof" markdown="1">
<summary>증명</summary>

$A$가 finite-dimensional $K$-vector space이므로, linear map $x\mapsto ax$가 injective하다는 것은 bijective하다는 것과 동치이고, 따라서 $a$의 inverse element가 존재한다.   

</details>

<div class="definition" markdown="1">

<ins id="df15">**정의 15**</ins> 주어진 field $K$에 대해, $K$의 두 extension $E$, $F$가 주어졌다고 하자. Field $L$이 $E$와 $F$의 *composite extension*이라는 것은, $L$이 $E$와 $F$의 extension이면서, $E\cup F$로 generate되는 것이다. 

</div>

혹은, 더 정확하게는 $L$이 $E$, $F$와 isomorphic한 subring에 의해 generate된다는 것이고, 이를 diagram으로 쓰면 (field extension과 ring homomorphism은 같은 것이므로) 다음과 같다.

![composite_extension](/assets/images/Galois_theory/Field_extension-1.png){:width="120px"  class="invert" .align-center}

물론 이렇게 새로 정의를 내린 후에는 이러한 $L$이 항상 존재하는지가 궁금하다.

<div class="proposition" markdown="1">

<ins id="pp16">**명제 16**</ins> 임의의 field $K$와 $K$의 두 extension $E$, $F$에 대하여, 이들의 composite extension이 존재한다.  

</div>
<details class="proof" markdown="1">
<summary>증명</summary>

$E\otimes\_KF$를 생각하자. 이제 $i:E\rightarrow E\otimes\_KF$와 $j:F\rightarrow E\otimes\_KF$를 $x\mapsto x\otimes 1$과 $y\mapsto 1\otimes y$로 정의하면, 이들은 자명하게 ring homomorphism이 된다. 한편, Krull's theorem에 의하여 $E\otimes\_KF$의 maximal ideal $\mathfrak{m}$이 존재하며, 따라서 canonical projection $p:E\otimes\_KF\rightarrow (E\otimes\_KF)/\mathfrak{m}$을 생각하면 두 개의 ring homomorphism $pi$와 $pj$를 얻는다. $E$와 $F$는 각각 field이므로, $pi$와 $pj$는 모두 injective이고, $(E\otimes\_KF)/\mathfrak{m}$은 이들의 extension이다. 또, 이 extension의 proper한 subextension은 ($\mathfrak{m}$의 maximality에 의해) 존재하지 않으므로, 정의에 의해 composite extension이 된다.

</details>

앞선 [참고](#rmk2)에 따라, 우리는 $L$이 $E$와 $F$를 포함하고 있고, $pi$와 $pj$ 각각을 $L$로의 injection으로 볼 수도 있다. 따라서 이를 다음과 같이 쓸 수도 있다.

>임의의 field $K$, $E$와 homomorphism $u:K\rightarrow E$에 대하여, 만일 $K'$가 $K$의 extension이라면, 적당한 $E$의 extension $E'$와, homomorphism $u':K'\rightarrow E'$가 존재하여 $u'$를 $K$ 위로 restrict한 것이 $u$와 같도록 할 수 있다.

## Linearly disjoint extensions

친절한 저자라면 이쯤에서 algebraic extension을 소개할테지만, 부르바키의 서술 스타일은 (직관에 대한 별다른 고려 없이...) 일관적으로 아주 general한 곳으로부터 특수한 경우로 논의를 좁혀나가는 스타일이다보니, linear disjointness부터 소개한다. 이건, 예를 들면 Hungerford 기준으로는 Galois theory를 챕터 5에서 소개한 후, separability를 일반적인 field extension으로 확장하며 나오는 내용인데, 어쨌든 부르바키는 이렇게 motivation을 주기보다는 처음부터 linear disjointness의 개념을 소개해서 separability를 이를 통해 증명하는 것을 택했다.

$A$와 $B$가 $\Omega$의 subalgebra라 하자. 그럼 $\varphi: A\otimes_KB\rightarrow \Omega$를 $x\otimes y\mapsto xy$로 정의할 수 있다. 그럼 $\im\varphi$는 $A\cup B$에 의해 generate된 $\Omega$의 subring이다. 

<div class="definition" markdown="1">

<ins id="df17">**정의 17**</ins> 만일 위에서 정의된 $\varphi$가 injective라면, $A$와 $B$가 $K$에 대해 *linearly disjoint*한 extension들이라 부른다. 

</div>

이 조건을 만족시키는 extension들이 linearly disjoint라 불리는 이유를 살펴보자. 만일 $A$와 $B$가 각각 $(a_i)$, $(b_j)$를 basis로 갖는다면, $\im\varphi$의 모든 원소들은 어차피 $\varphi(\sum\alpha_k'\otimes\beta_k')=\sum\alpha_k'\beta_k'$의 꼴이므로, 예를 들어 $\alpha_k'$들을 모두 basis를 이용해 쪼갠다면 적절한 $\beta_i$들에 대하여 $\sum\beta_ia_i$의 꼴로 나타날 것이다. 이와 비슷한 일을 $\beta_k'$들을 basis $(b_j)$를 이용해 쪼개어 반복할 수도 있고, 혹은 $\alpha_k'$들과 $\beta_k'$들을 모두 분해하여 반복할 수도 있다. 따라서, $\im\varphi$의 원소들은

$$\sum_{i\in I}\beta_ia_i,\qquad\sum_{j\in J}\alpha_jb_j,\qquad\sum_{(i,j)\in I\times J}\gamma_{ij}a_ib_j$$

등의 꼴로 ($\alpha_j\in A$, $\beta_i\in B$, $\gamma_{ij}\in K$) 나타난다.

<div class="proposition" markdown="1">

<ins id="pp18">**명제 18**</ins> 위와 같은 상황에서, 다음이 동치이다.

1. $A$와 $B$가 $K$에 대해 linearly disjoint하다.
2. $(a_i)$는 $B$-linearly independent이다. 즉, 만일 $\sum\beta_ia_i=0$이라면, 모든 $i$에 대해 $\beta_i=0$이다. 마찬가지로 $(b_j)$도 $A$-linearly independent이다.
3. $(a_ib_j)$는 $K$-linearly independent이다. 즉, 만일 $\sum\gamma_{ij}a_ib_j=0$이라면, $\gamma_{ij}=0$이다.

</div>
<details class="proof" markdown="1">
<summary>증명</summary>

1$\implies$2$\implies$3$\implies$1의 형태로 보인다.

우선 $A$와 $B$가 $K$에 대해 linearly disjoint라 가정하고, $\sum \beta_ia_i=0$라 하자. 가정에 의해 $\varphi$는 injective이므로, 

$$\sum_{i\in I} a_i\otimes \beta_i=0$$

이 성립해야 한다. 이제 $\beta_i=\sum \gamma_{ij}b_j$ ($\gamma_{ij}\in K$)라 하면, 위의 식은

$$\sum_{(i, j)\in I\times J} \gamma_{ij}(a_i\otimes b_j)$$

가 되고, $a_i\otimes b_j$들은 $A\otimes_KB$의 basis이므로 $\gamma_{ij}=0$이고, 따라서 $\beta_i$들도 모두 0이어야 한다. 비슷하게 $(b_j)$에 대해서도 증명할 수 있다.

엉겁결에 3번 비슷한 형태가 나와버렸는데, 아무튼 2번을 가정하자. 주어진 $\sum\gamma_{ij}a_ib_j=0$에 대하여, $\alpha_j=\sum_i\gamma_{ij}a_i$라 하면

$$0=\sum\gamma_{ij}a_ib_j=\sum_j\alpha_jb_j$$

이고, $(b_j)$는 $A$-linearly independent이므로 $\alpha_j=0$이 모든 $j$에 대해 성립한다. 그런데 $\alpha_j=\sum_i\gamma_{ij}a_i$에서, $a_i$들은 linearly independent하므로 $\gamma_{ij}$들도 모두 0이다. 따라서 3번이 성립한다.

마지막으로, 3번이 성립한다 하고, $\sum(\alpha_k\otimes\beta_k)\in\ker\varphi$라 하자. 즉, $\sum\alpha_k\beta_k=0$이 성립한다. 이제 $\alpha_k=\sum \gamma_{ki}a_i$, $\beta_k=\sum\delta_{kj}b_j$라 하면, 주어진 식은

$$\sum_{(i,j)\in I\times J}\left(\sum_{k=0}^n\gamma_{ki}\delta_{jk}\right)a_ib_j$$

가 되므로, $\sum\gamma_{ik}\delta_{kj}=\lambda_{ij}$라 하면 3번의 가정에 의해 $\lambda_{ij}$는 모두 0이다. 이제 

$$\begin{aligned}\sum_{k=0}^n\alpha_k\otimes\beta_k&=\sum_{k=0}^n\left(\sum_{i\in I}\gamma_{ki}a_i\right)\otimes\left(\sum_{j\in J}\delta_{jk}b_j\right)\\&=\sum_{k=0}^n\sum_{(i,j)\in I\times J} \gamma_{ki}\delta_{jk}(a_i\otimes b_j)=\sum_{(i,j)\in I\times J}\lambda_{ij}(a_i\otimes b_j)=0\end{aligned}$$

이므로 $\varphi$는 injective하다. 
</details>

물론, 우리는 $A$와 $B$가 각각 $\Omega$의 subextension인 경우에 많은 관심이 있다. 

<div class="proposition" markdown="1">

<ins id="pp19">**명제 19**</ins> $E$, $F$가 모두 $\Omega$의 subextension이라 하자. 
 
 1. 만일 $F$의 degree가 유한하다면, $E\cup F$에 의해 generate되는 subring이 field가 되고, 이는 $E(F)$와 같다. 또, 이 때 $[E(F):E]\leq[F:K]$가 성립하고, 등호는 정확히 $E$와 $F$가 linearly disjoint할 때 성립한다.
 2. 만일 $E$의 degree 또한 유한하다면, $E(F)$도 finite degree를 가지며, $[E(F):K]\leq[E:K][F:K]$가 성립하고 등호는 정확히 $E$, $F$가 linearly disjoint할 때 성립한다.

</div>
<details class="proof" markdown="1">
<summary>증명</summary>

우선 증명의 편의를 위해 $E\cup F$로 generate되는 subring을 $S$라 적자. $(x_i)$가 $F$의 finite $K$-basis라면, $S$의 모든 원소는 $x_i$들의 $E$-linear combination으로 적을 수 있으므로 $S$는 finitely generated $E$-algebra이고, $[S:E]\leq [F:K]$가 성립한다. 그런데 $S$는 field $\Omega$에 포함되어있으므로 integral domain이고, 따라서 field이다 ([명제 14](#pp14)). 즉, $S=E(F)$이고, 원하는 부등식 $[E(F):E]\leq[F:K]$가 성립한다. 이 부등식의 등호가 성립하는 조건은 정확히 $(x_i)$들의 $S=E(F)$의 basis 또한 되는 것이므로,  이는 앞선 명제의 동치조건 2번에 의하여 $E$, $F$가 linearly disjoint하다는 것이다.

만일 $E$도 $K$에 대해 finite degree를 갖는다면, $[E(F):K]=[E(F):E][E:K]\leq [F:K][E:K]$가 성립하므로 두 번째 파트는 자명하다.

</details>

Ring $E(F)=K(E\cup F)$를 생각하자. 앞서 말했던 것과 같이, $K[E\cup F]$가 field가 될 이유는 일반적으로 전혀 없다. 그러나, $K[E\cup F]$의 field of fraction은 $K(E\cup F)$와 동일하며, 더 일반적으로 다음이 성립한다. 

<div class="proposition" markdown="1">

<ins id="pp20">**명제 20**</ins> $E$, $F$가 $\Omega$의 subextension이라 하고, 각각이 $\Omega$의 sub-$K$-algebra $A$, $B$의 field of fraction들이라 하자. 그럼 $E$, $F$가 linearly disjoint한 것은 $A$, $B$가 linearly disjoint한 것과 동치이다. 

</div>

<details class="proof" markdown="1">
<summary>증명</summary>

만일 $E$, $F$가 linearly disjoint하다면 그 부분집합들인 $A$, $B$들이 linearly disjoint한 것은 자명하다. 따라서 그 역만 보이면 된다. 그런데, 만일 $\Omega$의 어떤 원소들이 $B$-linearly independent하다면 (통분을 통해) field of fraction인 $F$에 대해서도 $F$-linearly independent해야한다. 이와 비슷하게 $A$와 $E$에 대해서도 같은 것을 보일 수 있으므로, [명제 18](#pp18)의 2번 조건에 의하여 $E$, $F$도 linearly disjoint하다.

</details>

<div class="proposition" markdown="1">

<ins id="pp21">**명제 21**</ins> $E$, $F$가 $\Omega$의 sub-$K$-extension이라 하자. 만일 $E$, $F$가 linearly disjoint하다면, $E$와 $F$의 모든 subextension들은 서로 linearly disjoint하다. 거꾸로, 만일 $E$, $F$의 모든 *finitely generated* subextension들이 linearly disjoint하다면, $E$와 $F$도 linearly disjoint하다. 

</div>
<details class="proof" markdown="1">
<summary>증명</summary>

만일 $E$, $F$가 lienarly disjoint하다면 이들의 subextension들도 linearly disjoint하다는 것은 자명하다. 따라서 반대방향만 보이면 충분하다. 그런데 이것도 거의 자명한게, 어차피 linearly disjoint의 조건은 linearly independence로 정의되므로 finiteness가 어차피 정의에 포함되어 있다. 즉, 엄밀하게 증명하자면, ([명제 18](#pp18)의 3번 조건을 이용하기 위해) $E$와 $F$의 basis $(a_i)$, $(b_j)$에 대하여, 임의의 linear combination $\sum\gamma_{ij}a_ib_j$가 주어졌다고 하자. 이제 $\supp(\gamma)_{I\times J}$는 유한하므로, $(i,j)\in\supp(\gamma)\_{I\times J}$이도록 하는 index들의 부분집합 $I'$와 $J'$도 모두 유한집합이다.  그러므로, $(a_i)\_{i\in I'}$와 $(b_j)\_{j\in J'}$에 의해 generate되는 algebra들은 finitely generated이고, 가정에 의해 이들은 linearly disjoint하므로 모든 pair $i$, $j$에 대해 $\gamma\_{ij}=0$이다.  

</details>

앞선 두 명제를 이용하면, 다음과 같이 composite extension이 linearly disjoint할 조건을 state할 수 있다.

<div class="proposition" markdown="1">

<ins id="pp22">**명제 22**</ins> $E$, $F$, $G$가 $\Omega$의 sub-$K$-extension들이고, $F\subset G$라 하자. 그럼 $E$와 $G$가 linearly disjoint한 것은 $E$와 $F$가 $K$에 대해 linearly disjoint하고, $E(F)$와 $G$가 $F$에 대해 linearly disjoint한 것과 동치이다. 

</div>
<details class="proof" markdown="1">
<summary>증명</summary>

우선, 만일 $E$, $G$가 linearly disjoint하다면 $F$는 $G$의 subextension이니 $E$, $F$는 linearly disjoint하다. 이제 $B$가 $E$의 $K$-basis라 하자. 그럼 $F[E]$는 $B$의 원소들의 $F$-linear combination으로 나타나고, 이 표현은 유일하므로 $B$는 $F[E]$의 $F$-basis가 된다. 이제 $B$는 가정에 의해 $G$-linearly independent하고, 따라서 $F[E]$와 $G$는 linearly disjoint하다. 따라서, 이는 $F[E]$의 field of fraction $F(E)=E(F)$에 대해서도 성립한다. ([명제 20](#pp20)).

역을 보이기 위해, $B$를 위에서와 같이 잡자. 그럼 $E$와 $F$는 linearly disjoint해야 하므로 $B$는 $F$-linearly independent하다. 즉, $B$는 $F[E]$의 $F$-basis이며, 가정에 의해 $F[E]$와 $G$는 linearly disjoint하므로 $B$는 $G$-linearly independent하다. 따라서 $E$, $G$는 $K$에 대해 linearly disjoint다.

</details>

---
**Reference**

**[BCH]** N. Bourbaki, P.M. Cohn, and J. Howie. <i>Algebra II: Chapters 4 - 7</i>. Elements of mathematics. Springer Berlin-Heidelberg, 2013. 

---

[^1]: 정확히 말하자면, $E$는 $K$와 isomorphic한 subring $u(K)$를 가진다.
[^2]: 따라서, $K(X)$는 $X$에 대한 *rational function*들의 field다.
