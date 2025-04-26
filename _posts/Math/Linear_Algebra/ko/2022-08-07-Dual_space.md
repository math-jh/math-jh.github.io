---

title: "쌍대공간"
excerpt: "쌍대공간, 쌍대사상, 그리고 직교여공간"

categories: [Math / Linear Algebra]
permalink: /ko/math/linear_algebra/dual_space
sidebar: 
    nav: "linear_algebra-ko"

header:
    overlay_image: /assets/images/Math/Linear_Algebra/Dual_space.png
    overlay_filter: 0.5

date: 2022-08-05
last_modified_at: 2022-08-05

weight: 15

---

## 쌍대기저

$V$가 유한차원 $\mathbb{K}$-벡터공간이라 하자. [§선형사상들의 공간, ⁋명제 5](/ko/math/linear_algebra/space_of_linear_maps#prop5)에서 $W=\mathbb{K}$로 두면 $V^\ast=\Hom(V,\mathbb{K})$은 $V$와 같은 차원을 갖는다는 것을 안다. 특히, 만일 $\mathcal{B}=\\{x_1,\ldots, x_n\\}$이 $V$의 basis라면 $x_i$만을 1로, 나머지 $x_j$들은 0으로 보내는 linear map $\xi^i$들의 모임

$$\mathcal{B}^\ast=\{\xi^1,\ldots, \xi^n\}$$

이 $V^\ast$의 basis가 된다는 것을 안다. 이를 $\mathcal{B}$의 *dual basis<sub>쌍대기저</sub>*라 부른다. 

$V$가 무한차원이라 하더라도 basis $\mathcal{B}$에 대하여, 위의 식과 같이 정의된 집합 $\mathcal{B}^\ast$가 일차독립이라는 것은 어떠한 수정도 없이 [§선형사상들의 공간, ⁋명제 5](/ko/math/linear_algebra/space_of_linear_maps#prop5)의 증명과 동일한 증명을 이용할 수 있다. 따라서 항상 $\dim V\leq\dim V^\ast$가 성립하며, 사실 $V$가 무한차원인 경우 반드시 $\dim V<\dim V^\ast$이다. 이를 살펴보기 위해서는 임의의 $\mathcal{B}$의 모든 원소들을 $1$로 보내는 함수를 extend하여 얻이진 함수가 $\mathcal{B}^\ast$의 원소들의 일차결합으로 나타날 수 없음만 확인하면 된다.

## 이중쌍대공간

$V$가 유한차원일 경우 $V$와 $V^\ast$가 같은 차원을 가지며, 따라서 $V^\ast$의 dual space인 $V^{\ast\ast}$ 또한 $V^\ast$와 같은 차원을 갖는 $\mathbb{K}$-벡터공간이 된다. 이를 $V$의 *double dual<sub>이중쌍대공간</sub>*이라 부른다.

$V$와 $V^\ast$가 isomorphic하다는 것을 보이기 위해서는 특정한 basis를 택해야 했다. 반면, $V$에서 $V^{\ast\ast}$로의 <em_ko>basis의 선택에 의존하지 않는</em_ko> 단사인 linear map을 만들 수 있다. $V$와 $V^{\ast\ast}$의 차원이 같으므로, 이 단사인 linear map은 반드시 isomorphism이 되어야 한다.

<div class="definition" markdown="1">

<ins id="def1">**정의 1**</ins> 세 $\mathbb{K}$-벡터공간 $U,V,W$에 대하여, 함수 $f:U\times V\rightarrow W$이 *bilinear*라는 것은 임의의 $u,u_1,u_2\in U$, $v,v_1,v_2\in V$, 그리고 스칼라 $\alpha$에 대하여

$$f(u_1+u_2,v)=f(u_1,v)+f(u_2,v),\qquad f(u,v_1+v_2)=f(u,v_1)+f(u,v_2),\qquad f(\alpha u,v)=\alpha f(u,v)=f(u,\alpha v)$$

가 성립하는 것이다.

</div>

바꾸어 말하자면 이는 임의의 $u\in U$에 대하여 함수 $f(u,-):V\rightarrow W$가 linear이고, 또 임의의 $v\in V$에 대하여 $f(-,v):U\rightarrow W$ 또한 linear라는 뜻이다. 

<div class="definition" markdown="1">

<ins id="def2">**정의 2**</ins> 두 $\mathbb{K}$-벡터공간 $V,W$에 대하여, $V$와 $W$의 *pairing*은 bilinear map $(-,-):V\times W\rightarrow \mathbb{K}$를 의미한다. 만일 영벡터가 아닌 임의의 $v\in V$에 대하여 다음의 linear map

$$(v,-): W\rightarrow \mathbb{K}$$

가 항상 영함수가 아니라면 이 pairing이 *왼쪽에서 non-degenerate*이라 하고, 비슷하게 영벡터가 아닌 임의의 $w\in W$에 대하여

$$(-,w):U\rightarrow \mathbb{K}$$

가 항상 영함수가 아니라면 이 pairing이 *오른쪽에서 non-degenerate*라 한다. 왼쪽과 오른쪽 모두에서 non-degenerate인 pairing을 간단히 *non-degenerate pairing*이라 부른다.

</div>

표기법 $(-,-)$은 순서쌍의 표기법과 동일하여 약간의 혼동이 있을 수도 있지만, 문맥상 둘을 구별하는 것이 어렵지 않고 편하므로 이 표기법을 사용한다.

예를 들어 $V=W=\mathbb{R}^n$ 위에서 정의된 벡터의 내적 $(-,-):\mathbb{R}^n\times\mathbb{R}^n\rightarrow\mathbb{R}$은 non-degenerate pairing이다. 우선 다음의 식

$$(v,w_1+w_2)=(v,w_1)+(v,w_2),\qquad (v_1+v_2,w)=(v_1,w)+(v_2,w),\qquad (\alpha v,w)=\alpha(v,w)=(v,\alpha w)$$

이 성립하는 것은 자명하다. 따라서 벡터의 내적은 pairing이다. 한편 영벡터가 아닌 임의의 벡터 $v$에 대하여 $(v,v)=\lVert v\rVert^2\neq 0$이므로 non-degenerate 조건 또한 만족된다. 

위와 같이 $V=W$인 경우는 특별히 pairing을 *bilinear form*이라 부르기도 한다. 이번 글에서 사용할 예시는 다음의 예시이다.

<div class="example" markdown="1">

<ins id="ex3">**예시 3**</ins> 임의의 $\mathbb{K}$-벡터공간 $V$와, $V$의 dual space $V^\ast$에 대하여 $(-,-):V\times V^\ast\rightarrow \mathbb{K}$를 다음의 식

$$(v,f)=f(v)$$

으로 주면 $(-,-)$은 non-degenerate pairing이다. 우선 고정된 $v\in V$와 임의의 $f,g\in V^\ast$에 대하여

$$(v,f+g)=(f+g)(v)=f(v)+g(v)=(v,f)+(v,g)$$

이고, 또 고정된 $f\in V^\ast$와 임의의 $v_1,v_2\in V$에 대하여

$$(v_1+v_2,f)=f(v_1+v_2)=f(v_1)+f(v_2)=(v_1,f)+(v_2,f)$$

이 성립한다. 비슷하게 임의의 스칼라 $\alpha$에 대하여

$$(\alpha v,f)=f(\alpha v)=\alpha f(v)=(\alpha f)(v)=(v,\alpha f)$$

이 성립하므로 $(-, -)$은 pairing이다. 

뿐만 아니라 $(-,-)$은 non-degenerate이다. 우선 임의의 $f\in V^\ast$가 0이 아니라면 $f(v)\neq 0$이도록 하는 $v$가 존재하므로 $(-,-)$이 오른쪽에서 non-degenerate임은 자명하다. 또, 영벡터가 아닌 임의의 벡터 $v$에 대하여, $v$를 포함하는 basis $\mathcal{B}$를 찾은 후, 위와 같이 dual basis를 만들면, $v$에 대응되는 dual basis의 원소 $\xi$에 대해 $(v,\xi)=1$이므로 $(-,-)$은 왼쪽에서 non-degenerate이기도 하다. 

이로부터 $(-,-)$이 non-degenerate pairing임을 안다. 이를 *canonical pairing*이라 부른다.

</div>

<div class="proposition" markdown="1">

<ins id="prop4">**명제 4**</ins> Non-degenerate pairing $(-,-):V\times W\rightarrow \mathbb{K}$가 주어진 두 $\mathbb{K}$-벡터공간 $V,W$에 대하여, 다음의 식

$$v\mapsto (v,-)$$

으로 정의된 함수 $V\rightarrow W^\ast$는 단사인 linear map이다. 비슷하게, 다음의 식

$$w\mapsto (-,w)$$

으로 정의된 함수 $W\rightarrow V^\ast$도 단사인 linear map이다.

</div>
<details class="proof" markdown="1">
<summary>증명</summary>

이 함수가 linear map이라는 것은 $(-,-)$이 각 성분에 대해 linear이므로 자명하다. 이 함수들이 단사라는 것은 정확히 $(-,-)$이 왼쪽과 오른쪽에서 non-degenerate라는 것이다.

</details>

<div class="proposition" markdown="1">

<ins id="cor5">**따름정리 5**</ins> Non-degenerate pairing $(-,-):V\times W\rightarrow \mathbb{K}$가 주어진 두 <em_ko>유한차원</em_ko> $\mathbb{K}$-벡터공간 $V,W$는 isomorphic하다.

</div>
<details class="proof" markdown="1">
<summary>증명</summary>

두 부등식

$$\dim V\leq\dim W^\ast=\dim W,\qquad \dim W\leq\dim V^\ast=\dim V$$

으로부터 자명하다.

</details>

이러한 의미에서, 두 유한차원 벡터공간 사이의 non-degenerate pairing을 *perfect pairing*이라 부르기도 한다. 특별히 $W=V^\ast$인 [예시 3](#ex3)의 canonical pairing에 이 따름정리를 적용하면 우리는 $V$에서 $V^{\ast\ast}$로의 isomorphism을 얻는다. 명시적으로 이 함수는 임의의 $f\in V^\ast$에 대하여 

$$\ev_v:f\mapsto f(v)$$

으로 정의되는 *evaluation map<sub>값매김사상</sub>*으로 생각하면 된다. 위의 논의는 $v\mapsto \ev_v$로 정의된 $V\rightarrow V^{\ast\ast}$가 isomorphism임을 보여준다.

## 쌍대사상

두 $\mathbb{K}$-벡터공간 $V,W$와 linear map $L:V\rightarrow W$가 주어졌다 하자. 그럼 함수 $L^\ast:W^\ast\rightarrow V^\ast$를 다음의 식

$$L^\ast(f)=f\circ L$$

을 통해 정의할 수 있다. 이는 diagram으로 보면 다음과 같다.

![dual_map](/assets/images/Math/Linear_Algebra/Dual_space-1.png){:style="width:6em" class="invert" .align-center}

혹은, 위에서 정의한 canonical pairing에 따르면 $L^\ast$는 다음의 식

$$(Lv, f)=(v,L^\ast f)\qquad\text{for all $v\in V$ and $f\in W^\ast$}\tag{1}$$

을 통해 정의되었다 할 수 있다. 물론 좌변의 $(-,-)$은 $W$의 canonical pairing이고, 우변의 $(-,-)$은 $V$의 canonical pairing이다. 

특별히 $V,W$가 모두 유한차원 $\mathbb{K}$-벡터공간이라 하자. $V$의 basis를 $\mathcal{B}=\\{x_1,\ldots, x_n\\}$, $W$의 basis를 $\mathcal{C}=\\{y_1,\ldots, y_m\\}$이라 하고 이들의 dual basis를 각각 

$$\mathcal{B}^\ast=\{\xi^1,\ldots,\xi^n\},\qquad\mathcal{C}^\ast=\{\upsilon^1,\ldots,\upsilon^m\}$$

이라 하자. [§선형대수학의 기본정리](/ko/math/linear_algebra/ftla)에 의하여 모든 linear map은 basis의 선택이 주어진다면 행렬로 나타낼 수 있으므로, $L^\ast$를 두 basis $\mathcal{C}^\ast$와 $\mathcal{B}^\ast$에 대한 행렬로 표현할 수 있다. 우선 $L$이 basis $\mathcal{B},\mathcal{C}$에 대해 다음의 행렬

$$[L]_\mathcal{C}^\mathcal{B}=\begin{pmatrix}\alpha_{11}&\alpha_{12}&\cdots&\alpha_{1n}\\\alpha_{21}&\alpha_{22}&\cdots&\alpha_{2n}\\\vdots&\vdots&\ddots&\vdots\\\alpha_{m1}&\alpha_{m2}&\cdots&\alpha_{mn}\end{pmatrix}$$

으로 나타난다 하자. 즉

$$\begin{aligned}L(x_1)&=\alpha_{11}y_1+\alpha_{21}y_2+\cdots+\alpha_{m1}y_m\\L(x_2)&=\alpha_{12}y_1+\alpha_{22}y_2+\cdots+\alpha_{m2}y_m\\&\phantom{a}\vdots\\L(x_n)&=\alpha_{1n}y_1+\alpha_{2n}y_2+\cdots+\alpha_{mn}y_m\end{aligned}$$

이 성립한다. 이제 $L^\ast$를 행렬로 나타내기 위해서는 $\mathcal{C}^\ast$의 원소 각각이 어디로 옮겨지는가를 알면 된다. 임의의 $\upsilon^k\in\mathcal{C}^\ast$에 대하여, $L^\ast(\upsilon^k)=\upsilon^k\circ L$이며, $V^\ast$의 원소로서 이 함수는 $\mathcal{B}^\ast$의 원소들의 일차결합으로 표현된다. 

$$\begin{aligned}L^\ast(\upsilon^1)&=\beta_{11}\xi^1+\beta_{21}\xi^2+\cdots+\beta_{n1}\xi^n\\L^\ast(\upsilon^2)&=\beta_{12}\xi^1+\beta_{22}\xi^2+\cdots+\beta_{n2}\xi^n\\&\phantom{a}\vdots\\L^\ast(\upsilon^m)&=\beta_{1m}\xi^1+\beta_{2m}\xi^2+\cdots+\beta_{nm}\xi^n\end{aligned}$$

이라 하자. 이 때 계수 $\beta_{lk}$을 구하기 위해서는 다음의 식

$$L^\ast(\upsilon^k)=\beta_{1k}\xi^1+\cdots+\beta_{lk}\xi^l+\cdots+\beta_{nk}\xi^n$$

의 양 변에 $x_l$을 대입해보면 된다. 이를 해 보면 우변은 $\beta_{lk}$가 나오며, 좌변은

$$L^\ast(\upsilon^k)(x_l)=\upsilon^k(L(x_l))=\upsilon^k(\alpha_{1l}y_1+\cdots+\alpha_{ml}y_m)=\alpha_{kl}$$

이 된다. 따라서 $\beta_{lk}=\alpha_{kl}$이 성립하고, $L^\ast$의 행렬표현은 다음의 식

$$[L^\ast]_{\mathcal{B}^\ast}^{\mathcal{C}^\ast}=\begin{pmatrix}\alpha_{11}&\alpha_{21}&\cdots&\alpha_{m1}\\\alpha_{12}&\alpha_{22}&\cdots&\alpha_{m2}\\\vdots&\vdots&\ddots&\vdots\\\alpha_{1n}&\alpha_{2n}&\cdots&\alpha_{mn}\end{pmatrix}=\begin{pmatrix}\alpha_{11}&\alpha_{12}&\cdots&\alpha_{1n}\\\alpha_{21}&\alpha_{22}&\cdots&\alpha_{2n}\\\vdots&\vdots&\ddots&\vdots\\\alpha_{m1}&\alpha_{m2}&\cdots&\alpha_{mn}\end{pmatrix}^t=\bigl([L]_\mathcal{C}^\mathcal{B}\bigr)^t$$

을 만족한다. 즉 전치행렬은 별다른 것이 아니라 dual map의 행렬표현에 해당하는 행렬이었던 것이다.

## 직교여공간

우선 다음 명제가 성립한다.

<div class="proposition" markdown="1">

<ins id="prop6">**명제 6**</ins> 두 $\mathbb{K}$-벡터공간 $V,W$, 그리고 linear map $L:V\rightarrow W$와 그 dual $L^\ast:W^\ast\rightarrow V^\ast$가 주어졌다 하자. 

1. 만약 $L$이 단사라면 $L^\ast$는 전사이다.
2. 만약 $L$이 전사라면 $L^\ast$는 단사이다.

</div>
<details class="proof" markdown="1">
<summary>증명</summary>

두 주장 모두 [§선형사상들의 공간, ⁋따름정리 2](/ko/math/linear_algebra/space_of_linear_maps#cor2)에 의해 자명하다. 

1. 만약 $L$이 단사라면 $R\circ L=\id_V$를 만족하는 $R:W\rightarrow V$가 존재한다. 따라서 임의의 $f\in V^\ast$에 대하여, $f\circ R$은 $W$에서 $\mathbb{K}$로의 함수, 즉 $W^\ast$의 원소이고
    
    $$L^\ast(f\circ R)=(f\circ R)\circ L=f\circ(R\circ L)=f\circ\id_V=f$$
    
    를 만족하므로 $L^\ast$는 전사이다. 
2. 만약 $L$이 전사라면 $L\circ S=\id_W$를 만족하는 $S:W\rightarrow V$가 존재한다. 따라서, 만일 어떤 $f\in W^\ast$가 $L^\ast(f)=0$을 만족한다면,
    
    $$L^\ast(f)=f\circ L=0\implies 0=(f\circ L)\circ S=f\circ(L\circ S)=f\circ\id_W=f$$

    이므로 $L^\ast$는 단사이다.

</details>

이 명제는 $\ker L$과 $\im L^\ast$, 그리고 $\im L$과 $\ker L^\ast$ 사이에 특정한 관계가 있다는 것을 암시한다. 우선 다음을 정의하자. 

<div class="definition" markdown="1">

<ins id="def7">**정의 7**</ins> Canonical pairing $(-,-)$이 주어진 $\mathbb{K}$-벡터공간 $V$가 주어졌다 하고, 임의의 부분집합 $S\subseteq V$을 생각하자. 임의의 $v\in S$에 대하여 $(v,f)=0$을 만족하는 $f\in V^\ast$의 모임을 $S$의 *orthogonal complement<sub>직교여공간</sub>* 혹은 *annihilator<sub>소멸자</sub>*라 부르고, $S^\perp$로 표기한다. 

이와 비슷하게, 임의의 부분집합 $T\subseteq V^\ast$가 주어졌다 하자. 그럼 임의의 $f\in T$에 대하여 $(v,f)=0$을 만족하는 $v\in V$의 모임을 $T$의 orthogonal complement라 부르고 $T^\perp$로 표기한다.

</div>

특별히 $S$ 혹은 $T$가 singleton인 경우 이를 $v^\perp$ 혹은 $f^\perp$와 같이 표현하기도 한다. 

임의의 $v\in V$에 대하여 $v^\perp$가 $V^\ast$의 부분공간이 된다는 것은 $(-,-)$이 bilinear라는 사실로부터 자명하다. 이제 다음 등식

$$S^\perp=\bigcap_{v\in S}v^\perp$$

과 [§벡터공간의 기저, ⁋보조정리 3](/ko/math/linear_algebra/basis#lem3)을 이용하면 $S^\perp$가 $V^\ast$의 부분공간임을 안다. 이와 비슷하게 임의의 $T\subseteq V^\ast$에 대하여 $T^\perp$는 $V$의 부분공간이 된다. 

<div class="proposition" markdown="1">

<ins id="prop8">**명제 8**</ins> 두 $\mathbb{K}$-벡터공간 $V,W$, 그리고 linear map $L:V\rightarrow W$와 그 dual $L^\ast:W^\ast\rightarrow V^\ast$가 주어졌다 하자. 임의의 부분공간 $U\subseteq V$와 그 orthogonal complement $U^\perp$에 대하여,

$$L(U)^\perp=(L^\ast)^{-1}(U^\perp)$$

가 성립한다.

</div>
<details class="proof" markdown="1">
<summary>증명</summary>

Dual map $L^\ast$를 canonical pairing을 통해 정의한 식 (1)을 사용하면, 임의의 $\upsilon\in W^\ast$에 대하여

$$\upsilon\in L(U)^\perp\iff (L(u),\upsilon)=0\text{ for all $u\in U$}\iff (u, L^\ast(\upsilon))\text{ for all $u\in U$}\iff L^\ast(\upsilon)\in U^\perp$$

이 성립한다. 

</details>

<div class="proposition" markdown="1">

<ins id="cor9">**따름정리 9**</ins> 두 $\mathbb{K}$-벡터공간 $V,W$, 그리고 linear map $L:V\rightarrow W$와 그 dual $L^\ast:W^\ast\rightarrow V^\ast$가 주어졌다 하자. 그럼 $(\im L)^\perp=\ker(L^\ast)$이 성립한다.

</div>
<details class="proof" markdown="1">
<summary>증명</summary>

[명제 8](#prop8)에서 $U=V$로 두면 된다. Canonical pairing $(-,-)$의 non-degenerate 조건으로부터 $U^\perp=\\{0\\}$이 되어 원하는 결과를 얻는다.

</details>

[명제 8](#prop8)에서 $U\subseteq V$ 대신, $U\subseteq W^\ast$로 시작할 수도 있었다. 이 경우 다음의 명제를 얻는다.

<div class="proposition" markdown="1">

<ins id="prop10">**명제 10**</ins> 두 $\mathbb{K}$-벡터공간 $V,W$, 그리고 linear map $L:V\rightarrow W$와 그 dual $L^\ast:W^\ast\rightarrow V^\ast$가 주어졌다 하자. 임의의 부분공간 $U\subseteq W^\ast$와 그 orthogonal complement $U^\perp$에 대하여,

$$\bigl(L^\ast(U)\bigr)^\perp=L^{-1}(U^\perp)$$

가 성립한다.

</div>
<details class="proof" markdown="1">
<summary>증명</summary>

이 또한 식 (1)을 사용하면, 임의의 $x\in V$에 대하여

$$x\in \bigl(L^\ast(U)\bigr)^\perp\iff (x, L^\ast(\upsilon))=0\text{ for all $\upsilon\in U$}\iff (L(x),\upsilon)=0\text{ for all $\upsilon\in U$}\iff L(x)\in U^\perp$$

이므로 자명하다.

</details>

<div class="proposition" markdown="1">

<ins id="cor11">**따름정리 11**</ins> 두 $\mathbb{K}$-벡터공간 $V,W$, 그리고 linear map $L:V\rightarrow W$와 그 dual $L^\ast:W^\ast\rightarrow V^\ast$가 주어졌다 하자. 그럼 $\bigl(\im L^\ast\bigr)^\perp=\ker L$이 성립한다.

</div>
<details class="proof" markdown="1">
<summary>증명</summary>

[명제 10](#prop10)에서 $U=W^\ast$로 두면 된다.

</details>

---

**참고문헌**

**[Lee]** 이인석, *선형대수와 군*, 서울대학교 출판문화원, 2005.  
**[Bou]** Bourbaki, N. *Algebra I*, Elements of Mathematics. Springer-Verlag Berlin, 1998.  

---