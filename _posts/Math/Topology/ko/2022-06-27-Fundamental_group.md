---

title: "기본군"
excerpt: "Fundamental group"

lang: ko

categories: [Math / Topology]
permalink: /ko/math/topology/fundamental_group
header:
    overlay_image: /assets/images/Topology/Fundamental_group.png
    overlay_filter: 0.5
sidebar: 
    nav: "topology-ko"

date: 2022-06-27
last_modified_at: 2022-06-27
weight: 100
    
---

**[Mun]**에서는 connectedness를 살펴본 후 separation axiom들과 countability, 그리고 metrization theorem 등을 다룬다. 이들은 모두 굵직한 주제들이지만, 공부하기에 재미있는 주제는 아니므로 우리는 순서를 약간 바꾸어 **[Mun]** 뒤쪽의 대수위상부터 살펴본다.

## Motivation

비전공자, 혹은 위상수학을 아직 배우지 않은 학부생에게 가장 많이 드는 예시는 커피잔과 (속이 꽉 찬) 도넛의 예시일 것이다. 이들 두 도형은 서로 전혀 다르게 생겼지만, 위상수학에서 이야기하는 연속적인 변형이 무엇인지를 이해하면 이 둘이 위상적으로 동일한 공간이라는 것은 쉽게 납득할 수 있다.

하지만 반대로 누군가가 도넛과 볼링공이 어째서 위상적으로 동일하지 않은지를 물어본다면 답하기 쉽지 않다. 이들 두 공간은 모두 connected이고, path connected이며, compact이고, 등등 우리가 이미 배운 위상적인 불변량들을 통해서 구별할 수가 없기 때문이다. 즉 이 말은 우리가 공간에 뚫려 있는 구멍의 개수를 위상적으로 정의할 수 있는 언어가 아직은 없다는 뜻이다. 

직관적으로는 이 둘을 구분하는 방법은 자명하다. 볼링공에 들어있는 임의의 고리는 조금씩 수축시켜 점으로 줄일 수 있지만, 도넛에는 그럴 수 없는 고리가 존재한다. 예를 들어 도넛의 적도를 한 바퀴 감는 고리의 경우, 어떤 식으로 수축시켜도 이 고리를 끊지 않고서는 한 점으로 줄일 수 없기 때문이다. 실은 도넛의 어떠한 점을 잡더라도, 이 점을 지나며 한 점으로 수축될 수 없는 고리를 반드시 하나 찾을 수 있으며, 이는 이 정의가 잘 정의된다는 것을 암시해준다.

아무튼 위의 논증을 수학적인 언어로 쓰기 위해서는 <em_ko>조금씩 수축시키는 것</em_ko>이 어떤 것인지를 우선 정의해야 하는데, 그 정의가 이번 글에서 다룰 중요한 내용이다. 이후 우리는 이렇게 한 점을 지나는 고리들의 모임을 생각하면 이 모임이 실제로 group의 구조를 갖는다는 것을 확인하고, 이 group이 homeomorphism에 대해 불변이라는 것을, 즉 fundamental group이 topological invariant라는 것을 배운다.

한편, 위의 방법은 공간에 뚫려있는 구명의 개수를 세는 방법을 완전하게 제공하지는 않는다. 예컨대 3차원 공간 $\mathbb{R}^3$과, 한 점을 뺀 공간 $\mathbb{R}^3\setminus\\{0\\}$은 이러한 방식으로는 구분할 수 없다. 똑같은 방식으로 $\mathbb{R}^3\setminus\\{0\\}$에서, 뚫려있는 한 점 $0$을 중심으로 고리를 그린다고 하더라도, 이 뚫려 있는 구멍을 살짝 피해서 고리를 수축시킬 수 있기 때문이다. 이를 해결하는 방법 중 하나는, 예컨대 고리 대신 구면 $S^2$를 사용하는 것이겠지만 이와 같은 식의 일반화는 계산상의 문제로 잘 사용하지 않는다. 대수적 위상수학에서는 이 공간을 여전히 잘 구별하면서도 쉽게 계산할 수 있는 또 다른 불변량들을 정의하게 된다.

## Path and homotopy

위에서 정의한 <em_ko>고리</em_ko>라는 것은 본질적으로는 시작과 끝이 동일한 곡선에 불과하다. 그리고 우리는 후자에 대한 정의는 아주 잘 알고 있다. 편의상 앞으로 $I=[0,1]$로 고정하자.

<div class="definition" markdown="1">

<ins id="df1">**정의 1**</ins> 위상공간 $X$에서의 *path<sub>경로</sub>*는 연속함수 $\sigma:I\rightarrow X$를 뜻한다. 두 path $\sigma_0,\sigma_1:I\rightarrow X$가 *homotopic*하다는 것은 이들이 같은 끝점을 가지며, 또 이 끝점들을 공유하는 적당한 path들의 모임 $(\sigma\_t)\_{0\leq t\leq 1}$이 존재하여 다음의 함수

$$F:I\times I\rightarrow X;\qquad F(s,t)=\sigma_t(s)$$

가 연속인 것이다.

</div>

더 일반적으로, 임의의 위상공간 사이의 연속함수들 $f_0,f_1:X\rightarrow Y$이 언제 homotopic한지 또한 정의해줄 수 있다.

위의 식에서 두 번째 $I$와 변수 $t$를 시간의 변화를 나타내는 구간이라 생각하면, 이는 $t=0$에서 path $\sigma_0$으로 시작하여, 시간 $t=1$에서는 path $\sigma_1$로 끝나도록 연속적으로 경로를 변형시키는 것으로 생각할 수 있다. 어렵지 않게, 두 path가 homotopic하다는 relation $\sim$이 equivalence relation이 된다는 것을 확인할 수 있다. 이 때 $\sigma$를 포함하는 equivalence class를 $[\sigma]$로 표기하고, 이를 $\sigma$의 *homotopy class*라 부른다.

$\sim$이 equivalence relation이 된다는 것을 보일 때 가장 덜 자명한 부분은 transitivity이다. 이를 위해서는 시간 $t=0$에서 $1/2$까지는 첫 번째 homotopy를 따라, 그리고 $t=1/2$에서 $1$까지는 두 번째 homotopy를 따라 움직이면 된다. 비슷한 아이디어로 우리는 두 개의 path를 이어줄 수 있다. Path $\sigma:I\rightarrow X$와 $\tau:I\rightarrow X$가 주어졌고, 이들이 $\sigma(1)=\tau(0)$을 만족한다고 하자. 즉 $\sigma$의 끝점과 $\tau$의 시작점이 일치한다. 그럼 이들을 이은 path $\sigma\cdot \tau$는 다음의 식

$$(\sigma\cdot \tau)(s)=\begin{cases}\sigma(2s)&0\leq s\leq \frac{1}{2}\\ \tau(2s-1)&\frac{1}{2}\leq s\leq 1\end{cases}$$

으로 주어지는 path이다. 

## Fundamental group

위상공간 $X$의 *fundamental group*은, 그 이름대로 group이며 우리는 앞서 이 group이 어떻게 생겼는지도 간략하게 설명했다. 이제 이를 엄밀하게 정의하자.

<div class="definition" markdown="1">

<ins id="df2">**정의 2**</ins> 위상공간 $X$와 점 $x_0\in X$에 대하여, $\pi\_1(X,x\_0)$은 $x_0$를 시작점이자 끝점으로 갖는 path들의 homotopy class들로 이루어진 group이다. 이들 사이의 연산은 위에서 정의한 연산 $\cdot$으로 주어진다.

</div>

이 정의가 말이 되기 위해서는 체크해야 할 것이 아주 많다. 

우선 이 연산이 잘 정의되었는지를 확인해야 한다. 즉, $\sigma\sim \sigma'$이고 $\tau\sim \tau'$이라 할 때, $\sigma\cdot \tau$와 $\sigma'\cdot \tau'$이 homotopic인지를 확인해야 한다. 이는 위에서처럼 $t$를 반으로 쪼개어 한 번은 $\sigma$쪽의 homotopy를 타고, 다른 한 번은 $\tau$쪽의 homotopy를 타고 path를 변형시켜주어도 되고, 혹은 동시에 $\sigma,\tau$쪽을 모두 옮겨주어도 된다. 어쨌든 이를 통해 $[\sigma]=[\sigma']$이고 $[\tau]=[\tau']$라면 $[\sigma\cdot\sigma']=[\tau\cdot\tau']$임을 보일 수 있으므로, $\cdot$이 $\pi\_1(X,x\_0)$에서의 잘 정의된 연산이 된다.

이후 연산이 결합법칙을 만족한다는 것을 보여야 한다. 결과적으로 나오는 곡선의 모양은 동일하더라도, 앞서 정의한 $\cdot$의 정의를 따라 계산하면 $(\sigma\cdot \tau)\cdot \rho$는 $\sigma,\tau$를 움직이는 데에 각각 $1/4$만큼, $\rho$를 움직이는 데에 $1/2$만큼의 시간이 필요한 반면 $\sigma\cdot(\tau\cdot \rho)$는 $\tau,\rho$에 각 $1/4$초, $\sigma$에 $1/2$초가 필요하므로 같은 곡선은 아니다. 따라서 이를 보이기 위해서는 path의 재매개화가 homotopy라는 것을 보여야 한다.

물론 $\pi\_1(X,x\_0)$에서 항등원의 역할을 하는 것은 $t=0$부터 $t=1$까지 $x_0$에 멈춰있는 constant loop $e$이다. 다시 한 번 강조하자면, path로서 $\sigma\cdot e\neq \sigma$이지만, 재매개화가 homotopy이므로 $\pi\_1(X,x\_0)$의 원소로서는 $[\sigma][e]=[\sigma]$가 성립한다.

마지막으로 역원이 남아있는데, 이는 간단히 반대방향의 재매개화를 택하면 된다. 즉 $f(t)$의 역원은 $f(1-t)$이다.

이제 우리가 처음 motivation으로 제시했던 정의에 거의 근접했다. 위상공간 $X$와 한 점 $x_0\in X$에 대하여, 만일 $X$에 고리들로 감지할 수 있는 구멍이 존재하지 않는다면 $\pi\_1(X,x\_0)$는 trivial group이 될 것이다. 임의의 고리 $\sigma$를 항상 constant loop $e$로 변형시킬 수 있으므로, $[\sigma]=[e]$이기 때문이다. 만일 $X$에 고리들로 감지해낼 수 있는 구멍이 존재한다면, $\pi\_1(X,x\_0)$에는 최소한 두 개의 원소, 즉 constant loop $[e]$와, 구멍을 사이에 낀 loop $[\sigma]$가 존재할 것이다.

이것이 온전하게 공간 $X$의 성질이 되기 위해서는 위의 논증이 basepoint $x\_0$의 선택에 의존하지 않아야 한다. 만일 어떤 두 점 $x\_0$, $x\_1$에 대하여 $\pi\_1(X, x\_0)$과 $\pi\_1(X, x\_1)$이 서로 다르다면 이를 순수하게 $X$에 대한 성질이라고 부르기에는 찜찜하다.

안타깝게도 $\pi\_1(X,x\_0)$의 정의에 의하여, $X$가 둘 이상의 path component를 갖는다면 $\pi\_1(X,x\_0)$ 또한 basepoint $x_0$에 의해 달라질 수 있다는 것이 분명하다. 그 대신, 다음과 같이 하나의 path component에 대해서는 $\pi\_1(X,x\_0)$이 basepoint $x\_0$에 상관 없이 모두 동일하다.

<div class="proposition" markdown="1">

<ins id="lem3">**보조정리 3**</ins> 임의의 path connected space $X$와 두 점 $x\_0,x\_1\in X$에 대하여 $\pi\_1(X,x\_0)\cong\pi\_1(X,x\_1)$이 성립한다.

</div>

따라서 만일 $X$가 path connected라면 이들 공통의 group을 간단히 $\pi\_1(X)$로 쓰고, 이를 *$X$의 fundamental group*이라 불러도 어색하지 않다. 드디어 다음을 정의할 수 있다.

<div class="definition" markdown="1">

<ins id="df4">**정의 4**</ins> 위상공간 $X$가 *simply connected<sub>단순연결</sub>*이라는 것은 $X$가 path connected이고, $\pi\_1(X)=0$인 것이다.

</div>

## Induced morphism

이번 절에서는 위상공간들과 연속함수를 다루는 대신 *pointed* topological space와 *pointed* continuous map을 사용하는 것이 유리하다. 이들은 일반적인 위상공간과 크게 다른 것은 아니고, 단지 위상공간 $X$와 그 안의 한 원소 $x\_0$이 특정된 순서쌍 $(X,x\_0)$을 의미한다. 그럼 pointed continuous map이란 pointed topological space $(X,x\_0)$에서 $(Y,y\_0)$의 연속함수인데, $f(x\_0)=y\_0$를 만족하는 함수를 의미한다. 일반적인 위상공간들 사이의 연속함수 $f:X\rightarrow Y$가 주어졌고, $X$의 한 점 $x\_0$를 택한다면 $f$ 또한 자연스럽게 pointed topological space $(X,x\_0)$에서 $(Y, f(x\_0))$으로의 pointed continuous map으로 생각할 수 있다.

$f:X\rightarrow Y$가 일반적인 위상공간들 사이의 연속함수라 하자. 우리는 $X$ 위에 정의된 path $\sigma:I\rightarrow X$가 주어질 때마다 $Y$ 위의 path $f\circ\sigma:I\rightarrow Y$를 정의할 수 있다. 특히 만일 $\sigma(0)=\sigma(1)=x_0$라 하면 $(f\circ\sigma)(0)=(f\circ\sigma)(1)=f(x_0)=y_0$일 것이므로 연속함수 $f:X\rightarrow Y$는 식 $f_\ast\sigma=f\circ\sigma$를 통해 함수 $f_\ast:\pi\_1(X,x\_0)\rightarrow\pi\_1(Y,y\_0)$을 유도한다. 이 함수가 잘 정의되었음을 보이기 위해서는 만약 $\sigma_0\sim\sigma_1$이라면 $f\circ\sigma_0\sim f\circ\sigma_1$임을 보여야 하는데, 이는 $(f\circ\sigma\_t)\_{0\leq t\leq 1}$이 $f\circ\sigma_0$와 $f\circ\sigma_1$ 사이의 homotopy를 정의한다는 것을 확인하면 된다. 이를 통해 만일 $[\sigma\_0]=[\sigma\_1]$이라면 $f\_\ast[\sigma\_0]=f\_\ast[\sigma\_1]$임을 알 수 있다.

뿐만 아니라 $f\_\ast$는 이들 사이의 group homomorphism 또한 된다. 즉 $[\sigma],[\tau]\in\pi\_1(X,x\_0)$에 대하여, 다음의 식

$$f_\ast([\sigma][\tau])=(f_\ast[\sigma])(f_\ast[\tau])$$

가 성립한다. 두 연속함수 $f:X\rightarrow Y$, $g:Y\rightarrow Z$에 대하여 $g\_\ast\circ f\_\ast=(g\circ f)\_\ast$인 것과, $\operatorname{id}\_X:X\rightarrow X$가 $(\operatorname{id}\_X)\_\ast=\operatorname{id}\_{\pi\_1(X,x\_0)}$을 정의하는 것은 자명하므로 $\pi\_1$이 object들 $(X,x\_0)$을 $\pi\_1(X,x\_0)$으로, morphism $f:(X,x\_0)\rightarrow (Y,y\_0)$을 $f_\ast$로 옮기는 $\mathbf{Top}_\ast$에서 $\mathbf{Grp}$으로의 functor가 됨을 확인할 수 있다. <#ref#>

이를 통해 $f:X\rightarrow Y$가 homeomorphism이라면 $f_\ast:\pi\_1(X,x\_0)\rightarrow \pi\_1(Y,y\_0)$ 또한 isomorphism임을 알 수 있다. 이는 $(f^{-1})\_\ast$가 $f_\ast$의 역함수가 된다는 것으로부터 분명하다.