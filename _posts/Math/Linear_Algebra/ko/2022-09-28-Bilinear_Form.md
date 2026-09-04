---
title: "쌍선형형식"
description: "유한차원 벡터공간의 쌍대공간과 자연스러운 동형사상을 복습하고, 쌍선형형식의 정의·대칭성·교대성·비퇴화 조건을 정리한다."
excerpt: "쌍선형형식과 쌍대공간"

categories: [Math / Linear Algebra]
permalink: /ko/math/linear_algebra/bilinear_form
sidebar: 
    nav: "linear_algebra-ko"


date: 2022-09-28

weight: 20


---

앞선 글에서 우리는 벡터공간 $V$의 dual space $V^\ast$를 정의하고, 만일 $V$가 유한차원이라면 $V^\ast$의 dual space인 $V^{\ast\ast}$와 $V$가 isomorphic하다는 것을 살펴봤다. 이 과정에서 핵심적으로 쓰인 사실은 non-degenerate pairing $\langle -,-\rangle:V\times W \rightarrow \mathbb{K}$가 $V$에서 $W^\ast$, 그리고 $W$에서 $V^\ast$로의 단사인 linear map을 정의한다는 것이었다. 우리는 이 사실을 canonical pairing

$$\langle -,-\rangle:V\times V^\ast\rightarrow \mathbb{K};\quad (v,f)\mapsto f(v)$$

에 적용하고, 차원을 고려하여 $V$와 $V^{\ast\ast}$가 isomorphic하다는 것을 살펴보았다. 이렇게 유도되는 $V\rightarrow V^{\ast\ast}$를 기술하기 위해서는 $V$에서 basis를 선택할 필요가 없었다.

한편, 우리는 이전 글의 서두에서 $V$와 $V^\ast$ 또한 같은 차원을 갖는다는 것을 언급하였는데, 이는 위의 자연스러운 isomorphism $V\rightarrow V^{\ast\ast}$와는 다르게 특정한 basis $\{x_1,\ldots, x_n\}$을 택한 후, 이들의 dual basis $\{\xi^1,\ldots, \xi^n\}$을 택하여 $x_i\mapsto \xi^i$를 통해 정의해야 한다는 차이가 있었다. 

## 쌍선형형식

이제 우리는 $V=W$인 경우에 집중한다.

::: 정의 1
임의의 pairing $\langle -,-\rangle:V\times W\rightarrow \mathbb{K}$에 대하여, 만일 $W=V$라면 이 pairing을 $V$ 위에서 정의된 *bilinear form<sub>쌍선형형식</sub>*이라 부른다. $\langle -,-\rangle$이 *non-degenerate bilinear form<sub>비퇴화 쌍선형형식</sub>*이라는 것은 $\langle-,-\rangle$이 pairing으로서 non-degenerate인 것이다.
:::

$V$ 위에 bilinear form이 주어졌다 하자. 그럼 위와 같은 논증을 통해, 우리는 $V$에서 $V^\ast$로의 linear map들

$$v\mapsto \langle v,-\rangle,\qquad v\mapsto \langle -,v\rangle$$

을 얻는다. 일반적으로 이 둘은 같을 필요가 없지만, 다음을 정의할 수 있다.

::: 정의 2
임의의 bilinear form $\langle-,-\rangle:V\times V\rightarrow \mathbb{K}$에 대하여, 다음의 식

$$\langle v,w\rangle=\langle w,v\rangle$$

이 모든 $v,w\in V$에 대해 성립하면 이 form이 *symmetric<sub>대칭적</sub>*이라 말한다. 만일 모든 $v,w\in V$에 대해 다음의 식

$$\langle v,w\rangle=-\langle w,v\rangle$$

이 성립하면 이 form이 *alternating<sub>교대적</sub>*이라 말한다.
:::

## 비퇴화 쌍선형형식

유한차원 $\mathbb{K}$-벡터공간 $V$가 주어졌다 하고, 앞서 언급한 canonical pairing $\langle-,-\rangle:V\times V^\ast\rightarrow \mathbb{K}$을 생각하자. 만일 $V$ 위에 non-degenerate pairing $\langle -,-\rangle:V\times V\rightarrow \mathbb{K}$가 주어졌다면, 우리는 [§쌍대공간, ⁋명제 4](/ko/math/linear_algebra/dual_space#prop4)와 $\dim V=\dim V^\ast$로부터 $\langle -,-\rangle$이 isomorphism 

$$V\rightarrow V^\ast;\qquad v\mapsto \langle -,v\rangle\tag{1}$$

을 정의한다는 것을 안다. 

식 (1)의 isomorphism은 다음과 같이 다시 쓸 수 있다.

::: 따름정리 3
Non-degenerate bilinear form $\langle -,-\rangle$이 주어진 유한차원 $\mathbb{K}$-벡터공간 $V$를 생각하자. 임의의 $f\in V^\ast$가 주어질 때마다, 적당한 $w\in V$가 유일하게 존재하여 

$$f(v)=\langle v,w\rangle\qquad\text{for all $v\in V$}$$

이 성립한다.
:::

그럼 특히 이전 글에서 정의한 orthogonal complement의 개념을 $V$로 가져올 수 있다. 즉, 다음과 같이 정의하자.

::: 정의 4
Non-degenerate bilinear form $\langle -,-\rangle$이 주어진 유한차원 $\mathbb{K}$-벡터공간 $V$를 생각하자. 임의의 $v\in V$에 대하여, 다음의 식 $\langle w,v\rangle=0$을 만족하는 모든 $w\in V$들의 모임을 $v$의 *orthogonal complement<sub>직교여공간</sub>*이라 하고, $v^\perp$로 적는다. 더 일반적으로, 임의의 부분집합 $S\subseteq V$에 대하여, 다음 집합

$$S^\perp=\bigcap_{v\in S}v^\perp$$

을 $S$의 orthogonal complement로 정의한다.
:::

벡터 $w\in V$는 [따름정리 3](#cor3)에 의해 $f\in V^\ast$를 유일하게 지정하는데, 위의 정의는 만일 이렇게 얻어진 $f$가 [§쌍대공간, ⁋정의 7](/ko/math/linear_algebra/dual_space#def7)의 의미에서 $v$의 orthogonal complement에 속한다면, $w$를 $v$에 직교하는 것으로 생각하고, 이러한 $w$들을 모아둔 것을 orthogonal complement로 생각하겠다는 의미이다. 이러한 과정을 통해 [§쌍대공간](/ko/math/linear_algebra/dual_space)의 결과들을 모두 $V$로 가져올 수 있다. 남은 글에서 우리는 이 과정을 자세히 살펴본다.

일반적인 bilinear form에서는 $\langle w,v\rangle=0$으로 정의한 $v^\perp$과 $\langle v,w\rangle=0$으로 정의한 것이 서로 다를 수 있어, $W^\perp$이 왼쪽에서 정의되었는지, 오른쪽에서 정의되었는지에 따라 그 정의가 달라질 수 있다. 이와 같은 현상을 피하기 위해서는 다음과 같은 성질을 생각하는 것이 현명하다. 

::: 정의 5
Bilinear form $\langle-,-\rangle$이 임의의 $v,w\in V$에 대하여 $\langle v,w\rangle=0$과 $\langle w,v\rangle=0$이 서로 동치가 되도록 할 때, $\langle-,-\rangle$이 *reflexive<sub>반사적</sub>*라 한다.
:::

Symmetric form이 reflexive한 것은 자명하지만, 그 역은 성립하지 않는다. 가령 alternating form 역시

$$\langle v,w\rangle=-\langle w,v\rangle$$

이므로 reflexive이다. 놀랍게도 reflexive form은 정확히 이 둘, 곧 symmetric이거나 alternating인 form뿐이다.

::: 명제 6
유한차원 $\mathbb{K}$-벡터공간 $V$ 위의 bilinear form $\langle-,-\rangle$이 reflexive인 것은 그것이 symmetric이거나 alternating인 것과 동치이다.
:::

::: 증명
한쪽 방향은 이미 살펴보았으므로, $\langle-,-\rangle$이 reflexive라 가정하고 반대방향만 보이면 충분하다. 임의의 $u,v,w$에 대하여 

$$\langle u,\langle u,w\rangle v-\langle u,v\rangle w\rangle=\langle u,w\rangle\langle u,v\rangle-\langle u,v\rangle\langle u,w\rangle=0$$

이므로, reflexivity로부터 $\langle\langle u,w\rangle v-\langle u,v\rangle w,u\rangle=0$이고, 이를 같은 방식으로 전개하면

$$\langle u,w\rangle\langle v,u\rangle=\langle u,v\rangle\langle w,u\rangle\tag{$\ast$}$$

이 모든 $u,v,w$에 대해 성립한다. 

이제 만일 모든 $u$에 대해 $\langle u,u\rangle=0$이면 

$$0=\langle u+v,u+v\rangle=\langle u,v\rangle+\langle v,u\rangle$$

이므로 $\langle-,-\rangle$은 alternating이다. 

그렇지 않으면 $\langle u_0,u_0\rangle\neq 0$인 $u_0$이 존재하며, $(\ast)$에 $w=u=u_0$을 넣으면 

$$\langle u_0,u_0\rangle\bigl(\langle v,u_0\rangle-\langle u_0,v\rangle\bigr)=0$$

이라 모든 $v$에 대해 $\langle v,u_0\rangle=\langle u_0,v\rangle$이 성립함을 안다. 따라서 다시 $(\ast)$에 $v=u_0$을 넣으면 

$$\langle u,u_0\rangle\bigl(\langle u,w\rangle-\langle w,u\rangle\bigr)=0$$

을 얻는다. 위의 $u,w$는 임의의 벡터가 될 수 있으며, 두 가지 경우가 존재한다. 우선 만일 $\langle u,u_0\rangle\neq 0$이라면 곧바로 $\langle u,w\rangle=\langle w,u\rangle$이다. 만일 $\langle u,u_0\rangle=0$인 경우, $u'=u+u_0$로 두면 $\langle u', u_0\rangle=\langle u_0,u_0\rangle\neq 0$이며 따라서 모든 $w$에 대하여 $\langle u', w\rangle=\langle w,u'\rangle$이 성립한다. 그런데 우리는 이미 모든 벡터에 대하여 $\langle u_0,w\rangle=\langle w,u_0\rangle$임을 위에서 보였고, 이로부터 결론을 얻는다.
:::

따라서 orthogonal complement가 좌우에 무관한 form은 정확히 symmetric form과 alternating form이다. 앞으로 부분공간에 대한 결과들은 이 두 경우를 아우르는 non-degenerate reflexive form에서 전개하며, 이는 특히 non-degenerate alternating form에도 그대로 적용된다. 몇 가지 정의를 추가하자. 

::: 정의 7
Non-degenerate reflexive bilinear form이 주어진 유한차원 $\mathbb{K}$-벡터공간 $V$의 부분공간 $W\leq V$에 대하여, 다음을 정의한다. 

1. 교집합 $W\cap W^\perp$을 $W$의 *radical<sub>근기</sub>*이라 부른다. 
2. Radical이 $\{0\}$이라면 $W$가 *non-degenerate<sub>비퇴화</sub>*라 부른다.
3. $W\subseteq W^\perp$일 경우, $\langle-,-\rangle$을 $W$로 제한한 것이 항등적으로 $0$이며, 이 때 $W$가 *isotropic<sub>등방적</sub>*이라 말한다.
4. $W^\perp\subseteq W$일 때 $W$가 *coisotropic<sub>여등방적</sub>*이라 한다.
5. $W=W^\perp$인 공간을 *Lagrangian<sub>라그랑지안</sub>*이라 한다. 
:::

$W$의 radical은 $W$ 안에서 $W$ 전체와 직교하는 벡터들의 모임이므로, $W$가 non-degenerate라는 것은 정확히 $\langle-,-\rangle$을 $W$로 제한한 form이 다시 non-degenerate가 되는 것과 같다.

::: 명제 8
Non-degenerate reflexive bilinear form이 주어진 유한차원 $\mathbb{K}$-벡터공간 $V$의 임의의 부분공간 $W\leq V$에 대하여, 다음이 성립한다.

1. $\dim W+\dim W^\perp=\dim V$이다.
2. $(W^\perp)^\perp=W$이다.
3. $W$가 non-degenerate인 것, $W^\perp$가 non-degenerate인 것, 그리고 $V=W\oplus W^\perp$인 것은 서로 동치이다.
:::
::: 증명
Inclusion map $W\hookrightarrow V$의 dual인 restriction $V^\ast\rightarrow W^\ast$은 전사이다. ([§쌍대공간, ⁋명제 6](/ko/math/linear_algebra/dual_space#prop6)) 한편 $\langle-,-\rangle$이 non-degenerate이므로, $v\mapsto\langle v,-\rangle$은 단사이고 차원이 같아 isomorphism $V\rightarrow V^\ast$을 정의한다. 따라서 이를 위 restriction과 합성한 

$$V\rightarrow W^\ast;\qquad v\mapsto\langle v,-\rangle\vert_W$$

또한 전사이고 그 kernel은 정의에 의하여 $W^\perp$이다. 따라서 [§동형사상, ⁋정리 7](/ko/math/linear_algebra/isomorphic_vector_spaces#thm7)에 의하여 $\dim W^\perp=\dim V-\dim W^\ast=\dim V-\dim W$이므로 첫째 등호가 성립한다. 둘째 주장은 reflexivity에 의해 $W\subseteq(W^\perp)^\perp$이고, 따라서 첫째 등식을 두 번 적용하면 

$$\dim(W^\perp)^\perp=\dim V-\dim W^\perp=\dim W$$

이므로 두 공간이 일치한다.

마지막으로 [§벡터공간의 차원, ⁋예시 8](/ko/math/linear_algebra/dimension#ex8)과 1번을 결합하면

$$\dim(W+W^\perp)=\dim W+\dim W^\perp-\dim(W\cap W^\perp)=\dim V-\dim(W\cap W^\perp)$$

이다. 따라서 $W$의 radical $W\cap W^\perp$이 $\{0\}$인 것은 $W+W^\perp=V$인 것과 동치이고, 이 때 차원 계산에 의해 합은 자동으로 direct sum이 되어 $V=W\oplus W^\perp$이다. 한편 둘째 주장에 의해 $W\cap W^\perp=W^\perp\cap(W^\perp)^\perp$은 $W^\perp$의 radical이기도 하므로, $W$가 non-degenerate인 것과 $W^\perp$가 non-degenerate인 것이 동치이다.
:::

위의 조건을 만족하는 non-degenerate 부분공간에 대해서는 이렇게 정의된 orthogonal complement가 quotient space와 canonical하게 isomorphic하다. 

::: 명제 9
Non-degenerate reflexive bilinear form이 주어진 유한차원 $\mathbb{K}$-벡터공간 $V$의 non-degenerate 부분공간 $W\leq V$에 대하여, [§몫공간, ⁋정의 3](/ko/math/linear_algebra/quotient_space#def3)의 natural projection $p:V\rightarrow V/W$을 $W^\perp$로 제한한

$$p\vert_{W^\perp}:W^\perp\rightarrow V/W$$

은 isomorphism이다.
:::
::: 증명
$W$가 non-degenerate이므로 [명제 8](#prop8)에 의하여 $V=W\oplus W^\perp$이다. Natural projection은 $\ker p=W$를 만족하므로 $p\vert_{W^\perp}$의 kernel은 $W^\perp\cap W=\{0\}$이라 단사이고, $V=W+W^\perp$이므로 임의의 $v=w+w'$ ($w\in W$, $w'\in W^\perp$)에 대하여 $p(w')=w'+W=v+W$이라 전사이다. 따라서 $p\vert_{W^\perp}$은 isomorphism이다.
:::

곧 direct sum $V=W\oplus W^\perp$에서 $W$를 접어 없애면 $W^\perp$이 정확히 그 quotient $V/W$을 실현하게 된다. 일반적으로 quotient space $V/W$는 $\langle-,-\rangle$ 없이도 정의되는 표준적인 대상인 반면, 이를 $V$ 안에서 실현한 대상인 $W^\perp$은 form에 의존하게 되며 [명제 8](#prop8)의 non-degeneracy 없이는 이러한 표현이 불가능하다. 가령 $W\neq\{0\}$이 isotropic이면 $W\cap W^\perp\neq\{0\}$이라 $p\vert_{W^\perp}$이 단사가 되지 못한다.

## 네 개의 기본공간들

이제 두 유한차원 $\mathbb{K}$-벡터공간 $V,W$ 위에 non-degenerate bilinear form $\langle -,-\rangle_V$와 $\langle -,-\rangle_W$가 주어졌다 하자. 원칙적으로 이 절의 내용들은 이들 bilinear form들이 reflexive여도 전개할 수는 있지만, 이를 뒤에 나올 식 (2)와 같은 형태로 조금 더 깔끔하게 표현하기 위해서는 이들이 symmetric인 것이 편하므로 그렇게 가정하기로 하자. 또, 논의의 편의를 위하여 이들 bilinear form이 정의하는 식 (1)의 isomorphism들의 역을 각각

$$\varphi_V:V^\ast\rightarrow V,\qquad \varphi_W:W^\ast\rightarrow W$$

으로 적자. 

만일 $V,W$ 위에 각각 두 basis $\mathcal{B}=\{x_1,\ldots, x_n\}$과 $\mathcal{C}=\{y_1,\ldots, y_m\}$이 주어졌다면, dual basis

$$\mathcal{B}^\ast=\{\xi^1,\ldots, \xi^n\},\qquad\mathcal{C}^\ast=\{\upsilon^1,\ldots,\upsilon^m\}$$

들이 잘 정의된다. 이제 이들을 $\varphi_V,\varphi_W$를 따라 옮긴 basis

$$\mathcal{B}'=\{\varphi_V(\xi^1),\ldots,\varphi_V(\xi^n)\},\qquad\mathcal{C}'=\{\varphi_W(\upsilon^1),\ldots,\varphi_W(\upsilon^m)\}$$

를 생각하자. 즉 이들은 다음의 식

$$\langle x_i,\varphi_V(\xi^j)\rangle=\delta_{ij},\qquad\langle y_i,\varphi_W(\upsilon^j)\rangle=\delta_{ij}$$

을 통해 정의되는 $V,W$의 원소들이다. 이제 임의의 $L:V\rightarrow W$에 대하여, 

$$\begin{aligned}L(x_1)&=\alpha_{11}y_1+\alpha_{21}y_2+\cdots+\alpha_{m1}y_m\\L(x_2)&=\alpha_{12}y_1+\alpha_{22}y_2+\cdots+\alpha_{m2}y_m\\&\phantom{a}\vdots\\L(x_n)&=\alpha_{1n}y_1+\alpha_{2n}y_2+\cdots+\alpha_{mn}y_m\end{aligned}$$

이라 하자. 만일 dual map $L^\ast:W^\ast\rightarrow V^\ast$를 위의 identification $\varphi$들을 통해 $W$에서 $V$로의 map으로 생각한다면, 즉 다음의 diagram

{% diagram Math/Linear_Algebra/Bilinear_Form-1.svg width="8.27em" alt="identification" %}

을 통해 정의되는 $L':W\rightarrow V$를 생각한다면 이 linear map의 두 basis $\mathcal{C}'$, $\mathcal{B}'$에 대한 행렬표현이 $[L']_{\mathcal{B}'}^{\mathcal{C}'}=\bigl([L]_\mathcal{C}^\mathcal{B}\bigr)^t$가 됨을 확인할 수 있다. 

한편, 이렇게 정의한 $L':W\rightarrow V$는 다음 식

$$\langle Lv, w\rangle_W=\langle v,L'w\rangle_V\qquad\text{for all $v\in V$ and $w\in W$}\tag{2}$$

을 만족하는 것을 알 수 있다. 이는

$$\langle Lv,w\rangle=(\varphi^{-1}_W(w))(Lv)=(\varphi^{-1}_W(w)\circ L)(v)=(L^\ast(\varphi^{-1}_W(w)))(v)=(\varphi^{-1}_V(v)\circ L')(w)=(\varphi^{-1}_V(v))(L'w)=\langle v,L'w\rangle$$

으로부터 확인할 수 있다. 이러한 식을 만족하는 $L'$을 우리는 linear map $L$의 *adjoint*라 부르고, 약간의 abuse of notation을 통해 $L^\ast$으로 적기도 한다. 

[§쌍대공간, §§직교여공간](/ko/math/linear_algebra/dual_space#직교여공간)의 결과들은 모두 canonical pairing에 대한 식 $(Lv,f)=(v,L^\ast f)$로부터 얻어졌다. 따라서, 이를 위에서 얻은 non-degenerate bilinear form $\langle -,-\rangle$들에 대한 식 (2)로 대체하면 다음 결과들을 얻는다.

::: 명제 10
Symmetric non-degenerate bilinear form들이 주어진 두 유한차원 $\mathbb{K}$-벡터공간 $V,W$, linear map $L:V\rightarrow W$와 그 adjoint $L^\ast:W\rightarrow V$가 주어졌다 하자. 그럼

1. 임의의 부분공간 $U\subseteq V$에 대하여, $L(U)^\perp=(L^\ast)^{-1}(U^\perp)$가 성립한다.
2. 임의의 부분공간 $U\subseteq W$에 대하여, $L^\ast(U)^\perp=L^{-1}(U^\perp)$가 성립한다.
3. $(\im L)^\perp=\ker(L^\ast)$이 성립한다.
4. $(\im L^\ast)^\perp=\ker L$이 성립한다.
:::

특히, 3번과 4번에서 얻어지는 $V$와 $W$의 부분공간들

$$\ker L, \quad(\ker L)^\perp, \quad\im L,\quad(\im L)^\perp$$

를 $L$에 의해 결정되는 *네 개의 기본공간들<sub>four fundamental subspaces</sub>*이라 부르기도 한다. $\ker L$과 $\im L$이 [정의 7](#def7)의 뜻에서 non-degenerate이면 [명제 8](#prop8)에 의하여 이들은

$$V=\ker L\oplus(\ker L)^\perp,\qquad W=\im L\oplus(\im L)^\perp$$

로 직교분해되며, 특히 $\langle-,-\rangle$이 positive-definite이면 모든 부분공간이 non-degenerate이라 이 분해가 언제나 성립한다.

## 직교기저

이제 symmetric non-degenerate bilinear form이 주어진 $\mathbb{K}$-벡터공간 $V$를 생각하자. 그럼 $V$의 부분집합 $\{v_1,\ldots, v_n\}$이 *orthogonal set*이라는 것은 $i\neq j$일 때마다 $\langle v_i,v_j\rangle=0$이 성립하는 것이다. 만일 $V$의 basis $\mathcal{B}$가 orthogonal set이기도 하다면, 이를 *orthogonal basis*라 부른다.

::: 정의 11
Field $\mathbb{K}$가 다음의 조건

$$\underbrace{1+1+\cdots+1}_\text{$p$ times}=0$$

을 만족하는 자연수 $p$가 존재한다면, 그 가운데 가장 작은 것을 $\mathbb{K}$의 *characteristic<sub>표수</sub>*이라 하고 이를 $\ch \mathbb{K}=p$로 표기한다. 만일 위의 식을 만족하는 자연수 $p$가 존재하지 않는다면 $\mathbb{K}$는 characteristic 0을 갖는 것으로 생각한다.
:::

예를 들어 $\mathbb{R}$은 characteristic 0을 갖는다. 만일 $\mathbb{F}_2=\{0,1\}$에 다음의 식

$$0+0=0,\quad 0+1=1,\quad 1+0=1,\quad 1+1=0$$

그리고

$$0\cdot 0=0,\quad 0\cdot 1=0,\quad 1\cdot 0=0,\quad 1\cdot 1=1$$

으로 덧셈과 곱셈을 각각 정의한다면 $\mathbb{F}_2$는 field의 조건을 만족한다는 것을 확인할 수 있고, 이 때 $\ch\mathbb{F}_2=2$이다. 

::: 명제 12
$\ch \mathbb{K}\neq 2$인 field $\mathbb{K}$에 대하여, symmetric non-degenerate bilinear form이 주어진 유한차원 $\mathbb{K}$-벡터공간 $V$는 항상 orthogonal basis를 갖는다.  
:::
::: 증명
우선 간단한 보조정리를 보이자. 임의로 고정된 $0$이 아닌 $v\in V$에 대하여, 반드시 $\langle u,v\rangle\neq 0$이도록 하는 $u\in V$가 존재한다. 그럼

$$2\langle u,v\rangle=\langle u+v,u+v\rangle-\langle u,u\rangle-\langle v,v\rangle$$

이고, 두 조건 $\langle u,v\rangle\neq 0$과 $\ch \mathbb{K}\neq 2$에서 좌변은 0이 아니다. 따라서 우변의 세 항 $\langle u+v,u+v\rangle, \langle u,u\rangle,\langle v,v\rangle$ 가운데 적어도 하나는 0이 아니다. 따라서,

> Non-degenerate symmetric bilinear form이 주어진 임의의 $\{0\}$이 아닌 $\mathbb{K}$-벡터공간에는 $\langle w,w\rangle\neq 0$을 만족하는 $w$가 반드시 존재한다.

원래의 명제는 $V$의 차원에 대한 귀납법으로 증명한다. $\dim V=0$인 경우는 증명할 것이 없다. 이제 $\dim V=k$인 경우 증명이 완료되었다 가정하자. 그럼 $\dim V=k+1$를 만족하는 임의의 벡터공간 $V$에 대하여, $\langle w,w\rangle\neq 0$을 만족하는 벡터 $w$가 존재한다. 

이제 $W=\span w$라 하자. $\langle w,w\rangle\neq 0$이므로 $w\notin W^\perp$이고, $W$가 $1$차원이라 $W\cap W^\perp=\{0\}$, 곧 $W$는 [정의 7](#def7)의 뜻에서 non-degenerate이다. 따라서 [명제 8](#prop8)에 의하여 $V=W\oplus W^\perp$이고 $W^\perp$ 또한 non-degenerate이며 $\dim W^\perp=\dim V-1=k$이다. 귀납가정을 non-degenerate form을 갖춘 $k$차원 공간 $W^\perp$에 적용하면 orthogonal basis $\mathcal{B}$가 존재하고, $W=\span w$가 $W^\perp$과 직교하므로 $\mathcal{B}\cup\{w\}$가 $V$의 orthogonal basis이다.
:::

## Gram matrix

임의의 bilinear form $\langle-,-\rangle:V\times V\rightarrow \mathbb{K}$가 주어졌다 하자. 만일 $V$의 basis $\mathcal{B}=\{x_1,\ldots, x_n\}$가 고정되었다고 하면, 임의의 $v=\sum v_ix_i, w=\sum w_jx_j$에 대하여 다음의 식

$$\langle v,w\rangle=\left\langle\sum_{i=1}^nv_ix_i,\sum_{j=1}^n w_jx_j\right\rangle=\sum_{i,j=1}^n v_iw_j\langle x_i,x_j\rangle$$

이 성립한다. 잠시 $(i,j)$ 성분이 $\langle x_i,x_j\rangle$인 $n\times n$ 행렬을 $G$라 표기하면, 위 식은

$$\langle v,w\rangle=v^t Gw$$

으로 간단하게 쓸 수 있다. 이 때 $G$를 basis $\mathcal{B}$에 대한 *Gram matrix*라 부른다.

$V$ 위에 주어진 두 basis $\mathcal{B},\mathcal{C}$를 생각하자. 이들에 대한 Gram matrix를 각각 $G_\mathcal{B},G_\mathcal{C}$로 표현하고 위의 식을 정확하게 적으면, 

$$\langle v,w\rangle=[v]^t_\mathcal{B}G_\mathcal{B}[w]_\mathcal{B}=[v]^t_\mathcal{C}G_\mathcal{C}[w]_\mathcal{C}$$

라 할 수 있다. 이제 $[v]_\mathcal{C}=[\id]_\mathcal{C}^\mathcal{B}[v]_\mathcal{B}$이므로, 위의 식의 가장 우변은

$$[v]_\mathcal{C}^tG_\mathcal{C}[w]_\mathcal{C}=\left([\id]_\mathcal{C}^\mathcal{B}[v]_\mathcal{B}\right)^tG_\mathcal{C}\left([\id]_\mathcal{C}^\mathcal{B}[w]_\mathcal{B}\right)=[v]_\mathcal{B}^t\left(([\id]_\mathcal{C}^\mathcal{B})^t G_\mathcal{C}[\id]_\mathcal{C}^\mathcal{B}\right)[w]_\mathcal{B}$$

이 된다. 

---

**참고문헌**

**[Lee]** 이인석, *선형대수와 군*, 서울대학교 출판문화원, 2005.  
**[Goc]** M.S. Gockenbach, *Finite-dimensional linear algebra*, Discrete Mathematics and its applications, Taylor&Francis, 2011.

---