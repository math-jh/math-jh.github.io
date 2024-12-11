---

title: "스킴 사상의 성질들"
excerpt: ""

categories: [Math / Algebraic Geometry]
permalink: /ko/math/algebraic_geometry/properties_of_scheme_morphisms
header:
    overlay_image: /assets/images/Math/Algebraic_Geometry/Properties_of_scheme_morphisms.png
    overlay_filter: 0.5
sidebar: 
    nav: "algebraic_geometry-ko"

date: 2024-11-27
last_modified_at: 2024-11-27
weight: 5

---

## 점들의 함자

[§스펙트럼, ⁋예시 7](/ko/math/algebraic_geometry/spectrums#ex7) 이후에 우리는 임의의 affine scheme $\Spec A$와 한 점 $\mathfrak{p}$에 대하여, $\Spec \kappa(\mathfrak{p}) \rightarrow \Spec A$가 이 점 $\mathfrak{p}$에 대응되는 scheme morphism임을 살펴보았다. 다음 예시에서는 $\kappa(\mathfrak{p})$ 대신 다른 scheme을 넣어서 어떠한 일이 일어나는지 살펴본다. 

<div class="example" markdown="1">

<ins id="ex1">**예시 1**</ins> Affine scheme $\Spec \mathbb{Z}[\x_1,\ldots, \x_n]/(f_1,\ldots, f_r)$에 대하여, scheme morphism 

$$\Spec \mathbb{Q} \rightarrow \Spec \frac{\mathbb{Z}[\x_1,\ldots, \x_n]}{(f_1,\ldots, f_r)}$$

은 다음의 ring homomorphism

$$\mathbb{Z}[\x_1,\ldots, \x_n]/(f_1,\ldots, f_r) \rightarrow \mathbb{Q}$$

와 같다. 이 ring homomorphism은 다시 ring homomorphism

$$\mathbb{Z}[\x_1,\ldots, \x_n] \rightarrow \mathbb{Q}; \qquad \x_i\mapsto x_i$$

들 가운데 다음 조건들

$$f_1(x_1,\ldots, x_n)=\cdots=f_r(x_1,\ldots, x_n)=0$$

을 만족하는 ring homomorphism이 된다. 즉, scheme morphism

$$\Spec \mathbb{Q} \rightarrow \Spec \frac{\mathbb{Z}[\x_1,\ldots, \x_n]}{(f_1,\ldots, f_r)}$$

은 정수계수의 다항식들 $f_1,\ldots, f_r$들의 유리수 해에 일대일로 대응된다.

</div>

이로부터 더 일반적으로 다음의 정의를 내릴 수 있다.

<div class="definition" markdown="1">

<ins id="def2">**정의 2**</ins> 주어진 scheme $X$에 대하여, scheme $S$의 *$X$-valued point*를 집합 $S(X)=\Hom_\Sch(X, S)$으로 정의한다.

</div>

이 정의는 [\[범주론\] §표현가능한 함자, ⁋정리 3](/ko/math/category_theory/representable_functors#thm3)과 마찬가지 맥락으로, 우리는 임의의 scheme $S$에 대한 정보가 functor

$$h^S:\Sch^\op \rightarrow \Set;\quad X\mapsto S(X)=\Hom_\Sch(X,S)$$

에 담겨있다는 철학을 가지고 있으며, 이는 곧 $S$의 임의의 scheme-valued point를 살펴보아 $S$에 대한 정보를 복원할 수 있다는 것을 의미한다. 뿐만 아니라, 임의의 scheme은 affine scheme들을 붙여 만들어지므로 affine scheme-valued point만 보는 것으로 충분하다. 

## 스킴의 사상들이 갖는 성질들

한편, $\Hom_\Sch(X,S)$의 원소들은 slice category $\Sch_{/S}$의 대상들로 이해할 수 있다. ([\[범주론\] §범주, ⁋예시 13](/ko/math/category_theory/categories#ex13)) Category $\cRing$이 initial object $\mathbb{Z}$를 갖는 것으로부터 $\Sch$이 terminal object $\Spec \mathbb{Z}$를 갖는다는 것을 확인할 수 있으므로, $\Sch$를 자연스럽게 $\Sch_{/\Spec \mathbb{Z}}$으로 볼 수 있다. 

Grothendieck의 철학은 스킴들의 성질을 그대로 보는 것보다, 이 성질들을 scheme morphism에 대한 성질로 보는 것이 더 낫다는 것이다. 가령 다음을 정의한다. 

<div class="definition" markdown="1">

<ins id="def3">**정의 3**</ins> Scheme morphism $f:X \rightarrow S$가 *quasi-compact*인 것은 $S$의 임의의 quasi-compact open subset $V$에 대하여 $f^{-1}(V)$가 quasi-compact인 것이다. 

</div>

<div class="proposition" markdown="1">

<ins id="prop4">**명제 4**</ins> 다음이 모두 동치이다.

1. $f:X \rightarrow S$가 quasicommpact이다. 
2. $S$의 임의의 affine open subset의 preimage가 quasi-compact이다.
3. $S$의 affine open covering $(V_i)$가 존재하여, $f^{-1}(V_i)$가 모두 quasi-compact이다.

</div>
<details class="proof" markdown="1">
<summary>증명</summary>

두 번째와 세 번째 조건이 동치임은 [§스킴의 성질들, ⁋보조정리 10](/ko/math/algebraic_geometry/properties_of_schemes#lem10)에 의해 얻어진다. 

한편, 임의의 open affine subsubset은 quasi-compact이므로, 만일 첫째 조건이 만족된다면 이들 조건이 따라나오는 것은 자명하다. ([§스킴의 성질들, ⁋예시 1](/ko/math/algebraic_geometry/properties_of_schemes#ex1))

반대로 이들 조건이 만족된다 하면, 임의의 quasi-compact open subset $V$가 주어졌을 때, 이를 덮는 affine open covering을 잡고 quasi-compactness를 사용하여 이들 중 유한 개를 추려낸 후, 2번 조건을 사용하면 충분하다. 

</details>

특히 $S=\Spec \mathbb{Z}$인 경우, $f:X \rightarrow\Spec \mathbb{Z}$에 의한 $\Spec \mathbb{Z}$의 preimage는 $X$이므로 $X$가 [§스킴의 성질들, ⁋정의 2](/ko/math/algebraic_geometry/properties_of_schemes#def2)의 센스에서 quasi-compact인 것과 $f:X \rightarrow \Spec \mathbb{Z}$가 quasi-compact인 것이 동치이다. 

이제 우리는 scheme morphism의 성질들을 정의한다. 그 중 일부는 위의 예시와 마찬가지로 앞선 글에서 살펴보았던 것을 relative하게 적은 것이다.

우선 quasi-compactness와 같이 사용하는 정의로는 다음의 *quasi-seperatedness*가 있다. 이 또한 quasi-compactness와 마찬가지로 위상적인 성질이다.

<div class="definition" markdown="1">

<ins id="def5">**정의 5**</ins> Scheme $X$가 *quasi-separated*인 것은 $X$의 임의의 두 quasi-compact open subset의 교집합이 quasi-compact인 것이다. Scheme morphism $f:X \rightarrow S$가 *quasi-separated*인 것은 임의의 affine open subset $V\subseteq S$에 대하여 $f^{-1}(V)$가 quasi-separated인 것이다.

</div>

Quasi-separatedness 또한 quasi-compactness와 마찬가지로 affine local on target이다. ([명제 4](#prop4)) 즉, scheme morphism $f:X \rightarrow S$가 quasi-separated인 것은 $S$의 affine open covering $(V_i)$가 존재하여, $f^{-1}(V_i)$가 모두 quasi-separated인 것과 동치이다. 역시 이에 대한 증명 또한 [§스킴의 성질들, ⁋보조정리 10](/ko/math/algebraic_geometry/properties_of_schemes#lem10)를 사용하면 쉽게 얻어진다. 

뿐만 아니라, scheme이 affine인 것 또한 다음과 같이 relative한 방식으로 적을 수 있다. 

<div class="definition" markdown="1">

<ins id="def6">**정의 6**</ins> Scheme morphism $f:X \rightarrow S$가 *affine*인 것은 $S$의 임의의 affine open subset $V$에 대하여 $f^{-1}(V)$가 affine인 것이다.

</div>

이 정의가 affine-local on target인 것은 앞의 두 정의와 비교하여 덜 자명하지만, 이에 대한 증명은 생략하기로 한다. **[Vak]**에서는 이를 다음의 보조정리를 사용하여 보인다.

<div class="proposition" markdown="1">

<ins id="lem7">**보조정리 7**</ins> $X$가 quasi-compact, quasi-separated scheme이라면 임의의 $s\in\Gamma(X, \mathscr{O}_X)$에 대하여 $\Gamma(X, \mathscr{O}_X)_s \rightarrow \Gamma(X_s, \mathscr{O}_X)$가 isomorphism이다. 

</div>

여기서 $X_s$는

$$X_s=\{x\in X:\text{$s_x\neq 0$ in $\mathscr{O}_{X,x}$}\}$$

으로 정의되는 열린집합이다. 또, 다음을 정의한다.

<div class="definition" markdown="1">

<ins id="def8">**정의 8**</ins> Scheme morphism $f:X \rightarrow S$가 *finite*인 것은 $f$가 affine morphism이고, $S$의 임의의 affine open subset $V=\Spec B$에 대하여, $f^{-1}(V)=\Spec A$라 하였을 때 $A$가 $B$-module로서 finitely generated인 것이다. 

</div>

그럼 이 성질 또한 마찬가지로 [§스킴의 성질들, ⁋보조정리 10](/ko/math/algebraic_geometry/properties_of_schemes#lem10)의 두 조건을 만족하여 affine-local on target이 된다. 

<div class="example" markdown="1">

<ins id="ex9">**예시 9**</ins> Ring homomorphism

$$\mathbb{k}[\x] \rightarrow \mathbb{k}[\y];\qquad \x\mapsto \y^2$$

에 의해 유도되는 scheme morphism $\Spec \mathbb{k}[\y] \rightarrow \Spec \mathbb{k}[\x]$는 finite이다. 이는 $\mathbb{k}[\y]$가 $\mathbb{k}[\x]$-module로서 두 원소 $1$과 $\y$에 의해 생성되기 때문이다.

</div>

기하적인 직관으로는 scheme morphism이 finite인 것은 이 scheme morphism의 fiber가 유한한 것이라고 생각할 수 있다. 이를 설명하기 위해서는 scheme morphism의 fiber를 정의해야 하므로, 잠시 뒤로 미뤄둔다. 한편 [\[가환대수학\] §정수적 확장, ⁋명제 2](/ko/math/commutative_algebra/integral_extension#def2)를 생각하면 임의의 ring $B$에 대하여, $B$의 integral extension $A$는 항상 $B$-module로서 finitely generated이다. 이로부터 [정의 8](#def8)보다 다소 약한 다음 정의를 얻는다.

<div class="definition" markdown="1">

<ins id="def10">**정의 10**</ins> Scheme morphism Scheme morphism $f:X \rightarrow S$가 *integral*인 것은 $f$가 affine morphism이고, $Y$의 임의의 affine open subset $V=\Spec B$에 대하여, $f^{-1}(V)=\Spec A$라 하였을 때 $A$가 $B$의 integral extension인 것이다. 

</div>

어렵지 않게 integral morphism도 affine-local on target임을 확인할 수 있다. 

[정의 8](#def8)을 약화시키는 또 다른 방법 중 하나는 다음과 같다.

<div class="definition" markdown="1">

<ins id="def11">**정의 11**</ins> Scheme morphism $f:X \rightarrow S$가 *locally of finite type*인 것은 $S$의 임의의 affine open subset $V=\Spec B$와, $f^{-1}(V)$의 임의의 affine open subset $U=\Spec A$에 대하여 ring homomorphism $B \rightarrow A$가 $A$를 (algebra로서) finitely generated $B$-algebra로 만드는 것이다. Quasi-compact scheme morphism of locally finite type을 scheme morphism *of finite type*이라 부른다.

</div>

역시 이 성질 또한 affine-local on target임을 확인할 수 있다. 기하적인 직관으로는 scheme morphism이 finite type인 것은 그 fiber가 finite-dimension인 것이다. 아직 scheme morphism의 fiber도, scheme의 차원도 정의하지 않았지만 앞선 직관을 같이 받아들인다면 finite morphism은 finite type인 것을 납득할 수 있으며, 대수적인 증명 또한 자명하다. 더 나아가 다음이 성립한다.

<div class="proposition" markdown="1">

<ins id="prop12">**명제 12**</ins> Scheme morphism $f:X \rightarrow S$가 finite인 것과, $f$가 integral of finite type인 것이 동치이다.

</div>
<details class="proof" markdown="1">
<summary>증명</summary>

이는 위에서 말로만 언급한 ''finite$\Rightarrow$finite type''의 대수적인 증명, 즉 $B$-module로서 finitely generated이면 $B$-algebra로서 finitely generated라는 것보다 아주 조금만 더 증명하면 된다. 

$A$가 $B$-algebra로서 $a$에 의해 생성되었다 하자. 그럼 $1,a,\ldots$가 $A$를 $B$-module로서 생성하며 [\[가환대수학\] §정수적 확장, ⁋명제 2](/ko/math/commutative_algebra/integral_extension#def2)에 의하여, 이들 중 $1,a,\ldots, a^n$이 $A$를 $B$-module로 생성한다. 이제 나머지 부분은 $A$의 $B$-algebra로서의 generator들의 개수에 대한 귀납법으로 증명하면 된다.

</details>

Quasifinite? 7.4?
