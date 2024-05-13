---

title: "가군의 곱"
excerpt: ""

categories: [Math / Algebraic Structures]
permalink: /ko/math/algebraic_structures/product_of_modules
header:
    overlay_image: /assets/images/Math/Algebraic_Structures/Product_of_modules.png
    overlay_filter: 0.5
sidebar: 
    nav: "algebraic_structures-ko"

date: 2024-05-12
last_modified_at: 2024-05-12
weight: 203

---

$A$-module들의 product는 언제나와 같이 정의한다.

<div class="definition" markdown="1">

<ins id="def1">**정의 1**</ins> $A$-module들의 family $(E\_i)\_{i\in I}$에 대하여, 이들의 *product*는 다음의 universal property

> 임의의 $A$-module $F$와 $A$-linear map들 $f_i:F \rightarrow E_i$들이 주어졌을 때, $f_i=\pr_i\circ f$이도록 하는 유일한 $A$-linear map $f:F \rightarrow \prod E_i$이 존재한다.
> ![universal_property_of_product](/assets/images/Math/Algebraic_Structures/Product_of_modules-1.png){:width="251.4px" class="invert" .align-center}

를 만족하는 유일한 (up to unique isomorphism) $A$-module $\prod E\_i$를 뜻한다.

</div>

Product module의 성질 또한 언제나 기대하는 바와 같다. 가령 같은 index set을 공유하는 두 family $(E\_i)\_{i\in I}, (F\_i)\_{i\in I}$와 linear map들의 family $(f\_i:E\_i \rightarrow F\_i)\_{i\in I}$가 주어졌을 때, 이들의 product $f:E \rightarrow F$가 잘 정의되며 kernel과 image 등도 원하는대로 행동한다. 특히 이는 exact sequence를 이용하면 한 번에 표현할 수 있다.

<div class="proposition" markdown="1">

<ins id="prop2">**명제 2**</ins> $A$-module들의 family $(E\_i)\_{i\in I}$, $(F\_i)\_{i\in I}$, $(G\_i)\_{i\in I}$, 그리고 linear map들의 family $(f\_i:E\_i \rightarrow F\_i)\_{i\in I}$와 $(g\_i:F\_i \rightarrow G\_i)\_{i\in I}$가 주어졌다 하고, 이들의 곱을 각각 $E=\prod E\_i, F=\prod F\_i, G=\prod G\_i$ 그리고 $f=\prod f\_i,g=\prod g\_i$라 하자. 그럼 다음의 sequence

$$E \overset{f}{\longrightarrow} F\overset{g}{\longrightarrow} G$$

가 exact인 것은 각각의

$$E_i\overset{f_i}{\longrightarrow} F_i\overset{g_i}{\longrightarrow} G_i$$

이 모두 exact인 것과 동치이다.

</div>
<details class="proof" markdown="1">
<summary>증명</summary>

임의의 $y=(y_i)\in F$에 대하여,

$$y\in\ker g\iff g(y)=0\iff g_i(y_i)=0\text{ for all $i$}\iff $y_i\in\ker g\_i\text{ for all $i$}$$

이고, 비슷하게 $y\in \im(f)$인 것은 적당한 $x=(x_i)\in E$가 존재하여 $y=f(x)$인 것과 동치이며, 따라서 모든 $i$에 대하여 $y_i=f(x_i)$, 즉 모든 $i$에 대하여 $y_i\in\im(f_i)$인 것과 동치이다.

</details>

특별히 증명을 뜯어보면 $\ker(f)=\prod\ker(f_i)$이고 $\im(f)=\prod \im(f_i)$임을 확인할 수 있다. 