---

title: "완비화"
excerpt: ""

categories: [Math / Commutative Algebra]
permalink: /ko/math/commutative_algebra/completion
header:
    overlay_image: /assets/images/Math/Commutative_Algebra/Completion.png
    overlay_filter: 0.5
sidebar: 
    nav: "commutative_algebra-ko"

date: 2024-12-22
last_modified_at: 2024-12-22
weight: 14

---

임의의 abelian group $G$와 그 subgroup들의 decreasing sequence

$$G=H_0\supseteq H_1\supseteq\cdots$$

가 주어졌다 하면, $G/ H_{i+1} \rightarrow G/H_{i}$들이 잘 정의되며, 이로부터 inverse limit

$$\hat{G}=\varprojlim_i G/H_i=\left\{(g_1,g_2,\ldots)\in \prod G/H_i:\text{$g_j\equiv g_i\mod{H_i}$ for all $j>i$}\right\}$$

이 정의된다. 만일 $G$가 ring이고, $H_i$들이 ideal들이었다면 $\hat{G}$ 또한 자연스러운 ring 구조를 갖는다. 우리가 살펴볼 상황은 다음과 같은 상황이다. 

<div class="definition" markdown="1">

<ins id="def1">**정의 1**</ins> Ring $A$과 ideal $\mathfrak{a}$에 대하여, 

$$\hat{A}=\varprojlim_i A/\mathfrak{a}^i$$

을 $A$의 $\mathfrak{a}$에 대한 *completion<sub>완비화</sub>*이라 부른다. 만일 natural map $A \rightarrow \hat{A}$이 isomorphism이라면, $A$을 $\mathfrak{a}$에 대한 *complete ring<sub>완비환</sub>*이라 부른다. 특별히 $\mathfrak{a}$가 maximal ideal이라면, $\hat{A}$은 유일한 maximal ideal $\hat{\mathfrak{a}}$를 갖는 local ring이 되므로, 이 경우 $\hat{A}$을 *complete local ring<sub>국소완비환</sub>*이라 부른다. 

</div>

그럼 다음이 성립한다.

<div class="proposition" markdown="1">

<ins id="thm2">**정리 2**</ins> Noetherian ring $A$와 ideal $\mathfrak{a}$를 고정하고, $\hat{A}$가 $\mathfrak{a}$에 대한 $A$의 completion이라 하자. 그럼 다음이 성립한다.

1. $\hat{A}$는 noetherian이다.
2. $\hat{A}/\mathfrak{a}^i\hat{A}=A/\mathfrak{a}^i$가 모든 $i$에 대해 성립한다. 

</div>

또, 다음이 성립한다.

<div class="proposition" markdown="1">

<ins id="thm3">**정리 3**</ins> Noetherian ring $A$와 ideal $\mathfrak{a}$를 고정하고, $\hat{A}$가 $\mathfrak{a}$에 대한 $A$의 completion이라 하자. 그럼 다음이 성립한다.

1. 임의의 finitely generated $A$-module $M$에 대하여, 
    
    $$\hat{A}\otimes_A M \rightarrow\varprojlim_i M/\mathfrak{a}^iM$$

    이 isomorphism이다. 
2. $\hat{A}$는 flat $A$-module이다.

</div>

<div class="proposition" markdown="1">

<ins id="thm4">**정리 4**</ins> Ring $A$가 ideal $\mathfrak{a}$에 대해 complete이라 하고, $f(\x)\in A[\x]$라 하자. 만일 

$$f(a)\equiv 0\pmod{f'(a)^2 \mathfrak{a}}$$

이라면, 적당한 $b\in A$가 존재하여

$$f(b)=0,\qquad b\equiv a\pmod{f'(a)\mathfrak{a}}$$

이 성립하도록 할 수 있다. 뿐만 아니라, 만일 $f'(a)$가 non-zerodivisor라면 이러한 $b$는 유일하게 결정된다. 

</div>

<div class="proposition" markdown="1">

<ins id="thm5">**정리 5**</ins> Complete local noethherian ring $(A, \mathfrak{m})$과 residue field $\kappa$에 대하여, 만일 $A$가 어떠한 field를 포함한다면 $A\cong\kappa[[\x_1,\ldots, \x_n]]/\mathfrak{a}$를 만족하는 적당한 $n$과 ideal $\mathfrak{a}$가 존재한다. 

</div>