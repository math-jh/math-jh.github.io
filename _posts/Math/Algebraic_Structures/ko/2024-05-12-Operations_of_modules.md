---

title: "가군의 곱과 합, 텐서곱"
excerpt: ""

categories: [Math / Algebraic Structures]
permalink: /ko/math/algebraic_structures/product_and_sum_of_modules
header:
    overlay_image: /assets/images/Math/Algebraic_Structures/Product_and_sum_of_modules.png
    overlay_filter: 0.5
sidebar: 
    nav: "algebraic_structures-ko"

date: 2024-05-12
last_modified_at: 2024-05-12
weight: 203

---

## 가군의 곱과 합

Category $\lMod{A}$는 bicomplete category이다. 이를 보이기 위해서는 $\lMod{A}$에서의 임의의 product와 coproduct를 만들어야 하는데, 이를 보이기 위해서는 $\Ab$에서의 product와 coproduct 위에 자연스러운 $A$-action이 존재한다는 것을 보이면 된다.

$A$-module들의 family $(E\_i)\_{i\in I}$가 주어졌다 하자. 그럼 $\prod E\_i$ 위에서의 action은 다음의 식

$$A\otimes\left(\prod_{i\in I}E_i\right)\overset{\id_A\otimes\pr_i}{\longrightarrow} A\otimes E_i \overset{\rho_i}{\longrightarrow} E_i $$

을 통해 $A\otimes\left(\prod E\_i\right) \rightarrow E\_i$를 정의한 후, $\Ab$에서의 product의 universal property를 이용해 $A\otimes\left(\prod E\_i\right) \rightarrow \prod E\_i$를 만들고 이것이 action의 조건을 만족함을 보이면 된다. 

Coproduct의 경우, $A\otimes-$은 $\Ab$에서 $\Ab$로의 left adjoint이므로 colimit을 보존하고, 따라서 

$$A\otimes\left(\bigoplus_{i\in I} E_i\right)\cong\bigoplus_{i\in I}(A\otimes E_i)\overset{\bigoplus \rho_i}{\longrightarrow} \bigoplus_{i\in I}E_i$$

를 통해 $\bigoplus E\_i$ 위에서의 action이 정의된다. Equalizer와 coequalizer의 경우, 두 module homomorphism $f,g:E \rightarrow F$에 대하여

$$\Eq(f,g)=\{x\in E: f(x)=g(x)\}$$

그리고

$$\CoEq(f,g)=F/S,\qquad S=\langle f(x)-g(x)\rangle\rangle$$

을 통해 정의할 수 있다. 즉 다음이 성립한다. 

<div class="proposition" markdown="1">

<ins id="thm1">**정리 1**</ins> $\lMod{A}$는 bicomplete category이며, 특히 $A$-module들의 family $(E_i)$의 product는 이들의 direct product, coproduct는 이들의 direct sum으로 주어진다.

</div>

## 가군의 텐서곱

한편 우리는 $A$-module들의 텐서곱 또한 정의할 수 있다. 이를 위해서는 다음을 먼저 정의해야 한다. 

