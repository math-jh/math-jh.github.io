---

title: "동형사상"
excerpt: "동형사상 정리들"

categories: [Math / Groups]
permalink: /ko/math/groups/isomorphism_theorems
header:
    overlay_image: /assets/images/Groups/Isomorphism_theorems.png
    overlay_filter: 0.5
sidebar: 
    nav: "groups-ko"

date: 2022-11-30
last_modified_at: 2022-11-30
weight: 6

---

## The first isomorphism theorem

가벼운 보조정리부터 시작한다.

<div class="proposition" markdown="1">

<ins id="lem1">**보조정리 1**</ins> 임의의 homomorphism $f:G\rightarrow G'$에 대하여, $\ker f$는 $G$의 normal subgroup이다.

</div>
<details class="proof" markdown="1">
<summary>증명</summary>

임의의 $g\in G$와 $x\in \ker f$에 대하여, 

$$f(gxg^{-1})=f(g)f(x)f(g^{-1})=f(g)e'f(g)^{-1}=f(g)f(g)^{-1}=e'.$$

</details>

그런데 $\ker f$에 의하여 정의되는 동치관계 

$$x\sim y\iff xy^{-1}\ker f$$

를 생각하면, 다음 식

$$f(y)=e'f(y)=f(xy^{-1})f(y)=f(xy^{-1}y)=f(x)$$

으로부터 $x\sim y\iff f(x)=f(y)$임을 알 수 있다. 즉, 몫집합 $G/\ker f=G/{\sim}$은 별다른 것이 아니라 함수 $f$에 의해 정의되는 동치관계이며 ([집합론, §동치관계의 예시들, 정의 2](/ko/math/set_theory/examples_of_equivalence#df2)), 이 관계는 $G$의 연산과 compatible하므로 $G/\ker f$는 group이다. 따라서 $f$의 canonical decomposition을 생각하면 전단사함수 $h:G/\ker f\rightarrow\operatorname{im}f$를 얻는다. 이제 임의의 $[x], [x']\in G/\ker f$에 대하여

$$h([x][x'])=h([xx'])=f(xx')=f(x)f(x')=h([x])h([x'])$$

이므로 $h$는 homomorphism이고, 따라서 isomorphism이다. 

<div class="proposition" markdown="1">

<ins id="thm2">**정리 2 (The first isomorphism theorem)**</ins> 임의의 homomorphism $f:G\rightarrow G'$에 대하여, $G/\ker f\cong \operatorname{im}f$가 항상 성립한다.

</div>

한편 [집합론, §동치관계의 예시들, 명제 7](/ko/math/set_theory/examples_of_equivalence#pp7)을 이용하면 다음 명제를 얻는다. 

<div class="proposition" markdown="1">

<ins id="pp3">**명제 3**</ins> 임의의 homomorphism $f:G\rightarrow G'$와 $G$의 normal subgroup $N$에 대하여, $f=\tilde{f}\circ p$를 만족하는 $\tilde{f}:G/H\rightarrow G'$가 존재할 필요충분조건은 $N\leq \ker f'$인 것이다. 

</div>

## The second isomorphism theorem

두 번째 isomorphism theorem을 증명하기 위해서는 다음 보조정리를 보여야 한다.

<div class="proposition" markdown="1">

<ins id="lem4">**보조정리 4**</ins> 

</div>
<details class="proof" markdown="1">
<summary>증명</summary>



</details>

<div class="proposition" markdown="1">

<ins id="thm5">**정리 5 (The second isomorphism theorem)**</ins> Group $G$의 subgroup $K$, normal subgroup $N$이 주어졌다 하자. 그럼 $K/(N\cap K)\cong NK/N$이 성립한다.

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

## The third isomorphism theorem

<div class="proposition" markdown="1">

<ins id="thm6">**정리 6 (The third isomorphism theorem)**</ins> $H$, $K$가 group $G$의 정규부분군이고, $K&lt;H$라 하자. 그럼 $H/K$는 $G/K$의 정규부분군이며 $(G/K)/(H/K)\cong G/H$가 성립한다.  

</div>
<details class="proof" markdown="1">
<summary>증명</summary>

[집합론, §동치관계의 예시들, 정의 8](/ko/math/set_theory/examples_of_equivalence#df8) 이후의 decomposition.

</details>

## The fourth isomorphism theorem

다음 정리는 아주 많이 쓰이고, 그 증명 또한 어렵지는 않지만 보여야 할 것이 너무 많아 증명을 생략하기로 한다.

<div class="proposition" markdown="1">

<ins id="thm7">**정리 7 (The fourth isomorphism theorem)**</ins> $G$가 group이고, $N$이 $G$의 정규부분군이라 하자. 그럼 *$N$을 포함하는 $G$의 부분군들의 집합*과 *$G/N$의 부분군들의 집합* 사이의 inclusion-preserving bijection이 존재한다. 뿐만 아니라, 이 bijection은 교집합이나 index, 정규부분군등의 관계를 모두 보존한다.

</div>