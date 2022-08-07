---

title: "쌍대공간"
excerpt: ""

categories: [Math / Linear Algebra]
permalink: /ko/math/linear_algebra/space_of_linear_maps
sidebar: 
    nav: "linear_algebra-ko"

header:
    overlay_image: /assets/images/Linear_algebra/Linear_map.png
    overlay_filter: 0.5

date: 2022-08-05
last_modified_at: 2022-08-05

weight: 10

---

$V$와 $V^\ast$가 isomorphic하다는 것을 보이기 위해서는 반드시 특정한 basis를 택해야 했으나, $V$와 $V^{\ast\ast}$ 사이의 isomorphism은 basis의 의존하지 않도록 정의할 수 있다.[^1]

<div class="definition" markdown="1">

<ins id="df3">**정의 3**</ins> 세 $F$-벡터공간 $U,V,W$에 대하여, 함수 $f:U\times V\rightarrow W$이 *bilinear*라는 것은 임의의 $u,u_1,u_2\in U$, $v,v_1,v_2\in V$, 그리고 스칼라 $\alpha$에 대하여

$$f(u_1+u_2,v)=f(u_1,v)+f(u_2,v),\qquad f(u,v_1+v_2)=f(u,v_1)+f(u,v_2),\qquad f(\alpha u,v)=\alpha f(u,v)=f(u,\alpha v)$$

가 성립하는 것이다.

</div>

바꾸어 말하자면 이는 임의의 $u\in U$에 대하여 함수 $f(u,-):V\rightarrow W$가 linear이고, 또 임의의 $v\in V$에 대하여 $f(-,v):U\rightarrow W$ 또한 linear라는 뜻이다. 

<div class="definition" markdown="1">

<ins id="df4">**정의 4**</ins> 두 $F$-벡터공간 $V,W$에 대하여, $V$와 $W$의 *pairing*은 bilinear map $\langle -,-\rangle:V\times W\rightarrow F$를 의미한다. 만일 영벡터가 아닌 임의의 $v\in V$에 대하여 다음의 linear map

$$\langle v,-\rangle: W\rightarrow F$$

가 항상 영함수가 아니라면 이 pairing이 *왼쪽에서 non-degenerate*이라 하고, 비슷하게 영벡터가 아닌 임의의 $w\in W$에 대하여

$$\langle -,w\rangle:U\rightarrow F$$

가 항상 영함수가 아니라면 이 pairing이 *오른쪽에서 non-degenerate*라 한다. 왼쪽과 오른쪽 모두에서 non-degenerate인 pairing을 간단히 *non-degenerate pairing*이라 부른다.

</div>

예를 들어 $V=W=\mathbb{R}^n$ 위에서 정의된 벡터의 내적 $\langle -,-\rangle:\mathbb{R}^n\times\mathbb{R}^n\rightarrow\mathbb{R}$은 non-degenerate pairing이다. 우선 다음의 식

$$\langle v,w_1+w_2\rangle=\langle v,w_1\rangle+\langle v,w_2\rangle,\qquad \langle v_1+v_2,w\rangle=\langle v_1,w\rangle+\langle v_2,w\rangle,\qquad \langle\alpha v,w\rangle=\alpha\langle v,w\rangle=\langle v,\alpha w\rangle$$

이 성립하는 것은 자명하다. 따라서 벡터의 내적은 pairing이다. 한편 영벡터가 아닌 임의의 벡터 $v$에 대하여 $\langle v,v\rangle=\lVert v\rVert^2\neq 0$이므로 non-degenerate 조건 또한 만족된다. 

이 글에서 주로 사용하게 될 예시는 다음의 예시이다.

<div class="example" markdown="1">

<ins id="ex5">**예시 5**</ins> 임의의 $F$-벡터공간 $V$와, $V$의 dual space $V^\ast$에 대하여 $\langle-,-\rangle:V\times V^\ast\rightarrow F$를 다음의 식

$$\langle v,f\rangle=f(v)$$

으로 주면 $\langle-,-\rangle$은 non-degenerate pairing이다. 우선 고정된 $v\in V$와 임의의 $f,g\in V^\ast$에 대하여

$$\langle v,f+g\rangle=(f+g)(v)=f(v)+g(v)=\langle v,f\rangle+\langle v,g\rangle$$

이고, 또 고정된 $f\in V^\ast$와 임의의 $v_1,v_2\in V$에 대하여

$$\langle v_1+v_2,f\rangle=f(v_1+v_2)=f(v_1)+f(v_2)=\langle v_1,f\rangle+\langle v_2,f\rangle$$

이 성립한다. 비슷하게 임의의 스칼라 $\alpha$에 대하여

$$\langle \alpha v,f\rangle=f(\alpha v)=\alpha f(v)=(\alpha f)(v)=\langle v,\alpha f\rangle$$

이 성립하므로 $\langle -, -\rangle$은 pairing이다. 

뿐만 아니라 $\langle -,-\rangle$은 non-degenerate이다. 우선 임의의 $f\in V^\ast$가 0이 아니라면 $f(v)\neq 0$이도록 하는 $v$가 존재하므로 $\langle -,-\rangle$이 오른쪽에서 non-degenerate임은 자명하다. 또, 영벡터가 아닌 임의의 벡터 $v$에 대하여, $v$를 포함하는 basis $\mathcal{B}$를 찾은 후, 위와 같이 $\varphi_v$를 만들면 $\langle v,\varphi_v\rangle=1$이므로 $\langle-,-\rangle$은 왼쪽에서 non-degenerate이기도 하다. 

이로부터 $\langle-,-\rangle$이 non-degenerate pairing임을 안다. 이를 *canonical pairing*이라 부른다.

</div>

다시 일반적인 경우를 살펴보자. Non-degenerate pairing $\langle-,-\rangle:V\times W\rightarrow F$가 주어진 두 $F$-벡터공간 $V,W$에 대하여, $V$에서 $W^\ast$로의 linear map $v\mapsto \langle v,-\rangle$이 잘 정의된다. 또, $v$가 영벡터가 아닌 이상 $\langle v,-\rangle$은 영함수가 아니므로 이 linear map은 단사다. 

특별히 $V$가 유한차원 $F$-벡터공간이고, 위와 같이 $V$의 canonical pairing이 주어진 경우를 생각하자. 그럼 앞선 문단의 linear map은 $V$에서 $V^{\ast\ast}$로의 단사함수이며, 벡터공간의 차원을 고려하면 이 함수는 $V$에서 $V^{\ast\ast}$로의 isomorphism을 정의한다. 이 isomorphism도 마찬가지로 *canonical isomorphism*이라 부른다.

## Dual map

마지막으로 두 $F$-벡터공간 $V,W$와 linear map $L:V\rightarrow W$가 주어졌다 하자. 

[^1]: 다만, 이렇게 정의한 $V\rightarrow V^{\ast\ast}$가 isomorphism이라는 것을 증명하기 위해서는 여전히 $\dim V=\dim V^\ast$임을 이용해야 한다. 그럼에도 불구하고 이 함수 자체는 basis의 선택에 의존하지 않고 만들 수 있다.