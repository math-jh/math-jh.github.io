---

title: "뇌터 정규화"
excerpt: ""

categories: [Math / Commutative Algebra]
permalink: /ko/math/commutative_algebra/noether_normalization
header:
    overlay_image: /assets/images/Math/Commutative_Algebra/Noether_normalization.png
    overlay_filter: 0.5
sidebar: 
    nav: "commutative_algebra-ko"

date: 2025-03-23
last_modified_at: 2025-03-23
weight: 21

---

## 뇌터 정규화

이번 글의 목표는 다음의 정리를 보이고, 이에 따른 결과들을 살펴보는 것이다. 

<div class="proposition" markdown="1">

<ins id="thm1">**정리 1 (Noether normalization lemma)**</ins> Finitely generated $d$-dimensional $\mathbb{K}$-algebra $A$에 대하여, 다음의 부등식

$$d_1>d_2>\cdots>d_m>0$$

을 만족하는 자연수들과, $\dim \mathfrak{a}_i=d_i$를 만족하는 $A$의 ideal들의 descending chain

$$\mathfrak{a}_1\subset \mathfrak{a}_2\subset\cdots\subset \mathfrak{a}_m$$

이 주어졌다 하자. 그럼 $A$의 적당한 subring $B\cong \mathbb{K}[\x_1,\ldots, \x_d]$가 존재하여, $A$가 $B$-module로서 finitely generated이고 다음 식

$$\mathfrak{a}_i\cap B=(\x_{d_i+1},\ldots, \x_d)\qquad\text{for $i=1,\ldots, m$}$$

이 성립하도록 할 수 있다. 

</div>

이는 다음의 보조정리를 사용하여 보일 수 있으며, 이에 대한 증명은 생략하기로 한다. 

<div class="proposition" markdown="1">

<ins id="lem2">**보조정리 2**</ins> Field $\mathbb{K}$와, non-constant polynomial $f\in B=\mathbb{K}[\x_1,\ldots, \x_r]$이 주어졌다 하자. 그럼 적당한 원소들 $\x_1',\ldots, \x_{r-1}'\in B$가 존재하여, 원소들 $\x_1',\ldots, \x_{r-1}', f$로 생성된 $B$의 $\mathbb{K}$-subalgebra를 $B'$라 했을 때 $B$가 finitely generated $B'$-module이도록 할 수 있다. 뿐만 아니라, 이들 원소들은 다음과 같이 택할 수 있다.

1. 충분히 큰 정수 $e$에 대하여, $\x_i'=\x_i-\x_r^{e}$으로 택할 수 있다. 
2. 만일 $\mathbb{K}$가 infinite field라면, 적당한 $a_i\in \mathbb{K}$들에 대해 $\x_i'=\x_i-a_i\x_r$로 택할 수 있다. 

</div>

그럼 [정리 1](#thm1)의 증명은 다음과 같다. 

<details class="proof--alone" markdown="1">
<summary>정리 1의 증명</summary>

우선 $A$가 finitely generated $\mathbb{K}$-algebra이므로 $A=\mathbb{K}[\y_1,\ldots, \y_r]/\mathfrak{a}$라 적을 수 있다. 그럼 주어진 조건을 만족하는 ideal들의 chain이 주어졌다 하면, 이들의 $\mathbb{K}[\y_1,\ldots, \y_r]$에서의 preimage들로 이루어진 chain

$$\tilde{\mathfrak{a}}_1\subset \tilde{\mathfrak{a}}_2\subset\cdots\subset  \tilde{\mathfrak{a}}_m$$

를 생각한 후 $\mathfrak{a}_0=\mathfrak{a}$를 끼워넣어 이를 $\mathbb{K}[\y_1,\ldots, \y_r]$에서의 ideal들의 descending chain

$$\mathfrak{a}\subset \tilde{\mathfrak{a}}_1\subset \tilde{\mathfrak{a}}_2\subset\cdots\subset  \tilde{\mathfrak{a}}_m$$

으로 볼 수 있으므로 주어진 주장을 polynomial ring $A=\mathbb{K}[\y_1,\ldots, \y_r]$에 대해서만 보이면 충분하다. 이 경우, [§매개계, ⁋따름정리 10](/ko/math/commutative_algebra/system_of_parameters#cor10)에 의하여 $r=d$여야 한다. 

이제 정리의 원소들 $\x_i$들을 만들기 위해 우리는 우선 $\x_i'=\y_i$로 두고, 이들을 바꿔가며 주어진 조건을 만족하는 $\x_d$들을 찾을 것이다. 이를 위해 다음의 두 조건

1. $A$는 finitely generated $B_e=\mathbb{K}[\x_1',\ldots, \x_e',\x_{e+1},\ldots, \x_d]$-module이다. 
2. 각각의 $i$에 대하여 $\mathfrak{a}_i\cap B_e\supset(\x_m,\ldots, \x_d)$이 성립한다. 여기서 $m=\max(d_i+1, e+1)$이다. 

을 만족하는 원소들 $\x_1',\ldots, \x_e', \x_{e+1},\ldots, \x_d$들이 주어졌다 하고, 이로부터 새로운 원소들 $\x_1',\ldots, \x_{e-1}'$ 그리고 $\x_e$를 찾아 위의 조건이 그대로 유지되도록 할 수 있다는 것을 보인다. 그럼 이 과정을 반복하여 마지막으로 얻어진 $B=B_{d_m}$이 원하는 조건을 만족한다는 것은 둘째 조건의 포함관계가 사실 등식이라는 것을 보이면 자명하며, 이는 양 변에 있는 $B$의 두 ideal들의 차원을 생각하면 당연하다. 

이제 이 귀납법을 완성하기 위해, $d\geq e>d_m$을 만족하는 $e$에 대하여, 위의 두 조건을 만족하는 $\x_1',\ldots, \x_e', \x_{e+1},\ldots, \x_d$들이 주어졌다 하고, $i$가 $e>d_i$를 만족하는 것들 중 가장 작은 index라 가정하자. 그럼

$$\mathfrak{a}_i\cap \mathbb{K}[\x_1',\ldots, \x_e']\neq 0$$

이다. 만일 이 교집합이 $0$이라 가정하면, 둘째 조건에 의해 

$$\mathfrak{a}_i\cap B_e\supseteq (\x_{e+1},\ldots, \x_d)$$

이 성립하는데, 좌변의 ideal은 $d_i$-차원이고, 우변의 ideal의 차원은 $e$가 되어 모순이기 때문이다. 이제 $\x_e$를 위의 교집합에 속하는 아무 nonzero polynomial로 잡은 후, [보조정리 2](#lem2)를 사용하여 새로운 원소들 $\x_1',\ldots, \x_{e-1}'$들도 새로운 원소로 교체해주면 된다.

</details>

## 결과들

[정리 1](#thm1)은 다음의 결과를 준다.

<div class="proposition" markdown="1">

<ins id="thm3">**정리 3**</ins> Ring $A$가 integral domain이고, finitely generated $\mathbb{K}$-algebra라 하자. 그럼 $\dim A=\trdeg_\mathbb{K}\Frac(A)$이다. 

</div>