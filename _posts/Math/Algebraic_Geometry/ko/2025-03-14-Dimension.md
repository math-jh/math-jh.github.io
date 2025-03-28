---

title: "차원"
excerpt: ""

categories: [Math / Algebraic Geometry]
permalink: /ko/math/algebraic_geometry/dimension
header:
    overlay_image: /assets/images/Math/Algebraic_Geometry/Dimension.png
    overlay_filter: 0.5
sidebar: 
    nav: "algebraic_geometry-ko"

date: 2025-03-14
last_modified_at: 2025-03-14
weight: 11

---

## 스킴의 차원

이제 우리는 scheme의 차원을 정의한다.

<div class="definition" markdown="1">

<ins id="def1">**정의 1**</ins> Scheme $X$의 *dimension<sub>차원</sub>*은 위상공간 $X$의 Krull dimension으로 정의한다. ([\[위상수학\] §차원, ⁋정의 10](/ko/math/topology/dimension#def10))

</div>

그럼 [§스펙트럼, ⁋명제 16](/ko/math/algebraic_geometry/spectrums#def16)의 Galois correspondence로부터 우리는 $\Spec A$의 scheme으로서의 차원과 $A$의 ring으로서의 차원이 같다는 것을 안다. ([\[가환대수학\] §차원, ⁋정의 1](/ko/math/commutative_algebra/Krull_dimension#def1)) 뿐만 아니라, 정의에 의하여 $\Spec A$와 $\Spec A/\mathfrak{N}(A)$가 homeomorphic하다는 것을 보일 수 있으므로 $\dim A=\dim A/\mathfrak{N}(A)$가 성립한다. 즉 reducedness는 차원에 영향을 주지 않는다. 

한편 [\[위상수학\] §차원, ⁋명제 13](/ko/math/topology/dimension#prop13)와 마찬가지 이유로 다음이 성립한다. 

<div class="proposition" markdown="1">

<ins id="prop2">**명제 2**</ins> 임의의 scheme $X$에 대하여, $\dim X=n$인 것은 $X$의 affine open covering $(U_i)$가 존재하여, 모든 $U_i$에 대하여 $\dim U_i\leq n$이고, 적어도 하나의 $i$에 대해서는 등호가 성립하는 것과 동치이다. 

</div>

한편 우리는 [§스킴 사상의 성질들, ⁋명제 14](/ko/math/algebraic_geometry/properties_of_scheme_morphisms#prop14)에서 finite morphism은 integral morphism of finite type인 것을 살펴보았으며, [§올곱, ⁋명제 14](/ko/math/algebraic_geometry/fiber_products#prop14)에서 임의의 finite morphism은 quasi-finite인 것을 살펴보았다. 일반적으로 integral morphism이지만 finite type은 아닌 morphism이 존재하며, 따라서 아직까지는 integral morphism의 fiber에 대한 이야기를 할 수가 없다.

<div class="example" markdown="1">

<ins id="ex3">**예시 3**</ins> 예를 들어 $\mathbb{Q}$의 algebraic closure $\overline{\mathbb{Q}}$를 생각하자. 그럼 $\mathbb{Q} \rightarrow \overline{\mathbb{Q}}$는 integral이므로 scheme morphism $\Spec \overline{\mathbb{Q}} \rightarrow \Spec \mathbb{Q}$는 integral이다. 

한편 [§올곱, ⁋명제 15](/ko/math/algebraic_geometry/fiber_products)에 의하여 integral morphism은 base change에 의해 보존되므로, 이를 $\Spec \overline{\mathbb{Q}} \rightarrow \Spec \mathbb{Q}$를 통해 base change를 한 $\Spec \overline{\mathbb{Q}}\otimes_\mathbb{Q}\overline{\mathbb{Q}} \rightarrow \Spec \overline{\mathbb{Q}}$도 integral이다. 그러나 $\overline{\mathbb{Q}}\otimes \overline{\mathbb{Q}}$의 prime ideal은 $\Gal(\overline{\mathbb{Q}}/\mathbb{Q})$와 일대일로 대응되므로 $\Spec\overline{\mathbb{Q}}\otimes \overline{\mathbb{Q}}$은 무한집합이고, 따라서 $\Spec \overline{\mathbb{Q}}\otimes_\mathbb{Q}\overline{\mathbb{Q}} \rightarrow \Spec \overline{\mathbb{Q}}$는 quasi-finite morphism이 아니므로 finite morphism도 아니다. 

</div>

그러나 다음이 성립한다.

<div class="proposition" markdown="1">

<ins id="prop4">**명제 4**</ins> Integral morphism $\varphi: X \rightarrow Y$의 임의의 fiber는 항상 $0$차원이다. 

</div>
<details class="proof" markdown="1">
<summary>증명</summary>

정의에 의해 $Y$의 한 점 $y$에서의 fiber는 inclusion map $\Spec \kappa(y) \rightarrow Y$에 의한 $\varphi$의 base change

$$\varphi^{-1}(y)=X\times_Y\Spec \kappa(y)$$

으로 주어지며, integral morphism은 base change에 의해 보존되므로 

$$\varphi^{-1}(y)=X\times_Y\Spec \kappa(y) \rightarrow \Spec \kappa(y)$$

는 integral morphism이며, integral morphism은 그 정의에 의해 affine morphism이므로 임의의 integral morphism $\Spec B \rightarrow \Spec \mathbb{k}$에 대하여 $\dim \Spec B=\dim B=0$임을 보이면 충분하다. 즉, 임의의 integral extension $\mathbb{k} \rightarrow B$에 대하여, $B$의 prime ideal들의 chain

$$\mathfrak{q}_1\subsetneq \mathfrak{q}_2$$

이 존재할 수 없음을 보여야 한다. 이는 [\[가환대수학\] §정수적 확장과 아이디얼, ⁋따름정리 4](/ko/math/commutative_algebra/lying_over_and_going_up#lem4)의 결과이다. 

</details>

위의 명제의 증명에서 사용한 [\[가환대수학\] §정수적 확장과 아이디얼, ⁋따름정리 4](/ko/math/commutative_algebra/lying_over_and_going_up#lem4)는 임의의 integral extension $A\hookrightarrow B$에 대해서도 성립하므로, 더 일반적으로 다음이 성립한다.

<div class="proposition" markdown="1">

<ins id="prop5">**명제 5**</ins> 임의의 integral extension $\phi:A \rightarrow B$에 대하여 

$$\dim\Spec A=\dim\Spec B$$

가 항상 성립한다. 

</div>

특히 임의의 integral domain $A$와 $A$의 normalization $\tilde{A}$에 대하여, $\Spec \tilde{A}$와 $\Spec A$의 차원은 항상 같다. 이는 더 일반적으로 scheme $X$의 normalization을 정의한 후에도 성립한다. ([##ref##](normalization))

<div class="definition" markdown="1">

<ins id="def6">**정의 6**</ins> 위상공간 $X$의 irreducible subset $Y$에 대하여, $Y$의 $X$에서의 *codimension<sub>여차원</sub>* $\codim_XY$를 $X$의 irreducible closed subset들의 strictly descending chain 

$$A_n\supsetneq A_{n-1}\supsetneq\cdots\supsetneq A_0=\cl_X(Y)$$

의 length의 supremum으로 정의한다. 

</div>

그럼 ring $A$의 prime ideal $\mathfrak{p}$의 codimension ([\[가환대수학\] §차원, ⁋정의 2](/ko/math/commutative_algebra/Krull_dimension#def2))은 $\Spec A$에서 점 $\mathfrak{p}$의 codimension과 같은 것을 확인할 수 있다. 

<div class="proposition" markdown="1">

<ins id="prop7">**명제 7**</ins> $X$의 irreducible closed subset $Y$와 $Y$의 generic point $y$에 대하여, $\codim Y=\dim \mathscr{O}_{X, y}$이 성립한다. 

</div>
<details class="proof" markdown="1">
<summary>증명</summary>

$Y$가 generic point $y$를 가지므로, 정의에 의해 $\codim_XY$와 $\codim_X\\{y\\}$가 같다. 이제 $y$를 포함하는 임의의 affine open subset $U\cong\Spec A$를 택하고, 이 isomorphism에 의해 $y\in U$가 $\mathfrak{p}_y\in \Spec A$에 대응된다 하자. 그럼  [\[위상수학\] §차원, ⁋명제 14](/ko/math/topology/dimension#prop14)로부터 우리는 $U$와 만나는 $X$의 irreducible closed subset들과 $U$의 irreducible closed subset들 사이의 일대일 대응이 존재한다는 것을 안다. 즉, $\codim_X\\{y\\}=\codim_U \mathfrak{p}_y$이다. 이제 [§스펙트럼, ⁋명제 16](/ko/math/algebraic_geometry/spectrums#prop16)으로부터 원하는 결과를 얻는다. 

</details>

더 일반적으로 우리는 [\[가환대수학\] §차원, ⁋정의 2](/ko/math/commutative_algebra/Krull_dimension#def2)에서 codimension을 정의한 후 다음의 부등식

$$\dim \mathfrak{a}+\codim \mathfrak{a}\leq \dim A$$

를 증명하였는데, 여기에서 사용한 [\[가환대수학\] §국소화, ⁋명제 8](/ko/math/commutative_algebra/localization#prop8) 대신 [\[위상수학\] §차원, ⁋명제 14](/ko/math/topology/dimension#prop14)를 사용하면 scheme $X$와 $X$의 irreducible closed subset $Y$에 대하여 다음의 부등식

$$\dim Y+\codim_XY\leq \dim X$$

이 성립하는 것을 확인할 수 있다. 그러나 마찬가지로 일반적인 경우에는 등호가 성립하지 않는다. 

## 뇌터 정규화

이제 우리는 중요한 다음 결과를 보인다.

<div class="proposition" markdown="1">

<ins id="thm8">**정리 8 (Noether normalization lemma)**</ins> 임의의 field $\mathbb{k}$와, finitely generated $\mathbb{k}$-algebra $A$가 주어졌다 하자. 만일 $A$가 integral domain이고 

$$\trdeg_\mathbb{k}\Frac(A)=n$$

이라면 $A$의 적당한 원소들 $x_1,\ldots, x_n$이 존재하여 이들이 algebraically independent이고 $A$가 finite $\mathbb{k}[x_1,\ldots, x_n]$-module이도록 할 수 있다. 

</div>
<details class="proof" markdown="1">
<summary>증명</summary>

$A$가 finitely generated $\mathbb{k}$-algebra라는 가정으로부터

$$A=\mathbb{k}[y_1,\ldots, y_m]/\mathfrak{p}$$

로 적을 수 있다. 그럼 이들 $y_1,\ldots, y_m$의 $\Frac(A)$에서의 image가 $\mathbb{k}$의 field extension으로서 $\Frac(A)$를 생성하므로 반드시 $m\geq n$이어야 한다. 

이제 만일 $m=n$이라면, $y_i$들이 정확히 원하는 원소가 되므로 더 이상 증명할 것이 없다. 이제 주어진 주장을 보이기 위해 $m>n$이라 하고, $n\leq k< m$을 만족하는 임의의 $k$에 대하여 정리가 성립한다 하자. 그럼 $m>n$이라는 가정으로부터 $y_1,\ldots, y_m$들은 algebraically dependent이다. 즉, 다음의 식

$$f(y_1,\ldots, y_m)=0$$

을 만족하는 $\mathbb{k}$-계수 $m$변수 다항식 

$$f(\x_1,\ldots, \x_m)=\sum \alpha_{d_1d_2\cdots d_m}\x_1^{d_1}\cdots\x_m^{d_m}\in \mathbb{k}[\x_1,\ldots, \x_m]\tag{$\ast$}$$

이 존재한다. 이제 정수 $r_1,\ldots, r_{m-1}$에 대하여 다음의 식

$$z_1=y_1-y_m^{r_1},\quad z_2=y_2-y_m^{r_2},\quad\ldots\quad,\quad z_{m-1}=y_{m-1}-y_m^{r_{m-1}}$$

으로 원소들 $z_1,\ldots, z_{m-1}$을 정의하자. 그럼 정의에 의해 

$$f(z_1+y_m^{r_1},\ldots, z_{m-1}+y_m^{r_{m-1}}, y_m)=0\tag{$\ast\ast$}$$

이 성립한다. 이제 식 ($\ast$)에서 $f$를 이루는 각각의 monomial $\alpha_{d_1d_2\cdots d_m}\x_1^{d_1}\cdots\x_m^{d_m}$에 

$$\x_1=z_1+y_m^{r_1},\quad \ldots\quad,\quad \x_{m-1}=z_{m-1}+y_m^{r_{m-1}},\quad \x_m=y_m$$

을 대입하여 전개하면, 그 결과는 계수가 상수항인 $y_m$의 거듭제곱

$$\alpha_{d_1d_2\cdots d_m}y_m^{r_1d_1+\cdots+r_{m-1}d_{m-1}+d_m}$$

과 $z_k$를 포함하는 그 외의 항들이 될 것이다. 이제 $r_1,\ldots, r_{m-1}$을 충분히 크게 잡으면, 이러한 형태의 항이 최고차항이 되도록 할 수 있고, 따라서 위의 등식 ($\ast\ast$)은 $y_m$이 $z_1,\ldots, z_{m-1}$에 대해 intgrally dependent임을 보여준다. 한편 $z_1,\ldots, z_{m-1}$로 생성되는 $A$의 $\mathbb{k}$-subalgebra $A'$, 즉 ($\ast\ast$)를 $y_m$의 일변수 다항식으로 보았을 때 그 계수들이 존재하는 $A$의 $\mathbb{k}$-subalgebra $A'$에 대해서는 귀납적 가정에 의해 원하는 조건을 만족하는 $x_1,\ldots, x_n\in A$들이 존재한다. 이제 $A$는 위의 논증에 의해 finite $A'$-module이고, $A'$는 귀납적 가정에 의해 finite $\mathbb{k}[x_1,\ldots, x_n]$-module이므로 원하는 결과를 얻는다.

</details>

기하적으로 $A=\mathbb{k}[y_1,\ldots, y_m]/\mathfrak{p}$라 두는 것은 $\Spec A$가 affine space $\mathbb{A}^m_\mathbb{k}$의 integral closed subscheme이라는 것과 같으므로, 위의 정리의 결과로 얻어지는 finite ring homomorphism $\mathbb{k}[x_1,\ldots, x_n] \rightarrow \mathbb{k}[y_1,\ldots, y_m]/\mathfrak{p}$는 기하적으로는 finite scheme morphism $\Spec A \rightarrow \Spec \mathbb{k}[x_1,\ldots, x_n]$을 찾는 것과 같다. 이제 finite extension $\mathbb{k}[x_1,\ldots, x_n] \rightarrow A$은 integral extension이므로 [명제 5](#prop5)에 의하여 $\dim A=\dim \mathbb{k}[x_1,\ldots, x_n]$이므로, [\[가환대수학\] §매개계, ⁋따름정리 10](/ko/math/commutative_algebra/system_of_parameters#cor10)에 의하여 다음 결과를 얻는다.

<div class="proposition" markdown="1">

<ins id="prop9">**명제 9**</ins> 임의의 field $\mathbb{k}$와, finitely generated $\mathbb{k}$-algebra $A$가 주어졌다 하자. 만일 $A$가 integral domain이라면, $\dim\Spec A=\trdeg_\mathbb{k} \Frac(A)$이 성립한다. 

</div>

위의 주장들에서 가장 중요하게 쓰인 결과는 당연히 [\[가환대수학\] §정수적 확장과 아이디얼](/ko/math/commutative_algebra/lying_over_and_going_up)의 결과들이다. 비슷한 종류의 결과인 [##ref##](going_down)을 사용하면 다음을 얻는다. 

<div class="proposition" markdown="1">

<ins id="prop10">**명제 10**</ins> 임의의 field $\mathbb{k}$와, finitely generated $\mathbb{k}$-algebra $A$가 주어졌다 하자. 만일 $A$가 integral domain이고, $f\in A$가 non-unit이라면 $\dim A/(f)=\dim A-1$이 성립한다.  

</div>

## Principal ideal theorem

앞서 우리는 임의의 affine integral $\mathbb{k}$-scheme $X=\Spec A$에 대하여, $A$의 non-unit $f$를 통해 정의된 closed subscheme $Z(f)$는 $A$보다 하나 적은 차원을 갖는다는 것을 살펴보았다. 이는 분명 유용한 결과이지만, 다음과 같이 더 일반적인 경우에도 그 결과를 살펴볼 수 있다.

<div class="proposition" markdown="1">

<ins id="prop11">**명제 11**</ins> Locally noetherian scheme $X$와 $X$ 위의 함수 $f$에 대항, $Z(f)$의 irreducible component는 codimension $0$이거나 codimension $1$이다. 

</div>
<details class="proof" markdown="1">
<summary>증명</summary>

[\[가환대수학\] §차원, ⁋정리 6](/ko/math/commutative_algebra/Krull_dimension#thm6)

</details>

