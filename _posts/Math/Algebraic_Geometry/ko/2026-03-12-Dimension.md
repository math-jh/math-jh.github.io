---
title: "차원"
excerpt: "Dimension of algebraic varieties"

categories: [Math / Algebraic Geometry]
permalink: /ko/math/algebraic_geometry/dimension
sidebar: 
    nav: "algebraic_geometry-ko"

header:
    overlay_image: /assets/images/Math/Algebraic_Geometry/Dimension.png
    overlay_filter: 0.5

date: 2026-03-12
last_modified_at: 2026-03-22
weight: 5

---

기하학에서 차원은 가장 기본적인 불변량 중 하나이다. 대수기하학에서도 차원은 마찬가지로 중요하며, 이를 정의하는 여러 가지 동등한 방법이 존재한다. 이 글에서 우리는 variety의 차원을 정의하는 여러 방법을 살펴본다. 

## 위상공간으로서의 차원

Algebraic variety는 이미 위상공간이므로, [\[위상수학\] §차원, ⁋정의 10](/ko/math/topology/dimension#def10)을 사용하여 $$X$$의 차원을 irreducible closed subset들의 strictly descending chain의 length의 supremum으로 정의할 수 있다. 

<div class="example" markdown="1">

<ins id="ex1">**예시 1**</ins> $$\mathbb{A}^1$$에서 닫힌집합들은 $$\mathbb{A}^1$$ 전체와 유한집합들뿐이다. 따라서 가장 긴 chain은 $$\mathbb{A}^1 \supsetneq \{p\} \supsetneq \emptyset$$이며, 이는 length $$2$$ chain이므로 $$\mathbb{A}^1$$은 이 정의에 따르면 $$1$$차원이 된다.

</div>

이 정의는 순수하게 위상적인 관점에서 차원을 정의한다는 장점이 있다. 그러나 실제로 계산을 위해서는 irreducible closed subset들의 chain을 모두 알아야하므로 그렇게 효율적이지는 않다. 

## Affine variety의 차원

한편 우리는 이미 algebraic variety와 그 위에 정의된 함수들 사이의 관계가 아주 긴밀하다는 것을 알고 있다. 그렇다면, algebraic variety 위의 함수들의 대수구조가 차원에 대한 정보를 담고있다고 하여도 그렇게 놀라운 일은 아닐 것이다. 이러한 관점을 통해 접근하려면 그 coordinate ring $$\mathbb{K}[X]$$가 깔끔하게 주어지는 *affine* variety의 경우를 보는 것이 좋을 것이다. 

<div class="proposition" markdown="1">

<ins id="prop2">**명제 2**</ins> Affine variety $$X$$의 차원은 coordinate ring $$\mathbb{K}[X]$$의 Krull dimension과 같다. ([\[가환대수학\] §차원, ⁋정의 1](/ko/math/commutative_algebra/Krull_dimension#def1))

</div>

<details class="proof" markdown="1">
<summary>증명</summary>

[§아핀다양체, ⁋명제 12](/ko/math/algebraic_geometry/affine_varieties#prop12)로부터 affine variety의 irreducible closed subset과 $$\mathbb{K}[X]$$의 prime ideal 사이의 일대일대응이 존재한다. 

</details>
<div class="proposition" markdown="1">

<ins id="cor3">**따름정리 3**</ins> $$\dim \mathbb{A}^n = n$$이다.

</div>

<details class="proof" markdown="1">
<summary>증명</summary>

[\[가환대수학\] §매개계, ⁋정리 10](/ko/math/commutative_algebra/system_of_parameters#cor10)

</details>

한편, 우리는 임의의 prime ideal $$\mathfrak{p}\subset \mathbb{K}[\x_1,\ldots, \x_n]$$에 대하여 다음의 식

$$\dim \mathbb{K}[\x_1,\ldots, \x_n]/\mathfrak{p}+\codim \mathfrak{p}=\dim \mathbb{K}[\x_1,\ldots, \x_n]=n\tag{$\ast$}$$

이 성립하는 것을 안다. ([\[가환대수학\] §정칙국소환, ⁋명제 4](/ko/math/commutative_algebra/regular_local_rings#prop4)) 여기서 codimension $$\mathfrak{p}$$는 [\[가환대수학\] §차원, ⁋정의 2](/ko/math/commutative_algebra/Krull_dimension#def2)에서 정의된 것으로, $$\mathfrak{p}$$에 포함되는 prime ideal들의 chain의 길이의 supremum이며, 기하적으로는 $$X=Z(\mathfrak{p})$$를 포함하는 $$\mathbb{A}^n$$의 closed subvariety들의 chain의 길이의 supremum이다. 기하적으로 우리는 $$\dim \mathbb{K}[\x_1,\ldots, \x_n]/\mathfrak{p}$$이 $$Z(\mathfrak{p})$$의 차원인 것을 알고 있으므로, 이를 통해 ($\ast$)에 기하적인 의미를 부여할 수 있다. 

## Projective variety의 차원

문제는 projective variety로 넘어가면서부터 발생한다. $$\mathbb{P}^n$$의 global function은 오직 상수함수들 뿐이었음을 기억하자. 이러한 상황에서 projective variety의 차원을 정의하기 위해서는 affine chart를 잡으면 된다. 즉 $$X\subset \mathbb{P}^n$$이 주어졌을 때, $$\mathbb{P}^n$$의 affine open chart $$U_i$$를 택한 후, $$X_i=X\cap U_i$$의 affine variety로서의 차원을 생각하면 된다. 그러나 이 정의를 위해서는 임의의 열린집합의 차원이 원래 variety의 차원과 같다는 것을 보여야하므로 아직은 이를 정의로 택할 수 없다. 그 대신 우리는 $$X$$의 *affine cone* $$C(X)$$를 이용한다.

Projective variety $$X\subseteq \mathbb{P}^n$$에 대하여, affine cone $$C(X)\subseteq \mathbb{A}^{n+1}$$은 $$X$$를 정의하는 homogeneous ideal을 $$\mathbb{K}[\x_0,\ldots, \x_n]$$의 ideal로 봤을 때 이것이 정의하는 $$\mathbb{A}^{n+1}$$의 affine variety이다. 즉 $$X$$가 정의하는 homogeneous ideal $$I(X)$$에 대하여, ring $$S(X)$$를

$$S(X)=\mathbb{K}[\x_0,\ldots, \x_n]/I(X)$$

으로 정의하면 이것이 affine cone의 coordinate ring이 되는 것이다. Projective variety의 차원을 계산하기 위해 핵심적인 것은 다음의 결과이다. 

<div class="proposition" markdown="1">

<ins id="prop4">**명제 4**</ins> Projective variety $$X \subseteq \mathbb{P}^n$$에 대하여 $$\dim X = \dim S(X) - 1$$이다.

</div>

이는 graded ring에서의 계산을 통해 보일 수 있다. 특히 $$\dim C(X) = \dim X + 1$$이며, 이로부터 다음을 얻는다. 

<div class="proposition" markdown="1">

<ins id="prop5">**명제 5**</ins> $$\dim \mathbb{P}^n = n$$이다.

</div>

<details class="proof" markdown="1">
<summary>증명</summary>

$$\mathbb{P}^n$$의 cone은 $$\mathbb{A}^{n+1}$$이고 $$\dim \mathbb{A}^{n+1} = n+1$$이므로 $$\dim \mathbb{P}^n = (n+1) - 1 = n$$이다.

</details>

## 초곡면의 차원

Hypersurface는 단일 다항식의 zero set으로 정의되는 다양체이다. 직관적으로, 하나의 식을 추가하는 것은 하나의 제약조건을 주는 것과 같으므로 차원을 하나 줄이게 될 것이다. 

<div class="proposition" markdown="1">

<ins id="prop6">**명제 6**</ins> Irreducible polynomial $$f \in \mathbb{K}[\x_1, \ldots, \x_n]$$에 대해, irreducible hypersurface $$Z(f) \subset \mathbb{A}^n$$의 차원은 $$n - 1$$이다.

</div>

<details class="proof" markdown="1">
<summary>증명</summary>

$$f$$가 irreducible이므로 $$(f)$$는 prime ideal이고, 따라서 $$Z(f)$$의 coordinate ring은 $$\mathbb{K}[\x_1, \ldots, \x_n]/(f)$$이다. 이제 $$\mathbb{K}[\x_1, \ldots, \x_n]$$에서 $$(f)$$의 codimension—가 1임을 보이자. $$(0) \subsetneq (f)$$는 길이 1의 chain이므로 $$\codim(f) \ge 1$$이다. 반면, UFD $$\mathbb{K}[\x_1, \ldots, \x_n]$$에서 codimension 1인 prime ideal은 모두 principal prime ideal이므로, $$(f)$$ 사이에 다른 prime ideal이 존재할 수 없다. 따라서 $$\codim(f) = 1$$이고,

$$\dim \mathbb{K}[\x_1, \ldots, \x_n]/(f) = \dim \mathbb{K}[\x_1, \ldots, \x_n] - \codim(f) = n - 1$$

이다. 일반적으로 regular local ring $$R$$과 prime ideal $$\mathfrak{p}$$에 대하여 $$\dim R/\mathfrak{p} = \dim R - \codim(\mathfrak{p})$$가 성립한다. ([\[가환대수학\] §정칙국소환, ⁋명제 4](/ko/math/commutative_algebra/regular_local_rings#prop4))

</details>

## 함수체를 통한 차원

차원을 정의하는 또 다른 방법은 함수체를 사용하는 것이다. 함수체 $$\mathbb{K}(X)$$는 다양체의 generic point에서의 정보를 담고 있으며, birational invariant이기도 하다. 다음 명제 또한 대수적인 사실로부터 유도된다.

<div class="proposition" markdown="1">

<ins id="prop7">**명제 7**</ins> Variety $$X$$의 차원은 함수체 $$\mathbb{K}(X)$$의 $$\mathbb{K}$$ 위에서의 transcendence degree와 같다.

</div>

<div class="example" markdown="1">

<ins id="ex8">**예시 8**</ins> 다음은 function field를 통한 차원 계산의 예시들이다.

1. $$\mathbb{K}(\mathbb{A}^n) = \mathbb{K}(x_1, \ldots, x_n)$$이고, $$x_1, \ldots, x_n$$은 $$\mathbb{K}$$ 위에서 algebraically independent이므로 $$\dim \mathbb{A}^n = n$$이다. 
2. $$\mathbb{K}(V(\y - \x^2)) = \mathbb{K}(x)$$이고, $$x$$는 $$\mathbb{K}$$ 위에서 algebraically independent이므로 $$\dim V(\y - \x^2) = 1$$이다. 이는 parabola가 곡선이라는 직관과 일치한다.
3. $$\mathbb{K}(\mathbb{P}^n) = \mathbb{K}(\x_1/\x_0, \ldots, \x_n/\x_0)$$이고, $$\x_1/\x_0, \ldots, \x_n/\x_0$$는 $$\mathbb{K}$$ 위에서 algebraically independent이므로 $$\dim \mathbb{P}^n = n$$이다. 이는 projective space가 affine space와 birationally equivalent함을 반영한다.

</div>

## 차원의 기본 성질

차원의 가장 기본적인 성질은 진부분집합의 차원이 더 작다는 것이다. 이는 기하학적으로 자명한 사실이다. 

<div class="proposition" markdown="1">

<ins id="prop9">**명제 9**</ins> $$X$$의 closed subvariety $$Y \subsetneq X$$에 대하여 $$\dim Y < \dim X$$이 성립한다.

</div>

<details class="proof" markdown="1">
<summary>증명</summary>

$$Y$$의 닫힌집합들의 maximal chain 

$$Y = Y_0 \supsetneq Y_1 \supsetneq \cdots \supsetneq Y_n \neq \emptyset$$

을 생각하면

$$X \supsetneq Y = Y_0 \supsetneq Y_1 \supsetneq \cdots \supsetneq Y_n$$

은 $$X$$의  길이는 $$n+1$$ chain이다.

</details>

이는 [명제 6](#prop6)의 일반화라 생각할 수 있다. 이제 regular map과 차원의 관계에 대해 살펴보자. 

<div class="proposition" markdown="1">

<ins id="prop10">**명제 10**</ins> 두 variety $$X, Y$$와 regular map $$\varphi: X \to Y$$에 대해 다음이 성립한다.

1. $$\dim \varphi(X) \le \dim X$$가 성립한다.
2. 만약 $$\varphi$$가 dominant라면 $$\dim Y \le \dim X$$이 성립한다.  ([§유리사상, ⁋정의 8](/ko/math/algebraic_geometry/rational_maps#def8))

</div>

<details class="proof" markdown="1">
<summary>증명</summary>

1. $$\varphi(X)$$의 닫힌집합들의 chain  
    
    $$Z_0 \supsetneq Z_1 \supsetneq \cdots \supsetneq Z_n$$

    에 대하여, 이들의 preimage

    $$\varphi^{-1}(Z_0) \supsetneq \varphi^{-1}(Z_1) \supsetneq \cdots \supsetneq \varphi^{-1}(Z_n)$$

    은 $$X$$의 닫힌집합들의 chain이다. 
2. $$\varphi$$가 dominant라면, pullback $$\varphi^\ast: \mathbb{K}(Y)\rightarrow \mathbb{K}(X)$$가 injective이고, 따라서 [명제 7](#prop7)로부터 원하는 결과를 얻는다. 

</details>

첫째 결과는 일반적으로 기하적인 함수가 차원을 높일 수 없다는 우리의 직관을 뒷받침한다. 둘째 결과는 대략적으로 $$\varphi$$가 (up to birational equivalence) surjective라면 target의 차원이 domain의 차원보다 높을 수 없다는 것을 보여준다.

<div class="definition" markdown="1">

<ins id="def11">**정의 11**</ins> Irreducible 다양체 $$X, Y$$ 사이의 regular map $$\varphi: X \to Y$$가 *finite*라는 것은, 모든 affine open $$U \subseteq Y$$에 대하여 $$\varphi^{-1}(U)$$가 affine이고, $$\mathbb{K}[\varphi^{-1}(U)]$$가 $$\mathbb{K}[U]$$ 위의 finitely generated module인 것을 의미한다.

</div>

Finite morphism은 finite fiber를 갖는다는 것을 보일 수 있다. 그럼 다음이 자명하다. 

<div class="proposition" markdown="1">

<ins id="prop12">**명제 12**</ins> 두 variety들 $$X, Y$$와 finite map $$\varphi: X \to Y$$에 대해 $$\dim X = \dim Y$$이다.

</div>

<details class="proof" markdown="1">
<summary>증명</summary>

$$\varphi$$가 finite이면, coordinate ring level에서 $$\mathbb{K}[X]$$는 $$\mathbb{K}[Y]$$-module로서 finitely generated이다. 따라서 $$\mathbb{K}(X)$$는 $$\mathbb{K}(Y)$$의 finite degree extension이고, transcendence degree가 같다. 즉, $$\dim X = \dim Y$$이다.

</details>

<div class="example" markdown="1">

<ins id="ex13">**예시 13**</ins> $$\mathbb{A}^n$$의 $$k$$차원 linear subspace $$L$$은 $$\dim L = k$$이다. 이는 $$L \cong \mathbb{A}^k$$이기 때문이다. 마찬가지로 $$\mathbb{P}^n$$의 $$k$$차원 linear subspace $$L$$은 $$\dim L = k$$이다. 

</div>

<div class="example" markdown="1">

<ins id="ex14">**예시 14**</ins> 두 variety들 $$X, Y \subseteq \mathbb{A}^n$$에 대해, 일반적으로

$$\dim(X \cap Y) \ge \dim X + \dim Y - n$$

이다. 이를 *dimension inequality*라 부른다. 이것이 부등식인 이유는 가령, $$X=Y$$와 같은 극단적인 상황에서는 원하는 식이 성립하지 않을 수 있기 때문이다. 등호가 성립하는 경우를 *proper intersection*이라 부른다. 

</div>

---

**참고문헌**

**[Har]** J. Harris, *Algebraic Geometry: A First Course*, Springer, 1992.  
**[Hart]** R. Hartshorne, *Algebraic Geometry*, Graduate Texts in Mathematics, Springer, 1977.  
**[Sha]** I. R. Shafarevich, *Basic Algebraic Geometry I: Varieties in Projective Space*, Springer, 2013.  
**[AM]** M. F. Atiyah and I. G. Macdonald, *Introduction to Commutative Algebra*, Addison-Wesley, 1969.
