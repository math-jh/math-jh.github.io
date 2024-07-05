---

title: "군 동형사상"
excerpt: "동형사상 정리들"

categories: [Math / Algebraic Structures]
permalink: /ko/math/algebraic_structures/isomorphism_theorems
header:
    overlay_image: /assets/images/Math/Algebraic_Structures/Isomorphism_theorems.png
    overlay_filter: 0.5
sidebar: 
    nav: "algebraic_structures-ko"

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

으로부터 $x\sim y\iff f(x)=f(y)$임을 알 수 있다. 즉, $\sim$은 별다른 것이 아니라 함수 $f$에 의해 정의되는 동치관계이며 ([\[집합론\] §동치관계의 예시들, ⁋정의 2](/ko/math/set_theory/examples_of_equivalence#def2)), quotient group의 정의로부터 canonical map $p:G\rightarrow G/\ker f$는 homomorphism이 된다. 이제 $f$의 canonical decomposition을 생각하면 전단사함수 $h:G/\ker f\rightarrow\im f$를 얻는다. 그럼 임의의 $[x], [x']\in G/\ker f$에 대하여

$$h([x][x'])=h([xx'])=f(xx')=f(x)f(x')=h([x])h([x'])$$

이므로 $h$는 homomorphism이고, 따라서 isomorphism이다. 

<div class="proposition" markdown="1">

<ins id="thm2">**정리 2 (The first isomorphism theorem)**</ins> 임의의 homomorphism $f:G\rightarrow G'$에 대하여, $G/\ker f\cong \im f$가 항상 성립한다.

</div>

한편 [\[집합론\] §동치관계의 예시들, ⁋명제 7](/ko/math/set_theory/examples_of_equivalence#prop7)을 이용하면 다음 명제를 얻는다. 

<div class="proposition" markdown="1">

<ins id="prop3">**명제 3**</ins> 임의의 homomorphism $f:G\rightarrow G'$와 $G$의 normal subgroup $N$에 대하여, $f=\bar{f}\circ p$를 만족하는 $\bar{f}:G/N\rightarrow G'$가 존재할 필요충분조건은 $N\leq \ker f$인 것이다. 

</div>

## The second isomorphism theorem

두 번째 isomorphism theorem을 증명하기 위해서는 다음 보조정리를 보여야 한다. 다음 명제에서 $N\vee K$는 합집합 $N\cup K$를 포함하는 가장 작은 $G$의 subgroup, 즉 $\langle N\cup K\rangle$을 의미하며, $NK$는 집합

$$NK=\{nk\mid n\in N,k\in K\}$$

을 의미한다.

<div class="proposition" markdown="1">

<ins id="lem4">**보조정리 4**</ins> Group $G$의 subgroup $K$, normal subgroup $N$이 주어졌다 하자. 그럼 다음이 성립한다.

1. $N\cap K$는 $K$의 normal subgroup이다.
2. $N$은 $N\vee K$의 normal subgroup이다.
3. $NK=N\vee K=KN$이 성립한다.

</div>
<details class="proof" markdown="1">
<summary>증명</summary>

1. 임의의 $n\in N\cap K$와 $k\in K$에 대하여, $knk^{-1}$은 $K$의 원소들의 곱이므로 $K$의 원소이며, 동시에 $N$이 $G$의 normal subgroup이므로 $N$의 원소이다. 따라서 $knk^{-1}\in N\cap K$이다.
2. $N$은 $N\vee K$의 subgroup임이 자명하다. 또, 임의의 $g\in N\vee K$와 $n\in N$에 대하여 $gng^{-1}\in N$이 성립한다.
3. 임의의 $nk\in NK$에 대하여, $n,k\in N\vee K$이므로 $nk\in N\vee K$가 성립한다. 따라서 반대방향만 보이면 된다. $N$과 $K$의 원소들의 곱 $n_1k_1\cdots n_rk_r$들을 모두 포함하는 $G$의 부분집합을 생각하자. 이 집합이 subgroup인 것을 쉽게 확인할 수 있으며, 또한 이 subgroup은 $N$과 $K$를 모두 포함하므로 $N\vee K$ 또한 포함한다.[^1]  
따라서 임의의 $N\vee K$의 원소는 모두 $n_1k_1\cdots n_rk_r$의 꼴로 쓸 수 있다. 이제 $N$이 $N\vee K$의 normal subgroup이므로, $k_1n_2=n_2'k_1$을 만족하는 $n_1'\in N$이 존재한다. 이 과정을 계속해서 반복하면 $n_1k_1\cdots n_rk_r$을 $NK$의 원소의 형태로 바꾸어 쓸 수 있다.

</details>

<div class="proposition" markdown="1">

<ins id="thm5">**정리 5 (The second isomorphism theorem)**</ins> Group $G$의 subgroup $K$, normal subgroup $N$이 주어졌다 하자. 그럼 $K/(N\cap K)\cong NK/N$이 성립한다.

</div>
<details class="proof" markdown="1">
<summary>증명</summary>

우선 앞선 보조정리로부터, $N$은 $NK=N\vee K=KN$의 normal subgroup이 된다. 한편, $K\subset NK$이므로, 다음과 같은 homomorphism의 composition

$$K\overset{\iota}{\hookrightarrow}NK\overset{\pi}{\twoheadrightarrow}NK/N$$ 

을 생각할 수 있다. 그럼

$$\ker(\pi\iota)=(\pi\iota)^{-1}(e)=\iota^{-1}(\ker\pi)=\iota^{-1}(N)=K\cap N$$

이므로, $\pi\iota$에 first isomorphism theorem을 적용하면

$$K/\ker(\pi\iota)=K/(K\cap N)\cong\im(\pi\iota)$$

를 얻는다. 그런데 $NK/N$의 임의의 원소는 모두 $nkN$의 꼴이고, 적당한 $n'\in N$이 존재하여 $nk=kn'$이라 할 수 있으므로, $NK/N$의 임의의 원소 $nkN$은

$$nkN=kn'N=kN=\pi(k)=\pi(\iota(k))\in\im(\pi\iota)$$

을 만족하므로 원하는 결과를 얻는다.

</details>

## The third isomorphism theorem

<div class="proposition" markdown="1">

<ins id="thm6">**정리 6 (The third isomorphism theorem)**</ins> $H$, $K$가 group $G$의 normal subgroup이고, $K&lt;H$라 하자. 그럼 $H/K$는 $G/K$의 normal subgroup이며 $(G/K)/(H/K)\cong G/H$가 성립한다.  

</div>
<details class="proof" markdown="1">
<summary>증명</summary>

[\[집합론\] §동치관계의 예시들, ⁋정의 8](/ko/math/set_theory/examples_of_equivalence#def8) 이후의 decomposition.

</details>

## The fourth isomorphism theorem

다음 정리는 아주 많이 쓰이고, 그 증명 또한 어렵지는 않지만 보여야 할 것이 너무 많아 증명을 생략하기로 한다.

<div class="proposition" markdown="1">

<ins id="thm7">**정리 7 (The fourth isomorphism theorem)**</ins> $G$가 group이고, $N$이 $G$의 normal subgroup이라 하자. 그럼 *$N$을 포함하는 $G$의 subgroup들의 집합*과 *$G/N$의 subgroup들의 집합* 사이의 inclusion-preserving bijection이 존재한다. 뿐만 아니라, 이 bijection은 교집합이나 index, normal subgroup등의 관계를 모두 보존한다.

</div>

## 준동형사상의 coequalizer

이제 두 group homomorphism $f,g:G \rightarrow H$가 주어졌다 하자. 앞서 우리는 $f,g$의 equalizer $\Eq(f,g)$는 항상 $G$의 subgroup이 된다는 것을 살펴보았다. 이들의 coequalizer는 상황이 조금 복잡하다.

우선 coequalizer의 universal property를 생각하면, $q:H\rightarrow\CoEq(f,g)$는 $q\circ f=q\circ g$를 만족하는 것들 중 initial인 것이다. 만일 우리가 $\Set$에서 이러한 상황을 마주쳤다면 $H$ 위에 equivalence relation $\sim$을

$$f(x)\sim g(x)\qquad\text{for all $x\in G$}$$

에 의해 생성되는 relation으로 준 후, projection $H\rightarrow H/{\sim}$을 생각하면 이것이 coequalizer가 될 것이나 $\Grp$에서는 위에서 정의한 $\sim$이 $H$의 group operation과 compatible한지를 알 수 없다. 즉 다음 subset

$$S=\{f(x)g(x)^{-1}:x\in X\}$$

이 normal subgroup이 아니므로, $H/S$가 정의되지 않는다. 

이를 해결하기 위해 $\overline{S}$를 $S$의 *normal closure*, 즉 $S$를 포함하는 normal subgroup 중 가장 작은 것이라 하자. 그럼 $\overline{S}$에 의한 $H$의 quotient $H/\overline{S}$가 잘 정의된다.

<div class="proposition" markdown="1">

<ins id="prop8">**명제 8**</ins> 위와 같이 정의된 quotient $q: H \rightarrow H/\overline{S}$는 coequalizer이다.

</div>
<details class="proof" markdown="1">
<summary>증명</summary>

임의의 group homomorphism $q': G \rightarrow H'$가 존재하여 $q'\circ f=q'\circ g$를 만족한다 하자. 그럼 [보조정리 1](#lem1)에 의해 $\ker q'$는 normal subgroup이고, 조건 $q'\circ f=q'\circ g$에 의하여

$$q'(f(x))=q'(g(x))\iff q'(f(x)g(x)^{-1})=e$$

이므로 $f(x)g(x)^{-1}\in\ker q'$이 모든 $x\in g$에 대해 성립한다. 따라서, $\overline{S}$의 정의에 의해 $\overline{S}\leq\ker q'$이고, [명제 3](#prop3)을 적용하면 원하는 결과를 얻는다.

</details>

---

**참고문헌**

**[Bou]** Bourbaki, N. Algebra I. *Elements of Mathematics*. Springer. 1998.  

---

[^1]: 반대방향 포함관계가 성립하는 것 또한 쉽게 보일 수 있다.