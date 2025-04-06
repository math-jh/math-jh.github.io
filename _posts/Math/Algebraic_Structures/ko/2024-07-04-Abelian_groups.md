---

title: "가환군"
excerpt: "Free abelian group, tensor product"
categories: [Math / Algebraic Structures]
permalink: /ko/math/algebraic_structures/abelian_groups
header:
    overlay_image: /assets/images/Math/Algebraic_Structures/Abelian_groups.png
    overlay_filter: 0.5
sidebar: 
    nav: "algebraic_structures-ko"

date: 2024-07-04
last_modified_at: 2024-07-04
weight: 10

---

우리는 지금까지 category $\Ab$에 대해 그렇게까지 큰 관심을 기울이지 않았는데, 이번 글에서는 abelian group들에 대해 살펴본다.

## 가환군들의 합

우선, [§제한합, ⁋정리 2](/ko/math/algebraic_structures/restricted_sums#thm2)에서 보인 weak direct product의 universal property는 특히 group $H$가 abelian group일 경우 잘 적용된다.

<div class="proposition" markdown="1">

<ins id="thm1">**정리 1**</ins> Abelian group들의 family $(G_i)$가 주어졌다 하고, $\prod^w G_i$와 inclusion map들 $\iota_i$를 생각하자. 그럼 임의의 abelian group $H$와 group homomorphism들 $f_i:G_i\rightarrow H$에 대하여, $f_i=f\circ\iota_i$이도록 하는 유일한 group homomorphism $f:\prod^wG_i\rightarrow H$가 존재한다.

</div>

따라서, 적어도 abelian group들 사이에서는 weak direct product $\prod^w G_i$가 coproduct가 된다. 이를 다음과 같이 부르기로 한다.

<div class="definition" markdown="1">

<ins id="def2">**정의 2**</ins> Abelian group들의 family $(G_i)$와, 이들의 weak direct product $\prod^w G_i$, 그리고 inclusion map들 $\iota_i$가 주어졌다 하자. 그럼 $\prod^w G_i$와 $\iota_i$들을 묶어 $G_i$들의 *direct sum<sub>직합</sub>*이라 부르고 이를 $\bigoplus G_i$로 표현한다.  

</div>

약간의 표기법의 남용을 통해 $\iota_i(G_i)$와 $G_i$를 같은 것으로 보면, $\bigoplus G_i$의 임의의 원소는 다음 식

$$x=\sum_{i\in I} x_i,\qquad\text{$x_i\in G_i$, $x_i=0$ for all but finitely many $i$}$$

으로 쓸 수 있다. 이러한 상황에서 $x_i\neq 0$을 만족하는 $I$의 부분집합을 $x$의 *support<sub>지지집합</sub>*라 부르고 $\supp(x)$로 적고, 위의 조건이 성립하면 family $(x_i)$가 *finitely supported*라 부른다.

## Abelianization

이제 다음을 정의하자.

<div class="definition" markdown="1">

<ins id="def3">**정의 3**</ins> 임의의 group $G$와 $G$의 두 subgroup $H_1,H_2$에 대하여, $[H_1,H_2]$를 다음의 *commutator<sub>교환자</sub>*들

$$[h_1,h_2]=h_1^{-1}h_2^{-1}h_1h_2,\qquad h_1\in H_1,h_2\in H_2$$

로 생성된 $G$의 subgroup으로 정의한다.

</div>

특별히 우리가 이번 글에서 관심을 가지는 것은 $H_1=H_2=G$일 때이다. 만일 $G$가 abelian group이었다면, 모든 $x,y\in G$에 대하여 $x^{-1}y^{-1}xy=e$이므로 $[G,G]=\\{e\\}$이다. 따라서 $[G,G]$는 $G$가 abelian group이 되는 것으로부터 얼마나 떨어져 있는지를 나타낸다고 생각할 수 있다. 

한편 다음이 성립한다.

<div class="proposition" markdown="1">

<ins id="prop4">**명제 4**</ins> 임의의 group $G$에 대하여, commutator subgroup $[G,G]$는 $G$의 normal subgroup이다.

</div>
<details class="proof" markdown="1">
<summary>증명</summary>

임의의 $x,y\in G$와 $g\in G$에 대하여,

$$g(x^{-1}y^{-1}xy)g^{-1}=(gx^{-1}g^{-1})(gy^{-1}g^{-1})(gxg^{-1})(gyg^{-1})=(gxg^{-1})^{-1}(gyg^{-1})^{-1}(gxg^{-1})(gyg^{-1})\in [G,G]$$

이므로 자명하다. 

</details>

따라서, $G/[G,G]$가 잘 정의된다. 이는 $x^{-1}y^{-1}xy$꼴의 원소를 모두 $e$로 취급하겠다는 것이므로, $G/[G,G]$는 abelian group이 된다. 우리의 convention에 따르면 abelian group의 연산은 $+$로 적는 것이 맞으나, $G/[G,G]$는 동시에 $G$로부터 연산을 물려받으므로 이렇게 쓰면 혼동의 여지가 있을 수 있다. 따라서 $G/[G,G]$의 연산은 $+$가 아닌 곱셈으로 적기로 한다. 

한편, 임의의 abelian group $H$에 대하여, 만일 group homomorphism $f:G\rightarrow H$가 주어졌다면 임의의 $x,y\in G$에 대해 다음 식

$$e=f(x)^{-1}f(y)^{-1}f(x)f(y)=f(x^{-1}y^{-1}xy)$$

이 성립하므로, $[G,G]\leq\ker f$이다. 이제 [§군 동형사상, ⁋명제 3](/ko/math/algebraic_structures/isomorphism_theorems#prop3)에 의하여 다음을 얻는다.

<div class="proposition" markdown="1">

<ins id="prop5">**명제 5**</ins> 임의의 group $G$와 quotient homomorphism $p:G\rightarrow G/[G,G]$를 생각하자. 그럼 임의의 abelian group $H$와 group homomorphism $f:G \rightarrow H$에 대하여, $f=\bar{f}\circ p$를 만족하는 $\bar{f}:G/[G,G]\rightarrow H$가 존재한다.

</div>

특히, 임의의 group homomorphism $f:G\rightarrow H$가 주어졌다 하자. 그럼 합성 $G\rightarrow H\rightarrow H/[H,H]$에 의해 group $G$로부터 abelian group $H/[H,H]$로의 group homomorphism을 얻고, [명제 5](#prop5)에 의하여 이는 $G/[G,G]$에서 $H/[H,H]$로의 group homomorphism을 유도한다. 

<div class="definition" markdown="1">

<ins id="def6">**정의 6**</ins> 임의의 group $G$에 대하여, quotient group $G/[G,G]$를 $G$의 *abelianization*이라 부르고 $G^\ab$으로 표기한다.

</div>

그럼 앞선 논증은 이것이 functor $\ab:\Grp\rightarrow\Ab$를 정의한다는 것을 보여준다. 뿐만 아니라 다음이 성립한다.

<div class="proposition" markdown="1">

<ins id="prop7">**명제 7**</ins> Forgetful functor $U:\Ab \rightarrow \Grp$과 abelianization functor $\ab:\Grp \rightarrow \Ab$에 대하여, adjunction $\ab\dashv U$가 존재한다.

</div>

이에 대한 증명은 이미 위에서 완료하였다.

## 자유가환군

앞선 글의 말미에서 우리는 free group $F(X)$를 free product

$${\prod_{x\in X}}^\ast \mathbb{Z}$$

으로 해석할 수 있었다. 그런데 $\Ab$는 이미 coproduct $\bigoplus$를 갖는다는 것을 알고 있으므로, 동일한 논증을 통해 forgetful functor $U:\Ab \rightarrow \Set$의 left adjoint $F_\Ab:\Set\rightarrow \Ab$를 다음 식

$$F_\Ab(X)=F_\Ab\left(\coprod_{x\in X} \{x\}\right)\cong \coprod_{x\in X} F_\Ab(\ast)=\bigoplus_{x\in X} \mathbb{Z}$$

을 통해 얻을 수 있다. 이렇게 얻어지는 $F_\Ab(X)$를 *free abelian group*이라 정의한다. 즉 다음 명제가 성립한다.

<div class="proposition" markdown="1">

<ins id="prop8">**명제 8**</ins> Forgetful functor $U:\Ab \rightarrow \Set$의 left adjoint $F_\Ab:\Set \rightarrow\Ab$가 존재한다. 

</div>

## 가환군 $\Hom_\Ab(G,H)$

임의의 abelian group $G,H$에 대하여, $\Hom_\Ab(G,H)$는 $G$에서 $H$로의 group homomorphism들의 집합이다. 그런데 이 집합에는 흥미로운 성질이 있는데, 바로 $\Hom_\Ab(G,H)$는 이미 abelian group이라는 것이다. 이는 $\Grp$에서는 성립하지 않는 결과이다. 

<div class="proposition" markdown="1">

<ins id="prop9">**명제 9**</ins> 임의의 abelian group $G,H$에 대해 $\Hom_\Ab(G,H)$는 abelian group이다.

</div>
<details class="proof" markdown="1">
<summary>증명</summary>

임의의 $f,g:G \rightarrow H$에 대하여, $f+g$를

$$(f+g)(x)=f(x)+g(x)\qquad\text{for all $x\in G$}$$

으로 정의하면 된다.

</details>

$\Hom_\Ab(-,-)$는 원래 $\Ab^\op\times \Ab$에서 $\Set$으로의 bifunctor로 정의되었지만, 이 명제에 의해 실은 이를 $\Ab$로의 bifunctor로 볼 수도 있다. 즉 $\Hom_\Ab(-,-)$를 internal $\Hom$과 비슷한 것으로 생각할 수 있다. 그러나 지금까지 갖고 있는 언어로만 보았을 때 이는 불가능하다.

<div class="example" markdown="1">

<ins id="ex10">**예시 10**</ins> $\Ab$는 $\times$에 대해 cartesian monoidal category이다. 그러나 $\Hom_\Ab(-,-)$는 이 구조에 대해 internal $\Hom$으로 생각할 수 없다. 즉

$$\Hom_\Ab(G\times H, A)\cong \Hom_\Ab(G,\Hom_\Ab(H,A))$$

이 일반적으로 성립하지 않는다. 예를 들어, $G=\mathbb{Z}$라 하면 위의 식은

$$\Hom_\Ab(\mathbb{Z}\times H,A)\cong \Hom_\Ab(\mathbb{Z},\Hom_\Ab(H,A))\cong \Hom_\Ab(H,A)\tag{1}$$

이 될텐데, 이 식은 거의 대부분 거짓일 것이다. (가령 $H=\\{e\\}$를 넣어보면 된다.)

</div>

따라서, $\Hom_\Ab(-,-)$를 internal $\Hom$으로 생각하기 위해서는 $\Ab$ 위에 새로운 symmetric monoidal category 구조를 주어야 한다. 또 위의 식 (1)로부터 힌트를 얻으면 $\mathbb{Z}$가 이 monoidal product의 unit처럼 행동해야 한다는 것도 추측할 수 있다. 

## 텐서곱

[예시 10](#ex10)에서의 식이 성립할 수 없는 근본적인 이유는 꽤나 간단하다. $\Set$에서 위의 isomorphism이 성립했던 이유는 임의의 함수 $f:A\times B \rightarrow C$에 대하여, $A$의 원소 혹은 $B$의 원소를 하나 고정하고 나면 남는 것이 $B$ 혹은 $A$에서 $C$로의 함수가 되었기 때문이다.

반면, group homomorphism $f:G\times H \rightarrow A$의 첫 번째 혹은 두 번째 성분을 고정한 것이 group homomorphism이 되도록 하는 $f$는 오직 zero map 뿐이다. 임의의 $x\in G$에 대하여 $f(x, -)$이 group homomorphism이라면 $f(x,0)=0$이어야 하고, 비슷하게 임의의 $y\in H$에 대해 $f(0,y)=0$이어야 하므로 이를 $f$가 group homomorphism이라는 조건

$$f(x+0,0+y)=f(x,0)+f(0,y)$$

에 대입하면 $f(x,y)=0$이 모든 $(x,y)\in G\times H$에 대해 성립해야 하기 때문이다. 

위의 논증을 살펴보면, $f$의 source의 하나의 성분을 고정했을 때 나오는 함수가 group homomorphism임을 요구하는 것이 꽤나 자연스러워 보인다.

<div class="definition" markdown="1">

<ins id="def11">**정의 11**</ins> 두 abelian group $G,H$에 대하여, 함수 $f:G\times H \rightarrow A$가 *bilinear<sub>쌍선형</sub>*이라는 것은 다음 두 식

$$f(x,y_1+y_2)=f(x,y_1)+f(x,y_2),\qquad f(x_1+x_2,y)=f(x_1,y)+f(x_2,y)$$

이 항상 성립하는 것이다. 

</div>

이제 고정된 $G,H\in\obj(\Ab)$에 대하여, 집합 $\Bilin(G,H;A)$을 다음 식

$$\Bilin(G,H;A)=\{\text{bilinear maps from $G\times H$ to $A$}\}$$

으로 정의하자. 위의 논증에 의해 [예시 10](#ex10)의 첫 번째 식의 좌변을 $\Bilin(G,H;A)$로 바꾼다면 isomorphism

$$\Bilin(G,H;A)\cong \Hom_\Ab(G,\Hom_\Ab(H,A))$$

을 얻는다는 것을 확인할 수 있다. 뿐만 아니라, $\Bilin(G,H;-)$이 $\Ab$에서 $\Set$으로의 representable functor가 된다는 것을 확인할 수 있다. 

<div class="proposition" markdown="1">

<ins id="thm12">**정리 12**</ins> $\Bilin(G,H;-)$는 representable이다.

</div>
<details class="proof" markdown="1">
<summary>증명</summary>

Free abelian group $F_\Ab(G\times H)$의 subgroup $S$를

$$S=\left\langle (x, y_1+y_2)-(x,y_1)-(x,y_2), (x_1+x_2,y)-(x_1,y)-(x_2,y)\mathop{\big\vert}x,x_1,x_2\in G, y,y_1,y_2\in H\right\rangle$$

으로 정의하자. 그럼 free abelian group의 universal property에 의하여, 임의의 함수 $f:G\times H \rightarrow A$가 주어질 때마다 group homomorphism $\hat{f}:F_\Ab(G\times H)\rightarrow A$가 존재하고, $f$가 bilinear라면 이 $\hat{f}$의 kernel이 $S$를 포함하므로 $\hat{f}$가 $F_\Ab(G\times H)/S$에서 $A$로의 group homomorphism을 정의한다. 

Isomorphism $\Bilin(G,H;A)\cong\Hom_\Ab(F_\Ab(G\times H)/S,A)$의 naturality는 추가적으로 보여야 하긴 하지만, 단순한 계산이므로 생략한다. 

</details>

<div class="definition" markdown="1">

<ins id="def13">**정의 13**</ins> [정리 12](#thm12)의 representation을 $G$와 $H$의 *tensor product<sub>텐서곱</sub>*이라 부르고, $A\otimes B$로 적는다.

</div>

$A\otimes B$의 원소는 $a\otimes b$의 꼴의 원소들의 유한한 합으로 나타난다는 것을 알 수 있다. 그럼 $\otimes$가 $\mathbb{Z}$를 tensor unit으로 갖는 monoidal product임을 확인할 수 있다. 

<div class="proposition" markdown="1">

<ins id="thm14">**정리 14**</ins> $(\Ab,\otimes, \mathbb{Z})$는 symmetric monoidal category이다.

</div>
<details class="proof" markdown="1">
<summary>증명</summary>

Associator $\alpha$와 symmetor $\sigma$는 $\otimes$의 universal property에 의해 얻어진다. $\mathbb{Z}$가 tensor unit이라는 것은 다음 isomorphism

$$\Hom_\Ab(\mathbb{Z}\otimes G, H)\cong\Bilin(\mathbb{Z},G;H)\cong\Hom_\Ab(\mathbb{Z},\Hom_\Ab(G,H))\cong\Hom_\Ab(G,H)$$

이 natural하다는 것으로부터 얻어진다. 

</details>

특히, 임의의 $f:A \rightarrow A'$, $g:B \rightarrow B'$에 대하여 $\otimes$는 bifunctor이므로, morphism $f\otimes g:A\otimes B \rightarrow A'\otimes B'$가 존재한다. 이는 $a\otimes b$ 꼴의 원소들을 $f(a)\otimes g(b)$로 보내는 것을 통해 결정되는 group homomorphism이다. 종종 abelian group $A$의 $n$-fold tensor product를 생각할 일도 있는데, 이 경우

$$A^{\otimes n}=\underbrace{A\otimes\cdots\otimes A}_\text{$n$ times}$$

으로 적는다. 그럼 $\otimes$의 associativity에 의하여 

$$A^{\otimes m}\otimes A^{\otimes n}\cong A^{\otimes(m+n)}$$

이 성립한다. 이러한 관점에서 관례적으로 $A^{\otimes 0}$은 $\mathbb{Z}$로 정의한다. 

힌퍈, 이렇게 $(\Ab,\otimes, \mathbb{Z})$를 symmetric monoidal category로 생각하고 나면, 다음이 성립한다는 것을 이미 확인하였다.

<div class="proposition" markdown="1">

<ins id="thm15">**정리 15 ($\otimes\dashv\Hom$)**</ins> Adjunction 

$$\Hom_\Ab(G\otimes H, A)\cong\Hom_\Ab(G,\Hom_\Ab(H, A))\cong\Hom_\Ab(H,\Hom_\Ab(G, A))$$

이 존재한다. 따라서, $\Hom_\Ab(-,-)$를 $(\Ab,\otimes,\mathbb{Z})$의 internal $\Hom$으로 생각할 수 있다. 

</div>

## 등급가환군

Abelian group들의 family $(G_i)$에 대하여, direct sum $\bigoplus G_i$가 잘 정의된다. 다음 정의는 다른 대수적인 구조들에서 특히 유용하게 사용된다.

<div class="definition" markdown="1">

<ins id="def16">**정의 16**</ins> Commutative monoid $I$에 대하여, $I$로 index가 주어진 abelian group들의 family $(G\_i)\_{i\in I}$를 생각하자. 이를 *graded abelian group*이라 부른다.

</div>

현재로서는 commutative monoid $I$에 대하여, $I$를 집합으로 생각하여 direct sum을 취한 것과 위에서 정의한 graded abelian group 사이에 차이가 없으므로 현재로서는 이 정의는 기존에 있던 개념에 새로운 이름을 붙인 것에 불과하다. 이를 정의하는 이유는 나중에 abelian group 위에 새로운 연산을 정의했을 때 이 연산과 $I$의 덧셈 사이의 관계를 부여하기 위한 것이다.

---

**참고문헌**

**[nLab]** *Tensor product of abelian groups*. [Link](https://ncatlab.org/nlab/show/tensor+product+of+abelian+groups)