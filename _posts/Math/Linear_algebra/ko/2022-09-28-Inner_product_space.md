---

title: "쌍선형형식"
excerpt: ""

categories: [Math / Linear Algebra]
permalink: /ko/math/linear_algebra/bilinear_form
sidebar: 
    nav: "linear_algebra-ko"

header:
    overlay_image: /assets/images/Linear_algebra/Bilinear_form.png
    overlay_filter: 0.5

date: 2022-09-28
last_modified_at: 2022-09-28

weight: 16

---

앞선 글에서 우리는 벡터공간 $V$의 쌍대공간 $V^\ast$를 정의하고, 만일 $V$가 유한차원이라면 $V^\ast$의 쌍대공간인 $V^{\ast\ast}$와 $V$가 isomorphic하다는 것을 살펴봤다. 이 과정에서 핵심적으로 쓰인 사실은 non-degenerate pairing $\langle -,-\rangle:V\times W \rightarrow F$가 $V$에서 $W^\ast$, 그리고 $W$에서 $V^\ast$로의 단사인 linear map을 정의한다는 것이었다. 우리는 이 사실을 canonical pairing

$$\langle -,-\rangle:V\times V^\ast\rightarrow F;\quad (v,f)\mapsto f(v)$$

에 적용하고, 차원을 고려하여 $V$와 $V^{\ast\ast}$가 isomorphic하다는 것을 살펴보았다. 이렇게 유도되는 $V\rightarrow V^{\ast\ast}$를 기술하기 위해서는 $V$에서 basis를 선택할 필요가 없었다.

한편, 우리는 이전 글의 서두에서 $V$와 $V^\ast$ 또한 같은 차원을 갖는다는 것을 언급하였는데, 이는 위의 자연스러운 isomorphism $V\rightarrow V^{\ast\ast}$와는 다르게 특정한 basis $\\{x_1,\ldots, x_n\\}$을 택한 후, 이들의 dual basis $\\{\xi^1,\ldots, \xi^n\\}$을 택하여 $x_i\mapsto \xi^i$를 통해 정의해야 한다는 차이가 있었다. 

## 쌍선형형식

이제 우리는 $V=W$인 경우에 집중한다.

<div class="definition" markdown="1">

<ins id="df1">**정의 1**</ins> 임의의 pairing $\langle -,-\rangle:V\times W\rightarrow F$에 대하여, 만일 $W=V$라면 이 pairing을 $V$ 위에서 정의된 *bilinear form<sub>쌍선형형식</sub>*이라 부른다. $\langle -,-\rangle$이 *non-degenerate bilinear form<sub>비퇴화 쌍선형형식</sub>*이라는 것은 $\langle-,-\rangle$이 pairing으로서 non-degenerate인 것이다.

</div>

$V$ 위에 bilinear form이 주어졌다 하자. 그럼 위와 같은 논증을 통해, 우리는 $V$에서 $V^\ast$로의 linear map들

$$v\mapsto \langle v,-\rangle,\qquad v\mapsto \langle -,v\rangle$$

을 얻는다. 일반적으로 이 둘은 같을 필요가 없지만, 다음을 정의할 수 있다.

<div class="definition" markdown="1">

<ins id="df2">**정의 2**</ins> 임의의 bilinear form $\langle-,-\rangle:V\times V\rightarrow F$에 대하여, 다음의 식

$$\langle v,w\rangle=\langle w,v\rangle$$

이 모든 $v,w\in V$에 대해 성립하면 이 form이 *symmetric<sub>대칭적</sub>*이라 말한다. 만일 모든 $v,w\in V$에 대해 다음의 식

$$\langle v,w\rangle=-\langle w,v\rangle$$

이 성립하면 이 form이 *alternating<sub>교대적</sub>*이라 말한다.

</div>

임의의 bilinear form $\langle-,-\rangle:V\times V\rightarrow F$가 주어졌다 하자. 만일 $V$의 basis $\\{x_1,\ldots, x_n\\}$가 고정되었다고 하면, 임의의 $v=\sum v_ix_i, w=\sum w_jx_j$에 대하여 다음의 식

$$\langle v,w\rangle=\left\langle\sum_{i=1}^nv_ix_i,\sum_{j=1}^n w_jx_j\right\rangle=\sum_{i,j=1}^n v_iw_j\langle x_i,x_j\rangle$$

이 성립한다. 잠시 $(i,j)$ 성분이 $\langle x_i,x_j\rangle$인 $n\times n$ 행렬을 $G$라 표기하면, 위 식은

$$\langle v,w\rangle=v^T Gw$$

으로 간단하게 쓸 수 있다. 이 때 $G$를 원래의 bilinear form의 basis $\\{x_1,\ldots, x_n\\}$에 대한 행렬표현이라 부른다. 어렵지 않게 bilinear form이 symmetric인 것은 그 행렬표현이 symmetric matrix인 것과 동치이고, alternating인 것은 그 행렬표현이 skew-symmetric matrix인 것과 동치라는 것을 알 수 있다.

## 비퇴화 쌍선형형식

유한차원 $F$-벡터공간 $V$가 주어졌다 하고, 앞서 언급한 canonical pairing $\langle-,-\rangle:V\times V^\ast\rightarrow F$을 생각하자. 만일 $V$ 위에 non-degenerate pairing $(-,-):V\times V\rightarrow F$가 주어졌다면, 우리는 앞선 글의 [따름정리 5](/ko/math/linear_algebra/dual_space#crl5)로부터 $(-,-)$이 isomorphism 

$$V\rightarrow V^\ast;\qquad v\mapsto (-,v)\tag{1}$$

을 정의한다는 것을 안다. 물론 이 isomorphism 대신 $v\mapsto (v,-)$를 사용할 수도 있고, 필요하다면 다음의 식

$$V\rightarrow V^\ast;\qquad v\mapsto\frac{1}{2}((-,v)+(v,-))$$

을 통해 대칭성을 보장받을 수도 있다. 편의를 위해 앞으로는 $(-,-)$이 처음부터 symmetric non-degenerate bilinear form이었던 것으로 가정하자. 그럼 $(-,-)$는 식 (1)에 의해 정의된 isomorphism을 가지며, 이는 다음과 같이 쓸 수 있다.

<div class="proposition" markdown="1">

<ins id="crl3">**따름정리 3**</ins> Non-degenerate bilinear form $(-,-)$이 주어진 유한차원 $F$-벡터공간 $V$를 생각하자. 임의의 $f\in V^\ast$가 주어질 때마다, 적당한 $v\in V$가 유일하게 존재하여 

$$f(w)=(w,v)\qquad\text{for all $w\in V$}$$

이 성립한다.

</div>

