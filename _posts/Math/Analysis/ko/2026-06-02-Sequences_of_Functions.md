---
title: "함수열과 점별수렴"
description: "함수열이 수렴하는 가장 단순한 방식인 점별수렴을 정의하고, 연속성·적분·미분이 점별극한에서 보존되지 않는 표준 반례를 계산한다. 이 세 실패를 모두 두 극한의 순서 교환 문제로 정식화하고, 이중수열의 반복극한 예로 그 구조를 확인한다."
excerpt: "점별수렴과, 연속성·적분·미분을 깨뜨리는 반례들, 극한 순서 교환 문제"

categories: [Math / Analysis]
permalink: /ko/math/analysis/sequences_of_functions
sidebar: 
    nav: "analysis-ko"

date: 2026-06-02
weight: 20

published: false

---

수열의 수렴은 수들의 열에 대한 것이었다. 이 글에서는 집합 $E$ 위의 실수값 함수들의 열 $(f_n)$이 어떤 함수 $f$로 수렴한다는 것의 가장 단순한 뜻을 정하고, 그 수렴이 함수의 좋은 성질을 얼마나 보존하는지 확인한다. 결론부터 말하면 거의 아무것도 보존하지 않는다. 연속함수들의 극한이 불연속일 수 있고, 극한의 적분이 적분의 극한과 다를 수 있고, 극한의 도함수가 도함수의 극한과 다를 수 있다.

## 점별수렴

::: 정의 1
$E$ 위의 함수열 $(f_n)$이 함수 $f: E \to \mathbb{R}$로 *점별수렴<sub>pointwise convergence</sub>*한다는 것은, 각 $x \in E$에 대해 수열 $(f_n(x))$이 $f(x)$로 수렴하는 것이다. 곧 각 $x \in E$와 각 $\varepsilon > 0$에 대해 자연수 $N$이 존재하여 $n \geq N$이면 $\lvert f_n(x) - f(x)\rvert < \varepsilon$이다.
:::

정의에서 $N$은 $x$와 $\varepsilon$ 둘 모두에 의존할 수 있다. 점별수렴은 점마다 따로 일어나는 수열의 수렴을 모아 놓은 것일 뿐이어서, 한 점에서의 수렴 속도에 관한 정보는 이웃한 점으로 전달되지 않는다. 이 글의 반례들은 모두 여기서 나온다.

각 점에서의 극한은 [§수열의 수렴, ⁋명제 2](/ko/math/analysis/convergence_of_sequences#prop2)에서 보았듯 유일하므로 점별극한 $f$는 있으면 하나뿐이고, $f = \lim_{n\to\infty} f_n$으로 적는다. 또 $f_n \to f$, $g_n \to g$가 점별로 성립하면 각 점에서 수열의 극한법칙을 적용하여 $f_n + c g_n \to f + c g$와 $f_n g_n \to fg$가 점별로 성립함을 얻는다. 점별극한이 잃어버리는 것은 이런 대수적 구조가 아니라 연속성·적분·미분 같은 해석적 성질이다.

점별수렴하는 점들의 집합도 문제가 된다. $f_n(x) = x^n$을 $\mathbb{R}$ 전체에서 보면, $\lvert x\rvert < 1$이면 $x^n \to 0$이고 $x = 1$이면 $x^n = 1$이며, $x = -1$이면 $(-1)^n$이 진동하고 $\lvert x\rvert > 1$이면 발산한다. 따라서 $(x^n)$은 $(-1, 1]$에서만 점별수렴하고, 극한함수는 이 집합 위에서만 정의된다. 이하에서는 수렴하는 점들의 집합을 $E$로 잡고 이야기한다.

## 연속성의 상실

::: 예시 2 (연속함수의 점별극한)
$E = [0,1]$에서 $f_n(x) = x^n$을 보자. 각 $f_n$은 연속이다. $x = 1$이면 $f_n(1) = 1$이므로 $f(1) = 1$이다. $x = 0$이면 $f_n(0) = 0$이다. $0 < x < 1$이면 $\varepsilon \in (0,1)$에 대해 $x^n < \varepsilon$인 조건은 양변에 로그를 취해

$$n \ln x < \ln \varepsilon \iff n > \frac{\ln \varepsilon}{\ln x}$$

이다. $\ln x < 0$이므로 부등호의 방향이 바뀌었고, 우변은 양수이다. 그러므로 $N$을 $\ln \varepsilon / \ln x$보다 큰 자연수로 고르면 $n \geq N$에서 $x^n \leq x^N < \varepsilon$이다. 따라서 점별극한은

$$f(x) = \begin{cases} 0, & 0 \leq x < 1,\\ 1, & x = 1 \end{cases}$$

이고, 이는 $x = 1$에서 불연속이다.
:::

위에서 고른 $N = N(x, \varepsilon)$은 $x \to 1^-$일 때 $\ln x \to 0^-$이므로 한없이 커진다. 실제로 $\varepsilon$을 고정하면 어떤 $N$도 모든 $x \in [0,1)$에 대해 동시에 통하지 않는다. $x = \varepsilon^{1/N}$으로 두면 $x < 1$이고 $x^N = \varepsilon$이어서 $x^N < \varepsilon$이 깨지기 때문이다. 수렴 속도가 점마다 달라지는 이 현상이 극한함수의 불연속을 만든다.

## 적분의 비교환

::: 예시 3 (적분과 극한의 불일치)
$E = [0,1]$에서 $f_n(x) = n^2 x e^{-nx}$를 보자. $f_n(0) = 0$이다. $x > 0$이면 $e^{nx} \geq (nx)^3/6$이므로

$$0 \leq f_n(x) = \frac{n^2 x}{e^{nx}} \leq \frac{6 n^2 x}{n^3 x^3} = \frac{6}{n x^2}$$

이고, 우변은 $n \to \infty$에서 $0$으로 간다. 따라서 점별극한은 $f \equiv 0$이다. 그러나 $F_n(x) = -(nx + 1)e^{-nx}$는 $F_n'(x) = n^2 x e^{-nx}$를 만족하는 원시함수이므로

$$\int_0^1 f_n(x)\dd{x} = F_n(1) - F_n(0) = 1 - (n+1)e^{-n}$$

이다. 따라서 $\lim_{n} \int_0^1 f_n = 1$이지만 $\int_0^1 \lim_{n} f_n = 0$이다.
:::

$f_n$은 $x = 1/n$에서 최댓값 $n/e$를 갖는다. 봉우리가 원점으로 다가가면서 높아지고, 고정된 $\delta > 0$에 대해

$$\int_\delta^1 f_n(x)\dd{x} = (n\delta + 1)e^{-n\delta} - (n+1)e^{-n} \to 0$$

이므로 적분 $1$의 거의 전부가 $[0,\delta)$에 몰려 있다. 각 점에서는 봉우리가 지나가고 나면 값이 $0$으로 가라앉아 점별극한에 아무 흔적도 남지 않지만, 적분은 그 봉우리의 넓이를 계속 기억한다. 계수 $n^2$을 $n$으로 바꾸면 적분이 $(1 - (n+1)e^{-n})/n \to 0$이 되어 반례가 사라진다. 봉우리의 폭이 $1/n$ 정도로 줄어드는 동안 넓이가 유지되려면 높이가 $n$의 비율로 커져야 하기 때문이다.

## 미분의 비교환

::: 예시 4 (도함수의 극한과 극한의 도함수)
$E = \mathbb{R}$에서 $f_n(x) = \sin(nx)/\sqrt{n}$을 보자. $\lvert f_n(x)\rvert \leq 1/\sqrt{n}$이므로 $\varepsilon > 0$에 대해 $N > \varepsilon^{-2}$으로 두면 $n \geq N$일 때 모든 $x$에서 $\lvert f_n(x)\rvert < \varepsilon$이다. 따라서 점별극한은 $f \equiv 0$이고 $f' \equiv 0$이다. 그러나

$$f_n'(x) = \sqrt{n}\cos(nx)$$

이고, $f_n'(0) = \sqrt{n} \to \infty$이다. 곧 $f_n'(0)$은 $f'(0) = 0$으로 수렴하지 않는다. $x = \pi$에서는 $f_n'(\pi) = (-1)^n \sqrt{n}$이어서 수렴하는 부분수열조차 없다.
:::

이 예시에서 $f_n$은 모든 점에서 같은 크기 $1/\sqrt{n}$ 이내로 $0$에 가까워지므로, 함수값의 수렴은 점별수렴보다 훨씬 좋은 형태로 일어난다. 그런데도 도함수가 수렴하지 않는 것은, 진폭을 줄이는 인자 $1/\sqrt{n}$이 진동수 $n$과 곱해져 기울기에서는 $\sqrt{n}$으로 커지기 때문이다. 따라서 함수열의 수렴만으로는 도함수열의 수렴에 대해 아무것도 알 수 없다.

## 극한 순서의 교환

세 가지 실패는 모두 두 극한을 어느 순서로 취하느냐의 문제로 쓸 수 있다. $f_n \to f$가 $E$에서 점별로 성립한다고 하자.

연속성부터 보자. 각 $f_n$이 $a \in E$에서 연속이면 $\lim_{x \to a} f_n(x) = f_n(a)$이고, $f_n(a) \to f(a)$이다. 그러므로

$$\lim_{n\to\infty}\Bigl(\lim_{x\to a} f_n(x)\Bigr) = f(a), \qquad \lim_{x\to a}\Bigl(\lim_{n\to\infty} f_n(x)\Bigr) = \lim_{x\to a} f(x)$$

이다. 따라서 $f$가 $a$에서 연속인 것은 이 두 반복극한이 같은 것과 동치이다. [예시 2](#ex2)에서 $a = 1$이면 첫째 값은 $1$이고, 둘째 값은 $\lim_{x\to 1^-} 0 = 0$이다.

적분은 Riemann 합의 극한이다. 구간 $[a,b]$의 표본점 달린 분할 $P$에 대한 Riemann 합을 $S(P, g)$라 하면, [\[미적분학\] §적분, ⁋정의 9](/ko/math/calculus/integration#def9)에서 보았듯 $\int_a^b g = \lim_{\lVert P\rVert \to 0} S(P, g)$이다. 합은 유한합이므로 고정된 $P$에서 $S(P, f_n) \to S(P, f)$이고, 따라서 $f_n$과 $f$가 모두 적분가능할 때

$$\int_a^b f = \lim_{\lVert P\rVert \to 0}\Bigl(\lim_{n\to\infty} S(P, f_n)\Bigr), \qquad \lim_{n\to\infty}\int_a^b f_n = \lim_{n\to\infty}\Bigl(\lim_{\lVert P\rVert \to 0} S(P, f_n)\Bigr)$$

이다. 극한과 적분을 바꿀 수 있다는 것은 이 두 반복극한이 같다는 것이다.

미분도 같은 모양이다. $a$를 포함하는 구간에서 $t \neq a$에 대해 $D_n(t) = (f_n(t) - f_n(a))/(t - a)$로 두면 $D_n(t) \to D(t) = (f(t) - f(a))/(t-a)$이고, [§미분, ⁋정의 1](/ko/math/analysis/differentiation#def1)의 도함수 정의로부터

$$f'(a) = \lim_{t\to a}\Bigl(\lim_{n\to\infty} D_n(t)\Bigr), \qquad \lim_{n\to\infty} f_n'(a) = \lim_{n\to\infty}\Bigl(\lim_{t\to a} D_n(t)\Bigr)$$

이다. 도함수와 극한을 바꿀 수 있다는 것도 두 반복극한이 같다는 뜻이다.

이 교환이 일반적으로 성립하지 않음은 이중수열에서 이미 드러난다.

::: 예시 5 (이중수열의 반복극한)
$a_{m,n} = m/(m+n)$ ($m, n \geq 1$)에 대해 $m$을 고정하면 $n \to \infty$에서 $a_{m,n} \to 0$이고, $n$을 고정하면 $m \to \infty$에서 $a_{m,n} = 1/(1 + n/m) \to 1$이다. 따라서

$$\lim_{m\to\infty}\Bigl(\lim_{n\to\infty} a_{m,n}\Bigr) = 0 \neq 1 = \lim_{n\to\infty}\Bigl(\lim_{m\to\infty} a_{m,n}\Bigr)$$

이다.
:::

[예시 2](#ex2)도 이 모양이다. $a_{m,n} = (1 - 1/m)^n$으로 두면 $n \to \infty$에서 $0$, $m \to \infty$에서 $1$로 가서 같은 불일치가 생긴다. 반복극한의 순서를 바꾸는 일이 정당화되려면 두 극한이 서로 독립적으로 일어난다는 보장이 필요하다. 점별수렴은 한 극한 안에서 $N$이 다른 변수에 의존하는 것을 허용하므로 이 보장을 주지 못한다.

반복극한을 거듭하면 연속함수에서 출발해도 연속성·적분가능성을 완전히 잃은 함수까지 닿을 수 있다.

::: 예시 6 (Dirichlet 함수)
$\mathbb{R}$에서 $g_{m}(x) = \lim_{n\to\infty}\cos^{2n}(m!\pi x)$를 정의하고 $d(x) = \lim_{m\to\infty} g_m(x)$를 생각하자. $m!x$가 정수이면 $\cos(m!\pi x) = \pm 1$이므로 $\cos^{2n}(m!\pi x) = 1$이다. 정수가 아니면 $\lvert\cos(m!\pi x)\rvert < 1$이므로 $\cos^{2n}(m!\pi x)$는 공비의 절댓값이 $1$보다 작은 등비수열이어서 $0$으로 간다. 그러므로

$$g_m(x) = \begin{cases} 1, & m!x \in \mathbb{Z},\\ 0, & m!x \notin \mathbb{Z} \end{cases}$$

이다. $x = p/q$가 유리수이면 $m \geq q$인 모든 $m$에서 $m!x$가 정수이므로 $g_m(x) = 1$이고, 따라서 $d(x) = 1$이다. $x$가 무리수이면 어떤 $m$에 대해서도 $m!x$가 정수가 아니므로 $g_m(x) = 0$이고 $d(x) = 0$이다. 결국 $d$는 유리수에서 $1$, 무리수에서 $0$인 Dirichlet 함수이며([§Riemann 적분, ⁋예시 9](/ko/math/analysis/riemann_integral#ex9)), 이는 모든 점에서 불연속이고 어떤 구간에서도 Riemann 적분가능하지 않다.
:::

연속함수 $\cos^{2n}(m!\pi x)$의 열을 한 번 극한 취한 $g_m$은 값이 $1$인 점이 $\frac{1}{m!}\mathbb{Z}$뿐이고 나머지에서는 $0$인, 비교적 순한 함수이지만, 이를 한 번 더 극한 취하면 이처럼 병적인 함수가 된다. 점별극한을 취할 때마다 정규성이 한 단계씩 깨질 수 있다.

따라서 연속성·적분·미분이 극한을 통과하려면 점별수렴보다 강한 조건이 필요하다. $N$을 $x$와 무관하게 잡을 수 있는지가 그 조건의 핵심이고, 이는 다음 글의 주제이다.

---

**참고문헌**

**[Rud]** W. Rudin, *Principles of mathematical analysis*, 3rd ed., McGraw-Hill, 1976.
