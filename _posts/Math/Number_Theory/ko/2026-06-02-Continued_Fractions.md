---
title: "연분수"
description: "유리수의 유한 연분수를 유클리드 호제법과 연결하고, 점근분수의 점화식과 행렬식 항등식, 무한 연분수의 수렴을 증명한다. 점근분수가 최량근사임과 Legendre 판정법, 순환연분수와 이차무리수의 동치(Euler, Lagrange), √d의 연분수 전개를 다룬다."
excerpt: "연분수, 점근분수, 최량근사, 순환연분수와 이차무리수, √d의 전개"

categories: [Math / Number Theory]
permalink: /ko/math/number_theory/continued_fractions
sidebar: 
    nav: "number_theory-ko"

date: 2026-06-02
weight: 11

published: false

---

[§나눗셈과 유클리드 호제법, ⁋정리 6](/ko/math/number_theory/euclidean_algorithm#thm6){: data-lid="v7l98" }에서 $a$를 $b$로 나눈 몫과 나머지를 반복해서 구하면 $\gcd(a,b)$가 얻어졌다. 이때 나오는 몫들만 모아 $a/b$를 $a_0+1/(a_1+1/(a_2+\cdots))$ 꼴로 적은 것이 연분수이다. 유리수에서는 이 과정이 유한 단계에서 끝나고, 무리수에서는 끝나지 않는 대신 각 단계의 중간값이 원래 수를 매우 효율적으로 근사한다. 이 글에서는 연분수의 기본 성질을 정리한 뒤, 근사의 최적성과 이차무리수의 연분수가 순환한다는 Lagrange의 정리, 그리고 $\sqrt{d}$의 전개를 증명한다.

## 유한 연분수와 유클리드 호제법

::: 정의 1
정수 $a_0$과 양의 정수 $a_1,\ldots,a_n$에 대하여 *연분수<sub>continued fraction</sub>* $[a_0;a_1,\ldots,a_n]$을 $[a_0]=a_0$,

$$[a_0;a_1,\ldots,a_n]=a_0+\frac{1}{[a_1;a_2,\ldots,a_n]}$$

로 귀납적으로 정의한다. 마지막 항에는 양의 실수 $t$도 허용하여 $[a_0;\ldots,a_{n-1},t]$를 같은 식으로 정의한다. 수열 $a_0,a_1,a_2,\ldots$가 주어졌을 때 $c_k=[a_0;a_1,\ldots,a_k]$를 $k$번째 *점근분수<sub>convergent</sub>*라 부른다.
:::

정의에 의하여 $[a_0;\ldots,a_{k-1},a_k,t]=[a_0;\ldots,a_{k-1},a_k+1/t]$이다. 이후 $a_0$은 임의의 정수, $a_1,a_2,\ldots$는 항상 양의 정수로 둔다.

유클리드 호제법과의 관계는 다음과 같다. 유리수 $x=a/b$ ($b>0$)에 대하여 $x_0=x$로 두고 $x_k$가 정수가 아닐 때까지

$$a_k=\lfloor x_k\rfloor,\qquad x_{k+1}=\frac{1}{x_k-a_k}$$

를 반복한다. 여기서 $\lfloor x\rfloor$는 $x$를 넘지 않는 최대 정수이다. $r_0=a$, $r_1=b$에서 호제법 $r_{k}=a_kr_{k+1}+r_{k+2}$를 돌리면 $x_k=r_k/r_{k+1}$이므로, $a_k$는 호제법의 $k$번째 몫이다. 가령 $67/29$에 호제법을 적용하면

$$\begin{aligned}
67&=2\cdot 29+9,\\
29&=3\cdot 9+2,\\
9&=4\cdot 2+1,\\
2&=2\cdot 1
\end{aligned}$$

이므로 $67/29=[2;3,4,2]$이다. $a_0$은 소수부분을 버린 값이 아니라 바닥 함수의 값이어야 한다. $-7/3$은 $-7=(-3)\cdot 3+2$에서 $a_0=-3$이고, $x_1=3/2$, $x_2=2$로 이어져 $-7/3=[-3;1,2]$이다.

::: 명제 2
모든 유리수는 유한 연분수로 나타내어지며, 그 표현은 정확히 두 가지이다. 하나는 $[a_0;a_1,\ldots,a_n]$ ($n=0$이거나 $a_n\ge 2$) 꼴이고, 다른 하나는 이것의 마지막 항 $a_n$을 $a_n-1,1$로 쪼갠 $[a_0;a_1,\ldots,a_n-1,1]$이다.
:::

::: 증명
존재성. $x_k=u/v$ ($v>0$)가 정수가 아니면 $x_{k+1}=v/(u-a_kv)$이고 $0<u-a_kv<v$이므로 분모가 진짜로 줄어든다. 분모는 양의 정수이므로 어느 단계에서 $x_n$이 정수가 되어 멈춘다. 이때 $x=[a_0;a_1,\ldots,a_n]$이고, $n\ge1$이면 $x_n>1$이므로 $a_n=x_n\ge 2$이다.

유일성. $n\ge 1$이고 $a_n\ge 2$일 때 $y=[a_1;\ldots,a_n]>1$이다. 실제로 $n=1$이면 $y=a_1\ge2$이고, $n\ge2$이면 $y=a_1+1/[a_2;\ldots,a_n]>a_1\ge1$이다. 따라서 $0<1/y<1$이므로 $\lfloor x\rfloor=a_0$이고 $y=1/(x-a_0)$이다. $n=0$이면 $x=a_0$는 정수이다. $x=[a_0;\ldots,a_n]=[b_0;\ldots,b_m]$이 둘 다 이 꼴이면, 위에서 $a_0=b_0=\lfloor x\rfloor$이다. $n=0$이면 $x$가 정수이므로 $m=0$이어야 하고(그렇지 않으면 $x=b_0+1/z$가 정수가 아니다), 반대도 같다. $n,m\ge1$이면 $[a_1;\ldots,a_n]=[b_1;\ldots,b_m]$이므로 길이에 대한 귀납법으로 두 수열이 일치한다.

마지막 항이 $1$인 표현 $[a_0;\ldots,a_{n-1},1]$ ($n\ge 1$)은 $a_{n-1}+1/1=a_{n-1}+1$에 의하여 $[a_0;\ldots,a_{n-2},a_{n-1}+1]$과 같고, 이는 길이가 하나 짧은 위의 꼴이다. 한편 $a_n\ge 2$인 표현을 쪼갠 $[\ldots,a_n-1,1]$도 같은 수이고 $n=0$이어도 $a_0-1$이 정수이므로 성립한다. 따라서 표현은 정확히 두 가지이다.
:::

## 점근분수의 점화식

점근분수를 정의대로 안쪽부터 계산하면 항이 늘 때마다 처음부터 다시 해야 한다. 다음 점화식은 $c_{k}$를 앞의 두 점근분수와 $a_k$만으로 만들어 준다.

::: 명제 3
$p_{-1}=1$, $p_0=a_0$, $q_{-1}=0$, $q_0=1$로 두고 $k\ge1$에 대하여

$$p_k=a_kp_{k-1}+p_{k-2},\qquad q_k=a_kq_{k-1}+q_{k-2}$$

로 정의한다. 그러면 다음이 성립한다.

(가) $k\ge1$과 양의 실수 $t$에 대하여 $[a_0;\ldots,a_{k-1},t]=(tp_{k-1}+p_{k-2})/(tq_{k-1}+q_{k-2})$이다. 특히 $c_k=p_k/q_k$이다.

(나) $k\ge0$에 대하여 $p_kq_{k-1}-p_{k-1}q_k=(-1)^{k-1}$이다. 따라서 $\gcd(p_k,q_k)=1$이다.

(다) $k\ge1$에 대하여 $c_k-c_{k-1}=(-1)^{k-1}/(q_kq_{k-1})$이고, $k\ge2$에 대하여 $c_k-c_{k-2}=(-1)^ka_k/(q_kq_{k-2})$이다.

(라) $1=q_0\le q_1<q_2<\cdots$이고 $q_k\ge k$이다.

(마) $k\ge0$에 대하여 $\begin{pmatrix}p_k&p_{k-1}\\q_k&q_{k-1}\end{pmatrix}=\begin{pmatrix}a_0&1\\1&0\end{pmatrix}\begin{pmatrix}a_1&1\\1&0\end{pmatrix}\cdots\begin{pmatrix}a_k&1\\1&0\end{pmatrix}$이다.
:::

::: 증명
(가) $k$에 대한 귀납법을 쓴다. $k=1$이면 우변은 $(ta_0+1)/t=a_0+1/t=[a_0;t]$이다. $k$에서 성립한다고 하자. $[a_0;\ldots,a_k,t]=[a_0;\ldots,a_{k-1},a_k+1/t]$이고 $a_k+1/t$도 양의 실수이므로 가정에 의하여

$$\begin{aligned}
[a_0;\ldots,a_k,t]&=\frac{(a_k+1/t)p_{k-1}+p_{k-2}}{(a_k+1/t)q_{k-1}+q_{k-2}}
=\frac{t(a_kp_{k-1}+p_{k-2})+p_{k-1}}{t(a_kq_{k-1}+q_{k-2})+q_{k-1}}\\
&=\frac{tp_k+p_{k-1}}{tq_k+q_{k-1}}
\end{aligned}$$

이다 (둘째 등호는 분자와 분모에 $t$를 곱한 것이다). 이것이 $k+1$의 경우이다. $t=a_k$를 넣으면 $[a_0;\ldots,a_{k-1},a_k]=(a_kp_{k-1}+p_{k-2})/(a_kq_{k-1}+q_{k-2})=(p_k)/(q_k)$이다.

(나) $D_k=p_kq_{k-1}-p_{k-1}q_k$로 두면 $D_0=a_0\cdot 0-1\cdot 1=-1$이고, $k\ge1$에서

$$\begin{aligned}
D_k&=(a_kp_{k-1}+p_{k-2})q_{k-1}-p_{k-1}(a_kq_{k-1}+q_{k-2})\\
&=p_{k-2}q_{k-1}-p_{k-1}q_{k-2}=-D_{k-1}
\end{aligned}$$

이므로 $D_k=(-1)^{k+1}=(-1)^{k-1}$이다. $p_k,q_k$의 공약수는 $D_k=\pm1$을 나누므로 $\pm1$뿐이다.

(다) 첫째 식은 (나)의 양변을 $q_kq_{k-1}$로 나눈 것이다. 둘째 식은

$$\begin{aligned}
p_kq_{k-2}-p_{k-2}q_k&=(a_kp_{k-1}+p_{k-2})q_{k-2}-p_{k-2}(a_kq_{k-1}+q_{k-2})\\
&=a_k(p_{k-1}q_{k-2}-p_{k-2}q_{k-1})=(-1)^ka_k
\end{aligned}$$

의 양변을 $q_kq_{k-2}$로 나눈 것이다.

(라) $q_0=1$, $q_1=a_1\ge1$이고, $k\ge2$에서 $q_k=a_kq_{k-1}+q_{k-2}\ge q_{k-1}+1$이므로 $q_k>q_{k-1}$이고 $q_k\ge k$이다.

(마) $k=0$이면 양변이 $\begin{pmatrix}a_0&1\\1&0\end{pmatrix}$이다. 좌변에 오른쪽에서 $\begin{pmatrix}a_{k+1}&1\\1&0\end{pmatrix}$를 곱하면 첫 열은 $(a_{k+1}p_k+p_{k-1},\ a_{k+1}q_k+q_{k-1})^T=(p_{k+1},q_{k+1})^T$이고 둘째 열은 $(p_k,q_k)^T$이다.
:::

(나)를 유리수 $a/b=[a_0;\ldots,a_n]$에 적용하면 [§나눗셈과 유클리드 호제법, ⁋정리 8](/ko/math/number_theory/euclidean_algorithm#thm8){: data-lid="qmyh3" }의 Bézout 계수가 유클리드 호제법에서 나온다. $\gcd(p_n,q_n)=1$이고 $a/b=p_n/q_n$이므로 $a=gp_n$, $b=gq_n$ ($g=\gcd(a,b)$)이고, 따라서 $aq_{n-1}-bp_{n-1}=g(p_nq_{n-1}-p_{n-1}q_n)=(-1)^{n-1}g$이다. $67/29=[2;3,4,2]$에서는 $p_2/q_2=30/13$이고 $67\cdot13-29\cdot30=1$이다.

## 무한 연분수의 수렴

::: 명제 4
$a_0\in\mathbb{Z}$이고 $a_1,a_2,\ldots$가 양의 정수일 때 점근분수 $c_k$는 수렴하며, 극한 $\alpha$는 무리수이다. 또 $c_0<c_2<c_4<\cdots<\alpha<\cdots<c_5<c_3<c_1$이고, $\lvert\alpha-c_k\rvert<1/(q_kq_{k+1})$이다. 이 극한을 $[a_0;a_1,a_2,\ldots]$로 적는다.
:::

::: 증명
[명제 3](#prop3){: data-lid="tvgoe" }의 (다)에서 $c_{2j+2}-c_{2j}>0$, $c_{2j+1}-c_{2j-1}<0$이므로 짝수 번째 점근분수는 증가하고 홀수 번째는 감소한다. 또 $c_{2j+1}-c_{2j}=1/(q_{2j+1}q_{2j})>0$이다. 임의의 $j,m$에 대하여 $N=\max(j,m)$으로 두면 $c_{2j}\le c_{2N}<c_{2N+1}\le c_{2m+1}$이므로 짝수 번째 수열은 위로, 홀수 번째 수열은 아래로 유계이다. 따라서 두 수열은 수렴하고, $\lvert c_{k}-c_{k-1}\rvert=1/(q_kq_{k-1})\to0$이므로($q_k\ge k$) 극한 $\alpha$가 같다. 단조성에서 $\alpha$는 인접한 두 점근분수 사이에 엄밀하게 놓이므로 $\lvert\alpha-c_k\rvert<\lvert c_{k+1}-c_k\rvert=1/(q_kq_{k+1})$이다.

$\alpha=r/s$ ($s\ge1$)이라 하자. $\alpha\ne c_k$이므로 정수 $rq_k-sp_k$는 $0$이 아니고, $\lvert\alpha-c_k\rvert=\lvert rq_k-sp_k\rvert/(sq_k)\ge1/(sq_k)$이다. 앞의 부등식과 합치면 모든 $k$에 대하여 $q_{k+1}<s$가 되어 $q_k\to\infty$에 모순이다.
:::

반대로 무리수에서 출발하면 연분수가 다음과 같이 정해진다.

::: 명제 5
무리수 $\alpha$에 대하여 $x_0=\alpha$, $a_k=\lfloor x_k\rfloor$, $x_{k+1}=1/(x_k-a_k)$로 정의하면 모든 $x_k$는 무리수이고 $x_k>1$ ($k\ge1$)이며 $a_k\ge1$ ($k\ge1$)이다. 이때 $\alpha=[a_0;a_1,a_2,\ldots]$이고 $x_k=[a_k;a_{k+1},\ldots]$이며

$$\alpha-c_k=\frac{(-1)^k}{q_k(x_{k+1}q_k+q_{k-1})}$$

이다. 또 $\alpha=[b_0;b_1,\ldots]$ ($b_0\in\mathbb{Z}$, $b_i\ge1$)이면 $b_i=a_i$이다. 즉 무리수의 무한 연분수 표현은 유일하다.
:::

::: 증명
$x_k$가 무리수이면 $x_k-a_k\in(0,1)$은 무리수이고 $x_{k+1}>1$도 무리수이다. 정의에서 $x_k=a_k+1/x_{k+1}$이므로 $\alpha=[a_0;\ldots,a_k,x_{k+1}]$이고, [명제 3](#prop3){: data-lid="ia9k6" }의 (가)에서 $\alpha=(x_{k+1}p_k+p_{k-1})/(x_{k+1}q_k+q_{k-1})$이다. 따라서

$$\alpha-\frac{p_k}{q_k}=\frac{p_{k-1}q_k-p_kq_{k-1}}{q_k(x_{k+1}q_k+q_{k-1})}=\frac{(-1)^k}{q_k(x_{k+1}q_k+q_{k-1})}$$

이다. 분모의 절댓값이 $q_k^2\to\infty$보다 크므로 $c_k\to\alpha$이다. 즉 $\alpha=[a_0;a_1,\ldots]$이고, 같은 논증을 $x_k$에 적용하면 $x_k=[a_k;a_{k+1},\ldots]$이다.

유일성. $\alpha=[b_0;b_1,\ldots]$이면 $c_k=b_0+1/[b_1;\ldots,b_k]$에서 $k\to\infty$로 보내 $\alpha=b_0+1/y$, $y=[b_1;b_2,\ldots]$를 얻는다. $y=b_1+1/[b_2;b_3,\ldots]>b_1\ge1$이므로 $0<1/y<1$이고 $b_0=\lfloor\alpha\rfloor=a_0$, $y=1/(\alpha-a_0)=x_1$이다. 이제 $x_1$에 같은 논증을 반복하면 $b_i=a_i$이다.
:::

## 최량근사

[명제 5](#prop5){: data-lid="9yf62" }의 오차 공식에서 $x_{k+1}>a_{k+1}$이므로 분모는 $q_k(x_{k+1}q_k+q_{k-1})>q_kq_{k+1}$이다. 이는 [명제 4](#prop4){: data-lid="soh6h" }의 부등식 $\lvert\alpha-p_k/q_k\rvert<1/(q_kq_{k+1})\le1/q_k^2$이고, 무리수에 대하여 $\lvert\alpha-p/q\rvert<1/q^2$을 만족하는 기약분수가 무한히 많다는 것을 보인다. 점근분수는 여기에 더해 다음의 최적성을 갖는다.

::: 정리 6 (최량근사)
$\alpha$가 무리수이고 $k\ge0$, 정수 $p,q$가 $1\le q<q_{k+1}$을 만족하면 $\lvert q\alpha-p\rvert\ge\lvert q_k\alpha-p_k\rvert$이고, 등호는 $(p,q)=(p_k,q_k)$일 때에만 성립한다. 또 $k\ge1$이면 $q\le q_k$인 모든 유리수 $p/q\ne p_k/q_k$에 대하여 $\lvert\alpha-p/q\rvert>\lvert\alpha-p_k/q_k\rvert$이다.
:::

::: 증명
[명제 3](#prop3){: data-lid="re4cz" }의 (나)에 의하여 $p_kq_{k+1}-p_{k+1}q_k=\pm1$이므로 연립방정식 $p=up_k+vp_{k+1}$, $q=uq_k+vq_{k+1}$은 Cramer 공식으로 정수해 $(u,v)$를 갖는다.

$v=0$이면 $(p,q)=u(p_k,q_k)$이고 $q>0$이므로 $u\ge1$이다. 이때 $\lvert q\alpha-p\rvert=u\lvert q_k\alpha-p_k\rvert$이고 $u=1$일 때에만 등호이다. $u=0$이면 $q=vq_{k+1}$이므로 $q\ge q_{k+1}$이 되어 가정에 모순이다. 이제 $u,v\ne0$이라 하자. $u,v$가 둘 다 양수이면 $q\ge q_k+q_{k+1}>q_{k+1}$이고, 둘 다 음수이면 $q<0$이므로 둘은 부호가 반대이다. 한편 [명제 4](#prop4){: data-lid="lt118" }에서 $\alpha-c_k$의 부호는 $(-1)^k$이고 $\alpha-c_{k+1}$의 부호는 $(-1)^{k+1}$이므로 $q_k\alpha-p_k$와 $q_{k+1}\alpha-p_{k+1}$도 부호가 반대이다. 따라서 $u(q_k\alpha-p_k)$와 $v(q_{k+1}\alpha-p_{k+1})$은 부호가 같고

$$\lvert q\alpha-p\rvert=\lvert u\rvert\lvert q_k\alpha-p_k\rvert+\lvert v\rvert\lvert q_{k+1}\alpha-p_{k+1}\rvert>\lvert q_k\alpha-p_k\rvert$$

이다 ($\lvert u\rvert\ge1$이고 $q_{k+1}\alpha-p_{k+1}\ne0$).

둘째 주장. $k\ge1$이면 [명제 3](#prop3){: data-lid="u1paz" }의 (라)에서 $q_k<q_{k+1}$이므로 $q\le q_k$이면 첫 주장이 적용된다. $p/q\ne p_k/q_k$이면 $(p,q)\ne(p_k,q_k)$이므로 $\lvert q\alpha-p\rvert>\lvert q_k\alpha-p_k\rvert$이고,

$$\lvert\alpha-p/q\rvert=\frac{\lvert q\alpha-p\rvert}{q}>\frac{\lvert q_k\alpha-p_k\rvert}{q}\ge\frac{\lvert q_k\alpha-p_k\rvert}{q_k}=\lvert\alpha-p_k/q_k\rvert$$

이다.
:::

둘째 주장에서 $k\ge1$이 필요하다. $q_0=q_1=1$이면 $q_0<q_1$이 깨지기 때문이다.

::: 예시 7
$\alpha=\sqrt3-1$은 $x_1=(\sqrt3+1)/2$, $x_2=\sqrt3+1$, $x_3=x_1$로 이어지므로 $[0;\overline{1,2}]$이다. $c_0=0$인데 분모가 $q_0=1$ 이하인 유리수 $1$은 $\lvert\alpha-1\rvert=2-\sqrt3\approx0.27$로 $\lvert\alpha-c_0\rvert\approx0.73$보다 가깝다. $a_1=1$이면 $a_0$은 최량근사가 아닐 수 있다.
:::

반대 방향의 판정은 Legendre에 의한 다음 정리이다.

::: 정리 8 (Legendre)
$\alpha$가 무리수이고 정수 $p,q$ ($q\ge1$)가 $\lvert\alpha-p/q\rvert<1/(2q^2)$을 만족하면 $p/q$는 $\alpha$의 점근분수이다.
:::

::: 증명
$p/q$를 기약분수로 바꾸면 $q$는 작아지고 부등식은 더 강해지므로 $\gcd(p,q)=1$이라 가정한다. $q_0=1\le q$이고 $q_k\to\infty$이므로 $q_k\le q<q_{k+1}$인 $k$가 있다. [정리 6](#thm6){: data-lid="mpwyl" }에 의하여 $\lvert q_k\alpha-p_k\rvert\le\lvert q\alpha-p\rvert<1/(2q)$이고, 따라서 $\lvert\alpha-p_k/q_k\rvert<1/(2qq_k)$이다.

$p/q\ne p_k/q_k$라 가정하면 $pq_k-p_kq$가 $0$이 아닌 정수이므로 $\lvert p/q-p_k/q_k\rvert\ge1/(qq_k)$이다. 한편 삼각부등식에서

$$\frac{1}{qq_k}\le\left\lvert\frac pq-\alpha\right\rvert+\left\lvert\alpha-\frac{p_k}{q_k}\right\rvert<\frac{1}{2q^2}+\frac{1}{2qq_k}$$

이므로 $1/(2qq_k)<1/(2q^2)$, 즉 $q<q_k$가 되어 $q_k\le q$에 모순이다. 따라서 $p/q=p_k/q_k$이다.
:::

상수 $1/2$은 줄일 수 없다. 오차가 $1/q^2$ 미만이라는 조건만으로는 점근분수임이 보장되지 않기 때문이다.

::: 예시 9
$\sqrt2=[1;\overline{2}]$의 점근분수는 $1, 3/2, 7/5, 17/12,\ldots$이다. 분수 $4/3$은 점근분수가 아니지만 $4/3<\sqrt2<17/12=(4/3+3/2)/2$이므로 $3/2$보다 $\sqrt2$에 가깝고, $\sqrt2<13/9=4/3+1/9$이므로 $\lvert\sqrt2-4/3\rvert<1/3^2$이다. 이 값은 $1/(2\cdot3^2)$보다는 크다($\sqrt2>25/18$이 아니라 $\sqrt2<25/18$이므로 $\lvert\sqrt2-4/3\rvert>1/18$).
:::

따라서 [정리 6](#thm6){: data-lid="2jdv4" }은 점근분수가 분모가 작은 쪽의 모든 유리수보다 가깝다는 것을 말할 뿐, 그런 성질을 갖는 분수가 점근분수뿐이라는 것은 아니다. 점근분수와 점근분수 사이에 끼는 분수 $(p_{k-1}+jp_k)/(q_{k-1}+jq_k)$ ($1\le j<a_{k+1}$)도 이 성질을 가질 수 있고, [예시 9](#ex9){: data-lid="r6iup" }의 $4/3=(p_0+p_1)/(q_0+q_1)$이 그 경우이다.

## 순환연분수와 이차무리수

정수 계수 이차 polynomial의 무리수 근을 *이차무리수<sub>quadratic irrational</sub>*라 한다. 무한 연분수가 어느 항부터 반복되면, 즉 $a_{i+l}=a_i$ ($i\ge m$)인 $m,l\ge 1$이 있으면 이를 *순환연분수*라 하고 $[a_0;\ldots,a_{m-1},\overline{a_m,\ldots,a_{m+l-1}}]$로 적는다. $m=0$인 경우를 순수 순환이라 부른다.

::: 정리 10 (Euler)
순환연분수의 값은 이차무리수이다.
:::

::: 증명
$x=[a_0;\ldots,a_{m-1},\overline{b_0,\ldots,b_{l-1}}]$이라 하고 $y=[\overline{b_0;b_1,\ldots,b_{l-1}}]$로 둔다. [명제 5](#prop5){: data-lid="ft2nl" }의 꼬리 표현에서 $y=[b_0;\ldots,b_{l-1},y]$이다. $b$의 점근분수 분자·분모를 $P_k,Q_k$로 쓰면 [명제 3](#prop3){: data-lid="tzlvt" }의 (가)에 의하여 $y=(yP_{l-1}+P_{l-2})/(yQ_{l-1}+Q_{l-2})$이고, 정리하면

$$Q_{l-1}y^2+(Q_{l-2}-P_{l-1})y-P_{l-2}=0$$

이다. $Q_{l-1}\ge1$이고 $y$는 [명제 4](#prop4){: data-lid="kmapg" }에서 무리수이므로 $y$는 이차무리수이다. $m=0$이면 $x=y$이다. $m\ge1$이면 $x=[a_0;\ldots,a_{m-1},y]=(yp_{m-1}+p_{m-2})/(yq_{m-1}+q_{m-2})$이므로 $x\in\mathbb{Q}(y)$이다. $\mathbb{Q}(y)$는 $\mathbb{Q}$ 위의 2차 확대이고 $x$는 무리수이므로 $x$의 차수는 2이다.
:::

이 정리의 대우로, 이차무리수가 아닌 무리수의 연분수는 순환하지 않는다. $e=[2;1,2,1,1,4,1,1,6,\ldots]$이 그 예이다.

::: 정리 11 (Lagrange)
이차무리수의 연분수 전개는 어느 항부터 순환한다.
:::

::: 증명
$\alpha$가 $f(X)=aX^2+bX+c$ ($a,b,c\in\mathbb{Z}$, $a\ne0$)의 근이라 하자. $\alpha$가 무리수이므로 $f$는 유리근이 없고 $D=b^2-4ac>0$이다. $F(X,Y)=aX^2+bXY+cY^2$으로 두고, $k\ge1$에 대하여 [명제 5](#prop5){: data-lid="l669l" }의 $\alpha=(x_{k+1}p_k+p_{k-1})/(x_{k+1}q_k+q_{k-1})$을 $f(\alpha)=0$에 대입하여 $(x_{k+1}q_k+q_{k-1})^2$을 곱하면 $F(x_{k+1}p_k+p_{k-1},x_{k+1}q_k+q_{k-1})=0$이다. 이를 전개해

$$A_kx_{k+1}^2+B_kx_{k+1}+C_k=0,\quad A_k=F(p_k,q_k),\quad C_k=F(p_{k-1},q_{k-1})=A_{k-1}$$

을 얻는다. $B_k$도 정수이다. 이제 세 가지를 확인한다.

첫째, $A_k=q_k^2f(p_k/q_k)\ne0$이다. $f$에 유리근이 없기 때문이다.

둘째, $A_k$는 유계이다. $f(\alpha)=0$이므로 $f(p_k/q_k)=f(p_k/q_k)-f(\alpha)=(p_k/q_k-\alpha)\bigl(a(p_k/q_k+\alpha)+b\bigr)$이고, [명제 4](#prop4){: data-lid="uxq3p" }에서 $\lvert p_k/q_k-\alpha\rvert<1/q_k^2$이므로 $\lvert p_k/q_k+\alpha\rvert<2\lvert\alpha\rvert+1$이다. 따라서

$$\lvert A_k\rvert<\lvert a\rvert(2\lvert\alpha\rvert+1)+\lvert b\rvert=:M$$

이고 $\lvert C_k\rvert=\lvert A_{k-1}\rvert<M$이다.

셋째, 판별식이 보존된다. $F(X,Y)$의 Gram 행렬을 $S=\begin{pmatrix}a&b/2\\b/2&c\end{pmatrix}$, $N=\begin{pmatrix}p_k&p_{k-1}\\q_k&q_{k-1}\end{pmatrix}$으로 두면 $x$에 대한 이차식의 Gram 행렬은 $N^{T}SN=\begin{pmatrix}A_k&B_k/2\\B_k/2&C_k\end{pmatrix}$이다. 양변의 행렬식을 취하면 $A_kC_k-B_k^2/4=(\det N)^2(ac-b^2/4)$이고 [명제 3](#prop3){: data-lid="esjak" }의 (나)에서 $\det N=\pm1$이므로 $B_k^2-4A_kC_k=D$이다. 따라서 $B_k^2<D+4M^2$이다.

결국 $(A_k,B_k,C_k)$는 유한 개의 값만 가질 수 있고, 각 삼중쌍에 대하여 $A_k\ne0$이므로 $x_{k+1}$이 될 수 있는 값은 많아야 둘이다. 따라서 $x_j=x_l$인 $1<j<l$이 있다. $a_k=\lfloor x_k\rfloor$이고 $x_{k+1}=1/(x_k-a_k)$이므로 $x_{j+i}=x_{l+i}$ ($i\ge0$)이고, 연분수가 $j$번째 항부터 주기 $l-j$로 순환한다.
:::

## 제곱근의 연분수 전개

$d$가 제곱수가 아닌 양의 정수이면 $\sqrt d$는 이차무리수이므로 [정리 11](#thm11){: data-lid="ygjda" }에 의하여 순환한다. 이 경우 순환의 모양이 더 구체적으로 결정된다.

::: 명제 12
$d$가 제곱수가 아닌 양의 정수이고 $a_0=\lfloor\sqrt d\rfloor$이면 $\sqrt d=[a_0;\overline{a_1,\ldots,a_{l-1},2a_0}]$이고, $a_i=a_{l-i}$ ($1\le i\le l-1$)이다.
:::

::: 증명
$\omega=a_0+\sqrt d$로 두고 $\mathbb{Q}(\sqrt d)$의 켤레를 $z\mapsto z'$로 적는다. $\omega>1$이고 $\omega'=a_0-\sqrt d\in(-1,0)$이다. $x>1$이고 $-1<x'<0$인 수를 *reduced*라 부르자.

(1) $x_0=\omega$의 완전 몫 $x_k$는 모두 reduced이다. $x_k$가 reduced이면 $a_k=\lfloor x_k\rfloor\ge1$이고 $x_{k+1}=1/(x_k-a_k)>1$이다. 켤레는 덧셈과 곱셈을 보존하므로 $x_{k+1}'=1/(x_k'-a_k)$이고 $x_k'-a_k<-1$이므로 $x_{k+1}'\in(-1,0)$이다.

(2) $\omega$는 순수 순환이다. [정리 11](#thm11){: data-lid="8qh69" }에 의하여 $x_j=x_l$인 $0\le j<l$이 있고, $j\ge1$이면 $x_{j-1}=x_{l-1}$임을 보이면 귀납적으로 $x_0=x_{l-j}$를 얻는다. $x_{j-1}=a_{j-1}+1/x_j$이고 (1)에서 $x_{j-1}'=a_{j-1}+1/x_j'\in(-1,0)$이다. 길이가 1인 열린 구간은 정수를 많아야 하나 포함하므로 $a_{j-1}$은 $x_j$만으로 결정되고, $x_{l-1}$에 대해서도 같다. 따라서 $x_{j-1}=x_{l-1}$이다.

(3) 전개의 형태. $\lfloor\omega\rfloor=2a_0$이고 $x_1(\omega)=1/(\omega-2a_0)=1/(\sqrt d-a_0)=x_1(\sqrt d)$이므로 $\omega$의 전개는 $[2a_0;a_1,a_2,\ldots]$이다. (2)에서 $\omega=[\overline{b_0;b_1,\ldots,b_{l-1}}]$ ($b_0=2a_0$, $b_i=a_i$)이고, $\sqrt d=\omega-a_0$이므로 $\sqrt d=[a_0;\overline{a_1,\ldots,a_{l-1},2a_0}]$이다.

(4) 대칭성. $b$의 점근분수 분자·분모로 $N=\begin{pmatrix}p&p'\\q&q'\end{pmatrix}=\begin{pmatrix}P_{l-1}&P_{l-2}\\Q_{l-1}&Q_{l-2}\end{pmatrix}$을 두면 $\omega=[b_0;\ldots,b_{l-1},\omega]$에서 $\omega=(p\omega+p')/(q\omega+q')$이므로

$$q\omega^2+(q'-p)\omega-p'=0\qquad(\mathrm{E}_1)$$

이다. $\omega$는 이차무리수이므로 $\omega'$도 이 방정식의 근이다. $z=-1/\omega'$이라 하고 $\mathrm{E}_1$에 $\omega'=-1/z$를 넣어 정리하면 $z$는

$$p'z^2+(q'-p)z-q=0\qquad(\mathrm{E}_2)$$

의 근이다. 한편 [명제 3](#prop3){: data-lid="33me1" }의 (마)에서 순서를 뒤집은 수열 $b_{l-1},\ldots,b_0$의 행렬곱은 각 인자가 symmetric matrix이므로 $N^T=\begin{pmatrix}p&q\\p'&q'\end{pmatrix}$이다. 따라서 $\rho=[\overline{b_{l-1};\ldots,b_0}]$는 $\rho=(p\rho+q)/(p'\rho+q')$, 곧 $\mathrm{E}_2$를 만족한다. $b_0\ge2$이므로 $p'\ge1$이고 $\mathrm{E}_2$의 두 근의 곱은 $-q/p'<0$이다. 즉 positive root는 하나뿐이고, $z>1$과 $\rho>1$이 모두 positive root이므로 $z=\rho$이다.

이제 $z=-1/\omega'=1/(\sqrt d-a_0)=x_1(\sqrt d)$이므로

$$[a_1;a_2,\ldots,a_{l-1},2a_0,a_1,\ldots]=[a_{l-1};a_{l-2},\ldots,a_1,2a_0,a_{l-1},\ldots]$$

이다. [명제 5](#prop5){: data-lid="l6dod" }의 유일성에 의하여 항이 일치하므로 $a_i=a_{l-i}$ ($1\le i\le l-1$)이다.
:::

실제 전개는 $\mathbb{Q}(\sqrt d)$의 수를 매번 정리하지 않고 정수만으로 계산할 수 있다. $x_k=(P_k+\sqrt d)/Q_k$ ($P_0=0$, $Q_0=1$)로 쓰면 $a_k=\lfloor x_k\rfloor$이고

$$x_{k+1}=\frac{1}{x_k-a_k}=\frac{Q_k}{\sqrt d-P_{k+1}}=\frac{Q_k(\sqrt d+P_{k+1})}{d-P_{k+1}^2}$$

이므로 $P_{k+1}=a_kQ_k-P_k$, $Q_{k+1}=(d-P_{k+1}^2)/Q_k$이다. $Q_k\mid d-P_k^2$이면 $d-P_{k+1}^2=(d-P_k^2)-a_k^2Q_k^2+2a_kQ_kP_k$도 $Q_k$의 배수이므로 $Q_{k+1}$은 정수이고, $Q_{k+1}Q_k=d-P_{k+1}^2$에서 $Q_{k+1}\mid d-P_{k+1}^2$이 되어 귀납이 이어진다. 또 $k\ge1$에서 $Q_k=1$이면 $x_k=P_k+\sqrt d$가 reduced이므로 $-1<P_k-\sqrt d<0$에서 $P_k=a_0$, 즉 $x_k=\omega$이다. 따라서 $Q_k=1$이 되는 첫 $k\ge1$이 주기 $l$이다.

::: 예시 13
$d=7$, $a_0=2$에서 $a_k=\lfloor(P_k+\sqrt7)/Q_k\rfloor$이고 $\sqrt7\approx2.646$이므로

$$\begin{aligned}
(P_0,Q_0)&=(0,1), & a_0&=2,\\
(P_1,Q_1)&=(2,3), & a_1&=\lfloor4.646/3\rfloor=1,\\
(P_2,Q_2)&=(1,2), & a_2&=\lfloor3.646/2\rfloor=1,\\
(P_3,Q_3)&=(1,3), & a_3&=\lfloor3.646/3\rfloor=1,\\
(P_4,Q_4)&=(2,1), & a_4&=\lfloor4.646/1\rfloor=4
\end{aligned}$$

이다 ($P_2=1\cdot3-2$, $Q_2=(7-1)/3$ 등). $Q_4=1$이므로 $l=4$이고 $\sqrt7=[2;\overline{1,1,1,4}]$이다. 중간 항 $1,1,1$은 대칭이고 마지막 항은 $2a_0=4$이다. 점근분수는 $2, 3, 5/2, 8/3, 37/14,\ldots$이다.
:::

같은 방법으로 $\sqrt{13}=[3;\overline{1,1,1,1,6}]$, $\sqrt{19}=[4;\overline{2,1,3,1,2,8}]$, $\sqrt{23}=[4;\overline{1,3,1,8}]$를 얻는다. 주기의 길이는 $d$마다 다르고, 어느 경우에나 중간 항이 회문이며 마지막 항이 $2\lfloor\sqrt d\rfloor$이다.

---

**참고문헌**

**[OL]** 오정환·이준복, *기초 정수론*, 경문사, 2012.
