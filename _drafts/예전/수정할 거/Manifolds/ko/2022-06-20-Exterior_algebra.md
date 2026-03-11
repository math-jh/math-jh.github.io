---

title: "외대수"
excerpt: "Exterior algebra"

categories: [Math / Manifold]
permalink: /ko/math/manifold/exterior_algebra
header:
    overlay_image: /assets/images/Manifold/Exterior_algebra.png
    overlay_filter: 0.5
sidebar: 
    nav: "manifold-ko"

date: 2022-06-20
last_modified_at: 2022-06-20
weight: 12

---

우리는 이제 미분형식을 정의할 것인데, 우선은 조금 더 대수적인 세팅에서 이야기를 시작한다. 이번 글에서 $u,v$와 같은 영어 소문자들은 벡터공간 $V$의 원소를, $\alpha,\beta$와 같은 그리스 소문자들은 $V^\ast$의 원소들을 의미한다. 

## 외대수

유한차원 $\mathbb{R}$-벡터공간 $V$를 고정하고, commutative monoid $\Delta=\mathbb{N}\times\mathbb{N}$이 주어졌다 하자. 그럼 임의의 $(r,s)\in\Delta$에 대하여, $V$에 대한 *$(r,s)$-tensor space*를 다음의 식

$$T^{r,s}(V)=\underbrace{V\otimes\cdots\otimes V}_\text{$r$ copies}\otimes\underbrace{V^\ast\otimes\cdots\otimes V^\ast}_\text{$s$ copies}$$

으로 정의한다. 특별히 $r=s=0$인 경우는 $T^{0,0}(V)=\mathbb{R}$인 것으로 생각한다. 이제 direct sum

$$T^{\bullet,\bullet}(V)=\bigoplus_{(r,s)\in\Delta} T^{r,s}(V)$$

를 생각하면 $T^{\bullet,\bullet}$이 gradation $\Delta$가 주어진 $\mathbb{R}$-벡터공간이 되는 것은 자명하다. 뿐만 아니라, $T^{\bullet,\bullet}(V)$의 두 원소 (*simple tensor*들)

$$v=v_1\otimes v_2\otimes\cdots\otimes v_{r_1}\otimes \alpha^1\otimes \alpha^2\otimes\cdots\otimes \alpha^{s_1}, \quad u=u_1\otimes u_2\otimes\cdots\otimes u_{r_2}\otimes \beta^1\otimes \beta^2\otimes\cdots\otimes \beta^{s_2}$$

에 대하여 곱셈 $u\otimes v$를

$$u\otimes v=v_1\otimes \cdots\otimes v_{r_1}\otimes u_1\otimes \cdots\otimes u_{r_2}\otimes \alpha^1\otimes\cdots\otimes \alpha^{s_1}\otimes \beta^1\otimes\cdots\otimes \beta^{s_2}\in T^{r_1+r_2, s_1+s_2}(V)\tag{1}$$

으로 정의하면 이를 통해 $T^{\bullet,\bullet}(V)$의 임의의 두 원소의 곱을 정의할 수 있으며, 이 곱셈이 gradation을 잘 따른다는 것을 알 수 있다. 즉 $T^{\bullet,\bullet}(V)$는 gradation $\Delta$가 주어진 $\mathbb{R}$-algebra가 된다. 우리는 $T^{\bullet,\bullet}(V)$를 $V$ 위에서의 *mixed tensor algebra*라 부르고, 이들의 원소를 *mixed tensor*라 부른다.

$T^{\bullet,\bullet}(V)$의 두 ($\mathbb{N}$-graded) subalgebra

$$T^{0,\bullet}(V)=\bigoplus_{k\geq 0} T^{0,k}(V),\quad T^{\bullet,0}(V)=\bigoplus_{k\geq 0} T^{k,0}(V)$$

가 관심의 대상이 되는데, $T^{0,\bullet}(V)$의 원소들을 *covariant tensor*들, 그리고 $T^{\bullet,0}(V)$의 원소들을 *contravariant tensor*들이라 부른다. 특별히 후자의 경우를 앞으로 종종 사용하게 되므로, $T^{k,0}(V)$ 대신 $T^k(V)$, $T^{\bullet,0}(V)$ 대신 $T(V)$로 적고, $T(V)$를 $V$ 위에서의 *tensor algebra*라 부르기로 한다.

임의의 $x\in V$에 대하여, $x\otimes x$는 항상 $T(V)$의 원소임이 자명하다. 이러한 꼴을 갖는 원소들로 만들어지는 $T(V)$의 ideal을 $I(V)$라 하자. $I(V)$는 차수가 2인 homogeneous한 원소들로 생성된 ideal이므로, 다음의 식

$$I(V)=\bigoplus_{k\geq 0} I(V)\cap T^{k}(V)$$

이 성립하며, $T(V)/I(V)$ 또한 자연스러운 gradation

$$T(V)/I(V)=\bigoplus_{k\geq 0} T^{k}(V)/(I(V)\cap T^{k}(V))$$

을 갖는다. 

<div class="definition" markdown="1">

<ins id="df1">**정의 1**</ins> 위에서 정의한 $\mathbb{N}$-graded $\mathbb{R}$-algebra $T(V)/I(V)$를 $V$에서 정의된 *exterior algebra<sub>외대수</sub>*라 부르고, $\bigwedge(V)$로 적는다.

</div>

앞으로는 논의의 간결함을 위하여

$$I^k(V)=I(V)\cap T^{k}(V),\quad \bigwedge\nolimits^k(V)=T^{k}(V)/I^k(V)$$

으로 적기로 한다. 

Graded $\mathbb{R}$-algebra $T(V)$의 quotient algebra로서, $\bigwedge(V)$ 또한 graded $\mathbb{R}$-algebra가 되며, 특히 식 (1)로 정의한 곱셈구조를 물려받는다. 우리는 $v_1\otimes v_2\otimes\cdots\otimes v_k\in T^{k}(V)$의 equivalence class를 $v_1\wedge v_2\wedge\cdots\wedge v_k$으로 적을 것이며, 따라서 $\bigwedge(V)$에서의 곱셈 또한 마찬가지로 $\wedge$로 적는다. 

임의의 $x,y\in V$에 대하여,

$$0=(x+y)\wedge(x+y)=(x\wedge x)+(y\wedge x)+(x\wedge y)+(y\wedge y)=y\wedge x+x\wedge y$$

가 성립한다. 즉 $x\wedge y=-y\wedge x$이다. 더 일반적으로, 임의의 $u\in\bigwedge\nolimits^k(V)$, $v\in\bigwedge\nolimits^l(V)$에 대하여, $u=u_1\wedge\cdots\wedge u_k$, $v=v_1\wedge\cdots\wedge v_l$이라 하면

$$\begin{aligned}u\wedge v&=u_1\wedge\cdots\wedge u_k\wedge v_1\wedge\cdots\wedge v_l\\
&=(-1)^l u_1\wedge\cdots\wedge u_{k-1}\wedge v_1\cdots\wedge v_l\wedge u_k\\
&=(-1)^{kl}v_1\wedge\cdots\wedge v_l\wedge u_1\wedge\cdots\wedge u_k\\
&=(-1)^{kl}v\wedge u\end{aligned}$$

임을 확인할 수 있다. 특히 $k$가 $\dim V$보다 큰 경우, $v_1\wedge \cdots\wedge v_k$에서 $v_k$는 반드시 $v_1,\ldots, v_{k-1}$들의 일차결합으로 나타나야 하는데, 선형성을 이용하여 이를 쪼개준 후, 위의 식을 이용해서 $v_1\wedge v_1$, $v_2\wedge v_2$와 같은 식들을 만들어주어 $v_1\wedge\cdots\wedge v_k=0$임을 보일 수 있다. 즉, 

$$\bigwedge(V)=\bigoplus_{k\geq 0}\bigwedge\nolimits^k(V)$$

은 무한히 많은 $\bigwedge\nolimits^k(V)$들의 direct sum처럼 보이지만, 사실 이는 유한하다.

뿐만 아니라, 우리는 $\bigwedge(V)$의 차원과 basis를 명시적으로 계산할 수도 있다. $V$가 basis $e_1,\ldots, e_n$을 갖는다 하자. $\\{1,2,\ldots, n\\}$의 부분집합 $I$에 대하여, $I$의 원소들을 크기순으로 나열하여 

$$i_1 < i_2 < \cdots < i_k$$

라 하자. 이제 $\bigwedge\nolimits^k(V)$의 원소 $e\_I=e\_{i\_1}\wedge\cdots\wedge e\_{i\_k}$으로 정의하면, 이들 $e_I$들이 $\bigwedge(V)$의 basis가 되고, 또 $\lvert I\rvert=k$를 만족하는 $e_I$들은 $\bigwedge\nolimits^k(V)$의 basis가 된다는 것은 거의 자명하다. 

## 교대다중선형사상

다음 정의는 선형대수학에서부터 익숙한 것이다. 

<div class="definition" markdown="1">

<ins id="df2">**정의 2**</ins> $\mathbb{R}$-벡터공간 $V$에 대하여, multilinear map $V^r\rightarrow W$가 *alternating<sub>교대적</sub>*이라는 것은 임의의 $\sigma\in S_r$에 대하여 

$$h(v_{\sigma(1)},\ldots, v_{\sigma(r)})=\sgn(\sigma)h(v_1,\ldots, v_r)$$

이 성립하는 것이다. $V^r$에서 $\mathbb{R}$로의 모든 alternating multilinear map들의 모임을 $A^r(V)$로 적고, 편의상 $A^0(V)=\mathbb{R}$인 것으로 한다.

</div>

Exterior algebra $\bigwedge\nolimits^k(V)$는 다음의 universal property를 만족하는데, 이는 tensor product의 universal property로부터 쉽게 얻어진다.

<div class="proposition" markdown="1">

<ins id="pp3">**명제 3**</ins> 임의의 $\mathbb{R}$-벡터공간 $V$와 정수 $r$이 주어졌다 하자. 그럼 다음의 식

$$(v_1,\ldots, v_r)\mapsto v_1\wedge\cdots\wedge v_r$$

으로 정의된 함수 $V^r\rightarrow\bigwedge\nolimits^r(V)$는 alternating linear map이며, 이는 다음의 universal property를 만족한다.

> 임의의 $\mathbb{R}$-벡터공간 $W$와 alternating multilinear map $h:V^r\rightarrow W$에 대하여, 유일한 linear map $\tilde{h}:\bigwedge\nolimits^r(V)\rightarrow W$가 존재하여 $\tilde{h}\circ\varphi=h$가 성립한다.
> ![universal_property_of_ext_alg](/assets/images/Manifold/Exterior_algebra-1.png){:width="140px" class="invert" .align-center}

</div>

이를 조금 더 간결하게 적자면 $A^k(V)\cong\bigwedge\nolimits^k(V)^\ast$라 할 수 있다. 

특별히 $n$차원 $\mathbb{R}$-벡터공간 $\mathbb{R}^n$에 대하여, $\operatorname{det}:(\mathbb{R}^n)^n\rightarrow\mathbb{R}$ 또한 alternating multilinear map이었으며, 따라서 $\det$ 또한 $\bigwedge\nolimits^n(\mathbb{R}^n)$의 어떤 원소와 동일하게 취급할 수 있다. $\bigwedge\nolimits^n(\mathbb{R}^n)$는 1차원 $\mathbb{R}$-벡터공간인데, 이는 alternating multilinear map $(\mathbb{R}^n)^n\rightarrow\mathbb{R}$ 또한 상수배 차이를 제외하면 유일하게 결정된다는 사실에 해당한다.


## Duality

이 절에서는 다음의 세 isomorphism

$$T^{r,s}(V)^\ast\cong T^{r,s}(V^\ast),\quad \bigwedge\nolimits^k(V)^\ast\cong\bigwedge\nolimits^k(V^\ast),\quad \bigwedge(V)^\ast\cong\bigwedge(V^\ast)$$ 

을 증명한다. 이를 위해서 다음을 정의한다.

<div class="definition" markdown="1">

<ins id="df4">**정의 4**</ins> 두 $\mathbb{R}$-벡터공간 $V,W$에 대하여, 이들의 *pairing*은 bilinear map $(-,-):V\times W\rightarrow\mathbb{R}$을 의미한다. 이 때, 이 pairing이 *오른쪽에서 non-degenerate*라는 것은 linear map $(-,w):V\rightarrow \mathbb{R}$이 항상 0이 아닌 것이고, *왼쪽에서 non-degenerate*라는 것은 linear map $(v,-):W\rightarrow\mathbb{R}$이 항상 0이 아닌 것이다. Pairing $(-,-)$이 오른쪽과 왼쪽에서 모두 non-degenerate이라면 이를 간단히 non-degenerate이라 부른다.

</div>

두 유한차원 $\mathbb{R}$-벡터공간 $V,W$에 대하여, 이들 사이의 non-degenerate pairing $(-,-)$이 주어졌다 하자. 그럼 다음의 함수

$$v\mapsto (v,-)$$

가 $V$에서 $W^\ast$로의 linear map을 정의하며, $(-,-)$는 왼쪽에서 non-degenerate이므로 이는 injection이고 따라서 

$$\dim V\leq\dim W^\ast=\dim W$$

이 성립한다. 마찬가지로 $w\mapsto (-,w)$를 생각하면 $\dim V=\dim W$를 얻고, 따라서 $v\mapsto (v,-)$는 반드시 isomorphism이 되어야 한다.

이상에서 위에서 언급한 isomorphism을 만들기 위해서는 $T^{r,s}(V)\times T^{r,s}(V^\ast)\rightarrow\mathbb{R}$, $\bigwedge\nolimits^k(V)\times\bigwedge\nolimits^k(V^\ast)\rightarrow\mathbb{R}$과 같은 non-degenerate pairing을 만들면 충분하다는 것을 알 수 있다. 

<div class="example" markdown="1">

<ins id="ex5">**예시 5**</ins> 두 simple tensor 

$$\omega=\alpha^1\otimes\cdots\otimes \alpha^r\otimes u_{r+1}\otimes\cdots\otimes u_{r+s}\in T^{r,s}(V^\ast),\quad u=u_1\otimes\cdots\otimes u_r\otimes \alpha^{r+1}\otimes\cdots\otimes \alpha^{r+s}\in T^{r,s}(V)$$

에 대하여, 

$$(\omega,u)=\alpha^1(u_1)\alpha^2(u_2)\cdots \alpha^{r+s}(u_{r+s})$$

으로 정의하고, 이를 통해 pairing $(-,-)$을 정의하자. 그럼 $T^{r,s}(V^\ast)\cong T^{r,s}(V)^\ast$임을 확인할 수 있다. 한편, Tensor product의 universal property에 의하여, $T^{r,s}(V)^\ast$는 $V^r\times (V^\ast)^s$에서 $\mathbb{R}$로의 multilinear function들과의 isomorphism을 가지므로 $T^{r,s}(V^\ast), T^{r,s}(V)^\ast$, 그리고 $T^{r,s}(V)^\ast$는 $V^r\times (V^\ast)^s$에서 $\mathbb{R}$로의 multilinear function들 사이에 isomorphism이 존재함을 알 수 있다.

</div>

<div class="example" markdown="1">

<ins id="ex6">**예시 6**</ins> 마찬가지로 두 원소 

$$\omega=\alpha^1\wedge\cdots\wedge \alpha^k\in \bigwedge\nolimits^k(V^\ast),\quad u=u_1\wedge\cdots\wedge u_k\in\bigwedge\nolimits^k(V)$$

에 대하여 pairing을 정해주면 된다. 이는 다음의 식

$$(\omega, u)=\det\bigl(\alpha^i(u_j)\bigr)$$

으로 주어지며, 따라서 $\bigwedge\nolimits^k(V)^\ast\cong\bigwedge\nolimits^k(V^\ast)$가 성립한다. 뿐만 아니라, 앞서 $\bigwedge\nolimits^k(V)^\ast\cong A^k(V)$라는 것을 확인하였으므로

$$\bigwedge\nolimits^k(V^\ast)\cong\bigwedge\nolimits^k(V)^\ast\cong A^k(V)$$

를 얻는다.

</div>

한편, dual을 취하는 것은 유한한 direct sum과는 commute한다. 즉, index set이 유한하다면

$$\bigoplus_{i=1}^n V_i^\ast\cong \left(\bigoplus_{i=1}^n V_i\right)^\ast$$

이 성립한다. 이 isomorphism은 명시적으로는 $(\alpha^1,\ldots, \alpha^n)\in\bigoplus V_i^\ast$을 다음의 식

$$\alpha(v_1,\ldots, v_n)=\alpha^1(v_1)+\cdots+\alpha^n(v_n)$$

으로 정의된 $\alpha\in\left(\bigoplus V_i\right)^\ast$으로 보낸다. 

따라서, $\bigwedge(V)$는 오직 유한히 많은 $\bigwedge\nolimits^k(V)$들의 direct sum이므로

$$\bigwedge(V^\ast)=\bigoplus_{k\geq 0}\bigwedge\nolimits^k(V^\ast)=\bigoplus_{k\geq 0}\bigwedge\nolimits^k(V)^\ast\cong\bigwedge(V)^\ast$$

가 성립한다. 

위에서 정의한 identification은 다음과 같은 의미에서 자연스럽다. 

두 $\mathbb{R}$-벡터공간 $V,W$와 linear map $L:V\rightarrow W$, 그리고 그 dual map $L^\ast:W^\ast\rightarrow V^\ast$가 주어졌다 하자. 우선

$$L^\sim(v_1\wedge\cdots\wedge v_k)=L(v_1)\wedge\cdots\wedge L(v_k)$$

을 통해 $\bigwedge(V)$에서 $\bigwedge(W)$로의 $\mathbb{R}$-algebra homomorphism $L^\sim$을 정의할 수 있고, 이와 유사하게 다음의 식

$$L^{\ast\sim}(\alpha^1\wedge\cdots\wedge\alpha^k)=L^\ast(\alpha^1)\wedge\cdots\wedge L^\ast(\alpha^k)$$

을 통해 $\bigwedge(W^\ast)$에서 $\bigwedge(V^\ast)$로의 $\mathbb{R}$-algebra homomorphism $L^{\ast\sim}$을 정의할 수 있다. 

한편, 우리는 $L^\sim$의 dual map $L^{\sim\ast}:\bigwedge(W)^\ast\rightarrow\bigwedge(V)^\ast$ 또한 생각할 수 있다. 그럼 다음의 diagram이 commute한다.

![naturality](/assets/images/Manifold/Exterior_algebra-2.png){:width="180px" class="invert" .align-center}

(여기서 $\varphi$들은 pairing $(-,-):\bigwedge\nolimits^k(X^\ast)\times\bigwedge\nolimits^k(X)\rightarrow\mathbb{R}$에 의해 결정되는 isomorphism $\alpha\mapsto (\alpha, -)$를 뜻한다.)

이는 임의의 두 원소 

$$\alpha^1\wedge\cdots\wedge\alpha^k\in\bigwedge(W^\ast),\quad v_1\wedge\cdots\wedge v_k\in\bigwedge(V)$$

에 대하여, 

$$\begin{aligned}\bigl((\varphi_V\circ L^{\ast\sim})(\alpha^1\wedge\cdots\wedge\alpha^k)\bigr)(v_1\wedge\cdots\wedge v_k)&=\bigl(\varphi_V(L^\ast(\alpha^1)\wedge\cdots\wedge L^\ast(\alpha^k))\bigr)(v_1\wedge\cdots\wedge v_k)\\
&=\bigl(L^\ast(\alpha^1)\wedge\cdots\wedge L^\ast(\alpha^k), v_1\wedge\cdots\wedge v_k\bigr)\\
&=\det\bigl(\alpha^i(L(v_j))\bigr)\end{aligned}$$

이고

$$\bigl((L^{\sim\ast}\circ\varphi_W)(\alpha^1\wedge\cdots\wedge\alpha^k)\bigr)=\bigl(L^{\sim\ast}\circ (\alpha^1\wedge\cdots\wedge\alpha^k, -)\bigr)=\bigl(\alpha^1\wedge\cdots\wedge\alpha^k, L^\sim(-)\bigr)$$

이므로

$$\bigl((L^{\sim\ast}\circ\varphi_W)(\alpha^1\wedge\cdots\wedge\alpha^k)\bigr)(v_1\wedge\cdots\wedge v_k)=\bigl(\alpha^1\wedge\cdots\wedge\alpha^k, L(v_1)\wedge \cdots\wedge L(v_k)\bigr)=\det\bigl(\alpha^i(L(v_j))\bigr)$$

이 되기 때문이다.


## Interior multiplication

임의의 $u\in\bigwedge(V)$에 대하여, 다음의 식

$$v\mapsto u\wedge v$$

를 통해 *left multiplication*을 정의할 수 있다. 어렵지 않게 이 대응이 $\bigwedge(V)$에서 $\bigwedge(V)$로의 linear map임을 확인할 수 있다. 이제 이 linear map의 dual map $\bigwedge (V)^\ast\rightarrow\bigwedge(V)^\ast$를 생각하자.

![interior_multiplication](/assets/images/Manifold/Exterior_algebra-3.png){:width="160px" class="invert" .align-center}

즉 임의의 $\omega\in \bigwedge(V)^\ast$에 대하여, $\omega$를 이 dual map을 통해 보내면 새로운 $\bigwedge(V)^\ast$의 원소를 얻게 된다. 우리는 이를 $u\mathbin{\lrcorner}\omega$로 적는다. 그럼 정의에 의하여

$$(u\mathbin{\lrcorner}\omega, v)=(\omega, u\wedge v)$$

이다.

위에서 정의한 isomorphism을 통해 적당한 $k$에 대하여 $\omega\in\bigwedge\nolimits^k(V^\ast)$이고, $u\in \bigwedge\nolimits^l(V)$라 하자. 즉 $\omega$는 $\bigwedge\nolimits^k(V)$의 성분에만 영향을 받는 linear map $\bigwedge(V)\rightarrow\mathbb{R}$이며 $u$는 $\bigwedge\nolimits^l(V)$의 원소이다. 그럼 이제 $u\mathbin{\lrcorner}\omega$는 오직 $\bigwedge\nolimits^{k-l}(V)$의 성분에만 영향을 받게 되므로, $u\mathbin{\lrcorner}-$는 $\bigwedge\nolimits^k(V)$에서 $\bigwedge\nolimits^{k-l}(V)$로의 linear map을 정의한다 할 수 있다. 표기상 $u\mathbin{\lrcorner}-$를 계속 사용하는 것은 어색하므로, 이 linear map을 간단히 $i_u$로 적기도 한다.

다음을 정의하자.

<div class="definition" markdown="1">

<ins id="df7">**정의 7**</ins> $\bigwedge(V)$의 endomorphism $L$이 주어졌다 하자.

1. 만일 $L(u\wedge v)=L(u)\wedge v+u\wedge L(v)$가 성립한다면, $L$을 *derivation*이라 부른다.
2. 만일 $L(u\wedge v)=L(u)\wedge v+(-1)^p u\wedge L(v)$라면 $L$을 *anti-derivation*이라 부른다. 이 때 $u\in\bigwedge\nolimits^p(V)$이다.
3, 만일 $L$이 모든 $j$에 대하여 $\bigwedge\nolimits^j(V)$에서 $\bigwedge\nolimits^{j+k}(V)$로의 linear map이라면, $L$이 *degree $k$*의 linear map이라 한다.

</div>

<div class="proposition" markdown="1">

<ins id="pp8">**명제 8**</ins> 임의의 $u\in V=\bigwedge\nolimits^1(V)$에 대하여, $i_u$는 degree $-1$의 antiderivation이다.

</div>
<details class="proof" markdown="1">
<summary>증명</summary>



</details>

---

**참고문헌**

**[War]** Frank W. Warner. *Foundations of Differentiable Manifolds and Lie Groups*, Graduate texts in mathematics, Springer, 2013  
**[Lee]** John M. Lee. *Introduction to Smooth Manifolds*, Graduate texts in mathematics, Springer, 2012  

---