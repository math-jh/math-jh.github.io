---

title: "다항식환"
excerpt: ""

categories: [Math / Ring Theory]
permalink: /ko/math/ring_theory/polynomial_rings
header:
    overlay_image: /assets/images/Math/Ring_Theory/Polynomial_rings.png
    overlay_filter: 0.5
sidebar: 
    nav: "ring_theory-ko"

date: 2025-05-06
last_modified_at: 2025-05-06
weight: 3

---

<div class="remark" markdown="1">

<ins id="rmk">**주의**</ins> 이번 글에서 $A$는 항상 commutative ring이다.

</div>

우리는 [\[대수적 구조\] §대수, ⁋정의 7](/ko/math/algebraic_structures/algebras#def7)에서 임의의 (commutative) ring $A$에 대하여 polynomial algebra $A[\x\_i]\_{i\in I}$를 정의하였다. 이는 $A$-algebra 구조를 갖지만, 어차피 $A[\x\_i]\_{i\in I}$ 위에 정의된 $A$의 스칼라곱은 $A[\x\_i]\_{i\in I}$를 ring으로 보았을 때, inclusion $A\hookrightarrow A[\x\_i]\_{i\in I}$으로부터 오는 것이므로 $A[\x\_i]\_{i\in I}$의 성질을 살펴보기 위해서는 $A[\x\_i]\_{i\in I}$를 ring으로 생각하는 것만으로 충분하다. 

다항식들을 본격적으로 다루기 전에, 이들을 다루기 위한 도구들을 먼저 정의하자. 우선 $A$ 위에서 정의된 *다항식*들은 polynomial ring $A[\x\_i]\_{i\in I}$의 원소들을 의미한다. 이 때, $\mathbb{N}^{(I)}$를 $I$에서 $\mathbb{N}$으로 가는 finitely supported function들의 모임

$$\mathbb{N}^{(I)}=\{\nu:I \rightarrow \mathbb{N}\mid\text{$f(i)=0$ for all but finitely many $i\in $}\}$$

으로 정의하자. 그럼 임의의 $\nu\in \mathbb{N}^{(I)}$에 대하여, 

$$\x^\nu=\prod_{i\in I} \x_i^{\nu_i}$$

으로 두면 $\x^\nu$는 $A[\x\_i]\_{i\in I}$의 원소이다. 우리는 

$$a\x^\nu$$

꼴의 원소들을 *단항식*이라 부른다. 그럼 임의의 다항식 $p$는 단항식들의 유한합

$$p(\x)=\sum_{\nu\in \mathbb{N}^{(I)}} a_\nu \x^\nu,\qquad\text{$\alpha_\nu=0$ for all but finitely many $\nu$}$$

으로 나타낼 수 있다. 

<div class="definition" markdown="1">

<ins id="def1">**정의 1**</ins> Polynomial ring $A[\x]_{i\in I}$의 임의의 원소 

$$p(\x)=\sum_{\nu\in \mathbb{N}^{(I)}} a_\nu \x^\nu,\qquad\text{$\alpha_\nu=0$ for all but finitely many $\nu$}$$

에 대하여, 

$p(\x)=a_d\x^d+\cdots+a_1\x_a_0$ ($a_n\neq 0$)에 대하여, $d$를 $p$의 *degree*라 부르고 $\deg p$로 적는다. 이 때 단항식 $a_d\x^d$를 $p$의 *leading term*이라 부르고, 그 계수 $a_d$를 *leading coefficient*라 부른다. Leading coefficient가 $1$인 다항식을 *monic polynomial*이라 부른다. 

</div>

만일 $A$가 integral domain이라 하면, 임의의 두 $p,q\in A$에 대하여 