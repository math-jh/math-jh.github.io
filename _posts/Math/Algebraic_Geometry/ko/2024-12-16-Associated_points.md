---

title: "동반점"
excerpt: ""

categories: [Math / Algebraic Geometry]
permalink: /ko/math/algebraic_geometry/associated_points
header:
    overlay_image: /assets/images/Math/Algebraic_Geometry/Associated_points.png
    overlay_filter: 0.5
sidebar: 
    nav: "algebraic_geometry-ko"

date: 2024-12-16
last_modified_at: 2024-12-16
weight: 15

---

## 동반소아이디얼

이번 글에서 우리는 가환대수학에서 정의했던 개념인 associated prime ideal의 기하적인 의미에 대해 살펴본다. 이에 대한 정의와 성질들은 [\[가환대수학\] §동반소아이디얼](/ko/math/commutative_algebra/associated_primes)에서 찾을 수 있지만, 편의를 위하여 다음과 같이 나열해둔다.

<div class="definition" markdown="1">

<ins id="def1">**정의 1**</ins> Ring $A$와 $A$-module $M$에 대하여, $A$의 prime ideal $\mathfrak{p}$가 $M$의 *associated prime ideal<sub>동반소아이디얼</sub>*이라는 것은 어떠한 $x\in M$에 대해 $\mathfrak{p}=\ann(x)$인 것이다. Associated prime들의 모임을 $\Ass M$으로 적는다. 

</div>

$\Ass(M)$의 원소들 가운데, 포함관계에 대해 minimal한 것들을 *isolated prime*이라 부르고, 그렇지 않은 associated prime들을 *embedded prime*이라 부른다. 

<div class="proposition" markdown="1">

<ins id="thm2">**정리 2**</ins> Noetherian ring $A$와 finitely generated $A$-module $M$에 대하여, 다음이 성립한다. 

1. Associated prime ideal들의 모임 $\Ass M$은 공집합이 아닌 유한집합이며, 각각의 associated prime들은 $\ann M$을 포함한다. 거꾸로, $\ann M$을 포함하는 prime ideal들의 모임 중, 포함관계에 대해 minimal한 prime ideal들은 모두 $\Ass M$에 포함된다.
2. Associated prime들의 합집합은 $0$과, $M$의 모든 zero-divisor들의 모임으로 이루어진다.
3. 다음의 식
    
    $$\Ass_{S^{-1}A}S^{-1}M=\{\mathfrak{p}S^{-1}A: \mathfrak{p}\in\Ass M, \mathfrak{p}\cap S=\emptyset\}$$

    이 성립한다. 
4. 다음의 homomorphism
    
    $$M \rightarrow \prod_{\mathfrak{p}\in \Ass M} M_\mathfrak{p}$$

    은 injective이다. 

</div>

## 동반점의 정의

이제 이를 기하학적으로 해석하는 작업을 시작해보자. 우선 다음을 정의한다.

<div class="definition" markdown="1">

<ins id="def3">**정의 3**</ins> Scheme $X$와 $X$ 위에 정의된 quasi-coherent sheaf $\mathscr{F}$를 생각하자. 그럼 점 $x\in X$가 $\mathscr{F}$의 *associated point<sub>동반점</sub>*이라는 것은 $\mathfrak{m}\_x$가 $\mathscr{O}\_{X,x}$-module $\mathscr{F}\_x$의 associated prime ideal인 것이다. $\mathscr{F}$의 associated point들의 모임을 $\Ass(\mathscr{F})$로 쓰고, 특별히 $\mathscr{F}=\mathscr{O}_X$인 경우에 $\mathscr{O}_X$의 associated point들을 간단히 $X$의 associated point라 부른다. 

</div>

특히 $X$가 locally noetherian scheme이고 $\mathscr{F}$가 coherent인 경우를 생각하자. 그럼 $X$의 적당한 affine open subset $U=\Spec A$가 존재하여 $A$가 noetherian ring이고, $M=\Gamma(U, \mathscr{F})$는 finitely generated $A$-module이도록 할 수 있다. 특히 [정리 2](#thm2)의 모든 결과가 성립하며, 앞으로의 논의에서 noetherian ring $A$와 finitely generated $A$-module $M$은 항상 이러한 방식으로 얻어진 것이라 생각하는 것이 기하학적인 직관에 유용하다. 이 논증을 정리하면 다음과 같다.

<div class="proposition" markdown="1">

<ins id="lem4">**보조정리 4**</ins> Locally noetherian scheme $X$와 그 위에 정의된 coherent sheaf $\mathscr{F}$가 주어졌다 하자. 그럼 임의의 affine open subset $U=\Spec A$와, $x\in U$에 대응되는 $\mathfrak{p}$에 대하여 다음 동치관계

$$\mathfrak{p}\in\Ass M \iff x\in \Ass \mathscr{F}$$

가 성립한다.

</div>

이에 대한 증명은 [정리 2](#thm2)의 세 번째 결과로부터 자명하다. 추가적인 직관을 위해 다음을 정의하자.

<div class="definition" markdown="1">

<ins id="def5">**정의 5**</ins> Scheme $X$ 위에 정의된 quasi-coherent sheaf $\mathscr{F}$에 대하여, $\mathscr{F}$의 *support<sub>지지집합</sub>*는 다음 식

$$\supp \mathscr{F}=\{x\in X: \mathscr{F}_x\neq 0\}$$

으로 정의되는 집합이다. 또, 임의의 global section $s\in \Gamma(X, \mathscr{F})$에 대하여, $s$의 *support<sub>지지집합</sub>*는 다음 식

$$\supp(s)=\{x\in X: s_x\neq 0\text{ in $\mathscr{F}_x$}\}$$

으로 주어진다.

</div>

정의에 의해 어떠한 $x\in X$에 대해서 $s_x=0$이 성립하기 위해서는 적당한 열린근방이 존재하여 이 위에서는 $s$가 항등적으로 $0$이 되어야 하므로, $\supp(s)$는 반드시 닫힌집합이어야 한다는 것을 안다. 

이제 [정의 3](#def3) 이후에 생각한 상황을 local하게 보아, $X=\Spec A$가 noetherian ring의 스펙트럼이고 $M$이 finitely generated $A$-module이 되어, $\widetilde{M}$이 $X$ 위의 coherent sheaf가 되는 상황을 생각하자. 그럼 한 점 $\mathfrak{p}$에 대해 $\mathscr{O}\_{X,x}$-module $\widetilde{M}\_\mathfrak{p}$은 [§준연접가군층, ⁋명제 3](/ko/math/algebraic_geometry/quasicoherent_sheaves#prop3)에 의하여 $A\setminus \mathfrak{p}$에 속하는 원소들을 역원으로 추가하여 얻어지는 것이다. 따라서 임의의 $s\in M=\Gamma(X, \widetilde{M})$에 대하여,

$$\text{$s_\mathfrak{p}\neq 0$ in $M_\mathfrak{p}$} \iff \text{$as\neq 0$ for any $a\in A\setminus \mathfrak{p}$}\iff\text{$\mathfrak{p}$ contains $\ann(s)$}$$

이 성립하며, 거꾸로 $\ann(s)$를 포함하는 임의의 prime ideal은 반드시 $\supp(s)$에 속한다. ([\[가환대수학\] §국소화, ⁋명제 5](/ko/math/commutative_algebra/localization#prop5)) 일반적으로 $\supp(s)$에 속하는 임의의 prime ideal이 associated prime ideal이 되는 것은 아니지만, $\ann(s)$를 포함하는 prime ideal 중 minimal한 것들은 associated prime ideal이다. 한편 irreducible closed subset과 prime ideal들 사이에는 포함관계를 뒤집는 일대일대응이 존재하므로, 이를 다시 말하면 다음과 같다.

<div class="proposition" markdown="1">

<ins id="lem6">**보조정리 6**</ins> Noetherian scheme $X=\Spec A$와 그 위에 정의된 coherent sheaf $\widetilde{M}$에 대하여, $\widetilde{M}$의 associated point들은 정확하게 어떠한 $s\in M$의 support $\supp(s)$의 irreducible component의 generic point에 해당한다.

</div>

예를 들어, integral domain $A$의 스펙트럼 $\Spec A$의 associated point는 오직 $(0)$ 뿐이다. 

특별히 $M=A$인 경우를 생각하자. 그럼 $\Spec A$를 $1$의 support로 보아 위의 보조정리를 적용하면 우리는 $\Spec A$의 irreducible component들의 generic point들은 모두 $\Spec A$의 associated point가 되는 것을 안다. 더 일반적으로 다음이 성립한다.

<div class="proposition" markdown="1">

<ins id="prop7">**명제 7**</ins> Locally noetherian scheme $X$와 그 위에 정의된 coherent sheaf $\mathscr{F}$를 생각하자. 그럼 $\supp \mathscr{F}$의 irreducible component들의 generic point들은 $\mathscr{F}$의 associated point들이다.

</div>

이들 irreducible component들의 generic point들은 isolated prime에 대응되므로, associated point들 가운데 irreducible component들의 generic point가 아닌 것들을 *embedded point*라 부르면 적절할 것이다. 

이제 [정리 2](#thm2)의 두 번째 결과를 기하적인 언어로 옮기면 다음과 같다.

<div class="proposition" markdown="1">

<ins id="prop8">**명제 8**</ins> [보조정리 6](#lem6)의 상황에서, $a\in A$가 $M$의 zero-divisor인 것은 $a$가 $M$의 어떠한 associated point $\mathfrak{p}$에서 vanish하는 것과 동치이다.

</div>
<details class="proof" markdown="1">
<summary>증명</summary>

이는 $a$가 $\mathfrak{p}$에서 vanish하는 것이 정확히 정의에 의해 $a\in \mathfrak{p}$라는 것이므로, [정리 2](#thm2)의 두 번째 결과를 바로 사용할 수 있다. 

</details>

마지막으로 [정리 2](#thm2)의 네 번째 결과를 보자. 이는 $M$을 살펴보기 위해서는 $M$의 associated point들에서만 어떤 일이 일어나는지를 살펴보는 것으로 충분하다는 것을 보여준다. 특히, 임의의 locally noetherian scheme $X$와 open subset $U$에 대하여

$$\Gamma(U, \mathscr{F})\rightarrow \prod_{\text{\scriptsize associated $x$ in $U$}} \mathscr{F}_x\tag{$\ast$}$$

이 injective가 된다. 이러한 종류의 사실을 중요하게 사용했던 것은 variety $X$ 위의 임의의 점 $x\in X$에서의 stalk들을 항상 function field $K(X)$의 원소로 생각할 수 있다는 사실을 증명할 때였는데, 마찬가지 일을 이 경우에도 할 수 있다.

<div class="definition" markdown="1">

<ins id="def9">**정의 9**</ins> Locally noetherian scheme $X$와 그 위에 정의된 coherent sheaf $\mathscr{F}$를 생각하자. 그럼 $\mathscr{F}$에서 값을 가지는 *rational function*은 $\mathscr{F}$의 모든 associated point를 포함하는 적당한 열린집합 $U$에 대하여, 위의 injection $(\ast)$에 대한 $\Gamma(U, \mathscr{F})$의 image의 원소들을 의미한다. 만일 점 $x\in X$에 대하여, 열린근방 $U$가 존재하여 rational function $f$가 $U$ 위에서 정의되도록 할 수 있다면 $f$가 $x$에서 *regular*라 부른다. 모든 점에서 regular인 rational function을 *regular function*이라 부른다. 

</div>