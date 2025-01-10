---

title: "선형사상들의 공간"
excerpt: "Hom과 쌍대공간"

categories: [Math / Linear Algebra]
permalink: /ko/math/linear_algebra/space_of_linear_maps
sidebar: 
    nav: "linear_algebra-ko"

header:
    overlay_image: /assets/images/Math/Linear_Algebra/Space_of_linear_maps.png
    overlay_filter: 0.5

date: 2022-08-05
last_modified_at: 2022-08-05

weight: 11

---

## Extension by linearity

<div class="proposition" markdown="1">

<ins id="thm1">**정리 1 (Extension by linearity)**</ins> 임의의 $\mathbb{k}$-벡터공간 $V$와 basis $\mathcal{B}$가 주어졌다 하자. 또 다른 $\mathbb{k}$-벡터공간 $W$에 대하여, <em_ko>함수</em_ko> $g:\mathcal{B}\rightarrow W$가 주어질 때마다, $g=G\circ\iota$이도록 하는 유일한 <em_ko>linear map</em_ko> $G:V\rightarrow W$가 존재한다.

</div>

여기서 $\iota:\mathcal{B}\rightarrow V$는 포함관계 $\mathcal{B}\hookrightarrow V$를 의미한다.

<details class="proof" markdown="1">
<summary>증명</summary>

주어진 함수 $g$에 대하여, 해당 조건을 만족하는 linear map $G$가 유일해야 한다는 것은 자명하다. 왜냐하면, 만일 $G':V\rightarrow W$가 주어진 조건을 만족하는 또 다른 linear map이라면, 임의의 $v\in V$에 대하여 

$$v=\sum_{x\in \mathcal{B}}v_xx$$

라 하면

$$\begin{aligned}(G-G')\left(\sum_{x\in \mathcal{B}}v_xx\right)&=\sum_{x\in\mathcal{B}}v_x(G-G')(x)=\sum_{x\in\mathcal{B}}v_x(G-G')(\iota(x))\\&=\sum_{x\in\mathcal{B}}v_x(G\circ \iota-G'\circ\iota)(x)=\sum_{x\in\mathcal{B}}v_x(g-g)(x)=0\end{aligned}$$

이 되기 때문이다. 

이제 $G$를 실제로 만들어야 한다. 당연히 임의의 $v=\sum_{x\in\mathcal{B}}v_xx$에 대하여,

$$G(v)=\sum_{x\in\mathcal{B}} v_xg(x)$$

로 *정의*하는 것이 자연스럽다. $v$를 $B$의 원소들의 일차결합으로 쓰는 방법은 유일하므로, $G$는 잘 정의되었으며 어렵지 않게 $G$가 linear map이 된다는 것을 증명할 수 있다.

</details>

즉, 다음의 diagram이 항상 commute하도록 하는 $G:V\rightarrow W$를 찾을 수 있다.

![extend_by_linearity](/assets/images/Math/Linear_Algebra/Space_of_linear_maps-1.png){:style="width:6em" class="invert" .align-center}

반대로 임의의 linear map $G:V\rightarrow W$가 주어진다면 이를 $\mathcal{B}$로 제한하여 함수 $g=G\circ\iota$를 정의할 수 있으며, 위 정리의 유일성 파트에 의하여 이 등식을 만족하는 linear map은 오직 $G$ 뿐이다. 따라서 다음 두 집합 사이의 전단사함수가 존재한다.

$$\{\text{functions from $\mathcal{B}$ to $W$}\}\longleftrightarrow\{\text{linear maps from $V$ to $W$}\}$$

즉 $V$에서 $W$로의 linear map은 $L$이 basis $\mathcal{B}$ 위에서 어떻게 행동하는지에 의해 완벽하게 결정되며, 만일 $V$가 유한차원이었다면 이는 linear map $L$이 오직 <em_ko>유한 개</em_ko>의 원소에서의 함수값에 의해서만 결정된다는 의미가 된다.

특별히 공역 $W$ 또한 유한차원 $\mathbb{k}$-벡터공간이라 가정하고, $V$의 기저 $\mathcal{B}=\\{x\_1,\ldots, x\_n\\}$, 그리고 $W$의 기저 $\mathcal{C}=\\{y_1,\ldots,y_m\\}$를 고정하자. 그럼 앞선 논증에 의해 $V$에서 $W$로의 linear map $L$은 $W$의 $n$개의 벡터들

$$L(x_1),L(x_2)\ldots, L(x_n)$$

에 의해 완벽하게 결정되며, $W$의 원소로서 이들은 다시 $\mathcal{C}$의 원소들의 일차결합

$$\begin{aligned}L(x_1)&=\alpha_{11}y_1+\alpha_{21}y_2+\cdots+\alpha_{m1}y_m\\L(x_2)&=\alpha_{12}y_1+\alpha_{22}y_2+\cdots+\alpha_{m2}y_m\\&\phantom{a}\vdots\\L(x_n)&=\alpha_{1n}y_1+\alpha_{2n}y_2+\cdots+\alpha_{mn}y_m\end{aligned}\tag{1}$$

으로 표현해줄 수 있다. 그럼 $V$의 임의의 원소에서의 $L$의 값은 스칼라들 $\alpha_{i,j}$, 좌표표현 $v=\sum_{i=1}^n v_ix_i$에서 등장하는 스칼라들 $v_1,\ldots, v_n$들을 이용해 basis $\mathcal{C}$에 의한 일차결합으로 나타낼 수 있다. 

$$\begin{aligned}L(v_1x_1)&=\alpha_{11}v_1y_1+\alpha_{21}v_1y_2+\cdots+\alpha_{m1}v_1y_m\\L(v_2x_2)&=\alpha_{12}v_2y_1+\alpha_{22}v_2y_2+\cdots+\alpha_{m2}v_2y_m\\&\phantom{a}\vdots\\L(v_nx_n)&=\alpha_{1n}v_ny_1+\alpha_{2n}v_ny_2+\cdots+\alpha_{mn}v_ny_m\end{aligned}$$

이므로, 각 변을 더하면 좌변은

$$L(v_1x_1)+L(v_2x_2)+\cdots+L(v_nx_n)=L(v_1x_1+v_2x_2+\cdots+v_nx_n)=L(v)$$

그리고 우변은

$$(\alpha_{11}v_1+\alpha_{12}v_2+\cdots+\alpha_{1n}v_n)y_1+(\alpha_{21}v_1+\alpha_{22}v_2+\cdots+\alpha_{2n}v_n)y_2+\cdots+(\alpha_{m1}v_1+\alpha_{m2}v_2+\cdots+\alpha_{mn}v_n)y_m$$

이 된다. 따라서 $L$은 다음의 대응

$$v=\sum_{i=1}^n v_ix_i\quad\mapsto\quad \sum_{j=1}^m\left(\sum_{i=1}^n\alpha_{ji}v_i\right)y_j=L(v)$$

으로 이해할 수 있다.

위의 정리를 이용하면 [\[집합론\] §Retraction과 section, ⁋명제 1](/ko/math/set_theory/retraction_and_section#prop1)에 대응되는 다음 명제를 증명할 수 있다.

<div class="proposition" markdown="1">

<ins id="cor2">**따름정리 2**</ins> 두 $\mathbb{k}$-벡터공간 $V,W$와 linear map $L:V\rightarrow W$가 주어졌다 하자.

1. 만일 $L$이 단사함수라면, 적당한 linear map $R:W\rightarrow V$가 존재하여 $R\circ L=\id_V$이다.
2. 만일 $L$이 전사함수라면, 적당한 linear map $S:W\rightarrow V$가 존재하여 $L\circ S=\id_W$이다.

</div>
<details class="proof" markdown="1">
<summary>증명</summary>

1. 우선 $L$이 단사함수라 하고, $V$의 basis $x_1,\ldots,x_n$을 택하자. 그럼 $L(x_1),\ldots, L(x_n)$은 일차독립이고, 따라서 이들을 포함하는 $W$의 basis $\mathcal{B}$를 찾을 수 있다. 이제 함수 $r:\mathcal{B}\rightarrow V$를 다음의 식
    
    $$r(v)=\begin{cases}x_i&\text{if $v=L(x_i)$}\\0&\text{otherwise}\end{cases}$$

    으로 정의하고, 여기에 [정리 1](#thm1)을 적용하여 얻어진 linear map을 $R$이라 하자. 그럼 $V$의 basis $\\{x_1,\ldots,x_n\\}$의 임의의 원소 $x_i$에 대하여 $(R\circ L)(x_i)=x_i$이고, 따라서 정리 1의 유일성 부분에 의하여 $R\circ L=\id_V$가 성립한다.

2. $L$이 전사함수라 하고, $V$의 basis $x_1,\ldots,x_n$을 택하자. 그럼 $L(x_1),\ldots, L(x_n)$은 $W$를 span하므로 이 벡터들 중 일부를 택하여 $W$의 basis $\mathcal{B}$를 찾을 수 있다. 일반성을 잃지 않고 $\mathcal{B}=\\{L(x_1),\ldots, L(x_m)\\}$ ($m\leq n$)이라 하자. 함수 $s:\mathcal{B}\rightarrow V$를 다음의 식
    
    $$s(v)=x_k\qquad v=L(x_k)$$

    으로 정의하고, 여기에 [정리 1](#thm1)을 적용하여 얻어진 linear map을 $S$라 하자. 이제 $W$의 basis $\mathcal{B}$의 임의의 원소 $L(x_k)$에 대하여 $(L\circ S)(L(x_k))=L(x_k)$이므로 다시 정리 1의 유일성 부분에 의하여 $L\circ S=\id_W$가 성립한다.

</details>

## 선형사상들의 공간

<div class="proposition" markdown="1">

<ins id="lem3">**보조정리 3**</ins> 두 $\mathbb{k}$-벡터공간 $V$, $W$를 생각하자. $L,L_1,L_2$이 $V$에서 $W$로의 linear map들이고,  $\alpha\in\mathbb{k}$라면

$$L_1+L_2:v\mapsto L_1(v)+L_2(v),\qquad \alpha L:v\mapsto \alpha L(v)$$

들도 linear이다.

</div>
<details class="proof" markdown="1">
<summary>증명</summary>

$v, v_1,v_2\in V$이고, $\alpha\in\mathbb{k}$라 하자. 그럼

$$\begin{aligned}
        (L_1+L_2)(v_1+v_2)&=L_1(v_1+v_2)+L_2(v_1+v_2)\\
        &=L_1(v_1)+L_1(v_2)+L_2(v_1)+L_2(v_2)\\
        &=L_1(v_1)+L_2(v_1)+L_1(v_2)+L_2(v_2)\\
        &=(L_1+L_2)(v_1)+(L_1+L_2)(v_2)
    \end{aligned}$$

이고,

$$\begin{aligned}
        (L_1+L_2)(\alpha v)&=L_1(\alpha v)+L_2(\alpha v)=\alpha L_1(v)+\alpha L_2(v)\\
        &=\alpha(L_1(v)+L_2(v))\\
        &=\alpha (L_1+L_2)(v).
    \end{aligned}$$
    
이므로 $L_1+L_2$은 linear map이 된다. 두 번째 주장도 비슷하게 보일 수 있다.

</details>

따라서, 다음을 정의할 수 있다.

<div class="definition" markdown="1">

<ins id="def4">**정의 4**</ins> 두 $\mathbb{k}$-벡터공간 $V,W$에 대하여, $V$에서 $W$로의 linear map들의 집합에 [보조정리 3](#lem3)의 연산을 준 $\mathbb{k}$-벡터공간을 $\Hom_\mathbb{k}(V,W)$, 혹은 문맥에 따라 field $\mathbb{k}$가 명확할 때는 $\Hom(V,W)$로 적는다. 

특별히 $W=\mathbb{k}$일 경우, $\Hom(V,\mathbb{k})$를 $V$의 *dual space<sub>쌍대공간</sub>*이라 부르고 $V^\*$으로 적는다. $V^\ast$의 원소들을 *linear functional*들이라 부른다. 

</div>

벡터공간 $\Hom(V,W)$에서 영벡터에 해당하는 원소는 모든 원소를 0으로 보내는 함수 $0$이다. ([§선형사상, ⁋예시 10](/ko/math/linear_algebra/linear_map#ex10)) 이 함수를 지칭할 때는 편의상 영함수라 지칭하자.

두 공간 $V,W$가 모두 유한차원이고, $\mathcal{B}=\\{x_1,\ldots, x_n\\}$, $\mathcal{C}=\\{y_1,\ldots, y_m\\}$이 $V,W$ 각각의 basis라 하자. $\mathcal{B}$에서 $W$로의 $mn$개의 함수들

$$f_i^j(x)=\begin{cases}y_j&\text{if $x=x_i$}\\0&\text{otherwise}\end{cases}$$

을 생각하자. 즉 $f_i^j$는 <em_ko>오직</em_ko> $x_i$ 하나만을 $y_j$로 보내고, 나머지는 모두 0으로 보내는 함수이다. 그럼 [정리 1](#thm1)에 의하여 $f_i^j=B_i^j\circ\iota$이도록 하는 linear map $B_i^j$가 유일하게 존재한다. 

<div class="proposition" markdown="1">

<ins id="prop5">**명제 5**</ins> 두 유한차원 $\mathbb{k}$-벡터공간 $V,W$가 각각 basis $\\{x_1,\ldots,x_n\\}$, $\\{y_1,\ldots,y_m\\}$을 갖는다 하자. 그럼 $\Hom(V,W)$는 $mn$차원 벡터공간이며, 이 때 위의 $mn$개의 linear map들 $B_i^j$가 $\Hom(V,W)$의 basis가 된다.

</div>
<details class="proof" markdown="1">
<summary>증명</summary>

Basis에 대한 주장만 보이면 충분하다.

우선 $B_i^j$들은 일차독립이다. 스칼라들 $\alpha_{11},\ldots,\alpha_{mn}$에 대하여,

$$\alpha_{11}B_1^1+\alpha_{12}B_2^1+\cdots+\alpha_{mn}B_n^m=0$$

이라 가정하자. 즉 양 변은 $V$에서 $W$로의 영함수이며, 따라서 임의의 $v\in V$에 대하여 다음의 식

$$\alpha_{11}B_1^1(v)+\alpha_{12}B_2^1(v)+\cdots+\alpha_{mn}B_n^m(v)=0$$

이 성립한다. 특히 이 식은 $v=x_1,\ldots, x_n$일 때에도 성립하며, 이 때

$$\alpha_{11}B_1^1(x_k)+\alpha_{12}B_2^1(x_k)+\cdots+\alpha_{mn}B_n^m(x_k)=0$$

이다. 그런데 $B_i^j$의 정의에 의하여, $B_i^j(x_k)$는 오직 $i=k$일 때만 값 $y_j$가 나오므로 위의 식은

$$\alpha_{1k}y_1+\alpha_{2k}y_2+\cdots+\alpha_{mk}y_k=0$$

이 된다. 이제 $y_1,\ldots,y_k$는 일차독립이므로 $\alpha_{1k},\ldots,\alpha_{mk}$는 모두 $0$이다. $k$는 임의로 택할 수 있으므로 $\alpha_{11},\ldots,\alpha_{mn}$는 모두 0이고 $B_i^j$는 일차독립이다.

한편 이들 $B_i^j$는 $\Hom(V,W)$를 span한다. 임의의 $L\in\Hom(V,W)$가 주어졌다 하자. 그럼 도입부의 식 (1)을 만족하는 스칼라들 $\alpha_{11},\ldots,\alpha_{mn}$을 찾을 수 있다. 이제 다음의 식

$$L'(v)=\sum_{i,j}\alpha_{ji}B_i^j(v)$$

으로 정의된 $L'$는 linear map이다. 뿐만 아니라, $v=x_k$를 대입하면

$$L'(x_k)=\sum_{i,j}\alpha_{ji}B_i^j(x_k)=\sum_{j=1}^m\alpha_{jk}B_k^j(x_k)=\sum_{j=1}^m\alpha_{jk}y_j=L(x_k)$$

가 된다. 이제 [정리 1](#thm1)의 유일성 파트에 의하여 $L'=L$이 성립한다.

</details>

