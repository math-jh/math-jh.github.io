---
title: "곡선과 벡터함수"
description: "한 매개변수로 공간곡선을 그리는 벡터값 함수를 도입하고, 성분별 미분으로 속도·가속도·단위접선벡터를 정의한다. 호의 길이와 arc length 매개변수, 곡률과 단위법선벡터, 가속도의 접선·법선 분해를 다룬다."
excerpt: "벡터값 함수와 매개곡선, 속도와 접선, 호의 길이, 곡률과 가속도의 분해"

categories: [Math / Calculus]
permalink: /ko/math/calculus/vector_functions
sidebar: 
    nav: "calculus-ko"

date: 2026-07-04
weight: 13
---

지금까지 우리가 다룬 함수는 실수를 실수로 보내는 $f:\mathbb{R}\rightarrow\mathbb{R}$ 뿐으로, 냉정하게 말하면 극한의 개념이 $\epsilon$-$\delta$를 사용하여 엄밀하게 정의되었다는 것 외에는 고등학교에서 배운 내용과 큰 차이가 없었다. 우리는 이제 이를 일반화하여 실제로 새로운 내용을 살펴본다. 일반화의 방향은 차원을 늘리는 것으로, 여기에는 정의역의 차원을 올리는 방향과 공역의 차원을 올리는 방향이 있다. 이 글에서는 후자, 곧 한 실수를 여러 실수로 보내는 함수 $\mathbf{r}:\mathbb{R}\rightarrow\mathbb{R}^n$을 먼저 다룬다. 이는 매개변수 하나로 공간 속의 곡선을 그리는 벡터값 함수로, 시간에 따라 움직이는 점의 자취로 볼 수 있어 미분이 속도와 가속도라는 물리적 의미를 얻고 적분이 곡선의 길이를 잰다.

## 벡터공간

곡선은 한 실수를 받아 여러 실수로 이루어진 점을 내어주는 함수, 곧 $\mathbb{R}^n$ 안으로 들어가는 함수이므로, 그 공간의 구조를 먼저 간략히 정리한다. $\mathbb{R}^n$은 *벡터공간<sub>vector space</sub>*이며, 이 공간의 원소를 *벡터<sub>vector</sub>*라 부른다. 벡터는 순서쌍

$$\mathbf{a}=(a_1, \ldots, a_n)\qquad a_i\in\mathbb{R}$$

으로 쓰이며, 벡터들 사이에는 두 가지 기본 연산이 있다. 하나는 두 벡터 $\mathbf{v}=(v_1,\ldots,v_n)$와 $\mathbf{w}=(w_1,\ldots,w_n)$를 더하는 *덧셈*

$$\mathbf{v}+\mathbf{w}=(v_1+w_1,\ldots,v_n+w_n)$$

이고, 다른 하나는 실수 $c$를 곱하는 *스칼라곱*

$$c\mathbf{v}=(cv_1,\ldots,cv_n)$$

이다. 이 연산들은 좌표평면에서 본 벡터 연산을 $n$차원으로 그대로 옮긴 것이며, 교환법칙과 결합법칙, 분배법칙 등이 자연스럽게 성립한다. 특별히 다음의 벡터들

$$\mathbf{e}_1=(1,0,\ldots, 0,0),\ldots, \mathbf{e}_n=(0,0,\ldots, 0,1)$$

은 *표준기저벡터*들이라 불리며, 이들을 사용하면 임의의 벡터는

$$\mathbf{v}=\sum_{i=1}^n v_i \mathbf{e}_i$$

으로 써줄 수 있다.

우리가 다루는 공간은 유클리드 공간이므로 여기에 내적과 노름도 함께 사용한다. 두 벡터 $\mathbf{v},\mathbf{w}\in\mathbb{R}^n$의 *내적<sub>inner product</sub>*은 좌표별 곱의 합

$$\mathbf{v}\cdot \mathbf{w}=v_1w_1+\cdots+v_nw_n$$

으로 정의되고, 이로부터 벡터의 *norm<sub>노름</sub>*, 즉 크기는 $\lVert \mathbf{v}\rVert=\sqrt{\mathbf{v}\cdot \mathbf{v}}$로 주어진다. 내적은 두 벡터가 이루는 각도를 재는 데에도 쓰이며, 특히 $\mathbf{v}\cdot \mathbf{w}=0$일 때 두 벡터가 서로 *직교<sub>orthogonal</sub>*한다고 한다.

한편, 세 차원 $\mathbb{R}^3$에서는 추가로 *외적<sub>cross product</sub>*이 정의된다. 두 벡터 $\mathbf{v},\mathbf{w}\in\mathbb{R}^3$에 대해 외적 $\mathbf{v}\times \mathbf{w}$는 $\mathbf{v}$와 $\mathbf{w}$ 모두에 직교하면서 방향이 오른손 법칙을 따르고, 크기는 $\mathbf{v}$와 $\mathbf{w}$가 이루는 평행사변형의 넓이와 같은 벡터이다. 좌표로는

$$\mathbf{v}\times \mathbf{w}=(v_2w_3-v_3w_2,\ v_3w_1-v_1w_3,\ v_1w_2-v_2w_1)$$

로 계산한다. 이 글에서는 외적을 주로 직교하는 벡터를 만드는 도구로 쓴다.

## 벡터값 함수

그럼 우선 다음을 정의할 수 있다. 

::: 정의 1
구간 $I \subseteq \mathbb{R}$의 각 $t$에 점 $\mathbf{r}(t) = (x_1(t), \ldots, x_n(t)) \in \mathbb{R}^n$을 대응시키는 함수 $\mathbf{r}\colon I \rightarrow \mathbb{R}^n$을 *벡터값 함수<sub>vector-valued function</sub>* 또는 *매개곡선<sub>parametrized curve</sub>*이라 하고, 각 $x_i$를 그 *성분함수*라 한다.
:::

직관적으로 이는 $t$가 변함에 따라 벡터공간의 다른 점이 대응되는 규칙으로, 시간에 따라 움직이는 점의 자취를 표현한 것으로 생각할 수 있다. 

벡터값 함수의 극한은 일차원에서의 함수의 극한과 마찬가지로 정의된다. 즉, 임의의 $\epsilon$이 주어질 때마다, 항상 적당한 $\delta>0$이 존재하여 

$$0<\lvert t-t_0\rvert<\delta\implies \lVert \mathbf{r}(t)-\mathbf{v}\rVert<\epsilon$$

를 만족하도록 할 수 있을 때 이 벡터함수 $\mathbf{r}$이 $t\rightarrow t_0$일 때 벡터 $\mathbf{v}$로 수렴한다고 말한다. 그럼 코시–슈바르츠 부등식 

$$\lvert\mathbf{a}\cdot\mathbf{b}\rvert\leq\lVert\mathbf{a}\rVert\lVert\mathbf{b}\rVert$$

에 의하여, 

$$\lvert x_i(t)-v_i\rvert=\lvert(\mathbf{r}(t)-\mathbf{v})\cdot\mathbf{e}_i\rvert\leq\lVert\mathbf{r}(t)-\mathbf{v}\rVert$$

이므로 만일 $\mathbf{r}(t)\rightarrow\mathbf{v}$이면 각 성분도 $x_i(t)\rightarrow v_i$로 수렴한다. 반대로 모든 성분이 수렴하면 

$$\lVert\mathbf{r}(t)-\mathbf{v}\rVert^2=\sum_i(x_i(t)-v_i)^2\rightarrow 0$$

이므로 $\mathbf{r}(t)\rightarrow\mathbf{v}$이다. 즉, 벡터함수의 수렴은 각 성분함수의 수렴과 같은 것이며, 특히 벡터함수의 연속과 미분이 모두 성분별로 잘 정의된다. 

::: 명제 2
$\mathbf{r}(t) = (x_1(t), \ldots, x_n(t))$의 각 성분함수가 $t$에서 미분가능하면 $\mathbf{r}$도 $t$에서 미분가능하고 $\mathbf{r}'(t) = (x_1'(t), \ldots, x_n'(t))$이다.
:::

::: 증명
평균변화율 $(\mathbf{r}(t+h) - \mathbf{r}(t))/h$의 $i$번째 성분은 정확히 $(x_i(t+h) - x_i(t))/h$이다. 각 성분의 극한이 $x_i'(t)$로 존재하므로, $\mathbf{r}'(t) = (x_1'(t), \ldots, x_n'(t))$이다.
:::

또, 비슷한 논증으로 스칼라함수의 곱미분과 같은 규칙이 벡터의 곱셈들로 옮겨진다.

::: 명제 3 (미분 법칙)
$\mathbf{u}, \mathbf{v}\colon I \rightarrow \mathbb{R}^n$이 미분가능하고 $f\colon I \rightarrow \mathbb{R}$가 미분가능하며 $\varphi\colon J \rightarrow I$가 미분가능한 실함수이면

$$(f \mathbf{u})' = f' \mathbf{u} + f \mathbf{u}', \qquad (\mathbf{u} \cdot \mathbf{v})' = \mathbf{u}' \cdot \mathbf{v} + \mathbf{u} \cdot \mathbf{v}', \qquad (\mathbf{u} \circ \varphi)'(t) = \varphi'(t) \mathbf{u}'(\varphi(t))$$

이고, $n = 3$일 때 교차곱에 대해 $(\mathbf{u} \times \mathbf{v})' = \mathbf{u}' \times \mathbf{v} + \mathbf{u} \times \mathbf{v}'$이다.
:::

::: 증명
모두 성분별로 적으면 스칼라함수의 곱미분과 연쇄법칙으로 환원된다. 가령 내적은 $\mathbf{u} \cdot \mathbf{v} = \sum_i u_i v_i$이므로 $(\mathbf{u} \cdot \mathbf{v})' = \sum_i (u_i' v_i + u_i v_i') = \mathbf{u}' \cdot \mathbf{v} + \mathbf{u} \cdot \mathbf{v}'$이고, 외적과 스칼라곱도 각 성분이 $u_i v_j$ 꼴의 곱들의 합이라 같은 방식으로 보일 수 있다. 합성은 [§미분법, ⁋정리 4](/ko/math/calculus/differentiation_rules#thm4)를 각 성분에 적용한 것이다.
:::

이 명제의 유용한 따름정리 중 하나는 $\lVert \mathbf{u}(t)\rVert$가 상수이면 $\mathbf{u} \cdot \mathbf{u} = \lVert \mathbf{u}\rVert^2$도 상수이므로 $(\mathbf{u} \cdot \mathbf{u})' = 2 \mathbf{u} \cdot \mathbf{u}' = 0$, 곧 $\mathbf{u} \perp \mathbf{u}'$라는 것이다. 즉, 길이가 일정한 벡터의 변화율은 항상 그 벡터에 수직이며, 원운동에서 위치벡터와 속도가 수직인 것이 이 사실의 특수한 경우이다.

## 속도와 가속도

위에서 살펴봤듯 벡터 함수는 물리적 현상을 나타내는데 좋은 도구이다. 이제 그 물리적 직관을 설명해 보기로 한다. 

::: 정의 4
곡선 $\mathbf{r}(t)$에 대해 $\mathbf{r}'(t)$를 *속도<sub>velocity</sub>*, 그 크기 $\lVert \mathbf{r}'(t)\rVert$를 *속력<sub>speed</sub>*, $\mathbf{r}''(t)$를 *가속도<sub>acceleration</sub>*라 한다. $\mathbf{r}'(t) \neq 0$인 점에서

$$\mathbf{T}(t) = \frac{\mathbf{r}'(t)}{\lVert \mathbf{r}'(t)\rVert}$$

을 *단위접선벡터<sub>unit tangent vector</sub>*라 한다.
:::

속도는 곡선의 진행 방향을 가리키고 그 크기가 점이 움직이는 빠르기이며, 단위접선벡터는 속도의 방향만 남긴 것이다. 이것이 잘 정의되기 위한 조건은 매개곡선 $\mathbf{r}$이 *일급정칙곡선<sub>$C^1$-regular curve</sub>*이라는 것으로, 이는 다음 두 조건을 모두 만족하는 곡선들이다. 

1. $\mathbf{r}$이 *일급<sub>$C^1$</sub>*이다. 즉, 속도벡터 $\mathbf{r}'(t)$가 연속적으로 존재한다. 
2. $\mathbf{r}$이 *정칙<sub>regular</sub>*이다. 즉, $\mathbf{r}'(t)$가 $0$이 되는 곳이 없다. 

그럼 특히 둘째 조건에 의해 단위접선벡터 $\mathbf{T}$가 어디서나 잘 정의되며, 첫째 조건에 의해 $\mathbf{T}(t)$는 연속이다. 이 글에서는 특별한 언급이 없는 한 일급정칙 곡선을 기본으로 다룬다. 

움직이는 대상이 주어졌을 때, 우리가 궁금한 것 중 하나는 시간동안 움직인 거리다. 이는 1차원에서와 마찬가지로, 속도 벡터를 적분하여 얻을 수 있으며, 엄밀하게는 곡선을 곡선 위의 점들을 잇는 다각형으로 근사하여, 분할 

$$a = t_0 < \cdots < t_m = b$$

에 대해 선분 길이의 합 

$$\sum_k \lVert \mathbf{r}(t_k) - \mathbf{r}(t_{k-1})\rVert$$

을 만들고 분할을 잘게 하여 이것이 $\lVert \mathbf{r}'(t)\rVert$의 리만 합으로 수렴한다는 것을 보이는 것으로, 이 과정을 압축하면 다음의 정의를 얻는다. 

::: 정의 5
일급곡선 $\mathbf{r}\colon [a, b] \rightarrow \mathbb{R}^n$의 *arc length<sub>호의 길이</sub>*는

$$L = \int_a^b \lVert \mathbf{r}'(t)\rVert \mathop{dt}$$

이다.
:::

피적분함수 $\lVert \mathbf{r}'(t)\rVert$는 연속이므로 적분가능하다 ([§적분, ⁋정리 10](/ko/math/calculus/integration#thm10)). 이제 시작점에서 잰 호의 길이

$$s(t) = \int_a^t \lVert \mathbf{r}'(\tau)\rVert \mathop{d\tau}$$

를 *arc length<sub>호의 길이</sub>*라 하며, 미적분의 기본정리에 의해 $s'(t) = \lVert \mathbf{r}'(t)\rVert > 0$이므로 $s$는 증가함수이고, $t$를 $s$로 풀어 곡선을 arc length로 다시 매개화할 수 있다.

::: 명제 6
곡선을 arc length $s$로 매개화하면 단위속력이다. 즉 $\lVert d\mathbf{r}/ds\rVert = 1$이다.
:::

::: 증명
연쇄법칙으로 $d\mathbf{r}/\mathop{dt} = (d\mathbf{r}/ds)(ds/\mathop{dt})$이고 $ds/\mathop{dt} = \lVert \mathbf{r}'(t)\rVert = \lVert d\mathbf{r}/\mathop{dt}\rVert$이므로, $\lVert d\mathbf{r}/ds\rVert = \lVert d\mathbf{r}/\mathop{dt}\rVert / (ds/\mathop{dt}) = 1$이다.
:::

이렇게 얻어지는 parametrization을 *arc length parametrization*이라 부른다. 

## 곡률

곡선이 얼마나 휘는지는 단위접선벡터의 방향이 진행에 따라 얼마나 빨리 바뀌는가로 잰다. 그러나 곡선이 빠르게 움직인다면 바뀌는 속도 또한 같이 빨라질 것이므로, 곡선의 모양이 얼마나 휘었는지를 살펴보기 위해서는 이 속도를 똑같이 맞춰줘야 한다. 또, 직관적으로 이는 원래의 곡선을 미분한 단위접선벡터를 한 번 더 미분하여 얻어진 것이므로, 우리는 이제 <em-ko>이급</em-ko>곡선을 생각해야 한다. 즉, 가속도벡터 $\mathbf{r}''(t)$까지 연속적으로 존재한다.

::: 정의 7
이급정칙곡선의 *곡률<sub>curvature</sub>*은 단위접선벡터가 arc length에 대해 변하는 비율의 크기

$$\kappa = \left\lVert \frac{d\mathbf{T}}{ds}\right\rVert$$

이다. $d\mathbf{T}/ds \neq 0$일 때 그 방향의 단위벡터 

$$\mathbf{N} = \frac{d\mathbf{T}/ds}{\lVert d\mathbf{T}/ds\rVert}$$

를 *단위법선벡터<sub>unit normal vector</sub>*라 한다.
:::

[명제 6](#prop6)에 의해 $\mathbf{T} = d\mathbf{r}/ds$는 단위벡터인 것에 주목하자. 그럼 [명제 3](#prop3) 직후에 살펴본, 길이가 일정한 벡터의 변화율은 그 벡터에 수직이라는 앞의 관찰에 의해 $d\mathbf{T}/ds \perp \mathbf{T}$이다. 즉, 단위법선벡터 $\mathbf{N}$은 항상 접선에 수직이며, 곡선이 휘어 들어가는 안쪽을 가리킨다. 

위의 정의는 일반적인 $n$차원 공간 안에서의 곡선에 대한 것이지만, $3$차원 공간에서는 외적을 사용하면 이를 더 편하게 계산할 수 있다. 특히, 다음 공식은 arc length parametrization 없이 바로 적용 가능하므로 훨씬 편하다.

::: 명제 8 (곡률 공식)
$3$차원 공간 안의 이급정칙곡선 $\mathbf{r}(t)$의 곡률은

$$\kappa = \frac{\lVert \mathbf{r}' \times \mathbf{r}''\rVert}{\lVert \mathbf{r}'\rVert^3}$$

이고, 특히 평면곡선 $y = f(x)$의 곡률은 

$$\kappa = \frac{\lvert f''\rvert}{(1 + f'^2)^{3/2}}$$

이다.
:::

::: 증명
$v = \lVert \mathbf{r}'\rVert = ds/\mathop{dt}$로 두면 $\mathbf{r}' = v\mathbf{T}$이다. 곱의 미분법에 의해

$$\mathbf{r}'' = v'\mathbf{T} + v\mathbf{T}'(t)$$

이고, 연쇄법칙 $\mathbf{T}'(t) = (d\mathbf{T}/ds)v$와 $\lVert d\mathbf{T}/ds\rVert = \kappa$에서 $\mathbf{T}'(t) = \kappa v\mathbf{N}$이다. 따라서

$$\mathbf{r}' \times \mathbf{r}'' = (v\mathbf{T}) \times (v'\mathbf{T} + \kappa v^2\mathbf{N}) = v^3 \kappa(\mathbf{T} \times \mathbf{N})$$

이다. 여기서 둘째 등호는 $\mathbf{T}\times \mathbf{T}=0$으로부터 얻어진다. 이제 $\mathbf{T} \perp \mathbf{N}$이고 둘 다 단위벡터라 $\lVert \mathbf{T} \times \mathbf{N}\rVert = 1$이므로, 

$$\lVert \mathbf{r}' \times \mathbf{r}''\rVert = v^3 \kappa = \lVert \mathbf{r}'\rVert^3 \kappa$$

가 되어 원하는 등식을 얻는다. 평면곡선 $y = f(x)$에 대한 공식은 $\mathbf{r}(x) = (x, f(x),0)$으로 두고 $3$차원에서의 공식을 그대로 적용하면 된다. 
:::

증명에 등장한 $\mathbf{r}' = v\mathbf{T}$를 한 번 더 미분한 $\mathbf{r}'' = v'\mathbf{T} + \kappa v^2\mathbf{N}$은 그 자체로 의미가 깊다. 가속도가 접선 방향 성분과 법선 방향 성분으로 갈라지는 것이다. 이를 다음과 같은 별도의 명제로 적어두자. 

::: 명제 9 (가속도의 분해)
이급정칙곡선의 가속도는 

$$\mathbf{r}'' = \frac{dv}{\mathop{dt}}\mathbf{T} + \kappa v^2\mathbf{N}$$

으로 분해된다. 여기서 $v = \lVert \mathbf{r}'\rVert$는 속력이다.
:::

접선 성분 $dv/\mathop{dt}$는 속력이 변하는 정도를 알려주고, 법선 성분 $\kappa v^2$은 방향이 휘는 정도를 알려준다. 등속운동이면 $dv/\mathop{dt} = 0$이라 가속도는 순전히 법선 방향, 곧 구심가속도뿐이고 그 크기는 $\kappa v^2$이다. 

::: 예시 10 (나선)
나선 $\mathbf{r}(t) = (\cos t, \sin t, t)$에 대해 $\mathbf{r}'(t) = (-\sin t, \cos t, 1)$, $\mathbf{r}''(t) = (-\cos t, -\sin t, 0)$이다. 외적은

$$\mathbf{r}' \times \mathbf{r}'' = (\sin t,\ -\cos t,\ 1), \qquad \lVert \mathbf{r}' \times \mathbf{r}''\rVert = \sqrt{2}$$

이고 $\lVert \mathbf{r}'\rVert = \sqrt{2}$이므로 곡률은 $\kappa = \sqrt{2}/(\sqrt{2})^3 = 1/2$로 일정하다. 속력 $v = \sqrt{2}$가 일정하므로 [명제 9](#prop9)에서 가속도는 법선 성분뿐이고 그 크기는 $\kappa v^2 = (1/2)\cdot 2 = 1$인데, 실제로 $\lVert \mathbf{r}''(t)\rVert = \lVert(-\cos t, -\sin t, 0)\rVert = 1$로 일치한다.
:::