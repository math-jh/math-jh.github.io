---

title: "으뜸 분해"
excerpt: ""

categories: [Math / Commutative Algebra]
permalink: /ko/math/commutative_algebra/primary_decomposition
header:
    overlay_image: /assets/images/Math/Commutative_Algebra/Primary_decomposition.png
    overlay_filter: 0.5
sidebar: 
    nav: "commutative_algebra-ko"

date: 2024-10-17
last_modified_at: 2024-10-17
weight: 7

---

이번 글에서 $A$는 noetherian이고 $M$이 finitely generated $A$-module임을 가정한다. 

## Primary submodule

<div class="definition" markdown="1">

<ins id="def1">**정의 1**</ins> $M$의 submodule이 *primary submodule<sub>으뜸부분가군</sub>*인 것은 $\Ass(M/N)$이 하나의 prime ideal로만 구성된 것이다. 만일 $\Ass(M)$이 하나의 prime ideal로만 이루어져 있다면 $M$을 *coprimary submodule<sub>쌍대으뜸부분가군</sub>*이라 부른다. 

</div>

그럼 [§동반소아이디얼, ⁋보조정리 5](/ko/math/commutative_algebra/associated_primes#lem3)로부터 임의의 $\mathfrak{p}$-primary submodule들의 유한한 교집합은 $\mathfrak{p}$-primary인 것을 안다. 또, 다음이 성립한다.

<div class="proposition" markdown="1">

<ins id="prop2">**명제 2**</ins> Ring $A$와 prime ideal $\mathfrak{p}$에 대하여 다음이 모두 동치이다.

1. $A$-module $M$이 $\mathfrak{p}$-coprimary module이다.
2. $\mathfrak{p}$는 $\ann(M)$을 포함하는 prime ideal들 중에서 minimal이며, $\mathfrak{p}$에 속하지 않는 원소들은 $M$의 zero divisor가 아니다.
3. 적당한 $k$에 대하여 $\mathfrak{p}^k$가 $M$을 annihilate하며, $\mathfrak{p}$에 속하지 않는 원소들은 $M$의 zero divisor가 아니다.

</div>
<details class="proof" markdown="1">
<summary>증명</summary>

우선 첫 번째 조건이 성립한다 하면, 정의에 의하여 $\mathfrak{p}$가 $M$의 유일한 associated prime ideal이다. 이제 [§동반소아이디얼, ⁋정리 7](/ko/math/commutative_algebra/associated_primes#thm7)의 1번 조건에 의하여 $\mathfrak{p}$는 반드시 $\ann(M)$을 포함하는 prime ideal 중 minimal한 것이어야 하며, 2번 조건에 의하여 $\mathfrak{p}$ 바깥에 있는 원소들은 $M$의 zero divisor가 아니다.

이제 두 번째 조건이 성립한다 가정하자. 그럼 $A\setminus \mathfrak{p}$의 원소들은 $M$의 zero divisor가 아니므로, localization $M_\mathfrak{p}$를 생각할 수 있고 

</details>

한편 [§동반소아이디얼, ⁋정리 7](/ko/math/commutative_algebra/associated_primes#thm7)로부터 다음을 얻는다. 

<div class="proposition" markdown="1">

<ins id="thm2">**정리 2**</ins> $M$의 임의의 submodule은 primary submodule들의 교집합이다. 뿐만 아니라, prime ideal들 $\mathfrak{p}\_1,\ldots, \mathfrak{p}\_n$과 $\mathfrak{p}\_k$-primary submodule들 $M\_k$가 주어졌다 하자. 그럼 $M'=\bigcap_{k=1}^n M_k$에 대하여 다음이 성립한다. 

1. $M/M'$의 associated prime은 $\mathfrak{p}_k$들 중 하나이다.
2. 만일 $M'$을 표현할 때, $M_k$들 중 불필요한 것이 없다면 $\mathfrak{p}_i$들은 정확히 $M/M'$의 associated prime이다.
3. 만일 $M'$을 표현하는 방식 중 더 적은 $M_k$들을 이용하는 방식이 없다면, $M/M'$의 associated prime들은 정확히 index 하나 당 하나의 $\mathfrak{p}_k$가 된다. 만일 여기에 더해 $\mathfrak{p}_i$가 $M/M'$의 annihilator ideal들 중 minimal한 것이라면 $M_i$는 $M'$의 $\mathfrak{p}_i$-primary component가 된다. 
4. 주어진 minimal primary decomposition에 대하여, $A$의 임의의 multiplicative subset $S$에 대해, $\mathfrak{p}\_1,\ldots, \mathfrak{p}\_m$들이 $S$와 만나지 않는 prim ideal들이라 하자. 그럼
    
    $$S^{-1}M'=\bigcap_{i=1}^m S^{-1}M_i$$

    은 $S^{-1}A$에 대한 $S^{-1}M$의 minimal primary decomposition이다.

</div>

이 정리에 대한 증명은 다소 긴 감이 있어서 생략하기로 한다. 

<div class="proposition" markdown="1">

<ins id="thm3">**정리 3**</ins> Noetherian domain $A$에 대해 다음이 성립한다.

1. $f\in A$

</div>