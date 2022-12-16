---

title: "여접공간"
excerpt: "접벡터와 접공간"

categories: [Math / Manifold]
permalink: /ko/math/manifold/cotangent_space
header:
    overlay_image: /assets/images/Manifold/Cotangent_space.png
    overlay_filter: 0.5
sidebar: 
    nav: "manifold-ko"

date: 2022-12-09
last_modified_at: 2022-12-09
weight: 4

---

## 여접공간과 차원

앞선 글에서 $T_pM$은 $\mathbb{R}$-벡터공간이 된다는 것을 살펴보았다. 이제 우리는 $T_pM$이 실은 유한차원이라는 것을 보일 것인데, 이를 직접 보이는 대신 $T_pM$의 dual space가 유한차원임을 보인다.

[§접공간, 명제 2](/ko/math/manifold/tangent_space#pp2)에 의하여, $\mathcal{C}^\infty_p$의 ideal들의 descending chain

$$\mathcal{C}^\infty_p\supset\mathfrak{m}_p\supset\mathfrak{m}_p^2\supset\cdots$$

이 잘 정의된다. 그럼 특히 $\mathfrak{m}_p/\mathfrak{m}_p^2$를 $\mathcal{C}^\infty_p/\mathfrak{m}_p\cong\mathbb{R}$ 위의 벡터공간으로 볼 수 있다. 

<div class="proposition" markdown="1">

<ins id="lem1">**보조정리 1**</ins> Manifold $M$과 임의의 한 점 $p\in M$에 대하여, $T_pM\cong(\mathfrak{m}_p/\mathfrak{m}_p^2)^\ast$가 성립한다. 

</div>
<details class="proof" markdown="1">
<summary>증명</summary>

우선 임의의 $v\in T\_pM$가 주어졌다 하자. 이를 부분집합 $\mathfrak{m}\_p$으로 restrict하면 $v\|\_{\mathfrak{m}\_p}\in\operatorname{Hom}_\mathbb{R}(\mathfrak{m}_p,\mathbb{R})$이 성립한다. 이제 $v\|\_{\mathfrak{m}_p}$이 linear map $\mathfrak{m}_p/\mathfrak{m}_p^2\rightarrow\mathbb{R}$을 잘 정의한다는 것을 보이려면 $\mathfrak{m}_p^2\subset\ker (v\|\_{\mathfrak{m}_p})$임을 보여야 한다. 적당한 index set $I$에 대하여, $\mathfrak{m}_p$가 $\mathbf{f}_i$들에 의해 생성되는 ideal이라 하자. 그럼 $\mathfrak{m}_p^2$은 $\mathbf{f}_i\mathbf{f}_j$들에 의하여 생성되는 ideal이다. 그런데

$$v(\mathbf{f}_i\mathbf{f}_j)=\mathbf{f}_i(p)v(\mathbf{f}_j)+\mathbf{f}_j(p)v(\mathbf{f}_i)=0$$

이므로, $v$는 $\mathfrak{m}_p^2$의 임의의 generator를 항상 0으로 보내고, $\mathfrak{m}_p^2\subset\ker(v\|\_{\mathfrak{m}_p})$이며, 따라서 임의의 $v\in T_pM$마다 적당한 $\mathfrak{m}_p/\mathfrak{m}_p^2$의 원소를 대응시킬 수 있다. 이 대응이 $\mathbb{R}$-linear map이라는 것은 자명하다.

반대로 임의의 $L\in(\mathfrak{m}_p/\mathfrak{m}_p^2)^\ast$이 주어졌다 하고, 이를 이용해 tangent vector $v_L$을 하나 만들자. Tangent vector는 $C_p^\infty$에서 $\mathbb{R}$로의 linear map으로서, $v_L$을 만든다는 것은 임의의 $\mathbf{f}\in \mathcal{C}^\infty_p$에 대하여 $v_L(\mathbf{f})$의 값을 정해주는 것과 같다. $\mathbf{f(p)}$를 함숫값 $f(p)$를 갖는 상수함수라 하면, $\mathbf{f}-\mathbf{f(p)}$는 $\mathfrak{m}_p$의 원소이고, 따라서 

$$v_L(\mathbf{f})=L((\mathbf{f}-\mathbf{f(p)})+\mathfrak{m}_p^2)$$

으로 정의하는 것이 잘 정의된다. 이렇게 정의된 $v_L$이 linear map일 뿐만 아니라 [§접공간, 정의 3](/ko/math/manifold/tangent_space#df3)도 만족한다는 것을 보여야 하므로, 

$$\begin{aligned}
            v_L(\mathbf{f}\cdot\mathbf{g})&=L((\mathbf{fg}-\mathbf{f(p)g(p)})+\mathfrak{m}_p^2)\\
            &=L(((\mathbf{f}-\mathbf{f(p)})(\mathbf{g}-\mathbf{g(p)})+\mathbf{f(p)}(\mathbf{g}-\mathbf{g(p)})+(\mathbf{f}-\mathbf{f(p)})\mathbf{g(p)})+\mathfrak{m}_p^2)\\
            &=\mathbf{f}(p)L((\mathbf{g}-\mathbf{g(p)})+\mathfrak{m}_p^2)+\mathbf{g}(p)L((\mathbf{f}-\mathbf{f(p)})+\mathfrak{m}_p^2)\\
            &=\mathbf{f}(p)+v_L(\mathbf{g})+\mathbf{g}(p)v_L(\mathbf{f}).
        \end{aligned}
$$

을 계산할 수 있다. $L\mapsto v_L$ 또한 linear map이 된다는 것을 쉽게 보일 수 있으며, 뿐만 아니라 이 대응이 앞서 정의한 $T_pM$에서 $(\mathfrak{m}_p/\mathfrak{m}_p^2)^\ast$로의 linear map의 역함수가 된다는 것을 확인할 수 있다.

</details>

따라서 $\mathfrak{m}_p/\mathfrak{m}_p^2$이 유한차원이라면 $T_pM$도 유한차원이며, 이 때

$$(T_pM)^\ast\cong(\mathfrak{m}_p/\mathfrak{m}_p^2)^{\ast\ast}\cong\mathfrak{m}_p/\mathfrak{m}_p^2$$

이므로 $\mathfrak{m}_p/\mathfrak{m}_p^2$을 *cotangent space<sub>여접공간</sub>*이라 부른다. 

<div class="proposition" markdown="1">

<ins id="thm2">**정리 2**</ins> $\mathbb{R}$-벡터공간 $\mathfrak{m}_p/\mathfrak{m}_p^2$의 차원은 유한하며, 그 값은 manifold $M$의 차원과 같다.

</div>
<details class="proof" markdown="1">
<summary>증명</summary>

이를 보이기 위해, 다음의 다변수 테일러 근사

$$\begin{aligned}g(x)&=g(x_0)+\sum_{i=1}^m\frac{\partial g}{\partial r^i}\bigg|_{x_0}(r^i(x)-r^i(x_0))\\
&\phantom{phantom}+\sum_{i,j}(r^i(x)-r^i(x_0))(r^j(x)-r^j(x_0))\int_0^1(1-t)\frac{\partial^2g}{\partial r^i\partial r^j}\bigg|_{(x_0+t(x-x_0))}\mathop{dt}\end{aligned}$$

을 사용한다. 

$(U,\varphi)$가 $p$을 중심으로 하는 coordinate system이고, $\varphi=(x^i)\_{i=1}^m$라 하자. 또, $\mathbf{f}\in\mathfrak{m}_p$가 임의로 주어졌다 하자. 

위의 식은 유클리드 공간에서 성립하는 식이므로, $g=f\circ\varphi^{-1}$로 두고, $g$의 정의역이 $\varphi(U)$인 것으로 생각하자. 원점을 중심으로 한 테일러 근사로부터, 임의의 $x\in\varphi(U)$에 대하여 다음의 식

$$g(x)=g(0)+\sum_{i=1}^m\frac{\partial g}{\partial r^i}\bigg|_0r^i(x)+\sum_{i,j}r^i(x)r^j(x)\int_0^1(1-t)\frac{\partial^2g}{\partial r^i\partial r^j}\bigg|_{tx}\mathop{dt}$$

을 얻는다. 이제 $x=\varphi(q)$라 하면

$$\begin{aligned}f(q)&=f(p)+\sum_{i=1}^m\frac{\partial (f\circ\varphi^{-1})}{\partial r^i}\bigg|_0r^i(\varphi(q))+\sum_{i,j}r^i(\varphi(q))r^j(\varphi(q))\int_0^1(1-t)\frac{\partial^2g}{\partial r^i\partial r^j}\bigg|_{t\varphi(q)}\mathop{dt}\\ &=f(p)+\sum_{i=1}^m\frac{\partial(f\circ\varphi^{-1})}{\partial r^i}\bigg|_0 x^i(q)+\sum_{i,j} x^i(q)x^j(q)\int_0^1(1-t)\frac{\partial^2 g}{\partial r^i\partial r^j}\bigg|_{t\varphi(q)}dt\end{aligned}$$

이다. 우변을 살펴보면, $\mathbf{f}\in\mathfrak{m}_p$으로부터 $f(p)=0$이고, 또 우변의 적분은 $q$에 대한 $C^\infty$ 함수이다. 이제 $x^i$들은 모두 $x^i(p)=0$을 만족하는 함수이므로, 위 식을 germ으로 바꾸면 우변의 이중합은 $\mathfrak{m}_p^2$의 원소가 된다. 이를 모두 정리하면

$$\mathbf{f}=\sum_{i=1}^m\frac{\partial(f\circ\varphi^{-1})}{\partial r^i}\bigg|_0\mathbf{x}^i\mod \mathfrak{m}_p^2$$

이 성립한다. $\mathbf{f}$는 임의의 원소이므로, $\mathfrak{m}_p/\mathfrak{m}_p^2$이 $\mathbf{x}^i+\mathfrak{m}_p^2$들로 생성됨을 알 수 있다.

증명을 마무리하기 위해서는 이들 $n$개의 원소들 $\mathbf{x}^i+\mathfrak{m}_p^2$들이 일차독립임을 보여야 한다. 

$$\sum_{i=1}^m a_i\mathbf{x}^i=0\mod \mathfrak{m}_p^2$$

이라 하자. 그럼 $U$ 위에서 위 식은

$$\sum_{i=1}^m a_i (x^i\circ\varphi^{-1})=0\mod \mathfrak{m}_0^2$$

이 되고 (단, $\mathfrak{m}_0$은 점 $0\in\varphi(U)$에 대응되는 maximal ideal이다), $x^i\circ\varphi^{-1}=r^i$이므로 

$$\sum_{i=1}^m a_i\mathbf{r}^i=0\mod \mathfrak{m}^2_0$$

가 된다. 

우리는 아직 $\partial/\partial x^i$를 정의하진 않았지만, 유클리드 공간에서의 방향미분은 잘 알고 있다. 이를 이용해서 위 식의 양변에 $\partial/\partial r^j$를 취하면, 우변의 $0$ (즉 $\mathfrak{n}^2$의 어떤 원소)는 라이프니츠 법칙에 의해 $0$이 될 것이고, 따라서 이 식은

$$a_j=\frac{\partial}{\partial r^j}\bigg|_0\sum a_i r^i=0$$

이 된다. 따라서 $a_j=0$이 모든 $j$에 대해 성립하고 $\mathbf{x}^i+\mathfrak{m}_p^2$들은 일차독립이다.

</details>

이 정리의 증명을 잘 살펴보면, 단순히 차원에 대한 정보 뿐만 아니라 $T_pM$의 basis 또한 얻을 수 있다. 우리는 $\mathbf{x}^i+\mathfrak{m}_p^2$들이 $\mathfrak{m}_p/\mathfrak{m}_p^2$의 basis가 된다는 것을 보였는데, tangent space $T_pM$은 $(\mathfrak{m}_p/\mathfrak{m}_p^2)^\ast$와 isomorphic하다는 사실을 잘 알고 있으므로 $T_pM$의 basis를 이들의 dual basis로 잡는 것이 자연스러워 보인다. 즉,

<div class="definition" markdown="1">

<ins id="df3">**정의 3**</ins> Manifold $M$과 $p\in M$이 주어졌다 하자. $p$을 포함하는 coordinate system $(U,\varphi)$, 그리고 $\varphi$의 component function들 $x^i$에 대하여, $x^i$ 방향의 *directional derivative*는 다음의 식

$$\left(\frac{\partial}{\partial x^i}\bigg|_p\right)f=\frac{\partial(f\circ \varphi^{-1})}{\partial r^i}\bigg|_{\varphi(p)}$$

으로 정의되는 tangent vector이다.

</div>

물론 모든 tangent vector들은 방향미분들로 생각할 수 있지만, 이들 벡터들 $\partial/\partial x^i$들의 특별한 점은 이들이 <em_ko>정확히</em_ko> coordinate system이 정의해주는 좌표축과 평행한 방향의 미분들이라는 것이다. 

이 $m$개의 tangent vector들은 앞서 말했듯 $\mathfrak{m}_p/\mathfrak{m}_p^2$의 basis의 dual이므로, 이들이 basis를 이루는 것은 자명하다. 그러면, 임의의 $v\in T_pM$에 대해, $v$를 $\partial/\partial x^i$들의 linear combination으로 나타내는 방법 또한 유일하게 존재해야 할 것이다. 이는 다음의 식

$$v=\sum_{i=1}^m v(x^i)\frac{\partial}{\partial x^i}\bigg|_p$$

으로 주어진다. 이 식이 맞는지를 체크해 보기 위해서는 임의의 $\mathbf{f}$에다 위 식의 양 변에 있는 tangent vector들을 각각 적용해본 후 그 결과를 비교하면 된다. 혹은 더 간단하게, $\mathbf{f}$는 $\mathbf{x}^i+\mathfrak{m}_p^2$들의 linear combination으로 나타나니, $\mathbf{x}^j$에 대해서만 적용해 봐도 충분할 것이다. 우변을 $\mathbf{x}^j$에 적용해보면,

$$\sum_{i=1}^m v(x^i)\frac{\partial}{\partial x^i}\bigg|_p x^j=\sum_{i=1}^m v(x^i)\delta_{ij}=v(x^j)$$

이 되므로 앞선 식이 성립한다. 

이제 우리는 tangent vector를 엄밀한 언어로 정의하였으므로, 다음 글부터는 $\mathcal{C}^\infty_p$의 원소들을 germ $\mathbf{f}$로 쓰지 않고, 간단히 $f$로만 적기로 한다. 이 때 $f\in \mathcal{C}^\infty_p$이라는 것은 $f$가 $p\in M$의 적당한 열린근방에서 정의된 $C^\infty$ 함수라는 뜻이다.