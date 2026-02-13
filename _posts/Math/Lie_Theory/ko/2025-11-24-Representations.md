---

title: "리 군의 표현"
excerpt: ""

categories: [Math / Lie Theory]
permalink: /ko/math/Lie_theory/representations
header:
    overlay_image: /assets/images/Math/Lie_Theory/Representations.png
    overlay_filter: 0.5
sidebar: 
    nav: "Lie_theory-ko"

date: 2025-11-24
last_modified_at: 2025-11-24
weight: 2

---

그냥 이 부분은 풀톤 갖고 따로--

 Lie group의 경우 이러한 철학은 더 각별한데, Lie group의 대표적인 예시인 $\GL(n;\mathbb{R})$이나 $\Diff(M)$ 등을 생각하면 이들은 그 본질부터가 다른 대상 위에 act하는 것이기 때문이다. 이번 글에서 우리는 Lie group의 finite-dimensional representation을 살펴본다.

{% comment %}
나중에 표현론 카테고리 만들면 빼기
{% endcomment %}

## 표현론의 기본 개념

우선 우리는 유한군의 표현론을 살펴본다. 임의의 finite group은 discrete topology와 자명한 미분구조가 주어진 Lie group이라 생각할 수 있으므로 이는 앞으로 살펴볼 일반적인 경우의 특수한 케이스로 생각할 수 있다. 그러나 이 일반화의 과정은 상당히 단순한 것이며, 이 일반화 하에서 모든 원하는 결과들이 성립하므로 사실상 이 섹션에 우리의 주장들이 모두 담겨있다고 생각하여도 된다. 

## 마슈케의 정리

우리가 앞서 도입한 $V$의 $G$-invariant subspace

$$V^G=\{v\in V\mid g\cdot v=v\text{ for all $g\in G$}\}$$

는 흥미로운 성질이 있는데, 함수 $p: V \rightarrow V^G$를 다음의 식

$$p(v)=\frac{1}{\lvert G\rvert}\sum_{g\in G}g\cdot v$$

으로 정의하면 이것이 $G$-invariant projection이 된다는 것이다. 이 함수에 대한 아이디어는 $v\in V$를 $G$ 전체에 대해 돌려가며 평균을 내는 것으로, 앞으로도 이 아이디어는 종종 접하게 될 것이다. 







## 슈어 직교성

이제 우리는 decomposition (1)에 표현론적인 의미를 부여한다. 이를 위해 다음 보조정리부터 시작한다. 

<div class="proposition" markdown="1">

<ins id="lem8">**보조정리 8 (Schur)**</ins> (Compact) group $G$와 irreducible $G$-module들 $V,W$가 주어졌다 하자. 그럼 다음이 성립한다. 

1. 임의의 $G$-map $V\rightarrow W$는 zero map이거나 isomorphism이다. 
2. 임의의 $G$-automorphism $f\in \Aut_G(V)$는 $f(v)=\lambda v$의 꼴이다. 
3. $G$-map들의 모임 $\Hom_G(V,W)$은 $\mathbb{C}$이거나 $0$이다. 

</div>
<details class="proof" markdown="1">
<summary>증명</summary>

1. 이는 kernel과 image를 각각 생각하면 자명하다. 
2. 주어진 $f$는 $G$-linear map이기 이전에 $\mathbb{C}$-linear map이므로, $f$의 eigenvalue $\lambda$가 존재한다. 이제 이 eigenvalue에 대응되는 eigenspace를 $W$라 하고, 이것이 실은 $G$-submodule이 됨을 보이면 된다. 
3. 위의 두 명제에 의해 자명하다. 

</details>

이를 사용하면 우리는 다음 명제를 얻는다. 

<div class="proposition" markdown="1">

<ins id="prop9">**명제 9**</ins> 위와 같은 상황에서, 다음의 함수 

$$d=\bigoplus_{W\in\Irr(G, \mathbb{C})} d_W:\bigoplus_{W\in \Irr(G, \mathbb{C})}\Hom_G(W,V)\otimes_\mathbb{C}W\rightarrow V$$

는 isomorphism이다. 

</div>

이에 대한 증명은, $V$가 irreducible decomposition $V=\bigoplus V_j$을 가지므로 다음의 식

$$\Hom_G(W, V)=\Hom_G\left(W, \bigoplus V_j\right)\cong \bigoplus \Hom_G(W, V_j) $$

과 [보조정리 8](#lem8)에 의해 자명하다. 즉 복잡하게 써 두기는 했지만, 위의 $d$는 각각의 irreducible $G$-module $W$(의 isomorphism class)들이 $V$ 안에 얼마나 들어있는지를 세는 것이며, 따라서 다음 정의가 자연스럽다. 

<div class="definition" markdown="1">

<ins id="def10">**정의 10**</ins> 위의 함수에 의한 $W\in\Irr(G, \mathbb{C})$의 image를 $V$의 *$W$-isotypical summand*라 부르고, $\Hom_G(W, V)$를 $W$의 *multiplicity*라 부른다. 

</div>

약간의 믿음을 가지면 이러한 표현이 유일하다는 것도 납득할 수 있다. 

이제 우리는 다음을 정의한다. 

<div class="definition" markdown="1">

<ins id="def11">**정의 11**</ins> $G$의 representation $\rho:G\rightarrow\Aut(V)$에 대응하는 *character* $\chi_\rho:G\rightarrow\mathbb{C}$를

$$\chi_\rho(g)=\tr(\rho(g))$$

으로 정의한다. 

</div>

그 정의에 의하여 character $\chi_\rho$는 conjugacy class들 위에서 상수이다. 이러한 함수들에도 다음과 같은 이름을 붙인다. 

<div class="definition" markdown="1">

<ins id="def12">**정의 12**</ins> 함수 $f:G\rightarrow\mathbb{C}$가 class function이라는 것은 $f(hgh^{-1})=f(g)$가 모든 $g,h\in G$에 대해 성립하는 것이다. 

</div>

우리가 character function들과 class function들에 관심을 갖는 이유는 다음의 명제에 있다. 

<div class="proposition" markdown="1">

<ins id="prop13">**명제 13**</ins> Finite group $G$의 representation $\rho:G\rightarrow\Aut(V)$를 고정하자. 그럼 다음이 성립한다. 

1. 만일 $\rho\cong\rho'$이면 $\chi_\rho=\chi_{\rho'}$이 성립한다. 
2. $\chi_{V\oplus W}=\chi_V+\chi_W$이 성립한다. 
3. $\chi_{V\otimes W}=\chi_V \chi_W$이 성립한다.  

</div>

이에 대한 증명은 단순한 선형대수에 불과하다. 

Class function들의 공간은 inner product

$$\langle f,g\rangle_G:=\frac{1}{\lvert G\rvert}\sum_{x\in G}f(x)\overline{g(x)}$$

를 갖는다. 이는 단순히 이제 $V,W$가 irreducible $G$-module이라 하자. 임의의 $f\in\Hom_\mathbb{C}(V,W)$에 대하여,

$$p_f:=\frac{1}{|G|}\sum_{g\in G}\rho_W(g)\circ f\circ\rho_V(g^{-1})$$

으로 정의하면 $G$-map $V\rightarrow W$을 얻는다. 우리는 [보조정리 8](#lem8)에 의하여 이 함수는 zero map이거나 isomorphism인 것을 알고 있다. 실제로 만일 $V\not\cong W$이면 $p_f=0$이고 $V=W$이면 $p_f=\lambda_f\cdot\id_V$ ($\lambda_f\in\mathbb{C}$)인 것을 확인할 수 있으며, 따라서 다음의 식

$$\langle\chi_V,\chi_W\rangle_G=\delta_{VW}$$

이 성립하는 것을 안다. 즉, irreducible representation의 character들은 class function들의 공간에서 orthonormal basis를 준다. 여기에서 각각의 $\Mat_{n_i}(\mathbb{C})$는 simple $\mathbb{C}[G]$-module이다. 한편, 우리는 $\mathbb{C}[G]$의 center $Z(\mathbb{C}[G])$에 대하여, 위의 분해에 따르면

$$Z(\mathbb{C}[G])=\mathbb{C}I_{n_1}\oplus \cdots\oplus \mathbb{C}I_{n_r}$$

이므로 $Z(\mathbb{C}[G])$는 $r$차원 벡터공간이다. 그런데 임의의 $f=\sum f_xx\in \mathbb{C}[G]$에 대하여, 

$$f\in Z(\mathbb{C}[G])\iff y\left(\sum_{x\in G}f_xx\right)y^{-1}=f\iff \sum_{x\in G}f_xyxy^{-1}=f\iff \sum_{x\in G}f_{y^{-1}xy}x=f$$

이 성립하므로, $f\in Z(\mathbb{C}[G])$이 성립하는 것은 $f_x$들 각각이 conjugacy class 위에서 상수인 것과 동치이다. 즉 위에서 구한 $r$은 정확하게 $G$의 conjugacy class의 개수와 같다. 

바꿔 말하자면, 우리는 앞서 $G$의 irreducible decomposition들에 해당하는 character들이 orthonormal함을 확인하였으며, 이들은 적어도 $r$개가 존재한다. 그러나 이러한 것들은 많아야 $r$개 존재하므로, 이로부터 우리는 앞선 orthonormal set이 정확하게 orthonormal basis가 된다는 것을 안다. 

<div class="proposition" markdown="1">

<ins id="thm14">**정리 14 (Schur orthogonality)**</ins>  $G$의 서로 다른 isomorphism class에 속하는 irreducible representation $\rho,\rho'$에 대하여

$$\langle\chi_\rho,\chi_{\rho'}\rangle_G=\delta_{\rho\rho'}$$

가 성립한다. 특히 ${\chi_\rho}_{\rho\in\Irr(G,\mathbb{C})}$는 class function들의 모임 위에 orthonormal basis를 이룬다. 

</div>

따라서 임의의 두 $\mathbb{C}[G]$-module이 isomorphic한 것과 character function이 같은 것이 정확히 동치인 것을 안다. 

<div class="example" markdown="1">

<ins id="ex15">**예시 15**</ins> 우리는 $S_3$에 대하여 지금까지의 논의를 적용해본다. $S_3$은 세 개의 conjugacy class를 가지며, 이들은 각각 다음의 원소들

$$e,\quad (1,2),\quad (1,2,3)$$

로 대표된다. 그럼 위의 계산으로부터 이들은 각각 $1$차원, $1$차원, $2$차원이 되고, $1^2+1^2+2^2=6$이므로 우리가 놓친 것이 없는 것을 안다. 

구체적으로 $e$의 conjugacy class에 해당하는 trivial representation은 

$$\rho_1:S_3\rightarrow \Aut(\mathbb{C});\qquad \sigma\mapsto \id_\mathbb{C}$$

이며, $(1,2)$의 conjugacy class에 해당하는 representation은

$$\rho_2:S_3 \rightarrow \Aut(\mathbb{C});\qquad \sigma\mapsto \sgn(\sigma)\in\Aut(\mathbb{C})$$

이다. 마지막으로 $(1,2,3)$의 conjugacy class에 해당하는 representation은

$$\rho_3: S_3\rightarrow \Aut(\mathbb{C}^3);\qquad \sigma\mapsto \left((x_1,x_2,x_3)\mapsto (x_{\sigma(1)},x_{\sigma(2)},x_{\sigma(3)})$$

에서, 이 representation이 $x_1+x_2+x_3=0$ 평면에 대해서는 invariant이므로 그 orthogonal complement를 택하면 2차원의 representation을 얻는다. 

$V_2$의 기저 $\{e_1-e_2, e_2-e_3\}$에 대해:
$$\rho_2((12))=\begin{pmatrix}0&1\\1&0\end{pmatrix}, \quad \rho_2((123))=\begin{pmatrix}0&-1\\1&-1\end{pmatrix}$$

| Class | Size | $V_0$ | $V_1$ | $V_2$ |
|-------|------|-------|-------|-------|
| $\{e\}$ | 1 | 1 | 1 | 2 |
| $\{3\text{-cycles}\}$ | 2 | 1 | 1 | -1 |
| $\{2\text{-cycles}\}$ | 3 | 1 | -1 | 0 |

</div>

## Compact Lie group

이제 우리는 지금까지의 결과를 Lie group으로 옮길 수 있다는 것을 설명한다. 이는 간단한데, convolution algebra를 정의할 때 $G$에서 $\mathbb{C}$로의 모든 함수들의 모임 대신 $G$에서 $\mathbb{C}$로의 smooth function들의 모임들을 생각하고, 이 위에 전통적인 convolution을 정의하면 된다. 물론 이를 위해서는 $G$ 위에 정의된 적분이 필요하지만, 이는 Haar measure를 사용하면 된다.

<div class="example" markdown="1">

<ins id="ex16">**예시 16**</ins> $SO(2)\cong U(1)=\{z\in\mathbb{C}\mid |z|=1\}$는 아벨 군으로, 모든 기약표현은 1차원이다. 각 정수 $n\in\mathbb{Z}$에 대하여,

$$\chi_n(e^{i\theta})=e^{in\theta}$$

으로 정의되는 character $\chi_n$이 $U(1)$의 기약표현을 모두준다. 이들은 서로 동형이 아니며, 다음의 직교관계가 성립한다:

$$\langle\chi_m,\chi_n\rangle_{U(1)}=\frac{1}{2\pi}\int_0^{2\pi} e^{i(m-n)\theta}d\theta=\delta_{mn}$$

</div>
<div class="example" markdown="1">

<ins id="ex17">**예시 17**</ins> $SU(2)$는 3차원 compact Lie group으로, 각 $n\in\mathbb{N}$에 대하여 $(n+1)$차원의 기약표현 $V_n$이 존재한다. $V_n$은 동차다항식 공간

$$V_n = \{p:\mathbb{C}^2\to\mathbb{C}\mid p\text{ is homogeneous of degree }n\}$$

으로 이해할 수 있으며, $g=\begin{pmatrix}a&b\\-\overline{b}&\overline{a}\end{pmatrix}\in SU(2)$의 작용은 $(g\cdot p)(z)=p(g^{-1}z)$이다.

$V_n$의 character는

$$\chi_n\begin{pmatrix}e^{i\theta}&0\\0&e^{-i\theta}\end{pmatrix}=e^{in\theta}+e^{i(n-2)\theta}+\cdots+e^{-in\theta}$$

으로 주어지며, Weyl character formula의 가장 간단한 예시이다. 특히 $V_1\cong\mathbb{C}^2$는 표준표현, $V_2\cong\mathbb{R}^3$은 adjoint 표현에 동형이다.

</div> 

## 리 대수의 표현

우리는 Lie group의 infinitesimal한 정보가 모두 그 Lie algebra에 들어있는 것을 알고, 적당한 위상적인 조건들 하에서 Lie algebra의 정보는 Lie group을 복원해내는데에 충분하다는 것을 안다. 그렇다면, 적어도 철학적으로는 Lie group의 representation의 infinitisimal한 정보를 Lie algebra의 representation에 담아줄 수 있을 것이다. 그리고 이는 정당한 직관이다. 

임의의 $G$-module $V$가 주어졌다 하자. 그럼 $V$를 manifold로 본다면, 우리는 임의의 $X\in \mathfrak{g}$와 임의의 $v\in V$에 대하여, $v$에서 출발하여 $X$가 지정해주는 방향으로 움직이는 곡선 

$$t\mapsto\exp(tX)\cdot v$$

이 존재함을 안다. 그럼 이 action의 infinitesimal한 정보는 다음의 식

$$\mathcal{L}_X v:=\lim_{t \rightarrow 0}\frac{\exp(tX)\cdot v-v}{t}$$

에 담겨있는 것을 안다. 만일 우리가 $G$-module $V$를 $\rho:G\rightarrow \Aut(V)$로 해석한다면, 우변은 $\Aut(V)$의 Lie algebra에 해당하는 $\End(V)$의 원소이며, 더 나아가 $d\rho_e(X)$가 된다는 것을 안다. 즉 다음의 대응

$$\mathfrak{g}\times V \rightarrow V;\qquad (X,v)\mapsto \mathcal{L}_Xv$$

은 $G\times V \rightarrow V$의 infinitesimal한 버전으로 생각할 수 있으며, 이 대응은 그 자체로 *Lie algebra의 representation*을 준다. 여기서, 임의의 Lie algebra $L$과 벡터공간 $V$에 대하여 $L\times V \rightarrow V$가 Lie algebra representation이기 위해 우리가 요구하는 관계식은

$$X(Yv)-Y(Xv)=[X,Y]v$$

이다. 약간의 믿음을 가지면 simply connected Lie group $G$과 그 Lie algebra $\mathfrak{g}$에 대해서는 ([§리 군, ⁋정리 15](/ko/math/Lie_theory/Lie_groups#thm15)와 마찬가지 결과로) Lie algebra representation $\mathfrak{g}\times V \rightarrow V$이 Lie group의 representation $G\times V \rightarrow V$를 결정하는 것도 납득할 수 있다. 

이는 root systems나 Weyl group 등 후속 주제로 이어진다. 
