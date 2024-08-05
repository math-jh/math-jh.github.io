---

title: "가군의 곱과 합"
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

Category $\lMod{A}$는 bicomplete category이다. 이를 보이기 위해서는 $\lMod{A}$에서의 임의의 product와 coproduct를 만들어야 하는데, $A$-module을 $(\Ab,\otimes, \mathbb{Z})$에서의 monoid object로 생각하면 이를 보이기 위해서는 $\Ab$에서의 product와 coproduct 위에 자연스러운 $A$-action이 존재한다는 것을 보이면 된다.

$A$-module들의 family $(E\_i)\_{i\in I}$가 주어졌다 하자. 위의 관점에 따르면 $E\_i$들 각각은 abelian group으로 생각하고, 추가적인 데이터로 morphism $\rho_i:A\otimes E\_i \rightarrow E\_i$가 주어진 것으로 생각하면 된다. 이제 $\prod E\_i$ 위에서의 action은 다음의 식

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

## 준동형사상의 곱과 합

한편, $A$-module homomorphism들의 family가 주어졌을 경우 다음과 같은 명제들이 성립한다. 

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

$$y\in\ker g\iff g(y)=0\iff g_i(y_i)=0\text{ for all $i$}\iff y_i\in\ker g_i\text{ for all $i$}$$

이고, 비슷하게 $y\in \im(f)$인 것은 적당한 $x=(x_i)\in E$가 존재하여 $y=f(x)$인 것과 동치이며, 따라서 모든 $i$에 대하여 $y_i=f(x_i)$, 즉 모든 $i$에 대하여 $y_i\in\im(f_i)$인 것과 동치이다.

</details>

증명을 뜯어보면 $\ker(f)=\prod\ker(f_i)$이고 $\im(f)=\prod \im(f_i)$임을 확인할 수 있다. 특히 이를 inclusion들 $F_i\hookrightarrow E_i$에 적용하고, first isomorphism theorem을 사용하면 다음의 canonical isomorphism

$$\prod_{i\in I} E_i/F_i\cong \left(\prod E_i\right)\bigg/\left(\prod F_i\right)$$

을 얻는다. 

이에 대한 direct sum의 버전은 다음과 같다.

<div class="proposition" markdown="1">

<ins id="prop3">**명제 3**</ins> $A$-module들의 family $(E\_i)\_{i\in I}$, $(F\_i)\_{i\in I}$, $(G\_i)\_{i\in I}$, 그리고 linear map들의 family $(f\_i:E\_i \rightarrow F\_i)\_{i\in I}$와 $(g\_i:F\_i \rightarrow G\_i)\_{i\in I}$가 주어졌다 하고, 이들의 direct sum을 각각 $E=\bigoplus E\_i, F=\bigoplus F\_i, G=\bigoplus G\_i$ 그리고 $f=\bigoplus f\_i,g=\bigoplus g\_i$라 하자. 그럼 다음의 sequence

$$E \overset{f}{\longrightarrow} F\overset{g}{\longrightarrow} G$$

가 exact인 것은 각각의

$$E_i\overset{f_i}{\longrightarrow} F_i\overset{g_i}{\longrightarrow} G_i$$

이 모두 exact인 것과 동치이다.

</div>

뿐만 아니라, 위와 마찬가지로 $\ker f=\bigoplus\ker f_i$, $\im f=\bigoplus \im f_i$ 등이 성립하고, 다음 isomorphism 

$$\bigoplus(E_i/F_i)\cong\left(\bigoplus E_i\right)\bigg/\left(\bigoplus F_i\right)$$

이 존재한다. 또, Direct sum과 direct product의 universal property에 의하여, abelian group들 사이의 natural isomorphism

$$\Hom_A\left(\bigoplus_{i\in I} E_i,\prod_{j\in J} F_j\right)\cong\prod_{(i,j)\in I\times J}\Hom_A(E_i,F_j)$$

이 존재한다.

## Submodule과 exact sequence들

이제 우리는 submodule들을 통해 정의된 다양한 exact sequence들에 대해 살펴보자. 

<div class="proposition" markdown="1">

<ins id="prop4">**명제 4**</ins> 임의의 $A$-module $E$와, 그 submodule들의 family $(M\_i)\_{i\in I}$가 주어졌다 하자. 그럼 다음 sequence

$$0\rightarrow \bigcap_{i\in I} M_i\rightarrow E\rightarrow\prod_{i\in I} (E/M_i)$$

가 exact이다.

</div>
<details class="proof" markdown="1">
<summary>증명</summary>

$E$에서의 exactness만 보이면 된다. Linear map $E \rightarrow\prod(E/M_i)$가 어떻게 얻어졌는지를 생각하면, 각각의 $i$마다 canonical projection들 $E \rightarrow E/M_i$를 생각한 후 이들에 product의 universal property를 적용하여 얻어진다. 그럼 이 linear map의 kernel은 모든 $i$에 대하여 $\ker(E \rightarrow E/M_i)$에 속하는 원소들의 모임, 즉 $\bigcap M_i$이다.

</details>

비슷하게 $\sum M_i$를 $M_i$들에 의해 generate되는 $E$의 submodule이라 하자. 그럼 다음 명제를 얻는다.

<div class="proposition" markdown="1">

<ins id="prop5">**명제 5**</ins> 임의의 $A$-module $E$와, 그 submodule들의 family $(M\_i)\_{i\in I}$가 주어졌다 하자. 그럼 다음 sequence

$$\bigoplus_{i\in I} M_i \rightarrow E\rightarrow E\bigg/\sum_{i\in I} M_i\rightarrow 0$$

가 exact이다.

</div>
<details class="proof" markdown="1">
<summary>증명</summary>

마찬가지로 $E$에서의 exactness만 보이면 충분한데, $\bigoplus M_i \rightarrow E$는 inclusion들 $M_i \hookrightarrow E$에 의해 얻어진다. 이 map의 image를 생각해보면 $M_i$의 원소들을 유한하게 더하여 얻어질 수 있는 원소들, 즉 $\sum M_i$의 원소이다.

</details>

다음 명제는 위의 두 명제보다 조금 덜 자명하다.

<div class="proposition" markdown="1">

<ins id="prop6">**명제 6**</ins> 임의의 $A$-module $E$와, submodule들 $M,N$에 대하여 다음의 exact sequence들

$$0\longrightarrow M\cap N\overset{f}{\longrightarrow} M\oplus N\overset{g}{\longrightarrow} M+N\longrightarrow 0;\qquad f(x)=(x,x),\quad g(x,y)=x-y$$

그리고

$$0 \longrightarrow E/(M\cap N) \overset{f}{\longrightarrow} (E/M)\oplus (E/N) \overset{g}{\longrightarrow} E/(M+N) \longrightarrow 0$$

이 존재한다. 둘째 sequence의 경우, $f,g$는 각각

$$f(x+M\cap N)=(x+M, x+N),\quad g(x+M, y+N)=(x-y)+(M+N)$$

으로 정의된다.

</div>
<details class="proof" markdown="1">
<summary>증명</summary>

우선 첫 번째 sequence의 경우, 오직 $\ker g\subseteq \im f$인 것만이 자명하지 않은데, 이 또한 $g(x,y)=0$이라 가정하면 $x-y=0$이므로 $x=y$가 되어 $(x,y)\in \im f$여야 한다. 

두 번째 sequence의 경우, 

</details>