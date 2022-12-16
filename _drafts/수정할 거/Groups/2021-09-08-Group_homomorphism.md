---

title: "준동형사상"
excerpt: "Group homomorphism and the isomorphism theorems"

categories: [Math / Groups]
permalink: /ko/math/groups/group_homomorphisms
header:
    overlay_image: /assets/images/Groups/Group_homomorphisms.png
    overlay_filter: 0.5
sidebar: 
    nav: "algebraic_structures"
    
date: 2021-09-08
last_modified_at:
weight: 3

published: false

---
<div class="notice--warning" markdown="1">

이 글은 현재 수정중입니다.

이 글은 예전에 쓴 글로, 서술 방향이 마음에 들지 않거나 표기법이 마음에 들지 않아 전체적으로 수정이 진행중입니다. 읽으실 때 참고해주세요.

</div>

## Review of definitions

우리는 [§대수적 구조, 정의 19](/ko/math/groups/introduction#pp19)에서 군을 정의한 후에 군 준동형사상은 그냥 마그마 준동형사상과 동일한 것으로 정의했었다. 즉,

<div class="definition" markdown="1">

<ins id="df1">**정의 1**</ins> 두 군 $G$, $G'$에 대하여, $f:G\rightarrow G'$가 *군 준동형사상*이라는 것은 임의의 $x$, $y\in G$에 대하여 다음의 식

$$f(xy)=f(x)f(y)$$

이 항상 성립하는 것이다.
</div>

또한, 이후에는 다음 명제를 보였었다. 

<div class="proposition" markdown="1">

<ins id="pp2">**명제 2**</ins> 군 준동형사상 $f:G\rightarrow G'$에 대하여, $f(e)=e$가 성립한다.

</div>
<details class="proof" markdown="1">
<summary>증명</summary>

물론, 좌변의 $e$는 $G$의 항등원이고, 우변의 $e$는 $G'$의 항등원이다. 군 준동형사상의 정의에 의하여, 

$$f(e)=f(ee)=f(e)f(e)$$

가 성립한다. 그런데, $f(e)$는 군 $G'$의 원소이므로 역원이 존재하고, 따라서 양 변에 $f(e)^{-1}$을 곱해주면 $e=f(e)$를 얻는다. 

</details>

<div class="proposition" markdown="1">

<ins id="crl3">**따름정리 3**</ins> 군 준동형사상 $f:G\rightarrow G'$에 대하여, $f(x^{-1})=f(x)^{-1}$이 항상 성립한다.

</div>
<details class="proof" markdown="1">
<summary>증명</summary>

앞선 명제에 의하여 $f(e)=e$이므로, 

$$e=f(e)=f(xx^{-1})=f(x)f(x^{-1})$$

그리고 비슷하게 $e=f(x^{-1})f(x)$가 성립한다. 따라서, 역원의 유일성에 의하여 ([§Introduction, 명제 17](/ko/math/groups/introduction#pp17)) $f(x^{-1})$은 $f(x)$의 역원 $f(x)^{-1}$이다.
</details>

<div class="example" markdown="1">

<ins id="ex4">**예시 4**</ins> 임의의 군 $G$에 대하여, $\operatorname{id}_G:G\rightarrow G$는 자명하게 군 준동형사상이다. 또 다른 군 $G'$가 주어졌을 때, 상수함수 $f:G\rightarrow G'$가 군 준동형사상이 되기 위해서는 그 값이 $e$여야만 한다.

</div>

다음 명제는 어떤 수학적인 구조들 사이에 특별한 함수가 정의되면 항상 체크했던 것이며, 그 증명은 자명하다.

<div class="proposition" markdown="1">

<ins id="pp5">**명제 5**</ins> 두 군 준동형사상의 합성은 군 준동형사상이다.

</div>

<details class="proof" markdown="1">
<summary>증명</summary>

$f_1:G_0\rightarrow G_1$, $f_2:G_1\rightarrow G_2$가 각각 군 준동형사상이라 하자. 그럼 임의의 $x, y\in G_0$에 대하여, 

$$(f_2\circ f_1)(xy)=f_2(f_1(xy))=f_2(f_1(x)f_1(y))=f_2(f_1(x))f_2(f_1(y))=(f_2\circ f_1)(x)(f_2\circ f_1)(y)$$

이므로 주어진 명제가 성립한다. 

</details>

한편, 이렇게 준동형사상이 주어진다면 *동형사상*의 개념 또한 주어진다.

<div class="definition" markdown="1">

<ins id="df6">**정의 6**</ins> 군 준동형사상 $f:G\rightarrow G'$에 대하여, 적당한 군 준동형사상 $g:G'\rightarrow G$가 존재하여 $f\circ g=\operatorname{id}_{G'}$이고 $g\circ f=\operatorname{id}_G$라면 $f$가 *동형사상*이라 하고, $g$를 $f$의 *역 준동형사상*라 부른다. 

</div>

$\operatorname{id}\_G$와 $\operatorname{id}\_{G'}$는 모두 bijection이므로, [Set Theory, §함수, 명제 11](/ko/math/set_theory/functions#pp11)을 $f\circ g=\operatorname{id}_{G'}$와 $g\circ f=\operatorname{id}_G$에 각각 적용하면 동형사상은 항상 bijection이라는 것을 보일 수 있다. 뿐만 아니라, 그 역도 성립한다.

<div class="proposition" markdown="1">

<ins id="pp7">**명제 7**</ins> 임의의 군 준동형사상 $f$가 동형사상인 것은 $f:G\rightarrow G'$가 bijective 군 준동형사상인 것과 동치이다.

</div>

<details class="proof" markdown="1">
<summary>증명</summary>

반대쪽 방향만 보이면 충분하다. $f$는 bijection이므로, 함수로써 역함수 $f^{-1}:G'\rightarrow G$가 존재한다. 만일 $f^{-1}$이 군 준동형사상이기만 하다면, 정의에 의해 $f$는 동형사상이 될 것이다.

임의의 $y, y'\in  G'$를 택하자. 그럼 $f$는 bijection이므로, 적당한 $x$, $x'$가 유일하게 존재하여 $f(x)=y$이고 $f(x')=y'$이다. 이제

$$f^{-1}(yy')=f^{-1}(f(x)f(x')=f^{-1}(f(xx'))=xx'=f^{-1}(y)f^{-1}(y')$$

이므로, $f^{-1}$은 군 준동형사상이고 따라서 $f$는 동형사상이다. 

</details>

위의 명제의 증명에서 눈치챌 수 있겠지만, 만약 $f:G\rightarrow G'$가 동형사상이라면, 그 역 준동형사상 $g:G'\rightarrow G$는 유일하다. 또 다른 $g':G'\rightarrow G$가 $f\circ g'=\operatorname{id}_{G'}$, 그리고 $g'\circ f=\operatorname{id}_G$를 만족한다 가정하자. 임의로 주어진 $y\in G'$에 대하여, 유일한 $x\in G$가 존재하여 $f(x)=y$이고, 그럼

$$g'(y)=g'(f(x))=x=g(f(x))=g(y)$$

가 되기 때문이다. 

## Kernel and image

우리는 동형사상을 정의하기 위해서는 bijective 준동형사상을 살펴보면 된다고 하였으므로, 두 가지 종류의 준동형사상, 즉 *injective* 준동형사상과 *surjective* 준동형사상을 살펴볼 필요가 있다. 

Surjective 준동형사상을 어떻게 characterize해야할지는 꽤나 자명하다.

<div class="definition" markdown="1">

<ins id="df8">**정의 8**</ins> 군 준동형사상 $f:G\rightarrow G'$에 대하여, $f$의 함수로서의 image $f(G)$를 군 준동형사상 $f$의 *image*라 부르고, $\operatorname{im}f$으로 적는다.

</div>

그럼 $f$가 surjective 준동형사상인 것은 $\operatorname{im}f=G'$인 것과 동치이다. 뿐만 아니라, 다음이 성립한다.

<div class="proposition" markdown="1">

<ins id="pp9">**명제 9**</ins> 임의의 군 준동형사상 $f:G\rightarrow G'$의 image $\operatorname{im}f$는 $G'$의 부분군이다.

</div>
<details class="proof" markdown="1">
<summary>증명</summary>

임의의 $y_1, y_2\in \operatorname{im}f$를 택하자. 그럼 적절한 $x_1,x_2\in G$가 존재하여 $f(x_i)=y_i$가 $i=1,2$에 대하여 성립한다. 이제 $f(x_2^{-1})=f(x_2)^{-1}=y_2^{-1}$이고 ([따름정리 3](#crl3)), 따라서 

$$y_1y_2^{-1}=f(x_1)f(x_2)^{-1}=f(x_1)f(x_2^{-1})=f(x_1x_2^{-1})$$

이 성립한다. 당연히 $x_1x_2^{-1}\in G$이므로, $y_1y_2^{-1}\in\operatorname{im}f$가 성립하고 $\operatorname{im}f$는 $G'$의 부분군이다. 

</details>

대표적으로, 우리가 이전에 살펴본 canonical projection $G\rightarrow G/H$가 surjective 군 준동형사상이다. ([§부분군과 몫군, 정의 17](/ko/math/groups/subgroups#pp17) 이후의 remark)


반면 injective 준동형사상을 어떻게 characterize해야 할지는 좀 애매하다. 결론에 반하여, $f(x_1)=f(x_2)$인 $x_1\neq x_2$가 있다고 가정하자. 그럼

$$e=f(x_1)f(x_2)^{-1}=f(x_1x_2^{-1})$$

이어야 한다. 그런데, 이 계산을 잘 살펴보면, injectivity는 이렇게 $e$로 옮겨지는 값이 유일한지 아닌지만 결정하면 자연스럽게 따라온다는 사실을 알 수 있다. 즉,

<div class="proposition" markdown="1">

<ins id="pp10">**명제 10**</ins> 군 준동형사상 $f:G\rightarrow G'$가 injective인 것은 $f^{-1}(e)=\\{e\\}$가 성립하는 것과 동치이다.

</div>

<details class="proof" markdown="1">
<summary>증명</summary>

우선, 군 준동형사상은 항등원을 항등원으로 옮기므로, $f^{-1}(e)$는 어떤 경우에도 공집합이 되지는 않는다. 먼저 $f$가 injective라 가정하자. 만일 $x\in f^{-1}(e)$라면, $f(x)=e=f(e)$이므로, $x=e$여야 하고, 따라서 $f^{-1}(e)=\\{e\\}$가 된다.  
거꾸로, $f^{-1}(e)=\\{e\\}$라 가정하자. 만일 어떤 $x_1$, $x_2\in G$가 존재하여 $f(x_1)=f(x_2)$라면 위의 계산에 의해

$$e=f(x_1x_2^{-1})$$

여야 한다. 그런데, $f^{-1}(e)$의 유일한 원소는 $e$ 뿐이므로, $x_1x_2^{-1}=e$이다. 즉, $x_1=x_2$이고 따라서 $f$는 injective이다.

</details>

여기서 등장하는 집합 $f^{-1}(e)$를 다음과 같이 부르자.

<div class="definition" markdown="1">

<ins id="df11">**정의 11**</ins> 군 준동형사상 $f:G\rightarrow G'$에 대하여, 집합 $f^{-1}(e)$를 $f$의 *kernel*이라 부르고 $\ker f$로 적는다. 

</div>

$f$의 image와 마찬가지로, kernel도 그 자체로 group structure를 갖는다. 

<div class="proposition" markdown="1">

<ins id="pp12">**명제 12**</ins> 군 준동형사상 $f:G\rightarrow G'$에 대하여, $\ker f$는 $G$의 정규부분군이 된다. 

</div>
<details class="proof" markdown="1">
<summary>증명</summary>

우선, $\ker f$가 $G$의 부분군이 된다는 것부터 보여야 한다. 임의의 $x_1,x_2\in\ker f$에 대하여, $f(x_1x_2^{-1})$의 값을 계산해보면 

$$f(x_1x_2^{-1})=f(x_1)f(x_2)^{-1}=ee^{-1}=e$$

이므로, $x_1x_2^{-1}\in\ker f$가 성립하고, 따라서 $\ker f$는 $G$의 부분군이다. 여기에 더해, $\ker f$가 정규부분군임을 보이기 위해, 임의의 $g\in G$와 $x\in\ker f$에 대하여 $gxg^{-1}$의 값을 계산해보자. 그럼

$$f(gxg^{-1})=f(g)f(x)f(g)^{-1}=f(g)ef(g)^{-1}=f(g)f(g)^{-1}=e$$

이므로, $gxg^{-1}\in \ker f$이다. 따라서 $g(\ker f)g^{-1}\subset \ker f$가 성립하므로, $\ker f$는 $G$의 정규부분군이다. 

</details>
<div class="remark" markdown="1">

<ins id="rmk1">**참고**</ins> 그러나 일반적으로, 군 준동형사상의 image가 $G'$의 정규부분군이 될 이유는 당연히 없다. 예를 들어, group $G'$가 normal이 아닌 부분군 $G$를 가진다고 하면, canonical inclusion $i:G\rightarrow G'$의 image $i(G)=G$이다. 

</div>

## The isomorphism theorems 

임의의 group $G$와 정규부분군 $H$가 주어지면 quotient group $G/H$가 잘 정의된다.방금 살펴본 것과 같이 임의의 군 준동형사상 $f:G\rightarrow G'$는 자연스러운 정규부분군 $\ker f$를 만들어주므로, 이 때 만들어지는 quotient group $G/\ker f$를 살펴볼 수 있다.  
한편, $G/\ker f$는 equivalence relation에 의해 정의되는 quotient set이기도 하므로, [Set Theory, §Equivalence Relation](/ko/math/set_theory/equivalence_relations)에서 살펴본 많은 것들도 성립하리라 기대할 수 있다. 

$G/\ker f$는 다음의 relation (편의상 $R$이라 하자)

$$x\equiv y\iff xy^{-1}\in\ker f$$

에 의해 정의되는 quotient group이다. 그런데, [명제 12](#pp12)의 첫 번째 식을 거꾸로 써 보면, 이는 $f(x)=f(y)$라는 뜻이기도 하다. 즉, 이 말은 군 준동형사상 $f$가 $R$과 compatible하다는 뜻이다. ([Set Theory, §Equivalence Relation, 정의14](/ko/math/set_theory/equivalence_relations#df14)) 그럼 [Set Theory, §Equivalence Relation, 명제 15](/ko/math/set_theory/equivalence_relations#pp15)에 의하여, 적당한 함수 $\tilde{f}: G/\ker f\rightarrow G'$가 존재하여 $f=\tilde{f}\circ p$가 성립한다. 그런데, $p$는 surjection이므로, 즉 임의의 $\bar{a},\bar{b}\in G/\ker f$에 대하여[^1] $\bar{a}=p(a)$, $\bar{b}=p(b)$이므로,

$$\tilde{f}(\bar{a}\bar{b})=\tilde{f}(p(a)p(b))=\tilde{f}(p(ab))=f(ab)=f(a)f(b)=\tilde{f}(\bar{a})\tilde{f}(\bar{b})$$

가 성립한다. 즉, $\tilde{f}$ 또한 군 준동형사상이 된다. 뿐만 아니라, $\tilde{f}$의 공역을 치역으로 제한해준다면 다음의 commutative diagram

![elements]({{ site.url }}{{ site.baseurl }}/assets/images/<#name#>.png){:width="250px"  class="invert" .align-center}

을 얻고, 여기서 $\tilde{f}:G/\ker f\rightarrow \operatorname{im}f$는 bijection이므로 $\tilde{f}$는 동형사상이다. 이를 다음과 같이 이름붙인다.

<div class="proposition" markdown="1">

<ins id="thm13">**정리 13 (The first isomorphism theorem)**</ins> 임의의 군 준동형사상 $f:G\rightarrow G'$에 대하여, $G/\ker f\cong \operatorname{im}f$가 항상 성립한다.

</div>

더 일반적으로 다음이 성립한다.

<div class="proposition" markdown="1">

<ins id="pp14">**명제 14**</ins> 임의의 군 준동형사상 $f:G\rightarrow G'$와 $G$의 정규부분군 $H$에 대하여, $f=\tilde{f}\circ p$를 만족하는 $\tilde{f}:G/H\rightarrow G'$가 존재할 필요충분조건은 $N\leq \ker f'$인 것이다. 

</div>
<details class="proof" markdown="1">
<summary>증명</summary>

[Set Theory, §함수, 명제 12](/ko/math/set_theory/functions#pp12)의 첫 번째 assertion에 의해 자명하다. 

</details>

First isomorphism theorem이 있다는 것은, second, ... 도 있다는 뜻이다. 이들은 모두 first isomorphism theorem으로부터 얻어진다.

<div class="proposition" markdown="1">

<ins id="thm15">**정리 15 (The second isomorphism theorem)**</ins> $K$가 $G$의 부분군이고, $N$은 $G$의 정규부분군이라 하자. 그럼 $K/(N\cap K)\cong NK/N$이 성립한다.

</div>
<details class="proof" markdown="1">
<summary>증명</summary>

우선, [§부분군과 몫군, 명제 16](/ko/math/groups/subgroups#pp16)으로부터, $N$은 $NK=N\vee K=KN$의 정규부분군이 된다. 한편, $K\subset NK$이므로, 다음과 같은 준동형사상의 composition

$$K\overset{\iota}{\hookrightarrow}NK\overset{\pi}{\twoheadrightarrow}NK/N$$ 

을 생각할 수 있다. 그럼

$$\ker(\pi\iota)=(\pi\iota)^{-1}(e)=\iota^{-1}(\ker\pi)=\iota^{-1}(N)=K\cap N$$

이므로, $\pi\iota$에 first isomorphism theorem을 적용하면

$$K/\ker(\pi\iota)=K/(K\cap N)\cong\operatorname{im}(\pi\iota)$$

를 얻는다. 그런데 $NK/N$의 임의의 원소는 모두 $nkN$의 꼴이고, 적당한 $n'\in N$이 존재하여 $nk=kn'$이라 할 수 있으므로, $NK/N$의 임의의 원소 $nkN$은

$$nkN=kn'N=kN=\pi(k)=\pi(\iota(k))\in\operatorname{im}(\pi\iota)$$

을 만족하므로 원하는 결과를 얻는다.
</details>

집합론에서 하던 것과 같이, 다음과 같이 부분군 구조 $H\leq G$를 표현하자.

![<#description#>](/assets/images/<#path#>/<#name#>.png){:width="250px"  class="invert" .align-center}

그럼 위 명제에서, $NK=N\vee K=KN$은 $N$과 $K$를 모두 포함하는 $G$의 부분군이므로 다음과 같은 diagram을 얻는다.

![<#description#>](/assets/images/<#path#>/<#name#>.png){:width="250px"  class="invert" .align-center}

한편, $K$를 quotient해 준 $K\cap N$은 group structure를 가지므로 ([§부분군과 몫군, 명제 4](/ko/math/groups/subgroups#pp4)), 이들 사이의 포함관계는 최종적으로 다음의 diagram으로 표현된다.

![<#description#>](/assets/images/<#path#>/<#name#>.png){:width="250px"  class="invert" .align-center}

이 diagram에서, second isomorphism theorem은 두 마주보는 변 $N\cap K\leq K$와 $N\leq NK$가 서로 같다는 것을 의미한다. 

<div class="proposition" markdown="1">

<ins id="thm16">**정리 16 (The third isomorphism theorem)**</ins> $H$, $K$가 group $G$의 정규부분군이고, $K&lt;H$라 하자. 그럼 $H/K$는 $G/K$의 정규부분군이며 $(G/K)/(H/K)\cong G/H$가 성립한다.  

</div>
<details class="proof" markdown="1">
<summary>증명</summary>

마찬가지로 first isomorphism theorem을 사용한다. 이를 위해 우선 자연스러운 surjective map $G/K\rightarrow G/H$를 하나 정의한 다음, 이 map의 kernel이 $H/K$가 됨을 보여야 한다. $p:G/K\rightarrow G/H$를 다음의 식

$$p:aK\mapsto aH$$

로 정의하자. $K&lt;H$이므로, $p$는 well-defined이다. 즉, 만일 $G/K$에서 $aK=bK$라면, $ab^{-1}\in K&lt; H$이므로 $aH=bH$이기도 하다. 어렵지 않게 $p$가 군 준동형사상인 것을 보일 수 있다. 또, 임의의 $aH\in G/H$에 대해, $aK$는 $p(aK)=aH$를 만족하므로 $p$는 surjective이기도 하다. 마지막으로 

$$aK\in\ker p\iff aH=eH\iff a\in H$$

이므로, $\ker p$는 정확히 $H/K$가 된다. 따라서 first isomorphism theorem에 의해 원하는 결과가 성립한다.

</details>

마지막 정리는 꽤나 자연스럽다.

<div class="proposition" markdown="1">

<ins id="thm17">**정리 17 (The fourth isomorphism theorem)**</ins> $G$가 group이고, $N$이 $G$의 정규부분군이라 하자. 그럼 *$N$을 포함하는 $G$의 부분군들의 집합*과 *$G/N$의 부분군들의 집합* 사이의 inclusion-preserving bijection이 존재한다. 뿐만 아니라, 이 bijection은 교집합이나 index, 정규부분군등의 관계를 모두 보존한다.

</div>

---
**Reference**

**[Bou]** Bourbaki, N. Algebra. I. Chapters 1-3. Translated from the French. Reprint of the 1989 English translation. *Elements of Mathematics. Springer-Verlag, Berlin,* 1998. 

---

[^1]: 지저분한 notation을 피하기 위해 $a\ker f$ 대신 $\bar{a}$로 적었다.
